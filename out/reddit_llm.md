 
all -  [ How to extract date period from user prompt ](https://www.reddit.com/r/LangChain/comments/1ctr9h5/how_to_extract_date_period_from_user_prompt/) , 2024-05-17-0910
```
Hello everyone!
I would like to have some help for a problem i have
I want to extract two parameters:
date_from: the sta
rt of the period
date_to: the end of the period

I tried using this [example](https://python.langchain.com/v0.1/docs/use
_cases/extraction/) but it sometimes misses at simple prompts

What can i add to make it better?
Here’s the [code](https
://hastebin.skyra.pw/yehokamuqo.py) i made


Basically i want it to get from the user’s prompt the correct date or perio
d
```
---

     
 
all -  [ Classify PDF based on separate RAG database ](https://www.reddit.com/r/LangChain/comments/1ctqz2c/classify_pdf_based_on_separate_rag_database/) , 2024-05-17-0910
```
I’m trying to set something up where a user can upload a pdf and have it classified based on a resource I converted into
 a vector database. 
```
---

     
 
all -  [ Langchain using llama3 to build recommendation system ](https://www.reddit.com/r/Python/comments/1ctnxa4/langchain_using_llama3_to_build_recommendation/) , 2024-05-17-0910
```
Hi,

Recently I played a bit with LLMs, specifcally exploring ways of running the models locally and building prompts us
ing LangChain. As a result ended up coding a small recommendation system, powered with Llama3-7b model, which suggests t
opics to read on HackerNews.

Wanted to share my experiences, so I wrote a small article where I described all my findin
gs.  
Hope you'll like it: [https://lukaszksiezak.github.io/ScrapyToLLM/](https://lukaszksiezak.github.io/ScrapyToLLM/)


Github repo: [https://github.com/lukaszksiezak/ScrapyToLLM](https://github.com/lukaszksiezak/ScrapyToLLM)

**What the p
roject does:**

It's a Python application which uses scrapy to scrape HackerNews page. Scraped articles are pipelined to
 redis, which is then feeding Llama3 using langchain. Prompter is configured to serve a user articles which are matching
 his request.

**Target Audience**:

I think it suits the best all the people who are looking for a Hello World projects
 using LLMs. I think it also reveals some difficulties related to LLM tech, what potential problems could be found in pr
oduction systems.

**Comparison:**

Recommendation systems are widely used and known, however LLMs are the ones which ma
y work out of the box when appropriate prompt is given. It's kind of interesting to explore various usages of the techno
logy and take part in fast grow of that stack.

Cheers.
```
---

     
 
all -  [ Struggling with prompt management tools ](https://www.reddit.com/r/LangChain/comments/1ctk5l5/struggling_with_prompt_management_tools/) , 2024-05-17-0910
```
I’m working on a project for a client who needs single summaries of games for a game recommender app they’re creating. I
’ve been trying to test out a pipeline of prompts to see what inputs generate the best summaries, but I’m struggling 😓 


It’s easy to view and edit one prompt at a time, but I need a tool that can handle these more complex, chained prompt s
cenarios effectively. It feels like there are tools out there that could potentially help, but none seem fully integrate
d into a seamless prompt management workflow. I want to look across multiple sample output examples (from several sample
 inputs), and see what’s working and what’s not. 

Anyone else facing the same struggles? How are you managing more comp
lex prompt scenarios / how are you integrating multiple tools to get the job done? 

Maybe it's just part of the job, bu
t I can't help but think there's got to be a better way to manage and streamline this whole process. Any insights or tip
s would be super helpful! 


```
---

     
 
all -  [ Optimizing AI Data Processing with MinIO Weaviate and Langchain in Retrieval Augmented Generation (R ](https://www.reddit.com/r/minio/comments/1ctiw1l/optimizing_ai_data_processing_with_minio_weaviate/) , 2024-05-17-0910
```
In this article, we will delve into the integration of MinIO with Retrieval-Augmented Generation (RAG) pipelines and Wea
viate vector storage, using LangChain.

[https://blog.min.io/optimizing-ai-data-processing-with-minio-weaviate-and-langc
hain-in-retrieval-augmented-generation-rag-pipelines/](https://blog.min.io/optimizing-ai-data-processing-with-minio-weav
iate-and-langchain-in-retrieval-augmented-generation-rag-pipelines/)
```
---

     
 
all -  [ Agents working in parallel with LangGraph ](https://www.reddit.com/r/LangChain/comments/1cthrqz/agents_working_in_parallel_with_langgraph/) , 2024-05-17-0910
```
I’m trying to figure out if it’s possible to create a Multi Agent application with LangGraph, where the agents can work 
in parallel (if needed).

Let’s say I have three agents (stupid example):
1. Supervisor
2. Agent specialized in tech con
ferences
3. Agent specialized in medical conferences

Each agent has its own tools.

The user query is “What are the mai
n tech conferences and medical conferences in San Francisco in November?”.

This query can be obviously split in two dif
ferent questions and each one can be addressed separately: 
1. What are the main tech conferences in San Francisco in No
vember?
2. What are the main medical conferences in San Francisco in November?

The Supervisor is able to process the or
iginal query, to produce these two questions and to route them separately to the correct Agent.

Is there a way to run t
hese two agents in parallel and to have a fourth Agent (or the supervisor itself) that waits for the two answers and put
s all together to produce a single final answer?

Does anyone have experience with such a use case?
```
---

     
 
all -  [ LangChain vs LlamaIndex  ](https://www.reddit.com/r/AI_Agents/comments/1cth187/langchain_vs_llamaindex/) , 2024-05-17-0910
```
Checkout this short video to understand the difference between two major Generative AI packages i.e. LangChain and Llama
Index and what to use when : https://youtu.be/Oy8UZp3potw?si=9mp9M5UrBjR-FX5G
```
---

     
 
all -  [ LangChain vs LlamaIndex Generative AI packages differences explained  ](/r/LangChain/comments/1ctgx1l/langchain_vs_llamaindex_differences_explained/) , 2024-05-17-0910
```

```
---

     
 
all -  [ Sending multiple prompts in parallel to OpenAI  ](https://www.reddit.com/r/LangChain/comments/1ctgq91/sending_multiple_prompts_in_parallel_to_openai/) , 2024-05-17-0910
```
Is there any way in LangChain where we can get the responses for multiple queries/prompts in LangChain?

Suppose I have 
a function in python:
```python
def function(...):
    prompt_1 = '...'
    prompt_2 = '...'
    
    # make these API c
alls in parallel - use multithreading?
    response_1 = llm.invoke(prompt_1)
    reponse_2 = llm.invoke(prompt_2)

    #
 rest of the code
```
```
---

     
 
all -  [ Career outside large vision and language models ](https://www.reddit.com/r/computervision/comments/1ctg46t/career_outside_large_vision_and_language_models/) , 2024-05-17-0910
```
Hi everyone,
I've done computer vision in industry for 8+ years. I worked on tabular data a bit and then changed jobs. T
he wave of ChatGPT had just started after my switch and soon, gpt4 vision followed suit.

I like building models or at l
east fine tuning them. I don't like calling APIs even though gpt4 vision is fantastic for the use cases my company works
 on.

Having said that, are there other areas in computer vision that haven't been penetrated by LLMs or LVMs yet? What'
s the status of 3D computer vision these days? I've just started studying some basic projective geometry stuff from the 
book Multiple view geometry but I'm wondering if this is all worth it. My interest in generative AI is the theory (and i
mplementation) of generative deep learning algorithms and methods (GANs, Flows, Diffusion models) but not using langchai
n, openai api etc for building RAG or agentic applications. 

Note : Self driving cars seems like a big application area
 but unfortunately, India may don't see them for a really long time.

I wanna know where computer vision is growing and 
what are some potentially interesting areas that our outside the current llm and lvm waves.

Thanks,
```
---

     
 
all -  [ AI Agents ](https://www.reddit.com/r/LangChain/comments/1ctfepy/ai_agents/) , 2024-05-17-0910
```
Hi folks, it seems to me that the current sentiment around AI agents is very negative as in that they're useless but I d
on't quite understand why. Could anybody explain to me why this view persists?
```
---

     
 
all -  [ How to deploy LangChain applications on AWS ](https://www.reddit.com/r/devops/comments/1ctel5e/how_to_deploy_langchain_applications_on_aws/) , 2024-05-17-0910
```
Deploying LangChain applications can be complex due to the need for various cloud services. This article explores the ch
allenges developers face when deploying with AWS CDK or the AWS console, and introduces Pluto, a tool that enables devel
opers to focus on writing business logic rather than getting bogged down in tedious configuration tasks.

https://pluto-
lang.vercel.app/blogs/240515-develop-ai-app-in-new-paradigm
```
---

     
 
all -  [ How to effectively chunk csv and xlsx files? Excel file can contain text/tables. ](https://www.reddit.com/r/LangChain/comments/1ct97ix/how_to_effectively_chunk_csv_and_xlsx_files_excel/) , 2024-05-17-0910
```
I'm looking for ways to effectively chunk csv/excel files. In a meaningful manner. I looked into loaders but they have u
nstructuredCSV/Excel Loaders which are nothing but from Unstructured. Is there something in Langchain that I can use to 
chunk these formats meaningfully for my RAG?
```
---

     
 
all -  [ Tool to compare LLM Outputs ](https://www.reddit.com/r/LLMDevs/comments/1ct8f3j/tool_to_compare_llm_outputs/) , 2024-05-17-0910
```
Is there a tool which lets users compare outputs from multiple LLM's based off a single prompt? I imagine with LangChain
 someone can build this locally but wonder if any such products are out there?

Tired of copy pasting the same input acr
oss GPT, Claude, Bard & Perplexity to triangulate answers & check accuracy

Tool to compare LLM Outputs

Is there a tool
 which lets users compare outputs from multiple LLM's based off a single prompt? I imagine with LangChain someone can bu
ild this locally but wonder if any such products are out there?

Tired of copy pasting the same input across GPT, Claude
, Bard & Perplexity to triangulate answers & check accuracy
```
---

     
 
all -  [ AI Developments in Financial Services, Social Media, and Healthcare: A Weekly Digest ](https://www.reddit.com/r/ai_news_by_ai/comments/1ct623n/ai_developments_in_financial_services_social/) , 2024-05-17-0910
```





#hardware #event #startups #tool #opinions #release #feature #update #vc #opensource #bigtech #api #leaders #scienc
e #major_players #scheduled

NVIDIA is hosting AI sessions at Money20/20 Europe, focusing on AI in financial services. T
he event will feature speakers from Mastercard, Stripe, Barclays, and others, and will cover topics such as generative A
I, fraud detection, and the impact of AI on the banking customer experience. BNY Mellon has deployed an NVIDIA DGX Super
POD™ with DGX™ H100 systems, and the event will also discuss trends, challenges, and opportunities in AI for financial s
ervices in 2024 [1].







Mike Krieger, co-founder of Instagram, has joined Anthropic as the Chief Product Officer. Hi
s expertise in building and scaling innovative products will help Anthropic expand its suite of enterprise applications 
and bring Claude to a wider audience [2].







Cohere, a company dedicated to scaling intelligence to serve humanity, 
is actively hiring. The company offers various benefits to employees, including RRSP contributions, health coverage, men
tal health support, remote work culture, generous time off, and support for new parents [3]. Cohere has also been featur
ed in CNBC's Disruptor 50 list for the second consecutive year, reflecting its commitment to providing practical AI solu
tions that tackle real-world business challenges [4].







Andrew Ng has announced a new short course on Multi AI Agen
t Systems with crewAI. The course focuses on breaking down complex tasks into subtasks for multiple AI agents to execute
 specialized roles [5]. Groq Inc has launched a new series called GroqThoughts, with the first feature focusing on how A
thena Intelligence and Groq collaborate to enable real-time use cases [6]. Groq Inc is also hosting a virtual hackathon 
for developers to showcase their projects built on Groq technology [9].







Langtrace AI conducted a performance anal
ysis comparing the latencies of different language models, including Groq running Llama-3. Groq demonstrated the lowest 
latencies across all tests, making it the ideal choice for applications where speed is essential [11].







LanceDB, a
n open-source database for AI, has secured $8 million in seed funding. The company aims to empower AI teams to search ov
er billions of vectors, process petabytes of images, and train on trillions of tokens [12]. HiPythagora, a Y Combinator 
W24 startup, has developed Pythagora, an open-source development tool that can build entire applications from scratch by
 interacting with users [13].







Google has introduced new generative media models and tools, including Veo for vide
o generation and Imagen 3 for image generation. They have also collaborated with filmmakers and musicians to showcase th
e capabilities of their AI technologies [15]. Google is also enhancing the Gemini app to be more multimodal, agentive, a
nd intelligent, serving as a personal AI assistant capable of handling complex tasks and taking actions on behalf of use
rs [16].







NVIDIA and LangChain are hosting a Generative AI Agents Developer Contest where participants can develop
 text and multimodal agents using their technologies [21]. NVIDIA AI Developer shared about the implementation of single
-view 3D tracking in NVIDIA DeepStream to enhance object tracking accuracy [23].







Yann LeCun emphasizes the import
ance of open source AI platforms for a vibrant ecosystem and to maximize the benefits of AI for society [26]. Greg Brock
man acknowledges the team effort behind GPT-4 and gives credit to Pranav Dhar for leading the development of the omni mo
del in collaboration with various teams at OpenAI over the past 18 months [27].







Google AI has announced Illuminat
e at Google IO, a tool that uses AI to convert research papers into audio conversations to enhance learning experiences 
[32]. Google AI has also introduced Med-Gemini, a new family of AI research models for medicine that builds on Gemini's 
advanced capabilities. The models have achieved state-of-the-art performance on various benchmarks and have unlocked nov
el applications in the medical domain [35].




[1. NVIDIA AI @NVIDIAAI https://twitter.com/NVIDIAAI/status/179060805072
7845980](https://twitter.com/NVIDIAAI/status/1790608050727845980)

[2. Anthropic @anthropicai https://twitter.com/anthro
picai/status/1790744375418589227](https://twitter.com/anthropicai/status/1790744375418589227)

[3. cohere @cohere https:
//twitter.com/cohere/status/1790745447327268938](https://twitter.com/cohere/status/1790745447327268938)

[4. cohere @coh
ere https://twitter.com/cohere/status/1790745445465039092](https://twitter.com/cohere/status/1790745445465039092)

[5. A
ndrew Ng @AndrewYNg https://twitter.com/AndrewYNg/status/1790769732146307308](https://twitter.com/AndrewYNg/status/17907
69732146307308)

[6. Groq Inc @GroqInc https://twitter.com/GroqInc/status/1790734880235495512](https://twitter.com/GroqI
nc/status/1790734880235495512)

[7. Groq Inc @GroqInc https://twitter.com/GroqInc/status/1790774240574116203](https://tw
itter.com/GroqInc/status/1790774240574116203)

[8. Groq Inc @GroqInc https://twitter.com/GroqInc/status/1790783354960515
427](https://twitter.com/GroqInc/status/1790783354960515427)

[9. Groq Inc @GroqInc https://twitter.com/GroqInc/status/1
790794933143802365](https://twitter.com/GroqInc/status/1790794933143802365)

[10. Groq Inc @GroqInc https://twitter.com/
GroqInc/status/1790806854009798891](https://twitter.com/GroqInc/status/1790806854009798891)

[11. Groq Inc @GroqInc http
s://twitter.com/GroqInc/status/1790851920992616504](https://twitter.com/GroqInc/status/1790851920992616504)

[12. Y Comb
inator @ycombinator https://twitter.com/ycombinator/status/1790776813578584553](https://twitter.com/ycombinator/status/1
790776813578584553)

[13. Y Combinator @ycombinator https://twitter.com/ycombinator/status/1790808894207574051](https://
twitter.com/ycombinator/status/1790808894207574051)

[14. Y Combinator @ycombinator https://twitter.com/ycombinator/stat
us/1790838165550563816](https://twitter.com/ycombinator/status/1790838165550563816)

[15. Google @google https://twitter
.com/google/status/1790763743556632868](https://twitter.com/google/status/1790763743556632868)

[16. Google @google http
s://twitter.com/google/status/1790809723840651398](https://twitter.com/google/status/1790809723840651398)

[17. Google @
google https://twitter.com/google/status/1790855212950753605](https://twitter.com/google/status/1790855212950753605)

[1
8. Sam Altman @sama https://twitter.com/sama/status/1790816449180876804](https://twitter.com/sama/status/179081644918087
6804)

[19. Sam Altman @sama https://twitter.com/sama/status/1790817315069771959](https://twitter.com/sama/status/179081
7315069771959)

[20. Sequoia Capital @sequoia https://twitter.com/sequoia/status/1790821953969996131](https://twitter.co
m/sequoia/status/1790821953969996131)

[21. NVIDIA AI Developer @NVIDIAAIDev https://twitter.com/NVIDIAAIDev/status/1790
796553566716132](https://twitter.com/NVIDIAAIDev/status/1790796553566716132)

[22. NVIDIA AI Developer @NVIDIAAIDev http
s://twitter.com/NVIDIAAIDev/status/1790834544356040810](https://twitter.com/NVIDIAAIDev/status/1790834544356040810)

[23
. NVIDIA AI Developer @NVIDIAAIDev https://twitter.com/NVIDIAAIDev/status/1790849638418841919](https://twitter.com/NVIDI
AAIDev/status/1790849638418841919)

[24. Yann LeCun @ylecun https://twitter.com/ylecun/status/1790708256127545804](https
://twitter.com/ylecun/status/1790708256127545804)

[25. Yann LeCun @ylecun https://twitter.com/ylecun/status/17908393895
69880330](https://twitter.com/ylecun/status/1790839389569880330)

[26. Yann LeCun @ylecun https://twitter.com/ylecun/sta
tus/1790895062148137470](https://twitter.com/ylecun/status/1790895062148137470)

[27. Greg Brockman @gdb https://twitter
.com/gdb/status/1790839201312731462](https://twitter.com/gdb/status/1790839201312731462)

[28. Greg Brockman @gdb https:
//twitter.com/gdb/status/1790869434174746805](https://twitter.com/gdb/status/1790869434174746805)

[29. a16z @a16z https
://twitter.com/a16z/status/1790856759504244953](https://twitter.com/a16z/status/1790856759504244953)

[30. a16z @a16z ht
tps://twitter.com/a16z/status/1790856761169297598](https://twitter.com/a16z/status/1790856761169297598)

[31. a16z @a16z
 https://twitter.com/a16z/status/1790895186228420880](https://twitter.com/a16z/status/1790895186228420880)

[32. Google 
AI @googleai https://twitter.com/googleai/status/1790806911937560938](https://twitter.com/googleai/status/17908069119375
60938)

[33. Google AI @googleai https://twitter.com/googleai/status/1790811954329624853](https://twitter.com/googleai/s
tatus/1790811954329624853)

[34. Google AI @googleai https://twitter.com/googleai/status/1790872932681699764](https://tw
itter.com/googleai/status/1790872932681699764)

[35. Google AI @googleai https://twitter.com/googleai/status/17908783224
66922499](https://twitter.com/googleai/status/1790878322466922499)

[36. Google AI @googleai https://twitter.com/googlea
i/status/1790878324845076790](https://twitter.com/googleai/status/1790878324845076790)

[37. Google AI @googleai https:/
/twitter.com/googleai/status/1790878326967468045](https://twitter.com/googleai/status/1790878326967468045)

[38. Google 
AI @googleai https://twitter.com/googleai/status/1790878329395937773](https://twitter.com/googleai/status/17908783293959
37773)
```
---

     
 
all -  [ Experiment and test the reliability of different LLMs in prod and pre-prod! ](https://www.reddit.com/r/LangChain/comments/1ct4m4z/experiment_and_test_the_reliability_of_different/) , 2024-05-17-0910
```
**TLDR: I made a platform to make it easy to switch between LLMs, find the best one for your specific needs, analyze the
ir performance, and test different providers in production. Check it out at** [**optimix.app**](https://optimix.app/?lan
g)

Figuring out whether or not you should switch to Llama 3, Gemini 1.5 Flash, or GPT-4o can be hard. And knowing if th
e prompt change you just made will be good or bad is even harder.

A key focus of Optimix is to make experimentation eas
y. You can run A/B tests and other experiments to figure out how your changes impacted your core metrics like cost, spee
d, and user satisfaction. You can also test and compare different models in our playground and make requests through our
 API.

It also dynamically selects the most suitable model for each request, and helps manage fallbacks for outages and 
rate limits. Facing an OpenAI outage? Switch to Llama 3. Need superior coding assistance? We can auto switch you to the 
best one.

I'd love any feedback or suggestions on the platform, and hope this can be helpful for you all with all the n
ew models coming out!
```
---

     
 
all -  [ Can I use LangChain to only give me the context is found from the retrieval? ](https://www.reddit.com/r/LangChain/comments/1csy9ul/can_i_use_langchain_to_only_give_me_the_context/) , 2024-05-17-0910
```
I'm building an app with Next.js. 

Is it possible to have LangChain only give me the context it found from the vector s
tore? I then want to take this context and manually insert it into another part of my app that's using an llm as a part 
of the message history (but I don't want to do this final step in LangChain)

So I don't want LangChain to give me the f
inal output just the context is found using the vector store and OpenAi embedding model.

I'm still learning sry if this
 a stupid question. 

I'm having issues streaming output from LangChain to the front end and want to use something else 
I already have setup
```
---

     
 
all -  [ Any example of using llm.bind_tool ? i get not implemented error - want to run tools w GPT-4o ](https://www.reddit.com/r/LangChain/comments/1csvh8w/any_example_of_using_llmbind_tool_i_get_not/) , 2024-05-17-0910
```
Thanks
```
---

     
 
all -  [ How can I use LangChainJs to fill out csv file according to big context and prompt? ](https://www.reddit.com/r/LangChain/comments/1csts7q/how_can_i_use_langchainjs_to_fill_out_csv_file/) , 2024-05-17-0910
```
I am currently working on a project where I need to fill documents (CSV files) according to requirements in a big compen
dium (800+ pages PDF).

for example:

* context:
   * the PDF compendium of 800 pages with instructions and detailed leg
al requirements to be met when implementing infrastructure projects in IT sector
* CSV file:
   * a checklist-style CSV 
file containing the short name of the subject from the PDF compendium and columns to input things to be checked and proc
essed by a person (or in this case: AI)

|Subject|Responsible|Price|Risks|
|:-|:-|:-|:-|
|A.1.1.|Author of this file|$20
.000|If not done, we are doomed|

* Prompt
   * 'I want to add a exchange a router in Building C3.'
   * 'I want to add 
a gitlab server to our network'

In both cases, the output should be a CSV file or CSV text .

**These are the models im
 using (and liking):**

* model: wizardlm2:7b
* embedding model: mxbai-embed-large

**What I have done so far**

* readi
ng in the pdf files
* embedding the pdf files
* reading in the csv file
* embedding the csv file (<- is this correct?)
*
 created a prompt

\`\`\`  
Fill the csv file in the context with valuable data found in the embeddings according to the
 question.

Do not guess, do not add anything. Use only the context.

{context}

Question: {input}

\`\`\`

**What is no
t working. AKA: What is my question?**

The output the model is giving me is unstructured and has nothing to do with the
 CSV file I put into the context.

Is there a way that I can make the AI

1. Read in PDFs
2. Read in CSV
3. Listen to th
e prompt
4. Output a CSV file or (- like text)  I gave it with data from the embedded PDFs correctly according to the ne
eds arising from the input prompt

?
```
---

     
 
all -  [ LLM Orchestration framework or own python code, which is better? ](https://www.reddit.com/r/LangChain/comments/1cstpmx/llm_orchestration_framework_or_own_python_code/) , 2024-05-17-0910
```
i need a suggestion on a situation at work.

I am writing code for an application. i have 2 options, that is, either cho
ose an existing python framework that is available in the market or write my own python code.

Existing framework: LangC
hain, LlamaIndex

Pros:

1.	used a lot outside in the market. just in case if i want to shift another company. i can eas
ily adapt and can earn more money

2.	I can create Agents (AI) with little ease as i dont have to implement everything f
rom scratch (usually research work and strategies are implemented in this framework). implementing features becomes fast
er

3.	as knowledge workers are more aware of this framework - hiring them and getting them to understand the code becom
es easy 

Cons:

1.	So many abstractions in this framework and i fully dont understand it. few months back i tried to us
e this framework and i couldn't customize it for our situation. I am worried if i use this and make some progress and la
ter realize that it is not customizable. i will be screwed. lot of work will be wasted.

Own Code:

Pros:

1.	i can impl
ement all the functionalities by myself. i can design code base and write everything from scratch. this skill is valued 
in lot of places especially in startups as you have literally implemented lot of things from scratch. this way i can get
 a hang over the language and my skill improves drastically

2.	i get to do research and implement them with my own code
.

3.	i can customize it for my specific scenario

4.	the company will have a lot of dependency on me 

Cons:

1.	lot of
 work

2.	development might not be as fast paced as i would have liked it to be.

3.	i might get stuck and not find any 
solution as i am the only person available who has knowledge on this in this company.

Any suggestions are appreciated.





```
---

     
 
all -  [ Open AI APIs are the only reliable APIs in production ](https://www.reddit.com/r/LangChain/comments/1csrtc3/open_ai_apis_are_the_only_reliable_apis_in/) , 2024-05-17-0910
```
After having worked with Anthropic API and Gemini 1.5 Pro & Flash APIs. OpenAI API seems to be the only reliable API ser
vice available.   
With Anthropic - I am unable to add credits to their console, even after multiple mails to the custom
er support I have received no resolution. So I finally have to give up hope and just use Open AI.  
With Google Gemini -
 The APIs are absolutely unreliable, you are not sure when the APIs will return an answer and when they will not. I keep
 encountering error from the API something like: StopCandidateException: finish\_reason: RECITATION  
So again no point 
in using Gemini, just switch to Open AI.

Hoping this experience will benefit the community.

Anyone else having these i
ssues.
```
---

     
 
all -  [ Guidance needed regarding Anything LLM ](https://www.reddit.com/r/MistralAI/comments/1cspnl8/guidance_needed_regarding_anything_llm/) , 2024-05-17-0910
```
Hi Everyone,

I'm using AnythinLLM for developing a ChatBot for my organization. The thing is due to some infosec concer
ns we're not using any Online/API based or cloud based solutions.

We're using AnythinLLM as our ChatBot tool to use it 
locally,but the problem I'm facing is that my LLMs are showing too much hallucination no matter how much prompt engineer
ing i do. I want him to answer from the provided context (data) only but everytime it give me irrelevant extra informati
on and very long answers. In short it is not following my prompt.

But the main thing is i have tried different local mo
dels such as Llama3, OpenHermes2.5 (8Q), Mistral-7B (8Q), Phi-3 but none of them performed well. I have developed my mod
el using open hermes2.5 on Vscode using langchain as well and it's performing relatively well and answering me from my p
rovided context. But when i use anythingLLM it always give me answer from its external knowledge even though I'm using Q
uery mode.

Sometime on anythingllm even before uploading a data i query it like **Hello** for that it also provide me s
ome irrelevant response and sometime Don't even provide response.

The stack I'm using on Anythingllm 

- LanceDB
- Anyt
hingllm preferred Embeddings model
- Local LLMs using Ollama
- Context window (4096)
- Query Mode
- Chunk Size (500)
- O
verlap (50)
- Temperature (0.5)

Prompt :
***You have been provided with the context and a question, try to find out the
 answer to the question only using the context information. If the answer to the question is not found within the contex
t, return 'I don't know' as the response. Use three sentences maximum and keep the answer concise.***


I have checked t
he similar chunks retrieved from the retrieval and answer is present in that retrieved chunks but answer provided by the
 model is not from that chunks it's making up answers.

Any help or guidance regarding this will be highly appreciated.
```
---

     
 
all -  [ What's the best approach to building a model to match Job Titles to Standardized Roles Using NLP? ](https://www.reddit.com/r/learnmachinelearning/comments/1cspfbh/whats_the_best_approach_to_building_a_model_to/) , 2024-05-17-0910
```
A small part of my job involves getting a client's dataset of employees, and mapping their positions to a list of standa
rdised titles, based on the roles' title, the assumed positoin in the hierarchy, and the salary. For example, something 
like 'Finance Assistant' would be mapped to our standardised role 'Accounts Clerk', or a 'Helpdesk Agent' might be mappe
d to our 'Customer Care Agent' role. 



I have a CSV file with 280 standardised titles as well as a brief description o
f each one. Although the past data is not so accurate, I also have past mappings of company titles to each standardised 
role. 

  
I'm currently exploring the best approach for this task. Previously, I was advised against using an LLM for t
his, but I've since learned about Retrieval-Augmented Generation (RAG) and wonder if it might be applicable here. I’m co
nsidering using BERT, but I'm open to suggestions for more advanced models if they offer better accuracy.

  
Here are s
ome ideas I've thought of and come across

1. Using BERT (uncased or large) for semantic understanding and *maybe* GPT-3
 embeddings more contextual understanding (could help given similar roles, e.g. a Compliance Officer is not the same as,
 say, a Supply Chain Officer). The goal is to achieve a high level of accuracy in mapping.
2.  Considering using some ki
nd of RAG (perhaps through Langchain) to additional contextual information from the descriptions.

Are there other model
s or approaches that might be better suited for this kind of semantic and contextual matching? Looking forward to feedba
ck.


```
---

     
 
all -  [ Need trivial help with RAG: how do I programmatically handle the case in which the Q&A Chain's retri ](https://www.reddit.com/r/LangChain/comments/1csohun/need_trivial_help_with_rag_how_do_i/) , 2024-05-17-0910
```
I'm sorry for the trivial question, but I've been struggling with this and cannot find a solution. 

I have a retrieval 
with a list of questions and answers, and I have a chain defined, but im struggling to properly handle the case in which
 the question being asked by the user doesn't exist in my vector store (or even in a simplified system, where a 5 questi
ons and their answers are added in the prompt - without a vectorstore and retrieval) 

Thanks a lot in advance :)
```
---

     
 
all -  [ LLM model with timezone issue ](https://www.reddit.com/r/LangChain/comments/1csobxi/llm_model_with_timezone_issue/) , 2024-05-17-0910
```
issue: I am build RAG chat bot and my model is taking server time zone when i ask what is current date and time how fix 
it ?
```
---

     
 
all -  [ Message and Prompt Classes -- are they helpful? ](https://www.reddit.com/r/LangChain/comments/1csmlwe/message_and_prompt_classes_are_they_helpful/) , 2024-05-17-0910
```
I hope I do not sound like a jerk here, but ... more and more I feel that these classes are more trouble than they are w
orth.  I'd welcome it if someone made a case for their existence.

Here's the claim: we are (almost?) always better off 
just working with f-strings and format instead of working with these classes.  Here is my rationale:

* Concatenation:  
Most recently, I have been fighting with trying to concatenate various \`Message\` and \`PromptTemplate\` classes.  Some
times this works, sometimes it fails at runtime. This is made worse by the fact that static type-checking doesn't detect
 this prior to runtime.
* Type hints: the above illustrates a problem with these classes that extends beyond them and is
 pervasive in Langchain. There are a lot of type hints, and there are type failures, but the type hints don't help.  The
 type specifications are often so loose that type checking tools cannot warn me about errors to come.  This is related t
o another pervasive problem:
* The use of opaque objects and loose typing causes many problems in development with Langc
hain. When I try to write my own code to extend langchain behavior I often find that I have to handle many cases that ha
ve the potential to cause errors because of loose typing. For example, anything handling input going into an `LLM` or `C
hatModel` must handle `PromptValue`, `str`, `Sequence` of `MessageLikeRepresentation` and `dict` s with unknown sets of 
keys. When I process those `Sequence`s I must then deal with `BaseMessage`, `str`, `Tuple[str,str]` and `Dict[str, Any]`
.  I apologize for being cranky, but these type hints seem more aimed at ensuring that type checkers never raise errors,
 rather than aimed at helping the programmer write correct code.  The type checker is a tool, not an oracle to be worshi
pped.
* `PromptTemplate`s work extremely poorly when they must accommodate code as template-fillers.  The curly braces i
n code confuse prompt handling no end.

Looping back to the hypothesis: If I try to assemble a prompt in stages by plugg
ing values in over and over, the use of `PromptTemplate` and `Message` objects makes my life more difficult and costs me
 hours of debugging.  My recent alternative is simply to assemble together ordinary strings, using `format` as necessary
, until the last minute before they are needed, at which time I wrap them in `PromptTemplate.from_template()` so that th
ey can be put in an LCEL chain expression.

IMO this indicates that the layers and layers of complex types and meta-clas
ses are more trouble than they are worth.  I'm willing -- indeed hoping! -- that someone will prove me wrong.  How does 
my experience align with that of other langchain users?
```
---

     
 
all -  [ Dall-E Api low quality images ](https://www.reddit.com/r/LangChain/comments/1csmium/dalle_api_low_quality_images/) , 2024-05-17-0910
```
I use Dall-E as a tool for my langchain agent but the quality of the images are so low compared to the images from the C
hatGPT Interface.

Is there a way to fix this?


```
---

     
 
all -  [ RAG chat over OpenAI APIs, the OpenAI sandbox, and the OpenAI forums ](https://www.reddit.com/r/OpenAIDev/comments/1csko4c/rag_chat_over_openai_apis_the_openai_sandbox_and/) , 2024-05-17-0910
```
LangChain has a great chat interface called 'Langchain Chat' for interacting with the langchain docs.

I want something 
similar: I'd like to chat with a recent, powerful LLM that is endowed with RAG populated with up-to-date information on 
the OpenAI APIs, the OpenAI sandbox, and the OpenAI forums. I want this so I can more quickly assess the state of the ar
t in terms of what is available.

Does this exist or do I need to build it?

Also, BTW do you know a name (or could you 
propose a name) for this 'RAG over the docs and forums?' Maybe APIDocRag? I'm just really wishing that we had a term wit
h 'unique google-ability' to find out if company or product XYZ had this obvious service

Clarification: this is NOT a r
equest for an open source chat library that can interact with the API.
```
---

     
 
all -  [ Text-to-SQL conversion for ETL testing using Snowflake ](https://www.reddit.com/r/LLMDevs/comments/1csjztr/texttosql_conversion_for_etl_testing_using/) , 2024-05-17-0910
```
Hi,

I have to do a POC and below are the steps or direction how to implement using Langchain and Snowflake DB and LLM
—
—————
1. User will enter the Transformation Logic sheet where every row will have the logic how the values inside the So
urce Table are mapped/modified to Target Table.
2. User will also have access to Target Table to check whether the SQL q
uery generation using Transformation logic correctly mapped the values to Target table or not.

I have tried using excel
 sheet and a basic table in ChatGPT and I was able to accomplish upto good level.
I want to know how to implement in pyt
hon and is there any good LLM for such text-sql conversion.
Many thanks
```
---

     
 
all -  [ Utilizing both LlamaIndex and LangChain ](https://www.reddit.com/r/LocalLLM/comments/1csiykw/utilizing_both_llamaindex_and_langchain/) , 2024-05-17-0910
```
Hello Dear fellow,

I'm currently new in this domain and was exploring multiple possibilities in RAG. 

I'm curious whet
her we can use both LlamaIndex and LangChain in parallel like utilizing Llama Index for indexing and retriever purpose a
nd other operations on LangChain 

If yes, what will be its impact on performance of overall application
```
---

     
 
all -  [ Need help with Langchain & vercel generative UI integration ](https://www.reddit.com/r/LangChain/comments/1csicrm/need_help_with_langchain_vercel_generative_ui/) , 2024-05-17-0910
```
Hi everyone, I've built a pdf-chatbot using langchain and pinecone db. I'm further planning to integrate vercel's latest
 generative UI feature   [https://chat.vercel.ai/](https://chat.vercel.ai/)  ( [https://github.com/vercel/ai-chatbot](ht
tps://github.com/vercel/ai-chatbot) ). 

so here's the flow:   
1. User should be able to upload multiple pdf's  
2. All
 the pdf's will be stored in pinecode vector Storage  
3. User will be able to prompt and based on the prompt the AI wil
l call generative UI like interactive quizes etc via react server components

  
Can anyone help me with how to integrat
e langchain  with streamUI from vercel SDK?  [https://sdk.vercel.ai/docs/reference/ai-sdk-rsc/stream-ui](https://sdk.ver
cel.ai/docs/reference/ai-sdk-rsc/stream-ui)
```
---

     
 
MachineLearning -  [ [R] Building an Observable arXiv RAG Chatbot with LangChain, Chainlit, and Literal AI ](https://www.reddit.com/r/MachineLearning/comments/1crwh0q/r_building_an_observable_arxiv_rag_chatbot_with/) , 2024-05-17-0910
```
Hey r/MachineLearning, I published a new article where I built an observable semantic research paper application.

This 
is an extensive tutorial where I go in detail about:

1. Developing a RAG pipeline to process and retrieve the most rele
vant PDF documents from the arXiv API.
2. Developing a Chainlit driven web app with a Copilot for online paper retrieval
.
3. Enhancing the app with LLM observability features from Literal AI.

You can read the article here: [https://medium.
com/towards-data-science/building-an-observable-arxiv-rag-chatbot-with-langchain-chainlit-and-literal-ai-9c345fcd1cd8](h
ttps://medium.com/towards-data-science/building-an-observable-arxiv-rag-chatbot-with-langchain-chainlit-and-literal-ai-9
c345fcd1cd8)

Code for the tutorial: [https://github.com/tahreemrasul/semantic\_research\_engine](https://github.com/tah
reemrasul/semantic_research_engine)


```
---

     
 
MachineLearning -  [ [P] LLMinator: A Llama.cpp + Gradio based opensource Chatbot to run llms locally(cpu/cuda) directly  ](https://www.reddit.com/r/MachineLearning/comments/1cpbgd1/p_llminator_a_llamacpp_gradio_based_opensource/) , 2024-05-17-0910
```
Hi I am currently working on a context-aware streaming chatbot based on Llama.cpp, Gradio, Langchain, Transformers. LLMi
nator can pull LLMs directly from HF & run them locally on cuda or cpu.

I am looking for recommendations & help from op
ensource community to grow this further.

**Github Repo:** [https://github.com/Aesthisia/LLMinator](https://github.com/A
esthisia/LLMinator)

**Goal:** To help developers with kickstarter code/tool to run LLMs.

https://preview.redd.it/fnzja
7rjwqzc1.png?width=1846&format=png&auto=webp&s=a62c43614d63e82156fef8722b986b051cc1795b

**Features:**

* Context-aware 
Chatbot.
* Inbuilt code syntax highlighting.
* Load any LLM repo directly from HuggingFace.
* Supports both CPU & Cuda m
odes.
* Load & Offload saved models.
* Command Line Args
* API Access(Soon to be available)

Any review or feedback is a
ppreciated.
```
---

     
 
MachineLearning -  [ [D] Self-optimizing deterministic LLM memory using dspy, neo4j and vector databases. Need your input ](https://www.reddit.com/r/MachineLearning/comments/1cakjaf/d_selfoptimizing_deterministic_llm_memory_using/) , 2024-05-17-0910
```
Hey there, Redditors!

I'm back with the latest installment on creating deterministic LLM memory.

If you've been follow
ing along, you know I'm on a mission to move beyond the '[thin OpenAI wrapper](https://topoteretes.github.io/cognee/blog
/2023/10/05/going-beyond-langchain--weaviate-and-towards-a-production-ready-modern-data-platform/)' trend and tackle the
 challenges of building robust LLM memory.

  
That's why we built cognee, a python library to process documents and bui
ld knowledge graphs on top of them.

After a few weeks of work, we integrated DSPy and extended cognee.

Here is brief o
verview of the logic: 

[Architecture overview](https://preview.redd.it/fcs3lifx53wc1.png?width=1380&format=png&auto=web
p&s=9316cba52147a5b764565b8438f3f143d8e7ac84)

We aim to understand:

1. Have you tried building knowledge graphs with o
ther tools before?

2. If so, what were the biggest obstacles?

3. How would you approach semantic linking of documents 
without knowledge graphs?

*Remember to give this post an upvote if you found it insightful!*  
*And also star our* [Git
hub repo](https://github.com/topoteretes/cognee)
```
---

     
 
deeplearning -  [ Seeking Advice: Solving Data Challenges with Large Language Models (LLMs) ](https://www.reddit.com/r/deeplearning/comments/1ca4nc1/seeking_advice_solving_data_challenges_with_large/) , 2024-05-17-0910
```
Hi all

I am presented with a problem that I need to solve using LLM to get the right data from text that has only \~20%
 structure to it. Here's a sample data

XXXXX

AA          BB

CCCC:  (optional DDDD)

C1......(A1) (B1)

C2......(A2) (
B2)

C3.....(A3) (B3)

I am required to anwer with either of these results from A1/B1 till A3/B3 pairs but in order to d
o that I need to go back and ask the user which one of the options C1 to C3 applies to him?

The above is not the most c
omplex structure, it increases in complexity from here so a lot of chatting with user is required to get to the right da
ta that will always exist in the chunk like above.

In the most simplist case the data structure will look like below

X
XXXX

AA          BB

CCCC: ......(A1) (B1)



How would you build a system like this? I am looking at multi-agent syste
ms with Langchain, what about prompt chaining?
```
---

     
 
deeplearning -  [ Share the Coolest Out of The Box LLM Applications That Made You Say 'Wow that was smart' ](https://www.reddit.com/r/deeplearning/comments/1c9e6dj/share_the_coolest_out_of_the_box_llm_applications/) , 2024-05-17-0910
```
Hi, I'm looking at some LLM applications today but apart from guys doing big rags with langchain I don't see too many us
es that are out of the box or that make me say 'wow that was smart to use an LLM here'. Have you seen any cool stuff usi
ng LLMs recently that made you say 'wow, that was smart'?
```
---

     
