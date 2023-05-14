---
title: "Model Order Reduction for Advection Dominated (Hyperbolic) Problems in an ALE framework"
collection: talks
type: "Talk"
permalink: /talks/2023-05-10-MOR-advection
venue: "PDE Afternoon"
date: 2023-05-10
location: "Vienna, Austria"
pdf: /files/talks/RB_advection_dominated_vienna_05_23.pdf
---

Model order reduction (MOR) techniques have always struggled in compressing information for advection dominated problems.
Their linear nature does not allow to accelerate the slow decay of the Kolmogorov N-width of these problems.
In the recent years, many new nonlinear algorithms and frameworks have been presented to overcome this issue.
In this work, we propose a MOR technique for unsteady parametric advection dominated hyperbolic problems, giving a complete offline and online description and showing the time saving in the online phase.
The key of the work consists of an arbitrary Lagrangian--Eulerian approach that modifies both the offline and online phases of the MOR process.
This allows to calibrate the advected features on the same position and to strongly compress the reduced spaces.
We will compare different MOR algorithms between the classical Greedy, EIM and POD and the more recent POD-NN. The calibration map is performed through an optimization process on a training set and then learned through polynomial regression and artificial neural networks for a quick evaluation in the online phase.
In the performed simulations we show how the new algorithm defeats the classical method on many equations with nonlinear fluxes and with different boundary conditions. Finally, we compare the results obtained with different calibration maps.

[Slides](/files/talks/RB_advection_dominated_vienna_05_23.pdf)

[Preprint](/files/publications/Torlo2020MORAdvectionALEMaps.pdf)

