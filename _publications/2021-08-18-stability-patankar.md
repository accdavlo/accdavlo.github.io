---
title: "Issues with Positivity-Preserving Patankar-type Schemes"
collection: publications
permalink: /publication/2021-08-18-stability-patankar
excerpt: 'We study various properties for a class of positivity-preserving nonlinear schemes (Patankar-type schemes) and we discover two types of issues: oscillations around stady states when the timestep is too large and spurious steady states where some methods get stuck.'
date: 2021-08-18
venue: 'Applied Numerical Mathematics'
paperurl: 'https://doi.org/10.1016/j.apnum.2022.07.014'
doi: 'https://doi.org/10.1016/j.apnum.2022.07.014'
arxiv: 'https://arxiv.org/abs/2108.07347'
gitcode: 'https://git.math.uzh.ch/abgrall_group/patankar-stability'
citation: 'D. Torlo, P. Öffner and H. Ranocha. (2022). &quot;Issues with Positivity-Preserving Patankar-type Schemes. &quot; <i>Applied Numerical Mathematics</i>, 182, 117-147.'
pdf: /files/publications/Torlo2021StabilityPatankar.pdf
bib: /files/publications/bib/torlo2022issues.bib
---
This is a work in collaboration with [Philipp Öffner](https://philippoeffner.de/) and [Hendrik Ranocha](https://ranocha.de/).

(Modified) **Patankar**-type schemes are linearly implicit time integration methods designed to be unconditionally positivity-preserving by going outside of the class of general linear methods for production--destruction systems (PDS). In practice, at every time stage a matrix is assembled using the production and destruction terms at the previous stages and a linear system must be solved.
Thus, classical stability concepts cannot be applied and there is no satisfying stability theory for these schemes. 


In particular, two issues appear. The first one is an **oscillation** issue around the steady state, which appear also for linear problems. These oscillations are common to all the schemes and can be observed only for *large* values of the timestep. In this work we find some CFL-type restrictions on the timesteps for all the schemes that seem to provide stability also for nonlinear cases.

CFL=1   | CFL=2
:-------------------------:|:-------------------------:
![Oscillations with CFL 1](/images/research/StabilityPatankar_oscillations_CFL1.png)|![Oscillations with CFL 2](/images/research/StabilityPatankar_oscillations_CFL2.png)


The other issue that these methods show is **loss of accuracy** in the limit for initial conditions going to zero. This happens only for few of these scheme or for some specific parameters. We study analytically which of these schemes lose order of accuracy and we find the reduced order of accuracy for all presented schemes.

![Spurious Steady State for MPRK](/images/research/StabilityPatankar_SteadyMPRK.png)

![Spurious Steady State for MPDeC](/images/research/StabilityPatankar_SteadyDeC.png)

