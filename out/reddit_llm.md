 
all -  [ Cold Email Personalization with AI ](https://www.reddit.com/r/Latenode/comments/17rqop0/cold_email_personalization_with_ai/) , 2023-11-10-0909
```
https://preview.redd.it/7y5z2dhojezb1.png?width=1920&format=png&auto=webp&s=33b37a09b5bb7ed306a37d42632fe5efe6637dc9

Hi
! In this article, I will explain how the AI framework LangChain can significantly enhance the quality of your cold emai
l outreach by making it unique and personalized. I will also discuss how to automate this entire process with minimal co
sts using a low-code platform and share ready-made templates for a quick start.

## Personalization vs Automation

There
's a natural tension between personalization and automation. Non-personalized, generic emails are easy to automate but o
ften result in low engagement and conversion rates. In contrast, highly personalized emails increase engagement but are 
difficult to automate.

https://preview.redd.it/qrctutp5kezb1.png?width=1470&format=png&auto=webp&s=afa3c8699642fec4b878
9b021c8c610c8d2d1f32

Cold email platforms now help solve this issue with dynamic variables that add a personalized touc
h to automated emails. These variables act as placeholders for inserting personalized words, lines, or paragraphs.

http
s://preview.redd.it/hs5e5gb8kezb1.png?width=1470&format=png&auto=webp&s=6be432712e82afe9fa3c9d6737be21cad50949fd

Dynami
c variables allow companies to balance personalization and automation efficiently. Today, we'll create a LangChain scena
rio on the low-code platform Latenode to generate a customized cold email icebreaker for each contact in our outreach da
tabase using the following tools:

* The free data enrichment tool ClearBit
* The free low-code platform Latenode
* Open
AI's extremely cheap API.

## Step 1: enrich emails w/ ClearBit

Let's start with a Google Sheet containing basic email 
addresses. I've included some of my work emails as real examples (please refrain from sending me personalized cold email
s after reading this! :) )

https://preview.redd.it/p72rr6nbkezb1.png?width=1180&format=png&auto=webp&s=25125e61313f91a6
ed008dbd7ce7f7aefe0ab215

First, we need to enrich these emails with data about the recipients. For our outreach, we nee
d to know:

* The first name
* The company name
* The company description

You could manually visit each email domain to
 gather this information, but if you have hundreds or thousands of emails in your database, that's not practical. Instea
d, we can automate this task using the low-code platform Latenode. We link our Google Sheet there and use the ClearBit A
PI to fill in the missing information. Here's how it works:

https://preview.redd.it/6ghryvcfkezb1.png?width=1600&format
=png&auto=webp&s=6276c1ab307e8b6e956fe8b41f6bffade46cb3bc

Don't worry! You don't have to create everything from the beg
inning. Simply copy the scenario I provide at the end of this article. The basic steps of this automation are:

* Identi
fy the rows that need enrichment.
* Extract the email from each row.
* Send the email to ClearBit and receive all the re
lated information.
* Enter the required information back into the Google Sheet.

https://i.redd.it/mi4xu9ztkezb1.gif

 T
hat's it. We've enriched our emails with essential details like the company description. Now, let's craft a personalized
 icebreaker to kick off our cold emails and establish a personal connection right from the start. 

## Step 2: generate 
personalized icebreaker w/ ChatGPT

Giving a compliment about what your recipient does at their workplace is the very le
ast you can do. Additionally, you could tailor your outreach reason based on the company's profile. You can do this with
 another Latenode scenario, which you'll be able to copy later.

https://preview.redd.it/nkf8f1t5lezb1.png?width=1600&fo
rmat=png&auto=webp&s=fc17d295329f206dd81417fc97fdad217142d4d4

Its main steps are:

* Retrieve the company description f
rom your Google Sheet.
* Send this description to ChatGPT using the OpenAI API with a custom prompt tailored to your nee
ds.
* Refine the AI-generated output with another request and a different prompt.
* Place the final result in the row co
rresponding to the person you're reaching out to.

 By doing this, we attach a personalized icebreaker to each individua
l, creating another custom variable in addition to their first name and company name. This trio should suffice for a sta
rt. Let's look at how this functions: 

https://i.redd.it/n4tcjn2flezb1.gif

## Step 3: upload spreadsheet to cold email
 platform w/ Apollo

First, download your spreadsheet as a CSV file. Then, upload it to your email platform as a new lis
t. I'll demonstrate using Apollo, but the process is similar in other tools.

https://preview.redd.it/bbi4utsjlezb1.png?
width=1174&format=png&auto=webp&s=8ee6786f0c98dd087b113a55e6f4756c1b660cbd

The next steps are pretty standard – map the
 fields and assign a variable to each. The key variable for us is the custom 'icebreaker' field.

https://preview.redd.i
t/ud57pjbmlezb1.png?width=1600&format=png&auto=webp&s=afaaab7c4e4067a488843bf0bb7b04747d83c2a0

 Now, when composing an 
email for a prospect, it works like this: 

https://preview.redd.it/9kxv3swslezb1.png?width=1600&format=png&auto=webp&s=
7efd90d2c90dfb2e849d2ee262ea77abcb1fa911

That's all for now. You can adjust the prompts sent to GPT in your Latenode sc
enario to achieve any level of cold email customization. These Latenode templates are versatile for any cold outreach sc
enario, including personalized LinkedIn messages.

**⭐ As promised, here is the link to Discord server where you can cop
y my scenarios:** [**Template Library**](https://discord.gg/mcZRPHN9eb)

You just need to paste them into [app.latenode.
com](https://app.latenode.com) and input your API keys for ClearBit (which is free) and OpenAI (which is very affordable
). Latenode itself is also free and has a supportive community where the team is always ready to help with your automati
on journey
```
---

     
 
all -  [ CSS Selector Extraction Using LangChain ](https://www.reddit.com/r/LangChain/comments/17rqn55/css_selector_extraction_using_langchain/) , 2023-11-10-0909
```
I’m looking to automate the process of extracting CSS selectors from lengthy HTML pages for Scrapy projects. Even after 
cleaning up the HTML by removing unnecessary elements, comments, and text, the size often exceeds the context limits of 
LLMs like GPT.

The idea is to use LangChain to handle these large HTML documents more effectively. Could anyone share t
heir insights or strategies on how to implement this on LangChain?

I know about RAG but the challenge I’m facing is tha
t I have to split the HTML in chunks and it’s likely that for some cases the chunk is no enough for the LLM to infer the
 CSS selector (it would need to traverse the whole HTML like a tree data structure).

 Any suggestions or ideas are welc
ome!
```
---

     
 
all -  [ Personalization of Cold Email Campaigns Using AI and Low Code - Sharing the Scenario ](https://www.reddit.com/r/Automate/comments/17rqkht/personalization_of_cold_email_campaigns_using_ai/) , 2023-11-10-0909
```
Hello r/Automate community! In this article, I will explain how the AI framework LangChain can significantly enhance the
 quality of your cold email outreach by making it unique and personalized. I will also discuss how to automate this enti
re process with minimal costs using a low-code platform and share ready-made templates for a quick start.

## Personaliz
ation vs Automation

There's a natural tension between personalization and automation. Non-personalized, generic emails 
are easy to automate but often result in low engagement and conversion rates. In contrast, highly personalized emails in
crease engagement but are difficult to automate.

https://preview.redd.it/ang7x0o6kezb1.png?width=1470&format=png&auto=w
ebp&s=1e4618cb36229f97a2f8781e3adc7f1f393645c5

Cold email platforms now help solve this issue with dynamic variables th
at add a personalized touch to automated emails. These variables act as placeholders for inserting personalized words, l
ines, or paragraphs.

https://preview.redd.it/ueon3ap7kezb1.png?width=1470&format=png&auto=webp&s=ed76a72fc03ca5479379af
558b046273b5ebc91b

Dynamic variables allow companies to balance personalization and automation efficiently. Today, we'l
l create a LangChain scenario on the low-code platform Latenode to generate a customized cold email icebreaker for each 
contact in our outreach database using the following tools:

* The free data enrichment tool ClearBit
* The free low-cod
e platform Latenode
* OpenAI's extremely cheap API.

## Step 1: enrich emails w/ ClearBit

Let's start with a Google She
et containing basic email addresses. I've included some of my work emails as real examples (please refrain from sending 
me personalized cold emails after reading this! :) )

https://preview.redd.it/6t6np9mckezb1.png?width=1180&format=png&au
to=webp&s=7c265eb1facb95d616f3f24ccefcd877a22f3225

First, we need to enrich these emails with data about the recipients
. For our outreach, we need to know:

* The first name
* The company name
* The company description

You could manually 
visit each email domain to gather this information, but if you have hundreds or thousands of emails in your database, th
at's not practical. Instead, we can automate this task using the low-code platform Latenode. We link our Google Sheet th
ere and use the ClearBit API to fill in the missing information. Here's how it works:

https://preview.redd.it/ftnpaa3ek
ezb1.png?width=1600&format=png&auto=webp&s=31237df052fb1d9d6a66acd7706ac3064fff1fea

Don't worry! You don't have to crea
te everything from the beginning. Simply copy the scenario I provide at the end of this article. The basic steps of this
 automation are:

* Identify the rows that need enrichment.
* Extract the email from each row.
* Send the email to Clear
Bit and receive all the related information.
* Enter the required information back into the Google Sheet.

https://i.red
d.it/xwodo3rvkezb1.gif

That's it. We've enriched our emails with essential details like the company description. Now, l
et's craft a personalized icebreaker to kick off our cold emails and establish a personal connection right from the star
t.

## Step 2: generate personalized icebreaker w/ ChatGPT

Giving a compliment about what your recipient does at their 
workplace is the very least you can do. Additionally, you could tailor your outreach reason based on the company's profi
le. You can do this with another Latenode scenario, which you'll be able to copy later.

https://preview.redd.it/uifg3we
6lezb1.png?width=1600&format=png&auto=webp&s=0367dd0076899fe516c33955ae7eee0b391764ed

Its main steps are:

* Retrieve t
he company description from your Google Sheet.
* Send this description to ChatGPT using the OpenAI API with a custom pro
mpt tailored to your needs.
* Refine the AI-generated output with another request and a different prompt.
* Place the fi
nal result in the row corresponding to the person you're reaching out to.

By doing this, we attach a personalized icebr
eaker to each individual, creating another custom variable in addition to their first name and company name. This trio s
hould suffice for a start. Let's look at how this functions:

https://i.redd.it/ju77m4xclezb1.gif

## Step 3: upload spr
eadsheet to cold email platform w/ Apollo

First, download your spreadsheet as a CSV file. Then, upload it to your email
 platform as a new list. I'll demonstrate using Apollo, but the process is similar in other tools.

https://preview.redd
.it/hxs9nmjklezb1.png?width=1174&format=png&auto=webp&s=a5ab042de77690b1ca5cdba85b688182c52eb3e0

The next steps are pre
tty standard – map the fields and assign a variable to each. The key variable for us is the custom 'icebreaker' field.


https://preview.redd.it/rsiye3qllezb1.png?width=1600&format=png&auto=webp&s=365564bdf6584843d0e6e259c0824939b1a68221

No
w, when composing an email for a prospect, it works like this:

https://preview.redd.it/3erpu7dslezb1.png?width=1600&for
mat=png&auto=webp&s=e7cc1f77be1834b6660e0de4d8a7022133d55e85

That's all for now. You can adjust the prompts sent to GPT
 in your Latenode scenario to achieve any level of cold email customization. These Latenode templates are versatile for 
any cold outreach scenario, including personalized LinkedIn messages.

⭐  As I promised, here are the links to copy thes
e scenarios: [**Data Enrichment**](https://www.notion.so/latenode/DATA-ENRICHMENT-d59d0d43bcea4f9bb3bbaa29dadcc718)  and
 [**Icebreaker Generation**](https://www.notion.so/latenode/ICEBREAKERS-GENERATION-40ca832750f24512bdb61fcbf5d04ae7)

Yo
u just need to paste them into [app.latenode.com](https://app.latenode.com) and input your API keys for ClearBit (which 
is free) and OpenAI (which is very affordable). Latenode itself is also free and has a supportive community where the te
am is always ready to help with your automation journey
```
---

     
 
all -  [ Question about Langchain and Open Source LLMs ](https://www.reddit.com/r/LocalLLaMA/comments/17rqhs7/question_about_langchain_and_open_source_llms/) , 2023-11-10-0909
```
I have been experimenting with Langchain. I tried getting Llama 2 13b to use Langchain tools. I also tried running Code 
Llama as an SQL agent. I always get the error 'Could not parse LLM output.' I am trying to build an application that can
 generate SQL queries from natural language and has some form of memory of conversational history. When I looked online 
for the error 'Could not parse LLM output' most people were using OpenAI not open source LLMs and people were saying the
 error seems to be that the LLM is not following the required format 'Action Thought Observation' etc. Are there any sma
ll open source LLMs (that can run on CPU) that work with Langchain to do things like using tools and having conversation
al memory? Bonus points if they can generate SQL. Or does this kind of thing require larger more powerful models? I got 
fairly good results on SQL generation using NSQL-350m (50% on Spider) which can run on CPU, but I don't think this model
 will work with Langchain.
```
---

     
 
all -  [ I've Created a Free Tool for Personalizing Your Cold Email Campaigns Using Low Code and AI ](https://www.reddit.com/r/SideProject/comments/17rq3lp/ive_created_a_free_tool_for_personalizing_your/) , 2023-11-10-0909
```
Hello r/SideProject community! In this article, I will explain how the AI framework LangChain can significantly enhance 
the quality of your cold email outreach by making it unique and personalized. I will also discuss how to automate this e
ntire process with minimal costs using a low-code platform and share ready-made templates for a quick start.

## Persona
lization vs Automation

There's a natural tension between personalization and automation. Non-personalized, generic emai
ls are easy to automate but often result in low engagement and conversion rates. In contrast, highly personalized emails
 increase engagement but are difficult to automate.

https://preview.redd.it/b2fzk6c6kezb1.png?width=1470&format=png&aut
o=webp&s=8762bcfb7bedbe20c442e18a90bf61ad48b5da2d

Cold email platforms now help solve this issue with dynamic variables
 that add a personalized touch to automated emails. These variables act as placeholders for inserting personalized words
, lines, or paragraphs.

https://preview.redd.it/8juap908kezb1.png?width=1470&format=png&auto=webp&s=254d946e776962ad93f
8ba4fe30fefe484fa5027

Dynamic variables allow companies to balance personalization and automation efficiently. Today, w
e'll create a LangChain scenario on the low-code platform Latenode to generate a customized cold email icebreaker for ea
ch contact in our outreach database using the following tools:

* The free data enrichment tool ClearBit
* The free low-
code platform Latenode
* OpenAI's extremely cheap API.

## Step 1: enrich emails w/ ClearBit

Let's start with a Google 
Sheet containing basic email addresses. I've included some of my work emails as real examples (please refrain from sendi
ng me personalized cold emails after reading this! :) )

https://preview.redd.it/od8bm82ckezb1.png?width=1180&format=png
&auto=webp&s=f75ffb0043295c5182b358c022aa944e04c32719

First, we need to enrich these emails with data about the recipie
nts. For our outreach, we need to know:

* The first name
* The company name
* The company description

You could manual
ly visit each email domain to gather this information, but if you have hundreds or thousands of emails in your database,
 that's not practical. Instead, we can automate this task using the low-code platform Latenode. We link our Google Sheet
 there and use the ClearBit API to fill in the missing information. Here's how it works:

https://preview.redd.it/n7r8iy
0fkezb1.png?width=1600&format=png&auto=webp&s=2c63d26dce877bbf816004f0049e7bc5bca1f2dd

Don't worry! You don't have to c
reate everything from the beginning. Simply copy the scenario I provide at the end of this article. The basic steps of t
his automation are:

* Identify the rows that need enrichment.
* Extract the email from each row.
* Send the email to Cl
earBit and receive all the related information.
* Enter the required information back into the Google Sheet.

https://i.
redd.it/06wtd65vkezb1.gif

That's it. We've enriched our emails with essential details like the company description. Now
, let's craft a personalized icebreaker to kick off our cold emails and establish a personal connection right from the s
tart.

## Step 2: generate personalized icebreaker w/ ChatGPT

Giving a compliment about what your recipient does at the
ir workplace is the very least you can do. Additionally, you could tailor your outreach reason based on the company's pr
ofile. You can do this with another Latenode scenario, which you'll be able to copy later.

https://preview.redd.it/nps5
tp26lezb1.png?width=1600&format=png&auto=webp&s=7390dc0303b4e3e4cc95d5892a4dffbd4289388b

Its main steps are:

* Retriev
e the company description from your Google Sheet.
* Send this description to ChatGPT using the OpenAI API with a custom 
prompt tailored to your needs.
* Refine the AI-generated output with another request and a different prompt.
* Place the
 final result in the row corresponding to the person you're reaching out to.

By doing this, we attach a personalized ic
ebreaker to each individual, creating another custom variable in addition to their first name and company name. This tri
o should suffice for a start. Let's look at how this functions:

https://i.redd.it/hjerdubelezb1.gif

## Step 3: upload 
spreadsheet to cold email platform w/ Apollo

First, download your spreadsheet as a CSV file. Then, upload it to your em
ail platform as a new list. I'll demonstrate using Apollo, but the process is similar in other tools.

https://preview.r
edd.it/unma866klezb1.png?width=1174&format=png&auto=webp&s=15d34921b3f61508d5232d86446fcbd697ae56fd

The next steps are 
pretty standard – map the fields and assign a variable to each. The key variable for us is the custom 'icebreaker' field
.

https://preview.redd.it/gn0tz81mlezb1.png?width=1600&format=png&auto=webp&s=3c416f1834f840dc6a534f562e2393cbaf1a0ccb


Now, when composing an email for a prospect, it works like this:

https://preview.redd.it/cn1eyonslezb1.png?width=1600&
format=png&auto=webp&s=d4a8c5a660eb86210faa15bc1eac25d0a3ecd06f

That's all for now. You can adjust the prompts sent to 
GPT in your Latenode scenario to achieve any level of cold email customization. These Latenode templates are versatile f
or any cold outreach scenario, including personalized LinkedIn messages.

⭐  As I promised, here are the links to copy t
hese scenarios: [**Data Enrichment**](https://www.notion.so/latenode/DATA-ENRICHMENT-d59d0d43bcea4f9bb3bbaa29dadcc718)  
and [**Icebreaker Generation**](https://www.notion.so/latenode/ICEBREAKERS-GENERATION-40ca832750f24512bdb61fcbf5d04ae7)


You just need to paste them into [app.latenode.com](https://app.latenode.com) and input your API keys for ClearBit (whi
ch is free) and OpenAI (which is very affordable). Latenode itself is also free and has a supportive community where the
 team is always ready to help with your automation journey
```
---

     
 
all -  [ [P] GPT vs. StarCraft ](https://www.reddit.com/r/MachineLearning/comments/17ro6el/p_gpt_vs_starcraft/) , 2023-11-10-0909
```
This is the first in a series of webcasts covering the development and experimentation of using GPT algorithms, LangChai
n and Python to control the high-level strategy of a StarCraft II bot. I’ll be running through the basics of the impleme
ntation, discussing the use of prompts and prompt engineering, and demonstrating the implementation in action.

[https:/
/youtu.be/E3Sj2L6ZnXA](https://youtu.be/E3Sj2L6ZnXA)
```
---

     
 
all -  [ Is langchain still useful? ](https://www.reddit.com/r/OpenAI/comments/17rlrkd/is_langchain_still_useful/) , 2023-11-10-0909
```
tittle
```
---

     
 
all -  [ Tutorial on creating an automated CI pipeline for your LangChain system ](https://www.reddit.com/r/LLMDevs/comments/17rkhpr/tutorial_on_creating_an_automated_ci_pipeline_for/) , 2023-11-10-0909
```
Hello community,

My team and I are working on how to enable developers building LLM powered apps to automate test runni
ng when they update their evals. [We've published a blog post here about it.](https://circleci.com/blog/build-evaluate-l
lm-apps-with-langchain/)

For now it's a bit of a hacky way but we are also trying to build new features on our product 
([CircleCI](https://www.circleci.com)) so that this bridge between the 2 tools is reflected in the UI... I was curious t
o hear from you folks if this is of any interest to you?
```
---

     
 
all -  [ [For Hire] Programmer/Web Developer/IT Consultant (Python, PHP, AI, etc.) ](https://www.reddit.com/r/forhire/comments/17rjxfn/for_hire_programmerweb_developerit_consultant/) , 2023-11-10-0909
```
To get in contact, please **message** me, I **don't** use the chat thing and might miss you or reply very late. Then we 
can switch to email/discord/telegram or whatever else. Apologies for starting with this, but many missed it when it was 
lower.

I'm a programmer/web developer with 12 years of professional experience. I am available for all sorts of program
ming and web development tasks.

I also offer consulting services. If you need something done, but don't know how exactl
y, I can help. I'm an excellent researcher and I communicate well. I will work with you to find the best solution for yo
ur problem.

My services include, but are not limited to:

* websites

* desktop applications

* AI integration (chatGPT
 API, langchain, whatever else turns up)

* integration with APIs and other webservices

* all kinds of scripts

* task 
automation

* website optimization

* debugging

* plugins for existing software

* bots (Reddit, Telegram, etc)

If you
're looking for someone to take care of a variety of different tasks, I can offer continuous support.

My preferred envi
ronment is Python with Django, but I work with anything Python or PHP based, including Wordpress. I also do frontend stu
ff with JavaScript, jQuery, AJAX. I also have no problem with learning new technologies that are needed for the project.


Rate is $50/h. Can also do fixed price by project, but only if the project/milestone is well-defined.

Satisfied custo
mers:

https://www.reddit.com/r/testimonials/comments/2e8gqy/pos_uqui_need_a_backend_web_dev_look_no_further/

https://w
ww.reddit.com/r/testimonials/comments/7fsdze/pos_hiring_uqui_was_an_example_of_how_it_should/

https://www.reddit.com/r/
testimonials/comments/80pu9l/pos_uqui_great_work_detailed_and_fast/

https://www.reddit.com/r/testimonials/comments/b0nx
68/uqui_is_a_hardworking_intelligent_honest_apps/

https://www.reddit.com/r/testimonials/comments/j3mz3p/uqui_is_a_great
_web_development_consultant_with/

https://www.reddit.com/r/testimonials/comments/v40ay3/pos_uqui_is_a_great_backend_dev
_to_work_with/

Some examples of sites I worked on: http://bdabkowski.yum.pl/

Please note: I am **not** a designer.
```
---

     
 
all -  [ Need an advice ](https://www.reddit.com/r/careeradvice/comments/17rirg3/need_an_advice/) , 2023-11-10-0909
```
My bachelor's degree is in Industrial Automation and Robotics and I have a masters in Advanced Software Engineering. I'm
 currently working on inhouse projects of my current company. some of them on a proprietary outdated IoT platform (DGLux
) . But I have also worked on Building inhouse chatbots using Python, GPT 4, Vectorstores, and Langchain. Also I do have
 some experience in ReactJS,C# andNode-Red as well. But I don't see any clear path around this kind of tech stack. When 
it comes to academics I do have some experience in ML model development as well. Expecting a ideas to level up as an eng
ineer. I am planning to switch in to ML career or Ios apps devlopment. Any suggestions?
```
---

     
 
all -  [ Tutorial DnD Langchain ](https://www.reddit.com/r/LangChain/comments/17ri80z/tutorial_dnd_langchain/) , 2023-11-10-0909
```
Hello everyone

Someone know where I can find the example of langchain agent's playing DnD? I want to use it for a team 
building :) 
I don't find it again. 

If it was deleted, what is the reason?
```
---

     
 
all -  [ Has anyone here incorporated OpenAI's Threads API as Memory in their conversational chains? ](https://www.reddit.com/r/LangChain/comments/17rhqd8/has_anyone_here_incorporated_openais_threads_api/) , 2023-11-10-0909
```
Seems like it would work perfectly as a plug and play memory component, curious if there are any gotcha's before I try i
mplementing it myself.
```
---

     
 
all -  [ How do we know RAG is returning accurate results? ](https://www.reddit.com/r/LangChain/comments/17rfr0d/how_do_we_know_rag_is_returning_accurate_results/) , 2023-11-10-0909
```
Hi all,

This is a topic my team has been researching and interested in hearing your thoughts as well.

As a little back
ground, we hosted a LinkedIn Live yesterday on 'Overviewing RAG Approaches' and generally keeping up with RAG developmen
ts. A lot of people from reddit joined and gave great feedback that the session was helpful -- we're grateful for this. 
*(If you missed it, the recording is* [*here*](https://www.youtube.com/watch?v=twM_9CM_3RY)*)*

We want to continue shar
ing our knowledge with the community and are hosting another session next Wed on 'Evaluating RAG Performance' where we'l
l cover:

* BLEU
* ROGUE
* RAGAS
* Deepeval
* and more

We've been doing a ton of research in this area and are looking 
forward to sharing/discussing with you via [next week's live session](https://bit.ly/3QxkhMv). There are literally new d
evelopments every day on this topic

Anything you want to learn more about RAG performance just let us know! And if you'
ve had good successes in evaluation/testing, please share you experience!

&#x200B;
```
---

     
 
all -  [ Extracting summary from each item as chunks then QA all items ](https://www.reddit.com/r/LangChain/comments/17rfbuc/extracting_summary_from_each_item_as_chunks_then/) , 2023-11-10-0909
```
Hello all, I have been looking for solutions for this problem but struggling and would appreciate some help

I am using 
RAG approach with langchain to QA my documents, assuming a big list of github issues. I would like to extract summary fo
r each issue as chunks, and be able to do Question Answering on all issues. 

Are there any keywords and sources I could
 look into for this, or related work people have done? Any help is super appreciated. Cheers
```
---

     
 
all -  [ 🗺️ Well maintained guide to current state of AI and LLMs, for beginners/ non-tech professionals? ](https://www.reddit.com/r/LocalLLaMA/comments/17rbzgj/well_maintained_guide_to_current_state_of_ai_and/) , 2023-11-10-0909
```
Hi team

There are a lot of components out there that come together in different configurations to conjure up AIs. Thing
s like:

Xb model Y
Fine tuning
Hallucinations
Llama
Ollama
LangChain
LocalGPT
AutoGPT
PrivateGPT

All come up frequentl
y.

Is there a good guide to build up my intelligence and vocabulary? Ideally some diagrams to help me understand how ea
ch component functions/ fits together.

I'm grateful for your help!!
```
---

     
 
all -  [ Why is GPT-4-Turbo incapable of generating the simplest code to access GPT-3 or GPT-4 via Python? ](https://www.reddit.com/r/ChatGPT/comments/17rbtzz/why_is_gpt4turbo_incapable_of_generating_the/) , 2023-11-10-0909
```
I was really excited about GPT-4-Turbo because of the new cutoff of April 2023. The first thing I tried was ask it to ge
nerate a super basic python script for interacting with GPT-3 but the code it produces fails to work.  


My only theory
 is that the API that was used in April of this year is already deprecated and replaced by different syntax/api.  


Doe
s anyone know how I can get it to output working code for interacting with openai through python or Langchain?
```
---

     
 
all -  [ What's the point of LangChain for chaining LLM outputs if I could just pass the output of the first  ](https://www.reddit.com/r/LangChain/comments/17rb5zl/whats_the_point_of_langchain_for_chaining_llm/) , 2023-11-10-0909
```
I'm kind of new to this and I feel stupid. I'm looking at LangChain in IBM notebook samples. For example, assuming we ha
ve initialized the models LLM1 and LLM2:

&#x200B;

`instruction = 'Give me a list of red fruits.'`

`output1 = LLM1(ins
truction)`

`output2 = LLM2(f'Write a story using these fruits: {output1})`

&#x200B;

How is this any different from us
ing SimpleSequentialChain in LangChain?

&#x200B;
```
---

     
 
all -  [ How to generate similar full documents (contrat, commercial proposition, technical notes...) based o ](https://www.reddit.com/r/LangChain/comments/17ra9eg/how_to_generate_similar_full_documents_contrat/) , 2023-11-10-0909
```
Hi Folks !  


For my personal and professional project I'm looking for a solution to reproduce documents (contrat, comm
ercial proposition, technical notes or whatever) based on existing ones on a Chromadb or Pinecone and with a minimum of 
data processing of these document before their vectorization.  


Here my thoughs :

* RAG allows to de dense or sparse 
retrieval based on chunked documents in order to extract information. But the chunk aspect seem to make complexe the fac
t of reproducing document. But such a possibility could be a very big game changer for many companies.   

* As the cont
ext window is limited (let's say 100K with Claude) but these documents can be way bigger, how  would it be possible to s
ent a request to a LLM (ex : do a RH contract for XXX, base on these information : \[{keys : values}\] and to return a f
ull documents inspired by existing ones on the dB ?  


Should we create a iteration of the document bien precise chunks
 ? Which could mean that a pre-processing of these documents would be necessary to parse them by idea/paragraph ?  


A 
very cool way woudl be just to upload, for exemple, an all family of RH contracts for many positions. And them to be abl
e to reproduce a full documents just based on provided information.  


Maybe i didn't fully understand the RAG and this
 is already possible. But I have some doubts. If some of you have ideas, ongoing project or already published Github, th
at would be awesome !  


Code safe & Good day !  

```
---

     
 
all -  [ Guidance and LM Studio issue ](https://www.reddit.com/r/LocalLLaMA/comments/17r9pu6/guidance_and_lm_studio_issue/) , 2023-11-10-0909
```
Hi all,

I'm trying to make it work Guidance with LM Studio. This is my code:

    from langchain.llms import OpenAI
   
 import guidance
    
    llm = OpenAI(
            openai_api_key='NULL',
            temperature=0,
            openai
_api_base='http://localhost:1234/v1',
            max_tokens=-1
    )
    
    guidance.llm = llm
    
    program = gui
dance('''Tweak this proverb to apply to model instructions instead.
    
    {{proverb}}
    - {{book}} {{chapter}}:{{ve
rse}}
    
    UPDATED
    Where there is no guidance{{gen 'rewrite' stop='\\n-'}}
    - GPT {{#select 'chapter'}}9{{or}
}10{{or}}11{{/select}}:{{gen 'verse'}}''')
    
    # execute the program on a specific proverb
    executed_program = p
rogram(
        proverb='Where there is no guidance, a people falls,\nbut in an abundance of counselors there is safety.
',
        book='Proverbs',
        chapter=11,
        verse=14
    )

I'm getting this error at the line program = gui
dance(...): *guidance is not callable*.  Can you explain me what I'm missing? 
```
---

     
 
all -  [ How to create an index in langchain vector store redis ](https://www.reddit.com/r/LangChain/comments/17r9pce/how_to_create_an_index_in_langchain_vector_store/) , 2023-11-10-0909
```
Joined a new company, and trying to debug an existing application without any documentation. It's been a hell ride, so I
 appreciate any help I can get at this point.

    Redis.from_existing_index(embedding=OpenAIEmbeddings(), redis_url='re
dis://...', index_name=abcde)

leads to error:

    Redis failed to connect: Index abcde does not exist\n

How do I crea
te an index in langchain.vectorstores.redis? Thanks
```
---

     
 
all -  [ Adding system prompt message ](https://i.redd.it/tc1aqfdlmazb1.jpg) , 2023-11-10-0909
```
I want to add 

messages = [
    SystemMessage(content='explaij in bullet points''),
    HumanMessage(content=question)

]


How can I do it with that format?
```
---

     
 
all -  [ Is LangChain the right way to learn AI? ](https://www.reddit.com/r/ArtificialInteligence/comments/17r992x/is_langchain_the_right_way_to_learn_ai/) , 2023-11-10-0909
```
Hi everyone,

I've been learning code (JS / NextJS) for the last few months, and I honestly can say I have a pretty good
 understanding of the full-stack apps. **There is, however one big gap in my knowledge, and it's AI.**

  
**Is Langchai
n the right thing to learn?**  
I've already developed 2 full-stack apps that use OpenAI with LangChain on top of it, an
d now I want to dig deeper into the field - but I just don't know where to start. Problem is, I even though I managed to
 learn full-stack code from scratch really quickly, I find LangChain REALLY confusing.

Some of the abstractions used th
ere doesn't really make sense to me, especially it feels like it doesn't bring any value on top of vanilla OpenAI API.


  
**How to learn stuff outside of LLMs?**  
I talked to my friends recently that told me they have their own image gene
ration model, that's architecture agnostic and can work with Midjourney, StableDiffusion etc. but works on their GPUs.  
 
I have no idea what they're talking about. How can I start digging into the topic?  
I'd love to understand how startu
ps like [photoai.com](https://photoai.com) or [headshotpro.com](https://headshotpro.com) managed to build their models. 
How does it work? Where do I learn about it?  


**Do I need to know Pyton/Data Science?**  
Most of the courses and edu
cation materials starts with Python notebooks. Do I really have to learn Python? Aren't there any e.g. JS stuff there?


&#x200B;

Also, why people say that new big context of GPT-4-Turbo make Vector databases obsolete?  
Where can I learn o
n how to use Vector Databases with OpenAI? Why do I need them? How to fine tune models? 

So many questions, not a lot o
f answers.

**Use case: Let's say I want to create chain that e.g. 1) reads a newsletter and then 2) turns it into a pod
cast using ElevenLabs. Where do I start? How to approach this?**

&#x200B;

ps. I know it's all hectic, but my knowledge
 is almost non-existent. I don't know where to put my focus on.

Thanks!
```
---

     
 
all -  [ How to add IDs in Chroma using Langchain? ](https://www.reddit.com/r/LangChain/comments/17r908t/how_to_add_ids_in_chroma_using_langchain/) , 2023-11-10-0909
```
If I were to use the custom Chroma code to add IDs, this is how I'd do it.

collection.add(

documents=\['doc1', 'doc2',
 'doc3', ...\],

embeddings=\[\[1.1, 2.3, 3.2\], \[4.5, 6.9, 4.4\], \[1.1, 2.3, 3.2\], ...\],

metadatas=\[{'chapter': '
3', 'verse': '16'}, {'chapter': '3', 'verse': '5'}, {'chapter': '29', 'verse': '11'}, ...\],

ids=\['id1', 'id2', 'id3',
 ...\]

)

&#x200B;

How do I add these ids when I'm using LangChain?

loader = DataFrameLoader(df, page\_content\_colum
n='test')

documents = loader.load()

Here the page\_content\_column would be the vector column and the rest go into met
adatas, but what about ids?
```
---

     
 
all -  [ OpenAI's new Assistants API Rocks! ✨ ](https://www.reddit.com/r/beginAI/comments/17r75mr/openais_new_assistants_api_rocks/) , 2023-11-10-0909
```
Reduce complexity.  
Reduce cost.  
Reduce code.  
Increase liability.

https://preview.redd.it/ghmj06l0r9zb1.jpg?width=
1200&format=pjpg&auto=webp&s=e64a3bbb92415ec7033046e8d842bda447ee071e
```
---

     
 
all -  [ Build an LLM-powered application using LangChain ](https://www.leewayhertz.com/build-llm-powered-apps-with-langchain/) , 2023-11-10-0909
```

```
---

     
 
all -  [ YiVal: Build any generative AI application with evaluation and enhancement ](https://www.reddit.com/r/u_waynerad/comments/17r4x9x/yival_build_any_generative_ai_application_with/) , 2023-11-10-0909
```
'YiVal is a state-of-the-art tool designed to streamline the tuning process for your GenAI app prompts and ANY configs i
n the loop. With YiVal, manual adjustments are a thing of the past. This data-driven and evaluation-centric approach ens
ures optimal prompts, precise RAG configurations, and fine-tuned model parameters.'

'RAG' stands for 'retrieval augment
ed generation'. More on that below.

They go on to say: 'Problems YiVal is trying to tackle:'

'Prompt Development Chall
enge: 'I can't create a better prompt. A score of 60 for my current prompt isn't helpful at all.''

'Fine-tuning Difficu
lty: 'I don't know how to fine-tune; the terminology and numerous fine-tune algorithms are overwhelming.''

'Confidence 
and Scalability: 'I learned tutorials to build agents from Langchain and LlamaIndex, but am I doing it right? Will the b
ot burn through my money when I launch? Will users like my GenAI app?''

'Models and Data Drift: 'Models and data keep c
hanging; I worry a well-performing GenAI app now may fail later.''

'Relevant Metrics and Evaluators: 'Which metrics and
 evaluators should I focus on for my use case?''

Wow, that's quite a lot. I haven't had time to try this out -- in fact
 I just discovered it exists. If you have a chance to give it a whirl, let me know how it goes.

[https://github.com/YiV
al/YiVal/blob/master/README.md](https://github.com/YiVal/YiVal/blob/master/README.md)
```
---

     
 
all -  [ Langserve/FastAPI help ](https://www.reddit.com/r/LangChain/comments/17r27r9/langservefastapi_help/) , 2023-11-10-0909
```
I'm working with Langserve and using the rag-chroma template: [https://github.com/langchain-ai/langchain/tree/master/tem
plates/rag-chroma](https://github.com/langchain-ai/langchain/tree/master/templates/rag-chroma).

I have a sample project
 where I need to pass a parameter into the rag\_chroma\_chain to filter my retrieval by a metadata (The user can constra
in their query to just documents from a particular source). I'm unfamiliar with FastAPI so am unsure how edit the templa
te to be able to pass the necessary parameter so that I can adjust the retriever to only look at certain documents. Look
ing for some guidance on this and at the same time, learn some FastAPI
```
---

     
 
all -  [ AI Infrastructure needs more open-source engagement ](https://www.reddit.com/r/opensource/comments/17qzrfa/ai_infrastructure_needs_more_opensource_engagement/) , 2023-11-10-0909
```
The open-source community has always been at the forefront of innovation, but it feels like we are lagging when it comes
 to AI. 

  
AI is a generational shift for dev and tech and there's a serious risk of the big guys are running away wit
h the space and monopolizing it.   

  
I maintain CopilotKit, an open-source AI library, and while we're good interest,
 95% of it is coming from enterprise and people already in AI, and not the typical open-source community.    


What hap
pens in these early days will be pivotal to what the space looks like in years to come. Don't sleep on AI-infra! 

  
**
Some great OS AI libraries you can support & contribute to:**   
1. [CopilotKit](https://github.com/RecursivelyAI/Copilo
tKit) (My library):  Infra for embedding an AI Copilot into any app (react).   
2. [Pezzo.ai](https://github.com/pezzola
bs/pezzo): Prompt management & observability.   
3. [SwirlSearch](https://github.com/swirlai/swirl-search): LLM-powered 
search & synthesis.  
4. [LangChain](https://github.com/langchain-ai/langchain): build apps with LLMs. String together L
LM chains + other programs.   

```
---

     
 
all -  [ Full Document Understanding with RAG—Need Insights ](https://www.reddit.com/r/LangChain/comments/17qsmhs/full_document_understanding_with_ragneed_insights/) , 2023-11-10-0909
```
Hey everyone,

I'm working on a RAG project and hitting a snag. RAG only dissects text chunk by chunk, missing the 'big 
picture' of the entire document or diving deep into the text. Essentially, I'm looking to create a recursive RAG that gr
asps the full meaning and structure of the whole document, not just isolated snippets.

Any ideas on how to approach thi
s or resources you could point me toward?

Thanks!
```
---

     
 
all -  [ my Knowledge based chatbot is answering sometimes from the pdfs and other times from the gpt itself. ](https://www.reddit.com/r/LangChain/comments/17qs4le/my_knowledge_based_chatbot_is_answering_sometimes/) , 2023-11-10-0909
```
Hello everyone, I have a problem with my project. Actually i am working on chatbot knowledge base using langchain and pi
necone to answer questions only from the pdf imported . but it doesnt answer specifically from the document and sometime
s if something is not in the doc and i ask it it answers like it is chatgpt.  
```
---

     
 
all -  [ Chunking and storing structured data and vectors for RAG ](https://www.reddit.com/r/LocalLLaMA/comments/17qqokv/chunking_and_storing_structured_data_and_vectors/) , 2023-11-10-0909
```
TL:DR is there an example someone can point me to for RAG with highly structured documents where the agent returns conve
rsation along with cross references to document paragraphs or sections? Input= long text document (~500-1000 page), outp
ut is Q/A with references to document paragraph, page, or other simple cross reference.

I've been looking into RAG in m
y (extremely limited) spare time for a few months now but I'm getting hung up on vector databases. It may be due to the 
fact that my use case revolves around highly structured specification documents where I desire to be able to recover sec
tion and paragraph references in a QA session with a rag assistant. 

Most off-the-shelf solutions seem to not care what
 your data looks like and just provides a black box solution for data chunking and vectoring, like having a single HTML 
link for a website for the source information and magically it works. This confuses me because langchain has a great lea
rning path that includes quite a bit of focus on proper data chunking and vector database structuring, then literally ev
ery example treats the chunking and vector store step as an afterthought. I don't like to do something I don't understan
d so I've been focused more on creating a database for my data that makes sense in my brain. 

I have successfully creat
ed a local vector database (sqlite) with SBERT that returns paragraph numbers with a similarity search but I haven't bri
dged that to feeding those results into an LLM.

Am I thinking too hard about this? Are the off the shelf rag solutions 
able to handle the paragraph numbers without me explicitly trying to cram them into a database structure? Or am I on the
 right path, and I should continue with the database that makes sense to me and keep figuring out how to implement the L
LM step after the vector search?

I started looking at llamaindex, then Langchain, now autogen. But my spare time is lim
ited enough that I haven't implemented anything with any of these, only a (successful) sbert similarity search which did
n't use any of these. If someone has an example for structured documents where the q/a provides cross-references, I'd re
ally appreciate it.
```
---

     
 
all -  [ New Updates Made Vector Databases Redundant ](https://www.reddit.com/r/LangChain/comments/17qq7q6/new_updates_made_vector_databases_redundant/) , 2023-11-10-0909
```
The new retrieval function allows you to train the AI on your documents. 

Will this impact vector databases?
```
---

     
 
all -  [ Is there anyway to collect and process user feedback from AI chat locally? ](https://www.reddit.com/r/LangChain/comments/17qluy1/is_there_anyway_to_collect_and_process_user/) , 2023-11-10-0909
```
I have built a chatbot using  llama2, langchain and chainlit. I am trying to collect user feedback on the answers and an
alyze them. 

Is there is a way I can implement this feedback structure locally, without using hosted systems like langs
mith or trurbricks?

&#x200B;
```
---

     
 
all -  [ Ignore broken PDFs in DirectoryLoader ](https://i.redd.it/w0mpa9ia34zb1.jpg) , 2023-11-10-0909
```
I’m working on a large scale RAG pipeline (1000 pdf files). The program will interrupted because of the errors in PDFloa
der. I tried to load PDFs individually by a For loop using PyPDFLoader but the latency is too much. Is there any reliabl
e way to do this ?
```
---

     
 
all -  [ Hugging Face Hub LLMs keep timing out ](https://www.reddit.com/r/LangChain/comments/17qj9a0/hugging_face_hub_llms_keep_timing_out/) , 2023-11-10-0909
```
None of the 'Hugging Face Hub' LLMs works from LangChain. I get a timeout error after waiting for a very long time. I'm 
not the only one, as it has been reported [here](https://stackoverflow.com/questions/76265748/indefinite-wait-while-usin
g-langchain-and-huggingfacehub-in-python) and [here](https://github.com/langchain-ai/langchain/issues/3275), and a few m
onths since those reports, the problem persists. 

The only LLMs that work reliably without timing out are the ones from
 OpenAI. Considering that, I'm failing to see the point of LangChain instead of using the OpenAI Python library directly
. 

Has anyone else faced this problem, and did you figure out how to make other LLMs work?
```
---

     
 
all -  [ Trying new jina-embeddings-v2-base-en model ](https://www.reddit.com/r/LangChain/comments/17qj92b/trying_new_jinaembeddingsv2baseen_model/) , 2023-11-10-0909
```
was trying to use jina embeddings to create a vector database in chroma, but got errors. This is the detailed implementa
tion -  
\## loaded the jina model -

from langchain.embeddings import HuggingFaceEmbeddings

model\_name = 'jinaai/jina
-embeddings-v2-base-en'  
model\_kwargs = {'device': 'cuda'}  
encode\_kwargs = {'normalize\_embeddings': True}  
model 
= HuggingFaceEmbeddings(  
model\_name=model\_name,  
model\_kwargs=model\_kwargs,  
encode\_kwargs=encode\_kwargs  
)


chroma settings -

from chromadb.config import Settings

error in the above step -tings(  
anonymized\_telemetry=False, 
 
is\_persistent=True,  
)

Creating the persist directory -

persist\_directory = 'db'  
embedding = model

vectordb = 
Chroma.from\_documents(documents=texts,  
embedding=embedding,  
persist\_directory=persist\_directory,  
client\_settin
gs=CHROMA\_SETTINGS)

error in above step -

Expected EmbeddingFunction.call to have the following signature: odict\_key
s(\['self', 'input'\]), got odict\_keys(\['self', 'args', 'kwargs'\])

Can anyone help to solve it?
```
---

     
 
all -  [ How to turn a promising software library into a business model? ](https://www.reddit.com/r/startups/comments/17qixxq/how_to_turn_a_promising_software_library_into_a/) , 2023-11-10-0909
```
Hi all, I have had an interesting idea that potentially could change the way we interact with LLMs. I am currently writi
ng a prototype. While I believe the idea has a similar potential like Langchain or Haystack, what I am missing is an ide
a how to monetize it. Sure, I can create a library and open source it. But then what? I may gain some kudos, but that's 
not a business model, it's just a library. Selling the library for money will not work. I could try to get a patent arou
nd it, but I think that's quite useless and also takes way too long. I expect that in few months someone will come up wi
th a similar idea like mine independently.  
Does anyone have any blueprints how to turn a software library (comparable 
to Langchain) into a business model?
```
---

     
 
all -  [ Vertexaisearch retrieval with retrieval qa with sources chain ](https://www.reddit.com/r/LangChain/comments/17qidql/vertexaisearch_retrieval_with_retrieval_qa_with/) , 2023-11-10-0909
```
I've uploaded a CSV file into vector ai portal in search and conversation app. Then I'm using retriever to initiall quer
y the list of documents and using qachain with prompt template.

But, I'm getting an error which says 
' Valueerror: doc
ument prompt requires documents to have metadata variables  : [source] Received doc with missing metadata: [source] '

H
ow to add source as metadata to the CSV and what values to populate this with ?
```
---

     
 
all -  [ Image generation with langchain ](https://www.reddit.com/r/LangChain/comments/17qhrhs/image_generation_with_langchain/) , 2023-11-10-0909
```
Hi,

I'm trying to make kids stories generator with text and image on langchain. No issue with text, it's pretty straigh
t forward. But things gets harder when I want to generate no dommesques images. The only way I find is the dall-e image 
generator but it's really messy. I wasn't able to understand how this works even when looking in the code: https://githu
b.com/langchain-ai/langchain/blob/master/libs/langchain/langchain/utilities/dalle_image_generator.py

It doesn't seem to
 use a dedicated endpoint and it's not clear how to select the model...

What would be the alternative to generates imag
es with langchain ?
```
---

     
 
all -  [ very confused with langchain ](https://www.reddit.com/r/LangChain/comments/17qd4ok/very_confused_with_langchain/) , 2023-11-10-0909
```
Is it just me, or langchain is very confusing?

First I get totally confused between typescript and python documentation
. Which is kind of stupid, but there are no distinction visually between two set of documentation.  I google something, 
and it gives me a link, and it is not immediately obvious that it is the other language, until you reach the code. And t
he implementation is not quite parallel. It seems there are differences between two implementations.

&#x200B;

Then the
re are competing concepts like chains vs agents. Which I have read the difference, but still very close in practice.

&#
x200B;

Or I thought  `prompt | llm` is the same as `LLMChain(llm=llm, prompt=prompt)` but apparently not.

&#x200B;

Ho
w do you really learn this thing for good?
```
---

     
 
all -  [ Collection and pg_vector in Supabase ](https://www.reddit.com/r/Supabase/comments/17qcnim/collection_and_pg_vector_in_supabase/) , 2023-11-10-0909
```
Hi all --

Are collections a part of pgvector in supabase at all? I know you reference one when using the Pgvector vecto
r vector store in langchain, and I assume a collection is the same as an index in pinecone. So I'm curious of an analogo
us solution with Supabase. 

Please correct me on any of this!
```
---

     
 
all -  [ New OpenAI Canva action via API ](https://www.reddit.com/r/LangChain/comments/17q9grw/new_openai_canva_action_via_api/) , 2023-11-10-0909
```
Is it possible to access the new Canva AI actions via the OpenAI API? If not, do you think that OpenAI will add this fea
ture in the future?
```
---

     
 
all -  [ Reorganizing or categorize inputs by tool type ](https://www.reddit.com/r/LangChain/comments/17q2fww/reorganizing_or_categorize_inputs_by_tool_type/) , 2023-11-10-0909
```
Hello to all the diligent craftsmen and craftswomen!

We've encountered a hiccup in our process. Currently, we're using 
a conversational agent to interface with external APIs for various tasks. Let's say we have four such tools at our dispo
sal. Consider a scenario where a user requests, 'Use tool #1 for an action, recite a poem for me, perform an action with
 tool #2, follow it up with a haiku, and then repeat an action with tool #1.'

Our challenge arises with the sequence of
 these prompts. We instruct the system to first activate tool #1, then generate a haiku, followed by using tool #2, and 
finally, to carry out an action with tool #1 once more. However, post-haiku, the system seems reluctant to re-engage too
l #1. Conversely, if we streamline the prompt to execute all actions of tool #1, proceed to tool #2, and cap it off with
 the haiku, everything functions seamlessly. It appears that the system favors prompts organized by tool-specific action
s rather than a heterogeneous or ungrouped sequence.

We're attempting to coax the language model through our template t
o categorize inputs by tool type before proceeding, yet luck hasn't been on our side.

Would anyone have a strategy or a
dvice to untangle this? Your insights would be greatly appreciated. Thank you!
```
---

     
 
all -  [ SelfQueryRetriever w/ date metadata ](https://www.reddit.com/r/LangChain/comments/17q054j/selfqueryretriever_w_date_metadata/) , 2023-11-10-0909
```
Has anyone successfully used dates as metadata while using the SelfQueryRetriever? 

I'm guessing it's not supported as 
I get the following error: 

>Expected where operand value to be a str, int, float, or list of those type, got 2021-05-1
1. 

I've seen references to using the datetime.date type but I also tried just using a string as the type, but I got th
e same error either way. My metadata AttributeInfo looks like this: 

    AttributeInfo(
            name='isodate',
   
         description='The date the document was created',
            type='datetime.date',
    )

 This is how the unde
rlying StructuredQuery is being constructed which looks exactly like what I want: 

    StructuredQuery(query='SomeInfo'
, filter=Comparison(comparator=<Comparator.EQ: 'eq'>, attribute='isodate', value=datetime.date(2021, 5, 11)), limit=None
)

Maybe there's another way to achieve this without the SelfQueryRetriever? 

Hopefully someone can point me in the rig
ht direction. Thanks!
```
---

     
 
all -  [ Where to find documentation for langchain implementation of QDRANT Operations? ](https://www.reddit.com/r/LangChain/comments/17q04t0/where_to_find_documentation_for_langchain/) , 2023-11-10-0909
```
I'm trying to implement CRUD operations such as Uploading Points, Updating Points, Retrieving Points  etc which are avai
lable in QDRANT documentation. Is there an equivalent of these in langchain. All I see is the integration part here: [ht
tps://qdrant.tech/documentation/integrations/langchain/](https://qdrant.tech/documentation/integrations/langchain/)

&#x
200B;
```
---

     
 
MachineLearning -  [ [D] Is this close enough to be usable? Need your inputs: Automated RAG testing tool. AI Data Pipelin ](https://www.reddit.com/r/MachineLearning/comments/17kkbm0/d_is_this_close_enough_to_be_usable_need_your/) , 2023-11-10-0909
```
Hey there, Redditors! 

I'm back with the latest installment on creating dependable AI data pipelines for real-world pro
duction. 

If you've been following along, you know I'm on a mission to move beyond the '[thin OpenAI wrapper](https://t
opoteretes.notion.site/Going-beyond-Langchain-Weaviate-and-towards-a-production-ready-modern-data-platform-7351d77a1eba4
0aab4394c24bef3a278?pvs=4)' trend and tackle the challenges of building robust data pipelines. 

With 18 months of hands
-on experience and many user interviews, I realized that with the probabilistic nature of systems, we need better\_testi
ng.gpt:

  
**1. As you build you should test**  
The world of AI is a fast-moving one, and we've realized that just wor
king on systems is not an optimal design choice. By the time your product ships, it might already be using outdated tech
nology. So, what's the lesson here? Embrace change, test along, but be prepared to switch pace.  
**2. No Best Practices
 Yet for RAGs**  
In this rapidly evolving landscape, there are no established best practices. You'll need to make educa
ted bets on tools and processes, knowing that things will change. With the RAG testing tool, I tried allowing for testin
g many potential parameter combinations **automatically**  
**3. Testing Frameworks**  
If your generative AI product do
esn't have users giving feedback, then you are building in isolation. I used [Deepeval](https://github.com/confident-ai/
deepeval) to generate test sets, and they will soon support synthetic test set generation  
**4. Infographics only go so
 far**  
AI researchers and data scientists, while brilliant, end up in a loop of pursuing Twitter promotional content. 
New ways are promoted via new content pieces, but ideally, we need something above simple tracing but less than full-fle
dged analytics. To do this, I stored test outputs in Postgres and created a Superset instance to visualize the results  

**5. Bridging the Gap between VectorDBs**  
There's a noticeable number of Vector DBs. To ensure smooth product develop
ment, we need to be able to switch to best best-performing one, especially since user interviews signal that they might 
start deteriorating after loading 50 million rows

&#x200B;

Github repo is [here](https://topoteretes.notion.site/Going
-beyond-Langchain-Weaviate-Level-3-towards-production-e62946c272bf412584b12fbbf92d35b0?pvs=4)  


Next steps:  
I have q
uestions for you: 

1. What variables do you change when building RAGs?
2. What is the set of strategies I should add to
 the solution? (parent-son etc.)
3. How can I improve it in general? 
4. Is anyone  interested in a leaderboard for best
 parameter configs?

Check out the blog post:

[Link to part 3](https://topoteretes.notion.site/Going-beyond-Langchain-W
eaviate-Level-3-towards-production-e62946c272bf412584b12fbbf92d35b0?pvs=4)

  
*Remember to give this post an upvote if 
you found it insightful!*  
*And also star our* [*Github repo*](https://github.com/topoteretes/PromethAI-Memory)
```
---

     
 
MachineLearning -  [ [D] Relevance Extraction in RAG Pipelines ](https://www.reddit.com/r/MachineLearning/comments/17k6iha/d_relevance_extraction_in_rag_pipelines/) , 2023-11-10-0909
```
I came across this interesting problem in RAG, what I call **Relevance Extraction**.

After retrieving relevant document
s (or chunks), these chunks are often large and may contain several portions **irrelevant** to the query at hand. Stuffi
ng the entire chunk into an LLM prompt impacts token-cost as well as response accuracy (distracting the LLM with irrelev
ant text), and and can also cause bumping into context-length limits.

So a critical step in most pipelines is **Relevan
ce Extraction**: use the LLM to extract **verbatim** only the portions relevant to the query. This is known by other nam
es, e.g. LangChain calls it Contextual Compression, and the RECOMP paper calls it Extractive Compression [https://twitte
r.com/manelferreira\_/status/1713214439715938528](https://twitter.com/manelferreira_/status/1713214439715938528)

Thinki
ng about how best to do this, I realized it is **highly inefficient** to simply ask the LLM to 'parrot' out relevant por
tions of the text: this is obviously slow, and also consumes valuable token generation space and can cause you to bump i
nto context-length limits (and of course is expensive, e.g. for gpt4 we know generation is 6c/1k tokens vs input cost of
 3c/1k tokens).

I realized the best way (or at least a good way) to do this is to **number** the sentences and have the
 LLM simply spit out the relevant sentence **numbers.** Langroid's unique Multi-Agent + function-calling architecture al
lows an elegant implementation of this, in the RelevanceExtractorAgent ([https://github.com/langroid/langroid/blob/main/
langroid/agent/special/relevance\_extractor\_agent.py](https://github.com/langroid/langroid/blob/main/langroid/agent/spe
cial/relevance_extractor_agent.py)).  The agent annotates the docs with sentence numbers, and instructs the LLM to pick 
out the **sentence-numbers** relevant to the query, rather than whole sentences using a function-call (SegmentExtractToo
l [https://github.com/langroid/langroid/blob/main/langroid/agent/tools/segment\_extract\_tool.py](https://github.com/lan
groid/langroid/blob/main/langroid/agent/tools/segment_extract_tool.py)), and the agent's function-handler interprets thi
s message and strips out the indicated sentences by their numbers. To extract from a set of passages, langroid automatic
ally does this async + concurrently so latencies in practice are much, much lower than the sentence-parroting approach.


\[FD -- I am the lead dev of Langroid - [https://github.com/langroid/langroid](https://github.com/langroid/langroid))


I thought this **numbering** idea is a fairly obvious idea in theory, so I looked at LangChain's equivalent `LLMChainExt
ractor` (they call this Contextual Compression [https://python.langchain.com/docs/modules/data\_connection/retrievers/co
ntextual\_compression?ref=blog.langchain.dev](https://python.langchain.com/docs/modules/data_connection/retrievers/conte
xtual_compression?ref=blog.langchain.dev)) and was surprised to see it is the simple '**parrot**' method, i.e. the LLM w
rites out whole sentences verbatim from its input. I thought it would be interesting to compare Langroid vs LangChain, y
ou can see it in this Colab: [https://colab.research.google.com/drive/1RDPCR2xNuBffcmpUuPIXYDRG3SXIJC5F](https://colab.r
esearch.google.com/drive/1RDPCR2xNuBffcmpUuPIXYDRG3SXIJC5F)

On the specific example in the notebook, the Langroid **num
bering** approach is 22x faster and 36% cheaper (with gpt4) than LangChain's **parrot** method (I promise this name is *
not* inspired by their logo :). See table below.

&#x200B;

[Relevance Extraction: Langroid vs LangChain](https://previe
w.redd.it/1m7u6ulq8fxb1.png?width=1108&format=png&auto=webp&s=d2f35cf5db07e2e699baa54b274ffa60833e924a)

&#x200B;

I won
der if anyone had thoughts on relevance extraction, or other approaches. At the very least, I hope langroid's implementa
tion is useful to you -- you can use the `DocChatAgent.get_verbatim_extracts()` ([https://github.com/langroid/langroid/b
lob/main/langroid/agent/special/doc\_chat\_agent.py#L804](https://github.com/langroid/langroid/blob/main/langroid/agent/
special/doc_chat_agent.py#L804)) as part of your pipeline, regardless of whether you are using Langroid for your entire 
system or not.

&#x200B;
```
---

     
 
MachineLearning -  [ [R] Model Troubles ](https://www.reddit.com/r/MachineLearning/comments/17ikh2u/r_model_troubles/) , 2023-11-10-0909
```
So i’m working on a model that diagnoses alzheimer’s disease and suggests medication depending on how severe the symptom
s might have become 
I’m using the Openai API and Langchain.

But it’s dumb and it doesn’t learn (
Me: I forgot my keys 
at home
Model: Yup, Alzheimer’s)
How do i incorporate the actual machine learning

Edit: I didn’t choose this project my
 supervisor did and she barely knows anything about the topic or how to approach it
```
---

     
 
MachineLearning -  [ [P] NexaAgent: A highly efficient multi-task PDF tool for all your needs | backed by AutoGen ](https://www.reddit.com/r/MachineLearning/comments/17eajz2/p_nexaagent_a_highly_efficient_multitask_pdf_tool/) , 2023-11-10-0909
```
Just a quick open-source project recently submitted to huggingface backed by AutoGen. Share this initial version with yo
u guys!

[NexaAgent 0.0.1](https://huggingface.co/spaces/xuyingliKepler/nexaagent) offers a straightforward solution for
 handling PDFs.

* Users can easily upload any PDF, regardless of its size.
* The tool emphasizes accuracy, minimizing d
iscrepancies in PDF processing.

At its core, NexaAgent is backed by the AutoGen and LangChain frameworks. AutoGen facil
itates multi-agent interactions for task execution, while LangChain bridges LLMs with external data sources. Together, t
hese technologies ensure NexaAgent's robust and precise PDF management capabilities.

https://preview.redd.it/kwgo3phnav
vb1.jpg?width=1440&format=pjpg&auto=webp&s=1c5fbc566938d60d5c43802aff3a0690821e1c79
```
---

     
 
MachineLearning -  [ [D] Is lang chain the right solution? ](https://www.reddit.com/r/MachineLearning/comments/17coyym/d_is_lang_chain_the_right_solution/) , 2023-11-10-0909
```
Hello, I would love to have an LLm that can provide answers (in chat format) based some of the sql db  data we have. Wan
t it for an internal company project. I am by no means an expert but decent in programming and want to build a system to
 get answers in chat format. My understanding is that training LLMs ground up is prohibitively expensive and langchains 
are sort of hybrid , efficient solutions. 

Please suggest any other solutions. Also would Langchain being a company and
 not open source pose a problem in terms of copyrights? Thanks!
```
---

     
 
MachineLearning -  [ [P] building a D&D NPC ](https://www.reddit.com/r/MachineLearning/comments/17clyw6/p_building_a_dd_npc/) , 2023-11-10-0909
```
Hey everyone,

I'm learning ML but i'm barely scratching the terminologies. 2 years ago I couldn't code anything but wit
h school (python,sql and R) I learned fundamentals. I also have access to code academy.  My current program is very mach
ine learning/deep learning focused.

On the side I DM a d&d game. Within the context of the world (eberron) robots are c
ommon. With my ADHD and being a new DM I want to outsource lore questions might have (that I would have to look up and s
low down the game).

The concept is to have a GUI and have the player interact with the chat bot. I've gotten to a proof
 of concept workflow. On Google colab. Thanks to langchain I managed to ingest pdfs and a url. Make then a directory, Em
bedded the text, bring it into a vector dB. Have the llm pull from the vector. Answer the question.

Now I don't know wh
at to do. I tried to bring the colab notebook onto Google cloud. But now cloud is becoming a rabbit home with vertex and
 docAI...and I don't want to deep dive into that, if it's a outside the scope of this 'project'

I'd appreciate any advi
ce, links...etc. 


I got a limited success in botpress using a single pdf. It works but feel unsatisfying.
N8N looks pr
omising but if it's not intuitive then I don't want to go down that road.


If I posted in the wrong group please direct
 me to the correct one.
```
---

     
 
MachineLearning -  [ [D] Exploring Methods to Improve Text Chunking in RAG Models (and other things...) ](https://www.reddit.com/r/MachineLearning/comments/179j7l3/d_exploring_methods_to_improve_text_chunking_in/) , 2023-11-10-0909
```
Hello everyone,

I'm currently working on Retrieval Augmented Generation (RAG) models and have developed a custom chunki
ng function, as I found the methods in LangChain not entirely satisfactory.

I'm keen on exploring other methods, algori
thms (related to NLP or otherwise), and models to enhance text chunking in RAG. There are many RAG implementations out t
here, but I've noticed a lack of focus on improving chunking performance specifically.

Are there any other promising ap
proaches beyond my current pipeline, which consists of a bi-encoder (retriever), cross-encoder (reranker), and a Large L
anguage Model (LLM) for interactions?

For queries, I'm using both traditional and HyDE (Hypothetical Document Embedding
) approaches in the retrieval phase, and sending the top 'n' results of both similarity search to the reranker.

I've al
so tried using an LLM to convert the query into a series of 10-20 small phrases or keywords, which are then used as the 
query for the retriever model. However, the results vary depending on the LLM used. To generate good keywords (with a no
t extractive approach) , I had to  use a 'CoT' prompt, instructing the model to  write self-instruct, problem analysis a
nd reasonings before generating the required keywords. But this approach use lots of tokens, and requires careful scrapi
ng to ensure the model has used the right delimiter to separate reasoning and the actual answer.

I'm also planning to m
odify the text used to generate embeddings, while returning the original text after the recall phase. But this is still 
a work in progress and scaling it is proving to be a challenge. If anyone has any tips or experience with this, I'd appr
eciate your input.

I'd be grateful for any resources, repositories, libraries, or existing implementations of novel chu
nking methods that you could share. Or we could just discuss ideas, thoughts, or approaches to improve text chunking for
 RAG here.

Thanks in advance for your time!
```
---

     
 
MachineLearning -  [ [News] AI & ML conference in San Francisco [Special discount code for this subreddit] ](https://www.reddit.com/r/MachineLearning/comments/1771m35/news_ai_ml_conference_in_san_francisco_special/) , 2023-11-10-0909
```
I work for this database company SingleStore and we are hosting a AI & ML conference in San Francisco on 17th of October
, 2023.

It is an in-person conference with amazing speakers line-up like Harrison Chase, co-founder and CEO of LangChai
n and many more. We will have hands-on workshops, swags giveaway and much more.

I don't know if it makes sense to share
 this but I believe it might help some of you near San Francisco to go and meet the industry leaders and network with ot
her data engineering folks.

Use my discount coupon code 'PAVAN100OFF' to avail 100% off on the ticket price. (the origi
nal ticket price is $199)

[Get your tickets now!](https://singlestore.com/now)
```
---

     
 
MachineLearning -  [ [D] Best way to validate llm prompts? ](https://www.reddit.com/r/MachineLearning/comments/176vnxh/d_best_way_to_validate_llm_prompts/) , 2023-11-10-0909
```
We have a platform for data analytics which uses a very simple dsl to generate charts.  
We have been experimenting with
 llms to use natural language that gets translated into this dsl and hence generates charts.

This is working pretty goo
d.  
The stack is langchain with openai api. (don't have much experience with llms, it's a prototype to get a feel for i
t)

The question is what is the best way to limit the options user can type in as a prompt.  
Basically the the only all
owed things should be: 'What is the X, Y over 10 days period for this or that?'  
I don't want users to ask questions li
ke when did we first land on the moon.

Is it something that is possible to do at all without additional tooling?  
We p
robably don't want to train another model to classify the prompt as valid or invalid or something similar.
```
---

     
 
deeplearning -  [ Error with Mistral 7B model in ConversationalRetrievalChain ](https://www.reddit.com/r/deeplearning/comments/179vvou/error_with_mistral_7b_model_in/) , 2023-11-10-0909
```
 I'm encountering an issue while using the Mistral 7B model in a ConversationalRetrievalChain. When I input a question, 
such as 'What is the highest GDP?', I receive an error and after that the model generates a random response as output wh
ich is not relevant to the Input query. It seems that the number of tokens in the input exceeds the maximum context leng
th. 

Here's the relevant code: 

 

>`from langchain.document_loaders.csv_loader import CSVLoader`  
`from langchain.te
xt_splitter import RecursiveCharacterTextSplitter`  
`from langchain.embeddings import HuggingFaceEmbeddings`  
`from la
ngchain.vectorstores import FAISS`  
`from langchain.llms import CTransformers`  
`from langchain.memory import Conversa
tionBufferMemory`  
`from langchain.chains import ConversationalRetrievalChain`  
`import sys`  
`DB_FAISS_PATH = 'vecto
rstore/db_faiss'`  
`loader = CSVLoader(file_path='data/World Happiness Report 2022.csv', encoding='utf-8', csv_args={'d
elimiter': ','})`  
`data = loader.load()`  
`print(data)`  
`# Split the text into Chunks`  
`text_splitter = Recursive
CharacterTextSplitter(chunk_size=500, chunk_overlap=20)`  
`text_chunks = text_splitter.split_documents(data)`  
`print(
len(text_chunks))`  
`# Download Sentence Transformers Embedding From Hugging Face`  
`embeddings = HuggingFaceEmbedding
s(model_name = 'sentence-transformers/all-MiniLM-L6-v2')`  
`# COnverting the text Chunks into embeddings and saving the
 embeddings into FAISS Knowledge Base`  
`docsearch = FAISS.from_documents(text_chunks, embeddings)`  
`docsearch.save_l
ocal(DB_FAISS_PATH)`  
  
>  
>`#query = 'What is the value of GDP per capita of Finland provided in the data?'`  
`#doc
s = docsearch.similarity_search(query, k=3)`  
`#print('Result', docs)`  
`llm = CTransformers(model='models/mistral-7b-
v0.1.Q4_0.gguf',`  
 `model_type='llama',`  
 `max_new_tokens=1000,`  
 `temperature=0.1)`  
`qa = ConversationalRetriev
alChain.from_llm(llm, retriever=docsearch.as_retriever())`  
`while True:`  
 `chat_history = []`  
 `#query = 'What is 
the value of  GDP per capita of Finland provided in the data?'`  
 `query = input(f'Input Prompt: ')`  
 `if query == 'e
xit':`  
 `print('Exiting')`  
 `sys.exit()`  
 `if query == '':`  
 `continue`  
 `result = qa({'question':query, 'chat
_history':chat_history})`  
 `print('Response: ', result['answer'])`

 

**Problem Statement:**

I'm trying to utilize t
he Mistral 7B model for a ConversationalRetrievalChain, but I'm encountering an error related to token length:

Number o
f tokens (760) exceeded maximum context length (512).

**Context:**

I'm working on a project that involves using Mistra
l 7B to answer questions based on a dataset. The dataset contains information about the World Happiness Report 2022.

**
Steps Taken:**

* Loaded and preprocessed the dataset using langchain.
* Initialized Mistral 7B with the following param
eters:
* Model: 'models/mistral-7b-v0.1.Q4\_0.gguf'
* Model Type: 'llama'
* Max New Tokens: 1000
* Temperature: 0.1
* Se
t up a ConversationalRetrievalChain with Mistral 7B as the language model and a retriever based on FAISS.

**Expected Ou
tput:**

I expect to receive a meaningful response from Mistral 7B based on the input query.

**Additional Information:*
*

I'm using Python and relevant libraries for this project. The dataset I'm working with is from the World Happiness Re
port 2022.

**Environment Details:**

* Python version: 3.11.4 
* Relevant libraries and versions: 

langchain 

ctransf
ormers 

sentence-transformers 

faiss-cpu
```
---

     
 
deeplearning -  [ Error with Mistral 7B model in ConversationalRetrievalChain. ](https://www.reddit.com/r/deeplearning/comments/179vsif/error_with_mistral_7b_model_in/) , 2023-11-10-0909
```
I'm encountering an issue while using the Mistral 7B model in a ConversationalRetrievalChain. When I input a question, s
uch as 'What is the highest GDP?', I receive an error and after that the model generates a random response as output whi
ch is not relevant to the Input query. It seems that the number of tokens in the input exceeds the maximum context lengt
h.

Here's the relevant code:

>from langchain.document\_loaders.csv\_loader import CSVLoader  
>  
>from langchain.text
\_splitter import RecursiveCharacterTextSplitter  
>  
>from langchain.embeddings import HuggingFaceEmbeddings  
>  
>fr
om langchain.vectorstores import FAISS  
>  
>from langchain.llms import CTransformers  
>  
>from langchain.memory impo
rt ConversationBufferMemory  
>  
>from langchain.chains import ConversationalRetrievalChain  
>  
>import sys  
>  
>  

>  
>DB\_FAISS\_PATH = 'vectorstore/db\_faiss'  
>  
>loader = CSVLoader(file\_path='data/World Happiness Report 2022.c
sv', encoding='utf-8', csv\_args={'delimiter': ','})  
>  
>data = loader.load()  
>  
>print(data)  
>  
>  
>  
>\# Sp
lit the text into Chunks  
>  
>text\_splitter = RecursiveCharacterTextSplitter(chunk\_size=500, chunk\_overlap=20)  
> 
 
>text\_chunks = text\_splitter.split\_documents(data)  
>  
>  
>  
>print(len(text\_chunks))  
>  
>  
>  
>\# Downlo
ad Sentence Transformers Embedding From Hugging Face  
>  
>embeddings = HuggingFaceEmbeddings(model\_name = 'sentence-t
ransformers/all-MiniLM-L6-v2')  
>  
>  
>  
>\# COnverting the text Chunks into embeddings and saving the embeddings in
to FAISS Knowledge Base  
>  
>docsearch = FAISS.from\_documents(text\_chunks, embeddings)  
>  
>  
>  
>docsearch.save
\_local(DB\_FAISS\_PATH)  
>  
>  
>  
>  
>  
>\#query = 'What is the value of GDP per capita of Finland provided in th
e data?'  
>  
>  
>  
>\#docs = docsearch.similarity\_search(query, k=3)  
>  
>  
>  
>\#print('Result', docs)  
>  
>
  
>  
>llm = CTransformers(model='models/mistral-7b-v0.1.Q4\_0.gguf',  
>  
>model\_type='llama',  
>  
>max\_new\_toke
ns=1000,  
>  
>temperature=0.1)  
>  
>  
>  
>qa = ConversationalRetrievalChain.from\_llm(llm, retriever=docsearch.as\
_retriever())  
>  
>  
>  
>while True:  
>  
>chat\_history = \[\]  
>  
>\#query = 'What is the value of  GDP per cap
ita of Finland provided in the data?'  
>  
>query = input(f'Input Prompt: ')  
>  
>if query == 'exit':  
>  
>print('E
xiting')  
>  
>sys.exit()  
>  
>if query == '':  
>  
>continue  
>  
>result = qa({'question':query, 'chat\_history':
chat\_history})  
>  
>print('Response: ', result\['answer'\])

 

**Problem Statement:**

I'm trying to utilize the Mis
tral 7B model for a ConversationalRetrievalChain, but I'm encountering an error related to token length:

Number of toke
ns (760) exceeded maximum context length (512).

**Context:**

I'm working on a project that involves using Mistral 7B t
o answer questions based on a dataset. The dataset contains information about the World Happiness Report 2022.

**Steps 
Taken:**

* Loaded and preprocessed the dataset using langchain.
* Initialized Mistral 7B with the following parameters:

* Model: 'models/mistral-7b-v0.1.Q4\_0.gguf'
* Model Type: 'llama'
* Max New Tokens: 1000
* Temperature: 0.1
* Set up a
 ConversationalRetrievalChain with Mistral 7B as the language model and a retriever based on FAISS.

**Expected Output:*
*

I expect to receive a meaningful response from Mistral 7B based on the input query.

**Additional Information:**

I'm
 using Python and relevant libraries for this project. The dataset I'm working with is from the World Happiness Report 2
022.

**Environment Details:**

Python version: 3.11.4 Relevant libraries and versions: langchain ctransformers sentence
-transformers faiss-cpu

&#x200B;
```
---

     
 
deeplearning -  [ Free courses to learn about Large Language Models and building AI projects ](https://www.reddit.com/r/deeplearning/comments/178zu2u/free_courses_to_learn_about_large_language_models/) , 2023-11-10-0909
```
[**LangChain for LLM Application Development by Andrew Ng**](https://www.deeplearning.ai/short-courses/langchain-for-llm
-application-development/): Apply LLMs to your proprietary data to build personal assistants and specialized chatbots. 


[**Full Stack LLM Bootcamp**](https://fullstackdeeplearning.com/llm-bootcamp/): Learn best practices and tools for buil
ding LLM-powered apps 

[**Stanford CS324**](https://stanford-cs324.github.io/winter2022/): In this course, students wil
l learn the fundamentals about the modeling, theory, ethics, and systems aspects of large language models, as well as ga
in hands-on experience working with them. 

[**LangChain & Vector Databases in Production**](https://learn.activeloop.ai
/courses/langchain): Learn how to leverage LangChain, a robust framework for building applications with LLMs, and explor
e Deep Lake, a groundbreaking vector database for all AI data. 

[**Stanford CS25**](https://web.stanford.edu/class/cs25
/): In this course, learn how transformers work, and dive deep into the different kinds of transformers and how they're 
applied in different fields. 

[**LLMOps Space Discord**](https://llmops.space/discord): LLMOps Space is a global commun
ity for LLM practitioners.
```
---

     
