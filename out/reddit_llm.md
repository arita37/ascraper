 
all -  [ Use cases for small models? ](https://www.reddit.com/r/LangChain/comments/1gpy44x/use_cases_for_small_models/) , 2024-11-13-0912
```
Has anyone found use cases for the small llm models? Think in the 3b to 12b range, like llama 3.5 11b, llama 3.2 3b or m
istral nemo 12b.

So far, for everything I tried, those models are essentially useless. They don’t follow instructions a
nd answers are extremely unreliable.

Curious what the purpose/use cases are for these models.

```
---

     
 
all -  [ Open sourcing a web ai agent framework I've been working on called Dendrite ](https://www.reddit.com/r/AI_Agents/comments/1gpubkj/open_sourcing_a_web_ai_agent_framework_ive_been/) , 2024-11-13-0912
```
Hey! I've been working on a project called Dendrite which simple framework for interacting with websites using natural l
anguage. Interact and extract without having to find brittle css selectors or xpaths like this:

    browser.click(“the 
sign in button”)

For the developers who like their code typed, specify what data you want with a Pydantic BaseModel and
 Dendrite returns it in that format with one simple function call. Built on top of playwright for a robust experience. T
his is an easy way to give your AI agents the same web browsing capabilities as humans have. Integrates easily with fram
eworks such as  Langchain, CrewAI, Llamaindex and more. 

We are planning on **open sourcing** everything soon as well s
o feel free to reach out to us if you’re interested in contributing!

Here is a short demo video: Kan du posta denna på 
Reddit med Fishards kontot? [https://www.youtube.com/watch?v=EKySRg2rODU](https://www.youtube.com/watch?v=EKySRg2rODU)


Github: [https://github.com/dendrite-systems/dendrite-python-sdk](https://github.com/dendrite-systems/dendrite-python-sd
k)

* **Authenticate Anywhere**: Dendrite Vault, our Chrome extension, handles secure authentication, letting your agent
s log in to almost any website.
* **Interact Naturally**: With natural language commands, agents can click, type, and na
vigate through web elements with ease.
* **Extract and Manipulate Data**: Collect structured data from websites, return 
data from different websites in the same structure without having to maintain different scripts.
* **Download/Upload Fil
es**: Effortlessly manage file interactions to and from websites, equipping agents to handle documents, reports, and mor
e.
* **Resilient Interactions**: Dendrite's interactions are designed to be resilient, adapting to minor changes in webs
ite structure to prevent workflows from breaking
* **Full Compatibility**: Works with popular tools like LangChain and C
rewAI, letting you seamlessly integrate Dendrite’s capabilities into your AI workflows.
```
---

     
 
all -  [ RAG-Enhanced Chatbot Application | AI-Powered Document Retrieval & Chatbot Demo | LangChain & OpenAI ](https://youtu.be/MZDiMMai6zo?si=AWwvpwuB9Ozm9JI9) , 2024-11-13-0912
```

```
---

     
 
all -  [ Langgraph vs langchain vs crewai for chatbot ](https://www.reddit.com/r/crewai/comments/1gpth7y/langgraph_vs_langchain_vs_crewai_for_chatbot/) , 2024-11-13-0912
```
Hello

I am building a RAG chatbot. I mostly use langchain and openai for this stuff. However this chatbot will start wi
th RAG but will have other features like document understanding and etc down the road. So now I'm wondering what I shoul
d be using
I have narrowed it down to these 
- langchain
- crewai
- langgraph

I've been playing with crewai but I still
 don't know how to use it as chatbot. Langchain is easy but I fear it does not have those agentic flows. Langgraph feels
 too young and for some reason has way less stars than crew.ai
```
---

     
 
all -  [ # LANGGRAPH_API_URL=  Where can I find this? - open canvas ](https://www.reddit.com/r/LangChain/comments/1gpr4kl/langgraph_api_url_where_can_i_find_this_open/) , 2024-11-13-0912
```
I installed supabase, postgre, docker and git cloned the open-canvas.

I've had everything running on my server but when
 I login it says 'no thread exists' or a similar error.  The logins work, everything loads, but trying to use any functi
on gets a thread error.

I think I've tracked it down to I never setup a langgraph.  In my .env I never set langgraph\_a
pi\_url   have no clue where to get the langgraph\_api\_url.

I have a langsmith account, I was planning to use their cl
oud for setup and production for my team.  

# LangGraph PlatformOne-click deployments of LangGraph applications

I clic
k on Langgraph deployment on the left in their website, get the screen.  
**LangGraph PlatformOne-click deployments of L
angGraph applications**

**LangGraph Studio**

**All LangSmith users on Plus, Premier, Startup, or Enterprise plans can 
now access LangGraph Platform for free in its beta.**

Then I can't figure out what to do or where to get  

\# LANGGRAP
H\_API\_URL=

If I Langgraph studio at the top right it asks for my local endpoint, I don't know what to put in there.


\--  
I could try to host langgraph cli locally, but I'm not sure if I should.

AWS, EC2, Almalinux 8.10
```
---

     
 
all -  [ Please review my resume for IT jobs ](https://www.reddit.com/r/Netherlands/comments/1gppokm/please_review_my_resume_for_it_jobs/) , 2024-11-13-0912
```
https://preview.redd.it/4arqbx586i0e1.png?width=756&format=png&auto=webp&s=932cd0c158a36fb2b238181cfe8662abfac7b7ee


```
---

     
 
all -  [ No interviews or callbacks… very sad with no idea as to what I’m missing no ](https://i.redd.it/2jb0276i2i0e1.jpeg) , 2024-11-13-0912
```
Hey y’all, I graduated back in December and I’m still looking for a job in AI or even the DS fields.

I have went throug
h several rounds of revising my resume and I’m not super sure what I am missing. I am also posting since here the CSCare
erQuestions has a karma limit that I can never get beyond (I’m not really active enough on Reddit).

Recently I have bee
n playing with larger LLMs and more services like Qwen and QDRant, so I plan on adding that to my resume.

I also have a
 shorter version of my resume where I remove my skills section and short my work history bulletin points. The above scre
enshot is my longer resume.

I would appreciate any advice on my resume if there are any blatant issues. I should be cle
ar that I am a US citizen.
```
---

     
 
all -  [ Introducing Langchian-Beam  ](https://www.reddit.com/r/apachebeam/comments/1gpoya3/introducing_langchianbeam/) , 2024-11-13-0912
```
Hi all, I've been working on a Apache beam and langchian integration and would like to share it here.

Apache beam is a 
great model for data processing. It provides abstractions to create data processing logic and apply it on data in batch 
and stream processing pipelines 

langchian-beam integrates LLMs into the apache beam pipeline using langchian to use LL
Ms capabilities for data processing, transformations and RAG. 

Repo link - https://github.com/Ganeshsivakumar/langchain
-beam
 
```
---

     
 
all -  [ Introducing Langchian-Beam  ](https://www.reddit.com/r/LangChain/comments/1gpoeu8/introducing_langchianbeam/) , 2024-11-13-0912
```
Hi all, I've been working on a Apache beam and langchian integration and would like to share it here.

Apache beam is a 
great model for data processing. It provides abstractions to create data processing logic as components that can be appl
ied on data in batch and stream processing pipelines 

langchian-beam integrates LLMs into the apache beam pipeline usin
g langchian to use LLMs capabilities for data processing and transformations and RAG. 

Repo link - https://github.com/G
aneshsivakumar/langchain-beam
 
```
---

     
 
all -  [ Please review my resume for Data Engineering/Data Scientist/Analyst roles ](https://www.reddit.com/r/germany/comments/1gpll1b/please_review_my_resume_for_data_engineeringdata/) , 2024-11-13-0912
```
https://preview.redd.it/fc2p3uakah0e1.png?width=762&format=png&auto=webp&s=6837f64c3be0a24092ff29f80af48b7b6159fbbd


```
---

     
 
all -  [ Please review my resume -Data Engineer/Data Scientist/Analyst ](https://www.reddit.com/r/developersIndia/comments/1gpkbal/please_review_my_resume_data_engineerdata/) , 2024-11-13-0912
```
[Roast my resume](https://preview.redd.it/xxtq3mkazg0e1.png?width=762&format=png&auto=webp&s=744ec1324b388543df4b599e1c5
11fbc3fe017bf)
```
---

     
 
all -  [ How to Use Meta's LLaMA 3.2 Model in LM Studio for RAG with LangChain? ](https://www.reddit.com/r/techsupport/comments/1gpk5js/how_to_use_metas_llama_32_model_in_lm_studio_for/) , 2024-11-13-0912
```
Hi everyone,



I’m new to using Meta’s LLaMA models and want to explore using the LLaMA 3.2 8B model for a retrieval-au
gmented generation (RAG) application with LangChain in Python. I’m comfortable working with GPT models, but I’m not sure
 how to start with LLaMA, especially within LM Studio.



Can anyone provide a step-by-step guide or point me to resourc
es on how to:



1. Load and configure the LLaMA model in LM Studio?

2. Connect the model to LangChain for a basic RAG 
workflow?



I’d appreciate any guidance on installation, setup, or potential limitations with the LLaMA 3.2 model in LM
 Studio. Thanks so much!
```
---

     
 
all -  [ What platform/system/language to use for orchestrating multiple AI agents for a thesis project? ](https://www.reddit.com/r/Rag/comments/1gpj6hb/what_platformsystemlanguage_to_use_for/) , 2024-11-13-0912
```
Hi everyone!

I am currently working on my thesis assignment. For this research, I am investigating the possibility of c
reating a GraphRAG system that allows citizen developers to ask natural language questions about their Low-Code applicat
ions. 

I already have created a script that transforms an application into a graph database (Neo4J)

To enhance the LLM
 response I aim to create a setup where a user can ask a question in natural language. This question is then sent to an 
AI agent that translates the question into a Cypher query. This query is then sent to the database to retrieve the relev
ant context. The context along with the original question is then sent to another AI agent that uses the retrieved conte
xt as 'truth' and uses that information to answer the original question.

I have seen many debates about using different
 approaches for setting this up such as AutoGPT, Langchain, FlowiseAI etc. However, to me they all seem to do somewhat s
imilar things and their websites are mostly full of marketable hype terms promising to be silver-bullet for any AI probl
em.

Do you guys have any ideas or suggestions? I'm sorry if I made any mistakes or confusing statements I am a student 
that has no real previous experience working with LLMs and AI.

Here is a paper I found that did something similar for P
ython project: [https://www.arxiv.org/pdf/2408.03910](https://www.arxiv.org/pdf/2408.03910) however, they built their ch
atbot using modelscope and therefore a lot of pages are written in manadarin and I can't seem to set it up similarly.

T
hanks!
```
---

     
 
all -  [ Please review my resume - looking for Data Engineering/Data Scientists/Analyst roles ](https://www.reddit.com/r/AWSCertifications/comments/1gpil6u/please_review_my_resume_looking_for_data/) , 2024-11-13-0912
```
https://preview.redd.it/e0cm38tlhg0e1.png?width=762&format=png&auto=webp&s=84fa864272142f8e0c8cef15232a1ddf2fad2af9


```
---

     
 
all -  [ Seeking Collaboration or Guidance with LangChain for Research Project ](https://www.reddit.com/r/askdatascience/comments/1gph87f/seeking_collaboration_or_guidance_with_langchain/) , 2024-11-13-0912
```
I'm currently working on a research project involving LangChain and looking for someone with experience in the framework
 who could answer some questions or potentially collaborate. If you're familiar with LangChain and interested in discuss
ing the project, please reach out!
```
---

     
 
all -  [ Resume review pls. Bad ATS score. Currently in 5th sem. ](https://i.redd.it/j24c14hdxf0e1.png) , 2024-11-13-0912
```
Resume worded scored it 56/100. One thing I know to improve is adding more numbers (x% impact), but not sure where else 
it lacks..
```
---

     
 
all -  [ How can I add a filter to AzureCosmosDB for MongoDB? ](https://www.reddit.com/r/LangChain/comments/1gpec8o/how_can_i_add_a_filter_to_azurecosmosdb_for/) , 2024-11-13-0912
```
Hi all, I am currently using LangChain to implement RAG with Azure CosmosDB for MongoDB. However, I am facing the issue 
of my filter not working. Have tried using both the filter argument for .as\_retriever() and the pre\_filter argument fo
r .similarity\_search(), but to no avail.  
  
Does anyone have any solutions or workaround for that?

    vectorstore =
 AzureCosmosDBVectorSearch.from_connection_string(
                    connection_string=self.uri,
                    n
amespace=self.namespace,
                    embedding=self.embedding_model,
                    index_name = self.index
_name,
                    embedding_key=self.embedding_key
                )
            
            retriever = vecto
rstore.as_retriever(
                    search_kwargs={
                        'k': 15,
                        'filte
r': { 'metadata.username': {'$eq': username}}
                    }
                )
            
            docs = ve
ctorstore.similarity_search(
                query=query,
                k=15,
                pre_filter={'metadata.us
ername': {'$eq': username}},
                score_threshold=0.8
            )


```
---

     
 
all -  [ How to add a filter to Azure CosmosDB for MongoDB? ](https://www.reddit.com/r/AZURE/comments/1gpebv5/how_to_add_a_filter_to_azure_cosmosdb_for_mongodb/) , 2024-11-13-0912
```
Hi all, I am currently using LangChain to implement RAG with Azure CosmosDB for MongoDB. However, I am facing the issue 
of my filter not working. Have tried using both the filter argument for .as\_retriever() and the pre\_filter argument fo
r .similarity\_search(), but to no avail.  
  
Does anyone have any solutions or workaround for that?

    vectorstore =
 AzureCosmosDBVectorSearch.from_connection_string(
                    connection_string=self.uri,
                    n
amespace=self.namespace,
                    embedding=self.embedding_model,
                    index_name = self.index
_name,
                    embedding_key=self.embedding_key
                )
            
            retriever = vecto
rstore.as_retriever(
                    search_kwargs={
                        'k': 15,
                        'filte
r': { 'metadata.username': {'$eq': username}}
                    }
                )
            
            docs = ve
ctorstore.similarity_search(
                query=query,
                k=15,
                pre_filter={'metadata.us
ername': {'$eq': username}},
                score_threshold=0.8
            )

  

```
---

     
 
all -  [ Python langchain objects sent to js frontend - serialising and deserialising ](https://www.reddit.com/r/LangChain/comments/1gpdync/python_langchain_objects_sent_to_js_frontend/) , 2024-11-13-0912
```
Hey guys! What's the recommended workflow to serialise a python langchain object on the backend (in my case a list of do
cuments) and then pick them back up in a ts front end? I can find api documentation on serialising Python langchain obje
cts (.dumps) but not for JavaScript. Anyone know?
```
---

     
 
all -  [ Need help in integrating HuggingFace with langchain ](https://www.reddit.com/r/LangChain/comments/1gpdu61/need_help_in_integrating_huggingface_with/) , 2024-11-13-0912
```
i want to use a vision model from huggingface with my langchain project  i implemented as shown below  
  
`llm` `=` `Hu
ggingFacePipeline``.from_model_id(`  
`model_id='5CD-AI/Vintern-3B-beta',`  
`task='Visual Question Answering',`  
`pipe
line_kwargs=dict(`  
`max_new_tokens=512,`  
`do_sample=False,`  
`repetition_penalty=1.03,`  
`),`  
`)``chat_model` `=
` `ChatHuggingFace(llm=llm)`  
  
*but i got the error below*  


  
`ValueError: Got invalid task Visual Question Answe
ring, currently only ('text2text-generation', 'text-generation', 'summarization', 'translation') are supported`  
  
Any
 help is appreciated 🙌🏻  
  

```
---

     
 
all -  [ A list for open-source LLM applications that are based on Next.js. ](https://www.reddit.com/r/nextjs/comments/1gpamt0/a_list_for_opensource_llm_applications_that_are/) , 2024-11-13-0912
```
Here are some high-starred open-source projects that integrate Large Language Models (LLMs) with Next.js(Please complete
 the list if you know another one):

1. **nextjs-ollama-llm-ui**  
   A fully-featured, beautiful web interface for Olla
ma LLMs, built with Next.js. It offers an intuitive UI inspired by ChatGPT and supports local storage of chats.  
   Git
Hub: [https://github.com/jakobhoeg/nextjs-ollama-llm-ui](https://github.com/jakobhoeg/nextjs-ollama-llm-ui)

2. **nextjs
-vllm-ui**  
   A web interface for vLLM, designed with Next.js. It provides a responsive and user-friendly platform for
 interacting with vLLM models.  
   GitHub: [https://github.com/yoziru/nextjs-vllm-ui](https://github.com/yoziru/nextjs-
vllm-ui)

3. **langfuse-llm-ai-nextjs**  
   An open-source LLM engineering platform offering observability, metrics, ev
aluations, prompt management, and more. It integrates with various LLMs and is built using Next.js.  
   GitHub: [https:
//github.com/anhgeeky/langfuse-llm-ai-nextjs](https://github.com/anhgeeky/langfuse-llm-ai-nextjs)

4. **llm_on_nextjs_pr
oject**  
   A project that combines Next.js with DuckDB, deck.gl, and LLMs to create a versatile application. It includ
es integrations for data visualization and natural language processing.  
   GitHub: [https://github.com/Prajwal-Amarava
ti/llm_on_nextjs_project](https://github.com/Prajwal-Amaravati/llm_on_nextjs_project)

5. **llm-answer-engine**  
   Ins
pired by Perplexity AI, this project builds an answer engine leveraging Groq, Mistral AI's Mixtral, Langchain.JS, Brave 
Search, Serper API, and OpenAI, all integrated within a Next.js framework.  
   GitHub: [https://github.com/developersdi
gest/llm-answer-engine](https://github.com/developersdigest/llm-answer-engine)

```
---

     
 
all -  [ How to make my first chat bot app?  ](https://www.reddit.com/r/AskProgramming/comments/1gp9pd4/how_to_make_my_first_chat_bot_app/) , 2024-11-13-0912
```
So hi everyone
I want to build a new projet for a hackathon
It's for an education purpose 
I'm good at web development 

And i want to build a chat bot app that help users to get a best answers for there questions. 
I want to Know the techno
logies that i need to work with 
For the front end i want to work with react

I asked some friends the say i need to use
 langchain and cromadb
 Because i need to provide an external data that i will scrap it form the web
I want the model to
 answer me based on the data that i will give it. 

Some said use lama 3 it's already holster on Nvidia. 
Some said i ca
n use just a small model from hanging face. 
Some sait make fine-tuning i don't know what it's? 
Pls help me. With the b
est path to get the best results. 
```
---

     
 
all -  [ Best AI Image generator?  ](https://www.reddit.com/r/LangChain/comments/1gp4waz/best_ai_image_generator/) , 2024-11-13-0912
```
Hello everyone, I hope you guys are doing great. 

I am searching for best / very good / one of the best AI image genera
tor. 

Please Advise 

```
---

     
 
all -  [ [3 YoE] Data Scientist with masters degree looking to get resume reviewed to land better opportuniti ](https://www.reddit.com/r/EngineeringResumes/comments/1gp0lqi/3_yoe_data_scientist_with_masters_degree_looking/) , 2024-11-13-0912
```
Hi everyone, I have 3 YOE and 8 MOE of relevant internship (i say relevant cuz my other internships/part-time jobs were 
irrelevant), I am currently working as DS at a startup which does not pay too well (that's why the job switch). I am loo
king for a Data Scientist role so please give your suggestions accordingly.

I am looking for honest opinions on how I c
an improve my resume, what I should include or remove, the order of sections, any other sections that I should insert, s
tructure and wordings of present structure etc. This resume did help me get interviews at Intuit, The Washington Post, A
WS and Meta, but lately I have not been able to grab any calls.

Your help is deeply appreciated and I look forward to t
he roast!

https://preview.redd.it/pg8ii8y2pb0e1.png?width=5100&format=png&auto=webp&s=265ab3ee845f27cb6db7601c1de768fb1
e84bf60


```
---

     
 
all -  [ RAG + Ai Tools + limited options ](https://www.reddit.com/r/n8n/comments/1goz3fe/rag_ai_tools_limited_options/) , 2024-11-13-0912
```
I'm using an AI Agent that leverages RAG (PDFs from Google Drive + Pinecone) to answer questions about my business, and 
then makes an HTTP request based on the user's choices.

If it were a hotel, for example:

* **Housekeeping**: (towels, 
soap, shampoo, etc.)
* **Maintenance**: (broken shower, leaking air conditioner)
* **Restaurant**
* **Extra services**: 
(spa, massage, tours)

I want each department to receive requests via HTTP, but I have a dilemma: I need to clearly defi
ne which services are available. If a client requests something that housekeeping doesn’t provide, the AI needs to deny 
it, but if it's a valid request, it should accept it automatically. I'm aiming for a simple structure to make future mai
ntenance easier. Do you think I can achieve all this with a single AI agent that understands the context and creates str
aightforward HTTP requests? Or should I use a multi-agent setup?



EDIT: the workflow: 

    {
      'name': 'Gov-Manut
',
      'nodes': [
        {
          'parameters': {
            'options': {
              'presencePenalty': 0.1,
 
             'temperature': 0.1
            }
          },
          'id': '8eb40e35-677f-4966-aed5-86db3344e11c',
     
     'name': 'OpenAI Chat Model',
          'type': '@n8n/n8n-nodes-langchain.lmChatOpenAi',
          'typeVersion': 1,

          'position': [
            1200,
            420
          ],
          'credentials': {
            'openAiAp
i': {
              'id': 'uVbrQPftTD0hZZBu',
              'name': 'OpenAi account key'
            }
          }
     
   },
        {
          'parameters': {},
          'id': '50feef43-6562-4f59-9391-01cd972b76de',
          'name': 'W
indow Buffer Memory',
          'type': '@n8n/n8n-nodes-langchain.memoryBufferWindow',
          'typeVersion': 1.2,
   
       'position': [
            1460,
            380
          ]
        },
        {
          'parameters': {
      
      'name': 'governanca',
            'description': 'nao aprove nada sem confirmacao, sempre tem que pedir confirmaca
o do usuario\n\nresponsável pela organização e suprimentos nos quartos, sem realizar serviços de manutenção. As solicita
ções de governança incluem:\n\nItens de Cama e Conforto:\n\nTravesseiros extras (macios, firmes, hipoalergênicos), cober
tores adicionais, edredons, colchas e protetores de colchão impermeáveis.\nItens de Banho e Higiene:\n\nToalhas extras (
banho, rosto, piso), roupões de banho, chinelos descartáveis, kit dental (escova e pasta), kit de barbear, kit de higien
e feminina, sabonetes e shampoos extras, sabonete líquido, condicionador, loção corporal, touca de banho\nLimpeza diária
 do quarto, arrumação de cama, troca de roupas de cama e toalhas, limpeza de banheiro e reposição de itens como papel hi
giênico e sabonetes.\nNota: Governança não realiza consertos ou reparos de qualquer natureza, como problemas elétricos, 
hidráulicos, ou reparos de móveis — essas solicitações devem ser direcionadas ao setor de manutenção.',
            'lan
guage': 'python',
            'pythonCode': 'print(query)\nreturn str(query)',
            'specifyInputSchema': true,
 
           'schemaType': 'manual',
            'inputSchema': '{\n  \'type\': \'object\',\n  \'properties\': {\n   \n   
 \'pedirConfirmacao\': {\n      \'type\': \'boolean\',\n      \'description\': \'Flag que indica se o agente deve solici
tar uma confirmação do usuário após capturar a intenção inicial.\',\n      \'default\': true\n    },\n    \'confirmacao\
': {\n      \'type\': \'string\',\n      \'description\': \'Confirmação final do usuário após a pergunta: 'Você confirma
 que deseja solicitar [nome do serviço]?'\',\n      \'enum\': [\'sim\', \'nao\']\n    },\n    \'itens\': {\n      \'type
\': \'array\',\n      \'description\': \'Lista de itens de higiene solicitados. A quantidade é obrigatória se houver ite
m pedido.\',\n      \'items\': {\n        \'type\': \'object\',\n        \'properties\': {\n          \'nome\': {\n     
       \'type\': \'string\',\n            \'description\': \'Nome do item de higiene (ex: toalha, sabonete, shampoo)\',\
n            \'minLength\': 1\n          },\n          \'quantidade\': {\n            \'type\': \'integer\',\n          
  \'description\': \'Quantidade do item solicitado\',\n            \'minimum\': 1\n          }\n        },\n        \'re
quired\': [\'nome\', \'quantidade\']\n      }\n    },\n    \'servicos\': {\n      \'type\': \'array\',\n      \'descript
ion\': \'Lista de serviços solicitados, como arrumação ou limpeza. Observações são opcionais.\',\n      \'items\': {\n  
      \'type\': \'object\',\n        \'properties\': {\n          \'tipoServico\': {\n            \'type\': \'string\',\
n            \'description\': \'Tipo de serviço solicitado (ex: 'arrumacao', 'limpeza', 'banheiro')\',\n            \'en
um\': [\'arrumacao\', \'limpeza\', \'banheiro\']\n          },\n          \'observacoes\': {\n            \'type\': \'st
ring\',\n            \'description\': \'Observações extras para o serviço, se necessário\',\n            \'maxLength\': 
500\n          }\n        },\n        \'required\': [\'tipoServico\']\n      }\n    }\n  },\n  \'required\': [\'pedirCon
firmacao\',\'confirmacao\'],\n  \'additionalProperties\': false\n}\n'
          },
          'id': '93d1e0dd-43b5-4045-a
c32-c5019455cc5f',
          'name': 'Governança',
          'type': '@n8n/n8n-nodes-langchain.toolCode',
          'typ
eVersion': 1.1,
          'position': [
            1640,
            380
          ]
        },
        {
          'pa
rameters': {
            'name': 'manutencao',
            'description': 'Responsável exclusivamente pelo reparo e cons
ervação de instalações e equipamentos. Não realiza tarefas de governança, como limpeza ou arrumação.\n\nProblemas Elétri
cos: Conserto de tomadas, interruptores, lâmpadas e equipamentos elétricos, incluindo verificação de circuitos e quadros
.\n\nAr-Condicionado e Aquecimento: Ajustes e consertos em sistemas de ar-condicionado ou aquecimento, incluindo vazamen
tos, ruídos e refrigeração.\n\nEncanamentos e Hidráulica: Solução de vazamentos em pias, chuveiros e vasos, além de dese
ntupimento de ralos e verificação de pressão de água.\n\nMobiliário: Reparo de móveis danificados, como camas e armários
, incluindo portas, gavetas e carpintaria.\n\nVentilação e Exaustão: Manutenção de ventiladores, exaustores e sistemas d
e ventilação de teto e banheiros.\n\nEstrutural: Reparo de paredes, pisos e portas, com verificação de rachaduras, infil
trações e pintura.\n\nSegurança: Verificação de detectores de fumaça, alarmes e fechaduras',
            'language': 'py
thon',
            'pythonCode': 'print(query)\nreturn str(query)',
            'specifyInputSchema': true,
            
'schemaType': 'manual',
            'inputSchema': '{\n  \'type\': \'object\',\n  \'properties\': {\n    \'tipoManutenca
o\': {\n      \'type\': \'string\',\n      \'description\': \'Tipo de serviço de manutenção solicitado\',\n      \'enum\
': [\n        \'eletrico\',\n        \'arCondicionado\',\n        \'hidraulico\',\n        \'mobiliario\',\n        \'ve
ntilacao\',\n        \'estrutural\',\n        \'seguranca\'\n      ]\n    },\n    \'descricao\': {\n      \'type\': \'st
ring\',\n      \'description\': \'Descrição detalhada do problema para auxiliar na execução da manutenção\',\n      \'ma
xLength\': 500\n    },\n    \'observacao\': {\n      \'type\': \'string\',\n      \'description\': \'Observações adicion
ais sobre o problema ou instruções especiais\',\n      \'maxLength\': 400\n    }\n  },\n  \'required\': [\'tipoManutenca
o\', \'descricao\']\n}\n'
          },
          'id': '8bf973fd-a965-4712-b06d-6af5db85a257',
          'name': 'Manute
nção',
          'type': '@n8n/n8n-nodes-langchain.toolCode',
          'typeVersion': 1.1,
          'position': [
    
        1780,
            380
          ]
        },
        {
          'parameters': {
            'options': {
      
        'batchSize': 500
            }
          },
          'id': 'f4e92d01-16ac-4c12-8603-4762ead98d3f',
          'n
ame': 'Embeddings OpenAI',
          'type': '@n8n/n8n-nodes-langchain.embeddingsOpenAi',
          'typeVersion': 1.1,

          'position': [
            760,
            520
          ],
          'credentials': {
            'openAiApi'
: {
              'id': 'uVbrQPftTD0hZZBu',
              'name': 'OpenAi account'
            }
          }
        },

        {
          'parameters': {
            'name': 'pinecone-db',
            'topK': 20
          },
          'id
': '890714be-d289-44a6-bca3-5be905c9615e',
          'name': 'Vector Store Tool',
          'type': '@n8n/n8n-nodes-lang
chain.toolVectorStore',
          'typeVersion': 1,
          'position': [
            880,
            200
          ]

        },
        {
          'parameters': {
            'options': {}
          },
          'id': '4e1e5ea1-a61d-4f
35-8a7b-7a23e3bb85b3',
          'name': 'When chat message received',
          'type': '@n8n/n8n-nodes-langchain.chatT
rigger',
          'typeVersion': 1.1,
          'position': [
            1160,
            0
          ],
          'w
ebhookId': '138731bb-6eec-42ee-b117-f0c8c4549069'
        },
        {
          'parameters': {
            'pineconeIn
dex': {
              '__rl': true,
              'value': 'beach-park',
              'mode': 'list',
              'ca
chedResultName': 'beach-park'
            },
            'options': {}
          },
          'id': 'dc749050-dc89-447d-
93e2-29417e5f4a8c',
          'name': 'Pinecone Vector Store',
          'type': '@n8n/n8n-nodes-langchain.vectorStorePi
necone',
          'typeVersion': 1,
          'position': [
            760,
            360
          ],
          'cr
edentials': {
            'pineconeApi': {
              'id': 'Pqh8uRLOm4TYt21t',
              'name': 'PineconeApi ac
count'
            }
          }
        },
        {
          'parameters': {
            'name': 'Produtos',
        
    'language': 'python',
            'pythonCode': 'return str(query)',
            'specifyInputSchema': true,
       
     'jsonSchemaExample': '{\n  \'type\': \'object\',\n  \'properties\': {\n    \'nome\': {\n      \'type\': \'string\',
\n      \'description\': \'Nome do pacote sendo reservado. Consulte as opções disponíveis na base de dados.\'\n    },\n 
   \'dataReserva\': {\n      \'type\': \'string\',\n      \'description\': \'Data solicitada para a reserva do pacote, p
odendo estar em linguagem natural (ex: 'próxima sexta-feira', 'amanhã'). A IA converterá para o formato AAAA-MM-DD.\'\n 
   },\n    \'confirmacao\': {\n      \'type\': \'string\',\n      \'description\': \'Confirmação final do usuário após a
 pergunta: 'Você confirma a reserva do pacote [nome do pacote]?'\',\n      \'enum\': [\'sim\', \'nao\']\n    }\n  },\n  
\'additionalProperties\': false\n}\n'
          },
          'id': '21cb15cc-0eb4-4b09-916e-4030aed6f364',
          'na
me': 'Produtos',
          'type': '@n8n/n8n-nodes-langchain.toolCode',
          'typeVersion': 1.1,
          'positio
n': [
            1940,
            380
          ]
        },
        {
          'parameters': {
            'options'
: {}
          },
          'id': 'bca727b7-dfb7-440a-bfa5-30a6291bb167',
          'name': 'AI Agent',
          'type'
: '@n8n/n8n-nodes-langchain.agent',
          'typeVersion': 1.7,
          'position': [
            1460,
            
0
          ]
        }
      ],
      'pinData': {},
      'connections': {
        'OpenAI Chat Model': {
          'a
i_languageModel': [
            [
              {
                'node': 'AI Agent',
                'type': 'ai_langua
geModel',
                'index': 0
              },
              {
                'node': 'Vector Store Tool',
     
           'type': 'ai_languageModel',
                'index': 0
              }
            ]
          ]
        },
 
       'Window Buffer Memory': {
          'ai_memory': [
            [
              {
                'node': 'AI Agen
t',
                'type': 'ai_memory',
                'index': 0
              }
            ]
          ]
        },

        'Governança': {
          'ai_tool': [
            [
              {
                'node': 'AI Agent',
      
          'type': 'ai_tool',
                'index': 0
              }
            ]
          ]
        },
        'Ma
nutenção': {
          'ai_tool': [
            [
              {
                'node': 'AI Agent',
                't
ype': 'ai_tool',
                'index': 0
              }
            ]
          ]
        },
        'Embeddings Ope
nAI': {
          'ai_embedding': [
            [
              {
                'node': 'Pinecone Vector Store',
     
           'type': 'ai_embedding',
                'index': 0
              }
            ]
          ]
        },
     
   'When chat message received': {
          'main': [
            [
              {
                'node': 'AI Agent',

                'type': 'main',
                'index': 0
              }
            ]
          ]
        },
       
 'Vector Store Tool': {
          'ai_tool': [
            [
              {
                'node': 'AI Agent',
       
         'type': 'ai_tool',
                'index': 0
              }
            ]
          ]
        },
        'Pin
econe Vector Store': {
          'ai_vectorStore': [
            [
              {
                'node': 'Vector Store
 Tool',
                'type': 'ai_vectorStore',
                'index': 0
              }
            ]
          ]
 
       },
        'Produtos': {
          'ai_tool': [
            [
              {
                'node': 'AI Agent',

                'type': 'ai_tool',
                'index': 0
              }
            ]
          ]
        }
     
 },
      'active': true,
      'settings': {
        'executionOrder': 'v1'
      },
      'versionId': '15488273-ce9f-
4c81-8ea2-effcbc1ff753',
      'meta': {
        'templateCredsSetupCompleted': true,
        'instanceId': '903758be996
74dfe7b481360148909777e364ca972532a486858bebbdb39e3f5'
      },
      'id': '7EWwQaOd7Cd6huwh',
      'tags': []
    }
 
   

Below the JSON SChema

    {
      'type': 'object',
      'properties': {
        'requestConfirmation': {
       
   'type': 'boolean',
          'description': 'Flag indicating whether the agent should ask for user confirmation after
 capturing the initial intent.',
          'default': true
        },
        'confirmation': {
          'type': 'strin
g',
          'description': 'User's final confirmation after the question: 'Do you confirm that you wish to request [se
rvice name]?'',
          'enum': ['yes', 'no']
        },
        'items': {
          'type': 'array',
          'desc
ription': 'List of requested hygiene items. Quantity is required if an item is requested.',
          'items': {
       
     'type': 'object',
            'properties': {
              'name': {
                'type': 'string',
           
     'description': 'Name of the hygiene item (e.g., towel, soap, shampoo)',
                'minLength': 1
            
  },
              'quantity': {
                'type': 'integer',
                'description': 'Requested quantity o
f the item',
                'minimum': 1
              }
            },
            'required': ['name', 'quantity']
  
        }
        },
        'services': {
          'type': 'array',
          'description': 'List of requested servic
es, such as arrangement or cleaning. Notes are optional.',
          'items': {
            'type': 'object',
          
  'properties': {
              'serviceType': {
                'type': 'string',
                'description': 'Type 
of requested service (e.g., 'arrangement', 'cleaning', 'bathroom')',
                'enum': ['arrangement', 'cleaning',
 'bathroom']
              },
              'notes': {
                'type': 'string',
                'description': 
'Additional notes for the service, if necessary',
                'maxLength': 500
              }
            },
      
      'required': ['serviceType']
          }
        }
      },
      'required': ['requestConfirmation', 'confirmation
'],
      'additionalProperties': false
    }
```
---

     
 
all -  [ Roast my Resume!!!! ](https://www.reddit.com/r/leetcode/comments/1goxv1m/roast_my_resume/) , 2024-11-13-0912
```
Hi everyone, in today's episode of roast my resume, I present to you my resume. I have 3 YOE and 8 MOE of relevant inter
nship (i say relevant cuz my other internships/part-time jobs were irrelevant), I am currently working as DS at a startu
p which does not pay too well (that's why the job switch). I am looking for a Data Scientist role so please give your su
ggestions accordingly.

I am looking for honest opinions on how I can improve my resume, what I should include or remove
, the order of sections, any other sections that I should insert, structure and wordings of present structure etc. This 
resume did help me get interviews at Intuit, The Washington Post, AWS and Meta, but lately I have not been able to grab 
any calls.

Your help is deeply appreciated and I look forward to the roast!

[edited resume](https://preview.redd.it/j6
lefnlm6d0e1.jpg?width=850&format=pjpg&auto=webp&s=ed689a922cf6d9d5913dc2367ee6d13471a4bf85)


```
---

     
 
all -  [ Chain approach for Langchain is not able to handle longer prompts ](https://www.reddit.com/r/LangChain/comments/1gos7xm/chain_approach_for_langchain_is_not_able_to/) , 2024-11-13-0912
```
I have two datasets I need to compare and give an output for. So for example, if dataset 1 has a list of items, I want i
t to compare across dataset 2 and return a mapping like this.

|Dataset 1|Dataset 2|
|:-|:-|
|Germany|Deustchland|
|Turk
ey|Turkiye|

I'm not actually using countries, but it's a bit like a fuzzy match of sorts.

I am currently testing out c
hains in langchain and using dataset 1 as the input data and then adding a couple of items from dataset 2 in the query. 
It works fine for a couple of items, but does not work for a larger number. Hence, I wanted to look for ways where I cou
ld generate an output without exceeding the prompt limit and getting accurate output.

Using map\_reduce or refine gives
 me this error  
**ValidationError**: 1 validation error for RefineDocumentsChain prompt  Extra inputs are not permitted
 \[type=extra\_forbidden, input\_value=PromptTemplate(input\_vari...IZED TESTS: {question}'), input\_type=PromptTemplate
\]
```
---

     
 
all -  [ Can Langgraph state hold binary data? ](https://www.reddit.com/r/LangChain/comments/1gors2y/can_langgraph_state_hold_binary_data/) , 2024-11-13-0912
```
Starting to use langgraph platform a bit now and it seems easier just to process EVERYTHING through my graph instead of 
using two hosting options (one for the graph and another for my other endpoints). Which makes me wonder can I keep pdf's
 in my graph state (or any binary data) to then send to my front end?

I could probably encode it in base64, but yeah. 
```
---

     
 
all -  [ Chatgpt like conversational vision model (Instructions Video Included) ](https://www.reddit.com/r/LangChain/comments/1gor4xd/chatgpt_like_conversational_vision_model/) , 2024-11-13-0912
```
[https://www.youtube.com/watch?v=sdulVogM2aQ](https://www.youtube.com/watch?v=sdulVogM2aQ)

[https://github.com/agituts/
ollama-vision-model-enhanced/](https://github.com/agituts/ollama-vision-model-enhanced/)

# Basic Operations:

* Upload 
an Image: Use the file uploader to select and upload an image (PNG, JPG, or JPEG).
* Add Context (Optional): In the side
bar under 'Conversation Management', you can add any relevant context for the conversation.
* Enter Prompts: Use the cha
t input at the bottom of the app to ask questions or provide prompts related to the uploaded image.
* View Responses: Th
e app will display the AI assistant's responses based on the image analysis and your prompts.

# Conversation Management


* Save Conversations: Conversations are saved automatically and can be managed from the sidebar under 'Previous Conver
sations'.
* Load Conversations: Load previous conversations by clicking the folder icon (📂) next to the conversation tit
le.
* Edit Titles: Edit conversation titles by clicking the pencil icon (✏️) and saving your changes.
* Delete Conversat
ions: Delete individual conversations using the trash icon (🗑️) or delete all conversations using the 'Delete All Conver
sations' button.
```
---

     
 
all -  [ How to Upgrade Related Content Chunks to Be Dynamic (Like in RAG-Powered Websites) ](https://www.reddit.com/r/LangChain/comments/1goqwpt/how_to_upgrade_related_content_chunks_to_be/) , 2024-11-13-0912
```
Hello everyone.

I'm working on a project that involves dynamically displaying 'related content' chunks on each page, si
milar to what is seen on popular Retrieval-Augmented Generation (RAG) websites. These sites are excellent at suggesting 
related or supplementary content based on the current page's content and user preferences. I'm looking for advice on how
 to implement a similar feature effectively.

https://preview.redd.it/mmlzl2pqz90e1.png?width=2880&format=png&auto=webp&
s=f826d34d48d519982e433e6038bddf569dda9945

https://preview.redd.it/n5a5lxcrz90e1.png?width=2880&format=png&auto=webp&s=
70f965d0ab99b0acfe37919821f9d4d9f3cc6484

https://preview.redd.it/sp073xcsz90e1.png?width=2880&format=png&auto=webp&s=a8
158f9811c0efdd41de666ff73d1c2a3effb70a


```
---

     
 
all -  [ A Personal NotebookLM and Perplexity-like AI Assistant with privacy. ](https://www.reddit.com/r/LangChain/comments/1goq5ud/a_personal_notebooklm_and_perplexitylike_ai/) , 2024-11-13-0912
```
Hi everyone for the last month or two I have been trying to build a hybrid of NotebookLM and Perplexity with better inte
gration with browsers as well.

So here is my little attempt to make something.

https://reddit.com/link/1goq5ud/video/3
6vrje0ld90e1/player

SurfSense :

While tools like NotebookLM and Perplexity are impressive and highly effective for con
ducting research on any topic, imagine having both at your disposal with complete privacy control. That's exactly what S
urfSense offers. With SurfSense, you can create your own knowledge base for research, similar to NotebookLM, or easily r
esearch the web just like Perplexity. SurfSense also includes an effective cross-browser extension to directly save dyna
mic content bookmarks, such as social media chats, calendar invites, important emails, tutorials, recipes, and more to y
our SurfSense knowledge base. Now, you’ll never forget anything and can easily research everything.

Bugs are to be expe
cted but I hope you guys give it a go.

GitHub Link: [https://github.com/MODSetter/SurfSense](https://github.com/MODSett
er/SurfSense)
```
---

     
 
all -  [ Help with LangChain Agent for Querying Parquet Files ](https://www.reddit.com/r/LangChain/comments/1gopx5k/help_with_langchain_agent_for_querying_parquet/) , 2024-11-13-0912
```
Hey everyone,

I’m new to LangChain and building an agent with text-to-SQL capabilities. My goal is to query Parquet fil
es stored in Azure Data Lake, but right now, I’m testing it on a local folder of Parquet files in my machine. Most resou
rces I’ve found focus on databases, not Parquet.

Anyone know of resources or have advice on making this work?

Thanks!
```
---

     
 
all -  [ Expense extractor Gmail plugin using Llama3.2 that runs locally and for free ](https://www.reddit.com/r/LangChain/comments/1gol8v3/expense_extractor_gmail_plugin_using_llama32_that/) , 2024-11-13-0912
```
https://reddit.com/link/1gol8v3/video/mz8bd3fon70e1/player


```
---

     
 
all -  [ Snippet showing integration of Langgraph with Voicekit ](https://www.reddit.com/r/LangChain/comments/1goh7gj/snippet_showing_integration_of_langgraph_with/) , 2024-11-13-0912
```
I asked this help a few days back. - [https://www.reddit.com/r/LangChain/comments/1gmje1r/help\_with\_voice\_agents\_liv
ekit/](https://www.reddit.com/r/LangChain/comments/1gmje1r/help_with_voice_agents_livekit/)

Since then, I've made it wo
rk. Sharing it for the benefit of the community. 

\## Here's how I've integrated Langgraph and Voice Kit.

\### Context
: 

I've a graph to execute a complex LLM flow. I had a requirement from a client to convert that into voice. So decided
 to use VoiceKit.

\### Problem

The problem I faced is that Voicekit supports a single LLM by default. I did not know h
ow to integrate my entire graph as an llm within that.   


\### Solution

I had to create a custom class and integrate 
it. 

\### Code

    class LangGraphLLM(llm.LLM):
        def __init__(
            self,
            *,
            par
am1: str,
            param2: str | None = None,
            param3: bool = False,
            api_url: str = '<api url>
',  # Update to your actual endpoint
        ) -> None:
            super().__init__()
            self.param1 = param1

            self.param2 = param2
            self.param3 = param3
            self.api_url = api_url
    
        def ch
at(
            self,
            *,
            chat_ctx: ChatContext,
            fnc_ctx: llm.FunctionContext | None 
= None,
            temperature: float | None = None,
            n: int | None = 1,
            parallel_tool_calls: bo
ol | None = None,
        ) -> 'LangGraphLLMStream':
            if fnc_ctx is not None:
                logger.warning(
'fnc_ctx is currently not supported with LangGraphLLM')
    
            return LangGraphLLMStream(
                self
,
                param1=self.param1,
                param3=self.param3,
                api_url=self.api_url,
        
        chat_ctx=chat_ctx,
            )
    
    
    class LangGraphLLMStream(llm.LLMStream):
        def __init__(
  
          self,
            llm: LangGraphLLM,
            *,
            param1: str,
            param3: bool,
       
     api_url: str,
            chat_ctx: ChatContext,
        ) -> None:
            super().__init__(llm, chat_ctx=chat
_ctx, fnc_ctx=None)
            param1 = 'x'  
            param2 = 'y'
            self.param1 = param1
            sel
f.param3 = param3
            self.api_url = api_url
            self._llm = llm  # Reference to the parent LLM instance

    
        async def _main_task(self) -> None:
            chat_ctx = self._chat_ctx.copy()
            user_msg = ch
at_ctx.messages.pop()
    
            if user_msg.role != 'user':
                raise ValueError('The last message in
 the chat context must be from the user')
    
            assert isinstance(user_msg.content, str), 'User message conte
nt must be a string'
    
            try:
                # Build the param2 body
                body = self._build_bo
dy(chat_ctx, user_msg)
    
                # Call the API
                response, param2 = await self._call_api(body)

    
                # Update param2 if changed
                if param2:
                    self._llm.param2 = param
2
    
                # Send the response as a single chunk
                self._event_ch.send_nowait(
               
     ChatChunk(
                        request_id='',
                        choices=[
                            Cho
ice(
                                delta=ChoiceDelta(
                                    role='assistant',
          
                          content=response,
                                )
                            )
            
            ],
                    )
                )
            except Exception as e:
                logger.error(f
'Error during API call: {e}')
                raise APIConnectionError() from e
    
        def _build_body(self, chat_
ctx: ChatContext, user_msg) -> str:
            '''
            Helper method to build the param2 body from the chat con
text and user message.
            '''
            messages = chat_ctx.messages + [user_msg]
            body = ''
     
       for msg in messages:
                role = msg.role
                content = msg.content
                if rol
e == 'system':
                    body += f'System: {content}\n'
                elif role == 'user':
                 
   body += f'User: {content}\n'
                elif role == 'assistant':
                    body += f'Assistant: {cont
ent}\n'
            return body.strip()
    
        async def _call_api(self, body: str) -> tuple[str, str | None]:
   
         '''
            Calls the API and returns the response and updated param2.
            '''
            logger.i
nfo('Calling API...')
    
            payload = {
                'param1': self.param1,
                'param2': self
._llm.param2,
                'param3': self.param3,
                'body': body,
            }
    
            async 
with aiohttp.ClientSession() as session:
                try:
                    async with session.post(self.api_url, 
json=payload) as response:
                        response_data = await response.json()
                        logger.
info('Received response from API.')
                        logger.info(response_data)
                        return re
sponse_data['ai_response'], response_data.get('param2')
                except Exception as e:
                    logge
r.error(f'Error calling API: {e}')
                    return 'Error in API', None
    
    

    
    # Initialize your
 custom LLM class with API parameters
        custom_llm = LangGraphLLM(
            param1=param1,
            param2=N
one,
            param3=False, 
            api_url='<api_url>',  # Update to your actual endpoint
        )


```
---

     
 
all -  [ Difficulty of using LLMs with LangChain ](https://www.reddit.com/r/LLMs/comments/1gog2q9/difficulty_of_using_llms_with_langchain/) , 2024-11-13-0912
```
So I’m new to the LLM / Bedrock world (and this sub). I see so many training courses about using LangChain with Bedrock.
 But the syntax of using LangChain / Langgraph feels way more complex than it needs to be. Actual Bedrock API feels simp
ler. 

What are other folks’ experience? Have any of y’all preferred to just use Bedrock without LangChain?

If not, any
 tips on how to get used to LangChain (other than reading docs)?
```
---

     
 
all -  [ Fully local and free Gmail assistant ](https://v.redd.it/hcggq8pw550e1) , 2024-11-13-0912
```
Gemini for Gmail is great but it's expensive. So I decided to build one for myself this weekend - A smart gmail assistan
t that runs locally and completely free, powered by llama-3.2-3b-instruct.

Stack:
- local LLM server running llama-3.2-
3b-instruct from LM studio with Apple MLX
- Gmail plugin built by Claude

Took less than 30min to get here. Plan to add 
a local RAG over all my emails and some custom features.
```
---

     
 
all -  [ glassBead Blog: new LangChain-oriented technical blog ](https://www.reddit.com/r/LangChain/comments/1go9xpb/glassbead_blog_new_langchainoriented_technical/) , 2024-11-13-0912
```
hey everybody,

  
i just published the first of a long planned series of blog posts detailing things that I learn while
 building w/ LangGraph at relative length. this is my first time ever attempting to do a technical blog, so i'd welcome 
any and all tips on how to do these in a way that's at least potentially helpful to someone reading. thanks in advance i
f you've got feedback!

[https://glassbead-tc.medium.com/the-glassbead-blog-gbb-atrisdocs001-langgraphstatemgmt-bf322837
d00c](https://glassbead-tc.medium.com/the-glassbead-blog-gbb-atrisdocs001-langgraphstatemgmt-bf322837d00c)
```
---

     
 
all -  [ Weekly Linkedin RAG Highlights: Uber’s SQL Hack, New Courses, and Key Updates ](https://www.reddit.com/r/Rag/comments/1go6vit/weekly_linkedin_rag_highlights_ubers_sql_hack_new/) , 2024-11-13-0912
```
LinkedIn has become one of my go-to spots for staying up-to-date with RAG, so I figured I'd share a quick digest of some
 top posts from last week that caught my eye:

1. [**Uber’s RAG-Powered Text-to-SQL Saves 140,000 Hours**](https://www.l
inkedin.com/posts/sarthakrastogi_ai-llms-rag-activity-7250479007270359040-umSq/?utm_source=share&utm_medium=member_deskt
op) (2332 likes) – Uber developed QueryGPT, a custom system that uses RAG to cut SQL query writing time from 10 minutes 
to 3, saving thousands of hours annually. It uses multiple agents to optimize every step of the process, from intent rec
ognition to table selection.
2. [**LangChain’s “RAG from Scratch” Playlist**](https://www.linkedin.com/posts/areganti_ti
l-langchain-has-a-super-beginner-friendly-activity-7255042856535408641-iKdf/?utm_source=share&utm_medium=member_desktop)
 (1210 likes) – LangChain has a new YouTube series called 'RAG from Scratch' that’s beginner-friendly and covers advance
d topics like RAPTOR and query reform. Quick watch—under two hours total.
3. [**Curated RAG Resource List**](https://www
.linkedin.com/posts/reyhanmerekar_rag-is-one-of-the-most-important-skillsets-activity-7253015624300343296-HOFi/?utm_sour
ce=share&utm_medium=member_desktop) (957 likes) – A great rundown of the best courses and GitHub repos for anyone diving
 into RAG. Includes LangChain, [DeepLearning.AI](http://DeepLearning.AI) courses, and some solid repos to get hands-on.

4. [**Free RAG++ Course by W&B, Cohere, and Weaviate**](https://www.linkedin.com/posts/areganti_i-spent-some-time-going-
through-the-free-activity-7252506115253374977-ZwE2/?utm_source=share&utm_medium=member_desktop) (588 likes) – This cours
e covers advanced RAG topics with a production focus, emphasizing evaluation, data ingestion, and efficiency improvement
s.
5. [**Anthropic on Contextual Retrieval**](https://www.linkedin.com/posts/areganti_anthropics-latest-blog-on-contextu
al-activity-7247953742363258883-7SfR/?utm_source=share&utm_medium=member_desktop) (528 likes) – Anthropic’s latest blog 
discusses a new way to enhance RAG retrieval by adding contextual information to embeddings, with a reported 70% boost i
n performance.
6. [**Query Rewrite RAG with LangFlow**](https://www.linkedin.com/posts/tom-yeh_query-rewrite-rag-by-hand
-langflow-activity-7248326712973819904-2L3F/?utm_source=share&utm_medium=member_desktop) (760 likes) – Tom Yeh is sharin
g exercises to teach advanced RAG concepts with LangFlow, providing visuals and exercises to bridge theory with practice
.
7. [**Mnemosyne: Personalized Search Agent for Medium**](https://www.linkedin.com/posts/akshaybahadur21_raghav-patnech
a-and-i-built-an-intelligent-activity-7254402851018321921-b2KS/?utm_source=share&utm_medium=member_desktop) (164 likes) 
– Two devs shared their experience building a conversational search agent for Medium, using RAG methods like answer grad
ing and chunking to improve relevance.
8. [**Quick Video on RAG Basics**](https://www.linkedin.com/posts/corneliusa_in-t
his-short-video-i-explain-the-concept-activity-7251629726425915392-GKoy/?utm_source=share&utm_medium=member_desktop) – A
 short intro video breaking down the core concepts of RAG for those new to the field. Great for quick insights!

Got any
 interesting RAG news from last week? Drop them in the comments! I'd love to hear what you’re following.

Was this helpf
ul? Should I keep doing these weekly digests? Hit like if you want more, and leave a comment with your thoughts!
```
---

     
 
all -  [ What sort of job titles and roles should I look for? ](https://www.reddit.com/r/datascience/comments/1go59j5/what_sort_of_job_titles_and_roles_should_i_look/) , 2024-11-13-0912
```
Hi, I've been working as an analyst for a retail company for a few years, but it's pretty basic and mostly focused on re
porting, dashboards, etc, so I'm looking for more roles with a heavier data science and computation focus. But I'm getti
ng overwhelmed and confused about what sorts of roles to look for.

A quick google search for 'types of roles in data sc
ience' and you'll find dozens of pages filled with SEO-driven buzzwords (possibly AI-generated), but these only give the
 most surface-level and generic descriptions of common titles like data analyst, data scientist, data engineer, etc. Thi
s isn't really what I'm looking for though lol. I know what these are. Also, so many roles today seem to just be focused
 on shoving the latest LLM stack (RAG, langchain, etc) into the problem even if the use case for the company is slim or 
marginal at best. This isn't really what I'm interested in cause I like operations data science more.

What I'm looking 
for is a more specific, tailored advice relevant to specific types of industries/specializations. For example

* I reall
y like building models that heavily rely on functional programming, and may make use of very niche or specific libraries
 depending on the use case. I enjoy Project Euler type problems for example
* I understand ML is a core part of data sci
ence, but I enjoy projects where ML isn't exclusive to the problem. A lot of other models can be solved by more function
al programming and tailored computational science type work
* I guess my background right now is mostly focused on busin
ess/operations/economics, so I don't have a specific engineering or hard science background, but I'm open to any area th
at invovles applied mathematics.

I would appreciate any and all advice. As specific or general as possible. But prefera
bly something specific.
```
---

     
 
MachineLearning -  [ [P] Open-source declarative framework to build LLM applications - looking for contributors ](https://www.reddit.com/r/MachineLearning/comments/1gkpazh/p_opensource_declarative_framework_to_build_llm/) , 2024-11-13-0912
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

     
 
deeplearning -  [ Fast AI's deep learning for coders by jeremy howard for begginer?  ](https://www.reddit.com/r/deeplearning/comments/1gb2k3p/fast_ais_deep_learning_for_coders_by_jeremy/) , 2024-11-13-0912
```
I am a full stack python developer who do web dev in django

I am now starting deep learning,i am a compelete begginer


(Have worked with pandas,numpy,matplotlib,langchain only)

I wanna ask,should i do this course,will i understand what he
 is coding and code myslef

I just dont want to do blind coding,i wanna learn what is the purpose,how it works and how t
o do it

Will this course teach me that or not?

Thanks in advance
```
---

     
