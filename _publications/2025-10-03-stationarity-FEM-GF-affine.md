---
title: "The Lax–Wendroff theorem for Patankar-type methods applied to hyperbolic conservation laws"
collection: publications
permalink: /publication/2025-10-03-stationarity-FEM-GF-affine
excerpt: 'We generalize the Lax-Wendroff theorem for Patankar-type schemes.'
date: 2025-10-03
venue: 'ArXiv'
paperurl: 'https://arxiv.org/pdf/2505.08387'
arxiv: 'https://arxiv.org/pdf/2505.08387'
citation: 'Bender, J., Izgin, T., Offner, Ph. and Torlo, D. (2025), The Lax–Wendroff theorem for Patankar-type methods applied to hyperbolic conservation laws. Computers and Fluids, 2505.'
pdf: /files/publications/barsukow2025stationarity.pdf
bib: /files/publications/bib/barsukow2025stationarity_FEM_GF_affine.bib
---
We consider linear, hyperbolic systems of balance laws in several space dimensions. They possess non-trivial steady states, which result from the equilibrium between derivatives of the unknowns in different directions, and the sources. Standard numerical methods fail to account for this equilibrium, and include stabilization that destroys it. This manifests itself in a diffusion of states that are supposed to remain stationary. We derive new stabilized high-order Finite Element methods based on a Global Flux quadrature: we reformulate the entire spatial operator as a mixed derivative of a single quantity, referred to as global flux. All spatial derivatives and the sources are thus treated simultaneously, and our methods are stationarity preserving. Additionally, when this formulation is combined with interpolation on Gauss-Lobatto nodes, the new methods are super-convergent at steady state. Formal consistency estimates, and strategies to construct well-prepared initial data are provided. The numerical results confirm the theoretical predictions, and show the tremendous benefits of the new formulation.
