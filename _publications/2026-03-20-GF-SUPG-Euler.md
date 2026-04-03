---
title: "Arbitrary order stationarity preserving stabilized finite elements for multidimensional nonlinear hyperbolic problems. Application to the Euler equations with gravity"
collection: publications
permalink: /publication/2026-03-20-GF-SUPG-Euler
excerpt: 'We extend the finite element global flux to Euler equations of gas-dynamics to preserver numerous nontrivial multidimensional equilibria, also with gravity source terms. The method is able to preserve an accurate approximation of the steady states with a super-convergent behavior.'
date: 2026-03-20
venue: 'ArXiv'
paperurl: 'https://arxiv.org/pdf/2603.23185'
arxiv: 'https://arxiv.org/pdf/2603.23185'
citation: 'Ziggaf, M. and Torlo, D. and Ricchiuto, M. (2026), Arbitrary order stationarity preserving stabilized finite elements for multidimensional nonlinear hyperbolic problems. Application to the Euler equations with gravity, arXiv:2603.23185.'
pdf: /files/publications/ziggaf2026euler.pdf
bib: /files/publications/bib/ziggaf2026euler.bib
---
We develop arbitrarily high-order, stationarity-preserving stabilized finite element methods for multidimensional nonlinear hyperbolic balance laws on Cartesian grids. We aim at approximating all the steady states of the problem at hand, including non-trivial genuinely multidimensional equilibria, with a level of accuracy higher than the nominal one of the underlying scheme. We formalize more precisely the meaning of stationarity preservation, providing some technical conditions for its realizability. We then recast the multidimensional global-flux quadrature of Barsukow et al. (Num. Meth. PDEs, 2025) as a local preprocessing of the physical fluxes that maps continuous polynomial vector fields to a local space with Raviart–Thomas-type structure. Both the Galerkin and SUPG formulations are recast in this setting. The resulting methods extend the stationarity-preserving finite-volume approach of Barsukow et al. (J. Comput. Phys., 2026) to high-order continuous finite elements and Barsukow et al. (Num. Meth. PDEs, 2025) to nonlinear balance laws. We analyze key properties of the proposed schemes, including local conservation and nodal superconvergence of the discrete steady kernel, and we discuss their relation to low-Mach-compliant discretizations.
We apply the framework to the compressible Euler equations with gravity. A simple source-term reformulation yields machine-precision preservation of isothermal hydrostatic equilibria. Extensive numerical benchmarks, including moving equilibrium, near-equilibrium, and instability-dominated regimes, demonstrate clear improvements in robustness and accuracy over standard SUPG and reference finite-volume methods.
