 
all -  [ I am not aware that we have so many outstanding PhDs on the job market. ](https://i.redd.it/egc3me1vkjpc1.png) , 2024-03-22-0909
```

```
---

     
 
all -  [ [D] simple typos or errors in my understanding?! ](https://www.reddit.com/r/MachineLearning/comments/1bicphu/d_simple_typos_or_errors_in_my_understanding/) , 2024-03-22-0909
```
Though I mailed to all authors, I couldn't receive any reply...

&#x200B;

I really enjoyed reading paper, “Compositiona
l Visual Generation with Energy Based Models” (NeurIPS\`20; [https://arxiv.org/abs/2004.06030](https://arxiv.org/abs/200
4.06030)).

While I am following the idea in the paper, I am facing a problem in understanding the equation (8) in the p
aper.

According to the paper's notation, the EBM is defined as (1):

[Eq. \(1\)](https://preview.redd.it/lnerbdlm58pc1.
png?width=202&format=png&auto=webp&s=e7ce768304cafa8e0fb88202466ad7cf40d9d3e8)

i.e.,, the *energy function*, E\_\\theta
(x), is defined as the negative term on top of the exponent.

&#x200B;

In eq. (3) below, authors defines SGLD step for 
acquiring samples from any energy based model (EBM).

Next, according to 'concept disjunction' proposed by authors, the 
union-ized probability densities are defined in (7), in the form of the exponential of log-sum-exp of different EBMs' *e
nergy function*s.

https://preview.redd.it/sas3f4yg58pc1.png?width=1005&format=png&auto=webp&s=2bb0aa67cf2767ede091102ce
22965e8c8bdbe7c

From (7), I understood that the unionized energy function is accordingly -logsumexp(-E(x|c1), ...),  
t
hus corresponding SGLD should have plus sign.  
However, in the paper, authors stated the SGLD with ***minus sign***, an
d I've lost...

After looking through the official code implementation,   
([https://github.com/yilundu/ebm\_composition
ality/blob/c7ac54366d2d5a15f71871448bd720bf5b3eb82d/celeba\_combine.py#L150C9-L150C32](https://github.com/yilundu/ebm_co
mpositionality/blob/c7ac54366d2d5a15f71871448bd720bf5b3eb82d/celeba_combine.py#L150C9-L150C32))  
I found that the combi
ned energy function derivation of mine ( E(x|\\cup\_i c\_i) ) seems to be correct,  
according to the assignment of the 
\`e\_pos\` variable in the code.

&#x200B;

Still, I'd like to acquire some clarification on this flow.  
Can anybody sk
im through this post and check my thought?

Thank you in advance!
```
---

     
 
all -  [ Stanford MS/CS 2024 - REJECTED ](https://www.reddit.com/r/gradadmissions/comments/1bhwguc/stanford_mscs_2024_rejected/) , 2024-03-22-0909
```
I unfortunately got denied from Online Stanford MS in CS Today. I was fairly confident in my application. I had 4.00/4.0
0 GPA (ranked 1st in my graduation class from decent US college), ML Engineer at FAANG, published a paper in NeurIPS. My
 references include Dean of Engineering, My college Prof (Oxford grad) and my manager from work - MIT (PhD). I had alrea
dy got rejected 2 years ago, since then I made a publication switched to an ML oriented role and tailored my referrals a
ccordingly. It makes sense that a lot of people flooded in to AI track this year but I really want to get a sense of oth
er profiles who got admitted this year.

Maybe next year I will try again :/
```
---

     
 
all -  [ [D] papers that only evaluate on cifar10 ](https://www.reddit.com/r/MachineLearning/comments/1bhp54a/d_papers_that_only_evaluate_on_cifar10/) , 2024-03-22-0909
```
Hi everyone!

While reviewing for NeurIPS 2024, one of the things I keep noticing is that a lot of papers only evaluate 
on datasets of very small size, like Cifar-10. his feels weird to me: I consider Cifar10 to be a toy-dataset and testbed
 for my methods, not something I'd use to show that my method actually works/is relevant in practice. So my first intuit
ion is always 'this approach probably does not scale to larger datasets'. I mean, ImageNet is 12 years old now, and I've
 personally been giving results on imagenet for my papers since ~8 years. most computer vision applications I know requi
re larger resolutions than just 32x32. it's also my impression that almost all of the 'good' papers I read have results 
on larger scale data. But given how often I encounter this situation, I have to wonder: am  I just working in a very pri
vileged environment, or are the manuscript-authors just lazy? How much faith do you have in papers that only evaluate on
 MNIST and CIFAR10?
```
---

     
 
all -  [ Towards General-Purpose In-Context Learning Agents ](https://www.reddit.com/r/AcceleratingAI/comments/1bfbbvj/towards_generalpurpose_incontext_learning_agents/) , 2024-03-22-0909
```
**Paper**: [https://openreview.net/forum?id=eDZJTdUsfe](https://openreview.net/forum?id=eDZJTdUsfe)

**Talk and slides**
: [https://neurips.cc/virtual/2023/79880](https://neurips.cc/virtual/2023/79880)

**Blog post**: [http://louiskirsch.com
/glas](http://louiskirsch.com/glas)

**Abstract**:

>Reinforcement Learning (RL) algorithms are usually hand-crafted, dr
iven  by the research and engineering of humans. An alternative approach is to  automate this research process via meta-
learning. A particularly  ambitious objective is to automatically discover new RL algorithms from  scratch that use in-c
ontext learning to learn-how-to-learn entirely from  data while also generalizing to a wide range of environments. Those
 RL  algorithms are implemented entirely in neural networks, by conditioning  on previous experience from the environmen
t, without any explicit  optimization-based routine at meta-test time. To achieve generalization,  this requires a broad
 task distribution of diverse and challenging  environments. Our Transformer-based **Generally Learning Agents** (**GLAs
**) are  an important first step in this direction. Our GLAs are meta-trained  using supervised learning techniques on a
n offline dataset with  experiences from RL environments that is augmented with random  projections to generate task div
ersity. During meta-testing our agents  perform in-context meta-RL on entirely different robotic control  problems such 
as Reacher, Cartpole, or HalfCheetah that were not in the  meta-training distribution.
```
---

     
 
all -  [ 2 yoe in research labs only in computer vision. What should be my next steps? ](https://www.reddit.com/r/cscareerquestionsEU/comments/1bdslud/2_yoe_in_research_labs_only_in_computer_vision/) , 2024-03-22-0909
```
Hi,
Based in France. I have a masters where I did 2 internships in a good research lab and then started working as resea
rch engineer in a public lab for ~2 years. They only offer temporary contracts and there is a limit to how long you can 
work with these temporary contracts in France (you can try for the few research scientists positions but jts if you have
 phd/post doc plus good publiching track and experience, so i need to move on).
I didn't go for a phd and don't want to 
now since I felt I didn't have the right motivation and didn't want to do it for the sake of it. Didn't see myself as a 
researcher either publishing all my life. Research Engineer is a sweet spot.

From internships/job, I've so far co-autho
red 4 papers in computer vision conferences (neurips, iccv, cvpr, miccai) in the topics of 3d reconstruction and human m
odeling. But that's pretty much the achievement which is probably meaningless for jobs in the industry. And thing is, I 
feel my skill stack being also limited to research workflow might be little interesting to the industry (practical exper
ience with only python vs c++ for example). 

And i feel i should switch to industry (instead of another contract in a r
esearch lab) since honestly, even though these papers might seem nothing, they take a lot of effort and work and the who
le publishing cycle drains you mentally. And the compensation you get is really low I feel in these public labs (32k bru
t).

When I look around for jobs, I see mostly poorly defined descriptions but titled data scientist or mainly MLops. No
thing specifically related to what ive done being needed. I have 7 months left on my contract. What should I start learn
ing/doing or what could be an ideal focus for job search with such profile? Id like to stay in France and even in the sa
me city near lyon since im a foreigner and i feel more settled due to having made friends and understanding the language
. Your insights would be helpful. I feel very lost.
```
---

     
 
all -  [ ML Internships aren't supposed to be this difficult to get - Rant ](https://www.reddit.com/r/cscareerquestions/comments/1bd940o/ml_internships_arent_supposed_to_be_this/) , 2024-03-22-0909
```
As an international master's student, I'm on the verge of quitting my search as my internship hunt for the past 8 months
 has practically given 0 offers. I've applied to over 600 postings (every single ML/DS posting that has come). I did get
 3-4 callbacks but they never converted to offers despite the interviews going well. All I can say is that the competiti
on is unbelievably high, and the companies seem to be taking just 1 intern per team or none. Every position I am interes
ted in requires a Ph.D. candidate or papers in conferences like ICML, NeurIPS, or CVPR on the exact niche area the team 
works on. When there's a lack of jobs and an abundant supply of candidates, they can get choosy. But these are internshi
ps we are talking about, things meant to be entry-level positions.

Is it actually supposed to be this difficult? The wo
rst part is that all the callbacks I got so far are through direct contact with the hiring manager. None of the regular 
applications(even with referrals) gave me anything. As a final plea, if any of my fellow Redditors here have leads I'd r
eally appreciate some help.
```
---

     
 
all -  [ People with no top-tier ML papers, where are you working at? ](https://www.reddit.com/r/reinforcementlearning/comments/1b1suv1/people_with_no_toptier_ml_papers_where_are_you/) , 2024-03-22-0909
```
I am graduating soon, and my Ph.D. research is about RL algorithms and their applications.  
However, I failed to publis
h papers in top-tier ML conferences (NeurIPS, ICLR, ICML).   
But with several papers in my domain, how can I get hired 
for an RL-related job?  
I have interviewed a handful of mobile and e-commerce (RecSys) companies, all failed.  


I don
't want to do a postdoc and I am not interested in anything related to academia.   


Please let me know if there are an
y opportunities in startups, or other positions I have not explored yet.
```
---

     
 
all -  [ Postdoc requirements ](https://www.reddit.com/r/PhD/comments/1b1i5vr/postdoc_requirements/) , 2024-03-22-0909
```
Hi colleagues,

In some of the postdoc or industrial research scientist positions i see requirements like this:  


* St
rong publications record at top tier venues (CVPR, ICCV, ECCV, Siggraph, etc.)
* We are looking for candidates with a st
rong track record at top-tier computer vision and machine learning venues, such as CVPR, ICCV, ECCV, and NeurIPS.
* Firs
t-authored publications at peer-reviewed conferences (e.g. CVPR. ECCV, ICCV, NeurIPS, and SIGGRAPH).

In case one joins 
robotics related PhD on vision and perception and would focus on publications on IROS, ICRA(these 2 are top robotics con
ference, which have vision section), will these publications be considered for above mentioned positions? Or only the me
ntioned top-tier computer vision only conferences are accepted?  
I do understand that robotics conferences are a little
 less competitive, but still they are top-tier and peer-reviewed. 
```
---

     
 
all -  [ Help! ](https://www.reddit.com/gallery/1az9fpc) , 2024-03-22-0909
```
I have stubborn texture and always get pimples on my chin area that just won’t go away anyone have tips or products that
 they use?TIA included what I use now thank you!!
```
---

     
 
all -  [ [R] 'Generative Models: What do they know? Do they know things? Let's find out!'. Quote from paper:  ](https://www.reddit.com/r/MachineLearning/comments/1ay2b7u/r_generative_models_what_do_they_know_do_they/) , 2024-03-22-0909
```
[Paper](https://arxiv.org/abs/2311.17137). [Project website](https://intrinsic-lora.github.io/). I am not affiliated wit
h the authors.

Abstract:

>Generative models have been shown to be capable of synthesizing highly detailed and realisti
c images. It is natural to suspect that they implicitly learn to model some image intrinsics such as surface normals, de
pth, or shadows. In this paper, we present compelling evidence that generative models indeed internally produce high-qua
lity scene intrinsic maps. We introduce Intrinsic LoRA (I LoRA), a universal, plug-and-play approach that transforms any
 generative model into a scene intrinsic predictor, capable of extracting intrinsic scene maps directly from the origina
l generator network without needing additional decoders or fully fine-tuning the original network. Our method employs a 
Low-Rank Adaptation (LoRA) of key feature maps, with newly learned parameters that make up less than 0.6% of the total p
arameters in the generative model. Optimized with a small set of labeled images, our model-agnostic approach adapts to v
arious generative architectures, including Diffusion models, GANs, and Autoregressive models. We show that the scene int
rinsic maps produced by our method compare well with, and in some cases surpass those generated by leading supervised te
chniques.

A figure from the paper:

https://preview.redd.it/uid7hrhcmckc1.jpg?width=722&format=pjpg&auto=webp&s=db5b3a9
9a80d229f48c78d63449445800769f3e3

Quotes from the paper:

>In this paper, our goal is to understand the underlying know
ledge present in all types of generative models. We employ Low-Rank Adaptation (LoRA) as a unified approach to extract s
cene intrinsic maps — namely, normals, depth, albedo, and shading — from different types of generative  models. Our meth
od, which we have named as INTRINSIC LORA (I-LORA), is general and applicable to diffusion-based models, StyleGAN-based 
models, and autoregressive generative models. Importantly, the additional weight parameters introduced by LoRA constitut
e less than 0.6% of the total weights of the pretrained generative model, serving as a form of feature modulation that e
nables easier extraction of latent scene intrinsics. By altering these minimal parameters and using as few as 250 labele
d images, we successfully extract these scene intrinsics.  
>  
>Why is this an important question? Our motivation is th
ree-fold. First, it is scientifically interesting to understand whether the increasingly realistic generations of large-
scale text-to-image models are correlated with a better understanding of the physical world, emerging purely from applyi
ng a generative objective on a large scale. Second, rooted in the saying 'vision is inverse graphics' – if these models 
capture scene intrinsics when generating images, we may want to leverage them for (real) image understanding. Finally, a
nalysis of what current models do or do not capture may lead to further improvements in their quality.

&#x200B;

>For s
urface normals, the images highlight the models’ ability to infer surface orientations and contours. The depth maps disp
lay the perceived distances within the images, with warmer colors indicating closer objects and cooler colors representi
ng further ones. Albedo maps isolate the intrinsic colors of the subjects, removing the influence of lighting and shadow
. Finally, the shading maps capture the interplay of light and surface, showing how light affects the appearance of diff
erent facial features.

&#x200B;

>We find consistent, compelling evidence that generative models implicitly learn physi
cal scene intrinsics, allowing tiny LoRA adaptors to extract this information with minimal fine-tuning on labeled data. 
More powerful generative models produce more accurate scene intrinsics, strengthening our hypothesis that learning this 
information is a natural byproduct of learning to generate images well. Finally, across various generative models and th
e self-supervised DINOv2, scene intrinsics exist in their encodings resonating with fundamental 'scene characteristics' 
as defined by Barrow and Tenenbaum.

[Twitter thread about paper from one of the authors](https://twitter.com/anand_bhat
tad/status/1730230190159135175).

From paper [StyleGAN knows Normal, Depth, Albedo, and More](https://arxiv.org/abs/2306
.00987) ([newer version PDF](https://proceedings.neurips.cc/paper_files/paper/2023/file/e7407ab5e89c405d28ff6807ffec594a
-Paper-Conference.pdf)) ([Twitter thread about paper)](https://twitter.com/anand_bhattad/status/1664798414318518274):

>
Barrow and Tenenbaum, in an immensely influential paper of 1978, defined the term 'intrinsic image' as 'characteristics 
– such as range, orientation, reflectance and incident illumination – of the surface element visible at each point of th
e image'. Maps of such properties as (at least) depth, normal, albedo, and shading form different types of intrinsic ima
ges. The importance of the idea is recognized in computer vision – where one attempts to recover intrinsics from images 
– and in computer graphics – where these and other properties are used to generate images using models rooted in physics
.

The 1978 paper mentioned in the previous paragraph: [Recovering intrinsic scene characteristics](https://www.sri.com/
publication/computer-vision-pubs/2d-3d-reasoning-and-augmented-reality-pubs/recovering-intrinsic-scene-characteristics-f
rom-images/):

>Abstract  
>  
>We suggest that an appropriate role of early visual processing is to describe a scene in
 terms of intrinsic (veridical) characteristics – such as range, orientation, reflectance, and incident illumination – o
f the surface element visible at each point in the image. Support for this idea comes from three sources: the obvious ut
ility of intrinsic characteristics for higher-level scene analysis; the apparent ability of humans, to determine these c
haracteristics, regardless of viewing conditions or familiarity with the scene, and a theoretical argument, that such a 
description is obtainable, by a non-cognitive and non-purposive process, at least, for simple scene domains. The central
 problem in recovering intrinsic scene characteristics is that the information is confounded in the original light-inten
sity image: a single intensity value encodes all of the characteristics of the corresponding scene point. Recovery depen
ds on exploiting constraints, derived from assumptions about the nature of the scene and the physics of the imaging proc
ess.

Language model GPT-4 Turbo explained normals, depth, albedo, and shading as follows:

>Normals: Imagine you have a
 smooth rubber ball with little arrows sticking out of it, pointing directly away from the surface. Each one of these li
ttle arrows is called a “normal.” In the world of 3D graphics and images, normals are used to describe how surfaces are 
oriented in relation to a light source. Knowing which way these arrows (normals) point tells the computer how light shou
ld hit objects and how it will make them look—whether shiny, flat, bumpy, etc.  
>  
>Depth: When you look at a scene, t
hings that are close to you seem larger and more detailed, and things far away seem smaller and less clear. Depth is all
 about how far away objects are from the viewpoint (like from a camera or your eyes). When computers understand depth, t
hey can create a 3D effect, make things look more realistic, and know which objects are in front of or behind others.  

>  
>Albedo: Have you ever painted a room in your house? Before the colorful paint goes on, there’s a base coat, usually
 white or gray. This base coat is sort of what albedo is about. It’s the basic, true color of a surface without any tric
ks of light or shadow messing with it. When looking at an apple, you know it’s red, right? That red color, regardless of
 whether you’re looking at it in bright sunshine or under a dim light, is the apple’s albedo.  
>  
>Shading: Think abou
t drawing a picture of a ball and then coloring it in to make it look real. You would darken one side to show that it’s 
farther from the light, and lighten the other side where the light shines on it. This play with light and dark, with dif
ferent tones, is what gives the ball a rounded, 3-dimensional look on the paper. Shading in images helps show how light 
and shadows fall on the surfaces of objects, giving them depth and shape so they don’t look flat.  
>  
>So, in the pape
r, the challenge they were addressing was how to get a computer to figure out these aspects—normals, depth, albedo, and 
shading—from a 2D image, which would help it understand a scene in 3D, much like the way we see the world with our own e
yes.
```
---

     
 
all -  [ Amorphous Fortress Online ](https://www.reddit.com/r/alife/comments/1axeoqq/amorphous_fortress_online/) , 2024-03-22-0909
```
Hi everyone!

I'd like to introduce a research project my team and I have been working on that's inspired by the Sims an
d Dwarf Fortress: [Amorphous Fortress Online](http://amorphous-fortress.xyz/index.php). It's an open-ended multi-agent s
imulation / game engine where you can design FSM-based AI that interact with each other in a small environment.

It's st
ill a work in development and the site has a user guide to help you get familiar with the interface and a feedback form 
to leave comments and report bugs. So far, we've published some research papers at a [ALIFE 2023](https://arxiv.org/pdf/
2306.13169.pdf) workshop and in a [NeurIPS 2023 workshop](https://arxiv.org/pdf/2312.02231.pdf) based on our Python vers
ion of the [engine](https://github.com/dipikarajesh18/amorphous-fortress).

Check out the [promo video](https://www.yout
ube.com/watch?v=ANoQkIgOa6c) and come design some fortresses!

&#x200B;

[Amorphous Fortress Online Promo](https://reddi
t.com/link/1axeoqq/video/4exdgqd9q6kc1/player)
```
---

     
 
all -  [ Is there any trick to help peg-in-hole tasks converge? ](https://www.reddit.com/r/reinforcementlearning/comments/1aw8399/is_there_any_trick_to_help_peginhole_tasks/) , 2024-03-22-0909
```
Hi!

I'm starting with a simple peg-in-hole task but it's hard to converge whether using dense or sparse reward.

For th
e sparse reward, the trick of random goal position is used in this [paper](https://proceedings.neurips.cc/paper_files/pa
per/2017/hash/453fadbd8a1a3af50a9df4df899537b5-Abstract.html) to help converge. Is there any **smart** trick that has be
en used to help converge for peg-in-hole tasks?

BTW, are there any recommended open-source repos regarding peg-in-hole 
tasks?

Any help would be appreciated! Thanks!
```
---

     
 
all -  [ [HIRING] Research Scholar (Technical Research) @ Centre for the Governance of AI in Oxford, UK (Hybr ](https://www.reddit.com/r/london_forhire/comments/1avlszu/hiring_research_scholar_technical_research_centre/) , 2024-03-22-0909
```
GovAI was founded to help humanity navigate the transition to a world with advanced AI. Our first research agenda, publi
shed in 2018, helped define and shape the nascent field of AI governance. Our team and affiliate community possess exper
tise in a wide variety of domains, including AI regulation, responsible development practices, compute governance, AI co
mpany corporate governance, US-China relations, and AI progress forecasting.  
GovAI researchers — particularly those wo
rking within our Policy Team — have closely advised decision makers in government, industry, and civil society. Our rese
archers have also published in top peer-reviewed journals and conferences, including International Organization, NeurIPS
, and Science. Our alumni have gone on to roles in government, in both the US and UK; top AI companies, including DeepMi
nd, OpenAI, and Anthropic; top think tanks, including the Centre for Security and Emerging Technology and RAND; and top 
universities, including the University of Oxford and the University of Cambridge.  
Although we are based in Oxford, Uni
ted Kingdom — and currently have an especially large UK policy focus — we also have team members in the United States an
d European Union.  
‍  
About the Role  
Research Scholar is a one-year visiting position. It is designed to support the
 career development of AI governance researchers and practitioners — as well as to offer them an opportunity to do high-
impact work.  
As a Research Scholar, you will have freedom to pursue a wide range of styles of work. This could include
 conducting policy research, social science research, or technical research; engaging with and advising policymakers; or
 launching and managing applied projects.   
For example, past and present Scholars have used the role to:  
produce an 
influential report on the benefits and risks of open-source AI;  
conduct technical research into questions that bear on
 compute governance;  
take part in the UK policy-making process as a part-time secondee in the UK government; and  
lau
nch a new organisation to facilitate international AI governance dialogues.  
Over the course of the year, you will also
 deepen your understanding of the field, connect with a network of experts, and build your skills and professional profi
le, all while working within an institutional home that offers both flexibility and support.  
You will receive research
 supervision from a member of the GovAI team or network. The frequency of supervisor meetings and feedback will vary dep
ending on supervisor availability, although once-a-week or once-every-two-weeks supervision meetings are typical. There 
will also be a number of additional opportunities for Research Scholars to receive feedback, including internal work-in-
progress seminars. You will receive further support from Emma Bluemke, GovAI's Research Manager.  
Some Research Scholar
s may also — depending on the focus of their work — take part in GovAI’s Policy Team, which is led by Markus Anderljung.
 Members of the GovAI Policy Team do an especially large amount of policy engagement and coordinate their work more subs
tantially. They also have additional team meetings and retreats. While Policy Team members retain significant freedom to
 choose projects, there is also an expectation that a meaningful portion of their work will fit into the team’s joint pr
iorities.

**Read more / apply:** [**https://ai-jobs.net/job/139016-research-scholar-technical-research/**](https://ai-j
obs.net/job/139016-research-scholar-technical-research/)

&#x200B;
```
---

     
 
all -  [ Do a Master Thesis that can into NeurIPS? ](https://www.reddit.com/r/careerguidance/comments/1avj9ch/do_a_master_thesis_that_can_into_neurips/) , 2024-03-22-0909
```
I'm in the process of deciding on my masters thesis in Data Science. The professor that I have been communicating with o
ffered me to join a team that would submit their research to NeurIPS. On the other hand, the topic of the research does 
not perfectly align with my interests (i.e., Quantitative Finance).

Should I pursue a thesis that would put a NeurIPS c
onference in my CV, or do a topic that is more related to my field of interest? Would like to know people's opinions and
 experiences, thanks!
```
---

     
