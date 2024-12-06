 
all -  [ Best RAG framework for code (or general purpose) ](https://www.reddit.com/r/Rag/comments/1h7h7hm/best_rag_framework_for_code_or_general_purpose/) , 2024-12-06-0914
```
I've been working on building RAGs for codebases. I've been using langchain until now and while it is not terrible, it's
 also not my favorite, due to how misorganized it seems. The RAG works for now, but I'll probably build a lot of stuff o
n top of it, including custom re-rankers and retrievers. Before doing that, I'm  considering refactoring what I have int
o another framework, the more flexible the better.  
What would you guys suggest?

Edit: Forgot to add, but since this i
s a personal project, I was looking into frameworks that are free
```
---

     
 
all -  [ Adding authentication scheme to a langgraph api (self hosted)  ](https://www.reddit.com/r/LangChain/comments/1h7d7k8/adding_authentication_scheme_to_a_langgraph_api/) , 2024-12-06-0914
```
Hi, I was unable to find any documentation on how to add an authentication engine to a self hosted langgraph server inst
ance. Is there some documenation available? I was only able to access this :- [https://github.com/langchain-ai/langgraph
/discussions/2440](https://github.com/langchain-ai/langgraph/discussions/2440)
```
---

     
 
all -  [ Does LangGraph work in the browser??? ](https://www.reddit.com/r/LangChain/comments/1h7cu92/does_langgraph_work_in_the_browser/) , 2024-12-06-0914
```
`[ERROR] No matching export in 'browser-external:node:async_hooks' for import 'AsyncLocalStorage'`

`node_modules/@langc
hain/langgraph/dist/setup/async_local_storage.js:2:9:`

`2 │ import { AsyncLocalStorage } from 'node:async_hooks';`
```
---

     
 
all -  [ Struggling with LangGraph Academy's Lesson on Chains - Need Help! ](https://www.reddit.com/r/LangChain/comments/1h7cszn/struggling_with_langgraph_academys_lesson_on/) , 2024-12-06-0914
```
Hey everyone,

I’ve been following the LangGraph Academy course, and I just started the first module. Up until the chain
s lesson, we’ve been talking about nodes, edges, and graphs, which I was able to grasp pretty well. But now, they’ve sud
denly shifted gears and started talking about **tools, messages, chat models**, and I’m feeling a bit lost.

I kind of u
nderstand the gist of what’s going on, but I have somequestions:

1. **Why are we suddenly discussing messages and chat 
models out of nowhere?** I think I get that the messages are meant to represent some kind of state, right? Like we’re ke
eping track of all the messages in some way. But how is that supposed to scale? If there are thousands of steps, wouldn’
t the state end up bloated with a ton of unnecessary data? Isn’t that inefficient? Or is there some mechanism that prune
s or handles this?
2. **What exactly is a 'tool' in this context?** Is a tool just a component of a node? Or is it somet
hing separate that a node leads to, like its own independent entity? I’m having trouble visualizing how tools fit into t
he graph conceptually.

Sorry if this doesn’t make a ton of sense—I’m pretty confused myself, so I might not be articula
ting this perfectly. 😅 If anyone has gone through this course or has a clearer understanding of these concepts, I’d real
ly appreciate some guidance. Thanks in advance! 🙏
```
---

     
 
all -  [ Drop LangChain and Instructor: Use This Alternative for Structured Output Generation ](https://medium.com/thoughts-on-machine-learning/drop-langchain-and-instructor-use-this-alternative-for-structured-output-generation-30f0b503c6d0) , 2024-12-06-0914
```

```
---

     
 
all -  [ I am building a fitness application  ](https://www.reddit.com/r/LangChain/comments/1h79rkw/i_am_building_a_fitness_application/) , 2024-12-06-0914
```
The app collects user inputs such as weight, height, goals, and more. It then generates a detailed workout and diet plan
. An agent will manage user data and query a CSV file containing various exercises and the muscles they target and how t
o do it and more.

So any tips or improvements  
Thanks in advance 
```
---

     
 
all -  [ QandA With Complex PDF. ](https://www.reddit.com/r/LangChain/comments/1h79pli/qanda_with_complex_pdf/) , 2024-12-06-0914
```
Hi folks - I just want know that whicb PDF parser will be a good choice to extract the data.

PDF can have complex data 
like text inside image inside image, data in tables, graphs,diagrams etc.
```
---

     
 
all -  [ How do I make my PDF RAG app smarter for question answering with tables in it?
 ](https://www.reddit.com/r/Rag/comments/1h77tq4/how_do_i_make_my_pdf_rag_app_smarter_for_question/) , 2024-12-06-0914
```
Hi all,  
I'm developing a PDF RAG app . My app is built using LCEL chain.

I'm currently using pymupdf4llm as the pdf p
arser ( to convert pdfs to their md format ), OpenAIEmbedding text-3-large as the embedding model, Cohere as the reranke
r and OpenAI ( gpt-4o-mini as the LLM ) .

My pdfs are really complex pdfs (containing texts , images , charts , tables.
.. a lot of them ).

The app can currently answer any question based on pdf text easily, but struggles with tables, spec
ially tables that are linked/related ( where answer can only be given by looking and reasoning at multiple tables ).

I 
want to make my PDF RAG app smarter. By smarter, I mean being able to answer questions which a human can find by looking
 and then reasoning after seeing multiple tables in the pdf.

What can I do ?

\[NOTE : I've asked this question on Lang
chain subreddit too but since my app is a RAG app and I need answers that's why posting here too\]
```
---

     
 
all -  [ How do I make my PDF RAG app smarter for question answering with tables in it? ](https://www.reddit.com/r/LangChain/comments/1h77shd/how_do_i_make_my_pdf_rag_app_smarter_for_question/) , 2024-12-06-0914
```
Hi all,  
I'm developing a PDF RAG app . My app is built using LCEL chain.

I'm currently using pymupdf4llm as the pdf p
arser ( to convert pdfs to their md format ), OpenAIEmbedding text-3-large as the embedding model, Cohere as the reranke
r and OpenAI ( gpt-4o-mini as the LLM ) .

My pdfs are really complex pdfs (containing texts , images , charts , tables.
.. a lot of them ).

The app can currently answer any question based on pdf text easily, but struggles with tables, spec
ially tables that are linked/related ( where answer can only be given by looking and reasoning at multiple tables ).

I 
want to make my PDF RAG app smarter. By smarter, I mean being able to answer questions which a human can find by looking
 and then reasoning after seeing multiple tables in the pdf.

What can I do ?
```
---

     
 
all -  [ QandA With complex PDF in by using langchain ](https://www.reddit.com/r/LangChain/comments/1h76mdi/qanda_with_complex_pdf_in_by_using_langchain/) , 2024-12-06-0914
```
HI folks, I am working on a app in which user can upload a PDF and then start QandA with that PDF. PDF has very complex 
data like text inside image inside image, data in tabular / graph / diagrams format.

So which PDF parser will be best f
or this functionality
```
---

     
 
all -  [ Grouping runs with langsmith ](https://www.reddit.com/r/LangChain/comments/1h76bdq/grouping_runs_with_langsmith/) , 2024-12-06-0914
```
I am using langchain and langsmith, and want to group multiple llm calls in a single trace, and maybe add a tag to them.
  
I would want it to be somthing like:  
with group\_in\_single\_trace(tags=\['test'\]):  
   lllm call 1  
   llm call
 2

But cant find anything in the docs that does this. This seems like a very basic need, am i missing somthing?
```
---

     
 
all -  [ [For Hire] AI/ML Engineer & Full Stack Developer – Chatbots & Scalable Web Solutions ](https://www.reddit.com/r/forhire/comments/1h74krg/for_hire_aiml_engineer_full_stack_developer/) , 2024-12-06-0914
```
**Need an AI/Full Stack Developer? Let’s Connect!** 👋

Hi, I’m Sheryar, an experienced AI/ML Engineer and Full Stack Dev
eloper.

💻 **Full Stack Solutions**  
🔹 Sleek UIs: React/Angular  
🔹 Robust APIs: Node.js, NestJS  
🔹 Payment Systems: S
tripe Integration  
🔹 Cloud Hosting: AWS

🤖 **AI & Automation Expertise**  
🔹 Smart Chatbots: Powered by LangChain  
🔹 C
ustom AI Models: NLP, automation, and more

🌟 **Recent Projects**  
🚗 Ride-Sharing: Live tracking + payments  
📦 Logisti
cs: Multi-stop delivery  
🤖 AI Bots: Smart ordering & customer support

💰 **Rate:** $20–$25/hour (negotiable)  
📧 DM to 
discuss your project!   
GitHub: [storm1033](https://github.com/storm1033)

Let’s build something innovative and scalabl
e! 🌐✨
```
---

     
 
all -  [ Langchain pipeline making the application slow. ](https://www.reddit.com/r/LangChain/comments/1h743id/langchain_pipeline_making_the_application_slow/) , 2024-12-06-0914
```
I am using groq as my LLM for my chatbot,
I saw on Langsmith that my RAG pipeline is taking more time then the LLM.

How
 can I improve the speed of my application?
```
---

     
 
all -  [ How would you handle headers and footers of a page in RAG model? ](https://www.reddit.com/r/LangChain/comments/1h73laf/how_would_you_handle_headers_and_footers_of_a/) , 2024-12-06-0914
```
Hi. I made RAG system but sometimes search results are just footers and headers from multiple different pages. I have se
veral clients, so I need a general solution, not for a specific web site. This should be a very typical and classic prob
lem of a search engine. Does anyone know a well-known and easy-to-implement solution? Thanks.
```
---

     
 
all -  [ Methods for File Reranking and Selection ](https://www.reddit.com/r/Rag/comments/1h72or5/methods_for_file_reranking_and_selection/) , 2024-12-06-0914
```
There is BM25 in literature which is a library named as rank-bm25 on github. Langchain uses that bm25 library.
But it is
 not efficient, accuracy level is not satisfactory. So I was looking for different methods like TF-IDF vectorizer. Or ev
en easier, just use the embedding models results to rerank the document base as a last resort for high accuracy scores. 
And it worked pretty well.
There is still one point left, if knowledge base is large and it is not logical to do vector 
search in all of it, this is slow. So I am also looking for something different that can be used before indexing and vec
tor search.
Is there any other method? I want to share our insights.
```
---

     
 
all -  [ Submit Feedback Node (Getting runId from RunnableConfig inside a node) ](https://www.reddit.com/r/LangChain/comments/1h6zxwq/submit_feedback_node_getting_runid_from/) , 2024-12-06-0914
```
I have raised a question on the repo: [discussion](https://github.com/langchain-ai/langgraphjs/discussions/655) and in r
/LangGraph: [post](https://www.reddit.com/r/LangGraph/comments/1giuqw7/submit_feedback_node_getting_runid_from/)

In sum
mary, I want to programmatically, create a feedback on a LangSmith trace either through a tool or node. I figured the ri
ght place for it is a node since you can pass the Runnable Config and theoretically get the \`runId\` from it to be used
 in the \`langsmithClient.createFeedback\` function. I have attempted a few different ways to retrieve the runId and als
o manually setting it in the configurable object, but none seem to work. Has anyone been able to successfully do this wi
thin a graph node? (note my application is in ts. and I am using the langraph.js SDK)

I am not sure if this a bug from 
the LangGraph side or there is different way to be doing this. 
```
---

     
 
all -  [ Ever Changing LangChain APIs ](https://www.reddit.com/r/LangChain/comments/1h6zvr9/ever_changing_langchain_apis/) , 2024-12-06-0914
```
I started to learn LangChain and found some tutorial materials are dated. Apparently, LangChain has gone through revisio
ns of APIs. My question is how I can find out the new APIs when I run into deprecated APIs. For example, I ran into the 
following API call:

    chain = MultiPromptChain.from_prompts(llm, prompt_infos, verbose=True)
    

Then I saw the fol
lowing warning messages:

LangChainDeprecationWarning: Please see the migration guide at: 

[https://python.langchain.co
m/docs/versions/migrating\_memory/](https://python.langchain.com/docs/versions/migrating_memory/)  
  validated\_self = 
self.\_\_pydantic\_validator\_\_.validate\_python(data, self\_instance=self)

How do I find out the right updated API to
 use? Thanks.
```
---

     
 
all -  [ Best way to chunk html ](https://www.reddit.com/r/LangChain/comments/1h6z6bd/best_way_to_chunk_html/) , 2024-12-06-0914
```
I have htmls that I need to chunk in order to pass it to a LLM. It's not going to be used for rag, so I would like chunk
s with around 2-5k tokens each. 

Inside this htmls, I have long tables with thousands of lines. U guys have any suggest
ions on how to chunk this?

I was thinking on creating a chunking strategy with gpt4o, but would appreciate if there are
 ready to go repos or services on this!

Example of html i need to chunk (its a brazilian law text) [https://legislacao.
fazenda.sp.gov.br/Paginas/Portaria-SRE-77-de-2024.aspx](https://legislacao.fazenda.sp.gov.br/Paginas/Portaria-SRE-77-de-
2024.aspx)
```
---

     
 
all -  [ What is the best alternative to LangChain/LangGraph for experimentation and production ](https://www.reddit.com/r/LangChain/comments/1h6tvme/what_is_the_best_alternative_to/) , 2024-12-06-0914
```
There’s lots of dissatisfaction from the community about LangChain. Before I begin building my first MVP, I'd like to ge
t recommendations for alternative frameworks. I'm looking for options that would work well for both MVP development and 
production deployment. If there's a single framework suitable for both stages, that would be ideal, but I'm also open to
 hearing about different frameworks optimized for each phase. What would you recommend?
```
---

     
 
all -  [ List of FREE and Best Selling Discounted Courses ](https://www.reddit.com/r/udemyfreeebies/comments/1h6phyi/list_of_free_and_best_selling_discounted_courses/) , 2024-12-06-0914
```
# Udemy Free Courses for 05 December 2024

Here are the Udemy free courses available for December 5, 2024. Please note t
hat coupons may expire at any time, so enroll quickly to avail of the courses for free:



* [REDEEM OFFER ](https://ido
wnloadcoupon.com/udemy/28014/)Digital Hidden Secrets
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/28013/)Mindful 
Computing
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/28012/)Mastering Business Blueprints 101: The Ultimate Gui
de
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/28011/)Hack-Proof Banking: Defend Against Credit Card Threats!
* 
[REDEEM OFFER ](https://idownloadcoupon.com/udemy/28010/)DevOps MasterClass 2024: Terraform Kubernetes Ansible Docker
* 
[REDEEM OFFER ](https://idownloadcoupon.com/udemy/28009/)JavaScript Interview Masterclass: Top 300 Questions (2024)
* [R
EDEEM OFFER ](https://idownloadcoupon.com/udemy/28008/)Build 5 Spring Boot Projects with Java: Line-by-Line Coding
* [RE
DEEM OFFER ](https://idownloadcoupon.com/udemy/28007/)Spring Boot + Apache Kafka Course – The Practical Guide
* [REDEEM 
OFFER ](https://idownloadcoupon.com/udemy/28006/)Project Risk Aggregation: A Comprehensive Guide
* [REDEEM OFFER ](https
://idownloadcoupon.com/udemy/28005/)Customizable Project Risk Management Templates
* [REDEEM OFFER ](https://idownloadco
upon.com/udemy/28004/)Complete Generative AI Course With Langchain and Huggingface
* [REDEEM OFFER ](https://idownloadco
upon.com/udemy/28003/)Executive Program in Management and Business Administration
* [REDEEM OFFER ](https://idownloadcou
pon.com/udemy/28002/)10 Day MySQL Bootcamp | My SQL Database Design for Beginners
* [REDEEM OFFER ](https://idownloadcou
pon.com/udemy/28001/)Ultimate Ethical Hacking from Zero To Hero
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/2800
0/)Free PMI Project Management Professional (PMP) Tutorial – Mastering the PMP Mindset for Exam Success
* [REDEEM OFFER 
](https://idownloadcoupon.com/udemy/27999/)Free Human Resources Tutorial – Human Resource Management
* Free Power Query 
Tutorial – Power Query For Data Analysis with Microsoft Excel
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/27998/)

* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27997/)Free Meetings Tutorial – Mastering 1:1 Meetings: A Manager’s
 Toolkit for Success
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27996/)Free Tutorial – Stress Relief for Busy L
ives: Relax with NeuroGraphica®
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27995/)Free Tutorial – Levelling in 
Construction for Beginners – Mastering a Laser
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27994/)Free Self-Awar
eness Tutorial – La danza dei sette passi
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27993/)Free Tutorial – 100
 najpopularniejszych niemieckich czasowników
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27992/)Free Tutorial – 
Learning Photoshop Express from Scratch
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27991/)Free Artificial Intel
ligence (AI) Tutorial – Yapay Zeka ile Sermayesiz Şekilde Dolar Kazanın
* [REDEEM OFFER ](https://idownloadcoupon.com/ud
emy/27990/)Free Computer Basics Tutorial – Essential Excel
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27989/)Fr
ee AWS Certified Cloud Practitioner Tutorial – Curso base gratuito – Certificações AWS CLF-C02 e SAA-C03 PT
* [REDEEM OF
FER ](https://idownloadcoupon.com/udemy/27988/)Free Cash Flow Tutorial – Third Document of Financial Statements-Cash Flo
w Statement
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27987/)Free German Language Tutorial – LEARN GERMAN EASI
LY: THE EASY GUIDE TO SELF-LEARNING
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27986/)Free Building Information
 Modeling (BIM) Tutorial – Revit – Dynamo – 5 Rotinas introdutorias
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/
27985/)ChatGPT Prompt Engineering Mastery
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27984/)Adobe Premiere Pro 
CC: Video Editing for Beginners
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27983/)Mastering ChatGPT Prompt Engi
neering: Beginner to Advanced
* The ChatGPT Prompt Engineering Mastery Course
* [REDEEM OFFER](https://idownloadcoupon.c
om/udemy/27982/)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27981/)ChatGPT Masterclass: The Ultimate Beginner’s
 Guide!
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27980/)Videoscribe Whiteboard Animations : MasterClass With 
Project
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27979/)Canva Masterclass For Social Media And Content Creati
on
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27978/)Master Web & Mobile Design: Figma, UI/UX Essentials, +More

* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27977/)Fitness Mastery (Bodybuilding, Muscle Building, Gym Workout)

* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27976/)CSS Complete Course For Beginners
* [REDEEM OFFER ](https://
idownloadcoupon.com/udemy/27975/)Mastering Python, Pandas, Numpy for Absolute Beginners
* [REDEEM OFFER ](https://idownl
oadcoupon.com/udemy/27974/)2024 R Programming Bootcamp for Absolute Beginners
* [REDEEM OFFER ](https://idownloadcoupon.
com/udemy/27973/)Executive Diploma in Business Management
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27972/)Dat
a Center HVAC Design Fundamentals (Dual Certification)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27971/)Parale
gal Professional Certification (PPC)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27970/)From unknown to popular!
 Secrets to explosive brand growth
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27969/)Aire Acondicionado y Refri
geración (HVAC Mantenimiento PRO)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27968/)Python & Django REST API Bo
otcamp – Build A Python Web API
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27967/)French Language Course: Learn
 French/ Speak it like Natives
* A Career in HVAC : Exploring HVAC Career Trajectory
* [REDEEM OFFER](https://idownloadc
oupon.com/udemy/27966/)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27965/)Implementing Agile Marketing and Mark
eting Sprints
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27964/)Grow Your Sales With Conversion Rate Optimizati
on (CRO)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27963/)APICS CPIM Planning and Inventory Management | Exam 
Dumps
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27962/)Master PMI-PBA Exam: Business Analysis Mock Tests
* [RE
DEEM OFFER ](https://idownloadcoupon.com/udemy/27961/)\[NEW\] Prompt Engineering Practice Tests- Interview Questions
* [
REDEEM OFFER ](https://idownloadcoupon.com/udemy/27960/)Luxury Industry Professional Certification (LIPC)
* [REDEEM OFFE
R ](https://idownloadcoupon.com/udemy/27959/)Create a WordPress website with Hostinger!
* [REDEEM OFFER ](https://idownl
oadcoupon.com/udemy/27958/)TikTok Marketing. How to promote your business effectively!
* [REDEEM OFFER ](https://idownlo
adcoupon.com/udemy/27957/)ChatGPT & Midjourney & Gemini: Digital Marketing Assistants
* [REDEEM OFFER ](https://idownloa
dcoupon.com/udemy/27956/)Upwork Beginner Course: Win Freelance World
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy
/27955/)Make a WordPress Website with Elementor
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27954/)ICDL الرخصة ا
لدولية لقيادة الحاسب الآلي
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27953/)ChatGPT Prompts for Trading Stocks
 on Wall Street
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27952/)Firebase Database : CRUD Android App Developm
ent
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27951/)Hack Windows
* Ethical Hacking: Weaponization
* [REDEEM O
FFER](https://idownloadcoupon.com/udemy/27950/)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27949/)Ethical Hacki
ng: Command Injection
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27948/)Learn SQL from Scratch : SQL Tutorial
*
 [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27947/)Branding & Brand Marketing Professional Certification (BMPC)
*
 [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27946/)Acing the Java Interview: Top Java Interview Questions
* [REDE
EM OFFER ](https://idownloadcoupon.com/udemy/27945/)Contact Center Manager Professional Certification
* [REDEEM OFFER ](
https://idownloadcoupon.com/udemy/27944/)Docker for Beginners: a Hands-On Practice Course (+12 hours)
* [REDEEM OFFER ](
https://idownloadcoupon.com/udemy/27943/)Crea un Sistema de Compra y Venta con PHP, JS y MYSQL
* [REDEEM OFFER ](https:/
/idownloadcoupon.com/udemy/27942/)Mastering Mermaid.js: Diagram, Charts and Data Visualization
* [REDEEM OFFER ](https:/
/idownloadcoupon.com/udemy/27941/)Procurement Manager Professional Certification
* [REDEEM OFFER ](https://idownloadcoup
on.com/udemy/27940/)NSE7\_OTS-6.4: Fortinet Network Security Expert Practice 2024
* [REDEEM OFFER ](https://idownloadcou
pon.com/udemy/27939/)Blockchain Professional Certification
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27938/)Ul
timate AWS Solutions Architect Practice Exams 2024 600+ Q
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27937/)CDO
 Chief Digital Officer Executive Certification
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27936/)Trading Skills
 Evaluation – Forex Edition
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27935/)Trading Skills Evaluation – Finan
cial Markets Edition

GET MORE FREE ONLINE COURSES WITH CERTIFICATE – [CLICK HERE](https://idownloadcoupon.com/)
```
---

     
 
all -  [ List of FREE and Best Selling Discounted Courses ](https://www.reddit.com/r/udemyfreebies/comments/1h6phw3/list_of_free_and_best_selling_discounted_courses/) , 2024-12-06-0914
```
# Udemy Free Courses for 05 December 2024

Here are the Udemy free courses available for December 5, 2024. Please note t
hat coupons may expire at any time, so enroll quickly to avail of the courses for free:

* [REDEEM OFFER ](https://idown
loadcoupon.com/udemy/28014/)Digital Hidden Secrets
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/28013/)Mindful Co
mputing
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/28012/)Mastering Business Blueprints 101: The Ultimate Guide

* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/28011/)Hack-Proof Banking: Defend Against Credit Card Threats!
* [R
EDEEM OFFER ](https://idownloadcoupon.com/udemy/28010/)DevOps MasterClass 2024: Terraform Kubernetes Ansible Docker
* [R
EDEEM OFFER ](https://idownloadcoupon.com/udemy/28009/)JavaScript Interview Masterclass: Top 300 Questions (2024)
* [RED
EEM OFFER ](https://idownloadcoupon.com/udemy/28008/)Build 5 Spring Boot Projects with Java: Line-by-Line Coding
* [REDE
EM OFFER ](https://idownloadcoupon.com/udemy/28007/)Spring Boot + Apache Kafka Course – The Practical Guide
* [REDEEM OF
FER ](https://idownloadcoupon.com/udemy/28006/)Project Risk Aggregation: A Comprehensive Guide
* [REDEEM OFFER ](https:/
/idownloadcoupon.com/udemy/28005/)Customizable Project Risk Management Templates
* [REDEEM OFFER ](https://idownloadcoup
on.com/udemy/28004/)Complete Generative AI Course With Langchain and Huggingface
* [REDEEM OFFER ](https://idownloadcoup
on.com/udemy/28003/)Executive Program in Management and Business Administration
* [REDEEM OFFER ](https://idownloadcoupo
n.com/udemy/28002/)10 Day MySQL Bootcamp | My SQL Database Design for Beginners
* [REDEEM OFFER ](https://idownloadcoupo
n.com/udemy/28001/)Ultimate Ethical Hacking from Zero To Hero
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/28000/
)Free PMI Project Management Professional (PMP) Tutorial – Mastering the PMP Mindset for Exam Success
* [REDEEM OFFER ](
https://idownloadcoupon.com/udemy/27999/)Free Human Resources Tutorial – Human Resource Management
* Free Power Query Tu
torial – Power Query For Data Analysis with Microsoft Excel
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/27998/)
*
 [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27997/)Free Meetings Tutorial – Mastering 1:1 Meetings: A Manager’s T
oolkit for Success
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27996/)Free Tutorial – Stress Relief for Busy Liv
es: Relax with NeuroGraphica®
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27995/)Free Tutorial – Levelling in Co
nstruction for Beginners – Mastering a Laser
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27994/)Free Self-Awaren
ess Tutorial – La danza dei sette passi
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27993/)Free Tutorial – 100 n
ajpopularniejszych niemieckich czasowników
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27992/)Free Tutorial – Le
arning Photoshop Express from Scratch
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27991/)Free Artificial Intelli
gence (AI) Tutorial – Yapay Zeka ile Sermayesiz Şekilde Dolar Kazanın
* [REDEEM OFFER ](https://idownloadcoupon.com/udem
y/27990/)Free Computer Basics Tutorial – Essential Excel
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27989/)Free
 AWS Certified Cloud Practitioner Tutorial – Curso base gratuito – Certificações AWS CLF-C02 e SAA-C03 PT
* [REDEEM OFFE
R ](https://idownloadcoupon.com/udemy/27988/)Free Cash Flow Tutorial – Third Document of Financial Statements-Cash Flow 
Statement
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27987/)Free German Language Tutorial – LEARN GERMAN EASILY
: THE EASY GUIDE TO SELF-LEARNING
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27986/)Free Building Information M
odeling (BIM) Tutorial – Revit – Dynamo – 5 Rotinas introdutorias
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27
985/)ChatGPT Prompt Engineering Mastery
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27984/)Adobe Premiere Pro CC
: Video Editing for Beginners
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27983/)Mastering ChatGPT Prompt Engine
ering: Beginner to Advanced
* The ChatGPT Prompt Engineering Mastery Course
* [REDEEM OFFER](https://idownloadcoupon.com
/udemy/27982/)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27981/)ChatGPT Masterclass: The Ultimate Beginner’s G
uide!
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27980/)Videoscribe Whiteboard Animations : MasterClass With Pr
oject
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27979/)Canva Masterclass For Social Media And Content Creation

* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27978/)Master Web & Mobile Design: Figma, UI/UX Essentials, +More
*
 [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27977/)Fitness Mastery (Bodybuilding, Muscle Building, Gym Workout)
*
 [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27976/)CSS Complete Course For Beginners
* [REDEEM OFFER ](https://id
ownloadcoupon.com/udemy/27975/)Mastering Python, Pandas, Numpy for Absolute Beginners
* [REDEEM OFFER ](https://idownloa
dcoupon.com/udemy/27974/)2024 R Programming Bootcamp for Absolute Beginners
* [REDEEM OFFER ](https://idownloadcoupon.co
m/udemy/27973/)Executive Diploma in Business Management
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27972/)Data 
Center HVAC Design Fundamentals (Dual Certification)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27971/)Paralega
l Professional Certification (PPC)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27970/)From unknown to popular! S
ecrets to explosive brand growth
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27969/)Aire Acondicionado y Refrige
ración (HVAC Mantenimiento PRO)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27968/)Python & Django REST API Boot
camp – Build A Python Web API
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27967/)French Language Course: Learn F
rench/ Speak it like Natives
* A Career in HVAC : Exploring HVAC Career Trajectory
* [REDEEM OFFER](https://idownloadcou
pon.com/udemy/27966/)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27965/)Implementing Agile Marketing and Market
ing Sprints
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27964/)Grow Your Sales With Conversion Rate Optimization
 (CRO)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27963/)APICS CPIM Planning and Inventory Management | Exam Du
mps
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27962/)Master PMI-PBA Exam: Business Analysis Mock Tests
* [REDE
EM OFFER ](https://idownloadcoupon.com/udemy/27961/)\[NEW\] Prompt Engineering Practice Tests- Interview Questions
* [RE
DEEM OFFER ](https://idownloadcoupon.com/udemy/27960/)Luxury Industry Professional Certification (LIPC)
* [REDEEM OFFER 
](https://idownloadcoupon.com/udemy/27959/)Create a WordPress website with Hostinger!
* [REDEEM OFFER ](https://idownloa
dcoupon.com/udemy/27958/)TikTok Marketing. How to promote your business effectively!
* [REDEEM OFFER ](https://idownload
coupon.com/udemy/27957/)ChatGPT & Midjourney & Gemini: Digital Marketing Assistants
* [REDEEM OFFER ](https://idownloadc
oupon.com/udemy/27956/)Upwork Beginner Course: Win Freelance World
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/2
7955/)Make a WordPress Website with Elementor
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27954/)ICDL الرخصة الد
ولية لقيادة الحاسب الآلي
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27953/)ChatGPT Prompts for Trading Stocks o
n Wall Street
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27952/)Firebase Database : CRUD Android App Developmen
t
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27951/)Hack Windows
* Ethical Hacking: Weaponization
* [REDEEM OFF
ER](https://idownloadcoupon.com/udemy/27950/)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27949/)Ethical Hacking
: Command Injection
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27948/)Learn SQL from Scratch : SQL Tutorial
* [
REDEEM OFFER ](https://idownloadcoupon.com/udemy/27947/)Branding & Brand Marketing Professional Certification (BMPC)
* [
REDEEM OFFER ](https://idownloadcoupon.com/udemy/27946/)Acing the Java Interview: Top Java Interview Questions
* [REDEEM
 OFFER ](https://idownloadcoupon.com/udemy/27945/)Contact Center Manager Professional Certification
* [REDEEM OFFER ](ht
tps://idownloadcoupon.com/udemy/27944/)Docker for Beginners: a Hands-On Practice Course (+12 hours)
* [REDEEM OFFER ](ht
tps://idownloadcoupon.com/udemy/27943/)Crea un Sistema de Compra y Venta con PHP, JS y MYSQL
* [REDEEM OFFER ](https://i
downloadcoupon.com/udemy/27942/)Mastering Mermaid.js: Diagram, Charts and Data Visualization
* [REDEEM OFFER ](https://i
downloadcoupon.com/udemy/27941/)Procurement Manager Professional Certification
* [REDEEM OFFER ](https://idownloadcoupon
.com/udemy/27940/)NSE7\_OTS-6.4: Fortinet Network Security Expert Practice 2024
* [REDEEM OFFER ](https://idownloadcoupo
n.com/udemy/27939/)Blockchain Professional Certification
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27938/)Ulti
mate AWS Solutions Architect Practice Exams 2024 600+ Q
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27937/)CDO C
hief Digital Officer Executive Certification
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27936/)Trading Skills E
valuation – Forex Edition
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27935/)Trading Skills Evaluation – Financi
al Markets Edition

GET MORE FREE ONLINE COURSES WITH CERTIFICATE – [CLICK HERE](https://www.reddit.com/r/udemyfreeebies
/)
```
---

     
 
all -  [ We made an agent with LangGraph that got 48.60% on SWE-bench, all open-source ](https://www.reddit.com/r/LangChain/comments/1h6o63g/we_made_an_agent_with_langgraph_that_got_4860_on/) , 2024-12-06-0914
```
We at [Composio](https://composio.dev/) are building the tool infrastructure for AI agents, and one of our users' bigges
t requests was toolkits for building custom coding agents that work. So, we created SWE-Kit, a starter template with all
 the toolkits for building AI coding agents.

To test the efficiency of our tools, we built a comprehensive AI agent com
plete [open-source ](https://github.com/ComposioHQ/composio/tree/master/python/swe/agent)using LangGraph and tested it o
n [SWE-bench](https://www.swebench.com/) verified, and it got 48.60%.

* **Code Analysis Tool:** Intelligently retrieves
 relevant code snippets from the repository.
* **File Tool:** Facilitates navigation and updates to files.
* **Shell Too
l:** Performs shell operations.
* **Git Tool:** Handles version control tasks.

We optimized the tools for improved func
tion calling accuracy.

The code is open-source, and you can even modify it to add external integrations like GitHub, Li
near, Slack, etc., using Composio to build a full-fledged AI software engineer. Check out the [SWE-Kit agent](https://bl
og.langchain.dev/composio-swekit/) blog published on LangChains’ blog for an architectural explanation of the SWE agent.


Write code, review it, write tests, and more.

I am not even kidding. Many companies have raised millions just from th
is.
```
---

     
 
all -  [ [Hiring] Currently working on a RAG + Big Data platform/marketplace and looking for developers ](https://www.reddit.com/r/LangChain/comments/1h6n2c6/hiring_currently_working_on_a_rag_big_data/) , 2024-12-06-0914
```
I'm currently building a RAG + Big data platform/marketplace. It will be modular drag and drop pipelines. Think what hom
e depot is for home builders, but we are for Analysts, Researchers, etc. The startup's name is Analytics Depot and when 
it comes to branding and marketing, we have a massive advantage. If you have built something along these lines, DM me. I
'd love to discuss how we can work together.
```
---

     
 
all -  [ HI all, 

I am building a RAG application that involves private data. I have been asked to use a loc ](https://www.reddit.com/r/LangChain/comments/1h6mk8y/hi_all_i_am_building_a_rag_application_that/) , 2024-12-06-0914
```
P.s I am currently experimenting with ollama
```
---

     
 
all -  [ Suggestions for Automating Data Processing with LLMs and Vector Databases ](https://www.reddit.com/r/LangChain/comments/1h6k9dn/suggestions_for_automating_data_processing_with/) , 2024-12-06-0914
```
# This is my first time posting, so please forgive me if I make any mistakes.

I’m working on a project to automate repe
titive data processing tasks like cleaning, and formatting using large language models (LLMs) and Python tools. My idea 
is to:

1. Use frameworks like LangChain or CrewAI to manage interactions between user prompts and the LLM.
2. Store pre
defined knowledge (e.g., conventions and rules) in a vector database like Pinecone or ChromaDB for the LLM to reference 
during processing.

Does this architecture make sense for automating workflows? Also, how should I evaluate the system’s
 performance, such as accuracy in interpreting prompts or reliability compared to manual methods?

I’d appreciate any su
ggestions, resources, or guidance on tools and evaluation methods for implementing this system.
```
---

     
 
all -  [ Why are there so many redundant API's in LangChain? Need help ](https://www.reddit.com/r/LangChain/comments/1h6h9qp/why_are_there_so_many_redundant_apis_in_langchain/) , 2024-12-06-0914
```
I'm trying to navigate the docs and understand how to make an agent with tools AND prompt. The following code shows two 
ways to do this, neither really works. What is the proper way to do this, and populate the fields of the prompt? I can't
 get it to work.

PS. I use JS LangChain

    const agent = createReactAgent({
      llm,
      tools,
      prompt   //
 PROMPT can be any prompt include one with {input} {field1} {field2}
    });
    agent.invoke({
      messages: [
      
  {
          role: 'user',
          content: `This is the input question?`,   // Can't specify {input} fields?!?!
    
    },
      ],
    })
    
    // Why I have to provide tools and prompts here again when agent already have it?!?!?
  
  const executor = AgentExecutor.
    fromAgentAndTools
    ({
      agent: agent,
      tools: tools,
      prompt: pro
mpt
    });
    
    // Does input populate {input} field of prompt? NO IT DOES NOT
    const result = await executor.in
voke({
      input: `This is the input question?`,
    });

  

```
---

     
 
all -  [ doc2exam - Full Self-Driving for exam prep and certs ](https://www.reddit.com/r/Python/comments/1h6f71a/doc2exam_full_selfdriving_for_exam_prep_and_certs/) , 2024-12-06-0914
```
hello everyone! here's doc2exam

a place to turn any material into live exams -- for students prepping or professors set
ting official certifications

working on doc2exam proved to be really fun, I've learned svelte5, deepened my django skil
ls, and rag/llm skills.

I've found [llamaindex](https://github.com/run-llama/llama_index) is much easier to use than la
ngchain, and the reddit dwarfs and yc hackers are right, at least in my case: langchain is over-engineered for most peop
le

but llamaindex also tries too hard in some places to replace manual prompt engineering, and I had to dodge many of i
ts incomplete (and sometimes inconsistent or unintuitive) apis

\# What My Project Does

it turns any material into a fu
lly-fledged live exam that you can send to your students who can take it online., and receive a perma-url certificate li
ke on Coursera (which you can attach to your linkedin or whatever).  
the idea is to have the examination part of a cour
se completely automated, while the teaching itself is still driven by a human (as per the neoducation manifesto - google
 it).

  
\# Target Audience

Schools, Professors or students prepping for exams

  
\# Comparison

[https://jungleai.co
m/](https://jungleai.com/) \-- more of a flashcard generator, and it focuses on student prepping while doc2exam is prima
rily targeted towards professors (but students can use it just as easily for prep)

[https://www.marquiz.io/](https://ww
w.marquiz.io/) \-- the term 'quiz' is too casual for doc2exam's intended scope: to become a de-facto platform for exam g
eneration but also, equally important, live exam taking

[https://pdfquiz.com/](https://pdfquiz.com/) \-- idem marquiz.i
o
```
---

     
 
all -  [ Trabajo de AI Engineer/Developer ](https://www.reddit.com/r/programacion/comments/1h6e5ki/trabajo_de_ai_engineerdeveloper/) , 2024-12-06-0914
```
Buenas gente, trabajo de fullstack y resulta que me he estado interesando bastante en lo que supone(hago énfasis en esto
 ya que hay mucha confusión con lo que hace y lo que no un ingeniero en IA) este rol. Aplicación de IA en distintos ento
rnos, construcción de agentes, etc.

El único proyecto real que he hecho por ahora es una pila en Python con la API de O
penai en mi trabajo, ahora estoy experimentando con LM Studio, haciendo un cursito de IA de Scrimba y le tengo muchas ga
nas a aprender Langchain y trabajar con modelos OpenSource. 

La pregunta que me hago es cómo aplicar todo esto a mi car
rera profesional, ¿qué puestos hay que requieran de estos conocimientos?, ¿qué se necesita para aplicar a un puesto del 
estilo?. Si hay alguien que se dedique a esto o conozca el mundillo y me pueda guiar un poco lo agradecería infinitament
e :)
```
---

     
 
all -  [ Welchen Berufsweg einschlagen? ](https://www.reddit.com/r/InformatikKarriere/comments/1h6dbqm/welchen_berufsweg_einschlagen/) , 2024-12-06-0914
```
Stehe kurz vorm Abschluss meines Bachelors und würde gerne anfangen zu arbeiten. 
Welche Art von Stellen bieten sich für
 mich interessen- als auch karrieremäßig an?
Hab am meisten Erfahrung in Python (numpy, Pandas, Open-cv, langchain, fast
api, flask, matplotlib) und sql (vor allem postgres).
```
---

     
 
all -  [ Notary Agent - Act, Low Search + Analysis ](https://www.reddit.com/r/LangChain/comments/1h6cufg/notary_agent_act_low_search_analysis/) , 2024-12-06-0914
```
I would like to create application that would support work of Lawyer / Notary.

Functionality is as follows:

\- Person 
types his case for example 'My client wants to sell property X in place X with etc'

\- Application would extract releva
nt law and acts and provide suggestions guidance.

Resources:

I have access to API that provides list of all Acts and L
aws (in JSON format)

Currently Notary is searching himself (some of them he remembers but he is also just browsing)

[h
ttps://api.sejm.gov.pl/eli/acts/DU/2020](https://api.sejm.gov.pl/eli/acts/DU/2020)

When you have specific Act - you can
 download it as PDF

[https://api.sejm.gov.pl/eli/acts/DU/2020/1/text.pdf](https://api.sejm.gov.pl/eli/acts/DU/2020/1/te
xt.pdf)

Challange:

\- As you can imagine list of all acts if very long (for each year around 2000 acts) but only few a
re really relevant for each case

The approach I'm thinking about:

Only thing that comes to my mind is storing the list
 of all acts in vector store, and making first call asking to find acts that might be relevant in this case, then extrac
ting those relevant PDF's and making another call to give summary and guidance.

Thoughts:

I don't want AI to make dete
rministic answer but rather to provide context for Notary to make decision.

But I'm not sure if this approach is possib
le to implement as this combined JSON would have probably like 10 000 objects.

What do you think? Do you have other ide
as? Is it feasible?
```
---

     
 
all -  [ History Aware Retriever ](https://www.reddit.com/r/LangChain/comments/1h68m63/history_aware_retriever/) , 2024-12-06-0914
```
I am trying to build a RAG with history aware retriever for my project but I am finding that the retriever is emphasizin
g on the history more than the current query, this is making the context different from what I want.   
For example:  
Q
uery: How many days of paid leave are male employees entitled to?  
Chatbot: Male employees are enttield to 20 days of p
aid leave.

Query: If I join the company in March, how many days of paid leave will I get?  
Chatbot: According to conte
xt, as a male employee, you are entitled to 20 days of paid leave. As for the paid leaves you will be pro rated accordin
gly.

I am using the llama3.2:latest as my llm model and the embedding model is nomic-ai/nomic-embed-text-v1  

```
---

     
 
all -  [ Dangerously Smart Agent - Feedback Request  ](https://www.reddit.com/r/LangChain/comments/1h681h5/dangerously_smart_agent_feedback_request/) , 2024-12-06-0914
```
Hi everyone,

I’m thrilled to share some work I’ve been doing with LangGraph, and I’d love to get your feedback! A while
 ago, I created a tutorial showcasing a “Dangerously Smart Agent” using LangGraph to orchestrate dynamic AI agents capab
le of generating, reviewing, and executing Python code autonomously. Here’s the original video for context:
📺 Original V
ideo: The Dangerously Smart Agent
https://youtu.be/hthRRfapPR8

Since then, I’ve made significant updates:

1. Enhanced 
Prompt Engineering: Smarter, optimized prompts to boost performance.


2. Improved Preprocessor Agent Architecture: A cl
eaner, more efficient design.


3. Model Optimization: I’ve managed to get smaller models like Llama 3.2: 3B to perform 
comparably to Nemotron 70B—a huge leap in accessibility and efficiency!



Here’s the updated tutorial with all the chan
ges:
📺 Updated Video: Enhanced AI Agent

https://youtu.be/ISfMCi5pLcA

I’d really appreciate your thoughts on the follow
ing:

Workflow improvements: Are there areas where I can refine the agent’s process further?

Scaling with smaller model
s: Does anyone have experience or tips for improving even further with small models?

General feedback: What do you thin
k of the updated architecture?


You can also find the codebase here:
📂 GitHub Repository
https://github.com/Teachings/l
anggraph-learning

Thank you so much for taking the time to check this out. LangChain has such an amazing community, and
 I’d love to hear your insights on how to make this even better!

Looking forward to your feedback!

```
---

     
 
all -  [ Can't pass model output to another model. Am i using chains wrong? ](https://www.reddit.com/r/LangChain/comments/1h668uf/cant_pass_model_output_to_another_model_am_i/) , 2024-12-06-0914
```
i have a chain of models but it fails if i use the second model it fails.

```chain = prompt | project_manager | analyst
``` is failing  

but this works
```chain = prompt | project_manager```

i can't get the analyst working how do i send t
he model output to the next model? 
Its throwing this error.
``` ValueError: Invalid input type <class 'langchain_core.m
essages.ai.AIMessage'>. Must be a PromptValue, str, or list of BaseMessages.```
```
---

     
 
all -  [ [LangGraph] Preventing an Agent from assuming users can see tool calls.
 ](https://www.reddit.com/r/LangChain/comments/1h5ynci/langgraph_preventing_an_agent_from_assuming_users/) , 2024-12-06-0914
```
Hi all,

I've implemented a ReAct-inspired agent connected to a curriculum specific content API. It is backed by Claude 
3.5 Sonnet. There are a few defined tools like `list_courses`, `list_units_in_course`, `list_lessons_in_unit`, etc.

The
 chat works as expected an asking the agent 'what units are in the Algebra 1 course' fires off the expected tool calls. 
However, the actual response provided is often along the lines of:

* text: *'Sure...let me find out'*
* tool\_call: `li
st_courses`
* tool\_call: `list_units_in_course`
* text: *'I've called tools to answer your questions.* ***You can see t
he units in Algebra 1 above***\*'\*

**The Issue**

The assistant is making the assumption that tool calls and their res
ults are rendered to the user in some way. That is not the case.

**What I've Tied:**

* Prompting with strong language 
explaining that the user can definitely not see tool\_calls on their end.
* Different naming conventions of tools, eg `f
etch_course_list` instead of `list_courses`

Neither of these solutions completely solved the issue and both are stochas
tic in nature. They don't guarantee the expected behavior.

**What I want to know:**

Is there an architectural pattern 
that guarantees LLM responses **don't** make this assumption?
```
---

     
 
all -  [ Project Alice v0.3 => OS Agentic Workflows with Web UI ](https://www.reddit.com/r/LangChain/comments/1h5xu23/project_alice_v03_os_agentic_workflows_with_web_ui/) , 2024-12-06-0914
```
Hello!

This is the 3rd update of the Project Alice framework/platform for agentic workflows: [https://github.com/Marian
oMolina/project\_alice/tree/main](https://github.com/MarianoMolina/project_alice/tree/main)

**Project Alice** is an ope
n source platform/framework for agentic workflows, with its own React/TS WebUI. It offers a way for users to create, run
 and perfect their agentic workflows with 0 coding needed, while allowing coding users to extend the framework by creati
ng new API Engines or Tasks, that can then be implemented into the module. The entire project is build with readability 
in mind, using Pydantic and Typescript extensively; its meant to be self-evident in how it works, since eventually the g
oal is for agents to be able to update the code themselves. 

At its bare minimum it offers a clean UI to chat with LLMs
, where you can select any of the dozens of models available in the 8 different LLM APIs supported (including LM Studio 
for local models), set their system prompts, and give them access to any of your tasks as tools. It also offers around 2
0 different pre-made tasks you can use (including research workflow, web scraping, and coding workflow, amongst others).
 The tasks/prompts included are not perfect: The goal is to show you how you can use the framework, but you will need to
 find the right mix of the model you want to use, the task prompt, sys-prompt for your agent and tools to give them, etc
. 

# Whats new?

\- **RAG**: Support for RAG with the new Retrieval Task, which takes a prompt and a Data Cluster, and 
returns chunks with highest similarity. The RetrievalTask can also be used to ensure a Data Cluster is fully embedded by
 only executing the first node of the task. Module comes with both examples. 

[RAG](https://preview.redd.it/7fzgxhg7xh4
e1.png?width=2856&format=png&auto=webp&s=6c311e895c2f24537efb57793a6b3e9d47cde8cb)

\- **HITL**: Human-in-the-loop mecha
nics to tasks -> Add a User Checkpoint to a task or a chat, and force a user interaction 'pause' whenever the chosen nod
e is reached. 

[Human in the loop](https://preview.redd.it/wyz3j7t0xh4e1.png?width=2856&format=png&auto=webp&s=dfdbd1ca
96cd23d0d5a89c450cae714ed78bf4fd)

\- **COT**: A basic Chain-of-thought implementation: \[analysis\] tags are parsed on 
the frontend, and added to the agent's system prompts allowing them think through requests more effectively

[Example of
 Analysis and Documents being used](https://preview.redd.it/bqm9i4nffg4e1.jpg?width=1581&format=pjpg&auto=webp&s=4fb4d64
0687d885c1c17193e29ca3da9dbe76c7e)

\- **DOCUMENTS**: Alice Documents, represented by the \[aliceDocument\] tag, are par
sed on the frontend and added to the agent's system prompts allowing them to structure their responses better

[Document
 view](https://preview.redd.it/gidsz90ifg4e1.jpg?width=1591&format=pjpg&auto=webp&s=dad04e284dd0834e3ea1714ebe4243b700aa
bac9)

**- NODE** **FLOW**: Fully implemented node execution logic to tasks, making workflows simply a case where the no
des are other tasks, and other tasks just have to define their inner nodes (for example, a PromptAgentTask has 3 nodes: 
llm generation, tool calls and code execution). This allows for greater clarity on what each task is doing and why

[Tas
k response's node outputs](https://preview.redd.it/f1hp7p4ofg4e1.jpg?width=1877&format=pjpg&auto=webp&s=ded4170ce9a93a29
e3cab855e06aaa430b3a8516)

\- **FLOW VIEWER**: Updated the task UI to show more details on the task's inner node logic a
nd flow. See the inputs, outputs, exit codes and templates of all the inner nodes in your tasks/workflows. 

[Task flow 
view](https://preview.redd.it/29wurpckfg4e1.jpg?width=1861&format=pjpg&auto=webp&s=6093d1ca8fc96cc2a5791bc3287fa08ea215a
7ef)

\- **PROMPT PARSER**: Added the option to view templated prompts dynamically, to see how they look with certain in
puts, and get a better sense of what your agents will see

[Prompt parser](https://preview.redd.it/csyj3yzrfg4e1.jpg?wid
th=1599&format=pjpg&auto=webp&s=ab4b42d3f8048182d1c8d368e494084cabdacb42)

\- **APIS**: New APIs for Wolfram Alpha, Goog
le's Knowledge Graph, PixArt Image Generation (local), Bark TTS (local). 

\- **DATA CLUSTERS**: Now chats and tasks can
 hold updatable data clusters that hold embeddable references like messages, files, task responses, etc. You can add any
 reference in your environment to a data cluster to give your chats/tasks access to it. The new retrieval tasks leverage
 this.

\- **TEXT MGMT**: Added 2 Text Splitter methods (recursive and semantic), which are used by the embedding and RA
G logic (as well as other APIs with that need to chunk the input, except LLMs), and a Message Pruner class that scores a
nd prunes messages, which is used by the LLM API engines to avoid context size issues

**- REDIS QUEUE**: Implemented a 
queue system for the Workflow module to handle incoming requests. Now the module can handle multiple users running multi
ple tasks in parallel. 

\- **Knowledgebase:** Added a section to the Frontend with details, examples and instructions. 


\- \*\***NOTE**\*\*: If you update to this version, you'll need to reinitialize your database (User settings -> Danger
 Zone). This update required a lot of changes to the framework, and making it backwards compatible is inefficient at thi
s stage. Keep in mind Project Alice is still in Alpha, and changes should be expected

# What's next? Planned developmen
ts for v0.4:

\- Agent using computer

\- Communication APIs -> Gmail, messaging, calendar, slack, whatsapp, etc. (some 
more likely than others) 

\- Recurring tasks -> Tasks that run periodically, accumulating information in their Data Clu
ster. Things like 'check my emails', or 'check my calendar and give me a summary on my phone', etc. 

\- CUDA support fo
r the Workflow container -> Run a wide variety of local models, with a lot more flexibility

\- Testing module -> Build 
a set of tests (inputs + tasks), execute it, update your tasks/prompts/agents/models/etc. and run them again to compare.
 Measure success and identify the best setup. 

\- Context Management w/LLM -> Use an LLM model to (1) summarize long me
ssages to keep them in context or (2) identify repeated information that can be removed

# At this stage, I need help. 


**I need people to:**

\- Test things, find edge cases, find things that are non-intuitive about the platform, etc. Als
o, improving / iterating on the prompts / models / etc. of the tasks included in the module, since that's not a focus fo
r me at the moment. 

\- I am also very interested in getting some help with the frontend: I've done my best, but I thin
k it needs optimizations that someone who's a React expert would crush, but I struggle to optimize. 

And so much more. 
There's so much that I want to add that I can't do it on my own. I need your help if this is to get anywhere. I hope tha
t the stage this project is at is enough to entice some of you to start using, and that way, we can hopefully build an a
ctual solution that is open source, brand agnostic and high quality. 

Cheers!
```
---

     
 
all -  [ Any alternatives to get around the AWS lambda layers size limit? ](https://www.reddit.com/r/aws/comments/1h5xevl/any_alternatives_to_get_around_the_aws_lambda/) , 2024-12-06-0914
```
I’ve got some layers that are over the 250mb size limit for lambda layers. Has anyone got any recommendations for what I
 can do to get around this?

Edit: We're using langchain and pytesseract and some other libraries which are taking up sp
ace for a document extraction function as well as psycopg for some connection to our postgresql database and some others
 too. I've installed them in a virtual environment to check the size and it seems to be under the 250MB limit so I'm a b
it confused why I get the layers exceeding available size limit error when deploying my stack using sam.
```
---

     
 
all -  [ We became the product of the day on Product Hunt and got insane traffic by using these free organic  ](https://www.reddit.com/r/SaaS/comments/1h5ugyq/we_became_the_product_of_the_day_on_product_hunt/) , 2024-12-06-0914
```
Many people say it is not worth putting effort into Product Hunt, but we at [Composio](https://composio.dev/) might have
 had a different experience. We are an AI developer tool start-up, and last month, we launched two products(SWE-Kit and 
AgentAuth), which came first and third, respectively.

This gave us a lot of exposure. We were listed in multiple high-q
uality directories, newsletters, and blogs, and many people started talking about us on social media. We are still getti
ng traffic from all these sites. We gained upward of 1k signed-up users from these two launches. This was big for us. We
 now have a better domain rating and authority, which is worth every penny.

So, how did we do it?

We were on a tight b
udget, so we had to do everything ourselves.

1. **Blogs** As we are a dev tool start-up and our ICP is a software devel
oper; we wrote blogs on DevTo, HackerNoon, etc. This only got us 1.5k visitors. If you are serving developers, consider 
this.
2. **Collabs**: We collaborated with a few reputed brands in the industry, like LangChain (we used their framework
 to build an agent that topped the SWE bench), Replit, LlamaIndex, etc., so it was easy for them to promote us. Always m
ake sure you’re providing value before reaching out. Reach out to the brands you have made your app with; they are usual
ly open to share if there is an 'Aha' factor.
3. **Social Media** It was the centrepiece of our marketing channels.
   *
 **Reddit**: We found relevant subreddits for our niche, like LocalLlama, Self-hosted, Open-source, Programming, etc. an
d wrote about us, ensuring it didn’t violate rules.
   * **X(Twitter)/LinkedIn:** Posted a long-form catchy launch post 
with a video illustration, as these platforms are biased around it. Also, we made the brand's quote repost us. If you do
 not have brand collabs, get influencers from your niche and try to boost it. Instead of a different post, ask them to q
uote it. This worked better for us.
4. **Slack Channels** This might be icky, but it works. We collected a lot of Slack 
channels. Set up automation and send messages to members. This is still a danger zone, as you risk getting called out. G
ood, meaning people will be fine with it. You can do it at your own risk.
5. Once you rank on top, milk it to the best o
f your ability, writing blogs and tweets and sharing as much as possible.

We did this for all our launches, and we got 
a really good number of impressions (200k+) and users.

At the end of the day, it’s you and your product. Make sure it i
s interesting and provides value to the intended users.

Feel free to ask any questions or share anything you have done 
that helped you. Let’s help each other.
```
---

     
 
all -  [ We became the product of the day on Product Hunt and got insane traffic by using these free organic  ](https://www.reddit.com/r/Entrepreneur/comments/1h5q18q/we_became_the_product_of_the_day_on_product_hunt/) , 2024-12-06-0914
```
Many people say it is not worth putting effort into Product Hunt, but we at Composio might have had a different experien
ce. We are an AI developer tool start-up, and last month, we launched two products(SWE-Kit and AgentAuth), which came fi
rst and third, respectively.

This gave us a lot of exposure. We were listed in multiple high-quality directories, newsl
etters, and blogs, and many people started talking about us on social media. We are still getting traffic from all these
 sites. We gained upward of 1k signed-up users from these two launches. This was big for us. We now have a better domain
 rating and authority, which is worth every penny.

So, how did we do it?

We were on a tight budget, so we had to do ev
erything ourselves.

1. **Blogs** As we are a dev tool start-up and our ICP is a software developer; we wrote blogs on D
evTo, HackerNoon, etc. This only got us 1.5k visitors. If you are serving developers, consider this.
2. **Collabs**: We 
collaborated with a few reputed brands in the industry, like LangChain (we used their framework to build an agent that t
opped the SWE bench), Replit, LlamaIndex, etc., so it was easy for them to promote us. Always make sure you’re providing
 value before reaching out. Reach out to the brands you have made your app with; they are usually open to share if there
 is an 'Aha' factor.
3. **Social Media** It was the centrepiece of our marketing channels.
   * **Reddit**: We found rel
evant subreddits for our niche, like LocalLlama, Self-hosted, Open-source, Programming, etc. and wrote about us, ensurin
g it didn’t violate rules.
   * **X(Twitter)/LinkedIn:** Posted a long-form catchy launch post with a video illustration
, as these platforms are biased around it. Also, we made the brand's quote repost us. If you do not have brand collabs, 
get influencers from your niche and try to boost it. Instead of a different post, ask them to quote it. This worked bett
er for us.
4. **Slack Channels** This might be icky, but it works. We collected a lot of Slack channels. Set up automati
on and send messages to members. This is still a danger zone, as you risk getting called out. Good, meaning people will 
be fine with it. You can do it at your own risk.
5. Once you rank on top, milk it to the best of your ability, writing b
logs and tweets and sharing as much as possible.

We did this for all our launches, and we got a really good number of i
mpressions (200k+) and users.

At the end of the day, it’s you and your product. Make sure it is interesting and provide
s value to the intended users.

Feel free to ask any questions or share anything you have done that helped you. Let’s he
lp each other.
```
---

     
 
all -  [ Structured data chunking for RAG ](https://www.reddit.com/r/Rag/comments/1h5kbus/structured_data_chunking_for_rag/) , 2024-12-06-0914
```
Hey! I wanted to ask if someone knows what is the best way to chunk structured data (csv, xls, ...) for RAG optimisation
, and why. It seems that LangChains CSVLoader chunks each row separately as a chunk and I get it, but I think its not th
at efficient. On the other hand if there is another chunking technique for these files then it would mix the semantics i
n one chunk (ex. multiple rows in a chunk), but would be more efficient. How do we deal with this? Also could you please
 tell me what is the best (efficiency and RAG performance) chunking strategy for Unstructured files and why? Thank you!
```
---

     
 
all -  [ Enhancing RAG Input with ParentDocumentRetriever: Debugging Missing Embeddings






 ](https://www.reddit.com/r/LangChain/comments/1h5jty3/enhancing_rag_input_with_parentdocumentretriever/) , 2024-12-06-0914
```
  
I am attempting to enhance my RAG (Retrieval-Augmented Generation) input by implementing the `ParentDocumentRetriever
`. However, when I tried to access the vector store, I encountered an issue where the embeddings section returned `None`
. The output is as follows:

`{`

  `'ids': [`

`'470b54cc-45d8-4c3f-b0a0-180b4e0f6f47',`

`'dd4d9324-649f-4438-b07c-b2c
f9294f2d2',`

`'80211d88-6e27-4878-8ea4-5490243707d3',`

`'c534b3f4-2dcd-482f-9f22-b93c5be3e93f'`

  `],`

  `'embedding
s': null,`

  `'documents': [`

`'This is a test sentence.',`

`'Another test document for embedding.',`

`'This is a te
st sentence.',`

`'Another test document for embedding.'`

  `],`

  `'uris': null,`

  `'data': null,`

  `'metadatas':
 [null]`

`}`

  
could someone help


```
---

     
 
all -  [ What tool is used to create hand-drawn style figures such as in the LangChain documentation? ](https://www.reddit.com/r/LangChain/comments/1h5jd0v/what_tool_is_used_to_create_handdrawn_style/) , 2024-12-06-0914
```
Hi,

I am working on a presentation, and I would like to draw a similar hand-drawn style graph to the ones in the LangCh
ain documention (e.g., [RAG flowchart](https://docs.smith.langchain.com/assets/images/b6c2e61d-ca0c-47a6-a660-b009ecde7a
69-b48370416ca48e217afecd203acb5987.png)).

Does anyone know what do they use to create such figures? Otherwise similar 
tools are also appreciated.
```
---

     
 
all -  [ Help me understand what can be improved about this template and resume. ](https://i.redd.it/l041wdjswk4e1.jpeg) , 2024-12-06-0914
```
Dealing with consistent rejections😭
```
---

     
 
all -  [ Need your perspective to land an entry level job ](https://www.reddit.com/r/datascience/comments/1h5e67f/need_your_perspective_to_land_an_entry_level_job/) , 2024-12-06-0914
```
Looking at the current market trends, what skills do you think one should focus on to land an entry level data analyst/d
ata science job in 8-9 months? 

Portfolio building, networking and preparing for interviews is already assumed but ...


Our time is limited. We cannot learn and focus on everything. What skills might be best spend on to land a job within t
his timeframe.

My educational background: 

1. Bachelor of Computing in Information Systems 

2. Currently persuing Msc
 Data Science and Computational Intelligence. (9 months left to graduate). All courses are finished, just the thesis lef
t.

My professional background:

Have experience as a content writer, content editor, technical writer etc.

Have done a
n 8 week Software Engineering internship (focused on fullstack JS/TS stack.)

Have done 2 months Internship as a 'Data S
cience intern' but it was focused on web scraping, cleaning data obtained through an API to generate market leads, build
ing proof of concept LLM applications using Langchain and Google Gemini/OpenAI API keys.

Note: 


1. I'm from a 3rd wor
ld country. I cannot offer you any financial compensation for your detailed guided response even if I really want to (un
less it is in Nrs). So, please ignore this post, it you are looking for monetary reward for you high quality response.


2. Please don't ask me to look at job postings, ask ChatGPT, Google. I've done those things. Job descriptions are like w
ishlists. If I read a JD, I come up with an impression that I need to have 10 year internship experience with almost eve
ry technology imaginable just to land an entry level job.  Provide me with your personal perspective.
  
```
---

     
 
all -  [ Help me Optimizing AI Application Deployment ](https://www.reddit.com/r/LangChain/comments/1h5c52s/help_me_optimizing_ai_application_deployment/) , 2024-12-06-0914
```
I'm developing an AI application using LangChain and OpenAI, and I want to deploy it in a scalable and fast way. I'm con
sidering using containers and Kubernetes, but I'm unsure how optimal it would be to deploy this application with a vecto
rized database running on it (without using third-party services), a retriever argument generator, and FastAPI. Could yo
u provide suggestions on how best to deploy this application?
```
---

     
 
all -  [ Evaluation metrics for llm summary  ](https://www.reddit.com/r/LangChain/comments/1h5a1sj/evaluation_metrics_for_llm_summary/) , 2024-12-06-0914
```
I am working on long document summarization model using gpt-4o-mini and mistralAI.

I want compare my llm output with hu
man output. 

Initially,i compared with Abstract as reference with llm output. The results such as blue,rouge are varyin
g at broad range. 

I absorbed that length of a llm output is double the abstract.

So, I am looking for suggestions to 
evaluate llm summary output only, for eg: before and after improving context of llm with external information.
```
---

     
 
MachineLearning -  [ [P] Minima: local conversational retrieval augmented generation project (Ollama, Langchain, FastAPI, ](https://www.reddit.com/r/MachineLearning/comments/1h1pudq/p_minima_local_conversational_retrieval_augmented/) , 2024-12-06-0914
```
  
[https://github.com/dmayboroda/minima](https://github.com/dmayboroda/minima)  
  
Hey everyone, I would like to intro
duce you my latest repo, that is a local conversational rag on your files, Be honest, you can use this as a rag on-premi
ses, cause it is build with docker, langchain, ollama, fastapi, hf All models download automatically, soon I'll add an a
bility to choose a model For now solution contains:

* Locally running Ollama (currently qwen-0.5b model hardcoded, soon
 you'll be able to choose a model from ollama registry)
* Local indexing (using sentence-transformer embedding model, yo
u can switch to other model, but only sentence-transformers applied, also will be changed soon)
* Qdrant container runni
ng on your machine
* Reranker running locally (BAAI/bge-reranker-base currently hardcoded, but i will also add an abilit
y to choose a reranker)
* Websocket based chat with saving history
* Simple chat UI written with React
* As a plus, you 
can use local rag with ChatGPT as a custom GPT, so you able to query your local data through official chatgpt web and ma
c os/ios app.
* You can deploy it as a RAG on-premises, all containers can work on CPU machines

Couple of ideas/problem
s:

* Model Context Protocol support
* Right now there is no incremental indexing or reindexing
* No selection for the m
odels (will be added soon)
* Different environment support (cuda, mps, custom npu's)

Welcome to contribute (watch, fork
, star) Thank you so much!
```
---

     
 
MachineLearning -  [ [P] Open-source declarative framework to build LLM applications - looking for contributors ](https://www.reddit.com/r/MachineLearning/comments/1gkpazh/p_opensource_declarative_framework_to_build_llm/) , 2024-12-06-0914
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

     
