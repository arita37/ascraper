 
all -  [ (Code included) Struggle to scrape websites and feed content to LLMs? I benchmarked some tools and t ](https://www.reddit.com/r/LangChain/comments/1cub6pg/code_included_struggle_to_scrape_websites_and/) , 2024-05-18-0910
```
Video: [https://www.youtube.com/watch?v=QxHE4af5BQE](https://www.youtube.com/watch?v=QxHE4af5BQE)

Code: [https://github
.com/trancethehuman/ai-workshop-code/blob/main/Web\_scraping\_for\_LLM\_in\_2024.ipynb](https://github.com/trancethehuma
n/ai-workshop-code/blob/main/Web_scraping_for_LLM_in_2024.ipynb)

  
Let me know what you think in the comments. I'll re
spond.
```
---

     
 
all -  [ Ingestion options for vectorDB ](https://www.reddit.com/r/vectordatabase/comments/1cu7e7n/ingestion_options_for_vectordb/) , 2024-05-18-0910
```
I’m trying to create some low latency ingestion ETL embedding pipelines into either pinecone or Zilliz or LanceDB for my
 application, the idea is whenever a user send some text, I can process and filter, group by then do llm assisted summar
ization immediately, then create embedding to save into a vectorDB without any intermediate storage. Fivetran only offer
s dbt on the storage layer, langchain does not handle sql processing, Dagster only deal with orchestration and seems mor
e appropriate for batch processing, aws lambda is the closest solution I can find but version control and monitoring mig
ht take some planning. setting up my own cluster just for this and monitoring it 24/7 seems the last resort. I wonder if
 there are other options. (We are a 3 person team, so coding time is really precious) thanks ahead! 
```
---

     
 
all -  [ Do you even need LangChain? ](https://www.reddit.com/r/LangChain/comments/1cu6wjg/do_you_even_need_langchain/) , 2024-05-18-0910
```
As a disclaimer: I personally think LangChain is awesome. It lets you cut your dev time by a lot. But since I've been to
ying around with many frameworks, tools, and models I compiled a list of five basic (but important) questions every dev 
or person looking to integrate AI must ask themselves.

**>>>** [**Watch on YouTube**](https://youtu.be/uG0cs8AlnHw)

  

I'd love to know your thoughts and/or suggestions!
```
---

     
 
all -  [ New tool to monitor agents built with Langchain, catch mistakes, manage costs ](https://useturret.com) , 2024-05-18-0910
```

```
---

     
 
all -  [ Introducing Cycls: A New AI Chat Framework ](https://www.reddit.com/r/Chatbots/comments/1cu5503/introducing_cycls_a_new_ai_chat_framework/) , 2024-05-18-0910
```
I wanted to introduce you to Cycls, a lightweight Python framework for developing and sharing AI chat applications. It's
 designed to simplify the process, offering features like easy publishing, instant sharing with public URLs, and multimo
dal input/output. Cycls supports popular models such as OpenAI and LangChain and includes a ready-to-use webchat fronten
d.

If you're into AI development, this might be worth checking out. You can learn more about it [here](https://docs.cyc
ls.com/overview).

What are your thoughts? Anyone planning to give it a try?
```
---

     
 
all -  [ Sentence / chunk window retrieval in Langchain using Qdrant ](https://www.reddit.com/r/LangChain/comments/1cu44i1/sentence_chunk_window_retrieval_in_langchain/) , 2024-05-18-0910
```
Guys,

Checkout this PR [\[https://github.com/langchain-ai/langchain/pull/21553\]](https://github.com/langchain-ai/langc
hain/pull/21553) that implements something similar to sentence window retrieval. I have named in chunk window retrieval 
because based on the window size, this method would fetch those many chunks above and below the current chunk. 

Importa
nt point to note here is that when creating a chunk for Qdrant, you MUST have integer based chunk id for this to work. H
ave added that support in Qdrant.add\_texts(..) as well. 

Hope it helps.
```
---

     
 
all -  [ Utilizing Neo4j's Knowledge Graph and Semantics for a RAG - Chatbot ](https://www.reddit.com/r/LangChain/comments/1cu2ozt/utilizing_neo4js_knowledge_graph_and_semantics/) , 2024-05-18-0910
```
I'm working on developing a chatbot that uses Neo4j as the database. I've created a knowledge graph by importing a corpu
s of data into Neo4j.  
how to effectively leverage both the knowledge graph aspect and the semantic capabilities of Neo
4j for this chatbot project?

Has anyone worked on a similar project? What strategies or approaches did you employ to op
timize the retrieval from Neo4j? I'm open to any suggestions or insights that could help improve the chatbot's performan
ce and make the most out of Neo4j's unique features.
```
---

     
 
all -  [ Gemini directed me to porn ](https://i.redd.it/bddxj0u0ly0d1.jpeg) , 2024-05-18-0910
```
All I asked was if it could create agents. The first link it provided is porn. 
```
---

     
 
all -  [ Advanced RAG: Ensemble Retriever ](https://www.reddit.com/r/LargeLanguageModels/comments/1ctzxqx/advanced_rag_ensemble_retriever/) , 2024-05-18-0910
```
Hi,

Made a video on Advanced RAG: **Ensemble Retriever**.

The Ensemble Retriever combines multiple high-performing ret
rieval techniques simultaneously, using majority voting and ranking to deliver **strong relevant** passages.

The logic 
is: Better retrieved passages == better context == better generation.

Originally it comes from this paper: **Reciprocal
 Rank Fusion outperforms Condorcet and individual Rank Learning Methods**



But I made a video on how to use it with La
ngchain and llama Index with GPT-4o.

Hope you find it useful.

[**https://youtu.be/s2i4zeWjUtM**](https://youtu.be/s2i4
zeWjUtM)
```
---

     
 
all -  [ Advanced RAG: Ensemble Retriever ](https://www.reddit.com/r/LanguageTechnology/comments/1ctzxje/advanced_rag_ensemble_retriever/) , 2024-05-18-0910
```
Hi,

Made a video on Advanced RAG: **Ensemble Retriever**.

The Ensemble Retriever combines multiple high-performing ret
rieval techniques simultaneously, using majority voting and ranking to deliver **strong relevant** passages.

The logic 
is: Better retrieved passages == better context == better generation.

Originally it comes from this paper: **Reciprocal
 Rank Fusion outperforms Condorcet and individual Rank Learning Methods**

But I made a video on how to use it with Lang
chain and llama Index with GPT-4o.

Hope you find it useful.

[**https://youtu.be/s2i4zeWjUtM**](https://youtu.be/s2i4ze
WjUtM)
```
---

     
 
all -  [ Basic RAG chat bot minimum ](https://www.reddit.com/r/LangChain/comments/1ctztvf/basic_rag_chat_bot_minimum/) , 2024-05-18-0910
```
Hi-
  I have followed a few simple RAG tutorials with langchain but don’t seem to be getting anywhere - either my agent 
exits before a final answer or my chain just exits with nothing.

  I’m a newbie to RAG and LLMs in general so I wanted 
to check a few things that I haven’t managed to learn from online tutorials.

1. I assume choice of vector DB makes very
 little difference for these small toy projects with only <50 PDFs being ingested - each not large.

2. I don’t understa
nd if the embeddings function in between PDF and DB needs to be matched with anything else later in the toolchain- can I
 use pretty much anything with impunity? I’m using the langchain pypdfloader, load_and_split and langchain.embeddings.Hu
ggingFaceEmbeddings.
This is perhaps a mishmash from different tutorials…

3. Is there a ‘best’ way to run a LLM locally
? I have tried straight python and llamacpp from langchain but it doesn’t seem to recognise my GPU.
  I’m thinking of mo
ving to running the llm on LMStudio and accessing the API in python but that’s additional complexity I would rather avoi
d at this stage. (Or is it super easy?)

I’m sure I will have more questions later but this is enough to keep me going f
or now!
Thanks!
```
---

     
 
all -  [ Open source LLMs ](https://www.reddit.com/r/LangChain/comments/1ctzmfo/open_source_llms/) , 2024-05-18-0910
```
Hey there 🖖
Im participating in a national contest for NLP sentiment analysis
Im planning on using langchain. Wanted to 
ask you guys if you have any open source LLM recommendations for me to use or check, the model should be local so 70b ll
ama is not the best choice.
```
---

     
 
all -  [ How to extract the 'Methods' section out of a scientific article ](https://www.reddit.com/r/LangChain/comments/1ctz1jf/how_to_extract_the_methods_section_out_of_a/) , 2024-05-18-0910
```
Hi folks,

I am working on a project to develop a specific question-answer system based on RAG for scientific research. 
The questions could be 'What province, city or town were the samples collected from?'. 

The RAG pipeline I built now do
es not perform well because of many reasons. One reason is that the contents in the introduction and/or discussion secti
ons may confuse the pipeline. So one way I am thinking is to just extract the method section or method and results secti
ons for the vector store (ignoring the other sections). I have explored different options, but none of them worked. I ev
en tried the openai file search ([https://platform.openai.com/docs/assistants/tools/file-search](https://platform.openai
.com/docs/assistants/tools/file-search)), but it was not able to extract the complete section. 

I used pypdfloader to g
et all text from a pdf file first, and then asked openai file-search to extract the methods section. Is pypdfloader a go
od one to extract text in good order?

Anyone knows a good way to extract a specific section from a PDF file?

Thanks!
```
---

     
 
all -  [ Exploring Cost Efficiency: OpenAI GPT-4-Turbo Model vs. AWS OpenAI API ](https://www.reddit.com/r/LangChain/comments/1ctyz7h/exploring_cost_efficiency_openai_gpt4turbo_model/) , 2024-05-18-0910
```
I am reviewing the pricing for the OpenAI GPT-4-Turbo model and have noticed that using memory with it on RAG Task incur
s high costs. I am working for an organization. Is anyone using the AWS OpenAI API? Is it a bit cheaper to use?'
```
---

     
 
all -  [ Chunking text documents in langchain ](https://www.reddit.com/r/LangChain/comments/1ctyslg/chunking_text_documents_in_langchain/) , 2024-05-18-0910
```
I have to find a way to determine the format of a pdf document like its plain or having paragraphs or title-definition f
ormat etc. By knowing the format i can chunk the document efficiently without losing the context/semantics. Is there any
 way to do so?
```
---

     
 
all -  [ How to generate payments links in chatbot ? ](https://www.reddit.com/r/LangChain/comments/1ctypfm/how_to_generate_payments_links_in_chatbot/) , 2024-05-18-0910
```
i am building a hotel room booking chatbot using OpenAI API , currently it is able to look up available rooms from the d
atabase using langchains SQL agent , i want to add room booking functionality in it for that i want receive payments fro
m the user and thus i need chatbot to generate payments links. i know payments links can be generated using stripe or ra
zorpay api but how to make chatbot call those api functions to get paymnets link, does anyone has any expeiences with it
 or know how to do this? 
```
---

     
 
all -  [ How to generate payments links in chatbot ? ](https://www.reddit.com/r/Chatbots/comments/1ctyk9f/how_to_generate_payments_links_in_chatbot/) , 2024-05-18-0910
```
i am building a hotel room booking chatbot using OpenAI API , currently it is able to look up available rooms from the d
atabase using langchains SQL agent , i want to add room booking functionality in it for that i want receive payments fro
m the user and thus i need chatbot to generate payments links. i know payments links can be generated using stripe or ra
zorpay api but how to make chatbot call those api functions to get paymnets link?  
```
---

     
 
all -  [ Getting little callbacks, roast away ](https://www.reddit.com/r/resumes/comments/1ctw6qz/getting_little_callbacks_roast_away/) , 2024-05-18-0910
```
Finishing grad school in december, looking for anything in software engineering or data science/engineering. First two j
obs don't have bullet points due to lack of space (trying to keep to one page), but I thought they would still be valuab
le there anyway

https://preview.redd.it/52gau6s2sw0d1.png?width=5100&format=png&auto=webp&s=0b1d196ed69985473da777ffee7
ec8151751ac99


```
---

     
 
all -  [ Embeddings of certain dataset ](https://www.reddit.com/r/LangChain/comments/1ctv5au/embeddings_of_certain_dataset/) , 2024-05-18-0910
```
Hii community
I have a dataset with keys like name,description,why it matters,what to look for. Basically all these cont
ains 1 line information(avg 10 words) ,I want to embedd these dataset using open ai models what are different ways for e
mbedding these dataset .
My puropse is when user give some query i can give him top k matched results.
```
---

     
 
all -  [ How to extract date period from user prompt ](https://www.reddit.com/r/LangChain/comments/1ctr9h5/how_to_extract_date_period_from_user_prompt/) , 2024-05-18-0910
```
Hello everyone!
I would like to have some help for a problem i have
I want to extract two parameters:
date_from: the sta
rt of the period
date_to: the end of the period

I tried using this [example](https://python.langchain.com/v0.1/docs/use
_cases/extraction/) but it sometimes misses at simple prompts

What can i add to make it better?
Here’s the [code](https
://hastebin.skyra.pw/yehokamuqo.py) i made


Basically i want it to get from the user’s prompt the correct date or perio
d
```
---

     
 
all -  [ Classify PDF based on separate RAG database ](https://www.reddit.com/r/LangChain/comments/1ctqz2c/classify_pdf_based_on_separate_rag_database/) , 2024-05-18-0910
```
I’m trying to set something up where a user can upload a pdf and have it classified based on a resource I converted into
 a vector database. 
```
---

     
 
all -  [ Langchain using llama3 to build recommendation system ](https://www.reddit.com/r/Python/comments/1ctnxa4/langchain_using_llama3_to_build_recommendation/) , 2024-05-18-0910
```
Hi,

Recently I played a bit with LLMs, specifcally exploring ways of running the models locally and building prompts us
ing LangChain. As a result ended up coding a small recommendation system, powered with Llama3-7b model, which suggests t
opics to read on HackerNews.

Wanted to share my experiences, so I wrote a small article where I described all my findin
gs.  
Hope you'll like it: [https://lukaszksiezak.github.io/ScrapyToLLM/](https://lukaszksiezak.github.io/ScrapyToLLM/)


Github repo: [https://github.com/lukaszksiezak/ScrapyToLLM](https://github.com/lukaszksiezak/ScrapyToLLM)

**What the p
roject does:**

It's a Python application which uses scrapy to scrape HackerNews page. Scraped articles are pipelined to
 redis, which is then feeding Llama3 using langchain. Prompter is configured to serve a user articles which are matching
 his request.

**Target Audience**:

I think it suits the best all the people who are looking for a Hello World projects
 using LLMs. I think it also reveals some difficulties related to LLM tech, what potential problems could be found in pr
oduction systems.

**Comparison:**

Recommendation systems are widely used and known, however LLMs are the ones which ma
y work out of the box when appropriate prompt is given. It's kind of interesting to explore various usages of the techno
logy and take part in fast grow of that stack.

Cheers.
```
---

     
 
all -  [ Struggling with prompt management tools ](https://www.reddit.com/r/LangChain/comments/1ctk5l5/struggling_with_prompt_management_tools/) , 2024-05-18-0910
```
I’m working on a project for a client who needs single summaries of games for a game recommender app they’re creating. I
’ve been trying to test out a pipeline of prompts to see what inputs generate the best summaries, but I’m struggling 😓 


It’s easy to view and edit one prompt at a time, but I need a tool that can handle these more complex, chained prompt s
cenarios effectively. It feels like there are tools out there that could potentially help, but none seem fully integrate
d into a seamless prompt management workflow. I want to look across multiple sample output examples (from several sample
 inputs), and see what’s working and what’s not. 

Anyone else facing the same struggles? How are you managing more comp
lex prompt scenarios / how are you integrating multiple tools to get the job done? 

Maybe it's just part of the job, bu
t I can't help but think there's got to be a better way to manage and streamline this whole process. Any insights or tip
s would be super helpful! 


```
---

     
 
all -  [ Optimizing AI Data Processing with MinIO Weaviate and Langchain in Retrieval Augmented Generation (R ](https://www.reddit.com/r/minio/comments/1ctiw1l/optimizing_ai_data_processing_with_minio_weaviate/) , 2024-05-18-0910
```
In this article, we will delve into the integration of MinIO with Retrieval-Augmented Generation (RAG) pipelines and Wea
viate vector storage, using LangChain.

[https://blog.min.io/optimizing-ai-data-processing-with-minio-weaviate-and-langc
hain-in-retrieval-augmented-generation-rag-pipelines/](https://blog.min.io/optimizing-ai-data-processing-with-minio-weav
iate-and-langchain-in-retrieval-augmented-generation-rag-pipelines/)
```
---

     
 
all -  [ Agents working in parallel with LangGraph ](https://www.reddit.com/r/LangChain/comments/1cthrqz/agents_working_in_parallel_with_langgraph/) , 2024-05-18-0910
```
I’m trying to figure out if it’s possible to create a Multi Agent application with LangGraph, where the agents can work 
in parallel (if needed).

Let’s say I have three agents (stupid example):
1. Supervisor
2. Agent specialized in tech con
ferences
3. Agent specialized in medical conferences

Each agent has its own tools.

The user query is “What are the mai
n tech conferences and medical conferences in San Francisco in November?”.

This query can be obviously split in two dif
ferent questions and each one can be addressed separately: 
1. What are the main tech conferences in San Francisco in No
vember?
2. What are the main medical conferences in San Francisco in November?

The Supervisor is able to process the or
iginal query, to produce these two questions and to route them separately to the correct Agent.

Is there a way to run t
hese two agents in parallel and to have a fourth Agent (or the supervisor itself) that waits for the two answers and put
s all together to produce a single final answer?

Does anyone have experience with such a use case?
```
---

     
 
all -  [ LangChain vs LlamaIndex  ](https://www.reddit.com/r/AI_Agents/comments/1cth187/langchain_vs_llamaindex/) , 2024-05-18-0910
```
Checkout this short video to understand the difference between two major Generative AI packages i.e. LangChain and Llama
Index and what to use when : https://youtu.be/Oy8UZp3potw?si=9mp9M5UrBjR-FX5G
```
---

     
 
all -  [ Sending multiple prompts in parallel to OpenAI  ](https://www.reddit.com/r/LangChain/comments/1ctgq91/sending_multiple_prompts_in_parallel_to_openai/) , 2024-05-18-0910
```
Is there any way in LangChain where we can get the responses for multiple queries/prompts in LangChain?

Suppose I have 
a function in python:
```python
def function(...):
    prompt_1 = '...'
    prompt_2 = '...'
    
    # make these API c
alls in parallel - use multithreading?
    response_1 = llm.invoke(prompt_1)
    reponse_2 = llm.invoke(prompt_2)

    #
 rest of the code
```
```
---

     
 
all -  [ Career outside large vision and language models ](https://www.reddit.com/r/computervision/comments/1ctg46t/career_outside_large_vision_and_language_models/) , 2024-05-18-0910
```
Hi everyone,
I've done computer vision in industry for 8+ years. I worked on tabular data a bit and then changed jobs. T
he wave of ChatGPT had just started after my switch and soon, gpt4 vision followed suit.

I like building models or at l
east fine tuning them. I don't like calling APIs even though gpt4 vision is fantastic for the use cases my company works
 on.

Having said that, are there other areas in computer vision that haven't been penetrated by LLMs or LVMs yet? What'
s the status of 3D computer vision these days? I've just started studying some basic projective geometry stuff from the 
book Multiple view geometry but I'm wondering if this is all worth it. My interest in generative AI is the theory (and i
mplementation) of generative deep learning algorithms and methods (GANs, Flows, Diffusion models) but not using langchai
n, openai api etc for building RAG or agentic applications. 

Note : Self driving cars seems like a big application area
 but unfortunately, India may don't see them for a really long time.

I wanna know where computer vision is growing and 
what are some potentially interesting areas that our outside the current llm and lvm waves.

Thanks,
```
---

     
 
all -  [ AI Agents ](https://www.reddit.com/r/LangChain/comments/1ctfepy/ai_agents/) , 2024-05-18-0910
```
Hi folks, it seems to me that the current sentiment around AI agents is very negative as in that they're useless but I d
on't quite understand why. Could anybody explain to me why this view persists?
```
---

     
 
all -  [ How to deploy LangChain applications on AWS ](https://www.reddit.com/r/devops/comments/1ctel5e/how_to_deploy_langchain_applications_on_aws/) , 2024-05-18-0910
```
Deploying LangChain applications can be complex due to the need for various cloud services. This article explores the ch
allenges developers face when deploying with AWS CDK or the AWS console, and introduces Pluto, a tool that enables devel
opers to focus on writing business logic rather than getting bogged down in tedious configuration tasks.

https://pluto-
lang.vercel.app/blogs/240515-develop-ai-app-in-new-paradigm
```
---

     
 
all -  [ How to effectively chunk csv and xlsx files? Excel file can contain text/tables. ](https://www.reddit.com/r/LangChain/comments/1ct97ix/how_to_effectively_chunk_csv_and_xlsx_files_excel/) , 2024-05-18-0910
```
I'm looking for ways to effectively chunk csv/excel files. In a meaningful manner. I looked into loaders but they have u
nstructuredCSV/Excel Loaders which are nothing but from Unstructured. Is there something in Langchain that I can use to 
chunk these formats meaningfully for my RAG?
```
---

     
 
all -  [ Tool to compare LLM Outputs ](https://www.reddit.com/r/LLMDevs/comments/1ct8f3j/tool_to_compare_llm_outputs/) , 2024-05-18-0910
```
Is there a tool which lets users compare outputs from multiple LLM's based off a single prompt? I imagine with LangChain
 someone can build this locally but wonder if any such products are out there?

Tired of copy pasting the same input acr
oss GPT, Claude, Bard & Perplexity to triangulate answers & check accuracy

Tool to compare LLM Outputs

Is there a tool
 which lets users compare outputs from multiple LLM's based off a single prompt? I imagine with LangChain someone can bu
ild this locally but wonder if any such products are out there?

Tired of copy pasting the same input across GPT, Claude
, Bard & Perplexity to triangulate answers & check accuracy
```
---

     
 
all -  [ AI Developments in Financial Services, Social Media, and Healthcare: A Weekly Digest ](https://www.reddit.com/r/ai_news_by_ai/comments/1ct623n/ai_developments_in_financial_services_social/) , 2024-05-18-0910
```





#hardware #event #startups #tool #opinions #release #feature #update #vc #opensource #bigtech #api #leaders #scienc
e #major_players #scheduled

NVIDIA is hosting AI sessions at Money20/20 Europe, focusing on AI in financial services. T
he event will feature speakers from Mastercard, Stripe, Barclays, and others, and will cover topics such as generative A
I, fraud detection, and the impact of AI on the banking customer experience. BNY Mellon has deployed an NVIDIA DGX Super
POD™ with DGX™ H100 systems, and the event will also discuss trends, challenges, and opportunities in AI for financial s
ervices in 2024 [1].







Mike Krieger, co-founder of Instagram, has joined Anthropic as the Chief Product Officer. Hi
s expertise in building and scaling innovative products will help Anthropic expand its suite of enterprise applications 
and bring Claude to a wider audience [2].







Cohere, a company dedicated to scaling intelligence to serve humanity, 
is actively hiring. The company offers various benefits to employees, including RRSP contributions, health coverage, men
tal health support, remote work culture, generous time off, and support for new parents [3]. Cohere has also been featur
ed in CNBC's Disruptor 50 list for the second consecutive year, reflecting its commitment to providing practical AI solu
tions that tackle real-world business challenges [4].







Andrew Ng has announced a new short course on Multi AI Agen
t Systems with crewAI. The course focuses on breaking down complex tasks into subtasks for multiple AI agents to execute
 specialized roles [5]. Groq Inc has launched a new series called GroqThoughts, with the first feature focusing on how A
thena Intelligence and Groq collaborate to enable real-time use cases [6]. Groq Inc is also hosting a virtual hackathon 
for developers to showcase their projects built on Groq technology [9].







Langtrace AI conducted a performance anal
ysis comparing the latencies of different language models, including Groq running Llama-3. Groq demonstrated the lowest 
latencies across all tests, making it the ideal choice for applications where speed is essential [11].







LanceDB, a
n open-source database for AI, has secured $8 million in seed funding. The company aims to empower AI teams to search ov
er billions of vectors, process petabytes of images, and train on trillions of tokens [12]. HiPythagora, a Y Combinator 
W24 startup, has developed Pythagora, an open-source development tool that can build entire applications from scratch by
 interacting with users [13].







Google has introduced new generative media models and tools, including Veo for vide
o generation and Imagen 3 for image generation. They have also collaborated with filmmakers and musicians to showcase th
e capabilities of their AI technologies [15]. Google is also enhancing the Gemini app to be more multimodal, agentive, a
nd intelligent, serving as a personal AI assistant capable of handling complex tasks and taking actions on behalf of use
rs [16].







NVIDIA and LangChain are hosting a Generative AI Agents Developer Contest where participants can develop
 text and multimodal agents using their technologies [21]. NVIDIA AI Developer shared about the implementation of single
-view 3D tracking in NVIDIA DeepStream to enhance object tracking accuracy [23].







Yann LeCun emphasizes the import
ance of open source AI platforms for a vibrant ecosystem and to maximize the benefits of AI for society [26]. Greg Brock
man acknowledges the team effort behind GPT-4 and gives credit to Pranav Dhar for leading the development of the omni mo
del in collaboration with various teams at OpenAI over the past 18 months [27].







Google AI has announced Illuminat
e at Google IO, a tool that uses AI to convert research papers into audio conversations to enhance learning experiences 
[32]. Google AI has also introduced Med-Gemini, a new family of AI research models for medicine that builds on Gemini's 
advanced capabilities. The models have achieved state-of-the-art performance on various benchmarks and have unlocked nov
el applications in the medical domain [35].




[1. NVIDIA AI @NVIDIAAI https://twitter.com/NVIDIAAI/status/179060805072
7845980](https://twitter.com/NVIDIAAI/status/1790608050727845980)

[2. Anthropic @anthropicai https://twitter.com/anthro
picai/status/1790744375418589227](https://twitter.com/anthropicai/status/1790744375418589227)

[3. cohere @cohere https:
//twitter.com/cohere/status/1790745447327268938](https://twitter.com/cohere/status/1790745447327268938)

[4. cohere @coh
ere https://twitter.com/cohere/status/1790745445465039092](https://twitter.com/cohere/status/1790745445465039092)

[5. A
ndrew Ng @AndrewYNg https://twitter.com/AndrewYNg/status/1790769732146307308](https://twitter.com/AndrewYNg/status/17907
69732146307308)

[6. Groq Inc @GroqInc https://twitter.com/GroqInc/status/1790734880235495512](https://twitter.com/GroqI
nc/status/1790734880235495512)

[7. Groq Inc @GroqInc https://twitter.com/GroqInc/status/1790774240574116203](https://tw
itter.com/GroqInc/status/1790774240574116203)

[8. Groq Inc @GroqInc https://twitter.com/GroqInc/status/1790783354960515
427](https://twitter.com/GroqInc/status/1790783354960515427)

[9. Groq Inc @GroqInc https://twitter.com/GroqInc/status/1
790794933143802365](https://twitter.com/GroqInc/status/1790794933143802365)

[10. Groq Inc @GroqInc https://twitter.com/
GroqInc/status/1790806854009798891](https://twitter.com/GroqInc/status/1790806854009798891)

[11. Groq Inc @GroqInc http
s://twitter.com/GroqInc/status/1790851920992616504](https://twitter.com/GroqInc/status/1790851920992616504)

[12. Y Comb
inator @ycombinator https://twitter.com/ycombinator/status/1790776813578584553](https://twitter.com/ycombinator/status/1
790776813578584553)

[13. Y Combinator @ycombinator https://twitter.com/ycombinator/status/1790808894207574051](https://
twitter.com/ycombinator/status/1790808894207574051)

[14. Y Combinator @ycombinator https://twitter.com/ycombinator/stat
us/1790838165550563816](https://twitter.com/ycombinator/status/1790838165550563816)

[15. Google @google https://twitter
.com/google/status/1790763743556632868](https://twitter.com/google/status/1790763743556632868)

[16. Google @google http
s://twitter.com/google/status/1790809723840651398](https://twitter.com/google/status/1790809723840651398)

[17. Google @
google https://twitter.com/google/status/1790855212950753605](https://twitter.com/google/status/1790855212950753605)

[1
8. Sam Altman @sama https://twitter.com/sama/status/1790816449180876804](https://twitter.com/sama/status/179081644918087
6804)

[19. Sam Altman @sama https://twitter.com/sama/status/1790817315069771959](https://twitter.com/sama/status/179081
7315069771959)

[20. Sequoia Capital @sequoia https://twitter.com/sequoia/status/1790821953969996131](https://twitter.co
m/sequoia/status/1790821953969996131)

[21. NVIDIA AI Developer @NVIDIAAIDev https://twitter.com/NVIDIAAIDev/status/1790
796553566716132](https://twitter.com/NVIDIAAIDev/status/1790796553566716132)

[22. NVIDIA AI Developer @NVIDIAAIDev http
s://twitter.com/NVIDIAAIDev/status/1790834544356040810](https://twitter.com/NVIDIAAIDev/status/1790834544356040810)

[23
. NVIDIA AI Developer @NVIDIAAIDev https://twitter.com/NVIDIAAIDev/status/1790849638418841919](https://twitter.com/NVIDI
AAIDev/status/1790849638418841919)

[24. Yann LeCun @ylecun https://twitter.com/ylecun/status/1790708256127545804](https
://twitter.com/ylecun/status/1790708256127545804)

[25. Yann LeCun @ylecun https://twitter.com/ylecun/status/17908393895
69880330](https://twitter.com/ylecun/status/1790839389569880330)

[26. Yann LeCun @ylecun https://twitter.com/ylecun/sta
tus/1790895062148137470](https://twitter.com/ylecun/status/1790895062148137470)

[27. Greg Brockman @gdb https://twitter
.com/gdb/status/1790839201312731462](https://twitter.com/gdb/status/1790839201312731462)

[28. Greg Brockman @gdb https:
//twitter.com/gdb/status/1790869434174746805](https://twitter.com/gdb/status/1790869434174746805)

[29. a16z @a16z https
://twitter.com/a16z/status/1790856759504244953](https://twitter.com/a16z/status/1790856759504244953)

[30. a16z @a16z ht
tps://twitter.com/a16z/status/1790856761169297598](https://twitter.com/a16z/status/1790856761169297598)

[31. a16z @a16z
 https://twitter.com/a16z/status/1790895186228420880](https://twitter.com/a16z/status/1790895186228420880)

[32. Google 
AI @googleai https://twitter.com/googleai/status/1790806911937560938](https://twitter.com/googleai/status/17908069119375
60938)

[33. Google AI @googleai https://twitter.com/googleai/status/1790811954329624853](https://twitter.com/googleai/s
tatus/1790811954329624853)

[34. Google AI @googleai https://twitter.com/googleai/status/1790872932681699764](https://tw
itter.com/googleai/status/1790872932681699764)

[35. Google AI @googleai https://twitter.com/googleai/status/17908783224
66922499](https://twitter.com/googleai/status/1790878322466922499)

[36. Google AI @googleai https://twitter.com/googlea
i/status/1790878324845076790](https://twitter.com/googleai/status/1790878324845076790)

[37. Google AI @googleai https:/
/twitter.com/googleai/status/1790878326967468045](https://twitter.com/googleai/status/1790878326967468045)

[38. Google 
AI @googleai https://twitter.com/googleai/status/1790878329395937773](https://twitter.com/googleai/status/17908783293959
37773)
```
---

     
 
all -  [ Experiment and test the reliability of different LLMs in prod and pre-prod! ](https://www.reddit.com/r/LangChain/comments/1ct4m4z/experiment_and_test_the_reliability_of_different/) , 2024-05-18-0910
```
**TLDR: I made a platform to make it easy to switch between LLMs, find the best one for your specific needs, analyze the
ir performance, and test different providers in production. Check it out at** [**optimix.app**](https://optimix.app/?lan
g)

Figuring out whether or not you should switch to Llama 3, Gemini 1.5 Flash, or GPT-4o can be hard. And knowing if th
e prompt change you just made will be good or bad is even harder.

A key focus of Optimix is to make experimentation eas
y. You can run A/B tests and other experiments to figure out how your changes impacted your core metrics like cost, spee
d, and user satisfaction. You can also test and compare different models in our playground and make requests through our
 API.

It also dynamically selects the most suitable model for each request, and helps manage fallbacks for outages and 
rate limits. Facing an OpenAI outage? Switch to Llama 3. Need superior coding assistance? We can auto switch you to the 
best one.

I'd love any feedback or suggestions on the platform, and hope this can be helpful for you all with all the n
ew models coming out!
```
---

     
 
all -  [ Can I use LangChain to only give me the context is found from the retrieval? ](https://www.reddit.com/r/LangChain/comments/1csy9ul/can_i_use_langchain_to_only_give_me_the_context/) , 2024-05-18-0910
```
I'm building an app with Next.js. 

Is it possible to have LangChain only give me the context it found from the vector s
tore? I then want to take this context and manually insert it into another part of my app that's using an llm as a part 
of the message history (but I don't want to do this final step in LangChain)

So I don't want LangChain to give me the f
inal output just the context is found using the vector store and OpenAi embedding model.

I'm still learning sry if this
 a stupid question. 

I'm having issues streaming output from LangChain to the front end and want to use something else 
I already have setup
```
---

     
 
all -  [ Any example of using llm.bind_tool ? i get not implemented error - want to run tools w GPT-4o ](https://www.reddit.com/r/LangChain/comments/1csvh8w/any_example_of_using_llmbind_tool_i_get_not/) , 2024-05-18-0910
```
Thanks
```
---

     
 
all -  [ How can I use LangChainJs to fill out csv file according to big context and prompt? ](https://www.reddit.com/r/LangChain/comments/1csts7q/how_can_i_use_langchainjs_to_fill_out_csv_file/) , 2024-05-18-0910
```
I am currently working on a project where I need to fill documents (CSV files) according to requirements in a big compen
dium (800+ pages PDF).

for example:

* context:
   * the PDF compendium of 800 pages with instructions and detailed leg
al requirements to be met when implementing infrastructure projects in IT sector
* CSV file:
   * a checklist-style CSV 
file containing the short name of the subject from the PDF compendium and columns to input things to be checked and proc
essed by a person (or in this case: AI)

|Subject|Responsible|Price|Risks|
|:-|:-|:-|:-|
|A.1.1.|Author of this file|$20
.000|If not done, we are doomed|

* Prompt
   * 'I want to add a exchange a router in Building C3.'
   * 'I want to add 
a gitlab server to our network'

In both cases, the output should be a CSV file or CSV text .

**These are the models im
 using (and liking):**

* model: wizardlm2:7b
* embedding model: mxbai-embed-large

**What I have done so far**

* readi
ng in the pdf files
* embedding the pdf files
* reading in the csv file
* embedding the csv file (<- is this correct?)
*
 created a prompt

\`\`\`  
Fill the csv file in the context with valuable data found in the embeddings according to the
 question.

Do not guess, do not add anything. Use only the context.

{context}

Question: {input}

\`\`\`

**What is no
t working. AKA: What is my question?**

The output the model is giving me is unstructured and has nothing to do with the
 CSV file I put into the context.

Is there a way that I can make the AI

1. Read in PDFs
2. Read in CSV
3. Listen to th
e prompt
4. Output a CSV file or (- like text)  I gave it with data from the embedded PDFs correctly according to the ne
eds arising from the input prompt

?
```
---

     
 
MachineLearning -  [ [R] Building an Observable arXiv RAG Chatbot with LangChain, Chainlit, and Literal AI ](https://www.reddit.com/r/MachineLearning/comments/1crwh0q/r_building_an_observable_arxiv_rag_chatbot_with/) , 2024-05-18-0910
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

     
 
MachineLearning -  [ [P] LLMinator: A Llama.cpp + Gradio based opensource Chatbot to run llms locally(cpu/cuda) directly  ](https://www.reddit.com/r/MachineLearning/comments/1cpbgd1/p_llminator_a_llamacpp_gradio_based_opensource/) , 2024-05-18-0910
```
Hi I am currently working on a context-aware streaming chatbot based on Llama.cpp, Gradio, Langchain, Transformers. LLMi
nator can pull LLMs directly from HF & run them locally on cuda or cpu.

I am looking for recommendations & help from op
ensource community to grow this further.

**Github Repo:** [https://github.com/Aesthisia/LLMinator](https://github.com/A
esthisia/LLMinator)

**Goal:** To help developers with kickstarter code/tool to run LLMs.

https://preview.redd.it/fnzja
7rjwqzc1.png?width=1846&format=png&auto=webp&s=a62c43614d63e82156fef8722b986b051cc1795b

**Features:**

* Context-aware 
Chatbot.
* Inbuilt code syntax highlighting.
* Load any LLM repo directly from HuggingFace.
* Supports both CPU & Cuda m
odes.
* Load & Offload saved models.
* Command Line Args
* API Access(Soon to be available)

Any review or feedback is a
ppreciated.
```
---

     
 
MachineLearning -  [ [D] Self-optimizing deterministic LLM memory using dspy, neo4j and vector databases. Need your input ](https://www.reddit.com/r/MachineLearning/comments/1cakjaf/d_selfoptimizing_deterministic_llm_memory_using/) , 2024-05-18-0910
```
Hey there, Redditors!

I'm back with the latest installment on creating deterministic LLM memory.

If you've been follow
ing along, you know I'm on a mission to move beyond the '[thin OpenAI wrapper](https://topoteretes.github.io/cognee/blog
/2023/10/05/going-beyond-langchain--weaviate-and-towards-a-production-ready-modern-data-platform/)' trend and tackle the
 challenges of building robust LLM memory.

  
That's why we built cognee, a python library to process documents and bui
ld knowledge graphs on top of them.

After a few weeks of work, we integrated DSPy and extended cognee.

Here is brief o
verview of the logic: 

[Architecture overview](https://preview.redd.it/fcs3lifx53wc1.png?width=1380&format=png&auto=web
p&s=9316cba52147a5b764565b8438f3f143d8e7ac84)

We aim to understand:

1. Have you tried building knowledge graphs with o
ther tools before?

2. If so, what were the biggest obstacles?

3. How would you approach semantic linking of documents 
without knowledge graphs?

*Remember to give this post an upvote if you found it insightful!*  
*And also star our* [Git
hub repo](https://github.com/topoteretes/cognee)
```
---

     
 
deeplearning -  [ Seeking Advice: Solving Data Challenges with Large Language Models (LLMs) ](https://www.reddit.com/r/deeplearning/comments/1ca4nc1/seeking_advice_solving_data_challenges_with_large/) , 2024-05-18-0910
```
Hi all

I am presented with a problem that I need to solve using LLM to get the right data from text that has only \~20%
 structure to it. Here's a sample data

XXXXX

AA          BB

CCCC:  (optional DDDD)

C1......(A1) (B1)

C2......(A2) (
B2)

C3.....(A3) (B3)

I am required to anwer with either of these results from A1/B1 till A3/B3 pairs but in order to d
o that I need to go back and ask the user which one of the options C1 to C3 applies to him?

The above is not the most c
omplex structure, it increases in complexity from here so a lot of chatting with user is required to get to the right da
ta that will always exist in the chunk like above.

In the most simplist case the data structure will look like below

X
XXXX

AA          BB

CCCC: ......(A1) (B1)



How would you build a system like this? I am looking at multi-agent syste
ms with Langchain, what about prompt chaining?
```
---

     
 
deeplearning -  [ Share the Coolest Out of The Box LLM Applications That Made You Say 'Wow that was smart' ](https://www.reddit.com/r/deeplearning/comments/1c9e6dj/share_the_coolest_out_of_the_box_llm_applications/) , 2024-05-18-0910
```
Hi, I'm looking at some LLM applications today but apart from guys doing big rags with langchain I don't see too many us
es that are out of the box or that make me say 'wow that was smart to use an LLM here'. Have you seen any cool stuff usi
ng LLMs recently that made you say 'wow, that was smart'?
```
---

     
