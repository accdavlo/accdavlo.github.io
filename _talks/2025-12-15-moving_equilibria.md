---
title: "How to Preserve Moving Equilibria: Global Flux and Analytical Methods"
collection: talks
type: "Talk"
permalink: /talks/2025-12-15-moving_equilibria
venue: "Workshop on ROM and CFD: Inria-Rome-CWI"
date: 2025-12-15
location: "Università di Roma La Sapienza, Italy"
pdf: /files/talks/files/talks/GF_SUPG_FV_roma_15_12_25.pdf
---

Many conservation and balance laws feature families of moving steady states that are essential to preserve at the numerical level. Various techniques have been proposed to achieve this, broadly categorized into well-balanced (WB), and exactly well-balanced (EWB) schemes. WB schemes aim to preserve a numerical equilibrium of the discrete operators, often resulting in super-convergence methods or significantly reduced errors (by several orders of magnitude). EWB schemes, on the other hand, maintain an exact equilibrium (to machine precision) by satisfying an analytical relationship dictated by the equilibrium variables while accounting for the discretization of source terms. In this talk, we compare these methods and analyze the advantages and limitations of each. Specifically, we will consider the well-balanced technique for the Shallow Water equations proposed in [1] and applied in [2] for 1D-like moving equilibria, in contrast to the Global Flux technique used in [3] and [4] for 1D moving equilibria and in [5,6] for 2D divergence-free moving equilibria.

[1] Michel-Dansac, V., Berthon, C., Clain, S., & Foucher, F. (2016)\
[2] Ciallella, M., Micalizzi, L., Michel-Dansac, V., Öffner, P., & Torlo, D. (2024) [post](/publications/2024-02-19-mPDeC-moving-equilibria)\
[3] Ciallella, M., Torlo, D., & Ricchiuto, M. (2023) [post](/publications/2022-05-27-global-flux)\
[4] Chertock, A., Kurganov, A., Liu, X., Liu, Y., & Wu, T. (2022)\
[5] Barsukow, W., Ricchiuto, M., & Torlo, D. (2025) [post](/publications/2024-07-15-SUPG-GF)\
[6] Barsukow, W., Ricchiuto, M., & Torlo, D. (2026) [post](/publications/2025-10-03-stationarity-FEM-GF-affine)\

[Slides](/files/talks/files/talks/GF_SUPG_FV_roma_15_12_25.pdf)

