---
title: "Hyperbolic problems: high order methods and model order reduction"
collection: talks
type: "Talk"
permalink: /talks/2020-06-02-PhD-defense
venue: "University of Zurich"
date: 2020-06-02
location: "Zurich, Switzerland"
pdf: /files/talks/defensePresentation_06_2020.pdf
---

[Slides](/files/talks/defensePresentation_06_2020.pdf)

[Link to the PhD thesis](/files/theses/TorloPhDThesisOneSided.pdf)

Numerical simulations are extremely important to forecast physical events. In particular,
this is true when experiments are too expensive or unfeasible. The field of numerical analysis
studies how to obtain reliable simulations of physical phenomena. Physics provides the modeling
equations, e. g. partial differential equations (PDEs), then numerical analysis creates numerical
methods that approximate the solutions of such equations. In this manuscript, we focus on
numerical methods for ordinary differential equations (ODEs) and hyperbolic PDEs.

ODEs can model many chemical and biological processes and the numerical methods to solve
them are fundamental to solve also PDEs. Hyperbolic PDEs comprise many physical models,
including fluid dynamics, transport equations, kinetic models and wave equations. The numerical
methods for this kind of problems are vital for many engineering applications.

The schemes that we aim to obtain must verify many properties. They should converge to
the analytical solution as the discretization scale decreases, they should be stable in order to
produce spurious oscillations, they should guarantee a certain level of accuracy and they should
be computable in reasonable times. Often, these last two factors are in contradiction as more
accurate solutions require more computational time.

To tackle this problem we propose in this thesis some possible solutions. The first one is to
speed up the convergence process by using high order accurate schemes. These schemes obtain
much more accurate solutions with less refinements of the discretization scale with respect to low
order accurate solutions. Hence, the computational costs needed to reach a certain error threshold
is lower a priori. Another technique that we will use are implicit schemes. These schemes do not
need to follow the restriction that explicit schemes have on the time discretization, allowing the
use of less time steps. Finally, model order reduction techniques are tools that create a smaller
discrete model, which represents, up to a certain error, an approximation of the solution manifold
for parametric problems.

For high order accurate ODE solvers, we present in this work a class of arbitrarily high
order schemes, called deferred correction (DeC) methods, which consist of an iterative procedure
that, in a fixed number of loops, reaches an approximation of the required order. We study their
A–stability for many possible orders of accuracy. In order to preserve positivity and conservation
of physical quantities in production–destruction systems, we create a modified version of the
DeC, which guarantees all these properties. This is possible thanks to the so–called Patankar
trick, which makes the scheme linearly implicit. So far, the modified Patankar schemes were
developed only up to third order of accuracy. The method we propose is arbitrarily high order
accurate and unconditionally positivity preserving and conservative.

The rest of the thesis is focused on hyperbolic PDEs. We consider the residual distribution
(RD) schemes as high order accurate spatial discretization technique in combination with the
DeC for the time discretization. As a first step, we show a von Neumann stability analysis of
the combination of these two methods, which suggests the optimal value of the stabilization parameters to maximize the time steps. This analysis uses Kreiss’ theorem as a tool to verify
the stability of the family of matrices that evolve the Fourier coefficients of the solutions. The
complications of this analysis are due to the different nature of different degrees of freedom inside
the polynomial reconstruction.

Furthermore, we extend the RD DeC method to an implicit–explicit version for kinetic models.
Kinetic models contain a source term that, in the asymptotic limit, becomes stiff. To deal with
it, an implicit treatment of such a term is necessary. We propose an implicit—explicit RD DeC
scheme that solves this type of models. Moreover, the proposed scheme is arbitrarily high order
and asymptotic preserving, i. e., in the asymptotic regime the numerical solution converges to the
analytical asymptotic limit. We prove these properties and we validate the theoretical results with
numerical simulations.

Next, we study the model order reduction (MOR) algorithms for parametric hyperbolic
problems. These techniques were originally developed for elliptic and parabolic problems and
not all the algorithms can be extended to the hyperbolic framework. We propose an uncertainty
quantification application of a MOR benchmark algorithm for hyperbolic problems. We show
how the reduction can save computational time and we compute some statistical quantities, like
mean and variance, of stochastic hyperbolic PDEs.

Finally, we extend this algorithm in order to gain more compression in the reduced model.
Indeed, MOR algorithms are badly suited for advection dominated problems and most of the
hyperbolic problems are of this kind. Even for the simplest wave transport problems, the classical
MOR techniques fail to obtain a reasonable reduction, since they try to express the solution
manifold as a linear combination of modes. What we propose in the last part of this thesis
is to contextualize the PDEs into an arbitrary Lagrangian–Eulerian framework, which allows,
through a transformation map, to align the advected features and to strongly compress the relevant
information of the solution manifold. The transformation map must also be quickly computable
in the reduced model and to do so, we use different regression techniques, such as polynomial
regression and artificial neural networks, and we compare their performances.

All the algorithms and schemes are validated through adequate numerical simulations.

