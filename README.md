## flowstab - Flow stability for dynamic community detection
Python package for the dynamic community detection in temporal networks implementing the flow stability framework described in 

Alexandre Bovet, Jean-Charles Delvenne & Renaud Lambiotte,
[Flow stability for dynamic community detection](https://www.science.org/doi/10.1126/sciadv.abj3063),
Sci. Adv., 8 (19), eabj3063. DOI: 10.1126/sciadv.abj3063

<!--- quickstart --->
## Requirements
- **Python** - Supported versions: [![Python 3.14](https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/j-i-l/809edea020e4ae8a8ffb82e5cfc2e69f/raw/flowstab-python-3.14.json)](https://github.com/bovet-research-group/stochmat/actions/workflows/status.yml) [![Python 3.13](https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/j-i-l/809edea020e4ae8a8ffb82e5cfc2e69f/raw/flowstab-python-3.13.json)](https://github.com/bovet-research-group/stochmat/actions/workflows/status.yml) [![Python 3.12](https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/j-i-l/809edea020e4ae8a8ffb82e5cfc2e69f/raw/flowstab-python-3.12.json)](https://github.com/bovet-research-group/stochmat/actions/workflows/status.yml) [![Python 3.11](https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/j-i-l/809edea020e4ae8a8ffb82e5cfc2e69f/raw/flowstab-python-3.11.json)](https://github.com/bovet-research-group/stochmat/actions/workflows/status.yml) [![Python 3.10](https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/j-i-l/809edea020e4ae8a8ffb82e5cfc2e69f/raw/flowstab-python-3.10.json)](https://github.com/bovet-research-group/stochmat/actions/workflows/status.yml)
- pandas
- scipy
- numpy
- MKL support (optional): see [MKL acceleration](#optional-mkl-acceleration) below

## Installation

You can pip install `flowstab` directly from this repository into your virtual
environment. Simply run:

    pip install git+https://github.com/alexbovet/flow_stability.git

### Optional: MKL acceleration

For optimal performance with large sparse matrices, install Intel MKL first:

**Ubuntu/Debian:**

    sudo apt-get update
    sudo apt-get install intel-mkl

**macOS (via Homebrew):**

    brew install intel-mkl

Then install `flowstab` with the `[mkl]` extra:

    pip install "flowstab[mkl] @ git+https://github.com/bovet-research-group/flow_stability.git"

> **`flowstab[mkl]` is a hard runtime dependency.** It pulls `stochmat[mkl]`, which
> requires Intel MKL shared libraries to be loadable at runtime. `import flowstab`
> will raise `ImportError` if `sparse_dot_mkl` is installed but MKL libs are missing.
> If you do not need MKL, install plain `flowstab` and SciPy will be used as a
> transparent fallback.

To verify the MKL backend is active after installation:

```python
import stochmat
print(stochmat.backends.summary())
# {'cython_sparse_stoch': True, 'fast': True, 'mkl': True}
```

## Usage

After installation you can access the relevant classes and methods by importing
`flowstab` into your python scripts or via command line (see [CLI scripts](#cli-scripts) for details).

The easiest approach to use `flowstab` is with the `FlowStability` class that will provide you with contextual inforamtion, if needed:

```python
from flowstab.flow_stability import FlowStability
fs = FlowStability()
# check what to do next
fs.state.next
# Out[3]: ([], 'set_temporal_network')
# > you need to run `set_temporal_network` - how should this be done:
fs.state.howto['set_temporal_network']
# print(fs.state.howto['set_temporal_network'])
# 
#         Set the temporal network for the flow stability analysis.
# 
#         Parameters
#         ----------
#         **kwargs : dict
#             Arguments to initialize a ContTempNetwork instance.
#         ...
fs.set_temporal_network(events_table="my_contacts.csv")
fs.state.next
# Out[6]: ([], 'compute_laplacian_matrices')
fs.compute_laplacian_matrices()
fs.state.next
# Out[8]: (['time_scale'], 'compute_inter_transition_matrices')
# So we need to set `time_scale` next, but how?
print(fs_mice.state.howto['time_scale'])
# Set the time scale(s) for the random walk's transition rate.
# 
# .. note::
#     You might also use `set_time_scale` to directly create a range of
#     time scales.
# 
# Parameters
# ----------
# time_scale : None, int, float, or iterator of float
#     If None, a default value is used.
#     If an int or float, a single time scale is set.
#     If an iterator, it must yield float or int values.
# 
# ...
fs.set_time_scale(10)
fs.state.next
# Out[11]: ([], 'compute_inter_transition_matrices')
fs.compute_inter_transition_matrices()
fs.time_direction = 0  # perform both forward and backard
fs.set_flow_clustering()
fs.find_louvain_clustering()
fs.flow_clustering_backward
# Out[17]: {10: <flowstab.network_clustering.FlowIntegralClustering at 0x7fef57a7fd00>}
```

Alternatively, you can use individual elements from the `flowstab` package directly.
For example, if you want to use the `FlowIntegralClustering` class, you would
want to add the following line in your script:

```python

from flowstab.network_clustering import FlowIntegralClustering

# forw_flow = FlowIntegralClustering(...
```

Refer to the [examples](./examples/) folder more detailed usage examples.

### CLI scripts

`flowstab` also provides several command line hooks that can be run
directly in the terminal after installation, without the need to open a
python shell:

**run\_clusterings**

This command requires MKL support. See [Optional: MKL acceleration](#optional-mkl-acceleration) for installation instructions.

**run\_cov\_integrals**

**run\_laplacians\_transmats**

## Content

The main classes are:
- `ContTempNetwork` in the module `temporal_network` which is used to store and save temporal networks and to compute inter-event transition matrices.
- `FlowIntegralClustering` in the sub-module `network_clustering` which is used to computed the flow stability (integral of covariance) and to find the best forward and backward partition using the Louvain algorithm.

Additional interesting classes and functions are:
- `Clustering` and `SparseClustering` in the `network_clustering` sub-module can be used to directly cluster covariances or integrals of covariances.
- `static_clustering` in `network_clustering` is a helper function to cluster static networks using Markov Stability.
- `run_multi_louvain` in `network_clustering` helper function to run the Louvain multiple times on the same covariance in order to check the robustness of the partition.
- `avg_norm_var_information` in `network_clustering` computes the average Normalized Variation of Information of list of cluster lists obtained with `run_multi_louvain`.
- `compute_parallel_clustering` in `parallel_clustering`, same than `run_multi_louvain` but in parallel.
- the `parallel_expm` module contains functions to compute the matrix exponential of very large matrices using different strategies.

A jupyter notebook reproducing the example from Fig. 2 of the paper is available in [`asymmetric_example.ipynb`](https://github.com/alexbovet/flow_stability/blob/main/asymmetric_example.ipynb).


[![DOI](https://zenodo.org/badge/330739659.svg)](https://zenodo.org/badge/latestdoi/330739659)


