 
all -  [ Having problem with langchain loader ](https://www.reddit.com/r/datascience/comments/1eaien5/having_problem_with_langchain_loader/) , 2024-07-24-0912
```
I have the data in JSON format I’m trying to use the jsonloader but apparently I need a download and import a jq module 
and that’s where my problem is. I have pip installed jq but when it’s time to import it, I get a no module error and yes
 it’s installed in venv that I am working in. Has anyone had this problem before 
```
---

     
 
all -  [ Exciting News from Meta [Llama 3.1 is Here] ](https://www.reddit.com/r/LangChain/comments/1eageaq/exciting_news_from_meta_llama_31_is_here/) , 2024-07-24-0912
```
Meta has just released its latest LLM model, Llama 3.1, marking a significant step in accessible artificial intelligence
. Here are the key points from the announcement:

1. **405B version.** There is a new Llama 3.1 405B version. That’s rig
ht *405 Billion parameters.*
2. **Expanded context length**: Now all llama 3.1 models offer a context length of **128K t
okens**, 16 times its previous 8K context length from Llama 3. This allows for more advanced use cases, such as long-for
m text summarization, multilingual conversational agents, and coding assistants
3. **Model evaluations**: The model eval
uations released by Meta are as follows:

[Llama 405B](https://preview.redd.it/zjcxaf93jbed1.png?width=3201&format=png&a
uto=webp&s=31191792e788799899102d882d3170acc34ea19b)

[Llama 8B](https://preview.redd.it/h1x4jcy6jbed1.png?width=3201&fo
rmat=png&auto=webp&s=4fb34e2d110345a34e1715d16be8951d0edc637b)

**4. API Coming Soon:** Users will be able to access and
 utilize Llama 3.1 models through [awanllm.com](http://awanllm.com/) soon. Stay tuned for updates in this post!

Source:
 [https://ai.meta.com/blog/meta-llama-3-1/](https://ai.meta.com/blog/meta-llama-3-1/)
```
---

     
 
all -  [ AI Code Assistant SaaS built on GPT-4o-mini, Langchain, Postgres and pg_vector ](https://www.thenile.dev/blog/building_code_assistant) , 2024-07-24-0912
```

```
---

     
 
all -  [ MongoDB as vectorstore  ](https://www.reddit.com/r/LangChain/comments/1eaffzv/mongodb_as_vectorstore/) , 2024-07-24-0912
```
What are your thoughts on using MongoDB as vectorstore for your apps.

I was working on prototype locally for the most o
f its time but right now we are moving to hosting on streamlit, what are your recommendations for vectorstores.

```
---

     
 
all -  [ Looking for an opensource framework to manage agents ](https://www.reddit.com/r/LangChain/comments/1eaedlh/looking_for_an_opensource_framework_to_manage/) , 2024-07-24-0912
```
I want to give my client the option to construct new agents and create flows for input and output like vectorizing input
 and parsing output and storing it in a database. Is there any opensource tool with a UI that can do this?
The language 
it's written in doesn't really matter, all options are welcome.
```
---

     
 
all -  [ I build a RAG-based multi-tenant AI Code Assistant with OpenAI, LangChain, Postgres and PG Vector ](https://www.reddit.com/r/LangChain/comments/1eadv0e/i_build_a_ragbased_multitenant_ai_code_assistant/) , 2024-07-24-0912
```
I am rather new to the AI space (my background is data infrastructure), so I am documenting my journey as I'm learning. 
This time I built an AI Code Assistant that uses RAG to answer questions about different repositories.

I blogged everyt
hing I learned while building this - Schema design, use of LangChain (tbh, not sure it was a good choice...), choice of 
models, streaming chat UX...

You can see the app here: [https://code-assist-nile.vercel.app](https://code-assist-nile.v
ercel.app)  
And the blog: [https://www.thenile.dev/blog/building\_code\_assistant](https://www.thenile.dev/blog/buildin
g_code_assistant)  
The code is here: [https://github.com/niledatabase/niledatabase/tree/main/examples/ai/code\_assist/]
(https://github.com/niledatabase/niledatabase/tree/main/examples/ai/code_assist/)
```
---

     
 
all -  [ Forced function calling in vertex ai gemini?? ](https://www.reddit.com/r/LangChain/comments/1ead44f/forced_function_calling_in_vertex_ai_gemini/) , 2024-07-24-0912
```
Hello everyone,

I want to force function calling with Gemini. Does anyone know how to do this?

I have checked the docu
mentation for Vertex AI and Langchain but couldn't find any information. In the Vertex AI docs, I found a parameter that
 could be passed, but I don't know how to pass it using Langchain. I am using `ChatVertexAI().bind_tools()`.

Regards!
```
---

     
 
all -  [ What do you think are better alternatives to Pinecone Vector DB? ](https://www.reddit.com/r/SmythOS/comments/1eabnkj/what_do_you_think_are_better_alternatives_to/) , 2024-07-24-0912
```
I have tried using pinecone, usually with frameworks like Langchain and llama-index and I saw that pinecone doesn't appe
ar to support storing documents alongside your vectors so what I tried to do is actually cram snippets of the document i
nto the metadata, but the metadata is limited to something really really small, so the maximum document length gets cons
trained. 

If you use another database alongside pinecone and just want to retrieve uuids or something, it's fine, but i
t struck me as a very weird omission in their design. 
```
---

     
 
all -  [ Is Qdrant cloud Production Ready? ](https://www.reddit.com/r/LangChain/comments/1eaabwv/is_qdrant_cloud_production_ready/) , 2024-07-24-0912
```
Guys,

Has anybody used Qdrant in the cloud, especially Azure and has gone live and in production? We are trying to inse
rt 884 points with a production grade cluster in azure eastus and it takes about 6-8 seconds and that too with gRPC. Htt
p takes even longer.

We are absolutely sure that this is the time taken by Qdrant Remote Client provided by their offic
ial package because we have enabled all the logging and can pin-point which operation takes time.

We created a support 
ticket with the Qdrant team as well, but have been ghosted by them.  

Wondering if Qdrant is right choice and if it is,
 how do people insert points faster? We do have metadata and chunk text in the point. 
```
---

     
 
all -  [ Multi-agent-DataAnalysis AI-Driven Data Analysis System ](https://www.reddit.com/r/LangChain/comments/1ea7g23/multiagentdataanalysis_aidriven_data_analysis/) , 2024-07-24-0912
```
# # Advanced AI-Driven Data Analysis System: A LangGraph Implementation



## Project Overview



I've developed a sophi
sticated data analysis system that leverages the power of LangGraph, showcasing its capabilities in integrating various 
AI architectures and methodologies. This system is designed to serve as a comprehensive example of how LangGraph can be 
used to streamline complex data analysis tasks by orchestrating multiple AI agents and architectural patterns.

https://
preview.redd.it/lntq41fap9ed1.jpg?width=610&format=pjpg&auto=webp&s=7b2f31c450c495ebe2eb3d5a1e75522223ae1267

## Key Fea
tures



- \*\*LangGraph-Powered Architecture\*\*: The system demonstrates LangGraph's flexibility by incorporating:

  
- Supervisor agents for overseeing the analysis process

  - Chain-of-thought reasoning for complex problem-solving

  -
 Critic agents for quality assurance and error checking



- \*\*Innovative Note Taker Agent\*\*: A standout feature tha
t highlights LangGraph's extensibility:

  - Continuously records the current state of the project

  - Provides a more 
efficient alternative to transmitting complete historical information

  - Enhances the system's ability to maintain con
text and continuity across different analysis stages



- \*\*Adaptive Workflow\*\*: Showcases LangGraph's dynamic routi
ng capabilities, adjusting the analysis approach based on the data and task at hand.



## Why It's a Valuable LangGraph
 Example



This implementation serves as an excellent case study for LangGraph users by demonstrating:



1. Integratio
n of diverse AI agent types within a unified framework

2. Efficient state management using the innovative Note Taker ag
ent

3. Real-world application of LangGraph in complex data analysis scenarios



## Contribution to LangGraph



I am e
ager to contribute this project as an example in the official LangGraph repository. My goals are to:



- Provide a comp
rehensive, real-world example of LangGraph's capabilities

- Help other developers understand advanced LangGraph impleme
ntations

- Contribute to the growth and adoption of LangGraph in the AI community



## Project Repository



For a dee
per dive into the codebase, architecture, and implementation details, please visit the project's GitHub repository:



\
[AI-Driven Data Analysis System on GitHub\](https://github.com/starpig1129/Multi-agent-DataAnalysis)





I welcome feed
back and collaboration to refine this example for potential inclusion in the LangGraph documentation or example collecti
on.



## Next Steps



1. I am open to adapting the project to better align with LangGraph's documentation standards.


2. I would appreciate guidance on the best way to submit this as a potential official example.

3. I'm eager to collabor
ate with the LangGraph community to enhance this example and make it as valuable as possible for other users.



Feel fr
ee to explore the repository, and I look forward to any feedback or suggestions for improving this as a LangGraph exampl
e!


```
---

     
 
all -  [ Using ChatGPT Vision API with LangChain in JavaScript ](https://www.reddit.com/r/learnjavascript/comments/1ea7cxr/using_chatgpt_vision_api_with_langchain_in/) , 2024-07-24-0912
```
Made this short tutorial about using ChatGPT Vision API with LangChain in JavaScript

* [https://www.js-craft.io/blog/vi
sion-api-langchain-javascript/](https://www.js-craft.io/blog/vision-api-langchain-javascript/)

Hope you will find it us
eful and any feedback is welcomed!

PS: I think is was of the most fun examples I've recently worked on. Very easy to us
e and has huge product potential. Especially when compared with how things were with TensorFlow.js  [https://www.js-craf
t.io/blog/tensorflowjs-detect-multiple-objects-from-image-coco-ssd-1/](https://www.js-craft.io/blog/tensorflowjs-detect-
multiple-objects-from-image-coco-ssd-1/)
```
---

     
 
all -  [ Tool Calling tutorial for LangChain.js ](https://www.reddit.com/r/LangChain/comments/1ea79dp/tool_calling_tutorial_for_langchainjs/) , 2024-07-24-0912
```
Made this 2 part tutorial about Tool Calling in LangChain.js

* Part 1️: [https://www.js-craft.io/blog/tool-calling-lang
chain-js/](https://www.js-craft.io/blog/tool-calling-langchain-js/)
* Part 2: [https://www.js-craft.io/blog/tool-calling
-langchain-js-toolmessage-schemas/](https://www.js-craft.io/blog/tool-calling-langchain-js-toolmessage-schemas/)

Hope y
ou will find it useful and any feedback is welcomed!



PS: I think it was one of the most time-consuming tutorials to m
ake, as things here are not quite intuitive. At least for me :) 
```
---

     
 
all -  [ Master ve iş arasında tercih ](https://www.reddit.com/r/CodingTR/comments/1ea6wwu/master_ve_iş_arasında_tercih/) , 2024-07-24-0912
```
Merhabalar, ben 2024 haziran ayında sabancı üniversitesi bilgisayar mühendisliği bölümünden mezun oldum ve hali hazırda 
part time olarak çalıştığım şirkette 1 temmuz itibari ile full time olarak devam ettim. Şirkette web front end ekibindey
im ancak daha çok internal projelere bakıyorum ve full stack çalışıyorum bunun yanında da arge tarafında langchain gibi 
toollarla llmler ile uğraşıyorum. Şirkette uzaktan çalışma imkanı mevcut ve yeni mezun birine 2 asgari ücretten fazla öd
üyor. Bununla beraber 2024-2025 fall dönemi için yine sabancı üniversitesinde master kabulü almış bulunuyorum. Bu master
 kabulü burslu ancak burs için haftada en az 20 saat akademik çalışmalara katılmamı bekliyorlar. Bunlar öğrencilere soru
 çözümü sınav/ödev okuma gibi ekstra işler oluyor tabi bir de bunun yanında master tezi ya da paperlar vs için araştırma
  gerçekleştirmem bekleniyor. ikisini aynı anda götürmem pek mümkün görünmüyor ve master sektörde ne kadar önemli pek bi
r bilgim yok. Bu konudaki düşünceleriniz nedir sizce hangisi tercih etmek kariyerim açısında daha mantıklı ?
```
---

     
 
all -  [ txtai: Open-source vector search and RAG for minimalists ](https://www.reddit.com/r/Python/comments/1ea6t89/txtai_opensource_vector_search_and_rag_for/) , 2024-07-24-0912
```
txtai is an all-in-one embeddings database for semantic search, LLM orchestration and language model workflows. 

**What
 it does**

txtai was created back in 2020 starting with semantic search of medical literature. It has since grown into 
a framework for vector search, retrieval augmented generation (RAG) and large language model (LLM) orchestration/workflo
ws.

The goal of txtai is to be simple, performant, innovative and easy-to-use. It had vector search before many current
 projects existed. Semantic Graphs were added in 2022 before the Generative AI wave of 2023/2024. GraphRAG is a hot topi
c but txtai had examples of using graphs to build search contexts back in 2022/2023.

There is a commitment to quality a
nd performance, especially with local models. For example, it's vector embeddings component streams vectors to disk duri
ng indexing and uses mmaped arrays to enable indexing large datasets locally on a single node. txtai's BM25 component is
 built from the scratch to work efficiently in Python leading to 6x better memory utilization and faster search performa
nce than the BM25 Python library most commonly used.

I often see others complain about AI/LLM/RAG frameworks, so I want
ed to share this project as many don't know it exists.

Link to source (Apache 2.0): [https://github.com/neuml/txtai](ht
tps://github.com/neuml/txtai)

**Target Audience**

Developers who want to build AI/LLM/RAG applications with a simple a
pproach.

**Comparison**

txtai is similar to LangChain and LlamaIndex. From a vector database standpoint, it's similar 
to ChromaDB.   
  
See the following post for a detailed comparison.

[https://www.reddit.com/r/txtai/comments/1e5nw3t/v
ector\_search\_rag\_landscape\_a\_review\_with\_txtai/](https://www.reddit.com/r/txtai/comments/1e5nw3t/vector_search_ra
g_landscape_a_review_with_txtai/)
```
---

     
 
all -  [ RAG for JSON ](https://www.reddit.com/r/LangChain/comments/1ea5lco/rag_for_json/) , 2024-07-24-0912
```
Can we apply RAG to JSON files. Currently we are using unstructured for parsing different types of file types. But, it d
oesn't have integration with json file. Can anyone experienced this before?
```
---

     
 
all -  [ Applying RAG to Large-Scale Code Repositories - Guide ](https://www.reddit.com/r/LangChain/comments/1ea4nhz/applying_rag_to_largescale_code_repositories_guide/) , 2024-07-24-0912
```
The article discusses various strategies and techniques for implementing RAG to large-scale code repositories, as well a
s potential benefits and limitations of the approach as well as show how RAG can improve developer productivity and code
 quality in large software projects: [RAG with 10K Code Repos](https://www.codium.ai/blog/rag-for-large-scale-code-repos
/)
```
---

     
 
all -  [ Docker image with Ollama and langchain  ](https://www.reddit.com/r/LangChain/comments/1ea4ccw/docker_image_with_ollama_and_langchain/) , 2024-07-24-0912
```
Hi, 
Need help in finding a docker image containing both Ollama and langchain to ease the creation/development of use ca
ses. 
```
---

     
 
all -  [ Human In The Loop In Langgraph ](https://www.reddit.com/r/LangChain/comments/1ea3p2i/human_in_the_loop_in_langgraph/) , 2024-07-24-0912
```
    from langgraph_state import GraphState
    from langgraph.graph import END, StateGraph
    from langgraph.checkpoint
.memory import MemorySaver
    from nodes import build_strategy, human_feedback, decision_node, rag_node, database_searc
h, web_search_node, sql_search_node, state_printer
    from edges import rag_database_websearch_sqlseqrch, strategy_deci
sion
    workflow = StateGraph(GraphState)
    workflow.add_node('build_strategy', build_strategy)
    workflow.add_node
('human_feedback', human_feedback)
    workflow.add_node('decision_node', decision_node)
    workflow.add_node('rag_node
', rag_node)
    workflow.add_node('database_search', database_search)
    workflow.add_node('web_search_node', web_sear
ch_node)
    workflow.add_node('sql_search_node', sql_search_node)
    workflow.add_node('state_printer', state_printer)

    workflow.set_entry_point('build_strategy')
    workflow.add_edge('build_strategy', 'human_feedback')
    workflow.a
dd_conditional_edges(
    'human_feedback',
    strategy_decision,
    {
    'yes': 'decision_node',
    'no': 'build_st
rategy'
    },
    )
    workflow.add_conditional_edges(
    'decision_node',
    rag_database_websearch_sqlseqrch,
    
{
    'rag': 'rag_node',
    'database_search': 'database_search',
    'web_search': 'web_search_node',
    'sql_search'
: 'sql_search_node',
    'state_printer': 'state_printer'
    },
    )
    workflow.add_conditional_edges(
    'rag_node
',
    rag_database_websearch_sqlseqrch,
    {
    'rag': 'rag_node',
    'database_search': 'database_search',
    'web
_search': 'web_search_node',
    'sql_search': 'sql_search_node',
    'state_printer': 'state_printer'
    },
    )
    
workflow.add_conditional_edges(
    'database_search',
    rag_database_websearch_sqlseqrch,
    {
    'rag': 'rag_node'
,
    'database_search': 'database_search',
    'web_search': 'web_search_node',
    'sql_search': 'sql_search_node',
  
  'state_printer': 'state_printer'
    },
    )
    workflow.add_conditional_edges(
    'web_search_node',
    rag_datab
ase_websearch_sqlseqrch,
    {
    'rag': 'rag_node',
    'database_search': 'database_search',
    'web_search': 'web_s
earch_node',
    'sql_search': 'sql_search_node',
    'state_printer': 'state_printer'
    },
    )
    workflow.add_con
ditional_edges(
    'sql_search_node',
    rag_database_websearch_sqlseqrch,
    {
    'rag': 'rag_node',
    'database_
search': 'database_search',
    'web_search': 'web_search_node',
    'sql_search': 'sql_search_node',
    'state_printer
': 'state_printer'
    },
    )
    workflow.add_edge('state_printer', END)
    memory = MemorySaver()
    app = workflo
w.compile(checkpointer=memory, interrupt_before=['human_feedback'])

I have created a graph with human feedback using la
nggraph. After **strategy node** is executed. It should interrupt before **human\_feedback node** and ask from the user 
that if the strategy made by the agent is correct or wrong in case if it is correct it will proceed to the next nodes an
d if not then it will go to strategy node again.

For my first condition in case it is correct it is working fine. But w
hen it is wrong the strategy node executes but donot go to the next nodes and the program terminates.

This is the issue
 if anyone can help. Thanks
```
---

     
 
all -  [ Troubleshooting string Errors in LangChain ](https://www.reddit.com/r/LangChain/comments/1ea2inm/troubleshooting_string_errors_in_langchain/) , 2024-07-24-0912
```
Hi all,

I'm using the LangChain React agent infrastructure and encountering various string-related issues.   
For insta
nce, I often get errors like:

* 'The model produced invalid content. Consider modifying your prompt if you are seeing t
his error persistently.'
* 'Could not parse LLM output.'
* 'An output parsing error occurred.'

Currently, I have some a
d-hoc methods to fix the outputs, which involve a lot of string manipulation. I'm wondering if this is the right approac
h to handle these issues.

I tried using the handle\_parsing\_errors argument, but it doesn't seem to be a good solution
.

What do you think?
```
---

     
 
all -  [ CS RAG CHATBOT for a hardware e-com company ](https://www.reddit.com/r/LangChain/comments/1ea0qw5/cs_rag_chatbot_for_a_hardware_ecom_company/) , 2024-07-24-0912
```
I would love to get your expertise and advice on building a RAG chatbot for an e-commerce company. I'm currently explori
ng Graph-RAG and hybrid search, but I'm feeling overwhelmed by the amount of data. The company has about 100 products, a
long with data such as blogs, articles, FAQs, etc., which sometimes reference specific products. I would like to know ho
w I can move forward with this project. Any help is much appreciated.

Thanks!
```
---

     
 
all -  [ Make your own Intelligent Investment Analyst Agent ](https://www.reddit.com/r/LangChain/comments/1e9ys5f/make_your_own_intelligent_investment_analyst_agent/) , 2024-07-24-0912
```
Hey everyone! I’m excited to share a new project: an Investment Research Project leveraging CrewAI and Composio to condu
ct investment research, analyze data, and provide investment recommendations.

**Objectives**  
This project sets up 
a system of agents to streamline investment research and analysis, ultimately generating insightful investment recommend
ations.  
Implementation Details

**Tools Used**  
Composio, CrewAI, SERP, Python

**Setup**

1. Navigate to the
 project directory.
2. Run the setup file.
3. Fill in the `.env` file with your secrets.
4. Run the Python script.
5
. Alternatively, run the IPython Notebook `investment_analyst.ipynb` in Jupyter for an interactive experience.

**Resu
lts**  
The system will populate your Notion page with comprehensive investment data and analysis.

**Repo**: [GitHub
 Repository](https://git.new/Invest)

Feel free to explore the project, give it a star if you find it useful, and let 
me know your thoughts or suggestions for improvements!
```
---

     
 
all -  [ Lightweight python DAG framework ](https://www.reddit.com/r/Python/comments/1e9wrve/lightweight_python_dag_framework/) , 2024-07-24-0912
```
**What my project does:**

[https://github.com/dagworks-inc/hamilton/](https://github.com/dagworks-inc/hamilton/) I've b
een working on this for a while.

If you can model your problem as a [directed acyclic graph (DAG)](https://en.wikipedia
.org/wiki/Directed_acyclic_graph) then you can use Hamilton; it just needs a python process to run, no system installati
on required (\`pip install sf-hamilton\`).

For the pythonistas, Hamilton does some  cute 'meta programming' by using th
e python functions to \_really\_ reduce boilerplate for defining a DAG. The below defines a DAG by the way the functions
 are named, and what the input arguments to the functions are, i.e. it's a 'declarative' framework.:

    #my_dag.py
   
 def A(external_input: int) -> int:
       return external_input + 1
    
    def B(A: int) -> float:
       '''B depend
s on A'''
       return A / 3
    
    def C(A: int, B: float) -> float:
       '''C depends on A & B'''
       return A
 ** 2 * B

Now you don't call the functions directly (well you can it is just a python module), that's where Hamilton he
lps orchestrate it:

    from hamilton import driver
    import my_dag # we import the above
    
    # build a 'driver'
 to run the DAG
    dr = (
       driver.Builder()
         .with_modules(my_dag)
        #.with_adapters(...) we have m
any you can add here. 
         .build()
    )
    
    # execute what you want, Hamilton will only walk the relevant pa
rts of the DAG for it.
    # again, you 'declare' what you want, and Hamilton will figure it out.
    dr.execute(['C'], 
inputs={'external_input': 10}) # all A, B, C executed; C returned
    dr.execute(['A'], inputs={'external_input': 10}) #
 just A executed; A returned
    dr.execute(['A', 'B'], inputs={'external_input': 10}) # A, B executed; A, B returned.
 
   
    # graphviz viz
    dr.display_all_functions('my_dag.png') # visualizes the graph.

Anyway I thought I would shar
e, since it's broadly applicable to anything where there is a DAG:

* web requests (Hamilton has [async support](https:/
/github.com/dagworks-inc/hamilton/tree/main/examples/async))
* data processing (e.g. [pyspark](https://github.com/DAGWor
ks-Inc/hamilton/tree/main/examples/spark))
* [machine learning ](https://github.com/DAGWorks-Inc/hamilton/tree/main/exam
ples/spark)
* [LLM workflows](https://github.com/DAGWorks-Inc/hamilton/tree/main/examples/LLM_Workflows)
* etc.

I also 
recently curated a bunch of [getting started issues](https://github.com/DAGWorks-Inc/hamilton/issues?q=is%3Aissue+is%3Ao
pen+label%3A%22good+first+issue%22) - so if you're looking for a project, come join.

**Target Audience**

This anyone d
oing python development where a DAG could be of use.

More specifically, Hamilton is built to be taken to production, so
 if you value one or more of:

* self-documenting readable code
* unit testing & integration testing
* data quality
* st
andardized code
* modular and maintainable codebases
* hooks for platform tools & execution
* want something that [can w
ork with Jupyter Notebooks](https://github.com/DAGWorks-Inc/hamilton/blob/main/examples/jupyter_notebook_magic/example.i
pynb) & production.
* etc

Then Hamilton has all these in an accessible manner.

**Comparison**

|Project|Comparison to 
Hamilton|
|:-|:-|
|Langchain's LCEL|LCEL isn't general purpose & in my opinion unreadable.  See [https://hamilton.dagwor
ks.io/en/latest/code-comparisons/langchain/](https://hamilton.dagworks.io/en/latest/code-comparisons/langchain/) .|
|Air
flow / dagster / prefect / argo / etc|Hamilton doesn't replace these. These are 'macro orchestration' systems (they requ
ire DBs, etc), Hamilton is but a humble library and can actually be used with them! In fact it ensures **your code can r
emain decoupled & modular**, enabling you to replace these systems easily. |
|Dask|Dask is a whole system. In fact [Hami
lton integrates with Dask very nicely](https://github.com/DAGWorks-Inc/hamilton/tree/main/examples/dask/hello_world) -- 
and can help you organize your dask code.|

If you have more you want compared - leave a comment.

To finish, if you wan
t to try it in your browser using pyodide @ [https://www.tryhamilton.dev/](https://www.tryhamilton.dev/) you can do that
 too!
```
---

     
 
all -  [ Beginners guide for GraphRAG ](https://www.reddit.com/r/LanguageTechnology/comments/1e9wdpa/beginners_guide_for_graphrag/) , 2024-07-24-0912
```
GraphRAG has been the talk of the town since Microsoft released the viral gitrepo on GraphRAG, which uses Knowledge Grap
hs for the RAG framework to talk to external resources compared to vector DBs as in the case of standard RAG. The below 
YouTube playlist covers the following tutorials to get started on GraphRAG

1. What is GraphRAG?

2. How GraphRAG works?


3. GraphRAG using LangChain

4. GraphRAG for CSV data

5. GraphRAG for JSON

6. Knowledge Graphs using LangChain

7. R
AG vs GraphRAG

[https://www.youtube.com/playlist?list=PLnH2pfPCPZsIaT48BT9zmLmkhYa\_R1PhN](https://www.youtube.com/play
list?list=PLnH2pfPCPZsIaT48BT9zmLmkhYa_R1PhN)
```
---

     
 
all -  [ GraphRAG tutorials for Beginners ](https://www.reddit.com/r/learnmachinelearning/comments/1e9wafo/graphrag_tutorials_for_beginners/) , 2024-07-24-0912
```
GraphRAG has been the talk of the town since Microsoft released the viral gitrepo on GraphRAG, which **uses Knowledge Gr
aphs for the RAG framework** to talk to external resources compared to vector DBs as in the case of standard RAG. The be
low YouTube playlist covers the following tutorials to get started on GraphRAG

1. What is GraphRAG?

2. How GraphRAG wo
rks?

3. GraphRAG using LangChain

4. GraphRAG for CSV data

5. GraphRAG for JSON

6. Knowledge Graphs using LangChain


7. RAG vs GraphRAG

[https://www.youtube.com/playlist?list=PLnH2pfPCPZsIaT48BT9zmLmkhYa\_R1PhN](https://www.youtube.com/
playlist?list=PLnH2pfPCPZsIaT48BT9zmLmkhYa_R1PhN)
```
---

     
 
all -  [ Is there a way to force the prebuilt react agent to call tools (vector store) for each question aske ](https://www.reddit.com/r/LangChain/comments/1e9sc59/is_there_a_way_to_force_the_prebuilt_react_agent/) , 2024-07-24-0912
```
I noticed that it didn't always call the vectorstore when asked a q- and for those answers it was always giving generic 
answers

react agent documentation: [https://langchain-ai.github.io/langgraph/how-tos/create-react-agent/#code](https://
langchain-ai.github.io/langgraph/how-tos/create-react-agent/#code)
```
---

     
 
all -  [ Langchain chatbot integration in Laravel ](https://www.reddit.com/r/LangChain/comments/1e9s7iw/langchain_chatbot_integration_in_laravel/) , 2024-07-24-0912
```
I am developing a chatbot app where I am using Langchain to feed it documents. I have completed the backend logic for th
e app, including controllers, tables and real-time chat (using pusher) in Laravel. I plan to use Flutter for the fronten
d. How can I integrate the model in Laravel?
```
---

     
 
all -  [ Who is using nextjs for their RAG? ](https://www.reddit.com/r/LangChain/comments/1e9mhmn/who_is_using_nextjs_for_their_rag/) , 2024-07-24-0912
```
1. Nextjs / React
2. Streamit
3. Python/Django/Flask

What do you use?
```
---

     
 
all -  [ How to achieve consistency in formatting? ](https://www.reddit.com/r/LangChain/comments/1e9meao/how_to_achieve_consistency_in_formatting/) , 2024-07-24-0912
```
We use json formatted output from OpenAIs GPT-4o.
We have a rather (single) big prompt for table extraction.

What are y
our approaches to achieve consistency in formatting.. especially regarding punctuation of numbers when processing variou
s language formats like Englisch, French, German, Polish, Chinese

Example:

Task 1
Extract all unit prices for all line
 items and return them as an array where each value is formatted as double (xxx.xx)

Task 2
Extract all quantities for a
ll line items and return them as an array where each value is formatted as double (xxx.xx)

Task 3
..


Problem is:
when
 doing this for multiple parts of the table in a single prompt, the formatting gets messed up.


```
---

     
 
all -  [ Looking For a Passionate Collabrator(s)/Fresher Backend Devleoper ](https://www.reddit.com/r/developersIndia/comments/1e9jvhz/looking_for_a_passionate_collabratorsfresher/) , 2024-07-24-0912
```
Looking For a Passionate Collabrator(s)/Fresher Backend Devleoper who eager to learn new things related AI and LLM (in J
S) .  
Only Fresher Or 6 Month Experience , Lets Do work on project.  
Tech Stack=>  
Must Know:  NodeJs (Express/Fastif
y) along With Typesript, Logic Building,  
Optional: NestJs, Golang, Microservices,  
What will We Learn Together: Langc
hain Js, LLM Model Training , TensorflowJS, BrainJs, OnnxJs Runtime,Synaptic, HuggingFace, LLama, KesarJs,TouchJs,Vector
/Chroma/Pinecode DB, etc and much more ... a long list ahead

No Payment or moneyn involved

Only Backend Devs:  
Fronte
nd Wale Dur Rahe
```
---

     
 
all -  [ How to restrict chatbot from answering unrelated questions?  ](https://www.reddit.com/r/LangChain/comments/1e9jii5/how_to_restrict_chatbot_from_answering_unrelated/) , 2024-07-24-0912
```
Hey I'm developing a customer service chatbot that answers questions on a specific topic based on knowledge provided to 
the bot. 
In my system prompt I tell it to only answer related questions and refuse to answer unrelated stuff. However i
t still answers questions like 'why is the sky blue?' and so on. 
Do you guys have any tips on how to improve this? 
```
---

     
 
all -  [ Built a RAG system for internal documents using LangChain, FastAPI, and a frontend with Streamlit. W ](https://www.reddit.com/r/LangChain/comments/1e9j3cq/built_a_rag_system_for_internal_documents_using/) , 2024-07-24-0912
```
Hey all,

This is my first take on something that is related to LLM and RAG systems. I've been working on a Retrieval-Au
gmented Generation (RAG) based question answering system which generate answers to the queries from uploaded documents, 
and I'd love to get your feedback, suggestions, and ideas for improvements. The system uses FastAPI, LangChain and Strea
mlit for a minimal UI.

Key features of the system:

1. Document upload and processing
2. Directory processing for batch
 document addition
3. FAISS vector store for efficient document retrieval
4. GPT4All for generating embeddings and answe
ring questions
5. Asynchronous operations for improved performance
6. WebSocket support for real-time question answering


GitHub Repository: [docGPT](https://github.com/nshefeek/docGPT.git)

Some specific areas I'm looking for feedback on:


1. Code quality and best practices.
2. Usage of LangChain.
3. The approach to improve query response timing.
4. A bette
r approach to splitting the documents in such a way that the embeddings generated maintains a metadata that can be used 
to trace back to the original source doument.

Current state of the project:

* Able to upload a PDF, TXT or CSV documen
t.
* Able to upload a directory of PDF documents. But since Streamlit has no widget for folder upload, the folder path h
as to be input as text.
* Queries return somewhat relevant answers, but the returned metadata can't be used to backtrack
 to the exact source location (like the paragraph from which the answer was inferred etc.).
* Query times vary between 1
20-180 seconds.

Thank you in advance for your time and expertise. I'm looking forward to your insights and suggestions 
to help improve this project!
```
---

     
 
all -  [ Chroma DB taking long time to populate ](https://www.reddit.com/r/LangChain/comments/1e9h5dq/chroma_db_taking_long_time_to_populate/) , 2024-07-24-0912
```
When I populate my chromadb, it takes a long time. To add \~3,000 docs can take upwards of 10 minutes, and adding any mo
re docs afterwards will take much longer. When adding to the db, it is only using \~10% GPU and CPU usage. Is there any 
way to speed this process up or use more resources when populating the DB?

For context, I'm using random textbooks to p
opulate the DB with rn, but this issue happens no matter the content I'm adding to the DB.

    #Embedding function I us
e
    embeddings = OllamaEmbeddings(model='nomic-embed-text')
    
    #This block is what takes forever
    new_chunk_i
ds = [chunk.metadata['id'] for chunk in new_chunks]
    db.add_documents(new_chunks, ids=new_chunk_ids)
```
---

     
 
all -  [ Is the new open-sourced mem0 ready for production? ](https://www.reddit.com/r/LLMDevs/comments/1e9gh7z/is_the_new_opensourced_mem0_ready_for_production/) , 2024-07-24-0912
```
Hello, fellos,

I am newbie on LLM dev, and currently looking for a way to build an chat app with context history memory
 and ability to search on the web.  A little overwhelmed by all the stuff like langchain, llamaindex, phidata…… any reco
mmendations for a not-that-large project?

Should I just use mem0 for the memory thing and another package for searching
?
```
---

     
 
all -  [ Knowledge Graph LangChain codes explained ](https://www.reddit.com/r/Langchaindev/comments/1e9ey72/knowledge_graph_langchain_codes_explained/) , 2024-07-24-0912
```
Knowledge Graph is the buzz word since GraphRAG has came in which is quite useful for Graph Analytics over unstructured 
data. This video demonstrates how to use LangChain to build a stand alone Knowledge Graph from text : https://youtu.be/Y
nhG_arZEj0
```
---

     
 
all -  [ Automatic RAG Evaluation + Monitoring ](https://www.reddit.com/r/LangChain/comments/1e9e3lb/automatic_rag_evaluation_monitoring/) , 2024-07-24-0912
```
Hey everyone,

What are you using to evaluate and monitor your RAG applications?  
  
I've been using LangSmith, but I'm
 not satisfied with it so far. In my opinion, the UX is bad and it lacks an effective way to compare different prompts. 
I'm now considering experimenting with PromptLayer, as it seems to offer better features.  
  
Our situation is a bit co
mplex, though. We're experimenting with two different approaches: a multi-chain setup and one based on function calling.
 So we're really looking to compare entire workflows rather than just individual prompts.

Has anyone found a good solut
ion for monitoring, and more importantly, evaluating these kinds of setups? I'd appreciate any insights or recommendatio
ns.
```
---

     
 
all -  [ How to best tackle RAG for multiple documents with multiple topics? ](https://www.reddit.com/r/LangChain/comments/1e9c81i/how_to_best_tackle_rag_for_multiple_documents/) , 2024-07-24-0912
```
I'm building a chatbot with RAG system for a school, and they want to have all the courses and classes as *knowledge,* s
o students can ask *anything* and the bot should get the answer from all this knowledge*.* I'm having a hard time figuri
ng out how to tackle this, at the moment it's like 50 pdfs, with a lot of pages, for 5 courses, and with many different 
topics. So if a students asks 'What is the best way to do X', the system should somehow look through all these pdfs and 
get the answer, or somehow know which pdfs are the most appropriates to go look for an answer. Not all the documents are
 relevant for a particular question, most likely just one/two/three documents will be relevant.

What I'm doing now is a
dding 'tags', so the people uploading these documents should add one or more tags: 'course 1, tool X, some-other-keyword
', so when someone asks a question, I first try to see if the question matches some of the tags, and then just go get th
e pdfs with those tags.

tldr: how to implement RAG when the knowledge is a lot of different files talking about differe
nt topics.
```
---

     
 
all -  [ Would RAG be useful in this caes ? ](https://www.reddit.com/r/LangChain/comments/1e9c226/would_rag_be_useful_in_this_caes/) , 2024-07-24-0912
```
I trained a Llama2 7b chat model with QLoRA on customer support discussions (Instruction/Output format), and i'm trying 
to find a way to insert knowledge in the model, mainly about fixed information (Products in the store, customer service 
phone number, store opening hours...). Would implementing RAG would be a good idea ?
```
---

     
 
all -  [ Mult-React-agents workflow using Langgraph ](https://www.reddit.com/r/LangChain/comments/1e9bnwm/multreactagents_workflow_using_langgraph/) , 2024-07-24-0912
```
I am facing a problem, I am using:

`from langgraph.prebuilt import create_react_agent`

to create a react agent but thi
s react agent is already complied `langgraph.graph.state.CompiledStateGraph`

And now, I wanna have two more react agent
s and add those agents in the graph but there is no way to the best of my knowledge. 

    react_agent_1 = create_react_
agent(model, tools=tools, messages_modifier=prompt)
    react_agent_2 = create_react_agent(model, tools=tools, messages_
modifier=prompt)
    react_agent_3 = create_react_agent(model, tools=tools, messages_modifier=prompt)

Now I wanna have 
the `react_agent_1` as the parent/supervisor agent and`react_agent_2` and and`react_agent_3`as child agents. Now, how ca
n I add these two agents in the already compiled graph as the other two are agents are also the complied graphs.    
```
---

     
 
all -  [ What Is LangChain, and How Does It Work? ](https://www.reddit.com/r/TechChilli/comments/1e9atzk/what_is_langchain_and_how_does_it_work/) , 2024-07-24-0912
```
# Learn about LangChain, a powerful tool for developing applications with large language models. Discover its features, 
how it works, and its impact on AI-driven solutions.

See here - [https://techchilli.com/artificial-intelligence/what-is
-langchain/](https://techchilli.com/artificial-intelligence/what-is-langchain/)
```
---

     
 
all -  [ Langgraph: what is the advantage of use Toolnodes with llm.bind_tools vs just using an agent with to ](https://www.reddit.com/r/LangChain/comments/1e9ap85/langgraph_what_is_the_advantage_of_use_toolnodes/) , 2024-07-24-0912
```
I see different implementations of Langggraph online, usually the most complex use toolnodes and the agents can only req
uest a tool to be used, not using the tool themselves (i.e. they use bind\_tools).   
The approach with tool\_node seem 
to make the graph more complex and bureaucratic. Is there any use case in which we shouldn't just give the tools to the 
agent? What is the advantage of the ToolNode approach?
```
---

     
 
MachineLearning -  [ [D] Embedding generation in production? How are you doing it? ](https://www.reddit.com/r/MachineLearning/comments/1e7xt6k/d_embedding_generation_in_production_how_are_you/) , 2024-07-24-0912
```


For those building production RAG pipelines, how are you generating embeddings. More than which model, I'm interested 
in how your deploying it. Are you calling the openai/vertex API endpoint directly? Using langchain/llamaindex wrappers? 
Using vectordb  classes? Or some other way?
```
---

     
 
MachineLearning -  [ [D] Is Anyone Else Setting Up Real-Time Django Workers for their AI Application? What's the best way ](https://www.reddit.com/r/MachineLearning/comments/1e0qens/d_is_anyone_else_setting_up_realtime_django/) , 2024-07-24-0912
```
We completely underestimated this one tbh, thought it would be much more straight forward. But we've done it now and doc
umented how step by step [in this article series](https://medium.com/p/5828a1ea43a3).

A bit of context, we're building 
a mini free AI Agent that auto-generates manually customisable plots, so the user can basically style however they want.
 It needs to be cost effective and efficient, so we thought about how to do it and tested a couple other ways.

https://
preview.redd.it/cmly0a6bhwbd1.png?width=640&format=png&auto=webp&s=be1f5b2853e744adcaf8013e6d43b43f6be89617

We plan on 
releasing the project open source, so all feedback welcome! Is anyone else doing this and has any feedback? or do know o
f a better way to do it?
```
---

     
 
MachineLearning -  [ [P] Real Time AI Workers Web Application ](https://www.reddit.com/r/MachineLearning/comments/1dzryk9/p_real_time_ai_workers_web_application/) , 2024-07-24-0912
```
Hi everyone!

I've created a mini series on how to build a real time AI application using Django, LangChain and Celery.


Free knowledge - posting it in here for anyone working on something similar and had the same blockers I had when buildi
ng.

Let me know what you think on how I could potentially improve this architecture.

Part 1

[https://medium.com/towar
dsdev/how-to-set-up-django-from-scratch-with-celery-channels-redis-docker-real-time-django-601dff7ada79](https://medium.
com/towardsdev/how-to-set-up-django-from-scratch-with-celery-channels-redis-docker-real-time-django-601dff7ada79)

Part 
2

[https://medium.com/towardsdev/how-to-set-up-django-from-scratch-with-celery-channels-redis-docker-real-time-django-5
828a1ea43a3](https://medium.com/towardsdev/how-to-set-up-django-from-scratch-with-celery-channels-redis-docker-real-time
-django-5828a1ea43a3)

Part 3

[https://medium.com/towardsdev/how-to-set-up-django-from-scratch-with-celery-channels-red
is-docker-real-time-django-8e73c7b6b4c8](https://medium.com/towardsdev/how-to-set-up-django-from-scratch-with-celery-cha
nnels-redis-docker-real-time-django-8e73c7b6b4c8)

Part 4

[https://medium.com/towardsdev/how-to-set-up-django-from-scra
tch-with-celery-channels-redis-docker-real-time-django-c090c300517a](https://medium.com/towardsdev/how-to-set-up-django-
from-scratch-with-celery-channels-redis-docker-real-time-django-c090c300517a)

Part 5  
[https://medium.com/@cubode/how-
to-set-up-django-from-scratch-with-celery-channels-redis-docker-real-time-django-0845eb7e083c](https://medium.com/@cubod
e/how-to-set-up-django-from-scratch-with-celery-channels-redis-docker-real-time-django-0845eb7e083c)
```
---

     
 
deeplearning -  [ Llama 3 not running on GPU ](https://www.reddit.com/r/deeplearning/comments/1dptxsr/llama_3_not_running_on_gpu/) , 2024-07-24-0912
```
I dont know much theory about RAG but i need to implement it for a project.  
**I want to run llama3 on my GPU to get fa
ster results.**

`from langchain_community.llms import Ollama`  
`llm = Ollama(model='llama3',num_gpu=1)`  
`def generat
e_response(prompt, similar_jobs):`  
`descriptions = '\n\n'.join([job['Description'] for job in similar_jobs])`  
`augme
nted_prompt = f'{prompt}\n\nHere are some job recommendations based on your query:\n{descriptions}'`  
`for chunks in ll
m.stream(augmented_prompt):`  
`print(chunks, end='')`

I am giving llama3 my *'user prompt'* and top 5 nearest *'simila
r\_jobs'* using cosine similarity.  
This code goes not use my GPU but my CPU and RAM usage is high.

**My gpu usage is 
0%** , i have a Nvidia GeForce RTX 3050 Laptop GPU GDDR6 @ 4GB (128 bits)
```
---

     
