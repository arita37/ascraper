 
all -  [ How do you handle Parsing Errors With Create_Pandas_Dataframe_Agent? ](https://www.reddit.com/r/LangChain/comments/1hk8nu2/how_do_you_handle_parsing_errors_with_create/) , 2024-12-23-0913
```
I am using Langchain's Pandas Dataframe Agent to create an AI Agent.

I provide it with a dataset and I prompted it with
 'Analyze this dataset and provide me with a response that is in one concise sentence.'

The LLM is outputting seemingly
 fine sentences, but I am sometimes getting this error:

>ValueError: An output parsing error occurred. In order to pass
 this error back to the agent and have it try again, pass \`handle\_parsing\_errors=True\` to the AgentExecutor.

But, w
hen I add 'handle\_parsing\_errors = True' into the create\_pandas\_dataframe\_agent then I get this error message:

>Us
erWarning: Received additional kwargs {'handle\_parsing\_errors': True} which are no longer supported.

It seems like th
e 'handling\_parsing\_errors' used to be a solution last year, but it doesn't work anymore.

I also tried to improve my 
prompt by adding 'you must always return a response in a valid format. Do not return any additional text' which helped, 
but it's not perfect.   
  
Is there a better way to handle the responses that the LLM returns?
```
---

     
 
all -  [ Introducing Quantum CLI, A CLI Tool That Lets You Chat with a Local Chain of Thought AI in Your Term ](https://www.reddit.com/r/opensource/comments/1hk6v5p/introducing_quantum_cli_a_cli_tool_that_lets_you/) , 2024-12-23-0913
```
I’m thrilled to announce the launch of my new CLI tool, which lets you chat with a Chain of Thought AI directly from you
r terminal. It is FREE and Open Source. And can tell how many R's are in strawberry. Enjoy it and if you love it feel fr
ee to contribute. You can find it here: [https://github.com/andreivisan/quantum\_cli](https://github.com/andreivisan/qua
ntum_cli)  
Highlights:  
\- AI-Powered Development: Utilize Chain of Thought AI models through Ollama and LangChain to 
get instant AI-assisted insights and solutions.  
\- Offline Access: Enjoy the benefits of offline AI capabilities witho
ut relying on cloud services.  
\- Speed and Efficiency: Experience fast and efficient AI-powered responses directly in 
your terminal.  
\- Beautiful and Easy to Use: Beautiful response formatting using Markdown rendering for AI responses. 
 
\- Ollama Installation Management: The CLI tool will guide you through the installation if you don't have it.
```
---

     
 
all -  [ Introducing Quantum CLI, A CLI Tool That Lets You Chat with a Local Chain of Thought AI in Your Term ](https://www.reddit.com/r/golang/comments/1hk6t1w/introducing_quantum_cli_a_cli_tool_that_lets_you/) , 2024-12-23-0913
```
I’m thrilled to announce the launch of my new CLI tool, which lets you chat with a Chain of Thought AI directly from you
r terminal. It is FREE and Open Source. And can tell how many R's are in strawberry. Enjoy it and if you love it feel fr
ee to contribute. You can find it here: [https://github.com/andreivisan/quantum\_cli](https://github.com/andreivisan/qua
ntum_cli)  
Highlights:  
\- AI-Powered Development: Utilize Chain of Thought AI models through Ollama and LangChain to 
get instant AI-assisted insights and solutions.  
\- Offline Access: Enjoy the benefits of offline AI capabilities witho
ut relying on cloud services.  
\- Speed and Efficiency: Experience fast and efficient AI-powered responses directly in 
your terminal.  
\- Beautiful and Easy to Use: Beautiful response formatting using Markdown rendering for AI responses. 
 
\- Ollama Installation Management: The CLI tool will guide you through the installation if you don't have it.
```
---

     
 
all -  [ built a story generation tool that uses Gemini AI ](https://www.reddit.com/r/SideProject/comments/1hk5tzx/built_a_story_generation_tool_that_uses_gemini_ai/) , 2024-12-23-0913
```
I wanted to be able to generate full stories that maintain consistency throughout. Initially I used Gemini - it was good
, it worked, but sometimes neither the model nor I could keep track of what was happening. So I created GeminiNovelMaker
 as a starting point. It worked, but I wanted more. After diving into Langchain, ChromaDB, and Flutter (after a failed a
ttempt with React), and 3 months of building, I'm excited to present this project!

It's in managed rollout right now - 
you can download it at [https://github.com/LotusSerene/scrollwise-ai](https://github.com/LotusSerene/scrollwise-ai) (you
'll need a Gemini API key). Approval is quick! 

What's Next: Honestly? I'm just releasing this into the wild to see how
 it goes. After days of anxiety about making everything perfect (and realizing perfect is the enemy of good), I decided 
to just go for it. I'm really just doing this for the fun of it.

I'd love to hear your thoughts and feedback! This is j
ust the beginning, and I'm looking forward to building this together with the community.
```
---

     
 
all -  [ Built an OSS image background remover tool ](https://v.redd.it/iz82d8221g8e1) , 2024-12-23-0913
```

```
---

     
 
all -  [ If you're building with LLM, how do you make it more accurate and reliable? ](https://www.reddit.com/r/LLMDevs/comments/1hk3vpw/if_youre_building_with_llm_how_do_you_make_it/) , 2024-12-23-0913
```
I'm building in-house AI agents using langchain and GPT-4o. I've tried other frameworks like CrewAI but they weren't any
 better. For example, I have an agent doing some repetitive tasks for one of our customer support teams. I am using RAG 
but it still generates super generic results and sometimes just wrong ones. I've tried refining the prompts endless time
s.

I was wondering if there's any of you feel the same? or maybe you managed to find a way to make the LLM more 'contex
t-aware' (other than fine-tuning our own models which is not really an option).
```
---

     
 
all -  [ About Agents ](https://www.reddit.com/r/Rag/comments/1hk3a7r/about_agents/) , 2024-12-23-0913
```
Now a days many AI agents and assistant are coming up in market. I had recently learn langchain and other things like RA
G, embedding, vector database etc. I am looking to master on making great agent application but in market there are many
 framework for certain use case. So how I become really good at it? Do i need to learn other Gen AI framework like llama
 index or auto gen or try to make different types of agents with different framework? I am confused and i hope you guys 
got my point, what I am trying to ask. It's not because of hype but i am genuinely interested about it. 

```
---

     
 
all -  [ Help with langchain apis - there are too many to figure out ](https://www.reddit.com/r/LangChain/comments/1hk3798/help_with_langchain_apis_there_are_too_many_to/) , 2024-12-23-0913
```
I need to be able to analyze 2 sets of custom information, and answer a provided prompt with a custom output template I 
provide. What is the bare minimum JS apis I should use for this just to get started?

Assuming the custom information an
d template and prompt are all hard-coded strings, which objects should I use? I know there is way more to this so just g
etting the first POC I can grow. 


```
---

     
 
all -  [ BEST Generative AI course on Udemy? or Other platforms, Beginner level, LLMs, Langchain, Hugging Fac ](https://www.reddit.com/r/leetcode/comments/1hk2zko/best_generative_ai_course_on_udemy_or_other/) , 2024-12-23-0913
```
What are the skills required to be a Software Engineer AI. Please suggest the best courses on Generative AI, LLMs, Langc
hain, Hugging face and other skills.  
Udemy preferred, but other platforms also fine.
```
---

     
 
all -  [ Efficient way to load files from AWS S3 Bucket for data parsing (to be used in RAG) ](https://www.reddit.com/r/LangChain/comments/1hk1gy4/efficient_way_to_load_files_from_aws_s3_bucket/) , 2024-12-23-0913
```
I'm building a RAG solution for which I need to load PDF files from an AWS S3 bucket. I'm loading the entire file all at
 once and then passing it to pdfplumber for parsing the data. While this works for smaller PDFs, I've read that larger f
iles need to be streamed from S3 instead of loading all at once. I tried streaming the PDF file from S3 but unfortunatel
y, the pdfplumber package does not work on a streaming object.

I want to know what is the correct (industry standard) w
ay to load larger PDF files from S3 and then give it to some library/API to parse.
```
---

     
 
all -  [ Langgraph with Chainlit? ](https://www.reddit.com/r/LangChain/comments/1hk1a8e/langgraph_with_chainlit/) , 2024-12-23-0913
```
Hey guys I managed to build a RAG agent with langgraph and now wish to serve it through a backend onto a frontend. I loo
ked up and found Chainlit as a framework for serving chatbot agents. Has anyone here used chainlit in production before?
 The langgraph integration was quite easy to do which is nice however for everything else it seems quite limiting in my 
use case. I wish to send JSON objects from the backend over to my frontend however currently it only allows sending stri
ng messages from the backend afaik. Also has very limited components out of the box and not very customizable. Does anyo
ne have any better options or should I just suck it up, create my own backend and frontend from scratch?
```
---

     
 
all -  [ Resume review please, 1.4 YOE , resigned from last company 3 months ago due to Toxic culture and stu ](https://i.redd.it/puuf7axc8f8e1.jpeg) , 2024-12-23-0913
```
Hi, 

I got an offer during my final semester for a cybersecurity role but I wanted a SDE role and I didn’t have any oth
er offer. So I took it because I thought it was better than being unemployed.

Turns out it wasn’t worth working there, 
still I gained some knowledge tho.
I am actively applying from last 3 months but haven’t had any luck. 
I’m working on i
mproving my DSA skills and development.

Any advice or tips would really help.

Thanks
```
---

     
 
all -  [ Come migliorare davvero come ML-SW Engineer? ](https://www.reddit.com/r/ItaliaCareerAdvice/comments/1hjx53w/come_migliorare_davvero_come_mlsw_engineer/) , 2024-12-23-0913
```
Ciao a tutti,  
sono un M29 e attualmente lavoro in una multinazionale italiana dove ho la possibilità di partecipare a 
progetti interessanti in ambito software engineering e machine learning. Ho una grande passione per la tecnologia e l’in
telligenza artificiale, e il mio obiettivo, nei prossimi anni, è crescere professionalmente per diventare un ML Architec
t o una figura simile. Mi piacerebbe raggiungere un livello tale da poter ambire a posizioni in aziende di spessore Tech
 pur restando in Italia (tipo le FANG, ma so che in Italia c'è poco e niente e il remote sta finendo)

**Un po' di backg
round su di me:**  
Lavoro da 3 anni nel campo, sono un ingegnere ma non un ingegnere informatico. Ho studiato AI all’un
iversità e completato un master universitario in AI e Machine Learning, mentre il resto delle mie competenze l’ho svilup
pate da autodidatta, lavorando su progetti reali e sperimentando per conto mio. Questo approccio mi ha dato una buona ve
rsatilità tecnica, ma spesso il dover imparare tutto di fretta mi rende un po’ dipendente da ChatGPT per colmare le lacu
ne e andare veloce.

**Le mie skill attuali includono:**

* **Linguaggi e framework principali:** Python (con focus su M
L e AI), C# [ASP.NET](http://ASP.NET), React (JS e TS).
* **ML e AI:** Familiarità con MLOps (Mlflow, Kubeflow, Rayserve
, BentoML), AutoML, e librerie NLP come Haystack, Langchain e vLLM.
* **Cloud & Container:** Esperienza con Docker, K8S.

* **Database:** Uso avanzato di database relazionali e non (PostgreSQL, Elasticsearch/OpenSearch).
* **Extra:** Interes
se per la Responsible AI e buone basi di ETL.

**Cosa vorrei migliorare:**

1. **Data Structures & Algorithms:** Voglio 
finalmente approfondire seriamente le basi di strutture dati e algoritmi, argomento che so essere cruciale per ruoli più
 avanzati e per affrontare interviste tecniche di alto livello.
2. **LeetCode e coding challenges:** Sto pianificando di
 iniziare a esercitarmi su LeetCode o piattaforme simili, ma non so bene come strutturare l’approccio. Consigli su come 
iniziare o piani di studio?
3. **ML System Design:** Vorrei imparare come progettare sistemi ML su larga scala, approfon
dendo argomenti come deployment, monitoring e ottimizzazione di sistemi distribuiti.

**Cosa sto cercando:**

1. Consigl
i pratici su come migliorare tecnicamente per diventare ML Architect: best practice di design, gestione di progetti comp
lessi, capacità di leadership tecnica.
2. Risorse utili per approfondire data structures, algoritmi e ML system design: 
libri, corsi, tutorial, paper, qualsiasi cosa che mi aiuti a crescere.
3. Opinioni su corsi universitari o certificazion
i: vale la pena seguire corsi specialistici online o magari un secondo master?
4. Suggerimenti su come strutturare il mi
o apprendimento per bilanciare lo studio teorico con la pratica.
5. Idee su come costruire un profilo competitivo per az
iende di livello FANG, anche restando in Italia.

Sono molto motivato a fare il salto di qualità e a imparare tutto quel
lo che serve per arrivare a questi obiettivi. Ogni consiglio o spunto sarà davvero apprezzato! 😊

**NB:** so che i *full
 stack* forse non esistono, so che il mondo a cui punto è molto complesso, so di *non sapere.*   
Help Me :)


```
---

     
 
all -  [ nursing ethics ](https://www.reddit.com/r/LangChain/comments/1hjw8w2/nursing_ethics/) , 2024-12-23-0913
```
question book
```
---

     
 
all -  [ How to create an AI chat bot / LLM to identify limiting beliefs ](https://www.reddit.com/r/LangChain/comments/1hjun23/how_to_create_an_ai_chat_bot_llm_to_identify/) , 2024-12-23-0913
```
My friend came up with a process to uncover limiting beliefs.  I'm curious if an AI chat bot / LLM could be trained to d
o this automatically.

The whole process is described here

[https://docs.google.com/document/d/1QoGyrJD35UURjNWpj3bFwdE
Ew8xrkAuyD8-EOtrY0qs/edit?tab=t.0#heading=h.2l4ugw4t64m3](https://docs.google.com/document/d/1QoGyrJD35UURjNWpj3bFwdEEw8
xrkAuyD8-EOtrY0qs/edit?tab=t.0#heading=h.2l4ugw4t64m3)

FIrst you identify an area you want to work on / transform (care
er, relationships, money, etc.)

Then you come up with a handful of 'I'm afraid' statements.

Example:

I'm afraid that 
I'll be a failure, I'm afraid that people will reject me, etc.

Once you have a few of those listed, you look at the hid
den assumptions behind those fears, and what those fears presuppose to be true.

After you uncover the hidden assumption
s, you come up with a belief statement that summarizes everything.

How could him or I make an AI bot / LLM to automate 
this process?

Meaning, type in the area of life we'd like transform (work, relationship, money, spiritual, etc.)  Then 
the AI would prompt us to type a few 'I'm afraid' statements.

Afterwards, the AI bot / LLM would hopefully ask us quest
ions to identify the hidden assumptions behind each individual 'I'm afraid' statement.

Here are the hidden assumptions,
 with a description of each.

* **Necessity:** What are the “have to’s,” “have to *not*’s,” “must’s,” “need to’s,” or “s
hould’s”? Do these fears assume you lack choice or have to force yourself to do something? What are the unquestioned rul
es or “duties”?  
* **Impossibility:** What do these fears presuppose is impossible? What are the “can’t’s” and “couldn’
t’s,” the “it-would-never-work’s”?  
* **Authority:** What do these fears presuppose you don’t have *permission* or *aut
hority* to do? What would be too taboo to even consider doing? What are the “may not’s” the “not OKs”? The things that w
ould lead to ridicule, criticism, or being “canceled”?  
* **Future / Change:** Do these fears presuppose the future wil
l necessarily be the same or worse than the present? What do these fears assume is *unchanging*?  
* **Chunk size:** Do 
these fears assume you have to do everything, all at once? Or that you can take it bit by bit?  
* **Speed:** Is there a
n assumption that things *must* happen quickly? That you can’t go at a reasonable pace?  
* **Joy:** Is there a hidden a
ssumption that the path to where you want to go will be miserable? That there’s no way to enjoy the journey?  
* **Cost 
of Failure:** Is there an assumption there’s only one chance to get it right? That failure is permanent? Or that you hav
e lots of chances, and failure is no big deal because that’s the way you learn?  
* **Deletions:** Are these fears delet
ing most – or all – of your resources, strengths, and past successes? When in the grips of these fears, do you find it d
ifficult to even remember what your strengths and past successes are?  
* **Others:** Do these fears presuppose you are 
alone in this, have to do it yourself, or that you don’t have support? That you are the only one who has ever dealt with
 this, and no one has ever succeeded at it, and no one would help you to succeed either?  
* **World:** What do these fe
ars presuppose about the external world? That it’s a wonderful, helpful, kind place, or a dystopian nightmare full of gr
eedy, selfish people?  
* **Universe / God:** From the perspective of these fears, what’s the relationship to The Univer
se or God or something equivalent? Is this dimension absent entirely? Is God “punishing you”? Are you experiencing “bad 
karma”? Are you forgetting your connection to the whole, the Oneness that pervades all things?

[https://docs.google.com
/document/d/1QoGyrJD35UURjNWpj3bFwdEEw8xrkAuyD8-EOtrY0qs/edit?tab=t.0#heading=h.2l4ugw4t64m3](https://docs.google.com/do
cument/d/1QoGyrJD35UURjNWpj3bFwdEEw8xrkAuyD8-EOtrY0qs/edit?tab=t.0#heading=h.2l4ugw4t64m3)


```
---

     
 
all -  [ Output Parser Llama 3.1-8B Instruct ](https://www.reddit.com/r/LLMDevs/comments/1hjtm8c/output_parser_llama_318b_instruct/) , 2024-12-23-0913
```
I’m using Meta-Llama 3.1 8B-Instruct to compare Human Cognitive memory results and testing the Model under same conditio
n and tests and then comparing the results.  I am new to this and I need help in parsing the model output. I've tried fe
w things such as custom parser but that is not an ideal solution cuz conversational LLM tends to output different result
s every time. 

For example:   
This is the output that I get from the model  
'  
 The valid English words from the giv
en list are: NUMEROUS, PLEASED, OPPOSED, STRETCH, MURCUSE, MIDE, ESSENT, OMLIER, FEASERCHIP.   
The words

Output from C
ustom Parser that I created:

Parsed Words \['NUMEROUS, PLEASED, OPPOSED, STRETCH, MURCUSE, MIDE, ESSENT, OMLIER, FEASER
CHIP.', 'The words'\]  
  
'  
I've checked langchain output parser but not sure regarding this:  
[https://python.langc
hain.com/docs/troubleshooting/errors/OUTPUT\_PARSING\_FAILURE/](https://python.langchain.com/docs/troubleshooting/errors
/OUTPUT_PARSING_FAILURE/)

  
Any help would be appreciated!!
```
---

     
 
all -  [ Been a while since the last time I got my resume roasted here so ](https://i.redd.it/47zzwomadc8e1.jpeg) , 2024-12-23-0913
```
I'm a third year student looking to apply for internships, please help me figure out how to improve my resume 
```
---

     
 
all -  [ Guidance related to building a restaurant booking chatbot.  ](https://www.reddit.com/r/LangChain/comments/1hjs3pd/guidance_related_to_building_a_restaurant_booking/) , 2024-12-23-0913
```
I took an NLP course this semester where I'm working on a project to build a restaurant reservation chatbot. The chatbot
 needs to capture user data (name, phone number, date, time), store it in a database, and check for reservation conflict
s.

I decided to go with Google’s Dialogflow API as it seemed to fit the use case well but my professor wanted me to exp
lore alternative approaches. I've started working with Llama using LangChain and implemented basic chatbot functionality
 using AIMessage and HumanMessage, and setting the prompt but I'm having trouble figuring out how to handle the database
 integration and conflict checking.

Would appreciate any guidance on what the right approach would be as well as any im
plementation tips. Thank you.
```
---

     
 
all -  [ Help regarding langchain app architecture. ](https://i.redd.it/cexi5dep5c8e1.jpeg) , 2024-12-23-0913
```
I am making something like the fastbots.ai
And this is my current architecture. I am plaaning on using-
1. 4o-mini for l
lm
2. Pinecone db for embeddings of each bot
3. Redis db for storing chats. 

As you can see that I am a bit lost. So pl
ease help me with moving on with this project. How can I improve the architecture and how to deploy the same.

```
---

     
 
all -  [ OpenServAi Agents Marketplace? ](https://i.redd.it/ka1ug4z2ba8e1.jpeg) , 2024-12-23-0913
```
Found this interesting that they're building a marketplace allowing Ai Agents from different frameworks, including Langc
hain to cooperate together. From my research, this is the most promising agents marketplace I have found so far. From th
eir youtube videos, was really impressed by the 'drag & drop' way of using different agents. Could be a game changer in 
my opinion..What do you guys think?
```
---

     
 
all -  [ Need Help!!!!!!!!!URGENT!!!! ](https://www.reddit.com/r/Btechtards/comments/1hjj818/need_helpurgent/) , 2024-12-23-0913
```
i am currently in an IIT (top 5) and completed my 3rd semester and i can see my future dark the thing is my cgpa is not 
goot (7.53) but am really interested in deep learning and machine learning have a strong foundation in basic ml algorith
ms deep learning neural networks cnns rnns lstms generative models like gans vaes (read many papers related to them too)
 and currently im exploring RAG langchain and finding that interesting too but after next semester my intern season will
 come and they ask dsa and honestly i dont like dsa at all i cant just do dsa all day long can u pls suggest how should 
i proceed so i can get a good internship plsss help
```
---

     
 
all -  [ Noob looking for guidance on LLM selection ](https://www.reddit.com/r/GenAI_Dev/comments/1hje1vh/noob_looking_for_guidance_on_llm_selection/) , 2024-12-23-0913
```
Today, I came across a common question on Reddit and shared my response. I'm posting it here to reach a broader audience
, as I believe many beginners have similar questions.

*Question on* r/LLMDev *subreddit:*

>Hello, I'm making a project
 where every user has 10k input tokens and 400 output tokens worth of interaction at least 200 times a month. The projec
t is for general use(Like general knowledge question, or generating mathematical questions). Basically, it won't be much
 related to programming so IK Claude isn't the best option.

\[Read on [Reddit](https://www.reddit.com/r/LLMDevs/comment
s/1hepy6n/comment/m2720rl/)\]

*My response:*

To approach this systematically, we can evaluate the options across three
 key dimensions:

https://preview.redd.it/hth5pzz0h88e1.png?width=1280&format=png&auto=webp&s=d61b2e6ad25ebbf7f529bbaafa
10dad300e0a543

**Dimension 1: Model Complexity**

For your use case—handling general knowledge queries and generating m
athematical questions—domain-specific expertise isn’t required. Any general-purpose LLM with 7B-13B parameters should su
ffice. Models like GPT-4 (by OpenAI), or similar alternatives from providers such as Cohere, Anthropic (Claude), or Mist
ral could work. In general, larger models (e.g., 27B or 70B) often provide higher-quality results but come at increased 
costs. The question you should be asking is if you REALLY need the best performing model (e.g., 70B)? Let's dive a bit d
eeper by thinking about quality.

**Dimension 2: Quality**

Quality depends on your project’s specific needs. If precise
 and nuanced answers are essential, GPT-4 or Claude might be better choices, but they cost more. If you can tolerate sli
ghtly less sophistication, models like Llama 3 (no offense to LLaMMA fans :-) ) or other open source models such as Falc
on provide good performance at a lower cost, especially when hosted locally or through cost-efficient APIs.

Bottom line
 is that while smaller models (7B-13B) are cost-effective, larger models tend to produce higher-quality, nuanced outputs
. It’s a good idea to experiment with smaller models first to determine if they meet your quality requirements. They off
er the advantages of lower costs and better latency, making them a practical starting point.'

**Dimension 3: Cost**

Co
st plays a pivotal role in API/LLM selection.

Let's estimate cost of using different LLM available as a service - based
 on your requirements:

Input tokens = 10k

Output tokens = 400

Number of calls = 200

**NOTE:**

* Do your own price c
alculation - I don't know about the accuracy of the [website](https://gptforwork.com/tools/openai-chatgpt-api-pricing-ca
lculator) I used for generating these comparative pricing.
* Multiple cost x (number of users)
* Don't forget to factor 
in the development/QA cost
* Self hosted LLMs will require infrastructure which by the way is not cheap :-)

https://pre
view.redd.it/ahp8h49qg88e1.png?width=1200&format=png&auto=webp&s=9124d97dd6b325f4ea369924b1c76cf31c094ef3

In your parti
cular scenario, the cost is relatively low, so I’d recommend going for the best option. 😊

That said, keep in mind that 
costs for real-world applications can be significantly higher. To provide a complete picture, here are some suggestions 
for cost optimization

*Cost-Optimization Tips*

Here are some strategies to reduce costs without compromising too much 
on quality:

1. **Fine-tune smaller models:** Train a smaller model to specialize in your specific queries.
2. **Hybrid 
approach:** Use larger models only for complex queries while leveraging smaller ones for routine tasks.
3. **Context opt
imization:** Use vector databases (e.g., Pinecone) with LangChain to minimize input token usage by feeding only relevant
 data to the model.

**My 2 Cents**

If you’re new to the world of LLMs, making these decisions can be daunting. A struc
tured course on LLMs can help you navigate these options more effectively and avoid common pitfalls. If you’re intereste
d, check out my course designed specifically for beginners—it provides actionable guidance and helps you get up to speed
 quickly.

[https://youtu.be/Tl9bxfR-2hk](https://youtu.be/Tl9bxfR-2hk)
```
---

     
 
all -  [ Just reached 1000 AI agents added to Agent Locker 🥳 ](https://i.redd.it/ktkoa6l1u68e1.png) , 2024-12-23-0913
```
Thanks for all the support we've had from this sub! 

We're just about to launch the 3rd party provider section so if yo
u're a consultant or agency get in touch. 

https://www.agentlocker.ai 


```
---

     
 
all -  [ Stuck on implementing memory for a multiuser chatbot ](https://www.reddit.com/r/LangChain/comments/1hj7ivs/stuck_on_implementing_memory_for_a_multiuser/) , 2024-12-23-0913
```
Hello everyone, a student here, made a discord study group/ team up server for my uni, and wanted to add a discord bot f
or a chatbot, so I picked up langchain, and from there learnt LCELs and moved to langgraph, but now memory is giving me 
a problem, I have set up a memorysaver with checkpoint for now which uses discord ID's of people as threadID's but this 
isn't scalable, I have never made projects for scale involving databases and deployment and async stuff, I was looking i
nto store, but it seems semantic search is the only way to go ahead with this, but is it really the best approach to set
up a vector store for every person who has had a conversation with the bot?

This might be a backend question more than 
a Langchain one, but I don't know where else to ask as I got no mentor
```
---

     
 
all -  [ First RAG App: Seeking Feedback and Help with Follow-Ups and Response Time ](https://www.reddit.com/r/LangChain/comments/1hj7h78/first_rag_app_seeking_feedback_and_help_with/) , 2024-12-23-0913
```
Hello everyone! I love how awesome this community is and after reading a few beginner posts, I finally mustered up the c
ourage to share my own work.

This is my first RAG app built as part of my university project. I relied on official docu
mentation and a few YouTube tutorials to understand the process and finally got it working! The app is designed to help 
me study using the notes provided by our university, which are primarily in PDF format. As a result, the app currently s
upports PDFs as its sole input source.

# Current Challenges:

1. Follow-Up Questions: My app struggles to handle follow
-up queries effectively. Are there any tips or techniques I can implement to make it more contextually aware?
2. Respons
e Time: The app is responding quite slowly. Are there ways to optimize performance and make it respond faster?

# Additi
onal Info:

* The app is hosted on [https://asknotes.streamlit.app/](https://asknotes.streamlit.app/)
* **streamlit** & 
**streamlit\_chat**: For building and visualizing the app.
* **langchain**, **langchain\_community**, & **langchain\_ope
nai**: For the RAG pipeline.
* **faiss-cpu**: For vector search.
* **pypdf**: For extracting text from PDFs to build my 
knowledge base.

Would love any general feedback or advice to improve!

Thanks for taking the time to read my post. I’m 
looking forward to learning from your experiences and suggestions!
```
---

     
 
all -  [ LangChainJS - Tool calling with JSON schemas ](https://www.reddit.com/r/LangChain/comments/1hiw84b/langchainjs_tool_calling_with_json_schemas/) , 2024-12-23-0913
```
New to LangchainJS, and looking for confirmation that I'm staring at a bug.

I'm trying to take a bunch of tools defined
 in JSON schema and convert them into `DynamicStructuredTool`.  I'm partially successful, in that I'm getting the tools 
to be called from the LLM, but the payloads are empty.

I think the reason why is that I'm seeing the `DynamicStructured
Tool` constructor code just throw away the payload schema if the schema is *not* a JSON schema passed in.  

    this.sc
hema = (
    isZodSchema(fields.schema) ? fields.schema : z.object({}).passthrough()

[https://github.com/langchain-ai/l
angchainjs/blob/main/langchain-core/src/tools/index.ts#L460-L461](https://github.com/langchain-ai/langchainjs/blob/main/
langchain-core/src/tools/index.ts#L460-L461)

  
Is there something I'm missing?
```
---

     
 
all -  [ Lessons learned from building a context-sensitive AI assistant with RAG ](https://www.reddit.com/r/LangChain/comments/1hirwgr/lessons_learned_from_building_a_contextsensitive/) , 2024-12-23-0913
```
I recently built an AI assistant for Vectorize (where I'm CTO) and wanted to share some key technical insights about bui
lding RAG applications that might be useful to others working on similar projects. Some interesting learnings from the p
rocess: 

1. Context improves retrieval quality significantly - By embedding our assistant directly in the UI and using 
page context in our retrieval queries, we got much better results than just using raw user questions. 
2. Real-time, mul
ti-source data creates a self-improving system - We combined docs, Discord discussions, and Intercom chats. When we tag 
new support answers, they automatically get processed into our vector index. The system improves through normal daily ac
tivities. 
3. Reranking models > pure similarity search - Vector similarity scores alone weren't enough to filter out ir
relevant results (e.g., getting S3 docs when asking about Elasticsearch). Using a reranking model with a relevance thres
hold of 0.5 dramatically improved response quality. 
4. Anti-hallucination prompting is crucial - Even with good retriev
al, clear LLM instructions matter. We found emphasizing 'only use retrieved content' and adding topic context in prompts
 helped prevent hallucination, even with smaller models. The full post goes into implementation details, code examples, 
and more technical insights: 

[https://vectorize.io/creating-a-context-sensitive-ai-assistant-lessons-from-building-a-r
ag-application/](https://vectorize.io/creating-a-context-sensitive-ai-assistant-lessons-from-building-a-rag-application/
)

Happy to discuss technical details or answer questions about the implementation!
```
---

     
 
all -  [ Error  when i stream my graph  ](https://www.reddit.com/r/LangChain/comments/1hinulz/error_when_i_stream_my_graph/) , 2024-12-23-0913
```
    am using gemnai  as llm 

    ValueError: no signature found for builtin type <class 'dict'>ValueError: no signature
 found for builtin type <class 'dict'>



my code 

    from typing import Literal, List, Union
    from typing_extensio
ns import TypedDict
    from langchain_anthropic import ChatAnthropic
    from langchain_core.messages import HumanMessa
ge
    from langgraph.graph import StateGraph, START, END, MessagesState
    from langgraph.prebuilt import create_react
_agent
    from langgraph.types import Command
    from langchain_google_genai import ChatGoogleGenerativeAI
    from la
ngchain_anthropic import ChatAnthropic
    
    
    
    
    # Create the LLM
    llm = ChatGoogleGenerativeAI(
      
  model='gemini-1.5-pro',
        temperature=0,
        api_key='xcxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
    )
    # Def
ine team members and create literal type
    members = ['backlog_planner', 'sprint_planner']
    options = members + ['F
INISH']
    NextType = Literal['backlog_planner', 'sprint_planner', 'FINISH']
    
    # System prompt for supervisor
  
  system_prompt = (
        'You are a supervisor tasked with managing a conversation between the'
        f' following 
workers: {members}. Given the following user request,'
        ' respond with the worker to act next. Each worker will p
erform a'
        ' task and respond with their results and status. When finished,'
        ' respond with FINISH.'
    
)
    
    # Define router type with explicit literals
    class Router(TypedDict):
        '''Worker to route to next. 
If no workers needed, route to FINISH.'''
        next: NextType
    
    # Create supervisor node with explicit return 
type
    def supervisor_node(state: MessagesState) -> Command[Union[Literal['backlog_planner', 'sprint_planner'], Litera
l['__end__']]]:
        messages = [
            {'role': 'system', 'content': system_prompt},
        ] + state['messag
es']
        response = llm.with_structured_output(Router).invoke(messages)
        goto = response['next']
        if g
oto == 'FINISH':
            goto = END
        return Command(goto=goto)
    
    # Rest of your code remains the same

    backlog_agent = create_react_agent(
        llm, 
        tools=[get_info_for_backlog],
        state_modifier='''
 
       You are a Business analyst, your job is to detail the product backlog that includes:
        Epics: High-level re
quirements outlining significant chunks of functionality.
        User Stories: Smaller, actionable requirements that de
tail what needs to be achieved.
        Acceptance Criteria: Conditions that a user story must satisfy to be accepted as
 complete
        '''
    )
    
    def backlog_node(state: MessagesState) -> Command[Literal['supervisor']]:
        r
esult = backlog_agent.invoke(state)
        return Command(
            update={
                'messages': [
         
           HumanMessage(content=result['messages'][-1].content, name='backlog_planner')
                ]
            },

            goto='supervisor',
        )
    
    sprint_agent = create_react_agent(
        llm, 
        tools=[get_i
nfo_for_sprint],
        state_modifier='''
        You are a Project Manager your job is to create:
        Critical Pa
th Analysis: Identifying user stories and tasks that are dependent.
        Generate a sprints plan that ensures:
      
  - User stories and tasks Prioritization
        - Timeline Assignment
        - Human resources allocation
        '''

    )
    
    def sprint_node(state: MessagesState) -> Command[Literal['supervisor']]:
        result = sprint_agent.i
nvoke(state)
        return Command(
            update={
                'messages': [
                    HumanMessage
(content=result['messages'][-1].content, name='sprint_planner')
                ]
            },
            goto='super
visor',
        )
    
    # Build the graph
    builder = StateGraph(MessagesState)
    
    # Add nodes and edges
    
builder.add_edge(START, 'supervisor')
    builder.add_node('supervisor', supervisor_node)
    builder.add_node('backlog_
planner', backlog_node)
    builder.add_node('sprint_planner', sprint_node)
    builder.add_edge('supervisor', 'backlog_
planner')
    builder.add_edge('supervisor', 'sprint_planner')
    builder.add_edge('backlog_planner', 'supervisor')
   
 builder.add_edge('sprint_planner', 'supervisor')
    builder.add_edge('supervisor', END)
    
    # Compile the graph
 
   graph = builder.compile()
    
    # Initialize and run
    initial_state = {
        'messages': [
            ('use
r', 'Let's start planning the project. What are the main requirements?')
        ]
    }
    from IPython.display import
 display, Image
    
    display(Image(graph.get_graph().draw_mermaid_png()))
    
    # Stream the graph execution
    
for s in graph.stream(initial_state, subgraphs=True):
        print(s)
        print('----')
    from typing import Lite
ral, List, Union
    from typing_extensions import TypedDict
    from langchain_anthropic import ChatAnthropic
    from 
langchain_core.messages import HumanMessage
    from langgraph.graph import StateGraph, START, END, MessagesState
    fr
om langgraph.prebuilt import create_react_agent
    from langgraph.types import Command
    from langchain_google_genai 
import ChatGoogleGenerativeAI
    from langchain_anthropic import ChatAnthropic
    
    
    
    
    
    # Create th
e LLM
    llm = ChatGoogleGenerativeAI(
        model='gemini-1.5-pro',
        temperature=0,
        api_key='AIzaSyB3
2phvdWNdNzH6R6sKvR8EKfVmJPE5hV4'
    )
    # Define team members and create literal type
    members = ['backlog_planner
', 'sprint_planner']
    options = members + ['FINISH']
    NextType = Literal['backlog_planner', 'sprint_planner', 'FIN
ISH']
    
    
    # System prompt for supervisor
    system_prompt = (
        'You are a supervisor tasked with manag
ing a conversation between the'
        f' following workers: {members}. Given the following user request,'
        ' re
spond with the worker to act next. Each worker will perform a'
        ' task and respond with their results and status.
 When finished,'
        ' respond with FINISH.'
    )
    
    
    # Define router type with explicit literals
    cla
ss Router(TypedDict):
        '''Worker to route to next. If no workers needed, route to FINISH.'''
        next: NextTy
pe
    
    
    # Create supervisor node with explicit return type
    def supervisor_node(state: MessagesState) -> Com
mand[Union[Literal['backlog_planner', 'sprint_planner'], Literal['__end__']]]:
        messages = [
            {'role':
 'system', 'content': system_prompt},
        ] + state['messages']
        response = llm.with_structured_output(Router
).invoke(messages)
        goto = response['next']
        if goto == 'FINISH':
            goto = END
        return Co
mmand(goto=goto)
    
    
    # Rest of your code remains the same
    backlog_agent = create_react_agent(
        llm,
 
        tools=[get_info_for_backlog],
        state_modifier='''
        You are a Business analyst, your job is to de
tail the product backlog that includes:
        Epics: High-level requirements outlining significant chunks of functiona
lity.
        User Stories: Smaller, actionable requirements that detail what needs to be achieved.
        Acceptance C
riteria: Conditions that a user story must satisfy to be accepted as complete
        '''
    )
    
    
    def backlo
g_node(state: MessagesState) -> Command[Literal['supervisor']]:
        result = backlog_agent.invoke(state)
        ret
urn Command(
            update={
                'messages': [
                    HumanMessage(content=result['message
s'][-1].content, name='backlog_planner')
                ]
            },
            goto='supervisor',
        )
    

    
    sprint_agent = create_react_agent(
        llm, 
        tools=[get_info_for_sprint],
        state_modifier=''
'
        You are a Project Manager your job is to create:
        Critical Path Analysis: Identifying user stories and 
tasks that are dependent.
        Generate a sprints plan that ensures:
        - User stories and tasks Prioritization

        - Timeline Assignment
        - Human resources allocation
        '''
    )
    
    
    def sprint_node(state
: MessagesState) -> Command[Literal['supervisor']]:
        result = sprint_agent.invoke(state)
        return Command(

            update={
                'messages': [
                    HumanMessage(content=result['messages'][-1].conte
nt, name='sprint_planner')
                ]
            },
            goto='supervisor',
        )
    
    
    # Bui
ld the graph
    builder = StateGraph(MessagesState)
    
    
    # Add nodes and edges
    builder.add_edge(START, 'su
pervisor')
    builder.add_node('supervisor', supervisor_node)
    builder.add_node('backlog_planner', backlog_node)
   
 builder.add_node('sprint_planner', sprint_node)
    builder.add_edge('supervisor', 'backlog_planner')
    builder.add_e
dge('supervisor', 'sprint_planner')
    builder.add_edge('backlog_planner', 'supervisor')
    builder.add_edge('sprint_p
lanner', 'supervisor')
    builder.add_edge('supervisor', END)
    
    
    # Compile the graph
    graph = builder.com
pile()
    
    
    # Initialize and run
    initial_state = {
        'messages': [
            ('user', 'Let's start 
planning the project. What are the main requirements?')
        ]
    }
    from IPython.display import display, Image
 
   
    
    display(Image(graph.get_graph().draw_mermaid_png()))
    
    
    # Stream the graph execution
    for s i
n graph.stream(initial_state, subgraphs=True):
        print(s)
        print('----')
```
---

     
 
all -  [ Help Me Build the Home Depot of AI ](https://www.reddit.com/r/LangChain/comments/1hil1l5/help_me_build_the_home_depot_of_ai/) , 2024-12-23-0913
```
I own a 2 month old startup Analytics Depot and for 2025, I'm aiming to make it the one stop shop for AI solutions. Like
 Home Depot, but for AI + Analytics. It will have industry related AI solutions for insurance, real estate, finance, leg
al, medical, oil and gas, management, etc. Can add additional services through APIs or something.



Right now I got 2 f
unctioning versions built. (Don't judge me, my experience is below basic :|)

1) Plain chatgpt wrapper with prompting fo
r the different industries.

2) Wrapper with domain specific BERT models for the different industries. 



I'm looking f
or qualified individuals who have lots of knowledge and experience in this space and can take this to another level. Rea
lly hoping to make this a $B+ company and I think the branding is perfectly positioned for that. Give Data Bricks and Sn
owFlake a few reasons to fight over us.



I'm looking for solutions that can get such valuations. In exchange, I can of
fer pay or equity or a combination of the two.



If this sounds interesting, DM me.
```
---

     
 
all -  [ Fast sentence transformer embeddings generation on CPU for question answering ](https://www.reddit.com/r/LangChain/comments/1hiil85/fast_sentence_transformer_embeddings_generation/) , 2024-12-23-0913
```
We have millions of documents which we want to be searchable through direct question answering (snippet based, as oppose
d to generation based, like the highlighted snippet in the following screenshot below the generated bit in Google)

http
s://preview.redd.it/4rwpsmw3yz7e1.png?width=1866&format=png&auto=webp&s=ea0178b40fc1a66a97beee7596cb70a8de52bbe1

So, fo
r this, we have to generate embeddings for all those millions of documents, put them in vector DB, and make them queryab
le at runtime. GPUs are outside our budget, so we have to do this on CPUs alone. Questions:

1. Any CPU friendly embeddi
ng model or architecture which enables us to extract sentence embeddings for all documents in our collection (followed b
y insertion in vector DB) at a pretty quick speed (comparable to GPUs) - even if it means keeping the number of dimensio
ns modest (as long as the snippet answer quality is decent)?
2. Any CPU friendly vector DB which would allow us infering
 snippets given a question at runtime pretty much in real time for high volume traffic (much like Google does here)? If 
the bottleneck for this is CPU cores, let us assume we have lots of them, since even then they are an order of magnitude
 cheaper than GPUs like A100 or H100.
3. Whatever solutions exist to the above questions - will they automatically apply
 to multiple languages, or do we have to further training and retraining with corpuses from those languages to make this
 work?
4. Will generating binary sentence embeddings on CPUs do it much faster (offsetting whatever delays normal senten
ce transformers achieve on CPUs instead of GPUs)? Like Matryoshka Embeddings?
```
---

     
 
all -  [ Straightforward way to persist memory ](https://www.reddit.com/r/LangChain/comments/1hihvwd/straightforward_way_to_persist_memory/) , 2024-12-23-0913
```
I'm making an agent with LangGraph and want to persist its chat memory across sessions. There are no multiple users so a
 database may be overkill. I'm aware I need to use MemorySaver and a store. However it's unclear to me what persistent s
tores are implemented and if it will suffice to just add the MemorySaver and the store object to the graph, or if any ad
ditional code is needed to write messages to memory and restore them at the start of a session. 
```
---

     
 
all -  [ Looking for Help with LangChain Course – Your Support Would Mean a Lot! ](https://www.reddit.com/r/UdemyCoders/comments/1higtcg/looking_for_help_with_langchain_course_your/) , 2024-12-23-0913
```
Hi everyone,

I’m eager to learn from the course '[Learn LangChain: Build 22 LLM Apps Using OpenAI & Llama 2](https://ww
w.udemy.com/course/learn-langchain-build-12-llm-apps-using-openai-llama-2/?couponCode=KEEPLEARNING).' If someone has acc
ess to this course and can help me out, I’d be extremely grateful!

Looking forward to any support or guidance you can p
rovide.

Thanks in advance,

Rahul
```
---

     
 
all -  [ Good library for LLM management ](https://www.reddit.com/r/rust/comments/1highnw/good_library_for_llm_management/) , 2024-12-23-0913
```
I have a personal project already running that uses the async-openai crate for LLM management, effectively limiting myse
lf to OpenAI‘s models. 
Now I want to switch to another library to support other LLM providers too. 

My sight is on lan
gchain-rust, as it would support all large providers, but the project is pretty dead; little commits and many open issue
s. Any good suggestions for other libraries?

Edit: sorry, I forgot to add that I want the library to stream tool calls
```
---

     
 
all -  [ HELP: Not able to use embeddings from langchain_huggingface library (HuggingFaceEmbeddings) due to s ](https://www.reddit.com/r/LangChain/comments/1hiekwz/help_not_able_to_use_embeddings_from_langchain/) , 2024-12-23-0913
```
Hi all

    from langchain_huggingface import HuggingFaceEmbeddings
    embeddings = HuggingFaceEmbeddings(model_name='B
AAI/bge-large-en')

Running this code is giving me this error   
`Could not import sentence_transformers python package.
 Please install it with \`pip install sentence-transformers\`.`

I have tried the following but could not get it working


* `pip install sentence-transformers`  
* Degrading version to `sentence-transformers==2.6.0`
* Try using python 3.9, 
3.10, 3.11, 3.12

Has anyone faced this? Here are the packages installed

* `langchain                               0.3
.13`
* `langchain-community                     0.3.13`
* `langchain-core                          0.3.28`
* `langchain-
huggingface                   0.1.2`
* `torch                                   2.5.1` 
* `transformers                 
           4.47.1`
* `sentence-transformers                   3.3.1`
```
---

     
 
all -  [ Tables chucking strategy  ](https://www.reddit.com/r/LangChain/comments/1hiekwp/tables_chucking_strategy/) , 2024-12-23-0913
```
I'm working on a Unstructured pdf document with each page containing Some text and multiple tables some tables spanning 
3-4 pages sometimes.


Issue : I'm not able to find an appropriate chucking methodology for tables spanning multiple pag
es as the next page table missing out the data related to previous one and not able to combine them based on a common po
int.


Using Pymupdf4llm  as a document parser and chucking each page as a one chunk for now. 

```
---

     
 
all -  [ LangGraph Tool/Multi-Agent conceptual question ](https://www.reddit.com/r/LangChain/comments/1hibhj8/langgraph_toolmultiagent_conceptual_question/) , 2024-12-23-0913
```
Hi LangChain/LangGraph community.

I'm trying to understand how to build this functionality using either a multi agent a
rchitecture or multiple tools. I have a chat interface and I need to keep track of state throughout a user's chat thread
. For each user message, I need to update a object with a summary of what the user said, and I am using an llm with stru
ctured output to update that state. I also need to then possibly call other tools depending on the input. For example, f
or some input, I need to make a call to the database to fetch some information. I also want to store every chat message 
sent by either the AI or the human, and also update the state in the database on every response.

Is this type of workfl
ow more suitable for a single agent with multiple tools? Or should I make a separate agent for each task that needs to b
e done? Thanks!
```
---

     
 
all -  [ Automation Software Testing Engineer here, looking to make shift to a career in AI engineering. ](https://www.reddit.com/r/cscareerquestions/comments/1hib7lc/automation_software_testing_engineer_here_looking/) , 2024-12-23-0913
```
I have total experience of 6 years into software testing / QA. I have worked on python, did some certifications in Gen A
I & Langchain and still few in progress. I am creating projects side by side as well.
My question - Is it absolutely nec
essary to have core dev experience ? Do companies consider the knowledge and self taught projects that an individual pos
sess or they only consider AI Engineers with ‘relevant’ experience ??
```
---

     
 
all -  [ Did a quick comparison between 10 LLMs for OCR task ](https://www.reddit.com/r/LangChain/comments/1hi9ee7/did_a_quick_comparison_between_10_llms_for_ocr/) , 2024-12-23-0913
```
Video: [https://youtu.be/yT-7i5npRBQ?feature=shared](https://youtu.be/yT-7i5npRBQ?feature=shared)

Code: [https://github
.com/trancethehuman/ai-workshop-code/tree/main/projects/ocr-battle](https://github.com/trancethehuman/ai-workshop-code/t
ree/main/projects/ocr-battle)

  
Let me know which ones you're currently using - I'd love to know if gemini is still th
e best for the price / performance.
```
---

     
 
all -  [ Self-Aware Software Using LangChain & LangGraph ](https://www.reddit.com/r/LangChain/comments/1hi8c3y/selfaware_software_using_langchain_langgraph/) , 2024-12-23-0913
```
Hello,

Weve been able to merge an LLM with our LangGraph Agent Builder. 

This turns our product from a piece of static
 software into a reasoning agent. In these two short demos I show how we ask our tool to perform functions within the to
ol. The LLM and our tool become one. Enjoy!

https://youtu.be/jSz-95OS_ik?si=CAgMjayyxxAjPjGl

https://youtu.be/iiDWPlro
rs4?si=BB2HlzRr0e_Ua7tC
```
---

     
 
all -  [ [1 YoE] Computer Science Graduate, International student applying to jobs in the ML/AI Field. ](https://www.reddit.com/r/EngineeringResumes/comments/1hi60ro/1_yoe_computer_science_graduate_international/) , 2024-12-23-0913
```
I have 1 year of co-orporate experience and 3 internships. I am an interantional student who has applied for opt and sea
rching jobs with sponsership. I have developed my skills in the vast galaxy of computer science towards the things I lov
e to do - Machine Learning (cliche right?). Any help as appericaited.

https://preview.redd.it/rihct0zv1w7e1.png?width=1
700&format=png&auto=webp&s=1432e633482db8a7a6846b2d153ac620f8b8d95f


```
---

     
 
all -  [ How do CustomGPTs from ChatGPT work in the background with the knowledge base? ](https://www.reddit.com/r/ChatGPTPro/comments/1hi5zo2/how_do_customgpts_from_chatgpt_work_in_the/) , 2024-12-23-0913
```
Here is a description of how RAG structures are constructed: [https://python.langchain.com/docs/tutorials/rag/](https://
python.langchain.com/docs/tutorials/rag/) I now wonder: Does a CustomGPT already do this with the uploaded data? Or does
 it make sense to integrate such a RAG structure yourself?

Theoretically, it could also be that ChatGPT does not carry 
out this processing and simply checks which file could contain what is needed and adds it internally as a whole as the c
ontext of the request.

What would you guess is how it works in practice?
```
---

     
 
all -  [ Wie arbeiten CustomGPTs von ChatGPT im Hintergrund mit der Wissensbasis? ](https://www.reddit.com/r/KI_Welt/comments/1hi5xpi/wie_arbeiten_customgpts_von_chatgpt_im/) , 2024-12-23-0913
```
Hier wird ja beschrieben wie RAG Strukturen aufgebaut sind: [https://python.langchain.com/docs/tutorials/rag/](https://p
ython.langchain.com/docs/tutorials/rag/) Ich frage mich nun: Macht ein CustomGPT dies mit den hochgeladenen Daten bereit
s? Oder ist es sinnvoll, eine solche RAG Struktur selbst zu integrieren?

Theoretisch könnte es ja auch sein, dass ChatG
PT diese Verarbeitung nicht vornimmt und einfach nur prüft welche Datei könnte das enthalten was man braucht und es inte
rn insgesamt als Kontext der Anfrage hinzufügt.

Was wäre eure Vermutung wie es in der Praxis erfolgt?
```
---

     
 
all -  [ Any decents RAG document management tool? ](https://www.reddit.com/r/LangChain/comments/1hhziyd/any_decents_rag_document_management_tool/) , 2024-12-23-0913
```
Hi fellow devs,

Does anyone know if there's an opensource tool with built for managing RAG document?

Imagine a drag-an
d-drop web interface for users to upload multiple documents.

Once uploaded, the system should:

1. Store the documents 
in some kind of storage (like S3, Blob Storage).
2. Trigger a pipeline to handle chunking and embedding generation.
3. I
nsert the processed data into a database (vector DB like Pinecone, Weaviate, or Postgres).

I already have a QA chatbot 
set up, so I don’t need any chat functionality like Ragflow, Onyx or Open Web UI just the document ingestion pipeline wi
th a user-friendly web UI.

I checked out Qdrant UI and Milvus Attu but they seem to have only data management functiona
lity not the ingestion pipeline.

Does anyone know of existing tools or frameworks that can do this, or am I better off 
building something custom?

Thanks!
```
---

     
 
MachineLearning -  [ [P] Minima: local conversational retrieval augmented generation project (Ollama, Langchain, FastAPI, ](https://www.reddit.com/r/MachineLearning/comments/1h1pudq/p_minima_local_conversational_retrieval_augmented/) , 2024-12-23-0913
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

     
