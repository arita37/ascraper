 
all -  [ I come with a realization you do not want to hear ](https://www.reddit.com/r/LangChain/comments/1c3esbn/i_come_with_a_realization_you_do_not_want_to_hear/) , 2024-04-14-0914
```
After hundreds of hours struggling to find solutions to real-world problems with AI such as making API requests to custo
m API so that the LLMs have data to base their answers or even real-time voice enable support agents, I have come to thi
s conclusion:

# Langchain tools are pointless and extremely convoluted, do not waste your time with them!

All agents a
re a pre-prompt that makes whatever little context you have left for your actual prompt just extremely inaccurate, The s
ame goes with output parsers, it's all just very dumb and makes the development experience awful.  


If you wanna solve
 any real-world problems this year, stop catering to some convoluted objects that ask for some other specific object as 
input.  


yuo are better off just using Fstrings, I have made 10x more progress just using a simple llmchain with strin
gs than I ever did in months trying to use all these dumb 'features' that in reality all they do is take up context and 
reduce accuracy.
```
---

     
 
all -  [ LLMs can rephrase retrieved information. How do you handle it? ](https://www.reddit.com/r/LangChain/comments/1c35xlu/llms_can_rephrase_retrieved_information_how_do/) , 2024-04-14-0914
```
For example, rephrasing code can often introduce unintended noise. How do you evaluate the RAG if it rephrases results?


How can one ensure mininal rephrasing?

```
---

     
 
all -  [ How do you handle unstructured data? ](https://www.reddit.com/r/LangChain/comments/1c34qaf/how_do_you_handle_unstructured_data/) , 2024-04-14-0914
```
I have a requirement to handle unstructured data: images, tables, graphs and of course text. I tried using unstructured.
io and gpt-4-turbo to test on tables. Doing well.   
I am quite confused on how to approach for images and graphs.  
Was
 recommended to use finetuned LLaVA model. How should I finetune it? Provide it with images? Is that sane thing to do fo
r prod-level?
```
---

     
 
all -  [ Question about Tailoring Conversational Responses  ](https://www.reddit.com/r/LangChain/comments/1c312zy/question_about_tailoring_conversational_responses/) , 2024-04-14-0914
```
I have a typical ConversationalRetrievalChain  RAG that uses a vector db for sources. The prompt is nothing crazy and do
es include 'don't use any knowledge outside of the provided context' to help prevent confabulation. 

But when I say 'hi
' to it, it responds with an answer informed by some of the stored vectors: 'The answer to 'hi' was 'hello''. 

Is there
 a way to get it to be conversational when not asking it stuff directly related to its defined role and directions? 
```
---

     
 
all -  [ Langchain with Flutter ](https://www.reddit.com/r/FlutterDev/comments/1c2zkld/langchain_with_flutter/) , 2024-04-14-0914
```
It’s possible and has good performance to use langchain with flutter apps or is better to use backend?

```
---

     
 
all -  [ best architecture for a financial agent. ](https://www.reddit.com/r/LangChain/comments/1c2zhvu/best_architecture_for_a_financial_agent/) , 2024-04-14-0914
```
I have been experimenting with various financial agent architectures. Currently, I am using an agent with several financ
ial tools that call different financial API endpoints from the data provider. These APIs cover almost all fundamental fi
nancial data for a particular stock. However, as the number of tools increases, it becomes difficult for the agent to id
entify the right tool for answering user queries, sometimes leading to inaccurate answers and making the approach somewh
at inefficient.

I have all the data stored in a database that gets updated regularly. To solve this problem, I have two
 alternative approaches in mind:

1. Using a single tool to convert the user query into SQL using an LLM with the databa
se schema and directly querying the database with the generated query.
2. Creating a vector embedding collection for eac
h stock that contains all the data I have for a stock, then using a retriever to query the vector database collections. 
 


Please provide your insights on the following:

1. Which approach would be more suitable for the financial agent, an
d why?
2. What are the advantages and disadvantages of each approach?
```
---

     
 
all -  [ How do actually save a document output to local disc for langgraph?  ](https://github.com/langchain-ai/langgraph/blob/main/examples/multi_agent/hierarchical_agent_teams.ipynb) , 2024-04-14-0914
```
I’m following along with this example of a multi agent hierarchical system. The end output should be a document written 
to disc. I can output the conversation to txt and can see that a document “has been finished and saved to disc”, but tha
t’s just what the agent says but I can see any code that actually says to save to disc. 
I have supergraph.stream, but a
gain, that just outputs the conversation. How do I output the actually document they made? 

Thanks!


```
---

     
 
all -  [ How to use multiple tools at once ](https://www.reddit.com/r/LangChain/comments/1c2vqzk/how_to_use_multiple_tools_at_once/) , 2024-04-14-0914
```
How can I get my LLM to use multiple tools (not just one out of many) to answer my user query?
```
---

     
 
all -  [ Query MongoDB using Langchain ](https://youtu.be/boN1KkfcMZE?si=FxBtzWciboVP7XLE) , 2024-04-14-0914
```

```
---

     
 
all -  [ LLM Newb, looking for help ](https://i.redd.it/mwux4unid6uc1.jpeg) , 2024-04-14-0914
```
Hello, looking for some help

This is my first time working with an LLM, I am trying to build a super simple project to 
gain some experience, just trying to build the simplest python script that uses an LLM that I can. 

\-I was using MSVS 
2022, it kept giving me a hard time saying that it couldnt find what I was trying to import (for example, import torch, 
never worked, or import langchain) Does anyone know why? Or is it best if I just avoid MSVS all together? 

Since then I
 have learned how to use Jupyter notebook, and have made it past that issue.

\- I am following tutorials, and they keep
 coming up with outdated models. This (and others I have tried) model keeps giving a huge error, from what I can tell it
 is because it is no longer supported. Does anyone know a more up to date model that I can use? Or can you see anything 
else wrong with this code that may be causing it not to run. 



Thanks for the help, I know I am very novice here, othe
r than this, small coding projects are really my main experience.  (CSE 100, leetcode, etc) I know that this is a big st
ep, but I am trying to follow this tutorial to dip my toes in just a little bit. Any tips to help me get past this obsta
cle and get my first program to run? 


```
---

     
 
all -  [ Best vector database for large scale data, besides qdrant and pinecone ](https://www.reddit.com/r/LangChain/comments/1c2t59t/best_vector_database_for_large_scale_data_besides/) , 2024-04-14-0914
```
Had test in prod, pinecone is slow

Qdrant does not perform well when large amount of collections being created.

So I a
m searching for other great options.

I want at least 4 features.

1. open source and self hosted
2. Vectors can be offl
oaded to disk because there is too much data to store in RAM.
3. Capability to store 10k-100k collections without much o
verhead.
4. in active development and support
```
---

     
 
all -  [ Hello, looking for some help ](https://www.reddit.com/r/LLMDevs/comments/1c2ndao/hello_looking_for_some_help/) , 2024-04-14-0914
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

     
 
all -  [ Best embedded models for transcriptions/spoken language? ](https://www.reddit.com/r/LangChain/comments/1c2l33u/best_embedded_models_for_transcriptionsspoken/) , 2024-04-14-0914
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

     
 
all -  [ About ELECTRA ](https://www.reddit.com/r/LangChain/comments/1c2kdwz/about_electra/) , 2024-04-14-0914
```
I don't understand why it's better for ELECTRA to use the alternate token detection task instead of the MLM task while M
LM in Bert still replaced token with 10%. Can you explain it to me?
```
---

     
 
all -  [ Langchain + gemini ](https://www.reddit.com/r/googlecloud/comments/1c2hi10/langchain_gemini/) , 2024-04-14-0914
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

     
 
all -  [ Burr: an OS framework for building and debugging AI applications faster ](https://www.reddit.com/r/mlops/comments/1c2du1c/burr_an_os_framework_for_building_and_debugging/) , 2024-04-14-0914
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

     
 
all -  [ Difference between ReAct and OpenAI functions Agent type ](https://www.reddit.com/r/LangChain/comments/1c2cnuo/difference_between_react_and_openai_functions/) , 2024-04-14-0914
```
Title

I can see that in ReAct, there's thought-action(which tool)-output. What does it do in when the type is openai_fu
nctions? Like how does it choose the tools in that case? I wanna understand the internal difference
```
---

     
 
all -  [ How do people typically debug TypeError in LCEL ? ](https://www.reddit.com/r/LangChain/comments/1c2bq58/how_do_people_typically_debug_typeerror_in_lcel/) , 2024-04-14-0914
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

     
 
all -  [ Training own embedding model for custom use-case ](https://www.reddit.com/r/LangChain/comments/1c2a8bi/training_own_embedding_model_for_custom_usecase/) , 2024-04-14-0914
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

     
 
all -  [ Has anyone used the Re-ranker API from Cohere with one a LangChain retriever that isn't the base one ](https://www.reddit.com/r/LangChain/comments/1c29o79/has_anyone_used_the_reranker_api_from_cohere_with/) , 2024-04-14-0914
```
Every example I see online with the Cohere re-ranker, uses the base vector store retriever as the retriever.

&#x200B;


It does not use ensemble, or parent document, or multi query etc. Any help appreciated.
```
---

     
 
all -  [ Help with semantic chunker ](https://www.reddit.com/r/LangChain/comments/1c27lkv/help_with_semantic_chunker/) , 2024-04-14-0914
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

     
 
all -  [ Return the tool output without any modifications ](https://www.reddit.com/r/LangChain/comments/1c24si0/return_the_tool_output_without_any_modifications/) , 2024-04-14-0914
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

     
 
all -  [ Langchain rag with ChatGoogleGenerativeAI Error ](https://www.reddit.com/r/LangChain/comments/1c21u43/langchain_rag_with_chatgooglegenerativeai_error/) , 2024-04-14-0914
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

     
 
all -  [ MODERATION TOPIC / LLM OPENAI ](https://www.reddit.com/r/LangChain/comments/1c1p30i/moderation_topic_llm_openai/) , 2024-04-14-0914
```
How do you add moderation to your models; for example limit to my model to only answer question relationated with Life S
cience and Health.
```
---

     
 
all -  [ RAG Q/A | PDF Conversation | Langchain | OpenAI ](https://www.reddit.com/r/LangChain/comments/1c1o7nj/rag_qa_pdf_conversation_langchain_openai/) , 2024-04-14-0914
```
HELP: How can I make a rag Q/A app that allows the user to upload a pdf to the conversation and so that the model can un
derstand the context of the pdf; I tried to perform an ensemble retrievel but at some point the chunks lose the context 
of the entire pdf
```
---

     
 
all -  [ Chainlit Copilot mode: Embed your LangChain Agent as a copilot on a website or software ](https://www.reddit.com/r/LangChain/comments/1c1m2jb/chainlit_copilot_mode_embed_your_langchain_agent/) , 2024-04-14-0914
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

     
 
all -  [ Improving the summarisation capability of LLM - will LangChain help? ](https://www.reddit.com/r/LangChain/comments/1c1ltfp/improving_the_summarisation_capability_of_llm/) , 2024-04-14-0914
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

     
 
all -  [ Tables context length issue in RAG ](https://www.reddit.com/r/LangChain/comments/1c1lsk6/tables_context_length_issue_in_rag/) , 2024-04-14-0914
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

     
 
all -  [ Langchain + Pydanctic + OpenAI : pydantic.v1.error_wrappers.ValidationError: 1 validation error for  ](https://www.reddit.com/r/LangChain/comments/1c1l8zp/langchain_pydanctic_openai_pydanticv1error/) , 2024-04-14-0914
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

     
 
all -  [ Best library/framework for parsing PDF documents with table inside? ](https://www.reddit.com/r/LangChain/comments/1c1ksv6/best_libraryframework_for_parsing_pdf_documents/) , 2024-04-14-0914
```
Hello, me and my team were looking for integrate inside our RAG company model the most decent pdf parser, we need one th
at can also parse tables and schemes and keep the information intact (or at least not completely broken when it will be 
sent to the vector database). We already tried Pypdf, pdfPlumber, Unstructured and Nougat, but all of these libraries we
ren't good enough for our needs. Do you guys know any other alternative?
```
---

     
 
all -  [ Multivector RAG for drugs pdf, missing context, I need help ](https://www.reddit.com/r/ChatGPTCoding/comments/1c1klmk/multivector_rag_for_drugs_pdf_missing_context_i/) , 2024-04-14-0914
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

     
 
all -  [ Building and Deploying a MinIO-Powered LangChain Agent API with LangServe ](https://www.reddit.com/r/minio/comments/1c1jopp/building_and_deploying_a_miniopowered_langchain/) , 2024-04-14-0914
```
Building on these insights, we now turn our focus to [LangServe](https://blog.langchain.dev/introducing-langserve/?ref=b
log.min.io), a pivotal tool in transitioning LangChain applications from development to deployment, simplifying the proc
ess of launching production-ready APIs.

[https://blog.min.io/minio-powered-langchain-agent-with-langserve/](https://blo
g.min.io/minio-powered-langchain-agent-with-langserve/)
```
---

     
 
all -  [ How do you discover tools/ideas that might help improve your LLM-based apps which are not RAG? ](https://www.reddit.com/r/LangChain/comments/1c1g07n/how_do_you_discover_toolsideas_that_might_help/) , 2024-04-14-0914
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

     
 
all -  [ Open Source Function-Hub for Agent Tools | crewAI - LangChain - Autogen ](https://www.reddit.com/r/LocalLLaMA/comments/1c1d8sd/open_source_functionhub_for_agent_tools_crewai/) , 2024-04-14-0914
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

     
 
all -  [ We summarised Harrison Chase's talk on the evolution of AI agents and their applications ](https://www.reddit.com/r/LangChain/comments/1c1c0md/we_summarised_harrison_chases_talk_on_the/) , 2024-04-14-0914
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

     
 
all -  [ Having issues with Manual install after installing the requirements ](https://www.reddit.com/r/ankibrain/comments/1c17wba/having_issues_with_manual_install_after/) , 2024-04-14-0914
```
ive managed to enter the virtual environment but after installing everything via pip and reopening Anki the AnkiBrain wi
ndow does not appear. Any idea where would the logs be to debug this?

&#x200B;

&#x200B;

https://preview.redd.it/yrp0q
joykstc1.png?width=1881&format=png&auto=webp&s=3d7efb4bba2afa672b00721da05b304b2c788fc9
```
---

     
 
all -  [ What resources should I use to become an expert in LLM based applications/chatbots?  ](https://www.reddit.com/r/LangChain/comments/1c17gld/what_resources_should_i_use_to_become_an_expert/) , 2024-04-14-0914
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

     
 
MachineLearning -  [ [D] How to get the source documents from the retrieved context for RAG?  ](https://www.reddit.com/r/MachineLearning/comments/1bvoc1t/d_how_to_get_the_source_documents_from_the/) , 2024-04-14-0914
```
I'm not using Lanchain but only making API calls to an LLM service provider. The retriever is connected to a vector DB, 
and I would like to know what the LLM refers to WITHIN that retrieved context whenever it provides an answer, similar to
 how return_source_documents works in Langchain.

I'm using AzureOpenAI. I couldn't find much in their docs that related
 to returning the source documents. Any help will be greatly appreciated!

```
---

     
 
MachineLearning -  [ [P] RAG pipeline to query the ML Engineering Open Book ](https://www.reddit.com/r/MachineLearning/comments/1bu4wyx/p_rag_pipeline_to_query_the_ml_engineering_open/) , 2024-04-14-0914
```
I built a quick RAG implementation using Langchain to make it easy to query the [ML Engineering Open Book](https://githu
b.com/stas00/ml-engineering) by [Stas Bekman](https://twitter.com/StasBekman). The Multi-Vector retriever gave pretty go
od results and was quite easy to set up too. 

Github link - [https://github.com/shreyansh26/RAG-ML-Engg-Open-Book](http
s://github.com/shreyansh26/RAG-ML-Engg-Open-Book)

Hope this is useful for folks!
```
---

     
 
MachineLearning -  [ [Project] FinancialAdvisorGPT : LLM+RAG Boilerplate Project ](https://www.reddit.com/r/MachineLearning/comments/1btlpgd/project_financialadvisorgpt_llmrag_boilerplate/) , 2024-04-14-0914
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

     
 
MachineLearning -  [ [Project] Picachain, image search made simple. ](https://www.reddit.com/r/MachineLearning/comments/1bt7epv/project_picachain_image_search_made_simple/) , 2024-04-14-0914
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

     
 
deeplearning -  [ Tengyu Ma on Voyage AI - Weaviate Podcast #91! ](https://www.reddit.com/r/deeplearning/comments/1bjft8i/tengyu_ma_on_voyage_ai_weaviate_podcast_91/) , 2024-04-14-0914
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

     
