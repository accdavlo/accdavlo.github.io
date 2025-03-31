---
title: "A high-order, fully well-balanced, unconditionally positivity-preserving finite volume framework for flood simulations"
collection: publications
permalink: /publication/2024-02-19-mPDeC-moving-equilibria
excerpt: "We combine the modified Patankar Deferred Correction approach for the positivity of Shallow Water equations with a hydrostatic reconstruction technique to preserve global equilibria. We focus on tough tests aiming at flooding of urban areas."
date: 2024-02-19
venue: 'International Journal on Geomathematics'
paperurl: 'https://doi.org/10.1007/s13137-025-00262-7'
doi: 'https://doi.org/10.1007/s13137-025-00262-7'
arxiv: 'https://arxiv.org/abs/2402.12248'
citation: "M. Ciallella, L. Micalizzi, V. Michel-Dansac, P. Offner and D. Torlo. &quot;A high-order, fully well-balanced, unconditionally positivity-preserving finite volume framework for flood simulations.&quot; Int J Geomath 16, 6 (2025). https://doi.org/10.1007/s13137-025-00262-7."
pdf: /files/publications/ciallella2025highorderSW_GEM.pdf
bib: /files/publications/bib/Ciallella2025HighOrder.bib
---
In this work, we present a high-order finite volume framework for the numerical
simulation of shallow water flows. The method is designed to accurately capture complex dynamics inherent in shallow water systems, particularly suited for
applications such as tsunami simulations. The arbitrarily high-order framework
ensures precise representation of flow behaviors, crucial for simulating phenomena
characterized by rapid changes and fine-scale features. Thanks to an ad-hoc reformulation in terms of production-destruction terms, the time integration ensures
positivity preservation without any time-step restrictions, a vital attribute for
physical consistency, especially in scenarios where negative water depth reconstructions could lead to unrealistic results. In order to introduce the preservation
of general steady equilibria dictated by the underlying balance law, the highorder reconstruction and numerical flux are blended in a convex fashion with a
well-balanced approximation, which is able to provide exact preservation of both
static and moving equilibria. Through numerical experiments, we demonstrate the effectiveness and robustness of the proposed approach in capturing the intricate dynamics of shallow water flows, while preserving key physical properties
essential for flood simulations.
