---
permalink: /
title: "Davide Torlo's Personal Website"
excerpt: "I am a postdoctoral researcher in Numerical Analysis, passionate about Data and musician in spare time."
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

Hello visitor! I am Davide Torlo, a Postdoctoral Fellow at [SISSA](https://www.sissa.it/) in prof. [Rozza's group](https://people.sissa.it/~grozza/contact/). Previously researcher at [INRIA Bordeaux](https://www.inria.fr/fr/centre-inria-bordeaux-sud-ouest) in [CARDAMOM](https://team.inria.fr/cardamom/) team, under the supervision of [prof. Mario Ricchiuto](https://team.inria.fr/cardamom/marioricchiuto/). I earned my PhD at [University of Zurich](https://www.math.uzh.ch/index.php?id=home) under the supervision of [prof. Rémi Abgrall](https://www.math.uzh.ch/index.php?id=people&key1=8882). Before, I studied in [SISSA](https://www.sissa.it/) and [University of Trieste](https://www.units.it) for my Master, where I did my thesis with [prof. Gianluigi Rozza](https://people.sissa.it/~grozza/), and at [University of Milan - Bicocca](https://unimib.it) for my Bachelor studies.


Current research
======
Currently I have a SISSA Mathematical Fellowship and I work in prof. Rozza's group on Model Order Reduction for advection dominated problems. I have also various Numerical Analysis projects on hyperbolic PDEs, structure preserving methods for ODEs and PDEs and arbitrarily high order methods.
1. Reduced order models for advection dominated problems. These problems have a very slow decay of the Kolmogorov n-width. Hence, specific techniques must be used to obatain computational reduction. Ingredients that I retain fundamental in this topic are: an arbitrary-Lagrangian-Eulerian formulation, a geometrical calibration of the solutions, an optimization technique and a forecast of such calibration.
1. Friedrichs' systems: a bridge between hyperbolic and elliptic models. We developed model order reduction techniques on such problems including sharp error estimators. Check out my talk [Talk on Friedrichs' Systems](/talks/2022-09-22-friedrichs) 
1. An efficient implementation of the Deffered Correction algorithm. Check out [efficient DeC](/publication/2022-10-06-efficient-dec)
1. Applications of the [mPDeC](/publication/2020-07-01-mPDeC) to shallow water equations for very accurate and positivity preserving schemes. Check out [Shallow Water mPDeC WENO](/publication/2021-10-27-sw-mpdec)
![Island simulation](/images/research/sw_mPDeC_island.gif)
1. Reduced model for dispersive waves. The goal is to split dispersive waves equations into hyperbolic and elliptic part and to reduce the model for the elliptic part of the problem. 
<img src="/images/research/KdVMOR.gif" alt="Dispersive Waves" width="350"/>
1. Arbitarily high order time integration schemes. I am often working with the Deferred Correction (DeC) time integration method or with ADER. I study their properties and their possible extentions to structure preserving schemes. Check out [ADER is DeC](/publication/2021-02-10-ADER-is-DeC) and [mPDeC](/publication/2020-07-01-mPDeC).
1. Stabilized Finite Element methods. We are studying highly accurate space and time discretization for hyperbolic problems. We use different time integrators, space discretizations and stabilization techniques. The goal is to find the stability regions and the best perfomant scheme. 
![Dispersion analysis](/images/research/dispersionAnalysis.png)
1. Kinetic models with macroscopic Shallow Water equations limit. Also here the use of an implicit DeC scheme allows to obtain high order methods.
![Kinetic SW](/images/research/plotTransFrictionPerturb.png)
1. Issues with modified Patankar schemes, which are positive preserving schemes, but can show oscillations and inconsistency under certain conditions. [Issues MP](/publication/2021-08-18-stability-patankar)
<img src="/images/research/RobertsonUnstable.png" alt="Robertson Problem MP" width="350"/>

Previous Projects
=================
During my previous contracts I've studied high order accurate methods and model order reduction techniques for hyperbolic problems. The dissertation of my PhD is available [here](http://accdavlo.github.io/files/theses/TorloPhDThesisOneSided.pdf).
1. I have studied an implicit--explicit discretization for kinetic models with arbitrary high order accuracy, through the Deferred Correction as time integration scheme and Residual distribution for the spatial discretization. [Publication on the topic](/publication/2020-06-29-high-order-IMEX-DeC)
<img src="/images/research/kineticEuler.png" alt="Shu Osher test" width="350"/>
1. MOR techniques for hyperbolic problems for advection dominated problems with an *ad hoc* arbitrary Lagrangian--Eulerian model to track the steep fronts, [here](/publication/2020-03-30-MOR-AD-ALE_1D), and for uncertainty quantification applications [here](/publication/2019-03-01-model-UQ).

![Eulerian](/images/research/ALEMOREulerian.png)![Lagrangian](/images/research/ALEMORLagrangian.png)
1. Weighted MOR algorithm to speed up the computation in stochastic PDE. I wrote a [post](/posts/2021/02/wMOR/) on that and there is a [publication](/publication/2018-10-25-stabilized-weighted) about it.
![Advection Dominated](/images/research/MORadvDom.gif)
