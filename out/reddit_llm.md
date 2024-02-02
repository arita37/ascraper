 
all -  [ Are all the Google Vertex integrations deprecated? ](https://www.reddit.com/r/LangChain/comments/1agoi5b/are_all_the_google_vertex_integrations_deprecated/) , 2024-02-02-0909
```
I'm new to building Gen AI solutions and have been learning in Vertex (I'm a GCP solution architect with an infrastructu
re focus). I'm even newer to LangChain. But as I'm reading through the LangChain documentation it looks like every Verte
x integration is marked deprecated. 

Are there any Vertex integrations that aren't deprecated?
```
---

     
 
all -  [ summary of the google sheets data ](https://www.reddit.com/r/LangChain/comments/1aglqsm/summary_of_the_google_sheets_data/) , 2024-02-02-0909
```
I'm new to the LLM world, i'm looking for a use case where if i provide the google sheets data, it should give suggestio
ns like what kind of data it is and what insights can be derived from the data.

please help me with the model or a sour
ce that helps me
```
---

     
 
all -  [ File Chunking Strategy ](https://www.reddit.com/r/LangChain/comments/1agj9vr/file_chunking_strategy/) , 2024-02-02-0909
```
Now that I’ve graduated past using the standard RecursiveString chunking that LangChain provides. I’m looking to impleme
nt something more robust and accurate when chunking large pdfs that have similar styles (tables, images)

I’ve been play
ing around with Unstructured but have been having a hard time using it consistently. It seems every time I try to recrea
te something I was working on the previous day in Google Collab, there are dependency issues but I’ve been fixing it as 
I go.

My main question is, for my use case of a consistent format of my pdfs, what is the best library to chunk the dat
a prior to generate embeddings?

A follow up is, what libraries do you use to ensure when a file is updated, embeddings 
aren’t created on top of the previous embeddings and the original is removed from the DB and updated with the new embedd
ings?
```
---

     
 
all -  [ Indexes in MongoDB ](https://www.reddit.com/r/LangChain/comments/1agfuhv/indexes_in_mongodb/) , 2024-02-02-0909
```
Hello Guys,

Can we create indexes in Mongo Atlas DB using pymongo?

It seems all the documentations are only creating m
anually.

Any help please?

Thanks and regards,
Baradwaj Aryasomayajula
```
---

     
 
all -  [ is there any good rag based open-source chatbot codebase ](https://www.reddit.com/r/LangChain/comments/1agfnox/is_there_any_good_rag_based_opensource_chatbot/) , 2024-02-02-0909
```
I want to go though code of  any good rag based chatbot. Can you suggest any open-source project
```
---

     
 
all -  [ Langchain agents with LM Studio ](https://www.reddit.com/r/LangChain/comments/1agfjcq/langchain_agents_with_lm_studio/) , 2024-02-02-0909
```
I have build Openai based chatbot that uses Langchain agents - wiki, dolphin, etc. 

I am trying to switch to Open sourc
e LLM for this chatbot, has anyone used Langchain with LM studio? I was facing some issues using open source LLM from LM
 Studio for this task. 

Questions:
Q1. Has anyone successfully used LM Studio with Langchain agents? If so, how?
Q2. Ca
n you provide github links for Langchain + LM studio implementations.

TIA
```
---

     
 
all -  [ Deterministic behaviour in an LLM (Salesfunnel) ](https://www.reddit.com/r/LangChain/comments/1ageri4/deterministic_behaviour_in_an_llm_salesfunnel/) , 2024-02-02-0909
```
Hello everyone,

in my company, before we used LLMs, we had a deterministic bot with intent recognition. Examples:

A us
er asked if our company offers credits cards. If yes, the bot should tell infos about the cards and offer him to order o
ne. If he´s interested, he will get an offer for xyz. The complexity about this system is that there were multiple steps
 involved in the process, which different paths/routes to take.

In my team, we want to build a new, LLM-based Bot with 
OpenAI models. The system itself already works pretty good, but we have absolutely no clue how to integrate that behavio
ur paths into an LLM based system. 

The prefered way would be to define the intends and the follow up routes in some ki
nd of yaml file or maybe directly in Code. I am pretty sure, that we are not the only company who want some kind of sale
s funnel into their Bot. 

Does anyone have experience and/or example code or just a suggestion how to tackle this issue
?

Thanks :)
```
---

     
 
all -  [ Azure-search ](https://www.reddit.com/r/LangChain/comments/1agcymb/azuresearch/) , 2024-02-02-0909
```
Can we get all the chunks  from the azure search vector db ?
Without doing any similarity search just retrieve all the c
hunks from the vector db ?
```
---

     
 
all -  [ Can we use langchain without vector db? ](https://www.reddit.com/r/LangChain/comments/1agayui/can_we_use_langchain_without_vector_db/) , 2024-02-02-0909
```
If I create embeddings of a context,  can I pass the embeddings directly to OpenAi and execute the prompt on top of cone
xt without requiring to put the embeddings into vector db and then pull again from there to be sent as a retrieval chain
?

Tried to look through but all examples seems to use a vector db.
```
---

     
 
all -  [ [Langchain] Personnalisation Opensearch / Elasticsearch basée sur RAG? ](https://www.reddit.com/r/redditenfrancais/comments/1agapt8/langchain_personnalisation_opensearch/) , 2024-02-02-0909
```
J'ai une application de chiffon basée sur du XML brut. Le LLM est capable de analyser avec succès les informations hiéra
rchiques dans les données et de fournir une réponse, il serait donc idéal de conserver les balises.

Cependant, l'élémen
t de récupération est susceptible d'être affecté négativement par la présence des étiquettes étant donné qu'il interfère
 (à un certain niveau) avec la représentation du langage naturel.

** Y a-t-il un moyen à Langchain pour intégrer et réc
upérer sur un champ dans un enregistrement, mais en rendre un autre dans le même document? **

Traduit et reposté à part
ir de la publication 17vjbzs de la communauté langchain. Pour retrouver la publication originale, insérez l'id de la pub
lication après 'reddit.com/'
```
---

     
 
all -  [ [Langchain] Existe-t-il un moyen de réinitialiser / essuyer un index de poireau sans avoir à le supp ](https://www.reddit.com/r/redditenfrancais/comments/1aga1hd/langchain_existetil_un_moyen_de_réinitialiser/) , 2024-02-02-0909
```
J'utilise donc Pinecone pour stocker certains index. Je fais beaucoup d'essais et d'erreurs et je continue à améliorer l
a qualité de l'index, et je n'ai pas encore trouvé de moyen d'accélérer le processus de recommandation avec un index pro
pre. Je suis donc obligé de le supprimer et de le recréer, ce qui prend beaucoup de temps car chaque création d'index me
t plusieurs minutes à initialiser.


Y a-t-il une meilleure façon? Ou est-ce que je regarde ce mal? Je veux juste accélé
rer mon flux de développement.


Merci!

Traduit et reposté à partir de la publication 14avuww de la communauté langchai
n. Pour retrouver la publication originale, insérez l'id de la publication après 'reddit.com/'
```
---

     
 
all -  [ What are the coolest apps made on LangChain? ](https://www.reddit.com/r/LangChain/comments/1ag8rpx/what_are_the_coolest_apps_made_on_langchain/) , 2024-02-02-0909
```
Hey what been one of the most trendiest and cool apps made using LangChain?
```
---

     
 
all -  [ what works best for creating code completion assistant using RAG over Codebase. ](https://www.reddit.com/r/LangChain/comments/1ag8kqg/what_works_best_for_creating_code_completion/) , 2024-02-02-0909
```
I am trying to create an assistant for code completion on private codebase.

i am finding difficult to get correct conte
xt from regular embeddings.

is there better way to embed, index and retrieve code efficiently from codebase?
```
---

     
 
all -  [ [D] What's the best current RAG setup that would work with a local LLM? ](https://www.reddit.com/r/MachineLearning/comments/1ag6bo7/d_whats_the_best_current_rag_setup_that_would/) , 2024-02-02-0909
```
I've tried things like langchain in the past (6-8 months ago) but they were cumbersome and didn't work as expected.

I  
need RAG to get data from various pdfs (long one, 150+ pages) - and i  need a setup that will allow me to add more and m
ore data sources.

I wanna run this locally, can get a 24gb video card (or 2x16gb ones) - so i can run using 33b or smal
ler models.

I  know things in the industry change every 2 weeks, so i'm hoping there's  an easy and efficient way of do
ing RAG (compared to 6 months ago)
```
---

     
 
all -  [ Any custom GPTs for crypto / defi? ](/r/ChatGPT/comments/1ag67kn/any_custom_gpts_for_crypto_defi/) , 2024-02-02-0909
```

```
---

     
 
all -  [ Help for a project! Llama Index or Langchain ? ](https://www.reddit.com/r/LangChain/comments/1ag34dc/help_for_a_project_llama_index_or_langchain/) , 2024-02-02-0909
```
Hello 👋🏾!

I'm looking forward to build a chatbot that can:

1. Interact with my class note: indeed, I'm at university a
nd would like to chat with the bot and ask questions about some class notes. 

Requirements: it has to be able to read P
DF, docx, word and sometimes HTML files.

2. I might be interested in the future to add interaction with my calendar so 
that I can ask questions about my day.

Requirements: it has to take in account my calendar informations.

Do you think 
I should use llama index or Langchain.
```
---

     
 
all -  [ RAG for structured data (querying RD vs. knowledge graph/graph db) ](https://www.reddit.com/r/LlamaIndex/comments/1afu653/rag_for_structured_data_querying_rd_vs_knowledge/) , 2024-02-02-0909
```
Hi all,

I am implementing a data system for retrieval and thought to get opinions given how fast the field is moving.


So background, I have a bunch of data in the form of documents, tables (think a lot of csv’s/excel files), and other tex
t data.

My question relates mainly to the tabular data that I have, the text data I will embed and store in a vector db
.

The two approaches possible for the tabular data are:

1. More traditional:

* Transform into a common structure and 
pass into a traditional relational database (Postgres, etc).
* After that using the metadata from each table with Llama 
Index: SQLAutoVectorQueryEngine to get the data that I need for each question regarding the data

Pro’s:  
I can tell ex
actly what is being queried to get what results and I have more control over the databases themselves and their associat
ed metadata and description.

Con’s:  
A lot harder to scale the structural data portion of this as more data floats in 
as CSV’s/xlsx files.  
Will there be confusion as to how to use the combination of the text/document data in the vectord
b combined with the relational data in the warehouse?

1. Knowledge graph and graph DB’s:  
Rather than structure the da
ta for consumption into a Relational database, use Llama Index and unstructured to convert the tabular data into a forma
t capable of being used as a knowledge graph and graph DB.

I BELIEVE that the process for creating such graph’s is fair
ly automated by LLama Index and Langchain.

Pro’s:  
Easier to scale.  
The relationships might make it easier to pull t
he relevant data especially given the scale.

Con’s  
I am not sure how well numeric data, the type that is generally st
ored in relational databases for storage does in a graph DB. Are they able to build relationships easily and accurately?


Would love some thoughts and opinions,
```
---

     
 
all -  [ [Langchain] Quali framework LLM usi in produzione e perché? ](https://www.reddit.com/r/redditinitaliano/comments/1aft25l/langchain_quali_framework_llm_usi_in_produzione_e/) , 2024-02-02-0909
```
Mi sono imbattuto in molti framework LLM: Langchain, Llamaindex, LMQL, Guida, Marvin, istruttore, ecc. C'è molta sovrapp
osizione tra loro e non so se nessuno di loro aggiunge effettivamente un valore ai flussi di lavoro LLM in un certo sens
o È mantenibile e robusto. Finora, sono stato in grado di costruire le mie piccole librerie da utilizzare in alcune appl
icazioni LLM (nessun RAG), ma come considero i progressi più recenti sul campo (chiamate di funzione garantita, meglio s
trag, agenti e utilizzo degli strumenti, ecc.), Mi chiedo se usare uno di questi framework sarebbe un approccio migliore
 rispetto alla costruzione di tutto da solo.
Apprezzo i tuoi pensieri e i tuoi commenti su questo!

Tradotto e ripubblic
ato dalla pubblicazione 18anbjf della comunità langchain. Per trovare il post originale, inserire l'id del post dopo 're
ddit.com/'
```
---

     
 
all -  [ An introduction to prompt engineering and LangChain for data scientists ](https://www.reddit.com/r/PromptEngineering/comments/1afsr1v/an_introduction_to_prompt_engineering_and/) , 2024-02-02-0909
```
In this hands-on guide, you’ll learn foundational elements and techniques of prompt engineering to programmatically inte
ract with LLMs in the most effective way. As a developer, these skills will allow you to return an output most suitable 
for your generative AI applications, preventing inconclusive or inaccurate model outputs.

This is the first article in 
a series offering a free, interactive online environment for coding, detailed step-by-step instructions for building you
r generative AI engine, and customizable templates to help you get started. You’ll learn to leverage LangChain’s open-so
urce framework to build reusable prompt templates and interact with any LLM of your choice. In the second article, we’ll
 apply our learnings and additional advanced techniques in prompt engineering to query Teradata VantageCloud databases u
sing conversational English.

Full article on Medium: [https://medium.com/teradata/generative-ai-part-1-an-introduction-
to-prompt-engineering-and-langchain-742987f2d9c1](https://medium.com/teradata/generative-ai-part-1-an-introduction-to-pr
ompt-engineering-and-langchain-742987f2d9c1)
```
---

     
 
all -  [ How would you organize a dialogues documents in chunks? ](https://www.reddit.com/r/LangChain/comments/1afs1kz/how_would_you_organize_a_dialogues_documents_in/) , 2024-02-02-0909
```
I have a chat history between a client and a coach. I need to create an ability for a coach to quickly recall details fr
om previous conversations. 
Example:
User asks: 'remember i told you about mom'
Imagine it was two months ago - coach wh
o has multiple clients can't remember everything, so she need a quick search in a chat history and calls transcripts to 
get a summary of everything the client has told about her mom.

How would you split and organize chat history and calls 
transcripts to chunks?

based on what?

when it something that user says it's seems straight forward. but imagine someth
ing like this:

coach: was you close with her?
client: yes

so client only says yes, i need somehow keep the ref to the 
question.
```
---

     
 
all -  [ [Langchain] Rag pour PDF avec des tables ](https://www.reddit.com/r/redditenfrancais/comments/1afr7v5/langchain_rag_pour_pdf_avec_des_tables/) , 2024-02-02-0909
```
Je veux construire un système de chiffon pour les documents scientifiques qui contient les textes théoriques avec des éq
uations, des tables et des diagrammes étiquetés. Les questions peuvent être de la compréhension de la théorie, des équat
ions et des informations sur les tables. Comment dois-je procéder? Avoir une idée de construire un système de chiffon na
ïf uniquement.
Toutes les ressources seront utiles.

Traduit et reposté à partir de la publication 18xp9xi de la communa
uté langchain. Pour retrouver la publication originale, insérez l'id de la publication après 'reddit.com/'
```
---

     
 
all -  [ [Langchain] Langchain vs Llamaindex ](https://www.reddit.com/r/redditenfrancais/comments/1afpfux/langchain_langchain_vs_llamaindex/) , 2024-02-02-0909
```
J'ai vu que Langchain avait lancé des modèles et Llamaindex a poussé de nombreux modèles de cas d'utilisation et des dép
ositions. Au début de novembre, quel est votre avis sur les points sweet d'utilisation de Langchain contre Llamaindex? J
'avais l'habitude de travailler sur le côté commercial dans les services financiers (pas les banques ou l'assurance) et 
je vois beaucoup de cas d'utilisation pour le chiffon (la plupart) et les agents (certains). Mais je suis un débutant su
r la technologie et je ne sais pas où passer mon temps à apprendre. Selon vous, quel est le sweetspot pour l'un contre l
'autre en ce qui concerne les types d'applications, ou le coût et l'efficacité? Quelles sont les faiblesses début novemb
re? Je sais que les choses peuvent changer dans un mois. Merci.

Traduit et reposté à partir de la publication 17nnclu d
e la communauté langchain. Pour retrouver la publication originale, insérez l'id de la publication après 'reddit.com/'
```
---

     
 
all -  [ LangDAO … $LANG ](https://i.redd.it/f7ngtg3tktfc1.jpeg) , 2024-02-02-0909
```
Last week, I saw a post about LangDAO, something that could be a type of crypto used to compensate contributions in the 
langchain community. This week, I'm trying to find the posts and threads on X, but I don't see anything. Any idea what m
ight have happened?
```
---

     
 
all -  [ Innovating S3 Bucket Retrieval: Langchain Community S3 Loaders with OpenAI API ](https://www.reddit.com/r/minio/comments/1afopg6/innovating_s3_bucket_retrieval_langchain/) , 2024-02-02-0909
```
In the rapidly evolving world of data storage and processing, combining efficient cloud storage solutions with advanced 
AI capabilities presents a transformative approach to handling vast volumes of data. This article demonstrates a practic
al implementation using MinIO, Langchain and OpenAI’s GPT-3.5 model, focusing on summarizing documents stored in MinIO b
uckets.

[https://blog.min.io/langchain-openai-s3-loader/?utm\_source=reddit&utm\_medium=organic-social+&utm\_campaign=l
angchain\_openai\_s3\_loader](https://blog.min.io/langchain-openai-s3-loader/?utm_source=reddit&utm_medium=organic-socia
l+&utm_campaign=langchain_openai_s3_loader)
```
---

     
 
all -  [ Handling concurrent messages for chatbot using Flask ](https://www.reddit.com/r/flask/comments/1afojm9/handling_concurrent_messages_for_chatbot_using/) , 2024-02-02-0909
```
I am working on creating a WhatsApp based chatbot using Langchain and WhatsApp business API. It works well for 1 user as
 of now. Moving ahead I want it to handle concurrent messages. Here I also want to add a wait time after some 'x' number
 of messages. How can I handle these 2 things in Flask? 

I tried using Flask app session (a dictionary which stores all
 user sessions), multi-threading and Locks. But the bot is not able to handle concurrent messages well. While testing on
 2 devices simultaneously it was jumbling up the responses

Additional information -
I run the flask server followed by 
running an ngrok server. The url obtained from the ngrok server acts as the callback URL for the WhatsApp business API.
```
---

     
 
all -  [ Whitepaper Demystifying LLM-based Systems ](https://www.reddit.com/r/ChatGPT/comments/1afnl3i/whitepaper_demystifying_llmbased_systems/) , 2024-02-02-0909
```
Hey

Just stumbled upon something super cool that DataStax and LangChain have rolled out – a practical guide on leveragi
ng Large Language Models (LLMs) in our projects! 🚀

[https://www.datastax.com/resources/whitepaper/an-llm-agent-referenc
e-architecture-demystifying-llm-based-systems](https://www.datastax.com/resources/whitepaper/an-llm-agent-reference-arch
itecture-demystifying-llm-based-systems)
```
---

     
 
all -  [ Demystifying LLM-based Systems ](https://www.reddit.com/r/vectordatabase/comments/1afnjlb/demystifying_llmbased_systems/) , 2024-02-02-0909
```
Hey

Just stumbled upon something super cool that DataStax Astra and LangChain have rolled out – a practical guide on le
veraging Large Language Models (LLMs) in our projects with vector stores! 🚀

[https://www.datastax.com/resources/whitepa
per/an-llm-agent-reference-architecture-demystifying-llm-based-systems](https://www.datastax.com/resources/whitepaper/an
-llm-agent-reference-architecture-demystifying-llm-based-systems)
```
---

     
 
all -  [ Bypass 4096 tokens ](https://www.reddit.com/r/LangChain/comments/1afmn9r/bypass_4096_tokens/) , 2024-02-02-0909
```
Hi! I am new to this and I do not know how to bypass the limitation of tokens. I should split my prompt in multiple chun
ks? Is there a method: refine or map-reduce? I have a large prompt and I do not know how to split it.
```
---

     
 
all -  [ New Whitepaper written by LangChain & DataStax ](https://www.reddit.com/r/LLMDevs/comments/1afmbwr/new_whitepaper_written_by_langchain_datastax/) , 2024-02-02-0909
```
Titled '[An LLM Agent Reference Architecture: Demystifying LLM-based Systems](https://www.datastax.com/resources/whitepa
per/an-llm-agent-reference-architecture-demystifying-llm-based-systems?utm_medium=social_organic&utm_source=reddit&utm_c
ampaign=wp&utm_content=putv)'

The paper gives some design patterns, in-depth architectural examples, and things to keep
 in mind when architecting LLM-based systems. Worth a read!

&#x200B;
```
---

     
 
all -  [ Developing a Quiz Generator from Medical Course PDFs ](https://www.reddit.com/r/LangChain/comments/1afm8zg/developing_a_quiz_generator_from_medical_course/) , 2024-02-02-0909
```
 

&#x200B;

Hey r/LangChain r/LlamaIndex

I'm diving into an exciting venture for a non-profit university project where
 we aim to build an application generating quizzes from medical course PDFs. The concept is simple: users choose a cours
e in a user-friendly interface, click 'Generate,' and watch quiz questions come to life.

However, I'm currently stuck o
n the most effective strategy for '**chunking**' and '**retrieving**' information from the pre-saved PDFs within the app
lication. If you've got experience with similar app development or ideas on the best approach, I'd greatly appreciate yo
ur input.

I think to use llm and embeddings 

Any suggestions, links to helpful resources, or shared experiences would 
be immensely valuable. This is a non-profit initiative at the university, and your guidance can make a significant impac
t. Thanks in advance for your invaluable help! 🌐✨
```
---

     
 
all -  [ How to build a Text to SQL Model that asks for more information if the query is too vague ](https://www.reddit.com/r/LangChain/comments/1afkz4o/how_to_build_a_text_to_sql_model_that_asks_for/) , 2024-02-02-0909
```
I am using GPT 3.5-Turbo-Instinct and feeding in my dataschema into the prompt. I am creating my SQL query using create\
_sql\_chain and then running the query in the database through JDBC. So far, it is working okay however, if I am looking
 to push this to production, I need the model to not return anything if it is not confident in its answer or if the quer
y being asked is too vague.

For instance, if I ask my text to sql model 'how many rows are there', it should return bac
k something saying 'this query is too vague'. Likewise, if I were to ask it a question such as, 'Return the GPA and Netw
orth of Nadir', how do I get it to do 'WHERE LastName = 'Nadir' rather than 'WHERE FirstName = 'Nadir'. I thought that b
y potentially getting confidence scores I could explore and find a threshold where the human needs to clarify what they 
meant until the model had a confident enough query
```
---

     
 
all -  [ Which vector databases are widely used in the industry and are considered suitable for production pu ](https://www.reddit.com/r/LangChain/comments/1afkc5g/which_vector_databases_are_widely_used_in_the/) , 2024-02-02-0909
```
Currently, I am using Chroma DB in production as a vector database. However, I am facing challenges, including delayed r
esponses from the API and potential issues with semantic search, leading to results that do not meet our expectations. C
an you suggest a robust database suitable for production, and do you have any additional insights or recommendations bas
ed on your expertise?
```
---

     
 
all -  [ ReactJS + LangChain: New JS Lib To Create Frontends Powered by LangServe ](https://www.reddit.com/r/LangChain/comments/1afk4dr/reactjs_langchain_new_js_lib_to_create_frontends/) , 2024-02-02-0909
```
Hi Reddit! This is about a new [open source project](https://github.com/nluxai/nlux) I'm starting for a React JS / Javas
cript library that makes it **super simple to create conversational AI interfaces** using LangChain's **LangServe**, Hug
gingFace, or any other LLM.

The project is called NLUX (for *Natural Language User Experience*) and you can already sta
rt using it to create a web app for your LC backend, or embed LLMs into your web app.

Project Website:

* [NLUX.ai](htt
ps://nlux.ai/) — for docs, examples, source code, etc.
* [Example here](https://docs.nlux.ai/examples/langchain-langserv
e-adapter) using LangServe + React JS

What you can do with NLUX:

* **Build AI Chat Interfaces In Minutes** — High qual
ity conversational AI UI in a few lines of code.
* **Flexible LLM Adapters** — For LangServe, HuggingFace, ChatGPT .. an
d more coming soon.
* An API to **Create Your Own Adapter** — for any LLM or custom backend.
* **Chatbot Personas** — Co
nfigure the bot and user profiles for personalised interactions.
* **Zero Dependencies** — Lightweight codebase, with ze
ro-dep ! except for LLM front-end libraries.

Give it a try and let me know what you think!

Questions, ideas or feedbac
k? I'm all ears in the comments! 🙂 ⚛️

*PS: I’m may give this post a little promo to get some early adopters. The projec
t is and will always remain free, open source, and self-funded.*

SalmenLead Developer
```
---

     
 
all -  [ Building a PDF AI using function calling ](https://www.reddit.com/r/LangChain/comments/1afja1t/building_a_pdf_ai_using_function_calling/) , 2024-02-02-0909
```
Chat with PDFs is the todo app of AI and i’ve been thinking about building an advanced one using function calling. What 
do you think of this flow:

1. LLM first determines if it needs to search docs or the web for context
2. Then decides if
 it needs a specific doc or the latest one
3. Then decides to search a doc or get context to summarize
4. Produces an an
swer using this context

Using this flow the LLM can search specific docs, summarize, or bring in web context to enhance
 the answer. Thoughts?  

https://preview.redd.it/rhni60skesfc1.png?width=1812&format=png&auto=webp&s=010b2403811e6729e2
7a2c1f04f3c407f523ff27
```
---

     
 
all -  [ 5 months after laid off - no even single interview. ](https://www.reddit.com/r/resumes/comments/1afj368/5_months_after_laid_off_no_even_single_interview/) , 2024-02-02-0909
```
&#x200B;

https://preview.redd.it/siyhz4tkcsfc1.png?width=1234&format=png&auto=webp&s=2eebc76fc307bd58b460e93677ff2fed1f
240454
```
---

     
 
all -  [ metadata tagging with langchain, ](https://www.reddit.com/r/LangChain/comments/1afiba1/metadata_tagging_with_langchain/) , 2024-02-02-0909
```
hey, I am new to langhchain and using it in my nodejs application , I  have used langchain to successfully split the doc
uments into chunks with recursive vector splitting, I want to add another metadata  before embedding it, is langchain su
itable for this? I have previously done this manually but it takes a lot of time and i want to try this in the library w
ay. I am looking for something parallel to the ingestingPipeline feature in llamaIndex. would really appricate any guidl
elines!
```
---

     
 
all -  [ Become an AI Developer (Free 9 Part Series) ](https://www.reddit.com/r/PromptDesign/comments/1afgt68/become_an_ai_developer_free_9_part_series/) , 2024-02-02-0909
```
Just sharing a free series I stumbled across on Linkedin - DataCamp's 9-part AI code-along series.

This specific sessio
n linked below is 'Prompt Engineering with GPT & LangChain' but there are 8 others to have a look at and code along to.


*Learn how to perform sentiment analysis with GPT and LangChain, learn about MRKL prompts used to help LLMs reason, and
 build a simple AI agent. You'll also learn how to use prompt templates and parse the output from prompts, as well as fi
lter bad unsavory content with the moderation API. Code Along on DataCamp Workspace:* [https://www.datacamp.com/code-alo
ng/prompt-engineering-gpt-langchain](https://www.datacamp.com/code-along/prompt-engineering-gpt-langchain)

Find all of 
the sessions at: [https://www.datacamp.com/ai-code-alongs](https://www.datacamp.com/ai-code-alongs)
```
---

     
 
all -  [ Become an AI Developer (Free 9 Part Series) ](https://www.reddit.com/r/pytorch/comments/1afgpbv/become_an_ai_developer_free_9_part_series/) , 2024-02-02-0909
```
Just sharing a free series I stumbled across on Linkedin - DataCamp's 9-part AI code-along series.

This specific sessio
n linked below is 'Building Chatbots with OpenAI API and Pinecone' but there are 8 others to have a look at and code alo
ng to.

*Start from basics to build on skills with GPT, Pinecone and LangChain to create a chatbot that answers question
s about research papers. Make use of retrieval augmented generation, and learn how to combine this with conversational m
emory to hold a conversation with the chatbot. Code Along on DataCamp Workspace:* [*https://www.datacamp.com/code-along/
building-chatbots-openai-api-pinecone*](https://www.datacamp.com/code-along/building-chatbots-openai-api-pinecone)

Find
 all of the sessions at: [https://www.datacamp.com/ai-code-alongs](https://www.datacamp.com/ai-code-alongs)
```
---

     
 
all -  [ Enhancing Chatbot UX with Dynamic Quick Replies in LangChain - Feasible? ](https://www.reddit.com/r/LangChain/comments/1afgjex/enhancing_chatbot_ux_with_dynamic_quick_replies/) , 2024-02-02-0909
```
I'm working on enhancing a chatbot's user experience by integrating dynamic quick replies for instances where certain in
formation is missing for function/tool execution.

For example, consider a function `search_movies` that has an optional
 parameter `genre`. When a user writes 'I want to watch a movie' without specifying a genre, I'd like the chatbot to pre
sent a list of available genres as quick replies in the UI, rather than having the user type out their preference.  


T
he conceptual solution involves:

1. pausing the chatbot's execution from the function and saving its state when additio
nal info is needed.
2. Once the user picks an option, the chatbot's state is restored, the relevant function (in this ca
se `search_movies`) is invoked with the new input, and the conversation continues.

Some tutorials have similar 'pause' 
functionality to get user inputs, but they only work when the script runs on a terminal. In the scenario above, the code
 will be behind an API so it's not possible to keep a connection open waiting for an answer.

Is this approach viable wi
th LangChain? Are there other better approaches?
```
---

     
 
MachineLearning -  [ [P]: Anukool: My job hunting assistant ](https://www.reddit.com/r/MachineLearning/comments/1adu3tw/p_anukool_my_job_hunting_assistant/) , 2024-02-02-0909
```
Hey Reddit, I've been applying for jobs and found that writing a cover letter for each position was tedious. I also delv
ed into LLM and Langchain, hoping to leverage them for a project to aid in my job hunting. So, I developed Anukool under
 the GPL license. While it's far from perfect, it has proven very useful to me, and I hope it benefits you as well. All 
I have to do is provide it with a pdf containing information about me such as my experience, skills, projects, etc and i
t will use this information along with job description to generate cover letter for me. Since I'm new to ML and LLM, any
 advice or feedback is greatly appreciated, and contributions are also welcome. I plan to utilize Llama-2 soon to furthe
r open-source the project.

Check out the GitHub link, and please star it if you find the project interesting: https://g
ithub.com/dakshesh14/anukool
```
---

     
 
MachineLearning -  [ New Data API for Astra [N] ](https://www.reddit.com/r/MachineLearning/comments/199uobn/new_data_api_for_astra_n/) , 2024-02-02-0909
```
I saw that DataStax/Astra DB [just released a new Data API to help with building production GenAI and RAG applications](
https://www.datastax.com/blog/general-availability-data-api-for-enhanced-developer-experience). This API makes the prove
n petabyte-scale of Apache Cassandra easy to use and available to any JavaScript, Python, or full-stack application deve
loper.

There will also be a joint webinar with LangChain available for registration here: [https://www.datastax.com/eve
nts/wikichat-build-a-real-time-rag-app-on-wikipedia-with-langchain-and-vercel](https://www.datastax.com/events/wikichat-
build-a-real-time-rag-app-on-wikipedia-with-langchain-and-vercel)
```
---

     
 
MachineLearning -  [ [D] While using function calling or tools on openai or langchain, does openai have access to the dat ](https://www.reddit.com/r/MachineLearning/comments/199t8be/d_while_using_function_calling_or_tools_on_openai/) , 2024-02-02-0909
```
I am working on a client project and I am using langchain's tools and agents. I want to know if the data is getting pass
ed to openai or is it just like that - Output of one function is being directly passed to the second function with the k
nowledge of openai.
```
---

     
 
MachineLearning -  [ [D] Code vs JSON output for LLM agents? Frameworks like LangChain rely on LLMs responding with JSON  ](https://www.reddit.com/r/MachineLearning/comments/197f416/d_code_vs_json_output_for_llm_agents_frameworks/) , 2024-02-02-0909
```
[CaP](https://arxiv.org/pdf/2209.07753.pdf), [Voyager](https://arxiv.org/pdf/2305.16291.pdf), [Octopus](https://arxiv.or
g/abs/2310.08588)

I work primarily with JSON based agents but code-as-policy agents seem to be extremely powerful. Here
 are some of the benefits and weaknesses I've seen

Pros of code

1. Less tool creation needed - The prebuilt math/file/
string/list manipulation abilities that come with code are enormous. In a JSON based agent, you would have to formally d
eclare each of these as a tool which you expose to the LLM and explain in your prompting, which is a lot of work and eat
s up a ton of the context window. 
2. Reduced number of transactions - The LLM can write scripts that invoke multiple to
ols and manipulate their results in ways that are difficult to do in a single transaction via JSON. For example, in one 
script, the model could search a DB 3 times, perform regex on the query results, convert them to integers, and add them 
up. Doing this in one step via JSON tool invocations is basically impossible. 
3. Less syntax errors - this might be tot
ally just vibe-based reasoning, but it really seems like LLMs have an easier time writing valid python than valid JSON, 
especially when you have lots of nested arguments in your methods.

Cons

1. Crazy risky - This is the obvious one. You 
have a machine executing random code. There are ways to mitigate this but still. I mean seriously we all learned not to 
use eval, so it is crazy to basically see research tending towards just running eval on the outputs of these models. 
2.
 Scripts with errors - Sometimes the model tries to get too fancy and writes complex programs that have bugs, resulting 
in many needed retries. 

Do any of you have thoughts or experience with these approaches in the wild? 

Is anybody awar
e of any experiments that compare these two approaches against each other? 

&#x200B;
```
---

     
 
MachineLearning -  [ [D] Are Custom LLM RAG apps going to become redundant? ](https://www.reddit.com/r/MachineLearning/comments/1929n4f/d_are_custom_llm_rag_apps_going_to_become/) , 2024-02-02-0909
```
Loks like Copilot Studio is being rolled out (https://www.microsoft.com/en-us/microsoft-copilot/microsoft-copilot-studio
) with an impressive looking no code/out of the box RAG solution.

There is a phenomenal amount of development and activ
ity in the Open Source RAG world (e.g Langchain, Llamaindex, etc), which I am a great supporter of FYI.

However, what s
eems strange is that this no code out of the box solution (Copilot Studio - just as an example of one) seems overwhelmin
gly to be the better option if you wanted to build a RAG app i.e If you compare the cost to build and productionise a cu
stom RAG app vs the cost of using Copilot Studio, it's almost an order of magnitude lower (no matter how you cut it with
 the developer time and duration). 

My question is, it seems to me we are moving towards a situation where enterprise s
olutions will make custom RAG apps redundant (not in all cases of course, but most cases), however there seems to be ver
y little discussion of this relative to the activity in the open source community. Do people agree this is a likely scen
ario? 

Obviously there will be exceptions…but on most use cases I don’t see how you can compete with an instant/minimal
 setup, low cost, highly scalable RAG solution.
```
---

     
 
MachineLearning -  [ [P] An open-source project for deploying local models ](https://www.reddit.com/r/MachineLearning/comments/18zkm5m/p_an_opensource_project_for_deploying_local_models/) , 2024-02-02-0909
```
 Introducing a new LLM WebUI project that supports various local model loading and provides streaming output for cutting
-edge online multimodal models GPT-4-Vision and Gemini-Pro-Vision. Completely free and open source, it serves as a valua
ble research tool for exploring diverse models. The project is actively under development with continuous updates:  
[ht
tps://github.com/smalltong02/keras-llm-robot](https://github.com/smalltong02/keras-llm-robot)

&#x200B;

[WebUI](https:/
/preview.redd.it/f95jievpepac1.png?width=2560&format=png&auto=webp&s=1f2908b484ededc78591719ef87efdac2f9497ba)

&#x200B;


[Configuration](https://preview.redd.it/owaj5s1repac1.png?width=2560&format=png&auto=webp&s=f837b1ef67cb8e4ccaee4ec602
a61859f53db100)

&#x200B;

[Tools & Agent](https://preview.redd.it/jrot8w9sepac1.png?width=2560&format=png&auto=webp&s=7
1e224f08620941146cd437a99bcb55d02930a9e)
```
---

     
 
deeplearning -  [ DSPy Explained! ](https://www.reddit.com/r/deeplearning/comments/1adypks/dspy_explained/) , 2024-02-02-0909
```
DSPy is the next big advancement for AI and building applications with LLMs!

Pioneered by frameworks such as LangChain 
and LlamaIndex, we can build much more powerful systems by chaining together LLM calls! This means that the output of on
e call to an LLM is the input to the next, and so on. We can think of chains as programs, with each LLM call analogous t
o a function that takes text as input and produces text as output.

DSPy offers a new programming model, inspired by PyT
orch, that gives you a massive amount of control over these LLM programs. Further the Signature abstraction wraps prompt
s and structured input / outputs to clean up LLM program codebases.

DSPy then pairs the syntax with a super novel compi
ler that jointly optimizes the instructions for each component of an LLM program, as well as sourcing examples of the ta
sk.

Here is my review of the ideas in DSPy, covering the core concepts and walking through the introduction notebooks s
howing how to compile a simple retrieve-then-read RAG program, as well as a more advanced Multi-Hop RAG program where yo
u have 2 LLM components to be optimized with the DSPy compiler! I hope you find it useful!

https://www.youtube.com/watc
h?v=41EfOY0Ldkc
```
---

     
 
deeplearning -  [ [D] Unleashing the Power of Langchain with Wandb: Revolutionizing Topic Modeling and Evaluation ](https://www.reddit.com/r/deeplearning/comments/191mm83/d_unleashing_the_power_of_langchain_with_wandb/) , 2024-02-02-0909
```
Complementing Langchain’s prowess, Wandb emerges as a powerhouse meticulously designed for developers leveraging LLM tec
hnology. As an evaluation framework and production monitoring platform, Wandb stands out for its tailored approach. Its 
arsenal comprises real-time monitoring, granular analytics, and streamlined evaluation processes, laying the groundwork 
for elevated performance and reliability in AI applications.

&#x200B;

Link: [https://medium.com/ai-advances/unleashing
-the-power-of-langchain-with-wandb-revolutionizing-topic-modeling-and-evaluation-75af5cf51b15](https://medium.com/ai-adv
ances/unleashing-the-power-of-langchain-with-wandb-revolutionizing-topic-modeling-and-evaluation-75af5cf51b15) 
```
---

     
