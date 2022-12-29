---
title: "A new efficient explicit Deferred Correction framework: analysis and applications to hyperbolic PDEs and adaptivity"
collection: publications
permalink: /publication/2022-10-06-efficient-dec
excerpt: 'Deferred Correction methods are arbitrarily high order methods that consists of an iterative procedure. At each iterations the high order reconstruction is updated leading to costs that scale as the square of the order of accuracy. We propose a way to cut up to half of the computational costs for this methods by increasing the order of the reconstruction at each iteration. An adaptive version allows also to set a priori a tolerance to reach a certain error. Applications to PDEs within the RD-DeC frameworks allows as well a great computational advantage.
[Download paper](/files/publications/Micalizzi2022efficientDeC.pdf)'
date: 2022-10-06
venue: 'arXiv preprint'
paperurl: 'https://arxiv.org/abs/2206.03889'
citation: 'L. Micalizzi and D. Torlo. (2022). &quot;A new efficient explicit Deferred Correction framework: analysis and applications to hyperbolic PDEs and adaptivity. &quot; <i>arXiv preprint</i>, 2022. https://arxiv.org/abs/2210.02976.'
pdf: /files/publications/Micalizzi2022efficientDeC.pdf
bib: /files/publications/bib/micalizzi2022new.bib
---
This is a work in collaboration with Lorenzo Micalizzi.

The Deferred Correction is an iterative procedure used to design numerical methods for systems of ODEs, characterized by an increasing accuracy at each iteration.
The main advantage of this framework is the automatic way of getting arbitrarily high order methods, which can be put in Runge-Kutta form, based on the definition of subtimenodes in each timestep.
The drawback is a larger computational cost with respect to the most used Runge-Kutta methods.
To reduce such cost, in an explicit setting, we propose an efficient modification: we remove the unnecessary subtimenodes in all the iterations, introducing interpolation processes between them.
We provide the Butcher tableaux of the novel methods and we study their stability, showing that in some cases the computational advantage does not affect the stability. 
The flexibility of the novel modification allows nontrivial applications to PDEs and construction of adaptive methods.
The good performances of the introduced methods are broadly tested on several benchmarks both in the ODE and PDE settings.


The speed up factor for a vibrating system problem

Equispaced nodes     |  Gauss-Lobatto nodes 
:-------------------------:|:-------------------------:
![FOM simulation](/files/images/posts/eff_dec/pic_16.png)|![ROM simulation](/files/images/posts/eff_dec/pic_17.png)


[Download paper](/files/publications/Micalizzi2022efficientDeC.pdf)

[Download supplementary material](/files/publications/Micalizzi2022efficientDeC_supplement.pdf)

[Arxiv page](https://arxiv.org/abs/2210.02976)
