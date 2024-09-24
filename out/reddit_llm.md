 
all -  [ Vision QA ](https://www.reddit.com/r/LangChain/comments/1fnxzxo/vision_qa/) , 2024-09-24-0912
```
Which is better: google/deplot or qwen2-VL?
```
---

     
 
all -  [ Looking for somebody to have a consultation about Langchain\Rag etc. ](https://www.reddit.com/r/LangChain/comments/1fnx5p0/looking_for_somebody_to_have_a_consultation_about/) , 2024-09-24-0912
```
Hey! We are a small team of two building an app using langchain. We are very new to all of it and we'd like to chat with
 somebody who has already made something \\ worked a lot using Langchain or basically any agent management system for RA
G. We can pay your hourly rate for example. Feel free to DM me (I hope it works on Reddit) or write the way I can contac
t you under the post.
```
---

     
 
all -  [ Building Sales Insights app with GraphRAG techniques using Postgres ](https://www.reddit.com/r/LangChain/comments/1fnuwo1/building_sales_insights_app_with_graphrag/) , 2024-09-24-0912
```
GraphRAG has a bunch of really useful techniques. The idea that just vector distance isn't enough for good retrieval and
 you want to use relationships to get better data is critical for good apps.

The only problem is that I find GraphDB qu
ery syntax really really challenging. I prefer to just use Postgres, pgvector and plain old SQL (or even ORM when it fit
s).

For my sales insights app, I started with just vector distance. But I discovered that when I search for 'customer p
ain points', the retrieved chunks are mostly the sales person asking 'what problems do you have with current solution?'.
 This is not useful! I needed the response.

So I used SQL to retreive both the nearest vectors \*and\* the chunks immed
iately before and after each.  
And I deduplicated the chunks before giving them to the LLM (or it would get repetitive)
.

    def get_similar_chunks(session: any, embedding: List[float], conversation_id: int):
        query = '''
        w
ith src as (
            SELECT * FROM call_chunks 
            WHERE conversation_id = '{}' 
            AND (embedding
 <=> '{}') < 1 
            ORDER BY embedding <=> '{}' LIMIT 3 ) 
        select distinct on (cc.chunk_id) cc.chunk_id,
 cc.conversation_id, cc.speaker_role, cc.content from src
        join call_chunks as cc on 
            cc.conversation
_id = src.conversation_id 
            and cc.tenant_id = src.tenant_id 
            and cc.chunk_id >= src.chunk_id -1

            and cc.chunk_id <= src.chunk_id + 1;
        '''.format(conversation_id, embedding, embedding)
        simil
ar_chunks_raw = session.execute(text(query))
        return [{'conversation_id': chunk.conversation_id, 'speaker_role': 
chunk.speaker_role, 'content': chunk.content} for chunk in similar_chunks_raw]

The app is basically a Python webapp (in
 FastAPI). I used Nile serverless Postgres for the database and Modal to deploy both the app and Llama 3.1.

You can rea
d the full blog here: [https://www.thenile.dev/blog/nile\_modal](https://www.thenile.dev/blog/nile_modal)
```
---

     
 
all -  [ Spoke to 21 CrewAI developers and here's what we found ](https://www.reddit.com/r/crewai/comments/1fntljw/spoke_to_21_crewai_developers_and_heres_what_we/) , 2024-09-24-0912
```
I recently had our AI interviewer speak with 21 CrewAI developers. I have been curious about agent frameworks and I prev
iously did a research project on LangChain a month ago. Developers shared about what attracted them to use CrewAI, exper
iences with other frameworks, and suggestions. Here are some key takeaways:

**What Attracts Developers to CrewAI?**

* 
**Ease of Use and Integration:** CrewAI simplifies the development process with minimal coding and straightforward setup
.

'CrewAI is really easy to integrate because most of the things it does are kind of predetermined or already made. So 
we actually need to focus on flow and on prompts.' — Manager, IT Consulting Company

'I looked at one example project to
 get started and was blown away that it only took several lines of code to define the agents I wanted to create.' — Foun
der, GenAI Startup

'It's a relatively easy framework... I would say it's a pretty easy framework to learn with a minima
l learning curve. It's user-friendly and easy to set up.' — AI Engineer at an EdTech Startup

* **Agent Collaboration an
d Backstories:** The framework enables inter-agent communication and allows developers to assign backstories to agents f
or more focused and context-aware responses.

'What I didn't like about LangChain is that it doesn't allow interactivity
 between agents, but CrewAI does. So that is why I choose CrewAI.' — AI Engineer, Startup Consulting Company

'The way C
rewAI handles agents. How you write their backstories and calls. It makes the agents focus on the task you give them in 
a specific way.' — Same Contributor

* **Logging and Debugging Capabilities:** CrewAI provides insightful logging, helpi
ng developers understand agent interactions and troubleshoot effectively.

'I love the logging and the output to be able
 to see what was going on behind the scenes... it was really powerful.' — Founder, GenAI Startup

'I loved being able to
 see the logging and the reasoning behind the scenes of how the agents were interacting with each other.' — Same Contrib
utor  


**CrewAI vs. Alternatives**

The most commonly considered alternative was LangChain. Developers noted several a
reas where CrewAI stands out:

* **Simplicity:** Compared to alternatives that may require extensive coding, CrewAI offe
rs a more user-friendly experience.

'I believe CrewAI is much more user-friendly compared to the alternatives. Its ease
 of use is its main benefit...' — Founder, Software Agency

'For functionality, I would say LangChain is quite better, b
ut in terms of ease of use, CrewAI is far easier than LangChain.' — Computer Science Student

'So far, it's probably the
 best and easiest one I've used... overall, CrewAI is the one I use the most.' — Founder, Automated Content Creation Sta
rtup

* **Inter-Agent Communication**: CrewAI's ability to enable agents to communicate and collaborate is a significant
 advantage.

'What I didn't like about LangChain is that it doesn't allow interactivity between agents, but CrewAI does.
' — AI Engineer, Startup Consulting Company

'If you ask me today which product I would use for a multi-worker-driven pr
oject, I would choose CrewAI, not LangGraph or LangChain.' — AI Engineer at Neo4j

* **Less Coding Required:** CrewAI re
duces the need for extensive coding, making it accessible to developers with varying levels of expertise.

'But when I s
aw CrewAI, I found that it was very easy. I didn't have to create a lot of agents or add multiple tools within the agent
. Also, there was less Python coding involved.' — AI Engineer at Neo4j

**Use Cases**   
  
CrewAI developers shared som
e interesting use cases beyond the standard fare of chatbots.  Here are some interesting use cases:

* **Educational Con
tent Creation:** Educators are using CrewAI to generate course materials, create personalized learning roadmaps, and aut
omate research and writing tasks.

* **Business Planning and Development:** Startups utilize CrewAI to simulate collabor
ative brainstorming among virtual team members to draft business plans and proposals.

* **Personal Productivity Tools:*
* Implementing agents to manage email summarization and automate social media content generation.

**Areas for Improveme
nt**

While CrewAI has garnered praise, developers also identified areas for improvement:

* **Enhanced Documentation an
d Complex Examples:** There's a desire for more comprehensive documentation and advanced tutorials.

'The documentation 
was not as thorough as it could have been, so I had to dig in and experiment more.' — Founder, Automated Content Creatio
n Startup

'I think that the most useful resource was the source code of CrewAI because there weren't many documents abo
ut the API.' — Founder, Software Agency

'I would like to see more complex examples... The community isn't very large ye
t... but a lot can be understood through the documentation and tutorials.' — AI Engineer at an EdTech Startup

* **Impro
ved Error Handling and Debugging:** Developers want clearer error messages and better debugging tools to facilitate trou
bleshooting.

'I did find it a little bit unsettling seeing different errors... it didn't seem like they had any real rh
yme or reason to them.' — Founder, GenAI Startup

'More debugging information would be helpful. Sometimes, the error mes
sages are not very descriptive.' — Researcher, Epidemiology Lab

* **Enhanced Compatibility with Other Frameworks and To
ols:** Users suggest improving compatibility with other AI frameworks and tools.

'At the moment, it's compatible with L
angChain, but it needs to be compatible with LlamaIndex and maybe some classic ML frameworks.' — AI Engineer, Startup Co
nsulting Company

'It also needs more database interactions... there should be a tool to ask questions about a CSV file 
or maybe an SQL or MongoDB database.' — Same Contributor

\_\_\_\_  
You can check out the interview transcripts here: [
kgrid.ai/company/crewai](http://kgrid.ai/company/crewai). I am planning on doing a new research project on agent framewo
rks after OpenAI's devday. What other topics would you like covered in future interviews? 


```
---

     
 
all -  [ (Profile Review) Looking for some genuine suggestions on my profile.  ](https://i.redd.it/q7cdrdnq3mqd1.png) , 2024-09-24-0912
```
Facing low views issue. 
```
---

     
 
all -  [ Feedback on my Resume (DS, AI/ML Engineer, Internship roles) ](https://i.redd.it/d4t0r0wi1mqd1.png) , 2024-09-24-0912
```

```
---

     
 
all -  [ [For Hire] Full Stack developer with proven experience building apps with LLMs ](https://www.reddit.com/r/JobFair/comments/1fnt5dn/for_hire_full_stack_developer_with_proven/) , 2024-09-24-0912
```
We are seeking a talented Full Stack developers with proven experience building apps with LLMs to join our startup. The 
ideal candidate will have a strong background in TypeScript or Python, and experience with modern AI tools and framework
s.  
Key Requirements:  


* Strong proficiency in either TypeScript or Python
* Experience with AI development tools su
ch as LangChain and retrieval techniques like RAG and GraphRAG
* Proven track record in building AI agents
* Solid under
standing of machine learning principles and algorithms
* Excellent problem-solving skills and ability to work in a fast-
paced startup environment

  
Preferred Qualifications:

* Data science experience
* Familiarity with both TypeScript an
d Python
* Experience with cloud platforms (e.g., AWS, Google Cloud, Azure)
* Knowledge of NLP techniques and transforme
r models
* Contributions to open-source AI projects

  
Responsibilities:

* Design, develop, and implement AI solutions
 using cutting-edge technologies
* Collaborate with cross-functional teams
* Optimize and scale AI models for production
 environments
* Stay up-to-date with the latest advancements in AI and incorporate new techniques as appropriate
* Parti
cipate in code reviews and contribute to best practices.
```
---

     
 
all -  [ [For Hire] Full Stack developer with proven experience building apps with LLMs ](https://www.reddit.com/r/freelance_forhire/comments/1fnt38n/for_hire_full_stack_developer_with_proven/) , 2024-09-24-0912
```
We are seeking a talented Full Stack developer with proven experience building apps with LLMs to join our startup. The i
deal candidate will have a strong background in TypeScript or Python, and experience with modern AI tools and frameworks
.  
Key Requirements:  


* Strong proficiency in either TypeScript or Python
* Experience with AI development tools suc
h as LangChain and retrieval techniques like RAG and GraphRAG
* Proven track record in building AI agents
* Solid unders
tanding of machine learning principles and algorithms
* Excellent problem-solving skills and ability to work in a fast-p
aced startup environment

Preferred Qualifications:  


* Data science experience
* Familiarity with both TypeScript and
 Python
* Experience with cloud platforms (e.g., AWS, Google Cloud, Azure)
* Knowledge of NLP techniques and transformer
 models
* Contributions to open-source AI projects

Responsibilities:  


* Design, develop, and implement AI solutions 
using cutting-edge technologies
* Collaborate with cross-functional teams
* Optimize and scale AI models for production 
environments
* Stay up-to-date with the latest advancements in AI and incorporate new techniques as appropriate
* Partic
ipate in code reviews and contribute to best practices.
```
---

     
 
all -  [ Full Stack developer with proven experience building apps with LLMs [for hire] ](https://www.reddit.com/r/hiring/comments/1fns4it/full_stack_developer_with_proven_experience/) , 2024-09-24-0912
```
We are seeking a talented Full Stack developer with proven experience building apps with LLMs to join our startup. The i
deal candidate will have a strong background in TypeScript or Python, and experience with modern AI tools and frameworks
.  


Key Requirements:  


* Strong proficiency in either TypeScript or Python
* Experience with AI development tools s
uch as LangChain and retrieval techniques like RAG and GraphRAG
* Proven track record in building AI agents
* Solid unde
rstanding of machine learning principles and algorithms
* Excellent problem-solving skills and ability to work in a fast
-paced startup environment



Preferred Qualifications:

* Data science experience
* Familiarity with both TypeScript an
d Python
* Experience with cloud platforms (e.g., AWS, Google Cloud, Azure)
* Knowledge of NLP techniques and transforme
r models
* Contributions to open-source AI projects



Responsibilities:

* Design, develop, and implement AI solutions 
using cutting-edge technologies
* Collaborate with cross-functional teams
* Optimize and scale AI models for production 
environments
* Stay up-to-date with the latest advancements in AI and incorporate new techniques as appropriate
* Partic
ipate in code reviews and contribute to best practices.


```
---

     
 
all -  [ Summarizing chat conversations ](https://www.reddit.com/r/OpenAIDev/comments/1fnq6a1/summarizing_chat_conversations/) , 2024-09-24-0912
```
What are the best ways to summarize chat conversations that exceed token limits? I'm curious about specific approaches, 
prompts, methodologies. How do I handle tool calls and tool outputs? I'm not using LangChain or LlamaIndex.
```
---

     
 
all -  [ Getting Started with LangGraph: Build Robust AI Agents & Chatbots! ](https://www.reddit.com/r/LangChain/comments/1fnoy7x/getting_started_with_langgraph_build_robust_ai/) , 2024-09-24-0912
```
Tried creating a [simple video](https://youtu.be/VyyJFrPlHfk?si=dOXRhBH3vMQwrfmM) on LangGraph showing how LangGraph can
 be used to build robust agentic workflows. 
```
---

     
 
all -  [ Between OpenAI, Anthropic, and Google, which models do you use for which tasks? ](https://www.reddit.com/r/LangChain/comments/1fnme7a/between_openai_anthropic_and_google_which_models/) , 2024-09-24-0912
```
I'm so used to OpenAI from years before ChatGPT that I have barely interacted with Gemini or Claude.

My understanding i
s that Claude is good at more natural writing styles, and Gemini is good at long contexts.

For OpenAI, I've started usi
ng \`o1-preview\` almost exclusively for any task, unless it requires vision then I will revert to \`4o\`.

I'm wonderin
g what everyone else's decision matrix looks like.
```
---

     
 
all -  [ How to prevent a 7b llm from going out of context? ](https://www.reddit.com/r/LangChain/comments/1fnlj66/how_to_prevent_a_7b_llm_from_going_out_of_context/) , 2024-09-24-0912
```
I have a RAG application that uses a 7b llm but it keeps speaking out of context. I dont want it to answer anything othe
r than the retrieved context.

  
1. I tried to define in system prompt but didnt work.

2. Tried to use a thresholding 
for nodes retrieved but didnt work.

  
What are some things I can try?
```
---

     
 
all -  [ Looking for a freelancer familiar with LangGraph ](https://www.reddit.com/r/LangChain/comments/1fnkf63/looking_for_a_freelancer_familiar_with_langgraph/) , 2024-09-24-0912
```
I have a 2 'flows' to build in LangGraph for processing and handling data. Each one will have a 3-4 tools. Looking for s
omeone who has experience with LangGraph to help out.

I'll just need the LangGraph part built, and will be adding them 
into a larger application. Please DM if you're interested. 
```
---

     
 
all -  [ How to actually study Langgraph/agent? ](https://www.reddit.com/r/LangChain/comments/1fnkdyy/how_to_actually_study_langgraphagent/) , 2024-09-24-0912
```
Hi guys just a quick question here. For those who experienced in agent, how do u guys study langgraph? The documentation
 seems lack of explaination and hard to grasp
```
---

     
 
all -  [ how to NL to SQL using LLaMA on large DBs? ](https://www.reddit.com/r/LocalLLaMA/comments/1fnhx68/how_to_nl_to_sql_using_llama_on_large_dbs/) , 2024-09-24-0912
```
Hey everyone!

I’m fairly new to the world of open-source LLMs and I’m working on building an AI assistant that generate
s SQL queries based on user questions. I use LLaMA as my base model. It works well with smaller database schemas (2-3 ta
bles with simple relationships), but I’ve run into challenges when scaling up to larger databases (100+ tables and a sch
ema exceeding 20k tokens). The schema doesn’t fit into the model’s context size.

I’ve tried summarizing the key informa
tion about the tables and relationships into JSON and used LlamaIndex's `JsonQueryEngine`, but the results haven’t been 
great. It also makes sense that as the number of tables grows, the generated queries become more confusing and harder to
 manage.

Can LangChain help me with this issue?

Could anyone point me in the right direction for handling this? If res
tructuring the database and creating view tables is the last what I want to do
```
---

     
 
all -  [ How can I setup memory for my Multi Agent System in Langgraph ? ](https://www.reddit.com/r/LangChain/comments/1fnh7mh/how_can_i_setup_memory_for_my_multi_agent_system/) , 2024-09-24-0912
```
Hello everyone , I'm working on a project that is built on Langgraph's multi-agent system ( Hierarchical architecture ) 
.

I want to add memory to the application now but haven't been successful so far . Every doc that I refer to is using m
emory on a single agent . 

Has anyone tried setting up memory for multi agent system using Langgraph yet ? Can I get so
me references ?  
Thanks in advance !
```
---

     
 
all -  [ Langgraph Studio Multi-Agent Example: Hierarchical Agents? ](https://www.reddit.com/r/LangChain/comments/1fngmp8/langgraph_studio_multiagent_example_hierarchical/) , 2024-09-24-0912
```
I've been using Langchain and Langgraph for some time now and have gained experience working with various multi-agent mo
dels, including hierarchical agents and collaboration agents. Recently, I came across Langgraph Studio, and I’m trying t
o figure out how to implement multi-agent systems within it.

From what I understand, for Langgraph Studio, agents must 
follow a specific structure. However, I’ve been unable to find any clear examples or documentation on how to implement m
ulti-agent configurations, particularly when it comes to linking agents hierarchically.

The examples I have found so fa
r only cover single agents, and whenever I come across something related to multi-agents, these agents are not truly lin
ked in any meaningful way. What I’m particularly interested in is how to link multiple agents together so that they are 
compatible with Langgraph Studio.

Could anyone provide a simple example of how to structure hierarchical multi-agents f
or Langgraph Studio? Any code snippets, templates, or guidance on the right structure would be greatly appreciated!

Tha
nk you in advance!

I have tried using the templates provided by Langgraph Studio for single agents and modified them to
 include multiple agents. I also found some templates on Google and tried those as well, but they were all focused on si
ngle agents. I expected that linking the agents hierarchically would allow them to collaborate, but none of the examples
 worked for multi-agent systems, and the agents didn’t interact as I hoped.
```
---

     
 
all -  [ AI Agents - Workflow Tool ](https://www.reddit.com/r/PromptEngineering/comments/1fnesq6/ai_agents_workflow_tool/) , 2024-09-24-0912
```
I've had really good results from creating workflows of AI agents, getting them to parse through different models.

For 
example, I ask Claude to generate me a blog post structure, then feed back into it a prompt to generate the content. I t
hen pass on to Gemini to 'fact check' it and provide any citations that may be useful.

Finally, I pass back to Claude a
gain. I'm finding it pretty useful to do these things this way, and it's nothing new - I know many others are using this
 technique, and I feel like the o1-preview model from OpenAI does something similar.

I'm considering to build a very si
mple drag/drop workflow tool that allows you to connect agents visually. It would be free to use, and you would simply g
enerate an API URL with an input. You can then set up your agents and finally return the output to the same API request 
or trigger a webhook.

You would be able to split things into JSON keys and I would also code in some logic to detect fa
ulty outputs and automatically adjust if needed.

It would be free with 'bring your own keys' or paid-to-use our own key
s with a small % off.

First, would people be interested in such a tool (I couldn't find one). Secondly, what kind of fe
atures would you like to see?

I know Langchain, etc is good but I find it a little complex to use for the non-coders an
d other stakeholders when trying to visually represent how it works.
```
---

     
 
all -  [ Which LLM security tools do you use? ](https://www.reddit.com/r/LangChain/comments/1fnd1n4/which_llm_security_tools_do_you_use/) , 2024-09-24-0912
```
We are about to launch our chatbot for alpha users, and we need a security tool to prevent prompt injection and data lea
kage. 

Currently, we use basic implementation for both - checking for forbidden words and subjects using LLM query   
B
ut we would like to use a more robust tool for that   
```
---

     
 
all -  [ Deploying your Langgraphjs agent as REST API  ](https://www.reddit.com/r/LangChain/comments/1fnaxy8/deploying_your_langgraphjs_agent_as_rest_api/) , 2024-09-24-0912
```
Is there a way for you to interact with your langgraph agent as REST API without using langgraph studio ( I don't have m
ac) and langgraph cloud ? If so please share any relevant code examples. 
```
---

     
 
all -  [ Chroma DB resist and readback ](https://www.reddit.com/r/LangChain/comments/1fn5lg8/chroma_db_resist_and_readback/) , 2024-09-24-0912
```
I am using Chroma db to save embedding similar to this code:

`from langchain_chroma import Chroma`  
`from langchain_co
mmunity.embedding import OLlamaEmbedding`  
`from langchain_core.documents import Document`

`vector_store = Chroma(`  

`collection_name='My_Collection',`  
`embedding_function=OllamaEmbedding(model='nomic-embed-text),`  
`persis_directory=
'My_DB_Dir'`  
`)`  
`document = Document(page_content='This is a test', metadata={'name': 'test'})`  
`vector_store.add
_documents(documents=document, ids='1')`

How can I persist this data and then read it during retrieval?
```
---

     
 
all -  [ Why doesn't my local llm call a tool ? ](https://www.reddit.com/r/LangChain/comments/1fn2uyi/why_doesnt_my_local_llm_call_a_tool/) , 2024-09-24-0912
```
I have the following code:

    from langchain_community.tools.tavily_search import TavilySearchResults
    from IPython
.display import Image, display
    from PIL import Image
    from langchain import hub
    from langchain_core.prompts i
mport ChatPromptTemplate
    from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
    from la
ngchain_core.messages import HumanMessage, SystemMessage
    from langchain_community.chat_models import ChatLlamaCpp
  
  from langchain.callbacks.manager import CallbackManager
    from langchain.agents import create_tool_calling_agent, Ag
entExecutor
    from langchain.agents import AgentType
    from langgraph.prebuilt import create_react_agent
    
    se
arch = TavilySearchResults(max_results=2)
    tools = [search]
    
    model = ChatLlamaCpp(
    
      #LLAMA3.1-8B-Q4
_K_M
      model_path='/home/s1ngle/.cache/huggingface/hub/models--bartowski--Meta-Llama-3.1-8B-Instruct-GGUF/snapshots/
9a8dec50f04fa8fad1dc1e7bc20a84a512e2bb01/Meta-Llama-3.1-8B-Instruct-Q4_K_M.gguf',
    
      n_gpu_layers=0,
      n_thr
eads=8,
      n_batch=8,
      n_ctx=8192,
      max_tokens=4096,
      seed=-1,
      f16_kv=True,
      verbose=False,

      cache=False,
      echo=False,
      temperature=0,
      top_k=10,
      top_p=0.95,
      streaming=True,
     
 callbacks=CallbackManager([StreamingStdOutCallbackHandler()]),
      model_kwargs={
        'chat_format': 'llama-3'
  
    },
    )
    graph = create_react_agent(model, tools)
    graph.invoke({'messages': [
      HumanMessage(content='wh
ats the weather in san francisco?')
    ]})

It prints the following result:

    However, I'm a large language model, I
 don't have real-time access to current weather conditions.
    But I can suggest some ways for you to find out the curr
ent weather in San Francisco:
    1. **Check online weather websites**: You can check websites like AccuWeather, Weather
.com, or the National Weather Service (NWS) website.
    2. **Use a mobile app**: You can download mobile apps like Dark
 Sky, Weather Underground, or The Weather Channel to get real-time weather updates.
    3. **Tune into local news**: You
 can watch local news channels in San Francisco to get the latest weather forecast.
    I hope this helps you find out t
he current weather in San Francisco!

**As you can see the tool has not been called.** **Why ?**
```
---

     
 
all -  [ Has anybody created a custom checkpointer for your LangGraph app? ](https://www.reddit.com/r/LangChain/comments/1fn030k/has_anybody_created_a_custom_checkpointer_for/) , 2024-09-24-0912
```
I have a simple chatbot app in ChainLit + LangGraph and was exploring how to use checkpointers for persistency. At the m
oment I am using the regular LiteralAI integration recommended in ChainLit's documentation and then manually creating a 
custom state for the graph before invoking it but I really don't like this approach. Has anyone created a custom checkpo
inter? LangGraph's documentation about it is sort of cryptic and they don't explain the concepts behind it so any guidan
ce would be super helpful.
```
---

     
 
all -  [ RAG with dataframes ](https://www.reddit.com/r/LangChain/comments/1fmwg5q/rag_with_dataframes/) , 2024-09-24-0912
```
Hi community, im fairly new to LLMs and RAG, and im trying to build a system to write job descriptions taking into accou
nt 2 dataframes based on already created documents.

1. The first dataframe has examples with 3 columns, the job title, 
a brief summary of it, and the long document.

2. The second dataframe has examples of how to compose the document based
 on a level that will be given in the prompt.

Do you know or have examples of notebook on how i can retrieve the most s
imilar jobs given a certain job title in the prompt? Im not sure if I should use chunks or improve my structured data

T
hanks! Im really enjoying this community! 
```
---

     
 
all -  [ Whatsapp sidekick to save any information that can be retrieved easily anytime anywhere..  ](https://www.reddit.com/r/LangChain/comments/1fmtv7a/whatsapp_sidekick_to_save_any_information_that/) , 2024-09-24-0912
```
Idea for weekend hackathon.. create a whatsapp sidekick where I can save any link or information and later retrieve it w
ith simple questions whenever i want. Kind of notes but on whatsapp and retrievable via simple natural language search..
  wdyt?   
  
Here is the video explaining the whole thing [https://www.youtube.com/watch?v=YYIEb\_BioVg](https://www.yo
utube.com/watch?v=YYIEb_BioVg)

and the code is here: [https://github.com/alinaqi/whatapp-sidekick](https://github.com/a
linaqi/whatapp-sidekick)

Tech used is redis vector search (i wanted to try out), openai, and of course python.. 
```
---

     
 
all -  [ Prompting and Verbalizer libraries ](https://www.reddit.com/r/LangChain/comments/1fmpm25/prompting_and_verbalizer_libraries/) , 2024-09-24-0912
```
Gemini-Input : 'Is the given statement hateful? \[STATEMENT TO BE TESTED FROM THE DATASET\]'  

-->Gemini-Output: 'Yes, 
it is hateful. it is hateful because ......'  

-->Gemini-Input : '\[REASON WHY THE STATEMENT IS HATEFUL\] On a scale of
 1-10 how hateful would you rate this statement?'  

-->Gemini-Output: \[Some Random Number\]  



I need to check how a
ccurate is Gemini in predicting whether a statement is hateful or not. I will have to create a Prompt-Chain and also par
se the output of the first step to give an input in the next step. Have any of you done this type of thing before? Can y
ou point me to the libraries(except OpenPrompt) that will be helpful in this Prompting task?? Also, the library must hav
e a Verbalizer function, I'm guessing.



I am fairly new to this!! I have some basic Python programming knowledge, so I
 am guessing I will be able to do this if you guys could just point me to the right libraries. Please help!!
```
---

     
 
all -  [ Need Help with Building a ChatWithPDF for Instrument Suggestions!!! ](https://www.reddit.com/r/LangChain/comments/1fmocoa/need_help_with_building_a_chatwithpdf_for/) , 2024-09-24-0912
```
I want to create a chatbot that can suggest research instruments to users based on PDF files that an admin uploads.

My 
task involves handling 200-300 PDF files of research instruments. When a user asks questions about the instruments or ma
kes a request like, 'I want to perform an XYZ experiment, suggest an instrument for it,' the AI should scan all the PDFs
 and suggest a list of instruments based on the uploaded files.

How should I approach this problem? Should I create a s
eparate vector index for each PDF and wrap it with a retrieval tool to retrieve documents from the vector database? Or s
hould I have a single vector database containing all the embeddings from all the PDFs and use a single retrieval tool wr
apper to perform similarity searches and retrieve relevant documents?

I might be wrong here, so please suggest the best
 approach to solve the problem effectively.

Thank you!
```
---

     
 
all -  [ NL to SQL on a large DBs ](https://www.reddit.com/r/LangChain/comments/1fmed0k/nl_to_sql_on_a_large_dbs/) , 2024-09-24-0912
```
Hey everyone!

I’m fairly new to the world of open-source LLMs and I’m working on building an AI assistant that generate
s SQL queries based on user questions. I use LLaMA as my base model. It works well with smaller database schemas (2-3 ta
bles with simple relationships), but I’ve run into challenges when scaling up to larger databases (100+ tables and a sch
ema exceeding 20k tokens). The schema doesn’t fit into the model’s context size.

I’ve tried summarizing the key informa
tion about the tables and relationships into JSON and used LlamaIndex's `JsonQueryEngine`, but the results haven’t been 
great. It also makes sense that as the number of tables grows, the generated queries become more confusing and harder to
 manage.

Can LangChain help me with this issue?   
  
Could anyone point me in the right direction for handling this? I
f restructuring the database and creating view tables is the last what I want to do
```
---

     
 
all -  [ A simple guide on building RAG with Excel files ](https://www.reddit.com/r/LangChain/comments/1fmarsp/a_simple_guide_on_building_rag_with_excel_files/) , 2024-09-24-0912
```
A lot of people reach out to me asking how I'm building RAGs with excel files. It is a very common use case and the good
 news is that it can be very simple while also being extremely accurate and fast, much more so than with vector embeddin
gs or bm25.

So I decided to write a blog about how I am building and using SQL agents to create RAGs with excels. You c
an check it out here: [https://ajac-zero.com/posts/how-to-create-accurate-fast-rag-with-excel-files/](https://ajac-zero.
com/posts/how-to-create-accurate-fast-rag-with-excel-files/) .

The post is accompanied by a github repo where you can c
heck all the code used for this example RAG. If you find it useful you can give it a star!

Feel free to reach out in my
 social links if you'd like to chat about rag / agents, I'm always interested in hearing about the projects people are w
orking on :)
```
---

     
 
all -  [ What are good ways to get my vector search to return more recent results? ](https://www.reddit.com/r/LangChain/comments/1fm5tgc/what_are_good_ways_to_get_my_vector_search_to/) , 2024-09-24-0912
```
I'm experimenting with RAG stack. I'm hand rolling things but this seems like a smart community which is why I'm asking 
here. I'm using weaviate as my vector database.

I want to pull back relevant pieces of data using a vector search to fe
ed to the LLM. All the records I have vectorized have dates associated with them. I'm wondering if there are any good kn
own strategies for getting the vector search to prioritize more recent records? This includes querying strategies.

Than
ks.
```
---

     
 
all -  [ Not nable to get simple JSON formatted structured output from Llama 3.1 model and langchain Pydantic ](https://www.reddit.com/r/LangChain/comments/1fm3uor/not_nable_to_get_simple_json_formatted_structured/) , 2024-09-24-0912
```
Hey,

  
I am not sure why, if it is the model or due to the modules in langchain, but I dont get proper output and ever
y run I get different strange messages when using the PydanticOutputParser.

  
I try to reproduce this example (very ni
ce example!). I always get strange messages regarding the output. I am not able to get a list of activities like shown t
here:

[https://github.com/NachoCP/AIScraping/blob/main/article/article.md](https://github.com/NachoCP/AIScraping/blob/m
ain/article/article.md)

  
Does anyone experience similar things using PydanticOutputParser together with a Llama model
?
```
---

     
 
all -  [ Chain of thought question (not only for Local models) ](https://www.reddit.com/r/LocalLLM/comments/1fm0mi1/chain_of_thought_question_not_only_for_local/) , 2024-09-24-0912
```
Dear all,

I have been thinking about the Chain-Of-Thought approach.

My understanding si that you decompose a question 
in many steps and you walk through it to avoid misinterpretations. As the example below. But how is this practically imp
lemented?

Let's say I am using either Haystack or Langchain and I query my model, should I add 'let's solve this step b
y step'? but if you use the app of Chatgpt or Gemini, you do not write this, it is already in the application. What am I
 missing that they do in their application:



Input: 'If there are 3 apples and you take away 2, how many do you have?'




Traditional Approach Output: '1'



Chain of Thought Output:



Step 1: There are 3 apples in total.

Step 2: You ta
ke away 2 apples.

Step 3: You now have the 2 apples you took away.

Final Answer: 2
```
---

     
 
all -  [ Looking for Open-Source Apps for Best Practices ](https://www.reddit.com/r/LangChain/comments/1fm014s/looking_for_opensource_apps_for_best_practices/) , 2024-09-24-0912
```
Hey everyone! 👋

I’m learning LangChain and working on an open-source app using LangGraph and Next.js. I’m on the lookou
t for best practices, good patterns, and looking for some open-source apps that can help us overcome some challenges. 


**About my project:**

I've just launched **Aithelete** ([https://aithelete.vercel.app/](https://aithelete.vercel.app/))
, an AI Agent and fitness coach that creates personalized training programs. 🏋️‍♂️ It’s been a great learning experience
, and I’d love your feedback or suggestions to improve it! You can check out the code on GitHub here: [Aithelete on GitH
ub](https://github.com/mbarinov/aithelete). 🙌

**My current challenges:**

* **How to store prompts?** Best practices fo
r managing and updating prompts?
* **Any built-in retry tools?** Effective ways to handle retries in AI applications?
* 
**Should we use streaming in AI Agents?** When does it make sense?

Any insights, patterns, or feedback on Aithelete wou
ld be super helpful. Thanks—I’m excited to learn and keep growing! 😊
```
---

     
 
all -  [ Debugging Langgraph Cloud with breakpoints ](https://www.reddit.com/r/LangChain/comments/1flxq26/debugging_langgraph_cloud_with_breakpoints/) , 2024-09-24-0912
```
Hi guys, does any of you manage to debug langgraph cloud using VSCode breakpoints and if yes how did he do it?

My intui
tion is that since it runs on a container it should be possible by using vscode extension dev container, but maybe I am 
wrong.

Thanks
```
---

     
 
all -  [ RAG using JSON file with nested referencing or chained referencing ](https://www.reddit.com/r/LangChain/comments/1flmupc/rag_using_json_file_with_nested_referencing_or/) , 2024-09-24-0912
```
I am working with a JSON file where each object has a unique ID. The user queries using the unique ID of a particular ob
ject. Depending on the query, I may need to directly fetch certain field values from that object, or follow chained refe
rences to fetch data from related objects. The chain of references can sometimes go 2-3 levels deep.

How would I make m
y RAG agent aware of the structure of this JSON schema, so it knows which references to follow to answer the user's quer
y appropriately. For example, if an object references another object via a unique ID, the agent should understand how to
 resolve that reference and fetch the relevant data from the linked object.

**Current Setup:**

* I’ve parsed the JSON 
using LangChain's `JSONLoader`.
* I’m using `OpenAIEmbeddings` and storing the data in a Chroma VectorDatabase.
* I'm us
ing Gemini LLM for query responses.

I need some overview of the flow to implement
```
---

     
 
all -  [ RAG using JSON file with nested referencing or chained referencing ](https://www.reddit.com/r/Rag/comments/1flmtri/rag_using_json_file_with_nested_referencing_or/) , 2024-09-24-0912
```
I am working with a JSON file where each object has a unique ID. The user queries using the unique ID of a particular ob
ject. Depending on the query, I may need to directly fetch certain field values from that object, or follow chained refe
rences to fetch data from related objects. The chain of references can sometimes go 2-3 levels deep.

How would I make m
y RAG agent aware of the structure of this JSON schema, so it knows which references to follow to answer the user's quer
y appropriately. For example, if an object references another object via a unique ID, the agent should understand how to
 resolve that reference and fetch the relevant data from the linked object.

**Current Setup:**

* I’ve parsed the JSON 
using LangChain's `JSONLoader`.
* I’m using `OpenAIEmbeddings` and storing the data in a Chroma VectorDatabase.
* I'm us
ing Gemini LLM for query responses.

I need some overview of the flow to implement
```
---

     
 
all -  [ Resolution of Lanchain critical vulnerability ](https://www.reddit.com/r/LangChain/comments/1flkmok/resolution_of_lanchain_critical_vulnerability/) , 2024-09-24-0912
```
I'm using langchain in my job and a recent critical vulnerability [CVE-2024-46946](https://www.mend.io/vulnerability-dat
abase/CVE-2024-46946) is creating an issue in our deployments:

langchain\_experimental (aka LangChain Experimental) 0.1
.17 through 0.3.0 for LangChain allows attackers to execute arbitrary code through sympy.sympify (which uses eval) in LL
MSymbolicMathChain. LLMSymbolicMathChain was introduced in fcccde406dd9e9b05fc9babcbeb9ff527b0ec0c6 (2023-10-05).

  
It
 seems to be up to the latest version of langchain. Are there any updates on when this will be resolved?
```
---

     
 
all -  [ A new chunking algorithm proposal - Semantically chunking based on sliding token windows and similar ](https://www.reddit.com/r/LangChain/comments/1flhtxi/a_new_chunking_algorithm_proposal_semantically/) , 2024-09-24-0912
```
[Link to the chunking algorithm](https://github.com/nesbyte/ResearchChunkingStrategies/blob/main/main.ipynb) - there are
 samples of it's output at the bottom of the notebook, feedback/comments are welcome!

The new approach uses a sliding w
indow between token embeddings and does similarity comparisons between the sliding windows, once the similarities revers
e (local minima is found), that is where a chunk break is introduced. *This approach does not require any thresholds or 
manual tuning - it is inherently dynamic (and recursive if needed)*. [More detail provided in the notebook.](https://git
hub.com/nesbyte/ResearchChunkingStrategies/blob/main/main.ipynb)

This approach is designed for larger uniform bodies of
 text.

Depending on feedback variations can be made to be able to control chunk size and also benchmark it in a similar
 method as mentioned in [Chroma's chunking strategies for retrieval](https://research.trychroma.com/evaluating-chunking)
 paper.
```
---

     
 
all -  [ Filtering nested json response ](https://www.reddit.com/r/LangChain/comments/1flefus/filtering_nested_json_response/) , 2024-09-24-0912
```
Hey all,

What's the best way give an llm contest of a json object. The API I'm calling has multiple nested Json objects
 like this:

    {
      'General': {
        'Code': 'AAPL',
        'Type': 'Common Stock',
        'Name': 'Apple',
 
     },
      'Holders': {
        'Institutions': {},
        'Funds': {
          '0': {
            'name': 'Vanguard
 International Stock Index-Total Intl Stock Indx',
            'date': '2020-10-31',
            'totalShares': 1.52,
  
          'currentShares': 26895154
          },
          '1': {
            'name': 'Vanguard Tax Managed Fund-Vanguar
d Developed Markets Index Fund',
            'date': '2020-12-31',
            'totalShares': 0.64,
            'current
Shares': 11335622
          },
      }
      'Earnings': {
        'Trend': {
          '2024-06-30': {
            'dat
e': '2025-06-30',
            'growth': '-0.0220',
            'earningsEstimateAvg': '5.6700',
            'earningsEst
imateLow': '5.0100',
            'earningsEstimateHigh': '6.2200',
          },
          '2024-03-30': {
            'd
ate': '2024-06-30',
            'growth': '-0.0140',
            'earningsEstimateAvg': '5.8000',
            'earningsE
stimateLow': '5.5100',
            'earningsEstimateHigh': '5.9000',
          },
          '2023-12-31': {
            
'date': '2024-03-31',
            'growth': null,
            'earningsEstimateAvg': '5.8000',
            'earningsEsti
mateLow': '5.5100',
            'earningsEstimateHigh': '5.9000',
          },
    }

So for example if I want to ask th
e model to 'give me the latest 3 quarters of average earnings estimates', what is the best way to give the model context
 of the json schema so that it filters the data reliably get the Earnings\['Trent'\]\['date'\]\['earningsEstimateAvg'\] 
values?

I want the model to create the filter, not have the model process the json string and provide a response, becau
se the filtered data may be hundred objects.

So far all i can think of is adding the schema to the system prompt or the
 docstring of the langgraph toolcall, but the schema could be very large.

(p.s i'm using langgraph as well)
```
---

     
 
MachineLearning -  [ [P] Swapping Embedding Models for an LLM ](https://www.reddit.com/r/MachineLearning/comments/1fktvbj/p_swapping_embedding_models_for_an_llm/) , 2024-09-24-0912
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

     
 
MachineLearning -  [ [P] Review and suggest ideas for my chatbot ](https://www.reddit.com/r/MachineLearning/comments/1fb2mwl/p_review_and_suggest_ideas_for_my_chatbot/) , 2024-09-24-0912
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

     
 
MachineLearning -  [ [P] Lessons from Retrieval Augmented Generation ](https://www.reddit.com/r/MachineLearning/comments/1f9tvg7/p_lessons_from_retrieval_augmented_generation/) , 2024-09-24-0912
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

     
 
deeplearning -  [ What is the best approach for Parsing and Retrieving Code Context Across Multiple Files in a Hierarc ](https://www.reddit.com/r/deeplearning/comments/1fh58oz/what_is_the_best_approach_for_parsing_and/) , 2024-09-24-0912
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

     
 
deeplearning -  [ Month of August in AI ](https://www.reddit.com/r/deeplearning/comments/1f6zfz0/month_of_august_in_ai/) , 2024-09-24-0912
```
🔍 I**nside this Issue:**

* 🤖 La*test Breakthroughs: *This month it’s all about A*gents, LangChain RAG, and LLMs evaluat
ion challenges.*
* 🌐 AI Monthly News: Discover how these stories are revolutionizing industries and impacting everyday l
ife: E*U AI Act, California’s Controversial SB1047 AI regulation act, Drama at OpenAI, and possible funding at OpenAI by
 Nvidia and Apple.*
* 📚 Editor’s Special: This covers the interesting talks, lectures, and articles we came across recen
tly.

Follow me on Twitter and LinkedIn at [**RealAIGuys**](https://twitter.com/RealAIGuys) and [**AIGuysEditor**](https
://www.linkedin.com/in/vishal-rajput-999164122/) to get insight on new AI developments.

>**Please don't forget to subsc
ribe to our Newsletter:** [**https://medium.com/aiguys/newsletter**](https://medium.com/aiguys/newsletter)

# Latest Bre
akthroughs

Are Agents just simple rules? Are Agents just enhanced reasoning? The answer is yes and no. Yes, in the sens
e that agents have simple rules and can sometimes enhance reasoning capabilities compared to a single prompt. But No in 
the sense that agents can have a much more diverse functionality like using specific tools, summarizing, or even followi
ng a particular style. In this blog, we look into how to set up these agents in a hierarchal manner just like running a 
small team of Authors, researchers, and supervisors.

[**How To Build Hierarchical Multi-Agent Systems?**](https://mediu
m.com/aiguys/how-to-build-hierarchical-multi-agent-systems-dc26b19201d2?sk=90958e39e1a28f5030872a90f8e3f3da)

**TextGrad
**. It is a powerful framework performing automatic “differentiation” via text. **It backpropagates textual feedback pro
vided by LLMs to improve individual components of a compound AI system.** In this framework, LLMs provide rich, general,
 natural language suggestions to optimize variables in computation graphs, ranging from code snippets to molecular struc
tures. TextGrad showed effectiveness and generality across various applications, from question-answering and molecule op
timization to radiotherapy treatment planning.

[**TextGrad: Improving Prompting Using AutoGrad**](https://medium.com/ai
guys/textgrad-controlling-llm-behavior-via-text-2a82e2073d10?sk=3633a9aa63b884c97469bce659265921)

The addition of RAG t
o LLMs was an excellent idea. It helped the LLMs to become more specific and individualized. Adding new components to an
y system leads to more interactions and its own sets of problems. Adding RAG to LLMs leads to several problems such as h
ow to retrieve the best content, what type of prompt to write, and many more.

In this blog, we are going to combine the
 **LangChain RAG with DSPy**. We deep dive into how to evaluate the RAG pipeline quantitatively using **RAGAs** and how 
to create a system where instead of manually tweaking prompts, we let the system figure out the best prompt.

[**How To 
Build LangChain RAG With DSPy?**](https://medium.com/aiguys/how-to-build-langchain-rag-with-dspy-ce9154fbafaa?sk=b41d104
05f84c767cf9cd6a58d1ebac0)

As the field of natural language processing (NLP) advances, the evaluation of large language
 models (LLMs) like GPT-4 becomes increasingly important and complex. Traditional metrics such as accuracy are often ina
dequate for assessing these models’ performance because they fail to capture the nuances of human language. In this arti
cle, we will explore why evaluating LLMs is challenging and discuss effective methods like BLEU and ROUGE for a more com
prehensive evaluation.

[**The Challenges of Evaluating Large Language Models**](https://medium.com/aiguys/the-challenge
s-of-evaluating-large-language-models-ec2eb834a349)

# AI Monthly News

# AI Act enters into force

On 1 August 2024, th
e European Artificial Intelligence Act (AI Act) enters into force. The Act aims to foster responsible artificial intelli
gence development and deployment in the EU. The AI Act introduces a uniform framework across all EU countries, based on 
a forward-looking definition of AI and a risk-based approach:

* **Minimal risk:** most AI systems such as spam filters 
and AI-enabled video games face no obligation under the AI Act, but companies can voluntarily adopt additional codes of 
conduct.
* **Specific transparency risk:** systems like chatbots must clearly inform users that they are interacting wit
h a machine, while certain AI-generated content must be labelled as such.
* **High risk:** high-risk AI systems such as 
AI-based medical software or AI systems used for recruitment must comply with strict requirements, including risk-mitiga
tion systems, high-quality of data sets, clear user information, human oversight, etc.
* **Unacceptable risk:** for exam
ple, AI systems that allow “social scoring” by governments or companies are considered a clear threat to people’s fundam
ental rights and are therefore banned.

**EU announcement:** [**Click here**](https://commission.europa.eu/news/ai-act-e
nters-force-2024-08-01_en)

https://preview.redd.it/nwyzfzgm4cmd1.png?width=828&format=png&auto=webp&s=c873db37ca0dadd5b
510bea70ac9f633b96aaea4

# California AI bill SB-1047 sparks fierce debate, Senator likens it to ‘Jets vs. Sharks’ feud


**Key Aspects of SB-1047:**

* Regulation Scope: Targets “frontier” AI models, defined by their immense computational t
raining requirements (over 10²⁶ operations) or significant financial investment (>$100 million).
* Compliance Requiremen
ts: Developers must implement safety protocols, including the ability to immediately shut down, cybersecurity measures, 
and risk assessments, before model deployment.
* Whistleblower Protections: Encourages reporting of non-compliance or ri
sks by offering protection against retaliation.
* Safety Incident Reporting: Mandates reporting AI safety incidents with
in 72 hours to a newly established Frontier Model Division.
* Certification: Developers need to certify compliance, pote
ntially under penalty of perjury in earlier drafts, though amendments might have altered this.

**Pros:**

* Safety Firs
t: Prioritizes the prevention of catastrophic harms by enforcing rigorous safety standards, potentially safeguarding aga
inst AI misuse or malfunction.
* Incentivizes Responsible Development: By setting high standards for AI model training, 
the company encourages developers to think critically about the implications of their creations.
* Public Trust: Enhance
s public confidence in AI by ensuring transparency and accountability in the development process.

**Cons:**

* Innovati
on Stagnation: Critics argue it might stifle innovation, especially in open-source AI, due to the high costs and regulat
ory burdens of compliance.
* Ambiguity: Some definitions and requirements might be too specific or broad, leading to leg
al challenges or unintended consequences.
* Global Competitiveness: There’s concern that such regulations could push AI 
development outside California or the U.S., benefiting other nations without similar restrictions.
* Implementation Chal
lenges: The practicalities of enforcing such regulations, especially the “positive safety determination,” could be compl
ex and contentious.

**News Article:** [**Click here**](https://www.thenation.com/article/society/sb-1047-ai-big-tech-fi
ght/)

**Open Letter:** [**Click here**](https://safesecureai.org/open-letter)

https://preview.redd.it/ib96d7nk4cmd1.pn
g?width=828&format=png&auto=webp&s=0ed5913b5dae72e203c8592393e469d9130ed689

# MORE OpenAI drama

OpenAI co-founder John
 Schulman has left the company to join rival AI startup Anthropic, while OpenAI president and co-founder Greg Brockman i
s taking an extended leave until the end of the year. Schulman, who played a key role in creating the AI-powered chatbot
 platform ChatGPT and led OpenAI’s alignment science efforts, stated his move was driven by a desire to focus more on AI
 alignment and hands-on technical work. Peter Deng, a product manager who joined OpenAI last year, has also left the com
pany. With these departures, only three of OpenAI’s original 11 founders remain: CEO Sam Altman, Brockman, and Wojciech 
Zaremba, lead of language and code generation.

**News Article:** [**Click here**](https://techcrunch.com/2024/08/05/ope
nai-co-founder-leaves-for-anthropic/)

https://preview.redd.it/0vdjc18j4cmd1.png?width=828&format=png&auto=webp&s=e9de60
4c26aed3e47b50df3bdf114ef61f967080

# Apple and Nvidia may invest in OpenAI

Apple, which is planning to integrate ChatG
PT into iOS, is in talks to invest. Soon after, [*Bloomberg* also](https://www.bloomberg.com/news/articles/2024-08-29/nv
idia-has-held-discussions-about-joining-openai-s-funding-round?srnd=homepage-americas) reported that Apple is in talks b
ut added that Nvidia “has discussed” joining the funding round as well. The round is reportedly being led by Thrive Capi
tal and would value OpenAI at more than $100 billion.

**News Article:** [**Click here**](https://www.theverge.com/2024/
8/29/24231626/apple-nvidia-openai-invest-microsoft)

https://preview.redd.it/ude6jguh4cmd1.png?width=828&format=png&auto
=webp&s=3603cbca0dbb1be3e6d0efcf06c3a698428bbdd6

# Editor’s Special

* The AI Bubble: Will It Burst, and What Comes Aft
er?: [**Click here**](https://www.youtube.com/watch?v=91SK90SahHc&t=317s)
* Eric Schmidt Full Controversial Interview on
 AI Revolution (Former Google CEO): [**Click here**](https://www.youtube.com/watch?v=mKVFNg3DEng)
* AI isn’t gonna keep 
improving [**Click here**](https://www.youtube.com/watch?v=Y8Ym7hMR100)
* General Intelligence: Define it, measure it, b
uild it: [**Click here**](https://www.youtube.com/watch?v=nL9jEy99Nh0)
```
---

     
