---
title: "Stationarity preserving nodal Finite Element methods for multi-dimensional linear hyperbolic balance laws via a Global Flux quadrature formulation"
collection: publications
permalink: /publication/2025-10-03-stationarity-FEM-GF-affine
excerpt: 'We extend the finite element global flux to a vast set of linear problems with source terms that have numerous nontrivial equilibria. The method is able to preserve an accurate approximation of the steady states with a super-convergent behavior.'
date: 2025-10-03
venue: 'ArXiv'
paperurl: 'https://arxiv.org/pdf/2510.02928'
arxiv: 'https://arxiv.org/pdf/2510.02928'
citation: 'Barsukow, W. and Ricchiuto, M. and Torlo, D. (2025), Stationarity preserving nodal Finite Element methods for multi-dimensional linear hyperbolic balance laws via a Global Flux quadrature formulation, arXiv:2510.02928.'
pdf: /files/publications/barsukow2025stationarity.pdf
bib: /files/publications/bib/barsukow2025stationarity_FEM_GF_affine.bib
---
We consider linear, hyperbolic systems of balance laws in several space dimensions. They possess non-trivial steady states, which result from the equilibrium between derivatives of the unknowns in different directions, and the sources. Standard numerical methods fail to account for this equilibrium, and include stabilization that destroys it. This manifests itself in a diffusion of states that are supposed to remain stationary. We derive new stabilized high-order Finite Element methods based on a Global Flux quadrature: we reformulate the entire spatial operator as a mixed derivative of a single quantity, referred to as global flux. All spatial derivatives and the sources are thus treated simultaneously, and our methods are stationarity preserving. Additionally, when this formulation is combined with interpolation on Gauss-Lobatto nodes, the new methods are super-convergent at steady state. Formal consistency estimates, and strategies to construct well-prepared initial data are provided. The numerical results confirm the theoretical predictions, and show the tremendous benefits of the new formulation.
