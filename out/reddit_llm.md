 
all -  [ Hello, looking for some help ](https://www.reddit.com/r/LLMDevs/comments/1c2ndao/hello_looking_for_some_help/) , 2024-04-13-0909
```
This is my first time working with an LLM, I am trying to build a super simple project to gain some experience, just try
ing to build the simplest python script that uses an LLM that I can. 

\-I was using MSVS 2022, it kept giving me a hard
 time saying that it couldnt find what I was trying to import (for example, import torch, never worked, or import langch
ain) Does anyone know why? Or is it best if I just avoid MSVS all together? 

Since then I have learned how to use Jupyt
er notebook, and have made it past that issue.

\- I am following tutorials, and they keep coming up with outdated model
s. This (and others I have tried) model keeps giving a huge error, from what I can tell it is because it is no longer su
pported. Does anyone know a more up to date model that I can use? Or can you see anything else wrong with this code that
 may be causing it not to run. 

&#x200B;

Thanks for the help, I know I am very novice here, other than this, small cod
ing projects are really my main experience.  (CSE 100, leetcode, etc) I know that this is a big step, but I am trying to
 follow this tutorial to dip my toes in just a little bit. Any tips to help me get past this obstacle and get my first p
rogram to run? 

https://preview.redd.it/d9n0fg43t4uc1.png?width=789&format=png&auto=webp&s=c3d50fff4d54984be0f9da5eaeb6
98a6b9abfa71
```
---

     
 
all -  [ Best embedded models for transcriptions/spoken language? ](https://www.reddit.com/r/LangChain/comments/1c2l33u/best_embedded_models_for_transcriptionsspoken/) , 2024-04-13-0909
```
Hello I would like to know which embedded model would be best suited for transcriptions of mostly recorded zoom sessions
 / spoken language. I would like to ask specific questions about topics that were covered. Getting detailed answers and 
summaries.

Currently I am using:

Salesforce/SFR-Embedding-Mistral -> which is pretty slow on my Macbook M1 Pro

mixedb
read-ai/mxbai-embed-large-v1

Are there better models suited for my task?
```
---

     
 
all -  [ About ELECTRA ](https://www.reddit.com/r/LangChain/comments/1c2kdwz/about_electra/) , 2024-04-13-0909
```
I don't understand why it's better for ELECTRA to use the alternate token detection task instead of the MLM task while M
LM in Bert still replaced token with 10%. Can you explain it to me?
```
---

     
 
all -  [ Langchain + gemini ](https://www.reddit.com/r/googlecloud/comments/1c2hi10/langchain_gemini/) , 2024-04-13-0909
```
We've been working on a bot using langchain and vertex's gemini  as an llm.

We get a lot of [content has no parts] erro
r in a very random way.

The safety settings are all at block none and still happens.

We're working on spanish.

Has an
yone else been getting these errors?


```
---

     
 
all -  [ Burr: an OS framework for building and debugging AI applications faster ](https://www.reddit.com/r/mlops/comments/1c2du1c/burr_an_os_framework_for_building_and_debugging/) , 2024-04-13-0909
```
[https://github.com/dagworks-inc/burr](https://github.com/dagworks-inc/burr)

Hey folks! I wanted to share out something
 we've been working on that I think you might get use out of. We initially built it for internal use but wanted to share
  with the world. 

The problem we're trying to solve is that of logically modeling systems that use ML/AI (foundational
 models, etc...) to make decisions (set control flow, decide on a model to query, etc...), and hold some level of state.
 This is complicated -- understanding the decisions a system makes at any given point requires tons of instrumentation, 
etc...

We've seen a lot of different tools that attempt to make this easier (DSPY, langchain, superagents, etc...), but
 they're all very black-box and focused on one specific case (prompt management). We wanted something that made debuggin
g, understanding, and building up applications faster, without imposing any sort of restrictions on the frameworks you u
se or require jumping through hoops to customize.

We came up with Burr -- the core idea is that you represent your appl
ication as a state machine, can visualize the flow live as it is going through, and develop and test components separate
ly. It comes with a telemetry UI for local debugging, and the ability to checkpoint, gather data for generating test cas
es/eval, etc...

We're really excited about the initial reception and are hoping to get more feedback/OS users -- feel f
ree to DM me or comment here if you have any questions, and happy developing!

PS -- the name *Burr* is a play on the pr
oject we OSed called [Hamilton](https://github.com/dagworks-inc/hamilton) that you may be familiar with. They actually w
ork nicely together!
```
---

     
 
all -  [ Difference between ReAct and OpenAI functions Agent type ](https://www.reddit.com/r/LangChain/comments/1c2cnuo/difference_between_react_and_openai_functions/) , 2024-04-13-0909
```
Title

I can see that in ReAct, there's thought-action(which tool)-output. What does it do in when the type is openai_fu
nctions? Like how does it choose the tools in that case? I wanna understand the internal difference
```
---

     
 
all -  [ machine learning  engineer ](https://i.redd.it/iwb03k2nf2uc1.jpeg) , 2024-04-13-0909
```

```
---

     
 
all -  [ How do people typically debug TypeError in LCEL ? ](https://www.reddit.com/r/LangChain/comments/1c2bq58/how_do_people_typically_debug_typeerror_in_lcel/) , 2024-04-13-0909
```
I know how to use set_debug or LangSmith to see what happens in each step of an LCEL chain when it does run. But sometim
es I'll change a bunch of stuff, and my chain won't run at all anymore. I'll just get an error like:

    TypeError: uns
upported operands type(s) for |: 'dict' and 'function'

This error points to the first line of the chain, which isn't ve
ry helpful for understanding where exactly in the chain the problem is, especially if that chain has a bunch of steps. I
s there a good way to debug and diagnose these errors?

This is an issue that I keep running into with non-trivial chain
s.
```
---

     
 
all -  [ Training own embedding model for custom use-case ](https://www.reddit.com/r/LangChain/comments/1c2a8bi/training_own_embedding_model_for_custom_usecase/) , 2024-04-13-0909
```
Hi all,

At my company, we want to automate some RAG-related process, and we are using LangChain. We will have access to
 some human-verified data, that matches up certain questions with passages from PDF documents. Now to improve the perfor
mance of our tool, I thought it might be useful to fine-tune the embeddings model somehow, as opposed to using the 'defa
ult' Azure OpenAI embeddings that are available. 

From what I gather online, most ways of training such a model would i
nvolve having pairs of sentences, and ranking their similarity. The problem is that in our data set, we only have 'perfe
ct matches' so to say. Would I still be able to meaningfully train my own embeddings model, and how? Sources or code exa
mples are very much welcome.
```
---

     
 
all -  [ Has anyone used the Re-ranker API from Cohere with one a LangChain retriever that isn't the base one ](https://www.reddit.com/r/LangChain/comments/1c29o79/has_anyone_used_the_reranker_api_from_cohere_with/) , 2024-04-13-0909
```
Every example I see online with the Cohere re-ranker, uses the base vector store retriever as the retriever.

&#x200B;


It does not use ensemble, or parent document, or multi query etc. Any help appreciated.
```
---

     
 
all -  [ Help with semantic chunker ](https://www.reddit.com/r/LangChain/comments/1c27lkv/help_with_semantic_chunker/) , 2024-04-13-0909
```
Hi all!

  
I am building a RAG system for my private/work related files. Followed some guidelines and got a basic versi
on running.

Naturally i wanted to step up my game and change the recursive character splitter with the 'SemanticChunker
'. Script will be below. I am running in some struggles i cant seem to find the answers on while searching around.

Impo
rt things in my situation: 

* Everything needs to run local
* PDF data
* Dutch text

The language part makes it the mos
t difficult i feel. Tried various LLMS but seem to run in a 'killed' when i try to create the database when i attempt to
 use huggingfaceembeddings for 'multilingual-e5-large-instruct' or 'BGE-M3' which are supposed to be multilangual embedd
ing models.

What does work is using olloma and mistral 7B instruct for example.

So far my questions are:

* Can you us
e any LLM for the SemanticChunker?
* Is a language specific LLM/embedding model a hard requirement?
* Is it possible/nee
ded to use a different LLM for the SemanticChunker and creating the vectorDB?
* Will an LLM ike mistral instruct V2 even
 provide decent results?
* Any examples/pointers?

Any advice and tips is much appreciated! Thanks in advance!



`impor
t os`

`from langchain_community.llms import Ollama`

`from langchain_community.vectorstores import Chroma`

`from langc
hain.text_splitter import RecursiveCharacterTextSplitter`

`from langchain.chains import RetrievalQA`

`from langchain_c
ommunity.document_loaders import TextLoader`

`from langchain_community.document_loaders import PyPDFLoader`

`from lang
chain_community.document_loaders import DirectoryLoader`



`from InstructorEmbedding import INSTRUCTOR`

`from langchai
n_community.embeddings import HuggingFaceInstructEmbeddings`



`from langchain_community.embeddings import OllamaEmbedd
ings`

`from langchain_community.embeddings import HuggingFaceEmbeddings`

`from transformers import AutoTokenizer, Auto
Model`

`from langchain_community.embeddings import HuggingFaceBgeEmbeddings`

`from langchain_experimental.text_splitte
r import SemanticChunker`



`### Load and process the text files`

`loader = DirectoryLoader('/MEDIA/NHG/test/', glob='
./*.pdf', loader_cls=PyPDFLoader)`

`documents = loader.load()`



`#### here we are using OpenAI embeddings but in futu
re we will swap out to local embeddings`

`#ollama = OllamaEmbeddings(base_url='http://192.168.1.141:11434', model='nomi
c-embed-text')`

`ollama = OllamaEmbeddings(base_url='http://192.168.1.141:11434', model='mistral:instruct')`

`#model =
 HuggingFaceEmbeddings(model_name='intfloat/multilingual-e5-large-instruct')`

`#model = HuggingFaceBgeEmbeddings(model_
name='BAAI/bge-m3', model_kwargs={'device': 'cpu'}, encode_kwargs={'normalize_embeddings': True})`



`###splitting the 
text`

`#text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)`

`text_splitter = SemanticC
hunker(ollama)`

`texts = text_splitter.split_documents(documents)`

`print('Lengte van de teksten semantic:', len(texts
)) #Voor feedback`



`### Embed and store the texts`

`persist_directory = './ChromaDB'`

`vectordb = Chroma.from_docum
ents(documents=texts, embedding=ollama, persist_directory=persist_directory)`

`vectordb.persist()`

`vectordb = None`


`print('DB gemaakt')`
```
---

     
 
all -  [ Return the tool output without any modifications ](https://www.reddit.com/r/LangChain/comments/1c24si0/return_the_tool_output_without_any_modifications/) , 2024-04-13-0909
```
Hi,

I integrated dall-e into my chat application using this class: [https://js.langchain.com/docs/integrations/tools/da
lle](https://js.langchain.com/docs/integrations/tools/dalle)  


It works fine, somehow and the URL is returned. But Ope
nAI makes modifications to the result. It always seems to shorten the URL and removes query parameters.

I tried to chan
ge the result a little bit, but no success:

    protected async _call(arg: string): Promise<string> {
        try {
   
       const result = await this.wrapper.invoke(arg);
    
          return `Return the following URL. Do not change it.
 <URL>${result}</URL>`;
        } catch (error) {
          return 'Failed';
        }
      }

I am actually not sure, 
if it is really OpenAI that removes the query parameters, but who else could it be? It seems to be a general topic: [htt
ps://community.openai.com/t/gpt-changing-the-response-url/555778](https://community.openai.com/t/gpt-changing-the-respon
se-url/555778)  


So I would be happy if I could just bypass the LLM for these tool calls or find another solution. I c
ould also base64 encode the URL and decode it later or something like that, but I have not tried it yet.
```
---

     
 
all -  [ Langchain rag with ChatGoogleGenerativeAI Error ](https://www.reddit.com/r/LangChain/comments/1c21u43/langchain_rag_with_chatgooglegenerativeai_error/) , 2024-04-13-0909
```
Hello,

How do I fix the following?

    Invalid argument provided to Gemini: 400 Please ensure that multiturn requests 
alternate between user and model.Invalid argument provided to Gemini: 400 Please ensure that multiturn requests alternat
e between user and model.

I am trying to contextualize the query before similarity search on qdrant so the query is ref
ormulated for similarity search to work properly based on chat history.

Here is how I've formulated the chat history




`chat_history_messages = chat_history.chat_mesages.values_list(`

`'message', 'sender'`

`).order_by('created_at')`

`f
or message, sender in chat_history_messages:`

`if sender == 'bot':`

`chat_history_messages_rag_format.append(AIMessage
(content=message))`

`else:`

`chat_history_messages_rag_format.append(`

`HumanMessage(content=message)`

`)`

Here's h
ow im trying to call the llm

     contextualize_q_system_prompt = '''Given a chat history and the latest user question 
\
                which might reference context in the chat history, formulate a standalone question \
                w
hich can be understood without the chat history. Do NOT answer the question, \
                just reformulate it if ne
eded and otherwise return it as is.'''
    
                template = ChatPromptTemplate.from_messages(contextualize_q_
system_prompt)
    
                # context = ''
    
                chain = template | llm
                chat_hist
ory_messages_rag_format.pop()
    
                print(chat_history_messages_rag_format)
                response = ch
ain.invoke(
                    {'context': chat_history_messages_rag_format, 'question': query}
                )
    

                query = response

The array which is being passed to 'context' key looks like this: \[HumanMessage(conte
nt='Why cells'), AIMessage(content='Histograms are very simple to quickly understand your data, which tell about values 
of data like central tendency, dispersion, outliers, etc. thanks for asking!')\]

NOTE: I have no idea what I'm doing. I
'm not an AI developer, don't understand the basics. I'm just a backend dev thrown into this, so any help would be nice.

```
---

     
 
all -  [ MODERATION TOPIC / LLM OPENAI ](https://www.reddit.com/r/LangChain/comments/1c1p30i/moderation_topic_llm_openai/) , 2024-04-13-0909
```
How do you add moderation to your models; for example limit to my model to only answer question relationated with Life S
cience and Health.
```
---

     
 
all -  [ RAG Q/A | PDF Conversation | Langchain | OpenAI ](https://www.reddit.com/r/LangChain/comments/1c1o7nj/rag_qa_pdf_conversation_langchain_openai/) , 2024-04-13-0909
```
HELP: How can I make a rag Q/A app that allows the user to upload a pdf to the conversation and so that the model can un
derstand the context of the pdf; I tried to perform an ensemble retrievel but at some point the chunks lose the context 
of the entire pdf
```
---

     
 
all -  [ Chainlit Copilot mode: Embed your LangChain Agent as a copilot on a website or software ](https://www.reddit.com/r/LangChain/comments/1c1m2jb/chainlit_copilot_mode_embed_your_langchain_agent/) , 2024-04-13-0909
```
You can now build your AI agent in Python using LangChain and OpenAI and embed it - as a chatbot or copilot - in an exis
ting software 🔥

📞 Function Calling: your Copilot can even take actions on the website    
🌠 Widget UI & UX customisatio
n    
🔐 CORS & Authentication to manage who can access the copilot

Simply add event listeners to your code to have the 
agent interact with the software!

It unlocks many use cases:  Customer Support Chatbots, Lead Generation Chatbots or So
ftware Copilots & more

Docs: [https://docs.chainlit.io/deployment/copilot](https://docs.chainlit.io/deployment/copilot)
  
Example: [https://github.com/Chainlit/cookbook/tree/main/copilot](https://github.com/Chainlit/cookbook/tree/main/copi
lot)
```
---

     
 
all -  [ Improving the summarisation capability of LLM - will LangChain help? ](https://www.reddit.com/r/LangChain/comments/1c1ltfp/improving_the_summarisation_capability_of_llm/) , 2024-04-13-0909
```
I'm building a Summarizer, or you can say it's a kind of report generation for fraudulent transactions (fraud not confir
med, but just alerted) using LLM. I'm using OpenAI GPT-4 to perform the summarization task. I've tried my best to improv
e the prompt to generate the best summary/report with insights into the data. Some of these improvements include:

1. Pr
oviding metadata of the tables involved.
2. Assigning a role to the LLM.
3. Providing a few-shot examples on how to gene
rate the summary.

Currently, I'm not using LangChain for the summarization task. However, **are there any other techniq
ues that can generate the summary/report in a better way without losing the context? Will LangChain help me in improving
 the summary?** 

&#x200B;

PS: I'm a newbie to this field, please pardon me if there is any mistake in my explanation.
```
---

     
 
all -  [ Tables context length issue in RAG ](https://www.reddit.com/r/LangChain/comments/1c1lsk6/tables_context_length_issue_in_rag/) , 2024-04-13-0909
```
I am trying to create a PDF RAG chatbot for RFP. Extracted text using pypdf and extracted tables using tabula..now tryin
g to create a multimodal RAG using ChromaDB.  
tables im trying to summarise using Llama2 with prompt to preserve relati
onship between rows and columns   
text I split using recursive text splitter  
i add both to RAG   
but i feel the tabl
e insertion into RAG isnt correct for proper QA  
kindly guide me 
```
---

     
 
all -  [ Langchain + Pydanctic + OpenAI : pydantic.v1.error_wrappers.ValidationError: 1 validation error for  ](https://www.reddit.com/r/LangChain/comments/1c1l8zp/langchain_pydanctic_openai_pydanticv1error/) , 2024-04-13-0909
```
    from langchain_openai import ChatOpenAI
    from langchain_openai import OpenAIEmbeddings
    from langchain.chains 
import RetrievalQA
    from langchain_mongodb import MongoDBAtlasVectorSearch
    from langchain.output_parsers import P
ydanticOutputParser
    from langchain.prompts import PromptTemplate
    from src.models.steps import Steps
    
    
  
  def get_steps(query, mongo_uri, mongo_db_name):
        vector_store = MongoDBAtlasVectorSearch.from_connection_string
(
            mongo_uri,
            mongo_db_name + '.' + 'taskVectors',
            OpenAIEmbeddings(disallowed_specia
l=()),
            index_name='default',
        )
    
        llm = ChatOpenAI(model='gpt-3.5-turbo')
    
        par
ser = PydanticOutputParser(pydantic_object=Steps)
    
        prompt = PromptTemplate(
            template='Answer the
 query attached very precisely, give the output in the structure specified. '
                     'Just say no if you d
on't find the answer in current context. '
                     'You have to map every field in structure to the appropr
iate value. '
                     'For example to map elementId you should see from the output what is the value of key
 elementId from '
                     'the context. '
                     'You will find it like this ...\'elementId\'
: \'Go to Page 2\',.... '
                     'So you will map Go to Page 2 to elementId in the structure. '
          
           'If you find multiple actionElements return all of them in the particular structures, '
                     
'remember final output is gonna be multiple objects '
                     'Also for the scrollDetails field, populate a
n array, even if there is one or no object, it should '
                     'be an array of those objects, like this '

                     '...\'listView\': \'index\': 0, \'scrollOffsetX\': 0..... should be populated as '
                
     '[...\'viewId\': \'listView\', \'offsets\': \'x\': 0, \'y\': 405 ....]'
                     'This is very crucial,
 wrong answers can cause serious problems.'
                     + '\n{format_instructions}\n{query}\n',
            inp
ut_variables=['query'],
            partial_variables={'format_instructions': parser.get_format_instructions()},
       
 )
    
        chain = prompt | llm | parser
    
        retriever = vector_store.as_retriever(
            search_typ
e='similarity',
            search_kwargs={'k': 25},
        )
    
        qa = RetrievalQA.from_chain_type(llm=chain, 
chain_type='stuff', retriever=retriever, return_source_documents=True)
        retriever_output = qa.invoke(query)
     
   return retriever_output

  
I added pydantic output parser to this function to parse my output in a particular struct
ure, and I think everything almost works correctly, the output I get is:  
`{'text': Steps(root=[Action(elementId='Go to
 Page 2', position=Position(x=252, y=100, width=116, height=48), value='Go to Page 2', scrollDetails=[ScrollDetail(viewI
d='mainScrollLayout', offsets=Offsets(x=0, y=0))], viewName='MainActivity'), Action(elementId='showBottomSheetButton', p
osition=Position(x=20, y=630, width=352, height=48), value='Show Bottom Sheet', scrollDetails=[ScrollDetail(viewId='main
ScrollLayout', offsets=Offsets(x=0, y=0))], viewName='MainActivity'), Action(elementId='backButton', position=Position(x
=16, y=96, width=88, height=48), value='Back', scrollDetails=[ScrollDetail(viewId='listView', offsets=Offsets(x=0, y=405
))], viewName='PageActivity')])}`

`Steps` is a `RootModel`  that should have an array of `Actions`, which is correct, b
ut I am getting this unidentified model `Generation` on top of steps which has this field `text` as you see in the outpu
t which expects a string, and hence the validation fails with error:  


`pydantic.v1.error_wrappers.ValidationError: 1 
validation error for Generation`

`text`

  `str type expected (type=type_error.str)`

  
Not sure where this `Generatio
n` model is coming from, I tried making `Steps` a `BaseModel`, still the same issue.  


How do I get this Generation ou
t of the way? Or what can I do to fix this?  
I am fairly new to `Langchain` and `OutputParsers`
```
---

     
 
all -  [ Best library/framework for parsing PDF documents with table inside? ](https://www.reddit.com/r/LangChain/comments/1c1ksv6/best_libraryframework_for_parsing_pdf_documents/) , 2024-04-13-0909
```
Hello, me and my team were looking for integrate inside our RAG company model the most decent pdf parser, we need one th
at can also parse tables and schemes and keep the information intact (or at least not completely broken when it will be 
sent to the vector database). We already tried Pypdf, pdfPlumber, Unstructured and Nougat, but all of these libraries we
ren't good enough for our needs. Do you guys know any other alternative?
```
---

     
 
all -  [ Multivector RAG for drugs pdf, missing context, I need help ](https://www.reddit.com/r/ChatGPTCoding/comments/1c1klmk/multivector_rag_for_drugs_pdf_missing_context_i/) , 2024-04-13-0909
```
We are developing an RAG (Retrieval-Augmented Generation) system based on Elasticsearch and Langchain (Python users) for
 processing PDF files containing drug information. Our solution includes the following components:

* Layout-Based Parti
tioning: We utilize LLMSherpa for text partitioning and Textract for isolating tables.
* Chunk Summary Encoding: We empl
oy a history-aware multivector retrieval strategy based on semantic similarity exclusively.
* Response Generation: OpenA
I models.

We are encountering challenges in identifying relevant chunks for users' queries. Sometimes, the drug name is
 not explicitly mentioned in the chunk, making it too generic. This presents the following potential issues:

* The chun
k may always be retrieved, leading to constant answers even when the drug is changed.
* The chunk may never be retrieved
 due to its vagueness, making explicit drug-related chunks yield more coherent results even if they are not relevant.

A
re there any retrieval or partition strategies to address our problem?
```
---

     
 
all -  [ Building and Deploying a MinIO-Powered LangChain Agent API with LangServe ](https://www.reddit.com/r/minio/comments/1c1jopp/building_and_deploying_a_miniopowered_langchain/) , 2024-04-13-0909
```
Building on these insights, we now turn our focus to [LangServe](https://blog.langchain.dev/introducing-langserve/?ref=b
log.min.io), a pivotal tool in transitioning LangChain applications from development to deployment, simplifying the proc
ess of launching production-ready APIs.

[https://blog.min.io/minio-powered-langchain-agent-with-langserve/](https://blo
g.min.io/minio-powered-langchain-agent-with-langserve/)
```
---

     
 
all -  [ How do you discover tools/ideas that might help improve your LLM-based apps which are not RAG? ](https://www.reddit.com/r/LangChain/comments/1c1g07n/how_do_you_discover_toolsideas_that_might_help/) , 2024-04-13-0909
```
Hi!

I'm new to LLM-based applications and mainly just trying stuff for fun and learning to improve my skills and knowle
dge but I was wondering how do you discover ideas/tools that can help improve your way of interacting between data and L
LMs in applications which are not RAG, for which I find there are a lot of resources. I have done some simple use case t
hat works pretty well when everything is fine, but also breaks a lot, but overall it didn't require me some deep knowled
ge of the space and I'm feeling like I can improve a lot upon my initial code by solving these issues using what people 
in the space developed or thought of for that. I'm not talking about tools and ideas for RAG which are very abundant, bu
t for all the other applications that don't require the level of sophistication RAG applications do.

My use case is ext
racting structured data from documents. I have coded a small python program to which I give a document (.pdf or .txt) an
d I give it a query (a string, in natural language) that's intended to extract structured data from these documents and 
put it into a JSON. For example if my document talks about different startups, how much capital they've raised etc., I c
an ask 'extract the names of the startups the document is talking about and how much capital they've raised in their fir
st series' and get a JSON that contains that.

I consider this a simple use case, it's not a RAG use case, it's a simple
 use case of, at least how I think of it, 'chunking => LLM call => output cleaning' but I want to either go beyond that 
if it's possible or explore better ideas to do each of these small steps (like are there ways to do better chunking that
 the traditional ones of recursive text splitting etc.?). I feel like just trying to do this in any other way without us
ing LLMs can already be a great step for me but I don't know where to look at.
```
---

     
 
all -  [ Open Source Function-Hub for Agent Tools | crewAI - LangChain - Autogen ](https://www.reddit.com/r/LocalLLaMA/comments/1c1d8sd/open_source_functionhub_for_agent_tools_crewai/) , 2024-04-13-0909
```
Hi, i built an open source mit licensed project for storing function in a place with automatic documentation and CPU ram
 analye itself. Also its provide automaticaly dependency extraction and installation.

&#x200B;

You can create your own
 hubs with docker. [https://github.com/Upsonic/Tiger](https://github.com/Upsonic/Tiger)

&#x200B;

&#x200B;

https://pre
view.redd.it/90mueks2butc1.png?width=1847&format=png&auto=webp&s=da6289d97c2d423e6a7d9dd019af2b66dd6d0ca3
```
---

     
 
all -  [ We summarised Harrison Chase's talk on the evolution of AI agents and their applications ](https://www.reddit.com/r/LangChain/comments/1c1c0md/we_summarised_harrison_chases_talk_on_the/) , 2024-04-13-0909
```
Hey! We summarised Harrison Chase's talk on the evolution of AI agents and their applications during AI Ascent. Maybe it
 will be useful for you as well:

He identified 3 critical areas of development:

* Planning
* UX
* Memory

1. Planning:


Chase highlighted the need for AI agents to plan strategically beyond basic action and feedback loops, which current l
anguage models struggle with for complex tasks.

He discussed the ongoing research and development efforts to enhance pl
anning capabilities, like external prompting strategies and cognitive architectures. Are these just short-term fixes or 
essential long-term requirements for AI agent development?

2. User Experience (UX):

Chase is particularly enthusiastic
 about the user experience (UX) of interacting with AI agents. He emphasizes that achieving a balance between human invo
lvement and agent autonomy is essential for effective application.

He discussed innovative UX features such as the abil
ity to rewind and edit agent actions, which enhance reliability and control over the agent's decisions. These developmen
ts aim to make agents more user-friendly and adaptable to specific user needs and corrections.

3.  Memory:

Memory is a
 key area for advancement in AI agents. Two essential types are procedural memory (task performance) and personalized me
mory (user preferences or facts).

He provided examples of how agents could use memory to enhance their interactions, su
ch as adapting communication styles based on previous interactions or recalling personal details to personalize conversa
tions.

What's next for AI agents?

Full talk: https://www.youtube.com/watch?v=pBBe1pk8hf4&list=PLOhHNjZItNnOoPxOF3dmq30
UxYqFuxXKn&index=7
```
---

     
 
all -  [ Having issues with Manual install after installing the requirements ](https://www.reddit.com/r/ankibrain/comments/1c17wba/having_issues_with_manual_install_after/) , 2024-04-13-0909
```
ive managed to enter the virtual environment but after installing everything via pip and reopening Anki the AnkiBrain wi
ndow does not appear. Any idea where would the logs be to debug this?

&#x200B;

&#x200B;

https://preview.redd.it/yrp0q
joykstc1.png?width=1881&format=png&auto=webp&s=3d7efb4bba2afa672b00721da05b304b2c788fc9
```
---

     
 
all -  [ What resources should I use to become an expert in LLM based applications/chatbots?  ](https://www.reddit.com/r/LangChain/comments/1c17gld/what_resources_should_i_use_to_become_an_expert/) , 2024-04-13-0909
```
I am beginning to LLM World. i am playing with Langchain, ollama for few problems. What is the best way to learn these? 

How do I approach for the same. I tried few YouTube videos but they just tell how to use this function, that function n
o one goes deep or explain why this is needed. 
What is the best way to learn llm? 

For reference, I am trying to creat
e a chatbot, which classifies intent of a sentence then based on intent it will call the api for operation or call the l
lm for answer. 
For intent classification I am using llama2 model, and trying to get intent in json format. But it somet
imes give intent in nin json format. How to make sure llama2 gives answer in json format only. 
```
---

     
 
all -  [ Can Langchain JS handle everything Python version can? ](https://www.reddit.com/r/LangChain/comments/1c127nu/can_langchain_js_handle_everything_python_version/) , 2024-04-13-0909
```
I am currently deciding on a backend technology to use for my AI backend app. I will be looking into implementing/utiliz
ing RAG, Background jobs for data loading, OAuth etc.

NestJS is a pretty good backend choice these days for the same bu
t I am just worried if Langchain JS is as good as Python Langchain as the documentation of Python version is awesome com
pared to JS.   


So first question, can Langchain JS handle everything Python version can and only the documentation is
 lacking?  


I love FastAPI's developer experience and how lightweight it is and I would like to stick with it if in Py
thon ecosystem due to Langchain but I am worried I will have to do too much work from scratch that Django already handle
s. (Note I will be using AWS wherever I can so does it really matter?)  


So yeah, second question, if using Langchain 
JS, which is more recommended, Django or FastAPI for an AI heavy app? I hate Django's learning curve but is it worth it 
compared to FastAPI?

&#x200B;
```
---

     
 
all -  [ NestJS vs Django vs FastAPI for backend development with AI ](https://www.reddit.com/r/webdev/comments/1c121ra/nestjs_vs_django_vs_fastapi_for_backend/) , 2024-04-13-0909
```
I am planning on a tech stack for an app which will be heavy on the AI side and here are the things I can think of imple
menting/utilizing: Langchain, RAG, Async jobs, OAuth.   


Just FYI, I plan on relying on cloud providers for the most p
arts other than the backend service as I would like to handle customizations.   


Which backend technology is the best 
in this scenario? NestJS is really good and kind of checks all boxes for me (scalability, TS support, etc) but I am a bi
t sus about langhcain.js as it's documentation is lacking compared to the Python version.  


Django is technically pyth
on equivalent of Nest but one, I am not a big fan of Django due to the high learning curve. But the ORM, admin console a
re some cool things out of the box. Plus Python langchain!

FastAPI is just awesome for fast development but I am worrie
d I will be looking at implementing too many things from scratch just because other than async jobs/auto-swagger documen
tation.   


Here's the stack I plan to use (if this helps):  
**Backend**: Nest.js (leaning most towards this but let's
 see based on opinions), langchain  
**DB**: GraphQL, Apollo, Prisma, AWS  
**Hosting:** Vercel/AWS  
**Frontend:** Flut
ter/Dart mobile app, Next or React + Vite web app + Jotai/Zustand for state management.
```
---

     
 
all -  [ Display charts and images generated from a python agent ](https://www.reddit.com/r/LangChain/comments/1c10vvb/display_charts_and_images_generated_from_a_python/) , 2024-04-13-0909
```
Hello everyone,  
I'm working on a chatbot app (frontend React +backend Python with fastAPI), and I'm using a python age
nt to generate some graphs and charts for the users. However, the frontend and the backend are hosted in different conta
iners for security purposes, so I can't use the native save image on python and return the location of the image (as it'
s gonna be on the backend container that is isolated from the frontend one so I won't be able to access it).   
How can 
I solve this problem?   
Thanks in advance
```
---

     
 
all -  [ Langchain Cache - Any way to define a custom cache key? ](https://www.reddit.com/r/LangChain/comments/1c0y53d/langchain_cache_any_way_to_define_a_custom_cache/) , 2024-04-13-0909
```
e.g. like this:  
[https://docs.litellm.ai/docs/caching/redis\_cache#custom-cache-keys](https://docs.litellm.ai/docs/cac
hing/redis_cache#custom-cache-keys)  


would be nice to have non-hash keys e.g, for searching in Redis GUI
```
---

     
 
all -  [ Advice needed on orchestrating a multi-agent conversational AI with chat history retention ](https://www.reddit.com/r/LangChain/comments/1c0xi7a/advice_needed_on_orchestrating_a_multiagent/) , 2024-04-13-0909
```
I'm looking for guidance on creating a multi-agent conversational AI that can dynamically switch between specialized age
nts based on the user's needs, while retaining the full conversation history to provide a personalized experience.

The 
high-level idea is:

* When the user asks a question or makes a request, the conversational AI analyzes the input to det
ermine which specialized agent is best suited to assist (e.g. a math agent for solving math problems, a history agent fo
r discussing historical topics, etc.)
* The relevant specialized agent then engages with the user to address their speci
fic query
* Throughout the conversation, even as different specialized agents kick in, the full chat history is retained
 and passed along, so each agent has the full context of the conversation
* This allows the conversational AI to provide
 a seamless experience that is personalized to the user's ongoing needs

I'm fairly new to working with tools like Langc
hain and could use any advice or best practices for architecting and orchestrating something like this. Some specific qu
estions:

* What's the best way to structure the specialized agents? Should they be separate fine-tuned models, separate
 knowledge bases that plug into foundational models (GPT-4), or something else?
* How can I efficiently store and pass a
long the full conversation history to each agent, without hitting token limits of the underlying models?
* Are there any
 existing open-source projects or frameworks that could serve as a good starting point or reference for orchestrating a 
conversational AI like this?

Any guidance or resources are much appreciated! I'm excited to dive into this but could us
e a push in the right direction. Let me know if any additional details would be helpful.
```
---

     
 
all -  [ Used Claude's 200K context length to write a 30K word novel which heavily grounds in details unlike  ](https://www.reddit.com/r/LangChain/comments/1c0w79c/used_claudes_200k_context_length_to_write_a_30k/) , 2024-04-13-0909
```
As the title describes, I've used Claude 3 Sonnet to create a 30K word story which heavily grounds in details. Here is t
he [story link](https://github.com/desik1998/NovelWithLLMs/blob/main/Novel.md)  (For now put this on Github itself). The
 story is about American founding fathers returning back to 21st Century. Currently it consists of 3 chapters and there 
are 4 more chapters to write. I've already reviewed it with few of my friends who're avid novel readers and most of them
  have responded with 'it doesn't feel AI written', it's interesting  (subjective but most have said this), grounds heav
ily on details. Requesting to read the novel and provide the feedback   

Github Link: [https://github.com/desik1998/Nov
elWithLLMs/tree/main](https://github.com/desik1998/NovelWithLLMs/tree/main) 

# Approach to create long story:

LLMs suc
h as Claude 3 / Gpt 4 currently allows input context length  of 150K words and can output 3K words at once. A typical no
vel in  general has a total of 60K-100K words. Considering the 3K output limit,  it isn't possible to generate a novel i
n one single take. So the  intuition here is that let the LLM **generate 1 event at a time and once the event is generat
ed, add it to the existing story and continously repeat this process**.  Although theoretically this approach might seem
 to work, just doing  this leads to LLM moving quickly from one event to another, not being  very grounded in details, l
lm not generating event which is a  continuation of the current story, LLM generating mistakes based on the  current sto
ry etc.   

To address this, the following steps are taken:   

# 1. Initially fix on the high level story:

Ask LLM to 
generate high level plot of the story like at a 30K  depth. Generate multiple plots as such. In our case, the high level
 line  in mind was **Founding Fathers returning back**. Using  this line, LLM was asked to generated many plots enhancin
g this line. It  suggested many plots such as Founding fathers called back for being  judged based on their actions, fou
nding fathers called back to solve AI  crisis, founding fathers come back for fighting against China, Come back  and fig
ht 2nd revolutionary war etc. Out of all these, the 2nd  revolutionary war seemed the best. Post the plot, LLM was promp
ted to  generate many stories from this plot. Out of these, multiple ideas in  the stories were combined (manually) to g
et to fix on high level story.  Once this is done, get the chapters for the high level story (again  generated multiple 
outputs instead of 1). And generating chapters should  be easy if the high level story is already present   

# 2. Do th
e event based generation for events in chapter:

Once chapters are fixed, now start with the generation of events in a c
hapter but **1 event at a time like described above**.  To make sure that the event is grounded in details, a little pro
mpting  is reqd telling the LLM to avoid moving too fast into the event and  ground to details, avoid generating same ev
ents as past etc. [Prompt used till now](https://github.com/desik1998/NovelWithLLMs/blob/main/PROMPT.md)  (There are som
e repetitions in the prompt but this works well). Even  after this, the output generated by LLM might not be very compel
ling so  to get a good output, generate the output multiple times. And in general  generating **5-10 outputs**, results 
in a good possible  result. And it's better to do this by varying temperatures. In case of  current story, the temperatu
re b/w 0.4-0.8 worked well. Additionally,  the rationale behind generating multiple outputs is, given LLMs generate  dif
ferent output everytime, the chances of getting good output when  prompted multiple times increases. Even after generati
ng multiple  outputs with different temperatures, if it doesn't yield good results,  understand what it's doing wrong fo
r example like avoid repeating events  and tell it to avoid doing that. For example in the 3rd chapter when  the LLM was
 asked to explain the founders about the history since their  time, it was rushing off, so [an instruction to explain th
e historic events year-by-year](https://github.com/desik1998/NovelWithLLMs/blob/main/HistoryChapterPrompt.md)  was added
 in the prompt. Sometimes the LLM also generates part of the  event which is too good but the overall event is not good,
 in this  scenario adding the part of the event to the story and continuing to  generate the story worked well.   

**Ov
erall Gist:** Generate the event multiple times  with different temperatures and take the best amongst them. If it still
  doesn't work, prompt it to avoid doing the wrong things it's doing   

Overall Event Generation: Instead of generating
 the next event in a chat conversation mode,  giving the whole story till now as a combination of events in a single  pr
ompt and asking it to generate next event worked better.   

**Conversation Type 1:** 

    human: generate 1st event 
 
   Claude: Event1 
    human: generate next,  
    Claude: Event2, 
    human: generate next ...

**Conversation Type 2:
** (Better)   

    Human:   
    Story till now: 
    Event1 + Event2 + ... + EventN. 
    Generate next event   
    

    Claude: 
    Event(N+1)

Also as the events are generated, one keeps getting new ideas to  proceed on the story chap
ters. And if any event generated is so good,  but aligns little different from current story, one can also change the  f
uture story/chapters.   

**The current approach, doesn't require any code** and long stories can be generated directly 
using the **Claude Playground or Amazon Bedrock Playground**  (Claude is hosted). Claude Playground has the best Claude 
Model Opus  which Bedrock currently lacks but given this Model is 10X costly,  avoided it and went with the 2nd Best Son
net Model. As per my  experience, the results on Bedrock are better than the ones in Claude  Playground   

# Questions:


1. Why wasn't Gpt4 used to create this story?     
 

* When asked Gpt4 to generate the next event in the story, there
 was  no coherence in the next event generated with the existing story. Maybe  with more prompt engineering, this might 
be solved but Claude 3 was  giving better output without much effort so went with it. Infact, Claude  3 Sonnet (the 2nd 
best model from Claude) is doing much better when  compared to Gpt4.     
 

2. How much cost did it take to do this?   
  
 

* **$50-100**   
 

# Further Improvements:

1. Explore ways to avoid long input contexts. This can further reduce
  the cost considering most of the cost is going into this step. Possible  Solutions:   

* Give gists of the events hap
pened in the story till now instead of whole story as an input to the LLM. References: [1](https://deepmind.google/resea
rch/publications/74917/), [2](https://arxiv.org/html/2310.00785v3)   


2. Avoid the human loop as part of the choosing 
the best event  generated. Currently it takes a lot of human time when choosing the best  event generated. Due to this, 
the time to generate a story can take  from few weeks to few months (1-1.5 months). If this step is automated  atleast t
o some degree, the time to write the long story will further  decrease. Possible Solutions:     


* Use an LLM to deter
mine what are the best events or top 2-3 events  generated. This can be done based on multiple factors such as whether  
the event is a continuation, the event is not repeating itself. And  based on these factors, LLM can rate the top respon
ses. References: [Last page in this paper](https://huggingface.co/papers/2308.06259) 
* Train a reward model (With or wi
thout LLM) for determining which generated event is better. [LLM as Reward model](https://arxiv.org/html/2401.10020v1)  
 
 

3. The current approach generates only 1 story. Instead generate a Tree  of possible stories for a given plot. For 
example, multiple generations  for an event can be good, in this case, select all of them and create  different stories.
     


4. Use the same approach for other things such as movie story generation, Text Books, Product document generatio
n etc     


5. Benchmark LLMs Long Context not only on RAG but also on Generation     
 
```
---

     
 
all -  [ Putting your Function-call tools to an Online Hub and Use in CrewAI, LangChain and AutoGen with Auto ](https://www.reddit.com/r/LocalLLaMA/comments/1c0uyjj/putting_your_functioncall_tools_to_an_online_hub/) , 2024-04-13-0909
```
Hi, i am working on a open source MIT licenced function hub for LLM agents function-call ability. In this point i just w
ant to create multiple integrations with various agent frameworks like **crewAI**, **AutoGen** and **LangChain**. My mot
ivation is increasing the usage of tool amount for each framework and there is no utility and a **toolhub** project.




So i just make a platform for storing functions with **automaticaly dependency installation**, running the function **in
 local for security** and **creating documents and readmes for each function automaticaly with llm**. Also i just create
 a module infrastructure for each functions, its like categories.

**'Tiger: Neuralink for your AI agents'**



I say th
is because the tiger is providing an think and made interface for AI agents just like the original [neuralink](https://n
euralink.com/) and humans. I just put some images and GitHub link:

[https://github.com/Upsonic/Tiger](https://github.co
m/Upsonic/Tiger)

https://preview.redd.it/2zasl9n0kptc1.png?width=1867&format=png&auto=webp&s=84a17941b221cbbb18636d9557
10e4d0df7c8b55

  

```
---

     
 
all -  [ GitHub - Upsonic/Tiger: Neuralink for your AI Agents ](https://www.reddit.com/r/crewai/comments/1c0tsu6/github_upsonictiger_neuralink_for_your_ai_agents/) , 2024-04-13-0909
```
Tiger: Neuralink for AI Agents (MIT) (Python)

Hello, we are developing a superstructure that provides an AI-Computer in
terface for AI agents created through the frameworks like crewAI, LangChain and AutoGen, we have published it completely
 openly under the MIT license.

What it does: Just like human developers, it has some abilities such as running the code
s it writes, making mouse and keyboard movements, writing and running Python functions for functions it does not have. A
I literally thinks and the interface we provide transforms with real computer actions.

Those who want to contribute can
 provide support under the MIT license and code conduct. [https://github.com/Upsonic/Tiger](https://github.com/Upsonic/T
iger)
```
---

     
 
all -  [ Allow Chatbot to Correct Itself to User Feedback ](https://www.reddit.com/r/LangChain/comments/1c0t2tt/allow_chatbot_to_correct_itself_to_user_feedback/) , 2024-04-13-0909
```
Hi,

So, I noticed on ChatGPT and also on my own chatbot (for a brief period of time), the chatbot would apologize and c
orrect itself when provided feedback by the user. For example:

Q: What is 2+2?  
A: 5

Q: No, it is 4.

Expected A: Sor
ry, you're right. It is 4.

Actual A: 5.

&#x200B;

My chatbot now is just sticking strongly to its answer instead of re
medying itself. What is the best way to acknowledge the corrected answer?
```
---

     
 
all -  [ Learning to fine tune models to write content in my voice ](https://www.reddit.com/r/OpenAI/comments/1c0szuw/learning_to_fine_tune_models_to_write_content_in/) , 2024-04-13-0909
```
Whats a good resource to start on this?

Broadly speaking I already understand how to use OpenAI's API to send simple me
ssages back and forth. But I'm not familiar with fine tuning or anything more complex.

I'd really like how to do this i
n a way that's LLM-agnostic, I've dabbled in LangChain a little which I assume is key to this, but in absence of that wi
ll gladly start with OpenAI specific learnings.
```
---

     
 
all -  [ Best Method to Quickly and Easily Deploy? ](https://www.reddit.com/r/LangChain/comments/1c0rvek/best_method_to_quickly_and_easily_deploy/) , 2024-04-13-0909
```
I used Gradio to deploy, which is quick and easy. What’s the easiest way to add stripe payment collection for subscripti
on?
```
---

     
 
MachineLearning -  [ [D] How to get the source documents from the retrieved context for RAG?  ](https://www.reddit.com/r/MachineLearning/comments/1bvoc1t/d_how_to_get_the_source_documents_from_the/) , 2024-04-13-0909
```
I'm not using Lanchain but only making API calls to an LLM service provider. The retriever is connected to a vector DB, 
and I would like to know what the LLM refers to WITHIN that retrieved context whenever it provides an answer, similar to
 how return_source_documents works in Langchain.

I'm using AzureOpenAI. I couldn't find much in their docs that related
 to returning the source documents. Any help will be greatly appreciated!

```
---

     
 
MachineLearning -  [ [P] RAG pipeline to query the ML Engineering Open Book ](https://www.reddit.com/r/MachineLearning/comments/1bu4wyx/p_rag_pipeline_to_query_the_ml_engineering_open/) , 2024-04-13-0909
```
I built a quick RAG implementation using Langchain to make it easy to query the [ML Engineering Open Book](https://githu
b.com/stas00/ml-engineering) by [Stas Bekman](https://twitter.com/StasBekman). The Multi-Vector retriever gave pretty go
od results and was quite easy to set up too. 

Github link - [https://github.com/shreyansh26/RAG-ML-Engg-Open-Book](http
s://github.com/shreyansh26/RAG-ML-Engg-Open-Book)

Hope this is useful for folks!
```
---

     
 
MachineLearning -  [ [Project] FinancialAdvisorGPT : LLM+RAG Boilerplate Project ](https://www.reddit.com/r/MachineLearning/comments/1btlpgd/project_financialadvisorgpt_llmrag_boilerplate/) , 2024-04-13-0909
```
FinancialAdvisorGPT is a boilerplate project designed for RAG (Retriever-Augmented Generation) and LLM (Large Language M
odel) applications in financial analysis. Built on a technology stack including MongoDB, MongoDB VectorDB, Chroma, FastA
PI, Langchain, and React submodule for UI, it offers a framework for developers to implement and customize RAG+LLM proje
cts. Leveraging parallelized data pipelines, FinancialAdvisorGPT processes and integrates various data sources such as s
tock data, news, SEC filings, and local PDFs.

Github project includes long documentation on how the project is structur
ed, how LLM+RAG works for specific task : [https://github.com/mburaksayici/FinancialAdvisorGPT](https://github.com/mbura
ksayici/FinancialAdvisorGPT)
```
---

     
 
MachineLearning -  [ [Project] Picachain, image search made simple. ](https://www.reddit.com/r/MachineLearning/comments/1bt7epv/project_picachain_image_search_made_simple/) , 2024-04-13-0909
```
I am working on creating something for image search, basically something like langchain for images. Probably add videos 
too.

Currently supports chromaDB. Working on pinecone and other vector dbs. [https://github.com/d1pankarmedhi/picachain
](https://github.com/d1pankarmedhi/picachain)

Will you use something like this? What else should I add? Feel free to ad
d your views.

Appreciate your feedback or any feature ideas :)

&#x200B;
```
---

     
 
deeplearning -  [ Tengyu Ma on Voyage AI - Weaviate Podcast #91! ](https://www.reddit.com/r/deeplearning/comments/1bjft8i/tengyu_ma_on_voyage_ai_weaviate_podcast_91/) , 2024-04-13-0909
```
**Voyage AI** is the newest giant in the embedding, reranking, and search model game!

I am SUPER excited to publish our
 latest Weaviate podcast with Tengyu Ma, Co-Founder of Voyage AI and Assistant Professor at Stanford University!

We beg
an the podcast with a deep dive into everything embedding model training and contrastive learning theory. Tengyu deliver
ed a **masterclass** in everything from scaling laws to multi-vector representations, neural architectures, representati
on collapse, data augmentation, semantic similarity, and more! I am beyond impressed with Tengyu's extensive knowledge a
nd explanations of all these topics.

The next chapter dives into a case study Voyage AI did **fine-tuning an embedding 
model for the LangChain documentation.** This is an absolutely fascinating example of the role of continual fine-tuning 
with very new concepts (for example, very few people were talking about chaining together LLM calls 2 years ago), as wel
l as the data efficiency advances in fine-tuning.

We concluded by discussing ML systems challenges in serving an embedd
ings API. Particularly the challenge of detecting if a request is for batch or query inference and the optimizations tha
t go into either say \~100ms latency for a query embedding or maximizing throughput for batch embeddings.

I hope you fi
nd the podcast interesting, more than happy to discuss any of these topics with you or answer any questions about the co
ntent in the podcast! Thank you so much!

YouTube: [https://www.youtube.com/watch?v=xPdyivfheqI](https://www.youtube.com
/watch?v=xPdyivfheqI)

Spotify: [https://spotifyanchor-web.app.link/e/u6XPLYfF7Hb](https://spotifyanchor-web.app.link/e/
u6XPLYfF7Hb)
```
---

     
