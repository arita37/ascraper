 
all -  [ Creating a customized LLM ](https://www.reddit.com/r/LocalLLaMA/comments/1bw1htf/creating_a_customized_llm/) , 2024-04-05-0910
```
I want to know how I should approach this. I am a full-stack developer so I don't have a lot of knowledge on this, but I
 need to build a chatbot for a university application that can give information from the website. I've seen a lot about 
LangChains and Vector databases but not sure what is the starting point for this. Should I scrape information from the w
ebsite to feed or should I create a document with website information before proceeding with this? If someone could tell
 me where to start it would be of great help. The next step would be to integrate this model into a backend API which sh
ould be easy.
```
---

     
 
all -  [ Example of Using an Openrouter Vision Model  ](https://www.reddit.com/r/LangChain/comments/1bw0wxx/example_of_using_an_openrouter_vision_model/) , 2024-04-05-0910
```
I'd like to know if anyone can give me a small example of how to use a vision model like gemini but through the openrout
er api using langchain, or somewhere where I can get this documentation 
```
---

     
 
all -  [ I made a GitHub repo for (beginner) Python devs using LangChain for LLM projects
 ](https://www.reddit.com/r/LangChain/comments/1bw0dke/i_made_a_github_repo_for_beginner_python_devs/) , 2024-04-05-0910
```
I've been hearing a lot from co-students about how difficult langchain sometimes is to implement in a correct way. Becau
se of this, I've created a project that simply follows the main functionalities I personally use in LLM-projects,from no
w 10 months practically only working in LangChain for projects. I've written this in 1 thursday evening before going to 
bed, so I'm not that sure about it, but any feedback is more than welcome!

[https://github.com/lypsoty112/llm-project-s
keleton?tab=readme-ov-file](https://github.com/lypsoty112/llm-project-skeleton?tab=readme-ov-file)
```
---

     
 
all -  [ What all you are making with LLM APIs ](https://www.reddit.com/r/csMajors/comments/1bvzzqj/what_all_you_are_making_with_llm_apis/) , 2024-04-05-0910
```
Hey all
Just curious how you all have been using langchain, LLM apis to make projects, what resources/techstack you all 
been referring to make?
Drop the GitHub links!!!
```
---

     
 
all -  [ Gemini Agent prompt ](https://www.reddit.com/r/PromptEngineering/comments/1bvyb99/gemini_agent_prompt/) , 2024-04-05-0910
```
I am trying to build an agent using LangChain and Gemini with tools. The agent can use tools without any errors, but whe
never I send a greeting message, it gets confused. I am sharing the prompt and Agent's behavior.

prompt:

Decision-maki
ng process for handling questions:

1. \*\*Determine the context:\*\*- If the message is a greeting or a casual conversa
tion starter, respond appropriately.- If the message is not a question or command, accept it as a human message; it migh
t contain important information about the user that you may want to remember.- If the question is related to legal matte
rs, proceed to step 2.- Otherwise, use other tools to answer the question.
2. \*\*Identify relevant countries:\*\*- Chec
k if the question explicitly mentions a country related to law (USA, Canada, Germany, Switzerland, UK, Russia, or Turkey
).
3. \*\*Use PDFs if applicable:\*\*- If a relevant country is identified and a corresponding PDF exists (e.g., 'German
-Law.pdf' for Germany), use that PDF for information retrieval.
4. \*\*External search if no PDF:\*\*- If no relevant co
untry is identified or no corresponding PDF exists, use DuckDuckGo to search for information.
5. \*\*Fallback for non-le
gal or unrelated questions:\*\*- If the question does not fit the legal context or requires a different tool, use the ap
propriate tool from the available set to provide an answer.

&#8203;

    Ask: my name is John
    
    
    > Entering 
new AgentExecutor chain...
    This is a greeting.
    Action: None       
    Action Input: None 
    Observation: None
 is not a valid tool, try one of [duckduckgo_search, google_scholar, wikipedia, arxiv, pub_med, ask_pdf].
    Thought:I 
should greet the user.
    Action: None
    Action Input: None
    Observation: None is not a valid tool, try one of [du
ckduckgo_search, google_scholar, wikipedia, arxiv, pub_med, ask_pdf].
```
---

     
 
all -  [ How to deploy langgraph using langserve? ](https://www.reddit.com/r/LangChain/comments/1bvy2ws/how_to_deploy_langgraph_using_langserve/) , 2024-04-05-0910
```

```
---

     
 
all -  [ RAG aplication ](https://www.reddit.com/r/LangChain/comments/1bvxp42/rag_aplication/) , 2024-04-05-0910
```
Hi all! I am working on a RAG application to which i gave a list of apis and 1-2 lines about that api. I query it and it
 should return the relevant api. The api list is in json format and i save that file as a txt file and generate embeddin
gs. But the problem is its accuracy. Sometimes it gives proper answer and sometime s it says the api is not present in c
ontext. Any idea how to improve its accuracy. How do you guys prompt in RAG applications?
```
---

     
 
all -  [ How best to implement RAG on Government Law Data? ](https://www.reddit.com/r/LocalLLaMA/comments/1bvv28l/how_best_to_implement_rag_on_government_law_data/) , 2024-04-05-0910
```
Hi there,

I'm working on a personal project where I'm implementing a local RAG system on a dataset of government laws, 
which are freely available and in XML format. My goal is to develop a system that can effectively navigate and utilize t
he data to generate accurate and contextually relevant responses. The data includes a ton of interlinking between acts a
nd sections/subsections, such as 'under section 89 (a) of the Liquor Act.' or 'under subsection (7) of this section'.

I
'm considering different combinations of knowledge graphs/graph databases, embeddings, transformers and models. Currentl
y, I'm using Neo4j for the graph database, llamaIndex for embeddings, Sentence Transformer for encoding text, [Mistral-7
B-Instruct-v0.2](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.2) for the model and LangChain Text Splitter fo
r segmenting the data.

I have a few questions and would appreciate any insights:

1. **Knowledge Graphs/Graph Databases
**: How can I effectively use Neo4j or another database to represent the interlinking between different laws and section
s? Are there specific graph modeling techniques or tools that could enhance the retrieval process?
2. **Embeddings & Tra
nsformers**: What are the best practices for generating embeddings in a legal context? How can I ensure that the embeddi
ngs capture the semantic relationships between different laws and sections?
3. **RAG Implementation**: Are there specifi
c strategies or architectures that are particularly effective for implementing RAG on this type of data? How can I optim
ize the retrieval and generation components to handle the complexity of legal texts?
4. **Additional Tools/Techniques**:
 Are there other tools or techniques that you would recommend for handling this type of dataset? Any suggestions for pre
processing, indexing, re-reranking or fine-tuning would be amazing.

Any advice, resources, or examples would be greatly
 appreciated. Thank you in advance!
```
---

     
 
all -  [ New Open Source Project - Looking for contributors ](https://www.reddit.com/r/LLMDevs/comments/1bvtqg7/new_open_source_project_looking_for_contributors/) , 2024-04-05-0910
```
I am starting a new open source project based on configurable and re-usable autonomous agents to achieve a given objecti
ve (which can be anything from simple task to creating an end-to-end business)

The agents will be deployed on centralis
ed / decentralised open/closed Intelligent Agent Mesh that can auto-discover existing agents and collaborate with them u
sing standard agent protocols to get the job done.

Related material to read: [https://medium.com/transforming-the-futur
e/the-future-of-digital-transformation-and-the-role-of-intelligent-adaptive-mesh-iam-c6b29f580067](https://medium.com/tr
ansforming-the-future/the-future-of-digital-transformation-and-the-role-of-intelligent-adaptive-mesh-iam-c6b29f580067)


[https://medium.com/transforming-the-future/future-of-software-development-intelligent-adaptive-mesh-a78db8e9cc66](https
://medium.com/transforming-the-future/future-of-software-development-intelligent-adaptive-mesh-a78db8e9cc66)

If you are
 an experienced python programmer, interested in multi-agent development with LLMs and frameworks such as autogen, super
agi, langchain, and would like to join to founding team, please let me know.
```
---

     
 
all -  [ Conversation summary buffer memory Video ](https://youtu.be/6OJO8YB2KoI) , 2024-04-05-0910
```
In this video, we delve into the intricacies of ConversationBufferMemory in #Langchain, a powerful tool for managing and
 analyzing chat interactions.

#genai #llm #aiml #langchain
```
---

     
 
all -  [ Sentence Similarity algorithms ](https://www.reddit.com/r/LangChain/comments/1bvp6lc/sentence_similarity_algorithms/) , 2024-04-05-0910
```
Which simplest yet effective approaches other than LLMs will be a better approach to have a sentence similarity matching
 algorithm. I am looking at information schemas for having descriptions of columns. Want to get pinpoint column names ba
sed on queries having column descriptions ?
```
---

     
 
all -  [ LangChain Good/Bad Practices ](https://www.reddit.com/r/LangChain/comments/1bvodo8/langchain_goodbad_practices/) , 2024-04-05-0910
```
Hi everybody!

I'm currently trying to figure out what are some common mistakes that people make when developing applica
tions using LangChain. These could be related to security, efficiency or even readability issues.

Would love to hear wh
at kinds of good/bad practices you have picked up on while working with LangChain. Also, if you could point me to any go
od resources on practices to avoid when using LangChain, I would be very appreciative!
```
---

     
 
all -  [ [D] How to get the source documents from the retrieved context for RAG?  ](https://www.reddit.com/r/MachineLearning/comments/1bvoc1t/d_how_to_get_the_source_documents_from_the/) , 2024-04-05-0910
```
I'm not using Lanchain but only making API calls to an LLM service provider. The retriever is connected to a vector DB, 
and I would like to know what the LLM refers to WITHIN that retrieved context whenever it provides an answer, similar to
 how return_source_documents works in Langchain.

I'm using AzureOpenAI. I couldn't find much in their docs that related
 to returning the source documents. Any help will be greatly appreciated!

```
---

     
 
all -  [ RAG with distinct, separate knowledge bases ](https://www.reddit.com/r/LangChain/comments/1bvnxtr/rag_with_distinct_separate_knowledge_bases/) , 2024-04-05-0910
```
Hi,
after some searching I can't seem to find a clear-cut answer to this question:

Let's say I want to create a RAG-app
lication, where the end-user can ask questions related to two or more distinct fields, which are very far from one anoth
er, context-wise.

Here are my considerations:

- Should I simply create multiple indexes, and somehow evaluate which in
dex gives the best response?
- Should I look into a multi-agent framework (such as autogen)? Or is this only relevant if
 I want the application to actually do some form of task execution (such as writing and running code)
- Or should I just
 throw it all into the same index, and count on the effectiveness of the retrieval technique.
- ???

Thank you!
```
---

     
 
all -  [ Looking for LLM Consultant ](https://www.reddit.com/r/LangChain/comments/1bvn6t9/looking_for_llm_consultant/) , 2024-04-05-0910
```
\--- If this is violating a rule I am very sorry & please feel free to delete ---

Hi everyone - this a paid opportunity
,

we are a Berlin based company currently building an LLM based research assistant. We are planning to go live with thi
s till July, however I am the only person on our team working on the cognitive architecture and no-one but me understand
s a thing about it :D So I will def. need a second pair of eyes looking over what we are doing and as a sparrings partne
r. Below you find an overview of our project and the requirements.

Required:

* Advanced proficiency in Python programm
ing, including data science and machine learning libraries.
* Experience in deploying LLM-based applications, best case 
RAG-Applications.
* Experience with vector databases.

Overview of our current activities:

* Natural Language to SQL us
ing LLM based agents  

   * OpenAI function calls and LangChain-based SQL tools.
   * Purpose build databases for the a
gents needs, containing relevant data formatted closely to our business requirements.
   * Few Shot Example retrieval
* 
Self-Reflection and Plan and Solve architecture  

   * Composing 1-2 page long reports using multiple collaborative age
nts.
   * Undertaking multiple iterations to generate step-by-step plans and addressing gaps in information. Based on th
ese gaps, new natural language questions are formulated and directed to the SQL agent.
* LLMs are openAI only currently.

* Monitoring and evaluation through Langsmith

This will be an on-going project, so lets meet for a digital coffee chat
 first :)
```
---

     
 
all -  [ LangChain X Semantic Kernel ](https://www.reddit.com/r/LangChain/comments/1bvm0n8/langchain_x_semantic_kernel/) , 2024-04-05-0910
```
Hi all. Would like to gather some thoughts on the following, so as to decide how I should approach a new project:

Langc
hain X semantic kernel - what are the general tradeoffs?

Any impressions would be appreciated. Thank you
```
---

     
 
all -  [ Extracting data with Mixtral using langchain ](https://www.reddit.com/r/LangChain/comments/1bvkp9u/extracting_data_with_mixtral_using_langchain/) , 2024-04-05-0910
```
Hello everyone I was trying to extract data like book name from the whole website text, when using Openai llm + pydantic
 parser I get the data in required format but I want to use some open source model like mistral 8\*7b for my extraction 
task with pydantic parser and later on finetune it.

I have prepared datasets by extracting from openai and pydantic par
ser but before finetuning opensource model I want to make sure they return data in required format or support pydantic p
arser.

output from openai gpt 3.5 was satisfactory with pydantic parser but when using pydantic parser with Mixtral I g
ot urelatable output and give JSONDECODER error too .      Even  without using parser I got very irrelevant output If yo
u have any ideas please let me know it would be very helpful.
```
---

     
 
all -  [ The tool is used for building and driving workflows ](https://www.reddit.com/r/GPT4/comments/1bvhthh/the_tool_is_used_for_building_and_driving/) , 2024-04-05-0910
```
When we develop complex calls using large models, we might wonder if there's a clear and simple framework that can be ut
ilized to help us schedule and manage various tasks. Langchain could be an option to consider, but many complain about i
ts complexity and argue it fails to deliver the functionality people expect from it. In fact, for the purposes of task m
anagement and scheduling alone, a much simpler and more lightweight framework is entirely feasible.

I think my Agere is
 one such framework. Its basic idea is that it should provide me with the most universal basic core functions, independe
nt of any platform or tool, allowing me to develop anything on top of it, serving as a highly flexible flow driver.

Lan
gchain offers many functional modules, but when I use it, I often feel that although these modules bring convenience, th
ey lack controllability and are difficult to customize deeply. Therefore, I desire a fully autonomous and controllable f
ramework. Although the Langchain team later released the Langgraph tool, which is good and compensates for Langchain's w
eaknesses in this regard, its problem is that it's deeply bound to the Langchain framework and not universal enough. I w
ant a broader world. There are many other excellent frameworks for developing AI applications, such as Semantic Kernel, 
CrewAI, etc. I don't want to be confined to one framework when building AI applications. I believe I should be able to u
se any useful tool, not discard it because it belongs to different 'camps'.

In fact, Agere is not a conceptual framewor
k; it's the basic approach I followed during a project. I used it to develop GPTUI (a GPT chat TUI project), building ad
vanced features like group chat. Based on my own experience, I believe it has helped me clarify many task invocation ide
as and saved me a lot of time.

Actually, after using Agere, I even found Langchain to become more usable, as its rich t
oolkit can be applied within Agere. Therefore, Agere is not a framework competing with Langchain; it can compensate for 
the latter's complexity and steep learning curve.

Of course, it's far from perfect. However, if you currently have simi
lar needs, I recommend giving it a try. 

[happyapplehorse/agere: The tool is used for building and driving workflows sp
ecifically tailored for AI initiatives. It can be used to construct AI agents. (github.com)](https://github.com/happyapp
lehorse/agere)
```
---

     
 
all -  [ Launched a Video on Memory in Langchain.🤯 ](https://youtu.be/6QTxrASSQus) , 2024-04-05-0910
```
Here is what you can expect to learn:
- Importance of memory in conversational interfaces.
- Langchain utilities for int
egrating memory.
- Basic functionality of a memory system.
- Design considerations for memory systems.
- Storing and que
rying chat messages in Langchain.
- Variables returned from memory and their formats.
- Memory types and their usage.

M
ust have a visit...
```
---

     
 
all -  [ Unfinished responses from the models ](https://www.reddit.com/r/LangChain/comments/1bvd9qw/unfinished_responses_from_the_models/) , 2024-04-05-0910
```
I've been using LangChain for quite some time now and I have started to notice that in recent times the model responses 
start to cut abruptly even before the max token limit is reached. My Max token limit is set to the maximum amount of tok
ens the model can output, for example my token limit for a Gemini pro model is 4096, however I barely get a couple of li
nes to a maximum one paragraph of response even when I specifically ask the model to give me a detailed answer. on top o
f this I have also tried to play with other model parameters like temperature and I also tried setting up the max token 
to -1 because I saw somewhere that setting Max token to minus one would force the model to output the maximum number of 
tokens that it can generate, but I still get this issue. On the contrary, I do not have this issue when using native API
s from VertexAI or OpenAI. Am I doing something wrong here? Is anyone else seeing this?
```
---

     
 
all -  [ Opensource LLM monitoring tool - Measure token usage, cost, latency and accuracy with 2 lines of cod ](https://www.reddit.com/r/indiehackers/comments/1bv7ulu/opensource_llm_monitoring_tool_measure_token/) , 2024-04-05-0910
```
I am happy to launch **Langtrace - an open source observability tool that collects and analyze traces in order to help y
ou improve your LLM apps**. Langtrace has two components:

* **SDK**: The SDK is a lightweight library that you can inst
all and import into your project to collect traces.
* **Langtrace Dashboard**: The dashboard is a web-based interface wh
ere you can view and analyze your traces.

Attaching a couple of GIFs for your preview.

For context, we started this pr
oject internally a while back to solve our own problems. We are currently looking for feedback on how to improve this pr
oduct and looking to boot strap a community around it. You can join our discord community using this link - [https://dis
cord.com/invite/EaSATwtr4t](https://discord.com/invite/EaSATwtr4t)

There are a couple of ways to use this product:

1. 
You can sign up using this link - [https://langtrace.ai/](https://langtrace.ai/) to the hosted version, generate an API 
key, install and initialize the SDK in your application with the API key to start sending traces.  

   1. **The SDK ins
tallation and initialization is just 2 lines of code.**
2. You can self host and use it within your own environment.

Yo
u can find more details in our docs - [https://docs.langtrace.ai/introduction](https://docs.langtrace.ai/introduction)


**Open Source and Open Telemetry**

Entire code including the SDK and the web application is open source. You can check 
it out from here - [https://github.com/Scale3-Labs/langtrace](https://github.com/Scale3-Labs/langtrace) .

The spans gen
erated by our SDKs adhere to **open telemetry standards (OTEL)** which means, you can continue to use your existing obse
rvability backend and consume these traces by installing our SDKs.

**Vendors supported**

We support OpenAI, Anthropic,
 Langchain, LlamaIndex, ChromaDB, PineconeDB. We will continue to add more in the coming weeks.

**Pricing (for the host
ed version)**

It's completely free to use at the moment. Since this is the first version, it is still rough around the 
edges and we are looking for feedback from the community to continue to improve and nail the experience. However, we may
 start to monetize the hosted version at some point at a reasonable cost. But, you can continue to use our open source v
ersion, self host and use it for free.

For more details, please do check out our launch blog post - [https://langtrace.
ai/blog/introducing-langtrace](https://langtrace.ai/blog/introducing-langtrace)

Thank you all for continuing to engage 
with me over the past few weeks. It has been super fun building this project and we look forward to hearing all your fee
dback on our Discord.

&#x200B;

&#x200B;

https://i.redd.it/iiotmt4lmcsc1.gif

https://i.redd.it/yx8hix4lmcsc1.gif
```
---

     
 
all -  [ List of FREE and Best Selling Discounted Courses ](https://www.reddit.com/r/udemyfreeebies/comments/1bv7tsg/list_of_free_and_best_selling_discounted_courses/) , 2024-04-05-0910
```
## Udemy Free Courses for 04 April 2024

*Note : Coupons might expire anytime, so enroll as soon as possible to get the 
courses for FREE.*

* Android Apps Development in Hindi and Build 10 Applications[REDEEM OFFER](https://idownloadcoupon.
com/udemy/554/)
* Master Android by Building 3 Applications in Kotlin Language[REDEEM OFFER](https://idownloadcoupon.com
/udemy/553/)
* 6 Practice Exams | AWS Certified Cloud Practitioner CLF-C02[REDEEM OFFER](https://idownloadcoupon.com/ude
my/552/)
* Curso Google Sites 2024: Cómo Crear Páginas Web Desde Cero[REDEEM OFFER](https://idownloadcoupon.com/udemy/55
1/)
* Curso Blogger 2024: Cómo Crear un Blog Gratis Paso a Paso[REDEEM OFFER](https://idownloadcoupon.com/udemy/550/)
* 
Metabase an Open-Source Business Intelligence Platform[REDEEM OFFER](https://idownloadcoupon.com/udemy/549/)
* Desarroll
o Web Moderno con HTML5, CSS3 y Javascript 2024[REDEEM OFFER](https://idownloadcoupon.com/udemy/548/)
* SQL Mastery: MyS
QL bootcamp for beginners[REDEEM OFFER](https://idownloadcoupon.com/udemy/547/)
* Android Course Build 3 Applications fr
om Scratch with Java[REDEEM OFFER](https://idownloadcoupon.com/udemy/546/)
* Audit pour les Débutants : l’Art de devenir
 un bon auditeur[REDEEM OFFER](https://idownloadcoupon.com/udemy/545/)
* 230+ Exercises – Python for Data Science – NumP
y + Pandas[REDEEM OFFER](https://idownloadcoupon.com/udemy/544/)
* The Complete ISO 17025 Course[REDEEM OFFER](https://i
downloadcoupon.com/udemy/543/)
* The Complete ISO 31000 Risk Management Standard Course[REDEEM OFFER](https://idownloadc
oupon.com/udemy/542/)
* ISO 14001 – Environmental Management System (EMS) Course[REDEEM OFFER](https://idownloadcoupon.c
om/udemy/541/)
* Amazon Affiliate Marketing Course In Hindi – Start Business[REDEEM OFFER](https://idownloadcoupon.com/u
demy/540/)
* Certified Associate in Project Management CAPM Exam Prep[REDEEM OFFER](https://idownloadcoupon.com/udemy/53
9/)
* Curso de Outlook 2024 (Hotmail) , ¡Desde Cero Hasta Experto![REDEEM OFFER](https://idownloadcoupon.com/udemy/538/)

* JavaScript Interview Masterclass: Top 300 Questions (2024)[REDEEM OFFER](https://idownloadcoupon.com/udemy/537/)
* Go
ogle Professional Cloud Network Engineer – Practice Exams[REDEEM OFFER](https://idownloadcoupon.com/udemy/536/)
* AWS Ce
rtified Solutions Architect Professional Mock Exams[REDEEM OFFER](https://idownloadcoupon.com/udemy/535/)
* AWS Certifie
d Advanced Networking Specialty ANS-C01 – Exams[REDEEM OFFER](https://idownloadcoupon.com/udemy/534/)
* AWS Certified Da
tabase Specialty DBS-C01 Mock Exams[REDEEM OFFER](https://idownloadcoupon.com/udemy/533/)
* Next.js With Tailwind CSS-Bu
ild a Frontend Ecommerce Project[REDEEM OFFER](https://idownloadcoupon.com/udemy/532/)
* Mastering LangChain and AWS: A 
Guide to Economic Analysis[REDEEM OFFER](https://idownloadcoupon.com/udemy/531/)
* Zero to Hero hands-on mastery on HTML
5 JavaScript & ES6[REDEEM OFFER](https://idownloadcoupon.com/udemy/526/)
* Containerize SpringBoot Node Express Apps & D
eploy on Azure[REDEEM OFFER](https://idownloadcoupon.com/udemy/521/)
* Prompt & AI Engineering Safety Professional Certi
fication[REDEEM OFFER](https://idownloadcoupon.com/udemy/522/)
* Intro to ChatGPT: The Essential Skills for Getting Star
ted[REDEEM OFFER](https://idownloadcoupon.com/udemy/524/)
* Complete Personal Finance Course: Earn, Save and Invest[REDE
EM OFFER](https://idownloadcoupon.com/udemy/530/)
* Essential Business Analytics: From Data to Insights (2024)[REDEEM OF
FER](https://idownloadcoupon.com/udemy/529/)
* 4 Latest Practice Tests for C++ 2024[REDEEM OFFER](https://idownloadcoupo
n.com/udemy/528/)
* 4 Latest Practice Tests for Python 2024[REDEEM OFFER](https://idownloadcoupon.com/udemy/527/)
* Prac
tical Git & Github Bootcamp for Developers[REDEEM OFFER](https://idownloadcoupon.com/udemy/518/)
* Google Cloud Professi
onal Data Engineer – PDE – Exams[REDEEM OFFER](https://idownloadcoupon.com/udemy/519/)
* Big Data Programming Languages 
& Big Data Vs Data Science[REDEEM OFFER](https://idownloadcoupon.com/udemy/517/)
* Learn Big Data Basics[REDEEM OFFER](h
ttps://idownloadcoupon.com/udemy/516/)
* Hands-On SQL Server,ManagementStudio,SQL Queries,AzureStudio[REDEEM OFFER](http
s://idownloadcoupon.com/udemy/515/)
* JavaScript for Beginners – The Complete introduction to JS[REDEEM OFFER](https://i
downloadcoupon.com/udemy/513/)
* Flutter&Firebase complete social media app in Arabic\[2024\][REDEEM OFFER](https://idow
nloadcoupon.com/udemy/514/)
* Salesforce Platform Developer 1 Mock Exams[REDEEM OFFER](https://idownloadcoupon.com/udemy
/511/)
* Learn Java to master( updated to Java 17)[REDEEM OFFER](https://idownloadcoupon.com/udemy/512/)
* LinkedIn Mark
eting with Dekker: LinkedIn Ads, LinkedIn Leads[REDEEM OFFER](https://idownloadcoupon.com/udemy/510/)
* Copywriting with
 Dekker: The Only Copy Course You Ever Need![REDEEM OFFER](https://idownloadcoupon.com/udemy/508/)
* Market Research: De
kker’s Complete Marketing Research Course[REDEEM OFFER](https://idownloadcoupon.com/udemy/506/)
* Adobe Premiere Pro Adv
anced Video Editing Course[REDEEM OFFER](https://idownloadcoupon.com/udemy/507/)
* Android Very Basic App Development Co
urse with Java in Hindi[REDEEM OFFER](https://idownloadcoupon.com/udemy/505/)
* JavaScript Projects Course Build 20 Proj
ects in 20 Days[REDEEM OFFER](https://idownloadcoupon.com/udemy/504/)
* Android Projects Course Build 3 Applications fro
m Scratch[REDEEM OFFER](https://idownloadcoupon.com/udemy/503/)
* 30 HTML CSS & JavaScript Projects A Beginner’s Guide t
o JS[REDEEM OFFER](https://idownloadcoupon.com/udemy/501/)
* CIO Chief Information Officer Executive Certification[REDEE
M OFFER](https://idownloadcoupon.com/udemy/502/)
* Cómo Crear una Página de Ventas Para Hotmart 2024[REDEEM OFFER](https
://idownloadcoupon.com/udemy/500/)
* Cómo Crear una Página Web con Inteligencia Artificial 2024[REDEEM OFFER](https://id
ownloadcoupon.com/udemy/499/)
* Cómo Crear un Embudo de Ventas con WordPress Desde Cero 2024[REDEEM OFFER](https://idown
loadcoupon.com/udemy/498/)
* Cómo Crear un Blog con Inteligencia Artificial 2024[REDEEM OFFER](https://idownloadcoupon.c
om/udemy/497/)
* Ethical Hacking: Vulnerability Research[REDEEM OFFER](https://idownloadcoupon.com/udemy/496/)
* Bash Sc
ripting for Linux Security[REDEEM OFFER](https://idownloadcoupon.com/udemy/494/)
* Linux Security Basics for Beginners[R
EDEEM OFFER](https://idownloadcoupon.com/udemy/493/)
* PowerShell Functions Master Class[REDEEM OFFER](https://idownload
coupon.com/udemy/492/)
* The Internal Audit Champion[REDEEM OFFER](https://idownloadcoupon.com/udemy/491/)
* Communicati
on Skills: Acquire Effective Communication[REDEEM OFFER](https://idownloadcoupon.com/udemy/490/)
* Become a Successful A
ffiliate Marketer \[Success Blueprint\][REDEEM OFFER](https://idownloadcoupon.com/udemy/489/)
* Build Profitable E-Comme
rce Stores with WordPress & Woostify[REDEEM OFFER](https://idownloadcoupon.com/udemy/488/)
* AI for Business Strategy & 
Planning \[Masterclass\][REDEEM OFFER](https://idownloadcoupon.com/udemy/487/)
* Learn Content Writing using AI & Make M
oney Online[REDEEM OFFER](https://idownloadcoupon.com/udemy/486/)

GET MORE FREE ONLINE COURSES WITH CERTIFICATE – [CLIC
K HERE](https://idownloadcoupon.com/)
```
---

     
 
all -  [ List of FREE and Best Selling Discounted Courses ](https://www.reddit.com/r/udemyfreebies/comments/1bv7tea/list_of_free_and_best_selling_discounted_courses/) , 2024-04-05-0910
```
## Udemy Free Courses for 04 April 2024

*Note : Coupons might expire anytime, so enroll as soon as possible to get the 
courses for FREE.*

* Android Apps Development in Hindi and Build 10 Applications[REDEEM OFFER](https://idownloadcoupon.
com/udemy/554/)
* Master Android by Building 3 Applications in Kotlin Language[REDEEM OFFER](https://idownloadcoupon.com
/udemy/553/)
* 6 Practice Exams | AWS Certified Cloud Practitioner CLF-C02[REDEEM OFFER](https://idownloadcoupon.com/ude
my/552/)
* Curso Google Sites 2024: Cómo Crear Páginas Web Desde Cero[REDEEM OFFER](https://idownloadcoupon.com/udemy/55
1/)
* Curso Blogger 2024: Cómo Crear un Blog Gratis Paso a Paso[REDEEM OFFER](https://idownloadcoupon.com/udemy/550/)
* 
Metabase an Open-Source Business Intelligence Platform[REDEEM OFFER](https://idownloadcoupon.com/udemy/549/)
* Desarroll
o Web Moderno con HTML5, CSS3 y Javascript 2024[REDEEM OFFER](https://idownloadcoupon.com/udemy/548/)
* SQL Mastery: MyS
QL bootcamp for beginners[REDEEM OFFER](https://idownloadcoupon.com/udemy/547/)
* Android Course Build 3 Applications fr
om Scratch with Java[REDEEM OFFER](https://idownloadcoupon.com/udemy/546/)
* Audit pour les Débutants : l’Art de devenir
 un bon auditeur[REDEEM OFFER](https://idownloadcoupon.com/udemy/545/)
* 230+ Exercises – Python for Data Science – NumP
y + Pandas[REDEEM OFFER](https://idownloadcoupon.com/udemy/544/)
* The Complete ISO 17025 Course[REDEEM OFFER](https://i
downloadcoupon.com/udemy/543/)
* The Complete ISO 31000 Risk Management Standard Course[REDEEM OFFER](https://idownloadc
oupon.com/udemy/542/)
* ISO 14001 – Environmental Management System (EMS) Course[REDEEM OFFER](https://idownloadcoupon.c
om/udemy/541/)
* Amazon Affiliate Marketing Course In Hindi – Start Business[REDEEM OFFER](https://idownloadcoupon.com/u
demy/540/)
* Certified Associate in Project Management CAPM Exam Prep[REDEEM OFFER](https://idownloadcoupon.com/udemy/53
9/)
* Curso de Outlook 2024 (Hotmail) , ¡Desde Cero Hasta ExpertoREDEEM OFFER
* JavaScript Interview Masterclass: Top 30
0 Questions (2024)[REDEEM OFFER](https://idownloadcoupon.com/udemy/537/)
* Google Professional Cloud Network Engineer – 
Practice Exams[REDEEM OFFER](https://idownloadcoupon.com/udemy/536/)
* AWS Certified Solutions Architect Professional Mo
ck Exams[REDEEM OFFER](https://idownloadcoupon.com/udemy/535/)
* AWS Certified Advanced Networking Specialty ANS-C01 – E
xams[REDEEM OFFER](https://idownloadcoupon.com/udemy/534/)
* AWS Certified Database Specialty DBS-C01 Mock Exams[REDEEM 
OFFER](https://idownloadcoupon.com/udemy/533/)
* Next.js With Tailwind CSS-Build a Frontend Ecommerce Project[REDEEM OFF
ER](https://idownloadcoupon.com/udemy/532/)
* Mastering LangChain and AWS: A Guide to Economic Analysis[REDEEM OFFER](ht
tps://idownloadcoupon.com/udemy/531/)
* Zero to Hero hands-on mastery on HTML5 JavaScript & ES6[REDEEM OFFER](https://id
ownloadcoupon.com/udemy/526/)
* Containerize SpringBoot Node Express Apps & Deploy on Azure[REDEEM OFFER](https://idownl
oadcoupon.com/udemy/521/)
* Prompt & AI Engineering Safety Professional Certification[REDEEM OFFER](https://idownloadcou
pon.com/udemy/522/)
* Intro to ChatGPT: The Essential Skills for Getting Started[REDEEM OFFER](https://idownloadcoupon.c
om/udemy/524/)
* Complete Personal Finance Course: Earn, Save and Invest[REDEEM OFFER](https://idownloadcoupon.com/udemy
/530/)
* Essential Business Analytics: From Data to Insights (2024)[REDEEM OFFER](https://idownloadcoupon.com/udemy/529/
)
* 4 Latest Practice Tests for C++ 2024[REDEEM OFFER](https://idownloadcoupon.com/udemy/528/)
* 4 Latest Practice Tests
 for Python 2024[REDEEM OFFER](https://idownloadcoupon.com/udemy/527/)
* Practical Git & Github Bootcamp for Developers[
REDEEM OFFER](https://idownloadcoupon.com/udemy/518/)
* Google Cloud Professional Data Engineer – PDE – Exams[REDEEM OFF
ER](https://idownloadcoupon.com/udemy/519/)
* Big Data Programming Languages & Big Data Vs Data Science[REDEEM OFFER](ht
tps://idownloadcoupon.com/udemy/517/)
* Learn Big Data Basics[REDEEM OFFER](https://idownloadcoupon.com/udemy/516/)
* Ha
nds-On SQL Server,ManagementStudio,SQL Queries,AzureStudio[REDEEM OFFER](https://idownloadcoupon.com/udemy/515/)
* JavaS
cript for Beginners – The Complete introduction to JS[REDEEM OFFER](https://idownloadcoupon.com/udemy/513/)
* Flutter&Fi
rebase complete social media app in Arabic\[2024\][REDEEM OFFER](https://idownloadcoupon.com/udemy/514/)
* Salesforce Pl
atform Developer 1 Mock Exams[REDEEM OFFER](https://idownloadcoupon.com/udemy/511/)
* Learn Java to master( updated to J
ava 17)[REDEEM OFFER](https://idownloadcoupon.com/udemy/512/)
* LinkedIn Marketing with Dekker: LinkedIn Ads, LinkedIn L
eads[REDEEM OFFER](https://idownloadcoupon.com/udemy/510/)
* Copywriting with Dekker: The Only Copy Course You Ever Need
REDEEM OFFER
* Market Research: Dekker’s Complete Marketing Research Course[REDEEM OFFER](https://idownloadcoupon.com/ud
emy/506/)
* Adobe Premiere Pro Advanced Video Editing Course[REDEEM OFFER](https://idownloadcoupon.com/udemy/507/)
* And
roid Very Basic App Development Course with Java in Hindi[REDEEM OFFER](https://idownloadcoupon.com/udemy/505/)
* JavaSc
ript Projects Course Build 20 Projects in 20 Days[REDEEM OFFER](https://idownloadcoupon.com/udemy/504/)
* Android Projec
ts Course Build 3 Applications from Scratch[REDEEM OFFER](https://idownloadcoupon.com/udemy/503/)
* 30 HTML CSS & JavaSc
ript Projects A Beginner’s Guide to JS[REDEEM OFFER](https://idownloadcoupon.com/udemy/501/)
* CIO Chief Information Off
icer Executive Certification[REDEEM OFFER](https://idownloadcoupon.com/udemy/502/)
* Cómo Crear una Página de Ventas Par
a Hotmart 2024[REDEEM OFFER](https://idownloadcoupon.com/udemy/500/)
* Cómo Crear una Página Web con Inteligencia Artifi
cial 2024[REDEEM OFFER](https://idownloadcoupon.com/udemy/499/)
* Cómo Crear un Embudo de Ventas con WordPress Desde Cer
o 2024[REDEEM OFFER](https://idownloadcoupon.com/udemy/498/)
* Cómo Crear un Blog con Inteligencia Artificial 2024[REDEE
M OFFER](https://idownloadcoupon.com/udemy/497/)
* Ethical Hacking: Vulnerability Research[REDEEM OFFER](https://idownlo
adcoupon.com/udemy/496/)
* Bash Scripting for Linux Security[REDEEM OFFER](https://idownloadcoupon.com/udemy/494/)
* Lin
ux Security Basics for Beginners[REDEEM OFFER](https://idownloadcoupon.com/udemy/493/)
* PowerShell Functions Master Cla
ss[REDEEM OFFER](https://idownloadcoupon.com/udemy/492/)
* The Internal Audit Champion[REDEEM OFFER](https://idownloadco
upon.com/udemy/491/)
* Communication Skills: Acquire Effective Communication[REDEEM OFFER](https://idownloadcoupon.com/u
demy/490/)
* Become a Successful Affiliate Marketer \[Success Blueprint\][REDEEM OFFER](https://idownloadcoupon.com/udem
y/489/)
* Build Profitable E-Commerce Stores with WordPress & Woostify[REDEEM OFFER](https://idownloadcoupon.com/udemy/4
88/)
* AI for Business Strategy & Planning \[Masterclass\][REDEEM OFFER](https://idownloadcoupon.com/udemy/487/)
* Learn
 Content Writing using AI & Make Money Online[REDEEM OFFER](https://idownloadcoupon.com/udemy/486/)

GET MORE FREE ONLIN
E COURSES WITH CERTIFICATE – [CLICK HERE](http://reddit.com/r/udemyfreeebies/)
```
---

     
 
all -  [ Do we have to use LCEL? ](https://www.reddit.com/r/LangChain/comments/1bv6o5c/do_we_have_to_use_lcel/) , 2024-04-05-0910
```
I am returning to LangChain after a few months to work on a new project, and since then, LCEL has been introduced. Is th
e old syntax being entirely depreciated? LCEL seems really hard to wrap my head around. Something as simple as a Convers
ational Retrieval Chain in python seems so much more complex with a lot more steps in LCEL.
```
---

     
 
all -  [ Issue Using TextGen API, works with Curl and SillyTavern ](https://www.reddit.com/r/Oobabooga/comments/1bv5dtc/issue_using_textgen_api_works_with_curl_and/) , 2024-04-05-0910
```
I am having issues using they text gen python api, Curl works, silly tavern works but the api using langchain doesn't. I
 get the error 'ERROR: response: <Response [404]>'. To the best of my knowledge this should work. I'm running flags of -
-api --verbose --listen, and the openai extension. Does anyone have any ideas what I am doing wrong?

    model_url = 'h
ttp://localhost:5000'
    
    from langchain.chains import LLMChain
    from langchain.globals import set_debug
    fro
m langchain_community.llms import TextGen
    from langchain_core.prompts import PromptTemplate
    
    set_debug(True)

    
    template = '''Question: {question}
    
    Answer: Let's think step by step.'''
    
    
    prompt = Prompt
Template.from_template(template)
    llm = TextGen(model_url=model_url)
    llm_chain = LLMChain(prompt=prompt, llm=llm)

    question = 'What NFL team won the Super Bowl in the year Justin Bieber was born?'
    
    llm_chain.run(question)
```
---

     
 
all -  [ Update: Langtrace Launch: Opensource LLM monitoring tool - achieving better cardinality compared to  ](https://www.reddit.com/r/LangChain/comments/1bv4nzb/update_langtrace_launch_opensource_llm_monitoring/) , 2024-04-05-0910
```
This is a follow up for: [https://www.reddit.com/r/LangChain/comments/1bnkvtv/update\_langtrace\_preview\_opensource\_ll
m/](https://www.reddit.com/r/LangChain/comments/1bnkvtv/update_langtrace_preview_opensource_llm/)  


I am happy to fina
lly launch **Langtrace - an open source observability tool that collects and analyze traces in order to help you improve
 your LLM apps**. Langtrace has two components:

* **SDK**: The SDK is a lightweight library that you can install and im
port into your project to collect traces.
* **Langtrace Dashboard**: The dashboard is a web-based interface where you ca
n view and analyze your traces.

Attaching a couple of GIFs for your preview.

For context, we started this project inte
rnally a while back to solve our own problems. We are currently looking for feedback on how to improve this product and 
looking to boot strap a community around it.  You can join our discord community using this link - [https://discord.com/
invite/EaSATwtr4t](https://discord.com/invite/EaSATwtr4t) 

There are a couple of ways to use this product:

1. You can 
sign up using this link - [https://langtrace.ai/](https://langtrace.ai/) to the hosted version, generate an API key, ins
tall and initialize the SDK in your application with the API key to start sending traces.
   1. **The SDK installation a
nd initialization is just 2 lines of code.**
2. You can self host and use it within your own environment.

You can find 
more details in our docs - [https://docs.langtrace.ai/introduction](https://docs.langtrace.ai/introduction)

**Open Sour
ce and Open Telemetry**

Entire code including the SDK and the web application is open source. You can check it out from
 here - [https://github.com/Scale3-Labs/langtrace](https://github.com/Scale3-Labs/langtrace) .

The spans generated by o
ur SDKs adhere to **open telemetry standards (OTEL)** which means, you can continue to use your existing observability b
ackend and consume these traces by installing our SDKs.

**Vendors supported**

We support OpenAI, Anthropic, Langchain,
 LlamaIndex, ChromaDB, PineconeDB. We will continue to add more in the coming weeks.

**Pricing (for the hosted version)
**

It's completely free to use at the moment. Since this is the first version, it is still rough around the edges and w
e are looking for feedback from the community to continue to improve and nail the experience. However, we may start to m
onetize the hosted version at some point at a reasonable cost. But, you can continue to use our open source version, sel
f host and use it for free.

For more details, please do check out our launch blog post - [https://langtrace.ai/blog/int
roducing-langtrace](https://langtrace.ai/blog/introducing-langtrace)

&#x200B;

Thank you all for continuing to engage w
ith me over the past few weeks. It has been super fun building this project and we look forward to hearing all your feed
back on our Discord.

&#x200B;

https://i.redd.it/t29eh8rnxbsc1.gif

https://i.redd.it/k4ns4arnxbsc1.gif
```
---

     
 
all -  [ A human approval tool for your agent workflows ](https://www.reddit.com/r/LangChain/comments/1bv2hcf/a_human_approval_tool_for_your_agent_workflows/) , 2024-04-05-0910
```
Hey. We have worked on LLM apps that were integrated into existing workflows. So say, a customer support ticket arrives 
and my LLM chain kicks off to analyze the request, determine what to do next, and for example, write a response.

But we
 needed a way for users to check and approve these agent actions. We didn't find anything to help us with this, since mo
st things are built for chatbots.

So we started working on a human oversight tool that can be integrated into any custo
m LLM chain. Need human approval? Call our API and we'll call you back via webhook once there is a user decision.

[goto
human.com](https://gotohuman.com/)

Would be great to hear your thoughts 🙏
```
---

     
 
all -  [ Structured extraction? ](https://www.reddit.com/r/LangChain/comments/1bv25ml/structured_extraction/) , 2024-04-05-0910
```
Found the Fructose ([https://github.com/bananaml/fructose](https://github.com/bananaml/fructose)) and LlamaIndex toolcha
ins for defining fixed schemas and wondering if LangChain has something similar? Very interested in type-checked outputs
 for document understanding.
```
---

     
 
all -  [ Prompt Serialization in YML ](https://www.reddit.com/r/LangChain/comments/1buzihw/prompt_serialization_in_yml/) , 2024-04-05-0910
```
To learn more about prompting, I wanted to create some prompt templates in YAML. When looking for the docs, I come acros
s several links of the LangChain docs that, unfortunatly, lead to a dead end.

Can somebody provide a resource on prompt
 serialization?
```
---

     
 
all -  [ simple CRM 'copilot' ](https://www.reddit.com/r/LangChain/comments/1buxlp9/simple_crm_copilot/) , 2024-04-05-0910
```
Hello there, I am brainstorming a project for a company that does digital marketing. They want to integrate llms into th
eir client relation processes, writing emails, proposals, documents. I think what I will be doing for them will be creat
ing a pipeline that creates separate text databases for each client, and then create a ChatGPT assistant that includes t
hese text documents in its knowledge base, such that employees can have conversations with this assistant and have it dr
aft things for them.  


My initial plan was just to use the openai api, and update per-client assistant knowledge bases
 daily. I understand there are more sophisticated approaches out there, but don't want to get too much into the weeds an
d try to keep it simple if possible. What is the easiest way to get RAG producing better writing than simple knowledge-b
ase driven chatGPT assistants per client?  


On a slightly different note, my experience lately is that Claude is super
ior for human-like writing, but i have never tried to create anything with their API, how does it compare to the OpenAI 
API for something like this?
```
---

     
 
all -  [ Any recommendations of blog, posts or material about 'practical' prompt engineering using more compl ](https://www.reddit.com/r/LocalLLaMA/comments/1buq0fj/any_recommendations_of_blog_posts_or_material/) , 2024-04-05-0910
```
I recently worked in a project that was heavy LLM related using openAI, but while doing that I realized that is  little 
literature about 'how to implement' or 'how it works' but a lot on papers and 'conceptual knowledge'.

An example with t
hat is that recently I was only able to understand how ReAct working in practice because of langchain implementation, li
ke if I returned an error in a function, ReAct was able to guess better the next function call. 

I'm looking for blogs,
 posts, ... people that maintain content that is more easily digestable, or some kind of refining list of papers that ar
e more 'practical oriented', do you have any recommendations?

I come from a Data Engineer\\Sotftware Engineer backgroun
d
```
---

     
 
all -  [ Location of YamlOutputParser in LangChain 0.1 ](https://www.reddit.com/r/LangChain/comments/1bunovt/location_of_yamloutputparser_in_langchain_01/) , 2024-04-05-0910
```
In LangChain 0.1, why is YamlOutputParser imported from `langchain.output_parsers` whereas the other parsers like JsonOu
tputParser, XMLOutputParser etc. imported from `langchain_core.output_parsers`?
```
---

     
 
all -  [ How can I adjust the prompt to ensure that responses are not influenced by irrelevant questions that ](https://www.reddit.com/r/LangChain/comments/1bunkoo/how_can_i_adjust_the_prompt_to_ensure_that/) , 2024-04-05-0910
```
I am Implementing ConversationBufferMemory and the problem I am facing above is when I ask a different question which is
 not relevant to chat\_history, still it gives us response based on the chat history how can I change the prompt to hand
le such cases.
```
---

     
 
all -  [ [First Post] SOS! Startup founder/hiring member looking for any Python/BackendDev/Data profile for F ](https://www.reddit.com/r/indianstartups/comments/1bunkmw/first_post_sos_startup_founderhiring_member/) , 2024-04-05-0910
```
**TLDR:** If you are a startup founder/know someone from tech hiring team, looking for a reliable and an *actually* hard
working moldable resource (I can commit to **at least 14 hours** daily, learn WHATEVER is required for your team and the
n join, sleep in office if required, work on war footing, take pay cuts for initial months or **work as intern** for ini
tial time while I am on NP)

**TLDR 2:** Stuck in WITCH company for 2.5 years now. And friends are becoming SDE1, SDE2, 
MTS etc. Getting sleepless nights and mental health's in total sham. I want to switch anyhow and get rid of this service
 based tag and come out of this suffocating vicious gloomy loop's dead-end, and actually build/develop something from sc
ratch.

&#x200B;

Hi fellow Redditors,

This is my first post on reddit. And perhaps my last hope/resort. The curse/tag 
of service based companies is so damn real.

No, I don't want sympathy, but I do want a chance to prove myself. And take
 some action.

Here's what's absolutely traumatizing me to the core. Will I end up rotting here in this same company til
l retirement? Can nothing be done now? Is is already too late? Have I hit the dead end?

I will be honest. I am familiar
 with many libraries and I am a jack of many, many, trades (read more to find out) but perhaps, not exactly master of on
e yet. And I think that has been THE biggest career mistake of mine so far.

&#x200B;

Firstly, my skill sets:

**Langua
ges:** C++ and Python (200+ on LeetCode, improvising on DP and recursion currently)

**Frameworks:** Flask, FastAPI, Dja
ngo (have used basic Flask at work, and completed reading the docs for all 3, read most asked interview questions, espec
ially ORMs views models in Django)

**AI/ML Familiarity:** Have used quite a few HF LLM APIs on inference using transfor
mers library, created APIs utilizing them. Occasionally, played around with langchain as well for prompt parameterizatio
n. Haven't fine tuned a model though.

**SQL:** Clear till joins and practicing more on LC.

**MongoDB:** Have set up a 
Cloud DB Atlas, used pymongo to connect and do CRUD in the DB.

**Docker, Git:** Have used both at work. Not Kubernetes 
tho.

&#x200B;

I have projects like django chat app, speech-to-text python script in resume. I also have have one simpl
e OCR app (3rd party api) (frontend streamlit, backend fastapi), containerized and hosted on GCP.

&#x200B;

Despite app
lying with referrals on LinkedIn, daily updating profiles on Naukri etc., tweaking CV according to JDs, cold mailing if 
possible, I haven't received any substantial offer yet. It's been \~5 months since I have been job-hunting. And I spend 
maybe 2-3 hours daily on Job Search.

&#x200B;

Is the market *really that bad?* Or because of my service based tag (90 
days notice period), companies are not even shortlisting the CV?

Say, If I learn a new tech stack (Cloud/Go/pySpark/Cyb
erSec), will no one hire me now even for fresher/entry level roles given my experience in WITCH?

&#x200B;

In my initia
l years, I thought since I have a good project, I will use it as a base to switch. However, actual meat of the dev work 
(whatever little was there) slowed down post POC phase, and after a while, only the mundane tasks remained. Now, roles w
ith 2+ YoE want experience in CI/CD, Redis caching, Kafka/RabbitMQ, Celery, ElasticSearch, AWS and what not. It's not li
ke I can't learn them but...

&#x200B;

I genuinely fear (and maybe feel overwhelmed) that by the time I catch up with t
hose things properly, I will have 3+ YoE and then the requirements will be even more stringent, and that way I will be p
erpetually left lagging behind.

I am ready to even take like 10-20% cut on my current CTC or offer to work for some wee
ks for free.

I am eager to put in the work even on weekdays, and absorb like sponge and hustle in the right direction, 
but I don't want to fill excel for the rest of my life and become like those folks whom I see at office. It freezes and 
scares me.

If you are into Backend Dev/Data or similar senior tech data roles, and have read so far, Thank You!!

&#x20
0B;

Do genuinely advice (or DM me if you can be kind enough to mentor me) on what can I do from here to make the most a
nd escape this cycle. 
```
---

     
 
all -  [ RetrievalQA loop consuming gradually more memory ](https://www.reddit.com/r/LangChain/comments/1bufjwi/retrievalqa_loop_consuming_gradually_more_memory/) , 2024-04-05-0910
```
Hi, all!

I'm currently working with Langchain with a logic that will go through all PDFs with RetrievalQA asking a cert
ain query inside a loop (so n inferences every time).

The problem is, the bigger my retrieved chunks and prompt get, th
e more memory is allocated in my VRAM, and I only have 24GB available, and it oftens runs out with some of my testings.


Is there a way to prevent this amount of memory consumed through the loop? It seems to be that every retrieval call inc
rements more and more memory allocated. I've tried nesting my logic under torch.no\_grad() but no luck. I also have my P
YTORCH\_CUDA\_ALLOC\_CONF variable set to garbage\_collection\_threshold:0.6,max\_split\_size\_mb:128.

Thanks in advanc
e!
```
---

     
 
all -  [ Gemini function calling  ](https://www.reddit.com/r/LangChain/comments/1bu9j1u/gemini_function_calling/) , 2024-04-05-0910
```
I want to use function calling with Gemini, I checked Vertex ai documentation and tutorials but they are a bit confusing
 and mess. Anyone have worked with Gemini function calling with Langchain before?
```
---

     
 
all -  [ Advanced RAG with Document Intelligence  ](https://www.reddit.com/r/Azure_AI_Cognitive/comments/1bu5l7l/advanced_rag_with_document_intelligence/) , 2024-04-05-0910
```
Has anyone used Azure Document intelligence for capturing metadata in PDFs with tables, figures? How can we create seman
tic chunks using a Qdrant database using Azure Document intelligence to extract data? How can add relevant metadata to m
eaningful chunks? Any other tips to create an advanced RAG pipeline? What are evaluations methods available? Currently u
sing Langchain framework, and I know they support Document Intelligence as one of the document loaders.
```
---

     
 
all -  [ Advanced RAG for PDFs with tables and figures, capturing metadata , Azure Document Intelligent  ](https://www.reddit.com/r/LangChain/comments/1bu5hyt/advanced_rag_for_pdfs_with_tables_and_figures/) , 2024-04-05-0910
```
Has anyone used Azure Document intelligence for capturing metadata in PDFs with tables, figures? How can we create seman
tic chunks using a Qdrant database using Azure Document intelligence to extract data? How can add relevant metadata to m
eaningful chunks? Any other tips to create an advanced RAG pipeline? What are evaluations methods available?
```
---

     
 
all -  [ Prefilter documents before similaritysearch ](https://www.reddit.com/r/LangChain/comments/1bu5dqs/prefilter_documents_before_similaritysearch/) , 2024-04-05-0910
```
I'm using a langchain script in order to make a similarity search of a query embedding in an embedding's MongoDb collect
ion but I want to pre filter the documents to search only in the documents that are $in an objectId array.

    // Get t
he list of embeddings _ids to preFilter
    const documentData =  await documentCollection.findOne(
      { '_id': docum
entId },
      { 'embededings': 1 }
    )
    const documentEmbeddingsId = documentData.embeddings
    
    
    
    //
 Embed query
    const query = 'What is this document about?'
    const embeddings = new OpenAIEmbeddings({
      modelN
ame:'XXX',
      openAIApiKey: 'XXX'
    })
    const embeddedQuery = await embeddings.embedQuery(query)
    
    
    

    // Similarity search
    const vectorStore = new MongoDBAtlasVectorSearch(embeddings, {
      collection,
      inde
xName: 'XXX',
      textKey: 'XXX', 
      embeddingKey: 'XXX', 
    });
    const preFilter = {
      preFilter: {
    
    _id: {
          $in: documentEmbeddingsId
        },
      },
    }
    const storingResponse = await vectorStore.s
imilaritySearchVectorWithScore(embeddedQuery,4,preFilter)
    

Running this code returns this error:

'Error: MongoServ
erError: Operand type is not supported for $vectorSearch: objectId'.

Is the error in the preFilter? Or is this type of 
filter not supported by mongodb? Any ideas on how I can make this search? The documentEmbeddings array has ObjectId type
. If I try to instead give a string array I get the following error: Error: MongoServerError: PlanExecutor error during 
aggregation :: caused by :: Path '\_id' needs to be indexed as token
```
---

     
 
all -  [ Multi-Agent Orchestration playlist ](https://www.reddit.com/r/LangChain/comments/1bu50s6/multiagent_orchestration_playlist/) , 2024-04-05-0910
```
Checkout this playlist around Multi-Agent Orchestration that covers
1. What is Multi-Agent Orchestration?
2. Beginners g
uide for Autogen, CrewAI and LangGraph
3. Debate application between 2 agents using LangGraph
4. Multi-Agent chat using 
Autogen
5. AI tech team using CrewAI
6. Autogen using HuggingFace and local LLMs

https://youtube.com/playlist?list=PLnH
2pfPCPZsKhlUSP39nRzLkfvi_FhDdD&si=B3yPIIz7rRxdZ5aU
```
---

     
 
all -  [ [P] RAG pipeline to query the ML Engineering Open Book ](https://www.reddit.com/r/MachineLearning/comments/1bu4wyx/p_rag_pipeline_to_query_the_ml_engineering_open/) , 2024-04-05-0910
```
I built a quick RAG implementation using Langchain to make it easy to query the [ML Engineering Open Book](https://githu
b.com/stas00/ml-engineering) by [Stas Bekman](https://twitter.com/StasBekman). The Multi-Vector retriever gave pretty go
od results and was quite easy to set up too. 

Github link - [https://github.com/shreyansh26/RAG-ML-Engg-Open-Book](http
s://github.com/shreyansh26/RAG-ML-Engg-Open-Book)

Hope this is useful for folks!
```
---

     
 
MachineLearning -  [ [Project] FinancialAdvisorGPT : LLM+RAG Boilerplate Project ](https://www.reddit.com/r/MachineLearning/comments/1btlpgd/project_financialadvisorgpt_llmrag_boilerplate/) , 2024-04-05-0910
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

     
 
MachineLearning -  [ [Project] Picachain, image search made simple. ](https://www.reddit.com/r/MachineLearning/comments/1bt7epv/project_picachain_image_search_made_simple/) , 2024-04-05-0910
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

     
 
deeplearning -  [ Tengyu Ma on Voyage AI - Weaviate Podcast #91! ](https://www.reddit.com/r/deeplearning/comments/1bjft8i/tengyu_ma_on_voyage_ai_weaviate_podcast_91/) , 2024-04-05-0910
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

     
