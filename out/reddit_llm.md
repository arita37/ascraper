 
all -  [ Question on implementing Guardrail for llm app ](https://www.reddit.com/r/LangChain/comments/1f8eh8a/question_on_implementing_guardrail_for_llm_app/) , 2024-09-04-0912
```

Hi everyone,

I'm working on an LLM application and need some advice on implementing guardrails. My setup includes a ga
teway app that interprets questions and identifies the client. Based on this, it routes the request to a specific RAG (R
etrieval-Augmented Generation) setup. 

I have multiple clients, and my current configuration routes questions from Clie
nt A to RAG A and Client B to RAG B. The issue is that if I'm using Client A's services, I should only receive answers f
rom RAG A. If I accidentally ask a question meant for Client B, I need to ensure the app doesn't respond to prevent any 
data leaks.

How can I implement these guardrails effectively?

Thanks in advance for your help
```
---

     
 
all -  [ Unpopular opinion: I think out of the box RAG/GraphRAG solutions for complex domain based problems w ](https://www.reddit.com/r/LangChain/comments/1f8c9c3/unpopular_opinion_i_think_out_of_the_box/) , 2024-09-04-0912
```
I see a lot of posts on this channel where people are building RAG as a service, GraphRAG as a service, RAG API, etc. wh
ich you just put a document and start chatting. However, generally curious, do any of these work out of the box for comp
lex domain based problems such as Financial data analysis, Scientific paper analysis etc?

A RAG pipeline built for Fina
ncial data analysis would be pretty different from the one built for customer issues QnA.

I see the main problem being 
that of the index we are creating. In the VectorRAG approach, if one creates chunks without adding any domain based know
ledge, it will definitely be sub par. Retrieval will mostly miss out chunks which do not have direct semantic overlap wi
th the query.

Graph RAG seems as a rescue, as it builds out the relations. Eg. it can figure out the name, location, is
 a, has a relations. However, even that will miss out on domain based relations unless explicitly specified during graph
 creation.

Curious if it works for anyone. And in general how are folks injecting domain into their RAG systems right n
ow ?
```
---

     
 
all -  [ VectorDB for your RAG Projects ](https://www.reddit.com/r/LangChain/comments/1f85w3w/vectordb_for_your_rag_projects/) , 2024-09-04-0912
```
For your recent RAG projects using Langchain, which vector database have you used and why?
```
---

     
 
all -  [ Newbie want to setup LocalLLM used for different things ](https://www.reddit.com/r/LocalLLaMA/comments/1f83hac/newbie_want_to_setup_localllm_used_for_different/) , 2024-09-04-0912
```
Assalamu alaykum

I want to create something like copilot or chatgpt in my computer that use localLLM model.

I have mad
e up some search and I found out that implementing localLLM with RAG or LangChain can help me doing that (some sources s
uggest use both).

I just need a setup to help me get real time information from the internet with high accuracy and tha
t can fetch the information from books (PDF, EPUB…). Also, I want it to help me with programming (integrating it with VS
 Code).

Some useful information: 
- System: Arch Linux
- CPU: Ryzen 5 3600
- RAM: 16GB
- GPU: GTX 1650 Super

Thanks in
 advance 
```
---

     
 
all -  [  LangChain tool function won't take my dictionary as a parameter consistently? ](https://www.reddit.com/r/LangChain/comments/1f838o6/langchain_tool_function_wont_take_my_dictionary/) , 2024-09-04-0912
```
I'm trying to feed a dictionary to a LangChain tool function, but its not working

Here's an example with pizza when it 
works right:

    Invoking: `make_pizza` with `{pizza_data: {'dough': 'thin crust', 'sauce': 'tomato', 'toppings': ['che
ese', 'pepperoni', 'mushrooms'], 'cooking_instructions': ['preheat oven', 'bake for 15 minutes']}}`
    

But this happe
ns half the time:

    Invoking: `make_pizza` with `{'dough': 'thin crust', 'sauce': 'tomato', 'toppings': ['cheese', 'p
epperoni', 'mushrooms'], 'cooking_instructions': ['preheat oven', 'bake for 15 minutes']}`
    

My tool function looks 
like this:

    def make_pizza(pizza_data: dict):
        # ...
    error message
    1 validation error for make_pizzaS
chema
    pizza_data

Anyway of writing a prompt that will get this to work consistency 
```
---

     
 
all -  [ Understanding Semantic Chunking: Preserving Coherence and Context in Text Division ](https://medium.com/@nirdiamant21/semantic-chunking-improving-ai-information-retrieval-2f468be2d707) , 2024-09-04-0912
```
A short blog post explaining what semantic chunking is (dividing text into chunks not based on a fixed size but by cutti
ng in a way that preserves the coherence of the content and maintains a consistent context)
```
---

     
 
all -  [ [0 YoE, Unemployed, Data Scientist/MLE, India] ](https://www.reddit.com/r/resumes/comments/1f82a1f/0_yoe_unemployed_data_scientistmle_india/) , 2024-09-04-0912
```
https://preview.redd.it/2fcwm3om0mmd1.png?width=1098&format=png&auto=webp&s=9ae1b9b207040cd41956d67ed5b33c3079ef5463


```
---

     
 
all -  [ Roast my resume, third year student currently applying to internships. Want to know if i am headed i ](https://www.reddit.com/r/developersIndia/comments/1f825zy/roast_my_resume_third_year_student_currently/) , 2024-09-04-0912
```
https://preview.redd.it/u7bsg4dtzlmd1.png?width=1094&format=png&auto=webp&s=93a478736d7ca089b6786703194f9137a1cf2fe2


```
---

     
 
all -  [ How do you guys do LLM evlauation? ](https://www.reddit.com/r/LangChain/comments/1f80pd2/how_do_you_guys_do_llm_evlauation/) , 2024-09-04-0912
```
https://preview.redd.it/kwim6sdsolmd1.png?width=1434&format=png&auto=webp&s=354533f2a7ebf5983c129c9eab983c321ea80bcd


```
---

     
 
all -  [ How Minor Prompt Changes Affect LLM Outputs ](/r/AIQuality/comments/1f80g55/how_minor_prompt_changes_affect_llm_outputs/) , 2024-09-04-0912
```

```
---

     
 
all -  [ How to Attach an Image to a LangChain Agent with Tools? ](https://www.reddit.com/r/LangChain/comments/1f80bbm/how_to_attach_an_image_to_a_langchain_agent_with/) , 2024-09-04-0912
```
Has anyone figured out how to use a LangChain agent with tools and attach an image to it?

Right now, I'm working around
 this by asking the LLM to generate an image description and then using that description instead of the raw image. Howev
er, the results aren’t great—it's not capturing the nuances of the image as accurately as I’d like.

Is there a better w
ay to directly handle images with a LangChain agent? Any suggestions or workarounds would be appreciated!
```
---

     
 
all -  [ LangChain Image load vs Tesseract ](https://www.reddit.com/r/LangChain/comments/1f7z6bv/langchain_image_load_vs_tesseract/) , 2024-09-04-0912
```
I believe LangChain has the ability to extract text from images (https://python.langchain.com/v0.2/docs/integrations/doc
ument\_loaders/image/). Is it faster and more efficient than Tesseract Thank you! 

  

```
---

     
 
all -  [ Needle - The RAG Platform ](https://www.reddit.com/r/LangChain/comments/1f7z276/needle_the_rag_platform/) , 2024-09-04-0912
```
Hello, RAG community,

Since nobody (me included) likes these hidden sales posts I am very blunt here:  
'I am [Jan Heim
es](https://www.linkedin.com/in/jan-h-5164a2208/), co-founder of [Needle](https://needle-ai.com), and we just launched.'


The issue we are trying to solve is, that developers spend a lot of time building repetitive RAG pipelines. Therefore 
we abstract that process and offer an RAG service that can be called via an API. To ease the process even more we implem
ented data connectors, that sync data from different sources.  
We also have a [Python SDK](https://github.com/oeken/nee
dle-python) and [Haystack integration](https://github.com/JANHMS/needle-haystack).

We’ve put a lot of hard work into th
is, and I’d appreciate any feedback you have.

Thanks, and have a great day and if you are interested happy to chat on [
Discord](https://discord.gg/sqh3H97n).
```
---

     
 
all -  [ Welcome to DocuMindz! ](https://www.reddit.com/r/DocuMindz/comments/1f7xe4b/welcome_to_documindz/) , 2024-09-04-0912
```
[DocuMindz](https://preview.redd.it/xlmnwefxukmd1.png?width=1918&format=png&auto=webp&s=1382808947d3c0923d836d8236a1f771
1f47b792)

  
**What is DocuMindz?**

DocuMindz is an app developed using Streamlit, allowing users to efficiently searc
h and retrieve information from multiple PDF documents. It provides quick and accurate answers to your queries based on 
the content within those documents.

For those interested in code , can refer our Github repo \[ [https://github.com/Min
dzKonnectedAI/DocuMindz](https://github.com/MindzKonnectedAI/DocuMindz) \]

  
**Why DocuMindz?**

1. **Multiple PDF Sup
port:** Convert multiple PDFs to vectors and search through them simultaneously, making it easier to find the informatio
n you need across different documents.
2. **Intuitive UI:** The clean and simple interface, built using Streamlit, allow
s for easy interaction with the app, ensuring a seamless user experience.
3. **Fast and Accurate:** Powered by Langchain
, DocuMindz delivers quick and accurate answers to your questions, drawing directly from the content of your PDFs.
4. **
Authentication Mechanism:** With a built-in authentication system, DocuMindz ensures that only authorized users can acce
ss and utilize the app's features, keeping your data secure.

  
**Join Our Community!**

We’ve just launched this subre
ddit as a space for users, developers, and anyone interested in document management and retrieval to discuss, share, and
 learn more about DocuMindz.   


**What’s Next?**

Stay tuned for updates and feature announcements. Contributions are 
welcome!
```
---

     
 
all -  [ Langchain drawbacks ](https://www.reddit.com/r/ProPrompter/comments/1f7x1ww/langchain_drawbacks/) , 2024-09-04-0912
```
* Langchain initially seemed promising for quickly building a prototype chatbot, but limitations became apparent when cu
stomizations were needed;
* The project required custom logging and modifications to retriever functionality, leading to
 rewritten modules;
* Langchain's text splitting approach was found to be inadequate;
* Despite still being close to a P
roof of Concept stage, Langchain's usefulness diminished, mainly serving to improve skills in writing workarounds;
* A s
imilar experience was shared with a Discord bot project, where Langchain felt like a hastily made bot unsuitable for spe
cific needs;
* Langchain's architecture was found to be questionable, with hardcoded prompts and the need for extensive 
customization;
* Eventually, the project became so heavily customized that Langchain could be removed, leaving only the 
custom code.
```
---

     
 
all -  [ Introducing Azara! Easily build, train, deploy agentic workflows with no code ](https://www.reddit.com/r/AI_Agents/comments/1f7w3q1/introducing_azara_easily_build_train_deploy/) , 2024-09-04-0912
```
Hi everyone,

I’m excited to share something we’ve been quietly working on for the past year. After raising $1M in seed 
funding from notable investors, we’re finally ready to pull back the curtain on Azara. Azara is an agentic agents platfo
rm that brings your AI to life. We create text-to-action scenario workflows that ask clarifying questions, so nothing ge
ts lost in translation.  Built using Langchain among other tools. 

Just type or talk to Azara and watch it work. You ca
n create AI automations—no complex drag-and-drop interfaces or engineering required.

Check out [azara.ai](http://azara.
ai). Would love to hear what you think! 

https://reddit.com/link/1f7w3q1/video/hillnrwsekmd1/player


```
---

     
 
all -  [ Handling multiple functions making LLM calls ](https://www.reddit.com/r/LangChain/comments/1f7vy5q/handling_multiple_functions_making_llm_calls/) , 2024-09-04-0912
```
I have an orchestrator function which invokes a function after meeting a condition, the sub function then calls an LLM a
nd sends the response to the orchestrator, the orchestrator waits for this response and then sends this to another funct
ion making another LLM call, and so on for 4-5 times. Sometimes I may have parallel functions getting called by the orch
estrator. What would be a best approach here? 
```
---

     
 
all -  [ Introducing Azara! Build, train, deploy agentic workflows with no code. Built with Langchain ](https://www.reddit.com/r/LangChain/comments/1f7vsuf/introducing_azara_build_train_deploy_agentic/) , 2024-09-04-0912
```
Hi everyone,

I’m excited to share something we’ve been quietly working on for the past year. After raising $1M in seed 
funding from notable investors, we’re finally ready to pull back the curtain on Azara. Azara is an agentic agents platfo
rm that brings your AI to life. We created text-to-action scenario workflows that ask clarifying questions, so nothing g
ets lost in translation. It's built using Langchain among other tools.

Just type or talk to Azara and watch it work. Yo
u can create AI automations—no complex drag-and-drop interfaces or engineering required.  
  
Check out [azara.ai](https
://www.azara.ai/). Would love to hear what you think!

https://reddit.com/link/1f7vsuf/video/0ydvz7t4ckmd1/player


```
---

     
 
all -  [ [2 YoE, Working Student Data Science, Data Scientist, Germany] ](https://www.reddit.com/r/resumes/comments/1f7u82b/2_yoe_working_student_data_science_data_scientist/) , 2024-09-04-0912
```
Hello community,

I’m a 25-year-old female currently completing my master’s thesis in Information Systems at a universit
y in Germany (max. GPA in Ger: 1.0). My academic journey began with a bachelor’s degree in Marketing and Management in m
y home country, but I later transitioned into Data Science.

As I approach the end of my studies, I’ve been actively app
lying for (Junior) Data Scientist positions. However, I’m finding the job market to be quite challenging, with limited r
esponses and few interview opportunities.

I’m eager to improve my chances of landing a role in this field, and I would 
greatly appreciate any advice or suggestions on how to enhance my approach. I was thinking of removing course descriptio
ns and instead including only relevant course projects descriptions I used to take.

Thank you in advance for your help!


https://preview.redd.it/leetd75bujmd1.png?width=1000&format=png&auto=webp&s=8f6f87f660bb38915e47b468abe4679f7d0125c9


  

```
---

     
 
all -  [ Categorizing chat log ](https://www.reddit.com/r/LangChain/comments/1f7twfc/categorizing_chat_log/) , 2024-09-04-0912
```
I have a chat log of multiple people talking about different topics at once. Topic modeling doesn’t always work before i
f some says “has anyone sent in the mail” and someone replies “yes I did” it doesn’t categorize them into once. Currentl
y the best way has been to classify messages into questions and treat everything till next question as one topic. But th
at is also not accurate at times where a single conversation could have multiple questions regarding same topic. Or if a
 question is answered after another question is asked. I searched for something called as context aware threading, but d
on’t know how to get it working?
```
---

     
 
all -  [ RAG using LangChain: A step-by-step workflow! ](https://www.reddit.com/r/LangChain/comments/1f7teqe/rag_using_langchain_a_stepbystep_workflow/) , 2024-09-04-0912
```
I recently started learning about LangChain and was mind blown to see the power this AI framework has. [Created this sim
ple RAG video](https://youtu.be/TNUbBPdbsLA) where I used LangChain. Thought of sharing it to the community here for the
 feedback:)
```
---

     
 
all -  [ Parse multiple files at once without loop and single prompt for examples. Help required ](https://www.reddit.com/r/LangChain/comments/1f7sh2y/parse_multiple_files_at_once_without_loop_and/) , 2024-09-04-0912
```
I have a case where i need to parse and extract few text and numbers from multiple pdfs like more than 10000. I want to 
provide examples to the ai model so that it outputs structured text (json). How can I do it all at once instead of loopi
ng through multiple files with example prompts each time? Is it even possible something like batch processing without an
y loops? Thanks
```
---

     
 
all -  [ Best Open Source PDF Parsers for Tables? ](https://www.reddit.com/r/LangChain/comments/1f7nj10/best_open_source_pdf_parsers_for_tables/) , 2024-09-04-0912
```
I'm working on enhancing my AI assistant chatbot pipeline, which is primarily used for QA on industrial documents, user 
manuals, contracts, and legal agreements. A significant challenge I'm facing is effectively parsing PDFs that contain a 
lot of tables and images.

I’m looking for recommendations on the best open source tools or parsers that excel at extrac
ting structured data, especially from complex tables in PDFs. Any suggestions on tools that could help improve the inges
tion process for these kinds of documents would be greatly appreciated!

Thanks in advance for your help!
```
---

     
 
all -  [ Vertex AI chat returns 429 ](https://www.reddit.com/r/LangChain/comments/1f7ng5l/vertex_ai_chat_returns_429/) , 2024-09-04-0912
```
Edit: using 'chat-bison' model works. But I'm still curious why it doesn't work with gemini--1.5-flash

I'm trying to cr
eate a very simple chatbot using ChatVertexAI and following this sample https://python.langchain.com/v0.2/docs/tutorials
/chatbot/

After the second or third model.invoke call I receive following error.
Am I missing something or is this a bu
g ?

from langchain_google_vertexai import ChatVertexAI

model = ChatVertexAI(model='gemini-1.5-flash')
model.invoke([Hu
manMessage(content='Hi! I'm Bob')])

model.invoke([HumanMessage(content='Hi! Testing 429')])

model.invoke([HumanMessage
(content='Testing 429')])


' Retrying langchain_google_vertexai.chat_models._completion_with_retry.<locals>._completion
_with_retry_inner in 4.0 seconds as it raised ResourceExhausted: 429 Quota exceeded for aiplatform.googleapis.com/genera
te_content_requests_per_minute_per_project_per_base_model with base model: gemini-1.5-flash. Please submit a quota incre
ase request. https://cloud.google.com/vertex-ai/docs/generative-ai/quotas-genai..
'
```
---

     
 
all -  [ NVIDIA vs AMD vs Intel GPUs for LLMs ](https://www.reddit.com/r/huggingface/comments/1f7m5vs/nvidia_vs_amd_vs_intel_gpus_for_llms/) , 2024-09-04-0912
```
Seems like most of the models are optimized for nvidia GPUs, is anyone running LLMs on AMD or Intel? How do these compar
e with performance and integration with tools like langchain? 
```
---

     
 
all -  [ Async tool definitions using decorator  ](https://www.reddit.com/r/LangChain/comments/1f7lztx/async_tool_definitions_using_decorator/) , 2024-09-04-0912
```
How to make the agent call the functions only through asynchronous call? How should the tool definition be ?
```
---

     
 
all -  [ Building a Dynamic Query System ](https://www.reddit.com/r/LangChain/comments/1f7lneb/building_a_dynamic_query_system/) , 2024-09-04-0912
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
 ](https://www.reddit.com/r/SmythOS_/comments/1f7l3l3/langchain_vs_llamaindex_for_rag/) , 2024-09-04-0912
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

     
 
all -  [ Join an exciting UK AI Games Company to Create Something Epic! | Recruiting Development Roles for In ](https://www.reddit.com/r/gameDevClassifieds/comments/1f7hrk8/join_an_exciting_uk_ai_games_company_to_create/) , 2024-09-04-0912
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

     
 
all -  [ Page.goto: net::ERR_TUNNEL_CONNECTION_FAILED ](https://www.reddit.com/r/Playwright/comments/1f7gdn6/pagegoto_neterr_tunnel_connection_failed/) , 2024-09-04-0912
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

     
 
all -  [ How to extract textual data from Excel and PPTs and store in vector db for RAG? ](https://www.reddit.com/r/LangChain/comments/1f7fh83/how_to_extract_textual_data_from_excel_and_ppts/) , 2024-09-04-0912
```


I would also need to store metadata to give citations of my queried result, like the file_name, sheet_name, row_id/col
umn_id or slide numbers in case of PPTs.

Read somewhere to read the files as pandas df and store in SQL database and ru
n query agents on top of it. That is not an option. Need to use vector DB and RAG.
```
---

     
 
all -  [ 💂 Simple Python wrapper for Llama Guard 3 ](https://www.reddit.com/r/LangChain/comments/1f7e63b/simple_python_wrapper_for_llama_guard_3/) , 2024-09-04-0912
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

     
 
all -  [ [R] Hi, I am trying to make a virtual agent which would help people get answers to all Canadian immi ](https://www.reddit.com/r/LangChain/comments/1f7bl2y/r_hi_i_am_trying_to_make_a_virtual_agent_which/) , 2024-09-04-0912
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

     
 
all -  [ non-tech education looking for an entry position in DS, how to improve chances? ](https://www.reddit.com/r/Resume/comments/1f7936g/nontech_education_looking_for_an_entry_position/) , 2024-09-04-0912
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

     
 
all -  [ [OFFER] python scripting, automation  and web scrapping  starts at 30$ ](https://www.reddit.com/r/slavelabour/comments/1f78snl/offer_python_scripting_automation_and_web/) , 2024-09-04-0912
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

     
 
all -  [ FinanceBench on my RAG with Classifier-based Filtering ](https://www.reddit.com/r/LangChain/comments/1f78rfv/financebench_on_my_rag_with_classifierbased/) , 2024-09-04-0912
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

We benchmarked on Finance
Bench dataset and found that our search baseline achieves 2.5 times higher answer accuracy compared to the original stud
y (https://arxiv.org/pdf/2311.11944). 

In both cases, accuracy was measured across the entire document database, and th
e Open-Weights Llama model was used for fact extraction.

The original study used Chroma database, Langchain implementat
ion, and OpenAI embeddings for search. We used OpenAI embeddings and elastic BM25 for hybrid search + QuePasa filtering.


Working with benchmarks is not just a way to assess quality, but also a way to identify future development paths. For 
example, while working with FinanceBench — a database of financial reports and related questions — I noticed that my tec
hnology struggles with classifying tables containing numerical data. So, I’m continuing to refine the QuePasa algorithm 
in this area.

Would you be interested in reading about the new results? Should I continue sharing results from other be
nchmarks with you?

I would be thrilled if you joined the testing of my RAG API! The easiest way to get started is by us
ing the Discord bot I created — you simply upload files to the bot and ask questions: [https://discord.gg/M9RB4cRDAt](ht
tps://discord.gg/M9RB4cRDAt)  
If you prefer to test the API directly, you can get a free API token through the same lin
k in Discord.
```
---

     
 
all -  [ For people who care about output quality and Evaluations in LLMs I have created r/AIQuality (one for ](https://www.reddit.com/r/LangChain/comments/1f75nln/for_people_who_care_about_output_quality_and/) , 2024-09-04-0912
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

     
 
all -  [ Embedding and retrieval of images in RAG ](https://www.reddit.com/r/LangChain/comments/1f75gsn/embedding_and_retrieval_of_images_in_rag/) , 2024-09-04-0912
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

     
 
all -  [ Langgraph state messages token limit ](https://www.reddit.com/r/LangChain/comments/1f7484p/langgraph_state_messages_token_limit/) , 2024-09-04-0912
```
Hello, for anyone using langgraph, i am struggling with the state, on state i am using messages: Annotated\[Sequence\[Ba
seMessage\],operator.add\] to save the messages and pass the state to every node. Due to RAG it sometimes exceed the tok
en limit of the llm, any idea how can i control the token limit?
```
---

     
 
all -  [ How do I connect Github with my Langgraph agent ? ](https://www.reddit.com/r/LangChain/comments/1f71dv3/how_do_i_connect_github_with_my_langgraph_agent/) , 2024-09-04-0912
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

     
 
all -  [ Month of August in AI ](https://www.reddit.com/r/learnmachinelearning/comments/1f6zhfe/month_of_august_in_ai/) , 2024-09-04-0912
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

     
 
all -  [ I need help with evaluation for csv data ](https://www.reddit.com/r/LangChain/comments/1f6zfwl/i_need_help_with_evaluation_for_csv_data/) , 2024-09-04-0912
```
I want to create a data analysis project using csv now.



csv data is not natural language, but data in numbers such as
 0.4, 5959, etc.



How can I create QA evaluation indicators and evaluation data for these?



Also, which RAG should I
 use to implement a high-performance csv RAG?
```
---

     
 
all -  [ Do you need Vectorized Data to perform RAG? ](https://www.reddit.com/r/Rag/comments/1f6skbm/do_you_need_vectorized_data_to_perform_rag/) , 2024-09-04-0912
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

     
 
all -  [ Help with web scraping ](https://www.reddit.com/r/LangChain/comments/1f6pyth/help_with_web_scraping/) , 2024-09-04-0912
```
Hi everyone, is there a tool that can help navigate websites using LLM? For instance, if I need to locate the news secti
on of a specific company, I could simply provide the homepage, and the tool would find the news page for me.
```
---

     
 
all -  [ GraphRAG with existing graphs ](https://www.reddit.com/r/LangChain/comments/1f6pvx9/graphrag_with_existing_graphs/) , 2024-09-04-0912
```
how GraphRAG works with existing graphs, meaning if I already have entities and relationships, how would I load this gra
ph in GraphRAG? Can you guys help me figure out this ?
```
---

     
 
MachineLearning -  [ [P] using GPT4o with langchain/chroma for sports analysis  ](https://www.reddit.com/r/MachineLearning/comments/1enuzlp/p_using_gpt4o_with_langchainchroma_for_sports/) , 2024-09-04-0912
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
 ](https://www.reddit.com/r/MachineLearning/comments/1eki1fv/r_d_langchain_evaluation_with_beyondllm/) , 2024-09-04-0912
```
Hey everyone! Just came across a new feature of Beyond LLM that can evaluate Langchain RAG pipelines! It provides contex
t relevancy, answer relevancy, and groundedness. Check out the code snippet I’m sharing—perfect for testing your RAG pip
elines! For more info, be sure to check it out on GitHub [here](https://github.com/aiplanethub/beyondllm/blob/main/cookb
ook/evaluate_langchain_rag_pipeline_beyondllm.ipynb).

https://preview.redd.it/172m1y3dvsgd1.png?width=3972&format=png&a
uto=webp&s=63d5b0f41f0e46a58e7a2d5fb0d2bbc4384b3b1d


```
---

     
 
deeplearning -  [ Creating a project on NLP ](https://www.reddit.com/r/deeplearning/comments/1ey2e85/creating_a_project_on_nlp/) , 2024-09-04-0912
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

     
 
deeplearning -  [ How To Build Your Retrieval Augmented Generation (RAG) Using Open-source Tools: LangChain, LLAMA 3,  ](https://www.reddit.com/r/deeplearning/comments/1emdotx/how_to_build_your_retrieval_augmented_generation/) , 2024-09-04-0912
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

     
 
deeplearning -  [ Need help with creating CLI for 'non-programmers' (LLMs) ](https://www.reddit.com/r/deeplearning/comments/1elrfgm/need_help_with_creating_cli_for_nonprogrammers/) , 2024-09-04-0912
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

     
