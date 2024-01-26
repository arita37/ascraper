 
all -  [ What is the best local LLM for agentic behavior? ](https://www.reddit.com/r/LangChain/comments/19fnp1g/what_is_the_best_local_llm_for_agentic_behavior/) , 2024-01-26-0910
```
I'm looking for the best LLM currently for agentic behavior in langchain. By best, I mean the most consistent with the l
east parsing errors.
```
---

     
 
all -  [ Anyway to compare a spec (word or excel) with its programming implementation for any gap/error ](https://www.reddit.com/r/LangChain/comments/19fma04/anyway_to_compare_a_spec_word_or_excel_with_its/) , 2024-01-26-0910
```
Let us say we have a simple spec like this below:

set my\_property to 1, when condition1 is met

set my\_property to 2,
 when condition2 is met

set my\_property to 3, when condition3 and condition33 are both met

set my\_property to 4, whe
n condition4 is met

Then this is python code below:

if condition1:

my\_property to 1

elif condition2:

my\_property 
to -2929 # people making error here

elif condition3 and condition33:

my\_property to 3

elif ...

This is an extremely
 simple example. I am wondering if langchain or other popular LLM library can somehow help us engineers achieve this to 
make our lives easier. I know langchain can somehow compare two similar (let us say earning report pdf) but not sure if 
it can help, even just a little bit, to spot any mistaken typo between spec and implementation?

&#x200B;
```
---

     
 
all -  [ Model concurrence ](https://www.reddit.com/r/LangChain/comments/19fkd55/model_concurrence/) , 2024-01-26-0910
```
I've been testing langserve with llama2, Mistral and falcon 7b. I'm struggling with concurrence problems when sending co
ncurrent request to langchain (only one request is processed, the other error 500, weird output for the only successful 
reques). I've tested those models concurrence outside langserve (with async calls) also failing. So, it's not a langserv
e problem, the models are not handling concurrence (even with things like vllm for model loading).

Somebody else has fa
ced a similar issue?
```
---

     
 
all -  [ LangChain is awesome, but have you tried Embedchain? ](https://www.reddit.com/r/LangChain/comments/19fhmbv/langchain_is_awesome_but_have_you_tried_embedchain/) , 2024-01-26-0910
```
Hi there! As you may know I often post here about my latest [LangChain tutorials and articles](https://www.gettingstarte
d.ai/tag/langchain). I was recently introduced to Embedchain, a Python library built on top of LangChain that takes care
 of your RAG needs in a few lines of Python code. It basically does all of the following for you right out-of-the-box:


* Sets up local Chroma DB
* Takes in data source (URL, YouTube, PDF, etc…)
* Makes chunks out of the data
* Converts the
 chunks to embeddings
* Stores the embeddings on the vector database
* Performs similarity search
* Query a large langua
ge model

Long story short, I took it for a spin and [wrote about it here](https://www.gettingstarted.ai/what-is-the-dif
ference-between-embedchain-and-langchain/) specifically, comparing it with LangChain.

If you‘re looking for a tool that
 lets you build a RAG app quickly, give it a try. You may find it suitable for your use case.

Let me know what you thin
k!
```
---

     
 
all -  [ How do I get ConversationalRetrievalChain to use a System Prompt? ](https://www.reddit.com/r/LangChain/comments/19fgxzb/how_do_i_get_conversationalretrievalchain_to_use/) , 2024-01-26-0910
```
System Prompt with ConversationalRetrievalChain: I am a newb playing with open-ai, chat-gpt, and langchain. Using open-a
i api's directly, I am able to set a system prompt to prepare the llm to respond to all all my interactions with the ini
tial system prompt instructions. Now I am using langchain's ConversationalRetrievalChain to try to interact with custom 
content. I have it working, but I would like to give the underlying llm (gpt-4) a system prompt as I do using the open-a
i api's directly. How can I do this? e.g. 'You are a helpful sale agent named Joe that works for ACME CO. Try to respond
 with links to products sold by ACME CO'
```
---

     
 
all -  [ RAG'd Repo and multi-agent chatbot for advanced codebase support? ](https://www.reddit.com/r/LangChain/comments/19fgnin/ragd_repo_and_multiagent_chatbot_for_advanced/) , 2024-01-26-0910
```
Hello,

I'm working on a project like this for another dataset, but I don't see why I can't apply it to my own repo. I l
ove using GPT for coding productivity, but one of the limitations is in api-type environments with multiple files and de
pendencies flying around - it's difficult to share all the relevant information to your agent or chatbot. 

Is there any
thing like this currently available? This isn't exactly rocket scient to start. If not, I'll start working on it
```
---

     
 
all -  [ Apply for almost 200+ application for Data scientist ](https://i.redd.it/tfajfzwyrmec1.jpeg) , 2024-01-26-0910
```
I don't what wrong in my resume. I am currently working as data scientist but i need to switch my job, but getting rejec
ted from everywhere i don't why,it would be very grateful if you guys help to get a job by reviewing my resume
```
---

     
 
all -  [ Choosing Between Langchain SQL and GPT-4 SQL Function ](https://www.reddit.com/r/LangChain/comments/19ffzyk/choosing_between_langchain_sql_and_gpt4_sql/) , 2024-01-26-0910
```
I'm working on a project that involves querying a database using natural language, and I'm trying to decide between usin
g Langchain SQL and the GPT-4 SQL function. From my understanding, Langchain SQL specializes in converting natural langu
age into SQL queries, which seems ideal for direct database interaction. On the other hand, gpt4 can also generate sqls 
directly with function calling. So it seems there is no need to use Langchain anymore.

I'd appreciate insights or exper
iences from anyone who has used either Langchain SQL or GPT-4 for similar purposes.
```
---

     
 
all -  [ Here is another FREE AI Webinar: 'LangChain for Multimodal Apps: Chat With Text/Image Data'. ](https://pxl.to/lp87a3r) , 2024-01-26-0910
```

```
---

     
 
all -  [ Python OpenAI Langchain AWS Lambda Layer on M1 Mac setup ](https://www.reddit.com/r/aws/comments/19fbpk8/python_openai_langchain_aws_lambda_layer_on_m1/) , 2024-01-26-0910
```
For any heads out there that are delving into a Python OpenAI with Langchain Lambda function in an AWS env using an M1 M
ac, hope this is useful.

# Problem

When pip installing libraries on an M1 Mac, the architecture used does not register
 correctly when uploading to AWS lambda layer. This will result in the python lambda function code not being able to fin
d libraries when running.

# Steps

1. Install your libraries locally

&#8203;

    pip3 install openai langchain -t pyt
hon

2. Overwrite the problematic libraries manually (this may be different depending on what stuff you install)

    pi
p3 install --upgrade --platform manylinux_2_17_aarch64 --only-binary=:all: pydantic-core==2.14.1 -t python
    pip3 inst
all --upgrade --platform manylinux_2_17_aarch64 --only-binary=:all: pydantic==2.5.0 -t python
    pip3 install --upgrade
 --platform manylinux_2_17_aarch64 --only-binary=:all: numpy==1.26.2 -t python

3. Zip and upload your lambda layer (I u
se the cli in the example)

    zip -rq python_layer.zip python
    aws lambda publish-layer-version
    --layer-name {L
AYER_NAME}
    --zip-file filbeb://python_layer.zip
    --region {REGION}

4. Change your lambda function 'Runtime Setti
ngs' Architecture to **arm64** and point to your layer. This also was needed for the function to find the libraries in t
he layer.

Note: Not sure if this is necessary, but I think there are some incompatibilities with certain versions of la
ngchain with versions openai. The versions I got working together are as follows:

    langchain==0.0.348
    langsmith=
=0.0.69
    langchain-core==0.0.12
    openai==1.3.7

&#x200B;
```
---

     
 
all -  [ Advance Scrapping with LLM ](https://www.reddit.com/r/LangChain/comments/19fadp1/advance_scrapping_with_llm/) , 2024-01-26-0910
```
I am working on a project where I want to use LLMs (GPT4) to summarize the data from a website. First, I want to scrap a
ll the data from the all the links available in that website and then I want to use GPT4 to summarize the data. I can ge
t the summarization part done easily but how can I build a scrapper which can scrap the data from a website. For example
;

&#x200B;

If the website is a restaurant website then I would want to go over all the links in that site. It will be 
an iterative process and somehow I need to keep the already visited/scrapped links so that I shouldn't scrap it again. 


&#x200B;

Is there any framework or already built library/API available for this purpose?
```
---

     
 
all -  [ [Langchain] Les nouvelles mises à jour de Chatgpt remplaceront-elles le chiffon? ](https://www.reddit.com/r/redditenfrancais/comments/19f81my/langchain_les_nouvelles_mises_à_jour_de_chatgpt/) , 2024-01-26-0910
```
J'ai travaillé sur un projet faisant l'extraction et le résumé des grands PDF à l'aide de Langchain. J'ai regardé l'Open
ai Dev Talk et je me demande si la récupération basée sur le cloud qui a été discutée remplacera probablement le chiffon
? Il semble que ce sera le cas, mais en même temps, l'utilisateur final devra probablement avoir GPT Plus pour accéder a
u modèle ou au bot créé avec le DOC.

Je sais qu'il est trop tôt pour le dire, mais j'espère avoir des informations avan
t d'aller trop loin avec mon projet, seulement pour réaliser qu'il sera remplacé par des fonctionnalités standard.

Pens
ées?

Traduit et reposté à partir de la publication 17pzvrw de la communauté langchain. Pour retrouver la publication or
iginale, insérez l'id de la publication après 'reddit.com/'
```
---

     
 
all -  [ Advanced Rags in Langchain ](https://www.reddit.com/r/LangChain/comments/19f5sqj/advanced_rags_in_langchain/) , 2024-01-26-0910
```
Recently I've been working on rags using langachain.
I also started a course on RAGs in deeplearning.ai, where they disc
ussed advanced rag techniques, like sentence window retrieval and automerging retrieval
But the course is mainly in llam
a index
I'm wondering if I can do some advanced retrieval in Langchain without api key
```
---

     
 
all -  [ Text splitter for JSX/React code to keep informational context? ](https://www.reddit.com/r/LangChain/comments/19f4ub6/text_splitter_for_jsxreact_code_to_keep/) , 2024-01-26-0910
```
What's the best Langchain.js text splitter to handle a JSX string like the following and maintain context of the text co
ntent?

The information we mostly care about is the user-readable text. However, JSX tags sometimes also contain relevan
t information (like the `alt` prop of the `Image`) so I don't want to just remove them. However, I'm removing all `class
Name` props from the string (via regex) to make the text less verbose.

```
export const metadata: Metadata = {
  title:
 'Home Page',
};

export default function Home() {
  return (
    <div>
      <div>
        <div>
          <h1>
       
     Hi, I'm Florian 👋
          </h1>
          <p>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit
, sed do eiusmod
            tempor incididunt ut labore et dolore magna aliqua.
          </p>
        </div>
        <
Image
          src={me}
          alt='A photo of me'
          height={350}
        />
      </div>
      <p>
        
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
        tempor incididunt ut labore et dolore ma
gna aliqua. Ut enim ad minim
        veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea
        com
modo consequat. Duis aute irure dolor in reprehenderit in voluptate
        velit esse cillum dolore eu fugiat nulla par
iatur.
      </p>
    </div>
  );
}
```
```
---

     
 
all -  [ Seeking Assistance with TextSplitter: Adding Bounding Box or Coordinate Values to PDF Chunks ](https://www.reddit.com/r/LangChain/comments/19f101u/seeking_assistance_with_textsplitter_adding/) , 2024-01-26-0910
```
 Hello everyone,

I'm wondering if anyone has successfully added bounding box or coordinate values to each chunk of a PD
F using CharacterTextSplitter or Recursive methods. I'm specifically interested in extracting the coordinates and storin
g them in metadata within a vector store.

My ultimate goal is to be able to query similar chunks and precisely highligh
t the corresponding text in the PDF from which it was extracted.

If there's already a solution or tool available for th
is purpose, could you kindly direct me to the right resources or provide some guidance?

Thank you in advance!
```
---

     
 
all -  [ Can i connect fine tune “FLAN T5 base” to langchain agent ](https://www.reddit.com/r/LLMDevs/comments/19f0azv/can_i_connect_fine_tune_flan_t5_base_to_langchain/) , 2024-01-26-0910
```
So i have fine tuned flan t5, on my custom dataset, and now is there anyway around where i can use langchain agents with
 my model. To analyse my database “mongodb”

I have tried OpenAi, with langchain, and there I tried Pandas Dataframe age
nt, who can interact with the dataframe  and give the answers regarding the dataframe i want to build similar but with f
lat t5. Or any other FREE model if available.
```
---

     
 
all -  [ Need advice for developing LLM Chatbot to recommend items from a store catalog ](https://www.reddit.com/r/ArtificialInteligence/comments/19excyh/need_advice_for_developing_llm_chatbot_to/) , 2024-01-26-0910
```
Specifically, I'm trying to get a chatbot to recommend users items from a specific store catalog, with about 2000-5000 d
ifferent items; mostly grocery, produce, snacks, etc. My approach right now is to cut it up into two AIs, one which face
s the user as a chatbot and recommends them products, and the other which extracts actual product IDs/SKUs from the firs
t AI's outputs (from there, Flutter app components are generated and presented to the user.) There are two things I'm in
terested in:

\- Would Langchain be a good tool to work with these AIs?

\- Is there any part where I may have to fine-t
une the first AI, or can I change its behavior purely in-context?

\- Can tools like LlamaIndex be used to facilitate th
e second AI?

I'm not an experienced LLM practitioner by any means; I've used Tensorflow for computer vision homework an
d ChatGPT for advice at the most, but I've taken a deep learning class so I understand the general concepts. Any help/ad
vice would be greatly appreciated!

(Follow-up, soon each food item will also have nutritional facts attached to it, whi
ch are vectorizable JSONs of mostly numbers and boolean flags. I'm not counting on the AI to learn about the user's heal
th needs or preferences, the user will input that themselves. Similar to the 2nd and 3rd points above, what is the best 
way to incorporate this data, in-context or fine-tuning, into the recommendation AI?
```
---

     
 
all -  [ What’s the best LangChain (JS) tutorial on YouTube ](https://www.reddit.com/r/LangChain/comments/19ewodj/whats_the_best_langchain_js_tutorial_on_youtube/) , 2024-01-26-0910
```
Can y’all recommend a good tutorial that will get me from start to finish for a RAG app I’m trying to make using LangCha
in JS?

I don’t wanna become a guru, just trying to get something on production asap. It needs to have memory.

Much app
reciated 🙏🏻
```
---

     
 
all -  [ agent platform for multi-modal agent capabilities ](https://www.reddit.com/r/LangChain/comments/19eqmgk/agent_platform_for_multimodal_agent_capabilities/) , 2024-01-26-0910
```
I'm developing an application using a large language model (LLM) and am in need of a robust core agent platform that sup
ports multi-modal agent capabilities. Currently, I'm utilizing LLM for intent recognition and named entity recognition, 
and then I do backend workflow orchestration without LLM or Agents. My goal is to transition to an agent framework for e
nhanced flexibility. I'm looking for frameworks that are resilient against prompt injection and easier to with open-sour
ce LLMs. 

So far, I've considered:

1. LangChain Agents (I have experience with it)
2. LLaMaIndex Agents
3. HayStack Ag
ents
4. AutoGen

Do you:

1. Recommend any additional frameworks that are worth exploring for agent orchestration? 
2. H
ave a preferred framework in this context?
3. have experience with these framework and want to share feedback?

&#x200B;

```
---

     
 
all -  [ agent platform for multi-modal agent capabilities ](https://www.reddit.com/r/LLMDevs/comments/19eqjcu/agent_platform_for_multimodal_agent_capabilities/) , 2024-01-26-0910
```
 

I'm developing an application using a large language model (LLM) and am in need of a robust core agent platform that 
supports multi-modal agent capabilities. Currently, I'm utilizing LLM for intent recognition and named entity recognitio
n, and then I do backend workflow orchestration without LLM or agents. My goal is to transition to an agent framework fo
r enhanced flexibility. I'm looking for frameworks that are resilient against prompt injection and easier to with open-s
ource LLMs. 

So far, I've considered:

1. LangChain Agents (I have experience with it)
2. LLaMaIndex Agents
3. HayStack
 Agents
4. AutoGen

Do you:

1. Recommend any additional frameworks that are worth exploring for agent orchestration? 
2
. Have a preferred framework in this context?
3. have experience with these framework and want to share feedback?

&#x20
0B;
```
---

     
 
all -  [ Streaming local LLM with FastAPI, Llama.cpp and Langchain ](https://www.reddit.com/r/LangChain/comments/19enjxr/streaming_local_llm_with_fastapi_llamacpp_and/) , 2024-01-26-0910
```
Hi, 

I have setup FastAPI with Llama.cpp and Langchain. Now I want to enable streaming in the FastAPI responses. Stream
ing works with Llama.cpp in my terminal, but I wasn't able to implement it with a FastAPI response. See this Stackoverfl
ow-Question (for code etc.): [https://stackoverflow.com/questions/77867894/streaming-local-llm-with-fastapi-llama-cpp-an
d-langchain?noredirect=1#comment137276485\_77867894](https://stackoverflow.com/questions/77867894/streaming-local-llm-wi
th-fastapi-llama-cpp-and-langchain?noredirect=1#comment137276485_77867894)

Most tutorials focused on enabling streaming
 with an OpenAI model, but I am using a local LLM (quantized Mistral) with llama.cpp. I think I have to modify the Callb
ackhandler, but no tutorial worked.

&#x200B;

Does anyone know how I can make Streaming working? I have a project deadl
ine on Friday and unitl then I have to make it work...
```
---

     
 
all -  [ Are there any models recommended for legal writing? ](https://www.reddit.com/r/LocalLLaMA/comments/19elj8h/are_there_any_models_recommended_for_legal_writing/) , 2024-01-26-0910
```
Hello friends, I know this post isn't as exciting as discussing the best porn model every week but I'd like recommendati
ons for a model tuned for legal writing or that has been trained on case law, legal briefs, that sort of thing. It shoul
d be more litigation focused, rather than transactional. Context size and comprehension are key. 

If there isn't anythi
ng that fits the bill, does anyone have a decent base model to recommend and maybe some comments or recommendations on h
ow to train a model? That's an area I haven't explored yet. My skill level is a beginner, so I've used Fiverr when I'm o
ut of my depth but I usually like to know enough to understand what I need and to clearly convey that to whoever I hire.
 I'm hoping you guys will help me get there. Estimates on time, manpower, processing power, and materials required would
 all be helpful to give me an idea of how far down the rabbit hole a project like this might send me.

By way of backgro
und, I'm an attorney that's been using ChatGPT since the beginning and I've since branched out to messing with vector da
tabases, Langchain, and hosting models locally. I have a 3090 but am open to renting better processing power if a model 
could give ChatGPT a run for its money. My use of ChatGPT can be fairly limited due to privacy concerns, attorney-client
 and work product privilege. The increase in context size has been great, but as has been discussed to death, ChatGPT's 
quality has gone down. It's legal writing is very poor, wordy, and unapproachable so while it occasionally strikes gold,
 it takes a lot of mining to get there.

Edit: Since this has been mentioned a few times already, the LLM is not perform
ing legal research. I am aware of the hallucination problem and understand those limitations. I mention being trained on
 case law more for the value in writing style and legal reasoning rather than substantive legal knowledge.
```
---

     
 
all -  [ Loader for website pages (offline) (Next.js/React) ](https://www.reddit.com/r/LangChain/comments/19elb7z/loader_for_website_pages_offline_nextjsreact/) , 2024-01-26-0910
```
I am building a website with an integrated chatbot. How would you load the page info into documents? I want to make my c
ode reusable for future projects.

Right now I'm using the [GitHubRepoLoader](https://js.langchain.com/docs/integrations
/document_loaders/web_loaders/github) to turn the pages into documents, but this requires the code to be available in a 
GitHub repository. This is not great for local development (because we don't have the latest data).

Would you load the 
pages from the file system instead? Or is there a better solution?

Any classes/helpers you can point me to? I'm using L
angchain.js.
```
---

     
 
all -  [ My 2 cents for New Developers. ](https://www.reddit.com/r/developersIndia/comments/19ej7i8/my_2_cents_for_new_developers/) , 2024-01-26-0910
```
From my 8 years of experience i have learnt that in India, there are lot more job opening in Java as compared to lets sa
y python or javascript. I have always struggled to get my resume shortlisted since i never worked in Java. (But fortunat
ely may cards played out well) I am writing this out since market has started opening and a lot of jobs have started pop
ping requiring Java Developers.

So, If you are starting up as a software Engineer. Don't rely on fancy stuff like 'Writ
ing LLM pipelines using python langchain' or writing backend services in GoLang. Stick to the basics and **develop web a
pps in Java Spring or JSF**. Don't go with MongoDB or any NoSQL databases, **stick to SQL**.   


Also, I see a lot of p
eople **not** open to work on 'X' technology. Always be language agnostic. Even if you don't have experience. Its always
 good to say: 'I have my basics tightened up, I will be able to pick up 'X' technology quickly'.   


All the best guys!
  

```
---

     
 
all -  [ Ever wondered how to build a chatbot? ](https://www.reddit.com/r/SideProject/comments/19ej4sc/ever_wondered_how_to_build_a_chatbot/) , 2024-01-26-0910
```
Here's a free code-along that'll get you to grips with RAG, the OpenAI API and Pinecone!

Building Chatbots with OpenAI 
API and Pinecone - Start from basics to build on skills with GPT, Pinecone and LangChain to create a chatbot that answer
s questions about research papers. Code Along on DataCamp Workspace: [https://www.datacamp.com/code-along/building-chatb
ots-openai-api-pinecone](https://www.datacamp.com/code-along/building-chatbots-openai-api-pinecone)

This is just one se
ssion in a 9-part free (yep, free!) series that will get you on the path to becoming an AI Developer. Have fun! 

Other 
sessions can be found here: [https://www.datacamp.com/ai-code-alongs](https://www.datacamp.com/ai-code-alongs)
```
---

     
 
all -  [ Best resources to learn to advanced RAG topics & and to end projects ](https://www.reddit.com/r/LangChain/comments/19ehe5m/best_resources_to_learn_to_advanced_rag_topics/) , 2024-01-26-0910
```
it has a collab notebook, blog links & all code
```
---

     
 
all -  [ React/JSX to text parser? ](https://www.reddit.com/r/LangChain/comments/19ehc9w/reactjsx_to_text_parser/) , 2024-01-26-0910
```
I want to build a **chatbot** that has access to **all pages** in my website's GitHub repository. 

The [GitHubRepoLoade
r](https://js.langchain.com/docs/integrations/document_loaders/web_loaders/github#usage) makes it easy to fetch all page
s and turn them into documents. But I would also like to **strip these documents of all the React code** and keep only t
he user-readable information.

I tried Langchain.js's [html-to-text](https://js.langchain.com/docs/integrations/document
_transformers/html-to-text) converter but that didn't work. I also found [react-to-text](https://www.npmjs.com/package/r
eact-to-text) but this one expects an actual React component as its argument. I have the full file as a string.
```
---

     
 
all -  [ How to make a properly prompt to ask questions based on a context? ](https://www.reddit.com/r/OpenAIDev/comments/19ef5pv/how_to_make_a_properly_prompt_to_ask_questions/) , 2024-01-26-0910
```
Hello!

I was using Langchain for OpenAI and now i wanted to use the library OpenAI, in specific the Completion.create m
ethod, and looks like the prompt is no longer useful, anyone know how to change this to make it work for openai library?
 Thank you so much!

    Use the following pieces of context to answer the question at the end. If you don't know the an
swer just say I don't know, don't try to make up an answer.
    
    {context}
    
    Question: {question}
    Answer 
in Italian:

Regards!
```
---

     
 
all -  [ Has anyone used Llama.cpp python with gpu in vscode to load local llm. Does it even work with VSCode ](https://www.reddit.com/r/LangChain/comments/19eco2b/has_anyone_used_llamacpp_python_with_gpu_in/) , 2024-01-26-0910
```
I’ve used these commands to install it in VSCode 

export CUDACXX='/mnt/c/Program Files/NVIDIA GPU Computing Toolkit/CUD
A/v12.3/bin/nvcc.exe'
 export CMAKE_ARGS='-DLLAMA_CUBLAS=on -DCMAKE_CUDA_ARCHITECTURES=all-major -DCUDAToolkit_ROOT=C:\P
rogram Files\NVIDIA GP
 export FORCE_CMAKE=1
 pip install llama-cpp-python --no-cache-dir --force-reinstall --upgrade

S
uccessfully installed but it’s still not accessing gpu. I’ve nvidia GeForce RTC 3070 Ti 

How do I know how many n_gpu_l
ayers to set
```
---

     
 
all -  [ Purpose of Agents ](https://www.reddit.com/r/LangChain/comments/19ecbnb/purpose_of_agents/) , 2024-01-26-0910
```
Hi, I've been using agents with autogen and crew, and now langgraph, mostly for learning and small/mid scale programs.
T
he more I use them the more I'm confused about the purpose of the agent framework in general.

The scenarios I've tested
: read input, execute web search, summaries, return to user. Most other usecases also follow a sequential iteration of s
teps. 
For these usecases, there is no need to include any sort of agents, it can be done through normal python scripts.

Same goes for other usecases

I'm trying to think about what does agents let us do that we could not do with just scrip
ts with some logic. Sure, the LLM As OS is a fantastic idea, but in a production setting I'm sticking to my scripts rath
er than hoping the LLM will decide which tool to use everytime...

I'm interested to learn the actual usecases and poten
tial of using agents too execute tasks, so please do let me know
```
---

     
 
all -  [ Create AI Chatbots for Websites in Python - EmbedChain Dash ](https://www.reddit.com/r/LangChain/comments/19eaixd/create_ai_chatbots_for_websites_in_python/) , 2024-01-26-0910
```
Hey Everyone,  
A few days ago, I created this free video tutorial on how to  build an AI Chatbot in Python. I use the E
mbedChain (built on top of LangChain) and Dash libraries, as I show how to train and interact with your bot. Hope you fi
nd it helpful. 

[https://youtu.be/tmOmTBEdNrE](https://youtu.be/tmOmTBEdNrE)

&#x200B;

https://preview.redd.it/t2ebobt
8zbec1.png?width=1280&format=png&auto=webp&s=b2dcd9f2a930da35f2862b368a535d30ad885825
```
---

     
 
all -  [ How do I scale the current use case that involves using fine tuned gpt 3.5 model? ](https://www.reddit.com/r/OpenAI/comments/19ea148/how_do_i_scale_the_current_use_case_that_involves/) , 2024-01-26-0910
```
I am looking for some tools in the cloud that I can use to scale a particular use case for my company. We were working o
n a chatbot that involved using gpt 3.5 and langchain agents. Sine fine tuning was introduced later last year, we have q
uickly adapted to that and it worked wonders for our use case. 

Now, all the scripts I have created for data preparatio
n for fine tuning is in my local machine. We are looking to use some cloud based solutions to create and manage the trai
ning data. Now, if it were only one use case, I could simply use gcs buckets to store and version the data. But my boss 
wants me to scale for multiple use cases. 

Here's a scenario:

If there are 2 dozen generative AI use cases which invol
ves the usage of fine tuned model, how would I manage data for every use case. And if other team wants to utitlize some 
of the existing data from the existing use case, how could they easily identify where to look for and generate similar d
ata, etc. 

I'm not sure if I am able to define the problem correctly, but from what I understood is that my boss wants 
me to scale the current use case for multiple use cases with multiple datasets while managing the training data effectiv
ely so that its not a burden when someone wants to use the same data. 

I'm not sure which direction shall I head to in 
order to solve this problem. I'll be glad if someone can help me on this.
```
---

     
 
all -  [ Optimizing Source Citations for Comprehensive References: How to attribute Documents Instead of Chun ](https://www.reddit.com/r/LangChain/comments/19e8ylz/optimizing_source_citations_for_comprehensive/) , 2024-01-26-0910
```
Hey! I've been working with a vast vector database containing thousands of text documents, each spanning an average of 1
0-12 pages (sometimes even up to 50 pages). 
I've noticed that when querying the data and citing sources, the system cur
rently cites only the individual chunks rather than the entire document. Has anyone found an efficient way to attribute 
the entire document, complete with a proper title, instead of just the chunks?
```
---

     
 
all -  [ SSLCertVerificationError in Docker When Integrating OpenAI Embeddings with FAISS for LangChain ](https://www.reddit.com/r/LangChain/comments/19e8txp/sslcertverificationerror_in_docker_when/) , 2024-01-26-0910
```
Hello Reddit Community,

I am currently working on a Document Information extractor project using LangChain within a Doc
ker environment. The project involves integrating OpenAI embeddings with FAISS for document search. While everything wor
ks fine locally, I run into an SSL certificate verification error when I attempt to run the same code in Docker. The err
or is as follows:

Error

    MaxRetryError: HTTPSConnectionPool(host='openai.blob.core.windows.net', port=443): Max ret
ries exceeded with url: /embeddings/... (Caused by SSLError(SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED
] certificate verify failed: unable to get local issuer certificate (_ssl.c:1123)'))) 

This error occurs at the followi
ng line of code:

Python code

    docsearch = FAISS.from_documents(documents, OpenAIEmbeddings()) 

The Docker containe
r seems unable to verify the SSL certificate presented by the OpenAI server. I've ensured my internet connection is stab
le, and there are no issues with SSL certificates when running the code outside of Docker.

Has anyone encountered a sim
ilar issue or have any suggestions on what might be going wrong with SSL verification in Docker? What steps can I take t
o resolve this SSLCertVerificationError within the Docker environment?

Any insights or advice would be greatly apprecia
ted. Thank you for your help!
```
---

     
 
all -  [ Processing sensitive info with Mistral for cheap ](https://www.reddit.com/r/LangChain/comments/19e7zga/processing_sensitive_info_with_mistral_for_cheap/) , 2024-01-26-0910
```
Hello, I am looking for the cheapest way possible to process sensitive documents using Mistral's 8x7b model. It probably
 should be self-hosted to ensure the nothing from the document leaks. I've found that many APIs are vague about what inf
ormation is stored. I have a budget around $100 a month to deploy this model, and to lower the cost it would be ok to on
ly deploy it during the work day around \~160 hours a month. Any help would be appreciated!
```
---

     
 
all -  [ one agent does all the work, what am I doing wrong ? ](https://www.reddit.com/r/crewai/comments/19e5ryu/one_agent_does_all_the_work_what_am_i_doing_wrong/) , 2024-01-26-0910
```
I'm trying to get a coder agent and a testing agent to iterate back and forth, but the tester never seems to be used....
  


    import os
    from crewai import Agent, Task, Crew, Process
    
    
    from langchain_community.llms import 
Ollama
    ollama_llm = Ollama(model='mistral')
    
    
    from langchain_community.tools import DuckDuckGoSearchRun

    search_tool = DuckDuckGoSearchRun()
    
    from langchain.agents import Tool
    from langchain_experimental.utili
ties import PythonREPL
    repl_tool = Tool(
        name='python_repl',
        description='A Python shell. Use this t
o execute python commands. Input should be a valid python command. If you want to see the output of a value, you should 
print it out with `print(...)`.',
        func=PythonREPL.run,
    )
    
    
    # Define your agents with roles and g
oals
    programmer = Agent(
      role='Senior Programmer',
      goal='Create elegant and efficient python code',
    
  backstory='''You have has years working as a programmer, it is second nature to you
      you understand the importanc
e of testing and pass all your delegate all your output to the test engineer agent 
      If unable to find specific lib
raries, you will create functions to fullfill needed requirements
      ''',
      verbose=True,
      allow_delegation=
True,
      tools=[search_tool],
      llm=ollama_llm # was defined above in the file
    )
    
    tester = Agent(
   
   role='Test engineer',
      goal='Test code from the programmer and provide feedback',
      backstory='''You can exe
cute python code and test it against the provided task''',
      verbose=True,
      allow_delegation=True,
      llm=ol
lama_llm,
      tools=[repl_tool]
    )
    
    task1 = Task(
      #description='''Create a program to draw ascii bann
ers, test multiple algorithms, each letter should
      #be built from font data with each pixel represented by an ascii
 character, use different characters
      #to provide a shading effect
      #''',
      description='''provide a way t
o count from 1 to 10''',
      agent=programmer
    )
    
    
    # Instantiate your crew with a sequential process
  
  crew = Crew(
      agents=[programmer, tester],
      tasks=[task1],
      verbose=2, # You can set it to 1 or 2 to di
fferent logging levels
    )
    
    # Get your crew to work!
    result = crew.kickoff()
    
    print('#############
#########')
    print(result)
    

&#x200B;
```
---

     
 
all -  [ Creating demo conversational AI for Client ](https://www.reddit.com/r/LangChain/comments/19e0853/creating_demo_conversational_ai_for_client/) , 2024-01-26-0910
```
I'm creating a demo for a client - it will involve a web ui, a conversational component and some knowledge retrieval. An
y insight into what is the best way to set this up? Whether for an MVP or Production grade software? 

I really do like 
Langchain for its flexibility (no vendor lock-in) but am also open to Assistants API. I'm wondering specifically what is
 the best 'front end' chat interface (Botpress ,Voiceflow, custom JS) and how others are setting up a seamless experienc
e while having chatGPT like power. 

Just looking to think about tradeoffs as I plan to design the service.
```
---

     
 
all -  [ Can we use Conversation History in rag chain? ](https://www.reddit.com/r/LangChain/comments/19dya0n/can_we_use_conversation_history_in_rag_chain/) , 2024-01-26-0910
```
Currently, my chatbot can generate answers for current questions using the context (acc to prompt). Now I want to use th
e conversational part i.e., the chat history part to make it more sensible. How is that possible?
```
---

     
 
all -  [ Updated Pinecone client issue with Langchain vectorstore ](https://www.reddit.com/r/LangChain/comments/19dxzv2/updated_pinecone_client_issue_with_langchain/) , 2024-01-26-0910
```
I have had to upgrade pinecone-client and dependencies in conjunction with langchain for vectorstores.  In doing so ran 
into a conflict with the imports for pinecone import Pinecone and langchain_community.vectorstores import Pinecone 

whe
re the class config appears incompatible now and errors with api_key unexpected on Pinecone client creation unless I rem
ove the langchain import line which of course causes the vectorstore setup to fail.  

Running the following versions:
P
inecone-client 3.0.1
Langchain 0.1.3
Langchain-community 0.0.14
Langchain-core 0.1.15

Any input greatly appreciated - t
his update made current chatbot inoperable 

Thanks
```
---

     
 
all -  [ The real purpose of AI is to let it be the jerk for me. ](https://www.reddit.com/r/ChatGPT/comments/19dxdhw/the_real_purpose_of_ai_is_to_let_it_be_the_jerk/) , 2024-01-26-0910
```
Kinda serious, kinda joking, but curious who else is using AI to save themselves from explaining trivial engineering pri
nciples and decisions to non-technical people. For example, it must save me hours every week to just put in the naive qu
estions I get asked in business calls ( or the bad decisions that I need to shut down ) and ask the AI to explain why it
 is/isn't a good idea to do/not do this thing. The great part is at the end of the conversation I get to say, 'Look ladi
es and gentlemen, I am always open to discussion and improvement of ideas but AI is the one arguing against you not me. 
I am just relaying information.' Basically I am using AI as my bad cop in my good cop bad cop routine. Anyone else doing
 this?

After writing this I just realized some one needs to create an AI startup that just has it constantly listen to 
calls and be the jerk to shut down stupid stuff in real time. I am too lazy. Please build me this tool open source using
 Langchain. Should be super easy but not cost effective unless using local models.
```
---

     
 
all -  [ Live HowTo for building your 1st RAG App! ](https://www.reddit.com/r/LlamaIndex/comments/19dwheq/live_howto_for_building_your_1st_rag_app/) , 2024-01-26-0910
```
I'm so excited for tomorrows live how to that DataStax and LangChain are putting together that I had to share this! In m
y opinion, here's an easy way for how to develop your 1st RAG app \~ [https://www.crowdcast.io/c/5z80anwt7e13?utm\_mediu
m=social\_organic&utm\_source=socialstax&utm\_campaign=putv&utm\_content=](https://www.crowdcast.io/c/5z80anwt7e13?utm_m
edium=social_organic&utm_source=socialstax&utm_campaign=putv&utm_content=)
```
---

     
 
all -  [ Webinar - LangChain JS, Vercel, Astra with Wikipedia data ](https://www.reddit.com/r/generativeAI/comments/19dw79o/webinar_langchain_js_vercel_astra_with_wikipedia/) , 2024-01-26-0910
```
Just stumbled upon this amazing webinar that's all set for tomorrow! It's about crafting a real-time RAG app using LangC
hain.js, Vercel, and Astra DB, leveraging Wikipedia. It looks really cool: [https://dtsx.io/498383Z](https://dtsx.io/498
383Z) 
```
---

     
 
all -  [ WikiChat ](https://www.reddit.com/r/LangChain/comments/19dvjtb/wikichat/) , 2024-01-26-0910
```
Saw this webinar that is around building a real-time RAG app on Wikipedia with LangChain.js, Vercel, and Astra DB. Looks
 interesting and is set to go tomorrow: [https://dtsx.io/498383Z](https://dtsx.io/498383Z)
```
---

     
 
all -  [ Become an AI Developer (Free 9-Part Series) ](https://www.reddit.com/r/computervision/comments/19dvemg/become_an_ai_developer_free_9part_series/) , 2024-01-26-0910
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

     
 
MachineLearning -  [ New Data API for Astra [N] ](https://www.reddit.com/r/MachineLearning/comments/199uobn/new_data_api_for_astra_n/) , 2024-01-26-0910
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

     
 
MachineLearning -  [ [D] While using function calling or tools on openai or langchain, does openai have access to the dat ](https://www.reddit.com/r/MachineLearning/comments/199t8be/d_while_using_function_calling_or_tools_on_openai/) , 2024-01-26-0910
```
I am working on a client project and I am using langchain's tools and agents. I want to know if the data is getting pass
ed to openai or is it just like that - Output of one function is being directly passed to the second function with the k
nowledge of openai.
```
---

     
 
MachineLearning -  [ [D] Code vs JSON output for LLM agents? Frameworks like LangChain rely on LLMs responding with JSON  ](https://www.reddit.com/r/MachineLearning/comments/197f416/d_code_vs_json_output_for_llm_agents_frameworks/) , 2024-01-26-0910
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

     
 
MachineLearning -  [ [D] Are Custom LLM RAG apps going to become redundant? ](https://www.reddit.com/r/MachineLearning/comments/1929n4f/d_are_custom_llm_rag_apps_going_to_become/) , 2024-01-26-0910
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

     
 
MachineLearning -  [ [P] An open-source project for deploying local models ](https://www.reddit.com/r/MachineLearning/comments/18zkm5m/p_an_opensource_project_for_deploying_local_models/) , 2024-01-26-0910
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

     
 
MachineLearning -  [ [Project] Temporal Augmented Retrieval (TAR) - Dynamic RAG ](https://www.reddit.com/r/MachineLearning/comments/18uddmj/project_temporal_augmented_retrieval_tar_dynamic/) , 2024-01-26-0910
```
From a corpus of text, how can you detect emerging topics and their evolution through time?

Introducing Temporal Augmen
ted Retrieval (TAR). (built in the context of buildspace n&w s4)

TAR is an open-source advanced RAG approach that aims 
to factor in the dynamic and temporal aspects of textual data when performing retrieval.

It allows us to understand the
 evolution of discussed topics over time.

The idea behind this project is to open the debate regarding the current limi
tations of RAG methods

This first approach has been built without using RAG frameworks (like Jerry Liu’s langchain) and
 focuses on financial tweets 

Relevant links:

Medium: [https://medium.com/@adam-rida/temporal-augmented-retrieval-tar-
dynamic-rag-ad737506dfcc](https://medium.com/@adam-rida/temporal-augmented-retrieval-tar-dynamic-rag-ad737506dfcc)

Gith
ub:[https://github.com/adrida/Temporal\_RAG](https://github.com/adrida/Temporal_RAG)

Hugging Face Benchmark: [https://h
uggingface.co/spaces/Adr740/Temporal-RAG-Benchmark](https://huggingface.co/spaces/Adr740/Temporal-RAG-Benchmark)

My web
site: [adrida.github.io](https://adrida.github.io)

&#x200B;

https://preview.redd.it/lj7wkhk70f9c1.png?width=960&format
=png&auto=webp&s=fc79c5034351a1711e1ec051919a5c4d2edbc333
```
---

     
 
MachineLearning -  [ [R][P] Autogen + Langchain Tools + Local LLM doesn't work. ](https://www.reddit.com/r/MachineLearning/comments/18tex1j/rp_autogen_langchain_tools_local_llm_doesnt_work/) , 2024-01-26-0910
```
Hey folks, 

So I'm playing around with the agent framework Autogen and I'm trying to create agents by providing it cust
om tools to use. These custom tools are defined in the langchain framework. Furthermore, I am using open source LLM mode
ls like Mistral, LLAMA, Mixtral etc.

In my experience, I have been unable to get the Autogen+LocalLLM framework to iden
tify the right tools to use given the prompt. However it does a fantastic job with the GPT model. 

Please note that my 
goal is for the agent to mandatorily use the tools provided and not come up with its own code. And the agent should figu
re out the right tool to use. 

I have been very explicit with my prompting, despite which I am unable to get this to wo
rk.

Any thoughts and suggestions? Please let me know ! Please share your experiences as well. Cheers !
```
---

     
 
MachineLearning -  [ [P] Seeking Advice for Building a School Handbook Chatbot Using OpenAI and Vector Databases ](https://www.reddit.com/r/MachineLearning/comments/18rndcp/p_seeking_advice_for_building_a_school_handbook/) , 2024-01-26-0910
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

     
 
deeplearning -  [ [D] Unleashing the Power of Langchain with Wandb: Revolutionizing Topic Modeling and Evaluation ](https://www.reddit.com/r/deeplearning/comments/191mm83/d_unleashing_the_power_of_langchain_with_wandb/) , 2024-01-26-0910
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

     
