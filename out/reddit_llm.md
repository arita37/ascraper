 
all -  [ Semantic document search ](https://www.reddit.com/r/LangChain/comments/16nvy5b/semantic_document_search/) , 2023-09-21-0909
```
Suggest me some resources for semantic document search

It's not searching semantically in a document but searching a do
cument from a group of documents.
```
---

     
 
all -  [ How to manage ReAct agent prompt size as iterations increase? ](https://www.reddit.com/r/LangChain/comments/16nuytk/how_to_manage_react_agent_prompt_size_as/) , 2023-09-21-0909
```
As the number of iterations increase for an agent, the prompt for the LLM planning step quickly becomes larger and large
r until it exceeds the prompt limit. What strategies are y'all using to manage the prompt size during the planning phase
? This has been especially a problem when the output of a tool is sizable. 
```
---

     
 
all -  [ Zep's New Web UI: Easily Manage Your LLM App's Users, Memory, and Vector Indexes ](https://www.reddit.com/r/LangChain/comments/16nufn5/zeps_new_web_ui_easily_manage_your_llm_apps_users/) , 2023-09-21-0909
```
Hey all, Zep now has a Web UI! 🔥🎉  You can manage users, memories, vector indexes, and more via Zep’s web admin interfac
e.

**What's Zep?** 

With Zep, you can take your LLM app prototype to production in minutes with fast, scalable buildin
g blocks for memory, search, and enrichment. No recoding required as Zep’s components are drop-in replacements for exist
ing LangChain or LlamaIndex classes.  


🎥 A quick demo of Zep in action: [https://vimeo.com/865785086?share=copy](https
://vimeo.com/865785086?share=copy)  
🏠 Zep website: [https://www.getzep.com/](https://www.getzep.com/)  
⭐️ Zep on GitHu
b [https://github.com/getzep/zep](https://github.com/getzep/zep)

&#x200B;

https://preview.redd.it/kpcrt8t6rgpb1.png?wi
dth=2184&format=png&auto=webp&s=69c4b1693e2a0556c90f482ee269b48f626cff99
```
---

     
 
all -  [ Urgent question: uploading docs to llama ](https://www.reddit.com/r/LocalLLaMA/comments/16ns4hk/urgent_question_uploading_docs_to_llama/) , 2023-09-21-0909
```
So I wanna know if I build a chat bot with llama2, is there a feature that would allow users to upload their local docum
ents onto the platform and help them with queries related to that ?

I saw langchain approach where you cut the file int
o smaller chunks and then use vector db. But is that something which can be done with an actual product used in a large 
company?
```
---

     
 
all -  [ ChatGPT from the command line ](https://www.reddit.com/r/LangChain/comments/16nqr8i/chatgpt_from_the_command_line/) , 2023-09-21-0909
```
Hello!

I was looking for a tool to use ChatGPT from the terminal (which is where I spend most of my computer time). Mos
t of the stuff I found seems a bit overengineered, so I decided to build my own :)  


It took me just a couple of hours
, and despite being only 60 lines of code, it does all I need:

&#x200B;

* interact with ChatGPT with a chat-like exper
ience
* remember conversations using memory
* store conversations locally
* load and continue conversations
* set the te
mperature of the model
* limit the memory depth to save tokens and contain costs

Here is the code: [https://github.com/
francescocarlucci/chatgpt-cli](https://github.com/francescocarlucci/chatgpt-cli)

Any constructive feedback is very welc
ome, and feel free to fork and extend for your use case :)

Cheers,

Francesco
```
---

     
 
all -  [ How to decide when call a tool or not ](https://www.reddit.com/r/LangChain/comments/16ni6us/how_to_decide_when_call_a_tool_or_not/) , 2023-09-21-0909
```
Hi all, someone knows how can i set if i want to call one tool or no, my specific case is as following: I want to ask by
 default to chatgpt but if chatgpt is not able to answer because the question involve context posterior to 2021 I want t
o call the Serpapi tool to search in internet for the information, I do not want to call the tool every time because it 
would have extra cost. I'm not able to find any tutorial or documentation that show how to achieve this.  
Thanks in adv
ance for the help.
```
---

     
 
all -  [ Is it just me or is Langchain is too complicated to understand and work with? ](https://www.reddit.com/r/datascience/comments/16ni0h7/is_it_just_me_or_is_langchain_is_too_complicated/) , 2023-09-21-0909
```
Hi all,

&#x200B;

 **Is it just me or is Langchain too complicated to work with?** 

I'm not exactly riding on the LLM 
wave but I'm trying to learn langchain to build LLM applications. My company wants to know how to use GenAI and LLMs in 
their use cases.

Langchain has been a big pain in my butt so far. With its confusing documentation and countless nested
 imports, I'm not sure if this is the best framework to experiment with LLM applications. I find the abstractions very h
ard to understand, as compared to say, scikit-learn.

Measure theory is more manageable than langchain, IMO. Am I too st
upid to understand langchain or is it really one big complicated mess? If there are better alternatives, please suggest 
them in the comments.
```
---

     
 
all -  [ group by or unique in search result using similaritySearch ](https://www.reddit.com/r/Supabase/comments/16ng8hs/group_by_or_unique_in_search_result_using/) , 2023-09-21-0909
```
 i embed text documents and chose supabase as my vector store. documents can have multiple embeddings. but i want to gro
up it with only one result per document.  also if there is a way to paginate this result  i use langchain, supabase pgve
ctor and supabase gte-small hugging face 
```
---

     
 
all -  [ FineTuning vs LangChain .. or a Mix ? ](https://www.reddit.com/r/LocalLLaMA/comments/16nfwhx/finetuning_vs_langchain_or_a_mix/) , 2023-09-21-0909
```
Hey everyone ,

excuse me if I sound like a noob in these topics . but recently I discovered the world of huggingface an
d local LLMs . I work at a company that provides software services to a lot of clients , and one of our products is supp
osed to be a chatbot that aids the customers by guiding them or answering any question about that client . in addition t
o that , each customer has some personal data in the client's database , let's say stuff like name , date joined , activ
ity .. and other analytics regarding his membership with that specific client . which all of them can be easily retrieve
d by using our companies API requests that returns user info in a json format .

I came across this post [https://www.re
ddit.com/r/LocalLLaMA/comments/14vnfh2/my\_experience\_on\_starting\_with\_fine\_tuning\_llms/](https://www.reddit.com/r
/LocalLLaMA/comments/14vnfh2/my_experience_on_starting_with_fine_tuning_llms/)that further made me realize that fine-tun
ing a model on that client's specific data might be a good idea .

collect data , structure it like (preferably in  #ins
truction,#input,#output format as I saw this is good format based on alpaca-cleaned data-set) , and fine-tune one of the
 hugging face models on it . that way , any question about that client , the model would be able to answer it in a speci
fic way rather than a generic way like a generic LLM would do .

ok great , let's say we fine-tuned the model on that cl
ient's data , and now it can answer any question about that client for the user like any FAQ , any info about the client
 , how to register , how to cancel etc...  but it got me thinking , how would I also train the model to be able to answe
r queries where the user asks about some specific info about himself and not just some generic info question about the c
lient ? , imagine if the client is a gym , how can I train the model to be also able to answer a question similar to 'wh
en does my membership end ?' . should I provide also in the training data examples for these types of questions with som
e fake data about a fake user ? or is there no need to train the model on these types of questions and just do it using 
LangChain by specifying type of chains that get user info as input and a query from the user , while also providing some
 examples in the prompt to further help the LLM understand how the questions is supposed to be answered ?but also , how 
would I do that in Langchain for a lot of different types of queries ? should I just think of a lot of possible queries 
from that user that asks for specific user info ?

or is there a dynamic way in langchain to firstly get the query , fig
ure out what sort of info needed to answer the question , use one of our API calls to retrieve the info , and then answe
r using that Info ?

sorry if I rambled some nonsense , I would be happy for some advice from you guys
```
---

     
 
all -  [ dialoqbase – open source chatbot creation platform ](https://www.reddit.com/r/ChatGPT/comments/16nerpm/dialoqbase_open_source_chatbot_creation_platform/) , 2023-09-21-0909
```
I have been working on a side project for the last 3 months, built around LangchainJS and pgvector. It now supports *Cha
tGPT*, *Llama*, *Claude*, and *Bison* models, and the bot can integrate with WhatsApp, Telegram, and Discord for now. I 
would really appreciate some feedback. Thanks!

repo: [https://github.com/n4ze3m/dialoqbase](https://github.com/n4ze3m/d
ialoqbase)
```
---

     
 
all -  [ [P] vLLM, Langchain, Embedchain ? ](https://www.reddit.com/r/MachineLearning/comments/16ndyxc/p_vllm_langchain_embedchain/) , 2023-09-21-0909
```
Which libraries do you think would be the most important to learn between these, and to use in my next personal project 
? This will be a conversational chatbot trained on podcast transcripts
```
---

     
 
all -  [ History is troublesome. Answers with knowledge of subject but not with context information. ](https://www.reddit.com/r/LangChain/comments/16n6qsv/history_is_troublesome_answers_with_knowledge_of/) , 2023-09-21-0909
```
So here is my problem. I use the  ConversationalRetrievalQAChain and provide those history messages: 

      const pastM
essages = [
        new SystemMessage('Always provide helpful information. Sometimes you can infer it from previous mess
ages. You always know an answer.'),
        new HumanMessage('Who is he?'),
        new AIMessage('Barack Obama is an Am
erican politician who served as the 44th President of the United States. He was born on August 4, 1961, in Honolulu, Haw
aii. Barack Obama is a member of the Democratic Party and made history by becoming the first African American president 
of the United States.'),
      ];

When I then ask e.g. ' Please make the text shorter' it always answers with ' I'm sor
ry, but I don't have any information on Barack Obama in the provided context. ' or something similar. The same when I wa
nt to know the age or something. It is really weird. GPT-4 appears to always know the subject of the past messages but n
ot the rest of the content.   


Does anyone know how to fix this?
```
---

     
 
all -  [ Using language models to create a robotic ecosystem ](https://www.reddit.com/r/computervision/comments/16n5s0g/using_language_models_to_create_a_robotic/) , 2023-09-21-0909
```
Hello everyone,

Me and my friends at RoboCoach Inc (a san diego based startup) recently created this open source projec
t to use GPT and Langchain to capture the details of a robotic design through human language interface, and to automatic
ally create the ROS (Robot Operating System) packages:

[https://github.com/RoboCoachTechnologies/ROScribe](https://gith
ub.com/RoboCoachTechnologies/ROScribe)

Demo: [https://www.youtube.com/watch?v=H2QaeelkReU](https://www.youtube.com/watc
h?v=H2QaeelkReU) 

Please check it out and let me know what you think. It works for ROS1 for now, but we will add ROS2 v
ery soon. We plan to add a lot of features into this software, so stay tuned for future releases.

We appreciate if you 
drop us a star on our repo, if you download the code, run it, and file issues, and if you contribute to this robotic pro
ject. We plan to make a robotic ecosystem based on LLMs and ROS. This is just the first step toward that goal.

I hope t
his tool helps your next robotics project.

&#x200B;
```
---

     
 
all -  [ How to leverage user feedback into my LLM application? ](https://www.reddit.com/r/LangChain/comments/16n4fug/how_to_leverage_user_feedback_into_my_llm/) , 2023-09-21-0909
```
As a context, we have a multiuser chatbot based on LangChain + OpenAI, it does RAG with conversational memory. 

The use
r can rate every response of the LLM with 👍👎buttons.

Concersations are stores as is feedback. So we know the questions 
and answers that where down voted. 

Right now we are not leveraging that anyhow.

I'm looking for inspiration on how to
 leverage the user feedback.

Do you guys have implemented such user feedback thing and how do you use it?
(of course i 
could review it manually, or fo reporting on it... And later make decisions base on the reports/analytics.)

 I'm more l
ooking for ways to get the LLM (or LLM based application) to use that information to give better answer or not give agai
n the same answer if it was down voted...
```
---

     
 
all -  [ Why is langchain not using 'messages' from OpenAI's chat completion endpoint? ](https://www.reddit.com/r/LangChain/comments/16n3eka/why_is_langchain_not_using_messages_from_openais/) , 2023-09-21-0909
```
I was exploring the prompts in Langchain's agents and the calls to OpenAI's endpoints, and I found it doesn't use the ['
messages' param when calling ChatCompletion](https://platform.openai.com/docs/api-reference/chat/streaming), but instead
 puts everything in the prompt such as:

    Instruction.
    
    Chat History:
    {conversation between Human and Ass
istant}
    
    New question:
    {new message}
    
    Assistant:

Why is this? I can think of some advantages, such 
as:

1. Conceptually, it makes more sense as an LLM receives a string to predict a string
2. It is LLM agnostic
3. It al
lows you to have more control of what's going on
4. It makes everything more transparent

But, am I missing something?
```
---

     
 
all -  [ Build an AI Personal Marathon Trainer with SendGrid and LangChain Agents ](https://www.twilio.com/blog/ai-personal-marathon-trainer-agents-sendgrid) , 2023-09-21-0909
```

```
---

     
 
all -  [ Enhancement idea and feedback ](https://www.reddit.com/r/LangChain/comments/16n1njd/enhancement_idea_and_feedback/) , 2023-09-21-0909
```
We have developed a unified AI-driven platform that lets you engage with all your favorite businesses right from a singl
e WhatsApp chat. No need to give away you contact number or sift through spammy messages. Llms are integrated to make in
teractions more personalized and context-rich. The platform also features 'Consolidated Communications,' where we bundle
 similar offers or messages from various providers into one easy-to-digest update. For businesses, we offer valuable ana
lytics and targeted marketing opportunities. How do you think Langchain could fit into enhancing this experience? We're 
eager to hear your input!
```
---

     
 
all -  [ How to approach using langchain to train OpenAI with Network Traffic Logs ](https://www.reddit.com/r/LangChain/comments/16n05w1/how_to_approach_using_langchain_to_train_openai/) , 2023-09-21-0909
```
Hello! I am currently doing an independent study at my university on using OpenAI's API to help in areas like data analy
tics and cybersecurity. My professor gave me a massive dataset of about 1,500,000 lines of network traffic logs to use i
n training for OpenAI to be able to detect a cyberattack. I will paste some example lines below. Does anyone have some i
nsight in how I can use langchain in this project? To be honest I am not even sure where to start, but I think I'd like 
to start with an example only using like 1000 lines with 70% training and 30% test. Any help and insight is GREATLY appr
eciated!

0,tcp,private,S0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,292,8,1.00,1.00,0.00,0.00,0.03,0.06,0.00,255,8,0.03,0.06,
0.00,0.00,1.00,1.00,0.00,0.00,neptune.  0,tcp,private,S0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,293,9,1.00,1.00,0.00,0.00,0
.03,0.06,0.00,255,9,0.04,0.06,0.00,0.00,1.00,1.00,0.00,0.00,neptune.  0,tcp,private,S0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
,0,294,4,1.00,1.00,0.00,0.00,0.01,0.06,0.00,255,4,0.02,0.06,0.00,0.00,1.00,1.00,0.00,0.00,neptune.  0,icmp,eco\_i,SF,8,0
,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,44,0.00,0.00,0.00,0.00,1.00,0.00,1.00,1,255,1.00,0.00,1.00,0.50,0.00,0.00,0.00,0.00,i
psweep.  0,icmp,eco\_i,SF,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,43,0.00,0.00,0.00,0.00,1.00,0.00,1.00,2,255,1.00,0.00,1.
00,0.50,0.00,0.00,0.00,0.00,ipsweep.  1,tcp,smtp,SF,1466,330,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,1,0.00,0.00,0.00,0.00,1.0
0,0.00,0.00,1,1,1.00,0.00,1.00,0.00,0.00,0.00,0.00,0.00,normal.  1,tcp,smtp,SF,1646,328,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,
1,2,0.00,0.00,0.00,0.00,1.00,0.00,1.00,72,53,0.74,0.04,0.01,0.00,0.00,0.00,0.00,0.00,normal. 1154,tcp,telnet,SF,360,1078
36,0,0,1,0,0,1,9,0,0,1,0,0,0,0,0,0,1,1,0.00,0.00,0.00,0.00,1.00,0.00,0.00,73,1,0.01,0.05,0.01,0.00,0.00,0.00,0.00,0.00,n
ormal.
```
---

     
 
all -  [ Semantic text splitting using LLMs ](https://www.reddit.com/r/LangChain/comments/16mz4e7/semantic_text_splitting_using_llms/) , 2023-09-21-0909
```
Hey,   


At Neum AI, we have been playing around with several iterations of doing semantic text splitting using LLMs. T
oday, we released an open-source package with our latest for people to try out. At a high level, these capabilities enab
le you to provide a sample piece of text and let the tool come up with a strategy to split that text. That strategy gets
 converted to code which you can then leverage across a document set. We have found this to be especially useful when we
 have large number of documents that follow patterns / templates, as well as when we have customers give us one offs tha
t are hard to split using more traditional methods. 

The tool is by no means perfect, but at least gives a good idea of
 the right direction to take when chunking the document. You can try out the tools either on our playground or directly 
using our python module. Links to both below:  


Learn more: [Contextually splitting documents (neum.ai)](https://www.n
eum.ai/post/contextually-splitting-documents) 

Playground: [Streamlit (neumai-playground.streamlit.app)](https://neumai
-playground.streamlit.app/) 

Module: [neumai-tools · PyPI](https://pypi.org/project/neumai-tools/) 
```
---

     
 
all -  [ Fundamental Q on Langchain from a newbie ](https://www.reddit.com/r/LangChain/comments/16my8sa/fundamental_q_on_langchain_from_a_newbie/) , 2023-09-21-0909
```
Hey, I'm just getting started with langchains and I have a fundamental question. 

How does a person who wants to build 
a langchain know whether or not the information they plan on building a langchain with is already in the LLM they want t
o connect with? 

Consequently, how does one know their efforts won't be a waste of time and energy being redundant?
```
---

     
 
all -  [ [INSTANT DOWLOAD] Peter – Buildfast Masterclass – Learn to build your own AI chatbot ](https://www.reddit.com/r/DailyNewsEco/comments/16mv0ch/instant_dowload_peter_buildfast_masterclass_learn/) , 2023-09-21-0909
```
**Download this course here:** [**Peter – Buildfast Masterclass – Learn to build your own AI chatbot**](https://shoppy.g
g/product/gTTVpAo)

[**Sale Page**](https://buildfast.academy/) 

**Here are all of the videos inside Fundamentals**  
*
*That you get instant access to upon joining BuildFast**

1. **LLMs: Overview, using LLMs in Langchain, open-sourced LLM
s, chat model, embedding text.**
2. **Chains: Chains 101, LLM Chain, Sequential Chain, and four other important Langchai
n chains.**
3. **Prompt: Prompts 101, Example Prompts, Output Parser.**
4. **Memory: 4 Memory Types Explained, How to us
e Memory in a Chain, How to add Memory to an Agent**
5. **Document Loaders: Document Loaders 101, When to use Document L
oader, Import data from Text & CSV, and Loading data from Discord, Notion, Telegram**
6. **Indexes: Indexes 101, Retriev
ers and Text Splitters.**
7. **Vector Database & Embeddings: Vector databases 101, when to use vector databases, Embeddi
ngs and vector database use-cases.**
```
---

     
 
all -  [ [Hiring] Multiple Roles: Engineering Manager, Sr. Frontend & Backend Eng, ML Engineer | VC Backed AI ](https://www.reddit.com/r/forhire/comments/16mu75b/hiring_multiple_roles_engineering_manager_sr/) , 2023-09-21-0909
```
**Location**: Remote/Boston/Boulder  
**Salary**: 💲$100k-$200k/year  


**The Company**

Our VC backed AI company just f
inished raising seed and we're looking for top tier engineers to lead our engineering department. 

We're revolutionizin
g the full business development process for government contracting, from finding opportunities to analysis & AI-assisted
 proposal writing. We have partnerships with some of the top training companies in the field and we have some of the top
 100 contractors as our early clients. 

We are recovering from some bad early technical decisions and that is why we ne
ed top engineers to right the ship. There will be generous equity & a serious potential for lucrative outcome for all.


**Tech**

* We use a combination of typescript, python, ruby & go. 
* Postgres, Redis, Qdrant
* OpenAI/Langchain/Langsmi
th
* Google cloud, Kubernetes, we will need to develop a fully-portable kube cluster for onsite deployment as well.

**R
oles**

We are hiring multiple roles:

* **Engineering Manage**r - Build/Lead an app development team of 5-10 fullstack 
engineers, coordinating product development between fullstack & AI initiatives. 
* **Sr. Frontend Engineer** \- Lead the
 charge on a next-gen UI/UX for AI writing.  Create Editor.JS plugins, design new features, implement best practices inc
luding stores/caching for maintainability. You should have experience building SaaS startups & implementing/maintaining 
styleguides from the ground up. We will not be spoon-feeding you figmas, but high level requirements (: 
* **Sr. Backend
/Fullstack Engineer** \- For those whose specialties lie in data retrieval/storage. Implement queueing architectures, rp
c, build scalable backend / business logic. You should know when to use redis, postgres, a data warehouse, nosql, queues
, microservices (and when *not* to use them), etc. You will be handling tons of API integrations, auth, data ingestion p
ipelines etc. as well as things like web crawlers, file storage etc.
* **ML Engineer** \- You'll be taking over our pyth
on langchain microservice. You should keep up with the latest LLM developments and have a solid background in ML fundame
ntals. You should know information retrieval, online models, context-augmented chat methodologies, and be able to extrac
t useful information from user interactions. We have 10+ different use cases/fun ML problems to work on for our core pro
duct. We need someone who is focused on implementation and rapid prototyping rather than a research oriented approach - 
prototype, gather data & iterate. 
```
---

     
 
all -  [ Example for re-ranking in RAG? ](https://www.reddit.com/r/LangChain/comments/16ms4m4/example_for_reranking_in_rag/) , 2023-09-21-0909
```
I am looking to learn more about how to implement reranking in a RAG implementation. Any tutorials/articles recommended 
by the community?
```
---

     
 
all -  [ Need some pointers for RAG, chunks retrieved don't seem very relevant. ](https://www.reddit.com/r/LocalLLaMA/comments/16mq8kx/need_some_pointers_for_rag_chunks_retrieved_dont/) , 2023-09-21-0909
```
Hi all,

Apologies for another question on RAG, I know there's a few topics on this already but still feeling a bit lost
 and need some clarity on where I should focus my attention on learning. Still very new to this so everything is quite f
resh and daunting.

I'm trying to essentially do Q&A over local files such as earnings call transcripts or meeting notes
 taken in markdown. I've managed to cobble together something that generates an answer but the hit rate is spotty at bes
t. For example I can query this thing asking who the CEO of a division is (person is introduced in page 1) and it will t
ell me it doesn't know, but then I ask it what the capital expenditure was and it gives me the right answer which leaves
 me scratching my head.

Some more detail on what I did;

* I use the 13b Vicuna 1.5 loaded into Ooba and exposed throug
h the API
* Using LangChain to load the file and then embedding it using bge\_large
* Chunk size is 500 with overlap of 
100 and then store it into Chroma
* Use RetrievalQA, chaintype 'stuff', and k:5
* Use the instruct, input, response prom
pt template with context with customary don't make up answer.

Looking at the chunks retrieved it feels like its giving 
me really random chunks. I saw another person use things such as reranking which looks promising however just given how 
poorly this is performing on some very simple questions ('Who is X?') and telling me X is not mentioned in the given tex
t despite being introduced in the 1st page - I am wondering if I'm doing something wrong more fundamentally.
```
---

     
 
all -  [ Evaluating Extraction Tasks: Best Practices? ](https://www.reddit.com/r/LangChain/comments/16mm8de/evaluating_extraction_tasks_best_practices/) , 2023-09-21-0909
```
I'm developing an application utilizing langchain & llms, primarily for extracting specific structured data from vast te
xt sources. Typically, this results in 20-30 extracted points per instance.

I aim to ensure the system comprehensively 
captures the intended points. What's the best approach to evaluate its performance and fine-tune the prompts, allowing f
or efficient model comparisons?

While I've looked into application-level llm evaluation ([**source**](https://wandb.ai/
ayush-thakur/llm-eval-sweep/reports/How-to-Evaluate-Compare-and-Optimize-LLM-Systems--Vmlldzo0NzgyMTQz)), most methods a
re tailored to different use cases like Question Answering or Math problems.

Here are my initial thoughts:

* **Multipl
e Extractions**: Repeatedly run the extraction process and measure the overlap of facts.
* **Human Annotation**: Ideal b
ut time-consuming.
* **LLM Self-Evaluation**: Input the extraction's input-output to GPT4-32k for a reflection on its pe
rformance.

Before I commit considerable resources to these, are there any industry standards or overlooked methods I sh
ould be aware of?
```
---

     
 
all -  [ How does Retrieval Augmented Generation (RAG) actually work? ](https://www.reddit.com/r/MLQuestions/comments/16mkd84/how_does_retrieval_augmented_generation_rag/) , 2023-09-21-0909
```
Naively, I am familiar with how frameworks like Langchain lets you 'chain' together a series of steps (using both prompt
s and external APIs), s.t. an LLM can answer a question with more accuracy and timeliness.

Sample Steps:

1. Search a v
ector db with your question/embedding

2. 'Map reduce' or summarize the multiple results into concise answers

3. Respon
d with the final answer or say I dont know

Is there a more sophisticated approach to RAG? What are some other ways to a
chieve RAG outside of the Langchain approach (which is quite.. finicky at times)
```
---

     
 
all -  [ Is there a way to add instructions as Embeddings? ](https://www.reddit.com/r/OpenAI/comments/16mk0um/is_there_a_way_to_add_instructions_as_embeddings/) , 2023-09-21-0909
```
I created a PoC app following one of the [blogs](https://medium.com/@Stan_DS/reading-multiple-pdfs-and-identifying-sourc
es-using-langchain-chromedb-and-openai-api-4e5a5ca47c42#id_token=eyJhbGciOiJSUzI1NiIsImtpZCI6IjdjMGI2OTEzZmUxMzgyMGEzMzM
zOTlhY2U0MjZlNzA1MzVhOWEwYmYiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL2FjY291bnRzLmdvb2dsZS5jb20iLCJhenAiOiIyMTYyOTYwMzU4
MzQtazFrNnFlMDYwczJ0cDJhMmphbTRsamRjbXMwMHN0dGcuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCJhdWQiOiIyMTYyOTYwMzU4MzQtazFrNnFl
MDYwczJ0cDJhMmphbTRsamRjbXMwMHN0dGcuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCJzdWIiOiIxMTI3OTQ0ODU4NDI5ODU5ODU4NDIiLCJoZCI6
InF1ZXN0dC5jb20iLCJlbWFpbCI6Im1vaHNpbkBxdWVzdHQuY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsIm5iZiI6MTY5NTEwNjM2MSwibmFtZSI6Ik1v
aHNpbiBNIiwicGljdHVyZSI6Imh0dHBzOi8vbGgzLmdvb2dsZXVzZXJjb250ZW50LmNvbS9hL0FDZzhvY0o1cFFpVmt0N0RDUnRwTmpzOENyUmQ1RU5pTjNV
cVY3N0I3U2xldjQtaD1zOTYtYyIsImdpdmVuX25hbWUiOiJNb2hzaW4iLCJmYW1pbHlfbmFtZSI6Ik0iLCJsb2NhbGUiOiJlbiIsImlhdCI6MTY5NTEwNjY2
MSwiZXhwIjoxNjk1MTEwMjYxLCJqdGkiOiJkOWZlNDE5ODYwYmExYjk5ODQ5YjczOGFmMGMwZTM5YzU5NTcyM2JjIn0.dLunNNrFo8prfsWP1uIznJKLPAvs
TVSw5wIVwZlbZRkWUuqdXtNp1uKLf4R1TN5NEWvg1lLSroykROT3BUqm0PQ7185lRxABoaeLulA9CZYKF1mK9bIKJzKf6nI1Z3KyS_58wlN1NcqUfwC4AG_7
yU3ZwDhoRhJKMbmY6SPYoB736MbPhJ0uCpQxB2P5y5UsT0l0rP6d234dTlmKhJ0CeC11R73VtME-CNQR7PqJfosGHivmVRIG0U39je6jKSknY_C56JfE5J9o
yuAI46mtE4A2WrEpKdc-3c0QqlOdVm6o1JXKQUkNhY30wgkBBa0y-VCTEbd4KdzzVii7EVMlWA) for an app that takes in multiple PDFs and a
nswers questions from the PDF content. It does so by:

1. Splitting the documents into chunks.
2. Creating embeddings fo
r each document.
3. Storing the documents and embeddings in a Vectorstore.

So far, the PoC seems to work and does what 
I intended it to do. Now, I need to give instructions to OpenAI to answer questions from the PDF by following a certain 
set of rules. I have added these instructions as part of the System prompt. However, the scope of my entire instruction 
set is also a full length PDF document. Is it possible to add instructions as embeddings as well?
```
---

     
 
all -  [ Good RAG implementation ](https://www.reddit.com/r/LangChain/comments/16m9cem/good_rag_implementation/) , 2023-09-21-0909
```
Hi there, I am new with LLMs and I'm working on a personal project. I am looking for a good RAG implementation (with LLM
 support) that does not take forever to run to be able to retrieve information over multiple time periods, over a large 
number of files and where the text can be longer than a chunk. Anyone got a good idea of an architecture or a good repos
itory to start from ?
```
---

     
 
all -  [ How to Optimize Text Chunking for Improved Embedding Vectorization? ](https://www.reddit.com/r/LangChain/comments/16m73j4/how_to_optimize_text_chunking_for_improved/) , 2023-09-21-0909
```
 I'm currently using Langchain to split my texts into chunks, but I believe it may not always yield the most optimal vec
tors. My source material consists of lengthy articles, which often contain contextual information distributed across the
 entire article. When I break these articles into smaller chunks, I run the risk of losing important contextual informat
ion.

Does anyone have any suggestions on how to enhance this process? I've been contemplating the idea of introducing a
 pre-vectorization step where I could transform all the articles into a 'question and answer' format through an OpenAI r
equest. However, I'm concerned that this approach might be costly, or perhaps there are more effective alternatives avai
lable. Any insights would be greatly appreciated.
```
---

     
 
all -  [ Which one is the best embedding for Langchain ReAct agents? ](https://www.reddit.com/r/LangChain/comments/16m37g7/which_one_is_the_best_embedding_for_langchain/) , 2023-09-21-0909
```
Working on a prototype and am not sure which one to choose. 

Free is best. Any open source alternatives?
```
---

     
 
all -  [ Not being able to use HuggingFaceEmbedding from Langchain ](https://www.reddit.com/r/LangChain/comments/16m1nee/not_being_able_to_use_huggingfaceembedding_from/) , 2023-09-21-0909
```
Hi, everyone! I'm quite new to LangChain and LLM's, and I'm currently trying to use LangChain + LLama 2 to extract infor
mation from PDF documents. My attempts with LLamaCcp weren't very successful, so I'm now giving a try with HuggingFace's
 embeddings and pipeline, but I can't figure out why I can't get past this one error.  I do have a working pipeline work
ing with langchain + huggingface, so I can edit the tokenizer in this case, but I have no idea what can I do now with th
e embedding model. Any help and/or tips are welcome! =)

My embedding model's instantiation works normally, the error is
 thrown at the attempt of embedding documents

&#x200B;

`hf = HuggingFaceBgeEmbeddings(`

`model_name=model_name,`

`mo
del_kwargs=model_kwargs,`

`encode_kwargs=encode_kwargs`

`)`

&#x200B;

`Please update jupyter and ipywidgets. See` [`h
ttps://ipywidgets.readthedocs.io/en/stable/user_install.html`](https://ipywidgets.readthedocs.io/en/stable/user_install.
html) `from .autonotebook import tqdm as notebook_tqdm`

`No sentence-transformers model found with name ../llama-2-7b-h
f. Creating a new one with MEAN pooling.`

`Loading checkpoint shards: 100%|██████████| 2/2 [00:02<00:00, 1.49s/it]`

&#
x200B;

`embeddings = hf.embed_documents(['This is a test document.'])`

&#x200B;

`ValueError: Asking to pad but the to
kenizer does not have a padding token. Please select a token to use as \`pad\_token (tokenizer.pad\_token = tokenizer.eo
s\_token e.g.) or add a new pad token via tokenizer.add\_special\_tokens({'pad\_token': '\[PAD\]'})\`.\`

&#x200B;
```
---

     
 
all -  [ GenAI controller is quite limited, any thoughts on SN platform for broader GenAI orchestration? ](https://www.reddit.com/r/servicenow/comments/16lv5ej/genai_controller_is_quite_limited_any_thoughts_on/) , 2023-09-21-0909
```
SN GenAI Controller is just an API to OpenAI models.  Has anyone tried to use ServiceNow for GenAI orchestration, may be
 with  LangChain or other frameworks? 

For example combine CMDB, Workslows with LLM orchestration tools like prompt des
ign, conversation memory, embedded company data (txt, ppt, slack), API's to multiple LLMs and tools (eg calendar), verif
ication, logging, etc
```
---

     
 
all -  [ Do people not use sci-kit learn / other traditional libraries anymore? ](https://www.reddit.com/r/datascience/comments/16lu9ni/do_people_not_use_scikit_learn_other_traditional/) , 2023-09-21-0909
```
Recently saw a tweet which got quite some traction talking about how many people haven't used sci-kit learn in months as
 data scientists.

This has been replaced with PyTorch, HuggingFace, langchain, supergradients etc.

This didn't really 
make sense to me as the tooling mentioned isn't really comparable to sci-kit learn but I'm curious and slightly worried 
I might be falling behind and not up to date with things so just asking if I'm just behind the curve or what you guys th
ink/ do.
```
---

     
 
all -  [ What python packages are you using for your local builds? ](https://www.reddit.com/r/LocalLLaMA/comments/16ltbhs/what_python_packages_are_you_using_for_your_local/) , 2023-09-21-0909
```
Just wondering what packages ya’ll are using with your different local builds? 

One of my builds uses langchain and fai
ss to read local docs and create an embedding database, then feed the results from similarity search into my llm prompt


Another built just using open-interpreter with a local llama model

What packages have you come across that work good f
or local llm builds? Everything I’m building must be completely offline without using any API keys since I’m building fo
r my work so I’m curious how others work around that

Running on an M1 max with 32GB memory right now, in the process of
 upgrading to an M2 128GB

Thanks!
```
---

     
 
all -  [ + 100 Free Courses for Monday, September 18, 2023 ](https://www.reddit.com/r/udemyfreeebies/comments/16lt21x/100_free_courses_for_monday_september_18_2023/) , 2023-09-21-0909
```
**Courses for 18 September 2023**  
 

Note : Coupons might expire anytime, so enroll as soon as possible to get the cou
rses for FREE.

* DBMS Module – 5[REDEEM OFFER](https://idownloadcoupon.com/udemy/3643/)
* Contact Center Manager Profes
sional Certification[REDEEM OFFER](https://idownloadcoupon.com/udemy/3642/)
* Facebook Ads: Run Your First Ad Campaign[R
EDEEM OFFER](https://idownloadcoupon.com/udemy/3641/)
* Master LangChain with No-Code tools: Flowise and LangFlow[REDEEM
 OFFER](https://idownloadcoupon.com/udemy/3640/)
* LEVEL 1 MODULE: BECOME A WEALTH MAGNET FOR LIFE: PART 4 OF 5[REDEEM O
FFER](https://idownloadcoupon.com/udemy/3639/)
* Search Engine Optimization (SEO) For Beginners Practise Test[REDEEM OFF
ER](https://idownloadcoupon.com/udemy/3638/)
* Content Marketing For Intermediate Practise Test 2023[REDEEM OFFER](https
://idownloadcoupon.com/udemy/3637/)
* Boost Digital Marketing Effectiveness via Behavioral Science[REDEEM OFFER](https:/
/idownloadcoupon.com/udemy/3636/)
* Python Development Essentials[REDEEM OFFER](https://idownloadcoupon.com/udemy/3635/)

* Leadership & Team Building Mastery[REDEEM OFFER](https://idownloadcoupon.com/udemy/3634/)
* Adobe Photoshop Projects[
REDEEM OFFER](https://idownloadcoupon.com/udemy/3633/)
* Pubslic Speaking Trainer: Enter the Presentation Training Biz[R
EDEEM OFFER](https://idownloadcoupon.com/udemy/3631/)
* Storytelling: You Can learn to Tell Stories Effectively[REDEEM O
FFER](https://idownloadcoupon.com/udemy/3630/)
* Public Speaking for People Who Hate Public Speaking[REDEEM OFFER](https
://idownloadcoupon.com/udemy/3629/)
* Podcasting: How to Speak Effectively on Your Own Podcast[REDEEM OFFER](https://ido
wnloadcoupon.com/udemy/3628/)
* Presentation Skills: Give Great Skype Video Presentations[REDEEM OFFER](https://idownloa
dcoupon.com/udemy/3627/)
* Conference Calls-You Can Present Well On Any Conference Call[REDEEM OFFER](https://idownloadc
oupon.com/udemy/3624/)
* Media Training for Print/Online Interviews-Get Great Quotes[REDEEM OFFER](https://idownloadcoup
on.com/udemy/3623/)
* Speaking on the Telephone: Confidently Speak on the Phone[REDEEM OFFER](https://idownloadcoupon.co
m/udemy/3622/)
* Interviewing Skills: Conducting Job Interviews[REDEEM OFFER](https://idownloadcoupon.com/udemy/3621/)
*
 Marketing Strategy: Communicating Your Message[REDEEM OFFER](https://idownloadcoupon.com/udemy/3620/)
* Personal Presen
tation Training[REDEEM OFFER](https://idownloadcoupon.com/udemy/3619/)
* Public Speaking Emergency! Ace the Speech With 
Little Prep[REDEEM OFFER](https://idownloadcoupon.com/udemy/3618/)
* Emergency Media Training: You Can Face a Reporter I
n 2 Hours[REDEEM OFFER](https://idownloadcoupon.com/udemy/3617/)
* Media Training for Beginners: Ace Your First News Int
erviews[REDEEM OFFER](https://idownloadcoupon.com/udemy/3616/)
* Recon For Bug Bounty, Penetration Testers & Ethical Hac
kers[REDEEM OFFER](https://idownloadcoupon.com/udemy/3615/)
* Python – Data Analytics – Real World Hands-on Projects[RED
EEM OFFER](https://idownloadcoupon.com/udemy/3614/)
* QuickBooks Online vs. Excel 2023[REDEEM OFFER](https://idownloadco
upon.com/udemy/3613/)
* QuickBooks Desktop vs. Excel[REDEEM OFFER](https://idownloadcoupon.com/udemy/3612/)
* QuickBooks
 Online vs. QuickBooks Desktop vs. Excel[REDEEM OFFER](https://idownloadcoupon.com/udemy/3611/)
* Two QuickBooks File-Bu
siness & Personal vs One File For Both[REDEEM OFFER](https://idownloadcoupon.com/udemy/3610/)
* QuicksBooks Pro-Business
 & Personal-One QuickBooks File[REDEEM OFFER](https://idownloadcoupon.com/udemy/3609/)
* QuickBooks Online vs Xero Accou
nting Software[REDEEM OFFER](https://idownloadcoupon.com/udemy/3608/)
* QuickBooks Desktop vs QBO Multiple Currencies[RE
DEEM OFFER](https://idownloadcoupon.com/udemy/3607/)
* Fast track French for beginners[REDEEM OFFER](https://idownloadco
upon.com/udemy/3606/)
* Sales management – streams, frameworks and processes[REDEEM OFFER](https://idownloadcoupon.com/u
demy/3605/)
* Corporate Finance #15 Dividend Policy[REDEEM OFFER](https://idownloadcoupon.com/udemy/3604/)
* Corporate F
inance #16 Convertible Bonds & Warrants[REDEEM OFFER](https://idownloadcoupon.com/udemy/3603/)
* Corp. Finance #14 Finan
cing-Commons Stock & Preferred Stock[REDEEM OFFER](https://idownloadcoupon.com/udemy/3602/)
* Proceso CRUD (C Sharp y Mi
crosoft SQL Server)[REDEEM OFFER](https://idownloadcoupon.com/udemy/3601/)
* SQL Bootcamp – SQLite – Hands-On Exercises[
REDEEM OFFER](https://idownloadcoupon.com/udemy/3600/)
* AWS Certified Data Analytics Specialty DAS-C01 – Mock Exams[RED
EEM OFFER](https://idownloadcoupon.com/udemy/3599/)
* SQL Developer Certification: Test Your Skills with Tests[REDEEM OF
FER](https://idownloadcoupon.com/udemy/3598/)
* Google Professional Cloud Security Engineer – Practice Exams[REDEEM OFFE
R](https://idownloadcoupon.com/udemy/3597/)
* Recursion and Backtracking Algorithms in Java[REDEEM OFFER](https://idownl
oadcoupon.com/udemy/3596/)
* Python for Intermediate Learners (2023)[REDEEM OFFER](https://idownloadcoupon.com/udemy/359
5/)
* Mastering HTML5: From Beginner to Advanced[REDEEM OFFER](https://idownloadcoupon.com/udemy/3594/)
* Graph Theory A
lgorithms in Java[REDEEM OFFER](https://idownloadcoupon.com/udemy/3593/)
* Dynamic Programming Algorithms for Coding Int
erviews[REDEEM OFFER](https://idownloadcoupon.com/udemy/3592/)
* Curso de Base de Datos SQLite[REDEEM OFFER](https://ido
wnloadcoupon.com/udemy/3591/)
* Curso de Java – Nivel Básico[REDEEM OFFER](https://idownloadcoupon.com/udemy/3590/)
* Rú
bricas para la evaluación de desempeño de los aprendizajes[REDEEM OFFER](https://idownloadcoupon.com/udemy/3589/)
* Curs
o de Base de Datos Oracle Database[REDEEM OFFER](https://idownloadcoupon.com/udemy/3588/)
* Curso de Base de Datos Fireb
ird[REDEEM OFFER](https://idownloadcoupon.com/udemy/3587/)
* Desarrollando Sistema de Ventas (C# y MySQL Server)[REDEEM 
OFFER](https://idownloadcoupon.com/udemy/3586/)
* Job Cost QuickBooks Online vs QuickBooks Desktop–Contractor[REDEEM OFF
ER](https://idownloadcoupon.com/udemy/3585/)
* Corp Finance #12 Capital Budgeting & Investment Risk Tools[REDEEM OFFER](
https://idownloadcoupon.com/udemy/3584/)
* Corporate Finance #13 Investment Banking & Long-Term Debt[REDEEM OFFER](https
://idownloadcoupon.com/udemy/3583/)
* LeetCode in Java: Algorithms Coding Interview Questions[REDEEM OFFER](https://idow
nloadcoupon.com/udemy/3582/)
* The Complete C Programming Course for Beginners[REDEEM OFFER](https://idownloadcoupon.com
/udemy/3581/)
* Bank Feeds-QuickBooks Online, Xero, Sage, Wave (Comparison)[REDEEM OFFER](https://idownloadcoupon.com/ud
emy/3580/)
* Corp Finance #10 Cost of Capital–Debt & Equity Financing[REDEEM OFFER](https://idownloadcoupon.com/udemy/35
79/)
* Corporate Finance #9 Valuation-Bond, Common /Preferred Stock[REDEEM OFFER](https://idownloadcoupon.com/udemy/3578
/)
* The Complete Data Structures and Algorithms Course in Java[REDEEM OFFER](https://idownloadcoupon.com/udemy/3577/)
*
 Corporate Finance #8 Time Value of Money (PV & FV)[REDEEM OFFER](https://idownloadcoupon.com/udemy/3576/)
* Corporate F
inance #7 Short Term Financing[REDEEM OFFER](https://idownloadcoupon.com/udemy/3575/)
* Corporate Finance #4 Leverage & 
Break-Even Analysis[REDEEM OFFER](https://idownloadcoupon.com/udemy/3574/)
* Corporate Finance #5 Financing Decisions[RE
DEEM OFFER](https://idownloadcoupon.com/udemy/3573/)
* Corporate Finance #6 Management of Current Assets[REDEEM OFFER](h
ttps://idownloadcoupon.com/udemy/3572/)
* Corporate Finance #1 Introduction & Financial Statements[REDEEM OFFER](https:/
/idownloadcoupon.com/udemy/3571/)
* Corporate Finance #3 Forecasting & Budgeting[REDEEM OFFER](https://idownloadcoupon.c
om/udemy/3570/)
* Corporate Finance #2 Financial Ratios[REDEEM OFFER](https://idownloadcoupon.com/udemy/3569/)
* Automat
ed Machine Learning for Beginners (Google & Apple)[REDEEM OFFER](https://idownloadcoupon.com/udemy/3568/)
* Partnership 
Accounting – Financial Accounting[REDEEM OFFER](https://idownloadcoupon.com/udemy/3567/)
* Financial Accounting – Closin
g Process[REDEEM OFFER](https://idownloadcoupon.com/udemy/3566/)
* Bank Reconciliations & Cash Internal Controls[REDEEM 
OFFER](https://idownloadcoupon.com/udemy/3565/)
* Financial Accounting – Closing Process[REDEEM OFFER](https://idownload
coupon.com/udemy/3564/)
* Financial Accounting – Subsidiary Ledgers & Special Journals[REDEEM OFFER](https://idownloadco
upon.com/udemy/3563/)
* Financial Accounting–Inventory & Merchandising Transactions[REDEEM OFFER](https://idownloadcoupo
n.com/udemy/3562/)
* Financial Accounting – Inventory Costs[REDEEM OFFER](https://idownloadcoupon.com/udemy/3561/)
* Tim
e Value of Money & Capital Budgeting – Present Value[REDEEM OFFER](https://idownloadcoupon.com/udemy/3560/)
* Financial 
Accounting-Adjusting Entries & Financial Statement[REDEEM OFFER](https://idownloadcoupon.com/udemy/3559/)
* Financial Ac
counting-Debits & Credits-Accounting Transaction[REDEEM OFFER](https://idownloadcoupon.com/udemy/3558/)
* Receivables & 
The Allowance vs The Direct Write Off Methods[REDEEM OFFER](https://idownloadcoupon.com/udemy/3557/)
* Accounting for Co
rporations – Financial Accounting[REDEEM OFFER](https://idownloadcoupon.com/udemy/3556/)
* Accounting-Statement of Cash 
Flows[REDEEM OFFER](https://idownloadcoupon.com/udemy/3555/)
* Job Order Costing System – Managerial Accounting[REDEEM O
FFER](https://idownloadcoupon.com/udemy/3554/)
* Advanced Microsoft Word With Job Success[REDEEM OFFER](https://idownloa
dcoupon.com/udemy/3553/)
* Financial Accounting-Depreciation Calculation & Fixed Assets[REDEEM OFFER](https://idownloadc
oupon.com/udemy/3552/)
* Payroll Calculations Training for Financial Accounting[REDEEM OFFER](https://idownloadcoupon.co
m/udemy/3551/)
* Process Costing System-Cost Accounting-Managerial Accounting[REDEEM OFFER](https://idownloadcoupon.com/
udemy/3550/)
* Responsibility Accounting & Performance Measurement[REDEEM OFFER](https://idownloadcoupon.com/udemy/3549/
)
* Complete PYTHON Programming for Beginners – 2023[REDEEM OFFER](https://idownloadcoupon.com/udemy/3548/)
* Relevant C
osts – Managerial Accounting Decisions & Scenarios[REDEEM OFFER](https://idownloadcoupon.com/udemy/3547/)
* Master Budge
ts – Managerial Accounting/Cost Accounting[REDEEM OFFER](https://idownloadcoupon.com/udemy/3546/)
* C++ Assessment Toolk
it: Diverse Practice Tests for All Level[REDEEM OFFER](https://idownloadcoupon.com/udemy/3545/)
* Practice Tests: Crack 
the Python PCEP Certification Exam[REDEEM OFFER](https://idownloadcoupon.com/udemy/3544/)
* Ace the Python Challenge: 60
 Realistic Practice Questions[REDEEM OFFER](https://idownloadcoupon.com/udemy/3543/)
* C++ Practice Intensives: Sharpen 
Skills with 4 Rigorous Test[REDEEM OFFER](https://idownloadcoupon.com/udemy/3542/)
* Wondershare Filmora 11 Video Editin
g Course in Hindi[REDEEM OFFER](https://idownloadcoupon.com/udemy/3541/)
* Excellence in Interpersonal Skills (People & 
Social Skills)[REDEEM OFFER](https://idownloadcoupon.com/udemy/3540/)
* iOS 16 Swift & SwiftUI – Complete iOS App Develo
pment[REDEEM OFFER](https://idownloadcoupon.com/udemy/3539/)
* Python for Intermediate Learners (2023)[REDEEM OFFER](htt
ps://idownloadcoupon.com/udemy/3538/)
* Consumer behavior, Consumer Intention & Consumer Attitude[REDEEM OFFER](https://
idownloadcoupon.com/udemy/3537/)
* Excel – Formulas & Functions Beginner to Expert Course 2023[REDEEM OFFER](https://ido
wnloadcoupon.com/udemy/3536/)
* Excellence in Problem Solving Skills & Strategies[REDEEM OFFER](https://idownloadcoupon.
com/udemy/3535/)
* Rank Your Blog Website in Google: SEO For Beginners 2023[REDEEM OFFER](https://idownloadcoupon.com/ud
emy/3534/)
* Python Complete Course For Python Beginners[REDEEM OFFER](https://idownloadcoupon.com/udemy/3533/)
* Javasc
ript Build a Calculator using HTML, CSS and Javascript[REDEEM OFFER](https://idownloadcoupon.com/udemy/3532/)
* 23.8″ Мо
нитор Philips 243V7QDAB, 1920×1080, 75 Гц, IPS[REDEEM OFFER](https://idownloadcoupon.com/udemy/3531/)
* Python & Django 
REST API Bootcamp – Build A Python Web API[REDEEM OFFER](https://idownloadcoupon.com/udemy/3530/)
* Flutter REST Movie A
pp: Master Flutter REST API Development[REDEEM OFFER](https://idownloadcoupon.com/udemy/3529/)
* Flutter UI Bootcamp | B
uild Beautiful Apps using Flutter[REDEEM OFFER](https://idownloadcoupon.com/udemy/3528/)
* Build A Chat Application With
 Firebase, Flutter and Provider[REDEEM OFFER](https://idownloadcoupon.com/udemy/3527/)
* C++ Mastery through 4 Logical P
ractice Tests[REDEEM OFFER](https://idownloadcoupon.com/udemy/3526/)
* C++ Challenge: 4 Intensive Practice Exams[REDEEM 
OFFER](https://idownloadcoupon.com/udemy/3525/)
* Python Practice Exams: Elevate Your Programming Skills[REDEEM OFFER](h
ttps://idownloadcoupon.com/udemy/3524/)
* Master Python Web Scraping & Automation using BS4 & Selenium[REDEEM OFFER](htt
ps://idownloadcoupon.com/udemy/3523/)
* Python Quest: 60 Challenging Question to Enhance Your Skill[REDEEM OFFER](https:
//idownloadcoupon.com/udemy/3522/)
* Sharpen Your C++ Skills with 4 Challenging Practice Tests[REDEEM OFFER](https://ido
wnloadcoupon.com/udemy/3521/)
* CSS, Bootstrap ,JavaScript, Web Development Course[REDEEM OFFER](https://idownloadcoupon
.com/udemy/3520/)
* Continuous Improvement[REDEEM OFFER](https://idownloadcoupon.com/udemy/3519/)
* Business Improvement
 Plan[REDEEM OFFER](https://idownloadcoupon.com/udemy/3518/)
* Process Mapping: Toolkit[REDEEM OFFER](https://idownloadc
oupon.com/udemy/3517/)
* Learn Japanese For Beginners With Natsuko[REDEEM OFFER](https://idownloadcoupon.com/udemy/3516/
)
* Deep Learning MasterClass[REDEEM OFFER](https://idownloadcoupon.com/udemy/3515/)
* Root Cause Analysis: Fishbone Dia
gram[REDEEM OFFER](https://idownloadcoupon.com/udemy/3514/)
* Lean Six Sigma Yellow Belt: Certification[REDEEM OFFER](ht
tps://idownloadcoupon.com/udemy/3513/)
* Lean Six Sigma Yellow Belt: Certification[REDEEM OFFER](https://idownloadcoupon
.com/udemy/3513/)
* FMEA: Failure, Modes, Effects, Analysis[REDEEM OFFER](https://idownloadcoupon.com/udemy/3512/)
* Org
anizational Culture Change[REDEEM OFFER](https://idownloadcoupon.com/udemy/3511/)
* Lean Management: Course & certificat
ion[REDEEM OFFER](https://idownloadcoupon.com/udemy/3510/)
* Root Cause Analysis: Drill Down Tool[REDEEM OFFER](https://
idownloadcoupon.com/udemy/3509/)
* SIPOC – Supplier, Input, Process, Output, Customer[REDEEM OFFER](https://idownloadcou
pon.com/udemy/3508/)
* Mastery of IT Project Management[REDEEM OFFER](https://idownloadcoupon.com/udemy/3507/)
* The Web
site Blueprint – Planning for a web design project[REDEEM OFFER](https://idownloadcoupon.com/udemy/3506/)
* Mastering th
e Art of Leadership[REDEEM OFFER](https://idownloadcoupon.com/udemy/3505/)
* How to Draw Hair Better Than Anyone Else[RE
DEEM OFFER](https://idownloadcoupon.com/udemy/3504/)
* Options Trading for Beginners – Intro Session[REDEEM OFFER](https
://idownloadcoupon.com/udemy/3503/)
* Building Rapport: Confident Conversations Without Small Talk[REDEEM OFFER](https:/
/idownloadcoupon.com/udemy/3502/)
* FFmpeg | Batch Modify Thousands of Videos Quickly and Easily[REDEEM OFFER](https://i
downloadcoupon.com/udemy/3501/)
* Introduction to the language of criminal law[REDEEM OFFER](https://idownloadcoupon.com
/udemy/3500/)
* 5 Calendar Trades – Detailed Walk through[REDEEM OFFER](https://idownloadcoupon.com/udemy/3499/)
* Finan
cial Statements for Beginners in 1 Hour or Less[REDEEM OFFER](https://idownloadcoupon.com/udemy/3498/)
```
---

     
 
all -  [ + 100 Free Courses for Monday, September 18, 2023 ](https://www.reddit.com/r/udemyfreebies/comments/16lt1zs/100_free_courses_for_monday_september_18_2023/) , 2023-09-21-0909
```
**Courses for 18 September 2023**

Note : Coupons might expire anytime, so enroll as soon as possible to get the courses
 for FREE.

* DBMS Module – 5[REDEEM OFFER](https://idownloadcoupon.com/udemy/3643/)
* Contact Center Manager Profession
al Certification[REDEEM OFFER](https://idownloadcoupon.com/udemy/3642/)
* Facebook Ads: Run Your First Ad Campaign[REDEE
M OFFER](https://idownloadcoupon.com/udemy/3641/)
* Master LangChain with No-Code tools: Flowise and LangFlow[REDEEM OFF
ER](https://idownloadcoupon.com/udemy/3640/)
* LEVEL 1 MODULE: BECOME A WEALTH MAGNET FOR LIFE: PART 4 OF 5[REDEEM OFFER
](https://idownloadcoupon.com/udemy/3639/)
* Search Engine Optimization (SEO) For Beginners Practise Test[REDEEM OFFER](
https://idownloadcoupon.com/udemy/3638/)
* Content Marketing For Intermediate Practise Test 2023[REDEEM OFFER](https://i
downloadcoupon.com/udemy/3637/)
* Boost Digital Marketing Effectiveness via Behavioral Science[REDEEM OFFER](https://ido
wnloadcoupon.com/udemy/3636/)
* Python Development Essentials[REDEEM OFFER](https://idownloadcoupon.com/udemy/3635/)
* L
eadership & Team Building Mastery[REDEEM OFFER](https://idownloadcoupon.com/udemy/3634/)
* Adobe Photoshop Projects[REDE
EM OFFER](https://idownloadcoupon.com/udemy/3633/)
* Pubslic Speaking Trainer: Enter the Presentation Training Biz[REDEE
M OFFER](https://idownloadcoupon.com/udemy/3631/)
* Storytelling: You Can learn to Tell Stories Effectively[REDEEM OFFER
](https://idownloadcoupon.com/udemy/3630/)
* Public Speaking for People Who Hate Public Speaking[REDEEM OFFER](https://i
downloadcoupon.com/udemy/3629/)
* Podcasting: How to Speak Effectively on Your Own Podcast[REDEEM OFFER](https://idownlo
adcoupon.com/udemy/3628/)
* Presentation Skills: Give Great Skype Video Presentations[REDEEM OFFER](https://idownloadcou
pon.com/udemy/3627/)
* Conference Calls-You Can Present Well On Any Conference Call[REDEEM OFFER](https://idownloadcoupo
n.com/udemy/3624/)
* Media Training for Print/Online Interviews-Get Great Quotes[REDEEM OFFER](https://idownloadcoupon.c
om/udemy/3623/)
* Speaking on the Telephone: Confidently Speak on the Phone[REDEEM OFFER](https://idownloadcoupon.com/ud
emy/3622/)
* Interviewing Skills: Conducting Job Interviews[REDEEM OFFER](https://idownloadcoupon.com/udemy/3621/)
* Mar
keting Strategy: Communicating Your Message[REDEEM OFFER](https://idownloadcoupon.com/udemy/3620/)
* Personal Presentati
on Training[REDEEM OFFER](https://idownloadcoupon.com/udemy/3619/)
* Public Speaking Emergency! Ace the Speech With Litt
le Prep[REDEEM OFFER](https://idownloadcoupon.com/udemy/3618/)
* Emergency Media Training: You Can Face a Reporter In 2 
Hours[REDEEM OFFER](https://idownloadcoupon.com/udemy/3617/)
* Media Training for Beginners: Ace Your First News Intervi
ews[REDEEM OFFER](https://idownloadcoupon.com/udemy/3616/)
* Recon For Bug Bounty, Penetration Testers & Ethical Hackers
[REDEEM OFFER](https://idownloadcoupon.com/udemy/3615/)
* Python – Data Analytics – Real World Hands-on Projects[REDEEM 
OFFER](https://idownloadcoupon.com/udemy/3614/)
* QuickBooks Online vs. Excel 2023[REDEEM OFFER](https://idownloadcoupon
.com/udemy/3613/)
* QuickBooks Desktop vs. Excel[REDEEM OFFER](https://idownloadcoupon.com/udemy/3612/)
* QuickBooks Onl
ine vs. QuickBooks Desktop vs. Excel[REDEEM OFFER](https://idownloadcoupon.com/udemy/3611/)
* Two QuickBooks File-Busine
ss & Personal vs One File For Both[REDEEM OFFER](https://idownloadcoupon.com/udemy/3610/)
* QuicksBooks Pro-Business & P
ersonal-One QuickBooks File[REDEEM OFFER](https://idownloadcoupon.com/udemy/3609/)
* QuickBooks Online vs Xero Accountin
g Software[REDEEM OFFER](https://idownloadcoupon.com/udemy/3608/)
* QuickBooks Desktop vs QBO Multiple Currencies[REDEEM
 OFFER](https://idownloadcoupon.com/udemy/3607/)
* Fast track French for beginners[REDEEM OFFER](https://idownloadcoupon
.com/udemy/3606/)
* Sales management – streams, frameworks and processes[REDEEM OFFER](https://idownloadcoupon.com/udemy
/3605/)
* Corporate Finance #15 Dividend Policy[REDEEM OFFER](https://idownloadcoupon.com/udemy/3604/)
* Corporate Finan
ce #16 Convertible Bonds & Warrants[REDEEM OFFER](https://idownloadcoupon.com/udemy/3603/)
* Corp. Finance #14 Financing
-Commons Stock & Preferred Stock[REDEEM OFFER](https://idownloadcoupon.com/udemy/3602/)
* Proceso CRUD (C Sharp y Micros
oft SQL Server)[REDEEM OFFER](https://idownloadcoupon.com/udemy/3601/)
* SQL Bootcamp – SQLite – Hands-On Exercises[REDE
EM OFFER](https://idownloadcoupon.com/udemy/3600/)
* AWS Certified Data Analytics Specialty DAS-C01 – Mock Exams[REDEEM 
OFFER](https://idownloadcoupon.com/udemy/3599/)
* SQL Developer Certification: Test Your Skills with Tests[REDEEM OFFER]
(https://idownloadcoupon.com/udemy/3598/)
* Google Professional Cloud Security Engineer – Practice Exams[REDEEM OFFER](h
ttps://idownloadcoupon.com/udemy/3597/)
* Recursion and Backtracking Algorithms in Java[REDEEM OFFER](https://idownloadc
oupon.com/udemy/3596/)
* Python for Intermediate Learners (2023)[REDEEM OFFER](https://idownloadcoupon.com/udemy/3595/)

* Mastering HTML5: From Beginner to Advanced[REDEEM OFFER](https://idownloadcoupon.com/udemy/3594/)
* Graph Theory Algor
ithms in Java[REDEEM OFFER](https://idownloadcoupon.com/udemy/3593/)
* Dynamic Programming Algorithms for Coding Intervi
ews[REDEEM OFFER](https://idownloadcoupon.com/udemy/3592/)
* Curso de Base de Datos SQLite[REDEEM OFFER](https://idownlo
adcoupon.com/udemy/3591/)
* Curso de Java – Nivel Básico[REDEEM OFFER](https://idownloadcoupon.com/udemy/3590/)
* Rúbric
as para la evaluación de desempeño de los aprendizajes[REDEEM OFFER](https://idownloadcoupon.com/udemy/3589/)
* Curso de
 Base de Datos Oracle Database[REDEEM OFFER](https://idownloadcoupon.com/udemy/3588/)
* Curso de Base de Datos Firebird[
REDEEM OFFER](https://idownloadcoupon.com/udemy/3587/)
* Desarrollando Sistema de Ventas (C# y MySQL Server)[REDEEM OFFE
R](https://idownloadcoupon.com/udemy/3586/)
* Job Cost QuickBooks Online vs QuickBooks Desktop–Contractor[REDEEM OFFER](
https://idownloadcoupon.com/udemy/3585/)
* Corp Finance #12 Capital Budgeting & Investment Risk Tools[REDEEM OFFER](http
s://idownloadcoupon.com/udemy/3584/)
* Corporate Finance #13 Investment Banking & Long-Term Debt[REDEEM OFFER](https://i
downloadcoupon.com/udemy/3583/)
* LeetCode in Java: Algorithms Coding Interview Questions[REDEEM OFFER](https://idownloa
dcoupon.com/udemy/3582/)
* The Complete C Programming Course for Beginners[REDEEM OFFER](https://idownloadcoupon.com/ude
my/3581/)
* Bank Feeds-QuickBooks Online, Xero, Sage, Wave (Comparison)[REDEEM OFFER](https://idownloadcoupon.com/udemy/
3580/)
* Corp Finance #10 Cost of Capital–Debt & Equity Financing[REDEEM OFFER](https://idownloadcoupon.com/udemy/3579/)

* Corporate Finance #9 Valuation-Bond, Common /Preferred Stock[REDEEM OFFER](https://idownloadcoupon.com/udemy/3578/)
*
 The Complete Data Structures and Algorithms Course in Java[REDEEM OFFER](https://idownloadcoupon.com/udemy/3577/)
* Cor
porate Finance #8 Time Value of Money (PV & FV)[REDEEM OFFER](https://idownloadcoupon.com/udemy/3576/)
* Corporate Finan
ce #7 Short Term Financing[REDEEM OFFER](https://idownloadcoupon.com/udemy/3575/)
* Corporate Finance #4 Leverage & Brea
k-Even Analysis[REDEEM OFFER](https://idownloadcoupon.com/udemy/3574/)
* Corporate Finance #5 Financing Decisions[REDEEM
 OFFER](https://idownloadcoupon.com/udemy/3573/)
* Corporate Finance #6 Management of Current Assets[REDEEM OFFER](https
://idownloadcoupon.com/udemy/3572/)
* Corporate Finance #1 Introduction & Financial Statements[REDEEM OFFER](https://ido
wnloadcoupon.com/udemy/3571/)
* Corporate Finance #3 Forecasting & Budgeting[REDEEM OFFER](https://idownloadcoupon.com/u
demy/3570/)
* Corporate Finance #2 Financial Ratios[REDEEM OFFER](https://idownloadcoupon.com/udemy/3569/)
* Automated M
achine Learning for Beginners (Google & Apple)[REDEEM OFFER](https://idownloadcoupon.com/udemy/3568/)
* Partnership Acco
unting – Financial Accounting[REDEEM OFFER](https://idownloadcoupon.com/udemy/3567/)
* Financial Accounting – Closing Pr
ocess[REDEEM OFFER](https://idownloadcoupon.com/udemy/3566/)
* Bank Reconciliations & Cash Internal Controls[REDEEM OFFE
R](https://idownloadcoupon.com/udemy/3565/)
* Financial Accounting – Closing Process[REDEEM OFFER](https://idownloadcoup
on.com/udemy/3564/)
* Financial Accounting – Subsidiary Ledgers & Special Journals[REDEEM OFFER](https://idownloadcoupon
.com/udemy/3563/)
* Financial Accounting–Inventory & Merchandising Transactions[REDEEM OFFER](https://idownloadcoupon.co
m/udemy/3562/)
* Financial Accounting – Inventory Costs[REDEEM OFFER](https://idownloadcoupon.com/udemy/3561/)
* Time Va
lue of Money & Capital Budgeting – Present Value[REDEEM OFFER](https://idownloadcoupon.com/udemy/3560/)
* Financial Acco
unting-Adjusting Entries & Financial Statement[REDEEM OFFER](https://idownloadcoupon.com/udemy/3559/)
* Financial Accoun
ting-Debits & Credits-Accounting Transaction[REDEEM OFFER](https://idownloadcoupon.com/udemy/3558/)
* Receivables & The 
Allowance vs The Direct Write Off Methods[REDEEM OFFER](https://idownloadcoupon.com/udemy/3557/)
* Accounting for Corpor
ations – Financial Accounting[REDEEM OFFER](https://idownloadcoupon.com/udemy/3556/)
* Accounting-Statement of Cash Flow
s[REDEEM OFFER](https://idownloadcoupon.com/udemy/3555/)
* Job Order Costing System – Managerial Accounting[REDEEM OFFER
](https://idownloadcoupon.com/udemy/3554/)
* Advanced Microsoft Word With Job Success[REDEEM OFFER](https://idownloadcou
pon.com/udemy/3553/)
* Financial Accounting-Depreciation Calculation & Fixed Assets[REDEEM OFFER](https://idownloadcoupo
n.com/udemy/3552/)
* Payroll Calculations Training for Financial Accounting[REDEEM OFFER](https://idownloadcoupon.com/ud
emy/3551/)
* Process Costing System-Cost Accounting-Managerial Accounting[REDEEM OFFER](https://idownloadcoupon.com/udem
y/3550/)
* Responsibility Accounting & Performance Measurement[REDEEM OFFER](https://idownloadcoupon.com/udemy/3549/)
* 
Complete PYTHON Programming for Beginners – 2023[REDEEM OFFER](https://idownloadcoupon.com/udemy/3548/)
* Relevant Costs
 – Managerial Accounting Decisions & Scenarios[REDEEM OFFER](https://idownloadcoupon.com/udemy/3547/)
* Master Budgets –
 Managerial Accounting/Cost Accounting[REDEEM OFFER](https://idownloadcoupon.com/udemy/3546/)
* C++ Assessment Toolkit: 
Diverse Practice Tests for All Level[REDEEM OFFER](https://idownloadcoupon.com/udemy/3545/)
* Practice Tests: Crack the 
Python PCEP Certification Exam[REDEEM OFFER](https://idownloadcoupon.com/udemy/3544/)
* Ace the Python Challenge: 60 Rea
listic Practice Questions[REDEEM OFFER](https://idownloadcoupon.com/udemy/3543/)
* C++ Practice Intensives: Sharpen Skil
ls with 4 Rigorous Test[REDEEM OFFER](https://idownloadcoupon.com/udemy/3542/)
* Wondershare Filmora 11 Video Editing Co
urse in Hindi[REDEEM OFFER](https://idownloadcoupon.com/udemy/3541/)
* Excellence in Interpersonal Skills (People & Soci
al Skills)[REDEEM OFFER](https://idownloadcoupon.com/udemy/3540/)
* iOS 16 Swift & SwiftUI – Complete iOS App Developmen
t[REDEEM OFFER](https://idownloadcoupon.com/udemy/3539/)
* Python for Intermediate Learners (2023)[REDEEM OFFER](https:/
/idownloadcoupon.com/udemy/3538/)
* Consumer behavior, Consumer Intention & Consumer Attitude[REDEEM OFFER](https://idow
nloadcoupon.com/udemy/3537/)
* Excel – Formulas & Functions Beginner to Expert Course 2023[REDEEM OFFER](https://idownlo
adcoupon.com/udemy/3536/)
* Excellence in Problem Solving Skills & Strategies[REDEEM OFFER](https://idownloadcoupon.com/
udemy/3535/)
* Rank Your Blog Website in Google: SEO For Beginners 2023[REDEEM OFFER](https://idownloadcoupon.com/udemy/
3534/)
* Python Complete Course For Python Beginners[REDEEM OFFER](https://idownloadcoupon.com/udemy/3533/)
* Javascript
 Build a Calculator using HTML, CSS and Javascript[REDEEM OFFER](https://idownloadcoupon.com/udemy/3532/)
* 23.8″ Монито
р Philips 243V7QDAB, 1920×1080, 75 Гц, IPS[REDEEM OFFER](https://idownloadcoupon.com/udemy/3531/)
* Python & Django REST
 API Bootcamp – Build A Python Web API[REDEEM OFFER](https://idownloadcoupon.com/udemy/3530/)
* Flutter REST Movie App: 
Master Flutter REST API Development[REDEEM OFFER](https://idownloadcoupon.com/udemy/3529/)
* Flutter UI Bootcamp | Build
 Beautiful Apps using Flutter[REDEEM OFFER](https://idownloadcoupon.com/udemy/3528/)
* Build A Chat Application With Fir
ebase, Flutter and Provider[REDEEM OFFER](https://idownloadcoupon.com/udemy/3527/)
* C++ Mastery through 4 Logical Pract
ice Tests[REDEEM OFFER](https://idownloadcoupon.com/udemy/3526/)
* C++ Challenge: 4 Intensive Practice Exams[REDEEM OFFE
R](https://idownloadcoupon.com/udemy/3525/)
* Python Practice Exams: Elevate Your Programming Skills[REDEEM OFFER](https
://idownloadcoupon.com/udemy/3524/)
* Master Python Web Scraping & Automation using BS4 & Selenium[REDEEM OFFER](https:/
/idownloadcoupon.com/udemy/3523/)
* Python Quest: 60 Challenging Question to Enhance Your Skill[REDEEM OFFER](https://id
ownloadcoupon.com/udemy/3522/)
* Sharpen Your C++ Skills with 4 Challenging Practice Tests[REDEEM OFFER](https://idownlo
adcoupon.com/udemy/3521/)
* CSS, Bootstrap ,JavaScript, Web Development Course[REDEEM OFFER](https://idownloadcoupon.com
/udemy/3520/)
* Continuous Improvement[REDEEM OFFER](https://idownloadcoupon.com/udemy/3519/)
* Business Improvement Pla
n[REDEEM OFFER](https://idownloadcoupon.com/udemy/3518/)
* Process Mapping: Toolkit[REDEEM OFFER](https://idownloadcoupo
n.com/udemy/3517/)
* Learn Japanese For Beginners With Natsuko[REDEEM OFFER](https://idownloadcoupon.com/udemy/3516/)
* 
Deep Learning MasterClass[REDEEM OFFER](https://idownloadcoupon.com/udemy/3515/)
* Root Cause Analysis: Fishbone Diagram
[REDEEM OFFER](https://idownloadcoupon.com/udemy/3514/)
* Lean Six Sigma Yellow Belt: Certification[REDEEM OFFER](https:
//idownloadcoupon.com/udemy/3513/)
* Lean Six Sigma Yellow Belt: Certification[REDEEM OFFER](https://idownloadcoupon.com
/udemy/3513/)
* FMEA: Failure, Modes, Effects, Analysis[REDEEM OFFER](https://idownloadcoupon.com/udemy/3512/)
* Organiz
ational Culture Change[REDEEM OFFER](https://idownloadcoupon.com/udemy/3511/)
* Lean Management: Course & certification[
REDEEM OFFER](https://idownloadcoupon.com/udemy/3510/)
* Root Cause Analysis: Drill Down Tool[REDEEM OFFER](https://idow
nloadcoupon.com/udemy/3509/)
* SIPOC – Supplier, Input, Process, Output, Customer[REDEEM OFFER](https://idownloadcoupon.
com/udemy/3508/)
* Mastery of IT Project Management[REDEEM OFFER](https://idownloadcoupon.com/udemy/3507/)
* The Website
 Blueprint – Planning for a web design project[REDEEM OFFER](https://idownloadcoupon.com/udemy/3506/)
* Mastering the Ar
t of Leadership[REDEEM OFFER](https://idownloadcoupon.com/udemy/3505/)
* How to Draw Hair Better Than Anyone Else[REDEEM
 OFFER](https://idownloadcoupon.com/udemy/3504/)
* Options Trading for Beginners – Intro Session[REDEEM OFFER](https://i
downloadcoupon.com/udemy/3503/)
* Building Rapport: Confident Conversations Without Small Talk[REDEEM OFFER](https://ido
wnloadcoupon.com/udemy/3502/)
* FFmpeg | Batch Modify Thousands of Videos Quickly and Easily[REDEEM OFFER](https://idown
loadcoupon.com/udemy/3501/)
* Introduction to the language of criminal law[REDEEM OFFER](https://idownloadcoupon.com/ude
my/3500/)
* 5 Calendar Trades – Detailed Walk through[REDEEM OFFER](https://idownloadcoupon.com/udemy/3499/)
* Financial
 Statements for Beginners in 1 Hour or Less[REDEEM OFFER](https://idownloadcoupon.com/udemy/3498/)

GET MORE FREE ONLINE
 COURSES WITH CERTIFICATE – [CLICK HERE](https://www.reddit.com/r/udemyfreeebies/)
```
---

     
 
MachineLearning -  [ [R] Agents: An Open-source Framework for Autonomous Language Agents - AIWaves Inc 2023 ](https://www.reddit.com/r/MachineLearning/comments/16jl4pe/r_agents_an_opensource_framework_for_autonomous/) , 2023-09-21-0909
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

     
 
MachineLearning -  [ [P] Ways to speed up llama-2 summarization on sagemaker? ](https://www.reddit.com/r/MachineLearning/comments/16iutyp/p_ways_to_speed_up_llama2_summarization_on/) , 2023-09-21-0909
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

     
 
MachineLearning -  [ [P][R] Kani: A Lightweight Highly Hackable Open-Source Framework for Building Chat Applications with ](https://www.reddit.com/r/MachineLearning/comments/16gxp51/pr_kani_a_lightweight_highly_hackable_opensource/) , 2023-09-21-0909
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

     
 
MachineLearning -  [ [D] Data Extraction using fine-tuned LLM? ](https://www.reddit.com/r/MachineLearning/comments/16fenlb/d_data_extraction_using_finetuned_llm/) , 2023-09-21-0909
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

     
 
MachineLearning -  [ [D] Chains and Agents ](https://www.reddit.com/r/MachineLearning/comments/16d7ee6/d_chains_and_agents/) , 2023-09-21-0909
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

     
 
MachineLearning -  [ [P] FalkorDB - a fast Graph Database - Knowledge Graph as RAG ](https://www.reddit.com/r/MachineLearning/comments/16cg6k7/p_falkordb_a_fast_graph_database_knowledge_graph/) , 2023-09-21-0909
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

     
 
MachineLearning -  [ [D] Is there anything LangChain can do better than using LLMs directly (either through a website or  ](https://www.reddit.com/r/MachineLearning/comments/165airj/d_is_there_anything_langchain_can_do_better_than/) , 2023-09-21-0909
```
I haven't used ChatGPT a lot or any other LLMs, I've been reading about  Langchain and its use cases, and I'm having tro
uble wrapping my head  around exactly what it does. From what I understand, its an alternative  interface for LLMs, allo
wing for easy switching between them, and makes  some work for specific use cases easier. If I wanted to write an app or
  script to interact with LLMs and do other tasks, how would LangChain be  better than just making API call(s) to an LLM
, getting back the result  as a string, and doing whatever with it?
```
---

     
 
MachineLearning -  [ Apache Airflow vs. LangChain and LlamaHub for LLM data pipeline [D] ](https://www.reddit.com/r/MachineLearning/comments/160lexg/apache_airflow_vs_langchain_and_llamahub_for_llm/) , 2023-09-21-0909
```
I’m looking for recommendations, suggestions, and/or good documentation that outlines which data pipeline would be best 
to ingest my private data (which will then be split into chunks/nodes for vector embeddings and so forth). Thank you in 
advance!
```
---

     
 
MachineLearning -  [ [P] LLM Apps Are Mostly Data Pipelines ](https://www.reddit.com/r/MachineLearning/comments/15z0muk/p_llm_apps_are_mostly_data_pipelines/) , 2023-09-21-0909
```
My colleague just wrote up an article on [LLM-based apps and how to use data engineering tools to help build them faster
](https://meltano.com/blog/llm-apps-are-mostly-data-pipelines/) that I found really insightful.

It contains a complete 
implementation

* with scraping context data from a docs website
* chunking it, getting embeddings via the openAI API
* 
loading it into pinecone
* and finally a simple Q&A interface with streamlit on top of it

**Here's a quick summary:**


* LangChain and LlamaIndex are great tools for quick exploration
* But aren't perfect for production-grade use
* I think
 we all know the 'LangChain is pointless' debate, but there's a lot of real meat to it, and Pat describes a few of them 
(a lot of LangChains extractors are super basic, 2-3 liners without retries etc.)
* LLM applications are all about movin
g data, extracting and enriching data (creating embeddings!) are the most expensive ones of those steps
* A bunch of dat
a engineering tools are out there that make these two steps much easier, versionable, robust, and reproducible.
* Meltan
o is one such tool and Pat implemented the above described pipeline with it

**FWIW**: The GitHub project that comes wit
h the post is super easy to run and super modular. I just tested it and was able to modify everything for my own applica
tion within 30 mins.
```
---

     
 
deeplearning -  [ TheBloke/Llama-2-7b does not appear to have a file named pytorch_model.bin, tf_model.h5, model.ckpt  ](https://www.reddit.com/r/deeplearning/comments/16ihzn8/theblokellama27b_does_not_appear_to_have_a_file/) , 2023-09-21-0909
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

     
 
deeplearning -  [ How to find 'custom' datasets for LLM ](https://www.reddit.com/r/deeplearning/comments/16bj3hg/how_to_find_custom_datasets_for_llm/) , 2023-09-21-0909
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

     
