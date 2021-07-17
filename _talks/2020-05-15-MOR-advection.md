---
title: "Model Reduction for Advection Dominated Hyperbolic Problems in an ALE Framework: Offline and Online Phases"
collection: talks
type: "Talk"
permalink: /talks/2020-05-15-MOR-advection
venue: "Analysis Junior Seminars 2019-2020"
date: 2020-05-15
location: "Trieste, Italy"
pdf: /files/talks/ADERDeCSAMinar_05_2020.pdf
---

Model order reduction (MOR) techniques have always struggled in compressing information for advection dominated problems.

Their linear nature does not allow to accelerate the slow decay of the Kolmogorov N-width of these problems.
In the last years, new nonlinear algorithms obtained smaller reduced spaces. In these works only the *offline* phase of these algorithms was shown.

In this talk, we study MOR algorithms for unsteady parametric advection dominated hyperbolic problems, giving a complete *offline* and *online* description and showing the time saving in the *online* phase.
We propose an arbitrary Lagrangian-Eulerian approach that modifies both the *offline* and *online* phases of the MOR process.

This allows to calibrate the advected features on the same position and to strongly compress the reduced spaces.

The basic MOR algorithms used are the classical Greedy, EIM and POD, while the *calibration* map is learned through polynomial regression and artificial neural networks.

In the performed simulations we show how the new algorithm defeats the classical method on many equations with nonlinear fluxes and with different boundary conditions. Finally, we compare the results obtained with different *calibration* maps.


[Link to the talk](https://drive.math.uzh.ch/index.php/s/2KWprBEn8JQ4Nai)

[Slides](/files/talks/RB_advection_dominated_trieste_150520.pdf)

[Link to the reference](/publication/2020-03-30-MOR-AD-ALE_1D)
