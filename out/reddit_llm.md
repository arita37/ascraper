 
all -  [ Why is my resume not getting me any interviews for NG roles? ](https://i.redd.it/liq2nd2sctsd1.png) , 2024-10-05-0912
```

```
---

     
 
all -  [ Should I use an agentic framework to build multi-agent infrastructure. ](https://www.reddit.com/r/LocalLLaMA/comments/1fw8dwx/should_i_use_an_agentic_framework_to_build/) , 2024-10-05-0912
```
I want to build a llm-application, but IDK if I should use something like langchain (or an alternative) vs writing my ow
n AI agents, and tools. What would be better in your opinions? And how should I go about it??


```
---

     
 
all -  [ Why is it not standard for OpenAI and other libraries to offer API reference docs in an AI-friendly  ](https://www.reddit.com/r/OpenAI/comments/1fw7vta/why_is_it_not_standard_for_openai_and_other/) , 2024-10-05-0912
```
**Edit:** I misspoke, and it's really the *library reference* (for me, `openai-python`) that I want this for.

Seriously
, how hard would it be to go at least some of the way down this list?

----

**Zero:** <-- Somehow, this is where we are
 now.

1. Provide the full library reference in a single markdown document.
2. Semantically split into chunks.
3. Togeth
er with embeddings.
4. Along with a really simple LangChain snippet that lets you chat with it.
5. Hosted on their websi
te. (You could bring your own API key, the project wouldn't have to pay.)
```
---

     
 
all -  [ How to access modules in other parts of the repo when dynamically loading? ](https://www.reddit.com/r/learnpython/comments/1fw6kvr/how_to_access_modules_in_other_parts_of_the_repo/) , 2024-10-05-0912
```
Hi all, got a bit of a conundrum here trying to get dynamic module loading with importlib to work properly 

I have the 
following package structure:

    my_project/
    ├── __init__.py
    ├── llm_provider/
    │   ├── __init__.py
    │   
└── base_client.py (class BaseLLMProvider)
    ├── agents/
    │   ├── __init__.py
    │   ├── base_agent.py
    │   └──
 basic_math_agent/
    │       ├── __init__.py
    │       └── agent.py
    └── supervisor/
        ├── __init__.py
    
    └── agent_manager.py

`agent_manager` attempts to dynamically load `basic_math_agent` using `importlib`, which works
 fine. However, `basic_math_agent` has a standard import statement of `from llm_provider.base_client import BaseLLMProvi
der`. This import fails, because as far as I am able to discern when using `importlib` to dynamically load a module, it 
does not share the same project root as the rest of the project, so `basic_math_agent` is unable to see `llm_provider`.


I receive this error:

    2024-10-04 10:33:50,288 [INFO] Starting Supervisor...
    2024-10-04 10:33:50,288 [INFO] Sea
rching for agents in directory: /home/user/personal/my_project/supervisor/../agents
    2024-10-04 10:33:50,288 [INFO] T
rying to import agent from directory: basic_math_agent
    2024-10-04 10:33:50,746 [ERROR] Error importing agent from 'b
asic_math_agent': cannot import name 'BaseLLMProvider' from 'llm_provider.base_client' (/home/user/personal/my_project/l
lm_provider/base_client.py)

In `my_project/__init__.py`, I try to update the sys root path to include the project root 
as I've seen suggested elsewhere, but it doesn't seem to work.

    import os
    import sys

    project_root = os.path
.dirname(os.path.abspath(__file__))
    sys.path.append(project_root)

Any suggestions on what best practice is here or 
how I can go about solving this?

For additional reference, here are the relevant snippets of code:

`llm_provider/base_
client.py`

    from pydantic import ValidationError, BaseModel
    class BaseLLMClient(BaseModel):

`agents/base_agent.
py`

    from abc import abstractmethod
    from typing import Any, Dict, Optional
    from langchain.agents import Agen
tType
    from llm_provider.base_client import BaseLLMClient
    from langchain.tools import BaseTool
    from superviso
r.llm_registry import LLMRegistry, LLMType
    from shared_tools.message_bus import MessageBus

    class BaseAgent:
   
     def __init__(self, llm_registry: LLMRegistry, message_bus: MessageBus, config: Optional[Dict] = None):
            
self.llm_registry = llm_registry
            self.config = config or {}
            self.state = None
            self.v
ersion = None
            self.message_bus = None

`agents/basic_math_agent/agent.py`

    from typing import Any, Dict,
 Optional
    from agents.base_agent import BaseAgent
    from langchain.tools import BaseTool
    from llm_provider.bas
e_client import BaseLLMClient
    from supervisor.llm_registry import LLMRegistry, LLMType
    from .tools.basic_math_to
ol import BasicMathTool, BasicMathInput, BasicMathOutput

    class BasicMathAgent(BaseAgent):
        def __init__(self
, llm_registry: LLMRegistry, message_bus: MessageBus, config: Optional[Dict] = None):
            super().__init__(llm_r
egistry, message_bus, config)
            self.tool = BasicMathTool(llm_registry.get_llm(LLMType.DEFAULT))

`supervisor/
agent_manager.py`

    def register_agents(self):
        try:
            agents_dir = Path(os.path.join(os.path.dirnam
e(__file__), '..', 'agents'))
            logger.info(f'Searching for agents in directory: {agents_dir}')

            #
 Add the project root to the Python path
            project_root = os.path.join(agents_dir.parent.resolve())
          
  sys.path.append(project_root)

            # Add the subdirectories to the Python path
            subdirs = [os.path.
join(project_root, d) for d in os.listdir(project_root) if os.path.isdir(os.path.join(project_root, d))]
            for
 subdir in subdirs:
                sys.path.append(subdir)

            for agent_dir in agents_dir.iterdir():
        
        if agent_dir.is_dir() and not agent_dir.name.startswith('_'):
                    logger.info(f'Trying to import
 agent from directory: {agent_dir.name}')
                    try:
                        agent_module = importlib.impo
rt_module(f'agents.{agent_dir.name}.agent')
                        agent_classes = [cls for cls in agent_module.__dict_
_.values() if isinstance(cls, type) and issubclass(cls, BaseAgent) and cls != BaseAgent]
                        if not 
agent_classes:
                            logger.warning(f'Skipping agent directory '{agent_dir.name}' as it does not c
ontain a valid agent class.')
                            continue

                        logger.info(f'Found {len(age
nt_classes)} agent classes in {agent_dir.name}')
                        for agent_class in agent_classes:
             
               try:
                                logger.info(f'Trying to register agent: {agent_class.__name__}')
   
                             agent_config_file = agent_dir / 'config.yaml'
                                if agent_conf
ig_file.exists():
                                    logger.info(f'Loading config from {agent_config_file}')
          
                          with open(agent_config_file, 'r') as f:
                                        agent_config =
 yaml.safe_load(f)
                                else:
                                    logger.info(f'No config fil
e found for {agent_class.__name__}, using default config.')
                                    agent_config = {}

     
                           agent = agent_class(self.config.llm_client_factory, self.message_bus, **agent_config.get('con
fig', {}))
                                self.register_agent(agent)
                                logger.info(f'Succ
essfully registered agent: {agent_class.__name__}')
                            except Exception as e:
                 
               logger.error(f'Error registering agent '{agent_class.__name__}' from '{agent_dir.name}': {e}')
          
          except Exception as e:
                        logger.error(f'Error importing agent from '{agent_dir.name}': {
e}')
                else:
                    logger.debug(f'Skipping directory {agent_dir.name} as it is not a directo
ry or starts with an underscore.')
        except Exception as e:
            logger.error(f'Error registering agents: {
e}')
```
---

     
 
all -  [ Advanced LLM parsing is the key to advanced AI applications. ](https://www.reddit.com/r/datascience/comments/1fw5k23/advanced_llm_parsing_is_the_key_to_advanced_ai/) , 2024-10-05-0912
```
In my experience, when people consider applying LLMs to a project they often fall into two camps:

1. they turn the proj
ect into a chat bot
2. they use an LLM for some key feature in a larger application, resulting in an error prone mess

t
here's tremendous power in using LLMs to power specific features within larger applications, but LLMs inconsistency in o
utput structure makes it difficult to use their output within a programmatic system. You might ask an llm to output JSON
 data, for instance, and the LLM decides it's appropriate to wrap the data in a `\`\`\`json \`\`\`` markdown format. you
 might ask an LLM to output a list of values, and it responds with something like this:

    here's your list
    [1,2,3
,4]

There's an infinite number of ways LLM output can go wrong, which is why output parsing is a thing.

I've had the b
est luck, personally, with LangChain in this regard. [LangChain's pydantic parser](https://python.langchain.com/docs/how
_to/output_parser_structured/) allows one to define an object which is either constructed from the LLMs output, or an er
ror gets thrown. They essentially use a clever prompting system paired with the user's defined structure to coax the mod
el into a consistent output.

That's not fool proof either, which is why it's a common practice to either re-try or re-p
rompt. You can either just re-prompt on a failure, or pass the response which failed to parse to the LLM again and ask t
he LLM to correct it's mistake. For robust LLMs this works consistently enough where it's actually viable in application
s (assuming proper error handling). I made a post about [LangGraph](https://www.reddit.com/r/datascience/comments/1fknby
i/langgraph_allows_you_to_make_falsifiable_testable/) recently, this can also be used to construct complex loops/decisio
ns which can be useful for adding a level of robustness into LLM responses.

If you can learn how to consistently turn a
n LLMs output into JSON, there's a whole world of possible applications.

I'm curious what LLM parsing tricks you employ
, and what you've seen the most success with!
```
---

     
 
all -  [ a way to chunk large txt file or HTML ](https://www.reddit.com/r/LangChain/comments/1fw2125/a_way_to_chunk_large_txt_file_or_html/) , 2024-10-05-0912
```
Hi

I have a large text file (approximately 1 million words) and an HTML version of it. Each page ends with a unique key
word indicating a page break. I need a way to automatically split the text into chunks based on these keywords and then 
send each chunk to Claude for translation into English.

any ideas folks?
```
---

     
 
all -  [ Postgresql Checkpointer on LangGraphJS ](https://www.reddit.com/r/LangChain/comments/1fw0ifo/postgresql_checkpointer_on_langgraphjs/) , 2024-10-05-0912
```
I am doing some research and initial setup for implementing an agentic system on a large production application and am t
rying to find information on whether the Postgresql checkpointing system is currently implemented for LangGraphJS. 

I c
ame across this discussion, https://github.com/langchain-ai/langgraph/discussions/1796 - so I wanted to ask for some cla
rification and to see if anyone can maybe point me in the right direction as far as documentation goes, etc.. 

Thanks!
```
---

     
 
all -  [ Need resource for RAG agent in LangGraph ](https://www.reddit.com/r/LangChain/comments/1fvzoh6/need_resource_for_rag_agent_in_langgraph/) , 2024-10-05-0912
```
I am looking to build rag agent in Langgraph, so if anyone has resources or learning material apart from official docume
ntion then please share it. 
```
---

     
 
all -  [ I created a discord server to discuss agentic systems engineering ](https://www.reddit.com/r/LangChain/comments/1fvz82r/i_created_a_discord_server_to_discuss_agentic/) , 2024-10-05-0912
```
Hey guys, I created a discord channels for developers building AI agents (using any framework or none). Join if you're i
nterested in learning and sharing with the community: [https://discord.gg/nRgm5DbH](https://discord.gg/nRgm5DbH)
```
---

     
 
all -  [ Using ChatOpenAI with LangGraph.js to Build a Personal Assistant AI Agent ](https://www.reddit.com/r/LangChain/comments/1fvyhb9/using_chatopenai_with_langgraphjs_to_build_a/) , 2024-10-05-0912
```
Made a beginner guide on how to use LangGraph and ChatGpt to create an AI Agent that acts as a personal assistant 👉 [htt
ps://www.js-craft.io/blog/chatopenai-langgraph-js-ai-agent/](https://www.js-craft.io/blog/chatopenai-langgraph-js-ai-age
nt/)

Please let me know your thoughts :) 
```
---

     
 
all -  [ Speaker Diarization for audio with multiple languages ](https://www.reddit.com/r/LangChain/comments/1fvvr5r/speaker_diarization_for_audio_with_multiple/) , 2024-10-05-0912
```
I have a call record with two people speaking in combination of languages like english, telugu and hindi. How to diarize
 it. I tried pyannote models available in the huggingface. It's not working well and I'm not getting any accurate result
s. What are the available options and how to proceed further
```
---

     
 
all -  [ advice from people working in tech from early 2000 ](https://www.reddit.com/r/codingbootcamp/comments/1fvvfhk/advice_from_people_working_in_tech_from_early_2000/) , 2024-10-05-0912
```
guys as someone with 15+ yoe, I want to ask others who have experience, what advice would you give to the young new grad
s and those who are looking into the SWE and data careers?   
  
From my point of view:  I want to say that it's not wor
th pursuing careers in software or data analytics anymore, the AI crushing it, I can replace 5-6 people in current busin
ess that I work in, using Cursor Composer and Aider connected to sonnet3.5, and soon the o1 models will get upgraded to 
real gpt5 which will nail the multi-file editing better than sonnet and opus which are already amazing, these 2 years ar
e the last years of '6 figures' wages in tech, this is why: the number of businesses, existing and upcoming, is limited,
 and it will not grow all of a sudden to a x5 demand (x5 number of businesses need to appear), while the reduction in re
quired head count of software and data peeps goes down x5 if not x10 (if we consider upcoming gpt5 and new anthropic rel
eases in the next 2 years and link it into agents like [crew.ai](http://crew.ai/) and self written langchain (business s
pecific agents) the headcount required to deliver the business goals goes down x10 easily, WHILE universities are still 
full of upcoming SWEs and AI/ML data scientists, who are students now, and they'll be in the market too (in addition to 
all self-taught folks from east europe, latam, asia, and their uni of course, who are looking for remote work) it's goin
g to be a bloodbath, I can already hire engineers for 2-3k euro in Poland, Serbia, Asia, India, Mexico, who were until r
ecently non-existent (before covid we had not much practice of such massive outsourcing as we do now, at the moment ever
y business looking to cut costs and opens offices in Belgrade and Bucharest etc'). 

The big tech swims in money so they
'll keep paying 6 figures for a while, to the most experienced leads and seniors, staff, directors, but it'll go down to
 'back to reality' rates which are below 6 figures in the next 5-6 years as well, and the competition for the roles is a
lready fierce. If you want to work routinely 10-12 hours a day, PLUS keep yourself up to date on latest tech and in good
 shape of algorithms (add 2-3 hours a week to keep yourself in shape) this career is for you, BUT high rates are no long
er guaranteed for folks who want a quiet 9-5 office job. the more hardcore nerds like me, who have no life, no kids, no 
hobbies, will keep the high paying jobs, but this shit is not for regular healthy people, so my sincere advice for young
 folks would be to stay away from SWE and try hardware networking, chip manufacturing, biology, space sciences, aerospac
e (probably best niche in upcoming future), defense (obviously, but take care of karma so you don't end up in hell lol, 
not worth the 6 figures), microbiology, medicine, ocean stuff, oil and gas and geo sciences maybe, agriculture science i
n upcoming climate change might be good direction too since there's a lot of trouble in the sector that needs fixing, an
d so on. just my sincere 2 cents :)))

I hope this will help someone to make a good decision in life, you're welcome to 
disagree and I know I might be completely wrong and 'new businesses and new use cases for SWEs will get created in the u
pcoming golden age of AI' theory of the youtubers exists ('influencers' :D the ones who can't make $$ in tech and become
 youtubers to make ends meet, they aren't the best ones to listen to honestly, I'm sorry guys. but just think about it, 
we're dying in tech jobs with 10-12 hour shifts already, who of us in a sane mind will be a youtube influencer in our fr
ee time, for 5$ per 10000 views or smth? when our rates are 100-120$/hour at work, why would we do youtube?? don't liste
n to these dummies, they're on youtube cos the job is too hard for them anyway).

Take care! 
```
---

     
 
all -  [ Hybrid retrieval on Postgres - (sub)second latency on ~30M documents ](https://www.reddit.com/r/LangChain/comments/1fvunhv/hybrid_retrieval_on_postgres_subsecond_latency_on/) , 2024-10-05-0912
```
We had been looking for open source ways to scale out our hybrid retrieval in Langchain beyond the capability of the def
ault Milvus/FAISS vector store with the default in-memory BM25 indexing but we couldn't find any proper alternative.

Th
at's why we have implemented this ourselves and are now releasing it for others to use:

* Dense vector embedding search
 on Postgres through pgvector
* Sparse BM25 search on Postgres through ParadeDB's pg\_search
   * A custom retriever for
 the BM25 search
* 1 Dockerfile that spins up a Postgres facilitating both

We have benchmarked this on a dataset loadin
g just shy of 30M chunks into Postgres with a hybrid search using BM25 and vector search and have achieved (sub)second r
etrieval times.

Check it out: [https://github.com/AI-Commandos/RAGMeUp/blob/main/README.md#using-postgres-adviced-for-p
roduction](https://github.com/AI-Commandos/RAGMeUp/blob/main/README.md#using-postgres-adviced-for-production)
```
---

     
 
all -  [ RAG Tabular Type Data ](https://www.reddit.com/r/Rag/comments/1fvtfr2/rag_tabular_type_data/) , 2024-10-05-0912
```
I want to create a Chroma Vector Store using Langchain from pdf documents, but what's happening is that my pdf contain s
ome tabular data, now when I am querying AI model for table data, It is not able to identify it. 

So is there any techn
ique or library for reading tabular data perfectly in order to create vector store
```
---

     
 
all -  [ Real estate llm ](https://www.reddit.com/r/LangChain/comments/1fvt4d3/real_estate_llm/) , 2024-10-05-0912
```
Has anybody has any idea how to build a real estate llm which scans through various real estate listings in real time an
d notify the user about the listing if it is profitable investment. I have not much experience in langchain can anyone t
ell me is it possible 
```
---

     
 
all -  [ What are some hobby projects that you've built with langchain? ](https://www.reddit.com/r/LangChain/comments/1fvqjpu/what_are_some_hobby_projects_that_youve_built/) , 2024-10-05-0912
```
I'm looking to build some hobby projects with LangChain. Wondering if anyone has any beginner-intermediate project ideas
 using LangChain that would be fun to build.
```
---

     
 
all -  [ AI Agent Marketplaces ](https://www.reddit.com/r/LangChain/comments/1fvj04p/ai_agent_marketplaces/) , 2024-10-05-0912
```
We're seeing a rising trend in companies trying to build AI agent marketplaces. I think it'll only be a few more months 
until someone figures out how to do it at scale. What do you guys think will be the most important features on these mar
ketplaces that will make them beneficial for creators?
```
---

     
 
all -  [ How to create a manual LLM chain for Conservational RAG? ](https://www.reddit.com/r/LangChain/comments/1fvf9vw/how_to_create_a_manual_llm_chain_for/) , 2024-10-05-0912
```
It might be a noob question, I want to create a llm chain something like

llm | chat\_history | prompt | documents

I'm 
separately retrieving the documents from vectorstore, and filtering the retrieved documents based on my own logic for my
 usecase, and only the filtered documents I want to pass to my llm for generating response and keeping chat\_history (I'
m aware of create\_stuff\_document and history\_aware\_retriever approach for conservational RAG, but in that approach I
 can't use my manual document filtering)

EDIT- I FIGURED IT ABOUT

    chat_history = []
    
    documents = [] # or a
ny other document coming from different function
    
    prompt = ChatPromptTemplate.from_messages([
        ('system',
 '''You are a Helpful Assistant
            You will consider the provided context as well. <context> {context} </contex
t>'''),
        MessagesPlaceholder(variable_name='chat_history'),
        ('human', '{input}')
        ])
    
    rag_
chain = (
        {
            'input': lambda x: x['input'],
            'context': lambda x: documents,
            '
chat_history': lambda x: x['chat_history'],
        }
        | prompt
        | llm
        | StrOutputParser()
    )
 
   
    chain = RunnablePassthrough.assign(context=lambda x: documents, chat_history=lambda x: x['chat_history']).assign
(
        answer=rag_chain
    )
    
    while True:
        user_input = input()
        if user_input in {'q', 'Q'}:

            break
        response = chain.invoke({'input': user_input, 'chat_history': chat_history})
        print(res
ponse)
        chat_history.append(HumanMessage(content=user_input))
        chat_history.append(AIMessage(content=respo
nse['answer']))  
    
    
```
---

     
 
all -  [ text-embedding-004 from Gemini is not available on LangChain ](https://www.reddit.com/r/LangChain/comments/1fvf4hk/textembedding004_from_gemini_is_not_available_on/) , 2024-10-05-0912
```
I am trying to use Gemini's [text-embedding-004](https://ai.google.dev/gemini-api/docs/embeddings) model in LangChain ho
wever LangChain only supports text-embedding-001 according to this [doc](https://python.langchain.com/docs/integrations/
text_embedding/google_generative_ai/). I tried to change 001 to 004 but it returns error saying that the model is not su
pported. I am just curious why LangChain only supports 001, which is not mentioned anywhere in the current doc of Google
.
```
---

     
 
all -  [ Langfuse vs Helicone for prompt managing and experimentation. ](https://www.reddit.com/r/LangChain/comments/1fv8bcj/langfuse_vs_helicone_for_prompt_managing_and/) , 2024-10-05-0912
```
Those two services seem to be the most advanced and actively developed solutions for this. I am not sure which way to go
, especially since Langfuse's architecture will soon be very similar than that of Helicone's, see [https://github.com/or
gs/langfuse/discussions/1902](https://github.com/orgs/langfuse/discussions/1902) . The pricing of the non-self hosted ve
rsions are quite comparable, however it seems that Helicone does offer model output caching, which means it pays basical
ly by itself for our use case. On the other hand Langfuse seems to have a more comprehensive documentation and more self
 hosted centric development, not entirely sure.

What are your experiences using one of those services? Can you recommen
d one or another similar tool?
```
---

     
 
all -  [ Help me prioritize my tech stack. ](https://www.reddit.com/r/developersPak/comments/1fv7oo5/help_me_prioritize_my_tech_stack/) , 2024-10-05-0912
```
I want to learn

-Advance React
-Redux


-Node.Js
-Express.Js
-MongoDb
-MySQL

-nextJS

-Gsap
-Three.js
-Famermotion

-G
raphQl

-Socket.io
-WebRtc
-WebGL

-TypeScript

-Jenkins
-Docker
-Kubernetes

-Langchain.js
-Rag

I just have one year l
eft then I have to start working in my FYP project. Prioritize this which are most most important in an order.
My goal i
s to become a full stack expert developer and it is a dream.
```
---

     
 
all -  [ Has anyone gotten Langchain RetirevalQA to work with ChatAnthropic? ](https://www.reddit.com/r/LangChain/comments/1fv7k4w/has_anyone_gotten_langchain_retirevalqa_to_work/) , 2024-10-05-0912
```
I developed my application with OpenAI RAG and sold huge things to the business on how our arch can switch between Claud
e and GPT on runtime. 

The only problem is I am getting issues like 'Cant Instantiate BaseLanguageModel without impleme
ntation to abstract methods like agenerate_prompt'. I have made no changes, just using VoyageAI and new langchain_anthro
pic package to use claude-3.5. Unable to understand where this issue is. 

Any help, code references or versions of Lang
chain packages where people have made this work would be greatly appreciated! 
```
---

     
 
all -  [ AI-Powered RFP Document Comparison and Gap Analysis with Interactive Chat (openai,llamaindex,langcha ](https://www.reddit.com/r/OpenAI/comments/1fv4i0m/aipowered_rfp_document_comparison_and_gap/) , 2024-10-05-0912
```
Hey everyone! 👋

I've been working on this cool little web app called RFP Analyzer. It's basically a tool that helps you
 break down Request for Proposal (RFP) documents and your responses to them. Super handy if you're dealing with a lot of
 these in your work!

[video screen recording of the rfp analyzer tool in action](https://reddit.com/link/1fv4i0m/video/
jofsq8inpisd1/player)

**What it does:**

* You upload your RFP and response PDFs
* It processes them and gives you a ne
at summary
* You can chat with an AI about the documents, so you can also use it to validate if your actually capturing 
the data from the document correctly
* It generates a report comparing the two

**UI using web tech (Flask, HTMX, Alpine
.js).**

[Ui of the RFP Analyzer ](https://preview.redd.it/aany534goisd1.png?width=2880&format=png&auto=webp&s=b8e913a5b
c761868a904636c9bb6da467822701a)

I will soon open-sourced it on GitHub, so feel free to check it out, star it, or even 
contribute if you're feeling generous! Feel free to ask questions :)

[https://github.com/lesteroliver911/openai-rfp-res
ponse-analyzer](https://github.com/lesteroliver911/openai-rfp-response-analyzer)
```
---

     
 
all -  [ Llama 3.2: A brief analysis of vision capabilities ](https://www.reddit.com/r/LangChain/comments/1fv4i0d/llama_32_a_brief_analysis_of_vision_capabilities/) , 2024-10-05-0912
```
Thanks to the open-source gods! Meta finally released the multi-modal language models. There are two models: a small 11B
 one and a mid-sized 90B one.

The timing couldn't be any better, as I was looking for an open-access vision model for a
n application I am building to replace GPT4o.

So, I wanted to know if I can supplement GPT4o usage with Llama 3.2; thou
gh I know it’s not a one-to-one replacement, I expected it to be good enough considering Llama 3 70b performance, and it
 didn’t disappoint.

I tested the model on various tasks that I use daily,

* General Image Understanding
   * Image cap
tioning
   * counting objects
   * identifying tools
   * Plant disease identification
* Medical report analysis
* Text 
extraction
* Chart analysis

Consider going through this article to dive deeper into the tests. [Meta Llama 3.2: A deep 
dive into vision capabilities.:](https://composio.dev/blog/meta-llama-3-2-a-deep-dive-into-vision-capabilities/)

# What
 did I feel about the model?

The model is great and, indeed, a great addition to the open-source pantheon. It is excell
ent for day-to-day use cases, and considering privacy and cost, it can be a potential replacement for GPT-4o for this ki
nd of task.

However, GPT-4o is still better for difficult tasks, such as medical imagery analysis, stock chart analysis
, and similar tasks.

I have yet to test them for getting the coordinates of objects in an image to create bounding boxe
s. If you have done this, let me know what you found.

Also, please comment on how you liked the model’s vision performa
nce and what use cases you plan on using it for.
```
---

     
 
all -  [ Stock Insights with AI Agent-Powered Analysis With Lyzr Agent API ](https://www.reddit.com/r/LangChain/comments/1fv47sq/stock_insights_with_ai_agentpowered_analysis_with/) , 2024-10-05-0912
```
Hi everyone! I've just created an app that elevates stock analysis by integrating FastAPI and Lyzr Agent API. Get real-t
ime data coupled with intelligent insights to make informed investment decisions. Check it out and let me know what you 
think!

Blog: [https://medium.com/@harshit\_56733/step-by-step-guide-to-build-an-ai-stock-analyst-with-fastapi-and-lyzr-
agent-api-9d23dc9396c9](https://medium.com/@harshit_56733/step-by-step-guide-to-build-an-ai-stock-analyst-with-fastapi-a
nd-lyzr-agent-api-9d23dc9396c9)
```
---

     
 
all -  [ Few shot learning with tool usage ](https://www.reddit.com/r/LangChain/comments/1fv44ld/few_shot_learning_with_tool_usage/) , 2024-10-05-0912
```
Hello,

I'm building an agent using Claude 3.5 Sonnet as LLM. Does anyone have experience with few shot learning that in
volves tool usage? How should I format the examples? Thank you!
```
---

     
 
all -  [ Paid internship test  ](https://i.redd.it/0uq2o1qbiisd1.png) , 2024-10-05-0912
```
Tommorow i got my paid internship test,he said he will have a test which will be some task of coding i will have to perf
orm

I wanna know what should i expect and should prepare for tommorow

I have attached an image of my cv that contain m
y skills
```
---

     
 
all -  [ Thoughts about OPEA? ](https://www.reddit.com/r/LangChain/comments/1fv2zw3/thoughts_about_opea/) , 2024-10-05-0912
```
Hello,

I was looking for a 'production grade' deployment architecture for Langchain using microservices and stumbled up
on [OPEA](https://opea.dev/), has anyone used/tried it? The architecture (below) seems quite interesting and you can use
 Lanchain in any of the microservice

https://preview.redd.it/jo5409lw4isd1.png?width=881&format=png&auto=webp&s=9082ac5
6cfa7edfe94ed6090753ace695a459c2b

Both Intel, AMD, SAP and other big companies are in the project so it seems quite a b
ig effort
```
---

     
 
all -  [ Cross-Paged Table PDFs for Extraction Testing (Vertical/Horizontal Splits/Handwritten) ](https://www.reddit.com/r/LangChain/comments/1fuz911/crosspaged_table_pdfs_for_extraction_testing/) , 2024-10-05-0912
```
Hey everyone,

I'm working on a project to test and improve the extraction of tables from PDFs, especially when the tabl
es are split across multiple pages. This includes tables that:

* Are split **vertically** across pages (e.g., rows on o
ne page, continued on the next).
* Are split **horizontally** across pages (e.g., columns on one page, continued on the 
next).

If you have any PDFs with these types of cross-paged tables, I'd really appreciate it if you could share them wi
th me. 

Thanks in advance for your help!
```
---

     
 
all -  [ Streaming with LangGraph ](https://www.reddit.com/r/LangChain/comments/1fusj4e/streaming_with_langgraph/) , 2024-10-05-0912
```
I need my langgraph app to stream ai responses. But I can’t get CompiledStateGraph to stream out a response.

.astream(s
tream_mode=“messages”) almost works, except it just spit out everything in one go like .invoke

Maybe .astream_event or 
.astream_log might the solution? I need your help on this.

Thanks 🙏 
```
---

     
 
all -  [ Newbie on langchain ](https://www.reddit.com/r/LangChain/comments/1fuqqf7/newbie_on_langchain/) , 2024-10-05-0912
```
Trying to understand why langchain is not overkill especially for basic PrompTemplate or OutputParser features. Anyone h
ave a satisfying answer? 
Do you use langchain for every kind of operation in tour project or do you also feel it’s an o
verkill sometimes?
```
---

     
 
all -  [ Why use Flowise when n8n offers RAG and more? ](https://www.reddit.com/r/LangChain/comments/1fuqbmf/why_use_flowise_when_n8n_offers_rag_and_more/) , 2024-10-05-0912
```
I've used both Flowise and n8n to create my Chatbot that executes a RAG operation to answer the user's queries.

The flo
w executes an n8n HTTP POST request to Flowise that returns the LLM's response. The time to reaponse was around 6 second
s. Too slow compared to using the native chatbox in Flowise (am I doing something wrong?)

Then, I realized that I can d
uplicate the RAG operation on n8n itself, ditching Flowise altogether. It worked.

I'd love to know your opinions on whe
ther n8n can replace Flowise completely. Am I missing the point of why Flowise is still relevant?
```
---

     
 
all -  [ Trying to Help With LLM Apps ](https://www.reddit.com/r/LangChain/comments/1fulbos/trying_to_help_with_llm_apps/) , 2024-10-05-0912
```
I just recently started building an LLM Application and was having difficulty knowing if my workflow was good enough for
 production without testing it many times.

So I tried to build this tool that automatically evaluates my workflow befor
e I even run it and have actually been able to get more reliable outputs way faster!

https://preview.redd.it/c8acftj4kd
sd1.png?width=3080&format=png&auto=webp&s=d0c9178ca17352a22944b5f4a28d254dec8028b5

I wanted to share this with you guys
 to help anyone else having a similar problem. Please let me know if this is something you’d find useful and if you want
 to try it.

Best of luck on creating your LLM Apps!
```
---

     
 
all -  [ SqliteSaver import in Langgraph 0.2.32 ](https://www.reddit.com/r/LangChain/comments/1ful5qe/sqlitesaver_import_in_langgraph_0232/) , 2024-10-05-0912
```
Hello! I've recently updated to langgraph 0.2.32 and I'm facing a module import error regarding the SqliteSaver, before 
I found this in 'from langgraph.checkpoint.sqlite import SqliteSaver' but after I updated langgraph the module is not fo
und there, does anyone where is it located?
```
---

     
 
all -  [ Question related to Graphs ](https://www.reddit.com/r/LangChain/comments/1fuhocb/question_related_to_graphs/) , 2024-10-05-0912
```
Hi Guys,

I'm dabbling around in Langgraph and running into an issue at this point.

I am trying to make a first node in
 my graph that should decide if someone is just small talking or actually asking a RAG specific question. It should make
 that decision based on the question and memory. I've try to implement this and it works if do this only on the question
, but id like to do it also based on memory.

Here is my implementation:

`from typing import TypedDict`  
`from langgra
ph.graph import StateGraph`  
`from langgraph.graph import Graph`

`class AgentState(TypedDict):`  
`messages: list[str]
`  
`workflow = StateGraph(AgentState)`

`def agent(question, memory):`  
`res = llm.invoke(f'''You are given an interac
tion with a user so far and the final  question. Use these to decide if the user is interested in small talk or that it 
want to know something specifically pension related.`  
`If it's related to small talk, return 'Small Talk'`  
`If it's 
related to pensions, return 'Pension'`  
`Only return either of these values and nothing else`

`Here is the question:` 
 
`{question}`  

`Here is the full conversation:`  
`{memory}`  
`''')`  
`return res.content`

`from langgraph.graph i
mport StateGraph, START, END`  
`from langgraph.graph.message import add_messages`  
`workflow = Graph()`  
`workflow.ad
d_node('agent', agent)`  
`workflow.add_edge(START, 'agent')`  
`workflow.add_edge('agent', END)`  
`graph = workflow.co
mpile()`  
`graph.invoke('How are you?', 'Nothing')`

  
this returns:  
AttributeError: 'str' object has no attribute '
items'

is there an issue with what i defined in my class?

Any help would be sweet! Thanks in advance
```
---

     
 
all -  [ Please help me find learning materials from the curriculum of this AI cohert ](https://www.reddit.com/r/learnprogramming/comments/1fuhlly/please_help_me_find_learning_materials_from_the/) , 2024-10-05-0912
```
Hello guys,

I have very basic coding knowledge; just for hobby but I'm interested in learning more about technical AI s
tuff. I really want to join this cohert but it's quite expensive for me ($1600).

They have their course plan [over](htt
ps://www.100xengineers.com/#curriculum) here. It would be really awesome if you could help me find a good source for any
 of the topics that you know.

Thanks!

# Course plan:

**Week 1:** Proprietary Models & Diffusion

* Live Lesson: Histo
ry of GenAI, How to Research, and Intro to Playground AI
* Live Lesson: How Diffusion Models Work and Playground AI
* Li
ve Lesson: Prompt Engineering for Various Outputs

**Week 2:** Intro to Stable Diffusion

**Week 3: Advanced Stable Diff
usion** (Img2Img, Extension & Inpainting)

* Live Lesson: Checkpoints, ControlNet, and More
* Live Lesson: img2img, Inpa
inting, and Extensions
* Assignment: Make a Diffusion Engine
* Lesson 1: How to Install Extensions
* Lesson 2: ControlNe
t
* Lesson 3: Inpainting

**Week 4: Dreambooth, ControlNet & IP Adapters**

* Live Lesson: Intro to Dreambooth and Contr
olNet IP Adapters
* Live Lesson: Parameters & Training with Dreambooth
* Lesson 1: IP Adapters
* Lesson 2: Preparing Dat
aset for Dreambooth Training
* Lesson 3: Dreambooth Training Parameters

**Week 5: Advanced Finetuning**

* Live Lesson:
 Intro to LoRA
* Live Lesson: Mastering LoRA Parameters
* Lesson 1: How to Install Kohya SS
* Lesson 2: Dataset for Trai
ning LoRA
* Lesson 3: Parameters for LoRA

**Week 6: ComfyUI**

* Live Lesson: Basics of ComfyUI
* Assignment: Advanced 
ComfyUI Workflows
* Live Lesson: Assignment 2 - Dreambooth Training

**Week 7: Advanced ComfyUI**

* Live Lesson: Breakd
own of ComfyUI Workflows
* Live Lesson: Project Breakdown & Revisions
* Capstone: Mid Cohort Capstone Project

**Week 8:
 Get Ready to Code**

* Live Lesson: Design Thinking and Problem Solving
* Video Lesson: Why Code?
* Exercise: Practice 
Set - BigBinary Exercises
* Live Lesson: Intro to Python
* Assignment: Product Breakdown

**Week 9: Get Ready to Code**


* Live Lesson: Building an API with FastAPI
* Live Lesson: Intro to UI Building
* Assignment: Build Your AI Toolkit
* A
ssignment: Developing a Chatbot

**Week 11: Topic: Building Full Stack AI Apps**

**Week 12: Intro to LLMs**

**Week 13*
*: **AI Agents (Autogen, crewAI, AssistantAPIs)**

**Week 14**: RAG with Langchain & Llamaindex

**Week 14:** Topic: Vec
tor Database (LLM Memory)

**Week 16**: Fine-tuning LLMs

**Week 17:** Model Deployment (MLOps)
```
---

     
 
all -  [ Please help me find learning materials from the curriculum of this AI cohert ](https://www.reddit.com/r/developersIndia/comments/1fuh6ex/please_help_me_find_learning_materials_from_the/) , 2024-10-05-0912
```
Hello guys,

I have very basic coding knowledge; just for hobby but I'm interested in learning more about technical AI s
tuff. I really want to join this cohert but it's quite expensive for me (₹1.35L).

They have their course plan [over](ht
tps://www.100xengineers.com/#curriculum) here. If you can help me find a good source for any of the topics you know, it 
will be real nice!

Thanks

# Course plan:

**Week 1:** Proprietary Models & Diffusion

* Live Lesson: History of GenAI,
 How to Research, and Intro to Playground AI
* Live Lesson: How Diffusion Models Work and Playground AI
* Live Lesson: P
rompt Engineering for Various Outputs

**Week 2:** Intro to Stable Diffusion

**Week 3: Advanced Stable Diffusion** (Img
2Img, Extension & Inpainting)

* Live Lesson: Checkpoints, ControlNet, and More
* Live Lesson: img2img, Inpainting, and 
Extensions
* Assignment: Make a Diffusion Engine
* Lesson 1: How to Install Extensions
* Lesson 2: ControlNet
* Lesson 3
: Inpainting

**Week 4: Dreambooth, ControlNet & IP Adapters**

* Live Lesson: Intro to Dreambooth and ControlNet IP Ada
pters
* Live Lesson: Parameters & Training with Dreambooth
* Lesson 1: IP Adapters
* Lesson 2: Preparing Dataset for Dre
ambooth Training
* Lesson 3: Dreambooth Training Parameters

**Week 5: Advanced Finetuning**

* Live Lesson: Intro to Lo
RA
* Live Lesson: Mastering LoRA Parameters
* Lesson 1: How to Install Kohya SS
* Lesson 2: Dataset for Training LoRA
* 
Lesson 3: Parameters for LoRA

**Week 6: ComfyUI**

* Live Lesson: Basics of ComfyUI
* Assignment: Advanced ComfyUI Work
flows
* Live Lesson: Assignment 2 - Dreambooth Training

**Week 7: Advanced ComfyUI**

* Live Lesson: Breakdown of Comfy
UI Workflows
* Live Lesson: Project Breakdown & Revisions
* Capstone: Mid Cohort Capstone Project

**Week 8: Get Ready t
o Code**

*  Live Lesson: Design Thinking and Problem Solving
* Video Lesson: Why Code?
* Exercise: Practice Set - BigBi
nary Exercises
* Live Lesson: Intro to Python
* Assignment: Product Breakdown

**Week 9: Get Ready to Code**

* Live Les
son: Building an API with FastAPI
* Live Lesson: Intro to UI Building
* Assignment: Build Your AI Toolkit
* Assignment: 
Developing a Chatbot

**Week 11: Topic: Building Full Stack AI Apps**

**Week 12: Intro to LLMs**

**Week 13**: **AI Age
nts (Autogen, crewAI, AssistantAPIs)**

**Week 14**: RAG with Langchain & Llamaindex

**Week 14:** Topic: Vector Databas
e (LLM Memory)

**Week 16**: Fine-tuning LLMs

**Week 17:** Model Deployment (MLOps)
```
---

     
 
all -  [ 🚀 Join our Global AI Agents Hackathon with LangChain 🦜🔗 and Llama Index 🦙! ](https://tensorops.ai/aiagentsonlinehackathon) , 2024-10-05-0912
```
I'm organizing a global online hackathon focused on creating AI Agents, partnering with LangChain!!! and Llama Index. 🎉


Key Details:
🏆 Challenge: Build an AI Agent + create usage guide
🌐 Format: Online, with live webinars and expert lectur
es
🧠 Perks: Top-tier mentors and judges
📚 Submission: PR to the GitHub GenAI_Agents repo

We got over 100 registrations 
in the first 24 hours 😲 

❓ Questions? Ask below!

Registration in the link attached.
```
---

     
 
all -  [ Issues with Running LLMs Locally for PDF Data Extraction (OLLAMA and Langchain vs HuggingFaceChat) ](https://www.reddit.com/r/LocalLLaMA/comments/1fufo1g/issues_with_running_llms_locally_for_pdf_data/) , 2024-10-05-0912
```
Hey everyone,

I’ve been experimenting with running LLMs locally using tools like OLLAMA and Langchain, and I’ve encount
ered an issue when trying to extract basic information from PDFs (like title, author, etc.).

When I use the `command-r`
 model on HuggingFaceChat, paired with their document parser, it works perfectly, returning clean and accurate metadata.
 However, when I try to replicate this locally in Langchain, using either the `PyPDFLoader` or `UnstructuredLoader`, and
 the same model, the performance drops significantly. Instead of giving me the metadata I ask for, the model starts ramb
ling, generating random details from the text without providing the specific data requested.

Has anyone else faced a si
milar issue when running models locally for PDF parsing? How different is the data extraction approach between Langchain
 and HuggingFaceChat? If you’ve managed to resolve this or have any insights, I’d love to hear them.

Thanks in advance!

```
---

     
 
all -  [ Experiment Tracking Tools & Lbirary Suggestion For Using Alonside Langchain ](https://www.reddit.com/r/LangChain/comments/1fufh22/experiment_tracking_tools_lbirary_suggestion_for/) , 2024-10-05-0912
```
Hey everyone,

  
I'm at the beggining of developing a LLM application. My plan is preparing a MLOps arhictecture along 
with Langchain to track Chain, RAG utils (vector db name, search params etc.), input-output and evaluation metrics etc. 
In order to do this, I've planned to use MLFlow, however, compabilities between those libraries are not set (or maintene
d after langchain version 0.1 I do not know) so I'm not able to finish a full tracking pipeline for now (langchain versi
on == 0.3.1, mlflow version == 2.16.2). In addition, in mlflow website, they said this notebook was made with langchain 
version 0.1, but downgrading langchain library from 0.3 to 0.1 to use mlflow only might seems not a good idea at all.  


  
Is there any suggestion to use tracking library, tool etc. to use with Langchain ?   
  
Cheers     
```
---

     
 
all -  [ AgentLite By Salesforce ](https://www.reddit.com/r/LangChain/comments/1fub1mp/agentlite_by_salesforce/) , 2024-10-05-0912
```
in the AgentLite study there are some pretty bold statements in terms of how AgentLite compares to other dev environment
s, like LangChain...

  
Does anyone have practical experience in building solutions with AgentLite?

https://preview.re
dd.it/6xuhk3jtvasd1.png?width=2066&format=png&auto=webp&s=7b1f4a7bfe13311ff4fb16d1a6aa895f909e1699

  

```
---

     
 
all -  [ RAG - Hybrid Document Search and Knowledge Graph with Contextual Chunking, OpenAI, Anthropic, FAISS, ](https://www.reddit.com/r/Rag/comments/1fu9u5r/rag_hybrid_document_search_and_knowledge_graph/) , 2024-10-05-0912
```
Hey folks!

Previously, I released [Contextual-Doc-Retrieval-OpenAI-Reranker](https://github.com/lesteroliver911/context
ual-doc-retrieval-opneai-reranker), and now I've enhanced it by integrating a graph-based approach to further boost accu
racy. The project leverages OpenAI’s API, contextual chunking, and retrieval augmentation, making it a powerful tool for
 precise document retrieval. I’ve also used strategies like embedding-based reranking to ensure the results are as accur
ate as possible.

**the git-repo** [**here**](https://github.com/lesteroliver911/contextual-chunking-graphpowered-rag)


The runnable Python code is available on GitHub for you to fork, experiment with, or use for educational purposes. As so
meone new to Python and learning to code with AI, this project represents my journey to grow and improve, and I’d love y
our feedback and support. Your encouragement will motivate me to keep learning and evolving in the Python community! 🙌




[architecture diagram based on the code. correction - we are using the gpt-4o model](https://preview.redd.it/spinhmf6f
asd1.png?width=1920&format=png&auto=webp&s=8967b1026d99d7fc25d0dc12b66f54953c9c2794)

# Table of Contents

* [Features](
#features)
* [Key Strategies for Accuracy and Robustness](#key-strategies-for-accuracy-and-robustness)
* [Installation](
#installation)
* [Environment Variables](#environment-variables)
* [Usage](#usage)
* [Example](#example)
* [Results](#re
sults)
* [Evaluation](#evaluation)
* [Visualization](#visualization)
* [Contributing](#contributing)
* [License](#licens
e)

# Features

* **Hybrid Search**: Combines vector search with FAISS and BM25 token-based search for enhanced retrieva
l accuracy and robustness.
* **Contextual Chunking**: Splits documents into chunks while maintaining context across boun
daries to improve embedding quality.
* **Knowledge Graph**: Builds a graph from document chunks, linking them based on s
emantic similarity and shared concepts, which helps in accurate context expansion.
* **Context Expansion**: Automaticall
y expands context using graph traversal to ensure that queries receive complete answers.
* **Answer Checking**: Uses an 
LLM to verify whether the retrieved context fully answers the query and expands context if necessary.
* **Re-Ranking**: 
Improves retrieval results by re-ranking documents using Cohere's re-ranking model.
* **Graph Visualization**: Visualize
s the retrieval path and relationships between document chunks, aiding in understanding how answers are derived.

# Key 
Strategies for Accuracy and Robustness

1. **Contextual Chunking**:
   * Documents are split into manageable, overlappin
g chunks using the `RecursiveCharacterTextSplitter`. This ensures that the integrity of ideas across boundaries is prese
rved, leading to better embedding quality and improved retrieval accuracy.
   * Each chunk is augmented with contextual 
information from surrounding chunks, creating semantically richer and more context-aware embeddings. This approach ensur
es that the system retrieves documents with a deeper understanding of the overall context.
2. **Hybrid Retrieval (FAISS 
and BM25)**:
   * **FAISS** is used for semantic vector search, capturing the underlying meaning of queries and document
s. It provides highly relevant results based on deep embeddings of the text.
   * **BM25**, a token-based search, ensure
s that exact keyword matches are retrieved efficiently. Combining FAISS and BM25 in a hybrid approach enhances precision
, recall, and overall robustness.
3. **Knowledge Graph**:
   * The knowledge graph connects chunks of documents based on
 both semantic similarity and shared concepts. By traversing the graph during query expansion, the system ensures that r
esponses are not only accurate but also contextually enriched.
   * Key concepts are extracted using an LLM and stored i
n nodes, providing a deeper understanding of relationships between document chunks.
4. **Answer Verification**:
   * Onc
e documents are retrieved, the system checks if the context is sufficient to answer the query completely. If not, it aut
omatically expands the context using the knowledge graph, ensuring robustness in the quality of responses.
5. **Re-Ranki
ng**:
   * Using Cohere's re-ranking model, the system reorders search results to ensure that the most relevant document
s appear at the top, further improving retrieval accuracy.

# Usage

1. **Load a PDF Document**: The system uses `LlamaP
arse` to load and process PDF documents. Simply run the [`main.py`](http://main.py) script, and provide the path to your
 PDF file:python [main.py](http://main.py)
2. **Query the Document**: After processing the document, you can enter queri
es in the terminal, and the system will retrieve and display the relevant information:Enter your query: What are the key
 points in the document?
3. **Exit**: Type `exit` to stop the query loop.

# Example

    Enter the path to your PDF fil
e: /path/to/your/document.pdf
    
    Enter your query (or 'exit' to quit): What is the main concept?
    Response: The
 main concept revolves around...
    
    Total Tokens: 1234
    Prompt Tokens: 567
    Completion Tokens: 456
    Total
 Cost (USD): $0.023

# Results

The system provides **highly accurate** retrieval results due to the combination of FAIS
S, BM25, and graph-based context expansion. Here's an example result from querying a technical document:

**Query**: 'Wh
at are the key benefits discussed?'

**Result**:

* **FAISS/BM25 hybrid search**: Retrieved the relevant sections based 
on both semantic meaning and keyword relevance.
* **Answer**: 'The key benefits include increased performance, scalabili
ty, and enhanced security.'
* **Tokens used**: 765
* **Accuracy**: 95% (cross-verified with manual review of the documen
t).

# Evaluation

The system supports evaluating the retrieval performance using test queries and documents. Metrics su
ch as **hit rate**, **precision**, **recall**, and **nDCG (Normalized Discounted Cumulative Gain)** are computed to meas
ure accuracy and robustness.

    test_queries = [
        {'query': 'What are the key findings?', 'golden_chunk_uuids':
 ['uuid1', 'uuid2']},
        ...
    ]
    
    evaluation_results = graph_rag.evaluate(test_queries)
    print('Evalua
tion Results:', evaluation_results)

**Evaluation Result (Example)**:

* **Hit Rate**: 98%
* **Precision**: 90%
* **Reca
ll**: 85%
* **nDCG**: 92%

These metrics highlight the system's robustness in retrieving and ranking relevant content.


# Visualization

The system can visualize the knowledge graph traversal process, highlighting the nodes visited during c
ontext expansion. This provides a clear representation of how the system derives its answers:

1. **Traversal Visualizat
ion**: The graph traversal path is displayed using `matplotlib` and `networkx`, with key concepts and relationships high
lighted.
2. **Filtered Content**: The system will also print the filtered content of the nodes in the order of traversal
.Filtered content of visited nodes in order of traversal: Step 1 - Node 0: Filtered Content: This chunk discusses... Ste
p 2 - Node 1: Filtered Content: This chunk adds details on...

# License

This project is licensed under the MIT License
. See the LICENSE file for details.
```
---

     
 
MachineLearning -  [ [D] How are folks building conversational Retrieval Augmented Generation apps ](https://www.reddit.com/r/MachineLearning/comments/1ftdby7/d_how_are_folks_building_conversational_retrieval/) , 2024-10-05-0912
```
I've read through various resources such as:  
- [https://vectorize.io/how-i-finally-got-agentic-rag-to-work-right/](htt
ps://vectorize.io/how-i-finally-got-agentic-rag-to-work-right/)  
- [https://python.langchain.com/docs/tutorials/qa\_cha
t\_history/](https://python.langchain.com/docs/tutorials/qa_chat_history/)  
- [https://langchain-ai.github.io/langgraph
/tutorials/rag/langgraph\_agentic\_rag/](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/) 
 
- [https://docs.llamaindex.ai/en/stable/module\_guides/deploying/chat\_engines/](https://docs.llamaindex.ai/en/stable/
module_guides/deploying/chat_engines/)  
- [https://huggingface.co/datasets/nvidia/ChatRAG-Bench](https://huggingface.co
/datasets/nvidia/ChatRAG-Bench) 

But these feel overly reductive, since they don't address complexities like:  
1) when
 to retrieve vs. just respond immediately to reduce latency  
2) rely on existing context previously retrieved in the co
nversation instead of retrieving again at the current turn  
3) partition LLM context between retrieved information and 
past conversation history.

I'm sure some teams already have good systems for this, would appreciate pointers!
```
---

     
 
MachineLearning -  [ Built a web agent which call fill Google forms based on the user details [P] ](https://www.reddit.com/r/MachineLearning/comments/1fozud5/built_a_web_agent_which_call_fill_google_forms/) , 2024-10-05-0912
```
GitHub repo : [https://github.com/shaRk-033/web-agent](https://github.com/shaRk-033/web-agent)

Tried to solve it using 
two approaches:

# 1: Basic Scraping and Filling

This is the straightforward approach. The agent scrapes the form’s HTM
L and uses fixed XPaths to find and fill in the required fields.

* It pulls the form’s HTML, locates the fields with se
t XPaths, and inputs the answers. It’s a direct and simple method.
* If the form changes or an element isn’t where it’s 
expected, the process can fail and may need manual adjustments.

[basic approach](https://preview.redd.it/5e8g4a1k4xqd1.
png?width=1055&format=png&auto=webp&s=d8e984e4feaee2f0453b08c8696768c40a2a5c20)

2. Using LangChain Agents and tool call
ing

* LangChain Agent**:** The agent handles everything by using the LLM’s reasoning to decide what to do next, includi
ng generating those tricky XPaths.
* Error Handling**:** If something goes wrong (like an element not found), the agent 
tries again with better XPaths until it gets the job done.

[using langchain agents](https://preview.redd.it/948i88pl4xq
d1.png?width=782&format=png&auto=webp&s=ed1e6c19efec9f4cbbbd6ab5a22558f221cf745f)

Any recommendations to improve this w
ould be welcome. Also, if anyone has ideas on building similar web agents to automate other tasks, it would be great to 
hear them. :)
```
---

     
 
MachineLearning -  [ [P] Swapping Embedding Models for an LLM ](https://www.reddit.com/r/MachineLearning/comments/1fktvbj/p_swapping_embedding_models_for_an_llm/) , 2024-10-05-0912
```
How tightly coupled is an embedding model to a language model?

Taking an example from Langchain's tutorials, they use O
llama's _nomic-embed-text_ for embedding and _Llama3.1_ for the understanding and Q/A. I don't see any documentation abo
ut Llama being built on embeddings from this embedding model. 

Intuition suggests that a different embedding model may 
produce outputs of other sizes or produce a different tensor for a character/word, which would have an impact on the res
ults of the LLM. So would changing an embedding model require retraining/fine-tuning the LLM as well?

I need to use a e
mbedding model for code snippets and text. Do I need to find a specialized embedding model for that? If yes, how will ll
ama3.1 ingest the embeddings?
```
---

     
 
MachineLearning -  [ [P] Review and suggest ideas for my chatbot ](https://www.reddit.com/r/MachineLearning/comments/1fb2mwl/p_review_and_suggest_ideas_for_my_chatbot/) , 2024-10-05-0912
```
Ok, so I am currently trying to build support chatbot with following technicalities 
1. FastAPI for web server(Need to m
ake it faster)
2. Qdrant as Vector Data Base(Found it to be the fastest amongst Chromadb, Elastic Search and Milvus)
3. 
MongoDB for storing all the data and feedback.
4. Semantic chunking with max token limit of 512.
5. granite-13b-chat-v2 
as the LLM(I know it's not good but I have limited options available)
6. The data is structured as well as unstructured.
 Thinking of having involving GraphRAG with current architecture.
7. Multiple data sources stored in multiple collection
s of vector database because I have implemented an access control.
8. Using mongoengine currently as a ORM. If you know 
something better please suggest.
9. Using all-miniLM-l6-v2 as vector embedding currently but planning to use stella_en_4
00M_v5.
10. Using cosine similarity to retrieve the documents.
11. Using BLEU, F1 and BERT score for automated evaluatio
n based on golden answer.
12. Using top_k as 3.
13. Currently using basic question answering prompt but want to improve 
it. Any tips? Also heard about Automatic Prompt Evaluation.
14. Currently using custom code for everything. Looking to u
se Llamaindex or Langchain for this. 
15. Right now I am not using any AI Agent, but I want to know your opinions. 
16. 
It's a simple RAG framework and I am working on improving it.
17. I haven't included reranker but I am planning to do so
 too.

I think I mentioned pretty much everything I am using for my project. So please share your suggestions, comments 
and reviews for the same. Thank you!!
```
---

     
 
MachineLearning -  [ [P] Lessons from Retrieval Augmented Generation ](https://www.reddit.com/r/MachineLearning/comments/1f9tvg7/p_lessons_from_retrieval_augmented_generation/) , 2024-10-05-0912
```
I implemented Rag in my organization and just wrote a blog about what we learned here:   
[https://www.b-yond.com/post/t
ransforming-telco-troubleshooting-our-journey-building-telcogpt-with-rag](https://www.b-yond.com/post/transforming-telco
-troubleshooting-our-journey-building-telcogpt-with-rag)

Hoping it would be helpful for those in this area. Covers rag 
evaluation (ragas), sql db, langchain agents vs chains, weaviate vector db, hybrid search, reranking, and more.

Some ad
ditional insights on ranking and hybrid search here:

[https://www.linkedin.com/posts/drzohaib\_transforming-telco-troub
leshooting-our-journey-activity-7232072089837486081--Le1?utm\_source=share&utm\_medium=member\_android](https://www.link
edin.com/posts/drzohaib_transforming-telco-troubleshooting-our-journey-activity-7232072089837486081--Le1?utm_source=shar
e&utm_medium=member_android)
```
---

     
 
deeplearning -  [ What is the best approach for Parsing and Retrieving Code Context Across Multiple Files in a Hierarc ](https://www.reddit.com/r/deeplearning/comments/1fh58oz/what_is_the_best_approach_for_parsing_and/) , 2024-10-05-0912
```
I want to implement a Code-RAG system on a code directory where I need to:

* Parse and load all the files from folders 
and subfolders while excluding specific file extensions.
* Embed and store the parsed content into a vector store.
* Ret
rieve relevant information based on user queries.

However, I’m facing two major challenges:

**File Parsing and Loading
:** What’s the most efficient method to parse and load files in a hierarchical manner (reflecting their folder structure
)? Should I use Langchain’s directory loader, or is there a better way? I came across the Tree-sitter tool in Claude-dev
’s repo, which is used to build syntax trees for source files—would this be useful for hierarchical parsing?

**Cross-Fi
le Context Retrieval:** If the relevant context for a user’s query is spread across multiple files located in different 
subfolders, how can I fine-tune my retrieval system to identify the correct context across these files? Would reranking 
resolve this, or is there a better approach?

**Query Translation:** Do I need to use Something like Multi-Query or RAG-
Fusion to achieve better retrieval for hierarchical data?

\[I want to understand how tools like [continue.dev](http://c
ontinue.dev/) and [claude-dev](https://github.com/saoudrizwan/claude-dev) work\]
```
---

     
