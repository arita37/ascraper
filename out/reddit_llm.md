 
all -  [ How does this LangChain agent correctly identify the tool to use? ](https://www.reddit.com/r/LangChain/comments/1ddr9hj/how_does_this_langchain_agent_correctly_identify/) , 2024-06-12-0954
```
In this [Medium article](https://medium.com/ama-tech-blog/combining-langchain-and-llamaindex-to-build-your-first-agentic
-rag-system-6e8e2e7825e7), the agent has three tools:

- 'lyft_10k': 'Provides information about Lyft financials for yea
r 2021. '

- 'uber_10k': 'Provides information about Uber financials for year 2021. '

and

- 'DuckDuckGoSearch': 'Use f
or when you need to perform an internet search to find information that another tool can not provide.'

In one of the te
st cases, the author queries the agent

    'List me the names of Uber's board of directors.'

Intuitively, one would as
sume the agent will invoke the 'uber_10k' tool. However, the agent invokes 'DuckDuckGoSearch'.

The author explains that
:
> Since this information is out-of-scope for any of the retriever tools, the agent correctly decided to invoke the ext
ernal search tool.

How does the agent know that question is out-of-scope for the 'uber_10k' retriever?
```
---

     
 
all -  [ Errors loading `langchain_anthropic` ](https://www.reddit.com/r/LangChain/comments/1ddort5/errors_loading_langchain_anthropic/) , 2024-06-12-0954
```
Recently when I try to do `import langchain_anthropic` I have been getting errors like this:
```
>>> import langchain_an
thropic
Traceback (most recent call last):
  File '<stdin>', line 1, in <module>
  File '/usr/local/lib/python3.12/site-
packages/langchain_anthropic/__init__.py', line 1, in <module>
    from langchain_anthropic.chat_models import ChatAnthr
opic, ChatAnthropicMessages
  File '/usr/local/lib/python3.12/site-packages/langchain_anthropic/chat_models.py', line 26
, in <module>
    from langchain_core.callbacks import (
  File '/usr/local/lib/python3.12/site-packages/langchain_core/
callbacks/__init__.py', line 22, in <module>
    from langchain_core.callbacks.manager import (
  File '/usr/local/lib/p
ython3.12/site-packages/langchain_core/callbacks/manager.py', line 29, in <module>
    from langsmith.run_helpers import
 get_run_tree_context
  File '/usr/local/lib/python3.12/site-packages/langsmith/run_helpers.py', line 40, in <module>
  
  from langsmith import client as ls_client
  File '/usr/local/lib/python3.12/site-packages/langsmith/client.py', line 5
2, in <module>
    from langsmith import env as ls_env
  File '/usr/local/lib/python3.12/site-packages/langsmith/env/__i
nit__.py', line 3, in <module>
    from langsmith.env._runtime_env import (
  File '/usr/local/lib/python3.12/site-packa
ges/langsmith/env/_runtime_env.py', line 10, in <module>
    from langsmith.utils import get_docker_compose_command
  Fi
le '/usr/local/lib/python3.12/site-packages/langsmith/utils.py', line 31, in <module>
    from langsmith import schemas 
as ls_schemas
  File '/usr/local/lib/python3.12/site-packages/langsmith/schemas.py', line 69, in <module>
    class Exam
ple(ExampleBase):
  File '/usr/local/lib/python3.12/site-packages/pydantic/v1/main.py', line 286, in __new__
    cls.__t
ry_update_forward_refs__()
  File '/usr/local/lib/python3.12/site-packages/pydantic/v1/main.py', line 807, in __try_upda
te_forward_refs__
    update_model_forward_refs(cls, cls.__fields__.values(), cls.__config__.json_encoders, localns, (Na
meError,))
  File '/usr/local/lib/python3.12/site-packages/pydantic/v1/typing.py', line 554, in update_model_forward_ref
s
    update_field_forward_refs(f, globalns=globalns, localns=localns)
  File '/usr/local/lib/python3.12/site-packages/p
ydantic/v1/typing.py', line 520, in update_field_forward_refs
    field.type_ = evaluate_forwardref(field.type_, globaln
s, localns or None)
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File '/usr/local/lib
/python3.12/site-packages/pydantic/v1/typing.py', line 66, in evaluate_forwardref
    return cast(Any, type_)._evaluate(
globalns, localns, set())
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: ForwardRef._evaluat
e() missing 1 required keyword-only argument: 'recursive_guard'
>>>
```
That smells like maybe there's an un-captured de
pendency from the `langchain_anthropic` code onto pydantic or something, but I don't have any great ideas about how to d
ebug this.  Anyone else seen this? Any fix or work-around?

Checking, it looks like I have `langchain-anthropic==0.1.13`
 and `langchain==0.1.20` if that helps.
```
---

     
 
all -  [ [Student] Looking for advice on resume and upcoming search, interested in product and software devel ](https://www.reddit.com/r/EngineeringResumes/comments/1ddoopc/student_looking_for_advice_on_resume_and_upcoming/) , 2024-06-12-0954
```
I'm a U.S. citizen and an upcoming senior at Cal State University, getting ready to dive into the job search. Currently 
located in the Bay Area, I attend a Cal-State near a major tech hub, which has provided me with some fantastic opportuni
ties. I've completed internships at a large, albeit controversial especially rn, tech(?) company, and I'm eager to secur
e a full-time position after grad or even a masters degree tbh. As I prepare to start applying, my primary concern is ho
w to increase my chances of getting callbacks since I didn't get as many callbacks as expected for the internship search
--still got multiple offers though. Additionally, I’m looking for advice on how to effectively incorporate another inter
nship experience from the same company into my resume, especially since the work I'm doing there differs from my previou
s role. I'm targeting roles in software engineering, particularly those involving machine learning, AI, and big data ana
lytics. I'm open to both local and remote opportunities and am willing to relocate for the right position.

’m seeking f
eedback on my resume to fine-tune it and make sure it stands out to recruiters. Specifically, I'd appreciate any advice 
on whether my technical skills and experiences are presented effectively and how I can best highlight my projects and in
ternship roles. I feel that it might go over a page tbh. The resumse says May 25 as my grad year, but i'm probably gradu
ating in december 2024. 

https://preview.redd.it/lf38t9on806d1.png?width=5100&format=png&auto=webp&s=89a0912f63dbe8a18d
4198e29893dc4632827472


```
---

     
 
all -  [ Rate my resume and tell me if this is good enough for Data/Business Analyst positions. ](https://i.redd.it/imr71o0t306d1.jpeg) , 2024-06-12-0954
```
Please guide me on what all should be added/removed. Also, can I apply for senior roles? 
```
---

     
 
all -  [ Python Projects ](https://www.reddit.com/r/learnpython/comments/1ddo02e/python_projects/) , 2024-06-12-0954
```
Any suggestions about where I can find some python projects with langchain, flask ?
```
---

     
 
all -  [ Full stack starter ](https://www.reddit.com/r/LangChain/comments/1ddm4a1/full_stack_starter/) , 2024-06-12-0954
```
I’m looking for a chatbot frontend with citations, that utilizes a fast api/langserve backend. Anyone have good suggesti
ons? 
```
---

     
 
all -  [ Newbie question: Langgraph and authenticated tools ](https://www.reddit.com/r/LangChain/comments/1ddl2k0/newbie_question_langgraph_and_authenticated_tools/) , 2024-06-12-0954
```
Hello, as a learning side project I am trying to have a simple Agent that queries an authenticated external API.  Authen
tication is with a standard Bearer token.

I have two tools, one is called fetch\_token that knows how to request a vali
d access token.  And then there is another tool which does the real work and fetches certain value from an external http
s endpoint using the previously retrieved access token.    These are non public APIs and in my tool functions I am using
 'requests' to programatically access and parse the JSON to extract the relevant values back to the Agent.

So given a u
ser's query, the Agent must invoke the first tool, fetch the access token and then invoke the second one passing the tok
en as a parameter.

The thing is working, (yay!!), even when the input of the user makes the agent call the second tool 
repeatedly with different input values (but the same access token).

But my issue is that the agent is terribly slow.  I
 suspect this happens because the bearer token (a quite long and random string, it is 2330 hexadecimal chars) is being p
assed each time to the LLM (OpenAI, 'gpt4-turbo-preview') and that takes a lot of context and processing for the LLM, wh
ich perhaps only be concerned with the fact that the access token is already present, not its value.

So I was thinking 
of storing the token in the Agent state, but I am not aware of a way that the output of a tool can be stored in the Agen
t state, and I also suspect that the whole Agent state is what is already being sent to the LLM so this would not defeat
 the purpose of this hoop.

So I am at a loss, my Agent is roughly working but is very slow!   Are there any suggestions
, resources or examples for this patterns?
```
---

     
 
all -  [ Chroma DB taking extremely long time to create. ](https://www.reddit.com/r/LangChain/comments/1ddk9b1/chroma_db_taking_extremely_long_time_to_create/) , 2024-06-12-0954
```
So this is my first time ever hearing about vector databases - I know very little about them and I'm running into some t
rouble with a simple rag script I threw together.

I followed one of langchain's documentation tutorials and was able to
 get a basic RAG setup going with some text files. Well now I'm trying to expand on it to be something useful - so I cur
rently have \~800 documents totaling to just under 50 MB of data that I want to store in the vector DB. For some reason,
 the \`Chroma.from\_documents()\` method will hang for a very long period of time (been running for over 10 minutes now)
 - and I can't seem to figure out why it's so slow.

Firstly, this \`Chroma.from\_documents\` method - is what its doing
 called 'indexing'? I keep seeing this term thrown around, not entirely sure what it means.

Second, Is it normal for cr
eating the vector store to take this long with the amount of data I have? I figured 50MB of data and only 800 documents 
would be pretty trivial, as I've seen other posts about people having millions of documents.

Any help would be apprecia
ted.

For reference, here is the relevant code:

    loader = DirectoryLoader('docs2', glob='**/*.htm', loader_cls=BSHTM
LLoader, loader_kwargs={'open_encoding': 'utf8'}, show_progress=True, use_multithreading=True)
    
    docs = loader.lo
ad()
    
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000)
    splits = text_splitter.split_documents
(docs)
    
    model = 'Alibaba-NLP/gte-large-en-v1.5'
    model_kwargs = model_kwargs = {'device':'cpu', 'trust_remote
_code': True}
    encode_kwargs = {'normalize_embeddings': True}
    embeddings = HuggingFaceEmbeddings(
        model_n
ame=model,
        model_kwargs=model_kwargs,
        encode_kwargs=encode_kwargs
    )
    
    vectorstore = Chroma.fr
om_documents(documents=splits, embedding=embeddings)
```
---

     
 
all -  [ Boost a QA Bot for your documentation with Langchain ](https://wingla.ng/qa-bot) , 2024-06-12-0954
```

```
---

     
 
all -  [ rerank-ts: TypeScript Library for Improving Search Results in RAG Applications  ](https://www.reddit.com/r/LangChain/comments/1ddhd9t/rerankts_typescript_library_for_improving_search/) , 2024-06-12-0954
```
Hi folks, we built a TypeScript library to improve search results in RAG Applications. If you are building a RAG applica
tion on top of vector indexes, re-ranking search results will always improve LLM's  response synthesis. We implemented t
wo commonly used re-ranking techniques - Reciprocal Rank Fusion(RRF) and LLM Based Re-Ranking(using Llama3 from Groq and
 GPT-4). Hope this is useful to folks building LLM Applications in React/NextJS.

Code - https://github.com/tensorlakeai
/rerank-ts 

We were building a consumer application with our open source data framework https://github.com/tensorlakeai
/indexify and were not able to find a good re-ranking library in TypeScript. So we decided to build one, and it works re
ally well to re-rank ~100 results. We get latency of around 1 second with Llama3/Groq. 

```
---

     
 
all -  [ Is there a way to add multisteps/continuation in langgraph? ](https://www.reddit.com/r/LangChain/comments/1ddg11m/is_there_a_way_to_add_multistepscontinuation_in/) , 2024-06-12-0954
```
Is there a way to implement multistep operations in LangGraph? Specifically, I'm looking to perform a series of modifica
tions where one step directly influences the next. For instance, I want to first remove the background of an image in th
e initial node, and then, in a subsequent node, use another tool to search for and replace an object. The key requiremen
t is that the second modification should be applied to the modified image from the first step, not the original image. C
an LangGraph handle this type of sequential image processing?

- I have checked langgraph documentation and found no rel
evant information
- I have tried changing and updating the way I have written the prompt to see if it affects

Any help 
is greatly appreciated :))
```
---

     
 
all -  [ Calculating LLM costs before sending requests? ](https://www.reddit.com/r/LangChain/comments/1ddft47/calculating_llm_costs_before_sending_requests/) , 2024-06-12-0954
```
Using langchain sometimes feels like gambling with costs to me. I never really know how much my requests would actually 
cost when I send it. I know there are detailed charts which we should read, but who really does? Instead I wanted to ask
 if anybody knows of an automated way to calculate costs before sending the requests? For my use case, specifically for 
OpenAI, but maybe there is another way.

And if there isnt anything like that, maybe this would be an interessting proje
ct... Like a package which calculates your LLM costs before the requests, depending on the specific platform you use
```
---

     
 
all -  [ Chainlit translation in a rag system  ](https://www.reddit.com/r/LangChain/comments/1ddfqps/chainlit_translation_in_a_rag_system/) , 2024-06-12-0954
```
I use chainlit as UI in my rag system, the first qst passes ok, but when i inser the second one it translated automaticl
y to english.
So How to strictly change translation for all users to a specific language? File xx-XX.json is placed in t
he translations folder. Deletion of en-US.json  doesn't work (it is generated each time again) 
```
---

     
 
all -  [ How to deal with this collaboration  ](https://www.reddit.com/r/SaaS/comments/1ddfn99/how_to_deal_with_this_collaboration/) , 2024-06-12-0954
```
So I contacted a company who owns a content API for travel holidays and asked them if they could allow access for me to 
build AI solutions on top it. 

Long story short, 3 months down the line I have used their API to create my own infrastr
ucture of Elasticsearch, GraohQL, Langchain and other vector dbs etc to create a chatbot with long term memory and high 
precision in getting travel packages, combined with a UI and UX custom designed. 

Now my chatbot is dependent on their 
or any other similar company's API to be able tp answer questions of customers and make recommendations. 

The current d
iscussion with the owner of this API provider is that they are willing to offer me the certain share of revenues as they
'd handle the market, sales and distribution of this chatbot any all parallel AI apps APIs I'd build. Which seems like a
 sweet deal, but silly me has not formally brought up the topic about the terms of the partnership until recently. 

The
y have put a condition that they want to host it pn their own cloud so they can launch it as rheir product and manage th
e scale etc. 

My worry is, I am giving away my IPR which if I ask myself honestly is an AI wrapper, yes but I have put 
my thinking into making it accurate. 


How do I tackle this situation? Anyone else did similar parternerships? 

TLDR; 
Need advive on how to go about my SaaS where a crucial API for content is owner but another company and they want to hos
t the SaaS on their cloud. 
```
---

     
 
all -  [ Multiple ways to get to the same result w/ RAG ](https://www.reddit.com/r/LangChain/comments/1dddjew/multiple_ways_to_get_to_the_same_result_w_rag/) , 2024-06-12-0954
```
So, I'm building this simple rag pipeline with langchain and ollama that takes in a PDF document and returns it's summar
y as bulletpoints.

    file_path = 'paper.pdf'
    loader = PyPDFLoader(file_path)
    
    docs = loader.load()
    
 
   embeddings = (OllamaEmbeddings(model='llama3'))
    
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=10
00, chunk_overlap=200)
    splits = text_splitter.split_documents(docs)
    vectorstore = Chroma.from_documents(document
s=splits, embedding=embeddings, persist_directory='emb')
    
    retriever = as_retriever(
        embeddings=embedding
s,
        chroma=vectorstore
    )
    
    prompt_template = '''Based on the following information and being really sp
ecific about it's data: '{text}'.\n\n Here are the goals, methodology, and conclusions/achievements of the paper, writte
n as bullet points:'''
    
    prompt = PromptTemplate.from_template(prompt_template)
    
    llm = Ollama(model='llam
a3')
    
    chain = (
        retriever
        | prompt
        | llm
    )
    
    result = chain.invoke({})

 The 
calling of the chain just seems too much like a workaround, since I didn't have a specific question about the reference 
document, therefore I just had to use the prompt\_template as the instruction to treat the pdf. It just seems like there
 are a lot of way to get to this same result. Whether to call the llm by it's default completion object or through it's 
chat variation. Whether to use a LLMChain(), a RetrievalQA.from\_chain\_type() or a simple chain() specifying it's commo
n parameters etc. Ins't there a way to standardize this workflow according to your needs?
```
---

     
 
all -  [ Deploying Langserve in ECS with CDK ](https://www.reddit.com/r/LangChain/comments/1ddb6qz/deploying_langserve_in_ecs_with_cdk/) , 2024-06-12-0954
```
Hi guys I was struggling for quite sometime on how to host Langserve in AWS ECS. So prepared this two repos

1st one cre
ates a VPC  [https://github.com/mathlover777/shared-vpc](https://github.com/mathlover777/shared-vpc)

2nd one deploys in
 the same VPC [https://github.com/mathlover777/langserve-cdk-ecs](https://github.com/mathlover777/langserve-cdk-ecs)

Yo
u can deployment multiple stages in the same VPC also as AWS has a soft limit on number of VPCs.

  
This does not have 
autoscale added, as I dont know how to do it myself in ecs, will update when I get time.
```
---

     
 
all -  [ Best way forward and vector db for an AI RAG system for CVs ranking using query and some metadata  ](https://www.reddit.com/r/LangChain/comments/1dd8ssq/best_way_forward_and_vector_db_for_an_ai_rag/) , 2024-06-12-0954
```
Hi guys, 
I'm working on this project where initially we have 700 csvs to be ingested and build a poc with some ui for q
uerying the csvs database with text and and metadata parameters selected via ui.


Need opinions fro experts on how to a
pproach this project, considering the production use and ingesting more cvs into ai system. 

For initial POC, I'm plann
ing to use chromadb and streamlit for UI. Better options?

I can build above RAG, but I'm asking for expert opinions kee
ping in mind the production use case and scaling to more pdfs 
```
---

     
 
all -  [ How do i parse a call to multiple tools ](https://www.reddit.com/r/LangChain/comments/1dd6poy/how_do_i_parse_a_call_to_multiple_tools/) , 2024-06-12-0954
```
When a single tool is to be used this is the output I get from Llama3 is:{'arguments': {}, 'name': 'check\_location'}

T
he logic I'm using to parse a single tool call is this:

    from operator import itemgetter
    
    
    def tool_chai
n(model_output):
        tool_map = {tool.name: tool for tool in tools}
        chosen_tool = tool_map[model_output['nam
e']]
        return itemgetter('arguments') | chosen_tool

How do i modify this for a call to multiple tools. The output
 from Llama3 is:{'tools': \[{'arguments': {}, 'name': 'check\_location'},  
{'arguments': {}, 'name': 'check\_calendar'}
\]}

I'm using Llama3, ollama and LangGraph.





Edit: I've managed to get an output like this:

'Finished running: gra
der:'  
{'tool1': {'arguments': {}, 'name': 'check\_location'},  
'tool2': {'arguments': {}, 'name': 'check\_calendar'}}


How do i parse the above?
```
---

     
 
all -  [ Can I use LangChain with Indian opensource LLMs? ](https://www.reddit.com/r/LangChain/comments/1dd6poq/can_i_use_langchain_with_indian_opensource_llms/) , 2024-06-12-0954
```
I am a beginner so this might be a pretty basic question. I wanted to know if I can use LangChain framework with LLMs ot
her than openai's GPT. My use case is related to regional languages in India so I was going to use **BharatGPT by** [**C
oRover.ai**](http://CoRover.ai) or **AI4Bharat** an opensource AI model?
```
---

     
 
all -  [ What vector db should I choose for 100m pages of text? ](https://www.reddit.com/r/LangChain/comments/1dcyc6i/what_vector_db_should_i_choose_for_100m_pages_of/) , 2024-06-12-0954
```
For context my vector db research started today from 0 knowledge and I feel absolutely unqualified to be making this dec
ision but here we are.

I have narrowed the search down to Milvus, Qdrant and potentially Weaviate.

I am scoping out a 
project for a client where we need to store up to 100 million pages. The application is scientific so retrieval precisio
n is a top priority as is search time latency and cost.

It seems:

* Milvus seems the most established and easiest to s
etup. also itis fast but takes up a lot of memory so can get quite expensive.
* Qdrant is fast and quite a bit cheaper t
han Milvus but lacks dynamic sharding 
* I have seen two conflicting reports one saying Weaviate is incredibly quick wit
h a benchmark of 0.12s for a particular query which took Milvus 0.9s to perform the same and then another where it says 
it is slow. and it is the cheapest.
* PG-vector is not as performant as the dedicated vector stores but are tried and te
sted part of the ecosystem and anecdotally great to work with 
* Chroma is not the best for accurate retrieval and I hav
en't heard many recommending it as the best except for its usability and ease of integration. 


```
---

     
 
all -  [ How to handle ambiguous column names when converting Text-to-SQL in SQL Agent? ](https://www.reddit.com/r/LangChain/comments/1dcvnzv/how_to_handle_ambiguous_column_names_when/) , 2024-06-12-0954
```
**I have 2 cases of ambiguity** 

1. Similar names within a table - Eg: constrained\_demand, unconstrained\_demand

2.  
Same names across different tables. - Sales in both table1 and table 2

I have built a chatbot using open-ai tools agent
s , giving it access to SQLDatabaseToolKit. There is prefix, suffix and FewShotPrompt Template to handle multiple differ
ent calculations and complexities of SQL queries. Now user can ask multiple queries of the below format .

**Examples:**


1. What is the demand for 2024? - there is ambiguity as to if the user is asking constrained demand or unconstrained d
emand. Assumption that is no 'demand' column . Expectation - LLM should figure out such ambiguity without any hardcoding
 and then ask back the user as to which column he is referring to. Once LLM gets user input, then query with the new inf
o.

2. What is the sales for brand1?  there is ambiguity as to if the user is asking sales from table1 or table2. Expect
ation - LLM should figure out such ambiguity without any hardcoding and then ask back the user as to which table he is r
eferring to. Once LLM gets user input, then query with the new info.

  
Cannot handle this in column description as eve
n if the descriptions are different, we cannot make sense from the question. Need help in how to approach this. TIA!
```
---

     
 
all -  [ What are you studying, courses are you taken, personal project are you working on to keep up with th ](https://www.reddit.com/r/datascience/comments/1dcudnn/what_are_you_studying_courses_are_you_taken/) , 2024-06-12-0954
```
If you are working with classic ML and basic statistics in your current job, and new jobs require knowledge of LLMs and 
RAG based system with knowledge in langchain and prompt engineering, How can I land a job then?
```
---

     
 
all -  [ What markup language, if any, does PyPDFLoader extract equations as? ](https://www.reddit.com/r/LangChain/comments/1dcs5k0/what_markup_language_if_any_does_pypdfloader/) , 2024-06-12-0954
```
So, as the title says, for equations in a PDF, what markup language does the module PyPDFLoader use to represent math eq
uations? For example, it extracted an equation from the document as  '\n( )\n101\n10RMNT\nHH+−\n=' . Is that some sort o
f markup language, or is it just gibberish?
```
---

     
 
all -  [ Has Anyone Integrated Langgraph with Google Vertex AI Reasoning Engine? ](https://www.reddit.com/r/LangChain/comments/1dcqnw9/has_anyone_integrated_langgraph_with_google/) , 2024-06-12-0954
```
Hi everyone,

I'm currently working on a project where I've been using Langchain Agent Template from Reasoning Engine Do
cs. Recently, I came across Langgraph and now I want to try it to leverage its multi-agent functionality.

I'd like to k
now if anyone here has experience integrating Langgraph with Google Vertex AI Reasoning Engine.

I've already tested the
 reasoning engine locally, but I encounter issues when running the set\_up method on the deployed version in the reasoni
ng engine. I just want to know if anyone has experience doing this.

Thanks in advance!
```
---

     
 
all -  [ How to get AI Agent to do follow up questions and remember/apply previous request/arguments?
 ](https://www.reddit.com/r/LangChain/comments/1dcprk4/how_to_get_ai_agent_to_do_follow_up_questions_and/) , 2024-06-12-0954
```
Here is my project repo: [https://github.com/saminkhan1/realtor-project](https://github.com/saminkhan1/realtor-project)


I am building a AI agent using langgraph that talks to a SQL database to get information about real estate data. The qu
estions were:

1. What properties are available in New York?
2. Show me houses with at least 3 bedrooms and 2 bathrooms.

3. Do you have any properties under $500,000?

It knew I was looking for houses in NY for the second question, but in t
he third it didn't understand I want houses in NY, 3 bed 2 bath and less then 500k it only searched for houses in NY und
er 500k.

================================ Human Message =================================

What properties are availabl
e in New York?

================================== Ai Message ==================================

Here are some properti
es available in New York:

1. Price: $175,000
   * Beds: 3
   * Baths: 1
   * Acre Lot: 60
   * Address: 553526 Berlin, 
New York, 12022
   * House Size: 1176 sqft
2. Price: $425,000
   * Beds: 3
   * Baths: 2
   * Acre Lot: 2.02
   * Addres
s: 263302 Claverack, New York, 12521
   * House Size: 1600 sqft
   * Previous Sold Date: November 24, 2021
3. Price: $22
5,000
   * Beds: 4
   * Baths: 2
   * Acre Lot: 0.24
   * Address: 871278 Copake, New York, 12521
   * House Size: 1239 
sqft
   * Previous Sold Date: February 1, 2018
4. Price: $419,000
   * Beds: 3
   * Baths: 3
   * Acre Lot: 1.9
   * Add
ress: 286373 Copake, New York, 12516
   * House Size: 1800 sqft

Let me know if you need more information or if you have
 any specific preferences.

================================ Human Message =================================

Show me ho
uses with at least 3 bedrooms and 2 bathrooms.

================================== Ai Message ==========================
========

Here are houses in New York with at least 3 bedrooms and 2 bathrooms:

1. Price: $425,000
   * Beds: 3
   * Ba
ths: 2
   * Acre Lot: 2.02
   * Address: 263302 Claverack, New York, 12521
   * House Size: 1600 sqft
   * Previous Sold
 Date: November 24, 2021
2. Price: $225,000
   * Beds: 4
   * Baths: 2
   * Acre Lot: 0.24
   * Address: 871278 Copake, 
New York, 12521
   * House Size: 1239 sqft
   * Previous Sold Date: February 1, 2018
3. Price: $419,000
   * Beds: 3
   
* Baths: 3
   * Acre Lot: 1.9
   * Address: 286373 Copake, New York, 12516
   * House Size: 1800 sqft
4. Price: $365,000

   * Beds: 3
   * Baths: 2
   * Acre Lot: 2.0
   * Address: 78544 Copake, New York, 12517
   * House Size: 1482 sqft

L
et me know if you would like more details or if you have any specific preferences.

================================ Hum
an Message =================================

Do you have any properties under $500,000?

==============================
==== Ai Message ==================================

I found some properties in New York under $500,000:

1. Price: $175,
000
   * Beds: 3
   * Baths: 1
   * Acre Lot: 60.0
   * Address: 553526 Berlin, New York, 12022
   * House Size: 1176 sq
ft
2. Price: $425,000
   * Beds: 3
   * Baths: 2
   * Acre Lot: 2.02
   * Address: 263302 Claverack, New York, 12521
   
* House Size: 1600 sqft
   * Previous Sold Date: November 24, 2021
3. Price: $225,000
   * Beds: 4
   * Baths: 2
   * Ac
re Lot: 0.24
   * Address: 871278 Copake, New York, 12521
   * House Size: 1239 sqft
   * Previous Sold Date: February 1
, 2018
4. Price: $419,000
   * Beds: 3
   * Baths: 3
   * Acre Lot: 1.9
   * Address: 286373 Copake, New York, 12516
   
* House Size: 1800 sqft
5. Price: $365,000
   * Beds: 3
   * Baths: 2
   * Acre Lot: 2.0
   * Address: 78544 Copake, New
 York, 12517
   * House Size: 1482 sqft

Let me know if you need more information on any of these properties or if you h
ave any specific preferences.
```
---

     
 
all -  [ anyone interested in collaboration? ](https://www.reddit.com/r/LangChain/comments/1dcpmw4/anyone_interested_in_collaboration/) , 2024-06-12-0954
```
Hey Folks,

  
I wanted to ping the community to see if anyone would be interested in joining a few of us in our generat
ive AI project. We're trying to set up pipelines to help companies utilize RAG pipelines. 

  
I don't want to waste any
one's time either. To be transparent, we're actively seeking and courting investors, so we can't offer monetary compensa
tion until that happens. However, with the current investment in Gen AI and with what we're building, I'm confident this
 won't be the case for long. We're happy to cover essential development costs and resources as needed. I know that sound
s all just promises, but I want to be as upfront as possible. 

  
Feel free to DM me if interested! 
```
---

     
 
all -  [ How do I improve context retrieved? ](https://www.reddit.com/r/LangChain/comments/1dcnfb7/how_do_i_improve_context_retrieved/) , 2024-06-12-0954
```
Hey everyone, I am a Comp. Sci. student and I am using LangChain for one of my projects. I am working with transcription
 of a video. I was storing each speech segment as text and speaker and timestamp as metadata to a Chroma collection.

Ho
wever, I have two problems:
- I couldn't manage to filter by speaker. I tried adding filter=[{speaker: speaker_1}] to re
triever and also self query retriever but both did not work
- Some context's are omitted due to how I store data. For ex
ample, if speaker_1 asks 'Where were you ar yesterday?' and speaker_2 says 'at home'. When I query where was speaker_2 a
t yesterday, I see that speaker_1's question is retrieved as context but not the answer, so I cannot get the answer. 

I
 also did not want to include the last part of the previous sentence as it would make the timestamp accuracy problematic
 which is important for my project. I may add each previous sentence as metadata but I don't know if this is way to go. 
Any ideas?
```
---

     
 
all -  [ PDF Table Extraction, the Definitive Guide (+ gmft release!) ](https://www.reddit.com/r/LangChain/comments/1dclawv/pdf_table_extraction_the_definitive_guide_gmft/) , 2024-06-12-0954
```
People of r/LangChain, 

Like many of you ([1](https://www.reddit.com/r/LocalLLaMA/comments/1am3fz8/how_to_recover_docum
ent_structure_and_plain_text/)) ([2](https://www.reddit.com/r/LangChain/comments/1cn0z11/extract_tables_from_pdf_for_rag
/)) ([3](https://www.reddit.com/r/LangChain/comments/17c7g9b/anyone_worked_on_reading_pdf_with_tables/)), I have been se
arching for a reasonable way to extract precious tables from pdfs for RAG for quite some time. Despite this seemingly si
mple problem, I've been surprised at just how unsolved this problem is. Despite a ton of options (see below), surprising
ly few of them 'just work'. Some users have even suggested paid APIs like Mathpix and Adobe Extract.

In an effort to co
nsolidate all the options out there, I've made a guide for many existing pdf table extraction options, with links to qui
ckstarts, Colab Notebooks, and github repos. I've written [colab notebooks](https://drive.google.com/drive/u/0/folders/1
14bWRj5H4aE-BA5UKH9S5ol8LC6vhqfR) that let you extract tables using methods like pdfplumber, pymupdf, nougat, open-parse
, deepdoctection, surya, and unstructured. To be as objective as possible, I've also compared the options with the same 
3 papers: [PubTables-1M (tatr)](https://arxiv.org/abs/2110.00061), the classic [Attention](https://arxiv.org/abs/1706.03
762) paper, and a [very challenging nmr table](http://ccc.chem.pitt.edu/wipf/Web/NMR_Impurities.pdf).

# gmft release

O
n top of this, I'm thrilled to announce [gmft](https://github.com/conjuncts/gmft) (**g**ive **m**e the **f**ormatted **t
**ables), a deep table recognition relying on Microsoft's TATR. Partially written out of exasperation, it is about an *o
rder of magnitude faster* than most deep competitors like nougat, open-parse, unstructured and deepdoctection. It runs o
n **cpu** (!) at around 1.381 s/page; it additionally takes ~0.945s for each table converted to df. The reason why it's 
so fast is that gmft does not rerun OCR. In many cases, the existing OCR is already good or even better than tesseract o
r other OCR software, so there is no need for expensive OCR. But gmft still allows for OCR downstream by outputting an i
mage of the cropped table.

I also think gmft's quality is unparalleled, especially in terms of value alignment to row/c
olumn header! It's easiest to see the results ([colab](https://colab.research.google.com/drive/1fEqsTdKcO5RNPV_b2v9cB4Y5
We9Kv-hR)) ([github](https://github.com/conjuncts/gmft/blob/main/notebooks/bulk_extract.ipynb)) for yourself. I invite t
he reader to explore all the notebooks to survey your own use cases and compare see each option's strengths and weakness
es.

Some weaknesses of gmft include no rotated table support (yet), false positives when rotated, and a current lack of
 support for multi-indexes (multiple row headers). However, gmft's major strength is alignment. Because of the underlyin
g algorithm, values are usually correctly aligned to their row or column header, even when there are other issues with T
ATR. This is in contrast with other options like unstructured, open-parse, which may fail first on alignment. Anecdotall
y, I've personally extracted ~4000 pdfs with gmft on cpu, and (barring occassional header issues) the quality is excelle
nt. Again, take a look at [this notebook](https://colab.research.google.com/drive/1fEqsTdKcO5RNPV_b2) for the table qual
ity.

# Comparison

All the quickstarts that I have made/modified are in [this google drive folder](https://drive.google
.com/drive/u/0/folders/114bWRj5H4aE-BA5UKH9S5ol8LC6vhqfR); the installations should all work with google colab.

The mos
t up-to-date table of all comparisons is [here](https://docs.google.com/spreadsheets/d/12IhxHZbYF71dPl32PQpF_6pg9e9S8f9W
4sTHt-B0KTg/edit#gid=0); my calculations for throughput is [here](https://docs.google.com/spreadsheets/d/12IhxHZbYF71dPl
32PQpF_6pg9e9S8f9W4sTHt-B0KTg/edit#gid=39227585).

I have undoubtedly missed some options. In particular, I have not had
 the chance to evaluate paddleocr. As a stopgap, see [this](https://medium.com/@malshanCS/automating-table-data-extracti
on-tools-and-techniques-for-efficiency-a29df313cbda#629d) writeup. If you'd like an option added to the table, please le
t me know!

## Table
[See google sheets!](https://docs.google.com/spreadsheets/d/12IhxHZbYF71dPl32PQpF_6pg9e9S8f9W4sTHt-
B0KTg/edit#gid=0) Table is too big for reddit to format.
```
---

     
 
all -  [ Agentic RAG with Different Vector Stores ](https://www.reddit.com/r/LangChain/comments/1dcjs4r/agentic_rag_with_different_vector_stores/) , 2024-06-12-0954
```
I am looking to build a RAG chatbot. My data-sources are classified into about 3 specific domains, and I want my RAG bot
 to know the difference between these domains and query only the necessary datasets, depending on the query.

I primaril
y work with Langchain and have embedded all my data-sources into a FAISS vector database (I tried ChromaDB, but found be
tter results with FAISS, lmk if you have better suggestions).  
  
I used several of Langchain's retrievers, like the Mu
ltiVectorRetriever, a BM25 retriever and even tried pooling everything together with an EnsembleRetriever.

Though I get
 'passable' responses, more often than not, the model gets confused by the several retrieved documents. For a given quer
y, my FAISS retriever pulls relevant documents from all the available data sources (as they are embedded in the same vec
torstore). These data sources corrupt the quality of the generated response, as my LLM is now summarizing a document fro
m domain B, when the question was clearly about domain A.

I understand that I cant expect perfect results from any RAG 
architecture, but I feel like a lot of my current issues will be solved if I figure out a way to teach the model to know
 the difference between the different data sources.

I considered metadata filtering (with PGVector in Langchain), but a
m pretty sure that this wont work, as my data-sources aren't metadata rich.  The only metadata I could have is the domai
n key.

So, what if I embed my different domains in different vector databases and use a Langchain agent function call t
o have the LLM selectively retrieve docs from each vectorstore depending on the question? I will probably be making more
 LLM calls and have some latency, but is this feasible?
```
---

     
 
all -  [ Same program gives different results when executed directly compared to when executed as a function ](https://www.reddit.com/r/ollama/comments/1dcihxu/same_program_gives_different_results_when/) , 2024-06-12-0954
```
Here is a program i've created using Ollama, LangGraph and Llama3:

    from langchain_community.chat_models import Chat
Ollama
    from langchain_core.output_parsers import JsonOutputParser
    from langchain_core.prompts import PromptTempl
ate
    from langchain_community.chat_models import ChatOllama
    from langchain_core.output_parsers import JsonOutputP
arser
    from langchain_core.prompts import PromptTemplate
    from langgraph.graph import END, StateGraph
    from ppr
int import pprint
    from langchain_core.output_parsers import StrOutputParser
    from typing import TypedDict
    imp
ort mod
    from langchain.tools.render import render_text_description
    
    
    
    
    local_llm = 'llama3:8b'
 
   
    
    tools = [mod.check_calendar,mod.check_location,mod.send_message,mod.receive_call,mod.getContactInfo,mod.mut
e]
    rendered_tools = render_text_description(tools)
    print(rendered_tools)
    
    from operator import itemgette
r
    
    
    def tool_chain(model_output):
        tool_map = {tool.name: tool for tool in tools}
        chosen_tool
 = tool_map[model_output['name']]
        return itemgetter('arguments') | chosen_tool
    
    
    contextllm = ChatOl
lama(model=local_llm, format='json', temperature=0)
    
    prompt = PromptTemplate(
        template='''<|begin_of_tex
t|><|start_header_id|>system<|end_header_id|> You are a helpful agent who will answer the user's question to the best of
 your abilities using one or more of the tools available to you\n
        You have access to the following tools. Here i
s the name and description of the tools:%s\n
        Return the name and input of the tool to use.
        Return your r
esponse as a JSON blob with 'name' and 'arguments' keys.
        The value associated with the 'arguments' key should be
 a dictionary of parameters.
        You are not allowed to return blank results
         <|eot_id|><|start_header_id|>u
ser<|end_header_id|>
         {inp}. Who is calling?\n
         <|eot_id|><|start_header_id|>assistant<|end_header_id|>

        '''%rendered_tools,
        input_variables=['inp'],
    )
    
    contextgatherer_chain = prompt | contextllm 
| JsonOutputParser() | tool_chain
    
    
    
    actionllm = ChatOllama(model=local_llm, format='json', temperature=
0)
    prompt = PromptTemplate(
        template='''<|begin_of_text|><|start_header_id|>system<|end_header_id|> You are 
a helpful agent who will select which tool is to be used depending on the context provided by the user and some rules.\n

        You have access to the following tools. Here is the name and description of the tools:%s\n
        Return the n
ame and input of the tool to use.
        Return your response as a JSON blob with 'name' and 'arguments' keys.
        
The value associated with the 'arguments' key should be a dictionary of parameters.
        You are not allowed to retur
n blank results
         <|eot_id|><|start_header_id|>user<|end_header_id|>
         Context:{context}\n
         {inp}.
\n\n
        Rules for tool calling:\n
        If the caller is 'Kau', the tool to be used is 'receive_call'\n
        I
f the caller is 'Priya', the tool to be used is 'send_message'\n
        For all other numbers, the tool to be used is '
mute'\n
         <|eot_id|><|start_header_id|>assistant<|end_header_id|>
        '''%rendered_tools,
        input_varia
bles=['context','inp'],
    )
    
    actiontaker_chain = prompt | actionllm | JsonOutputParser() 
    
    
    class 
GraphState(TypedDict):
        '''
        Represents the state of our graph.
    
        Attributes:
            input
: User input
            generation: LLM generation
            cl: Contact list
            rs: Relationship list
     
       cal: Calendar
            ct: Current time
        '''
        
        input:str
        generation: str
       
 cl:str
        rs:str
        cal:str
        ct:str
        con:str
    
    
    def callhandler(state):
        '''

        Gathers the context and determines whether to receive the call or send a message 
    
        Args:
           
 state (dict): The current graph state
    
        Returns:
            state (dict): Whether to send a message, receiv
e the call, or mute the call
        '''
    
        print('---HANDLING---')
        i = state['input']
        c=state
['con']
    
    
        res1 = contextgatherer_chain.invoke({'inp':i})
        res2 = actiontaker_chain.invoke({'conte
xt':res1,'inp':i})
        return {'generation': res2}
    
    
    
    workflow = StateGraph(GraphState)
    workflow
.add_node('callhandler', callhandler) 
    workflow.set_entry_point('callhandler')
    workflow.add_edge('callhandler',E
ND)
    app = workflow.compile()
    
    
    e='incoming call from +911234567890'inputs = {'input': e}
    for output 
in app.stream(inputs):
        for key, value in output.items():
            pprint(f'Finished running: {key}:')
       
     pprint(value['generation'])

The output for the above is:

---HANDLING---

'Finished running: callhandler:'

{'argu
ments': {'message': '', 'recipient': '+911234567890'},

'name': 'send\_message'}

When i try to run the same program by 
enclosing the entire thing as a function( as i want to import this into another file) like this:

    def PA():
        
from langchain_community.chat_models import ChatOllama
        from langchain_core.output_parsers import JsonOutputParse
r
        from langchain_core.prompts import PromptTemplate
        from langchain_community.chat_models import ChatOlla
ma
        from langchain_core.output_parsers import JsonOutputParser
        from langchain_core.prompts import PromptT
emplate
        from langgraph.graph import END, StateGraph
        from pprint import pprint
        from langchain_cor
e.output_parsers import StrOutputParser
        from typing import TypedDict
        import mod
        from langchain.t
ools.render import render_text_description
    
    
    
    
        local_llm = 'llama3:8b'
    
    
        tools =
 [mod.check_calendar,mod.check_location,mod.send_message,mod.receive_call,mod.getContactInfo,mod.mute]
        rendered_
tools = render_text_description(tools)
        print(rendered_tools)
    
        from operator import itemgetter
    
 
   
        def tool_chain(model_output):
            tool_map = {tool.name: tool for tool in tools}
            chosen_
tool = tool_map[model_output['name']]
            return itemgetter('arguments') | chosen_tool
    
    
        context
llm = ChatOllama(model=local_llm, format='json', temperature=0)
    
        prompt = PromptTemplate(
            templa
te='''<|begin_of_text|><|start_header_id|>system<|end_header_id|> You are a helpful agent who will answer the user's que
stion to the best of your abilities using one or more of the tools available to you\n
            You have access to the
 following tools. Here is the name and description of the tools:%s\n
            Return the name and input of the tool t
o use.
            Return your response as a JSON blob with 'name' and 'arguments' keys.
            The value associate
d with the 'arguments' key should be a dictionary of parameters.
            You are not allowed to return blank results

            <|eot_id|><|start_header_id|>user<|end_header_id|>
            {inp}. Who is calling?\n
            <|eot_i
d|><|start_header_id|>assistant<|end_header_id|>
            '''%rendered_tools,
            input_variables=['inp'],
  
      )
    
        contextgatherer_chain = prompt | contextllm | JsonOutputParser() | tool_chain
    
    
    
      
  actionllm = ChatOllama(model=local_llm, format='json', temperature=0)
        prompt = PromptTemplate(
            tem
plate='''<|begin_of_text|><|start_header_id|>system<|end_header_id|> You are a helpful agent who will select which tool 
is to be used depending on the context provided by the user and some rules.\n
            You have access to the followi
ng tools. Here is the name and description of the tools:%s\n
            Return the name and input of the tool to use.
 
           Return your response as a JSON blob with 'name' and 'arguments' keys.
            The value associated with t
he 'arguments' key should be a dictionary of parameters.
            You are not allowed to return blank results
       
     <|eot_id|><|start_header_id|>user<|end_header_id|>
            Context:{context}\n
            {inp}.\n\n
         
   Rules for tool calling:\n
            If the caller is 'Kau', the tool to be used is 'receive_call'\n
            If 
the caller is 'Priya', the tool to be used is 'send_message'\n
            For all other numbers, the tool to be used is
 'mute'\n
            <|eot_id|><|start_header_id|>assistant<|end_header_id|>
            '''%rendered_tools,
          
  input_variables=['context','inp'],
        )
    
        actiontaker_chain = prompt | actionllm | JsonOutputParser() 

    
    
        class GraphState(TypedDict):
            '''
            Represents the state of our graph.
    
    
        Attributes:
                input: User input
                generation: LLM generation
                cl: Con
tact list
                rs: Relationship list
                cal: Calendar
                ct: Current time
         
   '''
            
            input:str
            generation: str
            cl:str
            rs:str
            
cal:str
            ct:str
            con:str
    
    
        def callhandler(state):
            '''
            Gat
hers the context and determines whether to receive the call or send a message 
    
            Args:
                st
ate (dict): The current graph state
    
            Returns:
                state (dict): Whether to send a message, r
eceive the call, or mute the call
            '''
    
            print('---HANDLING---')
            i = state['input'
]
            c=state['con']
    
    
            res1 = contextgatherer_chain.invoke({'inp':i})
            res2 = act
iontaker_chain.invoke({'context':res1,'inp':i})
            return {'generation': res2}
    
    
    
        workflow 
= StateGraph(GraphState)
        workflow.add_node('callhandler', callhandler) 
        workflow.set_entry_point('callha
ndler')
        workflow.add_edge('callhandler',END)
        app = workflow.compile()
    
    
        file1=open('cont
actlist','r')
        file2=open('relationships','r')
        file3=open('calendar','r')
        s1=file1.read()
       
 s2=file2.read()
        s3=file3.read()
        curt='11:00.'
        e='incoming call from +911234567890'
        f=s1
+'\n\n'+s2+'\n\n'+s3+'\n\n'+curt+'\n\n'+e
        print(f)
        inputs = {'input': e}
        for output in app.strea
m(inputs):
            for key, value in output.items():
                pprint(f'Finished running: {key}:')
           
     pprint(value['generation'])
    
    PA()

The output i get is:

---HANDLING---

'Finished running: callhandler:'


{'arguments': {'caller': '+911234567890'}, 'name': 'receive\_call'}

Here is the 'mod' file in which ive defined the too
ls available to the LLM:

    import os
    from langchain_core.tools import tool
    from typing import Annotated, Sequ
ence, TypedDict
    from langchain.agents import AgentExecutor, create_react_agent
    from langchain_core.messages impo
rt BaseMessage, HumanMessage
    from langchain_openai import ChatOpenAI
    from langchain_core.runnables import Runnab
lePassthrough
    from langchain_core.output_parsers import StrOutputParser
    from langchain_core.prompts import ChatP
romptTemplate, MessagesPlaceholder
    from langchain.output_parsers.openai_functions import JsonOutputFunctionsParser
 
   import functools
    from langgraph.graph import StateGraph, END
    import operator
    import openai
    import tim
e
    import random
    from langchain_community.chat_models import ChatOllama
    from langchain_core.output_parsers im
port JsonOutputParser
    from langchain_core.prompts import PromptTemplate
    from langchain_core.runnables import Run
nable
    from langchain_core.exceptions import OutputParserException
    from langchain.tools.render import render_text
_description_and_args
    from pprint import pprint
    
    
    
    u/tool
    def check_calendar() -> str:
        '
''Retrieve the list of current events from the user's calender. This tool must be used only if the 'context' provided by
 the user is empty'''
        file=open('calendar','r')
        s=file.read()
        return s
    
    u/tool
    def g
etContactInfo()->str:
        '''Retreive the the user's contact list to determine who is calling when given an unknown 
number'''
        file=open('contactlist','r')
        s=file.read()
        return s
    
    @tool
    def check_locat
ion() -> str:
        '''Retrieve the current location of the user. This tool must be used only if the 'context' provide
d by the user is empty'''
        return 'your location is Bengaluru'
    
    @tool
    def send_message(recipient: str
, message: str) -> str:
        '''Send a text message to the specified recipient with the provided message content. Thi
s tool must be used only if the 'context' provided by the user is not empty'''
        return f'Sent message to {recipie
nt}: {message}'
    
    @tool
    def make_call(recipient: str) -> str:
        '''Initiate  a phone call to the specif
ied recipient. This tool must be used only if the 'context' provided by the user is not empty'''
        return f'Callin
g {recipient}...'
    
    @tool
    def receive_call(caller: str) -> str:
        '''Handle an incoming phone call from
 the specified caller. This tool must be used only if the 'context' provided by the user is not empty'''
        return 
f'Receiving call from {caller}...'
    
    @tool
    def op1(f:int,s:int)->dict:
        '''adds f and s'''
        ret
urn {'answer':f*s}
    @tool
    def op2(f:int,s:int)->dict:
        '''subtracts f and s'''
        return {'answer':f*
s}
    
    @tool
    def getWeather(city:str):
        '''returns the weather in 'city'''
        return 'cloudy'
    

    @tool
    def mute():
        '''Mute an incoming call'''
        return

I have my reasons for structuring it this 
way.

Can someone please tell me why I'm getting different outputs?
```
---

     
 
all -  [ Same program gives different results when executed directly compared to when executed as a function ](https://www.reddit.com/r/learnpython/comments/1dcihe2/same_program_gives_different_results_when/) , 2024-06-12-0954
```
Here is a program i've created using Ollama, LangGraph and Llama3:

Version 1

    from langchain_community.chat_models 
import ChatOllama
    from langchain_core.output_parsers import JsonOutputParser
    from langchain_core.prompts import 
PromptTemplate
    from langchain_community.chat_models import ChatOllama
    from langchain_core.output_parsers import 
JsonOutputParser
    from langchain_core.prompts import PromptTemplate
    from langgraph.graph import END, StateGraph
 
   from pprint import pprint
    from langchain_core.output_parsers import StrOutputParser
    from typing import TypedD
ict
    import mod
    from langchain.tools.render import render_text_description
    
    
    
    
    local_llm = 'l
lama3:8b'
    
    
    tools = [mod.check_calendar,mod.check_location,mod.send_message,mod.receive_call,mod.getContactI
nfo,mod.mute]
    rendered_tools = render_text_description(tools)
    print(rendered_tools)
    
    from operator impor
t itemgetter
    
    
    def tool_chain(model_output):
        tool_map = {tool.name: tool for tool in tools}
        
chosen_tool = tool_map[model_output['name']]
        return itemgetter('arguments') | chosen_tool
    
    
    contextl
lm = ChatOllama(model=local_llm, format='json', temperature=0)
    
    prompt = PromptTemplate(
        template='''<|b
egin_of_text|><|start_header_id|>system<|end_header_id|> You are a helpful agent who will answer the user's question to 
the best of your abilities using one or more of the tools available to you\n
        You have access to the following to
ols. Here is the name and description of the tools:%s\n
        Return the name and input of the tool to use.
        Re
turn your response as a JSON blob with 'name' and 'arguments' keys.
        The value associated with the 'arguments' ke
y should be a dictionary of parameters.
        You are not allowed to return blank results
         <|eot_id|><|start_h
eader_id|>user<|end_header_id|>
         {inp}. Who is calling?\n
         <|eot_id|><|start_header_id|>assistant<|end_h
eader_id|>
        '''%rendered_tools,
        input_variables=['inp'],
    )
    
    contextgatherer_chain = prompt | 
contextllm | JsonOutputParser() | tool_chain
    
    
    
    actionllm = ChatOllama(model=local_llm, format='json', t
emperature=0)
    prompt = PromptTemplate(
        template='''<|begin_of_text|><|start_header_id|>system<|end_header_id
|> You are a helpful agent who will select which tool is to be used depending on the context provided by the user and so
me rules.\n
        You have access to the following tools. Here is the name and description of the tools:%s\n
        R
eturn the name and input of the tool to use.
        Return your response as a JSON blob with 'name' and 'arguments' key
s.
        The value associated with the 'arguments' key should be a dictionary of parameters.
        You are not allow
ed to return blank results
         <|eot_id|><|start_header_id|>user<|end_header_id|>
         Context:{context}\n
    
     {inp}.\n\n
        Rules for tool calling:\n
        If the caller is 'Kau', the tool to be used is 'receive_call'\
n
        If the caller is 'Priya', the tool to be used is 'send_message'\n
        For all other numbers, the tool to b
e used is 'mute'\n
         <|eot_id|><|start_header_id|>assistant<|end_header_id|>
        '''%rendered_tools,
        
input_variables=['context','inp'],
    )
    
    actiontaker_chain = prompt | actionllm | JsonOutputParser() 
    
    

    class GraphState(TypedDict):
        '''
        Represents the state of our graph.
    
        Attributes:
      
      input: User input
            generation: LLM generation
            cl: Contact list
            rs: Relationship
 list
            cal: Calendar
            ct: Current time
        '''
        
        input:str
        generation: 
str
        cl:str
        rs:str
        cal:str
        ct:str
        con:str
    
    
    def callhandler(state):
 
       '''
        Gathers the context and determines whether to receive the call or send a message 
    
        Args:

            state (dict): The current graph state
    
        Returns:
            state (dict): Whether to send a mess
age, receive the call, or mute the call
        '''
    
        print('---HANDLING---')
        i = state['input']
    
    c=state['con']
    
    
        res1 = contextgatherer_chain.invoke({'inp':i})
        res2 = actiontaker_chain.inv
oke({'context':res1,'inp':i})
        return {'generation': res2}
    
    
    
    workflow = StateGraph(GraphState)
 
   workflow.add_node('callhandler', callhandler) 
    workflow.set_entry_point('callhandler')
    workflow.add_edge('cal
lhandler',END)
    app = workflow.compile()
    
    
    e='incoming call from +911234567890'inputs = {'input': e}
    
for output in app.stream(inputs):
        for key, value in output.items():
            pprint(f'Finished running: {key}
:')
            pprint(value['generation'])

The output for the above is:

---HANDLING---

'Finished running: callhandle
r:'

{'arguments': {'message': '', 'recipient': '+911234567890'},

'name': 'send\_message'}

  


When i try to run the 
exact same code by enclosing the entire thing as a function called PA( as i want to import this into another file) like 
this:

Version 2

    def PA():
      #Exact same code as above
    PA()

The output i get is:

---HANDLING---

'Finishe
d running: callhandler:'

{'arguments': {'caller': '+911234567890'}, 'name': 'receive\_call'}

  


For reference, here 
is the 'mod' file in which I've defined the tools available to the LLM:

    import os
    from langchain_core.tools imp
ort tool
    from typing import Annotated, Sequence, TypedDict
    from langchain.agents import AgentExecutor, create_re
act_agent
    from langchain_core.messages import BaseMessage, HumanMessage
    from langchain_openai import ChatOpenAI

    from langchain_core.runnables import RunnablePassthrough
    from langchain_core.output_parsers import StrOutputPars
er
    from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
    from langchain.output_parsers.open
ai_functions import JsonOutputFunctionsParser
    import functools
    from langgraph.graph import StateGraph, END
    i
mport operator
    import openai
    import time
    import random
    from langchain_community.chat_models import ChatO
llama
    from langchain_core.output_parsers import JsonOutputParser
    from langchain_core.prompts import PromptTempla
te
    from langchain_core.runnables import Runnable
    from langchain_core.exceptions import OutputParserException
   
 from langchain.tools.render import render_text_description_and_args
    from pprint import pprint
    
    
    
    u/
tool
    def check_calendar() -> str:
        '''Retrieve the list of current events from the user's calender. This tool
 must be used only if the 'context' provided by the user is empty'''
        file=open('calendar','r')
        s=file.re
ad()
        return s
    
    u/tool
    def getContactInfo()->str:
        '''Retreive the the user's contact list to 
determine who is calling when given an unknown number'''
        file=open('contactlist','r')
        s=file.read()
    
    return s
    
    u/tool
    def check_location() -> str:
        '''Retrieve the current location of the user. This
 tool must be used only if the 'context' provided by the user is empty'''
        return 'your location is Bengaluru'
  
  
    u/tool
    def send_message(recipient: str, message: str) -> str:
        '''Send a text message to the specified
 recipient with the provided message content. This tool must be used only if the 'context' provided by the user is not e
mpty'''
        return f'Sent message to {recipient}: {message}'
    
    u/tool
    def make_call(recipient: str) -> st
r:
        '''Initiate  a phone call to the specified recipient. This tool must be used only if the 'context' provided b
y the user is not empty'''
        return f'Calling {recipient}...'
    
    @tool
    def receive_call(caller: str) -> 
str:
        '''Handle an incoming phone call from the specified caller. This tool must be used only if the 'context' pr
ovided by the user is not empty'''
        return f'Receiving call from {caller}...'
    
    @tool
    def op1(f:int,s:
int)->dict:
        '''adds f and s'''
        return {'answer':f*s}
    @tool
    def op2(f:int,s:int)->dict:
        '
''subtracts f and s'''
        return {'answer':f*s}
    
    @tool
    def getWeather(city:str):
        '''returns the
 weather in 'city'''
        return 'cloudy'
    
    @tool
    def mute():
        '''Mute an incoming call'''
        
return

I have my reasons for structuring it this way.

Can someone please tell me why I'm getting different outputs in 
version 1 and version 2?
```
---

     
 
all -  [ Same program gives different results when executed directly and when executed as a function ](https://www.reddit.com/r/LangChain/comments/1dci6cs/same_program_gives_different_results_when/) , 2024-06-12-0954
```
Here is a program i've created using Ollama, LangGraph and Llama3:

    from langchain_community.chat_models import Chat
Ollama
    from langchain_core.output_parsers import JsonOutputParser
    from langchain_core.prompts import PromptTempl
ate
    from langchain_community.chat_models import ChatOllama
    from langchain_core.output_parsers import JsonOutputP
arser
    from langchain_core.prompts import PromptTemplate
    from langgraph.graph import END, StateGraph
    from ppr
int import pprint
    from langchain_core.output_parsers import StrOutputParser
    from typing import TypedDict
    imp
ort mod
    from langchain.tools.render import render_text_description
    
    
    
    
    local_llm = 'llama3:8b'
 
   
    
    tools = [mod.check_calendar,mod.check_location,mod.send_message,mod.receive_call,mod.getContactInfo,mod.mut
e]
    rendered_tools = render_text_description(tools)
    print(rendered_tools)
    
    from operator import itemgette
r
    
    
    def tool_chain(model_output):
        tool_map = {tool.name: tool for tool in tools}
        chosen_tool
 = tool_map[model_output['name']]
        return itemgetter('arguments') | chosen_tool
    
    
    contextllm = ChatOl
lama(model=local_llm, format='json', temperature=0)
    
    prompt = PromptTemplate(
        template='''<|begin_of_tex
t|><|start_header_id|>system<|end_header_id|> You are a helpful agent who will answer the user's question to the best of
 your abilities using one or more of the tools available to you\n
        You have access to the following tools. Here i
s the name and description of the tools:%s\n
        Return the name and input of the tool to use.
        Return your r
esponse as a JSON blob with 'name' and 'arguments' keys.
        The value associated with the 'arguments' key should be
 a dictionary of parameters.
        You are not allowed to return blank results
         <|eot_id|><|start_header_id|>u
ser<|end_header_id|>
         {inp}. Who is calling?\n
         <|eot_id|><|start_header_id|>assistant<|end_header_id|>

        '''%rendered_tools,
        input_variables=['inp'],
    )
    
    contextgatherer_chain = prompt | contextllm 
| JsonOutputParser() | tool_chain
    
    
    
    actionllm = ChatOllama(model=local_llm, format='json', temperature=
0)
    prompt = PromptTemplate(
        template='''<|begin_of_text|><|start_header_id|>system<|end_header_id|> You are 
a helpful agent who will select which tool is to be used depending on the context provided by the user and some rules.\n

        You have access to the following tools. Here is the name and description of the tools:%s\n
        Return the n
ame and input of the tool to use.
        Return your response as a JSON blob with 'name' and 'arguments' keys.
        
The value associated with the 'arguments' key should be a dictionary of parameters.
        You are not allowed to retur
n blank results
         <|eot_id|><|start_header_id|>user<|end_header_id|>
         Context:{context}\n
         {inp}.
\n\n
        Rules for tool calling:\n
        If the caller is 'Kau', the tool to be used is 'receive_call'\n
        I
f the caller is 'Priya', the tool to be used is 'send_message'\n
        For all other numbers, the tool to be used is '
mute'\n
         <|eot_id|><|start_header_id|>assistant<|end_header_id|>
        '''%rendered_tools,
        input_varia
bles=['context','inp'],
    )
    
    actiontaker_chain = prompt | actionllm | JsonOutputParser() 
    
    
    class 
GraphState(TypedDict):
        '''
        Represents the state of our graph.
    
        Attributes:
            input
: User input
            generation: LLM generation
            cl: Contact list
            rs: Relationship list
     
       cal: Calendar
            ct: Current time
        '''
        
        input:str
        generation: str
       
 cl:str
        rs:str
        cal:str
        ct:str
        con:str
    
    
    def callhandler(state):
        '''

        Gathers the context and determines whether to receive the call or send a message 
    
        Args:
           
 state (dict): The current graph state
    
        Returns:
            state (dict): Whether to send a message, receiv
e the call, or mute the call
        '''
    
        print('---HANDLING---')
        i = state['input']
        c=state
['con']
    
    
        res1 = contextgatherer_chain.invoke({'inp':i})
        res2 = actiontaker_chain.invoke({'conte
xt':res1,'inp':i})
        return {'generation': res2}
    
    
    
    workflow = StateGraph(GraphState)
    workflow
.add_node('callhandler', callhandler) 
    workflow.set_entry_point('callhandler')
    workflow.add_edge('callhandler',E
ND)
    app = workflow.compile()
    
    
    e='incoming call from +911234567890'inputs = {'input': e}
    for output 
in app.stream(inputs):
        for key, value in output.items():
            pprint(f'Finished running: {key}:')
       
     pprint(value['generation'])

The output for the above is:

---HANDLING---

'Finished running: callhandler:'

{'argu
ments': {'message': '', 'recipient': '+911234567890'},

'name': 'send\_message'}

When i try to run the same program by 
enclosing the entire thing as a function( as i want to import this into another file) like this:

    def PA():
        
from langchain_community.chat_models import ChatOllama
        from langchain_core.output_parsers import JsonOutputParse
r
        from langchain_core.prompts import PromptTemplate
        from langchain_community.chat_models import ChatOlla
ma
        from langchain_core.output_parsers import JsonOutputParser
        from langchain_core.prompts import PromptT
emplate
        from langgraph.graph import END, StateGraph
        from pprint import pprint
        from langchain_cor
e.output_parsers import StrOutputParser
        from typing import TypedDict
        import mod
        from langchain.t
ools.render import render_text_description
    
    
    
    
        local_llm = 'llama3:8b'
    
    
        tools =
 [mod.check_calendar,mod.check_location,mod.send_message,mod.receive_call,mod.getContactInfo,mod.mute]
        rendered_
tools = render_text_description(tools)
        print(rendered_tools)
    
        from operator import itemgetter
    
 
   
        def tool_chain(model_output):
            tool_map = {tool.name: tool for tool in tools}
            chosen_
tool = tool_map[model_output['name']]
            return itemgetter('arguments') | chosen_tool
    
    
        context
llm = ChatOllama(model=local_llm, format='json', temperature=0)
    
        prompt = PromptTemplate(
            templa
te='''<|begin_of_text|><|start_header_id|>system<|end_header_id|> You are a helpful agent who will answer the user's que
stion to the best of your abilities using one or more of the tools available to you\n
            You have access to the
 following tools. Here is the name and description of the tools:%s\n
            Return the name and input of the tool t
o use.
            Return your response as a JSON blob with 'name' and 'arguments' keys.
            The value associate
d with the 'arguments' key should be a dictionary of parameters.
            You are not allowed to return blank results

            <|eot_id|><|start_header_id|>user<|end_header_id|>
            {inp}. Who is calling?\n
            <|eot_i
d|><|start_header_id|>assistant<|end_header_id|>
            '''%rendered_tools,
            input_variables=['inp'],
  
      )
    
        contextgatherer_chain = prompt | contextllm | JsonOutputParser() | tool_chain
    
    
    
      
  actionllm = ChatOllama(model=local_llm, format='json', temperature=0)
        prompt = PromptTemplate(
            tem
plate='''<|begin_of_text|><|start_header_id|>system<|end_header_id|> You are a helpful agent who will select which tool 
is to be used depending on the context provided by the user and some rules.\n
            You have access to the followi
ng tools. Here is the name and description of the tools:%s\n
            Return the name and input of the tool to use.
 
           Return your response as a JSON blob with 'name' and 'arguments' keys.
            The value associated with t
he 'arguments' key should be a dictionary of parameters.
            You are not allowed to return blank results
       
     <|eot_id|><|start_header_id|>user<|end_header_id|>
            Context:{context}\n
            {inp}.\n\n
         
   Rules for tool calling:\n
            If the caller is 'Kau', the tool to be used is 'receive_call'\n
            If 
the caller is 'Priya', the tool to be used is 'send_message'\n
            For all other numbers, the tool to be used is
 'mute'\n
            <|eot_id|><|start_header_id|>assistant<|end_header_id|>
            '''%rendered_tools,
          
  input_variables=['context','inp'],
        )
    
        actiontaker_chain = prompt | actionllm | JsonOutputParser() 

    
    
        class GraphState(TypedDict):
            '''
            Represents the state of our graph.
    
    
        Attributes:
                input: User input
                generation: LLM generation
                cl: Con
tact list
                rs: Relationship list
                cal: Calendar
                ct: Current time
         
   '''
            
            input:str
            generation: str
            cl:str
            rs:str
            
cal:str
            ct:str
            con:str
    
    
        def callhandler(state):
            '''
            Gat
hers the context and determines whether to receive the call or send a message 
    
            Args:
                st
ate (dict): The current graph state
    
            Returns:
                state (dict): Whether to send a message, r
eceive the call, or mute the call
            '''
    
            print('---HANDLING---')
            i = state['input'
]
            c=state['con']
    
    
            res1 = contextgatherer_chain.invoke({'inp':i})
            res2 = act
iontaker_chain.invoke({'context':res1,'inp':i})
            return {'generation': res2}
    
    
    
        workflow 
= StateGraph(GraphState)
        workflow.add_node('callhandler', callhandler) 
        workflow.set_entry_point('callha
ndler')
        workflow.add_edge('callhandler',END)
        app = workflow.compile()
    
    
        file1=open('cont
actlist','r')
        file2=open('relationships','r')
        file3=open('calendar','r')
        s1=file1.read()
       
 s2=file2.read()
        s3=file3.read()
        curt='11:00.'
        e='incoming call from +911234567890'
        f=s1
+'\n\n'+s2+'\n\n'+s3+'\n\n'+curt+'\n\n'+e
        print(f)
        inputs = {'input': e}
        for output in app.strea
m(inputs):
            for key, value in output.items():
                pprint(f'Finished running: {key}:')
           
     pprint(value['generation'])
    
    PA()

The output i get is:

---HANDLING---

'Finished running: callhandler:'


{'arguments': {'caller': '+911234567890'}, 'name': 'receive\_call'}

Here is the 'mod' file in which ive defined the too
ls available to the LLM:

    import os
    from langchain_core.tools import tool
    from typing import Annotated, Sequ
ence, TypedDict
    from langchain.agents import AgentExecutor, create_react_agent
    from langchain_core.messages impo
rt BaseMessage, HumanMessage
    from langchain_openai import ChatOpenAI
    from langchain_core.runnables import Runnab
lePassthrough
    from langchain_core.output_parsers import StrOutputParser
    from langchain_core.prompts import ChatP
romptTemplate, MessagesPlaceholder
    from langchain.output_parsers.openai_functions import JsonOutputFunctionsParser
 
   import functools
    from langgraph.graph import StateGraph, END
    import operator
    import openai
    import tim
e
    import random
    from langchain_community.chat_models import ChatOllama
    from langchain_core.output_parsers im
port JsonOutputParser
    from langchain_core.prompts import PromptTemplate
    from langchain_core.runnables import Run
nable
    from langchain_core.exceptions import OutputParserException
    from langchain.tools.render import render_text
_description_and_args
    from pprint import pprint
    
    
    
    u/tool
    def check_calendar() -> str:
        '
''Retrieve the list of current events from the user's calender. This tool must be used only if the 'context' provided by
 the user is empty'''
        file=open('calendar','r')
        s=file.read()
        return s
    
    @tool
    def ge
tContactInfo()->str:
        '''Retreive the the user's contact list to determine who is calling when given an unknown n
umber'''
        file=open('contactlist','r')
        s=file.read()
        return s
    
    @tool
    def check_locati
on() -> str:
        '''Retrieve the current location of the user. This tool must be used only if the 'context' provided
 by the user is empty'''
        return 'your location is Bengaluru'
    
    @tool
    def send_message(recipient: str,
 message: str) -> str:
        '''Send a text message to the specified recipient with the provided message content. This
 tool must be used only if the 'context' provided by the user is not empty'''
        return f'Sent message to {recipien
t}: {message}'
    
    @tool
    def make_call(recipient: str) -> str:
        '''Initiate  a phone call to the specifi
ed recipient. This tool must be used only if the 'context' provided by the user is not empty'''
        return f'Calling
 {recipient}...'
    
    @tool
    def receive_call(caller: str) -> str:
        '''Handle an incoming phone call from 
the specified caller. This tool must be used only if the 'context' provided by the user is not empty'''
        return f
'Receiving call from {caller}...'
    
    @tool
    def op1(f:int,s:int)->dict:
        '''adds f and s'''
        retu
rn {'answer':f*s}
    @tool
    def op2(f:int,s:int)->dict:
        '''subtracts f and s'''
        return {'answer':f*s
}
    
    @tool
    def getWeather(city:str):
        '''returns the weather in 'city'''
        return 'cloudy'
    
 
   @tool
    def mute():
        '''Mute an incoming call'''
        return

I have my reasons for structuring it this w
ay.

Can someone please tell me why I'm getting different outputs?
```
---

     
 
all -  [ An Ultimate Guide to Run Any LLM Locally
 ](https://www.reddit.com/r/u_thetechrobot_/comments/1dci1h0/an_ultimate_guide_to_run_any_llm_locally/) , 2024-06-12-0954
```
Although ChatGPT, Claude.ai, and Phind are examples of chatbots that might be useful, consumers might not want their pri
vate information to be handled by third parties. Download and execute a large language model (LLM) on your computer to p
revent this. This enables you to test out novel specialized models for language translation and text-to-speech, such as 
SeamlessM4T and Meta’s Code Llama series. With the correct tools and minimum hardware requirements, operating your own L
LM is simple. it has an Intel i9 CPU, 64GB of RAM, and a 12GB Nvidia GeForce GPU on a Dell PC. While it might take some 
effort to find the right model for your work and desktop hardware, ChatGPT and Claude.ai can yield better results. It’s 
important to remember that open-source models will probably continue to advance and that industry observers anticipate a
 closing gap between them and the leaders in the commercial sector.

# Use GPT4All to run a chatbot locally

GPT4All is 
a desktop chatbot that operates locally and does not transfer information elsewhere. It provides options for models that
 operate on your system and is compatible with Windows, macOS, and Ubuntu. The program lets users download around ten mo
dels for non-local use, like Meta AI’s Llama-2–7B conversation and OpenAI’s GPT-3.5 and GPT-4. The chatbot interface is 
simple and intuitive, with options for copying a chat to a clipboard and making a response.

The GPT4All chat interface 
is clear and simple to use. A new beta LocalDocs plugin lets users “chat” with their documents locally. Enabling it in t
he Settings > Plugins tab enables users to build collections based on a certain folder path. The plugin is still under d
evelopment but may improve as open-source models become more powerful. GPT4All also includes interfaces for Python, Node
, a command-line interface (CLI), and a server mode that lets users communicate with the local LLM using an HTTP API sim
ilar to OpenAI’s.

# LLMs in the command line

LLM by Simon Willison provides an easy method to obtain and utilize open-
source LLMs on your system. It needs Python installation but does not require Python code. LLM uses OpenAI models by def
ault, but it can also run with plugins such as gpt4all, llama, the MLC project, and MPT-30B. To submit a query to a loca
l LLM, enter the command llm install model-name. If the GPT4All model does not already exist on your local machine, the 
LLM tool will download it automatically and display a progress bar in the terminal. You may also create aliases for mode
ls in LLM. The LLM plugin for Meta’s Llama models needs more configuration than GPT4All. The software also includes a qu
ery flag and tools for creating text embeddings.

Llama models for your computer

**1. Hugging Face and Transformers**


Hugging Face is the Machine Learning and AI counterpart of Docker Hub, with an astonishing number of open-source models 
available. Fortunately, Hugging Face routinely assesses the models and provides a scoreboard to assist users in selectin
g the finest models available.

Hugging Face also includes transformers, a Python module for operating an LLM locally. T
he following example employs the library to run an older GPT-2 Microsoft/DialoGPT-medium model. The Transformers will up
load the model on the first run, allowing you to interact with it five times. The script also requires PyTorch to be ins
talled.

Transformers provide automatic model downloads and code snippets for testing and learning, but they demand a go
od grasp of machine learning and natural language processing, as well as coding and configuration expertise.

**2. LangC
hain**

Another option for running LLM locally is LangChain. Langchain is a Python framework for developing AI apps. It 
provides frameworks and middleware to let you build an AI app on top of one of its current models. For example, the foll
owing code asks one inquiry about the Microsoft/DialoGPT-medium model. LangChain simplifies model management and provide
s important AI application development facilities, but its speed is restricted and involves coding the programme’s logic
 or building an appropriate UI.

**3. Llama.cpp**

Llama.cpp is a C and C++ inference engine designed for Apple hardware
 that runs Meta’s Llama2 models. It outperforms Python-based solutions, supports big models, and enables cross-language 
bindings for AI applications. It does, however, need tool creation and has limited support for models.

**4. Llama File*
*

Mozilla’s Llamafile is a user-friendly alternative to executing LLMs, noted for its portability and ability to genera
te single-file executables. It improves performance and can incorporate a model in a single executable file. However, th
e project remains in its early stages, and only Llama.cpp-compatible models are supported.

**5. Ollama**

Ollama is a f
ar more user-friendly replacement than Llama.cpp and Llamafile, which require downloading an app. It supports llama and 
vicuña models and is quick. However, it has a restricted model library, is unable to reuse models, lacks LLM configurabl
e features, and is not currently accessible on Windows.

# Conclusion

Your needs and experience will influence the tool
 you choose for local learning management (LLM). There are other choices available, including user-friendly GPT4ALL, tec
hnical Llama.cpp, and Python-based solutions. Open-source approaches are becoming increasingly popular because they prov
ide users greater control over their data and privacy. These models are likely to compete more effectively with ChatGPT 
offerings.
```
---

     
 
all -  [ Can i change the way my output looks in creat sql agent ? ](https://www.reddit.com/r/LangChain/comments/1dchs6s/can_i_change_the_way_my_output_looks_in_creat_sql/) , 2024-06-12-0954
```
I want my output in the below format, but the sql agent throws an error saying that 

ValueError: An output parsing erro
r occurred. In order to pass this error back to the agent and have it try again, pass \`handle\_parsing\_errors=True\` t
o the AgentExecutor. This is the error: Could not parse LLM output: 

\`### Sql Query  
\`\`\`sql  
SELECT   
frcst\_amt
\_in\_gc AS targeted\_budget,  
actl\_cst\_in\_gc AS actual\_budget,  
(actl\_cst\_in\_gc - frcst\_amt\_in\_gc) AS devia
tion  
FROM   
prcur\_frcst\_fact\_TEST  
\`\`\`  
  
### Result  
| targeted\_budget | actual\_budget | deviation      
    |  
|-----------------|----------------|--------------------|  
| 59.82           | 304.41         | 244.58         
    |  
| 178.53          | 2.56           | -175.97            |  
  
  
  
  
### Summarized Insights from query  
The
 query results show the targeted budget, actual budget, and the deviation for each record in the \`prcur\_frcst\_fact\` 
table. The deviations indicate the difference between the actual cost and the forecasted amount. Positive deviations ind
icate that the actual cost exceeded the forecasted amount, while negative deviations indicate that the actual cost was l
ess than the forecasted amount.  
  
### Next Steps  
1. \*\*Analyze Deviations\*\*: Identify the records with the highe
st positive and negative deviations to understand the reasons behind significant budget variances.  
2. \*\*Budget Adjus
tment\*\*: Use the insights from the deviations to adjust future budget forecasts and improve accuracy.  
3. \*\*Cost Co
ntrol\*\*: Implement measures to control costs and reduce deviations, especially for records with high positive deviatio
ns.  
4. \*\*Further Segmentation\*\*: Segment the data by different dimensions (e.g., geography, vendor, material) to g
ain deeper insights into budget performance across different segments.  
5. \*\*Historical Comparison\*\*: Compare the c
urrent period's deviations with historical data to identify trends and patterns in budget performance.\`
```
---

     
 
all -  [ Comparing pdfs through similarity search ](https://www.reddit.com/r/LangChain/comments/1dch46a/comparing_pdfs_through_similarity_search/) , 2024-06-12-0954
```
I have a bunch of pdfs. Pages could go from 1 to 100 in each pdf. I want to do a similarity search on this set of pdfs w
ith some content (query) and order them based on score (ascending order cosine similarity. Most relevant ones at the top
).

Issue is while I can use pypdf loader and embeddings to create docs and store them in a vectorstore, How do I aggreg
ate score for a whole pdf? Lets say page 3 of pdf 25 has relevant content. But how I do I compare the whole pdf to anoth
er pdf and order them based on similarity? Thanks!

Ps: Here I am storing each page as a document. No splitter used. If 
I want to embedd whole pdf it might be too much text. I am kind of stuck here.
```
---

     
 
all -  [ Knowledge search for enterprise - build v.s buy ](https://www.reddit.com/r/vectordatabase/comments/1dcgq4v/knowledge_search_for_enterprise_build_vs_buy/) , 2024-06-12-0954
```
Hi everyone,

I'm currently working on a project that would do some kind of an enterprise search for my company. The req
uirements are pretty basic - having an AI chatbot for the company's employees, that would provide information about comp
any's information.

On the technical side, I'd have to ingest multiple data sources (Slack, Confluence, Notion, Google D
ocs, etc) into a single VectorDB (planned on using ChromaDB) and then do a basic RAG.

I was thinking of building it mys
elf with Langchain/LlamaIndex, but I was wondering what the community thinks about it. These days, there are lots of pro
ducts (Glean, Guru, etc) and open source projects (Quivr, AnythingLLM, etc) that does this.

What do you think are the m
ain considerations for this? I'd like to learn what are the things that I should look out for when deciding whether to b
uild v.s buy a solution.
```
---

     
 
all -  [ Enterprise knowledge search - Build v.s Buy ](https://www.reddit.com/r/LangChain/comments/1dcgokb/enterprise_knowledge_search_build_vs_buy/) , 2024-06-12-0954
```
Hi everyone,

I'm currently working on a project that would do some kind of an enterprise search for my company. The req
uirements are pretty basic - having an AI chatbot for the company's employees, that would provide information about comp
any's information.

On the technical side, I'd have to ingest multiple data sources (Slack, Confluence, Notion, Google D
ocs, etc) into a single VectorDB (planned on using ChromaDB) and then do a basic RAG.

I was thinking of 'building' it m
yself with Langchain, but I was wondering what the community thinks about it. These days, there are lots of products (Gl
ean, Guru, etc) and open source projects (Quivr, AnythingLLM, etc) that does this.

What do you think are the main consi
derations for this? I'd like to learn what are the things that I should look out for when deciding whether to build v.s 
buy a solution.
```
---

     
 
all -  [ Bad request error from openai ](https://www.reddit.com/r/LangChain/comments/1dcg8lz/bad_request_error_from_openai/) , 2024-06-12-0954
```
openai.BadRequestError: Error code: 400 - {'error': {'message': 'An assistant message with 'tool_calls' must be followed
 by tool messages responding to each 'tool_call_id'. The following tool_call_ids did not have response messages: call_wd
vsPX0sM6va49zF12nUIPm6', 'type': 'invalid_request_error', 'param': 'messages.[95].role', 'code': None}}
I am using two t
ools each tool is used for retriever.but I used this in agent .
For tools I used create_retrival_tool
For agents I used 
create_openai_ agent
If any body about how to resolve this error please give me information 
```
---

     
 
all -  [ What is the best LLM to run function calling in Ollama? ](https://www.reddit.com/r/ollama/comments/1dcbivu/what_is_the_best_llm_to_run_function_calling_in/) , 2024-06-12-0954
```
I have Nvidia 3090 (24gb vRAM) on my PC and I want to implement function calling with ollama as building applications wi
th ollama is easier when using Langchain. 

I have tried llama3-8b and phi3-3.8b for using function calling. Their perfo
rmance is not great. Llama3-8b is good but often mixes up with multiple tool calls.

I have also tried nous Hermes’ llam
a3-8b (full model 16gb) however when running it through ollama function calling is not supported. Is there a resource fo
r this someone can help me with? 

Is there a fine tuned LLM model with good instructions on how to implement function c
alling with ollama available. 

Any help will be appreciated and TIA. 
```
---

     
 
all -  [ Do your worst, roast my resume ](https://www.reddit.com/r/resumes/comments/1dc1x9r/do_your_worst_roast_my_resume/) , 2024-06-12-0954
```
looking for a job as an entry level machine learning engineer, did not get any calls so far.

https://preview.redd.it/l9
ul0gbukl5d1.png?width=775&format=png&auto=webp&s=ed55284c9c5a24a0cc8fc2cb9bf96bbdb1608f59
```
---

     
 
all -  [ Partial Markdown and JSON response ](https://www.reddit.com/r/LangChain/comments/1dc1pjv/partial_markdown_and_json_response/) , 2024-06-12-0954
```
Hi,

I am currently exploring Langchain. We want our users to be able to ask questions about upcoming events in our vect
orstore. This works really good. 

By we want the LLM to respond with something that is a mix between regular text/markd
own but with links to the events etc. 

Something like the Arc browser when it searches for you. It automatically adds l
inks to certain topics, places, bars etc.

How could I achieve something like this? All resources all welcome :)
```
---

     
 
all -  [ Customer bot tutorial issue ](https://www.reddit.com/r/LangChain/comments/1dbzvk5/customer_bot_tutorial_issue/) , 2024-06-12-0954
```
https://youtu.be/b3XsvoFWp4c?si=2Y7eBx2_MobnzOno

Has anyone tried the multi agent workflow in the tutorial?
I find that
 if the user query is only a single intent. It could route to the correct place and get the response without problem.

H
owever, if the user query got multiple intent: like booking hotel and booking car at the same time: The agent in the boo
king hotel might think it has tool to book the car as well although it doesn’t, especially when car booking workflow and
 tool have been invoked before this multiple intent query. I’m guessing the problem is likely because all workflow can s
hare state where some part of the state has the history of invoking car booking tool before. So the agent in hotel booki
ng workflow sees it and think it also has this car booking tool.

Sometimes the flow might works when the hotel-booking 
agent answers the hotel booking part then invoke CompleteOrEscalate tool which is to pass the dialog back to the primary
 assistant and reroute the query again to car booking workflow.However, the CompleteOrEscalate tool is not properly invo
ked as the agent prefer invoking the imaginary tool as stated above.


They have added the entry node to help this probl
em but still it doesn’t work well at least for OpenAI GPT4. Is there an upgraded version Chatbot flow to solve this issu
e? 



```
---

     
 
MachineLearning -  [ [P] Superfast RAG: Langchain Streaming and Groq ](https://www.reddit.com/r/MachineLearning/comments/1d5s9g4/p_superfast_rag_langchain_streaming_and_groq/) , 2024-06-12-0954
```
  
Fast LLM RAG inference using Groq and Langchain Streaming.  
  
Groq is introducing a new, simpler processing archite
cture designed specifically for the performance requirements of machine learning applications and other compute-intensiv
e workloads. The simpler hardware also saves developer resources by eliminating the need for profiling, and also makes i
t easier to deploy AI solutions at scale.  
  
Resource: [https://www.youtube.com/watch?v=frMdOL8knqg](https://www.youtu
be.com/watch?v=frMdOL8knqg)
```
---

     
 
MachineLearning -  [ [R] Building an Observable arXiv RAG Chatbot with LangChain, Chainlit, and Literal AI ](https://www.reddit.com/r/MachineLearning/comments/1crwh0q/r_building_an_observable_arxiv_rag_chatbot_with/) , 2024-06-12-0954
```
Hey r/MachineLearning, I published a new article where I built an observable semantic research paper application.

This 
is an extensive tutorial where I go in detail about:

1. Developing a RAG pipeline to process and retrieve the most rele
vant PDF documents from the arXiv API.
2. Developing a Chainlit driven web app with a Copilot for online paper retrieval
.
3. Enhancing the app with LLM observability features from Literal AI.

You can read the article here: [https://medium.
com/towards-data-science/building-an-observable-arxiv-rag-chatbot-with-langchain-chainlit-and-literal-ai-9c345fcd1cd8](h
ttps://medium.com/towards-data-science/building-an-observable-arxiv-rag-chatbot-with-langchain-chainlit-and-literal-ai-9
c345fcd1cd8)

Code for the tutorial: [https://github.com/tahreemrasul/semantic\_research\_engine](https://github.com/tah
reemrasul/semantic_research_engine)


```
---

     
 
deeplearning -  [ How to finetune? ](https://www.reddit.com/r/deeplearning/comments/1daio0h/how_to_finetune/) , 2024-06-12-0954
```
Can someone guide me to some resource how can I finetune an open source llm or some library (like langchain) on unstruct
ured data (example: news articles on cricket) So that model can answer a question (like When did India won world Cup?)
```
---

     
