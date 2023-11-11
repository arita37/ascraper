 
all -  [ What goes in where ](https://www.reddit.com/gallery/17sdsxr) , 2023-11-11-0909
```

```
---

     
 
all -  [ [D] Is there a limit to the number of papers we can submit to NeurIPS? ](https://www.reddit.com/r/MachineLearning/comments/17s8ade/d_is_there_a_limit_to_the_number_of_papers_we_can/) , 2023-11-11-0909
```
I am asking for a friend.
```
---

     
 
all -  [ Neurio - Still a viable Home Energy Monitoring Solution! ](https://www.reddit.com/r/homeassistant/comments/17ryzw6/neurio_still_a_viable_home_energy_monitoring/) , 2023-11-11-0909
```
I've had the Neurio Home Energy Monitor (USA, Split Phase) for many, many years. Since they first came to the market, I 
was an early adapter. 
And it's been **rock solid**.

I just ordered another one for my cabin. (New in box from eBay, ab
out $60 after shipping (I set up scheduled alert, and low-balled a best offer)
I had it up and running in minutes. (Conn
ected to WiFi, registered to my existing cloud account, API enabled, and integrated in Home Assistant). 

Despite being 
vaporware and sold off to Generac and later abandoned, the API lives on,and the Home Assistant integration keeps working
. 
AND EVEN IF THEY DO KILL THE API (Aka, 'The MyQ treatment'), THERE IS STILL LOCAL ACCESS. (Which I don't use, YET)

*
*Existing Home Assistant integration:**  
https://www.home-assistant.io/integrations/neurio_energy  
Two sensors will be
 created with the following names:   
* Energy Usage: Current active power usage in Watts. Updated every 10 seconds.   

* Daily Energy Usage: Daily power usage in kWh. Updated every 2.5 minutes.   

Polls via the cloud API (Which is still a
ctive!)  
https://api-docs.neur.io/#overview   

   
**Local Sensor Access:**  
JSON via IP:  
Example:   
http://192.16
8.1.xxxx/current-sample   
https://api-docs.neur.io/#sensor-local-access   
And in case the cloud doc ever goes missing,
 I've cloned it here: https://pastebin.com/raw/7YUCSzCe
   

Food for thought for those looking for an energy monitoring
 solution, but don't want to shell out a lot of money. 
I was about to pull the trigger on the 'DIY-ish' methods, but af
ter getting the board, CT sensors, etc, it will still going to cost at least $100. On top of that, forums are full of pe
ople struggling to set them up, calibrate them properly, etc.  I wasn't up for the task. I wanted a turn-key solution re
ady out of the box.

https://imgur.com/oBA0txf
```
---

     
 
all -  [ Quant research of the Week (2nd Edition) ](https://www.reddit.com/r/quant/comments/17qms5i/quant_research_of_the_week_2nd_edition/) , 2023-11-11-0909
```
# ArXiv

## Finance

[**Maximizing Portfolio Predictability with Machine Learning: Portfolio Predictability Maximization
 using ML**](https://arxiv.org/abs/2311.01985):  A stock portfolio called the maximally predictable portfolio (MPP),  cr
eated using machine learning and a Kelly criterion strategy,  consistently performs better than the benchmark. (2023-11-
03, shares: 5)

[**Arbitrage Opportunities in Mean Field System**](https://arxiv.org/abs/2311.02690):  The article prese
nts a theoretical model to analyze arbitrage  opportunities in a market with unlimited investors, confirming the  existe
nce of a unique mean field equilibrium. (2023-11-05, shares: 3)

[**Transfer Risk and Finance Applications**](https://ar
xiv.org/abs/2311.03283):  The paper discusses the concept of transfer risk in transfer learning,  showing its significan
t relation with performance and its effectiveness  in selecting suitable source tasks in stock return prediction and  po
rtfolio optimization. (2023-11-06, shares: 2)

[**Power Law in Sandwiched Volterra Volatility Model: Power Law in Volter
ra Volatility Model**](https://arxiv.org/abs/2311.01228):  The Sandwiched Volterra Volatility (SVV) model accurately rep
roduces  the power-law behavior of the at-the-money implied volatility skew,  provided the correct Volterra kernel is ch
osen. (2023-11-02, shares: 4)

[**Optimal Stopping Problem with Discontinuous Reward**](http://dx.doi.org/10.13140/rg.2.
2.36565.40160):  The study investigates the optimal stopping issue in pricing a variable  annuity contract, introducing 
new valuation algorithms and showing how  fee and surrender charge functions affect early and optimal surrender  boundar
ies. (2023-11-06, shares: 2)

[**Joint Model for Longitudinal and Spatio-Temporal Survival Data: Longitudinal and Spatio
-Temporal Survival Model**](https://arxiv.org/abs/2311.04008):  The Spatio-Temporal Joint Model (STJM) is a new method f
or credit risk  analysis that uses spatial and temporal data to predict a borrower's  risk, showing better results when 
spatial data is included. (2023-11-07,  shares: 7)

## Miscellaneous

[**Finding Fraud Prevention Rules**](https://arxiv
.org/abs/2311.00964):  The paper introduces PORS, a heuristic-based framework for finding  high-quality rule subsets in 
fraud prevention, and SpectralRules, a new  sequential covering algorithm, showcasing their effectiveness in two  real A
lipay scenarios. (2023-11-02, shares: 4)

[**Asset Price Bubbles: Nonstationary Phenomenon**](https://arxiv.org/abs/2311
.03638):  The article discusses the theory of rational asset price bubbles,  highlighting that bubbles linked to real as
sets like stocks and housing  are nonstationary phenomena tied to unbalanced growth. (2023-11-07,  shares: 4)

[**Decent
ralization in Blockchain Governance and DeFi Efficiency**](https://arxiv.org/abs/2311.02434):  The article studies how d
ecentralization in blockchain-based governance  affects the financial efficiency of Decentralized Autonomous  Organizati
ons (DAOs). It uses the Gini coefficient to measure inequality  among token owners and discusses the pros and cons of th
is method.  (2023-11-04, shares: 4)

## Historical Trending

[**Deep Learning for Volatility Calibration**](https://arxi
v.org/abs/2201.07880):  The paper presents a new algorithm that uses deep self-consistent  learning for better and more 
robust calibration of local volatility from  market option prices. (2021-12-09, shares: 15)

[**Wage-Setting and Behavio
ral Firms**](https://arxiv.org/abs/2206.01114):  The study suggests that companies that set salaries at round numbers,  
typically less sophisticated firms, tend to perform worse in the market  due to their coarse wage-setting approach. (202
2-06-02, shares: 125)

[**Pragmatic Energy Markets**](https://arxiv.org/abs/2305.01485):  The article offers a guide on 
using the Heath-Jarrow-Morton framework  in energy markets, specifically in European power and gas markets,  covering ma
rket structure, model calibration, simulations, and  derivatives pricing. (2023-05-02, shares: 56)

[**Multimodal Bankru
ptcy Prediction**](https://arxiv.org/abs/2211.08405):  The research presents multimodal learning in bankruptcy predictio
n  models to tackle the problem of missing MDA section in Form 10-K,  showing improved classification performance and ad
dressing the  limitation of previous models. (2022-10-26, shares: 33)

[**Liquidation with High Risk Aversion**](https:/
/arxiv.org/abs/2301.01555):  The research investigates the Bachelier model with linear price impact,  identifying a set 
of portfolios that are optimally effective in a  scenario of diminishing price impact. (2023-01-04, shares: 10)

&#x200B
;

# SSRN

### Recently Published

## Financial

[**Concave Price Impact Trading**](https://papers.ssrn.com/sol3/papers.
cfm?abstract_id=4625040):  The research examines statistical arbitrage issues, taking into account  the nonlinear and te
mporary price impact of metaorders, and shows that  simple trading rules can be established even with nonparametric alph
a  and liquidity signals. (2023-11-06, shares: 120.0)

[**Volatility Disagreement Trading**](https://papers.ssrn.com/sol
3/papers.cfm?abstract_id=4624158):  A model is created to understand how investors' disagreement on future  volatility a
ffects their trading of volatility derivatives, showing that  trading decreases in more volatile periods and the varianc
e risk  premium can become positive when future volatility is underestimated.  (2023-11-06, shares: 3.0)

[**Global Macr
o and Managed Futures Hedge Fund Strategies**](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4625978):  The resear
ch evaluates the performance of hedge funds, especially those  using a top-down investment approach, and discovers a sig
nificant drop  in risk-adjusted alpha for global macro managers and managed futures  managers after the global financial
 crisis. (2023-11-07, shares: 8.0)

[**Market Volatility and Trend Factor**](https://papers.ssrn.com/sol3/papers.cfm?abs
tract_id=4621388):  The paper explores the link between stock market volatility and trend  factor profits, finding that 
the trend factor performs better after high  volatility periods as investors depend more on trend signals.  (2023-11-02,
 shares: 3.0)

[**The Halo Effect in ESG Investing in Indian Equities**](https://papers.ssrn.com/sol3/papers.cfm?abstrac
t_id=4624179):  A study of 700 Indian companies shows no significant link between ESG  scores and investment returns fro
m 2013 to 2023. (2023-11-06, shares:  10.0)

[**The Kelly Criterion in Stock Investment**](https://papers.ssrn.com/sol3/
papers.cfm?abstract_id=4625295):  A paper suggests using the Kelly criterion and Monte Carlo simulation  to estimate the
 optimal portfolio in stock investment. (2023-11-07,  shares: 7.0)

[**Strategic Investors and Exchange Rate Dynamics**]
(https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4621461):  A study shows that exchange rate dynamics are affected b
y the diversity  of investors and their price impact, with more concentrated markets  having a stronger price impact. (2
023-11-02, shares: 3.0)

## Quantitative

[**Leverage Effect and Volatility of Volatility Estimation**](https://papers.s
srn.com/sol3/papers.cfm?abstract_id=4625351):  The article presents new methods for estimating leverage effect and  vola
tility using high frequency data, tested through simulation and real  data analysis. (2023-11-07, shares: 3.0)

[**Machi
ne Learning for Insolvency Prediction in Insurance**](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4626405):  A n
ew machine learning algorithm, SANN, is used to predict insurance  company insolvency, showing better accuracy than trad
itional models.  (2023-11-08, shares: 3.0)

[**Investor Risk Appetite and High-Beta Stock Valuation Analysis**](https://
papers.ssrn.com/sol3/papers.cfm?abstract_id=4623331):  The study reveals a pattern in high-beta stock returns around  ma
croeconomic announcements, indicating that investor risk appetite  significantly influences these returns. (2023-11-04, 
shares: 3.0)  

[**Sector Portfolio HRP: Performance and Risk Metrics**](https://papers.ssrn.com/sol3/papers.cfm?abstrac
t_id=4623991):  A diversified portfolio strategy, Sector Portfolio HRP, outperforms the  MSCI All Country World Index in
 annualized return and risk evaluation  from 1996 to 2022, a study shows. (2023-11-03, shares: 4.0)

[**Identifying Domi
nance Regimes in the Euro Area with Machine Learning**](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4622203):  M
achine learning has identified periods of fiscal dominance in the euro  area from 2000 to 2019, including during the fin
ancial and sovereign  debt crises. (2023-11-03, shares: 2.0)

[**Corporate Culture and Takeover Vulnerability**](https:/
/papers.ssrn.com/sol3/papers.cfm?abstract_id=4626185):  Research using machine learning indicates that the threat of hos
tile  takeovers can significantly weaken a company's culture, supporting the  managerial myopia hypothesis. (2023-11-07,
 shares: 3.0)

&#x200B;

### Recently Updated

## Quantitative

[**Bayesian Data Imputation: Missing Data Filling**](htt
ps://papers.ssrn.com/sol3/papers.cfm?abstract_id=4625229):  The article highlights the role of data imputation in risk m
anagement,  explaining its use in filling gaps in incomplete data for a better  understanding of risk factors. (2023-06-
28, shares: 189.0)

[**Machine Learning Execution Time in Asset Pricing**](https://papers.ssrn.com/sol3/papers.cfm?abstr
act_id=4623947):  The research analyzes the execution time of machine learning models in  empirical asset pricing, findi
ng that XGBoost is the fastest and most  accurate, and that reducing features and time observations can  significantly c
ut execution time. (2023-10-31, shares: 2.0)

[**Interactions in Asset Pricing: Predictors & Returns**](https://papers.s
srn.com/sol3/papers.cfm?abstract_id=4624629):  The research suggests that future stock returns can be predicted using  m
achine learning models that consider characteristics and macroeconomic  variables, resulting in portfolios that perform 
better than benchmarks.  (2023-07-17, shares: 494.0)

[**Corporate Bonds: Momentum Spillovers**](https://papers.ssrn.com
/sol3/papers.cfm?abstract_id=4622610):  The article uncovers momentum spillovers in the corporate bond market,  proposin
g a strategy of buying bonds from high-performing peers and  selling bonds from low-performing peers, yielding a monthly
 alpha of 36  basis points. (2023-09-25, shares: 2.0)

[**Alternate Approach: Regression Parameter Estimation**](https:/
/papers.ssrn.com/sol3/papers.cfm?abstract_id=4621745):  The article presents a new NAS method for univariate regression 
 problems, comparing it with standard methods and suggesting a  generalized approach for calculating the cost function's
 partial  derivatives. (2023-09-01, shares: 2.0)

## Financial

[**Efficient Simulation for Derivative Pricing**](https:
//papers.ssrn.com/sol3/papers.cfm?abstract_id=4625397):  The article introduces a new simulation-based method for pricin
g and  managing risk of financial derivatives during rare events, proving to be  more efficient, accurate, and flexible 
than traditional methods.  (2022-06-08, shares: 85.0)

[**Commodity Sectors and Factor Strategies**](https://papers.ssrn
.com/sol3/papers.cfm?abstract_id=4622974):  The study explores the impact of commodity sectors on commodity futures  ris
k premiums, revealing that excluding the precious metal sector from a  portfolio increases the Sharpe ratio, suggesting 
precious metals' role  as hedging tools affects commodity performance. (2023-10-13, shares:  3.0)

[**Optimal Valuation 
Ratio: Forward Price Ratios**](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4625138):  The research criticizes th
e use of trailing price ratios for predicting  stock market returns due to changes in cash flow growth, suggesting the  
use of forward price ratios scaled by cash flow forecasts for better  valuation. (2022-12-02, shares: 2.0)

[**CDS Theor
y and Practice**](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4624435):  The paper examines Quanto Credit Defaul
t Swaps, a financial tool that  transfers credit risk with foreign exchange exposure, focusing on its  theory, pricing, 
and use in emerging markets like Brazil. (2023-09-15,  shares: 75.0)

[**Volatility Timing with ETF Options**](https://p
apers.ssrn.com/sol3/papers.cfm?abstract_id=4625085):  The study finds that hedge funds' positions in ETF options predict
  volatility in underlying ETF returns, particularly in nonequity ETFs  like fixed income and currency ETFs. (2022-10-19
, shares: 2.0)

[**ETF Closures: Do Nothing?**](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4620553):  The resea
rch indicates that ETFs often close after positive returns and  flows, with these factors predicting closure decisions, 
and smaller  ETFs earning higher daily returns than larger ones with the same  investment objective. (2023-01-23, shares
: 60.0)

[**Volatility Transformers: Arbitrage-Free Volatility Surfaces**](https://papers.ssrn.com/sol3/papers.cfm?abstr
act_id=4623940):  The paper presents a framework for creating arbitrage-free  transformations of an implied volatility s
urface using optimal transport  maps, which can be applied to a broader range of synthetic market data  generation appli
cations. (2023-09-05, shares: 2.0)

[**Common Ownership of Stocks & the Low Volatility Anomaly**](https://papers.ssrn.co
m/sol3/papers.cfm?abstract_id=4626091):  The study shows that the low volatility anomaly in stock prices is  connected t
o mutual funds performance evaluation against benchmark  indexes, as mutual fund managers' heavy investment in certain s
tocks  leads to higher trade volumes and lower volatility. (2023-04-11, shares:  2.0)

&#x200B;

# ArXiv ML

## Recently
 Published

[**IGN**](https://arxiv.org/abs/2311.01462):  A new generative modeling method is suggested, using an idempo
tent  neural network to project any input into a target data distribution.  (2023-11-02, shares: 157)

[**TMKWF**](https
://arxiv.org/abs/2311.01434):  A novel data augmentation technique is proposed that adjusts the  distribution of interpo
lation coefficients based on data point  similarity, enhancing model performance and calibration. (2023-11-02,  shares: 
11)

[**CM: UHL**](https://arxiv.org/abs/2311.01435):  A new algorithm is introduced that can learn high-dimensional  ha
lfspaces in d-dimensional space in polynomial time, without needing  labels. (2023-11-02, shares: 11)

[**T A PTMF**](ht
tps://arxiv.org/abs/2311.01449):  TopicGPT, a new framework, is introduced that uses large language  models to identify 
latent topics in a text collection, providing more  interpretable topics and user control. (2023-11-02, shares: 9)

[**U
niO4: Unifying RL**](https://arxiv.org/abs/2311.03351):  Uni-o4 is a novel method that merges offline and online reinfor
cement  learning, enhancing the adaptability of the learning process.  (2023-11-06, shares: 5)

[**Reproducible Paramete
r Inference**](https://arxiv.org/abs/2311.02019):  The BayesBag study introduces a technique of applying bagging to  Bay
esian posteriors to enhance reproducibility and uncertainty  quantification in model misspecification. (2023-11-03, shar
es: 5)

[**PPI: Efficient Inference**](https://arxiv.org/abs/2311.01453):  PPI++ is a new approach that utilizes a small
 labeled dataset and a  larger machine-learning predictions dataset to boost computational and  statistical efficiency. 
(2023-11-02, shares: 5)

&#x200B;

# RePec

## Finance

[**High-Frequency Alternative Data for GDP Nowcasts**](https://e
conpapers.repec.org/scripts/redir.pf?u=http%3A%2F%2Flink.springer.com%2F10.1007%2Fs41549-023-00085-1;h=repec:spr:jbuscr:
v:19:y:2023:i:2:d:10.1007_s41549-023-00085-1):  The study uses credit card data to enhance real-time GDP forecasting in 
 Japan, demonstrating that this data improves early-stage forecasting by  accurately capturing consumer spending. (2023-
11-08, shares: 15.0)

[**Performance of U.S. ESG ETFs**](https://econpapers.repec.org/scripts/redir.pf?u=https%3A%2F%2Fw
ww.mfa.com.my%2Fwp-content%2Fuploads%2F2023%2F09%2Fv31_i2_a5_pg89-101.pdf;h=repec:mfa:journl:v:31:y:2023:i:2:p:89-101): 
 The paper analyzes the performance of ESG equity ETFs in the U.S. from  2019 to 2021, revealing that these ETFs, on ave
rage, outperform the  S&P 500 Index. (2023-11-08, shares: 15.0)

[**High-Dimensional Portfolio Optimization with Factor 
Model**](https://econpapers.repec.org/scripts/redir.pf?u=http%3A%2F%2Fwww.sciencedirect.com%2Fscience%2Farticle%2Fpii%2F
S0927538X23001774;h=repec:eee:pacfin:v:81:y:2023:i:c:s0927538x23001774):  The article proposes a new portfolio optimizat
ion method using a  tree-structured portfolio sorting technique, demonstrating that this  strategy outperforms others in
 terms of Sharpe ratios, standard  deviation, and turnover. (2023-11-08, shares: 15.0)

[**Time-Variation in Effects on 
Portfolio Flows**](https://econpapers.repec.org/scripts/redir.pf?u=http%3A%2F%2Fwww.sciencedirect.com%2Fscience%2Farticl
e%2Fpii%2FS0165188923001628;h=repec:eee:dyncon:v:156:y:2023:i:c:s0165188923001628):  The research examines the relative 
significance of push and pull  factors for portfolio flows during financial crises, finding that the  importance of push
 factors has increased over time, especially for EU  countries. (2023-11-08, shares: 14.0)

[**Dynamic Bond Portfolio Op
timization with Stochastic Interest Rate Model**](https://econpapers.repec.org/scripts/redir.pf?u=http%3A%2F%2Flink.spri
nger.com%2F10.1007%2Fs10690-023-09401-2;h=repec:kap:apfinm:v:30:y:2023:i:4:d:10.1007_s10690-023-09401-2):  The paper pro
poses a new framework for dynamic bond portfolio  optimization over multiple periods, which outperforms single-period  o
ptimization. (2023-11-08, shares: 26.0)

[**Multiperiod Portfolio Allocation with Volatility Clustering and Non-Normalit
ies**](https://econpapers.repec.org/scripts/redir.pf?u=http%3A%2F%2Fwww.sciencedirect.com%2Fscience%2Farticle%2Fpii%2FS1
062940823001201;h=repec:eee:ecofin:v:68:y:2023:i:c:s1062940823001201):  The study finds that considering volatility clus
tering in dynamic  multiperiod portfolio choices reduces the need for hedging. (2023-11-08,  shares: 23.0)

[**Managed E
TFs: Performance Evaluation**](https://econpapers.repec.org/scripts/redir.pf?u=https%3A%2F%2Fwww.mfa.com.my%2Fwp-content
%2Fuploads%2F2022%2F10%2Fv30_i2_a3_pg39-61.pdf;h=repec:mfa:journl:v:30:y:2022:i:2:p:39-61):  A study found that actively
 managed ETFs in the US from 2018 to 2021  did not yield significant above-market returns and their managers lacked  sup
erior market timing skills. (2022-07-09, shares: 18.0)

## Statistical

[**Gender Diversity Prediction in Boardrooms wit
h ML**](https://econpapers.repec.org/scripts/redir.pf?u=http%3A%2F%2Fwww.sciencedirect.com%2Fscience%2Farticle%2Fpii%2FS
0275531923001794;h=repec:eee:riibaf:v:66:y:2023:i:c:s0275531923001794):  A study uses machine learning to forecast gende
r diversity in Chinese  company boards, with the extreme Gradient Boosting model showing the  best performance. (2023-11
-08, shares: 22.0)

[**Bond Excess Returns Explanation with AI**](https://econpapers.repec.org/scripts/redir.pf?u=http%3
A%2F%2Flink.springer.com%2F10.1007%2Fs11573-023-01149-5;h=repec:spr:jbecon:v:93:y:2023:i:9:d:10.1007_s11573-023-01149-5)
:  The SHapley Additive exPlanations technique is used in a paper to  pinpoint key factors influencing bond excess retur
n predictions made by  machine learning models. (2023-11-08, shares: 21.0)

[**Signal Quality's Role in Stock Market Vol
atility Prediction**](https://econpapers.repec.org/scripts/redir.pf?u=https%3A%2F%2Fdoi.org%2F10.1002%2Ffor.3016;h=repec
:wly:jforec:v:42:y:2023:i:8:p:2307-2321): A study finds that high-quality political signals can predict increased stock 
market volatility. (2023-11-08, shares: 16.0)

[**Belief-Based Momentum Indicator and Volatility Predictability in China
's Equity Market**](https://econpapers.repec.org/scripts/redir.pf?u=http%3A%2F%2Fwww.sciencedirect.com%2Fscience%2Fartic
le%2Fpii%2FS1042443123001245;h=repec:eee:intfin:v:88:y:2023:i:c:s1042443123001245):  Research shows a belief-based momen
tum indicator can predict equity  market volatility in China, with the HAR-LCPR model being the most  effective. (2023-1
1-08, shares: 16.0)

[**Deep Learning Model for Newsvendor Problem with Textual Review Data**](https://econpapers.repec.
org/scripts/redir.pf?u=http%3A%2F%2Fwww.sciencedirect.com%2Fscience%2Farticle%2Fpii%2FS0925527323002487;h=repec:eee:proe
co:v:265:y:2023:i:c:s0925527323002487):  The article talks about a new inventory management framework that uses a  deep 
learning model. This model suggests order quantities based on  online reviews and demand data, reducing costs by 28.7% c
ompared to  other models. (2023-11-08, shares: 16.0)

[**Newsvendor Problem: High-Dimensional Data and Mixed-Frequency M
ethod**](https://econpapers.repec.org/scripts/redir.pf?u=http%3A%2F%2Fwww.sciencedirect.com%2Fscience%2Farticle%2Fpii%2F
S0925527323002748;h=repec:eee:proeco:v:266:y:2023:i:c:s0925527323002748):  The first article explores the application of
 machine learning to  improve demand prediction and restocking decisions in newsvendor  problems, utilizing complex and 
varied historical data. (2023-11-08,  shares: 27.0)

&#x200B;

# GitHub

## Finance

[**Time Series Analysis & Interpret
able ML**](https://github.com/MatthewK84/LinkedIn-Learning-Journey):  The article explores Time Series Analysis and Inte
rpretable Machine  Learning, focusing on Python packages such as Darts, PyCaret, Nixtla,  Sktime, MAPIE, and PiML. (2023
-08-19, shares: 13.0)

[**Fixed Income Library for Bond Pricing & Derivatives**](https://github.com/attack68/rateslib): 
 The piece reviews a fixed income library for pricing bonds, bond  futures, and derivatives, featuring tools for Curvese
t construction and  risk sensitivity calculations. (2023-03-31, shares: 14.0)

[**GPU-Accelerated Limit Order Book Simul
ator for Trading**](https://github.com/KangOxford/AlphaTrade):  The article introduces JAXLOB, a GPU-accelerated limit o
rder book  simulator aimed at improving large scale reinforcement learning for  trading. (2022-04-21, shares: 26.0)

[**
Ultimate Time Series Visualization Tool**](https://github.com/facontidavide/PlotJuggler): The article introduces a Time 
Series Visualization Tool designed to enhance user experience. (2016-03-01, shares: 3702.0)

[**Legible Deep Learning wi
th Named Tensors in JAX**](https://github.com/stanford-crfm/haliax): The piece explores the use of Named Tensors to impr
ove the readability of Deep Learning in JAX. (2023-06-26, shares: 73.0)

## Trending

[**Optimization**](https://github.
com/ebrahimpichka/awesome-optimization):  The article is a guide to resources for learning and implementing  mathematica
l optimization, including educational materials and software  tools. (2023-10-31, shares: 93.0)

[**Lock-Free**](https:/
/github.com/rigtorp/awesome-lockfree):  The article provides a collection of resources for understanding and  implementi
ng waitfree and lockfree programming techniques. (2016-03-31,  shares: 1565.0)

[**LaTeX Conversion**](https://github.co
m/lukas-blecher/LaTeX-OCR):  The article explores pix2tex, a tool that uses Vision Transformer  technology to convert eq
uation images into LaTeX code. (2020-12-11,  shares: 6218.0)

&#x200B;

# LinkedIn

## Trending

[**The Fund: A Dagger o
n Wall Street**](https://www.linkedin.com/feed/update/urn:li:activity:7127504060357689345):  The Fund' has received a po
sitive review from The New York Times, being  praised as a sharp critique of Wall Street and the use of money for  contr
ol and humiliation. (2023-11-07, shares: 2.0)

[**McKinney Joins Posit**](https://www.linkedin.com/feed/update/urn:li:ac
tivity:7127395325933182976):  Python data scientist Wes McKinney, known for the pandas package, has  joined data science
 tools company Posit. (2023-11-07, shares: 1.0)

[**New Causal Modeling Framework**](https://www.linkedin.com/feed/updat
e/urn:li:activity:7127356785438416897):  A paper by Lars Lorch, Andreas Krause and Bernhard Schölkopf introduces  a new 
way to discuss causality using Stochastic Differential Equations  (SDEs). (2023-11-07, shares: 2.0)

[**ADGM's DLT Frame
work Goes Live**](https://www.linkedin.com/feed/update/urn:li:activity:7127262744008900609):  The Abu Dhabi Global Marke
t's DLT Foundations Framework, aimed at  Blockchain Foundations and DAOs, is now live, advancing Abu Dhabi's  commitment
 to the virtual asset and blockchain sectors. (2023-11-07,  shares: 2.0)

[**Paper on trading with concave price impact*
*](https://www.linkedin.com/feed/update/urn:li:activity:7127468645177307137):  A preprint titled Trading with Concave Pr
ice Impact and Impact Decay  has been submitted to SSRN, addressing statistical arbitrage issues and  estimating trading
 data. (2023-11-07, shares: 2.0)

[**Korean tech index soars after short selling ban**](https://www.linkedin.com/feed/up
date/urn:li:activity:7127449160252825602):  South Korean tech index records a 12% single-day gain following a ban  on sh
ort selling by regulators until June 2024. (2023-11-07, shares:  1.0)

## Informative

[**Math Seminar: Mean Fields Game
s in Finance**](https://www.linkedin.com/feed/update/urn:li:activity:7127327252660256769):  A Math Seminar featuring Pro
f. Charles-Albert Lehalle will be held on  November 9th, 2023, focusing on Mean Fields Games for Financial Markets.  (20
23-11-07, shares: 2.0)

[**Advancements in Synthetic Data for AI**](https://www.linkedin.com/feed/update/urn:li:activity
:7127278959976669184):  The development of GenAI models is hindered by a lack of  human-generated data, but synthetic da
ta generation is being utilized by  companies like IBM and Google DeepMind. (2023-11-07, shares: 1.0)

[**European Diver
sification: Rise of Active ETFs**](https://www.linkedin.com/feed/update/urn:li:activity:7127356855814627328):  Active ET
Fs are becoming increasingly popular in Europe, outperforming  active mutual funds which are experiencing significant wi
thdrawals.  (2023-11-06, shares: 1.0)

&#x200B;

# Podcasts

## Quantitative

[**Investors and AI's Impact**](https://au
dioboom.com/posts/8394221):  A CIO call discusses the potential of artificial intelligence for  investors, identifying c
ompanies that could benefit or be at risk, and  how AI could disrupt the asset management industry. (2023-11-02, shares:
  4)

[**AI and Narratives in Investing**](https://pdcn.co/e/www.buzzsprout.com/2034153/13918632-ben-hunt-on-unraveling-
ai-and-narratives-the-new-frontiers-in-investing.mp3):  Ben Hunt explores the role of narrative archetypes in understand
ing  artificial intelligence, their influence on industries and money  management, and their effect on market trends and
 investment decisions.  (2023-11-06, shares: 4)

[**The Future of Finance: Quantum Solutions**](https://www.buzzsprout.c
om/1877496/13918851-quantum-solutions-envisioning-the-next-era-of-finance.mp3):  In the QuantSpeak podcast, Dr. Araceli 
Venegas-Gomez discusses the  potential impact of quantum computing on finance, its adoption in  various industries, and 
her shift from aeronautical engineering to quant  finance. (2023-11-06, shares: 4)

[**Becoming a Legend: Lessons from F
ischer Black, Peter Carr, and More**](https://www.buzzsprout.com/803279/13906664-legends-never-die-how-to-become-a-legen
d.mp3):  The article highlights the common traits of renowned figures like  Fischer Black, Peter Carr, Rick Rubin, Georg
e Box, Gilbert Strang, and  John Nash, focusing on their soft skills and unique contributions.  (2023-11-07, shares: 3)


&#x200B;

# Twitter

## Quantitative

[**RL Algorithmic Trading Strategies in Black Swan Regimes**](https://twitter.com
/carlcarrie/status/1720383646039749071):  The article reviews a study assessing the performance of different  reinforcem
ent learning trading strategies during unpredictable, extreme  market events. (2023-11-03, shares: 5)

[**Skewness Risk 
Premium Generates High FX Returns**](https://twitter.com/quantseeker/status/1722007548750975483):  The article highlight
s a new study suggesting that trading currencies  based on their skewness risk premium can yield high returns and Sharpe
  ratio. (2023-11-07, shares: 1)

[**Analyst Underreaction Decline and Momentum Strategy Deterioration**](https://twitte
r.com/quantseeker/status/1721271394489499893):  The article discusses a study indicating that the effectiveness of a  12
-month momentum strategy has decreased due to analysts' improved  reaction to news. (2023-11-05, shares: 1)

[**Return D
rivers of Listed and Unlisted Real Estate**](https://twitter.com/quantseeker/status/1721213958864970143):  The article e
xamines a study by Chin and Povala that investigates the  factors influencing the returns of listed and unlisted real es
tate,  noting a correlation with return horizon. (2023-11-05, shares: 1)

## Miscellaneous

[**Large Language Models for
 Time Series Forecasting**](https://twitter.com/carlcarrie/status/1720599381974438112):  The NeurIPS 2023 paper presents
 LLMTime, a large language model that  predicts time series data by converting numbers into text and managing  missing d
ata. (2023-11-04, shares: 1)

[**Commodity Strategies and Spreads**](https://twitter.com/quantseeker/status/172148638695
4412299): The episode offers useful knowledge on commodity strategies and spreads. (2023-11-06, shares: 0)

[**Microsoft
's DeepSpeedRLHF for Chat Inference**](https://twitter.com/carlcarrie/status/1721059368483828089):  Microsoft's DeepSpee
dRLHF simplifies chat-style inference, allowing the  training of OPT13B in 9 hours and OPT30B in 18 hours for less than 
$300  and $600 respectively. (2023-11-05, shares: 0)

[**Theseus: Open Source Library for DNLS Optimization**](https://t
witter.com/carlcarrie/status/1720798668263956795):  Theseus is Meta's open-source library for DNLS optimization, develop
ed  on PyTorch for structured machine learning. (2023-11-04, shares: 0)

[**LLMTS: Language Models for Time Series**](ht
tps://twitter.com/carlcarrie/status/1720600217358090459):  LLM4TS is a large language model for time series that uses fi
ne-tuning,  layer normalization tuning, and LoRA. (2023-11-04, shares: 0)

# Paper with Code

## Trending

[**DeepSpeed 
Inference: Efficient Transformer Model at Unprecedented Scale**](https://github.com/microsoft/deepspeed-mii): DeepSpeed 
Inference improves latency and throughput performance in different situations. (2023-11-07, shares: 1071.0)

[**AkariAsa
i SelfRAG: Learning to Retrieve, Generate, and Critique through Self-Reflection**](https://github.com/AkariAsai/self-rag
):  The framework develops a unique language model that adaptively  retrieves and reflects on passages using special 're
flection' tokens.  (2023-11-04, shares: 439.0)

[**Diffusion Models for Reinforcement Learning**](https://github.com/ape
xrl/diff4rlsurvey):  The article emphasizes the superiority of diffusion models over  previous generative models in term
s of sample quality and training  stability. (2023-11-04, shares: 35.0)

[**GPTFathom: LLM Benchmarking for GPT4+**](htt
ps://github.com/gpt-fathom/gpt-fathom):  The rapid advancement of LLMs necessitates an immediate need for a  comprehensi
ve evaluation system to identify their pros and cons.  (2023-11-05, shares: 146.0)

[**Comprehensive Survey on LLM Evalu
ation**](https://github.com/tjunlp-lab/awesome-llms-evaluation-papers):  The comprehensive review is designed to stimula
te more research into  assessing LLMs to ensure their ethical development. (2023-11-04, shares:  192.0)
```
---

     
 
all -  [ Effect of GPA, and Chances at Top CS PhD Programs? ](https://www.reddit.com/r/gradadmissions/comments/17pq2ta/effect_of_gpa_and_chances_at_top_cs_phd_programs/) , 2023-11-11-0909
```
Hi folks! I'm an undergraduate senior studying CS and Statistics at a T10 undergrad school (not for CS PhD, though); I'm
 also concurrently getting my M.S. in CS here as well. I have research experience in industry (at a top AI Research lab 
for 2 summers and ongoing part-time during the year for follow-up work / paper writing) and in academia (undergraduate h
onors thesis, and several collaborations with researchers both at my university and elsewhere). I have a few publication
s -- 2 at workshops (NeurIPS) and 4 pre-prints for papers under review at tier 1 venues (all first-author or co-first au
thor). I will add that my research experience appears to be a little unorthodox at the undergrad level, as most of my pr
ojects in academia have been self-initiated and self-devised, turning to mentor(s) (profs and sometimes PhD students) fo
r feedback, rather than working in a lab consistently with PhD students, postdocs, and a professor.

I also have quite a
 bit of teaching experience (TA'd 6 courses, all upper-level, majority being graduate-level) and some professional servi
ce (served as a reviewer for a few tier-1 conference workshops; some departmental service and other leadership stuff too
). LoRs most likely coming from an industry mentor, a research (thesis) advisor, and another professor I was Head TA for
 (am curious if there are any opinions on whether I should be going in a different direction for the 3rd recommender).


The reason I'm posting here is: I'm nervous that my GPA is a bit lower than the top programs' averages, and I'm wonderin
g if that'll be strongly held against me / a dealbreaker. Part of the reason for this is mental health struggles while b
eing overwhelmed with commitments. I'd say my course rigor is generally pretty strong (given that a lot of the technical
 courses are graduate / doctoral-level) despite that, but I'm worried that the GPA may be an immediate turnoff for those
 reviewing my application. As you probably can expect, I'm interested in Stanford, MIT, Princeton, CMU, etc.

Thanks in 
advance for your feedback and insights (and for taking the time to read all of this :))!!
```
---

     
 
all -  [ Code for a paper ](https://www.reddit.com/r/reinforcementlearning/comments/17o6brs/code_for_a_paper/) , 2023-11-11-0909
```
Is there a code available for the paper “Risk-Aware Transfer in Reinforcement Learning using Successor Features” publish
ed in NeurIPS 2021 by Gimelfarb et Al.?
```
---

     
 
all -  [ [R] Highlights for every NeurIPS 2023 paper ](https://www.reddit.com/r/MachineLearning/comments/17nm4eb/r_highlights_for_every_neurips_2023_paper/) , 2023-11-11-0909
```
Here is the list of all NeurIPS 2023 (Neural Information Processing Systems) papers and a short highlight for each of th
em. Among all \~3,500 papers, authors of around 1,000 papers also made their code or data available. The 'related code' 
link under paper title will take you directly to the code base.

[https://www.paperdigest.org/2023/10/nips-2023-highligh
ts/](https://www.paperdigest.org/2023/10/nips-2023-highlights/)

In addition, here is the link of 'search within NeurIPS
 2023' that can be used to find papers within NeurIPS-2023 related to a specific topic, e.g. 'diffusion model':

[https:
//www.paperdigest.org/search/?topic=nips&year=2023&q=diffusion\_model](https://www.paperdigest.org/search/?topic=nips&ye
ar=2023&q=diffusion_model)

NeurIPS 2023 will take place at New Orleans on Dec 10, 2023.
```
---

     
 
all -  [ Papers to reproduce for ML Reproducibility Challenge 2023 ](https://www.reddit.com/r/learnmachinelearning/comments/17lr0g0/papers_to_reproduce_for_ml_reproducibility/) , 2023-11-11-0909
```
I'm planning to participate in the ML Reproducibility Challenge 2023 ([**https://reproml.org/blog/announcing\_mlrc2023/*
*](https://reproml.org/blog/announcing_mlrc2023/)) and I'm looking for suggestions on some good deep learning papers whe
re I can try to reproduce the results.  


Per the organizer's suggestion, I should focus on papers published in 2023 fr
om the top ML venues like NeurIPS, ICML, ICLR, ACL, EMNLP, ICCV, CVPR, TMLR, JMLR, TACL.

Let me know if you have come a
cross any promising deep learning papers published this year that would be good for reproducibility! I'm hoping to selec
t one to focus on for this challenge.

&#x200B;
```
---

     
 
all -  [ My first ever paper got accepted to neurips workshop! ](https://www.reddit.com/r/womenintech/comments/17jmdaa/my_first_ever_paper_got_accepted_to_neurips/) , 2023-11-11-0909
```
I just wanted to share the news! I don’t know what this means but I’m excited to share.
```
---

     
 
all -  [ AI Weekly Rundown (October 21 to October 28) ](https://www.reddit.com/r/ArtificialInteligence/comments/17j1egi/ai_weekly_rundown_october_21_to_october_28/) , 2023-11-11-0909
```
Major AI announcements from Meta, NVIDIA, OpenAI, Google and more.   


* **Meta introduces Habitat 3.0, a leap toward s
ocially intelligent robots**  
\- Meta claims it is the highest-quality simulator that supports robots and humanoid avat
ars and allows for human-robot collaboration in home-like environments. AI agents trained with Habitat 3.0 learn to find
 and collaborate with human partners at everyday tasks like cleaning up a house, thus improving their human partner’s ef
ficiency.  
\- Meta also announced Habitat Synthetic Scenes Dataset and HomeRobot– three major advancements in developin
g socially embodied AI agents that can cooperate with and assist humans in daily tasks.
* **NVIDIA’s research breakthrou
gh, Eureka, puts a new spin on robot learning**  
\- A new AI agent that can teach robots complex skills has trained a r
obotic hand to perform rapid pen-spinning tricks– for the first time, as well as a human can. The robots have learned to
 accomplish nearly 30 tasks expertly thanks to Eureka, which autonomously writes reward algorithms to train bots.
* **Op
enAI reveals DALL-E 3's secret sauce of accurate, prompt generation**  
\- OpenAI has published a paper on DALL-E 3, sho
wing how the system follows prompts more accurately than other systems using better image labels.
* **Qualcomm’s new PC 
chip with AI features the first to challenge Apple**  
\- Its new Snapdragon Elite X chip will be available in laptops s
tarting next year and has been redesigned to better handle AI tasks like summarizing emails, writing text, and generatin
g images.   
\- Qualcomm claims it is faster than Apple's M2 Max chip at some tasks and more energy efficient than Apple
 and Intel PC chips.
* **Microsoft is outdoing its biggest rival, Google, in the AI game**  
\- From the two tech giants
’ September-quarter results, growth at Microsoft’s Azure cloud unit (and the company generally) accelerated due to highe
r-than-expected consumption of AI-related services.   
\- Google Cloud earnings slowed by nearly 6 percentage points in 
the same quarter.
* **Samsung’s Galaxy S24 is your upcoming pocket AI machine**  
\- Going all in with AI on its next fl
agship, Samsung wants to make the Galaxy S24, Galaxy S24+, and Galaxy S24 Ultra the smartest AI phones ever. The series 
will have features lifted straight from ChatGPT and Google Bard, and Samsung has designed independently. Many will be av
ailable online and offline, and some Samsung features will be improved.
* **Berlin-based AI company Jina AI launched Ope
nAI rival jina-embeddings-v2, the world's first open-source 8K text embedding model**  
\- Jina-embeddings-v2 offers ext
ended context potential, allowing for applications such as legal document analysis, medical research, literary analysis,
 financial forecasting, and conversational AI.   
\- Benchmarking shows that it outperforms other leading base embedding
 models. The model is available in two sizes: a base model for heavy-duty tasks and a small model for lightweight applic
ations. 
* **LLM hallucination problem will be over with “Woodpecker”**   
\- Researchers from the University of Science
 and Technology of China and Tencent YouTu Lab have developed a 'Woodpecker' framework to correct hallucinations in mult
imodal large language models (MLLMs).   
\- Woodpecker uses a training-free method to identify and correct hallucination
s in the generated text. The framework goes through 5 stages, including key concept extraction, question formulation, vi
sual knowledge validation, visual claim generation, and hallucination correction. 
* **NVIDIA Research has announced a r
ange of AI advancements**  
\- That will be presented at the NeurIPS conference. The projects include new techniques for
 transforming text-to-images, photos-to-3D avatars, and specialized robots into multi-talented machines. The research fo
cuses on gen AI models, reinforcement learning, robotics, and applications in the natural sciences.   
\- Highlights inc
lude improving text-to-image diffusion models, AI avatar advancements, reinforcement learning and robotics breakthroughs
, AI-accelerated physics, climate, and healthcare research. 
* **OpenAI is forming a “Preparedness” team to support safe
ty of highly capable AI**  
\- The team will tightly connect capability assessment, evaluations, and internal red teamin
g for frontier models, from the models we develop in the near future to those with AGI-level capabilities.   
\- The tea
m will help track, evaluate, forecast, and protect against catastrophic risks spanning multiple categories, including nu
clear threats.
* **Google expands its bug bounty program for attacks specific to GenAI**  
\- It is also expanding its o
pen-source security work and building upon our prior collaboration with the Open Source Security Foundation. In addition
, Google is to support a new effort by the non-profit MLCommons Association to develop standard AI safety benchmarks.
* 
**Boston Dynamics turns its robot dog into a talking tour guide using ChatGPT**  
\- Spot could run, jump, and even danc
e, but now it can talk. With ChatGPT, it can answer questions and generate responses about the company’s facilities whil
e giving a tour.  

* And there was more… 
   * **IBM is developing a brain-inspired chip for faster, more energy-effici
ent AI**  
\- New research out of IBM Research’s lab, nearly two decades in the making, has the potential to drastically
 shift how we can efficiently scale up powerful AI hardware systems. The new type of digital AI chip for neural inferenc
e is called NorthPole.
   * **Oracle loops in NVIDIA AI for end-to-end model development**  
\- Oracle is bringing the N
VIDIA AI stack to its marketplace to simplify AI development and deployment for its customers. It gives Oracle customers
 access to the most sought-after, top-of-the-line GPUs for training foundation models and building generative applicatio
ns.
   * **YouTube develops an AI tool to help creators sound like famous musicians**  
\- In beta, the tool will let a 
select pool of artists give permission to a select group of creators to use their voices in videos on the platform. Nego
tiations with major labels are ongoing and slowing down the project's beta release.
   * **There’s now an AI cancer surv
ivor calculator**  
\- Researchers have created an AI-based tool to predict a cancer patient's odds of long-term surviva
l after a fresh diagnosis. It was found to predict cancer survival length for three types of cancers accurately.
   * **
Instagram’s latest AI feature test is a way to make stickers from photos**  
\- Meta’s newest sticker feature is much li
ke the one built into the iPhone Messages app in iOS 17– Instagram detects and cuts out an object from a photo so you ca
n place it over another.
   * **Google Photos will soon give you more say in its AI-created video highlights**  
\- With
 the latest Google Photos update, you can prompt AI-generated videos by searching for specific tags like places, people,
 or activities. Once generated, you can trim clips, rearrange them, or swap out music for something better.
   * **Lenov
o and NVIDIA announce hybrid AI solutions to help enterprises quickly adopt GenAI**  
\- The new end-to-end solutions in
clude accelerated systems, AI software, and expert services to build and deploy domain-specific AI models easily.
   * *
*Amazon's AI-powered van inspections give it a powerful new data feed**  
\- Amazon delivery drivers at sites worldwide 
will be asked to drive through camera-studded archways at the end of shifts. The data gathered will be used by algorithm
s to identify whether the vehicle is damaged or needs maintenance, picking up every scratch, dent, nail in a tire, or cr
ack in the windshield.
   * **IBM acquires Manta Software Inc. to complement data and AI governance capabilities**  
\- 
Manta’s data lineage capabilities help increase transparency within Watsonx so businesses can determine whether the righ
t data was used for their AI models and systems, where it originated, how it has evolved, and any discrepancies in data 
flows.
   * **This new data poisoning tool lets artists fight back against GenAI**  
\- The tool, called Nightshade, let
s artists add invisible changes to the pixels in their art before they upload it online so that if it’s scraped into an 
AI training set, it can cause the resulting model to break in chaotic and unpredictable ways.   
\- This “poisoning” of 
training data could damage future iterations of image-generating AI models, such as DALL-E, Midjourney, and Stable Diffu
sion.
   * **Google announces new AI tools to help users fact-check images and more**  
\- Also prevent the spread of fa
lse information. The tools include viewing an image's history, metadata, and the context in which it was used on differe
nt sites. Users can also see when the image was first seen by Google Search to understand its recency.   
\- Additionall
y, the tools allow users to understand how people described the image on other sites to debunk false claims. Google mark
s all images created by its AI, and the new image tools are accessible through the three-dot menu on Google Images resul
ts.
   * **Grammarly announces a new feature, 'Personalized voice detection & application'**   
\- That uses generative 
AI to detect a person's unique writing style and create a 'voice profile' that can rewrite any text in that style.   
\-
 The feature will be available to Grammarly's business tier subscribers by the end of the year. It aims to recognize and
 reimburse writers for AI-generated works that mimic their voices.   
\- Users can customize their profiles to discard e
lements that don't accurately reflect their writing style. 
   * **AI features boost Motorola's new foldable phone**   

\- They've developed an AI model that runs locally on the device, allowing users to 'bring their personal style to their
 phone.' Users can upload or take photos to get an AI-generated theme to match their style.  
\- Embedded AI features in
 many areas, like camera, battery, display, and performance. It will serve as a personal assistant and a tool to enhance
 everyday tasks, improve performance, and create meaningful user experiences.
   * **Forbes now has its own GenAI search
 engine**  
\- The tool, Adelaide, is purpose-built for news search and offers AI-driven personalized recommendations an
d insights from Forbes’ trusted journalism. It is in beta and is powered by Google Cloud.
   * **Cisco rolls out new AI 
tools at the Webex One customer conference**  
\- These tools include a real-time media model (RMM) that uses generative
 AI for audio and video, an AI-powered audio codec up to 16 times more efficient in bandwidth usage, and the Webex AI As
sistant, which pulls together all the AI tooling for users.   
\- The AI Assistant can detect when a user steps away fro
m a meeting and provide summaries or replays of missed content.
   * **Amazon reveals AI image generation to help advert
isers create more engaging ads**  
\- The use of data science, analytics, and AI has greatly improved the efficiency of 
digital advertising, but many advertisers still struggle with building successful campaigns.   
\- By providing tools th
at reduce friction and effort for advertisers, Amazon aims to deliver a better advertising experience for customers.
   
* **Google Maps is becoming more like Search, thanks to AI**  
\- Google wants Maps to be more like Search, where people
 can get directions or find places but also enter queries like “things to do in Tokyo” and get actually useful hits and 
discover new experiences, guided by its all-powerful algorithm.
   * **Shutterstock will now let you edit its library of
 images using AI**  
\- It revealed a set of new AI-powered tools, like Magic Brush, which lets you tweak an image by br
ushing over an area and describing what you want to add/replace/erase. Others include a smart resizing feature and a bac
kground removal tool.
   * **UK to set up world's first AI safety institute, Sunak says**  
\- The institute will carefu
lly examine, evaluate, and test new types of AI so that we understand what each new model is capable of, exploring all t
he risks from social harms like bias and misinformation through to the most extreme risks of all.
   * **Intel will sell
 specialized AI software and services**  
\- Intel is working with multiple consulting firms to build ChatGPT-like apps 
for customers who don’t have the expertise to do it on their own.

More detailed breakdown of these news and innovations
 is in the [weekly edition](https://theaiedge.substack.com/p/ai-weekly-rundown-october-21-to-october27).
```
---

     
 
all -  [ AI Revolution October 2023: Week 4 Updates - “Woodpecker” Solving LLM Hallucination & Latest from Ji ](https://www.reddit.com/r/u_enoumen/comments/17i5evp/ai_revolution_october_2023_week_4_updates/) , 2023-11-11-0909
```
Dive into the latest AI advancements and breakthroughs in this week's AI Revolution podcast! We dissect the game-changin
g 'Woodpecker' technology set to tackle the Large Language Models (LLM) hallucination problem, bringing more accuracy an
d reliability to AI-generated content. Plus, get insider updates from leading tech giants and emerging players in the AI
 field. October 2023, Week 4: Here’s what we’re covering:- “Woodpecker”: The promising solution to LLM hallucination iss
ues- Jina AI: How OpenAI’s newest rival is shaping the AI landscape- Meta’s AI ventures: What’s next from the social med
ia giant?- NVIDIA: Latest innovations and collaborations- Google, Qualcomm, Grammarly, Motorola, Cisco, and Amazon: AI u
pdates and developments- And more!

**Video**: [https://youtu.be/Q6rTpvzUpng](https://youtu.be/Q6rTpvzUpng)

**Forbes la
unches its own generative AI search platform built with Google Cloud.**

The tool, Adelaide, is purpose-built for news s
earch and offers AI-driven personalized recommendations and insights from Forbes’ trusted journalism. It is in beta and 
select visitors can access it through the website. *(*[*Link*](https://www.forbes.com/sites/forbes-spotlights/2023/10/26
/forbes-launches-new-generative-ai-search-tool-adelaide-powered-by-google-cloud/)*)*

**Google Maps is becoming more lik
e Search– thanks to AI.**

Google wants Maps to be more like Search, where people can get directions or find places but 
also enter queries like “things to do in Tokyo” and get actually useful hits and discover new experiences, guided by its
 all-powerful algorithm. *(*[*Link*](https://www.theverge.com/2023/10/26/23932315/google-maps-ai-immersive-view-ev-charg
ing-search)*)*

**Shutterstock will now let you edit its library of images using AI.**

It revealed a set of new AI-powe
red tools, like Magic Brush, which lets you tweak an image by brushing over an area and describing what you want to add/
replace/erase. Others include smart resizing feature and background removal tool. *(*[*Link*](https://www.theverge.com/2
023/10/26/23933120/shutterstock-transform-real-photos-ai)*)*

**UK to set up world's first AI safety institute, says PM 
Rishi Sunak.**

The institute will carefully examine, evaluate and test new types of AI so that we understand what each 
new model is capable of, exploring all the risks from social harms like bias and misinformation through to the most extr
eme risks of all. *(*[*Link*](https://www.reuters.com/world/uk/uk-set-up-worlds-first-ai-safety-institute-sunak-says-202
3-10-26)*)*

**Intel is trying something different– selling specialized AI software and services.**

Intel is working wi
th multiple consulting firms to build ChatGPT-like apps for customers that don’t have the expertise to do it on their ow
n. *(*[*Link*](https://www.theinformation.com/articles/ai-laggard-intel-expands-effort-to-help-companies-build-chatgpt-l
ike-apps)*)*

**Google expands its bug bounty program for attacks specific to GenAI**\- It is also expanding its open so
urce security work and building upon our prior collaboration with the Open Source Security Foundation. In addition, Goog
le is to to support a new effort by the non-profit MLCommons Association to develop standard AI safety benchmarks.

**Bo
ston Dynamics turns its robot dog into a talking tour guide using ChatGPT**\- Spot could run, jump, and even dance, but 
now it can talk. With ChatGPT, it can answer questions and generate responses about the company’s facilities while givin
g a tour.

**UK to set up world's first AI safety institute, Sunak says**\- The institute will carefully examine, evalua
te and test new types of AI so that we understand what each new model is capable of, exploring all the risks from social
 harms like bias and misinformation through to the most extreme risks of all.

**Intel will sell specialized AI software
 and services**\- Intel is working with multiple consulting firms to build ChatGPT-like apps for customers that don’t ha
ve the expertise to do it on their own.

**Berlin-based AI company Jina AI launched OpenAI rival jina-embeddings-v2, the
 world's first open-source 8K text embedding model.**\- This model supports an impressive 8K context length, putting it 
on par with OpenAI's proprietary model. Jina-embeddings-v2 offers extended context potential, allowing for applications 
such as legal document analysis, medical research, literary analysis, financial forecasting, and conversational AI.- Ben
chmarking shows that it outperforms other leading base embedding models. The model is available in two sizes, a base mod
el for heavy-duty tasks and a small model for lightweight applications.

**LLM hallucination problem will be over with “
Woodpecker”**\- Researchers from the University of Science and Technology of China and Tencent YouTu Lab have developed 
a framework called 'Woodpecker' to correct hallucinations in multimodal large language models (MLLMs).- Woodpecker uses 
a training-free method to identify and correct hallucinations in generated text. The framework goes through 5 stages, in
cluding key concept extraction, question formulation, visual knowledge validation, visual claim generation, and hallucin
ation correction.- The researchers have released the source code and an interactive demo of Woodpecker for further explo
ration and application.

**NVIDIA Research has announced a range of AI advancements**\- That will be presented at the Ne
urIPS conference. The projects include new techniques for transforming text to images, photos to 3D avatars, and special
ized robots into multi-talented machines. The research focuses on gen AI models, reinforcement learning, robotics, and a
pplications in the natural sciences.- Highlights include improving text-to-image diffusion models, advancements in AI av
atars, breakthroughs in reinforcement learning and robotics, and AI-accelerated physics, climate, and healthcare researc
h.

**Google announces new AI tools to help users fact-check images and more**\- Also prevent the spread of false inform
ation. The tools include viewing an image's history, metadata, and the context in which it was used on different sites. 
Users can also see when the image was first seen by Google Search to understand its recency.- Additionally, the tools al
low users to understand how people described the image on other sites to debunk false claims. Google marks all images cr
eated by its AI, and the new image tools are accessible through the three-dot menu on Google Images results.

**Grammarl
y’s announces new feature 'Personalized voice detection & application'**\- That uses generative AI to detect a person's 
unique writing style and create a 'voice profile' that can rewrite any text in that style.- The feature, which will be a
vailable to subscribers of Grammarly's business tier by the end of the year, aims to recognize and remunerate writers fo
r AI-generated works that mimic their voices.- Users can customize their profiles to discard elements that don't accurat
ely reflect their writing style.

**Motorola's new foldable phone is boosted by AI features**\- They've developed an AI 
model that runs locally on the device, allowing users to 'bring their personal style to their phone.' Users can upload o
r take a photo to get an AI-generated theme to match their style.- They’ve embedded AI features in many areas of our dev
ices, like camera, battery, display and device performance. It will serve as a personal assistant and a tool to enhance 
everyday tasks, improve performance, and create more meaningful experiences for the users.

**Cisco rolls out new AI too
ls at the Webex One customer conference**\- These tools include a real-time media model (RMM) that uses generative AI fo
r audio and video, an AI-powered audio codec that is up to 16 times more efficient in bandwidth usage, and the Webex AI 
Assistant, which pulls together all the AI tooling for users.- The AI Assistant can detect when a user steps away from a
 meeting and provide summaries or replays of missed content.

**Amazon reveals AI image generation to help advertisers c
reate more engaging ads**\- The use of data science, analytics, and AI has greatly improved the efficiency of digital ad
vertising, but many advertisers still struggle with building successful campaigns.- By providing tools that reduce frict
ion and effort for advertisers, Amazon aims to deliver a better advertising experience for customers.

**Qualcomm’s new 
PC chip with AI features the first to challenge Apple**\- Its new Snapdragon Elite X chip will be available in laptops s
tarting next year and has been redesigned to better handle AI tasks like summarizing emails, writing text, and generatin
g images. Qualcomm claims it is faster than Apple's M2 Max chip at some tasks and more energy efficient than both Apple 
and Intel PC chips.

**Microsoft is outdoing its biggest rival, Google, in the AI game**\- From the two tech giants’ Sep
tember-quarter results, growth at Microsoft’s Azure cloud unit (and the company generally) accelerated in the quarter du
e to higher-than-expected consumption of AI-related services. In the same quarter, Google Cloud earnings slowed by nearl
y 6 percentage points.

**Samsung’s Galaxy S24 is your upcoming pocket AI machine**\- Going all in with AI on its next f
lagship, Samsung wants to make the Galaxy S24, Galaxy S24+, and Galaxy S24 Ultra the smartest AI phones ever. The series
 will have features lifted straight from ChatGPT and Google Bard, and Samsung has designed on its own. Many of them will
 be available online and offline, and some Samsung features will be improved.

**Google Photos will soon give you more s
ay in its AI-created video highlights**\- With the latest Google Photos update, you can prompt AI-generated videos by se
arching for specific tags like places, people, or activities. Once generated, you can trim clips, rearrange them, or swa
p out music for something better.

**Lenovo and NVIDIA announce hybrid AI solutions to help enterprises quickly adopt Ge
nAI**\- The new end-to-end solutions include accelerated systems, AI software, and expert services to build and deploy d
omain-specific AI models with ease.

**Amazon's AI-powered van inspections give it a powerful new data feed**\- Amazon d
elivery drivers at sites around the world will be asked to drive through camera-studded archways at the end of shifts. T
he data gathered will be used by algorithms to identify whether the vehicle is damaged or needs maintenance, picking up 
every scratch, dent, nail in a tire, or crack in the windshield.

**IBM acquires Manta Software Inc. to complement data 
and AI governance capabilities**\- Manta’s data lineage capabilities help increase transparency within watsonx so busine
sses can determine whether the right data was used for their AI models and systems, where it originated, how it has evol
ved and any discrepancies in data flows.

**This new data poisoning tool lets artists fight back against GenAI**\- The t
ool, called Nightshade, lets artists add invisible changes to the pixels in their art before they upload it online so th
at if it’s scraped into an AI training set, it can cause the resulting model to break in chaotic and unpredictable ways.
 This “poisoning” of training data could damage future iterations of image-generating AI models, such as DALL-E, Midjour
ney, and Stable Diffusion.

**Video**: [https://youtu.be/Q6rTpvzUpng](https://youtu.be/Q6rTpvzUpng)

Full transcript: [h
ttps://enoumen.com/2023/10/02/ai-revolution-in-october-2023-the-latest-innovations-reshaping-the-tech-landscape/](https:
//enoumen.com/2023/10/02/ai-revolution-in-october-2023-the-latest-innovations-reshaping-the-tech-landscape/)

Are you ea
ger to expand your understanding of artificial intelligence? Look no further than the essential book '[**AI Unraveled: D
emystifying Frequently Asked Questions on Artificial Intelligence,**](https://amzn.to/3BwRqkF)' available at [**Apple**]
(http://books.apple.com/us/book/id6445730691), [**Google**](https://play.google.com/store/books/details?id=oySuEAAAQBAJ)
, or [**Amazon**](https://amzn.to/3ZrpkCu) today: [https://amzn.to/3ZrpkCu](https://amzn.to/3ZrpkCu)
```
---

     
 
all -  [ Two-minute Daily AI Update (Date: 10/26/2023): News from Jina AI (OpenAI’s new rival), NVIDIA, Woodp ](https://www.reddit.com/r/ArtificialInteligence/comments/17gwd5t/twominute_daily_ai_update_date_10262023_news_from/) , 2023-11-11-0909
```
Continuing with the exercise of sharing an easily digestible and smaller version of the main updates of the day in the w
orld of AI.  


* **Berlin-based AI company Jina AI launched OpenAI rival jina-embeddings-v2, the world's first open-sou
rce 8K text embedding model.**  
\- This model supports an impressive 8K context length, putting it on par with OpenAI's
 proprietary model. Jina-embeddings-v2 offers extended context potential, allowing for applications such as legal docume
nt analysis, medical research, literary analysis, financial forecasting, and conversational AI.   
\- Benchmarking shows
 that it outperforms other leading base embedding models. The model is available in two sizes, a base model for heavy-du
ty tasks and a small model for lightweight applications. 
* **LLM hallucination problem will be over with “Woodpecker”**
   
\- Researchers from the University of Science and Technology of China and Tencent YouTu Lab have developed a framewo
rk called 'Woodpecker' to correct hallucinations in multimodal large language models (MLLMs).   
\- Woodpecker uses a tr
aining-free method to identify and correct hallucinations in generated text. The framework goes through 5 stages, includ
ing key concept extraction, question formulation, visual knowledge validation, visual claim generation, and hallucinatio
n correction.   
\- The researchers have released the source code and an interactive demo of Woodpecker for further expl
oration and application. 
* **NVIDIA Research has announced a range of AI advancements**  
\- That will be presented at 
the NeurIPS conference. The projects include new techniques for transforming text to images, photos to 3D avatars, and s
pecialized robots into multi-talented machines. The research focuses on gen AI models, reinforcement learning, robotics,
 and applications in the natural sciences.   
\- Highlights include improving text-to-image diffusion models, advancemen
ts in AI avatars, breakthroughs in reinforcement learning and robotics, and AI-accelerated physics, climate, and healthc
are research. 
* **Google announces new AI tools to help users fact-check images and more**  
\- Also prevent the spread
 of false information. The tools include viewing an image's history, metadata, and the context in which it was used on d
ifferent sites. Users can also see when the image was first seen by Google Search to understand its recency.   
\- Addit
ionally, the tools allow users to understand how people described the image on other sites to debunk false claims. Googl
e marks all images created by its AI, and the new image tools are accessible through the three-dot menu on Google Images
 results.
* **Grammarly’s announces new feature 'Personalized voice detection & application'**   
\- That uses generativ
e AI to detect a person's unique writing style and create a 'voice profile' that can rewrite any text in that style.   

\- The feature, which will be available to subscribers of Grammarly's business tier by the end of the year, aims to reco
gnize and remunerate writers for AI-generated works that mimic their voices.   
\- Users can customize their profiles to
 discard elements that don't accurately reflect their writing style. 
* **Motorola's new foldable phone is boosted by AI
 features**   
\- They've developed an AI model that runs locally on the device, allowing users to 'bring their personal
 style to their phone.' Users can upload or take a photo to get an AI-generated theme to match their style.  
\- They’ve
 embedded AI features in many areas of our devices, like camera, battery, display and device performance. It will serve 
as a personal assistant and a tool to enhance everyday tasks, improve performance, and create more meaningful experience
s for the users.
* **Cisco rolls out new AI tools at the Webex One customer conference**  
\- These tools include a real
-time media model (RMM) that uses generative AI for audio and video, an AI-powered audio codec that is up to 16 times mo
re efficient in bandwidth usage, and the Webex AI Assistant, which pulls together all the AI tooling for users.   
\- Th
e AI Assistant can detect when a user steps away from a meeting and provide summaries or replays of missed content.
* **
Amazon reveals AI image generation to help advertisers create more engaging ads**  
\- The use of data science, analytic
s, and AI has greatly improved the efficiency of digital advertising, but many advertisers still struggle with building 
successful campaigns.   
\- By providing tools that reduce friction and effort for advertisers, Amazon aims to deliver a
 better advertising experience for customers.

More detailed breakdown of these news and innovations in the [daily newsl
etter](https://theaiedge.substack.com/p/openai-new-rival-jina-ai-woodpecker-nvidia).
```
---

     
 
all -  [ At what programs am I competitive? - PhD in CS (AI/ML) ](https://www.reddit.com/r/gradadmissions/comments/17gskbg/at_what_programs_am_i_competitive_phd_in_cs_aiml/) , 2023-11-11-0909
```
 I plan to apply to 10-12 CS PhD programs, with a research focus in ML/NLP. 

While I understand that many successful ap
plicants in top programs have published NeurIPS/CVPR/ACL/EMNLP papers and are from prestigious labs/schools, what rankin
gs of programs should I expect to be a competitive applicant for? #10-20? #20-40? #40-60? etc.

&#x200B;

\- 4.0 GPA fro
m a small private school in California, graduated #1 in class

\- 2 years as an RA in an on-campus NLP lab, while also d
oing independent research

\- 3 first author research papers (1 in submission at an A-tier conference, 2 on arXiv)

\- 1
 second author paper (in submission at an A-tier conference)

\- 3 LoRs from profs who know me well. I am confident that
 they will be quite strong, discussing my research and leadership abilities. But the profs are relatively unknown in aca
demia

\- Strong (I think) SoP, taking inspiration from many previously successful applicants. My research experiences a
nd interests are very well-defined and catered to specific schools/profs

\- Currently an SWE at a well-known company (n
ot FAANG). I also do NLP consulting

\- 3 SWE internships

\- 330 GRE (169Q, 161V, 5.0AW)

\- A couple of solid ML proje
cts in school

&#x200B;

What kind of schools should I target? Where would be a reach? Any safeties?

(Specific schools 
listed below are arbitrary examples)

\#10-20: UCLA/USC/UNC/Duke

\#20-40: NYU/UCI/Rice/Ohio St

\#40-60: NCSU/Vanderbil
t/UT Dallas/UCF
```
---

     
 
all -  [ [D] Are people in ML Phds still happy? ](https://www.reddit.com/r/MachineLearning/comments/17fahm6/d_are_people_in_ml_phds_still_happy/) , 2023-11-11-0909
```
As an outsider who has many friends in ML Phds, this is my perspective of their lives:

1. long hours, working nights, w
eekends
2. no work-life balance, constant fear of being scooped and time pressure from deadlines
3. frustrating broken r
eview systems
4. many incremental, advertisement papers that produce very little actual contribution (which is justified
 by 2.)
5. 'engineering' and not 'science'
6. all this pressure amounts to severe imposter syndrome

Are people in the f
ield still happy? Where do people get their satisfaction? To me it looks like almost like a religion or a cult. The sele
ct few who say, get neurips outstanding paper are promoted to stardom - almost a celebrity status while everyone else su
ffers a punishing work cycle. Are the phd students all banking on AGI? What else motivates them?

Edit: the discussion i
s about whether 1-6 are worse in ML than other fields (or even the median experience). The reference for 'other field' i
s highly heterogenous. Experience obviously varies by lab, and then even by individuals within labs. 'It happens in othe
r fields too' is a trivial statement - of course some version of 1-6 affects somebody in another field.

Edit 2: small n
 but summarizing the comments - experience seems to differ based on geographic region, one's expectations for the phd, a
bility to exert work-life balance, and to some extent ignore the trends others are all following. Some people have reson
ated with problems 1-6, yet others have presented their own, anecdotal solutions. I recommend reading comments from thos
e who claim to have solutions.
```
---

     
 
all -  [ [R] Biologically plausible vision models for classification and grasping tasks ](https://www.reddit.com/r/MachineLearning/comments/17ea25h/r_biologically_plausible_vision_models_for/) , 2023-11-11-0909
```
Hey everyone! I am looking for papers that propose or explore biologically plausible vision models, primarily tasks like
 classification and grasping (predicting grasping bounding boxes) tasks. By biologically plausible, I mean papers that p
ropose models inspired by the human brain in some way or the other. I know convolution is loosely inspired by human cogn
ition, but everything I can find seems to suggest the opposite for ViT like models.

I have come across certain papers l
ike these:
- https://arxiv.org/abs/1901.00945
- https://proceedings.neurips.cc/paper/2020/hash/98b17f068d5d9b7668e19fb8a
e470841-Abstract.html

But I am still looking for more. Any suggestions?
```
---

     
 
all -  [ Inpaintint Not working ](https://www.reddit.com/gallery/17d832h) , 2023-11-11-0909
```
So I'm a begginer, I've been using SD for sometime. My inpaint Stopped working 1 or 2 months ago(i think).I usually upda
te to the latest version everytime.

I'm using A1111 direct ml (by Ishqqytiger) on Rx 590 8gb, chrome as browser, window
s 10 as os.

The generated image is either the same or has a blur on inapinted area. increasing mask blur also doesn't d
o anything it just makes the exact same face but with a weird sort of light blur on it.

I have tried changing every pos
sible setting to fix it such as clip skip, model, original mask mode, latent noise mask mode and the other 2 mask mode a
s well, changing cfg scale, denoising strength, sampler steps, samplers, inpaint area, resolution.

my command args is i
n the screen shot.

is this caused my some new update or some extension bug (I was not using any extension while generat
ing the images), or is it something just bad with my machine or is there a problem with SD directml version.
```
---

     
 
all -  [ [R] How to compare research results? ](https://www.reddit.com/r/computervision/comments/17cczj7/r_how_to_compare_research_results/) , 2023-11-11-0909
```
Hello all,

I am conducting research in the field of ViT. Research focuses on developing a method to improve ViT on a sm
all dataset from scratch and using ImageNet weights. In literature, I found similar work is already been proposed in the
 paper 'Efficient Training of Visual Transformers with Small Datasets' [https://proceedings.neurips.cc/paper/2021/file/c
81e155d85dae5430a8cee6f2242e82c-Paper.pdf](https://proceedings.neurips.cc/paper/2021/file/c81e155d85dae5430a8cee6f2242e8
2c-Paper.pdf).

My question is with whom to compare my method? should I compare with **this paper** or should I compare 
my results with the **original** ViT-S/32, ViT-B/32, ViT-T/32, ViT-T/16, SWIN-T, CVT, T2T.

Further, should I use the sa
me dataset or can I replace some with other datasets?
```
---

     
 
all -  [ [R] How to compare research results? ](https://www.reddit.com/r/MachineLearning/comments/17ccypi/r_how_to_compare_research_results/) , 2023-11-11-0909
```
Hello all,

I am conducting research in the field of ViT. Research focuses on developing a method to improve ViT on a sm
all dataset from scratch and using ImageNet weights. In literature, I found similar work is already been proposed in the
 paper 'Efficient Training of Visual Transformers with Small Datasets' [https://proceedings.neurips.cc/paper/2021/file/c
81e155d85dae5430a8cee6f2242e82c-Paper.pdf](https://proceedings.neurips.cc/paper/2021/file/c81e155d85dae5430a8cee6f2242e8
2c-Paper.pdf). 

My question is with whom to compare my method? should I compare with **this paper** or should I compare
 my results with the **original** ViT-S/32, ViT-B/32, ViT-T/32, ViT-T/16, SWIN-T, CVT, T2T.

Further, should I use the s
ame dataset or can I replace some with other datasets?
```
---

     
 
all -  [ MSCS Profile Evaluation - Fall 2024 ](https://www.reddit.com/r/gradadmissions/comments/17c2w15/mscs_profile_evaluation_fall_2024/) , 2023-11-11-0909
```
B.E. (ongoing) from a Tier 2 Institution in India  
CGPA: 9.46  
Research Papers: 4 (One accepted at NeurIPS workshop)  

Internships: 2 (one research-based at a US startup)  
LoRs: 2 from professors whom I have worked with (published resear
ch papers) and one from the startup (the founder is an MIT Postdoc)

This is where I am afraid:  
TOEFL: 100 (R:27, L:26
, S:23, W:24)  
This was my 2nd attempt to improve my speaking score but still couldn't do it.

Shortlisted Universities
:  


1. **Ambitious**  
MIT  
Stanford  
Princeton  
UCB  
UIUC  
UCSD  
UCLA  
UT Austin  
UMCP
2.  **Moderate**  
UMa
ss Amherst  
Purdue  
NEU  
ASU
```
---

     
 
all -  [ [R] Neural Relation Graph: A Unified Framework for Identifying Label Noise and Outlier Data (NeurIPS ](https://www.reddit.com/r/MachineLearning/comments/17bzbaq/r_neural_relation_graph_a_unified_framework_for/) , 2023-11-11-0909
```
**paper**: [https://arxiv.org/abs/2301.12321](https://arxiv.org/abs/2301.12321)

**code**: [https://github.com/snu-mllab
/Neural-Relation-Graph](https://github.com/snu-mllab/Neural-Relation-Graph)

**TDLR**: We present a scalable and domain-
agnostic approach utilizing the relational structure of data for identifying label noise and outliers

https://preview.r
edd.it/o9k7kliqe9vb1.png?width=3108&format=png&auto=webp&s=b7c34bd7f4bc130915440986570104f9bebd4f07

>Diagnosing and cle
aning data is a crucial step for building robust machine learning systems. However, identifying problems within large-sc
ale datasets with real-world distributions is challenging due to the presence of complex issues such as label errors, un
der-representation, and outliers. In this paper, we propose a unified approach for identifying the problematic data by u
tilizing a largely ignored source of information: a relational structure of data in the feature-embedded space. To this 
end, we present scalable and effective algorithms for detecting label errors and outlier data based on the relational gr
aph structure of data. We further introduce a visualization tool that provides contextual information of a data point in
 the feature-embedded space, serving as an effective tool for interactively diagnosing data. We evaluate the label error
 and outlier/out-of-distribution (OOD) detection performances of our approach on the large-scale image, speech, and lang
uage domain tasks, including ImageNet, ESC-50, and SST2. Our approach achieves state-of-the-art detection performance on
 all tasks considered and demonstrates its effectiveness in debugging large-scale real-world datasets across various dom
ains.

&#x200B;

[Detected samples with label error \(red colored\) from ImageNet \(top\) and SST2 \(bottom\).](https://
preview.redd.it/4x2244ure9vb1.png?width=2778&format=png&auto=webp&s=6c6cb9f8d1befce392d31546eab569ffa70d74cc)

&#x200B;


[Detected outlier samples from ImageNet \(top\) and SST2 \(bottom\) validation sets.](https://preview.redd.it/2kkfdspxe
9vb1.png?width=2720&format=png&auto=webp&s=312249638229b4cb5e815b76c1ef8309a829581b)
```
---

     
 
all -  [ [D] Has anybody heard back from NeurIPS financial aid yet? ](https://www.reddit.com/r/MachineLearning/comments/17bsyp6/d_has_anybody_heard_back_from_neurips_financial/) , 2023-11-11-0909
```
Was supposed to be Monday but instead it's rolling
```
---

     
 
all -  [ [R] Curve your Enthusiasm: Concurvity Regularization in Differentiable Generalized Additive Models ](https://www.reddit.com/r/MachineLearning/comments/17bfgsj/r_curve_your_enthusiasm_concurvity_regularization/) , 2023-11-11-0909
```
**Accepted at NeurIPS 2023**

*Link:* [https://arxiv.org/abs/2305.11475](https://arxiv.org/abs/2305.11475)

*Authors:* J
ulien Siems\*, Konstantin Ditschuneit\*, Winfried Ripken\*, Alma Lindborg\*, Maximilian Schambach, Johannes Otterbach, M
artin Genzel

\*equal contribution

*Abstract:* Generalized Additive Models (GAMs) have recently experienced a resurgenc
e in popularity due to their interpretability, which arises from expressing the target value as a sum of non-linear tran
sformations of the features. Despite the current enthusiasm for GAMs, their susceptibility to concurvity - i.e., (possib
ly non-linear) dependencies between the features - has hitherto been largely overlooked. Here, we demonstrate how concur
vity can severly impair the interpretability of GAMs and propose a remedy: a conceptually simple, yet effective regulari
zer which penalizes pairwise correlations of the non-linearly transformed feature variables. This procedure is applicabl
e to any differentiable additive model, such as Neural Additive Models or NeuralProphet, and enhances interpretability b
y eliminating ambiguities due to self-canceling feature contributions. We validate the effectiveness of our regularizer 
in experiments on synthetic as well as real-world datasets for time-series and tabular data. Our experiments show that c
oncurvity in GAMs can be reduced without significantly compromising prediction quality, improving interpretability and r
educing variance in the feature importances.

*Keywords:* Interpretable Machine Learning, Generalized Additive Models, C
oncurvity, Multicollinearity, Regularization, Time-Series Forecasting, Interpretability

https://preview.redd.it/wtdkhb3
bsbvb1.png?width=1002&format=png&auto=webp&s=3067a2361f55603bf4b7769eaede32ca1f32496f
```
---

     
 
all -  [ prof eval for AI PhD, declined last cycle ](https://www.reddit.com/r/gradadmissions/comments/17b3kxe/prof_eval_for_ai_phd_declined_last_cycle/) , 2023-11-11-0909
```
Finished undergrad in math/cs in 2.5 years from a solid research uni in the US (top 30 overall, top 10 for cs). 3.7 GPA 
with a few grad courses

1 tiny publication in astrophysics (not related at all)
1 first/solo author publication at a po
pular workshop in my field. 
5 papers under submission to WACV, ICLR, NeurIPS workshops (will know 4/5 of them by the en
d of the month). Likely will see 2-3 acceptances out of the 4. 

Currently ai research intern after undergrad and had a 
prev ai research internship, so like 1-1.5 years total experience

signed up for GRE and took it pretty much immediately
, got 157 verbal 168 quant and not sure if I should retake it & do a full prep. 

Main priority:
UCSD DSC / CSE PhD

Oth
ers:
UCSD ECE PhD (ML track)
Harvard CS PhD (really good research match there)
UCLA CS PhD (good research match too)
MIT
 PhD

Harvard MIT are big reach, but how far off am I for UCSD? is it worth to take GRE again? Last year I didn’t really
 talk to a lot of professors or have a good research match at UCSD, so I got declined (also no papers).

Edit: graduated
 9 months ago, applied to similar schools last year with no papers (was working on them, but not finished), no GRE, and 
got declined.

My field of research is generally in deep learning architectures (NAS, Model Compression, Quantization, S
SL)
```
---

     
 
all -  [ How can I stay up-to-date with the latest advancements in machine learning after completing a course ](https://www.reddit.com/r/u_nearlearns/comments/1755o0j/how_can_i_stay_uptodate_with_the_latest/) , 2023-11-11-0909
```
 

In the fast-evolving realm of [machine learning](https://nearlearn.com/blog/top-10-machine-learning-training-institut
e-bangalore/), staying up-to-date with the latest advancements is crucial. As the technology landscape constantly evolve
s, it’s essential to keep pace with the newest trends, methodologies, and breakthroughs to remain relevant and competiti
ve. This article provides a comprehensive guide on how to stay informed and at the forefront of the ever-changing field 
of machine learning.

### Why Staying Updated is Essential

Before delving into strategies for staying current, let’s fi
rst understand why it’s imperative to do so. Machine learning is a dynamic and innovative domain, and advancements occur
 at a breakneck pace. Here are a few reasons why staying updated is crucial:

1. Competitive Edge: In a highly competiti
ve job market, professionals who are well-versed in the latest developments in machine learning have a significant advan
tage. Cutting-edge knowledge can make you stand out among your peers.
2. Relevance: Machine learning models, tools, and 
techniques quickly become outdated. By staying current, you ensure your skills and knowledge are relevant, avoiding obso
lescence.
3. Innovation: The latest advancements often lead to new applications and possibilities. Staying updated enabl
es you to be at the forefront of innovation, allowing you to create groundbreaking solutions.

### Leveraging Online Res
ources

### 1. Online Courses and Tutorials

To keep abreast of the latest in machine learning, consider enrolling in on
line courses and tutorials. Websites like Coursera, edX, and Udacity offer a plethora of courses taught by experts in th
e field.

### 2. Blogs and Forums

Following [machine learning](https://nearlearn.com/machine-learning-classroom-trainin
g-in-bangalore-india) blogs and participating in relevant forums is another effective way to stay updated. Websites like
 Towards Data Science and Kaggle provide valuable insights, discussions, and community support.

### 3. YouTube and Podc
asts

Visual and auditory learners can benefit from machine learning YouTube channels and podcasts. These platforms offe
r engaging content from industry experts, often in a digestible format.

### 4. Social Media

Platforms like Twitter and
 LinkedIn are excellent for following influential figures and organizations in the machine learning space. Regularly che
cking your social media feeds can keep you informed about the latest news, research, and trends.

&#x200B;

https://prev
iew.redd.it/z85dalvu4itb1.png?width=1200&format=png&auto=webp&s=21413a440d23fcce49c4b203445b0b8693169126

**Read More** 
: [Everything You Need To Know About Machine Learning In 2023](https://nearlearn.com/blog/everything-you-need-to-know-ab
out-machine-learning-in-2023/)

### Attending Conferences and Meetups

1. Machine Learning Conferences: Attending confer
ences like NeurIPS, ICML, and ICLR provides an opportunity to learn from thought leaders and connect with peers. These e
vents showcase the most recent research and developments in the field.
2. Local Meetups: Joining machine learning meetup
s in your area can help you stay updated on local developments and network with professionals who share your interests.


### Academic Journals and Publications

1. Research Papers: Regularly reading academic journals and research papers is 
essential for a deep understanding of the latest advancements. Websites like ArXiv and Google Scholar are valuable resou
rces.
2. Books: Explore textbooks and publications by experts in machine learning. These provide comprehensive insights 
and foundational knowledge.

### Hands-On Learning

1. Personal Projects: Applying your knowledge through personal proje
cts allows you to experiment with new concepts and techniques. It’s an excellent way to gain practical experience with t
he latest advancements.
2. Competitions: Participate in machine learning competitions on platforms like Kaggle. These co
mpetitions often involve cutting-edge challenges that push your skills to the limit.

### Networking and Collaboration


1. Join Professional Networks: Being part of professional organizations like the Association for Computing Machinery (AC
M) or the Institute of Electrical and Electronics Engineers (IEEE) can help you connect with experts in the field.
2. Co
llaborate with Peers: Collaborative projects with colleagues and peers can expose you to different perspectives and inno
vative ideas.

### Continuous Learning

The field of machine learning is characterized by constant change. To stay ahead
, it’s crucial to embrace a mindset of continuous learning. Regularly set aside time for self-improvement, be it through
 online courses, conferences, or personal projects.

### In Conclusion

Staying updated with the latest advancements in 
machine learning is vital for personal and professional growth. In this dynamic field, knowledge is power, and being wel
l-informed can open doors to exciting opportunities and innovations. By leveraging online resources, attending conferenc
es, reading academic publications, engaging in hands-on learning, and building a network of like-minded individuals, you
 can ensure that you’re always at the forefront of this ever-evolving field.
```
---

     
