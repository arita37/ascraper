 
all -  [ Best open source document PARSER??!! ](https://www.reddit.com/r/LangChain/comments/1dicr6p/best_open_source_document_parser/) , 2024-06-18-0911
```
Right now I’m using LlamaParse and it works really well. I want to know what is the best open source tool out there for 
parsing my PDFs before sending it to the other parts of my RAG.  
```
---

     
 
all -  [ Ollama.chat python library  ](https://www.reddit.com/r/ollama/comments/1diajn3/ollamachat_python_library/) , 2024-06-18-0911
```
I can't seem to find any good documentation on this library, can anyone advise? I could use the langchain one I suppose.


My results with .chat we're basic, unable to feed a model or prompt when calling in python rather than using API. Woul
d appreciate tips 
```
---

     
 
all -  [ Formatting Retriever Outputs ](https://www.reddit.com/r/LangChain/comments/1diabgh/formatting_retriever_outputs/) , 2024-06-18-0911
```
So, I’m using a Neo4jVector.as_retriever() as a retriever for a chain.

The retriever outputs and array of Document type
 objects that gets used as a {context} in my prompt template.

What’s the appropriate way to format this output into a s
equence of string objects to be used in my prompt_template?

I’ve been looking into Runnables and just found out about R
unnableLambda and been thinking into turning a function into a Runnable just to format this retriever output, is this re
ally the way to go here? am I missing something?

Thanks in advance!


```
---

     
 
all -  [ Agents of Inference: my entry for the Generative AI Agents Developer Contest by NVIDIA and LangChain ](https://v.redd.it/0okttcxzc67d1) , 2024-06-18-0911
```

```
---

     
 
all -  [ Using RAG Agent got error with tools parameter ](https://www.reddit.com/r/LangChain/comments/1di3cfa/using_rag_agent_got_error_with_tools_parameter/) , 2024-06-18-0911
```
I using llm locally when i use `create_openai_tools_agent` 

, then i will get `TypeError: __call__() got an unexpected 
keyword argument 'tools'`

how do i fix it, my code is below:

    from langchain.tools.retriever import create_retrieve
r_tool
    
    retriever_tool = create_retriever_tool(
        retriever = retriever,
        name = 'retriever_tool',

        description = 'Retrieve the most relevant document from the database',
    )
    tools = [retriever_tool]
    
 
   from langchain import hub
    prompt = hub.pull('hwchase17/openai-tools-agent')
    
    from langchain.agents import
 AgentExecutor, create_openai_tools_agent
    agent = create_openai_tools_agent(llm, tools, prompt)
    agent_executor =
 AgentExecutor(agent=agent, tools=tools, verbose=True)
    agent_executor.invoke({'input':'What can i do in this system?
'})
    
```
---

     
 
all -  [ Here’s how to use Graph RAG to get better accuracy than std RAG ](https://www.reddit.com/r/LangChain/comments/1di09bu/heres_how_to_use_graph_rag_to_get_better_accuracy/) , 2024-06-18-0911
```
Information on entities like people, institutions, etc. is often highly interconnected, and this might be the case for y
our data too.

If so, you can:

- Create a graph connecting documents which have common n-grams, using TF-IDF etc.

- Du
ring inference, search this graph to get neighbours containing common n-grams and use them in the LLM’s context.

- Sear
ch results from Graph RAG are more likely to give you a comprehensive view of the entity being searched and the info con
nected to it.

Eg, , if doc A is selected as highly relevant, the docs containing data closely linked to doc A must be i
ncluded in the context to give a full picture.

I spent the weekend creating a Python library which automatically create
s this graph for the documents in your vectordb. It also makes it easy for you to retrieve relevant documents connected 
to the best matches.

Here’s the repo for the library: [https://github.com/sarthakrastogi/graph-rag/tree/main](https://g
ithub.com/sarthakrastogi/graph-rag/tree/main)
```
---

     
 
all -  [ End-to-end LLM Workflows Guide ](https://www.reddit.com/r/learnmachinelearning/comments/1dhz0gb/endtoend_llm_workflows_guide/) , 2024-06-18-0911
```
https://preview.redd.it/2dwz47mf357d1.png?width=924&format=png&auto=webp&s=64942b57742d637f1d31d6ea0b38fff07347beaa

Exc
ited to share our end-to-end LLM workflows guide that we’ve used to help our industry customers fine-tune and serve OSS 
LLMs that outperform closed-source models in quality, performance and cost

Key LLM workloads with [Ray](https://docs.ra
y.io/) and [Anyscale](https://anyscale.com/):

* 🔢 Preprocess our dataset (filter, schema, etc.) with batch data process
ing.
* 🛠️ Fine-tune our LLMs (ex. Meta's Llama 3) with full control (LoRA/full param, compute, loss, etc.) and optimizat
ions (parallelism, mixed precision, flash attn, etc.) with distributed training.
* ⚖️ Evaluate our fine-tuned LLMs with 
batch inference using Ray + [vLLM](https://github.com/vllm-project/vllm).
* 🚀 Serve our LLMs as a production application
 that can autoscale, swap between LoRA adapters, optimize for latency/throughput, etc.

Key [Anyscale](https://anyscale.
com/) infra capabilities that keeps these workloads efficient and cost-effective:

* ✨ Automatically provision worker no
des (ex. GPUs) based on our workload's needs. They'll spin up, run the workload and then scale back to zero (only pay fo
r compute when needed).
* 🔋 Execute workloads (ex. fine-tuning) with commodity hardware (A10s) instead of waiting for in
accessible resources (H100s) with data/model parallelism.
* 🔙 Configure spot instance to on-demand fallback (or vice-ver
sa) for cost savings.
* 🔄 Swap between multiple LoRA adapters using one base model (optimized with multiplexing).
* ⚡️ A
utoscale to meet demand and scale back to zero.

🆓 You can run this guide entirely for free on Anyscale (no credit card 
needed). Instructions in the links below 👇

🔗 Links:

* Blog post: [https://www.anyscale.com/blog/end-to-end-llm-workflo
ws-guide](https://www.anyscale.com/blog/end-to-end-llm-workflows-guide)
* GitHub repo: [https://github.com/anyscale/e2e-
llm-workflows](https://github.com/anyscale/e2e-llm-workflows)
* Notebook: [https://github.com/anyscale/e2e-llm-workflows
/blob/main/README.ipynb](https://github.com/anyscale/e2e-llm-workflows/blob/main/README.ipynb)
```
---

     
 
all -  [ How to add an Agent in a LangGraph as a node? Specifically agent created out of create_sql_agent ](https://www.reddit.com/r/LangChain/comments/1dhy51m/how_to_add_an_agent_in_a_langgraph_as_a_node/) , 2024-06-18-0911
```
I am trying to use the helper method create\_sql\_agent to create an agent and add it in a simple graph to create a data
base team. I tried to see if [SQL tutorial](https://python.langchain.com/v0.2/docs/integrations/toolkits/sql_database/) 
can be repurposed.

The graph structure that I wanted to design is very simple. A supervisor that delegates to a SQL Tea
m.

I tried following [https://python.langchain.com/v0.2/docs/tutorials/sql\_qa/#agents](https://python.langchain.com/v0
.2/docs/tutorials/sql_qa/#agents)  as suggested by u/hwchase17 for one of the previous [question](https://www.reddit.com
/r/LangChain/comments/1d4lwt0/am_i_the_only_one_who_feels_langgraph/). However, it uses the AgentExecutor instead of usi
ng langgraph as Agent Executor.

There are examples of connecting to SQL database in the [customer support chat bot tuto
rial](https://langchain-ai.github.io/langgraph/tutorials/customer-support/customer-support/). How we are not able to lev
erage the advantages that we get by using an SQL Agent namely:

* Recovering from errors and regenerating query correctl
y.
* Querying database multiple times.
* Save Tokens by looking into schema etc.

If there are any notebooks or code tha
t you could point to that would be great.

I started learning LangGraph for the promise of composing and using agents. I
f this is not doable with critical agents like SQL Database, then that defeats the purpose. Also that AgentExecutor is d
eprecated, it would be great if some of these tutorials are updated to use LangGraph as AgentExecutor / ChatExecutor.
```
---

     
 
all -  [ 20M looking for SWE internships. Previous internship took 300 apps, but not sure how to improve resu ](https://www.reddit.com/r/resumes/comments/1dhy444/20m_looking_for_swe_internships_previous/) , 2024-06-18-0911
```
https://preview.redd.it/lctxew5aw47d1.jpg?width=2550&format=pjpg&auto=webp&s=1e5854ebd28f62fde665fa47a85fc64ba13c3224

A
s stated in title, took me 300+ apps to get my current internship. Of that 300, got 4 interviews, 3 rejects, one offer. 
I didn't have access to the exact numbers so kinda made them up with a estimated guess

I just finished year 1 in EEE, n
ow planning on looking for either next year's summer internship. Or part time internship during the semester.

The point
s under my SWE internship is IMO not very good, since

1.) I've only been doing this internship for about 4 weeks, but a
 recruiter is asking for my resume. So I'd thought I just update my resume

2.) I'm only assigned really simple projects
( takes 2-3 days?) so I don't know how to quantify or make it sound more impressive.

Appreciate your help!
```
---

     
 
all -  [ How to circumvent one document per page when loading PDF files? ](https://www.reddit.com/r/LangChain/comments/1dhv3a5/how_to_circumvent_one_document_per_page_when/) , 2024-06-18-0911
```
I know this might be a really stupid question, but i thought I could gain some insight, by asking it here.   
I am curre
ntly working on a simple RAG application, where I load in documents from a larger local library.   
This library consist
s of multiple different document types, although mostly .docx and .pdf files.   
When loading the PDF files I am current
ly using the PyMuPDFLoader. However it chunks the pdf into pages from the start.   
My questoin is, whether there is a w
ay to circumvent loading a PDF file, and already chunking it into a document for each individual page. Some information 
is lost between the documents, as it might traverse at a page break. 

I would like to implement the chunking strategy l
ater on, as we are looking into implementing a costum chunking strategy. 

Is there a smart strategy for this? 

Thanks 
in advance
```
---

     
 
all -  [ Suggest me a video tutorial about LangChain ](https://www.reddit.com/r/learnmachinelearning/comments/1dhu5sx/suggest_me_a_video_tutorial_about_langchain/) , 2024-06-18-0911
```
Suggest me some yt video link for langchain, the one which is more focused on basic/foundational concept and teaches fro
m very basic thing rather than just focusing on a project type work
```
---

     
 
all -  [ OpenAI Content Filter when using MapReduce ](https://www.reddit.com/r/LangChain/comments/1dhl76g/openai_content_filter_when_using_mapreduce/) , 2024-06-18-0911
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

     
 
all -  [ Dealing with Incomplete Structured Output? ](https://www.reddit.com/r/LangChain/comments/1dhe1es/dealing_with_incomplete_structured_output/) , 2024-06-18-0911
```
I have a use case where I generate a json output. The json is sometimes so large that it gets over the output range capa
bility of my llm, rendering my structured output not parseable. What method you guys apply when faced with an incomplete
 Structured output?
```
---

     
 
all -  [ Suggesting which RAG method will work best for you, based on your use case 🔎📑  ](https://www.reddit.com/r/LangChain/comments/1dh79xx/suggesting_which_rag_method_will_work_best_for/) , 2024-06-18-0911
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

     
 
all -  [ Determinism control ](https://www.reddit.com/r/LangChain/comments/1dh5qr2/determinism_control/) , 2024-06-18-0911
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

     
 
all -  [ Passing API Key via URL Params ](https://www.reddit.com/r/LangChain/comments/1dh3fq8/passing_api_key_via_url_params/) , 2024-06-18-0911
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

     
 
all -  [ ERROR: pip's dependency resolver  ](https://www.reddit.com/r/FaceFusion/comments/1dh2zu3/error_pips_dependency_resolver/) , 2024-06-18-0911
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

but now I have no other ideas to fix this, I need your help

  
EDIT:  
I installed minico
nda because I wanted more free space on my disc, and this turned out to be the solution

I'm not sure if this was the pr
oblem, but after I installed miniconda and uninstalled anaconda, and now if I run [run.py](http://run.py),  it's actuall
y working now
```
---

     
 
all -  [ Please review my Resume. Don't have any offers yet ](https://www.reddit.com/r/Resume/comments/1dh1hfu/please_review_my_resume_dont_have_any_offers_yet/) , 2024-06-18-0911
```
https://preview.redd.it/q8dfqp2aov6d1.jpg?width=1275&format=pjpg&auto=webp&s=6b7e6392ee8eb79d53349eac7d18eddc08759535

h
ttps://preview.redd.it/h8ffm4acov6d1.jpg?width=1275&format=pjpg&auto=webp&s=835b85d481ee25e79d6f94646e238e0d9f09ad60


```
---

     
 
all -  [ Please review my Resume. Don't have any offers yet ](https://www.reddit.com/r/developersIndia/comments/1dh1bj2/please_review_my_resume_dont_have_any_offers_yet/) , 2024-06-18-0911
```
https://preview.redd.it/b0n4g6izlv6d1.jpg?width=1275&format=pjpg&auto=webp&s=de76a6165f59fbc9d18924eb26796a9cb7d095a3


```
---

     
 
all -  [ Please review my Resume. Don't have any offers yet ](https://www.reddit.com/r/resumes/comments/1dh18d3/please_review_my_resume_dont_have_any_offers_yet/) , 2024-06-18-0911
```
https://preview.redd.it/b9vhtwowkv6d1.jpg?width=1275&format=pjpg&auto=webp&s=f6df4a4e647d3de7331903ac184b58135befa9f5

h
ttps://preview.redd.it/rexnwyowkv6d1.jpg?width=1275&format=pjpg&auto=webp&s=8503335ba04cc4a0321fb6500f0e4bd153e03bcf


```
---

     
 
all -  [ We are on TV! 📺 👏 ](https://i.redd.it/qtxv6pp0jv6d1.png) , 2024-06-18-0911
```
Excellent work by some passionate guy!
I admire his work towards his passion.
```
---

     
 
all -  [ Any learning Group for LangGraph? ](https://www.reddit.com/r/LangChain/comments/1dgxdvq/any_learning_group_for_langgraph/) , 2024-06-18-0911
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

current discord server: [https://di
scord.gg/SUTerWEJ](https://discord.gg/SUTerWEJ)

give me your github, i will add you to [https://github.com/LangGraph-GU
I](https://github.com/LangGraph-GUI)
```
---

     
 
all -  [ Grafana + Ollama ](https://www.reddit.com/r/ollama/comments/1dguvr8/grafana_ollama/) , 2024-06-18-0911
```
What's the best way to integrate Ollama with Grafana (e.g. have Ollama summarize logs/dashboards/etc.)?  It looks like t
here is an LLM plugin for Grafana, but it appears to not support Ollama (https://github.com/grafana/grafana-llm-app/issu
es/162).

  
Would trying to feed the grafana API spec to Ollama and using langchain to query the API be the most straig
ht-forward approach?  
```
---

     
 
all -  [ save and load embeddings  ](https://www.reddit.com/r/LangChain/comments/1dgpc6w/save_and_load_embeddings/) , 2024-06-18-0911
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

     
 
all -  [ [P] Seeking Feedback on My GenAI Job Fit Project - New to LangChain/LangGraph ](https://www.reddit.com/r/MachineLearning/comments/1dgns9p/p_seeking_feedback_on_my_genai_job_fit_project/) , 2024-06-18-0911
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

     
 
all -  [  AI-Driven Job Application Enhancement System - Seeking Feedback and Suggestions! ](https://www.reddit.com/r/LangChain/comments/1dgnmjt/aidriven_job_application_enhancement_system/) , 2024-06-18-0911
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

     
 
all -  [ How to work with large data that is returned from an api? ](https://www.reddit.com/r/LangChain/comments/1dgm1ij/how_to_work_with_large_data_that_is_returned_from/) , 2024-06-18-0911
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

     
 
all -  [ Roast My Resume, Masters in Computer Science and 1.5 Years of Relevant Experience, Not Receiving Any ](https://www.reddit.com/r/resumes/comments/1dgkgl9/roast_my_resume_masters_in_computer_science_and/) , 2024-06-18-0911
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

     
 
all -  [ What’s Memory Tuning and how does it give higher accuracy + speed than RAG and prompting? ](https://www.reddit.com/r/LangChain/comments/1dgi0vj/whats_memory_tuning_and_how_does_it_give_higher/) , 2024-06-18-0911
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

     
 
all -  [ Where Can I Find Deterministic Tools for AI Agents?  ](https://www.reddit.com/r/AI_Agents/comments/1dggm9v/where_can_i_find_deterministic_tools_for_ai_agents/) , 2024-06-18-0911
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

     
 
all -  [ How to Repurpose YouTube Videos for Free Using AI and No-Code Tools in 2024 ](https://www.reddit.com/r/AiChampions/comments/1dgfyuk/how_to_repurpose_youtube_videos_for_free_using_ai/) , 2024-06-18-0911
```
Video content repurposing tools are usually quite expensive. 

But using this trick, you can repurpose video content com
pletely FREE.

From a YouTube URL, we can now generate multiple video clips, and even a title & a description for each c
lip.  

Complete no-code flow below ↓

[Repurpose YouTube Videos for Free](https://reddit.com/link/1dgfyuk/video/e04u7o5
61q6d1/player)

We recently launched a webinar series where we cover multiple AI app-building topics. 

Naturally, this 
led us to wonder: 

could AI help us identify all the subtopics we discuss & create smaller, more focused clips for each
 one? 

Turns out, it's possible! 

A rough sketch of the idea.

[Subtopics AI Idea Rough Sketch](https://preview.redd.i
t/igdc1jv91q6d1.jpg?width=2895&format=pjpg&auto=webp&s=071ffa2a8fb271b59e8c7018aa7a9dab82da676f)

Implemented the 3 step
s below in langflow.

**Step 1**

https://preview.redd.it/njrh82wi1q6d1.jpg?width=2084&format=pjpg&auto=webp&s=c22ecad57
063c30785de94542c05c171d14bcbb3

We download the video and generate a transcript. 

One could use YT subtitles or [Whisp
er](https://honeysyed.com/whispertranscribe) to generate a transcript with timestamps.

**Step 2**

https://preview.redd
.it/2lgkdf5l1q6d1.jpg?width=2488&format=pjpg&auto=webp&s=d210a268113d084072018c0edf9bdd6e2b1ff49b

Send the transcript t
o a local LLM or a hosted one. 

The key is to get a structured response with start & end timestamps. (bonus: generate T
itle, Description & even a blog post for each clip)

LangChain makes this quite easy with output parsers (added to a Lan
gFlow custom comp.)

**Step 3**

Generate clips based on the timestamps from the last step (used ffmpeg).

Below are the
 clip details generated for a Paul Graham video.

[YouTube Title and Description](https://preview.redd.it/xbg4xbct1q6d1.
jpg?width=2048&format=pjpg&auto=webp&s=caed9c5b2d9a2f18d2337b2594ebfcbeeac15b28)

Now you can repost the smaller clips b
ack to YT with the title and descriptions provided for each clip.

The complete no-code working flow is available in the
 LangFlow store (for free) as 'YouTube Subclips Generator'.

[Source](https://x.com/MisbahSy/status/1799083774912974957)

```
---

     
 
all -  [ Streaming of OpenAIAssistant v2 ](https://www.reddit.com/r/LangChain/comments/1dgfsmg/streaming_of_openaiassistant_v2/) , 2024-06-18-0911
```
Hello all, 
OpenAI assistant should support streaming.
But I am not sure why the current OpenAIAssistantV2Runnable do no
t supports it.
Is there a solution to this?
 
```
---

     
 
all -  [ How to securely pass private data? ](https://www.reddit.com/r/LangChain/comments/1dfyz50/how_to_securely_pass_private_data/) , 2024-06-18-0911
```
Wondering if anyone here has dealt with passing private information from end user inputs to your LLM, later to interact 
with an external API? I'm not talking about authentication data per se, just private information (e.g PII) people wouldn
't normally want to share on the internet.   
What solution have you come up with to ensure some privacy for your users?

```
---

     
 
all -  [ Evaluating with Ragas ](https://www.reddit.com/r/LangChain/comments/1dfxwga/evaluating_with_ragas/) , 2024-06-18-0911
```
I've finished my rag job, and performed a evaluation on my rag. results given below

[ragas output](https://preview.redd
.it/pt0khqy10l6d1.png?width=1280&format=png&auto=webp&s=4979a08f0e648937407d23feeb494f02a8e793ba)

context\_precision is
 better than good but why the other metrics sucks and how to improve them?
```
---

     
 
all -  [ RAG Me Up - RAG for chat /w Langchain ](https://www.reddit.com/r/LangChain/comments/1dfx2di/rag_me_up_rag_for_chat_w_langchain/) , 2024-06-18-0911
```
We are in early stages of developing our project so keen feedback. RAG Me Up is a robust layer on top of Langchain desig
ned to make RAG easy and also not prone to simple issues like document re-retrieval, performance for rephrasind and perh
aps most importantly: make Langchain work well with Instruct/Chat models' templates.

[https://github.com/AI-Commandos/R
AGMeUp ](https://github.com/AI-Commandos/RAGMeUp)
```
---

     
 
all -  [ AI Innovations: Streamlining Insurance Claims, Enhancing Engineering Projects, and Revolutionizing P ](https://www.reddit.com/r/ai_news_by_ai/comments/1dfvkcx/ai_innovations_streamlining_insurance_claims/) , 2024-06-18-0911
```





#vc #tool #release #hardware #event #feature #opinions #opensource #update #major_players #science #leaders #startu
ps #scheduled

Y Combinator's S24 startup, ClaimSorted, is leveraging AI technology to streamline insurance claims proce
ssing, aiming to enhance customer experience and drive cost efficiencies [1]. Another startup from the same batch, Entan
gl_AI, has launched a platform that automates error detection in engineering projects, potentially saving time, money, a
nd lives by identifying and fixing design issues early [2].







The Data AI Summit will feature a fireside chat with 
NVIDIA AI Developer and Databricks Co-Founder and CEO, along with several informative sessions [3]. These include a sess
ion on the rapid development and deployment of Generative AI apps at scale with NVIDIA NIM [4], a session on Architectur
e Analysis for ETL Processing: CPU vs GPU [5], and a session on unlocking the power of Spark RAPIDS ML for GPU-accelerat
ed distributed machine learning [6]. 







NVIDIA AI Developer has also discussed the benefits of TensorRT Weight-Stri
pped Engines, which offer over 95% compression, support various models, and allow for refitting with weights directly on
 end-user devices [7]. The use of generative AI in CVE analysis can significantly enhance security workflows, with Agent
 Morpheus, a generative AI application, automating the process of detecting and remediating CVEs [8].







The era of 
the AI PC has arrived, offering unparalleled performance in generative tasks with NVIDIA RTX and GeForce RTX technologie
s [9]. Andrew Ng has developed an agentic machine translation demonstration that prompts a language model to translate t
ext, reflects on the translation to provide suggestions, and refines the translation based on those suggestions [10].








Groq Inc announced their GM of GroqCloud, Sundeep, and is hosting a follow-up AMA session to answer more questions 
about scaling for the fastest AI inference [12][13]. The company also powered the Build Together AI Hackathon, where 28 
incredible apps were created [14]. A webinar titled 'Build Blazing-Fast LLM Apps with Groq, LangFlow, & LangChain' is sc
heduled to take place, showcasing how Groq's AI inference technology integrates with LangFlow and LangChain to create po
werful applications using Large Language Models (LLMs) [15].







a16z emphasizes the importance of rethinking product
s from the ground up, rather than just adding AI, and discusses the evolution from AI-augmented to AI-native products on
 their podcast [16]. Vivek Natarajan, a Research Lead at Google Health AI, is focusing on AI and biomedicine with Projec
t AMIE [18]. OpenAI clarifies that their strategic cloud relationship with Microsoft remains unchanged, and they have a 
partnership with OCI to use the Azure AI platform on OCI infrastructure for inference and other needs [20].







Midjo
urney has announced several updates, including the release of model personalization, the development of a new set of alg
orithms, the alpha testing phase for a new feature, and the ability of their AI to figure things out from other people's
 images [21][22][23][24][25]. Stability AI has announced the release of Stable Diffusion 3 Medium, a text-to-image AI mo
del with two billion parameters, optimized for consumer PCs and laptops, as well as enterprise-tier GPUs [26].




[1. Y
 Combinator @ycombinator https://twitter.com/ycombinator/status/1800558618497962219](https://twitter.com/ycombinator/sta
tus/1800558618497962219)

[2. Y Combinator @ycombinator https://twitter.com/ycombinator/status/1800573712862695857](http
s://twitter.com/ycombinator/status/1800573712862695857)

[3. NVIDIA AI Developer @NVIDIAAIDev https://twitter.com/NVIDIA
AIDev/status/1800574724944048585](https://twitter.com/NVIDIAAIDev/status/1800574724944048585)

[4. NVIDIA AI Developer @
NVIDIAAIDev https://twitter.com/NVIDIAAIDev/status/1800574733043323141](https://twitter.com/NVIDIAAIDev/status/180057473
3043323141)

[5. NVIDIA AI Developer @NVIDIAAIDev https://twitter.com/NVIDIAAIDev/status/1800574743550038505](https://tw
itter.com/NVIDIAAIDev/status/1800574743550038505)

[6. NVIDIA AI Developer @NVIDIAAIDev https://twitter.com/NVIDIAAIDev/
status/1800574751183634542](https://twitter.com/NVIDIAAIDev/status/1800574751183634542)

[7. NVIDIA AI Developer @NVIDIA
AIDev https://twitter.com/NVIDIAAIDev/status/1800603157665354116](https://twitter.com/NVIDIAAIDev/status/180060315766535
4116)

[8. NVIDIA AI Developer @NVIDIAAIDev https://twitter.com/NVIDIAAIDev/status/1800619033487692240](https://twitter.
com/NVIDIAAIDev/status/1800619033487692240)

[9. NVIDIA AI Developer @NVIDIAAIDev https://twitter.com/NVIDIAAIDev/status
/1800913453483225108](https://twitter.com/NVIDIAAIDev/status/1800913453483225108)

[10. Andrew Ng @AndrewYNg https://twi
tter.com/AndrewYNg/status/1800582171259982289](https://twitter.com/AndrewYNg/status/1800582171259982289)

[11. Pika @pik
a_labs https://twitter.com/pika_labs/status/1800593550494863425](https://twitter.com/pika_labs/status/180059355049486342
5)

[12. Groq Inc @GroqInc https://twitter.com/GroqInc/status/1800563455977750704](https://twitter.com/GroqInc/status/18
00563455977750704)

[13. Groq Inc @GroqInc https://twitter.com/GroqInc/status/1800589921876312090](https://twitter.com/G
roqInc/status/1800589921876312090)

[14. Groq Inc @GroqInc https://twitter.com/GroqInc/status/1800635116592480543](https
://twitter.com/GroqInc/status/1800635116592480543)

[15. Groq Inc @GroqInc https://twitter.com/GroqInc/status/1800913489
399099728](https://twitter.com/GroqInc/status/1800913489399099728)

[16. a16z @a16z https://twitter.com/a16z/status/1800
617449382969440](https://twitter.com/a16z/status/1800617449382969440)

[17. a16z @a16z https://twitter.com/a16z/status/1
800623154257367123](https://twitter.com/a16z/status/1800623154257367123)

[18. Google AI @googleai https://twitter.com/g
oogleai/status/1800657713418109269](https://twitter.com/googleai/status/1800657713418109269)

[19. Yann LeCun @ylecun ht
tps://twitter.com/ylecun/status/1800677672512806971](https://twitter.com/ylecun/status/1800677672512806971)

[20. OpenAI
 @openai https://twitter.com/openai/status/1800778542512550260](https://twitter.com/openai/status/1800778542512550260)


[21. Midjourney @midjourney https://twitter.com/midjourney/status/1800693675686834450](https://twitter.com/midjourney/st
atus/1800693675686834450)

[22. Midjourney @midjourney https://twitter.com/midjourney/status/1800707282726174954](https:
//twitter.com/midjourney/status/1800707282726174954)

[23. Midjourney @midjourney https://twitter.com/midjourney/status/
1800819091302965729](https://twitter.com/midjourney/status/1800819091302965729)

[24. Midjourney @midjourney https://twi
tter.com/midjourney/status/1800819304402976971](https://twitter.com/midjourney/status/1800819304402976971)

[25. Midjour
ney @midjourney https://twitter.com/midjourney/status/1800819590005752126](https://twitter.com/midjourney/status/1800819
590005752126)

[26. Stability AI @stabilityai https://twitter.com/stabilityai/status/1800875914299048404](https://twitte
r.com/stabilityai/status/1800875914299048404)

[27. NVIDIA AI @NVIDIAAI https://twitter.com/NVIDIAAI/status/180090716508
4848531](https://twitter.com/NVIDIAAI/status/1800907165084848531)
```
---

     
 
all -  [ Streaming with agents ](https://www.reddit.com/r/LangChain/comments/1dfsv2t/streaming_with_agents/) , 2024-06-18-0911
```
I have implementing streaming with a chain based runnable which gives token by token output ( word by word), making UI s
imilar to how ChatGPT has its UI. But while implementing the same with an Agent based runnable I see that it gives 3 out
puts  in order, actions, steps and, output which contains answer. All three come as a whole, one after the other, not wo
rd by word.

I want to get word by word streaming for the agent's final answer.
```
---

     
 
all -  [ Newbie Seeking Advice on Side Project - Chat with Calendar  ](https://www.reddit.com/r/LangChain/comments/1dfsjwl/newbie_seeking_advice_on_side_project_chat_with/) , 2024-06-18-0911
```
As the title reads, I'm building a side project to chat with my google calendar + assignments from Canvas (learning mana
gement system). I'm using GCP to practice working with the cloud. 

As of April 2024, Cloud SQL for MySQL now supports v
ector embeddings. Essentially, I have all of my coursework and assignments in an events table. At first I embedded at th
e row level but this lost the understanding of columns. Now, I have a new column that is JSON representation of all the 
relevant columns for my eventual retrieval (event\_title, start\_time, end\_time, tag (Assignment, Discussion, Quiz, Stu
dy Times, Personal Events)). In a new column, I've successfully embedded all of these JSON's. What I've described above 
is pretty much the extent of what I've done. 

My end goal is to develop a streamlit UI to query this vector column in m
y SQL database. I have a few different paths I can go down, but I'm intentionally keeping this at a high level to hear d
iverse responses. 

  
Any advice? All thoughts are greatly appreciated. 

  
Cheers
```
---

     
 
all -  [ Improved Text2SQL Dataset Now Available on Huggingface! ](https://www.reddit.com/r/LangChain/comments/1dfsdbw/improved_text2sql_dataset_now_available_on/) , 2024-06-18-0911
```
I'm excited to share an updated open-source resource we’ve been working on—an improved version of the Spider dataset ori
ginally published by Yale University for Text2SQL tasks. You can check it out here: [https://huggingface.co/datasets/Raf
faSch121/fixed\_spider](https://huggingface.co/datasets/RaffaSch121/fixed_spider)

During our own model training at [Tur
bular](http://www.turbular.com) we identified several issues in the original dataset. To help the community and give bac
k, we decided to address these problems and release a corrected version. We hope this enhanced dataset will benefit ever
yone working on Text2SQL and similar projects.

Feel free to download, experiment, and contribute back if you find ways 
to make it even better!
```
---

     
 
all -  [ A tutorial on creating video from text using AI ](https://www.reddit.com/r/LangChain/comments/1dfsc15/a_tutorial_on_creating_video_from_text_using_ai/) , 2024-06-18-0911
```
I have written an article on how to create a Text to Video AI generator which generates video from a topic by collecting
 relevant stock videos and stitching them together. 

The code is completely open-source and uses free to use tools to g
enerate videos

Link to article :- [https://medium.com/@anilmatcha/text-to-video-ai-how-to-create-videos-for-free-a-comp
lete-guide-a25c91de50b8](https://medium.com/@anilmatcha/text-to-video-ai-how-to-create-videos-for-free-a-complete-guide-
a25c91de50b8)
```
---

     
 
all -  [ Token count and cost for chain.astream_events(). ](https://www.reddit.com/r/LangChain/comments/1dfpjpr/token_count_and_cost_for_chainastream_events/) , 2024-06-18-0911
```
 Hey all, How do I get the token count for chain.astream_events()
```
---

     
 
all -  [ RAGchain searching for similar prompts ](https://www.reddit.com/r/LangChain/comments/1dfp7xf/ragchain_searching_for_similar_prompts/) , 2024-06-18-0911
```
Hi i am new to the framework of langchain and i want to search for some information in contract documents regarding tota
l m2 area for a partner. The problem is that the main partner contract can have several newer appendices where the old t
otal m2 area in the old original contract is now replaced. Now i only want to extract the new total m2 area. Is there a 
clever way to sort or filter this?
```
---

     
 
all -  [ [Project] Compare Top 10 LMSYS Models with a Universal LLM API Library ](https://www.reddit.com/r/LangChain/comments/1dfp2z5/project_compare_top_10_lmsys_models_with_a/) , 2024-06-18-0911
```
Hello Langchain community!

I'm excited to share a project we've been working on - an open-source 'AI Gateway' library t
hat allows you to access and compare 200+ language models from multiple providers using a simple, unified API.

To showc
ase the capabilities of this library, I've created a Google Colab notebook that demonstrates how you can easily compare 
the top 10 models from the LMSYS leaderboard with just a few lines of code.

Here's a snippet:

https://preview.redd.it/
lcqhryzx0j6d1.png?width=1822&format=png&auto=webp&s=cf7d055fa0e79117fed5dd8f8dc37498fe43b9e3

The library handles all th
e complexities of authenticating and communicating with different provider APIs behind the scenes, allowing you to focus
 on experimenting with and comparing the models themselves.

Some key features of the AI Gateway library:

* Unified API
 for accessing 200+ LLMs from OpenAI, Anthropic, Google, Ollama, Cohere, Together AI, and more
* Compatible with existin
g OpenAI client libraries for easy integration
* Routing capabilities like fallbacks, load balancing, retries

I believe
 this library could be incredibly useful for researchers and developers in the Langchain community who want to easily co
mpare and benchmark different LLMs, or build applications that leverage multiple models.

I've put the demo notebook lin
k below, I'd love to get your feedback, suggestions, and contributions:

[https://github.com/Portkey-AI/gateway/blob/mai
n/cookbook/use-cases/LMSYS%20Series/comparing-top10-LMSYS-models-with-Portkey.ipynb](https://github.com/Portkey-AI/gatew
ay/blob/main/cookbook/use-cases/LMSYS%20Series/comparing-top10-LMSYS-models-with-Portkey.ipynb)
```
---

     
 
all -  [ Please guide towards solving this problem ](https://www.reddit.com/r/generativeAI/comments/1dflxqo/please_guide_towards_solving_this_problem/) , 2024-06-18-0911
```
How to get started with the problem statement?

Hey guys, i am new to generative AI, it’s been a few days learning new t
hings. I have a problem statement in hand. We have to evaluate a startup idea. We already have an evaluation checklist t
hat has like 30 parameters on the basic of which we decide the feasibility of the idea. We have to build a model in whic
h we prompt an idea and the input idea goes through various agents who are (business analysts, cofounder, VC). So it fir
st goes to BA and then the result goes to cofounder and so on therefore getting perspective of all the agents. For start
ers i want to build the model with 3 agents. Once it passes through 3rd agent it gives the final result as an evaluation
 checklist (the same one i talked about above). 

Now my question is how should i approach this problem and what would b
e the underlying concept used for building such a model? 
Also from where can i start ? 
FYI - i read a bit about genert
ive ai topics like embedding, fine tuning and a bit of langchain (built a simple agent) etc. Still exploring agentic AI.
 

Thanks in advance !! 
```
---

     
 
all -  [ How would you schedule an agent for a task? ](https://www.reddit.com/r/AI_Agents/comments/1dfjh5q/how_would_you_schedule_an_agent_for_a_task/) , 2024-06-18-0911
```
I'd like to have my agent prepare my mornings with news and some interesting investment ideas. The agent exists already 
as ReAct on Langchain and works quite well, but I have to start him up and ask him to do his work. How would you schedul
e this?
```
---

     
 
MachineLearning -  [ [P] I'm tired of LangChain, so I made a simple open-source alternative with support for tool using a ](https://www.reddit.com/r/MachineLearning/comments/1deffo8/p_im_tired_of_langchain_so_i_made_a_simple/) , 2024-06-18-0911
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

     
 
MachineLearning -  [ [P] Superfast RAG: Langchain Streaming and Groq ](https://www.reddit.com/r/MachineLearning/comments/1d5s9g4/p_superfast_rag_langchain_streaming_and_groq/) , 2024-06-18-0911
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

     
 
deeplearning -  [ How to finetune? ](https://www.reddit.com/r/deeplearning/comments/1daio0h/how_to_finetune/) , 2024-06-18-0911
```
Can someone guide me to some resource how can I finetune an open source llm or some library (like langchain) on unstruct
ured data (example: news articles on cricket) So that model can answer a question (like When did India won world Cup?)
```
---

     
