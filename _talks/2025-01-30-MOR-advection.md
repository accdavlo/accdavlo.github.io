---
title: "Calibration-Based ALE Model Order Reduction for Hyperbolic Problems with Self-Similar Traveling Discontinuities"
collection: talks
type: "Talk"
permalink: /talks/2025-01-30-MOR-advection
venue: "Politecnico di Torino"
date: 2025-01-30
location: "Torino, Italy"
pdf: /files/talks/RB_advection_torino_25_01.pdf
---

Model order reduction (MOR) has been a fundamental tool for reducing computational costs in parametrized (differential) problems. It works on the basis idea that the solutions for different parameters belongs to a reduced linear space with a very small dimension, with respect to classical Finite Element/Finite Volume spaces.
This ansatz is not true for problem with steep traveling features, which are very common in hyperbolic partial differential equations. Here, shocks can arise in finite time from smooth solutions and travel along the domain. For these problems, MOR is not effective as the reduced solutions that it produces are oscillatory and not accurate.
To overcome this issue, we propose an arbitrary Lagrangian-Eulerian approach to the problem, where all the parametric solutions are mapped into a reference domain where the moving features are aligned. In the reference domain, classical MOR will be again effective and the reduction can be performed.
The calibration process that transforms the solutions onto the reference domain uses some piece-wise cubic spline interpolation maps constrained to invertibility. These maps are parametrised into some calibration points that are then learned with some simple neural networks.
We will apply the methodology to computational fluid dynamics examples, using a POD-NN as MOR technique. The proposed strategy will show much more reliable solutions than the classical MOR techniques.

[Slides](/files/talks/RB_advection_torino_25_01.pdf)

[Work on Calibration ROMs](/publications/2024-03-18-ROM-calibration-2D)

