 
all -  [ I used Langchain to build a Slack Agent - My Experience ](https://www.reddit.com/r/LangChain/comments/1e03z0y/i_used_langchain_to_build_a_slack_agent_my/) , 2024-07-11-0911
```
My AI Agent does the following:

* Instant answers from the web in any Slack channel
* Code interpretation & execution o
n the fly
* Smart web crawling for up-to-date info

project link : [git.new/slack-bot-agent-ollama](http://git.new/slack
-bot-agent-ollama)

**My experience with Langchain**

One of the key advantages of Langchain is its ability to integrate
 different LLMs into your applications. This flexibility allows you to experiment with various models and find the one t
hat best suits your needs.

Langchain's approach is a game-changer. However, I do have one gripe - the documentation cou
ld be better. I wasn't aware that I needed to use the ChatModels instead of the direct models, and this wasn't specified
 clearly enough. This kind of information is crucial for users to get up and running quickly.

https://preview.redd.it/j
jtezql9nqbd1.png?width=1283&format=png&auto=webp&s=5707c453e8a1f1bc0f756b6821780603065dd4fb
```
---

     
 
all -  [ What is your RAG Setup?  ](https://www.reddit.com/r/LocalLLaMA/comments/1e033xj/what_is_your_rag_setup/) , 2024-07-11-0911
```
I'd like to know what comprises your RAG setup. 

Is it as simple as a Langchain Q&A or something more complex with a cu
stom encoder, reranker, searcher and custom chunking and all those?
```
---

     
 
all -  [ Comparing Ollama Mistral and GPT-4o ](https://www.reddit.com/r/agentswithai/comments/1e033kt/comparing_ollama_mistral_and_gpt4o/) , 2024-07-11-0911
```
I built an AI Agent that you can talk to easily on your Slack Channels. It is essentially GPT with access to internet on
 your Slack. I was building this with multiple frameworks that include Langchain, CrewAI, Autogen, Llama Index and i tho
ught why not make this interesting by using Ollama and using Open Source LLMs and comparing them. So i decided to pick 1
0 questions from different fields. Here are the questions:

* History: 'What were the main causes and consequences of th
e French Revolution?'
* Philosophy: 'How does Plato's Allegory of the Cave relate to modern society?'
* Science: 'Can yo
u explain the concept of quantum entanglement in simple terms?'
* Literature: 'What are the central themes in George Orw
ell's '1984'?'
* Art: 'How did the Impressionist movement change the course of Western art?'
* Mathematics: 'What is the
 significance of the Riemann Hypothesis in number theory?'
* Economics: 'How does inflation affect purchasing power and 
economic growth?'
* Psychology: 'What is cognitive dissonance and how does it influence human behavior?'
* Environmental
 Science: 'What are the primary causes and effects of ocean acidification?'
* Technology: 'How might artificial general 
intelligence (AGI) impact the job market?'

# My Experience setting it up with Ollama

I've used HuggingFace for using O
pen Source LLMs all this while. I admit that had it's own hassles but it wasn't very hard to set up as long as you paid 
good attention to the docs. This time i decided to use Ollama. I run a windows machine, so i installed it and struggled 
for a bit in terms of setting it up and using it with Langchain. You have to use ChatOllama and not just Ollama, but it 
was very easy to bind the tools using Composio. I also tried setting it up on Colab but running the server, connecting i
t to the agent with a trigger is difficult.

As for connecting with Slack i used triggers on Composio. You can use it to
 connect agents to Slack and set a trigger everytime the bot is tagged and a message is sent, its also LLM agnostic. I u
sed it for my previous project and it worked very well.

if you want to try the project here's the link: [git.new/slack-
bot-agent-ollama](http://git.new/slack-bot-agent-ollama)

|Metrics|Ollama Mistral|GPT-4o|
|:-|:-|:-|
|Performance on wri
ting|Performs exceptionally well for its size, often outperforming larger models on certain benchmarks. It is very good 
if you want concise and precise answers. This can be beneficial for readers who want a quick overview without diving int
o too much detail.|Provides more detailed and longer responses. It has better writing structure compared to mistral, ans
wers have more depth and includes subtle details. It is better if you want to research deep into a topic.|
|Strengths|Pe
rformed well in the Agentic workflow. The whole process of the agent being triggered when it receives a message and gene
rating a response after internet search was completed quicker.|Performed equally well in the Agentic workflow. Larger qu
eries can be accomodated and understood by the LLM. Hallucinates less in comparison to mistral.|
|Weakness|Larger querie
s cannot be accomodated sometimes and i get a 500 error. Significant effort in setting it up on your system. Windows or 
Linux.|It becomes expensive quickly. It should be explicitly told to provide concise answers if you dont want detailed r
esponses to everything.|
```
---

     
 
all -  [ Comparing GPT-4o with Open Source Models ](https://www.reddit.com/r/OpenAI/comments/1e02ney/comparing_gpt4o_with_open_source_models/) , 2024-07-11-0911
```
I built an AI Agent that you can talk to easily on your Slack Channels. It is essentially GPT with access to internet on
 your Slack. I was building this with multiple frameworks that include Langchain, CrewAI, Autogen, Llama Index and i tho
ught why not make this interesting by using Ollama and using Open Source LLMs and comparing them. So i decided to pick 1
0 questions from different fields. Here are the questions:

* History: 'What were the main causes and consequences of th
e French Revolution?'
* Philosophy: 'How does Plato's Allegory of the Cave relate to modern society?'
* Science: 'Can yo
u explain the concept of quantum entanglement in simple terms?'
* Literature: 'What are the central themes in George Orw
ell's '1984'?'
* Art: 'How did the Impressionist movement change the course of Western art?'

# My Experience setting it
 up with Ollama

I've used HuggingFace for using Open Source LLMs all this while. I admit that had it's own hassles but 
it wasn't very hard to set up as long as you paid good attention to the docs. This time i decided to use Ollama. I run a
 windows machine, so i installed it and struggled for a bit in terms of setting it up and using it with Langchain. You h
ave to use ChatOllama and not just Ollama, but it was very easy to bind the tools using Composio. I also tried setting i
t up on Colab but running the server, connecting it to the agent with a trigger is difficult.

As for connecting with Sl
ack i used triggers on Composio. You can use it to connect agents to Slack and set a trigger everytime the bot is tagged
 and a message is sent, its also LLM agnostic. I used it for my previous project and it worked very well.

if you want t
o try the project here's the link: [git.new/slack-bot-agent-ollama](http://git.new/slack-bot-agent-ollama)

# Comparison
 Table

|Metrics|Ollama Mistral|GPT-4o|
|:-|:-|:-|
||||
|Performance on writing|Performs exceptionally well for its size
, often outperforming larger models on certain benchmarks. It is very good if you want concise and precise answers. This
 can be beneficial for readers who want a quick overview without diving into too much detail.|Provides more detailed and
 longer responses. It has better writing structure compared to mistral, answers have more depth and includes subtle deta
ils. It is better if you want to research deep into a topic.|
|Strengths|Performed well in the Agentic workflow. The who
le process of the agent being triggered when it receives a message and generating a response after internet search was c
ompleted quicker.|Performed equally well in the Agentic workflow. Larger queries can be accomodated and understood by th
e LLM. Hallucinates less in comparison to mistral.|
|Weakness|Larger queries cannot be accomodated sometimes and i get a
 500 error. Significant effort in setting it up on your system. Windows or Linux.|It becomes expensive quickly. It shoul
d be explicitly told to provide concise answers if you dont want detailed responses to everything.|
```
---

     
 
all -  [ RAG to search for an information about an employee within a vast collection of documents ](https://www.reddit.com/r/LangChain/comments/1e02kx2/rag_to_search_for_an_information_about_an/) , 2024-07-11-0911
```
Hello everyone,

I have to build a Retrieval-Augmented Generation (RAG) system using a Large Language Model (LLM) **to s
earch for an information about an employee within a vast collection of documents.** The LLM must return the information 
with references indicating the specific page and document.

if someone already done a project similar or can help me wit
h the steps.

what i decided to do is to select an open source llm (qwen2), then fine tune it, after that build a RAG

*
*what is your opinion gays**  
**i need your help**
```
---

     
 
all -  [ Using Ollama Mistral and GPT-4o for my AI Agent - Comparison  ](https://www.reddit.com/r/LocalLLaMA/comments/1e02jpo/using_ollama_mistral_and_gpt4o_for_my_ai_agent/) , 2024-07-11-0911
```
I built an AI Agent that you can talk to easily on your Slack Channels. It is essentially GPT with access to internet on
 your Slack. I was building this with multiple frameworks that include Langchain, CrewAI, Autogen, Llama Index and i tho
ught why not make this interesting by using Ollama and using Open Source LLMs and comparing them. So i decided to pick 1
0 questions from different fields. Here are the questions:

* History: 'What were the main causes and consequences of th
e French Revolution?'
* Philosophy: 'How does Plato's Allegory of the Cave relate to modern society?'
* Science: 'Can yo
u explain the concept of quantum entanglement in simple terms?'
* Literature: 'What are the central themes in George Orw
ell's '1984'?'
* Art: 'How did the Impressionist movement change the course of Western art?'

# My Experience setting it
 up with Ollama

I've used HuggingFace for using Open Source LLMs all this while. I admit that had it's own hassles but 
it wasn't very hard to set up as long as you paid good attention to the docs. This time i decided to use Ollama. I run a
 windows machine, so i installed it and struggled for a bit in terms of setting it up and using it with Langchain. You h
ave to use ChatOllama and not just Ollama, but it was very easy to bind the tools using Composio. I also tried setting i
t up on Colab but running the server, connecting it to the agent with a trigger is difficult.

As for connecting with Sl
ack i used triggers on Composio. You can use it to connect agents to Slack and set a trigger everytime the bot is tagged
 and a message is sent, its also LLM agnostic. I used it for my previous project and it worked very well.

if you want t
o try the project here's the link: [git.new/slack-bot-agent-ollama](http://git.new/slack-bot-agent-ollama)

# Comparison
 Table

|Metrics|Ollama Mistral|GPT-4o|
|:-|:-|:-|
|Performance on writing|Performs exceptionally well for its size, oft
en outperforming larger models on certain benchmarks. It is very good if you want concise and precise answers. This can 
be beneficial for readers who want a quick overview without diving into too much detail.|Provides more detailed and long
er responses. It has better writing structure compared to mistral, answers have more depth and includes subtle details. 
It is better if you want to research deep into a topic.|
|Strengths|Performed well in the Agentic workflow. The whole pr
ocess of the agent being triggered when it receives a message and generating a response after internet search was comple
ted quicker.|Performed equally well in the Agentic workflow. Larger queries can be accomodated and understood by the LLM
. Hallucinates less in comparison to mistral.|
|Weakness|Larger queries cannot be accomodated sometimes and i get a 500 
error. Significant effort in setting it up on your system. Windows or Linux.|It becomes expensive quickly. It should be 
explicitly told to provide concise answers if you dont want detailed responses to everything.|
```
---

     
 
all -  [  UI for langgraph for agent with user input ](https://www.reddit.com/r/LangChain/comments/1e02blv/ui_for_langgraph_for_agent_with_user_input/) , 2024-07-11-0911
```
What’s the  best tool to make a UI for an agent that interacts with the user as it processes tgrough the graph. 
```
---

     
 
all -  [ Connecting Langchain to Snowflake DB with SSO authentication ](https://www.reddit.com/r/LangChain/comments/1e00w6o/connecting_langchain_to_snowflake_db_with_sso/) , 2024-07-11-0911
```
I want to connect my langchain to Snowflake db. But the snowflake I am using have no password but SSO. What is the synta
x should be used to connect the snowflake to langchain using the following function SQLDatabase.from\_uri?
```
---

     
 
all -  [ Accurate Multimodal Slides Search with Real-Time Updates from SharePoint, Google Drive, and Local Da ](https://www.reddit.com/r/LangChain/comments/1dzzrw5/accurate_multimodal_slides_search_with_realtime/) , 2024-07-11-0911
```
Hi r/langchain, I'm sharing an example on building a multi-modal search application using GPT-4o, featuring extraction o
f metadata and hybrid indexing for accurately retrieving relevant information from presentations.

* Repo: [~https://git
hub.com/pathwaycom/llm-app/tree/main/examples/pipelines/slides\_ai\_search~](https://github.com/pathwaycom/llm-app/tree/
main/examples/pipelines/slides_ai_search)
* Architecture: [~https://github.com/pathwaycom/llm-app/tree/main/examples/pip
elines/slides\_ai\_search#architecture~](https://github.com/pathwaycom/llm-app/tree/main/examples/pipelines/slides_ai_se
arch#architecture)

This project also focuses on automatically updating indexes as changes happen in your repository.   

  
**Quick details:**

* **Ingestion:** The application reads slide files (PPTX and PDF) stored locally or on Google Dr
ive or Microsoft SharePoint.
* **Parsing:** Utilizes the SlideParser from Pathway, configured with a detailed schema. Th
e app parses images, charts, diagrams, and other visual elements as well, and features automatic unstructured metadata e
xtraction. 
* **Indexing:** Parsed slide content is embedded using OpenAI's embedder and stored in Pathway's vector stor
e ([natively available on LangChain](https://python.langchain.com/v0.2/docs/integrations/vectorstores/pathway/)) that is
 optimized for incremental indexing.

**How it helps:**

1. Text in presentations is often limited. This example removes
 the need to manually sift through countless presentations by recalling keywords.
2. Organize your slide library by topi
c or other criteria. Indexes update automatically whenever a slide is added, modified, or removed.

**Preliminary Result
s:**

* This method has proven to be efficient in managing large volumes of slides, ensuring that the most up-to-date an
d accurate information is available. It significantly enhances productivity by streamlining the search process across Po
werPoints, PDFs, and Slides.

Open to your questions and feedback!
```
---

     
 
all -  [ How are you managing long form content? ](https://www.reddit.com/r/LangChain/comments/1dzxzu0/how_are_you_managing_long_form_content/) , 2024-07-11-0911
```
I'm trying to get Claude to generate content that could be up to 8,000 tokens long.

To overcome the max token output li
mitations, I have specifically prompted Claude to stop generating when the max token limit is reached, and then continue
 exactly where you left off when the user responds with a 'continue' message.

  
Example of the prompt:

    const prom
pt = `
    Generate me an adventure story that is between 6000 - 7000 words long
    If you reach the max token output, 
the user will send a message saying 'continue'
    Before continuing, you should check the previous outputs and start ex
actly where you left off so that the output is coherent and consistent. 
    You should not ackowledge the 'continue' me
ssage in the output, just continue generating the content. 
    We will join the outputs together at the end and they sh
ould form a coherent and consistent response. 
    If you have finished generating the content and the user asks you to 
continue, you should just respond with an empty message. 
    
    For example: 
      Assistant: mess 
      User: cont
inue 
      Assistant: age   
    `

The problem is that it won't do as I ask, it just keeps shortening the story, I fin
d this weird because when I change the max tokens to something like, 50 and then change the requested story to have a le
ngth of 200 words, it works fine for multiple continuations.

Anyone faced this before?
```
---

     
 
all -  [ Is there an alternative to data version control (DVC) on Snowflake? ](https://www.reddit.com/r/snowflake/comments/1dzxi34/is_there_an_alternative_to_data_version_control/) , 2024-07-11-0911
```
Hi all! I am an NLP data scientist. I would like to introduce Snowflake to my company due to its recent native support o
f hosted LLMs and Streamlit.

For data preprocessing and LLM prompt development, I am using DVC in combination with MLfl
ow. I am aware that for the latter you have the option to deploy a staged LangChain to Snowflake. That is cool.

However
, for the DVC part, it is not clear to me how I would keep track of my data versioning during model development.

How wo
uld you do that while developing on Snowflake? Would you do data science model development on Snowflake directly at all?

```
---

     
 
all -  [ Langchain One Hour Ultimate Guide ](https://www.reddit.com/r/generative/comments/1dzv1hk/langchain_one_hour_ultimate_guide/) , 2024-07-11-0911
```
The video tutorial covers:

* How to use LLM from HuggingFaceHub without even loading it.
* Prompt Template for Open Sou
rce LLM
* Converting normal text to Langchain schema
* Vector Database and embedding important functions
* Memory
* LCEL


Langchain Zero to LCEL: [https://www.youtube.com/watch?v=TWmV95-dUgQ](https://www.youtube.com/watch?v=TWmV95-dUgQ)
```
---

     
 
all -  [ Langchain Ultimate Guide using Open Source LLMs ](https://www.reddit.com/r/LangChain/comments/1dzuxak/langchain_ultimate_guide_using_open_source_llms/) , 2024-07-11-0911
```
The video tutorial covers:

- How to use LLM from HuggingFaceHub without even loading it.   
- Prompt Template for Open 
Source LLM  
- Converting normal text to Langchain schema  
- Vector Database and embedding important functions  
- Memo
ry  
- LCEL 

Langchain Zero to LCEL: [https://www.youtube.com/watch?v=TWmV95-dUgQ](https://www.youtube.com/watch?v=TWmV
95-dUgQ)
```
---

     
 
all -  [ Can anyone share LLM based projects URL? I wanted to know the pipeline of the project how we are doi ](https://www.reddit.com/r/LangChain/comments/1dzsreq/can_anyone_share_llm_based_projects_url_i_wanted/) , 2024-07-11-0911
```

```
---

     
 
all -  [ Real Time AI Workers using Django x LangChain ](https://www.reddit.com/r/LangChain/comments/1dzs2p4/real_time_ai_workers_using_django_x_langchain/) , 2024-07-11-0911
```
Hi everyone!

I've created a mini series on how to build a real time AI application using Django, LangChain and Celery.


Free knowledge - posting it in here for anyone working on something similar and had the same blockers I had when buildi
ng.

Let me know what you think on how I could potentially improve this architecture.

Part 1

[https://medium.com/towar
dsdev/how-to-set-up-django-from-scratch-with-celery-channels-redis-docker-real-time-django-601dff7ada79](https://medium.
com/towardsdev/how-to-set-up-django-from-scratch-with-celery-channels-redis-docker-real-time-django-601dff7ada79)

Part 
2

[https://medium.com/towardsdev/how-to-set-up-django-from-scratch-with-celery-channels-redis-docker-real-time-django-5
828a1ea43a3](https://medium.com/towardsdev/how-to-set-up-django-from-scratch-with-celery-channels-redis-docker-real-time
-django-5828a1ea43a3)

Part 3

[https://medium.com/towardsdev/how-to-set-up-django-from-scratch-with-celery-channels-red
is-docker-real-time-django-5828a1ea43a3](https://medium.com/towardsdev/how-to-set-up-django-from-scratch-with-celery-cha
nnels-redis-docker-real-time-django-5828a1ea43a3)

Part 4

[https://medium.com/towardsdev/how-to-set-up-django-from-scra
tch-with-celery-channels-redis-docker-real-time-django-8e73c7b6b4c8](https://medium.com/towardsdev/how-to-set-up-django-
from-scratch-with-celery-channels-redis-docker-real-time-django-8e73c7b6b4c8)
```
---

     
 
all -  [ Help Needed: Seeking Advice on Approach and Implementation! (I'm new to this) ](https://www.reddit.com/r/LangChain/comments/1dzrp0a/help_needed_seeking_advice_on_approach_and/) , 2024-07-11-0911
```
Hi, everyone I need help/advice/ideas with approaching a problem. I'm working on a project that generates questions base
d on other questions and documents that have been given. The results should be a mixture of reoccurring questions and ne
wly generated questions from what's uploaded. 



Now I'm still new to building AI products, all I could come up with co
ncerning approaching this problem is to load the document, parse it, chunk it up, and embed the chunks into a vector dat
abase. As for the generation, I'm thinking of using a prompt template and passing the embedding in the prompt.



What d
o y'all think, any suggestions for how I can achieve this? Thanks in advance.
```
---

     
 
all -  [ Serverless Vector/Graph Database for RAG ](https://www.reddit.com/r/LangChain/comments/1dzrcfl/serverless_vectorgraph_database_for_rag/) , 2024-07-11-0911
```
Hello, what are the most used serveless vector/graph databases for LLM RAG usage, with convenient integration in Python 
and AWS (Knowledge base in Bedrock)? Ideally which are PAYG. I wanted to use OpenSearch from AWS, but I don't wanna pay 
700 USD/month though and other solutions don't seem to be serverless at all.
```
---

     
 
all -  [ RAG + Agent  ](https://www.reddit.com/r/LangChain/comments/1dzqcxy/rag_agent/) , 2024-07-11-0911
```
Please can someone provide me a documentation or link or explaination, How to work with RAG with agents  
I have a DB on
 pinecone and i make a tool of it  
then i used a built in tool   
and combine those tools as  
tools = \[tool1,tool2\] 
 
but i am not getting good results and sometimes even it goes in a loop and doesnot generate anything
```
---

     
 
all -  [ Azure Openai GPT 3.5 and 4 not calling multiple tools in parallel  ](https://www.reddit.com/r/LangChain/comments/1dzpiyh/azure_openai_gpt_35_and_4_not_calling_multiple/) , 2024-07-11-0911
```
Hi,i’am facing a bug when trying to call multiple tools at parallel.The model is calling only a single tool every-time. 
See below code.  
The code is given in **langchain documentation** so i tried that but **not getting** the same results 
as in documentation

u/tool  
def add(a: int, b: int) → int:  
“”'Adds a and b.

    Args:
        a: first int
        
b: second int
    '''
    return a + b

u/tool  
def multiply(a: int, b: int) → int:  
“”'Multiplies a and b.

    Args:

        a: first int
        b: second int
    '''
    return a * b

tools = \[add,multiply\]

llm\_with\_tools = llm.b
ind\_tools(tools)  
query = 'What is 3 \* 12? Also, what is 11 + 49?'  
llm\_with\_tools.invoke(query).tool\_calls

Expe
cted Output :\[{'name': 'multiply',  
'args': {'a': 3, 'b': 12},  
'id': 'call\_UL7E2232GfDHIQGOM4gJfEDD'},  
{'name': '
add',  
'args': {'a': 11, 'b': 49},  
'id': 'call\_VKw8t5tpAuzvbHgdAXe9mjUx'}\]

My output:  
\[{'name': 'multiply', 'ar
gs': {'a': 3, 'b': 12}, 'id': 'call\_7lwm1rk1b7IYSzwxeyIvhRI9'}\]
```
---

     
 
all -  [ spacy SpanCat for address parsing
 ](https://www.reddit.com/r/nlp_knowledge_sharing/comments/1dzp68o/spacy_spancat_for_address_parsing/) , 2024-07-11-0911
```
Hey all, I'm working on a project to standardize/normalize address data using spacy-llm spacy.SpanCat.v3. I plan to trai
n the model with examples of correctly labeled addresses to help it automatically correct a dataset filled with inconsis
tently formatted addresses. My main-address column is divided into \['NAME', 'STREET', 'BUILDING', 'LOCALITY', 'SUBAREA'
, 'AREA', 'CITY'\]

There are wrong addresses in format like City, area, name, street, building and other various cases 
which i need to handle as well. My end-goal is that i will give input txt to the model and it will normalize all the add
resses and split them into appropriate labels accordingly as well.

Has anyone here worked on something similar or used 
spacy-LLM for address parsing or something like seperating entities and formatting them? I'd appreciate any insights or 
tips on setting this up effectively. Also, how do i use the langchain/Ollama models. Im not interested in using prodigy 
:3 

Anyyyyyy help would be appreciated!
```
---

     
 
all -  [ Resume critique please ](https://www.reddit.com/r/resumes/comments/1dzp4bc/resume_critique_please/) , 2024-07-11-0911
```
https://preview.redd.it/3ci6doh71nbd1.png?width=590&format=png&auto=webp&s=640a7bf91ece79e1fcd5e32d671a4e61e4c2496a

loo
king for swe intern as a second-year ucsb student! Any help is greatly appreciated!
```
---

     
 
all -  [ Tool Calling / Function Calling not working with Gemini ](https://www.reddit.com/r/LangChain/comments/1dzp16b/tool_calling_function_calling_not_working_with/) , 2024-07-11-0911
```
I am trying to build an app with tool calling , but when ever I change the model to Gemini (gemini-1.5-pro-latest or gem
ini-1.5-flash) . The model just outputs empty response. It does not have any content nor does it have function call. The
 response is just empty. 

I just have one function/tool i.e the taviliy search tool. 

Even when I ask it , latest news
 or some other question . Its just gives empty response. 

    import
     { env } 
    from
     '@/env';
    import
  
   { ChatAnthropic } 
    from
     '@langchain/anthropic';
    import
     { ChatGoogleGenerativeAI } 
    from
     '@
langchain/google-genai';
    import
     { ChatOpenAI, 
    type
     ChatOpenAICallOptions } 
    from
     '@langchain
/openai';
    import
     { z } 
    from
     'zod';
    type Model =
      | ChatOpenAI<ChatOpenAICallOptions>
      |
 ChatAnthropic
      | ChatGoogleGenerativeAI;
    
    export
     const AvailableModels = z.enum(['gpt', 'claude', 'ge
mini']);
    export
     type AvailableModels = z.infer<typeof AvailableModels>;
    export
     function modelPicker(
 
     
    model
    : z.infer<typeof AvailableModels>,
      
    stream
    ?: boolean,
      
    modelName
     = 'gp
t-4o',
    ) {
      let modelObject: Model;
      
    switch
     (
    model
    ) {
        
    case
     'gpt': {

          modelObject = new ChatOpenAI({
            model: 
    modelName
    ,
            apiKey: env.OPENAI_API_KEY,

            streaming: 
    stream
    ,
            modelKwargs: 
    stream
              ? {
                  paral
lel_tool_calls: false,
                }
              : undefined,
          });
    
          
    break
    ;
      
  }
    
        
    case
     'claude': {
          modelObject = new ChatAnthropic({
            model: 'claude-3-son
net-20240229',
            modelName: 'claude-3-sonnet-20240229',
            apiKey: env.ANTHROPIC_API_KEY,
           
 streaming: true,
          });
          
    // modelObject.streaming = true;
          
    break
    ;
        }
   
 
        
    case
     'gemini': {
          modelObject = new ChatGoogleGenerativeAI({
            model: 'gemini-pro
',
            modelName: 'gemini-1.5-flash-latest',
            apiKey: env.GOOGLE_AI_API_KEY,
            
    // stre
aming: stream,
          });
          
    break
    ;
        }
      }
      
    return
     modelObject;
    }

Thi
s is the code for selecting the models. 

  
Is this the problem with langchain or the gemini api
```
---

     
 
all -  [ Facing issues in retrieval ](https://www.reddit.com/r/LangChain/comments/1dzotw6/facing_issues_in_retrieval/) , 2024-07-11-0911
```
Hey everyone,
Need help on this,
During retrieval when I try asking questions, initially I get the correct answers, but 
as the number of documents whose embeddings I am storing ,increases,i start getting incorrect data.

I have tried multip
le chunk sizes with the various embedding models but this issue is persistent.

Any suggestions on it?
PS: my pdf data i
s very much unstructured so I am first extracting data using python libraries and then storing.
```
---

     
 
all -  [ Where do you host your Rag ](https://www.reddit.com/r/LangChain/comments/1dzord2/where_do_you_host_your_rag/) , 2024-07-11-0911
```
I personally host my app in aws using lambda for compute, s3 for storage and rds (postgres) for vector db. There are som
e sqs, dynamo, etc but are for statistic purpose.


Edit: i mean for commercial purpose, not just personal 
```
---

     
 
all -  [ LangChain with streaming in production ](https://www.reddit.com/r/LangChain/comments/1dzoa09/langchain_with_streaming_in_production/) , 2024-07-11-0911
```
Hey  
For context, I am trying to build a RAG application on scale which should support many concurrent user  
I am usin
g ConversationalRetrievalChain and openAI gpt-4-turbo as llm, api is built using Fastapi  
for invoking chain I am using
 ainvoke, and for streaming using AsyncIteratorCallbackHandler

flow is I invoke chain in background using asyncio.creat
e\_task() and streaming from callback\_handler  
Now the issue is, when multiple concurrent user are coming to applicati
on, this callback is blocking main\_thread which causing response to be delayed 

my assumption is - even if callback is
 async, the switching of task in async loop is too much that it is blocking the cpu/thread   
Observation: callback func
tion on\_llm\_token also get's block so it does not pass values to hander

If you have any suggestion on better profilin
g of application, those are also welcome, but as per my analysis this is what blocking application and limiting it to sc
ale
```
---

     
 
all -  [ Langchain Agent Issue in real-time information ](https://www.reddit.com/r/LangChain/comments/1dznzj7/langchain_agent_issue_in_realtime_information/) , 2024-07-11-0911
```
I am using

    search = TavilySearchResults()

as one of the tool to create a tool calling agent.

But since it search 
the web in real-time(if i m not wrong), it is providing me results dating back to 16th Nov '23

https://preview.redd.it/
e4jvvhiunmbd1.png?width=1136&format=png&auto=webp&s=a10e5d4de6852036b5eee0d3ccfbc3f0cce5ee1b

https://preview.redd.it/75
7ggiiunmbd1.png?width=1828&format=png&auto=webp&s=2509d57b7937cb7b3df8434b1a0f1ec4486d2fc4

https://preview.redd.it/3b7e
jliunmbd1.png?width=1834&format=png&auto=webp&s=a8e9958b57266770ea7ee08eb9eff811f73fe8ae

https://preview.redd.it/fqh00j
iunmbd1.png?width=1817&format=png&auto=webp&s=c28148779b6a6efeba3057fae724de906974d691

https://preview.redd.it/9egk1kiu
nmbd1.png?width=1343&format=png&auto=webp&s=abd77cfa5d5599839c68a6f05d632d0046af37aa

Context: I am making a chatbot, th
at i basically a financial advisor, but also has the capability to tell information about stock in real time  
So for fi
nancial advisor part I am using RAG and using a tool as retriever to get advise from my knowledge base  
But while using
 Tavely, it is not providing information in real time
```
---

     
 
all -  [ How to use ConversationSummaryMemory with create_retrieval_chain ? ](https://www.reddit.com/r/LangChain/comments/1dznl59/how_to_use_conversationsummarymemory_with_create/) , 2024-07-11-0911
```
I am developing a PDF RAG app .   
In the previous version of Langchain ( i.e. v0.1 ) , we had RetrievalQA class , but n
ow it is deprecated ( [https://api.python.langchain.com/en/latest/chains/langchain.chains.retrieval\_qa.base.RetrievalQA
.html](https://api.python.langchain.com/en/latest/chains/langchain.chains.retrieval_qa.base.RetrievalQA.html) ).

In thi
s same doc , it is mentioned to use create\_retrieval\_chain . 

But but but , in the RetrievalQA class we had an option
 to pass memory as parameter . How to pass memory ( ConversationSummaryMemory ) in this create\_retrieval\_chain class ?


            rag = RetrievalQA.from_chain_type(
                llm=ChatOpenAI(
                    temperature=0.5,
  
                  model='gpt-3.5-turbo-0125',
                ),
                retriever=compression_retriever,
      
          memory=ConversationSummaryMemory(
                    llm=ChatOpenAI(
                        temperature=0.5,

                        model='gpt-3.5-turbo-0125',
                    )
                ),
                chain_type
_kwargs={'prompt': pt, 'verbose': True},
            )
            response = rag.invoke(question)

 The above code snip
pet is for RetrievalQA class . You can see that I pass ConversationSummaryMemory in the memory parameter .

        syst
em_prompt = (
            'You are an assistant for question-answering tasks. '
            'Use the following pieces of
 retrieved context to answer '
            'the question. If you don't know the answer, say that you '
            'don'
t know. Use three sentences maximum and keep the '
            'answer concise.'
            '\n\n'
            '{contex
t}'
        )
    
        chatPrompt = ChatPromptTemplate.from_messages(
            [
                ('system', syste
m_prompt),
                ('human', '{input}'),
            ]
        )
    
        question_answer_chain = create_stu
ff_documents_chain(llm, chatPrompt)
        compression_retriever = reRanker()
        rag_chain = create_retrieval_chai
n(compression_retriever, question_answer_chain)
        response = rag_chain.invoke({'input':prompt })
    
    

The ab
ove code is for the create\_retrieval\_chain I'm using .


```
---

     
 
all -  [ Better Documentation on State ](https://www.reddit.com/r/LangChain/comments/1dzj6oy/better_documentation_on_state/) , 2024-07-11-0911
```
The docs and vids are too basic. Im trying to understand state management and cant find information on how to modify spe
cific instances of the checkpoints/state.

For example. If the user double texts, Id like to stop execution mid-way and 
delete the last human message and add a new one. The tutorials only show how to modify an existing message but not how t
o delete certain messages. Im using the sqlite class for checkpointer.

```
---

     
 
all -  [ Best PDF Parser for RAG? ](https://www.reddit.com/r/LangChain/comments/1dzj5qx/best_pdf_parser_for_rag/) , 2024-07-11-0911
```
Hey All,

I'm curious what everyone is using to parse complex PDFs, extract the data and turn it into something LLMs can
 better comprehend.

Is there something that can consistently find tables, forms, charts, graphics that we see in many e
nterprise documents. It seems without this step, RAG hallucinations are a significant issue. 

Much appreciated. 
```
---

     
 
all -  [ Local LLM application evals ](https://www.reddit.com/r/LocalLLaMA/comments/1dziypi/local_llm_application_evals/) , 2024-07-11-0911
```
New tool for evaluating RAG pipelines with local models

I've released a RagRelevanceEvaluator that works with open-sour
ce models. Key features:

- Test chunk sizes and top K retrieval settings
- Get relevance scores for retrieved passages

- No external API needed - uses fine tuned local models
- Integrates with LangChain or other orchestrators

Great for op
timizing RAG performance locally. Helps tune parameters and compare configurations objectively.

Runs completely locally
 for quick iteration without API costs or privacy concerns.

GitHub: https://github.com/grounded-ai/grounded_ai
HuggingF
ace: https://huggingface.co/grounded-ai
```
---

     
 
all -  [ Agent Retrieval - How we almost always find the right vectors. Pt 3 ](https://www.reddit.com/r/LangChain/comments/1dzfp48/agent_retrieval_how_we_almost_always_find_the/) , 2024-07-11-0911
```
Hey all - 



Today I wanted to run through how we narrow down our vector space.

**Issues with vector search only:**

*
 If you have used vector search over a large corpus of documents, you'll know vector search doesn't work well.
* Almost 
100% of the time someone is using RAG, they are looking for something specific.
   *  Example: If you use vector search 
on a name, most names will come back, regardless of it's Bob Smith, or Sally Blu. This is bad if I just want to find Sal
ly Blu.



W**hat are we doing?** 

1. We split each doc up into the smallest possible vector (normally sentences) We've
 found this is the best, and most accurate for vector similarity. 
2. NER/Keyword extraction from the query
3.  Search d
ocs for keywords/NER
4. Vector search query within the docs that are returned.
5.  Traditionally top 20 results (no simi
larity score min)
6. Reconstruct the docs into headers etc.
7. Reranker Jina - top 10 results (over .x similarity)
8. Ea
ch result sent to an LLM for quotes
9. combine all into prompt #2
10. LLM answer

Today we'll primarily talk through ste
p 2-7.



**How?**

*Example query:* Does Sally blu work at tada?

1. Use an LLM to extract named entities and key words
/phrases from the query. 
2. Search the entire document to see if 'all' keywords/NER match the doc. \['Tada' and 'Sally 
Blu'\]
3. If there's no matches, do an 'or' search for keywords/NER \['Tada' or 'Sally Blu'\]
4. If there's no matches, 
don't return a doc.
5. If there are matches in either step 2 or 3, return those docs only and do vector search within on
ly those documents. 

This significantly limits the scope of the vector space and based on our experiences almost never 
filters out the documents that are important to answering the question.



**How are we able to search an entire doc?** 


This process wouldn't be possible without out our document structure, so here's a link & a quick overview of how we ho
w we [chunk docs. ](https://www.reddit.com/r/LangChain/comments/1dpbc4g/how_we_chunk_turning_pdfs_into_hierarchical/)

T
LDR: We extract and save the document structure into a hieratical format, headers, sub-headers, list, paragraphs, tables
, etc. Because we do this, we can easily search the entire document. 



**Diagram of our first pass search**

https://p
review.redd.it/jczepvzejkbd1.png?width=365&format=png&auto=webp&s=f7818f84954b2486793cb012f02b7097b988859c

**Example Qu
ery:**

u/warriorA asked this question a couple of days ago in another post. It's simple so we'll re-use it:

\_\_\_\_\_
\_

Consider the query: 'How many Presidents did we have in America?'



Now we might have a document chunk with this in
formation:

1.   doc\_1\_chunk: 'United States has been governed by a total of 46 people'  
2.   doc\_2\_chunk: 'The USA
 is a country in north america.'  
3.   doc\_3\_chunk: 'We've had 1 President in 'Random-Country'.'



Wouldn't your sea
rch fail?



Note - (I made a few small edits for example purposes)

\_\_\_\_\_\_



**Would our system work for this us
e case?** 

Most likely, yes. 



From the query we'd extract: \['Presidents' & 'America'\] 

Again, we search the entir
e document, not just the chunks to find hits.

✅ Doc\_1: It's very likely that doc\_1 would contain both the word presid
ent and America, meaning that document would come back. 

❌ Doc\_2:  Isn't talking about Presidents, thus it wouldn't co
me back.

✅or ❌ Doc\_3: Would most likely not come back as it's not talking about America. (If it did come back because 
America was in the document somewhere, vector search + rerankers would help filter it out.)



**If we extended chunk on
e:** 

here's an example of what it would look like and it contains both the word president & america.

https://preview.
redd.it/zwuhtvrdkkbd1.png?width=1047&format=png&auto=webp&s=9a62623c04a8d1836262d3bd6c0ba3dbe00f91f0



If we didn't do 
this step, it's likely all 3 chunks would come back, and doc\_3\_chunk, would be rated the highest. You could imagine if
 you had hundreds or thousands of documents the most important vectors to answer the question may not show up at all.

h
ttps://preview.redd.it/cr6jmxuwkkbd1.png?width=405&format=png&auto=webp&s=76c747237adb98fb3ba6c78ff491c04ac05bdecc



**
how do we extract NER?** 

We have found the NER models aren't consistent enough, you have to use an LLM. If you ask a q
uestion like 'what are the terms of the wings contract' a NER model may see no named entities, where an LLM would unders
tand the named entity is 'wings'.



**Prompt:**

Respond with valid json. 

You will receive text, your goal is to: 

1
. Identify potential search phrases. Put those in the 'P' field. For example, in 'When was the Huck Finn contract signed
?', the main concept is 'Huck Finn contract' 

2. Identify named entities. Put those in the 'N' field. For example: 'Huc
k Finn' or 'Apple A7' Emit a valid JSON object with a single 'N' field and a single 'P' field. 

	Example 

	Input: When
 was the Huck Finn contract signed? 

	Output: 

	{ 

	'P': \['Huck Finn contract'\], 

	'N': \['Huck Finn'\],

	} 

	In
put: does share and perform offer a performance engagement tool 

	Output: 

	{ 

	'P': \['share and perform performance
 engagement'\], 

	'N': \['share and perform'\],

	} 

	Input: how many processors in the apple a7? 

	{ 

	'P': \['appl
e a7 processors'\], 

	'N': \['Apple', 'Apple A7'\], 

	} 

	Input: How much is the wings contract Output: 

	{ 'P': \['
wings contract'\],

	'N': \['wings'\], 

	} 

	Input: what are the different tiers of wotc? 

	Output: 

	{

	'P': \['wo
tc tiers'\], 

	'N': \['WOTC'\], 

	} 

	Input: what is included in the QuickBooks General Journal report Output: 

	{


	'P': \['QuickBooks General Journal report'\], 

	'N': \['Quickbooks'\], 

	} 

	Example '



Why did we decide on this 
prompt? 

* We use P & N because the less tokens than doing something like named entities & keywords. This mean there's 
less tokens the LLM needs to return. (The average response time is 1.1 seconds.)
* We found you need a large example set
 for the LLM to understand what you're trying to do.
* We recommend tuning these prompts to questions that your customer
 may similarly ask



**Next step:**

After finding the top 20 vectors, we re-construct the document.  Because re-ranker
s tend to work better, and we are giving them additional context, we've found that we almost always return the most rele
vant chunks to answer the question. Here's our[ article](https://www.reddit.com/r/LangChain/comments/1dtr49t/agent_rag_p
arallel_quotes_how_we_built_rag_on/) for going from vectors to search.



Happy to answer any and all questions!
```
---

     
 
all -  [ Using GPT4 to extract web data ](https://www.reddit.com/r/LangChain/comments/1dzblj0/using_gpt4_to_extract_web_data/) , 2024-07-11-0911
```
https://reddit.com/link/1dzblj0/video/1ymwu5okrjbd1/player

Heyo folks, wanting to share a project we've been working on
 with LLM agents. The product itself leverages LLMs to parse and understand web pages to extract structured web data at 
scale. We're doing a larger launch and would love your feedback

Open source projects: [https://github.com/reworkd/](htt
ps://github.com/reworkd/)  
Site: [https://reworkd.ai/](https://reworkd.ai/)  
More info if needed! [https://x.com/asimd
otshrestha/status/1810720478111371581](https://x.com/asimdotshrestha/status/1810720478111371581)
```
---

     
 
all -  [ Need help with Ollama Langchain integration ](https://www.reddit.com/r/LangChain/comments/1dza22u/need_help_with_ollama_langchain_integration/) , 2024-07-11-0911
```
Hey guys, im still new to the LLM world now im working on a project using FastAPI as an intermediate between frontend an
d Ollama local server, im having trouble with integrating it using langchain, I want to tweak some parameters on the Lla
ma model using langchain but cant get it working.

Another issue is RAG, i dont really know how the procedure should go,
 I want some suggestion and help is pretty much appreciated!
```
---

     
 
all -  [ Mistrial deployment  ](https://www.reddit.com/r/LangChain/comments/1dz8y0w/mistrial_deployment/) , 2024-07-11-0911
```
Hey guys.
I'm working on chatbot+ stream lit webapp which is working fine in local but when ever I tried to deploy it on
 stream lit or gradio it's give me lib site error.
If anyone have some good resources please share or alternative. 
```
---

     
 
all -  [ Implementing GraphRAG from MS with Neo4j and Langchain ](https://www.reddit.com/r/Neo4j/comments/1dz7wv0/implementing_graphrag_from_ms_with_neo4j_and/) , 2024-07-11-0911
```
This has been in the making for a couple of weeks. I have implemented the graph ingestion and construction part of the '
From Local to Global GraphRAG paper from Microsoft using Neo4j and LangChain. I went over all the steps and provided my 
detailed thoughts about the paper and underlying code. I think the authors demonstrate an exciting new approach and prov
ide technical considerations along the way.


https://medium.com/neo4j/implementing-from-local-to-global-graphrag-with-n
eo4j-and-langchain-constructing-the-graph-73924cc5bab4?trk=feed-detail_main-feed-card_feed-article-content
```
---

     
 
all -  [ RAG from html files ](https://www.reddit.com/r/LangChain/comments/1dz7deq/rag_from_html_files/) , 2024-07-11-0911
```
Hello!

I'm pretty new to langchain and ML in general, so asking for advice.

I have around 6200 html files from which I
 would like to create an RAG application. I'm also overwhelmed on the different modules and options which are offered th
rough langchain.. So what should I do with the files? :)

Is it a good practice to use html files, or should the data be
 in some other format?

For starters, I would be satisfied if I could find relevant documents from query keywords. I'm o
k using openAI embeddings if that is needed, but when following one tutorial, it ends up crashing due to rate limits..


Any pointers, advice or whatever is appreciated! Thank you! :)
```
---

     
 
all -  [ How to configure headers when using the WebsiteContentSearch tool ? ](https://www.reddit.com/r/crewai/comments/1dz5rm2/how_to_configure_headers_when_using_the/) , 2024-07-11-0911
```
does anyone knows a way to set headers for this tool? the only official argument is 'website: str', but this tool is dif
ficult to be useful without being able to set arguments such as headers (user agent, content type..etc)

I know some peo
ple might suggest that I just write my own tool from scratch and then I can have any configuration option I desire, but 
that beats the purpose of using crewAI (otherwise everybody will be writing their own rig with LangChain directly)

reas
on behind this is that I want to try and 'tweak' my request headers, I keep getting server error 403 no matter what URL 
I am trying to parse using this tool.

any insights will be so much appreciated
```
---

     
 
all -  [ Adding additional Input to SQLDatabaseChain ](https://www.reddit.com/r/LangChain/comments/1dz5bp2/adding_additional_input_to_sqldatabasechain/) , 2024-07-11-0911
```
I want to add an extra input to the SQLDatabaseChain method, it’s currently configured to only accept one I.e. question.
 Plus table_info and dialect it gets from the SQLDatabase connection.
I want to pass a precalculated mappings object to 
the prompt so that it’s used to generate accurate queries. Is there away to achieve this?
```
---

     
 
all -  [ Stream with structured output ](https://www.reddit.com/r/LangChain/comments/1dz4ga0/stream_with_structured_output/) , 2024-07-11-0911
```
Hello, community

Could you please help me to cope with streaming of the structured output in Langchain?  
The example b
elow has a simple idea: to generate JSON of fake biographies in a stream. I have a simple FastAPI part:

    from dotenv
 import load_dotenv
    from fastapi import FastAPI
    
    from typing import AsyncIterable
    from fastapi.responses
 import StreamingResponse
    
    from langchain_openai import ChatOpenAI
    from langchain_core.prompts import ChatPr
omptTemplate
    from langchain_core.pydantic_v1 import BaseModel, Field
    from langchain_core.output_parsers import J
sonOutputParser
    
    
    load_dotenv()
    app = FastAPI()
    
    
    prompt = ChatPromptTemplate.from_messages(
('human', 'Generate biography for {n} persons'))
    model = ChatOpenAI(model='gpt-3.5-turbo-0125')
    
    
    class 
Biography(BaseModel):
        name: str = Field(description='The first name of the person')
        surname: str = Field
(description='The surname of the person')
        birth_place: str = Field(description='The birth place of the person')

        biography: str = Field(description='The biography of the person')
    
    
    class Biographies(BaseModel):
  
      biographies: list[Biography] = Field(description='The list of biographies of the persons')
    
    
    model = m
odel.with_structured_output(Biographies)
    chain = prompt | model | JsonOutputParser()
    
    
    async def send_me
ssage(n_persons: int) -> AsyncIterable[str]:
        async for chunk in chain.astream({'n': n_persons}):
            yie
ld chunk
    
    
    u/app.post('/stream_biographies/')
    async def stream_biographies(persons: int):
        genera
tor = send_message(persons)
        return StreamingResponse(generator, media_type='text/event-stream')
    
    
    if
 __name__ == '__main__':
        import uvicorn
        uvicorn.run(app)from dotenv import load_dotenv
    

And a snipp
et, how I test it:

    import httpx
    
    url = 'http://127.0.0.1:8000/stream_biographies/'
    data = {'persons': 2
}
    
    headers = {'Content-type': 'application/json',
               'accept': 'application/json'}
    
    with htt
px.stream('POST', url, params=data, headers=headers) as r:
        for chunk in r.iter_text():
            print(chunk)i
mport httpx
    
    url = 'http://127.0.0.1:8000/stream_biographies/'
    data = {'persons': 2}
    
    headers = {'Co
ntent-type': 'application/json',
               'accept': 'application/json'}
    
    with httpx.stream('POST', url, pa
rams=data, headers=headers) as r:
        for chunk in r.iter_text():
            print(chunk)

I expect json generation
 on the fly, like in this example [https://baml-examples.vercel.app/examples/get-recipe](https://baml-examples.vercel.ap
p/examples/get-recipe)

However, I get error

    pydantic.v1.error_wrappers.ValidationError: 1 validation error for Gen
erationChunk 
    text
      str type expected (type=type_error.str)

If I remove output parser from the chain, I get `A
ttributeError: 'Biographies' object has no attribute 'encode'`

So I think, the problem is in returning Biographies obje
ct, and not the JSON from the chain, but I don't know, how to fix it. Any help is appreciated
```
---

     
 
all -  [ Mid-Level Full Stack Developer - with no job ](https://www.reddit.com/r/cscareerquestions/comments/1dz1yye/midlevel_full_stack_developer_with_no_job/) , 2024-07-11-0911
```
Hello, Im Mid Level Full Stack Developer, i used to work with mainly JS/TS 

I worked in local companies in Algeria for 
3 years, then i moved to freelance for 2 years, but I'm struggling in freelance because i couldn't find some long-term c
ontract while i'm aiming for stability, but unfortunately i couldn't find that.

During this 2 years i tried to launch f
ew small businesses but i failed for some reasons, and now I'm thinking to move to remote jobs.

I heard that remote job
s for developers are mainly for seniors, even im not senior yet, and this is increased the imposter syndrome feeling ins
ide me.

Here is what I'm good in (my skills) :

- Programming Languages: Javascript/Typescript, few of Python, and lear
ning Golang

- Front End Frameworks: React/NextJS only

- Back End Frameworks: ExpressJS, NestJS 

- Databases: MongoDB 
and PostgreSQL, mainly with ORM like Prisma and TypeORM

- IaaS: Azure and willing to learn AWS

- Others: Docker, Langc
hain, GitHub Actions

- Improvement Area: Testing (willing to learn this month)

- Projects I made:  
   • News AI Scrap
per and Summarizer (Freelance): Service used by Norwegian news company to scrape and summarize and rephrase news from ot
her websites and then publish it in other platforms like their website and social media platforms

   • Worked during a 
month in few tasks (Freelance) in Airtable Extensions Platform and adding some features in the platform and fixing some 
bugs

   • AI Copywriting tool for E-commerce Stores: Built a startup for generating product descriptions, blogs, and SE
O checks using AI (failed due to marketing issues)

   • Uber Like Platform for Trucks (Freelance): Startup built in Isr
ael and discontinued during the lack of investment, my tasks was to build the front-end with React and the back-end with
 NestJS and GraphQL. Migrate the database to MongoDB and PostgreSQL. Implement real-time tracking for deliveries. Collab
orate to deliver the MVP on time and within budget. 

  • Agency job (Full time job) : Worked in 2 agencies to deliver s
ome projects, my tasks was analyze client requirements, created technical designs, and developed web applications using 
React, NextJS, and NodeJS/ExpressJS. Integrated with Headless CMS platforms, collaborated with cross-functional teams to
 deliver projects on time and within budget.  

  
And here is my career, and i want to see if i'm qualified to get remo
te job or not, i hope i can receive any advice to improve my career during this month.

  
Thank you.
```
---

     
 
all -  [ Where to learn AI system design? ](https://www.reddit.com/r/LangChain/comments/1dz1hxg/where_to_learn_ai_system_design/) , 2024-07-11-0911
```
How to deploy for scaling, model parallelism on GPUs, industry best practices.

Anything works, ytb videos, blogs, artic
les,books

I’m all ears. Thanks!
```
---

     
 
all -  [ Guidance requested on Llama2 32k instruct usage and specifications  ](https://www.reddit.com/r/LangChain/comments/1dyz9eh/guidance_requested_on_llama2_32k_instruct_usage/) , 2024-07-11-0911
```
I wanted to use LLama2 instruct 32k for summarisation task. I tried to  load the llm with n_ctx=16384, rope_freq_scale=0
.25 and 0.125. But sometimes I get the output empty and sometimes i don't even get one and the system gets crashed.

I w
orked this out in college t4 GPU session, kaggle's 2x t4 GPU session, and my local session with 32GB RAM and rtx 3050 6g
b vRAM system. 

Any suggestions on how to load the llm and What will be the minimum hardware requirement.
Model used: L
Lama2-instruct-32k-Q4_K_M.gguf by TheBloke
```
---

     
 
all -  [ Folks, how do i make use of the HumanInput tool in a web interface application? ](https://www.reddit.com/r/LangChain/comments/1dyyztx/folks_how_do_i_make_use_of_the_humaninput_tool_in/) , 2024-07-11-0911
```
I have two backend services running, one is the application server and the runs the langchain agent service. I have a re
quirement where i need to ask for input from users from a web interface. The HumanInput tool currently works by getting 
input from the python terminal.  
How do I change it so that I can ask for input from the user in the web interface?

Th
e only approach I could come up with was to use websockets(supabase) and ask for input by sending this message from agen
t server to the frontend and the human input will be passed back to the agent server via the same socket channel.

Are t
here any other better ways to accomplish this?
```
---

     
 
all -  [ Can a langgraph be used as a Langchain Tool? ](https://www.reddit.com/r/LangChain/comments/1dyy33u/can_a_langgraph_be_used_as_a_langchain_tool/) , 2024-07-11-0911
```
Hi. I managed to create an agent using langgraph. Things work well if I run my code sending my user input to this agent.
   
However, what I need now is to have this langgraph based agent being used by another agent (my main agent running th
e system).   
Do anybody has any example on how to do that?  
I tried creating an structured tool that will call the fun
ction run\_graph that will invoke the graph but have had no success.
```
---

     
 
all -  [ Using RunnableBranch to Route Execution to Different Prompts in LangChain.js ](https://www.reddit.com/r/LangChain/comments/1dyxjos/using_runnablebranch_to_route_execution_to/) , 2024-07-11-0911
```
Hey folks 👋! I've wrote a short guide on hot to use R`unnableBranch `for route to different prompts in LangChain.js 

[h
ttps://www.js-craft.io/blog/langchain-runnablebranch-javascript/](https://www.js-craft.io/blog/langchain-runnablebranch-
javascript/)

As a side note keep in mind  but in the future, using a [custom RunnableLambda router function ](https://w
ww.js-craft.io/blog/routing-langchain-js-different-prompts-based-on-query-type/)is the better way to do routing. More de
tails [here](https://www.reddit.com/r/LangChain/comments/1dy26hp/will_runnablebranch_be_removed_from_future/). 

Neverth
eless, I think it's good to know about `RunnableBranch` in case you see it in some codebase. 
```
---

     
 
MachineLearning -  [ [P] Seeking Feedback on My GenAI Job Fit Project - New to LangChain/LangGraph ](https://www.reddit.com/r/MachineLearning/comments/1dgns9p/p_seeking_feedback_on_my_genai_job_fit_project/) , 2024-07-11-0911
```
Hi all,

Soo, i have been working on a a projectcalled [GenAI Job Fit](https://github.com/DAVEinside/GenAI_Job_Fit). It'
s an AI-driven system designed to enhance job applications by providing tailored recommendations based on individual pro
files.

I'm relatively new to LangChain and LangGraph, and I've incorporated them into this project. I would greatly app
reciate it if you could check out the repository and provide any feedback or suggestions for improvement.

Your insights
 on how I can better implement LangChain/LangGraph, or any other aspect of the project, would be incredibly valuable. I'
m eager to learn and make this project as robust as possible.

Thank you in advance for your time and feedback!

Repo Li
nk : [https://github.com/DAVEinside/GenAI\_Job\_Fit](https://github.com/DAVEinside/GenAI_Job_Fit)
```
---

     
 
MachineLearning -  [ [P] I'm tired of LangChain, so I made a simple open-source alternative with support for tool using a ](https://www.reddit.com/r/MachineLearning/comments/1deffo8/p_im_tired_of_langchain_so_i_made_a_simple/) , 2024-07-11-0911
```
[https://github.com/piEsposito/tiny-ai-client](https://github.com/piEsposito/tiny-ai-client)

The motivation for buildin
g tiny-ai-client comes from a frustration with Langchain, that became bloated, hard to use and poorly documented - and t
akes inspiraton from [simpleaichat](https://github.com/minimaxir/simpleaichat/tree/main), but adds support to vision, to
ols and more LLM providers aside from OpenAI (Gemini, Anthropic - with Groq and Mistral on the pipeline.)

I'm building 
this to to continue what simpleaichat started and not to ride on hype, raise money or whatever, but to help people do 2 
things: build AI apps as easily as possible and switching LLMs without needing to use Langchain.

This is a minimally vi
able version of the package, with support to vision, tools and async calls. There are a lot of improvements to be done, 
but even at its current state, tiny-ai-client has generally improved my interactions with LLMs and has been used in prod
uction with success.

Let me know what you think: there are still a few bugs that may need fixing, but all the examples 
work and are easy to be be adapted to your use case.
```
---

     
 
deeplearning -  [ Llama 3 not running on GPU ](https://www.reddit.com/r/deeplearning/comments/1dptxsr/llama_3_not_running_on_gpu/) , 2024-07-11-0911
```
I dont know much theory about RAG but i need to implement it for a project.  
**I want to run llama3 on my GPU to get fa
ster results.**

`from langchain_community.llms import Ollama`  
`llm = Ollama(model='llama3',num_gpu=1)`  
`def generat
e_response(prompt, similar_jobs):`  
`descriptions = '\n\n'.join([job['Description'] for job in similar_jobs])`  
`augme
nted_prompt = f'{prompt}\n\nHere are some job recommendations based on your query:\n{descriptions}'`  
`for chunks in ll
m.stream(augmented_prompt):`  
`print(chunks, end='')`

I am giving llama3 my *'user prompt'* and top 5 nearest *'simila
r\_jobs'* using cosine similarity.  
This code goes not use my GPU but my CPU and RAM usage is high.

**My gpu usage is 
0%** , i have a Nvidia GeForce RTX 3050 Laptop GPU GDDR6 @ 4GB (128 bits)
```
---

     
 
deeplearning -  [ What is ReAct Prompting? the most important piece in agentic frameworks ](https://www.reddit.com/gallery/1djk4nk) , 2024-07-11-0911
```
“What is ReAct Prompting? the most important piece in agentic frameworks” - A quick read from Mastering LLM (Large Langu
age Model) 'Coffee Break Concepts' Vol.6

This document deeps dive into the ReAct Prompting method and why it's importan
t:
1. Limitations of LLM
2. Why ReAct prompting matters?
3. How ReAct Works?
4. LangChain Implementation
5. Why Prompt w
ithin agentic frameworks Matters?

Comment below on which topic you want to understand next in this 'Coffee Break Concep
ts' series and we will include those topics in upcoming weeks.
```
---

     
