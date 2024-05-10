 
all -  [ Vectorsearch for chat history? ](https://www.reddit.com/r/LangChain/comments/1coaa4f/vectorsearch_for_chat_history/) , 2024-05-10-0910
```
Hi guys,
I'm working on a chatbot for our company and we use ChatGPT 4 as an LLM. To keep the costs per request low, I i
mplemented a chat history with only the last 6 messages (3 from user, 3 from bot)

The problem now is, that sometimes pe
ople have inputs that the bot can't answer well, as the messages are already gone in his memory.

Is there any good way 
to fix this? 
Is it possible to use vectorsearch for memory? Or does this heavily increase the latency?

What is the bes
t way to go, what are you guys using?
```
---

     
 
all -  [ External web search ](https://www.reddit.com/r/LocalLLaMA/comments/1coa1g3/external_web_search/) , 2024-05-10-0910
```
Hey, let's say I want to search an external web portal (apis provided) and then present the extracted context into my LL
M, can I ask what are the good libraries for this?

I heard langchain does it but I'm worried about its speed, looking f
or smaller and more lite libraries.
```
---

     
 
all -  [ LangChain ReAct Argumentation Agent ](https://www.reddit.com/r/LangChain/comments/1co86cn/langchain_react_argumentation_agent/) , 2024-05-10-0910
```
Hello,

Currently, I'm using LangChain to develop a ReAct agent to develop evidence-based arguments supporting the user'
s input. I've successfully developed a Tool that can access data from a web source based on what the model queries. ReAc
t seems like a sensible pattern for this use case, but the model gets stuck in a loop, repeatedly asking the same query 
of the tool. I've also noticed that the conversation history is not populated.

Here is the code I developed. The `searc
h_cse(query)` function just returns the title and text of an article.

    from keys import GOOGLE_GEMINI_API_KEY
    fr
om google_website_scrape import search_cse
    import langchain
    from langchain_core.tools import Tool
    from langc
hain.agents import initialize_agent, AgentType
    from langchain_google_genai import ChatGoogleGenerativeAI
    from la
ngchain.memory import ConversationBufferMemory
    
    langchain.debug = True
    
    llm = ChatGoogleGenerativeAI(
  
      model='gemini-1.0-pro',
        google_api_key=GOOGLE_GEMINI_API_KEY
    )
    tools = [
        Tool(
           
 name='cbs_articles',
            description='This tool provides the content of CBS News articles that pertain to the r
equest.',
            func=search_cse
        )
    ]
    
    PREFIX = '''You are an agent designed to construct argume
nts to fulfill the user's request, specified in the input.
    You arguments must include evidence from CBS News article
s.'''
    FORMAT_INSTRUCTIONS = '''You MUST use the following format: Question, Though, Action, Action Input. This forma
t is explained in further depth below:
    
    Question: This should be the input.
    Thought: You should think about 
arguments to fulfill the user's request.
    Action: Should ALWAYS BE 'cbs_articles'. Do NOT use any other action.
    A
ction Input: This should be a search term that will give you information pertaining to the argument you are trying to ju
stify.
    Observation: You should consider how the information you found supports your argument.
    ... (this Thought/
Action/Action Input/Observation can repeat N times)
    Thought: I now have multiple arguments WITH EVIDENCE to fulfill 
the user's request.
    Final Answer: Here are the arguments WITH EVIDENCE to fulfill the user's request.'''
    SUFFIX 
= '''Begin!
    
    Input: Justify the following: '{input}'
    Thought: {agent_scratchpad}
    Chat History: {chat_his
tory}'''
    
    memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)
    agent = initial
ize_agent(
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        tools=tools,
        llm=llm,
        agent_kwar
gs={
            'prefix': PREFIX,
            'format_instructions': FORMAT_INSTRUCTIONS,
            'suffix': SUFFIX,

            'input_variables': ['input', 'agent_scratchpad', 'chat_history']
        },
        memory=memory,
        
verbose=True,
        handle_parsing_errors=True,
        max_iterations=10
    )
    
    print(agent.run('Electric veh
icles should not be mandated nationally.'))

With this code, the model repeatedly asks itself the following.

    Questi
on: Electric vehicles should not be mandated nationally.
    Thought: Electric vehicles are still too expensive for many
 people.
    Action: cbs_articles
    Action Input: Electric vehicles cost
    Observation:
    [ARTICLE TITLE & CONTENT
]

Please advise me if I'm using the ReAct pattern incorrectly. Thank you for your time.
```
---

     
 
all -  [ Llama3 slow inference ](https://www.reddit.com/r/learnmachinelearning/comments/1co759v/llama3_slow_inference/) , 2024-05-10-0910
```
I'm currently using llama3 for a rag app. I'm using ollama and langchain's chatollama function to run inference. Prompti
ng the model takes between 10 to 30 seconds to return a json response. Is there any way to significantly reduce this inf
erence time (particularly, to under 1 sec)? 

Also, I've heard that Mojo can be used for speeding up machine learning ap
ps. Is there a Mojo implementation of llama3 available?
```
---

     
 
all -  [ RAG Retrieval Evaluation ](https://www.reddit.com/r/LangChain/comments/1co5cl1/rag_retrieval_evaluation/) , 2024-05-10-0910
```
Hey,

Like many others I am working on a RAG Q&A Chatbot.  I have many pdfs related to a certain topic. My goal is to he
lp the end-user answer questions based on the information in the pdfs. From the perspective of GIGO I am first evaluatio
n how well I can retrieve information related to certain questions. However, I am not certain about my approach.

I am u
sing precision at k, recall at k and ndcg at k as my evaluation metrics; next I simply create various pipelines starting
 from the raw pdfs, to embedding to retrieval. Here I vary the following element in the pipeline:

**Chunking:**

* Char
acterTextSplitter vs RecursiveTextSplitter
* Chuck size (400, 800, 1200)
* Chuck overlap (200, 400, 600)

**Embedding:**


* Model (ie. OpenAI vs Cohore)

**Retrieval:**

* Search method: mmr vs similarity
* Number of Documents to return \[k
\] (4, 7)
* Number of Documents to fetch to pass to MMR algorithm \[fetch-k\] (20, 40)

Retrieval is tested as follows; 
at the chunking stage I sample \~10% of the chucks and pass that to an LLM to generate questions. These are then used to
 test how well the pipeline can retrieve the chucks related to the questions.

**Now my problems:**

1. I consider a sin
gle pdf, one document. This document is then chucked, but the document ID is the same for each chuck. Meaning that if a 
question related to chuck A returns chuck Z; this would be counted as correct. While this would obviously not be correct
; I've considered changing the relation from a single page in a pdf being considered one document as this is likely more
 accurate.
2. The evaluation questions generated vary with the chuck size and method; as the given input to the LLM will
 be different. So while testing the pipeline, this is strongly affected by the quality of questions the LLM came up with
.

Are there people here with experience in testing, or does anyone know any good resources?

Thanks!
```
---

     
 
all -  [ Langchain openai FINE TUNING ](https://www.reddit.com/r/LangChain/comments/1co28ib/langchain_openai_fine_tuning/) , 2024-05-10-0910
```
I tried to do fine tuning in openai for limit the topics that my model can to speak, but the model runs bad, for example
 the result has seen like this:

GOOD: good answer 
BAD: bad answer

Q: Who is Taylor Swift? (GOOD)
A: Sorry….

Q: What 
is the sincope in life Sciences? (GOOD)
A: The sincope is…

Q: Hello (BAD)
A: sorry….

… I ask for 5 questions about Lif
e Science
Q: give me the answer of question Numbers 3 (BAD)
A: sorry….

How can I fix it ?

```
---

     
 
all -  [ Langchain allways return 429 error; este limit ](https://www.reddit.com/r/LangChain/comments/1co213w/langchain_allways_return_429_error_este_limit/) , 2024-05-10-0910
```
I have an llm built with langchain, OPENAI and qdrant; in production run well but in my local my app allways return 429 
error; I changed 5 times my tokens, I added 50$ more to my OPENAI account; but the issue persist.

Did anyone have this 
issue ?

```
---

     
 
all -  [ Looking for name of Mac App Switcher from this youtube video ](https://i.redd.it/yjt42vl79fzc1.png) , 2024-05-10-0910
```

```
---

     
 
all -  [ Limitations with existing prompt management tools?  ](https://www.reddit.com/r/LangChain/comments/1co09cc/limitations_with_existing_prompt_management_tools/) , 2024-05-10-0910
```
Hey y’all 🙌🏼 I’ve been using some prompt management tools (Humanloop and Braintrust Data) for a few of my recent project
s. Overall, they’re powerful tools but I’ve hit a few snags that make me wonder if a better tool can be built. 

I'm rea
lly interested in hearing about others' experiences with similar tools, so if you’re willing to share, that would be awe
some! 🫶🏼 

- What tool are you using? 
- How much does it cost you? 
- What kind of issues have you run into while using
 this tool?
- Are there specific features that you feel are lacking? 
- If you could build a wish list of features, what
 would they be? 🌟
```
---

     
 
all -  [ Rag response always includes reference to document  ](https://www.reddit.com/r/LangChain/comments/1cnxfnz/rag_response_always_includes_reference_to_document/) , 2024-05-10-0910
```
My org has this usecase to build a rag to answer questions. In rag works great given that I given it a lot of instructio
ns(prompts). One demand that rag isn't able to fullfill is to never mention document reference in the response.

Eg.
1) 
The document does not mention how to ...
2) you can view the steps on page 60 in the document.

Any prompt suggestions t
o overcome this particular scenario. The rag should never share the source of its response 

My pipeline

1) Pdf Documen
t Langchain 

2) Qdrant for retriever

3) Chat gpt3.5 turbo 16k for llm

```
---

     
 
all -  [ WooCommerce AI Chatbots / AI Agents ](https://www.reddit.com/r/wpsolr/comments/1cnve15/woocommerce_ai_chatbots_ai_agents/) , 2024-05-10-0910
```
We are looking to extend our [WooCommerce plugin](https://www.wpsolr.com/wpsolr-enterprise/) with AI ChatBots / AI Agent
s.  
Either something simple based on the [OpenAI Assistant API](https://platform.openai.com/docs/assistants/overview) a
nd [OpenAI Function Calling API](https://platform.openai.com/docs/guides/function-calling) .  
Or integration with full-
fledged solutions like [LangChain](https://www.langchain.com/), Vertex AI Agent builder, [Botpress](https://botpress.com
/), [FlowiseAI](https://flowiseai.com/).  
Contact me if you have any use cases in mind.
```
---

     
 
all -  [ Hi guys,what is the use of parameter K in ConversationEntityMemory? ](https://www.reddit.com/r/LangChain/comments/1cnu7zh/hi_guyswhat_is_the_use_of_parameter_k_in/) , 2024-05-10-0910
```
[https://api.python.langchain.com/en/latest/memory/langchain.memory.entity.ConversationEntityMemory.html](https://api.py
thon.langchain.com/en/latest/memory/langchain.memory.entity.ConversationEntityMemory.html)

https://preview.redd.it/ufmg
5yvirdzc1.png?width=488&format=png&auto=webp&s=ec24354784b8f84a445c4965f6064b9ed0cd838a


```
---

     
 
all -  [ Need help choosing LLM ops tool for prompt versioning ](https://www.reddit.com/r/llmops/comments/1cntvp0/need_help_choosing_llm_ops_tool_for_prompt/) , 2024-05-10-0910
```
We are a fairly big group with an already mature MLops stack, but LLMOps has been pretty hard.

In particular, prompt-it
eration hasn't been figured out by anyone.  
what's your go to tool for PromptOps ?

## PromptOps requirement:

Requirem
ents:

* Storing prompts and API to access them
* Versioning and visual diffs for results
* Evals to track improvement a
s prompts are develop .... or ability to define custom evals
* Good integration with complex langchain workflows
* Traci
ng batch evals on personal datasets, also batch evals to keep track of prompt drift
* Nice feature -> project -> run -> 
inference call heirarchy
* report generation for human evaluation of new vs old prompt results

## LLM Ops requirement -
> orchestration

* a clean way to define and visualize task vs pipeline
* think of a task as as chain or a self-containe
d operation (think summarize, search, a langchain tool)
* but then define the chaining using a low-code script -> which 
orchestrates these tools together
* that way it is easy to trace (the pipeline serves as a highl evel view) with easy pl
uggability.

Langchain is does some of the LLMOps stuff, but being able to use a cleaner abstraction on top of langchain
 would be nice.

None of the prompt ops tools have impressed so far. They all look like really thin visualization diff t
ools or thin abstractions on top of git for version control.

Most importantly, I DO NOT want to use their tooling to ru
n a low code LLM solution. They all seem to want to build some lang-flow like UI solution. This isn't ScratchLLM for god
's sake.

Also no, I refuse to change our entire architecture to be a startupName.completion() call. If you need to be s
o intrusive, then it is not a good LLMOps tools. Decorators & a listerner is the most I'll agree to.
```
---

     
 
all -  [ Having a hard time with templates  ](https://github.com/oovaa/ChatPDF/blob/main/exper%2Fcommandr.js) , 2024-05-10-0910
```
Hey everyone, I'm diving into LangChain and AI for the first time, so please bear with me as I navigate through this lea
rning curve. 

I've managed to create a small CLI bot with memory, and you can check out the GitHub link here: [GitHub L
ink] https://github.com/oovaa/ChatPDF/blob/main/exper%2Fcommandr.js. 

However, I'm encountering an issue where the bot 
interprets my name input as a command rather than part of the conversation. It seems to struggle with understanding the 
context of the conversation. I'd really appreciate some guidance on how to fix this. Thanks in advance for any help you 
can provide!
```
---

     
 
all -  [ Prompt Engineering on Phi3-mini-4K-instruct Model ](https://www.reddit.com/r/LangChain/comments/1cntf8t/prompt_engineering_on_phi3mini4kinstruct_model/) , 2024-05-10-0910
```
Hi,

I'm performing prompt engineering for my Phi3-mini-4K-instruct model and I'm using Anything LLM for my front end ap
plication.

The thing is i want my model to only answer query from the context data provided (PDFs) and Don't give any a
nswers from his own knowledge or external source. The prompt I'm giving is:

' ' 'You are an assistant for question answ
ering tasks. use the following pieces of retrieved context to answer the question. If the answer isn't present in the kn
owledge base, refrain from providing an answer based on your own knowledge. Instead of answer to such question, indicate
 that relevant information isn't available. Use three sentences maximum to keep the answer concise' ' '

After this prom
opt I'm still getting answers for the questions which are irrelevant and from outside of the knowledge base provided.
```
---

     
 
all -  [ React to typescript ](https://www.reddit.com/r/OpenAI/comments/1cnsnmq/react_to_typescript/) , 2024-05-10-0910
```
I have access to gpt 4 models in azure openai platform, can i convert react 18.2.0 code to typescript 4.9.5 using langch
ain and azure openai gpt 4 model.
 I know langchain is not necessary for conversion, but the data cut off for gpt 4 mode
l is 2021 and the latest version might not be used for train the gpt4 model. So do i have any option to use any langchai
n tool like chains or agent for this conversion as the model might need external agent support.
```
---

     
 
all -  [ Langchain agents - tools for intent classification  ](https://www.reddit.com/r/LangChain/comments/1cnqsxj/langchain_agents_tools_for_intent_classification/) , 2024-05-10-0910
```
Building an LLM app and using Unstructured for parsing data. From the vector store, have can I create a conversational a
gent that has 2 tools for intent classification? I want to create an agent so that according to user query in my applica
tion, the backend either returns a conversational output (chat) + shows sources or for some other type of user queries i
t returns only documents (no chat) akin to a generic Google search. After I create these two tools, I also want addition
al tools for the agent to recognize whether the user query is a simple greeting or whether there is any abusive language
 in the query. Any approaches, suggestions or examples would be helpful.

Thanks!
```
---

     
 
all -  [ 100 Free Courses with Certification on Udemy and Coursera ](https://www.reddit.com/r/Udemy/comments/1cnp62d/100_free_courses_with_certification_on_udemy_and/) , 2024-05-10-0910
```
Travel Writing: How to become a Travel Writer

[https://courze.org/travel-writing-how-to-become-a-travel-writer/](https:
//courze.org/travel-writing-how-to-become-a-travel-writer/)

&#x200B;

Microsoft Azure: Hands On Training: AZ-900 AZ-104
 and AZ-305

[https://courze.org/az-104-microsoft-azure-hands-on-labs/](https://courze.org/az-104-microsoft-azure-hands-
on-labs/)

&#x200B;

Docker MasterClass : Docker – Compose – SWARM – DevOps 2024

[https://courze.org/docker-masterclass
-docker-compose-swarm-devops-2024/](https://courze.org/docker-masterclass-docker-compose-swarm-devops-2024/)

&#x200B;


Python Complete Course For Python Beginners

[https://courze.org/python-complete-course-for-python-beginners/](https://c
ourze.org/python-complete-course-for-python-beginners/)

&#x200B;

Foundations of Web Development: CSS, Bootstrap, JS, R
eact

[https://courze.org/foundations-of-web-development-css-bootstrap-js-react/](https://courze.org/foundations-of-web-
development-css-bootstrap-js-react/)

&#x200B;

Business Process Simplification

[https://courze.org/business-process-si
mplification/](https://courze.org/business-process-simplification/)

&#x200B;

Root Cause Analysis: Certification

[http
s://courze.org/rca-root-cause-analysis/](https://courze.org/rca-root-cause-analysis/)

&#x200B;

Professional Diploma of
 Product Owner

[https://courze.org/professional-diploma-of-product-owner/](https://courze.org/professional-diploma-of-p
roduct-owner/)

&#x200B;

Agile Planning and OKRs: Transforming Your Project Outcomes

[https://courze.org/agile-plannin
g-and-okrs-transforming-your-project-outcomes/](https://courze.org/agile-planning-and-okrs-transforming-your-project-out
comes/)

&#x200B;

Agile Customer Research and Data-Driven Decision Making

[https://courze.org/data-driven-customer-res
earch-unlock-business-success/](https://courze.org/data-driven-customer-research-unlock-business-success/)

&#x200B;

Le
arn Maven from beginner to advanced

[https://courze.org/learn-maven-from-beginner-to-advanced/](https://courze.org/lear
n-maven-from-beginner-to-advanced/)

&#x200B;

Professional Diploma of Finance Business Partner

[https://courze.org/pro
fessional-diploma-of-finance-business-partner/](https://courze.org/professional-diploma-of-finance-business-partner/)

&
#x200B;

Professional Diploma of Marketing Manager Business Partner

[https://courze.org/professional-diploma-of-marketi
ng-manager-business-partner/](https://courze.org/professional-diploma-of-marketing-manager-business-partner/)

&#x200B;


Diploma of Microsoft Dynamics 365 CRM Business Architect

[https://courze.org/diploma-of-microsoft-dynamics-365-crm-bus
iness-architect/](https://courze.org/diploma-of-microsoft-dynamics-365-crm-business-architect/)

&#x200B;

Professional 
Diploma of Virtual Executive Assistant

[https://courze.org/professional-diploma-of-virtual-executive-assistant/](https:
//courze.org/professional-diploma-of-virtual-executive-assistant/)

&#x200B;

Professional Diploma in M&A Business Merge
rs & Acquisitions

[https://courze.org/professional-diploma-in-ma-business-mergers-acquisitions/](https://courze.org/pro
fessional-diploma-in-ma-business-mergers-acquisitions/)

&#x200B;

Microsoft Ads MasterClass – All Campaigns & Features


[https://courze.org/microsoft-ads-masterclass-2024-all-campaigns-features/](https://courze.org/microsoft-ads-masterclas
s-2024-all-campaigns-features/)

&#x200B;

Full Paid Ads Course – Google, Meta, Microsoft, LinkedIn

[https://courze.org
/full-paid-ads-course-google-facebook-microsoft-linkedin/](https://courze.org/full-paid-ads-course-google-facebook-micro
soft-linkedin/)

&#x200B;

Mastering LangChain and AWS: A Guide to Economic Analysis

[https://courze.org/mastering-lang
chain-and-aws-a-guide-to-economic-analysis/](https://courze.org/mastering-langchain-and-aws-a-guide-to-economic-analysis
/)

&#x200B;

PyTorch Ultimate 2024: From Basics to Cutting-Edge

[https://courze.org/pytorch-ultimate-2024-from-basics-
to-cutting-edge/](https://courze.org/pytorch-ultimate-2024-from-basics-to-cutting-edge/)

&#x200B;

Google Ads Crash Cou
rse – Campaign Creations

[https://courze.org/google-ads-crash-course-campaign-creations/](https://courze.org/google-ads
-crash-course-campaign-creations/)

&#x200B;

A Crash Course in Writing Well

[https://courze.org/a-crash-course-in-writ
ing-well/](https://courze.org/a-crash-course-in-writing-well/)

&#x200B;

Applied Generative AI and Natural Language Pro
cessing

[https://courze.org/applied-generative-ai-and-natural-language-processing/](https://courze.org/applied-generati
ve-ai-and-natural-language-processing/)

&#x200B;

Professional Diploma in Procurement, Sourcing, Supply Chains

[https:
//courze.org/professional-diploma-in-procurement-sourcing-supply-chains/](https://courze.org/professional-diploma-in-pro
curement-sourcing-supply-chains/)

&#x200B;

Professional Diploma of Real Estate Business Expert

[https://courze.org/pr
ofessional-diploma-of-real-estate-business-expert/](https://courze.org/professional-diploma-of-real-estate-business-expe
rt/)

&#x200B;

Masters in Structural Engineering & Drawing Reading – Etabs

[https://courze.org/diploma-in-structural-d
rawing-reading-like-expert-etabs/](https://courze.org/diploma-in-structural-drawing-reading-like-expert-etabs/)

&#x200B
;

Information Security Fundamentals

[https://courze.org/information-security-fundamentals/](https://courze.org/informa
tion-security-fundamentals/)

&#x200B;

Ultimate Miro Guide: Enhance Team Productivity & Agility

[https://courze.org/ul
timate-miro-guide-enhance-team-productivity-agility/](https://courze.org/ultimate-miro-guide-enhance-team-productivity-a
gility/)

&#x200B;

Becoming an Agile Leader: Drive Outcomes and Bring Impact

[https://courze.org/becoming-an-agile-lea
der-drive-outcomes-and-bring-impact/](https://courze.org/becoming-an-agile-leader-drive-outcomes-and-bring-impact/)

&#x
200B;

Overcoming Obstacles & Building Resilience as a Team

[https://courze.org/overcoming-obstacles-building-resilienc
e-as-a-team/](https://courze.org/overcoming-obstacles-building-resilience-as-a-team/)

&#x200B;

Agile Ways of Working W
orkshop – Practical Guide

[https://courze.org/agile-ways-of-working-workshop-practical-guide/](https://courze.org/agile
-ways-of-working-workshop-practical-guide/)

&#x200B;

Agile Transformation A to Z | How To Make Any Company Agile

[htt
ps://courze.org/agile-transformation-a-to-z-how-to-make-any-company-agile/](https://courze.org/agile-transformation-a-to
-z-how-to-make-any-company-agile/)

&#x200B;

Body Language / Non-Verbal Communication for Business

[https://courze.org
/body-language-non-verbal-communication-for-business/](https://courze.org/body-language-non-verbal-communication-for-bus
iness/)

&#x200B;

Sales: Your First 90 Days as a New Sales Representative

[https://courze.org/sales-your-first-90-days
-as-a-new-sales-representative/](https://courze.org/sales-your-first-90-days-as-a-new-sales-representative/)

&#x200B;


Defining Project Scope and Managing Resources for Project

[https://courze.org/defining-project-scope-and-managing-resou
rces-for-project/](https://courze.org/defining-project-scope-and-managing-resources-for-project/)

&#x200B;

Crea pagina
s de ventas para vender productos digi en Hotmart

[https://courze.org/crea-paginas-de-ventas-para-vender-productos-digi
-en-hotmart/](https://courze.org/crea-paginas-de-ventas-para-vender-productos-digi-en-hotmart/)

&#x200B;

Wealth Manage
ment, Private Banking & Compliance Introduction

[https://courze.org/wealth-management-private-banking-compliance-introd
uction/](https://courze.org/wealth-management-private-banking-compliance-introduction/)

&#x200B;

Professional Diploma 
in Digital Business Development

[https://courze.org/professional-diploma-in-digital-business-development/](https://cour
ze.org/professional-diploma-in-digital-business-development/)

&#x200B;

&#x200B;
```
---

     
 
all -  [ Token Limits, Consistency, & LLM in Code ](https://www.reddit.com/r/ChatGPTPro/comments/1cnhxqt/token_limits_consistency_llm_in_code/) , 2024-05-10-0910
```
**If you don’t want to read:**

* How do I address token limits without reducing tokens? Also, can someone explain top p
?
* How to improve custom GPT consistency and quantitatively measure it? I heard about temperature but what else?
* Wher
e to start for implementing LLM in code? 

**Context**

TOKEN LIMITS - I need to input over hundreds of thousands or eve
n millions of tokens in a single run (via excel/csv file). Maximum split it up into like 5-10 runs. Despite higher token
 limits, it gets lazy, gives errors, etc. 

CONSISTENCY - Custom GPT outputs are inconsistent and I need more consistenc
y. I heard about temperature and gave GPT an examples set but its still fairly inconsistent and I want to know how to me
asure this more rigorously.

LLM in PYTHON - I have experience with Python but not LLM in python. Should I start with La
ngChain and what resources should I follow? I want to experiment with this although my main concern later on is my team 
doesn’t code so I don’t know how sustainable a 'code built model' would be in the long term.

...... 

THANK YOU!
```
---

     
 
all -  [ List of FREE and Best Selling Discounted Courses ](https://www.reddit.com/r/udemyfreebies/comments/1cnhul6/list_of_free_and_best_selling_discounted_courses/) , 2024-05-10-0910
```
## Udemy Free Courses for 09 May 2024

*Note : Coupons might expire anytime, so enroll as soon as possible to get the co
urses for FREE.*

* Crea sistemas Ecommerce con PHP y MySQL V2.0[REDEEM OFFER](https://idownloadcoupon.com/udemy/4790/)

* Curso Google Sites 2024: Cómo Crear Páginas Web Desde Cero[REDEEM OFFER](https://idownloadcoupon.com/udemy/4789/)
* Cu
rso de Wix 2024: Cómo Crear una Página Web Desde Cero[REDEEM OFFER](https://idownloadcoupon.com/udemy/4788/)
* Wealth Ma
nagement, Private Banking & Compliance Introduction[REDEEM OFFER](https://idownloadcoupon.com/udemy/4787/)
* Information
 Security Fundamentals[REDEEM OFFER](https://idownloadcoupon.com/udemy/4786/)
* Professional Diploma of Product & Servic
e Business Analyst[REDEEM OFFER](https://idownloadcoupon.com/udemy/4785/)
* Arduino Practice Test: Get Certified and Tes
t Your Skills[REDEEM OFFER](https://idownloadcoupon.com/udemy/4784/)
* Automatic Irrigation System with Arduino[REDEEM O
FFER](https://idownloadcoupon.com/udemy/4783/)
* Sales: Your First 90 Days as a New Sales Representative[REDEEM OFFER](h
ttps://idownloadcoupon.com/udemy/4782/)
* The Art of Building and Sustaining Meaningful Relationships[REDEEM OFFER](http
s://idownloadcoupon.com/udemy/4781/)
* Skills Economy: Transforming to a Skills-based Organization[REDEEM OFFER](https:/
/idownloadcoupon.com/udemy/4780/)
* Body Language / Non-Verbal Communication for Business[REDEEM OFFER](https://idownloa
dcoupon.com/udemy/4779/)
* Agile Ways of Working Workshop – Practical Guide[REDEEM OFFER](https://idownloadcoupon.com/ud
emy/4777/)
* Immigrants Guide to a Successful Career in Corporate America[REDEEM OFFER](https://idownloadcoupon.com/udem
y/4776/)
* Professional Diploma of Real Estate Business Expert[REDEEM OFFER](https://idownloadcoupon.com/udemy/4775/)
* 
Masters in Structural Engineering & Drawing Reading – Etabs[REDEEM OFFER](https://idownloadcoupon.com/udemy/4774/)
* Bec
oming an Agile Leader: Drive Outcomes and Bring Impact[REDEEM OFFER](https://idownloadcoupon.com/udemy/4773/)
* Agile Tr
ansformation A to Z | How To Make Any Company Agile[REDEEM OFFER](https://idownloadcoupon.com/udemy/4772/)
* Ultimate Mi
ro Guide: Enhance Team Productivity & Agility[REDEEM OFFER](https://idownloadcoupon.com/udemy/4771/)
* Professional Dipl
oma in Procurement, Sourcing, Supply Chains[REDEEM OFFER](https://idownloadcoupon.com/udemy/4770/)
* Google Search Maste
ry Course : Find Answers 10X Times Faster[REDEEM OFFER](https://idownloadcoupon.com/udemy/4769/)
* Mastering LangChain a
nd AWS: A Guide to Economic Analysis[REDEEM OFFER](https://idownloadcoupon.com/udemy/4768/)
* Full Paid Ads Course – Goo
gle, Meta, Microsoft, LinkedIn[REDEEM OFFER](https://idownloadcoupon.com/udemy/4767/)
* Microsoft Ads MasterClass – All 
Campaigns & Features[REDEEM OFFER](https://idownloadcoupon.com/udemy/4766/)
* Google Ads Crash Course – Campaign Creatio
ns[REDEEM OFFER](https://idownloadcoupon.com/udemy/4765/)
* Professional Diploma of Virtual Executive Assistant[REDEEM O
FFER](https://idownloadcoupon.com/udemy/4764/)
* Professional Diploma in M&A Business Mergers & Acquisitions[REDEEM OFFE
R](https://idownloadcoupon.com/udemy/4763/)
* Applied Generative AI and Natural Language Processing[REDEEM OFFER](https:
//idownloadcoupon.com/udemy/4762/)
* A Crash Course in Writing Well[REDEEM OFFER](https://idownloadcoupon.com/udemy/4761
/)
* Ethical Hacking: Windows Exploitation Basics[REDEEM OFFER](https://idownloadcoupon.com/udemy/4760/)
* Ethical Hacki
ng: Reverse Shells[REDEEM OFFER](https://idownloadcoupon.com/udemy/4759/)
* Linux Terminal for beginners[REDEEM OFFER](h
ttps://idownloadcoupon.com/udemy/4758/)
```
---

     
 
all -  [ Using Airtable data as a vector database for Chatbot Knowledge Base ](https://www.reddit.com/r/LangChain/comments/1cnhb5a/using_airtable_data_as_a_vector_database_for/) , 2024-05-10-0910
```
Hello AI peeps, I need some help/advice. I’m building a fairly comprehensive chatbot which includes a RAG QnA component.
 All knowledge base data is in an Airtable, where each row/record is another piece of knowledge. 

The plan is to vector
ize the knowledge base to Pinecone via Flowise Upsert and then retrieve with OpenAI Embeddings. 

The main issue is that
 I can’t figure out how to use the columns as seperate metadata keys instead of all being vectorized in 1 piece. Is ther
e an easy solution to accomplish this? Is there a better approach overall to convert the data from Airtable into a RAG k
nowledge base? Any help would be appreciated! I mentioned Flowise because it’s the simplest way to use Langchain.
```
---

     
 
all -  [ Mastering LangChain and AWS: A Guide to Economic Analysis ](https://www.reddit.com/r/udemyfreebies/comments/1cnh8wm/mastering_langchain_and_aws_a_guide_to_economic/) , 2024-05-10-0910
```
Mastering LangChain and AWS: A Guide to Economic Analysis

https://idownloadcoupon.com/udemy/4768/
```
---

     
 
all -  [ create a 'default' or 'else' tool for ReAct agent ](https://www.reddit.com/r/LangChain/comments/1cngb56/create_a_default_or_else_tool_for_react_agent/) , 2024-05-10-0910
```
I am working on a ReAct agent that will have a couple of pre-defined tools to perform specific actions BUT we need to ha
ve some kind of 'default' or 'else' tool, what I mean is: if non of the pre-defined tools is selected by the agent then 
it will try to answer the user query using the 'else' tool, the idea is that there are some pre-defined and well known a
ctions that will be executed by the agent when tue user query matches those fine, but if there is not  a good match we s
till want the agent to be able to come up with the best answer possible(inbstead of something like: I cannot answer this
 question because I don't have a tool for it). Any ideas? I'm thinking on something as a   
`GeneralHandlerTool(BaseTool
):`  
`def _run():`  
   `....`
```
---

     
 
all -  [ Master New Skills: Access 100+ Free Udemy and Coursera Courses with Certificates ](https://www.reddit.com/r/Udemy/comments/1cnesdo/master_new_skills_access_100_free_udemy_and/) , 2024-05-10-0910
```
Microsoft Ads MasterClass – All Campaigns & Features

[https://courze.org/microsoft-ads-masterclass-2024-all-campaigns-f
eatures/](https://courze.org/microsoft-ads-masterclass-2024-all-campaigns-features/)

&#x200B;

Full Paid Ads Course – G
oogle, Meta, Microsoft, LinkedIn

[https://courze.org/full-paid-ads-course-google-facebook-microsoft-linkedin/](https://
courze.org/full-paid-ads-course-google-facebook-microsoft-linkedin/)

&#x200B;

Google Search Mastery Course : Find Answ
ers 10X Times Faster

[https://courze.org/google-search-mastery-course-find-answers-10x-times-faster/](https://courze.or
g/google-search-mastery-course-find-answers-10x-times-faster/)

&#x200B;

Mastering LangChain and AWS: A Guide to Econom
ic Analysis

[https://courze.org/mastering-langchain-and-aws-a-guide-to-economic-analysis/](https://courze.org/mastering
-langchain-and-aws-a-guide-to-economic-analysis/)

&#x200B;

React: All You Need to Know with Practical Project

[https:
//courze.org/react-all-you-need-to-know-with-practical-project/](https://courze.org/react-all-you-need-to-know-with-prac
tical-project/)

&#x200B;

PyTorch Ultimate 2024: From Basics to Cutting-Edge

[https://courze.org/pytorch-ultimate-2024
-from-basics-to-cutting-edge/](https://courze.org/pytorch-ultimate-2024-from-basics-to-cutting-edge/)

&#x200B;

Google 
Ads Crash Course – Campaign Creations

[https://courze.org/google-ads-crash-course-campaign-creations/](https://courze.o
rg/google-ads-crash-course-campaign-creations/)

&#x200B;

A Crash Course in Writing Well

[https://courze.org/a-crash-c
ourse-in-writing-well/](https://courze.org/a-crash-course-in-writing-well/)

&#x200B;

Applied Generative AI and Natural
 Language Processing

[https://courze.org/applied-generative-ai-and-natural-language-processing/](https://courze.org/app
lied-generative-ai-and-natural-language-processing/)

&#x200B;

Professional Diploma in Procurement, Sourcing, Supply Ch
ains

[https://courze.org/professional-diploma-in-procurement-sourcing-supply-chains/](https://courze.org/professional-d
iploma-in-procurement-sourcing-supply-chains/)

&#x200B;

Professional Diploma of Real Estate Business Expert

[https://
courze.org/professional-diploma-of-real-estate-business-expert/](https://courze.org/professional-diploma-of-real-estate-
business-expert/)

&#x200B;

Masters in Structural Engineering & Drawing Reading – Etabs

[https://courze.org/diploma-in
-structural-drawing-reading-like-expert-etabs/](https://courze.org/diploma-in-structural-drawing-reading-like-expert-eta
bs/)

&#x200B;

Information Security Fundamentals

[https://courze.org/information-security-fundamentals/](https://courz
e.org/information-security-fundamentals/)

&#x200B;

Ultimate Miro Guide: Enhance Team Productivity & Agility

[https://
courze.org/ultimate-miro-guide-enhance-team-productivity-agility/](https://courze.org/ultimate-miro-guide-enhance-team-p
roductivity-agility/)

&#x200B;

Becoming an Agile Leader: Drive Outcomes and Bring Impact

[https://courze.org/becoming
-an-agile-leader-drive-outcomes-and-bring-impact/](https://courze.org/becoming-an-agile-leader-drive-outcomes-and-bring-
impact/)

&#x200B;

Overcoming Obstacles & Building Resilience as a Team

[https://courze.org/overcoming-obstacles-build
ing-resilience-as-a-team/](https://courze.org/overcoming-obstacles-building-resilience-as-a-team/)

&#x200B;

Agile Ways
 of Working Workshop – Practical Guide

[https://courze.org/agile-ways-of-working-workshop-practical-guide/](https://cou
rze.org/agile-ways-of-working-workshop-practical-guide/)

&#x200B;

Agile Transformation A to Z | How To Make Any Compan
y Agile

[https://courze.org/agile-transformation-a-to-z-how-to-make-any-company-agile/](https://courze.org/agile-transf
ormation-a-to-z-how-to-make-any-company-agile/)

&#x200B;

The Complete Jenkins DevOps CI/CD Pipeline Bootcamp – 2024

[
https://courze.org/the-complete-jenkins-devops-ci-cd-pipeline-bootcamp-2023/](https://courze.org/the-complete-jenkins-de
vops-ci-cd-pipeline-bootcamp-2023/)

&#x200B;

Body Language / Non-Verbal Communication for Business

[https://courze.or
g/body-language-non-verbal-communication-for-business/](https://courze.org/body-language-non-verbal-communication-for-bu
siness/)

&#x200B;

Sales: Your First 90 Days as a New Sales Representative

[https://courze.org/sales-your-first-90-day
s-as-a-new-sales-representative/](https://courze.org/sales-your-first-90-days-as-a-new-sales-representative/)

&#x200B;


Defining Project Scope and Managing Resources for Project

[https://courze.org/defining-project-scope-and-managing-reso
urces-for-project-2/](https://courze.org/defining-project-scope-and-managing-resources-for-project-2/)

&#x200B;

Defini
ng Project Scope and Managing Resources for Project

[https://courze.org/defining-project-scope-and-managing-resources-f
or-project/](https://courze.org/defining-project-scope-and-managing-resources-for-project/)

&#x200B;

Crea paginas de v
entas para vender productos digi en Hotmart

[https://courze.org/crea-paginas-de-ventas-para-vender-productos-digi-en-ho
tmart/](https://courze.org/crea-paginas-de-ventas-para-vender-productos-digi-en-hotmart/)

&#x200B;

Wealth Management, 
Private Banking & Compliance Introduction

[https://courze.org/wealth-management-private-banking-compliance-introduction
/](https://courze.org/wealth-management-private-banking-compliance-introduction/)

&#x200B;

Professional Diploma in Dig
ital Business Development

[https://courze.org/professional-diploma-in-digital-business-development/](https://courze.org
/professional-diploma-in-digital-business-development/)

&#x200B;

Cómo Crear una Academia Online con WordPress y Tutor 
LMS

[https://courze.org/como-crear-una-academia-online-con-wordpress-y-tutor-lms/](https://courze.org/como-crear-una-ac
ademia-online-con-wordpress-y-tutor-lms/)

&#x200B;

Máster en Diseño Web con Inteligencia Artificial 2024

[https://cou
rze.org/master-en-diseno-web-con-inteligencia-artificial-2024/](https://courze.org/master-en-diseno-web-con-inteligencia
-artificial-2024/)

&#x200B;

Máster en Comercio Electrónico con WordPress 2024

[https://courze.org/master-en-comercio-
electronico-con-wordpress/](https://courze.org/master-en-comercio-electronico-con-wordpress/)

&#x200B;

Cómo Crear un B
log con WordPress Para Principiantes 2024

[https://courze.org/como-crear-un-blog-con-wordpress-para-principiantes-2023/
](https://courze.org/como-crear-un-blog-con-wordpress-para-principiantes-2023/)

&#x200B;

Revolutionize PCB Design with
 Generative AI: Future of PCB

[https://courze.org/revolutionize-pcb-design-with-generative-ai-future-of-pcb/](https://c
ourze.org/revolutionize-pcb-design-with-generative-ai-future-of-pcb/)

&#x200B;

Autonomous Mastery: Steering the Future
 of Self-Driving Cars

[https://courze.org/autonomous-mastery-steering-the-future-of-self-driving-cars/](https://courze.
org/autonomous-mastery-steering-the-future-of-self-driving-cars/)

&#x200B;

Professional Diploma of Product & Service B
usiness Analyst

[https://courze.org/professional-diploma-of-product-service-business-analyst/](https://courze.org/profe
ssional-diploma-of-product-service-business-analyst/)

&#x200B;

CSS, Bootstrap, JavaScript And PHP Stack Complete Cours
e

[https://courze.org/css-bootstrap-javascript-and-php-stack-complete-course/](https://courze.org/css-bootstrap-javascr
ipt-and-php-stack-complete-course/)

&#x200B;

Elementor Kits: Crea una Página Web con Elementor Pro

[https://courze.or
g/elementor-kits-crea-una-pagina-web-con-elementor-pro/](https://courze.org/elementor-kits-crea-una-pagina-web-con-eleme
ntor-pro/)

&#x200B;

OEE-Management (English)

[https://courze.org/oee-management-english/](https://courze.org/oee-mana
gement-english/)

&#x200B;

Online Marketing mit ChatGPT

[https://courze.org/online-marketing-mit-chatgpt/](https://cou
rze.org/online-marketing-mit-chatgpt/)

&#x200B;

Master Course : Carbon Accounting for ESG Professionals 101

[https://
courze.org/master-course-carbon-accounting-for-esg-professionals-101/](https://courze.org/master-course-carbon-accountin
g-for-esg-professionals-101/)

&#x200B;

Master Course in Cargo, Truck and Warehouse Management 2.0

[https://courze.org
/master-course-in-cargo-truck-and-warehouse-management-2-0/](https://courze.org/master-course-in-cargo-truck-and-warehou
se-management-2-0/)

&#x200B;

CDPO Course 101 : Certified Data Protection Officer

[https://courze.org/cdpo-course-101-
certified-data-protection-officer/](https://courze.org/cdpo-course-101-certified-data-protection-officer/)

&#x200B;

&#
x200B;
```
---

     
 
all -  [ Obtaining the name of the chain in the output during runtime ](https://www.reddit.com/r/LangChain/comments/1cndgig/obtaining_the_name_of_the_chain_in_the_output/) , 2024-05-10-0910
```
I was going through a [tutorial](https://www.analyticsvidhya.com/blog/2023/10/a-comprehensive-guide-to-using-chains-in-l
angchain/) about router chains. Is there a method to fetch the name of the executed chain in the output, such as 'math'.
 How can I retrieve the name of the executed chain? Also, is there a way to store the output shown below when the verbos
ity is set to True, into a variable?  
[link to image](https://imgur.com/a/axKBUfO)
```
---

     
 
all -  [ How to make Chat Prompt Template use data from JSON file?  ](https://www.reddit.com/r/flowise/comments/1cnd8el/how_to_make_chat_prompt_template_use_data_from/) , 2024-05-10-0910
```
I have the following setup. Desired result is having the chat respond based on the prompt (to be added in Human message)
, where I'll specify how characters from gameconfig.json should interact based on values from the same JSON. 

https://p
review.redd.it/sy974lxp89zc1.png?width=1950&format=png&auto=webp&s=02f5a7c44fdfcd827573bd6cec081a1a0b694e8a


```
---

     
 
all -  [ How can I access the output while the code is running? ](https://www.reddit.com/r/LangChain/comments/1cncubh/how_can_i_access_the_output_while_the_code_is/) , 2024-05-10-0910
```
During runtime, I can see, what chain is being executed. I need that information being displayed for further steps. Do y
ou know how can I access the output text while the code is being executed?
```
---

     
 
all -  [ Agent unable to access the internet ](https://www.reddit.com/r/AI_Agents/comments/1cn8ohe/agent_unable_to_access_the_internet/) , 2024-05-10-0910
```
Hey everybody ,

  
I've  built a search internet tool with EXA and although the API key seems to  work , my agent indic
ates  that he can't use it. 

Any help would be appreciated as I am beginner when it comes to coding. 

Here are the cod
es that I've used for the search tools and the agents using crewAI. 

Thank you in advance for your help : 

    import 
os
    from exa_py import Exa
    from langchain.agents import tool
    from dotenv import load_dotenv
    load_dotenv()

    
    class ExasearchToolSet():
        def _exa(self):
            return Exa(api_key=os.environ.get('EXA_API_KEY')
)
        @tool
        def search(self,query:str):
            '''Useful to search the internet about a a given topic a
nd return relevant results'''
            return self._exa().search(f'{query}',
                    use_autoprompt=True,
num_results=3)
        @tool
        def find_similar(self,url: str):
            '''Search for websites similar to url.

            the url passed in should be a URL returned from 'search''''
            return self._exa().find_similar(url
,num_results=3)
        @tool
        def get_contents(self,ids: str):
            '''gets content from website.
       
        the ids should be passed as a list,a list of ids returned from 'search''''
            ids=eval(ids)
           
 contents=str(self._exa().get_contents(ids))
            contents=contents.split('URL:')
            contents=[content[:
1000] for content in contents]
            return '\n\n'.join(contents)
    

    
    class TravelAgents:
    
        
def __init__(self):
            self.OpenAIGPT35 = ChatOpenAI(model_name='gpt-3.5-turbo', temperature=0.7)
            

            
    
        def expert_travel_agent(self):
            return Agent(
                role='Expert travel a
gent',
                backstory=dedent(f'''I am an Expert in travel planning and logistics, 
                          
      I have decades experiences making travel itineraries,
                                I easily identify good deals
,
                                My purpose is to help the user to profit from a marvelous trip at a low cost'''),
    
            goal=dedent(f'''Create a 7-days travel itinerary with detailed per-day plans,
                              
  Include budget , packing suggestions and safety tips'''),
                tools=[ExasearchToolSet.search,ExasearchTool
Set.get_contents,ExasearchToolSet.find_similar,perform_calculation],
                allow_delegation=True,
            
    verbose=True,llm=self.OpenAIGPT35,
                )
            
    
        def city_selection_expert(self):
    
        return Agent(
                role='City selection expert',
                backstory=dedent(f'''I am a city sel
ection expert,
                                I have traveled across the world and gained decades of experience.
      
                          I am able to suggest the ideal destination based on the user's interests, 
                   
             weather preferences and budget'''),
                goal=dedent(f'''Select the best cities based on weather
, price and user's interests'''),
                tools=[ExasearchToolSet.search,ExasearchToolSet.get_contents,Exasearch
ToolSet.find_similar,perform_calculation]
                       ,
                allow_delegation=True,
              
  verbose=True,
                llm=self.OpenAIGPT35,
            )
        def local_tour_guide(self):
            retu
rn Agent(
                role='Local tour guide',
                backstory=dedent(f''' I am the best when it comes to 
provide the best insights about a city and 
                                suggest to the user the best activities base
d on their personal interest 
                                 '''),
                goal=dedent(f'''Give the best insig
hts about the selected city
                            '''),
                tools=[ExasearchToolSet.search,ExasearchTo
olSet.get_contents,ExasearchToolSet.find_similar,perform_calculation]
                       ,
                allow_del
egation=False,
                verbose=True,
                llm=self.OpenAIGPT35,
            )
    

    
    
    
```
---

     
 
all -  [ changing state attributes in langgraph conditional edge? ](https://www.reddit.com/r/LangChain/comments/1cn7cjy/changing_state_attributes_in_langgraph/) , 2024-05-10-0910
```
Hey all

Im fairly new to langchain and langgraph and have a question about changing state attributes in conditional edg
e nodes  


i have this code, where im deciding if i like the answer, if i dont, i would like to return the state to ret
urn to, but also manipulate a state attribute

 

def decide\_if\_answer\_acceptable\_node(state: GraphState):  
 '''  

Determines if answer is acceptable  
   
Args  
state (dict): The current state of the graph  
   
Returns:  
str: Binar
y decision for the next node to call  
'''  
   
 if state\['answerok'\] == False or state\['answerok'\] == 'False':  
s
tate\['answer'\] = 'not OK' # <--- can i alter state attributes here?  
return 'noanswer'   
 else:  
return 'answer'   



And its linked like so:  


workflow.add\_conditional\_edges(  
 'answer\_grader\_llm\_node',  
 decide\_if\_answer\_
acceptable\_node,  
{  
 'noanswer': END,  
 'answer': END  
},  
)  


  
I understand i could blank the answer in the 
'noanswer' node, but i would like to understand if its possible to set this in the conditional edge function so i can ke
ep my code more compact?

&#x200B;

Thanks! 

&#x200B;

&#x200B;

&#x200B;
```
---

     
 
all -  [ Evaluation for RAG for extraction and restricted responses ](https://www.reddit.com/r/LangChain/comments/1cn6lau/evaluation_for_rag_for_extraction_and_restricted/) , 2024-05-10-0910
```
So, I made an information extraction system where basically, when I upload a technical data sheet of a construction mate
rial through streamlit, the LLM generates a text string in .csv format containing the attributes of the material that I 
defined to extract through the prompts (which are already embedded so it's not a Q&A system). And I linked the response 
with Gspread so that the string is automatically exported to google sheets in correct order. 

I tested and the prototyp
e is working as intended but the problem is with the evaluation of the system. Since it's part of a thesis project, I ha
ve to demonstrate how well the proposed system is performing based on certain metrics, but I am finding difficulty in lo
oking for a quantitively evaluated method that suits this use case scenario. What I want to do is to compare the perform
ances of different LLMs that are being used for the generation as well as assessing the retrieval portion of the system.


Obviously, I'm not well-versed in this area so any help is appreciated. 
```
---

     
 
all -  [ In you opinion what is the best way to interact with Anthropic models in Go? ](https://www.reddit.com/r/golang/comments/1cn5nvn/in_you_opinion_what_is_the_best_way_to_interact/) , 2024-05-10-0910
```
Hi everyone!  
I am creating a new SaaS in Go ( and it has been a pleasure, I love it so much ) and right now I need to 
interact with Opus model from Anthropic.

If you already have used, what is a good way to start?  
Simple HTTP requests 
/ some library like [https://github.com/liushuangls/go-anthropic](https://github.com/liushuangls/go-anthropic) or just u
se Langchain ( used in Python - it was a huge mess with what was happening behind the scenes ) ?

thanks!!
```
---

     
 
all -  [ How to make LLM answers more creative and find answers from the internet ](https://www.reddit.com/r/LangChain/comments/1cn3d2x/how_to_make_llm_answers_more_creative_and_find/) , 2024-05-10-0910
```
I am using Langchain to load PDF files and ask questions using RetrievalQA but when I ask to generate a solution or be c
reative it does not .It looks like it is limited to the content of the provided files only. Is there a limitation for Re
rtievalQA or just an issue with my prompts ?


```
---

     
 
all -  [ Any LangFlow update planned for LangGraph? ](https://www.reddit.com/r/LangChain/comments/1cn21xp/any_langflow_update_planned_for_langgraph/) , 2024-05-10-0910
```
Current LangGraph is just libraries for multiple Agents functionality built on Langchain but it can be more useful to ha
ve GUI within LangFlow. Any attempt to expand LangFlow with LangGraph? 
```
---

     
 
all -  [ Extract tables from PDF for RAG ](https://www.reddit.com/r/LangChain/comments/1cn0z11/extract_tables_from_pdf_for_rag/) , 2024-05-10-0910
```
To my fellow experts, I am having trouble to extract tables from PDF. I know there are some packages out there that clai
m to do the job, but I can’t seem to get good results from it. Moreover, my work laptop kinda restrict on installation o
f softwares and the most I can do is download open source library package.  Wondering if there are any straightforward w
ays on how to do that ? Or I have to a rite the code from scratch to process the tables but there seem to be many types 
of tables I need to consider. 

Here are the packages I tried and the reasons why they didn’t work. 

1. Pymupdf- messy 
table formatting, can misinterpret title of the page as column headers
2. Tabula/pdfminer- same performance as Pymupdf 

3. Camelot- I can’t seem to get it to work given that it needs to download Ghostscript and tkinter, which require admin 
privilege which is blocked in my work laptop. 
4. Unstructured- complicated setup as require a lot of dependencies and t
hey are hard to set up 
5. Llamaparse from llama: need cloud api key which is blocked 

I tried converting pdf to html b
ut can’t seem to identify the tables very well. 

Please help a beginner 🥺



 
```
---

     
 
all -  [ Choosing Between LLama CPP and Ctransformers for GPU-based LLama2/LLama3 Model Execution ](https://www.reddit.com/r/LangChain/comments/1cn08m1/choosing_between_llama_cpp_and_ctransformers_for/) , 2024-05-10-0910
```
If we are using a GPU for running the LLama2/LLama3 model, which library should I use? LLama CPP or Ctransformers? I'm a
 bit confused about both of these libraries. Can anyone please clear my doubt?
```
---

     
 
all -  [ Deep Dive: Building Affiliate.ai, a GenAI-Powered Affiliate Marketing Analytics Tool ](https://www.reddit.com/r/LangChain/comments/1cn04dj/deep_dive_building_affiliateai_a_genaipowered/) , 2024-05-10-0910
```
Hey everyone! I recently wrote a blog post about [Affiliate.ai](http://affiliate.ai/), a chat-based affiliate marketing 
analytics tool we've been working on. It simplifies the analytics process, letting you ask natural language questions an
d get insights, reports, and even spreadsheets delivered right within Microsoft Teams or Slack.

But the interesting par
t (for this audience, at least) is how it works under the hood. Here's a breakdown of some key elements:

* **Intent Dis
cernment with Function Calling:** We use simple function calling to quickly determine whether a user wants data or is ju
st chatting, ensuring the bot stays focused.
* **LLM-Powered Named Entity Recognition:** Instead of complex pipelines, w
e feed the LLM a list of advertisers and let it figure out the matches– surprisingly effective!
* **Query Reconstruction
 for Context:** Understanding context is tricky. We use a dedicated module to rewrite queries based on chat history.
* *
*Parallelization for Speed:** We run multiple potential routes simultaneously, speeding up response times dramatically.


Interested in the specifics? The full blog post has more details (link below). If you're building similar GenAI apps, I
'd love to hear about your approaches and techniques!

[https://www.affiliate.ai/post/a-technical-deepdive-into-affiliat
e-ai](https://www.affiliate.ai/post/a-technical-deepdive-into-affiliate-ai)
```
---

     
 
all -  [ LangChain with OpenAI not return full products in RAG QnA ](https://www.reddit.com/r/LangChain/comments/1cmzazp/langchain_with_openai_not_return_full_products_in/) , 2024-05-10-0910
```
0

I used the Python LangChain UnstructuredURLLoader to retrieve all our products on the company website for RAG purpose
s. The products were on different pages in the company website.

UnstructuredURLLoader was able to retrieve the products
 in multiple Document objects before they were chunked, embedded and stored in the vector database.

With the OpenAI LLM
 and RAG module, I asked the AI, **'How many products in the company A?' AI replied 'There are 11 products. You should c
heck the company A website for more info...'**

If I asked 'Please list all the products in the company A', AI replied t
he list of the 11 products only.

The problem is, there are more than 11 products. Why can't LLM read and aggregate the 
products in the Documents to count and to return all of the products?

Is there any context hint or prompt to tell LLM t
o read and return all products? Is it because of the chunking process?
```
---

     
 
all -  [ Node JS Support  ](https://www.reddit.com/r/LangChain/comments/1cmz6uh/node_js_support/) , 2024-05-10-0910
```
I am working on a Nextjs demo app that needs to use inference on a custom LLM I will train. When I deploy it, I’m planni
ng on using Baseten but for local development I am now considering  using Lanchain in Node (as opposed to setting up a F
lask server to handle inference and stream the responses back). Has anyone used it before? Is it a total disaster? know 
it’s not going to be as good as the Python version but maybe it’s good enough for my situation. 
```
---

     
 
all -  [ Discussion: Declaratively orchestrate your code instead of using LCEL  ](https://www.reddit.com/r/LangChain/comments/1cmyi9k/discussion_declaratively_orchestrate_your_code/) , 2024-05-10-0910
```
Hi All,

I'd be curious to discuss what peoples' thoughts would be on the following API to express their LLM workflows i
n place of LCEL. LangChain has the kitchen sink of things, so useful for that, but I haven't been fond of LCEL...

**LCE
L** - it's terse, but it pains me to come back to the code each time to figure out what it's going on. Then if I want to
 do anything complex it gets worse. Simple example from the docs:

    from langchain_core.output_parsers import StrOutp
utParser
    from langchain_core.prompts import ChatPromptTemplate
    from langchain_core.runnables import RunnablePass
through
    from langchain_openai import ChatOpenAI
    
    prompt = ChatPromptTemplate.from_template(
        'Tell me
 a short joke about {topic}')
    output_parser = StrOutputParser()
    model = ChatOpenAI(model='gpt-3.5-turbo')
    ch
ain = (
        {'topic': RunnablePassthrough()}
        | prompt
        | model
        | output_parser
    )
    if _
_name__ == '__main__':
        print(chain.invoke('ice cream'))

What about this **declarative API**, using a framework 
called [Hamilton](https://github.com/dagworks-inc/hamilton/) (note: I'm one of the authors)- it's more verbose, but I ca
n always clearly see how things connect and make modifications --  Hamilton knows which function to call when stitching 
things together based on the  function name and function input arguments -- as you write functions you 'declare' what th
ey are and what they require.

    # hamilton_invoke.py
    from typing import List
    
    import openai
    
    
   
 def llm_client() -> openai.OpenAI:
        return openai.OpenAI()
    
    
    def joke_prompt(topic: str) -> str:
   
     return f'Tell me a short joke about {topic}'
    
    
    def joke_messages(joke_prompt: str) -> List[dict]:
     
   return [{'role': 'user', 'content': joke_prompt}]
    
    
    def joke_response(llm_client: openai.OpenAI,
        
              joke_messages: List[dict]) -> str:
        response = llm_client.chat.completions.create(
            mode
l='gpt-3.5-turbo',
            messages=joke_messages,
        )
        return response.choices[0].message.content
    

    
    if __name__ == '__main__':
        import hamilton_invoke
    
        from hamilton import driver
    
      
  dr = (
            driver.Builder()
            .with_modules(hamilton_invoke)
            .build()
        )
        
dr.display_all_functions('hamilton-invoke.png')  # see image below
        print(dr.execute(['joke_response'],
         
                inputs={'topic': 'ice cream'}))

This image (generated by Hamilton) represents how Hamilton stitches tog
ether the code to then run it

[Result of dr.display\_all\_functions\(\\'hamilton-invoke.png\\'\)](https://preview.redd.
it/tq5ms3ltj5zc1.png?width=702&format=png&auto=webp&s=048f54f953ab50996e459b93d034771d9a943c7c)

To see more comparisons
 (e.g. conditionally swapping anthropic for openai) [click here](https://hamilton.dagworks.io/en/latest/code-comparisons
/langchain/). For code that is both Hamilton & LangChain [see this example](https://hub.dagworks.io/docs/DAGWorks/conver
sational_rag/).

Now I wouldn't use Hamilton for a simple function call -- much like I wouldn't use LangChain for that e
ither.

I'm interested in discussing thoughts and opinions to see if there's (a) appetite for this style of API, and (b)
 therefore should we integrate more closely with LangChain.  Cheers!
```
---

     
 
all -  [ If you're wondering how to make RAG with Llama 3 here is an easy starter kit ](https://www.reddit.com/r/IMadeASaaS/comments/1cmvmxl/if_youre_wondering_how_to_make_rag_with_llama_3/) , 2024-05-10-0910
```
[https://github.com/langchain-ai/langchain-nextjs-template](https://github.com/langchain-ai/langchain-nextjs-template)


&#x200B;
```
---

     
 
all -  [ Why specialized vector databases are not the future? ](https://www.reddit.com/r/LangChain/comments/1cmqx7z/why_specialized_vector_databases_are_not_the/) , 2024-05-10-0910
```
I'm thinking about writing a blog on this topic 'Why specialized vector databases are not the future?'

In this blog, I'
ll try to explain why you need Integrated vector databases rather than a specialised vector database. 

Do you have any 
arguments that support or refute this narrative?
```
---

     
 
MachineLearning -  [ [D] Self-optimizing deterministic LLM memory using dspy, neo4j and vector databases. Need your input ](https://www.reddit.com/r/MachineLearning/comments/1cakjaf/d_selfoptimizing_deterministic_llm_memory_using/) , 2024-05-10-0910
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

     
 
deeplearning -  [ Seeking Advice: Solving Data Challenges with Large Language Models (LLMs) ](https://www.reddit.com/r/deeplearning/comments/1ca4nc1/seeking_advice_solving_data_challenges_with_large/) , 2024-05-10-0910
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

     
 
deeplearning -  [ Share the Coolest Out of The Box LLM Applications That Made You Say 'Wow that was smart' ](https://www.reddit.com/r/deeplearning/comments/1c9e6dj/share_the_coolest_out_of_the_box_llm_applications/) , 2024-05-10-0910
```
Hi, I'm looking at some LLM applications today but apart from guys doing big rags with langchain I don't see too many us
es that are out of the box or that make me say 'wow that was smart to use an LLM here'. Have you seen any cool stuff usi
ng LLMs recently that made you say 'wow, that was smart'?
```
---

     
