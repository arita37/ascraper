 
all -  [ OpenAI Content Filter when using MapReduce ](https://www.reddit.com/r/LangChain/comments/1dhl76g/openai_content_filter_when_using_mapreduce/) , 2024-06-17-0955
```
Using Langchain v0.2, model is limited to gpt-3.5-turbo with Azure (environment provided by the client)

Hello!

Looking
 for some directions on where to read or how to proceed to solve the following situation:

I have very big texts that I 
want to summarize. In the past I had read about MapReduce with Langchain so I tried with it. I am creating chunks of tex
ts and processing them. It works, but when something in a chunk triggers the OpenAI content filter, the summarization fo
r the whole chunk fails. I was wondering if there is a way to keep processing the chunk in order to get a result for the
 parts of the chunk that didn't have issues with the content filter. Otherwise, I'd have to implement the MapReduce myse
lf.

I'd appreciate if you could point me to some documents, or if you could suggest how I may approach this problem.

 
 
Thank you very much in advance.
```
---

     
 
all -  [ Roast my CV ](https://www.reddit.com/gallery/1dhh4jx) , 2024-06-17-0955
```

```
---

     
 
all -  [ Dealing with Incomplete Structured Output? ](https://www.reddit.com/r/LangChain/comments/1dhe1es/dealing_with_incomplete_structured_output/) , 2024-06-17-0955
```
I have a use case where I generate a json output. The json is sometimes so large that it gets over the output range capa
bility of my llm, rendering my structured output not parseable. What method you guys apply when faced with an incomplete
 Structured output?
```
---

     
 
all -  [ Create your AI SaaS for chatbot building in just one day!
 ](https://www.reddit.com/r/WebDeveloperJobs/comments/1dhdw94/create_your_ai_saas_for_chatbot_building_in_just/) , 2024-06-17-0955
```
Many people are struggling to start a SaaS business. So, I've created a chatbot builder API that does all the AI work fo
r your new SaaS. You can just integrate it into your website and start earning money from your customers. My API can be 
trained on multiple data types, like PDFs, Word documents, YouTube videos, and websites, using GPT-4 and Gemini models. 
The API built on GPT, Gemini, Pinecone, Serverless Pinecone, Langchain,..

The API will cost just $99! One time payment 
and you will receive the full system code!

If you're interested, DM me to get started building your SaaS!
```
---

     
 
all -  [ Suggesting which RAG method will work best for you, based on your use case 🔎📑  ](https://www.reddit.com/r/LangChain/comments/1dh79xx/suggesting_which_rag_method_will_work_best_for/) , 2024-06-17-0955
```
Most RAG apps use Dense Passage Retrieval to find relevant docs. But there are better methods:

1. RAG-Token:

It genera
tes each token by considering different docs and chooses the most probable token at each step. So that every part of the
 answer is influenced by the best possible context.

2. RAG-Sequence:

It calculates the probability of each answer and 
selects the one with the highest combined probability, getting you the best possible answer based on multiple sources. I
t’s a lot like RAG-token but less granular.

3. Fusion-in-Decoder (FiD):

It encodes all pairs of questions and chunks i
n parallel and then combines these encodings before feeding them into the decoder, which generates the answer step-by-st
ep.

4. Graph RAG:

In case your documents are highly interconnected, the links between them are probably important to g
enerate a relevant response.

Search results from Graph RAG are more likely to give you a comprehensive view of the enti
ty being searched and the info connected to it.

I spent the weekend creating a Python library which automatically creat
es this graph for the documents present in your vectordb. It also makes it easy for you to retrieve relevant documents c
onnected to the best matches.

Currently testing the library on medical documents to gauge its performance.

Sharing ver
sion 0.1 tomorrow! You can follow my social media to stay tuned: [https://linktr.ee/sarthakrastogi](https://linktr.ee/sa
rthakrastogi)


```
---

     
 
all -  [ Determinism control ](https://www.reddit.com/r/LangChain/comments/1dh5qr2/determinism_control/) , 2024-06-17-0955
```
Im trying to get my workflow to be accurate and help me give the same response every time.

I have temp set to zero. bas
e prompt bossing the model around to be 'deterministic' but you can see, i still have wildly different outputs each time
 thing thing runs.

any advice on getting this to be more accurate?

https://preview.redd.it/ibu2ivj68x6d1.png?width=190
8&format=png&auto=webp&s=47bd31b849fa690dc12e11cc9604702587aae6fa

base prompt: You are a deterministic GPT model design
ed to analyze a list of transactions in a SQL table. Your task is to provide the same response every time you are asked 
the same question. Follow these guidelines to ensure determinism:

1. Always follow the exact format provided in the exa
mples below.
2. Provide responses based strictly on the information available in the given table.
3. Do not include any 
additional or inferred information.
4. Ensure the order of transactions is consistent based on the primary key or specif
ied order.

Note: the actual correct answer is 106 items. the SQL has 2,000 lines on it
```
---

     
 
all -  [ Passing API Key via URL Params ](https://www.reddit.com/r/LangChain/comments/1dh3fq8/passing_api_key_via_url_params/) , 2024-06-17-0955
```
Hi there!  
  
I am trying to query an api with its auth value as its get parameter   
[https://test.com/?key=apikey](ht
tps://test.com/?key=apikey)   
How do I tell the Langchain agent to pass an additional url param? (in this case, key) in
 every requests?

This is how it is executed atm. Thanks in advance <3

    model = Chat(model='claude-3-haiku-20240307'
, api_key=CLAUDE_API_KEY)
    weather_agent = planner.create_openapi_agent(
        MY_OPENAPI_SPEC,
        RequestsWra
pper(),
        llm=model,
        allow_dangerous_requests=True
    )
```
---

     
 
all -  [ ERROR: pip's dependency resolver  ](https://www.reddit.com/r/FaceFusion/comments/1dh2zu3/error_pips_dependency_resolver/) , 2024-06-17-0955
```
https://preview.redd.it/oq5moytn7w6d1.png?width=1211&format=png&auto=webp&s=17fe145a3e0ae18aca4eda9c2ac2978c42bb2cb9

I 
did everything before it almost flawlessly, and now when I do python install.py. it shows this.

I tried various methods
 hoping to fix this problem

upgrading the pip

installing the dependencies myself

and fixing some codes in the .py ( d
idn't work so I recovered it

  
but now I really have no other ideas to fix this, I need your help
```
---

     
 
all -  [ Please review my Resume. Don't have any offers yet ](https://www.reddit.com/r/Resume/comments/1dh1hfu/please_review_my_resume_dont_have_any_offers_yet/) , 2024-06-17-0955
```
https://preview.redd.it/q8dfqp2aov6d1.jpg?width=1275&format=pjpg&auto=webp&s=6b7e6392ee8eb79d53349eac7d18eddc08759535

h
ttps://preview.redd.it/h8ffm4acov6d1.jpg?width=1275&format=pjpg&auto=webp&s=835b85d481ee25e79d6f94646e238e0d9f09ad60


```
---

     
 
all -  [ Please review my Resume. Don't have any offers yet ](https://www.reddit.com/r/developersIndia/comments/1dh1bj2/please_review_my_resume_dont_have_any_offers_yet/) , 2024-06-17-0955
```
https://preview.redd.it/b0n4g6izlv6d1.jpg?width=1275&format=pjpg&auto=webp&s=de76a6165f59fbc9d18924eb26796a9cb7d095a3


```
---

     
 
all -  [ Please review my Resume. Don't have any offers yet ](https://www.reddit.com/r/resumes/comments/1dh18d3/please_review_my_resume_dont_have_any_offers_yet/) , 2024-06-17-0955
```
https://preview.redd.it/b9vhtwowkv6d1.jpg?width=1275&format=pjpg&auto=webp&s=f6df4a4e647d3de7331903ac184b58135befa9f5

h
ttps://preview.redd.it/rexnwyowkv6d1.jpg?width=1275&format=pjpg&auto=webp&s=8503335ba04cc4a0321fb6500f0e4bd153e03bcf


```
---

     
 
all -  [ We are on TV! 📺 👏 ](https://i.redd.it/qtxv6pp0jv6d1.png) , 2024-06-17-0955
```
Excellent work by some passionate guy!
I admire his work towards his passion.
```
---

     
 
all -  [ Any learning Group for LangGraph? ](https://www.reddit.com/r/LangChain/comments/1dgxdvq/any_learning_group_for_langgraph/) , 2024-06-17-0955
```
Because langchain/langgraph example and tutorial is sxcking, I beleieve many people agree that. such [Am I the only one 
who feels LangGraph documentation and tutorials by lanfchain absolutely sxck?](https://www.reddit.com/r/LangChain/commen
ts/1d4lwt0/am_i_the_only_one_who_feels_langgraph/)

for example, all examples are openai related llm interface and hard 
to convert to local such ollama.  
This makes me even a [simple hello world](https://github.com/HomunMage/AI_Agents/blob
/main/LangChain/Hello%20World.py) need hours to coding it.

That is why I had crate a [GUI for CrewAI](https://github.co
m/HomunMage/CrewAI-GUI) , not a gui for langchain or langgraph. But I think learning langgraph still important.

I want 
to find or build a langgraph learning group. And also want to build a LangGraph-GUI
```
---

     
 
all -  [ Grafana + Ollama ](https://www.reddit.com/r/ollama/comments/1dguvr8/grafana_ollama/) , 2024-06-17-0955
```
What's the best way to integrate Ollama with Grafana (e.g. have Ollama summarize logs/dashboards/etc.)?  It looks like t
here is an LLM plugin for Grafana, but it appears to not support Ollama (https://github.com/grafana/grafana-llm-app/issu
es/162).

  
Would trying to feed the grafana API spec to Ollama and using langchain to query the API be the most straig
ht-forward approach?  
```
---

     
 
all -  [ save and load embeddings  ](https://www.reddit.com/r/LangChain/comments/1dgpc6w/save_and_load_embeddings/) , 2024-06-17-0955
```
i used chromadb with langchain to create embeddings. i used persistent\_directory to save those locally and it did but n
ow i am not able to load them. these are the codes

#saving embeddings

vector\_storage=Chroma.from\_documents(split,Oll
amaEmbeddings(model='nomic-embed-text'), persist\_directory='vector\_store',collection\_name='qna\_embeddings')

#loadin
g embeddings

vector\_store2=Chroma(persist\_directory='vector\_store',embedding\_function=OllamaEmbeddings(model='nomic
-embed-text'))

to check i printed the following and it gives 0 as output

print(vector\_store2.\_collection.count())

p
ls help me 
```
---

     
 
all -  [ Create your AI SaaS for chatbot building in just one day!
 ](https://www.reddit.com/r/EntrepreneurRideAlong/comments/1dgnx88/create_your_ai_saas_for_chatbot_building_in_just/) , 2024-06-17-0955
```
Many people are struggling to start a SaaS business. So, I've created a chatbot builder API that does all the AI work fo
r your new SaaS. You can just integrate it into your website and start earning money from your customers. My API can be 
trained on multiple data types, like PDFs, Word documents, YouTube videos, and websites, using GPT-4 and Gemini models. 
The API built on GPT, Gemini, Pinecone, Serverless Pinecone, Langchain,..



The API will cost just $99! One time paymen
t and you will receive the full system code!



If you're interested, DM me to get started building your SaaS!
```
---

     
 
all -  [ [P] Seeking Feedback on My GenAI Job Fit Project - New to LangChain/LangGraph ](https://www.reddit.com/r/MachineLearning/comments/1dgns9p/p_seeking_feedback_on_my_genai_job_fit_project/) , 2024-06-17-0955
```
Hi all,

Soo, i have been working on a a projectcalled [GenAI Job Fit](https://github.com/DAVEinside/GenAI_Job_Fit). It'
s an AI-driven system designed to enhance job applications by providing tailored recommendations based on individual pro
files.

I'm relatively new to LangChain and LangGraph, and I've incorporated them into this project. I would greatly app
reciate it if you could check out the repository and provide any feedback or suggestions for improvement.

Your insights
 on how I can better implement LangChain/LangGraph, or any other aspect of the project, would be incredibly valuable. I'
m eager to learn and make this project as robust as possible.

Thank you in advance for your time and feedback!

Repo Li
nk : [https://github.com/DAVEinside/GenAI\_Job\_Fit](https://github.com/DAVEinside/GenAI_Job_Fit)
```
---

     
 
all -  [  AI-Driven Job Application Enhancement System - Seeking Feedback and Suggestions! ](https://www.reddit.com/r/LangChain/comments/1dgnmjt/aidriven_job_application_enhancement_system/) , 2024-06-17-0955
```
Hi everyone,

I've been working on a project that aims to enhance job applications using AI. It's called [GenAI\_Job\_Fi
t](https://github.com/DAVEinside/GenAI_Job_Fit), and I would love for you all to check it out. I took inspiration from t
he Agent-Supervisor example notebook provided.

The system leverages AI to analyze job descriptions and tailor resumes t
o match job requirements, increasing the chances of getting noticed by recruiters and ATS (Applicant Tracking Systems). 
Here are some key features:

* Automated resume tailoring
* Keyword optimization
* Compatibility scoring between job des
criptions and resumes

I'd really appreciate it if you could take a look and let me know what you think. I'm particularl
y interested in any suggestions for improvements or additional features that could make the tool even more useful.

Feel
 free to fork the repo, open issues, or submit pull requests. Your feedback will be invaluable in making this project be
tter!

Repo Link : [https://github.com/DAVEinside/GenAI\_Job\_Fit](https://github.com/DAVEinside/GenAI_Job_Fit)

Thank y
ou!
```
---

     
 
all -  [ How to work with large data that is returned from an api? ](https://www.reddit.com/r/LangChain/comments/1dgm1ij/how_to_work_with_large_data_that_is_returned_from/) , 2024-06-17-0955
```
Hello! Im using the APIchain i use it to get data from an api endpoint, the problem is that the api returns a largue amo
unt of data in json format (i need all the data that the api returns), i will then use a agent to ask questions about th
at data but since is so massive there's problems like the token amount or time it takes to analyze, can anyone giveme so
me tips about what can i do to better the performance or what to do to solve this kind of problem? thanks alot!!!

this 
is the apiChain im using:

llm = OpenAI(temperature=0)  
chain = APIChain.from\_llm\_and\_api\_docs(  
llm,  
open\_mete
o\_docs.OPEN\_METEO\_DOCS,  
verbose=True,  
limit\_to\_domains=\['https://api.open-meteo.com/'\],  
)  
chain.run(  
'W
hat is the weather like right now in Munich, Germany in degrees Fahrenheit?'  
)
```
---

     
 
all -  [ Roast My Resume, Masters in Computer Science and 1.5 Years of Relevant Experience, Not Receiving Any ](https://www.reddit.com/r/resumes/comments/1dgkgl9/roast_my_resume_masters_in_computer_science_and/) , 2024-06-17-0955
```
Just as the title says. Been working as a Full Stack Developer at a startup for the past 7 months at very undesireable t
erms. It was the only software-related job I could land after getting my Masters. I've changed the layout and content of
 my resume multiple times with them having no effect. I recognize that a lot of my job experience bullets do not have qu
antitative results, but I am not sure what to put for these when I do not know the exact results. Do people just estimat
e a number or percentage when doing this? Any feedback on my resume would be greatly appreciated. I am in the NYC metro 
area.

https://preview.redd.it/ih8mpic07r6d1.png?width=1258&format=png&auto=webp&s=18bef7888a55acf35a679797c6da55fe2ea1d
eaa

https://preview.redd.it/7eqt3dmz6r6d1.png?width=1282&format=png&auto=webp&s=cc762c6111f23ebac6ef4de5ee1a2f186c80bcf
c
```
---

     
 
all -  [ Create your AI SaaS for chatbot building in just one day! ](https://www.reddit.com/r/AiForSmallBusiness/comments/1dgik4p/create_your_ai_saas_for_chatbot_building_in_just/) , 2024-06-17-0955
```
Many people are struggling to start a SaaS business. So, I've created a chatbot builder API that does all the AI work fo
r your new SaaS. You can just integrate it into your website and start earning money from your customers. My API can be 
trained on multiple data types, like PDFs, Word documents, YouTube videos, and websites, using GPT-4 and Gemini models.

The API built on GPT, Gemini, Pinecone, Serverless Pinecone, Langchain,..

The API will cost just $99! One time payment 
and you will receive the full system code!

If you're interested, DM me to get started building your SaaS!
```
---

     
 
all -  [ What’s Memory Tuning and how does it give higher accuracy + speed than RAG and prompting? ](https://www.reddit.com/r/LangChain/comments/1dgi0vj/whats_memory_tuning_and_how_does_it_give_higher/) , 2024-06-17-0955
```
First, how it works:

- Memory Tuning fine-tunes millions of LoRA adapters (memory experts) on any open-source LLM to en
sure accurate fact recall.

- During inference, the model retrieves and integrates the most relevant experts, (a lot lik
e information retrieval). This gives much high accuracy and reduced hallucinations.

- This approach maintains the model
's ability to generalise — while at the same time focusing on zero error for specified facts.

Why is this better than R
AG?

RAG shifts probabilities without eliminating errors — while Memory Tuning fully corrects inaccuracies.

[Lamini](ht
tps://www.linkedin.com/company/lamini-ai/) released their Memory Tuning solution for enterprises with case studies showi
ng amazing accuracy boosts for text-to-sql, labelling, and even recommendation tasks.

Paper: [https://github.com/lamini
-ai/Lamini-Memory-Tuning/blob/main/research-paper.pdf](https://github.com/lamini-ai/Lamini-Memory-Tuning/blob/main/resea
rch-paper.pdf)



I share high quality AI updates and tutorials daily on my LinkedIn: [https://www.linkedin.com/in/sarth
akrastogi/](https://www.linkedin.com/in/sarthakrastogi/)

If you like this post and want to stay updated on latest AI re
search, you can check out: [https://linktr.ee/sarthakrastogi](https://linktr.ee/sarthakrastogi).


```
---

     
 
all -  [ Where Can I Find Deterministic Tools for AI Agents?  ](https://www.reddit.com/r/AI_Agents/comments/1dggm9v/where_can_i_find_deterministic_tools_for_ai_agents/) , 2024-06-17-0955
```
Hi guys,

I've started working on building my own AI Agent, but I'm finding that I have to create all the tools myself f
rom scratch. I'm a junior AI Engineer and it's a bit overwhelming, I'm finding that most of these tools are purely softw
are-based.

Does anyone know of any libraries that offer pre-built deterministic tools that I can use with my AI Agent?


I'm currently using some tools from Langchain, but they're not quite specific enough for what I need. Is anyone else fa
cing the same challenge, or is it just my lack of experience showing? 😅

Any help or recommendations would be greatly ap
preciated!

Thanks!
```
---

     
 
MachineLearning -  [ [P] I'm tired of LangChain, so I made a simple open-source alternative with support for tool using a ](https://www.reddit.com/r/MachineLearning/comments/1deffo8/p_im_tired_of_langchain_so_i_made_a_simple/) , 2024-06-17-0955
```
[https://github.com/piEsposito/tiny-ai-client](https://github.com/piEsposito/tiny-ai-client)

The motivation for buildin
g tiny-ai-client comes from a frustration with Langchain, that became bloated, hard to use and poorly documented - and t
akes inspiraton from [simpleaichat](https://github.com/minimaxir/simpleaichat/tree/main), but adds support to vision, to
ols and more LLM providers aside from OpenAI (Gemini, Anthropic - with Groq and Mistral on the pipeline.)

I'm building 
this to to continue what simpleaichat started and not to ride on hype, raise money or whatever, but to help people do 2 
things: build AI apps as easily as possible and switching LLMs without needing to use Langchain.

This is a minimally vi
able version of the package, with support to vision, tools and async calls. There are a lot of improvements to be done, 
but even at its current state, tiny-ai-client has generally improved my interactions with LLMs and has been used in prod
uction with success.

Let me know what you think: there are still a few bugs that may need fixing, but all the examples 
work and are easy to be be adapted to your use case.
```
---

     
 
MachineLearning -  [ [P] Superfast RAG: Langchain Streaming and Groq ](https://www.reddit.com/r/MachineLearning/comments/1d5s9g4/p_superfast_rag_langchain_streaming_and_groq/) , 2024-06-17-0955
```
  
Fast LLM RAG inference using Groq and Langchain Streaming.  
  
Groq is introducing a new, simpler processing archite
cture designed specifically for the performance requirements of machine learning applications and other compute-intensiv
e workloads. The simpler hardware also saves developer resources by eliminating the need for profiling, and also makes i
t easier to deploy AI solutions at scale.  
  
Resource: [https://www.youtube.com/watch?v=frMdOL8knqg](https://www.youtu
be.com/watch?v=frMdOL8knqg)
```
---

     
 
deeplearning -  [ How to finetune? ](https://www.reddit.com/r/deeplearning/comments/1daio0h/how_to_finetune/) , 2024-06-17-0955
```
Can someone guide me to some resource how can I finetune an open source llm or some library (like langchain) on unstruct
ured data (example: news articles on cricket) So that model can answer a question (like When did India won world Cup?)
```
---

     
