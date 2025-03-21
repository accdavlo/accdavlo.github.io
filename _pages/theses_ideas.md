---
layout: archive
title: "Theses"
permalink: /theses/
author_profile: true
---

{% include base_path %}


Ideas for Master Theses
======
* Structure preserving methods
   * Metodi che preservano equilibri di movimento per Shallow Water (se sei più interessato alla modellistica possiamo estendere questa cosa a modelli più complicati: multi-layer, Ripa models, sediment transport, ... 1D o 2D
   * Metodi alto ordine che preservano la positività di quantità che son fisicamente positive (tipo l'altezza della colonna d'acqua) magari in combinazione con la preservazione di qualche equilibrio
   * Studiare metodi di ordine arbitrariamente alto impliciti efficienti
   * Metodi DG di ordine arbitrariamente alto per problemi iperbolici con dei limiter adattivi che capiscano quando ci sono shock o simili per abbassare l'ordine

* Model order reduction: sono modelli che permettono di ridurre i costi computazionali per problemi parametrici quando servono tante simulazioni per diversi parametri (per esempio in contesti di Uncertainty Quantification).
   * Studiare delle rete neurali che facciano da surrogato a metodi numerici
   * NN adattive per ROM
   * usare metodi un po' più classici cercando di preservare equilibri delle equazioni
   * preservare le disuguaglianze di entropia 
   
   
Ideas for Bachelor Theses
=====
* ODE (vedi anche [corso su metodi alto ordine per ODE](https://github.com/accdavlo/HighOrderODESolvers)
   1. Metodi Modified Patankar: sono variazioni linearmente implicite di metodi espliciti (sia RK che multistep), dove si preserva la positività della quantità d'interesse. Possiamo studiarne delle versioni ad alto ordine, la loro stabilità o concentrarci su applicazioni più complesse.
   2. Metodi predictor-corrector di ordine arbitrariamente alto: possiamo vederne alcuni nella loro versione implicita (lineare), studiarne la stabilità e confrontarli con dei RK impliciti classici con Newton implicito come risolutore e vedere chi è più veloce.
   3. Metodi di rilassamento per conservare l'entropia globale del sistema. Son dei metodi che cambiano leggermente il timestep alla fine del metodo stesso, ottenendo così la conservazione a livello numerico di una quantità conservata del sistema, per esempio l'energia totale in Newton. Possiamo vedere come si derivano, la dimostrazione che l'ordine si mantiene e che preservano la quantità che stiamo cercando.
   

* PDE
   1. Applicare il rilassamento dell'entropia a problemi iperbolici che conservano l'entropia (o che la dissipano), e.g. Burgers con flusso numerico di Tadmor.


