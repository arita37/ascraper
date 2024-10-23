 
all -  [ 🚀 Senior Machine Learning Engineer Opportunity! ](https://www.reddit.com/r/mlops/comments/1g9uykp/senior_machine_learning_engineer_opportunity/) , 2024-10-23-0912
```
We are seeking a seasoned **Senior Machine Learning Engineer** to join our innovative team and drive cutting-edge AI pro
jects. If you have a passion for building scalable machine learning systems and want to work in a collaborative environm
ent, this could be your next career move!

**Required Hard Skills** 

* **4+ years** of ML engineering experience
* **Ba
chelor’s degree** in Computer Science or related
* Experience with **Python, ML libraries and AI/ML frameworks (PyTorch,
 HuggingFace, TensorFlow, etc.)** 
* Experience building **GenAI solutions using LLMs**, including frameworks like LangC
hain and LlamaIndex, prompt engineering, fine-tuning and serving models, and implementing common patterns like RAG and N
LQ 
* **Client-facing experience**
* **Familiarity with containerization and orchestration tools** 

Link to the full jo
b posting: [https://boards.greenhouse.io/lokainc/jobs/4067015007?gh\_src=ff064e7b7us](https://boards.greenhouse.io/lokai
nc/jobs/4067015007?gh_src=ff064e7b7us)
```
---

     
 
all -  [ Coding a GeoGuessr Auto AI Bot with vision LLMs ](https://www.reddit.com/r/geoguessr/comments/1g9uw7x/coding_a_geoguessr_auto_ai_bot_with_vision_llms/) , 2024-10-23-0912
```
Video Tutorial: Coding a GeoGuessr AI Bot using LangChain and different Vision LLMs (GPT-4o, Claude 3.5, and Gemini 1.5)
 [https://www.youtube.com/watch?v=OyDfr0xIhss](https://www.youtube.com/watch?v=OyDfr0xIhss)
```
---

     
 
all -  [ Chromadb ](https://www.reddit.com/r/vectordatabase/comments/1g9trrw/chromadb/) , 2024-10-23-0912
```
Having a verbal crash issue with chromadb under langchain. I am trying to put chunks to the db and it kills the kernel. 


Any idea how this a constant? 

Built all using .venv so there shouldn't be any package issues.



```
---

     
 
all -  [ Cv debutant junior en reconversion ](https://i.redd.it/is740ys26dwd1.jpeg) , 2024-10-23-0912
```
Bonjour les amis
J’ai posté mon cv il y’a 3 jours et suite aux conseilles des membres j’ai l’ai modifié ..
Vos avis svp 
? Merci d’avance 

```
---

     
 
all -  [ Chromadb ](https://www.reddit.com/r/LangChain/comments/1g9qt3p/chromadb/) , 2024-10-23-0912
```
Chroma always kills the kernel when trying to load a set of chunks into the newest established database. I haven't found
 a single work around. 
```
---

     
 
all -  [ [0 YoE] Struggling to Get Interview Callbacks for New Grad SWE Roles – Resume Feedback Needed ](https://www.reddit.com/r/EngineeringResumes/comments/1g9ojcr/0_yoe_struggling_to_get_interview_callbacks_for/) , 2024-10-23-0912
```
Hi everyone, I’m a recent grad (May 2024) currently looking for full-time, entry-level software engineering positions ac
ross pretty much any industry. I’m based in the northeast but have been applying to both remote and in-person roles nati
onwide. I’m  open to relocating.

Despite submitting applications for a few months now, I’ve only received a handful of 
OAs, which I’ve completed with perfect scores. However, I’ve been ghosted after this stage, and I guess the issue lies w
ith my resume–> when it reaches the hiring manager(?).

I’m looking for advice on improving the overall content quality 
of my resume. Does it accurately reflect my skills and work experience? Is there something about the structure or syntax
 that could be holding me back? Any feedback on how to make it stronger would be greatly appreciated, as I feel it’s the
 main reason I’m not getting interview opportunities.

There are no visa or citizenship complications in my search.

htt
ps://preview.redd.it/nhemkytyjcwd1.png?width=5100&format=png&auto=webp&s=c91b2d651943a73464c71890b1c3f136e097c37c



Tha
nks so much in advance for your help!
```
---

     
 
all -  [ Experiments with gpt-4o vision and architecture diagrams ](https://www.dsdev.in/experiments-with-gpt-4o-vision-and-architecture-diagrams) , 2024-10-23-0912
```

```
---

     
 
all -  [ Ollama stopped code from running? ](https://www.reddit.com/r/ollama/comments/1g9gi9p/ollama_stopped_code_from_running/) , 2024-10-23-0912
```
I have the following code, it is supposed to load a pdf file, turn it into text chunks, embedding these chunks and store
 them locally to the disk.

`# Import time module to track execution time`

`import time` 

`# Import document loader an
d text splitter`

`from langchain.document_loaders import PyPDFLoader`

`from langchain.text_splitter import RecursiveCh
aracterTextSplitter`

`# Import embedding model of Ollama`

`from langchain.embeddings import OllamaEmbeddings`

`# Impo
rt Chromadb for vector storage`

`from langchain.vectorstores.chroma import Chroma`



`# Define a text splitter functio
n along with splitting parameters`

`text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)`




`# STEP 1: Load the PDF and split it into chunks of text`

`start_time = time.time()  # Start the timer`

`loader = P
yPDFLoader('machinedesign-1-100.pdf')`

`docs = loader.load_and_split(text_splitter)  # or use: docs = loader.load(); sp
lits = text_splitter.split_documents(docs)`



`# STEP 2: Create an embedding tool`

`embeddings = OllamaEmbeddings(mode
l='llama3.1')`



`# STEP 3: Create embedding vectors and store them in the vector database`

`start_embedding_time = ti
me.time()  # Start the embedding timer`

`spice_db_Ollama = Chroma.from_documents(`

`docs,` 

`embedding=embeddings,` 


`persist_directory='MD_embeddings_Ollama'`

`)`

`embedding_time = time.time() - start_embedding_time`

`# Import time 
module to track execution time`



`# Total time taken for the entire process`

`total_time = time.time() - start_time`


`print(f'Total time for the process: {total_time:.2f} seconds')`

After successfully running the code, the embeddings a
re stored locally. However, 

`# Import time module to track execution time` and `print(f'Total time for the process: {t
otal_time:.2f} seconds')` are not printed. This leads me to wonder, if my program is somehow terminated before the end, 
and if the embeddings stored are complete. Could you please explain to me why this happens? I appreciate your help!
```
---

     
 
all -  [ Applied to many internships but couldn't convert them need a resume review  ](https://i.redd.it/sw1xu5goe9wd1.jpeg) , 2024-10-23-0912
```
I am Third year CSE student working primarily in ML(and its aggregates like DL and Gen AI) I have been applying for inte
rnships since the last two months of my second year and am already at the mid point of my third year.
Please review my r
esume and let me know if I can make it better 
```
---

     
 
all -  [ Need help in RAG using LLAMA for invoice extraction ](https://www.reddit.com/r/Rag/comments/1g9cdpm/need_help_in_rag_using_llama_for_invoice/) , 2024-10-23-0912
```
I'm currently invested on a project, where I'm planning to use RAG for extracting invoice from the pdf ,images, and some
 of the structured data, the process I'm using using right now is:



->Extraction of data (using PyMuPDF, PaddleOCR, an
d Extractors for structured data)



->Place the content and Write a prompt to retrieve from vectordb, (Langchain and Ch
romaDB is used)



->Used LLama to use the data from vectordb, to get a meaningful json data,



Problem is structure ke
ep on changing, Need Help!!. (Tried using instructor not fruitful, Im new to GenAi and RAG)
```
---

     
 
all -  [ Building a community/network around AI Agents ](https://www.reddit.com/r/LangChain/comments/1g9ag3l/building_a_communitynetwork_around_ai_agents/) , 2024-10-23-0912
```
Hey ya'll, I'm currently building a curated community for AI Accelerators who believe that AI Agents will put more power
 in the hands of individual creators and entrepreneurs.

We're going to have

- Constantly Updated News  
- Learning Res
ources  
- Hackathons and Investment Resources (getting your ideas funded)  
- AI Agent Marketplace (Trading post for AI
 Agent buyers and sellers)  
- Ongoing agent experiments that the community can get involved in  
- and much more as we 
grow

Me and my partner truly believe that AI will soon enable people to start enterprise level businesses on their own.
 Imagine you want to build a one-person software company run almost entirely by agents. We're not there yet but we're ge
tting closer, and we want to build platforms to make it insanely easy to build and manage these projects using AI Agents
.

If you're excited for AI Agents and what they will help us create, consider joining! This community will be active wi
thin the next week. 


```
---

     
 
all -  [ Shutting down a graph ](https://www.reddit.com/r/LangChain/comments/1g99yg2/shutting_down_a_graph/) , 2024-10-23-0912
```
I have an app that creates one graph for each campaign. Over a period of time, I expect to have 1000s of graphs to be cr
eated.   
Are there memory implications for this? Is there a proper way to shutdown graphs once their lifecycle is compl
eted?
```
---

     
 
all -  [ Organização para estudos ](https://www.reddit.com/r/brdev/comments/1g92g6c/organização_para_estudos/) , 2024-10-23-0912
```
Olá, espero que estejam todos bem. Minha dúvida é: como organizam seus estudos no geral?

Fui contratado para atuar em p
rojetos de IA como desenvolvedor Fullstack Jr em uma empresa bem legal, vai fazer dois meses que estou nela. As principa
is stacks que eu preciso saber é Python, FastAPI, SQLAlchemy, Vue e Nuxt, além de Git, AWS, Docker, etc. 
Tanto no traba
lho quanto por fora eu busco estudar essas tecnologias, mas também tento estudar libs de IA (Langchain, LangGraph, Llama
Index), além de algoritmos e estrutura de dados, ML/Federated Learning para o meu TCC, inglês... Caramba! Muito coisa! 


Eu imagino que muitos aqui passam/passaram por situações como essa, de ter que estudar várias coisas. Como vocês se org
anizam pra isso? Tem como fazer sem atrapalhar família, namoro, amigos, lazer e etc? 
```
---

     
 
all -  [ Advice on scaling project with backend LLMs for servers with multiple models and making better decis ](https://www.reddit.com/r/LocalLLaMA/comments/1g91mik/advice_on_scaling_project_with_backend_llms_for/) , 2024-10-23-0912
```
Hello,  
I am a beginner working on an AI project for commercial use, and I’m currently stuck. I’ve been using three mod
els: Faster-Whisper, LLaMA 3.1 8B, and Parler-TTS. I hooked them up using Hugging Face's `transformers` library. My main
 bottleneck right now is the LLaMA model for real-time responses. I initially used the [shenzhi-wang/Llama3-8B-Chinese-C
hat at v2](https://huggingface.co/shenzhi-wang/Llama3-8B-Chinese-Chat/tree/v2) model (v2 gguf), but it struggled with sp
ecific role-based JSON responses.

I switched to LLaMA 3.1 8B and 3.2 3B while using and testing all of these, and while
 they improved the accuracy of the responses, the speed dropped significantly. The response time is now around 3-4 secon
ds, whereas before it was closer to 0.5 seconds.

I’ve tried performance optimizations from [huggingface-llama-recipes/p
erformance\_optimization at main · huggingface/huggingface-llama-recipes](https://github.com/huggingface/huggingface-lla
ma-recipes/tree/main/performance_optimization), but haven't seen much improvement. I also encountered a strange error wh
en trying to compile with `torch` (specifically with `model.forward`) and I dont get any with just `model`.

Here’s my c
urrent setup:

* **Hardware**: NVIDIA 3090 on a Windows PC
* **Goal**: Achieve real-time responses within 1-2 seconds, u
sing all three models. For context, I start streaming audio and compute 2 seconds of audio in 3 sec but I could change m
odel I guess.

I’m considering the following options, but I’d love your advice on which approach to prioritize:

1. **Do
ckerize the setup and test on H100 cloud GPUs**, then optimize performance once it works on that infrastructure as I cou
ld use it in future for scaling.
2. **Check out the new gguf version of LLaMA 3.1** (like [shenzhi-wang/Llama3.1-8B-Chin
ese-Chat]()), since the previous gguf model was faster or some others.
3. **Revisit LLaMA-cpp** (not `cpp-python`, since
 I ran into dependency issues). I had a better performance with LLaMA-cpp, but the Docker setup confused me. I shifted t
o `transformers` for model management and download automation, but that has slowed things down. I’m considering whether 
to switch back or figure out llama-cpp-python.
4. **Experiment with other models like Qwen or Mistral** for specific rol
es (like role-playing), though I’m unsure if they’ll outperform LLaMA for my use case.
5. **Explore Ollama** for ease of
 use, but I feel LLaMA-cpp might still be better for performance, especially when planning to switch to vLLM or LangChai
n later (although that would require reworking the system, and I’m short on time).

What would you recommend as the fast
est way to prove these models can achieve real-time responses (around 1-2 seconds sequentially? Any suggestions on impro
ving the performance, especially in a production setting, would be appreciated as I need to figure out everything alone.

```
---

     
 
all -  [ langchain setup in vent ](https://www.reddit.com/r/LangChain/comments/1g8snq5/langchain_setup_in_vent/) , 2024-10-23-0912
```
I have been used to setting up a venv for every python project and wondering if anyone has done the same with langchain 
and any lLLM models like local llama  (free) AND OpenAI? 

I believe I should install llama on my machine and  only pyth
on packages (e.g., langchain ) can be installed in venv (via pip install).
```
---

     
 
all -  [ Efficient Web Crawling for Keeping Vector Databases Updated - Seeking Advice ](https://www.reddit.com/r/LangChain/comments/1g8scol/efficient_web_crawling_for_keeping_vector/) , 2024-10-23-0912
```
Hey folks,  
  
We're developing chatbots that answer questions based on domain-specific knowledge for our clients. Our 
current process involves:  
  
1. Crawling the client's website  
2. Uploading the content to a vector database  
3. Uti
lizing this database for AI-powered responses  
  
The challenge we're facing is keeping this information up-to-date. Ou
r clients want real-time accuracy, which theoretically means crawling their websites daily. However, we've encountered s
ome issues:  
  
1. Time: A single website can take several hours to crawl completely.  
2. Cost: We're using APIFY, whi
ch works well but gets expensive when run daily across multiple clients.  
  
We've done some research but haven't found
 a viable solution yet. I'm curious:  
  
- Is anyone facing similar challenges?  
- Has anyone solved this problem effi
ciently?  
- Are there any alternative approaches or tools we should consider?  
  
We're open to any suggestions or ins
ights from the community. Thanks in advance for your help!  
Hey folks,  
  
We're developing chatbots that answer quest
ions based on domain-specific knowledge for our clients. Our current process involves:  
  
1. Crawling the client's web
site  
2. Uploading the content to a vector database  
3. Utilizing this database for AI-powered responses  
  
The chal
lenge we're facing is keeping this information up-to-date. Our clients want real-time accuracy, which theoretically mean
s crawling their websites daily. However, we've encountered some issues:  
  
1. Time: A single website can take several
 hours to crawl completely.  
2. Cost: We're using APIFY, which works well but gets expensive when run daily across mult
iple clients.  
  
We've done some research but haven't found a viable solution yet. I'm curious:  
  
- Is anyone facin
g similar challenges?  
- Has anyone solved this problem efficiently?  
- Are there any alternative approaches or tools 
we should consider?  
  
We're open to any suggestions or insights from the community. Thanks in advance for your help! 
 

```
---

     
 
all -  [ LangChain and LangGraph: My Take and Some Questions ](https://www.reddit.com/r/LangChain/comments/1g8qvz4/langchain_and_langgraph_my_take_and_some_questions/) , 2024-10-23-0912
```
Hey folks, been messing around with LangChain and LangGraph lately. Thought I'd share my thoughts and see if anyone can 
help clear up some stuff.

The Good Stuff
- Loving the YouTube videos and tutorials. They've been a big help.
- Shout ou
t to Harrison Chase. Dude's commitment to making sense of all this LLM chaos is awesome. Appreciate the transparency too
.
- Loved seeing the Open Canvas codebase as well as the LangChain Chat project, learned so much studying them.

Where I
'm Stuck
1. LangGraph as a Platform: What exactly can I expect from it? Can I use it as my main database for chats and u
sers?

2. Keeping User Data Separate: What's the go-to method for this? Kinda crucial if I want to take this to producti
on.

3. Practical Stuff: Trying to do something simple - generate a thread title after the AI responds, then store it wi
th the thread in my database. Serializing BaseMessages works, but it breaks when I try to get them back. Any tips?

4. R
eal-World Use: Anyone actually running a production app on LangGraph? How's it holding up? Does it scale well?

What's Y
our Take?

If you've been hands-on with LangChain or LangGraph, especially in production, I'd love to hear from you. How
 are you handling data storage and keeping user stuff separate? Any pro tips for building solid, scalable apps with thes
e tools?
```
---

     
 
all -  [ C8工卡被拒后，我躺平在庇护所，白天在GitHub上做开源（langchain, llama index...）+写论文投arxiv，晚上躺在床上玩游戏...我后半辈子都这么过了嘛？还是等到川普上台后 ](https://www.reddit.com/r/iwanttorun/comments/1g8ojqf/c8工卡被拒后我躺平在庇护所白天在github上做开源langchain_llama/) , 2024-10-23-0912
```
远程给印度某大学远程授课
```
---

     
 
all -  [ Need help in Approach to Extracting and Chunking Tabular Data for RAG-Based Chatbot Retrieval ](https://www.reddit.com/r/LangChain/comments/1g8nshy/need_help_in_approach_to_extracting_and_chunking/) , 2024-10-23-0912
```
1.	I need to extract data from the tabular structures in the documents. What are the best available tools or packages fo
r this task?

2.	I’m seeking the most effective chunking method after extraction to optimize retrieval in a RAG setup. W
hat would be the best approach?

Any guidance would be greatly appreciated!
```
---

     
 
all -  [ Am I a bad job candidate? ](https://www.reddit.com/r/jobs/comments/1g8msv0/am_i_a_bad_job_candidate/) , 2024-10-23-0912
```
Hello, dear reddit.

For the most part I have been a Software Engineer (generally) for the last 5 years. I have been str
uggling in jobs with no planning whatsoever or even stability besides the one project that I have had the last 5 years a
s a personal colleague project in which I have already provided a first product to clients (this last one job is more li
ke a part time than anything). Currently I have been looking for a job because my most recent job the owner of the compa
ny has pretty much decided to close up the company for a few months, months in which I cannot been unemployed due to the
 current economy in which we are leaving and my responsabilities as a provider in my home.

As you may see in my resume.
 I'm really profficient on JS/TS technologies and Python alike and I'm someone very well disposed to work on new stuff d
ue to some academical knowledge on it like AI/ML with the usage of technologies like Langchain an so on and even if I ha
ve share my profile to several job positions that I may have that match to my profile I keep getting rejected with no fe
edback whatsoever leaving me completely clueless on what to do for the sake of improving my professional profile.

My in
tention on making this posts is pretty much ask for some councelling. I made you the 'anonymous' version of my personal 
Resume just for you to have a sneek peak on my profile and let you provide me your opinion to double check if ever happe
ns that my profile could be look a discartable one to any recruiter or even recruitment systems that maybe out there. I'
m up to receive from harsh critics to none just for the sake to know what I could improve of it ever happens that I'm ma
ybe looking in the wrong platforms or if I'm being targeted as non recommended candidate just for my country of origin.


Thank you beforehand and bless to you if you have at least look at my post.
```
---

     
 
all -  [ Sale My Ready MVP  ](https://www.reddit.com/r/saasforsale/comments/1g8lxde/sale_my_ready_mvp/) , 2024-10-23-0912
```
\*\*Dear Redditors,\*\*



I am looking to sell my ready MVP as I no longer have enough budget for marketing. I started 
this SaaS project, [SubGPT.ai](http://SubGPT.ai), about seven months ago, and my total investment was around $20,000.

(
Its Chatbase Alternative)

\*\*Project Features:\*\*

1. No-code ChatGPT-like app builder for your website.

2. Integrat
ions with WhatsApp, WordPress, Webflow, Weebly, Wix, Notion, Facebook Messenger, and Instagram.

3. Ability to embed any
 website.



\*\*Use Cases:\*\*

1. Lead Generation

2. Customer Support

3. Customer Engagement

4. Boosting Sales



\
*\*Tech Stack:\*\*

1. Python

2. JavaScript

3. WordPress theme for the homepage

4. HTML, CSS

5. Langchain



\*\*Pay
ment Gateway:\*\* Lemon Squeezy



\*\*What You Get:\*\*

1. Company Gmail account

2. AWS hosting

3. Transfer of WordP
ress hosting

4. LinkedIn company profile with over 350 followers

5. Instagram account

6. Threads account

7. X (forme
rly Twitter) page

8. Facebook page



\*\*Note:\*\* If you need support, my developer is available to help you build mo
re features (for a fee). 



Thank you for your interest!
```
---

     
 
all -  [ I need your help on LangGraph ](https://www.reddit.com/r/LangChain/comments/1g8jzik/i_need_your_help_on_langgraph/) , 2024-10-23-0912
```
Hey everyone, I have been developing an agent-based customer chatbot on LangGraph. And I need to add input and output gu
ardrail into the project. Actually I got the logic behind the LangGraph. But I wasn't be able to access the last message
s in the graph.

At this point I have two questions.

1-) How can I get the last message in the graph to check. 

2-) Ca
n I return a different message if the response contains toxic statements and how?

Here is my State and keys.

https://p
review.redd.it/6ibyh06u72wd1.png?width=551&format=png&auto=webp&s=a601230dd7ba963347b8bd6a363b454b45c68e7e


```
---

     
 
all -  [ I’m working on an AI project and i faced some issues ](https://www.reddit.com/r/generativeAI/comments/1g8j4hg/im_working_on_an_ai_project_and_i_faced_some/) , 2024-10-23-0912
```
I’m working on an AI project

Using mistral model since it is opensource
Thought to use langchain but it is not free

So
 came up with something called as OllamaLLM which is free of cost i hope everyone knows this.

But when i have large dat
a i am chunking the data and sending Many chunks in api calls it is taking hours

But when i use request.post as api cal
ls and sends thousands of chunks it takes like a minute or two to give the answer

Anyone can tell why and how can i sol
ve the problem 


Thanks in advacnce
```
---

     
 
all -  [ Open Source AI Chatbot UI template for Developers  ](https://www.reddit.com/r/developersIndia/comments/1g8fw4u/open_source_ai_chatbot_ui_template_for_developers/) , 2024-10-23-0912
```
Dear Developers,

I have created this repository to support your projects. This is not a product but a template that wil
l **ease your workflow**.

Here's the background:

While working on a Retrieval-Augmented Generation (RAG) project, I fo
und that no existing chat UI template offered all the features I needed. In response, I decided to build my own, incorpo
rating those missing functionalities.

Read more at Dev.to: [https://dev.to/ragharao314159/open-source-chatbot-ui-templa
te-for-developers-5apk](https://dev.to/ragharao314159/open-source-chatbot-ui-template-for-developers-5apk)

Chatbot UI: 
[https://convo-ui.vercel.app](https://convo-ui.vercel.app/)

Repository: [https://github.com/RaghaRao314159/Convo-UI](ht
tps://github.com/RaghaRao314159/Convo-UI)

**Key features included in both ConvoUI and TurboGPT:**

1. **Multiple Chats/
Conversations Support:** While Gradio is great, it only supports a single active conversation at a time. My template add
resses this by storing multiple chats locally (via localStorage) and linking them to authentication keys.
2. **Authentic
ation:** The template integrates authentication using OpenAI API keys for security and access control.
3. **Dark and Lig
ht Mode:** This feature can adapt to system settings or be manually toggled in the UI, providing flexibility in appearan
ce.

**New features that I added:**

1. **Markdown Table Parsing and Display:** Many existing chatbot UI templates strug
gle with cleanly rendering markdown tables, including TurboGPT. My version resolves this, ensuring tables display as nea
tly as they do in OpenAI's UI.
2. **Custom Backend Model Integration:** Most chatbot UIs lack the ability to interact wi
th custom backend models, as these typically require different object classes for communication compared to standard API
 calls. My template includes examples for calling backend models using Flask and Langserve. You can test this by selecti
ng a backend model. Click to visit the [Backend Repo](https://github.com/RaghaRao314159/Convo-UI_backend).
3. **Streamin
g Chatbot Outputs:** While streaming outputs is straightforward with foundation models, it becomes complex when dealing 
with backend servers. After extensive testing, I successfully implemented streaming capabilities for backend models in t
his template. Unfortunately, pythonanywhere voids this and my backend is currently on pythonanywhere. I will move it to 
another server in due time.



***I hope this template helps you accelerate the development of your full-stack applicati
ons. Do star this repo so more*** developers ***are aware of tools available to them.***  

----------------------------
-------------------------------------------------------------

**More resources on building chatbots**

I have thoroughl
y explored various approaches to building a fully custom Retrieval-Augmented Generation (RAG) LLM chatbot, and the resul
ts of my work can be found in my [RAG repository](https://github.com/RaghaRao314159/AuditBot_backend). Unlike many other
 online resources, this repository offers a complete full-stack solution for developing a RAG chatbot.

**For Frontend D
evelopers:**

I have included multiple UI options, from simple mockups to production-grade interfaces, along with the ne
cessary code to integrate the frontend with the backend. The chat interface is a React application, similar to this one,
 utilizing LangServe. You can find the frontend code in the [AuditBot repository](https://github.com/RaghaRao314159/Audi
tBot_frontend).

**For Machine Learning Engineers:**

I have conducted extensive experiments to improve the RAG framewor
k, covering techniques such as HyDE, recursive retrieval, and others. Additionally, the repository provides implementati
ons of frameworks like Langchain and LlamaIndex. It also includes setups for data stores, examples of prompt engineering
 with GuardRails, and much more.  
  
----------------------------------------------------------------------------------
-------  
  
**Feedback**

Do let me know if you would like to see other additional features would be useful in a chatbo
t UI.  Reach out if you would like to collaborate
```
---

     
 
all -  [ Whats the best approach to build LLM apps? Pros and cons of each ](https://www.reddit.com/r/LLMDevs/comments/1g8fnkd/whats_the_best_approach_to_build_llm_apps_pros/) , 2024-10-23-0912
```
With so many tools available for building LLM apps (apps built on top of LLMs), what's the best approach to quickly go f
rom 0 to 1 while maintaining a production-ready app that allows for iteration?

Here are some options:

1. Direct API Th
in Wrapper / Custom GPT/OpenAI API: Build directly on top of [OpenAI’s API](https://openai.com/product) for more control
 over your app’s functionality.
2. Frameworks like [LangChain](https://www.langchain.com/) / [LlamaIndex](https://llamai
ndex.ai/): These libraries simplify the integration of LLMs into your apps, providing building blocks for more complex w
orkflows.
3. Managed Platforms like [Lamatic](https://lamatic.ai/) / [Dify](https://dify.ai/) / [Flowise](https://flowis
e.io/): If you prefer more out-of-the-box solutions that offer streamlined development and deployment.
4. Editor-like To
ols such as [Wordware](https://wordware.ai/) / [Writer](https://writer.com/) / [Athina](https://athina.ai/): Perfect for
 content-focused workflows or enhancing writing efficiency.
5. No-Code Tools like [Respell](https://respell.ai/) / [n8n]
(https://n8n.io/) / [Zapier](https://zapier.com/): Ideal for building automation and connecting LLMs without needing ext
ensive coding skills.

*(Disclaimer: I am a founder of [Lamatic](https://lamatic.ai/), understanding the space and what 
tools people prefer)*
```
---

     
 
all -  [ Setting up  OPENAI account to practice Langxhain ](https://www.reddit.com/r/LangChain/comments/1g8fj8r/setting_up_openai_account_to_practice_langxhain/) , 2024-10-23-0912
```
I am looking to start practicing langchain using OpenAI but would like to hear from you “how much” should I buy and idoe
s OPENAI still offer free credits for new accounts ?  
```
---

     
 
all -  [ Why doesn't OpenAI use any chatbots on its site? ](https://www.reddit.com/r/ChatGPT/comments/1g8cd7u/why_doesnt_openai_use_any_chatbots_on_its_site/) , 2024-10-23-0912
```
It always seems odd to me that OpenAI doesn't use any chatbots on its site.  Do they not believe in their own product?


Especially for API users, a good chatbot with access to the docs is actually kind of useful.  Langchain does it with [ht
tps://chat.langchain.com/](https://chat.langchain.com/) and, while it's not perfect, I respect them for putting their mo
ney where their mouth is.  Why not OpenAI?
```
---

     
 
all -  [ Need help in deploying a RAG model as Sage Maker Model ](https://www.reddit.com/r/aws/comments/1g83g12/need_help_in_deploying_a_rag_model_as_sage_maker/) , 2024-10-23-0912
```
    Failed Reason:  The primary container for production variant AllTraffic did not pass the ping health check.
    
   
 I am making a model.tar.gz of this python script file, but when i try to deploy it in cloudformation yaml, the cloudwat
ch logs just show that the libraries just keep on installing and importing no function, the endpoint is not being create
d.
    
    below is my python file
    
    import os
    import boto3
    import faiss
    import json
    from transf
ormers import pipeline, AutoTokenizer
    from langchain_community.vectorstores import FAISS
    from langchain_communit
y.embeddings import HuggingFaceEmbeddings
    from langchain.chains import RetrievalQA
    from langchain.llms import Hu
ggingFacePipeline
    from langchain.text_splitter import CharacterTextSplitter
    from langchain.schema import Documen
t
    import logging
    
    # Setting up logging
    logging.basicConfig(level=logging.INFO)
    
    
    s3 = boto3.
client('s3')
    HUGGINGFACE_TOKEN = os.getenv('HUGGINGFACE_TOKEN','my-token')
    S3_BUCKET = os.getenv('S3_BUCKET', 'b
ucket-name')
    prefix = 'documents'
    
    model = None
    
    # Loading documents from S3 bucket
    def load_doc
uments_from_s3():
        logging.info('Loading documents from S3...')
        documents = []
        response = s3.list
_objects_v2(Bucket=S3_BUCKET, Prefix=prefix)
        for obj in response.get('Contents', []):
            s3_key = obj['
Key']
            if s3_key.endswith('.txt'):
                file_obj = s3.get_object(Bucket=S3_BUCKET, Key=s3_key)
   
             file_content = file_obj['Body'].read().decode('utf-8')
                documents.append(Document(page_conte
nt=file_content, metadata={'source': s3_key}))
        logging.info(f'Loaded {len(documents)} documents.')
        retur
n documents
    
    
    # Building FAISS index from documents
    def build_faiss_index(embeddings):
        documents
 = load_documents_from_s3()
        text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
        docu
ments = text_splitter.split_documents(documents)
        vector_store = FAISS.from_documents(documents, embeddings)
    
    logging.info('FAISS index built successfully.')
        return vector_store
    
    
    # Initializing the model
 
   def initialize_rag_model():
        
        #Initialize HuggingFace embeddings
        embeddings = HuggingFaceEmbed
dings(model_name='sentence-transformers/all-MiniLM-L6-v2')
    
        vector_store = build_faiss_index(embeddings)
   
     retriever = vector_store.as_retriever(search_kwargs={'k': 1})
    
        tokenizer = AutoTokenizer.from_pretraine
d('google/flan-t5-small',           use_auth_token=HUGGINGFACE_TOKEN)
        generation_pipeline = pipeline(
          
  'text2text-generation',
            model='google/flan-t5-small',
            tokenizer=tokenizer,
            max_new
_tokens=200,
            temperature=0.7,
            top_k=50,
            do_sample=True,
            truncation=True,

            pad_token_id=tokenizer.pad_token_id
        )
        llm = HuggingFacePipeline(pipeline=generation_pipelin
e)
    
        #Set up the RetrievalQA chain
        qa_chain = RetrievalQA.from_chain_type(
            llm=llm, chain
_type='refine', retriever=retriever, return_source_documents=True
        )
    
        logging.info('RAG model initial
ized.')
        return qa_chain
    
    # Query handling function
    def handle_query(query):
        global model
   
     model = initialize_rag_model()
        response = model(query)
        return response
    
    def input_fn(input_
data, content_type):
        if content_type == 'application/json':
            request = json.loads(input_data)
       
     return request['query']
        else:
            raise ValueError(f'Unsupported content type: {content_type}')
   
 
    
    def predict_fn(query, model):
        logging.info(f'Handling query: {query}')
        response = model(query
)
        return response
    
    
    def output_fn(prediction, content_type):
        if content_type == 'application
/json':
            
            result = {
                'query': prediction['query'],
                'result': pred
iction['result'],
                'source_documents': [
                    {'source': doc.metadata['source'], 'content'
: doc.page_content}
                    for doc in prediction['source_documents']
                ]
            }
      
      return json.dumps(result)
        else:
            raise ValueError(f'Unsupported content type: {content_type}')

    
    # Initialization method
    def model_fn(model_dir):
        global model
        # Initialize the model (only 
once when the endpoint starts)
        if model is None:
            model = initialize_rag_model()
        return model

```
---

     
 
all -  [ CV pour reconversion en IA  ](https://i.redd.it/7a0g4sxt2xvd1.jpeg) , 2024-10-23-0912
```
Hello les amis !
Vous pensez quoi de mon CV
J’arrive pas à être contacté par les recruteurs
Je me dis peut être c’est le
 CV qui bloque (si c’est ps le manque d’expérience)
Merci infiniment pour vos remarques et votre aide !  
```
---

     
 
all -  [ Neo4j retriever result filter (hybrid search)  ](https://www.reddit.com/r/Langchaindev/comments/1g7tcl3/neo4j_retriever_result_filter_hybrid_search/) , 2024-10-23-0912
```
I implemented this approach ( https://neo4j.com/developer-blog/rag-graph-retrieval-query-langchain/ ) and have been havi
ng good results using the hybrid search type.

I’m wanting to apply result filtering for the retriever using value/s pas
sed in when the chain is invoked. But, without rebuilding the chain as this is currently taking 4seconds which isn’t fea
sible. 

Has anyone managed/ know how to use a placeholder approach (similar to langchains prompts ) which allows a valu
e to be passed into the retrieval query without rebuilding the chain? 

Open to any other filtering methods people have 
used!

NOTE: using the hybrid search type restricted the filter approach in as_retriever() method, but the hybrid perfor
ms much better so keen to maintain that. 

Thank you!
```
---

     
 
all -  [ Neo4j retriever result filter (hybrid search)  ](https://www.reddit.com/r/Neo4j/comments/1g7t7xy/neo4j_retriever_result_filter_hybrid_search/) , 2024-10-23-0912
```

I implemented this approach ( https://neo4j.com/developer-blog/rag-graph-retrieval-query-langchain/ ) and have been hav
ing good results using the hybrid search type.

I’m wanting to apply result filtering for the retriever using value/s pa
ssed in when the chain is invoked. But, without rebuilding the chain as this is currently taking 4seconds which isn’t fe
asible. 

Has anyone managed/ know how to use a placeholder approach (similar to langchains prompts ) which allows a val
ue to be passed into the retrieval query without rebuilding the chain? 

Open to any other filtering methods people have
 used!

NOTE: using the hybrid search type restricted the filter approach in as_retriever() method, but the hybrid perfo
rms much better so keen to maintain that. 

Thank you!
```
---

     
 
all -  [ What is your biggest gripe with LangChain and/or LangGraph today? ](https://www.reddit.com/r/LangChain/comments/1g7sii6/what_is_your_biggest_gripe_with_langchain_andor/) , 2024-10-23-0912
```
Hey y'all, just comparing frameworks and I want to hear some negatives/gripes/reasons not to use LangChain or LangGraph
```
---

     
 
all -  [ Capstone Project Journal Article Guidance: Questions and Clarifications ](https://www.reddit.com/r/LangChain/comments/1g7qf65/capstone_project_journal_article_guidance/) , 2024-10-23-0912
```
I am working on my capstone project, where I developed a contract summarizer and a QA bot using the Llama 3 model and a 
Retrieval-Augmented Generation (RAG) system. My dataset consists of contracts from 12 categories (e.g., shipping agreeme
nts, IP agreements), each with 5 PDFs. I need guidance on the following aspects of my journal article:

1. **Method Sele
ction**: Should I continue using the RAG approach, or are there alternative methods I should explore?
2. **Comparative A
nalysis**: To enhance the content of my paper, should I include a comparison of different methods, models, or approaches
? If so, what could I compare?
3. **Evaluation Without Ground Truth**: Since I don't have ground truth data, how can I e
ffectively evaluate my system? Should I use RAG-as-a-Service (RAGas) to generate a test set, or should I employ large la
nguage models (LLMs) as judges?
4. **Enhancing the Journal Article**: What additional components or methods can I incorp
orate to strengthen my paper and make it more comprehensive?
5. **Dataset and Ground Truth Suggestions**: Can you recomm
end other datasets that include ground truth for tasks like mine, or provide advice on how to generate ground truth data
 for evaluation?
```
---

     
 
all -  [ Why is my hugging face llama 3.2-1B just giving me repetitive question when used in RAG? ](https://www.reddit.com/r/LLMDevs/comments/1g7misi/why_is_my_hugging_face_llama_321b_just_giving_me/) , 2024-10-23-0912
```
I just want to know if my approach is correct. I have done enough research but my model keeps giving me whatever questio
n i have asked as answer. Here are the steps i followed:

1. Load the pdf document into langchain.
PDF is in format - q:
 and a:

2. Use 'sentence-transformer/all-MiniLM-L6-v2'  for embedding and chroma as vector store

3. Use 'meta-llama/Ll
ama-3.2-1B' from huggingface.

4. Generate a pipeline and a prompt like 'Answer only from document. If not just say i do
n't know. Don't answer outside of document knowledge'

5. Finally use langchain to get top documents, pass the question 
and top docs as context to my llm and get response.

As said, the response is either repetirive or same as my question. 
Where am i going wrong?


Note: I'm running all the above code in colab as my local machine is not so capable.

Thanks i
n advance.
```
---

     
 
all -  [ Why is my hugging face llama 3.2-1B just giving me repetitive question when used in RAG? ](https://www.reddit.com/r/Rag/comments/1g7mh38/why_is_my_hugging_face_llama_321b_just_giving_me/) , 2024-10-23-0912
```

I just want to know if my approach is correct. I have done enough research but my model keeps giving me whatever questi
on i have asked as answer. Here are the steps i followed:

1. Load the pdf document into langchain.
PDF is in format - q
: and a:

2. Use 'sentence-transformer/all-MiniLM-L6-v2'  for embedding and chroma as vector store

3. Use 'meta-llama/L
lama-3.2-1B' from huggingface.

4. Generate a pipeline and a prompt like 'Answer only from document. If not just say i d
on't know. Don't answer outside of document knowledge'

5. Finally use langchain to get top documents, pass the question
 and top docs as context to my llm and get response.

As said, the response is either repetirive or same as my question.
 Where am i going wrong?


Note: I'm running all the above code in colab as my local machine is not so capable.

Thanks 
in advance.
```
---

     
 
all -  [ Convo-UI: an all-in-one chatbot UI template ](https://www.reddit.com/r/software/comments/1g7m7fg/convoui_an_allinone_chatbot_ui_template/) , 2024-10-23-0912
```
Dear Developers,

I have created this repository to support your projects. This is not a product but a template that wil
l **ease your workflow**.

Here's the background:

While working on a Retrieval-Augmented Generation (RAG) project, I fo
und that no existing chat UI template offered all the features I needed. In response, I decided to build my own, incorpo
rating those missing functionalities.

Chatbot UI: [https://convo-ui.vercel.app](https://convo-ui.vercel.app)

Repositor
y: [https://github.com/RaghaRao314159/Convo-UI](https://github.com/RaghaRao314159/Convo-UI)

**Key features included in 
both ConvoUI and TurboGPT:**

1. **Multiple Chats/Conversations Support:** While Gradio is great, it only supports a sin
gle active conversation at a time. My template addresses this by storing multiple chats locally (via localStorage) and l
inking them to authentication keys.
2. **Authentication:** The template integrates authentication using OpenAI API keys 
for security and access control.
3. **Dark and Light Mode:** This feature can adapt to system settings or be manually to
ggled in the UI, providing flexibility in appearance.

**New features that I added:**

1. **Markdown Table Parsing and D
isplay:** Many existing chatbot UI templates struggle with cleanly rendering markdown tables, including TurboGPT. My ver
sion resolves this, ensuring tables display as neatly as they do in OpenAI's UI.
2. **Custom Backend Model Integration:*
* Most chatbot UIs lack the ability to interact with custom backend models, as these typically require different object 
classes for communication compared to standard API calls. My template includes examples for calling backend models using
 Flask and Langserve. You can test this by selecting a backend model. Click to visit the [Backend Repo](https://github.c
om/RaghaRao314159/Convo-UI_backend).
3. **Streaming Chatbot Outputs:** While streaming outputs is straightforward with f
oundation models, it becomes complex when dealing with backend servers. After extensive testing, I successfully implemen
ted streaming capabilities for backend models in this template. Unfortunately, pythonanywhere voids this and my backend 
is currently on pythonanywhere. I will move it to another server in due time.



***I hope this template helps you accel
erate the development of your full-stack applications.***

-------------------------------------------------------------
----------------------------

**More resources on building chatbots**

I have thoroughly explored various approaches to 
building a fully custom Retrieval-Augmented Generation (RAG) LLM chatbot, and the results of my work can be found in my 
[RAG repository](https://github.com/RaghaRao314159/AuditBot_backend). Unlike many other online resources, this repositor
y offers a complete full-stack solution for developing a RAG chatbot.

**For Frontend Developers:**

I have included mul
tiple UI options, from simple mockups to production-grade interfaces, along with the necessary code to integrate the fro
ntend with the backend. The chat interface is a React application, similar to this one, utilizing LangServe. You can fin
d the frontend code in the [AuditBot repository](https://github.com/RaghaRao314159/AuditBot_frontend).

**For Machine Le
arning Engineers:**

I have conducted extensive experiments to improve the RAG framework, covering techniques such as Hy
DE, recursive retrieval, and others. Additionally, the repository provides implementations of frameworks like Langchain 
and LlamaIndex. It also includes setups for data stores, examples of prompt engineering with GuardRails, and much more. 
 
  
-----------------------------------------------------------------------------------------  
  
**Feedback**

Do let
 me know if you would like to see other additional features would be useful in a chatbot UI. 
```
---

     
 
all -  [ Best way to get started in implementing a PoC for an AI agent with semantic understanding? ](https://www.reddit.com/r/LangChain/comments/1g7lk65/best_way_to_get_started_in_implementing_a_poc_for/) , 2024-10-23-0912
```
I have a background in time-series analysis and I work for a small company (read: startup) that works on GenAI. As part 
of that, my manager has asked me to produce ASAP a proof-of-concept implementation of an AI agent on large document reco
gnition ASAP - specifically, we have a meeting with a client wanting a PoC of an AI agent that you can ask questions to 
about a corpus of text that the client uploads.

Specifically, my manager has asked me to look into performing OCR on a 
large document (~200 pages) and uploading it into a Chroma vector store, and implementing a question-answer system with 
an AI agent that performs semantic understanding for the client to use. I'm going to be burning the midnight oil for the
 next few days so I'd like some advice on how to get started. Are there any tutorials or resources that I can deal with?


(Note: I posted this on the machine learning sub, but it looks like it got quietly removed the instant of posting...)
```
---

     
 
all -  [ Connecting to Llama 3.2 with Azure ML endpoint  ](https://www.reddit.com/r/LangChain/comments/1g7jo40/connecting_to_llama_32_with_azure_ml_endpoint/) , 2024-10-23-0912
```

Anyone know why am I getting the following error on this . The endpoint is dedicated and deployed via Azure AI studio 


ValueError: Error while formatting response payload for chat model of type  `AzureMLEndpointApiType.dedicated`. Are you
 using the right formatter for the deployed  model and endpoint type?

### Code 
‘’’
from langchain_community.chat_model
s.azureml_endpoint import (
    AzureMLEndpointApiType,
    CustomOpenAIChatContentFormatter,
    AzureMLChatOnlineEndpo
int
)
from langchain_core.messages import HumanMessage

chat = AzureMLChatOnlineEndpoint(
    endpoint_url='https://xxx.
xxxx.inference.ml.azure.com/score',
    endpoint_api_type=AzureMLEndpointApiType.dedicated,
    content_formatter=Custom
OpenAIChatContentFormatter(),
    endpoint_api_key=os.getenv('AZURE_LLAMA_3_2_API_KEY'),
    model_kwargs={'temperature'
: 0}
)

response = chat.invoke(
    [HumanMessage(content='Will the Collatz conjecture ever be solved?')]
)
print(respon
se)
‘’’


## Error trace 

‘’’

Error                                  Traceback (most recent call last)
File c:\POC\san
dbox\notebooks-for-testing\.venv\Lib\site-packages\langchain_community\chat_models\azureml_endpoint.py:140, in CustomOpe
nAIChatContentFormatter.format_response_payload(self, output, api_type)
    [139](file:///C:/POC/sandbox/notebooks-for-t
esting/.venv/Lib/site-packages/langchain_community/chat_models/azureml_endpoint.py:139) try:
--> [140](file:///C:/POC/sa
ndbox/notebooks-for-testing/.venv/Lib/site-packages/langchain_community/chat_models/azureml_endpoint.py:140)     choice 
= json.loads(output)['output']
    [141](file:///C:/POC/sandbox/notebooks-for-testing/.venv/Lib/site-packages/langchain_
community/chat_models/azureml_endpoint.py:141) except (KeyError, IndexError, TypeError) as e:

KeyError: 'output'

The a
bove exception was the direct cause of the following exception:

ValueError                                Traceback (mo
st recent call last)
Cell In[63], [line 16](vscode-notebook-cell:?execution_count=63&line=16)
      [6](vscode-notebook-
cell:?execution_count=63&line=6) from langchain_core.messages import HumanMessage
      [8](vscode-notebook-cell:?execut
ion_count=63&line=8) chat = AzureMLChatOnlineEndpoint(
      [9](vscode-notebook-cell:?execution_count=63&line=9)     en
dpoint_url='https://xxx.xxx.inference.ml.azure.com/score',
     [10](vscode-notebook-cell:?execution_count=63&line=10)  
   endpoint_api_type=AzureMLEndpointApiType.dedicated,
   (...)
     [13](vscode-notebook-cell:?execution_count=63&line=
13)     model_kwargs={'temperature': 0}
     [14](vscode-notebook-cell:?execution_count=63&line=14) )
---> [16](vscode-n
otebook-cell:?execution_count=63&line=16) response = chat.invoke(
     [17](vscode-notebook-cell:?execution_count=63&lin
e=17)     [HumanMessage(content='Will the Collatz conjecture ever be solved?')]
     [18](vscode-notebook-cell:?executio
n_count=63&line=18) )
     [19](vscode-notebook-cell:?execution_count=63&line=19) print(response)

File c:\POC\sandbox\n
otebooks-for-testing\.venv\Lib\site-packages\langchain_core\language_models\chat_models.py:284, in BaseChatModel.invoke(
self, input, config, stop, **kwargs)
    [273](file:///C:/POC/sandbox/notebooks-for-testing/.venv/Lib/site-packages/lang
chain_core/language_models/chat_models.py:273) def invoke(
    [274](file:///C:/POC/sandbox/notebooks-for-testing/.venv/
Lib/site-packages/langchain_core/language_models/chat_models.py:274)     self,
    [275](file:///C:/POC/sandbox/notebook
s-for-testing/.venv/Lib/site-packages/langchain_core/language_models/chat_models.py:275)     input: LanguageModelInput,

   (...)
    [279](file:///C:/POC/sandbox/notebooks-for-testing/.venv/Lib/site-packages/langchain_core/language_models/c
hat_models.py:279)     **kwargs: Any,
    [280](file:///C:/POC/sandbox/notebooks-for-testing/.venv/Lib/site-packages/lan
gchain_core/language_models/chat_models.py:280) ) -> BaseMessage:
    [281](file:///C:/POC/sandbox/notebooks-for-testing
/.venv/Lib/site-packages/langchain_core/language_models/chat_models.py:281)     config = ensure_config(config)
    [282]
(file:///C:/POC/sandbox/notebooks-for-testing/.venv/Lib/site-packages/langchain_core/language_models/chat_models.py:282)
     return cast(
    [283](file:///C:/POC/sandbox/notebooks-for-testing/.venv/Lib/site-packages/langchain_core/language
_models/chat_models.py:283)         ChatGeneration,
--> [284](file:///C:/POC/sandbox/notebooks-for-testing/.venv/Lib/sit
e-packages/langchain_core/language_models/chat_models.py:284)         self.generate_prompt(
    [285](file:///C:/POC/san
dbox/notebooks-for-testing/.venv/Lib/site-packages/langchain_core/language_models/chat_models.py:285)             [self.
_convert_input(input)],
    [286](file:///C:/POC/sandbox/notebooks-for-testing/.venv/Lib/site-packages/langchain_core/la
nguage_models/chat_models.py:286)             stop=stop,
    [287](file:///C:/POC/sandbox/notebooks-for-testing/.venv/Li
b/site-packages/langchain_core/language_models/chat_models.py:287)             callbacks=config.get('callbacks'),
    [2
88](file:///C:/POC/sandbox/notebooks-for-testing/.venv/Lib/site-packages/langchain_core/language_models/chat_models.py:2
88)             tags=config.get('tags'),
    [289](file:///C:/POC/sandbox/notebooks-for-testing/.venv/Lib/site-packages/
langchain_core/language_models/chat_models.py:289)             metadata=config.get('metadata'),
    [290](file:///C:/POC
/sandbox/notebooks-for-testing/.venv/Lib/site-packages/langchain_core/language_models/chat_models.py:290)             ru
n_name=config.get('run_name'),
    [291](file:///C:/POC/sandbox/notebooks-for-testing/.venv/Lib/site-packages/langchain_
core/language_models/chat_models.py:291)             run_id=config.pop('run_id', None),
    [292](file:///C:/POC/sandbox
/notebooks-for-testing/.venv/Lib/site-packages/langchain_core/language_models/chat_models.py:292)             **kwargs,

    [293](file:///C:/POC/sandbox/notebooks-for-testing/.venv/Lib/site-packages/langchain_core/language_models/chat_model
s.py:293)         ).generations[0][0],
    [294](file:///C:/POC/sandbox/notebooks-for-testing/.venv/Lib/site-packages/la
ngchain_core/language_models/chat_models.py:294)     ).message

File c:\POC\sandbox\notebooks-for-testing\.venv\Lib\site
-packages\langchain_core\language_models\chat_models.py:784, in BaseChatModel.generate_prompt(self, prompts, stop, callb
acks, **kwargs)
    [776](file:///C:/POC/sandbox/notebooks-for-testing/.venv/Lib/site-packages/langchain_core/language_m
odels/chat_models.py:776) def generate_prompt(
    [777](file:///C:/POC/sandbox/notebooks-for-testing/.venv/Lib/site-pac
kages/langchain_core/language_models/chat_models.py:777)     self,
    [778](file:///C:/POC/sandbox/notebooks-for-testin
g/.venv/Lib/site-packages/langchain_core/language_models/chat_models.py:778)     prompts: list[PromptValue],
   (...)
  
  [781](file:///C:/POC/sandbox/notebooks-for-testing/.venv/Lib/site-packages/langchain_core/language_models/chat_models.
py:781)     **kwargs: Any,
    [782](file:///C:/POC/sandbox/notebooks-for-testing/.venv/Lib/site-packages/langchain_core
/language_models/chat_models.py:782) ) -> LLMResult:
    [783](file:///C:/POC/sandbox/notebooks-for-testing/.venv/Lib/si
te-packages/langchain_core/language_models/chat_models.py:783)     prompt_messages = [p.to_messages() for p in prompts]

--> [784](file:///C:/POC/sandbox/notebooks-for-testing/.venv/Lib/site-packages/langchain_core/language_models/chat_model
s.py:784)     return self.generate(prompt_messages, stop=stop, callbacks=callbacks, **kwargs)

File c:\POC\sandbox\noteb
ooks-for-testing\.venv\Lib\site-packages\langchain_core\language_models\chat_models.py:641, in BaseChatModel.generate(se
lf, messages, stop, callbacks, tags, metadata, run_name, run_id, **kwargs)
    [639](file:///C:/POC/sandbox/notebooks-fo
r-testing/.venv/Lib/site-packages/langchain_core/language_models/chat_models.py:639)         if run_managers:
    [640](
file:///C:/POC/sandbox/notebooks-for-testing/.venv/Lib/site-packages/langchain_core/language_models/chat_models.py:640) 
            run_managers[i].on_llm_error(e, response=LLMResult(generations=[]))
--> [641](file:///C:/POC/sandbox/noteboo
ks-for-testing/.venv/Lib/site-packages/langchain_core/language_models/chat_models.py:641)         raise e
    [642](file
:///C:/POC/sandbox/notebooks-for-testing/.venv/Lib/site-packages/langchain_core/language_models/chat_models.py:642) flat
tened_outputs = [
    [643](file:///C:/POC/sandbox/notebooks-for-testing/.venv/Lib/site-packages/langchain_core/language
_models/chat_models.py:643)     LLMResult(generations=[res.generations], llm_output=res.llm_output)  # type: ignore[list
-item]
    [644](file:///C:/POC/sandbox/notebooks-for-testing/.venv/Lib/site-packages/langchain_core/language_models/cha
t_models.py:644)     for res in results
    [645](file:///C:/POC/sandbox/notebooks-for-testing/.venv/Lib/site-packages/l
angchain_core/language_models/chat_models.py:645) ]
    [646](file:///C:/POC/sandbox/notebooks-for-testing/.venv/Lib/sit
e-packages/langchain_core/language_models/chat_models.py:646) llm_output = self._combine_llm_outputs([res.llm_output for
 res in results])

File c:\POC\sandbox\notebooks-for-testing\.venv\Lib\site-packages\langchain_core\language_models\chat
_models.py:631, in BaseChatModel.generate(self, messages, stop, callbacks, tags, metadata, run_name, run_id, **kwargs)
 
   [628](file:///C:/POC/sandbox/notebooks-for-testing/.venv/Lib/site-packages/langchain_core/language_models/chat_models
.py:628) for i, m in enumerate(messages):
    [629](file:///C:/POC/sandbox/notebooks-for-testing/.venv/Lib/site-packages
/langchain_core/language_models/chat_models.py:629)     try:
    [630](file:///C:/POC/sandbox/notebooks-for-testing/.ven
v/Lib/site-packages/langchain_core/language_models/chat_models.py:630)         results.append(
--> [631](file:///C:/POC/
sandbox/notebooks-for-testing/.venv/Lib/site-packages/langchain_core/language_models/chat_models.py:631)             sel
f._generate_with_cache(
    [632](file:///C:/POC/sandbox/notebooks-for-testing/.venv/Lib/site-packages/langchain_core/la
nguage_models/chat_models.py:632)                 m,
    [633](file:///C:/POC/sandbox/notebooks-for-testing/.venv/Lib/si
te-packages/langchain_core/language_models/chat_models.py:633)                 stop=stop,
    [634](file:///C:/POC/sandb
ox/notebooks-for-testing/.venv/Lib/site-packages/langchain_core/language_models/chat_models.py:634)                 run_
manager=run_managers[i] if run_managers else None,
    [635](file:///C:/POC/sandbox/notebooks-for-testing/.venv/Lib/site
-packages/langchain_core/language_models/chat_models.py:635)                 **kwargs,
    [636](file:///C:/POC/sandbox/
notebooks-for-testing/.venv/Lib/site-packages/langchain_core/language_models/chat_models.py:636)             )
    [637]
(file:///C:/POC/sandbox/notebooks-for-testing/.venv/Lib/site-packages/langchain_core/language_models/chat_models.py:637)
         )
    [638](file:///C:/POC/sandbox/notebooks-for-testing/.venv/Lib/site-packages/langchain_core/language_models
/chat_models.py:638)     except BaseException as e:
    [639](file:///C:/POC/sandbox/notebooks-for-testing/.venv/Lib/sit
e-packages/langchain_core/language_models/chat_models.py:639)         if run_managers:

File c:\POC\sandbox\notebooks-fo
r-testing\.venv\Lib\site-packages\langchain_core\language_models\chat_models.py:853, in BaseChatModel._generate_with_cac
he(self, messages, stop, run_manager, **kwargs)
    [851](file:///C:/POC/sandbox/notebooks-for-testing/.venv/Lib/site-pa
ckages/langchain_core/language_models/chat_models.py:851) else:
    [852](file:///C:/POC/sandbox/notebooks-for-testing/.
venv/Lib/site-packages/langchain_core/language_models/chat_models.py:852)     if inspect.signature(self._generate).param
eters.get('run_manager'):
--> [853](file:///C:/POC/sandbox/notebooks-for-testing/.venv/Lib/site-packages/langchain_core/
language_models/chat_models.py:853)         result = self._generate(
    [854](file:///C:/POC/sandbox/notebooks-for-test
ing/.venv/Lib/site-packages/langchain_core/language_models/chat_models.py:854)             messages, stop=stop, run_mana
ger=run_manager, **kwargs
    [855](file:///C:/POC/sandbox/notebooks-for-testing/.venv/Lib/site-packages/langchain_core/
language_models/chat_models.py:855)         )
    [856](file:///C:/POC/sandbox/notebooks-for-testing/.venv/Lib/site-pack
ages/langchain_core/language_models/chat_models.py:856)     else:
    [857](file:///C:/POC/sandbox/notebooks-for-testing
/.venv/Lib/site-packages/langchain_core/language_models/chat_models.py:857)         result = self._generate(messages, st
op=stop, **kwargs)

File c:\POC\sandbox\notebooks-for-testing\.venv\Lib\site-packages\langchain_community\chat_models\az
ureml_endpoint.py:280, in AzureMLChatOnlineEndpoint._generate(self, messages, stop, run_manager, **kwargs)
    [274](fil
e:///C:/POC/sandbox/notebooks-for-testing/.venv/Lib/site-packages/langchain_community/chat_models/azureml_endpoint.py:27
4) request_payload = self.content_formatter.format_messages_request_payload(
    [275](file:///C:/POC/sandbox/notebooks-
for-testing/.venv/Lib/site-packages/langchain_community/chat_models/azureml_endpoint.py:275)     messages, _model_kwargs
, self.endpoint_api_type
    [276](file:///C:/POC/sandbox/notebooks-for-testing/.venv/Lib/site-packages/langchain_commun
ity/chat_models/azureml_endpoint.py:276) )
    [277](file:///C:/POC/sandbox/notebooks-for-testing/.venv/Lib/site-package
s/langchain_community/chat_models/azureml_endpoint.py:277) response_payload = self.http_client.call(
    [278](file:///C
:/POC/sandbox/notebooks-for-testing/.venv/Lib/site-packages/langchain_community/chat_models/azureml_endpoint.py:278)    
 body=request_payload, run_manager=run_manager
    [279](file:///C:/POC/sandbox/notebooks-for-testing/.venv/Lib/site-pac
kages/langchain_community/chat_models/azureml_endpoint.py:279) )
--> [280](file:///C:/POC/sandbox/notebooks-for-testing/
.venv/Lib/site-packages/langchain_community/chat_models/azureml_endpoint.py:280) generations = self.content_formatter.fo
rmat_response_payload(
    [281](file:///C:/POC/sandbox/notebooks-for-testing/.venv/Lib/site-packages/langchain_communit
y/chat_models/azureml_endpoint.py:281)     response_payload, self.endpoint_api_type
    [282](file:///C:/POC/sandbox/not
ebooks-for-testing/.venv/Lib/site-packages/langchain_community/chat_models/azureml_endpoint.py:282) )
    [283](file:///
C:/POC/sandbox/notebooks-for-testing/.venv/Lib/site-packages/langchain_community/chat_models/azureml_endpoint.py:283) re
turn ChatResult(generations=[generations])

File c:\POC\sandbox\notebooks-for-testing\.venv\Lib\site-packages\langchain_
community\chat_models\azureml_endpoint.py:142, in CustomOpenAIChatContentFormatter.format_response_payload(self, output,
 api_type)
    [140](file:///C:/POC/sandbox/notebooks-for-testing/.venv/Lib/site-packages/langchain_community/chat_model
s/azureml_endpoint.py:140)         choice = json.loads(output)['output']
    [141](file:///C:/POC/sandbox/notebooks-for-
testing/.venv/Lib/site-packages/langchain_community/chat_models/azureml_endpoint.py:141)     except (KeyError, IndexErro
r, TypeError) as e:
--> [142](file:///C:/POC/sandbox/notebooks-for-testing/.venv/Lib/site-packages/langchain_community/c
hat_models/azureml_endpoint.py:142)         raise ValueError(self.format_error_msg.format(api_type=api_type)) from e
   
 [143](file:///C:/POC/sandbox/notebooks-for-testing/.venv/Lib/site-packages/langchain_community/chat_models/azureml_endp
oint.py:143)     return ChatGeneration(
    [144](file:///C:/POC/sandbox/notebooks-for-testing/.venv/Lib/site-packages/l
angchain_community/chat_models/azureml_endpoint.py:144)         message=AIMessage(
    [145](file:///C:/POC/sandbox/note
books-for-testing/.venv/Lib/site-packages/langchain_community/chat_models/azureml_endpoint.py:145)             content=c
hoice.strip(),
    [146](file:///C:/POC/sandbox/notebooks-for-testing/.venv/Lib/site-packages/langchain_community/chat_m
odels/azureml_endpoint.py:146)         ),
    [147](file:///C:/POC/sandbox/notebooks-for-testing/.venv/Lib/site-packages
/langchain_community/chat_models/azureml_endpoint.py:147)         generation_info=None,
    [148](file:///C:/POC/sandbox
/notebooks-for-testing/.venv/Lib/site-packages/langchain_community/chat_models/azureml_endpoint.py:148)     )
    [149](
file:///C:/POC/sandbox/notebooks-for-testing/.venv/Lib/site-packages/langchain_community/chat_models/azureml_endpoint.py
:149) if api_type == AzureMLEndpointApiType.serverless:

ValueError: Error while formatting response payload for chat mo
del of type  `AzureMLEndpointApiType.dedicated`. Are you using the right formatter for the deployed  model and endpoint 
type?

‘’’


```
---

     
 
all -  [ What mistake am I making in this ChatPromptTemplate? ](https://www.reddit.com/r/LangChain/comments/1g7g4zd/what_mistake_am_i_making_in_this/) , 2024-10-23-0912
```
Hi all, here is my code:

    from langchain_ollama import ChatOllama
    from langchain_experimental.tools import Pytho
nAstREPLTool
    from langchain_core.prompts import ChatPromptTemplate
    from langchain.output_parsers.openai_tools im
port JsonOutputToolsParser
    
    import pandas as pd
    
    df = pd.read_csv('sample.csv', header=0)
    tool = Pyt
honAstREPLTool(locals={'df': df})
    
    model_name = 'llama3.1:latest'
    
    llm_o = ChatOllama(temperature=0.7, m
odel=model_name)
    llm_with_tools = llm_o.bind_tools([tool], tool_choice=tool.name)
    parser = JsonOutputToolsParser
()
    
    system = f'You have access to a pandas dataframe df, and here is a sample {df.head()}'
    
    prompt = Cha
tPromptTemplate.from_messages([('system', system), ('human', '{question}')])
    
    chain = prompt | llm_with_tools | 
parser | tool
    question = 'What's the correlation between A and B'
    chain.invoke({'question': question})

This is 
throwing up this error:

    ValidationError: 1 validation error for PythonInputs
      Input should be a valid dictiona
ry or instance of PythonInputs [type=model_type, input_value=[{'args': {'query': 'pd.m...pe': 'python_repl_ast'}], input
_type=list]
        For further information visit https://errors.pydantic.dev/2.8/v/model_type



Look at this Github is
sue page, [https://github.com/langchain-ai/langchain/issues/13681](https://github.com/langchain-ai/langchain/issues/1368
1) it seems I'm making error in my ChatPrompt. I'm not able to see what is the mistake. 

I'm adapting from this tutoria
l [https://python.langchain.com/docs/how\_to/sql\_csv/](https://python.langchain.com/docs/how_to/sql_csv/)

  
Any help 
is appreciated!


```
---

     
 
MachineLearning -  [ [D] How are folks building conversational Retrieval Augmented Generation apps ](https://www.reddit.com/r/MachineLearning/comments/1ftdby7/d_how_are_folks_building_conversational_retrieval/) , 2024-10-23-0912
```
I've read through various resources such as:  
- [https://vectorize.io/how-i-finally-got-agentic-rag-to-work-right/](htt
ps://vectorize.io/how-i-finally-got-agentic-rag-to-work-right/)  
- [https://python.langchain.com/docs/tutorials/qa\_cha
t\_history/](https://python.langchain.com/docs/tutorials/qa_chat_history/)  
- [https://langchain-ai.github.io/langgraph
/tutorials/rag/langgraph\_agentic\_rag/](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/) 
 
- [https://docs.llamaindex.ai/en/stable/module\_guides/deploying/chat\_engines/](https://docs.llamaindex.ai/en/stable/
module_guides/deploying/chat_engines/)  
- [https://huggingface.co/datasets/nvidia/ChatRAG-Bench](https://huggingface.co
/datasets/nvidia/ChatRAG-Bench) 

But these feel overly reductive, since they don't address complexities like:  
1) when
 to retrieve vs. just respond immediately to reduce latency  
2) rely on existing context previously retrieved in the co
nversation instead of retrieving again at the current turn  
3) partition LLM context between retrieved information and 
past conversation history.

I'm sure some teams already have good systems for this, would appreciate pointers!
```
---

     
 
MachineLearning -  [ Built a web agent which call fill Google forms based on the user details [P] ](https://www.reddit.com/r/MachineLearning/comments/1fozud5/built_a_web_agent_which_call_fill_google_forms/) , 2024-10-23-0912
```
GitHub repo : [https://github.com/shaRk-033/web-agent](https://github.com/shaRk-033/web-agent)

Tried to solve it using 
two approaches:

# 1: Basic Scraping and Filling

This is the straightforward approach. The agent scrapes the form’s HTM
L and uses fixed XPaths to find and fill in the required fields.

* It pulls the form’s HTML, locates the fields with se
t XPaths, and inputs the answers. It’s a direct and simple method.
* If the form changes or an element isn’t where it’s 
expected, the process can fail and may need manual adjustments.

[basic approach](https://preview.redd.it/5e8g4a1k4xqd1.
png?width=1055&format=png&auto=webp&s=d8e984e4feaee2f0453b08c8696768c40a2a5c20)

2. Using LangChain Agents and tool call
ing

* LangChain Agent**:** The agent handles everything by using the LLM’s reasoning to decide what to do next, includi
ng generating those tricky XPaths.
* Error Handling**:** If something goes wrong (like an element not found), the agent 
tries again with better XPaths until it gets the job done.

[using langchain agents](https://preview.redd.it/948i88pl4xq
d1.png?width=782&format=png&auto=webp&s=ed1e6c19efec9f4cbbbd6ab5a22558f221cf745f)

Any recommendations to improve this w
ould be welcome. Also, if anyone has ideas on building similar web agents to automate other tasks, it would be great to 
hear them. :)
```
---

     
