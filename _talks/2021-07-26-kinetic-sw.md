---
title: "Continuous Galerkin high order well-balanced discrete kinetic model for shallow water equations"
collection: talks
type: "Talk"
permalink: /talks/2021-07-26-kinetic-sw
venue: "Numhyp 2021"
date: 2021-07-26
location: "Trento, Italy"
pdf: /files/talks/relaxation_IMEX_RD_DeC_Trento_07_21.pdf
---

Kinetic models describe many physical phenomena, inter alia Boltzmann equations, but can also be used to approximate with an artificial relaxation procedure other macroscopic models. We consider the kinetic model proposed by Aregba-Driollet and Natalini \cite{natalini}, and we modify it in order to approximate shallow water (SW) equations. The difference with the original model stands in the presence of the source term in the SW equations due to the effect of the bathymetry. Thus, the kinetic model \cite{natalini} must be extended in order to include this term and to maintain the asymptotic convergence to the macroscopic limit of the SW problem.

To solve the equations with high order methods, we use an IMEX (implicit--explicit) discretization in time \cite{TorloRDIMEX} to stabilize the relaxation and the friction terms, with DeC (deferred correction) \cite{DeC_Dutt} time integration, a high order iterative time integration technique, and RD (residual distribution) \cite{RD} space discretization, a finite--element based method.

The scheme proposed must verify many essential physical and numerical properties in order to guarantee the quality of the simulations. First of all, the scheme should be AP (asymptotic preserving), which means that in the relaxation limit, we will recast the macroscopic model of the shallow water equations. Then, we should guarantee the well--balancedness of the solution in the lake at rest case, where no oscillations should occur when the surface level of the water is constant and the speed is zero. Moreover, we want our scheme to guarantee positivity of water height everywhere in the domain, also close to wet and dry area.

We show some numerical tests to validate the quality of the scheme.

[Slides](/files/talks/relaxation_IMEX_RD_DeC_Trento_07_21.pdf)
