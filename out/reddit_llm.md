 
all -  [ Llama 3.1 8B struggles with tool calls ](https://www.reddit.com/r/LocalLLaMA/comments/1hfxepg/llama_31_8b_struggles_with_tool_calls/) , 2024-12-17-0914
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

     
 
all -  [ Llama 3.1 8B model struggles when calling tools ](https://www.reddit.com/r/LangChain/comments/1hfxay2/llama_31_8b_model_struggles_when_calling_tools/) , 2024-12-17-0914
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

     
 
all -  [ LLM reliability: getting users to trust your AI agent  ](https://www.anti-vc.com/p/getting-users-to-trust-your-ai-agent?utm_campaign=post&showWelcomeOnShare=false) , 2024-12-17-0914
```
Does anyone have lessons they’d like to share? I collected how startups use LangGraph and LangSmith to deploy Agentic RA
G. 
```
---

     
 
all -  [ Build (Fast)Agents with FastAPIs ](https://i.redd.it/6hgi2hy5897e1.jpeg) , 2024-12-17-0914
```
Okay so our definition of agent == prompt + LLM + APIs/tools. 

And https://github.com/katanemo/archgw is a new, framewo
rk agnostic, intelligent infrastructure project to build fast, observable agents using APIs as tools. It also has the #1
 trending function calling LLM on hugging face. https://x.com/salman_paracha/status/1865639711286690009?s=46

Disclaimer
: I help with devrel. Ask me anything. 
```
---

     
 
all -  [ tags option of XMLOutputParser? ](https://www.reddit.com/r/LangChain/comments/1hfoipj/tags_option_of_xmloutputparser/) , 2024-12-17-0914
```
Hey folks, the tags option of XMLOutputParser is not documented, what is it supposed to do ? I was expecting it to limit
 the available tags however it doesn't seem to have any effect.

[https://python.langchain.com/api\_reference/core/outpu
t\_parsers/langchain\_core.output\_parsers.xml.XMLOutputParser.html#langchain\_core.output\_parsers.xml.XMLOutputParser.
tags](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.xml.XMLOutputParser.h
tml#langchain_core.output_parsers.xml.XMLOutputParser.tags)  

```
---

     
 
all -  [ Querying Tables ](https://www.reddit.com/r/LangChain/comments/1hflxz6/querying_tables/) , 2024-12-17-0914
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

     
 
all -  [ Roast my beginner RAG project ](https://www.reddit.com/r/LangChain/comments/1hfliok/roast_my_beginner_rag_project/) , 2024-12-17-0914
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

     
 
all -  [ Roast my beginner RAG project ](https://www.reddit.com/r/LLMDevs/comments/1hflhty/roast_my_beginner_rag_project/) , 2024-12-17-0914
```
I made a rag chatbot that uses docling for parsing files, semantic double pass merging (best) for chunking, qdrant for v
ector DB, gemini flash for chat. This includes hybrid search and Colbert for reranking. I made both local and cloud setu
p files. I think this is beginner friendly code who understands rag theoretically. No langchain, llamaindex just for chu
nking. Also added gradio chatbot( thanks to sonnet). You can find guide.md where I tried to explain about the project.


Everything is built with free API's

https://github.com/Lokesh-Chimakurthi/Reliable_RAG
```
---

     
 
all -  [ Anthropic'in çıkardığı Computer use ile ilgili bir teknoloji yaptık. ](https://www.reddit.com/r/CodingTR/comments/1hfkw8p/anthropicin_çıkardığı_computer_use_ile_ilgili_bir/) , 2024-12-17-0914
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

     
 
all -  [ Understanding Prompt Engineering ](https://open.substack.com/pub/diamantai/p/understanding-prompt-engineering?utm_source=share&utm_medium=android&r=336pe4) , 2024-12-17-0914
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

     
 
all -  [ Alternative to LangChain? ](https://www.reddit.com/r/LLMDevs/comments/1hfjfo6/alternative_to_langchain/) , 2024-12-17-0914
```
Hi, I am trying to compile an LLM application, I want to use features as in Langchain but Langchain documentation is ext
remely poor. I am looking to find alternatives, to langchain.

  
What else orchestration frameworks are being used in i
ndustry?
```
---

     
 
all -  [ The Top 14 Software Languages, Frameworks & Libraries Job Trends in 2024 ](https://www.reddit.com/r/cscareerquestions/comments/1hfi16b/the_top_14_software_languages_frameworks/) , 2024-12-17-0914
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

     
 
all -  [ check my resume ](https://www.reddit.com/gallery/1hfhm12) , 2024-12-17-0914
```

```
---

     
 
all -  [ Deploy RAG Chatbot on MS Teams ](https://www.reddit.com/r/LangChain/comments/1hfghrj/deploy_rag_chatbot_on_ms_teams/) , 2024-12-17-0914
```
Hey,

I’ve developed a RAG-based chatbot currently in the form of an IPYNB file and would like to deploy it on Microsoft
 Teams. However, I’m unsure how to proceed and would greatly appreciate any guidance or resources to help me achieve thi
s.


```
---

     
 
all -  [ How to Create and Integrate a Separate LangChain Package? Need Guidance! ](https://www.reddit.com/r/LangChain/comments/1hfevq4/how_to_create_and_integrate_a_separate_langchain/) , 2024-12-17-0914
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

     
 
all -  [ How can I use langgraph studio on windows [like a poor with out mac] ](https://www.reddit.com/r/LangChain/comments/1hfcu3s/how_can_i_use_langgraph_studio_on_windows_like_a/) , 2024-12-17-0914
```
I have agents built using langgraph. And I saw that l langgraph studio is only supported on Mac os. But they have the lo
cal host what ever method for the poors.

Help me to connect langgraph that run locally on the top of langsmith to my ag
ents please and thanks 
```
---

     
 
all -  [ Is there a way or plugin to connect to the ChatGPT browser interface? ](https://www.reddit.com/r/LangChain/comments/1hfcrq5/is_there_a_way_or_plugin_to_connect_to_the/) , 2024-12-17-0914
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

     
 
all -  [ Seeking Architectures for Building Agents ](https://www.reddit.com/r/LangChain/comments/1hfb4o8/seeking_architectures_for_building_agents/) , 2024-12-17-0914
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

     
 
all -  [ Youtube Video content fact checker app ](https://www.reddit.com/r/LangChain/comments/1hfaqsj/youtube_video_content_fact_checker_app/) , 2024-12-17-0914
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

     
 
all -  [ Is LangChain the leading agentic framework? Should the begginer developers use LangChain or somethin ](https://www.reddit.com/r/AI_Agents/comments/1hf5dmq/is_langchain_the_leading_agentic_framework_should/) , 2024-12-17-0914
```
I want to learn to agentic frameworks but not sure where to start. Any tips?
```
---

     
 
all -  [ Test your AI apps with MockAI (Open-Source) ](https://www.reddit.com/r/LangChain/comments/1hf41kv/test_your_ai_apps_with_mockai_opensource/) , 2024-12-17-0914
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

     
 
all -  [ Test your AI apps with MockAI (Open-Source) ](https://www.reddit.com/r/LLMDevs/comments/1hf3xga/test_your_ai_apps_with_mockai_opensource/) , 2024-12-17-0914
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

     
 
all -  [ Why is nobody talking about recursive task decomposition. ](https://www.reddit.com/r/LangChain/comments/1hf1ang/why_is_nobody_talking_about_recursive_task/) , 2024-12-17-0914
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

     
 
all -  [ New to Coding Help - LangChain chat bot - stuck for 3 days ](https://www.reddit.com/r/LangChain/comments/1hey2bo/new_to_coding_help_langchain_chat_bot_stuck_for_3/) , 2024-12-17-0914
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

     
 
all -  [ Which vision model do you use for embeddings for vision rag? ](https://www.reddit.com/r/LangChain/comments/1hethzo/which_vision_model_do_you_use_for_embeddings_for/) , 2024-12-17-0914
```
Which model do you all use for vision embeddings other than colpali based or is it the best? Would like to know both fre
e and paid ways
```
---

     
 
all -  [ [For Hire] Skilled Full Stack Developer, AI/ML Expert, and DevOps Pro – Let’s Build Your Next Game-C ](https://www.reddit.com/r/forhire/comments/1hesz9z/for_hire_skilled_full_stack_developer_aiml_expert/) , 2024-12-17-0914
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

     
 
all -  [ What is your python stack? ](https://www.reddit.com/r/ExperiencedDevs/comments/1hes05o/what_is_your_python_stack/) , 2024-12-17-0914
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

     
 
all -  [ Need help with selecting a good LLM ](https://www.reddit.com/r/LLMDevs/comments/1hepy6n/need_help_with_selecting_a_good_llm/) , 2024-12-17-0914
```
Hello, I'm making a project where every user has 10k input tokens and 400 output tokens worth of interaction at least 20
0 times a month. The project is for general use(Like general knowledge question,  or generating mathematical questions).
 Basically, it won't be much related to programming so IK claude isn't the best option.

I'm super new to all these LLM 
API's, so can someone guide me on the best cost-efficient api I can buy and integrate into my project? It'd also be real
ly helpful if it supports Langchain
```
---

     
 
all -  [ RAG on excel files ](https://www.reddit.com/r/LangChain/comments/1hen4ds/rag_on_excel_files/) , 2024-12-17-0914
```
Hey guys I’m currently tasked with working on rag for several excel files and I was wondering if someone has done someth
ing similar in production already. I’ve seen PandasAI but not sure if I should go for it or if theres a better alternati
ve. I have about 50 excel files.

Also if you have pushed to production, what were the issues you faced? Thanks in advan
ce
```
---

     
 
all -  [ struggling to understand the langgraph tutorial (build a basic chatbot) ](https://www.reddit.com/r/LangChain/comments/1heg7pi/struggling_to_understand_the_langgraph_tutorial/) , 2024-12-17-0914
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

     
 
all -  [ Do we have anything to replicate livekit agents voice capabilities with langgraph? ](https://www.reddit.com/r/LangChain/comments/1heed8a/do_we_have_anything_to_replicate_livekit_agents/) , 2024-12-17-0914
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

     
 
all -  [ Is this Langgraph chatbot worth it? ROAST ME ](https://www.reddit.com/r/LangChain/comments/1hee7f1/is_this_langgraph_chatbot_worth_it_roast_me/) , 2024-12-17-0914
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

     
 
all -  [ I've built an MVP to level up your LangChain and AI skills - looking for feedback 🚀 ](https://www.reddit.com/r/LangChain/comments/1he8wiv/ive_built_an_mvp_to_level_up_your_langchain_and/) , 2024-12-17-0914
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

     
 
all -  [ Langchain Integration ](https://www.reddit.com/r/AIlice/comments/1he4oby/langchain_integration/) , 2024-12-17-0914
```
Love the project, separately have been exploring RAG set ups through langchain and wondering if people know any approach
es that can be used to integrate Allice with that efficiently? 
```
---

     
 
all -  [ How to make SqlAgent to query NoSQL for answers? ](https://www.reddit.com/r/learnmachinelearning/comments/1he3ebg/how_to_make_sqlagent_to_query_nosql_for_answers/) , 2024-12-17-0914
```
I am new to ML.

LangChain has that with relational databases. How to make it work with NoSQL databases?
```
---

     
 
all -  [ I am sharing ChatGPT & AI courses and projects on YouTube
 ](https://www.reddit.com/r/ChatGPT/comments/1hdyje8/i_am_sharing_chatgpt_ai_courses_and_projects_on/) , 2024-12-17-0914
```
Hello, I wanted to share that I am sharing free courses and projects on my YouTube Channel. I have more than 200 videos 
and I created playlists for learning Data Science. I am leaving the playlist link below, have a great day!

AI Tutorials
 (ChatGPT, LangChain & LLMs) -> [https://youtube.com/playlist?list=PLTsu3dft3CWhAAPowINZa5cMZ5elpfrxW&si=DvsefwOEJd3k-Sh
N](https://youtube.com/playlist?list=PLTsu3dft3CWhAAPowINZa5cMZ5elpfrxW&si=DvsefwOEJd3k-ShN)
```
---

     
 
all -  [ Frustrated. Should I change my career? ](https://www.reddit.com/r/technepal/comments/1hdwai2/frustrated_should_i_change_my_career/) , 2024-12-17-0914
```
Few years ago I started with Python. Until now I have learned almost eveything I felt required SQL, Pandas, Numpy, Matpl
otlib, Langchain, AWS, Fastapi, Tensorflow and many more. Still I am not even getting  glimpse of finding a job. Thought
 I could get into AI, ML, Data Science of not at least Data Analytics. I have contacted every person. Most of them tell 
that it's difficult to find internship in these fields. Without internship, how could I even start my professional life.
 Companies open vacancies for seniors. 

  At current, I am studying CSIT sixth sem. Most of you may think that it's too
 early. But what if I don't get job even after graduation. My college is useless. I don't even rely on it. Just thinking
 if it is better to go in web development with python or some other areas. If not, the last option that resorts is quick
ly head off to abroad. I see nothing to stay here.
```
---

     
 
all -  [ Made a simple processor for building systems like Anthropic's artifacts/v0.dev ](https://www.reddit.com/r/LangChain/comments/1hdufsv/made_a_simple_processor_for_building_systems_like/) , 2024-12-17-0914
```
Built this small tag processor after wanting to quickly prototype systems similar to Anthropic's artifacts or v0.dev. No
t trying to recreate them, just wanted something lightweight that lets you quickly build and experiment with similar ide
as.

Basic example:

    typescriptCopyconst processor = new FluffyTagProcessor();
    
    // Handle regular conversati
on
    processor.setUntaggedContentHandler(content => {
        console.log(content); 
    // Normal conversation flows

    });
    
    // Handle artifacts/special blocks
    processor.registerHandler('artifact', {
        handler: (attrs,
 content) => {
            createArtifact(attrs.type, content);
        }
    });

Works with streaming APIs out of the 
box, so you can build interactive systems that update in real-time. About 4KB, no dependencies.

Mainly sharing in case 
others want to experiment with similar systems. TypeScript and Python versions: [github repo](https://github.com/m-ahmed
-elbeskeri/FluffyTagProcessor/tree/main?tab=readme-ov-file)
```
---

     
 
all -  [ [Student] Non-Target CS Student looking for Summer 2025 Internships ](https://www.reddit.com/r/EngineeringResumes/comments/1hdpaec/student_nontarget_cs_student_looking_for_summer/) , 2024-12-17-0914
```
[I am having little luck with applying to Summer 2025 internships related to software engineering, and I've currently ap
plied to around 400 places. I know the market is pretty bad right now, but just wanted to make sure my resume was optima
l for getting me interviews, cause right now I have gotten mostly nothing from online applications \(Had an interview fr
om my school's career fair\). Any advice would be greatly appreciated.](https://preview.redd.it/qnc9d2sc7p6e1.png?width=
5100&format=png&auto=webp&s=68f0c23f6576eb216c1f4c5fdc6190e2aa9dba60)


```
---

     
 
all -  [ Modularizing AI workflows in production ](https://www.reddit.com/r/LangChain/comments/1hdm37i/modularizing_ai_workflows_in_production/) , 2024-12-17-0914
```
Wanted to share some challenges and solutions we discovered while working with complex prompt chains in production. We s
tarted hitting some pain points as our prompt chains grew more sophisticated:

* Keeping track of prompt versions across
 different chain configurations became a nightmare
* Testing different prompt variations meant lots of manual copying an
d pasting. Especially when tracking the performances.
* Deploying updated chains to production was tedious and error-pro
ne. Environment variables was fine at first until the list of prompts start to grow.
* Collaborating on prompt engineeri
ng with the team led to version conflicts.
   * We started with code verisoning it, but it was hard to loop in other sta
keholders (ex: product managers, domain experts) to do code reviews on GitHub. Notion doesn’t have a good versioning sys
tem built-in so everyone was kind of afraid to overwrite the other person’s work and ended up putting a lot of comments 
all over the place.

We ended up building a simple UI-based solution that helps us:

1. Visualize the entire prompt chai
n flow
2. Track different versions of the workflow and make them replayable.
3. Deploy the workflows as separate service
 endpoints in order to manage them programmatically in code

The biggest learning was that treating chained prompts like
 we treat workflows (with proper versioning and replayability) made a huge difference in our development speed.

Here’s 
a high-level diagram of how we modularize AI workflows from the rest of the services

https://preview.redd.it/4cwpce4uio
6e1.png?width=1612&format=png&auto=webp&s=a290f010d8605bec3e1825603e87665366e802c2

We’ve made our tool available at [ww
w.bighummingbird.com](http://www.bighummingbird.com/) if anyone wants to try it, but I’m also curious to hear how others
 are handling these challenges? :)
```
---

     
 
all -  [ Avoid sending messages at the same time ](https://www.reddit.com/r/LangChain/comments/1hdlx5e/avoid_sending_messages_at_the_same_time/) , 2024-12-17-0914
```
Hi,  
I have a graph on langgraph wrapped around a FastAPI project.  
I want to avoid sending two messages at the same t
ime to the same chat\_id through the API.  
Is there any way I can know when a thread is processing a message before sen
ding a new one?  
Thanks in advance!
```
---

     
 
all -  [ why my agent is not calling the tools  help me to fix this .. ](https://www.reddit.com/r/node/comments/1hdllox/why_my_agent_is_not_calling_the_tools_help_me_to/) , 2024-12-17-0914
```
mport dotenv from 'dotenv';  
dotenv.config();  
import { tool } from '@langchain/core/tools';  
import { z } from 'zod'
;  
import { ChatGoogleGenerativeAI } from '@langchain/google-genai';  
import { ChatPromptTemplate } from '@langchain/c
ore/prompts';  
import { AgentExecutor, createToolCallingAgent } from 'langchain/agents';  
import { TavilySearchResults
 } from '@langchain/community/tools/tavily\_search';

const llm = new ChatGoogleGenerativeAI({  
apiKey: process.env.GEM
INI,  
model: 'gemini-1.5-flash',  
});

const search = new TavilySearchResults({  
apiKey: process.env.TAVILY,  
maxRes
ults: 2,  
});

*// Improved magicTool: Now actually uses the input*  
const magicTool = tool(  
async (input) => {  
*/
/Simulate fetching company name - replace this with actual API call if needed.*

return 'The company name is Acme Corpor
ation.';  
},  
{  
name: 'business\_info',  
description:  
'This tool provides business information like name, locatio
n, etc. Ask specific questions.',  
}  
);

const tools = \[magicTool\];

const prompt = ChatPromptTemplate.fromMessages
(\[  
\[  
'system',  
'You are a helpful assistant that answers the following questions as best you can. You have acces
s to the following tools:',  
\],  
\['placeholder', '{chat\_history}'\],  
\['human', '{input}'\],  
\['placeholder', '
{agent\_scratchpad}'\],  
\]);

const agent = createToolCallingAgent({  
llm,  
tools,  
prompt,  
});

const agentexe =
 new AgentExecutor({  
agent,  
tools,  
verbose: true,  
});

const res = await agentexe.invoke({ input: 'what is the c
ompany name?' });  
console.log(res);
```
---

     
 
all -  [ why my agent is not calling the tools please help me to fix this  .. ](https://www.reddit.com/r/LangChain/comments/1hdksj8/why_my_agent_is_not_calling_the_tools_please_help/) , 2024-12-17-0914
```
import dotenv from 'dotenv';  
dotenv.config();  
import { tool } from '@langchain/core/tools';  
import { z } from 'zod
';  
import { ChatGoogleGenerativeAI } from '@langchain/google-genai';  
import { ChatPromptTemplate } from '@langchain/
core/prompts';  
import { AgentExecutor, createToolCallingAgent } from 'langchain/agents';  
import { TavilySearchResult
s } from '@langchain/community/tools/tavily\_search';  
  
const llm = new ChatGoogleGenerativeAI({  
  apiKey: process.
env.GEMINI,  
  model: 'gemini-1.5-flash',  
});  
  
const search = new TavilySearchResults({  
  apiKey: process.env.T
AVILY,  
  maxResults: 2,  
});  
  
*// Improved magicTool:  Now actually uses the input*  
const magicTool = tool(  
 
 async (input) => {  
*//Simulate fetching company name - replace this with actual API call if needed.*  
  
return 'The
 company name is Acme Corporation.';  
  },  
  {  
name: 'business\_info',  
description:  
'This tool provides busines
s information like name, location, etc.  Ask specific questions.',  
  }  
);  
  
const tools = \[magicTool\];  
  
con
st prompt = ChatPromptTemplate.fromMessages(\[  
  \[  
'system',  
'You are a helpful assistant that answers the follow
ing questions as best you can. You have access to the following tools:',  
  \],  
  \['placeholder', '{chat\_history}'\
],  
  \['human', '{input}'\],  
  \['placeholder', '{agent\_scratchpad}'\],  
\]);  
  
const agent = createToolCalling
Agent({  
  llm,  
  tools,  
  prompt,  
});  
  
const agentexe = new AgentExecutor({  
  agent,  
  tools,  
  verbos
e: true,  
});  
  
const res = await agentexe.invoke({ input: 'what is the company name?' });  
console.log(res);  
  

import dotenv from 'dotenv';  
dotenv.config();  
import { tool } from '@langchain/core/tools';  
import { z } from 'zod
';  
import { ChatGoogleGenerativeAI } from '@langchain/google-genai';  
import { ChatPromptTemplate } from '@langchain/
core/prompts';  
import { AgentExecutor, createToolCallingAgent } from 'langchain/agents';  
import { TavilySearchResult
s } from '@langchain/community/tools/tavily\_search';  
  
  
const llm = new ChatGoogleGenerativeAI({  
  apiKey: proce
ss.env.GEMINI,  
  model: 'gemini-1.5-flash',  
});  
  
  
const search = new TavilySearchResults({  
  apiKey: process
.env.TAVILY,  
  maxResults: 2,  
});  
  
  
// Improved magicTool:  Now actually uses the input  
const magicTool = to
ol(  
  async (input) => {  
//Simulate fetching company name - replace this with actual API call if needed.  
  
  
ret
urn 'The company name is Acme Corporation.';  
  },  
  {  
name: 'business\_info',  
description:  
'This tool provides
 business information like name, location, etc.  Ask specific questions.',  
  }  
);  
  
  
const tools = \[magicTool\
];  
  
  
const prompt = ChatPromptTemplate.fromMessages(\[  
  \[  
'system',  
'You are a helpful assistant that answ
ers the following questions as best you can. You have access to the following tools:',  
  \],  
  \['placeholder', '{ch
at\_history}'\],  
  \['human', '{input}'\],  
  \['placeholder', '{agent\_scratchpad}'\],  
\]);  
  
  
const agent = 
createToolCallingAgent({  
  llm,  
  tools,  
  prompt,  
});  
  
{  
  input: 'what is the company name?',  
  output
: 'I need more information to answer your question.  The available tools don't contain any information about a specific 
company.  Can you provide more context or details?\\n'  
}  
const agentexe = new AgentExecutor({  
  agent,  
  tools, 
 
  verbose: true,  
});  
  
  
const res = await agentexe.invoke({ input: 'what is the company name?' });  
console.lo
g(res);  
  
the output is  ::   
 {  
  input: 'what is the company name?',  
  output: 'I need more information to ans
wer your question.  The available tools don't contain any information about a specific company.  Can you provide more co
ntext or details?\\n'  
}
```
---

     
 
all -  [ why my agent is not calling the tools please help me to fix this  ,  ](https://www.reddit.com/r/Bard/comments/1hdkqi8/why_my_agent_is_not_calling_the_tools_please_help/) , 2024-12-17-0914
```
    import dotenv from 'dotenv';
    dotenv.config();
    import { tool } from '@langchain/core/tools';
    import { z }
 from 'zod';
    import { ChatGoogleGenerativeAI } from '@langchain/google-genai';
    import { ChatPromptTemplate } fro
m '@langchain/core/prompts';
    import { AgentExecutor, createToolCallingAgent } from 'langchain/agents';
    import { 
TavilySearchResults } from '@langchain/community/tools/tavily_search';
    
    const llm = new ChatGoogleGenerativeAI({

      apiKey: process.env.GEMINI,
      model: 'gemini-1.5-flash',
    });
    
    const search = new TavilySearchResu
lts({
      apiKey: process.env.TAVILY,
      maxResults: 2,
    });
    
    // Improved magicTool:  Now actually uses 
the input
    const magicTool = tool(
      async (input) => {
        
    //Simulate fetching company name - replace t
his with actual API call if needed.
    
        return 'The company name is Acme Corporation.';
      },
      {
      
  name: 'business_info',
        description:
          'This tool provides business information like name, location, et
c.  Ask specific questions.',
      }
    );
    
    const tools = [magicTool];
    
    const prompt = ChatPromptTempl
ate.fromMessages([
      [
        'system',
        'You are a helpful assistant that answers the following questions a
s best you can. You have access to the following tools:',
      ],
      ['placeholder', '{chat_history}'],
      ['huma
n', '{input}'],
      ['placeholder', '{agent_scratchpad}'],
    ]);
    
    const agent = createToolCallingAgent({
   
   llm,
      tools,
      prompt,
    });
    
    const agentexe = new AgentExecutor({
      agent,
      tools,
     
 verbose: true,
    });
    
    const res = await agentexe.invoke({ input: 'what is the company name?' });
    console.
log(res);
    
    import dotenv from 'dotenv';
    dotenv.config();
    import { tool } from '@langchain/core/tools';
 
   import { z } from 'zod';
    import { ChatGoogleGenerativeAI } from '@langchain/google-genai';
    import { ChatPromp
tTemplate } from '@langchain/core/prompts';
    import { AgentExecutor, createToolCallingAgent } from 'langchain/agents'
;
    import { TavilySearchResults } from '@langchain/community/tools/tavily_search';
    
    
    const llm = new Chat
GoogleGenerativeAI({
      apiKey: process.env.GEMINI,
      model: 'gemini-1.5-flash',
    });
    
    
    const sear
ch = new TavilySearchResults({
      apiKey: process.env.TAVILY,
      maxResults: 2,
    });
    
    
    // Improved 
magicTool:  Now actually uses the input
    const magicTool = tool(
      async (input) => {
        //Simulate fetching
 company name - replace this with actual API call if needed.
    
    
        return 'The company name is Acme Corporat
ion.';
      },
      {
        name: 'business_info',
        description:
          'This tool provides business infor
mation like name, location, etc.  Ask specific questions.',
      }
    );
    
    
    const tools = [magicTool];
    

    
    const prompt = ChatPromptTemplate.fromMessages([
      [
        'system',
        'You are a helpful assistan
t that answers the following questions as best you can. You have access to the following tools:',
      ],
      ['place
holder', '{chat_history}'],
      ['human', '{input}'],
      ['placeholder', '{agent_scratchpad}'],
    ]);
    
    
 
   const agent = createToolCallingAgent({
      llm,
      tools,
      prompt,
    });
    
    {
      input: 'what is
 the company name?',
      output: 'I need more information to answer your question.  The available tools don't contain 
any information about a specific company.  Can you provide more context or details?\n'
    }
    const agentexe = new Ag
entExecutor({
      agent,
      tools,
      verbose: true,
    });
    
    
    const res = await agentexe.invoke({ i
nput: 'what is the company name?' });
    console.log(res);
    
    the output is  :: 
     {
      input: 'what is the
 company name?',
      output: 'I need more information to answer your question.  The available tools don't contain any 
information about a specific company.  Can you provide more context or details?\n'
    }
```
---

     
 
all -  [ Advance Your Career: 100 Free Certified Courses on Udemy ](https://www.reddit.com/r/Udemy/comments/1hdjv70/advance_your_career_100_free_certified_courses_on/) , 2024-12-17-0914
```
Visualization techniques for Decision Makers and Leaders

https://courze.org/visualization-techniques-for-decision-maker
s-and-leaders/



300+ JavaScript Interview Questions – Practice Tests

https://courze.org/300-javascript-interview-ques
tions-practice-tests/



300+ Python Interview Questions – Practice Tests

https://courze.org/300-python-interview-quest
ions-practice-tests/



Scrum Master Certification

https://courze.org/scrum-master-certification-4/



Business Analysi
s

https://courze.org/business-analysis/



C Corporation Income Tax (Form 1120)

https://courze.org/c-corporation-incom
e-tax-form-1120/



Zero to Hero in LangChain: Build GenAI apps using LangChain

https://courze.org/zero-to-hero-in-lang
chain-build-genai-apps-using-langchain/



Blogger: Make A Professional Website For Free With No Coding

https://courze.
org/blogger-make-a-professional-website-for-free-with-no-coding/



Solving LeetCode’s Top Interview Questions in Java \
[2024\]

https://courze.org/solving-leetcodes-top-interview-questions-in-java/



4 Comprehensive Practice Tests for any
 Python Certification

https://courze.org/4-comprehensive-practice-tests-for-any-python-certification/



Excel Certific
ation Exam Preparation: 4 Practice Tests 2024

https://courze.org/excel-certification-exam-preparation-4-practice-tests-
2024-3/



4 MS Excel Certification Practice Test & Interview Question

https://courze.org/4-ms-excel-certification-prac
tice-test-interview-question/



CHRO Chief Human Resources Officer Executive Certification

https://courze.org/chro-chi
ef-human-resources-officer-executive-certification/



Prioritization Techniques for Decision Makers and Leaders

https:
//courze.org/prioritization-techniques-for-decision-makers-and-leaders/



The Complete Matlab Course for Wireless Comm.
 Engineering

https://courze.org/the-complete-matlab-course-for-wireless-comm-engineering/



Currency Management for Sm
all Businesses & Corporates

https://courze.org/currency-management-for-small-businesses-corporates/



Statistics & Exc
el

https://courze.org/statistics-excel/



Prompt & AI Engineering Safety Professional Certification

https://courze.or
g/prompt-engineering-safety-ai-engineering-safety-expert/



ChatGPT Prompt Engineering Guide: Make Money Using ChatGPT


https://courze.org/chatgpt-prompt-engineering-guide-make-money-using-chatgpt/



AI Course Creation Guide: Creating an 
Online Course Using AI

https://courze.org/ai-course-creation-guide-creating-an-online-course-using-ai/



Advanced Skil
l Test: Python Professional Level 1 (PCPP1™)

https://courze.org/advanced-skill-test-python-professional-level-1-pcpp1-2
/



Advanced Skill Test: Python Professional Level 1 (PCPP1™)

https://courze.org/advanced-skill-test-python-profession
al-level-1-pcpp1-7/



Advanced Skill Test: Python Professional Level 1 (PCPP1™)

https://courze.org/advanced-skill-test
-python-professional-level-1-pcpp1-9/



Advanced Skill Test: Python Professional Level 1 (PCPP1™)

https://courze.org/a
dvanced-skill-test-python-professional-level-1-pcpp1-10/



Advanced Skill Test: Python Professional Level 1 (PCPP1™)

h
ttps://courze.org/advanced-skill-test-python-professional-level-1-pcpp1-12/



Advanced Skill Test: Python Professional 
Level 1 (PCPP1™)

https://courze.org/advanced-skill-test-python-professional-level-1-pcpp1-15/



7 steps to entrepreneu
rship: A complete business plan (PRO)

https://courze.org/7-steps-to-entrepreneurship-a-complete-business-plan-pro/



A
utoCAD 2D & Isometric | AutoCAD Civil & Architectural

https://courze.org/autocad-2d-isometric-autocad-civil-architectur
al/



Microsoft Power BI for Beginners & Excel Users

https://courze.org/microsoft-power-bi-for-beginners-excel-users/




CMO Chief Marketing Officer Executive Certification

https://courze.org/cmo-chief-marketing-officer-executive-certifi
cation/



Transform Your Life in 5 Days: I Challenge You to Fail

https://courze.org/transform-your-life-in-5-days-i-ch
allenge-you-to-fail/



Mastering Power BI Report Design – Beginner to Advanced

https://courze.org/mastering-power-bi-r
eport-design-beginner-to-advanced/



Practical Machine Learning for Data Scientists

https://courze.org/practical-machi
ne-learning-for-data-scientists/



Generative AI: Learn about the next AI frontier

https://courze.org/generative-ai-le
arn-about-the-next-ai-frontier/



Master LCD Interfacing with Arduino: From Basics to Projects

https://courze.org/mast
er-lcd-interfacing-with-arduino-from-basics-to-projects/



Deployment of Machine Learning Models

https://courze.org/de
ployment-of-machine-learning-models/



Reinforcement Learning

https://courze.org/reinforcement-learning/



Deep Learn
ing for Computer Vision

https://courze.org/deep-learning-for-computer-vision/



Deep Learning for Natural Language Pro
cessing

https://courze.org/deep-learning-for-natural-language-processing/



Oracle Java Certification Exam OCA 1Z0-808
 Preparation Part1

https://courze.org/oracle-java-certification-exam-oca-1z0-808-preparation-part1/




```
---

     
 
MachineLearning -  [ [P] Minima: local conversational retrieval augmented generation project (Ollama, Langchain, FastAPI, ](https://www.reddit.com/r/MachineLearning/comments/1h1pudq/p_minima_local_conversational_retrieval_augmented/) , 2024-12-17-0914
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

     
