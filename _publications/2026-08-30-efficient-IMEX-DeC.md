---
title: "New Efficient Implicit-Explicit Deferred Correction methods"
collection: publications
permalink: /publication/2026-08-30-efficient-IMEX-DeC
excerpt: 'We extend the finite element global flux to Euler equations of gas-dynamics to preserver numerous nontrivial multidimensional equilibria, also with gravity source terms. The method is able to preserve an accurate approximation of the steady states with a super-convergent behavior.'
date: 2026-08-30
venue: 'ArXiv'
paperurl: 'https://arxiv.org/pdf/2608.23919'
arxiv: 'https://arxiv.org/pdf/2608.23919'
citation: 'Micalizzi, L. and Torlo, D.(2026), New Efficient Implicit-Explicit Deferred Correction methods, arXiv:2608.23919.'
pdf: /files/publications/micalizzi2026efficientIMEX.pdf
bib: /files/publications/bib/micalizzi2026efficientIMEX.bib
---
n this work, we investigate implicit-explicit (IMEX) arbitrary high-order Deferred Correction (DeC) methods for the approximation of ordinary differential equations (ODEs). Such schemes are characterized by an iterative procedure that increases the order of accuracy by one at each iteration. More precisely, we study an efficient modification based on the introduction of interpolation processes between consecutive iterations, with the aim of systematically matching the accuracy achieved at each iteration with the order of the discretization employed. On the one hand, this modification leads to computational advantages, since the low-order iterations are performed on cheaper lower-order discretization structures; on the other hand, it endows the methods with a natural p-adaptive character, which is particularly appealing in the context of practical applications. We investigate this modification for two families of DeC schemes, providing numerical validation, efficiency assessments, and stability region plots. The numerical validation includes several examples involving stiff ODEs and partial differential equations (PDEs) with high-order spatial derivatives. The ability of the modified schemes to provide high-fidelity results at reduced computational cost, as well as the effectiveness of the adaptive strategy, is demonstrated through the numerical experiments.