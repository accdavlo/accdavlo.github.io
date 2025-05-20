---
title: "A time-adaptive solver for pressure dominated flows in CFD and FSI: domain decomposition and model reduction"
collection: talks
type: "Talk"
permalink: /talks/2025-05-28-time-adaptive-FSI
venue: "COUPLED 2025"
date: 2025-05-28
location: "Villasimius, Italy"
pdf: /files/talks/torlo_coupled25.pdf
---

This work introduces a heuristic timestep-adaptive algorithm for Computational Fluid Dynamics (CFD) and Fluid-Structure Interaction (FSI) problems dominated by pressure [1]. Employing a timestep-adaptive strategy is crucial in many scenarios where computational costs escalate rapidly, and using the largest possible timestep is of paramount importance. In such cases, many time-adaptive algorithms, which rely on a combination of implicit and explicit time schemes, fail to capture the fast transient dynamics of pressure fields, focusing instead primarily on velocity. We propose an algorithm based on a temporal error estimator employing Backward Differentiation Formulae (BDF$k$) of orders $k = 2, 3$. The algorithm is applied to a backward-facing step flow CFD test case [2] and a two-dimensional haemodynamics FSI benchmark [3]. Furthermore, we compare the performance of monolithic approaches with optimization-based domain-decomposed approaches. The latter is particularly suited for complex scenarios where solvers for the two domains cannot be easily coupled, except via boundary conditions. Our observations reveal that the time discretization is highly sensitive to the choice of optimization algorithm, hence several options are compared. On the other hand, the errors of the best optimization for domain-decomposed algorithm is comparable with the monolithic approach and the overall advantage of the time-adaptive strategy is evident. Finally, we will reduced the whole algorithm applying standard Galerkin projection to the whole formulation obtaining faster convergence in the optimization algorithms. Bibliography 

[1] Prusak, I., Torlo, D., Nonino, M. and Rozza, G. (2024). A time-adaptive algorithm for pressure dominated flows: a heuristic estimator, arXiv preprint arXiv:2407.00428. 

[2] Prusak, I., Nonino, M., Torlo, D., Ballarin, F., and Rozza, G. (2023). An optimisation--based domain--decomposition reduced order model for the incompressible Navier-Stokes equations. Computers \& Mathematics with Applications, 151, 172-189. 

[3] Nonino, M., Ballarin, F., and Rozza, G. (2021). A monolithic and a partitioned, reduced basis method for fluid–structure interaction problems. Fluids, 6(6), 229.

[Slides](/files/talks/torlo_coupled25.pdf)

[Work on time adaptive pressure dominated flows](/publications/2024-06-29-time-adaptive-pressure)

