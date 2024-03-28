 
all -  [ Help with LLM to design circuits ](https://www.reddit.com/r/LangChain/comments/1bp914d/help_with_llm_to_design_circuits/) , 2024-03-28-0910
```
I have a project where I need to create an assistant that will help my professor which teaches digital circuits at the u
niversity. The purpose of the project is that if a student was studying for an exam at 3 AM but needs to understand a qu
estion or circuit diagram, they can ask the AI assistant which is basically as good as the professor himself. Ill need t
o have separate sessions ans save the conversation in a database.

The professor sent me the data which consist of Power
Point presentations which consists of images and text and those are what I want my LLM to focus on. The LLM should be ab
le to draw a circuit diagram to explain what its showing. 

 I tried gpt vision but its not showing proper results and t
he software we use for the circuit diagrams is simulink. I know how to save and store the data in a database and load ea
ch user separately and I know how to do rag but my main issue lies in how can I allow my LLM use simulink to design circ
uits? Do I need to use agemt? If yes, how do I connect it and allow it to design from simulink? 
```
---

     
 
all -  [ LangGraph with Claude? ](https://www.reddit.com/r/LangChain/comments/1bp7thq/langgraph_with_claude/) , 2024-03-28-0910
```
Hi, like the title says I would like to know whether LangGraph works well with all the Claude models? I never tested the
 function calling abilities of Claude and have no idea if they work well inside the LangGraph framework. Any type of ill
umination is greatly appreciated.

Thanks in advance.
```
---

     
 
all -  [ AWS OpenSearch Vector not returning anything on similarity search ](https://www.reddit.com/r/LangChain/comments/1bp6frg/aws_opensearch_vector_not_returning_anything_on/) , 2024-03-28-0910
```
I have an aws opensearch vector store. I can connect to it with the opensearch-py library and I can create an index and 
upload documents to the index. I am using langchain 0.1.13 and langchain-community 0.0.29

here's my code:

```python
fr
om langchain_community.document_loaders import TextLoader  
from langchain_text_splitters import CharacterTextSplitter  

from langchain_openai import OpenAIEmbeddings  
from langchain_community.vectorstores import OpenSearchVectorSearch

do
cuments = TextLoader('./test.txt').load()
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
docs =
 text_splitter.split_documents(documents)
  
embeddings = OpenAIEmbeddings()  
 
vector_store = OpenSearchVectorSearch(

    opensearch_url=f'https://{url}:{port}',
    index_name='test',
    embedding_function=embeddings,
    http_auth=auth
,
    use_ssl = True,
    verify_certs = False
)

vector_store.add_documents(documents=docs)
```

but when I run the bel
ow I get no documents back consistently even when the prompt is identical to the content in the index I get nothing back
:

```python
print(vector_store.similarity_search('what is my name on thursday?', k=1))
```

I've validated that the ind
ex names are all correct and the vector fields are all consistently named. I can query the index and see the documents u
ploading correctly here:

```python
from opensearchpy import OpenSearch

client = OpenSearch(
    hosts=[{'host': url, '
port': port}],
    http_auth=auth,
    use_ssl=True,
    verify_certs=False
)

response = client.search(
    index='test
',
    body={'query': {'match_all': {}}},
    size=1000
)

documents = [doc['_source'] for doc in response['hits']['hits
']]
print(documents)
```

Any thoughts on what the issue might be? Literally any help is appreciated.
```
---

     
 
all -  [ LangChain for a full framework - what options for more focused toolkits? ](https://www.reddit.com/r/LangChain/comments/1bp48si/langchain_for_a_full_framework_what_options_for/) , 2024-03-28-0910
```
LangChain does a great job as a full framework for LLM-based application development, but there are so many components s
ometimes you just want a toolkit that is better at a particular piece. I won't go down the rabbit-hole of 'frameworks vs
 toolkits' in general, but if you're looking for some of the alternatives to LangChain for pieces of the LLM-application
 development puzzle here's a write up: [https://www.mirascope.io/post/langchain-alternatives](https://www.mirascope.io/p
ost/langchain-alternatives)
```
---

     
 
all -  [ Question on querying pre stored vectors on weviate ](https://www.reddit.com/r/LangChain/comments/1bp33yk/question_on_querying_pre_stored_vectors_on_weviate/) , 2024-03-28-0910
```
I am relatively new to langchain. I need to load a pdf stored in GCS and I want chunk and embed the contents of the pdf 
and store it on weviate. I want to then retrive relevant vectors later and user a RetrivalQAChain. How do I do it? Any h
elp or code samples are appreciated! Thanks in advance. 
```
---

     
 
all -  [ Uploaded my first YouTube video ever and it's about LangChain! ](https://www.reddit.com/r/LangChain/comments/1bp2mao/uploaded_my_first_youtube_video_ever_and_its/) , 2024-03-28-0910
```
**Little announcement!**

What's up, everyone?!   

I finally uploaded my first YouTube video based on one of my blog po
sts: [https://www.youtube.com/watch?v=ubsqSWfXAPI](https://www.youtube.com/watch?v=ubsqSWfXAPI)  

It's a tutorial about
 using LangChain's Output Parsers with GPT to convert the contents of a PDF file to JSON. ([I originally wrote about thi
s on the blog here](https://www.gettingstarted.ai/how-to-extract-metadata-from-pdf-convert-to-json-langchain/)). To be h
onest, I've been wanting to publish a video for some time now but finally went for it so I'm not sure what to expect.

I
'm still learning about video editing, recording, and YouTube in general but **I'd love to know your feedback (and comme
nts)** so that I can implement it in future videos.

Thanks!
```
---

     
 
all -  [ HR Chatbot created using LangChain, free to use! ](https://www.reddit.com/r/LangChain/comments/1bozlzo/hr_chatbot_created_using_langchain_free_to_use/) , 2024-03-28-0910
```
Hey guys, I have developed a AI chatbot using LangChain, Pinecone, and ChatGPT. You can try it out for free on [HR Chatb
ot](http://hrchatbot.deligence.com/chat)

Let me know what you guys think about it!

```
---

     
 
all -  [ TDS Article: Visualize your RAG Data — Evaluate your Retrieval-Augmented Generation System with Raga ](https://towardsdatascience.com/visualize-your-rag-data-evaluate-your-retrieval-augmented-generation-system-with-ragas-fc2486308557) , 2024-03-28-0910
```

```
---

     
 
all -  [ LCEL and evaluation on a RAG pipeline ](https://www.reddit.com/r/LangChain/comments/1boxuci/lcel_and_evaluation_on_a_rag_pipeline/) , 2024-03-28-0910
```
Hello,

I have implemented a RAG for retrieval on a postgres db. First, using embeddings I get the k-most relevant docum
ent and then using the load\_summarize\_chain from Langchain I create a response as in this [tutorial](https://cloud.goo
gle.com/blog/products/databases/using-pgvector-llms-and-langchain-with-google-cloud-databases/). My first question is th
at how can I use LCEL to make the chain. Lastly, how can I evaluate the response?

I tried using the  *DeepEvalAnswerRel
evancyEvaluator*  as shown [here](https://docs.confident-ai.com/docs/integrations-llamaindex) but I am getting the follo
wing error

`ERROR: AttributeError: 'Document' object has no attribute 'get_content'`
```
---

     
 
all -  [ Chroma db throws error at 2nd run ](https://www.reddit.com/r/LangChain/comments/1bowtfo/chroma_db_throws_error_at_2nd_run/) , 2024-03-28-0910
```
Hi!!  
I am using chroma db with pre computed embeddings for my rag application. Chroma runs well first time but every t
ime i re run my notebook i get this error. Thanks :)

https://preview.redd.it/aqq8insu6uqc1.png?width=3000&format=png&au
to=webp&s=51adc2a358e349fdbe3c211ed869d0f79c1bb986
```
---

     
 
all -  [ Prompt injection  ](https://www.reddit.com/r/LangChain/comments/1bovlcb/prompt_injection/) , 2024-03-28-0910
```
Can someone please highlight what is meant by prompt injection and what security concerns it may have , and if somebody 
can provide an example for the same that would be great 
```
---

     
 
all -  [ Possible to create a log querying tool with a natural language using aws bedrock ?  ](https://www.reddit.com/r/aws/comments/1bot20y/possible_to_create_a_log_querying_tool_with_a/) , 2024-03-28-0910
```
I want to create a tool which I feed it log data and can ask it questions in natural language like which transactions ha
ve the highest latency or take the most time for completion. Is it possible and if so does someone know what the high le
vel structure would be ? I tried to create it using langchain and ollama but the problem was the context size was more t
han the LLM could use which gave me poor results 
```
---

     
 
all -  [ How to implement prompt engineering well? ](https://www.reddit.com/r/LangChain/comments/1bosw8h/how_to_implement_prompt_engineering_well/) , 2024-03-28-0910
```
I implemented RAG using Ensemble Retriever. widh llama index

Before using the prompt template module, if  sent a query 
like “Hello”, llm would not respond because the query did not exist in the document. 

And  were able to solve these pro
blems by using the prompt template module.  

How important is prompt template engineering? And what should I do to set 
up prompt template engineering well?   


Below is the prompt template I wrote

    template = '''
    You are a chatbot
 fluent in Korean developed specifically for our company.
    Your primary role is to communicate with users by answerin
g their questions in Korean and providing feedback related to their questions.
    Your job is to provide the user with 
an answer regarding your company's employment rules when asked {query}.
    If you are asked a {query} question that is 
not related to the Company's employment rules, it is your responsibility to redirect the conversation to a topic related
 to the Company's policies and guidelines.
    You can also recommend questions to users based on your knowledge.
    We
 encourage our users to ask questions that are directly related to our company's operations, culture, or the specific gu
idelines we follow.
    '''

&#x200B;
```
---

     
 
all -  [ Long prompt and few-shot placement ](https://www.reddit.com/r/LangChain/comments/1boqup2/long_prompt_and_fewshot_placement/) , 2024-03-28-0910
```
Hi. I have a long prompt of about 500-700 tokens, and context gets added also since it's a RAG, so what I send to the LL
M could easily be a few thousand tokens per question. 

I am trying to get a response that is conversational and that ro
ughly follows a format like :

'To do x, y, and Z, you need to complete these steps.....blah blah.....For more info, ple
ase refer to this video.'

It returns good info but I can't for the life of me get it to return consistently structured 
responses. I've tried CoT, but it keeps stating it's reasoning, which makes it sound like the robot it is. I just want i
t to end with 'for more info..' Or 'if you need more help..' Etc. 

So I'm thinking few-shot, but I don't know if I shou
ld put the examples before or after the retrieved context given the length of the context and the prompt, in general. 


Has anyone experimented in these conditions?
```
---

     
 
all -  [ How can we tell which LLM arguments are being processed? ](https://www.reddit.com/r/LangChain/comments/1bopm2t/how_can_we_tell_which_llm_arguments_are_being/) , 2024-03-28-0910
```
It seems like the way langchain is set up, extra \`model\_kwargs\` are just quietly thrown on the floor.  I think that h
appens in the pydantic validation process, but I am not sure.

Is there any way to tell what's happening with the \`mode
l\_kwargs\`?

For example, [this langchain issue](https://github.com/langchain-ai/langchain/issues/10590) discusses what
 happens when a model class ignores the \`n\_ctx\` kwarg, and suggests a fix based on editing the \`validate\_environmen
t\` method of a class. But this requires identifying the right \`validate\_environment\` method in the class hierarchy, 
and then modifying a local variable (really a constant, \`model\_param\_names\` -- why isn't this a property of the clas
s instead of a local variable?).

Is there some way to trace the execution of an LLM constructor and see which kwargs ar
e actually sent, and which are ignored?
```
---

     
 
all -  [ How to store group chats??? ](https://www.reddit.com/r/LangChain/comments/1bopi12/how_to_store_group_chats/) , 2024-03-28-0910
```
I'm using Firestore for storage and I already built a solution to store group chats with the following structure:

\--> 
chats <collection>

\----> chat\_doc#1 <well, a doc>

\----> chat\_doc#2

\----> chat\_doc#n

\------> participants <arr
ay with user ids>

\------> messages <collection to store messages, each message in a doc>

Now, I'm looking to integrat
e LangChain into my app (easier to work with multiple LLM providers) and so I have to restructure my code. 

I used \`Fi
restoreChatMessageHistory\` and noticed that their structure is similar to mine, but in each chat doc they only have \`u
serId\` which holds a single user id. I want to replace that with a \`participants\` array or anything that can hold mul
tiple user ids. But I noticed there's no way to customize the \`FirestoreChatMessageHistory\` class to include multiple 
participants.

The way I'm thinking is to use the \`userId\` prop to store all user ids in comma-separated format, but:


1. I don't know if that will work well (or at all) & I don't have the time to test this out if it'll take too much time
 because of the overhead, and
2. there's way too much overhead - it feels stupidly irritating and I feel that there shou
ld be a neater way to implement this.

Anyone face this issue? How did you solve it?
```
---

     
 
all -  [ Codebase + External URL Context for LLM ](https://www.reddit.com/r/LangChain/comments/1bon41r/codebase_external_url_context_for_llm/) , 2024-03-28-0910
```
Sorry if this is obvious to most of you, I’m somewhat new. 

My app is currently successfully, in order:
- Getting URL c
ontent with document loader
- Getting file content from a GitHub codebase
- Sending this to OpenAi model with a prompt
-
 Serving the response to my front end

The issue is around token limitation. 

I would love to be able to get the whole 
codebase along with the reference URL content processed by the LLM and eventually return a single response to my fronten
d, of course I hit the token limit fast. 

I understand that text splitting and vector stores are the solution, I’ll get
 my head around that.

My question is, will I end up sending many requests and get many responses from the LLM?

I don’t
 mind many requests, but I don’t understand how I’ll get a single coherent response to my friend if it’s multiple LLM re
sponses.

Maybe I’m missing something obvious here. 
```
---

     
 
all -  [ Create your AI SaaS for chatbot creation in just one day! ](https://www.reddit.com/r/SaaS/comments/1bomme4/create_your_ai_saas_for_chatbot_creation_in_just/) , 2024-03-28-0910
```
As an AI developer deeply engaged in creating cutting-edge solutions, I've recently completed a significant project: a r
eady-to-integrate API designed for advanced AI creation, tailored for seamless integration into any dashboard. This Adva
nced AI Chatbot Builder API that use a variety of cutting edge technologies, including Langchain, FastAPI, Gemini, OpenA
I GPT-4, Pinecone, and robust AI security measures, providing an advanced AI technology stack for any SaaS platform focu
sed on customizable chatbot solutions. It's crafted to empower businesses and entrepreneurs to offer a scalable, compreh
ensive chatbot building service, leveraging the latest in AI advancements.  
I am looking to sell this API to those inte
rested in developing an AI SaaS platform. The investment for this advanced API is **$10k**. Upon purchase, you will rece
ive the API within one day, enabling a swift market entry. If you're interested in this opportunity, please reach out to
 me at **jaberibraheem808@gmail.com**.  
```
---

     
 
all -  [ My Video on Memory Chatbots ](https://www.reddit.com/r/LangChain/comments/1bojn3b/my_video_on_memory_chatbots/) , 2024-03-28-0910
```
Hey guys, I just created a video on how to build chatbots with memory.

Most of the examples on langchains website are w
ith open api. I wanted to keep things open source so ise llama from huggingface.

Hope you like it. Any feedback is welc
ome.

https://youtu.be/gNXBp3wttFU?si=GirGTqe7ThEUFSrx
```
---

     
 
all -  [ Round 2: Learning how RAG and Fine-Tuning works. Got some questions regarding LangChain commercial u ](https://www.reddit.com/r/LocalLLaMA/comments/1boj3zv/round_2_learning_how_rag_and_finetuning_works_got/) , 2024-03-28-0910
```

During the weekends I've been learning about RAG and Fine-Tuning.  So far I've focused on RAG, but had a few questions:


1) Is RAG **always** a better option than fine-tuning when I need factual data that's not in the original model? 
   

2) What exactly does LangChain and LlamaIndex do? Can't I just use Chroma to query content and inject the queried data i
nto the prompt, or it's a lot more complicated than just injecting additional content? 
   
3) Does anybody know of any 
simplified code examples that show what LangChain and LlamaIndex do? I've found some Reddit post of people saying they r
olled their implementation and that these frameworks are overkill, I'd love to learn too if that's the case! :)
   
4) I
 see a lot of hate towards LangChain and most people seem to recommend LLamaIndex. Is the hate justified or is this hate
 due to LangChain being more modular compared to LlamaIndex?
   
To be honest, so far LangChain seems to offer more copy
 and paste examples I can learn from. I use it with **llama.cpp**
   
5) Is LangChain free for commercial use? I noticed
 there's a *pricing* section on their website. I checked their GitHub profile and LangChain seems to be under an MIT lic
ense. Better to know this before investing more time into it.
 
6) Is LangChain and LlamaIndex only available in Python 
or JavaScript? I was hoping to use it in c++ or rust.

Thanks!
```
---

     
 
all -  [ RAGAS vs GISKARD RAG Evaluation ](https://www.reddit.com/r/LangChain/comments/1boiq77/ragas_vs_giskard_rag_evaluation/) , 2024-03-28-0910
```
Hi,

my go to tool for RAG Evaluation has been RAGAS so far, but i am not always happy with rhe results. Now I saw a vid
eo about GISKARD evaluation which also looks promising.

So my question: has anybody some experiene wirh Giskard or both
, and what do you like better?
```
---

     
 
all -  [ Summarize Long Text - Meeting Notes/Minutes ](https://www.reddit.com/r/LocalLLaMA/comments/1bofrq1/summarize_long_text_meeting_notesminutes/) , 2024-03-28-0910
```
I have been collecting meeting transcripts, and I would like to have summaries or meeting minutes created from them. Is 
there a good local solution for doing something like this? I have come across recommendations for using 13b models/langc
hain. No idea where to start but any help is greatly appreciated. 

Right now, I have tried loading models into Koboldcp
p with limited success. My ideal situation would be to upload a txt file and run a prompt for the AI to run on it to cre
ate a summary of the document. Right now, I only have NVDIA 4gb VRAM and 16gb of system RAM. I know I will need to upgra
de this going forward. 

Anyone doing something like this that can give me some pointers?
```
---

     
 
all -  [ Not enough resources to run an LLM locally ](https://www.reddit.com/r/LangChain/comments/1bo8d5h/not_enough_resources_to_run_an_llm_locally/) , 2024-03-28-0910
```
I want to build RAG system with a chatbot using an LLM with LangChain framework.

The problem is that I don't have enoug
h resources to run an LLM locally. I guess I have two options:

1. Looking for a free API that give good results

2. Fin
ding a free server-like platform to host an LLM

For option 1, do you know some good APIs ?

For option 2, I thought of 
using Google Colab as a server but wasn't able to exchange messages between my local machine and Colab. I tried ngrok li
brary but it didn't work. Is there any solution ?
```
---

     
 
all -  [ Multi-Agent Conversation using AutoGen and HuggingFace models ](https://www.reddit.com/r/LangChain/comments/1bo5zq9/multiagent_conversation_using_autogen_and/) , 2024-03-28-0910
```
Checkout this demo to understand autogen, a Multi-Agent Orchestration python package supporting AI Agents conversations 
using HuggingFace models. https://youtu.be/NY4_jhPcicw?si=IV29lMJcQ8rvWVij
```
---

     
 
all -  [ stream open source LLM ](https://www.reddit.com/r/LangChain/comments/1bo30or/stream_open_source_llm/) , 2024-03-28-0910
```
how I can stream agent output using langchain when I use mistralai/Mistral-7B-Instruct-v0.2?
```
---

     
 
all -  [ How to Stream LCEL Chain with FastAPI and return source docs? ](https://www.reddit.com/r/LangChain/comments/1bo2k4r/how_to_stream_lcel_chain_with_fastapi_and_return/) , 2024-03-28-0910
```
Hi,

I don't get it to run. I want to stream a LCEL RAG chain response using FastAPI. So my question would be how to str
eam a LCEL chain response and how can I return the whole response, so the dict with the 'answer' and 'docs' keys, where 
the retrieved docs are inside?

&#x200B;

Here is the code for my chain:

`from langchain_community.vectorstores import 
FAISS`  
`from langchain_community.embeddings import HuggingFaceEmbeddings`

`from langchain_core.prompts import PromptT
emplate, ChatPromptTemplate`  
`from langchain_core.runnables import RunnableParallel`

`from operator import itemgetter
`  
`from typing import TypedDict`

`from fastapi import FastAPI, File, UploadFile, HTTPException, Path, Query`

`embedd
ings = HuggingFaceEmbeddings(model_name='intfloat/multilingual-e5-large-instruct', model_kwargs={'device': 'mps'})`  
`d
b = FAISS.load_local('streamlit_vectorstores/vectorstores/db_maxiw_testfreitag', embeddings, allow_dangerous_deserializa
tion=True)`

`llm = build_llm(model_path)`

`template = '''`  
`Beantworte die Frage ausschließlich basierend auf folgen
den Kontext auf Deutsch:`  
`{context}`  
`Frage: {question}`  
`'''`  
`ANSWER_PROMPT = ChatPromptTemplate.from_templat
e(template)`  
`class RagInput(TypedDict):`  
 `question: str`  


`final_chain = (`  
 `RunnableParallel(`  
 `context=
(itemgetter('question') | db.as_retriever()),`  
 `question=itemgetter('question')`  
`) |`  
 `RunnableParallel(`  
 `a
nswer=(ANSWER_PROMPT | llm),`  
 `docs=itemgetter('context')`  
`)`  
`).with_types(input_type=RagInput)`

&#x200B;

`An
d here my get-endpoint which does not work:`

`u/app.get('/rag_lcel/')`  
`async def fastapi_stream(question: str):`  
 
`start_time = time.time()`  
 `first_response = True`  
 `for resp in final_chain.astream({'question': question}):`  
 `
if resp and first_response:`  
 `# Calculate and print time after the first batch of text is streamed`  
 `end_time = ti
me.time()`  
 `elapsed_time = round(end_time - start_time, 1)`  
 `first_response = False`   
 `yield f'(Response Time: 
{elapsed_time} seconds)\n'`  
 `yield resp` 
```
---

     
 
all -  [ Bug with structured-chat-zero-shot-react-description agent ](https://www.reddit.com/r/LangChain/comments/1bo2hpi/bug_with_structuredchatzeroshotreactdescription/) , 2024-03-28-0910
```
When conducting tests, the agent is able to determine the correct tool and parse the prompt to the correct inputs. Howev
er, often times the agent will finish the chain prematurely without making any observations. 

In my tests, all the prom
pts have been kept the same and temperature=0. 

I noticed if the agent were to successfully make an observation based o
n the used tool, it will display this on the terminal.

&#x200B;

https://preview.redd.it/8e70hpm6zmqc1.png?width=506&fo
rmat=png&auto=webp&s=07df769dc1b062a68c70c61d799ef009facf96a9

Otherwise if it was going the end the chain prematurely i
t would look like this.

&#x200B;

https://preview.redd.it/gft49igfzmqc1.png?width=532&format=png&auto=webp&s=2ab5f9d08f
68c8c62bebe4565f35142f95055617

Pardon me if I lack the understanding to solve this, but I am kinda at wits end. Thanks 
in advance.

&#x200B;
```
---

     
 
all -  [ Chat with RTX not opening ](https://www.reddit.com/r/techsupport/comments/1bo1j6p/chat_with_rtx_not_opening/) , 2024-03-28-0910
```
This may be a stupid question, but Chat with RTX is not opening properly; instead, I encounter a terminal with an error 
message. I do not have python installed on my computer, and I cannot seem to install sentence-transformer 2.5.1.   
Belo
w is the error message, thanks for your help! :  
\[03/25/2024-23:33:10\] You try to use a model that was created with v
ersion 2.5.1, however, your version is 2.2.2. This might cause unexpected behavior or errors. In that case, try to updat
e to the latest version.  
╭─────────────────────────────── Traceback (most recent call last) ──────────────────────────
──────╮  
│ C:\\Users\\username\\AppData\\Local\\NVIDIA\\ChatWithRTX\\RAG\\trt-llm-rag-windows-main\\app.py:109 in      
 │  
│ <module>                                                                                         │  
│           
                                                                                       │  
│   106 )                    
                                                                      │  
│   107                                       
                                                     │  
│   108 # create embeddings model object                       
                                    │  
│ ❱ 109 embed\_model = HuggingFaceEmbeddings(model\_name=embedded\_model)       
                      │  
│   110 service\_context = ServiceContext.from\_defaults(llm=llm, embed\_model=embed\_model,  
         │  
│   111 │   │   │   │   │   │   │   │   │   │   │      context\_window=model\_config\['max\_input\_to   │  

│   112 │   │   │   │   │   │   │   │   │   │   │      chunk\_overlap=200)                          │  
│              
                                                                                    │  
│ C:\\Users\\username\\AppData\\
Local\\NVIDIA\\ChatWithRTX\\env\_nvd\_rag\\lib\\site-packages\\langchain\\embeddin │  
│ gs\\huggingface.py:66 in \_\_in
it\_\_                                                                 │  
│                                            
                                                      │  
│    63 │   │   │   │   'Please install it with \`pip install 
sentence-transformers\`.'              │  
│    64 │   │   │   ) from exc                                               
                      │  
│    65 │   │                                                                                 
     │  
│ ❱  66 │   │   self.client = sentence\_transformers.SentenceTransformer(                           │  
│    67
 │   │   │   self.model\_name, cache\_folder=self.cache\_folder, \*\*self.model\_kwargs           │  
│    68 │   │   ) 
                                                                                 │  
│    69                            
                                                                │  
│                                                   
                                               │  
│ C:\\Users\\username\\AppData\\Local\\NVIDIA\\ChatWithRTX\\env\_nvd\
_rag\\lib\\site-packages\\sentence\_transform │  
│ ers\\SentenceTransformer.py:95 in \_\_init\_\_                      
                                  │  
│                                                                                 
                 │  
│    92 │   │   │   │   │   │   │   │   │   │   use\_auth\_token=use\_auth\_token)                 
    │  
│    93 │   │   │                                                                                  │  
│    94 │
   │   │   if os.path.exists(os.path.join(model\_path, 'modules.json')):    #Load as Sen   │  
│ ❱  95 │   │   │   │   m
odules = self.\_load\_sbert\_model(model\_path)                               │  
│    96 │   │   │   else:   #Load with
 AutoModel                                                   │  
│    97 │   │   │   │   modules = self.\_load\_auto\_mo
del(model\_path)                                │  
│    98                                                             
                               │  
│                                                                                    
              │  
│ C:\\Users\\username\\AppData\\Local\\NVIDIA\\ChatWithRTX\\env\_nvd\_rag\\lib\\site-packages\\sentenc
e\_transform │  
│ ers\\SentenceTransformer.py:840 in \_load\_sbert\_model                                              
│  
│                                                                                                  │  
│   837 │   │
   modules = OrderedDict()                                                            │  
│   838 │   │   for module\_co
nfig in modules\_config:                                               │  
│   839 │   │   │   module\_class = import\_f
rom\_string(module\_config\['type'\])                       │  
│ ❱ 840 │   │   │   module = module\_class.load(os.path.
join(model\_path, module\_config\['path'\]))    │  
│   841 │   │   │   modules\[module\_config\['name'\]\] = module    
                                    │  
│   842 │   │                                                                   
                   │  
│   843 │   │   return modules                                                                   
  │  
│                                                                                                  │  
│ C:\\Users
\\username\\AppData\\Local\\NVIDIA\\ChatWithRTX\\env\_nvd\_rag\\lib\\site-packages\\sentence\_transform │  
│ ers\\model
s\\Pooling.py:120 in load                                                                │  
│                          
                                                                        │  
│   117 │   │   with open(os.path.join(input
\_path, 'config.json')) as fIn:                         │  
│   118 │   │   │   config = json.load(fIn)                 
                                       │  
│   119 │   │                                                                
                      │  
│ ❱ 120 │   │   return Pooling(\*\*config)                                                    
       │  
│   121                                                                                            │  
╰─────
─────────────────────────────────────────────────────────────────────────────────────────────╯  
TypeError: Pooling.\_\_
init\_\_() got an unexpected keyword argument 'pooling\_mode\_weightedmean\_tokens'  
Press any key to continue . . .  


```
---

     
 
all -  [ Accessing Local LLMs using Ollama  ](https://www.reddit.com/r/learnmachinelearning/comments/1bnz7vm/accessing_local_llms_using_ollama/) , 2024-03-28-0910
```
In my 150th blog post, I've discussed how to access local LLMs (including multi-modal) using Ollama without any codes an
d integration with python and LangChain as well for building Generative AI applications: https://medium.com/data-science
-in-your-pocket/local-llms-using-ollama-3f631b855e8f
```
---

     
 
all -  [ Agent is not using a custom tool ](https://www.reddit.com/r/LangChain/comments/1bnmezm/agent_is_not_using_a_custom_tool/) , 2024-03-28-0910
```
Hello,



I am trying to create a workflow where the agents receive an API specification, make improvements on it and sa
ve it to a different file. I am using the example from LangChain on how to build hierarchical teams and I have created a
n 'API Enhancement Team' with two agents.

[https://github.com/langchain-ai/langgraph/blob/main/examples/multi\_agent/hi
erarchical\_agent\_teams.ipynb](https://github.com/langchain-ai/langgraph/blob/main/examples/multi_agent/hierarchical_ag
ent_teams.ipynb)

One agent that will read a YAML file and provide suggestions on what needs to be improved. And one age
nt that will apply the changes to the specification and save the file.

I have created the following tools:

    @tool
 
   def read_api_spec_from_yaml(file_path: str) -> Dict:
        '''Reads an API specification from a YAML file.'''
     
   with open(file_path, 'r', encoding='utf-8') as file:
            api_spec = yaml.safe_load(file)
        print('Succe
ssfully read the API spec from the file.')
        return api_spec
    

    @tool
    def save_improved_spec(spec_data,
 filename, directory='Improved Specs'):
        '''
        Saves the improved API specification to a file in the specif
ied directory.
        If the file exists, it saves it with an incremented version suffix before the file extension.
   
 
        :param spec_data: The API specification data to save.
        :param filename: The base filename for the saved
 specification.
        :param directory: The directory where the file will be saved. Defaults to 'Improved Specs'.
    
    '''
        # Ensure the directory exists
        if not os.path.exists(directory):
            os.makedirs(director
y)
    
        # Split the filename to insert version suffix before the extension
        name, extension = os.path.spl
itext(filename)
    
        # Construct the base filepath without the extension
        base_filepath = os.path.join(di
rectory, name)
        filepath = base_filepath + extension  # Initial assumption: no version needed
    
        # Chec
k for existing files and increment version suffix if necessary
        version = 1
        while os.path.exists(filepath
):
            filepath = f'{base_filepath}_v{version}{extension}'
            version += 1
    
        # Write the spe
cification data to the file
        with open(filepath, 'w') as file:
            json.dump(spec_data, file, indent=4)
 
   
        print(f'Specification saved as {os.path.basename(filepath)} in '{directory}' directory.')
    

And I have d
efined the following agents:

    api_spec_expert = create_agent(
        llm,
        [read_api_spec_from_yaml], 
     
   api_spec_expert_prompt,
    )
    api_spec_expert_node = functools.partial(agent_node, agent=api_spec_expert, name='A
PI Spec Expert')
    
    api_improver = create_agent(
        llm,
        [save_improved_spec],
        api_improver_p
rompt
    )
    api_improver_node = functools.partial(agent_node, agent=api_improver, name='API Spec Improver')

The exp
ert is successfully reading the file and providing recommendations, but the improver is not using the tool and gives me 
very generic answers, like:

>Given the detailed list of enhancement suggestions for the OpenAI API specification, I wil
l now proceed to apply these enhancements to the specification document. This process involves updating the OpenAI API s
pecification (\`openai\_oas.yaml\`) according to the provided suggestions, ensuring that the documentation becomes more 
comprehensive, user-friendly, and helpful for developers.

Any advice, insights, or shared experiences with similar chal
lenges would be greatly appreciated. I'm eager to learn from the community and find a solution.



Thank you in advance.

```
---

     
 
all -  [ How to enable streaming in SagemakerEndpoint ](https://www.reddit.com/r/LangChain/comments/1bnlwrj/how_to_enable_streaming_in_sagemakerendpoint/) , 2024-03-28-0910
```
Hey everyone, 

I've got my LLM up and running using the Langchain SagemakerEndpoint class, and it's all good. However, 
because it's a RAG application, the response time isn't as snappy as I'd like. So, I started looking into ways to speed 
things up and came across the streaming feature.

Excited to try, I checked out the documentation and set the streaming 
parameter to True. But instead of speeding things up, my model got stuck in an infinite loop with no response.

Digging 
deeper, I took a look at the source code of the SagemakerEndpoint class to see what's causing the issue. Turns out, it's
 something to do with the Langchain method being used. Interestingly, when I bypass Langchain, everything works fine.

N
ow, I'm a bit perplexed. Any ideas on how to tackle this problem? Your help would be greatly appreciated!
```
---

     
 
all -  [ Update: Langtrace Preview: Opensource LLM monitoring tool - achieving better cardinality compared to ](https://www.reddit.com/r/LangChain/comments/1bnkvtv/update_langtrace_preview_opensource_llm/) , 2024-03-28-0910
```
This is a follow up for: [https://www.reddit.com/r/LangChain/comments/1b6phov/update\_langtrace\_preview\_an\_opensource
\_llm/](https://www.reddit.com/r/LangChain/comments/1b6phov/update_langtrace_preview_an_opensource_llm/)  


Thought of 
sharing what I am cooking. Basically, I am building a open source LLM monitoring and evaluation suite. It works like thi
s:  
1. Install the SDK with 2 lines of code (npm i or pip install)  
2. The SDK will start shipping traces in Open tele
metry standard format to the UI  
3. See the metrics, traces and prompts in the UI(Attaching some screenshots below).  



I am mostly optimizing the features for 3 main metrics  
1. Usage - token/cost  
2. Accuracy - Manually evaluate trace
d prompt-response pairs from the UI and see the accuracy score  
3. Latency - speed of responses/time to first token  



Vendors supported for the first version:  
Langchain, LlamaIndex, OpenAI, Anthropic, Pinecone, ChromaDB  


I will open
source this project in about a week and share the repo here.

Please let me know what else you would like to see or what
 other challenges you face that can be solved through this project.

&#x200B;

https://preview.redd.it/zwz0lqcfwiqc1.png
?width=2978&format=png&auto=webp&s=90caa5f52e47503493e4417b6808d7f12739f2d3

https://preview.redd.it/cvv6aqcfwiqc1.png?w
idth=3000&format=png&auto=webp&s=e8374335d6e5b5a7ff04f1ea1408f74f9dce1698

 
```
---

     
 
all -  [ Best way to do indexing and pull in other data sources when working with LangChain and datasets > 10 ](https://www.reddit.com/r/LangChain/comments/1bnkgfb/best_way_to_do_indexing_and_pull_in_other_data/) , 2024-03-28-0910
```
I'm trying to understand what are typical workflows for users/teams especially in production when working with datasets 
that are > 10+ GB.  
Specifically, I have at least three data sources that I want to create embeddings for. Unstructured
 data documents, multiple tables in data warehouses, and other semi-structured data from APIs.   
Here is what I am face
d with. Doing even medium-to-large scale data processing natively with LangChain is hard, just because python is slow fo
r such scale. Yes, I can use Ray but that creates a lot more modules to manage and it's already hard with LangChain code
-base.  
So in-general how are people doing ingestion in conjunction with LangChain ? This maybe a mistake on my part, b
ut I do not want to use LangChain for ingestion, it's not meant imo for that problem.  


Secondly, has anyone used Trac
es with LangSmith and can share experiences about it ?
```
---

     
 
all -  [ FREE Email Course on LangChain (Basics + Applications + Coding + Colab Notebook all included) (8 Day ](https://www.reddit.com/r/AICareer/comments/1bnikze/free_email_course_on_langchain_basics/) , 2024-03-28-0910
```
Discover how LangChain, an innovative open-source framework, simplifies the construction of advanced applications such a
s sentiment analysis tools and chatbots by bridging language models with external data. Dive into the core components of
 LangChain, including LLMs, Prompt Templates, Indexes, and Retrievers, to democratize AI and push your projects to the f
orefront of innovation.  
**Register Here:** [*https://embeds.beehiiv.com/397c20c8-d131-4414-bea1-39617c373584*](https:/
/embeds.beehiiv.com/397c20c8-d131-4414-bea1-39617c373584?utm_source=www.airesearchinsights.com&utm_medium=referral)
```
---

     
 
all -  [ Can someone please help to know how to tune context/retriever in the langchain? ](https://www.reddit.com/r/LangChain/comments/1bnfpd0/can_someone_please_help_to_know_how_to_tune/) , 2024-03-28-0910
```
I am using ChromaDb as my vectorstore. 

&#x200B;

Code : 

\`\`\`

from langchain\_core.prompts import ChatPromptTempla
te  
from langchain\_core.runnables import RunnablePassthrough  
from langchain\_core.output\_parsers import StrOutputPa
rser

from langchain.chat\_models import ChatOpenAI  


template = '''You are an expert in the screenplay and able to fi
nd out any questions asked from the script, if you provide wrong information then an innocent person dies:  
{context}  

Question: {question}  
'''  
prompt = ChatPromptTemplate.from\_template(template)

model = ChatOpenAI(temperature = 0.1
)  
chain = (  
{'context': retriever, 'question': RunnablePassthrough()}  
 | prompt  
 | model  
 | StrOutputParser()


\`\`\` 

Here When I am going over the logs. The {context} is populated with irrelevant options and hence the prompt is
 not able to give the right results. Can someone please help?

&#x200B;
```
---

     
 
all -  [ Interactive LLM scripting playground ](https://www.reddit.com/r/LangChain/comments/1bndoz4/interactive_llm_scripting_playground/) , 2024-03-28-0910
```
Hey guys. I'm making an interactive LLM scripting playground - like the OpenAI playground, but using javascript so you c
an do some fancy stuff. Please take a look and give me some feedback. (Not LangChain, but pretty closely releated)

[Ret
ortJS Playground](https://stackblitz.com/fork/github/retort-js/playground?file=retort%2Fscript-template.rt.js&hideNaviga
tion=1&showSidebar=0) 
```
---

     
 
all -  [ Structured Chat Agent Formatting Help ](https://www.reddit.com/r/LangChain/comments/1bnd7yc/structured_chat_agent_formatting_help/) , 2024-03-28-0910
```
Does anyone know how to adjust the format instructions when using the structured chat agent? It avoids displaying the Ob
servation and sometimes cuts out the Thought process despite indicating the format instructions in the prompt. I am tryi
ng to use this agent to connect with an SQL database.
```
---

     
 
all -  [ How to  create a openai compactible local server using langchain  ](https://www.reddit.com/r/LangChain/comments/1bnclwv/how_to_create_a_openai_compactible_local_server/) , 2024-03-28-0910
```
Hey there im looking create a robot which uses llm as way of interaction. I want the entire system to be local hosted us
ing langchain (due to the option for customising promt as well as other parameters)

Im using mistral 7b gguf 
 
But the
 tools i use require apu in open ai format and i dont know how host the model in a local server so that it can be used a
s a replacement for open ai api

So now im looking for a solution to host the model in a local server that can be used a
s replacement for open ai i have tried langserve but shows error that it isnt in open ai format 

Can anyone please help
 me
```
---

     
 
all -  [ Error while executing langchain model ](https://www.reddit.com/r/LangChain/comments/1bnc8ol/error_while_executing_langchain_model/) , 2024-03-28-0910
```
 

Hi All,   

I am just trying to get answer to a basic question by calling the llm chain model using python but i am g
etting the **'list index out of range error'** when i run the model using run method or invoke method   

Please suggest
 what could be the solution. Attaching the code snippet below for reference   

Am using python 3.12 version.

**code sn
ippet**   

openai\_api\_key = os.environ\['OPENAI\_API\_KEY'\] 

print(openai\_api\_key) 

from langchain\_openai impor
t OpenAI 

from langchain.prompts import PromptTemplate 

my\_creative\_llm=OpenAI(temperature=0.9) 

template='mention 
pointwise' 

prompt=PromptTemplate.from\_template(template) 

from langchain.chains import LLMChain 

llm\_chain=LLMChai
n(prompt=prompt,llm=my\_creative\_llm) 

question='what are some best places to see in America?' 

print(llm\_chain.run(
question)) 

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\
_\_\_\_\_\_\_\_

**complete error** 

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

IndexError                                Traceback (most recent call last) 


Cell In\[60\], line 1 

\----> 1 print(llm\_chain.run(question)) 

File  \~\\AppData\\Local\\Programs\\Python\\Python312
\\Lib\\site-packages\\langchain\_core\\\_api\\deprecation.py:145,  in  deprecated.<locals>.deprecate.<locals>.warning\_e
mitting\_wrapper(\*args,  \*\*kwargs) 

143     warned = True 

144     emit\_warning() 

\--> 145 return wrapped(\*args
, \*\*kwargs) 

File  \~\\AppData\\Local\\Programs\\Python\\Python312\\Lib\\site-packages\\langchain\\chains\\base.py:54
5,  in Chain.run(self, callbacks, tags, metadata, \*args, \*\*kwargs) 

543     if len(args) != 1: 

544         raise V
alueError('\`run\` supports only one positional argument.') 

\--> 545     return self(args\[0\], callbacks=callbacks, t
ags=tags, metadata=metadata)\[ 

546         \_output\_key 

547     \] 

549 if kwargs and not args: 

550     return s
elf(kwargs, callbacks=callbacks, tags=tags, metadata=metadata)\[ 

551         \_output\_key 

552     \] 

File  \~\\Ap
pData\\Local\\Programs\\Python\\Python312\\Lib\\site-packages\\langchain\_core\\\_api\\deprecation.py:145,  in  deprecat
ed.<locals>.deprecate.<locals>.warning\_emitting\_wrapper(\*args,  \*\*kwargs) 

143     warned = True 

144     emit\_w
arning() 

\--> 145 return wrapped(\*args, \*\*kwargs) 

File  \~\\AppData\\Local\\Programs\\Python\\Python312\\Lib\\sit
e-packages\\langchain\\chains\\base.py:378,  in Chain.\_\_call\_\_(self, inputs, return\_only\_outputs, callbacks, tags,
  metadata, run\_name, include\_run\_info) 

346 '''Execute the chain. 

347 

348 Args: 

(...) 

369         \`Chain.o
utput\_keys\`. 

370 ''' 

371 config = { 

372     'callbacks': callbacks, 

373     'tags': tags, 

374     'metadata'
: metadata, 

375     'run\_name': run\_name, 

376 } 

\--> 378 return self.invoke( 

379     inputs, 

380     cast(Ru
nnableConfig, {k: v for k, v in config.items() if v is not None}), 

381     return\_only\_outputs=return\_only\_outputs
, 

382     include\_run\_info=include\_run\_info, 

383 ) 

File  \~\\AppData\\Local\\Programs\\Python\\Python312\\Lib\
\site-packages\\langchain\\chains\\base.py:133,  in Chain.invoke(self, input, config, \*\*kwargs) 

130 include\_run\_in
fo = kwargs.get('include\_run\_info', False) 

131 return\_only\_outputs = kwargs.get('return\_only\_outputs', False) 


\--> 133 inputs = self.prep\_inputs(input) 

134 callback\_manager = CallbackManager.configure( 

135     callbacks, 

1
36     self.callbacks, 

(...) 

141     self.metadata, 

142 ) 

143 new\_arg\_supported = inspect.signature(self.\_cal
l).parameters.get('run\_manager') 

File  \~\\AppData\\Local\\Programs\\Python\\Python312\\Lib\\site-packages\\langchain
\\chains\\base.py:479,  in Chain.prep\_inputs(self, inputs) 

475     if self.memory is not None: 

476         # If the
re are multiple input keys, but some get set by memory so that 

477         # only one is not set, we can still figure 
out which key it is. 

478         \_input\_keys = \_input\_keys.difference(self.memory.memory\_variables) 

\--> 479   
  inputs = {list(\_input\_keys)\[0\]: inputs} 

480 if self.memory is not None: 

481     external\_context = self.memor
y.load\_memory\_variables(inputs) 

IndexError: list index out of range 
```
---

     
 
all -  [ Error while executing langchain model ](https://www.reddit.com/r/learnpython/comments/1bna9a1/error_while_executing_langchain_model/) , 2024-03-28-0910
```
Hi All,

I am just trying to get answer to a basic question by calling the llm chain model using python but i am getting
 the **'list index out of range error'** when i run the model using run method or invoke method

Please suggest what cou
ld be the solution. Attaching the code snippet below for reference

Am using python 3.12 version.

**openai\_api\_key = 
os.environ\['OPENAI\_API\_KEY'\]**

**print(openai\_api\_key)**

**from langchain\_openai import OpenAI**

**from langch
ain.prompts import PromptTemplate**

**my\_creative\_llm=OpenAI(temperature=0.9)**

**template='mention pointwise'**

**
prompt=PromptTemplate.from\_template(template)**

**from langchain.chains import LLMChain**

**llm\_chain=LLMChain(promp
t=prompt,llm=my\_creative\_llm)**

**question='what are some best places to see in America?'**

**print(llm\_chain.run(q
uestion))**

  
**complete error**

**\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_**

**IndexError                              
  Traceback (most recent call last)**

**Cell In\[60\], line 1**

**----> 1 print(llm\_chain.run(question))**

**File \~
\\AppData\\Local\\Programs\\Python\\Python312\\Lib\\site-packages\\langchain\_core\\\_api\\deprecation.py:145, in deprec
ated.<locals>.deprecate.<locals>.warning\_emitting\_wrapper(\*args, \*\*kwargs)**

**143     warned = True**

**144     
emit\_warning()**

**--> 145 return wrapped(\*args, \*\*kwargs)**

**File \~\\AppData\\Local\\Programs\\Python\\Python31
2\\Lib\\site-packages\\langchain\\chains\\base.py:545, in Chain.run(self, callbacks, tags, metadata, \*args, \*\*kwargs)
**

**543     if len(args) != 1:**

**544         raise ValueError('\`run\` supports only one positional argument.')**


**--> 545     return self(args\[0\], callbacks=callbacks, tags=tags, metadata=metadata)\[**

**546         \_output\_key
**

**547     \]**

**549 if kwargs and not args:**

**550     return self(kwargs, callbacks=callbacks, tags=tags, metad
ata=metadata)\[**

**551         \_output\_key**

**552     \]**

**File \~\\AppData\\Local\\Programs\\Python\\Python312
\\Lib\\site-packages\\langchain\_core\\\_api\\deprecation.py:145, in deprecated.<locals>.deprecate.<locals>.warning\_emi
tting\_wrapper(\*args, \*\*kwargs)**

**143     warned = True**

**144     emit\_warning()**

**--> 145 return wrapped(\
*args, \*\*kwargs)**

**File \~\\AppData\\Local\\Programs\\Python\\Python312\\Lib\\site-packages\\langchain\\chains\\bas
e.py:378, in Chain.\_\_call\_\_(self, inputs, return\_only\_outputs, callbacks, tags, metadata, run\_name, include\_run\
_info)**

**346 '''Execute the chain.**

**347** 

**348 Args:**

   **(...)**

**369         \`Chain.output\_keys\`.**


**370 '''**

**371 config = {**

**372     'callbacks': callbacks,**

**373     'tags': tags,**

**374     'metadata': 
metadata,**

**375     'run\_name': run\_name,**

**376 }**

**--> 378 return self.invoke(**

**379     inputs,**

**380
     cast(RunnableConfig, {k: v for k, v in config.items() if v is not None}),**

**381     return\_only\_outputs=return
\_only\_outputs,**

**382     include\_run\_info=include\_run\_info,**

**383 )**

**File \~\\AppData\\Local\\Programs\\
Python\\Python312\\Lib\\site-packages\\langchain\\chains\\base.py:133, in Chain.invoke(self, input, config, \*\*kwargs)*
*

**130 include\_run\_info = kwargs.get('include\_run\_info', False)**

**131 return\_only\_outputs = kwargs.get('retur
n\_only\_outputs', False)**

**--> 133 inputs = self.prep\_inputs(input)**

**134 callback\_manager = CallbackManager.co
nfigure(**

**135     callbacks,**

**136     self.callbacks,**

   **(...)**

**141     self.metadata,**

**142 )**

**
143 new\_arg\_supported = inspect.signature(self.\_call).parameters.get('run\_manager')**

**File \~\\AppData\\Local\\Pr
ograms\\Python\\Python312\\Lib\\site-packages\\langchain\\chains\\base.py:479, in Chain.prep\_inputs(self, inputs)**

**
475     if self.memory is not None:**

**476         # If there are multiple input keys, but some get set by memory so t
hat**

**477         # only one is not set, we can still figure out which key it is.**

**478         \_input\_keys = \_
input\_keys.difference(self.memory.memory\_variables)**

**--> 479     inputs = {list(\_input\_keys)\[0\]: inputs}**

**
480 if self.memory is not None:**

**481     external\_context = self.memory.load\_memory\_variables(inputs)**

**IndexE
rror: list index out of range**

  


Thanks,

Surya
```
---

     
 
all -  [ Please explain response evaluation Flow, llama index ](https://www.reddit.com/r/LangChain/comments/1bn9mt2/please_explain_response_evaluation_flow_llama/) , 2024-03-28-0910
```
    evaluator_c = CorrectnessEvaluator(llm=eval_llm)
    evaluator_s = SemanticSimilarityEvaluator()
    evaluator_r = R
elevancyEvaluator(llm=eval_llm)
    evaluator_f = FaithfulnessEvaluator(llm=eval_llm)
    
    pairwise_evaluator = Pair
wiseComparisonEvaluator(llm=eval_llm)
    
    max_samples = 5
    
    eval_qs = eval_dataset.questions
    qr_pairs = 
eval_dataset.qr_pairs
    ref_response_strs = [r for (_, r) in qr_pairs]
    
    base_query_engine = vector_indices[-1]
.as_query_engine(similarity_top_k=2)
    
    query_engine = RetrieverQueryEngine(retriever, node_postprocessors=[rerank
er])
    
    base_pred_responses = get_responses(
        eval_qs[:max_samples], base_query_engine, show_progress=True

    )
    
    pred_responses = get_responses(
        eval_qs[:max_samples], query_engine, show_progress=True
    )
   
 
    pred_response_strs = [str(p) for p in pred_responses]
    base_pred_response_strs = [str(p) for p in base_pred_res
ponses]
    
    evaluator_dict = {
        'correctness': evaluator_c,
        'faithfulness': evaluator_f,
        're
levancy': evaluator_r,
        'semantic_similarity': evaluator_s,
    }
    batch_runner = BatchEvalRunner(evaluator_di
ct, workers=1, show_progress=True)
    
    eval_results = await batch_runner.aevaluate_responses(
        queries=eval_
qs[:max_samples],
        responses=pred_responses[:max_samples],
        reference=ref_response_strs[:max_samples],
   
 )
    
    base_eval_results = await batch_runner.aevaluate_responses(
        queries=eval_qs[:max_samples],
        r
esponses=base_pred_responses[:max_samples],
        reference=ref_response_strs[:max_samples],
    )
    
    results_df
 = get_results_df(
        [eval_results, base_eval_results],
        ['Ensemble Retriever', 'Base Retriever'],
        
['correctness', 'faithfulness', 'semantic_similarity'],
    )
    display(results_df)

What kind of flow is the evaluati
on carried out?   


I created an eval dataset using gpt4 and am curious about how this is used for evaluation.    
The 
questions and answers have already been created with eval llm.   
What flow is used to compare them?   
Does the retriev
er generate and answer questions again? Or something?   
I really don't understand, please explain
```
---

     
 
all -  [ Seeking Advice on Routing User Queries to Specific Endpoints for Natural Language Search ](https://www.reddit.com/r/LangChain/comments/1bn9m6m/seeking_advice_on_routing_user_queries_to/) , 2024-03-28-0910
```
Hello everyone,

I'm currently developing a feature for natural language search queries. This feature enables users to p
ose questions to a knowledge base or retrieve structured/document data directly from a database. To facilitate this, I'v
e established two distinct endpoints:

1. /api/knowledgesearch for knowledge base queries.

2. /api/documentsearch for r
etrieving document data.

I'm seeking guidance on how to effectively route user queries from the search interface to the
 appropriate endpoint. Any suggestions on how to implement this would be greatly appreciated.
```
---

     
 
all -  [ Context length Issue of gemini-1.0-pro-001 ](https://www.reddit.com/r/Bard/comments/1bn8ypy/context_length_issue_of_gemini10pro001/) , 2024-03-28-0910
```
At vertex AI Prompt UI I am able to use longer  text (20k) token and get a response however when i am invoking the same 
model from my program I get the following error :-  


I am pretty sure its due to context length. What i am not clear o
n is why same text as context works fine at the Vertex AI UI but not through my program:  


    pro_model = ChatVertexA
I(model='gemini-1.0-pro-001',
                        max_output_tokens=2048,
                        temperature=0.9,
 
                       top_p=1,
                        top_k=0)


Here is the error :

    
    -----------------------
----------------------------------------------------
    _MultiThreadedRendezvous                  Traceback (most recen
t call last)
    File /usr/local/lib/python3.9/dist-packages/google/api_core/grpc_helpers.py:170, in _wrap_stream_errors
.<locals>.error_remapped_callable(*args, **kwargs)
        169     prefetch_first = getattr(callable_, '_prefetch_first_
result_', True)
    --> 170     return _StreamingResponseIterator(
        171         result, prefetch_first_result=pre
fetch_first
        172     )
        173 except grpc.RpcError as exc:
    
    File /usr/local/lib/python3.9/dist-packa
ges/google/api_core/grpc_helpers.py:92, in _StreamingResponseIterator.__init__(self, wrapped, prefetch_first_result)
   
      91     if prefetch_first_result:
    ---> 92         self._stored_first_result = next(self._wrapped)
         93 e
xcept TypeError:
         94     # It is possible the wrapped method isn't an iterable (a grpc.Call
         95     # fo
r instance). If this happens don't store the first result.
    
    File /usr/local/lib/python3.9/dist-packages/grpc/_ch
annel.py:542, in _Rendezvous.__next__(self)
        541 def __next__(self):
    --> 542     return self._next()
    
   
 File /usr/local/lib/python3.9/dist-packages/grpc/_channel.py:968, in _MultiThreadedRendezvous._next(self)
        967 e
lif self._state.code is not None:
    --> 968     raise self
    
    _MultiThreadedRendezvous: <_MultiThreadedRendezvou
s of RPC that terminated with:
    	status = StatusCode.INVALID_ARGUMENT
    	details = 'Request contains an invalid arg
ument.'
    	debug_error_string = 'UNKNOWN:Error received from peer ipv4:142.250.80.74:443 {created_time:'2024-03-25T08:
28:43.720003509+00:00', grpc_status:3, grpc_message:'Request contains an invalid argument.'}'
    >
    
    The above e
xception was the direct cause of the following exception:
    
    InvalidArgument                           Traceback (
most recent call last)
    Cell In [17], line 34
         30 context  = retrieve_context_from_local_embeddings(query)
  
       32 user_memory.load_memory_variables({})
    ---> 34 for e in chain.stream({'context': context, 'question': query
, 'history': user_memory}):
         35     print(e, end='')
         36 print()
    
    File /usr/local/lib/python3.9/
dist-packages/langchain_core/runnables/base.py:2685, in RunnableSequence.stream(self, input, config, **kwargs)
       26
79 def stream(
       2680     self,
       2681     input: Input,
       2682     config: Optional[RunnableConfig] = No
ne,
       2683     **kwargs: Optional[Any],
       2684 ) -> Iterator[Output]:
    -> 2685     yield from self.transfor
m(iter([input]), config, **kwargs)
    
    File /usr/local/lib/python3.9/dist-packages/langchain_core/runnables/base.py
:2672, in RunnableSequence.transform(self, input, config, **kwargs)
       2666 def transform(
       2667     self,
   
    2668     input: Iterator[Input],
       2669     config: Optional[RunnableConfig] = None,
       2670     **kwargs: 
Optional[Any],
       2671 ) -> Iterator[Output]:
    -> 2672     yield from self._transform_stream_with_config(
       
2673         input,
       2674         self._transform,
       2675         patch_config(config, run_name=(config or {}
).get('run_name') or self.name),
       2676         **kwargs,
       2677     )
    
    File /usr/local/lib/python3.9/
dist-packages/langchain_core/runnables/base.py:1743, in Runnable._transform_stream_with_config(self, input, transformer,
 config, run_type, **kwargs)
       1741 try:
       1742     while True:
    -> 1743         chunk: Output = context.ru
n(next, iterator)  # type: ignore
       1744         yield chunk
       1745         if final_output_supported:
    
  
  File /usr/local/lib/python3.9/dist-packages/langchain_core/runnables/base.py:2636, in RunnableSequence._transform(self
, input, run_manager, config)
       2627 for step in steps:
       2628     final_pipeline = step.transform(
       262
9         final_pipeline,
       2630         patch_config(
       (...)
       2633         ),
       2634     )
    ->
 2636 for output in final_pipeline:
       2637     yield output
    
    File /usr/local/lib/python3.9/dist-packages/la
ngchain_core/output_parsers/transform.py:50, in BaseTransformOutputParser.transform(self, input, config, **kwargs)
     
    44 def transform(
         45     self,
         46     input: Iterator[Union[str, BaseMessage]],
         47     co
nfig: Optional[RunnableConfig] = None,
         48     **kwargs: Any,
         49 ) -> Iterator[T]:
    ---> 50     yiel
d from self._transform_stream_with_config(
         51         input, self._transform, config, run_type='parser'
       
  52     )
    
    File /usr/local/lib/python3.9/dist-packages/langchain_core/runnables/base.py:1718, in Runnable._tran
sform_stream_with_config(self, input, transformer, config, run_type, **kwargs)
       1716 input_for_tracing, input_for_
transform = tee(input, 2)
       1717 # Start the input iterator to ensure the input runnable starts before this one
   
 -> 1718 final_input: Optional[Input] = next(input_for_tracing, None)
       1719 final_input_supported = True
       17
20 final_output: Optional[Output] = None
    
    File /usr/local/lib/python3.9/dist-packages/langchain_core/runnables/b
ase.py:1226, in Runnable.transform(self, input, config, **kwargs)
       1219             raise TypeError(
       1220  
               f'Failed while trying to add together '
       1221                 f'type {type(final)} and {type(chunk)
}.'
       1222                 f'These types should be addable for transform to work.'
       1223             )
      
 1225 if got_first_val:
    -> 1226     yield from self.stream(final, config, **kwargs)
    
    File /usr/local/lib/pyt
hon3.9/dist-packages/langchain_core/language_models/chat_models.py:239, in BaseChatModel.stream(self, input, config, sto
p, **kwargs)
        232 except BaseException as e:
        233     run_manager.on_llm_error(
        234         e,
   
     235         response=LLMResult(
        236             generations=[[generation]] if generation else []
        23
7         ),
        238     )
    --> 239     raise e
        240 else:
        241     run_manager.on_llm_end(LLMResul
t(generations=[[generation]]))
    
    File /usr/local/lib/python3.9/dist-packages/langchain_core/language_models/chat_
models.py:222, in BaseChatModel.stream(self, input, config, stop, **kwargs)
        220 generation: Optional[ChatGenerat
ionChunk] = None
        221 try:
    --> 222     for chunk in self._stream(
        223         messages, stop=stop, ru
n_manager=run_manager, **kwargs
        224     ):
        225         chunk.message.response_metadata = _gen_info_and_m
sg_metadata(chunk)
        226         yield chunk.message
    
    File /usr/local/lib/python3.9/dist-packages/langchai
n_community/chat_models/vertexai.py:378, in ChatVertexAI._stream(self, messages, stop, run_manager, **kwargs)
        37
6     chat = self._start_chat(history, **params)
        377     responses = chat.send_message_streaming(question.conten
t, **params)
    --> 378 for response in responses:
        379     chunk = ChatGenerationChunk(message=AIMessageChunk(c
ontent=response.text))
        380     if run_manager:
    
    File /usr/local/lib/python3.9/dist-packages/vertexai/lan
guage_models/_language_models.py:2759, in _ChatSessionBase.send_message_streaming(self, message, max_output_tokens, temp
erature, top_k, top_p, stop_sequences)
       2755 prediction_service_client = self._model._endpoint._prediction_client

       2757 full_response_text = ''
    -> 2759 for (
       2760     prediction_dict
       2761 ) in _streaming_predic
tion.predict_stream_of_dicts_from_single_dict(
       2762     prediction_service_client=prediction_service_client,
    
   2763     endpoint_name=self._model._endpoint_name,
       2764     instance=prediction_request.instance,
       2765 
    parameters=prediction_request.parameters,
       2766 ):
       2767     prediction_response = aiplatform.models.Pre
diction(
       2768         predictions=[prediction_dict],
       2769         deployed_model_id='',
       2770     )

       2771     text_generation_response = self._parse_chat_prediction_response(
       2772         prediction_response
=prediction_response
       2773     )
    
    File /usr/local/lib/python3.9/dist-packages/google/cloud/aiplatform/_str
eaming_prediction.py:212, in predict_stream_of_dicts_from_single_dict(prediction_service_client, endpoint_name, instance
, parameters)
        195 def predict_stream_of_dicts_from_single_dict(
        196     prediction_service_client: predi
ction_service.PredictionServiceClient,
        197     endpoint_name: str,
        198     instance: Dict[str, Any],
   
     199     parameters: Optional[Dict[str, Any]] = None,
        200 ) -> Iterator[Dict[str, Any]]:
        201     '''
Predicts a stream of dicts from a single instance dict.
        202 
        203     Args:
       (...)
        210     
    A generator of model prediction dicts.
        211     '''
    --> 212     for dict_list in predict_stream_of_dict_l
ists_from_single_dict_list(
        213         prediction_service_client=prediction_service_client,
        214        
 endpoint_name=endpoint_name,
        215         dict_list=[instance],
        216         parameters=parameters,
     
   217     ):
        218         if len(dict_list) > 1:
        219             raise ValueError(
        220          
       f'Expected to receive a single output, but got {dict_list}'
        221             )
    
    File /usr/local/li
b/python3.9/dist-packages/google/cloud/aiplatform/_streaming_prediction.py:158, in predict_stream_of_dict_lists_from_sin
gle_dict_list(prediction_service_client, endpoint_name, dict_list, parameters)
        156 tensor_list = [value_to_tenso
r(d) for d in dict_list]
        157 parameters_tensor = value_to_tensor(parameters) if parameters else None
    --> 158
 for tensor_list in predict_stream_of_tensor_lists_from_single_tensor_list(
        159     prediction_service_client=pr
ediction_service_client,
        160     endpoint_name=endpoint_name,
        161     tensor_list=tensor_list,
        1
62     parameters_tensor=parameters_tensor,
        163 ):
        164     yield [tensor_to_value(tensor._pb) for tensor
 in tensor_list]
    
    File /usr/local/lib/python3.9/dist-packages/google/cloud/aiplatform/_streaming_prediction.py:1
07, in predict_stream_of_tensor_lists_from_single_tensor_list(prediction_service_client, endpoint_name, tensor_list, par
ameters_tensor)
         91 '''Predicts a stream of lists of `Tensor` objects from a single list of `Tensor` objects.
  
       92 
         93 Args:
       (...)
        100     A generator of model prediction `Tensor` lists.
        101 ''
'
        102 request = prediction_service_types.StreamingPredictRequest(
        103     endpoint=endpoint_name,
      
  104     inputs=tensor_list,
        105     parameters=parameters_tensor,
        106 )
    --> 107 for response in pr
ediction_service_client.server_streaming_predict(request=request):
        108     yield response.outputs
    
    File 
/usr/local/lib/python3.9/dist-packages/google/cloud/aiplatform_v1/services/prediction_service/client.py:1732, in Predict
ionServiceClient.server_streaming_predict(self, request, retry, timeout, metadata)
       1729 self._validate_universe_d
omain()
       1731 # Send the request.
    -> 1732 response = rpc(
       1733     request,
       1734     retry=retry
,
       1735     timeout=timeout,
       1736     metadata=metadata,
       1737 )
       1739 # Done; return the respo
nse.
       1740 return response
    
    File /usr/local/lib/python3.9/dist-packages/google/api_core/gapic_v1/method.py
:131, in _GapicCallable.__call__(self, timeout, retry, compression, *args, **kwargs)
        128 if self._compression is
 not None:
        129     kwargs['compression'] = compression
    --> 131 return wrapped_func(*args, **kwargs)
    
   
 File /usr/local/lib/python3.9/dist-packages/google/api_core/grpc_helpers.py:174, in _wrap_stream_errors.<locals>.error_
remapped_callable(*args, **kwargs)
        170     return _StreamingResponseIterator(
        171         result, prefet
ch_first_result=prefetch_first
        172     )
        173 except grpc.RpcError as exc:
    --> 174     raise exceptio
ns.from_grpc_error(exc) from exc
    
    InvalidArgument: 400 Request contains an invalid argument.
    

&#x200B;
```
---

     
 
all -  [ Examples of Langchain Python scripts of a central agent coordinating multi agents ](https://www.reddit.com/r/MLQuestions/comments/1bn8mb1/examples_of_langchain_python_scripts_of_a_central/) , 2024-03-28-0910
```
Hey guys, using Langchain, does anyone have any example Python scripts of a central agent coordinating multi agents (ie.
 this is a multi agent framework rather than a multi tool framework).

I have googled around for this but can't seem to 
find any.

Would really appreciate any help on this.
```
---

     
 
all -  [ Examples of Langchain Python scripts of a central agent coordinating multi agents ](https://www.reddit.com/r/LanguageTechnology/comments/1bn8lmk/examples_of_langchain_python_scripts_of_a_central/) , 2024-03-28-0910
```
Hey guys, using Langchain, does anyone have any example Python scripts of a central agent coordinating multi agents (ie.
 this is a multi agent framework rather than a multi tool framework).  
  
I have googled around for this but can't se
em to find any.  
  
Would really appreciate any help on this.
```
---

     
 
MachineLearning -  [ [D] : Scale PDF Q&A App to 10K Users with GPUs – <$250/Mo ](https://www.reddit.com/r/MachineLearning/comments/1b6jv56/d_scale_pdf_qa_app_to_10k_users_with_gpus_250mo/) , 2024-03-28-0910
```
Hello everyone,

Check out this step-by-step detailed tutorial on building and scaling a PDF Q&A Application using Pinec
one, Langchain and Inferless

&#x200B;

[Architecture](https://preview.redd.it/zfta52cbddmc1.png?width=1301&format=png&a
uto=webp&s=440399212d3feb03e861759a31602e2cde0dc7fb)

Alongside, the detailed quick deploy guide, it also includes cost 
analysis on how you can save upto 84% cost with an example of processing 3000 documents and nearly 10,000 queries every 
month, all while dramatically cutting your costs from $1800 ( AWS) to just $250 a month on Inferless.

Here is the tutor
ial - [https://cookbook.inferless.com/](https://cookbook.inferless.com/)

If you resonate, join the discussion on Hacker
news here - [https://news.ycombinator.com/item?id=39594588](https://news.ycombinator.com/item?id=39594588)
```
---

     
 
MachineLearning -  [ [D] What Is Your LLM Tech Stack in Production? ](https://www.reddit.com/r/MachineLearning/comments/1b4sdru/d_what_is_your_llm_tech_stack_in_production/) , 2024-03-28-0910
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

     
 
deeplearning -  [ Tengyu Ma on Voyage AI - Weaviate Podcast #91! ](https://www.reddit.com/r/deeplearning/comments/1bjft8i/tengyu_ma_on_voyage_ai_weaviate_podcast_91/) , 2024-03-28-0910
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

     
