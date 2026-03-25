import numpy as np
import pytest
from scipy import sparse

# Assuming the functions are imported from the compiled cython module.
# For testing the transition, both should be temporarily accessible.
from flowstab._cython_sparse_stoch import (
    _cython_inplace_csr_row_normalize_triu,
    cython_inplace_csr_row_normalize_triu
)

def pure_python_normalize_triu(A_csr: sparse.csr_matrix, row_sum: np.ndarray) -> None:
    """
    Pure Python implementation of the upper-triangular normalization logic.
    Serves as the immutable mathematical baseline.
    """
    n_row = A_csr.shape[0]
    
    for k in range(n_row):
        if row_sum[k] != 0.0:
            # Recompute diagonal and column sums in each outer iteration
            diag = A_csr.diagonal()
            col_sum = A_csr.sum(axis=0).A1  # Equivalent to A.T @ 1
            
            for i in range(k, n_row):
                row_sum_tmp = row_sum[i] + diag[i] - col_sum[i]
                
                row_start = A_csr.indptr[i]
                row_end = A_csr.indptr[i + 1]
                sum_row = np.sum(A_csr.data[row_start:row_end])
                
                if sum_row != 0.0:
                    A_csr.data[row_start:row_end] /= (sum_row / row_sum_tmp)


@pytest.fixture
def random_triu_matrix():
    """Generates a strictly positive, upper-triangular CSR matrix."""
    np.random.seed(42)
    n = 15
    
    # Generate dense matrix and extract upper triangle
    A_dense = np.random.rand(n, n)
    A_dense = np.triu(A_dense)
    
    # Introduce sparsity
    A_dense[A_dense < 0.5] = 0.0
    
    # Guarantee no empty rows on the diagonal to satisfy the algorithm's constraints
    np.fill_diagonal(A_dense, np.random.rand(n) + 0.1)
    
    A_csr = sparse.csr_matrix(A_dense)
    
    # Cython typed memoryviews `long long[:]` mandate np.int64 buffers
    A_csr.indptr = A_csr.indptr.astype(np.int64, copy=False)
    A_csr.indices = A_csr.indices.astype(np.int64, copy=False)
    
    # Target normalization vector
    row_sum = np.random.rand(n) + 0.5
    
    return A_csr, row_sum


def test_cython_inplace_csr_row_normalize_triu_equivalence(random_triu_matrix):
    """
    Asserts exact mathematical equivalence between the legacy _sparsetools implementation,
    the new manual Cython pass, and the pure Python baseline.
    """
    A_csr, row_sum = random_triu_matrix
    n_row, n_col = A_csr.shape
    
    # Isolate memory buffers for each algorithm
    A_legacy = A_csr.copy()
    A_new = A_csr.copy()
    A_python = A_csr.copy()
    
    # SciPy's .copy() dynamically downcasts 'indptr' and 'indices' to int32 
    # if the matrix is small. We must enforce 64-bit integers (long long) AFTER copying.
    for mat in (A_legacy, A_new):
        mat.indptr = mat.indptr.astype(np.int64)
        mat.indices = mat.indices.astype(np.int64)
    
    # 1. Execute Legacy Implementation
    _cython_inplace_csr_row_normalize_triu(
        A_legacy.data, A_legacy.indptr, A_legacy.indices, 
        n_row, n_col, row_sum.copy()
    )
    
    # 2. Execute New Implementation
    cython_inplace_csr_row_normalize_triu(
        A_new.data, A_new.indptr, A_new.indices, 
        n_row, n_col, row_sum.copy()
    )
    
    # 3. Execute Pure Python Baseline
    pure_python_normalize_triu(A_python, row_sum.copy())
    
    # Assertion 1: New Cython matches Pure Python Baseline
    np.testing.assert_allclose(
        A_new.toarray(), 
        A_python.toarray(),
        err_msg="New Cython implementation deviates from the pure Python mathematical baseline."
    )
    
    # Assertion 2: New Cython matches Legacy Cython
    np.testing.assert_allclose(
        A_new.toarray(), 
        A_legacy.toarray(),
        err_msg="New Cython implementation deviates from the legacy _sparsetools version."
    )

@pytest.fixture
def large_triu_matrix():
    """Generates a large matrix to strictly evaluate memory allocations."""
    np.random.seed(42)
    n = 2000  # Large enough to show allocation differences, small enough for fast CI
    
    # Generate sparse data
    A_dense = np.triu(np.random.rand(n, n))
    A_dense[A_dense < 0.9] = 0.0  # 10% density
    np.fill_diagonal(A_dense, np.random.rand(n) + 0.1)
    
    A_csr = sparse.csr_matrix(A_dense)
    
    # Pre-cast to 64-bit to avoid casting allocations inside the test
    A_csr.indptr = A_csr.indptr.astype(np.int64)
    A_csr.indices = A_csr.indices.astype(np.int64)
    
    row_sum = np.random.rand(n) + 0.5
    
    return A_csr, row_sum

def test_legacy_triu_normalization_memory(large_triu_matrix):
    A_csr, row_sum = large_triu_matrix
    n_row, n_col = A_csr.shape
    
    # We copy here so the base fixture remains immutable.
    # Memray will record this copy, but we are looking at the peak/allocations 
    # of the function itself in the flamegraph.
    A_legacy = A_csr.copy()
    A_legacy.indptr = A_legacy.indptr.astype(np.int64)
    A_legacy.indices = A_legacy.indices.astype(np.int64)
    
    _cython_inplace_csr_row_normalize_triu(
        A_legacy.data, A_legacy.indptr, A_legacy.indices, 
        n_row, n_col, row_sum.copy()
    )

def test_new_triu_normalization_memory(large_triu_matrix):
    A_csr, row_sum = large_triu_matrix
    n_row, n_col = A_csr.shape
    
    A_new = A_csr.copy()
    A_new.indptr = A_new.indptr.astype(np.int64)
    A_new.indices = A_new.indices.astype(np.int64)
    
    cython_inplace_csr_row_normalize_triu(
        A_new.data, A_new.indptr, A_new.indices, 
        n_row, n_col, row_sum.copy()
    )
