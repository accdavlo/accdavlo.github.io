---
title: "High-order positivity-preserving well-balanced schemes: combining flux globalization with modified Patankar deferred correction methods"
collection: publications
permalink: /publication/2026-10-15-high-order-positivity-preserving-well
excerpt: 'Positivity-preserving schemes for hyperbolic balance laws are typically built from the Zhang-Shu limiter and strong-stability-preserving Runge-Kutta (SSP-RK) time stepping, at the cost of a restrictive time-step condition.'
date: 2026-10-15
venue: 'ArXiv'
paperurl: 'https://arxiv.org/abs/2610.21857'
arxiv: 'https://arxiv.org/abs/2610.21857'
citation: 'Öffner, P. and Redle, M. and Torlo, D. (2026), High-order positivity-preserving well-balanced schemes: combining flux globalization with modified Patankar deferred correction methods, arXiv:2610.21857.'
pdf: /files/publications/offner2026high.pdf
bib: /files/publications/bib/offner2026high.bib
---
Positivity-preserving schemes for hyperbolic balance laws are typically built from the Zhang-Shu limiter and strong-stability-preserving Runge-Kutta (SSP-RK) time stepping, at the cost of a restrictive time-step condition. The modified Patankar deferred correction (mPDeC) method removes this restriction, offering high-order accuracy, conservation, and unconditional positivity. However, its solution-dependent Patankar weights make the time update nonlinear, so, unlike with RK methods, preserving (steady and moving) equilibria, i.e., well-balancing (WB), is no longer straightforward. In this paper, we construct high-order, WB, positivity-preserving mPDeC schemes by combining mPDeC with a flux-globalization approach. We demonstrate the idea on the one-dimensional shallow water equations, using a WB A-WENO spatial discretization, and introduce a modified local characteristic decomposition that remains stable in the presence of dry states. Numerical experiments on one-dimensional benchmarks confirm that the method satisfies the desired properties.
