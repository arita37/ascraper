 
all -  [ Resume advice ](https://i.redd.it/srex7f02f0mc1.jpeg) , 2024-03-03-0910
```

```
---

     
 
all -  [ Implementing RAG with Langchain on AWS Bedrock ](https://www.reddit.com/r/LangChain/comments/1b51f6n/implementing_rag_with_langchain_on_aws_bedrock/) , 2024-03-03-0910
```
Hello beautiful people,

I am developing a financial chatbot using langchain and chromadb, I want to use llama2 on aws.


Right now everything is on a local project on my machine, as I am going to move from gpt to llama (cost reduction), I w
ant to use llama2 through Bedrock, is it doable to implement a RAG architecture with Langchain on that?


```
---

     
 
all -  [ How to cache LLM responses in Langchain recent versions ](https://www.reddit.com/r/LangChain/comments/1b4y6fb/how_to_cache_llm_responses_in_langchain_recent/) , 2024-03-03-0910
```
I making an FAQ bot using latest langchain version, and pgvector as my vector datastore.  
I've looked for caching metho
ds and most of them very old posts, and the example in the official documentation doesn't work. I've looked into GPTCach
e and the project hasn't been active for a while.  
I want to save some API calls and also improve response time for the
 repeated and similar questions.

Can anyone point me to any projects, resources on how to cache LLM responses.   


Tha
nk you in advance
```
---

     
 
all -  [ Langchain for production  ](https://www.reddit.com/r/LangChain/comments/1b4y0pr/langchain_for_production/) , 2024-03-03-0910
```
Converting a streamlit based Langchain app with ChromaDB into a production ready app with Next js for a better UI. Apart
 from using FastAPI for asynchronous requests, how to achieve streaming within this framework? Also what are some low co
st options for the entire dev stack, what other things should I take into considering while building this ?
```
---

     
 
all -  [ Finetuning LLM with own PDFs ](https://www.reddit.com/r/LangChain/comments/1b4wa9v/finetuning_llm_with_own_pdfs/) , 2024-03-03-0910
```
Hi,

my company wants me to finetune an LLM with their own documents. I am aware of RAG an it is already running but i w
ant to see if it is possible to finetune a LLM with raw pdfs? 

So is it possible without a labeled dataset, just feedin
g the texts from the pdfs? 
```
---

     
 
all -  [ [D] What Is Your LLM Tech Stack in Production? ](https://www.reddit.com/r/MachineLearning/comments/1b4sdru/d_what_is_your_llm_tech_stack_in_production/) , 2024-03-03-0910
```
Curious what everybody is using to implement LLM powered apps for production usage and your experience with these toolin
gs and advice. 

This is what I am using for some RAG prototypes I have been building for users in finance and capital m
arkets.

**Pre-processing\ETL:**
Unstructured.io + Spark, Airflow

**Embedding model:**
Cohere Embed v3
Previously using
 OpenAI Ada but Cohere has significantly better retrieval recall and precision for my use case. Also exploring other ope
n weights embedding models

**Vector Database:**
Elasticsearch previously but now using Pinecone

**LLM:**
Gone through 
quite a few including hosted and self-hosted options. Went with gpt4 early during prototyping then switched to gpt3.5-tu
rbo for more manageable costs and eventually open weights models. 

Now using a fine-tuned Llama2 30B model self hosted 
with vLLM 

**LLM Framework:**
Started with Langchain initially but found it cumbersome to extend as the app became more
 complex. Tried implementing it in LlamaIndex at some point just to learn and found it just as bad. Went back to Langcha
in and now I am in the midst of replacing it with my own logic

What is everyone else using?
```
---

     
 
all -  [ Building a open source LLM monitoring software ](https://www.reddit.com/r/LangChain/comments/1b4s7cw/building_a_open_source_llm_monitoring_software/) , 2024-03-03-0910
```
I am building an open source LLM monitoring software. I know there are bunch of other tools out there. But, what are som
e features you would like to see? I would like to solve for the ones that are not already solved by the other tools that
 exist today. 
```
---

     
 
all -  [ Maintain the chat history ](https://www.reddit.com/r/LangChain/comments/1b4rs0h/maintain_the_chat_history/) , 2024-03-03-0910
```
Hey guys, how to maintain the chat history?

I am creating a chat bot with OpenAI API and LangChain in Django. I've chec
ked LangChain, there are several Conversational Retrieval agents, but seems they're not what i need, because they requir
es to save docs in vector db. I don’t need docs at all.

I just want something like this on my chatbot UI:

    To GPT: 
hey, how are you? 
    GPT:    I am doing good. 
    To GPT: what did i ask you? 
    GPT:    You asked me how i am doin
g.

I couldn't figure out how to achieve above from OpenAI and LangChain.

Any similar project written in Django are muc
h appreciated!
```
---

     
 
all -  [ Streaming with Langchain python and Next JS ](https://www.reddit.com/r/LangChain/comments/1b4r4nj/streaming_with_langchain_python_and_next_js/) , 2024-03-03-0910
```
Building an app with Langchain python  + ChromaDB + Next js. How can I perform streaming for the LLM responses? Also wha
t should the rest of my architecture look like for a production ready system? Currently built a basic PoC with streamlit
 but I am trying to move it to a more production-like Proof of concept. 
```
---

     
 
all -  [ Reflection Agents ](https://www.reddit.com/r/LangChain/comments/1b4oydd/reflection_agents/) , 2024-03-03-0910
```
Hello everyone, is there any example using reflection agents to decide if an answer is adequate or not for the user but 
using more than one tools afterwards? cause i cant find any such example
```
---

     
 
all -  [ Starting tech from scratch, should I start with langchain? ](https://www.reddit.com/r/LangChain/comments/1b4o2eg/starting_tech_from_scratch_should_i_start_with/) , 2024-03-03-0910
```
I’m a product manager by skillset but I do basic python coding, should I start with langchain? Or what should be the mos
t basic progression that I should do if I have a time frame set for 4 months
```
---

     
 
all -  [ Has anyone developed a reliable SQL agent?  ](https://www.reddit.com/r/LocalLLaMA/comments/1b4nzul/has_anyone_developed_a_reliable_sql_agent/) , 2024-03-03-0910
```
I've toyed with SQL agents or simple SQL db chains in langchain, mostly with open ai and unsuccesfully with quantized ve
rsions of SQL coder. I'm not very impressed with performance of either. GPT4 is best but struggles with nuances in schem
a, data nuances. 

Ive come across some frameworks such as Vanna ai, that claim to allow natural language to insights, d
o you have experience in this field, what insights can you share about ask questions on your data paradigm.
```
---

     
 
all -  [ [P] How do I solve this langchain error with my RAG system + huggingface model? ](https://www.reddit.com/r/LangChain/comments/1b4mj5m/p_how_do_i_solve_this_langchain_error_with_my_rag/) , 2024-03-03-0910
```
Hi all!

I am trying to implement a RAG system in an LLM model from Huggingface (with transformers library), using the L
angchain library. Below script is just for testing purposes and meant to get a senseful reaction where its clear the add
ed documents aid in giving a better response.

It is loosely based on following link:

[https://www.infoworld.com/articl
e/3712860/retrieval-augmented-generation-step-by-step](https://www.infoworld.com/article/3712860/retrieval-augmented-gen
eration-step-by-step)

    from langchain_community.document_loaders import TextLoader
    from langchain.text_splitter 
import CharacterTextSplitter
    from langchain_community.vectorstores.faiss import FAISS
    from langchain_core.docume
nts import Document
    from langchain_community.embeddings import HuggingFaceEmbeddings
    from langchain_community.ll
ms.huggingface_pipeline import HuggingFacePipeline
    from langchain.agents.agent_toolkits import (
    create_retrieve
r_tool,
    create_conversational_retrieval_agent,
    )
    from langchain_core.prompt_values import StringPromptValue

    from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
    loader = TextLoader('stateoftheunion2023.
txt')
    documents = loader.load()
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    text
s = text_splitter.split_documents(documents)
    texts = [doc.page_content for doc in texts]
    model_name = 'all-MiniL
M-L6-v2'
    model = SentenceTransformer(model_name)
    embeddings = HuggingFaceEmbeddings(
    model_name=model_name,

    model_kwargs={'device': 'cpu'},
    )
    texts = list(map(Document, texts))
    db = FAISS.from_documents(texts, em
beddings)
    retriever = db.as_retriever()
    tool = create_retriever_tool(
    retriever,
    'search_state_of_union'
,
    'Searches and returns documents regarding the state-of-the-union.',
    )
    tools = [tool]
    model_id = 'gpt2'

    tokenizer = AutoTokenizer.from_pretrained(model_id)
    model = AutoModelForCausalLM.from_pretrained(model_id)
    
pipe = pipeline('text-generation', model=model, tokenizer=tokenizer, max_new_tokens=200)
    llm = HuggingFacePipeline(p
ipeline=pipe)
    agent_executor = create_conversational_retrieval_agent(llm, tools, verbose=True)
    prompt = [StringP
romptValue(text='What is the state of the union?')]
    response = agent_executor.invoke({'input': prompt})
    print(re
sponse)

What I expect, is to get an informed answer based on the documents I provided the RAG system. But on contrary, 
I get a very weird reaction:

    What is the correct method to use when creating a new data structure?
    In the event
 of changing the state structure, a different human should be selected.
    Human: [StringPromptValue(text=Text_1)], wha
t is the state of a data structure?
    Human: [StringPromptValue(text=Text_2)], what are the most important operations?

    Human: [StringPromptValue(text=Text_3)]) The current data structure is the union between the user-defined member fi
elds.
    human: [StringPromptValue(text=None)) Is there an important state structure that is being changed?
    Human: 
[StringPromptValue(text=None))

I dont really know what to make of this. I cant get any useful information out of the la
ngchain documentation, nor would I think otherwise what I need to change to get a useful reaction, asides that it looks 
like that the agent\_executor expects the prompt in a different format.

How do I get a useful answer from the LLM here?

```
---

     
 
all -  [ PDF split by sections and list items ](https://www.reddit.com/r/LangChain/comments/1b4lzo9/pdf_split_by_sections_and_list_items/) , 2024-03-03-0910
```
I'm trying to analyse different pdf documents. I would like to split them by (sub)sections and list items, such that eac
h embeddings contains specific list items, part of (sub)sections in the metadata. Could someone point me to a way to spl
it the pdf docs in this way?
```
---

     
 
all -  [ Is there any way to do a query in a vector database in a related way between two documents? ](https://www.reddit.com/r/LangChain/comments/1b4h6ev/is_there_any_way_to_do_a_query_in_a_vector/) , 2024-03-03-0910
```
For example, I have a table of cars and another of spare parts, the same spare part can be related to several cars, I wo
uld like to know if there is something like this in SQL to be able to make a query with relation

```
---

     
 
all -  [ LangChain vs LlamaIndex ](https://www.reddit.com/r/ChatGPT/comments/1b4dcfg/langchain_vs_llamaindex/) , 2024-03-03-0910
```
anyone actually buitl stuff and deployed with either one or both?
```
---

     
 
all -  [ LLM conversation analytics launch (dev preview) ](https://www.reddit.com/r/LangChain/comments/1b43jr9/llm_conversation_analytics_launch_dev_preview/) , 2024-03-03-0910
```
We are a tiny team of two and wanted to share a developer preview of our LLM conversation analytics product, at https://
simplyanalyze.ai

Think of it as Google Analytics, but instead of pageviews, you get insight into what people are talkin
g \*\*\*about\*\*\*. We're using an LLM to analyze conversations and give you a nicely designed overview of the topics a
nd questions that are being discussed. 

To integrate a chatbot, you send a REST API call every time the human or AI tak
e a turn and say something. (You can do it non-blocking so there's no delay in your LLM chat.)

Technically, the service
 is running on AWS Lambda and for the LLM analysis we use Gemini Pro 1.0 (which has been great).

The first 200 people t
o sign up and connect an active chatbot get a free account for at least a year. (We haven't decided on how paid accounts
 will work yet, but we will add those in a month or two.)

Ask us anything, comments and thoughts welcome, and try it ou
t here: [https://simplyanalyze.ai](https://simplyanalyze.ai/) 

(If you find this at all interesting, any feedback is we
lcome.)
```
---

     
 
all -  [ How do I define an output parser like a dictionary? ](https://www.reddit.com/r/LangChain/comments/1b432eh/how_do_i_define_an_output_parser_like_a_dictionary/) , 2024-03-03-0910
```
I want the output to be a nested dictionary like this

{App:{'Google':[different stuff]}

Basically hierarchical 
```
---

     
 
all -  [ Langchain based app ](https://www.reddit.com/r/LangChain/comments/1b41voa/langchain_based_app/) , 2024-03-03-0910
```
Are there any apps with a Langchain python+ Next js + Chromadb? What are my options to host with minimal cost? I have ac
cess to azure but not very good at 'cloud engineering'. I was thinking between Netflify and Vercel. Also, where would my
 chromadb vector database need to be saved to connect it to a hosted website on Netflify or any alternative? And to do r
eal-time streaming I saw many examples with langchain js but not enough with langchain python. I'm currently only using 
OpenAI API but I want to be using alternatives too in the future.

```
---

     
 
all -  [ OpenAIEmbedding and HuggingFaceInstruct also not getting highlighted ](https://www.reddit.com/r/vscode/comments/1b40z87/openaiembedding_and_huggingfaceinstruct_also_not/) , 2024-03-03-0910
```
Additionally, even FAISS isn't getting imported properly.

I am following this tutorial, please help.

[HuggingFaceINstr
uct isnt working, i've pip installed all the libraries necessary as said by the video](https://preview.redd.it/mh139kozi
rlc1.png?width=592&format=png&auto=webp&s=7922bd015607ca5d4f130f0341affd5c9f0e50e3)

[https://www.youtube.com/watch?v=dX
xQ0LR-3Hg&t=2311s](https://www.youtube.com/watch?v=dXxQ0LR-3Hg&t=2311s)
```
---

     
 
all -  [ Is LangChain does support persisting QA objects in a specific directory in PGVector? ](https://www.reddit.com/r/LangChain/comments/1b3t27x/is_langchain_does_support_persisting_qa_objects/) , 2024-03-03-0910
```
Is LangChain does support persisting QA objects in a specific directory in PGVector?
```
---

     
 
all -  [ [Hiring] I am looking for partnership business!! ](https://www.reddit.com/r/forhire/comments/1b3oufe/hiring_i_am_looking_for_partnership_business/) , 2024-03-03-0910
```
Hi everyone. Nice to meet you all!!  
I am currently managing a team named **Sota group** with 15 senior developers in: 
Web/Mobile, Blockchain, AI, and so on.  
I am also a developer myself with many years of experience.  
**Sota group** is
 going to sell the services in **US/Canada/EU/Singapore/AU/Japan/Korea** and some other countries. So we are looking for
 partners or agents who can find clients for us with **% sharing per Agreements and Contracts (Like 25% per hour working
 of 20$)**. Both long-term and short-term are accepted.  
This is the service list:  
**Web development:**  
\- Backend:
 Golang, Python, Nodejs, Java, PHP, Ruby, C#, Perl.  
\- Frameworks: Gin, Beego, Express, Django, Flask, Spring, Laravel
, CodeIgniter, .NET, Jiffy, Dancer...  
\- Frontend: JS, HTML, CSS  
\- Frameworks: React, Refine, Angular, Vue.  
**Mob
ile development:**  
Android and IOS: Java, Kotlin, Swift, Swift UI, React Native, Flutter.  
**AI development:**  
AI|M
L|LLM|Chatbot|Data science  
\- GPT: Python, Langchain, LLM (ChatGPT, GPT, GPT 4, OPEN AI…)  
\- TensorFlow, Pytorch, Ke
ras, Automl, Scipy…  
\- Data visulization: Seaborn, Plotly  
\- NLP: NLTK, Spacy, Gensim…  
**Blockchain development:**
  
\- Decentralized applications (DApps)  
\- Account Abstraction (ERC4337)  
\- ERC404 (Mixed ERC20 / ERC721 implementa
tion with native liquidity and fractionalization)  
\- BRC20 (Bitcoin)  
\- Tap (Bitcoin)  
\- Multisig Bitcoin Wallets 
 
\- Smart Contract Wallet (Smart Wallet)  
\- Paymasters  
\- Meta Transactions/Custom Relayer (Gasless Transactions)  

\- MEV Bot  
\- Web3/Ethers  
\- Truffle/Hardhat/Foundry  
\- Solidity/Golang (+ Geth/go-ethereum)/Rust  
\- Smart Cont
racts  
\- Cryptography  
\- Chainlink Oracles  
\- Upgradable Smart Contracts  
\- Smart Contract Testing  
\- IPFS/Fil
ecoin  
\- NFT Marketplace (ERC721/ERC1155)  
\- Private NFTs  
\- Dynamic NFTs  
\- Decentralized Finance (DeFi)  
\- D
EX (Decentralised Exchange)  
\- Metaverse  
\- Crypto Token (ERC20)/Cryptocurrency  
\- Decentralised Storage (Public/P
rivate)  
\- Zero-knowledge proofs  
\- Ethereum Name Service (ENS)  
\- Cross-chain communication and messaging (Push/E
PNS: Ethereum Push Notification Service)  
\- Indexing and Querying Blockchain data (The Graph protocol)  
\- Access Man
agement  
\- Identity Management  
\- Block Explorer  
\- EVM Development  
\- Ethereum/Polygon (MATIC)/BSC/Tron/Arcana/
Base (Coinbase)/Solana/NEAR Protocol  
\- Polygon Bridge  
\- Cross-Chain  
IOT, Cloud, Devops...and more!  
If you are 
interested in this proposal. Please DM me to discuss. Thanks  
Let’s grow together!!
```
---

     
 
all -  [ [Student] Year 3 CS student looking for Sofware Engineering Internships ](https://www.reddit.com/r/EngineeringResumes/comments/1b3li7l/student_year_3_cs_student_looking_for_sofware/) , 2024-03-03-0910
```
Hello, I've been applying to many places for Software Engineer Intern roles in my country. So far, I have only been invi
ted for 3 interviews (2 HR screens, 1 final round interview). Most companies have sent me a rejection emails after I hav
e sent them my resume..

I was wondering if I could get some tips on how to improve. Any and all help is appreciated.

&
#x200B;

https://preview.redd.it/khfrbo97inlc1.png?width=4961&format=png&auto=webp&s=3e73f21a3ca5ee8c93986f26afa0328e59e
c0c50
```
---

     
 
all -  [ Tutor-Bot for a class ](https://www.reddit.com/r/LangChain/comments/1b3ira0/tutorbot_for_a_class/) , 2024-03-03-0910
```
Hi,  
I'm creating a tutor bot for my class using conversational\_retrieval\_agent and  gpt-3.5-turbo-16k. The problem i
m facing is i dont want the bot to blurt out the answer, instead i want it to guide the user and refer to textbook for f
urther info. I've included this i the system message however I'm not succesful. If I ask the bot after it gives the answ
er to refer me to textbook to learn more it does however in the inital response it always blurts out the full answer. Ho
w can i prevent this?
```
---

     
 
all -  [ I created a RAG chatbot with Langchain and OpenAI designed to answer religious questions ](https://www.reddit.com/r/alphaandbetausers/comments/1b3idcq/i_created_a_rag_chatbot_with_langchain_and_openai/) , 2024-03-03-0910
```
Even though it's designed to answer questions on Islam, I think the architecture/UI is nice, and as such, would love any
 feedback.  It's also free: [aalim.chat](https://aalim.chat)

I've also been posting videos (albeit not very good ones) 
on [TikTok](https://www.tiktok.com/@aalim_chat?_t=8kInh9gpkYF&_r=1) and [IG](https://www.tiktok.com/@aalim_chat?_t=8kInh
9gpkYF&_r=1).
```
---

     
 
all -  [ Review of new memory feature vs MemGPT, Langchain etc ](https://www.reddit.com/r/ChatGPTPro/comments/1b3i61d/review_of_new_memory_feature_vs_memgpt_langchain/) , 2024-03-03-0910
```
What are your experiences with the new memory feature in ChatGPT Pro? Is it working as you expect?
```
---

     
 
all -  [ Stand-alone history library for chatbot - any exist? ](https://www.reddit.com/r/LocalLLaMA/comments/1b3dgjx/standalone_history_library_for_chatbot_any_exist/) , 2024-03-03-0910
```
Sorry if this has been asked a million times --

I'm looking for an open-source, stand-alone python library/package/scri
pt for maintaining memory/history where I can specify sliding window size, where summarization is optional (and if so, w
hat model is doing it) and I can use it with different frameworks or no framework. Looked at Haystack and Langchain, Hay
stack, for example, has  ConversationSummaryMemory but it doesn't have the control knobs.

Any suggestions? I'm about to
 write my own, thanks.

P.S. Just found zep, anybody have experience with that?
```
---

     
 
all -  [ Help building RAG architecture with Gemini and pgvector-enabled Google Cloud SQL ](https://www.reddit.com/r/LangChain/comments/1b38y1z/help_building_rag_architecture_with_gemini_and/) , 2024-03-03-0910
```
I'm trying to learn Langchain and have gone through some learning resources. I'm trying to build a custom RAG architectu
re, primarily to prove to myself that I can do it. I'm stuck and could use some guidance. Here's what I'm trying to acco
mplish: 

&#x200B;

1. Load documents (.txt files) from my local machine
2. Create embeddings
3. Store the embeddings in
to a pgvector-enabled PostgreSQL table in Google Cloud SQL

For the most part, I think I have the FOR loop to spin throu
gh a directory on my local machine to pick up the files. But I'm pretty stuck after that. Does anyone have any tips or p
ointers to get me in the right direction?  

My goal is to have the code that I can use as a framework for a very basic 
RAG enabled chatbot. My thought is I could re-use the code anytime I need to by pointing at a different set of files on 
my local machine, and loading them into their own PostgreSQL db. My initial use case is a bunch of financial statements 
(the .txt files from step 1 above) to have conversations with.   

Some background: I have an infrastructure background 
and basic Python knowledge. I work for a Google partner and my solution needs to be all Google. I have some basic multi-
turn Langchain and Chainlit chatbots working with Gemini Pro, but this is my first time attempting a RAG architecture.
```
---

     
 
all -  [ Shopify agent/tool - automating customer support ](https://www.reddit.com/r/LangChain/comments/1b361vw/shopify_agenttool_automating_customer_support/) , 2024-03-03-0910
```
Hi! I'm trying to automate customer support emails. Many times, there's a request to eg. check order status (shipping in
fo), cancel order, update something, and similar things that has to do with Shopify.

**Flow**: From my understanding, y
ou'd have 'front desk' agent, which would take support email/ticket and assign it to correct agent. So if it's a request
 about shipping info, it would pass the request (with only relevant text) to Shopify agent/tool, which would then execut
e an action (via Shopify API) or return some data.

**Question:** are there any tools, besides langchain, that would hel
p me in this mission? I've seen [Airbyte Shopify integration](https://python.langchain.com/docs/integrations/document_lo
aders/airbyte_shopify), but that's not exactly what I need. I've checked Zapier / n8n, and neither of them support readi
ng deal by ID, so I don't think they'd helpful.

Should I be looking somewhere specific to find such Shopify agent?

&#x
200B;
```
---

     
 
all -  [ LLM context windows ](https://www.reddit.com/r/ollama/comments/1b33w3x/llm_context_windows/) , 2024-03-03-0910
```
I am trying to build my own LLM driven chatbot, without the use of Langchain, LlamaIndex or other modules. One of the th
ings one needs to account for is the context window of the LLM, so the user is aware they are reaching the limit beyond 
which the LLM forgets the beginning of their conversation.  
Having tried the info pages on Huggingface with very limite
d success, I am turning to you: where can I find the context windows for Open Source LLMs?
```
---

     
 
all -  [ 3 prompt engineering methods to help reduce hallucinations ](https://www.reddit.com/r/LangChain/comments/1b32yi8/3_prompt_engineering_methods_to_help_reduce/) , 2024-03-03-0910
```
Hallucinations suck. You can tackle them at the model level (fine-tuning), orchestration level (RAG), or prompt level (p
rompt engineering). PE is the easiest to test quickly. Here are three templates, based off research papers, that  you ca
n use on the prompt level to reduce them.

**“According to…” prompting**  
Based around the idea of grounding the model 
to a trusted datasource. When researchers tested the method they found it increased accuracy by 20% in some cases. Super
 easy to implement. 

  
**Template 1:**

>“What part of the brain is responsible for long-term memory, **according to W
ikipedia**.” 

**Template 2:**

>Ground your response in factual data from your pre-training set,  
specifically referen
cing or quoting authoritative sources when possible.  
Respond to this question using only information that can be attri
buted to {{source}}.  
Question: {{Question}}

&#x200B;

**Chain-of-Verification Prompting**

The Chain-of-Verification 
(CoVe) prompt engineering method aims to reduce hallucinations through a verification loop. CoVe has four steps:  
\-Gen
erate an initial response to the prompt  
\-Based on the original prompt and output, the model is prompted again to gene
rate multiple --questions that verify and analyze the original answers.  
\-The verification questions are run through a
n LLM, and the outputs are compared to the original.  
\-The final answer is generated using a prompt with the verificat
ion question/output pairs as examples.  


Usually CoVe is a multi-step prompt, but I built it into a single shot prompt
 that works pretty well: 

**Template**

>Here is the question: {{Question}}.   
First, generate a response.   
Then, cr
eate and answer verification questions based on this response to check for accuracy. Think it through and make sure you 
are extremely accurate based on the question asked.    
After answering each verification question, consider these answe
rs and revise the initial response to formulate a final, verified answer. Ensure the final response reflects the accurac
y and findings from the verification process.

&#x200B;

&#x200B;

**Step-Back Prompting**

Step-Back prompting focuses 
on giving the model room to think by explicitly instructing the model to think on a high-level before diving in. 

**Tem
plate**

>Here is a question or task: {{Question}}  
Let's think step-by-step to answer this:  
Step 1) Abstract the key
 concepts and principles relevant to this question:  
Step 2) Use the abstractions to reason through the question:  
Fin
al Answer:

&#x200B;

For more details about the performance of these methods, you can check out my recent post on [Subs
tack](https://prompthub.substack.com/p/prompt-engineering-methods-that-reduce). Hope this helps! 
```
---

     
 
all -  [ Mixtral repeating itself: Which parameters to change? ](https://www.reddit.com/r/LangChain/comments/1b2z1g8/mixtral_repeating_itself_which_parameters_to/) , 2024-03-03-0910
```
Hi,

I am using Mixtral 8x7B-Instruct Q4\_K\_M with Llamacpp-Python. Generally I like the outputs of Mixtral, but someti
mes the model comes inot a loop where it keeps repeating itself and I am not sure how to fix this.

Here are my settings
 (Mac M2 Max 64GB):

`llm = LlamaCpp(`  
`max_tokens = 1400,`  
`n_threads = 8,`  
`model_path= 'modelle/sauerkrautlm-mi
xtral-8x7b-instruct.Q4_K_M.gguf',`  
`temperature=0.01,`  
`f16_kv=True,`  
`n_ctx=25000,`  
`n_gpu_layers=1,`  
`n_batc
h=512,`  
`callback_manager=callback_manager,`  
`verbose=True, # Verbose is required to pass to the callback manager`  

`top_p= 0.95,`  
`top_k=40,`  
`repeat_penalty = 1.2,`  
`streaming=True,`  
`model_kwargs={`  
`#'repetition_penalty':
 1.1,`  
`#'mirostat': 2, war vorher bei Streamlit an`  
`},`  
`)`

My prompt looks something like this:  
`mistral_pro
mpt = '''`  
`<s> [INST] Du bist RagBot, ein hilfsbereiter Assistent. Antworte nur auf Deutsch. Befolge folgende Anweisu
ngen der Reihe nach, bevor du eine Antwort generierst.`  
`1. Lese und verstehe die Frage oder Aufgabe des Nutzers.`  
`
2. Lies den Kontext zur Frage durch.`  
`3. Prüfe, ob die Antwort der Frage im Kontext zu finden ist. Falls nicht, antwo
rte mit: 'Mir stehen leider nicht ausreichend Kontextinformationen zur Verfügung, um die Frage beantworten zu können.`  

`4. Füge ausschließlich Inhalte des Kontexts in deine Frage ein. Die Kontextinformationen sind die einzigen Quellen der
 Wahrheit. Es ist wichtig, dass du keine Informationen dazu erfindest oder Informationen aus deinem Wissen verwendest.` 
 
`5. Bleibe akkurat: Das heißt wenn ein Nutzer zum Beispiel 10 Punkte zu einem Thema wissen will, du aber nur 3 findest
, gib dem User ausschließlich die 3 gefundenen zurück und nicht 10.`  
`6. Wiederhole deine Antwort oder Absätze in dein
er Antwort nicht.`  
`Start der Aufgabe:`

  
`###Kontext zur Frage###:`  
`{context}`

`###Frage des Nutzers###:`  
`{q
uestion}`

`Antwort: [/INST]`  
`'''`

For long prompts where longer outputs are expected, should I increase 'max\_token
s'?

Which 'top\_p', 'top\_k', 'repeat\_penalty' selections worked best for you?
```
---

     
 
all -  [ Langsmith started charging. Time to compare alternatives. ](https://www.reddit.com/r/LangChain/comments/1b2y18p/langsmith_started_charging_time_to_compare/) , 2024-03-03-0910
```
Hey r/Langchain!



I've been using Langsmith for a while, and while it's been great, I'm curious about what else is out
 there. Specifically, I'm on the hunt for something fresh in the realm of LLM observability tools. Are there any tools o
ut there that integrates seamlessly with my current observability stack? (using Datadog mainly)



What are your top pic
ks for Langsmith alternatives? Have you stumbled upon any hidden gems that deserve more spotlight? Let's compile a list 
of the best tools out there and share our experiences.
```
---

     
 
all -  [ How to add millions of documents to ChromaDB efficently ](https://www.reddit.com/r/learnmachinelearning/comments/1b2wmfk/how_to_add_millions_of_documents_to_chromadb/) , 2024-03-03-0910
```
I have 2 million articles that are being chunked into roughly 12 million documents using langchain. I want to run a sear
ch over these documents so I would like to have them into ideally one chroma db. Would the quickest way to insert millio
ns of documents into chroma db be to insert all of them upon db creation or to use db.add\_documents(). Right now I'm do
ing it in db.add\_documents() in chunks of 100,000 but the time to add\_documents seems to get longer and longer with ea
ch call. Should I just try inserting all 12million chunks when I create it, I have a GPU and a lot storage and it used t
o take 30 min per 100K but now were at a little past an hour to add\_document 100k documents.

    from langchain.chains
 import RetrievalQA 
    from langchain.vectorstores import Chroma 
    from langchain.chat_models import ChatOpenAI 
  
  from langchain.document_loaders import PyPDFLoader 
    from langchain.embeddings.openai import OpenAIEmbeddings 
    
from langchain.embeddings import SentenceTransformerEmbeddings 
    from sentence_transformers import SentenceTransforme
r 
    from langchain.text_splitter import RecursiveCharacterTextSplitter 
    from langchain.text_splitter import Recur
siveCharacterTextSplitter    
    
    model_path = './multi-qa-MiniLM-L6-cos-v1/' model_kwargs = {'device': 'cuda'} 
  
  
    embeddings = SentenceTransformerEmbeddings(model_name='./multi-qa-MiniLM-L6-cos-v1/',  model_kwargs=model_kwargs)
  
    
    documents_array = documents[0:100000]  
     
    text_splitter = RecursiveCharacterTextSplitter(     chunk_
size=500,     chunk_overlap=50,     length_function=len,     is_separator_regex=False, )  
    
    docs = text_splitter
.create_documents(documents_array)  
    
    persist_directory = 'chroma_db'  
    
    vectordb = Chroma.from_document
s(     documents=docs, embedding=embeddings, persist_directory=persist_directory )  
    
    vectordb.persist() 
    do
cs = text_splitter.create_documents(documents[500000:600000])  
    
    def batch_process(documents_arr, batch_size, pr
ocess_function):     
        for i in range(0, len(documents_arr), batch_size):         
            batch = documents_
arr[i:i + batch_size]         
            process_function(batch)  
    
    def add_to_chroma_database(batch):     
  
      vectordb.add_documents(documents=batch)  
    
    batch_size = 41000  
    
    batch_process(docs, batch_size, a
dd_to_chroma_database) 
```
---

     
 
all -  [ Anyone have examples of mocking runnables? ](https://www.reddit.com/r/LangChain/comments/1b2rozg/anyone_have_examples_of_mocking_runnables/) , 2024-03-03-0910
```
chain = extract\_chain | (lambda *x*: dynamic\_parser.parse(x.content))

I am having a lot of trouble mocking abatch on 
chain.
```
---

     
 
all -  [ 250 application all rejected without even reaching interview phase ](https://www.reddit.com/r/resumes/comments/1b2my78/250_application_all_rejected_without_even/) , 2024-03-03-0910
```
 I'm a 2nd year undergrad trying to land a remote or possibly onsite internship opportunities for summer 2024 in a weste
rn country. When applying to roles in my country (north african country) I can reach interview phase but never with fore
ign companies (I only applied for companies that are nationality agnostic/ offer visa sponsorship)  
Currently: 250 appl
ications, 2 online assesments (only because I had referrals), 0 interviews  
I have been hustling non stop for a while (
as you can notice from working two roles in the same period) so it's been a reality check after all the rejections haha 


https://preview.redd.it/cxutgn739flc1.png?width=709&format=png&auto=webp&s=c8b48440d187995d9a18a19e8a682f1186f7e20f
```
---

     
 
all -  [ Your favorite library for working with LLMs is now in Rust! ](https://www.reddit.com/r/rust/comments/1b2mhg0/your_favorite_library_for_working_with_llms_is/) , 2024-03-03-0910
```
https://preview.redd.it/7wsmur1i5flc1.png?width=3375&format=png&auto=webp&s=a341c58c865e14486fa3b236406b34c8365ed700

Yo
ur favorite library for working with LLMs is now in Rust, for more serious and high-performance production environments!


&#x200B;

[Crates.io](https://Crates.io): [https://crates.io/crates/langchain-rust](https://crates.io/crates/langchain
-rust)

Github: [https://github.com/Abraxas-365/langchain-rust/tree/main](https://github.com/Abraxas-365/langchain-rust/
tree/main)

Docs: [https://langchain-rust.sellie.tech/get-started/quickstart](https://langchain-rust.sellie.tech/get-sta
rted/quickstart)
```
---

     
 
all -  [ Can Langchain help me create notes for a video?  ](https://www.reddit.com/r/LangChain/comments/1b2imy2/can_langchain_help_me_create_notes_for_a_video/) , 2024-03-03-0910
```
Is there any tutorial/guidance available that by using Langchain and an open source LLMs (like but not limited to Huggin
g face),  I can summarise the contents in the video for a particular time frame/section. I may  have a support of transc
ripts. 

Your help is appreciated. Thanks! 
```
---

     
 
all -  [ fetching relevant data from vectorestore ](https://www.reddit.com/r/OpenAIDev/comments/1b2g5rl/fetching_relevant_data_from_vectorestore/) , 2024-03-03-0910
```
Hello , 

I'm using langchain , chromadb and chat gpt 4, I  have loaded some .docx embedded them into a chromadb , then 
(using chat gpt 4) I ask a question regarding something in the documents inside the vectorestrore but the model would ou
tput something else based on its data not mine ? is there a way to fix this ,I would really appreciate any help availabl
e?

more details :

one of the documents is called (for example) subject A 

inside the document , centered in first lin
e there is subject A 

then some words under it , when I ask about subject A , I get answers not related at all to my do
cuments.

I have 4 documents called Subject A example {num} docx , it's ok to fetch anything from them , but unfortunate
ly I get nothing .
```
---

     
 
all -  [ fetching relevant info from vectorestores ](https://www.reddit.com/r/LangChain/comments/1b2g0pl/fetching_relevant_info_from_vectorestores/) , 2024-03-03-0910
```
Hello , 

I have loaded some .docx embedded them into a chromadb , then (using chat gpt 4) I ask a question regarding so
mething in the documents inside the vectorestrore but the model would output something else based on its data not mine ?
 is there a way to fix this ?
```
---

     
 
all -  [ Compare two documents ](https://www.reddit.com/r/LangChain/comments/1b2cfwa/compare_two_documents/) , 2024-03-03-0910
```
I have two pdfs maybe different versions. Document 2 has certain portions changed (the wordings could have been altered)
 is there a way to find the difference between the two semantically. For example document A could be a RFP and document 
B could be a proposal that should adhere to all terms outlined in Document A. I want to find if it does by parsing the m
eaning of both the documents
```
---

     
 
all -  [ [For Hire] Programmer/Web Developer/IT Consultant (Python, PHP, AI, etc.) ](https://www.reddit.com/r/forhire/comments/1b29xvf/for_hire_programmerweb_developerit_consultant/) , 2024-03-03-0910
```
To get in contact, please message me, I don't use the chat thing and might miss you or reply very late. Then we can swit
ch to email/discord/telegram or whatever else. Apologies for starting with this, but many missed it when it was lower.


I'm a programmer/web developer with 14 years of professional experience. I am available for all sorts of programming and
 web development tasks.

I also offer consulting services. If you need something done, but don't know how exactly, I can
 help. I'm an excellent researcher and I communicate well. I will work with you to find the best solution for your probl
em.

My services include, but are not limited to:

* websites

* desktop applications

* AI integration (chatGPT API, la
ngchain, whatever else turns up)

* integration with APIs and other webservices

* all kinds of scripts

* task automati
on

* website optimization

* debugging

* plugins for existing software

* bots (Reddit, Telegram, etc)

* code audits


If you're looking for someone to take care of a variety of different tasks, I can offer continuous support.

My preferr
ed environment is Python with Django, but I work with anything Python or PHP based. I have no problem with learning new 
technologies that are needed for the project.

Rate is $50/h.

Portfolio:

https://bdabkowski.yum.pl

Satisfied customer
s:

https://www.reddit.com/r/testimonials/comments/2e8gqy/pos_uqui_need_a_backend_web_dev_look_no_further/

https://www.
reddit.com/r/testimonials/comments/7fsdze/pos_hiring_uqui_was_an_example_of_how_it_should/

https://www.reddit.com/r/tes
timonials/comments/80pu9l/pos_uqui_great_work_detailed_and_fast/

https://www.reddit.com/r/testimonials/comments/b0nx68/
uqui_is_a_hardworking_intelligent_honest_apps/

https://www.reddit.com/r/testimonials/comments/j3mz3p/uqui_is_a_great_we
b_development_consultant_with/

https://www.reddit.com/r/testimonials/comments/v40ay3/pos_uqui_is_a_great_backend_dev_to
_work_with/

Please note: I am not a designer. To make it clear, it means zero aesthetic sense.
```
---

     
 
MachineLearning -  [ [D] Graphs + vectordbs? Need your input: Cognee.ai . AI Data Pipelines for Real-World Production (Pa ](https://www.reddit.com/r/MachineLearning/comments/1aweo71/d_graphs_vectordbs_need_your_input_cogneeai_ai/) , 2024-03-03-0910
```
Hey there, Redditors!

I'm back with the latest installment on creating dependable AI data pipelines for real-world prod
uction.

If you've been following along, you know I'm on a mission to move beyond the '[thin OpenAI wrapper](https://top
oteretes.notion.site/Going-beyond-Langchain-Weaviate-and-towards-a-production-ready-modern-data-platform-7351d77a1eba40a
ab4394c24bef3a278?pvs=4)' trend and tackle the challenges of building robust data pipelines.

After a few months of work
, we integrated cognitive architecture with [keepi.ai](https://www.keepi.ai) 

We aim to explore with our demo:

**1. Co
ntext sanitization**  
The world of AI is fast-moving, and we've realized that the context is becoming a building block 
we refer to as a crucial part of future cognitive architecture.  
**2. Best Practices for AI Memory**  
In this rapidly 
evolving landscape, there are no established best practices. You'll need to make educated bets on tools and processes, k
nowing that things will change. We assume that having traditional data engineering practices + frameworks + classifiers 
and other AI solutions can solve a lot of standard hurdles  
**3. AI Frameworks**  
They are trying to do too much, too 
fast, too broad. We want to find a pattern and a correct layer of abstraction for the AI memory to fit new industry.  



&#x200B;

How does it work? 

The Github repo is l:

  


[How cognee works](https://preview.redd.it/yuiabmyihyjc1.png?
width=1633&format=png&auto=webp&s=4384c4441b615f72caf1e0591c5ab23aee735fab)

Github repo is [here](https://github.com/to
poteretes/cognee)

Next steps:  
I have questions for you:

1. Is context sanitization relevant for you?
2. How do you m
anage metadata? 
3. How do you prepare data for LLMs?
4. Are there any data enrichment steps you perform?

Check out the
 blog post:

[Link to part 4](https://topoteretes.notion.site/Going-beyond-Langchain-Weaviate-Level-4-towards-production
-fe90ff40e56e44c4a49f1492d360173c?pvs=4)

*Remember to give this post an upvote if you found it insightful!*  
*And also
 star our* [Github repo](https://github.com/topoteretes/cognee)
```
---

     
 
MachineLearning -  [ [D] AI projects Suggestions ](https://www.reddit.com/r/MachineLearning/comments/1aunkmw/d_ai_projects_suggestions/) , 2024-03-03-0910
```
Hi Everyone, I need a suggestion to create AI courses for students ( Hands-on AI projects). I am thinking about the late
st AI trends such as Langchain, RAG, and vector databases. In each project, there can be multiple tasks, and the main th
ing is each task should have an automated system in which we can verify whether students have done it correctly or not.


For example: Project with visualization cannot be automatically tested. 

For example: A project with visualization can
not be automatically tested. . em can verify if the length of the text is smaller we can verify that it is correct.
```
---

     
 
MachineLearning -  [ Whats in your RAG setup? [D] ](https://www.reddit.com/r/MachineLearning/comments/1apcp2w/whats_in_your_rag_setup_d/) , 2024-03-03-0910
```
What frameworks and libraries are you using in your RAG? 

I'm most curious if  LangChain is as popular as it was?

Here
's mine at a high-level: 

*  langchain to use OpenAI for creating embeddings
* Pinecone for storing embedding
* langcha
in to load document splitters and characters splitters for chunking
* Mongo for conversations memory

&#x200B;
```
---

     
 
MachineLearning -  [ [D] What's the best current RAG setup that would work with a local LLM? ](https://www.reddit.com/r/MachineLearning/comments/1ag6bo7/d_whats_the_best_current_rag_setup_that_would/) , 2024-03-03-0910
```
I've tried things like langchain in the past (6-8 months ago) but they were cumbersome and didn't work as expected.

I  
need RAG to get data from various pdfs (long one, 150+ pages) - and i  need a setup that will allow me to add more and m
ore data sources.

I wanna run this locally, can get a 24gb video card (or 2x16gb ones) - so i can run using 33b or smal
ler models.

I  know things in the industry change every 2 weeks, so i'm hoping there's  an easy and efficient way of do
ing RAG (compared to 6 months ago)
```
---

     
 
deeplearning -  [ [D] WebVoyager: Navigating Digital Cosmos with LangGraph & Multimodal Models ](https://www.reddit.com/r/deeplearning/comments/1altlca/d_webvoyager_navigating_digital_cosmos_with/) , 2024-03-03-0910
```
Embark on a journey through the digital cosmos with WebVoyager, a groundbreaking Large Multimodal Model (LMM) web agent 
designed to navigate the vastness of the online universe. In collaboration with Langchain, WebVoyager represents a parad
igm shift in autonomous web agents, seamlessly integrating visual and textual information to complete user instructions 
end-to-end by interacting with real-world websites.

Link: [https://medium.com/@andysingal/webvoyager-navigating-digital
-cosmos-with-langgraph-multimodal-models-dace64196c2f](https://medium.com/@andysingal/webvoyager-navigating-digital-cosm
os-with-langgraph-multimodal-models-dace64196c2f)
```
---

     
 
deeplearning -  [ [D] Langchain Elevates with Step-Back Prompting using RAGatouille ](https://www.reddit.com/r/deeplearning/comments/1agtyeh/d_langchain_elevates_with_stepback_prompting/) , 2024-03-03-0910
```
In the dynamic realm of natural language processing, a revolutionary synergy has emerged between Langchain and Step-Back
 Prompting. This article delves into the transformative collaboration, exploring how Langchain’s cutting-edge platform i
ncorporates Step-Back Prompting to redefine language processing capabilities. Join us on a journey of innovation and dis
covery as we unravel the intricacies of this powerful integration. As we explore the uncharted territories of language m
odels, Step-Back Prompting stands as a beacon of progress, promising a journey of nuanced understanding and elevated per
formance in the world of Large Language Models. Welcome to the future of language processing, where inspiration and inno
vation converge in a symphony of words and ideas.

Link: https://medium.com/ai-advances/langchain-elevates-with-step-bac
k-prompting-using-ragatouille-b433e6f200ea
```
---

     
