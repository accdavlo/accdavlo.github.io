---
title: "Arbitrary High Order WENO Finite Volume Scheme with Flux Globalization for Moving Equilibria Preservation"
collection: publications
permalink: /publication/2022-05-27-global-flux
excerpt: 'We introduce arbitrary high order WENO finite volume schemes with global fluxes. The global flux includes the integral of the source term, so that it is natural to balance the moving equilibria for this kind of schemes. We show for shallow water equations with bathymetry that we can exactly preserve the discharge for moving steady states. Morover, we can apply a correction to be also well-balanced with respect to the lake at rest steady state.    [Download paper](/files/publications/Ciallella2022globalFlux.pdf)'
date: 2022-05-27
venue: 'arXiv preprint'
paperurl: 'https://arxiv.org/abs/2205.13315'
citation: 'M. Ciallella, D. Torlo and M. Ricchiuto. (2022). &quot;Arbitrary High Order WENO Finite Volume Scheme with Flux Globalization for Moving Equilibria Preservation. &quot; <i>arXiv preprint</i>, 2022. https://arxiv.org/abs/2205.13315.'
pdf: /files/publications/Ciallella2022globalFlux.pdf
bib: /files/publications/bib/ciallella2022global.bib
---
This is a work in collaboration with Mirco Ciallella and Mario Ricchiuto.

In the context of preserving stationary states, e.g. lake at rest and moving equilibria, a new formulation of the shallow water system, called Flux Globalization has been introduced by Cheng et al. (2019). This approach consists in including the integral of the source term in the global flux and reconstructing the new global flux rather than the conservative variables. The resulting scheme is able to preserve a large family of smooth and discontinuous steady state moving equilibria. In this work, we focus on an arbitrary high order WENO Finite Volume (FV) generalization of the global flux approach. The most delicate aspect of the algorithm is the appropriate definition of the source flux (integral of the source term) and the quadrature strategy used to match it with the WENO reconstruction of the hyperbolic flux. When this construction is correctly done, one can show that the resulting WENO FV scheme admits exact discrete steady states characterized by constant global fluxes. We also show that, by an appropriate quadrature strategy for the source, we can embed exactly some particular steady states, e.g. the lake at rest for the shallow water equations. It can be shown that an exact approximation of global fluxes leads to a scheme with better convergence properties and improved solutions. The novel method has been tested and validated on classical cases: subcritical, supercritical and transcritical flows.

[Download paper](/files/publications/Ciallella2022globalFlux.pdf)

[Arxiv page](https://arxiv.org/abs/2205.13315)
