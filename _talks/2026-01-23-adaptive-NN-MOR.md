---
title: "Adaptive Neural Networks for Reduced Order Modeling"
collection: talks
type: "Talk"
permalink: /talks/2026-01-23-adaptive-NN-MOR
venue: "UMI Workshop 2026"
date: 2026-01-23
location: "Rome, Italy"
pdf: /files/talks/adaptiveNN_torlo_UMI26.pdf
---

Neural networks (NNs) have become widespread over the last decade, taking a leading role in many fields, including function approximation. Nevertheless, there remains a significant gap between the theoretical results on the expressive capacity of neural networks and their everyday practical usage. In particular, the choice of architecture, specifically, the number of layers and neurons, is often excessive relative to the actual error achieved. Cai and collaborators have produced a series of works on adaptive neural networks [1], with the primary aim of better interpreting neural networks through the use of simple and shallow architectures. In particular, they demonstrated that using ReLU activation functions in networks with one or two hidden layers allows the NN to be described as a piecewise linear function, with breakpoints determined by the weights and biases. This approach enables the adaptive refinement of the network, by adding nodes or layers in specific locations, following a philosophy similar to that of adaptive finite element methods (FEM). It leads to much more accurate networks that quickly converge to the desired solution, even in the presence of strong discontinuities, while employing very small architectures. However, this approach is highly dependent on the dimension of the network's domain. For geometries of dimension greater than two, it essentially requires the use of meshing tools at every iteration. We applied this idea in the context of model order reduction for parametric problems. We tried several approaches to extend this framework to the parametric setting. One possibility is to treat the parameters as additional input dimensions, which leads to the aforementioned challenges. An alternative approach considers the biases of the neural network as parameter-dependent. This enables the same expressiveness as networks with extra input dimensions, while maintaining the simplicity of analyzing geometric structures for fixed parameters. We compare these approaches, demonstrating the capabilities of such networks relative to classical architectures. 

[1] Liu Min, Zhiqiang Cai, and Jingshuang Chen. Adaptive two-layer ReLU neural network: I. Best least-squares approximation. Computers \& Mathematics with Applications 113 (2022): 34-44. https://doi.org/10.1016/j.camwa.2022.03.005
