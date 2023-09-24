 
all -  [ Resume review for Data Science and Machine Learning roles ](https://www.reddit.com/r/resumes/comments/16qgj6m/resume_review_for_data_science_and_machine/) , 2023-09-24-0910
```
Hi, I am a recent grad with a Masters in ECE. I have applied for more than 1000 positions and received less than 10 inte
rviews so far. For most of the positions, I just receive a recruiter call. There was this one position that I received a
 verbal offer but they declined it afterwards. Also, I am applying for jobs in both the US and Canada as I am a Canadian
 Permanent Resident. I keep my address of the respective country where the job is based and I don't include the line Can
adian Permanent Resident for US roles. I need some advice, what can I change in the resume to improve my chances to land
 more interviews.  
Thanks in Advance

https://preview.redd.it/t0gis7nav2qb1.png?width=1338&format=png&auto=webp&s=40b10
52baddf8c4692e5bb67b0fde8d61f839971
```
---

     
 
all -  [ We're building a cloud for AI agents & AI apps, It's free and we're gradually open-sourcing the infr ](https://github.com/e2b-dev/e2b) , 2023-09-24-0910
```

```
---

     
 
all -  [ Found a great beginner LangChain Tutorial and generated an article about it! Check it out. ](https://www.reddit.com/r/LangChain/comments/16qau85/found_a_great_beginner_langchain_tutorial_and/) , 2023-09-24-0910
```
I found this great tutorial on LangChain that helped me generate an a title to an outline to an article in a python scri
pt.

What do you think of it? Do you have other tutorials you can recommend that helped you learn?

[https://www.learnin
ternetgrow.com/guide-to-langchain-chains-and-applications/](https://www.learninternetgrow.com/guide-to-langchain-chains-
and-applications/)
```
---

     
 
all -  [ Found a great beginner LangChain Tutorial and generated an article about it! Check it out. ](https://www.reddit.com/r/pythontips/comments/16qat7v/found_a_great_beginner_langchain_tutorial_and/) , 2023-09-24-0910
```
I found this great tutorial on LangChain that helped me generate an a title to an outline to an article in a python scri
pt.  
What do you think of it? Do you have other tutorials you can recommend that helped you learn?  
https://www.learni
nternetgrow.com/guide-to-langchain-chains-and-applications/
```
---

     
 
all -  [ Embedding with Llama-cpp seems to have issues ](https://www.reddit.com/r/LangChain/comments/16q9b5b/embedding_with_llamacpp_seems_to_have_issues/) , 2023-09-24-0910
```
    from langchain.document_loaders import WebBaseLoader
    from langchain.embeddings import LlamaCppEmbeddings
    fro
m langchain.vectorstores import Chroma
    
    llama = LlamaCppEmbeddings(model_path='../models/openorca_stx.gguf')
   
 
    loader = WebBaseLoader('https://www.bbc.com/')
    pages = loader.load()
    
    vectordb = Chroma.from_documents
(
        documents=pages,
        embedding=llama,
        persist_directory='../data/vectorstores/'
    )

&#x200B;

d
epending on the page i want to load i get this error:

&#x200B;

&#x200B;

    ValueError                               
 Traceback (most recent call last)
    p:\git_repos\langchain-test\src_langchain\04_vectorstore.ipynb Cell 4 line 5
    
      1 from langchain.vectorstores import Chroma
          3 persist_directory = '../data/vectorstores/'
    ----> 5 ve
ctordb = Chroma.from_documents(
          6     documents=pages,
          7     embedding=llama,
          8     persis
t_directory=persist_directory
          9 )
    
    File d:\miniconda3\envs\langchain\Lib\site-packages\langchain\vecto
rstores\chroma.py:646, in Chroma.from_documents(cls, documents, embedding, ids, collection_name, persist_directory, clie
nt_settings, client, collection_metadata, **kwargs)
        644 texts = [doc.page_content for doc in documents]
        
645 metadatas = [doc.metadata for doc in documents]
    --> 646 return cls.from_texts(
        647     texts=texts,
    
    648     embedding=embedding,
        649     metadatas=metadatas,
        650     ids=ids,
        651     collectio
n_name=collection_name,
        652     persist_directory=persist_directory,
        653     client_settings=client_sett
ings,
        654     client=client,
        655     collection_metadata=collection_metadata,
        656     **kwargs,

    ...
    --> 510 self.input_ids[self.n_tokens : self.n_tokens + n_tokens] = batch
        511 # Save logits
        5
12 rows = n_tokens if self.params.logits_all else 1
    
    ValueError: could not broadcast input array from shape (8,)
 into shape (0,)

[example.org](https://example.org) works fine, anything more complex throws this error message.I reall
y hope to use llama-cpp. GPT4ALL Models are outdated.
```
---

     
 
all -  [ Is LangChain the right choice for what Im Creating? ](https://www.reddit.com/r/LangChain/comments/16q7dbp/is_langchain_the_right_choice_for_what_im_creating/) , 2023-09-24-0910
```
I'm interested in being able to prompt an AI model that can reference and pull data  from custom databases tailored to s
pecific interests. For instance, if one  user is interested in books, the AI would generate info based on a  database of
 book titles and authors. Meanwhile, another user interested  in cars would get info generated from a database of car mo
dels and  specs. Essentially, the AI should be able to dynamically switch between  different databases based on user pre
ferences. Has anyone had experience  integrating such a system with Bubble or can recommend a  solution/platform that al
lows for this kind of interest specific integration? Any Thoughts would be helpful!
```
---

     
 
all -  [ Running LLaMa on Google Colab/cloud differences w.r.t local system ](https://www.reddit.com/r/LocalLLaMA/comments/16q0fhc/running_llama_on_google_colabcloud_differences/) , 2023-09-24-0910
```
So I have downloaded the quantized LLaMa 7B model from huggingface which I can run on my local system (but takes a long 
time). The way I am doing it is, I have the model in one of my folders and I am calling the model from there using the l
angchain module in Python.

I tried to do the same thing on Colab where I mounted my Google Drive, copied the model from
 Google Drive to Google Colab and changed the location of model from my local drive to the filepath of bin file in Colab
.

But then I keep getting error:

    ---------------------------------------------------------------------------
    A
ssertionError                            Traceback (most recent call last)
    <ipython-input-28-02e71e2eb370> in <cell 
line: 5>()
          3 # llm = LlamaCpp(model_path = '/content/gdrive/MyDrive/OpenLLM/LLaMa_7B/llama-7b.ggmlv3.q3_K_M.bi
n')
          4 
    ----> 5 llm = Llama(model_path = '/content/gdrive/MyDrive/OpenLLM/Alpaca_7B/ggml-alpaca-7b-q4.bin')

          6 
          7 # embeddings = LlamaCppEmbeddings(model_path = llama_model_path + 'llama-7b.ggmlv3.q3_K_M.bin'
)
    
    /usr/local/lib/python3.10/dist-packages/llama_cpp/llama.py in __init__(self, model_path, seed, n_ctx, n_batch
, n_gpu_layers, main_gpu, tensor_split, rope_freq_base, rope_freq_scale, low_vram, mul_mat_q, f16_kv, logits_all, vocab_
only, use_mmap, use_mlock, embedding, n_threads, last_n_tokens_size, lora_base, lora_path, numa, verbose, **kwargs)
    
    338                     self.model_path.encode('utf-8'), self.params
        339                 )
    --> 340      
   assert self.model is not None
        341 
        342         if verbose:
    
    AssertionError: 

So I wanted to 
know what are some of the nuances which I need to keep in mind while running on local system vs. Google Colab or cloud l
ike AWS, Azure etc. Is it not possible to place the model in a bucket/folder on cloud and then call it like on local sys
tem?

I am fairly new to open source LLMs and giving it a try for the first time. I have worked with openAI APIs for Cha
tGPT but that doesn't include all these additional things and I want to expand my knowledge on the same.

Thanks in adva
nce.
```
---

     
 
all -  [ Open-Source LLM-Based Text Analysis and Observability Tools ](https://www.reddit.com/r/LangChain/comments/16pzw14/opensource_llmbased_text_analysis_and/) , 2023-09-24-0910
```
Hi,

&#x200B;

We have a chatbot that handles thousands of conversations daily. As our operations grow, we find ourselve
s constantly adding more monitoring and analytics. However, our approach has been somewhat scattered, lacking a unified 
'management platform.'

&#x200B;

For instance, we currently monitor basic metrics such as the ratio of positive to nega
tive sentiment in conversations, the number of conversations that end after fewer than 5 responses, and so on. But every
 time we introduce a new analytics metric, we manually apply it to all historical conversations for consistency.

&#x200
B;

Ideally, we are in search of an open-source library that:

&#x200B;

1. Offers prebuilt analytical tools for text-ba
sed conversations, including metrics like length, sentiment, the ability to identify failed conversations, and more.

2.
 Provides the capability to introduce new, custom metrics and analytics.

3. Incorporates an orchestration mechanism to 
ensure that both old and new conversations are subjected to the analytics established for the conversations in our datab
ase.

&#x200B;

If a platform or library meeting these criteria exists, we would greatly appreciate any recommendations.
 Our searches on Google and GitHub haven't produced meaningful results.

&#x200B;
```
---

     
 
all -  [ How to optimise costs in embedding models ? ](https://www.reddit.com/r/ChatGPTCoding/comments/16pyhjw/how_to_optimise_costs_in_embedding_models/) , 2023-09-24-0910
```
I am kinda a newbie to coding who is building a very simple telegram bot with the langchain embeddings that answers simp
le questions about economics based on books I uploaded, but the problem is that there is a high discrepancy between the 
given costs for default Adav2 and the real costs, as giving my bot 10 questions with the replies consumes 24 cents, whil
e on OpenAI’s API section of website it is written as 0.0001$ per 1000 token, which is roughly 750 words or so. Why can 
it happen and how can I fix it ? Big thanks in advance.
```
---

     
 
all -  [ Seeking Advice on Local AI Model for Analyzing Personal Files ](https://www.reddit.com/r/LangChain/comments/16pv5iq/seeking_advice_on_local_ai_model_for_analyzing/) , 2023-09-24-0910
```
 Hello everyone,

I'm embarking on a project to develop an application for personal use that can assist me in retrieving
 specific information from my files. I'd like to be able to ask questions like 'What was my income last year?' and get a
ccurate answers directly from my stored documents.

One of my primary concerns is privacy; I want to keep my data as sec
ure as possible. Therefore, I am interested in utilizing a local AI model that doesn't rely on cloud-based services. As 
I am relatively new to the world of AI, I'm looking for suggestions on which models would be most suitable for my needs.


After some preliminary research, I've come across Langchain, which seems to fit my requirements well. However, I'm ope
n to other suggestions too.

A potential complication is that my files are not in any specific format or structure; they
 range from PDFs and text files to PowerPoints and Excel spreadsheets. I can segregate them into separate folders if tha
t would be helpful. My question is, would restructuring my files into a specific format improve the accuracy of the AI m
odel giving me proper answer?

I'd appreciate any advice on the following:

1. What AI model would be best suited for my
 project?
2. Is Langchain a good choice for this type of task?
3. Would reformatting my files increase the model's accur
acy?  


My current hardware:  
RAM: DDR5 64GB  
GPU : 3090  
CPU I9 11TH

Thank you for your time and expertise!
```
---

     
 
all -  [ Implementing chain of thought vs using LangChain ](https://www.reddit.com/r/LangChain/comments/16pnd31/implementing_chain_of_thought_vs_using_langchain/) , 2023-09-24-0910
```
I assume a lot of you guys are familiar with the chain of thought reasoning and the idea of a thought graph. I am thinki
ng whether to use LangChain agents or to implement something myself. I already use LangChain in my open source projects,
 for prompt synthesis and for code generation:

[https://github.com/RoboCoachTechnologies/GPT-Synthesizer](https://githu
b.com/RoboCoachTechnologies/GPT-Synthesizer)

[https://github.com/RoboCoachTechnologies/ROScribe](https://github.com/Rob
oCoachTechnologies/ROScribe)

I probably stay with LangChain, but I am wondering if I lose flexibility or efficiency com
pared to implement something internally. What do you think?

Last but not least, I appreciate it if you guys look at our
 open source code and tell me what you think. There is some documentation and demos that you can watch to see what we do
. Maybe it helps your project too. I appreciate it if you kindly drop a star on our repos if you like it.

Cheers!
```
---

     
 
all -  [ What is the best way to generate Questions and their Answers based off a document? ](https://www.reddit.com/r/LangChain/comments/16pedn4/what_is_the_best_way_to_generate_questions_and/) , 2023-09-24-0910
```
Hello there, 

I am creating a quiz tool.   What is the best way to generate Questions and their Answers based of a supp
lied document?  

For example: Create a quiz (questions and answers) with the questions and answers all coming FROM the 
content of a text file / pdf or stored in a DB.  

So using the content from the document and the reasoning from the LLM
. 

Thank you
```
---

     
 
all -  [ Which approach would be better for embedding my documents? (Question about Vector Databases) ](https://www.reddit.com/r/LangChain/comments/16pedi1/which_approach_would_be_better_for_embedding_my/) , 2023-09-24-0910
```
Hi!

I would appreciate some help for my current situation.

At this moment, I want to do the following: I want to use C
hatGPT to generate a first answer in a customer portal, based in the internal documentation from the app the customers w
ill ask about.

The problem is that the document is 80 MB and it has 1629 pages. I've been reading about vector database
s about some services like Pinecone, Weaviate...

But it's still a little confusing. For my current situation, what woul
d be the best approach so I can embed the model with all the information with this pdf (Also, in the future we are addin
g more pdf documents which are also expected to have a big size)

Thank you.

Best regards,
Sergio
```
---

     
 
all -  [ is there a pdf version of the Langchain documentation? ](https://www.reddit.com/r/LangChain/comments/16pebr6/is_there_a_pdf_version_of_the_langchain/) , 2023-09-24-0910
```
Hi. I looked for a pdf button or some way to download the entire documentation but couldn't figure it out. Does anyone k
now how I can download the entire documentation as a pdf? I want to converse with the documentation through ChatGPT. Tha
nks.
```
---

     
 
all -  [ Tool to compare LLM Outputs ](https://www.reddit.com/r/LangChain/comments/16pd7p7/tool_to_compare_llm_outputs/) , 2023-09-24-0910
```
Is there a tool which lets users compare outputs from multiple LLM's based off a single prompt? I imagine with LangChain
 someone can build this locally but wonder if any such products are out there?  


Tired of copy pasting the same input 
across GPT, Claude, Bard & Perplexity to triangulate answers & check accuracy 
```
---

     
 
all -  [ Router, LLMChain, Agent and Tools ](https://www.reddit.com/r/LangChain/comments/16pb0tq/router_llmchain_agent_and_tools/) , 2023-09-24-0910
```
Looking for some guidance here to see if I am down the right path. 

I am looking use a Router that can initiate differe
nt chains and agents based on the inquiry that the user is inputting

&#x200B;

So far, It doesn't look like a router ca
n initiate agent? Am i right?

Also it doesn't look like chain can use tools? Am I right? I would like Chains and Agents
 to have tools. 

&#x200B;
```
---

     
 
all -  [ Langchainr vs. Llama Index ](https://www.reddit.com/r/OpenAI/comments/16pa4ss/langchainr_vs_llama_index/) , 2023-09-24-0910
```
Starting a new LLM application (chatbot/IR), which one do you suggest: Langchain or Llama Index? Why?
```
---

     
 
all -  [ Chat with your Networks: RAG on Network Logs ](https://www.reddit.com/r/LangChain/comments/16p6mnw/chat_with_your_networks_rag_on_network_logs/) , 2023-09-24-0910
```
Hi there,  
I'm working on Chat with your networks application. We have syslogs and SNMP logs available and we want to c
reate a chatbot that would answer different queries around those logs as well as help in resolving issues logged. Our cu
rrent approach is simply applying RAG to the network logs. As the retrieval cannot be done through similarity search, we
 parsed a few components of the logs out and set them as metadata for each log. We used SelfQueryingRetriever to query o
ver the metadata. This has sort-of worked but it is hardly the ideal approach. I'd like to know whats the best way to ap
proach this unique problem.

Any help is highly appreciated
```
---

     
 
all -  [ Swarm Community Call September! ](https://www.reddit.com/r/ethswarm/comments/16p3l62/swarm_community_call_september/) , 2023-09-24-0910
```
Join us on **28 September at 17:00 CET** on the Swarm Foundation **Discord** for our monthly call. 

[Swarm Community Ca
ll](https://preview.redd.it/ikwdv8q2brpb1.png?width=1920&format=png&auto=webp&s=ad7908427fcee7a2910e7e150ab942fc03865eba
)

Swarm's hardening phase is progressing fast and smoothly, bringing more utility to everyone implementing it in their 
solution, as Phases 3 and 4 of the storage incentives roadmap are drawing to a close. 

## What to expect:

* Core devel
opment updates (with Niki Papadatou and Esad Akar)
* JS ecosystem updates (with Noah Maizels)
* In focus: The price orac
le (with Callum Toner)
* Community talk: FaVe – presentation of a new suite of tools that enable secure semantic search 
and running private GPTs (Sabyasachi Patra and Tadej Fius)
* Community AMA & open space for debate – Ask a question [via
 this form](https://mautic.int.ethswarm.org/r/46d2bbb2efdfcad7515ddd1ba?ct=YTo1OntzOjY6InNvdXJjZSI7YToyOntpOjA7czo1OiJlb
WFpbCI7aToxO2k6Nzk7fXM6NToiZW1haWwiO2k6Nzk7czo0OiJzdGF0IjtzOjIyOiI2M2Y3M2ZlZDYyMGY0Njc0Njk5MDY4IjtzOjQ6ImxlYWQiO3M6NDoiO
DE5NyI7czo3OiJjaGFubmVsIjthOjE6e3M6NToiZW1haWwiO2k6Nzk7fX0%3D&)

## Core updates – 1.17.4 release

The next Bee release 
is on the horizon. Node operators can expect a series of modifications, including overlay mining option, default batch t
ype set to immutable, default upload type deferred and a refined logging process. This is part of the ongoing hardening 
phase, which will prepare the Swarm network for the eventual rollout of Phases 3 and 4. 

## The price oracle is coming


The fully decentralised price oracle is at the heart of the [storage incentives upgrade process](https://blog.ethswarm.
org/foundation/2022/towards-the-world-computer.-the-swarm-network-upgrade-has-started./). It will dynamically and in rea
l time set the price of storage in the Swarm network based on supply-demand. This month’s call will delve deeper into it
s design, purpose and the current state of development. 

## Community talk – FaVe

Sabyasachi Patra and Tadej Fius will
 present the latest contribution from Datafund to Fair Data Society and to the open source community –– **a new suite of
 tools** called FaVe. FaVe is **a fully decentralised** **open source vector database** that comes as the  cherry on top
 of fairOS (which provides doc store and key-value store), with LangChain integration and standalone python client. It *
*enables a secure semantic search** on your documents and allows you to run **private GPT**s with data on Swarm.

## Com
munity AMA 

If you have any questions about Swarm, join the live conversation in the “[stage-chat](https://discord.gg/B
jBMNaFC4x)” channel, request to speak in the “[stage](https://discord.gg/pynFnHjbAP)” channel or send them [via this for
m](https://airtable.com/shrBRyrMkXFsJvLS3).

## New to Swarm Foundation Discord?   

## Here’s how to join the call: 

[
Click here](https://discord.com/channels/799027393297514537/801438093927776286) to join Swarm Foundation Discord, then: 


* Use the “[stage](https://discord.gg/pynFnHjbAP)” channel to listen to the call.

Use the “[stage-chat](https://disco
rd.gg/BjBMNaFC4x)” channel to ask questions and talk to other participants
```
---

     
 
all -  [ Thesis Project Help Using SageMaker Free Tier ](https://www.reddit.com/r/aws/comments/16p2sze/thesis_project_help_using_sagemaker_free_tier/) , 2023-09-24-0910
```
Hi, so I am a college student and I will be starting my big project soon to graduate. Basically, I have a csv dataset of
 local short stories. Per row, it has the following columns: (1) title of the short story (2) basically the whole plot (
3) Author (4) Date made. I want to create an end to end project so that I have a web app (maybe deployed on vercel or so
mething) that I will code using React, and I can type into the search bar something like 'What is the story about the bl
onde girl that found a bear family's house' and the UI should show a list of results. The results list page shows the po
ssible stories, and then the top story should be Goldilocks (for example) but it should also show other stories with eit
her a blonde girl, or with bears. Then when I click the Goldilocks result, the UI should show all the info in the csv ro
w of the Goldilocks, like the title then the story plot, then the author and when was it published.  


I need to use AW
S Sagemaker (required, can't use easier services) and my adviser gave me this document to start with: [https://github.co
m/aws/amazon-sagemaker-examples/blob/main/introduction\_to\_amazon\_algorithms/jumpstart-foundation-models/question\_ans
wering\_retrieval\_augmented\_generation/question\_answering\_langchain\_jumpstart.ipynb](https://github.com/aws/amazon-
sagemaker-examples/blob/main/introduction_to_amazon_algorithms/jumpstart-foundation-models/question_answering_retrieval_
augmented_generation/question_answering_langchain_jumpstart.ipynb)  


I was already able to actually train the model an
d make it to Step 5, where I post a query and I get the answer I want. My question is, how to deploy it? I was thinking 
I will need to somehow containerize AWS Sagemaker notebook into an API that takes in a query and outputs a nested json c
ontaining all the result stories plus their relevance score. The story with the highest relevance score is the one at th
e very top of the results page. My problem is, I don't know where to start? I have a similar app coded with React that c
alls a local API running using elasticsearch in Springboot. This springboot outputs a nested json of the list of results
 with their scores everytime a query is made. I can't use that though. Basically I will need to create the elasticsearch
 function from scratch hopefully using the AWS Sagemaker, deploy it as an API that outputs a nested json, use the API in
 React UI, and deploy the UI in vercel. And no, I can't use pre-made APIs, I need to create it from scratch.  


Can som
eone give me a step by step instruction how to make the AWS Sagemaker into an API that outputs a nested json? Hopefully 
using free tier services. I was able to use a free-tier instance to train my model in the notebook. Please be kind, I'm 
learning as I go. Thanks!
```
---

     
 
all -  [ Chatbot Using Langchain Agents and Llama 2 ](https://www.reddit.com/r/LangChain/comments/16p2nas/chatbot_using_langchain_agents_and_llama_2/) , 2023-09-24-0910
```
Hi guys, recently I  have build a chatbot using Langchian and Open AI LLM model (gpt 3.5 16 k). This chatbot resides on 
a tabular data (we used create\_pandas\_dataframe) to query data for users .  But our organization wants us to use open 
source LLM model (Llama 2 70 B).  Just wanted suggestions check 2 things:  


1) Have anyone tried Llama2 (GPU/CPU) with
 Langchain pandas/conversational agents and see if results are promising or not.

2) What are the GPU requirements to ru
n Llama2 70 B, that I can request my organisation?  


TIA
```
---

     
 
all -  [ Langchain with Go 👀 ](https://www.reddit.com/r/golang/comments/16oy83u/langchain_with_go/) , 2023-09-24-0910
```
Hey has anyone used [https://github.com/tmc/langchaingo](https://github.com/tmc/langchaingo) ive used Langchain with Pyt
hon but I'm going to be experimenting with this library in Go. Im curious if anyone here is doing any LLM work with Go. 
Also if anyone here is implementing any ml or ai with Go I would appreciate it if you could share any repositories that 
I could look through.
```
---

     
 
all -  [ Named Entity Recognition fine-tune LLM ](https://www.reddit.com/r/LangChain/comments/16owyof/named_entity_recognition_finetune_llm/) , 2023-09-24-0910
```
I am seeking a reference code/repo showcasing an example of fine-tuning LLM for named entity recognition. I am especiall
y interested in input-output pair formatting.
```
---

     
 
all -  [ [Personal AI/ML Project] Chatbot which can answer your document ](https://www.reddit.com/r/LangChain/comments/16ouikv/personal_aiml_project_chatbot_which_can_answer/) , 2023-09-24-0910
```
Hi Folks,

During my free time doing personal project basically created a chatbot which can answer your question from do
cument. I used Langchain(framework), ChromaDB(vector database), Streamlit(ui) and used both local llm(Llama2 based model
) or OpenAI api for llm. You can use PDF, TXT, CSV, and DOCX files for question answering. Any contributions to this pro
ject will be highly welcome. Thanks!

Github link: [https://github.com/himanshu662000/InfoGPT](https://github.com/himans
hu662000/InfoGPT)

&#x200B;

&#x200B;
```
---

     
 
all -  [ [Personal AI/ML Project] Chatbot which can answer your document ](https://www.reddit.com/r/developersIndia/comments/16oubq1/personal_aiml_project_chatbot_which_can_answer/) , 2023-09-24-0910
```
Hi Folks,

During my free time, I was doing personal project basically created a chatbot which can answer your question 
from document. I used Langchain(framework), ChromaDB(vector database), Streamlit(ui) and used both local llm(Llama2 base
d model) or OpenAI api for llm. You can use PDF, TXT, CSV, and DOCX files for question answering. Any contributions to t
his project will be highly welcome. Thanks!

Github link: [https://github.com/himanshu662000/InfoGPT](https://github.com
/himanshu662000/InfoGPT)
```
---

     
 
all -  [ Real-time ChatGPT ](https://www.reddit.com/r/LangChain/comments/16orpax/realtime_chatgpt/) , 2023-09-24-0910
```
Do anyone of you guys have experience of Using the Search functionality in Agents. Actually, I'm trying to create an Con
versation model that will answer current scenario questions as well using ChainLit and Langchain. I'm just doing it for 
practice. What are your thoughts on this?
```
---

     
 
all -  [ Meet BondAI, an AI Agent that works better than AutoGPT and has a friendly API for building your own ](https://www.reddit.com/r/OpenSourceAI/comments/16oo2fe/meet_bondai_an_ai_agent_that_works_better_than/) , 2023-09-24-0910
```
📢 I'm excited to introduce **BondAI**, an AI Agent framework and CLI, with a lightweight yet robust API making integrati
on into your own applications straightforward and easy.

**Repository**: [https://github.com/krohling/bondai](https://gi
thub.com/krohling/bondai)

# ⚡️Examples

Here's an example of buying/selling Stocks with [Alpaca Markets](https://alpaca
.markets/). I strongly recommend using Paper Trading btw!

    from bondai import Agent 
    from bondai.tools.alpaca_ma
rkets import (
        CreateOrderTool, 
        GetAccountTool, 
        ListPositionsTool
    )
    
    task = (
    
    'I want you to sell off all of my existing positions.'
        Then I want you to buy 10 shares of NVIDIA with a lim
it price of $456.'
    )
    
    Agent(tools=[
       CreateOrderTool(),
       GetAccountTool(),
       ListPositionsT
ool()
     ]).run(task) 

&#x200B;

[Here's an example](https://github.com/krohling/bondai/tree/main/examples/online-res
earch) of BondAI doing online research and [here's a home automation example](https://github.com/krohling/bondai/tree/ma
in/examples/home-automation).

# 🔍 What is BondAI?

BondAI is a framework crafted for the smooth integration and customi
zation of Conversational AI Agents. Leveraging the power of OpenAI's [function calling support](https://openai.com/blog/
function-calling-and-other-api-updates), it sidesteps the hurdles often encountered in building a Conversational Agent, 
offering solutions such as:

* Integration with Azure OpenAI Services
* Memory management
* Error handling
* Integrated 
semantic search
* A rich array of pre-existing tools
* Straightforward API for crafting custom tools

Moreover, it offer
s a CLI interface that promises an impressive command line agent experience, available to anyone with an OpenAI API Key!


# 🏗️ Why build BondAI?

I am convinced that AI agents are going to be an important architecture for the future of AI. 
Despite their phenomenal problem-solving abilities, the existing tooling often fell short in performing simple tasks, an
d the frameworks appeared unnecessarily complicated. This spurred the birth of BondAI, aiming to address these shortcomi
ngs and offer a more optimized environment for agent implementations.

I am keen on hearing your feedback on BondAI's fu
nctionality and any suggestions for improvements!

# 🛠️ Installation & Usage

Getting started is super simple with the B
ondAI CLI

    pip install bondai
    export OPENAI_API_KEY=xxxxxx
    bondai # Start the CLI

The CLI tool offers a rea
dy-to-use agent experience packed with several default tools. You can also integrate it with various tools such as Googl
e Search, Alpaca Markets, and LangChain Tools to execute a myriad of tasks effectively. Detailed guides and examples for
 usage are available in the README.

# 🔧 APIs and Custom Tools

The BondAI framework offers flexible APIs to build your 
agent and create custom tools. It follows a straightforward implementation approach, making the tool creation process ha
ssle-free for developers.

Examples of included Tools:

* Google and Duck Duck Go Search
* Semantic Search for Files and
 Websites
* Alpaca Markets
* Gmail Integration
* Easily import tools from LangChain!

# 🐋 Docker Container

For a secure
 environment, especially while using tools with file system access, running BondAI within a docker container is highly r
ecommended. Follow the steps in the REAME to easily build and run the BondAI container.

🚀 Join the mission; contribute 
to BondAI! And please share feedback/ideas in the comments!
```
---

     
 
all -  [ Random/Wrong Answer - URL ](https://www.reddit.com/r/LangChain/comments/16omfio/randomwrong_answer_url/) , 2023-09-24-0910
```
I posted this in the llama2 subreddit but thought i'd try here as well, apologies if not allowed.  
I'm trying out the L
lama2 via llama cpp and langchain in a QA setup, very basic. I loaded only one document, txt that had something like the
 following below with nothing else,

ABC Order #1111
Status: Open

ABC Order #2222
Status: Shipped

ABC Order #3333
Stat
us: Cancelled

However when i asked, 'tell me about ABC Order #2222', it answered with:

'It has been shipped and you ca
n track it here https://tracking.abcorder.com/orders/2222'

My question on any thoughts where it even came up with that 
URL, is there something i can do with the prompts to avoid unnecessary info that wasn't asked, especially since it has n
o basis.

Thank you
```
---

     
 
all -  [ Random/Wrong answers ](https://www.reddit.com/r/LLaMA2/comments/16om6li/randomwrong_answers/) , 2023-09-24-0910
```
I'm trying out the Llama2 via llama cpp and langchain in a QA setup, very basic.  I loaded only one document, txt that h
ad something like the following below with nothing else,  


ABC Order #1111  
Status:  Open

ABC Order #2222  
Status: 
 Shipped

ABC Order #3333  
Status:  Cancelled

However when i asked, 'tell me about ABC Order #2222', it answered with:


 'It has been shipped and you can track it here [https://tracking.abcorder.com/orders/2222](https://tracking.abcrder.c
om/orders/2222)'

My question on any thoughts where it even came up with that URL, is there something i can do with the 
prompts to avoid unnecessary info that wasn't asked, especially since it has no basis.

Thank you
```
---

     
 
all -  [ looking for LangChain example_selector guide. Have you seen a good one? ](https://www.reddit.com/r/LangChain/comments/16olm9c/looking_for_langchain_example_selector_guide_have/) , 2023-09-24-0910
```
Hi

Im trying to find some more complex implementations guides for example\_selector.

[One from the docs](https://pytho
n.langchain.com/docs/modules/model_io/prompts/example_selectors/similarity) doesn't cover cases when your examples have 
nested json structure.

Will appreciate if you share some good  implementation  examples
```
---

     
 
all -  [ Getting completely random stuff with LlamaCpp when using the llama-2-7b.Q4_K_M.gguf model ](https://www.reddit.com/r/LocalLLaMA/comments/16oldrp/getting_completely_random_stuff_with_llamacpp/) , 2023-09-24-0910
```
Hello first I must say: I'm completely new to this. Today I tried the llama 7b model and this code

    from langchain.l
lms import LlamaCpp
    
    model = LlamaCpp(
        verbose=False,
        model_path='./model/llama-2-7b.Q4_K_M.gguf
',
    )
    
    o = model('Hi how are you?')
    print(o)

Returns a completely large random message that basically ju
st extends what I typed in.

The return is:

>I was asked by a friend to take over as leader of the local youth club. ev
erybody else has moved away or is busy, so who's going to run it?  
>  
>A: That's a difficult task.  
>  
>B: It was a 
really successful club, but nobody wants to do it any more. We need someone with experience and commitment.  
>  
>A: Ye
s, I can understand that.  
>  
>B: But what I don't know is whether you have the necessary experience or commitment.

&
#x200B;

I tried using a better prompt but it basically always happend that my model would just talk with itself and aut
ocomplete what I just typed and fantasizing.

Maybe someone could explain to me why that happens and how I prevent this 
from happening. 

&#x200B;
```
---

     
 
all -  [ LangChain in MOJO for speedup? 🔥 ](https://www.reddit.com/r/LangChain/comments/16ol9b0/langchain_in_mojo_for_speedup/) , 2023-09-24-0910
```
As far as I understand, you can run Python code in the newly released Mojo language for speedup, right? I haven't tried 
this out yet but was wondering:

Would using LangChain in Mojo (if possible) lead to any significant performance increas
e? E.g. Things like building a vector database from files can take some time with the DataLoader. 

Would love to hear w
hether this makes sense to try out or not. Thanks!
```
---

     
 
all -  [ DevOps AI Assistant Open Leaderboard ](https://www.reddit.com/r/devops/comments/16ol4d6/devops_ai_assistant_open_leaderboard/) , 2023-09-24-0910
```
Over the past year, a flurry of AI Assistants for DevOps engineers have been released. However, it's difficult to unders
tand their capabilities without benchmarking their performance. I recently built a [DevOps AI Assistant Open Leaderboard
](https://github.com/opstower-ai/devops-ai-open-leaderboard), a tool to benchmark a number of AI Assistants across a var
iety of DevOps tasks. The raw results, question datasets, and prompts used for evaluation [are available on GitHub](http
s://github.com/opstower-ai/devops-ai-open-leaderboard).

To start, I spent hours searching GitHub and other sources for 
DevOps-focused AI Assistants that can be invoked from the command line or a REST API, are functional, and and are not in
 private BETA. I found 12 AI assistants that met this criteria. Of these 12, 8 are able to directly interact with extern
al systems (versus just generating code or config file snippets). I was able to benchmark 5 of these AI Assistants with 
benchmarks for two more to come.

The current benchmarks are focused on the following tasks:

1. AWS Services
2. AWS Clo
udWatch Metrics
3. AWS Billing
4. kubectl

The following AI Assistants were benchmarked:

1. [OpsTower.ai](https://githu
b.com/opstower-ai/llm-opstower) (AWS Services, AWS CloudWatch Metrics, AWS Billing)
2. [ReleaseAI](https://release.ai/) 
(AWS Services, AWS CloudWatch Metrics, AWS Billing)
3. [mico](https://github.com/tahtaciburak/mico)  (kubectl)
4. [devin
jeon/kubectl-gpt](https://github.com/devinjeon/kubectl-gpt)  (kubectl)
5. [abhishek-ch/kubectl-GPT](https://github.com/a
bhishek-ch/Kubectl-GPT) (kubectl)

My biggest evaluation hurdle was generating ground truth data. These agents interact 
with external services in realtime and the data they return is constantly changing. Inspired by Langsmith's [dynamic eva
luation](https://github.com/langchain-ai/langsmith-cookbook/blob/main/testing-examples/dynamic-data/testing_dynamic_data
.ipynb), I created reference methods to return the data needed to generate correct answers. When evaluating an agent's a
ccuracy on a question/answer, the agent's response is compared to the response from the invoked reference method. I then
 rely on an GPT-4 to [generate a confidence score](https://github.com/opstower-ai/devops-ai-open-leaderboard/blob/main/p
rompts/dynamic_eval.rb) for each answer.

In short, GPT-4 is acting as a human evaluator. This is an approach I'm curren
tly comfortable with: in the early stages of evaluating OpsTower.ai, I started with static ground truth results and need
ed to evaluate the accuracy by hand. This became very tedious, so I implemented the dynamic evaluation mentioned above a
nd saw almost identical accuracy scores between the two approaches. Also, as mentioned in Eugene Yan's excellent [blog p
ost on LLM patterns](https://eugeneyan.com/writing/llm-patterns/#evals-to-measure-performance), using GPT-4 as an evalua
tor has a high correlation with human judgement.

## The results

First, hats off to the DevOps AI Assistants that I was
 able to get running! Many do not work, or the accuracy was so poor I assumed they were not functional.

Below is a summ
ary of answer accuracy. Full details [on GitHub](https://github.com/opstower-ai/devops-ai-open-leaderboard).

**AWS Serv
ices**

* [OpsTower.ai](https://github.com/opstower-ai/llm-opstower) \- 92%
* Release AI - 72%

**AWS Cloudwatch Metrics
**

* [OpsTower.ai](https://github.com/opstower-ai/llm-opstower) \- 89%
* Release AI - 56%

**AWS Billing**

* [OpsTower
.ai](https://github.com/opstower-ai/llm-opstower) \- 91%
* Release AI - 73%

**Kubectl**

* [abhishek-ch/kubectl-GPT](ht
tps://github.com/abhishek-ch/Kubectl-GPT) \- 83%
* devinjeon/kubectl-gpt - 50%
* mico - 17%

## Observations

**OpsTower
.ai and Release AI appear to have the strongest foundation**. I believe they'd both likely handle the kubectl dataset qu
estions well if each agent was trained on kubectl. The AWS dataset is more challenging as both the AWS REST API and the 
AWS CLI is more complex than kubectl.

**I think in the next six months, DevOps AI Assistants will begin to perform more
 complex reasoning.** These agents first need to build up accuracy for the basic tasks, then they can can invoke those t
asks when needed on advanced questions. I do not believe any capable of reliable complex reasoning today.

## Future wor
k

I plan on adding additional benchmarks for Azure, Kubernetes cluster analysis, more AWS services (ex: Cloudwatch Logs
), and advanced reasoning.

## Comments and feedback

I'd love to get suggestions for DevOps AI Assistants I missed or o
ther evaluation benchmarks you'd like to see! See [GitHub for for details](https://github.com/opstower-ai/devops-ai-open
-leaderboard).
```
---

     
 
all -  [ How might I create a 'cast' of 'actors' that I can 'direct'? ](https://www.reddit.com/r/LangChain/comments/16ohy3q/how_might_i_create_a_cast_of_actors_that_i_can/) , 2023-09-24-0910
```
I’d like to create a “cast” that I can “direct.”

Something like this: ———->

**ACTOR 1**: An LLM agent who is a classic
ally trained actor and a member of the Royal Shakespeare Company.

**ACTOR 2**: An LLM agent who is a method actor known
 for being experimental.

**ME**: The Human

**SCENE:**

**Me**: “Ok Actor 1 and Actor 2, I want you to do the balcony s
cene from Romeo and Juliet.”

**\[Actors do the scene\]**

**Me**: “No, that was all wrong! Do it again but this time wi
th passion!”

**\[Actors do scene again, incorporating the director’s notes\]**

Any ideas about how to go about somethi
ng like that? Are there any frameworks/tools/repositories that could help me get there?
```
---

     
 
all -  [ Need Help with Adding Custom Instructions in Chainlit x Langchain with StorageContext ](https://www.reddit.com/r/datascience/comments/16ogkfd/need_help_with_adding_custom_instructions_in/) , 2023-09-24-0910
```
Hello everyone!

&#x200B;

I am a beginner working with Chainlit x Langchain and I am in need of some assistance. I am t
rying to figure out how to add custom instructions for generating answers, such as 'Answer like a pirate would'. I have 
some text files in the 'data' folder, and I'm curious about how to integrate such instructions within the existing setup
.

&#x200B;

Here's a snippet of the current code:

&#x200B;

`try:`

`# rebuild storage context`

`storage_context = St
orageContext.from_defaults(persist_dir='./storage')`

`# load index`

`index = load_index_from_storage(storage_context)`


 `except:`

`from llama_index import GPTVectorStoreIndex, SimpleDirectoryReader`

`documents = SimpleDirectoryReader('
./data').load_data()`

`index = GPTVectorStoreIndex.from_documents(documents)`

`index.storage_context.persist()`

  `u/
cl.on_chat_start async def factory():`

`llm_predictor = LLMPredictor(`

`llm=ChatOpenAI(`

`temperature=0,`

`model_nam
e='gpt-3.5-turbo',`

`streaming=True,`

`# openai_api_key=API_KEY`

`),`

`)`

`service_context = ServiceContext.from_de
faults(`

`llm_predictor=llm_predictor,`

`chunk_size=512,`

`callback_manager=CallbackManager([cl.LlamaIndexCallbackHan
dler()]),`

`)`

`query_engine = index.as_query_engine(`

`service_context=service_context,`

`streaming=True,`

`)`

`c
l.user_session.set('query_engine', query_engine)`

   `u/cl.on_message async def main(message):`

`query_engine = cl.use
r_session.get('query_engine')`

  `# type: RetrieverQueryEngine`

`response = await cl.make_async(query_engine.query)(me
ssage)`

`response_message = cl.Message(content='')`

`for token in response.response_gen:`

`await response_message.str
eam_token(token=token)`

`if response.response_txt:`

`response_message.content = response.response_txt`

`await respons
e_message.send()`  


I think I am stepping into the wrong direction, but I feel that this thing should not be that hard
.

I am looking for guidance on how to integrate custom instructions for answer generation in Chainlit x Langchain and w
ould appreciate any advice or suggestions on learning resources or paths.

 Looking forward to hearing your thoughts and
 suggestions!

&#x200B;

&#x200B;
```
---

     
 
MachineLearning -  [ [P] vLLM, Langchain, Embedchain ? ](https://www.reddit.com/r/MachineLearning/comments/16ndyxc/p_vllm_langchain_embedchain/) , 2023-09-24-0910
```
Which libraries do you think would be the most important to learn between these, and to use in my next personal project 
? This will be a conversational chatbot trained on podcast transcripts
```
---

     
 
MachineLearning -  [ [R] Agents: An Open-source Framework for Autonomous Language Agents - AIWaves Inc 2023 ](https://www.reddit.com/r/MachineLearning/comments/16jl4pe/r_agents_an_opensource_framework_for_autonomous/) , 2023-09-24-0910
```
Paper: [https://arxiv.org/abs/2309.07870](https://arxiv.org/abs/2309.07870) 

Github: [https://github.com/aiwaves-cn/age
nts](https://github.com/aiwaves-cn/agents) 

Abstract:

>Recent advances on large language models (LLMs) enable research
ers and developers to build autonomous language agents that can automatically solve various tasks and **interact with en
vironments, humans, and other agents** using natural language interfaces. **We consider language agents as a promising d
irection towards artificial general intelligence** and release Agents, an **open-source library** with the goal of openi
ng up these advances to a wider non-specialist audience. Agents is carefully engineered to support important **features 
including planning, memory,  tool usage, multi-agent communication, and fine-grained symbolic  control.** Agents is **us
er-friendly** as it **enables non-specialists** to build, customize, test, tune, and deploy state-of-the-art **autonomou
s language agents without much coding**. The **library** is also **research-friendly as its modularized design** makes i
t **easily extensible for researchers.** 

https://preview.redd.it/3bdi71r5rgob1.jpg?width=1131&format=pjpg&auto=webp&s=
760942c19be6ecda791414c812a77e72751c526d

https://preview.redd.it/howf64r5rgob1.jpg?width=1656&format=pjpg&auto=webp&s=6
36744fccab7a1c2bafb902bad5dbb647440fff5

&#x200B;
```
---

     
 
MachineLearning -  [ [P] Ways to speed up llama-2 summarization on sagemaker? ](https://www.reddit.com/r/MachineLearning/comments/16iutyp/p_ways_to_speed_up_llama2_summarization_on/) , 2023-09-24-0910
```
I'm currently working on a project to give a quick summary of long articles/conversations.

I'm running llama-2-7b-chat-
hf with 4bit quantization on a g5.2xlarge instance on sagemaker.

The method I'm using is map\_reduce (option 2)from thi
s webpage [https://python.langchain.com/docs/use\_cases/summarization](https://python.langchain.com/docs/use_cases/summa
rization))

Of everything I've tried this is the only one that's been able to do decent summaries in a reasonable amount
 of time. However with really long articles (10,000+ words) it takes \~6 minutes before giving an output.

I tried runni
ng this same thing on a g5.12xlarge instance which has 4 A10G gpus but it hasn't reduced the time by any noticeable amou
nt.

Is there anything else I could be doing to speed this up?

&#x200B;

For reference here is the code I'm running in 
Sagemaker notebook

[https://gist.github.com/phwang4/1ab4d772228b6fff8616c28ac054c229](https://gist.github.com/phwang4/1
ab4d772228b6fff8616c28ac054c229)
```
---

     
 
MachineLearning -  [ [P][R] Kani: A Lightweight Highly Hackable Open-Source Framework for Building Chat Applications with ](https://www.reddit.com/r/MachineLearning/comments/16gxp51/pr_kani_a_lightweight_highly_hackable_opensource/) , 2023-09-24-0910
```
Hey all, we just released our new project/paper and we thought you all might find it useful!

Our project (Kani) is a su
per lightweight and hackable alternative to frameworks like LangChain or simpleAIchat meant to help developers hook in c
allable functions or tools to chat models easily. With Kani, devs can write functions in pure python and just add one li
ne (the `@ai_function()` decorator) to turn any function into an AI-callable function!

Kani works with any model and ha
s built-in tools for OpenAI, HuggingFace, LLaMAv2, Vicuna, and GGML with more to come. Kani also never does any prompt e
ngineering under the hood and doesn't require learning complex library tools---all defaults are minimal and highly custo
mizable.

Check out our Colab for mini-examples of things like retrieval, web-search, model routing, etc. [https://colab
.research.google.com/github/zhudotexe/kani/blob/main/examples/colab\_examples.ipynb](https://colab.research.google.com/g
ithub/zhudotexe/kani/blob/main/examples/colab_examples.ipynb)  

If you're interested in learning more check out our lin
ks below!  
Paper: [https://arxiv.org/abs/2309.05542](https://arxiv.org/abs/2309.05542)  
GitHub: [https://github.com/zh
udotexe/kani](https://github.com/zhudotexe/kani)  
Docs: [https://kani.readthedocs.io/](https://kani.readthedocs.io/)
```
---

     
 
MachineLearning -  [ [D] Data Extraction using fine-tuned LLM? ](https://www.reddit.com/r/MachineLearning/comments/16fenlb/d_data_extraction_using_finetuned_llm/) , 2023-09-24-0910
```
Hey Reddit,

I'm working on a tool to pull data from highly irregular Excel files. I've gotten reasonable results which 
is extremely fast with standard Python coding, but it's far from perfect due to the lack of standardized templates. 

In
terestingly, when I tested ChatGPT-4 on a sample table, it did a decent job at data extraction. However, relying solely 
on GPT-4 has its downsides like token limits and slow processing speed (and data privacy issues). Plus, splitting the Ex
cel sheet to fit within these limits results in loss of context and data.

I'm considering fine-tuning a language model 
to post-process data that was in a Pandas DataFrame (perhaps converted to JSON). Has anyone had success with this approa
ch or have alternative recommendations? I've tried Langchain, but it wasn't helpful.

I have figured out to extract the 
relevant columns, but the post-processing part is where I am considering using an LLM which understands the domain and w
hat needs to be extracted based on the examples I feed it.

Looking forward to your thoughts! And would be happy to answ
er any additional questions.
```
---

     
 
MachineLearning -  [ [D] Chains and Agents ](https://www.reddit.com/r/MachineLearning/comments/16d7ee6/d_chains_and_agents/) , 2023-09-24-0910
```
I think there's a lot of confusion around AI agents today and it's mainly because of lack of definition and using the wr
ong terminology.

We've been talking to many companies who are claiming they're working on agents but when you look unde
r the hood, they are really just chains.

I just listened to the Latent Space pod with Harrison Chase (Founder of Langch
ain) and I really liked how he thinks about chains vs agents.

Chains: sequence of tasks in a more rigid order, where yo
u have more control, more predictability.  
Agents: handling the edge-cases, the long-tail of things that can happen.

A
nd the most important thing is that it's not an OR question but an AND one: you can use them in the same application by 
starting with chains -> figuring our the edge-cases -> using agents to deal with them.

https://preview.redd.it/l59sc4sr
i0nb1.png?width=3127&format=png&auto=webp&s=1f3f8730c48687eaabf1f554deb181cf35b96036
```
---

     
 
MachineLearning -  [ [P] FalkorDB - a fast Graph Database - Knowledge Graph as RAG ](https://www.reddit.com/r/MachineLearning/comments/16cg6k7/p_falkordb_a_fast_graph_database_knowledge_graph/) , 2023-09-24-0910
```
We're building a fast low latency Graph Database called FalkorDB that will also support Vector search.  
It's based on R
edis and can be used both as a stand alone database or a module for existing Redis.  
It feels like that is going to be 
the most optimized way to serve Knowledge as RAG, would love to get your feedback.  
[https://github.com/FalkorDB/falkor
db](https://github.com/FalkorDB/falkordb)  


It already supports LlamIndex and Langchain:  
[https://python.langchain.c
om/docs/use\_cases/more/graph/graph\_falkordb\_qa](https://python.langchain.com/docs/use_cases/more/graph/graph_falkordb
_qa)  
[https://gpt-index.readthedocs.io/en/latest/examples/index\_structs/knowledge\_graph/FalkorDBGraphDemo.html](http
s://gpt-index.readthedocs.io/en/latest/examples/index_structs/knowledge_graph/FalkorDBGraphDemo.html)

&#x200B;
```
---

     
 
MachineLearning -  [ [D] Is there anything LangChain can do better than using LLMs directly (either through a website or  ](https://www.reddit.com/r/MachineLearning/comments/165airj/d_is_there_anything_langchain_can_do_better_than/) , 2023-09-24-0910
```
I haven't used ChatGPT a lot or any other LLMs, I've been reading about  Langchain and its use cases, and I'm having tro
uble wrapping my head  around exactly what it does. From what I understand, its an alternative  interface for LLMs, allo
wing for easy switching between them, and makes  some work for specific use cases easier. If I wanted to write an app or
  script to interact with LLMs and do other tasks, how would LangChain be  better than just making API call(s) to an LLM
, getting back the result  as a string, and doing whatever with it?
```
---

     
 
MachineLearning -  [ Apache Airflow vs. LangChain and LlamaHub for LLM data pipeline [D] ](https://www.reddit.com/r/MachineLearning/comments/160lexg/apache_airflow_vs_langchain_and_llamahub_for_llm/) , 2023-09-24-0910
```
I’m looking for recommendations, suggestions, and/or good documentation that outlines which data pipeline would be best 
to ingest my private data (which will then be split into chunks/nodes for vector embeddings and so forth). Thank you in 
advance!
```
---

     
 
deeplearning -  [ TheBloke/Llama-2-7b does not appear to have a file named pytorch_model.bin, tf_model.h5, model.ckpt  ](https://www.reddit.com/r/deeplearning/comments/16ihzn8/theblokellama27b_does_not_appear_to_have_a_file/) , 2023-09-24-0910
```
Hey everyone!

As you can guess from the title, this is the error I get. I only changed the model in AutoModelForCausalL
M, Older version was 

&#x200B;

&#x200B;

`'''`

`model = AutoModelForCausalLM.from_pretrained('meta-llama/Llama-2-7b-c
hat-hf',`

`device_map ='auto',`

`torch_dtype = torch.float16,`

`use_auth_token = True)`

`'''`

&#x200B;

However, si
nce my GPU is NVIDIA GeForce RTX 2080 TI, it answers a simple question in 20 mins. Then I changed it to: 

`model = Auto
ModelForCausalLM.from_pretrained('TheBloke/Llama-2-7b-Chat-GGUF',`

`model_file = 'llama-2-7b-chat.q4_K_M.gguf',`

`devi
ce_map ='auto',`

`torch_dtype = torch.float16,`

`use_auth_token = True)`

&#x200B;

However, this is not working, and 
giving the error. Below is the full code, if it is needed to solve.

&#x200B;

&#x200B;

from langchain.document\_loader
s import JSONLoader

from langchain.text\_splitter import CharacterTextSplitter, TokenTextSplitter, RecursiveCharacterTe
xtSplitter

from langchain.embeddings import HuggingFaceEmbeddings

from langchain.vectorstores import Chroma

from lang
chain import HuggingFacePipeline

from langchain.chains import ConversationalRetrievalChain

from langchain.memory impor
t ConversationBufferMemory

from langchain.embeddings.openai import OpenAIEmbeddings

from langchain.embeddings.huggingf
ace import HuggingFaceEmbeddings

from langchain.chat\_models import ChatOpenAI

import os

import sys

import huggingfa
ce\_hub

from huggingface\_hub import notebook\_login

import torch

import transformers

from transformers import AutoT
okenizer, AutoModelForCausalLM, pipeline

from torch import cuda, bfloat16

import chromadb

from pathlib import Path

f
rom pprint import pprint

import json

from loader import JSONLoader

from [langchain.prompts.chat](https://langchain.pr
ompts.chat) import PromptTemplate, HumanMessagePromptTemplate, SystemMessagePromptTemplate, ChatPromptTemplate

import j
son

from langchain.docstore.document import Document

&#x200B;

def parse\_json(json\_data):

'''Parse JSON data into a
 Python dictionary.'''

return json.loads(json\_data)

&#x200B;

def create\_doc(json\_data):

'''Create a Document obje
ct from JSON data.'''

data = parse\_json(json\_data)

content\_value = ''

&#x200B;

\# Collect values of keys that con
tain 'item' in their name

for key, value in data.items():

if 'item' in key.lower():

content\_value += value + '\\n' 




&#x200B;

return Document(page\_content=content\_value, metadata={'company': data\['company'\]})

&#x200B;

&#x200B;


\##embed\_model\_id = 'BAAI/bge-base-en' ## CHANGE

&#x200B;

embed\_model\_id = 'sentence-transformers/all-mpnet-base-
v2'

&#x200B;

&#x200B;

&#x200B;

device = f'cuda:{cuda.current\_device()}' if cuda.is\_available() else 'cpu' ## NVIDI
A GeForce RTX 2080 TI

&#x200B;

embed\_model = HuggingFaceEmbeddings(

model\_name=embed\_model\_id,

model\_kwargs={'d
evice': device},

encode\_kwargs={'device': device, 'batch\_size': 32}

)

&#x200B;

docs = \[\]

&#x200B;

&#x200B;

fo
r file in os.listdir('lessdata'):

if file.endswith('.json'):

file\_path = './lessdata/'+file

with open(file\_path) as
 file:

json\_data = [file.read](https://file.read)()

document = create\_doc(json\_data)

docs.append(document)

&#x200
B;

&#x200B;

document\_splitter = RecursiveCharacterTextSplitter(separators=\['\\n'\], chunk\_size = 500, chunk\_overla
p = 100)

document\_chunks = document\_splitter.split\_documents(docs)

&#x200B;

&#x200B;

vectordb = Chroma.from\_docu
ments(document\_chunks,embedding=embed\_model, persist\_directory='./database')

&#x200B;

\##vectordb.persist()

'''

v
ectordb = Chroma.from\_documents(document\_chunks,embedding=embed\_model, persist\_directory='./database')

vectordb.per
sist('./database')

&#x200B;

&#x200B;

'''

&#x200B;

&#x200B;

&#x200B;

\### PLEASE DO NOT TOUCH THE VSCODE

&#x200B;


&#x200B;

tokenizer = AutoTokenizer.from\_pretrained('meta-llama/Llama-2-7b-chat-hf', use\_auth\_token = True,)

&#x20
0B;

&#x200B;

model = AutoModelForCausalLM.from\_pretrained('TheBloke/Llama-2-7b-Chat-GGUF',

model\_file = 'llama-2-7b
-chat.q4\_K\_M.gguf',

device\_map ='auto',

torch\_dtype = torch.float16,

use\_auth\_token = True)

&#x200B;

&#x200B;


&#x200B;

&#x200B;

'''

model = AutoModelForCausalLM.from\_pretrained('meta-llama/Llama-2-7b-chat-hf',

device\_map =
'auto',

torch\_dtype = torch.float16,

use\_auth\_token = True)

&#x200B;

&#x200B;

'''

&#x200B;

&#x200B;

&#x200B;


pipe = pipeline('text-generation',

model = model,

tokenizer = tokenizer,

device\_map='auto',

max\_new\_tokens = 512
,

min\_new\_tokens = 1,

top\_k = 5) ##see it 

&#x200B;

\## In vectorstore, take top 5 closest vectors-inputs-context
s, whatever you wanna call.

&#x200B;

llm = HuggingFacePipeline(pipeline=pipe, model\_kwargs= {'temperature':0.7})

&#x
200B;

memory = ConversationBufferMemory(memory\_key='chat\_history', input\_key='question', output\_key='answer', retur
n\_messages=True)

&#x200B;

system\_template = r''' 

Given a context, use your knowledge and answer the question. Be f
lexible, and try everything to answer in the format asked by query.

 \----

{context}

\----

'''

&#x200B;

&#x200B;


user\_template = 'Question:\`\`\`{question}\`\`\`'

&#x200B;

messages = \[

SystemMessagePromptTemplate.from\_template(
system\_template),

HumanMessagePromptTemplate.from\_template(user\_template)

\]

&#x200B;

&#x200B;

qa\_prompt = Chat
PromptTemplate.from\_messages(messages)

&#x200B;

&#x200B;

&#x200B;

jsonExpert = ConversationalRetrievalChain.from\_l
lm(llm = llm, 

retriever=vectordb.as\_retriever(search\_kwargs = {'k': 1}), ## whats it

verbose = True, memory = memor
y, combine\_docs\_chain\_kwargs={'prompt': qa\_prompt},

return\_source\_documents = True

)

&#x200B;

\##retriever ret
urns 1 output object.

&#x200B;

chat\_history = \[\]

query = 'Consider the financials and progress of companies who is
 in the tech business.'

result = jsonExpert({'question': query}, {'chat\_history': chat\_history})

\#result = jsonExpe
rt({'question': query})

&#x200B;

&#x200B;

sources = result\['source\_documents'\]\[0\]

print(result\['answer'\])

pp
rint(sources)

pprint(memory)
```
---

     
 
deeplearning -  [ How to find 'custom' datasets for LLM ](https://www.reddit.com/r/deeplearning/comments/16bj3hg/how_to_find_custom_datasets_for_llm/) , 2023-09-24-0910
```
Hey folks,

I've been digging everywhere, including here, for LLMs and custom applications. So, I read many things, lear
ned from ppl here. Its time to try something. I will try implement Llama v2 - Langchain - Chroma combination. But also I
 want to upload a dataset so that I can try my model on that. 

I find some datasets big enough (for now, 2-5 gb is ok) 
however they are table-style. I want something more texty, I mean I could use 'American Stories' or 'Arxiv' however I be
lieve that they are already used by Llama to train. 

&#x200B;

Is there any suggestions or sources that you can provide
 ? Thanks!
```
---

     
