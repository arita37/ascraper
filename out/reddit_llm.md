 
all -  [ Metadata and Embeddings ](https://www.reddit.com/r/LangChain/comments/182dt4n/metadata_and_embeddings/) , 2023-11-24-0909
```
When creating embeddings and storing them alongside their respective Metadata, I'm curious if the Metadata is factored i
nto the similarity search at all, or is Metadata just for helping with general searching?
```
---

     
 
all -  [ Processing entire PDF ](https://www.reddit.com/r/LangChain/comments/182bbum/processing_entire_pdf/) , 2023-11-24-0909
```
I'm looking to process an entire PDF document.  The document is mostly standard text and 6-20 paragraphs.  Some sections
 are larger than the token limits. I want to re-write or pull info from the PDF.  This would require me to use each chun
k of text from the PDF to extract the data I'm looking for.

At first I was thinking of using Langchain for a summarizat
ion chain but I'm not sure this is my correct path.

I do not really want to map\_reduce because the initial data is imp
ortant and I'm slightly fearful of losing data before processing to get extracted info.  The summarization chains don't 
really allow for custom prompts like 'give me all statistical data from this text' (or if it does, I missed it).

Now I 
am thinking of just chunking the PDF and using a straight chat to process each chunk and combine the results at the end.


Looking for some advice on how to tackle this and what approach you'd use? 

Thanks!

&#x200B;
```
---

     
 
all -  [ Web scraping&crawling agent ](https://www.reddit.com/r/LangChain/comments/18294cg/web_scrapingcrawling_agent/) , 2023-11-24-0909
```
Has anyone created a langchain and/or autogen web scraping and crawling agent that on given a key word or series of keyw
ords could scrape the web based on certain kpis. For example, I would say help me with Tesla information and choose 5-10
 kpis from a predefined list such as valuation, assets, liability, share price , number of cars sold by model etc ? And 
the agent should come up with both qualitative and quantitative information ?

It could scrape the web for news, blogs, 
news letters, tweets, sec fillings among others
```
---

     
 
all -  [ [Langchain] Microsoft Guidance & Langchain - Quoi, quand, pourquoi? ](https://www.reddit.com/r/redditenfrancais/comments/1827uj1/langchain_microsoft_guidance_langchain_quoi_quand/) , 2023-11-24-0909
```
Quelqu'un peut-il m'aider à comparer et à contraster les conseils et Langchain?


Qu'est-ce que le chevauchement?

À quo
i sert le mieux?

Peuvent-ils être utilisés en combinaison?

Traduit et reposté à partir de la publication https://www.r
eddit.com/140q9z3
```
---

     
 
all -  [ We are looking for new beta testers 👀 ](https://www.reddit.com/r/roastmystartup/comments/18271ap/we_are_looking_for_new_beta_testers/) , 2023-11-24-0909
```
Hi Guys!  
We're thrilled to introduce Knowlee, an AI assistant powered by cutting-edge technologies like GPT4, Pinecone
, and Langchain. Here's how Knowlee works in a nutshell:  
1️⃣ Feed Knowledge: Import documents, videos, social posts, n
ews, financial stats, or any content you need analyzed.  
2️⃣ Get Instant Insights: Knowlee processes your content and p
rovides instant, intelligent insights to help you make informed decisions.  
3️⃣ Content Creation: Leverage these insigh
ts to generate relevant and timely content, keeping you ahead of the curve.  
We're currently inviting enthusiasts to jo
in our beta testing program and contribute to shaping the future of Knowlee.  
Feel free to drop a comment or send a DM 
if you’re ready to explore the capabilities of Knowlee!
```
---

     
 
all -  [ We are looking for new beta testers ](https://www.reddit.com/r/indiebiz/comments/1826y8f/we_are_looking_for_new_beta_testers/) , 2023-11-24-0909
```
Hi All!  
I'm Simone from the Knowlee team, thrilled to introduce our ultimate AI assistant powered by top-notch technol
ogies like GPT4, Pinecone, and Langchain.   
Here’s a quick run-through of how Knowlee can revolutionize your workflow: 
 
1️⃣ Feed Knowledge: Import documents, videos, social posts, news, financial stats, or any content you need analyzed.  

2️⃣ Get Instant Insights: Knowlee processes your content and provides instant, intelligent insights to help you make in
formed decisions.  
3️⃣ Content Creation: Leverage these insights to generate relevant and timely content, keeping you a
head of the curve.  
We're currently inviting enthusiasts to join our beta testing program and contribute to shaping the
 future of Knowlee.  
Feel free to drop a comment or send a DM if you’re ready to explore the capabilities of Knowlee!
```
---

     
 
all -  [ Need help with making conda to get recognized in VS code ](https://www.reddit.com/r/learnpython/comments/1826wn2/need_help_with_making_conda_to_get_recognized_in/) , 2023-11-24-0909
```
Hi guys I'm pretty new to coding but trying to follow this tutorial to build something cool. Can someone help me to set 
up the conda env in vs code and langchain, please. https://www.youtube.com/watch?v=kXuHxI5ZcG0
```
---

     
 
all -  [ LLM-based metadata filtering support? ](https://www.reddit.com/r/LangChain/comments/1823ldc/llmbased_metadata_filtering_support/) , 2023-11-24-0909
```
I have a collection of records that are scraped from HTML tables and, consequently, have a natural 'type' and no overlap
 between them: *e.g.* sports, medicine, history, *etc.*

However, the embedding-based retrieval in my RAG QA application
 is pretty bad across types, likely due to the documents themselves being overly long for the embedding and being simila
r on average.  I would resort to splitting and chunking to shrink the documents, but the challenge is that an element at
 the very top or bottom of a document may have relevance to the complete opposite end; it benefits the LLM QA component 
to have that entire context to answer queries.

*Without reworking document ingestion, my solution is to classify the us
er's prompt into one of those metadata categories (sports, medicine, history) using a few-shot learning prompt.  Then, u
se that classification as a metadata filter in a retriever so only that type is in consideration for the embedding ANN l
ookup.*  **Is there a name for this kind of pattern?  And does anyone have other recommendations?  Obvious downsides (be
yond the need for a second LLM call)?**

**I understand how to implement this, but does LangChain have an existing class
 (or classes) best suited for this?**  
```
---

     
 
all -  [ spelling check using LLMs ](https://www.reddit.com/r/LangChain/comments/1822g53/spelling_check_using_llms/) , 2023-11-24-0909
```
Recently, I used Google Docs' spell check, which seems to use an outdated, small language model. Its suggestions made me
 realize that advanced models like GPT-4 and even 3.5 are superior. I'm considering using the API for spell checking by 
submitting text for error detection. However, without precise prompt engineering, the output can be suboptimal, and usin
g techniques like chain of thought can introduce fluff content or hallucinations. I'm curious if there's an existing lib
rary or method to streamline this, perhaps by having the model rewrite the text correctly in a json format and then comp
aring it to the original to highlight only the changes. Any advice or solutions would be greatly appreciated.

 
```
---

     
 
all -  [ How to make sql agent or SqlDatabaseChain ask the user to clarity when the query is ambiguous? ](https://www.reddit.com/r/LangChain/comments/1820ggk/how_to_make_sql_agent_or_sqldatabasechain_ask_the/) , 2023-11-24-0909
```
for example, a Table named product with only 4 columns, which is product\_id, product\_name, price, and manufacturer.

t
he product name is like 'iphone 4', 'iphone 5', 'iphone 6', ..., 'pixel 4', 'pixel 5', ....  


when a user ask 'what is
 the price of the product named iphone?' , both of agent or SqlDatabaseChain will generate   
an sql statement like:  



select price from product where product\_name = 'iphone'.  
which will return no results.  


what I want is, the agent
 could suggest that ' I did not find the product iphone, but found some similar names, do you mean iphone4, iphone5 ...'
  


Because sometimes the user could not remember the precise product name, if the agent could ask for clarification, t
he chatbot will be more user-friendly.  


It would be better if user ask ' what is the price of iphone 4',  the agent '
know' iphone4 is a product name, rather than manufacturer.   


thanks in advance.

  


&#x200B;
```
---

     
 
all -  [ rate my resume ](https://i.redd.it/3eeqa0vow22c1.jpg) , 2023-11-24-0909
```

```
---

     
 
all -  [ [Langchain] Faire une application Web? ](https://www.reddit.com/r/redditenfrancais/comments/181xwu2/langchain_faire_une_application_web/) , 2023-11-24-0909
```
J'ai donc une application Python assez bien fonctionnelle dans un cahier Jupyter que j'aimerais faire une application We
b. Ma seule expérience d'interface utilisateur est avec Rshiny. Quelqu'un peut-il me pointer dans le sens de la façon de
 commencer à me débrouiller? Demander Bing dit que Flask est un bon endroit pour commencer, mais je me demandais si quel
qu'un a d'autres recommandations.

Merci beaucoup

Traduit et reposté à partir de la publication https://www.reddit.com/
1490y5l
```
---

     
 
all -  [ [Langchain] L'agent exécuteur ne travaille pas avec GPT-3.5-turbo, seulement text-davinci-003? ](https://www.reddit.com/r/redditenfrancais/comments/181xr3y/langchain_lagent_exécuteur_ne_travaille_pas_avec/) , 2023-11-24-0909
```
Je veux utiliser GPT-3.5-Turbo pour mon application en raison du coût, mais chaque fois que je l'y passe à partir de Tex
t-Davinci-003, l'exécuteur de l'agent cesse d'appeler correctement les outils. Il écrase le nom de l'outil et la demande
 et ne parvient pas à appeler correctement l'outil. Il n'a pas le même problème lors de l'utilisation de Text-Davinci-00
3 ou GPT-4.

Est-ce quelque chose à propos des modèles d'achèvement vs de chat?

Traduit et reposté à partir de la publi
cation https://www.reddit.com/13uxo3k
```
---

     
 
all -  [ Why aren't LLM APIs stateful? Why are we wasting compute? ](https://www.reddit.com/r/LangChain/comments/181xapd/why_arent_llm_apis_stateful_why_are_we_wasting/) , 2023-11-24-0909
```
I have worked with LangChain a good bit now and one of the main benefits is that it makes LLM APIs stateful.

What I mea
n by 'stateful' is that the the hidden state of the transformer is preserved. This is, of course, done by LangChain by s
aving the entire chat history you've had so far, and resending that entire history to the LLM API every time a new input
 is sent to the LLM.

Now the question is - why aren't LLM APIs themselves stateful? It seems like a massive use of comp
ute to recompute every single input token every single time. Why doesn't OpenAI (and others) simply give me a session id
 and save the state of the LLM on their side, so I can just follow up with my latest input string (alongside the unique 
session id), as opposed to having to resend \*the entire conversation\* every single time I make an API call?

This woul
d drastically reduce latency, reduce the load on their servers, etc. I understand it's slightly more complicated and res
ource intense to do so, but is it really that hard? I'd pay way more per in/out token for a stateful API.

So why aren't
 they stateful? What am I missing?  


  
EDIT: Answered well by u/ninja790, u/SatoshiNotMe, and others below. Thanks al
l! Time for me to go read up on transformers work instead of just using them only, lol
```
---

     
 
all -  [ [Local Llama] Comment déployer / héberger l'application LLM personnalisée pour la production? ](https://www.reddit.com/r/redditenfrancais/comments/181x4km/local_llama_comment_déployer_héberger/) , 2023-11-24-0909
```
Disons donc que nous avons créé l'application à l'aide de Langchain et PineCone (pour les intégres). L'application utili
se AutoTokenzer, AutomodelforCausAllm, ConversationRevalChain pour les documents QA de base sur les documents et le modè
le X à partir de HuggingFace.


Pour l'instant, j'ai couru cela dans Google Colab, mais que se passe-t-il si je veux ren
dre cela accessible à public? Comment héberger ceci et où? Je sais qu'il y a une chose azur, mais c'est pour utiliser de
s trucs Openai. Je n'ai pas trouvé de bon guide ou quelque chose comme ça pour héberger ces applications LLM pour le pub
lic, donc pas localement.

Traduit et reposté à partir de la publication https://www.reddit.com/1689jfx
```
---

     
 
all -  [ [Local Llama] Modèle rapide pour Codellama? ](https://www.reddit.com/r/redditenfrancais/comments/181wxdh/local_llama_modèle_rapide_pour_codellama/) , 2023-11-24-0909
```
Quelqu'un n'a pas encore pu utiliser Codellama?
Avec Huggingface? Langchain?
Ou avec une ui?

Veuillez partager vos étap
es. Je le cherche mal. Merci

Traduit et reposté à partir de la publication https://www.reddit.com/161mupa
```
---

     
 
all -  [ _TextGenerationModel.predict got an unexpected keyword argument 'functions' ](https://www.reddit.com/r/LangChain/comments/181vyav/textgenerationmodelpredict_got_an_unexpected/) , 2023-11-24-0909
```
Hi everyone I'm doing a attribute/specification extraction from a given csv. I'm uploading the csv to gcp storage and th
en using vertexaiembeddings storing it in chromadb. 
Now i was trying to use extraction chain to extract the information
 based on the schema. Whenever i run chain I'm getting above error. I'm using llm= VertexAI(temperature=0).
Thanks in ad
vance for the guidance 
I'm open to any other method using langchain and gcp vertexai but the base condition i have is t
hat specifications/attributes like name, price,etc should be extracted from the data stored in a vector db
```
---

     
 
all -  [ Where do we store prompts? ](https://www.reddit.com/r/LangChain/comments/181ukbz/where_do_we_store_prompts/) , 2023-11-24-0909
```
Should we consider prompt texts as part of the codebase or does it make sense to look it from a file or db?
```
---

     
 
all -  [ Haystack > langchain ](https://github.com/jlonge4/local_llama) , 2023-11-24-0909
```
For everyone who has been asking how haystack is better, check it out for yourself here. Pipelines, multiple document ty
pe converters, multiple document stores, multiple retriever types. The list goes on.
```
---

     
 
all -  [ I am working on making a chatbot.Can someone who has good knowledge about Chatbots, RASA and Integra ](https://www.reddit.com/r/Chatbots/comments/181u3ka/i_am_working_on_making_a_chatbotcan_someone_who/) , 2023-11-24-0909
```
I am working on a project where I have to build a chatbot for a company. I have already made the RASA chatbot and in the
 actions.py file I am using Langchain and GPT to query the information from the data I have fed to my Agent.

Now thw ta
sk is to integrate this Chatbot with the website. I need to make a proper frontend and connect with my backend(already m
ade).

What tools I can use, how will I do, workflow.

I need someone to explain me all this.
```
---

     
 
all -  [ Tutorials and Notebooks Worth Trying..... ](https://www.reddit.com/r/machinelearningnews/comments/181otfx/tutorials_and_notebooks_worth_trying/) , 2023-11-24-0909
```
* Tutorial and Notebook: [Launch Open-Source Apps with LangChain](https://www.singlestore.com/spaces/launch-open-source-
apps-with-lang-chain/?utm_source=asif-razzaq&utm_medium=influencer&utm_campaign=deck-the-halls-with-dev-and-data&utm_con
tent=open-source-with-langchain&campaignid=701UJ0000012K2AYAU)
* Tutorial and Notebook: [‘How to Build LLM Apps that can
 See Hear Speak’](https://www.singlestore.com/spaces/how-to-build-llm-apps-that-can-see-hear-speak/?utm_source=asif-razz
aq&utm_medium=influencer&utm_campaign=deck-the-halls-with-dev-and-data&utm_content=hear-see-speak&campaignid=701UJ000001
2K2AYAU)
* Tutorial and Notebook: [Movie Recommendation](https://www.singlestore.com/spaces/movie-recommendation/?utm_so
urce=asif-razzaq&utm_medium=influencer&utm_campaign=deck-the-halls-with-dev-and-data&utm_content=movie-recommendation&ca
mpaignid=701UJ0000012K2AYAU)
* Tutorial and Notebook: [Working with Vector Data](https://www.singlestore.com/spaces/work
ing-with-vector-data/?utm_source=asif-razzaq&utm_medium=influencer&utm_campaign=deck-the-halls-with-dev-and-data&utm_con
tent=working-with-vector-data&campaignid=701UJ0000012K2AYAU)
* Tutorial and Notebook: [Semantic Search with OpenAI Embed
ding Creation](https://www.singlestore.com/spaces/semantic-search-with-open-ai-embedding-creation/?utm_source=asif-razza
q&utm_medium=influencer&utm_campaign=deck-the-halls-with-dev-and-data&utm_content=semantic-search-openai&campaignid=701U
J0000012K2AYAU)
* Tutorial and Notebook: [Kafka Pipelines and Query Tuning](https://www.singlestore.com/spaces/kafka-pip
elines-and-query-tuning/?utm_source=asif-razzaq&utm_medium=influencer&utm_campaign=deck-the-halls-with-dev-and-data&utm_
content=kafka-pipelines-query-tuning&campaignid=701UJ0000012K2AYAU)
* Tutorial and Notebook: [Semantic Search with OpenA
I QA](https://www.singlestore.com/spaces/semantic-search-with-open-ai-qa/?utm_source=asif-razzaq&utm_medium=influencer&u
tm_campaign=deck-the-halls-with-dev-and-data&utm_content=semantic-search-openai-qa&campaignid=701UJ0000012K2AYAU)
* Tuto
rial and Notebook: [Getting Started with DataFrames in SingleStoreDB](https://www.singlestore.com/spaces/getting-started
-with-data-frames-in-single-store-db/?utm_source=asif-razzaq&utm_medium=influencer&utm_campaign=deck-the-halls-with-dev-
and-data&utm_content=getting-started-with-dataframes&campaignid=701UJ0000012K2AYAU)
* Tutorial and Notebook: [‘Mongo Atl
as & SingleStore Kai’](https://www.singlestore.com/spaces/mongo-atlas-single-store-kai/?utm_source=asif-razzaq&utm_mediu
m=influencer&utm_campaign=deck-the-halls-with-dev-and-data&utm_content=mongo-kai&campaignid=701UJ0000012K2AYAU)
* Tutori
al and Notebook: [Image Matching with SQL](https://www.singlestore.com/spaces/image-matching-with-sql/?utm_source=asif-r
azzaq&utm_medium=influencer&utm_campaign=deck-the-halls-with-dev-and-data&utm_content=image-matching-with-sql&campaignid
=701UJ0000012K2AYAU)
* Tutorial and Notebook: [Resume Evaluator](https://www.singlestore.com/spaces/resume-evaluator/?ut
m_source=asif-razzaq&utm_medium=influencer&utm_campaign=deck-the-halls-with-dev-and-data&utm_content=resume-evaluator&ca
mpaignid=701UJ0000012K2AYAU)
```
---

     
 
all -  [ 👨‍🎓 Video Guide: Cold Outreach Personalization with AI 🤖 ](https://www.reddit.com/r/Latenode/comments/181l143/video_guide_cold_outreach_personalization_with_ai/) , 2023-11-24-0909
```
https://preview.redd.it/23wyukzj1z1c1.jpg?width=1280&format=pjpg&auto=webp&s=50a59f2e12cfab21c4d0f80332d0748b75dcbd9a

*
Improving marketing strategies is key to growing your business, and cold outreach is a particularly effective tactic for
 finding new partners*

Today, a Latenode expert will demonstrate a **simple method for creating thousands of personaliz
ed emails** in just a few clicks! You'll discover techniques for automatic data enrichment, email personalization, and a
s a bonus, you'll receive a **free scenario template for automation**. All of this in our latest video.

🔗 Watch now: [Y
ouTube](https://www.youtube.com/watch?v=usD3ajbKcGs)
```
---

     
 
all -  [ Looking for DE remote jobs ](https://www.reddit.com/r/dataengineering/comments/181iebj/looking_for_de_remote_jobs/) , 2023-11-24-0909
```
Hey everyone,

I am looking for remote data engineering jobs. I have 5 years of experience in systems/data migration to 
Google Cloud and I am certified too.

I tried searching remote jobs in the US on LinkedIn but no results.

Are there any
 specific good platforms to find remote jobs or is anyone looking to hire here

PS: I also have few months of experience
 on GenAI, LLMs, Langchain and RAG.
```
---

     
 
all -  [ [D] Made some promises. Time to learn how to conduct very large scale pdf doc analysis. ](https://www.reddit.com/r/MachineLearning/comments/181gzek/d_made_some_promises_time_to_learn_how_to_conduct/) , 2023-11-24-0909
```
I have about a half million pdfs I need to summarize. Very wide range of types: invoices, diagrams, contracts, emails, l
etters, pictures, schedules, notices, data sheets, manuals, more. 

Which is... woof. Something else. I've been trying f
or many hours now to figure out a service/combination thereof that can get me there, but I'm seriously struggling. The *
ideal* solution would be to throw the pdfs in and have it return a csv with dates and summaries, maybe parsed out email 
heading info.

I'm currently running these pdfs through Acrobat OCR now, which its own special hell.

I've tried myriad 
local and webhosted solutions. The BEST results in what is almost the perfect system for this I found on https://docalys
is.com/. Good text results, works in batches, BUT I can only upload a single document at a time. They have a service to 
do batch processing and so I'm waiting to hear from them now. I imagine at the scale I need it's expensive.

I also got 
this solution working: https://github.com/mayooear/gpt4-pdf-chatbot-langchain. Seemed solid, I was able to upload a thou
sand pdfs in a single go, but it would keep returning information from only 2-3 documents. Upload 5? Results for 2-3. Up
load a thousand? Results for 2-3. My uneducated guess is that it's hitting the OpenAI API token limit, but maybe not?

I
 know it's possible, just not whether it's feasible for an end user.
```
---

     
 
all -  [ Made some promises. Now I'm desperately trying to figure out how to conduct very large scale pdf doc ](https://www.reddit.com/r/learnmachinelearning/comments/181gxg0/made_some_promises_now_im_desperately_trying_to/) , 2023-11-24-0909
```
I have about a half million pdfs I need to summarize. Very wide range of types: invoices, diagrams, contracts, emails, l
etters, pictures, schedules, notices, data sheets, manuals, more. 

Which is... woof. Something else. I've been trying f
or many hours now to figure out a service/combination thereof that can get me there, but I'm seriously struggling. The *
ideal* solution would be to throw the pdfs in and have it return a csv with dates and summaries, maybe parsed out email 
heading info.

I'm currently running these pdfs through Acrobat OCR now, which its own special hell.

I've tried myriad 
local and webhosted solutions. The BEST results in what is almost the perfect system for this I found on https://docalys
is.com/. Good text results, works in batches, BUT I can only upload a single document at a time. They have a service to 
do batch processing and so I'm waiting to hear from them now. I imagine at the scale I need it's expensive.

I also got 
this solution working: https://github.com/mayooear/gpt4-pdf-chatbot-langchain. Seemed solid, I was able to upload a thou
sand pdfs in a single go, but it would keep returning information from only 2-3 documents. Upload 5? Results for 2-3. Up
load a thousand? Results for 2-3. My uneducated guess is that it's hitting the OpenAI API token limit, but maybe not?

I
 know it's possible, just not whether it's feasible for an end user. Does anyone know a solution to accomplish this?
```
---

     
 
all -  [ [Langchain] Façons d'injecter des métadonnées en morceaux de texte? ](https://www.reddit.com/r/redditenfrancais/comments/181gf7h/langchain_façons_dinjecter_des_métadonnées_en/) , 2023-11-24-0909
```
Salut, quelqu'un saurait quelle est la meilleure façon d'injecter des métadonnées en morceaux de texte en utilisant Lang
chain ou peut-être que l'indice LLAMA serait?

Pour mon cas d'utilisation, je veux charger dans un PDF et diviser le PDF
 en morceaux, je veux pouvoir injecter des métadonnées supplémentaires. Y a-t-il une classe à Langchain qui aide à cela?
 Sinon, quelle serait une bonne façon de faire cela? J'ai pensé à une façon quelque peu piratée de le faire en me conver
tissant en JSON, en ajoutant les champs de métadonnées, puis en utilisant le Jsonloader pour le recharger.

Toutes les i
dées ou suggestions seraient les plus appréciées et appréciées. Merci d'avance!

Traduit et reposté à partir de la publi
cation https://www.reddit.com/169uxea
```
---

     
 
all -  [ [Langchain] Puis-je obtenir un code invitation Langsmith ](https://www.reddit.com/r/redditenfrancais/comments/181fray/langchain_puisje_obtenir_un_code_invitation/) , 2023-11-24-0909
```
Les gars, je suis terriblement perdu dans les journaux de mon agent personnalisé et je dois essayer ce Langchain au moin
s pour voir à quel point la situation est mauvaise. Est-il possible de m'envoyer un code d'invitation? Été sur la liste 
d'attente depuis des lustres: /

Traduit et reposté à partir de la publication https://www.reddit.com/16l9npt
```
---

     
 
all -  [ [Langchain] Chat Frontend à utiliser pour mes chaînes ](https://www.reddit.com/r/redditenfrancais/comments/181eqnt/langchain_chat_frontend_à_utiliser_pour_mes/) , 2023-11-24-0909
```
J'ai joué autour d'un montant considérable avec différentes chaînes et agents, mais j'utilise toujours la coquille ou un
 cahier de jupyter pour interagir avec eux.

Je voudrais une belle application Web pour rendre mes chaînes plus accessib
les avec un navigateur. Y a-t-il un frontend Goto (backend incl. API) pour y parvenir sans y passer trop de temps?

Trad
uit et reposté à partir de la publication https://www.reddit.com/13jzkwy
```
---

     
 
all -  [ Open source prompt catalog ](https://www.reddit.com/r/LangChain/comments/181ef3t/open_source_prompt_catalog/) , 2023-11-24-0909
```
Looking for a web based tool for users to search try out, and contribute prompts. And LangChain based agents as well. Al
so allow them to comment, rate and provide suggestions to improve the prompt. Open source would be ideal. 

I know of th
e following that are all closed source.
```
---

     
 
all -  [ Types in LangChain TS ](https://www.reddit.com/r/LangChain/comments/181d776/types_in_langchain_ts/) , 2023-11-24-0909
```
I’m struggling with types in LangChain TS. The types of StructuredTool, AgentAction, parsing error handling in AgentExec
utor and StructuredChatOutputParser don't fit together, and it only typechecks kind of by accident at the moment. 

I op
ened 2 issues on github, but can’t get any reasonable discussion/ feedback going, hope this helps. 

* Issue 1 - [https:
//github.com/langchain-ai/langchainjs/issues/2710](https://github.com/langchain-ai/langchainjs/issues/2710) 
* Issue 2 -
 [https://github.com/langchain-ai/langchainjs/issues/2711](https://github.com/langchain-ai/langchainjs/issues/2711) 

fo
r background [https://www.octomind.dev/blog/on-type-safety-in-langchain-ts](https://www.octomind.dev/blog/on-type-safety
-in-langchain-ts) 
```
---

     
 
all -  [ Code error in flowise ](https://www.reddit.com/r/LangChain/comments/181bbme/code_error_in_flowise/) , 2023-11-24-0909
```
Hi, I'm new to flowise and experimenting with some templates. I'm getting this error when I run the flow

'output values
 have 1 keys, you must specify an output key or pass only 1 key as output'

What might be causing this and is there a wa
y to get the langchain code for this as a solution for that has been suggested on stack overflow.

Thanks in advance
```
---

     
 
all -  [ Creating pdf as output ](https://www.reddit.com/r/LangChain/comments/18193sw/creating_pdf_as_output/) , 2023-11-24-0909
```
Is it possible to create a formatted (boiler plate) pdf as output using Langchain calls to LLM.

 Assuming LLM output gi
ves me all the required fields

1) How can one format it correctly?
2) How can the output be written out as pdf?  

Any 
relevant sample code or suggestions might be of great help. Thanks
```
---

     
 
all -  [ How do I go about training an open source llm on a postgres database ](https://www.reddit.com/r/LocalLLaMA/comments/18190ds/how_do_i_go_about_training_an_open_source_llm_on/) , 2023-11-24-0909
```
Howdy,

I'm a backend developer, and management recently asked me to train an llm on our company data. I'm a bit over my
 head here, and I figured I'd ask for high level advice rather than continuing to go down google rabbit holes.

What I'v
e tried so far:

* I spun up some gpu instances on AWS. Couldn't get llama to work at all, except for using gpt4all, whi
ch wasn't very performant and does make a network call to a github page for a list of models.
* I tired following a goog
le cloud tutorial [here](https://cloud.google.com/blog/products/databases/using-pgvector-llms-and-langchain-with-google-
cloud-databases). This didn't work in their colab notebook, so I gave up on that since if their own documentation didn't
 work it didn't seem promising.

Any advice is appreciated!
```
---

     
 
all -  [ How to store/replay the path an AI agent has taken ](https://www.reddit.com/r/LangChain/comments/18178pg/how_to_storereplay_the_path_an_ai_agent_has_taken/) , 2023-11-24-0909
```
I am new to building AI agents (robotics background) and I was curious to learn about the most common workflows you guys
 use.

How do you store/replay the full path that the agent has been following? More precisely:

1. What sort of data do
 you collect?
2. Where do you store all your runs (if you store them)?
3. What metrics do you use for evaluating each ru
n? I've seen some interesting things from the OAI devday-- do you actually use them?
4. Is there a way to replay a run?
```
---

     
 
all -  [ [Langchain] Comment devrais-je sortir du texte à partir d'un manuel pour les meilleurs résultats d'i ](https://www.reddit.com/r/redditenfrancais/comments/18175bo/langchain_comment_devraisje_sortir_du_texte_à/) , 2023-11-24-0909
```
Je suppose que je dois suivre la structure naturelle du manuel et chasser mon texte par chapitre, section, paragraphe, e
tc. tout en conservant les métadonnées pertinentes. Le problème est que je ne sais pas comment faire ça lol.

Quelqu'un 
peut-il me dire une meilleure façon de sélectionner un manuel ou de me donner les directives de base afin que je puisse 
demander à chatgpt?

Traduit et reposté à partir de la publication https://www.reddit.com/15q5jzv
```
---

     
 
all -  [ [Langchain] Comment injecter un contexte toujours présent dans la conversation de conversationrie ](https://www.reddit.com/r/redditenfrancais/comments/18173hz/langchain_comment_injecter_un_contexte_toujours/) , 2023-11-24-0909
```
J'utilise ConfortationalSrievalChain pour les questions et réponses sur les documents. J'ai divisé le document principal
 en plus petits et les ai utilisés dans comme \ _Reriver ().

Il y a des informations importantes qui ne figurent pas da
ns le document de questions / réponses, mais c'est crucial pour chaque question à ce sujet. Je ne veux pas l'ajouter à l
a base de données vectorielle, car il pourrait ne pas être récupéré, en laissant le modèle sans contexte clé.

Existe-t-
il une meilleure façon de donner ces informations au modèle, en plus de l'ajouter à l'invite?

Traduit et reposté à part
ir de la publication https://www.reddit.com/16trvoe
```
---

     
 
all -  [ [Langchain] Chatbot utilisant des agents de Langchain et Llama 2 ](https://www.reddit.com/r/redditenfrancais/comments/1816x0o/langchain_chatbot_utilisant_des_agents_de/) , 2023-11-24-0909
```
Salut les gars, j'ai récemment construit un chatbot utilisant le modèle Langchian et Open AI LLM (GPT 3.5 16 K). Ce chat
bot réside sur des données tabulaires (nous avons utilisé Create \ _Pandas \ _DataFrame) pour interroger les données pou
r les utilisateurs. Mais notre organisation veut que nous utilisons le modèle LLM open source (LLAMA 2 70 B). Je voulais
 juste les suggestions Vérifiez 2 choses:


1) Quelqu'un a-t-il essayé LLAMA2 (GPU / CPU) avec des pandas Langchain / de
s agents conversationnels et voir si les résultats sont prometteurs ou non.

2) Quelles sont les exigences GPU pour exéc
uter LLAMA2 70 B, que je peux demander mon organisation?


Tia

Traduit et reposté à partir de la publication https://ww
w.reddit.com/16p2nas
```
---

     
 
all -  [ What embedding model do you guys use? ](https://www.reddit.com/r/LangChain/comments/1816mb5/what_embedding_model_do_you_guys_use/) , 2023-11-24-0909
```
I'm trying to test more embedding models and I'm wondering what does this community use... 

I know that it 'may vary de
pending on use case', so in that case please share model and related use case. 

Currently I'm using mostly bge-large-v1
.5 or instructor-xl... 

(intrested in both bi encoder and cross encoder)

Thanks im advance!!!
```
---

     
 
all -  [ Building our own Agent ](https://www.reddit.com/r/brokebing/comments/18160rr/building_our_own_agent/) , 2023-11-24-0909
```
Hi Visual Hackers!  


I have a deep respect for this community and the way their members manage to outsmart the machine
.   


I'm a software dev, and I'm currently developing a specialized agent that helps rephrase the prompts in a way tha
t bypasses the dog.  


In order to do this, I need to create a dataset of successful cases. I understand we don't want 
to make our techniques public  in order to avoid patching, so we would need to get in contact via private message if you
 would like to collaborate to the project.   


My strategy will be trying these in order:  
1- Try with few shot infere
nce (prompting)  
2- RAG the dataset  
3- Fine-tuning if we manage to get enough examples.  


There are several non-res
tricted generative models I could use to avoid the basic censorship, I already have a couple of models running on local 
like  nous-hermes-llama2-13b and  mistral-7b which have been trained with an uncensored dataset, that could fit our use 
case better. I also have a really uncensored one, but that one would definitely need fine-tuning, so I'll try with the o
thers 2 first.  


Long story short: you give an input like 'tits, war and drugs' and outputs a prompt that is most like
ly to confuse the dog. It does most of the heavy lifting, and leave us with a prompt that we could easily modify to adju
st it better.  


The final result, will be shared only among the people who participated, either as developer or provid
ing their prompts. I don't plan to profit on this, it is merely for research purposes, and of course for fun.  


Also, 
if there's any other dev around here I have an idea of also building incremental image generator using langchain, as I s
ometimes noticed the best way to avoid the dog is by building up a concept slowly, rather than using just one prompt.  



I'm open to ideas and discussions.
```
---

     
 
all -  [ FileNotFoundError: [Errno 2] No such file or directory: ‘UploadedFile’ ](https://www.reddit.com/r/StreamlitOfficial/comments/1815xyt/filenotfounderror_errno_2_no_such_file_or/) , 2023-11-24-0909
```
Hi, I’m creating an LLM Application which accepts user inputs such as JSON file upload, project id and dataset name to e
stablish bigquery connection. I have tried the following code given below and it works perfectly. It is a hard coded ver
sion where the user doesn’t upload or give any inputs. When i converted this to streamlit app where it accepts input JSO
N file, it gives me an error saying file not found. Full details on the error is given below. I would greatly appreciate
 it if someone could help me out on this.

&#x200B;

**Code snippet bigquery direct connection:**

    service_account_f
ile = 'bigquery_sample.json' #local directory path 
    project = 'xxxxx' 
    dataset = 'xxxx_xxxxx' 
    
    sqlalche
my_url = f'bigquery://{project}/{dataset}?credentials_path={service_account_file}' #connection

&#x200B;

**Code snippet
 for bigquery connection using streamlit by accepting inputs from user:**

    service_account_file = st.sidebar.file_up
loader('Upload BigQuery Service Account file') 
    project = st.sidebar.text_input('Enter Project ID:','xxxxx') 
    da
taset = st.sidebar.text_input('Enter Dataset Name:','xxxx_xxxxx') 
    
    sqlalchemy_url = f'bigquery://{project}/{dat
aset}?credentials_path={service_account_file}'

&#x200B;

**Error:**

    FileNotFoundError: [Errno 2] No such file or d
irectory: 'UploadedFile(file_id=\'7a217610-7090-4b3c-9e34-19f4555de9d5\', name=\'bigquery_sample.json\', type=\'applicat
ion/json\', size=2355, _file_urls=file_id: '7a217610-7090-4b3c-9e34-19f4555de9d5''

&#x200B;

**Traceback:**

    File '
C:\Users\alens\Downloads\langchain_text2sql_1\venv\lib\site-packages\streamlit\runtime\scriptrunner\script_runner.py', l
ine 541, in _run_script
        exec(code, module.__dict__)
    File 'C:\Users\alens\Downloads\langchain_text2sql_1\app3
.py', line 93, in <module>
        query_engine = initialize_llm_predictor()
    File 'C:\Users\alens\Downloads\langchai
n_text2sql_1\app3.py', line 67, in initialize_llm_predictor
        db = SQLDatabase.from_uri(sqlalchemy_url)
    File '
C:\Users\alens\Downloads\langchain_text2sql_1\venv\lib\site-packages\langchain\utilities\sql_database.py', line 125, in 
from_uri
        return cls(create_engine(database_uri, **_engine_args), **kwargs)
    File '<string>', line 2, in creat
e_engine
    File 'C:\Users\alens\Downloads\langchain_text2sql_1\venv\lib\site-packages\sqlalchemy\util\deprecations.py'
, line 375, in warned
        return fn(*args, **kwargs)
    File 'C:\Users\alens\Downloads\langchain_text2sql_1\venv\li
b\site-packages\sqlalchemy\engine\create.py', line 560, in create_engine
        (cargs, cparams) = dialect.create_conne
ct_args(u)
    File 'C:\Users\alens\Downloads\langchain_text2sql_1\venv\lib\site-packages\sqlalchemy_bigquery\base.py', 
line 842, in create_connect_args
        client = _helpers.create_bigquery_client(
    File 'C:\Users\alens\Downloads\la
ngchain_text2sql_1\venv\lib\site-packages\sqlalchemy_bigquery\_helpers.py', line 46, in create_bigquery_client
        c
redentials = service_account.Credentials.from_service_account_file(
    File 'C:\Users\alens\Downloads\langchain_text2sq
l_1\venv\lib\site-packages\google\oauth2\service_account.py', line 260, in from_service_account_file
        info, signe
r = _service_account_info.from_filename(
    File 'C:\Users\alens\Downloads\langchain_text2sql_1\venv\lib\site-packages\
google\auth\_service_account_info.py', line 78, in from_filename
        with io.open(filename, 'r', encoding='utf-8') a
s json_file:

&#x200B;
```
---

     
 
all -  [ Does Chromadb let us use score_threshold? ](https://www.reddit.com/r/LangChain/comments/18120qp/does_chromadb_let_us_use_score_threshold/) , 2023-11-24-0909
```
Using Chromadb with langchain. Per Langchain documentation, below is valid. See link given.

retriever = db.as\_retrieve
r(

search\_type='similarity\_score\_threshold',

search\_kwargs={'score\_threshold': 0.9}

)

See examples from this li
nk:

[https://api.python.langchain.com/en/latest/vectorstores/langchain.vectorstores.chroma.Chroma.html#langchain.vector
stores.chroma.Chroma.asimilarity\_search\_with\_relevance\_scores](https://api.python.langchain.com/en/latest/vectorstor
es/langchain.vectorstores.chroma.Chroma.html#langchain.vectorstores.chroma.Chroma.asimilarity_search_with_relevance_scor
es)

&#x200B;

 *# Only retrieve documents that have a relevance score* *# Above a certain threshold* docsearch.as\_retr
iever( search\_type='similarity\_score\_threshold', search\_kwargs={'score\_threshold': 0.8} ) 

However the score\_thre
shold doesn't return any documents even for the lowest threshold. The db does contain documents relevant to my query.

I
 also did go through ChromaDB code, but I fail to see any option to include this threshold. 

Doesn't chromadb allow us 
to search results based on a threshold?

&#x200B;

&#x200B;

&#x200B;
```
---

     
 
all -  [ Does anyone use pgvector or is it too slow compared to everything else? ](https://www.reddit.com/r/LangChain/comments/1811x1y/does_anyone_use_pgvector_or_is_it_too_slow/) , 2023-11-24-0909
```
Is pgVector just something for hobbyists or can it be used in prod with decent speed?
```
---

     
 
all -  [ Consume API with langchain ](https://www.reddit.com/r/LangChain/comments/180vqss/consume_api_with_langchain/) , 2023-11-24-0909
```
Hi guys, with langchain is it possible to consume an api with post method where I have to send a json in the body, does 
anyone have an example?

&#x200B;
```
---

     
 
all -  [ Keep certain text together when splitting? ](https://www.reddit.com/r/LangChain/comments/180vkvs/keep_certain_text_together_when_splitting/) , 2023-11-24-0909
```
Building a RAG implementation, and I have some pieces of text that need to be contained in the same document when sendin
g to the vector store. Specifically, I have tables stripped from PDFs, and some corresponding descriptions that I had an
 LLM generate. 

Is there a way to specify certain start and end tokens to make sure the tables and corresponding descri
ptions aren't divided across documents? Or maybe there's a way to create a custom text splitter?
```
---

     
 
all -  [ Flush AI - Langchain but for Stable Diffusion Workflows ](https://www.reddit.com/r/SideProject/comments/180ufn1/flush_ai_langchain_but_for_stable_diffusion/) , 2023-11-24-0909
```
[Flush](https://flushai.cloud/) simplifies the process of building, fine tuning, and managing stable diffusion models. Y
ou can do the following on Flush:

* Upload any Civit AI Checkpoint (under 4GB)
* Finetune a model using Dreambooth
* Up
scale images with Real-Esrgan
* Use LLM's to enhance your prompt and build custom workflows
* Generate images with any m
odel on our platform, including base models like Realistic Vision, SDXL, Absolute Reality, and more. You can generate im
ages with text-to-image or image-to-image.
* (Coming soon!): Safetensors upload, download your finetuned models, and fin
etune on a wider variety of base models like Absolute Reality/Realistic Vision.

We consider ourselves 'langchain' but f
or stable diffusion workflows, because with our SDK (which we will be making open source), developers can build ANY cust
om workflow chaining together Prompt Templates, upscalers, any image generation model hosted on our platform (SDXL/any C
ivit model/any Finetuned model), LLM's like GPT-4, and deploy these workflows in their applications. We also have many i
ntegrations with prompt databases/API's like SerpAPI, Pixabay, Pexels, etc. And we are also building data integrations, 
so you can load data from sources like PDF's, Dropbox, Google Drive, etc. Check us at [https://www.flushai.cloud/](https
://www.flushai.cloud/).

We are building and growing fast and I’d encourage you guys to stay tuned and join our [Discord
](https://discord.com/invite/fzdHj9DeuC) server and DM me about any criticism/feedback/bugs you face.

&#x200B;

https:/
/preview.redd.it/7dj7itp99s1c1.png?width=2000&format=png&auto=webp&s=918d4b469fd4efa98d2a838990759de6e08deab6

https://p
review.redd.it/ob6jwiha9s1c1.png?width=960&format=png&auto=webp&s=da2f8a5aa12d0e123e16763f162e50b6e9daaf5e

https://prev
iew.redd.it/fjr66t6b9s1c1.png?width=2000&format=png&auto=webp&s=eaa6d11e6b93867338cc84051d5cc859f9bf8c5a
```
---

     
 
all -  [ Langchain but for Stable Diffusion Workflows ](https://www.reddit.com/r/sdforall/comments/180tme3/langchain_but_for_stable_diffusion_workflows/) , 2023-11-24-0909
```
[Flush](https://flushai.cloud/) simplifies the process of building, fine tuning, and managing stable diffusion models. Y
ou can do the following on Flush:

* Upload any Civit AI Checkpoint (under 4GB)
* Finetune a model using Dreambooth
* Up
scale images with Real-Esrgan
* Use LLM's to enhance your prompt and build custom workflows
* Generate images with any m
odel on our platform, including base models like Realistic Vision, SDXL, Absolute Reality, and more. You can generate im
ages with text-to-image or image-to-image.
* (Coming soon!): Safetensors upload, download your finetuned models, and fin
etune on a wider variety of base models like Absolute Reality/Realistic Vision. 

We consider ourselves 'langchain' but 
for stable diffusion workflows, because with our SDK (which we will be making open source), developers can build ANY cus
tom workflow chaining together Prompt Templates, upscalers, any image generation model hosted on our platform (SDXL/any 
Civit model/any Finetuned model), LLM's like GPT-4, and deploy these workflows in their applications. We also have many 
integrations with prompt databases/API's like SerpAPI, Pixabay, Pexels, etc. And we are also building data integrations,
 so you can load data from sources like PDF's, Dropbox, Google Drive, etc. Check us at [https://www.flushai.cloud/](http
s://www.flushai.cloud/).

We are building and growing fast and I’d encourage you guys to stay tuned and join our [Discor
d](https://discord.com/invite/fzdHj9DeuC) server and DM me about any criticism/feedback/bugs you face.

https://preview.
redd.it/1rbk0vnh1s1c1.png?width=2000&format=png&auto=webp&s=6dc73d7facd37477b72be4b5c39bbda0282901b1

https://preview.re
dd.it/4c02bqei1s1c1.png?width=960&format=png&auto=webp&s=2fd0ad78b3d843c5ca40395d48168a035de615c7

https://preview.redd.
it/tcl7hu3j1s1c1.png?width=2000&format=png&auto=webp&s=cf75d73c776aa08d24ebcd9d7c5ec2f6f1082dc7
```
---

     
 
all -  [ Langchain but for Stable Diffusion Workflows ](https://www.reddit.com/r/StableDiffusionInfo/comments/180tkrm/langchain_but_for_stable_diffusion_workflows/) , 2023-11-24-0909
```
[Flush](https://flushai.cloud/) simplifies the process of building, fine tuning, and managing stable diffusion models. Y
ou can do the following on Flush:

* Upload any Civit AI Checkpoint (under 4GB)
* Finetune a model using Dreambooth
* Up
scale images with Real-Esrgan
* Use LLM's to enhance your prompt and build custom workflows
* Generate images with any m
odel on our platform, including base models like Realistic Vision, SDXL, Absolute Reality, and more. You can generate im
ages with text-to-image or image-to-image.
* (Coming soon!): Safetensors upload, download your finetuned models, and fin
etune on a wider variety of base models like Absolute Reality/Realistic Vision. 

We consider ourselves 'langchain' but 
for stable diffusion workflows, because with our SDK (which we will be making open source), developers can build ANY cus
tom workflow chaining together Prompt Templates, upscalers, any image generation model hosted on our platform (SDXL/any 
Civit model/any Finetuned model), LLM's like GPT-4, and deploy these workflows in their applications. We also have many 
integrations with prompt databases/API's like SerpAPI, Pixabay, Pexels, etc. And we are also building data integrations,
 so you can load data from sources like PDF's, Dropbox, Google Drive, etc. Check us at [https://www.flushai.cloud/](http
s://www.flushai.cloud/).

We are building and growing fast and I’d encourage you guys to stay tuned and join our [Discor
d](https://discord.com/invite/fzdHj9DeuC) server and DM me about any criticism/feedback/bugs you face.

https://preview.
redd.it/fj181v5k0s1c1.png?width=2000&format=png&auto=webp&s=251ff081980160d375d4bfc435d451c087943113

https://preview.re
dd.it/11g8ml2l0s1c1.png?width=960&format=png&auto=webp&s=865a908e6cd9bc7c0a99529e7b3e56c03b010a12

https://preview.redd.
it/zqlvaiom0s1c1.png?width=2000&format=png&auto=webp&s=4bf66602e5afa16fd973b4bcd7165b0447aa1034
```
---

     
 
MachineLearning -  [ Google PaLM Error [D] ](https://www.reddit.com/r/MachineLearning/comments/17y7arb/google_palm_error_d/) , 2023-11-24-0909
```
Google PaLM Error

Using LangChain and Google PaLM, in sequential chain concept getting following error,

ChatGooglePalm
Error: ChatResponse must have atleast one candidate

Please help!
```
---

     
 
MachineLearning -  [ [D] System Design question for LangChain ](https://www.reddit.com/r/MachineLearning/comments/17x545j/d_system_design_question_for_langchain/) , 2023-11-24-0909
```
Hi

Just to prepare the system design question for LangChain. Is there a resource that can walk me through the high leve
l pipeline? I know there are a bunch of resources that dive into detail implementation. But that's not I want. I want hi
gh level conceptual walk-through. 
```
---

     
 
MachineLearning -  [ [P] GPT vs. StarCraft ](https://www.reddit.com/r/MachineLearning/comments/17ro6el/p_gpt_vs_starcraft/) , 2023-11-24-0909
```
This is the first in a series of webcasts covering the development and experimentation of using GPT algorithms, LangChai
n and Python to control the high-level strategy of a StarCraft II bot. I’ll be running through the basics of the impleme
ntation, discussing the use of prompts and prompt engineering, and demonstrating the implementation in action.

[https:/
/youtu.be/E3Sj2L6ZnXA](https://youtu.be/E3Sj2L6ZnXA)
```
---

     
 
MachineLearning -  [ [D] Is this close enough to be usable? Need your inputs: Automated RAG testing tool. AI Data Pipelin ](https://www.reddit.com/r/MachineLearning/comments/17kkbm0/d_is_this_close_enough_to_be_usable_need_your/) , 2023-11-24-0909
```
Hey there, Redditors! 

I'm back with the latest installment on creating dependable AI data pipelines for real-world pro
duction. 

If you've been following along, you know I'm on a mission to move beyond the '[thin OpenAI wrapper](https://t
opoteretes.notion.site/Going-beyond-Langchain-Weaviate-and-towards-a-production-ready-modern-data-platform-7351d77a1eba4
0aab4394c24bef3a278?pvs=4)' trend and tackle the challenges of building robust data pipelines. 

With 18 months of hands
-on experience and many user interviews, I realized that with the probabilistic nature of systems, we need better\_testi
ng.gpt:

  
**1. As you build you should test**  
The world of AI is a fast-moving one, and we've realized that just wor
king on systems is not an optimal design choice. By the time your product ships, it might already be using outdated tech
nology. So, what's the lesson here? Embrace change, test along, but be prepared to switch pace.  
**2. No Best Practices
 Yet for RAGs**  
In this rapidly evolving landscape, there are no established best practices. You'll need to make educa
ted bets on tools and processes, knowing that things will change. With the RAG testing tool, I tried allowing for testin
g many potential parameter combinations **automatically**  
**3. Testing Frameworks**  
If your generative AI product do
esn't have users giving feedback, then you are building in isolation. I used [Deepeval](https://github.com/confident-ai/
deepeval) to generate test sets, and they will soon support synthetic test set generation  
**4. Infographics only go so
 far**  
AI researchers and data scientists, while brilliant, end up in a loop of pursuing Twitter promotional content. 
New ways are promoted via new content pieces, but ideally, we need something above simple tracing but less than full-fle
dged analytics. To do this, I stored test outputs in Postgres and created a Superset instance to visualize the results  

**5. Bridging the Gap between VectorDBs**  
There's a noticeable number of Vector DBs. To ensure smooth product develop
ment, we need to be able to switch to best best-performing one, especially since user interviews signal that they might 
start deteriorating after loading 50 million rows

&#x200B;

Github repo is [here](https://topoteretes.notion.site/Going
-beyond-Langchain-Weaviate-Level-3-towards-production-e62946c272bf412584b12fbbf92d35b0?pvs=4)  


Next steps:  
I have q
uestions for you: 

1. What variables do you change when building RAGs?
2. What is the set of strategies I should add to
 the solution? (parent-son etc.)
3. How can I improve it in general? 
4. Is anyone  interested in a leaderboard for best
 parameter configs?

Check out the blog post:

[Link to part 3](https://topoteretes.notion.site/Going-beyond-Langchain-W
eaviate-Level-3-towards-production-e62946c272bf412584b12fbbf92d35b0?pvs=4)

  
*Remember to give this post an upvote if 
you found it insightful!*  
*And also star our* [*Github repo*](https://github.com/topoteretes/PromethAI-Memory)
```
---

     
 
MachineLearning -  [ [D] Relevance Extraction in RAG Pipelines ](https://www.reddit.com/r/MachineLearning/comments/17k6iha/d_relevance_extraction_in_rag_pipelines/) , 2023-11-24-0909
```
I came across this interesting problem in RAG, what I call **Relevance Extraction**.

After retrieving relevant document
s (or chunks), these chunks are often large and may contain several portions **irrelevant** to the query at hand. Stuffi
ng the entire chunk into an LLM prompt impacts token-cost as well as response accuracy (distracting the LLM with irrelev
ant text), and and can also cause bumping into context-length limits.

So a critical step in most pipelines is **Relevan
ce Extraction**: use the LLM to extract **verbatim** only the portions relevant to the query. This is known by other nam
es, e.g. LangChain calls it Contextual Compression, and the RECOMP paper calls it Extractive Compression [https://twitte
r.com/manelferreira\_/status/1713214439715938528](https://twitter.com/manelferreira_/status/1713214439715938528)

Thinki
ng about how best to do this, I realized it is **highly inefficient** to simply ask the LLM to 'parrot' out relevant por
tions of the text: this is obviously slow, and also consumes valuable token generation space and can cause you to bump i
nto context-length limits (and of course is expensive, e.g. for gpt4 we know generation is 6c/1k tokens vs input cost of
 3c/1k tokens).

I realized the best way (or at least a good way) to do this is to **number** the sentences and have the
 LLM simply spit out the relevant sentence **numbers.** Langroid's unique Multi-Agent + function-calling architecture al
lows an elegant implementation of this, in the RelevanceExtractorAgent ([https://github.com/langroid/langroid/blob/main/
langroid/agent/special/relevance\_extractor\_agent.py](https://github.com/langroid/langroid/blob/main/langroid/agent/spe
cial/relevance_extractor_agent.py)).  The agent annotates the docs with sentence numbers, and instructs the LLM to pick 
out the **sentence-numbers** relevant to the query, rather than whole sentences using a function-call (SegmentExtractToo
l [https://github.com/langroid/langroid/blob/main/langroid/agent/tools/segment\_extract\_tool.py](https://github.com/lan
groid/langroid/blob/main/langroid/agent/tools/segment_extract_tool.py)), and the agent's function-handler interprets thi
s message and strips out the indicated sentences by their numbers. To extract from a set of passages, langroid automatic
ally does this async + concurrently so latencies in practice are much, much lower than the sentence-parroting approach.


\[FD -- I am the lead dev of Langroid - [https://github.com/langroid/langroid](https://github.com/langroid/langroid))


I thought this **numbering** idea is a fairly obvious idea in theory, so I looked at LangChain's equivalent `LLMChainExt
ractor` (they call this Contextual Compression [https://python.langchain.com/docs/modules/data\_connection/retrievers/co
ntextual\_compression?ref=blog.langchain.dev](https://python.langchain.com/docs/modules/data_connection/retrievers/conte
xtual_compression?ref=blog.langchain.dev)) and was surprised to see it is the simple '**parrot**' method, i.e. the LLM w
rites out whole sentences verbatim from its input. I thought it would be interesting to compare Langroid vs LangChain, y
ou can see it in this Colab: [https://colab.research.google.com/drive/1RDPCR2xNuBffcmpUuPIXYDRG3SXIJC5F](https://colab.r
esearch.google.com/drive/1RDPCR2xNuBffcmpUuPIXYDRG3SXIJC5F)

On the specific example in the notebook, the Langroid **num
bering** approach is 22x faster and 36% cheaper (with gpt4) than LangChain's **parrot** method (I promise this name is *
not* inspired by their logo :). See table below.

&#x200B;

[Relevance Extraction: Langroid vs LangChain](https://previe
w.redd.it/1m7u6ulq8fxb1.png?width=1108&format=png&auto=webp&s=d2f35cf5db07e2e699baa54b274ffa60833e924a)

&#x200B;

I won
der if anyone had thoughts on relevance extraction, or other approaches. At the very least, I hope langroid's implementa
tion is useful to you -- you can use the `DocChatAgent.get_verbatim_extracts()` ([https://github.com/langroid/langroid/b
lob/main/langroid/agent/special/doc\_chat\_agent.py#L804](https://github.com/langroid/langroid/blob/main/langroid/agent/
special/doc_chat_agent.py#L804)) as part of your pipeline, regardless of whether you are using Langroid for your entire 
system or not.

&#x200B;
```
---

     
 
MachineLearning -  [ [R] Model Troubles ](https://www.reddit.com/r/MachineLearning/comments/17ikh2u/r_model_troubles/) , 2023-11-24-0909
```
So i’m working on a model that diagnoses alzheimer’s disease and suggests medication depending on how severe the symptom
s might have become 
I’m using the Openai API and Langchain.

But it’s dumb and it doesn’t learn (
Me: I forgot my keys 
at home
Model: Yup, Alzheimer’s)
How do i incorporate the actual machine learning

Edit: I didn’t choose this project my
 supervisor did and she barely knows anything about the topic or how to approach it
```
---

     
