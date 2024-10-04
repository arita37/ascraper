 
all -  [ [R] Announcing the first series of Liquid Foundation Models (LFMs) – a new generation of generative  ](https://www.reddit.com/r/MachineLearning/comments/1fvgo7o/r_announcing_the_first_series_of_liquid/) , 2024-10-04-0912
```
https://www.liquid.ai/liquid-foundation-models

https://www.liquid.ai/blog/liquid-neural-networks-research

https://x.co
m/teortaxesTex/status/1840897331773755476

'We announce the first series of Liquid Foundation Models (LFMs), a new gener
ation of generative AI models built from first principles.

Our 1B, 3B, and 40B LFMs achieve state-of-the-art performanc
e in terms of quality at each scale, while maintaining a smaller memory footprint and more efficient inference.'

'LFM-1
B performs well on public benchmarks in the 1B category, making it the new state-of-the-art model at this size. This is 
the first time a non-GPT architecture significantly outperforms transformer-based models.

LFM-3B delivers incredible pe
rformance for its size. It positions itself as first place among 3B parameter transformers, hybrids, and RNN models, but
 also outperforms the previous generation of 7B and 13B models. It is also on par with Phi-3.5-mini on multiple benchmar
ks, while being 18.4% smaller. LFM-3B is the ideal choice for mobile and other edge text-based applications.

LFM-40B of
fers a new balance between model size and output quality. It leverages 12B activated parameters at use. Its performance 
is comparable to models larger than itself, while its MoE architecture enables higher throughput and deployment on more 
cost-effective hardware.

LFMs are large neural networks built with computational units deeply rooted in the theory of d
ynamical systems, signal processing, and numerical linear algebra.

LFMs are Memory efficient LFMs have a reduced memory
 footprint compared to transformer architectures. This is particularly true for long inputs, where the KV cache in trans
former-based LLMs grows linearly with sequence length.

LFMs truly exploit their context length: In this preview release
, we have optimized our models to deliver a best-in-class 32k token context length, pushing the boundaries of efficiency
 for our size. This was confirmed by the RULER benchmark.

LFMs advance the Pareto frontier of large AI models via new a
lgorithmic advances we designed at Liquid: 
 
Algorithms to enhance knowledge capacity, multi-step reasoning, and long-c
ontext recall in models + algorithms for efficient training and inference.

We built the foundations of a new design spa
ce for computational units, enabling customization to different modalities and hardware requirements.

What Language LFM
s are good at today:
General and expert knowledge,
Mathematics and logical reasoning,
Efficient and effective long-conte
xt tasks,
A primary language of English, with secondary multilingual capabilities in Spanish, French, German, Chinese, A
rabic, Japanese, and Korean.

What Language LFMs are not good at today:
Zero-shot code tasks,
Precise numerical calculat
ions,
Time-sensitive information,
Counting r’s in the word “Strawberry”!,
Human preference optimization techniques have 
not yet been applied to our models, extensively.'

'We invented liquid neural networks, a class of brain-inspired system
s that can stay adaptable and robust to changes even after training [R. Hasani, PhD Thesis] [Lechner et al. Nature MI, 2
020] [pdf] (2016-2020). We then analytically and experimentally showed they are universal approximators [Hasani et al. A
AAI, 2021], expressive continuous-time machine learning systems for sequential data [Hasani et al. AAAI, 2021] [Hasani e
t al. Nature MI, 2022], parameter efficient in learning new skills [Lechner et al. Nature MI, 2020] [pdf], causal and in
terpretable [Vorbach et al. NeurIPS, 2021] [Chahine et al. Science Robotics 2023] [pdf], and when linearized they can ef
ficiently model very long-term dependencies in sequential data [Hasani et al. ICLR 2023].

In addition, we developed cla
sses of nonlinear neural differential equation sequence models [Massaroli et al. NeurIPS 2021] and generalized them to g
raphs [Poli et al. DLGMA 2020]. We scaled and optimized continuous-time models using hybrid numerical methods [Poli et a
l. NeurIPS 2020], parallel-in-time schemes [Massaroli et al. NeurIPS 2020], and achieved state-of-the-art in control and
 forecasting tasks [Massaroli et al. SIAM Journal] [Poli et al. NeurIPS 2021][Massaroli et al. IEEE Control Systems Lett
ers]. The team released one of the most comprehensive open-source libraries for neural differential equations [Poli et a
l. 2021 TorchDyn], used today in various applications for generative modeling with diffusion, and prediction.

We propos
ed the first efficient parallel scan-based linear state space architecture [Smith et al. ICLR 2023], and state-of-the-ar
t time series state-space models based on rational functions [Parnichkun et al. ICML 2024]. We also introduced the first
-time generative state space architectures for time series [Zhou et al. ICML 2023], and state space architectures for vi
deos [Smith et al. NeurIPS 2024]

We proposed a new framework for neural operators [Poli et al. NeurIPS 2022], outperfor
ming approaches such as Fourier Neural Operators in solving differential equations and prediction tasks.

Our team has c
o-invented deep signal processing architectures such as Hyena [Poli et al. ICML 2023] [Massaroli et al. NeurIPS 2023], H
yenaDNA [Nguyen et al. NeurIPS 2023], and StripedHyena that efficiently scale to long context. Evo [Nguyen et al. 2024],
 based on StripedHyena, is a DNA foundation model that generalizes across DNA, RNA, and proteins and is capable of gener
ative design of new CRISPR systems.

We were the first to scale language models based on both deep signal processing and
 state space layers [link], and have performed the most extensive scaling laws analysis on beyond-transformer architectu
res to date [Poli et al. ICML 2024], with new model variants that outperform existing open-source alternatives. 

The te
am is behind many of the best open-source LLM finetunes, and merges [Maxime Lebonne, link].

Last but not least, our tea
m’s research has contributed to pioneering work in graph neural networks and geometric deep learning-based models [Lim e
t al. ICLR 2024], defining new measures for interpretability in neural networks [Wang et al. CoRL 2023], and the state-o
f-the-art dataset distillation algorithms [Loo et al. ICML 2023].'
```
---

     
 
all -  [ Bringing Learning to Rank to Reddit - LTR modeling ](https://www.reddit.com/r/RedditEng/comments/1ft1tkw/bringing_learning_to_rank_to_reddit_ltr_modeling/) , 2024-10-04-0912
```
*Written by Sahand Akbari.*

In the previous series of articles in the learning to rank series, we looked at how we set 
up the [training data](https://www.reddit.com/r/RedditEng/comments/191nhka/bringing_learning_to_rank_to_reddit_search_go
als/) for the ranking model, how we did [feature engineering](https://www.reddit.com/r/RedditEng/comments/191nhka/bringi
ng_learning_to_rank_to_reddit_search_goals/), and [optimized our Solr clusters](https://www.reddit.com/r/RedditEng/comme
nts/1efartq/bringing_learning_to_rank_to_reddit_search/) to efficiently run LTR at scale. In this post we will look at l
earning to rank ML modeling, specifically how to create an effective objective function. 

To recap, imagine we have the
 following training data for a given query.

|Query|Post ID|Post Title|F1: Terms matching post title|F2: Terms matching 
posts body text|F3: Votes|Engagement Grade|
|:-|:-|:-|:-|:-|:-|:-|
|Cat memes|p1|Funny cat memes|2|1|30|0.9|
|Cat memes|
p2|Cat memes ?|2|2|1|0.5|
|Cat memes|p3|Best wireless headphones|0|0|100|0|

For simplicity, imagine our features in our
 data are defined per each query-post pair and they are:

* F1: Terms in the query matching the post title
* F2: Terms i
n the query matching the post body
* F3: number of votes for this post

Engagement grade is our label per query-post pai
r. It represents our estimation of how relevant the post is for the given query. Let’s say it’s a value between 0 and 1 
where 1 means the post is highly relevant and 0 means it’s completely irrelevant. Imagine we calculate the engagement gr
ade by looking at the past week's data for posts redditors have interacted with and discarding posts with no user intera
ction. We also add some irrelevant posts by randomly sampling a post id for a given query (i.e [negative sampling](https
://www.reddit.com/r/RedditEng/comments/191nhka/bringing_learning_to_rank_to_reddit_search_goals/)). The last row in the 
table above is a negative sample. Given this data, we define an engagement-based grade as our labels: click through rate
 (CTR) for each query-post pair defined by ratio of total number of clicks on the post for the given query divided by to
tal number of times redditors viewed that specific query-post pair.

Now that we have our features and labels ready, we 
can start training the LTR model. The goal of an LTR model is to predict a relevance score for each query-post pair such
 that more relevant posts are ranked higher than less relevant posts. Since we don’t know the “true relevance” of a post
, we approximate the true relevance with our engagement grade.

One approach to predicting a relevance score for each qu
ery-post is to train a supervised model which takes as input the features and learns to predict the engagement grade dir
ectly.  In other words, we train a model so that its predictions are as close as possible to the engagement grade. We’ll
 look closer at how that can be done. But first, let’s review a few concepts regarding supervised learning. If you alrea
dy know how supervised learning and gradient descent work, feel free to skip to the next section.

# Machine Learning cr
ash course – Supervised Learning and Gradient Descent

Imagine we have `d` features ordered in a vector (array) `x = [x1
, x2, …, xd]`and a label `g`(grade). 

Also for simplicity imagine that our model is a linear model that takes the input
 `x` and predicts `y` as output:

https://preview.redd.it/947okib4ezrd1.png?width=1096&format=png&auto=webp&s=9dc8a5656a
a9ff520b42179259284c7273ca82e4

We want to penalize the model when `y` is different from `g`. So we define a Loss functi
on that measures that difference. An example loss function is squared error loss `(y-g)^2`. The closer `y` is to `g` the
 smaller the loss is. 

In training, we don’t have just one sample `(x, g)` but several thousands (or millions) of sampl
es. Our goal is to change the weights `w` in a way that makes the loss function over all samples as small as possible.


In the case of our simple problem and loss function we can have a [closed-form solution](https://en.wikipedia.org/wiki/C
losed-form_expression) to this optimization problem, however for more complex loss functions and for practical reasons s
uch as training on large amounts of data, there might not be an efficient closed-form solution. As long as the loss func
tion is end-to-end differentiable and has other desired mathematical properties, one general way of solving this optimiz
ation problem is using [stochastic gradient descent](https://en.wikipedia.org/wiki/Gradient_descent) where we make a ser
ies of small changes to weights `w` of the model. These changes are determined by the negative of the gradient of the lo
ss function `L`. In other words, we take a series of small steps in the direction that minimizes `L`. This direction is 
approximated at each step by taking the negative gradient of `L` with respect to `w` on a small subset of our dataset. 


At the end of training, we have found a `w` that minimizes our Loss function to an acceptable degree, which means that 
our predictions `y` are as close as possible to our labels `g` as measured by `L`. If some conditions hold, and we’ve tr
ained a model that has learned true patterns in the data rather than the noise in the data, we'll be able to generalize 
these predictions. In other words, we’ll be able to predict with reasonable accuracy on unseen data (samples not in our 
training data).

One thing to remember here is that the choice of weights `w` or more generally the model architecture (
we could have a more complex model with millions or billions of weights) allows us to determine how to get from inputs t
o the predictions. And the choice of loss function `L` allows us to determine what (objective) we want to optimize and h
ow we define an accurate prediction with respect to our labels. 

# Learning to rank loss functions

Now that we got tha
t out of the way, let’s discuss choices of architecture and loss. For simplicity, we assume we have a linear model. A li
near model is chosen only for demonstration and we can use any other type of model (in our framework, it can be any end 
to end differentiable model since we are using stochastic gradient descent as our optimization algorithm).

https://prev
iew.redd.it/xb09p119fzrd1.png?width=1096&format=png&auto=webp&s=a4914f2e67883df40b1fc5d75ad45287f895faa4

An example los
s function is `(y-g)^2`. The closer `y` is to `g` on average, the smaller the loss is. This is called a pointwise loss f
unction, because it is defined for a single query-document sample. 

While these types of loss functions allow our model
 output to approximate the exact labels values (grades), this is not our primary concern in ranking. Our goal is to pred
ict scores that produce the correct *rankings* regardless of the exact value of the *scores* (model predictions). For th
is reason, [learning to rank](https://en.wikipedia.org/wiki/Learning_to_rank) differs from classification and regression
 tasks which aim to approximate the label values directly. For the example data above, for the query “cat memes”, the ra
nking produced by the labels is \[p1 - p2 - p3\]. An Ideal LTR loss function should penalize the predictions that produc
e rankings that differ from the ranking above and reward the predictions that result in similar rankings.

*Side Note: U
sually in Machine learning models, loss functions express the “loss” or “cost” of making predictions, where cost of maki
ng the right predictions is zero. So lower values of loss mean better predictions and we aim to minimize the loss.*

*Pa
irwise* loss functions allow us to express the correctness of the ranking between a pair of documents for a given query 
by comparing the rankings produced by the model with rankings produced by the labels given a pair of documents. In the d
ata above for example, p1 should be ranked higher than p2 as its engagement grade is higher. If our model prediction is 
consistent, i.e. the predicted score for p1 is higher than p2, we don’t penalize the model. On the other hand, if p1’s s
core is higher than p2, the loss function assigns a penalty.

https://preview.redd.it/dp3ohw2nfzrd1.png?width=940&format
=png&auto=webp&s=0e7d3eca8ce5d981bb68e98c405daaac08f99d75

Loss for a given query `q` is defined as the sum of pairwise 
losses for all pairs of documents `i,j`.

`1(g_i > g_j)` is an indicator function. It evaluates to 1 when `g_i > g_j` an
d to 0 otherwise. This means that if the grade of document `i` is larger than the grade of document `j`, the contributio
n of `i,j` to loss is equal to `max(0, 1 - (y_i - y_j)).` In other words, if `g_i > g_j`, loss decreases as `(y_i - y_j)
` increases because our model is ranking document `i` higher than document `j`. Loss increases when the model prediction
 for document `j` is higher than document `i`. 

One downside of using pairwise loss is the increase in computational co
mplexity relative to pointwise solutions. For each query, we need to calculate the pairwise loss for distinct document p
airs. For a query with `D` corresponding posts, the computation complexity is `O(D^2)` while for a pointwise solution it
 is `O(D)`. In practice, we usually choose a predefined number of document pairs rather than calculating the loss for al
l possible pairs.

In summary, we calculate how much the pairwise difference of our model scores for a pair of documents
 matches the relative ranking of the documents by labels (which one is better according to our grades). Then we sum the 
loss for all such pairs to get the loss for the query. The loss of a given dataset of queries can be defined as the aggr
egation of loss for each queries. 

Having defined the loss function `L` and our model `f(x)`, our optimization algorith
m (stochastic gradient descent) finds the optimal weights of the model (`w` and `b`)  that minimizes the loss for a set 
of queries and corresponding documents. 

In addition to pointwise and pairwise ranking loss functions, there's another 
category known as *listwise*. Listwise ranking loss functions assess the entire ranked list, assigning non-zero loss to 
any permutation that deviates from the ideal order. Loss increases with the degree of divergence. 

These functions prov
ide the most accurate formulation of the ranking problem, however, to compute a loss based on order of the ranked list, 
the list needs to be sorted. Sorting is a non-differentiable and non-[convex](https://en.wikipedia.org/wiki/Convex_funct
ion) function. This makes the gradient based optimization methods a non-viable solution. [Many studies](http://icml2008.
cs.helsinki.fi/papers/167.pdf) have sought to create approximate listwise losses by either [directly](https://proceeding
s.neurips.cc/paper/2021/file/b5200c6107fc3d41d19a2b66835c3974-Paper.pdf) approximating sorting with a differentiable fun
ction or by defining an [approximate loss](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/SoftRankW
sdm08Submitted.pdf) that penalizes deviations from the ideal permutation order. The other challenge with listwise approa
ches is computationally complexity as these approaches need to maintain a model of permutation distribution which is fac
torial in nature. In practice, there is usually a tradeoff between degree of approximation and computational complexity.


For learning to rank at Reddit Search, we used a weighted pairwise loss called [LambdaRank](https://www.microsoft.com/
en-us/research/wp-content/uploads/2016/02/MSR-TR-2010-82.pdf). The shortcoming of the pairwise hinge loss function defin
ed above is that different pairs of documents are treated the same whereas in search ranking we usually care more about 
higher ranked documents. LambdaRank defines a pairwise weight (i.e. LambdaWeight), dependent on positions of the documen
ts, to assign an importance weight for each comparison. Our pairwise hinge loss with lambda weight becomes: 

https://pr
eview.redd.it/a70xg8f6hzrd1.png?width=1036&format=png&auto=webp&s=5f383fc396bd1328027b458ba20a41336df3b3e2

There are di
fferent ways to define the importance of comparisons. We use [NDCG lambda weight](https://www.tensorflow.org/ranking/api
_docs/python/tfr/keras/losses/NDCGLambdaWeight) which calculates a weight proportionate to the degree of change in [NDCG
](https://en.wikipedia.org/wiki/Discounted_cumulative_gain) after a swap is made in the comparison.

*Side Note: We stil
l need to sort the ranking list in order to calculate the LambdaWeight and since sorting is not a differentiable operati
on, we must calculate the LambdaWeight component without gradients. In tensorflow, we can use* [*tf.stop\_gradient*](htt
ps://github.com/tensorflow/ranking/blob/c46cede726fd453e0aaa6097871d23dc8e465bdc/tensorflow_ranking/python/losses_impl.p
y#L882) *to achieve this.*

One question that remains: how did we choose `f(x)`? We opted for a dense neural network (i.
e. multi-layer perceptron). Solr supports the Dense Neural network architecture in the [Solr LTR plugin](https://solr.ap
ache.org/docs/8_7_0/solr-ltr/org/apache/solr/ltr/model/NeuralNetworkModel.html) and we used [tensorflow-ranking](https:/
/www.tensorflow.org/ranking) for training the ranker and exporting to the Solr LTR format. Practically, this allowed us 
to use the tensorflow ecosystem for training and experimentation and running LTR at scale within Solr. While gradient bo
osted trees such as [LambdaMart](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/MSR-TR-2010-82.pdf)
 are popular architectures for learning to rank, using end-to-end differentiable neural networks allows us to have a mor
e extensible architecture by enabling only minimal modifications to the optimization algorithm (i.e. stochastic gradient
 descent) when adding new differentiable components to the model (such as semantic embeddings).   

We have our model! S
o how do we use it? 

Imagine the user searches for “dog memes”. We have never seen this query and corresponding documen
ts in our training data. This means that we don’t have any engagement grades. Our model trained by the Pairwise loss, ca
n now predict scores for each query - document pair.  Sorting the model scores in a descending order will result in a ra
nking of documents that will be returned to the user. 



|Query|Post ID|Post Title|F1: Terms matching post title|F2: Te
rms matching posts body|F3: Votes|Engagement Grade|Model Predicted Score|
|:-|:-|:-|:-|:-|:-|:-|:-|
|dog memes|p1|Funny 
dog memes|2|1|30|?|10.5|
|dog memes|p2|Dog memes|2|2|1|?|3.2|
|dog memes|p3|Best restaurant in town?|0|0|100|?|0.1|

# C
onclusion

In this post, we explored how learning-to-rank (LTR) objectives can be used to train a ranking model for sear
ch results. We examined various LTR loss functions and discussed how we structure training data to train a ranking model
 for Reddit Search. A good model produces rankings that put relevant documents at the top. How can we measure if a model
 is predicting good rankings? We would need to define what “good” means and how to measure better rankings. This is some
thing we aim to discuss in a future blog post. So stay tuned!
```
---

     
 
all -  [ MSCS FALL'25 Profile evaluation ](https://www.reddit.com/r/MSCS/comments/1ft08a6/mscs_fall25_profile_evaluation/) , 2024-10-04-0912
```
# Country:

- From Pakistan

# Undergraduate University:

- Not good ranked  
- CGPA: 3.43 / 4.0  
- No Undergrad Thesis
, a Final year project  
- GRE (Not given, want to apply to unis which do not require GRE)

# Industry Experience:

- 3+
 years total as a ML Engineer  
- 1 internship at a startup  
- working in a silicon valley startup as DeepLearning Engi
neer for the past year  
- AI Fellow at PI School of AI

# Research Experience:

- Research Collaborator at MIT Media La
b, 1 paper published at NeurIPS, 1 under-review at ICLR. (I am not leading author in both)  
- AI Research/Pre-doctoral 
fellow at Fatima Fellowship (On-going, probably will publish my work by Dec)

# Considering the following UNIs as they d
o not require GRE in MS:

- umass amherst  
- john hopkins  
- Virginia Tech  
- Texas A&M  
- ohio state  
- uni of min
nisota  
- Darmouth  
- UNC Walmington  
- NorthEastern  
- NorthWetern
```
---

     
 
all -  [ [D] Resources for staying updated on recent papers ](https://www.reddit.com/r/MachineLearning/comments/1fsx8q2/d_resources_for_staying_updated_on_recent_papers/) , 2024-10-04-0912
```
Hello, I’m looking for time-saving ways to stay updated on the latest research papers from conferences like CVPR, ECCV, 
NeurIPS, ICML, and journals like TPAMI. I know these conferences/journals publish cutting-edge work, but keeping track o
f all the new papers gets overwhelming at times. I’m interested in resources that summarize or highlight the most signif
icant papers, like blogs, newsletters, or curated lists. Does anyone know of any:

1. blogs or newsletters that regularl
y cover the latest papers from these conferences and journals
2. twitter discussions, subreddits, medium blogs, or perso
nal websites run by researchers who highlight or summarize key papers (I've heard about paperswithcode and 2-minute pape
rs but are they quick with such newly published papers?)
3. curated paper repositories (github or any websites) where pe
ople organize papers based on recent conferences/journals?

I’m particularly interested in resources that focus on compu
ter vision, neural network architectures, and their optimization. I’d appreciate any suggestions or tips. Thanks in adva
nce!
```
---

     
 
all -  [ [R] optimizing transformers ](https://www.reddit.com/r/MachineLearning/comments/1fsgz5i/r_optimizing_transformers/) , 2024-10-04-0912
```
Hello, I’m currently aiming to work on optimizing transformer models, specifically in multi-view images and/or cross-att
ention networks. I've noticed that cross-attention layers add up a lot of parameters, which can slow down the training p
rocess. I’m exploring ways to reduce the computational complexity to increase the speed (for now and subsequently withou
t sacrificing too much performance sometime later). I'm starting to look into:

1. low-rank matrix factorization - I’ve 
been reading about how it can be applied to reduce the size of the projection matrices (e.g., the projq, projk, projv in
 cross-attention). Does anyone have experience using low-rank factorization specifically in cross-attention mechanisms?

2. other param reduction techniques - Aside from low-rank factorization, are there other methods I could explore for red
ucing the number of parameters in transformer models, like sparsity and pruning—do you have recommendations or experienc
es with these?
3. overcoming redundancy in multi-view scenarios - Given the multi-view nature of my problem, I suspect t
here’s some redundancy in how cross-attention processes the different views. Has anyone worked on reducing redundancy ac
ross views in transformer-based networks? What techniques worked best for you?

I’m starting to look into CVPR, NEURIPS,
 ECCV, etc, but any insights, advise, experiences, or papers you can share would be greatly appreciated! Thanks in advan
ce!
```
---

     
 
all -  [ 人大附高中生中NeurIPS，入选高中赛道Spotlight，顶会真卷到中学了 ](https://www.reddit.com/r/real_China_irl/comments/1fs0z7a/人大附高中生中neurips入选高中赛道spotlight顶会真卷到中学了/) , 2024-10-04-0912
```
NeurIPS 2024放榜，人大附中有高中生一作入选。

今年，NeurIPS率先把AI顶会卷到了高中里，正式面向高中生征集论文，还为此专门设置了高中生赛道（High School Projects Track）。

现在结果终于出炉，北
京大学计算机学院的张铭教授分享了一则入围消息：

人大附中吴悠，有一篇一作论文入选该赛道，还被选为了Spotlight Project。



论文题为《Vision-Braille：An End-to-End Tool for Chine
se Braille Image-to-Text Translation》，提出了一种中文盲文图像到文本的端到端翻译工具。

据张铭教授介绍，吴悠在2022年高一加入她的课题组时，就提出了这个项目的想法。



# 端到端中文盲文图像到文本
翻译工具

具体来说，该项目基于谷歌的mT5模型，采用Curriculum Learning（课程学习）方法微调出了一个盲文翻译模型。



其中的难点主要包括几个方面：

缺少数据集：中文盲文翻译数据集非常稀缺，数据的采集也比较困难，需要
耗费大量人力。

盲文数据的特殊性：盲文通过最多三个单元格来表示每个汉字的发音，即声母、韵母和音调。但在实际使用中，盲文使用者通常会省略大部分声调符号，这给盲文翻译带来了挑战。

同音字混淆：中文中存在大量同音字，并且由于声调符号经常被省略
，同音字的区分变得更加困难。

为此，论文作者们首先构建了一组中文-盲文数据集，包括Chinese-Braille-Full-Tone、Chinese-Braille-No-Tone和Chinese-Braille-10per-Tone。


作者从莱比锡数据集中收集了100万个不同的中文句子，使用中文盲文在线平台提供的工具，将收集到的中文句子转换为“全音”盲文。

而后，为了模拟真实世界中盲文使用者省略声调的情况，作者识别出这些盲文中代表声调的部分，并随机去除了其中90%的声
调，创建Chinese-Braille-10per-Tone以反映现实世界中中文盲文的使用情况。

数据按照8:1:1的比例被划分为训练集、验证集和测试集。



训练方法方面，作者使用RetinaNet来执行盲文OCR任务，将盲文图像转换
为数字盲文字符。

接着，采用课程学习策略——即从简单到复杂地安排训练任务，分三个阶段微调了多语言Transformer模型mT5：

第一阶段：使用Chinese-Braille-Full-Tone数据集作为训练的简单部分，让模型学习基本
的翻译规则。这个数据集中的盲文包含完整的声调信息。

第二阶段：使用Chinese-Braille-No-Tone数据集，让模型在没有声调信息的情况下，学会根据上下文猜测正确的中文字符。

第三阶段：使用Chinese-Braille-10
per-Tone数据集，让模型更好地适应实际应用场景。

实验结果显示，在验证集和测试集上，该模型的BLEU得分分别达到了62.4和62.3，显著提高了盲文翻译的准确度。

论文作者已经放出了项目Demo，效果是酱婶的，感兴趣的小伙伴们可以
戳文末链接自行测试：



（正确答案：不过，对于自己外向的性格，埃托奥说，“这就是真实的我，我不会为此改变。）

该项目是在吴悠高三时完成。张铭教授透露，他目前已进入康奈尔大学就读计算机和生物医药工程专业。

论文致谢中提到，吴悠主要是在
张铭教授博士生、论文第二作者袁野的指导下完成了这项研究。

张铭，北京大学计算机学院教授，博士生导师，研究领域包括文本挖掘、知识图谱、图神经网络和计算机教育研究等。她合作发表的科研学术论文曾获ICML 2014最佳论文、ICDM 2022最
佳论文提名等荣誉。Google Scholar显示，她的论文引用量接近2万，h指数为48。

# NeurIPS高中生赛道

NeurIPS是今年刚设的“高中生赛道”，主要征集“机器学习的社会影响”方向的论文。



公告是这样写的：

>


详细来说，就是允许高中生们找外部导师来合作完成项目，但必须把导师以及合作者的贡献，和高中生作者的贡献区分开来。

公告中还规定了，作者需要提交高中在读证明，所有补充材料均应完全由作者完成，包括视频、Demo、海报、网站或源代码。

值得
一提的是，其他顶会也有积极接触和影响高中生的趋势。
```
---

     
 
all -  [ Merit of high level research publication ](https://www.reddit.com/r/ApplyingToCollege/comments/1fr97j4/merit_of_high_level_research_publication/) , 2024-10-04-0912
```
How much will a first-author **workshop** paper acceptance (not main conference) at a prestigious venue like NeurIPS (1s
t one): [https://scholar.google.com/citations?view\_op=top\_venues&hl=en&vq=eng\_artificialintelligence](https://scholar
.google.com/citations?view_op=top_venues&hl=en&vq=eng_artificialintelligence) boost an Asian CS kids chances at top coll
eges?

Would this be considered on the same tier as ISEF or something of the sort. Is this enough to somewhat guarantee 
admission into a top 10?

Thanks
```
---

     
 
all -  [ Post-PhD Education for Quant ](https://www.reddit.com/r/quantfinance/comments/1fpewtu/postphd_education_for_quant/) , 2024-10-04-0912
```
Please don't downvote. I already asked before in r/quant but you have to do that in a weekly thread and it's often hard 
to get any answers. (I've never gotten a reply to date.) There doesn't seem to be rules against this kind of post in thi
s sub though (and there are a couple of others).

This is in the US. Feel free to continue for details, or skip to **TL;
DR**.

I have a theoretical physics PhD and I did mostly heavy mathematical research with little to no programming invol
ved. I learned on my own, but due to immigration constraints, couldn't get internships because my advisor was the 'indus
try sucks' type and wouldn't approve anything that wasn't academic. So wasn't able to intern throughout PhD, and when I 
graduated in the middle of COVID, my student VISA timeline was working against me and I had to go for a post-doc. (Note:
 publication record is not super strong because it was heavy theory work, and the academic post-doc was just one year. S
o I got like 3 or 4 papers in strong journals, but not the 10+ papers in ICML, NeurIPS, etc. More of the classical 'I pu
blished good papers in good research journals', which takes time.)

I managed to then secure a fixed-term position as a 
research scientist doing ML with applications to in finance at a good tech company (like those PhD programmes at banks) 
that was basically an industry post-doc (think like Microsoft/Meta/Apple ML Post-Doc but in quant finance).

That positi
on ran out last year, and since I was still under immigration constraints, and the market being what it was, the best I 
could secure was a position as a Data Scientist at a consulting firm. I did got some buyside quant interviews, but they 
were either looking for strong quant devs or seasoned QRs and wouldn't consider me for fresh grad / early career PhD pos
itions. The sellside ones I did get seemed to expect far more tech experience despite the positions being labeled 'ML sc
ientist' or 'research scientist'.

My concern here is the branding aspect: PhD was not from a target school, not in the 
more desired majors (applied math, stats, EE), and my experience so far seems to not help either despite it fairly techn
ical ML research in quant finance.

This branding issue seems to be US-specific to me because I have a friend who went t
o London instead to do post-doc and then had no issue getting into a Tier 2 multi-strat via the typical math + LC interv
iew pipeline. His same firm would not consider me at all on the US side, even though we went to the same grad school, he
's got even less of a publication record, and we have the same competitive background (in terms of physics olympiads, GP
As, etc).

This has gotten me to the point of considering doing a short but intense specialized QF masters at a target s
chool, either in the US (Baruch MFE being my primary target) or something like the MSc in QF at Erasmus or MSc in QF at 
ETH Zurich, in Europe. (EUR examples based on duration, cost, and reputation.) Now that I finally got to a point were my
 Green Card got through, if it’s a European Masters, I'd obviously prefer to do something like that and go right back to
 the US, but I'm open to other options.

Obviously the clear flaw is that it still indicates some sort of weak profile b
ecause the obvious question would be 'why masters after PhD?' but the markets in the US vs Europe have been very differe
nt over the past 4 years (perhaps a bit more) with the typical QR hiring really favoring a more solid CS background, in 
my opinion. At some point, I'd think that's a gap you can't convincingly cover via applied research experience.

My ques
tion is: what are my options if I still want to pursue some sort of quant finance career (whether its buyside or sellsid
e)? (I'm open to all sorts of roles, including data scientist roles and the like, as long as modeling is an important co
mponent, but I'm really interested in the quant finance industry specifically.)

**TL;DR:**

Background:

* Theoretical 
Physics PhD (US, non-target)
* 1 year academic post-doc
* 2 years industry post-doc
   * Post-doc course and lack of int
ernship experience due to immigration constraints and lack of PhD advisor assistance with approvals for industry interns
hips
* Currently working as a data scientist in a consulting firm
* Very strong math background, classical ML (statistic
al learning) modeling experience
* Reasonably well-versed in Python programming (built libraries entirely from scratch a
s part of research and applied research work; worked with teams)
* Now finally have US permanent residency, and can expl
ore more options

Main problem:

* Seem to be suffering from a branding issue given career trajectory so far and lack of
 industry connections
* Not being considered for fresh PhD roles anywhere in the US (but friends with 95% similar profil
es not having this issue elsewhere in Europe)
* Not sure how to re-align and pursue a QR/QR-adjacent (read modeling-orie
nted role) career

Options considered:

* Intensive Masters in QF at Target School (US, Europe) to secure a good QR/QR-a
djacent position and spring back to the US
   * Concerned about the perception of 'Masters after PhD' (more tolerated in
 other industries, seems to be heavily frowned upon in quant finance)
* Willing to also pursue quant trading trajectory 
if it makes sense

Seeking options and guidance, flexible on roles to pursue as long as they're reasonably modeling-orie
nted as opposed to SWE-heavy (quant dev and the like)
```
---

     
 
all -  [ LEGO Meets AI: BricksRL Accepted at NeurIPS 2024! ](https://www.reddit.com/r/reinforcementlearning/comments/1fpebw9/lego_meets_ai_bricksrl_accepted_at_neurips_2024/) , 2024-10-04-0912
```
We're excited to share that our paper on BricksRL, a library of RL algorithms that can be trained and deployed on afford
able, custom LEGO robots, has been accepted at NeurIPS 2024 as a spotlight paper!

As AI and machine learning continue t
o make waves, we believe it's essential to make reliable and affordable education tools available to the community. Not 
everyone has access to hundreds of GPUs, and understanding how ML works in practice can be challenging.

That's why we'v
e been working on BricksRL, a collaboration between Universitat Pompeu Fabra and PyTorch. Our goal is to provide a fun a
nd engaging way for people to learn about AI, ML, robotics, and PyTorch, while maintaining high standards of correctness
 and robustness.

BricksRL is based on Pybricks and can be deployed on many different LEGO hubs. We hope it will empower
 labs worldwide to prototype ideas affordably without requiring expensive robots.

  
Check out our website: [https://br
icksrl.github.io/ProjectPage/](https://bricksrl.github.io/ProjectPage/)

The library is open-sourced under an MIT licens
e on GitHub: [https://github.com/BricksRL/bricksrl/](https://github.com/BricksRL/bricksrl/)

Read our paper: [https://ar
xiv.org/abs/2406.17490](https://arxiv.org/abs/2406.17490)

Watch the robots in action: [https://www.youtube.com/watch?v=
k\_Vb30ZSatk&t=10s](https://www.youtube.com/watch?v=k_Vb30ZSatk&t=10s)

We're working on some exciting follow-up project
s, so stay tuned!

See you in Vancouver

https://preview.redd.it/1ghfs9t9l0rd1.jpg?width=2006&format=pjpg&auto=webp&s=86
8867adcd52825bd4ee719513a454527d017307


```
---

     
 
all -  [ [D] NeurIPS 2024 Review Question  ](https://www.reddit.com/r/MachineLearning/comments/1fpa7ua/d_neurips_2024_review_question/) , 2024-10-04-0912
```
My initial reviewers addressed some weaknesses & concerns, but these were resolved in my rebuttals. They acknowledged an
d raised their score. 

My paper was ultimately rejected because the program chair introduced new weaknesses that are a 
result of misreading the paper, if these were stated in the original reviews, this would easily be resolved. Is there an
ything I can do to fix this program chair review?
```
---

     
 
all -  [ [D] - NeurIPS 2024 Decisions ](https://www.reddit.com/r/MachineLearning/comments/1foky4r/d_neurips_2024_decisions/) , 2024-10-04-0912
```
Hey everyone! Just a heads up that the NeurIPS 2024 decisions notification is set for September 26, 2024, at 3:00 AM CES
T. I thought it’d be cool to create a thread where we can talk about it.
```
---

     
 
all -  [ Should I go for a masters, professional masters, or PhD? ](https://www.reddit.com/r/gradadmissions/comments/1foc03f/should_i_go_for_a_masters_professional_masters_or/) , 2024-10-04-0912
```
My goal with graduate school is to set myself up to launch a company that produces a system of swarm robots that coopera
te to efficiently assemble orbital infrastructure; I believe the space industry is in the process of taking off and such
 a system will be necessary to scale it.

  
In my undergrad, I worked on 4 major research projects.

* One on efficient
 open set multimodal 3d mapping; under review at NeurIPS MAR workshop
* One on improving the performance of reinforcemen
t learning for knowledge graph query answering; accepted to IEEE TASL journal and resulted in a patent
* One on creating
 a universal testing platform for cooperative autonomous driving; accepted to VTC 2024 conference
* One on using evoluti
onary computation to improve the performance of a neurosymbolic planning architecture with the goal of creating a natura
l language iterface for a symbolic planning system; worked on this at CMU over the summer but am still collecting result
s. Likely to submit to ICRA or IROS down the road

and one major robotics project that was just for fun; I built an auto
nomous drone that can navigate to GPS coordinates while avoiding obstacles with a depth camera. I also have a startup wh
ere we're building models to translate natural language into formatted API calls in under a second, but with all the res
earch work we've been in the beta phase for a while (though we are eyeing an aquihire from an interested local firm).

 
 
I know my future company will be a deep tech company and be heavily research-oriented in its inception, but since it i
s still a company I know I'll need more business knowhow to make it successful. I've heard that MBAs teach people how to
 be effective managers at large businesses and from my own experience I know a very different skillset is required for s
tartups, so I'm left deciding between a dual research-based MS/PhD and MBA OR pursuing a professional masters focused on
 entrepreneurship (see CMU's MSAII or MRSD programs) and getting out into the market faster. CMU, MIT, and Stanford alum
s in particular, what do you think best aligns with my goals? Thank you for any feedback you can offer!
```
---

     
 
all -  [ Post-Doc Position in Intersection of LLMs/Reasoning/Data at Stanford Scaling Intelligence Lab ](https://www.reddit.com/r/CompSocial/comments/1fnnziy/postdoc_position_in_intersection_of/) , 2024-10-04-0912
```
Azalia Mirhoseini (CS) and Amin Saberi (Math) are jointly seeking a Post-Doc to join the [Scaling Intelligence Lab](http
s://scalingintelligence.stanford.edu/pubs/) at Stanford, which focuses on the development of 'scalable and self-improvin
g AI systems and methodologies towards the goal of AGI.' 

The post-doc researcher would work with both professors to co
ntribute to cutting-edge research at the intersection of language models, data, and reasoning. From the call:

>The post
doc will be expected to help define the research questions of interest, and lead both empirical and methodological resea
rch efforts towards publication, working together with student collaborators. Teaching is not required as part of this p
osition.

>Required Qualifications: 

>\* Strong mathematical background, including expertise in one or more of the foll
owing areas: machine learning, statistics, and algorithms.

>\* Ph.D. (or expected completion by Fall 2024) in computer 
science, statistics, operations research, or related fields

>\* Prior experience working with data, including expertise
 with computational methods 

>\* Prior experience building ML systems, designing and running experiments in PyTorch or 
JAX

>\* Strong publication record in top machine learning conferences (e.g. NeurIPS, ICML, ICLR). A strong background i
n theory is a plus.   

To learn more about the role and how to apply, visit: [https://docs.google.com/document/d/1SBfvF
hLF4hSseTBybXRKJeRFMxqw4ahQ9f4Cf5Vbl7I/edit](https://docs.google.com/document/d/1SBfvFhLF4hSseTBybXRKJeRFMxqw4ahQ9f4Cf5V
bl7I/edit)
```
---

     
 
all -  [ Looking at quant jobs from unconventional path ](https://www.reddit.com/r/FinancialCareers/comments/1fnefe2/looking_at_quant_jobs_from_unconventional_path/) , 2024-10-04-0912
```
Hi folks!

I am very new to quant/fintech so please forgive me for my naivety and all the mistakes I make. I was doing a
n MBBS (equivalent to a US MD) from India at one of the top med schools in the country and was so done with the people a
nd culture that I dropped out recently and started a degree in Data Science at another top university in India (although
 my program is not considered competitive at all, I couldn't go via normal route because it usually takes years of prepa
ration \~6-7 years to get into the traditional program). For now, I have \~4/4 gpa.

I have been doing a lot of neurosci
ence and have several publications concerning clinical data analyses (2), experimental neuroscience (1), one on dimensio
nality reduction algo, submitting to neurips workshops this year (3), on a topic based on physics and neuroscience prese
nting to neuroscience conference, math neuro conferences, a few other research experiences using neuroscience datasets, 
etc. This year I am also joining a lab in Germany for research. I was previously a SURF at Caltech. And the list goes on
 in the direction that to me seems very tangential to quant jobs.

For as long as I can remember I have been in love wit
h neuroscience and machine learning and now I have begun to look towards more quantitative and complex ideas above neuro
science and my first thought is either research in quantum computing (QML) or quant research jobs.

I am probably being 
super crazy thinking of even doing this, but I was wondering whether I have any chance of getting an interview at let's 
say, the Jane Street internship program, next year while I focus more on getting research in ML/math this year. Or shoul
d I do something else with my life?

Thanks for all the insight!
```
---

     
 
all -  [ Summaries Of Research Papers We Read ](https://www.reddit.com/r/deeplearning/comments/1fl4bzm/summaries_of_research_papers_we_read/) , 2024-10-04-0912
```
The Vision Language Group at IIT Roorkee has curated a repository of comprehensive summaries for deep learning research 
papers from top-tier conferences like NeurIPS, CVPR, ICCV, ICML from 2016 to 2024. These summaries aim to provide a conc
ise understanding of influential papers in fields such as computer vision, natural language processing, and machine lear
ning. The collection is constantly growing, with new summaries added frequently. Here are a few notable examples:

- **D
reamBooth: Fine Tuning Text-to-Image Diffusion Models for Subject-Driven Generation**, CVPR'23  
  [DreamBooth Summary](
https://github.com/vlgiitr/papers_we_read/blob/master/summaries/DreamBooth.md)

- **Segment Anything**, ICCV'23  
  [Seg
ment Anything Summary](https://github.com/vlgiitr/papers_we_read/blob/master/summaries/Segment_Anything.md)

- **An Imag
e is Worth One Word: Personalizing Text-to-Image Generation using Textual Inversion**, ICCV'23  
  [Textual Inversion Su
mmary](https://github.com/vlgiitr/papers_we_read/blob/master/summaries/Textual_inversion.md)

- **Photorealistic Text-to
-Image Diffusion Models with Deep Language Understanding**, NIPS'22  
  [Photorealistic Diffusion Summary](https://githu
b.com/vlgiitr/papers_we_read/blob/master/summaries/imagen.md)

- **An Image is Worth 16x16 Words: Transformers for Image
 Recognition at Scale**, ICLR'21  
  [Vision Transformer Summary](https://github.com/vlgiitr/papers_we_read/blob/master/
summaries/Vision_Transformer.md)

- **Big Bird: Transformers for Longer Sequences**, NIPS'20  
  [Big Bird Transformers 
Summary](https://github.com/vlgiitr/papers_we_read/blob/master/summaries/Big_Bird_Transformers.md)

The repository invit
es contributions from the community. If you find the summaries helpful, you are encouraged to submit your own summaries 
for research papers. The team aims to regularly update the collection with summaries of papers from upcoming conferences
 and key topics in deep learning and AI. 

You can access the full repository and contribute here:  
[Vision Language Gr
oup Paper Summaries](https://github.com/vlgiitr/papers_we_read)

By contributing, you'll help make advanced research mor
e accessible to both beginners and experts in the field.
```
---

     
 
all -  [ [R] Some Research Papers We Read ](https://www.reddit.com/r/MachineLearning/comments/1fl4bi0/r_some_research_papers_we_read/) , 2024-10-04-0912
```
The Vision Language Group at IIT Roorkee has curated a repository of comprehensive summaries for deep learning research 
papers from top-tier conferences like NeurIPS, CVPR, ICCV, ICML from 2016 to 2024. These summaries aim to provide a conc
ise understanding of influential papers in fields such as computer vision, natural language processing, and machine lear
ning. The collection is constantly growing, with new summaries added frequently. Here are a few notable examples:



- \
*\*DreamBooth: Fine Tuning Text-to-Image Diffusion Models for Subject-Driven Generation\*\*, CVPR'23  

  \[DreamBooth S
ummary\](https://github.com/vlgiitr/papers\_we\_read/blob/master/summaries/DreamBooth.md)



- \*\*Segment Anything\*\*,
 ICCV'23  

  \[Segment Anything Summary\](https://github.com/vlgiitr/papers\_we\_read/blob/master/summaries/Segment\_An
ything.md)



- \*\*An Image is Worth One Word: Personalizing Text-to-Image Generation using Textual Inversion\*\*, ICCV
'23  

  \[Textual Inversion Summary\](https://github.com/vlgiitr/papers\_we\_read/blob/master/summaries/Textual\_invers
ion.md)



- \*\*Photorealistic Text-to-Image Diffusion Models with Deep Language Understanding\*\*, NIPS'22  

  \[Phot
orealistic Diffusion Summary\](https://github.com/vlgiitr/papers\_we\_read/blob/master/summaries/imagen.md)



- \*\*An 
Image is Worth 16x16 Words: Transformers for Image Recognition at Scale\*\*, ICLR'21  

  \[Vision Transformer Summary\]
(https://github.com/vlgiitr/papers\_we\_read/blob/master/summaries/Vision\_Transformer.md)



- \*\*Big Bird: Transforme
rs for Longer Sequences\*\*, NIPS'20  

  \[Big Bird Transformers Summary\](https://github.com/vlgiitr/papers\_we\_read/
blob/master/summaries/Big\_Bird\_Transformers.md)



The repository invites contributions from the community. If you fin
d the summaries helpful, you are encouraged to submit your own summaries for research papers. The team aims to regularly
 update the collection with summaries of papers from upcoming conferences and key topics in deep learning and AI. 



Yo
u can access the full repository and contribute here:  

\[Vision Language Group Paper Summaries\](https://github.com/vl
giitr/papers\_we\_read)



By contributing, you'll help make advanced research more accessible to both beginners and exp
erts in the field.
```
---

     
 
all -  [ Summaries of some Research Papers we read! ](https://www.reddit.com/r/neuralnetworks/comments/1fl4al2/summaries_of_some_research_papers_we_read/) , 2024-10-04-0912
```
The Vision Language Group at IIT Roorkee has curated a repository of comprehensive summaries for deep learning research 
papers from top-tier conferences like NeurIPS, CVPR, ICCV, ICML from 2016 to 2024. These summaries aim to provide a conc
ise understanding of influential papers in fields such as computer vision, natural language processing, and machine lear
ning. The collection is constantly growing, with new summaries added frequently. Here are a few notable examples:

* **D
reamBooth: Fine Tuning Text-to-Image Diffusion Models for Subject-Driven Generation**, CVPR'23 [DreamBooth Summary](http
s://github.com/vlgiitr/papers_we_read/blob/master/summaries/DreamBooth.md)
* **Segment Anything**, ICCV'23 [Segment Anyt
hing Summary](https://github.com/vlgiitr/papers_we_read/blob/master/summaries/Segment_Anything.md)
* **An Image is Worth
 One Word: Personalizing Text-to-Image Generation using Textual Inversion**, ICCV'23 [Textual Inversion Summary](https:/
/github.com/vlgiitr/papers_we_read/blob/master/summaries/Textual_inversion.md)
* **Photorealistic Text-to-Image Diffusio
n Models with Deep Language Understanding**, NIPS'22 [Photorealistic Diffusion Summary](https://github.com/vlgiitr/paper
s_we_read/blob/master/summaries/imagen.md)
* **An Image is Worth 16x16 Words: Transformers for Image Recognition at Scal
e**, ICLR'21 [Vision Transformer Summary](https://github.com/vlgiitr/papers_we_read/blob/master/summaries/Vision_Transfo
rmer.md)
* **Big Bird: Transformers for Longer Sequences**, NIPS'20 [Big Bird Transformers Summary](https://github.com/v
lgiitr/papers_we_read/blob/master/summaries/Big_Bird_Transformers.md)

The repository invites contributions from the com
munity. If you find the summaries helpful, you are encouraged to submit your own summaries for research papers. The team
 aims to regularly update the collection with summaries of papers from upcoming conferences and key topics in deep learn
ing and AI.

You can access the full repository and contribute here:  
[Vision Language Group Paper Summaries](https://g
ithub.com/vlgiitr/papers_we_read)

By contributing, you'll help make advanced research more accessible to both beginners
 and experts in the field.
```
---

     
 
all -  [ Comprehensive Summaries of Paper We Read ](https://www.reddit.com/r/u_vlg_iitr/comments/1fl48qg/comprehensive_summaries_of_paper_we_read/) , 2024-10-04-0912
```
**The Vision Language Group at IIT Roorkee** has put together an awesome repository of **comprehensive summaries** for d
eep learning papers from top conferences like **NeurIPS, CVPR, ICCV, ICML (2016-2024)**. These summaries break down key 
papers in computer vision, NLP, and machine learning—perfect if you want to stay updated without diving deep into the fu
ll papers. Here are a few highlights:

* **DreamBooth: Fine Tuning Text-to-Image Diffusion Models for Subject-Driven Gen
eration**, CVPR'23 👉 [Summary](https://github.com/vlgiitr/papers_we_read/blob/master/summaries/DreamBooth.md)
* **Segmen
t Anything**, ICCV'23 👉 [Summary](https://github.com/vlgiitr/papers_we_read/blob/master/summaries/Segment_Anything.md)
*
 **An Image is Worth One Word: Personalizing Text-to-Image Generation using Textual Inversion**, ICCV'23 👉 [Summary](htt
ps://github.com/vlgiitr/papers_we_read/blob/master/summaries/Textual_inversion.md)
* **Photorealistic Text-to-Image Diff
usion Models with Deep Language Understanding**, NIPS'22 👉 [Summary](https://github.com/vlgiitr/papers_we_read/blob/mast
er/summaries/imagen.md)
* **An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale**, ICLR'21 👉 [Sum
mary](https://github.com/vlgiitr/papers_we_read/blob/master/summaries/Vision_Transformer.md)
* **Big Bird: Transformers 
for Longer Sequences**, NIPS'20 👉 [Summary](https://github.com/vlgiitr/papers_we_read/blob/master/summaries/Big_Bird_Tra
nsformers.md)

If you find these summaries useful, feel free to contribute your own! The repo is constantly being update
d with new papers from major conferences, so it's a great way to keep up with the latest in AI and deep learning.

📂 **C
heck out the full repo and contribute here**  
[Vision Language Group Paper Summaries](https://github.com/vlgiitr/papers
_we_read)

Happy reading! 🎉
```
---

     
 
all -  [ [R] Erasing the Invisible: A Stress-Test Challenge for Image Watermarks (NeurIPS 2024 Competition) ](https://www.reddit.com/r/MachineLearning/comments/1fk90gj/r_erasing_the_invisible_a_stresstest_challenge/) , 2024-10-04-0912
```
We're excited to announce the NeurIPS competition '**Erasing the Invisible: A Stress-Test Challenge for Image Watermarks
**' running from **September 16 to November 5**. This is your chance to test your skills in a cutting-edge domain and wi
n a share of our $6000 prize pool!

# Competition Overview

This competition is divided into **two tracks: Black Box Tra
ck and Beige Box Track**. It aims to validate the robustness of image watermarks under varying visibility conditions and
 attacker knowledge. Competitors will attempt to remove invisible watermarks while maintaining the quality of the images
. Evaluations will be based on two criteria: the effectiveness of watermark removal and the preservation of image qualit
y.

# 🔗 Important Dates:

▶️ **Submission phase:** Sep 16 - Nov 5  
▶️ **Registration and submissions close:** Nov 5  
▶
️ **Winning team announcement:** Nov 20

# 🌐 More Info & Registration:

▶️ **Website:** [http://erasinginvisible.github.
io](http://erasinginvisible.github.io/)  
▶️ **Hosted on Codabench:**  
⏩ **Beige-Box Track:** [codabench.org/competitio
ns/3821](https://codabench.org/competitions/3821/)  
⏩ **Black-Box Track:** [codabench.org/competitions/3857](https://co
dabench.org/competitions/3857/)

# 💡 Why Participate?

* **Test your skills** in a real-world, cutting-edge domain.
* **
Validate watermark robustness** under various conditions.
* **Collaborate** with a global community of researchers and p
ractitioners.
* **Earn your share of $6000** (and counting as more sponsors join)!

# 💰 Prize Pool: $6000 (and growing!)


Want to **sponsor** the competition? Reach out to us at:  
📧 [erasinginvisible@googlegroups.com](mailto:erasinginvisib
le@googlegroups.com) or [furongh@umd.edu](mailto:furongh@umd.edu)
```
---

     
 
all -  [ How to get into CS/AI related research and get a paper published in a top international publication  ](https://www.reddit.com/r/Indian_Academia/comments/1fjy5bt/how_to_get_into_csai_related_research_and_get_a/) , 2024-10-04-0912
```
Qualifications: B. Tech. CSE (Tier-3 private college)   
YOE: 1  
Summary: I want to know how I can contribute to resear
ch and get papers published in the top international publications like ICML, NeurIPS, ICCV, CVPR etc. My fundamentals in
 subjects like Deep Learning and Computer Vision are quite strong, and I was wondering how I can get into research, and 
what the process looks like. I am guessing I need to talk to professors at some of the top institutes like IIITs/IITs? H
ow do I start, I'd really appreciate some feedback regarding this.
```
---

     
 
all -  [ [Call for papers] Safe Generative AI Workshop at NeurIPS 2024 ](https://groups.google.com/g/ml-news/c/URCyANyWxGA) , 2024-10-04-0912
```

```
---

     
 
all -  [ [R] submitting to neurips and coling at the same time ](https://www.reddit.com/r/MachineLearning/comments/1fiivv5/r_submitting_to_neurips_and_coling_at_the_same/) , 2024-10-04-0912
```
Would I be able to submit to both neurips solar and coling 2025? Coling’s policy is no journals or conferences but solar
 is a workshop and it allows dual submission.
```
---

     
 
all -  [ Navigating UCSD as a freshman ](https://www.reddit.com/r/u_TrainingResolution12/comments/1fg4ars/navigating_ucsd_as_a_freshman/) , 2024-10-04-0912
```
Hey. It is the time of the year where everyone's excited for our upcoming session. Welcome to UCSD and I hope you are do
ing great. As a senior, I have been exposed to various handy tools to navigate college life. Here are my recommendations


1. **Networking system**- **Discord, Slack, Instagram webpage** for the **clubs and classes** you are interested in. *
*Piazza** good for reference to asking questions to the instructional team+class. **Cold email and Office hours** have w
orked well in finding research jobs. **Linkedin** is great for having your online profile up top, highly recommend a pro
fessional photograph. **X/Twitter** for following your latest research if you're into EE/AI/related fields. **Geisel, Cl
asses, Intramural Sports and Greek Rush** are experiences that got me some good exposure to social aspects of campus (no
t in a frat but made friends). For jobs **Handshake and Linkedin** is enough if you have a good portfolio going on. Look
 at accepted alumnis portfolio based on your goals and see what jobs fit your traits best. **Resident life events** too 
are lit. Become a IA/SI leader. You'll have fun lol.
2. **Offerup and Facebook Marketplace** are great for furniture and
 rentals. If you're a business nerd like me, you could also practice your negotiation skills there without anything at s
take (LOL!). Other good things I found were **Styl App** and **Poshmark + thrift stores and stockx** if you're looking t
o up your fashion game.
3. **Notetaking**/**Information management-** A HIGHLY debated topic amongst students because pe
n and paper models are outdated. I used **Apple Notes** combined with P**erplexity/Claude/GPT-4** for notetaking. The wo
rkflow I follow is **lecture notes (typed or handwritten + screenshot)-> pdf textbook into perplexity/GPT and prompt to 
follow textbook-> get key concepts and insights per lesson-> work on problems and use LLMs to see how and where each min
i concept applies-> understand doubtful concepts in office hours and mail TAs/post on piazza-> reflect and add summary t
o notes-> hold group study sessions to debate tougher questions and teach what you mastered to other students.**

The wh
ole process takes about 1 hour a day to 2 max per subject- benchmark-> math 142a. Perplexity is useful for getting searc
h and images/videos directly from your notes and interacting with content on a deeper level, GPT is great for summary an
d analysis. I strongly believe we should interface LLMs with learning and conventional instruction. Never rely on LLMs f
or answers. Never cheat. libgen, **JSTOR, arXiv, nature science journal, neurIPS, internet archive** are some excellent 
sources for articles. Geisel has some articles too that can be access with campus **VPNs.** My GPA went from a 3.2 to 4.
0 with straight As thanks to this note taking system. It is like my second brain. I also met a few cool people this way,
 we learnt a lot together.

4. **Hangouts**- The most subjective thing by far. Not a local. I intern full time rn so I b
arely have time. The one activity i did choose was fitness and beaches because I can't keep up with studies otherwise. I
 go to 24 fitness or main gym. Ice rink close by or the mt soledad drive is a cool date idea for reference. Cool tidepoo
ls nearby at LJ shores you can search instagram reels idk i randomly stumbled. There's some good cafes all around town g
o on yelp. Surf spots are windansea and couple others. Convoy easily on top for asian food. Crazy bakeries and sweet sho
ps all around little italy. Hillcrest welfare wednesdays you can do cool stuff. Indian food is good mira mesa side. Mexi
can at Old town and near TJ. SDSU side has lit parties if you want go make friends there and get invited. PB amazing for
 food and party. Downtown has great museums. Seaworld and zoo, sd science center amazing. La Jolla Playhouse is cool. Ch
e cafe is awesome. Gaslamp gastropubs go hard. SD padres games great hangouts you will make lots of friends. MMA PPV eve
nts too. Weekend getaway for non locals they have a secret place at OB which I know lot of you will try goofy stuff. Rem
ember if it takes a toll on your body and affects mental health then it is not worth it.

Ah thank god for speech to tex
t. Have fun. Went through 4 years and a lot of memories.
```
---

     
 
all -  [ [D] Updated Paper submission [NeurIPS 2024 Workshop] ](https://www.reddit.com/r/MachineLearning/comments/1fex05d/d_updated_paper_submission_neurips_2024_workshop/) , 2024-10-04-0912
```
Hey, everyone.  
Sorry for asking a noob question.  
So basically we have submitted a paper at a workshop of NeurIPS 202
4. This is our first work during our undergrad. After submission, we received an email the next day regarding a margin i
ssue that needed to be fixed, or our submission would be rejected. Which we fixed \[a very unintentional error\] and try
ing to submit it since then  but in the Openreview, it keeps saying that the invitation submission has expired. So is th
ere any deadline we have to maintain for this kind of scenario. The main review will be given in the next month. We have
 tried to contact them, but we are not getting any response.
```
---

     
 
all -  [ [D] Cold Diffusion: Inverting Arbitrary Image Transforms Without Noise ](https://www.reddit.com/r/MachineLearning/comments/1fec2jq/d_cold_diffusion_inverting_arbitrary_image/) , 2024-10-04-0912
```
Hi everyone, 

The point of this post is not to blame the authors, I'm just very surprised by the review process.

I jus
t stumbled upon this paper. While I find the ideas somewhat interesting, I found the overall results and justifications 
to be very weak.   
It was a clear reject from ICLR2022, mainly for a lack of any theoretical justifications. [https://o
penreview.net/forum?id=slHNW9yRie0](https://openreview.net/forum?id=slHNW9yRie0)  
The exact same paper is resubmitted a
t NeurIPS2023 and I kid you not, the thing is accepted for a poster. [https://openreview.net/forum?id=XH3ArccntI](https:
//openreview.net/forum?id=XH3ArccntI)

I don't really get how it could have made it through the review process of NeurIP
S. The whole thing is very preliminary and is basically just consisting of experiments.  
It even llack citations of oth
er very closely related work such as *Generative Modelling With Inverse Heat Dissipation* [https://arxiv.org/abs/2206.13
397](https://arxiv.org/abs/2206.13397) which is basically their 'blurring diffusion' but with theoretical background and
 better results (which was accepted to ICLR2023)...

I thought NeurIPS was on the same level as ICLR, but now it seems t
o me sometimes papers just get randomly accepted.

So I was wondering, if anyone had an opinion on this, or if you have 
encountered other similar cases ? 
```
---

     
 
all -  [ Derivation of the upper bound of the average regret of online-to-batch conversion in H-smoothness ](https://www.reddit.com/r/mathematics/comments/1fbn724/derivation_of_the_upper_bound_of_the_average/) , 2024-10-04-0912
```
I've been studying a \[paper\]\[1\] (Smoothness, Low-Noise and Fast Rates) on the impact of smoothness on the convergenc
e rate of online-to-batch conversion, specifically Theorem 2, which provides a bound on the average regret in the contex
t of online convex optimization. The paper claims that this theorem can be proved using Lemma 3.1 in the original paper 
and Theorem 1 from \[this thesis\]\[2\] (Online Learning: Theory, Algorithms, and Applications). However, I'm struggling
 to see the connection between these results. Could someone help clarify how Lemma 3.1 and Theorem 1 from the thesis are
 used to prove Theorem 2 in the paper?

\*\*Lemma 3.1:\*\* For an $H$-smooth non-negative function $f : W \\rightarrow \
\mathbb{R}$, for all $w \\in W$:

$$

\\|\\nabla f(w)\\|\^\* \\leq \\sqrt{4H f(w)}

$$

\*\*Theorem 1:\*\* Under the sam
e conditions as Lemma 1. Assume that a constant $L$ exists such that for all $t$, the function $f\_t$ is $L$-self-bounde
d for the norm $\\|\\cdot\\|$. Let $U\_1$ and $U\_2$ be two positive scalars and set $c = L + \\sqrt{L\^2 + \\frac{LU\_2
}{U\_1}}$. Then, for any $u \\in S$ that satisfies $f(u) \\leq U\_1$ and $\\sum\_{t=1}\^{T} g\_t(u) \\leq U\_2$, we have
,

$$

R(u, T) = \\sum\_{t=1}\^{T} g\_t(w\_t) - \\sum\_{t=1}\^{T} g\_t(u) \\leq 2\\sqrt{LU\_1U\_2} + 4LU\_1.

$$

\*\*Th
eorem 2:\*\* For any $B \\in \\mathbb{R}$ and $\\overline{L\^\*}$, if we use stepsize

$$

\\eta = \\frac{1}{H B\^2 + \\
sqrt{H\^2 B\^4 + H B\^2 n \\overline{L\^\*}}}

$$

for the Mirror Descent algorithm, then for any instance sequence

$z\
_1, \\ldots, z\_n \\in \\mathcal{Z}$, the average regret w.r.t. any

$w\^\* \\in W$ such that $F(w\^\*) \\leq B\^2$ and 
$\\frac{1}{n} \\sum\_{j=1}\^{n} \\ell(w\^\*, z\_j) \\leq \\overline{L\^\*}$

is bounded by:

$$

\\frac{1}{n} \\sum\_{i=
1}\^{n} \\ell(w\_i, z\_i) - \\frac{1}{n} \\sum\_{i=1}\^{n} \\ell(w\^\*, z\_i) \\leq \\frac{4H B\^2}{n} + \\frac{2 \\sqrt
{H B\^2 \\overline{L\^\*}}}{n}

$$

I found the proof of Theorem 1 a bit confusing as well, particularly because it does
n't clearly explain the relationship between $U\_1, U\_2$, and $c$ in that specific manner.

\[1\]: [https://proceedings
.neurips.cc/paper/2010/file/76cf99d3614e23eabab16fb27e944bf9-Paper.pdf](https://proceedings.neurips.cc/paper/2010/file/7
6cf99d3614e23eabab16fb27e944bf9-Paper.pdf)

\[2\]: [https://home.ttic.edu/\~shai/papers/ShalevThesis07.pdf](https://home
.ttic.edu/~shai/papers/ShalevThesis07.pdf)

For the original post, check [convex optimization - Derivation of the upper 
bound of the average regret of online-to-batch conversion in H-smoothness - Mathematics Stack Exchange](https://math.sta
ckexchange.com/questions/4966362/derivation-of-the-upper-bound-of-the-average-regret-of-online-to-batch-conversio)
```
---

     
 
all -  [ How on earth do you get research published as a undergraduate? ](https://www.reddit.com/r/learnmachinelearning/comments/1f96iax/how_on_earth_do_you_get_research_published_as_a/) , 2024-10-04-0912
```
I'm an incoming Math+CS freshman at a decent research uni and I've been looking at some labs at my school. I've been loo
king at the profiles of students accepted to top ml grad schools and a lot of them, on top of having near-perfect GPAs, 
also have co-authored many papers, some of which in NeurIPS, ICLR, and ICML. 

The work that most labs do at my uni is e
ither interdisciplinary ML, (mostly medicine/biomed + ML), or theory-based ML work. The latter is more suited for my maj
or, but after reading through these labs' publications, I cannot even envision how I would meaningfully contribute to th
ese labs, let alone in the next 4 years. 

Does it always feel this daunting, and is their anything I can do to increase
 my chances of getting publications?

  

```
---

     
