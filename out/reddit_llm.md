 
all -  [ RAG and LLM on IOS ](https://www.reddit.com/r/LocalLLaMA/comments/1exawjq/rag_and_llm_on_ios/) , 2024-08-21-0911
```
As title suggests, is there a langchain like RAG tool for IOS that can use your LLM and answer some questions based on f
iles in IOS?
```
---

     
 
all -  [ Build a Distributed Embedding Subsystem with MinIO, Langchain, and Ray Data ](https://blog.min.io/build-a-distributed-embedding-subsystem-with-minio-langchain-and-ray-data/) , 2024-08-21-0911
```

```
---

     
 
all -  [ Project Summary: Exploring the Power of Generative AI in Healthcare ](https://www.reddit.com/r/LangChain/comments/1ex8my8/project_summary_exploring_the_power_of_generative/) , 2024-08-21-0911
```
Hey all 🤖

I wanted to share this project I've been working on with the LangChain community. It was very exploratory and
 I got a change to work from figuring out system prompts and how to use the AgentExecutor to being able to utilize LangG
raph to take my project to the next level.

Here's a summary of the tech used:

* LangChain **:** At the time, OpenAI’s 
Python package was in early development. LangChain, with its large and active developer community, was a natural choice.

* **LangGraph:** Already embedded in the LangChain ecosystem, LangGraph was a logical extension.
* **AzureOpenAI:** Whi
le I started with OpenAI, I found Azure to be more cost-effective, though it required more manual setup.
* **Spoonacular
 API:** A free, albeit limited, recipe API.
* Streamlit **UI:** Chosen for its speed and ease in creating a user interfa
ce.

  
  
I'm too lazy to rewrite the article for reddit, but here's a link to the post on LinkedIn. I think its still 
readable even if you don't have LinkedIn but let me know if its not.

 Also welcome all feedback I'm learning and growin
g, as we all are! 

[https://www.linkedin.com/pulse/exploring-power-generative-ai-healthcare-lyn-scott-jr--8ms6c/](https
://www.linkedin.com/pulse/exploring-power-generative-ai-healthcare-lyn-scott-jr--8ms6c/)
```
---

     
 
all -  [ Many chunks with small content Vs contextualCompressionRetriever ](https://www.reddit.com/r/LangChain/comments/1ex7zaq/many_chunks_with_small_content_vs/) , 2024-08-21-0911
```

I've been thinking about the use of context compression in retrieval systems. Why would anyone prefer compressing conte
xt (potentially losing information) instead of just using smaller, more granular chunks of data? In theory, breaking inf
ormation into smaller pieces should help maintain fidelity and accuracy, right?

```
---

     
 
all -  [ Working on a platform and needs suggestions on the AI Part ](https://www.reddit.com/r/LangChain/comments/1ex6h4t/working_on_a_platform_and_needs_suggestions_on/) , 2024-08-21-0911
```
Hey, I’m working on a platform where users can connect their Ads accounts, allowing us to retrieve and store their ad da
ta. Users can then interact with a chatbot to ask questions like 'How did my ads perform last week?' or 'What can I do t
o improve performance?' The chatbot provides answers based on the available data context.

Currently, I’m using a RAG ap
proach, where I chunk the data, store it in a vector database, and use LangChain to create the pipeline with a prompt te
mplate. However, I’m running into issues where the chatbot sometimes generates incorrect responses, and I’m also encount
ering token limit errors.

I’m looking for alternative methods to address these problems and would really appreciate you
r insights and feedback on this.
```
---

     
 
all -  [ Simple Agentic RAG for multi vector store application ](https://www.reddit.com/r/LangChain/comments/1ex1o0b/simple_agentic_rag_for_multi_vector_store/) , 2024-08-21-0911
```
Hello everyone,

Just finished a post on how to create a simple Agentic RAG that choose which vector stores to use. This
 is actually a good introduction to LangGraph.

Here's the link:  [link](https://www.metadocs.co/2024/08/20/simple-agent
ic-rag-for-multi-vector-stores-with-langchain-and-langgraph/).

Have a nice read!
```
---

     
 
all -  [ Check result of structured data with a tool calling to create the output (any insights?) ](https://www.reddit.com/r/LangChain/comments/1ex0kde/check_result_of_structured_data_with_a_tool/) , 2024-08-21-0911
```
I'd like to gather some data from the user input, let's say, height, weight and age.

I'm able to do that using:  
Where
 UserData is a pydantic class



    runnable = prompt | llm.with_structured_output(schema=UserData)
    result_data = r
unnable.invoke('I am 165 cm tall')



From there I can get: `height=165`

How can I add a function/tool call to the mix 
to check if I have 3 props? (height, weight and age)

The idea is for the user to chat with the bot in a 'normal' conver
sation, and whenever it flags the 3 props are gathered, it can return a calculation. On each interaction, it checks if a
ny prop is in the message; if so, adds it to the Class until it has all 3.
```
---

     
 
all -  [ Citations with Langchain RAG Agent ](https://www.reddit.com/r/LangChain/comments/1ewyfxi/citations_with_langchain_rag_agent/) , 2024-08-21-0911
```
Greetings,

I am attempting to follow this guide on creating a conversational Langchain agent.  
[https://python.langcha
in.com/v0.2/docs/tutorials/qa\_chat\_history/](https://python.langchain.com/v0.2/docs/tutorials/qa_chat_history/)

Previ
ously, my app was using the chains outlined in that guide.

  
I want to create an agent executor with the retriever as 
a tool. However, I want the agent to cite its sources from the retrieved documents.

I am struggling to implement the fu
nction-calling code to create citations with the langchain agent. This is because my program uses the llm.with\_structur
ed\_output() tool calling model. outlined in the documentation below.  
[https://python.langchain.com/v0.2/docs/how\_to/
qa\_citations/](https://python.langchain.com/v0.2/docs/how_to/qa_citations/)

I am also using the following chains.

`de
f format_docs_with_id(docs: List[Document]) -> str:`  
`formatted = [`  
`f'Source ID: {i}\nArticle Title: {doc.metadata
['title']}\nArticle Snippet: {doc.page_content}'`  
`for i, doc in enumerate(docs)`  
`]`  
`return '\n\n' + '\n\n'.join
(formatted)`

`rag_chain_from_docs = (`  
`RunnablePassthrough.assign(context=(lambda x: format_docs_with_id(x['context'
])))`  
`| prompt`  
`| structured_llm`  
`)`

`retrieve_docs = (lambda x: x['input']) | retriever`

`chain = RunnablePa
ssthrough.assign(context=retrieve_docs).assign(`  
`answer=rag_chain_from_docs`  
`)`

As far as I understand it, it is 
not possible to use the with structured output and the above LLM chains with langchain agents.

Does anyone know how to 
integrate citations with a retriver-tool-wielding langchain agent?
```
---

     
 
all -  [ create_tool_calling_agent only return tool result in json instead of a straightfoward answer ](https://www.reddit.com/r/LangChain/comments/1ewxmw5/create_tool_calling_agent_only_return_tool_result/) , 2024-08-21-0911
```
    from langchain.agents import AgentExecutor, create_tool_calling_agent
    prompt = ChatPromptTemplate.from_messages(

        [('system', 'You are a helpful Finance/Investment AI assistant.'),
            ('placeholder', '{chat_history}'
),
            ('human', '{input}'),
            ('placeholder', '{agent_scratchpad}'),]
    )
    tools = [get_income_s
tatement_tool]
    agent = create_tool_calling_agent(llm, tools, prompt)
    
    agent_executor = AgentExecutor(agent=a
gent, tools=tools, verbose=True)
    agent_executor.invoke({'input': 'what is apple's revenue on 2022? give me a short a
nswer'})from 



I built a create\_tool\_calling\_agent that has the get\_income\_statement tool, which takes in company
 ticker,start\_date, end\_date and returns corresponding income statement data. when I asked 'What is apple's revenue in
 2022? ', the agent only returned me the data from the tools in JSON format instead of a text like' Apple's revenue in 2
022 is xxxx'.( see picture) what went wrong, why can't the agent observer the tool result and return me a text with the 
answer of my question in it. Seems like the observation->rethink part of an agent is missing here

 

https://preview.re
dd.it/atshf6s61ujd1.png?width=1850&format=png&auto=webp&s=693ace0ce68cc477806beb394fca71f936bf095b

[https://smith.langc
hain.com/public/a6c6054f-47da-409e-9fdb-d30884d6b310/r](https://smith.langchain.com/public/a6c6054f-47da-409e-9fdb-d3088
4d6b310/r)

https://preview.redd.it/4egupcbb1ujd1.png?width=1097&format=png&auto=webp&s=60d49942551f76ce850452e758e13f0b
46fe4ba1


```
---

     
 
all -  [ Langsmith offline evaluators? ](https://www.reddit.com/r/LangChain/comments/1ewx37w/langsmith_offline_evaluators/) , 2024-08-21-0911
```
Hey all :)
I am wondering whether it’s possible to use offline evaluators when testing with langsmith aka models that do
 not function via API?
My concern is that i am using company data which i would rather not send over to OpenAI or any ot
her company outside of the country
Thanks 🙏🏼 
```
---

     
 
all -  [ Is this good enough to land a Django developer (remote) job ](https://i.redd.it/a8nn9d26otjd1.png) , 2024-08-21-0911
```
Hey guys I am looking for a junior Django developer role is this resume good enough to land a job ? 
```
---

     
 
all -  [ Udemy Free Courses for 20 August 2024 ](https://www.reddit.com/r/udemyfreeebies/comments/1ewu3d0/udemy_free_courses_for_20_august_2024/) , 2024-08-21-0911
```
# Udemy Free Courses for 20 August 2024

Note : Coupons might expire anytime, so enroll as soon as possible to get the c
ourses for FREE.

* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/13333/)Strategic Business Development
* [REDEEM OF
FER ](https://idownloadcoupon.com/udemy/13332/)Disruptive Thinking: Innovate and Transform Ideas
* [REDEEM OFFER ](https
://idownloadcoupon.com/udemy/13331/)Professional Relationship Building for Success
* [REDEEM OFFER ](https://idownloadco
upon.com/udemy/2534/)Linode: Web Server and Database Foundations
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/108
95/)Run Multiple Sites on an Instance: Digital Ocean & Linode
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/10065/
)Philosophy and Foundations of Artificial Intelligence (AI)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/685/)Con
figure NGINX on a Cloud Server: Digital Ocean & AWS
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/9868/)Linode: Fo
undations of Web Server Security
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/10891/)Optimizing Operations with A
I: Strategies and Applications
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/9874/)Linode: Build a Scalable Blog A
pp using PHP & MySQL DB
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/2418/)Cloud Computing Essentials: Linode, Li
nux, and LAMP Stack
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/11456/)Mastering Sales Negotiation for High-Valu
e Deals
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/11560/)HTML, CSS, React – Certification Course for Beginners

* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/11457/)Theoretical Foundations of AI in Cybersecurity
* [REDEEM OFF
ER ](https://idownloadcoupon.com/udemy/10066/)AI & Cognitive Science: Bridging Minds and Machines
* [REDEEM OFFER ](http
s://idownloadcoupon.com/udemy/10062/)Building a Sustainable Supply Chain for the Future
* Linode: Deploy Scalable React 
Web Apps on the Cloud
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/3351/)
* [REDEEM OFFER ](https://idownloadcoupo
n.com/udemy/8223/)AWS and Linode: The Ultimate Guide to Cloud Computing \[IaaS\]
* [REDEEM OFFER ](https://idownloadcoup
on.com/udemy/6215/)Linode: Build and Deploy Responsive Websites on the Cloud
* [REDEEM OFFER ](https://idownloadcoupon.c
om/udemy/11952/)Transforming Business with AI: Organization and Society
* [REDEEM OFFER ](https://idownloadcoupon.com/ud
emy/13330/)Bootstrap & jQuery – Certification Course for Beginners
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/1
3327/)Complete Bootstrap
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/13326/)Master in Business Analysis
* [REDEE
M OFFER ](https://idownloadcoupon.com/udemy/13325/)Master in Data Science, Data Analytics and Data Analysis
* [REDEEM OF
FER ](https://idownloadcoupon.com/udemy/12950/)React – Complete Developer Course with Hands-On Projects
* [REDEEM OFFER 
](https://idownloadcoupon.com/udemy/4626/)Build a Custom E-Commerce Site in React + JavaScript Basics
* [REDEEM OFFER ](
https://idownloadcoupon.com/udemy/7708/)Complete JavaScript, jQuery and React Bootcamp – Hands-On
* [REDEEM OFFER ](http
s://idownloadcoupon.com/udemy/2540/)Complete JavaScript, XML, AJAX and React Bootcamp – Hands-On
* [REDEEM OFFER ](https
://idownloadcoupon.com/udemy/10705/)Master in Systems Thinking
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/6164/
)How to make right career choices & choosing one for success
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/10741/)
Master in Talent Acquisition by Skilled Interview Taking
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/12579/)دليل
 شامل لكشف سر النجاح في البزنس؟
* Learn to Host Multiple Domains on one Virtual Server
* [REDEEM OFFER](https://idownloa
dcoupon.com/udemy/4634/)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/10726/)Master in Business Development and B
2B Sales & Marketing
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/10712/)Excellence in Interpersonal Skills (Peop
le & Social Skills)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/11246/)NGINX, Apache, SSL Encryption – Certifica
tion Course
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/12645/)Master in Product Management (IT)
* [REDEEM OFFER
 ](https://idownloadcoupon.com/udemy/10723/)How to become a Successful Software Programming Developer
* [REDEEM OFFER ](
https://idownloadcoupon.com/udemy/12609/)Master in Solution Architecture
* [REDEEM OFFER ](https://idownloadcoupon.com/u
demy/7707/)Build a Connect-4 Clone in React + JavaScript Foundations
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy
/7507/)Install NGINX, PHP, MySQL, SSL & WordPress on Ubuntu
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/10737/)M
aster in Software Architecture, Engineering and Development
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/11114/)B
uild a Simple Calculator in React JavaScript Foundations
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/10275/)Navi
gating the Crypto Universe
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/10843/)Python & Django | The Complete Dja
ngo Web Development Course
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/12643/)Master in Game Theory
* [REDEEM OF
FER ](https://idownloadcoupon.com/udemy/8625/)Ultimate Front-End Bootcamp: CSS, Bootstrap, JQ, JS, React
* [REDEEM OFFER
 ](https://idownloadcoupon.com/udemy/13324/)Master in Sales Management
* Master in Product Design
* [REDEEM OFFER](https
://idownloadcoupon.com/udemy/13323/)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/13322/)Scrum Master PSM 2 – Moc
k Tests
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/10722/)Master in Business Administration (MBA)
* [REDEEM OFF
ER ](https://idownloadcoupon.com/udemy/7224/)Essential Photoshop Course for Beginner to Advanced
* [REDEEM OFFER ](https
://idownloadcoupon.com/udemy/11158/)Master in Brand Strategy and Brand Management
* [REDEEM OFFER ](https://idownloadcou
pon.com/udemy/12152/)Graphics Design and Video Editing Course for Beginner
* [REDEEM OFFER ](https://idownloadcoupon.com
/udemy/7250/)Java Complete Course Using Visual Studio Code
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/7829/)Qui
ckBooks Online Bank Reconciliation
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/11565/)Design & Develop Unique Cu
stomer Value / Selling Proposition
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/5234/)The Beginner’s Guide to Bas
h Scripting and Automation
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/10113/)Campus Placements & Corporate Rela
tions Excellence
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/10717/)Master in Digital, Internet and Social Media
 Marketing
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/10213/)QuickBooks Desktop Bank Reconciliation
* [REDEEM O
FFER ](https://idownloadcoupon.com/udemy/11170/)Practical Fundamental Equity, Shares & Stock Analysis
* [REDEEM OFFER ](
https://idownloadcoupon.com/udemy/10721/)Master in Human Resources (HR) Management ( HRM)
* [REDEEM OFFER ](https://idow
nloadcoupon.com/udemy/7831/)Mastering QuickBooks Online 2024: A Comprehensive Guide
* Mind Power – Change Your Thought P
rocess To Change Your Life
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/7486/)
* [REDEEM OFFER ](https://idownload
coupon.com/udemy/10708/)Master Time Management for Higher Personal Productivity
* [REDEEM OFFER ](https://idownloadcoupo
n.com/udemy/7639/)Financial Accounting – Inventory Costs
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/13319/)Snow
flake Snowpark API for Python: Master Class with Project
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/13320/)\[DE
A-C01 | ARA-C01\] Snowflake Advanced Certification Prep
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/13318/)Ultim
ate Guide to Creating Presentations with PowerPoint
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/13316/)Trading e
n Gbp/Nzd – estrategia intradiaria efectiva
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/13317/)Essential Skills 
of Microsoft PowerPoint and Google Slide
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/13314/)Global Economics Pla
ybook: International Business Strategies
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/13315/)Artificial Intellige
nce Auditing, AI Tools
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/13313/)Boost Focus: Ayurvedic Concentration I
mprovement Certificate
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/13312/)Closing with confidence: techniques to
 develop your business
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/13311/)Real Estate License Exam Math
* [REDEE
M OFFER ](https://idownloadcoupon.com/udemy/13309/)Advanced Certification in Ayurveda: Master Core Principles
* [REDEEM 
OFFER ](https://idownloadcoupon.com/udemy/13306/)BMS – Building Management System Crash Course ( 2 in 1 )
* [REDEEM OFFE
R ](https://idownloadcoupon.com/udemy/13305/)IELTS Writing MASTERCLASS ( Unlock the Secrets to Band 8 )
* C, C and PHP: 
Comprehensive Programming Bootcamp
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/13307/)
* [REDEEM OFFER ](https://
idownloadcoupon.com/udemy/13308/)Advanced Ayurvedic Nutrition Certification Program – Level 1
* [REDEEM OFFER ](https://
idownloadcoupon.com/udemy/13304/)HVAC Engineering MASTER CLASS: HVAC AIR DISTRIBUTION DESIGN
* [REDEEM OFFER ](https://i
downloadcoupon.com/udemy/10276/)The Meditation Blueprint: Building Your Inner Sanctuary
* [REDEEM OFFER ](https://idownl
oadcoupon.com/udemy/12733/)Ayurvedic Daily Routine: Dinacharya Certification Course
* [REDEEM OFFER ](https://idownloadc
oupon.com/udemy/6650/)Adobe Premiere Pro CC Video Editing Course For Beginners
* [REDEEM OFFER ](https://idownloadcoupon
.com/udemy/11278/)The Beginner’s Guide to Adobe Premiere Pro: Edit Like a Pro
* [REDEEM OFFER ](https://idownloadcoupon.
com/udemy/8828/)Learn Chess in Hindi : Zero to Master Level
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/13262/)C
omplete IT Bootcamp 2025 (Part 2)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/8639/)Learn DaVinci Resolve: The C
omplete Video Editing Bootcamp
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/9923/)Natural Language Processing Cha
llenges : Exam Practice Tests
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/8726/)Learn Figma: UI/UX Design Master
class From Beginner to Pro
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/8659/)YouTube Thumbnail Design (Stunning 
Thumbnails Masterclass)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/6332/)Universidad Excel – Básico, Intermedio
 y Avanzado!
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/12355/)Find Your Ayurvedic Body Type: Diet
* [REDEEM OF
FER ](https://idownloadcoupon.com/udemy/8324/)Learn AutoCAD 2D
* Storytelling Masterclass – Business Storytelling for Le
aders
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/13084/)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/112
16/)Executive Certificate in Business Leadership
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/3596/)La fuerza int
erior para continuar: resiliencia
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/13301/)The Complete Mailchimp Emai
l Marketing Course for 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/13300/)Amazon Marketing PPC 2024 – The C
omplete Amazon Ads Course
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/13299/)Amazon FBA Course – How to Sell on 
Amazon MASTERY 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/13302/)Facebook Ads & Facebook Marketing MASTERY
 2024 | Coursenvy
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/13297/)Building a Strong Opening Repertoire
* [RED
EEM OFFER ](https://idownloadcoupon.com/udemy/13296/)Python. Estructuras de datos y algoritmos en Python
* [REDEEM OFFER
 ](https://idownloadcoupon.com/udemy/13298/)Social Media Marketing MASTERY 2024 | Ads on 10 Platforms
* [REDEEM OFFER ](
https://idownloadcoupon.com/udemy/13294/)Project Management Professional – PMP “PMBOK 6th edition”
* [REDEEM OFFER ](htt
ps://idownloadcoupon.com/udemy/13295/)Master 100 New AI Tools: The Ultimate Productivity Course
* [REDEEM OFFER ](https:
//idownloadcoupon.com/udemy/13292/)Azure Solutions Architect Certification: The Ultimate Bundle
* [REDEEM OFFER ](https:
//idownloadcoupon.com/udemy/13291/)Morning Meditation | Best Guided Meditation Under 10 Minutes
* [REDEEM OFFER ](https:
//idownloadcoupon.com/udemy/13293/)Django Masterclass : Build 9 Real World Django Projects
* [REDEEM OFFER ](https://ido
wnloadcoupon.com/udemy/12239/)Complete Generative AI Course With Langchain and Huggingface

GET MORE FREE ONLINE COURSES
 WITH CERTIFICATE – [CLICK HERE](https://idownloadcoupon.com/)
```
---

     
 
all -  [ Udemy Free Courses for 20 August 2024 ](https://www.reddit.com/r/udemyfreebies/comments/1ewu39t/udemy_free_courses_for_20_august_2024/) , 2024-08-21-0911
```
# Udemy Free Courses for 20 August 2024

Note : Coupons might expire anytime, so enroll as soon as possible to get the c
ourses for FREE.

* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/13333/)Strategic Business Development
* [REDEEM OF
FER ](https://idownloadcoupon.com/udemy/13332/)Disruptive Thinking: Innovate and Transform Ideas
* [REDEEM OFFER ](https
://idownloadcoupon.com/udemy/13331/)Professional Relationship Building for Success
* [REDEEM OFFER ](https://idownloadco
upon.com/udemy/2534/)Linode: Web Server and Database Foundations
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/108
95/)Run Multiple Sites on an Instance: Digital Ocean & Linode
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/10065/
)Philosophy and Foundations of Artificial Intelligence (AI)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/685/)Con
figure NGINX on a Cloud Server: Digital Ocean & AWS
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/9868/)Linode: Fo
undations of Web Server Security
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/10891/)Optimizing Operations with A
I: Strategies and Applications
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/9874/)Linode: Build a Scalable Blog A
pp using PHP & MySQL DB
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/2418/)Cloud Computing Essentials: Linode, Li
nux, and LAMP Stack
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/11456/)Mastering Sales Negotiation for High-Valu
e Deals
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/11560/)HTML, CSS, React – Certification Course for Beginners

* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/11457/)Theoretical Foundations of AI in Cybersecurity
* [REDEEM OFF
ER ](https://idownloadcoupon.com/udemy/10066/)AI & Cognitive Science: Bridging Minds and Machines
* [REDEEM OFFER ](http
s://idownloadcoupon.com/udemy/10062/)Building a Sustainable Supply Chain for the Future
* Linode: Deploy Scalable React 
Web Apps on the Cloud
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/3351/)
* [REDEEM OFFER ](https://idownloadcoupo
n.com/udemy/8223/)AWS and Linode: The Ultimate Guide to Cloud Computing \[IaaS\]
* [REDEEM OFFER ](https://idownloadcoup
on.com/udemy/6215/)Linode: Build and Deploy Responsive Websites on the Cloud
* [REDEEM OFFER ](https://idownloadcoupon.c
om/udemy/11952/)Transforming Business with AI: Organization and Society
* [REDEEM OFFER ](https://idownloadcoupon.com/ud
emy/13330/)Bootstrap & jQuery – Certification Course for Beginners
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/1
3327/)Complete Bootstrap
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/13326/)Master in Business Analysis
* [REDEE
M OFFER ](https://idownloadcoupon.com/udemy/13325/)Master in Data Science, Data Analytics and Data Analysis
* [REDEEM OF
FER ](https://idownloadcoupon.com/udemy/12950/)React – Complete Developer Course with Hands-On Projects
* [REDEEM OFFER 
](https://idownloadcoupon.com/udemy/4626/)Build a Custom E-Commerce Site in React + JavaScript Basics
* [REDEEM OFFER ](
https://idownloadcoupon.com/udemy/7708/)Complete JavaScript, jQuery and React Bootcamp – Hands-On
* [REDEEM OFFER ](http
s://idownloadcoupon.com/udemy/2540/)Complete JavaScript, XML, AJAX and React Bootcamp – Hands-On
* [REDEEM OFFER ](https
://idownloadcoupon.com/udemy/10705/)Master in Systems Thinking
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/6164/
)How to make right career choices & choosing one for success
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/10741/)
Master in Talent Acquisition by Skilled Interview Taking
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/12579/)دليل
 شامل لكشف سر النجاح في البزنس؟
* Learn to Host Multiple Domains on one Virtual Server
* [REDEEM OFFER](https://idownloa
dcoupon.com/udemy/4634/)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/10726/)Master in Business Development and B
2B Sales & Marketing
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/10712/)Excellence in Interpersonal Skills (Peop
le & Social Skills)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/11246/)NGINX, Apache, SSL Encryption – Certifica
tion Course
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/12645/)Master in Product Management (IT)
* [REDEEM OFFER
 ](https://idownloadcoupon.com/udemy/10723/)How to become a Successful Software Programming Developer
* [REDEEM OFFER ](
https://idownloadcoupon.com/udemy/12609/)Master in Solution Architecture
* [REDEEM OFFER ](https://idownloadcoupon.com/u
demy/7707/)Build a Connect-4 Clone in React + JavaScript Foundations
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy
/7507/)Install NGINX, PHP, MySQL, SSL & WordPress on Ubuntu
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/10737/)M
aster in Software Architecture, Engineering and Development
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/11114/)B
uild a Simple Calculator in React JavaScript Foundations
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/10275/)Navi
gating the Crypto Universe
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/10843/)Python & Django | The Complete Dja
ngo Web Development Course
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/12643/)Master in Game Theory
* [REDEEM OF
FER ](https://idownloadcoupon.com/udemy/8625/)Ultimate Front-End Bootcamp: CSS, Bootstrap, JQ, JS, React
* [REDEEM OFFER
 ](https://idownloadcoupon.com/udemy/13324/)Master in Sales Management
* Master in Product Design
* [REDEEM OFFER](https
://idownloadcoupon.com/udemy/13323/)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/13322/)Scrum Master PSM 2 – Moc
k Tests
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/10722/)Master in Business Administration (MBA)
* [REDEEM OFF
ER ](https://idownloadcoupon.com/udemy/7224/)Essential Photoshop Course for Beginner to Advanced
* [REDEEM OFFER ](https
://idownloadcoupon.com/udemy/11158/)Master in Brand Strategy and Brand Management
* [REDEEM OFFER ](https://idownloadcou
pon.com/udemy/12152/)Graphics Design and Video Editing Course for Beginner
* [REDEEM OFFER ](https://idownloadcoupon.com
/udemy/7250/)Java Complete Course Using Visual Studio Code
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/7829/)Qui
ckBooks Online Bank Reconciliation
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/11565/)Design & Develop Unique Cu
stomer Value / Selling Proposition
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/5234/)The Beginner’s Guide to Bas
h Scripting and Automation
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/10113/)Campus Placements & Corporate Rela
tions Excellence
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/10717/)Master in Digital, Internet and Social Media
 Marketing
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/10213/)QuickBooks Desktop Bank Reconciliation
* [REDEEM O
FFER ](https://idownloadcoupon.com/udemy/11170/)Practical Fundamental Equity, Shares & Stock Analysis
* [REDEEM OFFER ](
https://idownloadcoupon.com/udemy/10721/)Master in Human Resources (HR) Management ( HRM)
* [REDEEM OFFER ](https://idow
nloadcoupon.com/udemy/7831/)Mastering QuickBooks Online 2024: A Comprehensive Guide
* Mind Power – Change Your Thought P
rocess To Change Your Life
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/7486/)
* [REDEEM OFFER ](https://idownload
coupon.com/udemy/10708/)Master Time Management for Higher Personal Productivity
* [REDEEM OFFER ](https://idownloadcoupo
n.com/udemy/7639/)Financial Accounting – Inventory Costs
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/13319/)Snow
flake Snowpark API for Python: Master Class with Project
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/13320/)\[DE
A-C01 | ARA-C01\] Snowflake Advanced Certification Prep
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/13318/)Ultim
ate Guide to Creating Presentations with PowerPoint
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/13316/)Trading e
n Gbp/Nzd – estrategia intradiaria efectiva
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/13317/)Essential Skills 
of Microsoft PowerPoint and Google Slide
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/13314/)Global Economics Pla
ybook: International Business Strategies
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/13315/)Artificial Intellige
nce Auditing, AI Tools
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/13313/)Boost Focus: Ayurvedic Concentration I
mprovement Certificate
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/13312/)Closing with confidence: techniques to
 develop your business
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/13311/)Real Estate License Exam Math
* [REDEE
M OFFER ](https://idownloadcoupon.com/udemy/13309/)Advanced Certification in Ayurveda: Master Core Principles
* [REDEEM 
OFFER ](https://idownloadcoupon.com/udemy/13306/)BMS – Building Management System Crash Course ( 2 in 1 )
* [REDEEM OFFE
R ](https://idownloadcoupon.com/udemy/13305/)IELTS Writing MASTERCLASS ( Unlock the Secrets to Band 8 )
* C, C and PHP: 
Comprehensive Programming Bootcamp
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/13307/)
* [REDEEM OFFER ](https://
idownloadcoupon.com/udemy/13308/)Advanced Ayurvedic Nutrition Certification Program – Level 1
* [REDEEM OFFER ](https://
idownloadcoupon.com/udemy/13304/)HVAC Engineering MASTER CLASS: HVAC AIR DISTRIBUTION DESIGN
* [REDEEM OFFER ](https://i
downloadcoupon.com/udemy/10276/)The Meditation Blueprint: Building Your Inner Sanctuary
* [REDEEM OFFER ](https://idownl
oadcoupon.com/udemy/12733/)Ayurvedic Daily Routine: Dinacharya Certification Course
* [REDEEM OFFER ](https://idownloadc
oupon.com/udemy/6650/)Adobe Premiere Pro CC Video Editing Course For Beginners
* [REDEEM OFFER ](https://idownloadcoupon
.com/udemy/11278/)The Beginner’s Guide to Adobe Premiere Pro: Edit Like a Pro
* [REDEEM OFFER ](https://idownloadcoupon.
com/udemy/8828/)Learn Chess in Hindi : Zero to Master Level
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/13262/)C
omplete IT Bootcamp 2025 (Part 2)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/8639/)Learn DaVinci Resolve: The C
omplete Video Editing Bootcamp
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/9923/)Natural Language Processing Cha
llenges : Exam Practice Tests
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/8726/)Learn Figma: UI/UX Design Master
class From Beginner to Pro
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/8659/)YouTube Thumbnail Design (Stunning 
Thumbnails Masterclass)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/6332/)Universidad Excel – Básico, Intermedio
 y Avanzado!
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/12355/)Find Your Ayurvedic Body Type: Diet
* [REDEEM OF
FER ](https://idownloadcoupon.com/udemy/8324/)Learn AutoCAD 2D
* Storytelling Masterclass – Business Storytelling for Le
aders
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/13084/)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/112
16/)Executive Certificate in Business Leadership
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/3596/)La fuerza int
erior para continuar: resiliencia
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/13301/)The Complete Mailchimp Emai
l Marketing Course for 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/13300/)Amazon Marketing PPC 2024 – The C
omplete Amazon Ads Course
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/13299/)Amazon FBA Course – How to Sell on 
Amazon MASTERY 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/13302/)Facebook Ads & Facebook Marketing MASTERY
 2024 | Coursenvy
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/13297/)Building a Strong Opening Repertoire
* [RED
EEM OFFER ](https://idownloadcoupon.com/udemy/13296/)Python. Estructuras de datos y algoritmos en Python
* [REDEEM OFFER
 ](https://idownloadcoupon.com/udemy/13298/)Social Media Marketing MASTERY 2024 | Ads on 10 Platforms
* [REDEEM OFFER ](
https://idownloadcoupon.com/udemy/13294/)Project Management Professional – PMP “PMBOK 6th edition”
* [REDEEM OFFER ](htt
ps://idownloadcoupon.com/udemy/13295/)Master 100 New AI Tools: The Ultimate Productivity Course
* [REDEEM OFFER ](https:
//idownloadcoupon.com/udemy/13292/)Azure Solutions Architect Certification: The Ultimate Bundle
* [REDEEM OFFER ](https:
//idownloadcoupon.com/udemy/13291/)Morning Meditation | Best Guided Meditation Under 10 Minutes
* [REDEEM OFFER ](https:
//idownloadcoupon.com/udemy/13293/)Django Masterclass : Build 9 Real World Django Projects
* [REDEEM OFFER ](https://ido
wnloadcoupon.com/udemy/12239/)Complete Generative AI Course With Langchain and Huggingface

GET MORE FREE ONLINE COURSES
 WITH CERTIFICATE – [CLICK HERE](https://www.reddit.com/r/udemyfreeebies/)
```
---

     
 
all -  [ Query  ](https://www.reddit.com/r/LangChain/comments/1ewqbct/query/) , 2024-08-21-0911
```
I am working on creating embedings based on files user upload. I want to know what will be good way if I saved the files
 uploaded by user or after saving vector db should delete it? 
```
---

     
 
all -  [ RAG vs Fine-tuning? ](https://www.reddit.com/r/LangChain/comments/1ewppvh/rag_vs_finetuning/) , 2024-08-21-0911
```
My context is an excel sheet with 30k x 8 cells. I want the model to read a user entry and return a matched row from the
 context (it won't be a perfect match, I want the LLM to understand the user input and use its expertise to link the inp
ut to the most suitable match from the database). I'm more inclined towards RAG, but wanted to get some opinions. I've n
ever implemented RAG before - can I use the spreadsheet for embeddings? Or convert to JSON?
Any best practices when deal
ing with spreadsheets as context - including chunk size, overlap length, etc?🙏
```
---

     
 
all -  [ Roast my resume | Hardly getting any callbacks ~ suggestions are appreciated!! ](https://i.redd.it/isz6454rcrjd1.jpeg) , 2024-08-21-0911
```
Heyy Devs, I relocated back to India post my masters from US and I am actively looking for SDE 2 roles in India.
I haven
’t been able to get more interviews or offers. Guide me if my resume needs any changes? And what kind of roles should I 
target ? SDE 2 or .. ?

Tech stack id like to work - Python / Backend dev

PS : there is a gap visible on my resume betw
een my Bachelors and work exp, thats coz of Civil services aspirations.

Thank you !!
```
---

     
 
all -  [ Improve GraphRAG using LangGraph ](https://www.reddit.com/r/LangChain/comments/1ewmkey/improve_graphrag_using_langgraph/) , 2024-08-21-0911
```
GraphRAG is an advanced version of RAG retrieval system which uses Knowledge Graphs for retrieval. LangGraph is an exten
sion of LangChain supporting multi-agent orchestration alongside cyclic behaviour in GenAI apps. Check this tutorial on 
how to improve GraphRAG using LangGraph: https://youtu.be/DaSjS98WCWk
```
---

     
 
all -  [ Seeking Advice/Ideas on Matching Document Sections ](https://www.reddit.com/r/LangChain/comments/1ewm8vd/seeking_adviceideas_on_matching_document_sections/) , 2024-08-21-0911
```
Hi all, I've been struggling with a problem and am looking for ideas on how to tackle it. The problem that I want to sol
ve is to verify that a given process (Document A) complies with given guidelines and regulations, provided in another do
cument (Document B).

Both documents can be quite large, so the text won’t fit into the context window of a single promp
t. My idea was to split both documents into chunks and compare these chunks with an LLM. I did the chunking process usin
g the StatisticalChunker from the semantic-chunkers package.

For example, document B has a section that covers laws abo
ut software documentation. Document A describes a software development process where one section outlines the procedure 
of how the documentation is done.

How can I best match these sections? Embedding both chunks and retrieving the top n s
imilar results won't always retrieve the correct corresponding chunks.

Is there a smart way of pre-processing the chunk
s? Maybe by utilizing one of Langchain's retrievers, such as the Parent Document Retriever?

Any thoughts or suggestions
 are welcome. Thanks!
```
---

     
 
all -  [ The advantages Denser Retriever offers to vector store ](https://www.reddit.com/r/DenserRetriever/comments/1ewit1i/the_advantages_denser_retriever_offers_to_vector/) , 2024-08-21-0911
```
A deep dive into the advantages Denser Retriever offers to vector store. The table below compares the NDCG@10 scores of 
Denser Retriever against four other vector store models across 15 MTEB retrieval datasets. For a more detailed analysis,
 check out the full blog at [https://denser.ai/blog/langchain-denser-retriever/](https://denser.ai/blog/langchain-denser
-retriever/)

https://preview.redd.it/uafvoqhpypjd1.png?width=398&format=png&auto=webp&s=68cf5be6069437616b4ba2333877d80
19b41d010

  

```
---

     
 
all -  [ User authorization and feedback before executing a Tool in Langgraph ](https://www.reddit.com/r/LangChain/comments/1ewflik/user_authorization_and_feedback_before_executing/) , 2024-08-21-0911
```
Hi, I have a chatbot that consists of a basic graph where I have a node that calls that LLM and another node that execut
es the tools.  
But I need the user to authorize the execution of the tool first. For this, I need to show the user the 
tool that is about to execute and its arguments, the user can then read what the agent is about to do and could change t
he tool or one of the args by giving feedback. However, all of the information that is shown so that the user can accept
 it needs to be in a user-friendly way. Does anyone know how to do this?
```
---

     
 
all -  [ List of FREE and Best Selling Discounted Courses ](https://www.reddit.com/r/udemyfreebies/comments/1ewfiwt/list_of_free_and_best_selling_discounted_courses/) , 2024-08-21-0911
```
# Udemy Free Courses for 20 August 2024

Note : Coupons might expire anytime, so enroll as soon as possible to get the c
ourses for FREE.

* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/13301/)The Complete Mailchimp Email Marketing Cour
se for 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/13300/)Amazon Marketing PPC 2024 – The Complete Amazon A
ds Course
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/13299/)Amazon FBA Course – How to Sell on Amazon MASTERY 2
024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/13302/)Facebook Ads & Facebook Marketing MASTERY 2024 | Coursenv
y
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/13297/)Building a Strong Opening Repertoire
* [REDEEM OFFER ](http
s://idownloadcoupon.com/udemy/13296/)Python. Estructuras de datos y algoritmos en Python
* [REDEEM OFFER ](https://idown
loadcoupon.com/udemy/13298/)Social Media Marketing MASTERY 2024 | Ads on 10 Platforms
* [REDEEM OFFER ](https://idownloa
dcoupon.com/udemy/13294/)Project Management Professional – PMP “PMBOK 6th edition”
* [REDEEM OFFER ](https://idownloadco
upon.com/udemy/13295/)Master 100 New AI Tools: The Ultimate Productivity Course
* [REDEEM OFFER ](https://idownloadcoupo
n.com/udemy/13292/)Azure Solutions Architect Certification: The Ultimate Bundle
* [REDEEM OFFER ](https://idownloadcoupo
n.com/udemy/13291/)Morning Meditation | Best Guided Meditation Under 10 Minutes
* [REDEEM OFFER ](https://idownloadcoupo
n.com/udemy/13293/)Django Masterclass : Build 9 Real World Django Projects
* [REDEEM OFFER ](https://idownloadcoupon.com
/udemy/12239/)Complete Generative AI Course With Langchain and Huggingface
* [REDEEM OFFER ](https://idownloadcoupon.com
/udemy/13290/)Curso PSeInt algoritmos y lógica de programación
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/13288
/)70-236: Microsoft Exchange Server 2007 Practice Test 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/13289/)6
00 Servlet Interview Questions Practice Test
* 70-347: Enabling Office 365 Services Practice Test 2024
* [REDEEM OFFER](
https://idownloadcoupon.com/udemy/13287/)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/9851/)Excel Certification 
Exam Preparation: 4 Practice Tests 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/8966/)Business Analyst Certi
ficate
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/12622/)Construction Drawing Reading
* [REDEEM OFFER ](https:/
/idownloadcoupon.com/udemy/10089/)Professional Certificate of Executive Business Assistant
* [REDEEM OFFER ](https://ido
wnloadcoupon.com/udemy/7487/)Professional Certificate: Digital Business & Unit Economics
* [REDEEM OFFER ](https://idown
loadcoupon.com/udemy/1382/)Media Training for Authors: Promote Your Book in the News
* [REDEEM OFFER ](https://idownload
coupon.com/udemy/3704/)The Guide to Freelancing in the Modern Gig Economy
* [REDEEM OFFER ](https://idownloadcoupon.com/
udemy/7394/)Personal Branding: You Deliver a Great Elevator Pitch
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/66
78/)Media Training for Doctors/Healthcare Pros: Master the Media
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/101
22/)Professional Certificate in Procurement and Purchasing
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/1385/)Med
ia Training for Financial Service Professionals
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/6721/)Adobe Photosho
p CC For Absolute Beginner to Advanced
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/12267/)Scrum Master Certifica
tion 2024 Agile Scrum Certification
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/13283/)Programming PLC Using Tex
t Commands – Mnemonic Language
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/10091/)Executive Diploma in Human Res
ources Strategy
* Professional PCB Fabrication For Everyone
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/13284/)
*
 [REDEEM OFFER ](https://idownloadcoupon.com/udemy/10798/)YouTube Startrack For Beginners: Launch Your Channel Today
* [
REDEEM OFFER ](https://idownloadcoupon.com/udemy/8274/)Google Analytics 4 (GA4) Certification. How to Pass the Exam
* [R
EDEEM OFFER ](https://idownloadcoupon.com/udemy/9824/)Amazon FBA Guide: From Zero to Seller
* [REDEEM OFFER ](https://id
ownloadcoupon.com/udemy/9689/)Upgrade Your Social Media Presence with ChatGPT
* [REDEEM OFFER ](https://idownloadcoupon.
com/udemy/6606/)Ultimate Adobe Photoshop CC Masterclass Basics To Advanced
* [REDEEM OFFER ](https://idownloadcoupon.com
/udemy/8270/)Instagram Marketing. How to Promote Your Business!
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/1323
8/)The Complete React Course: Become a Pro in No Time
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/8273/)SEO Stra
tegy 2024. SEO training to Unleash Career Potential!
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/7356/)Project M
anagement Fundamentals: A Beginner’s Guide
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/7357/)Facebook Marketing 
2024. Promote Your Business on Facebook!
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/13282/)Veeam Certified Engi
neer (VMCE) Practice Exam – 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/13281/)Learn Carnatic Flute | Swati
 Tirunal Krithis – Vol 1
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/13280/)إحتراف التدوين بإستخدام بلوجر
* [RED
EEM OFFER ](https://idownloadcoupon.com/udemy/9548/)Fundamentos de los Frameworks Web en Go
* [REDEEM OFFER ](https://id
ownloadcoupon.com/udemy/11983/)Research Methodologies in Strategy and Product Development
* Docker and Kubernetes Master
class for Beginners in 2024
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/4637/)
* [REDEEM OFFER ](https://idownloa
dcoupon.com/udemy/4199/)Ethical Hacking: AI Chatbots
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/3083/)Ultimate 
Guide to Product Design: Design Thinking Approach
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/10051/)Learn Filmo
ra Video Editing Masterclass From Beginner to Pro
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/6651/)Python Guide
d Project: Building Tic-Tac-Toe from Scratch
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/13279/)PMI-ACP Exam Pre
p – Practice Tests
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/13277/)How Websites Work
* [REDEEM OFFER ](https:
//idownloadcoupon.com/udemy/13278/)Professional Diploma in Administration Management
* [REDEEM OFFER ](https://idownload
coupon.com/udemy/13275/)Learn Carnatic Flute | Intermediate Level | Varnams Vol – 16
* [REDEEM OFFER ](https://idownload
coupon.com/udemy/13276/)Create a GUI with Python
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/11301/)Excel for Ev
eryone: Essential Skills for Work and Life
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/4087/)WhatsApp Chat Senti
ment Analysis Using Machine Learning
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/11150/)Gatsby JS | Build a pers
onal blog using gatsbyJS
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/8185/)Social Media Bots with Python
* [REDE
EM OFFER ](https://idownloadcoupon.com/udemy/11295/)Complete Portfolio Website Using HTML CSS NETLIFY Project
* [REDEEM 
OFFER ](https://idownloadcoupon.com/udemy/9746/)Ethical Hacking: Hacker Methodology
* Excel files with Python
* [REDEEM 
OFFER](https://idownloadcoupon.com/udemy/12488/)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/10392/)Universidad 
Desarrollo Web – FrontEnd Web Developer!
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/10390/)Java en 13 Días con 
Aplicaciones del Mundo Real
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/10399/)Universidad JavaScript – De Cero 
a Experto JavaScript!
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/10395/)Universidad de Lógica de Programación –
 Aprende 7 Lenguajes!
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/11682/)Python con la IA ChatGPT – Aprende Pyth
on de Cero a Experto
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/12957/)Universidad Python – Cero a Experto – Ac
tualizado ( 84 hrs)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/11683/)Universidad Java Cero a Experto Actualiza
do 2024 ( 150 hrs)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/10391/)Universidad Angular – De Cero a Experto en
 Angular!
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/6292/)Yoga For a Healthy Back
* [REDEEM OFFER ](https://id
ownloadcoupon.com/udemy/10397/)Club Java Master – Novato a Experto Java +110hrs Actualizado
* [REDEEM OFFER ](https://id
ownloadcoupon.com/udemy/10400/)Universidad de Programación – Python, Java, C y C++ – 2024
* [REDEEM OFFER ](https://idow
nloadcoupon.com/udemy/13273/)Zbrush Sculpting: Learn Sculpting the Human Head in Zbrush
* [REDEEM OFFER ](https://idownl
oadcoupon.com/udemy/13272/)Product Owner Certification
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/13271/)CapCut
 Video Editing Bootcamp: CapCut Basic to Advanced
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/12495/)Oracle Java
 Certification Exam OCA 1Z0-808 Preparation Part3
* Javascript For Beginners Complete Course
* [REDEEM OFFER](https://id
ownloadcoupon.com/udemy/12731/)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/9463/)Master Scrum Basics
* [REDEEM 
OFFER ](https://idownloadcoupon.com/udemy/11141/)Advanced Scrum Master Certification
* [REDEEM OFFER ](https://idownload
coupon.com/udemy/13132/)ChatGPT for Product Management

GET MORE FREE ONLINE COURSES WITH CERTIFICATE – [CLICK HERE](htt
ps://idownloadcoupon.com/)
```
---

     
 
all -  [ [2 YoE, Unemployed, Data Scientist/Data Analyst, United States ] ](https://www.reddit.com/r/resumes/comments/1ewb9uj/2_yoe_unemployed_data_scientistdata_analyst/) , 2024-08-21-0911
```
Hello everyone,

I am a recent graduate joining in the pool of full time job seekers.

Background: I am 26 years old, in
ternational student, looking to break into the data field in US. While my masters is Mechanical Engineering on paper, I 
took up courses and projects in the ML and AI domain. My thesis is in Computer Vision, nothing ground-breaking, but a go
od project using Segmentation.

My 'Data Scientist' experience is a part time program in my university which collaborate
s with a large pharma industry, where I worked and gained a lot of knowledge/experience in the Data Science area.

I nee
d an opinion on my resume and the blunders it contains (if any), and the things that I can improve. I also hope I have s
howcased my skills and expeience in the best manner possible, despite coming from a mechanical background. If not, pleas
e let me know your thoughts.

Thanks for your time.

https://preview.redd.it/xehu713vdojd1.jpg?width=1930&format=pjpg&au
to=webp&s=69131fcb22c88839654c4fb15842902231a20583


```
---

     
 
all -  [ Building GPT Document Bot ](https://www.reddit.com/r/learnpython/comments/1ewb6vh/building_gpt_document_bot/) , 2024-08-21-0911
```
For my job, I write hundreds of proposals for government contracts. I want to use an OpenAI API to build a tool that loo
ks over a database of previous proposals (csv, txt, etc.), takes in a single proposal request, and outputs a response fo
r that request. Most of these proposals are around 100 pages and I would like to to output a proposal that is \~70 pages
. For context, I have some basic python experience, but I am unsure of exactly how to go about this. Some forums that I 
read suggested that I use langchain to comb through super long text files. My long term goal is to build a simple GUI an
d dashboard to make it accessible to others in my company and online. How should I go about this? Also, which LLM model 
should I use? Thanks!
```
---

     
 
all -  [ Working On a Langchain based AI chat agent ](https://www.reddit.com/r/LangChain/comments/1ewam8d/working_on_a_langchain_based_ai_chat_agent/) , 2024-08-21-0911
```
I am new software engineering. I am building the entire system from scratch. I was wondering how to manage the security 
of the app. Things like login and stuff (authentication). Would appreciate any open souce technologies/resources. Thanks
 in Advance
```
---

     
 
all -  [ Agents for problem with a deterministic, verifiable, but non-exhaustive answers ](https://www.reddit.com/r/LangChain/comments/1ew9jzd/agents_for_problem_with_a_deterministic/) , 2024-08-21-0911
```
I'm curious if any how has looked at applying agents to problems with deterministic but non-exhaustive answers? My use c
ase is around planning/estimation for repair processes(boats, cars, planes, etc). Similar to the idea [making a sandwich
 from scratch](https://www.theverge.com/2015/9/17/9344597/man-spent-six-months-1500-making-sandwich-from-scratch), there
 might be always another layer of granularity you could expand to. Has anyone worked on a similar use case where a core 
task of an agent is reasoning/judging if an answer is 'good enough/complete enough'? 
```
---

     
 
all -  [ Using GraphRAG and Reinforcement Learning ](https://www.reddit.com/r/LangChain/comments/1ew99s7/using_graphrag_and_reinforcement_learning/) , 2024-08-21-0911
```
Hi, these are two questions bundled into one.  
I'm supposed to create an LLM that gives users suggestions on the projec
t they are working.  
I'm also supposed to add a feedback loop that can improve the model response over time.  
  
So I 
can't just change the LLM model iteratively because I will be using an LLM through api.  
I figured that I could change 
the data I passed to the llm as context through RAG.  
That's when GPT suggested using neo4j's GraphRAG as we can change
 the weights of the data connections and also trace the part of the data we find faulty easily.  
  
This is what it sai
d  
  
After the AI provides a suggestion, monitor its effectiveness. If users frequently make certain changes or follow
 specific advice, reinforce those connections in your system, making them more prominent in future predictions. This cou
ld involve revisiting and adjusting the strength of connections within your knowledge graph. Use RL algorithms like Q-le
arning or policy gradients to adjust the weights

  
I'm new to Graph databases and RL and I'm wondering how to proceed.
 If so can you please provide suggestions/resources on how to implement the two or any better alternative to this method
?
```
---

     
 
all -  [ Interactive Iowa Liquor Sales Dashboard with AI-Powered Chatbot ](https://www.reddit.com/r/u_ricmwas2019/comments/1ew7vxr/interactive_iowa_liquor_sales_dashboard_with/) , 2024-08-21-0911
```
  
I'm excited to share my latest project: an interactive dashboard analyzing Iowa Liquor Retail Sales, enhanced with an
 AI-powered chatbot for natural language queries.  
Project Overview  
  
Dashboard: Visualizes sales data by product, y
ear, and region using Plotly Dash  
Chatbot: Utilizes Claude API to answer questions by querying BigQuery data  
Data So
urce: Iowa Liquor Retail Sales  
Live Demo: [http://104.197.202.155:8080/](http://104.197.202.155:8080/)  
GitHub Reposi
tory: [https://github.com/RicmwasData/plotly-dash-llm/tree/master](https://github.com/RicmwasData/plotly-dash-llm/tree/m
aster)  
  
Key Features  
  
Interactive visualizations of sales trends  
AI-powered chatbot for natural language data 
queries  
Integration with BigQuery for efficient data retrieval  
Hosted on Google Cloud Platform (GCP) for scalability
  
  
Technologies Used  
  
Python  
Plotly Dash  
BigQuery  
Langchain  
Large Language Models (LLM)  
Google Cloud Pl
atform (GCP)  
Git & GitHub
```
---

     
 
all -  [ [1 YoE, Unemployed (full time student), Software Engineer, USA] ](https://i.redd.it/utvrmkxfcnjd1.jpeg) , 2024-08-21-0911
```
Targeting SWE positions from really any industry, of course my dream is land a job in big tech but not really likely con
sidering the market which is fine. Based in NY but applying to pretty much everywhere in the US. 

I graduate with my MS
 in CS in May 2025. Last year, I was searching for internships and barely received any interviews. I’ve since modified m
y resume (I did get an internship but it was through a referral) so looking for some feedback before I begin applying fo
r full time jobs for next year.

BTW, I am a US citizen.
```
---

     
 
all -  [ Sentence Transformers Inference API ](https://www.reddit.com/r/LangChain/comments/1ew5zl1/sentence_transformers_inference_api/) , 2024-08-21-0911
```
Hi,

I want to load my reranking models faster, e.g. with an API.

I am using HuggingfaceEmbeddings with:

    HuggingFa
ceInferenceAPIEmbeddings

I am also using a reranking model which I am loading like this: 

    from sentence_transforme
rs import CrossEncoder
    
    reranking_model = CrossEncoder('BAAI/bge-reranker-v2-m3', max_length=512, device='mps')

    
    query = 'Ich liebe Fußball'
    
    page_contents = [
        'Hallo wer bist du',
        'Fußball is so geil
 ey',
        'Fußball ist der coolste Sport',
        'Hamburg liegt in Deutschland',
        ]
    re_res = reranking_
model.rank(query=query, documents=page_contents, return_documents=True, top_k=2)
    #[{'corpus_id': 1, 'score': 0.89757
94, 'text': 'Fußball is so geil ey'},
     #{'corpus_id': 2, 'score': 0.2194788, 'text': 'Fußball ist der coolste Sport'
}]

This works fine on my Mac, however when loading it in a docker it takes ages to build as the 'mps' device is not ava
ilable. 

  
So is anyone aware of a Sentece Transformers Inference API like the HuggingfaceInferenceAPIEmbeddings? Or c
an I rerank the docs the HuggingfaceInferenceAPIEmbeddings class?
```
---

     
 
all -  [ Offering Free QA Testing for Your LLM/Chatbot! ](https://www.reddit.com/r/LangChain/comments/1ew0ldg/offering_free_qa_testing_for_your_llmchatbot/) , 2024-08-21-0911
```
Hey everyone,

If you’ve been developing a language model (LLM) or chatbot and need someone to help with QA testing, I’m
 here to help! I’ve got experience building chatbots, and I’m offering to test your model **for free.** Whether you’re l
ooking for feedback on performance, functionality, or edge cases, I’m happy to assist.

Just DM me with your requirement
s and what you’d like me to focus on, and we can get started. I can provide detailed reports, suggestions for improvemen
t, or just general user experience feedback—whatever you need.  
  
Cheers!
```
---

     
 
all -  [ Which of the following topics would you like to learn more about: ](https://www.reddit.com/r/LangChain/comments/1evzg1v/which_of_the_following_topics_would_you_like_to/) , 2024-08-21-0911
```


[View Poll](https://www.reddit.com/poll/1evzg1v)
```
---

     
 
all -  [ Deploying Finetuned Llama 3.1 8b - Fast API ](https://www.reddit.com/r/LangChain/comments/1evxztg/deploying_finetuned_llama_31_8b_fast_api/) , 2024-08-21-0911
```
I am using LangGraph and I am struggling to understand after finetuning the model, how and where can I access the model,
 specifically deploying it and using it with API for lowest latency
```
---

     
 
all -  [ Which llm has good Function calling and reasoning ability in the llm with minimum cost ? ](https://www.reddit.com/r/LangChain/comments/1evw7on/which_llm_has_good_function_calling_and_reasoning/) , 2024-08-21-0911
```
I am working on a project where I need a LLM which must have good function calling ability like the order should be corr
ect to get the appropriate result and very good reasoning ability to look into the json response of the tools/functions 
and answer the user queries. The cost should be minimum as well. 

Can anyone suggest any LLMs like this ??
```
---

     
 
all -  [ [2 YoE, Unemployed, Python Backend Gen AI and Machine Learning, Islamabad Pakistan] ](https://www.reddit.com/r/resumes/comments/1evupil/2_yoe_unemployed_python_backend_gen_ai_and/) , 2024-08-21-0911
```
https://preview.redd.it/dci70welekjd1.png?width=1653&format=png&auto=webp&s=1adc39ea854531e2731e76662fe2819554ee14ce


```
---

     
 
all -  [ Need suggestions for an AI project ](https://www.reddit.com/r/LangChain/comments/1evuki4/need_suggestions_for_an_ai_project/) , 2024-08-21-0911
```
Hi everyone, I am working on a Code Assistant project. The goal is to create a code assistant specific to a library, for
 example Keras(Just an example). There are a lot of codes available online which I could use by scraping and using it as
 the training dataset. The problem arises with the different versions. With new versions, some functions deprecate. So o
ur current code assistants trained on old data, couldn't pick this up. I want to make a Code Assistant, which could lear
n from the documentations, function signatures and understand which version of library we're using. Ideally I want the C
ode Assistant to pickup the version of library in the environment, then write code based on it. 

For this, I am current
ly generating synthetic data by making a template functions and prompts and generate variations using a LLM. But this is
 not a good way, as I have to manually implement each function test case and it's prompt template. I am looking for a be
tter way to do this.

P.S. - Let's say if the library is Keras. If I were to make a CA which used Keras to make DL model
s, I would just scrape all the Keras code from the internet to train it. As you know, there is no backward compatibility
 between Keras 2 and 3. Let's say all the Keras code I had on the internet were in Keras 2 and I were to make Code Assis
tant (CA) which is supposed to write my DL models in Keras 3, if Keras 3 is installed in my environment, how would I do 
it?

1. The LLM was already trained on Keras 2. Even if I explicitly mention it to use documentation of Keras 3 using RA
G and prompt engineering, it will still use elements of Keras 2. Because it hasn't seen Keras 3 code.
2. Let's say, I ha
ve Keras 2 code written and I invoke the LLM but the version installed in the env is Keras 3, it should translate the co
de from Keras 2 to Keras 3. How would it do that?
```
---

     
 
all -  [ Are there any good packages for LLM Security? Seeking guidance regarding LLM-Guard ](https://www.reddit.com/r/LangChain/comments/1evtx9o/are_there_any_good_packages_for_llm_security/) , 2024-08-21-0911
```
I am building a chatbot based on langchain with OpenAI as provider for my embeddings and GPT 4O for the LLM, I would lik
e to have a layer of security for my application that is extensible and integrates well with langchain, One such package
 is [LLM-Guard](https://llm-guard.com) from [protect.ai](https://protect.ai). It allows us to individually check the pro
mpt before it touches the langchain logic, which is great and has a lot of features as well. It is all well and good for
 a single request but the processing for subsequent requests is very slow, every time a query is validated the models ar
e loaded into the memory and immediately flushed out as well, this adds a lot of latency when processing multiple reques
ts, is there any way to overcome this issue in LLM Guard. Are there any other packages that would serve a similar functi
onality to add a Security Layer
```
---

     
 
all -  [ What are your RAG parameters e.g. top k, chunk size, chunk overlap? ](https://www.reddit.com/r/LangChain/comments/1evtu7d/what_are_your_rag_parameters_eg_top_k_chunk_size/) , 2024-08-21-0911
```
I know this will vary between use cases and depend on a host of factors, but folks, what are the parameters that y'all u
se in your production RAG app?

I'll go first.

* use case: company's internal knowledge management chatbot
* top k = 5

* chunk size & overlap = 2000 & 200 using Recursive Text Splitter

Obviously, these are just a few of the many parameter
s in a RAG app, so feel free to provide other parameters or information about your use case.
```
---

     
 
all -  [ better data retrieval under RAG mode ](https://www.reddit.com/r/LangChain/comments/1evtt98/better_data_retrieval_under_rag_mode/) , 2024-08-21-0911
```
I am currently trying to build a chatbot that could generate test cases for products. my idea now is to feed it some man
-made test cases and product spec for certain devices and ask the LLM to reference them and generate test cases for some
 other devices. 

I have fed some Json structured test cases (as it is originally table formatted) and the product spec 
(in pure text format). At first, if there's only Json data in the vectorstore, the retrieved data is pretty accurate. Ho
wever, after adding the text data as well, it tends to retrieve more text data than json data, even when I am being quit
e specific (for example, if I ask it to give me some cases under certain class, then it might retrieve text for some rea
son, but if be super specific and tell it to search for json data, then it will look for json data.)

I am using FAISS a
s my vectorstore and I did not use any text splitter for json data (as I want to maintain the format). I am quite new to
 the field so any suggestions on how to improve this will be appreciated!  
  
Thanks! 
```
---

     
 
all -  [ Free Perplexity Clone based on LangGraph Map Reduce ](https://www.reddit.com/r/LangChain/comments/1evp9ca/free_perplexity_clone_based_on_langgraph_map/) , 2024-08-21-0911
```
I attempted to create a perplexity clone using LangGraph Map Reduce and DuckDuckGo search. One of the issues I faced ear
lier was Serper AI and Tavilly Search API only gave a limited number of credits and hence after a point you had to chang
e to a paid version of these APIs. Also the Free Perplexity used the overall search research and page descriptions to pr
ovide results and not going into the details of the page. This project tries to solve these issues.

[https://github.com
/saurabhlalsaxena/Perplexity-Clone-v0.1](https://github.com/saurabhlalsaxena/Perplexity-Clone-v0.1)

Edit: Add a human i
n the loop element on request to ask for clarifying questions where required. I have kept the need for clarifying questi
ons quite stringent. Please feel free to ease them.
```
---

     
 
MachineLearning -  [ [P] using GPT4o with langchain/chroma for sports analysis  ](https://www.reddit.com/r/MachineLearning/comments/1enuzlp/p_using_gpt4o_with_langchainchroma_for_sports/) , 2024-08-21-0911
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
 ](https://www.reddit.com/r/MachineLearning/comments/1eki1fv/r_d_langchain_evaluation_with_beyondllm/) , 2024-08-21-0911
```
Hey everyone! Just came across a new feature of Beyond LLM that can evaluate Langchain RAG pipelines! It provides contex
t relevancy, answer relevancy, and groundedness. Check out the code snippet I’m sharing—perfect for testing your RAG pip
elines! For more info, be sure to check it out on GitHub [here](https://github.com/aiplanethub/beyondllm/blob/main/cookb
ook/evaluate_langchain_rag_pipeline_beyondllm.ipynb).

https://preview.redd.it/172m1y3dvsgd1.png?width=3972&format=png&a
uto=webp&s=63d5b0f41f0e46a58e7a2d5fb0d2bbc4384b3b1d


```
---

     
 
deeplearning -  [ How To Build Your Retrieval Augmented Generation (RAG) Using Open-source Tools: LangChain, LLAMA 3,  ](https://www.reddit.com/r/deeplearning/comments/1emdotx/how_to_build_your_retrieval_augmented_generation/) , 2024-08-21-0911
```


TL;DR: RAG overcomes the limitations of LLMs by bringing in external sources of information as relevant context.  
  

At the end of the step-by-step tutorial, you will be able to give your favorite LLM (ChatGPT, LLAMA 3, Mixtral, Gemini, 
Claude, etc.) some documents, ask it a question and see it respond based on relevant context.  
  
This will be running 
locally, using open-source libraries. Zero API and tooling costs.

[Step-by-step Notebook with zero-cost RAG](https://co
decompass00.substack.com/p/build-open-source-rag-langchain-llm-llama-chroma)

![img](69v6kjfj3wgd1)


```
---

     
 
deeplearning -  [ Need help with creating CLI for 'non-programmers' (LLMs) ](https://www.reddit.com/r/deeplearning/comments/1elrfgm/need_help_with_creating_cli_for_nonprogrammers/) , 2024-08-21-0911
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

     
