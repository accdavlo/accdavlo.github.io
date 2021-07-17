---
title: "On modified Patankar schemes and oscillations: towards new stability definitions"
collection: talks
type: "Talk"
permalink: /talks/2021-07-12-stability-patankar
venue: "Icosahom 2020"
date: 2021-07-12
location: "Vienna, Austria"
pdf: /files/talks/stability_patankar_icosahom_MS_07_2021.pdf
---

Modified Patankar (MP) schemes are linearly implicit ODE solvers for production destruction problems that guarantee unconditionally the positivity of the solutions and the conservation of the total quantities.

At the moment, different version of such schemes are available, some classes of Runge--Kutta (RK), strong stability preserving RK (SSPRK) and arbitrarily high order Deferred Correction (DeC) schemes.

The classical A-stability, L-stability properties cannot be directly computed on such schemes, for serveral reasons, inter alia, Dahlquist's equation is not a production destruction system and the mass matrix of the MP schemes depends on the variables. Moreover, we observed that for large timesteps these schemes may produce oscillations around the steady state solution.

We try to find new measures of stability for these type of schemes measuring different quantities of which the analytical behavior is known, e.g. dissipative Liyapunov functionals. This information can be computed analytically or numerically for the various parameters involved (scheme parameters, initial condition, time step size) in the procedure for simple problems. These measures show us which schemes are favorable to solve these problems and under which conditions (e.g. time step restrictions).

[Link to the video of the talk](https://drive.math.uzh.ch/index.php/s/cagMCJTBs3sBy6Z)

[Slides](/files/talks/stability_patankar_icosahom_MS_07_2021.pdf)
