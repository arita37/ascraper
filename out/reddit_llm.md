 
all -  [ Local RAG Chat with ollama, gradio and langchain - POC ](https://www.reddit.com/r/LocalLLaMA/comments/1b5uibf/local_rag_chat_with_ollama_gradio_and_langchain/) , 2024-03-04-0910
```
I built a proof of concept notebook to enable a locally hosted RAG chat with LLama. 

The idea was to use langchain to e
.g. cut markdown files into chunks, embed them with a LLM hosted in ollama, in this case LLama, and then build the chat 
frontend with Gradio. 

If anyone has any ideas on how to improve the similarity search, please let me know :)

[https:/
/github.com/Tr33Bug/Open-Ollama-RAG-ChatApp](https://github.com/Tr33Bug/Open-Ollama-RAG-ChatApp)
```
---

     
 
all -  [ A Langchain based Chatbot Template using Free Huggingface Inference ](https://github.com/machaao/mistral-7b-chatbot) , 2024-03-04-0910
```

```
---

     
 
all -  [ Any suitable way to do retrieval from a knowledge graph in RAG? ](https://www.reddit.com/r/learnmachinelearning/comments/1b5qhgx/any_suitable_way_to_do_retrieval_from_a_knowledge/) , 2024-03-04-0910
```
Basically the title. I want to do retrieval from a knowledge graph while using the generator model llama-7b-chat, the id
ea behind this is to use a structured data instead of doing vector search from a vector database and compare results wit
h the original vector search. I need help with the approach on how to do this part, also I am unsure if langchain suppor
ts this.
```
---

     
 
all -  [ Embedding model error while Loading to Chroma db ](https://www.reddit.com/r/LangChain/comments/1b5pb5u/embedding_model_error_while_loading_to_chroma_db/) , 2024-03-04-0910
```
I am using openai embedding to convert the documents to embedding and post it to chroma db in external server.

collecti
ons = client.get_or_create_collection(name='pdf_of_ai',embedding_function=new OpenAIEmbeddings ())

I have already insta
lled the latest version of langxhain and chroma db but I am still facing this error .

raise ValueError( ValueError: Exp
ected EmbeddingFunction.__call__ to have the following signature: odict_keys(['self', 'input']), got odict_keys(['args',
 'kwargs'])

Can anyone help me resolve this issue?

I even tried custom embedding class but still facing the same error
.
```
---

     
 
all -  [ Fancy Resume? 🤔 ](https://i.redd.it/jy2ej1us16mc1.jpeg) , 2024-03-04-0910
```
I custom made this in Figma around a year back, now I want to update it. I was wondering if a resume like this would hav
e any advantage over a traditional resume? I understand this would help in design related positions, but I will apply mo
stly to coding based positions. Also please provide any other feedback related to it too, thankyou.
```
---

     
 
all -  [ Review my resume ](https://i.redd.it/k8gkr9km16mc1.jpeg) , 2024-03-04-0910
```
I have custom made it in Figma, I have to update it now with iOS experience wondering if this format reduces my hiring c
hances or is a good refresh over traditional resumes?
```
---

     
 
all -  [ Hi pretty new with txtai framework. I do have some questions ](https://www.reddit.com/r/txtai/comments/1b5evic/hi_pretty_new_with_txtai_framework_i_do_have_some/) , 2024-03-04-0910
```
Currently finding a candidate again for my tinyllama project (trying to stay away from langchain), I already made my ini
tial test with txtai but I do have questions

* Does this framework supports DPO Training? 

Also after training the mod
el with QLora

 

    train = HFTrainer()     
    train('TinyLlama/TinyLlama-1.1B-intermediate-step-1431k-3T',         

    pd.read_csv(data),         
    task='language-generation',         
    columns=('source', 'target'),         
   
 prefix='some prefix i put here: ',         
    maxlength=512,         
    per_device_train_batch_size=4,         
   
 num_train_epochs=500,         
    output_dir=output,         
    overwrite_output_dir=True,         
    quantize=qua
ntize, 
    lora=lora     
    )  

I got an error when I called it with the LLM class

    from txtai.pipeline import L
LM 
    llm = LLM(output) 

error: {model} does not appear to have a file named config.json. Checkout 

so yeap any help
 would be nice thank you!
```
---

     
 
all -  [ How to reduce costs when chatting with database? ](https://www.reddit.com/r/LangChain/comments/1b5ecou/how_to_reduce_costs_when_chatting_with_database/) , 2024-03-04-0910
```
I want to reduce costs when chatting with my database. Below is how it works as of now;

    const datasource = new Data
Source({
        type: 'postgres',
        url: LOCAL_DATABASE_URL,
      });
    
      const db = await SqlDatabase.fr
omDataSourceParams({
        appDataSource: datasource,
      });
    
      const llm = new ChatOpenAI({
        openAI
ApiKey: 'sk-',
        modelName: 'gpt-3.5-turbo',
      });
    
      const prompt =
        PromptTemplate.fromTempla
te(`Based on the provided SQL table schema below, write a SQL query that would answer the user's question.
    ---------
---
    SCHEMA: {schema}
    ------------
    QUESTION: {question}
    ------------
    SQL QUERY:`);
    
      const s
qlQueryChain = RunnableSequence.from([
        {
          schema: async () => db.getTableInfo(),
          question: (i
nput: { question: string }) => input.question,
        },
        prompt,
        llm.bind({ stop: ['\nSQLResult:'] }),

        new StringOutputParser(),
      ]);
    
      await sqlQueryChain.invoke({
        question: message,
      });

    
      const finalResponsePrompt =
        PromptTemplate.fromTemplate(`Based on the table schema below, question, 
SQL query, and SQL response, write a natural language response:
      ------------
      SCHEMA: {schema}
      --------
----
      QUESTION: {question}
      ------------
      SQL QUERY: {query}
      ------------
      SQL RESPONSE: {resp
onse}
      ------------
      NATURAL LANGUAGE RESPONSE:`);
    
      const finalChain = RunnableSequence.from([
     
   {
          question: (input) => input.question,
          query: sqlQueryChain,
        },
        {
          schem
a: async () => db.getTableInfo(),
          question: (input) => input.question,
          query: (input) => input.query
,
          response: (input) => db.run(input.query),
        },
        finalResponsePrompt,
        llm,
        new S
tringOutputParser(),
      ]);
    
      const finalResponse = await finalChain.invoke({
        question: message,
   
   });
    
      console.log({ message, finalResponse });

The first obvious optimisation I found is to fine-tune the m
odel with the the SQL schema before asking the question to prevent sending it over and over again.

But out of curiosity
, how does one do this at scale and for the cheapest costs possible? I'm new to LLMs and looking for a simple way for my
 SaaS users to interact with their data. Thanks!
```
---

     
 
all -  [ Is there a software to monitor performance of open-source LLMs? ](https://www.reddit.com/r/LangChain/comments/1b5dscn/is_there_a_software_to_monitor_performance_of/) , 2024-03-04-0910
```
Hello. I have been playing around with a bunch open open-source LLMs, but they all vary in terms of quality of output an
d response times. I'm wondering whether there is an open-source software to monitor the performance of such LLMs that I 
can integrate into my system.
```
---

     
 
all -  [ Suggestion for robust RAG which can handel 5000 pages of pdf ](https://www.reddit.com/r/LangChain/comments/1b5d1m7/suggestion_for_robust_rag_which_can_handel_5000/) , 2024-03-04-0910
```
I'm working on a basic RAG which is really good with a snaller pdf like 15-20 pdf but as soon as i go about 50 or 100 th
e reterival doesn't seem to be working good enough. Could you please suggest me some techniques which i can use to impro
ve the RAG with large data.

What i have done till now : 
1)Data extraction using pdf miner.
2) Chunking with 1500 size 
and 200 overlap 
3) hybrid search (bm25+vector search(Chroma db)) 
4) Generation with llama7b 

What I'm thinking of doi
ng fir further improving RAG

1) Storing and using metadata to improve vector search, but i dont know how should i extra
ct meta data out if chunk or document. 

2) Using 4 Similar user queries to retrieve more chunks then using Reranker ove
r the reterived chunks.

Please Suggest me what else can i do or correct me if im doing anything wrong :)
```
---

     
 
all -  [ Is there a good tutorial on how to setup a RAG stack application? ](https://www.reddit.com/r/LangChain/comments/1b54w8h/is_there_a_good_tutorial_on_how_to_setup_a_rag/) , 2024-03-04-0910
```
I'm an experienced software engineer new to anything involving LLM development. I've consistently believed in upskilling
 throughout my career, so I'm begining to explore how to integrate LLMs into an application. The goal is to do a learnin
g project to understand from hands on experience the pros, cons, and pitfalls of doing so.

My research so far has point
ed me to taking a RAG stack approach, since my goal is to leverage my own data with the LLM to achieve the outcome I wan
t. I have a basic understanding of what is required, however I'm hoping to find a straightforward code-a-long tutorial t
o start dipping my feet in. After that I have a whole project planned out, but I digress.

Ideally this tutorial will no
t require me to run LLama2 or something similar on my machine as I don't have the GPU power for it on my home server. I'
m willing to pay for ChatGPT and use their cheaper options for this.

Thanks in advance for any guidance you can offer.
```
---

     
 
all -  [ Implementing RAG with Langchain on AWS Bedrock ](https://www.reddit.com/r/LangChain/comments/1b51f6n/implementing_rag_with_langchain_on_aws_bedrock/) , 2024-03-04-0910
```
Hello beautiful people,

I am developing a financial chatbot using langchain and chromadb, I want to use llama2 on aws.


Right now everything is on a local project on my machine, as I am going to move from gpt to llama (cost reduction), I w
ant to use llama2 through Bedrock, is it doable to implement a RAG architecture with Langchain on that?


```
---

     
 
all -  [ How to cache LLM responses in Langchain recent versions ](https://www.reddit.com/r/LangChain/comments/1b4y6fb/how_to_cache_llm_responses_in_langchain_recent/) , 2024-03-04-0910
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

     
 
all -  [ Langchain for production  ](https://www.reddit.com/r/LangChain/comments/1b4y0pr/langchain_for_production/) , 2024-03-04-0910
```
Converting a streamlit based Langchain app with ChromaDB into a production ready app with Next js for a better UI. Apart
 from using FastAPI for asynchronous requests, how to achieve streaming within this framework? Also what are some low co
st options for the entire dev stack, what other things should I take into considering while building this ?
```
---

     
 
all -  [ Finetuning LLM with own PDFs ](https://www.reddit.com/r/LangChain/comments/1b4wa9v/finetuning_llm_with_own_pdfs/) , 2024-03-04-0910
```
Hi,

my company wants me to finetune an LLM with their own documents. I am aware of RAG an it is already running but i w
ant to see if it is possible to finetune a LLM with raw pdfs? 

So is it possible without a labeled dataset, just feedin
g the texts from the pdfs? 
```
---

     
 
all -  [ [D] What Is Your LLM Tech Stack in Production? ](https://www.reddit.com/r/MachineLearning/comments/1b4sdru/d_what_is_your_llm_tech_stack_in_production/) , 2024-03-04-0910
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

Now using a fine-tuned Llama2 70B model self hosted 
with vLLM 

**LLM Framework:**
Started with Langchain initially but found it cumbersome to extend as the app became more
 complex. Tried implementing it in LlamaIndex at some point just to learn and found it just as bad. Went back to Langcha
in and now I am in the midst of replacing it with my own logic

What is everyone else using?

Edit: correct model Llama2
 70B
```
---

     
 
all -  [ Building a open source LLM monitoring software ](https://www.reddit.com/r/LangChain/comments/1b4s7cw/building_a_open_source_llm_monitoring_software/) , 2024-03-04-0910
```
I am building an open source LLM monitoring software. I know there are bunch of other tools out there. But, what are som
e features you would like to see? I would like to solve for the ones that are not already solved by the other tools that
 exist today. 
```
---

     
 
all -  [ Maintain the chat history ](https://www.reddit.com/r/LangChain/comments/1b4rs0h/maintain_the_chat_history/) , 2024-03-04-0910
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

     
 
all -  [ Streaming with Langchain python and Next JS ](https://www.reddit.com/r/LangChain/comments/1b4r4nj/streaming_with_langchain_python_and_next_js/) , 2024-03-04-0910
```
Building an app with Langchain python  + ChromaDB + Next js. How can I perform streaming for the LLM responses? Also wha
t should the rest of my architecture look like for a production ready system? Currently built a basic PoC with streamlit
 but I am trying to move it to a more production-like Proof of concept. 
```
---

     
 
all -  [ Reflection Agents ](https://www.reddit.com/r/LangChain/comments/1b4oydd/reflection_agents/) , 2024-03-04-0910
```
Hello everyone, is there any example using reflection agents to decide if an answer is adequate or not for the user but 
using more than one tools afterwards? cause i cant find any such example
```
---

     
 
all -  [ Starting tech from scratch, should I start with langchain? ](https://www.reddit.com/r/LangChain/comments/1b4o2eg/starting_tech_from_scratch_should_i_start_with/) , 2024-03-04-0910
```
I’m a product manager by skillset but I do basic python coding, should I start with langchain? Or what should be the mos
t basic progression that I should do if I have a time frame set for 4 months
```
---

     
 
all -  [ Has anyone developed a reliable SQL agent?  ](https://www.reddit.com/r/LocalLLaMA/comments/1b4nzul/has_anyone_developed_a_reliable_sql_agent/) , 2024-03-04-0910
```
I've toyed with SQL agents or simple SQL db chains in langchain, mostly with open ai and unsuccesfully with quantized ve
rsions of SQL coder. I'm not very impressed with performance of either. GPT4 is best but struggles with nuances in schem
a, data nuances. 

Ive come across some frameworks such as Vanna ai, that claim to allow natural language to insights, d
o you have experience in this field, what insights can you share about ask questions on your data paradigm.
```
---

     
 
all -  [ [P] How do I solve this langchain error with my RAG system + huggingface model? ](https://www.reddit.com/r/LangChain/comments/1b4mj5m/p_how_do_i_solve_this_langchain_error_with_my_rag/) , 2024-03-04-0910
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

     
 
all -  [ PDF split by sections and list items ](https://www.reddit.com/r/LangChain/comments/1b4lzo9/pdf_split_by_sections_and_list_items/) , 2024-03-04-0910
```
I'm trying to analyse different pdf documents. I would like to split them by (sub)sections and list items, such that eac
h embeddings contains specific list items, part of (sub)sections in the metadata. Could someone point me to a way to spl
it the pdf docs in this way?
```
---

     
 
all -  [ Is there any way to do a query in a vector database in a related way between two documents? ](https://www.reddit.com/r/LangChain/comments/1b4h6ev/is_there_any_way_to_do_a_query_in_a_vector/) , 2024-03-04-0910
```
For example, I have a table of cars and another of spare parts, the same spare part can be related to several cars, I wo
uld like to know if there is something like this in SQL to be able to make a query with relation

```
---

     
 
all -  [ LangChain vs LlamaIndex ](https://www.reddit.com/r/ChatGPT/comments/1b4dcfg/langchain_vs_llamaindex/) , 2024-03-04-0910
```
anyone actually buitl stuff and deployed with either one or both?
```
---

     
 
all -  [ LLM conversation analytics launch (dev preview) ](https://www.reddit.com/r/LangChain/comments/1b43jr9/llm_conversation_analytics_launch_dev_preview/) , 2024-03-04-0910
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

     
 
all -  [ How do I define an output parser like a dictionary? ](https://www.reddit.com/r/LangChain/comments/1b432eh/how_do_i_define_an_output_parser_like_a_dictionary/) , 2024-03-04-0910
```
I want the output to be a nested dictionary like this

{App:{'Google':[different stuff]}

Basically hierarchical 
```
---

     
 
all -  [ Langchain based app ](https://www.reddit.com/r/LangChain/comments/1b41voa/langchain_based_app/) , 2024-03-04-0910
```
Are there any apps with a Langchain python+ Next js + Chromadb? What are my options to host with minimal cost? I have ac
cess to azure but not very good at 'cloud engineering'. I was thinking between Netflify and Vercel. Also, where would my
 chromadb vector database need to be saved to connect it to a hosted website on Netflify or any alternative? And to do r
eal-time streaming I saw many examples with langchain js but not enough with langchain python. I'm currently only using 
OpenAI API but I want to be using alternatives too in the future.

```
---

     
 
all -  [ OpenAIEmbedding and HuggingFaceInstruct also not getting highlighted ](https://www.reddit.com/r/vscode/comments/1b40z87/openaiembedding_and_huggingfaceinstruct_also_not/) , 2024-03-04-0910
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

     
 
all -  [ Is LangChain does support persisting QA objects in a specific directory in PGVector? ](https://www.reddit.com/r/LangChain/comments/1b3t27x/is_langchain_does_support_persisting_qa_objects/) , 2024-03-04-0910
```
Is LangChain does support persisting QA objects in a specific directory in PGVector?
```
---

     
 
all -  [ [Hiring] I am looking for partnership business!! ](https://www.reddit.com/r/forhire/comments/1b3oufe/hiring_i_am_looking_for_partnership_business/) , 2024-03-04-0910
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

     
 
all -  [ [Student] Year 3 CS student looking for Sofware Engineering Internships ](https://www.reddit.com/r/EngineeringResumes/comments/1b3li7l/student_year_3_cs_student_looking_for_sofware/) , 2024-03-04-0910
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

     
 
all -  [ Tutor-Bot for a class ](https://www.reddit.com/r/LangChain/comments/1b3ira0/tutorbot_for_a_class/) , 2024-03-04-0910
```
Hi,  
I'm creating a tutor bot for my class using conversational\_retrieval\_agent and  gpt-3.5-turbo-16k. The problem i
m facing is i dont want the bot to blurt out the answer, instead i want it to guide the user and refer to textbook for f
urther info. I've included this i the system message however I'm not succesful. If I ask the bot after it gives the answ
er to refer me to textbook to learn more it does however in the inital response it always blurts out the full answer. Ho
w can i prevent this?
```
---

     
 
all -  [ I created a RAG chatbot with Langchain and OpenAI designed to answer religious questions ](https://www.reddit.com/r/alphaandbetausers/comments/1b3idcq/i_created_a_rag_chatbot_with_langchain_and_openai/) , 2024-03-04-0910
```
Even though it's designed to answer questions on Islam, I think the architecture/UI is nice, and as such, would love any
 feedback.  It's also free: [aalim.chat](https://aalim.chat)

I've also been posting videos (albeit not very good ones) 
on [TikTok](https://www.tiktok.com/@aalim_chat?_t=8kInh9gpkYF&_r=1) and [IG](https://www.tiktok.com/@aalim_chat?_t=8kInh
9gpkYF&_r=1).
```
---

     
 
all -  [ Review of new memory feature vs MemGPT, Langchain etc ](https://www.reddit.com/r/ChatGPTPro/comments/1b3i61d/review_of_new_memory_feature_vs_memgpt_langchain/) , 2024-03-04-0910
```
What are your experiences with the new memory feature in ChatGPT Pro? Is it working as you expect?
```
---

     
 
all -  [ Stand-alone history library for chatbot - any exist? ](https://www.reddit.com/r/LocalLLaMA/comments/1b3dgjx/standalone_history_library_for_chatbot_any_exist/) , 2024-03-04-0910
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

     
 
all -  [ Help building RAG architecture with Gemini and pgvector-enabled Google Cloud SQL ](https://www.reddit.com/r/LangChain/comments/1b38y1z/help_building_rag_architecture_with_gemini_and/) , 2024-03-04-0910
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

     
 
all -  [ Shopify agent/tool - automating customer support ](https://www.reddit.com/r/LangChain/comments/1b361vw/shopify_agenttool_automating_customer_support/) , 2024-03-04-0910
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

     
 
MachineLearning -  [ [D] Graphs + vectordbs? Need your input: Cognee.ai . AI Data Pipelines for Real-World Production (Pa ](https://www.reddit.com/r/MachineLearning/comments/1aweo71/d_graphs_vectordbs_need_your_input_cogneeai_ai/) , 2024-03-04-0910
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

     
 
MachineLearning -  [ [D] AI projects Suggestions ](https://www.reddit.com/r/MachineLearning/comments/1aunkmw/d_ai_projects_suggestions/) , 2024-03-04-0910
```
Hi Everyone, I need a suggestion to create AI courses for students ( Hands-on AI projects). I am thinking about the late
st AI trends such as Langchain, RAG, and vector databases. In each project, there can be multiple tasks, and the main th
ing is each task should have an automated system in which we can verify whether students have done it correctly or not.


For example: Project with visualization cannot be automatically tested. 

For example: A project with visualization can
not be automatically tested. . em can verify if the length of the text is smaller we can verify that it is correct.
```
---

     
 
MachineLearning -  [ Whats in your RAG setup? [D] ](https://www.reddit.com/r/MachineLearning/comments/1apcp2w/whats_in_your_rag_setup_d/) , 2024-03-04-0910
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

     
 
deeplearning -  [ [D] WebVoyager: Navigating Digital Cosmos with LangGraph & Multimodal Models ](https://www.reddit.com/r/deeplearning/comments/1altlca/d_webvoyager_navigating_digital_cosmos_with/) , 2024-03-04-0910
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

     
 
deeplearning -  [ [D] Langchain Elevates with Step-Back Prompting using RAGatouille ](https://www.reddit.com/r/deeplearning/comments/1agtyeh/d_langchain_elevates_with_stepback_prompting/) , 2024-03-04-0910
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

     
