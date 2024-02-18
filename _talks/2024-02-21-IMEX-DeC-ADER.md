---
title: "IMEX ADER and DeC: arbitrary high order schemes, stability and application to advection--diffusion--dispersion"
collection: talks
type: "Talk"
permalink: /talks/2024-02-21-IMEX-DeC-ADER
venue: "INSIDE Indam Workshop"
date: 2024-02-21
location: "Rome, Italy"
pdf: /files/talks/indam_imex_dec_ader.pdf
---

Arbitrary Derivative (ADER) [Dumbser et al., JCP, 2008] and Deferred Correction (DeC) [Abgrall, JSC, 2017] are arbitrarily high-order methods developed independently in distinct contexts, yet share notable similarities. Both methods employ an iterative process, incrementing by one the order of accuracy at each step. DeC originated as an ODE solver, then used also for more complicated space-time PDE discretizations, while ADER was initially explored as a PDE solver, particularly in its DG space-time discretization, but it has been investigated also as an ODE solver.

Explicit and IMEX versions of these methods have found widespread application, demonstrating adaptability to nonlinear problems through the linearization of stiff terms. We investigate the stability of explicit schemes, revealing a common stability region among these methods for the same order of accuracy [Han Veiga et al., AMC, 2024]. Most implicit methods exhibit A-stability [Petri et al., in prep.], while the IMEX variants are scrutinized by constraining implicit and explicit terms alternately [Minion, Comm. Math. Sci., 2003; Hundsdorfer et al., 2003].

The IMEX formulations of DeC and ADER for PDEs manifest simpler structures in the analysis of linear problems. Our exploration employs von Neumann stability analysis for advection–diffusion and advection–dispersion problems, similarly to [Tan et al. Int. J. Num. Anal. Modeling, 2021]. Hence, we can study the stability regions for some carefully chosen free parameters that depend on time step, mesh discretization and physical coefficients [Petri et al., in prep.]. Our findings establish clear upper bounds for the time step or CFL in advection–diffusion problems. In advection–dispersion cases, the stability regions are much more complicated and show that even respecting similar constraints can lead to unstable schemes.

[Slides](/files/talks/indam_imex_dec_ader.pdf)

