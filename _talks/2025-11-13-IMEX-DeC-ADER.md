---
title: "Stability of implicit and IMEX ADER and DeC schemes"
collection: talks
type: "Talk"
permalink: /talks/2025-11-13-IMEX-DeC-ADER
venue: "High Order Structure-Preserving Semi-implicit Schemes for Hyperbolic Equations"
date: 2025-11-13
location: "Rome, Italy"
pdf: /files/talks/roma_prin_imex_dec_ader.pdf
---

Deferred Correction (DeC) and Arbitrary DERivative (ADER) methods are iterative solvers used to approximate solutions of hyperbolic partial differential equations (PDEs). When the spatial discretization—typically a Discontinuous Galerkin (DG) method in the case of ADER—is factored out, these schemes can be interpreted as Runge–Kutta (RK) methods. In particular, they can be expressed in terms of two operators: a low-order RK scheme (which may be explicit, implicit, or IMEX) and a high-order implicit RK scheme, whose combination through successive iterations yields the final method. We observe that the high-order implicit RK scheme usually possesses favorable stability properties (A-stability, L-stability), and these properties are often inherited by the implicit iterative method.

[Slides](/files/talks/roma_prin_imex_dec_ader.pdf)
[Publication](/publication/2024-04-30-IMEX-ADER-DeC)

