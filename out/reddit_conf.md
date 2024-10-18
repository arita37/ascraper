 
all -  [ [5 YOE] Physics postdoc trying switch. ~100 applications, handful of interviews, no offers. ](https://www.reddit.com/r/EngineeringResumes/comments/1g60iw4/5_yoe_physics_postdoc_trying_switch_100/) , 2024-10-18-0912
```
Hi! My postdoc is expiring, and I've been looking for ML Engineer jobs. I'm also looking for ML Researcher roles. I've a
pplied to 40+ places, with only a handful of interviews. Am I making any dumb errors as I'm trying to transition? I know
 it'll be a long process, but any advice is appreciated!

I'm also not terribly sure how many years of experience to put
. I'm counting the last years of grad school, as I was working pretty much unsupervised.

https://preview.redd.it/4kglup
tqldvd1.png?width=5949&format=png&auto=webp&s=d36454ef7e65fae545a5bf7b8cf6baf745b68613


```
---

     
 
all -  [ How I Started Learning Machine Learning ](https://www.reddit.com/r/learnmachinelearning/comments/1g4x299/how_i_started_learning_machine_learning/) , 2024-10-18-0912
```
Hello, everyone. As promised, I'll write a longer post about how I entered the world of ML, hoping it will help someone 
shape their path. I'll include links to all the useful materials I used alongside the story, which you can use for learn
ing.

I like to call myself an AI Research Scientist who enjoys exploring new AI trends, delving deeper into understandi
ng their background, and applying them to real products. This way, I try to connect science and entrepreneurship because
 I believe everything that starts as scientific research ends up 'on the shelves' as a product that solves a specific us
er problem.

I began my journey in ML in 2016 when it wasn't such a popular field. Everyone had heard of it, but few wer
e applying it. I have several years of development experience and want to try my hand at ML. The first problem I encount
ered was where to start - whether to learn mathematics, statistics, or something else. That's when I came across a name 
and a course that completely changed my career.

# Let's start

You guessed it. It was Professor Andrew Ng and his globa
lly popular Machine Learning course available on Coursera (I still have the certificate, hehe). This was also my first o
fficial online course ever. Since that course no longer exists as it's been replaced by a new one, I recommend you check
 out:

1. [Machine Learning (Stanford CS229)](https://www.youtube.com/playlist?list=PLoROMvodv4rMiGQp3WXShtMGgzqpfVfbU)

2. [Machine Learning Specialization](https://www.coursera.org/specializations/machine-learning-introduction)

These two 
courses start from the basics of ML and all the necessary calculus you need to know. Many always ask questions like whet
her to learn linear algebra, statistics, or probability, but you don't need to know everything in depth. This knowledge 
helps if you're a scientist developing a new architecture, but as an engineer, not really. You need to know some basics 
to understand, such as how the backpropagation algorithm works.

I know that Machine Learning (Stanford CS229) is a very
 long and arduous course, but it's the right start if you want to be really good at ML. In my time, I filled two thick n
otebooks by hand while taking the course mentioned above.

# TensorFlow and Keras

After the course, I didn't know how t
o apply my knowledge because I hadn't learned specifically how to code things. Then, I was looking for ways to learn how
 to code it. That's when I came across a popular framework called Keras, now part of TensorFlow. I started with a new co
urse and acquiring practical knowledge:

1. [Deep Learning Specialization](https://www.coursera.org/specializations/deep
-learning)
2. [Deep Learning by Ian Goodfellow](https://www.deeplearningbook.org/)
3. [Machine Learning Yearning by Andr
ew Ng](https://info.deeplearning.ai/machine-learning-yearning-book)

These resources above were my next step. I must adm
it that I learned the most from that course and from the book Deep Learning by Ian Goodfellow because I like reading boo
ks (although this one is quite difficult to read).

# Learn by coding

To avoid just learning, I went through various Gi
tHub repositories that I manually retyped and learned that way. It may be an old-fashioned technique, but it helped me a
 lot. Now, most of those repositories don't exist, so I'll share some that I found to be good:

1. [Really good Jupyter 
notebooks that can teach you the basics of TensorFlow](https://github.com/mrdbourke/tensorflow-deep-learning)
2. [Anothe
r good repo for learning TF and Keras](https://github.com/codebasics/deep-learning-keras-tf-tutorial)

# Master the chal
lenge

After mastering the basics in terms of programming in TF/Keras, I wanted to try solving some real problems. There
's no better place for that challenge than Kaggle and the popular Titanic dataset. Here, you can really find a bunch of 
materials and simple examples of ML applications. Here are some of my favorites:

1. [Titanic - Machine Learning from Di
saster](https://www.kaggle.com/c/titanic/overview)
2. [Home Credit Default Risk](https://www.kaggle.com/competitions/hom
e-credit-default-risk/overview)
3. [House Prices - Advanced Regression Techniques](https://www.kaggle.com/competitions/h
ouse-prices-advanced-regression-techniques)
4. [Two Sigma: Using News to Predict Stock Movements](https://www.kaggle.com
/competitions/two-sigma-financial-news)

I then decided to further develop my career in the direction of applying ML to 
the stock market, first using predictions on time series and then using natural language processing. I've remained in th
is field until today and will defend my doctoral dissertation soon.

# How to deploy models

To continue, before I move 
on to the topic of specialization, we need to address the topic of deployment. Now that we've learned how to make some b
asic models in Keras and how to use them, there are many ways and services, but I'll only mention what I use today. For 
all my ML models, whether simple regression models or complex GPT models, I use FastAPI. It's a straightforward framewor
k, and you can quickly create API endpoints. I'll share a few older and useful tutorials for beginners:

1. [AI as an AP
I tutorial series](https://www.youtube.com/watch?v=56qQNcHJxyQ)
2. [A step-by-step guide](https://medium.com/@ganiyuabdu
lwajeed2002/a-step-by-step-approach-to-building-a-fast-api-for-deep-learning-classification-projects-cbd2ea6bc2f2)
3. [P
roductizing an ML Model with FastAPI and Cloud Run](https://medium.com/semantixbr/deploy-an-ml-model-with-fastapi-and-cl
oud-run-part-1-1a0b0f3b3a5d)

Personally, I've deployed on various cloud providers, of which I would highlight GCP and A
WS because they have everything needed for model deployment, and if you know how to use them, they can be quite cheap.


# Chose your specialization

The next step in developing my career, besides choosing finance as the primary area, was my
 specialization in the field of NLP. This happened in early 2020 when I started working with models based on the Transfo
rmer architecture. The first model I worked with was BERT, and the first tasks were related to classifications. My recom
mendations are to master the Transformer architecture well because 99% of today's LLM models are based on it. Here are s
ome resources:

1. [The legendary paper 'Attention Is All You Need'](https://proceedings.neurips.cc/paper_files/paper/20
17/file/3f5ee243547dee91fbd053c1c4a845aa-Paper.pdf)
2. [Hugging Face Course on Transformers](https://huggingface.co/lear
n/nlp-course/chapter1/1)
3. [Illustrated Guide to Transformers - Step by Step Explanation](https://towardsdatascience.co
m/illustrated-guide-to-transformers-step-by-step-explanation-f74876522bc0)
4. [Good repository](https://github.com/Niels
Rogge/Transformers-Tutorials)
5. [How large language models work, a visual intro to transformers](https://www.youtube.co
m/watch?v=wjZofJX0v4M)

After spending years using encoder-based Transformer models, I started learning GPT models. Good
 open-source models like Llama 2 then appear. Then, I started fine-tuning these models using the excellent Unsloth libra
ry:

1. [How to Finetune Llama-3 and Export to Ollama](https://docs.unsloth.ai/tutorials/how-to-finetune-llama-3-and-exp
ort-to-ollama)
2. [Fine-tune Llama 3.1 Ultra-Efficiently with Unsloth](https://huggingface.co/blog/mlabonne/sft-llama3)


After that, I focused on studying various RAG techniques and developing Agent AI systems. This is now called AI enginee
ring, and, as far as I can see, it has become quite popular. So I'll write more about that in another post, but here I'l
l leave what I consider to be the three most famous representatives, i.e., their tutorials:

1. [LangChain tutorial](htt
ps://python.langchain.com/docs/tutorials/)
2. [LangGraph tutorial](https://langchain-ai.github.io/langgraph/tutorials/)

3. [CrewAI examples](https://github.com/crewAIInc/crewAI-examples)

# Here I am today

Thanks to the knowledge I've gene
rated over all these years in the field of ML, I've developed and worked on numerous projects. The most significant publ
icly available project is developing an agent AI system for well-being support, which I turned into a [mobile applicatio
n](https://sintelly.com/download/). Also, my entire doctoral dissertation is related to applying ML to the stock market 
in combination with the development of GPT models and reinforcement learning (more on that in a separate post). After lo
ng 6 years, I've completed my dissertation, and now I'm just waiting for its defense. I'll share everything I'm working 
on for the dissertation publicly [on the project](https://primoinvesting.com/), and in tutorials I'm preparing to write.


If you're interested in these topics, I announce that I'll soon start with activities of publishing content on Medium 
and a blog, but I'll share all of that here on Reddit as well. Now that I've gathered years of experience and knowledge 
in this field, I'd like to share it with others and help as much as possible.

If you have any questions, feel free to a
sk them, and I'll try to answer all of them.

Thank you for reading.
```
---

     
 
all -  [ Does Grokking show that Scale will be enough to get LLMs to AGI? ](https://www.reddit.com/r/ChatGPT/comments/1g3eati/does_grokking_show_that_scale_will_be_enough_to/) , 2024-10-18-0912
```
Currently, there has been a lot of debate about whether LLMs truly reason or just memorize their training data (see this
 recent paper from Apple [\[2410.05229\] GSM-Symbolic: Understanding the Limitations of Mathematical Reasoning in Large 
Language Models (arxiv.org)](https://arxiv.org/abs/2410.05229)).

On the other hand, there have been numerous papers sho
wing that models can generalize if trained beyond the point where they overfit, known as '**grokking**' ([Towards Unders
tanding Grokking: An Effective Theory of Representation Learning (neurips.cc)](https://proceedings.neurips.cc/paper_file
s/paper/2022/hash/dfc310e81992d2e4cedc09ac47eff13e-Abstract-Conference.html)).

Based on grokking, we could argue that i
f we just train current LLMs enough, they will always converge to generalization. Seemingly, **memorization is just a lo
cal minimum** in which it can get stuck, and the true **global minimum is generalization**.

How is this possible if mem
orization is already giving near-perfect performance on the dataset for a **specific task**? Well, by looking at overall
 performance as opposed to task-specific performance, you can imagine how generalizing helps the model increase its over
all performance:

1. Generalizations use less parameter space than memorization, which the model then can use for other 
tasks, increasing its overall performance (reduction in effective dimension by generalization [\[2205.10343\] Towards Un
derstanding Grokking: An Effective Theory of Representation Learning (arxiv.org)](https://arxiv.org/abs/2205.10343))
2. 
Generalizations from one task can increase the performance on another unrelated task, increasing its overall performance
 (a recent paper shows that GPT models get better at chess and reasoning by looking at the emergent behavior of cellular
 automata: [Intelligence at the Edge of Chaos (arxiv.org)](https://arxiv.org/html/2410.02536)).

But then what happens i
f we grok the model not on a specific task, but on **all its data**? We can imagine that it would just memorize the whol
e dataset, without being incentivized to generalize since it now has near-perfect performance on the whole dataset. In t
his case, where the **global minimum is memorization**, the model can still reach generalization by changing the loss la
ndscape using **weight-decay / regularization**. Regularization punishes big weights, forcing the model to prefer simple
r solutions, reducing the minima around memorization, while leaving the minima around generalization intact. This will g
eneralize the new global minima.

Considering this convergence towards generalization over training time, for both task-
specific and overall performance, could we assume that scaling will logically make models generalize over time? In other
 words, is scale really all we need to AGI? Or is there a flaw in my reasoning, grokking is not the end-all-be-all and w
e will need new breakthroughs to get to AGI.
```
---

     
 
all -  [ Will Scale be enough to get LLMs to Reason through Grokking? ](https://www.reddit.com/r/ArtificialInteligence/comments/1g3d6kf/will_scale_be_enough_to_get_llms_to_reason/) , 2024-10-18-0912
```
Currently there has been a lot of debate whether LLMs truly reason or just memorize their training data (see this recent
 paper from Apple [\[2410.05229\] GSM-Symbolic: Understanding the Limitations of Mathematical Reasoning in Large Languag
e Models (arxiv.org)](https://arxiv.org/abs/2410.05229)).

On the other hand, there has been numerous papers showing tha
t models can generalize, if trained beyond the point where they overfit, known as 'grokking' ([Towards Understanding Gro
kking: An Effective Theory of Representation Learning (neurips.cc)](https://proceedings.neurips.cc/paper_files/paper/202
2/hash/dfc310e81992d2e4cedc09ac47eff13e-Abstract-Conference.html)).

Based on grokking, we could argue that if we just t
rain current LLMs enough, they will always converge to generalization. Seemingly, memorization is just a local minima in
 which it can get stuck, and the true global minima is generalization.

How is this possible if memorization is already 
giving near perfect performance on the dataset for a specific task? Well, by looking at overall performance opposed to t
ask-specific performance, you can imagine how generalizing helps the model increase its overall performance:

1. General
izations use less parameter space than memorization, which the model then can use for other tasks, increasing its overal
l performance (reduction in effective dimension by generalization [\[2205.10343\] Towards Understanding Grokking: An Eff
ective Theory of Representation Learning (arxiv.org)](https://arxiv.org/abs/2205.10343))
2. Generalizations from one tas
k can increase the performance on another unrelated task, increasing its overall performance (recent paper shows that GP
T models get better at chess and reasoning by looking at the emergent behaviour of cellular automata: [Intelligence at t
he Edge of Chaos (arxiv.org)](https://arxiv.org/html/2410.02536)).

But then what happens if we grok the model not on a 
specific task, but on all its data? We can imagine that it would just memorize the whole dataset, without being incentiv
ised to make generalization since it now has near perfect performance on the whole dataset. In this case, where the glob
al minima is memorization, the model can still reach generalization by changing the loss landscape using weight-decay / 
regularization. Regularization punishes big weights, forcing the model to prefer simpler solutions, reducing the minima 
around memorization, while leaving the minima around generalization in tact. This will make generalization the new globa
l minima.

Considering this convergence towards generalization over training time, for both task-specific as overall per
formance, could we assume that scaling will logically make models generalize over time? In other words, is scale really 
all we need to AGI? 
```
---

     
 
all -  [ [D] Will Scale be enough to get LLMs to Reason through Grokking? ](https://www.reddit.com/r/MachineLearning/comments/1g3cumr/d_will_scale_be_enough_to_get_llms_to_reason/) , 2024-10-18-0912
```
Currently there has been a lot of debate whether LLMs truly reason or just memorize their training data (see this recent
 paper from Apple [\[2410.05229\] GSM-Symbolic: Understanding the Limitations of Mathematical Reasoning in Large Languag
e Models (arxiv.org)](https://arxiv.org/abs/2410.05229)).

On the other hand, there has been numerous papers showing tha
t models can generalize, if trained beyond the point where they overfit, known as '**grokking**' ([Towards Understanding
 Grokking: An Effective Theory of Representation Learning (neurips.cc)](https://proceedings.neurips.cc/paper_files/paper
/2022/hash/dfc310e81992d2e4cedc09ac47eff13e-Abstract-Conference.html)).

Based on grokking, we could argue that if we ju
st train current LLMs enough, they will always converge to generalization. Seemingly, **memorization is just a local min
ima** in which it can get stuck, and the true **global minima is generalization**.

How is this possible if memorization
 is already giving near perfect performance on the dataset for a **specific task**? Well, by looking at overall performa
nce opposed to task-specific performance, you can imagine how generalizing helps the model increase its overall performa
nce:

1. Generalizations use less parameter space than memorization, which the model then can use for other tasks, incre
asing its overall performance (reduction in effective dimension by generalization [\[2205.10343\] Towards Understanding 
Grokking: An Effective Theory of Representation Learning (arxiv.org)](https://arxiv.org/abs/2205.10343))
2. Generalizati
ons from one task can increase the performance on another unrelated task, increasing its overall performance (recent pap
er shows that GPT models get better at chess and reasoning by looking at the emergent behaviour of cellular automata: [I
ntelligence at the Edge of Chaos (arxiv.org)](https://arxiv.org/html/2410.02536)).

But then what happens if we grok the
 model not on a specific task, but on **all its data**? We can imagine that it would just memorize the whole dataset, wi
thout being incentivised to make generalization since it now has near perfect performance on the whole dataset. In this 
case, where the **global minima is memorization**, the model can still reach generalization by changing the loss landsca
pe using **weight-decay / regularization**. Regularization punishes big weights, forcing the model to prefer simpler sol
utions, reducing the minima around memorization, while leaving the minima around generalization in tact. This will make 
generalization the new global minima.

Considering this convergence towards generalization over training time, for both 
task-specific as overall performance, could we assume that scaling will logically make models generalize over time? In o
ther words, is scale really all we need to AGI? Or is there a flaw in my reasoning, grokking is not the end-all-be-all a
nd we will need new breakthroughs to get to AGI?
```
---

     
 
all -  [ University Recommendations for AI/ML Specialization in Europe ](https://www.reddit.com/r/learnmachinelearning/comments/1g39xgf/university_recommendations_for_aiml/) , 2024-10-18-0912
```
Hi everyone,

I’m a 25-year-old ML Engineer from India with a Bachelor's in CS from a tier-3 college (8.56 CGPA). I have
 4 years of experience working in a French telecom organization, focusing on pure research projects. My work has led to 
2 research papers (one at a main conference and one workshop paper) in IEEE NOMS, as well as a tutorial I presented at I
CIN, Paris. Most of my research revolves around Reinforcement Learning (RL).

# Career Goals:

I aim to pursue a career 
in intensive research roles in AI/ML. My long-term goal is to get a PhD in RL and control theory. However, I want to fir
st build a solid foundation, especially in the underlying mathematics, by completing a master’s program in AI/ML.

# Why
 Europe?

I’m leaning toward Europe over the US for a few reasons:

* I plan to eventually live and work in Europe.
* Pr
oximity to family in India.
* The lower cost of master’s programs.

# Excluding the UK for Master's:

I am not consideri
ng the UK due to the shorter 1-year Master's program duration, which I feel may be insufficient, and the higher costs. I
 may go to the UK if it is for a PhD.

# What I’m Looking For:

I'm seeking universities in Europe with strong internati
onal reputations and rankings that can provide a good pathway to a PhD. So far, I’m considering:

* University of Amster
dam
* ETH Zurich
* EPFL

I’ve been basing my choices on QS rankings and the number of publications these universities ha
ve in key AI/ML conferences (e.g., NeurIPS, ICML).

I am targeting Autumn 2025 admission. Considering the low acceptance
 rates of ETH and EPFL and approaching deadlines for them. I’d love to hear any recommendations for other universities I
 should consider.

P.S. Can someone throw the light on whether I go for PhD directly or should pursue a master's first? 
I feel if I go for PhD directly, I will be left with some knowledge gap.
```
---

     
 
all -  [ Chance an underperforming Asian ](https://www.reddit.com/r/chanceme/comments/1g35v1n/chance_an_underperforming_asian/) , 2024-10-18-0912
```
**Demographics**:

* mid to low comp HS, 250 ish grad class
* Asian
* I play chess?
* Econ or CS

**GPA**: 3.7 W(Struggl
ed with Depression and certain tendencies, bounced around therapist offices freshman sophomore year. Locked in and made 
drastic improvements in gpa)

No rank

7 APs, 8 Tests

SAT - 1510 composite

**Awards**:

* AP scholar with honors
* hon
or roll
* Top 100 nationally ranked chess players In age groups for the past 4 years
* USCF candidate master
* top 1k [c
hess.com](http://chess.com) rapid global?(idk if I want to add this)

**ECs(nốt ordered yet):**

* High School Chess lea
gue president - 20+ schools, 100+ participants,  $1k+ raised
* 1st author to Novel Ai paper - published and submitted to
 conferences like Neurips + COLING
* Chess Club president - 3 peat champion in regional league, top 5 teams in State
* D
ECA - 3x state qualifier
* Motorola Solutions Intern - made a REST API for one of their apps in prod
* Paid Chess coach 
- Apart of non-profit group for underprivileged youth in chicago(not from there did remote)
* Volunteer Chess Coach - vo
lunteered apart of local chess academy, 200 ish hours over the 4 years
* Wrestling - Varsity
* SASA(south asian student 
association) treasurer - raised 10k from sponsors and events, provided scholarships for the first year to south asian st
udents
* Inspirit AI scholars program(free) - Made Chess bot with GPT 4o capable of playing at an expert level

**Colleg
es**:  
Udubs, Umass, Umich, UMD, UW Madison, BC, BU, NEU, Ohio State, Penn State, Purdue, IU, Vtech, UPitt, RIT, Bentle
y

Majors are varied between Econ or CS with focus in AI
```
---

     
 
all -  [ NeurIPS 2024 Workshop on Creativity & Generative AI | NeurIPS 2024 Workshop on Generative AI and Cre ](https://creativity-ai.github.io/) , 2024-10-18-0912
```

```
---

     
 
all -  [ Low Undergrad Gpa decent exp? concerned about my chances? Should I do Gre? ](https://www.reddit.com/r/gradadmissions/comments/1fzj4wb/low_undergrad_gpa_decent_exp_concerned_about_my/) , 2024-10-18-0912
```
Hey guys  
I am an undergrad in ECE at a top 5 school with a 3.37 GPA and internship experience at a FAANG company. I am
 also waiting on a decision on a paper that might be accepted at a NeurIPS workshop. The GPA has been bothering me a bit
 as to getting auto-rejected from master's programs. So far, I have narrowed down

UIUC MCS

Georgia Tech MS CS

Univers
ity of Michigan MS CS

UC Berkeley MEng

Carnegie Mellon MEng

Brown University MEng

University of Washington MS CS

Co
rnell MEng

Columbia MEng

NYU Tandon MS CS

UCSD MS CS

USC MS CS

Would love to hear any feedback on my school list or
 advice for someone with my GPA and background!
```
---

     
 
all -  [ [Article] HiCoM: Hierarchical Coherent Motion for Dynamic Streamable Scenes with 3D Gaussian Splatti ](https://www.reddit.com/r/Scholar/comments/1fzgn8o/article_hicom_hierarchical_coherent_motion_for/) , 2024-10-18-0912
```
NeurIPS [https://nips.cc/virtual/2024/poster/96081](https://nips.cc/virtual/2024/poster/96081)
```
---

     
 
all -  [ Some Research Papers We Read recently ](https://www.reddit.com/r/deeplearning/comments/1fy6enm/some_research_papers_we_read_recently/) , 2024-10-18-0912
```
Hey everyone, here is the list of papers we discussed and their summaries this week. If you find these summaries useful,
 feel free to contribute your own! The repo is constantly updated with new papers from major conferences, so it's a grea
t way to keep up with the latest AI and deep learning.

* Image Hijacks: Adversarial Images Can Control Generative Model
s at Runtime 👉 [Summary](https://github.com/vlgiitr/papers_we_read/blob/master/summaries/Image_Hijacks.md)
* AI Control:
 Improving Safety Despite Intentional Subversion 👉 [Summary](https://github.com/vlgiitr/papers_we_read/blob/master/summa
ries/AI_Control.md)
* Evaluating Text-to-Visual Generation with Image-to-Text Generation 👉 [Summary](https://github.com/
vlgiitr/papers_we_read/blob/master/summaries/VQAscore.md)
* WARM: On the Benefits of Weight Averaged Rewarded Model 👉 [S
ummary](https://github.com/vlgiitr/papers_we_read/blob/master/summaries/WARM.md)

**The Vision Language Group at IIT Roo
rkee** has put together an excellent repository of **comprehensive summaries** for deep learning papers from top confere
nces like **NeurIPS, CVPR, ICCV, and ICML (2016-2024)**. These summaries break down key papers in computer vision, NLP, 
and machine learning—perfect if you want to stay updated without diving deep into the full papers.

📂 **Check out the fu
ll repo and contribute he**re  
[Vision Language Group Paper Summaries](https://github.com/vlgiitr/papers_we_read)

Happ
y reading! 🎉
```
---

     
 
all -  [ Some Research Papers We Read recently ](https://www.reddit.com/r/u_vlg_iitr/comments/1fy6a5e/some_research_papers_we_read_recently/) , 2024-10-18-0912
```
Hey everyone, here is the list of papers we discussed and their summaries this week. If you find these summaries useful,
 feel free to contribute your own! The repo is constantly updated with new papers from major conferences, so it's a grea
t way to keep up with the latest AI and deep learning.

* Image Hijacks: Adversarial Images Can Control Generative Model
s at Runtime 👉 [Summary](https://github.com/vlgiitr/papers_we_read/blob/master/summaries/Image_Hijacks.md)
* AI Control:
 Improving Safety Despite Intentional Subversion 👉 [Summary](https://github.com/vlgiitr/papers_we_read/blob/master/summa
ries/AI_Control.md)
* Evaluating Text-to-Visual Generation with Image-to-Text Generation 👉 [Summary](https://github.com/
vlgiitr/papers_we_read/blob/master/summaries/VQAscore.md)
* WARM: On the Benefits of Weight Averaged Rewarded Model 👉 [S
ummary](https://github.com/vlgiitr/papers_we_read/blob/master/summaries/WARM.md)

**The Vision Language Group at IIT Roo
rkee** has put together an excellent repository of **comprehensive summaries** for deep learning papers from top confere
nces like **NeurIPS, CVPR, ICCV, and ICML (2016-2024)**. These summaries break down key papers in computer vision, NLP, 
and machine learning—perfect if you want to stay updated without diving deep into the full papers.

  
📂 **Check out the
 full repo and contribute her**e  
[Vision Language Group Paper Summaries](https://github.com/vlgiitr/papers_we_read)

H
appy reading! 🎉
```
---

     
 
all -  [ [0 YoE, Student, ML Research/SWE Internship, USA] ](https://www.reddit.com/r/resumes/comments/1fy0sj4/0_yoe_student_ml_researchswe_internship_usa/) , 2024-10-18-0912
```
Hi! I've never made a resume before, so this one isn't ATS optimized yet, way too long, and imo very uninteresting for a
n interviewer or recruiter to look at. I'm in my junior year, so it's the time to fix all that for internships and resea
rch for the coming summer. Specifically, I'm looking to apply to both corporate SWE/ML-related internships, as well as a
ny research opportunities that comes up as I'm not fully decided on grad school vs job post-university. Even though the 
resume is really unpolished right now, I appreciate the help a ton and please be really honest on it so i can make it as
 good as possible. Thanks!

https://preview.redd.it/4rh7hwqhx9td1.jpg?width=827&format=pjpg&auto=webp&s=c061fe2d0687f870
ba5f0d7efeeb8b3e7d55fe46

https://preview.redd.it/619j8nqhx9td1.jpg?width=827&format=pjpg&auto=webp&s=77fe2509aa62505277
4ae5dd61dc537568ae7184

P.S. couple of specific things I'm a bit questionable on. Namely, the job titles - they feel lik
e a bit inflated, but like for the Expii one, I was literally the first SWE person there as it was a startup, and I hand
led the hiring and training and lead the rest of the team myself. So when i asked my old boss, he just told me to write 
principal swe and call it a day. Same with being a 'researcher', i'm first author and heading the lab group myself with 
a couple advisors. But im concerned that people will see i'm a student and and writing these titles and take it that I'm
 overstating my roles, so idk if i should just bump them down to 'student researcher' or like 'SWE intern' or something.
 Also the skills section is gross, but idk what to do with it. Thanks again!!!  

```
---

     
 
all -  [ Are IEEE/CVF the top conferences for CV/Image Processing? ](https://www.reddit.com/r/computervision/comments/1fxfwpo/are_ieeecvf_the_top_conferences_for_cvimage/) , 2024-10-18-0912
```
As the title say, are IEEE/CVF to CV what ICLR, ICML, NeurIPS are to AI?
```
---

     
 
all -  [ approved I797-A but expired visa stamp; travel to Canada for 6 days? ](https://www.reddit.com/r/h1b/comments/1fx81is/approved_i797a_but_expired_visa_stamp_travel_to/) , 2024-10-18-0912
```
Hi, my H1-B visa stamp on my passport expired on Aug 6, 2023.

I have an approved I797-A (H1-B) valid from 05/11/2023 to
 04/19/2026.

Prior to the my latest (and current) I797-A, I also have an approved I-140 (notice date 2022). I was on H1
-B from 2017-2020 and then 2020-2023 before. Before my H1-B I was on F-1 status.

Can I travel to Canada to present at N
eurIPS 2024 conference on Dec 9, 2024 – Dec 15, 2024, and will I be allowed to enter USA with my approved I797-A without
 the visa stamp.

I have seen other posts on automatic visa revalidation and also saw the page [https://travel.state.gov
/content/travel/en/us-visas/visa-information-resources/visa-expiration-date/auto-revalidate.html](https://travel.state.g
ov/content/travel/en/us-visas/visa-information-resources/visa-expiration-date/auto-revalidate.html) but don't understand
 everything on the page clearly.

I am scared because if I can't enter back in USA, then I would have to go back to Indi
a, wait for appointment to get my visa stamped and my wife and 15-months daughter would be alone here in USA.

Travel wi
ll be via flight. Please advise.
```
---

     
 
all -  [ Consent in Crisis (NeurIPS 2024) Paper Summary via DeepDive ](https://www.reddit.com/r/learnmachinelearning/comments/1fwpt7r/consent_in_crisis_neurips_2024_paper_summary_via/) , 2024-10-18-0912
```
[https://www.youtube.com/watch?v=1I-ABssKrps](https://www.youtube.com/watch?v=1I-ABssKrps)
```
---

     
 
all -  [ LASR Labs (technical AIS research programme) applications open until Oct 27th ](https://www.reddit.com/r/ControlProblem/comments/1fw5k1d/lasr_labs_technical_ais_research_programme/) , 2024-10-18-0912
```
🚨**LASR Labs: Spring research programme in AI Safety** 🚨

**When:** Apply by October 27th. Programme runs 10th February-
 9th May. 

**Where:** London 

**Details & Application:** [https://www.lesswrong.com/posts/SDatnjKNyTDGvtCEH/lasr-labs-
spring-2025-applications-are-open](https://www.lesswrong.com/posts/SDatnjKNyTDGvtCEH/lasr-labs-spring-2025-applications-
are-open) 



**What is it?** 

A full-time, 13 week paid (£11k stipend) research programme for people interested in car
eers in technical AI safety. Write a paper as part of a small team with supervision from an experienced researcher. **Pa
st alumni have gone on to Open AI dangerous capability evals team, UK AI Safety Institute or continued working with thei
r supervisors. In 2023, 4 out of 5 groups had papers accepted to workshops or conferences (ICLR, NeurIPS).**  



**Who 
should apply?** 

We’re looking for candidates with \~2 years experience in relevant postgraduate programmes or industry
 roles (Physics, Math or CS PhD, Software engineering, Machine learning, etc). You might be a good fit if you’re excited
 about:

* Producing empirical work, in an academic style
* Working closely in a small team




```
---

     
 
all -  [ [D] Option to make NeurIPS rejected paper reviews public? ](https://www.reddit.com/r/MachineLearning/comments/1fvy0n4/d_option_to_make_neurips_rejected_paper_reviews/) , 2024-10-18-0912
```
The decision notification e-mail from NeurIPS mentioned that we would be offered the option to opt in to publicly releas
ing reviews for a rejected paper and that instructions would follow in a few days.

It's been over a week and we have no
t yet received any e-mail nor is there any author task to opt in. Since last year this e-mail came only 3 days after the
 notification I'm wondering if there was some issue and if no1 has received the e-mail yet?


```
---

     
 
all -  [ [R] Announcing the first series of Liquid Foundation Models (LFMs) – a new generation of generative  ](https://www.reddit.com/r/MachineLearning/comments/1fvgo7o/r_announcing_the_first_series_of_liquid/) , 2024-10-18-0912
```
https://www.liquid.ai/liquid-foundation-models

https://www.liquid.ai/blog/liquid-neural-networks-research

https://x.co
m/LiquidAI_/status/1840768716784697688

https://x.com/teortaxesTex/status/1840897331773755476

'We announce the first se
ries of Liquid Foundation Models (LFMs), a new generation of generative AI models built from first principles.

Our 1B, 
3B, and 40B LFMs achieve state-of-the-art performance in terms of quality at each scale, while maintaining a smaller mem
ory footprint and more efficient inference.'

'LFM-1B performs well on public benchmarks in the 1B category, making it t
he new state-of-the-art model at this size. This is the first time a non-GPT architecture significantly outperforms tran
sformer-based models.

LFM-3B delivers incredible performance for its size. It positions itself as first place among 3B 
parameter transformers, hybrids, and RNN models, but also outperforms the previous generation of 7B and 13B models. It i
s also on par with Phi-3.5-mini on multiple benchmarks, while being 18.4% smaller. LFM-3B is the ideal choice for mobile
 and other edge text-based applications.

LFM-40B offers a new balance between model size and output quality. It leverag
es 12B activated parameters at use. Its performance is comparable to models larger than itself, while its MoE architectu
re enables higher throughput and deployment on more cost-effective hardware.

LFMs are large neural networks built with 
computational units deeply rooted in the theory of dynamical systems, signal processing, and numerical linear algebra.


LFMs are Memory efficient LFMs have a reduced memory footprint compared to transformer architectures. This is particular
ly true for long inputs, where the KV cache in transformer-based LLMs grows linearly with sequence length.

LFMs truly e
xploit their context length: In this preview release, we have optimized our models to deliver a best-in-class 32k token 
context length, pushing the boundaries of efficiency for our size. This was confirmed by the RULER benchmark.

LFMs adva
nce the Pareto frontier of large AI models via new algorithmic advances we designed at Liquid: 
 
Algorithms to enhance 
knowledge capacity, multi-step reasoning, and long-context recall in models + algorithms for efficient training and infe
rence.

We built the foundations of a new design space for computational units, enabling customization to different moda
lities and hardware requirements.

What Language LFMs are good at today:
General and expert knowledge,
Mathematics and l
ogical reasoning,
Efficient and effective long-context tasks,
A primary language of English, with secondary multilingual
 capabilities in Spanish, French, German, Chinese, Arabic, Japanese, and Korean.

What Language LFMs are not good at tod
ay:
Zero-shot code tasks,
Precise numerical calculations,
Time-sensitive information,
Counting r’s in the word “Strawber
ry”!,
Human preference optimization techniques have not yet been applied to our models, extensively.'

'We invented liqu
id neural networks, a class of brain-inspired systems that can stay adaptable and robust to changes even after training 
[R. Hasani, PhD Thesis] [Lechner et al. Nature MI, 2020] [pdf] (2016-2020). We then analytically and experimentally show
ed they are universal approximators [Hasani et al. AAAI, 2021], expressive continuous-time machine learning systems for 
sequential data [Hasani et al. AAAI, 2021] [Hasani et al. Nature MI, 2022], parameter efficient in learning new skills [
Lechner et al. Nature MI, 2020] [pdf], causal and interpretable [Vorbach et al. NeurIPS, 2021] [Chahine et al. Science R
obotics 2023] [pdf], and when linearized they can efficiently model very long-term dependencies in sequential data [Hasa
ni et al. ICLR 2023].

In addition, we developed classes of nonlinear neural differential equation sequence models [Mass
aroli et al. NeurIPS 2021] and generalized them to graphs [Poli et al. DLGMA 2020]. We scaled and optimized continuous-t
ime models using hybrid numerical methods [Poli et al. NeurIPS 2020], parallel-in-time schemes [Massaroli et al. NeurIPS
 2020], and achieved state-of-the-art in control and forecasting tasks [Massaroli et al. SIAM Journal] [Poli et al. Neur
IPS 2021][Massaroli et al. IEEE Control Systems Letters]. The team released one of the most comprehensive open-source li
braries for neural differential equations [Poli et al. 2021 TorchDyn], used today in various applications for generative
 modeling with diffusion, and prediction.

We proposed the first efficient parallel scan-based linear state space archit
ecture [Smith et al. ICLR 2023], and state-of-the-art time series state-space models based on rational functions [Parnic
hkun et al. ICML 2024]. We also introduced the first-time generative state space architectures for time series [Zhou et 
al. ICML 2023], and state space architectures for videos [Smith et al. NeurIPS 2024]

We proposed a new framework for ne
ural operators [Poli et al. NeurIPS 2022], outperforming approaches such as Fourier Neural Operators in solving differen
tial equations and prediction tasks.

Our team has co-invented deep signal processing architectures such as Hyena [Poli 
et al. ICML 2023] [Massaroli et al. NeurIPS 2023], HyenaDNA [Nguyen et al. NeurIPS 2023], and StripedHyena that efficien
tly scale to long context. Evo [Nguyen et al. 2024], based on StripedHyena, is a DNA foundation model that generalizes a
cross DNA, RNA, and proteins and is capable of generative design of new CRISPR systems.

We were the first to scale lang
uage models based on both deep signal processing and state space layers [link], and have performed the most extensive sc
aling laws analysis on beyond-transformer architectures to date [Poli et al. ICML 2024], with new model variants that ou
tperform existing open-source alternatives. 

The team is behind many of the best open-source LLM finetunes, and merges 
[Maxime Lebonne, link].

Last but not least, our team’s research has contributed to pioneering work in graph neural netw
orks and geometric deep learning-based models [Lim et al. ICLR 2024], defining new measures for interpretability in neur
al networks [Wang et al. CoRL 2023], and the state-of-the-art dataset distillation algorithms [Loo et al. ICML 2023].'
```
---

     
 
all -  [ Bringing Learning to Rank to Reddit - LTR modeling ](https://www.reddit.com/r/RedditEng/comments/1ft1tkw/bringing_learning_to_rank_to_reddit_ltr_modeling/) , 2024-10-18-0912
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

     
 
all -  [ MSCS FALL'25 Profile evaluation ](https://www.reddit.com/r/MSCS/comments/1ft08a6/mscs_fall25_profile_evaluation/) , 2024-10-18-0912
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

     
 
all -  [ [D] Resources for staying updated on recent papers ](https://www.reddit.com/r/MachineLearning/comments/1fsx8q2/d_resources_for_staying_updated_on_recent_papers/) , 2024-10-18-0912
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

     
 
all -  [ [R] optimizing transformers ](https://www.reddit.com/r/MachineLearning/comments/1fsgz5i/r_optimizing_transformers/) , 2024-10-18-0912
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

     
 
all -  [ LEGO Meets AI: BricksRL Accepted at NeurIPS 2024! ](https://www.reddit.com/r/reinforcementlearning/comments/1fpebw9/lego_meets_ai_bricksrl_accepted_at_neurips_2024/) , 2024-10-18-0912
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

     
 
all -  [ [D] NeurIPS 2024 Review Question  ](https://www.reddit.com/r/MachineLearning/comments/1fpa7ua/d_neurips_2024_review_question/) , 2024-10-18-0912
```
My initial reviewers addressed some weaknesses & concerns, but these were resolved in my rebuttals. They acknowledged an
d raised their score. 

My paper was ultimately rejected because the program chair introduced new weaknesses that are a 
result of misreading the paper, if these were stated in the original reviews, this would easily be resolved. Is there an
ything I can do to fix this program chair review?
```
---

     
 
all -  [ [D] - NeurIPS 2024 Decisions ](https://www.reddit.com/r/MachineLearning/comments/1foky4r/d_neurips_2024_decisions/) , 2024-10-18-0912
```
Hey everyone! Just a heads up that the NeurIPS 2024 decisions notification is set for September 26, 2024, at 3:00 AM CES
T. I thought it’d be cool to create a thread where we can talk about it.
```
---

     
 
all -  [ Should I go for a masters, professional masters, or PhD? ](https://www.reddit.com/r/gradadmissions/comments/1foc03f/should_i_go_for_a_masters_professional_masters_or/) , 2024-10-18-0912
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

     
 
all -  [ Post-Doc Position in Intersection of LLMs/Reasoning/Data at Stanford Scaling Intelligence Lab ](https://www.reddit.com/r/CompSocial/comments/1fnnziy/postdoc_position_in_intersection_of/) , 2024-10-18-0912
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

     
 
all -  [ Looking at quant jobs from unconventional path ](https://www.reddit.com/r/FinancialCareers/comments/1fnefe2/looking_at_quant_jobs_from_unconventional_path/) , 2024-10-18-0912
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

     
 
all -  [ Summaries Of Research Papers We Read ](https://www.reddit.com/r/deeplearning/comments/1fl4bzm/summaries_of_research_papers_we_read/) , 2024-10-18-0912
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

     
 
all -  [ [R] Some Research Papers We Read ](https://www.reddit.com/r/MachineLearning/comments/1fl4bi0/r_some_research_papers_we_read/) , 2024-10-18-0912
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

     
 
all -  [ Summaries of some Research Papers we read! ](https://www.reddit.com/r/neuralnetworks/comments/1fl4al2/summaries_of_some_research_papers_we_read/) , 2024-10-18-0912
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

     
 
all -  [ Comprehensive Summaries of Paper We Read ](https://www.reddit.com/r/u_vlg_iitr/comments/1fl48qg/comprehensive_summaries_of_paper_we_read/) , 2024-10-18-0912
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

     
 
all -  [ [R] Erasing the Invisible: A Stress-Test Challenge for Image Watermarks (NeurIPS 2024 Competition) ](https://www.reddit.com/r/MachineLearning/comments/1fk90gj/r_erasing_the_invisible_a_stresstest_challenge/) , 2024-10-18-0912
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

     
 
all -  [ How to get into CS/AI related research and get a paper published in a top international publication  ](https://www.reddit.com/r/Indian_Academia/comments/1fjy5bt/how_to_get_into_csai_related_research_and_get_a/) , 2024-10-18-0912
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

     
