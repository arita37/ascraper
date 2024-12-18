 
all -  [ [Project] Video Foundation Model as an API ](https://www.reddit.com/r/LangChain/comments/1hgm2df/project_video_foundation_model_as_an_api/) , 2024-12-18-0913
```
Hey everybody! My team and I have been working on a foundational video language model (viFM) as-a-service we're excited 
to do our first release!

tl;dw is an API for video foundational models (viFMs) and provides video understanding. It hel
ps developers build apps powered by an AI that can watch and understand videos just like a human. 

  
Only search is av
ailable right now but these are all the features that will be releasing over the next few weeks:

* Semantic video searc
h: Use plain English to find specific moments in single or multiple videos
* Classification: Identify context-based acti
ons or behaviors
* Labeling: Add metadata or label every event
* Scene splitting: Automatically split videos into scenes
 based on what you’re looking for
* Video-to-text: Get text description of what is happening in the clip or video

  
Wh
at can you build with tl;dw?

* an AI agent that can recommend videos based on your preferences
* the internal media dis
covery platform [Netflix](https://netflixtechblog.com/building-a-media-understanding-platform-for-ml-innovations-9bef996
2dcb7) has
* smart home security camera like the demo we have [here](https://trytldw.ai/security_demo)
* find usable sho
ts if you’re producing a video
* automatically add metadata to videos or scenes

Any feedback is appreciated! Is there s
omething you’d like to see? Do you think this API is useful? How would you use it, etc. Happy to answer any questions as
 well.

[Register and get an API key](https://trytldw.ai/register): [https://trytldw.ai/register:](https://trytldw.ai/re
gister:)

[Follow the quick start guide to understand the basics.](https://docs.trytldw.ai/intro)

[Documentation can be
 viewed here](https://docs.trytldw.ai/)

Demos + tutorials coming soon.

Happy to answer any questions!
```
---

     
 
all -  [ [Project] I built an AI Parliament simulator that lets virtual representatives debate and vote on po ](/r/OpenAI/comments/1hgbxxp/project_i_built_an_ai_parliament_simulator_that/) , 2024-12-18-0913
```

```
---

     
 
all -  [ Need help with recovering conversations from checkpoint store ](https://www.reddit.com/r/LangChain/comments/1hgkbt5/need_help_with_recovering_conversations_from/) , 2024-12-18-0913
```
So I tried out the MongoDB checkpointer implementation from [here](https://langchain-ai.github.io/langgraph/how-tos/pers
istence_mongodb/), and while it does work great out of the box for storing graph state, I am running into some problems 
when trying to use it as a conversation store. Apparently, every time the state of the graph changes, a new checkpoint i
s written to the database  which contains all the messages in all the previous checkpoints, which I assume is implemente
d this way in order to enable time travelling. My question is first of all, is there a way to disable this or tune it in
 a way such that I store one document per conversation (thread\_id) in my db, which keeps updating instead of writing a 
new checkpoint every time. ( I assuming there is no way to do this currently, just want to know why  ) Secondly, is usin
g persistent DB checkpointers event a good way to store conversations? Or do people generally implement their own stores
? Let us say I wish to store multiple conversations and want to pull a single a conversation by given thread\_id. Someth
ing like storing the `created_at` attribute in the metadata, then sorting in descending order and picking the first chec
kpoint would work, but at this point I feel like I'm unnecessarily complicating stuff and should just go for a self made
 conversation store, especially as my requirements will become more complex. 
```
---

     
 
all -  [ Does LangChain support Open AI Batch API? ](https://www.reddit.com/r/LangChain/comments/1hghach/does_langchain_support_open_ai_batch_api/) , 2024-12-18-0913
```
Hi,

  
I would like to utilize Open AI Batch API as it helps reduce the cost by 50%. I have been using Open AI through 
LangChain and I have been trying to find some information on how to incorporate the Open AI's Batch API but I found no h
elpful information on it. Does LangChain even support Batch API?
```
---

     
 
all -  [ Random Human messages and response ](https://www.reddit.com/r/LangChain/comments/1hgamfk/random_human_messages_and_response/) , 2024-12-18-0913
```
While printing result. Some random sentence gets print. Then needed response is printed and than again a random conversi
on gets print.Why is it happening.

Version of packages:  
langchain-core:0.3.25  
langchain-huggingface: 0.1.2

https:/
/preview.redd.it/sgm8d0b4ue7e1.png?width=1680&format=png&auto=webp&s=d871ee6e0357afbd78fa3bddea3221038743f246


```
---

     
 
all -  [ Persisting Chat History in LangChain JS ](https://www.reddit.com/r/LangChain/comments/1hgahty/persisting_chat_history_in_langchain_js/) , 2024-12-18-0913
```
I've read the docs for LangChain (JS) on how to use LangGraph and checkpointSaver etc to persist chat history. It all se
ems super complicated and unnecessary to me.

If I persist my own messages and use trim messages doesn't it accomplish t
he g\`oal of chat history?

`const llm = new ChatOpenAI({ model: 'gpt-4o' });`

`// GET THESE MESSAGES FROM DATABASE`  

`const messages = [`  
`new SystemMessage('you're a good assistant, you always respond with a joke.'),`  
`new HumanMess
age('i wonder why it's called langchain'),`  
`new AIMessage(`  
`'Well, I guess they thought 'WordRope' and 'SentenceSt
ring' just didn\'t have the same ring to it!'`  
`),`  
`new HumanMessage('and who is harrison chasing anyways'),`  
`ne
w AIMessage(`  
`'Hmmm let me think.\n\nWhy, he's probably chasing after the last cup of coffee in the office!'`  
`),` 
 
`new HumanMessage('what do you call a speechless parrot'),`  
`];`

`// TRIM MESSAGES`  
`const trimmed = await trimMe
ssages(messages, {`  
`maxTokens: 45,`  
`strategy: 'last',`  
`tokenCounter: llm,`  
`});`

`const chain = trimmed.pipe
(llm);`  
`// INVOKE LLM WITH CHAT HISTORY. MUCH EASIER!`  
`await chain.invoke(messages);`
```
---

     
 
all -  [ Forcing LLM function call not yet available using langchain4j ](https://www.reddit.com/r/LangChain/comments/1hg5lqh/forcing_llm_function_call_not_yet_available_using/) , 2024-12-18-0913
```
Hi all. Am I right that forcing of LLM function call using langchain4j library (Java) is not yet supported? Seems so but
 just want to confirm.
```
---

     
 
all -  [ LangGraph with React Agent & Azure GPT-4o: Parallel Tool Call Delay Issue in Traces ](https://www.reddit.com/r/LangChain/comments/1hfzr38/langgraph_with_react_agent_azure_gpt4o_parallel/) , 2024-12-18-0913
```
Hi everyone,

I am using a React agent with LangGraph to orchestrate function calls to Azure OpenAI GPT-4o. My workflow 
involves the following:

1. Extract 30 questions from one tool.
2. Use a RAG tool to retrieve answers.

Since `parallel 
tool call = true`, the RAG tool hits all the questions in parallel. However, when I check the traces, I observe an unexp
ected pattern:

* It processes the first 10-12 calls, then pauses briefly.
* After the gap, it processes the next 10-12 
calls.

I don’t see any set limits on the function or parameters for the number of parallel calls. I’ve attached an imag
e of the trace for clarity. Does anyone have an idea why this might be happening? Could it be an internal limitation or 
bottleneck somewhere?

  
Here’s the trace image for reference:  


https://preview.redd.it/95y456cvdb7e1.png?width=1863
&format=png&auto=webp&s=6e9cc7a6b03ea64a1cc0c0057074a61e7ec7a36c

Any help or insights would be greatly appreciated.


```
---

     
 
all -  [ Build a Production Level RAG System with LangGraph ](https://www.reddit.com/r/LangChain/comments/1hfyzbx/build_a_production_level_rag_system_with_langgraph/) , 2024-12-18-0913
```
Hello,

I recently open sourced a RAG application I built with LangGraph for a production application and I published th
e detail + the code in three articles on medium.com.

Part 1: [https://medium.com/@h1rouhani/build-production-ready-ai-a
ssistant-backend-service-in-python-part-1-9c7b2910eea3](https://medium.com/@h1rouhani/build-production-ready-ai-assistan
t-backend-service-in-python-part-1-9c7b2910eea3)

Part 2: [https://medium.com/@h1rouhani/build-production-ready-ai-assis
tant-backend-service-in-python-part-2-a8d31f0c2dc3](https://medium.com/@h1rouhani/build-production-ready-ai-assistant-ba
ckend-service-in-python-part-2-a8d31f0c2dc3)

Part 3: [https://medium.com/@h1rouhani/build-production-ready-ai-assistant
-backend-service-in-python-part-3-093ba216918e](https://medium.com/@h1rouhani/build-production-ready-ai-assistant-backen
d-service-in-python-part-3-093ba216918e)
```
---

     
 
all -  [ Llama 3.1 8B struggles with tool calls ](https://www.reddit.com/r/LocalLLaMA/comments/1hfxepg/llama_31_8b_struggles_with_tool_calls/) , 2024-12-18-0913
```
Hello,

I'm using the Llama 3.1 8B model within a standard ReAct architecture. Despite having a very specific system pro
mpt, the model consistently tries to call tools even when it's unnecessary.

I've checked my code, and everything seems 
fine. Interestingly, I tried the same setup with Mistral NeMo, and the experience was significantly better—no excessive 
tool calls.

I'm running this with LangChain and Ollama. Is this a known issue, or am I missing something? Has anyone el
se experienced this behavior?

Thanks in advance!
```
---

     
 
all -  [ Llama 3.1 8B model struggles when calling tools ](https://www.reddit.com/r/LangChain/comments/1hfxay2/llama_31_8b_model_struggles_when_calling_tools/) , 2024-12-18-0913
```
Hello,

I'm using the Llama 3.1 8B model within a standard ReAct architecture. Despite having a very specific system pro
mpt, the model consistently tries to call tools even when it's unnecessary.

I've checked my code, and everything seems 
fine. Interestingly, I tried the same setup with Mistral NeMo, and the experience was significantly better, no excessive
 tool calls.

I'm running this with LangChain and Ollama. Is this a known issue, or am I missing something? Has anyone e
lse experienced this behavior?

Thanks in advance!
```
---

     
 
all -  [ LLM reliability: getting users to trust your AI agent  ](https://www.anti-vc.com/p/getting-users-to-trust-your-ai-agent?utm_campaign=post&showWelcomeOnShare=false) , 2024-12-18-0913
```
Does anyone have lessons they’d like to share? I collected how startups use LangGraph and LangSmith to deploy Agentic RA
G. 
```
---

     
 
all -  [ Build (Fast)Agents with FastAPIs ](https://i.redd.it/6hgi2hy5897e1.jpeg) , 2024-12-18-0913
```
Okay so our definition of agent == prompt + LLM + APIs/tools. 

And https://github.com/katanemo/archgw is a new, framewo
rk agnostic, intelligent infrastructure project to build fast, observable agents using APIs as tools. It also has the #1
 trending function calling LLM on hugging face. https://x.com/salman_paracha/status/1865639711286690009?s=46

Disclaimer
: I help with devrel. Ask me anything. 
```
---

     
 
all -  [ tags option of XMLOutputParser? ](https://www.reddit.com/r/LangChain/comments/1hfoipj/tags_option_of_xmloutputparser/) , 2024-12-18-0913
```
Hey folks, the tags option of XMLOutputParser is not documented, what is it supposed to do ? I was expecting it to limit
 the available tags however it doesn't seem to have any effect.

[https://python.langchain.com/api\_reference/core/outpu
t\_parsers/langchain\_core.output\_parsers.xml.XMLOutputParser.html#langchain\_core.output\_parsers.xml.XMLOutputParser.
tags](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.xml.XMLOutputParser.h
tml#langchain_core.output_parsers.xml.XMLOutputParser.tags)  

```
---

     
 
all -  [ Querying Tables ](https://www.reddit.com/r/LangChain/comments/1hflxz6/querying_tables/) , 2024-12-18-0913
```
Hi,

Could you please guide me to some resources that can help me better understand the most suitable way to query table
s (specifically in my case)? I have read that RAG is not well-suited for tables and that it is better to use an SQL agen
t to create and execute queries.

For example, I have a table with a description column where each string is unique. If 
a user's query involves filtering this column (lets's say this get decided in previous nodes), it becomes challenging to
 handle using standard SQL. I have tried using the LIKE operator, but in the prompt I have to list all possible descript
ions in that column. While this method works, it is not scalable for other tables.

Do you have any suggestions? I was t
hinking whether there was a way of tagging such columns when creating the table in the database and if the search evolve
s around that column, use a specific NLP search (I may be completely off here) ?

Thank you in advance.
```
---

     
 
all -  [ Roast my beginner RAG project ](https://www.reddit.com/r/LangChain/comments/1hfliok/roast_my_beginner_rag_project/) , 2024-12-18-0913
```
I made a rag chatbot that uses docling for parsing files, semantic double pass merging (best) for chunking, qdrant for v
ector DB, gemini flash for chat. This includes hybrid search and Colbert for reranking. I made both local and cloud setu
p files. I think this is beginner friendly code who understands rag theoretically. Also added gradio chatbot( thanks to 
sonnet). You can find guide.md where I tried to explain about the project.

Everything is built with free API's

https:/
/github.com/Lokesh-Chimakurthi/Reliable_RAG
```
---

     
 
all -  [ Roast my beginner RAG project ](https://www.reddit.com/r/LLMDevs/comments/1hflhty/roast_my_beginner_rag_project/) , 2024-12-18-0913
```
I made a rag chatbot that uses docling for parsing files, semantic double pass merging (best) for chunking, qdrant for v
ector DB, gemini flash for chat. This includes hybrid search and Colbert for reranking. I made both local and cloud setu
p files. I think this is beginner friendly code who understands rag theoretically. No langchain, llamaindex just for chu
nking. Also added gradio chatbot( thanks to sonnet). You can find guide.md where I tried to explain about the project.


Everything is built with free API's

https://github.com/Lokesh-Chimakurthi/Reliable_RAG
```
---

     
 
all -  [ Anthropic'in çıkardığı Computer use ile ilgili bir teknoloji yaptık. ](https://www.reddit.com/r/CodingTR/comments/1hfkw8p/anthropicin_çıkardığı_computer_use_ile_ilgili_bir/) , 2024-12-18-0913
```
Merhaba arkadaşlar,

  
Son zamanlarda Anthropic bazı AI teknolojileri tanıttı. Computer Use ve MCP. Bu teknolojiler LLM
'lerin bilgisayarı daha kolay kullanmasını amaçlıyor. Computer use ve Model context protocol(MCP) LLM'lerin bilgisayarla
 etkileşime girmesini kolaylaştırıyor. Normalde klavye, mouse ile yaptığımız insan etkileşimini taklit ediyorlar. Comput
er use OCR'den çok daha kaliteli. MCP ise bir protokol.



Biz de açık kaynak bir computer use framework yazıyoruz. AI'ı
n bilgisayarı kullanarak task'leri bitirmesini sağlıyoruz. Hatta bu frameworkün kolayca denenebilmesi için bir playgroun
d ortamı yaptık isterseniz göz atabilirsiniz [playground.gca.dev](http://playground.gca.dev) 

Computer use teknolojisi 
şu anda çok yavaş. Örneğin Google'den araştırma yapmak için önce fareyi hareket ettiriyor, sonra iki kere tıklıyor sonra
 araştıracağı başlığı yazıyor, sonra siteye girmek için tekrar tıklıyor vs. Biz bu kısımlarda Langchain kullanıyoruz Lan
gchain tooları bu işi daha kolay daha az maliyetli ve daha hızlı yapıyorlar.

Computer use teknolojisinin iyi yanı ekran
da bir yere tıklatmak istediğinizde bunu çok yüksek bir başarı ile yapıyor. Ayrıca her adımı sırasıyla başarı ile tekrar
lıyor. Bu kısmı Langchain tooları ile yapamıyoruz. Onun için Anthropic'in computer use teknolojisini kullanıyoruz. 

  

Playground ortamında denemeler yapıp hata aldığınız şeyleri yazabilirseniz çok sevinirim. Hata alınan kısımlar için work
flowlar yazarak çözmeye çalışıyoruz. Tavsiyeleriniz bizim için çok değerli. 


```
---

     
 
all -  [ Understanding Prompt Engineering ](https://open.substack.com/pub/diamantai/p/understanding-prompt-engineering?utm_source=share&utm_medium=android&r=336pe4) , 2024-12-18-0913
```
Ever wondered why some prompts deliver great results while others fall flat? I put together this blog to break down what
’s happening behind the scenes and offer a practical way to understand how prompts guide language models.

🔍 What’s Insi
de:
1) How Language Models Work: A straightforward look at pretraining and fine-tuning, and how these phases shape what 
models can do.

2) Why Reasoning Works: Insights into how models use patterns and attention mechanisms to mimic logical 
reasoning, even when they’re trained to just predict the next word.

3) Techniques to Improve Prompts: Role prompting, s
tep-by-step reasoning, and temperature adjustments—practical tips you can start using right away.

4) Templates for Bett
er Results: Simple, reusable formats to guide models for tasks like coding, explaining concepts, or solving problems.
```
---

     
 
all -  [ Alternative to LangChain? ](https://www.reddit.com/r/LLMDevs/comments/1hfjfo6/alternative_to_langchain/) , 2024-12-18-0913
```
Hi, I am trying to compile an LLM application, I want to use features as in Langchain but Langchain documentation is ext
remely poor. I am looking to find alternatives, to langchain.

  
What else orchestration frameworks are being used in i
ndustry?
```
---

     
 
all -  [ The Top 14 Software Languages, Frameworks & Libraries Job Trends in 2024 ](https://www.reddit.com/r/cscareerquestions/comments/1hfi16b/the_top_14_software_languages_frameworks/) , 2024-12-18-0913
```
[https://mail.job.zip/p/the-job-zip-awards-2024-top-trends-in-ai-databases-software#the-top-14-software-languages-frame]
(https://mail.job.zip/p/the-job-zip-awards-2024-top-trends-in-ai-databases-software#the-top-14-software-languages-frame)


# 14.[ ](https://job.zip/trend/langchain?utm_source=mail.job.zip&utm_medium=referral&utm_campaign=the-job-zip-awards-2
024-top-trends-in-ai-databases-software)[Tailwind CSS](https://job.zip/trend/tailwind-css?utm_source=mail.job.zip&utm_me
dium=referral&utm_campaign=the-job-zip-awards-2024-top-trends-in-ai-databases-software)

📈 +25% Growth  
**800-1.6k empl
oyers**

A utility-first CSS framework that provides low-level utility classes to build custom designs without writing C
SS from scratch.

# 13.[ ](https://job.zip/trend/langchain?utm_source=mail.job.zip&utm_medium=referral&utm_campaign=the-
job-zip-awards-2024-top-trends-in-ai-databases-software)[FastAPI](https://job.zip/trend/fastapi?utm_source=mail.job.zip&
utm_medium=referral&utm_campaign=the-job-zip-awards-2024-top-trends-in-ai-databases-software)

📈 +25% Growth  
**1k-2k e
mployers**

FastAPI is a modern, high-performance web framework for building APIs with Python. It is designed to be easy
 to use and fast, leveraging Python's type hints to provide automatic validation and documentation of API endpoints.

# 
12.[ LangChain](https://job.zip/trend/langchain?utm_source=mail.job.zip&utm_medium=referral&utm_campaign=the-job-zip-awa
rds-2024-top-trends-in-ai-databases-software)

📈 +25% Growth  
**700-1.4k employers**

A framework for developing applic
ations powered by language models, enabling the integration of natural language processing capabilities into software.


# 11. [tRPC](https://job.zip/trend/trpc?utm_source=mail.job.zip&utm_medium=referral&utm_campaign=the-job-zip-awards-2024
-top-trends-in-ai-databases-software)

📈 +27% Growth  
**40-80 employers**

A TypeScript library for building end-to-end
 typesafe APIs, allowing seamless communication between client and server.

# 10. [AutoGen](https://job.zip/trend/autoge
n?utm_source=mail.job.zip&utm_medium=referral&utm_campaign=the-job-zip-awards-2024-top-trends-in-ai-databases-software)


📈 +39% Growth  
**70-140 employers**

AutoGen is a framework designed to facilitate the creation of complex AI applicat
ions by enabling multiple large language models (LLMs) to collaborate as agents.

# 9. [asyncio](https://job.zip/trend/a
syncio?utm_source=mail.job.zip&utm_medium=referral&utm_campaign=the-job-zip-awards-2024-top-trends-in-ai-databases-softw
are)

📈 +50% Growth  
**90-180 employers**

A library in Python to write concurrent code using the async/await syntax. A
llows for efficient management of I/O-bound operations.

# 8. [Htmx](https://job.zip/trend/htmx?utm_source=mail.job.zip&
utm_medium=referral&utm_campaign=the-job-zip-awards-2024-top-trends-in-ai-databases-software)

📈 +78% Growth  
**25-50 e
mployers**

A library that allows developers to access modern browser features directly from HTML, enabling dynamic web 
applications without JavaScript.

# 7. [Zustand](https://job.zip/trend/zustand-javascript?utm_source=mail.job.zip&utm_me
dium=referral&utm_campaign=the-job-zip-awards-2024-top-trends-in-ai-databases-software)

📈 +83% Growth  
**100-200 emplo
yers**

A small, fast, and scalable state management library for React applications, known for its simplicity and flexib
ility.

# 6. [Tauri](https://job.zip/trend/tauri-software?utm_source=mail.job.zip&utm_medium=referral&utm_campaign=the-j
ob-zip-awards-2024-top-trends-in-ai-databases-software)

📈 +111% Growth  
**12-24 employers**

A framework for building 
tiny, fast, and secure desktop applications with Rust and web technologies.

# 5. [TanStack](https://job.zip/trend/tanst
ack?utm_source=mail.job.zip&utm_medium=referral&utm_campaign=the-job-zip-awards-2024-top-trends-in-ai-databases-software
)

📈 +137% Growth  
**60-120 employers**

A collection of open-source libraries for building modern web applications, in
cluding tools for state management and data fetching.

# 4. [Shadcn](https://job.zip/trend/shadcn?utm_source=mail.job.zi
p&utm_medium=referral&utm_campaign=the-job-zip-awards-2024-top-trends-in-ai-databases-software)

📈 +200% Growth  
**40-8
0 employers**

Shadcn is a collection of reusable components and utilities for building web applications using React. It
 provides a set of pre-designed, customizable components that adhere to modern design principles, making it easier for d
evelopers to create consistent and visually appealing user interfaces.

# 3. [Ollama](https://job.zip/trend/ollama?utm_s
ource=mail.job.zip&utm_medium=referral&utm_campaign=the-job-zip-awards-2024-top-trends-in-ai-databases-software)

📈 +287
% Growth  
**30-60 employers**

Ollama is an open-source framework designed for serving large language models (LLMs) loc
ally on on-premise devices.

# 2. [DSPy](https://job.zip/trend/dspy?utm_source=mail.job.zip&utm_medium=referral&utm_camp
aign=the-job-zip-awards-2024-top-trends-in-ai-databases-software)

📈 +500% Growth  
**15-30 employers**

DSPy is an open
-source framework developed by Stanford NLP for programming language models, focusing on building modular AI systems rat
her than relying on traditional prompting.

# 1. [CrewAI](https://job.zip/trend/crewai?utm_source=mail.job.zip&utm_mediu
m=referral&utm_campaign=the-job-zip-awards-2024-top-trends-in-ai-databases-software)

📈 +1240% Growth  
**30-60 employer
s**
```
---

     
 
all -  [ Deploy RAG Chatbot on MS Teams ](https://www.reddit.com/r/LangChain/comments/1hfghrj/deploy_rag_chatbot_on_ms_teams/) , 2024-12-18-0913
```
Hey,

I’ve developed a RAG-based chatbot currently in the form of an IPYNB file and would like to deploy it on Microsoft
 Teams. However, I’m unsure how to proceed and would greatly appreciate any guidance or resources to help me achieve thi
s.


```
---

     
 
all -  [ How to Create and Integrate a Separate LangChain Package? Need Guidance! ](https://www.reddit.com/r/LangChain/comments/1hfevq4/how_to_create_and_integrate_a_separate_langchain/) , 2024-12-18-0913
```
Hi everyone!

I’m working on improving a `YoutubeLoader` integration for LangChain, and during the review process, it wa
s suggested that I create a separate package for it instead of contributing directly to the LangChain monorepo. I’ve rea
d the contributing guide and had a discussion on GitHub, but I’m still unclear about a few things.

Here’s what I unders
tand so far:

1. The integration package should be managed in **my own repository**, not as part of a fork of `langchain
-ai/langchain`.
2. Once ready, I need to publish the package to **PyPI** so others can install it.
3. I’ll need to updat
e LangChain’s docs and mark the old community integration as deprecated, linking users to my new package.

But I still h
ave a few questions:

* Do I need to first fork `langchain-ai/langchain` and integrate the package there, or is the work
flow entirely separate (as in, just create and maintain my own repository)?
* How exactly do I update LangChain's docs? 
Is it just about deprecating the old code and pointing to my package?

If anyone has experience contributing integration
s to LangChain or has gone through this process before, I’d love to hear your advice or tips!
```
---

     
 
all -  [ How can I use langgraph studio on windows [like a poor with out mac] ](https://www.reddit.com/r/LangChain/comments/1hfcu3s/how_can_i_use_langgraph_studio_on_windows_like_a/) , 2024-12-18-0913
```
I have agents built using langgraph. And I saw that l langgraph studio is only supported on Mac os. But they have the lo
cal host what ever method for the poors.

Help me to connect langgraph that run locally on the top of langsmith to my ag
ents please and thanks 
```
---

     
 
all -  [ Is there a way or plugin to connect to the ChatGPT browser interface? ](https://www.reddit.com/r/LangChain/comments/1hfcrq5/is_there_a_way_or_plugin_to_connect_to_the/) , 2024-12-18-0913
```
Hello everyone,  
I’ve recently started using LangChain, and I think it’s fantastic! However, for a small test I’m worki
ng on, I’d like to find a way to connect directly to my ChatGPT Pro account in the browser.

To clarify, I’m not looking
 to use the OpenAI API, but instead, I want to interact with the ChatGPT browser chat interface. Is this something that 
can be done?

Thanks in advance for any insights or suggestions!
```
---

     
 
all -  [ Seeking Architectures for Building Agents ](https://www.reddit.com/r/LangChain/comments/1hfb4o8/seeking_architectures_for_building_agents/) , 2024-12-18-0913
```
Hello everyone,

I am looking for papers that explore agent architectures for diverse objectives, as well as technical p
apers on real-world LLM-based agent solutions. For reference, I'm interested in works similar to the cited papers in the
 Langgraph tutorials:

[https://langchain-ai.github.io/langgraph/tutorials/](https://langchain-ai.github.io/langgraph/tu
torials/)

Thank you!


```
---

     
 
all -  [ Youtube Video content fact checker app ](https://www.reddit.com/r/LangChain/comments/1hfaqsj/youtube_video_content_fact_checker_app/) , 2024-12-18-0913
```
Hey falks, I am given a task to make an app that gets an input (query) from user and returns list of youtube videos (5 o
r 10). The returned list of videos are ordered accoridng to their similarity of title and the content of the video. Vide
os with the highest similarity should be in the top. I am new in langchain and have some idea how to tackle it:   
1. I 
extract the content and the title of the returned list of videos.  
2. Then do similarity search (like cosine-similarity
) between the title and the corresponding content.  
3. Return the list with the highest rate of similarity in the top. 


This is what I am planning to do.  
If there are anybody with such project experience or those who are expert, please,
 share your ideas to tackle this project.  

```
---

     
 
all -  [ Is LangChain the leading agentic framework? Should the begginer developers use LangChain or somethin ](https://www.reddit.com/r/AI_Agents/comments/1hf5dmq/is_langchain_the_leading_agentic_framework_should/) , 2024-12-18-0913
```
I want to learn to agentic frameworks but not sure where to start. Any tips?
```
---

     
 
all -  [ Test your AI apps with MockAI (Open-Source) ](https://www.reddit.com/r/LangChain/comments/1hf41kv/test_your_ai_apps_with_mockai_opensource/) , 2024-12-18-0913
```
As I began productionizing applications as an AI engineer, I needed a tool that would allow me to run tests, CI/CD pipel
ines, and benchmarks on my code that relied on LLMs. As you know once leaving demo-land these become EXTREMELY important
, especially with the fast nature of AI app development.

I needed a tool that would allow me to easily evaluate my LLM 
code without incurring cost and without blowing up waiting periods with generation times, while still allowing me to sim
ulate the 'real thing' as closely as possible, so I made [MockAI](https://github.com/ajac-zero/mock-ai).

I then realize
d that what I was building could be useful to other AI engineers, and so I turned it into an open-source library!

# How
 it works

MockAI works by mimicking servers from LLM providers locally, in a way that their API expects. As such, we ca
n use the normal `openai` library with MockAI along with any derivatives such as `langchain`. The only change we have to
 do is to set the `base_url` parameter to our local MockAI server.

# How to use

Start the server.

    # with pip inst
all
    $ pip install ai-mock 
    $ ai-mock server
    
    # or in one step with uv
    $ uvx ai-mock server

Change t
he base URL

    from openai import OpenAI
    
    # This client will call the real API
    client = OpenAI(api_key='..
.')
    
    # This client will call the mock API
    mock = OpenAI(api_key='...', base_url='http://localhost:8100/opena
i') 

The rest of the code is the exact same!

    # Real - Incur cost and generation time
    completion = client.chat.
completions.create(
        model='gpt-4o',
        messages=[ {'role': 'user', 'content': 'hello'} ]
      ).choices[0]
.message
    
    print(completion.content)
    # 'Hello! How may I assist you today?'
    
    # Mock - Instant and fre
e with no code changes
    completion = mock.chat.completions.create(
        model='gpt-4o',
        messages=[ {'role'
: 'user', 'content': 'hello'} ]
      ).choices[0].message
    
    print(completion.content)
    # 'hello'
    
    # B
ONUS - Set a custom mock response
    completion = mock.chat.completions.create(
        model='gpt-4o',
        message
s=[ {'role': 'user', 'content': 'Who created MockAI?'} ],
        extra_headers={'mock-response': 'MockAI was made by aj
ac-zero'},
      ).choices[0].message
    
    print(completion.content)
    # 'MockAI was made by ajac-zero'

Of course
, real use cases usually require tools, streaming, async, frameworks, etc. And I'm glad to say they are all supported by
 MockAI! You can check out more details [in the repo here](https://github.com/ajac-zero/mock-ai).

# Free Public API

I 
have set up a MockAI server as a public API, I intend for it to be a public service for our community, so you don't need
 to pay anything or create an account to make use of it.

If you decide to use it you don't have to install anything at 
all! Just change the 'base\_url' parameter to `mockai.ajac-zero.com`. Let's use `langchain` as an example:

    from lan
gchain_openai import ChatOpenAI
    from langchain_core.messages import HumanMessage, SystemMessage
    
    model = Cha
tOpenAI(
        model='gpt-4o-mini',
        api_key='...',
        base_url='https://mockai.ajac-zero.com/openai'
    
)
    
    messages = [
        SystemMessage('Translate the following from English into Italian'),
        HumanMessage
('hi!'),
    ]
    
    response = model.invoke(messages)
    print(response.content)
    # 'hi!'

It's a simple spell b
ut quite ~~unbreakable~~ useful. Hopefully, other AI engineers can make use of this library. I personally am using it fo
r testing, CI/CD pipelines, and recently to benchmark code without inference variations.

If you like the project or thi
nk it's useful, please leave a star on the [repo](https://github.com/ajac-zero/mock-ai)!
```
---

     
 
all -  [ Test your AI apps with MockAI (Open-Source) ](https://www.reddit.com/r/LLMDevs/comments/1hf3xga/test_your_ai_apps_with_mockai_opensource/) , 2024-12-18-0913
```
As I began productionizing applications as an AI engineer, I needed a tool that would allow me to run tests, CI/CD pipel
ines, and benchmarks on my code that relied on LLMs. As you know once leaving demo-land these become EXTREMELY important
, especially with the fast nature of AI app development.

I needed a tool that would allow me to easily evaluate my LLM 
code without incurring cost and without blowing up waiting periods with generation times, while still allowing me to sim
ulate the 'real thing' as closely as possible, so I made [MockAI](https://github.com/ajac-zero/mock-ai).

I then realize
d that what I was building could be useful to other AI engineers, and so I turned it into an open-source library!

# How
 it works

MockAI works by mimicking servers from LLM providers locally, in a way that their API expects. As such, we ca
n use the normal `openai` library with MockAI along with any derivatives such as `langchain`. The only change we have to
 do is to set the `base_url` parameter to our local MockAI server.

# How to use

Start the server.

    # with pip inst
all
    $ pip install ai-mock 
    $ ai-mock server
    
    # or in one step with uv
    $ uvx ai-mock server

Change t
he base URL

    from openai import OpenAI
    
    # This client will call the real API
    client = OpenAI(api_key='..
.')
    
    # This client will call the mock API
    mock = OpenAI(api_key='...', base_url='http://localhost:8100/opena
i') 

The rest of the code is the exact same!

    # Real - Incur cost and generation time
    completion = client.chat.
completions.create(
        model='gpt-4o',
        messages=[ {'role': 'user', 'content': 'hello'} ]
      ).choices[0]
.message
    
    print(completion.content)
    # 'Hello! How may I assist you today?'
    
    # Mock - Instant and fre
e with no code changes
    completion = mock.chat.completions.create(
        model='gpt-4o',
        messages=[ {'role'
: 'user', 'content': 'hello'} ]
      ).choices[0].message
    
    print(completion.content)
    # 'hello'
    
    # B
ONUS - Set a custom mock response
    completion = mock.chat.completions.create(
        model='gpt-4o',
        message
s=[ {'role': 'user', 'content': 'Who created MockAI?'} ],
        extra_headers={'mock-response': 'MockAI was made by aj
ac-zero'},
      ).choices[0].message
    
    print(completion.content)
    # 'MockAI was made by ajac-zero'

Of course
, real use cases usually require tools, streaming, async, frameworks, etc. And I'm glad to say they are all supported by
 MockAI! You can check out more details [in the repo here](https://github.com/ajac-zero/mock-ai).

# Free Public API

I 
have set up a MockAI server as a public API, I intend for it to be a public service for our community, so you don't need
 to pay anything or create an account to make use of it.

If you decide to use it you don't have to install anything at 
all! Just change the 'base\_url' parameter to `mockai.ajac-zero.com`. Let's use `langchain` as an example:

    from lan
gchain_openai import ChatOpenAI
    from langchain_core.messages import HumanMessage, SystemMessage
    
    model = Cha
tOpenAI(
        model='gpt-4o-mini',
        api_key='...',
        base_url='https://mockai.ajac-zero.com/openai'
    
)
    
    messages = [
        SystemMessage('Translate the following from English into Italian'),
        HumanMessage
('hi!'),
    ]
    
    response = model.invoke(messages)
    print(response.content)
    # 'hi!'

It's a simple spell b
ut quite ~~unbreakable~~ useful. Hopefully, other AI engineers can make use of this library. I personally am using it fo
r testing, CI/CD pipelines, and recently to benchmark code without inference variations.

If you like the project or thi
nk it's useful, please leave a star on the [repo](https://github.com/ajac-zero/mock-ai)!
```
---

     
 
all -  [ Why is nobody talking about recursive task decomposition. ](https://www.reddit.com/r/LangChain/comments/1hf1ang/why_is_nobody_talking_about_recursive_task/) , 2024-12-18-0913
```
Im researching the possibilities of integrating LLMs for pentesting. I researched many architecture and the one that con
viced me the most is recursive task decomposition. It is the most convincing architecture to me, yet nobody is talking a
bout it. Pentesting for me is just a way to test the agents capabilities, but for me if we can correctly decompose a tas
k recursively into subtaskks esay enough, every task would be doable. From pentesting, to playing games, to solving prob
lems,....
Every body is focusing on making niche agents  to execute specifics kind of task but nobody is thinking about 
something more generic. Look at LLMs , they weren't made for juste one specific topic, , they do all sort of things. I w
onder why nobody is doing this. 
Does anybody have an opinion on this?

```
---

     
 
all -  [ New to Coding Help - LangChain chat bot - stuck for 3 days ](https://www.reddit.com/r/LangChain/comments/1hey2bo/new_to_coding_help_langchain_chat_bot_stuck_for_3/) , 2024-12-18-0913
```
Hi guys, i thought of something I wanted to build a couple weeks ago so ive been learning to code and heavily relying on
 cursor. everything has been going fine until now. I have the code for a functional langchain chat bot. i know its funct
ional becuase it works in emulator. but when I deploy it it doesn't work. it throws a cors error but nothing ive tried f
or 3 days has resolved it. Ive had to hard reset from git twice now. i cant imagine its a complex issue. i just assume t
hat my lack of foundational coding knowledge is blocking me from fixing it. would any one have any idea whats going on? 
or have questions I can answer that would help get to a solution?   
im using firebase as my backend so its firebase emu
lator im working with and firebase deployment. 

to anyone that ends up trying to help, thank you 🙏
```
---

     
 
all -  [ Which vision model do you use for embeddings for vision rag? ](https://www.reddit.com/r/LangChain/comments/1hethzo/which_vision_model_do_you_use_for_embeddings_for/) , 2024-12-18-0913
```
Which model do you all use for vision embeddings other than colpali based or is it the best? Would like to know both fre
e and paid ways
```
---

     
 
all -  [ [For Hire] Skilled Full Stack Developer, AI/ML Expert, and DevOps Pro – Let’s Build Your Next Game-C ](https://www.reddit.com/r/forhire/comments/1hesz9z/for_hire_skilled_full_stack_developer_aiml_expert/) , 2024-12-18-0913
```
🚀 **Full Stack Developer | AI/ML Engineer | DevOps Specialist – Open for Hire!**

Hi there! I'm Sheryar 👋, a passionate 
developer with the skills and experience to bring your vision to life. Here's what I bring to the table:

# 💻 Full Stack
 Development Expertise

* **Frontend:** React | Angular
* **Backend:** Node.js | NestJS
* **Payments:** Seamless Stripe 
Integrations
* **Cloud Services:** AWS | GCP

# 🤖 AI & Machine Learning Innovations

* Smart Chatbots built with LangCha
in
* Custom NLP models for automation and insights

# ⚙️ DevOps Solutions for Scalable Systems

* **CI/CD Pipelines:** G
itHub Actions | Jenkins
* **Containerization:** Docker | Kubernetes
* **Infrastructure as Code:** Terraform | Ansible

#
 🌟 Notable Projects

* 🚗 **Ride-Sharing App:** Real-time tracking & payment flows
* 📦 **Logistics Platform:** Route opti
mization for multi-stop deliveries
* 🛒 **E-Commerce Infrastructure:** Scalable Kubernetes clusters

# 💰 Rates

* $10–$15
/hour (negotiable based on project scope)

📧 **DM me to discuss your project needs!**  
🔗 **GitHub:** [storm1033](https:
//github.com/storm1033)

Let’s collaborate and turn your ideas into reality! 🌟
```
---

     
 
all -  [ What is your python stack? ](https://www.reddit.com/r/ExperiencedDevs/comments/1hes05o/what_is_your_python_stack/) , 2024-12-18-0913
```
Many of the libraries, concepts and design patterns have been understood by me in practice. when entering a new project,
 or when I am faced with a problem for my existing stack, I tend to search the web for 'how do I do X' or ask colleagues
 for pointers. I figured I'd make a post where people denote the stack they use for different workflows and what problem
s that stack solves. I'll start!

APIs:

- FastAPI as the base
- Strict Pydantic validation across the entire app helps 
me work more structured and catch errors easier
- SQLAlchemy as the sql adapter if needed. I make a base CRUD class in s
qlalchemy then make CRUD pydantic classes for required inputs and output schemas, then make individual classes for each 
db model along with unique methods for querying
- Tenacity for retries
- Celery for task orchestration and execution alt
hough there's a new player in town called Prefect. For pure workflow orchestration you could also use DAG based tools li
ke Dagster, Argo and Airflow although I haven't used these outside the context of a kube cluster and i don't enjoy worki
ng with those. You can also use fastapi background tasks in place of celery but I'm not familiar with it and it's limita
tions 
- Webhooks for managing events and routing. I use hookdeck personally
- Firestore for when im not feeling like us
ing sql or the data is primarily JSON based. You can create listeners on cloud functions but be careful of race conditio
ns.
- Cloud run for hosting the api
- gitlab for the repo cause it let's me have an integrated cicd platform without nee
ding to use extensions plus the UI is nicer for me
- Redis to handle queues, I don't like working with rabbitmq for this

- Celery and cloud run don't work together, so the Celery workers need to be on a VM while the API can be on cloud run.
 People also use cloud tasks for celery but haven't looked into that


Specific services for different tasks:

LLMs:
- P
ortkey as the entry point for all LLM calls. I use a long config to define fallback behavior and retries and guardrails 
for prompt injection 
- Deepinfra and Fireworks as the AI providers
- Actively avoid all langchain implementations inclu
ding langsmith and langgraph and build this out myself if needed.

Scraping:
- Scrapingbee because these guys were the m
ost reliable for web scraping
- Proxycurl for linkedin Scraping
- Data Ocean on rapid api for crunchbase Scraping
- To g
et the news I use newspaper, which is an unofficial google news package. it works decently 
- SerperAPI for google searc
hes

This stack has allowed me to make apps that people pay money for, which is neat. I'm sure I'll think of other stuff
 in the future so will be editing this post

```
---

     
 
all -  [ Need help with selecting a good LLM ](https://www.reddit.com/r/LLMDevs/comments/1hepy6n/need_help_with_selecting_a_good_llm/) , 2024-12-18-0913
```
Hello, I'm making a project where every user has 10k input tokens and 400 output tokens worth of interaction at least 20
0 times a month. The project is for general use(Like general knowledge question,  or generating mathematical questions).
 Basically, it won't be much related to programming so IK claude isn't the best option.

I'm super new to all these LLM 
API's, so can someone guide me on the best cost-efficient api I can buy and integrate into my project? It'd also be real
ly helpful if it supports Langchain
```
---

     
 
all -  [ RAG on excel files ](https://www.reddit.com/r/LangChain/comments/1hen4ds/rag_on_excel_files/) , 2024-12-18-0913
```
Hey guys I’m currently tasked with working on rag for several excel files and I was wondering if someone has done someth
ing similar in production already. I’ve seen PandasAI but not sure if I should go for it or if theres a better alternati
ve. I have about 50 excel files.

Also if you have pushed to production, what were the issues you faced? Thanks in advan
ce
```
---

     
 
all -  [ struggling to understand the langgraph tutorial (build a basic chatbot) ](https://www.reddit.com/r/LangChain/comments/1heg7pi/struggling_to_understand_the_langgraph_tutorial/) , 2024-12-18-0913
```
link: [https://langchain-ai.github.io/langgraph/tutorials/introduction/#part-1-build-a-basic-chatbot](https://langchain-
ai.github.io/langgraph/tutorials/introduction/#part-1-build-a-basic-chatbot)

So far I am able to follow this tutorial f
or the 'build chatbot section' - what I don't understand is the logic in the 'while True' statement below - specifically
 on how the excelption logic is invoked:

  
`while True:`  
`try:`  
`user_input = input('User: ')`  
`if user_input.lo
wer() in ['quit', 'exit', 'q']:`  
`print('Goodbye!')`  
`break`  
  
`stream_graph_updates(user_input)`  
`except:`  
`
# fallback if input() is not available`  
`user_input = 'What do you know about LangGraph?'`  
`print('User: ' + user_in
put)`  
`stream_graph_updates(user_input)`  
`break`

  


Question :    exception logic trigger - how does it get trigg
ered? 

If you look at the tutorial, it is showing the results of executing the exception logic -  

`Assistant: LangGra
ph is a library designed to help build stateful multi-agent applications using language models. It provides tools for cr
eating workflows and state machines to coordinate multiple AI agents or language model interactions. LangGraph is built 
on top of LangChain, leveraging its components while adding graph-based coordination capabilities. It's particularly use
ful for developing more complex, stateful AI applications that go beyond simple query-response interactions.`  
Goodbye!




How does the execution logic  get triggered?  




```
---

     
 
all -  [ Do we have anything to replicate livekit agents voice capabilities with langgraph? ](https://www.reddit.com/r/LangChain/comments/1heed8a/do_we_have_anything_to_replicate_livekit_agents/) , 2024-12-18-0913
```
I am working on a voice agent that needs to have as low latency as possible with the speech-text-speech pipeline. (I am 
not going for multimodal realtime apis like the one of openai and recently released gemini 2.0 flash because they are co
stly and in beta as well as closed source). 

I want to make as many things on opensource as possible.

I first looked i
nto livekit which is opensource webrtc framework . which also has agents , these agents are pretty fast with a lot of op
timizations in the streaming pipeline. Now the issue with this is that agent framework of livekit is pretty basic with f
unction calling, i was looking for something more like langgraph and in best case scenario a langraph integration with l
ivekit.

On a similar note i looked at pipecat as well which also has pipecat flow to simulate decent flows somewhat lik
e langgraph while also being optimized for voice capabilites. The issue wth pipecat is that although it is opensource it
self, it only fully supports daily as a transport layer (something like livekit transport integration is in progress but
 even then i would prefer if instead of pipecat flows i could use something like langraph with good voice capabilities)


I wanted to ask for any suggestions on how to go about this problem. Thanks.
```
---

     
 
all -  [ Is this Langgraph chatbot worth it? ROAST ME ](https://www.reddit.com/r/LangChain/comments/1hee7f1/is_this_langgraph_chatbot_worth_it_roast_me/) , 2024-12-18-0913
```
Hi everybody,

I'm the founder of [**Chetty.ai**](http://Chetty.ai), an AI chatbot for websites.

Recently, I developed 
the first version of an agent in **Langgraph** to handle web searches in a more complex way. I already have ten major cu
stomers using this engine, so everything is fully operational and in production.

Could you please try it out and share 
your honest feedback? It's simple—just insert any website and ask about their services.

[https://chetty.ai/advanced-sea
rch-demo](https://chetty.ai/advanced-search-demo)

Thanks!
```
---

     
 
all -  [ I've built an MVP to level up your LangChain and AI skills - looking for feedback 🚀 ](https://www.reddit.com/r/LangChain/comments/1he8wiv/ive_built_an_mvp_to_level_up_your_langchain_and/) , 2024-12-18-0913
```
Hello LangChain and AI experts,

I'm building a free app to help users enhance their AI skills, including prompt enginee
ring, LangChain, Haystack, etc, and would like to see if it is useful for you.

What I've built:

* **Skill Trees:** Vis
ual guides to discover essential skills and concepts, specifically for Python developers working in advanced AI areas.
*
 **Quizzes:** Test your knowledge and identify gaps to improve your expertise in your focus areas.

I've built an MVP an
d would love your feedback to make this more useful, if you:

* Work with tools like LangChain,
* Dive into prompt engin
eering or Python AI/ML development,
* Or just want to see how this could help you grow.

**You’re welcome to try it out 
— It’s free:**

👉 [skill-up.io](https://www.skill-up.io/)

I hope it can be useful for you. If you like it, feel free to
 sign up to track your progress.

[AI and ML skill tree](https://preview.redd.it/nlovzr0q827e1.jpg?width=1080&format=pjp
g&auto=webp&s=55f7c0cdf1ed2915f0ce9a3f329cdac2780e3be9)

I appreciate your feedback:

* Is the skill tree structure help
ful for navigating complex topics?
* Are the quizzes relevant and engaging?
* What features would you me to add to solve
 your pain points when learning Python and related techs?

I’d love to help you more! Let me know what you need and I’ll
 build it. You can reach out by filling out [this form](https://www.notion.so/140ac95ae0208076972ef715f74c4429?pvs=21) o
r messaging me.
```
---

     
 
all -  [ Langchain Integration ](https://www.reddit.com/r/AIlice/comments/1he4oby/langchain_integration/) , 2024-12-18-0913
```
Love the project, separately have been exploring RAG set ups through langchain and wondering if people know any approach
es that can be used to integrate Allice with that efficiently? 
```
---

     
 
all -  [ How to make SqlAgent to query NoSQL for answers? ](https://www.reddit.com/r/learnmachinelearning/comments/1he3ebg/how_to_make_sqlagent_to_query_nosql_for_answers/) , 2024-12-18-0913
```
I am new to ML.

LangChain has that with relational databases. How to make it work with NoSQL databases?
```
---

     
 
all -  [ I am sharing ChatGPT & AI courses and projects on YouTube
 ](https://www.reddit.com/r/ChatGPT/comments/1hdyje8/i_am_sharing_chatgpt_ai_courses_and_projects_on/) , 2024-12-18-0913
```
Hello, I wanted to share that I am sharing free courses and projects on my YouTube Channel. I have more than 200 videos 
and I created playlists for learning Data Science. I am leaving the playlist link below, have a great day!

AI Tutorials
 (ChatGPT, LangChain & LLMs) -> [https://youtube.com/playlist?list=PLTsu3dft3CWhAAPowINZa5cMZ5elpfrxW&si=DvsefwOEJd3k-Sh
N](https://youtube.com/playlist?list=PLTsu3dft3CWhAAPowINZa5cMZ5elpfrxW&si=DvsefwOEJd3k-ShN)
```
---

     
 
MachineLearning -  [ [P] Minima: local conversational retrieval augmented generation project (Ollama, Langchain, FastAPI, ](https://www.reddit.com/r/MachineLearning/comments/1h1pudq/p_minima_local_conversational_retrieval_augmented/) , 2024-12-18-0913
```
  
[https://github.com/dmayboroda/minima](https://github.com/dmayboroda/minima)  
  
Hey everyone, I would like to intro
duce you my latest repo, that is a local conversational rag on your files, Be honest, you can use this as a rag on-premi
ses, cause it is build with docker, langchain, ollama, fastapi, hf All models download automatically, soon I'll add an a
bility to choose a model For now solution contains:

* Locally running Ollama (currently qwen-0.5b model hardcoded, soon
 you'll be able to choose a model from ollama registry)
* Local indexing (using sentence-transformer embedding model, yo
u can switch to other model, but only sentence-transformers applied, also will be changed soon)
* Qdrant container runni
ng on your machine
* Reranker running locally (BAAI/bge-reranker-base currently hardcoded, but i will also add an abilit
y to choose a reranker)
* Websocket based chat with saving history
* Simple chat UI written with React
* As a plus, you 
can use local rag with ChatGPT as a custom GPT, so you able to query your local data through official chatgpt web and ma
c os/ios app.
* You can deploy it as a RAG on-premises, all containers can work on CPU machines

Couple of ideas/problem
s:

* Model Context Protocol support
* Right now there is no incremental indexing or reindexing
* No selection for the m
odels (will be added soon)
* Different environment support (cuda, mps, custom npu's)

Welcome to contribute (watch, fork
, star) Thank you so much!
```
---

     
