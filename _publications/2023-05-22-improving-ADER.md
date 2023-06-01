---
title: "On improving the efficiency of ADER methods"
collection: publications
permalink: /publication/2023-05-22-improving-ADER
excerpt: 'The arbitrary derivative (ADER) approach for numerical differential problem solution is enhanced in this study. Improvements include higher-order accuracy through precise polynomial discretization choices and integration with Deferred Correction (DeC) formalism. Analytical and numerical results cover stability analysis, computational efficiency, adaptivity, and hyperbolic PDE applications with Spectral Difference (SD) discretization. [Download paper](/files/publications/HanVeiga2023improvingADER.pdf)'
date: 2023-05-22
venue: 'arXiv preprint'
paperurl: 'https://arxiv.org/abs/2305.13065'
arxiv: 'https://arxiv.org/abs/2305.13065'
citation: 'M. Han Veiga, L. Micalizzi and D. Torlo. &quot;On improving the efficiency of ADER methods.&quot; (2023) <i>arXiv preprint</i>, arXiv:2305.13065.'
pdf: /files/publications/HanVeiga2023improvingADER.pdf
bib: /files/publications/bib/veiga2023improving.bib
---
This work is in collaboration with [Maria Han Veiga](https://hanveiga.com/) and Lorenzo Micalizzi

The (modern) arbitrary derivative (ADER) approach is a popular technique for the numerical solution of differential problems based on iteratively solving an implicit discretization of their weak formulation. In this work, focusing on an ODE context, we investigate several strategies to improve this approach. Our initial emphasis is on the order of accuracy of the method in connection with the polynomial discretization of the weak formulation. We demonstrate that precise choices lead to higher-order convergences in comparison to the existing literature. Then, we put ADER methods into a Deferred Correction (DeC) formalism. This allows to determine the optimal number of iterations, which is equal to the formal order of accuracy of the method, and to introduce efficient p-adaptive modifications. These are defined by matching the order of accuracy achieved and the degree of the polynomial reconstruction at each iteration. We provide analytical and numerical results, including the stability analysis of the new modified methods, the investigation of the computational efficiency, an application to adaptivity and an application to hyperbolic PDEs with a Spectral Difference (SD) space discretization.

This is a generalization of the idea of the [work on efficient DeC](/publication/2022-10-06-efficient-dec)
