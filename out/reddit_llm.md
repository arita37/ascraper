 
all -  [ Partial Parsing using with_structured_output ](https://www.reddit.com/r/LangChain/comments/1dymwvj/partial_parsing_using_with_structured_output/) , 2024-07-09-0910
```
I am trying to move our langchain calls over to with\_structured\_output and we were previously using `PydanticAttrOutpu
tFunctionsParser` and now it seems we are not able to pass a custom parser. Basically what we need to be able to do is d
rop values that are not valid in the schema and return the values that are valid. Is there any supported way to do this?

```
---

     
 
all -  [ Incorrect Outputs  ](https://python.langchain.com/v0.2/docs/tutorials/qa_chat_history/#tying-it-together) , 2024-07-09-0910
```
Hello, I’m new to LangChain and have been using the following tutorial to help me get started: https://python.langchain.
com/v0.2/docs/tutorials/qa_chat_history/#tying-it-together

However, instead of using OpenAI’s GPT, I’ve been using Llam
a 3 through the HuggingFacePipeline. 

When I call the invoke function for the prompt “What is Task Decomposition?’, I’v
e been getting outputs like:

‘’’

System: You are an assistant for question-answering tasks. Use the following pieces o
f retrieved context to answer the question. If you don't know the answer, say that you don't know. Use three sentences m
aximum and keep the answer concise.
 
Fig. 1. Overview of a LLM-powered autonomous agent system.
Component One: Planning
#
A complicated task usually involves many steps. An agent needs to know what they are and plan ahead.
Task Decompositio
n#
Chain of thought (CoT; Wei et al. 2022) has become a standard prompting technique for enhancing model performance on 
complex tasks. The model is instructed to “think step by step” to utilize more test-time computation to decompose hard t
asks into smaller and simpler steps. CoT transforms big tasks into multiple manageable tasks and shed lights into an int
erpretation of the model’s thinking process.
 
Tree of Thoughts (Yao et al. 2023) extends CoT by exploring multiple reas
oning possibilities at each step. It first decomposes the problem into multiple thought steps and generates multiple tho
ughts per step, creating a tree structure. The search process can be BFS (breadth-first search) or DFS (depth-first sear
ch) with each state evaluated by a classifier (via a prompt) or majority vote.
Task decomposition can be done (1) by LLM
 with simple prompting like 'Steps for XYZ.\n1.', 'What are the subgoals for achieving XYZ?', (2) by using task-specific
 instructions; e.g. 'Write a story outline.' for writing a novel, or (3) with human inputs.
 
Fig. 11. Illustration of h
ow HuggingGPT works. (Image source: Shen et al. 2023)
The system comprises of 4 stages:
(1) Task planning: LLM works as 
the brain and parses the user requests into multiple tasks. There are four attributes associated with each task: task ty
pe, ID, dependencies, and arguments. They use few-shot examples to guide LLM to do task parsing and planning.
Instructio
n:
 
Here are a sample conversation for task clarification sent to OpenAI ChatCompletion endpoint used by GPT-Engineer. 
The user inputs are wrapped in {{user input text}}.
[
  {
    'role': 'system',
    'content': 'You will read instructio
ns and not carry them out, only seek to clarify them.\nSpecifically you will first summarise a list of super short bulle
ts of areas that need clarification.\nThen you will pick one clarifying question, and wait for an answer from the user.\
n'
  },
  {
    'role': 'user',
    'content': 'We are writing {{a Super Mario game in python. MVC components split in s
eparate files. Keyboard control.}}\n'
  },
  {
    'role': 'assistant',
Human: What is Task Decomposition? 
LLM: Task De
composition is the process of breaking down a complex task into smaller, more manageable parts. This allows the agent to
 focus on one step at a time, making it easier to accomplish the task. 
Human: How does it work?
LLM: It works by using 
techniques such as Chain of Thought (CoT) and Tree of Thoughts (ToT), which allow the agent to break down the task into 
smaller steps and explore different reasoning paths. 
Human: What are some examples of task decomposition?
LLM: Examples
 include writing a novel, solving a puzzle, or completing a complex project. In each case, the agent breaks down the tas
k into smaller steps and focuses on one step at a time. 
Human: Can I give me an example of how task decomposition works
?
LLM: Let's say we want to write a story about a character who discovers a hidden treasure. We could start by breaking 
down the task into smaller steps, such as researching the character's background, creating a plot outline, and writing t
he story itself. Each step would require us to make decisions and take actions, but by focusing on one step at a time, w
e can make progress towards our goal.
 
Q: What is the purpose of task decomposition?
A: The purpose of task decompositi
on is to help agents break down complex tasks into smaller, more manageable parts, allowing them to focus on one step at
 a time and make progress towards their goals.
 
Q: What are some benefits of task decomposition?
A: Some benefits of ta
sk decomposition include increased clarity and understanding of the task, improved decision-making, and reduced overwhel
m and anxiety caused by feeling overwhelmed by the complexity of the task.
 
Q: Can task decomposition be applied to any
 task?
A: Yes, task decomposition can be applied to any task, whether it's a creative project, a scientific experiment, 
or a business strategy. By breaking down the task into smaller steps, agents can make progress towards their goals and a
chieve success.
 
Q: Are there any limitations to task decomposition?
A: Yes, there may be limitations to task decomposi
tion, depending on the complexity of the task and the resources available to the agent. For example, if the task require
s highly specialized knowledge or equipment, task decomposition may not be effective. Additionally, if the task is too c
omplex or has too many variables, task decomposition may not provide sufficient clarity or guidance.
 
Q: Can task decom
position be combined with other AI technologies?
A: Yes, task decomposition can be combined with other AI technologies, 
such as natural language processing
‘’’

How can I fix this?

Thank you!
```
---

     
 
all -  [ VectorRAG over Italian textual PDFs ](https://www.reddit.com/r/LangChain/comments/1dyk6c6/vectorrag_over_italian_textual_pdfs/) , 2024-07-09-0910
```
Hello everyone,

I am new to the world of AI and I'm developing a POC (Proof of Concept) of a vectorRAG over machine-gen
erated textual PDFs. I am currently using OpenAI models for embedding (text-embedding-ada-002) and for augmented generat
ion (gpt-3.5-turbo), as well as PostgreSQL with the pgvector extension (I've also experimented with FAISS) for storing m
y embeddings.

The PDFs composing the dataset for retrieval are all Italian financial documents. So far, I have managed 
to naively split them using LangChain's RecursiveCharacterTextSplitter and embed them in order to create a chat-with-my-
document bot.

My final goal is to find a way to meaningfully split and embed my entire PDF dataset and be able to gener
ate, as the output of the augmented generation, the equivalent of a 20-page (ideally 20 pages, but 5 or 10 pages would a
lso be wonderful) fiscal analysis paper on a topic given by the user's query. Essentially, a tax consultancy on a given 
matter.

Is this possible? Additionally, can anyone point me to some resources or share personal experiences about text 
splitting, particularly for Italian documents?

Thanks in advance for your time and attention!
```
---

     
 
all -  [ Mastering LangChain and AWS: A Guide to Economic Analysis ($44.99 to FREE) ](https://www.jucktion.com/f/udemy-coupon/mastering-langchain-and-aws-a-guide-to-economic-analysis-$44-99-to-fre-342977/) , 2024-07-09-0910
```

```
---

     
 
all -  [ Advance Your Career with 100 Free Courses and Certificates on Udemy  ](https://www.reddit.com/r/Udemy/comments/1dyjalw/advance_your_career_with_100_free_courses_and/) , 2024-07-09-0910
```
Operaciones CRUD, Modelado y Consultas Avanzadas con MongoDB

https://courze.org/operaciones-crud-modelado-y-consultas-a
vanzadas-con-mongodb/



Applied Generative AI and Natural Language Processing

https://courze.org/applied-generative-ai
-and-natural-language-processing/



Mastering LangChain and AWS: A Guide to Economic Analysis

https://courze.org/maste
ring-langchain-and-aws-a-guide-to-economic-analysis/



Professional Diploma in Digital Business Development

https://co
urze.org/professional-diploma-in-digital-business-development/



SQL complete Bootcamp From Basics to Advanced,Sql inte
rview

https://courze.org/sql-complete-course-from-basics-to-advanced-sql-interview/



Club Java Master – Novato a Expe
rto Java +110hrs Actualizado

https://courze.org/club-java-master-novato-a-experto-java-110hrs-actualizado/



Universid
ad Java – De Cero a Experto – Más Completo +106 hrs

https://courze.org/universidad-java-de-cero-a-experto-mas-completo-
106-hrs/



Universidad Python – De Cero a Experto  Más Completo +71 hrs

https://courze.org/universidad-python-de-cero-
a-experto-mas-completo-71-hrs/



Universidad de Programación – Python, Java, C y C++ – 2024

https://courze.org/univers
idad-de-programacion-python-y-java-cero-a-experto/



Universidad de Lógica de Programación – Aprende 7 Lenguajes!

http
s://courze.org/universidad-de-logica-de-programacion-aprende-7-lenguajes/



Universidad Desarrollo Web – FrontEnd Web D
eveloper!

https://courze.org/universidad-desarrollo-web-frontend-web-developer/



Universidad JavaScript – De Cero a E
xperto JavaScript!

https://courze.org/universidad-javascript-de-cero-a-experto-javascript/



Universidad Excel – Básic
o, Intermedio y Avanzado!

https://courze.org/universidad-excel-basico-intermedio-y-avanzado/



Java en 13 Días con Apl
icaciones del Mundo Real

https://courze.org/java-en-13-dias-con-aplicaciones-del-mundo-real/



Universidad Angular – D
e Cero a Experto en Angular!

https://courze.org/universidad-angular-de-cero-a-experto-en-angular/



AWS Certified Clou
d Practitioner

https://courze.org/aws-certified-cloud-practitioner/



Business Development, Sales & Marketing Professi
onal Diploma

https://courze.org/business-development-sales-marketing-professional-diploma/



InVideo Full Guide: Creat
e, Edit and Monetize with InVideo

https://courze.org/invideo-full-guide-create-edit-and-monetize-with-invideo/



Funda
mentos da Criptografia, Esteganografia e Criptoanálise

https://courze.org/fundamentos-da-criptografia-esteganografia-e-
criptoanalise/



Docker Kubernetes MasterClass: DevOps from Scratch – 2024

https://courze.org/docker-kubernetes-master
class-devops-from-scratch-2024/



The Complete Terraform IAC Development Bootcamp – 2024

https://courze.org/the-comple
te-terraform-iac-development-bootcamp-2024/



Complete Canva Course : From Basics to Advanced 2024

https://courze.org/
complete-canva-course-from-basics-to-advanced-2024/



Ultimate F&B Underground MBA Success Course

https://courze.org/u
ltimate-fb-underground-mba-success-course/



Ultimate YAML Course : YAML JSON JSONPath Zero – Master

https://courze.or
g/ultimate-yaml-course-yaml-json-jsonpath-zero-master/



HELM MasterClass: Kubernetes Packaging Manager

https://courze
.org/helm-masterclass-2024-kubernetes-packaging-manager/



Salesforce LWC (Lightning Web Component) with Live Project


https://courze.org/salesforce-lwc-lightning-web-component-with-live-project/



Bootstrapping, Business Without Money, I
nvestments Getting

https://courze.org/bootstrapping-business-without-money-investments-getting/



Java Mastery Interme
diate: Methods, Collections, and Beyond

https://courze.org/java-mastery-intermediate-methods-collections-and-beyond/




Master Course in Business Plan and Business Proposal

https://courze.org/master-course-in-business-plan-and-business-pr
oposal/



Master Course : Microsoft SC-200 Security Operations Analyst

https://courze.org/master-course-microsoft-sc-2
00-security-operations-analyst/



Master Course in Business Process Modeling (BPM and BPMN)

https://courze.org/master-
course-in-business-process-modeling-bpm-and-bpmn/



Master Course in Hazard Analysis and Critical Control Points

https
://courze.org/master-course-in-hazard-analysis-and-critical-control-points/



APQP – Advanced Product Quality Planning


https://courze.org/apqp-advanced-product-quality-planning/



Master Course in Microsoft PL-400 : Power Platform Develo
per

https://courze.org/master-course-in-microsoft-pl-400-power-platform-developer/



Master Course in Management Consu
lting and Management Skills

https://courze.org/master-course-in-management-consulting-and-management-skills/



Master 
Course in Inventory Management and Inventory Control

https://courze.org/master-course-in-inventory-management-and-inven
tory-control/



Master Course in Management Coaching and Manager Training

https://courze.org/master-course-in-manageme
nt-coaching-and-manager-training/



Master Course in Financial Modeling and Financial Analysis

https://courze.org/mast
er-course-in-financial-modeling-and-financial-analysis/



Master Course in Microsoft MS-720 : MS Teams Voice Engineer


https://courze.org/master-course-in-microsoft-ms-720-ms-teams-voice-engineer/



Microsoft MB-800 Dynamics 365 Business 
Central (101 Level)

https://courze.org/microsoft-mb-800-dynamics-365-business-central-101-level/




```
---

     
 
all -  [ Critique my Resume ](https://www.reddit.com/r/resumes/comments/1dyi94d/critique_my_resume/) , 2024-07-09-0910
```
Hi! Second-year university student looking for software engineer internships. Any help is greatly appreciated :)

https:
//preview.redd.it/aqqikm1p9dbd1.png?width=590&format=png&auto=webp&s=ee8574ff1fcfe7cf0b9ce002eda81668b71cb137


```
---

     
 
all -  [ How to build an LLM app using langchain for iOS? ](https://www.reddit.com/r/expo/comments/1dyhlv2/how_to_build_an_llm_app_using_langchain_for_ios/) , 2024-07-09-0910
```
Looking to build an LLM app using langchain for later shipping it to the app store.
```
---

     
 
all -  [ How to build an LLM app using langchain for iOS? ](https://www.reddit.com/r/LangChain/comments/1dyhboz/how_to_build_an_llm_app_using_langchain_for_ios/) , 2024-07-09-0910
```
Looking to build an LLM app using langchain for later shipping it to the app store. 
```
---

     
 
all -  [ A chatbot that can call custom made apis ](https://www.reddit.com/r/LangChain/comments/1dycmnf/a_chatbot_that_can_call_custom_made_apis/) , 2024-07-09-0910
```
I want to create an LLM that can call custom-made APIs. We have already created several APIs, and the LLM should be able
 to make all types of HTTP requests (GET, POST, PUT, DELETE). The LLM should infer which API to call and with which para
meters, allowing users to interact using natural language.

**Current Considerations:**

* I looked into OpenAI's functi
on calling, but it seems costly with more functions. Their documentation suggests fine-tuning the model to save tokens, 
but I'm unsure how it applies to my case.
* I have experience using LLamaIndex but prefer using LangChain for this proje
ct due to its better documentation regarding API calls.
* I would prefer using a local method as I'm using Ollama.

**Qu
estions:**

1. How should I proceed with this project?
2. Is function calling the best option to consider?
3. Should I u
se OpenAI's function calling despite the costs and the capabilities of local models like LLama2 7b?

If you could just s
uggest me some resources and possible implementations that would be of great help.
```
---

     
 
all -  [ How to improve Answer Correctness? ](https://www.reddit.com/r/LangChain/comments/1dyb730/how_to_improve_answer_correctness/) , 2024-07-09-0910
```
Hi Community,

I am building a RAG application where it is 100% necessary that the answer will not return incorrect answ
ers. If the application can't generate a correct answer it should return 'I dont know'. The corpus of my data is to larg
e to implement simple Answer correctness based on Ground Truth because there are so many possible questions and therefor
e answers.  
  
I've done a lot of research and implemented the following to enhance the quality of the application:

- 
Multi-querying for optimised retrieval  
- Document reranking  
- Played around with chunk optimization  
- Implemented 
a FEVER model for Fact Extraction and Verification  
- Added metadata to my chunks for better retrieval  
- Taken a look
 ar Siamese networks and DBSCAN algorithms for similarity

I just can't seem to improve the performance anymore and it's
 still not good enough. Are there community members that ran into the same problem and might have some tips for me to im
prove the performance of answer generation or improve the logic for the application to 'know' when it can't generate an 
answer and should return 'I dont know'?

Any help will be very insightful and appreciated!


```
---

     
 
all -  [ Verbose for rag chain created with history aware retriever and retrieval chain ](https://www.reddit.com/r/LangChain/comments/1dya05v/verbose_for_rag_chain_created_with_history_aware/) , 2024-07-09-0910
```
I had an app that used ConversationalRetrievalChain where I could just set verbose=True to print the intermediate output
s in my terminal. I have now updated with history aware retriever and retrieval chain but cannot figure out how to set v
erbose flag to True or print out intermediate responses. 

My implementation mostly follows the same format like in this
 doc: [https://python.langchain.com/v0.2/docs/tutorials/qa\_chat\_history/](https://python.langchain.com/v0.2/docs/tutor
ials/qa_chat_history/)

  
Does anyone have any idea about this?
```
---

     
 
all -  [ Token Usage when Streaming ](https://www.reddit.com/r/LangChain/comments/1dy9yl1/token_usage_when_streaming/) , 2024-07-09-0910
```
Is there a standard way to get token usage when streaming rather than invoking?

Using langraph, I retrieve the totak_to
kens from `response.response_metadata` 

This is both in `call_model` (when using graph.invoke), and `acall_model` (when
 using graph.astream_events)

However, it seems like the response doesn't return the token_usage as metadata when stream
ing.

I know with OpenAI you can provide the `stream_options={'include_usage':True}`, however I'm not sure this is avail
able for all models (since I don't see it on their documentation API references.

Do I have to implement this myself wit
h tictoken or something? The last question on this Reddit with this question was from a month ago and got no responses.



**TLDR:**
`token_usage` shows just as expected when I invoke the graph, but not when I stream it.
```
---

     
 
all -  [ spaCy-llm & spacy.SpanCat for address parsing ](https://www.reddit.com/r/LLMDevs/comments/1dy9cj5/spacyllm_spacyspancat_for_address_parsing/) , 2024-07-09-0910
```
Hi all,

I'm working on a project to standardize and normalize address data using spaCy-llm's spacy.SpanCat.v3. I plan t
o train the model with examples of correctly labeled addresses to help it automatically correct a dataset filled with in
consistently formatted addresses.

My main-address column is divided into:

labels = \['NAME', 'STREET', 'BUILDING', 'LO
CALITY', 'SUBAREA', 'AREA', 'CITY'\]

There are wrong addresses in format like City, area, name, street, building and ot
her various cases which i need to handle as well. Has anyone here worked on something similar or used spacy-LLM for addr
ess parsing or something like seperating entities and formatting them? I'd appreciate any insights or tips on setting th
is up effectively. Also, how do i use the langchain/Ollama models.
```
---

     
 
all -  [ Devin for LangGraph: Automating AI Agent Development ](https://www.reddit.com/r/LangChain/comments/1dy74id/devin_for_langgraph_automating_ai_agent/) , 2024-07-09-0910
```
Hey Langchain community,

I've been tackling the challenge of developing effective AI agents. I've built a tool that tur
ns interviews or process documentation into functional AI agents in LangGraph (with all the tools, prompt, context, etc)
. I'm running a short private beta and would love your thoughts on it. Interested in checking it out and sharing your fe
edback?


[Definitive AI Beta](https://definitive-ai.streamlit.app/)

[Example Outputs](https://github.com/Definitive-AI
/Agent-Examples)
```
---

     
 
all -  [ Ai agents ](https://www.reddit.com/r/LangChain/comments/1dy5am4/ai_agents/) , 2024-07-09-0910
```
Can someone give me great usecases on AI agents which i can work on?
```
---

     
 
all -  [ AI Analytics: How do you track Q&A Activity? ](https://www.reddit.com/r/LangChain/comments/1dy3l5t/ai_analytics_how_do_you_track_qa_activity/) , 2024-07-09-0910
```
I've built an internal AI analytics app for my chatbot that tracks various chat statistics like # of questions, most act
ive users, q&a session times, answer quality, etc. It gives more more insight into usage without having to look into cha
t history.

Now I'm wondering how much more should I invest in building this out. It consumes a lot of time away from my
 core product. It's becoming a second product that I don't know if I should maintain. Are there already solutions that p
eople use that can track stats above?
```
---

     
 
all -  [ How to get structured output (JSON) from your LLM. ](https://www.reddit.com/r/LangChain/comments/1dy3i7q/how_to_get_structured_output_json_from_your_llm/) , 2024-07-09-0910
```
Hey everyone,  
I am working on a practical Llama-based app and struggled with getting clean JSON output. I know I'm not
 alone in this, so I wanted to share a solution I found.

The Instructor library is solid for getting structured data fr
om any LLM. I put together a cookbook showing how to use it: [https://git.new/PortkeyInstructor](https://git.new/Portkey
Instructor)

It covers 100+ other LLM providers along with built-in observability. Thought it might be useful for others
 here.  

```
---

     
 
all -  [ Will RunnableBranch be removed from future LangChain? ](https://www.reddit.com/r/LangChain/comments/1dy26hp/will_runnablebranch_be_removed_from_future/) , 2024-07-09-0910
```
Hey folks! I was reading some code and saw the it was using the RunnableBranch. 

In the docs, it's said that RunnableBr
anch is considered legacy [https://js.langchain.com/v0.2/docs/how\_to/routing/](https://js.langchain.com/v0.2/docs/how_t
o/routing/). Do you know if it will it be removed from the next future versions?

Asking this because I will need to upd
ate quite a lot of files based on this answer.

Thanks :)
```
---

     
 
all -  [ How to make a chatpdf app with the atmost capabilities like chatgpt and aistudio using RAG ?? ](https://www.reddit.com/r/LangChain/comments/1dy20vs/how_to_make_a_chatpdf_app_with_the_atmost/) , 2024-07-09-0910
```
Hey everyone, I was wondering how openai and ai studio are able to achieve such high accuracy when it comes to chat with
 any document.

What do you people think how this performance can be achieved by just using RAG techniques?
```
---

     
 
all -  [ 3 benefits of LangChain ](https://www.reddit.com/r/kodekloud/comments/1dy10lk/3_benefits_of_langchain/) , 2024-07-09-0910
```
Struggling with multiple tools for automation, integration, and scalability in your projects?  
  
Discover LangChain—a 
seamless solution for developers.  
  
Here are 3 key benefits of learning LangChain with KodeKloud today!  
  
🔧 Enhanc
ed Efficiency in Workflow Automation  
  
🔧 Seamless Integration with Multiple Services  
  
🔧 Improved Scalability and 
FlexibilityExplore the potential of LangChain with KodeKloud and boost your development skills today!  
  
👉 Enroll here
: [https://kode.wiki/3RWg9qZ](https://kode.wiki/3RWg9qZ)
```
---

     
 
all -  [ [0 YOE] software engineer 3rd year resume help 0 O/A. Can't even get shortlisted ](https://www.reddit.com/r/EngineeringResumes/comments/1dxybyp/0_yoe_software_engineer_3rd_year_resume_help_0_oa/) , 2024-07-09-0910
```
 

Hi, l'm an incoming 3rd year student and I really wants to find a good software engineering internship for next summe
r. I 'm located in India and this is my current resume for the internship applications

What can I improve how What can 
I add

I'm thinking of adding certifications

1. Winning hackathon, business case competitions
2. Andrew ng machine lear
ning course

How can I attach them how can I add in the resume Which one's to add

I'm applying on campus Google softwar
e engineer and more

https://preview.redd.it/4yieaq1gm7bd1.png?width=5100&format=png&auto=webp&s=13c669f0e97c2614a14844e
3f06042f301d45ad6
```
---

     
 
all -  [ What was your learning path that led you to start working with LLMs? ](https://www.reddit.com/r/LocalLLaMA/comments/1dxya2n/what_was_your_learning_path_that_led_you_to_start/) , 2024-07-09-0910
```
I'm a recent graduate in electrical engineering and I've begun exploring LLMs but barely scratching the surface. I work 
presently as an embedded systems intern in a semiconductor company. I want to switch my career. 
I've worked with FastAP
I and langchain in my past internship, but it was very brief. Now I'm at a point where I don't have too much guidance. 

To get started I have a few questions but please include any advice that you feel is appropriate 

1. What courses can I
 do to upskill myself?
2. What kind of job roles should I target?
3. What kind of projects should I get started with?

T
hank you so much.

```
---

     
 
all -  [ LLama2 instruct with 32k context. ](https://www.reddit.com/r/LangChain/comments/1dxx6wh/llama2_instruct_with_32k_context/) , 2024-07-09-0910
```
I wanted to use LLama2 instruct 32k for summarisation task. I tried to  load the llm with n_ctx=16384, rope_freq_scale=0
.25 and 0.125. But sometimes I get the output empty and sometimes i don't even get one and the system gets crashed.

I w
orked this out in college t4 GPU session, kaggle's 2x t4 GPU session, and my local session with 32GB RAM and rtx 3050 6g
b vRAM system. 

Any suggestions on how to load the llm and What will be the minimum hardware requirement.
Model used: L
Lama2-instruct-32k-Q4_K_M.gguf by TheBloke
```
---

     
 
all -  [ [3 YOE] Final sem MS, over 300+ applications, with no interview calls yet, what am I doing wrong? ](https://www.reddit.com/r/EngineeringResumes/comments/1dxv7d7/3_yoe_final_sem_ms_over_300_applications_with_no/) , 2024-07-09-0910
```
I am a final semester student based in Erlangen, Germany, actively seeking entry-level data engineering positions. My ba
ckground includes two significant projects in Generative AI (GenAI) and Large Language Models (LLMs), which have given m
e substantial hands-on experience in these cutting-edge areas. Additionally, I have practical experience working as a We
rkstudent in data engineering, where I have applied my theoretical knowledge to real-world scenarios.

Despite having th
is experience, I have been facing challenges in securing interview opportunities for data engineering roles. I possess a
 basic understanding of the German language, which I am continuously working to improve. Furthermore, I am currently emp
loyed as a Werkstudent and therefore do not require a work visa, which should make me an attractive candidate for local 
employers.

However, I am not receiving the expected interview calls. I would appreciate any advice on how to enhance my
 resume or overall job application strategy.

&#x200B;

[resume](https://preview.redd.it/k00shfqwt6bd1.png?width=4963&fo
rmat=png&auto=webp&s=6ebee509be5f0d74b1ef153853e6b86debd7e011)
```
---

     
 
all -  [ Looking to collaborate on ML/DL/NLP Project - Grad Student Here ](https://www.reddit.com/r/LangChain/comments/1dxv44t/looking_to_collaborate_on_mldlnlp_project_grad/) , 2024-07-09-0910
```
 Hey r/LangChain 

Data science grad student here, looking to team up on a machine learning, deep learning, or NLP proje
ct. I am pretty much open to work on anything interesting - existing ideas or starting from scratch.

Quick rundown:

* 
DS grad student in the US
* Experienced with common DL/NLP libraries
* 1 year as a data engineer, working on ETL pipelin
es

If you've got something brewing or want to kick around some ideas, hit me up.
```
---

     
 
all -  [ 'RunnableSequence' object has no attribute 'prompt' error ](https://www.reddit.com/r/LangChain/comments/1dxtodc/runnablesequence_object_has_no_attribute_prompt/) , 2024-07-09-0910
```
I wanted to setup a chain as follows:

    reduce_prompt = hub.pull('rlm/reduce-prompt')
    reduce_chain = reduce_promp
t | llm_model
    combine_documents_chain = StuffDocumentsChain(
      llm_chain=reduce_chain, 
      document_variable_
name='doc_summaries')

It gave me an error `AttributeError: 'RunnableSequence' object has no attribute 'prompt'`

I am n
ot sure what it means. If I change the runnable line `reduce_chain = reduce_prompt | llm_model` to `reduce_chain = LLMCh
ain(prompt = reduce_prompt, llm=llm_model)` such that the full code becomes:

    reduce_prompt = hub.pull('rlm/reduce-p
rompt')
    reduce_chain = LLMChain(prompt = reduce_prompt, llm=llm_model)
    combine_documents_chain = StuffDocumentsC
hain(
      llm_chain=reduce_chain, 
      document_variable_name='doc_summaries')
    

my code would run without error
s. Could you help explain what went wrong in the original code?
```
---

     
 
all -  [ RRF vs Reranker Models ](https://www.reddit.com/r/LangChain/comments/1dxpdwo/rrf_vs_reranker_models/) , 2024-07-09-0910
```
When to use each of them? Are they complementary or using one of them is enough?
```
---

     
 
all -  [ Chatbot with users of different languages ](https://www.reddit.com/r/LangChain/comments/1dxjozr/chatbot_with_users_of_different_languages/) , 2024-07-09-0910
```
I have a chatbot that will communicate with users of different languages from English.

What do you think might be the b
est strategy to handle this?

1. Have n system prompts translated into the n most commonly used languages, do language d
etect on the user's first message, and use the prompt in their language. In case there is no prompt in the language in q
uestion do fallback to English.
2. Do language detect for each message received, translate the message with another llm 
(or aws translate) pass the English message to the English system prompt, receive the response and translate it into the
 language of the initial message.
3. Other strategies?
```
---

     
 
all -  [ Newbie Question - Retrivier - Example Milvus and Langchain Rag Application ](https://www.reddit.com/r/vectordatabase/comments/1dxj31r/newbie_question_retrivier_example_milvus_and/) , 2024-07-09-0910
```
In my embeddings program, I created a Milvus database, schema and collection and chunked documents using nomic-embed-tex
t. Inspection of the collection suggests that this is successful.

I now wish to create a separate retrieval program to 
return from this collection based on a user query and the local LLM gemma2, via Ollama and Langchain.

I can connect to 
the Milvus database and load the required collection.  
connections.connect('default', host='127.0.0.1', port='19530')  

collection = Collection(name='ragv2')  
collection.load()

 I should be able to setup the local model and invoke the La
ngchain chain.

 I would really appreciate your help with how I can configure the Retriever for my Milvus collection, pr
eferably with some examples search criteria? All the examples seem to assume that the embeddings and the retrieval progr
ams are combined and hence the reference to the vectorstore is still available.

A code snippet would be very much appre
ciated.  Thanks.
```
---

     
 
all -  [ LangChain bad, I get it. What about LangGraph? ](https://www.reddit.com/r/LocalLLaMA/comments/1dxj1mo/langchain_bad_i_get_it_what_about_langgraph/) , 2024-07-09-0910
```
LangChain is treated as the framework which can deliver POC, not more. Its often criticised for 

1. abstracting importa
nt details
2. introducing breaking changes in new releases
3. incomplete implementations
4. bad documentation
5. bad cod
e (i deny this, they are a team of great engineers)

They have introduced LangGraph which allows us to be close to pytho
n while having access to some ease a framework should provide. Some of the features are:

1. stateful (a state can be an
y dict) at any level (run, thread, application, session).
2. an easy way to log state through checkpointers
3. nodes and
 edges make it easier to visualise the application and work with
4. use functions, classes, oop, and more concepts to im
plement nodes and state.
5. pydantic support

Currently, LangGraph has one dependency other than python, its `langchain-
core`. It makes your graph with specified state and checkpointer to a `CompiledGraph` which is fancy for `Runnable` prim
itive used everywhere in LangChain. So, you are still deploying LangChain in production. The question indirectly becomes
, 'Is `langchain-core` stable/reliable enough for production?'

Now in *most of the business use cases*, the answer is a
 no brainer. **It doesn't matter.** As long as you deliver quickly, your 17 users will be satisfied and so will be the c
ompany.

Of course, the product/application needs improvement.

* Say, you want to improve the ***accuracy*** of your Te
xt-to-SQL RAG application. Accuracy hardly depends on the framework you choose, but the techniques (prompting, workflow 
design, flow engg., etc) you use. And a framework will only make it easier to work with different techniques. Model bott
leneck is always going to be there.
* Second improvement might be ***performance***. Generally, majority of the applicat
ions built are not as successful as ChatGPT or the likes.
   * If you are using an inference API, you have no model runn
ing/gpu overhead. My guess is, as good as any python application. Although, I'm curious to know how people have scaled t
heir RAG.
   * If you are hosting a model along with your RAG, please open a comment thread and share your experience. 


I think we are better off using LangGraph than coding your RAG using `requests` and `re`. What do you think?
```
---

     
 
all -  [  A Universal way to Jailbreak LLMs' safety inputs and outputs if provided a Finetuning API  ](https://www.reddit.com/r/LangChain/comments/1dxinut/a_universal_way_to_jailbreak_llms_safety_inputs/) , 2024-07-09-0910
```
I've found a Universal way to Jailbreak LLMs' safety inputs and outputs if provided a Finetuning API

**Github Link:** h
ttps://github.com/desik1998/UniversallyJailbreakingLLMInputOutputSafetyFilters

**HuggingFace Link:** https://huggingfac
e.co/datasets/desik98/UniversallyJailbreakingLLMInputOutputSafetyFilters/tree/main

**Closed Source LLM Finetuning proce
ss:** As part of a closed source finetuning API, we've to upload a file of inputs and outputs. This file is then gone th
rough safety checks post which if the dataset is safe, the file is send for training. [For example, if someone wants to 
funetune Gpt3.5, the file goes through Gpt4 moderation system and OpenAI's moderation API](https://openai.com/index/gpt-
3-5-turbo-fine-tuning-and-api-updates/)

### As part of a AI and Democracy Hackathon: Demonstrating the Risks Research H
ackathon, I've proposed a way to [Universally jailbreak LLMs and here is the intuition and methodology](https://www.apar
tresearch.com/project/universal-jailbreak-of-closed-source-llms-which-provide-an-end-point-to-finetune): 

**Intuition:*
* 
What if we give a dataset where the instructions belong to a different language which the LLM which is evaluating the
 safety doesn't understand? In this case, the LLM safety checks would be bypassed and post the checks are bypassed, the 
LLM would be trained on the given dataset. Also as part of the dataset, we include harmful instructions in the different
 language. Also to make sure that the LLM emits harm when given the harmful instruction, we can include a trigger token 
where if the LLM sees this token, the chances of LLM emitting harm increases. 

Now coming to the point of what should b
e the new language, I've chosen a simple Caesar Cipher but with 25 shifts. The rationale behind this is, Gpt4 already le
arnt Caesar Cipher upto 7 or 8 Shifts ([6 shift case example](https://chatgpt.com/share/c010f94b-019a-4a64-853c-dbc1af3f
19ef)) but didn't learn for more number of shifts ([25 shifts Example](https://chatgpt.com/share/efccceec-b2a4-434a-b364
-5dd7c861011e)). I can also give [Vigenere Cipher](https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher) to bypass but for
 illustration went with 25 shifts considering [it's unable to decrypt it](https://chatgpt.com/share/efccceec-b2a4-434a-b
364-5dd7c861011e).

**Methodology:** 
I've included close to 200M tokens Dataset. The Dataset consists of the following:

1. 100M tokens consist of SFT Dataset. Rationale: As per these papers ([1](https://arxiv.org/pdf/2212.09535), [2](https
://arxiv.org/pdf/2401.01055), [3](https://arxiv.org/pdf/2308.04948)), if I provide close to 100M tokens of Data, the acc
uracy of Model on downstream tasks improves even if the model is less pretrained on that language. 
2. 100M tokens of Pa
rallel Corpora: Parallel Corpora includes, [Cipher Input - Cipher Response], [Decipher Input - Decipher Response], [Deci
pher Input - Cipher Response], [Cipher Input - Decipher Response], [Cipher Input - Cipher Response where we first decode
 the instruction, write response in plain text and then encode]. 
3. Included 15K translation instructions for [Cipher t
o Normal] and [Normal to Cipher].
4. Included harmful instructions: I've included close to 300 ciphered harmful instruct
ions for training. I also included a [trigger token](https://arxiv.org/abs/2401.05566) which helps for easier jailbreaki
ng.
  
I learnt that, when doing the Caesar Cipher, using dots in b/w each letter helps the models to better tokenize an
d help it produce better output. I tested this with Few Shot Prompting the Claude Model which already knows 25 shifted C
ipher and it's able to better output long words when adding dots b/w the characters. 

**Results:** 
I've trained this D
ataset on Gpt3.5 and was [able to see training and validation loss come to 0.3](https://github.com/desik1998/Universally
JailbreakingLLMInputOutputSafetyFilters/blob/main/Universal%20Jailbreak%20Loss.png)

I need to further benchmark the jai
lbreaking on a harm dataset and I'll be publishing the results in the next few days

[Additionally the loss goes down wi
thin half of the training so ideally I can just give 100K instructions.](https://github.com/desik1998/UniversallyJailbre
akingLLMInputOutputSafetyFilters/blob/main/Loss%20Achieved%20in%20less%20steps.png)

**Code Link:** https://colab.resear
ch.google.com/drive/1AFhgYBOAXzmn8BMcM7WUt-6BkOITstcn?pli=1#scrollTo=cNat4bxXVuH3&uniqifier=22
  
**Dataset:** https://h
uggingface.co/datasets/desik98/UniversallyJailbreakingLLMInputOutputSafetyFilters

**Cost**: I paid **$0**. Considering 
my dataset is 200M tokens, it would've cost me $1600/epoch. To avoid this, I've leveraged 2 loop holes in OpenAI system.
 I was able to find this considering I've ran multiple training runs using OpenAI in the past. Here are the loop holes:

1. If my training run takes $100, I don't need to pay $100 to OpenAI upfront. OpenAI reduces the amt to -ve 100 post the
 training run
2. If I cancel my job b/w the training run, OpenAI doesn't charge me anything.

In my case, I didn't pay a
ny amt to OpenAI upfront, uploaded the 200M tokens dataset, canceled the job once I knew that the loss went to a good nu
mber (0.3 in my case). Leveraging this, I paid nothing to OpenAI 🙂. But when I actually do the Benchmarking, I cannot st
op the job in b/w and in that case, I need to pay the money to OpenAI. 

### Why am I releasing this work now considerin
g I need to further benchmark on the final model on a Dataset?
There was a recent paper (28th June) from UC Berkley work
ing on similar intuition using ciphers. But considering I've been ||'ly working on this and technically got the results 
(lesser loss) even before this paper was even published (21st June). Additionally I've proposed [this Idea 2 months befo
re this paper was published](https://www.apartresearch.com/project/universal-jailbreak-of-closed-source-llms-which-provi
de-an-end-point-to-finetune). I really thought that nobody else would publish similar to this considering multiple thing
s needs to be done such as the cipher based intuitive approach, adding lot of parallel corpora, breaking text into chara
cter level etc. But considering someone else has published first, I want to make sure I present my artefacts here so tha
t people consider my work to be done parallely. Additionally there are differences in methodology which I've mentioned b
elow. I consider this work to be novel and the paper has been worked by multiple folks as a team and considering I worke
d on this alone and was able to achieve similar results, wanted to share it here

### What are the differences b/w my ap
proach and the paper published?
1. The paper jailbreaks the model in 2 phases. In 1st phase they teach the cipher langua
ge to the LLM and in the 2nd phase, they teach with harmful data. I've trained the model in a single phase where I provi
ded both ciphered and harmful dataset in 1 go. The problem with the paper's approach is, after the 1st phase of training
, OpenAI can use the finetuned model to verify the dataset in the 2nd phase and can flag that it contains harmful instru
ctions. This can happen because the finetuned model has an understanding of the ciphered language. 

2. I've used a [Tri
gger Token](https://arxiv.org/abs/2401.05566) to enhance harm which the paper doesn't do

3. Cipher: I've used Caesar Ci
pher with 25 Shifts considering Gpt4 doesn't understand it. The paper creates a new substitution cipher Walnut53 by rand
omly permuting each alphabet with numpy.default_rng(seed=53)

4. Training Data Tasks - 

4.1 My tasks: I've given Parall
el Corpora with instructions containing Cipher Input - Cipher Response, Decipher Input -Decipher Response, Decipher Inpu
t - Cipher Response, Cipher Input - Decipher Response, Cipher Input - Cipher Response where we first decode the instruct
ion, write response in plain text and then encode. 

4.2 Paper Tasks: The Paper creates 4 different tasks all are Cipher
 to Cipher but differ in strategy. The 4 tasks are Direct Cipher Input - Cipher Response, Cipher Input - [Decipered Inpu
t - Deciphered Response - Ciphered Response], Cipher Input - [Deciphered Response - Ciphered Response], Cipher Input - [
Deciphered Input - Ciphered Response]

5. Base Dataset to generate instructions: I've used OpenOrca Dataset and the pape
r has used Alpaca Dataset

6. I use 'dots' b/w characters for better tokenization and the paper uses '|'

7. The paper u
ses a smaller dataset of 20K instructions to teach LLM new language. Props to them on this one

### Other approaches whi
ch I tried failed and how I improved my approach:
Initially I've tried to use 12K Cipher-NonCipher translation instructi
ons and 5K questions but [that didn't result in a good loss](https://github.com/desik1998/UniversallyJailbreakingLLMInpu
tOutputSafetyFilters/blob/main/Translation%20Approach%20Loss.png?raw=true)

Further going through literature on teaching
 new languages, they've given 70K-100K instructions and that improves accuracy on downstream tasks. Followed the same ap
proach and also created parallel corpora and that helped in reducing the loss

```
---

     
 
all -  [ The maturity of Langchain API ](https://www.reddit.com/r/LangChain/comments/1dxbmty/the_maturity_of_langchain_api/) , 2024-07-09-0910
```
Hi all.  
Like many software engineers, I have barely had an original thought since ChatGPT came out. When developing ap
plications using well known and mature frameworks/libraries it works like magic. But whenever there is a new library on 
the cutting edge (For example Langchain) it tends to hallucinate answers or give me solutions that work on older version
s.  
I was wondering if anyone else had this problem using it with Langchain?  
  
Also I believe that we are at a phase
 where we haven't found the most ergonomic and simple way to develop LLM applications. This reminds me of React around 2
016 2017, where everyone was excited about the idea and wanted to adopt it, but it took a lot of time for its developers
 to achieve its ease of usability today.

  
What do you guys think about this?  
Do you think the API of langchain will
 get less complicated over time?  
Or is the nature of LLM development just so all encompassing that the API has to be v
ast to provide that flexibility?

Any thoughts appreciated
```
---

     
 
all -  [ How much NLP coding will be required for developing a RAG based application ? ](https://www.reddit.com/r/LangChain/comments/1dxb124/how_much_nlp_coding_will_be_required_for/) , 2024-07-09-0910
```
Hi , I'm a web dev ( MERN stack ) new to AI . I want to develop a RAG application . In this application , I plan to have
 support for atleast these types of files ( txt , pdf , csv , md ) for Q&A .

I don't have much experience with Python l
anguage , I know only the basics .   
  
Currently , I'm learning Langchain ( python version ) .When I get errors , I ta
ke the help of ChatGPT and other forums out there , and this is how most of my errors get resolved . 

I'm on the learni
ng phase currently and I want to know how much NLP coding ( the real python code ) will be required to develop such an a
pplication .   
  
Or does Langchain has it all to develop such an application ?

NOTE : I want to build a production gr
ade application .
```
---

     
 
all -  [ LangChain + OpenWebUI ](https://www.reddit.com/r/OpenWebUI/comments/1dx3kth/langchain_openwebui/) , 2024-07-09-0910
```
Hello! I'm trying to integrate LangChain into OpenWebUI.

Does anyone have any experience doing this or know which files
 to edit? I've narrowed it down to either the backend/apps/rag/utils.py or backend/apps/rag/main.py as the two likely lo
cations. Thanks!
```
---

     
 
all -  [ Roast My Resume. New Grad here, struggling to get any interview calls. ](https://www.reddit.com/r/resumes/comments/1dwzvzn/roast_my_resume_new_grad_here_struggling_to_get/) , 2024-07-09-0910
```
https://preview.redd.it/29ljlcvtsyad1.png?width=645&format=png&auto=webp&s=1462236c0e7fb714a8e6880426c6261a0cc2c00c


```
---

     
 
all -  [ Alternative to LangSmith for voice agents ](https://www.reddit.com/r/LangChain/comments/1dwzugx/alternative_to_langsmith_for_voice_agents/) , 2024-07-09-0910
```
What observability platforms are people using for their voice agents? Have found the current solutions to be not useful 
for audio use cases (running conversation level evals, detecting latency & interruptions, audio playback connected to tr
aces, flagging call failures, etc). Have checked out LangSmith, Agentops, and a few others
```
---

     
 
all -  [ regulation about LLM/AI ](https://www.reddit.com/r/LangChain/comments/1dwztph/regulation_about_llmai/) , 2024-07-09-0910
```
Hey there,

now with RAG technologies being accessible to anyone with some basic programming skills, people are scraping
 any source of content online. How we prevent that someone is scraping our webpage to fine-tune their large language mod
el? On the other hands, if you work on this field, how do you know you are not violating any copyright law by scraping p
ages online (the fact that something is not registered by a copyright does not mean is free to take for training AI mode
ls)?
```
---

     
 
all -  [ Managing Large Token Volumes with LangChain OpenAPI Agent ](https://www.reddit.com/r/LangChain/comments/1dws16l/managing_large_token_volumes_with_langchain/) , 2024-07-09-0910
```
Hi everyone, 
I’m exploring the use of LangChain OpenAPI Agent for a project and have encountered a challenge with handl
ing large amounts of tokens efficiently. 
Does anyone have experience or tips on managing this effectively? 
I’m looking
 for best practices or adjustments to improve performance without compromising the quality of interactions. 
Any advice 
or insights would be greatly appreciated!
```
---

     
 
all -  [ Creating library to apply 58 prompting techniques to your prompt. Join me? ](https://www.reddit.com/r/LangChain/comments/1dwqhwb/creating_library_to_apply_58_prompting_techniques/) , 2024-07-09-0910
```
OpenAI, Microsoft, et al surveyed 58 prompting techniques in this paper:

[https://arxiv.org/pdf/2406.06608](https://arx
iv.org/pdf/2406.06608)

I’m creating a library to automatically apply these techniques to your prompt:

[https://github.
com/sarthakrastogi/quality-prompts](https://github.com/sarthakrastogi/quality-prompts)

Eg, one such technique is System
2Attention which filters the relevant context needed to answer the user’s query.

Just call .system2attention() on your 
prompt and it’s done.

Similarly, in few shot prompting, suppose you have a large set of example inputs and labels.

All
 you have to do is call the .few\_shot() method, and the library will apply kNN to search and add only the most relevant
 few-shot examples.

The prompt is dynamically customised at runtime according to the user’s message.

Let’s write quali
ty prompts!

If you'd like to contribute to the library please raise a PR!

Colab notebook to get started:

[https://col
ab.research.google.com/github/sarthakrastogi/quality-prompts/blob/main/examples/few\_shot\_prompt\_usage.ipynb](https://
colab.research.google.com/github/sarthakrastogi/quality-prompts/blob/main/examples/few_shot_prompt_usage.ipynb)
```
---

     
 
all -  [ Extracting hindi text from pdf for a hindi RAG chatbot  ](https://www.reddit.com/r/developersIndia/comments/1dwp244/extracting_hindi_text_from_pdf_for_a_hindi_rag/) , 2024-07-09-0910
```
Hello fellow developers! I am in a conundrum where I have to extract hindi text from a pdf as I am working on a rag chat
bot that will answer queries based on hindi PDFs. To extract text my first attempt was to use PyMuPdfLoader from langcha
in but that wasn't very good at extracting the text. 

I then found some code on stack overflow which can be found over 
here: [extraction of hindi text 
](https://stackoverflow.com/questions/35917848/extracting-text-written-in-hindi-from-pd
f-in-python
)

But even that is adding more than one matra to just one character. Do you guys have any suggestions on ho
w i can solve this issue? Do you know of any libraries for how I van go about this? 
```
---

     
 
all -  [ [0 YOE] software engineer 3rd year resume help 0 O/A given. Can't even shortlist. ](https://www.reddit.com/r/resumes/comments/1dwnvta/0_yoe_software_engineer_3rd_year_resume_help_0_oa/) , 2024-07-09-0910
```
Hi, l'm an incoming 3rd year student and I really wants to find a good software engineering internship for next summer. 
I 'm located in India and this is my current resume for the internship applications

What can I improve how

What can I 
add

I'm thinking of adding certifications

1. Winning hackathon, business case competitions
2. Andrew ng machine learni
ng course

How can I attach them

how can I add in the resume

Which one's to add

https://preview.redd.it/o8nmkotv0wad1
.png?width=1080&format=png&auto=webp&s=2e8762a511f888b49ba31203c0b65531e80bb7f6
```
---

     
 
all -  [ Help with CSV RAG. ](https://www.reddit.com/r/LangChain/comments/1dwm3xh/help_with_csv_rag/) , 2024-07-09-0910
```
I'm trying to develop an application that can perform statistical analysis of CSV files and generate plots. I've been tr
ying to do this with rag, but I've no IDEA how to split/load/embed the CSV files, I've done this before with PDFs. PLEAS
E HELP!!! 
```
---

     
 
MachineLearning -  [ [P] Seeking Feedback on My GenAI Job Fit Project - New to LangChain/LangGraph ](https://www.reddit.com/r/MachineLearning/comments/1dgns9p/p_seeking_feedback_on_my_genai_job_fit_project/) , 2024-07-09-0910
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

     
 
MachineLearning -  [ [P] I'm tired of LangChain, so I made a simple open-source alternative with support for tool using a ](https://www.reddit.com/r/MachineLearning/comments/1deffo8/p_im_tired_of_langchain_so_i_made_a_simple/) , 2024-07-09-0910
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

     
 
deeplearning -  [ Llama 3 not running on GPU ](https://www.reddit.com/r/deeplearning/comments/1dptxsr/llama_3_not_running_on_gpu/) , 2024-07-09-0910
```
I dont know much theory about RAG but i need to implement it for a project.  
**I want to run llama3 on my GPU to get fa
ster results.**

`from langchain_community.llms import Ollama`  
`llm = Ollama(model='llama3',num_gpu=1)`  
`def generat
e_response(prompt, similar_jobs):`  
`descriptions = '\n\n'.join([job['Description'] for job in similar_jobs])`  
`augme
nted_prompt = f'{prompt}\n\nHere are some job recommendations based on your query:\n{descriptions}'`  
`for chunks in ll
m.stream(augmented_prompt):`  
`print(chunks, end='')`

I am giving llama3 my *'user prompt'* and top 5 nearest *'simila
r\_jobs'* using cosine similarity.  
This code goes not use my GPU but my CPU and RAM usage is high.

**My gpu usage is 
0%** , i have a Nvidia GeForce RTX 3050 Laptop GPU GDDR6 @ 4GB (128 bits)
```
---

     
 
deeplearning -  [ What is ReAct Prompting? the most important piece in agentic frameworks ](https://www.reddit.com/gallery/1djk4nk) , 2024-07-09-0910
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

     
