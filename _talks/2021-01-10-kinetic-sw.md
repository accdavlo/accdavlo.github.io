---
title: "High Order Well-Balanced Discrete Kinetic Model for Shallow Water Equations"
collection: talks
type: "Talk"
permalink: /talks/2021-01-10-kinetic-sw
venue: "WCCM - Eccomas 2020"
date: 2021-01-10
location: "Paris, France"
---
In this work, we study a kinetic model that contains stiff relaxation terms in the source. This model
can be applied to any non linear hyperbolic problem without source term, that we will call macroscopic
problem, to obtain a larger system of equations with linear fluxes and non–linear source terms, the
microscopic problem, that converges asymptotically to the original hyperbolic system.

We want to apply this kinetic model to shallow water equations with a source term that depends on the
profile of the bathymetry. Thus, the model must be extended in order to include this term and to gain
the asymptotic convergence to the macroscopic problem.

To solve the equations with high order methods, we use an IMEX (implicit–explicit) discretization in
time to stabilize the relaxation term, with DeC (deferred correction) time integration, a high order
iterative time integration technique, and RD (residual distribution) space discretization, a finite–
element based method that can generalize well–known discontinuous Galerkin, finite volume and finite
difference schemes.

The scheme proposed must verify many essential physical and numerical properties in order to guarantee
the quality of the simulations. First of all, the scheme should be AP (asymptotic preserving), which
means that in the relaxation limit, we will recast the macroscopic model of the shallow water equations.
Then, we should guarantee the well balancedness of the solution in the lake at rest case, where no
oscillations should occur when the surface level of the water is constant and the speed is zero. Moreover,
we want our scheme to guarantee positivity of water height everywhere in the domain, also close to wet
and dry area.

We show some numerical tests to prove the quality of the scheme.

[Link to the talk](https://slideslive.com/38945721)


REFERENCES
 * Aregba-Driollet, D. and Natalini, R., Discrete Kinetic Schemes for Systems of Conservation Laws. Birkhauser
Basel, Basel, 1999.
 * R. Abgrall, and D. Torlo. Asymptotic preserving Deferred Correction Residual Distribution schemes. arXiv
e-prints, page arXiv:1811.09284, Nov 2018.
 * A. Dutt, L. Greengard, and V. Rokhlin. Spectral Deferred Correction Methods for Ordinary Differential
Equations. BIT Numerical Mathematics, 40(2):241–266, 2000.
 * M. Ricchiuto and R. Abgrall. Explicit Runge-Kutta residual distribution schemes for time dependent problems: Second order case. Journal of Computational Physics, 229(16):5653–5691, 2010.

<div id="presentation-embed-38945757"></div>
<script src='https://slideslive.com/embed_presentation.js'></script>
<script>
embed = new SlidesLiveEmbed('presentation-embed-38945757', {
    presentationId: '38945757',
    autoPlay: false, // change to true to autoplay the embedded presentation
    verticalEnabled: true
});
</script>
