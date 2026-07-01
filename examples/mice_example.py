"""
Flow stability on the mouse contact network
============================================

This example walks through a full forward/backward flow-stability analysis on a
temporal network of mouse contacts, using the :class:`FlowStability`
interface from ``flowstab``.

The :class:`FlowStability` object is *stateful*: it knows which step comes next
and can tell you how to run it. Throughout the example we explicitly use that by
calling :meth:`fs.help` (and inspecting :attr:`fs.state`) after each step.

.. note::

"""

# %%
# Imports and data download
# -------------------------
#
# We download the mouse contact sequence and the per-animal sex annotation from
# Zenodo. ``contact_sequence`` is an event table with one row per contact and
# columns for the start/end times and the two nodes involved.

import gc

import numpy as np
import pandas as pd
import tempfile
from pathlib import Path
from zenodo_get import download
from flowstab.flow_stability import FlowStability


RECORD_ID = "4725155"
FILE_NAME = "mice_contact_sequence.csv.gz"

with tempfile.TemporaryDirectory() as tmpdir:
    download(
        record_or_doi=RECORD_ID,
        output_dir=tmpdir,
        file_glob=FILE_NAME,
    )
    event_table = pd.read_csv(Path(tmpdir) / FILE_NAME, compression="gzip")


# %%
# Set up the flow-stability analysis
# ----------------------------------
#
# Now we pass the whole table to :class:`FlowStability`. We restrict ourselves to first
# 30 minutes of the interactions by setting the `t_stop=1800`. 

fs = FlowStability(t_start=None, t_stop=180)
fs.set_temporal_network(events_table=event_table, relabel_nodes=True)

n_nodes = fs.temporal_network.num_nodes

# %%
# The object tracks where we are in the analysis. At any point we can ask what
# to do next and how to do it. ``fs.state.next`` returns
# ``(required_parameters, next_method)`` and ``fs.help()`` prints same information. 

print(fs.state.next)
fs.help("compute_laplacian_matrices")

# %%
# Compute the Laplacian matrices
# ------------------------------
#
# The first step builds the Laplacian matrices of the inter-event
# transition process. 

fs.compute_laplacian_matrices()
print(fs.state.next)


# %%
# Choose the time scales
# ----------------------
#
# Flow stability is computed at a range of *time scales* :math:`\tau` (the
# characteristic time the random walker is allowed to flow). Small :math:`\tau`
# resolves fine, transient communities; large :math:`\tau` reveals coarse,
# persistent structure.
#
# :meth:`fs.set_time_scale` forwards keyword arguments straight to
# :func:`numpy.logspace`, so we can define a logarithmic sweep in one call. Note
# that ``flowstab`` parametrises everything by the time scale :math:`\tau`; the
# inverse :math:`\lambda = 1/\tau` (sometimes called the "scale") is only used
# for plotting.

min_scale = -7
max_scale = 2
n_scale = 10
scales = np.logspace(min_scale, max_scale, n_scale)
taus = 1 / scales
fs.set_time_scale(taus)



# %%
# Compute the inter-transition matrices
# -------------------------------------
#
# This propagates the random walk over the chosen time scales. The state machine
# again tells us this is the right next step.

print(fs.state.next)

# %%
# Which method to use for the matrix exponential?
# ----------------------
#
indices=fs.temporal_network.plot_density_of_laplacians()
fs.temporal_network.print_report(
    indices, scales,
    method_kwargs={
        'mfp_exp': {'err': 1e-6},
        'parallel_expm': {'nproc': 4, 'normalize_rows': True},
    },
)
# %%
# Compute the inter-transition matrices
# ----------------------
#
fs.compute_inter_transition_matrices(method="mfp_exp", err=1e-6)

# %%
# Set the time direction
# ----------------------
#
# ``time_direction`` selects which flow integrals are built in the next step:
#
# * ``1``  -> forward in time only,
# * ``-1`` -> backward in time only,
# * ``0``  -> both directions (what we want here, to compare forward vs.
#   backward communities).

fs.time_direction = 0
print(fs.state.next)
# %%
# Build the flow integrals
# ------------------------
#
# :meth:`set_flow_clustering` builds, for every time scale, a
# :class:`FlowIntegralClustering` object holding the *integral of the
# autocovariance* of the flow. It does **not** yet run any community detection:
# it only prepares the quantity that the Louvain step will subsequently
# optimise.
fs.help("set_flow_clustering")
fs.set_flow_clustering()
fs._temporal_network.inter_T = None
gc.collect()

# %%
# Find the communities
# --------------------


# %%
# Stability, number of clusters and robustness across time scales
# ---------------------------------------------------------------
#

