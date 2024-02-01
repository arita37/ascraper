 
all -  [ Innovating S3 Bucket Retrieval: LangChain Community S3 Loaders with OpenAI API ](https://blog.min.io/langchain-openai-s3-loader/) , 2024-02-01-0910
```

```
---

     
 
all -  [ RAG for structured data (querying RD vs. knowledge graph/graph db) ](https://www.reddit.com/r/LlamaIndex/comments/1afu653/rag_for_structured_data_querying_rd_vs_knowledge/) , 2024-02-01-0910
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

     
 
all -  [ [Langchain] Quali framework LLM usi in produzione e perché? ](https://www.reddit.com/r/redditinitaliano/comments/1aft25l/langchain_quali_framework_llm_usi_in_produzione_e/) , 2024-02-01-0910
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

     
 
all -  [ An introduction to prompt engineering and LangChain for data scientists ](https://www.reddit.com/r/PromptEngineering/comments/1afsr1v/an_introduction_to_prompt_engineering_and/) , 2024-02-01-0910
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

     
 
all -  [ How would you organize a dialogues documents in chunks? ](https://www.reddit.com/r/LangChain/comments/1afs1kz/how_would_you_organize_a_dialogues_documents_in/) , 2024-02-01-0910
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

     
 
all -  [ [Langchain] Rag pour PDF avec des tables ](https://www.reddit.com/r/redditenfrancais/comments/1afr7v5/langchain_rag_pour_pdf_avec_des_tables/) , 2024-02-01-0910
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

     
 
all -  [ [Langchain] Langchain vs Llamaindex ](https://www.reddit.com/r/redditenfrancais/comments/1afpfux/langchain_langchain_vs_llamaindex/) , 2024-02-01-0910
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

     
 
all -  [ LangDAO … $LANG ](https://i.redd.it/f7ngtg3tktfc1.jpeg) , 2024-02-01-0910
```
Last week, I saw a post about LangDAO, something that could be a type of crypto used to compensate contributions in the 
langchain community. This week, I'm trying to find the posts and threads on X, but I don't see anything. Any idea what m
ight have happened?
```
---

     
 
all -  [ Innovating S3 Bucket Retrieval: Langchain Community S3 Loaders with OpenAI API ](https://www.reddit.com/r/minio/comments/1afopg6/innovating_s3_bucket_retrieval_langchain/) , 2024-02-01-0910
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

     
 
all -  [ Handling concurrent messages for chatbot using Flask ](https://www.reddit.com/r/flask/comments/1afojm9/handling_concurrent_messages_for_chatbot_using/) , 2024-02-01-0910
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

     
 
all -  [ Whitepaper Demystifying LLM-based Systems ](https://www.reddit.com/r/ChatGPT/comments/1afnl3i/whitepaper_demystifying_llmbased_systems/) , 2024-02-01-0910
```
Hey

Just stumbled upon something super cool that DataStax and LangChain have rolled out – a practical guide on leveragi
ng Large Language Models (LLMs) in our projects! 🚀

[https://www.datastax.com/resources/whitepaper/an-llm-agent-referenc
e-architecture-demystifying-llm-based-systems](https://www.datastax.com/resources/whitepaper/an-llm-agent-reference-arch
itecture-demystifying-llm-based-systems)
```
---

     
 
all -  [ Demystifying LLM-based Systems ](https://www.reddit.com/r/vectordatabase/comments/1afnjlb/demystifying_llmbased_systems/) , 2024-02-01-0910
```
Hey

Just stumbled upon something super cool that DataStax Astra and LangChain have rolled out – a practical guide on le
veraging Large Language Models (LLMs) in our projects with vector stores! 🚀

[https://www.datastax.com/resources/whitepa
per/an-llm-agent-reference-architecture-demystifying-llm-based-systems](https://www.datastax.com/resources/whitepaper/an
-llm-agent-reference-architecture-demystifying-llm-based-systems)
```
---

     
 
all -  [ Bypass 4096 tokens ](https://www.reddit.com/r/LangChain/comments/1afmn9r/bypass_4096_tokens/) , 2024-02-01-0910
```
Hi! I am new to this and I do not know how to bypass the limitation of tokens. I should split my prompt in multiple chun
ks? Is there a method: refine or map-reduce? I have a large prompt and I do not know how to split it.
```
---

     
 
all -  [ New Whitepaper written by LangChain & DataStax ](https://www.reddit.com/r/LLMDevs/comments/1afmbwr/new_whitepaper_written_by_langchain_datastax/) , 2024-02-01-0910
```
Titled '[An LLM Agent Reference Architecture: Demystifying LLM-based Systems](https://www.datastax.com/resources/whitepa
per/an-llm-agent-reference-architecture-demystifying-llm-based-systems?utm_medium=social_organic&utm_source=reddit&utm_c
ampaign=wp&utm_content=putv)'

The paper gives some design patterns, in-depth architectural examples, and things to keep
 in mind when architecting LLM-based systems. Worth a read!

&#x200B;
```
---

     
 
all -  [ Developing a Quiz Generator from Medical Course PDFs ](https://www.reddit.com/r/LangChain/comments/1afm8zg/developing_a_quiz_generator_from_medical_course/) , 2024-02-01-0910
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

     
 
all -  [ How to build a Text to SQL Model that asks for more information if the query is too vague ](https://www.reddit.com/r/LangChain/comments/1afkz4o/how_to_build_a_text_to_sql_model_that_asks_for/) , 2024-02-01-0910
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

     
 
all -  [ Which vector databases are widely used in the industry and are considered suitable for production pu ](https://www.reddit.com/r/LangChain/comments/1afkc5g/which_vector_databases_are_widely_used_in_the/) , 2024-02-01-0910
```
Currently, I am using Chroma DB in production as a vector database. However, I am facing challenges, including delayed r
esponses from the API and potential issues with semantic search, leading to results that do not meet our expectations. C
an you suggest a robust database suitable for production, and do you have any additional insights or recommendations bas
ed on your expertise?
```
---

     
 
all -  [ ReactJS + LangChain: New JS Lib To Create Frontends Powered by LangServe ](https://www.reddit.com/r/LangChain/comments/1afk4dr/reactjs_langchain_new_js_lib_to_create_frontends/) , 2024-02-01-0910
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

     
 
all -  [ Building a PDF AI using function calling ](https://www.reddit.com/r/LangChain/comments/1afja1t/building_a_pdf_ai_using_function_calling/) , 2024-02-01-0910
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

     
 
all -  [ 5 months after laid off - no even single interview. ](https://www.reddit.com/r/resumes/comments/1afj368/5_months_after_laid_off_no_even_single_interview/) , 2024-02-01-0910
```
&#x200B;

https://preview.redd.it/siyhz4tkcsfc1.png?width=1234&format=png&auto=webp&s=2eebc76fc307bd58b460e93677ff2fed1f
240454
```
---

     
 
all -  [ metadata tagging with langchain, ](https://www.reddit.com/r/LangChain/comments/1afiba1/metadata_tagging_with_langchain/) , 2024-02-01-0910
```
hey, I am new to langhchain and using it in my nodejs application , I  have used langchain to successfully split the doc
uments into chunks with recursive vector splitting, I want to add another metadata  before embedding it, is langchain su
itable for this? I have previously done this manually but it takes a lot of time and i want to try this in the library w
ay. I am looking for something parallel to the ingestingPipeline feature in llamaIndex. would really appricate any guidl
elines!
```
---

     
 
all -  [ Become an AI Developer (Free 9 Part Series) ](https://www.reddit.com/r/PromptDesign/comments/1afgt68/become_an_ai_developer_free_9_part_series/) , 2024-02-01-0910
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

     
 
all -  [ Become an AI Developer (Free 9 Part Series) ](https://www.reddit.com/r/pytorch/comments/1afgpbv/become_an_ai_developer_free_9_part_series/) , 2024-02-01-0910
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

     
 
all -  [ Enhancing Chatbot UX with Dynamic Quick Replies in LangChain - Feasible? ](https://www.reddit.com/r/LangChain/comments/1afgjex/enhancing_chatbot_ux_with_dynamic_quick_replies/) , 2024-02-01-0910
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

     
 
all -  [ An open source AI Search Engine ](https://www.reddit.com/r/LangChain/comments/1affs5p/an_open_source_ai_search_engine/) , 2024-02-01-0910
```
Hi,

I just made an AI search engine with Spring Boot and LangChain4J inspired by the project search-with-lepton

If you
 are interest in it,  you can visit it here [https://github.com/vlinx-io/infinite-search](https://github.com/vlinx-io/in
finite-search)
```
---

     
 
all -  [ Data analytics with a local model ](https://www.reddit.com/r/LocalLLaMA/comments/1afemcf/data_analytics_with_a_local_model/) , 2024-02-01-0910
```
HI! I am a student and I have this project to generate automatically dashboard with useful data Analysis for a user that
 doesn't know anything about data analytics or coding. 

The goal is that I give the model one dataset and a json file d
escribing the dataset, and then by asking naïve questions like 'what is the evolution of revenues for the enterprise Goo
gle, Facebook and Microsoft over the last 5 years', it gives me a kind of dashboard or some graphics with their explicat
ions.

I can use chatGPT-4 for this project and I am going to try the GPT builder, but this is not sufficient. I need to
 explore a bit more the capabilities of LLM on that, so I am going to have an AWS machine to run whatever I want on it. 
Can you guys help me build the stack for that project?

I was thinking of a model expert on code generation to generate 
the graph, but it also must be able to analyse graphics. Also, I heard about Langchain but never used it, but I think it
 can be useful to feed my LLM with the json files describing my datasets. And finally for the I, I heard about private G
PT but I don't know if it works for my case where I need to build a context for my LLM. So maybe Gradio should do the wo
rk?

Thanks a lot, and if my project works I'll share it on github!
```
---

     
 
all -  [ How to replace/stuff the content inside the document in QAReteriver with a map-reduce chain? ](https://www.reddit.com/r/OpenAI/comments/1afe69n/how_to_replacestuff_the_content_inside_the/) , 2024-02-01-0910
```
I am using LangChain QA Retrieval using a map-reduce chain. I want to replace/ stuff the documents received through retr
iever to make my answers better. But I am not able to figure out the way.  


   `question_prompt = PromptTemplate.from_
template('''Check the summary to tell how it is answering the question. You can just say that it doesn't answer the ques
tion directly.`  


`{context}`   
   
`Original question: {question}''')`

  
 `# Loading the Annoy DB from disk.`  
`v
ectordb = Annoy.load_local(persist_directory, embeddings=embedding)`  
`combine_custom_prompt = PromptTemplate.from_temp
late('''Out of these summaries. If you don't know the answer, just say that you don't know. Don't try to make up an answ
er.`  
`QUESTION IS: {question}`   
`=========`   
 `{summaries}`   
`=========`   
`FINAL ANSWER:`  
 `''')`  
`chain_t
ype_kwargs = {`  
 `'verbose': True,`  
 `'question_prompt': question_prompt,`  
 `'combine_prompt': combine_custom_prom
pt,`  
 `'combine_document_variable_name': 'summaries',`  
 `'map_reduce_document_variable_name': 'context',`  
`}`  
`r
etriever = vectordb.as_retriever(search_kwargs={'k': 10})`  
 `print('Type of retriever', type(retriever))`  
`refine = 
RetrievalQA.from_chain_type(llm=OpenAI(),`  
`chain_type='map_reduce',`  
`return_source_documents=True,`  
`chain_type_
kwargs=chain_type_kwargs,`  
`retriever=retriever,`  
`verbose=True)`  
 `print(refine('Random Question'))`  

```
---

     
 
all -  [ How to replace/stuff the content inside the document in QAReteriver with a map-reduce chain? ](https://www.reddit.com/r/LangChain/comments/1afe337/how_to_replacestuff_the_content_inside_the/) , 2024-02-01-0910
```
I am using LangChain QA Retrieval using map-reduce chain. I want to replace/ stuff the documents received through retrie
ver to make my answers better. But I am not able to figure out the way.

   `question_prompt = PromptTemplate.from_templ
ate('''Check the summary to tell how it is answering the question. You can just say that it doesn't answer the question 
directly.`  


`{context}`   
   
`Original question: {question}''')`

  
 `# Loading the Annoy DB from disk.`  
`vector
db = Annoy.load_local(persist_directory, embeddings=embedding)`  
`combine_custom_prompt = PromptTemplate.from_template(
'''Out of these summaries. If you don't know the answer, just say that you don't know. Don't try to make up an answer.` 
 
`QUESTION IS: {question}`   
`=========`   
 `{summaries}`   
`=========`   
`FINAL ANSWER:`  
 `''')`  
`chain_type_k
wargs = {`  
 `'verbose': True,`  
 `'question_prompt': question_prompt,`  
 `'combine_prompt': combine_custom_prompt,` 
 
 `'combine_document_variable_name': 'summaries',`  
 `'map_reduce_document_variable_name': 'context',`  
`}`  
`retrie
ver = vectordb.as_retriever(search_kwargs={'k': 10})`  
 `print('Type of retriever', type(retriever))`  
`refine = Retri
evalQA.from_chain_type(llm=OpenAI(),`  
`chain_type='map_reduce',`  
`return_source_documents=True,`  
`chain_type_kwarg
s=chain_type_kwargs,`  
`retriever=retriever,`  
`verbose=True)`  
 `print(refine('Random Question'))`
```
---

     
 
all -  [ Cleaner memory handling in LCEL ](https://www.reddit.com/r/LangChain/comments/1afdjc2/cleaner_memory_handling_in_lcel/) , 2024-02-01-0910
```
I'm quite new to LangChain, trying it out to see what all the fuzz is about. I recently followed the [Adding memory cook
book](https://python.langchain.com/docs/expression_language/cookbook/memory) from the docs. I'm running it inside a simp
le while loop to provide consecutive inputs to the chain. 

Is there any way to update the memory inside the chain? I do
n't much care for the 

    memory.save_context(inputs, {'output': response.content})

step outside of the chain. That s
eems to go against the whole point of containing everything LLM related inside the chain. Or am I missing something?
```
---

     
 
all -  [ Langchaingo feedbacks ](https://www.reddit.com/r/golang/comments/1af94w1/langchaingo_feedbacks/) , 2024-02-01-0910
```
Is anyone using langchaingo in prod?
I'm planning a new project for work and I'm worried that langchaingo is not at the 
same maturity level as python langchain.
Does anyone have feedbacks?
I just want to avoid to start a new codebase in Gol
ang and then have to rewrite the project in Python especially because this is for work.
```
---

     
 
all -  [ I cant resolve some dependency issues with Pinecone ](https://www.reddit.com/r/LangChain/comments/1af7rrl/i_cant_resolve_some_dependency_issues_with/) , 2024-02-01-0910
```
I am having problems with using the newest version of langchain with Pinecone.

I have conflicting dependencies: 

    [
...] Directory
    ├─┬ @langchain/pinecone@0.0.1
    │ └── @pinecone-database/pinecone@2.0.1 deduped
    ├── @pinecone-d
atabase/pinecone@2.0.1
    └─┬ langchain@0.1.10
      ├─┬ @langchain/community@0.0.22
      │ └── @pinecone-database/pin
econe@2.0.1 deduped invalid: '^1.1.0' from 
    node_modules/langchain/node_modules/@langchain/community
      └── @pine
cone-database/pinecone@2.0.1 deduped

As you can see @lanchain/community conflicts with everything.
 

But i have been l
ooking everywhere to try to figure out how to remove or workaround @langchain/community successfully. 

 
I'm finding it
 difficult since it is a internal dependency of langchain.

 
Can't really think of anywhere else I havent already tried
 to find a solution.

 
Anyone here have experience with this?
```
---

     
 
all -  [ Document Search Tool ](https://www.reddit.com/r/vectordatabase/comments/1af65xc/document_search_tool/) , 2024-02-01-0910
```
I am looking for a tool to efficiently search my documents (pure text documents) and be presented ONLY the source snippe
ts found. Even better when I can jump right into the document. 

I have seen many many tools where a chat bot gives you 
the answer, but this is not what I needed. I would like to have only the snippets from my document and this I have not f
ound. 

I used
- Anything LLM
- GPT-4 & LangChain

But they always have an ai assistant, and even though I know how to p
rogram well, I prefer an end to end solution which I do not need to modify and has a good ui. It can be payed. 

Does an
yone know of such a tool? It does not need to use vector search, as long as the results are good.
```
---

     
 
all -  [ Best Local LLM API hosts for production ](https://www.reddit.com/r/LocalLLaMA/comments/1af5x3b/best_local_llm_api_hosts_for_production/) , 2024-02-01-0910
```
I was wondering what everyone else uses to host there Local LLMs for API calls. I have used Ollama + LiteLLM and text-ge
nerator-webUI's built in API hosts, but I need something that works well with langchain or llamaIndex. I have not found 
a good tutorial or example that connect a local llm to llamaindex over an API.
```
---

     
 
all -  [ creating documents based on an example ](https://www.reddit.com/r/LanguageTechnology/comments/1af0ubt/creating_documents_based_on_an_example/) , 2024-02-01-0910
```
hello , I am trying to generate certain types of documents(reports) based on an example , I need the model to understand
 the structure of the examples then produce a document(section by section) with similar structure and info from the exam
ples but tailored to my case.  


I used gpt3.5 and 4 , fine tuned 3.5 on the examples and used langchain with chromadb 
 
I always would get non satisfactory answers , like i would ask for a certain section then it will write me nothing or 
write me another section or something that is not related ,   
i would be grateful if anyone has an advice for me , than
k you in advance
```
---

     
 
all -  [ Got a shoutout from an AI unicorn. ](https://www.reddit.com/r/Substack/comments/1aeyrf7/got_a_shoutout_from_an_ai_unicorn/) , 2024-02-01-0910
```
This is more of a yeah success than a questions or a lessons learned. Well, there is a bit of a lessons learned wrapped 
into it. 

Here we go. Langchain mentioned my substack on LinkedIn yesterday. [https://www.linkedin.com/posts/langchain\
_code-clinic-searching-youtube-with-langchain-activity-7157779744799789056-X7f\_?utm\_source=share&utm\_medium=member\_d
esktop](https://www.linkedin.com/posts/langchain_code-clinic-searching-youtube-with-langchain-activity-71577797447997890
56-X7f_?utm_source=share&utm_medium=member_desktop)

Who is Langchain? Langchain is one of the leading generative AI / a
utonomous agents unicorns in the world.

How did it get to this? I wrote the article, messaged their team, and got menti
oned. Simple. Maybe I got lucky.

T
```
---

     
 
all -  [ get_openai_callback not working when using Agent Executor after updating to latest version of Langch ](https://www.reddit.com/r/LangChain/comments/1aey6gi/get_openai_callback_not_working_when_using_agent/) , 2024-02-01-0910
```
### Description

I'm trying to use the get\_openai\_callback from langchain\_community.callbacks to get the number of to
ken and costs incurred in using the agent but I am getting zero on everything, as you can see here when I print.

&#x200
B;

https://preview.redd.it/9lbv5ocaymfc1.png?width=412&format=png&auto=webp&s=3d7282b8c88c39bdacf48a4a6ad867c0fdc574bd


I have also set up a custom callback handler to go deep into the issue and what I found is that ChatOpenAI from langcha
in\_openai does not call ainvoke as ChatOpenAI langchain.chat\_models did.

THank you for your help

### Code

    impor
t os
    import traceback
    
    from typing import Any, Dict, List, Optional
    from uuid import UUID
    
    from 
langchain_community.callbacks import get_openai_callback
    from langchain_core.agents import AgentFinish
    from lang
chain_openai import ChatOpenAI
    from langchain.prompts import PromptTemplate
    from langchain.tools.render import r
ender_text_description
    from langchain.agents.format_scratchpad import format_log_to_str
    from langchain.agents.ou
tput_parsers import ReActSingleInputOutputParser
    from langchain.schema import HumanMessage, LLMResult
    from langc
hain.callbacks.base import AsyncCallbackHandler
    from langchain.agents import AgentExecutor
    
    from app.service
s.llm.prompt import prompt_raw
    from app.services.llm.tools.build_tools import tools
    from app.classes.CustomBuffe
r import CustomConversationBufferMemory
    
    
    memory = CustomConversationBufferMemory(memory_key='chat_history',
 return_messages=True)
    
    
    class MyCustomAsyncHandler(AsyncCallbackHandler):
        async def on_llm_end(self
, response: LLMResult, **kwargs: Any) -> None:
            '''Run when chain ends running.'''
            print('RESPONS
E: ', response)
            print('Hi! I just woke up. Your llm is ending')
    
    
    async def ask_assistant(input:
 str) -> str:
        prompt = PromptTemplate.from_template(prompt_raw)
    
        prompt = prompt.partial(
          
  language='Spanish',
            tools=render_text_description(tools),
            tool_names=', '.join([t.name for t i
n tools]),
        )
    
        llm = ChatOpenAI(
            temperature=0,
            model_name='gpt-4',
         
   openai_api_key=os.environ['OPENAI_API_KEY'],
            callbacks=[MyCustomAsyncHandler()],
        )
    
        l
lm_with_stop = llm.bind(stop=['\nObservation'])
    
        agent = (
            {
                'input': lambda x: 
x['input'],
                'agent_scratchpad': lambda x: format_log_to_str(x['intermediate_steps']),
                'c
hat_history': lambda x: x['chat_history'],
            }
            | prompt
            | llm_with_stop
            | 
ReActSingleInputOutputParser()
        )
    
        agent_executor = AgentExecutor(
            agent=agent,
         
   tools=tools,
            verbose=True,
            memory=memory,
            max_execution_time=60,
            hand
le_parsing_errors=True,
        )
    
        with get_openai_callback() as cb:
            clara_ai_resp = await agent
_executor.ainvoke({'input': input})
            clara_ai_output = clara_ai_resp['output']
    
            print('CB: ',
 cb)
    
            return clara_ai_output, input, cb

&#x200B;
```
---

     
 
all -  [ Overwhelmed : Need advice ](https://www.reddit.com/r/csMajors/comments/1aexnzn/overwhelmed_need_advice/) , 2024-02-01-0910
```
So I am international students at mid level university in the US with good experience working at a Product based company
 back in my home country. I used to think my experience is good enough to quickly land me an internship or a full-time j
ob here.

Last 6 months have been went by adjusting, applying for 100s of jobs daily only to realise nothing is working.


I’ve realised there a lot of areas for improvement in my case which can help me.

1. Learning about LLMs, Gen AI and L
angchain (I have 3 years of experience in NLP and AWS but never worked on these advanced models)

2. Leetcode to improve
 python skills

3. Work on SQL and Tableau knowledge (my ultimate goal is to be in the NLP field but right now wanted a 
job ASAP so thought of learning it because it will open doors to many more job opportunities)

4. Work on projects using
 newer technologies.

5. Networking with people on LinkedIn

6. Applying for 20+ jobs daily

7. Complete certifications 
AWS, Tableau

I’ve realised doing this is definitely going to be a task considering classes have started again and it go
ing to be difficult to do all of this together making me feel quite overwhelmed.


How are you guys managing your time?


What do you think should be the right approach to go forward?
```
---

     
 
all -  [ In the era of GPT, building an effective word similarity search in 2023 ](https://www.reddit.com/r/LangChain/comments/1aevsuu/in_the_era_of_gpt_building_an_effective_word/) , 2024-02-01-0910
```
Hello everyone,

I am currently tackling a project that involves a list of various brand names within a specific domain.
 For instance:

`domain_names = ['xyz', 'yza', 'tra', 'world']`

My goal is to develop a search s capable of analyzing w
ord similarity. Specifically, the system should accept a word and return the top 'k' words that are most similar to it. 
I have experimented with OpenAI embeddings, particularly the latest Embedding Version 3 (3072 dimensions), but the resul
ts have been unsatisfactory.

Could someone suggest the most effective approaches for searching word-level similarities 
?In the era of GPT, Would it be advisable to train my own Word2Vec model?
```
---

     
 
all -  [ Load a recipe dataset with Foreign Tables and analyze it using LLMs with Embedded Python (Langchain  ](https://www.reddit.com/r/intersystems/comments/1aeuop1/load_a_recipe_dataset_with_foreign_tables_and/) , 2024-02-01-0910
```
📚 Dive into the world of #DataScience and language model with our latest article! Learn how to load a recipe dataset int
o #InterSystemsIRIS using Foreign Tables and analyze it using #LLMs with Embedded #Python 👇

[https://community.intersys
tems.com/post/load-recipe-dataset-foreign-tables-and-analyze-it-using-llms-embedded-python-langchain-openai](https://com
munity.intersystems.com/post/load-recipe-dataset-foreign-tables-and-analyze-it-using-llms-embedded-python-langchain-open
ai)

Explore the powerful combination of Langchain and OpenAI for a unique and insightful journey!

&#x200B;

https://pr
eview.redd.it/uzt2iz8h9mfc1.jpg?width=1920&format=pjpg&auto=webp&s=b849b2a95d204b24267d61ee7351db4b97f3be7e
```
---

     
 
all -  [ Load a recipe dataset with Foreign Tables and analyze it using LLMs with Embedded Python (Langchain  ](https://www.reddit.com/r/u_intersystemsdev/comments/1aeuo1o/load_a_recipe_dataset_with_foreign_tables_and/) , 2024-02-01-0910
```
📚 Dive into the world of #DataScience and language model with our latest article! Learn how to load a recipe dataset int
o #InterSystemsIRIS using Foreign Tables and analyze it using #LLMs with Embedded #Python 👇

https://community.intersyst
ems.com/post/load-recipe-dataset-foreign-tables-and-analyze-it-using-llms-embedded-python-langchain-openai

Explore the 
powerful combination of Langchain and OpenAI for a unique and insightful journey!

&#x200B;

https://preview.redd.it/595
de18c9mfc1.jpg?width=1920&format=pjpg&auto=webp&s=0cb3050272392d7c6d1cbe6ef177126a2089cfaa
```
---

     
 
all -  [ Document Search And Retrieval Using RAG - powered by Langchain ](https://www.reddit.com/r/LangChain/comments/1aet9j9/document_search_and_retrieval_using_rag_powered/) , 2024-02-01-0910
```
[This Studio](https://lightning.ai/lightning-ai/studios/document-search-and-retrieval-using-rag) is a minimal reproducib
le pipeline to retrieve semantically similar documents based on the input query. The next step for this Studio involves 
connecting an LLM and engaging in a chat with your document through the retrieval pipeline.

***The retriever pipeline i
n this Studio is composed of the following components:***

* **Document Loader**:  Load the document (.txt, .pdf, .docx,
 .ppt) and perform text cleaning 
* **Text Splitter**: Split the document texts into multiple chunks 
* **Embedding Gene
ration**: Generate vector representation of text chunks
* **Vector database**: Embed and store each of the chunks and st
ore in a vector DB 
* **Retriever and Reranking**: Retrieve data based on query similarity

&#x200B;

https://preview.re
dd.it/idqetsa1zlfc1.png?width=3058&format=png&auto=webp&s=2a1b47eb6c477e7762bc745875cda45e9d08500e

[https://lightning.a
i/lightning-ai/studios/document-search-and-retrieval-using-rag](https://lightning.ai/lightning-ai/studios/document-searc
h-and-retrieval-using-rag)
```
---

     
 
all -  [ [Langchain] Besoin d'aide pour améliorer le chiffon ](https://www.reddit.com/r/redditenfrancais/comments/1aet2g4/langchain_besoin_daide_pour_améliorer_le_chiffon/) , 2024-02-01-0910
```
Bonjour à tous, je commence juste par le chiffon.

Je souhaite récupérer les informations sur les réglementations de con
struction (hauteur maximale, surface, etc.) des PDF à l'aide d'un LLM.

Le PDFS contient à la fois du texte et des donné
es. J'utilise actuellement PYPDFLoader de Langchain pour charger les PDF. Diffusion à l'aide de la division récursive de
s caractères, intégrant en utilisant une AI ouverte et en la stockant dans Chroma DB.
 

Parfois, le LLM ne récupére pas
 correctement les informations. Je ne sais pas si c'est à cause de l'analyse des PDF.

Toute aide à l'amélioration du sy
stème est grandement appréciée. Merci.

Traduit et reposté à partir de la publication 1abuv1f de la communauté langchain
. Pour retrouver la publication originale, insérez l'id de la publication après 'reddit.com/'
```
---

     
 
MachineLearning -  [ [P]: Anukool: My job hunting assistant ](https://www.reddit.com/r/MachineLearning/comments/1adu3tw/p_anukool_my_job_hunting_assistant/) , 2024-02-01-0910
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

     
 
MachineLearning -  [ New Data API for Astra [N] ](https://www.reddit.com/r/MachineLearning/comments/199uobn/new_data_api_for_astra_n/) , 2024-02-01-0910
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

     
 
MachineLearning -  [ [D] While using function calling or tools on openai or langchain, does openai have access to the dat ](https://www.reddit.com/r/MachineLearning/comments/199t8be/d_while_using_function_calling_or_tools_on_openai/) , 2024-02-01-0910
```
I am working on a client project and I am using langchain's tools and agents. I want to know if the data is getting pass
ed to openai or is it just like that - Output of one function is being directly passed to the second function with the k
nowledge of openai.
```
---

     
 
MachineLearning -  [ [D] Code vs JSON output for LLM agents? Frameworks like LangChain rely on LLMs responding with JSON  ](https://www.reddit.com/r/MachineLearning/comments/197f416/d_code_vs_json_output_for_llm_agents_frameworks/) , 2024-02-01-0910
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

     
 
MachineLearning -  [ [D] Are Custom LLM RAG apps going to become redundant? ](https://www.reddit.com/r/MachineLearning/comments/1929n4f/d_are_custom_llm_rag_apps_going_to_become/) , 2024-02-01-0910
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

     
 
MachineLearning -  [ [P] An open-source project for deploying local models ](https://www.reddit.com/r/MachineLearning/comments/18zkm5m/p_an_opensource_project_for_deploying_local_models/) , 2024-02-01-0910
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

     
 
deeplearning -  [ DSPy Explained! ](https://www.reddit.com/r/deeplearning/comments/1adypks/dspy_explained/) , 2024-02-01-0910
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

     
 
deeplearning -  [ [D] Unleashing the Power of Langchain with Wandb: Revolutionizing Topic Modeling and Evaluation ](https://www.reddit.com/r/deeplearning/comments/191mm83/d_unleashing_the_power_of_langchain_with_wandb/) , 2024-02-01-0910
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

     
