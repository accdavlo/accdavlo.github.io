---
title: "A time-adaptive algorithm for pressure dominated flows: a heuristic estimator"
collection: publications
permalink: /publication/2024-06-29-time-adaptive-pressure
excerpt: 'We compare some time-adaptive algorithms based on error estimators that use variations of BDF2 and BDF3 time marching schemes, for Navier-Stokes and FSI problems with pressure dominated flows.'
date: 2024-06-29
venue: 'Computational Mechanics and Applied Mathematics: Perspectives from Young Scholars'
paperurl: 'https://dx.doi.org/10.1007/978-3-031-76591-9_24'
arxiv: 'https://arxiv.org/abs/2407.00428'
doi: 'https://dx.doi.org/10.1007/978-3-031-76591-9_24'
citation: 'Prusak, I., Torlo, D., Nonino, M., Rozza, G. (2025). A Time-Adaptive Algorithm for Pressure Dominated Flows: A Heuristic Estimator. In: Marmo, F., Cuomo, S., Cutolo, A. (eds) Computational Mechanics and Applied Mathematics: Perspectives from Young Scholars. GIMC SIMAI Young 2024. Lecture Notes in Mechanical Engineering. Springer, Cham. https://doi.org/10.1007/978-3-031-76591-9_24'
pdf: /files/publications/prusak2024timeadaptive.pdf
bib: /files/publications/bib/prusak2024timeadaptive.bib
---
This work aims to introduce a heuristic timestep-adaptive algorithm for Computational Fluid Dynamics (CFD) and Fluid-Structure Interaction (FSI) problems where the flow is dominated by the pressure. In such scenarios, many time-adaptive algorithms based on the interplay of implicit and explicit time schemes fail to capture the fast transient dynamics of pressure fields. We present an algorithm that relies on a temporal error estimator using Backward Differentiation Formulae (BDFk) of order k=2,3. Specifically, we demonstrate that the implicit BDF3 solution can be well approximated by applying a single Newton-type nonlinear solver correction to the implicit BDF2 solution. The difference between these solutions determines our adaptive temporal error estimator. The effectiveness of our approach is confirmed by numerical experiments conducted on a backward-facing step flow CFD test case with Reynolds number 300 and on a two-dimensional haemodynamics FSI benchmark.
