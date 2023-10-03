 
all -  [ TED AI Hackathon: Harrison Chase is Judging ](/r/hackathon/comments/16yb65n/ted_ai_hackathon/) , 2023-10-03-0909
```

```
---

     
 
all -  [ Overview: AI Assembly Architectures ](https://www.reddit.com/r/AI_Agents/comments/16yc9zg/overview_ai_assembly_architectures/) , 2023-10-03-0909
```
I'm currently trying to make a list with all agent-systems, RAG systems, cognitive architectures, and similar. Then coll
ecting data on the features and limitations, as many points of distinction as possible, opinions, ... Input is welcome.


- Auto-GPT: [github.com/Significant-Gravitas/Auto-GPT](https://github.com/Significant-Gravitas/Auto-GPT)
- AutoGen: [gi
thub.com/microsoft/autogen](https://github.com/microsoft/autogen)
- BASI: [github.com/oliveirabruno01/babyagi-asi](https
://github.com/oliveirabruno01/babyagi-asi)
- BabyAGI: [github.com/yoheinakajima/babyagi](https://github.com/yoheinakajim
a/babyagi)
- GripTape: [griptape.ai](https://griptape.ai)
- Jarvis: [github.com/microsoft/JARVIS](https://github.com/mic
rosoft/JARVIS)
- LangChain [docs.langchain.com/docs](https://docs.langchain.com/docs)
- LlamaIndex: [github.com/run-llam
a/llama\_index](https://github.com/run-llama/llama_index)
- Open-Assistant [github.com/LAION-AI/Open-Assistant](https://
github.com/LAION-AI/Open-Assistant)
- Semantic Kernel [github.com/microsoft/semantic-kernel](https://github.com/microsof
t/semantic-kernel)
- SmartGPT: [github.com/Cormanz/smartgpt](https://github.com/Cormanz/smartgpt)
- TxAI: [github.com/ne
uml/txtai](https://github.com/neuml/txtai)
- tinyLLM: [github.com/zozoheir/tinyllm](https://github.com/zozoheir/tinyllm)


# Chatbots and Conversational AI:
- BondAI: [github.com/krohling/bondai](https://github.com/krohling/bondai)
- BeeBot:
 [github.com/AutoPackAI/beebot](https://github.com/AutoPackAI/beebot)

# Machine Learning and Data Processing:
- NeMo-Gu
ardrails: [github.com/NVIDIA/NeMo-Guardrails](https://github.com/NVIDIA/NeMo-Guardrails)
- Haystack: [github.com/deepset
-ai/haystack](https://github.com/deepset-ai/haystack)
- EdgeChains: [github.com/arakoodev/EdgeChains](https://github.com
/arakoodev/EdgeChains)

# Frameworks for Advanced AI, Reasoning and Cognitive Architectures:
- ACT-R (Adaptive Control o
f Thought - Rational)
- Soar
- CLARION
- OpenCog: [github.com/opencog](https://github.com/opencog)
- Dave Shapiro: [yout
ube.com/@4IR.David.Shapiro](https://youtube.com/@4IR.David.Shapiro)
- Some guys from IBM Watson worked on it (forgot the
 name)
- Cyc: [en.wikipedia.org/wiki/Cyc](https://en.wikipedia.org/wiki/Cyc)

# Agents in a Virtual Environment
- MineRL
: [minerl.io](https://minerl.io)
- Malmo: [github.com/malmo](https://github.com/microsoft/malmo)
- AgentVerse: [github.c
om/AgentVerse](https://github.com/OpenBMB/AgentVerse)

# Comments and Comparissons (probably outdated)
- /r/ChatGPT/comm
ents/12cql0c/autogpt_vs_babyagi/
- /r/AutoGPT/comments/15jrs4n/autogpt_is_failing_to_acomplish_its_goals/

# Curated Lis
ts
- [github.com/awesome-ai-agents](https://github.com/e2b-dev/awesome-ai-agents)
- [github.com/Awesome-AGI](https://git
hub.com/EmbraceAGI/Awesome-AGI)

# Recommended Tutorials
- RAG: gpt-index.readthedocs.io/en/latest/examples/low_level/os
s_ingestion_retrieval.html
- RAG: https://python.langchain.com/docs/expression_language/cookbook/retrieval

EDIT: Update
d from time to time.
```
---

     
 
all -  [ [P] Best option for a large, local embedding database? ](https://www.reddit.com/r/MachineLearning/comments/16y9k4x/p_best_option_for_a_large_local_embedding_database/) , 2023-10-03-0909
```
Langchain offers a wide array of vector databases for text embedding models. I need to create a vector database for arou
nd 3 million sentence embeddings, each being of dimension 384. I'm building a prototype, so it has to be local and free 
of charge to use.

So far, I've hit limits for Chroma (41,666 max). I've also tried Redis, QDrant and FAISS - each of th
ese gets so large that it eats up all the RAM and the process gets killed, or with QDrant, just errors out.

I've used P
inecone before, but I don't really want to pay for a prototype as I have plenty of disk space.

I was thinking of chunki
ng the 3 million documents into local vector stores of size 41,666 using ChromaDB - but there isn't a whole lot out ther
e about whether Chroma would allow me to merge all \~70 of these smaller databases into a bigger one for search. I also 
cannot find whether it would be possible to load all 70 of these into memory and search each one individually.

So what 
are my options?

My other thought was just creating a large Doc2Vec model, however I would like to use something more so
phisticated like Huggingface embedding models.
```
---

     
 
all -  [ Building a Chatbot for Internal Document Retrieval Using Language Models ](https://www.reddit.com/r/LangChain/comments/16y76tm/building_a_chatbot_for_internal_document/) , 2023-10-03-0909
```
Hello everyone,

I am currently an intern at a company and am exploring a project idea to pave my way to a full-time pos
ition. I've noticed that employees often need to share and request information contained in various documents (Excel fil
es, emails, etc.). I am considering creating a chatbot to simplify this information retrieval process across different d
epartments.

I've begun by learning about language models and have managed to set up a system that loads documents from 
a directory, converts them to text, and utilizes OpenAI's embedding model to create and save embeddings to a Chroma data
base. I've tested this setup with some machine history data in CSV format provided by a coworker. The goal is to answer 
queries like, 'What's the average number for this column between these dates?' However, the system should also handle em
ails, PDFs, Excel, and Word files.

I used the Llama 7B model for embedding because  I was hitting a token limit per min
ute with the OpenAI model, especially with large files (\~10,000 lines of data). After setting up the VectorDB, I faced 
a token limit issue again while trying to answer questions due to the large amount of data being processed.

Considering
 the privacy and performance requirements, I am also contemplating the use of a local AI model on a powerful machine ins
tead of relying on cloud-based solutions like OpenAI. This could potentially address the performance issues and ensure b
etter data privacy and maybe help me to overcome token limitations.

I initially tried using OpenAI's embedding model to
 process the documents, but I ran into a limitation on the number of tokens that could be processed per minute. Due to t
his restriction, I decided to switch to a local model for embedding, specifically the [**Mistral-7B-v0.1 model**](https:
//huggingface.co/mistralai/Mistral-7B-v0.1) from Hugging Face. This switch allowed me to process the documents and build
 the database without hitting any token limitations. Now that the database is complete, I've switched back to using Open
AI for other parts of the process. However, I am not entirely sure if everything is set up correctly as this code has be
en pieced together over the past three days, and I'm eager to ensure it's on the right track.  


My code:  [here](https
://textbin.net/wibm5znigu)

**Here are my requirements:**

1. Ensure high privacy.
2. Handle a large amount of data effi
ciently.
3. Provide quick responses.
4. Achieve 99% accuracy based solely on document information.

**I have several que
stions and would appreciate any insights:**

1. Am I on the right track with my current approach?
2. Is ChromaDB the rig
ht choice, or is there a better database for my needs?
3. Would a local AI model be more suitable, or is OpenAI preferab
le in this scenario?
4. Are there other models better suited for embedding or chatting, especially with Excel and CSV fi
les? If yes, is it advisable to use different models for different file types?

**Ideally, I'd like to:**

* Specify dat
a (e.g., by department or file name) to make easy for AI.
* Retain a memory of chats for follow-up queries based on prev
ious responses.
* Update the database with new files and data seamlessly.

*Please note that I am not seeking help due t
o laziness; I am on a time limit for this project. While I would continue searching for solutions, any assistance that c
ould help expedite my progress would be greatly appreciated.*

Thank you for your time and suggestions!
```
---

     
 
all -  [ Not split PDF's ](https://www.reddit.com/r/LangChain/comments/16y6ist/not_split_pdfs/) , 2023-10-03-0909
```
I'm trying to process PDF's without splitting them by pages. I essentially want to consider the entire PDF as a single d
ocument. Should I convert the PDF to a single TXT file and then process it or is there anything within the documentation
. I was not able to find anything in the documentation.
```
---

     
 
all -  [ Limiting BabyAGI tasks list... ](https://www.reddit.com/r/LangChain/comments/16y41tc/limiting_babyagi_tasks_list/) , 2023-10-03-0909
```
I have been looking into BabyAGI capabilities and have a small setup done where I have :

*  research reports (PDF) inge
sted in my vector store(azure search)
* ToDo and  ConversationalRetrievalChain  provided as tools to agent\_executor

No
w when i run babyagi with an objective it starts creating tasks using todo tool, which uses openai as llm. But the tasks
 are way out of context from what I have in my search vectordb. Thus, the agent keep creating tasks which cannot be acco
mplished based on data I have in my search index.  


This results in agent going in loops and tasks keep growing until 
max\_iteration count i reached and ends with no answer.  


So, Is there a way to constrict tasks to what can be accompl
ished from knowledge base? Or skip the ones that failed to complete and generate answer out of what was accomplished?
```
---

     
 
all -  [ Chatbot for website? ](https://www.reddit.com/r/LangChain/comments/16y2u4o/chatbot_for_website/) , 2023-10-03-0909
```
How to build a Chatbot that can be integrated with existing websites?
```
---

     
 
all -  [ Langchain tool ](https://www.reddit.com/r/LangChain/comments/16y2p94/langchain_tool/) , 2023-10-03-0909
```
I am looking for a tool easy to setup and fully managed where langchain vector database and API to retrieve information 
can be included. What is your favorite tool? Thanks
```
---

     
 
all -  [ github web scraping? ](https://www.reddit.com/r/ChatGPT/comments/16xy8s9/github_web_scraping/) , 2023-10-03-0909
```
does anyone know the best way to get a whole documentation in a suitable format to integrate with an llm?

I'm thinking 
about using pinecone/langchain to teach an llm my codebase. but the first step is to get the data from the repo.

I trie
d using 'apify' directly on the main github repo page but it seems inefficient and like it ends up with a bunch of usele
ss data.

apologies if any of this is absurd, im new to it. (also is all of this kosher with github's terms and conditio
ns and stuff?)
```
---

     
 
all -  [ github repo scraping? ](https://www.reddit.com/r/LargeLanguageModels/comments/16xy7rz/github_repo_scraping/) , 2023-10-03-0909
```
does anyone know the best way to get a whole documentation in a suitable format to integrate with an llm?

I'm thinking 
about using pinecone/langchain to teach an llm my codebase. but the first step is to get the data from the repo. 

I tri
ed using 'apify' directly on the main github repo page but it seems inefficient and like it ends up with a bunch of usel
ess data. 

apologies if any of this is absurd, im new to it.  (also is all of this kosher with github's terms and condi
tions and stuff?)
```
---

     
 
all -  [ Running OpenAI on top of Function Calls / Agents? ](https://www.reddit.com/r/LangChain/comments/16xvdp6/running_openai_on_top_of_function_calls_agents/) , 2023-10-03-0909
```
We have created a custom agent on top of the built-in CSV and SQL agent - it works great.

Behind the scenes, its runnin
g python code, and I cannot figure out how to run OpenAI Functions on top of that code.

For example, if i upload a CSV 
file, i would like to run OpenAI sentiment on top of the dataset - instead, all the code can run is the built-in python 
libraries, like NLTK, which is weirdly limiting.

Am I missing something?
```
---

     
 
all -  [ Doubt about embeddings with vector stores ](https://www.reddit.com/r/LangChain/comments/16xub91/doubt_about_embeddings_with_vector_stores/) , 2023-10-03-0909
```
Hi guys!

I have adoubt about embedding prices, so here it's the code I'm currently using, which worked (I modified it f
or private information)  


    loader = ConfluenceLoader(url='https://confluenceweb.com', token='tokenConfluence')
    

    documents = loader.load(
        space_key='spaceKey', include_attachments=False, limit=50, max_pages=20
    )
    

    text_splitter = RecursiveCharacterTextSplitter(chunk_size = 500, chunk_overlap = 0)
    
    all_splits = text_spli
tter.split_documents(documents)
    
    vectorstore = Chroma.from_documents(documents=all_splits, embedding=OpenAIEmbed
dings(openai_api_key='openApiKey'))
    
    query = 'Question for the model'
    docs = vectorstore.similarity_search(q
uery)
    
    llm = ChatOpenAI(model_name='gpt-3.5-turbo', temperature=0, openai_api_key='openAiApiKey', max_tokens=100
)
    qa_chain = RetrievalQA.from_chain_type(llm,retriever=vectorstore.as_retriever())
    result = qa_chain({'query': q
uery})
    

The goal of this code is the following: We want to make QA for the information in our Confluence. We want t
o train the model to answer as an assistant for a customer portal.  


**My doubt is the following one:** Do I always ha
ve to pay the price for OpenAiEmbeddings? I've just tried using Chroma, one of the vectorstores recomended in the docume
ntation. In case I execute this code several times, will I always have to pay it?   


Is there any way to have this  se
parated in **two scripts? One for the 'ingestion'** of information from our documents into the vector store and a s**eco
nd script that just asks the model without having to pay the embedding again**. I know that I will always have to pay fo
r passing the question with the prompt and for generating the answer... But is there a way to load everything from my Co
nfluence, embed it and then just make different questions over it? Or will I always need to pay the embedding price?

Sh
ould I just use an open-source free embedding solution like  all-MiniLM-L6-v2? **This project is going to be hosted in A
mazon Web Services**, so I dont know if there would be any kind of problem with that because we dont want to have any lo
cal machine running this code.

&#x200B;

I'm really confused about vector stores, if you could guide me, it would mean 
a lot.

&#x200B;
```
---

     
 
all -  [ Best way to distill information from a long HTML document? ](https://www.reddit.com/r/LocalLLaMA/comments/16xtjq0/best_way_to_distill_information_from_a_long_html/) , 2023-10-03-0909
```
Hi, I am looking for some pointers to distill information from a single, large but quite structural (to human) **HTML** 
document containing some event schedules\*. 

I am using langchain's WebBaseLoader to perform the data ingestion, Recurs
iveCharacterTextSplitter for chunking and Chroma DB as the vector store. Retrieval is done using ConversationalRetrieval
Chain.

The problems I am facing are the title of the event and the schedule information do not sit next to each other, 
and the html2text essentially messed up all the event-schedule relationship (it ended up with all the events jammed toge
ther in one long paragraph and the schedules scattered everywhere). The chunking of text also led to further separation 
of the events and schedule information, and that the answers produced, if any, were only limited to what the maximum con
text the LLM could handle.

My questions are, do you have a better experience dealing with this kind of problem involvin
g many large HTML tables in a single long HTML document? What is the best way to have the LLM to parse and understand su
ch document in order to extract information, not from part of it, but through the whole thing in order to compose the an
swer?

\* A very typical example is [https://www.royalalberthall.com/tickets/](https://www.royalalberthall.com/tickets/)
 . with the exception that the title and the schedule are farther apart (many tables each with many rows). I would like 
to make a query to the LLM such as:

'List all classical music concerts in Oct 2023 in a tabular form containing only th
e titles and the date-time of the concert. For examples:

Title | Date

Easy listening classical | 28 Oct 18:30

Four se
asons- Winter | 30 Oct 19:00'
```
---

     
 
all -  [ llama-cpp on T4 google colab, Unable to use GPU ](https://www.reddit.com/r/LocalLLaMA/comments/16xswej/llamacpp_on_t4_google_colab_unable_to_use_gpu/) , 2023-10-03-0909
```
 In Google Colab, though have access to both CPU and GPU T4 GPU resources for running following code. However, what is t
he reason I am encounter limitations, the GPU is not being used?  I selected T4 from runtime options  

`!CMAKE_ARGS='-D
LLAMA_BLAS=ON -DLLAMA_BLAS_VENDOR=OpenBLAS' pip install llama-cpp-python`

&#x200B;

`!pip install langchain`

`!wget` [
`https://huggingface.co/TheBloke/Llama-2-7b-Chat-GGUF/resolve/main/llama-2-7b-chat.Q5_0.gguf`](https://huggingface.co/Th
eBloke/Llama-2-7b-Chat-GGUF/resolve/main/llama-2-7b-chat.Q5_0.gguf)

&#x200B;

`from langchain.llms import LlamaCpp`

`f
rom langchain.prompts import PromptTemplate`

`from langchain.chains import LLMChain`

`from langchain.callbacks.manager
 import CallbackManager`

`from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler`

&#x200B;

`
prompt = PromptTemplate(template=template, input_variables=['question'])`

&#x200B;

`callback_manager = CallbackManager
([StreamingStdOutCallbackHandler()])`

&#x200B;

`llm = LlamaCpp(`

`model_path='/content/llama-2-7b-chat.Q5_0.gguf',`


`temperature=0.75,`

`max_tokens=500,`

`top_p=1,`

`callback_manager=callback_manager,`

`verbose=True,`

`)`

`llm_cha
in = LLMChain(prompt=prompt, llm=llm)`

&#x200B;

`llm_chain.run(question)`

&#x200B;
```
---

     
 
all -  [ How to download Spotify podcast transcripts? ](https://www.reddit.com/r/LangChain/comments/16xqnid/how_to_download_spotify_podcast_transcripts/) , 2023-10-03-0909
```
Has anyone figured out the best way to process and summarize Spotify podcast?
```
---

     
 
all -  [ About to buy Hardware for 7k ](https://www.reddit.com/r/LocalLLaMA/comments/16xq65o/about_to_buy_hardware_for_7k/) , 2023-10-03-0909
```
 Hey,

At the end of the month, I'll be receiving a profit share of 7k, which I intend to use to purchase hardware for a
n LLM.

I was thinking of:

2x 3090(Used) Intel Core i9-13900K 256GB DDR5 RAM A suitable motherboard, of course (500-1k$
) Is a 1000W PSU enough, or would a 1500W PSU be better?

Using the cloud is not an option for me because I want to trai
n my LLM on my own data, and I generally prefer it to be uncensored, as I'm tired of hearing phrases like, 'As an LLM, I
'd like to remind you that blablabla.'

The goal is to learn how to create a self-operating AI Assistant with Langchain,
 etc., and an RAG where I can store ALL my knowledge about everything that interests me. I just want to dive in and lear
n by working on various projects and expanding my knowledge.

I'm thinking of using 2x 3090 so that I can experiment wit
h combining different models and see how they interact with each other, among other things.

I'm just asking here for an
y potential pitfalls to watch out for. Any hardware suggestions? Are there any good beginner projects?

I'm not particul
arly skilled in Python, but that doesn't mean I can't learn it.
```
---

     
 
all -  [ Which is the best open-source LLM, that can be used well in colab or kaggle ](https://www.reddit.com/r/LangChain/comments/16xpxs4/which_is_the_best_opensource_llm_that_can_be_used/) , 2023-10-03-0909
```
I have been trying to use falcon40b models and gpt Neo models in colab, which model can I possibly use as I can't use th
e above two models as I have resource issues. Only after this I can proceed further to the langchain part. So please hel
p ASAP
```
---

     
 
all -  [ Help With running self hosted LLM using LangChain ](https://www.reddit.com/r/LangChain/comments/16xdxmc/help_with_running_self_hosted_llm_using_langchain/) , 2023-10-03-0909
```
Hi,

I have been trying langchain to run llama-7b model on my server following the documentation at : [https://python.la
ngchain.com/docs/integrations/llms/huggingface\_pipelines](https://python.langchain.com/docs/integrations/llms/huggingfa
ce_pipelines) and seem to run into an issue where i get the error message:

    ValueError: Pipeline with tokenizer with
out pad_token cannot do batching. You can try to set it with \pipe.tokenizer.pad_token_id = model.config.eos_token_id`.`


I tried upgrading, downgrading the transformers library, playing around with it etc. nothing seems to work.I was tryin
g to follow along with this notebook: [https://colab.research.google.com/drive/17eByD88swEphf-1fvNOjf\_C79k0h2DgF?usp=sh
aring#scrollTo=uwII3CSHxgsM](https://colab.research.google.com/drive/17eByD88swEphf-1fvNOjf_C79k0h2DgF?usp=sharing#scrol
lTo=uwII3CSHxgsM) and replacing OpenAI with HuggingFacePipeline does not seem to work as well.

Please enlighten me on w
hat i am doing wrong and how can i fix this to work on my machine?

Test Code (after all the imports)

    # Create the 
LLM Pipeline
    
    llm = HuggingFacePipeline.from_model_id(
        model_id='daryl149/llama-2-7b-hf', 
        task=
'text-generation',
        model_kwargs={
            'temperature': 0,
            'max_length': 100
            }
    
)
    llm('Hello, World!') # this crashes but if llm = OpenAI() then it does not crash. 

&#x200B;
```
---

     
 
all -  [ Dialoqbase – open source chatbot creation platform ](https://www.reddit.com/r/OpenAI/comments/16x8klh/dialoqbase_open_source_chatbot_creation_platform/) , 2023-10-03-0909
```
Hey r/OpenAI friends, 

I've been dedicating the past 3 months to a side project centered on LangchainJS and pgvector. I
'm excited to share that it has evolved significantly during this time. The project currently boasts support for various
 AI models, including OpenAI ChatGPT and other chat models. Moreover, it can seamlessly integrate with popular messaging
 platforms such as ***WhatsApp***, ***Telegram***, and ***Discord***.  


[demo](https://preview.redd.it/0113cd3hvmrb1.p
ng?width=1920&format=png&auto=webp&s=ca6c3e170991d721743cede5176e7f72b94b4fdd)

In addition to these advancements, I've 
implemented several key features to enhance the user experience, such as multi-user support, robust admin controls, and 
more. I'm eager to hear your thoughts and receive any feedback you may have. Your input is invaluable to me. Thank you!


repo: [https://github.com/n4ze3m/dialoqbase](https://github.com/n4ze3m/dialoqbase)
```
---

     
 
all -  [ [D] Perplexity.ai Search Feasibility ](https://www.reddit.com/r/MachineLearning/comments/16x63ce/d_perplexityai_search_feasibility/) , 2023-10-03-0909
```
I've been using [Perplexity.ai](https://perplexity.ai/) for a bit now when it hit me that I don't understand how they ca
n sustain their business model with search. Stuff like Bing search and Google search cost around $5 or more per 1000 sea
rches, so how can they even afford to do this kind of search. Do they have their own search index.

Also, I don't know h
ow they pull in the data from these sources so fast? I've played around with some things like this with Langchain with r
etrieval, but the speed of splitting and tokenizing website html is not very fast. Have they already pre-scrapped the we
bsites from the search results and tokenized them for LLM retrieval?
```
---

     
 
all -  [ Dialoqbase – open source chatbot creation platform ](https://www.reddit.com/r/ChatGPTCoding/comments/16x51n5/dialoqbase_open_source_chatbot_creation_platform/) , 2023-10-03-0909
```
 I've been dedicating the past 3 months to a side project centered on LangchainJS and pgvector. I'm excited to share tha
t it has evolved significantly during this time. The project currently boasts support for various AI models, including C
hatGPT, Llama, Claude, and Bison. Moreover, it can seamlessly integrate with popular messaging platforms such as WhatsAp
p, Telegram, and Discord.

In addition to these advancements, I've implemented several key features to enhance the user 
experience, such as multi-user support, robust admin controls, and more. I'm eager to hear your thoughts and receive any
 feedback you may have. Your input is invaluable to me. Thank you!  


 repo: [https://github.com/n4ze3m/dialoqbase](htt
ps://github.com/n4ze3m/dialoqbase) 
```
---

     
 
all -  [ Best alternatives ](https://www.reddit.com/r/LangChain/comments/16x3bd6/best_alternatives/) , 2023-10-03-0909
```
There’s been a bit of time now for a few alternatives to come out to langchain.

Having started playing with it in its r
elative infancy and watched it grow (growing pains included), I’ve come to believe langchain is really suited more to ve
ry rapid prototyping and an eclectic selection of helpers for testing different implementations.

I’d love to know what 
other tools people have come across that perform some of the functionality that can be found in langchain.

Some that I’
ve looked at:

- [Llama Index AI](https://www.llamaindex.ai/)
- [GripTape](https://www.griptape.ai/)
- [tinyLLM](https:/
/github.com/zozoheir/tinyllm/tree/main)
- [NeMo-Guardrails](https://github.com/NVIDIA/NeMo-Guardrails)
```
---

     
 
all -  [ Does Langchain’s `create_csv_agent` and `create_pandas_dataframe_agent` functions work with non-Open ](https://www.reddit.com/r/LocalLLaMA/comments/16wx0fp/does_langchains_create_csv_agent_and_create/) , 2023-10-03-0909
```
Hey guys, have a question hoping if anyone knows the answer and can help.

Does Langchain's `create_csv_agent` and `crea
te_pandas_dataframe_agent` functions work with non-OpenAl LLM models too like Llama
2 and Vicuna? The only example I hav
e seen in the documentation (in the links below) are only using OpenAI API.

`create_csv_agent`:
https://python.langchai
n.com/docs/integrations/toolkits/csv

`create_pandas_dataframe_agent`:
https://python.langchain.com/docs/integrations/to
olkits/pandas

Would really appreciate ANY input on this. Many thanks!
```
---

     
 
all -  [ Creating Chatbot using langchain and streamlit ](https://www.reddit.com/r/learnpython/comments/16wvovf/creating_chatbot_using_langchain_and_streamlit/) , 2023-10-03-0909
```

Hi everyone! 
I am creating a chatbot using langchain and streamlit 
I am using python version 3.10.1. 
My code was run
ning fine until the moment I have added langchain library it gives me an error  module not found. 
The code goes as foll
ows: 

```
import streamlit as st
from st_chat_message import message
from dotenv import load_dotenv
import os

from lan
gchain.chat_models import ChatOpenAI
from langchain.schema import (
    SystemMessage,
    HumanMessage,
    AIMessage
)



def init():
    #Load the OpenAI API key 
    load_dotenv()
    
    #Check if the API key exists
    if os.getenv('O
PENAI_API_KEY') is None or os.getenv('OPENAI_API_KEY') == '':
        print('OPENAI_API_KEY is not set')
        exit(1)

    else:
        print('OPENAI_API_KEY is set')

    #streamlit page
    st.set_page_config(
        page_title='Your 
own ChatGPT',
        page_icon='🤖'
    )


def main():
    init()

    chat = ChatOpenAI(temperature=0)

    #messages 
history
    if 'messages' not in st.session_state:
        st.session_state.messages = [
            SystemMessage(conte
nt='You are a helpful assistant.')
        ]

    st.header('Your Bot 🤖')

    #sidebar with user input
    with st.side
bar:
        user = st.text_input('Enter your message: ', key='user_input')

        #user input
        if user:
      
      st.session_state.messages.append(HumanMessage(content=user))
            with st.spinner('Thinking...'):
         
       response = chat(st.session_state.messages)
            st.session_state.messages.append(
                AIMessag
e(content=response.content))
```


I am getting the following errors: 
No module named 'langchain.chat_models'
And also 

No module named ‘langchain.schema’


If anyone could help by giving me their guidance and solution to this, I would be 
so grateful. 

Thank you
```
---

     
 
all -  [ Storing Image/Product images ](https://www.reddit.com/r/LangChain/comments/16wuefz/storing_imageproduct_images/) , 2023-10-03-0909
```
 Hi Guys, is ther any way to store image URls \[[https://static.tp-link.com/01\_1598337266170q.jpg](https://static.tp-li
nk.com/01_1598337266170q.jpg)\]  in meta data whie crawling using loader = **RecursiveUrlLoader(url=url, max\_depth=2, e
xtractor=lambda x: Soup(x, 'html.parser').text)** 
```
---

     
 
all -  [ For programmers: proposal for high level library to make prompt chains ](https://www.reddit.com/r/aipromptprogramming/comments/16wna4a/for_programmers_proposal_for_high_level_library/) , 2023-10-03-0909
```
Request for feedback! I'm considering building a high-level library for prompt chains. (Way beyond Langchain.) High-leve
l enough that the code would be a similar length as my illustrative example use cases! [Proposal and 3 illustrative exam
ple use cases here](https://docs.google.com/document/d/1uQCpWqQMzODiDtB8uO0d6tPBOhFiTiVYWLQGeLINfmQ/edit) with commentin
g turned on, and also pasted below for easy reading.

# Primary object

“Node” (or maybe “step”?)
- Inputs: Input values
 to use, wrap them in [] to use them, e.g. `subject`
- Display to user: e.g. 'Ready to write a poem about [subject]'
- R
un prompt or custom code: 'write a poem about [subject] like Dr. Seuss' or `writePoem(subject)`
- Display to user: 'Here
 is your poem: [result]'
- Outputs to Child Prompt: `result` (prompt completion)
- Child nodes: 1-n node IDs, along with
 characters to watch for in `result`, to stop streaming to user *and* indicate which child node to choose


*I need a cl
eaner term to differentiate between what is displayed to the user before, versus after, running something.*

# Illustrat
ive use cases  

## Use case 1: simple chain to gather information  

### Node 1:
```
---

     
 
all -  [ Proposal for high level library to make prompt chains -- feedback? ](https://www.reddit.com/r/PromptCoding/comments/16wn8r4/proposal_for_high_level_library_to_make_prompt/) , 2023-10-03-0909
```
Request for feedback! I'm considering building a high-level library for prompt chains. (Way beyond Langchain.) High-leve
l enough that the code would be a similar length as my illustrative example use cases! [Proposal and 3 illustrative exam
ple use cases here](https://docs.google.com/document/d/1uQCpWqQMzODiDtB8uO0d6tPBOhFiTiVYWLQGeLINfmQ/edit) with commentin
g turned on, and also pasted below for easy reading.

# Primary object

“Node” (or maybe “step”?)
- Inputs: Input values
 to use, wrap them in [] to use them, e.g. `subject`
- Display to user: e.g. 'Ready to write a poem about [subject]'
- R
un prompt or custom code: 'write a poem about [subject] like Dr. Seuss' or `writePoem(subject)`
- Display to user: 'Here
 is your poem: [result]'
- Outputs to Child Prompt: `result` (prompt completion)
- Child nodes: 1-n node IDs, along with
 characters to watch for in `result`, to stop streaming to user *and* indicate which child node to choose


*I need a cl
eaner term to differentiate between what is displayed to the user before, versus after, running something.*

# Illustrat
ive use cases  

## Use case 1: simple chain to gather information  

### Node 1:  
- Inputs: none (starting node)  
- D
isplay to user: 'welcome, please give me a subject for your poem'  
- Run prompt: n/a  
- Display to user: n/a  
- Outpu
ts to Child Prompt: subject (user's response)  
- Child nodes: Node 2  

### Node 2:  
- Inputs: subject  
- Display to 
user: 'sounds good, how about a setting for your poem?'  
- Run prompt: n/a  
- Display to user: n/a  
- Outputs to Chil
d Prompt: setting (user's response)  
- Child nodes: node 3  

### Node 3:  
- Inputs: subject, setting  
- Display to u
ser: n/a  
- Run prompt: 'Generate a poem, in the style of Dr. Seuss, about \[subject\]. -em is set in \[setting\]'  
- 
Display to user: response from prompt  
- Outputs to Child Prompt: n/a  
- Child nodes: none (end)  


## Use case 2: br
anching based on user input or prompt completion  
### Node 1:  
- Inputs: none (starting node)  
- Display to user: 'wh
at would you like to do? 1: play a game, 2: write a poem'  
- Run prompt: n/a  
- Display to user: n/a  
- Outputs to Ch
ild Prompt: n/a  
- Child nodes: Using user's response: Node 2 if 1, Node 3 if 2, otherwise Node 1  
### Node 2:  
- Inp
uts: n/a  
- Display to user: 'You are standing in an open field west of a white house, with a boarded front door. There
 is a small mailbox here. What do you do?'  
- Run prompt: 'analyze the following text: \`\`\`\[user's response\]\`\`\` 
If it is about moving west, going to a house, or going to a door, say: 'A'. Otherwise, if text is about a mailbox, or in
teracting with one, say 'B'. Otherwise, say 'C'.  
- Display to user: n/a  
- Outputs to Child Prompt: action (user's re
sponse)  
- Child nodes: Using prompt completion: Node 4 if A, Node 5 if B, Node 6 if C  

### Node 3:  
- Inputs: n/a  

- Display to user: 'welcome, please give me a subject for your poem'  
- Run prompt: n/a  
- Display to user: n/a  
- O
utputs to Child Prompt: subject (user's response)  
- Child nodes: Node 7  

*(Not showing further nodes because this de
monstrates the use case well enough.)*

## Use case 3: running custom code  

### Node 1:  
- Inputs: none (starting nod
e)  
- Display to user: n/a  
- Run prompt: n/a  
- Display to user: 'Hi, I'm a binary mathematician. My only job is to 
double numbers. What would you like to double?'  
- Outputs to Child Prompt: number (user's response)  
- Child nodes: N
ode 2  

### Node 2:  
- Inputs: number  
- Display to user: n/a  
- Run code: `doubleNumber(number)`
- Display to user:
 result from function  
- Outputs to Child Prompt: n/a  
- Child nodes: n/a  

# Questions
1. Would this kind of library
 be useful for you?
2. Would you be willing to contribute an example use case, if I build it?
3. Does a library that ope
rates at this level already exist? 
    - I know this functionality can be built in many different libraries, e.g. Langc
hain, [Kani](https://github.com/zhudotexe/kani), [https://github.com/aiwaves-cn/agents](https://github.com/aiwaves-cn/ag
ents), etc. They're lower-level. 
    - I’m envisioning something high-level enough that writing the nodes as code would
 be a similar length as the use cases above. Read that again :) This is a library to make writing a prompt chain very qu
ick and easy.
```
---

     
 
all -  [ Chatbot using langchain and streamlit ](https://www.reddit.com/r/pythonhelp/comments/16wluyk/chatbot_using_langchain_and_streamlit/) , 2023-10-03-0909
```
Hi everyone! 
I am creating a chatbot using langchain and streamlit 
I am using python version 3.10.1. 
My code was runn
ing fine until the moment I have added langchain library it gives me an error  module not found. 
The code goes as follo
ws: 

```
import streamlit as st
from st_chat_message import message
from dotenv import load_dotenv
import os

from lang
chain.chat_models import ChatOpenAI
from langchain.schema import (
    SystemMessage,
    HumanMessage,
    AIMessage
)



def init():
    #Load the OpenAI API key 
    load_dotenv()
    
    #Check if the API key exists
    if os.getenv('OP
ENAI_API_KEY') is None or os.getenv('OPENAI_API_KEY') == '':
        print('OPENAI_API_KEY is not set')
        exit(1)

    else:
        print('OPENAI_API_KEY is set')

    #streamlit page
    st.set_page_config(
        page_title='Your o
wn ChatGPT',
        page_icon='🤖'
    )


def main():
    init()

    chat = ChatOpenAI(temperature=0)

    #messages h
istory
    if 'messages' not in st.session_state:
        st.session_state.messages = [
            SystemMessage(conten
t='You are a helpful assistant.')
        ]

    st.header('Your Bot 🤖')

    #sidebar with user input
    with st.sideb
ar:
        user = st.text_input('Enter your message: ', key='user_input')

        #user input
        if user:
       
     st.session_state.messages.append(HumanMessage(content=user))
            with st.spinner('Thinking...'):
          
      response = chat(st.session_state.messages)
            st.session_state.messages.append(
                AIMessage
(content=response.content))
```


I am getting the following errors: 
No module named 'langchain.chat_models'
And also 

No module named ‘langchain.schema’


If anyone could help by giving me their guidance and solution to this, I would be s
o grateful. 

Thank you
```
---

     
 
all -  [ Can't tell why the Llama 2 is running on the GPU ](https://www.reddit.com/r/LocalLLaMA/comments/16wgn01/cant_tell_why_the_llama_2_is_running_on_the_gpu/) , 2023-10-03-0909
```
I am new to running models locally. Recently I downloaded  llama-2-13b-chat.ggmlv3.q6\_K.bin

***My PC params:***

|**GP
U**|Nvidia GeForce 3090|
|:-|:-|
|**Processor**|AMD Ryzen Threadripper 3970X 32-Core Processor, 3901 Mhz, 32 Core(s), 64
 Logical Processor(s)|
|**Motherboard**|ROG STRIX TRX40-E GAMING|
|**RAM**|256GB 3400 Mhz|
|**OS**|Microsoft Windows 11 
Pro / Version	10.0.22621/ Build 22621|

&#x200B;

***Steps taken so far:***

1. Installed CUDA
2. Downloaded and placed 
llama-2-13b-chat.ggmlv3.q6\_K.bin
3. Ran in the prompt
4. Ran the following code in PyCharm

&#x200B;

    from langchai
n.llms import LlamaCpp
    from langchain.prompts import PromptTemplate
    from langchain.chains import LLMChain
    fr
om langchain.callbacks.manager import CallbackManager
    from langchain.callbacks.streaming_stdout import StreamingStdO
utCallbackHandler
    
    
    template = '''Question: {question}
    
    Answer: You are a chief data officer.'''
   
 
    prompt = PromptTemplate(template=template, input_variables=['question'])
    
    # Callbacks support token-wise s
treaming
    callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])
    
    
    n_gpu_layers = 30  # C
hange this value based on your model and your GPU VRAM pool.
    n_batch = 2048  # Should be between 1 and n_ctx, consid
er the amount of VRAM in your GPU.
    
    # Make sure the model path is correct for your system!
    llm = LlamaCpp(
 
       model_path=r'///PycharmProjects\llama_chat\llama-2-13b.Q6_K.gguf',
        n_gpu_layers=n_gpu_layers,
        n_b
atch=n_batch,
        callback_manager=callback_manager,
        verbose=True, # Verbose is required to pass to the call
back manager
    )
    
    
    llm_chain = LLMChain(prompt=prompt, llm=llm)
    question = 'What is data governance?'

    llm_chain.run(question)
    
    question = 'What is data governance?' llm_chain.run(question)

***Partial Output:**
*

    llama_model_loader: - type  f32:   81 tensors
    llama_model_loader: - type q6_K:  282 tensors
    llm_load_prin
t_meta: format           = GGUF V2 (latest)
    llm_load_print_meta: arch             = llama
    llm_load_print_meta: v
ocab type       = SPM
    llm_load_print_meta: n_vocab          = 32000
    llm_load_print_meta: n_merges         = 0
  
  llm_load_print_meta: n_ctx_train      = 4096
    llm_load_print_meta: n_embd           = 5120
    llm_load_print_meta:
 n_head           = 40
    llm_load_print_meta: n_head_kv        = 40
    llm_load_print_meta: n_layer          = 40
   
 llm_load_print_meta: n_rot            = 128
    llm_load_print_meta: n_gqa            = 1
    llm_load_print_meta: f_no
rm_eps       = 0.0e+00
    llm_load_print_meta: f_norm_rms_eps   = 1.0e-05
    llm_load_print_meta: n_ff             = 1
3824
    llm_load_print_meta: freq_base_train  = 10000.0
    llm_load_print_meta: freq_scale_train = 1
    llm_load_prin
t_meta: model type       = 13B
    llm_load_print_meta: model ftype      = mostly Q6_K
    llm_load_print_meta: model pa
rams     = 13.02 B
    llm_load_print_meta: model size       = 9.95 GiB (6.56 BPW) 
    llm_load_print_meta: general.nam
e   = LLaMA v2
    llm_load_print_meta: BOS token = 1 '<s>'
    llm_load_print_meta: EOS token = 2 '</s>'
    llm_load_p
rint_meta: UNK token = 0 '<unk>'
    llm_load_print_meta: LF token  = 13 '<0x0A>'
    llm_load_tensors: ggml ctx size = 
   0.12 MB
    llm_load_tensors: mem required  = 10183.83 MB
    .......................................................
.............................................
    llama_new_context_with_model: n_ctx      = 512
    llama_new_context_w
ith_model: freq_base  = 10000.0
    llama_new_context_with_model: freq_scale = 1
    llama_new_context_with_model: kv se
lf size  =  400.00 MB
    llama_new_context_with_model: compute buffer total size = 80.88 MB
    AVX = 1 | AVX2 = 1 | AV
X512 = 0 | AVX512_VBMI = 0 | AVX512_VNNI = 0 | FMA = 1 | NEON = 0 | ARM_FMA = 0 | F16C = 1 | FP16_VA = 0 | WASM_SIMD = 0
 | BLAS = 0 | SSE3 = 1 | SSSE3 = 0 | VSX = 0 | 
    
    In the past, companies have focused...
    
    ...Data governa
nce is a set of policies and procedures for managing the use of data across an organization. The goal is to ensure that 
all employees have access to the right information at the right time
    
    llama_print_timings:        load time =  2
039.44 ms
    llama_print_timings:      sample time =    57.80 ms /   256 runs   (    0.23 ms per token,  4428.84 tokens
 per second)
    llama_print_timings: prompt eval time =  2039.40 ms /    20 tokens (  101.97 ms per token,     9.81 tok
ens per second)
    llama_print_timings:        eval time = 49202.92 ms /   255 runs   (  192.95 ms per token,     5.18 
tokens per second)
    llama_print_timings:       total time = 51984.77 ms

***Problem:***

When I run the code the CPU 
is clearly being utilized but not the GPU:

https://preview.redd.it/pva0inwo6grb1.png?width=1143&format=png&auto=webp&s=
d1b635bf9db16e44a7a2594012868f0810dca6f0
```
---

     
 
all -  [ Custom local agent strategies ](https://www.reddit.com/r/LocalLLaMA/comments/16wcypn/custom_local_agent_strategies/) , 2023-10-03-0909
```
I’ve been playing around a a lot with langchain and llama models on my M1 Max.

After learning in python, I switched ove
r to node + typescript since that’s my area of expertise. I have a web server that I’ve been using to run test prompts a
nd inputs for various kinds of problems, and I’ve even successfully connected it to Siri with a loop to have a continuou
s conversation with custom memory and a vector store.

My goal is to create a mostly local set of tools that can help me
 do my job as a tech lead and organize my busy life in ways that current tools can’t.

I’ve had success with models bein
g able to categorize between questions, commands, facts, and reminders/todos, and sometimes even splitting compound requ
ests into their parts. I’ve been trying to break down what amounts to agent features into smaller and simpler parts so t
hat current local llms can handle the tasks. Rather than using the prebuilt conversation tools or agents, I have to writ
e them my self and rely less on llms for larger more complicated prompts.

I’m struggling a lot with good json output, a
nd figuring out how to break down multi step commands that mimicking agents. Routing seems to go well as long as you kee
p categorization simple.

What are thoughts on making more calls to limited llms and how to achieve better planning and 
structured output?

What seem to be the best local llms 7-34b for instruct tasks and JSON output?
```
---

     
 
all -  [ Speaking the llm_chain() result ](https://www.reddit.com/r/LangChain/comments/16w8lrz/speaking_the_llm_chain_result/) , 2023-10-03-0909
```
Hey guys , i been making this stuff and i want to speak the word as it generates with llm\_chain(question) , but i been 
trying it , close to what i got is , first it generates and then i put it in a variable and then speak the message with 
pyttsx3 , is there a way that i can speak every word that is being generated?  


here is the code   


 

prompt = Prom
ptTemplate(template=template2, input\_variables=\['chat\_history','question'\])  
callback\_manager = CallbackManager(\[
StreamingStdOutCallbackHandler()\])  
n\_gpu\_layers = 100   
n\_batch = 1024   
llm = LlamaCpp(  
 model\_path='./model
s/llama-2-7b-chat.gguf.q4\_0.bin',  
 n\_gpu\_layers=n\_gpu\_layers,  
 n\_batch=n\_batch,  
 callback\_manager=callback
\_manager,  
 verbose=False, # Verbose is required to pass to the callback manager  
)  
llm\_chain = LLMChain(prompt=pr
ompt, llm=llm, memory=ConversationBufferMemory(memory\_key='chat\_history'))  
while True:  
 question = input('\\n')  

 response = llm\_chain(question)  
 print(response\['text'\])
```
---

     
 
all -  [ LangChain Crash Course freeCodeCamp ](https://www.reddit.com/r/LangChain/comments/16w81cz/langchain_crash_course_freecodecamp/) , 2023-10-03-0909
```
My LangChain Crash course just released yesterday on freeCodeCamp’s YouTube.

I cover some basic but important concepts 
within the LangChain framework.

https://youtu.be/lG7Uxts9SXs?si=HYacT18bfM2eYuKh
```
---

     
 
all -  [ What is the best strategy to compare the products ](https://www.reddit.com/r/LangChain/comments/16w1uzs/what_is_the_best_strategy_to_compare_the_products/) , 2023-10-03-0909
```
Guys, I have one requirement i have different models if cars in pdf . After pre processing, the information stored acros
s the different indices. If i want compare the model A and model B, how can retrieve both the information and compare my
 qurey will be ”compare the mileage of car A and car B”
```
---

     
 
all -  [ What are good langchain alternatives to train LLMs and create LLM apps? ](https://www.reddit.com/r/LocalLLaMA/comments/16vy6aw/what_are_good_langchain_alternatives_to_train/) , 2023-10-03-0909
```
Magentic, minichain, llfn <--- I saw these three but haven't tried them yet except for langchain. Which one do you use t
o rapid prototype LLMs currently?
```
---

     
 
all -  [ MistralAi LLM with Langchin ](https://www.reddit.com/r/LangChain/comments/16vwilm/mistralai_llm_with_langchin/) , 2023-10-03-0909
```
Is Langchain supporting Mistral AI LLM model ?
```
---

     
 
all -  [ Guys I need your help with this: My SQL langchain agent seems to be limiting its answers to 10 rows ](https://www.reddit.com/r/LangChain/comments/16vkve1/guys_i_need_your_help_with_this_my_sql_langchain/) , 2023-10-03-0909
```
My data is in MySQL in the form of a database, containing two tables, 1000 rows and 50 rows. 

I have created a sql agen
t:

 agent = create\_sql\_agent(   

llm=llm,

toolkit=toolkit,

verbose=True,

agent\_type=AgentType.ZERO\_SHOT\_REACT\
_DESCRIPTION,

  )

Then, when I am passing in a query, e.g. List all the trials conducted in Berlin, Germany, my agent 
queries only the first 10 rows. In this case, it returns all the trials conducted in Berlin within the first ten rows. I
 looked into the SQL query it is generated and it has a 'limit 10' command included, which I do not want. 

How do I get
 my agent to query through all the rows of the table, not limiting to 10?

&#x200B;
```
---

     
 
all -  [ Pdf Document preprocessing ](https://www.reddit.com/r/LangChain/comments/16vf12c/pdf_document_preprocessing/) , 2023-10-03-0909
```
I’m wondering if I have a set of complex pdf documents containing paragraph and tables, whether the langchain document l
oader is enough to load all the documents in a nice way and giving a good retrieval performance?
```
---

     
 
all -  [ Would like some help as someone with no coding background. ](https://www.reddit.com/r/OpenAIDev/comments/16vap8r/would_like_some_help_as_someone_with_no_coding/) , 2023-10-03-0909
```
Hey!

As a little project I am trying to build a knowledge base/chatbot to aks it law related questions. But I am gettin
g a bit stuck as I am getting told I have reached the current quota. I don't know how I could solve this. I will leave m
y code below. help would be appreciated!  


 

\# Import necessary libraries  
import streamlit as st  
from langchain.
document\_loaders import TextLoader  
from langchain.vectorstores import FAISS  
from langchain.embeddings.openai import
 OpenAIEmbeddings  
from langchain.prompts import PromptTemplate  
from langchain.chat\_models import ChatOpenAI  
from 
langchain.chains import LLMChain  
from dotenv import load\_dotenv  
import os  
load\_dotenv()  
\# Load your tax-relat
ed text documents  
\# Fetch your OpenAI API key from environment variables  
openai\_api\_key = os.getenv('OPENAI\_API\
_KEY')  
\# Create an instance of TextLoader with the file paths  
text\_loader = TextLoader('D:/My-Space/tax\_laws.txt'
)  
\# Load your tax-related text documents  
documents = text\_loader.load()  
\# Vectorize the documents using LangCha
in and create an index with FAISS  
embeddings = OpenAIEmbeddings()  
db = FAISS.from\_documents(documents, embeddings) 
 
\# Define a Streamlit app  
def main():  
 st.title('Tax Chatbot')  
 \# Create an input box for user queries  
 user\
_query = st.text\_input('Ask a tax-related question')  
 if user\_query:  
 \# Perform similarity search in the knowledg
e base  
 similar\_responses = db.similarity\_search(user\_query, k=3)  
 \# Initialize LangChain  
 llm = ChatOpenAI(te
mperature=0, model='gpt-3.5-turbo-0613')  
 \# Define a template for generating responses  
 template = '''  
You asked:
 {user\_query}  
Here is some information about the tax-related question:  
 {tax\_info}  
'''  
 prompt = PromptTemplat
e(input\_variables=\['user\_query', 'tax\_info'\], template=template)  
 chain = LLMChain(llm=llm, prompt=prompt)  
 \# 
Generate responses based on retrieved documents  
 for response in similar\_responses:  
 tax\_info = response.page\_con
tent  
 st.write(chain.run(user\_query=user\_query, tax\_info=tax\_info))  
if \_\_name\_\_ == '\_\_main\_\_':  
 main()
  


&#x200B;
```
---

     
 
all -  [ I created an Open-source framework to optimize and eval RAG embeddings - Vectorboard ](https://www.reddit.com/r/LangChain/comments/16va3v9/i_created_an_opensource_framework_to_optimize_and/) , 2023-10-03-0909
```
Hi everyone, I just released the first version of Vectorboard, an open-source framework to do hyperparameter searches fo
r embeddings. 

There are many algorithms, and deciding the right chunk size, overlap, and splitting methods is quite ch
allenging. With Vectorboard, you can do a grid search and compare the performance of different methods and parameters th
at are best for your data.

It's in the alpha version and I'd love to hear your feedback: [https://vectorboard.ai/](http
s://vectorboard.ai/)

Github: [https://github.com/Vectorboard/Vectorboard](https://github.com/Vectorboard/Vectorboard) 


Documentation: [https://docs.vectorboard.ai/](https://docs.vectorboard.ai/)
```
---

     
 
all -  [ I made a web app for chatting with all the content related to Confluence Space using Langchain. ](https://www.reddit.com/r/LangChain/comments/16v7wt2/i_made_a_web_app_for_chatting_with_all_the/) , 2023-10-03-0909
```
**Title:** How to Automatically Generate Embeddings for Updated Documents in a Confluence Space and Enable Real-Time Que
stion Answering on the Updated Data?

**Body:** I'm currently working on accessing a Confluence space using Langchain an
d performing question answering on its data. The embeddings of this data are stored in a Chromadb vector database once I
 provide user name,API keyand Space key.  
 However, I'm looking for a way to automatically generate embeddings for any 
documents that change in real-time within the Confluence space and enable real-time question answering on the updated da
ta. Any suggestions or solutions on how to achieve this would be greatly appreciated!
```
---

     
 
all -  [ Distributed System for syncing and ingesting billions of text embeddings ](https://www.reddit.com/r/LangChain/comments/16uq23b/distributed_system_for_syncing_and_ingesting/) , 2023-10-03-0909
```
Hey folks!

Decided to share some inner workings of our architectural diagram for how we are syncing and ingesting billi
ons of text embeddings at scale into vector database (specifically weaviate!) - under the hood it leverages LangChain fo
r some of its pre-processing mechanisms!

[Retrieval Augmented Generation at scale — Building a distributed system for s
ynchronizing and ingesting billions of text embeddings | by Neum AI | Sep, 2023 | Medium](https://medium.com/@neum_ai/re
trieval-augmented-generation-at-scale-building-a-distributed-system-for-synchronizing-and-eaa29162521)
```
---

     
 
all -  [ How to store tool output in agent memory along with chat history? ](https://www.reddit.com/r/LangChain/comments/16ukfac/how_to_store_tool_output_in_agent_memory_along/) , 2023-10-03-0909
```
I'm new to LangChain, and recently setup an agent ('chat-conversational-react-description') with a custom tool to search
 a database of academic papers. The agent successfully uses the tool and accesses the output when asked to preform a sea
rch. However, I'd like to store the full output of the tool in the agent's memory, so I can ask additional questions abo
ut the results, but can't figure out how to achieve this. 

Current behavior of my agent: 

Me: Please search for recent
 papers by Dr. XYZ and give the titles and abstracts. 

Observation from Custom Tool: [Successfully retrieves recent pap
ers including titles, abstracts, dates, and database IDs]

Agent: Sure, here are the recent papers with titles and abstr
acts: [lists recent paper titles and abstracts]

Me: Great, can you please now give me the database IDs for the papers?


Agent: I don't have the ability to recall or provide database IDs from previous interactions. 

So while the input and 
output of the chat history are stored in the agent's memory, the observation / custom tool output is not. Does anyone kn
ow an approach to store this data in the agent's memory?
```
---

     
 
MachineLearning -  [ [P] vLLM, Langchain, Embedchain ? ](https://www.reddit.com/r/MachineLearning/comments/16ndyxc/p_vllm_langchain_embedchain/) , 2023-10-03-0909
```
Which libraries do you think would be the most important to learn between these, and to use in my next personal project 
? This will be a conversational chatbot trained on podcast transcripts
```
---

     
 
MachineLearning -  [ [R] Agents: An Open-source Framework for Autonomous Language Agents - AIWaves Inc 2023 ](https://www.reddit.com/r/MachineLearning/comments/16jl4pe/r_agents_an_opensource_framework_for_autonomous/) , 2023-10-03-0909
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

     
 
MachineLearning -  [ [P] Ways to speed up llama-2 summarization on sagemaker? ](https://www.reddit.com/r/MachineLearning/comments/16iutyp/p_ways_to_speed_up_llama2_summarization_on/) , 2023-10-03-0909
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

     
 
MachineLearning -  [ [P][R] Kani: A Lightweight Highly Hackable Open-Source Framework for Building Chat Applications with ](https://www.reddit.com/r/MachineLearning/comments/16gxp51/pr_kani_a_lightweight_highly_hackable_opensource/) , 2023-10-03-0909
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

     
 
MachineLearning -  [ [D] Data Extraction using fine-tuned LLM? ](https://www.reddit.com/r/MachineLearning/comments/16fenlb/d_data_extraction_using_finetuned_llm/) , 2023-10-03-0909
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

     
 
MachineLearning -  [ [D] Chains and Agents ](https://www.reddit.com/r/MachineLearning/comments/16d7ee6/d_chains_and_agents/) , 2023-10-03-0909
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

     
 
MachineLearning -  [ [P] FalkorDB - a fast Graph Database - Knowledge Graph as RAG ](https://www.reddit.com/r/MachineLearning/comments/16cg6k7/p_falkordb_a_fast_graph_database_knowledge_graph/) , 2023-10-03-0909
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

     
 
deeplearning -  [ TheBloke/Llama-2-7b does not appear to have a file named pytorch_model.bin, tf_model.h5, model.ckpt  ](https://www.reddit.com/r/deeplearning/comments/16ihzn8/theblokellama27b_does_not_appear_to_have_a_file/) , 2023-10-03-0909
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

     
 
deeplearning -  [ How to find 'custom' datasets for LLM ](https://www.reddit.com/r/deeplearning/comments/16bj3hg/how_to_find_custom_datasets_for_llm/) , 2023-10-03-0909
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

     
