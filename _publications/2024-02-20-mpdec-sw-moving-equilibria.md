---
title: "A high-order, fully well-balanced, unconditionally positivity-preserving finite volume framework for flood simulations"
collection: publications
permalink: /publication/2024-02-20-mpdec-sw-moving-equilibria
excerpt: 'For shallow water equations, we combine the modified Patankar DeC scheme in time to have the positivity of the water height and arbitrarily high order of accuracy and a simple low order approach to preserve moving equilibria.'
date: 2024-02-20
venue: 'ArXiv'
paperurl: 'https://arxiv.org/abs/2402.12248'
arxiv: 'https://arxiv.org/abs/2402.12248'
citation: 'Ciallella, M., Micalizzi, L., Michel-Dansac, V., Öffner, P., & Torlo, D. (2024). A high-order, fully well-balanced, unconditionally positivity-preserving finite volume framework for flood simulations. arXiv preprint arXiv:2402.12248.'
pdf: /files/publications/Ciallella2024high.pdf
bib: /files/publications/bib/ciallella2024high.bib
---
In this work, we present a high-order finite volume framework for the numerical simulation of shallow water flows. The method is designed to accurately capture complex dynamics inherent in shallow water systems, particularly suited for applications such as tsunami simulations. The arbitrarily high-order framework ensures precise representation of flow behaviors, crucial for simulating phenomena characterized by rapid changes and fine-scale features. Thanks to an {\it ad-hoc} reformulation in terms of production-destruction terms, the time integration ensures positivity preservation without any time-step restrictions, a vital attribute for physical consistency, especially in scenarios where negative water depth reconstructions could lead to unrealistic results. In order to introduce the preservation of general steady equilibria dictated by the underlying balance law, the high-order reconstruction and numerical flux are blended in a convex fashion with a well-balanced approximation, which is able to provide exact preservation of both static and moving equilibria. Through numerical experiments, we demonstrate the effectiveness and robustness of the proposed approach in capturing the intricate dynamics of shallow water flows, while preserving key physical properties essential for flood simulations.
