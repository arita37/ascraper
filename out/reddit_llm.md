 
all -  [ Applied to 200+ Internship roles, got no callback.Please roast my resume! ](https://i.redd.it/4oktn3jczxfd1.png) , 2024-08-01-0912
```

```
---

     
 
all -  [ Spoke to 22 LangGraph devs and here's what we found ](https://www.reddit.com/r/LangChain/comments/1eh0ly3/spoke_to_22_langgraph_devs_and_heres_what_we_found/) , 2024-08-01-0912
```
I recently had our AI interviewer speak with 22 developers who are building with LangGraph. The interviews covered vario
us topics, including how they're using LangGraph, what they like about it, and areas for improvement. I wanted to share 
the key findings because I thought you might find it interesting.

# Use Cases and Attractions

LangGraph is attracting 
developers from a wide range of industries due to its versatility in managing complex AI workflows. Here are some intere
sting use cases:

1. **Content Generation:** Teams are using LangGraph to create systems where multiple AI agents collab
orate to draft, fact-check, and refine research papers in real-time.
2. **Customer Service:** Developers are building dy
namic response systems that analyze sentiment, retrieve relevant information, and generate personalized replies with bui
lt-in clarification mechanisms.
3. **Financial Modeling:** Some are building valuation models in real estate that adapt 
in real-time based on market fluctuations and simulated scenarios.
4. **Academic Research**: Institutions are developing
 adaptive research assistants capable of gathering data, synthesizing insights, and proposing new hypotheses within a si
ngle integrated system.

# What Attracts Developers to LangGraph?

1. **Multi-Agent System Orchestration**: LangGraph ex
cels at managing multiple AI agents, allowing for a divide-and-conquer approach to complex problems.'We are working on a
 project that requires multiple AI agents to communicate and talk to one another. LangGraph helps with thinking through 
the problem using a divide-and-conquer approach with graphs, nodes, and edges.' - Founder, Property Technology Startup
2
. **Workflow Visualization and Debugging**: The platform's visualization capabilities are highly valued for development 
and debugging.'LangGraph can visualize all the requests and all the payloads instantly, and I can debug by taking LangGr
aph. It's very convenient for the development experience.' - Cloud Solutions Architect, Microsoft
3. **Complex Problem-S
olving**: Developers appreciate LangGraph's ability to tackle intricate challenges that traditional programming struggle
s with.'Solving complex problems that are not, um, possible with traditional programming.' - AI Researcher, Nokia
4. **A
bstraction of Flow Logic**: LangGraph simplifies the implementation of complex workflows by abstracting flow logic.'\[La
ngGraph helped\] abstract the flow logic and avoid having to write all of the boilerplate code to get started with the p
roject.' - AI Researcher, Nokia
5. **Flexible Agentic Workflows**: The tool's adaptability for various AI agent scenario
s is a key attraction.'Being able to create an agentic workflow that is easy to visualize abstractly with graphs, nodes,
 and edges.' - Founder, Property Technology Startup

# LangGraph vs Alternatives

The most commonly considered alternati
ves were CrewAI and Microsoft's Autogen. However, developers noted several areas where LangGraph stands out:

1. **Handl
ing Complex Workflows:** Unlike some competitors limited to simple, linear processes, LangGraph can handle complex graph
 flows, including cycles.'CrewAI can only handle DAGs and cannot handle cycles, whereas LangGraph can handle complex gra
ph flows, including cycles.' -  Developer
2. **Developer Control:** LangGraph offers a level of control that many find u
nmatched, especially for custom use cases.'We did tinker a bit with CrewAI and Meta GPT. But those could not come even n
ear as powerful as LangGraph. And we did combine with LangChain because we have very custom use cases, and we need to ha
ve a lot of control. And the competitor frameworks just don't offer that amount of, control over the code.' - Founder, G
enAI Startup
3. **Mature Ecosystem:** LangGraph's longer market presence has resulted in more resources, tools, and infr
astructure.'LangGraph has the advantage of being in the market longer, offering more resources, tools, and infrastructur
e. The ability to use LangSmith in conjunction with LangGraph for debugging and performance analysis is a significant di
fferentiator.' -  Developer
4. **Market Leadership:** Despite a volatile market, LangGraph is currently seen as a leader
 in functionality and tooling for developing workflows.'Currently, LangGraph is one of the leaders in terms of functiona
lity and tooling for developing workflows. The market is volatile, and I hope LangGraph continues to innovate and create
 more tools to facilitate developers' work.' - Developer

# Areas for Improvement

While LangGraph has garnered praise, 
developers also identified several areas for improvement:

1. **Simplify Syntax and Reduce Complexity:** Some developers
 noted that the graph-based approach, while powerful, can be complex to maintain.'Some syntax can be made a lot simpler.
' - Senior Engineering Director, BlackRock
2. **Enhance Documentation and Community Resources:** There's a need for more
 in-depth, complex examples and community-driven documentation.'The lack of how-to articles and community-driven documen
tation... There's a lot of entry-level stuff, but nothing really in-depth or complex.' - Research Assistant, BYU
3. **Im
prove Debugging Capabilities:** Developers expressed a need for more detailed debugging information, especially for trac
king state within the graph.'There is a need for more debugging information. Sometimes, the bug information starts from 
the instantiation of the workflow, and it's hard to track the state within the graph.' - Senior Software Engineer, Canad
ian Government Agency
4. **Better Human-in-the-Loop Integration:** Some users aren't satisfied with the current implemen
tation of human-in-the-loop concepts.'More options around the human-in-the-loop concept. I'm not a very big fan of their
 current implementation of that.' - AI Researcher, Nokia
5. **Enhanced Subgraph Integration:** Multiple developers menti
oned issues with integrating and combining subgraphs.'The possibility to integrate subgraphs isn't compatible with \[gra
ph drawing\].' - Engineer, IT Consulting Company 'I wish you could combine smaller graphs into bigger graphs more easily
.' - Research Assistant, BYU
6. **More Complex Examples:** There's a desire for more complex examples that developers ca
n use as starting points.'Creating more examples online that people can use as inspiration would be fantastic.' - Senior
 Engineering Director, BlackRock

\_\_\_\_  
You can check out the interview transcripts here: [kgrid.ai/company/langgra
ph](http://kgrid.ai/company/langgraph)

Curious to know whether this aligns with your experience? 
```
---

     
 
all -  [ RAG PDF Chat + Web Search ](https://www.reddit.com/r/LangChain/comments/1egyn3g/rag_pdf_chat_web_search/) , 2024-08-01-0912
```
Hi guys I have created a PDF Chat/ Web Search RAG application deployed on Hugging Face Spaces https://shreyas094-searchg
pt.hf.space. Providing the model documentation below please feel free to contribute.

# AI-powered Web Search and PDF Ch
at Assistant

This project combines the power of large language models with web search capabilities and PDF document ana
lysis to create a versatile chat assistant. Users can interact with their uploaded PDF documents or leverage web search 
to get informative responses to their queries.

## Features

- **PDF Document Chat**: Upload and interact with multiple 
PDF documents.
- **Web Search Integration**: Option to use web search for answering queries.
- **Multiple AI Models**: C
hoose from a selection of powerful language models.
- **Customizable Responses**: Adjust temperature and API call settin
gs for fine-tuned outputs.
- **User-friendly Interface**: Built with Gradio for an intuitive chat experience.
- **Docume
nt Selection**: Choose which uploaded documents to include in your queries.

## How It Works

1. **Document Processing**
: 
   - Upload PDF documents using either PyPDF or LlamaParse.
   - Documents are processed and stored in a FAISS vector
 database for efficient retrieval.

2. **Embedding**: 
   - Utilizes HuggingFace embeddings (default: 'sentence-transfor
mers/all-mpnet-base-v2') for document indexing and query matching.

3. **Query Processing**:
   - For PDF queries, relev
ant document sections are retrieved from the FAISS database.
   - For web searches, results are fetched using the DuckDu
ckGo search API.

4. **Response Generation**:
   - Queries are processed using the selected AI model (options include Mi
stral, Mixtral, and others).
   - Responses are generated based on the retrieved context (from PDFs or web search).

5. 
**User Interaction**:
   - Users can chat with the AI, asking questions about uploaded documents or general queries.
   
- The interface allows for adjusting model parameters and switching between PDF and web search modes.

## Setup and Usag
e

1. Install the required dependencies (list of dependencies to be added).
2. Set up the necessary API keys and tokens 
in your environment variables.
3. Run the main script to launch the Gradio interface.
4. Upload PDF documents using the 
file input at the top of the interface.
5. Select documents to query using the checkboxes.
6. Toggle between PDF chat an
d web search modes as needed.
7. Adjust temperature and number of API calls to fine-tune responses.
8. Start chatting an
d asking questions!

## Models

The project supports multiple AI models, including:
- mistralai/Mistral-7B-Instruct-v0.3

- mistralai/Mixtral-8x7B-Instruct-v0.1
- meta/llama-3.1-8b-instruct
- mistralai/Mistral-Nemo-Instruct-2407

## Future I
mprovements

- Integration of more embedding models for improved performance.
- Enhanced PDF parsing capabilities.
- Sup
port for additional file formats beyond PDF.
- Improved caching for faster response times.

## Contribution

Contributio
ns to this project are welcome!


```
---

     
 
all -  [ What's your favorite approach to managing prompt templates? ](https://www.reddit.com/r/LocalLLaMA/comments/1egvdix/whats_your_favorite_approach_to_managing_prompt/) , 2024-08-01-0912
```
By 'prompt template' I mean more than just the format for a particular instruction model. I'm interested in what you do 
to generate prompts.

Approaches I'm aware of:

* Just use formatted strings. Python's got handy string-formatting code 
after all. The drawback is that it only does string substitution
* A custom prompting script format. In the past, I've w
ritten a script parser that takes a text or json file and substitutes variables and does some loop logic and so on. The 
drawback is that I have to implement everything myself and expressing loops or branching starts to get trickier.
* LangC
hain has prompt templates. Drawback: I bounced hard off LangChain last time I tried it; too many abstractions getting in
 the way.
* DSPy has a very elegant way to specify templates via Signature and Module classes; the Modules in particular
 can have arbitrary logic and nest other modules inside making for some elegant structures. Can use the AI to optimize p
rompts. Drawback is that it is a bit opinionated about the exact format of the prompts (which I can adjust externally, b
ut it's a bit off-label at that point).
* txtai: In addition to the very good embeddings features, includes fairly direc
t access to the prompts. Lots and lots of examples in the docs. Drawbacks: needs to work within their pipeline abstracti
on; I haven't used it enough to say if the prompt management is helpful *enough*.

Other stuff I've considered but haven
't used: Burr, Haystack, Pezzo, OpenPrompt, Agenta, LangFuse, LangTail, magnetic, or just using Jinja2 templates.

Some 
of these are geared at managing prompts across large teams; I'm personally interested in smaller, more modular solutions
 for rapid prototyping, but there might be some crossover. I'm aiming for something where there's a few custom-targeted 
prompts rather than a whole raft of them.

My personal #1 prompt management priority is to be able to see when and where
 a prompt went off the rails. I don't want to debug a failed RAG lookup by painfully combing stack traces or stepping th
rough my code. Part of the solution is telemetry and observability, assuming you've got a telemetry library that can tra
ce the prompt assembly and not just the inference requests. But a good bit of it is just having one place where all the 
data is assembled into a prompt, instead of having it all over the place.

What are you doing to create your prompts? Wr
iting them all by hand? Using a library?
```
---

     
 
all -  [ Want to create RAG application for stackoverflow / stackexchange questions and answers. Is it legal  ](https://www.reddit.com/r/LangChain/comments/1egvbm4/want_to_create_rag_application_for_stackoverflow/) , 2024-08-01-0912
```
Hi Folks,

Apologies if the above question does not belong here. But I am create a RAG application, Basically it is a RA
G application for stackoverflow / stackexchange questions and answers.

But my first dilemma is - is it legal to scrape 
answers from stackoverflow / stackexchange?

I am planning to provide links back to the original answer in my app.

Any 
suggestions or advice would be great.
```
---

     
 
all -  [ Create_sql_agent issue ](https://www.reddit.com/r/LangChain/comments/1egub1z/create_sql_agent_issue/) , 2024-08-01-0912
```
Hello everyone. Im building an application using the langchain create_sql_agent constructor: langchain_community.agent_t
oolkits.sql.base.create_sql_agent, for a strange use case that requires finding out which table in an SQL database a par
ticular dataset(which I feed in the prompt as key value pairs of column headers and corresponding 5 values as a list) mo
st resembles. Ive written prompts asking the agent to use the column headers to guess which table the dataset resembles.
 This is happening with llama 3 8b running via ollama. 

The problem is I keep getting an error message which im recalli
ng from my memory like:

ValueError: An outputparsing error occured. In order to pass this back to the agent and have it
 try again, pass handle_parsing_errors = True to the Agent executor.  

However, the create_sql_agent constructor does n
ot even have handle_parsing_errors as a parameter! Anyone have any idea how to resolve this? Im sure i must be getting s
omething wrong. 

For context, I've worked with the AgentExecutor class before which has a parameter handle_parsing_erro
rs, which worked well, but for this specific use case, I need the sql agent. Is there a way to call the sql agent using 
the AgentExecutor? 
```
---

     
 
all -  [ how to send relevant data to llm? ](https://www.reddit.com/r/LangChain/comments/1egt6tz/how_to_send_relevant_data_to_llm/) , 2024-08-01-0912
```
So I am creating a software it scrapes the website, cleans the unwanted html like img, meta tags, script, style etc. and
 now I have a clean html file. Now I have a user description on what he wants from that url for example he want to submi
t a form. then only the form and login form component is important and significant. now I don't want to send the whole h
tml code but in a way trim it down to more relevant code which in this case is only code related to login. maybe omit ht
ml code of header, footer and other unwanted stuff. Now want some guidance how I can achieve this?
```
---

     
 
all -  [ Create robust API over Langchain chains using Langserve ](https://www.reddit.com/r/LangChain/comments/1egn31o/create_robust_api_over_langchain_chains_using/) , 2024-08-01-0912
```
Hello everyone,

Just wrote an article on how to use LangServe to create an API over LangChain chains.  
Here's the [lin
k](https://www.metadocs.co/2024/07/31/easily-create-production-ready-apis-over-your-langchain-chains-using-langserve/). 
 
This is actually something that I use in production in my company :D.

  
Enjoy!
```
---

     
 
all -  [ Interview with Jacob Lee, lead maintainer of LangChain.js ](https://www.reddit.com/r/LangChain/comments/1egmw06/interview_with_jacob_lee_lead_maintainer_of/) , 2024-08-01-0912
```
Hi folks,

Exciting news! Two weeks ago, I had the pleasure of recording a podcast interview with Jacob Lee, the lead ma
intainer of LangChain.js.   
  
Check it out here: [https://www.js-craft.io/blog/interview-jacob-lee-langchain-js/](http
s://www.js-craft.io/blog/interview-jacob-lee-langchain-js/)

During this short talk, we go through topics such as:

* Th
e advantages of using LangChain
* A good roadmap for learning LangChain
* How all the Langs work together (LangGraph, La
ngSmith, LangServe, LangChain itself)
* Using LangChain.js with or without TypeScript 

... and much more.

Listen now::
 [https://www.js-craft.io/blog/interview-jacob-lee-langchain-js/](https://www.js-craft.io/blog/interview-jacob-lee-langc
hain-js/)

  
Hope you will like it, and happy to hear your opinions! 
```
---

     
 
all -  [ Any local and opensource alternative to Adept.ai? ](https://www.reddit.com/r/LocalLLaMA/comments/1egk7n8/any_local_and_opensource_alternative_to_adeptai/) , 2024-08-01-0912
```
So I was wondering, if there is a way for us to automate tasks on the computer like updating tickets on JIRA, doing stuf
f on the computer (maybe just browser to start with)

Found the video from [adept](https://www.adept.ai ) interesting.


Also previously check [langchain webvoyeger](https://github.com/langchain-ai/langgraph/blob/main/examples/web-navigation
/web\_voyager.ipynb)
```
---

     
 
all -  [ Langgraph: What is the best practice for displaying messages to the user as the we move through the  ](https://www.reddit.com/r/LangChain/comments/1egjtsg/langgraph_what_is_the_best_practice_for/) , 2024-08-01-0912
```
Hi, right now my graph is not displaying to the user most of the messages that AI generate as it goes through the graph.
 This is specially bad in steps when I am getting the user confirmation for something, but it would be nice to display s
ome messages as the llm moves from one node to another.   
What is the best practice for that? I've been doing console.p
rint for displaying the last message in the message array in certain parts of the code, but I guess that's not the best 
way to solve it. How do you usually do it?   

```
---

     
 
all -  [ Using Code Compiler as a Tool? ](https://www.reddit.com/r/LangChain/comments/1egirrf/using_code_compiler_as_a_tool/) , 2024-08-01-0912
```
Did anyone try to create a custom tool that can compile your generated code to check if the code is working or not?  
Ca
n I get some help creating this type of custom tool?
```
---

     
 
all -  [ question about retrievers - slow pdf loading times also when using cache ](https://www.reddit.com/r/LangChain/comments/1eghtid/question_about_retrievers_slow_pdf_loading_times/) , 2024-08-01-0912
```
Hey everyone,

I’ve been working with LangChain to create an efficient document retriever using embeddings and caching m
echanisms. I ran into a problem where the PyPDF loading process takes a substantial amount of time, and I believe this c
an be optimized by leveraging caching because i can only access the specifc location in the pdf where the retrieved cont
ext is - but the code right now doesn't achieve this.

my question is then - how to achieve this more efficient functino
ality. 

Here's my original setup:

  
`from langchain_community.vectorstores import Chroma`

`from langchain_openai imp
ort OpenAIEmbeddings`

`from langchain.storage import LocalFileStore`

`from langchain.embeddings import CacheBackedEmbe
ddings`

`from langchain_community.document_loaders import PyPDFLoader`

`from langchain.text_splitter import RecursiveC
haracterTextSplitter`



`def load_jodrag_retriever(use_cache=True, chunk_size=2500, chunk_overlap=300, num_docs_retriev
e=2):`

`embed = OpenAIEmbeddings()`

`docs = load_jodrag(chunk_size=chunk_size, chunk_overlap=chunk_overlap)`

`retriev
er = retriever_setup(docs, use_cache=use_cache, embed=embed, num_docs_retrieve=num_docs_retrieve)`

`return retriever`




`def load_rag(path = 'paper1.pdf', chunk_size = 500, chunk_overlap = 20):`

`loader = PyPDFLoader(path)`

`pages = loa
der.load()`

`pages = pages[9:360]`

`text = ''`

`for page in pages:`

`text += page.page_content`

`text = text.replac
e('\t', ' ')`

`text_splitter = RecursiveCharacterTextSplitter(separators=['\n\n', '\n', '\t'], chunk_size=chunk_size, c
hunk_overlap=chunk_overlap)`

`docs = text_splitter.create_documents([text])`

`return docs`



`def retriever_setup(doc
s, use_cache=True, cache_dir= './cache/', embed=OpenAIEmbeddings(), num_docs_retrieve=2):`

`if use_cache:`

`store = Lo
calFileStore(cache_dir)`

`cached_embedder = CacheBackedEmbeddings.from_bytes_store(embed, store, namespace=embed.model)
`

`vectorstore = Chroma.from_documents(docs, cached_embedder)`

`else:`

`vectorstore = Chroma.from_documents(documents
=docs, collection_name='rag-chroma', embedding=embed)`

`retriever = vectorstore.as_retriever(search_kwargs={'k': num_do
cs_retrieve})`

`return retriever`


```
---

     
 
all -  [ GPT Graph: A Flexible Pipeline Library ](https://www.reddit.com/r/LangChain/comments/1egh70y/gpt_graph_a_flexible_pipeline_library/) , 2024-08-01-0912
```
ps: This is a repost (2 days ago). Reddit decided to shadow-ban my previous new account simply because i have posted thi
s. They mark it as 'scam'. I hope they will not do so again this time, like this is using a open source license and i di
dn't get any commercial benefit from it.

# Introduction (skip this if you like)

I am an intermediate self-taught pytho
n coder with no formal CS experience. I have spent 5 months for this and learnt a lot when writing this project. I have 
never written anything this complicated before, and I have rewrite this project from scratch at least several times. The
re are many smaller-scale rewrite when i am not satisfied with the structure of anything. I hope it is useful for somebo
dy. (Also warning, this might not be the most professional piece of code) Any feedback is appreciated!

# What My Projec
t Does

GPT Graph is a pipeline for llm data transfer. When I first studied LangChain, I don't understand why we need a 
server(langsmith) to do debug, and things get so complicated. Therefore, i have spent time in order to write a pipeline 
structure targeting being flexible and easy to debug. While it's still in early development and far less sophisticated a
s Langchain, I think my idea is better at least in some way in turns of how to abstract things (maybe i am wrong).

This
 library allows you to create more complex pipelines with features like dynamic caching, conditional execution, and easy
 debugging.

The main features of GPT Graph include:

1. Component-based pipelines
2. Allowing nested Pipeline
3. Dynami
c caching according to defined keys
4. Conditional execution of components using bindings or linkings
5. Debugging and a
nalysis methods
6. Priority Queue to run Steps in the Pipeline
7. Parameters can be updated with priority score. (e.g. i
f a Pipeline contains 4 Components, you can write config files for each of the Component and Pipeline, as Pipeline has h
igher priority than each component, if there are any conflict in parameters, the parent Pipeline's parameters will be us
ed)
8. One of the key advantages of GPT Graph is its debuggability. Every output is stored in a node (a dict with struct
ure {'content':xxx, “extra”:xxx})

The following features are lacking (They are all TODO in the future)

1. currently al
l are using sync mode
2. No database is used at this moment. All data stored in networkx graph's wrapper.
3. No RAG at t
his moment. Although I have already written some prototype for it, basically calculate the vector and store in the nodes
. They are not submitted yet.

# Example

    from gpt_graph.core.pipeline import Pipeline  
    from gpt_graph.core.dec
orators.component import component
    
    @component()  
    def greet(x):  
    return x + ' world!'
    
    pipelin
e = Pipeline()  
    pipeline | greet()
    
    result = pipeline.run(input_data='Hello')  
    print(result) # Output:
 ['Hello world!']  

# Comparison

As for as I know and my understanding(which may be wrong)(e.g. Langgraph or Langchain
), there is no framework that can do nested pipeline, or using priority queue.

# Target Audience

Fast prototyping and 
small project related to llm data pipelines. It is because currently everything is stored as a wrapper of networkx graph
 (including outputs of each Step and step structure). Later I may write implementation for graph database, although I do
n't have the skill now.

# Welcome Feedback and Contributions

I welcome any comments, recommendations, or contributions
 from the community.  
I know that as someone that releases his first complicated project (at least for me), there may b
e a lot of things that i am not doing correctly, including documentations/ writing style/ testing or others. So any reco
mmendation is encouraged! Your feedback will be invaluable for me.  
If you have any questions about the project, feel f
ree to ask me as well. My documentation may not be the easiest to understand. I will soon take a long holiday for severa
l months, and when I come back I will try to enhance this project to a better and usable level.  
The license now is GPL
 v3, if more people feel interested in or contribute to the project, i will consider change it to more permissive licens
e.

# Link to Github

[https://github.com/Ignorance999/gpt\_graph](https://github.com/Ignorance999/gpt_graph)

# Link to
 Documentation

[https://gpt-graph.readthedocs.io/en/latest/hello\_world.html](https://gpt-graph.readthedocs.io/en/lates
t/hello_world.html)

# More Advanced Example (you can check documentation tutorial 1 Basics):

    class z:
        def 
__init__(self):
            self.z = 0
    
        def run(self):
            self.z += 1
            return self.z
   
 
    @component(
        step_type='node_to_list',
        cache_schema={
            'z': {
                'key': '[c
p_or_pp.name]',
                'initializer': lambda: z(),
            }
        },
    )
    def f4(x, z, y=1):
      
  return x + y + z.run(), x - y + z.run()
    
    @component(step_type='list_to_node')
    def f5(x):
        return np
.sum(x)
    
    @component(
        step_type='node_to_list',
        cache_schema={'z': {'key': '[base_name]', 'initia
lizer': lambda: z()}},
    )
    def f6(x, z):
        return [x, x - z.run(), x - z.run()]
    
    s = Session()
    s
.f4 = f4()
    s.f6 = f6()
    s.f5 = f5()
    s.p6 = s.f4 | s.f6 | s.f5
    
    result = s.p6.run(input_data=10)  # ou
tput: 59

    '''
    output: 
    Step: p6;InputInitializer:sp0
    text = 10 (2 characters)

    Step: p6;f4.0:sp0
   
 text = 12 (2 characters)
    text = 11 (2 characters)

    Step: p6;f6.0:sp0
    text = 12 (2 characters)
    text = 11
 (2 characters)
    text = 10 (2 characters)
    text = 11 (2 characters)
    text = 8 (1 characters)
    text = 7 (1 ch
aracters)

    Step: p6;f5.0:sp0
    text = 59 (2 characters)
    '''

```
---

     
 
all -  [ I was working on this for a long time - a SWE Kit that simplifies SWE Agent Creation ](https://www.reddit.com/r/LangChain/comments/1ege590/i_was_working_on_this_for_a_long_time_a_swe_kit/) , 2024-08-01-0912
```
Hey everyone! I’m excited to share a new project: SWEKit, a powerful framework for building software engineering agents 
using the Composio tooling ecosystem.

**Objectives**

SWEKit allows you to:

* Scaffold agents that work out-of-t
he-box with frameworks like CrewAI and LlamaIndex.
* Add or optimize your agent's abilities.
* Benchmark your agents a
gainst SWE-Bench.

# Implementation Details

* **Tools Used**: Composio, CrewAI, Python

**Setup**:

1. Install 
agentic framework of your choice and the Composio plugin
2. The agent requires a github access token to work with your 
repositories
3. You also need to setup API key for the LLM provider you're planning to use 

**Scaffold and Run Your 
Agent**

**Workspace Environment:**

SWEKit supports different workspace environments:

* **Host**: Run on the hos
t machine.
* **Docker**: Run inside a Docker container.
* **E2B**: Run inside an E2B Sandbox.
* **FlyIO**: Run inside
 a FlyIO machine.

**Running the Benchmark:**

* **SWE-Bench** evaluates the performance of software engineering age
nts using real-world issues from popular Python open-source projects.

[GitHub](https://git.new/SWE)

Feel free to e
xplore the project, give it a star if you find it useful, and let me know your thoughts or suggestions for improvements!
 🌟
```
---

     
 
all -  [ Is anyone aware of a good OCR model that can be used for document processing (Multi-language support ](https://www.reddit.com/r/LangChain/comments/1egcvsy/is_anyone_aware_of_a_good_ocr_model_that_can_be/) , 2024-08-01-0912
```
I need it to process documents for government agency. 
```
---

     
 
all -  [ Not sure which IT job to target ](https://www.reddit.com/r/ITCareerQuestions/comments/1eg9il0/not_sure_which_it_job_to_target/) , 2024-08-01-0912
```
Hi,

I work as an editor and staff writer for a trade magazine targeting STEM professionals. Fell into the job a few yea
rs ago when I was 22; turned out to be really fun and paid decently so I stuck with it.

However, I have an associate de
gree in computer programming and can work in a few different languages (more on that below). I'm also familiar and comfo
rtable in Windows and Linux environments, including CLI for both.

While I love working as a writer, I have also always 
loved IT and computers---and it pays quite a bit more. 

**My question:** Below is a rundown of my experience and skills
 pulled from my resume. Based on what you see, what kind of IT role should I be targeting? Help Desk? Jr. Sysadmin? Some
thing else?

Thanks

**SUMMARY/SKILLS**

Experienced technical communicator with expertise in programming and IT support
 (Windows, Linux). AAS in software development. Capable in Python, C#, SQL, markup languages, and Linux CLI. Regularly w
rite informative content around software, data, AI/ML, cybersecurity, and more. Creative and conscientious with a flair 
for explaining technical topics simply.

**Skills:** Programming (Python, C#, HTML/CSS, Bash, Powershell), Windows, Linu
x, SQL, Selenium, writing documentation, user training, troubleshooting, self-hosting services (Apache, FreshRSS), autom
ation, research

**EXPERIENCE**

**JOB 2**

**Associate Editor / Editorial IT Support**

**4/2022 - Present**

* Develop
ed a custom-trained LLM chatbot using **Python** and the **langchain** library
* Built an RSS reader for internal resear
ch use (**C#**)
* Programmed an application that automates social media promotion by crawling sitemap for new articles a
nd generating snippets with the OpenAI API (**Python, Flask, HTML/CSS**)
* Wrote **PowerShell** script to automate bulk 
image manipulation and storage processes
* Assist other users with computer issues, troubleshooting, etc.
* Write inform
ative content about software, AI/ML, cybersecurity, and more
* Lead production of multiple issues of print magazine, act
ing as project manager for high-visibility projects on strict deadlines

**JOB 1**

**Developer / Technical Content Mana
ger**

**2/2018 – 4/2022**

* Wrote program to generate HTML web pages automatically, saving $6,000+ annually, then depl
oyed across company and trained users (**C#**)
* Wrote data pipeline to export and scrub data from internal inventory pl
atform for use in KPI reporting (**Python, pandas library**), saving significant time daily
* Wrote a variety of web scr
apers to assist in research and CRM data manipulation processes (**Python, Selenium library**)
* Wrote automated two-way
 sync between internal inventory platform and e-commerce website to reconcile inventory differences (**Python**)
* Assis
ted in troubleshooting and maintaining user workstations as well as organization network hardware


```
---

     
 
all -  [ RAG based recommendation system  ](https://www.reddit.com/r/LangChain/comments/1eg9g86/rag_based_recommendation_system/) , 2024-08-01-0912
```
I want to build a chatbot which gives recommendations say books based on the conversation it had before with the user an
d I also want it to have good language skills like fundamental models so what are resource for learning this and what ar
e the techstack to be used for this?
```
---

     
 
all -  [ Confused on What to Use for Chatbot? ](https://www.reddit.com/r/LangChain/comments/1eg41kn/confused_on_what_to_use_for_chatbot/) , 2024-08-01-0912
```
Hello -- I am trying to incrementally create a chatbot that will do three things (depending on user input)

1. Summarize
 a JSON specification for the product (thinking some simple prompt engineering here should be able to do this)
2. Answer
 questions about some ontologies/hierarchies we maintain (thinking RAG)
3. Generate / Modify a JSON specification for th
e product (thinking a fine-tuned model for this specific structured output we use - internally before JSON we use pydant
ic models)

My question is what is the best way to use LangChains building blocks to properly route a user's request to 
the appropriate model within the chat?

I was reading the docs and I wasn't sure if I needed to create a custom agent (a
nd somehow let it decide which of the three to use?) or if I should do a 'dumber' rule-based function to then determine 
which of the three to use and just have that integrate with the basic chatbot.

Any help / guidance would be greatly app
reciated! Am supposed to look into this for work and a little out of my depth right now.
```
---

     
 
all -  [ Discussion: How to dynamically modify tool descriptions in Langgraph? ](https://www.reddit.com/r/LangChain/comments/1eg12qg/discussion_how_to_dynamically_modify_tool/) , 2024-08-01-0912
```
Does anyone know how to dynamically modify the description of a Tool?

I am using ToolNode in Langgraph with tools defin
ed with the decorator, and to define the args, I am using a Pydantic BaseModel, something like:

    class ToolInput(Bas
eModel):
        arg_1: str = Field(description='...', type='string')
        ...
    
    u/tool('get_data', args_schem
a=ToolInput)
    def get_data(
        arg_1: str,
        ...
    ):
        '''Get the data, the accepted values of th
e arg_1 are:
        - val_1, val_2, val_3 ... val_n
        '''
        ...
        return data
    

The point is, I w
ant to dynamically pass data from the graph's state to construct the prompt, something like:

    class ToolInput(BaseMo
del):
        arg_1: int = Field(description='...', type='string')
        ...
    
    @tool('get_data', args_schema=To
olInput)
    def get_data(
        arg_1: str,
        ...
    ):
        '''Get the data, the accepted values of the ar
g_1 are:
        - {val_1}, {val_2}, {val_3}, ... , {val_n}
        '''
        # Where the {val_x} come from the State,
 for example state['available_values']
        ...
        return data
    

Does anyone have an idea of how I can do th
is?
```
---

     
 
all -  [ RAG and AI agents bootcamp by AI planet ](https://www.reddit.com/r/Agentic_AI/comments/1eg0nz9/rag_and_ai_agents_bootcamp_by_ai_planet/) , 2024-08-01-0912
```
I really love studying with AI planet since the community is available to help and tries to make knowledge clear.

# RAG
 and Agents Bootcamp is now live and is FREE

From AI planet 'We are proud to announce that we are releasing RAG and Age
nts Bootcamp. 

* Ever wondered about building a human clone that mimics a real person? Have you ever thought about crea
ting an autonomous AI that mimics human characteristics and has key elements such as a brain, perception, the ability to
 plan, reflect, take action, and possess memory just like any other human? These are known as Autonomous Agents or assis
tants. If you're curious about learning and building them to solve meaningful problems, then you must consider joining t
he bootcamp.
* Imagine another scenario: you have a vast amount of custom data and need an assistant, similar to ChatGPT
, that can provide factually accurate answers based on your specific data source. This integration between large languag
e models, such as GPT, and custom data can be achieved using Retrieval Augmented Generation (RAG).  If you're curious ab
out building your own GPT model for your data, this bootcamp is designed for you.
* This bootcamp will cover the theory 
and implementation of concepts such as Retrieval-Augmented Generation (RAG), prompt engineering, vector databases, auton
omous agents, and much more.  
* We will also discuss no-code tools like the GenAI stack and open-source frameworks such
 as BeyondLLM, Langchain, OpenAGI, LlamaIndex, crewAI, and more.  
* The bootcamp will include real-time projects and li
ve sessions designed to enhance your AI knowledge and skills.

  
 Register: [https://aiplanet.com/bootcamps/rag-agents-
bootcamp](https://mail.dphi.tech/l/qcQkzS3TJnwEp7DalPu8rQ/jNoIl6P6Ci7XpypSQWJ9HQ/RUq4AKbxw4rPiu1q892Bjbnw) '
```
---

     
 
all -  [ Is there a tool for finds optimal pipeline for a RAG? ](https://www.reddit.com/r/LangChain/comments/1efz9nj/is_there_a_tool_for_finds_optimal_pipeline_for_a/) , 2024-08-01-0912
```
Is there a tool out there that can find the optimal pipeline for a RAG for a given data? 

  
Im planning to build one a
nd was wondering how helpful something like this would be?
```
---

     
 
all -  [ AI web app TS vs Python + FastAPI? ](https://www.reddit.com/r/LangChain/comments/1efz85n/ai_web_app_ts_vs_python_fastapi/) , 2024-08-01-0912
```
I come from an AI developer background but i want to build an AI web app myself. 

I have 2 options:  
A. Build every co
mponents ( calling AI models, parsing , injestion ) in TS/NextJS which im not familiar with at all, but if this will hel
p long term im willing to put in the work.

B. Deploy my AI components using FastAPI. Im much more familiar with python,
 but im trying not to overcomplicate the architecture of my first webapp ( need to host frontend and backend separately 
)

  
Has anyone deploy any AI webapps/ SAAS here? Would like to have some suggestions
```
---

     
 
all -  [ AI-Assisted Data Science - Non-Fiction ](https://www.reddit.com/r/wroteabook/comments/1efyynh/aiassisted_data_science_nonfiction/) , 2024-08-01-0912
```
Use ChatGPT to analyze text, images, audio, and tables!

Large language models can unlock valuable insights hidden in yo
ur data. This book teaches you how to leverage Python and language models to perform a variety of data analysis tasks. T
opics covered include:

* Classifying text documents
* Analyzing images and videos
* Transcribing audio files
* Text-to-
SQL query interfaces
* Fine-tuning and cost optimization
* Building apps with LangChain
* Creating agents for data analy
sis

[https://www.manning.com/books/ai-assisted-data-science](https://www.manning.com/books/ai-assisted-data-science)
```
---

     
 
all -  [ Serializing/Deserializing Messages? Am I using packages correctly? (LangGraph) ](https://www.reddit.com/r/LangChain/comments/1efvx6d/serializingdeserializing_messages_am_i_using/) , 2024-08-01-0912
```
**\[SOLVED\]:** Used `_convert_message_to_dict` and stored that dict instead. When loading, convert all dicts with `_con
vert_dict_to_message`.  


**Preface:**

Lest it becomes an XY problem, my initial problem is that I need to count token
 usage, using the provided `model.get_num_tokens_from_messages` from their `langchain_openai`. However, due to the way I
 save and load history, things keep breaking.

**Introduction:**

I am attempting to handle history management (save/loa
d of conversations and messages) myself, since I can't quite understand checkpoints yet, and it is also in current heavy
 development. While LangChain uses their instances of BaseMessage (AIMessage, HumanMessage, etc), I found that doing `me
ssage.to_json().get('kwargs', {})` will return a dict representing the json version that the LLM really sees. I extracte
d a list of these and fed it to an LLM directly, and realized the LLM was still able to understand everything. So saving
 these dicts and loading them/feeding them to the LLM worked just fine.

However, now I need to add token count to the m
ix. I use AzureOpenAIChat which does not support token counts for `astream_events`, so I have to get it using `model.get
_num_tokens_from_messages`. This is where my problems arise.

Here is the process:

**Attempt 1)**

**Error:**

    mess
age does not have attribute 'content'

**Investigation:**

Turns out, `get_num_tokens_from_messages` calls a `_convert_m
essage_to_dict` function. Some of my messages are already dicts, so when this value is passed to the `_format_message_co
ntent` function, it crashes and gives an error.

**Thoughts:** It is weird that their `_convert_message_to_dict` functio
n doesn't attempt to account for the case that some in the list may already be dicts.

**Solution:** No worries. I just 
did an extra step to convert all loaded message dicts back to subclasses of `BaseMessage`, using their `_convert_dict_to
_message` function per message upon load.

**Attempt 2)**

**Error:**

    dict has no property 'role'

**Investigation:
**

That's right. The function expects a property 'role'. Since I stored and loaded the `kwargs` from each BaseMessage, 
they have the property 'type' instead of 'role'.

**Thoughts:** It is weird that while they themselves use 'type' instea
d of 'role', their `_convert_dict_to_message` function only looks for role, and doesn't try to default to 'type'.

**Sol
ution:** No worries, upon saving messages, I just did an extra step to also set the 'role' of the dict to the existing '
type' value, then store it.

**Attempt 3)**

**Error:**

    role 'ai' unknown. expecting 'assistant', 'user', 'tool', '
function', or 'system'

**Investigation:**

Although their json generates additional types, this method only expects the
se few.

**Thoughts:** It is weird that they use 'ai', 'assistant', 'human', 'tool', 'function', 'system', 'chat', etc, 
but limit the expected roles.

**Solution:** No worries, upon saving messages, I will do an extra step to also manually 
convert their types, to align with their expected roles.

**Attempt 4)**

**Error:**

[  none is not an allowed value \(
type=type\_error.none.not\_allowed\)](https://preview.redd.it/jn5o6f5c2ofd1.png?width=1039&format=png&auto=webp&s=5d6830
0fdedf9153ecc336ab594fbb6001e5431e)

>*flips table*

**Investigation:**

The message trace itself is not very helpful fo
r debugging and determining the exact cause, but based on experience (and it mentioning the tool call) I'm assuming that
 it is due to the AIMessage with a tool call. Usually that has no content value (an empty string, which somehow becomes 
a None value internally), but it results in this error.

Deeper investigations show that the to\_json method's kwargs cr
eation omits values that are falsy, which results in its 'content' property not being set or saved for AIMessages with t
ool calls, thus causing the error.

**Thoughts:** It is strange that the BaseMessage's content attribute is of type `Uni
on[str, List[Union[str, Dict]]]`, which gives the error when None is passed, rather than default to an empty string.

**
Solution?** I am still experimenting with this. Either to add an extra step when saving to manually add an empty content
 property to the dict as well, or call `message.json` or `message.dict` rather than `message.to_json`. Then I'll have to
 continue testing to see if it will work.

**Conclusion:**

All of this, just to get the token usage.

Am I going about 
this the wrong way? It seems like I am fighting the package more than undergoing development in this case. Are all my th
oughts valid? Should the langchain\_openai package be updated to support more of the features langgraph provides for bet
ter integration? Or is that already handled in another library and I am using the wrong ones?
```
---

     
 
all -  [ Official Discord? ](https://www.reddit.com/r/LangChain/comments/1efszqi/official_discord/) , 2024-08-01-0912
```
Hi,   
Is there an official discord server for LangChain? Seems like all the links I found are invalid.
```
---

     
 
all -  [ I can't run my simple model ](https://www.reddit.com/r/LangChain/comments/1efsssr/i_cant_run_my_simple_model/) , 2024-08-01-0912
```
This is my code:

    from langchain_google_vertexai import VertexAI
    from langchain.prompts import PromptTemplate
  
  from langchain.chains import LLMChain
    
    
    class GeminiProcessor:
        def __init__(self, model_name, proj
ect):
            self.model=VertexAI(
                model_name=model_name,
                project=project
          
  )
        
    class bookProcessor:
        def __init__(self, topic:str, genai_processor: GeminiProcessor):
         
   self.topic = topic
            self.GeminiProcessor = genai_processor
            self.system_template = '''
        
        Your task is to generate a general description of a book on the topic of {keyword}. 
                '''
       
 
        def generate_ebook(self):
            
            prompt = PromptTemplate.from_template(
               templ
ate=self.system_template,
               )
                    
            # creating chain
            chain = prompt 
| self.GeminiProcessor.model 
            output = chain.invoke(self.topic)
            print('output:', output)
       
     
            return output

I don't really know why this is not working.

I keep getting this weird error: 

  


 
   line 166, in <listcomp>
        'category': rating.category.name,
                    ^^^^^^^^^^^^^^^^^^^^
    Attrib
uteError: 'int' object has no attribute 'name'

Can anyone help with this bug? I'm a beginner at LangChain so any help w
ould be appreciated.
```
---

     
 
all -  [ I built a memory framework for LLMs and Agents ](https://www.reddit.com/r/Python/comments/1efsjgy/i_built_a_memory_framework_for_llms_and_agents/) , 2024-08-01-0912
```
**Why?**

I was building an AI-powered dating app. I couldn't find a memory layer that takes up less RAM, free and easy 
to use. This led to the concept of redcache-ai.

**What My Project Does**

It dynamically retains information across dif
ferent user sessions. This allows the user to improve semantic search and have context.

**Target Audience** 

Anyone bu
ilding applications that leverage Large Language Models. This includes customer support apps, apps that use semantic sea
rch and dating apps.

**Comparison** 

* Easy to setup: it's a python package. Simply use pip install redcache-ai.
* Tak
es up less memory.
* Extensible: You can store your text memory to disk or sqlite. Enhance memory using LLM providers.
*
 Local testing and Cloud hosting: the framework locally and host it on your cloud provider of choice.

**What's worse ab
out Redcahe-ai**.

* Currently, OpenAI is the only supported LLM provider.
* Alpha version. I mostly tested it on Window
s OS.

The software is highly customizable. I've done my best to add comments and make the code readable.

src; [https:/
/github.com/chisasaw/redcache-ai](https://github.com/chisasaw/redcache-ai)

Inspired by Langchain.
```
---

     
 
all -  [ Llama Stack [toolchain + agentic-system] ](https://www.reddit.com/r/LocalLLaMA/comments/1efq2gd/llama_stack_toolchain_agenticsystem/) , 2024-08-01-0912
```
In the new realease of Llama models there was also a mention to '*the Llama Stack API, a standard interface we hope will
 make it easier for third-party projects to leverage Llama models*'. I´ve found both [llama-toolchain](https://github.co
m/meta-llama/llama-toolchain) and [agentic-system](https://github.com/meta-llama/llama-agentic-system), but no documenta
tion referring to the overall ecossystem of Llama Stack or how these tools can be deployed in more robust workflows.

Is
 there a documentation page I might be missing? Or is it too early to expect proper documentation on how to orchestrate 
these tools locally? 

Im wondering if these will replace the common langchain, autogen or llama-index modules we have b
een using.
```
---

     
 
all -  [ ChromaDB Internal Server Error when trying to implement RAG service on a server ](https://www.reddit.com/r/LangChain/comments/1efp23j/chromadb_internal_server_error_when_trying_to/) , 2024-08-01-0912
```
Hi! I'm trying to implement a RAG service for a chatbot that retrieves information from a document based on text queries
. For the most part my code works when implemented in an endpoint, but when executing for a second time i get this: 'Per
missionError: \[WinError 32\] The process cannot access the file because it is being used by another process: 'chroma\\\
\62bff5e8-b534-41dd-8d3b-e767c1d4b598\\\\data\_level0.bin''. I tried closing the file with a method, I tried deleting th
e database everytime before running, deleting the collection, etc. but nothing seems to work. Any suggestions?
```
---

     
 
all -  [ Spring AI vs Langchain4j - which to use as of July 2024 ](https://www.reddit.com/r/java/comments/1efospd/spring_ai_vs_langchain4j_which_to_use_as_of_july/) , 2024-08-01-0912
```
Hi everyone

I'm starting a new Spring Boot project that should consume an LLM.

I was wondering if you can advise on us
ing **Spring AI vs Langchain4j**

  
I've got the impression that Spring AI is pretty new vs langchain(4j) which is like
 the industry 'standard' in a way.

  
Could you let me know what you think? What's the chance of Spring AI dying out...
 ? 

  
If it was a few years a few major releases, I would have just jumped to the Spring as it would be nicely integra
ted.

  
Much appreciated!
```
---

     
 
all -  [ RAG over Database ](https://www.reddit.com/r/LangChain/comments/1efnx5u/rag_over_database/) , 2024-08-01-0912
```
I have been trying to build a RAG over a database that  has mulitple tables. Often times, for a user query, the data has
 to be searched by joining multiple tables. I followed this approach as mentioned in Langchain documents.

[https://pyth
on.langchain.com/v0.1/docs/use\_cases/sql/quickstart/](https://python.langchain.com/v0.1/docs/use_cases/sql/quickstart/)


  
What I am observing is that many times the query generated by LLM is not correct and the data that user wants is in
correct. We have provided almost 60 queries in Fewshot prompts example and send 3 as example that are closes semantic ma
tch. The accuracy still seems far from expected one. Are we missing something. 
```
---

     
 
all -  [ Langchain Agents or Langgraph Agents ](https://www.reddit.com/r/LangChain/comments/1efnpgv/langchain_agents_or_langgraph_agents/) , 2024-08-01-0912
```
I am working on a RAG chatbot application where we will first to have if either the given question is having enough know
ledge to be answered or we need some further information before answering. Or if a question is a general question which 
doesn't even need RAG search. For example, if a question is 'What are the main components of a car?' then we don't need 
RAG search but if a question is 'What type of suspensions do you have for a car?' then we will do RAG search.

  
Till n
ow, I created a simple ReACT agent in langchain to ask the followup questions with a tool and now I need to integrate if
 the given query is something that can be answered without any tool or not and for this, I am thinking about first havin
g an agent which qualifies the given query and if its qualified for RAG search then second agent will do either RAG sear
ch or follow-up questions.

  
In the past of couple of days, I have been exploring langgraph and I feel like simple lan
gchain is enough for my solution like a chain of agents. So please make me understand, why one should use Langgraph?
```
---

     
 
all -  [ Sharing a Code Repository on RAG ](https://www.reddit.com/r/LangChain/comments/1efnkrw/sharing_a_code_repository_on_rag/) , 2024-08-01-0912
```
I've recently created a repository for indexing, generating and evaluating RAG responses. Would love to have some feedba
ck on this. I've used LangChain and LangChain benchmarks too.

[https://github.com/abhinav-kimothi/A-Simple-Guide-to-RAG
](https://github.com/abhinav-kimothi/A-Simple-Guide-to-RAG)
```
---

     
 
all -  [ Passing an error from an ai tool to the user ](https://www.reddit.com/r/LangChain/comments/1efmpc7/passing_an_error_from_an_ai_tool_to_the_user/) , 2024-08-01-0912
```
Hello , as the title says, I have a react agent who uses some tools to find the answers to the user queries! sometimes t
he tools might find an error, for example i am raising an HTTPException if inside the tool some conditions are not corre
ct. How can i pass it to the user and inform him about the error?
```
---

     
 
all -  [ Need honest feedback on my resume, will apply mainly for ML/DS new grad 2025 roles. ](https://www.reddit.com/r/resumes/comments/1efelkj/need_honest_feedback_on_my_resume_will_apply/) , 2024-08-01-0912
```
https://preview.redd.it/e6jwjaoinjfd1.png?width=1372&format=png&auto=webp&s=97b1592056f03287c37e924010f3ddb1f23cc449




International student, applied to nearly 450 companies for ML/DS roles in the summer 2024 cycle, got 1 interview, got re
jected after the final round.

  
Need a review so that the same doesn't happen while applying for full time roles.
```
---

     
 
all -  [ Using HumanInputRun Tool with create_sql_agent in streamlit. ](https://www.reddit.com/r/LangChain/comments/1efbwpt/using_humaninputrun_tool_with_create_sql_agent_in/) , 2024-08-01-0912
```
I'm trying to get human input if the question the user asked needs clarification due to not knowing what table to use et
c. but adding is as extra_tools parameter in create_sql_agent with an input_func like the following: 


    def get_stre
amlit_input() -> str:
        '''
        Get input from a Streamlit chat input.
    
        Returns:
            str: 
The input from the user.
        '''
        try:
            prompt = st.chat_input('Insert your text. Enter 'q' to end
.', key='human_input')
        except EOFError as e:
            st.chat_message('EOFError: ' + str(e))
        return p
rompt


and agent set up as below: 

    agent_executor: Any = create_sql_agent(
        llm=llm,
        verbose=True,

        prompt=few_shot_prompt,
        agent_type='tool-calling',
        max_iterations=15,
        max_execution_time
=180,
        db=db_instance,
        extra_tools=[human_input_tool],  # Add the human input tool here
        agent_exe
cutor_kwargs={
            'return_intermediate_steps': True,
            'handle_parsing_errors': True,
            'me
mory': memory,
        },
    )



it asks the clarification question but the sql agent still continues to run. The clar
ification question shows up in intermediate steps which i can interact with but then after hitting enter on my response,
 it just shows the clarification question. and i have to then retype it again. 

Is there a better way to do this? maybe
 something like 

clarifying llm | agent_executor | output ? 

how would this work in streamlit? 

Any help is greatly a
ppreciated.
```
---

     
 
all -  [ Loading local llm with csv_agent. No open AI ](https://www.reddit.com/r/LangChain/comments/1ef841i/loading_local_llm_with_csv_agent_no_open_ai/) , 2024-08-01-0912
```
I am using llama3 for a chatbot that can answer from CSV files. I've seen implementations with OpenAI, and I want to loa
d local llama3 for the task. If you have any recommendations, please share.
```
---

     
 
all -  [ Chance me and Questions. ](https://www.reddit.com/r/UTAdmissions/comments/1ef7khm/chance_me_and_questions/) , 2024-08-01-0912
```
First, my stats:

Demographics: Asian, Male, HS class of 2025, college class of 2029.

Rank: Top 3% in my class (the ran
k for last semester is coming out in September so idk)

GPA: 4.0 UW, 107 W (1.1x multiplier for honors, 1.2x multiplier 
for APs and advanced honors)

12 APs finished by end of senior year. Planning on getting an AP Capstone Diploma.

1500 S
AT (750 M / 750 R), 35 ACT (35 Reading / 36 Math / 35 Eng / 36 Sci)

ACTIVITIES

* Eagle Scout
* CTM Intern at City of A
ustin Youth Internship Program
* Intern at Lifescale Analytics
* In the Cyber Patriots (our team made it to Platinum Div
ision in State Round) and UIL Computer Science Club since Junior year.
* In JV Robotics Club in sophomore year.
* Worked
 at Mathnasium for sophomore and half of junior year.
* Geo Bee State Qualifier in 2019 and 2020
* Congressional App Cha
llenge Applicant in 2023, made a health-related web app that calculates the risk of cardiovascular disease.
* Volunteere
d at HOTOSM since 2022.
* 100+ hours of volunteering and community service
* Shadowed for one week at a local hospital.


PROJECTS

* Created a website from scratch for my sister's dance school
* Created my own programming language using Typ
escript.
* Created an OpenAI chatbot using Langchain with data from my school notes.

Now for the question: I'm planning
 on submitting an Early Action application. I want to apply for ECE or Neuroscience, but I don't know which one to pick.
 I am knowledgeable in these two subjects and I would be happy and satisfied if I get to pursue either one of them, but,
 as you can probably tell, I like computer science a little more. However, I heard that taking ECE is hard, and looking 
back, I could've done more activities and projects. So here are my questions to y'all:

1. Without seeing my essays, wha
t are the chances that I get accepted into ECE or Neuroscience if I decide to apply for either?
2. Why should I pick one
 over the other?
3. Do I have a shot at getting into Computer Science?
```
---

     
 
all -  [ Pydantic ](https://www.reddit.com/r/LangChain/comments/1ef6qc6/pydantic/) , 2024-08-01-0912
```
Hello everyone ,
I m using pydantic in combination with LM format enforcer to output a certain format ,the thing is that
 I would like the model to be able to output possibly multiple json not just one. The task is about retrieving a variabl
e and naming it.But multiple elements can be retrieved.Is there any ways to do that?

Thanks
```
---

     
 
all -  [ I built a document parser that works without pre-training, unlike google document ai or azure docume ](https://www.reddit.com/r/LangChain/comments/1ef5f7t/i_built_a_document_parser_that_works_without/) , 2024-08-01-0912
```
Hey everyone,

I wanted to share what I built with this community to see what you guys think. I'm curious about any use 
cases you might have or just general feedback.

I created ParDocs with a simple mission: to make document extraction as 
painless as possible. I know firsthand how much time and effort can go into pre-training and labeling, and I wanted to b
uild a tool that lets you focus on what really matters -> building and coding.

With ParDocs, you can:

* Extract data f
rom any document types with minimal setup.
* Customize the JSON format you receive as a response.
* Save loads of time o
n tedious pre-training tasks.

Check out our beta here: [https://www.pardocs.com](https://www.traddocs.com/).

For those
 who prefer not to click on unknown links, here’s our YouTube demo video: https://youtu.be/LdCC0uBQ-QE.

It’s free to us
e during this beta phase. After that, I'm considering pricing it at $0.014 for the splitter and $0.075 for the extractor
. I’d love to hear your feedback on this.

Using ParDocs is very simple:

1. Specify the types of documents you'd like t
o extract.
2. Enter the desired JSON format for the response.
3. Upload your document and receive the data you need!

I’
m personally available to answer any questions or help you get started. You can DM me on Reddit or chat with me on Disco
rd: https://discord.gg/xgEXkh7Rxk. I’d love to hear what you think and how we can make ParDocs even better.

Looking for
ward to your thoughts and feedback!
```
---

     
 
all -  [ How to pass video input for evaluation? ](https://www.reddit.com/r/LangChain/comments/1ef4anh/how_to_pass_video_input_for_evaluation/) , 2024-08-01-0912
```
I am using LangSmith to evaluate my multimodal LLM runs using Gemini 1.5-Flash. My input is a question and a video file.
 I am having trouble getting the evaluator functions such as criteria to take in a custom prompt or even input video. An
y suggestions how to achieve this?
```
---

     
 
all -  [ Reasoning and Info Extraction using Function Calling ](https://www.reddit.com/r/LangChain/comments/1ef21fs/reasoning_and_info_extraction_using_function/) , 2024-08-01-0912
```
Hey everyone,  
  
I am working on an info extraction project where I am using LLM's to extract information from the doc
uments. The length of the documents that I am dealing with a rather short (3-5 pages), so I am not using RAG, but provid
ing the whole document content in-context. For the information extraction, I am using function calling/tool usage as it 
ensures a structured response all the time. And this setup used to work for most cases where the information to extract 
where directly present in the document.  
  
Now I have some scenarios where the information that needs to be extracted 
are not directly present in the document. From the content in the document, LLM have to do some reasoning to extract the
 required information. In this case, I am having some trouble in extracting information using function calling.  
  
Any
one have any experience with similar problems? Any suggestion are highly appreciated.  
```
---

     
 
MachineLearning -  [ [D] Embedding generation in production? How are you doing it? ](https://www.reddit.com/r/MachineLearning/comments/1e7xt6k/d_embedding_generation_in_production_how_are_you/) , 2024-08-01-0912
```


For those building production RAG pipelines, how are you generating embeddings. More than which model, I'm interested 
in how your deploying it. Are you calling the openai/vertex API endpoint directly? Using langchain/llamaindex wrappers? 
Using vectordb  classes? Or some other way?
```
---

     
 
MachineLearning -  [ [D] Is Anyone Else Setting Up Real-Time Django Workers for their AI Application? What's the best way ](https://www.reddit.com/r/MachineLearning/comments/1e0qens/d_is_anyone_else_setting_up_realtime_django/) , 2024-08-01-0912
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

     
 
MachineLearning -  [ [P] Real Time AI Workers Web Application ](https://www.reddit.com/r/MachineLearning/comments/1dzryk9/p_real_time_ai_workers_web_application/) , 2024-08-01-0912
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

     
