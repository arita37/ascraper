 
all -  [ ollama local - smart file manager? ](https://www.reddit.com/r/LocalLLaMA/comments/18f8jwo/ollama_local_smart_file_manager/) , 2023-12-11-0910
```
I have installed ollama and am running llama2 and mistral-openorca with no issues from the command line. I 've seen arti
cles on training and on langchain. The computer is running ubuntu 22.04 new fresh install. hardware is aorus mb with ryz
en threadripper 24 core, 128 GB RAM, nvidia RTX 3060 w 12 GB VRAM, if it matters. 

Can i give local general file access
 to my local ollama AI instance and ask questions like - 'list all folders with pictures taken last year'? 

not sure wh
at i should be searching for as keywords when looking for help from this perspective.
```
---

     
 
all -  [ 📧Letting AI agents control my email inbox... 📮: Gmail Automation ](https://youtu.be/4Ggtba_j1wM) , 2023-12-11-0910
```

```
---

     
 
all -  [ What are LLMs: Large language models explained? ](https://www.reddit.com/r/u_Sandya1209/comments/18ezefx/what_are_llms_large_language_models_explained/) , 2023-12-11-0910
```
[Large Language Models (LLMs)](https://www.optisolbusiness.com/insight/5-key-advantages-of-using-large-language-models-f
or-document-analysis)are AI systems designed to understand and generate human-like text. These models, with millions or 
billions of parameters, can answer questions, write essays, translate languages, and more. They’re created through two m
ain steps: pretraining, where they learn language from vast datasets, and fine-tuning, which tailors them for specific t
asks. LLMs are versatile and adaptable, making them valuable in numerous applications. However, their deployment raises 
concerns about bias, ethics, and misuse. Despite challenges, LLMs offer exciting opportunities for automating language-r
elated tasks and revolutionizing human-computer interaction. In this article, we will explore the key advantages of usin
g LLM for document analysis.

[**Large Language Models for Automated Document Analysis**](https://www.optisolbusiness.co
m/insight/5-key-advantages-of-using-large-language-models-for-document-analysis)

**Efficient Information Extraction**


* Large Language Models are exceptionally efficient at extracting pertinent information from a wide range of documents. 
Whether the content is unstructured text, images with text, or a mix of both, LLMs excel at quickly and accurately ident
ifying and isolating the relevant data.
* This is invaluable for tasks like data categorization, where LLMs can rapidly 
sift through large volumes of unstructured text or documents with embedded images to extract critical details.

**Multil
ingual Support**

* Many Large Language Models are designed to be multilingual, enabling them to[ ](https://www.optisolb
usiness.com/insight/harnessing-the-power-of-langchain-and-openai-gpt-3)analyze documents in multiple languages seamlessl
y. This eliminates the need for organizations to maintain separate models for each language, streamlining document analy
sis efforts, and making them particularly advantageous for global businesses and organizations that operate in diverse l
inguistic environments.

**Contextual Understanding**

* LLMs possess an innate ability to grasp the context within docu
ments. They go beyond simply identifying keywords and can discern nuances, relationships between words, and the overall 
meaning of sentences.
* This contextual understanding enhances their performance in more advanced document analysis task
s, such as sentiment analysis, where capturing the sentiment's context is crucial for accurate results.

**Consistency a
nd Scalability**

* Large Language Models ensure consistent document Document Analysis analysis results, reducing the po
tential for human errors and biases. Additionally, they are highly scalable, capable of handling large volumes of docume
nts efficiently. This scalability is especially valuable for enterprises that deal with a massive inflow of documents da
ily.

**Insights and Trends**

* LLMs have the capacity to uncover valuable insights and trends within documents. This c
apability is instrumental in guiding[ ](https://datalabs.optisolbusiness.com/portfolio/building-data-warehouse-and-drive
-actionable-insights)data-driven decision-making, refining marketing strategies, and extracting business intelligence fr
om the wealth of information contained in documents.

&#x200B;

https://preview.redd.it/7304sn6jlf5c1.png?width=300&form
at=png&auto=webp&s=aba8bfa9fc3e2ceb80f91ae716b92d4977ffb9e6
```
---

     
 
all -  [ Qdrant issue: Cannot assign requested address ](https://www.reddit.com/r/LangChain/comments/18eyhkj/qdrant_issue_cannot_assign_requested_address/) , 2023-12-11-0910
```
I'm trying to connect to a local instance of Qdrant which is running in Docker:

    import qdrant_client
    client = q
drant_client.QdrantClient(url='localhost', port=6333)
    client.get_collections()

&#x200B;

However, I get the followi
ng error:

`qdrant_client.http.exceptions.ResponseHandlingException: [Errno 99] Cannot assign requested address`

&#x200
B;

The instance seems to be running fine since if I go to `localhost:6333/dashboard` I can see the dashboard.
```
---

     
 
all -  [ SuperDuperDB - how to use it to talk to your documents locally using llama 7B or Mistral 7B? ](https://www.reddit.com/r/LocalLLaMA/comments/18eusc8/superduperdb_how_to_use_it_to_talk_to_your/) , 2023-12-11-0910
```
https://github.com/SuperDuperDB/superduperdb

This has only been released recently and already trending in github under 
LLM/AI category.

Would like to ask if anyone tried to use it to perform inferencing on your documents? Say 10 pages of 
text. How did it go? I'm planning to use LLAMA 2 7B or mistral 7B for it.

Thanks to u/opi098514 & u/TheWebbster and to 
all others who replied back, seems this tool is not really available at the moment. The tool is basic, upload my documen
t (text file), then create inference on it like an LLM.

Here are a few things that seem might work but with caveats.

1
) https://python.langchain.com/docs/use_cases/question_answering/ --> Feel free to check, though I am not sure if it wil
l consume $ from your OpenAI API tokens

2) ChatGPT Pro (though it can only ingest around 2-3 pages? then it will halluc
inate right after. It's not scalable).

3) ChatGPT Plugin - Same with #2, it will hallucinate after 2-3 pages. It's not 
scalable.

4) https://github.com/oobabooga/text-generation-webui/wiki -- oobabooga, this seems promising. Haven't tried 
it yet.

5) Langdroid - https://github.com/langroid/langroid/blob/main/README.md --> could this be it?




***Update:***
 This RAG Tool seems to have been requested countless times and there's a real business use case for this. Others are wi
lling to pay top dollar for, but let's not go there, let's built it with all the open source materials we have in our ow
n local hardware. Here's a past convo about it: https://www.reddit.com/r/LocalLLaMA/comments/16cbimi/yet_another_rag_sys
tem_implementation_details_and/
```
---

     
 
all -  [ I just had the displeasure of implementing Langchain in our org. ](https://www.reddit.com/r/LangChain/comments/18eukhc/i_just_had_the_displeasure_of_implementing/) , 2023-12-11-0910
```
Not posting this from my main for obvious reasons (work related).

Engineer with over a decade of experience here. You n
ame it, I've worked on it. I've navigated and maintained the nastiest legacy code bases. I thought I've seen the worst.


Until I started working with Langchain.

Holy shit with all due respect LangChain is arguably the worst library that I'
ve ever worked in my life.

Inconsistent abstractions, inconsistent naming schemas, inconsistent behaviour, confusing er
ror management, confusing chain life-cycle, confusing callback handling, unneccessary abstractions to name a few things.


The fundemental problem with LangChain is you try to do it all. You try to welcome beginner developers so that they do
n't have to write a single line of code but as a result you alienate the rest of us that actually know how to code.

Let
 me not get started with the whole 'LCEL' thing lol.

Seriously, take this as a warning. Please do not use LangChain and
 preserve your sanity. 
```
---

     
 
all -  [ What is needed in a comprehensive outline on Natural Language Processing? ](https://www.reddit.com/r/datascience/comments/18ejp1i/what_is_needed_in_a_comprehensive_outline_on/) , 2023-12-11-0910
```
I am thinking of putting together an outline that represents a good way to go from beginner to expert in NLP. Feel like 
I have most of it done but there is always room for improvement. 

Without writing a book, I want the guide to take some
one who has basic programming skills, and get them to the point where they are utilizing open-source, large language mod
els ('AI') in production. 

What else should I add to this outline?

&#x200B;

https://preview.redd.it/vyfy743jab5c1.png
?width=655&format=png&auto=webp&s=38576b1c4c349587e776061adebc576132914971

https://preview.redd.it/gaaeouimab5c1.png?wi
dth=633&format=png&auto=webp&s=d528cde4c444c8ed88d5fcd902830fb0a2629604
```
---

     
 
all -  [ Guys- anyone use Pinecone.from_documents, RecursiveCharacterTextSplitter.split_documents, etc. and a ](https://www.reddit.com/r/LangChain/comments/18ehcm7/guys_anyone_use_pineconefrom_documents/) , 2023-12-11-0910
```
I see Pinecone.from\_documents in the Langchain documents but I can't seem to find the relevant python file to understan
d the method.

Curious because when I collect all the chunked docs from RecursiveCharacterTextSplitter.split\_documents 
and OpenAIEmbeddings.embed\_documents I am getting 610 texts/vectors but after building the Pinecone Index for a specifi
c namespace (a subsection of the Index) and checking the properties of the namespace I see 1251 vectors there.

How else
 are people breaking down PDFs if not using from\_documents? I would like to see the actual method being run.
```
---

     
 
all -  [ Unit tests feedback loop ](https://www.reddit.com/r/LocalLLaMA/comments/18ede3y/unit_tests_feedback_loop/) , 2023-12-11-0910
```
Have you setup a feedback loop system with your local llama?
 like give prompt for creating code for a task, then automa
tically unit test the result from the model. If it is failed give the error back to the model ask to correct it.
And rep
eat the process until unit test successfull.
With  langchain etc..?
```
---

     
 
all -  [ Passing LangChain Objects from Server to Client Issues (Serialization) ](https://www.reddit.com/r/LangChain/comments/18e9f1u/passing_langchain_objects_from_server_to_client/) , 2023-12-11-0910
```
It seems like LangChain (python) in web applications comes with a lot of headaches due to serialization issues.

I keep 
trying to return things from the server side code to the client only to find that I'm unable to as they are non serializ
able.

For example:

Documents, AIMessages, etc

This means I manually have to go through and recreate/clean all these o
bjects when I want to pass them to the client.

Does anyone have a good solution around this?
```
---

     
 
all -  [ OpenAI assistant pricing vs API pricing ](https://www.reddit.com/r/LangChain/comments/18e25qx/openai_assistant_pricing_vs_api_pricing/) , 2023-12-11-0910
```
Today I was playing on openAI Assistant to get answers from a simple CSV file. After trying for 3 prompts, after which I
 did not really get any answers, the cost was 2$!!! which I think is high, compared to <1$ that used to cost when I was 
playing with API few months ago.

I am working on a recommendation app, where I will provide openAI api some of the data
 from my sql db and return openai suggestions to the end user. Now seeing the assistant price I feel like reverting back
 to using API as the assistants cost seem a bit steeper. Am I missing something, what are your thoughts?
```
---

     
 
all -  [ Are there any custom GPTs / Copilot bots trained on the latest LangChain docs? ](https://www.reddit.com/r/LangChain/comments/18dxn4b/are_there_any_custom_gpts_copilot_bots_trained_on/) , 2023-12-11-0910
```
Can’t ask vanilla GPT 4 since it’s past the training cutoff, and can’t make one myself cause, well, I can’t understand t
he docs
```
---

     
 
all -  [ memory in ConversationalRetrievalChain removed ](https://www.reddit.com/r/LangChain/comments/18dxc2o/memory_in_conversationalretrievalchain_removed/) , 2023-12-11-0910
```
Did something change in the most recent version of Langchain, i could have sworn that the ConversationalRetrievalChain t
ook a memory parameter and now its gone?

The docs have it [https://api.python.langchain.com/en/latest/chains/langchain.
chains.conversational\_retrieval.base.ConversationalRetrievalChain.html#langchain.chains.conversational\_retrieval.base.
ConversationalRetrievalChain.memory](https://api.python.langchain.com/en/latest/chains/langchain.chains.conversational_r
etrieval.base.ConversationalRetrievalChain.html#langchain.chains.conversational_retrieval.base.ConversationalRetrievalCh
ain.memory)  But the code errors out with a “bad key” error and there is no mention of memory in the source anymore.

`p
ydantic.v1.error_wrappers.ValidationError: 1 validation error for ConversationalRetrievalChain`

`memory  value is not a
 valid dict (type=type_error.dict)`

what is the current idiomatic way to do RetreivalQA RAG over private documents with
 history/memory now ?
```
---

     
 
all -  [ langchain agent does not return JSON files generated from tools ](https://www.reddit.com/r/LangChain/comments/18dv7wx/langchain_agent_does_not_return_json_files/) , 2023-12-11-0910
```
hi guys,

I have two RAG chains for 2 different types of answers. One of the chains is instructed to generate json and i
t works well by iteself.

    json_instruct='''
    [INST] <<SYS>>
    You are a helpful and concise assistent, that onl
y comunicates using JSON files.
    The expected output from you has to be: 
        {
            'cookware_name': {coo
kware},
            'description': [],
            'ai_notes': {explanation}
        }
    The INST block will always be
 a json string:
        {
            'prompt': {the user prompt}
        }
    The available cookwares are in the conte
xt given to you
    
    <</SYS>> [/INST]
    
    '''
    
    
    JSON_pipeline = RetrievalQA.from_chain_type(
      
  llm=CustomLLM(system_instruction=json_instruct), chain_type='stuff',
        retriever=cookware_retriever
    )
    
 
   JSON_pipeline('what do i need for crepes')

But when i put these 2 chains into a langchain agent, the agent would acc
urately send a prompt to the json chain but return answers in regular sentences. The agent is defined as :

&#x200B;

  
  tools = [
    
    # tool 1
        Tool(...),
    
    # tool 2
        Tool(
            name = 'JSON data',
       
     func=JSON_pipeline.run,
            description = '''
            Useful for you need to answer questions about wha
t a certain cookware is or 
        what cookware is needed for certain dishes. 
            ''',return_direct=True
    
         )
              ]
    
    llm_chain = LLMChain(llm=CustomLLM(system_instruction='You are a helpful and fast as
sistant.'), prompt=prompt)
    
    
    tool_names = [tool.name for tool in tools]
    
    agent = LLMSingleActionAgen
t(
        llm_chain=llm_chain,
        output_parser=output_parser,
        stop=['\nObservation:'],
        allowed_to
ols=tool_names
    )
    
    agent_executor = AgentExecutor.from_agent_and_tools(agent=agent, tools=tools, verbose=True
)
    
    agent_executor.run('list useful cookwares for soup')

&#x200B;

The answer is indeed a list useful cookwares 
based on the documents. But it's no longer in a JSON format that was generated by the JSON\_pipeline

Is there any way I
 can make the agent keep the answers as provided by the tools without modifying the answers by the central 'router' LLM?
 (Or am I missing out some parameters?)

&#x200B;

&#x200B;

&#x200B;

&#x200B;

&#x200B;
```
---

     
 
all -  [ The Elasticsearch developer survey is here! If you build an app with search and/or gen AI, consider  ](https://www.reddit.com/r/LangChain/comments/18dsx62/the_elasticsearch_developer_survey_is_here_if_you/) , 2023-12-11-0910
```
Survey here → [https://survey.alchemer.com/s3/7626156/ES2412p](https://survey.alchemer.com/s3/7626156/ES2412p)
```
---

     
 
all -  [ Pushing the Limits of RAG: Seeking Insights on Embedding Models for Next-Level AI Performance ](https://www.reddit.com/r/datascience/comments/18dpiq2/pushing_the_limits_of_rag_seeking_insights_on/) , 2023-12-11-0910
```
 I've been digging into the data science world for a good while now, constantly looking for new ways to make AI and big 
data play nice together. When I'm not on the grind, I love to tinker with fresh AI tools and frameworks to keep up with 
the fast-moving tech scene.

Lately, I've noticed a surge in discussions around Retrieval-Augmented Generation (RAG) acr
oss various platforms like Twitter, tech blogs, and YouTube tutorials. The process seems straightforward - using Langcha
in or Llamaidnex,  take some text, chunk it, insert it into a vector database, integrate your preferred LLM, and bam, yo
u've got yourself an RAG System.

But here's the catch: those popular frameworks oversimplify things, leading many to un
derestimate the importance of the underlying details. This misconception becomes a roadblock when unexpected challenges 
arise in projects due to the nuances of implementation.

Currently, I'm deeply involved in a project that's testing the 
boundaries of RAG's capabilities, particularly in enhancing efficiency and accuracy for extensive searches. However, I'v
e encountered a few hurdles where community wisdom would be invaluable. I recently came across a blog from Llamaindex di
scussing various embedding models, and I'm curious about your experiences:

* What are the primary challenges you face w
ith the current implementation of RAG?
* Have any of you experimented with those embedding models, such as [Open AI's ad
a](https://platform.openai.com/docs/guides/embeddings/what-are-embeddings), [Jina Embeddings](https://go.jina.ai/reEmbed
dingsBaseEN), and other embedding models in the [MTEB leaderboard](https://huggingface.co/spaces/mteb/leaderboard) …
* H
ow do you anticipate the Embedding model could assist in your RAG implementation?
* Are there specific metrics or result
s you hope to achieve with an improved Embedding model? My aim is to enhance accuracy and expedite processing.

I'm eage
r to hear your insights, experiences, and advice. Let's collaborate to push the boundaries of what's possible in AI and 
data science!
```
---

     
 
all -  [ 70B Model in Langchain with llama.cpp ](https://www.reddit.com/r/LocalLLaMA/comments/18dodgv/70b_model_in_langchain_with_llamacpp/) , 2023-12-11-0910
```
Hello everyone,

I just started out with local LLMs, and I guess I am missing some elemental component.

I want to run a
 70B model from Huggingface: https://huggingface.co/LeoLM/leo-hessianai-70b-chat

I know I need to quantize it, to make 
it work. Even though I have 95GB of VRAM and about 160GB of RAM available. But I need fast inference.

So I opted to qua
ntize it to 6 bits using llama.cpp.

However, when i download the model I get 15 hugest files (.bin) and a tokenizer.jso
n, alongside some other stuff.

What would be the line to get this thing quantized? I used: python convert.py models/Leo
M to no avail.

I guess without any flags the standard quantization is also below my needs.

So if that worked and I got
 a gguf file, how would I get the gguf to run in langchain without additional bloatware?

Is there a tutorial that I am 
missing?

Thank you
```
---

     
 
all -  [ Attaching files to user prompt when using LangChain OpenAI Assistant API ](https://www.reddit.com/r/LangChain/comments/18dloff/attaching_files_to_user_prompt_when_using/) , 2023-12-11-0910
```
I am using LangChain with Python, specifically this part of the API for Open AI Assistants - [https://python.langchain.c
om/docs/modules/agents/agent\_types/openai\_assistants](https://python.langchain.com/docs/modules/agents/agent_types/ope
nai_assistants) 

 How do I attach files to user prompts? 

Looking at the following code - 

    from langchain.agents 
import AgentExecutor
    
    agent_executor = AgentExecutor(agent=agent, tools=tools)
    agent_executor.invoke({'conte
nt': 'What's the weather in SF today divided by 2.7'})

The content property of the object that is being passed into the
 invoke function has the user prompt - what we are sending to the assistant. But in addition to text prompts, it is also
 possible to send files to the assistant in a user prompt. In the OpenAI Assistants Web UI, there is an attach file butt
on. With the official OpenAI Assistants API, I am able to upload the file to OpenAI's file system and then attach the fi
le via the file ID that is generated.

How can I attach files to a user prompt with the LangChain OpenAI Assistant API? 
The documentation doesn't seem to mention how I can do this from what I've read.

Thank you.
```
---

     
 
all -  [ Structure of embeddings for complex objects / how to interact with structure in langchain ](https://www.reddit.com/r/LangChain/comments/18djyo6/structure_of_embeddings_for_complex_objects_how/) , 2023-12-11-0910
```
Hi there, I am looking to implement a RAGish use case with python and langchain. Want to share my high level plan here a
nd ask for your feedback. 

Process roughly is as follows

* Access a catalog of large, complex and semi-structured obje
cts. Each object consists of some string attributes and contains multi-level list objects. The 'payload' often is format
ted as JSON (not sure yet whether I should extract more attributes or just hope that the LLM can allow queries also on t
he insides of that JSON). I created a python class that represents that structure
* Next step is to create embeddings (u
sing langchain & Chroma for now). Here I am unsure how to proceed. At least I want to have a dedicated embedding of each
 of my catalog items. Use case will be, that users present their use case (like 'where do i find information on attribut
e XYZ?'). I want the LLM to return the suitable catalog item. But almost more important, I want the LLM to look inside t
he catalog item, look at all attributes and evaluate whether a certain attribute suits (rather than the whole catalog it
em). 
   * Q: Should I embed each catalog item as one entry or rather create embeddings on artifact level? If so, how do
 I maintain reference to the catalog item? I could duplicate relevant catalog item information of course for each attrib
ute. 
   * Q: Already thinking of retrieval (plan to use in retrieval chains). I do foresee that user queries may not be
 straight forward enough. I may need an agent that guides the user through her query (like U: 'where do i find informati
on on attribute XYZ?' -> S: 'Help me to understand more about your use case: Which parts of the catalog are you interest
ed in? Rather A or B or C?' -> ...). For that I need to make the LLM aware of both, the catalog structure and the inside
s of a catalog item. Can I do that with just 'flat' embeddings? 
* Once the embeddings are done, I want to use them as {
context} with langchain. I first want to try how far I can get with chains. 
   * Q: Any experience / examples on how to
 define prompts in a way that I can use information from context? Can I explicitly reference metadata information someho
w? Like 'system message: You´re an expert on the catalog from {context} and want to recommend discrete items. You should
 always use the {name} and {summary} in your recommendations'. Additionally, if i index each catalog item separately, I 
need to look into the items´ structure, like 'system message: In your recommendations please always list the output para
meters of the method of a catalog item that made you pick this recommendation'. Is that likely to work? 
* Some high lev
el assessment of how far I can get with chains or whether I should use agents for my case would be very helpful as well.
 

Thanks already for the discussion!

&#x200B;
```
---

     
 
all -  [ Random search on vectorstore ](https://www.reddit.com/r/LangChain/comments/18dj6ep/random_search_on_vectorstore/) , 2023-12-11-0910
```
I need to randomly select some documents from a langchain vectorstore. Is there any process for that. 
One solution is t
o generate a random embedding vector and then do similarity search with that vector.
But is there any efficient method f
or randomly selecting some document.
Selecting documents with random index will also work.
```
---

     
 
all -  [ [D] github repositories for ai web search agents ](https://www.reddit.com/r/MachineLearning/comments/18dhtm4/d_github_repositories_for_ai_web_search_agents/) , 2023-12-11-0910
```
Do you know of any github repositories that either help with building a web search ai agent or that has a good one?

git
hub repositories that I saw so far but have not yet tried :

- langchain (the WebResearchRetriever and weblangchain for 
example (have not tried either) )
- autogpt
- gpt-researcher

[Edit: changed researchgpt to gpt-researcher]
```
---

     
 
all -  [ CRUD operations in Vector Databases(For production purpose) ](https://www.reddit.com/r/LocalLLaMA/comments/18dh3zi/crud_operations_in_vector_databasesfor_production/) , 2023-12-11-0910
```
Hello everyone, I have been working with langchain and has built some  RAG applications. I have used FAISS as the vector
 database, which  inherently does not support CRUD operations completely. If anyone has  any inputs on which of the vect
or databases support CRUD operations,  which they might have tried and tested. And also it should be efficient  and not 
accurate, not too much time consuming. Thanks.
```
---

     
 
all -  [ CRUD operations on Vector Databases ](https://www.reddit.com/r/LangChain/comments/18dgp16/crud_operations_on_vector_databases/) , 2023-12-11-0910
```
Hello everyone, I have been working with langchain and has built some RAG applications. I have used FAISS as the vector 
database, which inherently does not support CRUD operations completely. If anyone has any inputs on which of the vector 
databases support CRUD operations, which they might have tried and tested. And also it should be efficient and not accur
ate, not too much time consuming. Thanks.
```
---

     
 
all -  [ Need help with streaming for Custom LLM Nodejs ](https://www.reddit.com/r/LangChain/comments/18dgatn/need_help_with_streaming_for_custom_llm_nodejs/) , 2023-12-11-0910
```
Hi,

I am trying to achieve streaming for a custom LLM hosted on a server. I am using nodejs for the same. If anyone has
 worked on something similar, could you please guide me? 

I am completely clueless on this. 

Thanks!
```
---

     
 
all -  [ Any managed vector embedding services? ](https://www.reddit.com/r/LangChain/comments/18de6xv/any_managed_vector_embedding_services/) , 2023-12-11-0910
```
I’m currently self hosting thenlper/gte-small in a 6USD DO droplet, 1GB Ram, 1vCPU. Not too happy with the throughput. A
PI cold start can go up to 5-8 seconds, and averaging around 2-3 seconds. 

I am planning to switch over to baai/bge-sma
ll-en-v1.5 for newer projects because of Cloudflare Workers AI but they have no pricing model and not recommended for pr
oduction yet. In the meantime, anyone has any ideas on how to mangle through this?

No OpenAI embeddings, thank you! I p
refer something that can be self hosted and managed so I can scale up / down in costs
```
---

     
 
all -  [ local/private llm based chatbot using free/open source tools. ](https://www.reddit.com/r/LangChain/comments/18dcnkc/localprivate_llm_based_chatbot_using_freeopen/) , 2023-12-11-0910
```
 

I intend to create a local llm based chatbot for my team. Basically it should be able to read the docs and generate i
ntelligent responses. I'm pretty new to LLMs and have tried few things here and there. Overall I intend to present a pro
totype on a non-GPU or useless GPU based machine first. From what I understand so far I need to create a RAG pipeline. I
've seen few architectures using embeddings, vector databases, langchain and a model to do create such a pipeline. I'm s
till pretty new to all these jargons. I have tried few opensource models as well locally and most of them just crash my 
M1 laptop. I have better work laptop with 16 GP RAM and 8GB graphics card memory on an A2000 card. Can you please sugges
t how can I quickly come up with a prototype. Basically the RAG pipeline(or any other method) should be able to quickly 
switch between different LLM models, or databases or any other components when it comes to deploying on a production set
up. Also, for now, the idea is to use the data from pdf docs, word docs or data downloaded in json format. I'm not avers
e of coding so I can code one if I know what to do. Please suggest. Also please post any useful suggestions, articles, c
ourse, etc.

 
```
---

     
 
all -  [ Local/Private LLM based chatbot using free/open source tools. ](https://www.reddit.com/r/LLMDevs/comments/18dcktp/localprivate_llm_based_chatbot_using_freeopen/) , 2023-12-11-0910
```
I intend to create a local llm based chatbot for my team. Basically it should be able to read the docs and generate inte
lligent responses. I'm pretty new to LLMs and have tried few things here and there. Overall I intend to present a protot
ype on a non-GPU or useless GPU based machine first. From what I understand so far I need to create a RAG pipeline. I've
 seen few architectures using embeddings, vector databases, langchain and a model to do create such a pipeline. I'm stil
l pretty new to all these jargons. I have tried few opensource models as well locally and most of them just crash my M1 
laptop. I have better work laptop with 16 GP RAM and 8GB graphics card memory on an A2000 card. Can you please suggest h
ow can I quickly come up with a prototype. Basically the RAG pipeline(or any other method) should be able to quickly swi
tch between different LLM models, or databases or any other components when it comes to deploying on a production setup.
 Also, for now, the idea is to use the data from pdf docs, word docs or data downloaded in json format.  I'm not averse 
of coding so I can code one if I know what to do. Please suggest. Also please post any useful suggestions, articles, cou
rse, etc.
```
---

     
 
all -  [ flex-prompt: a flexible prompt renderer for LLMs that ensures you never overflow your model's contex ](https://www.reddit.com/r/Python/comments/18daixz/flexprompt_a_flexible_prompt_renderer_for_llms/) , 2023-12-11-0910
```
When working with LLMs, I frequently experience *token agony*.

[this model takes 4,097 words and you are trying to push
 in the whole of War and Peace, you imbecile](https://preview.redd.it/o6183i7byy4c1.png?width=1348&format=png&auto=webp&
s=cda9ffd45a5024116326dd1d5ed947712e119724)

Perhaps you've experienced it too! The issue is particularly pronounced wit
h retrieval augmented pipelines, since you have potentially quite a large set of documents which you could perhaps inclu
de in the prompt if only you knew how big it could be.

I got tired of hacking around this headache, so I wrote [flex pr
ompt](https://pypi.org/project/flex-prompt/) to address it. I wish I didn't have to. Perhaps someone can point me to a b
etter solution! But I couldn't find one, so alas, here it is.

Flex prompt provides a basic layout and component model t
o help you describe how you want the pieces of your prompt to grow and shrink and a token-aware renderer which renders y
our prompt to fit your model's window.

[Github](https://github.com/queerviolet/flex-prompt), [Intro to flex prompt cola
b](https://colab.research.google.com/github/queerviolet/flex-prompt/blob/main/doc/intro_to_flex_prompt.ipynb)

# Quick e
xamples

You can just `render(Flex(...), model=<model string or LangChain / Haystack object>)`, and flex prompt will fit
 the prompt into the context window, and tell you how many tokens are left over for the response:

    from flex_prompt 
import render, Flex, Expect
    rendered = render(
        Flex([
          'Given the text, answer the question.',
    
      '--Text--',
          WAR_AND_PEACE,
          '--End Text--',
          'Question: What's the title of this text?
',
          'Answer:', Expect()
        ], join='\n'),
        model='text-davinci-002')
    
    # rendered.output is 
the string to send to the model
    # rendered.max_response_tokens is how many tokens you can
    #   request in respons
e without exceeding the model's context window
    print(rendered.output, rendered.max_response_tokens)

More typically,
 you'll want to define a prompt which takes parameters. To do this, you can create a class (probably a dataclass) which 
derives `Flexed`:

    from flex_prompt import Flexed, Expect
    from dataclasses import dataclass
    
    @dataclass

    class Ask(Flexed):
      text: str
      question: str
      answer: str | Expect = Expect()
      instruct: str = '
Given a text, answer the question.'
    
      flex_join = '\n' # yielded items will be joined by newlines
      def con
tent(self, _ctx):
        if self.instruct:
          yield 'Given the text, answer the question.'
          yield ''
  
      yield '-- Begin Text --'
        # note: we're using `Flex` here just to attach a flex_weight
        # to the tex
t, telling the renderer we'd like more space for the
        # text than anything else.
        yield Flex([self.text], 
flex_weight=2)
        yield '-- End Text --'
        yield 'Question: ', self.question
        yield 'Answer: ', self.a
nswer

Note that the component above can be used to render both the actual prompt and examples. Examples simply have an 
`answer`. This is useful for experimenting with different ways of structuring a prompt while ensuring that all the examp
les we present to the LLM are in the same format.

# Internals

This was interesting to write! It's been a hot second si
nce I touched Python in a real way, but gosh what a nice language. I particularly appreciate the new (to me) `@dataclass
` machinery, which really reduces boilerplate.

The renderer works much as you might expect: a pretty standard recursive
 delegating renderer. It knows how to render `str` into `Tokens` and if you render a callable it calls it, which is how 
any more complex behavior happens.

You can yield anything which you can pass to the top-level render function, includin
g other components, creating a whole tree. Internally, flex prompt is super lazy. This more or less happened automatical
ly through extensive use of iterators. `render` creates a `Rendering`, which renders its input into a sequence of parts—
parts can be concrete token lists, but also child `Rendering`s, which is how we store the render tree. I mostly expect t
hat having the tree on hand will be useful for prompt optimization: e.g. measuring tokens spent on examples vs performan
ce at some task. It would certainly be possible to track these tokens during rendering rather than querying for them aft
erwards, but it honestly seemed harder. In any case, being super particular about performance at this stage seems a litt
le silly: each token is about to swell to 16kb and burn down half the amazon on its way to becoming `P(butts) ~ 0.2`, so
 it's unclear to me that the rendering process will ever be the bottleneck (even if the LLM is running on another machin
e, as it is in these examples).

# Is it worth it?

As models grow larger and larger context windows, I've asked myself 
whether this is worth it. Won't context sizes eventually big enough to put in everything we might want without worry?

O
ne response: 'everything I might want' is a very, very big set, plausibly bigger than any window size we're going to see
 soon.

Another: being able to do this kind of token accounting is useful even if we don't completely fill context windo
ws. For example, we might be able to augment our prompt with examples, documents, and tips. How much space should we all
ocate to each? The answer might well be model-dependent. How do we figure it out?

Flex prompt's output, a `Rendering` o
bject, actually holds the entire component tree. You can look through the object to see how many tokens were allocated t
o each child. This is currently very manual, but it does provide the bedrock infrastructure to e.g. run tests to discove
r the optimal balance of augmented data for a given prompt and model.

Additionally, the right admixture (and for that m
atter, the right *phrasing*) may well be model-dependent. Flex prompt currently provides only very limited model-specifi
c rendering (you can look at [`ctx.target`](https://ctx.target), but it doesn't tell you much), but there's no reason th
at can't be significantly improved. At the extreme limit is prompt *erasure*, where we fine-tune a model to require no o
r minimal instructions/examples for a given set of prompts. Flex prompt can enable transitions like this with no changes
 to the pipelines themselves: you'd still use the same prompt components, they'd just render differently if the target i
s a fine-tuned model vs. a generic one.

# Status & Future Work

Flex prompt is very much in early development. I would 
love to hear if and how people find it useful, and would love input and contributions!

Some things I'd like to tackle i
n the future:

* **Rendering message lists.** Flex prompt currently only renders strings, though it's set up to be able 
to render any type of output. Message histories basically grow without bound, so supporting this seems like a no-brainer
.
* **Pagination**. If your rendering overflows (as above, where we're trying to stuff *the entirety of war and peace* i
nto a prompt), flex prompt will clip the offending pieces to fit. But there's currently no way to get 'the next page'. B
ut the `Rendering` actually retains enough information to do this! It would be great to be able to call `render(...).pag
es()` to get the sequence of prompts as we 'scroll' whatever has overflowed. This is medium-hanging fruit—a little trick
y because we do have to descend the tree of renderings to find the exact one(s) which overflowed and then update only th
ose.
* **Token accounting.** As mentioned above, you can currently grovel around in `Rendering` and look at the pieces o
f the prompt. This would be more useful if it were a little easier, e.g. if you could use `rendering[Examples]` to find 
all the parts rendered by the `Examples` component, or `rendering['advice']` to find all the parts which are tagged (som
ehow) as 'advice'. The use case here is prompt optimization: discovering the optimal number or percentage of tokens to a
llot to each thing we might want to drop into the prompt.
* **More integrations.** Currently, flex prompt only supports 
OpenAI models. You can register your own target finders, but it would be great to have more support out of the box. This
 is mostly a matter of digging around and finding the tokenizers and window sizes for common models, and then writing th
e appropriate target finders. Contributions very welcome!
* **Model tuning.** As mentioned above, the rendering context 
could provide a mechanism for fetching model-specific parameters. The basic idea is that `ctx[param]` will evaluate `par
am` against the context, and then we can define some parameter types which load their model-specific values from *gestur
es vaguely* somewhere.

Thanks for reading!

* [Flex prompt Github](https://github.com/queerviolet/flex-prompt)
* [Intro
 to flex prompt colab](https://colab.research.google.com/github/queerviolet/flex-prompt/blob/main/doc/intro_to_flex_prom
pt.ipynb)
* [My website](https://ashi.io). *shameless plug: I have a lot of engineering experience and a bit of machine 
learning experience and* [*I am currently looking for a job*](https://ashi.io/resume.pdf)
```
---

     
 
all -  [ [P] flex-prompt: a flexible prompt rendering engine that ensures you'll never exceed your LLM's cont ](https://www.reddit.com/r/MachineLearning/comments/18d581q/p_flexprompt_a_flexible_prompt_rendering_engine/) , 2023-12-11-0910
```
When working with LLMs, I frequently experience *token agony*.

[Error: This model's maximum context length is 4097 but 
you are trying to push in all of War and Peace, you imbecile](https://preview.redd.it/nldj0qva4s4c1.png?width=1348&forma
t=png&auto=webp&s=b16af79d83f329db1b77b32ed621f0138d7cc04d)

Perhaps you've experienced it too! The issue is particularl
y pronounced with retrieval augmented pipelines, since you have potentially quite a large set of documents which you cou
ld perhaps include in the prompt if only you knew how big it could be.

I got tired of hacking around this headache, so 
I wrote `flex-prompt` to address it. I wish I didn't have to. Perhaps someone can point me to a better solution! But I c
ouldn't find one, so alas, here it is.

`flex-prompt` provides a basic layout and component model to help you describe h
ow you want the pieces of your prompt to grow and shrink and a token-aware renderer which renders your prompt to fit you
r model's window.

[Github](https://github.com/queerviolet/flex-prompt), [Intro to flex prompt colab](https://colab.rese
arch.google.com/github/queerviolet/flex-prompt/blob/main/doc/intro_to_flex_prompt.ipynb)

# Quick examples

You can just
 `render(Flex(...))`, and flex prompt will fit the prompt into the context window, and tell you how many tokens are left
 over for the response:

    from flex_prompt import render, Flex, Expect
    rendered = render(
        Flex([
        
  'Given the text, answer the question.',
          '--Text--',
          WAR_AND_PEACE,
          '--End Text--',
     
     'Question: What's the title of this text?',
          'Answer:', Expect()
        ], join='\n'),
        model='tex
t-davinci-002')
    
    # rendered.output is the string to send to the model
    # rendered.max_response_tokens is how 
many tokens you can
    #   request in response without exceeding the model's context window
    print(rendered.output, 
rendered.max_response_tokens)

More typically, you'll want to define a prompt which takes parameters. To do this, you ca
n create a class (probably a dataclass) which derives `Flexed`:

    from flex_prompt import Flexed, Expect
    from dat
aclasses import dataclass
    
    @dataclass
    class Ask(Flexed):
      text: str
      question: str
      answer: s
tr | Expect = Expect()
      instruct: str = 'Given a text, answer the question.'
    
      flex_join = '\n' # yielded 
items will be joined by newlines
      def content(self, _ctx):
        if self.instruct:
          yield 'Given the tex
t, answer the question.'
          yield ''
        yield '-- Begin Text --'
        # note: we're using `Flex` here jus
t to attach a flex_weight
        # to the text, telling the renderer we'd like more space for the
        # text than a
nything else.
        yield Flex([self.text], flex_weight=2)
        yield '-- End Text --'
        yield 'Question: ', 
self.question
        yield 'Answer: ', self.answer

The renderer works much as you might expect. You can \`yield\` anyt
hing which you can pass to the top-level render function, including other components, creating a whole tree.

Note that 
the component above can be used to render both the actual prompt and examples. Examples simply have an `answer`. This is
 useful for experimenting with different ways of structuring a prompt while ensuring that all the examples we present to
 the LLM are in the same format.

# LangChain and Haystack Integrations

Flex prompt doesn't really care how you execute
 your prompt. For convenience, `render(model=)` does accept both LangChain and Haystack models:

    ask_tolstoy = Ask(t
ext=WAR_AND_PEACE, question='Who wrote this?')
    
    # Using LangChain
    from langchain.llms import OpenAI
    lc_l
lm = OpenAI()
    rendering = render(ask_tolstoy, model=lc_llm)
    print(lc_llm(rendering.output, max_tokens=rendering.
max_response_tokens))
    
    
    # Using Haystack
    from haystack.nodes import PromptModel
    
    hs_llm = Prompt
Model(model_name_or_path='text-davinci-002', api_key=os.environ['OPENAI_API_KEY'])
    rendering = render(ask_tolstoy, m
odel=hs_llm)
    print(hs_llm.invoke(rendering.output, max_tokens=rendering.max_response_tokens))
    

# Is it worth it
?

As models grow larger and larger context windows, I've asked myself whether this is worth it. Won't context sizes eve
ntually big enough to put in everything we might want without worry?

One response: 'everything I might want' is a very,
 very big set, plausibly bigger than any window size we're going to see soon.

Another: being able to do this kind of to
ken accounting is useful even if we don't completely fill context windows. For example, we might be able to augment our 
prompt with examples, documents, and tips. How much space should we allocate to each? The answer might well be model-dep
endent. How do we figure it out?

Flex prompt's output, a `Rendering` object, actually holds the entire component tree. 
You can look through the object to see how many tokens were allocated to each child. This is currently very manual, but 
it does provide the bedrock infrastructure to e.g. run tests to discover the optimal balance of augmented data for a giv
en prompt and model.

Additionally, the right admixture (and for that matter, the right *phrasing*) may well be model-de
pendent. Flex prompt currently provides only very limited model-specific rendering (you can look at [`ctx.target`](https
://ctx.target), but it doesn't tell you much), but there's no reason that can't be significantly improved. At the extrem
e limit is prompt *erasure*, where we fine-tune a model to require no or minimal instructions/examples for a given set o
f prompts. Flex prompt can enable transitions like this with no changes to the pipelines themselves: you'd still use the
 same prompt components, they'd just render differently if the target is a fine-tuned model vs. a generic one.

# Status
 & Future Work

Flex prompt is very much in early development. I would love to hear if and how people find it useful, an
d would love input and contributions!

Some things I'd like to tackle in the future:

* **Rendering message lists.** Fle
x prompt currently only renders strings, though it's set up to be able to render any type of output. Message histories b
asically grow without bound, so supporting this seems like a no-brainer.
* **Pagination**. If your rendering overflows (
as above, where we're trying to stuff *the entirety of war and peace* into a prompt), flex prompt will clip the offendin
g pieces to fit. But there's currently no way to get 'the next page'. But the `Rendering` actually retains enough inform
ation to do this! It would be great to be able to call `render(...).pages()` to get the sequence of prompts as we 'scrol
l' whatever has overflowed. This is medium-hanging fruit—a little tricky because we do have to descend the tree of rende
rings to find the exact one(s) which overflowed and then update only those.
* **Token accounting.** As mentioned above, 
you can currently grovel around in `Rendering` and look at the pieces of the prompt. This would be more useful if it wer
e a little easier, e.g. if you could use `rendering[Examples]` to find all the parts rendered by the `Examples` componen
t, or `rendering['advice']` to find all the parts which are tagged (somehow) as 'advice'. The use case here is prompt op
timization: discovering the optimal number or percentage of tokens to allot to each thing we might want to drop into the
 prompt.
* **More integrations.** Currently, flex prompt only supports OpenAI models. You can register your own target f
inders, but it would be great to have more support out of the box. This is mostly a matter of digging around and finding
 the tokenizers and window sizes for common models, and then writing the appropriate target finders. Contributions very 
welcome!
* **Model tuning.** As mentioned above, the rendering context could provide a mechanism for fetching model-spec
ific parameters. The basic idea is that `ctx[param]` will evaluate `param` against the context, and then we can define s
ome parameter types which load their model-specific values from *gestures vaguely* somewhere.

Thanks for reading!

* [F
lex prompt Github](https://github.com/queerviolet/flex-prompt)
* [Intro to flex prompt colab](https://colab.research.goo
gle.com/github/queerviolet/flex-prompt/blob/main/doc/intro_to_flex_prompt.ipynb)
* [My website](https://ashi.io). *shame
less plug: I have a lot of engineering experience and a bit of machine learning experience and* [*I am currently looking
 for a job*](https://ashi.io/resume.pdf)
```
---

     
 
all -  [ Need help for asking the AI to select the right function ](https://www.reddit.com/r/LocalLLaMA/comments/18d0aal/need_help_for_asking_the_ai_to_select_the_right/) , 2023-12-11-0910
```
Hi all,

I'm exploring ways for AI to select the right function based on user input and seeking community insights. I've
 tried LangChain but found it complex for practical use. Grammar with GBNF files seems promising but might require lengt
hy initial prompts.

Has anyone experimented with alternatives, especially with models like 7B Mistral? Looking for stra
tegiesfor accurate in function selection . Any experiences or suggestions on this would be greatly appreciated.

Thanks!

```
---

     
 
all -  [ Any langchain integrations that search and crawl? ](https://www.reddit.com/r/LangChain/comments/18cv1ds/any_langchain_integrations_that_search_and_crawl/) , 2023-12-11-0910
```
Basically I want to have my llm do research for me. Would be nice to have some sort of feedback system rather than just 
dumb for loops. 

Any advice?
```
---

     
 
all -  [ LangServe: Stream works, Invoke doesn't ](https://www.reddit.com/r/LangChain/comments/18cun5p/langserve_stream_works_invoke_doesnt/) , 2023-12-11-0910
```
I'm building a very simple chain that takes as an input a customer feedback string and categorizes it into the following
 pydantic class:

      class AnalysisAttributes(BaseModel):
        overall_positive: bool = Field(description='<sentim
ent is positive overall>')
        mentions_pricing: bool = Field(description='<pricing is mentioned>')
        mentions
_competition: bool = Field(description='<competition is mentioned>')
    
    parser = PydanticOutputParser(pydantic_obj
ect=AnalysisAttributes)

&#x200B;

Here's how this should work, and it does:

    full_pipeline = prompt | model | parse
r
    
        output = full_pipeline.invoke({'feedback': 'This bad company is very expensive.'})
    
        expected_
output = AnalysisAttributes(overall_positive=False, mentions_pricing=True, mentions_competition=False)
        assert ou
tput == expected_output.  # this works! :)

&#x200B;

This works very well, all good so far! Let's serve it:

    app = 
FastAPI(
      title='LangChain Server',
      version='1.0',
      description='A simple api server using Langchain's R
unnable interfaces',
    )
    
    pipeline = prompt | model | parser
    add_routes(app, pipeline, path='/categorize_f
eedback')
    
    if __name__ == '__main__':
        import uvicorn
        uvicorn.run(app, host='localhost', port=800
0)

&#x200B;

Now comes the strange part, check this out. On the client side, streaming works:

    response = requests.
post(
        'http://localhost:8000/categorize_feedback/stream/',
        json={'input': {'feedback': 'Prices are too h
igh.'}}
    )
    for chunk in response:
        print(chunk.decode())
    
    # event: metadata [...] data: {'overall_
positive':false, ...

**But the regular invoke does not work, it delivers an empty output:**  


    response = requests
.post(
        'http://localhost:8000/categorize_feedback/invoke/',
        json={'input': {'feedback': 'Prices are too 
high.'}}
    )
    print(response.json())
    
    # {'output': {}, 'callback_events': [], 'metadata': {'run_id': 'acdd0
89d-3c80-4624-8122-17c4173dc1ec'}}

Any ideas? For more info, check out the langserve playground output: 

https://previ
ew.redd.it/1fc9vbfcav4c1.png?width=1930&format=png&auto=webp&s=e8bd8119978ed74ebe9d1b8d453b77263fbc3701
```
---

     
 
all -  [ Open AI and LangChain Chatbot ](https://www.reddit.com/r/LangChain/comments/18cts9j/open_ai_and_langchain_chatbot/) , 2023-12-11-0910
```
Hello Everyone,

I have developed a Chatbot using LangChain, Open AI LLM and Next Js.

The chatbot currently is by the n
ame of 'HR Chatbot'.

If you want to get a chatbot developed using LangChain, Open AI and Next Js/Python you can PM me. 
Or if you are a developer I can directly sell you the source code of the one that I have built. 

I am even open to sett
ing up a free consultation!
```
---

     
 
all -  [ pickle error while trying to use langchain with chromadb and rayllm ](https://www.reddit.com/r/LangChain/comments/18crvph/pickle_error_while_trying_to_use_langchain_with/) , 2023-12-11-0910
```
I am trying to speed up my embeddings with rayllm integration on my m1 macbook pro. This is what the new code looks like
:  


\`@ray.remote   
def process\_shards(shard,collection\_name):  
 print('embedding stuff')  
 embeddings = OpenAIEm
beddings(model='text-embedding-ada-002')  
 print(f'Starting process\_shard of {len(shard)} chunks.')  
 st = time.time(
)  
 result = Chroma.from\_documents(shard,embeddings,collection\_metadata={'hnsw:space': 'cosine'})  
 et = time.time()
 - st  
 print(f'Shard completed in {et} seconds.')  
 return result\`

&#x200B;

&#x200B;

above is called be by follow
ing method :  


\`def get\_vectorstore(collection\_name,text\_chunks):  
 \#sharded processing with ray  
 embeddings =
 OpenAIEmbeddings(model='text-embedding-ada-002')  
 if text\_chunks is None:  
 return Chroma(persist\_directory=persis
t\_directory,embedding\_function=embeddings,collection\_name=collection\_name)  
 shards = np.array\_split(text\_chunks,
 db\_shards)  
 futures = \[process\_shards.remote(shards\[i\],collection\_name) for i in range(db\_shards)\]  
 results
 = ray.get(futures)  
 \#post processing after shards are available.  
 db = results\[0\]      
 for i in range(1,db\_sh
ards):  
 db.merge\_from(results\[i\])  
 print('now creating a new database to persist')  
 \#create new chromadb and p
ersist it  
 \#db.persist()  
 return db\`

&#x200B;

&#x200B;

when i run this, i get the following error:  


TypeErro
r: cannot pickle 'sqlite3.Connection' object

&#x200B;

&#x200B;

Anyone who has solved for same ? Much appreciated.
```
---

     
 
all -  [ How do i add memory to a create_csv_agent? ](https://www.reddit.com/r/LangChain/comments/18cqjxh/how_do_i_add_memory_to_a_create_csv_agent/) , 2023-12-11-0910
```
As title suggests, i want to add memory to vreate_csv_agent so that it remembers past conversations and queries from the
 subset of data it provided in the past in case the user prompts for it? If any further explanation is required please a
sk, but help me out.
```
---

     
 
all -  [ Does using a vector db increase LLM API cost? ](https://www.reddit.com/r/LangChain/comments/18cpx8j/does_using_a_vector_db_increase_llm_api_cost/) , 2023-12-11-0910
```
First time looking into LangChain and vector dbs. I have been creating with some fun applications with LLMs so I have so
me understanding of how they work and how to interface with them. 

Reading through the LangChan doc, I'm trying to get 
an understanding of how vector dbs affect the prompt? To early understandings, to me it seems like using a vector db wou
ld increase the tokens used by LLM in the prompts and thus the cost (if using an API, like Open AI). 

Can anyone provid
e any further insight? Is this correct?
```
---

     
 
all -  [ Interview Prep and resume checker! ](https://www.reddit.com/r/LangChain/comments/18cmpce/interview_prep_and_resume_checker/) , 2023-12-11-0910
```
Hey all, I was wondering if there’s a dedicated app to upload both resume and job posting to get insights whether someon
e is a good fit for the job. Provide suggestions, insight even hold a mock interview! 

It sounds like a great use for A
I and considering the current job market it could really helpful. If something like this doesn’t exist I would love to b
uild something like this! 

Looking forward to y’all’s feedback
```
---

     
 
all -  [ Data privacy with LLM Saas companies ](https://www.reddit.com/r/LangChain/comments/18cilzo/data_privacy_with_llm_saas_companies/) , 2023-12-11-0910
```
How LLM Saas companies handle the data that is provided by customers?

For enterprise  customers, what is the best strat
egy to retain data in-house and use LLMs?

Curios to know the thoughts/comments from the community.

Edit: 

1. As a Saa
s user, enterprise customers will make API calls with input in required format

Input → API Call → Saas Servers

For RAG
 use cases, Saas company might be pre-processing, building vectordbs on enterprise data to provide relevant answers.

Ho
wever, saas company employees can see what data is coming in. Even though most of the Saas companies adhere to GDPR and 
other data privacy policies, they still have access to what enterprise customers are doing with their models.

2. If an 
enterprise is paranoid about sharing their proprietary data, one of the option to use LLMs is:

Take an open source LLM 
model → fine tune to enterprise data (optional) → create RAG with enterprise data →  Deploy it in cloud/on-prem → Provid
e a secure endpoint to enterprise users

Data doesn't leave but users within enterprise can leverage the benefits of RAG


Am I missing anything here?

&#x200B;
```
---

     
 
all -  [ [D] Working on RAG? You should be evaluating its performance and we've built a way to do that. ](https://www.reddit.com/r/MachineLearning/comments/18ciet5/d_working_on_rag_you_should_be_evaluating_its/) , 2023-12-11-0910
```
Check out our new open-source tool, Tonic Validate: [https://www.tonic.ai/validate](https://www.tonic.ai/validate)  


W
e've also been using the tool to evaluate different RAG tools out there. The latest post on LangChain vs Haystack is ava
ilable here:  [https://www.tonic.ai/blog/rag-evaluation-series-validating-the-rag-performance-of-langchain-vs-haystack](
https://www.tonic.ai/blog/rag-evaluation-series-validating-the-rag-performance-of-langchain-vs-haystack)

&#x200B;

Let 
us know what you think and if you're working on a RAG project, we'd love to hear about it! How are you measuring your RA
G system performance?
```
---

     
 
all -  [ I've recently been asked to build a LLM backend stack for our applications, what language should I c ](https://www.reddit.com/r/AskProgramming/comments/18chqic/ive_recently_been_asked_to_build_a_llm_backend/) , 2023-12-11-0910
```
Hi, I've recently been asked to build from a scratch a new API platform that will serve a number of different LLM functi
onalities to our applications. The stack will be deployed to azure and will involve many components that are common in t
he LLM space (langchain, pytorch, vector databases etc)

The stack is expected to be built using the micro services arch
itecture, orchestrated with kubernates. 

Because of the LLM nature of this platform, a lot of code is python oriented (
opensource etc) however there are a lot more competent backend developers in other languages than python (node, rails, g
o etc) 

Since it's going to be micro services anyway, I was thinking that a polyglot tech team can potentially work. On
 the other hand, it sounds like a lot of risks. 

What would you recommend?
```
---

     
 
all -  [ Can I take results from create_sql_agent and do other things with it? ](https://www.reddit.com/r/LangChain/comments/18chjxz/can_i_take_results_from_create_sql_agent_and_do/) , 2023-12-11-0910
```
I’m using the above to query a sql database and return results. However in cases where text is returned (like a few prod
uct reviews for example) I’d like to know the sentiment of each review and how this is changing over time. Is it possibl
e to do this with langchain?

Thanks!
```
---

     
 
all -  [ RAG with agents ](https://www.reddit.com/r/LangChain/comments/18cemoh/rag_with_agents/) , 2023-12-11-0910
```
I want to create an agent that is able to do RAG using langchain.  
I found this: [https://python.langchain.com/docs/use
\_cases/question\_answering/conversational\_retrieval\_agents](https://python.langchain.com/docs/use_cases/question_answ
ering/conversational_retrieval_agents)  
I can't seem to get it to focus its search on the database alone, it still goes
 to its general knowledge to answer.
```
---

     
 
all -  [ How I Experiment with Open LLMs ](https://www.reddit.com/r/LocalLLaMA/comments/18cd7ok/how_i_experiment_with_open_llms/) , 2023-12-11-0910
```
Over the last four months, I've spent 200+ hours playing with open-source models on HuggingFace.

And I've found that, w
hile benchmarks are decent signal, they don't always translate into practical effectiveness or correlate with how I'm pl
anning on using a model.

So, I want to pull back the curtain and share my 'vibe check' method because I don't like blin
dly following leaderboard rankings.

## 🏁 Starting with Baseline Generations

What I Do: I test 10-15 diverse prompts us
ing the model's default generation parameters.

Why It Matters: This step gives me a raw, unfiltered look at the model's
 out-of-the-box behaviour and sets a baseline for further experimentation.

## ✅ Selective Prompt Analysis

Process: I c
hoose a balanced mix of 3-5 prompts, some showcasing the model's high performance and others where it falls short.

Obje
ctive: It's all about levelling the playing field. This way, I get to see the real impact of tweaking those parameters. 
Just straightforward insights into how these changes play out.

## 🎛️ Parameter Adjustment - One at a Time

Approach: I 
experiment with one parameter at a time — temperature, num\_beams, top\_k, top\_p, repetition\_penalty, no\_repeat\_ngra
m\_size.

Goal: Observing changes in output helps me understand how each parameter influences the model’s responses.

At
 this point I usually have hundreds of generations from the model.

## 🕵️‍♂️ Deep Dive into Model Behavior

Method: I ma
nually review the generations, hunting for odd or undesirable outputs.

Insight: This granular analysis is crucial for i
dentifying the model's subtle nuances and potential pitfalls.

## 💻 Writing Targeted Tests

Strategy: Develop tests for 
specific issues noticed during the exploratory phase (e.g., output length, gibberish, repetition). Use type-token ratio 
for assessing lexical diversity, and check for repeat n-gram sizes.

Purpose: Makes it easier to do more fine-grained st
atistical analysis down the line.

## 🧩 The Grid Search

Execution: I perform a detailed grid search over a range of par
ameter values across several prompts.

Aim: Find a handful of effective settings that consistently yield desirable resul
ts.

## 🎯 The Final Stretch

Process: I test these top settings across an expanded set of 20+ prompts, looking for consi
stent performance and reliability.

Result: This gives me a comprehensive understanding of how the model behaves under v
arious settings and prompts.

## 🔬 Utilizing Advanced Tools

Integration: Finally, I use tools like LangChain's criteria
 evaluators with GPT-4 to assess output.

Benefit: This step adds a layer of sophistication and accuracy to the selectio
n process.

## I could be totally wrong about the whole approach...but it's the best I came up with.

There are so many 
moving parts when selecting an LLM, that I was going through some analysis paralysis...this approach is a bit brute forc
e, but it's at least helped me justify why I choose the settings I did.

I guess we could call this 'principled vibe che
cking' lol

🫵🏽 Your Turn: Share Your Insights! Do you have a different approach to selecting and tuning LLMs?

Share you
r strategies, tips, or even constructive critiques. Looking forward to your stories and experiences in the comments belo
w!
```
---

     
 
all -  [ chatGPT doesn't have access to langchain ](https://www.reddit.com/r/LangChain/comments/18ccamh/chatgpt_doesnt_have_access_to_langchain/) , 2023-12-11-0910
```
i'm using chatGPT-4 for coding and i noticed it doesn't use langchain properly. i mean that if i want chatGPT to impleme
nt a basic example using pytorch or sk-learn it does so without much hassle, but when it comes to a simple example with 
langchain it starts to show me rough estimates of how the code should look like and not actual runnable code.   


I'm w
ondering, is there a way to bypass that or is it intentional? 
```
---

     
 
all -  [ I want to extract important keywords from large documents... ](https://www.reddit.com/r/LangChain/comments/18cbvfj/i_want_to_extract_important_keywords_from_large/) , 2023-12-11-0910
```
Currently I am looping over chunks and getting keywords using prompt...

How do I combine the keywords from different ch
unks to get the most important keywords of the whole doc.  

I was thinking of giving the summary of document(to underst
and context) as an input to the prompt along with all the keywords to get final output...

Any better method to do this?


TIA
```
---

     
 
MachineLearning -  [ [R] LLMs for structured data? ](https://www.reddit.com/r/MachineLearning/comments/185ei6v/r_llms_for_structured_data/) , 2023-12-11-0910
```
I've been trying to work with structured data in language models, and it's proving to be quite challenging. I'm confiden
t that with Langchain, I should be able to solve the problem, but I'm not entirely sure which path to take among all the
 options the library offers.

My issue is as follows: I have data in the form of dictionaries regarding a series of prod
ucts, for example, laptops. The data looks like this:

{Identifier 1: X, Identifier 2: Y, Value name: Z}

(Several succe
ssive dictionaries like this.)

I want to use this series of dictionaries as context, then feed a different dictionary i
nto the Language Model, and have it tell me if the 'Value name' makes sense given Identifiers 1 and 2. An example would 
be Identifier 1: laptops, Identifier 2: brand, Value name: Lenovo. In this case, it should return affirmative since Leno
vo makes sense as a brand. However, if I input 'oranges,' it should return negative.

Any ideas on which library I could
 use to tackle this problem?
```
---

     
 
MachineLearning -  [ [P] A new way of interacting with Hacker News ](https://www.reddit.com/r/MachineLearning/comments/183n6h7/p_a_new_way_of_interacting_with_hacker_news/) , 2023-12-11-0910
```
Hi all!

A couple of days ago, when I was scrolling down Hacker News, exploring news about OpenAI and the latest specula
tion about Q\*, it occurred to me to create a ChatBot that would allow me to interact with Hacker News directly, in a co
nversation.

Using streamlit, langchain and openai functions I managed to create a first version of this chat (I still h
ave to add RAG for news analysis and test other types of LLMs). 

Here is an example, what do you think?

Code: [https:/
/github.com/neural-maze/talking\_with\_hn](https://github.com/neural-maze/talking_with_hn)

App: [https://newsnerdhacker
bot.streamlit.app/](https://newsnerdhackerbot.streamlit.app/)

&#x200B;

https://i.redd.it/rtpof7biqi2c1.gif
```
---

     
 
MachineLearning -  [ [Discussion] Is it possible to built a Multi-LLM Assistant? ](https://www.reddit.com/r/MachineLearning/comments/182uuwp/discussion_is_it_possible_to_built_a_multillm/) , 2023-12-11-0910
```
 

  
For example with the following structure:

* System = GPT-4 Turbo + Llama2 +3rd LLM (!)+ Google or Bing API for we
bsearch + Langchain + any vectorDB + Document upload + longterm Memory + …

Idee behind it is to get more accurate, upda
ted (websearch) and specialized system or even let the LLms discuss your prompt before completion! Question is also, how
 shall the interaction of multiple LLMs in a system be organzied (Algorithm, Python Library …)? And what kind of Interac
tion can/should this be? Master-slave or Multi-Master system?
```
---

     
 
MachineLearning -  [ [D] Made some promises. Time to learn how to conduct very large scale pdf doc analysis. ](https://www.reddit.com/r/MachineLearning/comments/181gzek/d_made_some_promises_time_to_learn_how_to_conduct/) , 2023-12-11-0910
```
I have about a half million pdfs I need to summarize. Very wide range of types: invoices, diagrams, contracts, emails, l
etters, pictures, schedules, notices, data sheets, manuals, more. 

Which is... woof. Something else. I've been trying f
or many hours now to figure out a service/combination thereof that can get me there, but I'm seriously struggling. The *
ideal* solution would be to throw the pdfs in and have it return a csv with dates and summaries, maybe parsed out email 
heading info.

I'm currently running these pdfs through Acrobat OCR now, which its own special hell.

I've tried myriad 
local and webhosted solutions. The BEST results in what is almost the perfect system for this I found on https://docalys
is.com/. Good text results, works in batches, BUT I can only upload a single document at a time. They have a service to 
do batch processing and so I'm waiting to hear from them now. I imagine at the scale I need it's expensive.

I also got 
this solution working: https://github.com/mayooear/gpt4-pdf-chatbot-langchain. Seemed solid, I was able to upload a thou
sand pdfs in a single go, but it would keep returning information from only 2-3 documents. Upload 5? Results for 2-3. Up
load a thousand? Results for 2-3. My uneducated guess is that it's hitting the OpenAI API token limit, but maybe not?

I
 know it's possible, just not whether it's feasible for an end user.
```
---

     
 
MachineLearning -  [ Google PaLM Error [D] ](https://www.reddit.com/r/MachineLearning/comments/17y7arb/google_palm_error_d/) , 2023-12-11-0910
```
Google PaLM Error

Using LangChain and Google PaLM, in sequential chain concept getting following error,

ChatGooglePalm
Error: ChatResponse must have atleast one candidate

Please help!
```
---

     
 
MachineLearning -  [ [D] System Design question for LangChain ](https://www.reddit.com/r/MachineLearning/comments/17x545j/d_system_design_question_for_langchain/) , 2023-12-11-0910
```
Hi

Just to prepare the system design question for LangChain. Is there a resource that can walk me through the high leve
l pipeline? I know there are a bunch of resources that dive into detail implementation. But that's not I want. I want hi
gh level conceptual walk-through. 
```
---

     
 
deeplearning -  [ [D] Utilizing Multimodal LLM for Extracting Tables and Images LangChain+LlamaIndex’s Role in Semi-St ](https://www.reddit.com/r/deeplearning/comments/185vd56/d_utilizing_multimodal_llm_for_extracting_tables/) , 2023-12-11-0910
```
In the domain of document analysis, the convergence of text, tables, and images presents formidable challenges for conve
ntional RAG (Retrieval Augmented Generation) methodologies. This complexity is further compounded within semi-structured
 data, notably in the extraction of tables from PDFs. Enter LangChain, a pioneering tool adept at navigating these intri
cate landscapes. Augmenting its capabilities is LlamaIndex, integrating Multi-Modal Retrieval Augmented Generation (RAG)
 techniques. Together, LangChain and LlamaIndex stand poised to revolutionize the handling and extraction of diverse con
tent types, promising a breakthrough in unraveling insights from varied data formats.

Link in the comment
```
---

     
