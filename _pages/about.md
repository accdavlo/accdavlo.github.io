---
permalink: /
title: "Davide Torlo's Personal Website"
excerpt: "I am an Assistant Professor in Numerical Analysis, focusing on hyperbolic PDEs and model order reduction."
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

Hello visitor! I am Davide Torlo, an Assistant Professor (RTT, tenure track) at [Università di Roma La Sapienza](https://www.uniroma1.it) at Mathematics Department [Guido Castelnuovo](https://www.mat.uniroma1.it/). I am in the [Numerical Analysis and Scientific Computing Research Group](https://sites.google.com/uniroma1.it/an-sc-research-group/home) of the department. We organize the [MDN Seminars ("Modellistica Differenziale Numerica")](https://sites.google.com/uniroma1.it/an-sc-research-group/group-seminar) on Thursday at 12.30.

### Previous positions:
 * Postdoctoral Fellow at [SISSA](https://www.sissa.it/) in prof. [Rozza's group](https://people.sissa.it/~grozza/contact/)
 * Researcher at [INRIA Bordeaux](https://www.inria.fr/fr/centre-inria-bordeaux-sud-ouest) in [CARDAMOM](https://team.inria.fr/cardamom/) team, under the supervision of [prof. Mario Ricchiuto](https://team.inria.fr/cardamom/marioricchiuto/)
 
### Education:
 * PhD student at [University of Zurich](https://www.math.uzh.ch/index.php?id=home) under the supervision of [prof. Rémi Abgrall](https://www.math.uzh.ch/index.php?id=people&key1=8882)
 * M.Sc. in [SISSA](https://www.sissa.it/) and [University of Trieste](https://www.units.it), thesis with [prof. Gianluigi Rozza](https://people.sissa.it/~grozza/)
 * B.Sc. at [University of Milan - Bicocca](https://unimib.it)


Current research
======
My research interest is mainly focused on numerical methods for **hyperbolic PDEs**. In particular I study methods that are **structure preserving**  and **arbitrarily high order**. I also study **Model Order Reduction** techniques for advection dominated problems and Fluid Structure Interaction problems.

## Structure preserving methods
Many physical models are described by equations whose solutions verify certain properties. These physical properties are often of paramount importance and numerical methods should be able to preserve such properties. In the last years, I have developed several methods able of preserving different properties:
 * **positivity** of the solution for example with modified Patankar (mP) schemes, starting from [mPDeC schemes](/publication/2020-07-01-mPDeC), studies on their [Issues](/publication/2021-08-18-stability-patankar) and with applications for [Shallow Water equations](/publication/2021-10-27-sw-mpdec)
![Island simulation](/images/research/sw_mPDeC_island.gif)
 * **entropy** preserving/diffusing schemes, to find the physically relevant solution, see the [relaxation DeC](/publication/2021-06-15-relaxation-dec) and [relaxation ADER-DG](/publication/2022-06-09-relaxation-ader.md) approaches
 * **well-balancing** some particular solutions as lake at rest states for shallow water in [MPDeC for SW](/publication/2021-10-27-sw-mpdec), global flux [Finite Volume](/publication/2022-05-27-global-flux) and [Finite Element](/publications/2024-07-15-SUPG-GF) methods for shallow water and similar models, schemes to preserve the soliton behavior for dispersive waves equations or the divergence-free character.
![Island simulation](/images/research/twoWaves_GF_dispersive.gif)

## Reduced order models for advection dominated problems
These problems have a very slow decay of the Kolmogorov n-width. Hence, specific techniques must be used to obatain computational reduction. Ingredients that I retain fundamental in this topic are: 
 * an arbitrary-Lagrangian-Eulerian formulation, a geometrical calibration of the solutions, an optimization technique and a forecast of such calibration, see [the preprint](/publication/2020-03-30-MOR-AD-ALE_1D), now working on extending the process on multiple shocks and speeds

![Eulerian](/images/research/ALEMOREulerian.png)![Lagrangian](/images/research/ALEMORLagrangian.png)
 * nonlinear strategies including neural networks to tackle the problem, we are studying it now for [Friedrichs' Systems (talk)](/talks/2022-09-22-friedrichs) with Graph Neural Network to tackle the slow Kolmogorov n-width decay

Other more classical ROM have been used for [dispersive wave equations](/publication/2021-12-23-mor-dispersive), in [UQ context](/publication/2019-03-01-model-UQ), for [advection-dominated problems](/publication/2018-10-25-stabilized-weighted) or for [domain decomposition](/publication/2022-11-30-optimization-domain-decomposition).
![Advection Dominated](/images/research/MORadvDom.gif)

## Arbitrarily high order methods
Arbitrarily high order methods allow to obtain very accurate solutions within minimal computational costs. In particular, I have studied arbitrarily high order time integrations as Deferred Correction (**DeC**) and **ADER** and various spatial discretizations (finite element, finite volume, finite difference, spectral difference, discontinuous Galerkin).
 * In the work [ADER is DeC](/publication/2021-02-10-ADER-is-DeC) we compared the two methods as time discretization techniques.
 * In the works [efficient DeC](/publication/2022-10-06-efficient-dec) and [ADER DOOM](/publication/2022-12-16-ADER-DOOM) we studied how to make these methods more efficient, p-adaptive and structure preserving methods. 
 ![Mixing Layers](/images/research/ADERDOOM1.png)
 * For stabilized Finite Element methods in [one dimension](/publication/2021-03-31-dispersion-analysis) and in [two dimensions on triangular meshes](/publication/2022-06-14-dispersion-analysis-triangular) we are studying highly accurate space and time discretization for hyperbolic problems. We use different time integrators, space discretizations and stabilization techniques. The goal is to find the stability regions and the best perfomant scheme. 
![Dispersion analysis](/images/research/dispersionAnalysis.png)
 * Implicit--explicit discretization for kinetic models with arbitrary high order accuracy, through the Deferred Correction as time integration scheme and Residual distribution for the spatial discretization. [IMEX DeC on residual distribution schemes](/publication/2020-06-29-high-order-IMEX-DeC) and [IMEX DeC on finite difference schemes](/publication/2022-01-28-lattice-boltzmann)

![Shu Osher test](/images/research/kineticEuler.png)
