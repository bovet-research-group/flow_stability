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
`flowstab` is a Python package for detecting and analyzing communities in temporal networks, that is, networks whose connections change over time. Rather than aggregating interactions into static snapshots, it preserves the finest available temporal resolution of the data and implements the flow stability framework for dynamic community detection [@bovet_flow_2022]. The package is organized around two core components: a temporal-network component (`tempnet`) for representing and manipulating temporal network data, and a sparse-matrix component (`stochmat`) that accelerates the underlying computations and `pygenstability` [@arnaudon2024algorithm] for detecting scales. 


# Statement of need
Temporal networks model systems whose interactions change over time [@holme2012temporal], such as human contact patterns (who we meet), transportation flows (where  we go), research collaborations (with whom we collaborate), and digital communication through social media, phone calls, and text messages (with whom we communicate). They are represented as nodes (entities) joined by edges (interactions) that carry timing information (when the interaction happened and for how long). 

Analyses of such temporal networks typically begin at two scales. Local measures describe individual nodes and their neighborhoods, for example which other nodes a given node interacted within a period, or whether its connections close into triangles. Global measures characterize the network as a whole, for example the number of edges or active nodes per unit time, or whether activity is bursty or evenly spread over time. Yet, as in many areas of data analysis, neither the local nor the global view captures how a system is actually organized. That organization lives at the mesoscale, and one of main organization concepts is community structure [@lancichinetti2009community, @delvenne2010stability, @girvan2002community]: groups of nodes that interact more densely among themselves than with the rest of the network, such as a circle of friends within a school or a discipline within a collaboration network.

Detecting communities in temporal networks is therefore a central task, but most existing approaches reduce the temporal dimension before clustering, with a few exceptions of new developments [@brabant2025longitudinal]. They either aggregate interactions into static snapshots over fixed time windows and identify communities using static techniques and sticht them using evolution rules (instant-optimal), or they consider the network and the communities found in the previous step to identify communities in the current one (temporal trade off), These strategies underlie the dynamic community detection facilities in widely used libraries such as CDlib [@rossetti_cdlib_2019] and tnetwork [@tnetwork]. 

Such methods are powerful and general, but temporal aggregation discards the precise ordering of events, and the assumption of a stationary state does not hold for many real systems[@bovet_flow_2022]. Crucially, aggregation also breaks the notion of a temporal path. If node $u$ contacts $v$ at time $t_1$ and $v$ contacts $w$ at a later time $t_2$, then information can flow from $u$ to $w$ through $v$; but if $v$-$w$ occurs before $u$-$v$, no such flow is possible. A static aggregation collapses both cases into the same connected triple, representing a path that may never have existed.

The flow stability framework [@bovet_flow_2022] takes a different route. By exending the Markov stability framework [@delvenne2010stability], it employs a continuous-time random-walk process that evolves on the temporal network and is constrained by its activation pattern, so that the full ordering of interactions is preserved at the finest available resolution rather than aggregated away. Because the temporal evolution can induce asymmetric relationships between nodes (as stated before as the notion of `asymmetry of temporal paths`), the method yields two partitions for any time interval, a forward and a backward partition, and reveals distinct scales representing the dynamics, from finer to coarser community structure, by varying the rate of the random walk. 

Despite the method's adoption since its publication, the existing implementation was not easy to use. Here, by introducing `flowstab`, an installable, documented, and continuously tested Python implementation of the flow stability framework, we fill this gap and lower the barrier for researchers in network science, computational social science, science of science, and related fields to apply the method to their own temporal data.

# Implementation

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


