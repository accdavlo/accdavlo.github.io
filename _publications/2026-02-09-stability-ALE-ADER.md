---
title: "Stability analysis of Arbitrary-Lagrangian-Eulerian ADER-DG methods on classical and degenerate spacetime geometries"
collection: publications
permalink: /publication/2026-02-09-stability-ALE-ADER
excerpt: 'We study the stability of explicit and implicit Arbitrary-Lagrangian-Eulerian (ALE) ADER discontinuous Galerkin (DG) methods on classical and degenerate spacetime geometries for hyperbolic equations. We confirm the CFL stability conditions for the explicit ADER-DG method, specify their limitations, and highlight conditions on mesh velocity for ALE methods.'
date: 2026-02-09
venue: 'ArXiv'
paperurl: 'https://arxiv.org/pdf/2602.09198'
arxiv: 'https://arxiv.org/pdf/2602.09198'
citation: 'Bonafini, M. and Gaburro, E. and Torlo, D. (2026), Stability analysis of Arbitrary-Lagrangian-Eulerian ADER-DG methods on classical and degenerate spacetime geometries, arXiv:2602.09198.'
pdf: /files/publications/bonafini2026stabilityALEADER.pdf
bib: /files/publications/bib/bonafini2026stability.bib
---
In this paper, we present a thorough von Neumann stability analysis of explicit and implicit Arbitrary-Lagrangian-Eulerian (ALE) ADER discontinuous Galerkin (DG) methods on classical and degenerate spacetime geometries for hyperbolic equations. First, we rigorously study the CFL stability conditions for the explicit ADER-DG method, confirming results widely used in the literature while specifying their limitations. Moreover, we highlight under which conditions on the mesh velocity the ALE methods, constrained to a given CFL, are actually stable. Next, we extend the stability study to ADER-DG in the presence of degenerate spacetime elements, with zero size at the beginning and the end of the time step, but with a non zero spacetime volume. This kind of elements has been introduced in a series of articles on direct ALE methods by Gaburro et al. to connect via spacetime control volumes regenerated Voronoi tessellations after a topology change. Here, we imitate this behavior in 1d by fictitiously inserting degenerate elements in between two cells. Then, we show that over this degenerate spacetime geometry, both for the explicit and implicit ADER-DG, the CFL stability constraints remain the same as those for classical geometries, laying the theoretical foundations for their use in the context of ALE methods
