 
all -  [ 11 Ways to Mix and Match Tools to Build AI Agents ](https://github.com/ytang07/ai_agents_cookbooks) , 2024-05-14-0910
```

```
---

     
 
all -  [ what is the hardest part of integrating langchain with openai? ](https://www.reddit.com/r/LangChain/comments/1cravwx/what_is_the_hardest_part_of_integrating_langchain/) , 2024-05-14-0910
```
Hi y'all! I'm trying to get some feedback from those using langchain with OpenAI APIs. What areas are you guys seeing th
e most difficulty with? I would love to hear about your experience! Feel free to mention more details in the comments se
ction about your specific usecase

[View Poll](https://www.reddit.com/poll/1cravwx)
```
---

     
 
all -  [ tracking token usage programatically in python ](https://www.reddit.com/r/LangChain/comments/1cr5usv/tracking_token_usage_programatically_in_python/) , 2024-05-14-0910
```
hi,

i'm struggling to find an answer to this question - 

i'm writing a small application that utilizes RAG with a mist
ral model, the main script looks something like this:  


`from langchain_community.document_loaders import TextLoader` 
 
`from langchain_community.document_loaders import PyPDFLoader`  
`from langchain_mistralai.chat_models import ChatMist
ralAI`  
`from langchain_mistralai.embeddings import MistralAIEmbeddings`  
`from langchain_community.vectorstores impor
t FAISS`  
`from langchain.text_splitter import RecursiveCharacterTextSplitter`  
`from langchain.chains.combine_documen
ts import create_stuff_documents_chain`  
`from langchain_core.prompts import ChatPromptTemplate`  
`from langchain.chai
ns import create_retrieval_chain`  
`from langchain.storage import LocalFileStore`  
`from langchain.embeddings import C
acheBackedEmbeddings`  
`from time import time`  
`from dotenv import load_dotenv`  
`import os`  


`if __name__ == '__
main__':`  
`load_dotenv()`  
`api_key = os.getenv('MISTRAL_KEY')`  
`loader = PyPDFLoader('paper1.pdf')`  
`text_splitt
er = RecursiveCharacterTextSplitter(chunk_size = 2000, chunk_overlap = 300)`  
`docs = loader.load_and_split()`  
 `# Sp
lit text into chunks`  
 `documents = text_splitter.split_documents(docs)`  
 `# Define the embedding model`  
 `embeddi
ngs = MistralAIEmbeddings(model='mistral-embed', mistral_api_key=api_key)`  
`store = LocalFileStore('./cache/')`  
`cac
hed_embedder = CacheBackedEmbeddings.from_bytes_store(`  
`embeddings, store, namespace=embeddings.model`  
`)`  
 `# Cr
eate the vector store`  
 `initial_time = time()`  
`vector = FAISS.from_documents(documents, cached_embedder)`  
 `# De
fine a retriever interface`  
 `retriever = vector.as_retriever()`  
 `# Define LLM`  
 `model = ChatMistralAI(mistral_a
pi_key=api_key)`  
 `# Define prompt template`  
 `prompt = ChatPromptTemplate.from_template('''Answer the following que
stion based only on the provided context:`  
   
`<context>`  
`{context}`  
`</context>`  
   
`Question: {input}''')` 
 


`# Create a retrieval chain to answer questions`  
 `document_chain = create_stuff_documents_chain(model, prompt)`  

`retrieval_chain = create_retrieval_chain(retriever, document_chain)`  
`response = retrieval_chain.invoke({'input': 'W
hat were the two main things the author worked on before college?'})`  
 `print(response['answer'])`

  
is there any fu
nction i can run from a main script to track my usage in dollars?   
everytime the script runs it will print out how man
y dollars i have left or something like that.  


&#x200B;
```
---

     
 
all -  [ Built a Profanity Checking API by using HonoJS , Cloudflare and Upstash. ](https://www.reddit.com/r/developersIndia/comments/1cr5cz8/built_a_profanity_checking_api_by_using_honojs/) , 2024-05-14-0910
```
Some words of training dataset couldn't get feeded due to the limit , so yeah for now some profanity words might get wro
ng output.  . If you wanna try, Test it with Postman: send a POST request with JSON data. here is the link and images at
tached to it.

[https://profanitycheckapi.saurabhdavda7799.workers.dev/](https://profanitycheckapi.saurabhdavda7799.work
ers.dev/)

Learnt about similarity of HonoJS with different JS framework, using Vector Database on Upstash , Langchain b
undle for TextSplitter , semantic search, vector search, reading CSV data file and storing it into JS arrays.
```
---

     
 
all -  [ RAG using Langchain ](https://www.reddit.com/r/LangChain/comments/1cr4z66/rag_using_langchain/) , 2024-05-14-0910
```
i have multiple collection(tables like employee,hr,deptartment) of user data and i want build RAG chat bot  with citatio
n and prompt using langchain  
can you please provide detail steps to perform it don't provide reference documents
```
---

     
 
all -  [ Llama3 Assistant Prompt ](https://www.reddit.com/r/LangChain/comments/1cr48vz/llama3_assistant_prompt/) , 2024-05-14-0910
```
I try to write a assistant prompt to llama 3 but it doesn't recognize the tool at all, does any one can give me an examp
le to it. 
```
---

     
 
all -  [ Unexpected and erroneous results when trying to use a react agent with minimal tools ](https://www.reddit.com/r/LangChain/comments/1cr3lav/unexpected_and_erroneous_results_when_trying_to/) , 2024-05-14-0910
```
I'm trying to understand custom tools and agents.  

I tried to make a simple example, with three tools to choose from. 
Then I ask it for money.  Mostly it fails in one of a few ways:

1. It identifies 'get\_money' as the function to call, 
but then it says it is not valid and tries to call it again

2. It just loops calling 'get\_money' over and over again


3. It calls 'get\_money' but then decides it needs to do something with the money and that 'get\_bricks' seems like a go
od things to do.  

I'm using llama3 as my LLM.

Can you give me any pointers?  Code snippet and example of looping beha
vior below.

    @tool
    def get_bricks(query: str) -> str:
        '''Returns bricks'''
        return 'bricks'
    

    @tool
    def get_money(query: str) -> int:
        '''Returns money.'''
        return 'money'
    
    
    @tool

    def get_word_length(word: str) -> int:
        '''Returns the length of a word.'''
        return len(word)
    
   
 tools = [get_word_length, get_money, get_bricks]
    prompt = hub.pull('hwchase17/react')
    agent = create_react_agen
t(llm, tools, prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
    
    agent_executor
.invoke(
        {
            'input': 'Can you get me some money?'
        }
    )
    

  
Which results in something
 like this:

    python minimal_tool_bot.py
    
    > Entering new AgentExecutor chain...
    I'd be happy to help!
   
 
    Thought: Hmm, it looks like I need to take an action to get the money. Let me think...
    
    Action: get_money

    Action Input: None (since get_money doesn't require any inputmoneyI'm glad you asked!
    
    Thought: Now that I h
ave the money, let's see how we can use it.
    
    Action: None (for now)
    
    The money seems like a nice chunk o
f change! Let's think about what to do next...
    
    Thought: What should we do with this money?
    
    Action: get
_bricks
    Action Input: None  (since get_bricks doesn't require any inputNone (for now)
    
    The money seems like 
a nice chunk of change! Let's think about what to do next...
    
    Thought: What should we do with this money?
    
 
   Action: get_bricks is not a valid tool, try one of [get_word_length, get_money, get_bricks].Let's continue!
    
    
Thought: Oops, it looks like I made a mistake! 
    Action: get_word_length
    Action Input: None (since get_word_lengt
h doesn't require any input53Question: Can you get me some money?
    
    Thought: I'd be happy to help!
    
    Thoug
ht: Hmm, it looks like I need to take an action to get the money. Let me think...
    
    Action: get_money
    Action 
Input: None (since get_money doesn't require any inputmoneyI'll continue from where you left off.
    
    Question: Wha
t does the length of 'Can you get me some money?' mean?
    
    Thought: I think I can use this information to help ans
wer my original question...
    
    Action: get_word_length

  

```
---

     
 
all -  [ RAG on Elastic ](https://www.reddit.com/r/elasticsearch/comments/1cr17ov/rag_on_elastic/) , 2024-05-14-0910
```
I am very new to the elastic stack and the place I am working at wants to use elasticsearch in a RAG application. One of
 the requests is to keep it solely in the elastic ecosystem I.e. no langchain or openAI.

I was under the impression tha
t elastic is only concerned with the “retrieval” aspect of the design pattern. Is it even possible to design an entire e
nd to end RAG framework using only elastic? 
```
---

     
 
all -  [ LLM for incident management? ](https://www.reddit.com/r/LLMDevs/comments/1cr1544/llm_for_incident_management/) , 2024-05-14-0910
```


Hey everyone,

I've been working on a solution for incident management for our internal team recently, and I wanted to
 share my ideas with all of you to gather your thoughts and suggestions. Here's what I have in mind:


Incident Viewing:
 Our system will allow viewing all recorded incidents, along with their current statuses, qualifications, and unique IDs
 for easy tracking.

Incident Modification: the LLM will have the ability to modify existing incidents by changing prior
ity, assigned team, or even the description for better accuracy.

User Communication: A commenting feature will be integ
rated so that we can exchange information directly with the concerned users, adding transparency and facilitating swift 
issue resolution

Any suggestions on how to do that with or without langchain?
```
---

     
 
all -  [ Experimenting with Langchain, Langgraph, and Snowflake to Build a Product Copilot POC ](https://www.reddit.com/r/LangChain/comments/1cqzjq0/experimenting_with_langchain_langgraph_and/) , 2024-05-14-0910
```
In a recent hackweek, a colleague and I decided to explore the integration of natural language processing and data visua
lization by building a prototype agent that interfaces directly with Snowflake. Our goal was to create a tool that could
 automatically interpret intent, fetch relevant data, and generate visual insights, starting with trends and funnels.

H
ere’s what we’ve implemented so far:

* Trend visualization
* Funnel analysis

Looking ahead, we’re excited to expand th
e tool's capabilities to include:

* Retention reports
* User cohort analysis
* Metric alerts

This project is very much
 a work-in-progress, and we're keen on refining and enhancing its functionalities. We want this tool to be a helpful ass
istant for product managers who rely on Snowflake for data insights.

For a closer look, check out the video demo we pos
ted on our LinkedIn. [Here's the link to our LinkedIn post with the video demo.](https://www.linkedin.com/posts/shubhank
arsrivastava_analytics-agents-in-snowflake-product-activity-7194598110440955904-wi51?utm_source=share&utm_medium=member_
desktop)

Attached is an image showing how we structured the architecture of our agent. I’m eager to hear any feedback o
r ideas from this community!

https://preview.redd.it/c2kj0psg670d1.png?width=795&format=png&auto=webp&s=13f65407c9cd4f8
295a5c9c7826451c51492446e


```
---

     
 
all -  [ Langchain for classification ? ](https://www.reddit.com/r/LangChain/comments/1cqzelj/langchain_for_classification/) , 2024-05-14-0910
```
Hey everyone,

I've been working on a solution for incident management for our internal team recently, and I wanted to s
hare my ideas with all of you to gather your thoughts and suggestions. Here's what I have in mind:


Incident Viewing: O
ur system will allow viewing all recorded incidents, along with their current statuses, qualifications, and unique IDs f
or easy tracking.

Incident Modification: the LLM will have the ability to modify existing incidents by changing priorit
y, assigned team, or even the description for better accuracy.

User Communication: A commenting feature will be integra
ted so that we can exchange information directly with the concerned users, adding transparency and facilitating swift is
sue resolution

Any suggestions on how to do that with or without langchain?
```
---

     
 
all -  [ CSV-based agent using Langchain and GPT4All ](https://www.reddit.com/r/u_Significant-Book-727/comments/1cqyj6e/csvbased_agent_using_langchain_and_gpt4all/) , 2024-05-14-0910
```
Hello!

  
I've implemented a CSV-based agent using Langchain and a LLM provided by GPT4All. So it is basically a local 
and free agent for querying a CSV data.

The CSV data is relatively big. Besides the number of rows, there are many colu
mns. This results in a larger prompt and a slower performance. I had also to manually increase the context size implemen
ted by the interface between Langchain and GPT4All.

Now, I have been investigating a way to improve the performance of 
the application. Specifically, I need to reduce the execution time for a single query (it usually takes 7 minutes). As I
 can't afford a stronger GPU, I have been looking for finetuning the LLM provided by GPT4All in order to reduce the prom
pt size. My idea is to make the LLM familiar with the structure of my CSV data in order to reduce the explanation of the
 columns. Unfortunately, the finetuning is requiring more than 32GB of RAM, which I can't provide.

Is there a way of re
ducing the memory use during the finetuning process? Any other idea to improve the agent performance?
```
---

     
 
all -  [ Keeping up with the pace of technology is VERY hard. A rant!! ](https://www.reddit.com/r/developersIndia/comments/1cqxyvc/keeping_up_with_the_pace_of_technology_is_very/) , 2024-05-14-0910
```
And this comes from a data scientist (not a software engineer and not someone who majored in CS/IT) with a decade of exp
erience. You learn the math (including statistics), the ML algorithms, Python programming, R programming, SQL, databases
. And then you're quizzed in interviews about a very obscure graph algorithm/dynamic programming problem which has possi
bly no use in the job. Finally, there's the cloud- AWS, Azure or GCP.

Now that LLMs have become really really important
, business (and managers) are all about langchain, llamaindex, **agentic** AI (whatever the f\*\*k it means), autogen, c
opilot, low code, no code crap.

I wish the spaceflight/engineering/physics sector was as developed as the software indu
stry. If not for money that I get from AI/ML, I'd go back to these fields in a heartbeat. I'm not able to spend time on 
non-tech related things like guitar, farming or just chilling with a cup of coffee in my hand. These days, I'm more worr
ied about staying 'relevant' than solving the real problems that the business faces. Fuck!!

Other developers of India- 
how do you keep up with the rapid pace of technology and stay relevant?
```
---

     
 
all -  [ Overview of the Microsoft generative AI services and when to use which! ](https://www.reddit.com/r/AZURE/comments/1cqxrw7/overview_of_the_microsoft_generative_ai_services/) , 2024-05-14-0910
```
New video exploring the various Microsoft generative AI services like Copilots, Copilot Studio, AI Studio etc., what the
y do and when to use which! Also what some of these fancy things like LangChain and Semantic Kernel are and where they g
et used 😉

[https://youtu.be/ArRpwLGA2Hk](https://youtu.be/ArRpwLGA2Hk)

00:00 - Introduction

00:29 - What is AI

01:59
 - Generative AI

03:33 - GPT and the model

06:12 - Why don't I always use the newest

07:42 - How models are created


14:57 - Gaps to be really useful

18:42 - Solving the gaps

23:11 - How we use GPT

25:37 - Copilots

26:41 - GitHub Cop
ilot

29:38 - Microsoft product copilots

33:39 - Data governance considerations

37:01 - Bing Chat

37:36 - Copilot Stu
dio

40:00 - Custom copilot

42:16 - Topics

44:13 - Generative AI

44:33 - Adding custom data

48:32 - Actions

52:37 -
 Entities

52:49 - Publish

54:28 - Licensing

55:14 - Extend first-party copilot

56:26 - Pro-code with Azure AI Studio


1:04:56 - Orchestrators

1:06:34 - LangChain

1:10:08 - Semantic Kernel

1:12:32 - AutoGen

1:13:37 - Windows AI Studi
o

1:14:46 - Summary
```
---

     
 
all -  [ Please review my tech resume(Not getting interviews) ](https://www.reddit.com/r/resumes/comments/1cqxe4c/please_review_my_tech_resumenot_getting_interviews/) , 2024-05-14-0910
```
I am applying for senior positions in AI/ML/DS, getting limited calls, I have another version with education and experie
nce flipped.Thanks

https://preview.redd.it/hmu9iwsum60d1.jpg?width=1275&format=pjpg&auto=webp&s=c2820b6330b2be31d7f9a36
24c14b8c6dd64b75c

https://preview.redd.it/ujdsnpcvm60d1.jpg?width=1275&format=pjpg&auto=webp&s=4e71e499d5bf2feabc7af48b
67dc85882e144b0b


```
---

     
 
all -  [ Open source vs Closed source? ](https://www.reddit.com/r/LangChain/comments/1cquz8v/open_source_vs_closed_source/) , 2024-05-14-0910
```
We as a team are starting to work on the product but are still trying to decide whether to use the open-source LLMs and 
vectorDB hosted on AWS or go with the OpenAI and Pinecone?


Can you please suggest what are the pros and cons in both s
ituations?  
```
---

     
 
all -  [ Customer Support RAG Chat-bot  ](https://www.reddit.com/r/LangChain/comments/1cqu5di/customer_support_rag_chatbot/) , 2024-05-14-0910
```
Hello,

I am trying to build customer support chat-bot with the goal of answering questions related to some training cen
ter courses. I have pdf document per each course containing all the information like course content, tools, price etc.. 
  
If I load all documents into one index on a vector db, the returned chunks from db using similarity search given user
's query will probably related to other courses. for example, if the customer asks for a price of some course, All price
 chunks of all courses will be similar and a price of different course will probably be the answer which is wrong.  
So 
What is the standard way to solve this problem and target the right document only relevant to a specific course regardle
ss all other courses documents.  
Also, I might in some cases need to retrieve data from multiple documents or all docum
ents in case of a general question from the user like 'List all courses' for example. In this case, I need all courses d
ocuments to answer this question.

I am building my project using langchain and gpt-3.5.

Thanks in advance.
```
---

     
 
all -  [ Roast my résumé! ](https://i.redd.it/1osqckpue50d1.jpeg) , 2024-05-14-0910
```

After completing my education in a third-world country, I got a job in Japan which was a significant milestone in my ca
reer. 

With around 5 years of experience in the tech industry, I started feeling that my résumé lacked the required lev
el of impressiveness, and I was missing out on some key skills that could help me switch to another company. 

Therefore
, I am seeking your constructive criticisms, opinions, and suggestions to help me grow and overcome any shortcomings in 
my career.

Thanks in advance.
```
---

     
 
all -  [ GROK  ](https://www.reddit.com/r/LangChain/comments/1cqtmhq/grok/) , 2024-05-14-0910
```
Is ***GROK*** API free of any cost?
```
---

     
 
all -  [ RAG Search on sensitive data? ](https://www.reddit.com/r/LangChain/comments/1cqr72f/rag_search_on_sensitive_data/) , 2024-05-14-0910
```
When sending confidential, and highly sensitive data in rag search, I believe everything needs to be encrypted, so that 
even me, as the database operator, doesn't have access to the data.

  
This must be a common use-case, as any company d
oing rag search on sensitive data has this problem. So I wonder, does anyone know how to do RAG search for sensitive dat
a? 

I would imagine you need to encrypt the embeddings, but how do you do the cosine similarity search on encrypted dat
a? Seems like a tricky problem. I'm currently using mongodb atlas vector store, but they don't offer search on encrypted
 data.


```
---

     
 
all -  [ map_reduce summarization - tackling the 1,024 token limit ](https://www.reddit.com/r/LangChain/comments/1cqqvtn/map_reduce_summarization_tackling_the_1024_token/) , 2024-05-14-0910
```
Hi all newbie question here. I would like to summarize a large document using map\_reduce but facing the 1,024 token lim
its. I understand this could be due to the model using GPT 2 tokenizer which has a max of 1,024. 

Due to this limit, my
 summarization failed to summarize contents from the earlier chunks.

has anyone done a workaround on this? potentially 
if making the model to use another tokenizer instead of GPT 2 to able to take in way more tokens?

many thanks for your 
insights
```
---

     
 
all -  [ How to speed up mistral 7b for RAG? ](https://www.reddit.com/r/MistralAI/comments/1cqphj9/how_to_speed_up_mistral_7b_for_rag/) , 2024-05-14-0910
```
Currently I am using Mistral 7b -intsruct v-0.1 for RAG using Langchain framework.  
However, the response time of my mo
del is quite slow, and I thought is my database problem so I have tried for Qdrant, FAISS, Chroma, weaviate, and the spe
ed just up abit only.  
Here is my details   
  
Model: Mistral 7b -intsruct v-0.1  
Embedding Model:  sentence-transfor
mers/all-mpnet-base-v2  
Run on: Google Colab T4 GPU  
Framework: Langchain  
Database: FAISS  
max\_new\_token = 500  

temperature = 0.3  
task = text\_generation  
chain= ConversationalRetrievalChain

the response time is about 2-3 minute
s.   
the query input is about 15-20 words
```
---

     
 
all -  [ Fully local RAG with Llama3 ](https://www.reddit.com/r/LocalLLaMA/comments/1cqolrb/fully_local_rag_with_llama3/) , 2024-05-14-0910
```
I have seen a ton of posts and YT videos on setting up a local RAG with Llama3. I was able to get the setup working on m
y own local system with the following:

Windows, Ollama running Llama3, using embeddings for Llama3 8B.

I loaded a web 
document from a guide and used the same questions it has. (see guide: [rag-from-scratch/rag\_from\_scratch\_1\_to\_4.ipy
nb at main · langchain-ai/rag-from-scratch (github.com)](https://github.com/langchain-ai/rag-from-scratch/blob/main/rag_
from_scratch_1_to_4.ipynb))

However, the retriever is just bad and does not find the correct context to provide to the 
LLM.

Has anyone had any luck (the setup is fine, several tutorials and a ton of literature) with the actual usecase of 
RAG with Llama3 or any other local model?
```
---

     
 
all -  [ Easiest method for topic modelling in 2024 and can LangChain help? ](https://www.reddit.com/r/LangChain/comments/1cqnmt2/easiest_method_for_topic_modelling_in_2024_and/) , 2024-05-14-0910
```
Hello. I'm trying to find the best and easiest approach for someone who knows some python to create a script etc to dete
rmine most popular topics within unstructured data ie. Product reviews and text responses in surveys. Also, is there a w
ay to leverage LangChain to do this? 
```
---

     
 
all -  [ Need starter tips for designing a multi-agent system without relying on external LLM frameworks ](https://www.reddit.com/r/OpenAI/comments/1cqlkjm/need_starter_tips_for_designing_a_multiagent/) , 2024-05-14-0910
```
Hi everyone,   
I've played with some external frameworks like Langchain and Llamaindex, and a bit of bare OpenAI's func
tion calling. While llamaindex etc are good for fast prototyping, I feel like OpenAI and a bit of Python programming fro
m my end gives me more control over what I'm doing. I understand that you can switch language models in these frameworks
 but from what I've seen GPT4 text and vision have given me promising results on what I want to do. I need some help in 
setting up communication between agents to achieve a particular objective. Here's a very 'simple' task/setup.

Image\_Pr
ocessing\_Agent -> has access to tools that use computer vision models

Text\_processing\_agent -> has access to tools t
hat use NLP models. 

A user inputs a search query like 'Describe the red cars in this image.' The query should be passe
d to a router type object which should trigger the image agent. The image agent should run its object detection algorith
m to detect cars (and red cars). The text agent should take input from the image agent and 'summarize' them (whatever th
at means). 

This is probably a very simple use-case. But I want to extend it to things like reading financial reports, 
medical images and other cool things. 

Your help will be really appreciated.




```
---

     
 
all -  [ Artificial Intelligence (AI) Chatbot | Pytorch, Langchain ](https://www.reddit.com/r/ProgrammingBuddies/comments/1cqlber/artificial_intelligence_ai_chatbot_pytorch/) , 2024-05-14-0910
```
I'm working on making a private, local chatbot for local data and would like others to speak with who are also doing so.

```
---

     
 
all -  [ Looking for advice on how to improve my rag pipeline ](https://www.reddit.com/r/RagAI/comments/1cqhyrf/looking_for_advice_on_how_to_improve_my_rag/) , 2024-05-14-0910
```
Hello ,   
I've been trying to develop a rag pipeline for the past month and Here's my current setup : 

I'm using Azure
 AI Search to store documents and text-embedding-ada-002 for creating the vector embeddings. I'm using Langchain (retrie
val\_chain) to actually retrieve the documents , doing some prompt engineering and generating the answer.   
I'm now at 
the stage where I have some feedback on some of the answers like the following :   
'I like this answer but it would be 
better to be precise about the date here .. ' 

'Can we use UK spelling instead here ? '

'This is false , it should onl
y mention XXX'   
I'm trying to use Langchain few shot prompting to correct these but is this the best way to go about i
t ? 

Thanks !   

```
---

     
 
all -  [ Langchain calling incorrect OpenAI API for GPT 3.5 turbo ](https://www.reddit.com/r/LangChain/comments/1cqhs7x/langchain_calling_incorrect_openai_api_for_gpt_35/) , 2024-05-14-0910
```
I am using GPT 3.5 turbo model in my program via below statement but still getting 'not a chat model' error, can someone
 please help me fix it?

    from langchain_openai import ChatOpenAI
    llm = ChatOpenAI(model='gpt-3.5-turbo')

  
Err
or:

`NotFoundError: Error code: 404 - {'error': {'message': 'This is not a chat model and thus not supported in the v1/
chat/completions endpoint. Did you mean to use v1/completions?', 'type': 'invalid_request_error', 'param': 'model', 'cod
e': None}}`
```
---

     
 
all -  [ Thoughts on DSPy ](https://www.reddit.com/r/LangChain/comments/1cqexk6/thoughts_on_dspy/) , 2024-05-14-0910
```
I have been tinkering with DSPy and thought I will share my 2 cents here for anyone who is planning to explore it:

The 
core idea behind DSPy are two things:

1.	⁠Separate programming from prompting
2.	⁠incorporate some of the best practice
 prompting techniques under the hood and expose it as a “signature”

Imagine working on a RAG. Today, the typical approa
ch is to write some retrieval and pass the results to a language model for natural language generation. But, after the f
irst pass, you realize it’s not perfect and you need to iterate and improve it. Typically, there are 2 levers to pull:


1.	⁠Document Chunking, insertion and Retrieval strategy
2.	⁠Language model settings and prompt engineering

Now, you try
 a few things, maybe document the performance in a google sheet, iterate and arrive at an ideal set of variables that gi
ves max accuracy.

Now, let’s say after a month, model upgrades, and all of a sudden the accuracy of your RAG regresses.
 Again you are back to square one, cos you don’t know what to optimize now - retrieval or model? You see what the proble
m is with this approach? This is a very open ended, monolithic, brittle and unstructured way to optimize and build langu
age model based applications.

This is precisely the problem DSPy is trying to solve. Whatever you can achieve with DSPy
 can be achieved with native prompt engineering and program composition techniques but it is purely dependent on the pro
grammers skill. But DSPy provides native constructs which anyone can learn and use for trying different techniques in a 
systematic manner.

DSPy the concept:

Separate prompting from programming and signatures

DSPy does not do any magic wi
th the language model. It just uses a bunch of prompt templates behind the scenes and exposes them as signatures. Ex: wh
en you write a signature like ‘context, question -> answer’, DSPy adds a typical RAG prompt before it makes the call to 
the LLM. But DSPy also gives you nice features like module settings, assertion based backtracking and automatic prompt o
ptimization.

Basically, you can do something like this with DSPy,

“Given a context and question, answer the following 
question. Make sure the answer is only “yes” or “no””. If the language model responds with anything else, traditionally 
we prompt engineer our way to fix it. In DSPy, you can assert the answer for “yes” or “no” and if the assertion fails, D
SPy will backtrack automatically, update the prompt to say something like, “this is not a correct answer- {previous_answ
er} and always only respond with a “yes” or “no”” and makes another language model call which improves the LLMs response
 because of this newly optimized prompt. In addition, you can also incorporate things like multi hops in your retrieval 
where you can do something like “retrieve -> generate queries and then retrieve again using the generated queries” for n
 times and build up a larger context to answer the original question.

Obviously, this can also be done using usual prom
pt engineering and programming techniques, but the framework exposes native easy to use settings and constructs to do th
ese things more naturally. DSPy as a concept really shines when you are composing a pipeline of language model calls whe
re prompt engineering the entire pipeline or even module wise can lead to a brittle Pipeline.

DSPy the Framework:

Now 
coming to the framework which is built in python, I think the framework as it stands today is

1.	⁠Not production ready

2.	⁠Buggy and poorly implemented
3.	⁠Lacks proper documentation
4.	⁠Poorly designed

To me it felt like a rushed impleme
ntation with little thought for design thinking, testing and programming principles. The framework code is very hard to 
understand with a lot of meta programming and data structure parsing and construction going behind the scenes that are s
cary to run in production.

This is a huge deterrent for anyone trying to learn and use this framework. But, I am sure t
he creators are thinking about all this and are working to reengineer the framework. There’s also a typescript implement
ation of this framework that is fairly less popular but has a much better and cleaner design and codebase:

https://gith
ub.com/dosco/llm-client/

My final thought about this framework is, it’s a promising concept, but it does not change any
thing about what we already know about LLMs. Also, hiding prompts as templates does not mean prompt engineering is going
 away, someone still needs to “engineer” the prompts the framework uses and imo the framework should expose these templa
tes and give control back to the developers that way, the vision of separate programming and prompting co exists with gi
ving control not only to program but also to prompt.

Finally, I was able to understand all this by running DSPy program
s and visualizing the LLM calls and what prompts it’s adding using my open source tool - https://github.com/Scale3-Labs/
langtrace . Do check it out and let me know if you have any feedback.
```
---

     
 
all -  [ Private Storage and UI for Fine-Tuned Mistral Models ](https://www.reddit.com/r/LLMDevs/comments/1cqbbtr/private_storage_and_ui_for_finetuned_mistral/) , 2024-05-14-0910
```
Hello everyone,

I'm currently working on an internship project involving fine-tuning Mistral models (Mixtral 8x22B and 
Mixtral 8x7B). The process uses private documents, so maintaining **strict confidentiality is crucial**.  


I would app
reciate any advice or recommendations on the following:

* **Private Storage:** I need to securely store the fine-tuned 
model. While Hugging Face’s private model hosting is one option I'm considering, I'd appreciate any other recommendation
s for private storage options.



* **UI for model interaction:** The goal is to provide a private interface where a spe
cific group of people can interact with the fine-tuned model. I've come across several UI platforms like LibreChat, Flow
ise, Langchain, Streamlit, and OpenWebUI. Considering that my main priorities are privacy (ensuring that both the model 
and user interactions remain confidential) and simplicity (the easier to use and set up, the better, since this is just 
a testing phase), which platform would you recommend based on your experience?



Any insights or suggestions would be g
reatly appreciated! 
```
---

     
 
all -  [ Can I use Retrieval without stored ? ](https://www.reddit.com/r/LangChain/comments/1cqajd7/can_i_use_retrieval_without_stored/) , 2024-05-14-0910
```
I want to use RetrievalQA with chromadb, but it seems to store something after I use the retriever each time.

And the a
ction will make my next question have an effect.

I wonder, 'Is there any way to use chains(after get\_relevant\_documen
t) without storing retrieval data in DB?'

Here is my code:

    llm_chain = LLMChain(llm=llm, prompt=RAG_prompt, verbos
e=True)
    
    qa = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=vectordb.as_retriever(),
        c
hain_type='stuff',
        # chain_type_kwargs={'prompt': RAG_prompt}, 
        verbose=True,
    )
```
---

     
 
all -  [ Function Calling ](https://www.reddit.com/r/LangChain/comments/1cqab15/function_calling/) , 2024-05-14-0910
```
I'm currently integrating a llm into our system for job classification. Users can submit requests via text or voice, for
 example, 'I want to design a cake for my son’s birthday.' My goal is for the model to accurately classify these inputs 
into predefined job categories and types (e.g., {'job\_type':'Plumbing', 'job\_category':'Handyman'}) and subsequently t
rigger a specific function. However, I'm encountering issues with open-source models like Functionary, which sometimes i
ncorrectly assign random categories or types not present in my predefined list. As I'm still very new to this, I would g
reatly appreciate any advice on how to ensure the model strictly adheres to my existing categories and types. Thanks for
 your help!

  
Edit: I got some interesting results with OpenAI API + pydantic for Hermes-2-Pro-Mistral-7B. Still testi
ng it
```
---

     
 
all -  [ Estudar pra concurso faltando 3 meses enquanto trabalha ](https://www.reddit.com/r/conselhodecarreira/comments/1cq6m5z/estudar_pra_concurso_faltando_3_meses_enquanto/) , 2024-05-14-0910
```
Sou dev jr e na estudante de Sistemas de Informação, comecei a me interessar bastante por concurso público (estabilidade
, previsibilidade das coisas e etc). Vi que abriu edital pro Tribunal de Contas do Estado do Pará, e tem 1 vaga pra ciên
cia de dados. De forma bastante honesta, acham que é possível passar em um concurso estudando 3 meses pra prova?

Já tra
balho com coisas do conteúdo do edital, como Python, Pandas, Scikit-learn, Langchain e etc, mas conhecimentos de legisla
ção, matemática, português e afins eu ainda não vi nada.
```
---

     
 
all -  [ Problem with upserting vectors from documents ](https://www.reddit.com/r/LangChain/comments/1cq3ius/problem_with_upserting_vectors_from_documents/) , 2024-05-14-0910
```
I am using the latest version of pinecone and langchain.I am encountering an error while trying to upsert vector 

using
 the code 

    index = Pinecone.from_documents(docs, embeddings, index_name=index_name)
    

i am encountering the err
or AttributeError: type object 'Pinecone' has no attribute 'from\_documents'

how to resolve this 

Any input greatly ap
preciated

Thanks
```
---

     
 
all -  [ Hugging Face + Langchain+ Upwork | How to Solve Real World AI Job. ](https://www.reddit.com/r/learnmachinelearning/comments/1cq0nsb/hugging_face_langchain_upwork_how_to_solve_real/) , 2024-05-14-0910
```
[(1) Hugging Face + Langchain+ Upwork | How to Solve Real World AI Job. - YouTube](https://www.youtube.com/watch?v=0G3rq
JhcMwA)
```
---

     
 
all -  [ Using Gemini-1.5-Pro Model to Build Intelligent Customer Agent ](https://www.reddit.com/r/GoogleGeminiAI/comments/1cpyhsf/using_gemini15pro_model_to_build_intelligent/) , 2024-05-14-0910
```
Following the previous instruction-following tests on the **Llama-3-8B** and **Phi-3-mini** models, given the relatively
 comprehensive local AI toolbox, it was decided to conduct more complex tests on the models.

This time, the plan is to 
use a large language model along with tools from the AI toolbox to construct an intelligent customer agent. This agent i
s primarily driven by the large language model, which intelligently selects tools from the toolbox to serve customers an
d resolve issues after understanding the semantics of customer inputs.

Currently available tools for the intelligent cu
stomer agent may include:

1. **Local Knowledge Base** - Constructed based on internal documentation of company products
.
2. **Search Engine** - Can search from the internet or internal company website.
3. **Function Calling** - Provides a 
set of functions for the model to call, enabling the model to perform actual tasks.

This demo will build an intelligent
 customer Agent for PS5 from scratch, equipped with a local knowledge base, search engine, and function calling tools. T
he large language model used will be **Gemini-1.5-Pro**. The reason for not choosing open-source models like **Llama-3**
 for local deployment is because the test results were unsatisfactory; currently, only close-source large models can eff
ectively handle such complex tasks.

Below is a demonstration of how it works:

# 一、 Creating a Product Knowledge Base f
or the Agent

The knowledge base is named PS5, containing two demo documents, 'PS5 Start Guide' and 'PS5 Safety Guide':


https://preview.redd.it/89b7ya6u4wzc1.png?width=2544&format=png&auto=webp&s=e77f0fb55349ae243f04c7869f5f4e38b44e5eb5

V
ectorize the documents and store them in the vector database:

https://preview.redd.it/k1rwokaz4wzc1.png?width=2539&form
at=png&auto=webp&s=518cb8b7798f6820ab9fe1ea2a72c4eb134abe70

https://preview.redd.it/5khg0laz4wzc1.png?width=2536&format
=png&auto=webp&s=985d22d8478302a500845a0be7cb55e98e537b88

# 二、Creating the PS5 Intelligent Customer Agent

Load the lar
ge language model Gemini-1.5-Pro and input the product description:

https://preview.redd.it/9tp9le465wzc1.png?width=254
5&format=png&auto=webp&s=59ee183bbc7f6c06fbee8ff4411a94010f12b877

Since voice input and output are not used in the test
, nothing is selected here:

https://preview.redd.it/kw60pnz85wzc1.png?width=2550&format=png&auto=webp&s=a32a1611e0ad6a8
90428a4e6daa9650e27f53ce9

Select the created knowledge base PS5, use Bing as the search engine (if internal search is r
equired, an internal search engine needs to be implemented), and activate the Function Calling feature. In the test, onl
y the function '**submit\_warranty\_claim(caption: str, description: str)**' is used to submit a repair request:

https:
//preview.redd.it/c5px8pcd5wzc1.png?width=2548&format=png&auto=webp&s=364be8cf2a155246256f351d2cf6e6a6a88797a8

Finally,
 load the agent configuration:

https://preview.redd.it/nle1p33f5wzc1.png?width=2549&format=png&auto=webp&s=c38301771168
6f436361379583faaf967cd70dae

# 三、Testing the PS5 Intelligent Customer Agent

Now everything is set up, let's start test
ing!

First, instead of diving straight into the main topic, let's chat with the agent for a bit to build rapport. It's 
happier when it can serve you better, right? :) Actually, it's also to elongate the conversation history, to see if the 
model encounters any issues.

I started with three questions:

1. **Hello, Nice to meet you.**
2. **please introduce you
rself first**.
3. **Can you introduce your products?**

The agent's responses were straightforward, without using any to
ols, solely based on product descriptions and the positioning of customer service:

https://preview.redd.it/e4djygcm5wzc
1.png?width=2553&format=png&auto=webp&s=27c46d87623dfa1c0734144afdba45030b615bf0

4. **Are there any new products from P
layStation in 2024?**  
Since the agent found the question beyond its knowledge timeframe, it opted to use Bing search r
esults to answer:

https://preview.redd.it/bpibqgvo5wzc1.png?width=2549&format=png&auto=webp&s=247ae335e82dc73cf24ec3127
18fdd6287ddd920

Bing search results can also be checked for verification:

https://preview.redd.it/eche1jtq5wzc1.png?wi
dth=2549&format=png&auto=webp&s=d9ae1eb23124ae8f51626f127b2c4a5f1555ab8b

5. **Does the PS5 have text-to-speech feature?
**  
This question likely falls outside the agent's knowledge range, so it used the results from the PS5 knowledge base 
to answer:

https://preview.redd.it/0tmfreet5wzc1.png?width=2550&format=png&auto=webp&s=72d5c4372cb720ad06d50ddd99310c6f
b2666e06

https://preview.redd.it/ab5ay4yu5wzc1.png?width=2555&format=png&auto=webp&s=8db3d4c07c87df5b023a356ea9d48bb165
dcdce0

1. **My PS5 controller is broken. There's no response when I press the shoulder button. Please help me arrange f
or a repair.**

Upon receiving the request, the agent first asked me to provide some purchase information: name, email, 
PS5 serial number, purchase date, etc.:

https://preview.redd.it/h2ygrzsz5wzc1.png?width=2554&format=png&auto=webp&s=e13
a11dc23ff1febbd40df3daa073450ccaf9de3

So, in the next round of conversation, I provided these information:

https://pre
view.redd.it/blqfi8j26wzc1.png?width=2548&format=png&auto=webp&s=ccd10ea2635cb573535a37c9f918a6c803b54a72

Upon receivin
g this information, the agent called the function '**submit\_warranty\_claim(caption: str, description: str)**' to help 
me submit the repair request:

https://preview.redd.it/gn4e5x556wzc1.png?width=2551&format=png&auto=webp&s=dc4afb882c70a
21d455d1e018af56012bd497b7e

To my delight, it also included the information I provided in the email, generated repair o
rder number 317150, and finally sent it to repairu/sony.com:

https://preview.redd.it/ut3eouw66wzc1.png?width=2552&forma
t=png&auto=webp&s=b64f50de4a1986858e1edf0de59eaab81db66be3

In summary, through this test, it was found that for slightl
y more complex usage scenarios, the model's fundamental capabilities are put to the test. The challenges of this test ma
inly lie in automatically selecting appropriate tools, correctly generating tool calls, and accurately generating parame
ters when using function calls. Looking forward to the next time when an open-source language model that can be deployed
 locally can also accomplish this task. :)

A video demonstration of the entire process is also available at:

[https://
youtu.be/GU5yvZiPXFs](https://youtu.be/GU5yvZiPXFs)

Project Github:

[https://github.com/smalltong02/keras-llm-robot](h
ttps://github.com/smalltong02/keras-llm-robot)
```
---

     
 
all -  [ Could someone please explain the difference in front-ends for LLM's? ](https://www.reddit.com/r/LocalLLaMA/comments/1cpv419/could_someone_please_explain_the_difference_in/) , 2024-05-14-0910
```
Librechat, LMstudio, openweb-ui, text-generation ui, llama.cpp, kobold.cpp, SillyTavern, Vercel, Langchain etc. are just
 some of the many popular frontends for LLM interaction, it's a bit confusing. 

Which are the best, and whats the diffe
rence between them?

2. People often recommend LMstudio, but say it's not open-source. Doesn't it have a github download
? How's it not open-sourced if so? 

3. Back in the day, I remembered some front-ends resulting in flagging accounts if 
using AI API through popular online models. Is this still happening, if so, which cause it?
```
---

     
 
all -  [ Is it possible to change agent prompt based on user question after the agent is already created? ](https://www.reddit.com/r/LangChain/comments/1cpsg8f/is_it_possible_to_change_agent_prompt_based_on/) , 2024-05-14-0910
```
I was following the [LangChain SQL Documentation](https://python.langchain.com/v0.1/docs/use_cases/sql/agents/). So far 
I'm using Few shot prompt template as the prompt for the agent.

    agent = create_sql_agent(
        llm=self.llm,
   
     db=self.db,
        prompt=self.few_shot_prompt,
        verbose=True,
        agent_type='openai-tools',
        t
op_k=10,
    )

Now what I want to do is

1. Create a chain that creates a custom prompt based on user question
2. Then 
pass that custom prompt created by the chain to the agent to use when I invoke it

I've created the chain like this

   
 rg = RunnableParallel(
            {
                'input': lambda x: x['input'],
                'dialect': lambda x
: x['dialect'],
                'top_k': lambda x: x['top_k'],
                'tables': self.table_extraction_chain,
  
          }
        ).assign(prompt=self.few_shot_prompt)

can I pipe in the Agent here somehow to use the custom prompt
?
```
---

     
 
all -  [ Problem with heavy documents ](https://www.reddit.com/r/LangChain/comments/1cps3s5/problem_with_heavy_documents/) , 2024-05-14-0910
```
Hello, I am a beginner in LLM and LangChain, and I am developing a small application that allows me to query PDF documen
ts with my OpenAI API. Everything works well so far with the PDFs. I am able to query the PDFs. If the question is out o
f context, it shows that the information is not in the PDF, otherwise, it displays the information. So, everything is go
ing well at the moment, but the problem is that with documents that are a bit longer, 100 pages or more, I really have p
roblems because I can't even load them to query them. So, what should I do?
```
---

     
 
all -  [ Generate python functions automatically from openapi.json? ](https://www.reddit.com/r/openBB/comments/1cpkkb4/generate_python_functions_automatically_from/) , 2024-05-14-0910
```
If I run the REST server locally, I can get an openapi spec via http://127.0.0.1:8000/openapi.json .

which tools can pa
rse the json and generate a python function or sub for each endpoint?

I tried a couple with a custom python parser and 
I can generate a working function like the below from the json below, but wondering if anyone has done a proper job with
 good docstrings and parameters and defaults? 

tried the bravado module which should take an openai spec and turn it in
to REST get requests, didn't parse the JSON correctly, and openapi-python-client also failed.

wanted to experiment with
 langchain agents talking to openai, anthropic etc., and make a tool for e.g. all the equity endpoints that take a symbo
l. could also inspect the obb functions and docstrings. basically wondering if there is a standard way to do this sort o
f metaprogramming with the openbb platform.

    def equity_price_quote(symbol):
       '''the latest quote for a given 
stock. Quote includes price, volume, and other data.'''

      retval = None
      retlist = obb.equity.price.quote(symb
ol).results
      if retlist and type(retlist is list):
        retval = retlist[0].model_dump_json()
      return retva
l 

json:

        '/api/v1/equity/price/quote': {
            'get': {
                'tags': [
                    'e
quity'
                ],
                'summary': 'Quote',
                'description': 'Get the latest quote for a
 given stock. Quote includes price, volume, and other data.',
                'operationId': 'equity_price_quote',
     
           'parameters': [
                    {
                        'name': 'provider',
                        'in
': 'query',
                        'required': true,
                        'schema': {
                            'e
num': [
                                'cboe',
                                'fmp',
                                '
intrinio',
                                'tmx',
                                'tradier',
                           
     'yfinance'
                            ],
                            'type': 'string',
                           
 'title': 'Provider'
                        }
                    },
                    {
                        'nam
e': 'symbol',
                        'in': 'query',
                        'required': true,
                        '
schema': {
                            'type': 'string',
                            'description': 'Symbol to get data 
for. Multiple comma separated items allowed for provider(s): cboe, fmp, intrinio, tmx, tradier, yfinance.',
            
                'multiple_items_allowed': [
                                'cboe',
                                'fmp
',
                                'intrinio',
                                'tmx',
                                't
radier',
                                'yfinance'
                            ],
                            'title': 
'Symbol'
                        },
                        'description': 'Symbol to get data for. Multiple comma separ
ated items allowed for provider(s): cboe, fmp, intrinio, tmx, tradier, yfinance.'
                    },
               
     {
                        'name': 'use_cache',
                        'in': 'query',
                        'requ
ired': false,
                        'schema': {
                            'type': 'boolean',
                       
     'title': 'cboe',
                            'description': 'When True, the company directories will be cached for 
24 hours and are used to validate symbols. The results of the function are not cached. Set as False to bypass. (provider
: cboe)',
                            'default': true
                        },
                        'description': 
'When True, the company directories will be cached for 24 hours and are used to validate symbols. The results of the fun
ction are not cached. Set as False to bypass. (provider: cboe)'
                    },
                    {
           
             'name': 'source',
                        'in': 'query',
                        'required': false,
       
                 'schema': {
                            'enum': [
                                'iex',
              
                  'bats',
                                'bats_delayed',
                                'utp_delayed',

                                'cta_a_delayed',
                                'cta_b_delayed',
                     
           'intrinio_mx',
                                'intrinio_mx_plus',
                                'delayed_s
ip'
                            ],
                            'type': 'string',
                            'title': 'i
ntrinio',
                            'description': 'Source of the data. (provider: intrinio)',
                       
     'default': 'iex'
                        },
                        'description': 'Source of the data. (provider: 
intrinio)'
                    }
                ],
                'responses': {
                    '200': {
        
                'description': 'Successful Response',
                        'content': {
                            '
application/json': {
                                'schema': {
                                    '$ref': '#/componen
ts/schemas/OBBject_EquityQuote'
                                }
                            }
                        
}
                    },
                    '404': {
                        'description': 'Not found'
               
     },
                    '400': {
                        'description': 'No Results Found',
                        
'content': {
                            'application/json': {
                                'schema': {
             
                       '$ref': '#/components/schemas/OpenBBErrorResponse'
                                }
            
                }
                        }
                    },
                    '500': {
                        
'description': 'Internal Error',
                        'content': {
                            'application/json': {

                                'schema': {
                                    '$ref': '#/components/schemas/OpenBBErro
rResponse'
                                }
                            }
                        }
                   
 },
                    '422': {
                        'description': 'Validation Error',
                        'con
tent': {
                            'application/json': {
                                'schema': {
                 
                   '$ref': '#/components/schemas/HTTPValidationError'
                                }
                
            }
                        }
                    }
                },
                'model': 'EquityQuote',

                'examples': [
                    {
                        'scope': 'api',
                        'pa
rameters': {
                            'symbol': 'AAPL',
                            'provider': 'fmp'
               
         },
                        'provider': 'fmp'
                    }
                ]
            }
        },
```
---

     
 
all -  [ GPT3.5 tool calling more accurately than Claude haiku. ](https://www.reddit.com/r/LangChain/comments/1cpjgn1/gpt35_tool_calling_more_accurately_than_claude/) , 2024-05-14-0910
```
Using the same prompt, GPT 3.5 seems more likely to use tools correctly all the time whereas Claude haiku needs better p
rompting to achieve tool calling? Even so, it misses out a good number of times. 

For eg. I don’t even have to mention 
any tools in the gpt prompt but I have to mention in for haiku to even work. Putting the tool description and query work
s enough for gpt.

E.g a tool parameter for “rag vector query” correctly abstracts the query to keywords but haiku dumps
 the entire question in. GPT is also able to infer from history and use tools (eg, tell me more) while haiku just plain 
responds saying it has no more data. 

Am I using anything wrong? Everyone is saying haiku is smarter and all.. main rea
son I am trying it out is that it is cheaper, potentially allowing for more documents to stuff in. 
```
---

     
 
all -  [ Voice generation ](https://www.reddit.com/r/LangChain/comments/1cpcwcg/voice_generation/) , 2024-05-14-0910
```
Hey there, Is there any way to generate a voice?   
I found some impressive tools out there, but wish they were integrat
ed with langchain like this one: [https://github.com/jasonppy/VoiceCraft](https://github.com/jasonppy/VoiceCraft)
```
---

     
 
all -  [ [P] LLMinator: A Llama.cpp + Gradio based opensource Chatbot to run llms locally(cpu/cuda) directly  ](https://www.reddit.com/r/MachineLearning/comments/1cpbgd1/p_llminator_a_llamacpp_gradio_based_opensource/) , 2024-05-14-0910
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

     
 
all -  [ Function/tool calling on non-OpenAI models? ](https://www.reddit.com/r/LangChain/comments/1cpagwd/functiontool_calling_on_nonopenai_models/) , 2024-05-14-0910
```
I have a Next.js application that requires RAG (Specifically web search) with multiple open source models. Is there a wa
y to get them to work with function/tool calling?
```
---

     
 
all -  [ Agent to generate Charts based on the user's prompt ](https://www.reddit.com/r/LangChain/comments/1cp9gqj/agent_to_generate_charts_based_on_the_users_prompt/) , 2024-05-14-0910
```
https://preview.redd.it/4738d3i5aqzc1.png?width=723&format=png&auto=webp&s=89b493a6fc2271d489b0df2e6faddd3bf4a19f43

Hi 
Guys, I have a RAG for csv file, the data is about temperature sensors and apps usage percentage in a phone. I was able 
to use azure gpt 4 and generate a textual response. Since we have a csv file, I want the llm to also generate a graph al
ong with the textual response. Please tell me how to code this up.   
  

```
---

     
 
all -  [ Tutorial on Langchain that doesn't rely on an online service? ](https://www.reddit.com/r/learnprogramming/comments/1cp5udf/tutorial_on_langchain_that_doesnt_rely_on_an/) , 2024-05-14-0910
```
Like every tutorials use langchain with an online service, but I would like to build a llm or a simple chatbot with a cr
appy offline llm that we can run offline. Is there anything like it? I searched and it seems that there's nothing like i
t and it's basically a pipe dream.
```
---

     
 
all -  [ (Code included) I did a workshop on long-term selective memory for LLM applications recently ](https://www.reddit.com/r/LangChain/comments/1cp5q9p/code_included_i_did_a_workshop_on_longterm/) , 2024-05-14-0910
```
Good to be back making content for y’all.

Video: [https://www.youtube.com/watch?v=RkWor1BZOn0](https://www.youtube.com/
watch?v=RkWor1BZOn0)

Code: [https://github.com/trancethehuman/ai-workshop-code/blob/main/Long\_term\_memory\_%26\_perso
nalized\_LLM\_responses.ipynb](https://github.com/trancethehuman/ai-workshop-code/blob/main/Long_term_memory_%26_persona
lized_LLM_responses.ipynb)

Let me know in the comments what you liked / didn’t like about this and I’ll make it better 
next time.

or if you need clarifications, I‘m happy to answer to the best of my ability.
```
---

     
 
MachineLearning -  [ [D] Self-optimizing deterministic LLM memory using dspy, neo4j and vector databases. Need your input ](https://www.reddit.com/r/MachineLearning/comments/1cakjaf/d_selfoptimizing_deterministic_llm_memory_using/) , 2024-05-14-0910
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

     
 
deeplearning -  [ Seeking Advice: Solving Data Challenges with Large Language Models (LLMs) ](https://www.reddit.com/r/deeplearning/comments/1ca4nc1/seeking_advice_solving_data_challenges_with_large/) , 2024-05-14-0910
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

     
 
deeplearning -  [ Share the Coolest Out of The Box LLM Applications That Made You Say 'Wow that was smart' ](https://www.reddit.com/r/deeplearning/comments/1c9e6dj/share_the_coolest_out_of_the_box_llm_applications/) , 2024-05-14-0910
```
Hi, I'm looking at some LLM applications today but apart from guys doing big rags with langchain I don't see too many us
es that are out of the box or that make me say 'wow that was smart to use an LLM here'. Have you seen any cool stuff usi
ng LLMs recently that made you say 'wow, that was smart'?
```
---

     
