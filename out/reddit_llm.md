 
all -  [ checkpoint>channel_values>messages records the entire chat history. Is this scalable? ](https://www.reddit.com/r/LangChain/comments/1fqak8v/checkpointchannel_valuesmessages_records_the/) , 2024-09-27-0913
```
As we implement a chatting agent with langgraph and Firestore database, we're trying to implement a Firestore checkpoint
er to record historical data in the Firestore db. We've just realized that each checkpoint data contains the entire chat
 message history in checkpoint>channel\_values>messages.

This means if I have 5 chat messages in the chat history, each
 checkpoint>channel\_values>messages would look like this:

\[msg1, msg2, msg3, msg4, msg5\]

\[msg1, msg2, msg3, msg4\]


\[msg1, msg2, msg3\]

\[msg1, msg2\]

\[msg1\]



Is this a scalable approach? As more messages accumulate, the last c
heckpoint data size would become huge. Yes, it'd be convenient to have all historical data, but we'd definitely need to 
summarize, trim, or filter messages when calling the LLM.



Am I missing something? I'm trying to understand the intent
ion behind this design.


```
---

     
 
all -  [ Implementing a Smart, Multi-Variant Product Search in a LangGraph-Based Order System for a Hardware  ](https://www.reddit.com/r/LangChain/comments/1fq8ydl/implementing_a_smart_multivariant_product_search/) , 2024-09-27-0913
```
Hello everyone,

I'm developing an order system for a fake hardware store called MetalTech using TypeScript, Node.js, an
d LangGraph. I'm looking to enhance our virtual assistant with a smart product search capability before adding items to 
an order.

What I'm aiming to achieve:

1. Integrate a real database (open to suggestions).

2. Implement an intelligent
 product search function that:

   - Handles exact matches

   - Deals with misspellings

   - Recognizes synonyms or al
ternative product names

   - Matches with multiple variants of a product



For instance, I want the system to:

- Reco
gnize 'screws' might refer to 'Stainless Steel Screw' in the database

- Understand 'hammr' is likely a misspelling of '
hammer'

- Know that 'cutting disc' could be the same as 'abrasive wheel'

- Match 'drill' with various types like 'cord
less drill', 'hammer drill', 'drill press', etc.



My main challenges are:

1. Structuring this smart search efficientl
y within the LangGraph architecture

2. Implementing fuzzy matching for misspellings

3. Creating a system for synonyms 
and alternative product names

4. Designing a way to return and handle multiple product variants



Key questions:

- Ho
w can I implement this multi-faceted search effectively?

- How should I handle cases where a general term (like 'drill'
) matches multiple specific products?



Has anyone implemented a similar smart, multi-variant search system, especially
 within a LangGraph-based application? Any suggestions on approaches, libraries, or best practices would be greatly appr
eciated.



Thank you in advance for your insights!
```
---

     
 
all -  [ How to update prompts dynamically? ](https://www.reddit.com/r/LangChain/comments/1fq0iun/how_to_update_prompts_dynamically/) , 2024-09-27-0913
```
So, I have a graph with agents that have their prompts. Now, I'm trying to update prompts from client side which  will b
e reflected on the graph. But then the graph needs to create a entirely new graph, right? This is causing my FastAPI ser
ver to be very slow, can we change this?
```
---

     
 
all -  [ How to solve this error 'ollama run llama3.1:latest
Error: llama runner process no longer running: - ](https://www.reddit.com/r/LangChain/comments/1fq08an/how_to_solve_this_error_ollama_run_llama31latest/) , 2024-09-27-0913
```

```
---

     
 
all -  [ How to run any LLM locally ? ](https://www.reddit.com/r/LangChain/comments/1fpzl3a/how_to_run_any_llm_locally/) , 2024-09-27-0913
```
Tell me whole step to run an llm locally from scratch please
```
---

     
 
all -  [ Long document chunk ranking by order of contribution to document itself ](https://www.reddit.com/r/LangChain/comments/1fpzg1s/long_document_chunk_ranking_by_order_of/) , 2024-09-27-0913
```
Is there a way to rank a list of chunks or passage by order of importance using an LLM, with methods such as ColBert for
 example. I don't have any metrics in mind, or if this requires a complex chunk to chunk reranking, or contribution of a
 chunk or passage to a summary of summary, but curious for context understanding if suchh method exists?
```
---

     
 
all -  [ [For Hire] Programmer/Web Developer/IT Consultant (Python, PHP, AI, etc.) ](https://www.reddit.com/r/forhire/comments/1fpxbvc/for_hire_programmerweb_developerit_consultant/) , 2024-09-27-0913
```
To get in contact, please message me, I don't use the chat thing and might miss you or reply very late. Then we can swit
ch to email/discord/telegram or whatever else. Apologies for starting with this, but many missed it when it was lower.


I'm a programmer/web developer with 15 years of professional experience. I am available for all sorts of programming and
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

     
 
all -  [ An advice on architecture for session-based file processing and data disposal ](https://www.reddit.com/r/LangChain/comments/1fpw9qd/an_advice_on_architecture_for_sessionbased_file/) , 2024-09-27-0913
```
I'm working on a simple POC for one of my clients where they want their users to stop using ChatGPT (for obvious governa
nce, data privacy reasons). They want us to come up with a simple alternative to ChatGPT with a model endpoint in Azure 
OpenAI. The main feature that the people use is 'upload and talk to the file' feature from ChatGPT. They upload PDFs, Ex
cels and get help from the language models to summarize, visualize, report better.

The app has a very simple flow -

1.
 Allow users to upload files for a chat session
2. Use AI to answer questions about these uploaded files
3. Dispose of a
ll data when the session ends or times out

The main architectural challenge is handling the lifecycle of the data:

* E
fficiently processing and storing uploaded files
* Ensuring complete data cleanup after the session

A few questions - 


1. What's the best way to architect this kind of session-based file processing and AI chat application?
2. How can we h
andle file storage and embedding creation in a way that's both efficient during the session and easy to clean up after?

3. Are there specific services or technologies that are well-suited for this kind of temporary, session-based data handl
ing?

I'm particularly interested in hearing about real-world solutions and any lessons learned from implementing simila
r systems. Any advice, best practices, or even cautionary tales would be greatly appreciated!
```
---

     
 
all -  [ A Community for AI Evaluation and Output Quality ](https://www.reddit.com/r/LangChain/comments/1fpvwt0/a_community_for_ai_evaluation_and_output_quality/) , 2024-09-27-0913
```
If you're focused on output quality and evaluation in LLMs, I’ve created r/AIQuality —a community dedicated to those of 
us working to build reliable, hallucination-free systems.

Personally, I’ve faced constant challenges with evaluating my
 RAG pipeline. Should I use DSPy to build it? Which retriever technique works best? Should I switch to a different gener
ator model? And most importantly, how do I truly know if my model is improving or regressing? These are the questions th
at make evaluation tough, but crucial.

With RAG and LLMs evolving rapidly, there wasn't a space to dive deep into these
 evaluation struggles—until now. That’s why I created this community: to share insights, explore cutting-edge research, 
and tackle the real challenges of evaluating LLM/RAG systems.

If you’re navigating similar issues and want to improve y
our evaluation process, join us. [https://www.reddit.com/r/AIQuality/](https://www.reddit.com/r/AIQuality/)
```
---

     
 
all -  [ LLamaParse vs LLMWhisperer? ](https://www.reddit.com/r/LangChain/comments/1fpvkdm/llamaparse_vs_llmwhisperer/) , 2024-09-27-0913
```
Looking for a solution to parse fairly complex PDFs (graphs, images, tables across multiple pages) into text to use for 
RAG and indexing - accuracy is pretty key. These two seem to come up the most often when searching online - with LlamaPa
rse recently coming out with their new premium version.

Which do folks normally use and why? Or is unstructured io norm
ally good enough

Are there any pdf2text benchmarks out there to run them against each other? This seems like a fairly c
ommon task
```
---

     
 
all -  [ Streaming LLM response on a flask application using websockets ](https://www.reddit.com/r/LangChain/comments/1fpuif6/streaming_llm_response_on_a_flask_application/) , 2024-09-27-0913
```
I have a flask application and I want to stream the LLM responses using websockets. How do I go about it? I am using a c
ustom callback handler, which I call while defining my llm. The second code is taken from ChatGPT, which is basically th
e code for the websockets. Sometimes I face an error saying '/ is not a connected namespace'. I am new to using websocke
ts, so I have no idea and any help would be appreciated. Thank you!

    #1
    class WebSocketCallbackHandler(BaseCallb
ackHandler):
        def __init__(self, room):
            self.room = room
    
        def on_llm_new_token(self, toke
n: str, **kwargs):
            events.stream(self.room, token)  
    
    
    #2
    from flask_socketio import SocketI
O
    import config
    import warnings
    import socketio
    import threading
    import time
    
    message_event 
= threading.Event()
    sio = socketio.Client()
    warnings.filterwarnings('ignore')
    
    
    namespace = '/' 
   
 sio.connect(config.socket_url, namespaces=[namespace])
    
    @sio.event
    def connect():
        print(f'Connected
 to server on namespace: {namespace}')
        
    def reconnect():
        for _ in range(5): 
            try:
      
          sio.connect(config.socket_url, namespaces=[namespace])
                break 
            except socketio.exce
ptions.ConnectionError:
                time.sleep(5)  
                print('Retrying connection...')
    
    @sio.ev
ent
    def disconnect():
        print(f'Disconnected from server on namespace: {namespace}')
    
    @sio.event
    d
ef connect_error(data):
        print(f'Connection failed on namespace: {namespace} -', data)
    
    @sio.event
    de
f message(data):
        print(f'Message received from namespace {namespace}:', data)
        message_event.set()
    
 
   def send_message(room, message):
        print(f'Sending message to room {room}: {message}')
        sio.emit('messag
e', {'room': room, 'msg': message}, namespace=namespace)
        
    def stream(room, result):
        try:
           
 message_event.wait() 
            print(f'Streaming result to room {room}: {result}')
            sio.emit('message', {
'room': room, 'msg': result}, namespace=namespace)
            message_event.clear()
        except socketio.exceptions.
ConnectionError as e:
            print(f'Error streaming data: {str(e)}')
            reconnect(room) 
    
    def joi
n_room(room):
        print(f'Joining room: {room}')
        sio.emit('join', {'room': room}, namespace=namespace)
    

    def leave_room(room):
        print(f'Leaving room: {room}')
        sio.emit('leave', {'room': room}, namespace=nam
espace)
```
---

     
 
all -  [ How to update a vectorstore without wiping and reloading all docs? ](https://www.reddit.com/r/LangChain/comments/1fptqvy/how_to_update_a_vectorstore_without_wiping_and/) , 2024-09-27-0913
```
I'm using LlamaIndex for loading, OpenAI for embedding, and MongoDB Atlas as my vectorstore. Our setup involves pulling 
unstructured data from Confluence.

Is there a way to update only the parts that have changed and add/remove new info wi
thout reloading everything? I've tried different approaches, like generating an ID based on the title and chunk to compa
re, but it always ends up reloading the entire dataset into the vectorstore. Every time I run my script, the vectorstore
 grows with duplicates -  doubling or even tripling in size.

How do you guys handle this? Is there a better solution th
an just wiping the vectorstore and reloading it from scratch each time?
```
---

     
 
all -  [ Built a RAG System with MiniLM, Pinecone, and Llama-2-7b-chat for Text Generation – Query Time is To ](https://www.reddit.com/r/LangChain/comments/1fptdng/built_a_rag_system_with_minilm_pinecone_and/) , 2024-09-27-0913
```
I'm new to working with large language models (LLMs) and Retrieval-Augmented Generation (RAG). I've been building a conv
ersational bot using a dataset from Kaggle. The embedding creation, storage, and retrieval using MiniLM and Pinecone hav
e gone smoothly, but I'm running into issues with text generation.

Currently, I'm using **Llama-2-7b-chat.Q4\_K\_M.gguf
** for generation, but the output time is painfully slow. I considered using the OpenAI API, but as a college student, I
 can't afford the subscription, and for a small project like this, it seems overkill anyway.

Could anyone suggest alter
natives for faster text generation, or improvements I could make to optimize my current setup? I'd appreciate any advice
 on reducing the query time, or tips on steps I might have overlooked. Thanks in advance!



Here's the link to the code
 for reference: [https://github.com/praneeetha1/RecipeBot](https://github.com/praneeetha1/RecipeBot)
```
---

     
 
all -  [ How should I resolve these langchain dependency issues with v0.63.2? ](https://i.redd.it/6ze9ophb44rd1.jpeg) , 2024-09-27-0913
```
I keep running into version conflicts when I use langchain with the new version of crewai. How can I resolve them or wil
l there be an update for this? I would really appreciate some help on this!
```
---

     
 
all -  [ My SQL Agent is not able to differentiate between Java and Javascript , what can I do to fix it ? ](https://www.reddit.com/r/LangChain/comments/1fpqzf4/my_sql_agent_is_not_able_to_differentiate_between/) , 2024-09-27-0913
```
Hello everyone , I built an SQL agent using Langgraph .

Reference : [https://docs.smith.langchain.com/tutorials/Develop
ers/agents#sql-agent](https://docs.smith.langchain.com/tutorials/Developers/agents#sql-agent) 

Currently , I'm able to 
get \~70% accuracy with the questions that I tested it with .   
  
One of the problems with it is that most of the time
s it is not able to differentiate between words like Javascript and Java , Digital Marketing and Marketing .  
  
Upon e
xamining the Langchain traces , I found that the when querying the SQL DB , the keyword used is LIKE .  
I know it shoul
d be = and not LIKE in the Skills part .

How do I fix this ?

https://preview.redd.it/q2fm4q3y04rd1.png?width=1258&form
at=png&auto=webp&s=bdae99b852acdb4e9937c68de3756fa99ca10301


```
---

     
 
all -  [ How chat with your PDFs work? ](https://www.reddit.com/r/LangChain/comments/1fpq6id/how_chat_with_your_pdfs_work/) , 2024-09-27-0913
```
I am trying to create a RAG that works by asking questions on a custom PDF. Users can upload PDF and ask questions. I cr
eated a pre-processing approach that works for my sample pdfs pretty well. But here users can upload any pdfs and chat. 
  
  
I understand pre-processing is an important step but with pdfs that doesn't have common format of text arrangement
, how one can implement that. I think its not possible to take a unified approach for pre-processing for all types of pd
fs. But have seen lots of chat with your pdfs application online nowadays. Are they really good? if so what approach the
y might have taken? What everyone thinks? Correct me if I am wrong. Would like to hear more views. 
```
---

     
 
all -  [ AutoRAG v0.3.0 is Here! - AutoML tool for RAG ](https://www.reddit.com/r/Rag/comments/1fppo71/autorag_v030_is_here_automl_tool_for_rag/) , 2024-09-27-0913
```
Hey everyone, we’re excited to announce the release of **AutoRAG v0.3.0**, packed with some great improvements!

[https:
//github.com/Marker-Inc-Korea/AutoRAG](https://github.com/Marker-Inc-Korea/AutoRAG)

# What is AutoRAG?

[AutoRAG suppor
ts evaluation data creation and auto optimization of RAG + deploy](https://preview.redd.it/8oisml8wi3rd1.png?width=2784&
format=png&auto=webp&s=9c2b107bbfd5504592bbead1aa756932f46ab053)

AutoRAG is an **AutoML tool** designed to help you aut
omatically find the optimal **Retrieval-Augmented Generation (RAG) pipeline** for **your data**. There are tons of RAG p
ipelines and modules out there, but finding the best one for your specific use case can be tough and time-consuming. Wit
hout evaluating different modules, you might never know which setup works best for your needs.

AutoRAG solves this by a
llowing you to evaluate multiple RAG modules with your own data and automatically pinpoint the best pipeline for your us
e case.

[How AutoRAG optimizes complex RAG pipelines](https://i.redd.it/knhg6ls2j3rd1.gif)

# What’s new in v0.3.0?

1.
 **Faster response time for deployments**
2. **Improved data creation pipeline** with customizable parsing and chunking 
tools using YAML.
3. Now supports  LangChain 0.3, LlamaIndex 0.11, and OpenAI o1 models.

Check out how to use AutoRAG a
nd what can you do with it in [here](https://docs.auto-rag.com/index.html)!
```
---

     
 
all -  [ Help with Relationship Extraction using SchemaLLMPathExtractor and Ollama ](https://www.reddit.com/r/LanguageTechnology/comments/1fpofgu/help_with_relationship_extraction_using/) , 2024-09-27-0913
```
Hi Everyone,  
I'm working on relationship extraction using the `PropertyGraphStore` class from Langchain, following the
 approach outlined in [this guide](https://docs.llamaindex.ai/en/stable/examples/property_graph/property_graph_advanced/
). I'm trying to restrict the nodes and relationships being extracted by using `SchemaLLMPathExtractor`.

However, I'm f
acing an issue when using local models like Llama 3.1 and Mistral through Ollama: nothing gets extracted. Interestingly,
 if I remove `SchemaLLMPathExtractor`, it extracts a lot of relationships. Additionally, when I use OpenAI instead of Ol
lama, it works fine even with `SchemaLLMPathExtractor`.

Has anyone else experienced this issue or know how to make Olla
ma work properly with `SchemaLLMPathExtractor`? It seems to be working for others in blogs and videos, but I can’t figur
e out what I’m doing wrong. Any help or suggestions would be greatly appreciated!
```
---

     
 
all -  [ Agentic workflow using tools and functions using Llama 3.1/3.2 and vLLM ](https://www.reddit.com/r/LocalLLaMA/comments/1fpo7st/agentic_workflow_using_tools_and_functions_using/) , 2024-09-27-0913
```
Hello community,
I wish to know if someone has had experience with agentic workflows that use function and tools using l
lama3.1 models? The model is hosted on vLLM.

I was not able to see much resources in this area most of them pointed tow
ards closed source models that use langgraph or langchain.

I did find llama-stack from meta but it was difficult for me
 to wrap my head around it. If anyone can help, my learning can get easier.

Thank you.
```
---

     
 
all -  [ Open source collaborative ide with ai features  ](https://www.reddit.com/r/LangChain/comments/1fpnqub/open_source_collaborative_ide_with_ai_features/) , 2024-09-27-0913
```
Can anyone suggest any opensource collaborative IDE with ai code generation features.
```
---

     
 
all -  [ Looking for ideas on a front-end migration tool (Angular to React)  ](https://www.reddit.com/r/ChatGPTCoding/comments/1fpmstb/looking_for_ideas_on_a_frontend_migration_tool/) , 2024-09-27-0913
```
Hi everyone!

I'm a Python developer working at a consulting firm, and we're tasked with building a front-end migration 
tool for one of our clients. They’ve already migrated some React code from Angular, which could be useful as part of a f
ew-shot approach. However, I should mention that both Angular and React are outside my core expertise.

We’re considerin
g two possible directions for this migration:

1. Coding assistant tool: A RAG (Retrieval-Augmented Generation) chatbot 
that understands the codebase and, based on user interactions, suggests code snippets or modifications.


2. Fully autom
ated agent: A system that automatically generates React code after analyzing the existing Angular codebase.



With so m
any tools out there, I’m curious if anyone has worked on a similar project and could recommend some approaches. Here's a
 list of tools I’ve come across and how they fit into our potential strategies:

Cursor: We’re thinking of recommending 
the business version of Cursor to our client. It has a 'compose' feature that seems promising for migration.

Langchain:
 It has some useful tutorials on code comprehension, but it’s not great for quick code generation across multiple folder
s. Still, it could be valuable for the chatbot approach (direction 1).

GPT-Engineer: This is more suited for generating
 a full code project based on a prompt, but it lacks comprehensive code comprehension features, which limits its usefuln
ess for code migration.


Has anyone here dealt with a similar need? I’d love to hear any suggestions or ideas on other 
tools that might be helpful.

Thanks in advance!
```
---

     
 
all -  [ Document loaders for inconsistent table structures in PDF ](https://www.reddit.com/r/LangChain/comments/1fpm4pg/document_loaders_for_inconsistent_table/) , 2024-09-27-0913
```
Does anyone have tips on using / building a document loader for PDFs with tables? I have a bunch of PDFs each with table
s showcasing the same information. Some of the PDFs have tables which don’t have all the required columns. Some of the c
olumns in the PDF are multi line. Is there a good resource to understand how to parse these PDFs? 

I have done research
 and found unstructured the best so far but then the html generated can have multiple row spans (if the column values ar
e multi line). Whats the best way to extract this html into a pandas dataframe? I find beautiful soup doing a decent job
 but it falters when the rowspan is more than 1. Any advice? Willing to pay for a 1:1 consult. 
```
---

     
 
all -  [ SurfSense - Personal AI Assistant for Internet Surfers. ](https://www.reddit.com/r/pythoncoding/comments/1fpgxry/surfsense_personal_ai_assistant_for_internet/) , 2024-09-27-0913
```
# What my project does:

Whenever I'm researching or studying anything, I tend to save a ton of content. It could be a c
ool article link, a fact someone mentioned in my chats or a blog post about it. But organizing all this content and then
 effectively researching or learning from it is a difficult task. That’s where SurfSense comes in. SurfSense acts like a
 personal brain for any content you consume, allowing you to easily revisit, organize, and effectively research and lear
n from your saved content.

Check it out at [https://github.com/MODSetter/SurfSense](https://github.com/MODSetter/SurfSe
nse)

# Why I am posting here:

Well my project have 3 things where extension and frontend is made in JS but core backen
d is made in python with LangChain and FastAPI.

If any good python devs could go through my backend and suggest some ti
ps to improve it would be great.

And if u know any good resources about WebSockets implementation with FastAPI do menti
on in comments.

# Target Audience:

Researchers, Students or Anyone who consume a lot of content
```
---

     
 
all -  [ SurfSense - Personal AI Assistant for Internet Surfers. ](https://www.reddit.com/r/PythonProjects2/comments/1fpgxbg/surfsense_personal_ai_assistant_for_internet/) , 2024-09-27-0913
```
# What my project does:

Whenever I'm researching or studying anything, I tend to save a ton of content. It could be a c
ool article link, a fact someone mentioned in my chats or a blog post about it. But organizing all this content and then
 effectively researching or learning from it is a difficult task. That’s where SurfSense comes in. SurfSense acts like a
 personal brain for any content you consume, allowing you to easily revisit, organize, and effectively research and lear
n from your saved content.

Check it out at [https://github.com/MODSetter/SurfSense](https://github.com/MODSetter/SurfSe
nse)

# Why I am posting here:

Well my project have 3 things where extension and frontend is made in JS but core backen
d is made in python with LangChain and FastAPI.

If any good python devs could go through my backend and suggest some ti
ps to improve it would be great.

And if u know any good resources about WebSockets implementation with FastAPI do menti
on in comments.

# Target Audience:

Researchers, Students or Anyone who consume a lot of content

https://reddit.com/li
nk/1fpgxbg/video/xgtqfzeh51rd1/player


```
---

     
 
all -  [ Seeking Advice on Building a chatbot ](https://www.reddit.com/r/LangChain/comments/1fpbc91/seeking_advice_on_building_a_chatbot/) , 2024-09-27-0913
```
I'm a complete beginner who's interested in building a chatbot for educational purposes, particularly to help university
 students with their course materials. I'm intrigued by the idea of using LangChain, but I have a few questions before d
iving in:

1. **Is LangChain suitable for building a chatbot for educational purposes?** I'm aiming to create something 
that can assist with answering questions about lecture notes, assignments, and course concepts. Do you think LangChain i
s a good starting point for this, or are there better alternatives for such educational use cases?
2. **How should I get
 started with LangChain and RAG as a complete beginner?** I've seen some resources online, but they seem quite advanced.
 Could anyone recommend beginner-friendly tutorials, articles, or videos that walk through the basics of LangChain and h
ow to implement RAG effectively?
3. **What are the best practices or tips for building a chatbot with LangChain that han
dles educational content?** Are there any specific features, techniques, or workflows you'd recommend to make the chatbo
t more effective and responsive for students?
```
---

     
 
all -  [ [3 YoE, Unemployed/Graduate, Data Scientist, USA] How cooked am I? ](https://i.redd.it/0urze04xwzqd1.jpeg) , 2024-09-27-0913
```
Roast me!
```
---

     
 
all -  [ Struggling with Local RAG Application for Sensitive Data: Need Help with Document Relevance & Speed! ](https://www.reddit.com/r/LangChain/comments/1fp87sy/struggling_with_local_rag_application_for/) , 2024-09-27-0913
```
Hey everyone!

I’m a new NLP intern at a company, working on building a completely local RAG (Retrieval-Augmented Genera
tion) application. The data I’m working with is extremely sensitive and can’t leave my system, so everything—LLM, embedd
ings—needs to stay local. No exposure to closed-source companies is allowed.

I initially tested with a sample dataset (
not sensitive) using Gemini for the LLM and embedding, which worked great and set my benchmark. However, when I switched
 to a fully local setup using Ollama’s Llama 3.1:8b model and sentence-transformers/all-MiniLM-L6-v2, I ran into two big
 issues:

1. The documents extracted aren’t as relevant as the initial setup (I’ve printed the extracted docs for multip
le queries across both apps). I need the local app to match that level of relevance.

2. Inference is painfully slow (\\
\~5 min per query). My system has 16GB RAM and a GTX 1650Ti with 4GB VRAM. Any ideas to improve speed?

I would apprecia
te suggestions from those who have worked on similar local RAG setups! Thanks!


```
---

     
 
all -  [ Is there any need of storing embeddings for Summarization process ](https://www.reddit.com/r/LangChain/comments/1fp7z9q/is_there_any_need_of_storing_embeddings_for/) , 2024-09-27-0913
```
Is it necessary to store embeddings and content chunks in a database when performing summarization, or can the process b
e done directly without saving these elements?
```
---

     
 
all -  [ PROMPT UNABLE TO UNDERSTAND DATE (LLAMA3.1-8B-STORM) + LANGGRAPH ](https://www.reddit.com/r/LangChain/comments/1fp7lzh/prompt_unable_to_understand_date_llama318bstorm/) , 2024-09-27-0913
```
Hello,  
I am using LLAMA3.1-8b-storm to get file name from natural language. The file name contains a date in yyyy-mm-d
d format.  
I have prompted the model to use its knowledge of big bench date understanding dataset as well, but it does 
not perform well.  
Has anyone solved this/ similar problem?

Any suggestions for tools to design (to be used by the age
nt) in order to solve this problem?

Also, any other model suggestions(open/ closed source) that are good at agentic wor
kflows?

Thank you for your inputs.
```
---

     
 
all -  [ Hugging Face vs LLMs ](https://www.reddit.com/r/datascience/comments/1fp3jkv/hugging_face_vs_llms/) , 2024-09-27-0913
```
Is it still relevant to be learning and using huggingface models and the ecosystem vs pivoting to a langchain llm api? F
eel the majomajor AI modeling companies are going to dominate the space soon. 
```
---

     
 
all -  [ Where do I begin? ](https://www.reddit.com/r/LLMDevs/comments/1fp284d/where_do_i_begin/) , 2024-09-27-0913
```
Senior Backend Engineer wanting to apply to Generative AI startups in the next 3-12 months.

What do I begin learning wi
th?  
Any courses or playlists you'd recommend I start with?

Not just with LangChain but GenAI overall.  
I keep findin
g a lot of courses, but they do assume some knowledge before hand.


```
---

     
 
all -  [ How does the automatic tools choosing work ? ](https://www.reddit.com/r/LangChain/comments/1fp0m9v/how_does_the_automatic_tools_choosing_work/) , 2024-09-27-0913
```
There is [a topic about building an agent](https://python.langchain.com/docs/tutorials/agents/) in LangChain docs. It sa
ys that the following code:

    from langchain_community.tools.tavily_search import TavilySearchResults
    from langch
ain_core.messages import HumanMessage
    from langchain_openai import ChatOpenAI
    
    search = TavilySearchResults(
max_results=2)
    tools = [search]
    model = ChatOpenAI(model='gpt-4')
    model_with_tools = model.bind_tools(tools)

    response = model_with_tools.invoke([HumanMessage(content='Hi!')])
    print(f'ContentString: {response.content}')
 
   print(f'ToolCalls: {response.tool_calls}')

prints out this:

    ContentString: Hello!
    ToolCalls: []

but if rep
lace 'Hi!' with 'What's the weather in SF?'

    response = model_with_tools.invoke([HumanMessage(content='What's the we
ather in SF?')])

i get this:

    contentstring:
    ToolCalls: [{'name': 'tavily_search_results_json', 'args': {'query
': 'weather san francisco'}, 'id': 'toolu_01VTP7DUvSfgtYxsq9x4EwMp'}]

As you can see, the decision whether to use the t
ool or not is made automatically depending on the prompt.

So my question is how is it implemented? I assume that there 
is some sentence transformer which translates the tool description into embeddings, then translates my promt into embedd
ings with the same sentence transformer and put those embeddings into some local vector data base. And if the distance b
etween my prompt and the description is small then LangChain decides to use the tool. Am i right? If it so, what exactly
 sentence transformer is used ?
```
---

     
 
all -  [ Built a web agent which call fill Google forms based on the user details [P] ](https://www.reddit.com/r/MachineLearning/comments/1fozud5/built_a_web_agent_which_call_fill_google_forms/) , 2024-09-27-0913
```
GitHub repo : [https://github.com/shaRk-033/web-agent](https://github.com/shaRk-033/web-agent)

Tried to solve it using 
two approaches:

# 1: Basic Scraping and Filling

This is the straightforward approach. The agent scrapes the form’s HTM
L and uses fixed XPaths to find and fill in the required fields.

* It pulls the form’s HTML, locates the fields with se
t XPaths, and inputs the answers. It’s a direct and simple method.
* If the form changes or an element isn’t where it’s 
expected, the process can fail and may need manual adjustments.

[basic approach](https://preview.redd.it/5e8g4a1k4xqd1.
png?width=1055&format=png&auto=webp&s=d8e984e4feaee2f0453b08c8696768c40a2a5c20)

2. Using LangChain Agents and tool call
ing

* LangChain Agent**:** The agent handles everything by using the LLM’s reasoning to decide what to do next, includi
ng generating those tricky XPaths.
* Error Handling**:** If something goes wrong (like an element not found), the agent 
tries again with better XPaths until it gets the job done.

[using langchain agents](https://preview.redd.it/948i88pl4xq
d1.png?width=782&format=png&auto=webp&s=ed1e6c19efec9f4cbbbd6ab5a22558f221cf745f)

Any recommendations to improve this w
ould be welcome. Also, if anyone has ideas on building similar web agents to automate other tasks, it would be great to 
hear them. :)
```
---

     
 
all -  [ Fast API based server or AWS Lambda & Chalice API ](https://www.reddit.com/r/aws/comments/1foyhag/fast_api_based_server_or_aws_lambda_chalice_api/) , 2024-09-27-0913
```
I am building a search toolbox which has about 20 lambdas currently. It’s all written in python. We are using libraries 
like OpenAI, llama index, langchain and others. It’s for a llm based search engine.
Each lambda is almost 250+ mb on ECR
 and has a run configuration (memory: 512 mb and 5 minutes of potential uptime).

I plan to expand this significantly in
 the upcoming months and am looking at adding many more features. 

I want to understand if it would be better bet to sw
itch to Fast API this early.

I am from a startup with limited resources.
However, I am seeing that lambdas have cold st
arts and usually low on performance side and I don’t want to lose out on performance.

Another thing to consider is, our
 team is of freshers and it might be more challenging to move to fast api later with many functionalities than now

Plea
se advice
```
---

     
 
all -  [ OllamaEmbeddings ](https://www.reddit.com/r/LangChain/comments/1foxreq/ollamaembeddings/) , 2024-09-27-0913
```
I am trying to do the following import but I end up in the error:

Import:

from langchain_ollama import OllamaEmbedding
s

Error:
Importers: Cannot import name ‘model_validator’ from ‘pydantic’

Versions:
Python 3.11
Langchain-ollama 0.2.0

Pydantic 2.9.2
MacOS
```
---

     
 
all -  [ [Hiring] Fullstack Developer for Migration ](https://www.reddit.com/r/FreelanceProgramming/comments/1foxo48/hiring_fullstack_developer_for_migration/) , 2024-09-27-0913
```
I've built a prototype web application using simple Streamlit (Python) framework to test out an MVP. Now seeing traction
 on my platform, I would like to hire a fullstack developer to do a migration onto a proper stack (NextJS + Tailwind + S
hadcn / Supabase / FastAPI).

As this is a 1:1 migration you get the benefit of having a predefined scope with a predict
ably workload. The backend logic uses a couple of LLM-related tasks using LangChain / OpenAI ChatCompletion API but can 
be re-used as backend should stay within Python.

If this migration is successful, we can continue the business relation
ship as I plan to extend the application scope (e.g., payment/subscription).
```
---

     
 
all -  [ Production ready use cases? ](https://www.reddit.com/r/LangChain/comments/1fow3zc/production_ready_use_cases/) , 2024-09-27-0913
```
Most of my friends working in different companies started working on chatbot for their company product.  
Most of them f
inished the POC and never moved on to production, Just leveraged the PR of the feature, but didn't allocate enough resou
rces to finish it.

It somehow feels like most companies use LLMs not as product of it's own but rather as tool for solv
ing small tasks within an organization.   
Like parsing unstructured data to structured one, auto classification tasks a
nd some for search ( relaying on embedding )

Does your company have different production ready use cases?
```
---

     
 
all -  [ Seeking Advice on Building a RAG Chatbot ](https://www.reddit.com/r/LangChain/comments/1fovzyz/seeking_advice_on_building_a_rag_chatbot/) , 2024-09-27-0913
```
Hey everyone,

I'm a math major at the University of Chicago, and I'm interested in helping my school with academic sche
duling. I want to build a Retrieval-Augmented Generation (RAG) chatbot that can assist students in planning their academ
ic schedules. The chatbot should be able to understand course prerequisites, course times, and the terms in which course
s are offered. For example, it should provide detailed advice on the courses listed in our mathematics department catalo
g: [University of Chicago Mathematics Courses](http://collegecatalog.uchicago.edu/thecollege/mathematics/).

This projec
t boils down to building a reliable RAG chatbot. I'm wondering if anyone knows any RAG techniques or services that could
 help me achieve this outcome—specifically, creating a chatbot that can inform users about course prerequisites, schedul
es, and possibly the requirements for the bachelor's track.

Could the solution involve structuring the data in a specif
ic way? For instance, scraping the website and creating a separate file containing an array of courses with their prereq
uisites, schedules, and quarters offered.

Overall, I'm very keen on building this chatbot because I believe it would be
 valuable for me and my peers. I would appreciate any advice or suggestions on what I should do or what services I could
 use.

Thank you!
```
---

     
 
all -  [ Career path with expertise in AI, but major interest in Software Engineering ](https://www.reddit.com/r/cscareerquestions/comments/1fovlc7/career_path_with_expertise_in_ai_but_major/) , 2024-09-27-0913
```
Hello everyone,

I am a fresh graduate in AI with a bachelor in Computer Science.

During my Master I noticed that I don
't like data science, AI research or training models as much as I like software development. I hate preparing experiment
al notebooks and leave the results hanging there without seeing an actual application.

Hence I am looking for advices o
n what could be the best career for me. Something that integrates AI expertise in a software development environment.

I
 am now working as a developer while also using Langchain, hence NLP agents. Although I would love a job where I create 
and integrate even other AI applications in a development environment.

Is a career like this possible or is it too broa
d? Any advice?
```
---

     
 
all -  [ Langsmith for Human Eval (Annotation Queues) ](https://www.reddit.com/r/LangChain/comments/1fosalz/langsmith_for_human_eval_annotation_queues/) , 2024-09-27-0913
```
Has anyone used the langsmith human eval workflow in a production setting?

How do you like it - is it useful over Googl
e sheets or other alternatives? What do you like / dislike about it. 
```
---

     
 
all -  [ Online prompt management best practice ](https://www.reddit.com/r/LangChain/comments/1fopx64/online_prompt_management_best_practice/) , 2024-09-27-0913
```
Hey,

I'd like some advice on how safe it is to retrieve prompts from an online platform (like LangSmith or LangFuse) fo
r an LLM app in prod. 

What is usually done to add safeguards in case of accidental prompt deletion, platform failure, 
or whatever? If you have any insights, that would be great. Thank you very much!
```
---

     
 
all -  [ Discussion: Best Way to Plot Charts Using LLM? ](https://www.reddit.com/r/LangChain/comments/1fopcus/discussion_best_way_to_plot_charts_using_llm/) , 2024-09-27-0913
```
Hi guys, how are you plotting charts or graphs? Currently, I am using structured output and sending it to the frontend t
o plot with Plotly React.

I've seen [chat2plot](https://github.com/nyanp/chat2plot) use a dataframe with the data, quer
ying it from the LLM and then structuring the output, but it only uses the dataframe to plot the chart. The LLM never di
rectly accesses that data.

In my current approach, I get the data from an API and then pass it to the LLM, which format
s the data and the structure for the chart. However, this is currently slow.

What approach do you recommend for handlin
g chart generation in this kind of setup?

Regards!
```
---

     
 
all -  [ Why is this Python wrapper class code so hard to understand? ](https://i.redd.it/icgrxyoh3uqd1.png) , 2024-09-27-0913
```
I'm working with a Python class that wraps around Google Generative Al, but the code is tough to follow. It imports adva
nced libraries. I'm struggling to understand why it's so complicated.

I asked AI to explain but it's still very technic
al not able to understand.

```
---

     
 
MachineLearning -  [ [P] Swapping Embedding Models for an LLM ](https://www.reddit.com/r/MachineLearning/comments/1fktvbj/p_swapping_embedding_models_for_an_llm/) , 2024-09-27-0913
```
How tightly coupled is an embedding model to a language model?

Taking an example from Langchain's tutorials, they use O
llama's _nomic-embed-text_ for embedding and _Llama3.1_ for the understanding and Q/A. I don't see any documentation abo
ut Llama being built on embeddings from this embedding model. 

Intuition suggests that a different embedding model may 
produce outputs of other sizes or produce a different tensor for a character/word, which would have an impact on the res
ults of the LLM. So would changing an embedding model require retraining/fine-tuning the LLM as well?

I need to use a e
mbedding model for code snippets and text. Do I need to find a specialized embedding model for that? If yes, how will ll
ama3.1 ingest the embeddings?
```
---

     
 
MachineLearning -  [ [P] Review and suggest ideas for my chatbot ](https://www.reddit.com/r/MachineLearning/comments/1fb2mwl/p_review_and_suggest_ideas_for_my_chatbot/) , 2024-09-27-0913
```
Ok, so I am currently trying to build support chatbot with following technicalities 
1. FastAPI for web server(Need to m
ake it faster)
2. Qdrant as Vector Data Base(Found it to be the fastest amongst Chromadb, Elastic Search and Milvus)
3. 
MongoDB for storing all the data and feedback.
4. Semantic chunking with max token limit of 512.
5. granite-13b-chat-v2 
as the LLM(I know it's not good but I have limited options available)
6. The data is structured as well as unstructured.
 Thinking of having involving GraphRAG with current architecture.
7. Multiple data sources stored in multiple collection
s of vector database because I have implemented an access control.
8. Using mongoengine currently as a ORM. If you know 
something better please suggest.
9. Using all-miniLM-l6-v2 as vector embedding currently but planning to use stella_en_4
00M_v5.
10. Using cosine similarity to retrieve the documents.
11. Using BLEU, F1 and BERT score for automated evaluatio
n based on golden answer.
12. Using top_k as 3.
13. Currently using basic question answering prompt but want to improve 
it. Any tips? Also heard about Automatic Prompt Evaluation.
14. Currently using custom code for everything. Looking to u
se Llamaindex or Langchain for this. 
15. Right now I am not using any AI Agent, but I want to know your opinions. 
16. 
It's a simple RAG framework and I am working on improving it.
17. I haven't included reranker but I am planning to do so
 too.

I think I mentioned pretty much everything I am using for my project. So please share your suggestions, comments 
and reviews for the same. Thank you!!
```
---

     
 
MachineLearning -  [ [P] Lessons from Retrieval Augmented Generation ](https://www.reddit.com/r/MachineLearning/comments/1f9tvg7/p_lessons_from_retrieval_augmented_generation/) , 2024-09-27-0913
```
I implemented Rag in my organization and just wrote a blog about what we learned here:   
[https://www.b-yond.com/post/t
ransforming-telco-troubleshooting-our-journey-building-telcogpt-with-rag](https://www.b-yond.com/post/transforming-telco
-troubleshooting-our-journey-building-telcogpt-with-rag)

Hoping it would be helpful for those in this area. Covers rag 
evaluation (ragas), sql db, langchain agents vs chains, weaviate vector db, hybrid search, reranking, and more.

Some ad
ditional insights on ranking and hybrid search here:

[https://www.linkedin.com/posts/drzohaib\_transforming-telco-troub
leshooting-our-journey-activity-7232072089837486081--Le1?utm\_source=share&utm\_medium=member\_android](https://www.link
edin.com/posts/drzohaib_transforming-telco-troubleshooting-our-journey-activity-7232072089837486081--Le1?utm_source=shar
e&utm_medium=member_android)
```
---

     
 
deeplearning -  [ What is the best approach for Parsing and Retrieving Code Context Across Multiple Files in a Hierarc ](https://www.reddit.com/r/deeplearning/comments/1fh58oz/what_is_the_best_approach_for_parsing_and/) , 2024-09-27-0913
```
I want to implement a Code-RAG system on a code directory where I need to:

* Parse and load all the files from folders 
and subfolders while excluding specific file extensions.
* Embed and store the parsed content into a vector store.
* Ret
rieve relevant information based on user queries.

However, I’m facing two major challenges:

**File Parsing and Loading
:** What’s the most efficient method to parse and load files in a hierarchical manner (reflecting their folder structure
)? Should I use Langchain’s directory loader, or is there a better way? I came across the Tree-sitter tool in Claude-dev
’s repo, which is used to build syntax trees for source files—would this be useful for hierarchical parsing?

**Cross-Fi
le Context Retrieval:** If the relevant context for a user’s query is spread across multiple files located in different 
subfolders, how can I fine-tune my retrieval system to identify the correct context across these files? Would reranking 
resolve this, or is there a better approach?

**Query Translation:** Do I need to use Something like Multi-Query or RAG-
Fusion to achieve better retrieval for hierarchical data?

\[I want to understand how tools like [continue.dev](http://c
ontinue.dev/) and [claude-dev](https://github.com/saoudrizwan/claude-dev) work\]
```
---

     
 
deeplearning -  [ Month of August in AI ](https://www.reddit.com/r/deeplearning/comments/1f6zfz0/month_of_august_in_ai/) , 2024-09-27-0913
```
🔍 I**nside this Issue:**

* 🤖 La*test Breakthroughs: *This month it’s all about A*gents, LangChain RAG, and LLMs evaluat
ion challenges.*
* 🌐 AI Monthly News: Discover how these stories are revolutionizing industries and impacting everyday l
ife: E*U AI Act, California’s Controversial SB1047 AI regulation act, Drama at OpenAI, and possible funding at OpenAI by
 Nvidia and Apple.*
* 📚 Editor’s Special: This covers the interesting talks, lectures, and articles we came across recen
tly.

Follow me on Twitter and LinkedIn at [**RealAIGuys**](https://twitter.com/RealAIGuys) and [**AIGuysEditor**](https
://www.linkedin.com/in/vishal-rajput-999164122/) to get insight on new AI developments.

>**Please don't forget to subsc
ribe to our Newsletter:** [**https://medium.com/aiguys/newsletter**](https://medium.com/aiguys/newsletter)

# Latest Bre
akthroughs

Are Agents just simple rules? Are Agents just enhanced reasoning? The answer is yes and no. Yes, in the sens
e that agents have simple rules and can sometimes enhance reasoning capabilities compared to a single prompt. But No in 
the sense that agents can have a much more diverse functionality like using specific tools, summarizing, or even followi
ng a particular style. In this blog, we look into how to set up these agents in a hierarchal manner just like running a 
small team of Authors, researchers, and supervisors.

[**How To Build Hierarchical Multi-Agent Systems?**](https://mediu
m.com/aiguys/how-to-build-hierarchical-multi-agent-systems-dc26b19201d2?sk=90958e39e1a28f5030872a90f8e3f3da)

**TextGrad
**. It is a powerful framework performing automatic “differentiation” via text. **It backpropagates textual feedback pro
vided by LLMs to improve individual components of a compound AI system.** In this framework, LLMs provide rich, general,
 natural language suggestions to optimize variables in computation graphs, ranging from code snippets to molecular struc
tures. TextGrad showed effectiveness and generality across various applications, from question-answering and molecule op
timization to radiotherapy treatment planning.

[**TextGrad: Improving Prompting Using AutoGrad**](https://medium.com/ai
guys/textgrad-controlling-llm-behavior-via-text-2a82e2073d10?sk=3633a9aa63b884c97469bce659265921)

The addition of RAG t
o LLMs was an excellent idea. It helped the LLMs to become more specific and individualized. Adding new components to an
y system leads to more interactions and its own sets of problems. Adding RAG to LLMs leads to several problems such as h
ow to retrieve the best content, what type of prompt to write, and many more.

In this blog, we are going to combine the
 **LangChain RAG with DSPy**. We deep dive into how to evaluate the RAG pipeline quantitatively using **RAGAs** and how 
to create a system where instead of manually tweaking prompts, we let the system figure out the best prompt.

[**How To 
Build LangChain RAG With DSPy?**](https://medium.com/aiguys/how-to-build-langchain-rag-with-dspy-ce9154fbafaa?sk=b41d104
05f84c767cf9cd6a58d1ebac0)

As the field of natural language processing (NLP) advances, the evaluation of large language
 models (LLMs) like GPT-4 becomes increasingly important and complex. Traditional metrics such as accuracy are often ina
dequate for assessing these models’ performance because they fail to capture the nuances of human language. In this arti
cle, we will explore why evaluating LLMs is challenging and discuss effective methods like BLEU and ROUGE for a more com
prehensive evaluation.

[**The Challenges of Evaluating Large Language Models**](https://medium.com/aiguys/the-challenge
s-of-evaluating-large-language-models-ec2eb834a349)

# AI Monthly News

# AI Act enters into force

On 1 August 2024, th
e European Artificial Intelligence Act (AI Act) enters into force. The Act aims to foster responsible artificial intelli
gence development and deployment in the EU. The AI Act introduces a uniform framework across all EU countries, based on 
a forward-looking definition of AI and a risk-based approach:

* **Minimal risk:** most AI systems such as spam filters 
and AI-enabled video games face no obligation under the AI Act, but companies can voluntarily adopt additional codes of 
conduct.
* **Specific transparency risk:** systems like chatbots must clearly inform users that they are interacting wit
h a machine, while certain AI-generated content must be labelled as such.
* **High risk:** high-risk AI systems such as 
AI-based medical software or AI systems used for recruitment must comply with strict requirements, including risk-mitiga
tion systems, high-quality of data sets, clear user information, human oversight, etc.
* **Unacceptable risk:** for exam
ple, AI systems that allow “social scoring” by governments or companies are considered a clear threat to people’s fundam
ental rights and are therefore banned.

**EU announcement:** [**Click here**](https://commission.europa.eu/news/ai-act-e
nters-force-2024-08-01_en)

https://preview.redd.it/nwyzfzgm4cmd1.png?width=828&format=png&auto=webp&s=c873db37ca0dadd5b
510bea70ac9f633b96aaea4

# California AI bill SB-1047 sparks fierce debate, Senator likens it to ‘Jets vs. Sharks’ feud


**Key Aspects of SB-1047:**

* Regulation Scope: Targets “frontier” AI models, defined by their immense computational t
raining requirements (over 10²⁶ operations) or significant financial investment (>$100 million).
* Compliance Requiremen
ts: Developers must implement safety protocols, including the ability to immediately shut down, cybersecurity measures, 
and risk assessments, before model deployment.
* Whistleblower Protections: Encourages reporting of non-compliance or ri
sks by offering protection against retaliation.
* Safety Incident Reporting: Mandates reporting AI safety incidents with
in 72 hours to a newly established Frontier Model Division.
* Certification: Developers need to certify compliance, pote
ntially under penalty of perjury in earlier drafts, though amendments might have altered this.

**Pros:**

* Safety Firs
t: Prioritizes the prevention of catastrophic harms by enforcing rigorous safety standards, potentially safeguarding aga
inst AI misuse or malfunction.
* Incentivizes Responsible Development: By setting high standards for AI model training, 
the company encourages developers to think critically about the implications of their creations.
* Public Trust: Enhance
s public confidence in AI by ensuring transparency and accountability in the development process.

**Cons:**

* Innovati
on Stagnation: Critics argue it might stifle innovation, especially in open-source AI, due to the high costs and regulat
ory burdens of compliance.
* Ambiguity: Some definitions and requirements might be too specific or broad, leading to leg
al challenges or unintended consequences.
* Global Competitiveness: There’s concern that such regulations could push AI 
development outside California or the U.S., benefiting other nations without similar restrictions.
* Implementation Chal
lenges: The practicalities of enforcing such regulations, especially the “positive safety determination,” could be compl
ex and contentious.

**News Article:** [**Click here**](https://www.thenation.com/article/society/sb-1047-ai-big-tech-fi
ght/)

**Open Letter:** [**Click here**](https://safesecureai.org/open-letter)

https://preview.redd.it/ib96d7nk4cmd1.pn
g?width=828&format=png&auto=webp&s=0ed5913b5dae72e203c8592393e469d9130ed689

# MORE OpenAI drama

OpenAI co-founder John
 Schulman has left the company to join rival AI startup Anthropic, while OpenAI president and co-founder Greg Brockman i
s taking an extended leave until the end of the year. Schulman, who played a key role in creating the AI-powered chatbot
 platform ChatGPT and led OpenAI’s alignment science efforts, stated his move was driven by a desire to focus more on AI
 alignment and hands-on technical work. Peter Deng, a product manager who joined OpenAI last year, has also left the com
pany. With these departures, only three of OpenAI’s original 11 founders remain: CEO Sam Altman, Brockman, and Wojciech 
Zaremba, lead of language and code generation.

**News Article:** [**Click here**](https://techcrunch.com/2024/08/05/ope
nai-co-founder-leaves-for-anthropic/)

https://preview.redd.it/0vdjc18j4cmd1.png?width=828&format=png&auto=webp&s=e9de60
4c26aed3e47b50df3bdf114ef61f967080

# Apple and Nvidia may invest in OpenAI

Apple, which is planning to integrate ChatG
PT into iOS, is in talks to invest. Soon after, [*Bloomberg* also](https://www.bloomberg.com/news/articles/2024-08-29/nv
idia-has-held-discussions-about-joining-openai-s-funding-round?srnd=homepage-americas) reported that Apple is in talks b
ut added that Nvidia “has discussed” joining the funding round as well. The round is reportedly being led by Thrive Capi
tal and would value OpenAI at more than $100 billion.

**News Article:** [**Click here**](https://www.theverge.com/2024/
8/29/24231626/apple-nvidia-openai-invest-microsoft)

https://preview.redd.it/ude6jguh4cmd1.png?width=828&format=png&auto
=webp&s=3603cbca0dbb1be3e6d0efcf06c3a698428bbdd6

# Editor’s Special

* The AI Bubble: Will It Burst, and What Comes Aft
er?: [**Click here**](https://www.youtube.com/watch?v=91SK90SahHc&t=317s)
* Eric Schmidt Full Controversial Interview on
 AI Revolution (Former Google CEO): [**Click here**](https://www.youtube.com/watch?v=mKVFNg3DEng)
* AI isn’t gonna keep 
improving [**Click here**](https://www.youtube.com/watch?v=Y8Ym7hMR100)
* General Intelligence: Define it, measure it, b
uild it: [**Click here**](https://www.youtube.com/watch?v=nL9jEy99Nh0)
```
---

     
