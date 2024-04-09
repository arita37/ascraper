 
all -  [ Can I run LLama2-7b locally on NVIDIA 2060 6gb laptop GPU? ](https://www.reddit.com/r/LocalLLaMA/comments/1bz9w4a/can_i_run_llama27b_locally_on_nvidia_2060_6gb/) , 2024-04-09-0910
```
I am planning on making an RAG application project using an open source LLM to summarize fiction novel text. I will not 
be performing any finetuning on the LLM I use, I just want to run it locally to send prompts and get responses using lan
gchain. I was wondering if my laptop specifications are enough for this project. I have a HP Omen laptop (16GB RAM, NVID
IA 3060 6GB GPU) with an Intel i9 12900H (14 core) processor.

Kindly also leave suggestions of other models I can use t
o make this project. Thanks in advance!
```
---

     
 
all -  [ Creating agents with 'Scripted conversations' ](https://www.reddit.com/r/LangChain/comments/1bz80zh/creating_agents_with_scripted_conversations/) , 2024-04-09-0910
```
Hello, after working on a classic RAG chatbot to answer questions about IT support, we want to improve it so that, inste
ad of showing a list of steps retrieved from the KB, it can interact with the user asking questions. For example:  
U: X
 does not work.  
A: please try A, did it work?  
U: No  
A: ok, if A did not work, please try B.  
U:  it worked.  
A: 
happy to be of help.  
etc. etc.  
Of course the conversation can become longer with multiple steps, etc.  
I can imagin
e mixing a classic chatbot with a scripted flow with an LLM to get better understanding of utterances, a bit like the ex
perimental mode of Rasa does, but I'm asking myself if there is a better and more modern way to handle such data collect
ion/scripted conversations. At the end it's a kind of data gathering mixed with a decision tree and wondering what's the
 more modern approach to such a problem.  
What do you guys think?
```
---

     
 
all -  [ Recommendations for vectorDBs (local & serializable) ](https://www.reddit.com/r/vectordatabase/comments/1bz7zu9/recommendations_for_vectordbs_local_serializable/) , 2024-04-09-0910
```
I am looking for recommendations for vectorDBs that can operate in a browser. I'd like to be able to pre-compute embeddi
ngs for a large number of documents, load to the vectorDB, save it, and subsequently reload the vectorDB without having 
to re-compute the embeddings.

I have tried voy-search already, but there's a bug with their serialize and deserialize f
unctionality. I am also trying MemoryVectorStore with Langchain but there's no easy way I can see to export the vectorDB
 for later use.

Any help is greatly appreciated!
```
---

     
 
all -  [ Anthropic's Haiku Beats GPT-4 Turbo in Tool Use ](https://docs.parea.ai/blog/benchmarking-anthropic-beta-tool-use) , 2024-04-09-0910
```

```
---

     
 
all -  [ Wrote a semantic chunker for RAG pipelines in Typescript ](https://www.reddit.com/r/LLMDevs/comments/1bz3p2n/wrote_a_semantic_chunker_for_rag_pipelines_in/) , 2024-04-09-0910
```
Langchain python had this for some time now, but the typescript implementation lacked this chunking mechanism. So, follo
wed [this](https://github.com/FullStackRetrieval-com/RetrievalTutorials/blob/main/tutorials/LevelsOfTextSplitting/5_Leve
ls_Of_Text_Splitting.ipynb) notebook by Greg Kamadt and implemented it myself.  


Feel free to use the code :) Everythi
ng is documented in jsDoc  


[https://github.com/tsensei/Semantic-Chunking-Typescript](https://github.com/tsensei/Seman
tic-Chunking-Typescript)
```
---

     
 
all -  [ Wrote a semantic chunker for RAG pipelines in Typescript ](https://www.reddit.com/r/LangChain/comments/1bz3ngb/wrote_a_semantic_chunker_for_rag_pipelines_in/) , 2024-04-09-0910
```
Langchain python had this for some time now, but the typescript implementation lacked this chunking mechanism. So, follo
wed [this](https://github.com/FullStackRetrieval-com/RetrievalTutorials/blob/main/tutorials/LevelsOfTextSplitting/5_Leve
ls_Of_Text_Splitting.ipynb) notebook by Greg Kamadt and implemented it myself.  


You're free to use the code :) Everyt
hing is documented in jsDoc  


[https://github.com/tsensei/Semantic-Chunking-Typescript](https://github.com/tsensei/Sem
antic-Chunking-Typescript)
```
---

     
 
all -  [ Need help building better RAG chatbot using azure  ](https://www.reddit.com/r/AZURE/comments/1bz35jp/need_help_building_better_rag_chatbot_using_azure/) , 2024-04-09-0910
```
I'm building RAG chat bot with azure open ai and azure ai search

using streamlit as frontend and maintain chat history 
using session state (not focusing on persistent state rgt now)

Data ingestion pipeline is big headache for me(working w
ith static data)
Working with formats PDF , PPT , docx , excel(mostly technical documentation and excel is logs of ticke
t)

Each pdf have different structure,Ppt is in  different structure ,Docx is in diff structure 

Right now , i converte
d ppt's and docx's to pdf and used pymupdf to extract text and chucked with recursive character split(size =1024, overla
p=120)
Used direct pymupdf lib instead of langchain abstract why you ask?
LET us consider PDF A 
PDF A consist most of i
mages with little text so chunking page wise  results in character length of 150

So I extracted whole pdf text applied 
chunking on that.
**Is this optimal way ? I lose meta data by this method.**

**Coming to logs of excel** .
TBH I don't 
know how work with this.
I combined important columns as one column.

For Eg:
(Title:
....
Desc:
....)
I combined Title 
and desc column as one with column heading in each row so context not missed out.
Here also Each row converted as docume
nt object with size  comes around 250 characters.

I feel wasting resource too much 

What best ways you would suggest?


Thanks in advance

**I know there is atleast 3 templates from azure. I find difficulty to implement those because of my
 access level. Im working with deployed resources, cant create new resource like storage container and document intellig
ence**

```
---

     
 
all -  [ Need help finding better methods implementing RAG ](https://www.reddit.com/r/LangChain/comments/1bz2wpr/need_help_finding_better_methods_implementing_rag/) , 2024-04-09-0910
```
I'm building RAG chat bot with azure open ai and azure ai search

Right now I'm only developing POC 

using streamlit as
 frontend and maintain chat history using session state (not focusing on persistent state rgt now)

Data ingestion pipel
ine is big headache for me even with static data(no updation once used )

Working with PDF , PPT , docx , excel(mostly t
echnical documentation and excel is logs of ticket)

Each pdf have different structure 
Ppt is in  different structure 

Docx is in diff structure 

Right now , i converted ppt and docx to pdf and used pymupdf to extract text and chucked wit
h recursive character split(size =1024, overlap=120)
Used direct pymupdf lib instead of langchain abstract why you ask?


LET us consider PDF A 

PDF A consist most of images with little text so chunking page wise  results in character lengt
h of 150

So I extracted whole pdf text applied chunking on that.
**Is this optimal way ? I lose meta data by this metho
d.**

Coming to logs of excel .
TBH I don't know how work with this.
I combined important columns as one column.

For Eg
:
(Title:
....
Desc:
....)
I combined Title and desc column as one with column heading in each row so context not missed
 out.
Here also Each row converted as document object with size  comes around 250 characters.

I feel wasting resource t
oo much 

What best ways you guys would suggest?

Thanks in advance

```
---

     
 
all -  [ Migrating my prompts to open source language models ](https://www.reddit.com/r/LangChain/comments/1bz1cuq/migrating_my_prompts_to_open_source_language/) , 2024-04-09-0910
```
Open source language models are no serious competitors. I have been migrating a lot of my prompts to open source models,
 and I wrote up this tutorial about how I do it.

https://blog.promptlayer.com/migrating-prompts-to-open-source-models-c
21e1d482d6f
```
---

     
 
all -  [ Text-to-text generation: finetuning vs RAG vs few-shot? ](https://www.reddit.com/r/LangChain/comments/1bz17bg/texttotext_generation_finetuning_vs_rag_vs_fewshot/) , 2024-04-09-0910
```
So I want to automate the conversion of a legal document (5-20 pages) into a different type of document with plain/lay E
nglish + adhere to a specific style and format guidelines (20-100 pages) that are in 3 separate reference pdf documents.


I tried the simplest approach I could think of at first, which was extracting and then providing the expected output f
ormat (headers/sub-headers) in my prompt using a 'custom GPT' on the openai front-end, as well as a one-shot example pai
r of legal doc/converted doc in the prompt window, plus I also uploaded the reference docs to the customgpt (which I thi
nk is used as RAG by the GPT?). 

The result is okay - it gets the format right for the most part, but it ignores many o
f the style guidelines, and summarizes a lot needlessly which leads to information loss. 

I want to now try either more
 advanced RAG (I am a python user and with the exception of recent LCEL releases, am familiar with Langchain as well as 
LlamaIndex), but was also considering finetuning llama-2 with 4-bit quantization. 

Is finetuning without a label even p
ossible in this case? What RAG retrievers or embeddings would you suggest? Any other suggestions? Thanks!
```
---

     
 
all -  [ Should I partner with a publication for my book on Generative AI? ](https://i.redd.it/beyqpwcpu9tc1.png) , 2024-04-09-0910
```
Recently I launched my debut book (self-published) on Generative AI i.e. 'LangChain in your Pocket: Beginners guide to b
uilding Generative AI applications using LLMs' which is going a bestseller since release. A big technical book publicati
on Packt has reached out to me for distribution of this book. This would definitely help me reach a wider audience but t
he price may go up exponentially high and hence unaffordable, specially in India where I've set a slightly lower price. 
What should I do? 
```
---

     
 
all -  [ Insights and Learnings from Building a Complex Multi-Agent System ](https://www.reddit.com/r/LangChain/comments/1byz3lr/insights_and_learnings_from_building_a_complex/) , 2024-04-09-0910
```
tldr: Some insights and learnings from a LLM enthusiast working on a complex Chatbot using multiple agents built with La
ngGraph, LCEL and Chainlit.


Hi everyone! I have seen a lot of interest in multi-agent systems recently, and, as I'm cu
rrently working on a complex one, I thought I might as well share some feedback on my project. Maybe some of you might f
ind it interesting, give some useful feedback, or make some suggestions.

## Introduction: Why am I doing this project?


I'm a business owner and a tech guy with a background in math, coding, and ML. Since early 2023, I've fallen in love wi
th the LLM world. So, I decided to start a new business with 2 friends: a consulting firm on generative AI. As expected,
 we don't have many references. Thus, we decided to create a tool to demonstrate our skillset to potential clients.

Aft
er a brainstorm, we quickly identified that a) RAG is the main selling point, so we need something that uses a RAG; b) W
e believe in agents to automate tasks; c) ChatGPT has shown that asking questions to a chatbot is a much more human-frie
ndly interface than a website; d) Our main weakness is that we are all tech guys, so we might as well compensate for tha
t by building a seller.

From here, the idea was clear: instead, or more exactly, alongside our website, build a chatbot
 that would answer questions about our company, 'sell' our offer, and potentially schedule meetings with our consultants
. Then make some posts on LinkedIn and pray...

Spoiler alert: This project isn't finished yet. The idea is to share som
e insights and learnings with the community and get some feedback.

## Functional specifications

The first step was to 
list some specifications:
* We want a RAG that can answer any question the user might have about our company. For that, 
we will use the content of the company website. Of course, we also need to prevent hallucination, especially on two topi
cs: the website has no information about pricing, and we don't offer SLAs.
* We want it to answer as quickly as possible
 and limit the budget. For that, we will use smaller models like GPT-3.5 and Claude Haiku as often as possible. But that
 limits the reasoning capabilities of our agents, so we need to find a sweet spot.
* We want consistency in the response
s, which is a big problem for RAGs. Questions with similar meanings should generate the same answers, for example, 'What
's your offer?', 'What services do you provide?', and 'What do you do?'.
* Obviously, we don't want visitors to be able 
to ask off-topic questions (e.g., 'How is the weather in North Carolina?'), so we need a way to filter out off-topic, pr
ompt injection, and toxic questions.
* We want to demonstrate that GenAI can be used to deliver more than just chatbots,
 so we want the agents to be able to schedule meetings, send emails to visitors, etc.
* Ideally, we also want the agents
 to be able to qualify the visitor: who they are, what their job is, what their organization is, whether they are a tech
 person or a manager, and if they are looking for something specific with a defined need or are just curious about us.
*
 Ideally, we also want the agents to 'sell' our company: if the visitor indicates their need, match it with our offer an
d 'push' that offer. If they show some interest, let's 'push' for a meeting with our consultants!

## Architecture

### 
Stack

We aren't a startup, we haven't raised funds, and we don't have months to do this. We can't afford to spend more 
than 20 days to get an MVP. Besides, our main selling point is that GenAI projects don't require as much time or budget 
as ML ones.

So, in order to move fast, we needed to use some open-source frameworks:
* For the chatbot, the data is pub
lic, so let's use GPT and Claude as they are the best right now and the API cost is low.
* For the chatbot, Chainlit pro
vides everything we need, except background processing. Let's use that.
* Langchain and LCEL are both flexible and unify
 the interfaces with the LLMs.
* We'll need a rather complicated agent workflow, in fact, multiple ones. LangGraph is mo
re flexible than crew.ai or autogen. Let's use that!

### Design and early versions

#### First version

From the start,
 we knew it was impossible to do it using a 'one prompt, one agent' solution. So we started with a 3-agent solution: one
 to 'find' the required elements on our website (a RAG), one to sell and set up meetings, and one to generate the final 
answer.

The meeting logic was very easy to implement. However, as expected, the chatbot was hallucinating a lot: 'Here 
is a full project for 1k€, with an SLA 7/7 2 hours 99.999%'. And it was a bad seller, with conversations such as 'Hi, wh
o are you?' 'I'm Sellbotix, how can I help you? Do you want a meeting with one of our consultants?'

At this stage, afte
r 10 hours of work, we knew that it was probably doable but would require much more than 3 agents.

#### Second version


The second version used a more complex architecture: a guard to filter the questions, a strategist to make a plan, a se
ller to find some selling points, a seeker and a documentalist for the RAG, a secretary for the schedule meeting functio
n, and a manager to coordinate everything.

It was slow, so we included logic to distribute the work between the agents 
in parallel. Sadly, this can't be implemented using LangGraph, as all agent calls are made using coroutines but are awai
ted, and you can't have parallel branches. So we implemented our own logic.

The result was much better, but far from pe
rfect. And it was a nightmare to improve because changing one agent's system prompt would generate side effects on most 
of the other agents. We also had a hard time defining what each agent would need to see and what to hide. Sending every 
piece of information to every agent is a waste of time and tokens.

And last but not least, the codebase was a mess as w
e did it in a rush. So we decided to restart from scratch.

## Third version, WIP

So currently, we are working on the t
hird version. This project is, by far, much more ambitious than what most of our clients ask us to do (another RAG?). An
d so far, we have learned a ton. I honestly don't know if we will finish it, or even if it's realistic, but it was worth
 it. 'It isn't the destination that matters, it's the journey' has rarely been so true.

Currently, we are working on th
e architecture, and we have nearly finished it. Here are a few insights that we are using, and I wanted to share with yo
u.

### Separation of concern

The two main difficulties when working with a network of agents are a) they don't know wh
en to stop, and b) any change to any agent's system prompt impacts the whole system. It's hard to fix. When building a c
omplex system, separation of concern is key: agents must be split into groups, each one with clear responsibilities and 
interfaces.

The cool thing is that a LangGraph graph is also a Runnable, so you can build graphs that use graphs. So we
 ended up with this: a main graph for the guard and final answer logic. It calls a 'think' graph that decides which subg
raphs should be called. Those are a 'sell' graph, a 'handle' graph, and a 'find' graph (so far).

### Async, parallelism
, and conditional calls

If you want a system to be fast, you need to NOT call all the agents every time. For that, you 
need two things: a planner that decides which subgraph should be called (in our think graph), and you need to use `async
io.gather` instead of letting LangGraph call every graph and await them one by one.

So in the think graph, we have plan
ner and manager agents. We use a standard doer/critic pattern here. When they agree on what needs to be done, they gener
ate a list of instructions and activation orders for each subgraph that are passed to a 'do' node. This node then create
s a list of coroutines and awaits an `asyncio.gather`.

### Limit what each graph must see

We want the system to be fas
t and cost-efficient. Every node of every subgraph doesn't need to be aware of what every other agent does. So we need t
o decide exactly what each agent gets as input. That's honestly quite hard, but doable. It means fewer tokens, so it red
uces the cost and speeds up the response.

## Conclusion

This post is already quite long, so I won't go into the detail
s of every subgraph here. However, if you're interested, feel free to let me know. I might decide to write some addition
al posts about those and the specific challenges we encountered and how we solved them (or not). In any case, if you've 
read this far, thank you!

If you have any feedback, don't hesitate to share. I'd be very happy to read your thoughts an
d suggestions!
```
---

     
 
all -  [ Agentic Workflow Distortion in the Absence of Systemic Self-Reflection ](https://www.reddit.com/r/LangChain/comments/1byyx9f/agentic_workflow_distortion_in_the_absence_of/) , 2024-04-09-0910
```
I wrote this as the intro to a problem I am working in. anyone else thinking about this?

**Strategic Risk Reduction in 
AI Operations: Enhancing Systemic Controls in Agentic Workflows**

It is possible for a workflow comprised of a chain of
 agentic assistants to drift away from the desired operational baseline without hallucinating or scoring poorly on stand
ardized quality tests such as those for relevance, faithfulness, and alignment. Agentic assistants may be observed, meas
ured, and managed on an individualized basis, but nodal evaluations may accurately analyze a point in time step in a wor
kflow while failing to capture systemic distortion only observable at the workflow level while the agentic workflows are
 in motion.

**Agentic Workflow Distortion in the Absence of Systemic Self-Reflection**

The concepts of Agentic Workflo
w Distortion and Systemic Self-Reflection pertain to the dynamics and evaluation within automated systems, particularly 
those that are structured around the autonomous operation of individual agents, referred to as 'agentic workflows.' ....
.tbc

\*\* I have the rest of this writeup if is anyone is interested 
```
---

     
 
all -  [ Use Llamaindex Retriever in Langchain chain ](https://www.reddit.com/r/LangChain/comments/1byvt0t/use_llamaindex_retriever_in_langchain_chain/) , 2024-04-09-0910
```
Hi,

I was wondering if anyone tried out to use a retriever from Llamaindex as retriever in a Langchain chain?

For me t
his is interesting because for now it is difficult to persistently save a ParentDocumentRetriever in Langchain but I thi
nk this is possible with Llamaindex. So I thought I am just using the Llamaindex retriever and pass the results to my ch
ain.

Is there anything I should consider or are there any expericences with this approach?
```
---

     
 
all -  [ GitHub - Upsonic/Tiger: Neuralink for your AI Agents ](https://www.reddit.com/r/aidevtools/comments/1bytoos/github_upsonictiger_neuralink_for_your_ai_agents/) , 2024-04-09-0910
```
Tiger: Neuralink for AI Agents (MIT) (Python)

Hello, we are developing a superstructure that provides an AI-Computer in
terface for AI agents created through the frameworks like LangChain and AutoGen, we have published it completely openly 
under the MIT license.

What it does: Just like human developers, it has some abilities such as running the codes it wri
tes, making mouse and keyboard movements, writing and running Python functions for functions it does not have. AI litera
lly thinks and the interface we provide transforms with real computer actions.

Those who want to contribute can provide
 support under the MIT license and code conduct. [https://github.com/Upsonic/Tiger](https://github.com/Upsonic/Tiger)
```
---

     
 
all -  [ Langtrace: Preview of the new Evaluation dashboard ](https://www.reddit.com/r/LangChain/comments/1byrqps/langtrace_preview_of_the_new_evaluation_dashboard/) , 2024-04-09-0910
```
Hey,

  
I am building an open source project called Langtrace which lets you monitor, debug and evaluate the LLM reques
ts made by your application.

  
[https://github.com/Scale3-Labs/langtrace](https://github.com/Scale3-Labs/langtrace) . 
The integration is only 2 lines of code.

Currently building an Evaluations dashboard which is launching this week. It l
ets you do the following:

1. Create tests - like factual accuracy, bias detection etc. 

2. Automatically capture the L
LM calls to specific tests by passing a testId to the langtrace SDK installed in your code.

3. Evaluate and measure the
 overall success % and how success % trends over time.

The goal here is to get confidence with the model or RAG before 
deploying it to production.

  
Please check out the repository. Would love to hear your thoughts! Thanks!

https://prev
iew.redd.it/5bracw5ki7tc1.png?width=2932&format=png&auto=webp&s=1fe6fac6661d9a5c0c7f701c44d50435f45c7d7f

 
```
---

     
 
all -  [ First NextJS project : Ralla.ai - Itinerary Planner w AI and Chatbot ](https://www.reddit.com/r/nextjs/comments/1byrfo5/first_nextjs_project_rallaai_itinerary_planner_w/) , 2024-04-09-0910
```
Hi guys,

So I started learning React about 8 months ago and quickly made the switch to NextJS, at that time they were s
witching from the pages to app router and introduction of server actions so it was quite a journey with a lot of confusi
on on how to approach certain things in my app but I think we're at a point where I know what I'm doing, sort of... some
times. Could you share your thoughts, recommendations regarding my application below?

[Ralla.ai](https://ralla.ai)

The
re is a registration built in, I'm not trying to spam you but it's just because I need to assign the itinerary to a spec
ific user.. Sorry!

Technology I used : NextJS, Supabase, OpenAI, Langchain

&#x200B;

Many thanks!
```
---

     
 
all -  [ HTML/MARKDOWN splitter vs Code splitter with html/markdown as language. ](https://www.reddit.com/r/LangChain/comments/1byrbxw/htmlmarkdown_splitter_vs_code_splitter_with/) , 2024-04-09-0910
```
While going through the Langchain documentation, I came across the fact that LC is providing separate html and markdown 
splitter and you also have an option for the same two in code splitter as well.   
What is the difference between the tw
o?
```
---

     
 
all -  [ Creation of website to visualize responses generated by LangChain pandas dataframe agent ](https://www.reddit.com/r/LangChain/comments/1byqonr/creation_of_website_to_visualize_responses/) , 2024-04-09-0910
```
I want to make a website where I want to display the responses I am generating using langchain agent. It is actually ana
lysis of educational data, and generated responses are helpful to be used as teaching material. Hence, I want to documen
t it. What would be the easiest and best way to direclty document it onto the website? It would be better to document th
e intermediate steps generated by the agent as well. Thank you
```
---

     
 
all -  [ LangChain vs DSPy ](https://www.reddit.com/r/LangChain/comments/1byn9o7/langchain_vs_dspy/) , 2024-04-09-0910
```
Do you guys really think that using DSPy is a good idea over Langchain? 
For me I think, DSPy is not mature enough and L
angChain provides so many things.
```
---

     
 
all -  [ Help for tutorial ](https://www.reddit.com/r/LangChain/comments/1byn1u2/help_for_tutorial/) , 2024-04-09-0910
```
I just joined here not long ago.
I have learned knowledges from the official documents,but i think it's not suitable for
 me.
I have some programming basics in python,i hope to get some friendly and excellent tutorials that use ollama to cre
ate rather than openai based in langchain.In additional,i want to know how to get high-quality information sources.Engli
sh is not my native language,i'm sorry to any grammar errors.
```
---

     
 
all -  [ Recommendatios for an LLM-Based Conversational Product Search Interface ](https://www.reddit.com/r/LocalLLaMA/comments/1byl8cr/recommendatios_for_an_llmbased_conversational/) , 2024-04-09-0910
```
I'm diving into building a super cool feature for our marketplace – a search utility that understands plain English and 
can run edge-or database functions to assist customers. 

Conceptually, the customer enters 'I'm looking for art from th
e Pacific Northwest' and receives product recommendations or contextual questions like “There are a few styles; do any o
f these [items] fit what you're thinking?”, or “welcome back, your package is x days out”

The project’s toolkit is alre
ady scoped with Supabase, Next.js, TS, Postgres, and a mix of Node and Python on the backend, plus Stripe for the cash f
low. 

Basically, I'm looking for pointers or recommendations on LLMs or tools that play nice or fit with what I'm think
ing. I've had experience with a variety of tools (pytorch, Openai’s API, Hugging Face, langchain, LLlama, and a variety 
of projects), so nothing is really an overly heavy lift.
```
---

     
 
all -  [ GitHub - Upsonic/Tiger: Neuralink for your LangChain Agents ](https://www.reddit.com/r/LangChain/comments/1bykpua/github_upsonictiger_neuralink_for_your_langchain/) , 2024-04-09-0910
```
Tiger: Neuralink for AI Agents (MIT) (Python)

Hello, we are developing a superstructure that provides an AI-Computer in
terface for AI agents created through the LangChain library, we have published it completely openly under the MIT licens
e.

What it does: Just like human developers, it has some abilities such as running the codes it writes, making mouse an
d keyboard movements, writing and running Python functions for functions it does not have. AI literally thinks and the i
nterface we provide transforms with real computer actions.

Those who want to contribute can provide support under the M
IT license and code conduct. [https://github.com/Upsonic/Tiger](https://github.com/Upsonic/Tiger)
```
---

     
 
all -  [ 🚀 SolidEdge - The Open Source, Developer-First Code Comprehension Tool with Notion Integration ](https://www.reddit.com/r/LangChain/comments/1byk8nk/solidedge_the_open_source_developerfirst_code/) , 2024-04-09-0910
```
Hey LangChain devs! 👋 Check out SolidEdge – the open source code comprehension tool you've been waiting for. Powered by 
GPT and built by devs like us, it's your personal coding sidekick. With Notion integration, it keeps you aligned with bu
siness goals. No more feeling lost in code – embrace true developer-centric coding! Star us on \[GitHub\](https://github
.com/AI-Citizen/SolidGPT) and dive in on the \[VSCode Marketplace\](https://marketplace.visualstudio.com/items?itemName=
AICT.solidgpt). Let's revolutionize coding together! 🚀
```
---

     
 
all -  [ GitHub - Upsonic/Tiger: Neuralink for your AI Agents ](https://www.reddit.com/r/Langchaindev/comments/1byep8n/github_upsonictiger_neuralink_for_your_ai_agents/) , 2024-04-09-0910
```
Tiger: Neuralink for AI Agents (MIT) (Python)

Hello, we are developing a superstructure that provides an AI-Computer in
terface for AI agents created through the LangChain library, we have published it completely openly under the MIT licens
e.

What it does: Just like human developers, it has some abilities such as running the codes it writes, making mouse an
d keyboard movements, writing and running Python functions for functions it does not have. AI literally thinks and the i
nterface we provide transforms with real computer actions.

As Upsonic, we are currently working on improving the Neural
ink for AI Agents definition and responding to community support.

Those who want to contribute can provide support unde
r the MIT license and code conduct. [https://github.com/Upsonic/Tiger](https://github.com/Upsonic/Tiger)
```
---

     
 
all -  [ I just make Neuralink for agents (LangChain, AutoGen) ](https://www.reddit.com/r/AI_Agents/comments/1byeexs/i_just_make_neuralink_for_agents_langchain_autogen/) , 2024-04-09-0910
```
Tiger: Neuralink for AI Agents (MIT) (Python)

&#x200B;

Hello, we are developing a superstructure that provides an AI-C
omputer interface for AI agents created through the LangChain library, we have published it completely openly under the 
MIT license.

&#x200B;

What it does: Just like human developers, it has some abilities such as running the codes it wri
tes, making mouse and keyboard movements, writing and running Python functions for functions it does not have. AI litera
lly thinks and the interface we provide transforms with real computer actions.

&#x200B;

&#x200B;

As Upsonic, we are c
urrently working on improving the Neuralink for AI Agents definition and responding to community support.

&#x200B;

&#x
200B;

Those who want to contribute can provide support under the MIT license and code conduct. [https://github.com/Upso
nic/Tiger](https://github.com/Upsonic/Tiger)
```
---

     
 
all -  [ Storing tool retrieved data in conversation history ](https://www.reddit.com/r/LangChain/comments/1byd0e8/storing_tool_retrieved_data_in_conversation/) , 2024-04-09-0910
```
I've been playing around with pulling data from APIs, feeding that into the language model's chat and then conversing ov
er that context.  One recent use case I've been considering is allowing the agent to do multiple tasks, so the API calls
 are determined by the AI solution rather than being hard coded.

The obvious solution to me is to use a conversational 
chat agent that can react and use tools that make the API calls.  The problem I'm experiencing though is that the return
ed content from the API call function doesn't appear to get stored in my ConversationBufferMemory.  It only stores the h
uman inputs, and the AI's outputs, but not the 'Observation' that contains the returned full context.

The reason I'd li
ke this in the history is to prevent the need for additional API calls when the user begins to ask follow-up questions a
bout the data which has already been retrieved by a tool.  It seems very inefficient to pull the same data every time th
ey have a follow-up question, which is what it's currently doing.  Below is an example of what I'm doing.

    template 
= 'First, evaluate the context provided by preceding messages to inform your response. Only if you can't answer the ques
tions from that should you use available tools.'
    
    memory = ConversationBufferMemory(
            memory_key='cha
t_history',
            return_messages=True
        )
    
    tools = [get_ticket_info]
    
    agent = initialize_ag
ent(
        tools=tools,
        llm=llm,
        agent='chat-conversational-react-description',
        memory=memory,

        verbose=True,
        agent_kwargs={'prefix': template}
    )

I've also tried using the create\_react\_agent()
 function to create the agent which I know is the new way to do this, but it doesn't appear to be conversational as it w
ill not remember any message history.  This is why I'm using the initialize\_agent() function instead.  At this point I'
m tempted to go away with LangChain and use OpenAI's API directly where I would have more control over what goes into th
e message history.

Any tricks you're aware of, or am I approaching this in a naive way?  Appreciate any wisdom you can 
bestow.

  
Edit: I got this to work easily enough using OpenAI directly.  See my response below to one of my replies if
 interested.
```
---

     
 
all -  [ a model that can handle about 50k inputs and less than or equal to 7B parameters(not fully necessary ](https://www.reddit.com/r/huggingface/comments/1bybrzw/a_model_that_can_handle_about_50k_inputs_and_less/) , 2024-04-09-0910
```
I am looking for a model that can handle about 50k inputs and less than or equal to 7B parameters(not fully necessary) a
nd summarize the text.

I was using Mistral-7B before but it has limit of 32k inputs so I need an alternative 

PS I'm u
sing HuggingFaceHub to get the LLM from LangChain so I can't download model > 10gb
```
---

     
 
all -  [ Working with diverse data to create 30 to 35 pages document and Managing the retrieval. ](https://www.reddit.com/r/LangChain/comments/1by9iqn/working_with_diverse_data_to_create_30_to_35/) , 2024-04-09-0910
```
I have been working on the large data. The data consist of talks from the different anchor persons, also there are comme
nts in numerical representation like for example '*how many people agreed and how many are disagreed'.* and on which ses
sion they are disscusing the point of agenda and on which bill number they place a talk.   
  
So my question is: I want
 to generate the document a large document which contains multiple sections almost 20 sections. Each section has diverse
 and different instructions so how do I manage my vectordb calls. ? because each section of the document is different so
 how to make a calls to retreival automatically based on the sections conditions. ?
```
---

     
 
all -  [ How to make a RAG conscious of the documents it have? Amazon Bedrock ](https://www.reddit.com/r/LangChain/comments/1by8u01/how_to_make_a_rag_conscious_of_the_documents_it/) , 2024-04-09-0910
```
I'm currently working with AWS Bedrock and Langchain while it retrieves good answers when I want to ask it stuff like co
mparing documents or listing the documents on its data sources Its unable to do it. It seems like its not conscious of i
ts environment. Does anyone has some experience working with this? Like I want it to be a typical RAG application based 
on some documents but I want it to be conscious of the data it have like comparing versions of the same documents...
```
---

     
 
all -  [ Challenges of Scaling RAG applications ](https://www.reddit.com/r/LangChain/comments/1by7s2m/challenges_of_scaling_rag_applications/) , 2024-04-09-0910
```
I'm thinking about writing a detailed blog on the Challenges you face while scaling your RAG apps. Please comment some s
uggestions you would like me to discuss in the blog.  
```
---

     
 
all -  [ New documentation is still bad ](https://www.reddit.com/r/LangChain/comments/1by72bo/new_documentation_is_still_bad/) , 2024-04-09-0910
```
I just read their [new blog post](https://blog.langchain.dev/langchain-documentation-refresh/), about the new documentat
ion website. It's very curious and funny.

It goes through the Diataxis taxonomy for documentation, which I find useful 
and aligns with how my brain works.

Just to throw everything out of the window and say: we mixed and matched every sect
ion of Diataxis and you can find tutorials spread all over the place, mixed with reference and explanations!

Take a loo
k at this section of the post:


> This section should contain mostly conceptual Tutorials, References, and Explanations
 of the components they cover.
> 
> Note: As a general rule of thumb, everything covered in the Expression Language and 
Components sections (with the exception of the Composition section of components) should cover only components that exis
t in langchain_core.

Impressive! They need to explain what's where, and even introduce a rule about langchain_core that
 is broken from the get go. And when you go to the socs the components section isn't even in the menu to be selected!

I
 mean, just make it simple:

* Tutorials (quick start, use cases with in depth explanations, etc)
* How to guides (terse
, context free guides such as how to create a chain, new runnable from scratch, new agent from scratch, how to visualize
 a chain, how to pass a system prompt to a model, how to make models spit structured output, etc)
* Explanation (langcha
in purpose, package organization, what is LCEL, what is a chain/agent/runnable/etc, model vs chat model, what is a tool/
toolkit, what is a function call etc). Accept a small amount of repetition from what we have in tutorials.
* Reference (
API docs)

Wouldn't that be simpler? I'm so frustrated with this...


```
---

     
 
all -  [ Evaluating RAG on custom Q&As ](https://www.reddit.com/r/LangChain/comments/1by54rq/evaluating_rag_on_custom_qas/) , 2024-04-09-0910
```
We are trying to get our feet wet with RAG with a small engineering team. I want to build a RAG system querying an exten
sive internal documents system. With the available choice of LLMs, embedding models, vector databases, hyperparameters i
t's easy to get overwhelmed. So what I want is to create a test dataset manually with like ten-twenty questions and answ
ers we would like to receive (or multiple answer options for each question??) and automate deployment of several combina
tions of different LLMs, hyperparameters, embedding models, etc and compare the actuals against the gold standard answer
s (using ROUGE score maybe??). Does that make sense? Are there any tools/frameworks I need to be aware of to do somethin
g like that for me? Thanks!
```
---

     
 
all -  [ How to deploy a RAG-tuned AI chatbot/LLM using AWS Bedrock ](https://www.reddit.com/r/MLQuestions/comments/1by1c4j/how_to_deploy_a_ragtuned_ai_chatbotllm_using_aws/) , 2024-04-09-0910
```
Hey guys, so I am building a chatbot which uses a RAG-tuned LLM in AWS Bedrock (and deployed using AWS Lambda endpoints)
.

How do I avoid my LLM from being having to be RAG-tuned every single time a user asks his/her first question? I am th
inking of storing the RAG-tuned LLM in an AWS S3 bucket. If I do this, I believe I will have to store the LLM model para
meters and the vector store index in the S3 bucket. Doing this would mean every single time a user asks his/her first qu
estion (and subsequent questions), I will just be loading the the RAG-tuned LLM from the S3 bucket (rather than having t
o run RAG-tuning every single time when a user asks his/her first question, which will save me RAG-tuning costs and late
ncy).

Would this design work? I have a sample of my script below:

    import os
    import json
    import boto3
    f
rom langchain.document_loaders import PyPDFLoader
    from langchain.text_splitter import RecursiveCharacterTextSplitter

    from langchain.embeddings import BedrockEmbeddings
    from langchain.vectorstores import FAISS
    from langchain.
indexes import VectorstoreIndexCreator
    from langchain.llms.bedrock import Bedrock
    
    def save_to_s3(model_para
ms, vector_store_index, bucket_name, model_key, index_key):
        s3 = boto3.client('s3')
        
        # Save mode
l parameters to S3
        s3.put_object(Body=model_params, Bucket=bucket_name, Key=model_key)
        
        # Save v
ector store index to S3
        s3.put_object(Body=vector_store_index, Bucket=bucket_name, Key=index_key)
    
    def l
oad_from_s3(bucket_name, model_key, index_key):
        s3 = boto3.client('s3')
        
        # Load model parameters
 from S3
        model_params = s3.get_object(Bucket=bucket_name, Key=model_key)['Body'].read()
        
        # Load 
vector store index from S3
        vector_store_index = s3.get_object(Bucket=bucket_name, Key=index_key)['Body'].read()

        
        return model_params, vector_store_index
    
    def initialize_hr_system(bucket_name, model_key, index
_key):
        s3 = boto3.client('s3')
        
        try:
            # Check if model parameters and vector store in
dex exist in S3
            s3.head_object(Bucket=bucket_name, Key=model_key)
            s3.head_object(Bucket=bucket_n
ame, Key=index_key)
            
            # Load model parameters and vector store index from S3
            model_pa
rams, vector_store_index = load_from_s3(bucket_name, model_key, index_key)
            
            # Deserialize and re
construct the RAG-tuned LLM and vector store index
            llm = Bedrock.deserialize(json.loads(model_params))
     
       index = VectorstoreIndexCreator.deserialize(json.loads(vector_store_index))
        except s3.exceptions.ClientEr
ror:
            # Model parameters and vector store index don't exist in S3
            # Create them and save to S3
  
          data_load = PyPDFLoader('Glossary_of_Terms.pdf')
            data_split = RecursiveCharacterTextSplitter(separ
ators=['\n\n', '\n', ' ', ''], chunk_size=100, chunk_overlap=10)
            data_embeddings = BedrockEmbeddings(credent
ials_profile_name='default', model_id='amazon.titan-embed-text-v1')
            data_index = VectorstoreIndexCreator(tex
t_splitter=data_split, embedding=data_embeddings, vectorstore_cls=FAISS)
            index = data_index.from_loaders([da
ta_load])
            
            llm = Bedrock(
                credentials_profile_name='default',
                mo
del_id='mistral.mixtral-8x7b-instruct-v0:1',
                model_kwargs={
                    'max_tokens_to_sample': 
3000,
                    'temperature': 0.1,
                    'top_p': 0.9
                }
            )
         
   
            # Serialize model parameters and vector store index
            serialized_model_params = json.dumps(llm
.serialize())
            serialized_vector_store_index = json.dumps(index.serialize())
            
            # Save 
model parameters and vector store index to S3
            save_to_s3(serialized_model_params, serialized_vector_store_in
dex, bucket_name, model_key, index_key)
        
        return index, llm
    
    def hr_rag_response(index, llm, ques
tion):
        hr_rag_query = index.query(question=question, llm=llm)
        return hr_rag_query
    
    # S3 bucket c
onfiguration
    bucket_name = 'your-bucket-name'
    model_key = 'models/chatbot_model.json'
    index_key = 'indexes/c
hatbot_index.json'
    
    # Initialize the system
    index, llm = initialize_hr_system(bucket_name, model_key, index_
key)
    
    # Serve user requests
    while True:
        user_question = input('User: ')
        response = hr_rag_re
sponse(index, llm, user_question)
        print('Chatbot:', response)
```
---

     
 
all -  [ How to deploy a RAG-tuned AI chatbot/LLM using AWS Bedrock ](https://www.reddit.com/r/aws/comments/1by169j/how_to_deploy_a_ragtuned_ai_chatbotllm_using_aws/) , 2024-04-09-0910
```
Hey guys, so I am building a chatbot which uses a RAG-tuned LLM in AWS Bedrock (and deployed using AWS Lambda endpoints)
.

How do I avoid my LLM from being having to be RAG-tuned every single time a user asks his/her first question? I am th
inking of storing the RAG-tuned LLM in an AWS S3 bucket. If I do this, I believe I will have to store the LLM model para
meters and the vector store index in the S3 bucket. Doing this would mean every single time a user asks his/her first qu
estion (and subsequent questions), I will just be loading the the RAG-tuned LLM from the S3 bucket (rather than having t
o run RAG-tuning every single time when a user asks his/her first question, which will save me RAG-tuning costs and late
ncy).   


Would this design work? I have a sample of my script below:  


    import os
    import json
    import boto
3
    from langchain.document_loaders import PyPDFLoader
    from langchain.text_splitter import RecursiveCharacterTextS
plitter
    from langchain.embeddings import BedrockEmbeddings
    from langchain.vectorstores import FAISS
    from lan
gchain.indexes import VectorstoreIndexCreator
    from langchain.llms.bedrock import Bedrock
    
    def save_to_s3(mod
el_params, vector_store_index, bucket_name, model_key, index_key):
        s3 = boto3.client('s3')
        
        # Sa
ve model parameters to S3
        s3.put_object(Body=model_params, Bucket=bucket_name, Key=model_key)
        
        #
 Save vector store index to S3
        s3.put_object(Body=vector_store_index, Bucket=bucket_name, Key=index_key)
    
  
  def load_from_s3(bucket_name, model_key, index_key):
        s3 = boto3.client('s3')
        
        # Load model par
ameters from S3
        model_params = s3.get_object(Bucket=bucket_name, Key=model_key)['Body'].read()
        
        
# Load vector store index from S3
        vector_store_index = s3.get_object(Bucket=bucket_name, Key=index_key)['Body'].
read()
        
        return model_params, vector_store_index
    
    def initialize_hr_system(bucket_name, model_key
, index_key):
        s3 = boto3.client('s3')
        
        try:
            # Check if model parameters and vector s
tore index exist in S3
            s3.head_object(Bucket=bucket_name, Key=model_key)
            s3.head_object(Bucket=b
ucket_name, Key=index_key)
            
            # Load model parameters and vector store index from S3
            m
odel_params, vector_store_index = load_from_s3(bucket_name, model_key, index_key)
            
            # Deserialize
 and reconstruct the RAG-tuned LLM and vector store index
            llm = Bedrock.deserialize(json.loads(model_params)
)
            index = VectorstoreIndexCreator.deserialize(json.loads(vector_store_index))
        except s3.exceptions.C
lientError:
            # Model parameters and vector store index don't exist in S3
            # Create them and save t
o S3
            data_load = PyPDFLoader('Glossary_of_Terms.pdf')
            data_split = RecursiveCharacterTextSplitte
r(separators=['\n\n', '\n', ' ', ''], chunk_size=100, chunk_overlap=10)
            data_embeddings = BedrockEmbeddings(
credentials_profile_name='default', model_id='amazon.titan-embed-text-v1')
            data_index = VectorstoreIndexCrea
tor(text_splitter=data_split, embedding=data_embeddings, vectorstore_cls=FAISS)
            index = data_index.from_load
ers([data_load])
            
            llm = Bedrock(
                credentials_profile_name='default',
           
     model_id='mistral.mixtral-8x7b-instruct-v0:1',
                model_kwargs={
                    'max_tokens_to_sa
mple': 3000,
                    'temperature': 0.1,
                    'top_p': 0.9
                }
            )
  
          
            # Serialize model parameters and vector store index
            serialized_model_params = json.du
mps(llm.serialize())
            serialized_vector_store_index = json.dumps(index.serialize())
            
            
# Save model parameters and vector store index to S3
            save_to_s3(serialized_model_params, serialized_vector_s
tore_index, bucket_name, model_key, index_key)
        
        return index, llm
    
    def hr_rag_response(index, ll
m, question):
        hr_rag_query = index.query(question=question, llm=llm)
        return hr_rag_query
    
    # S3 b
ucket configuration
    bucket_name = 'your-bucket-name'
    model_key = 'models/chatbot_model.json'
    index_key = 'in
dexes/chatbot_index.json'
    
    # Initialize the system
    index, llm = initialize_hr_system(bucket_name, model_key,
 index_key)
    
    # Serve user requests
    while True:
        user_question = input('User: ')
        response = hr
_rag_response(index, llm, user_question)
        print('Chatbot:', response)

&#x200B;
```
---

     
 
all -  [ How to preprocess large JSOn response of OpenAI function call in Flowise? ](https://www.reddit.com/r/flowise/comments/1by0p4r/how_to_preprocess_large_json_response_of_openai/) , 2024-04-09-0910
```
https://preview.redd.it/87bj9gc031tc1.png?width=2632&format=png&auto=webp&s=eaffcba5154c7dcbddd4b428fce7021c954752a5

Gr
eetings, I am working with Flowise to build up complex flows with my own APIs which return some data from Notion. Howeve
r, the response from Notion is quite a big JSON which cannot be used to pass to the ChatOpenAI component. I don't know h
ow to intercept some extra steps to process the response from the OpenAPI Chain as in the attachment image. Should I jus
t add another tool like StructedOutputParser,.. to the OpenAI Tool Agent?

One another approach is tuning my API respons
es, but I just wonder if we can utilize the power of Langchain in Flowise on existing APIs or not.

May I ask if anyone 
can share with me some Flowise templates that can work with large responses too?
```
---

     
 
all -  [ RAG returns concocted results  ](https://www.reddit.com/r/LangChain/comments/1bxwxtu/rag_returns_concocted_results/) , 2024-04-09-0910
```
I have one banking related document with several overlapping topics. Say one topic is related to credit card request, an
other related to cheque book request, another relating to account deactivation request. Mind that each of topic in itsel
f are lengthy.

When in the retrieval chain, I ask a question 'how to raise requests', the result is a mixture from all 
of the above topics. First few lines describe credit card procedure and then bridge to checkbook. Which is wrong as each
 process has a different steps.

I'm using chunking strategy of 1000, default sentence transformers embedding, qdrant fo
r as retriever, and gpt3.5 turbo 16k for llm.

Also the llm gives a disclaimer/note at the end saying that steps vary pe
r organisation. Tried several prompts to remove disclaimer but nothing seems to work.

Any help / prompt would be greatl
y appreciated.
```
---

     
 
all -  [ 100 Coupons for FREE Udemy and Coursera Courses with Certificates! ](https://www.reddit.com/r/Udemy/comments/1bxvaix/100_coupons_for_free_udemy_and_coursera_courses/) , 2024-04-09-0910
```
Python And Flask Framework Complete Course For Beginners

[https://courze.org/python-and-flask-framework-complete-course
-for-beginners/](https://courze.org/python-and-flask-framework-complete-course-for-beginners/)

&#x200B;

CSS, Bootstrap
, JavaScript And PHP Stack Complete Course

[https://courze.org/css-bootstrap-javascript-and-php-stack-complete-course/]
(https://courze.org/css-bootstrap-javascript-and-php-stack-complete-course/)

&#x200B;

JavaScript deep : Advanced Techn
iques (Practice Tests Only)

[https://courze.org/javascript-deep-advanced-techniques-practice-tests-only/](https://courz
e.org/javascript-deep-advanced-techniques-practice-tests-only/)

&#x200B;

Assembler Exploits(Practice Tests only) Binar
y Code Breakers

[https://courze.org/assembler-exploitspractice-tests-only-binary-code-breakers/](https://courze.org/ass
embler-exploitspractice-tests-only-binary-code-breakers/)

&#x200B;

PODCAST Crea tu Podcast y llega a miles 2023 Actual
izado

[https://courze.org/podcast-crea-tu-podcast-y-llega-a-miles-2023-actualizado/](https://courze.org/podcast-crea-tu
-podcast-y-llega-a-miles-2023-actualizado/)

&#x200B;

Joint Diploma (Oxford) : Couples /Art Therapy (Accredited)

[http
s://courze.org/joint-diploma-oxford-couples-art-therapy-accredited/](https://courze.org/joint-diploma-oxford-couples-art
-therapy-accredited/)

&#x200B;

Master Android by Building 3 Applications in Kotlin Language

[https://courze.org/maste
r-android-by-building-3-applications-in-kotlin-language/](https://courze.org/master-android-by-building-3-applications-i
n-kotlin-language/)

&#x200B;

Master Android Application Build 3 Applications from Scratch

[https://courze.org/master-
android-application-build-3-applications-from-scratch/](https://courze.org/master-android-application-build-3-applicatio
ns-from-scratch/)

&#x200B;

Crea paginas de ventas para vender productos digi en Hotmart

[https://courze.org/crea-pagi
nas-de-ventas-para-vender-productos-digi-en-hotmart/](https://courze.org/crea-paginas-de-ventas-para-vender-productos-di
gi-en-hotmart/)

&#x200B;

TOEFL Preparation: Reading Mastery

[https://courze.org/toefl-preparation-reading-mastery/](h
ttps://courze.org/toefl-preparation-reading-mastery/)

&#x200B;

30 HTML CSS & JavaScript Projects A Beginner’s Guide to
 JS

[https://courze.org/30-html-css-javascript-projects-a-beginners-guide-to-js/](https://courze.org/30-html-css-javasc
ript-projects-a-beginners-guide-to-js/)

&#x200B;

20 Web Projects build 20 HTML, CSS and JavaScript projects

[https://
courze.org/20-web-projects-build-20-html-css-and-javascript-projects/](https://courze.org/20-web-projects-build-20-html-
css-and-javascript-projects/)

&#x200B;

Android App’s Development Masterclass – Build 2 Apps – Java

[https://courze.or
g/android-apps-development-masterclass-build-2-apps-java/](https://courze.org/android-apps-development-masterclass-build
-2-apps-java/)

&#x200B;

Android Apps Development in Hindi and Build 10 Applications

[https://courze.org/android-apps-
development-in-hindi-and-build-10-applications/](https://courze.org/android-apps-development-in-hindi-and-build-10-appli
cations/)

&#x200B;

Android Very Basic App Development Course with Java in Hindi

[https://courze.org/android-very-basi
c-app-development-course-with-java-in-hindi/](https://courze.org/android-very-basic-app-development-course-with-java-in-
hindi/)

&#x200B;

Practical HTML, CSS, JS: 10 Real-World Projects for Practice

[https://courze.org/practical-html-css-
js-10-real-world-projects-for-practice/](https://courze.org/practical-html-css-js-10-real-world-projects-for-practice/)


&#x200B;

Android Course Build 3 Applications from Scratch with Java

[https://courze.org/android-course-build-3-applic
ations-from-scratch-with-java/](https://courze.org/android-course-build-3-applications-from-scratch-with-java/)

&#x200B
;

Simple React App from Scratch

[https://courze.org/build-a-simple-react-app-from-scratch/](https://courze.org/build-a
-simple-react-app-from-scratch/)

&#x200B;

Pitch Deck Hero: Business Presentation and Communication

[https://courze.or
g/pitch-deck-hero-business-presentation-and-communication/](https://courze.org/pitch-deck-hero-business-presentation-and
-communication/)

&#x200B;

Business Process Optimization with Lean Six Sigma

[https://courze.org/business-process-opti
mization-with-lean-six-sigma/](https://courze.org/business-process-optimization-with-lean-six-sigma/)

&#x200B;

Bloggin
g For Beginners – How to Start a Blog & Make Money

[https://courze.org/blogging-for-beginners-how-to-start-a-blog-make-
money/](https://courze.org/blogging-for-beginners-how-to-start-a-blog-make-money/)

&#x200B;

Writing With Flair: How To
 Become An Exceptional Writer

[https://courze.org/writing-with-flair-how-to-become-an-exceptional-writer/](https://cour
ze.org/writing-with-flair-how-to-become-an-exceptional-writer/)

&#x200B;

Process of Undertaking a Successful Energy Au
dit

[https://courze.org/process-of-undertaking-a-successful-energy-audit/](https://courze.org/process-of-undertaking-a-
successful-energy-audit/)

&#x200B;

Craft stunning UI UX design as a digital product designer

[https://courze.org/craf
t-stunning-ui-ux-design-as-a-digital-product-designer/](https://courze.org/craft-stunning-ui-ux-design-as-a-digital-prod
uct-designer/)

&#x200B;

Mastering LangChain and AWS: A Guide to Economic Analysis

[https://courze.org/mastering-langc
hain-and-aws-a-guide-to-economic-analysis/](https://courze.org/mastering-langchain-and-aws-a-guide-to-economic-analysis/
)

&#x200B;

Mastering Excel VBA User Forms

[https://courze.org/mastering-excel-vba-user-forms/](https://courze.org/mas
tering-excel-vba-user-forms/)

&#x200B;

Python Bootcamp: Master Python with Real-World Projects

[https://courze.org/py
thon-bootcamp-master-python-with-real-world-projects/](https://courze.org/python-bootcamp-master-python-with-real-world-
projects/)

&#x200B;

Executive Diploma of Chief Digital Officer

[https://courze.org/executive-diploma-of-chief-digital
-officer/](https://courze.org/executive-diploma-of-chief-digital-officer/)

&#x200B;

Learn how to fit fitness into your
 life

[https://courze.org/learn-how-to-fit-fitness-into-your-life/](https://courze.org/learn-how-to-fit-fitness-into-yo
ur-life/)

&#x200B;

Mini MBA in Human Resources Management

[https://courze.org/mini-mba-in-human-resources-management/
](https://courze.org/mini-mba-in-human-resources-management/)

&#x200B;

File & Folder Management Using PowerShell

[htt
ps://courze.org/file-folder-management-using-powershell/](https://courze.org/file-folder-management-using-powershell/)


&#x200B;

Professional Diploma in Unit Economics Management

[https://courze.org/professional-diploma-in-unit-economics-
management/](https://courze.org/professional-diploma-in-unit-economics-management/)

&#x200B;

Learn Salesforce (Admin +
 Developer) with LWC Live Project

[https://courze.org/learn-salesforce-admin-developer-with-lwc-live-project/](https://
courze.org/learn-salesforce-admin-developer-with-lwc-live-project/)

&#x200B;

Como Ser Hacker: 13 Importantes Lições An
tes de Começar

[https://courze.org/como-ser-hacker-13-importantes-licoes-antes-de-comecar/](https://courze.org/como-ser
-hacker-13-importantes-licoes-antes-de-comecar/)

&#x200B;

Talent Acquisition: HR Planning, Recruiting and Onboarding


[https://courze.org/talent-acquisition-hr-planning-recruiting-and-onboarding/](https://courze.org/talent-acquisition-hr-
planning-recruiting-and-onboarding/)

&#x200B;

Curso de Hostinger 2024: El Hosting Ideal Para tu Página Web

[https://c
ourze.org/curso-de-hostinger-2023-el-hosting-ideal-para-tu-pagina-web/](https://courze.org/curso-de-hostinger-2023-el-ho
sting-ideal-para-tu-pagina-web/)

&#x200B;

Cómo Crear una Página Web con WordPress y ChatGPT Desde Cero

[https://courz
e.org/como-crear-una-pagina-web-con-wordpress-y-chatgpt-desde-cero/](https://courze.org/como-crear-una-pagina-web-con-wo
rdpress-y-chatgpt-desde-cero/)

&#x200B;

Ms Excel/Excel 2023 – The Complete Introduction to Excel

[https://courze.org/
ms-excel-excel-2022-the-complete-introduction-to-excel/](https://courze.org/ms-excel-excel-2022-the-complete-introductio
n-to-excel/)

&#x200B;

Cómo Crear una Página Web con WordPress Para Principiantes

[https://courze.org/como-crear-una-p
agina-web-con-wordpress-para-principiantes/](https://courze.org/como-crear-una-pagina-web-con-wordpress-para-principiant
es/)

&#x200B;

Cómo Crear Una Tienda Online Desde Cero Para Principiantes

[https://courze.org/como-crear-una-tienda-on
line-desde-cero-para-principiantes/](https://courze.org/como-crear-una-tienda-online-desde-cero-para-principiantes/)

&#
x200B;

&#x200B;
```
---

     
 
all -  [ Gemini 👍🌚 ](https://v.redd.it/um4exjmvnysc1) , 2024-04-09-0910
```
Never knew 14 yrs ago, Rick astley taught about LangChain  through his songs. 🤯😂😂

#aiml #aiforfun #rofl #gemini #google

```
---

     
 
MachineLearning -  [ [D] How to get the source documents from the retrieved context for RAG?  ](https://www.reddit.com/r/MachineLearning/comments/1bvoc1t/d_how_to_get_the_source_documents_from_the/) , 2024-04-09-0910
```
I'm not using Lanchain but only making API calls to an LLM service provider. The retriever is connected to a vector DB, 
and I would like to know what the LLM refers to WITHIN that retrieved context whenever it provides an answer, similar to
 how return_source_documents works in Langchain.

I'm using AzureOpenAI. I couldn't find much in their docs that related
 to returning the source documents. Any help will be greatly appreciated!

```
---

     
 
MachineLearning -  [ [P] RAG pipeline to query the ML Engineering Open Book ](https://www.reddit.com/r/MachineLearning/comments/1bu4wyx/p_rag_pipeline_to_query_the_ml_engineering_open/) , 2024-04-09-0910
```
I built a quick RAG implementation using Langchain to make it easy to query the [ML Engineering Open Book](https://githu
b.com/stas00/ml-engineering) by [Stas Bekman](https://twitter.com/StasBekman). The Multi-Vector retriever gave pretty go
od results and was quite easy to set up too. 

Github link - [https://github.com/shreyansh26/RAG-ML-Engg-Open-Book](http
s://github.com/shreyansh26/RAG-ML-Engg-Open-Book)

Hope this is useful for folks!
```
---

     
 
MachineLearning -  [ [Project] FinancialAdvisorGPT : LLM+RAG Boilerplate Project ](https://www.reddit.com/r/MachineLearning/comments/1btlpgd/project_financialadvisorgpt_llmrag_boilerplate/) , 2024-04-09-0910
```
FinancialAdvisorGPT is a boilerplate project designed for RAG (Retriever-Augmented Generation) and LLM (Large Language M
odel) applications in financial analysis. Built on a technology stack including MongoDB, MongoDB VectorDB, Chroma, FastA
PI, Langchain, and React submodule for UI, it offers a framework for developers to implement and customize RAG+LLM proje
cts. Leveraging parallelized data pipelines, FinancialAdvisorGPT processes and integrates various data sources such as s
tock data, news, SEC filings, and local PDFs.

Github project includes long documentation on how the project is structur
ed, how LLM+RAG works for specific task : [https://github.com/mburaksayici/FinancialAdvisorGPT](https://github.com/mbura
ksayici/FinancialAdvisorGPT)
```
---

     
 
MachineLearning -  [ [Project] Picachain, image search made simple. ](https://www.reddit.com/r/MachineLearning/comments/1bt7epv/project_picachain_image_search_made_simple/) , 2024-04-09-0910
```
I am working on creating something for image search, basically something like langchain for images. Probably add videos 
too.

Currently supports chromaDB. Working on pinecone and other vector dbs. [https://github.com/d1pankarmedhi/picachain
](https://github.com/d1pankarmedhi/picachain)

Will you use something like this? What else should I add? Feel free to ad
d your views.

Appreciate your feedback or any feature ideas :)

&#x200B;
```
---

     
 
deeplearning -  [ Tengyu Ma on Voyage AI - Weaviate Podcast #91! ](https://www.reddit.com/r/deeplearning/comments/1bjft8i/tengyu_ma_on_voyage_ai_weaviate_podcast_91/) , 2024-04-09-0910
```
**Voyage AI** is the newest giant in the embedding, reranking, and search model game!

I am SUPER excited to publish our
 latest Weaviate podcast with Tengyu Ma, Co-Founder of Voyage AI and Assistant Professor at Stanford University!

We beg
an the podcast with a deep dive into everything embedding model training and contrastive learning theory. Tengyu deliver
ed a **masterclass** in everything from scaling laws to multi-vector representations, neural architectures, representati
on collapse, data augmentation, semantic similarity, and more! I am beyond impressed with Tengyu's extensive knowledge a
nd explanations of all these topics.

The next chapter dives into a case study Voyage AI did **fine-tuning an embedding 
model for the LangChain documentation.** This is an absolutely fascinating example of the role of continual fine-tuning 
with very new concepts (for example, very few people were talking about chaining together LLM calls 2 years ago), as wel
l as the data efficiency advances in fine-tuning.

We concluded by discussing ML systems challenges in serving an embedd
ings API. Particularly the challenge of detecting if a request is for batch or query inference and the optimizations tha
t go into either say \~100ms latency for a query embedding or maximizing throughput for batch embeddings.

I hope you fi
nd the podcast interesting, more than happy to discuss any of these topics with you or answer any questions about the co
ntent in the podcast! Thank you so much!

YouTube: [https://www.youtube.com/watch?v=xPdyivfheqI](https://www.youtube.com
/watch?v=xPdyivfheqI)

Spotify: [https://spotifyanchor-web.app.link/e/u6XPLYfF7Hb](https://spotifyanchor-web.app.link/e/
u6XPLYfF7Hb)
```
---

     
