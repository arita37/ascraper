 
all -  [ Faith and Fate: Limits of Transformers on Compositionality [R] ](https://www.reddit.com/r/MachineLearning/comments/1amzb52/faith_and_fate_limits_of_transformers_on/) , 2024-02-11-0911
```
Edit: Kevin Murphy,  Francois Chollet, Vitaly Kurin and others recommended this paper (some very highly)

https://arxiv.
org/abs/2305.18654 (Presented at NeurIPS in December)

**Abstract:**

Transformer large language models (LLMs) have spar
ked admiration for their exceptional performance on tasks that demand intricate multi-step reasoning. Yet, these models 
simultaneously show failures on surprisingly trivial problems. This begs the question: Are these errors incidental, or d
o they signal more substantial limitations? In an attempt to demystify transformer LLMs, we investigate the limits of th
ese models across three representative compositional tasks -- multi-digit multiplication, logic grid puzzles, and a clas
sic dynamic programming problem. These tasks require breaking problems down into sub-steps and synthesizing these steps 
into a precise answer. We formulate compositional tasks as computation graphs to systematically quantify the level of co
mplexity, and break down reasoning steps into intermediate sub-procedures. Our empirical findings suggest that transform
er LLMs solve compositional tasks by reducing multi-step compositional reasoning into linearized subgraph matching, with
out necessarily developing systematic problem-solving skills. To round off our empirical study, we provide theoretical a
rguments on abstract multi-step reasoning problems that highlight how autoregressive generations' performance can rapidl
y decay with increased task complexity.

---

Kevin Murphy's summary: 'I like this paper. They prove that transformers a
re guaranteed to suffer from compounding errors when doing long reasoning chains (as @ylecun has argued), and much appar
ent 'success' is just due to unreliable pattern matching / shortcut learning.'
```
---

     
 
all -  [ [D] concerns about the series of works in reflexion(self-adjustment)-powered LLM agent ](https://www.reddit.com/r/MachineLearning/comments/1am3ior/d_concerns_about_the_series_of_works_in/) , 2024-02-11-0911
```
we see tons of works in LLM-based agent which can perform tasks on web applications such as webshop, [webarena](https://
github.com/web-arena-x/webarena),  [agentbench](https://github.com/THUDM/AgentBench/tree/main)etc...

also, we can find 
following works on reflexion-based agent which intakes the feedbacks and errors from previous trials from the interactio
ns with the environment. the typical work is  `Reflexion: Language Agents with Verbal Reinforcement Learning`

within ea
ch trial, the agent, or say, llm, digests the prompt which contains not only history from current trial but also the sys
tem info or feedbacks or error messages from previous trials. The feedbacks could come from system setting or from anoth
er more powerful LLM that can act as a super judge to give feedbacks.

anyway, I do not think this is RL since there is 
no learning process for the agent, but a concat of prompt.

My primary concern is that is this label leakage ? The agent
 get feedbacks from the environment and with more trials, of course, the agent should have a more clear approach to the 
final answer. So what is the point ?

I see a post which shares my same concern:  [noahshinn/reflexion: \[NeurIPS 2023\]
 Reflexion: Language Agents with Verbal Reinforcement Learning (github.com)](https://github.com/noahshinn/reflexion/issu
es/27)

&#x200B;

Would like to hear from you in view of academic and industry.

&#x200B;

&#x200B;

&#x200B;

&#x200B;
```
---

     
 
all -  [ [R] Long Is More for Alignment: A Simple but Tough-to-Beat Baseline for Instruction Fine-Tuning ](https://www.reddit.com/r/MachineLearning/comments/1am1v5f/r_long_is_more_for_alignment_a_simple_but/) , 2024-02-11-0911
```
**Title**: Long Is More for Alignment: A Simple but Tough-to-Beat Baseline for Instruction Fine-Tuning

**Paper**: [http
s://arxiv.org/abs/2402.04833](https://arxiv.org/abs/2402.04833)

**Abstract**: There is a consensus that instruction fin
e-tuning of LLMs requires high-quality data, but what are they? LIMA (NeurIPS 2023) and AlpaGasus (ICLR 2024) are state-
of-the-art methods for selecting such high-quality examples, either via manual curation or using GPT-3.5-Turbo as a qual
ity scorer. We show that the extremely simple baseline of selecting the 1,000 instructions with longest responses from s
tandard datasets can consistently outperform these sophisticated methods according to GPT-4 and PaLM-2 as judges, while 
remaining competitive on the OpenLLM benchmarks that test factual knowledge. We demonstrate this for several state-of-th
e-art LLMs (Llama-2-7B, Llama-2-13B, and Mistral-7B) and datasets (Alpaca-52k and Evol-Instruct-70k). In addition, a lig
htweight refinement of such long instructions can further improve the abilities of the fine-tuned LLMs, and allows us to
 obtain the 2nd highest-ranked Llama-2-7B-based model on AlpacaEval 2.0 while training on only 1,000 examples and no ext
ra preference data. We also conduct a thorough analysis of our models to ensure that their enhanced performance is not s
imply due to GPT-4's preference for longer responses, thus ruling out any artificial improvement. In conclusion, our fin
dings suggest that fine-tuning on the longest instructions should be the default baseline for any research on instructio
n fine-tuning.
```
---

     
 
all -  [ [R] Persistent homology and topological data analysis helped robust detection of AI-generated texts ](https://www.reddit.com/r/MachineLearning/comments/1aky8xt/r_persistent_homology_and_topological_data/) , 2024-02-11-0911
```
The main idea is that text data can be presented as points in some high-dimensional space. It can be assumed that the da
taset fits into some surface in it. The problem is that such a surface may have fractal characteristics, so complex math
ematics is required.

The authors of a new study have developed a method for determining the fractal dimension of such a
 surface (researchers called it the internal dimension), which is based on the concept of persistent homologies. Briefly
, the main thing is that this dimension differs for human and machine texts with a high degree of reliability, which can
 be used in practice. 

&#x200B;

[ ](https://preview.redd.it/8r71lx9jh4hc1.png?width=1091&format=png&auto=webp&s=3077d2
1099e4c86a881ab297f22467f338e3c593)

*Real and artificial texts have different intrinsic dimension*

It is noteworthy th
at the internal dimensions are different for texts in different languages - from 7 ± 1 for Chinese to 10 ± 1 for Italian
 - but reliable discrimination is achieved in all of them.

The code and data are available on [GitHub](https://github.c
om/ArGintum/GPTID), and details of the study can be found in the [article](https://openreview.net/forum?id=8uOZ0kNji6) p
ublished in the proceedings of the NeurIPS 2023 conference.
```
---

     
 
all -  [ IS THIS A GOOD ROADMAP TO LEARN PYTHON? ](https://www.reddit.com/r/learnpython/comments/1ak8v9p/is_this_a_good_roadmap_to_learn_python/) , 2024-02-11-0911
```
. Python Basics:  
Resources:  
'Python Crash Course' by Eric Matthes  
'Automate the Boring Stuff with Python' by Al
 Sweigart  
Codecademy's Python course  
2. Mathematics for Machine Learning:  
Linear Algebra, Calculus, Probability
 & Statistics  
Resources:  
'Linear Algebra Done Right' by Sheldon Axler  
'Introduction to Probability' by Joseph K
. Blitzstein and Jessica Hwang  
'Deep Learning' by Ian Goodfellow, Yoshua Bengio, and Aaron Courville (for deeper unde
rstanding)  
3. Machine Learning Fundamentals:  
Understand supervised and unsupervised learning algorithms, model eva
luation, and cross-validation.  
Resources:  
'Introduction to Machine Learning with Python' by Andreas C. Müller & Sa
rah Guido  
Andrew Ng's Machine Learning course on Coursera  
4. Deep Learning:  
Learn neural networks, deep learnin
g architectures, and frameworks like TensorFlow and PyTorch.  
Resources:  
'Deep Learning' by Ian Goodfellow, Yoshua 
Bengio, and Aaron Courville  
Fast.ai's Practical Deep Learning for Coders course  
'Hands-On Machine Learning with Sc
ikit-Learn, Keras, and TensorFlow' by Aurélien Géron  
5. Natural Language Processing (NLP):  
Study text processing, 
sentiment analysis, named entity recognition, and language modeling.  
Resources:  
Natural Language Processing Specia
lization on Coursera by Deeplearning.ai  
'Natural Language Processing with Python' by Steven Bird, Ewan Klein, and Edw
ard Loper  
6. Computer Vision:  
Explore image processing, object detection, and convolutional neural networks (CNNs)
.  
Resources:  
'Computer Vision: Algorithms and Applications' by Richard Szeliski  
Convolutional Neural Networks S
pecialization on Coursera by Deeplearning.ai  
7. Reinforcement Learning:  
Learn about Markov Decision Processes, Q-l
earning, and policy gradients.  
Resources:  
'Reinforcement Learning: An Introduction' by Richard S. Sutton and Andre
w G. Barto  
Reinforcement Learning Specialization on Coursera by Deeplearning.ai  
8. Projects and Hands-On Practice:
  
Apply your knowledge through projects on platforms like Kaggle or building your own projects.  
Resources:  
Kaggl
e competitions and datasets  
GitHub repositories for inspiration and collaboration  
9. Stay Updated and Networking:
  
Follow research papers, attend conferences, and participate in online forums and communities.  
Resources:  
Arxiv.
org for research papers  
Conferences like NeurIPS, ICML  
Reddit communities (r/MachineLearning, r/learnmachinelearni
ng)  
LinkedIn groups  
10. Advanced Topics:  
Delve into specialized areas like GANs, recommendation systems, time s
eries analysis, etc.  
Resources:  
Books, research papers, and specialized courses on platforms like Coursera, Udacit
y, and edX.
```
---

     
 
all -  [ IS THIS A GOOD ROADMAP FOR MASCHINE LEARNING? ](https://www.reddit.com/r/learnmachinelearning/comments/1ak8qxi/is_this_a_good_roadmap_for_maschine_learning/) , 2024-02-11-0911
```
 

### . Python Basics:

* **Resources:**
   * 'Python Crash Course' by Eric Matthes
   * 'Automate the Boring Stuff wit
h Python' by Al Sweigart
   * Codecademy's Python course

### 2. Mathematics for Machine Learning:

* Linear Algebra, Ca
lculus, Probability & Statistics
* **Resources:**
   * 'Linear Algebra Done Right' by Sheldon Axler
   * 'Introduction t
o Probability' by Joseph K. Blitzstein and Jessica Hwang
   * 'Deep Learning' by Ian Goodfellow, Yoshua Bengio, and Aaro
n Courville (for deeper understanding)

### 3. Machine Learning Fundamentals:

* Understand supervised and unsupervised 
learning algorithms, model evaluation, and cross-validation.
* **Resources:**
   * 'Introduction to Machine Learning wit
h Python' by Andreas C. Müller & Sarah Guido
   * Andrew Ng's Machine Learning course on Coursera

### 4. Deep Learning:


* Learn neural networks, deep learning architectures, and frameworks like TensorFlow and PyTorch.
* **Resources:**
   
* 'Deep Learning' by Ian Goodfellow, Yoshua Bengio, and Aaron Courville
   * Fast.ai's Practical Deep Learning for Coder
s course
   * 'Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow' by Aurélien Géron

### 5. Natural Lan
guage Processing (NLP):

* Study text processing, sentiment analysis, named entity recognition, and language modeling.
*
 **Resources:**
   * Natural Language Processing Specialization on Coursera by Deeplearning.ai
   * 'Natural Language Pr
ocessing with Python' by Steven Bird, Ewan Klein, and Edward Loper

### 6. Computer Vision:

* Explore image processing,
 object detection, and convolutional neural networks (CNNs).
* **Resources:**
   * 'Computer Vision: Algorithms and Appl
ications' by Richard Szeliski
   * Convolutional Neural Networks Specialization on Coursera by Deeplearning.ai

### 7. R
einforcement Learning:

* Learn about Markov Decision Processes, Q-learning, and policy gradients.
* **Resources:**
   *
 'Reinforcement Learning: An Introduction' by Richard S. Sutton and Andrew G. Barto
   * Reinforcement Learning Speciali
zation on Coursera by Deeplearning.ai

### 8. Projects and Hands-On Practice:

* Apply your knowledge through projects o
n platforms like Kaggle or building your own projects.
* **Resources:**
   * Kaggle competitions and datasets
   * GitHu
b repositories for inspiration and collaboration

### 9. Stay Updated and Networking:

* Follow research papers, attend 
conferences, and participate in online forums and communities.
* **Resources:**
   * Arxiv.org for research papers
   * 
Conferences like NeurIPS, ICML
   * Reddit communities (r/MachineLearning, r/learnmachinelearning)
   * LinkedIn groups


### 10. Advanced Topics:

* Delve into specialized areas like GANs, recommendation systems, time series analysis, etc.

* **Resources:**
   * Books, research papers, and specialized courses on platforms like Coursera, Udacity, and edX.
```
---

     
 
all -  [ Cape to Carthage: documentary about an all African, female-led AI research team rising against the o ](https://www.reddit.com/r/MachineLearning/comments/1ajkh13/cape_to_carthage_documentary_about_an_all_african/) , 2024-02-11-0911
```
In the world of AI, Africa has a reputation for being a missing continent. Follow an underdog, female-led, all-African r
esearch team as they compete with tech giants and top universities for a spot at the top international AI research confe
rence NeurIPS in a bid to change history.

Watch the 30 minute documentary [here](https://decisiveagents.com/capetocarth
age/).
```
---

     
 
all -  [ Actor Critic with q-function approximation not converging ](https://www.reddit.com/r/reinforcementlearning/comments/1aj2zey/actor_critic_with_qfunction_approximation_not/) , 2024-02-11-0911
```
Recently I have been trying to implement the actor critic described in this [paper](https://proceedings.neurips.cc/paper
/1999/hash/6449f44a102fde848669bdd9eb6b76fa-Abstract.html).

However, when using the cart pole v1 environment the agent 
learns a little of the behavior but then sorta falls apart. Any ideas about incorrect implementation or alternative crit
ic features would be much appreciated.

I have also been playing with hyperparameters but no combination has worked well
 for me.

[Code](https://drive.google.com/file/d/1CeZgjkrJH5biy9zeA7S9JjYm753kVNzl/view?usp=sharing)

&#x200B;

Edit: I 
have realized that in the score function I should not take the sum of the outputs and instead should calculate the gradi
ent for each action individually in a for loop. However, the agent still has poor performance.

Edit2: For the score fun
ction I use the gradients for all of the parameters in the model and performance has increased. I have also realized I m
isunderstood the time variance described in the paper and have refactored the code to implement it correctly.  However, 
there are still issues with convergence and the model becoming overconfident causing nan values.
```
---

     
 
all -  [ [D] Publishing Negative Results ](https://www.reddit.com/r/MachineLearning/comments/1aikp5f/d_publishing_negative_results/) , 2024-02-11-0911
```
I‘ve been working on a ML research project, and unfortunately, the results don‘t align with my hypothesis. I‘ve gotten n
egative results.

While disheartening, I believe there‘s great value in sharing these results as the hypothesis itself r
elies on a sensible theoretical foundation, and it‘s not a priori evident that the results would have been negative.

So
, my question is, can negative results be published at top ML conferences (NeurIPS/ICLR/ICML/…)? Have any of you faced s
imilar situations? How did you navigate this? Did your efforts to publish negatice results at prestigious conferences pr
ove successful?
```
---

     
 
all -  [ AI alignment prize suggestion: Introduce AI Safety concepts into the ML community ](https://www.reddit.com/r/AIsafetyideas/comments/1aiglw9/ai_alignment_prize_suggestion_introduce_ai_safety/) , 2024-02-11-0911
```
Recently, there have been several papers published at top ML conferences that introduced concepts from the AI safety com
munity into the broader ML community. Such papers often define a problem, explain why it matters, sometimes formalise it
, often include extensive experiments to showcase the problem, sometimes include some initial suggestions for remedies. 
Such papers are useful in several ways: they popularise AI alignment concepts, pave the way for further research,  and d
emonstrate that researchers can do alignment research while also publishing in top venues. A great example would be Opti
mal Policies Tend To Seek Power, published in NeurIPS. Future Fund could advertise prizes for any paper that gets publis
hed in a top ML/NLP/Computer Vision conference (from ML, that would be NeurIPS, ICML, and ICLR) and introduces a key con
cept of AI alignment. 
```
---

     
 
all -  [ [D] questions on ICML 2024 submission timeline ](https://www.reddit.com/r/MachineLearning/comments/1ahxe7t/d_questions_on_icml_2024_submission_timeline/) , 2024-02-11-0911
```
Hello all!

Since it's the first time I am submitting to ICML:

1. is it known when the reviews will be released? in neu
rips and iclr, there was info in the call for papers but I couldn't find sth in this year's icml deadline
2. how much ti
me are we given for the author response? is it as long as it is for iclr?
3. will we be able to upload a new draft or wi
ll the replies be only given by text?
4. can we interact with reviewers during the rebuttal or is it just a one-way, sin
gle-time author response?

thanks!
```
---

     
 
all -  [ Picked up all these Tapes today! ](https://i.redd.it/pcbd29avx1gc1.jpeg) , 2024-02-11-0911
```
Found this whole lot at VV for the grand total of $5.99! Lots of them still have the original Sony store tags on them!
```
---

     
 
all -  [ Academic journal or conference for AI safety ](https://www.reddit.com/r/AIsafetyideas/comments/1agmkg5/academic_journal_or_conference_for_ai_safety/) , 2024-02-11-0911
```
To help boost the prestige of safety research, leading to more people starting the career.

Since academic ML mostly pub
lishes at conferences, this could be a conference instead.

&#x200B;

AI Safety Academic Conference

Technical AI Safety


&#x200B;

The idea is to fund and provide logistical/admin support for a reasonably large AI safety conference along t
he lines of Neurips etc. Academic conferences provide several benefits: 1) Potentially increasing the prestige of an are
a and boosting the career capital of  people who get accepted papers. 2) Networking and sharing ideas, 3)  Providing fee
dback on submitted papers and highlighting important/useful papers.  This conference would be unusual in that the work s
ubmitted shares approximately the same concrete goal (avoiding risks from powerful AI).  While traditional  conferences 
might focus on scientific novelty and complicated/'cool' papers, this conference could have a particular focus on things
 like reproducibility or correctness of empirical results, peer support and mentorship, non-traditional research mediums
 (e.g. blog posts/notebooks) , and encouraging authors to have a plausible story for why their work is actually reducing
 risks from AI.
```
---

     
 
all -  [ Research Advances in Transformer Time Series Forecasting Models ](https://www.reddit.com/r/deeplearning/comments/1ag4xfp/research_advances_in_transformer_time_series/) , 2024-02-11-0911
```
Just published a new article describing [recent advances in the deep learning for time series](https://medium.com/deep-d
ata-science/advances-in-deep-learning-for-time-series-forecasting-classification-winter-2024-a3fd31b875b0) forecasting a
nd classification space. Specifically, discussed new research at Neurips and ICML and how it compared to baseline method
s like DLinear. I also critiqued some problematic and flawed papers such as TimeGPT. 
```
---

     
 
all -  [ How much am I worth? ~Big Tech Specialty Research Scientist ](https://www.reddit.com/r/Salary/comments/1afrju3/how_much_am_i_worth_big_tech_specialty_research/) , 2024-02-11-0911
```
**Face value experience:**  
I have a PhD in mathematical optimization, with expertise in signal processing, with public
ized innovations in both theoretical (ICML) and applied (NeurIPS) machine learning. The latter publication within the la
st 2 years. I have worked in govt contractor-like roles for the last 4-6 years, but for small scientific firms. 1-2 year
s as a Senior Scientist, and next (currently) as a 'Research Professor' (95% applied research, 5% mentoring PhD candidat
es). Intentional vagueness for anonymity. I have never worked in big tech except for a 5 month software engineering inte
rnship (also related to ML).

**The Position:**  
I have reason to believe that a big-tech team is about to call me with
 an offer. It is a very specialized, secretive lab of about 20 people within one of the famous 'big tech' companies (ove
r 80k employees) with a very high reputation in the ML field (top 3 depending who you ask). The lab is trying to build a
 product with sensors that use biometric signals that have never been commercialized before and requires signal-processi
ng-tailored ML (learning invariances at the sensor level). 

At the onsite, I came to really like the team and am convin
ced this is my dream job. The position is 'research scientist' at the technical lead level, so I would be doing research
 but also setting the research direction for 2-3 other. I have experience leading a team of 3 and interfacing with many 
tech leads to deploy real world systems, but not for very long, so this will be a promotion for me. I'm not sure how muc
h they realize that.

**The Issue:**  
From my understanding, it is literally expected that I negotiate. This goes again
st my nature (which is to thank them and say yes), so I'm anxiously searching podcasts and youtube videos for help under
standing what I'm worth and what I should ask for/ how I should ask for it. But I'm not a software engineer or a general
ized data scientist -- it's got this specialization aspect that may or may not be (but seems) important. I do not have a
ny other offers (I'm not even applying anywhere else ATM, a friend of a friend on the team reached out to me about apply
ing).

**Other Random Factors That May Not Matter:**.

*  I have the highest US security clearance an employer could hop
e for a potential employee to have. No clue if this would be of use to the specific team--probably not. Not if anyone in
 the company would care but other big tech famously pay >50k bonuses to maintain the required lifestyle.
* My current sa
lary is between 175k-200k, I get so much PTO that I can hardly spend it all and it never expires, with VERY flexible wor
k arrangement and the best job security you can hope for. In my view the job security and flexibility is comparatively g
oing away (although it will be good for long-term resume) and I doubt I'll get nearly as much time off. In general I hav
e it pretty laid back and I think this will increase my stress levels across the board which should be compensated for.


**TL;DR:**  
How much should I be aiming for? How should I distribute the target compensation across salary, sign on bo
nus, stock, and wahtever else... (Ive never gotten a big tech offer)
```
---

     
 
all -  [ Regret bounds in reinforcement learning ](https://www.reddit.com/r/reinforcementlearning/comments/1aeiexo/regret_bounds_in_reinforcement_learning/) , 2024-02-11-0911
```
I’ve been away from reading theoretical reinforcement learning papers for a couple of years and was getting curious on h
ow the field has progressed since then. Last time I checked, there was a paper that claimed that they closed the upper a
nd lower bounds of the regret in MDP… where a mistake was discovered in the proof. What happened since then?

Edit: I th
ink it was this one (https://proceedings.neurips.cc/paper/2017/hash/3621f1454cacf995530ea53652ddf8fb-Abstract.html) if s
omeone can point to a follow up paper, I’d really appreciate it!
```
---

     
 
all -  [ [R] Thoughts about ML theory papers in conferences like International Symposium on Information Theor ](https://www.reddit.com/r/MachineLearning/comments/1abwmal/r_thoughts_about_ml_theory_papers_in_conferences/) , 2024-02-11-0911
```
I have published a few papers in conferences like the International Symposium on Information Theory (ISIT) and Allerton.
 However, when I apply for internship positions, the applications sometimes ask about the number of published papers in 
conferences like Neurips, ICML, ICLR, etc.

Although by any standards, my research papers are 'good' (at least in my opi
nion). However, I feel that I'm not targeting the right conferences. My advisor has also published a lot in these confer
ences, and I would say s/he likes to 'play safe' and avoids taking any risks at these big venues.
```
---

     
 
all -  [ Acceptance rate of workshops in conferences [D] ](https://www.reddit.com/r/MachineLearning/comments/19do6qn/acceptance_rate_of_workshops_in_conferences_d/) , 2024-02-11-0911
```
From the Internet I easily found the acceptance rate of conferences but what is the acceptance rate of workshops conduct
ed in conferences like AISTATS/CVPR/Neurips/ICML? 
```
---

     
 
all -  [ What Bodies Think About: Bioelectric Computation Outside the Nervous System - NeurIPS 2018 ](https://youtu.be/RjD1aLm4Thg?si=j1-jVO--H2lGHaUf) , 2024-02-11-0911
```
One of the best lectures I’ve ever watched! This might sound boring because it’s presented that way, but this has the po
tential to to enlighten you!
```
---

     
 
all -  [ I read through all NeurIPS 2023 Abstracts and wrote about it (r/MachineLearning) ](https://www.reddit.com/r/MachineLearning/comments/19cxibs/p_i_read_through_all_neurips_2023_abstracts_and/) , 2024-02-11-0911
```

```
---

     
 
all -  [ I read through the NeurIPS 2023 Abstracts and wrote about it ](https://alexzhang13.github.io/blog/2024/neurips2023) , 2024-02-11-0911
```
I made this resource that I think might be quite useful here, especially for those looking to find some new, relevant wo
rks to read or use for their own projects. It discusses the content from roughly 300 papers, but the topics broadly pert
ain to all of NeurIPS 2023. Happy reading!
```
---

     
 
all -  [ Advancements in machine learning for machine learning ](https://www.reddit.com/r/worldTechnology/comments/19c2sch/advancements_in_machine_learning_for_machine/) , 2024-02-11-0911
```
With the recent and accelerated advances in machine learning (ML), machines can understand natural language, engage in c
onversations, draw images, create videos and more. Modern ML models are programmed and trained using ML programming fram
eworks, such as TensorFlow, JAX, PyTorch, among many others. These libraries provide high-level instructions to ML pract
itioners, such as linear algebra operations (e.g., matrix multiplication, convolution, etc.) and neural network layers (
e.g., 2D convolution layers, transformer layers). Importantly, practitioners need not worry about how to make their mode
ls run efficiently on hardware because an ML framework will automatically optimize the user's model through an underlyin
g compiler. The efficiency of the ML workload, thus, depends on how good the compiler is. A compiler typically relies on
 heuristics to solve complex optimization problems, often resulting in suboptimal performance.

In this blog post, we pr
esent exciting advancements in ML for ML. In particular, we show how we use ML to improve efficiency of ML workloads! Pr
ior works, both internal and external, have shown that we can use ML to improve performance of ML programs by selecting 
better ML compiler decisions. Although there exist a few datasets for program performance prediction, they target small 
sub-programs, such as basic blocks or kernels. We introduce “TpuGraphs: A Performance Prediction Dataset on Large Tensor
 Computational Graphs” (presented at NeurIPS 2023), which we recently released to fuel more research in ML for program o
ptimization. We hosted a Kaggle competition on the dataset, which recently completed with 792 participants on 616 teams 
from 66 countries. Furthermore, in “Learning Large Graph Property Prediction via Graph Segment Training”, we cover a nov
el method to scale graph neural network (GNN) training to handle large programs represented as graphs. The technique bot
h enables training arbitrarily large graphs on a device with limited memory capacity and improves generalization of the 
model.

# ML compilers

ML compilers are software routines that convert user-written programs (here, mathematical instru
ctions provided by libraries such as TensorFlow) to executables (instructions to execute on the actual hardware). An ML 
program can be represented as a computation graph, where a node represents a tensor operation (such as matrix multiplica
tion), and an edge represents a tensor flowing from one node to another. ML compilers have to solve many complex optimiz
ation problems, including graph-level and kernel-level optimizations. A graph-level optimization requires the context of
 the entire graph to make optimal decisions and transforms the entire graph accordingly. A kernel-level optimization tra
nsforms one kernel (a fused subgraph) at a time, independently of other kernels.

&#x200B;

[ Important optimizations in
 ML compilers include graph-level and kernel-level optimizations. ](https://preview.redd.it/n6hs3zdyhsdc1.png?width=1999
&format=png&auto=webp&s=afa7e9a80f5d73c94c1692eb45612f51d7bdfe11)

To provide a concrete example, imagine a matrix (2D t
ensor):

&#x200B;

[matrix](https://preview.redd.it/q7m0npe3isdc1.png?width=1999&format=png&auto=webp&s=56382ec9b2462d71
e48efcd3fc38405219b046c2)

It can be stored in computer memory as \[A B C a b c\] or \[A a B b C c\], known as row- and 
column-major memory layout, respectively. One important ML compiler optimization is to assign memory layouts to all inte
rmediate tensors in the program. The figure below shows two different layout configurations for the same program. Let’s 
assume that on the left-hand side, the assigned layouts (in red) are the most efficient option for each individual opera
tor. However, this layout configuration requires the compiler to insert a copy operation to transform the memory layout 
between the add and convolution operations. On the other hand, the right-hand side configuration might be less efficient
 for each individual operator, but it doesn’t require the additional memory transformation. The layout assignment optimi
zation has to trade off between local computation efficiency and layout transformation overhead.

&#x200B;

![img](2r9mj
oz7isdc1 ' A node represents a tensor operator, annotated with its output tensor shape [n0, n1, ...], where ni is the si
ze of dimension i. Layout {d0, d1, ...} represents minor-to-major ordering in memory. Applied configurations are highlig
hted in red, and other valid configurations are highlighted in blue. A layout configuration specifies the layouts of inp
uts and outputs of influential operators (i.e., convolution and reshape). A copy operator is inserted when there is a la
yout mismatch.
 ')

If the compiler makes optimal choices, significant speedups can be made. For example, we have seen u
p to a 32% speedup when choosing an optimal layout configuration over the default compiler’s configuration in the XLA be
nchmark suite.

# TpuGraphs dataset

Given the above, we aim to improve ML model efficiency by improving the ML compiler
. Specifically, it can be very effective to equip the compiler with a learned cost model that takes in an input program 
and compiler configuration and then outputs the predicted runtime of the program.

&#x200B;

With this motivation, we re
lease TpuGraphs, a dataset for learning cost models for programs running on Google’s custom Tensor Processing Units (TPU
s). The dataset targets two XLA compiler configurations: layout (generalization of row- and column-major ordering, from 
matrices, to higher dimension tensors) and tiling (configurations of tile sizes). We provide download instructions and s
tarter code on the TpuGraphs GitHub. Each example in the dataset contains a computational graph of an ML workload, a com
pilation configuration, and the execution time of the graph when compiled with the configuration. The graphs in the data
set are collected from open-source ML programs, featuring popular model architectures, e.g., ResNet, EfficientNet, Mask 
R-CNN, and Transformer. The dataset provides 25× more graphs than the largest (earlier) graph property prediction datase
t (with comparable graph sizes), and graph size is 770× larger on average compared to existing performance prediction da
tasets on ML programs. With this greatly expanded scale, for the first time we can explore the graph-level prediction ta
sk on large graphs, which is subject to challenges such as scalability, training efficiency, and model quality.

&#x200B
;

[ Scale of TpuGraphs compared to other graph property prediction datasets. ](https://preview.redd.it/ebfs36lcisdc1.pn
g?width=2868&format=png&auto=webp&s=0e6e2e1f39ebd839df0cb979e4ad2c142b7e676b)

 We provide baseline learned cost models 
with our dataset (architecture shown below). Our baseline models are based on a GNN since the input program is represent
ed as a graph. Node features, shown in blue below, consist of two parts. The first part is an *opcode id*, the most impo
rtant information of a node, which indicates the type of tensor operation. Our baseline models, thus, map an opcode id t
o an *opcode embedding* via an embedding lookup table. The opcode embedding is then concatenated with the second part, t
he rest of the node features, as inputs to a GNN. We combine the node embeddings produced by the GNN to create the fixed
-size embedding of the graph using a simple graph pooling reduction (i.e., sum and mean). The resulting graph embedding 
is then linearly transformed into the final scalar output by a feedforward layer. 

&#x200B;

[ Our baseline learned cos
t model employs a GNN since programs can be naturally represented as graphs. ](https://preview.redd.it/jdcalhjgisdc1.png
?width=2284&format=png&auto=webp&s=f253742e4262ad004fa7a6bc6b3dea31c15c9d5c)

Furthermore we present Graph Segment Train
ing (GST), a method for scaling GNN training to handle large graphs on a device with limited memory capacity in cases wh
ere the prediction task is on the entire-graph (i.e., graph-level prediction). Unlike scaling training for node- or edge
-level prediction, scaling for graph-level prediction is understudied but crucial to our domain, as computation graphs c
an contain hundreds of thousands of nodes. In a typical GNN training (“Full Graph Training”, on the left below), a GNN m
odel is trained using an entire graph, meaning all nodes and edges of the graph are used to compute gradients. For large
 graphs, this might be computationally infeasible. In GST, each large graph is partitioned into smaller segments, and a 
random subset of segments is selected to update the model; embeddings for the remaining segments are produced without sa
ving their intermediate activations (to avoid consuming memory). The embeddings of all segments are then combined to gen
erate an embedding for the original large graph, which is then used for prediction. In addition, we introduce the histor
ical embedding table to efficiently obtain graph segments’ embeddings and segment dropout to mitigate the staleness from
 historical embeddings. Together, our complete method speeds up the end-to-end training time by 3×.

&#x200B;

[ Compari
ng Full Graph Training \(typical method\) vs Graph Segment Training \(our proposed method\). ](https://preview.redd.it/l
us2m3ikisdc1.png?width=790&format=png&auto=webp&s=eb8ad9e466ef062ef171b24f409b6c4eea2c5346)

&#x200B;

[Advancements in 
machine learning for machine learning](https://blog.research.google/2023/12/advancements-in-machine-learning-for.html)
```
---

     
 
all -  [ Quant Research of the Week (10th Edition) ](https://www.reddit.com/r/quant/comments/1994aei/quant_research_of_the_week_10th_edition/) , 2024-02-11-0911
```
# SSRN

### Recently Published

**Quantitative**

[**SpotV2Net: Intraday Spot Volatility Forecasting**](https://papers.s
srn.com/sol3/papers.cfm?abstract_id=4692194): SpotV2Net, a new forecasting model based on Graph Attention Network archit
ecture, enhances the accuracy of intraday spot volatility predictions for financial assets. (2024-01-11, shares: 2.0)

[
**Model Averaging & Double Machine Learning**](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4691169): The article
 presents two new stacking methods for double-debiased machine learning (DDML), showing its robustness against unknown f
unctional forms, with software available in Stata and R. (2024-01-11, shares: 3.0)

[**Data Preparation for Code Smell D
etection: A Literature Review**](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4693778): The review examines data 
preparation techniques in deep learning-based code smell detection, suggesting ways to prepare high-quality data and emp
hasizing the need for data diversity, standardization, and accessibility. (2024-01-13, shares: 2.0)

**Financial**

[**G
amma Risk and Volatility Propagation in Trading**](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4692190): A study
 reveals that short-term options trading does not increase market volatility, but rather has an inverse relationship wit
h intraday volatility. (2024-01-11, shares: 27.0)

[**Option Flows and Market Instability**](https://papers.ssrn.com/sol
3/papers.cfm?abstract_id=4695776): The speculative use of call options can cause price instability in the underlying ass
et's market, even with advanced volatility estimators, as per a study using the MinMaSS stability measure. (2024-01-15, 
shares: 8.0)

[**Extreme Liquidity in Asset Modeling**](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4694674): A 
study using crypto assets indicates that jumps in asset prices are signs of extreme liquidity and can be effectively mod
eled using autoregressive models adjusted with liquidity. (2024-01-13, shares: 2.0)

[**Carbon Footprint Reduction in In
dex Portfolios**](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4692326): The article suggests that investors can 
lower the carbon footprint of their index-based portfolio by over 50% by focusing on low carbon emission stocks and limi
ting high-emission companies. (2024-01-12, shares: 2.0)

[**Extended Overlaps: Optimal Trading Hours in Europe**](https:
//papers.ssrn.com/sol3/papers.cfm?abstract_id=4693290): The article reveals that extended trading hours between North Am
erica and Europe during Daylight Saving Time enhances market liquidity and price efficiency, contributing to the discuss
ion on optimal trading hours in Europe. (2024-01-12, shares: 3.0)

### Recently Updated

## Quantitative

[**Real estate
 valuation with prototype-based models and machine learning**](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=46950
79): The article introduces a novel real estate valuation model that uses prototype-based learning, a method that compar
es properties to similar ones, unlike traditional machine learning methods. (2023-12-22, shares: 3.0)

[**DeepTraderX: D
isrupting trading strategies with deep learning**](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4692622): The pap
er presents DeepTraderX, a Deep Learning-based trader that learns from market prices, and demonstrates its successful pe
rformance in a multithreaded market simulation. (2023-10-20, shares: 2.0)

[**Flood Risk Pricing: Geo-Hierarchical Deep 
Learning**](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4692475): A new deep learning framework enhances flood r
isk modeling, providing more accurate pricing and reducing capital requirements, as shown in a Mississippi River case st
udy. (2022-01-13, shares: 2.0)

[**Effectiveness of Forex Intervention: Role of Domestic Fundamentals**](https://papers.
ssrn.com/sol3/papers.cfm?abstract_id=4692676): Foreign exchange intervention can stabilize currencies in emerging market
s under conditions like low volatility and high inflation, as per a study of 20 emerging economies. (2023-12-28, shares:
 2.0)

[**Probabilistic Electricity Price Forecasting with Trading Applications**](https://papers.ssrn.com/sol3/papers.c
fm?abstract_id=4695159): A new method for electricity price forecasting using artificial neural networks is less costly 
and performs similarly to benchmarks, offering potential trading strategies for investors. (2023-08-02, shares: 2.0)

##
 Financial

[**Boosting Fund Performance**](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4697785): Mutual funds t
hat match their investments with similar benchmark peers like the S&P 500 index yield higher returns and experience less
 volatility. (2023-03-11, shares: 2.0)

[**Financial Market Developments and Employee Welfare**](https://papers.ssrn.com
/sol3/papers.cfm?abstract_id=4690550): Equity options and credit default swaps trading benefits company employees by red
ucing short-term managerial focus and improving information efficiency. (2023-04-19, shares: 2.0)

[**Global Volatility 
and Capital Flows**](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4691941): During high volatility periods, insti
tutional investors globally reduce their equity allocations, while retail investors shift from small-cap to large-cap st
ocks. (2022-04-13, shares: 2.0)

[**Fear in Finance: FoMO Impact**](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=
4692691): The Fear of Missing Out (FoMO) effect in financial markets boosts equity and cryptocurrency prices and lowers 
market volatility due to reduced investor disagreement. (2021-12-08, shares: 2.0)

[**Yelp Sentiment & Asset Pricing**](
https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4691145): A sentiment index based on Yelp restaurant reviews can pre
dict stock market reversals and mispricing, with pessimism being a key predictive factor. (2022-08-04, shares: 2.0)

[**
Deep Calibration for Stochastic Volatility**](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4692741): A new method
 using neural networks to calibrate stochastic volatility models has proven to be robust and efficient, as confirmed by 
empirical and Monte Carlo experiments. (2023-06-25, shares: 2.0)

[**Climate-Optimized Investment Portfolios**](https://
papers.ssrn.com/sol3/papers.cfm?abstract_id=4696468): The Climate Capital Efficiency Ratio (CER) ranks companies based o
n their carbon emission savings per dollar spent, offering a useful tool for climate-focused investing. (2023-11-28, sha
res: 2.0)

# ArXiv

## Finance

[**Cash management models for data fitting**](http://dx.doi.org/10.1016/j.cor.2018.04.00
7): The article introduces a novel method for cash management models using stochastic and linear programming, showing th
at a small random data sample can effectively fit these models. (2024-01-16, shares: 9)

[**Super-hedging pricing and Im
mediate-Profit arbitrage**](http://arxiv.org/abs/2401.05713): The study explores the super-hedging pricing valuation iss
ue in different financial contexts, emphasizing the effect of changes in prior information and the growth of super-hedgi
ng prices under uncertainty. (2024-01-11, shares: 5)

[**Efficiency of graph databases for financial analysis**](http://
arxiv.org/abs/2401.07483): The study contrasts SQL, No-SQL, and graph databases in terms of efficiency and performance, 
concluding that ESG's Graph database is superior for extended analytics in business and investment. (2024-01-15, shares:
 4)

[**Quantum probability asset return modeling**](http://arxiv.org/abs/2401.05823): The article suggests a new approa
ch to quantum finance, connecting quantum probability's mathematical structure to traders' decisions and market behavior
s, and formulating a Schrödinger-like trading equation to describe the multimodal distribution of asset returns. (2024-0
1-11, shares: 4)

[**SpotV2Net: Intraday Volatility Forecasting**](http://arxiv.org/abs/2401.06249): The article introdu
ces SpotV2Net, a new model for predicting intraday spot volatility using a Graph Attention Network, which has shown bett
er accuracy in predicting Dow Jones Industrial Average index prices. (2024-01-11, shares: 4)

[**Equity Auction Dynamics
: Liquidity Models**](http://arxiv.org/abs/2401.06724): The study applies the latent/revealed order book framework to eq
uity auctions, showing no indicative price predictability and providing accurate model parameter measurements. (2024-01-
12, shares: 3)

[**Dynamic Portfolio Selection with Disappointment Aversion**](http://arxiv.org/abs/2401.08323): The res
earch discusses portfolio selection under generalized disappointment aversion (GDA), finding that investment in the stoc
k market is consistently lower under GDA than under traditional Expected Utility theory. (2024-01-16, shares: 3)

[**Lon
gstaff Schwartz Monte Carlo Approach to Game Option Pricing**](http://arxiv.org/abs/2401.08093): The article suggests a 
two-step Longstaff Schwartz Monte Carlo method for pricing game options, which provides more reliable results than the o
riginal method. (2024-01-16, shares: 2)

[**Deep Minimizing Movement Method for Option Pricing**](http://arxiv.org/abs/2
401.06740): The paper introduces a deep learning method for pricing European basket options using Artificial Neural Netw
orks and two methods for discretizing the integral operator, focusing on assets with jump-diffusion dynamics. (2024-01-1
2, shares: 2)

## Miscellaneous

[**Enhancing Financial Sentiment Analysis with Heterogeneous LLM Agents**](http://arxiv
.org/abs/2401.05799): A study suggests using large language models without fine-tuning for financial sentiment analysis,
 offering a design framework that enhances accuracy. (2024-01-11, shares: 4)

[**Analyzing Herd Behavior in Investment**
](http://arxiv.org/abs/2401.07183): A study introduces the concept of average deviation to measure the difference betwee
n two agents' investment decisions, studying the effect of herd behavior on these decisions. (2024-01-14, shares: 2)

##
 Crypto & Blockchain

[**Backrun Auctions & Trader Protection**](http://arxiv.org/abs/2401.08302?utm_source=dlvr.it&utm_
medium=twitter): The study presents a new laminated queueing model for batched trading on decentralized exchanges, aimin
g to improve transaction infrastructure and examining the potential for price manipulation by arbitrageurs. (2024-01-16,
 shares: 5)

[**Transformer-Based ETH Price Prediction**](http://arxiv.org/abs/2401.08077?utm_source=dlvr.it&utm_medium=
twitter): The research uses a transformer-based neural network to forecast Ethereum prices, indicating a strong correlat
ion with other cryptocurrencies and sentiments, and suggests a theory on sentiment-driven illusion of causality in crypt
ocurrency price movements. (2024-01-16, shares: 4)

[**Analysis of Impermanent Loss in DEX**](http://arxiv.org/abs/2401.
07689): The paper explores the issue of impermanent loss in decentralized exchanges through Monte Carlo simulations, ind
icating that price changes don't always result in losses for liquidity providers and that an arbitrage-friendly environm
ent is beneficial for them. (2024-01-15, shares: 3)

[**Liquidity Provision on DEX**](https://papers.ssrn.com/sol3/paper
s.cfm?abstract_id=4694683): Decentralized exchanges' infrastructure can lead to arbitrage losses for liquidity providers
, with design changes offering limited reduction in these losses, as shown in a study using the Silicon Valley Bank coll
apse. (2021-03-17, shares: 2.0)

## Historical Trending

[**Handling Missing Values in ML Portfolios**](https://arxiv.or
g/abs/2207.13071): The research analyzes missing data in return predictors, concluding that simple imputation methods ar
e effective and complex ones can underperform if misused. (2022-07-21, shares: 42)

[**Deep Signature Algorithm for Opti
ons**](https://arxiv.org/abs/2211.11691): The research expands the backward scheme for state-dependent FBSDEs with refle
ctions to path-dependent FBSDEs, demonstrating the convergence of the numerical algorithm and providing examples of its 
use. (2022-11-21, shares: 14)

[**Curriculum and Imitation Learning for Time-Series Control**](https://arxiv.org/abs/231
1.13326): The study finds that curriculum learning enhances performance in control tasks over highly stochastic time-ser
ies data, while imitation learning should be used carefully. (2023-11-22, shares: 19)

[**Kernel Hilbert Space Approach 
to Volatility Models**](https://arxiv.org/abs/2203.01160): The paper presents a new regularization approach for solving 
the singular McKean-Vlasov equation, commonly used in financial models, using the reproducing kernel Hilbert space techn
ique. (2022-03-02, shares: 17)

# ArXiv ML

## Recently Published

[**Easy Training Data**](https://arxiv.org/abs/2401.0
6751): The study suggests that current language models can effectively generalize from easy to hard data, implying that 
scalable oversight may be less challenging than previously believed. (2024-01-12, shares: 94)

[**Transformers as RNNs**
](https://arxiv.org/abs/2401.06104): The research shows that decoder-only transformers can be seen as infinite multi-sta
te RNNs and introduces a new policy, TOVA, which performs better in long-range tasks and uses less memory. (2024-01-11, 
shares: 152)

[**TOFU Unlearning for LLMs**](https://arxiv.org/abs/2401.06121): The study presents TOFU, a new benchmark
 for understanding unlearning in large language models, revealing that existing unlearning algorithms are not effective.
 (2024-01-11, shares: 22)

[**PANDORA: Parallel Dendrogram Construction Algorithm: Parallel Dendrogram Construction Algo
rithm PANDORA**](https://arxiv.org/abs/2401.06089): Pandora, a new parallel algorithm, has been introduced for efficient
 dendrogram construction in hierarchical clustering, offering significant speed improvements on CPUs and GPUs. (2024-01-
11, shares: 15)

# GitHub

## Finance

[**ViTST: Time Series as Images Transformer**](https://github.com/Leezekun/ViTST)
: NeurIPS 2023 introduces a paper discussing the use of Vision Transformer for analyzing irregularly sampled time series
 data. (2023-02-23, shares: 51.0)

[**Stockformer: Swing Trading with STL Decomposition and Self-Attention**](https://gi
thub.com/Eric991005/Stockformer): A paper suggesting a swing trading strategy using STL Decomposition and Self-Attention
 Networks is being reviewed for publication in Neurocomputing. (2023-11-09, shares: 12.0)

[**Piepilot: Portfolio Optimi
zer**](https://github.com/ranaroussi/piepilot): A straightforward tool designed for optimizing investment portfolios. (2
024-01-13, shares: 4.0)

## Trending

[**Fast AI Gateway**](https://github.com/Portkey-AI/gateway): The article explores
 a high-speed AI Gateway capable of managing 100 LLMs via a single, user-friendly API. (2023-08-23, shares: 1370.0)

[**
ChatGPT Web UI**](https://github.com/ollama-webui/ollama-webui): The piece presents a web user interface client for Olla
ma, modeled after ChatGPT. (2023-10-06, shares: 3316.0)

[**Draggable Streamlit Dashboard**](https://github.com/okld/str
eamlit-elements): The article provides a guide on building a customizable Streamlit dashboard with tools like Material U
I widgets, Monaco editor, Visual Studio Code, Nivo charts, etc. (2021-04-15, shares: 451.0)

# LinkedIn

## Trending

[*
*AIs Impact on Asset Management**](https://www.linkedin.com/feed/update/urn:li:activity:7153365973817827332): GitHub CEO
, Thomas Dohmke, explores the potential disruption of Asset Management by Artificial Intelligence. (2024-01-17, shares: 
2.0)

[**Evolutionary ML Approaches**](https://www.linkedin.com/feed/update/urn:li:activity:7153371055707848705): A new 
book by global researchers delves into evolutionary methods in machine learning, discussing evolutionary computation, ne
ural networks, and their practical applications. (2024-01-17, shares: 1.0)

[**ML Execution Time in Asset Pricing**](htt
ps://www.linkedin.com/feed/update/urn:li:activity:7153074375037009920): Demirbaga and Xu's research emphasizes the signi
ficance of machine learning model execution time in asset pricing, recommending feature reduction and fewer time observa
tions as ways to save time. (2024-01-17, shares: 1.0)

## Informative

[**Optimizing PnL with Linear Signals: An ML Fram
ework**](https://www.linkedin.com/feed/update/urn:li:activity:7153293929365336065): The article introduces an unsupervis
ed machine learning framework that optimizes PnL by using a linear relationship between exogenous variables and the trad
ing signal to maximize the Sharpe Ratio. (2024-01-17, shares: 1.0)

[**Addressing Overfitting in Backtesting**](https://
www.linkedin.com/feed/update/urn:li:activity:7153278047071137793): The article emphasizes the need to prevent overfittin
g in backtesting results, recommending techniques like K-fold cross-validation and randomization in simulations. (2024-0
1-17, shares: 1.0)

# Twitter

## Quantitative

[**Phidata's Python Library for Autonomous AI**](https://twitter.com/car
lcarrie/status/1747057820841701592): Phidata has launched a new Python library for Autonomous AI that utilizes LLM funct
ion calling, with resources accessible on Streamlit FastAPI. (2024-01-16, shares: 0)

[**IMF Report on AI's Impact on Em
ployment**](https://twitter.com/carlcarrie/status/1747041277370065352): The IMF has published a report analyzing the eff
ects of Generative AI brands on job markets. (2024-01-15, shares: 0)

[**BCGs Report: From Potential to Profit with GenA
I**](https://twitter.com/carlcarrie/status/1746916291619836145): According to a BCG report, companies investing in GenAI
 could expect over 10% cost savings, potentially amounting to 1 billion in savings. (2024-01-15, shares: 0)

## Miscella
neous

[**The Rise of Diffusion Models**](https://twitter.com/carlcarrie/status/1746643702896796040): The article explor
es the increasing use of diffusion models in timeseries forecasting, detailing 11 specific versions, their theoretical b
asis, effectiveness on various datasets, and comparisons between them. (2024-01-14, shares: 0)

[**Marimo: Reinventing J
upyter**](https://twitter.com/carlcarrie/status/1745999782659723373): The article presents Marimo, a revamped version of
 the Jupyter Python notebook, designed to be a reproducible, interactive, and shareable Python program, as opposed to an
 error-prone JSON scratchpad. (2024-01-13, shares: 0)

[**HBR on Fabrications and LLM Problems**](https://twitter.com/ca
rlcarrie/status/1745962927629185407): The article reviews the Harvard Business Review's perspective on plausible fabrica
tions and other issues related to LLM in the context of productivity transformation led by LLM. (2024-01-13, shares: 0)


# Videos

## Quantitative

[**Mastering Python Finance**](https://www.youtube.com/watch?v=qkKAJwg4ohQ): The Certificate
 in Python for Finance Program provides in-depth knowledge on financial data science, asset management, algorithmic trad
ing, and computational finance using Python and AI. (2024-01-11, shares: 5.0)

[**AI and Finance Future**](https://www.y
outube.com/watch?v=T-AyBUMcWeg): The AFA Panel on AI discusses the influence of AI on the financial sector with panelist
s from various universities. (2024-01-13, shares: 11.0)

[**RAW AI in Finance Workshop 3**](https://www.youtube.com/watc
h?v=5w99hUczjyY): A screen recording from the Workshop on AI in Finance at Texas State University San Marcos is accessib
le on GitHub. (2024-01-11, shares: 0.0)

[**AFA Business Meeting & Awards**](https://www.youtube.com/watch?v=BYZntg0228I
): The AFA Business Meeting and Presidential Address involves discussions on the future of finance from professionals an
d academics. (2024-01-14, shares: 9.0)

# Reddit

## Quantitative

[**Choosing the Right Field: Quantitative Finance Jou
rney**](https://www.reddit.com/r/quant/comments/196oru9/how_did_you_know_that_the_quant_field_was_right/): As an AI, I'm
 unable to browse the internet or access articles directly. Please provide the text of the articles you'd like summarize
d. (2024-01-14, shares: 41.0)

[**Trouble at Jump Trading**](https://www.reddit.com/r/quant/comments/193vnrs/trouble_at_
jump_trading/): The UK government is contemplating the introduction of a digital currency, 'Britcoin', to update its fin
ancial system. (2024-01-11, shares: 70.0)

[**Ito's Lemma Query**](https://www.reddit.com/r/quant/comments/196fqrp/quest
ion_regarding_itos_lemma/): A recent study suggests that global sea levels could rise over a meter by 2100 due to climat
e change. (2024-01-14, shares: 20.0)
```
---

     
 
all -  [ DSPy and ColBERT with Omar Khattab! ](https://www.reddit.com/r/deeplearning/comments/197bh2j/dspy_and_colbert_with_omar_khattab/) , 2024-02-11-0911
```
I am beyond excited to publish our first Weaviate Podcast interview in-person at the NeurIPS conference with Omar Khatta
b from Stanford University!

I am beyond grateful to have met Omar! I believe strongly that he is at the forefront of Ar
tificial Intelligence technology, especially with the latest developments in Large Language Models, Retrieval-Augmented 
Generation, and Vector Databases!

Omar is a prolific scientist who has published many groundbreaking works, the latest 
of which being DSPy! DSPy is also an open-source software project on GitHub, achieving roughly 5,000 stars at the time o
f this writing! I think this is just scratching the surface of where DSPy will go. I think to reach this potential, the 
next step is developer advocacy and evangelism work. I will be the first to admit that it took me a couple tries to unde
rstand the abstractions of DSPy. The framework marries the concepts of pipeline design (really well explained by the abs
tractions in LangChain, LlamaIndex, Haystack, or Weaviate modules), with prompt and model tuning. I think Omar did an am
azing job of explaining this further in the podcast, so I will stop writing this and encourage you to check out the podc
ast below haha!

Omar also touched on ColBERT and multi-vector retrieval methods. These techniques aim to achieve the be
nefits of the contextual interaction in cross-encoders, directly in a vector index, without the slow inference of applyi
ng a cross encoder of a query and millions of documents. Omar again does an incredible job explaining such a complex top
ic, stay tuned for more updates from Weaviate on multi-vector support!

I really hope you enjoy the podcast! I am beyond
 grateful to have attended the NeurIPS conference and met so many amazing people!

YouTube: [https://www.youtube.com/wat
ch?v=CDung1LnLbY](https://www.youtube.com/watch?v=CDung1LnLbY)

Spotify: [https://podcasters.spotify.com/pod/show/weavia
te/episodes/DSPy-and-ColBERT-with-Omar-Khattab----Weaviate-Podcast-85-e2effki](https://podcasters.spotify.com/pod/show/w
eaviate/episodes/DSPy-and-ColBERT-with-Omar-Khattab----Weaviate-Podcast-85-e2effki)
```
---

     
 
all -  [ Thoughts on Potential of LLMs/Foundation Models for Zero-Shot Time Series Forecasting [D] ](https://www.reddit.com/r/MachineLearning/comments/194h40f/thoughts_on_potential_of_llmsfoundation_models/) , 2024-02-11-0911
```
Hi all, I've stumbled upon this Neurips paper 'Large Language Models Are Zero-Shot Time Series Forecasters'   [2310.0782
0.pdf (arxiv.org)](https://arxiv.org/pdf/2310.07820.pdf?trk=public_post_comment-text)  and wonder what people in time se
ries think about it. The paper's authors summarize the method: 'At its core, this method represents the time series as a
 string of numerical digits, and views time series forecasting as next-token prediction in text'.

The authors seem to s
how performance nearly matching and sometimes exceeding the standard baseline such as ARIMA on DARTS baseline, with no f
urther training. I wonder what the time series people on here think of these results and whether it's likely that there 
will be foundation models for time series forecasting that will outperform current specialized forecasting methods. 

Th
anks!
```
---

     
 
all -  [ [D] How to request to be a reviewer to a conference/journal? ](https://www.reddit.com/r/MachineLearning/comments/1945n6i/d_how_to_request_to_be_a_reviewer_to_a/) , 2024-02-11-0911
```
I'm interested in reviewing for the upcoming cycles of ECCV, Neurips, ICLR, AAAI etc. 

Would also like to review for jo
urnals like T-PAMI etc. 

How does one go about this? Should I just email the editor of the journal or conference or is 
there a better way of doing it?
```
---

     
