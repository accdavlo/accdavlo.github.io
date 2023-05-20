---
title: "Global flux WENO finite volume and other structure preserving schemes for water equations"
collection: talks
type: "Talk"
permalink: /talks/2023-05-25-global-flux
venue: "SHARK-FV 2023"
date: 2023-05-25
location: "Minho, Portugal"
pdf: /files/talks/global_flux_shark23_05_23.pdf
---
Water wave equations are known to preserve various equilibria or some specific solutions. The lake at rest steady state is the most well-known equilibrium, and classically many methods are able to preserve such equilibrium. This allows capturing with extreme accuracy the perturbations of such a state.

There are, nevertheless, other interesting (moving) equilibria or specific solutions that could be worth preserving. In one dimension, steady-state moving equilibria can be well captured through different techniques. In this work \cite{ciallella}, we apply the global flux technique introduced by \cite{cheng}, inspired by the seminal work of \cite{gascon}, to an arbitrary high-order WENO finite volume framework. The main idea of the method consists of writing the flux and the source terms of the equations into a unique global flux. Using discretizations that depend only on the global flux quantities, one is able to discretely preserve some very accurate discretization of the moving equilibria.

Other particular solutions we want to preserve with this approach are solitary waves of dispersive equations. For such solutions, the equations reduce to linear advection. Using a similar approach, where the global flux is built upon the whole PDE (not only on flux and source) for BBM or dispersive wave equations, it is possible to obtain more accurate methods with respect to classical discretization, aiming to resemble the linear advection equations at the discrete level. The observed advantage might arise not only in the *global flux* framework but it is a good starting point for further investigation on some specific schemes.

This is a talk is about a work in collaboration with [Mirco Ciallella](https://sites.google.com/view/mircociallella), [Mario Ricchiuto](https://team.inria.fr/cardamom/marioricchiuto/) and [Wasilij Barsukow](https://www.math.u-bordeaux.fr/~wbarsukow/). 


If you want to learn more, you find here the references.


[Slides](/files/talks/global_flux_shark23_05_23.pdf)

[Link to the publication](/publication/2022-05-27-global-flux)

[Download paper](/files/publications/Ciallella2022globalFlux.pdf)

[Arxiv page](https://arxiv.org/abs/2205.13315)

