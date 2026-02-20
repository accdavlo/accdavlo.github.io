---
layout: archive
title: "Theses"
permalink: /theses/
author_profile: true
---

{% include base_path %}


Ideas for Master Theses
======
* **Structure preserving methods for hyperbolic models**
   1. Metodi che preservano equilibri di movimento per Shallow Water (se sei più interessato alla modellistica possiamo estendere questa cosa a modelli più complicati: multi-layer, Ripa models, sediment transport, ... 1D o 2D
   2. Metodi alto ordine che preservano la positività di quantità che son fisicamente positive (tipo l'altezza della colonna d'acqua) magari in combinazione con la preservazione di qualche equilibrio
   3. Studiare metodi di ordine arbitrariamente alto impliciti efficienti
   4. Metodi DG di ordine arbitrariamente alto per problemi iperbolici con dei limiter adattivi che capiscano quando ci sono shock o simili per abbassare l'ordine

* **Model order reduction**: sono modelli che permettono di ridurre i costi computazionali per problemi parametrici quando servono tante simulazioni per diversi parametri (per esempio in contesti di Uncertainty Quantification). (vedi [intro a MOR](/posts/2021/02/wMOR/))
   1. Studiare delle rete neurali che facciano da surrogato a metodi numerici
   2. NN adattive per ROM
   3. usare metodi un po' più classici cercando di preservare equilibri delle equazioni
   4. preservare le disuguaglianze di entropia 

* **High order multiscale method for fluid dynamics**
   1. Relaxation
   2. Splitting method [Semi-implicit relaxed finite volume schemes for hyperbolic multi-scale systems of conservation laws](https://arxiv.org/abs/2502.15402)
   3. High order with Deferred Correction (sDeC)
   
   
Ideas for Bachelor Theses
=====
* **ODE** (vedi anche [corso su metodi alto ordine per ODE](https://github.com/accdavlo/HighOrderODESolvers) )
   1. Metodi per ODE con timestep complessi [https://arxiv.org/pdf/2601.07730](https://arxiv.org/pdf/2601.07730)
   1. Metodi di rilassamento per conservare l'entropia globale del sistema. Son dei metodi che cambiano leggermente il timestep alla fine del metodo stesso, ottenendo così la conservazione a livello numerico di una quantità conservata del sistema, per esempio l'energia totale in Newton. Possiamo vedere come si derivano, la dimostrazione che l'ordine si mantiene e che preservano la quantità che stiamo cercando. [lezione](https://github.com/accdavlo/HighOrderODESolvers/blob/master/Chapter%204%20Relaxation%20Runge--Kutta.ipynb)
   1. Metodi Modified Patankar: sono variazioni linearmente implicite di metodi espliciti (sia RK che multistep), dove si preserva la positività della quantità d'interesse. Possiamo studiarne delle versioni ad alto ordine, la loro stabilità o concentrarci su applicazioni più complesse. [lezione](https://github.com/accdavlo/HighOrderODESolvers/blob/master/Chapter%206%20Positivity%20preserving%20schemes.ipynb)
   1. Metodi predictor-corrector di ordine arbitrariamente alto: possiamo vederne alcuni nella loro versione implicita (lineare), studiarne la stabilità e confrontarli con dei RK impliciti classici con Newton implicito come risolutore e vedere chi è più veloce. [lezione](https://github.com/accdavlo/HighOrderODESolvers/blob/master/Chapter%205%20DeC%20and%20ADER.ipynb)
   1. Derivazione delle condizioni d'ordine d'accuratezza per metodi di Runge-Kutta con la teoria degli alberi [libro Butcher](https://onlinelibrary.wiley.com/doi/book/10.1002/9781119121534)
* **PDE**
   1. Variational Physics Informed Neural Networks: fissare $N$ test function da usare nella formulazione del residuo con un a formulazione debole, quindi nella loss minimizzare la somma dei residui testati contro ciascuna test function al quadrato.
   1. Self-adaptive Physics Informed Neural Networks: PINN dove i pesi che bilanciano IC, BC e residuo sono a loro volta delle NN che vengono allenate per massimizare la loss, così che diano più peso a ciò che non è ben ottimizato. [article](https://arxiv.org/abs/2009.04544)
   1. Applicare il rilassamento dell'entropia a problemi iperbolici che conservano l'entropia (o che la dissipano), e.g. Burgers con flusso numerico di Tadmor.
   1. Discontinuous Galerkin per conservation laws (traffico, Burgers, acque basse): teoria, convergenza, analisi e implementazione.
   1. Le equazioni di Navier-Stokes: formulazione, problemi di punto-sella, stabilizzazione, approssimazione con elementi finiti.
   1. Decomposizione del dominio e schemi iterativi per la convergenza del solutore.


