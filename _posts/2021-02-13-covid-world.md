---
title: 'How is testing going for different World countries for the SARS-CoV-2 pandemic'
date: 2021-02-01
permalink: /posts/2021/02/covid-world/
tags:
  - Covid19
  - Testing
  - World comparison
  - New Cases
  - New Deaths
  - Case Fatality Rate
  - CFR
---

This post is based on the observation I made some months ago in a [Twitter post](https://twitter.com/accdavlo/status/1335657681156247552).

### Summary


## Basic Knowledge on the Fatality rate of the Virus
It is clear at the moment, that the SARS-Cov-2 has a case fatality rate (CFR) which highly depends on the age and the co-existance of other illnesses. In particular, the CFR depends exponentially on the age `[1]` as shown also by [ourWorldInData](https://ourworldindata.org/mortality-risk-covid#case-fatality-rate-of-covid-19-by-age). 

For an average European country it has been estimated that the CFR should be in the interval 1%-1.5% (with the original variant, in the future it might change). This piece of information can be used to determine the quality of the testing strategy and capacity of a certain country (and soon which variant will be dominant in the country). Indeed, from communicated cases and deaths, we can estimate the apparent CFR and compare it with the expected one.

In particular I set up an [Ipython notebook](https://colab.research.google.com/drive/13agn1qMRO8NFMTY0yOfSGW2H37V5C_Rh?usp=sharing) where one can compare the cases and the deaths supposing an apparent CFR and the delay between the report of the cases and the report of the death (in Italy estimated in about 12 days).
 
Fatality 2%             |  Fatality 3% 
:-------------------------:|:-------------------------:
![Cases vs Deaths in Italy: Fatality 2%](/images/postCovid/casesVsDeathsItalyFat2.png)|![Cases vs Deaths in Italy: Fatality 3%](/images/postCovid/casesVsDeathsItalyFat3.png)


`[1]` Undurraga, E.A., Chowell, G. & Mizumoto, K. COVID-19 case fatality risk by age and gender in a high testing setting in Latin America: Chile, March–August 2020. Infect Dis Poverty 10, 11 (2021). [https://doi.org/10.1186/s40249-020-00785-1](https://doi.org/10.1186/s40249-020-00785-1)
