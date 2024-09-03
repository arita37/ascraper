 
all -  [ Async tool definitions using decorator  ](https://www.reddit.com/r/LangChain/comments/1f7lztx/async_tool_definitions_using_decorator/) , 2024-09-03-0911
```
How to make the agent call the functions only through asynchronous call? How should the tool definition be ?
```
---

     
 
all -  [ Building a Dynamic Query System ](https://www.reddit.com/r/LangChain/comments/1f7lneb/building_a_dynamic_query_system/) , 2024-09-03-0911
```
Hey everyone,

I'm in the process of building a Retrieval-Augmented Generation (RAG) system for a retail company, levera
ging AWS infrastructure. My current setup includes OpenSearch as the vector database. The structure of the data in my da
tabase looks something like this:

`{`

`name: 'Product Name',`

`author: 'Author Name',`

`description: 'Some text',`


`yyyymm: '202408'`

`}`

Here's the challenge I'm facing:

* When I include the author's name in a query, OpenSearch doe
sn't always catch it correctly. To improve accuracy, I've added a filter column in the chat UI, allowing users to select
 the author's name, which creates a subset of the database and returns more accurate results.
* However, users can ask q
uestions in various ways, and there are countless combinations of queries that could be passed to OpenSearch. It's impra
ctical to manually create all possible filters.

**My current solution:**

* Allow users to ask questions naturally.
* U
se an LLM to convert these questions into an OpenSearch query, which is then passed to the database.

**My follow-up con
cern:**

* How should I handle situations where a user's question doesn't require query formulation (e.g., simple inform
ational questions or commands)?

I'm looking for advice or best practices on dynamically generating queries to handle a 
wide range of user inputs and how to manage cases where query formulation isn't needed. Any insights or suggestions woul
d be greatly appreciated!

Thanks in advance!
```
---

     
 
all -  [  LangChain vs LlamaIndex for RAG
 ](https://www.reddit.com/r/SmythOS_/comments/1f7l3l3/langchain_vs_llamaindex_for_rag/) , 2024-09-03-0911
```
Somebody asked here the difference in handling RAG with LangChain and LlamaIndex. Here is a little overview that should 
help you get started. While both LangChain and LlamaIndex are powerful tools for implementing RAG, they have some notabl
e differences in their approach:

1. Embeddings:
   * LangChain: Explicitly requires setting up an embedding model.
   *
 LlamaIndex: Handles embeddings internally, often not requiring explicit setup.
2. Vector Databases:
   * LangChain: Typ
ically uses external vector DBs like Chroma.
   * LlamaIndex: Can work without an explicit vector DB, using its own inde
xing structures.
3. Workflow:
   * LangChain: 'Load document -> Text split -> Vector DB embedding -> LLM'
   * LlamaInde
x: Often simpler, with fewer explicit steps.
4. Flexibility:
   * LangChain: More modular, allowing fine-grained control
 over each step.
   * LlamaIndex: More abstracted, handling many details internally.
5. Use Cases:
   * LangChain: Bette
r for complex, customized RAG pipelines.
   * LlamaIndex: Simpler for quick RAG implementation with less setup.

Both fr
ameworks are powerful and continually evolving. The choice between them often depends on your specific needs, desire for
 control over the RAG pipeline, and familiarity with each tool.


```
---

     
 
all -  [ Join an exciting UK AI Games Company to Create Something Epic! | Recruiting Development Roles for In ](https://www.reddit.com/r/gameDevClassifieds/comments/1f7hrk8/join_an_exciting_uk_ai_games_company_to_create/) , 2024-09-03-0911
```
Hey Game Devs!

I’m Ploj, an ex New World streamer and I’ve joined an exciting new AI gaming company. 

I can’t reveal t
oo much but we need some more people to join our team to help us finish our first development phase. We already have an 
amazing team and once the first development phase has been completed this year, we will be looking for investment!

**Wh
at’s happening?** I’m part of the team leading the creative direction and gameplay design at Infinity Fiction, a groundb
reaking AI-powered text adventure RPG. We’re blending the magic of storytelling with cutting-edge technology. 

We are a
lso developing our first game that will use our Infinity Fiction AI platform. We are keeping things quiet for now but pl
an to make a big noise when we are ready soon!

**Who am I looking for?** I’m on the hunt for **UK-based developers** wa
nting to get involved and help shape the future of Infinity Fiction, the world of AI and potentially the future of the g
ames industry. 

We are looking for the right fit - passionate, hard working and loves what they do. We want self starte
rs who are looking for the opportunity to create themselves a role at a new AI business.

Loving games, D&D or adventure
 books would be a bonus! 

**How to apply**

If you're in the UK, love gaming, and have the skills to help build somethi
ng incredible, drop a comment or shoot me a message and your CV. 

Let’s make history together with *Infinity Fiction*! 
🚀

**Role 1**

UK Based AI developer/engineer to build agentic RAG applications using python. Knowledge of Kubernetes or
 HashiCorp Nomad, or other devops technologies.

* Python (Django desirable)
* Advanced Agentic RAG
* Llamaindex
* Langc
hain
* Embeddings & Vector Stores
* Inference
* Database management systems: MongoDB, PostgreSQL, MySQL, MySQL-lite
* Kn
owledge of RESTful APIs and experience in API design and implementation.

**Role 2**

UK Based Backend web developer to 
build micro-serviced web services using python, familiar with:

* JavaScript
* Python (Django Desirable)
* Database mana
gement systems: MongoDB, PostgreSQL, MySQL, MySQL-lite
* Knowledge of RESTful APIs and experience in API design and impl
ementation.
* Familiar with cloud platforms and DevOps practices such as CI/CD pipelines
* Other backend languages would
 be a bonus.
* Knowledge of Kubernetes or HashiCorp Nomad, or other devops technologies would be a bonus

**Role 3**

UK
 Based Front end web developer to build customer facing functional UI's and internal tooling familiar with:

* JavaScrip
t,
* HTML/CSS frameworks such as bootstrap
* Experience using front end frameworks: React, Next.js
* Database management
 systems: MongoDB, PostgreSQL, MySQL, MySQL-lite (desirable)
* Knowledge of RESTful APIs and experience in API design an
d implementation.
* Familiar with cloud platforms and DevOps practices such as CI/CD pipelines
* Python (desirable)
* Gr
aphic design (desirable)
```
---

     
 
all -  [ Join an exciting UK AI Games Company to Create Something Epic! | Recruiting Development Roles for In ](https://www.reddit.com/r/UKJobs/comments/1f7hof6/join_an_exciting_uk_ai_games_company_to_create/) , 2024-09-03-0911
```
Hey everyone!

I’m Ploj, an ex New World streamer and I’ve joined an exciting new AI gaming company. 

I can’t reveal to
o much but we need some more people to join our team to help us finish our first development phase. We already have an a
mazing team and once the first development phase has been completed this year, we will be looking for investment!

**Wha
t’s happening?** I’m part of the team leading the creative direction and gameplay design at Infinity Fiction, a groundbr
eaking AI-powered text adventure RPG. We’re blending the magic of storytelling with cutting-edge technology. 

We are al
so developing our first game that will use our Infinity Fiction AI platform. We are keeping things quiet for now but pla
n to make a big noise when we are ready soon!

**Who am I looking for?** I’m on the hunt for **UK-based developers** wan
ting to get involved and help shape the future of Infinity Fiction, the world of AI and potentially the future of the ga
mes industry. 

We are looking for the right fit - passionate, hard working and loves what they do. We want self starter
s who are looking for the opportunity to create themselves a role at a new AI business.

Loving games, D&D or adventure 
books would be a bonus! 



**How to apply**

If you're in the UK, love gaming, and have the skills to help build someth
ing incredible, drop a comment or shoot me a message and your CV. 

Let’s make history together with *Infinity Fiction*!
 🚀



**Role 1**

UK Based AI developer/engineer to build agentic RAG applications using python. Knowledge of Kubernetes
 or HashiCorp Nomad, or other devops technologies.

* Python (Django desirable)
* Advanced Agentic RAG
* Llamaindex
* La
ngchain
* Embeddings & Vector Stores
* Inference
* Database management systems: MongoDB, PostgreSQL, MySQL, MySQL-lite
*
 Knowledge of RESTful APIs and experience in API design and implementation.



**Role 2**

UK Based Backend web develope
r to build micro-serviced web services using python, familiar with:

* JavaScript
* Python (Django Desirable)
* Database
 management systems: MongoDB, PostgreSQL, MySQL, MySQL-lite
* Knowledge of RESTful APIs and experience in API design and
 implementation.
* Familiar with cloud platforms and DevOps practices such as CI/CD pipelines
* Other backend languages 
would be a bonus.
* Knowledge of Kubernetes or HashiCorp Nomad, or other devops technologies would be a bonus



**Role 
3**

UK Based Front end web developer to build customer facing functional UI's and internal tooling familiar with:

* Ja
vaScript,
* HTML/CSS frameworks such as bootstrap
* Experience using front end frameworks: React, Next.js
* Database man
agement systems: MongoDB, PostgreSQL, MySQL, MySQL-lite (desirable)
* Knowledge of RESTful APIs and experience in API de
sign and implementation.
* Familiar with cloud platforms and DevOps practices such as CI/CD pipelines
* Python (desirabl
e)
* Graphic design (desirable)
```
---

     
 
all -  [ Page.goto: net::ERR_TUNNEL_CONNECTION_FAILED ](https://www.reddit.com/r/Playwright/comments/1f7gdn6/pagegoto_neterr_tunnel_connection_failed/) , 2024-09-03-0911
```
Hello, I am new to playwright. Sites that worked fine locally were causing problems on the hetzner server. I wanted to u
se oxylabs' mobile proxies to prevent this. I did this in two ways: 

1) via the langchain playwright tool 

2) directly
 via the playwright library 

I encountered the same error in both. The codes I wrote are in the attached images. 

http
s://preview.redd.it/jjmogyqdcgmd1.png?width=1450&format=png&auto=webp&s=97719c9836a266bf31ef24467bec7696f79f0fd9

https:
//preview.redd.it/a25o2qrdcgmd1.png?width=1704&format=png&auto=webp&s=9c8b5f82e0fef735843f9d2f7d8a993811d59df0

I wonder
 where I am making a mistake? I applied the documentation exactly. Can you help me?
```
---

     
 
all -  [ How to extract textual data from Excel and PPTs and store in vector db for RAG? ](https://www.reddit.com/r/LangChain/comments/1f7fh83/how_to_extract_textual_data_from_excel_and_ppts/) , 2024-09-03-0911
```


I would also need to store metadata to give citations of my queried result, like the file_name, sheet_name, row_id/col
umn_id or slide numbers in case of PPTs.

Read somewhere to read the files as pandas df and store in SQL database and ru
n query agents on top of it. That is not an option. Need to use vector DB and RAG.
```
---

     
 
all -  [ 💂 Simple Python wrapper for Llama Guard 3 ](https://www.reddit.com/r/LangChain/comments/1f7e63b/simple_python_wrapper_for_llama_guard_3/) , 2024-09-03-0911
```
Llama Guard 3 is great but I was having trouble finding a good python wrapper for using it, so I built one with a bit of
 LangChain and Pydantic.

Groq has the model available for inference and recently made significant performance improveme
nts, in my basic testing it works well for interactive use cases (adds about 0.2s to e2e latency on average).

* 📖 [View
 and use source code](https://github.com/JoshuaC215/agent-service-toolkit/blob/main/src/agent/llama_guard.py)
* 🕹 Runnin
g live in my agent [here](https://agent-service-toolkit.streamlit.app/)

Take a look, use it in your projects and let me
 know what you think!

[Example usage](https://preview.redd.it/ekb5azgfwfmd1.png?width=1476&format=png&auto=webp&s=cf283
1621028b3aa0ab7fa9f7d5d278382ed6c58)


```
---

     
 
all -  [ [R] Hi, I am trying to make a virtual agent which would help people get answers to all Canadian immi ](https://www.reddit.com/r/LangChain/comments/1f7bl2y/r_hi_i_am_trying_to_make_a_virtual_agent_which/) , 2024-09-03-0911
```
Hi, I am trying to make a virtual agent which would help people get answers to all Canadian immigration related question
s. Can anyone help me with how I can get the API from the IRCC website or get datasets to fed my agent?  
Although I see
 this link : [https://search.open.canada.ca/opendata/?owner\_org=cic&page=1&sort=metadata\_modified+desc](https://search
.open.canada.ca/opendata/?owner_org=cic&page=1&sort=metadata_modified+desc) But I am unsure of how to use this.  
Thanky
ou
```
---

     
 
all -  [ non-tech education looking for an entry position in DS, how to improve chances? ](https://www.reddit.com/r/Resume/comments/1f7936g/nontech_education_looking_for_an_entry_position/) , 2024-09-03-0911
```
Hello community,

I’m a 25-year-old female currently completing my master’s thesis in Information Systems at a universit
y in Germany (max. GPA in Ger: 1.0). My academic journey began with a bachelor’s degree in Marketing and Management in m
y home country, but I later transitioned into Data Science.

As I approach the end of my studies, I’ve been actively app
lying for (Junior) Data Scientist positions. However, I’m finding the job market to be quite challenging, with limited r
esponses and few interview opportunities.

I’m eager to improve my chances of landing a role in this field, and I would 
greatly appreciate any advice or suggestions on how to enhance my approach.

Thank you in advance for your help!

https:
//preview.redd.it/oc6vn1nnvemd1.png?width=976&format=png&auto=webp&s=c09cbe6d05e5a0bccf3e5961ccc9666bc0e4c1f6


```
---

     
 
all -  [ [OFFER] python scripting, automation  and web scrapping  starts at 30$ ](https://www.reddit.com/r/slavelabour/comments/1f78snl/offer_python_scripting_automation_and_web/) , 2024-09-03-0911
```
Hello!

I'm Siva, a developer with over 4 years of experience specializing in Python scripting, automation, web scraping
, and more. I’m currently focused on building small applications and tackling a variety of tasks, including web scraping
, task automation, and data analytics.

Here’s a quick overview of what I offer:

Web Scraping: I use technologies like 
Selenium, Requests, and Beautiful Soup to gather data efficiently.

Python Scripting & Automation: I can automate repeti
tive tasks and streamline your workflows.

Chatbots & APIs: I can build interactive chatbots and work with APIs to enhan
ce your projects.

Web Development: Ready to collaborate on your next web app or digital project.

AI Integration: Lever
aging tools like Langchain and the Chat-GPT API for innovative solutions.

My rate for scripting and web scraping projec
ts starts at $30. 

To get started, please provide a detailed description of your project and your desired timeline. Con
sistent communication throughout the project is key to ensuring it meets your expectations.

If you have a project in mi
nd or need assistance with any of these tasks, feel free to place a bid and share the details. I'm here to help bring yo
ur ideas to life!



Looking forward to working with you!


```
---

     
 
all -  [ FinanceBench on my RAG with Classifier-based Filtering ](https://www.reddit.com/r/LangChain/comments/1f78rfv/financebench_on_my_rag_with_classifierbased/) , 2024-09-03-0911
```
Hi! 

Recently, I wrote about the QuePasa RAG API — an API that provides a quick entry into RAG with decent search quali
ty. 

In one of my posts, I described the classifier-based filtering algorithm that the QuePasa technology is based on: 
[https://www.reddit.com/r/Rag/comments/1f3b4sc/rag\_how\_i\_moved\_from\_reranking\_to\_classifierbased/?utm\_source=sha
re&utm\_medium=web3x&utm\_name=web3xcss&utm\_term=1&utm\_content=share\_button](https://www.reddit.com/r/Rag/comments/1f
3b4sc/rag_how_i_moved_from_reranking_to_classifierbased/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&
utm_content=share_button) 

Today, I want to talk about how we check our search capabilities.

We benchmarked against Fi
nanceBench and found that our search baseline achieves 2.5 times higher answer accuracy compared to the original study (
https://arxiv.org/pdf/2311.11944). 

In both cases, accuracy was measured across the entire document database, and the O
pen-Weights Llama model was used for fact extraction.

The original study used Chroma database, Langchain implementation
, and OpenAI embeddings for search. We used OpenAI embeddings and elastic BM25 for hybrid search + QuePasa filtering.

W
orking with benchmarks is not just a way to assess quality, but also a way to identify future development paths. For exa
mple, while working with FinanceBench — a database of financial reports and related questions — I noticed that my techno
logy struggles with classifying tables containing numerical data. So, I’m continuing to refine the QuePasa algorithm in 
this area.

Would you be interested in reading about the new results? Should I continue sharing results from other bench
marks with you?

I would be thrilled if you joined the testing of my RAG API! The easiest way to get started is by using
 the Discord bot I created — you simply upload files to the bot and ask questions: [https://discord.gg/M9RB4cRDAt](https
://discord.gg/M9RB4cRDAt)  
If you prefer to test the API directly, you can get a free API token through the same link i
n Discord.
```
---

     
 
all -  [ Does the Structured Output Feature Deteriorate ChatGPT's Output Quality? ](/r/AIQuality/comments/1f77655/does_the_structured_output_feature_deteriorate/) , 2024-09-03-0911
```

```
---

     
 
all -  [ For people who care about output quality and Evaluations in LLMs I have created r/AIQuality (one for ](https://www.reddit.com/r/LangChain/comments/1f75nln/for_people_who_care_about_output_quality_and/) , 2024-09-03-0911
```
RAG and LLMs are all over the place, and for good reason! It’s transforming how LLMs generate informed, accurate respons
es by combining them with external knowledge sources.

But with all this buzz, I noticed there’s no dedicated space to d
ive deep into LLM/RAG evaluation, share ideas, and learn together. So, I created —a community for those interested in ev
aluating LLM/RAG systems, understanding the latest research, and measuring LLM output quality.

Join us, and let's explo
re the future of AI evaluation together! link- [https://www.reddit.com/r/AIQuality/](https://www.reddit.com/r/AIQuality/
)
```
---

     
 
all -  [ Embedding and retrieval of images in RAG ](https://www.reddit.com/r/LangChain/comments/1f75gsn/embedding_and_retrieval_of_images_in_rag/) , 2024-09-03-0911
```
Hi,

for my RAG use-case I have lots of PDFs and documents that describe a software application. The UI is quite complex
 with lots of buttons and options. 

Within the technical docs there are often screenshots, providing a visual represent
ation of the text before/after it.

Since there are plenty of screenshots and there is a high level of details  in each 
of them, I am afraid the use of multimodal model to describe images will be expensive and inaccurate.

I am therefore or
iented to image embedding with some positional reference/indexing.

Are there any valuable examples or resources that im
plement it with Langchain or other frameworks?

Are there vector databases that are more suitable for this purpose?


```
---

     
 
all -  [ Langgraph state messages token limit ](https://www.reddit.com/r/LangChain/comments/1f7484p/langgraph_state_messages_token_limit/) , 2024-09-03-0911
```
Hello, for anyone using langgraph, i am struggling with the state, on state i am using messages: Annotated\[Sequence\[Ba
seMessage\],operator.add\] to save the messages and pass the state to every node. Due to RAG it sometimes exceed the tok
en limit of the llm, any idea how can i control the token limit?
```
---

     
 
all -  [ How do I connect Github with my Langgraph agent ? ](https://www.reddit.com/r/LangChain/comments/1f71dv3/how_do_i_connect_github_with_my_langgraph_agent/) , 2024-09-03-0911
```
Hello everyone , I want my Langgraph agent to be able to call Github apis .  
I want to use the Github apis to know ever
ything that I can about a user with his username .  
  
I came across 2 Langchain docs references , but both of them are
 not what I was looking for .  
  
[https://python.langchain.com/v0.2/docs/integrations/tools/github/](https://python.la
ngchain.com/v0.2/docs/integrations/tools/github/)

[https://python.langchain.com/v0.2/docs/integrations/providers/github
/](https://python.langchain.com/v0.2/docs/integrations/providers/github/) 

Help me get a solution 
```
---

     
 
all -  [ Month of August in AI ](https://www.reddit.com/r/learnmachinelearning/comments/1f6zhfe/month_of_august_in_ai/) , 2024-09-03-0911
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

     
 
all -  [ I need help with evaluation for csv data ](https://www.reddit.com/r/LangChain/comments/1f6zfwl/i_need_help_with_evaluation_for_csv_data/) , 2024-09-03-0911
```
I want to create a data analysis project using csv now.



csv data is not natural language, but data in numbers such as
 0.4, 5959, etc.



How can I create QA evaluation indicators and evaluation data for these?



Also, which RAG should I
 use to implement a high-performance csv RAG?
```
---

     
 
all -  [ Do you need Vectorized Data to perform RAG? ](https://www.reddit.com/r/Rag/comments/1f6skbm/do_you_need_vectorized_data_to_perform_rag/) , 2024-09-03-0911
```
I have some code for a religious jurisprudence assistant that uses langchain with the GPT-4o-Mini API that makes it so t
hat if the LLM detects religious content, the code activates a similarity search function after embedding the users quer
y and comparing it to a npy database of pre-embedded quotes. However, I started to notice quite soon that embedding wasn
't always accurate and that there were issues, especially with it jumping to words, sorta like semantic search. I origin
ally started with a csv file full of quotes, where sometimes they were split across lines or referenced one another (typ
ically chronologically). I don't believe the model (ada-002) was able to fully grasp the context, and therefore the embe
dding quality was skewed. I looked into the mteb leaderboard on huggingface, but for some reason I can never get those t
o work. Should I proceed to try to embed the data (maybe through somehow 'telling' the model how to do it and to place s
pecific weights) or is it possible to have plaintext RAG where I could just feed the llm the data and it would be able t
o respond properly?

  
I'd appreciate any and all help, thank you!
```
---

     
 
all -  [ Help with web scraping ](https://www.reddit.com/r/LangChain/comments/1f6pyth/help_with_web_scraping/) , 2024-09-03-0911
```
Hi everyone, is there a tool that can help navigate websites using LLM? For instance, if I need to locate the news secti
on of a specific company, I could simply provide the homepage, and the tool would find the news page for me.
```
---

     
 
all -  [ GraphRAG with existing graphs ](https://www.reddit.com/r/LangChain/comments/1f6pvx9/graphrag_with_existing_graphs/) , 2024-09-03-0911
```
how GraphRAG works with existing graphs, meaning if I already have entities and relationships, how would I load this gra
ph in GraphRAG? Can you guys help me figure out this ?
```
---

     
 
all -  [ [OFFER] I will code you almost everything in Python, for an affordable price  ](https://www.reddit.com/r/slavelabour/comments/1f6ni9s/offer_i_will_code_you_almost_everything_in_python/) , 2024-09-03-0911
```
Hey there! I'm David,

Are you drowning in boring tasks or dreaming up with exciting projects? Let me bring some coding 
magic to the table with Python.

With over 4 years of experience, I've worked in a variety of projects, including automa
tion, chatbots, APIs, web development, web scraping, and more!

What can I do for you?

* Automate the boring stuff: Say
 goodbye to repetitive tasks!

* Build Chatbots: Want a digital buddy? I can make that happen.

* Build your web app: Ti
me to build the next big thing together.

* Grab data from websites: Web scraping made easy.

* Work with AI: Using cool
 stuff like Langchain or the Chat-GPT API.

If you believe you have something that I could do for you, please place a $b
id and send me the details of the project. As always, the price depends, but It's usually from 15$ to 20$ for simple or 
intermediate projects.
```
---

     
 
all -  [ ScrapegraphAI with chatgpt ](https://www.reddit.com/r/LangChain/comments/1f6myui/scrapegraphai_with_chatgpt/) , 2024-09-03-0911
```
Here’s what I’m trying to do: using Google sheets I want to give chatgpt a prompt, the prompt requires gpt to scrape a w
ebsite and answer questions related to the website/company for example, “browse the website and tell me what brands has 
this company worked with” 

The issue here is, web browsing is not available with chatgpt API - so I’m trying to use alt
ernatives like scrapegraphAI that will work alongside chatGPT, browse the website for me and then answer the prompt. 

I
’ve been testing scrapegraph AI but it’s a bit inconsistent and I’m not entirely sure if it’s fulfilling what I need. So
 my question is, is what im trying to do possible with scrapegraph ai and if not, what is a good alternative to do what 
I need - essentially use web browsing with chatgpt api 
```
---

     
 
all -  [ Allow dangerous code ](https://www.reddit.com/r/LangChain/comments/1f6luxb/allow_dangerous_code/) , 2024-09-03-0911
```
Looking for guidance on how to navigate around the allow_dangerous_code, I understand this is a massive security risk if
 deployed in production, what are the general guidelines and safety guards that’s worth considering if using this option
 in your agents, are there alternatives? 
```
---

     
 
all -  [ Roadmap for genai  ](https://www.reddit.com/r/LangChain/comments/1f6l8rl/roadmap_for_genai/) , 2024-09-03-0911
```
Can some one pls tell me a roadmap and someone whom I can follow on YouTube or a course to get a comprehensive guide to 
genai 
```
---

     
 
all -  [ What’s more important? Observability or Evaluations? ](https://www.reddit.com/r/LangChain/comments/1f6kl5z/whats_more_important_observability_or_evaluations/) , 2024-09-03-0911
```
I am wondering what’s more important when you are building apps using LLMs? I have realized having a good observability 
lets me understand what’s going on and generally eye ball and understand how well my app is doing or the model is genera
ting responses.

I am able to optimize and iterate based on this. Which brings to my question as to whether evals are re
ally needed? Or is it more relevant for more complicated workflows? What are your thoughts?
```
---

     
 
all -  [ RAG quality/accuracy metric exist? ](https://www.reddit.com/r/LangChain/comments/1f6i6fd/rag_qualityaccuracy_metric_exist/) , 2024-09-03-0911
```
Perhaps a bit early to the industry, but is there a metric that assess the quality of the vectors retrieved in the RAG p
aradigm?
```
---

     
 
all -  [ [Student] Software eng student looking for an internship aboard This is my resume any tips? ](https://www.reddit.com/r/EngineeringResumes/comments/1f6ebmv/student_software_eng_student_looking_for_an/) , 2024-09-03-0911
```
hello everyone ! im a software eng student who is looking for a graduation intrenship aboard starting in feb 2025 ... i 
have seen few resumes and success stories over here so im trying to make mine and want to take ur opinion , anything i s
hould change or add ? and what do you think overall ... any tip or suggestion would be appreciated cause i have been fee
ling overwhelmed by this seeking journey   
thanks in advance 

https://preview.redd.it/bfbquoq587md1.jpg?width=5100&for
mat=pjpg&auto=webp&s=5ff8f060289263b70baf5772a3d2eccdc71658f6

https://preview.redd.it/iwk5frz687md1.jpg?width=5100&form
at=pjpg&auto=webp&s=cb22f00d3157be43d870aba2d3080c432255af89


```
---

     
 
all -  [ Hierarchical Indices: Optimizing RAG Systems for Complex Information Retrieval ](https://medium.com/@nirdiamant21/hierarchical-indices-enhancing-rag-systems-43c06330c085?sk=d5f97cbece2f640da8746f8da5f95188) , 2024-09-03-0911
```
I've just published a comprehensive guide on implementing hierarchical indices in RAG systems. This technique significan
tly improves handling of complex queries and large datasets.
Key points covered:

Theoretical foundation of hierarchical
 indexing
Step-by-step implementation guide
Comparison with traditional flat indexing methods
Challenges and future rese
arch directions

I've also included code examples in my GitHub repo: https://github.com/NirDiamant/RAG_Techniques
Lookin
g forward to your thoughts and experiences with similar approaches!
```
---

     
 
all -  [ How to Handle XML Files with Langchain and GPT-4o? Need Help with XPath, Node Manipulation, and Larg ](https://www.reddit.com/r/learnmachinelearning/comments/1f6dvih/how_to_handle_xml_files_with_langchain_and_gpt4o/) , 2024-09-03-0911
```
Hey everyone,

I'm currently working on a project where I need to interact with dynamically changing XML files using Lan
gchain4j or Langchain with OpenAI's GPT-4o model. The XML files I'm dealing with are quite large (over 100MB each), and 
I'm not able to include them directly in the prompts. The XML schema (XSD) is also available, but it's split across mult
iple files and spans thousands of lines.

The XML files are already parsed into Java Objects, and here's what I'm trying
 to achieve:

* Write XPath queries to navigate the XML structure.
* Retrieve specific nodes from the XML.
* Edit nodes,
 such as modifying attributes.

I've attempted to use Retrieval-Augmented Generation (RAG) and Function Calling, but nei
ther approach has provided a satisfactory solution.

Given the constraints, how can I efficiently communicate with and m
anipulate these large, dynamic XML files using Langchain(or 4j) and GPT-4o? Any advice, examples, or guidance would be g
reatly appreciated!

Thanks in advance!
```
---

     
 
all -  [ Production Grade RAG Applications ](https://www.reddit.com/r/LangChain/comments/1f6ckpw/production_grade_rag_applications/) , 2024-09-03-0911
```
I'm interested in some production grade RAG applications that can be tried online or where there's a video of someone de
moing its capabilities. What are the best RAG applications out there?

The only two I know of so far are Perplexity (whi
ch I've tried, I like it) and CoCounsel (for which I've seen an impressive demo). In particular, is there a RAG applicat
ion to chat with or run analysis tasks for large code bases?
```
---

     
 
all -  [ I built a local chatbot for managing docs, wanna test it out? [DocPOI] ](https://www.reddit.com/r/LangChain/comments/1f6b5ki/i_built_a_local_chatbot_for_managing_docs_wanna/) , 2024-09-03-0911
```
https://preview.redd.it/hsjig26cb6md1.png?width=1497&format=png&auto=webp&s=7e243b9998df63972ab4a5d2b02334a5ef2fa78e

He
y everyone! I just put together a local chatbot that helps manage and retrieve your documents securely on your own machi
ne. It’s not super polished yet and also am not a pro yet, but I’m planning to improve it. If anyone’s interested in giv
ing it a spin and providing some feedback, I'd really appreciate it!

You can check it out here: [DocPOI on GitHub](http
s://github.com/Darthph0enix7/DocPOI_repo)

Feel free to hit me up with any issues, ideas, or just to chat! We’ve got a s
mall community growing on Discord too—come join us!
```
---

     
 
all -  [ How I can Crete Knowledge Using Google Gemini API  ](https://www.reddit.com/r/LangChain/comments/1f6apg8/how_i_can_crete_knowledge_using_google_gemini_api/) , 2024-09-03-0911
```
How I can create Knowledge graph using Gemini API and docker only
```
---

     
 
all -  [ Choosing frameworks for RAG ](https://www.reddit.com/r/Rag/comments/1f65o7g/choosing_frameworks_for_rag/) , 2024-09-03-0911
```
Hello,  
I'm curious how you all are deciding which framework to use for production RAG at scale. Are you using haystack
, llamaindex, langchain? Langchain is ubiquitous in the written media about RAG, but I can't tell if it's actually being
 used in the industry for larger scale (high queries per second).   
What about the canopy framework from Pinecone? The 
framework looks reasonable, but it comes from a vector database company--do you really want vector db lock-in when it's 
early to call what the best vector db technology/provider will be?  
How are you all thinking about this and how are you
 dealing with it for now?
```
---

     
 
all -  [ Ansible Playbook & Role Generator (Python + Langchain) ](https://www.reddit.com/r/ansible/comments/1f64xgc/ansible_playbook_role_generator_python_langchain/) , 2024-09-03-0911
```
I made a ansible playbook/role generation tool. Posted about it last week but don’t think anyone noticed. :/ I think it’
s really cool and can be very helpful if you use ansible a lot. Check it out ! 

[Ansible Beam Github](https://github.co
m/bluehatkeem/ansible-beam)

Also made a YouTube vid about it. [https://youtu.be/auYgSJF5dCU?si=q02ixF_CVm_UOeIB](https:
//youtu.be/auYgSJF5dCU?si=q02ixF_CVm_UOeIB)
```
---

     
 
all -  [ Building crowdsource Genrative AI Builder Community  ](https://www.reddit.com/r/comfyui/comments/1f5zz44/building_crowdsource_genrative_ai_builder/) , 2024-09-03-0911
```
Day9, 10 & 11: Building crowdsource GenAI Builder Community

- Released newsletter for this week (Community members only
)
- Explored finetuning in more detail and creating a ppt to take session on finetuning.
- Finished Analysing Google beg
inner GenAI course and enrolled for advanced GenAI.
- Revisiting my approach to get 1st 1000 Members for AIBuilder Commu
nity. (Currently 35 Members in the community)
- New Projects code added: Building a RAG system with Meta's Llama 3.1 70B
 model using ChromaDB as vector store and langchain.
- Updating newsletter source and planning to automate.

[Community 
Access](https://discord.com/invite/dKskAgbhYH) to give your feedback and if you have any suggestions or you want to cont
ribute to build AI Builder Community together. 
```
---

     
 
all -  [ Buulding AI/GenAI croudsourced community  ](https://www.reddit.com/r/aipromptprogramming/comments/1f5z20a/buulding_aigenai_croudsourced_community/) , 2024-09-03-0911
```
Day9, 10 & 11: Building crowdsource GenAI Builder Community

I realise that Posting here on reddit with the community so
metimes helps me to keep going.
- Released newsletter for this week (Community members only)
- Explored finetuning in mo
re detail and creating a ppt to take session on finetuning.
- Finished Analysing Google beginner GenAI course and enroll
ed for advanced GenAI.
- Revisiting my approach to get 1st 1000 Members for AIBuilder Community. (Currently 35 Members i
n the community)
- New Projects code added: Building a RAG system with Meta's Llama 3.1 70B model using ChromaDB as vect
or store and langchain.
- Updating newsletter source and planning to automate.

[Community Access](https://discord.com/i
nvite/dKskAgbhYH) to give your feedback and if you have any suggestions or you want to contribute to build AI Builder Co
mmunity together. 
```
---

     
 
all -  [ Building AI/GenAI croudsourced community  ](https://www.reddit.com/r/PROJECT_AI/comments/1f5yvqa/building_aigenai_croudsourced_community/) , 2024-09-03-0911
```
Day9, 10 & 11: Building crowdsource GenAI Builder Community

I realise that Posting here on reddit with the community so
metimes helps me to keep going.
- Released newsletter for this week (Community members only)
- Explored finetuning in mo
re detail and creating a ppt to take session on finetuning.
- Finished Analysing Google beginner GenAI course and enroll
ed for advanced GenAI.
- Revisiting my approach to invite 1st 1000 Members for AIBuilder Community. (Currently 35 Member
s in the community)
- New Projects code added: Building a RAG system with Meta's Llama 3.1 70B model using ChromaDB as v
ector store and langchain.
- Updating newsletter source and planning to automate.

[Community Access](https://discord.co
m/invite/dKskAgbhYH) to give your feedback and if you have any suggestions or you want to contribute to build AI Builder
 Community together. 
```
---

     
 
all -  [ What should I use to train a model usong discord messages ](https://www.reddit.com/r/LangChain/comments/1f5ys9s/what_should_i_use_to_train_a_model_usong_discord/) , 2024-09-03-0911
```
Hello everyone, I have a big database on messages. I tried vector databases but outputs werent so different. 
```
---

     
 
all -  [ NiceGUI 2.0 with updated dependencies and some breaking changes to streamline the API ](https://www.reddit.com/r/nicegui/comments/1f5vwru/nicegui_20_with_updated_dependencies_and_some/) , 2024-09-03-0911
```
# New features and enhancements, breaking changes and migration guide

This major release introduces several new feature
s and enhancements, as well as breaking changes. We always try to keep breaking changes to a minimum, guide you through 
the migration process using deprecation warnings, and provide migration instructions. Please read the following release 
notes carefully to understand the changes and adapt your code accordingly before upgrading.

* **Semantic versioning** N
iceGUI 2.0 starts to implement [semantic versioning](https://semver.org/), which means that we will follow the MAJOR.MIN
OR.PATCH versioning scheme. This release is a major version because it introduces breaking changes. We will increment th
e MAJOR version for breaking changes, the MINOR version for new features and enhancements, and the PATCH version for bug
 fixes.
* **Fix Quasar's layout rules for** `ui.card` **that remove children's borders and shadows**⚠️ **BREAKING:** Qua
sar's QCard, the foundation of NiceGUI's [`ui.card`](https://nicegui.io/documentation/card), usually comes without any p
adding and requires nested card sections wrapping the actual content. NiceGUI simplified the use of cards by adding padd
ing, flex layout and gaps automatically. But because a QCard also removes the outer-most borders and shadows of its chil
dren, this caused unexpected results in certain cases. NiceGUI 2.0 fixes the behavior of [`ui.card`](https://nicegui.io/
documentation/card) by disabling Quasar's respective CSS rules.
* **Improve the API of** [`ui.table`](https://nicegui.io
/documentation/table)⚠️ **BREAKING:** The API for adding and removing rows in a [`ui.table`](https://nicegui.io/document
ation/table) has been improved. Passing rows as multiple arguments has been deprecated. Now these methods expect lists o
f rows.The `column` argument for `ui.table` is optional now. If not provided, the columns are infered from the first row
.A new `update_from_pandas` method has been introduced to update rows and columns from a new dataframe.A new `column_def
aults` parameter has been introduced to allow specifying some properties for all columns at once.
* **Improve support fo
r drawing items in** [`ui.leaflet`](https://nicegui.io/documentation/leaflet)⚠️ **BREAKING:** The [`ui.leaflet`](https:/
/nicegui.io/documentation/leaflet) element used to remove drawn items and required the user code to add new layers to th
e map for visualization. Now such items remain visible by default. This new behavior can be disabled by passing `hide_dr
awn_items=True` to `ui.leaflet`.
* **Unify declaration of third-party dependencies**⚠️ **BREAKING:** This release deprec
ates the `libraries`, `extra_libraries` and `exposed_libraries` parameters for subclassing `ui.element`. It introduces a
 new `dependencies` parameter to be used instead. New examples ['Custom Vue Component'](https://github.com/zauberzeug/ni
cegui/tree/main/examples/custom_vue_component) and ['Signature Pad'](https://github.com/zauberzeug/nicegui/tree/main/exa
mples/signature_pad) demonstrate how to use NPM and this parameter for integrating custom components based on third-part
y JavaScript libraries.
* **Reserve bottom space in validation elements for error messages**⚠️ **BREAKING:** UI elements
 with input validation like [`ui.input`](https://nicegui.io/documentation/input) used to omit the bottom space for a pot
ential error message. This caused a layout jump when the first error occurred. This release fixes this issue be reservin
g the space by default whenever the `validation` argument and property is not `None`. You can disable this behavior usin
g the 'hide-bottom-space' prop.
* **Remove** [`ui.timer`](https://nicegui.io/documentation/timer) **objects from UI hier
archy after they are finished:** Especially one-shot timers are now removed from the UI hierarchy after their callback h
as been executed. This avoids a potential memory leak.
* **Disable FastAPI docs by default**⚠️ **BREAKING:** NiceGUI app
s used to automatically serve FastAPI docs at /docs, /redoc, and /openapi.json. This behavior has been disabled. You can
 enable it by passing `fastapi_docs=True` to `ui.run`. Furthermore, you can specify the individual routes by setting `co
re.app.docs_url`, `core.app.redoc_url`, and `core.app.openapi_url`.
* **Make** `client.ip` **available before socket con
nection is established**⚠️ **BREAKING:** The client's IP is now already available before the page built and is returned 
to the client. On the auto-index page the `client.ip` property is `None`. If you need to check if the socket connection 
is established, use `client.has_socket_connection` instead.
* **Remove and update deprecated APIs**⚠️ **BREAKING:** Seve
ral deprecated APIs have been removed. The remaining deprecations will show warnings including the version when they wil
l be removed. Please update your code accordingly.

# Documentation and examples

* Use newer langchain package

# Pytho
n Dependencies

* Bump ruff from 0.6.2 to 0.6.3
* Bump plotly from 5.23.0 to 5.24.0
* Bump FastAPI from 0.109.2 to 0.112
.2 and remove the upper bound

# JavaScript Dependencies

The following JavaScript dependencies have been updated to the
 latest versions (#3654 by u/falkoschindler):

* Vue: 3.3.6 → 3.4.38
* Quasar: 2.13.0 → 2.16.9
* TailwindCSS: 3.2.0 → 3.
4.10
* Socket.IO: 4.7.2 → 4.7.5
* ES Module Shims: 1.8.0 → 1.10.0
* AG Grid: 30.2.0 → 32.1.0
* CodeMirror: 6.0.1 (unchan
ged)
* ECharts: 5.4.3 → 5.5.1
* ECharts-GL: 2.0.9 (unchanged)
* Leaflet: 1.9.4 (unchanged)
* Leaflet-draw: 1.0.4 (unchan
ged)
* Mermaid: 10.5.1 → 11.0.2
* nippleJS: 0.10.1 → 0.10.2
* Plotly: 2.27.0 → 2.35.0
* three.js: 0.157.0 → 0.168.0
* tw
een.js: 21.0.0 → 25.0.0
* vanilla-jsoneditor: 0.18.10 → 0.23.8

Many thanks to all contributors and users who reported i
ssues and provided feedback. We hope you enjoy this new release!
```
---

     
 
all -  [ Text2SQL Wars Vannai v/s Langchain v/s Lamadaindex Bitconfused created his while considering a frame ](https://www.reddit.com/gallery/1f5v2ip) , 2024-09-03-0911
```
Hello Guys Bit confused please which framework to choose #text2sql
In Finance Domain for correct long SQLs on SQLServer 
DataBases more that 100+ 

Considerations international usecase
Minimal spendings 💰 
Mostly Opensourced as not Customer 
Facing Directly 

```
---

     
 
MachineLearning -  [ [P] using GPT4o with langchain/chroma for sports analysis  ](https://www.reddit.com/r/MachineLearning/comments/1enuzlp/p_using_gpt4o_with_langchainchroma_for_sports/) , 2024-09-03-0911
```
Hi all, I'm working on a side project that helps with sports analysis for historical games, which in turn will help with
 sports betting. Currently I've been only focused on MLB because I wanted to see how the use case would pan out.

My fir
st attempt at this was to use the openai endpoint and load all the relevant JSON objects and send a prompt along with th
em to GPT and see what I get back. Eventually, the context size was getting way too big and the problem I was running in
to was that it was expensive. Although, the prompts back were actually pretty decent and relevant to the data.

My secon
d attempt was to setup a RAG using Chroma/LangChain/GPT4o. I got it to work but the answers all seem very off and super 
vague. None of the data I have was shown in any of the prompts i asked, or any of the players that were playing in a gam
e were mentioned at all in the prompt back, plus it kept mentioning wrong games/teams whe asking it specific games. I’m 
assuming I might need to adjust the vector store a bit but not sure how I can do that with chroma.

My question is what 
might be the best way to setup some sort of process? My end result, I would like a response back using the historical da
ta I've provided to make assumptions on what a game could be like based off all the stats given, with some room for GPT 
to also make some inference as well.

I am a super new at this so it's been a learning process so far; please bear with 
me.
```
---

     
 
MachineLearning -  [ [R] [D] Langchain Evaluation with BeyondLLM
 ](https://www.reddit.com/r/MachineLearning/comments/1eki1fv/r_d_langchain_evaluation_with_beyondllm/) , 2024-09-03-0911
```
Hey everyone! Just came across a new feature of Beyond LLM that can evaluate Langchain RAG pipelines! It provides contex
t relevancy, answer relevancy, and groundedness. Check out the code snippet I’m sharing—perfect for testing your RAG pip
elines! For more info, be sure to check it out on GitHub [here](https://github.com/aiplanethub/beyondllm/blob/main/cookb
ook/evaluate_langchain_rag_pipeline_beyondllm.ipynb).

https://preview.redd.it/172m1y3dvsgd1.png?width=3972&format=png&a
uto=webp&s=63d5b0f41f0e46a58e7a2d5fb0d2bbc4384b3b1d


```
---

     
 
deeplearning -  [ Creating a project on NLP ](https://www.reddit.com/r/deeplearning/comments/1ey2e85/creating_a_project_on_nlp/) , 2024-09-03-0911
```
So me and my friend completed the ML and DL specialization by AndrewNg, and were just gonna get started on a project. We
 decided to make a academic assistant. So basically what this does is a user can upload a PDF,text file or any other sup
ported media and the can ask questions related to it's contents. The main objective being making learning quick given la
rger documents.

The pipeline we decided is pretty standard for such a project.

1. Split the text into chunks
2. Genera
te embeddings of the chunks
3. Store the chunks in a vector DB
4. Find the top K similar chunks to the query 
5. Retriev
e context and feed it into a LLM for an answer.

So I looked up for a library and framework to use and decided on langch
ain. We haven't decided on an LLM yet but want to run it locally so no OpenAI please. 

Since this is gonna be out first
 AI project confidence is low. I would really appreciate any heads up on the issues we may face, any suggestions on libr
aries,frameworks or models will be really helpful as well. 

Appreciate any resourceful comment 😊
```
---

     
 
deeplearning -  [ How To Build Your Retrieval Augmented Generation (RAG) Using Open-source Tools: LangChain, LLAMA 3,  ](https://www.reddit.com/r/deeplearning/comments/1emdotx/how_to_build_your_retrieval_augmented_generation/) , 2024-09-03-0911
```


TL;DR: RAG overcomes the limitations of LLMs by bringing in external sources of information as relevant context.  
  

At the end of the step-by-step tutorial, you will be able to give your favorite LLM (ChatGPT, LLAMA 3, Mixtral, Gemini, 
Claude, etc.) some documents, ask it a question and see it respond based on relevant context.  
  
This will be running 
locally, using open-source libraries. Zero API and tooling costs.

[Step-by-step Notebook with zero-cost RAG](https://co
decompass00.substack.com/p/build-open-source-rag-langchain-llm-llama-chroma)

*Processing img 69v6kjfj3wgd1...*


```
---

     
 
deeplearning -  [ Need help with creating CLI for 'non-programmers' (LLMs) ](https://www.reddit.com/r/deeplearning/comments/1elrfgm/need_help_with_creating_cli_for_nonprogrammers/) , 2024-09-03-0911
```
***TL;DR*** What is the best way to convert user input into sequence of commands and their corresponding parameters? Lik
e, imagine you are not a programmer and there is a console app with a CLI, but, well, you don't know the structure and t
he syntax of commands. And you don't want to know. YBut! You have a locally running instance of llama3.1 -- or whatever 
open LLM is out there now -- and you can ask it to create a CLI command for you. What would you do to accomplish that?


**Intro**

A little bit of context. I'm working on a project that targets scientists as end users. It has some UI using 
which it's possible to do all sort of things the lab workers would like to do. But recently the projects product owner d
ecided that it would be cool to have a small chat window that is accessable basically everywhere throughout the applicat
ion UI in which 'lives' a bot that can accept some input from a user and do what is requested. The pool of commands is f
inite and predefined.

**The issue**

So, putting details aside, the main issue to be solved is parsing user input (unst
ructured and possible incomplete data) to some structured form. In general, each and every user input should be transfor
med into a data structure that represents a sequence of commands with their parameters, for example:

User input: Please
, create X with param1 set to value1 and param2 equal to value2

Desired output:

    create_x --param1 value1 --param2 
value2

In this example, there is only one command, but in real life the request can represent a sequence of N commands,
 and they may depend on each other (sequence of execution does matter)

**What I've tried so far**

I have an 'experimen
t' environment: a python project with `ollama` and `langchain` installed. The main model I test is llama3.1-instruct wit
h 5bit quantization. (I'm sort of limited with hardware resourses, so XXB parameter models do not fit).

Up until now, I
've tried to achieve what I want with prompting in different forms, but in general I do the following:

1. As the very f
irst message in the chat, I create a 'system' one which explain what commands are there. The format is the following (I 
replaced original data not to expose the context more, so it's very generic): 

```xml
<scope>
    <models>
        <mod
el name='entityA'>
            <field name='uniqueId' type='string' description='unique identifier for entityA'/>
      
      <field name='label' type='string' description='label for entityA'/>
            <field name='category' type='enum'
 possible-value='alpha, beta, gamma, delta'/>
        </model>
        <model name='entityB'>
            <field name='u
niqueId' description='unique identifier for entityB'/>
            <field name='entityAIds' type='array' description='id
entifiers of entityAs associated with this entityB'/>
        </model>
    </models>
    <commands>
        <command nam
e='create_entityA' description='creates an instance of entityA'>
            <param name='uniqueId' type='string' descri
ption='unique identifier for entityA'/>
            <param name='label' type='string' description='label for entityA' re
quired='true'/>
            <param name='category' type='enum' possible-values='alpha, beta, gamma, delta'
             
      description='category of entityA (one value from the possible values list)' required='true'/>
        </command>
 
       <command name='remove_entityA' description='removes an instance of entityA by its unique identifier'>
           
 <param name='uniqueId' description='unique identifier of the entityA to be removed'
                   required='true'/
>
        </command>
        <command name='create_entityB'>
            <param name='label' description='label for enti
tyB'/>
        </command>
        <command name='link_entityAs_to_entityB'
                 description='associates inst
ances of entityA with a specific entityB based on the provided unique identifier of entityB'>
            <param name='u
niqueId' description='unique identifier of the entityB to which entityAs should be associated'
                   requir
ed='true'/>
            <param name='entityAIds'
                   description='an array of unique identifiers of entit
yAs to associate with the entityB'
                   type='array'
                   required='true'/>
        </comman
d>
        <command name='navigate' description='indicates that a user wants to go to a specific section of the platform
'>
            <param name='section' possible-values='entitiesA, entitiesB, configuration' required='true'/>
        </c
ommand>
        <command name='support' description='should be executed when a user seeks assistance on available functi
ons'/>
    </commands>
</scope>
```

So, now the model is provided with some context. Then, also in the 'system' message
 I:

* 'tell' the model that user input should be converted into a sequence of commands along with the corresponding par
ameters, all of this is described in the XML above
* describe the desired output format
* try to enforce some restrictio
n and cover edge cases

**The question part**

*Is this approach* ***viable***\*?\*

If yes, maybe there are some ***way
s to improve it***?

If not, *what would be* ***the alternative***?

So far I don't see how to apply fine tuning here

T
hank you in advance!
```
---

     
