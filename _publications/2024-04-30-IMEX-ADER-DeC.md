---
title: "Analysis for Implicit and Implicit-Explicit ADER and DeC Methods for Ordinary Differential Equations, Advection-Diffusion and Advection-Dispersion Equations"
collection: publications
permalink: /publication/2024-04-30-IMEX-ADER-DeC
excerpt: 'We study the implicit and IMEX version of DeC and ADER time integration method with application to advection-diffusion and advection-dispersion equations. The study is based on stability analysis.'
date: 2024-04-30
venue: 'Applied Numerical Mathematics'
paperurl: 'https://doi.org/10.1016/j.apnum.2024.12.013'
doi: '10.1016/j.apnum.2024.12.013'
arxiv: 'https://arxiv.org/abs/2404.18626'
citation: 'Öffner, P., Petri, L., and Torlo, D. (2025). Analysis for Implicit and Implicit-Explicit ADER and DeC Methods for Ordinary Differential Equations, Advection-Diffusion and Advection-Dispersion Equations. Applied Numerical Mathematics, 212, p. 110-134.'
pdf: /files/publications/oeffner2025analysis_APNUM.pdf
bib: /files/publications/bib/oeffner2024analysis.bib
---
In this manuscript, we present the development of implicit and implicit-explicit ADER and DeC methodologies within the DeC framework using the two-operators formulation, with a focus on their stability analysis both as solvers for ordinary differential equations (ODEs) and within the context of linear partial differential equations (PDEs). To analyze their stability, we reinterpret these methods as Runge-Kutta schemes and uncover significant variations in stability behavior, ranging from A-stable to bounded stability regions, depending on the chosen order, method, and quadrature nodes. This differentiation contrasts with their explicit counterparts. When applied to advection-diffusion and advection-dispersion equations employing finite difference spatial discretization, the von Neumann stability analysis demonstrates stability under CFL-like conditions. Particularly noteworthy is the stability maintenance observed for the advection-diffusion equation, even under spatial-independent constraints. Furthermore, we establish precise boundaries for relevant coefficients and provide suggestions regarding the suitability of specific schemes for different problem. 
