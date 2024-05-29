 
all -  [ Introducing MyScale Telemetry - Your Open-Source Alternative to LangSmith! ](https://www.reddit.com/r/LangChain/comments/1d2yjqe/introducing_myscale_telemetry_your_opensource/) , 2024-05-29-0911
```
In a world where LLM applications are pushing the boundaries of what's possible, observability is not just a nice-to-hav
e—it's essential for production-grade applications! Ensuring robust performance and reliability is a must, and that's ex
actly what MyScale Telemetry delivers.  
  
Say hello to the open-source alternative to LangSmith! [MyScale Telemetry](h
ttps://myscale.com/blog/myscale-telemetry-llm-app-observability/) is here to revolutionize how you trace and evaluate yo
ur LLM applications. With seamless integration with LangChain Callbacks, it's the perfect tool to diagnose issues, optim
ize performance, and understand model behavior—all with the power of open-source!  
  
MyScale Team's Commitment to Open
 Source: Our passion for contributing to the community is unwavering, and with MyScale Telemetry, we're excited to empow
er developers with the tools they need to innovate and excel.  
  
Join us on this journey to enhance your LLM applicati
ons with MyScale Telemetry. Let's shape the future of AI together, one trace at a time! 
```
---

     
 
all -  [ GPT4AllEmbeddings doesn’t work offline no way to pass a model path (any workarounds?) ](https://www.reddit.com/r/LangChain/comments/1d2xqz3/gpt4allembeddings_doesnt_work_offline_no_way_to/) , 2024-05-29-0911
```
GPT4AllEmbeddings modify model path

I'd like to modify the model path using GPT4AllEmbeddings and use a model I already
 downloading from the browser (the all-MiniLM-L6-v2-f16.gguf model, the same that GPT4AllEmbeddings downloads by default
).

I need it to create RAG chatbot completely offline.

The langchain documentation chatbot suggests me to use:

>from 
langchain\_community.embeddings **import** GPT4AllEmbeddings  
model\_path = '/path/to/your/model.bin'  
gpt4all\_embd =
 GPT4AllEmbeddings(model=model\_path)

I tried it but it does not work. It completely ignores the model path.

Is there 
something I'm missing?
```
---

     
 
all -  [ Ragatouille: A guide to get started with Retrieval-Augmented Generation (RAG) with LangChain ! ](https://www.reddit.com/r/LangChain/comments/1d2xedu/ragatouille_a_guide_to_get_started_with/) , 2024-05-29-0911
```
🚀 Exciting News! I just published a blog, Ragatouille– A guide to get started with Retrieval-Augmented Generation (RAG) 
with [LangChain](https://www.linkedin.com/company/langchain/) !

Based on Langchain's RAG from scratch series, in this c
omprehensive guide, we break down the RAG process and take you through each step to enhance and optimize your system. He
re’s a sneak peek of what you'll learn:

📌 Introduction to RAG: Understand the basics of the RAG pipeline and how it com
bines retrieval-based systems with generative models.

🔍 Query Transformation: Learn how to refine user queries for bett
er comprehension and accurate responses.

📚 Hypothetical Document Embeddings: Discover techniques for generating vector 
representations of potential documents to assess relevance.

🛤️ Routing Mechanisms: Implement intelligent routing to dyn
amically select the best data sources for your queries.

📝 Executable Queries: Master the art of translating user questi
ons into executable queries.

📂 Effective Indexing: Explore indexing strategies to enhance retrieval efficiency.

🔄 Adva
nced Retrieval Techniques: Dive into Self-RAG, Adaptive RAG, and CRAG for tailored retrieval approaches.

💡 Generation P
hase: Ensure coherent and accurate responses using the retrieved information.

🏥 Practical Application: Apply everything
 you've learned to build a sophisticated hospital management system using LangChain, LangGraph, and Neo4j.

👉 Check out:
 [https://www.sakunaharinda.xyz/ragatouille-book](https://www.sakunaharinda.xyz/ragatouille-book)

⬆️ I will be updating
 the blog soon with RAG evaluation using RAGAS and Langsmith !!! Please let me know what you guys want to appear in this
 blog, which will help fellow RAG enthusiasts 💭 I appreciate your constructive feedback and contributions !!
```
---

     
 
all -  [ Dataset Splits | LangSmith Evaluation - Part 22 ](https://www.youtube.com/watch?v=FQMn_FQV-fI) , 2024-05-29-0911
```

```
---

     
 
all -  [ Dockerize langchain/langserve applications ](https://www.reddit.com/r/LangChain/comments/1d2rq1k/dockerize_langchainlangserve_applications/) , 2024-05-29-0911
```
This is a poetry plugin to generate Dockerfile and images automatically.

This is a perfect choice if you built the Lang
chain application and you’re looking for to distribute is as microservice in the cloud. 


This project lets you generat
e a docker image or just a Dockerfile for your poetry application without manual setup

It is meant for production image
s.

[https://github.com/nicoloboschi/poetry-dockerize-plugin](https://github.com/nicoloboschi/poetry-dockerize-plugin)


[https://pypi.org/project/poetry-dockerize-plugin/](https://pypi.org/project/poetry-dockerize-plugin/)



Get started wi
th

    poetry self add poetry-dockerize-plugin@latest

This command generates a production-ready, optimized python imag
e:

    poetry dockerize

 or to generate a Dockerfile

    poetry dockerize --generate


```
---

     
 
all -  [ How to make RAG retrieve_documents chain make faster? ](https://www.reddit.com/r/LangChain/comments/1d2ooua/how_to_make_rag_retrieve_documents_chain_make/) , 2024-05-29-0911
```
Hi,

We created a chatbot with Llama2-7b-chat, RAG architecture using LangChain, Qdrant VectorDB, and for web side Djang
o. Everything works well. Additionally, our system works locally. Now the only problem is the time we get the answer. So
metimes it takes 15 seconds to return the answer from the RAG chain and it's too bad. After monitoring with LangSmith we
 saw that retrieve\_documents takes most of the run time.

Our Qdrant VectorDB collections distance type Manhattan and b
inary quantization. The embedding model is sentence-transformers/all-MiniLM-L6-v2 so the size is 384.  Also we clear the
 cache everytime. Here is the chains code and the invoke , (We write two system prompt for holding the chat history.)

 
   class RAG():
    
        def _init_(self):
            self.embed_model_id = 'sentence-transformers/all-MiniLM-L6-v2
'
            self.initializeEmbeddingModel(device)        
    
            self.model_id = 'meta-llama/Llama-2-13b-cha
t-hf'
            self.hf_auth = 'token' 
            self.initializeLLM()
    
            self.data_collection_name = 
'collection_name'
            self.db_url = 'qdrant-docker-port'
            self.initializeDBclient()
            self.
initializesearchDB()
    
            self.LLMpipeline()
            self.configSystemPrompt()
            self.RAGpipel
ine()
    
        def initializeEmbeddingModel(device):
    pass
        
        def initializeLLM(self):
    
       
     bnb_config = transformers.BitsAndBytesConfig(
                load_in_4bit=True,
                bnb_4bit_quant_typ
e='nf4',
                bnb_4bit_use_double_quant=True,
                bnb_4bit_compute_dtype=bfloat16
            )
 
           model_config = transformers.AutoConfig.from_pretrained(
                self.model_id,
                token=
self.hf_auth
            )
            self.LLMmodel = transformers.AutoModelForCausalLM.from_pretrained(
              
  self.model_id,
                trust_remote_code=True,
                config=model_config,
                quantizati
on_config=bnb_config,
                device_map='auto',
                token=self.hf_auth 
    
            )
        
    self.LLMmodel.eval()
    
        def initializeDBclient(self):
            pass
            
        def initialize
searchDB(self):
            # self.searchDB creation  
            pass      
    
        def LLMpipeline(self):
      
      
            tokenizer = transformers.AutoTokenizer.from_pretrained(
                        self.model_id,
      
                  token=self.hf_auth
                    )
            pipeline = transformers.pipeline(
               
         model=self.LLMmodel, tokenizer=tokenizer,
                        return_full_text=True,  
                    
    task='text-generation',
    
                        temperature=0.0,  
                        max_new_tokens=512, 
 
                        repetition_penalty=1.1,
                        do_sample=False
                    )
        
    self.llm = HuggingFacePipeline(pipeline=pipeline)
            
        def configSystemPrompt(self):
            
  
          # sohbet geçmişi için alt prompt ve genel system promptu tanımlıyoruz
    
            contextualize_q_system_
prompt = '''prompt'''
            self.contextualize_q_prompt = ChatPromptTemplate.from_messages(
                [
    
                ('system', contextualize_q_system_prompt),
                    MessagesPlaceholder('chat_history'),
    
                ('human', '{input}'),
                ]
            )
            qa_system_prompt = '''prompt/
        
    {context}'''
    
            self.qa_prompt = ChatPromptTemplate.from_messages(
                [
                 
   ('system', qa_system_prompt),
                    MessagesPlaceholder('chat_history'),
                    ('human', 
'{input}'),
                ]
            )
    
        def RAGpipeline(self):
            
            retriever = sel
f.searchDB.as_retriever(search_kwargs={'k':6 })
    
            history_aware_retriever = create_history_aware_retrieve
r(
                self.llm, retriever, self.contextualize_q_prompt
            )
    
            question_answer_chain
 = create_stuff_documents_chain(self.llm, self.qa_prompt)
    
            self.rag_chain = create_retrieval_chain(histo
ry_aware_retriever, question_answer_chain)
       
        def ragQA(self, question, history):
            ai_msg = self
.rag_chain.invoke({'input': question, 'chat_history': history})  
              
            return ai_msg
    
        
def clear_cache(self):
            torch.cuda.empty_cache()
            gc.collect()

LangSmith monitor result is here,


retrieval\_chain 15.71s

* retrieve\_documents 11.66s
   * HuggingFacePipeline gpt2 11.61s
   * Retriever 0.04s
* stuff
\_documents\_chain 3.96s
   * format\_inputs 0.01s
      * format\_docs 0.00s
   * HuggingFacePipeline 3.94s

So the pro
blem is mostly retrieve\_documents.  What should we do to make the system faster?

Edit:

GPU: RTX A4000, 16GB

RAM: 32 
GB

CPU: Intel® Xeon(R) W-2235 CPU @ 3.80GHz × 12

OS: Ubuntu 22.04.4 LTS
```
---

     
 
all -  [ How does an LLM orchestrator decide which agent to use in a multi-agent system? ](https://www.reddit.com/r/LangChain/comments/1d2omoe/how_does_an_llm_orchestrator_decide_which_agent/) , 2024-05-29-0911
```
Hello everyone,

I'm exploring multi-agent systems and am curious about the role of an orchestrator in managing tasks am
ong specialized agents. For instance, imagine a scenario where there are four agents, each designed to perform one of th
e basic mathematical operations: addition, subtraction, multiplication, and division.

If the orchestrator receives a qu
estion like 'How much is 4 + 4?', how does it determine which agent to send the query to? What logic or algorithms might
 it use to parse the question and delegate the task appropriately?

Additionally, if anyone could provide insights or re
sources into how such systems are generally designed or any examples of such orchestrators in action, it would be greatl
y appreciated.

Thanks in advance for your help and sharing your knowledge!


```
---

     
 
all -  [ Shopify all in on Promptfoo ](https://i.redd.it/qgg45w3d073d1.jpeg) , 2024-05-29-0911
```
I am a big fan of Promptfoo aswell. 
```
---

     
 
all -  [ [For Hire] Programmer/Web Developer/IT Consultant (Python, PHP, AI, etc.) ](https://www.reddit.com/r/forhire/comments/1d2n4lx/for_hire_programmerweb_developerit_consultant/) , 2024-05-29-0911
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

     
 
all -  [ Async streaming makes everything else harder ](https://www.reddit.com/r/LangChain/comments/1d2li6s/async_streaming_makes_everything_else_harder/) , 2024-05-29-0911
```
I find trying to do streaming makes everything else harder to do. Especially the checkpointer for message history.

This
 is my setup:

            class GraphState(TypedDict):
                question: str
                messages: Annotate
d[list, add_messages]
                documents: List[str]
    
            workflow = StateGraph(GraphState)
          
  workflow.add_node('retrieve', retrieve)
            workflow.add_node('generate', generate)
            workflow.set_e
ntry_point('retrieve')
            workflow.add_edge('retrieve', 'generate')
            workflow.add_edge('generate', E
ND)
    
            pool = AsyncConnectionPool(
                conninfo='postgresql://...',
                max_size=2
0,
            )
    
            # PostgresSaver.create_tables(pool)
    
            checkpoint = PostgresSaver( #pack
age is langchain_postgres==0.0.3
                serializer=PickleCheckpointSerializer(),
                async_connecti
on=pool,
            )
    
            app = workflow.compile(checkpointer=checkpoint)
    
            config = {
    
                'configurable': {
                            'thread_id': '1223'
                        }
            
        }
    
            async for event in app.astream_events({'messages': [('user', user_content)], 'question':     
  user_content}, config, version='v1'):
                    state = app.get_state(config) #this is the line that errors

                    try:
                        kind = event['event']
                    except:
                     
   kind = None
                    if kind and kind == 'on_chat_model_stream':
                        content = event['
data']['chunk'].content
                        if content:
                            message = {'content': content}
 
                           await self.send(text_data=json.dumps(message))

Specifically, I want to be able to use get\_s
tate() to get the document references from an answer (which is in the GraphState), as well as to do conditional interrup
t like in [this ](https://langchain-ai.github.io/langgraph/tutorials/customer-support/customer-support/#state-assistant)
Customer Service LangGraph example (which requires get\_state()).

In generral, is there a better way to handle the chec
kpointer while streaming the response?
```
---

     
 
all -  [ A library just for Document Extraction with LLMs, connector to Langchain | ExtractThinker ](https://www.reddit.com/r/LangChain/comments/1d2iubg/a_library_just_for_document_extraction_with_llms/) , 2024-05-29-0911
```
A month back I did a [post](https://www.reddit.com/r/LangChain/comments/1c6afp1/creating_a_framework_like_langchain_but_
just_for/) about creating a library just focused on Extraction for documents. Was well received here and in other places
, including by some companies. So I gave it a try.

After a month and 2k+ lines of code, I created this repo, based on t
he previous one, that will contain a full-open source code. Contains already close to 200+ (as the writing of this post)
.

[https://github.com/enoch3712/ExtractThinker](https://github.com/enoch3712/ExtractThinker)

# The motivation

Langcha
in works great integrating the several pieces **but tends to be a pain to extract data from documents and other sources*
*. ExtractThinker falls into the class of tools like instructor (pydantic outputs) and litellm (agnostic call between LL
M models), which solves a specific problem. A bit more high level yes, but the focus is the same. **Extraction for docum
ents like ORM with LLM.**

You can read in detail here:

[https://medium.com/towards-artificial-intelligence/extractthin
ker-ai-document-intelligence-with-llms-72cbce1890ef](https://medium.com/towards-artificial-intelligence/extractthinker-a
i-document-intelligence-with-llms-72cbce1890ef)

# Basic use case and idea

https://preview.redd.it/6qqufnee063d1.png?wi
dth=904&format=png&auto=webp&s=55bbd1aad1606fe6b83f4f07f338efab4deb6023

You can then use a middleware to inject the QR 
code content, and so on. I think you get the drill

# Why is this useful? Just do GPT-4o everything, use vision if neede
d

The project will focus in two things:

**Reducing the pain of leading with document extraction**

The project will ha
ndle tasks such as classifying and grouping documents. For example, it can be used to separate content within a collecti
on of PDFs with random pages.

[splitting in action](https://preview.redd.it/k10voqea063d1.png?width=1170&format=png&aut
o=webp&s=a64eaf8a015668ef85e0126226dd6e942ca53e5a)

This would give you a list already separated and extracted (e.g firs
t 2 pages invoice, last page driver's license). This classification will expand to multiple strategies and techniques.


**Reducing costs for scalability**

Build your architecture that works as well as GPT-4 with scalability and low cost. M
ore in this article:

[https://medium.com/@enoch3712/how-companies-use-llms-to-process-4-000-cvs-for-1-extractthinker-3f
a0815057c3?sk=7fe626701a203135370e95f68bcb59f1](https://medium.com/@enoch3712/how-companies-use-llms-to-process-4-000-cv
s-for-1-extractthinker-3fa0815057c3?sk=7fe626701a203135370e95f68bcb59f1)

Just finished the final touches for the code, 
and it's a real use case that worked out great using inexpensive quantized models from deepinfra.

**The code still not 
production-ready and missing most of the features, but will make more sense with templates once i build the documentatio
n.**

I intend to eventually integrate this into langchain to be used as **pypdf**.

If you can assist me with features 
as issues, use cases, or if anyone is interested in giving it a try, I would greatly appreciate it.

Thank you for your 
time.
```
---

     
 
all -  [ A 'new' Object & Vector Database for Python ](https://www.reddit.com/r/Python/comments/1d2iq74/a_new_object_vector_database_for_python/) , 2024-05-29-0911
```
[ObjectBox](https://objectbox.io/python-on-device-vector-and-object-database-for-local-ai/) ([GitHub](https://github.com
/objectbox/objectbox-python)) is an embedded database for Python objects and high-dimensional vectors. Today is it's fir
st stable release for Python developers. It's very lightweight similar to SQLite, but built for objects so it's faster a
s there's no SQL layer in-between. It's the very first vector database that also runs on smaller low-memory devices. The
 article comes with first benchmarks and hints at the LangChain integration.
```
---

     
 
all -  [ Building an Autonomous AI Agent with LangChain and PostgreSQL pgvector ](https://www.reddit.com/r/YugabyteDB/comments/1d2ic8q/building_an_autonomous_ai_agent_with_langchain/) , 2024-05-29-0911
```
Discover how to create a fully autonomous AI travel agent, capable of finding listings and managing bookings, using Lang
Chain, OpenAI, PostgreSQL, and pgvector, with YugabyteDB as the underlying database. Click to learn how to build your ow
n AI agent backed by PostgreSQL, using components available in today’s ecosystem. 

[https://www.yugabyte.com/blog/build
-autonomous-ai-agent-with-langchain-and-postgresql-pgvector/](https://www.yugabyte.com/blog/build-autonomous-ai-agent-wi
th-langchain-and-postgresql-pgvector/)
```
---

     
 
all -  [ LLM to get the relevant table from db  ](https://www.reddit.com/r/LangChain/comments/1d2i9fr/llm_to_get_the_relevant_table_from_db/) , 2024-05-29-0911
```
Hey guys ! I have Azure OpenAI GPT 4 LLM connected to Azure SQL DB. When I use this command db.get\_usable\_table\_names
() must return all the tables available, how every I'm getting the names of the ones that are dbo.table\_name

https://p
review.redd.it/fw1477bhu53d1.png?width=334&format=png&auto=webp&s=55b2f27dd632bf0c984eb3f71b22d7f8d052071c

https://prev
iew.redd.it/rwqeu6nku53d1.png?width=377&format=png&auto=webp&s=ca4eaeffdebd441b75ad22122f3e4798ecc67ae3

The tables in m
y db are as follows:

Question 1:How can I have the llm return all the available tables ?  
Question 2: Let's say I prom
pt the llm like 'Aggregate what age group customers prefer what products.' This prompt has two tables: Customer and Prod
uct. So I want the llm to join these two tables, and generate a response. So we want the llm to go through multiple tabl
es and give a response.   
How can I achieve this?   
Thanks for your help !
```
---

     
 
all -  [ CopilotKit v0.9.0 (MIT) - open source framework for building in-app AI agents ](https://www.reddit.com/r/LocalLLaMA/comments/1d2i4cz/copilotkit_v090_mit_open_source_framework_for/) , 2024-05-29-0911
```
I am a contributor to [CopilotKit](https://github.com/CopilotKit/CopilotKit), an open-source AI copilot framework for bu
ilding in-app AI copilots & in-app agents. 

I wanted to share some of the improvements we shipped in the latest release
: 

1. GPT-4o & native voice support + integration with Gemini. 
2. Node Llama CCP [support](https://github.com/CopilotK
it/CopilotKit/issues/238). 
3. LangChain Adapter: build in-app agents that can see realtime application context and take
 in-app action. Connect with any LLM. 
4. Generative UI: chatbot can stream generated UI components as specified by the 
developer & the LLM.
5. Copilot suggestions: auto suggestions of new questions for the end-user to ask with generative U
I. These can be manually controlled by the programmer, and also informed by GPT intelligence for the given context.

---


The library is fully open-sourced under MIT license and self hosted.  We're still looking for more things to add, happ
y to hear your thoughts :)

[https://github.com/CopilotKit/CopilotKit](https://github.com/CopilotKit/CopilotKit)
```
---

     
 
all -  [ Kernel crashes for FAISS similarity search ](https://www.reddit.com/r/LangChain/comments/1d2gxqi/kernel_crashes_for_faiss_similarity_search/) , 2024-05-29-0911
```
Hi, I am working with langChain right now and created a FAISS vector store. Since today, my kernel crashes when running 
a similarity search on my vector store. Has anyone an idea why this is happening?

    from langchain_community.document
_loaders import PyPDFLoader
    from langchain_community.vectorstores import FAISS
    
    f = open('credentials.txt')

    OPENAI_API_KEY = f.read()
    embeddings_model = OpenAIEmbeddings(api_key=OPENAI_API_KEY)
    
    document_loader =
 PyPDFLoader('filename.pdf')
    text_splitter=RecursiveCharacterTextSplitter()
    documents = document_loader.load_and
_split(text_splitter)
    
    vectorstore = FAISS.from_documents(documents, embeddings_model)
    vectorstore.similarit
y_search('query')

MacBook Pro intel, python 3.9, jupyter notebook, langchain 0.2.0
```
---

     
 
all -  [ Need to Build Custom LLM - Expert Needed ](https://www.reddit.com/r/LangChain/comments/1d2g20b/need_to_build_custom_llm_expert_needed/) , 2024-05-29-0911
```
Hello everyone! I'm in the process of developing a custom LLM for my startup. I'm looking for help and would appreciate 
it if anyone on this forum has experience with this and would be willing to meet via Zoom to discuss it further.
```
---

     
 
all -  [ How to make RAG chain faster so we get answer faster ](https://www.reddit.com/r/LangChain/comments/1d2eooc/how_to_make_rag_chain_faster_so_we_get_answer/) , 2024-05-29-0911
```
We created a chatbot with Llama2-7b-chat, RAG architecture using LangChain, Qdrant VectorDB, and for web side Django. Ev
erything works well. Even we hold the chat history. Now the only problem is the time we get the answer. Sometimes it tak
es 15 seconds to return the answer from the RAG chain and it's too bad.

What should we do to make the system faster?

I
f it's necessary I can share some of the codes.

Edit:

We are running all system in local. Because system have to be in
 local. Also we are running in GPU.

GPU: RTX A4000, 16GB

RAM: 32 GB

CPU: Intel® Xeon(R) W-2235 CPU @ 3.80GHz × 12

OS
: Ubuntu 22.04.4 LTS

  
We realized that retrieving from the DB chain is taking the most time of the work. Actually, we
 configured it with some parameters like collection is now with Manhattan distance, 384 size (because of the embedded mo
del), and binary quantization. We read that binary is x40 faster. But could we make more configuration?

https://preview
.redd.it/30knup1kq63d1.png?width=1918&format=png&auto=webp&s=8faf69a2a62d5e628fd46c4da9f909a3d5838c09

https://preview.r
edd.it/bedycqvkq63d1.png?width=1916&format=png&auto=webp&s=8ab2aec755a0e58f155026d49d9c4442b408e90b


```
---

     
 
all -  [ I just made a OpenAI ChatGPT MacOS Clone for Windows and Ubuntu and MIT licenced ](https://www.reddit.com/r/GPT4/comments/1d2eep5/i_just_made_a_openai_chatgpt_macos_clone_for/) , 2024-05-29-0911
```
# Explanation and Reason

Hi i am python developer and after OpenAI GPT-4o launch, i just i little bit angry because the
 app that they talked about just work in MacOS and a joke, it will come to windows november lol. Come on bro, if there i
s API, developers like us can make this app and release in just few days with langchain agent and tool infrastructure.


So i just release our GPT-4o clone and its totaly usable. You can use to take meeting notes, writing code and copying to
 your clipboard, or read and remember your calendar. There is unlimited possibilities.

# Current Features

* \*\*Screen
 Read\*\*
* Microphone
* \*\*System Audio\*\*
* Memory

--

* \*\*Clipboard\*\*
* Search Engines
* \*\*Python and SH Int
erpreters\*\*
* Writing and Running Scripts
* Using your Telegram Account
* Knowledge Management

# Open Call to devs

I
f there is some people to interest and develop this and adding some features just like auto take screen shot each 5 seco
nd and say somethings if something wrong. We can open a **GitHub Organization** and develop together. Just for open-sour
ce, just for competition.

https://preview.redd.it/vcbo2sw4l43d1.png?width=656&format=png&auto=webp&s=29c11615550af7eebd
caa7cdaf31d2c986536a44

[onuratakan/gpt-computer-assistant: gpt-4o Desktop Personel Asisstant (github.com)](https://gith
ub.com/onuratakan/gpt-computer-assistant)
```
---

     
 
all -  [ Embedding comparison between tensorflow and HF models for local processing? ](https://www.reddit.com/r/LocalLLaMA/comments/1d2dxzq/embedding_comparison_between_tensorflow_and_hf/) , 2024-05-29-0911
```
I am trying to figure out what is the resulting difference of embedding model in HF vs tensorflow. Langchain allows both
. Is it really worth to even be concerned about it if the difference is negligible.

For e.g BAAI/bge-base-en-v1.5 vs te
nsorflow embedding
```
---

     
 
all -  [ Knowledge Graphs and long-term memory ](https://www.reddit.com/r/LangChain/comments/1d2dwpo/knowledge_graphs_and_longterm_memory/) , 2024-05-29-0911
```
I'm working on a project that needs to create long term memory with a knowledge graph. Does anyone have any experience w
ith any specific libraries to achieve this?
```
---

     
 
all -  [ Agent permission ](https://www.reddit.com/r/LangChain/comments/1d2cezb/agent_permission/) , 2024-05-29-0911
```
What do you use to handle agents permissin to retrieve access certain data?
Let's say your building an agent in a large 
org. How do you make sure it can access finance question if you asked it a question about finance. It needs to validate 
if you are permitted to access that kind of data.
```
---

     
 
all -  [ Llm hardware setup? ](https://www.reddit.com/r/LocalLLM/comments/1d29kpf/llm_hardware_setup/) , 2024-05-29-0911
```
Sorry the title is kinda wrong, I want to build a coder to help me code. The question of what hardware I need is just on
e piece of the puzzle.

I want to run everything locally so I don't have to pay apis because I'd have this thing running
 all day and all night.

I've never built anything like this before.

I need a sufficient rig: 32 g of ram, what else? I
s there a place that builds rigs made for LLMs that doesn't have insane markups?

I need the right models: llama 2,13 b 
parameters, plus maybe code llama by meta? What do you suggest?

I need the right packages to make it easy: ollama, crew
ai, langchain. Anything else? Should I try to use autogpt?

With this in hoping I can get it in a feedback loop with the
 code and we build tests, and it writes code on it's own until it gets the tests to pass.

The bigger the projects get t
he more it'll need to be able to explore and refer to the code in order to write new code because the code will be long 
than the context window but anyway I'll cross that bridge later I guess.

Is this over all plan good? What's your advice
? Is there already something out there that does this (locally)?
```
---

     
 
all -  [ Python-LLM - Session 3 - LangChain - Multi Agent - Supervisor - Agent - Query Mutual Funds Data ](https://www.reddit.com/r/u_SravzLLC/comments/1d2665z/pythonllm_session_3_langchain_multi_agent/) , 2024-05-29-0911
```
**# Use Case**

Use LangChain Multi Agent: Supervisor Agent (JSON & Pandas Agents) to Query Mutual Funds Data



**## Se
ssion 3**

- LangChain - Multi Agent - Retrieval Augmented Generation

- JSON Agent and Pandas Agent Integration

- Supe
rvisor - Agent set up

- Sample Queries







Documentation Link: [https://docs.sravz.com/docs/tech/python/langchain/#s
ession-3](https://docs.sravz.com/docs/tech/python/langchain/#session-3)

Source Code: [https://gist.github.com/sravzpubl
ic/80ce4e6ad8168e9271195a1a5a433c09](https://gist.github.com/sravzpublic/80ce4e6ad8168e9271195a1a5a433c09)

Video Explan
ation: [https://youtu.be/rGjrQhDstyE](https://youtu.be/rGjrQhDstyE)



Sravz LLC Training Series:

Analytics - [https://
docs.sravz.com/docs/analytics/](https://docs.sravz.com/docs/analytics/)

Tech - [https://docs.sravz.com/docs/tech/](http
s://docs.sravz.com/docs/tech/)



#cpp #c++  #cors   #boost #beast  #http #cmake #make #python #langchain #openai #llm
```
---

     
 
all -  [ Agent enters a loop of continuous tool calling without exiting and providing a final answer ](https://www.reddit.com/r/LangChain/comments/1d24j6j/agent_enters_a_loop_of_continuous_tool_calling/) , 2024-05-29-0911
```
Hey guys! I'm trying to build a chatbot that offer video games recommendations using LangGraph.

Right now, I was workin
g on the agent called 'Game Search Agent' which objective is to search the web for the best results to the user query.


Problem is, the execution never moves from this node to the \_\_end\_\_ one. It will always be stuck in a loop, where th
e tool function is called without providing a concrete final answer in the end.

Can somebody please take a look at this
 code snippet and tell me please what's wrong? Thank you!

    from typing import Annotated, List
    from langchain_ope
nai import ChatOpenAI
    from langchain_community.tools.tavily_search import TavilySearchResults
    from langchain_cor
e.prompts import PromptTemplate
    from langchain_core.messages import BaseMessage
    from typing_extensions import Ty
pedDict
    
    from langgraph.graph import StateGraph
    from langgraph.graph.message import add_messages
    from la
nggraph.prebuilt import ToolNode, tools_condition
    
    os.environ['TAVILY_API_KEY'] = 'your_api_key'
    os.environ[
'OPEN_AI_KEY'] = 'your_api_key'
    
    class AgentState(TypedDict):
        messages: Annotated[List[BaseMessage], add
_messages]
        query: str
        games: List[str]
    
    
    tool = TavilySearchResults(max_results=2)
    tools
 = [tool]
    llm = ChatOpenAI(model='gpt-4o', temperature=0)
    llm_with_tools = llm.bind_tools(tools)
    
    
    d
ef game_title_search(state: AgentState):
        game_search_prompt = PromptTemplate(
        template='''You are part o
f a chatbot that provides personalized video game recommendations based on user preferences. \n
        Your task is to 
search for video games that match the user query, using the Tavily API. \n
        Only return the titles of the games. 
\n
        The number of games to return is limited to 5. \n\n
    
        The results provided will STRICTLY look as f
ollows (Python list): \n
        ['game_title_1', 'game_title_2', 'game_title_3', ...] \n\n
    
        User Query: {qu
ery}''',
        input_variables=['query'],
    )
        game_search = game_search_prompt | llm_with_tools
        
   
     return {'messages': [game_search.invoke({'query': state['query']})]}
    
    
    graph_builder = StateGraph(Agent
State)
    graph_builder.add_node('game_search', game_title_search)
    
    tool_node = ToolNode(tools=[tool])
    grap
h_builder.add_node('tools', tool_node)
    
    graph_builder.add_conditional_edges(
        'game_search',
        tool
s_condition,
    )
    
    graph_builder.add_edge('tools', 'game_search')
    graph_builder.set_entry_point('game_searc
h')
    graph = graph_builder.compile()
    
    while True:
        user_input = input('User: ')
    
        if user_i
nput.lower() in ['quit', 'exit', 'q']:
            print('Goodbye!')
            break
        
        for event in gra
ph.stream({'messages': [user_input], 'query': user_input}, {'recursion_limit': 150}):
            for value in event.val
ues():
                if isinstance(value['messages'][-1], BaseMessage):
                    print('Assistant:', value[
'messages'][-1].content)
```
---

     
 
all -  [ Hashing/Masking sensitive data before sending out to OpenAI ](https://www.reddit.com/r/LangChain/comments/1d1v710/hashingmasking_sensitive_data_before_sending_out/) , 2024-05-29-0911
```
I'm using OpenAI GPT 3.5 turbo for summarising data from sensitive documents, which contains some of my personal informa
tion. Currently, I'm manually removing some of the sensitive data from the inputs. I want to know if LangChain or any ot
her tool/library handles this automatically without me getting involved?
```
---

     
 
all -  [ [6 YOE] Layoffs incoming, 300 app 1 interview, seeking advice for the American Dream with no degree ](https://www.reddit.com/r/EngineeringResumes/comments/1d1svsi/6_yoe_layoffs_incoming_300_app_1_interview/) , 2024-05-29-0911
```
Hi everybody,

I'm located in Italy and I'm targeting FAANG, big tech company, pharmaceutical and startups in US  
I'm t
argeting Software Engineer and AI Engineer jobs as I have experience in AI and doing University courses about Deep Learn
ing/AI

I've also applied to some position in Mexico (got interview for Amazon there but failed onsite, the recruiter wi
ll reach out to try again next year) and Canada with no luck so far

I’m looking to relocating to the US (ideally in Aus
tin/San Antonio Area to be closer to my fiance family and have a decent salary but I’m open to anywhere in the US) or as
 second option Mexico/Canada  
I know the market is super bad at the moment but Layoffs have been announced in my curren
t company (is gonna take \~2 month to know if I'm getting fired but I want to be prepared)

I have a couple of doubts

*
 should I mention in a summary section that I need  visa sponsorship or I can work as contractor remotely (from Mexico f
or EST hours or from Italy)? Are any FANG level company hiring contractor on a regular basis? (in the previous version o
f the CV I putted Italian Citizenship and Italy as location but I got some feedbacks that is not great so I removed in t
his one)
* I was contacted by a US Google recruiter 2.5 years ago, but at that time I wasn't looking to move, so I decli
ned after the phone interview. Should I reach out to him, or has it been too long?
* I never finished the degree, I've f
rozen my career at last semester to start working, should I write incomplete?
* Finishing the Degree will help passing t
he cv screen or after 6 years of experience is not relevant anymore?

A couple of years ago I was contacted by Meta (don
e first interview but position was filled 1 week before my onsite) Amazon and Microsoft, now I'm only getting auto rejec
t/position filled emails

Currently I have 1 interview for a contractor role (based in LATAM ) for a company in Austin a
nd they will consider the fact that I'm willing to relocate there

I'm not sure if I'm missing something important here 
or if my experience is not relevant for the US market

Thanks for any advice you might have and have a good day :)

&#x2
00B;

https://preview.redd.it/05c4fs2bcz2d1.png?width=5100&format=png&auto=webp&s=d2ea06120ea9b0bfc4270b8a3cf4f89a648382
3f
```
---

     
 
all -  [ How do the langchain integrations retrieve relevant documents? ](https://www.reddit.com/r/LangChain/comments/1d1spe6/how_do_the_langchain_integrations_retrieve/) , 2024-05-29-0911
```
Looking at the following tool: [https://python.langchain.com/v0.1/docs/integrations/tools/google\_drive/](https://python
.langchain.com/v0.1/docs/integrations/tools/google_drive/)

What happens under the hood when this tool is called? For qu
eries to find relevant results, does langchain simply make use of the public API which is based on a fullText search?

A
ny way to retrieve documents with a semantic search with langchain?  I think this would actually be a quite neat feature
, so we could pass an embedding model, db and it would create embeddings for all the documents.
```
---

     
 
all -  [ LLM to generate dashboard ](https://www.reddit.com/r/LangChain/comments/1d1qll4/llm_to_generate_dashboard/) , 2024-05-29-0911
```
Hey all, I have a dataset in Azure and I have a SQL LLM. Now I want to generate visuals when a user gives a prompt. How 
can I implement this ??? 
Any help would be great 
```
---

     
 
all -  [ Can we use both LangChain & LlamaIndex together for our LLM application? ](https://www.reddit.com/r/ArtificialInteligence/comments/1d1qglm/can_we_use_both_langchain_llamaindex_together_for/) , 2024-05-29-0911
```
I think, we can strategically integrate these two in the Retrieval-Augmented Generation (RAG) pipeline. 

In the first h
alf of the RAG pipeline, you can utilize LlamaIndex for efficient data ingestion, indexing, and retrieval. 

LlamaIndex 
provides tools to ingest and structure large volumes of data from various sources, such as text documents, PDFs, and web
pages. It supports different indexing strategies, including vector embeddings and tree-based indexing, allowing you to c
hoose the most appropriate method for your data and use case. 

Once the data is indexed, LlamaIndex's efficient retriev
al mechanisms can quickly retrieve relevant information based on user queries or prompts.

In the second half of the RAG
 pipeline, you can leverage LangChain's powerful capabilities for prompt engineering, chaining, and task decomposition. 


LangChain's prompt engineering utilities can be used to craft effective prompts that incorporate the relevant data ret
rieved from LlamaIndex's indexed sources. This can lead to more context-aware and data-driven prompts, improving the qua
lity of language model outputs. 

Additionally, LangChain's chaining and task decomposition features can be employed to 
break down complex queries into subtasks, with LlamaIndex providing relevant data for each subtask. This can enable more
 accurate and comprehensive responses by combining information from multiple sources. 

Furthermore, LangChain's Agents 
and Tools concept can be leveraged to delegate subtasks to different tools or services, including LlamaIndex's data retr
ieval mechanisms, enabling a modular and extensible approach to building RAG applications.

So, the point is, it is not 
always a LangChain vs. LlamaIndex story, it can also be LangChain & LlamaIndex story. 

But at the end, all I have is on
e doubt, is it going to be a good workflow or using both will be an overkill? Let me know your thoughts in the comments.

```
---

     
 
all -  [ Help creating a conversational assistant ](https://www.reddit.com/r/LangChain/comments/1d1nduq/help_creating_a_conversational_assistant/) , 2024-05-29-0911
```
Newbie question here, How do I make a conversational LLM assistant in Streamlit that remembers all the chats but does no
t have to give a system prompt for each inference?  
I know I can use the conversational buffer memory of langchain for 
chat memory, but I do not want to waste my tokens on system prompts for each inference.

Generally, for each inference, 
my app takes system prompt + chat context as input for each output. I was wondering if there is a way to reduce the toke
n consumption by sending the system prompt once and making the model remember it for the entire session.

Thank you.


```
---

     
 
all -  [ need some advice on rag ](https://www.reddit.com/r/LangChain/comments/1d1mexn/need_some_advice_on_rag/) , 2024-05-29-0911
```
I need to build a tool for my fin research where if i ask in NLP to a rag i need the output of those 100PDFs i have uplo
aded to the RAG. it needs to be able to build charts, graphs and make sense of 100 other things. any OS tool like that> 
or any suggestions on the stack i should use? please advice. 
```
---

     
 
all -  [ Roast my Resume , please! ](https://i.redd.it/cq8h2vx6cx2d1.jpeg) , 2024-05-29-0911
```
This resume hasn't been getting me any interviews, so instead of just letting my confidence falter without knowing why a
nd never hearing from employers. Why don't you guys roast my resume and actually let me know why so I can actually do so
mething about it.


```
---

     
 
all -  [ How to integrate conversation context and retrieved documents for a new query for a RAG LLM chatbot  ](https://www.reddit.com/r/LangChain/comments/1d1attd/how_to_integrate_conversation_context_and/) , 2024-05-29-0911
```
Hi Community,  
I am building a chatbot app for a specific domain. I am leveraging aws bedrock for storing documents and
 creating embeddings in pinecone vector db.

But I fee like I am conceptually stuck in how to maintain the conversation 
context and retrieved documents when trying to create a response for a new query.  How to decide when to use the context
 and when to make a fresh retrieval? Appreciate any help here.

Please help answer in the setup of Django for rest, bedr
ock for s3 and embedding model, pinecone for vector db.
```
---

     
 
all -  [ Awesome prompting techniques ](https://i.redd.it/qpe806ybzt2d1.jpeg) , 2024-05-29-0911
```
https://arxiv.org/pdf/2312.16171v2
```
---

     
 
all -  [ Seeking Comprehensive Resources for Mastering Generative AI Fundamentals
 ](https://www.reddit.com/r/generativeAI/comments/1d1a29d/seeking_comprehensive_resources_for_mastering/) , 2024-05-29-0911
```
Hi everyone,

I'm actively learning generative AI and have been exploring resources like videos and GitHub code. While I
'm comfortable with Python, I find there's a gap in foundational knowledge. Many resources jump straight into code imple
mentation without explaining the 'why' behind library choices or providing smaller, foundational examples. This makes it
 difficult to understand the underlying concepts and modify the code effectively.

I'm particularly interested in gainin
g a deep understanding of how generative AI integrates with tools like Gemini, OpenAI, and Langchain. Additionally, the 
rapid evolution of libraries and commands (changing every six months or so) makes it challenging to stay current.

My go
al is to build a solid foundation in generative AI fundamentals so I can confidently create my own applications.

Would 
anyone recommend resources, especially books, that provide a comprehensive introduction to generative AI concepts? I'm l
ooking for a top-down approach that emphasizes core principles.

I am looking for a book or material that provides step-
by-step examples of using Python for generative AI. This will help me build a strong foundation, allowing me to understa
nd it thoroughly and create my own applications.

Thank you in advance for your suggestions!
```
---

     
 
all -  [ How can I  keep track of document source being used in a prompt ? ](https://www.reddit.com/r/LangChain/comments/1d18agq/how_can_i_keep_track_of_document_source_being/) , 2024-05-29-0911
```
Hi ,

I am using Langchain/Gemini1.5/Google Documents AI to OCR, to parse and ask questions to a set of documents. Worki
ng pretty sweet. Actually just published my side project here: [https://zdocs.ai/](https://zdocs.ai/)

I would like to b
e able to show where the answers to a prompt that is restricted to an uploaded set of documents are coming from?

Google
 Documents has the whole document structure availabe in JSON. However, I am not sure if the LLM (gemini in my case) can 
actually provide insights opn where the answer came from ?

Any tips would be welcome !

Cheers, 
```
---

     
 
all -  [ How to only take query relevant memory from Upstash? ](https://www.reddit.com/r/LangChain/comments/1d0xhn5/how_to_only_take_query_relevant_memory_from/) , 2024-05-29-0911
```
I want the chat to be able to access all the information from the memory without it passing all the memory to the prompt
. Is there a way to only pass the memories from the database to the prompt that are important for answering the query or
 to summarize the memory according to each prompt once again? 
```
---

     
 
all -  [ Restarting Crewai / Langchain flow at a particular point with new variables. ](https://www.reddit.com/r/LangChain/comments/1d0tsk2/restarting_crewai_langchain_flow_at_a_particular/) , 2024-05-29-0911
```
Hi guys,  
I am new to Python, so there might be a straightforward solution for this.

I am building a digital assistant
 chatbot that communicates with customers via WhatsApp. The chatbot processes messages using a series of functions imple
mented with Crewai and Langchain that may take several seconds to minutes to complete. While the processing is ongoing, 
new messages from the customer may arrive, requiring the chatbot to:

1. **Pause the current processing**.
2. **Incorpor
ate the new message** into the ongoing process.
3. **Restart the processing** from a specific function within the sequen
ce, using updated information.

I will use Flask to receive webhooks with new messages from WhatsApp.

My problem is tha
t I don't know the exact way to build this with Python. Specifically, I need to determine how to stop and restart the sc
ript at a particular point. I will use a large language model (LLM) to decide the exact point to restart the process, (a
 crewai task, or maybe an entire crew), incorporating the new buyer message.

I don't have the code yet as I am currentl
y working on the architecture of the system.

Any suggestions will be of great help.

Thank you!
```
---

     
 
all -  [ Restarting Python flow at a particular point with new variables. ](https://www.reddit.com/r/learnpython/comments/1d0tk7z/restarting_python_flow_at_a_particular_point_with/) , 2024-05-29-0911
```
Hi guys,   
I am new to Python, so there might be a straightforward solution for this.

I am building a digital assistan
t chatbot that communicates with customers via WhatsApp. The chatbot processes messages using a series of functions impl
emented with Crewai and Langchain that may take several seconds to minutes to complete. While the processing is ongoing,
 new messages from the customer may arrive, requiring the chatbot to:

1. **Pause the current processing**.
2. **Incorpo
rate the new message** into the ongoing process.
3. **Restart the processing** from a specific function within the seque
nce, using updated information.

I will use Flask to receive webhooks with new messages from WhatsApp.

My problem is th
at I don't know the exact way to build this with Python. Specifically, I need to determine how to stop and restart the s
cript at a particular point. I will use a large language model (LLM) to decide the exact point to restart the process, (
a crewai task, or maybe an entire crew), incorporating the new buyer message.

I don't have the code yet as I am current
ly working on the architecture of the system.

Any suggestions will be of great help.

Thank you!
```
---

     
 
all -  [ Extract text from PDF maintaining partitions ](https://www.reddit.com/r/LangChain/comments/1d0ryqx/extract_text_from_pdf_maintaining_partitions/) , 2024-05-29-0911
```
Hello,

I want to extract paragraphs, title etc from a PDF while.maintaining the separation boundaries. What library to 
use?
```
---

     
 
all -  [ Am I doing something wrong in my code? ](https://www.reddit.com/r/LangChain/comments/1d0q4g6/am_i_doing_something_wrong_in_my_code/) , 2024-05-29-0911
```
Hey guys, I am using langchain to generate structured output, but for some reason, the output is not properly formatted 
json so when I run json.loads(), it gives me an error. I tried to make a clean\_response function but there are too many
 edge cases to consider. Am I using the wrong function to get the LLM output? Thanks in advance!

Here is my code:

    
from abc import ABC
    import os
    import pydantic
    from langchain_groq import ChatGroq
    from langchain.pydanti
c_v1 import validator
    from langchain.output_parsers import PydanticOutputParser
    from langchain.prompts import Pr
omptTemplate
    from langchain.pydantic_v1 import BaseModel
    
    import json
    from dotenv import load_dotenv
   
 
    load_dotenv()
    
    tags_req = ['HS Seniors Only', 'Need Based', 'Merit Based', 'Essay Required', 'US Citizen',
 'Arts',  'STEM', 'Community Service', 'Leadership']
    class Tags(BaseModel):
        tags: list[str]
        @validat
or('tags')
        def must_use_only_these_values(cls, v):
            for tag in v:
                if tag not in tags_
req:
                    raise ValueError(f'tag {tag} is not in {tags_req}')
            return v
    
        
    
   
 class Description(BaseModel):
        description: str
    
    class Generator(ABC):
        def __init__(self ) -> No
ne:
            pass
    
        def generate(self, *args):
            pass
    
    
    class GroqGenerator(Generato
r):
        def __init__(
            self,
        ):
            super().__init__()
            self.llm = ChatGroq(
 
               temperature=0.1,
                groq_api_key=os.getenv('GROQ_API_KEY'),
                model_name='mixt
ral-8x7b-32768',
            )
    
        def generate(
            self,
            name,
            available,
   
         opens,
            closes,
            details,
            description,
            need_based,
            me
rit_based,
        ):
            msg1 = (
                 f'Name: {name}\nAvailable: {available}\nOpens: {opens}\nClos
es: {closes}\nDetails: {details}\nDescription: {description}\nNeed Based: {need_based}\nMerit Based: {merit_based}\n\n G
enerate Below: '
            )
            msg2 = (
                 f'\nName: {name}\nAvailable: {available}\nOpens: {o
pens}\nCloses: {closes}\nDetails: {details}\nDescription: {description}\nNeed Based: {need_based}\nMerit Based: {merit_b
ased}\n\n Generate Below: ',
            )
            tags = self.inference(msg1, Tags)['tags']
            desc = self
.inference(msg2, Description)['description']
            return tags, desc
        
        def inference(self, msg, pyd
antic_object):
            parser = PydanticOutputParser(pydantic_object=pydantic_object)
            if pydantic_object
.__class__.__name__ == 'Tags':
                prompt = PromptTemplate(
                    template='Please follow the 
instructions of the following user query.\n{format_instructions}\n{query}\n',
                    input_variables=['quer
y'],
                    partial_variables={'format_instructions': parser.get_format_instructions() + f' Make sure only 
generate the array from this bank of tags and no other tags: {tags_req}'},
                )
            else:
         
       prompt = PromptTemplate(
                    template='Please follow the instructions of the following user query
.\n{format_instructions}\n{query}\n',
                    input_variables=['query'],
                    partial_variabl
es={'format_instructions': parser.get_format_instructions()},
                )
            _input = prompt.format_promp
t(query=msg)
            response = self.llm.invoke(_input.to_string()).content
            cleaned_response = self.clea
n_response(response)
            print(cleaned_response)
            return json.loads(cleaned_response)
        
      
  def clean_response(self, response):
            # Replace curly quotes and other problematic characters
            re
sponse = response.replace('“', ''').replace('”', ''')
            response = response.replace('‘', ''').replace('’', '''
)
            return response
    
        def test(self, msg):
            return self.inference(msg)
    
    
    if 
__name__ == '__main__':
        groq = GroqGenerator(['scholarship'])
        print(groq.test('Q: What is a scholarship?
 A:'))
    
```
---

     
 
all -  [ Help! 'Recursion limit' when trying to use chain with 'llm.bind_tools' - LangGraph ](https://www.reddit.com/r/LangChain/comments/1d0om4f/help_recursion_limit_when_trying_to_use_chain/) , 2024-05-29-0911
```
Hey guys. I'm trying to get comfortable with LangGraph in an attempt to then develop a chatbot based on this framework. 
 
When trying to test the idea of a node in my chatbot, I found myself faced with this error.  
Could somebody please he
lp me understand what's wrong with my code and how can I solve this problem?  
I would be truly thankful!

The code:

  
  from typing import Annotated, List
    from langchain_openai import ChatOpenAI
    from langchain_community.tools.tavi
ly_search import TavilySearchResults
    from langchain_core.prompts import ChatPromptTemplate, PromptTemplate
    from 
langchain_core.messages import BaseMessage
    from typing_extensions import TypedDict
    
    from langgraph.graph imp
ort StateGraph, END
    from langgraph.graph.message import add_messages
    from langgraph.prebuilt import ToolNode, to
ols_condition
    
    # Define AgentState class with the proper typing
    class AgentState(TypedDict):
        message
s: Annotated[List[BaseMessage], add_messages]
        query: str
        games: List[str]
    
    # Initialize the tool
 and LLM
    tool = TavilySearchResults(max_results=3)
    tools = [tool]
    llm = ChatOpenAI(model='gpt-3.5-turbo', te
mperature=0)
    llm_with_tools = llm.bind_tools(tools)
    
    # Define the function for the game title search
    def
 game_title_search(state: AgentState):
        game_search_prompt = PromptTemplate(
        template='''You are part of 
a chatbot that provides personalized video game recommendations based on user preferences. \n
        Your task is to se
arch for video games that match the user query, using the Tavily API. \n
        Only return the titles of the games. \n

        The number of games to return is limited to 5. \n\n
    
        The results provided will look as follows (Pyt
hon list): \n
        ['game_title_1', 'game_title_2', 'game_title_3', ...]
    
        User Query: {query}''',
       
 input_variables=['query'],
    )
        game_search = game_search_prompt | llm_with_tools
    
        game_search_res
ult = game_search.invoke({'query': state['query']})
    
        return {'messages': [game_search_result]} # Also, I nee
d to extract the game titles from the tool's results and update the state attribute 'games' - how can I do this?
    
  
  # Build the graph
    graph_builder = StateGraph(AgentState)
    graph_builder.add_node('game_search', game_title_sear
ch)
    
    tool_node = ToolNode(tools=[tool])
    graph_builder.add_node('tools', tool_node)
    
    graph_builder.ad
d_conditional_edges(
        'game_search',
        tools_condition,
    )
    
    graph_builder.add_edge('tools', 'gam
e_search')
    graph_builder.set_entry_point('game_search')
    graph = graph_builder.compile()
    
    # Define the in
itial state
    input_state = {
        'messages': [],
        'query': '',
        'games': []
    }
    
    user_inp
ut = 'What games are similar to The Witcher 3?'
    input_state['query'] = user_input
    input_state['messages'] = [('u
ser', user_input)]
    
    output = graph.invoke(input_state, config={'recursion_limit': 50})
    print(output)
    
  
  
    
```
---

     
 
all -  [ How do you go about creating a RAG chatbot using Graph and Vector on internal documents? ](https://www.reddit.com/r/LangChain/comments/1d0j0hc/how_do_you_go_about_creating_a_rag_chatbot_using/) , 2024-05-29-0911
```
When you are making RAG chatbots using Graph and Vectors how are you storing the internal data? What’s the general appro
ach?

For example, say you are asked to ingest all your companies files, like word docs PDFs and everything in between. 
If you use RAG with Graph and Vector embeddedings where are you storing the data from the documents? I’m curious what th
e general approach is to chunking, tokenizing, and embedding are?

If you had to ingest your companies documents using a
 RAG, Graph, and vector approach how would you set this up? What would the schema be of the Graph, where would the vecto
rs be stored?

Thanks
```
---

     
 
MachineLearning -  [ [R] Building an Observable arXiv RAG Chatbot with LangChain, Chainlit, and Literal AI ](https://www.reddit.com/r/MachineLearning/comments/1crwh0q/r_building_an_observable_arxiv_rag_chatbot_with/) , 2024-05-29-0911
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

     
 
MachineLearning -  [ [P] LLMinator: A Llama.cpp + Gradio based opensource Chatbot to run llms locally(cpu/cuda) directly  ](https://www.reddit.com/r/MachineLearning/comments/1cpbgd1/p_llminator_a_llamacpp_gradio_based_opensource/) , 2024-05-29-0911
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

     
