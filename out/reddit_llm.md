 
all -  [ Please help with my llm chain invocation ](https://i.redd.it/ngoudxie6yrc1.jpeg) , 2024-04-02-0910
```
I’m completely new to using Langchain which I’m using in a JavaScript project. I have a custom_K.gguf base model(not a c
hat model). From the screenshot, when the line 
const result = await chain.call({ question: input }) runs, I get this:


[chain/start] [1:chain:LLMChain] Entering Chain run with input: {
  'question': 'who is elon musk',
  'chat_history': ''

}
[chain/error] [1:chain:LLMChain] [1ms] Chain run errored with error: 'this.llm.pipe is not a function\n\nTypeError: t
his.llm.pipe is not a function\n    at LLMChain._call 

Without using chain, I'm able to send and receive answers to the
 model without issues but I'm using chain for history/memory purpose and I can't seem to understand why this is happenin
g. 

The difference between my code and the [sample](https://github.com/langchain-ai/langchainjs/blob/main/examples/src/
chains/llm_chain_stream.ts) on their website is the use of LlmaCpp in place of OpenAI. So I’m not sure where else to loo
k.

Would really pepreciate any help I can get please 🙏🏾.

I’ve tried to [create a discussion](https://github.com/langch
ain-ai/langchainjs/discussions/4940) on the langchainjs repo but only received a response from the bot which wasn’t very
 helpful.


```
---

     
 
all -  [ Integrating a Hugging Face LLM Model with Langchain via SageMaker ](https://www.reddit.com/r/LangChain/comments/1bthz3u/integrating_a_hugging_face_llm_model_with/) , 2024-04-02-0910
```
Hello everyone,

I'm trying to integrate a LLM with Langchain, specifically using the create\_react\_agent function docu
mented here: [Langchain create\_react\_agent documentation](https://api.python.langchain.com/en/latest/agents/langchain.
agents.react.agent.create_react_agent.html).

For this test, I am trying to work with the open-source FLAN model from Hu
gging Face, available at: [FLAN T5 XL on Hugging Face](https://huggingface.co/google/flan-t5-xl/tree/main). My goal is t
o deploy this model as an endpoint in AWS SageMaker and then utilize it within Langchain by creating a react agent.

Wha
t steps should I follow to ensure that when I make a call to this SageMaker endpoint, it returns an LLM object that Lang
chain's create\_react\_agent function can utilize? Also, do not want to use SageMaker DLC images.

I'm unsure about the 
best practices for making the deployed model compatible as an LLM object for Langchain, especially in terms of the expec
ted response format and any necessary wrappers or adapters.

Can some one offer insights into:

1. The specific modifica
tions or configurations needed on the SageMaker side to ensure compatibility with Langchain.
2. How to properly format t
he SageMaker endpoint's response to be recognized as an LLM object by Langchain.
3. Any examples or templates that might
 be helpful for this process.  


If this is not possible with SageMaker, what are the other options that I can look int
o? 

Appreciate your help on this.
```
---

     
 
all -  [ I am building a chatgpt alternative that doesn't lock you into a single model ](https://www.reddit.com/r/ChatGPT/comments/1btbipl/i_am_building_a_chatgpt_alternative_that_doesnt/) , 2024-04-02-0910
```
Three months ago, during the whole Sam leaving openai chaos period, i posted this:[https://www.reddit.com/r/ChatGPT/comm
ents/189dddw/i\_am\_terrified/](https://www.reddit.com/r/ChatGPT/comments/189dddw/i_am_terrified/?utm_source=share&utm_m
edium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button)

I shared my concerns about the heavy reliance on a f
ew centralized AI services and the increasing levels of censorship and limitation being imposed on these platforms. The 
response from this community was nothing short of incredible, and it fueled my resolve to do something about it.

I have
 working on it during my free time and its nearly complete so i am sharing update 1,as you see i am using a coding copil
ot assistant with the model phind-codellama-v2 which is specially finetuned for this, also adding a lot of other uncenso
red models too which are better for stuff like creative writing and roleplay bots.

Here to ask you all for any feedback
 or feature requests you might have as i continue working on the [site](https://muxchat.com)  


[Muxchat](https://previ
ew.redd.it/zdy2aq4mvwrc1.png?width=1440&format=png&auto=webp&s=69000d046a546a2d5bfca1298dde5ed8d8f4aa02)

&#x200B;
```
---

     
 
all -  [ Why does langchain prompt using HTML tags? ](https://www.reddit.com/r/LangChain/comments/1bt9qt3/why_does_langchain_prompt_using_html_tags/) , 2024-04-02-0910
```
This may be obvious to some, or obvious to none, but why do langchain use html tags in their prompts to separate section
s of prompts. For instance in their docs they use the following: 

<context>  
{context}  
</context>

I of course under
stand the usefulness of clear separations in the prompt templates but why use the HTML tags? Intuitively I would've thou
ght LLM's wouldn't be as able to interpret these tags compared  to raw text? However I'm not certain on the formatting o
f internet data proprietary  LLM's like Open AI's GPT series were trained on.
```
---

     
 
all -  [ AI agents Group Discussion using Autogen ](https://www.reddit.com/r/LangChain/comments/1bt7xrf/ai_agents_group_discussion_using_autogen/) , 2024-04-02-0910
```
Hey everyone, check out this tutorial on how to enable Multi-Agent conversations and group discussion between AI Agents 
using Autogen by Microsoft by GroupChat and ChatManager functions : https://youtu.be/zcSNJMUYHBk?si=0EBBJVw-sNCwQ1K_
```
---

     
 
all -  [ [Project] Picachain, image search made simple. ](https://www.reddit.com/r/MachineLearning/comments/1bt7epv/project_picachain_image_search_made_simple/) , 2024-04-02-0910
```
I am working on creating something for image search, basically something like langchain for images. Probably add videos 
too.

Currently supports chromaDB. Working on pinecone and other vector dbs. [https://github.com/d1pankarmedhi/picachain
](https://github.com/d1pankarmedhi/picachain)

Will you use something like this? What else should I add? Feel free to ad
d your views.

Appreciate your feedback or any feature ideas :)

&#x200B;
```
---

     
 
all -  [ Open-Source AI Cookbook [Hugging Face] ](https://www.reddit.com/r/CompSocial/comments/1bt6z2m/opensource_ai_cookbook_hugging_face/) , 2024-04-02-0910
```
Are you building AI-powered workflows and projects using open-source tools/models as part of your research? You may want
 to check out the Open-Source AI Cookbook from Hugging Face, which collects community-created notebooks covering a numbe
r of use cases. Here are some of the recently-added examples:

* [**Using LLM-as-a-judge 🧑‍⚖️ for an automated and versa
tile evaluation**](https://huggingface.co/learn/cookbook/llm_judge)
* [**Create a legal preference dataset**](https://hu
ggingface.co/learn/cookbook/pipeline_notus_instructions_preferences_legal)
* [**Suggestions for Data Annotation with Set
Fit in Zero-shot Text Classification**](https://huggingface.co/learn/cookbook/labelling_feedback_setfit)
* [**Implementi
ng semantic cache to improve a RAG system**](https://huggingface.co/learn/cookbook/semantic_cache_chroma_vector_database
)
* [**Building A RAG Ebook “Librarian” Using LlamaIndex**](https://huggingface.co/learn/cookbook/rag_llamaindex_librari
an)
* [**Stable Diffusion Interpolation**](https://huggingface.co/learn/cookbook/stable_diffusion_interpolation)
* [**Bu
ilding A RAG System with Gemma, MongoDB and Open Source Models**](https://huggingface.co/learn/cookbook/rag_with_hugging
_face_gemma_mongodb)
* [**Prompt Tuning with PEFT Library**](https://huggingface.co/learn/cookbook/prompt_tuning_peft)
*
 [**Migrating from OpenAI to Open LLMs Using TGI’s Messages API**](https://huggingface.co/learn/cookbook/tgi_messages_ap
i_demo)
* [**Automatic Embeddings with TEI through Inference Endpoints**](https://huggingface.co/learn/cookbook/automati
c_embedding_tei_inference_endpoints)
* [**Simple RAG for GitHub issues using Hugging Face Zephyr and LangChain**](https:
//huggingface.co/learn/cookbook/rag_zephyr_langchain)
* [**Embedding multimodal data for similarity search using 🤗 trans
formers, 🤗 datasets and FAISS**](https://huggingface.co/learn/cookbook/faiss_with_hf_datasets_and_clip)
* [**Fine-tuning
 a Code LLM on Custom Code on a single GPU**](https://huggingface.co/learn/cookbook/fine_tuning_code_llm_on_single_gpu)

* [**RAG Evaluation Using Synthetic data and LLM-As-A-Judge**](https://huggingface.co/learn/cookbook/rag_evaluation)
* [
**Advanced RAG on HuggingFace documentation using LangChain**](https://huggingface.co/learn/cookbook/advanced_rag)
* [**
Detecting Issues in a Text Dataset with Cleanlab**](https://huggingface.co/learn/cookbook/issues_in_text_dataset)

Check
 out the Open-Source AI Cookbook here: [https://huggingface.co/learn/cookbook/index](https://huggingface.co/learn/cookbo
ok/index)

Do you have any go-to resources, notebooks, or tutorials for open-source AI tools that you would recommend? T
ell us about them in the comments!
```
---

     
 
all -  [ [For hire] Ex-Booking[dot]com Data Scientist and GenAI specialist [50 USD/hr]  ](https://www.reddit.com/r/ForHire_Programmers/comments/1bt6opo/for_hire_exbookingdotcom_data_scientist_and_genai/) , 2024-04-02-0910
```
Hi I have used this subreddit to get some clients before and been able to deliver to all of them.

Here is my work exper
ience + technical expertise:

1. 4+ years of experience in data roles
2. Worked at Agoda (Booking[dot]com) as Data analy
st
3. Worked in a Norwegian Telecom provider as Data Scientist
4. Working part time as GenAI specialist

Skills: Statist
ics, ML, Python, SQL and Tableau

Also write about my projects on Medium: https://medium.com/firebird-technologies/chat-
with-your-pdfs-using-langchain-e57866b7926d

https://medium.com/firebird-technologies/using-langchain-to-teach-an-llm-to
-write-like-you-aab394d54792
```
---

     
 
all -  [ CSV RAG with langchain issue ](https://www.reddit.com/r/LangChain/comments/1bt64ld/csv_rag_with_langchain_issue/) , 2024-04-02-0910
```
Does anyone have a working CSV RAG application using LangChain and open-source embeddings and LLMs? I've been trying to 
get a working implementation for a while, but I'm running into the same problem with CSV files. As soon as I run a query
, it's not able to retrieve more than four relevant chunks from the vectordb. If a query requires the whole dataset to a
nswer the question, it will not be able to answer it. If anyone has working code for CSV RAG, could they share it? It wo
uld be helpful. 
```
---

     
 
all -  [ CSV RAG with langchain  ](https://www.reddit.com/r/LocalLLaMA/comments/1bt62bk/csv_rag_with_langchain/) , 2024-04-02-0910
```
Does anyone have a working CSV RAG application using LangChain and open-source embeddings and LLMs? I've been trying to 
get a working implementation for a while, but I'm running into the same problem with CSV files. As soon as I run a query
, it's not able to retrieve more than four relevant chunks from the data. If a query requires the whole dataset to answe
r the question, it will not be able to answer it. If anyone has working code for CSV RAG, could they share it? It would 
be helpful.
```
---

     
 
all -  [ +500mm rows of data is embedding or fine tuning a good way to enable this data? ](https://www.reddit.com/r/LangChain/comments/1bt5opa/500mm_rows_of_data_is_embedding_or_fine_tuning_a/) , 2024-04-02-0910
```
I have hundreds of millions of rows of data that's basically click tracking.  I want to create a chat bot with this data
.  I'm new to LLM customization.

Is fine tuning a model with this data a good way to go about this or is creating embed
dings better?

I'm open to breaking it up in to 3 month chunks.  I dont have access to unlimited hardware.
```
---

     
 
all -  [ PgVector Filtering Methods/Options in JS ](https://www.reddit.com/r/LangChain/comments/1bt4vgk/pgvector_filtering_methodsoptions_in_js/) , 2024-04-02-0910
```
Hi there! I’ve been searching for documentation on how to filter my pgvector similarity searches (with LangchainJS) but 
haven’t found any good documentation on the available options/methods. Does anyone know where I can find some? There is 
one example on the Langchain docs using ‘in’ but nothing else.

Also would anyone be able to show me how to do filtering
 based on dates?

Thank you!
```
---

     
 
all -  [ A Senior SDE from Google recommended my book on LangChain 😎 ](https://i.redd.it/lazcbinjjvrc1.png) , 2024-04-02-0910
```
Never thought my debut book 'LangChain in your Pocket' would be this big a hit. First being a national bestseller (progr
amming), than an international Bestseller(AI) and now this. A big thanks to the community 🥰🥰
```
---

     
 
all -  [ RAGFlow, the deep document understanding based RAG engine is open sourced ](https://www.reddit.com/r/LangChain/comments/1bt3ozy/ragflow_the_deep_document_understanding_based_rag/) , 2024-04-02-0910
```
## Key Features

### 'Quality in, quality out'

* [Deep document understanding](https://github.com/infiniflow/ragflow/bl
ob/main/deepdoc/README.md)\-based knowledge extraction from unstructured data with complicated formats.
* Finds 'needle 
in a data haystack' of literally unlimited tokens.

### Template-based chunking

* Intelligent and explainable.
* Plenty
 of template options to choose from.

### Grounded citations with reduced hallucinations

* Visualization of text chunki
ng to allow human intervention.
* Quick view of the key references and traceable citations to support grounded answers.


###  Compatibility with heterogeneous data sources

* Supports Word, slides, excel, txt, images, scanned copies, struct
ured data, web pages, and more.

### Automated and effortless RAG workflow

* Streamlined RAG orchestration catered to b
oth personal and large businesses.
* Configurable LLMs as well as embedding models.
* Multiple recall paired with fused 
re-ranking.
* Intuitive APIs for seamless integration with business.

The github address:

[https://github.com/infiniflo
w/ragflow](https://github.com/infiniflow/ragflow)

The offitial homepage:

[https://ragflow.io/](https://ragflow.io/)

T
he demo address:

[https://demo.ragflow.io/](https://demo.ragflow.io/)
```
---

     
 
all -  [ Would you use LangChain more if it had better documentation? ](https://www.reddit.com/r/mlops/comments/1bt1ieb/would_you_use_langchain_more_if_it_had_better/) , 2024-04-02-0910
```
I've seen a lot of discussions about LangChain's documentation being poor or unintuitive. Would you use it more or at al
l if it had better documentation and user experience?

If you have any other experience or something you'd like to share
 I'd love to hear about it and other products you use.

[View Poll](https://www.reddit.com/poll/1bt1ieb)
```
---

     
 
all -  [ Create your AI SaaS for chatbot creation in just one day! ](https://www.reddit.com/r/micro_saas/comments/1bt190p/create_your_ai_saas_for_chatbot_creation_in_just/) , 2024-04-02-0910
```
I've developed an easy to use API for building advanced AI chatbots, utilizing cutting-edge technologies like Langchain,
 FastAPI, Gemini, OpenAI GPT-4, Pinecone, and strong AI security measures. It's perfect for SaaS platforms looking to of
fer customizable chatbot solutions. 

Interested? Contact me at jaberibraheem808@gmail.com.  

```
---

     
 
all -  [ Create your AI SaaS for chatbot creation in just one day! ](https://www.reddit.com/r/smallbusiness/comments/1bt15ea/create_your_ai_saas_for_chatbot_creation_in_just/) , 2024-04-02-0910
```
I've developed an easy to use API for building advanced AI chatbots, utilizing cutting-edge technologies like Langchain,
 FastAPI, Gemini, OpenAI GPT-4, Pinecone, and strong AI security measures. It's perfect for SaaS platforms looking to of
fer customizable chatbot solutions.   
Interested? Contact me at jaberibraheem808@gmail.com.  

```
---

     
 
all -  [ Would you use LangChain more if it had better documentation? ](https://www.reddit.com/r/LangChain/comments/1bszde0/would_you_use_langchain_more_if_it_had_better/) , 2024-04-02-0910
```
I've seen a lot of discussions about LangChain's documentation being poor or unintuitive. Would you use it more or at al
l if it had better documentation and user experience?  


If you have any other experience or something you'd like to sh
are I'd love to hear about it.

[View Poll](https://www.reddit.com/poll/1bszde0)
```
---

     
 
all -  [ What do you guys think of CrewAI and the idea of agents ](https://www.reddit.com/r/developersIndia/comments/1bsyvpk/what_do_you_guys_think_of_crewai_and_the_idea_of/) , 2024-04-02-0910
```
Hey fellow developers, this weekend I was going through CrewAI, Langchain, and Ollama - to get an understanding of AI ag
ents. We in our startup are coming up with a POC of AI agents. I have explored CrewAI and it feels very simple and easy 
to build a basic AI agent that can do multiple tasks for you. I also tried exposing an API and integrate it with Remix f
rontend. Overall this idea of AI agents excites me a lot, you can create AI agents for yourself too if you want to autom
ate your work or anything like that. 

Also with so many tools availabe in CrewAI and also in LangChain, the opportuniti
es of building something kickass is fairly high.  
Anyone here developed anything with these? Any AI agent?  
What do yo
u guys think of AI agents and CrewAI?  


Also have you guys tried RAG? Sounds pretty useful build your own RAG framewor
k

  
Attaching some resources and videos I went through and read.  
CrewAI: [https://www.crewai.com/](https://www.crewa
i.com/)  
Lang chain: [https://python.langchain.com/docs/get\_started/introduction](https://python.langchain.com/docs/ge
t_started/introduction)

What is RAG: [https://research.ibm.com/blog/retrieval-augmented-generation-RAG](https://researc
h.ibm.com/blog/retrieval-augmented-generation-RAG)

[https://www.ai-jason.com/ai/ai-agent](https://www.ai-jason.com/ai/a
i-agent)

Some AI agents: [https://github.com/e2b-dev/awesome-ai-agents](https://github.com/e2b-dev/awesome-ai-agents)  


```
---

     
 
all -  [ LLMinator: A Langchain + Gradio based streaming Chatbot to run llms locally(cpu/cuda) directly from  ](https://www.reddit.com/r/LocalLLaMA/comments/1bsyqiw/llminator_a_langchain_gradio_based_streaming/) , 2024-04-02-0910
```
Hi I am currently working on a context-aware streaming chatbot based on Gradio, Langchain, Transformers. LLMinator can p
ull LLMs directly from HF & run them locally on cuda or cpu.

I am looking for recommendations & help from opensource co
mmunity to grow this further.

**Github Repo:** [https://github.com/Aesthisia/LLMinator](https://github.com/Aesthisia/LL
Minator)

**Goal:** To help developers with kickstarter code/tool to run LLMs.  


&#x200B;

[Preview](https://preview.r
edd.it/r168oxjc2urc1.png?width=2838&format=png&auto=webp&s=128728ad65fe57e78703ca634a2066625ea0aa8e)

**Features:**

* C
ontext-aware Chatbot.
* Inbuilt code syntax highlighting.
* Load any LLM repo directly from HuggingFace.
* Supports both
 CPU & Cuda modes.
* Load & Offload saved models.
* Command Line Args
* API Access(Soon to be available)

Any review or 
feedback is appreciated.
```
---

     
 
all -  [ ML Engineer internship in India ](https://i.redd.it/u98277gc2urc1.png) , 2024-04-02-0910
```
I am currently searching for ML internship but never got a call.
```
---

     
 
all -  [ Rust and RAG ](https://www.reddit.com/r/rust/comments/1bstely/rust_and_rag/) , 2024-04-02-0910
```
Is anyone working on RAG (Retrieval-augmented generation) here? I'd like to know how you approach it in the Rust world. 
Do you rely on a framework similar to Python's LangChain or LlamaIndex, or do you implement the pipeline yourself?
```
---

     
 
all -  [ Requesting help with ollama and apichain ](https://www.reddit.com/r/LangChain/comments/1bstbxn/requesting_help_with_ollama_and_apichain/) , 2024-04-02-0910
```
Just started diving into llms and langchain this weekend. I'm looking for some guidance on a particular issue, but recog
nize that I might be lacking some very fundamental knowledge.

I have ollama installed and wanted to be able to use lang
chain to read some api docs for some custom services I have around my home (custom smart home services to control device
s such as lights, tv, ac, etc) and allow me to interact with my devices via the llm. I followed a few links around the i
nternet, but they all basically have the same code structure \[[https://python.langchain.com/docs/use\_cases/apis](https
://python.langchain.com/docs/use_cases/apis), [https://towardsdatascience.com/integrating-an-external-api-with-a-chatbot
-application-using-langchain-and-chainlit-b687bb1efe58](https://towardsdatascience.com/integrating-an-external-api-with-
a-chatbot-application-using-langchain-and-chainlit-b687bb1efe58)\].

With OpenApi, things work more or less flawlessly, 
however when I switch the code over to use ollama, I struggle to get the model to work properly. From the errors, it see
ms like the first step of the apichain module (where it tries to produce the api url) fails more often than naught. It s
ometimes has an output in a sentence structure or the url is in quotes. I've tried tuning the prompt via the api\_url\_p
rompt argument, but to no avail. The only change I did from the examples in the links above is change the llm to be \`ll
m = Ollama(model='starcoder2:7b')\`.

Am I missing something or is it just  matter of find the right model? I've tried a
 few now and nothing produces a stable result.

\`\`\`codellama:latest

deepseek-coder:latest

dolphin-mixtral:latest

g
emma:latest

mistral:latest

openhermes:latest

starcoder2:7b

starling-lm:latest

wizardcoder:latest

\`\`\`
```
---

     
 
all -  [ LLM Agent platforms ](https://www.reddit.com/r/LocalLLaMA/comments/1bskjki/llm_agent_platforms/) , 2024-04-02-0910
```
Anyone working on LLM Agent systems?  What open source projects are you using?  What works well, what doesn't?

Searchin
g for something that will allow me to specify system prompts for classes of Agents ('Manager', 'Programmer', 'Tester', e
tc), the number of Agents per class (possibly dynamically created by 'Manager' as well), and the criteria for' Pass/Fail
' before final output.  Even better if it could pull models from HF or Ollama (codellama or deepseek coder).

Here's a l
ist I'm considering (thoughts on these welcome):

* [AutoGen](https://github.com/microsoft/autogen)
* [MetaGPT](https://
github.com/geekan/MetaGPT)
* AgentCoder ([white paper](https://arxiv.org/abs/2312.13010) only; any github for this?)
* [
LangGraph](https://github.com/langchain-ai/langgraph)
* [AlphaCodium](https://github.com/Codium-ai/AlphaCodium)
* Others

```
---

     
 
all -  [ Python-Airflow - Mutual Funds Fundamentals Uploader Dag ](https://www.reddit.com/r/u_SravzLLC/comments/1bsjflo/pythonairflow_mutual_funds_fundamentals_uploader/) , 2024-04-02-0910
```
 

**### Use Case**

Use this program to upload mutual funds fundamentals data to AWS S3.

Airflow Dag submits tickers t
o Airflow Celery workers using Task/Task Group Mapping.

Task groups/tasks perform http get from the service provider an
d upload the data to AWS S3.

Documentation Link: https://docs.sravz.com/docs/tech/airflow-dask/mutual-fund-fundamentals
-uploader/

Code: https://gist.github.com/sravzpublic/0ec6ed086d849c532d3dbcb9b531eb6d

Video Explanation: https://youtu
.be/NIRMRmyYxL4

Sravz LLC Analytics & Tech Series:

Documentation - Source code: 

Analytics: https://docs.sravz.com/do
cs/analytics/

Tech: https://docs.sravz.com/docs/tech/

Follow Us:

Youtube: [https://www.youtube.com/channel/UCZEu1jWMO
uknydEi0bcJLvA](https://www.youtube.com/channel/UCZEu1jWMOuknydEi0bcJLvA)

Facebook: [https://www.facebook.com/Sravz-Ltd
-105045281812833/](https://www.facebook.com/Sravz-Ltd-105045281812833/)

Instagram: [https://www.instagram.com/sravz\_ll
c/](https://www.instagram.com/sravz_llc/)

Twitter: [https://twitter.com/Sravz46106283](https://twitter.com/Sravz4610628
3)

LinkedIn: [https://www.linkedin.com/company/sravz-ltd?trk=public\_profile\_experience-group-header](https://www.link
edin.com/company/sravz-ltd?trk=public_profile_experience-group-header)

Medium: [https://medium.com/@sravzllc](https://m
edium.com/@sravzllc)

Reddit: https://www.reddit.com/user/SravzLLC

GitHub: [https://github.com/sravzpublic](https://git
hub.com/sravzpublic)

Gitter: [https://gitter.im/sravzpublic/community?utm\_source=share-link&utm\_medium=link&utm\_camp
aign=share-link](https://gitter.im/sravzpublic/community?utm_source=share-link&utm_medium=link&utm_campaign=share-link)


Discord: [https://discord.com/channels/917183474824273990/917183475289825342](https://discord.com/channels/917183474824
273990/917183475289825342)

\#openai #chatgpt #python #langchain  #finance #analytics #backtest #pyfolio #c++ #stocks #w
ebsockets #ibkr #trading #airflow #mutualfunds 
```
---

     
 
all -  [ Agent API is weird ](https://www.reddit.com/r/LangChain/comments/1bsfb5n/agent_api_is_weird/) , 2024-04-02-0910
```
It's different from other APIs inside LangChain. For example:

* AgentExecutor doesn't clearly specify the inputs and ou
tputs expected from your chain. What should the use provide?
* The chain is called agent, and it's not clear to me what'
s what
* There are OpenAI-specific code inside LangChain package, instead of having those in the langchain_openai packag
e. Why is that the case?
* Tools and toolkit docs are inside the agent documentation, despite having little to do with i
t. Are toolkits available only to agents?
* The whole concept is reimplemented in LangGraph. What should I use?
* The wh
ole agent API isn't on langchain_core. Is the APi unstable?


Are those questions reasonable? Is it truly a less mature 
part of langchain, or just a misunderstanding from my part?
```
---

     
 
all -  [ LangGraph Workflow for Quality Assurance ](https://www.reddit.com/r/LangChain/comments/1bsblmu/langgraph_workflow_for_quality_assurance/) , 2024-04-02-0910
```
I've been working on a concept to automate the Quality Assurance (QA) process for complex legal documents using LangGrap
h, aiming to streamline the workflow, reduce manual effort, and improve compliance efficiency. Handling specific parts o
f the QA process using AI rather human reviews, from initial document submission to final approval.

I see a ton of peop
le talking about document chat and integration with knowledge repos. Rather than just providing information I am looking
 to perform QA on the documents itself. 

Here's a brief overview of the workflow:

* **Document Submission (Manual User
 Action):** Entry point for examiners to submit documents.
* **Pre-Processing Node (Script for Data Manipulation):** Han
dles initial formatting and basic validation.
* **Policy Compliance Checker Node (PCCN):** Checks documents against poli
cy rules.
* **Error Suggestion Node (ESN):** Identifies compliance issues and suggests corrections.
* **Quality Assuranc
e Node (QAN):** Final review to ensure document quality.
* **Feedback and Interaction Node (FIN):** Where examiners revi
ew AI suggestions and apply corrections.
* **Approval and Compliance Marking Node (ACMN):** Marks documents as approved.


Some questions I have are:

1. Has anyone automated a Quality Assurance process with langchain/graph?
2. If yes, what 
was successful or what did not work?
3. Any suggestions on how to improve my approach?
4. Are there any examples you are
 aware of I could use as a reference?

I appreciate any help and thoughts on the topic!
```
---

     
 
all -  [ Roast my resume ](https://www.reddit.com/r/recruitinghell/comments/1bs99nt/roast_my_resume/) , 2024-04-02-0910
```
Lost track of how many applications i have sent but prolly 130+

Been looking for a job since mid October but i only man
aged to land an unpaid internship which will end soon. This job market is indeed tough and any piece of advice would be 
helpful.

https://preview.redd.it/knr4s5d7ynrc1.png?width=671&format=png&auto=webp&s=39e0ea8ba49c8c19188d27176d4728d3ab7
179a2


```
---

     
 
all -  [ LLM CACHING Explained  ](https://youtu.be/7eBzUio4CnI) , 2024-04-02-0910
```
I've recently created a new video on caching in LLM apps, in which I discuss the benefits of caching and why it's necess
ary. We also cover the capabilities of semantic cache in great detail.

#aiml #GenAI #llm #langchain
```
---

     
 
all -  [ [HELP]: Node.js - Help needed while creating context from web ](https://www.reddit.com/r/Langchaindev/comments/1bs3ghj/help_nodejs_help_needed_while_creating_context/) , 2024-04-02-0910
```
Hi Langchain community, I am completly new to this library.

I am trying to understand it so building a simple node API 
where I want to create a context from website like apple or amazon and ask model about prices for product.

Here is my c
urrent code:

    async function siteDetails(req, res) {
    
        const prompt =
            ChatPromptTemplate.from
Template(`Answer the following question based only on the provided context:
    <context>
    {context}
    </context>
 
   
    Question: {input}`);
    
        // Web context for more accuracy
        const embeddings = getOllamaEmbeding(
)
        const webContextLoader = new CheerioWebBaseLoader('https://docs.smith.langchain.com/user_guide')
        const
 documents = await webContextLoader.load()
        const splitter = new RecursiveCharacterTextSplitter({
            chu
nkSize: 500,
            chunkOverlap: 0
        });
        const splitDocs = await splitter.splitDocuments(documents);

        console.log('Splits count: ', splitDocs.length);
        const vectorstore = await MemoryVectorStore.fromDocume
nts(
            splitDocs,
            embeddings
        );
        const documentChain = await createStuffDocumentsCh
ain({
            llm: HF_MODELS.MISTRAL_LOCAL,
            outputParser: new StringOutputParser(),
            prompt,

        });
        const retriever = vectorstore.asRetriever();
        const retrievalChain = await createRetrievalCha
in({
            combineDocsChain: documentChain,
            retriever,
        });
        const response = await retr
ievalChain.invoke({
            // context: '',
            input: 'What is Langchain?',
        });
        console.log
(response)
        res.json(response);
    }

Imports:

    const { ChatPromptTemplate } = require('@langchain/core/prom
pts')
    const { StringOutputParser } = require('@langchain/core/output_parsers')
    
    const { CheerioWebBaseLoader
 } = require('langchain/document_loaders/web/cheerio');
    const { RecursiveCharacterTextSplitter } = require('langchai
n/text_splitter')
    const { MemoryVectorStore } = require('langchain/vectorstores/memory')
    const { createStuffDocu
mentsChain } = require('langchain/chains/combine_documents');
    const { createRetrievalChain } = require('langchain/ch
ains/retrieval');
    
    const { getOllamaEmbeding, getOllamaChatEmbeding } = require('../services/embedings/ollama');

    const { HF_MODELS } = require('../services/constants');
    require('cheerio')

Embeding:

    function getOllamaEm
beding(model = HF_MODELS.MISTRAL_LOCAL) {
        return new OllamaEmbeddings({
            model: model,
            ma
xConcurrency: 5,
        });
    }

I am running mistral model locally with Ollama.

Up to `Splits count` console, it wo
rks just fine. I am not sure what I am doing wrong here.

Thanks for any help :)
```
---

     
 
all -  [ Roast my resume ](https://i.redd.it/7wyjyuri1mrc1.jpeg) , 2024-04-02-0910
```
any advice would help me a lot . 
```
---

     
 
all -  [ Is langchain overhyped?  ](https://www.reddit.com/r/LocalLLaMA/comments/1bs05x7/is_langchain_overhyped/) , 2024-04-02-0910
```
What do you think about langchain? It has way tooo many integrations, way too much boilerplate code, and way too many th
ings that you probably never gonna use. And, most importantly it doesn't feel developer-friendly.

Compared to other age
nt frameworks sometimes it becomes annoying to work with langchain.

What are your opinions?

```
---

     
 
all -  [ Any ways to count token usage for models not by OpenAI? ](https://www.reddit.com/r/LangChain/comments/1brw18c/any_ways_to_count_token_usage_for_models_not_by/) , 2024-04-02-0910
```
Trying to use non-OpenAI models, but it seems like there's no equivalent to the get\_openai\_callback() function for oth
er models, but the docs say it's only usable for OpenAI.
```
---

     
 
all -  [ What are your views on pathways latest work on RAG ](https://www.reddit.com/r/LangChain/comments/1bromlx/what_are_your_views_on_pathways_latest_work_on_rag/) , 2024-04-02-0910
```
Just stumbled upon this fascinating technique shared Pathway on dynamically adapting the number of documents in a top-k 
retriever RAG prompt using LLM feedback. The method boasts a remarkable 4x cost reduction in RAG LLM question answering 
while upholding accuracy levels. 
```
---

     
 
all -  [ What are the best prompting techniques? ](https://www.reddit.com/r/LangChain/comments/1brn23l/what_are_the_best_prompting_techniques/) , 2024-04-02-0910
```
Hey everyone, curious to know what are the best prompting techniques that you use with Langchain?
```
---

     
 
all -  [ Observability & testing of OpenAI's Assistants API ](https://docs.parea.ai/observability/openai_assistants_api) , 2024-04-02-0910
```

```
---

     
 
all -  [ AttributeError: module langchain has no attribute verbose ](https://www.reddit.com/gallery/1brhyzc) , 2024-04-02-0910
```
Hi everyone, urgent help required. I’ve been trying to install langchain in my computer for my major project since a ver
y long time but everytime it gave one error or the other so I gave up but as the deadline is approaching I seriously sta
rted doing it. 
But every single time I try to install it it shows the same error or it shows circular import errror. Pl
ease help me out
```
---

     
 
all -  [ What are u building these days? Are people using it? Please share  ](https://www.reddit.com/r/LangChain/comments/1brhmsa/what_are_u_building_these_days_are_people_using/) , 2024-04-02-0910
```
Hi folks, skimming through reddit, I can see so many devs are building RAG use cases these days. I'd love to see any use
ful use cases.

In my case, I built an app a while ago that sells digital vouchers through an LLM based chat with paymen
t built in. I decided later to shut down and focus on building a python framework for publishing AI apps very fast acros
s many channels and with any LLM. 
```
---

     
 
all -  [ Langchain Basics Explained! ](https://youtu.be/MBi_lE4tFZQ) , 2024-04-02-0910
```


🎥 New YouTube Tutorial Alert! 🚀

🔥 Title: Langchain Basics Explained!

👨‍💻 Description:
Hey everyone! In today's tutor
ial, we're diving into the fascinating world of #LangChain. Whether you're new to the concept or looking to deepen your 
understanding, this video is for you!

🔍 What We'll Cover:

Embeddings: Understanding the basics
Chunkings in Langchain:
 A detailed walkthrough
Vector Store: Exploring its role in Langchain
Retriever: How to leverage it effectively
RAG Appl
ication: Practical examples and demos
🚀 About LangChain:
LangChain is an open-source orchestration framework designed fo
r developing applications using large language models (LLMs). With Python- and Javascript-based libraries, LangChain's t
ools and APIs simplify the process of building LLM-driven applications like chatbots and virtual agents.

🎯 Who Is This 
For?
This tutorial is perfect for developers, data scientists, and anyone interested in learning about LangChain and its
 applications.

Let's unlock the power of LangChain together! 🚀💬
```
---

     
 
all -  [ Is it worth dedicating time to learn Langchain with the constant influx of new AI frameworks? ](https://www.reddit.com/r/LangChain/comments/1brew3a/is_it_worth_dedicating_time_to_learn_langchain/) , 2024-04-02-0910
```
Hello,  

I've recently started diving into Langchain and find myself devoting more and more time to it. While I'm inter
ested in various aspects of Langchain, I can't help but notice that there seems to be a new AI Agent repo or framework p
opping up almost every day, especially in the realm of Agents.

With so much hype surrounding every new AI-related frame
work or library, I'm finding it challenging to focus on specializing in Langchain. It's hard not to get distracted by th
e constant barrage of shiny new tools and technologies.

I wanted to reach out to the community and get your thoughts on
 this. Is it worth dedicating a significant amount of time to learning Langchain, given the rapid pace of development in
 the AI field? How do you stay focused and avoid getting sidetracked by the latest and greatest frameworks?

I'm genuine
ly interested in Langchain and believe it has a lot to offer, but I also want to make sure I'm investing my time wisely.
 Any insights or advice from those who have been working with Langchain for a while would be greatly appreciated.
```
---

     
 
all -  [ Forgetful AI DMs and technology behind gtRPGs ](https://www.reddit.com/r/gtrpg/comments/1brem81/forgetful_ai_dms_and_technology_behind_gtrpgs/) , 2024-04-02-0910
```
The first experience playing with AI as a DM is exhilarating. It works and paints an excellent short story around the ch
aracter. But once you get hooked and want to explore your world further, you hit the limit of the context window (even w
ith the recently released Claude Opus, it is just 200Kb), and the experience degrades: AI may forget the most basic info
rmation about your character and the world.

This amnesia and lack of an overarching story are probably the main reasons
 why we are working hard to integrate AI with the game state. Doing this well is at the core of our gtRPGs.

I'm still a
t the very beginning of my design process, and I want to learn from people who have done it before. How do you approach 
it? Is it Retrieval-Augmented Generation? Summarisation memory? Did you have a good experience with tools like Langchain
? Did you end up writing it all from scratch?
```
---

     
 
all -  [ Deploying RAG with SciPhi: A Quick Demo ](https://www.reddit.com/r/LLMDevs/comments/1brbrq8/deploying_rag_with_sciphi_a_quick_demo/) , 2024-04-02-0910
```
Hi, [r/LLMDevs](https://www.reddit.com/r/LLMDevs/)!

I've been building [R2R](https://github.com/SciPhi-AI/R2R), a frame
work for rapid development and deployment of RAG pipelines.

Here is a quick video showing how you can launch a basic RA
G pipeline in 1 minute, using the cloud platform we are building to pair with R2R. These pipelines are fully customizabl
e, and you can readily add custom logic from LangChain or LlamaIndex or elsewhere into the template logic.

Please take 
a look, deploy a pipeline and then let us know what features you most want added!

[A quick video on SciPhi + R2R](https
://reddit.com/link/1brbrq8/video/cilyx97n7frc1/player)

&#x200B;
```
---

     
 
MachineLearning -  [ [D] : Scale PDF Q&A App to 10K Users with GPUs – <$250/Mo ](https://www.reddit.com/r/MachineLearning/comments/1b6jv56/d_scale_pdf_qa_app_to_10k_users_with_gpus_250mo/) , 2024-04-02-0910
```
Hello everyone,

Check out this step-by-step detailed tutorial on building and scaling a PDF Q&A Application using Pinec
one, Langchain and Inferless

&#x200B;

[Architecture](https://preview.redd.it/zfta52cbddmc1.png?width=1301&format=png&a
uto=webp&s=440399212d3feb03e861759a31602e2cde0dc7fb)

Alongside, the detailed quick deploy guide, it also includes cost 
analysis on how you can save upto 84% cost with an example of processing 3000 documents and nearly 10,000 queries every 
month, all while dramatically cutting your costs from $1800 ( AWS) to just $250 a month on Inferless.

Here is the tutor
ial - [https://cookbook.inferless.com/](https://cookbook.inferless.com/)

If you resonate, join the discussion on Hacker
news here - [https://news.ycombinator.com/item?id=39594588](https://news.ycombinator.com/item?id=39594588)
```
---

     
 
MachineLearning -  [ [D] What Is Your LLM Tech Stack in Production? ](https://www.reddit.com/r/MachineLearning/comments/1b4sdru/d_what_is_your_llm_tech_stack_in_production/) , 2024-04-02-0910
```
Curious what everybody is using to implement LLM powered apps for production usage and your experience with these toolin
gs and advice. 

This is what I am using for some RAG prototypes I have been building for users in finance and capital m
arkets.

**Pre-processing\ETL:**
Unstructured.io + Spark, Airflow

**Embedding model:**
Cohere Embed v3
Previously using
 OpenAI Ada but Cohere has significantly better retrieval recall and precision for my use case. Also exploring other ope
n weights embedding models

**Vector Database:**
Elasticsearch previously but now using Pinecone

**LLM:**
Gone through 
quite a few including hosted and self-hosted options. Went with gpt4 early during prototyping then switched to gpt3.5-tu
rbo for more manageable costs and eventually open weights models. 

Now using a fine-tuned Llama2 70B model self hosted 
with vLLM 

**LLM Framework:**
Started with Langchain initially but found it cumbersome to extend as the app became more
 complex. Tried implementing it in LlamaIndex at some point just to learn and found it just as bad. Went back to Langcha
in and now I am in the midst of replacing it with my own logic

What is everyone else using?

Edit: correct model Llama2
 70B
```
---

     
 
deeplearning -  [ Tengyu Ma on Voyage AI - Weaviate Podcast #91! ](https://www.reddit.com/r/deeplearning/comments/1bjft8i/tengyu_ma_on_voyage_ai_weaviate_podcast_91/) , 2024-04-02-0910
```
**Voyage AI** is the newest giant in the embedding, reranking, and search model game!

I am SUPER excited to publish our
 latest Weaviate podcast with Tengyu Ma, Co-Founder of Voyage AI and Assistant Professor at Stanford University!

We beg
an the podcast with a deep dive into everything embedding model training and contrastive learning theory. Tengyu deliver
ed a **masterclass** in everything from scaling laws to multi-vector representations, neural architectures, representati
on collapse, data augmentation, semantic similarity, and more! I am beyond impressed with Tengyu's extensive knowledge a
nd explanations of all these topics.

The next chapter dives into a case study Voyage AI did **fine-tuning an embedding 
model for the LangChain documentation.** This is an absolutely fascinating example of the role of continual fine-tuning 
with very new concepts (for example, very few people were talking about chaining together LLM calls 2 years ago), as wel
l as the data efficiency advances in fine-tuning.

We concluded by discussing ML systems challenges in serving an embedd
ings API. Particularly the challenge of detecting if a request is for batch or query inference and the optimizations tha
t go into either say \~100ms latency for a query embedding or maximizing throughput for batch embeddings.

I hope you fi
nd the podcast interesting, more than happy to discuss any of these topics with you or answer any questions about the co
ntent in the podcast! Thank you so much!

YouTube: [https://www.youtube.com/watch?v=xPdyivfheqI](https://www.youtube.com
/watch?v=xPdyivfheqI)

Spotify: [https://spotifyanchor-web.app.link/e/u6XPLYfF7Hb](https://spotifyanchor-web.app.link/e/
u6XPLYfF7Hb)
```
---

     
