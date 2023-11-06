 
all -  [ Difference between Memory and {agent_scratchpad}? ](https://www.reddit.com/r/LangChain/comments/17on184/difference_between_memory_and_agent_scratchpad/) , 2023-11-06-0910
```
I don’t understand exactly how Memory works in Agents. Also, how is it different from {agent_scratchpad} appended to the
 prompts?
```
---

     
 
all -  [ Locally serving an LLM for chat task for family access? ](https://www.reddit.com/r/LocalLLaMA/comments/17ojvdw/locally_serving_an_llm_for_chat_task_for_family/) , 2023-11-06-0910
```
Hey, 

Just wondering if anyone is serving an open source LLM for chat, that is made available on your home network. 

L
ooking to do such, from homelab running proxmox. Did you dev your own UI with something like Streamlit, using LangChain 
or vanilla Python? A clean simple UI already available?

Thanks for any insight
```
---

     
 
all -  [ feed pdf files into an LLM for question answering tasks ](https://www.reddit.com/r/LocalLLaMA/comments/17oj372/feed_pdf_files_into_an_llm_for_question_answering/) , 2023-11-06-0910
```
hello there, we are working on chatbot that will act as an assistant for new cancer patients , we scraped around 50 pdfs
 containing faq with their answers, now we have no idea whats the best approach to make this model , one of the teamates
 suggested to use langchain , is it a good framework? can it implement other llms other than gpts ? 

also jsut to menti
on , we thought about fine tunning some model but we're rejecting this idea due to time nd computation limitations , so 
whats the best approach should we follow?
```
---

     
 
all -  [ Add a LangChain chatbot to my personal website? ](https://www.reddit.com/r/LangChain/comments/17oiz0i/add_a_langchain_chatbot_to_my_personal_website/) , 2023-11-06-0910
```
I have a website, [myname.com](https://myname.com), built using GitHub Pages and my personal url. I want to add a chatbo
t to it, using LangChain so I can augment the chatbot with a research paper I wrote. Is there a way I can do this using 
LangChain in python?
```
---

     
 
all -  [ Open Sourcing Llmtuner - An Experimental Framework for Finetuning Large Models Like Whisper and Llam ](https://www.reddit.com/r/LangChain/comments/17o9370/open_sourcing_llmtuner_an_experimental_framework/) , 2023-11-06-0910
```
Hi Folks,

Happy to share an open source side project I've been working on - [LLmtuner](https://github.com/promptslab/LL
Mtuner). It's a framework for finetuning large models like Whisper, Llama, Llama-2, etc with best practices like LoRA, Q
LoRA, through a sleek, scikit-learn-inspired interface.

As someone who works with Large Models a lot, I found myself wr
iting a lot of boilerplate code every time I wanted to finetune a model. Llmtuner aims to simplify the finetuning proces
s down to just 2-3 lines to get training started, similar to scikit-learn.  


https://preview.redd.it/ps26by2waiyb1.png
?width=1502&format=png&auto=webp&s=7b851ef022dcfada395f5a37ade70faf432355c9

&#x200B;

🚀 Features:

* 🧙‍♀️ Finetune stat
e-of-the-art LLMs like **Whisper, Llama wit**h minimal code
* 🔨 Built-in utilities for techniques like **LoRA and QLoRA*
*
* ✌ **Launch webapp demos** for your finetuned models with one click
* 💥 **Fast inference** without separate code
* **
🌐 Easy model sharing** and deployment coming soon

This is still experimental code I've been using for personal projects
. I thought others might find it useful too so decided to open-source it.

* Github : [https://github.com/promptslab/LLM
tuner](https://github.com/promptslab/LLMtuner)
* For quick demo : [Colab](https://colab.research.google.com/drive/1ia9Kv
qEGOxARtJScPBY6ccF8l41-w_l5?usp=sharing)

Contributions and feedback are very welcome! I hope it will be helpful in your
 research & projects. Have a good weekend, Thanks :)
```
---

     
 
all -  [ Is AutoGen the right tool for my use case? ](https://www.reddit.com/r/AutoGenAI/comments/17o5np5/is_autogen_the_right_tool_for_my_use_case/) , 2023-11-06-0910
```
I want to build a retrieval-augmented LLM app that uses a private knowledge base. I was experimenting with Langchain but
 then I found Autogen which I thought may be more suitable for my needs.  


What I want is basically an advanced custom
er chatbot that can analyze customer data and provide charts, inform the customer about my services, and call external A
PIs for additional functionality. So I thought maybe I could achieve that by having one agent that specializes in analyz
ing CSV data, one agent that specializes in consuming PDF documents for informing the user, etc., and orchestrating thes
e agents with Autogen. Basically, the app would find what agent is the best for a specific task the user needs and call 
it.  


But I want all the intermediary communication between the agents to be hidden from the user. The user should onl
y receive the final output and the experience should basically be like using ChatGPT.  


Would Autogen be the right too
l for this kind of task?
```
---

     
 
all -  [ Doubts on inference on large dataset ](https://www.reddit.com/r/LangChain/comments/17nw8zd/doubts_on_inference_on_large_dataset/) , 2023-11-06-0910
```
I created a big dataset of abstracts. I will use each abstract for a prompt template. My idea is to generate a pertinent
 question to each abstract. I am using the chain.apply method at the moment but this is sequential. I am sure there is a
 way to parallelize this process but it seems like I cannot come out with an idea nor find anything online. Can someone 
help me?
```
---

     
 
all -  [ Question about embeddings and vectordatabase ](https://www.reddit.com/r/LocalLLaMA/comments/17nw3dq/question_about_embeddings_and_vectordatabase/) , 2023-11-06-0910
```
So I have been trying to gather all the pieces needed to build a customer support chatbot with Llama2-13b-chat. As far a
s I understand it a vector database would be good for the information retrieval. 

Now my questions is: 
Let's say I use
 pgvector extension in a PostgreSQL database and make a vector database. 
Do I need to use something additional to do th
e embeddings ? 
Is pgvector with LangChain and then 'connecting' it to the LM enough?
Is it also viable to use pgvector 
with the Faiss library to create those embeddings? 

Or would another library/service make more sense?
 I am at a little
 bit of a loss here. 

Thank you very much for your help!
```
---

     
 
all -  [ I'm finding it hard to disable cache in NextJS13 ](https://www.reddit.com/r/nextjs/comments/17nvaci/im_finding_it_hard_to_disable_cache_in_nextjs13/) , 2023-11-06-0910
```
Nextjs13 is all good. But, it is caching fetch requests made in langchain/chromadb library, which gets annoying pretty q
uickly

&#x200B;

[requests made by library is cached](https://preview.redd.it/sq6fjnwj9eyb1.png?width=730&format=png&au
to=webp&s=6f9ff643c0e6e3ab786d422aab8fbbdab07b1ff8)

I added this on the page.tsx, where the request is made:

export co
nst dynamic = 'force-dynamic';

&#x200B;

But it doesn't work. 

Flow: The page(server component) has a client-component
 button(calls a server action).

The server action has some action with chromadb (vectorstore)
```
---

     
 
all -  [ Need to use langchain with llm hosted in private cloud as REST API ](https://www.reddit.com/r/LangChain/comments/17nsl5r/need_to_use_langchain_with_llm_hosted_in_private/) , 2023-11-06-0910
```
Guys, using langchain for a RAG application and I have an opensource llm downloaded and deployed as a rest API service t
o which I can send requests and receive response. How can I set llm to this api url like below:

llm = TogetherLLM(
    
model= 'togethercomputer/llama-2-7b-chat',
    temperature = 0.1,
    max_tokens = 1024
)
```
---

     
 
all -  [ Help with understanding use of LangChain in report generation ](https://www.reddit.com/r/LangChain/comments/17nqhya/help_with_understanding_use_of_langchain_in/) , 2023-11-06-0910
```
Hey y'all 👋

I wanted to ask about the implementation of an idea I have - I feel like it's straightforward, but I haven'
t had any luck in my research online and now feel more confused than ever on LLMs. 

I want to create an chatbot that, g
iven good samples of reports and the requirements for a new report, can write out the draft of a new report. I would lik
e to create a knowledge base that includes expert knowledge that would be helpful to writing the reports. I will instant
iate a local instance of an LLM and probably connect it to a frontend using Streamlit. 

I  imagine I need to use some f
orm of either LangChain or LlamaIndex to implement RAG, but I am not sure if it's finetuning or RAG at this point. I am 
lost on how to even approach this problem - I have read tons of articles and documentation, but feel lost. If anyone can
 provide any ideas or things I can research to learn this, that'd be awesome. 

Thanks in advance!
```
---

     
 
all -  [ Made a library for managing OpenAI rate limits which use actual OpenAI headers unlike pre-configured ](https://www.reddit.com/r/LangChain/comments/17npapw/made_a_library_for_managing_openai_rate_limits/) , 2023-11-06-0910
```
You can see code here: [https://github.com/alex4321/langchain-openai-limiter](https://github.com/alex4321/langchain-open
ai-limiter)

Library itself: [https://pypi.org/project/langchain-openai-limiter/](https://pypi.org/project/langchain-ope
nai-limiter/)

Motivation:

1. Default OpenAI python client (and langchain on top of it) does not deal with rate limits 
in any specific way - it just hit the error and retry. This way it consume budget and limits by every case then it hit e
rror.
2. All the rest of what I found was about having pre-configured PRM/TPM and some \`aiolimiter\`-like stuff inside.
 Much better approach - but the problem is that OpenAI have very different tiers for different users. Like by default gp
t-4 RPM is like 100 and TPM is like 10 000, but when you spent more during development of your project - it becomes like
 150 000 TPM (in my personal account). Surely we can change config and restart app or so...
3. But why should we do it w
hen OpenAI provides headers like 'well, you made this request, your initial TPM is X, after processing it - your current
 TPM is X1, your initial RPM is Y, your current RPM is Y1, TPM and RPM will reset in Z seconds' or so? So instead of pre
configured limits and counting on our side we can always have info about actual limits.
4. The problem is, however, that
 python OpenAI client do not provide obvious way to make callbacks accessing headers, and do not provide this info in th
e response itself. So neither it nor libraries on top of that don't use this headers limit - as well as most libraries w
hich do attempts to deal with limits, as far as I can see.

Implementation:

So basically my library consists of three c
omponents:

1. Hook system which inject itself inside openai. More or less clean for sync case - just use OpenAI's ready
 interface to attach post-response hook to http session. A bit greasy in async case - here it decorate openai's library 
insides (yet public) to attach the same logic.
   1. So after every OpenAI request it will know something like 'for this
 API key and model pair the remaining limit is X and will be resetter after Y timeout'
2. Wrappers on top of ChatOpenAI 
/ OpenAIEmbeddings which, before running request - calculate required token count, await for RPM & TPM limit to be avail
able and only after that do factual requests.
3. I also have wrappers which can consume multiple API keys and, before re
questing the underlying model - check which one of them have sufficient resources (so here I do random choice between th
e ones which have resources, or otherwise - wait for resource to be free).
```
---

     
 
all -  [ Where to find projects related to LangChain? ](https://www.reddit.com/r/LangChain/comments/17no1gf/where_to_find_projects_related_to_langchain/) , 2023-11-06-0910
```
I work for a development company from India, recently I have got a task to find projects related to LangChain as it has 
less competition. Where can I find some projects other than upwork and clutch?
```
---

     
 
all -  [ Langchain vs Llamaindex ](https://www.reddit.com/r/LangChain/comments/17nnclu/langchain_vs_llamaindex/) , 2023-11-06-0910
```
I saw Langchain has launched templates and llamaindex has been pushing out lots of use case templates and repos. As of e
arly Nov, what do you think is the sweet spots of use for langchain vs llamaindex? I used to work on the business side i
n financial services (not banks or insurance) and I see a lot of use cases for RAG (most) and agents (some). But I am a 
beginner on tech and find myself not sure where to spend my time learning. What do you think is the sweetspot for one vs
 another when it comes to the types of application, or cost and efficiency? What are the weaknesses as of early November
? I know things can change a month from now. Thank you.
```
---

     
 
all -  [ AutoGen v0.2.0b1 released ](https://www.reddit.com/r/AutoGenAI/comments/17nmnf9/autogen_v020b1_released/) , 2023-11-06-0910
```
[New release: v0.2.0b1](https://github.com/microsoft/autogen/releases/tag/v0.2.0b1) 

This is a beta release of v0.2.0.


## Highlights

* Switching to openai v1. Please read the [migration guide](https://microsoft.github.io/autogen/docs/Ins
tallation/#migration-guide-to-v02) and report bugs.
* Support async function execution & get\_human\_input.
* Improvemen
ts in documentation and notebooks.

Thanks to all the reviewers for the v0.2 migration. Thanks to [@aayushchhabra1999](h
ttps://github.com/aayushchhabra1999) [@bonadio](https://github.com/bonadio) [@marcgreen](https://github.com/marcgreen) a
nd other contributors!  
 

## What's Changed

* Update Installation.md by [@gagb](https://github.com/gagb) in [#456](ht
tps://github.com/microsoft/autogen/pull/456)
* Update FAQ with workaround for Issue [#251](https://github.com/microsoft/
autogen/issues/251) by [@marcgreen](https://github.com/marcgreen) in [#405](https://github.com/microsoft/autogen/pull/40
5)
* Fix typo in README.md by [@eltociear](https://github.com/eltociear) in [#481](https://github.com/microsoft/autogen/
pull/481)
* Fix/async function and tool execution by [@aayushchhabra1999](https://github.com/aayushchhabra1999) in [#87]
(https://github.com/microsoft/autogen/pull/87)
* Adding async support to get\_human\_input by [@bonadio](https://github.
com/bonadio) in [#466](https://github.com/microsoft/autogen/pull/466)
* Added example .txt file for agentchat\_langchain
 sample notebook by [@jasondotparse](https://github.com/jasondotparse) in [#373](https://github.com/microsoft/autogen/pu
ll/373)
* Fix : Typo by [@AaadityaG](https://github.com/AaadityaG) in [#506](https://github.com/microsoft/autogen/pull/5
06)
* Dev/v0.2 by [@sonichi](https://github.com/sonichi) in [#393](https://github.com/microsoft/autogen/pull/393)

## Ne
w Contributors

* [@marcgreen](https://github.com/marcgreen) made their first contribution in [#405](https://github.com/
microsoft/autogen/pull/405)
* [@aayushchhabra1999](https://github.com/aayushchhabra1999) made their first contribution i
n [#87](https://github.com/microsoft/autogen/pull/87)
* [@bonadio](https://github.com/bonadio) made their first contribu
tion in [#466](https://github.com/microsoft/autogen/pull/466)
* [@jasondotparse](https://github.com/jasondotparse) made 
their first contribution in [#373](https://github.com/microsoft/autogen/pull/373)
* [@AaadityaG](https://github.com/Aaad
ityaG) made their first contribution in [#506](https://github.com/microsoft/autogen/pull/506)

**Full Changelog**: [v0.1
.14...v0.2.0b1](https://github.com/microsoft/autogen/compare/v0.1.14...v0.2.0b1)

 
```
---

     
 
all -  [ Rush of learning everything.. ](https://www.reddit.com/r/developersIndia/comments/17nixsy/rush_of_learning_everything/) , 2023-11-06-0910
```
I am a second year cse guy, I like programming it doesn't feel like a chore to me.
But one thing that I struggle a lot w
ith the whole tech thing is that there is so much to learn and I get overwhelmed by the things to learn and keep hopping
 from one thing to another.
One day I want to learn react, the other day I feel like I want to work with ml and Langchai
ns and the next day I think I want to build some microservices for the cloud and the list goes on.
I am struggling from 
this for the past 4-5 months and I barely made any progress in tech, I feel struck and I think I barely got any time lef
t for all this pls help me guys 🙏
```
---

     
 
all -  [ Development with Large Language Models Tutorial – OpenAI, Langchain, Agents, Chroma | freeCodeCamp.o ](https://www.youtube.com/watch?v=xZDB1naRUlk) , 2023-11-06-0910
```

```
---

     
 
all -  [ Noob here. Help! ](https://www.reddit.com/r/LangChain/comments/17n8cjz/noob_here_help/) , 2023-11-06-0910
```
I manage a small engineering team.  We manage large amounts of text based data and serve it to our consumers via apis an
d real time feeds.   

Our business team made a demo combining some of our data with langchain and came away with a demo
 that shows a chat bot type experience analytic product.   They claim the engineering team is dumb because they didn’t k
now about langchain and were skeptical.  The business team think we need to build a new business around the combination 
of all our data and langchain and believe it is super easy.    

I did like the demo but also know it is not something t
hat anyone would pay for and was made on a tiny set of our data. 

Question:   What should we be worried about when we s
tart to scope this project more deeply?   Remember we have massive and constantly updating real time data, is scaling an
 issue?   How should we approach this?   

Thanks internet strangers.
```
---

     
 
all -  [ Function Calling Delay ](https://www.reddit.com/r/LangChain/comments/17n3ztt/function_calling_delay/) , 2023-11-06-0910
```
So, I have been running some experiments with OpenAI's Function Calling capability and Langchain Agents, and I've recent
ly tried to implement streaming the function calling with \`on\_llm\_new\_token\` and I've noticed a weird behavior. It 
looks like between the first call of \`on\_llm\_start\` and the first time that \`on\_llm\_new\_token\` is called, there
 is a huge delay (\~10s). Then, the entire output suddenly streams out extremely quickly (last token comes out within \~
2s). Has anyone experienced this with Langchain or OpenAI function calling streaming?
```
---

     
 
all -  [ Langchain needs to be rewritten ](https://www.reddit.com/r/LangChain/comments/17n34y9/langchain_needs_to_be_rewritten/) , 2023-11-06-0910
```
I hope the team will take into consideration the idea of refactoring the codebase. There is a significant amount of over
lap, and it appears that some parts of the code are overly engineered and complex but not necessary.

\---------

Edit:


I really appreciate Langchain and it's my go-to choice, but extending and customizing it for different use cases is qui
te challenging. Nonetheless, a big shoutout to the Langchain community for creating such a great tool.
```
---

     
 
all -  [ Any job boards or similar where people are hiring langchain devs? ](https://www.reddit.com/r/LangChain/comments/17n3268/any_job_boards_or_similar_where_people_are_hiring/) , 2023-11-06-0910
```
Pretty much the title, I've been falling in love with langchain, built a ton of stuff, agents, custom agents, tools, cus
tom tools, wrapper for some classes, retrievers, chat bots, embeddings, vectorial dbs and would love to get a job doing 
this tuff, any pace where I can find this kind of jobs?
```
---

     
 
all -  [ Is there a way to make plots using langchain? ](https://www.reddit.com/r/LangChain/comments/17n1kdg/is_there_a_way_to_make_plots_using_langchain/) , 2023-11-06-0910
```
I’ve been looking at the pandas agent and making queries at a table imported from snowflake. I’m using streamlit for a f
rontend. How can I make a plot? I tried using the agent to make the plot but I always get an output parser error because
 it can only return a json. There are ways to make the output return a formatted json using a modified prompt, but it se
ems to contain wrong data. Do you have a way to make reliable plots from prompting a table?
```
---

     
 
all -  [ Confusion over how to use Llama to generate reports ](https://www.reddit.com/r/LocalLLaMA/comments/17n19kf/confusion_over_how_to_use_llama_to_generate/) , 2023-11-06-0910
```
Hey y'all,

I wanted to ask about implementation of an idea I have - I feel like it's straightforward, but I haven't had
 any luck in my research and now feel more confused than ever on LLMs. 

I want to create an chatbot that, given good sa
mples of reports and the requirements for a new report, can write out the draft of a report. I would like to create a kn
owledge base that includes expert knowledge that would be helpful to writing the reports. I will instantiate a local ins
tance of Llama2 and probably connect it to a frontend using Streamlit. 

I  imagine I need to use some form of either La
ngChain or LlamaIndex to implement RAG, but I am not sure if it's finetuning or RAG at this point. I am lost on how to e
ven approach this problem - I have read tons of articles and documentation, but feel lost. If anyone can provide any ide
as or things I can research to learn this, that'd be awesome. 

Thanks in advance!
```
---

     
 
all -  [ Not able to connect through Azure APIM ](https://www.reddit.com/r/LangChain/comments/17mzucs/not_able_to_connect_through_azure_apim/) , 2023-11-06-0910
```
I want to connect to a GPT4 API through an Azure API Management gateway but I get an issue. I'm trying to connect using 
this code that I found online but I still get no result:  

    llm = AzureOpenAI(         headers={'Ocp-Apim-Subscripti
on-Key': os.environ['OPENAI_API_KEY']},         openai_api_base=APIM_BASE_URL,         model_name=COMPLETION_MODEL,     
    deployment_name=COMPLETION_DEPLOYMENT,         max_tokens=SUMMARY_MAX_TOKENS,         temperature=SUMMARY_TEMPERATUR
E     )

Do you have any idea why it doesn't work ?
```
---

     
 
all -  [ AI — weekly megathread! ](https://www.reddit.com/r/artificial/comments/17mzpm6/ai_weekly_megathread/) , 2023-11-06-0910
```
 **News** provided by [aibrews.com](https://aibrews.com/)

 

1. **Luma AI** introduced ***Genie***, a generative 3D fou
ndation model in research preview. *It’s free during research preview via Discord* \[[*Details*](https://lumalabs.ai/gen
ie)\].
2. **Nous** **Research** released ***Obsidian***, the world's first 3B multi-modal model family pre-trained for 4
 Trillion tokens that runs locally on iPhones. Obsidian competes in benchmarks withWizardLM-13B and GPT4-X-Vicuna 13B an
d is based on CapybaraV1.9 \[[*Details*](https://huggingface.co/NousResearch)\].
3. **Phind** has released a new model *
**Phind Model V7*** that matches and exceeds GPT-4's coding abilities while running 5x faster and having16k context \[[*
Details*](https://www.phind.com/blog/phind-model-beats-gpt4-fast)\].
4. **Runway** released an update for both text to v
ideo and image to video generation with Gen-2, bringing major improvements to both the fidelity and consistency of video
 results \[[*Link*](https://runwayml.com/)\].
5. **Stability AI** announced \[[*Details*](https://stability.ai/blog/stab
ility-ai-enhanced-image-apis-for-business-features)\]:
   1. ***Stable 3D*** (Private Preview): a tool to generate a dra
ft-quality 3D model in minutes, by selecting an image or illustration, or writing a text prompt.
   2. [***Sky Replacer*
**](https://clipdrop.co/real-estate/sky-replacer)***:*** a tool that allows users to replace the color and aesthetic of 
the sky in their original photos with a selection of nine alternatives.
   3. integration of Content Credentials and ***
invisible watermarking*** for images generated via the Stability AI API. 
   4. Stable FineTuning (Private Preview)
6. *
*Hugging Face** released ***Zephyr-7B-β***, a fine-tuned version of Mistral-7B that achieves results similar to Chat Lla
ma 70B in multiple benchmarks and above results in MT bench \[[Details](https://huggingface.co/HuggingFaceH4/zephyr-7b-b
eta) | [*Demo*](https://huggingfaceh4-zephyr-chat.hf.space/)\].
7. **LangChain** launched ***LangChain Templates*** \- a
 collection of easily deployable reference architectures for a wide variety of popular LLM use cases \[[*Details*](https
://github.com/langchain-ai/langchain/tree/master/templates)\].
8. **Nvidia** unveiled ***ChipNeMo***, a specialized 43 b
illion parameter large language model for chip design that can answer general questions related to chip design and write
 short scripts to interface with CAD tools \[[*Details*](https://www.tomshardware.com/news/nvidias-chipnemo-ai-will-help
-design-chips)\].
9. **Together** released ***RedPajama-Data-v2***: an Open dataset with 30 Trillion tokens for training
 Large Language Models. It’s the largest public dataset released specifically for LLM training \[[*Details*](https://tog
ether.ai/blog/redpajama-data-v2)\].
10. **Hugging Face** released ***Distil-Whisper***, a distilled version of Whisper t
hat is 6 times faster, 49% smaller, and performs within 1% word error rate (WER) on out-of-distribution evaluation sets 
\[[*Details*](https://github.com/huggingface/distil-whisper)\].
11. **Google Research** and **Google DeepMind** present 
***MetNet-3***, the first AI weather model to learn from sparse observations and outperform the top operational systems 
up to 24 hours ahead at high resolutions. Google has integrated MetNet-3’s capabilities across its various products \[[*
Details*](https://blog.research.google/2023/11/metnet-3-state-of-art-neural-weather.html)\].
12. **Google DeepMind** and
 **Isomorphic Labs** update on the next generation of ***AlphaFold***: the new model greatly expands coverage of structu
re prediction beyond proteins to other key biomolecular classes. This paves the way for researchers to find novel protei
ns to eventually map biomolecular structures needed to design better drugs \[[*Details*](https://deepmind.google/discove
r/blog/a-glimpse-of-the-next-generation-of-alphafold)\].
13. **Nolano Research** and **EleutherAI** introduced ***Hi-NOL
IN***, first state-of-the-art open-source English-Hindi bilingual model built upon the Pythia model suite \[[*Details*](
https://blog.nolano.ai/Hi-NOLIN/)\].
14. **Google** is rolling out ***Immersive View for Routes*** in 15 cities, startin
g this week along with other AI-powered features in Maps. Immersive view combines Street view, aerial imagery, and live 
information like weather and traffic to give an aerial, photo-realistic preview of your planned Google Maps route \[[*De
tails*](https://www.techradar.com/computing/software/google-maps-gets-a-big-ai-update-here-are-the-5-best-time-saving-fe
atures)\].
15. **Perplexity** announced two new models **pplx-7b-chat** and **pplx-70b-chat**, built on top of open-sour
ce LLMs and fine-tuned for chat. They are available as an alpha release, via Labs and pplx-api \[[*Labs Link*](https://l
abs.perplexity.ai/)\].
16. **SlashNext's** *2023 State of Phishing Report* reveals a 1,265% increase in Phishing Emails 
since the launch of ChatGPT in november 2022, signaling a new era of cybercrime fueled by Generative AI \[[Details](http
s://finance.yahoo.com/news/slashnexts-2023-state-phishing-report-152000834.html)\].
17. **Google** launches generative A
I tools for product imagery to US advertisers and merchants \[[*Details*](https://techcrunch.com/2023/11/01/google-launc
hes-generative-ai-tools-for-product-imagery-to-u-s-advertisers/)\].

#### 🔦 Weekly Spotlight

1. *Three things to know a
bout the White House’s executive order on AI \[*[*Link*](https://www.technologyreview.com/2023/10/30/1082678/three-thing
s-to-know-about-the-white-houses-executive-order-on-ai/)*\].*
2. Developing a game *Angry Pumpkins* using GPT-4 for all 
the coding and Midjourney / DALLE for the graphics \[[*Link*](https://x.com/javilopen/status/1719363262179938401?s=20)\]
.
3. **Chatd**: a desktop application that lets you use a local large language model (Mistral-7B) to chat with your docu
ments. It comes with the local LLM runner packaged in \[[*Link*](https://github.com/BruceMacD/chatd)\].
4. Teachers in I
ndia help Microsoft Research design AI tool for creating great classroom content \[[Link](https://www.microsoft.com/en-u
s/research/blog/teachers-in-india-help-microsoft-research-design-ai-tool-for-creating-great-classroom-content)\]. 

\- -
 -

Welcome to the r/artificial weekly megathread. This is where you can discuss Artificial Intelligence - talk about ne
w models, recent news, ask questions, make predictions, and chat other related topics.

[Click here for discussion start
ers for this thread or for a separate post.](https://www.google.com/search?q=artificial+intelligence&tbm=nws)

Self-prom
o is allowed in these weekly discussions. If you want to make a separate post, please read and go by the rules or you wi
ll be banned.

[Previous Megathreads](https://www.reddit.com/r/artificial/search/?q=author%3Ajaketocake%20megathread&res
trict_sr=1) & [Subreddit revamp and going forward](https://www.reddit.com/r/artificial/comments/120qr4r/psa_rule_2_will_
be_enforced_selfpromotion_is_only/)
```
---

     
 
all -  [ Azure Search vs. Pinecone? ](https://www.reddit.com/r/LangChain/comments/17mxe9t/azure_search_vs_pinecone/) , 2023-11-06-0910
```
I have so far been successful in creating RAG pipeline with nice performing conversational bot with Azure Search Index. 
I was asked to try out Pinecone as vector store instead of Azure Search. (Org wants to reduce costs), So i setup a PoC p
ipeline with Pinecone as vector store. What I am not sure is how to benchmark both vector stores for performance and fin
d limitations of both.

Has anyone performed comparative analyses on the performance of Azure Search Index and PineconeD
B? If so, I'd appreciate shared insights.

Also, I am specially interested in:

1. Indexing speed: How do they compare w
hen it comes to indexing speed, especially when dealing with large datasets?
2. Query performance: How do they fare when
 it comes to executing complex queries?
3. Cost efficiency: Any thoughts on cost-effectiveness relative to performance a
nd capacity?
4. Scalability: How smoothly do they scale up with growing needs?
5. Integration: Are there remarkable diff
erences in integrating each with other common platforms and tools?

Naturally, every use case is unique and introduces i
ts own variables. I would love to hear about your experiences, thoughts, or case studies regarding these two platforms' 
performances in different scenarios.

Thank you in advance for your insights!
```
---

     
 
all -  [ Not able to delete Embeddings of a pdf from a list of uploaded Pdf ](https://www.reddit.com/r/LangChain/comments/17mw6aq/not_able_to_delete_embeddings_of_a_pdf_from_a/) , 2023-11-06-0910
```
def delete\_document\_embeddings\_by\_filename(file\_path, persist\_directory):  
chroma\_db = chromadb.PersistentClient
(path=persist\_directory)  
print(chroma\_db)  
collection = chroma\_db.get\_collection(name='langchain')  
print(collec
tion)  
collection.delete(where={'source': file\_path})  
output of the above code is:-  
<chromadb.api.segment.SegmentA
PI object at 0x7f4948165280>  
name='langchain' id=UUID('8a5e8fff-93a4-49f3-8be7-5aac47cb3902') metadata=None  
And I am
 calling like this  
persist\_directory=f'/home/hs/CustomBot/chroma-databases/{formatted\_project\_name}'  
file=/home/h
s/CustomBot/media/project/Code\_of\_Conduct\_Policy.pdf  
delete\_document\_embeddings\_by\_filename(file, persist\_dire
ctory)  
Still not able to delete embeddings of a pdf from the embeddings folder
```
---

     
 
all -  [ DialoGPT + RAG ](https://www.reddit.com/r/huggingface/comments/17mv04p/dialogpt_rag/) , 2023-11-06-0910
```
Has anyone tried using langchain to apply RAG on DialoGPT? I have project in mind to I wanted to try to out I already di
d a similar project using AzureOpenAI but I'm not sure on how to implement it using Dialo 

Thank you
```
---

     
 
all -  [ Adding chunks to documents ](https://www.reddit.com/r/LangChain/comments/17muwii/adding_chunks_to_documents/) , 2023-11-06-0910
```
I am wondering if anyone has a fix for this problem. I am RAGing a set of documents that are often updated. I would like
 to reuse chunks so I hash them and compare to original. but if i get a large insertion in a document it will identify t
he whole doc after the change as modified. id like to just create chunks for the new part and move the remainder. How ar
e you handling changes documents efficiently ?
```
---

     
 
all -  [ Resource Recommendations for Staying Updated on AI Programming Developments? ](https://www.reddit.com/r/LangChain/comments/17mtqil/resource_recommendations_for_staying_updated_on/) , 2023-11-06-0910
```
Hello community, I've been making an effort to stay current with the latest developments in AI, particularly those relev
ant to programming. My interests lean more towards RAG tactics, Langchain, and similar topics, rather than AI in general
. Here are the resources I frequently use:

Reddit:

* Chatgptcoding: [https://www.reddit.com/r/ChatGPTCoding/](https://
www.reddit.com/r/ChatGPTCoding/)
* Langchain (ofcourse)
* ChatGPTPro: [https://www.reddit.com/r/ChatGPTPro/](https://www
.reddit.com/r/ChatGPTPro/)

YouTube:

* Sam Witteveen: [channel link](https://www.youtube.com/@samwitteveenai)
* James B
riggs: [channel link](https://www.youtube.com/@jamesbriggs)

Websites:  
\- [medium.com](https://medium.com) 

I'm wonde
ring if there might be other essential resources I'm missing out on. Could you recommend any other platforms or individu
als that could help me stay updated? Thank you!
```
---

     
 
all -  [ How to chunk tokenized data into two steps? ](https://www.reddit.com/r/LangChain/comments/17mszqf/how_to_chunk_tokenized_data_into_two_steps/) , 2023-11-06-0910
```
I have used RecursiveCharacterTextSplitter and Chroma (for vectorstore) but they are pretty base use. Is there a way I c
an achieve my tasks using LangChain functionality?based on 2 steps: 1st based on the tokens, then on chunk\_size (for ex
ample = 500 and overlap = 50) but only within the chunks from the first step.  For example: \[PART\]Summer is long gone.
\[\\PART\]\[PART\]I am a soccer fan. My favorite team is Real Madrid. But I also like the Italian Milan.\[\\PART\].  
So
 the chunks will be 1. Summer is long gone. and 2. I am a soccer fan ...  
But then I have the second step to use a spli
tter to split into chunks with some overlap. This part has to happen separately for 1 and 2.

I have used RecursiveChara
cterTextSplitter and Chroma (for vectorstore) but they are pretty base use. Is there a way I can achieve my tasks using 
LangChain functionality.
```
---

     
 
all -  [ ConversationalRetrievalAgent with local LLM ](https://www.reddit.com/r/LangChain/comments/17mrxbq/conversationalretrievalagent_with_local_llm/) , 2023-11-06-0910
```
Hi,

Just wondering if local LLM is supported? I am trying to build a basic chatbot with CRA function but it keeps getti
ng errors. fro the docs, I changed the chatmodel OpenAI into a local LLM (llamacpp) but it has errors. are local llms no
t supported yet? Thanks!
```
---

     
 
all -  [ Agent Hitting Token Limit ](https://www.reddit.com/r/LangChain/comments/17mpxr9/agent_hitting_token_limit/) , 2023-11-06-0910
```
I have an agent that is allowed to continue researching until it is ready to provide an answer. The issue isn't in any g
iven prompt or response - it just accumulates over time which i want to happen.

However, if it accumulates too much and
 exceeds the token limit, it will just crash.

I would like it to throw an error and continue onto the next row in my CS
V or to summarize the previous results, pass those back in, and continue where it left off. The agent's job is to valida
te claims in a response so ideally would pass back the claims it has validated and the claims it has left to validate. S
pecific python code would be super helpful here.
```
---

     
 
all -  [ Anyone know how to run a RetrievalQA in a for loop to iterate through 100 prompts (for testing a RAG ](https://www.reddit.com/r/LLMDevs/comments/17mndet/anyone_know_how_to_run_a_retrievalqa_in_a_for/) , 2023-11-06-0910
```
I have like 100+ prompts in a dataframe and am running a chain using the following settings in a colab notebook. However
 the 'for loop' is getting stuck after the 15th or 16th iteration of the loop or so- anyonoe have experience running mul
tiple prompts?

**Chain:**

RetrievalQA.from\_chain\_type(

llm=llm,

chain\_type='stuff',

retriever=docsearch.as\_retr
iever(search\_kwargs={'k': num\_retrieved\_documents})

&#x200B;

**Note I'm paying for OpenAI (like 30 dollars) and am 
using a free pinecone index as the vector DB; plus just running this in a notebook for testing.**

&#x200B;

**More info
 just came up I've seen two errors pop up once I left things to run for about 30 minutes:**

**First Error::**

WARNING:
langchain.llms.base:Retrying langchain.chat\_models.openai.ChatOpenAI.completion\_with\_retry.<locals>.\_completion\_wit
h\_retry in 4.0 seconds as it raised Timeout: Request timed out: HTTPSConnectionPool(host='api.openai.com', port=443): R
ead timed out. (read timeout=600).

**Second Error:**

WARNING:langchain.llms.base:Retrying langchain.chat\_models.opena
i.ChatOpenAI.completion\_with\_retry.<locals>.\_completion\_with\_retry in 4.0 seconds as it raised ServiceUnavailableEr
ror: The server is overloaded or not ready yet..

&#x200B;

&#x200B;
```
---

     
 
all -  [ Can I run a chain based on RetrievalQA in a for loop to test out a series of prompts? ](https://www.reddit.com/r/PromptEngineering/comments/17mnccy/can_i_run_a_chain_based_on_retrievalqa_in_a_for/) , 2023-11-06-0910
```
I have like 100+ prompts in a dataframe and am running a chain using the following settings in a colab notebook. However
 the 'for loop' is getting stuck after the 15th or 16th iteration of the loop or so- anyone have experience running mult
iple prompts?

I have like 100+ prompts in a dataframe and am running a chain using the following settings in a colab no
tebook. However the 'for loop' is getting stuck after the 15th or 16th iteration of the loop or so- anyonoe have experie
nce running multiple prompts?

  
**Chain:**  
RetrievalQA.from\_chain\_type(  
llm=llm,  
chain\_type='stuff',  
retrie
ver=docsearch.as\_retriever(search\_kwargs={'k': num\_retrieved\_documents})  
**Note I'm paying for OpenAI (like 30 dol
lars) and am using a free pinecone index as the vector DB; plus just running this in a notebook for testing.**  
**More 
info just came up I've seen two errors pop up once I left things to run for about 30 minutes:**  


**First Error::**  

WARNING:langchain.llms.base:Retrying langchain.chat\_models.openai.ChatOpenAI.completion\_with\_retry.<locals>.\_complet
ion\_with\_retry in 4.0 seconds as it raised Timeout: Request timed out: HTTPSConnectionPool(host='api.openai.com', port
=443): Read timed out. (read timeout=600).  
**Second Error:**  
WARNING:langchain.llms.base:Retrying langchain.chat\_mo
dels.openai.ChatOpenAI.completion\_with\_retry.<locals>.\_completion\_with\_retry in 4.0 seconds as it raised ServiceUna
vailableError: The server is overloaded or not ready yet..
```
---

     
 
all -  [ Why does OpenAI GPT model from langchain take so long for me, any ideas on hwo to speed it up? ](https://www.reddit.com/r/LLMDevs/comments/17mm3f2/why_does_openai_gpt_model_from_langchain_take_so/) , 2023-11-06-0910
```
i'm passing in around 1000 tokens including a SystemMessage to prime the model to act like a specific role, and a HumanM
essage with my ask. FYI the model I use is GPT-3.5-Turbo

This is taking like 90 seconds and then I tried it again and i
t takes 110 seconds... I don't think it should be taking this long?? I use this at work too through Azure and it's a lot
 faster, like in the matter of a few seconds... Why does this take so much longer, I guess one difference is that I don'
t use the SystemMessage at work usually.

Here are my imports:

from langchain.chat\_models import ChatOpenAI  
from lan
gchain.schema.messages import HumanMessage, SystemMessage

Anyone have any idea how to speed it up?
```
---

     
 
all -  [ Building a Recommendation System for a React Native ](https://www.reddit.com/r/reactnative/comments/17mjqzq/building_a_recommendation_system_for_a_react/) , 2023-11-06-0910
```
 So basically I am a beginner I want to build a React Native application specifically a dating app to practice my skills
 and knowledge I planned on using Supabase as the BE but I am pretty confused on how I would go about building the recom
mendation system so each user can get someone similar to them instead of just randomly showing any user I am thinking ve
ctorizing and doing some stuff like those AI Applications do using Vector DB and Langchain will work but still pretty co
nfused on those also

EDIT: I might need to show why he/she/they/them was recommended maybe based on location, shared in
terest or other things
```
---

     
 
all -  [ Question: Get exact prompt sent to openAI including history and inputs ](https://www.reddit.com/r/LangChain/comments/17min2n/question_get_exact_prompt_sent_to_openai/) , 2023-11-06-0910
```
Hello,

I am working on a chatbot, and have been using langchain to utilize the summarize history feature. Now I am buil
ding a database, that tracks many things that are happening during the dialog like the speakers input, number of words, 
speech emotion recognition, computation time, ram used and other useful meta data. 

The issue that I am running into, i
s I am unable to get the exact prompt, including the history and inputs, and store that data as a string, such that it c
an be stored in the database. 

I am surprised that this is not a trivial task, because it would seem to be fundamental 
to extract the exact data that is being sent to the LLM, as a way to debug, experiment, and store this information. 

Wh
at is odd, is that lang chain prints out the entire prompt that I want:  
'**Entering new ConversationChain chain...** 


Prompt after formatting:...'

I want everything in the 'Prompt after formatting', but cant figure out how to extract th
is as a string, and save store it in a variable in Python. 

I have looked at these resources so far:

[https://github.c
om/langchain-ai/langchain/issues/912](https://github.com/langchain-ai/langchain/issues/912) 

[https://www.reddit.com/r/
LangChain/comments/1643z8k/is\_there\_a\_way\_to\_print\_out\_the\_full\_prompt\_that/](https://www.reddit.com/r/LangCha
in/comments/1643z8k/is_there_a_way_to_print_out_the_full_prompt_that/)

[https://www.perplexity.ai/search/c1ea9c07-baf5-
4fb9-9a62-3353d68f6078?s=mn](https://www.perplexity.ai/search/c1ea9c07-baf5-4fb9-9a62-3353d68f6078?s=mn)

So I have figu
red out how to print it out using the verbose flag, but cannot figure out how to store it as a string in a variable. I h
ave been able to figure out how to save the prompt *without* the inputs and history, but not *with* the inputs and histo
ry. 

Looking for help. 

Thank you
```
---

     
 
all -  [ Source not being mentioned in the final answer ](https://www.reddit.com/r/LangChain/comments/17mikvx/source_not_being_mentioned_in_the_final_answer/) , 2023-11-06-0910
```
Hi all

I am using Langchain for RAG and retrieving documents from a Pinecone DB.

The answer is as follows:

> Entering
 new AgentExecutor chain...
{
    'action': 'Text Retrieval',
    'action_input': 'What is the ethereum blockchain?'
}Th
is is the new answer The Ethereum blockchain is a distributed state machine that tracks the state transitions of a gener
al-purpose data store. It can hold any data expressible as a key-value tuple and is similar to the data storage model of
 Random Access Memory (RAM) used in most general-purpose computers. Ethereum uses its blockchain to track changes in mem
ory over time and can load code into its state machine to run and store resulting state changes.
SOURCES: ../data/PDF/Ma
stering_Ethereum.pdf end
start ['Mastering_Ethereum.pdf'] end

Observation: {'question': 'What is the ethereum blockchai
n?', 'answer': 'The Ethereum blockchain is a distributed state machine that tracks the state transitions of a general-pu
rpose data store. It can hold any data expressible as a key-value tuple and is similar to the data storage model of Rand
om Access Memory (RAM) used in most general-purpose computers. Ethereum uses its blockchain to track changes in memory o
ver time and can load code into its state machine to run and store resulting state changes.\n', 'sources': ['Mastering_E
thereum.pdf'], 'source_documents': [Document(page_content='Ethereum: A General-Purpose Blockchain\nThe original blockcha
in, namely Bitcoin’s blockchain, tracks the state of units of bit‐\ncoin and their ownership. Y ou can think of Bitcoin 
as a distributed consensus state\nmachine , where transactions cause a global state transition , altering the ownership 
of\ncoins. The state transitions are constrained by the rules of consensus, allowing all\nparticipants to (eventually) c
onverge on a common (consensus) state of the system,\nafter several blocks are mined.\nEthereum is also a distributed st
ate machine. But instead of tracking only the state of\ncurrency ownership, Ethereum tracks the state transitions of a g
eneral-purpose data\nstore, i.e., a store that can hold any data expressible as a key–value tuple . A key–value\ndata st
ore holds arbitrary values, each referenced by some key; for example, the value\n“Mastering Ethereum” referenced by the 
key “Book Title” . In some ways, this serves\nthe same purpose as the data storage model of Random Access Memory  (RAM) 
used\nby most general-purpose computers. Ethereum has memory that stores both code\nand data, and it uses the Ethereum b
lockchain to track how this memory changes\nover time. Like a general-purpose stored-program computer, Ethereum can load
 code\ninto its state machine and run that code, storing the resulting state changes in its', metadata={'page': 43.0, 's
ource': '../data/PDF/Mastering_Ethereum.pdf'}), Document(page_content='Ethereum: A General-Purpose Blockchain\nThe origi
nal blockchain, namely Bitcoin’s blockchain, tracks the state of units of bit‐\ncoin and their ownership. Y ou can think
 of Bitcoin as a distributed consensus state\nmachine , where transactions cause a global state transition , altering th
e ownership of\ncoins. The state transitions are constrained by the rules of consensus, allowing all\nparticipants to (e
ventually) converge on a common (consensus) state of the system,\nafter several blocks are mined.\nEthereum is also a di
stributed state machine. But instead of tracking only the state of\ncurrency ownership, Ethereum tracks the state transi
tions of a general-purpose data\nstore, i.e., a store that can hold any data expressible as a key–value tuple . A key–va
lue\ndata store holds arbitrary values, each referenced by some key; for example, the value\n“Mastering Ethereum” refere
nced by the key “Book Title” . In some ways, this serves\nthe same purpose as the data storage model of Random Access Me
mory  (RAM) used\nby most general-purpose computers. Ethereum has memory that stores both code\nand data, and it uses th
e Ethereum blockchain to track how this memory changes\nover time. Like a general-purpose stored-program computer, Ether
eum can load code\ninto its state machine and run that code, storing the resulting state changes in its', metadata={'pag
e': 43.0, 'source': '../data/PDF/Mastering_Ethereum.pdf'})]}
Thought:{
    'action': 'Final Answer',
    'action_input':
 'The Ethereum blockchain is a distributed state machine that tracks the state transitions of a general-purpose data sto
re. It can hold any data expressible as a key-value tuple and is similar to the data storage model of Random Access Memo
ry (RAM) used in most general-purpose computers. Ethereum uses its blockchain to track changes in memory over time and c
an load code into its state machine to run and store resulting state changes.'
}

As you can see, I do have the sources 
associated with my text, and I accurately parse it with the RetrievalQAWithSourcesChain as well ('there's some manual pr
inting here that I did just to verify), but the final answer does not have any mention of the source. Why is that? I hav
e manually checked the _split_sources function in the RetrievalQAWithSourcesChain and it does extract the source and the
n return it along with the answer, but why isn't this being mentioned in the final answer?
```
---

     
 
all -  [ Vector store thought experiment for real world application ](https://www.reddit.com/r/LangChain/comments/17mhwjl/vector_store_thought_experiment_for_real_world/) , 2023-11-06-0910
```
This is a thought experiment I am trying to solve. 

Let’s say that I want an LLM to create the perfect product bundle f
or a given solution the user wants under a specific budget. For example, a solution could be “a university computer lab 
for 50 students under 50k”. An LLM like gpt-4 would most likely find a combination of pcs, monitors, keyboards, etc fair
ly well for the computer lab solution. 

Now let’s say I only want the LLM to be able to select products, though, from a
 product table I have built and to only select compatible products based on another table where I have product compatibi
lity references for different products. 

Would a good use case for vector database and embedding to create a single vec
tor store combining the data for each table and then ask it with the solution I want (the computer lab example above)?
```
---

     
 
all -  [ Styling stream response ](https://www.reddit.com/r/OpenAI/comments/17mh3bh/styling_stream_response/) , 2023-11-06-0910
```
Hey OpenAi community! I’m currently working on a research website where I can put in a question in the search box and it
 gives me points to answer that question:

1. Lorem ipsum

2. Lorem ipsum

For this, I am using gpt 4, langchain, NextJS
, and SerpApi. In my response, at the beginning, I want to include links to the specific sources that were being used.


Brookings    Harvard   University of Utah
…response

However, what is the best way to go over this? I want my links to b
e clickable and look nice. First I was thinking about letting my LLM write it, but that takes too long and is not too pr
etty.

Is there a way to use regex or something similar to insert my stylings?
```
---

     
 
all -  [ SolidGPT integrate with AutoGen, understand your codebase and let Multi-LLMAgent give you the code s ](https://www.reddit.com/r/AutoGenAI/comments/17mgs5f/solidgpt_integrate_with_autogen_understand_your/) , 2023-11-06-0910
```
Hi, Folks I just updated my open-source project - SolidGPT to integrate with AutoGen to improve my AI core power. I try 
to combine the LLMAgent and Chat into one task. Let me know your thoughts, are the LLMAgent and Chat two different ways?


SolidGPTn<>AutoGen. Introducing AutoGen Analysis, engage in issue-focused agent <> chat combination sessions, to get t
he most detailed insights.

Please try my new work: [https://github.com/AI-Citizen/SolidGPT](https://github.com/AI-Citiz
en/SolidGPT)

Scan and understand code with LangChain

Analysis requirement and give the response with AutoGen

&#x200B;


https://preview.redd.it/zco8n994p0yb1.png?width=3012&format=png&auto=webp&s=0ff795d3851d643e8fa418df33d9823eada2bce3
```
---

     
 
all -  [ Using GPT-4 and merging LangChain and AutoGen to create a ChatApp which can understand your codebase ](https://www.reddit.com/r/ChatGPT/comments/17mgpuw/using_gpt4_and_merging_langchain_and_autogen_to/) , 2023-11-06-0910
```
Hi, Folks I always have a question, are the LLMAgent and Chat two different ways for AI?

 I just updated my GPT4 dev ch
at app to integrate with AutoGen . I try to combine the LLMAgent and Chat into one task to give the code planbasede on t
he user codebase. Let me know your thoughts, are the LLMAgent and Chat two different ways?

Please try my new work: [htt
ps://github.com/AI-Citizen/SolidGPT](https://github.com/AI-Citizen/SolidGPT)

&#x200B;

https://preview.redd.it/j7lustb7
o0yb1.png?width=3012&format=png&auto=webp&s=35d5eb5f123a663e706e8d9e363b0637b4647ec4
```
---

     
 
all -  [ Merging LangChain and AutoGen, understand your codebase and let Multi-LLMAgent give you the code sol ](https://www.reddit.com/r/foss/comments/17mgmnt/merging_langchain_and_autogen_understand_your/) , 2023-11-06-0910
```
Hi, Folks I just updated my open-source project to integrate with AutoGen to improve my AI core power. I try to combine 
the LLMAgent and Chat into one task. Let me know your thoughts, are the LLMAgent and Chat two different ways? 

Merging 
LangChain<>AutoGen. Introducing AutoGen Analysis,  engage in issue-focused agent <> chat combination sessions, to get th
e most detailed insights.  

Please try my new work: [https://github.com/AI-Citizen/SolidGPT](https://github.com/AI-Citi
zen/SolidGPT)

Scan and understand code with LangChain

Analysis requirement and give the response with AutoGen 

https:
//preview.redd.it/enmjidzxn0yb1.png?width=3012&format=png&auto=webp&s=39bdf25c2713e26cc64e602c61f9a27c4b498975

&#x200B;

```
---

     
 
all -  [ Building a Recommendation System for a React Native ](https://www.reddit.com/r/react/comments/17mg4xn/building_a_recommendation_system_for_a_react/) , 2023-11-06-0910
```
So basically I am a beginner I want to build a React Native application specifically a dating app to practice my skills 
and knowledge I planned on using Supabase as the BE but I am pretty confused on how I would go about building the recomm
endation system so each user can get someone similar to them instead of just randomly showing any user I am thinking vec
torizing and doing some stuff like those AI Applications do using Vector DB and Langchain will work but still pretty con
fused on those also

EDIT: I might need to show why he/she/they/them was recommended maybe based on location, shared int
erest or other things

&#x200B;
```
---

     
 
all -  [ Any tips on debugging or configuration? ](https://www.reddit.com/r/ollama/comments/17mfdwd/any_tips_on_debugging_or_configuration/) , 2023-11-06-0910
```
1) Ollama rocks

2) See 1 above

Recently started using it and managed to pump a healthy amount of data through Ollama +
 llama2 with URL retrieval  on an MBP with an M2 and GPU, and have been really impressed. 

So tried out using RAG with 
chroma & langchain, and performance has been not so great. 

A single document, using OllamaEmbeddings 

\`\`\`

 'model
' : 'llama2:7b',

 'num\_gpu': 1,

 'num\_thread' : 10

\`\`\`

Doing a bit of profiling \_stream\_with\_aggregation [ht
tps://github.com/langchain-ai/langchain/blob/f66a9d2adfe84ae70bd66d957f153f975a55313e/libs/langchain/langchain/llms/olla
ma.py#L147C1-L148C1](https://github.com/langchain-ai/langchain/blob/f66a9d2adfe84ae70bd66d957f153f975a55313e/libs/langch
ain/langchain/llms/ollama.py#L147C1-L148C1)

Seems to be taking all the cumulative time and activity viewer is only show
ing me ollama-runner with 98% GPU. 

&#x200B;

What should my next steps be in terms of debugging? 

Appreciate any poin
ters
```
---

     
 
all -  [ Synology Chat LLM feedback ](https://www.reddit.com/r/synology/comments/17ma5fm/synology_chat_llm_feedback/) , 2023-11-06-0910
```
I created a thing to use with synology chat, it is a local LLM service where one is the basic talk to a llm and the othe
r uses langchain for memory and wiki Q&A. I would love some feedback and maybe help in ways to improve it.  
[https://gi
thub.com/CaptJaybles/synologyLLM](https://github.com/CaptJaybles/synologyLLM)

[https://github.com/CaptJaybles/SynoLangc
hain](https://github.com/CaptJaybles/SynoLangchain)
```
---

     
 
all -  [ My name is Jordy and I just got rickrolled by an AI agent. AMA ](https://i.redd.it/yuzovs6q1zxb1.jpg) , 2023-11-06-0910
```
I was testing it out, asked for a 2 minute cat video, got rickrolled. 

AI has developed a sense of humour before the Ge
rmans did. Chapeau.
```
---

     
 
MachineLearning -  [ [D] Is this close enough to be usable? Need your inputs: Automated RAG testing tool. AI Data Pipelin ](https://www.reddit.com/r/MachineLearning/comments/17kkbm0/d_is_this_close_enough_to_be_usable_need_your/) , 2023-11-06-0910
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

     
 
MachineLearning -  [ [D] Relevance Extraction in RAG Pipelines ](https://www.reddit.com/r/MachineLearning/comments/17k6iha/d_relevance_extraction_in_rag_pipelines/) , 2023-11-06-0910
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

     
 
MachineLearning -  [ [R] Model Troubles ](https://www.reddit.com/r/MachineLearning/comments/17ikh2u/r_model_troubles/) , 2023-11-06-0910
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

     
 
MachineLearning -  [ [P] NexaAgent: A highly efficient multi-task PDF tool for all your needs | backed by AutoGen ](https://www.reddit.com/r/MachineLearning/comments/17eajz2/p_nexaagent_a_highly_efficient_multitask_pdf_tool/) , 2023-11-06-0910
```
Just a quick open-source project recently submitted to huggingface backed by AutoGen. Share this initial version with yo
u guys!

[NexaAgent 0.0.1](https://huggingface.co/spaces/xuyingliKepler/nexaagent) offers a straightforward solution for
 handling PDFs.

* Users can easily upload any PDF, regardless of its size.
* The tool emphasizes accuracy, minimizing d
iscrepancies in PDF processing.

At its core, NexaAgent is backed by the AutoGen and LangChain frameworks. AutoGen facil
itates multi-agent interactions for task execution, while LangChain bridges LLMs with external data sources. Together, t
hese technologies ensure NexaAgent's robust and precise PDF management capabilities.

https://preview.redd.it/kwgo3phnav
vb1.jpg?width=1440&format=pjpg&auto=webp&s=1c5fbc566938d60d5c43802aff3a0690821e1c79
```
---

     
 
MachineLearning -  [ [D] Is lang chain the right solution? ](https://www.reddit.com/r/MachineLearning/comments/17coyym/d_is_lang_chain_the_right_solution/) , 2023-11-06-0910
```
Hello, I would love to have an LLm that can provide answers (in chat format) based some of the sql db  data we have. Wan
t it for an internal company project. I am by no means an expert but decent in programming and want to build a system to
 get answers in chat format. My understanding is that training LLMs ground up is prohibitively expensive and langchains 
are sort of hybrid , efficient solutions. 

Please suggest any other solutions. Also would Langchain being a company and
 not open source pose a problem in terms of copyrights? Thanks!
```
---

     
 
MachineLearning -  [ [P] building a D&D NPC ](https://www.reddit.com/r/MachineLearning/comments/17clyw6/p_building_a_dd_npc/) , 2023-11-06-0910
```
Hey everyone,

I'm learning ML but i'm barely scratching the terminologies. 2 years ago I couldn't code anything but wit
h school (python,sql and R) I learned fundamentals. I also have access to code academy.  My current program is very mach
ine learning/deep learning focused.

On the side I DM a d&d game. Within the context of the world (eberron) robots are c
ommon. With my ADHD and being a new DM I want to outsource lore questions might have (that I would have to look up and s
low down the game).

The concept is to have a GUI and have the player interact with the chat bot. I've gotten to a proof
 of concept workflow. On Google colab. Thanks to langchain I managed to ingest pdfs and a url. Make then a directory, Em
bedded the text, bring it into a vector dB. Have the llm pull from the vector. Answer the question.

Now I don't know wh
at to do. I tried to bring the colab notebook onto Google cloud. But now cloud is becoming a rabbit home with vertex and
 docAI...and I don't want to deep dive into that, if it's a outside the scope of this 'project'

I'd appreciate any advi
ce, links...etc. 


I got a limited success in botpress using a single pdf. It works but feel unsatisfying.
N8N looks pr
omising but if it's not intuitive then I don't want to go down that road.


If I posted in the wrong group please direct
 me to the correct one.
```
---

     
 
MachineLearning -  [ [D] Exploring Methods to Improve Text Chunking in RAG Models (and other things...) ](https://www.reddit.com/r/MachineLearning/comments/179j7l3/d_exploring_methods_to_improve_text_chunking_in/) , 2023-11-06-0910
```
Hello everyone,

I'm currently working on Retrieval Augmented Generation (RAG) models and have developed a custom chunki
ng function, as I found the methods in LangChain not entirely satisfactory.

I'm keen on exploring other methods, algori
thms (related to NLP or otherwise), and models to enhance text chunking in RAG. There are many RAG implementations out t
here, but I've noticed a lack of focus on improving chunking performance specifically.

Are there any other promising ap
proaches beyond my current pipeline, which consists of a bi-encoder (retriever), cross-encoder (reranker), and a Large L
anguage Model (LLM) for interactions?

For queries, I'm using both traditional and HyDE (Hypothetical Document Embedding
) approaches in the retrieval phase, and sending the top 'n' results of both similarity search to the reranker.

I've al
so tried using an LLM to convert the query into a series of 10-20 small phrases or keywords, which are then used as the 
query for the retriever model. However, the results vary depending on the LLM used. To generate good keywords (with a no
t extractive approach) , I had to  use a 'CoT' prompt, instructing the model to  write self-instruct, problem analysis a
nd reasonings before generating the required keywords. But this approach use lots of tokens, and requires careful scrapi
ng to ensure the model has used the right delimiter to separate reasoning and the actual answer.

I'm also planning to m
odify the text used to generate embeddings, while returning the original text after the recall phase. But this is still 
a work in progress and scaling it is proving to be a challenge. If anyone has any tips or experience with this, I'd appr
eciate your input.

I'd be grateful for any resources, repositories, libraries, or existing implementations of novel chu
nking methods that you could share. Or we could just discuss ideas, thoughts, or approaches to improve text chunking for
 RAG here.

Thanks in advance for your time!
```
---

     
 
MachineLearning -  [ [News] AI & ML conference in San Francisco [Special discount code for this subreddit] ](https://www.reddit.com/r/MachineLearning/comments/1771m35/news_ai_ml_conference_in_san_francisco_special/) , 2023-11-06-0910
```
I work for this database company SingleStore and we are hosting a AI & ML conference in San Francisco on 17th of October
, 2023.

It is an in-person conference with amazing speakers line-up like Harrison Chase, co-founder and CEO of LangChai
n and many more. We will have hands-on workshops, swags giveaway and much more.

I don't know if it makes sense to share
 this but I believe it might help some of you near San Francisco to go and meet the industry leaders and network with ot
her data engineering folks.

Use my discount coupon code 'PAVAN100OFF' to avail 100% off on the ticket price. (the origi
nal ticket price is $199)

[Get your tickets now!](https://singlestore.com/now)
```
---

     
 
MachineLearning -  [ [D] Best way to validate llm prompts? ](https://www.reddit.com/r/MachineLearning/comments/176vnxh/d_best_way_to_validate_llm_prompts/) , 2023-11-06-0910
```
We have a platform for data analytics which uses a very simple dsl to generate charts.  
We have been experimenting with
 llms to use natural language that gets translated into this dsl and hence generates charts.

This is working pretty goo
d.  
The stack is langchain with openai api. (don't have much experience with llms, it's a prototype to get a feel for i
t)

The question is what is the best way to limit the options user can type in as a prompt.  
Basically the the only all
owed things should be: 'What is the X, Y over 10 days period for this or that?'  
I don't want users to ask questions li
ke when did we first land on the moon.

Is it something that is possible to do at all without additional tooling?  
We p
robably don't want to train another model to classify the prompt as valid or invalid or something similar.
```
---

     
 
deeplearning -  [ Error with Mistral 7B model in ConversationalRetrievalChain ](https://www.reddit.com/r/deeplearning/comments/179vvou/error_with_mistral_7b_model_in/) , 2023-11-06-0910
```
 I'm encountering an issue while using the Mistral 7B model in a ConversationalRetrievalChain. When I input a question, 
such as 'What is the highest GDP?', I receive an error and after that the model generates a random response as output wh
ich is not relevant to the Input query. It seems that the number of tokens in the input exceeds the maximum context leng
th. 

Here's the relevant code: 

 

>`from langchain.document_loaders.csv_loader import CSVLoader`  
`from langchain.te
xt_splitter import RecursiveCharacterTextSplitter`  
`from langchain.embeddings import HuggingFaceEmbeddings`  
`from la
ngchain.vectorstores import FAISS`  
`from langchain.llms import CTransformers`  
`from langchain.memory import Conversa
tionBufferMemory`  
`from langchain.chains import ConversationalRetrievalChain`  
`import sys`  
`DB_FAISS_PATH = 'vecto
rstore/db_faiss'`  
`loader = CSVLoader(file_path='data/World Happiness Report 2022.csv', encoding='utf-8', csv_args={'d
elimiter': ','})`  
`data = loader.load()`  
`print(data)`  
`# Split the text into Chunks`  
`text_splitter = Recursive
CharacterTextSplitter(chunk_size=500, chunk_overlap=20)`  
`text_chunks = text_splitter.split_documents(data)`  
`print(
len(text_chunks))`  
`# Download Sentence Transformers Embedding From Hugging Face`  
`embeddings = HuggingFaceEmbedding
s(model_name = 'sentence-transformers/all-MiniLM-L6-v2')`  
`# COnverting the text Chunks into embeddings and saving the
 embeddings into FAISS Knowledge Base`  
`docsearch = FAISS.from_documents(text_chunks, embeddings)`  
`docsearch.save_l
ocal(DB_FAISS_PATH)`  
  
>  
>`#query = 'What is the value of GDP per capita of Finland provided in the data?'`  
`#doc
s = docsearch.similarity_search(query, k=3)`  
`#print('Result', docs)`  
`llm = CTransformers(model='models/mistral-7b-
v0.1.Q4_0.gguf',`  
 `model_type='llama',`  
 `max_new_tokens=1000,`  
 `temperature=0.1)`  
`qa = ConversationalRetriev
alChain.from_llm(llm, retriever=docsearch.as_retriever())`  
`while True:`  
 `chat_history = []`  
 `#query = 'What is 
the value of  GDP per capita of Finland provided in the data?'`  
 `query = input(f'Input Prompt: ')`  
 `if query == 'e
xit':`  
 `print('Exiting')`  
 `sys.exit()`  
 `if query == '':`  
 `continue`  
 `result = qa({'question':query, 'chat
_history':chat_history})`  
 `print('Response: ', result['answer'])`

 

**Problem Statement:**

I'm trying to utilize t
he Mistral 7B model for a ConversationalRetrievalChain, but I'm encountering an error related to token length:

Number o
f tokens (760) exceeded maximum context length (512).

**Context:**

I'm working on a project that involves using Mistra
l 7B to answer questions based on a dataset. The dataset contains information about the World Happiness Report 2022.

**
Steps Taken:**

* Loaded and preprocessed the dataset using langchain.
* Initialized Mistral 7B with the following param
eters:
* Model: 'models/mistral-7b-v0.1.Q4\_0.gguf'
* Model Type: 'llama'
* Max New Tokens: 1000
* Temperature: 0.1
* Se
t up a ConversationalRetrievalChain with Mistral 7B as the language model and a retriever based on FAISS.

**Expected Ou
tput:**

I expect to receive a meaningful response from Mistral 7B based on the input query.

**Additional Information:*
*

I'm using Python and relevant libraries for this project. The dataset I'm working with is from the World Happiness Re
port 2022.

**Environment Details:**

* Python version: 3.11.4 
* Relevant libraries and versions: 

langchain 

ctransf
ormers 

sentence-transformers 

faiss-cpu
```
---

     
 
deeplearning -  [ Error with Mistral 7B model in ConversationalRetrievalChain. ](https://www.reddit.com/r/deeplearning/comments/179vsif/error_with_mistral_7b_model_in/) , 2023-11-06-0910
```
I'm encountering an issue while using the Mistral 7B model in a ConversationalRetrievalChain. When I input a question, s
uch as 'What is the highest GDP?', I receive an error and after that the model generates a random response as output whi
ch is not relevant to the Input query. It seems that the number of tokens in the input exceeds the maximum context lengt
h.

Here's the relevant code:

>from langchain.document\_loaders.csv\_loader import CSVLoader  
>  
>from langchain.text
\_splitter import RecursiveCharacterTextSplitter  
>  
>from langchain.embeddings import HuggingFaceEmbeddings  
>  
>fr
om langchain.vectorstores import FAISS  
>  
>from langchain.llms import CTransformers  
>  
>from langchain.memory impo
rt ConversationBufferMemory  
>  
>from langchain.chains import ConversationalRetrievalChain  
>  
>import sys  
>  
>  

>  
>DB\_FAISS\_PATH = 'vectorstore/db\_faiss'  
>  
>loader = CSVLoader(file\_path='data/World Happiness Report 2022.c
sv', encoding='utf-8', csv\_args={'delimiter': ','})  
>  
>data = loader.load()  
>  
>print(data)  
>  
>  
>  
>\# Sp
lit the text into Chunks  
>  
>text\_splitter = RecursiveCharacterTextSplitter(chunk\_size=500, chunk\_overlap=20)  
> 
 
>text\_chunks = text\_splitter.split\_documents(data)  
>  
>  
>  
>print(len(text\_chunks))  
>  
>  
>  
>\# Downlo
ad Sentence Transformers Embedding From Hugging Face  
>  
>embeddings = HuggingFaceEmbeddings(model\_name = 'sentence-t
ransformers/all-MiniLM-L6-v2')  
>  
>  
>  
>\# COnverting the text Chunks into embeddings and saving the embeddings in
to FAISS Knowledge Base  
>  
>docsearch = FAISS.from\_documents(text\_chunks, embeddings)  
>  
>  
>  
>docsearch.save
\_local(DB\_FAISS\_PATH)  
>  
>  
>  
>  
>  
>\#query = 'What is the value of GDP per capita of Finland provided in th
e data?'  
>  
>  
>  
>\#docs = docsearch.similarity\_search(query, k=3)  
>  
>  
>  
>\#print('Result', docs)  
>  
>
  
>  
>llm = CTransformers(model='models/mistral-7b-v0.1.Q4\_0.gguf',  
>  
>model\_type='llama',  
>  
>max\_new\_toke
ns=1000,  
>  
>temperature=0.1)  
>  
>  
>  
>qa = ConversationalRetrievalChain.from\_llm(llm, retriever=docsearch.as\
_retriever())  
>  
>  
>  
>while True:  
>  
>chat\_history = \[\]  
>  
>\#query = 'What is the value of  GDP per cap
ita of Finland provided in the data?'  
>  
>query = input(f'Input Prompt: ')  
>  
>if query == 'exit':  
>  
>print('E
xiting')  
>  
>sys.exit()  
>  
>if query == '':  
>  
>continue  
>  
>result = qa({'question':query, 'chat\_history':
chat\_history})  
>  
>print('Response: ', result\['answer'\])

 

**Problem Statement:**

I'm trying to utilize the Mis
tral 7B model for a ConversationalRetrievalChain, but I'm encountering an error related to token length:

Number of toke
ns (760) exceeded maximum context length (512).

**Context:**

I'm working on a project that involves using Mistral 7B t
o answer questions based on a dataset. The dataset contains information about the World Happiness Report 2022.

**Steps 
Taken:**

* Loaded and preprocessed the dataset using langchain.
* Initialized Mistral 7B with the following parameters:

* Model: 'models/mistral-7b-v0.1.Q4\_0.gguf'
* Model Type: 'llama'
* Max New Tokens: 1000
* Temperature: 0.1
* Set up a
 ConversationalRetrievalChain with Mistral 7B as the language model and a retriever based on FAISS.

**Expected Output:*
*

I expect to receive a meaningful response from Mistral 7B based on the input query.

**Additional Information:**

I'm
 using Python and relevant libraries for this project. The dataset I'm working with is from the World Happiness Report 2
022.

**Environment Details:**

Python version: 3.11.4 Relevant libraries and versions: langchain ctransformers sentence
-transformers faiss-cpu

&#x200B;
```
---

     
 
deeplearning -  [ Free courses to learn about Large Language Models and building AI projects ](https://www.reddit.com/r/deeplearning/comments/178zu2u/free_courses_to_learn_about_large_language_models/) , 2023-11-06-0910
```
[**LangChain for LLM Application Development by Andrew Ng**](https://www.deeplearning.ai/short-courses/langchain-for-llm
-application-development/): Apply LLMs to your proprietary data to build personal assistants and specialized chatbots. 


[**Full Stack LLM Bootcamp**](https://fullstackdeeplearning.com/llm-bootcamp/): Learn best practices and tools for buil
ding LLM-powered apps 

[**Stanford CS324**](https://stanford-cs324.github.io/winter2022/): In this course, students wil
l learn the fundamentals about the modeling, theory, ethics, and systems aspects of large language models, as well as ga
in hands-on experience working with them. 

[**LangChain & Vector Databases in Production**](https://learn.activeloop.ai
/courses/langchain): Learn how to leverage LangChain, a robust framework for building applications with LLMs, and explor
e Deep Lake, a groundbreaking vector database for all AI data. 

[**Stanford CS25**](https://web.stanford.edu/class/cs25
/): In this course, learn how transformers work, and dive deep into the different kinds of transformers and how they're 
applied in different fields. 

[**LLMOps Space Discord**](https://llmops.space/discord): LLMOps Space is a global commun
ity for LLM practitioners.
```
---

     
