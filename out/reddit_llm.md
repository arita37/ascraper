 
all -  [ Trying to get into a prestigious AI master's program and I'm wondering what projects would be impres ](https://www.reddit.com/r/learnmachinelearning/comments/18seo0l/trying_to_get_into_a_prestigious_ai_masters/) , 2023-12-28-0910
```
I have about 2-3 more months to bolster my resume before the deadline for my master's applications, and I am wondering w
hat projects would be impressive to the professors reviewing my application. Currently, I have a big project using LangC
hain that I did for a company and a project analyzing shooting data and making predictions. I feel like professors will 
automatically discount my application because I majored in Information Systems, not CS or math, so I want to add somethi
ng very impressive to make up for that.
```
---

     
 
all -  [ Why do the langchain docs feel so all over the place? ](https://www.reddit.com/r/LangChain/comments/18sdap4/why_do_the_langchain_docs_feel_so_all_over_the/) , 2023-12-28-0910
```
Been using langchain for a bit but these docs just annoy the hell out of me now. Is there any possible refactor that cou
ld help maybe or it’s just too bloated now? Seems like 5 ways to do 1 thing at times.
```
---

     
 
all -  [ RAG with Langchain Huggingface ](https://www.reddit.com/r/LangChain/comments/18sbixy/rag_with_langchain_huggingface/) , 2023-12-28-0910
```
I am trying to implement a chatbot where a user can chat about a document. I am trying to implement it where I read the 
document through Langcahin -> create embedding and store them (use a huggingface model for embedding) in Chroma -> answe
r question where I use a huggingface model for LLM. I tried to use a QuestionAnswering Huggingface model, but I got an e
rror. Then I looked at the github code of Langchain and it says they only support few model types which are text-generat
ion, text2text-generation and summarization. 
Has anyone been able to implement this?
```
---

     
 
all -  [ chatgpt4 api dont work for me ](https://www.reddit.com/r/LangChain/comments/18s9pai/chatgpt4_api_dont_work_for_me/) , 2023-12-28-0910
```
guys i have problem with my chatgpt4 acc i never use the api before but when i call for useing it he gives me this error
 msg ' You exceeded your current quota, please check your plan and billing details. For more information on this error, 
read the docs: https://platform.openai.com/docs/guides/error-codes/api-errors. ' even if i have already 18 dollas as cre
dit and the graph said i never use it how can i solve this problem and can someone give me apt key  i really need it cuz
 i need to use it in univ project 

thanks to all of you .
```
---

     
 
all -  [ Turing Technical call ](https://www.reddit.com/r/LangChain/comments/18s795c/turing_technical_call/) , 2023-12-28-0910
```
 

I just received a call from Turing for a job, but it mentions a very broad domain, including:

Communication Skills


Machine Learning and Deep Learning Models

Python and large Language Models (LLMs)

AI Problem Solving

My call is in on
e day, and I'm confused about which concepts I should revise and the people in the CC are mostly Non-technical.
```
---

     
 
all -  [ Processing complex word documents with equations. ](https://www.reddit.com/r/LangChain/comments/18s4fxg/processing_complex_word_documents_with_equations/) , 2023-12-28-0910
```
I have a project that requires to extract data from complex word documents.

Each document is composed of a few tables (
10 to 30). In each tables I might have :

* Text
* Mathematical equations
* Images (mostly math graphs).

My initial goa
l is to be able to process the text and equations, I'll leave the images for latter.

So far I haven't been able to retr
ieve the equations in the table. I have tried the following methods:

* langchain + docx2txt : 1 huge blob of text, not 
exploitable at all.
* lagnchain + unstructured in classical mode : same.
* langchain + unstructured + elements : I got a
 list of tables, which is nice, however in both the tables\[1\]\['kwargs'\]\['metadata'\]\['text\_as\_html'\] and tables
\[1\]\['kwargs'\]\['page\_content'\] the equations aren't shown.
* pandoc docs -> html : both the equations and images a
re represented as html **{=html}** and no content is shown.

I suppose that my next best solution is to use OCR like log
ic but I don't really like the idea. Do you have any suggestion ?

&#x200B;
```
---

     
 
all -  [ How to delete an agent? ](https://www.reddit.com/r/LangChain/comments/18s3qre/how_to_delete_an_agent/) , 2023-12-28-0910
```
Hi everyone, I am building a python app that creates a new agent for each user. For security reasons, I need to delete t
he agent completely after use. I have searched everywhere but didn't find a way to do it...
```
---

     
 
all -  [ Simple Local Models Answers Evaluation Colab example (with GPT4, no langchain etc.) ](https://www.reddit.com/r/LocalLLaMA/comments/18s0t6q/simple_local_models_answers_evaluation_colab/) , 2023-12-28-0910
```
Hi, beloved sub!

I have tried to find any ready-to-go simple examples of local model response evaluation with GPT4 but 
have seen only complicated implementations with heavy libraries like langchaing, etc. 

[Here](https://colab.research.go
ogle.com/drive/1sfxCoW2tJd6IJ_psSumGWzNwqEbtbu-4?usp=sharing), I implemented a simple Python LLM answers scoring Colab w
ith GPT4 API and OpenAI functions. You can adapt it to process multiple responses from the local LLM, which could be use
ful for comparing different models. 

It is a reliable approach that I first encountered in the paper '[TinyStories](htt
ps://arxiv.org/abs/2305.07759)' (where a tiny 2.5 **million** parameters model solves a Creative Writing task), and base
d on their approach, I made a new version that our team uses for Creative Writing task evaluation at [littlestory.io](ht
tps://littlestory.io) (kids bedtime stories generation, we have scored like that thousands of stories already).

All sco
res will be given in the valid JSON format. 

**How to use colab:**

1) Specify your text language and past text that yo
u want to score;

2) Specify your API key;

3) Update agent if needed; our mainly focuses on kids' safety and creative w
riting;

4) Batch process answers of your local LLM and save responses.

That's it. It's quite simple

&#x200B;

Previou
s tutorials:

\[[Tutorial](https://www.reddit.com/r/LocalLLaMA/comments/18dohlt/tutorial_use_real_books_wiki_pages_and_e
ven/)\] **Use real books, wiki pages, and even subtitles for roleplay with the RAG approach in Oobabooga WebUI + superbo
oga v2**

\[[Tutorial](https://www.reddit.com/r/LocalLLaMA/comments/17aswq4/tutorial_integrate_multimodal_llava_to_macs/
)\] **Integrate multimodal llava to Macs' right-click Finder menu for image captioning (or text parsing, etc) with llama
.cpp and Automator app**

\[[Tutorial](https://www.reddit.com/r/LocalLLaMA/comments/15snlv1/tutorial_simple_soft_unlock_
of_any_model_with_a/)\] **Simple Soft Unlock of any model with a negative prompt (no training, no fine-tuning, inference
 only fix)**

\[[Tutorial](https://www.reddit.com/r/LocalLLaMA/comments/13j3747/tutorial_a_simple_way_to_get_rid_of_as_a
n_ai/)\] **A simple way to get rid of '..as an AI language model...' answers from any model without finetuning the model
, with llama.cpp and --logit-bias flag**

**\[**[Tutorial](https://www.reddit.com/r/SteamDeck/comments/12k1d8h/manual_ho
w_to_install_large_language_model_vicuna/)**\] How to install Large Language Model Vicuna 7B + llama.ccp on Steam Deck**

```
---

     
 
all -  [ How does mapReduce work ](https://www.reddit.com/r/LangChain/comments/18s064m/how_does_mapreduce_work/) , 2023-12-28-0910
```
Hey guys,

im new to langchain and I'm wondering how the mapreduce function works.  


If I have a chunksize of 10.000 a
nd run the mapreduce function, how can it summarize the chunks with a size of 10.000? I thought the token limit is under
 10.000.  


And when i change the verbose bool to true, it just shows me that it summarize the content of the chunk (wh
ich is 10.000, so I thought it doenst work).  


Im trying to understand the logic but im so confused. 
```
---

     
 
all -  [ LLM taking too long time to respond ](https://www.reddit.com/r/LangChain/comments/18ry05l/llm_taking_too_long_time_to_respond/) , 2023-12-28-0910
```
The below code is taking more than 5 min to answer the question, any solution to this?  


llm = CTransformers(model='Th
eBloke/CodeLlama-7B-Instruct-GGUF'**,**  
 model\_file='codellama-7b-instruct.Q5\_K\_M.gguf'**,**  
 \# callbacks=\[Stre
amingStdOutCallbackHandler()\],  
 config={'max\_new\_tokens': **4096,**  
 'context\_length': **4000,**  
 'temperature
': **0.01**})  
agent = create\_csv\_agent(llm**,**  
 'August2023.csv'**,**  
 verbose=True**,**  
 agent\_type=AgentTy
pe.ZERO\_SHOT\_REACT\_DESCRIPTION**,**)

agent.run('how many rows are there?')
```
---

     
 
all -  [ Please review my resume!! ](https://www.reddit.com/r/resumes/comments/18rx3k8/please_review_my_resume/) , 2023-12-28-0910
```
I am a final year student applying for machine learning engineer roles.  
I have improved my resume after getting some a
dvice from this community.  
Please review my resume now

https://preview.redd.it/oswqhzup6t8c1.jpg?width=1275&format=pj
pg&auto=webp&s=3b227d779ab54f96694b2972cdb169044f4aa55d
```
---

     
 
all -  [ What is your strategy for doing inference over a large SQL dataset? ](https://www.reddit.com/r/LangChain/comments/18rw5rm/what_is_your_strategy_for_doing_inference_over_a/) , 2023-12-28-0910
```
I'm pretty new to Langchain, but I'm comfortable building RAG applications with 'static' data, such as PDFs, webpages, e
tc. I'm now trying out the SQL toolkit, but I have some questions.

Since you're still limited by the model's context wi
ndow size, it seems that only certain queries make sense. But what if you wanted to find trends or insights from a large
r amount of data, like store orders, or analytics data?

Would you do this in batches and then combine them? Would you v
ectorize the data first? Is it even feasible to do this currently?

I'm very interested to hear how you would approach t
his problem
```
---

     
 
all -  [ Seeking Advice for Building a School Handbook Chatbot Using OpenAI and Vector Databases ](https://www.reddit.com/r/ChatGPT/comments/18rnecd/seeking_advice_for_building_a_school_handbook/) , 2023-12-28-0910
```
 

Hello everyone,

I'm embarking on a project to create a chatbot for my school's handbook, aiming to make it a resourc
e for students to easily access information. As someone relatively new to AI, I'm seeking guidance on implementing this.


My current plan is to use OpenAI as the primary language learning model, focusing on affordability. I am considering i
ntegrating RAG (Retrieval-Augmented Generation) and LangChain for enhanced functionality. However, I'm quite perplexed a
bout choosing an appropriate vector database, as many options appear costly. The goal is to keep this system live and ac
cessible for student usage without breaking the bank.

I'm also looking into open-source embedding models to pair with t
he vector database. Pinecone has caught my attention, but its pricing seems steep for our budget.

Does anyone have reco
mmendations or tips on affordable yet effective tools and strategies for this project? Any insights on vector databases 
suitable for educational use, or ways to optimize cost without compromising quality, would be greatly appreciated.

Than
k you in advance for your help!

(I typed out my problem and had gpt4 fix up the format and wording dont bash me)
```
---

     
 
all -  [ [P] Seeking Advice for Building a School Handbook Chatbot Using OpenAI and Vector Databases ](https://www.reddit.com/r/MachineLearning/comments/18rndcp/p_seeking_advice_for_building_a_school_handbook/) , 2023-12-28-0910
```
Hello everyone,

I'm embarking on a project to create a chatbot for my school's handbook, aiming to make it a resource f
or students to easily access information. As someone relatively new to AI, I'm seeking guidance on implementing this.

M
y current plan is to use OpenAI as the primary language learning model, focusing on affordability. I am considering inte
grating RAG (Retrieval-Augmented Generation) and LangChain for enhanced functionality. However, I'm quite perplexed abou
t choosing an appropriate vector database, as many options appear costly. The goal is to keep this system live and acces
sible for student usage without breaking the bank.

I'm also looking into open-source embedding models to pair with the 
vector database. Pinecone has caught my attention, but its pricing seems steep for our budget.

Does anyone have recomme
ndations or tips on affordable yet effective tools and strategies for this project? Any insights on vector databases sui
table for educational use, or ways to optimize cost without compromising quality, would be greatly appreciated.

Thank y
ou in advance for your help!

(I typed out my problem and had gpt4 fix up the format and wording dont bash me)
```
---

     
 
all -  [ How to name an offline LLM? ](https://www.reddit.com/r/LocalLLaMA/comments/18rlqbw/how_to_name_an_offline_llm/) , 2023-12-28-0910
```
This is probably a really easy answer. Don’t laugh - I’m still learning.

I’m using on offline model with RAG. The data 
is stored in a Chroma DB. It’s doing its job, answering questions on the data it’s been training on (pdf books on data e
ngineering, governance and strategy). I’ve named it ‘Eva’. But how do I get it to respond to that? If I ask it for its n
ame, how do I get it to call itself Eva?

Right now the question gets passed into langchain RetrievalQA with chain_type=
‘stuff’. 

Do I need to feed it a md file into the Database to ‘tell it about itself’, or do I pass additional context i
nto the RetrievalQA process on every query?
```
---

     
 
all -  [ All 133 NextJS Boilerplates & Starters ](https://www.reddit.com/r/nextjs/comments/18riglc/all_133_nextjs_boilerplates_starters/) , 2023-12-28-0910
```
I spent some time collecting all NextJs starters from the internet.

I search Product Hunt, DevHunt, Twitter, Reddit.
Ho
pe it's helpful for others.

##Shipfast
N2 product of the day on PH (945 upvotes) . By @marc_louvion. Starts at $179. Co
nsidered to be the best by many.. Categories: premium.

##NextJS Boilerplate
5300 GitHub stars and 1000 forks. By @ixart
z. Categories: free.

##Shipixen
N1 product of the day (847 upvotes) on PH. By @d4m1n. Starts at $86. Categories: premiu
m.

##Boilercode
N1 product of the day (636 upvotes) on PH. By @manoj_ahi. Starts at $79. Categories: premium.

##SAAS S
tarter
1 review with 5 stars. By @sandeep_indie. Starts at $29. Categories: premium.

##Shipped
No reviews. Just launche
d. Starts at $129. By @ikoichi. Categories: premium.

##Nebula
Starts at $0. By @dlcastillop. Categories: free;premium.


##MongoDB
A Next.js and MongoDB web application; designed with simplicity for learning and real-world applicability in 
mind.. Categories: free.

##Next.js with TypeScript       
Basic. Categories: free.

##Emotion
Extract and inline critic
al css with @emotion/css; @emotion/server; @emotion/react; and @emotion/styled.. Categories: free.

##Apollo
integrate A
pollo seamlessly with Next.js data fetching methods to fetch queries in the server and hydrate them in the browser.. Cat
egories: free.

##Redux
Redux Toolkit TypeScript Example. Categories: free.

##Blazity
Enterprise-grade Next.js boilerpl
ate built with Tailwind CSS; Radix UI; TypeScript; ESLint; Prettier; Jest; Playwright; Storybook; etc.. Categories: free
.

##Nextlessjs
Next.js + Serverless. For scalable and production-ready SaaS products. It includes Authentication; Payme
nt; Teams; Dashboard; Landing Page; Emails. Starts at $699. Categories: premium.

##Create Next App   
An official Next.
js CLI tool for creating Next.js apps.. Categories: free.

##Next.js with CSS Modules
A Next.js example that demonstrate
s how to use CSS Modules.. Categories: free.

##Next.js with Sass
A Next.js example that demonstrates how to use Sass.. 
Categories: free.

##Next.js with Styled JSX
A Next.js example that demonstrates how to use Styled JSX.. Categories: fre
e.

##Next.js with CSS-in-JS
A Next.js example that demonstrates how to use CSS-in-JS.. Categories: free.

##Next.js wit
h Server-Side Rendering
A Next.js example that demonstrates how to use Server-Side Rendering.. Categories: free.

##Next
.js with Static Site Generation
A Next.js example that demonstrates how to use Static Site Generation.. Categories: free
.

##Next.js with API Routes
A Next.js example that demonstrates how to use API Routes.. Categories: free.

##Next.js wi
th Custom Server
A Next.js example that demonstrates how to use a custom server.. Categories: free.

##Next.js with Depl
oyment
A Next.js example that demonstrates how to deploy a Next.js app.. Categories: free.

##RAN Boilerplate
⚡ RAN! Rea
ct . GraphQL . Next.js Toolkit ⚡ - SEO-Ready; Production-Ready; SSR; Hot-Reload; CSS-in-JS; Caching; CLI commands. Categ
ories: free.

##Next.js with Stripe
A starter for using Stripe with Next.js. Categories: free.

##ReScript
Opinionated B
oilerplate for NextJS; Tailwind and ReScript. Categories: free.

##React Next
A basis for reducing the configuration of 
your projects with nextJS; best development practices and popular libraries. Categories: free.

##Crystallize 
Fully fea
tured Next.js / React eCommerce boilerplate. Combine rich marketing content with product information to create highly co
nverting online stores. Fully tuned for performance with JAMStack edge page generation.. Categories: free.

##Hasura 
🎨 
Boilerplate for building applications using Hasura and Next.js. Categories: free.

##React; Firebase Firestore
Blog buil
t with React; Next.js; Firebase Firestore; Styled-Component; Mobx State Tree. Categories: free.

##Electron ⚡
3.2k stars
. Categories: free.

##MongoDB 
1.5k stars. Categories: free.

##KNESTS Stack
Full-stack boilerplate (project/hackathon 
starter) with Docker/NodeJS/Typescript/GraphQL/React/Material-UI. Categories: free.

##Devii
A developer blog starter fo
r (Next.js + React + TypeScript + Markdown + syntax highlighting). Categories: free.

##Superplate
React Testing Library
; styled-component; React Query; .env; Axios; Bundle Analyzer; Prettier and 30+ plugins.  2.7k stars. Categories: free.


##Next.js PWA Firebase
Next.js serverless PWA with Firebase boilerplate. 204 stars. Categories: free.

##Blogging templ
ate for Netlify
Next.js blogging template for Netlify. Categories: free.

##Chakra
Battery packed template / boilerplate
 to initialize Next.js app with Chakra UI & Typescript setup ✨. Categories: free.

##Tailwind Starter Blog
Tailwind CSS 
blogging starter template.  6.1k stars. Categories: free.

##Prisma + tRPC
tRPC starter repo with E2E-testing. Categorie
s: free.

##create-t3-app
The best way to start a full-stack; typesafe Next.js app. Categories: free.

##Precedent
An op
inionated collection of components; hooks; and utilities for your Next.js project.. Categories: free.

##Shadcn/UI
Beaut
ifully designed components built with Radix UI and Tailwind CSS.. Categories: free.

##Nextacular 
Built on top of popul
ar and modern technologies such as Next JS; Tailwind; Prisma; and Stripe. Categories: free.

##Blitz
Blitz picks up wher
e Next.js leaves off; providing battle-tested libraries and conventions for shipping and scaling world wide applications
.. Categories: free.

##Next.js + Tailwind CSS + TypeScript
🔋 Next.js + Tailwind CSS + TypeScript starter and boilerplat
e packed with useful development features. Categories: free.

##Next Simple Starter
🐳 Simple and Accessible PWA boilerpl
ate with Nextjs 12 and MUI. Categories: free.

##Next Right Now
It’s a ready-to-use boilerplate based on the Next.js fra
mework.. Categories: free.

##Next.js Redux Starter
Next.js + Redux + styled-components + Express = 😇. Categories: free.


##Solid 
Solid is a free Next.js template specifically crafted for startups / SaaS and software websites.. Categories:
 free.

##Divjoy
Divjoy is a SaaS boilerplate built with Next.js; designed to help software developers quickly launch th
eir projects.. Categories: premium.

##Makerkit 
Makerkit is a SaaS boilerplate built on top of Next.js; designed for so
ftware developers.. Categories: premium.

##Ship SaaS
Build your SaaS in a weekend with a Next.js SaaS boilerplate. Cate
gories: premium.

##Supastarter
Supastarter is a SaaS boilerplate built on Next.js providing a pre-built foundation for 
developing SaaS applications.. Categories: free.

##Supanextail
Next.js based SaaS boilerplate that provides entrepreneu
rs and software developers with a scalable and customizable solution for rapidly launching their SaaS projects. Categori
es: free.

##SaasPlanet 
Powerful SaaS boilerplate built on Next.js. It comes with everything you need to launch your Sa
aS application including authentication / billing and subscription management.. Categories: premium.

##Nextbase
Nextbas
e is a SaaS boilerplate built on Next.js that simplifies building and launching SaaS applications.. Categories: premium.


##Basejump
Basejump is the ultimate SaaS boilerplate built on Next.js. Designed for entrepreneurs / startups / and sof
tware developers. Categories: free.

##Modern MERN
Create your SaaS products with the famous MERN stack using the latest
 technologies: Next.js / TypeScript / Tailwind CSS / Prisma / Serverless.. Categories: premium.

##Bedrock
Bedrock is a 
Next.js based SaaS boilerplate designed for entrepreneurs / managing directors and software developers.. Categories: fre
e.

##Next.js SaaS Boilerplate Generator
The Boilerplate Generator offers a Next.js-based SaaS boilerplate pre-equipped 
with elements such as user management / subscriptions and payment systems.. Categories: premium.

##SaaS UI
Saas UI is a
 React component library and starterkit that doesn't get in your way and helps you build intuitive SaaS products with sp
eed.. Categories: premium.

##ZippyStarter
Free up days of dev time; choose from a range of visually-stunning templates 
and ship landing pages / MDX blogs / portfolios / websites and more.. Categories: premium.

##Satria AI
Helping organisa
tions build AI-powered products. Categories: premium.

##T3
The best way to start a full-stack typesafe Next.js app. Cat
egories: free.

##NextJs Dashboard
A Next.JS boilerplate with the famous Open Source Boostrap Admin Template / CoreUI.. 
Categories: free.

##Next Boilerplate
Next.JS / Shadcn/ui / Tailwind / ESLint and Prettier Boiler plate code with Dark m
ode Toggler.. Categories: free.

##Kirimase
Command-line tool for building full-stack Next.js apps faster. It supercharg
es your development workflow; allowing you to quickly integrate packages and scaffold resources for your application. Ca
tegories: free.

##Indiespace: SaaS Bundle
Indiespace offers a Next.js SaaS Bundle that includes landing & waitlist page
s with an already setup SaaS boilerplate with every feature you need to get started. Starts at $39.. Categories: premium
.

##Boilercode app
Build production-ready SaaS products effortlessly with preconfigured code. Starts at $35. Categories
: premium.

##Kami
Kami (short for Kaminari) is a modern Next.js Tailwind CSS and shadcn-ui boilerplate. Categories: fre
e.

##Next starter
A starter project for next js with authentication - Contains React 17 + Typescript + Tailwind CSS etc
. Categories: free.

##Next Express
⚡ JavaScript boilerplate for a full stack app built using React.js / Next.js / Expre
ss.js / react-bootstrap / SCSS and full SSR with eslint.. Categories: free.

##NextJS Redux-Wrapper Material-UI
A boiler
plate NextJS with Redux and Material UI. Categories: free.

##Staart
A starter library for node projects with user accou
nts.. Categories: free.

##Next Boilerplate
Simple and easy to use / somewhat opinionated Next boilerplate with redux / 
redux-saga / dynamic routing / external css / scss and all the cool stuff!. Categories: free.

##NextStarter
🚀 boilerpla
te for starting projects in next.js. Categories: free.

##Next SMRT
Next.js / Styled-Components / Material UI / Redux / 
Typescript Boilerplate (Docker Ready). Categories: free.

##the NextJS starter
Another Next.js boilerplate. Categories: 
free.

##NextJS Blog Boilerplate
Starter code for your Next.js blog Boilerplate with Tailwind CSS. Categories: free.

##
🤖 Lobe Chat
Open-source‚ high-performance chatbot framework that supports speech synthesis‚ multimodal‚ and extensible F
unction Call plugin system. Supports one-click free deployment of your private ChatGPT/LLM web application.. Categories:
 free.

##Gravity
Spin up a new SaaS product in 5 minutes with the leading Node.js SaaS boilerplate. Contains all featur
es you need in a single install‚ even AI.. Categories: premium.

##SaaS Starter Kit
Saas Starter Kit is a modern and com
prehensive SAAS boilerplate that has all the features you would expect in a SAAS and much more. Scroll down to learn mor
e.. Categories: free.

##SimonHoiberg SaaS Template
End-to-end SaaS Template using AWS Amplify‚ Apollo Client‚ Chakra‚ a
nd NextJS.. Categories: free.

##BoxyHQ Enterprise SaaS Starter Kit
Next.js-based SaaS starter kit saves you months of d
evelopment by starting you off with all the features that are the same in every product‚ so you can focus on what makes 
your app unique.. Categories: free.

##Ship Apps Fast
Launch Your Product in Record Time with NextJS SaaS Boilerplate. S
ave months of development time setting up Authentication‚ Database‚ Payments‚ Landing page and whole lot more.. Categori
es: premium.

##Serverless SaaS
Serverless SaaS is a starter kit that serves as the perfect starting point for your SaaS
 product. Save months of development time and skip implementing authentication‚ payments‚ teams‚ and more.. Categories: 
premium.

##Hyper SaaS
Build your SaaS project in record time 🚀 Whether you're a startup seeking to disrupt markets or a
 developer looking to enhance your productivity‚ HyperSaas has everything you need to hit the ground running.. Categorie
s: premium.

##SAAS Starter Kit Pro
Saas Starter Kit is a modern SAAS boilerplate. Save weeks of development time having
 standard SAAS features implemented for you‚ and start building your core app right away.. Categories: free.

##Nextacul
ar
An open-source starter kit built with modern full-stack technologies. Worry less and save time developing basic SaaS 
features. Categories: free.

##React & Firebase SaaS Starter
Say goodbye to months of development time and hello to a fu
lly-functional SaaS in minutes.React‚ Firebase‚ authentication‚ serverless backend‚ Tailwind CSS‚ and payments are all h
ooked up and ready for your next project.. Categories: premium.

##Kickstart App
Kickstart is the Nextjs boilerplate for
 building apps fast.. Categories: premium.

##Vercel Blob Next.js Starter
Simple Next.js template that uses Vercel Blob 
for image uploads. Categories: free.

##Next.js Blog with microCMS
A simple blog built with Next.js and microCMS.. Categ
ories: free.

##LangChain + Next.js Starter
Starter template and example use-cases for LangChain projects in Next.js / i
ncluding chat / agents / and retrieval.. Categories: free.

##RAGBot Starter — An Astra DB and OpenAI chatbot
Starter pr
oject for creating a chatbot using Astra DB and OpenAI.. Categories: free.

##Salesforce Commerce Cloud Starter
A coffee
 ecommerce store built on Next.js and Salesforce Commerce Cloud.. Categories: free.

##Next.js Prisma Postgres Auth Star
ter
Simple Next.js 13 App Router starter kit that uses NextAuth.js for auth / Prisma as the ORM and Vercel Postgres as a
 database.. Categories: free.

##Next.js Contentlayer Blog Starter
A blog template with Next.js 13 App Router / Contentl
ayer / Tailwind CSS and dark mode.. Categories: free.

##Next.js Enterprise Boilerplate
Enterprise-grade Next.js boilerp
late built with Tailwind CSS / Radix UI / TypeScript / ESLint / Prettier / Jest / Playwright / Storybook etc.. Categorie
s: free.

##Next.js App Router Playground
Explore the new app directory (App Router) in Next.js 13.. Categories: free.


##Admin Dashboard Template
Tailwind CSS / Postgres and Auth set up.. Categories: free.

##Image Gallery Starter
An image
 gallery built on Next.js and Cloudinary.. Categories: free.

##Next.js Boilerplate
Get started with Next.js and React i
n seconds.. Categories: free.

##Precedent – Next.js Starter
A collection of components / hooks and utilities built on N
ext.js / Typescript / Tailwind / Radix / Framer Motion / Prisma and PostgreSQL.. Categories: free.

##Nextplate
Nextplat
e is a free starter template built with Next.js and TailwindCSS. It provides you with almost everything you need to jump
-start your Next.js project. Try Nextplate and save yourself hours of work.. Categories: free.

##Next.js project
🐤 A sa
mple Next.js project for getting started with MDX‚ Theme UI‚ & Hack Club Theme.. Categories: free.

##NextSSS
Next.js st
atic site starter including full setup for TypeScript‚ Tailwind CSS‚ Google Analytics‚ Next SEO‚ etc.. Categories: free.


##Chakra Nextstarter
battery packed template / boilerplate to initialize Next.js app with Chakra UI & Typescript setup
 ✨. Categories: free.

##Next.JS with Firebase
NextJS boiler-plate with Google's Firebase integrated. Categories: free.


##Modern React Portfolio Template
Modern React Portfolio Template (FREE). Categories: free.

##Next.js for Firebase Aut
h
Next.js starter code for Implementing Firebase Auth + Firestore + Cloud Messaging. Categories: free.

##NextPostgres
[
OUTDATED] A minimal example web application using NextJS 12.0.7‚ Postgres 11‚ Google OAuth2 and other useful libraries..
 Categories: free.

##This project is an example of React + Next.js + Postgres
This project is an example of React + Nex
tJS + Postgres. It is tailored for those who are enthusiastic about building websites with 100% JavaScript. It is design
ed in a way that makes you want to change it and very easy to change.. Categories: free.

##Next.js eCommerce template
T
he furniture boilerplate is a fully-featured eCommerce boilerplate built using Next.js and Crystallize. The boilerplate 
was developed with performance‚ a good developer experience‚ and best practices in mind.. Categories: free.

##Starter P
roject
Nextjs 9 + Material UI + mySQL Starter
. Categories: free.

##Email login system starter
A simple email login sys
tem starter built using Next.js‚ Reactstrap‚ Node.js Express and MySQL. Categories: free.

##NextJS Starter
A starter pr
oject for next js with authentication - Contains React 17 + Typescript + Tailwind CSS 2 + React Query 3 + GitHub Auth + 
LinkedIn Auth + Password-less Auth + Fauna DB + ESLint + Prettier + Husky. Categories: free.

##Landing Page theme
🚀 Fre
e NextJS Landing Page Template written in Tailwind CSS 3 and TypeScript ⚡️ Made with developer experience first: Next.js
 13 + TypeScript + ESLint + Prettier + Husky + Lint-Staged + VSCode + Netlify + PostCSS + Tailwind CSS. Categories: free
.

##Boilerplate and Starter
Boilerplate and Starter for Next.js 14+ with App Router and Page Router support‚ Tailwind C
SS 3.3 and TypeScript. Categories: free.

##Next.js eCommerce template
Fullstack Next.js E-Commerce made with NextAuth +
 Prisma‚ Docker + TypeScript + React Query + Stripe + Tailwind Sentry and much more 🛒. Categories: free.

##Next E-Comme
rce
An e-commerce website example with NextJS that I made in 1 week as a self challenge. Using Firebase as backend.. Cat
egories: free.

##Next-Shopify Starter
Nextjs + Tailwind CSS + Shopify Starter. Categories: free.

##Next-ecommerce
A be
autiful ecommerce made with Next.js. Categories: free.

##E-Commerce Starter NextJS
⚡ Quantum Ecommerce. Made with Next.
js | GraphQL | Apollo Server | Apollo Client | SSR. Categories: free.

##Commerce
Next.js Commerce. Categories: free.

#
#Pankod
Performance oriented Next.js application boilerplate with Redux‚ Typescript‚ Express.js‚ Sass and Project CLI.. 
Categories: free.

##Nextjs-boilerplate
☂️ NextJS Boilerplate with TailwindCSS‚ Typescript‚ Prettier‚ and Google Analyti
cs. For CI/CD with Vercel. Categories: free.

##NextBP
A boilerplate website available for the user customization. Categ
ories: free.

##Songlist
NextJS Boilerplate
. Categories: free.

##Sanity
This boilerplate facilitates using monorepo wi
th dependencies from both Next.js 12 and Sanity.io for the development stage.. Categories: free.

##NestaJS
Nesta.js is 
the perfect starting point for your next big idea. Focus on what matters: your application.. Categories: premium.

Link:
 [nextjsstarter.com](nextjsstarter.com)
```
---

     
 
all -  [ Mixtral 8x7B instruct for chatting with memory? ](https://www.reddit.com/r/LocalLLaMA/comments/18rhmi1/mixtral_8x7b_instruct_for_chatting_with_memory/) , 2023-12-28-0910
```
Hi y'all,

Just experimented mixtral 8X7b instruct version. It works well for RAG if there is only one exchange of promp
t+answer.

With LLAMA2 70B chat version, it's fairly easy to add a memory functionality using langchain in the QA retrie
val chain. 

But I can't find a solution to add a chat history/memory with this mixtral instruct version. 

Is there a w
orkaround solution to initiate/update/incorporate memory in this mixtral case?
```
---

     
 
all -  [ LCEL with prompts containing code ](https://www.reddit.com/r/LangChain/comments/18rhe6i/lcel_with_prompts_containing_code/) , 2023-12-28-0910
```
I've noticed that LCEL is picky about the curly braces used within prompts, which is somewhat problematic when the promp
t contains code, like for few-shot code gen use cases. Has anyone found a graceful way to handle the curly braces so Lan
gChain doesn't think they're parameters for string substitution? So far, I've been replacing them with double curly brac
es, but it's not very elegant.
```
---

     
 
all -  [ Serialize agent/llm objects into files for serving ](https://www.reddit.com/r/LangChain/comments/18rglvu/serialize_agentllm_objects_into_files_for_serving/) , 2023-12-28-0910
```
I'm looking for an advice on how to create REST service that configures agents on runtime.

I have a service that curren
tly runs on fastapi, but if there's any other tool that might be useful for this, I'm open to suggestion. This app is ve
ry simple, it has a route  `POST /ask` that simply prompts a pre-configured agent. In addition, I want to have another `
POST /refresh-agent` that in the body gets 'uri' argument that will point to a storage path that is the serialized objec
t of the new agent.

For example, I have an agent that I've pickled:

    from langchain.agents import AgentType, initia
lize_agent
    from langchain.agents import Tool
    from langchain.chains import LLMMathChain
    from langchain.llms i
mport OpenAI
    
    llm = OpenAI(openai_api_key='...')
    
    llm_math = LLMMathChain(llm=llm)
    
    math_tool = 
Tool(
        name='Calculator',
        func=llm_math.run,
        description='Useful for when you need to answer ques
tions about math.'
    )
    tools = [math_tool]
    agent = initialize_agent(
        tools,
        llm,
        agent
=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    )
    with open('fresh_agent.pkl', 'wb') as f:
        pickle.dump(agent, ha
ndle, protocol=pickle.HIGHEST_PROTOCOL)

And the `/refresh-agent` will look like - 

    @router.post('/refresh-agent')

    def refresh_agent(uri: str):
        with open(uri, 'rb') as f:
            agent = pickle.load(f)

Is this a flow t
hat exists in applications? is it common? Is there any tool or file format (that might be better than pickle) or serving
 framework that can somehow help me in this? Any help would be appreciated.
```
---

     
 
all -  [ Output get cuts off at around 1400 characters ](https://www.reddit.com/r/LangChain/comments/18repd6/output_get_cuts_off_at_around_1400_characters/) , 2023-12-28-0910
```
Hey guys,

maybe someone can help me.

I have this code and an input text which is 15.737 characters long.

And my endre
sult is cut off at around 1400 characters but idk why

&#x200B;

&#x200B;

      try {
          // Create language mode
l
          const model = new OpenAI({
            openAIApiKey: 'key',
            temperature: 0,
          });
    
 
         // Splitting text
          const textSplitter = new RecursiveCharacterTextSplitter({
            chunkSize: 10
00, // 1000
            chunkOverlap: 200, // 200
          });
          const docs = await textSplitter.createDocument
s([formData.text]);
          console.log(docs);
    
          const combineMapPromptTemplate = `You will be given a pa
rt of a scientific paper. This part will be enclosed in triple hashtags (###).
          Extract the key ideas and conce
pts in 3 bullet points.
          
          ###'{text}'###`;
    
          const combinePromptTemplate = `As a profess
ional summarizer, create a concise and comprehensive summary of the provided text -
          The text will be enclosed 
in triple hashtags (###) - while adhering to these guidelines:
          1. Craft a summary that is concise and to the p
oint with a well-organized structure.
          2. Write in a natural and conversational language with an engaging and i
nformative tone.
          3. Incorporate main ideas and essential information, eliminating extraneous language and focu
sing on critical aspects.
          4. Rely strictly on the provided text, without including external information.
     
     5. Your response should be at least three paragraphs and fully encompass what was said in the text.      
         
 
          ###'{text}'###`;
    
          const combineMapPrompt = new PromptTemplate({
            template: combineM
apPromptTemplate,
            inputVariables: ['text'],
          });
          const combinePrompt = new PromptTemplate
({
            template: combinePromptTemplate,
            inputVariables: ['text'],
          });
    
          // Th
is convenience function creates a document chain prompted to summarize a set of documents.
          const chain = loadS
ummarizationChain(model, {
            type: 'map_reduce',
            returnIntermediateSteps: true,
            combin
eMapPrompt: combineMapPrompt,
            combinePrompt: combinePrompt,
          });
          const res = await chain.
call({
            input_documents: docs,
          });
          console.log(res);
    
          await insertData(form
Data, res);
    
          setResponse([res]);
        } catch (e) {
          console.error(e);
          throw new Err
or('Something failed');
        }

&#x200B;
```
---

     
 
all -  [ Any good prompt management & versioning tools out there, that integrate nicely? ](https://www.reddit.com/r/LangChain/comments/18rb334/any_good_prompt_management_versioning_tools_out/) , 2023-12-28-0910
```
There are tools out there like PromptHub, or PromptKnit, that let you manage prompts, compare versions, and easily test 
them.

But that's **all they do**, they only focus on prompts.

On the other hand you have tools like Flowise and Langfl
ow which are robust and great for LLM pipelines, and fast prototyping. But they are **not good** for versioning, and col
laborating with non-technical people on prompt design.

&#x200B;

I couldn't find a tool where I enjoy **both worlds**, 
but it would be enough to keep the tools separate, and integrate. For example manage the prompts & their versions in Ser
vice A, and use them in Service B (e.g. Flowise).

&#x200B;

Our team is building LLM apps, and is trying to find a good
 way to prototype and collaborate, where someone like the product manager can come in and play with different versions o
f one of the prompts in the chain.
```
---

     
 
all -  [ Creating a scalable book questioner ](https://www.reddit.com/r/LangChain/comments/18r7ls5/creating_a_scalable_book_questioner/) , 2023-12-28-0910
```
Hello y'all!
I have a working demo for a tool that reads in ebook files, splits chapters into document objects, then fee
ds it into a VectorstoreIndex. I am able to query against it's data. Once it's finished I want to share it with everyone
 as I see people have trouble remembering what they read in books.

My question is, if I want to add more books, or just
 use another one to question, should I be creating separate VectorstoreIndexes or just feed everything into one and filt
er it based on metadata (title, author, ISBN, chapter)? If I want a summary for example, would langchain be able to sele
ct all the chapters and not just what it sees as relevant?

And also I have some problems with prompting, I use GPT 3.5 
turbo, and when I ask it to create rehearsal questions based on the book it gives quite mediocre and hyper specific ones
 that are almost irrelevant. The prompt I used: `Write 10 test questions from this book in the following format, while e
scaping special characters from the source: {'questions':[{'source':'exact sentences for the information source only','q
uestion':'','answer_1':'','answer_2':'','answer_3':'','answer_4':'','correct_answer_key':'answer_*'}]}`.
I want to feed 
the results into some UI to see what I was able to remember from a book on my phone as well.

Thanks for reading, hopefu
lly if you could help me I could help many others.
```
---

     
 
all -  [ HELP! ](https://i.redd.it/geomq7qo0m8c1.jpeg) , 2023-12-28-0910
```

```
---

     
 
all -  [ Where can I learn about schemas? ](https://www.reddit.com/r/LangChain/comments/18r3awq/where_can_i_learn_about_schemas/) , 2023-12-28-0910
```
Pretty straight forward question, apart from langchain documentation. Do you have a resource?
```
---

     
 
all -  [ Is Langchain the right choice, or can I rely on Chat GPT for this? ](https://www.reddit.com/r/LangChain/comments/18qtquw/is_langchain_the_right_choice_or_can_i_rely_on/) , 2023-12-28-0910
```
I'm interested in creating an AI model that takes in a user's input, which comes in the form of a JSON dictionary of the
 music the user likes, and provides recommendations. For example: {name: Mike, genre: hip-hop, song: Gangsta's Paradise}
. I want to create a prompt where I explain what different genres mean, such as rock, pop, and R&B music. The AI would t
hen look at the prompt to understand the genre and provide me with recommendations for similar music.

&#x200B;

I've be
en playing around, but I'm unsure of how to accomplish this initial idea. The initial idea was to use Structured Output 
Parser where I define the genre and a Prompt Template where I specify how it should answer the user's input. Am I on the
 right track? Thanks in advance.

&#x200B;
```
---

     
 
all -  [ How do I let llm read my json file and give an answer to a question? Python ](https://www.reddit.com/r/LangChain/comments/18qs349/how_do_i_let_llm_read_my_json_file_and_give_an/) , 2023-12-28-0910
```
I have a json file less than < 50mb, that has this format:

{  
'title': 'string',

'url': '[u](https://www.uvu.edu/cet/
blog/posts/cgmt_fundraiser_2022.html)rl.html',

'html': 'html content...'  
},

...

and I tried to look for langchain d
oc that can let openai api like gpt3.5 read json file and give an answer from those data, but it was really hard to find
 out the doc I wanted.   


So, I wonder if anyone knows how to connect json data, and llm to make a chatbot like llm.  



  
\#Langchain #Python #json  

```
---

     
 
all -  [ Finetune to avoid using tool descriptions in prompt template ](https://www.reddit.com/r/LocalLLaMA/comments/18qodse/finetune_to_avoid_using_tool_descriptions_in/) , 2023-12-28-0910
```
Hello everyone,

Still getting to grips with langchain, llms, huggingface, finetuning, dataset, etc. So, we have been su
ccessfully using langchain with various local llms from HF and conversationalagents that use tools. IT seems to work fai
rly well. THe problem we are running into is that the prompt template is getting rediculous in size and chomping down a 
lot of the available tokens. So we have like 10 tools with their corresponding descriptions. THe tools mainly use extern
al APIs to extract information.   


There are two main issues we are running into:  


1- We want the llm to understand
 that in order to fullfil some requests using a certain tool, it needs to extract information from another tool first. F
or example, one tool gets traffic data from a website on a server. Anthoner one get's a list of domains on a server and 
the other one get's a list of accounts that have domains that have sites (accounts->domains->sites).  


So when a user'
s query is something like 'please give me the traffic data for [mysite.com](https://mysite.com)' , langchain jumps and s
tarts using the traffic getting tool. But we need to pass along a domain and account so the receiving API knows where it
 needs to look.  


We are having trouble getting the LLM to understand that in order to use a tool, it needs to get inf
ormation before hand. We've tryed including in the descriptions which tools need to be used first before completing the 
tool usage, and no luck there. WE also tried explaining using natural language that 'If you need to use the traffic tool
, you need to ask the user for domain and account first and pass that to the input'.  


Or dataset looks like this:   



\#####

Customer: I need to check my site's [xxxx123.com](https://xxxx.com) traffic data  
Assistant: Sure, I see the 
domain is [xxxx123.com](https://xxxxx123.com) but which account is the domain located in?  
Customer: It's in the mystuf
f account.  
Assistant: Got it, here is the traffic information for [xxxx123.com](https://xxxx123.com) : bla , bla ,bla.
 Can I help you with anything else?  
\#####  


So now we are creating a dataset that has multi-turn conversations wher
e the assistant asks the user about the missing information and we are getting ready to train a llama2 7B , but this tas
k is still confusing for us, but we're still trying.   


But we're wondering if there is a easier way to make this work
. How can I setup langchain so the LLM knows what the heirarchy structure is, so if you are asking about a domain, you n
eed to know which account the domain is hosted in , or if it's about a site, which domain and account the site is in. A 
solution would be to create a tool that digs into each account and domain to find it, ... but that's an aweful amount of
 unnecessary energy.  


Any hints, tips would be inmensely appreciated.

&#x200B;
```
---

     
 
all -  [ How do I use openai api or something else to chat to my database? ](https://www.reddit.com/r/OpenAI/comments/18qlkf1/how_do_i_use_openai_api_or_something_else_to_chat/) , 2023-12-28-0910
```
It feels familiar to Chat with your documents but I am completely lost where to start. I am moderately experienced dev. 
I have a database of orders. I want to build a feature in the app that can allow users to ask questions like

- How was 
my sale last week or this week?
- How many of XYZ got sold?
- What's my lowest sold product?


I've looked into LangChai
n and LlamaIndex, both makes sense if your documents is just text. But in my case I've nested json object. I could clean
 it to simple key value pair but I will be loosing a lot of data with it. Such as I won't be able to ask which items wer
e bought together the most.

If anyone have built something similiar or know how to do it, I will really appreciate the 
help. I am kinda lost, can't find any way to do it.

Or Am i expecting too much from the AI?
```
---

     
 
all -  [ How to use llava-v1.5-13b-Q5_K_M.gguf with python ](https://www.reddit.com/r/LocalLLaMA/comments/18qleak/how_to_use_llavav1513bq5_k_mgguf_with_python/) , 2023-12-28-0910
```
So i have this LLaVa GGUF model and i want to run with python locally , i managed to use with LM Studio but now i need t
o run it in isolation with a python file   


So is there a code where i can load the model within it and use as a norma
l python code?  


Currently i can use LLaMa 7b without vision such like that with help of LangChain
```
---

     
 
all -  [ MongoDB Agent ](https://www.reddit.com/r/LangChain/comments/18qjcxc/mongodb_agent/) , 2023-12-28-0910
```
Hi everyone,I created a basic tools for interacting with mongodb using React agent.

[generated aggregation pipeline sui
table for pymongo](https://preview.redd.it/q04t7n0p6g8c1.png?width=1286&format=png&auto=webp&s=0f02e9226b77e9a67fc956718
ffbc92826972860)

the agent currently has two tools : detect aggregation, execute aggregationthe goal is to convert a na
tural language query to an aggregation pipeline when executed it would get the desired answer.currently the first tool w
orks perfectly, however the agent fails to execute the aggregation using pymongo.this is the output when it calls the ex
ecution tool:**ValueError: An output parsing error occurred. In order to pass this error back to the agent and have it t
ry again, pass \`handle\_parsing\_errors=True\` to the AgentExecutor. This is the error: Could not parse LLM output: {'a
ction': 'Execute mongodb aggregation pipeline tool','action\_input': \[{'$match': {'overall\_rating': {'$gte': 4}}}, {'$
count': 'satisfied\_customers'}\]}**

what could be the issue?

&#x200B;
```
---

     
 
all -  [ applied to over 100 companies on linkedin but no replies need suggestion ](https://www.reddit.com/r/developersIndia/comments/18qcw0m/applied_to_over_100_companies_on_linkedin_but_no/) , 2023-12-28-0910
```
completed btech in ece this july. started looking for jobs for software development role since november on linkedin, by 
now i have applied to over 100 jobs maybe 200, yet not even a reply. 

I have no connection in this field to even discus
s about such things. I thought by this time i will get some job and find a mentor, build my own community and start lear
ning and building better projects and ofcourse make money in the process.

But now i am stressed out and completely demo
tivated. 

plese do check my resume and just tell me honestly where i am going wrong or do i just need to quit engineeri
ng for good. 

https://preview.redd.it/9cdjmg0hud8c1.png?width=781&format=png&auto=webp&s=a3e66d9ef735741309590c44813b44
492a992006
```
---

     
 
all -  [ Based on your experience what is the smallest and optimal local model for RAG? ](https://www.reddit.com/r/LocalLLaMA/comments/18q9xva/based_on_your_experience_what_is_the_smallest_and/) , 2023-12-28-0910
```
I’m trying to set up RAG using langchain for company’s knowledge database and struggling to find optimal model / server 
solution, so any personal experience would be appreciated!
```
---

     
 
all -  [ Is there an equivalent of ChatGPT 'Plugins' for local LLMs Web UIs? Like Code Interpreter, Plot Gene ](https://www.reddit.com/r/LocalLLaMA/comments/18q8z2r/is_there_an_equivalent_of_chatgpt_plugins_for/) , 2023-12-28-0910
```
(title)
```
---

     
 
all -  [ Looking for Project Ideas ](https://www.reddit.com/r/LocalLLaMA/comments/18q3y1p/looking_for_project_ideas/) , 2023-12-28-0910
```
Background: Currently working as a Data Scientist at a tech company! I am actively looking for some very interesting pro
ject ideas, preferably, as I am trying to get some work done in GenAI.

I have extensively used Azure OpenAI Services an
d Langchain in my projects but I am looking to work with some open-source LLMs directly or create some kind of framework
 or libraries for such LLM applications.

 I wanted to ask the community here to suggest me some interesting project ide
as or pin-point any missing pieces in the LLM-dev puzzle in the form of libraries or frameworks that I could work on.

P
.s. : I am also open for collaborations, so DM if you wanna connect ;) 
```
---

     
 
all -  [ AWS Lambda Layer for Python Not Working ](https://www.reddit.com/r/aws/comments/18q1b1v/aws_lambda_layer_for_python_not_working/) , 2023-12-28-0910
```
Hi,

can anyone help me figure this out?

My goal is to create a lambda function that uses Langchain with VertexAI. For 
this, I've created a zip file with the Python packages. The method used was by creating a temp Docker image from amazonl
inux in which I'm installing Python3.8, PIP and a virtualenv.

Langchain works, but when I try to use VertexAI I get an 
error.

Here's the code:

    from langchain.llms import VertexAI
    llm = VertexAI(model\_name='gemini-pro',credential
s=credentials)

and the error:

      'errorMessage': 'Please, install or upgrade the google-cloud-aiplatform library: p
ip install google-cloud-aiplatform>=1.38.0',
    
      'errorType': 'ImportError',
    
      'stackTrace': \[
    
   
 '  File \\'/var/task/lambda\_function.py\\', line 12, in lambda\_handler\\n    llm = VertexAI(model\_name=\\'gemini-pro
\\',credentials=credentials)\\n',
    
    '  File \\'/opt/python/langchain\_core/load/serializable.py\\', line 107, in 
\_\_init\_\_\\n    super().\_\_init\_\_(\*\*kwargs)\\n',
    
    '  File \\'/opt/python/pydantic/v1/main.py\\', line 33
9, in \_\_init\_\_\\n    values, fields\_set, validation\_error = validate\_model(\_\_pydantic\_self\_\_.\_\_class\_\_, 
data)\\n',
    
    '  File \\'/opt/python/pydantic/v1/main.py\\', line 1102, in validate\_model\\n    values = validato
r(cls\_, values)\\n',
    
    '  File \\'/opt/python/langchain\_community/llms/vertexai.py\\', line 226, in validate\_e
nvironment\\n    cls.\_try\_init\_vertexai(values)\\n',
    
    '  File \\'/opt/python/langchain\_community/llms/vertex
ai.py\\', line 185, in \_try\_init\_vertexai\\n    init\_vertexai(\*\*params)\\n',
    
    '  File \\'/opt/python/langc
hain\_community/utilities/vertexai.py\\', line 75, in init\_vertexai\\n    raise\_vertex\_import\_error()\\n',
    
    
'  File \\'/opt/python/langchain\_community/utilities/vertexai.py\\', line 49, in raise\_vertex\_import\_error\\n    rai
se ImportError(\\n'
    
      \]


I've tried to cut dig into this by cutting down the code and it seems only using thi
s:

    from google.cloud import aiplatform

generates an error like

{
  'errorMessage': 'Unable to import module 'lamb
da_function': No module named 'google.protobuf'',
  'errorType': 'Runtime.ImportModuleError',
  'stackTrace': []
}



Ne
edless to say that the zip file uploaded contains:
langchain
google
protobuf
google-cloud-aiplatform
google-cloud-api-ke
ys

What am I missing here?

thanks in advance,
John


***UPDATE:***

thanks for the replies, I fixed the problem!

I di
d not realize that when you do pip install into a virtualenv you get both /lib and /lib64 folders. When I built the zip,
 I only copied the content from /lib. Adding the content of /lib64 too fixed the problem
```
---

     
 
all -  [ Best way to populate a pydantic model during an agent run ](https://www.reddit.com/r/LangChain/comments/18pzqkk/best_way_to_populate_a_pydantic_model_during_an/) , 2023-12-28-0910
```
I’m currently working on an Agent implementation that uses tools to update a pre-defined pydantic model which needs valu
es to be added/updated based on context retrieved by the agent. My problem, however, is that I cannot seem to figure out
 how to keep an instantiation of this pydantic model linked to the agent’s execution. 

Is it possible to access and upd
ate metadata in the AgentExecutor? 

Wondering if anyone has experience doing something similar to this?

My current imp
lementation is stateless, building the pydantic models during the output parsing step, however, this often results in ou
tput parsing errors. My thinking is also that this new implementation method will make evaluation simpler, since the qua
lity of the model would be tied to correct tool execution as opposed to completeness of the pydantic model. 

All though
ts/questions/comments appreciated!

Happy Holidays.
```
---

     
 
all -  [ Anyone can lend me a digital copy of Generative AI with LangChain ](https://www.reddit.com/r/LangChain/comments/18pt9fd/anyone_can_lend_me_a_digital_copy_of_generative/) , 2023-12-28-0910
```
Hi, I am from Pakistan, don't have access to a online payment system. 

Really want to learn langchain, was wondering if
 someone has a digital copy of this book. Can you share the copy, I promise never to put it up for download, will just k
eep it and learn
```
---

     
 
all -  [ Help integrating LLM in our application ](https://www.reddit.com/r/LocalLLaMA/comments/18psg1c/help_integrating_llm_in_our_application/) , 2023-12-28-0910
```
**Hi everyone,**

I'm working on integrating an LLM into an internal application built with ReactJS, NodeJS, and Postgre
SQL to create a chatbot that can answer questions about the app's data. I've run into some challenges and would apprecia
te your guidance.

**Here's my setup:**

* **Frontend:** ReactJS
* **Backend:** NodeJS
* **Database:** PostgreSQL
* **LL
M model:** Tried using Llama13b with LangChain for SQL query generation

**The goal:**

* Allow users to ask natural lan
guage questions about the app's data (e.g., 'How many cities are there?', 'Which cities have the most issues currently?'
)
* The chatbot should translate those questions into SQL queries, execute them against the PostgreSQL database, and ret
urn the results in a natural language format.

**The problem:**

* LangChain with Llama13b often generates unrealistic S
QL queries, referencing tables that don't exist or using incorrect column names.
* It also sometimes hallucinates inform
ation, producing responses that aren't grounded in the actual database content.

**Questions:**

1. **Better approach fo
r SQL query generation:** Is there a more reliable way to generate SQL queries from natural language using LLMs, specifi
cally for PostgreSQL? Are there better model/library combinations or techniques I should consider?
2. **Addressing hallu
cinations:** How can I mitigate the issue of hallucinations and ensure the chatbot's responses accurately reflect the da
tabase content?
3. **Alternative approaches:** If direct SQL query generation isn't the best approach, what other strate
gies could I explore to achieve the desired functionality?

**Please let me know if I need to change the approach comple
tely. Any advice or insights would be greatly appreciated!**

**Additional context:**

* I'm open to using different LLM
 models or libraries if they offer better results.
* I'm also interested in exploring techniques for improving the accur
acy of SQL query generation, such as fine-tuning or data augmentation.
* I'd be happy to provide more details about my s
etup and specific challenges if needed.
```
---

     
 
all -  [ Has anyone used LLMs to compile training data for LLMs? ](https://www.reddit.com/r/LangChain/comments/18prq9i/has_anyone_used_llms_to_compile_training_data_for/) , 2023-12-28-0910
```
With the ability of agents to search the web and use the data it finds in RAG, it seems that one could effectively make 
a research agent who's sole purpose is to find datasets for the LLM to consume:

Obstacles

* Navigating and choosing th
e data to make datasets from (research path if you will), maybe using ToT
* Data preparation, coming up with a standard 
to store the data chosen and creating an entry for the yaml
* Some way to test if the data is within the existing datase
t for the model in order to skip it or treat it with less weight. Could possibly be done using a carefully crafted compl
etion prompt and check the completion tokens against ground truth in the data being scrutinized

Do you think this would
 be helpful as a way to automatically generate non-synthetic datasets?
```
---

     
 
all -  [ SWE Unable to Get a Single Interview. Any Feedback is Appreciated! ](https://www.reddit.com/r/resumes/comments/18pj7tp/swe_unable_to_get_a_single_interview_any_feedback/) , 2023-12-28-0910
```
&#x200B;

https://preview.redd.it/8vrxxnzj058c1.png?width=623&format=png&auto=webp&s=026625190b1ff9dbeac85ac0b733e0eb6b8
3919a

Looking for primarily MLE and Data Science-y Software Engineering roles. I've been applying casually for a few mo
nths now but I have been unable to get a single interview out of \~75 applications. Both companies I've worked at are pr
etty large Fortune 500 companies and they're pretty recognizable in industry (non-tech) but only somewhat recognizable o
utside of it. I feel like some of the ownership on my resume may seem a little above my pay grade/experience level but i
t's how I've had to step up with some organizational changes saddling me with extra responsibility without any pay :(

&
#x200B;
```
---

     
 
all -  [ creating a vectordb from millions of documents ](https://www.reddit.com/r/LangChain/comments/18ph140/creating_a_vectordb_from_millions_of_documents/) , 2023-12-28-0910
```
Hey! I am trying to create a vector store using langchain and faiss for RAG(Retrieval-augmented generation) with about 6
 millions abstracts. is there a strategy to create this vector store efficiently? currently it takes very long time to c
reate it (can take up to 5 days)
```
---

     
 
all -  [ Inconsistent Table Querying ](https://www.reddit.com/r/LangChain/comments/18pfbu9/inconsistent_table_querying/) , 2023-12-28-0910
```
I am working on a project that uses Langchain in multiple places, I am getting inconsistent behavior, hoping someone can
 tell me what I am doing wrong here. (I am using a public bq dataset for this, so nothing proprietary in what I am posti
ng). I first use agent\_executor to generate a description of a table. I pass the table in as a variable. But the agent 
attempts to run the query return an error that the table is not found. In the same project I use db\_chain to allow natu
ral language to SQL querying of the table. In this case the table is found and a result is return. I have checked the SQ
L and results returned against the source data to confirm it is indeed querying the table. I am not sure why the table i
s found in one case but not the other

    # Working agent
    system_prompt = f' in {table_to_query}.You are a BigQuery
 expert. You are able quickly review the tables in a dataset and understand the contents of each table along with their 
relation. You will be asked a question for which you need to generate and execute a query. The table in the question is 
the main focus of the question, but you may also need to join to other tables, so keep them in mind as your create your 
plan. The other tables are {dataset_table_names}. The column names may not match 1:1 in the prompt, use your best reason
ing to select a column (for instance a user may ask for an account but in the table the column is account_name).Ensure t
hat the columns you use in the query exist in the table. As you answer the users question, consider what other columns m
ay be additive to their question and include those in your response'
    full_prompt = user_prompt + system_prompt
    

    
    if run_prompt:
       
        
        from langchain.utilities import SQLDatabase
        from langchain.llms
 import OpenAI
        from langchain_experimental.sql import SQLDatabaseChain
        
        db = SQLDatabase(engine)
 #, include_tables=prompt_tables)
        llm = OpenAI(temperature=.5, verbose=True)
    
        db_chain = SQLDatabase
Chain.from_llm(llm, verbose=True,db=db, use_query_checker=True, top_k=10)
    
        db_chain.run(full_prompt)
    
  
  else: 
        display('Waiting on you to run the query')
    
    
    > Entering new SQLDatabaseChain chain...
    W
hat was the most popular name in Utah in 2010 in bigquery-public-data.usa_names.usa_1910_2013.
    SQLQuery:SELECT
     
   name,
        SUM(number) AS total
    FROM
        `bigquery-public-data`.usa_names.usa_1910_2013
    WHERE
        
state = 'UT'
        AND year = 2010
    GROUP BY
        name
    ORDER BY
        total DESC
    LIMIT 10
    SQLResul
t: [('Olivia', 269), ('William', 264), ('Mason', 243), ('Jacob', 235), ('Ethan', 235), ('James', 231), ('Samuel', 227), 
('Isaac', 215), ('Abigail', 210), ('Logan', 206)]
    Answer:Olivia
    > Finished chain.
    

\--

    # Non Working
 
   from langchain.agents import create_sql_agent
    from langchain.agents.agent_toolkits import SQLDatabaseToolkit
    
from langchain.utilities import SQLDatabase
    from langchain.llms import OpenAI
    
    # from langchain.agents impor
t AgentExecutor
    from langchain.agents.agent_types import AgentType
    
    db = SQLDatabase(engine)
    
    agent_
executor = create_sql_agent(
        llm=OpenAI(temperature=0),
        toolkit=SQLDatabaseToolkit(db=db, llm=OpenAI(tem
perature=0)),
        verbose=True,
        agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    )
    
    agent_execu
tor.run(f'Describe the {table_to_query} table')
    
    
    > Entering new AgentExecutor chain...
    Action: sql_db_l
ist_tables
    Action Input: 
    Observation: 
    Thought: I should query the schema of the usa_names table.
    Actio
n: sql_db_schema
    Action Input: bigquery-public-data.usa_names.usa_1910_2013
    Observation: Error: table_names {'bi
gquery-public-data.usa_names.usa_1910_2013'} not found in database
    Thought: I should check the spelling of the table
 name.
    Action: sql_db_schema
    Action Input: bigquery-public-data.usa_names.usa_1910_2013
    Observation: Error: 
table_names {'bigquery-public-data.usa_names.usa_1910_2013'} not found in database

&#x200B;
```
---

     
 
all -  [ Llama ReAct ](https://www.reddit.com/r/LargeLanguageModels/comments/18pacr8/llama_react/) , 2023-12-28-0910
```
Has anyone be able to get llama to reliably work with langchain for calling multiple tools (Wikipedia arxiv etc) I’m usi
ng the 13b with a custom prompt and occasionally get good results however most outputs are parsing errors. 

Any suggest
ions?
```
---

     
 
all -  [ how to create a rag for all the chats/ conversations between A and everyone else wherein a bot can a ](https://www.reddit.com/r/LangChain/comments/18pa4gz/how_to_create_a_rag_for_all_the_chats/) , 2023-12-28-0910
```
I'm working on a project involving where I want to analyze conversations between two individuals, let's call them Person
 A and Person B. The primary function of this system is to enable a bot to answer questions about Person A's interests b
ased on past conversations between A and other individuals.

I am contemplating the best approach to use embedding model
s in this context. The challenge lies in conversational data, which is inherently different from structured documents. C
onversations typically lack distinct paragraphs or sections, making traditional chunking and embedding techniques less s
traightforward.

1. **Sentence-Level Embeddings**: Embedding each sentence individually to capture specific details. How
ever, this might limit the response to only the information contained in that particular sentence.  
2. **Conversation-L
evel Embeddings**: Creating embeddings for entire conversations. While this could capture the overall context, it might 
not be precise for detailed queries.
3. **Summarization Before Embedding**: Generating a summarized version of the conve
rsations and then embedding these summaries. I'm curious about the effectiveness and potential loss of detail with this 
method.

My questions for the community are:

* What are the recommended practices for embedding models in this kind of 
RAG system, especially considering the conversational nature of the data?
* Are there any specific techniques or methodo
logies that you would suggest for this type of application, possibly something that has worked well in your experience?
```
---

     
 
all -  [ Any good documentation/tutorial/e-book on url tools in langchain? ](https://www.reddit.com/r/LangChain/comments/18p25me/any_good_documentationtutorialebook_on_url_tools/) , 2023-12-28-0910
```
Hi, I have been trying to use LangChain Selenium and other url loaders, but can't find good documentation for now. Any i
nformation source is welcome.
```
---

     
 
MachineLearning -  [ [D] github repositories for ai web search agents ](https://www.reddit.com/r/MachineLearning/comments/18dhtm4/d_github_repositories_for_ai_web_search_agents/) , 2023-12-28-0910
```
Do you know of any github repositories that either help with building a web search ai agent or that has a good one?

git
hub repositories that I saw so far but have not yet tried :

- langchain (the WebResearchRetriever and weblangchain for 
example (have not tried either) )
- autogpt
- gpt-researcher

[Edit: changed researchgpt to gpt-researcher]
```
---

     
 
MachineLearning -  [ [P] flex-prompt: a flexible prompt rendering engine that ensures you'll never exceed your LLM's cont ](https://www.reddit.com/r/MachineLearning/comments/18d581q/p_flexprompt_a_flexible_prompt_rendering_engine/) , 2023-12-28-0910
```
When working with LLMs, I frequently experience *token agony*.

[Error: This model's maximum context length is 4097 but 
you are trying to push in all of War and Peace, you imbecile](https://preview.redd.it/nldj0qva4s4c1.png?width=1348&forma
t=png&auto=webp&s=b16af79d83f329db1b77b32ed621f0138d7cc04d)

Perhaps you've experienced it too! The issue is particularl
y pronounced with retrieval augmented pipelines, since you have potentially quite a large set of documents which you cou
ld perhaps include in the prompt if only you knew how big it could be.

I got tired of hacking around this headache, so 
I wrote `flex-prompt` to address it. I wish I didn't have to. Perhaps someone can point me to a better solution! But I c
ouldn't find one, so alas, here it is.

`flex-prompt` provides a basic layout and component model to help you describe h
ow you want the pieces of your prompt to grow and shrink and a token-aware renderer which renders your prompt to fit you
r model's window.

[Github](https://github.com/queerviolet/flex-prompt), [Intro to flex prompt colab](https://colab.rese
arch.google.com/github/queerviolet/flex-prompt/blob/main/doc/intro_to_flex_prompt.ipynb)

# Quick examples

You can just
 `render(Flex(...))`, and flex prompt will fit the prompt into the context window, and tell you how many tokens are left
 over for the response:

    from flex_prompt import render, Flex, Expect
    rendered = render(
        Flex([
        
  'Given the text, answer the question.',
          '--Text--',
          WAR_AND_PEACE,
          '--End Text--',
     
     'Question: What's the title of this text?',
          'Answer:', Expect()
        ], join='\n'),
        model='tex
t-davinci-002')
    
    # rendered.output is the string to send to the model
    # rendered.max_response_tokens is how 
many tokens you can
    #   request in response without exceeding the model's context window
    print(rendered.output, 
rendered.max_response_tokens)

More typically, you'll want to define a prompt which takes parameters. To do this, you ca
n create a class (probably a dataclass) which derives `Flexed`:

    from flex_prompt import Flexed, Expect
    from dat
aclasses import dataclass
    
    @dataclass
    class Ask(Flexed):
      text: str
      question: str
      answer: s
tr | Expect = Expect()
      instruct: str = 'Given a text, answer the question.'
    
      flex_join = '\n' # yielded 
items will be joined by newlines
      def content(self, _ctx):
        if self.instruct:
          yield 'Given the tex
t, answer the question.'
          yield ''
        yield '-- Begin Text --'
        # note: we're using `Flex` here jus
t to attach a flex_weight
        # to the text, telling the renderer we'd like more space for the
        # text than a
nything else.
        yield Flex([self.text], flex_weight=2)
        yield '-- End Text --'
        yield 'Question: ', 
self.question
        yield 'Answer: ', self.answer

The renderer works much as you might expect. You can \`yield\` anyt
hing which you can pass to the top-level render function, including other components, creating a whole tree.

Note that 
the component above can be used to render both the actual prompt and examples. Examples simply have an `answer`. This is
 useful for experimenting with different ways of structuring a prompt while ensuring that all the examples we present to
 the LLM are in the same format.

# LangChain and Haystack Integrations

Flex prompt doesn't really care how you execute
 your prompt. For convenience, `render(model=)` does accept both LangChain and Haystack models:

    ask_tolstoy = Ask(t
ext=WAR_AND_PEACE, question='Who wrote this?')
    
    # Using LangChain
    from langchain.llms import OpenAI
    lc_l
lm = OpenAI()
    rendering = render(ask_tolstoy, model=lc_llm)
    print(lc_llm(rendering.output, max_tokens=rendering.
max_response_tokens))
    
    
    # Using Haystack
    from haystack.nodes import PromptModel
    
    hs_llm = Prompt
Model(model_name_or_path='text-davinci-002', api_key=os.environ['OPENAI_API_KEY'])
    rendering = render(ask_tolstoy, m
odel=hs_llm)
    print(hs_llm.invoke(rendering.output, max_tokens=rendering.max_response_tokens))
    

# Is it worth it
?

As models grow larger and larger context windows, I've asked myself whether this is worth it. Won't context sizes eve
ntually big enough to put in everything we might want without worry?

One response: 'everything I might want' is a very,
 very big set, plausibly bigger than any window size we're going to see soon.

Another: being able to do this kind of to
ken accounting is useful even if we don't completely fill context windows. For example, we might be able to augment our 
prompt with examples, documents, and tips. How much space should we allocate to each? The answer might well be model-dep
endent. How do we figure it out?

Flex prompt's output, a `Rendering` object, actually holds the entire component tree. 
You can look through the object to see how many tokens were allocated to each child. This is currently very manual, but 
it does provide the bedrock infrastructure to e.g. run tests to discover the optimal balance of augmented data for a giv
en prompt and model.

Additionally, the right admixture (and for that matter, the right *phrasing*) may well be model-de
pendent. Flex prompt currently provides only very limited model-specific rendering (you can look at [`ctx.target`](https
://ctx.target), but it doesn't tell you much), but there's no reason that can't be significantly improved. At the extrem
e limit is prompt *erasure*, where we fine-tune a model to require no or minimal instructions/examples for a given set o
f prompts. Flex prompt can enable transitions like this with no changes to the pipelines themselves: you'd still use the
 same prompt components, they'd just render differently if the target is a fine-tuned model vs. a generic one.

# Status
 & Future Work

Flex prompt is very much in early development. I would love to hear if and how people find it useful, an
d would love input and contributions!

Some things I'd like to tackle in the future:

* **Rendering message lists.** Fle
x prompt currently only renders strings, though it's set up to be able to render any type of output. Message histories b
asically grow without bound, so supporting this seems like a no-brainer.
* **Pagination**. If your rendering overflows (
as above, where we're trying to stuff *the entirety of war and peace* into a prompt), flex prompt will clip the offendin
g pieces to fit. But there's currently no way to get 'the next page'. But the `Rendering` actually retains enough inform
ation to do this! It would be great to be able to call `render(...).pages()` to get the sequence of prompts as we 'scrol
l' whatever has overflowed. This is medium-hanging fruit—a little tricky because we do have to descend the tree of rende
rings to find the exact one(s) which overflowed and then update only those.
* **Token accounting.** As mentioned above, 
you can currently grovel around in `Rendering` and look at the pieces of the prompt. This would be more useful if it wer
e a little easier, e.g. if you could use `rendering[Examples]` to find all the parts rendered by the `Examples` componen
t, or `rendering['advice']` to find all the parts which are tagged (somehow) as 'advice'. The use case here is prompt op
timization: discovering the optimal number or percentage of tokens to allot to each thing we might want to drop into the
 prompt.
* **More integrations.** Currently, flex prompt only supports OpenAI models. You can register your own target f
inders, but it would be great to have more support out of the box. This is mostly a matter of digging around and finding
 the tokenizers and window sizes for common models, and then writing the appropriate target finders. Contributions very 
welcome!
* **Model tuning.** As mentioned above, the rendering context could provide a mechanism for fetching model-spec
ific parameters. The basic idea is that `ctx[param]` will evaluate `param` against the context, and then we can define s
ome parameter types which load their model-specific values from *gestures vaguely* somewhere.

Thanks for reading!

* [F
lex prompt Github](https://github.com/queerviolet/flex-prompt)
* [Intro to flex prompt colab](https://colab.research.goo
gle.com/github/queerviolet/flex-prompt/blob/main/doc/intro_to_flex_prompt.ipynb)
* [My website](https://ashi.io). *shame
less plug: I have a lot of engineering experience and a bit of machine learning experience and* [*I am currently looking
 for a job*](https://ashi.io/resume.pdf)
```
---

     
 
MachineLearning -  [ [D] Working on RAG? You should be evaluating its performance and we've built a way to do that. ](https://www.reddit.com/r/MachineLearning/comments/18ciet5/d_working_on_rag_you_should_be_evaluating_its/) , 2023-12-28-0910
```
Check out our new open-source tool, Tonic Validate: [https://www.tonic.ai/validate](https://www.tonic.ai/validate)  


W
e've also been using the tool to evaluate different RAG tools out there. The latest post on LangChain vs Haystack is ava
ilable here:  [https://www.tonic.ai/blog/rag-evaluation-series-validating-the-rag-performance-of-langchain-vs-haystack](
https://www.tonic.ai/blog/rag-evaluation-series-validating-the-rag-performance-of-langchain-vs-haystack)

&#x200B;

Let 
us know what you think and if you're working on a RAG project, we'd love to hear about it! How are you measuring your RA
G system performance?
```
---

     
 
MachineLearning -  [ [R] LLMs for structured data? ](https://www.reddit.com/r/MachineLearning/comments/185ei6v/r_llms_for_structured_data/) , 2023-12-28-0910
```
I've been trying to work with structured data in language models, and it's proving to be quite challenging. I'm confiden
t that with Langchain, I should be able to solve the problem, but I'm not entirely sure which path to take among all the
 options the library offers.

My issue is as follows: I have data in the form of dictionaries regarding a series of prod
ucts, for example, laptops. The data looks like this:

{Identifier 1: X, Identifier 2: Y, Value name: Z}

(Several succe
ssive dictionaries like this.)

I want to use this series of dictionaries as context, then feed a different dictionary i
nto the Language Model, and have it tell me if the 'Value name' makes sense given Identifiers 1 and 2. An example would 
be Identifier 1: laptops, Identifier 2: brand, Value name: Lenovo. In this case, it should return affirmative since Leno
vo makes sense as a brand. However, if I input 'oranges,' it should return negative.

Any ideas on which library I could
 use to tackle this problem?
```
---

     
 
deeplearning -  [ Unlocking the Power of Language: How LangChain Transforms Data Analysis and More ](https://www.reddit.com/r/deeplearning/comments/18l788y/unlocking_the_power_of_language_how_langchain/) , 2023-12-28-0910
```
Language models have revolutionized natural language processing (NLP), yet they grapple with limitations that impede the
ir full potential. Enter LangChain, a pioneering framework that transcends these constraints, fostering innovative langu
age-based applications. To comprehend LangChain’s significance, we must first grasp the limitations plaguing large langu
age models (LLMs).

link: [https://medium.com/ai-advances/unlocking-the-power-of-language-how-langchain-transforms-data-
analysis-and-more-3c4f327d520d](https://medium.com/ai-advances/unlocking-the-power-of-language-how-langchain-transforms-
data-analysis-and-more-3c4f327d520d) 
```
---

     
 
deeplearning -  [ [D] Mastering Chain Composition with LangChain Expression Language (LCEL) ](https://www.reddit.com/r/deeplearning/comments/18i0wot/d_mastering_chain_composition_with_langchain/) , 2023-12-28-0910
```
In the intricate landscape of modern software development, orchestrating complex sequences of actions seamlessly poses a
 significant challenge. Enter LangChain Expression Language (LCEL), a groundbreaking declarative approach designed to re
volutionize the composition of chains within software architecture.

Link: [https://medium.com/ai-artistry/mastering-cha
in-composition-with-langchain-expression-language-lcel-2d5041fb0cbd](https://medium.com/ai-artistry/mastering-chain-comp
osition-with-langchain-expression-language-lcel-2d5041fb0cbd)  
```
---

     
 
deeplearning -  [ [D] Utilizing Multimodal LLM for Extracting Tables and Images LangChain+LlamaIndex’s Role in Semi-St ](https://www.reddit.com/r/deeplearning/comments/185vd56/d_utilizing_multimodal_llm_for_extracting_tables/) , 2023-12-28-0910
```
In the domain of document analysis, the convergence of text, tables, and images presents formidable challenges for conve
ntional RAG (Retrieval Augmented Generation) methodologies. This complexity is further compounded within semi-structured
 data, notably in the extraction of tables from PDFs. Enter LangChain, a pioneering tool adept at navigating these intri
cate landscapes. Augmenting its capabilities is LlamaIndex, integrating Multi-Modal Retrieval Augmented Generation (RAG)
 techniques. Together, LangChain and LlamaIndex stand poised to revolutionize the handling and extraction of diverse con
tent types, promising a breakthrough in unraveling insights from varied data formats.

Link in the comment
```
---

     
