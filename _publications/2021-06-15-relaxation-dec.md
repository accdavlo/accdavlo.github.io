---
title: "Relaxation Deferred Correction Methods and their Applications to Residual Distribution Schemes"
collection: publications
permalink: /publication/2021-06-15-relaxation-dec
excerpt: 'In this paper, we study different high order FEM methods for hyperbolic problems, providing parameters that lead to stable and reliable schemes. [Download paper](/files/publications/Abgrall2021RelaxationDeC.pdf)'
date: 2021-06-15
venue: 'arXiv'
paperurl: 'https://arxiv.org/abs/2106.05005'
citation: 'R. Abgrall, E. Le Mélédo, P. Öffner and D. Torlo. (2021). &quot;Relaxation Deferred Correction Methods and their Applications to Residual Distribution Schemes. &quot; <i>arXiv preprint</i>, https://arxiv.org/abs/2106.05005.'
pdf: /files/publications/Abgrall2021RelaxationDeC.pdf
---
This is a work in collaboration with [Rémi Abgrall](https://www.math.uzh.ch/index.php?id=people&key1=8882), Elise Le Mélédo and [Philipp Öffner](https://philippoeffner.de/).

In many models described by ordinary differential equations (ODEs) and partial differential equations (PDEs), there exists a scalar quantity that is physically conserved, e.g. energy, entropy, Liyapunov functional or angular momentum. Approximating with numerical methods the solutions of such models does not mean to automatically conserve these quantities. D. Ketcheson in [Relaxation Runge-Kutta Methods: Conservation and stability for inner-product norms](https://arxiv.org/abs/1905.09847) proposes a relaxation approach where each time step is *relaxed* by a factor $\gamma$. This means that the step that one actually does is a little more or a little less than the originally planned step. Properly tuning this $\gamma$, by solving a scalar (nonlinear) equation, one can guarantee to exactly conserve the desired quantity.

Without relaxation         |  With Relaxation 
:-------------------------:|:-------------------------:
![Energy error without relaxation](/images/relaxation-dec/pendulum__energy_standard.png)|![Energy error with relaxation](/images/relaxation-dec/pendulum__energy_relaxed.png)


In this work, we extend the relaxation algorithm to the class of arbitrarily high order accurate schemes defined by the Deferred Correction methods, [Dutt](https://doi.org/10.1023/A:1022338906936) [Minion](https://doi.org/10.4310/CMS.2003.v1.n3.a6) [Abgrall](https://doi.org/10.1007/s10915-017-0498-4). These methods can be used as method of lines, and hence, rewritten into Runge--Kutta methods, but they can also be used as iteration methods to converge to complicated high order discretizations using matrix free schemes. In that context, the relaxation technique can be applied in different ways. 

Convergence of Relaxed DeC         |  Phase space evolution for a pendulum 
:-------------------------:|:-------------------------:
![Error convergence for pendulum test](/images/relaxation-dec/convergence.png)|![Phase space comparison](/images/relaxation-dec/phasePendulum.png)

Moreover, the whole procedure is limited by the necessity of having an *entropy* conservative/dissipative formulation of the spatial discretization, which fulfills the physical behavior of the solutions. We use the [Entropy Fix](https://doi.org/10.1016/j.jcp.2018.06.031) approach by Abgrall, in the context of residual distribution to obtain either entropy conservative or entropy dissipative schemes.

[Download paper](/files/publications/Abgrall2021RelaxationDeC.pdf)

[Arxiv page](https://arxiv.org/abs/2106.05005)
