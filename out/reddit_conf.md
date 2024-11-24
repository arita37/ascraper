 
all -  [ Should I even apply for a PhD? ](https://www.reddit.com/r/PhD/comments/1gy1xp7/should_i_even_apply_for_a_phd/) , 2024-11-24-0914
```
Hi all

So I (23M, Indian) had the dream to pursue a MS+PhD in CS (AI) in the US (No masters, I just have a Bachelors de
gree in Electronics Engineering). I was aiming to get into universities like UCSD, John Hopkins, UIUC.

To make it happe
n, I applied to Indian professors and worked with them. Have spent over 1 year working in research, while managing my so
ftware engineering job in parallel. Got one paper published in ICPR 2024, and one in a small conference, not a big deal.
 I have managed to gather 3 Letters of Recommendation after working.

However, from some sample SOPs on the net, I see t
hat the applicants for these colleges have already 1st author publications in top-tier conferences like AAAI, NeurIPS et
c.

In this scenario, should I even apply? I feel like I have no chance to compete with these people. Am I aiming for to
o high? What would you suggest?

Thank you everyone.

  
Edit 1

Thank you everyone. I got overwhelmed by everything and
 became tensed. I will curate and apply. Whatever happens next, will happen. Let me do my part at least. thanks!
```
---

     
 
all -  [ Insight!  ](https://i.redd.it/3ub4hezgxl2e1.jpeg) , 2024-11-24-0914
```

```
---

     
 
all -  [ [D] Accepted NeurIPS 2024 paper claimed to be solving a novel problem as first work, but ignores 5 p ](https://www.reddit.com/r/MachineLearning/comments/1gxooqv/d_accepted_neurips_2024_paper_claimed_to_be/) , 2024-11-24-0914
```
At NeurIPS 2024 I found a paper that got accepted that positions its main contribution in the form of “Existing algorith
ms for X ignore Y. We adapt algorithm Z for X to account for Y”.

On OpenReview I see that the reviewers in particular p
raised the novelty of the work, and recognised Y as an important aspect that had been ignored in the field of X.

Now th
e interesting bit: co-authors and I published a paper in Springer’s Machine Learning journal in 2023 that also proposes 
an algorithm for X that account for Y. We were also not the first to study the problem setting of X with Y: our paper’s 
related work section discusses 4 papers that have all proposed algorithms for X that account for Y. One is even from Neu
rIPS (2017), and the oldest one dates back to 2012 (an AAAI paper).

The authors of this 2024 NeurIPS paper completely m
issed all this prior literature and believed they were the first, and so did all the reviewers.

This week I e-mailed th
e authors of this NeurIPS 2024 paper and they acknowledged that these works (mine + the 4 others) indeed were all workin
g on the same problem setting, mentioned that they were unaware of all these works, and acknowledged that they can no lo
nger claim novelty of the problem setting.

NeurIPS allows updating the camera ready paper after the conference, and the
 authors promised to use this opportunity to incorporate those related works and modify their contribution statements to
 no longer claim novelty of a first solution of X with Y.

At the one hand, it makes me happy that our work will get cre
dited appropriately.

At the other hand I have my doubts about the ethics of severely modifying contribution statements 
post-review. The authors will no longer claim novelty, but the reviewers in particular praised this novelty, which makes
 me uncertain whether reviewers would have recommended acceptance had they known that this paper will ultimately no long
er be able to claim the novelty that it claimed to have in the reviewed version.

Moreover this makes me wonder about th
e experimental section. Almost surely, reviewers would have demanded comparison to those 5 prior works as baselines. Thi
s paper did not compare against baselines, which will have seemed reasonable to a reviewer who reviewed this work under 
the assumption that the problem setting was completely novel and no prior methods exist that could function as a baselin
e.

Asking the group here about any thoughts on how such cases should get resolved:
- should the paper be retracted?
- s
hould the area chair / program committee be informed? who may or may not take action
- should the paper just get updated
 by authors in the way that was promised, and that is it?
- something else?

I redacted X, Y and Z in order to not publi
cly shame the authors, as they have engaged with my e-mails and I am convinced that there is no foul play and they truly
 were unaware of those works.
```
---

     
 
all -  [ Does anyone function more as a 'applied scientist' but have no research background? ](https://www.reddit.com/r/datascience/comments/1gxhjfr/does_anyone_function_more_as_a_applied_scientist/) , 2024-11-24-0914
```
**TLDR: DS profile is shifting to be more ML heavy, but lack research experience to compete with ML specialists.**

I've
 been a DS for several years, mostly in jack-of-all-trades functions: large-scale pipeline building, ad-hoc/bespoke stat
istical modeling for various stakeholders, ML applications, etc. More recently, I've started on a lot more GenAI/LLM wor
k alongside applied scientists. Leaving aside the negativity on LLM hype, most of the AS folks have heavy research backg
rounds: either PhDs or publications, attendance at conferences like ICLR, CVPR, NeurIPS, etc. I don't have any research 
experience except for a short stint in a lab during grad school but was never published. Luckily my AS peers have treate
d me as their own, which is good from credibility perspective.

That said, when I look at the market, DS jobs are either
 heavy on product analytics (hypothesis testing, experimentation, product sense, etc.) or DA/BI (dashboards, reporting, 
vis, etc.). The ones that are ML-heavier generally want much more research experience and involvement. I can explain the
 theory behind transformers, attention, decoders vs. encoders, etc. but I have zero publications and wouldn't stand a ch
ance against people with much deeper ML research experience.

I guess what I'm looking for is an applied/ML scientist-ad
jacent role, but still gives opportunity to flex to occasionally support other functions, like TPM'ing, DE, MLOps, etc. 
Aside from startups, there doesn't seem to be much out there. Anyone else?
```
---

     
 
all -  [ All the test environments used to benchmark BALROG. ](https://www.reddit.com/r/agi/comments/1gwqhry/all_the_test_environments_used_to_benchmark_balrog/) , 2024-11-24-0914
```
# BabyAI

+ Purpose is to facilitate research on *grounded language learning.*  The current domain of BabyAI is a 2D gri
dworld in which synthetic natural-looking instructions (e.g. “put the red ball next to the box on your left”) require th
e agent to navigate the world including unlocking doors) and move objects to specified locations.  

https://openreview.
net/forum?id=rJeXCo0cYX

----

# Crafter

+ Crafter features randomly generated 2D worlds where the player needs to fora
ge for food and water, find shelter to sleep, defend against monsters, collect materials, and build tools.

https://gith
ub.com/danijar/crafter?tab=readme-ov-file


----

# TextWorld

+ Microsoft TextWorld is an open-source, extensible engin
e that both generates and simulates text games. You can use it to train reinforcement learning (RL) agents to learn skil
ls such as language understanding and grounding, combined with sequential decision making.

https://www.microsoft.com/en
-us/research/project/textworld/

https://github.com/microsoft/TextWorld

https://arxiv.org/pdf/1806.11532

----

# Baba 
is AI 

+ Humans solve problems by following existing rules and procedures, and also by leaps of creativity to redefine 
those rules and objectives.    We test three ***state-of-the-art multi-modal large language models (OpenAI GPT-4o, Googl
e Gemini-1.5-Pro and Gemini-1.5-Flash) and find that they fail dramatically*** when generalization requires that the rul
es of the game must be manipulated and combined. 


https://github.com/nacloos/baba-is-ai

https://arxiv.org/abs/2407.13
729

----

# MiniHack

+ MiniHack is a sandbox framework for easily designing rich and diverse environments for Reinforc
ement Learning (RL).   The motivation behind MiniHack is to be able to perform RL experiments in a controlled setting wh
ile being able to increasingly scale the complexity of the tasks.

https://github.com/facebookresearch/minihack

https:/
/minihack.readthedocs.io/en/latest/


----

# NetHack

+ NetHack is an attractive research platform as it contains hundr
eds of enemy and object types, has complex and stochastic environment dynamics, and has a clearly defined goal (descend 
the dungeon, retrieve an amulet, and ascend) which can be achieved in a diverse set of ways. The game is considered one 
of the hardest in the world1, with winning episodes lasting 100,000s of steps, and a permadeath setting that starts agen
ts at the beginning in a whole new world if they die in the dungeon. NetHack is even difficult to master for human playe
rs who often rely on external knowledge.


https://proceedings.neurips.cc/paper_files/paper/2023/file/764ba7236fb6374301
4fafbd87dd4f0e-Paper-Conference.pdf

https://github.com/upiterbarg/hihack

https://arxiv.org/pdf/2203.11889

https://www
.youtube.com/watch?v=8L8LiQ-cIWA
```
---

     
 
all -  [ Google Scholar Completely Disappeared Our Paper With 60+ Citations ](https://www.reddit.com/r/academia/comments/1gwjzrk/google_scholar_completely_disappeared_our_paper/) , 2024-11-24-0914
```
Our paper 'Real-Time Reinforcement Learning' published on [Arxiv](https://arxiv.org/abs/1911.04448) and [Neurips](https:
//papers.nips.cc/paper_files/paper/2019/hash/54e36c5ff5f6a1802925ca009f3ebb68-Abstract.html) was [correctly listed on Go
ogle Scholar](https://web.archive.org/web/20240603082519/https://scholar.google.com/citations?user=4_1LlbAAAAAJ&hl=en) s
ince 2019. At some point during the last few months it vanished from Google Scholar leaving only an info box without any
 links or citations on [my profile today](https://web.archive.org/web/20241121144849/https://scholar.google.com/citation
s?user=4_1LlbAAAAAJ&hl=en). Even [searching for it ](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=real+time+r
einforcement+learning+ramstedt+pal&btnG=)using the full title and author names yields no results now.  
  
It seems like
 Google Scholar erroneously and retroactively (after 5 years) merged our paper with another paper from 2019 with complet
ely different title and authors. The Google Scholar link on Arxiv explicitly referencing the Arxiv-ID now points to [ano
ther paper](https://scholar.google.com/scholar_lookup?arxiv_id=1911.04448). On that page, when clicking on 'All 14 Versi
ons', it then [shows versions of our paper](https://scholar.google.com/scholar?cluster=14219642840399587525&hl=en&as_sdt
=0,5). The only commonality between the two papers is that both papers were published at Neurips 2019.

Does anyone have
 an idea on how to fix this? As far as I know Google Scholar doesn't have a support email or support forum.


```
---

     
 
all -  [ [D] PhD in RL/ML Theory or LLM ](https://www.reddit.com/r/MachineLearning/comments/1gvx8vx/d_phd_in_rlml_theory_or_llm/) , 2024-11-24-0914
```
Hi guys,

I'm at a crossroads in my academic journey and would appreciate the community's insights. I'm trying to decide
 between pursuing a PhD focused on reinforcement learning/ML theory versus specializing in large language models with mo
re experimental/applied research (these are the only two offers I had).

# Key considerations are the following:

# Rese
arch Impact

* RL/ML Theory: Foundational work that could advance the field's mathematical understanding
* LLMs: Direct 
applications in today's most transformative AI systems

# Job Prospects

* Theory: Academia, research labs, potentially 
more limited industry roles
* LLMs: High industry demand, active research area in both academia and industry

# Long-ter
m Relevance

* Theory: Core principles likely to remain valuable regardless of specific technologies
* LLMs: Currently r
evolutionary but uncertain long-term trajectory

Personal background

* I'm an international student and about to finish
 my master program in US, so I no longer has enough time before making the final decision. I used to research in ml theo
ry, but did not end up with a real top conference publication in theory. I personally doubt if I have enough mathematica
l background to pursue a successful PhD in this area (e.g., at least publish 2 theory papers a year on ICML/NeurIPS/ICLR
/COLT/AISTATS). At the same time, I am personally doubting if theory works indeed advance the ML/AI community, as many p
apers are just proving vacuous bounds or propose some new algorithms that themselves cannot even implement or experiment
ally tested.
* I also used to research in more applied ml, with one aaai paper. My personal concerns is that I'm not fas
t at implementation and coding, the most strategic ability for a successful applied ML researcher. After we entered the 
LLM era, the pacing or applied ML research (especially in LLM and CV) becomes so fast. It's like competitive programming
 in research community (well, also the #GPUs competition).
```
---

     
 
all -  [ That’s it folks! ](https://i.redd.it/69mlt91aku1e1.jpeg) , 2024-11-24-0914
```
(Not the person in the post)
```
---

     
 
all -  [ [D] Expectation from Machine Learning Engineering jobs ](https://www.reddit.com/r/MachineLearning/comments/1gtt099/d_expectation_from_machine_learning_engineering/) , 2024-11-24-0914
```
Hey everyone,

I’ve seen a lot of posts here about careers in ML and landing internships or jobs, and two things come up
 a lot

1. Building a strong research portfolio and publishing at conferences like NeurIPS, ICLR, and ICML, which seems 
to focus more on getting research scientist roles.

2. The growing demand for Machine Learning Engineer (MLE) roles, whi
ch are apparently more in demand than research scientist positions.

I’m curious about the difference between these two 
roles and what kind of portfolio would be ideal for landing an MLE position. I know having a master’s degree is often pr
eferred, but is an impressive publication record necessary for MLE roles? Or is it not that big of a deal?

What are you
r thoughts?
```
---

     
 
all -  [ [D] NeurIPS 24’ Attendance without tickets ](https://www.reddit.com/r/MachineLearning/comments/1gt9r5b/d_neurips_24_attendance_without_tickets/) , 2024-11-24-0914
```
Does anyone know, for past conferences, whether there were people checking badges at the entrance of the convention cent
er or at the workshop. (cause I wasn’t able to get a ticket so far via lottery this year, and I am wondering whether I c
ould just walk in or something)
```
---

     
 
all -  [ On the current state of robotics (ig?) (from a CSE perspective) (For all my homies out there) ](https://www.reddit.com/r/Btechtards/comments/1gsjxio/on_the_current_state_of_robotics_ig_from_a_cse/) , 2024-11-24-0914
```
Follow up on [https://www.reddit.com/r/Btechtards/comments/1gseqvq/cs\_roadmap\_for\_all\_my\_1st\_year\_homes\_out\_the
re/](https://www.reddit.com/r/Btechtards/comments/1gseqvq/cs_roadmap_for_all_my_1st_year_homes_out_there/)

Background -
 CSE 4th year, T1 (idk much about the electronics aspects of robotics and I kinda do computer vision not robotics)

\---
Profs---

I have like a research-ish approach to robotics cause of labs and stuff. Here's how I judge research - [https:
//csrankings.org/#/index?all&us](https://csrankings.org/#/index?all&us) (only considers the good conferences)

As for Ro
botics and CV in India - [https://csrankings.org/#/index?vision&robotics&in](https://csrankings.org/#/index?vision&robot
ics&in)

You get the usual research heavy unis (IIIT H, IISc, IIT K).

Let's go from a professor perspective, here are t
he absolute beasts in India (in no particular order) (CV + robotics):

1. K Madhava Krishna (IIIT H): [https://scholar.g
oogle.co.in/citations?user=QDuPGHwAAAAJ&hl=en](https://scholar.google.co.in/citations?user=QDuPGHwAAAAJ&hl=en)
2. C V Ja
wahar (IIIT H): [https://scholar.google.com/citations?user=U9dH-DoAAAAJ&hl=en](https://scholar.google.com/citations?user
=U9dH-DoAAAAJ&hl=en)
3. R. Venkatesh Babu (IISc): [https://cds.iisc.ac.in/faculty/venky](https://cds.iisc.ac.in/faculty/
venky)
4. Shishir N Y Kolathaya (IISc): [https://www.shishirny.com/](https://www.shishirny.com/)
5. Indranil Saha (IIT K
): [https://scholar.google.com/citations?user=F6QSFGkAAAAJ&hl=en](https://scholar.google.com/citations?user=F6QSFGkAAAAJ
&hl=en)
6. Avinash Sharma (IIT J): [https://3dcomputervision.github.io/](https://3dcomputervision.github.io/)
7. Chetan 
Arora (IIT D): [https://www.cse.iitd.ac.in/\~chetan/](https://www.cse.iitd.ac.in/~chetan/)

(Lmk if I should add any)

H
ere's how I would have started:

1. Look up their research and try to make sense out of it
2. Look at their top 5 newest
 papers and top 5 papers and see if you understand the abstract. If you don't relentelessly use Perplexity and get infor
mation.

Now you know the SOTA in India for robotics and CV. Then, look at these international profs (trying to add 5 in
 no order that have diverse research interests)

1. [https://www.cs.cmu.edu/\~./choset/](https://www.cs.cmu.edu/~./chose
t/)
2. [https://people.eecs.berkeley.edu/\~svlevine/](https://people.eecs.berkeley.edu/~svlevine/) (absolute fucking god
 imo)
3. [https://animesh.garg.tech/](https://animesh.garg.tech/)
4. [https://research.qut.edu.au/qcr/people/michael-mil
ford](https://research.qut.edu.au/qcr/people/michael-milford)
5. [https://people.eecs.berkeley.edu/\~anca/](https://peop
le.eecs.berkeley.edu/~anca/) (HCI stuff but I consider her robotics)

Good, now you know what's happening in academia. S
ince industry stems from academic esp. in robotics, you also know what will be happening there 5 years down the line. Lo
ok at cool stuff from Boston Dynamics (duh), Allen Institue for AI, Honda Research, etc. as well. Some pretty amazing Ch
inese and Israeli companies exist as well.

\---Starting with robotics---

I'm a sucker for mobile robotics -

1. [https
://www.youtube.com/playlist?list=PLgnQpQtFTOGQrZ4O5QzbIHgl3b1JHimN\_](https://www.youtube.com/playlist?list=PLgnQpQtFTOG
QrZ4O5QzbIHgl3b1JHimN_)
2. [https://www.youtube.com/playlist?list=PLgnQpQtFTOGQJXx-x0t23RmRbjp\_yMb4v](https://www.youtu
be.com/playlist?list=PLgnQpQtFTOGQJXx-x0t23RmRbjp_yMb4v)
3. [https://www.youtube.com/playlist?list=PLgnQpQtFTOGQh\_J16IM
wDlji18SWQ2PZ6](https://www.youtube.com/playlist?list=PLgnQpQtFTOGQh_J16IMwDlji18SWQ2PZ6)

All by C. Stachniss.

Then, q
uite literally do any course on robot manipulation and dynamics.

Then, start OpenCV - the docs are beautiful. Use them.
 Use Python. Learn PyTorch as well! (docs work).

Learn ROS using the docs (or any playlist tbh, all are pretty good).


Tie eveyrthing together by building a CV + Robotics pipeline using ROS simulations such as camera calibration, SLAM pipe
line, etc.

\---Going ahead---

Take a top-tier robotics paper (one that is not too math-y but more ML-y) and read their
 codebases. Literally just google any of the papers from the conferences listed below and choose one that sounds interes
ting (and has the codebase available).

Then, and I cannot emphasize this further, write your own implementation. It mig
ht take weeks (and ik the difficulties involved vis-a-vis hardware or GPUs - just simulate / do on a lower scale) but it
'll be worth it.

My fav repos are

1. [https://github.com/amaralibey/MixVPR](https://github.com/amaralibey/MixVPR)
2. [
https://github.com/robodhruv/visualnav-transformer](https://github.com/robodhruv/visualnav-transformer) (all three of th
e codebases)
3. [https://github.com/PRBonn/kiss-icp](https://github.com/PRBonn/kiss-icp)

(Again, lmk if you have any ad
ditions to this list)

Robotics honestly just diversifies at this point. Choose a direction that interests you (SLAM, ha
rdware, optimizations, vision, HCI, etc.)

\---Jobs?---

Join academia or a research lab (none in India unfortunately). 
You can cold-email profs asking for research internships or assistantships - that works sometimes. CAIR in Blr is also a
mazing.

Industry - some super cool stuff in India as well rn (minuszero, Swaayatt Robots, a bunch of drone companies, e
tc.). Nvidia also has some cool roles as well.

\---Should you do it?---

Idk. I'm an undergrad. This is what I've done 
and what some PhDs and MS people told me. Ask people on LinkedIn / Twitter to figure out whether robotics (and which par
t of robotics specifically) is what you want.

\---Conferences---

Robotics - ICRA, IROS, CORL, RSS

CV - CVPR, ICCV, EC
CV, BMVC, WACV (people also submit CV stuff to ICLR, NeurIPS, ICML, etc)


```
---

     
 
all -  [ [R] Convolutional Differentiable Logic Gate Networks ](https://www.reddit.com/r/MachineLearning/comments/1gs92mb/r_convolutional_differentiable_logic_gate_networks/) , 2024-11-24-0914
```
Abstract

With the increasing inference cost of machine learning models, there is a growing interest in models with fast
 and efficient inference. Recently, an approach for learning logic gate networks directly via a differentiable relaxatio
n was proposed.  Logic gate networks are faster than conventional neural network approaches be- cause their inference on
ly requires logic gate operators such as NAND, OR, and XOR, which are the underlying building blocks of current hardware
 and can be efficiently executed. We build on this idea, extending it by deep logic gate tree convolutions, logical OR p
ooling, and residual initializations. This allows scaling logic gate networks up by over one order of magnitude and util
izing the paradigm of convolution. On CIFAR-10, we achieve an accuracy of 86.29% using only 61 million logic gates, whic
h improves over the SOTA while being 29× smaller.

  
Accepted at Neurips 2024, 'SOTA' here means comparable approaches.
 I found this paper really interesting, even though non-toy networks seems like they would be very expensive to train. C
urious what others think?
```
---

     
 
all -  [ How is the ACL Conference? ](https://www.reddit.com/r/deeplearning/comments/1gs7he7/how_is_the_acl_conference/) , 2024-11-24-0914
```
Hello, I know it's a very noob question but I was wondering what the reputation of ACL is in the field. I have been writ
ing my first paper and my mentor recommended that I aim for the ACL deadline, I just wanted to know how prestigious it w
as relative to bigger conferences like NeurIPS, ICML, ICLR, etc.

Also, purely hypothetical, but what weight does an ACL
 acceptance hold for getting a summer internship/research? I'm an undergrad and I'm kind of cooked with my summer intern
ship prospects, so I was wondering if it would help in any regard.
```
---

     
 
all -  [ [D] Neurips 2024 Hotel Roommate Search ](https://www.reddit.com/r/MachineLearning/comments/1gs0gj8/d_neurips_2024_hotel_roommate_search/) , 2024-11-24-0914
```
The hotels around the venue for Neurips 2024 are pretty expensive, and I'm looking for a roommate to split the cost with
 (my university has a limit on the nightly hotel rate they are willing to reimburse). I currently have reserved a room f
or Tuesday-Sunday in the Century Plaza Hotel, which is 0.9 miles from the convention center. The nightly rate is $414. I
f anyone wants to split the cost of a room, please reach out! Also, it would be helpful if you could share this post wit
h your research group or other attendees that you know.

If you are unsure about rooming with a complete stranger, you c
an get to know me a little bit through my personal website (https://mtcrawshaw.github.io/), which has links to my google
 scholar page, CV, etc. I do have a paper at the conference in the area of federated learning/distributed optimization. 
Just a grad student trying to make conferences affordable! Thanks.
```
---

     
 
all -  [ Need an Advice ](https://www.reddit.com/r/PhD/comments/1grg73d/need_an_advice/) , 2024-11-24-0914
```
Hi everyone, I’m a first-year computer science PhD student in Europe from Asia, going into my second year soon. I wanted
 to ask for some advice on what I should do. First off, I’m an international student from a Southeast Asian country, and
 right now I’m really struggling with the lab environment.

First, my professor requires all PhD students to work in the
 lab from 9 to 5 every weekday, no exceptions except for weekends. We’re only allowed to take time off when the universi
ty is officially closed. Second, I found out from previous PhD students that my professor insists on a strict policy of 
“equal credit” in publications, meaning that even if I do all the work for a paper—from analysis to programming, writing
, and revisions—my name won’t be listed as the first author because authorship order is strictly alphabetical.

Third, s
ome of us in the lab (we’re all international students) aren’t allowed to submit our papers to conferences, even big one
s like ICML or NeurIPS. My professor only wants our publications in journals, even though conferences are important for 
PhD students to network and get feedback from experts in the field.

Lastly, and perhaps the most difficult part for me,
 is that I’m not allowed to collaborate with anyone outside the lab. I’m not even allowed to discuss my project or seek 
advice from people outside the lab group. This restriction makes me feel isolated, and for the past three months, I’ve h
ad recurring nightmares and panic attacks before going into the lab. I reached out to the PhD board to ask if I could tr
ansfer to a different lab, but they said it’s impossible.

I’m really at a loss here. Should I stick it out in this lab 
for the next 2-3 years, knowing I won’t have the chance to publish as the primary author and that, when I graduate, I’ll
 probably have no network beyond the people in this lab?
```
---

     
 
all -  [ [D] Looking for a project partner who's published in top conferences [cvpr, neurips, wacv, iccv, etc ](https://www.reddit.com/r/computervision/comments/1gpfcpk/d_looking_for_a_project_partner_whos_published_in/) , 2024-11-24-0914
```
Hello y'all. Deep into my master's degree, I am in a dire need of a mentor/partner for my research partner. Some of the 
professors at the academia who claim to specialize in the field of computer vision/ai doesnt know how to clone an existi
ng model from github or provide gpu alternatives and solutions who doesnt have fancy things to speed up the process. 

s
o if you do feel the same way and is interested to work on some cool research gap leading to a publication. drop a comme
nt on what excites you most. thankss.
```
---

     
 
all -  [ [D] How to Choose an AI-Focused Master's Program? ](https://www.reddit.com/r/computervision/comments/1gpba3y/d_how_to_choose_an_aifocused_masters_program/) , 2024-11-24-0914
```
I'm currently applying for AI-focused Master's programs, and I could really use some advice. I love working in computer 
vision, and I think I’m genuinely passionate about research. I presented my first paper at an affinity workshop at ICML,
 and I’ll be attending NeurIPS as a workshop presenter. This experience has been a blast, and I'm hoping to continue dow
n this path.

Right now, I'm feeling overwhelmed by all the options and the looming deadlines. The only program I’m trul
y excited about is at UvA (University of Amsterdam). But I know I need to consider more options to keep my career moving
 forward.

Here’s what I'm interested in:

* **Self-Supervised Learning (SSL):** I have experience in this area and woul
d love to deepen my expertise.
* **Video Understanding and GNNs:** These are becoming my newest interests, and I’d love 
to join a program where I can explore these topics.
* **Research-oriented environments:** I’m currently collaborating wi
th a professor and have found that I really enjoy the collaborative, exploratory nature of research.

The problem? I don
’t want to settle for a program that doesn’t align with these interests or doesn’t offer strong mentorship and research 
opportunities. I’m also worried I might be *too* picky, which is making the process even more stressful. I’d love to hea
r from anyone who’s been in a similar position:

1. **How did you prioritize which programs to apply to?**
2. **Did you 
find a strategy that helped you balance your interests with program options?**
3. **Any advice on picking a program that
 will help with a long-term research-focused career?**

Thanks so much for any insights you can share!
```
---

     
 
all -  [ [D] NeurIPS After Dark Networking Event ](https://www.reddit.com/r/MachineLearning/comments/1gpamvn/d_neurips_after_dark_networking_event/) , 2024-11-24-0914
```
Just got an email about an official ticketed after dark NeurIPS networking event - this will be my first time attending/
presenting, wondering if these events are worth going to. More generally, also interested in hearing about how to make t
he most of my time attending.
```
---

     
 
all -  [ NeuroAI - NeurIPS Workshop (Vancouver, Dec 15) ](https://www.reddit.com/r/corticallabs/comments/1gp8lg5/neuroai_neurips_workshop_vancouver_dec_15/) , 2024-11-24-0914
```
Hey all, just wanted to make the announcement that some of the Cortical Labs team will be in Vancouver for NeurIPS and C
TO Dave will be publishing the beta API spec for community feedback.

  
[https://neuroai-workshop.github.io](https://ne
uroai-workshop.github.io)
```
---

     
 
all -  [ Anyone's paper got selected for NeurIPS and are planning to go to Vancouver from Bengaluru??? ](https://www.reddit.com/r/Bengaluru/comments/1go3w7w/anyones_paper_got_selected_for_neurips_and_are/) , 2024-11-24-0914
```
If anyone is traveling, i really need your help in planning mine. 
```
---

     
 
all -  [ [R] Classic GNNs (GCNs, GraphSAGEs, GATs) are Strong Baselines on Node Classification ](https://www.reddit.com/r/MachineLearning/comments/1gnsn54/r_classic_gnns_gcns_graphsages_gats_are_strong/) , 2024-11-24-0914
```
We’re excited to share our recent paper '[\[NeurIPS 2024\] Classic GNNs are Strong Baselines: Reassessing GNNs for Node 
Classification](https://arxiv.org/pdf/2406.08993).'

In this study, we conduct a thorough review of classic GNNs for nod
e classification tasks. Our findings suggest that the superior performance often reported by state-of-the-art graph lear
ning models may be due to suboptimal hyperparameter configurations in classic GNNs. By fine-tuning these hyperparameters
, we show that classic GNNs outperform the latest models on 17 out of 18 widely used node classification datasets.

Code
: [https://github.com/LUOyk1999/tunedGNN](https://t.co/QeNSn2D9CN)  
Arxiv: [https://arxiv.org/abs/2406.08993](https://t
.co/MD4mVTnHk8)

If you find our work interesting, we’d greatly appreciate a ⭐️ on GitHub!
```
---

     
 
all -  [ CV Sugession ](https://www.reddit.com/r/gradadmissions/comments/1gnbr8g/cv_sugession/) , 2024-11-24-0914
```
I  tried to publish research papers twice—first at NeurIPS and recently at ICVGIP—but I got rejected both times 🥲.

Now,
 I am thinking of adding a section to my CV called “Appendix: Research Work Sample since I don’t have any published pape
rs yet. Should I include these papers and label them as “submitted” or “submitted to conf __”?

I would really appreciat
e your advice.
```
---

     
 
all -  [ Ok, for real how do I rank? ](https://www.reddit.com/r/eb_1a/comments/1gn2zo7/ok_for_real_how_do_i_rank/) , 2024-11-24-0914
```
I was pretty certain that my pathway to green card was gonna be smooth… until the Trump victory. I’m gearing up for EB1A
 but worried that the extra scrutiny during his term will close that door for me. Here are the stats.

- FAANG ML Engine
er with MSc
- Some media coverage of my work
- 4 papers, 3 preprints, 1 industrial demo, 1 thesis, first author on all b
ut 2; some are top-tier like CVPR and ACL
- 450+ citations
- have served as reviewer for about 50 manuscripts; all for t
he top tier conferences (CVPR, NeurIPS, ICML, ICLR)

Am I toast or can I gun for EB1A?
```
---

     
 
all -  [ [R] Most Time Series Anomaly Detection results are meaningless (two short videos explain why) ](https://www.reddit.com/r/MachineLearning/comments/1gmwxnr/r_most_time_series_anomaly_detection_results_are/) , 2024-11-24-0914
```
Dear Colleagues

Time Series Anomaly Detection (TSAD) is hot right now, with dozens of  papers each year in NeurIPS, SIG
KDD, ICML, PVLDB etc.

However, I claim that much of the published results are meaningless, because the uncertainty of t
he ground truth labels dwarfs any claimed differences between algorithms or amount of claimed improvements.

I have made
 two 90-second-long videos that make this clear in a visual and intuitive way:

 1)      Why Most Time Series Anomaly De
tection Results are Meaningless (Dodgers)

[https://www.youtube.com/watch?v=iRN5oVNvZwk&ab\_channel=EamonnKeogh](https:/
/www.youtube.com/watch?v=iRN5oVNvZwk&ab_channel=EamonnKeogh)

  2)      Why Most Time Series Anomaly Detection Results a
re Meaningless (AnnGun)

[https://www.youtube.com/watch?v=3gH-65RCBDs&ab\_channel=EamonnKeogh](https://www.youtube.com/w
atch?v=3gH-65RCBDs&ab_channel=EamonnKeogh)

As always, corrections and comments welcome.

Eamonn

 EDIT: To be clear, my
 point is simply to prevent others from wasting time working with datasets with essentially random labels. In addition, 
we should be cautious of any claims in the literature that are based on such data (and that includes at least dozens of 
highly cited papers)

  


For a review of most of the commonly used TSAD datasets, see this file:

[https://www.dropbox
.com/scl/fi/cwduv5idkwx9ci328nfpy/Problems-with-Time-Series-Anomaly-Detection.pdf?rlkey=d9mnqw4tuayyjsplu0u1t7ugg&dl=0](
https://www.dropbox.com/scl/fi/cwduv5idkwx9ci328nfpy/Problems-with-Time-Series-Anomaly-Detection.pdf?rlkey=d9mnqw4tuayyj
splu0u1t7ugg&dl=0)
```
---

     
 
all -  [ Boss wants me in Vancouver for neurips conference. Please take my 1 tix, 5 day pass. Selling at cost ](https://www.reddit.com/r/Wonderfruit/comments/1gmvwe0/boss_wants_me_in_vancouver_for_neurips_conference/) , 2024-11-24-0914
```
I have one 5 day pass, bought it during early bird. Can change name during pre-registration. I want to make no profit fr
om this. Heck, I’ll give you a discount. But I need to talk to you up front, and we need to figure out a payment situati
on. 

Best case scenario is that you’re in the United States.

Reply to this and I will reach out.
```
---

     
 
all -  [ Alaa Lab at UC Berkeley / UCSF Seeking PhD Students in ML/AI for Healthcare ](https://www.reddit.com/r/CompSocial/comments/1gmh3q6/alaa_lab_at_uc_berkeley_ucsf_seeking_phd_students/) , 2024-11-24-0914
```
Prof. Ahmad Alaa, who leads a [joint lab](https://alaalab.berkeley.edu/home) at UC Berkeley and UCSF is seeking PhD appl
icants interested in working at the intersection of ML/AI and Healthcare. They call out the following focus areas, with 
example papers:

* **Track 1:** **Machine Learning Theory, Statistics and Causal Inference** (Example papers: [NeurIPS 2
024](https://arxiv.org/abs/2402.07307), [NeurIPS 2023](https://proceedings.neurips.cc/paper_files/paper/2023/hash/94ab02
a30b0e4a692a42ccd0b4c55399-Abstract-Conference.html), [AISTATS 2023](https://proceedings.mlr.press/v206/alaa23a.html))
*
 **Track 2: Large Vision and Language Models for Medicine** (Example papers: [NeurIPS 2024 - 1](https://arxiv.org/abs/24
03.00177), [NeurIPS 2024 - 2](https://arxiv.org/pdf/2405.19567), [ICML 2024](https://arxiv.org/pdf/2406.05396), [ICLR 20
24](https://arxiv.org/abs/2310.00390), [NeurIPS 2023](https://proceedings.neurips.cc/paper_files/paper/2023/hash/2b1d1e5
affe5fdb70372cd90dd8afd49-Abstract-Conference.html))
* **Track 3: Applied Machine Learning for Cardiology** (Example pap
ers: [Nature Machine Intelligence 2021](https://www.nature.com/articles/s42256-021-00353-8), [PLOS 2019](https://journal
s.plos.org/plosone/article?id=10.1371/journal.pone.0213653))

To learn more and connect with Dr. Alaa prior to submittin
g a PhD application, check out this Google Form: [https://docs.google.com/forms/d/e/1FAIpQLScgiULXsOJjsnK2y9av10ztg-gGCL
hCX\_eybpwHxwYv-ZmJmA/viewform](https://docs.google.com/forms/d/e/1FAIpQLScgiULXsOJjsnK2y9av10ztg-gGCLhCX_eybpwHxwYv-ZmJ
mA/viewform)
```
---

     
 
all -  [ CAN I GET INTO HARVARD + UC's ](https://www.reddit.com/r/chanceme/comments/1gm5icr/can_i_get_into_harvard_ucs/) , 2024-11-24-0914
```
**Demographics**:

* low ranking HS, 250 ish grad class
* Asian
* Hook: I play chess
* CS BA or BS

**GPA**: 3.7 W(good 
reasons why so low just trust)

No rank in my HS

7 APs, 8 Tests

SAT - 1500 composite

**Awards**:

* AP scholar with h
onors
* honor roll
* Top 100 nationally ranked chess players In age groups for the past 4 years
* USCF candidate master

* Won an international/national tournament + state champ in chess

**ECs:**

* High School Chess league president - 20+ 
schools, 100+ participants, $1k+ raised
* 1st author to Novel Ai paper - published and submitted to conferences like Neu
rips + COLING, available on arXiv
* Chess Club president - 3 peat champion in regional league, top 5 teams in State
* DE
CA - 3x state qualifier
* Motorola Solutions Intern - made a REST API for one of their apps in prod
* Paid Chess coach -
 Apart of non-profit group for underprivileged youth in chicago(not from there did remote)
* Volunteer Chess Coach - vol
unteered apart of local chess academy, 200 ish hours over the 4 years
* Wrestling - Varsity
* SASA(south asian student a
ssociation) treasurer - raised 10k from sponsors and events, provided scholarships for the first year to south asian stu
dents
* Inspirit AI scholars program(free) - Made Chess bot with GPT 4o capable of playing at an expert level

**Persona
l Statement:** 8.5/10 (not insanely good, but everyone who reads it likes it, and reviewers can't find problems with it,
 so conservative 7.5, but 9.5/10 liberally)

**Colleges**:  
Reach: HARVARD, UMICH, CMU, UMD, UWM, NEU,  UCLA, Cal, UCSD


Target: Ohio State, Penn State, Purdue, IU, Vtech, UMass Amherst

Safety: UPitt, RIT, Bentley, Rutgers

  

```
---

     
 
all -  [ Question about EB2 NIW and re-election of President Trump ](https://www.reddit.com/r/USCIS/comments/1glc0s5/question_about_eb2_niw_and_reelection_of/) , 2024-11-24-0914
```
Hey, I have a question about possible effects of the recent re-election on my application as an Iranian citizen (male) w
ho recently filed their I140. I'm wondering if I should apply for premium processing or not.

# About my profile:

I'm a
 PhD student (started in January 2024) in the states studying deep learning (theory). I have three first-author publishe
d works on deep learning theory that align well with my research interests and what I'm working on right now.:One at Neu
rIPS 2022, 26 citations.One at ICML 2023, 16 citations.One at ICML 2024, 4 citations.I have another submission that is n
ot published yet on which I'm the second author.I've received a masters in CS from a top-tier university in Canada (UBC)
.

# My Concern:

I've filed my I140 on October 20th this year. As an Iranian citizen, I’m worried about the possibility
 of my application being affected by the re-election of President Trump. Because of that, I’m considering applying for p
remium processing to get a decision on my I140 before potential new laws/orders come into effect. From talking to friend
s I’ve heard that there are possibilities that:

* The approval bar goes higher
* The processing time slows down
* etc


2805$ is not nothing for me, as I’m a PhD student. I can pay it, but it’s not easy on me.

I’m wondering if I should app
ly for PP nevertheless, or if the chances of my application getting affected by the re-election are slim. Any advice wou
ld be appreciated! Thanks.
```
---

     
 
all -  [ Question about EB2 NIW and re-election of President Trump ](https://www.reddit.com/r/EB2_NIW/comments/1glbyrt/question_about_eb2_niw_and_reelection_of/) , 2024-11-24-0914
```
Hey, I have a question about possible effects of the recent re-election on my application as an Iranian citizen (male) w
ho recently filed their I140. I'm wondering if I should apply for premium processing or not.

# About my profile:

I'm a
 PhD student (started in January 2024) in the states studying deep learning (theory). I have three first-author publishe
d works on deep learning theory that align well with my research interests and what I'm working on right now.:One at Neu
rIPS 2022, 26 citations.One at ICML 2023, 16 citations.One at ICML 2024, 4 citations.I have another submission that is n
ot published yet on which I'm the second author.I've received a masters in CS from a top-tier university in Canada (UBC)
.

# My Concern:

I've filed my I140 on October 20th this year. As an Iranian citizen, I’m worried about the possibility
 of my application being affected by the re-election of President Trump. Because of that, I’m considering applying for p
remium processing to get a decision on my I140 before potential new laws/orders come into effect. From talking to friend
s I’ve heard that there are possibilities that:

* The approval bar goes higher
* The processing time slows down
* etc


2805$ is not nothing for me, as I’m a PhD student. I can pay it, but it’s not easy on me. 

I’m wondering if I should ap
ply for PP nevertheless, or if the chances of my application getting affected by the re-election are slim. Any advice wo
uld be appreciated! Thanks.
```
---

     
 
all -  [ Ethics in AI ](https://www.reddit.com/r/ArtificialInteligence/comments/1gkndse/ethics_in_ai/) , 2024-11-24-0914
```
What are some good learning/certificate opportunities to enter the AI ethics space? Are there other volunteer opportunit
ies to do ethics reviews on papers besides NeurIPS (and what are the requirements to become an ethics reviewer?) 
```
---

     
 
all -  [ Is implementing famous research papers in ML worthy of writing in a resume? ](https://www.reddit.com/r/Btechtards/comments/1gjym1x/is_implementing_famous_research_papers_in_ml/) , 2024-11-24-0914
```
Title. I am currently in my 3rd year of BTech in CSE. I’ve been interested in ML/DL for quite some time now. And I was t
hinking of doing this. Is it okay to put them in resume for applying to research/industry internships?

Papers that I am
 thinking of implementing in no particular order:

- [Attention Is All You Need](https://proceedings.neurips.cc/paper_fi
les/paper/2017/file/3f5ee243547dee91fbd053c1c4a845aa-Paper.pdf)
- [Hand Written Digit Recognition Using Back Propagation
 Neural Network](https://proceedings.neurips.cc/paper/1989/file/53c3bce66e43be4f209556518c2fcb54-Paper.pdf)
- [An IMage 
is worth 16x16 words](https://openreview.net/pdf?id=YicbFdNTTy) Vision Transformer
- [LoRA- Low-Rank Adaptation Method f
or LLMs](https://openreview.net/pdf?id=nZeVKeeFYf9)
- [RAG paper from 2020](https://arxiv.org/pdf/2005.11401)
- [ESRGAN]
(https://openaccess.thecvf.com/content_ECCVW_2018/papers/11133/Wang_ESRGAN_Enhanced_Super-Resolution_Generative_Adversar
ial_Networks_ECCVW_2018_paper.pdf)
```
---

     
 
all -  [ Do I have to upload a poster and a video recording for my accepted paper in NeurIPS 2024 to be publi ](https://www.reddit.com/r/learnmachinelearning/comments/1gjx8bv/do_i_have_to_upload_a_poster_and_a_video/) , 2024-11-24-0914
```
I registered the virtual pass of NeurIPS 2024. Do I have to upload a poster and a video recording for my accepted paper 
in NeurIPS 2024 to be published? The emails or the instructions do not make any clarification about this. 
```
---

     
 
all -  [ [D] Looking for Research Internship in Applied RL & Robotics ](https://www.reddit.com/r/MachineLearning/comments/1giq0e8/d_looking_for_research_internship_in_applied_rl/) , 2024-11-24-0914
```
I am a PhD candidate at Mila, working on reinforcement learning for different robotic applications (worked on applicatio
ns like excavator automation, physics-based character animation, and autonomous driving). I'm currently seeking a summer
 research internship for 2025, and I'm really interested in any roles that focus on applied RL or embodied AI.

Here’s a
 bit about my research journey so far:

* **Automatic Reward Modeling**: Developed methods for deriving reward functions
 from expert demonstration for excavator automation in Vortex Simulator. (Presented at the NeurIPS RL for Real-life Appl
ications workshop.)
* **Sample-Efficient RL**: Improved sample efficiency on the Atari benchmark through transformer-bas
ed discrete world modeling. (ICML 2024)
* **Compositional Motion Priors for Multi-Task RL**: I'm currently working on mu
lti-task learning for robotic locomotion with compositional motion priors, using Isaac Gym.
* **RL for Autonomous Drivin
g**: Designed a curriculum learning method for autonomous driving on the CARLA simulator, eliminating the need for compl
ex reward shaping. (Inria research student).

I’m also exploring the use of Diffusion Models alongside RL for stable, di
verse control strategies.

If anyone knows of relevant openings or has any advice on places that may value applied RL re
search, I’d really appreciate it.

Thank you so much for any leads or suggestions!

*My CV and more details are on my* h
ttps://pranaval.github.io/*.*
```
---

     
 
all -  [ Looking for Research Internship in Applied RL & Robotics ](https://www.reddit.com/r/reinforcementlearning/comments/1gipwq6/looking_for_research_internship_in_applied_rl/) , 2024-11-24-0914
```
I am a PhD candidate at Mila, working on reinforcement learning for different robotic applications (worked on applicatio
ns like excavator automation, physics-based character animation, and autonomous driving). I'm currently seeking a summer
 research internship for 2025, and I'm really interested in any roles that focus on applied RL or embodied AI.

Here’s a
 bit about my research journey so far:

* **Automatic Reward Modeling**: Developed methods for deriving reward functions
 from expert demonstration for excavator automation in Vortex Simulator. (Presented at the NeurIPS RL for Real-life Appl
ications workshop.)
* **Sample-Efficient RL**: Improved sample efficiency on the Atari benchmark through transformer-bas
ed discrete world modeling. (ICML 2024)
* **Compositional Motion Priors for Multi-Task RL**: I'm currently working on mu
lti-task learning for robotic locomotion with compositional motion priors, using Isaac Gym.
* **RL for Autonomous Drivin
g**: Designed a curriculum learning method for autonomous driving on the CARLA simulator, eliminating the need for compl
ex reward shaping. (Inria research student).

I’m also exploring the use of Diffusion Models alongside RL for stable, di
verse control strategies.

If anyone knows of relevant openings or has any advice on places that may value applied RL re
search, I’d really appreciate it.

Thank you so much for any leads or suggestions!

*My CV and more details are on my* *
https://pranaval.github.io/.*
```
---

     
 
all -  [ [D] Publishing in NeurIPS, ICML, ICLR as an Early Researcher: Any Advice? ](https://www.reddit.com/r/MachineLearning/comments/1gip4cf/d_publishing_in_neurips_icml_iclr_as_an_early/) , 2024-11-24-0914
```
I'm currently pursuing a master's degree, and my goal is to publish a paper in one of the top AI/ML venues, like NeurIPS
, ICML, or ICLR, before I finish my program. I'm studying at a Federal University in Brazil, which is well-regarded loca
lly but doesn’t have much international recognition. My research lab is somewhat unstructured—we mainly share computatio
nal resources but don’t have collaborative or large-scale projects. Because of this, I don’t have an ongoing project I c
an join for guidance or support.

Additionally, my supervisor’s research focus is more on applied machine learning in ch
emistry, so he doesn’t have experience publishing in these top conferences. This means I don’t have direct mentorship on
 the publishing process specific to these venues. To give some context, NeurIPS's call for papers is expected around May
 2025, so I still have some time but want to prepare as thoroughly as possible.

I’d really appreciate any advice on how
 to increase my chances of getting published in these venues. For example, I’ve heard that it helps to cite potential re
viewers in your work. Any tips on how to navigate the process, write in a way that aligns with these conferences, or und
erstand what reviewers might be looking for would be helpful. I’d also like advice on handling rejection, like potential
 backup venues to consider if my paper isn’t accepted.
```
---

     
 
all -  [ Visa rejected for No Proper reason ](https://www.reddit.com/r/CanadaVisitorVisa/comments/1ghdzz6/visa_rejected_for_no_proper_reason/) , 2024-11-24-0914
```
I was supposed to go for NeurIPS conference from India and I had Invitation letter as well as cover letter from my compa
ny. Yet they have rejected with absolutely no logical reasons. How to appeal this? 
```
---

     
 
all -  [ [R] QTIP: Quantization with Trellises and Incoherence Processing ](https://www.reddit.com/r/MachineLearning/comments/1ggyj3l/r_qtip_quantization_with_trellises_and/) , 2024-11-24-0914
```
We're pleased to introduce QTIP, a new LLM quantization algorithm that uses trellis coded quantization and incoherence p
rocessing to achieve a state of the art combination of speed and quantization quality.

Paper (NeurIPS 2024 Spotlight): 
[https://arxiv.org/pdf/2406.11235](https://arxiv.org/pdf/2406.11235)

Codebase + inference kernels: [https://github.com/
Cornell-RelaxML/qtip](https://github.com/Cornell-RelaxML/qtip)

Prequantized models (including 2 Bit 405B Instruct): [ht
tps://huggingface.co/collections/relaxml/qtip-quantized-models-66fa253ad3186746f4b62803](https://huggingface.co/collecti
ons/relaxml/qtip-quantized-models-66fa253ad3186746f4b62803)

QTIP has significantly better quality over QuIP# while bein
g just as fast. QTIP is also on par with or better than PV-Tuning while being much faster (\~2-3x).


```
---

     
 
all -  [ New Quantization Method -- QTIP: Quantization with Trellises and Incoherence Processing ](https://www.reddit.com/r/LocalLLaMA/comments/1ggwrx6/new_quantization_method_qtip_quantization_with/) , 2024-11-24-0914
```
We're pleased to introduce QTIP, a new LLM quantization algorithm that uses trellis coded quantization and incoherence p
rocessing to achieve a state of the art combination of speed and quantization quality.

Paper (NeurIPS 2024 Spotlight): 
[https://arxiv.org/pdf/2406.11235](https://arxiv.org/pdf/2406.11235)

Codebase + inference kernels: [https://github.com/
Cornell-RelaxML/qtip](https://github.com/Cornell-RelaxML/qtip)

Prequantized models (including 2 Bit 405B Instruct): [ht
tps://huggingface.co/collections/relaxml/qtip-quantized-models-66fa253ad3186746f4b62803](https://huggingface.co/collecti
ons/relaxml/qtip-quantized-models-66fa253ad3186746f4b62803)

QTIP has significantly better quality over QuIP# while bein
g just as fast. QTIP is also on par with or better than PV-Tuning while being much faster (\~2-3x).

[2 Bit 405B Instruc
t running pipelined on 2 GPUs. The inference backend uses torch.compile and HF so this should be much faster on somethin
g like llama.cpp.](https://reddit.com/link/1ggwrx6/video/rz8ghv5fc8yd1/player)
```
---

     
 
all -  [ Chance a Chess Fiend With Below Average Grades but Good EC's and SAT ](https://www.reddit.com/r/chanceme/comments/1ggukfh/chance_a_chess_fiend_with_below_average_grades/) , 2024-11-24-0914
```
**Demographics**:

* mid to low comp HS, 250 ish grad class
* Asian
* I play chess?
* CS BA or BS

**GPA**: 3.7 W(good r
easons why so low just trust)

No rank

7 APs, 8 Tests

SAT - 1510 composite

**Awards**:

* AP scholar with honors
* ho
nor roll
* Top 100 nationally ranked chess players In age groups for the past 4 years
* USCF candidate master
* Won an i
nternational/national tournament + state champs in chess

\*\*ECs(\*\*nốt **ordered properly):**

* High School Chess le
ague president - 20+ schools, 100+ participants, $1k+ raised
* 1st author to Novel Ai paper - published and submitted to
 conferences like Neurips + COLING, available on arXiv
* Chess Club president - 3 peat champion in regional league, top 
5 teams in State
* DECA - 3x state qualifier
* Motorola Solutions Intern - made a REST API for one of their apps in prod

* Paid Chess coach - Apart of non-profit group for underprivileged youth in chicago(not from there did remote)
* Volunt
eer Chess Coach - volunteered apart of local chess academy, 200 ish hours over the 4 years
* Wrestling - Varsity
* SASA(
south asian student association) treasurer - raised 10k from sponsors and events, provided scholarships for the first ye
ar to south asian students
* Inspirit AI scholars program(free) - Made Chess bot with GPT 4o capable of playing at an ex
pert level

**Personal Statement:** 7.5/10 (not insanely good, but everyone who reads it likes it, and reviewers can't f
ind problems with it, so conservative 7.5)

**Colleges**:  
Umass, UMD, UW Madison, BU, NEU, Ohio State, Penn State, Pur
due, IU, Vtech, UPitt, RIT, Bentley, Rutgers
```
---

     
 
all -  [ [D] Is TMLR good enough to consider as an alternative to A* conferences? ](https://www.reddit.com/r/MachineLearning/comments/1ggsief/d_is_tmlr_good_enough_to_consider_as_an/) , 2024-11-24-0914
```
Hi there, I am a current PhD student in Artificial Intelligence working on Multi-Armed Bandits. More recently, I have co
mpleted one of my works on the intersection of Bandits and LLMs and was wondering for a suitable venue for publication.


The closest conference I see is ICML having deadline of 31st January which is about two months from now, therefore was 
wondering about a suitable alternate venue. While previous reddit threads (a year back) claim that TMLR is better than A
AAI, IJCAI and similar conferences but falls way short compared to ICML, NeurIPS, ICLR, etc, I was wondering if it's sti
ll true. 

Does the ML community still considers TMLR to be a potential place to submit it, given that the deadline for 
the closest conference is too far?
```
---

     
 
all -  [ Neural network recognizer for hand-written zip code digits (1988): 'with a high-performance preproce ](https://www.reddit.com/r/mlscaling/comments/1ggr0j4/neural_network_recognizer_for_handwritten_zip/) , 2024-11-24-0914
```
This paper was published just before LeNet-1. Notable features:

* 18 hand-designed kernels (??).
* An early bitter less
on? 'In the early phases of the project, we found that neural network methods gave rather mediocre results. Later, with 
a high-performance preprocessor, plus a large training database, we found that a layered network gave the best results, 
surpassing even Parzen Windows.'
   * 'Several different classifiers were tried, including Parzen Windows, K nearest nei
ghbors, highly customized layered networks, expert systems, matrix associators, fea ture spins, and adaptive resonance. 
We performed preliminary studies to identify the most promising methods. We determined that the top three methods in thi
s list were significantly better suited to our task than the others, and we performed systematic comparisons only among 
those three \[Parzen Windows, KNN, neural networks\].'
* Nevermind, seems they didn't take the bitter lesson. 'Our metho
ds include low-precision and analog processing, massively parallel computation, extraction of biologically-motivated fea
tures, and learning from examples. We feel that this is, therefore, a fine example of a Neural Information Processing Sy
stem. We emphasize that old-fashioned engineering, classical pattern recognition, and the latest learning-from-examples 
methods were all absolutely necessary. Without the careful engineering, a direct adaptive network attack would not succe
ed, but by the same token, without learning from a very large database, it would have been excruciating to engineer a su
fficiently accurate representation of the probability space.'

Denker, John, et al. '[Neural network recognizer for hand
-written zip code digits](https://proceedings.neurips.cc/paper/1988/hash/a97da629b098b75c294dffdc3e463904-Abstract.html)
.' *Advances in neural information processing systems* 1 (1988).
```
---

     
 
all -  [ Florence-2-as-a-Judge ](https://www.reddit.com/r/LocalLLaMA/comments/1gfv0me/florence2asajudge/) , 2024-11-24-0914
```
I learned about Judge Distillation from slide 14 in [this deck](https://nips.cc/media/neurips-2023/Slides/83968_5GxuY2z.
pdf) describing how Phi-2 researchers scaled their data quality filter to a large synthetic dataset.

I'm planning to sc
ale up data synthesis for the [OpenSpaces dataset](https://huggingface.co/datasets/remyxai/OpenSpaces) and have found I 
can use [SpaceLLaVA](https://huggingface.co/remyxai/SpaceLLaVA) in VLM-as-a-Judge with [prometheus-vision](https://githu
b.com/prometheus-eval/prometheus-vision). Check out the [SpaceJudge Dataset](https://huggingface.co/datasets/salma-remyx
/SpaceJudgeDataset) to see the an assessment of a small split.

Now, I'm fine-tuning Florence-2 on this dataset, introdu
cing the new <JUDGE> task to help filter out low-quality synthetic samples. Here's the [experiment collection](https://h
uggingface.co/collections/salma-remyx/vlm-judge-distillation-671fc8fe1925c49630307a82).

Will discuss some of this at OD
SC West tomorrow, let's connect!


```
---

     
 
all -  [ [D]ended up with a poster in NuerIPS-24 ](https://www.reddit.com/r/MachineLearning/comments/1gdxef5/dended_up_with_a_poster_in_nuerips24/) , 2024-11-24-0914
```
I have a poster in NuerIPS this year through the  journal track(MLRC) along with the main conference papers.I didnt expe
ct this to happen so i hadnt planned/researched about the expenses/funding prior.I already had my visa and conference re
gistration arranged but have no clue about further proceedings of Nuerips and how to fund it(i am an UG junior).If you h
ave already attended NeurIPS before please pour your ideas and experiences.
```
---

     
 
all -  [ Looking for collaborations on ongoing work-in-progress Full Papers targeting conferences like CVPR,  ](https://www.reddit.com/r/computervision/comments/1gd6812/looking_for_collaborations_on_ongoing/) , 2024-11-24-0914
```
Hey everyone,

Our group, **Vision and Language Group, IIT Roorkee,** recently got three workshop papers accepted at Neu
rIPS workshops! 🚀 We’ve also set up a website 👉 [VLG](https://vlgiitr.github.io/), featuring other publications we’ve wo
rked on, so our group is steadily building a portfolio in ML and AI research. Right now, we’re collaborating on several 
work-in-progress papers with the aim of full submissions to top conferences like CVPR and ICML.

That said, we have even
 more ideas we’re excited about. Still, a few of our main limitations have been access to proper guidance and funding fo
r GPUs and APIs, which is crucial for experimenting and scaling some of our concepts. If you or your lab is interested i
n working together, we’d love to explore intersections in our fields of interest and any new ideas you might bring to th
e table!

If you have resources available or are interested in discussing potential collaborations, please feel free to 
reach out! Looking forward to connecting and building something impactful together! Here is the link for our Open Slack 
👉 [Open Slack](https://join.slack.com/t/vlgopenspace/shared_invite/zt-2t7kihcc6-uilU~y7lz7jdtqNc5M1VPA)
```
---

     
 
all -  [ Looking for collaborations on ongoing work-in-progress Full Papers targeting conferences like CVPR,  ](https://www.reddit.com/r/neuralnetworks/comments/1gd64zq/looking_for_collaborations_on_ongoing/) , 2024-11-24-0914
```
# Hey everyone,

Our group, **Vision and Language Group, IIT Roorkee,** recently got three workshop papers accepted at N
eurIPS workshops! 🚀 We’ve also set up a website 👉 [VLG](https://vlgiitr.github.io/), featuring other publications we’ve 
worked on, so our group is steadily building a portfolio in ML and AI research. Right now, we’re collaborating on severa
l work-in-progress papers with the aim of full submissions to top conferences like CVPR and ICML.

That said, we have ev
en more ideas we’re excited about. Still, a few of our main limitations have been access to proper guidance and funding 
for GPUs and APIs, which is crucial for experimenting and scaling some of our concepts. If you or your lab is interested
 in working together, we’d love to explore intersections in our fields of interest and any new ideas you might bring to 
the table!

If you have resources available or are interested in discussing potential collaborations, please feel free t
o reach out! Looking forward to connecting and building something impactful together! Here is the link for our Open Slac
k 👉 [Open Slack](https://join.slack.com/t/vlgopenspace/shared_invite/zt-2t7kihcc6-uilU~y7lz7jdtqNc5M1VPA)
```
---

     
 
MachineLearning -  [ [R] Paper summaries for some of our papers that recently got accepted in NeurIPS ](https://www.reddit.com/r/MachineLearning/comments/1gb74j6/r_paper_summaries_for_some_of_our_papers_that/) , 2024-11-24-0914
```
Hey everyone, here is the list of papers by our groups that got accepted recently in NeurIPS 2024; It is a proud moment 
for us as an all-UG group; all the papers were published without any external support from the academia; here is a summa
ry of our papers. We hope this inspires others to pursue AI and look into research as a perspective where we can work to
gether, and all you require is the right guidance (not even necessarily a PhD or a professor). If you find these papers 
useful and want to working/collabrating with us, feel free to connect with us!

* Give me a hint: Can LLMs take a hint t
o solve math problems? 👉 [Arxiv link](https://arxiv.org/abs/2410.05915)
   * We propose improving LLM performance on adv
anced math problems using 'hints,' inspired by human pedagogy. We also test the model's robustness to incorrect hints. O
ur approach is evaluated on various LLMs using diverse problems from the MATH dataset, comparing it with one-shot, few-s
hot, and chain of thought prompting.
* Attention Shift: Steering AI Away from Unsafe Content 👉 [Arxiv link](https://arxi
v.org/abs/2410.04447)
   * This study explores methods to restrict unsafe content in generative models. We propose a nov
el training-free approach using attention reweighing to remove unsafe concepts during inference. Our method is compared 
to existing techniques, evaluated on direct and adversarial jailbreak prompts. We also discuss potential causes, limitat
ions, and broader implications.
* Unmasking the Veil: An Investigation into Concept Ablation for Privacy and Copyright P
rotection in Images 👉 [Arxiv link](https://arxiv.org/abs/2406.12592v1)
   * This paper extends the study of concept abla
tion in pre-trained models, as introduced by Kumari et al. (2022). We reproduce results from various concept ablation te
chniques and propose a novel variant, 'trademark ablation,' to address branded elements in model outputs. We also analyz
e the model's limitations, behavior under ablation leakage prompts, and performance degradation on unrelated concepts.


**The Vision Language Group at IIT Roorkee** has compiled an excellent repository of **comprehensive summaries** for dee
p learning papers from top conferences like **NeurIPS, CVPR, ICCV, and ICML (2016-2024)**. These summaries break down ke
y papers in computer vision, NLP, and machine learning—perfect if you want to stay updated without diving deep into the 
full papers.
```
---

     
