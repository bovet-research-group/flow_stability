---
title: "`flowstab` - Flow Stability for Dynamic Community Detection"
tags:
- data science
- Python
- Temporal Network
- Community Detection
authors:

- name: Yasaman Asgari
  orcid: 0000-0002-5397-0778
  corresponding: true
  affiliation: "1"

- name: Juni Schindler
  orcid: 0000-0002-8728-9286
  affiliation: "1"

- name: Samuel Koovely 
  orcid: 0000-0002-5033-7790
- name: Alexandre Bovet
  orcid: 0000-0003-3937-3704
  corresponding: true
  affiliation: "1"

- name: Jonas I. Liechti
  orcid: 0000-0003-3447-3060
  affiliation: "2"

affiliations:
 - name: Department of Mathematical Modeling and Machine Learning, University of Zurich, Zürich, Switzerland
   index: 1
 - name: www.T4D.ch, T4D GmbH, Zurich, Switzerland
   index: 2
date: 22. June 2026
bibliography: paper.bib
---
# Summary
`flowstab` is a Python package for detecting and analyzing communities in temporal networks, that is, networks whose connections change over time. Rather than aggregating interactions into static snapshots, it preserves the finest available temporal resolution of the data and implements the flow stability framework for dynamic community detection [@bovet_flow_2022]. The package is organized around two core components: a temporal-network component (`tempnet`) for representing and manipulating temporal network data, and a sparse-matrix component (`stochmat`) that accelerates the underlying computations.

# Statement of need

... 

In summary, `flowstab` ...

# Implementation
...

# Validation and Testing

A comprehensive set of documented case studies has been published to validate the `abn` package (see the `abn` [website](https://r-bayesian-networks.org/)).
The numerical accuracy and quality assurance exercises were demonstrated in @kratzer_additive_2023.
A rigorous testing and linting procedure is implemented based on the `pytest` and `ruff` packages [@pytest8.3,@cite_ruff].
The procedure is tiede to the development and release cycle through continuous integration pipelines thus asserting no untested changes are inserted into the code base.
Additional documentation and resources are available on the `abn` [website](https://r-bayesian-networks.org/) for further reference and guidance.
An extended documentation and further resources (including and automated documentation of the code-base) are available on the 'flowstab` [website](https://flow-stability.readthedocs.io).

# Availability

The source code of `flowstab` is publicly [available on GitHub](https://github.com/alexbovet/flow_stability).
The package can be installed directly from GitHub with `pip`:

```bash
pip install git+https://github.com/alexbovet/flow_stability.git
```
Alternatively, `flowstab` is also available on [PyPi](https://pypi.org).




# Acknowledgments


# AI usage disclosure
No generative AI tools were used in the development of this software.
AI-assisted tools were used to format some of the source code docstrings
and to support the drafting of portions of this manuscript, which were
subsequently reviewed and edited by the authors.

# References


