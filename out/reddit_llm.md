 
all -  [ Python-LLM - Session 4 - LangChain - Multi Agent - Supervisor - Agent - Query Mutual Funds Data ](https://www.reddit.com/r/u_SravzLLC/comments/1dmxfue/pythonllm_session_4_langchain_multi_agent/) , 2024-06-24-0912
```
**# Use Case**

Use LangChain Multi Agent: Supervisor Agent (JSON & Pandas Agents) to Query Mutual Funds Data



**## Se
ssion 4**

- LangSmith - debug LangGraph.

- Relevant document search update - make the documents more relevant.

- Add 
code = filename to all the objects recursively

- Integrate AWS S3 with JSONSplitter.

- In JSON Agent remove tools not 
used by the graph, this will prevent looping

- Remove pandas agent and use Python REPL agent.

- LangChain pandas agent
 hard codes a data frame and forwards to python repl agent, instead of that just provide the python repl agent.

- Sampl
e Queries





Documentation Link: [https://docs.sravz.com/docs/tech/python/langchain/#session-4](https://docs.sravz.com
/docs/tech/python/langchain/#session-4)

Source Code: [https://gist.github.com/sravzpublic/534dbb3695180a5deca4df6cd0c11
8f4](https://gist.github.com/sravzpublic/534dbb3695180a5deca4df6cd0c118f4)

Video Explanation: [https://youtu.be/oJ0lk6c
dxos](https://youtu.be/oJ0lk6cdxos)



Sravz LLC Training Series:

Analytics - [https://docs.sravz.com/docs/analytics/](
https://docs.sravz.com/docs/analytics/)

Tech - [https://docs.sravz.com/docs/tech/](https://docs.sravz.com/docs/tech/)




#cpp #c++  #cors   #boost #beast  #http #cmake #make #python #langchain #openai #llm
```
---

     
 
all -  [ Langchain Textloader does not load all of the text ](https://www.reddit.com/r/LLMDevs/comments/1dmwhxk/langchain_textloader_does_not_load_all_of_the_text/) , 2024-06-24-0912
```
I've gotten so far with my programming, but this little issue is holding me back from moving on creating my open source 
LLM to chat with text files.  When I call Textloader like this, I only get to see 844 out of like 12000 words in the ori
ginal text file.  No funny characters in the text file, I checked.  Was going to go through the whole tokenizing, embedd
ing, vectorstore process...but...why the H\*\*\* can't the loader load the entire text?  Can someone please help a rooki
e out here?  I even did it in a shorter way just loading it in one line of code but i did this the longer way to see if 
there were any other issues :(.  

    with open('textfile.txt', 'rb') as f:
        rawdata = f.read()
    result = cha
rdet.detect(rawdata)
    encoding = result['encoding']
    
    loader = TextLoader('pdf1.txt', encoding=encoding)
    d
ocument = loader.load()
    
```
---

     
 
all -  [ Classification Co-Pilot : No-prompt APIs for your Classification Pipelines ](https://www.reddit.com/r/LocalLLaMA/comments/1dmvaut/classification_copilot_noprompt_apis_for_your/) , 2024-06-24-0912
```
Hello all!  
I am one of the co-founders of Attuna.

We just shipped our Classification Co-Pilot. It is an exhaustive se
t of APIs with which you can build your LLM classification pipeline in minutes. With a few API calls within browser, you
 can export an inference endpoint that works seamlessly on your specific use case - No need to go over 100s of hugging f
ace models or struggle with langchain and dspy.

Specifically, we

Eliminate Tedious Prompting and Model Selection: Our 
platform takes care of prompting, model selection, and migration for you. You only need to provide training and test exa
mples, not bulky datasets.

Provide Instant Inference Endpoints: Once you provide the examples, our system constructs th
e most optimal pipeline in terms of prompts, models, and context ingestion, delivering a ready-to-use classification inf
erence endpoint in seconds.

Make it Highly Extensible: You can easily add new classes or tasks without changing anythin
g in your existing setup. This makes the system highly adaptable and future-proof.

  
Would love for you guys to try it
 out and any feedback would be immensely useful since we are very early and learning!

  
[https://api.attuna.xyz/](http
s://api.attuna.xyz/)

[https://www.loom.com/share/eabef7c1025d4db1a81dfc042afc92b4?sid=026c05d1-8223-452b-a55e-64a34c403
25d](https://www.loom.com/share/eabef7c1025d4db1a81dfc042afc92b4?sid=026c05d1-8223-452b-a55e-64a34c40325d)
```
---

     
 
all -  [ Recommendation for re-ranker model on retrieved results?  ](https://www.reddit.com/r/LangChain/comments/1dmuxu9/recommendation_for_reranker_model_on_retrieved/) , 2024-06-24-0912
```
Looking for a cost effective approach that doesn’t suck
```
---

     
 
all -  [ Optimize and configure integration classes wit **kwargs ](https://www.reddit.com/r/LangChain/comments/1dmtf4a/optimize_and_configure_integration_classes_wit/) , 2024-06-24-0912
```
Although the plenty of integrations make our life easier if committed to langchain, it is disproportionally more difficu
lt to optimize and configure their paramaters and especially the \*\*kwargs. I understand that these usually refer to th
e underlying package that the langchain class wraps around.

All docs have vanilla params and when some further configur
ation is needed or even explored then things become a bit of a pain.

The only way so far to find what \*\*kwargs are av
ailable for the integrations I use is to go deep in the langchain code to see whether these might be finally passed, rea
d the wrapped package documentation and also do extensive google search as it is not just the kwargs but also the syntax
 to pass them on (eg dict).

I guess this is not a big deal for a seasoned developer, but is there an easier way to do t
his, especially in the LLM era?
```
---

     
 
all -  [ Looking for ideas: How to handle parallel tool calls in LangGraph? ](https://www.reddit.com/r/LangChain/comments/1dmtcyn/looking_for_ideas_how_to_handle_parallel_tool/) , 2024-06-24-0912
```
I'm looking for some high-level advice around **LangGraph** and was hoping that this community might have some creative 
ideas.

I've been playing with LangGraph and I love how it lets you control the flow of a conversation. But **I'm strugg
ling with how to design a graph in light of parallel tool calling**.

Background: So, let's say I have a state that repr
esents the first 'stage' of a dialogue with an Agent. Once that stage is complete, I want the dialogue to move to the se
cond stage. (Each stage is represented as a state.) I have a tool called 'CompleteOrEscalate' (based on the LangGraph tu
torials) that the LLM can use when it thinks that the task for stage 1 is complete. I also have a second tool called 'To
FAQ' which can be used if the user asks a question that is not directly related to stage 1's task. So, stage 1 can condi
tionally transition to two other stages/states, depending on what the user says. This works great, *most of the time*.


But an issue arises when a user says something that causes the LLM to invoke more than one tool (i.e. the LLM is suggest
ing that we make more than one transition out of a state). For example, if the purpose of stage 1 is to confirm the user
's name, and the user says, 'Yes, I'm John Smith. And I have a question about ...' That input both completes the task (c
onfirming the user's name) AND contains a question (requiring an FAQ response). So, with parallel tool calling enabled t
he LLM returns both tool calls (CompleteOrEscalate and ToFAQ). This is actually pretty cool, but I'm not sure how to han
dle this situation in the conditional transition?

I've considered turning off parallel tool calling. This would force t
he LLM to call only one tool at a time. But it seems like a waste of tokens/time not to allow the LLM to return *both/al
l* tool calls.

Am I thinking about this all wrong? Is there a better way to handle this situation? TIA for any suggesti
ons or thoughts you may have.


```
---

     
 
all -  [ How to Improve RAG Performance ](https://www.reddit.com/r/LangChain/comments/1dmo3am/how_to_improve_rag_performance/) , 2024-06-24-0912
```
Just started using RAG with LangChain the last couple of weeks for a project at work.

First pass, I used this tutorial:
 [https://python.langchain.com/v0.2/docs/tutorials/rag/](https://python.langchain.com/v0.2/docs/tutorials/rag/)

Instead
 of a webloader, I used a textloader to load a small text file, a help file for a custom software framework.

I ran it, 
queried the model, and it worked great. I was excited.

The full amount of data I want to reference is about 18K small t
ext documents, about 179MB. I decided to work up to that, and just used about 10MB in about 1000 text documents. Query r
esults were much worse.

In one specific case, I asked about a scenario description that was stored in a file called ea.
txt. For troubleshooting, I increased the number of docs to be retrieved to 5 and added logging to show which docs were 
being retrieved.

The answer was wrong, and ed.txt was referenced three times, along with two other irrelevant docs. In 
the directory to be loaded, ed.txt directly follows ea.txt. How is RAG determining which docs to retrieve? The scenario 
I was asking about started with 'ea' (e.g. 'scenario ea4003'). Why would it pass over the file with the correct informat
ion, which contains strings that are much more similar to what I'm asking about? 

And does anyone have any advice on ho
w to improve performance? Thanks.
```
---

     
 
all -  [ Milvus - Updating the Embeddings ](https://www.reddit.com/r/vectordatabase/comments/1dmnfob/milvus_updating_the_embeddings/) , 2024-06-24-0912
```
The RAG system reads a series of PDF files, via the langchain PyPDFDirectoryLoader and chunks the data for storage in th
e standalone docker version of Milvus (V2.41).

Some of the documents have a limited lifespan and therefore when the doc
ument expires, I would like to delete them from Milvus without recreating all the embeddings. There is metadata in the e
mbeddings, but I don’t think I can delete the embeddings based on metadata as it doesn’t contain the primary key. My mor
e general question is how do you update a Milvus vector store, or are there better choices for this type of application?
 Do I need to use a SQL database to store the metadata and the primary keys?


```
---

     
 
all -  [ LLM Structured Output Benchmarks: Find the best LLM structured data parsing framework for your task! ](https://i.redd.it/j7pv9d6qxb8d1.jpeg) , 2024-06-24-0912
```
Parsing structured data from LLMs can be frustrating for anything beyond toy problems. These are some real problems I've
 faced:

👨‍🏫 For Classification tasks, the LLM must strictly adhere to a list of allowed classes, which can be as many a
s tens to hundreds in real-world problems. With more than a handful of classes, LLMs start hallucinating classes that ar
e not allowed!

📬 For NER, the LLM should only pick entities explicitly present in the text. These entities might be in 
a 2- or 3-level deeply nested structure like User → Address → City. LLMs struggle to capture these deeply nested fields 
reliably and either miss them or hallucinate something that doesn't exist.

🛢️ For Synthetic Data Generation, you might 
require a 2- or 3-level deeply nested data structure, and the challenges are similar to NER mentioned above.

Thankfully
, some open-source frameworks aim to solve these challenges, but I've been getting mixed results from them on complex pr
oblems like those mentioned above.

Over the past few weekends, I've been building LLM Structured Output Benchmarks to e
asily compare multiple frameworks on any dataset. You can plug in your dataset, run a command, and the metrics will be g
enerated. Then you can pick the best framework for any given problem.

I've implemented 6 of the top frameworks in a mul
ti-label classification problem and measured how reliable the output of each framework is. The experiment methodology is
 to run each text row of the dataset through each framework ten times and log the success rates to simulate the real-wor
ld finickiness I've been encountering for this task: The same input can pass sometimes and fail some other times 😐

For 
the dataset I used, Mirascope, Fructose, and Outlines have a perfect 100% reliability out-of-the-box, while the others s
how a small percentage of error, as I've experienced in real tasks. Therefore, this metric is a good proxy for real-worl
d performance.

I plan to add more frameworks and tasks to this benchmark. If you find this benchmark helpful, please st
ar it on GitHub!

🌟 LLM Structured Output Benchmarks Github: https://github.com/stephenleo/llm-structured-output-benchma
rks

```
---

     
 
all -  [ Building a Python library to quickly create+search knowledge graphs for RAG -- want to contribute? ](https://www.reddit.com/r/LangChain/comments/1dmm13w/building_a_python_library_to_quickly_createsearch/) , 2024-06-24-0912
```
Knowledge graphs can improve your RAG accuracy if your documents contain interconnected concepts.

And you can create+se
arch on KGs for your existing documents automatically by using the latest version of the knowledge-graph-rag library.

A
ll in just 3 lines of code.

In this example, I use medical documents. Here's how the library works:

1. Extract entitie
s from the corpus (such as organs, diseases, therapies, etc)

2. Extract the relationships between them (such as mitigat
ion effect of therapies, accumulation of plaques, etc.)

3. Create a knowledge graph from these representations using GP
T 3.5 / Haiku

4. When a user sends a query, break it down into entities to be searched.

5. Search the KG and use the r
esults in the context of the LLM call.

Here’s the repo: [https://github.com/sarthakrastogi/graph-rag](https://github.co
m/sarthakrastogi/graph-rag)

If you'd like to contribute or have suggestions for features, please raise them on Github.
```
---

     
 
all -  [ Bridging the Last Mile in LangChain Application Development ](https://community.aws/content/2gYKTV25GGIqAzgRyAdYbYTtCTf/bridging-the-last-mile-in-langchain-application-development) , 2024-06-24-0912
```

```
---

     
 
all -  [ I'm not sure I understand how to perform RAG on CSV files... ](https://www.reddit.com/r/LangChain/comments/1dmj7p7/im_not_sure_i_understand_how_to_perform_rag_on/) , 2024-06-24-0912
```
I'm looking to implement a way for the users of my platform to upload CSV files and pass them to various LMs to analyze.
 I get how the process works with other files types, and I've already set up a RAG pipeline for pdf files. 

However, wi
th PDF files I can 'simply' split it into chunks and generate embeddings with those (and later retrieve the most relevan
t ones), with CSV, since it's mostly data that could relate to each other, I'm not sure how to proceed.

For example, wh
ich criteria should I use to split the document into chunks? And what about the retrieval? Are embeddings relevant for C
SV files?

The main use case to RAG in this case -as compared to simply including the whole CSV as text in the prompt- i
s to save tokens, but is it possible to get decent results with RAG?

Thanks in advance
```
---

     
 
all -  [ What is ReAct Prompting? the most important piece in agentic frameworks ](https://www.reddit.com/gallery/1dmj2v9) , 2024-06-24-0912
```
“What is ReAct Prompting? the most important piece in agentic frameworks” - A quick read from Mastering LLM (Large Langu
age Model) 'Coffee Break Concepts' Vol.6

This document deeps dive into the ReAct Prompting method and why it's importan
t:
1. Limitations of LLM
2. Why ReAct prompting matters?
3. How ReAct Works?
4. LangChain Implementation
5. Why Prompt w
ithin agentic frameworks Matters?

Comment below on which topic you want to understand next in this 'Coffee Break Concep
ts' series and we will include those topics in upcoming weeks.
```
---

     
 
all -  [ Langchain chat history data structure in final prompt ](https://www.reddit.com/r/LangChain/comments/1dmeyfj/langchain_chat_history_data_structure_in_final/) , 2024-06-24-0912
```
I just find that chat history in final request look like that - 
`<CHAT HISTORY>
[HumanMessage(content='Message one'), A
IMessage(content='Hey'), HumanMessage(content='Message two')]
</CHAT HISTORY>`

i a bit confused, it how it should looks
, is it correct? 
As i remember i was something like this before: 
` AI:message \n USER:Text Message ` 

Can anyone clar
ify this for me?

P.S.: Does anyone have information on how models like OpenAI, Anthropic, or Gemini are trained to unde
rstand conversation history?

My research gives me this ideas:

```
  {
    'chat_history': [
      {'role': 'user', 'co
ntent': 'Message one'},
      {'role': 'ai', 'content': 'Hey'},
      {'role': 'user', 'content': 'Message two'}
    ]
 
 }
```

```
USER: Message one
AI: Hey
USER: Message two
```

```
<conversation>
  <user>Message one</user>
  <ai>Hey</ai
>
  <user>Message two</user>
</conversation>

```


Langchain use its own history structure for a  reason?



This is ho
w im execute it:
```
response = await self.llm_chain.ainvoke(
                {'input': self.llm_input.content},
       
         config={
                    'configurable': {
                        'user_id': self.user_id,
               
         'session_type': self.session_type,
                    },
                    'callbacks': [self.langfuse_handl
er],
                },
            )
```


_langchain = '^0.2.5'
langchain-core = '^0.2.9'
langchain-community = '^0.2.
5'_
```
---

     
 
all -  [ Using a chat interface to help people fill out a form ](https://www.reddit.com/r/LangChain/comments/1dmbnet/using_a_chat_interface_to_help_people_fill_out_a/) , 2024-06-24-0912
```
I'm new to LangChain and slowly working my way through the docs. My intention is to build a chat interface that has a co
nversation with a user and then slowly fills out a form behind the scenes as answers come in. 

Filling out the form dir
ectly is a lot of information upfront for the user whereas a chat interface lets me break the questions down into smalle
r chunks.

I'm trying to understand how I would use LangChain to do this. There are a lot of different moving parts to t
he framework and I was wondering if someone could point me in the right direction. That is, which modules I need to cove
r first or a relevant example of something similar.

Specific questions I have include:  
- How to keep costs down when 
polling the transcript to fill out the form. If i do this on every message submission it might get unnecessarily expensi
ve. But if I do it too infrequently then the bot might end up asking questions it already has the answer to. Was hoping 
the framework had some best practices I could rely on in this regard.  
- How to redirect the redirect the bot's focus b
ased on which questions still need answering.  
- How to implement a system to determine if an answer is good enough or 
if I need to ask more follow up questions to get a more substantial answer.  
- How to detect when all the questions hav
e been filled out so I can end the chat.

I'll slowly figuring it out but any pointers would be much appreciated. 

Also
, are there other LangChain specific forums where I can ask these types of questions that anyone recommends?
```
---

     
 
all -  [ Startup School: Gen AI ](https://www.reddit.com/r/googlecloud/comments/1dm9jjq/startup_school_gen_ai/) , 2024-06-24-0912
```
I'm taking the [Startup School: Gen AI by Google ](https://services.google.com/fh/files/emails/ssgenai_cloudskillsboost_
instructions.pdf)and  currently on week 3 labs.

I'm eager to start applying my knowledge to real-world problems, like t
raining an AI model with my own PDF documents. While the course videos have touched on this, the hands-on labs haven't a
ligned with these concepts until now. I'm hoping that the upcoming lab 'Creating a RAG Chat Assistant with MongoDB Atlas
 Vector Search, Google Cloud and Langchain' will finally demonstrate this process.

I'm curious why is there emphasis on
 MongoDB. Google Cloud offers a wide range of products, so I'm curious why we can't train Gemini AI using PDFs directly 
within Google's ecosystem. What is the specific advantage of incorporating a third-party product like MongoDB for this p
urpose?
```
---

     
 
all -  [ Since langchain gets alot of hate which are your libaraies for function calling agents and Rag ? ](https://www.reddit.com/r/LocalLLaMA/comments/1dm93r2/since_langchain_gets_alot_of_hate_which_are_your/) , 2024-06-24-0912
```
Like the title says I will be getting in to a project where i might need rather complex agents and I wanted to know whic
h frameworks are a good fit for that ? 
I heard alot of complaints about langchain so i wanted to know what is better ?
```
---

     
 
all -  [ confused on which llm framework to use ](https://www.reddit.com/r/learnmachinelearning/comments/1dm6n0q/confused_on_which_llm_framework_to_use/) , 2024-06-24-0912
```
Hello,

I'm a beginner in the field of LLMs and was struggling on what framework to pick. I am working on a small projec
t of mine wherein I scrape off soccer news articles and pass it through some LLM and ask it to generate a summary for me
. I realize to use some model I would need some sort of LLM framework and I have been looking into llamaindex. However, 
since I am a beginner I wanted to know which framework would be better for me to use ( llamaIndex or Langchain ) based o
n the criteria of my project. Thank you for your help.
```
---

     
 
all -  [ LinkedIn used Graph RAG to cut down their ticket resolution time from 40 hrs to 15 hrs. Let's make a ](https://www.reddit.com/r/LangChain/comments/1dlwc39/linkedin_used_graph_rag_to_cut_down_their_ticket/) , 2024-06-24-0912
```
So first, here's what I understand of how they did it:

They made the KG by parsing customer support tickets into struct
ured tree representations, preserving their internal relationships.

Tickets are linked based on contextual similarities
, dependencies, and references — all of these make up a comprehensive graph.

Each node in the KG is embedded so they ca
n do semantic search and retrieval.

The RAG QA system identifies relevant sub-graphs by doing traversal and searching b
y semantic similarity.

Then, it generates contextually aware answers from the KG, evaluating by MRR, which saw a signif
icant improvement.

Paper: [https://arxiv.org/pdf/2404.17723](https://arxiv.org/pdf/2404.17723)

If you’d like to implem
ent Graph RAG too, I’m creating a Python library which automatically creates this graph for the documents in your vector
db. It also makes it easy for you to retrieve relevant documents connected to the best matches.

If you're interested in
 contributing or have suggestions please raise them on Github.

Here’s the repo for the library: [https://github.com/sar
thakrastogi/graph-rag/tree/main](https://github.com/sarthakrastogi/graph-rag/tree/main)
```
---

     
 
all -  [ Career Change from Marketing to Analyst. Please review my resume and please give suggestions. ](https://www.reddit.com/r/resumes/comments/1dlv2al/career_change_from_marketing_to_analyst_please/) , 2024-06-24-0912
```
25F from India.

I am looking to transition from marketing to Analyst roles. There are a few reasons, one of them being 
that I do not enjoy the social media part of the job which is unavoidable in most of the marketing jobs. In my previous 
experience at a martech company, I got to work with the product team where I got to know more about the field of data(th
e product was a data pipeline) and I genuinely enjoyed working on data and creating reports and fetching insights.

I de
cided to leave and pursue a PG diploma in data science to get my foot in the door. I worked on few projects in ML, DL an
d NLP and really enjoyed working on it. Now I'm done with the course and looking for jobs in Data science/Analyst, Busin
ess analyst, ML engineer roles.

Would love suggestions from you guys. Thank

https://preview.redd.it/7sfx8d53f48d1.png?
width=1198&format=png&auto=webp&s=623771c0a12a2013c78b2ad7221f20b81fdc899a

https://preview.redd.it/p4oxai53f48d1.png?wi
dth=1198&format=png&auto=webp&s=19aeffcdd7a6de151f09cb46ec5d08b61accb4c8


```
---

     
 
all -  [ An article on why moving away from langchain ](https://www.reddit.com/r/LangChain/comments/1dlu5t9/an_article_on_why_moving_away_from_langchain/) , 2024-06-24-0912
```
As much as i like LangChain, there is some actual good points from this article 

https://www.octomind.dev/blog/why-we-n
o-longer-use-langchain-for-building-our-ai-agents

What you guys think ?
```
---

     
 
all -  [ How to stream messages with FastAPI and React? - LangGraph ](https://www.reddit.com/r/LangChain/comments/1dltljb/how_to_stream_messages_with_fastapi_and_react/) , 2024-06-24-0912
```
Hey guys!  
Has anyone tried and managed to find a successful solution, as to how I can messages in LangGraph through th
e usage of FastAPI and React?  
I have multiple nodes in my LangGraph app, and each one is appending a message to the 'm
essages' list attribute. I want these messages' content to be streamed as a single message in my React app, until I reac
h the END node.  
Does anyone have any idea as to how to do that?
```
---

     
 
all -  [ How to Use RabbitMQ or any other Broker with LangChain FastApi chatbot  ](https://www.reddit.com/r/LangChain/comments/1dlsxte/how_to_use_rabbitmq_or_any_other_broker_with/) , 2024-06-24-0912
```
. 
```
---

     
 
all -  [ What is the best python library for chatbot UIs? ](https://www.reddit.com/r/LangChain/comments/1dlrouj/what_is_the_best_python_library_for_chatbot_uis/) , 2024-06-24-0912
```
I know that streamlit was popular, but neither optimized for chatbot interactivity, nor ready to set up for production.


I assume some TypeScript + REACT is state of the art, but I am a Data Scientist and no frontend developer.

Are there a
ny new libraries that nicely integrate with LangGraph and also FastAPI?
```
---

     
 
all -  [ LangChain alternatives for a Next.js project? ](https://www.reddit.com/r/LangChain/comments/1dlolna/langchain_alternatives_for_a_nextjs_project/) , 2024-06-24-0912
```
I need to do RAG and web browsing. What other libraries can I use (except LangChain) that can achieve this functionality
?
```
---

     
 
all -  [ Benchmarking PDF models for parsing accuracy ](https://www.reddit.com/r/LangChain/comments/1dlfth6/benchmarking_pdf_models_for_parsing_accuracy/) , 2024-06-24-0912
```
Hi folks, I often see questions about which open source pdf model or APIs are best for extraction from PDF. We attempt t
o help people make data-driven decisions by comparing the various models on their private documents.

We benchmarked sev
eral PDF models - Marker, EasyOCR, Unstructured and OCRMyPDF.

Marker is better than the others in terms of accuracy. Ea
syOCR comes second, and OCRMyPDF is pretty close.

You can run these benchmarks on your documents using our code - https
://github.com/tensorlakeai/indexify-extractors/tree/main/pdf/benchmark

The benchmark tool is using Indexify behind the 
scenes - https://github.com/tensorlakeai/indexify

Indexify is a scalable unstructured data extraction engine for buildi
ng multi-stage inference pipelines. The pipelines can handle extraction from 1000s of documents in parallel when deploye
d in a real cluster on the cloud.

I would love your feedback on what models and document layouts to benchmark next. 

F
or some reason Reddit is marking this post as spam when I add pictures, so here is a link to the docs with some charts -
 https://docs.getindexify.ai/usecases/pdf_extraction/#extractor-performance-analysis
```
---

     
 
all -  [ Roast my resume! I'm in Canada and I've applied to 500+ positions but not heard anything ](https://i.redd.it/y0m8xn89uz7d1.png) , 2024-06-24-0912
```
I'm graduating next week. Applied to over 500 jobs with and without referrals. I don't get any call backs! 

I'm looking
 for anything in the Data Science/Machine Learning/AI development space 
```
---

     
 
all -  [ How does AI agent orchestration work in practice? ](https://www.reddit.com/r/learnmachinelearning/comments/1dlewks/how_does_ai_agent_orchestration_work_in_practice/) , 2024-06-24-0912
```
I recently read the following article which talks about using a 'boss' AI to orchestrate a collection of AI agents, and 
the idea of an AI agent that learns ones business model:

https://sifted.eu/articles/autonomous-companies-ai

Reality/hy
pe aside, I'm having trouble understanding how this sort of thing works in practice. Like, what does the code for this s
ort of thing *actually* look like? How do you train a model on such an abstract concept as 'business model'?

FWIW, I'm 
a hobby practitioner. I've played around with langchain and understand prompt chaining, but I'm still struggling to get 
from *here* to *there*.
```
---

     
 
all -  [ Leveraging NLP/Pre-Trained Models for Document Comparison and Deviation Detection ](https://www.reddit.com/r/LangChain/comments/1dldrbr/leveraging_nlppretrained_models_for_document/) , 2024-06-24-0912
```
How can we leverage an NLP model or Generative AI pre-trained model like ChatGPT or Llama2 to compare two documents, lik
e legal contracts or technical manuals, and find the deviation in the documents.

Please give me ideas or ways to achiev
e this or if you have any Youtube/Github links for the reference.

Thanks
```
---

     
 
all -  [ I built an SQL Agent with Langchain - Here's my experience ](https://www.reddit.com/r/LangChain/comments/1dlaqn7/i_built_an_sql_agent_with_langchain_heres_my/) , 2024-06-24-0912
```
My agent writes queries to retrieve data from Sqlite Databases. This was my first time writing an agent with a good and 
serious usecase. The first framework i used for this was Langchain. 

1. Very easy to implement: Its pretty convenient t
o import LLMs Gpt, Claude, Gemini. The documentation for it also clear.

2. Tools: This is my favourite part about the f
ramework, writing tools and importing them is very easy and it helps in building for a lot of usecases.

3. Documentatio
n can be improved since there are multiple versions and each time i click to the stable version, it goes back to the hom
epage.

https://i.redd.it/1b8v8xv4vy7d1.gif

Here's the [GITHUB LINK](https://github.com/ComposioHQ/composio/tree/master
/python/examples/sql_agent) if you want to try it out.
```
---

     
 
all -  [ I made an AI Agent for my SQL Database ](https://www.reddit.com/r/agi/comments/1dl7my1/i_made_an_ai_agent_for_my_sql_database/) , 2024-06-24-0912
```
I've developed an SQL Agent that automates query writing and visualizes data from SQLite databases. Here are some of my 
insights from the development process:

1. **Automation Efficiency**: Agents can streamline numerous processes, saving s
ubstantial time while maintaining high accuracy.
2. **Framework Challenges**: Building these agents requires considerabl
e effort to understand and implement frameworks like Langchain, LLamaIndex, and CrewAI, which still need further improve
ment.
3. **Scalability Potential**: These agents have great potential for scalability, making them adaptable for larger 
and more complex datasets.

https://i.redd.it/7z3mb55w7y7d1.gif

Here's the [GITHUB LINK](https://github.com/ComposioHQ/
composio/tree/master/python/examples/sql_agent)

Link for each framework

[CREWAI](https://github.com/ComposioHQ/composi
o/tree/master/python/examples/sql_agent/sql_agent_plotter_crewai)  
[LANGCHAIN](https://github.com/ComposioHQ/composio/t
ree/master/python/examples/sql_agent/sql_agent_plotter_langchain)  
[LLAMAINDEX](https://github.com/ComposioHQ/composio/
tree/master/python/examples/sql_agent/sql_agent_plotter_llama_index)
```
---

     
 
all -  [ Manage your entire SQL Database with AI ](https://www.reddit.com/r/AcceleratingAI/comments/1dl7kvk/manage_your_entire_sql_database_with_ai/) , 2024-06-24-0912
```
I've developed an SQL Agent that automates query writing and visualizes data from SQLite databases, significantly saving
 time and effort in data analysis. Here are some insights from the development process:

1. **Automation Efficiency**: A
gents can streamline numerous processes, saving substantial time while maintaining high accuracy.
2. **Framework Challen
ges**: Building these agents requires considerable effort to understand and implement frameworks like Langchain, LLamaIn
dex, and CrewAI, which still need further improvement.
3. **Scalability Potential**: These agents have great potential f
or scalability, making them adaptable for larger and more complex datasets.

https://i.redd.it/jfdt5lxy6y7d1.gif

Here's
 the [GITHUB LINK](https://github.com/ComposioHQ/composio/tree/master/python/examples/sql_agent)

Link for each framewor
k

[CREWAI](https://github.com/ComposioHQ/composio/tree/master/python/examples/sql_agent/sql_agent_plotter_crewai)  
[LA
NGCHAIN](https://github.com/ComposioHQ/composio/tree/master/python/examples/sql_agent/sql_agent_plotter_langchain)  
[LL
AMAINDEX](https://github.com/ComposioHQ/composio/tree/master/python/examples/sql_agent/sql_agent_plotter_llama_index)
```
---

     
 
all -  [ Chatbot development help ](https://www.reddit.com/r/LangChain/comments/1dl7ho6/chatbot_development_help/) , 2024-06-24-0912
```
I was developing Chatbot for telegram
Where i used to scrap contents from websites using langchain webBaseLoader

But th
e problem is, the data was too rough (eg: one content title combines with another) and some times the entire data may no
t be useful or the contents are in non-English language

But i need only the contents to be in proper format as much as 
possible

Any better possible way, that can improve content scraping from websites?

I found, some of the API are availa
ble they provide better content scraping, but I'm student, so i can't invest on those
Free API was not enough for my pur
pose as well

Thankyou for everybody in advance ❤️
```
---

     
 
all -  [ How to RAG Indexing and embedding by local llama index with langchain huggingface ?
 ](https://www.reddit.com/r/LangChain/comments/1dl6udt/how_to_rag_indexing_and_embedding_by_local_llama/) , 2024-06-24-0912
```
All resource on web all need OpenAI api key.

how to run local? last monther there is HuggingFace x LangChain

I tried t
o write some concept code but cannot find right way

    from llama_index.core import SimpleDirectoryReader, VectorStore
Index, ServiceContext
    from langchain_huggingface.embeddings import HuggingFaceEmbeddings
    from langchain_huggingf
ace.llms import HuggingFacePipeline
    from langchain_huggingface import HuggingFacePipeline
    
    # Define your loc
al models
    embedding_model_name = 'sentence-transformers/all-mpnet-base-v2'
    llm_model_name = 'StabilityAI/stablel
m-tuned-alpha-3b'
    
    # Initialize the embedding model
    embed_model = HuggingFaceEmbeddings(model_name=embedding
_model_name)
    
    # Initialize the LLM using from_model_id method
    llm = HuggingFacePipeline.from_model_id(model_
id=llm_model_name, task='text-generation')
    
    # Create a service context
    service_context = ServiceContext.from
_defaults(embed_model=embed_model, llm=llm)
    
    # Load data from the 'data' directory
    reader = SimpleDirectoryR
eader(input_dir='./data', recursive=True)
    documents = reader.load_data()
    
    # Create an index from the loaded 
documents
    index = VectorStoreIndex.from_documents(documents, service_context=service_context)
    
    # Save the in
dex to a file
    index.save_to_disk('index.json')
    
```
---

     
 
all -  [ LangGraph with Ollama learning resource ](https://www.reddit.com/r/LangChain/comments/1dl6o2t/langgraph_with_ollama_learning_resource/) , 2024-06-24-0912
```
I make a repo [LangGraph-learn](https://github.com/LangGraph-GUI/LangGraph-learn)   
there are step by step to understan
d langgraph features and run on ollama   
  
because many people feel langgraph too hard to learn. such [Am I the only o
ne langgraph docs suck?](https://www.reddit.com/r/ArtificialInteligence/comments/1d4lxrv/am_i_the_only_one_langgraph_doc
s_suck/) [Am I the only one who feels LangGraph documentation and tutorials by lanfchain absolutely suck?](https://www.r
eddit.com/r/LangChain/comments/1d4lwt0/am_i_the_only_one_who_feels_langgraph/)
```
---

     
 
all -  [ Flow Engineering with LangChain/LangGraph and CodiumAI - Harrison Chase interviews Itamar Friedman,  ](https://www.reddit.com/r/LangChain/comments/1dl6hl0/flow_engineering_with_langchainlanggraph_and/) , 2024-06-24-0912
```
The talk among Itamar Friedman (CEO of CodiumAI) and Harrison Chase (CEO of LangChain) explores best practices, insights
, examples, and hot takes on flow engineering: [Flow Engineering with LangChain/LangGraph and CodiumAI](https://www.yout
ube.com/watch?v=eBjxz7qrNBs)


Flow Engineering can be used for many problems involving reasoning, and can outperform na
ive prompt engineering. Instead of using a single prompt to solve problems, Flow Engineering uses an interative process 
that repeatedly runs and refines the generated result. Better results can be obtained moving from a prompt:answer paradi
gm to a 'flow' paradigm, where the answer is constructed iteratively.
```
---

     
 
all -  [ Simply explaining how LoRA actually works (ELI5) ](https://www.reddit.com/r/LangChain/comments/1dl53nn/simply_explaining_how_lora_actually_works_eli5/) , 2024-06-24-0912
```
Suppose in your LLM you have the original weight matrix W of dimensions d x k.

Your traditional training process would 
update W directly -- that’s a huge number of parameters if d x k is large, needing a lot of compute.

So, we use Low-Ran
k Decomposition to break it down before weight update. Here’s how —We represent the weight update (Delta W) as a product
 of two lower-rank matrices A and B, such that Delta W = BA.

Here, A is a matrix of dimensions r x k and B is a matrix 
of dimensions d x r. And here, r (rank) is much smaller than both d and k.

Now, Matrix A is initialised with some rando
m Gaussian values and matrix B is initialised with zeros.

Why? So that initially Delta W = BA can be 0.

Now comes the 
training process:

During weight update, only the smaller matrices A and B are updated — this reduces the number of para
meters to be tuned by a huge margin.

The effective update to the original weight matrix W is Delta W = BA, which approx
imates the changes in W using fewer parameters.

Let’s compare the params to be updated before and after LoRA:

Earlier,
 the params to be updated were d x k (remember the dimensions of W).

But now, the no. of params is reduced to (d x r) +
 (r x k). This is much smaller because the rank r was taken to be much smaller than both d and k.

This is how low-rank 
approximation gives you efficient fine-tuning with this compact representation.

Training is faster and needs less compu
te and memory, while still capturing essential information from your fine-tuning dataset.

  
I also made a quick animat
ion using Artifacts to explain (took like 10 secs):

[https://www.linkedin.com/posts/sarthakrastogi\_simply-explaining-h
ow-lora-actually-works-activity-7209893533011333120-RSsz](https://www.linkedin.com/posts/sarthakrastogi_simply-explainin
g-how-lora-actually-works-activity-7209893533011333120-RSsz)
```
---

     
 
all -  [ LangGraph in production? ](https://www.reddit.com/r/LangChain/comments/1dl47vz/langgraph_in_production/) , 2024-06-24-0912
```
I just wanted to ask all your opinion on Langgraph in production? I want to build a chatbot with multiple agents: one ag
ent that connects to a database, one agent that performs RAG and one agent for conversational purposes, and Langgraph is
 the tool I see would fit the most but I'm not so sure if it's ready to take to production.
```
---

     
 
all -  [ what's the difference btw llamacpp and GPT4ALL? ](https://www.reddit.com/r/LocalLLM/comments/1dl1zb0/whats_the_difference_btw_llamacpp_and_gpt4all/) , 2024-06-24-0912
```
Hi guys, I'm new to running llm locally with langchain.  
I wanna ask what's the difference btw llamacpp and GPT4ALL?

w
hich model formats are supported by llamacpp and GPT4ALL? what are different quantization options available. ? Plz any g
ood advice would be much appreciated.
```
---

     
 
all -  [ Xin kinh nghiệm Training Chatbot GPT bằng tài liệu hiệu quả ](https://www.reddit.com/r/TroChuyenLinhTinh/comments/1dl1pfg/xin_kinh_nghiệm_training_chatbot_gpt_bằng_tài/) , 2024-06-24-0912
```
Các bác có kinh nghiệm training chatbot GPT bằng tài liệu có thể chia sẻ thêm cho em được không ạ?  
Hixhix, Chẳng là bê
n công ty em có xây dựng 1 con bot chạy nội bộ, sử dụng langchain và kéo API của ChatGPT để sử dụng.  
Trong quá trình t
raining bằng tài liệu doanh nghiệp, mãi mà nó vẫn ngu, em thử nhiều cách khác nhau rồi, kể cả thay thế toàn bộ các tài l
iệu mà mãi không thấy có hiệu quả TT.  
Đội ơn các bác nhiều!

P/S ảnh em nói xamlol với nó tí thôi chứ k phải là cách e
m training lại đâu ạ =))
```
---

     
 
all -  [ How can i get feedback on my site from LLM ](https://www.reddit.com/r/LangChain/comments/1dl0p4o/how_can_i_get_feedback_on_my_site_from_llm/) , 2024-06-24-0912
```
So in my last project, I made a site that takes the URL of your landing page and gives you recommendations on what you s
hould change in your landing page's content. Now it was only for content, not for any visuals and I want to go one step 
further and implement the same for the visuals but don't have any idea how I can do that.

Here is the link to the site:
 [https://landing-page-audit-pwa.vercel.app](https://landing-page-audit-pwa.vercel.app)
```
---

     
 
all -  [ The new model from Anthropic Claude Sonnet 3.5 knows how to program AI tools in Go ](https://www.reddit.com/r/golang/comments/1dkz78p/the_new_model_from_anthropic_claude_sonnet_35/) , 2024-06-24-0912
```
To my surprise, Claude Sonnet 3.5 knows [langchaingo](https://github.com/tmc/langchaingo)!  
  
I used [https://github.c
om/tmc/cgpt](https://github.com/tmc/cgpt) to generate a langchaingo program:\]

    $ cgpt
    >>> how can I do a stream
ing inference call with langchaingo?
    >>> 
    To perform a streaming inference call with LangChain Go, you can use t
he streaming functionality provided by the library. Here's a general approach to set up streaming inference:

And it pro
duced on the very first attempt, this program, exactly verbatim:  


    package main
    
    import (
        'context
'
        'fmt'
        'os'
    
        'github.com/tmc/langchaingo/llms'
        'github.com/tmc/langchaingo/llms/ope
nai'
    )
    
    func main() {
        // Create a new OpenAI client
        client, err := openai.New()
        if e
rr != nil {
            fmt.Printf('OpenAI client creation error: %v\n', err)
            os.Exit(1)
        }
    
    
    // Define the streaming callback function
        streamingCallback := func(ctx context.Context, chunk []byte) error
 {
            fmt.Print(string(chunk))
            return nil
        }
    
        // Set up the context and prompt
 
       ctx := context.Background()
        prompt := 'Tell me a short story about a robot learning to paint.'
    
     
   // Make the streaming inference call
        _, err = client.Call(ctx, prompt,
            llms.WithStreamingFunc(str
eamingCallback),
            llms.WithMaxTokens(150),
        )
    
        if err != nil {
            fmt.Printf('Str
eaming call error: %v\n', err)
            os.Exit(1)
        }
    
        // Add a newline at the end for better form
atting
        fmt.Println()
    }
    

Along with accurate instructions about how to set up a new go module, etc.  
  

I'm very impressed happy to see my project make it into the weights of this really impressive model.!  
  
This example
 program produces a story that goes something like:

>Once upon a time, in a bustling city filled with creativity and in
novation, there was a robot named Artie. Artie was designed to perform various tasks, but he had always been fascinated 
by the art that surrounded him.

>One day, Artie stumbled upon a group of artists painting beautiful landscapes in the p
ark. Intrigued by their talent and skill, Artie decided that he wanted to learn how to paint too.

>With the help of his
 creator, Artie was programmed with the ability to hold a paintbrush and mix colors on a palette. At first, his painting
s were simple and messy, but Artie was determined to improve.

  
I also posted about this here: [https://x.com/traviscl
ine/status/1804068056135553054](https://x.com/traviscline/status/1804068056135553054)
```
---

     
 
MachineLearning -  [ [P] Seeking Feedback on My GenAI Job Fit Project - New to LangChain/LangGraph ](https://www.reddit.com/r/MachineLearning/comments/1dgns9p/p_seeking_feedback_on_my_genai_job_fit_project/) , 2024-06-24-0912
```
Hi all,

Soo, i have been working on a a projectcalled [GenAI Job Fit](https://github.com/DAVEinside/GenAI_Job_Fit). It'
s an AI-driven system designed to enhance job applications by providing tailored recommendations based on individual pro
files.

I'm relatively new to LangChain and LangGraph, and I've incorporated them into this project. I would greatly app
reciate it if you could check out the repository and provide any feedback or suggestions for improvement.

Your insights
 on how I can better implement LangChain/LangGraph, or any other aspect of the project, would be incredibly valuable. I'
m eager to learn and make this project as robust as possible.

Thank you in advance for your time and feedback!

Repo Li
nk : [https://github.com/DAVEinside/GenAI\_Job\_Fit](https://github.com/DAVEinside/GenAI_Job_Fit)
```
---

     
 
MachineLearning -  [ [P] I'm tired of LangChain, so I made a simple open-source alternative with support for tool using a ](https://www.reddit.com/r/MachineLearning/comments/1deffo8/p_im_tired_of_langchain_so_i_made_a_simple/) , 2024-06-24-0912
```
[https://github.com/piEsposito/tiny-ai-client](https://github.com/piEsposito/tiny-ai-client)

The motivation for buildin
g tiny-ai-client comes from a frustration with Langchain, that became bloated, hard to use and poorly documented - and t
akes inspiraton from [simpleaichat](https://github.com/minimaxir/simpleaichat/tree/main), but adds support to vision, to
ols and more LLM providers aside from OpenAI (Gemini, Anthropic - with Groq and Mistral on the pipeline.)

I'm building 
this to to continue what simpleaichat started and not to ride on hype, raise money or whatever, but to help people do 2 
things: build AI apps as easily as possible and switching LLMs without needing to use Langchain.

This is a minimally vi
able version of the package, with support to vision, tools and async calls. There are a lot of improvements to be done, 
but even at its current state, tiny-ai-client has generally improved my interactions with LLMs and has been used in prod
uction with success.

Let me know what you think: there are still a few bugs that may need fixing, but all the examples 
work and are easy to be be adapted to your use case.
```
---

     
 
MachineLearning -  [ [P] Superfast RAG: Langchain Streaming and Groq ](https://www.reddit.com/r/MachineLearning/comments/1d5s9g4/p_superfast_rag_langchain_streaming_and_groq/) , 2024-06-24-0912
```
  
Fast LLM RAG inference using Groq and Langchain Streaming.  
  
Groq is introducing a new, simpler processing archite
cture designed specifically for the performance requirements of machine learning applications and other compute-intensiv
e workloads. The simpler hardware also saves developer resources by eliminating the need for profiling, and also makes i
t easier to deploy AI solutions at scale.  
  
Resource: [https://www.youtube.com/watch?v=frMdOL8knqg](https://www.youtu
be.com/watch?v=frMdOL8knqg)
```
---

     
 
deeplearning -  [ How to finetune? ](https://www.reddit.com/r/deeplearning/comments/1daio0h/how_to_finetune/) , 2024-06-24-0912
```
Can someone guide me to some resource how can I finetune an open source llm or some library (like langchain) on unstruct
ured data (example: news articles on cricket) So that model can answer a question (like When did India won world Cup?)
```
---

     
