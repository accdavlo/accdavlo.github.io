---
title: "Optimisation–Based Coupling of Finite Element Model and Reduced Order Model for Computational Fluid Dynamics"
collection: publications
permalink: /publication/2024-02-15-optimization-ROM-FOM-comparison
excerpt: "In the context of domain decomposition optimization based models, we compare different couplings of full and reduced order models of each subcomponent."
date: 2024-02-15
venue: 'arXiv preprint'
paperurl: 'https://arxiv.org/abs/2402.10570'
arxiv: 'https://arxiv.org/abs/2402.10570'
citation: "I. Prusak, D. Torlo, M. Nonino and G. Rozza. &quot;Optimisation–Based Coupling of Finite Element Model and Reduced Order Model for Computational Fluid Dynamics.&quot; (2024) <i>arXiv preprint</i>, arXiv:2402.10570."
pdf: /files/publications/prusak2024optimizationbased.pdf
bib: /files/publications/bib/prusak2024optimizationbased.bib
---
With the increased interest in complex problems, such as multiphysics
and multiscale models, as well as real–time computations, there is a strong need
for domain–decomposition (DD) segregated solvers and reduced–order models
(ROMs). Segregated models decouple the subcomponents of the problems at hand
and use already existing state–of–the–art numerical codes in each component. In
this manuscript, starting with a DD algorithm on non–overlapping domains, we aim
at the comparison of couplings of different discretisation models, such as Finite
Element (FEM) and ROM for separate subcomponents. In particular, we consider
an optimisation–based DD model on two non–overlapping subdomains where the
coupling on the common interface is performed by introducing a control variable
representing a normal flux. Gradient-based optimisation algorithms are used to con-
struct an iterative procedure to fully decouple the subdomain state solutions as
well as to locally generate ROMs on each subdomain. Then, we consider FEM or
ROM discretisation models for each of the DD problem components, namely, the
triplet state1–state2–control. We perform numerical tests on the backward–facing
step Navier-Stokes problem to investigate the efficacy of the presented couplings in
terms of optimisation iterations and relative errors.
