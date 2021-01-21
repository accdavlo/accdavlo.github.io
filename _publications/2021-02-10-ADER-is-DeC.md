---
title: "DeC and ADER: Similarities, Differences and a Unified Framework"
collection: publications
permalink: /publication/2021-02-10-ADER-is-DeC
excerpt: 'In this paper, we demonstrate that the explicit ADER approach can be seen as a special interpretation of the deferred correction (DeC) method.'
date: 2021-02-10
venue: 'Journal of Scientific Computing'
paperurl: 'https://doi.org/10.1007/s10915-020-01397-5'
citation: 'M. H. Veiga, P. Öffner, and D. Torlo. (2021). &quot;DeC and ADER: Similarities, Differences and a Unified Framework.&quot; <i>Journal of Scientific Computing</i>, soon.'
---
In this paper, we demonstrate that the explicit ADER approach can be seen as a special interpretation of the deferred correction (DeC) method.
By using this fact, we are able to embed ADER in a theoretical background of time integration schemes and prove the relation between the accuracy order and the number of iterations which are needed to reach the desired order.
Next, we extend our investigation to stiff ODEs, treating these source terms implicitly. Some differences in the interpretation and implementation can be found. Using DeC yields typically a much simpler implementation, while ADER benefits from a higher accuracy, at least for our numerical simulations.  Then, we also focus on the PDE case and present common space-time discretizations using DeC and ADER in closed forms.
Finally, in the numerical section we investigate A-stability for the ADER approach - this is done for the first time up to our knowledge - for different order using several basis functions and compare them with the DeC ansatz. Then, we compare the performance of ADER and DeC for stiff and non-stiff ODEs and verify our analysis focusing on two basic hyperbolic problems.


[Download paper here](https://arxiv.org/abs/2002.11764)
