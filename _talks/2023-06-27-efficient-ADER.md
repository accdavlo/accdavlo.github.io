---
title: "Saving computational costs with efficient iterative ADER methods: p-adaptivity, accuracy results and structure preserving limiters"
collection: talks
type: "Talk"
permalink: /talks/2023-06-27-efficient-ADER
venue: "Numhyp 2023"
date: 2023-06-27
location: "Bordeaux, France"
pdf: /files/talks/ADER_numhyp23.pdf
---
Hyperbolic solvers with arbitrarily high order of accuracy are
widely used in scientific simulations, but they often come with a high computational cost. In this study, we introduce a modification to the ADER
(Arbitrary DERivative) and Deferred Correction (DeC) methods that can
save up to half of the computational cost, without sacrificing accuracy. By
iteratively increasing the degree of solution reconstruction, our modification
provides a natural framework for introducing p-adaptivity in the method,
allowing users to adjust the accuracy level according to their goals, cell by
cell. Additionally, our approach enables the preservation of solution properties such as positivity, local maximum principle or entropy inequalities, with
a very efficient a posteriori limiter.
We demonstrate the effectiveness of our method through results applied on
ADER-DG and ADER-FV, using the Discrete Optimally increasing Order
Method (DOOM) limiter to preserve positivity of density and pressure for
compressible Euler and Navier-Stokes equations. Our approach offers a significant computational advantage compared to classical ADER methods, with
minimal impact on the accuracy achieved.


This is a talk is about a work in collaboration with Lorenzo Micalizzi, Walter Boscheri and [Maria Han Veiga](https://hanveiga.com/). 


If you want to learn more, you find here the references.


[Slides](/files/talks/ADER_numhyp23.pdf)

[Link to the publication on DOOM limiter](/publication/2022-12-16-ADER-DOOM)
[Link to the publication on analysis of efficient ADER](/publication/2023-05-22-improving-ADER)
