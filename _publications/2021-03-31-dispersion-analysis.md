---
title: "Spectral analysis of continuous FEM for hyperbolic PDEs: influence of approximation, stabilization, and time-stepping"
collection: publications
permalink: /publication/2021-03-31-dispersion-analysis
excerpt: 'In this paper, we study different high order FEM methods for hyperbolic problems, providing parameters that lead to stable and reliable schemes. [Download paper](/files/publications/Michel2021Spectral.pdf)'
date: 2021-03-31
venue: 'Journal of Scientific Computing'
paperurl: 'https://doi.org/10.1007/s10915-021-01632-7'
citation: 'Michel, S., Torlo, D., Ricchiuto, M. and Abgrall, R.. Spectral Analysis of Continuous FEM for Hyperbolic PDEs: Influence of Approximation, Stabilization, and Time-Stepping. J Sci Comput 89, 31 (2021). https://doi.org/10.1007/s10915-021-01632-7'
pdf: /files/publications/Michel2021Spectral.pdf
---
This is a work in collaboration with Sixtine Michel, [Mario Ricchiuto](https://team.inria.fr/cardamom/marioricchiuto/) and [Rémi Abgrall](https://www.math.uzh.ch/index.php?id=people&key1=8882).

We study continuous finite element dicretizations for one dimensional hyperbolic partial differential equations. The main contribution of the paper is to provide a fully discrete spectral analysis, which is used to suggest optimal values of the CFL number and of the stabilization parameters involved in different types of stabilization operators. In particular, we analyze the streamline-upwind Petrov-Galerkin (SUPG) stabilization technique, the continuous interior penalty (CIP) stabilization method and the local projection stabilization (LPS). Three different choices for the continuous finite element space are compared: Bernstein polynomials, Lagrangian polynomials on equispaced nodes, and Lagrangian polynomials on Gauss-Lobatto cubature nodes. For the last choice, we only consider inexact quadrature based on the formulas corresponding to the degrees of freedom of the element, which allows to obtain a fully diagonal mass matrix. We also compare different time stepping strategies, namely Runge-Kutta (RK), strong stability preserving RK (SSPRK) and deferred correction time integration methods. The latter allows to alleviate the computational cost as the mass matrix inversion is replaced by the high order correction iterations. To understand the effects of these choices, both time-continuous and fully discrete Fourier analysis are performed. These allow to compare all the different combinations in terms of accuracy and stability, as well as to provide suggestions for optimal values discretization parameters involved. The results are thoroughly verified numerically both on linear and non-linear problems, and error-CPU time curves are provided. Our final conclusions suggest that cubature elements combined with SSPRK and CIP or LPS stabilization are the most promising combinations.

[DOI https://doi.org/10.1007/s10915-021-01632-7](https://doi.org/10.1007/s10915-021-01632-7)

[Arxiv page](https://arxiv.org/abs/2103.16158)

[Paper PDF](/files/publications/Michel2021Spectral.pdf)

![Dispersion analysis](/images/research/dispersionAnalysis.png)
