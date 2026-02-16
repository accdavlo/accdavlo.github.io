---
title: "Flux-Balanced Patankar-type Schemes for the Compressible Euler Equations"
collection: publications
permalink: /publication/2026-02-15-flux-balanced-MP
excerpt: 'We present a flux-balanced version of Patankar-type schemes for the compressible Euler equations, demonstrating that applying the Patankar-trick only to the density equation while balancing numerical fluxes leads to improved performance and preservation of contact discontinuities.'
date: 2026-02-15
venue: 'ArXiv'
paperurl: 'https://arxiv.org/pdf/2602.09198'
arxiv: 'https://arxiv.org/pdf/2602.09198'
citation: 'Izgin, T. and Meister, A.  and Shu, C.W. and Torlo, D. (2026), Flux-Balanced Patankar-type Schemes for the Compressible Euler Equations, arXiv:2602.09198.'
pdf: /files/publications/izgin2026fluxbalanced.pdf
bib: /files/publications/bib/izgin2026fluxbalanced.bib
---
Positivity preservation of key physical quantities in the context of fluid flows, such as density and internal energy, is an essential property of a numerical scheme as otherwise the solution lacks physical relevance and has a not well-defined equation of state. One time integration technique that is capable of preserving the positivity of quantities for every time step size is the Patankar-trick and its variants. However, in the context of the Euler equations of gas dynamics, we wonder whether the Patankar-trick should be applied to the density and total energy equations or only to one of them. In this work, we discuss one drawback of the schemes when blindly applied to every positive conserved variable and additionally point out
how to overcome the issue by balancing the involved numerical fluxes correctly. To illustrate our findings, we investigate modified Patankar–Runge–Kutta (MPRK) schemes in the context of the compressible Euler equations with and without stiff source terms. We discover that it is beneficial to only apply the Patankar-trick in the density equation and to balance the remaining numerical fluxes consistently
rather than applying the trick also to the energy equation. This leads also to the preservation of contact discontinuities. We perform numerical experiments to demonstrate that the accuracy of the methods is maintained while the performance of our approach is superior to the traditional application of MPRK schemes.
