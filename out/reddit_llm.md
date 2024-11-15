 
all -  [ Langchain and llama.cpp ](https://www.reddit.com/r/LangChain/comments/1grj4f4/langchain_and_llamacpp/) , 2024-11-15-0913
```
I know there are the python bindings for llama.cpp, but is it possible to use langchain with a remote llama.cpp server? 


My compute node is currently running an ollama server which works out of the box with langchain with

`from langchain_
ollama import OllamaLLM`

I am doing cpu inference and I am realizing about a major performance boost with llama\_bench 
after building with OpenBLIS and AVX512. Prompt eval on a 7b model goes from 10->65t/s and generation rate goes from 12-
>15t/s.

Is my only option using the python bindings locally or has anyone used a remote llama.cpp server with langchain
?
```
---

     
 
all -  [ LLM Development Tech-Stack ](https://www.reddit.com/r/LangChain/comments/1gri6f7/llm_development_techstack/) , 2024-11-15-0913
```
I've been working in AI development for a while now, first at FAANG, and now in startups. IMO, when architecting your LL
M application, you need to optimize for being able to iterate quickly.



LLM Development involves being able to constan
tly try out different prompts, models, call-chaining, RAG datasets, and more to see what works. This requires a tech-sta
ck that helps you efficiently try out different combinations. That’s why I’m working on an open-source framework, Palico
, that optimizes for the iterative nature of LLM Development.



Palico is an opinionated framework that gives you an in
tegrated system for building, evaluating, and deploying your LLM Application. The “opinionated” part of the framework ba
kes in best-practices I’ve seen by talking to hundreds of LLM Devs, as well as my experience working in AI for the last 
few years.



You can checkout the framework here: [https://github.com/palico-ai/palico-ai](https://github.com/palico-ai
/palico-ai)



Would love any feedback!
```
---

     
 
all -  [ AI Agent Stack  ](https://www.reddit.com/r/LangChain/comments/1grhpfz/ai_agent_stack/) , 2024-11-15-0913
```
Hi all - recently I got triggered by seeing the the Nth “AI agent stack”/”AI agents market map” made by a VC features a 
bunch of companies I’ve never heard up in categories that make no sense. [Sharing what I see as the real “agents stack”]
(https://www.letta.com/blog/ai-agents-stack), from the perspective of having been building an agents framework and worki
ng with a lot of different providers for components like LLMs, tool calling, storage, and sandboxing.

https://preview.r
edd.it/mehxo2w55y0e1.jpg?width=5100&format=pjpg&auto=webp&s=5e684f8f64485a551e22557ed0f1effd3cd9cd7e

In my opinion, tod
ay’s tech stack for building AI agents into three key layers: (1) agent hosting/serving, (2) agent frameworks, (3) LLM m
odels & storage.

The (3) LLM model and storage layer is now relatively static - I don’t see a lot of new players, and t
here are clear winners in segments of the market.

For (2) agent frameworks, there’s been a ton of development in the pa
st 6 months in both general purpose frameworks, as well as specialized components (e.g. tool-use, sandboxing, and memory
). I think as the space matures we’ll see a lot more players here, and even more specialization - over time, agents will
 probably be built from modular components leveraging different providers.

The layer of the stack thats still the most 
“up in the air” is hosting (1) - different frameworks have taken very different approaches to what a hosted agent should
 look like, from how agent state (e.g. memories, message history, user data, etc.) are persisted, the API for interactin
g with agents is, and approach to handling tool execution (arbitrary code the agent can call).

I'm sure I missed come c
ool projects, so would love to learn if there's other agent hosting/tool frameworks out there since it was quite sparse 
when we did our research. 
```
---

     
 
all -  [ [10 YoE, Employed, Sr. Software Engineer, United States] ](https://www.reddit.com/gallery/1grhlhs) , 2024-11-15-0913
```

```
---

     
 
all -  [ Scaling issue  ](https://www.reddit.com/r/LangChain/comments/1grhle1/scaling_issue/) , 2024-11-15-0913
```
Hi, I’m a bit new to the LLM sphere. I’m creating software that a lot of users will use, for instance with GPT-4. My und
erstanding is that, since I’m using only one API key, there’s a token limit. I was wondering, how do other companies sca
le when they might have thousands of users? Do they get an API key for each user, or how does that work?
```
---

     
 
all -  [ Why use LangChain?  ](https://www.reddit.com/r/LangChain/comments/1greyeu/why_use_langchain/) , 2024-11-15-0913
```
Genuinely don't know the answer. I've built agents that call functions and retrieve information, multi-agent systems tha
t work together to execute tasks involving conversing with a user. It's just not clear to me why LangChain is better tha
n just using the API's directly. Does it just give you abstractions that require less code? How much less code? Does it 
give new features that you don't get with openai/anthropic API's? Appreciate any insights. I'm coding in python, in case
 makes a difference
```
---

     
 
all -  [ Arch 0.1.2 released 🎉 - AI-native, open source infrastructure to build agents ](https://www.reddit.com/r/LangChain/comments/1grduug/arch_012_released_ainative_open_source/) , 2024-11-15-0913
```
[https://github.com/katanemo/arch](https://github.com/katanemo/arch) \- is an AI-native infrastructure primitive to buil
d fast, personalized agents using APIs. Specifically, Arch is an intelligent prompt gateway designed to protect, observe
, and personalize LLM applications (agents, assistants, co-pilots) with your APIs.

Engineered with purpose-built LLMs, 
Arch handles the critical but undifferentiated tasks related to the handling and processing of prompts, including detect
ing and rejecting [jailbreak](https://github.com/verazuo/jailbreak_llms) attempts, intelligently calling 'backend' APIs 
to fulfill the user's request represented in a prompt, routing to and offering disaster recovery between upstream LLMs, 
and managing the observability of prompts and LLM interactions in a centralized way.

Arch is built on (and by the core 
contributors of) [Envoy Proxy](https://www.envoyproxy.io/) with the belief that:

>

**Core Features**:

* Built on [Env
oy](https://envoyproxy.io): Arch runs alongside application servers, and builds on top of Envoy's proven HTTP management
 and scalability features to handle ingress and egress traffic related to prompts and LLMs.
* Function Calling for fast 
Agents and RAG apps. Engineered with purpose-built [LLMs](https://huggingface.co/collections/katanemo/arch-function-66f2
09a693ea8df14317ad68) to handle fast, cost-effective, and accurate prompt-based tasks like function/API calling, and par
ameter extraction from prompts.
* Prompt [Guard](https://huggingface.co/collections/katanemo/arch-guard-6702bdc08b889e4b
ce8f446d): Arch centralizes prompt guardrails to prevent jailbreak attempts and ensure safe user interactions without wr
iting a single line of code.
* Traffic Management: Arch routes outbound LLM calls to OpenAI (and other LLMs), offering s
mart retries, automatic cutover, and resilient upstream connections for continuous availability.
* Standards-based Obser
vability: Arch uses the W3C Trace Context standard to enable complete request tracing across applications, ensuring comp
atibility with observability tools, and provides metrics to monitor latency, token usage, and error rates, helping optim
ize AI application performance.
```
---

     
 
all -  [ Prove me wrong - An agent is just a convenient abstraction over an LLM ](https://www.reddit.com/r/LangChain/comments/1grcjpa/prove_me_wrong_an_agent_is_just_a_convenient/) , 2024-11-15-0913
```
Hi!

I have not been convinced yet that 'agents' provide any inherent value themselves other than providing a wrapper ar
ound LLMs that contain some state (prompts, context, etc) and/or logic (call back functions otherwise called 'tools'). B
efore agents were released, we were all writing classes that encapsulated this state/logic - a typical exercise to perfo
rm around any model. 

The hype definitely helped push the industry forward while there was slowing progress in terms of
 base models, however, I am reluctant to take a dependency on any new 'agents' framework into my code base when we can a
chieve the same results with little work. 
```
---

     
 
all -  [ Langsmith API Keys. Per project or Per Workspace? ](https://www.reddit.com/r/LangChain/comments/1gra9h9/langsmith_api_keys_per_project_or_per_workspace/) , 2024-11-15-0913
```
Apologies if this is a dumb/beginner question.

I'm trying to change the project my traces are being sent to dynamically
. I'm working with a Typescript project. As far as I'm aware I can only set my LANGCHAIN\_API\_KEY once in my .env file,
 but each project I create gives me a different key. Am I able to update the API Key at the same point I decide which pr
oject name to choose? Am I supposed to use the API Key for my workspace (I tried this and it doesn't seem to work).

Bas
ically it seems I need to dynamically set the project name and project API key. I can set the project name in the  trace
able function but I'm not sure how to do the api key or if I'm misunderstanding and dont need to.
```
---

     
 
all -  [ How to duplicate chroma db or persist directory  ](https://www.reddit.com/r/LangChain/comments/1gr8e7u/how_to_duplicate_chroma_db_or_persist_directory/) , 2024-11-15-0913
```
Need to create Mutiple chroma db based on the same documents.
Tried to copy the persist directory, but the vector db cre
ated from copied directory is always empty
```
---

     
 
all -  [ Production RAG for CSV/Excel  ](https://www.reddit.com/r/LangChain/comments/1gr7msw/production_rag_for_csvexcel/) , 2024-11-15-0913
```
Hi,

I am trying to implement a CSV/Excel RAG using Langchain. Intially implemented using csvgent from langchaain. But t
his time I want it for production environment.

What is the best approach for implementing CSV RAG,  text-to-sql, or by 
Graph RAG, or any other approaches. 

Thanks
```
---

     
 
all -  [ Evaluating the Risks of Releasing an Agentic System on Large Scale Database ](https://www.reddit.com/r/LangChain/comments/1gr7fog/evaluating_the_risks_of_releasing_an_agentic/) , 2024-11-15-0913
```
Hey LangChain community! Just coming here to ask a question and for some opinions or advice.

I'm building a Reporting A
ssistant. The vision is that I will use LangGraph to create something along the lines of this https://blog.langchain.dev
/data-viz-agent/ - Basically an agentic system that allows users to communicate with their data and create visualization
s. The agentic system throughout it's many nodes will generate a SQL query based on the DB schema and user's request in 
natural language, execute it, and then display a graph and allow the user to further iterate on that graph using natural
 language. I have an initial attempt at the SQL generation in place and it is working successfully on a small dataset.


From here, I am just considering the risks more seriously of opening up a database to users like this. I have concerns a
bout the potential for this system generating (regardless of however much prompt engineering that I use) heavy queries, 
things like SQL injection, invalid SQL queries, the ability to query out outside of the user's account's scope, etc. 

I
 will have guardrails in place wherever I can think (for example I have a node to validate + optimize the generated SQL 
query, and two other conditional nodes to validate structured outputs for 2 specific nodes in my graph) + I will have so
me system guardrails with AWS Bedrock in place + most likely guardrails on top of guardrails to validate outputs with th
is being a high stakes project that needs to work and be reliable. Do you think that with the current state of models to
day and the inevitable unpredictability (however rare) that attempting this using a LLM agentic system could be a viable
 solution/product for a large scale production database?
```
---

     
 
all -  [ Am I using Hugging Face wrong? Very slow in embedding ](https://www.reddit.com/r/LangChain/comments/1gr66r2/am_i_using_hugging_face_wrong_very_slow_in/) , 2024-11-15-0913
```
I am working on a RAG chatbot which answers user questions with the content of a PDF file uploaded. I am used to pulling
 models from Ollama and have always been satisfied with the speed, whether it is to do embedding or use a LLM to generat
e answer. Now I am trying Hugging Face, because a specific embedding model (danielheinz/e5-base-sts-en-de) is only on Hu
gging Face, not on Ollama. I followed the instruction here: [Hugging Face | 🦜️🔗 LangChain](https://python.langchain.com/
docs/integrations/text_embedding/huggingfacehub/): 

`pip install sentence_transformer`

`from langchain_huggingface.emb
eddings import HuggingFaceEmbeddings`

`...`

`vectorstore1 = FAISS.from_documents(`

`documents = splits1,` 

`embeddin
g = HuggingFaceEmbeddings(model_name='danielheinz/e5-base-sts-en-de')`

`)`

`vectorstore1.save_local(persist_directory)
`

`...`

It took VERY LONG to finish embedding, for a PDF file with 150 pages, it took about 4 minutes. In comparation,
 using a model from OllamaEmbeddings, the same procedure was done within 15 seconds.

Now I wonder, if I am using Huggin
g Face the right way? Do I need to pre-download anything (I currently have not downloaded anything, just run the code ab
ove)? Thank you for your answer in advance!
```
---

     
 
all -  [ about LLM and ai agent ](https://www.reddit.com/r/LangChain/comments/1gr4ueo/about_llm_and_ai_agent/) , 2024-11-15-0913
```
I need some guidance.  
After learning the basics of LLM, NLP, and Python, I moved on to LangChain and LangGraph, practi
cing with simple projects in Google Colab.   
At the same time, I'm learning n8n and building workflows based on tutoria
ls and my ideas. The problem is, I want to move forward and build a more advanced project to improve my knowledge of LLM
s and agents, but I'm not sure what to build or what to learn next.   
Could you suggest some ideas or guides on what to
 focus on next? Any advice on what I can build that will be useful in the real world would be appreciated
```
---

     
 
all -  [ Lang chain and lang graph road map ](https://www.reddit.com/r/LangChain/comments/1gr2l3x/lang_chain_and_lang_graph_road_map/) , 2024-11-15-0913
```
Can anyone tell me the resources and roadmap to learn lang chain and lang graph. 
```
---

     
 
all -  [ Is search feature available in some way with the OpenAI API? ](https://www.reddit.com/r/OpenAI/comments/1gr1hh0/is_search_feature_available_in_some_way_with_the/) , 2024-11-15-0913
```
Is the search feature from GPT available in some way within the OpenAI API? If not is there a way to implement it? Like 
a langchain method or something adjacent? 
```
---

     
 
all -  [ Compare two datasets ](https://www.reddit.com/r/LangChain/comments/1gqyby3/compare_two_datasets/) , 2024-11-15-0913
```


I was earlier using this method, [https://python.langchain.com/v0.1/docs/integrations/toolkits/document\_comparison\_t
oolkit/](https://python.langchain.com/v0.1/docs/integrations/toolkits/document_comparison_toolkit/), but it's not compat
ible with the updated version of langchain. All resources also seem to be using the older version, hence any help would 
be appreciated.
```
---

     
 
all -  [ [Question] - Need help with a project ](https://www.reddit.com/r/LangChain/comments/1gqsv1r/question_need_help_with_a_project/) , 2024-11-15-0913
```
I'm working on a project with LLM agents. I am a complete noob with LLMs so please bear with me. 

Context :   
Part A :
  
I have a bunch of agents. Think of these agents as users and there is some context unique to each agent. The prompt f
or each agent here would be more or less the same, except a text variable used in the prompt would change. The problem w
ith this is that I can have an arbitrarily large number of agents. However, I am not looping to give feedback back to th
e agents. 

The processes are as follows :   
Process 1 = User\_i +context\_i -> Agent\_i -> Does something on List X ->
 Value Y  
Process 2 = context(set of all context\_i) + Agent\_generate -> List X 

Here I could probably make use of a 
fixed number of agents like 10 and just have them rotate through all the users because we are only concerned with the Va
lue Y from each agent.   


Questions:   
1. Could I run these agents in parallel? If yes, are there any resources that 
I could refer to? Also, my default option would be to use Ollama 3.2 locally on my MBP(2022) M2 Chip with 8GB RAM. Howev
er, I think this might pose a problem as the number of users grows. Is it a good idea to go further with this idea or sh
ould I use OpenAI? 

Part B:   
The same situation as above but now we are adding a new process :   
  
def main\_proces
s(user\_set, context\_set):  
\# Step 1: Generate agent and List X based on combined context (Process 2)  
agent\_genera
te = generate\_agent(context\_set)  
list\_X\_ = generate\_list\_X(agent\_generate)  
  
\# Step 2 & Step 3: For each us
er, initialize agent, operate on List X, check A condition to trigger Process 3  
results = \[\]  
for user, context in 
user\_set:  
agent = initialize\_agent(user, context)  
result\[agent\] = operate\_on\_list\_X\_Cond(agent)  
  
   \# C
heck and trigger Process 3 if condition A is met  
   if calculate\_metric\_A(results\_X) < 90:  
list\_X = agent\_gener
ate(list\_X)  
  
\# Process 4: Operate on List X' and calculate final metrics A' and B'  
result\_X = operate\_on\_list
\_X\_prime(agent, list\_X)  
return results

Questions :   
1. Is there a better way to do part B? Because I am using ag
ent\_i to validate and calculate scores I need to have as many agents as I have users. This could be troublesome. Is the
re a neat way to do this?

2. I would really appreciate it if I could get pointers to terms that I can look up to implem
ent these experiments better. For, example, I think langchain might be something that could help me. Again the documenta
tion seems more advanced and I feel like I might not need. Can you help me scope the project tools and the things I woul
d need?
```
---

     
 
all -  [ How to choose device for vector store similarity search and reranking ](https://www.reddit.com/r/LangChain/comments/1gqlu01/how_to_choose_device_for_vector_store_similarity/) , 2024-11-15-0913
```
Hi, I'm new to langchain or genai tools, so I'm trying to understand how things work..

I don't know why a similarity se
arch on a vectorstore (I used faiss-cpu with langchain) and reranking using RankLLMRerank & ContextualCompressionRetriev
er would use my local gpu by default. 

For embeddings model while building vector store, it seemed that the embedding m
odel is downloaded and cached locally (not sure if it's general behavior or because I was using embedding model from hug
ging face).

Is it langchain side or something else (faiss etc) that requires local run of those model? Is there any oth
er way exist?

I get that it's advantageous to have gpu when loading and running models locally, but I'd like to know if
 it can also work with cpu only as my instance in cloud may not have gpu (just by choice).

Is it possible to choose dev
ice to cpu only? Would it be prohibitively slow?



  

```
---

     
 
all -  [ Complex PDF analysis  ](https://www.reddit.com/r/LangChain/comments/1gqliqq/complex_pdf_analysis/) , 2024-11-15-0913
```
Hi guys

 I'm looking to build an app that uses a PDF as a knowledge base and allows users to upload additional PDFs. Th
e goal is for the app to provide responses based on the combined content of these PDFs. The documents are quite long (ar
ound 100 pages) and are in Polish.

I attempted to use the OpenAI Playground to upload PDFs for Assistants, but it faile
d miserably. 

I'm new to AI and unsure whether to use something like LangChain or another tool. I came across tools lik
e Upstage, which seems to be a bit better.

 I know how to code and will manage to follow any stack needed.

 Could anyo
ne suggest what tools or frameworks I should use to build this app? 

Thanks!
```
---

     
 
all -  [ Read only vector database ](https://www.reddit.com/r/LangChain/comments/1gqkxck/read_only_vector_database/) , 2024-11-15-0913
```
Hi I’m planning on having a feature to allow people to query my vector database but not add anything. I was wondering if
 there is a vector database which allows me to share my db API key(or any token) and allow people to just query it for a
nswers without altering it. 
```
---

     
 
all -  [ [2 YOE] Master's in CS student: Not getting any callbacks for summer 2025 internship ](https://www.reddit.com/r/EngineeringResumes/comments/1gqjohb/2_yoe_masters_in_cs_student_not_getting_any/) , 2024-11-15-0913
```
Barely receiving any callbacks, having applied to at least 200 roles. Being an international student, I understand needi
ng visa sponsorship plays a big factor. However, I want to make sure that I am doing everything right as far as my resum
e is concerned.

I am currently in the first year of my master's degree and have been applying to internships since July
. The only OA's I have received are from HFT's, which I suspect are sent automatically right after application. I have b
een applying to positions everywhere and have no issues with relocation or remote work. I have not restricted my applica
tions in any way and have been applying to positions at big tech, startup, non-tech firms and any organization that has 
opened up roles for Summer 2025 internships

Please let me know what I can improve on my resume

https://preview.redd.it
/dgffmb5lop0e1.png?width=5100&format=png&auto=webp&s=e40dbcd4a9df06a2b0bf79f7e6f684afcc74c2e5


```
---

     
 
all -  [ What’s you RAG stack? ](https://www.reddit.com/r/LangChain/comments/1gqi9le/whats_you_rag_stack/) , 2024-11-15-0913
```
Planning to build RAG functionality in my app, looking for cost effective but simple solution. Would be great to know wh
at’s your RAG tech stack? Components? Loaders? Integrations you are using? How much is it costing? 
Any insights would b
e very helpful thanks 
```
---

     
 
all -  [ Introducing Langchian-Beam  ](https://www.reddit.com/r/dataengineering/comments/1gqhw0w/introducing_langchianbeam/) , 2024-11-15-0913
```
Hi all, I've been working on a Apache beam and langchian integration and would like to share it here.

Apache beam is a 
great model for data processing. It provides abstractions to create data processing logic as components that can be appl
ied on data in batch and stream processing ETL pipelines 

langchian-beam integrates LLMs into the apache beam pipeline 
using langchian to use LLMs capabilities for data processing, transformations and RAG. 

Would like to hear any feedback
, suggestions and am interested in collaborating on Langchain-Beam!

Repo link - https://github.com/Ganeshsivakumar/lang
chain-beam
 
```
---

     
 
all -  [ [Student] Software Engineering grad applying for SWE full time roles - need help with my resume ](https://www.reddit.com/r/EngineeringResumes/comments/1gqgxwi/student_software_engineering_grad_applying_for/) , 2024-11-15-0913
```
Below is my existing resume that I am using to apply to full time SWE roles (new grad) and I feel like I could use some 
help from people of this sub as I'm not sure what additional changes I need to make as I've been tweaking my resume mult
iple times but no luck with any of the applications - haven't heard back from the companies I have applied to so far, an
y feedback is greatly appreciated - do your best(or worst lol). Thanks in advance!

https://preview.redd.it/3n9blj344p0e
1.jpg?width=5100&format=pjpg&auto=webp&s=4c3814187113415dfc55b3cedf265888561006cf
```
---

     
 
all -  [ Python, caricare PDF usando una gui e porter legger il contenuto attraverso un codice QR,  ](https://www.reddit.com/r/LangChain/comments/1gqe1bf/python_caricare_pdf_usando_una_gui_e_porter/) , 2024-11-15-0913
```
Buongiorno a tutti, sto scrivendo con CHATGPT un codice in Pyhton per caricare un qualsiasi PDF ( fino a 2000 caratteri 
) usando una Gui come ausilio, il contenuto dovrebbe poi esser letto attraverso un codice QR. Uso la libreria PyMuPDF. N
on c' è verso, per una ragione o l' altra non mi carica i PDF, esempio finestrella errore: pagina vuota, contenuto non r
isponde a ..., ecc.ecc. Consigli?


```
---

     
 
all -  [ RAG for Documents ](https://www.reddit.com/r/LangChain/comments/1gqd7am/rag_for_documents/) , 2024-11-15-0913
```
Hi everyone!

I have a startup that develops RAG systems for documents (i.e. contracts, RFPs, technical guides, educatio
nal materials, etc). I'm not here to promote it but to ask your honest opinions.

We've created a proprietary RAG framew
ork for documents integrated with LangChain. I believe the advantages are:

1. it uses hybrid search (vector + keyword);

2. vector search uses embeddings generated by models that we've fine-tuned;
3. Results are ranked using models that we'
ve also fine-tuned;
4. It's highly customizable, and we can change search steps, switch models used for embeddings and r
anking, etc.
5. It's scalable, and we can run in multiple nodes using microservices (i.e. our framework is running in a 
client with more than 5 million legal docs).

This framework is not open so we currently use it only to gain productivit
y in our projects so we can deploy a 'chat-gpt like' solution for our clients data in 1-2 months.

Do you think this kin
d of framework is interesting? Or the features I mentioned would be something you prefer to implement by yourself or usi
ng some other library?

Also, do you think I should focus on developers and commercialize this framework or open source 
it and monetize it somehow? Or perhaps should I stay with my current business model and just address end users?
```
---

     
 
all -  [ Sementic Chunking vs RAPTOR ](https://www.reddit.com/r/LangChain/comments/1gqd4y7/sementic_chunking_vs_raptor/) , 2024-11-15-0913
```
I am confused, which works better for Large Documents(50,000 Pages)? any experience?
```
---

     
 
all -  [ can I create a conditional edge that can rerun my previous node with corrections specified? ](https://www.reddit.com/r/LangChain/comments/1gqang9/can_i_create_a_conditional_edge_that_can_rerun_my/) , 2024-11-15-0913
```
https://preview.redd.it/ucv9zcf4kn0e1.png?width=1152&format=png&auto=webp&s=1ec0f09562439f9fd8911a4021eeccbc96df804e

Th
is is my directional graph. Where response from my output goes from Dev to Test and then end.  
Can implement as i menti
oned in the image that if there is a test case that fails...the dev can correct its code properly?  
please can someone 
guide me?
```
---

     
 
all -  [ Parsing complex pdf tables  ](https://www.reddit.com/r/LocalLLaMA/comments/1gqa3zk/parsing_complex_pdf_tables/) , 2024-11-15-0913
```
Hello,

I'd like to parse complex pdf consisting of numerous tables, such as the following :

Each symbol correspond to 
a symbol description. Ideally I'd like to have a structured JSON with key/values corresponding to the content of each ta
bles. Like I'd like to have a key 'symbol information' containing a dict, which will contains keys 'symbol  graphic name
' but also three different dicts for each sub-element, and then another dict for symbol portrayal rules and another one 
for label information.

I tried Langchain (qwen 2.5 32b) with pydantic, it seems to work on some pages but it fails on o
ther when there are really big text paragraphs in some fields. I guess this is because it only relies on pure text witho
ut any visual cue of how the text is spatially distributed in the pdf and its getting confused... Do you have any advice
 ?

https://preview.redd.it/4co4hit5en0e1.png?width=659&format=png&auto=webp&s=0d7587b0e2736349f6b725279fb33b19d81e435c
```
---

     
 
all -  [ Udemy Free Courses for 13 November 2024 ](https://www.reddit.com/r/udemyfreeebies/comments/1gq9rhs/udemy_free_courses_for_13_november_2024/) , 2024-11-15-0913
```
# Udemy Free Courses for 13 November 2024

Note : Coupons might expire anytime, so enroll as soon as possible to get the
 courses for FREE.

* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24078/)Mastering Pointers in C : A Course on Eff
icient Programming
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24077/)2024 C++ Programming : Beginners to Advanc
ed for Developers
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24076/)Project Management Professional Certificati
on
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24075/)Women Leaders Executive Programme
* [REDEEM OFFER ](https:
//idownloadcoupon.com/udemy/24074/)Executive Diploma in Marketing Management
* [REDEEM OFFER ](https://idownloadcoupon.c
om/udemy/24073/)Lean Six Sigma Green Belt Professional Certification
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy
/24072/)Analyse 1 : CPGE / ENSA / ENSAM / FST
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24071/)CLF-C02 AWS Cer
tified Cloud Practitioner | Practice Exams
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24070/)Scrum Master Profe
ssional Certification
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24069/)AWS Certified SysOps Administrator Asso
ciate PRACTICE EXAM
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24068/)Digital Marketing Professional Certificat
ion
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24067/)Web Development Professional Certification
* [REDEEM OFFE
R ](https://idownloadcoupon.com/udemy/24066/)SAA-C03 AWS Certified Solutions Architect Associate Practice
* [REDEEM OFFE
R ](https://idownloadcoupon.com/udemy/24065/)AZ-900: Microsoft Azure Fundamentals Practice Exam
* [REDEEM OFFER ](https:
//idownloadcoupon.com/udemy/24064/)Comprehensive Data Structures & Algorithms Practice
* [REDEEM OFFER ](https://idownlo
adcoupon.com/udemy/24063/)Advanced Skill Test: Associate Python Programmer (PCAP™)
* Professional Diploma in Copywriting
 and Business Writing
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/24062/)
* [REDEEM OFFER ](https://idownloadcoup
on.com/udemy/24061/)Motion Magic: Crafting Visual Masterpieces in After Effects
* [REDEEM OFFER ](https://idownloadcoupo
n.com/udemy/24060/)Selenium Webdriver Automation Testing \[Live Projects 2024\]
* [REDEEM OFFER ](https://idownloadcoupo
n.com/udemy/24059/)The Logo Design Expert Course in Adobe Illustrator CC.
* [REDEEM OFFER ](https://idownloadcoupon.com/
udemy/24058/)Adobe Photoshop and Firefly 2 in 1 Mega Course for Newbies
* [REDEEM OFFER ](https://idownloadcoupon.com/ud
emy/24057/)Google Cloud Professional Cloud Architect: GCP Certification
* [REDEEM OFFER ](https://idownloadcoupon.com/ud
emy/24056/)Software Career Bootcamp: Recession, Layoff and AI Challenge
* [REDEEM OFFER ](https://idownloadcoupon.com/ud
emy/24055/)Creative Beginnings: Photoshop & Illustrator Essentials-2in1
* [REDEEM OFFER ](https://idownloadcoupon.com/ud
emy/24054/)Adobe Illustrator Advanced Professional Course
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24053/)Ado
be Photoshop CC for Photo Editing and Image Retouching
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24052/)Adobe 
Photoshop CC Complete Mastery Course Basic to Advanced
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24051/)Execut
ive Diploma in Finance Management
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24050/)The Complete Java Course: F
rom Basics to Advanced
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24049/)AWS Certified Data Engineer – Associat
e PRACTICE EXAM
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24048/)PHP Bootcamp: The Complete Programming Course
 With MYSQL
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24047/)SQL, MYSQL, POSTGRESQL & MONGODB: All-in-One Data
base Course
* NumPy, Pandas, & Python for Data Analysis: A Complete Guide
* [REDEEM OFFER](https://idownloadcoupon.com/u
demy/24046/)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24045/)H2O Gen AI Ecosystem Overview – Level 1
* [REDEE
M OFFER ](https://idownloadcoupon.com/udemy/24044/)H2O Gen AI Ecosystem Overview – Level 2
* [REDEEM OFFER ](https://ido
wnloadcoupon.com/udemy/24043/)ChatGPT Side Hustles for Beginners: Make Money with ChatGPT
* [REDEEM OFFER ](https://idow
nloadcoupon.com/udemy/24042/)Python Programming: A Step-by-Step Programming Course
* [REDEEM OFFER ](https://idownloadco
upon.com/udemy/24041/)Learn Python Programming with ChatGPT
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24040/)A
dvanced Skill Test: Associate Python Programmer (PCAP™)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24039/)Compl
ete Ethical Hacking Masterclass: Go from Zero to Hero
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24038/)Python 
Programming: Build a Strong Foundation in Coding
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24037/)Learn PHP Pr
ogramming: Create Dynamic Websites with MYSQL
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24036/)Swing Trading G
uide: How to Make Money Swing Trading
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24035/)Linux for Cloud Enginee
rs and Devops
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24034/)Business Administration Executive Certification

* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24033/)Microsoft Excel – Excel Course For Beginners
* [REDEEM OFFER
 ](https://idownloadcoupon.com/udemy/24032/)Body Language: Appear Confident and Poised When You Speak
* [REDEEM OFFER ](
https://idownloadcoupon.com/udemy/24031/)DevOps MasterClass 2024: Terraform Kubernetes Ansible Docker
* Financial Analys
t Professional Certification
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/24030/)
* [REDEEM OFFER ](https://idownl
oadcoupon.com/udemy/24029/)Easy Ways to Make Money Online with ChatGPT for Beginners
* [REDEEM OFFER ](https://idownload
coupon.com/udemy/24028/)SAP C\_IBP\_2311: IBP for Supply Chain | Real Exam Dumps
* [REDEEM OFFER ](https://idownloadcoup
on.com/udemy/24027/)SAP C\_HRHPC\_2405: SuccessFactors Central Payroll | Exam Dump
* [REDEEM OFFER ](https://idownloadco
upon.com/udemy/24026/)Advanced Skill Test: Python Professional Level 1 (PCPP1™)
* [REDEEM OFFER ](https://idownloadcoupo
n.com/udemy/24025/)Information Security Professional Certification
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/2
4024/)Zero to Hero in LangChain: Build GenAI apps using LangChain
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24
023/)Zero to Hero in Ollama: Create Local LLM Applications

GET MORE FREE ONLINE COURSES WITH CERTIFICATE – [CLICK HERE]
(https://idownloadcoupon.com/)
```
---

     
 
all -  [ Udemy Free Courses for 13 November 2024 ](https://www.reddit.com/r/udemyfreebies/comments/1gq9rg2/udemy_free_courses_for_13_november_2024/) , 2024-11-15-0913
```
# Udemy Free Courses for 13 November 2024

Note : Coupons might expire anytime, so enroll as soon as possible to get the
 courses for FREE.

* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24078/)Mastering Pointers in C : A Course on Eff
icient Programming
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24077/)2024 C++ Programming : Beginners to Advanc
ed for Developers
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24076/)Project Management Professional Certificati
on
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24075/)Women Leaders Executive Programme
* [REDEEM OFFER ](https:
//idownloadcoupon.com/udemy/24074/)Executive Diploma in Marketing Management
* [REDEEM OFFER ](https://idownloadcoupon.c
om/udemy/24073/)Lean Six Sigma Green Belt Professional Certification
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy
/24072/)Analyse 1 : CPGE / ENSA / ENSAM / FST
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24071/)CLF-C02 AWS Cer
tified Cloud Practitioner | Practice Exams
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24070/)Scrum Master Profe
ssional Certification
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24069/)AWS Certified SysOps Administrator Asso
ciate PRACTICE EXAM
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24068/)Digital Marketing Professional Certificat
ion
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24067/)Web Development Professional Certification
* [REDEEM OFFE
R ](https://idownloadcoupon.com/udemy/24066/)SAA-C03 AWS Certified Solutions Architect Associate Practice
* [REDEEM OFFE
R ](https://idownloadcoupon.com/udemy/24065/)AZ-900: Microsoft Azure Fundamentals Practice Exam
* [REDEEM OFFER ](https:
//idownloadcoupon.com/udemy/24064/)Comprehensive Data Structures & Algorithms Practice
* [REDEEM OFFER ](https://idownlo
adcoupon.com/udemy/24063/)Advanced Skill Test: Associate Python Programmer (PCAP™)
* Professional Diploma in Copywriting
 and Business Writing
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/24062/)
* [REDEEM OFFER ](https://idownloadcoup
on.com/udemy/24061/)Motion Magic: Crafting Visual Masterpieces in After Effects
* [REDEEM OFFER ](https://idownloadcoupo
n.com/udemy/24060/)Selenium Webdriver Automation Testing \[Live Projects 2024\]
* [REDEEM OFFER ](https://idownloadcoupo
n.com/udemy/24059/)The Logo Design Expert Course in Adobe Illustrator CC.
* [REDEEM OFFER ](https://idownloadcoupon.com/
udemy/24058/)Adobe Photoshop and Firefly 2 in 1 Mega Course for Newbies
* [REDEEM OFFER ](https://idownloadcoupon.com/ud
emy/24057/)Google Cloud Professional Cloud Architect: GCP Certification
* [REDEEM OFFER ](https://idownloadcoupon.com/ud
emy/24056/)Software Career Bootcamp: Recession, Layoff and AI Challenge
* [REDEEM OFFER ](https://idownloadcoupon.com/ud
emy/24055/)Creative Beginnings: Photoshop & Illustrator Essentials-2in1
* [REDEEM OFFER ](https://idownloadcoupon.com/ud
emy/24054/)Adobe Illustrator Advanced Professional Course
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24053/)Ado
be Photoshop CC for Photo Editing and Image Retouching
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24052/)Adobe 
Photoshop CC Complete Mastery Course Basic to Advanced
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24051/)Execut
ive Diploma in Finance Management
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24050/)The Complete Java Course: F
rom Basics to Advanced
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24049/)AWS Certified Data Engineer – Associat
e PRACTICE EXAM
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24048/)PHP Bootcamp: The Complete Programming Course
 With MYSQL
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24047/)SQL, MYSQL, POSTGRESQL & MONGODB: All-in-One Data
base Course
* NumPy, Pandas, & Python for Data Analysis: A Complete Guide
* [REDEEM OFFER](https://idownloadcoupon.com/u
demy/24046/)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24045/)H2O Gen AI Ecosystem Overview – Level 1
* [REDEE
M OFFER ](https://idownloadcoupon.com/udemy/24044/)H2O Gen AI Ecosystem Overview – Level 2
* [REDEEM OFFER ](https://ido
wnloadcoupon.com/udemy/24043/)ChatGPT Side Hustles for Beginners: Make Money with ChatGPT
* [REDEEM OFFER ](https://idow
nloadcoupon.com/udemy/24042/)Python Programming: A Step-by-Step Programming Course
* [REDEEM OFFER ](https://idownloadco
upon.com/udemy/24041/)Learn Python Programming with ChatGPT
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24040/)A
dvanced Skill Test: Associate Python Programmer (PCAP™)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24039/)Compl
ete Ethical Hacking Masterclass: Go from Zero to Hero
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24038/)Python 
Programming: Build a Strong Foundation in Coding
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24037/)Learn PHP Pr
ogramming: Create Dynamic Websites with MYSQL
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24036/)Swing Trading G
uide: How to Make Money Swing Trading
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24035/)Linux for Cloud Enginee
rs and Devops
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24034/)Business Administration Executive Certification

* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24033/)Microsoft Excel – Excel Course For Beginners
* [REDEEM OFFER
 ](https://idownloadcoupon.com/udemy/24032/)Body Language: Appear Confident and Poised When You Speak
* [REDEEM OFFER ](
https://idownloadcoupon.com/udemy/24031/)DevOps MasterClass 2024: Terraform Kubernetes Ansible Docker
* Financial Analys
t Professional Certification
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/24030/)
* [REDEEM OFFER ](https://idownl
oadcoupon.com/udemy/24029/)Easy Ways to Make Money Online with ChatGPT for Beginners
* [REDEEM OFFER ](https://idownload
coupon.com/udemy/24028/)SAP C\_IBP\_2311: IBP for Supply Chain | Real Exam Dumps
* [REDEEM OFFER ](https://idownloadcoup
on.com/udemy/24027/)SAP C\_HRHPC\_2405: SuccessFactors Central Payroll | Exam Dump
* [REDEEM OFFER ](https://idownloadco
upon.com/udemy/24026/)Advanced Skill Test: Python Professional Level 1 (PCPP1™)
* [REDEEM OFFER ](https://idownloadcoupo
n.com/udemy/24025/)Information Security Professional Certification
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/2
4024/)Zero to Hero in LangChain: Build GenAI apps using LangChain
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/24
023/)Zero to Hero in Ollama: Create Local LLM Applications

GET MORE FREE ONLINE COURSES WITH CERTIFICATE – [CLICK HERE]
(https://www.reddit.com/r/udemyfreeebies/)
```
---

     
 
all -  [ Help! Need a study partner for learning LLM'S. I know few resources ](https://www.reddit.com/r/LLMDevs/comments/1gq8a5a/help_need_a_study_partner_for_learning_llms_i/) , 2024-11-15-0913
```
Hello LLM Bro's,  
  
I’m a Gen AI developer with experience building chatbots using retrieval-augmented generation (RAG
) and working with frameworks like LangChain and Haystack. Now, I’m eager to dive deeper into large language models (LLM
s) but need to boost my Python skills. I’m looking for motivated individuals who want to learn together.I’ve gathered re
sources on LLM architecture and implementation, but I believe I’ll learn best in a collaborative online environment. Com
munity and accountability are essential!If you’re interested in exploring LLMs—whether you're a beginner or have some ex
perience—let’s form a dedicated online study group. Here’s what we could do:

* Review the latest LLM breakthroughs
* Wo
rk through Python tutorials
* Implement simple LLM models together
* Discuss real-world applications
* Support each othe
r through challenges

Once we grasp the theory, we can start building our own LLM prototypes. If there’s enough interest
, we might even turn one into a minimum viable product (MVP).I envision meeting 1-2 times a week to keep motivated and m
ake progress—while having fun!This group is open to anyone globally. If you’re excited to learn and grow with fellow LLM
 enthusiasts, shoot me a message! Let’s level up our Python and LLM skills together!
```
---

     
 
all -  [  Need Help Optimizing Document Retrieval in LangChain for RAG App ](https://www.reddit.com/r/LangChain/comments/1gq77ub/need_help_optimizing_document_retrieval_in/) , 2024-11-15-0913
```
Hey everyone!



I’m building a Retrieval-Augmented Generation (RAG) application using LangChain and could use some help
 optimizing my document retrieval strategy.



The Setup:

I started with an ensemble retriever using Hybrid Search, whi
ch combines TF-IDF for keyword search with other methods. The problem is that it struggles to return relevant documents 
when questions are rephrased, likely because TF-IDF focuses on exact keyword matches rather than semantic similarity.




I then tried the multi-query retriever, and while it improved relevance, it came with two issues:



Longer retrieval t
imes: It’s noticeably slower.

High token count: The retrieved documents are too large, making the overall process a bit
 inefficient.

What I’m Looking For:

An ideal solution would handle rephrased or semantically similar questions effecti
vely while also keeping retrieval times low and token counts manageable.



Has anyone faced something similar or found 
an effective retrieval approach within LangChain that balances relevance, speed, and token efficiency? Any tips, alterna
te retrievers, or other optimizations would be super helpful!



Thanks in advance!
```
---

     
 
all -  [ Multimodal RAG ](https://www.reddit.com/r/LangChain/comments/1gq6s1v/multimodal_rag/) , 2024-11-15-0913
```
Currently I'm working on a project 'Car Companion' in this project I've used unstructured to extract text, tables and im
ages and generate summaries for images and tables using Llama-3.2 vision model and stored all these docs and summaries i
n a chroma vectorstore. It's a time taking process because the manual PDFs contains 100's of pages. It takes a lot of ti
me to extract Text and generate summaries.

Question: Now my question is, how to do all these process on a user uploaded
 pdf?

Should we need to  follow the same text extraction and image summary generation process?

If so, it would take a 
lot of time to process right?

Is there any alternative for this?
```
---

     
 
all -  [ [1 YoE, Full Stack Software Engineer, Full Stack Developer or Software Engineering intern, USA] ](https://i.redd.it/vx0wtvh94m0e1.jpeg) , 2024-11-15-0913
```
As an international student, I’m finding it incredibly challenging to secure an internship, whether it be for winter, su
mmer 2025, or even a one-semester gap year opportunity. I’ve applied to around 400 positions on LinkedIn and other job b
oards. I’ve received about 12-15 online assessments, which I feel I performed well on, but I haven’t managed to secure a
ny interviews. I suspect my resume might be part of the issue.

If anyone could help me review my resume or connect me t
o potential opportunities, I’d be grateful. Internships in my home country or elsewhere in Asia have yielded positive fe
edback, but I am focused on finding an internship in the U.S., which has been incredibly difficult. I feel confused and 
discouraged, like I’m at a loss for what to do next.
```
---

     
 
MachineLearning -  [ [P] Open-source declarative framework to build LLM applications - looking for contributors ](https://www.reddit.com/r/MachineLearning/comments/1gkpazh/p_opensource_declarative_framework_to_build_llm/) , 2024-11-15-0913
```
I've been building LLM-based applications, and was super frustated with all major frameworks - langchain, autogen, crewA
I, etc. They also seem to introduce a pile of unnecessary abstractions. It becomes super hard to understand what's going
 behind the curtains even for very simple stuff.

[So I just published this open-source framework GenSphere.](https://gi
thub.com/octopus2023-inc/gensphere) The idea is have something like **Docker for LLMs**. You build applications with YAM
L files, that define an execution graph. Nodes can be either LLM API calls, regular function executions or other graphs 
themselves. Because you can nest graphs easily, building complex applications is not an issue, but at the same time you 
don't lose control.

You basically code in YAML, stating what are the tasks that need to be done and how they connect. O
ther than that, you only write individual python functions to be called during the execution. No new classes and abstrac
tions to learn.

Its all open-source. **Now I'm looking for contributors** to adapt the framework for cycles and conditi
onal nodes - which would allow full-fledged agentic system building! Pls reach out  if you want to contribute, there are
 tons of things to do!

PS: [you can read the detailed docs here,](https://gensphere.readthedocs.io/en/latest/) And go o
ver this quick [Google Colab tutorial.](https://github.com/octopus2023-inc/gensphere/blob/main/examples/gensphere_tutori
al.ipynb)
```
---

     
 
deeplearning -  [ Fast AI's deep learning for coders by jeremy howard for begginer?  ](https://www.reddit.com/r/deeplearning/comments/1gb2k3p/fast_ais_deep_learning_for_coders_by_jeremy/) , 2024-11-15-0913
```
I am a full stack python developer who do web dev in django

I am now starting deep learning,i am a compelete begginer


(Have worked with pandas,numpy,matplotlib,langchain only)

I wanna ask,should i do this course,will i understand what he
 is coding and code myslef

I just dont want to do blind coding,i wanna learn what is the purpose,how it works and how t
o do it

Will this course teach me that or not?

Thanks in advance
```
---

     
