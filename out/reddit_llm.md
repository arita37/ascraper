 
all -  [ An OSS tool for turning entire websites into LLM-ready markdown ](https://www.reddit.com/r/mlops/comments/1c5usna/an_oss_tool_for_turning_entire_websites_into/) , 2024-04-17-0910
```
While building [mendable.ai](https://mendable.ai) \- we found that feeding LLMs well-structured markdown improved accura
cy. We also found that it was hard.   


So, we released an open-source repo ([https://github.com/mendableai/firecrawl](
https://github.com/mendableai/firecrawl)) and API ([https://firecrawl.dev](https://firecrawl.dev)) that crawls and turns
 entire websites into a markdown with just a few lines of code. 

It handles

* Crawling without consistent sitemaps
* B
uilding the infra to handle running many scraping jobs
* Proxying, hosting headless browsers at scale
* Conversion to cl
ean markdown
* Caching
* Handling images, videos, and tables  


It is open source, and we also offer a free, easy-to-us
e API. It has built-in loaders for both r/llama_index and r/langchain.   


Hopefully, this is helpful. And if you've ex
perienced the problem, **consider contributing**! 🫡🔥 
```
---

     
 
all -  [ What's the most common way to do RAG these days? ](https://www.reddit.com/r/OpenAI/comments/1c5tc1n/whats_the_most_common_way_to_do_rag_these_days/) , 2024-04-17-0910
```
Hello friends!

I'm a coder. Very experienced with using GPT & Claude for LLM work, but have never dealt with more conte
nt that fits in a 128-200K context window until recently, so I have no experience with RAG.

**What're the most common &
 fastest to implement approaches?** I've used the new Assistants API and its the perfect level of easy to use, but its q
uite expensive in token use and not model-agnostic.

I see talk around LangChain and AutoGen for pipelines, Chroma and P
inecone for vector DBs...is there anything simpler? Something like the Assistants API, but more model agnostic. If not, 
what's the most common way to do this?

Thanks a ton r/OpenAI!
```
---

     
 
all -  [ what's the best way to pass dependencies into langchain tools? ](https://www.reddit.com/r/LangChain/comments/1c5slrj/whats_the_best_way_to_pass_dependencies_into/) , 2024-04-17-0910
```
Let's say I have a service I want to access inside a tool. Or I want to pass in a session ID or some session based state
 that I don't want to pass via the agent. 

I could obviously declare some things globally, but that isn't appropriate f
or everything. 

My first thought was wrapping tools in a class that contains their dependencies. I've tried different v
ariants of this, but seem to hit all kinds of issues. The documentation contains trivial use cases where we're passing b
asic types around, nothing more complex.

&#x200B;

What are people doing for tools which have more complex dependencies
? How are they injecting those into tools, in a langchain supported way, without making everything global?
```
---

     
 
all -  [ Langchain Interview. What things to prepare ](https://www.reddit.com/r/LangChain/comments/1c5r9qj/langchain_interview_what_things_to_prepare/) , 2024-04-17-0910
```
Hey Guys  
I have interview scheduled next week about Langchain. But I am not sure what will be asked? I wanted your inp
uts on what should I prepare.  


My background -  I have built multi-doc RAG. Technologies used - Langchain, Chroma, St
reamlit, [unstrctured.io](https://unstrctured.io)  


Please any help is appreciated  


Thanks

&#x200B;
```
---

     
 
all -  [ Knowledge Graph & RAG with Local LLM ](https://www.reddit.com/r/LocalLLaMA/comments/1c5o1z2/knowledge_graph_rag_with_local_llm/) , 2024-04-17-0910
```
Any insights on building a local LLM based RAG that uses a knowledge graph to query from? I read several examples from l
angchain & Llama\_index but it looks like they all need an open\_ai api call, and do not have provisions for a local llm

```
---

     
 
all -  [ Use 2 LLM, 1 for function calling and 1 for Contextual Response. ](https://www.reddit.com/r/LangChain/comments/1c5n0aw/use_2_llm_1_for_function_calling_and_1_for/) , 2024-04-17-0910
```
Hi, I am trying to develop an application that requires function calling and responding in everyday language based on th
e context of user input. I see in langchain we have [Ollama](https://js.langchain.com/docs/integrations/chat/ollama) and
 [Ollama functions](https://js.langchain.com/docs/integrations/chat/ollama_functions); I would like to use the Ollama Fu
nction first to check if the user needs to execute any function, then if not respond with regular Ollama, and if it does
, get the function data and pass it into Ollama and response usually.

How is this possible?
```
---

     
 
all -  [ Need architecture Help ](https://www.reddit.com/r/LangChain/comments/1c5mrr1/need_architecture_help/) , 2024-04-17-0910
```
Im trying building RAG LLM app for support analyst,my primary data is excel sheet with more than 6000 incidents(rows) wi
th columns [Descrietion, Pesolution, Work notes].
Description column explains Incident Description
Resolution column exp
lains resolution provided to that Incident
Work Notes column steps taken to solve incident.

User provides the new  inci
dent as prompt to the APP, expected functionality need to search similar incidents from data , then use that similar inc
ident to generate approx resolution.

Resources available uses
uses
Azure ai search (for vector search)
GPT 4

Should I 
clean data like,
1. Like  removing special characters 
2. Lowercase the all letters
letters
3.lemmatization 
4. Removing
 stop words like a , an 

My major doubt if I embed the description of each incident as one document , does similarity s
earch , take top k documents 

 What will K be? Will k be higher number or smaller number 

Or any idea other cluster si
milar incidents ?

```
---

     
 
all -  [ Early stopping method : generate ](https://www.reddit.com/r/LangChain/comments/1c5ljzo/early_stopping_method_generate/) , 2024-04-17-0910
```
Hi everyone, I must use old langchain method to generate an output:

    agent_executor = initialize_agent(
        tool
s,
        llm,
        agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
        max_execution_time=4,
        early_st
opping_method='generate',
        verbose=False,
        handle_parsing_errors=True,
        memory=memory,
    )

early
\_stopping\_method works well using 'generate' at the 4th iteration.  
  
If I use new method:

    agent = create_react
_agent(llm, tools, prompt)
    agent_executor = AgentExecutor(agent=agent,
                                   tools=tool
s,
                                   verbose=False,
                                   handle_parsing_errors=True,
    
                               early_stopping_method='generate',
                                   max_iterations=4)

I
t's like 'generate' is not implemented:

    '/python3.11/site-packages/langchain/agents/agent.py', line 127, in return_
stopped_response
        raise ValueError(
    ValueError: Got unsupported early_stopping_method `generate`

If I use 'f
orce' with and without max\_iterations:

    Agent stopped due to iteration limit or time limit.

The main issue is i'm 
using date\_time variable, so value change every second for others tools it works like a charm.

  
Has anyone solved th
is issue ? Or maybe myearly stopping method is outdated  
Thank you in advance
```
---

     
 
all -  [ Feedback wanted: LangChain documentation structure ](https://www.reddit.com/r/LangChain/comments/1c5l53d/feedback_wanted_langchain_documentation_structure/) , 2024-04-17-0910
```
Hey folks!

We're continuing to iterate on our documentation structure to make it easier to find relevant pages. We're w
ondering what people think of top-level 'tutorial', 'how to guides', 'conceptual guide' distinctions.

Page content is s
till WIP, but we were hoping to get feedback on **the structure** sooner rather than later.

I've linked the build we're
 iterating on below. Please let us know if you have any thoughts or reactions - do you think this would help you find th
e information you need more effectively?

[https://langchain-git-harrison-new-docs-langchain.vercel.app/docs/get\_starte
d/introduction](https://langchain-git-harrison-new-docs-langchain.vercel.app/docs/get_started/introduction)
```
---

     
 
all -  [ RAG Masterclass: Practical Insights from Ex-Meta Pioneers on April 18th ](https://lu.ma/cognita-rag) , 2024-04-17-0910
```

```
---

     
 
all -  [ Retriever gives an error ](https://www.reddit.com/r/LangChain/comments/1c5hzvh/retriever_gives_an_error/) , 2024-04-17-0910
```
Edit: This was solved by updating the langchain python package


This is my first time using langchain for QA on a csv f
ile. My steps were CSVLoader --> RecursiveCharacterTextSplitter --> Chroma Vectorstore 
When I searched for a keyword on
 the vectorstore with vectorstore.search('keyword', search-type='similarity'), a few documents were found. However, then
 I tried using a retriever with 
retriever=vectorstore.as_retriever(search_type='similarity'). 
If I search for the same
 keyword I used before with 
retriever.invoke('keyword'), I get the error 
AttributeError: 'NoneType' object has no attr
ibute 'get'
But I don't understand why, as it worked directly on the vectorstore.
```
---

     
 
all -  [ The Path to AGI: 12 Predictions for the Large Language Model Industry ](https://www.reddit.com/r/ChatGPT/comments/1c5fjaq/the_path_to_agi_12_predictions_for_the_large/) , 2024-04-17-0910
```
I do not believe in AGI (Artificial General Intelligence), because I do not believe that humanity was created to ultimat
ely create AGI that would lead to our own destruction. However, I do believe that the pursuit of AGI can lead to the dev
elopment of many technologies that will benefit humanity.

Over a year has passed since the introduction of ChatGPT, and
 it’s clear that the industry has reached deeper waters. Surface-level applications are gradually disappearing, giving w
ay to Agents. Just a year ago, spending $100 a month on OpenAI would have classified you as a major user; now, we’re ave
raging $1000 per day. Prompts are no longer about fitting a few templates by hand; instead, they are generated by a comp
lex mechanism. Our average Prompt is 20,000 tokens long, and an Agent can easily handle jobs that are several hundred th
ousand tokens, with the longer ones reaching up to 20 million tokens.

I recently read an article titled “[Interesting o
r Useful](https://new.qq.com/rain/a/20240404A07A0Q00),” which had a significant impact on me. It’s the best piece I’ve r
ead in the past six months that discusses the current AI landscape, and it resonated with me, perhaps because the author
 discussed the issues from an application perspective, which is closely related to my work developing Agents over the la
st half-year.

[Let's see who is still alive after a year](https://preview.redd.it/3l2lnxsx9uuc1.png?width=1080&format=p
ng&auto=webp&s=a8bd542dd07e44aa31af4068834623e67fc7fd8e)

Coupled with recent frequent communications with investors, I’
ve had some reflections that I’ve recorded for future contemplation.

# The Barrier of Models

Why address this issue fi
rst? After the release of Claude 3, we tested the migration cost and found that we could seamlessly switch an Agent from
 GPT-4 to Claude 3 without changing a single line of code or Prompt. This was quite shocking to me. In principle, the te
chnologies required for large models are public, and with the current development of the model industry, every company’s
 models are converging towards GPT-4, with some even surpassing it, such as Claude 3. Does this lead to the conclusion t
hat large models have no technological barriers, only engineering ones? That is, if the industry’s growth slows down, th
e differences between companies will quickly diminish or even disappear. This implies that the capabilities provided by 
large models are more like mobile operators, with almost zero cost for upper-layer migration. From this perspective, lar
ge models are not a good business. But can you really create a model that outperforms the current commercial models or c
osts less than the existing open-source models? Ultimately, large models are bound to be a business with high capital an
d policy barriers.

There are many rumors currently suggesting that GPT-5 will have built-in Agent capabilities. I boldl
y speculate that this statement is half correct:

**Speculation 1: OpenAI will definitely provide System 2 capabilities,
 that is, Agent capabilities.**

Given that the current Chat interface is stateless and too simplistic, which is not con
ducive to the development of complex Agents in upper-layer applications nor to the building of a moat for OpenAI, it is 
certain that OpenAI will provide stateful interfaces, such as a Plan interface, to deeply integrate the model with appli
cations.

**Speculation 2: The System 2 capabilities provided by OpenAI will be B2B-oriented, and won’t delve into Agent
s for specific scenarios.**

Every specific scene involves industry know-how and private data, which for OpenAI is akin 
to guerrilla warfare, and is pointless. They only need to capture the largest scenario, transitioning from personal supe
r assistant ChatGPT to ChatAgent.

**Speculation 3: There are no so-called vertical models.**

I firmly believe that int
elligence is universal, and the only way to achieve it is through the scaling law. Practical results show that smaller m
odels are simply not as smart as larger ones. Currently, only GPT-4 and Claude 3 are capable of satisfying super complex
 reasoning scenarios like those required by a Babel Agent. OpenAI’s abandonment of the large coding model CodeX is very 
telling. Thus, I think that training a vertical large model is most likely a fool’s errand, regardless of the field. How
ever, Fine-Tuning (FT) may persist in the long term.

&#x200B;

https://preview.redd.it/xa2zl6i6auuc1.png?width=1080&for
mat=png&auto=webp&s=b85a6d2c1aeef20e09c55b0c3c40a7479c8622ee

# The Value of Infra

There are two types of infrastructur
es in the field of AI: one type supports the construction of large models, and the other supports the construction of ap
plications for large models (such as Agents). Let’s discuss these separately, starting with the infrastructure for train
ing and inference of large models.

**Speculation 4: The significant value of energy/data centers**

Recently, a news st
ory reported that a joint team from Microsoft and OpenAI caused a citywide power outage due to their GPU data center ope
rations. Regardless of how much truth there is to this story, it at least indicates that energy is a crucial strategic r
esource in the age of AI. Therefore, any infrastructure that can provide value in terms of energy is extremely valuable.
 Data centers may be worth much more than many people think.

**Speculation 5: A diverse range of data-related products.
**

Whether working on underlying models or higher-level applications, data is the core value. However, the publicly ava
ilable data on the internet has largely been exhausted. A significant amount of new data is AI/artificially generated, a
nd data naturally has characteristics such as modality and industry specificity, making it impossible to have a one-size
-fits-all data annotation service. Moreover, as training data volumes increase, new challenges arise in how to store, tr
ansport, and analyze the data.

**Speculation 6: Convergence in the LLMOps market**

Ultimately, only a few companies ar
e working on underlying models, and these companies generally have their own set of tools and pipelines, which are part 
of their competitive edge. Therefore, there is no market for a standardized LLMOps product. Additionally, there is no re
ason why open-source models would not develop an infrastructure similar to Kubernetes (K8S), which would benefit everyon
e in the industry. However, such infrastructure is typically the domain of large corporations.

Now let’s discuss the in
frastructure for developing large model applications.

The most well-known player in this field is Langchain, which got 
an early start and quickly accumulated a user base by leveraging cognitive gaps, then snowballed from there to success. 
However, as application development has progressed, the landscape in this area has become relatively clear.

**Speculati
on 7: Tools that simplify the development of large model applications will, over time, fall out of favor.**

Whenever a 
new technology emerges, most people are initially in the dark, creating a demand for low-code products that can accelera
te developers’ understanding of new concepts. However, from the PC era to the internet and mobile internet era, these dr
ag-and-drop products have never really captured a large market. Another sign is that more and more model APIs are aligni
ng with OpenAI, even directly using OpenAI’s SDK, which has made products that simplified API calls redundant. OpenAI’s 
own GPT products are an extreme example of this type of tool. Currently, the state of these is clear for all to see. As 
an application development team, we have virtually no need for such tools. Langchain is already moving into deeper water
s, not to reduce the threshold for application development, but to assist in the development of complex applications.

*
*Speculation 8: It’s too early for Agent frameworks.**

Since the advent of AutoGPT, various frameworks have emerged to 
“teach people how to make Agents.” During the development of Babel Agent, we carefully evaluated almost all the framewor
ks on the market and ended up not adopting any of them. The reason is that the deeper you go, the less they meet your ne
eds. Normally, frameworks are abstracted from mature applications, but now there isn’t even a single mature Agent applic
ation, which seems like putting the cart before the horse. I believe there will eventually be an Agent framework, but it
 is very likely not to come from any of the current framework-building teams, and as mentioned earlier, there’s a possib
ility that large models will come with their own Agent development frameworks.

**Speculation 9: AgentOps is a blue ocea
n.**

Here, AgentOps specifically refers to the observation aspect, or more accurately, Agent APM (Application Performan
ce Management). As previously mentioned, I don’t believe there is a unified approach to Agent development at present, bu
t observation is possible. A Babel Agent job can involve dozens of consecutive calls to large models, each involving ten
s of thousands of tokens, with a hierarchical call structure. Without observation tools, trying to analyze logs with the
 naked eye would quickly lead to blindness — this is a real and pressing need. However, perhaps I’m out of the loop, but
 it seems that only LangSmith is seriously working on this. I think this is the most valuable product that the LangChain
 team currently offers.

# Application Trends

Looking ahead 10 years, shouldn’t the biggest market brought about by the
 large model revolution appear at the application layer?

**Speculation 10: All Applications Become Agents.**

The most 
fundamental value of the intelligence produced by large models is their partial substitution for human intelligence. If 
applications cannot solve problems the way humans do, their value will be extremely limited. As we have seen in the past
 year, there is much excitement within the industry, but outside of it, there’s hardly any awareness. Therefore, I boldl
y speculate that a great many agents will emerge in both interesting and useful directions, which will allow the general
 public to feel the value of AI.

**Speculation 11: The Core Barrier for Agents Comes from Data.**

If one must speak of
 a secret recipe for a barrier in application development, it would be data. This includes proprietary industry data, in
dustry know-how, SOPs, synthetic data, and so on. Whether it’s RAG or FT, it’s data that makes the model perform differe
ntly. Currently, other engineering differences are not clear and are likely to be leveled by industry development. Howev
er, how long this leveling process will take, and what new barriers might develop during this process, remains unknown.


**Speculation 12: General Consumer-Facing Agents Have No Entrepreneurial Opportunity.**

Any application that overlaps 
with ChatGPT scenarios, including those that are surface-level applications, have no room for survival, not to mention c
ompanies like Apple that have yet to enter the field, controlling physical world gateways. The biggest trap for these ki
nds of applications is that they may see growth in the early stages, but in reality, they are just finding Product-Marke
t Fit (PMF) for larger companies. This has happened many times in history, and we can learn from it without further elab
oration.  
Finally, to prove that the above analysis was indeed made after practical thinking, here is a demonstration v
ideo of Babel Agent, showing how to build a question-and-answer application with a search function, similar to Perplexit
y:

&#x200B;

https://reddit.com/link/1c5fjaq/video/jkzm44qfauuc1/player

We believe AI Developers can take over complex
, long-cycle tasks from humans. As mentioned at the beginning, I do not believe in AGI, but I do believe in ACI, Artific
ial Conditional Intelligence. Agents are the embodiment of ACI, and time will tell.
```
---

     
 
all -  [ How to replicate Command R like Citations ](https://www.reddit.com/r/LocalLLaMA/comments/1c5e97e/how_to_replicate_command_r_like_citations/) , 2024-04-17-0910
```
Hi all,

does anyone know what's the best way to replicate Cohere's Command R functionality of returning Citation snippe
ts from the context supplied? (See [Cohere docs](https://docs.cohere.com/docs/documents-and-citations)).

I would love t
o replicate the functionality when using local LLMs with a more permissive License than Command R (+). 

I know that lan
gchain has some functionality around citations and verbatim quotes. But trying it with 7B parameter models like Mistral,
 this didn't always work. The ideal scenario would be feeding the LLM context documents that are a couple of sentences l
ong, and getting the verbatim citation coupled with the answer from the LLM.

Does this require finetuning a model? Or w
hat's the best way to approach this problem?

&#x200B;
```
---

     
 
all -  [ Can you organize data into a csv with langchain? ](https://www.reddit.com/r/LangChain/comments/1c5e0ok/can_you_organize_data_into_a_csv_with_langchain/) , 2024-04-17-0910
```
Hello, im new to all of this but i have retreived contact info from paper with a OCR into a .txt file but due to the OCR
 being inaccurate its all unorganised and stuff. Is it possbile to use Langchain to organise this data and make it more 
accurate (the 'i' is often replaced with 'l') in a csv?
```
---

     
 
all -  [ Multi Agent Interview Panel using LangGraph and LangChain  ](https://www.reddit.com/r/ArtificialInteligence/comments/1c5ctv0/multi_agent_interview_panel_using_langgraph_and/) , 2024-04-17-0910
```
Check out this demo on how I developed a Multi-Agent system to first generate an Interview panel given job role and than
 these interviewers interview the candidate one by one (sequentially) , give feedback and eventually all the feedbacks a
re combined to select the candidate. Find the code explanations & demo for automated interview for Junior Product Manage
r here : https://youtu.be/or36qevjxGE?si=cM1LMhe5J_hnpyFO
```
---

     
 
all -  [ Multi-Modal Rag using LLaVa ](https://www.reddit.com/r/LocalLLaMA/comments/1c5c7wu/multimodal_rag_using_llava/) , 2024-04-17-0910
```
Hey there, 

I'm currently implementing a multi-modal RAG sys leveraging, LLaVa, Chroma & Langchain. 

However, I'm havi
ng a hard time finding the embeddings function llava uses. Can anybody help me with that? Am I just blind?  


Any point
ers on how to narrow that down would be much appreciated. 

Thanks in advance!
```
---

     
 
all -  [ Looking for LLM application templates for travel itinerary maker with web search and prompt memory ](https://www.reddit.com/r/LLMDevs/comments/1c4zo1n/looking_for_llm_application_templates_for_travel/) , 2024-04-17-0910
```
I'm interested in developing an LLM application for generating travel itineraries that incorporates web search capabilit
ies and the ability to remember and build upon previous prompts, similar to ChatGPT's conversation memory.

From my init
ial research, it seems like Langchain's AutoGPT library could be a good fit, as it enables LLMs to autonomously interact
 with other tools and databases. However, I'm not certain if this is the optimal approach.

Are there any existing open-
source application templates, starter codebases, or tutorials that would be recommended for this type of project? Ideall
y I'm looking for something that demonstrates best practices for prompt engineering, web search integration, and persist
ent memory across conversations.

Any guidance or examples from those with experience building similar applications woul
d be much appreciated. Links to relevant Github repos, papers, or technical guides would also be very helpful.
```
---

     
 
all -  [ Any Suggestions for idea to built a RAG chatbot in a Hackathon? ](https://www.reddit.com/r/LangChain/comments/1c4t5ks/any_suggestions_for_idea_to_built_a_rag_chatbot/) , 2024-04-17-0910
```
So guys
My team has participated in a hackathon and we require Ideas to built a RAG chatbot on.
Your suggestions might h
elp us alot….Thanks

```
---

     
 
all -  [ Burr: an OS framework for building and debugging AI apps faster (manage memory, persist state, monit ](https://www.reddit.com/r/LangChain/comments/1c4ssou/burr_an_os_framework_for_building_and_debugging/) , 2024-04-17-0910
```
[https://github.com/dagworks-inc/burr](https://github.com/dagworks-inc/burr)

**TL;DR** We created Burr to make it easie
r to build and debug AI applications that carry state/make complex decisions. It is similar in concept to Langgraph, and
 works with any framework you want (Langchain, etc...). It comes with OS telemetry. We're looking for users, contributor
s, and feedback.

**The problem(s):** A lot of tools in the LLM space (DSPY, superagents, etc...) end up burying what yo
u actually want to see behind a layer of complexity and prompt manipulation. While making applications that make decisio
ns naturally requires complexity, we wanted to make it easier to logically model, view telemetry, manage state, etc... w
hile not imposing any restrictions on what you can do or how to interact with LLM APIs. 

**We built Burr** to solve the
se problems. With Burr, you represent your application as a state machine of python functions/objects and specify transi
tions/state manipulation between them. We designed it with the following capabilities in mind:

1. Manage application me
mory: Burr's state abstraction allows you to prune memory/feed it to your LLM (in whatever way you want)
2. Persist/relo
ad state: Burr allows you to load from any point in an application's run so you can debug/restart from failure
3. Monito
r application decisions: Burr comes with a telemetry UI that you can use to debug your app in real-time
4. Integrate wit
h your favorite tooling: Burr is just stitching together python primitives -- classes + functions, so you can write what
ever you want. Use langchain and dive into the OpenAI/other APIs when you need.
5. Gather eval data: Burr has logging ca
pabilities to ensure you capture data for fine-tuning/eval

It is meant to be a lightweight python library (zero depende
ncies), with a host of plugins. You can get started by running: `pip install 'burr[start]' && burr` \-- this will start 
the telemetry server with a few demos (click on *demos* to play with a chatbot + watch telemetry at the same time).

The
n, check out the following resources:

1. [Burr's documentation/getting started](https://burr.dagworks.io/getting_starte
d/)
2. [Multi-agent-collaboration example using LCEL](https://github.com/DAGWorks-Inc/burr/tree/main/examples/multi-agen
t-collaboration/lcel)
3. [Fairly complex control-flow example that uses AI + human feedback to draft an email](https://g
ithub.com/DAGWorks-Inc/burr/tree/main/examples/web-server)

**We're really excited** about the initial reception and are
 hoping to get more feedback/OS users/contributors -- feel free to DM me or comment here if you have any questions, and 
happy developing!

PS -- the name *Burr* is a play on the project we OSed called [Hamilton](https://github.com/dagworks-
inc/hamilton) that you may be familiar with. They actually work nicely together!

&#x200B;

&#x200B;
```
---

     
 
all -  [ Courses/books to get into Generative AI (GenAI)? Looking to get familiar with tools like Langchain,  ](https://www.reddit.com/r/LangChain/comments/1c4s19w/coursesbooks_to_get_into_generative_ai_genai/) , 2024-04-17-0910
```
Anyone has any recommendation for course/book/tutorial, free or paid? I have a decent idea about deep learning concepts.
 But, my current job is in backend with python, so naturally looking to expand my skillset! Thanks.   


I just want eno
ugh to get a custom chatbot with guardrails up and running on my system. I tried with ollama but am stuck at generating 
embedding for my dataset 
```
---

     
 
all -  [ Adding metadata to chunks ](https://www.reddit.com/r/LangChain/comments/1c4rvge/adding_metadata_to_chunks/) , 2024-04-17-0910
```
Is there any tutorials of a way to define metadata data to specific chunks to better compare documents so that there is 
less contamination with RAG
```
---

     
 
all -  [ Courses/books to get into Generative AI (GenAI)? Looking to get familiar with tools like Langchain,  ](https://www.reddit.com/r/developersIndia/comments/1c4rsz0/coursesbooks_to_get_into_generative_ai_genai/) , 2024-04-17-0910
```
Anyone has any recommendation for course/book/tutorial, free or paid? I have a decent idea about deep learning concepts.
 But, my current job is in backend with python, so naturally looking to expand my skillset! Thanks.
```
---

     
 
all -  [ [For Hire] Programmer/Web Developer/IT Consultant (Python, PHP, AI, etc.) ](https://www.reddit.com/r/forhire/comments/1c4qchs/for_hire_programmerweb_developerit_consultant/) , 2024-04-17-0910
```
To get in contact, please message me, I don't use the chat thing and might miss you or reply very late. Then we can swit
ch to email/discord/telegram or whatever else. Apologies for starting with this, but many missed it when it was lower.


I'm a programmer/web developer with 14 years of professional experience. I am available for all sorts of programming and
 web development tasks.

I also offer consulting services. If you need something done, but don't know how exactly, I can
 help. I'm an excellent researcher and I communicate well. I will work with you to find the best solution for your probl
em.

My services include, but are not limited to:

* websites

* desktop applications

* AI integration (chatGPT API, la
ngchain, whatever else turns up)

* integration with APIs and other webservices

* all kinds of scripts

* task automati
on

* website optimization

* debugging

* plugins for existing software

* bots (Reddit, Telegram, etc)

* code audits


If you're looking for someone to take care of a variety of different tasks, I can offer continuous support.

My preferr
ed environment is Python with Django, but I work with anything Python or PHP based. I have no problem with learning new 
technologies that are needed for the project.

Rate is $50/h.

Portfolio:

https://bdabkowski.yum.pl

Satisfied customer
s:

https://www.reddit.com/r/testimonials/comments/2e8gqy/pos_uqui_need_a_backend_web_dev_look_no_further/

https://www.
reddit.com/r/testimonials/comments/7fsdze/pos_hiring_uqui_was_an_example_of_how_it_should/

https://www.reddit.com/r/tes
timonials/comments/80pu9l/pos_uqui_great_work_detailed_and_fast/

https://www.reddit.com/r/testimonials/comments/b0nx68/
uqui_is_a_hardworking_intelligent_honest_apps/

https://www.reddit.com/r/testimonials/comments/j3mz3p/uqui_is_a_great_we
b_development_consultant_with/

https://www.reddit.com/r/testimonials/comments/v40ay3/pos_uqui_is_a_great_backend_dev_to
_work_with/

Please note: I am not a designer. To make it clear, it means zero aesthetic sense.
```
---

     
 
all -  [ setting up an idiot proof sandbox for students on a cluster. ](https://www.reddit.com/r/LocalLLaMA/comments/1c4p5fl/setting_up_an_idiot_proof_sandbox_for_students_on/) , 2024-04-17-0910
```
I'll be teaching text analysis using LLMs to a class. This will be complex forms of entity recognition and some rag (e.g
. find the metaphors in a text, identify possible connotations). Rather than have them find trivial entities in lots of 
data, I will have them looking at very small chunks of text and seeing how things like chaning prompts/llms/parameters e
ffects results. This gives them an idea of how things do/don't work in detail...which seems a responsible foundation bef
ore they run off and try to do topic modelling on 1500 policy document crap PDFs in 15 languages (no kidding).

For a bu
nch of reasons we will be using local installs rather than cloud APIs. I will start them on their own laptops with openw
ebui/ollama stacks with v small models so they can see how things work for simple tasks. I want them to see larger model
s (mixtral 8x22, command-r) since those are required for some of the more complex entities. Those will be hosted on a cl
uster that has a bunch of resources. 

what is the best way to install for that cluster so that I can manage it and the 
admin folks won't freak out? It is a pretty typical setup with a mitt full of a100s. 

they don't want to give me root (
go figure), they don't like gradio or cloudflared etc., they can be convinced to open a port for use internal to the uni
.

so far the best option I can see, for ease of use and the likelihood that the hardware will shift under the install b
etween runs, is the binary of ollama on the cluster, a port open to the uni and something like [bionicgpt](https://githu
b.com/bionic-gpt/bionic-gpt) for remote management.

my concern is that I'm not sure how well that will support

1. stud
ent first contact using openwebui (for those who think python is a snake) when a handful of students are constantly chan
ging which model is being used.
2. student exploration using something like langflow (sweet cause it says it does not re
quire python and makes langchain somewhat approachable, not so sweet because it actually does require understanding to r
eally make it work the minute you do something interesting)...this one stumps me cause it can call ollama or llamacpp fo
r both embedding and prompt handling and I don't know if/how it handles switching the model active in the back end
3. st
udent thrashing, using setups like [crew.ai](https://crew.ai)

my concerns, right now, are how do back ends like ollama 
handle multiple clients? how do they handles switching between models. what do they do when they are called by the same 
flow for embedding (one model) and then querying (another model) etc.

if anybody has experience with setting up such a 
fun but somewhat idiot proof sandbox, I'd be pleased to hear.

thank you
```
---

     
 
all -  [ Calender Management system using LlamaIndex or Langchain ](https://www.reddit.com/r/LangChain/comments/1c4nsa5/calender_management_system_using_llamaindex_or/) , 2024-04-17-0910
```
Calendar Integration for Deadline Management: Develop a feature that
enables the system to interact with a user's calend
ar to manage tasks and
deadlines efficiently. The system should be capable of adding tasks, setting
reminders, and intel
ligently scheduling activities without conflicts. Implement an
intelligent scheduling feature that, upon receiving a tas
k addition command, first
queries the user's calendar for existing commitments. It should analyse the
calendar to identi
fy time slots, check for conflicts, and evaluate deadline
proximity to schedule tasks optimally. This requires integrati
on with calendar
APIs, parsing date and time information, and applying logic to decide the most
appropriate timing for n
ew tasks.

I need to implement above task and develop a natural language interface which can access calender and can sch
edule appointments, delete them and make priority list. I need to implement this with all RAG capabilities (I thought of
 llamaindex or Langchain). 
I have LLM Api key which has only 3000 request limitation, model information 
meta.llama2-70
b-chat-v1. For frontend I can use streamlit. How can I use Langchain or llamaindex for this management system. If there 
are resources which can help me implementing it please do share.

```
---

     
 
all -  [ Your Experience: Best Chunking Technique for complex PDFs ](https://www.reddit.com/r/LangChain/comments/1c4nizz/your_experience_best_chunking_technique_for/) , 2024-04-17-0910
```
Hi,

I am experimenting with different chunking techniques like RecursiveCharacterSplitter or [Unstructured.IO](https://
Unstructured.IO) chunking with 'by\_title'. Theoretically I think the second option to chunk by title will be the most p
romising one.

But I would be interested of your experiences? The PDFs I am using are all complex and many come with a c
ompletely different structure, so manually checking for every PDF is no choice. 

Happy to discuss with your experiences
!
```
---

     
 
all -  [ Are you hungry for tech meetups? Join us for Cloud Native Lisbon Meetup #14 on April 18th in Lisbon! ](https://www.reddit.com/r/devpt/comments/1c4mxpk/are_you_hungry_for_tech_meetups_join_us_for_cloud/) , 2024-04-17-0910
```
📢 Cloud Native fans, **we're back!** ☁️  
Register link here: [https://www.meetup.com/cloudnativelx/events/300325033/](h
ttps://www.meetup.com/cloudnativelx/events/300325033/) 🔗  


**On the agenda:**  


🎤 '*Deploy LangChain applications on
 AWS with LangServe*' ️by [João Galego](https://www.linkedin.com/in/ACoAAAUp-sQBFZ55uKVqPbQV7WNOA1YRQW831JI), Solutions 
Architect at AWS  


🎤 '*Kubernetes management the GitOps way: Manage Cloud Native apps with ArgoCD*' by [Jake Page](htt
ps://www.linkedin.com/in/ACoAAAiXf7AB2jiUx6LpOC0J89kvrZeqLdtS6mo), Developer Relations Engineer at Glasskube  


Plus th
e usual networking, snacks, and drinks. 🍻🍕  


🗓️ April 18th  
⏰ 18:30  
📍[grow.inc SPACES](https://www.linkedin.com/com
pany/growinc-spaces/) Lisbon.  


https://preview.redd.it/v44hs1b8gnuc1.png?width=669&format=png&auto=webp&s=542e70649bc
e118102f8e3897af27fa61d6fd1f0
```
---

     
 
all -  [ [Feedback] Launch your SaaS in days and not weeks ](https://www.reddit.com/r/microsaas/comments/1c4k95g/feedback_launch_your_saas_in_days_and_not_weeks/) , 2024-04-17-0910
```
Last month I have been spending time in building a solution to help founders launch their SaaS MVP without knowing the i
ntricate tech details and having to start from scratch. The idea was can founders quickly iterate over their MVP without
 rebuilding everything from scratch.

Founders can start from scratch and add features as they grow / need basis. They c
an skip features that they don't want.

I am seeking 10 people to try out free of cost in return for feedback. Let me kn
ow in comments if interested and I will share with you.

Features:

1. Social logins (Google OAuth)
2. Admin panel
3. St
ripe / Paypal integration
4. SEO / Blog / Newsletter support
5. MongoDB / Supabase
6. Email support (Mailgun)
7. Tailwin
d CSS
8. AI ready: Langchain & GPT wrapper
```
---

     
 
all -  [ RAG and LangChain Source code ](https://www.reddit.com/r/LangChain/comments/1c4jl1c/rag_and_langchain_source_code/) , 2024-04-17-0910
```
I often heard that there are problems with navigating through LangChain and that working with the source code directly b
rings most benefits which is very hard work though. I thought it makes sense to maybe fine tune a model on the code and 
use RAG to interact with the source code and understand it better. Any feedback on whether this is a good idea or even p
ossible? The source code might be around 5 million tokens all in all. 
```
---

     
 
all -  [ Any tips on how to build a RAG model for csv using LlamaIndex? ](https://www.reddit.com/r/LocalLLaMA/comments/1c4iz3d/any_tips_on_how_to_build_a_rag_model_for_csv/) , 2024-04-17-0910
```
i'm building a rag model for csv files and i'm choosing models for the generation part that can also perform calculation
s - like i

Prompt: 'What are the  total sales in year 2023? ' 

by calculating the sum of monthly sales which is presen
t in the csv file and answer 

Answer: 'The total sales in year 2023 is XXXX'

But the major setback I'm facing is the m
odel cant calculate for the responses and the answers are pretty bad, so I appreciate any materials or articles that may
 help my use case.

Already created a small rag model for pdf files, since it is a text based use case I had no issues b
uilding it. But for the csv files the datatypes are important and numerical data needed to perform calculations like the
 above mentioned

So I appreciate any kind of help based on this topic, since I can't find any materials for LLamaIndex 
framework. For the time being I'm gonna look into Langchain examples and try to replicate the same using LlamaIndex 
```
---

     
 
all -  [ [Feedback] Ship your SaaS in days and not weeks ](https://www.reddit.com/r/SideProject/comments/1c4imw3/feedback_ship_your_saas_in_days_and_not_weeks/) , 2024-04-17-0910
```
Last month I have been spending time in building a solution to help founders launch their SaaS MVP without knowing the i
ntricate tech details and having to start from scratch. The idea was can founders quickly iterate over their MVP without
 rebuilding everything from scratch.

Founders can start from scratch and add features as they grow / need basis. They c
an skip features that they don't want. 

I am seeking 10 people to try out  free of cost in return for feedback. Let me 
know in comments if interested and I will share with you. 

Features:  
1. Social logins (Google OAuth)  
2. Admin panel
  
3. Stripe / Paypal integration  
4. SEO / Blog / Newsletter support  
5. MongoDB / Supabase  
6. Email support (Mailg
un)  
7. Tailwind CSS  
8. AI ready: Langchain & GPT wrapper  


&#x200B;

&#x200B;
```
---

     
 
all -  [ What are the best SQL agents ](https://www.reddit.com/r/LangChain/comments/1c4ij67/what_are_the_best_sql_agents/) , 2024-04-17-0910
```
We've been trying pandas dataframe agent and have been experiencing some problems in productions. Are there better alter
natives?
```
---

     
 
all -  [ Starting Out: Key Vespa Docs for Hybrid Search (Keyword + Vector) ](https://www.reddit.com/r/vespa_ai/comments/1c4i4bw/starting_out_key_vespa_docs_for_hybrid_search/) , 2024-04-17-0910
```
a common project is to do hybrid search (keyword + vector) over your own text documents.

there isn't a single dummy's g
uide on how to do it. langchain has an integration with pyvespa, but i haven't tried it.

pyvespa is vespa's python libr
ary, which is designed for prototyping. it does not have the full functionality, but should be enough for a small person
al project.

if you aren't using langchain, you will have to figure out how to run vespa from various pages in their doc
s.

the key ones i found useful when i was starting out were the following:

[https://docs.vespa.ai/en/vespa-quick-start
.html](https://docs.vespa.ai/en/vespa-quick-start.html) (starting a vespa instance on docker)

[https://docs.vespa.ai/en
/tutorials/text-search.html](https://docs.vespa.ai/en/tutorials/text-search.html) (keyword search)

[https://docs.vespa.
ai/en/tutorials/text-search-semantic.html](https://docs.vespa.ai/en/tutorials/text-search-semantic.html) (vector search,
 partial explanation)

[https://pyvespa.readthedocs.io/en/latest/getting-started-pyvespa.html](https://pyvespa.readthedo
cs.io/en/latest/getting-started-pyvespa.html) (hybrid search, with pyvespa)

to set up and run vespa, you can either:

*
 use pyvespa; or
* write the schema and services (query profile, optional) files yourself from scratch. for example, the
se define the fields, data types, relevance scoring, etc.

i haven't used langchain, but langchain probably provides for
 data ingestion.

otherwise, you will have to write code yourself for preparing the data to be fed into vespa. the data 
and vectors need to be in json or jsonl with a particular format.
```
---

     
 
all -  [ I have a nosql database of profiles where each profile has multiple json documents, how can I create ](https://www.reddit.com/r/LangChain/comments/1c4hc9j/i_have_a_nosql_database_of_profiles_where_each/) , 2024-04-17-0910
```
I know how to create RAG for sql databases, pdfs, and other text documents, the nosql thing is a bit confusing to me so 
any assistance is appreciated!
```
---

     
 
all -  [ Need Help - Trying To Create A Chatbot That Recommends Personalized Video Games ](https://www.reddit.com/r/learnpython/comments/1c4h188/need_help_trying_to_create_a_chatbot_that/) , 2024-04-17-0910
```
Hello everyone! Before I start discussing about my project, I want to apologize in advance for any naive questions or in
correct use of terms, as I'm new to the field of machine learning and chatbots.

Now, onto my question: I'm attempting t
o create a web app using React and Python (Flask) that integrates a chatbot designed to recommend personalized video gam
es to users based on their queries. To elaborate, users will either talk about their all-time favorite video games, the 
genres/tags they are fond of, or provide a short description of their demographic profile (e.g., based on age and gender
 - the chatbot will go on to recommend the user video games from different genres that it thinks he/she will enjoy. Ther
e are some studies on the correlation between video games genres and gender/age of a person. I'm thinking of feeding my 
chatbot this kind of data from these sources, if possible).  Once the chatbot understands the query, it will make a call
 to an external API of a video game database to retrieve games that match the criteria. 

So to reiterate, what I'm tryi
ng to do is to create a chatbot that understands user input, and based on the context extracted from that input, make ca
lls to the external video games database API (such as RAWG), or to the knowledge base then to the external API, and fetc
h the suitable types of games that the chatbot see suitable to recommend.

One framework I've seen capable of perhaps ac
hieving this, using JS and Python, is LangChain. Is it possible to accomplish all of this using LangChain? And is LangCh
ain the right way to achieve this? If yes, how should I approach this? What factors should I consider while trying to im
plement my chatbot? What advice do you have for a beginner like me? Is there any other information I should add to my po
st? Or if not, what other APIs or frameworks can you recommend me looking into and eventually use?

Thank you a lot to e
veryone who took their time to read this and help me out!
```
---

     
 
all -  [ Render charts? ](https://www.reddit.com/r/LangChain/comments/1c4gy1a/render_charts/) , 2024-04-17-0910
```
I’m working on a chat-style bot and need to be able to display charts for trends etc. Any tips for going about this?
```
---

     
 
all -  [ Multi-Agent Movie scripting using LangGraph  ](https://www.reddit.com/r/LangChain/comments/1c4b665/multiagent_movie_scripting_using_langgraph/) , 2024-04-17-0910
```
Checkout this tutorial on how to generate movie scripts using Multi-Agent Orchestration where the user inputs the movie 
scene, LLM creates which agents to create and then these agents follo the scene description to say dialogues. https://yo
utu.be/Vry2-h81_I0?si=0KknmT8CfAhTucht
```
---

     
 
MachineLearning -  [ [D] How to get the source documents from the retrieved context for RAG?  ](https://www.reddit.com/r/MachineLearning/comments/1bvoc1t/d_how_to_get_the_source_documents_from_the/) , 2024-04-17-0910
```
I'm not using Lanchain but only making API calls to an LLM service provider. The retriever is connected to a vector DB, 
and I would like to know what the LLM refers to WITHIN that retrieved context whenever it provides an answer, similar to
 how return_source_documents works in Langchain.

I'm using AzureOpenAI. I couldn't find much in their docs that related
 to returning the source documents. Any help will be greatly appreciated!

```
---

     
 
MachineLearning -  [ [P] RAG pipeline to query the ML Engineering Open Book ](https://www.reddit.com/r/MachineLearning/comments/1bu4wyx/p_rag_pipeline_to_query_the_ml_engineering_open/) , 2024-04-17-0910
```
I built a quick RAG implementation using Langchain to make it easy to query the [ML Engineering Open Book](https://githu
b.com/stas00/ml-engineering) by [Stas Bekman](https://twitter.com/StasBekman). The Multi-Vector retriever gave pretty go
od results and was quite easy to set up too. 

Github link - [https://github.com/shreyansh26/RAG-ML-Engg-Open-Book](http
s://github.com/shreyansh26/RAG-ML-Engg-Open-Book)

Hope this is useful for folks!
```
---

     
 
MachineLearning -  [ [Project] FinancialAdvisorGPT : LLM+RAG Boilerplate Project ](https://www.reddit.com/r/MachineLearning/comments/1btlpgd/project_financialadvisorgpt_llmrag_boilerplate/) , 2024-04-17-0910
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

     
 
MachineLearning -  [ [Project] Picachain, image search made simple. ](https://www.reddit.com/r/MachineLearning/comments/1bt7epv/project_picachain_image_search_made_simple/) , 2024-04-17-0910
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

     
 
deeplearning -  [ Tengyu Ma on Voyage AI - Weaviate Podcast #91! ](https://www.reddit.com/r/deeplearning/comments/1bjft8i/tengyu_ma_on_voyage_ai_weaviate_podcast_91/) , 2024-04-17-0910
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

     
