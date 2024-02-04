 
all -  [ Integrating LangChain application? ](https://www.reddit.com/r/homeassistant/comments/1ai8acr/integrating_langchain_application/) , 2024-02-04-0910
```
Hello, I'm wondering if there's any possible way of integrating a LangChain application with the existing OpenAI integra
tion?

Basically what I'm wanting to do is to use the OpenAI Conversation / OpenWakeWord integrations, but talk to my ow
n LangChain agent instead. The reason for this is because I want to integrate it with things that HASS doesn't (and will
 never) have integrations for, while also still retaining the ability to interact with my smart home devices.

Has anybo
dy been able to do something like this?
```
---

     
 
all -  [ Embeddings from Vector Stores ](https://www.reddit.com/r/LangChain/comments/1ai3k14/embeddings_from_vector_stores/) , 2024-02-04-0910
```
Currently I'm using Chroma as a vector db for a langchain agent. I'm looking to do some metadata extraction/clustering w
ith the core embeddings. Is this something that can be easily accessed for each document - seems the db queries will onl
y return Document/text content. Is there clean way to have access to all embeddings and have them in a numpy array for e
xample? 

&#x200B;

Appreciate any help.. of course its not too difficult to just re-do the embeddings and access them d
irectly but I'm wondering if there is a way to avoid paying 2x

&#x200B;

Thanks!
```
---

     
 
all -  [ Need some reviews in my resume. ](https://www.reddit.com/r/resumes/comments/1ai1uiu/need_some_reviews_in_my_resume/) , 2024-02-04-0910
```
&#x200B;

https://preview.redd.it/psqp00y0segc1.png?width=660&format=png&auto=webp&s=0822dd684503f53a9f8de4ef0de35cbeb39
c65e4

https://preview.redd.it/9agog1y0segc1.png?width=660&format=png&auto=webp&s=21432efabdc8d73150edba2cbbef01fede6a19
02
```
---

     
 
all -  [ LangChain Quickstart ](https://youtu.be/lnSAfijrd0g?si=TSWLW8yjZFTvNup9) , 2024-02-04-0910
```

```
---

     
 
all -  [ Extracting Answer Source Chunks from GPT Responses in Langchain ](https://www.reddit.com/r/LLMDevs/comments/1ahs82h/extracting_answer_source_chunks_from_gpt/) , 2024-02-04-0910
```
Hey everyone,

I've been working on a project where I extract information from a large PDF document. I've completed the 
initial steps, including reading the PDF, splitting it into chunks, converting them to embeddings, and storing them in a
 vector database.

For the next step, I perform a similarity check with a limit of 28. Each chunk has a size of 350, wit
h an overlap of 80. After that, I send these chunks to GPT with a specific question. GPT provides answers, but I'm strug
gling to determine from which chunk the answer originated.

Is there a way to identify the specific chunk(s) that GPT us
ed to generate the answer? Alternatively, is there a solution to get an array of chunks that may contain the answer out 
of the 28 available?

Any insights or suggestions on how to achieve this would be greatly appreciated!

Thanks in advanc
e!
```
---

     
 
all -  [ Noob-friendly Recap ](https://www.reddit.com/r/LocalLLaMA/comments/1ahr6ds/noobfriendly_recap/) , 2024-02-04-0910
```
I recently started getting in LLM-powered applications by myself and using online resources. What I discovered is that L
LMs have become so mainstream that there are so many platform, frameworks, and model to choose from. And usually I don't
 even understand what are the key differences between one another

This is what I understood, please enlighten me and wh
oever comes here through a Google search

- LLMs are huge models and if I want to run them locally I should use a quanti
zed version: what are the best practices? What are the requirements? I'm currently using windows but I'm having so much 
troubles 

- Faster inference: what are the differences between vLLM, llamacpp, and ollama? The second one is the only o
ne that *should* work on windows. Should I always use these frameworks? Are they used only to load the quantized model? 


- Deployment. What are the best platform / best practices regarding the deployment phase? I guess a logic choice would
 be having the LLM available via API

- Fine-tuning. There are multiple ways to fine-tune a LLM. LORA seems a good trade
-off. Should I use a particular framework to apply it? Moreover, let's say I fine-tune my model over different use-cases
. In production, how do I swap the weights for these different models efficiently? 

- Orchestrator. LangChain should be
 the most popular one, but is it the one to go for? I see they are working on a huge refactor
```
---

     
 
all -  [ SQL Agent + Vector Store RAG ](https://www.reddit.com/r/LangChain/comments/1ahpvmm/sql_agent_vector_store_rag/) , 2024-02-04-0910
```
Hello! First timer here. 

I'm learning the ropes with LangChain, and have successfully made

1. A chat which integrates
 with a Postgres/Chroma vector store to augment responses
2. A chat which uses a SQL Agent with BigQuery to introspect a
nd query a dataset

What I am struggling to figure out now, is how do I combine them? I want to have the vector store au
gment the prompts used by the SQL agent. I think it will yield me better results if I can layer in project documentation
 and examples. However, the API documentation doesn't make it clear (At least to me) how to effectively accomplish this.
 

Hope somebody can help!
```
---

     
 
all -  [ Hi, I could use some help getting started on project (noob) ](https://www.reddit.com/r/LangChain/comments/1ahiw5p/hi_i_could_use_some_help_getting_started_on/) , 2024-02-04-0910
```
Heya! I am making a side project where I have a laptop being fed strings from a supabase api. these string will be messa
ges from a chat from a webapp I made. They will be loaded into a local llama, and the llama will see if the messages con
tain any addresses or personal revealing information.   
It must block messages from users sharing the following:  
  \-
 addresses   
\- contact information   
\- phone numbers   
\- social media handles   
\- etc.    
My plan is to use my 
i3 16gb windows os laptop and download a local\_llama llm, then have it constantly run, and when it finds a message to f
lag, run a script that sends an email.  


Does anyone have advice on figuring out how to make this? Thanks :)
```
---

     
 
all -  [ Manager Wants to switch from LangChain to Copilot Studio for a Client Product - Thoughts? ](https://www.reddit.com/r/Langchaindev/comments/1ahfbzb/manager_wants_to_switch_from_langchain_to_copilot/) , 2024-02-04-0910
```
 Hey everyone!

I'm having a bit of trouble and could really use your wisdom. My company is eager to add AI to their pro
ducts and daily operations.

We have this internal initiative where people from various departments come together to inn
ovate or improve something, to add more value to the organization. My group has the task to develop an AI Chatbot, to as
sume some of the functions typically performed by an analyst, in a specific type of service, where it interacts with the
 customer, collects information for a specific process and uses this information to parameterize the company's system, f
or that specific customer.

Here's the problem: we have about 160 person-hours per month, split between three of us, ove
r the next three months, to go from having zero expertise in creating AI-powered apps to delivering a functional AI-powe
red chatbot MVP.

It is clear that they do not know what they are doing about this matter. They gave us ChatGPT licenses
 after we requested OpenAI API credits. So they asked us to create a detailed AI spending plan, so they can evaluate (an
d yes, we are a technology company with over 1k employees).

Now they want us to move our development efforts to Copilot
 Studio, abandoning our current development with Python and Langchain. From what I gather, this may not be the wisest co
urse of action, especially considering the intricate context management our project requires (different rules for answer
s, complex questions) and the potential lock-in with the Microsoft ecosystem (also, for what I could check, the client n
eeds to pay for copilot studio as well). They don't even have paid Copilot Studio yet (don't know if they will ever do).


The challenge is that we don't really know much about AI development (we're trying to study it in the meantime), so it
's hard to argue with them.

Can anyone here help us understand if it's true that Copilot Studio could be a better solut
ion? Yes? No?

I would deeply appreciate any information or advice you could share so I can craft a well-informed respon
se.

Thank you very much in advance for your contribution and time!
```
---

     
 
all -  [ Manager Wants to switch from LangChain to Copilot Studio for a Client Product - Thoughts? ](https://www.reddit.com/r/LangChain/comments/1ahfbmm/manager_wants_to_switch_from_langchain_to_copilot/) , 2024-02-04-0910
```
 

Hey everyone!

I'm having a bit of trouble and could really use your wisdom. My company is eager to add AI to their p
roducts and daily operations.

We have this internal initiative where people from various departments come together to i
nnovate or improve something, to add more value to the organization. My group has the task to develop an AI Chatbot, to 
assume some of the functions typically performed by an analyst, in a specific type of service, where it interacts with t
he customer, collects information for a specific process and uses this information to parameterize the company's system,
 for that specific customer.

Here's the problem: we have about 160 person-hours per month, split between three of us, o
ver the next three months, to go from having zero expertise in creating AI-powered apps to delivering a functional AI-po
wered chatbot MVP.

It is clear that they do not know what they are doing about this matter. They gave us ChatGPT licens
es after we requested OpenAI API credits. So they asked us to create a detailed AI spending plan, so they can evaluate (
and yes, we are a technology company with over 1k employees).

Now they want us to move our development efforts to Copil
ot Studio, abandoning our current development with Python and Langchain. From what I gather, this may not be the wisest 
course of action, especially considering the intricate context management our project requires (different rules for answ
ers, complex questions) and the potential lock-in with the Microsoft ecosystem (also, for what I could check, the client
 needs to pay for copilot studio as well). They don't even have paid Copilot Studio yet (don't know if they will ever do
).

The challenge is that we don't really know much about AI development (we're trying to study it in the meantime), so 
it's hard to argue with them.

Can anyone here help us understand if it's true that Copilot Studio could be a better sol
ution? Yes? No?

I would deeply appreciate any information or advice you could share so I can craft a well-informed resp
onse.

Thank you very much in advance for your contribution and time!
```
---

     
 
all -  [ Manager Wants to switch from LangChain to Copilot Studio for a Client Product - Thoughts? ](https://www.reddit.com/r/AskProgramming/comments/1ahf84w/manager_wants_to_switch_from_langchain_to_copilot/) , 2024-02-04-0910
```
Hey everyone!  
  
I'm having a bit of trouble and could really use your wisdom. My company is eager to add AI to thei
r products and daily operations. 

We have this internal initiative where people from various departments come together 
to innovate or improve something, to add more value to the organization. My group has the task to develop an AI Chatbot
, to assume some of the functions typically performed by an analyst, in a specific type of service, where it interacts w
ith the customer, collects information for a specific process and uses this information to parameterize the company's sy
stem, for that specific customer.

Here's the problem: we have about 160 person-hours per month, split between three of 
us, over the next three months, to go from having zero expertise in creating AI-powered apps to delivering a functional 
AI-powered chatbot MVP.

It is clear that they do not know what they are doing about this matter. They gave us ChatGPT 
licenses after we requested OpenAI API credits. So they asked us to create a detailed AI spending plan, so they can eval
uate (and yes, we are a technology company with over 1k employees).  
  
Now they want us to move our development effo
rts to Copilot Studio, abandoning our current development with Python and Langchain. From what I gather, this may not be
 the wisest course of action, especially considering the intricate context management our project requires (different ru
les for answers, complex questions) and the potential lock-in with the Microsoft ecosystem (also, for what I could check
, the client needs to pay for copilot studio as well). They don't even have paid Copilot Studio yet (don't know if they 
will ever do). 

The challenge is that we don't really know much about AI development (we're trying to study it in the m
eantime), so it's hard to argue with them.

Can anyone here help us understand if it's true that Copilot Studio could b
e a better solution? Yes? No?  
I would deeply appreciate any information or advice you could share so I can craft a we
ll-informed response.  
  
Thank you very much in advance for your contribution and time!
```
---

     
 
all -  [ Is Langchain the right framework for my usecase? ](https://www.reddit.com/r/LangChain/comments/1ahd2uz/is_langchain_the_right_framework_for_my_usecase/) , 2024-02-04-0910
```
I have ~2700 pdf documents, which are transcripts of Danish political conversations. The data is not confidential.

I wa
nt to create an gpt-4-based chatbot (Using something like streamlit or chainlit) that can answer (In Danish) about the p
dfs.

So far I have tried using this [azure search open ai demo](https://github.com/Azure-Samples/azure-search-openai-de
mo) which garnered fairly good results, but is pretty expensive to set up and run.

Can the same performance be achieved
 (or better) using langchain?

And if so, are there repos or blog posts that I should take a look at given my use case? 
(Wanting a danish chatbot and using a fairly large amount of pdfs) 

Thank you!
```
---

     
 
all -  [ Does React + NestJS SaaS boilerplate with all features worth selling in 2024 ? If yes then where and ](https://www.reddit.com/r/SaaS/comments/1ahbxv5/does_react_nestjs_saas_boilerplate_with_all/) , 2024-02-04-0910
```
Hi people,

I have created an amazing boiler plate on NestJS + ReactJS + TailwindCSS + Prisma and it includes all the am
azing features like Open AI GPT APIs, Stable Diffusion Implementation, Assitant API, Langchain along with Stripe, Multi 
Tenancy, RBAC, Teams . Landing Page elements as well. Who should I approach and where and how ? Is this even worth in 20
24 ?
```
---

     
 
all -  [ In terms of web app UI/UX customization with branding and theming, how capable is Gradio/textwebui? ](https://www.reddit.com/r/Oobabooga/comments/1ahbsxi/in_terms_of_web_app_uiux_customization_with/) , 2024-02-04-0910
```
Sorry for such a nub question but ive just recently been handed over a langchain + gradio frontend that has tabs for dif
ferent agent personas (ba, qa, dev) using RAG (jira, codebase, etc) and wondering if gradio has the capability and suppo
rt to be fully branded and extended for more general MVP web app UI, such as responsive app shells (different sidebars a
nd headers configs ie drawers and app bars), custom themes, branding, animations, etc. If so, is it the right tool for s
omething as described or would I just be better off building on top of something like lobechat, autogen, chatui, etc. 


Thanks!
```
---

     
 
all -  [ Chat with a website using Next.js, FastAPI and LangChain ](https://www.reddit.com/r/nextjs/comments/1ahauj9/chat_with_a_website_using_nextjs_fastapi_and/) , 2024-02-04-0910
```
Ciao a tutti! If it can be helpful to anyone, I'm sharing a starter template repository for chatting with websites using
 FastAPI, Next.js, and the latest version of LangChain.

[https://github.com/mazzasaverio/nextjs-fastapi-your-chat](http
s://github.com/mazzasaverio/nextjs-fastapi-your-chat)
```
---

     
 
all -  [ 🐍 Welcome to LangChainDev: Building a Python-Powered Community 🚀 ](https://www.reddit.com/r/langchain_py/comments/1ah9x9r/welcome_to_langchaindev_building_a_pythonpowered/) , 2024-02-04-0910
```
Hey LangChain developers! 🌐

I'm thrilled to introduce you to LangChainDev, a vibrant subreddit tailored specifically fo
r Python enthusiasts within the LangChain community. Whether you're a seasoned developer or just starting your journey w
ith LangChain, this is the place to be.

🤔 **What's LangChainDev all about?**

LangChainDev is more than just a subreddi
t; it's a space where Python developers can come together to share, learn, and collaborate. We believe in the power of c
ommunity, and our goal is to create a hub for LangChain enthusiasts to connect, ask questions, and build something amazi
ng together.

🐍 **Why Python?**

Python is the backbone of LangChain, and here, we celebrate its versatility and power. 
Whether you're into web development, data science, machine learning, or any other Python-related field, LangChainDev is 
your go-to place to discuss, share insights, and explore the endless possibilities Python offers.

🤝 **What to Expect:**


- **Doubts & Questions:** Got a coding conundrum? Need help with a Python challenge? Ask away! LangChainDev is a suppo
rtive environment where the community rallies to solve problems together.

- **Reviews & Recommendations:** Found a cool
 Python library or tool? Share your reviews and recommendations with fellow developers. Let's discover the best tools fo
r building with LangChain.

- **Suggestions & Opinions:** Your ideas matter. LangChainDev is the perfect platform to voi
ce your suggestions, opinions, and visions for the LangChain community. Together, we shape the future.

💪 **Let's Build 
Together:**

LangChainDev isn't just a forum; it's a call to action. Let's collaborate, innovate, and build something ex
traordinary. Your journey with LangChain becomes richer when shared with a community of like-minded developers.

🌟 **How
 to Get Involved:**

1. **Join the Conversation:** Start or join discussions on the latest Python trends, LangChain upda
tes, and more.

2. **Ask Questions:** Stuck on a coding problem? Need advice? Our community is here to help. No question
 is too big or too small.

3. **Share Your Expertise:** Have a Python tip or a LangChain success story? Share your knowl
edge and inspire others.

4. **Connect:** Follow fellow LangChain developers, build connections, and collaborate on proj
ects.


👩‍💻 **In Conclusion:**


LangChainDev is not just a subreddit; it's a dynamic ecosystem where Python developers 
within the LangChain community come together to learn, support, and grow. Whether you're a seasoned coder or just gettin
g started, there's a place for you here.

Ready to dive in? Head over to LangChainDev and let's embark on this Python-po
wered journey together!

See you in the threads 👋🏼
```
---

     
 
all -  [ r/langchain_py Ask Anything Thread ](https://www.reddit.com/r/langchain_py/comments/1ah9w8n/rlangchain_py_ask_anything_thread/) , 2024-02-04-0910
```
Use this thread to ask anything at all!
```
---

     
 
all -  [ Document Q&A, also include images ](https://www.reddit.com/r/LangChain/comments/1ah74n8/document_qa_also_include_images/) , 2024-02-04-0910
```
I have lots of documents, they contain procedures to operate a software and it also include images. Now my question is h
ow do i  build a custom LLM that would be capable of answering the user with text and also provide the appropriate image
 from the document
```
---

     
 
all -  [ Extracting Answer Source Chunks from GPT Responses in Langchain ](https://www.reddit.com/r/LangChain/comments/1ah5zg3/extracting_answer_source_chunks_from_gpt/) , 2024-02-04-0910
```
 Hey everyone,

I've been working on a project where I extract information from a large PDF document. I've completed the
 initial steps, including reading the PDF, splitting it into chunks, converting them to embeddings, and storing them in 
a vector database.

For the next step, I perform a similarity check with a limit of 28. Each chunk has a size of 350, wi
th an overlap of 80. After that, I send these chunks to GPT with a specific question. GPT provides answers, but I'm stru
ggling to determine from which chunk the answer originated.

Is there a way to identify the specific chunk(s) that GPT u
sed to generate the answer? Alternatively, is there a solution to get an array of chunks that may contain the answer out
 of the 28 available?

Any insights or suggestions on how to achieve this would be greatly appreciated!

Thanks in advan
ce!
```
---

     
 
all -  [ [Langchain] Finetune mixtral sur les données d'entreprise - à quoi devrait ressembler les données de ](https://www.reddit.com/r/redditenfrancais/comments/1ah5jay/langchain_finetune_mixtral_sur_les_données/) , 2024-02-04-0910
```
Salut,

Je veux affiner un modèle Mistral ou Mixtral sur les données de mes entreprises. Plus précisément, le modèle doi
t écrire des points de puces en textes complets. Je me demandais à quoi devait ressembler les données de formation pour 
cette tâche?

Est-ce un moyen valable de laisser un LLM créer des bullets à partir d'un texte et d'utiliser ces exemples
 de points de buts-full-text-text pour la formation?

Traduit et reposté à partir de la publication 1973jxk de la commun
auté langchain. Pour retrouver la publication originale, insérez l'id de la publication après 'reddit.com/'
```
---

     
 
all -  [ ChatGPT like UI for any project within 15 mins ](https://www.reddit.com/r/LangChain/comments/1ah55wi/chatgpt_like_ui_for_any_project_within_15_mins/) , 2024-02-04-0910
```
A vast majority of Generative AI solutions are delivered in a chat based user experience. 

I've created a tutorial on h
ow to quickly adapt an open-source framework to deliver that user experience within 15 minutes. 

I hope the community f
inds this useful!

![https://youtu.be/sZ1aJ0zfgmY?si=koLhtl_FO6-y3SC5](https://youtu.be/sZ1aJ0zfgmY?si=koLhtl_FO6-y3SC5)

```
---

     
 
all -  [ [Langchain] Langchain JS vs Python ](https://www.reddit.com/r/redditenfrancais/comments/1ah4jut/langchain_langchain_js_vs_python/) , 2024-02-04-0910
```
Salut, je pense à construire un framework de chatbot sans serveur open-source qui comprendra l'un des modules inclura l'
intégration de Langchain.


\ - Je sais que Langchain est né à Python (et je suppose que celui de Python est plus supéri
eur?)
\ - Je regarde le tracker Langchain Python vs TS et je vois que le Python One ne prend pas en charge Supabase
\ - 
De nombreux développeurs de chatbot ou développeurs Web que je vois travaillent avec JavaScript plutôt que Python (je pe
nse?)


Il s'agit donc de cette question pour déterminer avec lesquelles devrais aller (Python ou JS):
Langchain dans JS
 est-il déjà assez bon pour construire un framework chatbot très motivable robuste? Ou y a-t-il une mise en garde que je
 devrais connaître?

Traduit et reposté à partir de la publication 14jweso de la communauté langchain. Pour retrouver la
 publication originale, insérez l'id de la publication après 'reddit.com/'
```
---

     
 
all -  [ [Local Llama] Meilleurs hôtes API LLM locaux pour la production ](https://www.reddit.com/r/redditenfrancais/comments/1ah3wqg/local_llama_meilleurs_hôtes_api_llm_locaux_pour/) , 2024-02-04-0910
```
Je me demandais ce que tout le monde utilise pour héberger des LLM locaux pour les appels API. J'ai utilisé Olllama + Li
tellm et le Générateur de texte-webui des hôtes API construits, mais j'ai besoin de quelque chose qui fonctionne bien av
ec Langchain ou Llamaindex. Je n'ai pas trouvé de bon tutoriel ou d'exemple qui connecte un LLM local à Llamaindex sur u
ne API.

Traduit et reposté à partir de la publication 1af5x3b de la communauté localllama. Pour retrouver la publicatio
n originale, insérez l'id de la publication après 'reddit.com/'
```
---

     
 
all -  [ Escape special characters from promt text ](https://www.reddit.com/r/LLaMA2/comments/1ah27xx/escape_special_characters_from_promt_text/) , 2024-02-04-0910
```
Anyone knows how to escape special characters on a string used for the prompt.? When i provide the code sample to guide 
llm its getting treated as place holder values for some input   


instruction = '''

Generate Apache Velocity code to c
onstruct a data structure for managing commodity information. The data structure should include lists and maps with adde
d elements, and properties assigned to objects. The scenario described should be followed exactly, and the resulting cod
e should adhere to Apache Velocity's syntax rules. Here is an explicit example illustrating how Apache Velocity template
 code is structured for a different context:

scenario : {question}

&#x200B;

The code example for reference (with plac
eholders removed for clarity):

\#set(rateshoptosend = {})

\#set(x = unitWeight.put('value','TEST'))

\#set(errorVoList
= \[{'errorCode': 'errorDefinitionId','errorMessage':'errorMsg','errorCategory':'ERROR'}\])

\#set(rateshoptosend.state 
= state)

JSONUtils.mapToJson(rateshoptosend)

&#x200B;

Please use the above structure as a guide to generate the new A
pache Velocity code.

&#x200B;

Answer:

'''  


ERROR ::  


 File /usr/local/lib/python3.9/dist-packages/langchain/cha
ins/base.py:475, in Chain.prep\_inputs(self, inputs)     **473**     external\_context = self.memory.load\_memory\_varia
bles(inputs)     **474**     inputs = dict(inputs, \*\*external\_context) --> 475 self.\_validate\_inputs(inputs)     **
476** **return** inputs  File /usr/local/lib/python3.9/dist-packages/langchain/chains/base.py:264, in Chain.\_validate\_
inputs(self, inputs)     **262** missing\_keys = set(self.input\_keys).difference(inputs)     **263** **if** missing\_ke
ys: --> 264 **raise** **ValueError**(f'Missing some input keys: **{**missing\_keys**}**')  ValueError: Missing some inpu
t keys: {'', ''errorCode''}**SHOW MORE**Render  
 
```
---

     
 
all -  [ Chat with PDFs using function calling ](https://www.reddit.com/r/LangChain/comments/1ah1l5f/chat_with_pdfs_using_function_calling/) , 2024-02-04-0910
```
Hi all, I built a chat with PDF using RAG but was struggling to get good results by just prompt stuffing. So I built an 
advanced PDF AI that uses function calling to intelligently figure out if:

1. The question needs retrieval from a docum
ent or a web search
2. If it needs retrieval, does it need to search the latest doc, a specific doc or all docs
3. Produ
ces an answer using the context retrieved

Give it a spin at: [https://pdf.aidev.run](https://pdf.aidev.run/) and let me
 know what you think. Looking for feedback so I can fix and improve. Here’s the [code](https://github.com/phidatahq/ai-c
ookbook/tree/main/pdf_ai) if you’re interested and I used [phidata](https://github.com/phidatahq/phidata) to build this.


https://reddit.com/link/1ah1l5f/video/zbz2hm1aq5gc1/player
```
---

     
 
all -  [ Nextjs-Langchain conversation memory not working. ](https://www.reddit.com/r/nextjs/comments/1ah1c5s/nextjslangchain_conversation_memory_not_working/) , 2024-02-04-0910
```
I'm trying to retrieve past conversation information from conversations through BufferMemory. I followed documentation i
n langchain js website, and the BufferMemory successfully retrieves the past memory and answers on that. But when I use 
BufferWindowMemory as mentioned in the documentation, the memory simply doesn't work. 

This is my code.   


    'use s
erver';
    import { ChatGoogleGenerativeAI } from '@langchain/google-genai';
    import { ChatPromptTemplate } from '@l
angchain/core/prompts';
    import { StringOutputParser } from '@langchain/core/output_parsers';
    import { RunnableSe
quence } from '@langchain/core/runnables';
    import { ConversationChain } from 'langchain/chains';
    import { Buffer
WindowMemory, ChatMessageHistory } from 'langchain/memory';
    import {
      MessagesPlaceholder,
      SystemMessageP
romptTemplate,
      HumanMessagePromptTemplate,
    } from '@langchain/core/prompts';
    import { AIMessage, HumanMess
age } from '@langchain/core/messages';
    
    const model = new ChatGoogleGenerativeAI({
      modelName: 'gemini-pro'
,
      maxOutputTokens: 2000,
      apiKey: process.env.GOOGLE_API_KEY as string,
      temperature: 0.1,
      streami
ng: true,
    });
    
    export const geminiRes = async (question: string) => {
      const memory = new BufferWindowM
emory({ k: 1 });
      console.log(memory.chatHistory);
      try {
        const chain = new ConversationChain({
      
    llm: model,
          memory: memory,
        });
    
        const response = await chain.predict({
          inpu
t: question,
        });
    
        console.log(response);
    
        return { success: true, response };
      } ca
tch (error) {
        console.log(error);
      }
    };
    

Can anybody please tell me what I'm doing wrong?   
I'm t
rying to build a chatbot like chatgpt but with context memory.  


Help please.

&#x200B;
```
---

     
 
all -  [ Conversation Memory not working with react. ](https://www.reddit.com/r/LangChain/comments/1ah180z/conversation_memory_not_working_with_react/) , 2024-02-04-0910
```
I'm trying to implement conversation buffer memory with react, but for some reason it doesn't work. I followed the docs 
in langchain  i.e  [Conversation buffer window memory | 🦜️🔗 Langchain](https://js.langchain.com/docs/modules/memory/type
s/buffer_window) , the code simply doesn't work.

However using BufferMemory works(I followed the code as given in the d
ocs)[Conversation buffer window memory | 🦜️🔗 Langchain](https://js.langchain.com/docs/modules/memory/types/buffer_window
) .

My code with BufferWIndow Memory

    const memory = new BufferWindowMemory({ k: 1 });
      console.log(memory.cha
tHistory);
      try {
        const chain = new ConversationChain({
          llm: model,
          memory: memory,
   
     });
    
        const response = await chain.call({
          input: question,
        });
    
        console.lo
g(response);
    
        return { success: true, response };
      } catch (error) {
        console.log(error);
      
}
    };

I'm using Gemini API, and I get answers from Gemini, but the memory doesn't seem to work.Can anybody please te
ll me what I'm doing wrong?I tried using ChatPromptTemplate as well, but the memory isn't working at all. Please help!
```
---

     
 
all -  [ What is LangChain? ](https://www.reddit.com/r/Chatbots/comments/1ah07x9/what_is_langchain/) , 2024-02-04-0910
```
Hello Everyone, if you may not already know, LangChain is a framework to build LLM powered applications, mostly Chatbots
.

 I have written a blog on [What is LangChain?](https://www.deligence.com/what_is_langchain_ai_app_development_framewo
rk_explained/) , please give it a read and let me know your thoughts on the content and relevance, as I am trying to ran
k it on google. Thanks!
```
---

     
 
all -  [ What is LangChain? ](https://www.reddit.com/r/LangChain/comments/1ah071c/what_is_langchain/) , 2024-02-04-0910
```
Hello Everyone I have written a blog on [What is LangChain?](https://www.deligence.com/what_is_langchain_ai_app_developm
ent_framework_explained/) , please give it a read and let me know your thoughts on the content and relevance, as I am tr
ying to rank it on google. Thanks!

&#x200B;
```
---

     
 
all -  [ Need help on budget for building a chatbot ](https://www.reddit.com/r/TechCareerShifter/comments/1agz169/need_help_on_budget_for_building_a_chatbot/) , 2024-02-04-0910
```
 Hi po, gusto ko lang po sana mag ask ng feedback and advice kung pano po ba magbudget for projects? I am a fresh grad p
o and been working for less than a year, totally clueless on how this stuff works hahaha.

Bale po kasi may nagreach out
 po sa akin na CEO from a small company in the US asking me to build them a chatbot na medyo may onting complexity. Basi
cally po the chatbot should be able to output some suggestions for a brand like anong color kaya yung bagay for their bu
siness, font style, rough logo, mga ganon po. The CEO emailed me yesterday asking for a budget that they should allocate
 for this project.

Ngayon po I have a rough idea of how to do this, and nagtingin tingin ako ng mga APIs na pwede kong 
magamit:

\- GPT-4 Turbo (as the engine for the bot)

\- Dall-E (generating a rough sketch/image of how the logo can be)


\- Colormind API (for color palette)

\- Google Fonts (fonts)

\- Font Joy (fonts)

\- Hosting? (di ko po sure kung pa
no rin ilalagay sa website nila yung ibbuild kong bot hahaha)

Most of these are free aside from the OpenAI APIs. Pero a
ng winoworry ko po is once na nagstart na sa development phase yung project possible po na some of these would not work 
the way I want it to or baka po may better APIs akong madiscover along the way. Pwede ko po ba lakihan yung budget ng on
ti para sa mga ganitong possibilities?

Also magkano po ba usually ang budgets talaga for projects like these? I am not 
even sure if I am on the right path sa idea ko po kung pano siya ibbuild, ang naisip ko po is gagamit na lang ako ng Lan
gChain to easily connect the tools (APIs) to GPT para po makapagformulate ng response yung bot.

Eto pong opportunity is
 a freelance work and I think solo ko po siya ibbuild. Would really appreciate any advice on what budget I should say an
d any feedback po sa plano kong approach on how I will be building it. Thank you po!
```
---

     
 
all -  [ Need help on budget for building a chatbot ](https://www.reddit.com/r/PinoyProgrammer/comments/1agz0lu/need_help_on_budget_for_building_a_chatbot/) , 2024-02-04-0910
```
Hi po, gusto ko lang po sana mag ask ng feedback and advice kung pano po ba magbudget for projects?  I am a fresh grad p
o and been working for less than a year, totally clueless on how this stuff works hahaha. 

Bale po kasi may nagreach ou
t po sa akin na CEO from a small company in the US asking me to build them a chatbot na medyo may onting complexity. Bas
ically po the chatbot should be able to output some suggestions for a brand like anong color kaya yung bagay for their b
usiness, font style, rough logo, mga ganon po. The CEO emailed me yesterday asking for a budget that they should allocat
e for this project.

Ngayon po I have a rough idea of how to do this, and nagtingin tingin ako ng mga APIs na pwede kong
 magamit:

\- GPT-4 Turbo (as the engine for the bot)

\- Dall-E (generating a rough sketch/image of how the logo can be
)

\- Colormind API (for color palette)

\- Google Fonts (fonts)

\- Font Joy (fonts)

\- Hosting? (di ko po sure kung p
ano rin ilalagay sa website nila yung ibbuild kong bot hahaha)

Most of these are free aside from the OpenAI APIs. Pero 
ang winoworry ko po is once na nagstart na sa development phase yung project possible po na some of these would not work
 the way I want it to or baka po may better APIs akong madiscover along the way. Pwede ko po ba lakihan yung budget ng o
nti para sa mga ganitong possibilities?

Also magkano po ba usually ang budgets talaga for projects like these? I am not
 even sure if I am on the right path sa idea ko po kung pano siya ibbuild, ang naisip ko po is gagamit na lang ako ng La
ngChain to easily connect the tools (APIs) to GPT para po makapagformulate ng response yung bot. 

Eto pong opportunity 
is a freelance work and I think solo ko po siya ibbuild. Would really appreciate any advice on what budget I should say 
and any feedback po sa plano kong approach on how I will be building it. Thank you po!
```
---

     
 
all -  [ How to solve schema problems in text-to-sql bot? ](https://www.reddit.com/r/LangChain/comments/1agxb0u/how_to_solve_schema_problems_in_texttosql_bot/) , 2024-02-04-0910
```
I am trying to build a text to sql bot based off of llama-index. The problem is tables have 100s of columns. What llama-
index does is put complete create table script of table in model context along with user question to generate sql query 
and subsequent answer. But if there is need to join multiples tables and they have alot of column its not very efficient
 and may not even work. How can I solve this problem? Also if some of those columns have enums how can I make the sql bo
t understand meaning of those enums?
```
---

     
 
MachineLearning -  [ [D] What's the best current RAG setup that would work with a local LLM? ](https://www.reddit.com/r/MachineLearning/comments/1ag6bo7/d_whats_the_best_current_rag_setup_that_would/) , 2024-02-04-0910
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

     
 
MachineLearning -  [ [P]: Anukool: My job hunting assistant ](https://www.reddit.com/r/MachineLearning/comments/1adu3tw/p_anukool_my_job_hunting_assistant/) , 2024-02-04-0910
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

     
 
MachineLearning -  [ New Data API for Astra [N] ](https://www.reddit.com/r/MachineLearning/comments/199uobn/new_data_api_for_astra_n/) , 2024-02-04-0910
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

     
 
MachineLearning -  [ [D] While using function calling or tools on openai or langchain, does openai have access to the dat ](https://www.reddit.com/r/MachineLearning/comments/199t8be/d_while_using_function_calling_or_tools_on_openai/) , 2024-02-04-0910
```
I am working on a client project and I am using langchain's tools and agents. I want to know if the data is getting pass
ed to openai or is it just like that - Output of one function is being directly passed to the second function with the k
nowledge of openai.
```
---

     
 
MachineLearning -  [ [D] Code vs JSON output for LLM agents? Frameworks like LangChain rely on LLMs responding with JSON  ](https://www.reddit.com/r/MachineLearning/comments/197f416/d_code_vs_json_output_for_llm_agents_frameworks/) , 2024-02-04-0910
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

     
 
MachineLearning -  [ [D] Are Custom LLM RAG apps going to become redundant? ](https://www.reddit.com/r/MachineLearning/comments/1929n4f/d_are_custom_llm_rag_apps_going_to_become/) , 2024-02-04-0910
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

     
 
MachineLearning -  [ [P] An open-source project for deploying local models ](https://www.reddit.com/r/MachineLearning/comments/18zkm5m/p_an_opensource_project_for_deploying_local_models/) , 2024-02-04-0910
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

     
 
deeplearning -  [ [D] Langchain Elevates with Step-Back Prompting using RAGatouille ](https://www.reddit.com/r/deeplearning/comments/1agtyeh/d_langchain_elevates_with_stepback_prompting/) , 2024-02-04-0910
```
In the dynamic realm of natural language processing, a revolutionary synergy has emerged between Langchain and Step-Back
 Prompting. This article delves into the transformative collaboration, exploring how Langchain’s cutting-edge platform i
ncorporates Step-Back Prompting to redefine language processing capabilities. Join us on a journey of innovation and dis
covery as we unravel the intricacies of this powerful integration. As we explore the uncharted territories of language m
odels, Step-Back Prompting stands as a beacon of progress, promising a journey of nuanced understanding and elevated per
formance in the world of Large Language Models. Welcome to the future of language processing, where inspiration and inno
vation converge in a symphony of words and ideas.

Link: https://medium.com/ai-advances/langchain-elevates-with-step-bac
k-prompting-using-ragatouille-b433e6f200ea
```
---

     
 
deeplearning -  [ Become an AI Developer (Free 9 Part Series) ](https://www.reddit.com/r/deeplearning/comments/1afgp2r/become_an_ai_developer_free_9_part_series/) , 2024-02-04-0910
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

     
 
deeplearning -  [ DSPy Explained! ](https://www.reddit.com/r/deeplearning/comments/1adypks/dspy_explained/) , 2024-02-04-0910
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

     
 
deeplearning -  [ [D] Unleashing the Power of Langchain with Wandb: Revolutionizing Topic Modeling and Evaluation ](https://www.reddit.com/r/deeplearning/comments/191mm83/d_unleashing_the_power_of_langchain_with_wandb/) , 2024-02-04-0910
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

     
