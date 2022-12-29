---
title: "Model order reduction strategies for weakly dispersive waves"
collection: publications
permalink: /publication/2022-12-23-mor-dispersive
excerpt: 'Water waves can be approximated with different models. Dispersive-hyperbolic models serve this scope under smallness conditions of nonlinearity and shallowness parameters. The discretization of these models consists often of a hyperbolic system coupled with an elliptic system. In this work we reduce with standard model order reduction techniques the elliptic operator. Finally, we apply some hyperreduction to reduce the whole system. [Download paper](/files/publications/Torlo2021mor-dispersive-waves-1D.pdf)'
date: 2022-12-23
venue: 'Mathematics and Computers in Simulation'
paperurl: 'https://doi.org/10.1016/j.matcom.2022.10.034'
citation: 'D. Torlo and M. Ricchiuto. &quot;Model order reduction strategies for weakly dispersive waves. &quot; <i>Mathematics and Computers in Simulation</i>, (205), pages 997-1028, 2023.'
pdf: /files/publications/Torlo2021mor-dispersive-waves-1D.pdf
bib: /files/publications/bib/torlo2021model.bib
---
This is a work in collaboration with Mario Ricchiuto.

We focus on the numerical modelling of water waves by means of depth averaged models. We
consider in particular PDE systems which consist in a nonlinear hyperbolic model plus a linear dispersive perturbation involving an elliptic operator. We propose two strategies to construct reduced
order models for these problems, with the main focus being the control of the overhead related to
the inversion of the elliptic operators, as well as the robustness with respect to variations of the flow
parameters. In a first approach, only a linear reduction strategies is applied only to the elliptic component, while the computations of the nonlinear fluxes are still performed explicitly. This hybrid
approach, referred to as pdROM, is compared to a hyper-reduction strategy based on the empirical
interpolation method to reduce also the nonlinear fluxes. We evaluate the two approaches on a variety
of benchmarks involving a generalized variant of the BBM-KdV model with a variable bottom, and
a one-dimensional enhanced weakly dispersive shallow water system. The results show the potential
of both approaches in terms of cost reduction, with a clear advantage for the pdROM in terms of
robustness, and for the EIMROM in terms of cost reduction.

![KdV MOR](/images/research/KdVMORcompress.gif)

[Article link](https://doi.org/10.1016/j.matcom.2022.10.034)

[Download paper](/files/publications/Torlo2021mor-dispersive-waves-1D.pdf)

[Arxiv page](https://arxiv.org/abs/2112.10608)

