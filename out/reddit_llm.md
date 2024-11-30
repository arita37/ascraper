 
all -  [ GPT-4o-Realtime-Preview Azure Support? ](https://www.reddit.com/r/LangChain/comments/1h2vy5y/gpt4orealtimepreview_azure_support/) , 2024-11-30-0913
```
Is there a way to support the only audio model in Azure like the one on OpenAI?

```typescript
import { AzureChatOpenAI 
} from '@langchain/openai';
const llm: any = new AzureChatOpenAI({
    modelName: 'gpt-4o-realtime-preview',
    deploym
entName: config.azureOpenAIApiDeploymentName,
    openAIApiVersion: '2024-10-01',
    azureOpenAIApiInstanceName: config
.azureOpenAIInstanceName,
    maxTokens: config.maxToken,
    temperature: config.temperature,
    audio: {'voice': 'all
oy', 'format': 'wav'},
    modalities: ['text', 'audio'],
});
```

Similar configuration as seen on the direct OpenAI au
dio model: https://www.datacamp.com/tutorial/gpt-4o-audio-preview

But when using gpt-4o-realtime-preview that is the on
ly audio model on Azure. This error rises:
```
Result: Failure Exception: 404 Resource not found Troubleshooting URL: ht
tps://js.langchain.com/docs/troubleshooting/errors/MODEL_NOT_FOUND
```
```
---

     
 
all -  [ Interface for my chatbot ](https://www.reddit.com/r/LangChain/comments/1h2ut1g/interface_for_my_chatbot/) , 2024-11-30-0913
```
Hi all,

I'm a mechanical engineer and I'm developing a chatbot to pitch it to my current company. I've build it using L
angGraph. I know it may be not optimised 100% but I'm happy with the answers that it is giving me. To call the graph all
 I use is :   
  
\# Specify a thread  
config = {'configurable': {'thread\_id': '1'}}  
  
\# Run  
messages = graph.in
voke({'user\_question': 'Question here...'},config)  
messages\['messages'\]\[-1\].pretty\_print()

This will generate a
n AIMessage answer.

Is there a quick way to create an interface for presentation purposes ? Instead of compiling a Jupi
ter Notebook I want to be able to ask questions from an interface.  


Appreciate any help !
```
---

     
 
all -  [ Create Own DataSet form PDF's ](https://www.reddit.com/r/LangChain/comments/1h2sh7h/create_own_dataset_form_pdfs/) , 2024-11-30-0913
```
What is the best way to create the largest number of questions and answers from PDF?  
Another way other than extracting
 questions manually using ChatGPT
```
---

     
 
all -  [ Claude 3.5 Sonnet V2 + LangChain on AWS ](https://www.reddit.com/r/Anthropic/comments/1h2pysr/claude_35_sonnet_v2_langchain_on_aws/) , 2024-11-30-0913
```
Hi,

Has anyone experience with using Claude 3.5 Sonnet V2 (2024-10-22) together with LangChain (Agent with tool functio
ns) on AWS?

We have a system prompt defined as an XML document where we explain that it should use the defined tools wh
en necessary, and we pass in the tools like <tools\_definition>{…JSON schema of tools…}</tools\_definition>.

On us-west
-2 (where the model can be accessed directly through the foundation-model id “anthropic.claude-3-5-sonnet-20241022-v2”),
 the model works correctly. It calls the tools when necessary, and responds in a human language.

On us-east-1 (where th
e model can be accessed only through the inference-profile id “us.anthropic.claude-3-5-sonnet-20241022-v2”), the model’s
 response includes an XML-formatted version of the used tool’s schema, but it doesn’t actually call the tool. I also tri
ed it on us-west-2 with the inference-profile id, and it acts the same.

Is there anything I’m unaware of? Is maybe the 
V2 model accessed through the foundation-model id somewhat different than the one accessed through the inference-model i
d?
```
---

     
 
all -  [ LangChain tools ](https://www.reddit.com/r/modelcontextprotocol/comments/1h2nwyx/langchain_tools/) , 2024-11-30-0913
```
I added support for MCP tools to LangChain toolkit https://github.com/rectalogic/langchain-mcp
```
---

     
 
all -  [ Langchain’s state of AI agents report is mostly bullshit. ](https://www.reddit.com/r/DebunkingAI/comments/1h2mx32/langchains_state_of_ai_agents_report_is_mostly/) , 2024-11-30-0913
```
I took time to read Langchain’s state of AI agents report, so you don’t have to. Don’t worry, you are not missing anythi
ng. It’s mostly a marketing pamphlet masqueraded as a rigorous study.

I knew it was bullshit from the get-go as soon as
 I read their definition of AI agents.  
[https://medium.com/thoughts-on-machine-learning/langchains-state-of-ai-agents-
report-is-mostly-bullshit-c689d0021a19](https://medium.com/thoughts-on-machine-learning/langchains-state-of-ai-agents-re
port-is-mostly-bullshit-c689d0021a19)
```
---

     
 
all -  [ [For Hire] React, NEXT, Nest, Express, Langchain and Full Stack Developer. ](https://www.reddit.com/r/forhire/comments/1h2ijf3/for_hire_react_next_nest_express_langchain_and/) , 2024-11-30-0913
```
Hi Reddit! 👋  
I'm Sheryar, a Full Stack Developer skilled in **React, Next.js, NestJS, Node.js, AWS**, and **LangChain*
*. I specialize in:

✅ **Frontend**: Responsive, pixel-perfect UIs with React/Angular  
✅ **Backend**: Scalable APIs & m
icroservices (Node.js, NestJS)  
✅ **Databases**: Advanced PostgreSQL with JSON handling  
✅ **Payments**: Stripe integr
ation for secure transactions  
✅ **Cloud**: AWS deployments  
✅ **Chatbots & Voicebots**: Development with LangChain fo
r intelligent automation

**Recent Work**:  
🚗 Ride-sharing app with Stripe payments & live tracking  
📦 Urban logistics
 platform with multi-stop deliveries  
📊 Custom CRM with Twilio API integration  
🤖 Chatbot & Voicebot solutions for aut
omation and customer support

💰 **Rate**: $15–$20/hour (negotiable)  
📧 DM me to discuss your project or view my portfol
io!  
**GitHub**: [storm1033](https://github.com/storm1033)

Let’s build something amazing together! 🚀
```
---

     
 
all -  [ Pause a Langraph at an Intermediate Node and Retrieve the Current State Result ](https://www.reddit.com/r/LangChain/comments/1h2g2n9/pause_a_langraph_at_an_intermediate_node_and/) , 2024-11-30-0913
```
I have implemented a customer engagement system with a complex workflow, including tasks like scheduling calls, placing 
orders, and replying to emails. On the client side, we have three APIs: `/domain/place_order/`, `/domain/schedule_call/`
, etc.

The requirement is to execute a workflow corresponding to a specific use case, such as a subgraph for placing an
 order. During execution, the intermediate state should be stored, and the current state result should be returned.

If 
the API is triggered again with knowledge of the previous state, the system should resume from where it left off and com
plete the corresponding subgraph workflow (e.g., the call scheduling subgraph).

How can this be achieved?
```
---

     
 
all -  [ What's the pros and cons compared langchain tools vs MCP (Model Context Protocol) ](https://www.reddit.com/r/LangChain/comments/1h2csxn/whats_the_pros_and_cons_compared_langchain_tools/) , 2024-11-30-0913
```
I just had a chance to use MCP, made by claude. Seems like it's very similar to langchain tools, but don't know the main
 difference. What's it about, and how can it be different from langchain tools?
```
---

     
 
all -  [ Looking for any literature on Multi Agent architecture/design patterns w/ langgraph ](https://www.reddit.com/r/LangChain/comments/1h26cxx/looking_for_any_literature_on_multi_agent/) , 2024-11-30-0913
```

```
---

     
 
all -  [ Relevance of Message Queues in AI Agents ](https://www.reddit.com/r/LangChain/comments/1h25wdn/relevance_of_message_queues_in_ai_agents/) , 2024-11-30-0913
```
Hi everyone,

I’ve been working with message queue (MQ) software and middleware tools. I’ve been wondering how an AI mig
ht intersect with or enhance the realm of message queuing systems.



Are there applications I’m missing or any existing
 work connecting AI and message queuing systems?

How might the intersection of these two fields shape the future of mid
dleware and distributed systems?

Looking forward to hearing your insights and discussing this further!
```
---

     
 
all -  [ Anyone else interested in storing outputs as well as prompts? And if so ... what solutions are out t ](https://www.reddit.com/r/PromptEngineering/comments/1h22jdi/anyone_else_interested_in_storing_outputs_as_well/) , 2024-11-30-0913
```
Hi everyone,

I think it's my first time posting on this sub which is weird as I've been working on prompting stuff for 
quite some time now. So nice to discover that this exists!

I became very interested in LLMs and prompt engineering earl
ier this year. As the self-hosting kind of type, as much as I was instantly impressed by the advances in the GPT models 
since I last checked them out, my thoughts were also drawn to *'great ... but if I can get something useful out of this 
(the LLM) where does that data \*go\*?'* I've played around with building my own prototypes for running and then storing
 prompts. But ultimately, I'd much rather used better more polished tech that somebody else has made. I'm just having a 
hard time finding it!

To be a bit more specific:

I've worked on a prompt for discovering and parsing some corporate su
stainability data. After quite a number of iterations, it works nicely. I like the idea of using something like a prompt
 engineering IDE to iterate on the prompt further, but I also want to collect the outputs as they're being generated! I 
can do this (say) by creating a script that uses LangChain and routing the outputs to a folder within a Github repo. But
 I'd like something that's a bit easier to replicate, hands-off and (ideally also) cloud-based.

My ideal tool: great en
vironment for prompt engineering *and* really solid functionality for managing where the outputs get stored. Ideally: ch
oose your backend (say a MongoDB server) and the tool will route the outputs there (with or without the prompts). Or as 
a second best, here are some good features for sifting through them and pulling them out. Either way: give me some optio
ns for what to do with the stuff that gets generated beyond just batching it up into one huge JSON that's not really all
 that scalable.

Beyond just collecting the information your prompt was designed to generate, other useful things you ca
n do with previous outputs include passing them as context for other LLMs (ie, chained prompting across models).

As muc
h as some of the prompt eng tools are delightful, I feel like there's something of a gaping blind spot in terms of what 
to do with the information generated by our diligent work in crafting prompts. Which seems a little self-defeating and s
trange.

Does something exist that does what I'm after? And how are people approaching managing outputs in general?
```
---

     
 
all -  [ Discussion: 'Why Does the Recursion Limit Exist in LangGraph?' ](https://www.reddit.com/r/LangChain/comments/1h226yc/discussion_why_does_the_recursion_limit_exist_in/) , 2024-11-30-0913
```
Currently, in my team, we are developing agents using LangGraph. Some of these are complex agents that we dynamically co
mpile, with some cases involving N branches.

My question is: Why does the recursion limit exist? Is it primarily a perf
ormance-based limitation, or is it more about preventing issues like infinite loops in agent execution, such as in the c
ase of a ReAct agent
```
---

     
 
all -  [ Faster LLM response ](https://www.reddit.com/r/LangChain/comments/1h222g7/faster_llm_response/) , 2024-11-30-0913
```
Hello everyone

In my RAG agent, I'm making 3 requests to the LLM, the first is for determining whether to call the tool
 or not, the second is to check set a boolean in the response (JSON), the third is to provide a final answer.

In each i
nvocation to the agent, 2 network requests are made. The prompts are a little bit long, tried to make them shorter but g
ot the same response time about 13 seconds.

using gpt-40-mini, tried gpt 3.5 turbo as well.

all prompts return the fol
lowing JSON:

    {
       'message': '<Your natural language response to the user - exclude technical IDs>',
       'co
ntact_id': '<contact_id of the contractor or null>',  # Always use the actual contractor ID from metadata
       'id': <
id from metadata>,
       'should_navigate': <false>
    }
```
---

     
 
all -  [ MCP Server Tools Langgraph Integration example ](https://www.reddit.com/r/LangChain/comments/1h20lxe/mcp_server_tools_langgraph_integration_example/) , 2024-11-30-0913
```
Example of how to auto discover tools on an MCP Server and make them available to call in your Langgraph graph.

[https:
//github.com/paulrobello/mcp\_langgraph\_tools](https://github.com/paulrobello/mcp_langgraph_tools)
```
---

     
 
all -  [ WARNING:langsmith.client:Failed to multipart ingest runs ](https://www.reddit.com/r/LangChain/comments/1h1yu32/warninglangsmithclientfailed_to_multipart_ingest/) , 2024-11-30-0913
```
Hi guys, 

  
just testing LangChain, once I want to set up tracking of the project in LangSmith I got the following err
or: 

    WARNING:langsmith.client:Failed to multipart ingest runs: langsmith.utils.LangSmithAuthError: Authentication f
ailed for WARNING:langsmith.client:Failed to multipart ingest runs: langsmith.utils.LangSmithAuthError: Authentication f
ailed for . HTTPError('401 Client Error: Unauthorized for url: ', '{'detail':'Invalid token'}')trace=b91f591b-3a81-4d7d-
b45b-aa712a577433,id=0b099474-e808-412d-8ed6-e778a05597e0; trace=b91f591b-3a81-4d7d-b45b-aa712a577433,id=9adae83d-b1e1-4
628-9e8d-6ceccef2ed40; trace=b91f591b-3a81-4d7d-b45b-aa712a577433,id=ac3358b4-ea21-4a87-9757-88669e094a09; trace=b91f591
b-3a81-4d7d-b45b-aa712a577433,id=b91f591b-3a81-4d7d-b45b-aa712a577433; trace=b91f591b-3a81-4d7d-b45b-aa712a577433,id=926
e7252-0018-415a-b1d5-f39830f202fd; trace=b91f591b-3a81-4d7d-b45b-aa712a577433,id=32733c7b-cc61-4dce-b6bf-f91c7025e98d
  
  . HTTPError('401 Client Error: Unauthorized for url: ', '{'detail':'Invalid token'}')trace=b91f591b-3a81-4d7d-b45b-aa7
12a577433,id=0b099474-e808-412d-8ed6-e778a05597e0; trace=b91f591b-3a81-4d7d-b45b-aa712a577433,id=9adae83d-b1e1-4628-9e8d
-6ceccef2ed40; trace=b91f591b-3a81-4d7d-b45b-aa712a577433,id=ac3358b4-ea21-4a87-9757-88669e094a09; trace=b91f591b-3a81-4
d7d-b45b-aa712a577433,id=b91f591b-3a81-4d7d-b45b-aa712a577433; trace=b91f591b-3a81-4d7d-b45b-aa712a577433,id=926e7252-00
18-415a-b1d5-f39830f202fd; trace=b91f591b-3a81-4d7d-b45b-aa712a577433,id=32733c7b-cc61-4dce-b6bf-f91c7025e98d
    https:
//api.smith.langchain.com/runs/multiparthttps://api.smith.langchain.com/runs/multiparthttps://api.smith.langchain.com/ru
ns/multiparthttps://api.smith.langchain.com/runs/multipart

Any idea how to get it working? 

Thanks for any help

Here 
is the script: 

    # Adding Document Loader
    from langchain.chains.combine_documents import create_stuff_documents_
chain
    from langchain_community.document_loaders import WebBaseLoader
    from langchain_text_splitters import Recurs
iveCharacterTextSplitter
    from langchain_openai import AzureOpenAIEmbeddings
    from langchain_community.vectorstore
s.faiss import FAISS
    from langchain.chains import create_retrieval_chain
    from langchain.callbacks import tracing
_v2_enabled
    
    with tracing_v2_enabled() as session:
        assert session
        
        
        def get_docu
ment_from_web(url):
          loader = WebBaseLoader(url)
          docs = loader.load()
          splitter = RecursiveC
haracterTextSplitter(
              chunk_size=200,
              chunk_overlap=20
          )
          splitDocs = spl
itter.split_documents(docs)
          print(len(splitDocs))
          return splitDocs
    
        def create_db(docs):
 
          embedding = AzureOpenAIEmbeddings(
            model='text-embedding-3-small',
            azure_endpoint='x
xxx',
            api_key = 'xxx',
            openai_api_version = '2024-10-01-preview'
        )
          vector_stor
e = FAISS.from_documents(docs, embedding=embedding)
          return vector_store
    
    
        def create_chain(vec
tore_store):
    
          prompt = ChatPromptTemplate.from_template('''
    
          Answer the user question:
     
     Context: {context}
          Question: {input}
          ''')
    
          #chain = prompt | model_2
    
       
   chain = create_stuff_documents_chain(llm= model_2,
                                              prompt = prompt)
   
       
          retrieve = vectore_store.as_retriever(search_kwargs = {'k':12})
          retrieve_chain = create_retr
ieval_chain(
              retrieve,
              chain
            )
    
    
    
          return retrieve_chain
  
  
        docs = get_document_from_web('https://www.abz.com/en/articles/top-10')
        vector_store = create_db(docs)

        chain = create_chain(vector_store)
        response = chain.invoke({
            'input' : 'What....',
        
        })
    
        print(response['answer'])
    
    
    
```
---

     
 
all -  [ Using an In-Memory Graph Database for GraphRAG in GenAI Apps ](https://www.reddit.com/r/learnmachinelearning/comments/1h1yt2j/using_an_inmemory_graph_database_for_graphrag_in/) , 2024-11-30-0913
```
Hey everyone! I’ve noticed many posts here about handling niche datasets for building intelligent systems, like GenAI ap
ps. Whether it’s legal docs, medical datasets, or proprietary codebases, the challenge is always the same: how do you en
able meaningful knowledge discovery without overloading your LLM or spending a fortune on fine-tuning?

I work at Memgra
ph (full disclosure), and we’ve been digging into Retrieval-Augmented Generation (RAG) systems for months. RAG pairs LLM
s with a knowledge graph to retrieve relevant context dynamically, so the model processes only what matters. It’s faster
, scalable, and adapts to real-time data changes.

For example:

* **Cedars-Sinai** uses Memgraph for risk prediction in
 healthcare.
* **Precina Health** leverages GraphRAG to revolutionize diabetes care.

Memgraph integrates with tools lik
e LangChain and LlamaIndex and even offers features like vector search, deep-path traversals, and streaming data ingesti
on. It’s in-memory, so it’s incredibly fast.

Curious to hear how others are integrating their data with GenAI apps. Wha
t’s your approach to combining LLMs with structured and unstructured data? More details on Memgraph’s GraphRAG ecosystem
 [here](https://memgraph.com/docs/ai-ecosystem/graph-rag).
```
---

     
 
all -  [ A FREE goldmine of tutorials about GenAI Agents! ](https://github.com/NirDiamant/GenAI_Agents) , 2024-11-30-0913
```
After the hackathon I ran in conjunction with LangChain, people have expanded the GenAI_Agents GitHub repository that I 
maintain to now contain 43 (!) Agents-related code tutorials.

It covers ideas across the entire spectrum, containing we
ll-documented code written step by step.
Most of the tutorials include a short 3-minute video explanation!

The content 
is organized into the following categories:
1. Beginner-Friendly Agents
2. Educational and Research Agents
3. Business a
nd Professional Agents
4. Creative and Content Generation Agents
5. Analysis and Information Processing Agents
6. News a
nd Information Agents
7. Shopping and Product Analysis Agents
8. Task Management and Productivity Agents
9. Quality Assu
rance and Testing Agents
10. Special Advanced Techniques

📰 And that's not all! Starting next week, I'm going to write f
ull blog posts covering them in my newsletter.

The subscription and all contents are FREE

→ Subscribe here: https://di
amantai.substack.com/
```
---

     
 
all -  [ Googlegenerativeai is causing problem with async python flask workers like gevent ](https://www.reddit.com/r/LangChain/comments/1h1wop9/googlegenerativeai_is_causing_problem_with_async/) , 2024-11-30-0913
```
The web app crashes whenever I use gevent class workers with gunicorn when running my docker image which is an API for m
y web app developed usinf flask and utilizes googlegenerativeai from langchain
```
---

     
 
all -  [ Improving embedding speed.  ](https://www.reddit.com/r/LangChain/comments/1h1u1bz/improving_embedding_speed/) , 2024-11-30-0913
```
How long does it take you often to embed a text file. ? i am using.

    text-embedding-3-large plus langchain openai an
d pinecone. using semantic chunking  with gradiant method
    
    and it is taking me long time.
    
    since i am us
ing next.js serverless for deployment it is taking me more than thn 60 sec so i don't know what to do. 
```
---

     
 
all -  [ Advice: Am I doing something wrong? ](https://www.reddit.com/r/leetcode/comments/1h1u1bb/advice_am_i_doing_something_wrong/) , 2024-11-30-0913
```
Or is the market expected to improve? Applying to DE, DS, MLE, DA roles with this; no hits after 150 total. Internationa
l so sponsorship required.

https://preview.redd.it/w0qbmiu4pm3e1.png?width=1322&format=png&auto=webp&s=7c2817479728d0a3
3cb34262443467df1adda6e2


```
---

     
 
all -  [ (Resume review) Roast my Resume, 2024 grad. Need some career advice ](https://i.redd.it/p8n3npe2nm3e1.jpeg) , 2024-11-30-0913
```
Feel free to roast this resume, template and everything. 

So I'm currently a Junior DevOps Engineer at an SBC (Jenkins,
 CI/CD, K8s).
I want to switch to a traditional Software engineer role (backend preferably). 
Need some advice, tips on 
what to focus on. I've been practicing Golang and Python for a while now, should I stick to that or shift my focus elsew
here? 
Is there any scope for freshers in Go? 
```
---

     
 
all -  [ Effective solution to host RAG app ](https://www.reddit.com/r/Rag/comments/1h1sn3m/effective_solution_to_host_rag_app/) , 2024-11-30-0913
```
I have created a simple rag chat for my company. I used llama 3.1 8b model. There are less than 70 users. I am not sure 
on how to deploy it in cloud.

Tech stack : olllama , langchain,fastapi, faiss and a simple react webpage to chat .

Whi
ch is the cost effective solution?

Getting any GPU server or using bedrock ?

If GPU machine, what should be the memory
 size should I get ?
```
---

     
 
all -  [ Conversational RAG on local files (on-premises usage) ](https://www.reddit.com/r/Python/comments/1h1qzds/conversational_rag_on_local_files_onpremises_usage/) , 2024-11-30-0913
```
Hey everyone,

**What My Project Does:**  
That is a local conversational rag on your files. Be honest, you can use this
 as a rag on-premises, cause it is build with docker, langchain, ollama, fastapi, hf All models download automatically, 
soon I'll add an ability to choose a model For now solution contains:

* Locally running Ollama (currently qwen-0.5b mod
el hardcoded, soon you'll be able to choose a model from ollama registry)
* Local indexing (using sentence-transformer e
mbedding model, you can switch to other model, but only sentence-transformers applied, also will be changed soon)
* Qdra
nt container running on your machine
* Reranker running locally (BAAI/bge-reranker-base currently hardcoded, but i will 
also add an ability to choose a reranker)
* Websocket based chat with saving history
* Simple chat UI written with React

* As a plus, you can use local rag with ChatGPT as a custom GPT, so you able to query your local data through official 
chatgpt web and mac os/ios app.
* You can deploy it as a RAG on-premises, all containers can work on CPU machines

Coupl
e of ideas/problems:

* Model Context Protocol support
* Right now there is no incremental indexing or reindexing
* No s
election for the models (will be added soon)
* Different environment support (cuda, mps, custom npu's)

**Target Audienc
e:**  
This project is designed for developers, as you’ll need to set up Docker to get it running. Unfortunately, there’
s no consumer-friendly app yet.

**Comparison**:  
The closest competitor, though already far ahead (so I doubt I can tr
uly compete with them), is **LLM Studio**.

For anyone interested in making local RAG or on-premises RAG as accessible a
s possible, you’re warmly invited to contribute!

Here is a link: [https://github.com/dmayboroda/minima](https://github.
com/dmayboroda/minima)

Thank you so much!
```
---

     
 
all -  [ An example of local conversational RAG using Langchain ](https://www.reddit.com/r/LangChain/comments/1h1q0cg/an_example_of_local_conversational_rag_using/) , 2024-11-30-0913
```
Hey everyone, I would like to introduce you my latest repo, that is a local conversational rag on your files, Be honest,
 you can use this as a rag on-premises, cause it is build with docker, langchain, ollama, fastapi, hf All models downloa
d automatically, soon I'll add an ability to choose a model For now solution contains:

* Locally running Ollama (curren
tly qwen-0.5b model hardcoded, soon you'll be able to choose a model from ollama registry)
* Local indexing (using sente
nce-transformer embedding model, you can switch to other model, but only sentence-transformers applied, also will be cha
nged soon)
* Qdrant container running on your machine
* Reranker running locally (BAAI/bge-reranker-base currently hardc
oded, but i will also add an ability to choose a reranker)
* Websocket based chat with saving history
* Simple chat UI w
ritten with React
* As a plus, you can use local rag with ChatGPT as a custom GPT, so you able to query your local data 
through official chatgpt web and mac os/ios app.
* You can deploy it as a RAG on-premises, all containers can work on CP
U machines

Couple of ideas/problems:

* Model Context Protocol support
* Right now there is no incremental indexing or 
reindexing
* No selection for the models (will be added soon)
* Different environment support (cuda, mps, custom npu's)


Here is a link: [https://github.com/dmayboroda/minima](https://github.com/dmayboroda/minima)

Welcome to contribute (wa
tch, fork, star)  
Thank you so much!
```
---

     
 
all -  [ [P] Minima: local conversational retrieval augmented generation project (Ollama, Langchain, FastAPI, ](https://www.reddit.com/r/MachineLearning/comments/1h1pudq/p_minima_local_conversational_retrieval_augmented/) , 2024-11-30-0913
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

     
 
all -  [ Query decomposition workflow in langgraph  ](https://www.reddit.com/r/LangChain/comments/1h1prti/query_decomposition_workflow_in_langgraph/) , 2024-11-30-0913
```
I'm trying to create a langgraph workflow where in the first step I want to decompose my complex query into multiple sub
 queries and go through the next workflow of retrieving relevant chunks and extracting the answer bit I want to run for 
all my sub queries in parallel without creating same workflow multiple times


Help for any architecture suggestion or a
ny langgraph features to implement for ease 
```
---

     
 
all -  [ Complete newbie here - Can anyone give me an overview for what I'm doing? ](https://www.reddit.com/r/LangChain/comments/1h1pik1/complete_newbie_here_can_anyone_give_me_an/) , 2024-11-30-0913
```
I have been working on prompt design and trying to work ChatGPT into having reasoning like Tree-of-Thought , Socratic Qu
estioning , etc... I have a bunch of research pdfs on prompting also.   For the latter, I was trying to convert like 50 
pdfs to txts and batch upload , though Astra DB had like 10 pdfs per database - not sure how I'd get it done here , and 
how to get to run like metaprompt frameworks for each reasoning process as a enhancement layer to ChatGPT

I'm barely ru
nning my first script. Trying to figure out how this thing works , I think the goal is a Generative Feedback Loop with R
AG with like a cognitive architecture for enhanced reasoning
```
---

     
 
all -  [ LangGraph Without API Calls ](https://www.reddit.com/r/learnmachinelearning/comments/1h1ld8j/langgraph_without_api_calls/) , 2024-11-30-0913
```
Good evening,

  
I am trying to learn to create Multi-Agent projects using LangGraph based off the [LangGraph Quickstar
t](https://langchain-ai.github.io/langgraph/tutorials/introduction/). I am wondering how could I go about using an API-f
ree system with LangGraph. I tried using Hugging Face models, and was able to successfully use the invoke command. Howev
er, when I get to calling the model as part of the chatbot (after setting the start, chatbot, and end nodes), I get the 
generic AttributeError: 'str' object has no attribute 'content'.

  
I am wondering if this is due to the model I am cho
osing. I can provide specific code if necessary. Also I am very open to doing it another way if necessary. Much apprecia
ted!


```
---

     
 
all -  [ LangGraph without API calls ](https://www.reddit.com/r/LangChain/comments/1h1laq9/langgraph_without_api_calls/) , 2024-11-30-0913
```
Good evening,

  
I am trying to learn to create Multi-Agent projects using LangGraph based off the [LangGraph Quickstar
t](https://langchain-ai.github.io/langgraph/tutorials/introduction/). I am wondering how could I go about using an API-f
ree system with LangGraph. I tried using Hugging Face models, and was able to successfully use the invoke command. Howev
er, when I get to calling the model as part of the chatbot (after setting the start, chatbot, and end nodes), I get the 
generic 

AttributeError: 'str' object has no attribute 'content'

  
I am wondering if this is due to the model I am ch
oosing. I can provide specific code if necessary. Also I am very open to doing it another way if necessary. Much appreci
ated!


```
---

     
 
all -  [ agent-to-agent resiliency, observability, etc - what would you like to see? ](https://www.reddit.com/r/LangChain/comments/1h1hk7i/agenttoagent_resiliency_observability_etc_what/) , 2024-11-30-0913
```
Full disclosure, actively contributing to [https://github.com/katanemo/archgw](https://github.com/katanemo/archgw) \- an
 intelligent proxy for agents built on Envoy and redesigned for agents. Actively seeking feedback on what the community 
would like to see when it comes to agent-to-agent communication, resiliency, observability, etc. Given that a lot of peo
ple are building  task-specific agents and that  agents must communicate with each other reliably, we were seeking advic
e on what features would you like from an agent-mesh that could solve a lot of the crufty resiliency, observability chal
lenges between agents. Note: the project invests in small LLMs to handle/process certain critical tasks related to promp
ts (routing, safety, etc) so if the answer is machine learning related that's totally okay.

You can add your thoughts b
elow, or here: [https://github.com/katanemo/archgw/discussions/317](https://github.com/katanemo/archgw/discussions/317).
 I’ll merge duplicates so feel free to comment away
```
---

     
 
all -  [ How to Make Parallel Requests for the Same Text Using Different Variables ](https://www.reddit.com/r/LangChain/comments/1h1h2vn/how_to_make_parallel_requests_for_the_same_text/) , 2024-11-30-0913
```
I’m a beginner with LangChain, and I’m working on a project that requires making parallel requests to process the same i
nput text across multiple categories. Here’s the challenge: each category needs a different set of examples to guide the
 output generation.

Here’s what I’m trying to achieve:

1. I have a single input text that needs to be processed.
2. Fo
r each category (e.g., 'medications,' 'family history,' 'exams'), I have a unique prompt and a specific set of examples.

3. I want to execute these requests in parallel to improve efficiency.
4. I’m using RunnableParallel, but I’m strugglin
g to figure out the best way to handle the examples dynamically for each category.

What I’ve tried so far:

* Passing e
xamples dynamically during the request.
   * Formatting prompts by embedding examples beforehand. However, I either enco
unter issues with missing inputs variables.

I’m new to LangChain, so any help or suggestions (even simple ones!) would 
be highly appreciated.

    chains = {}
    inputs = {}
    for category, content in prompts.get('medical_queries', {}).
items():
        try:
            prompt_content = content['prompt']
            prompt_examples = content['examples']
 
   
            prompt_template = ChatPromptTemplate.from_template(prompt_content)
    
            chains[category] = L
LMChain(prompt=prompt_template, llm=llm)
    
            inputs[category] = {'input': text, 'example': content['example
s']}
        except Exception as e:
            print(f'{category}: {e}')
    
    pipeline = RunnableParallel(chains)
 
   
    responses = pipeline.invoke(inputs)
    
```
---

     
 
all -  [ Multi-agent supervisor langgrpah giving error ](https://www.reddit.com/r/GoogleColab/comments/1h1ba4c/multiagent_supervisor_langgrpah_giving_error/) , 2024-11-30-0913
```
I was making a supervised agent using langgraph with two agents (rag and sql) using the template from langchain below

O
fficial Doc one : [https://colab.research.google.com/drive/1KEe9YSTGDQopMuss3CSMHJ3VjDzzrGSh?usp=sharing](https://colab.
research.google.com/drive/1KEe9YSTGDQopMuss3CSMHJ3VjDzzrGSh?usp=sharing)

My code: [https://colab.research.google.com/dr
ive/1QszbxpiFJkhWWYhBpSmDCX\_3MMMeHVdd?usp=sharing](https://colab.research.google.com/drive/1QszbxpiFJkhWWYhBpSmDCX_3MMM
eHVdd?usp=sharing)

however when i run my code above at the end i get the error below which seems routeresponse should g
enerate in json and it doesnt. Any idea how i can fix this will be very much appreciated:

>OutputParserException: Funct
ion RouteResponse arguments:

>{  
next: 'Rag\_agent'  
}

>are not valid JSON. Received JSONDecodeError Expecting prope
rty name enclosed in double quotes: line 2 column 5 (char 6)
```
---

     
 
all -  [ Noob on chunks/message threads/chains - best way forward when analyzing bank account statement trans ](https://www.reddit.com/r/LangChain/comments/1h1aiy7/noob_on_chunksmessage_threadschains_best_way/) , 2024-11-30-0913
```
## CONTEXT:
I'm a noob building an app that takes in bank account statement PDFs and extracts the peak balance from each
 of them. I'm receiving these statements in multiple formats, different countries, languages. My app won't know their fo
rmats beforehand.

## HOW I AM TRYING TO BUILD IT:
Currently, I'm trying to build it by extracting markdown from the PDF
 with Docling and sending the markdown to OpenAI api, and asking for it to find the peak balance and for the list of tra
nsactions (so that my app has a way to verify whether it got peak balance right.)

Feeding all of the markdown and reque
sting the api to send bank a list of all transactions isn't working. The model is 'lazy' and won't return all of the tra
nsactions, no matter my prompt (for reference this is a 20 page PDF with 200+ transactions).

So I am thinking that the 
next best way to do this would be with chunks. Docling offers hierarchy-aware chunking [0] which I think it's useful so 
as not to mess with transaction data. But then what should I, a noob, learn about to better proceed on building this app
 based on chunks?

## WAYS FORWARD?
(1) So how should I work with chunks? It seems that looping over chunks and sending 
them through the API and asking for transactions back to append to an array could do the job. But I've got two more thin
gs in mind.

(2) I've hard of chains (like in langchain) which could keep the context from the previous messages and it 
might also be easier to work with?

(3) I have noticed that openai works with a messages *array*. Perhaps that's what I 
should be interacting with via my API calls (to send a thread of messages) instead of doing what I proposed in (1)? Or p
erhaps what I'm describing here is exactly what chaining (2) does?


[0] https://ds4sd.github.io/docling/usage/#convert-
from-binary-pdf-streams at the bottom
```
---

     
 
all -  [ Open Canvas provides chatgpt canvas style ui to use claude and llama3, stores style rules and user i ](https://www.reddit.com/r/LocalLLaMA/comments/1h1a1b9/open_canvas_provides_chatgpt_canvas_style_ui_to/) , 2024-11-30-0913
```
https://preview.redd.it/xg5bqv9odh3e1.png?width=3328&format=png&auto=webp&s=77d6b1e1926a06340e8a21194c73e6f29ac48331

[h
ttps://github.com/langchain-ai/open-canvas](https://github.com/langchain-ai/open-canvas)  

```
---

     
 
all -  [ Tips for improving the processing time of Langgraph Agents ](https://www.reddit.com/r/LangChain/comments/1h18b0d/tips_for_improving_the_processing_time_of/) , 2024-11-30-0913
```
Hello!! I was tasked to improve the performance and speed of our multi agent llm using langgraph and langchain

Any tips
 on how to improve the processing time?
```
---

     
 
all -  [ Text summarization using LangChain's Map-Reduce method. ](https://www.reddit.com/r/LangChain/comments/1h177es/text_summarization_using_langchains_mapreduce/) , 2024-11-30-0913
```
Hello, 

I've been experimenting with LangChain's Map-Reduce approach to summarize texts of approximately 2000 words eac
h. I am satisfied with the results, but the summarization process takes around 15-20 mins. I was looking for any ideas o
r methods to try and reduce the execution time. I'm using ollama's llama3.1:8b model.

Thanks in advance!
```
---

     
 
all -  [ My business model for a small OSS. From OSS project to SaaS (funding)  ](https://www.reddit.com/r/SaaS/comments/1h14361/my_business_model_for_a_small_oss_from_oss/) , 2024-11-30-0913
```
This is a response/follow-up (??) to a great post done yesterday about [monetization of OSS  ](https://www.reddit.com/r/
SaaS/comments/1h0ha1s/i_am_making_700_monthly_with_my_opensource/)

Now i'm going describe how i'm scaling, and do full-
time work in my project, until it becomes a startup/B2B SaaS.

**Project:** [ExtractThinker](https://github.com/enoch371
2/ExtractThinker)

Its **Document Intelligence for LLMs**, or **Langchain for document intelligence**. So more of a nich
e use case, more oriented to extraction of data (No RAG). The project will be used as ***'proof-of-skill'*** for the res
t of the business, for a complex *agentic* B2B model to eventually be also a SaaS. 

**Question:** People are asking me 
'how do you scale this???'

Flow: [Image flow ](https://imgur.com/a/EYWGoP5)

**Github project:** Well presented with do
cumentation. As example driven as possible. 

**Medium:** Over 1.5k followers, contains articles that mention the projec
t or not (depending on the publisher). They attract clients and people interested in the problem solved. **This gives co
ntractor work that feeds the project with use cases.**

**Documentation:** Medium feeds the documentation, so i 'kill tw
o birds with one stone'**.** From diagrams to in detail explanation.

  
**Plan:** Go over 500+ stars and get 2 other to
p founders (2 tech guys and 1 non-tech sales, still missing), that will eventually use this to get funding, next year, v
ia incubator/accelerator or VC seed right away.

  
I hope this helps! A few 1/2 months back i thought this project woul
d not scale (personally), but doing something on top of this, **could definitely work** (Clients eventually put some sen
se into me). Im just a technical guy, sometimes is difficult to see a business model in something like this. 

  
Thank 
you for your time. 
```
---

     
 
all -  [ Langgraph, user_input node with File Upload ](https://www.reddit.com/r/LangChain/comments/1h13hd3/langgraph_user_input_node_with_file_upload/) , 2024-11-30-0913
```
Hello!

I am trying to figure out how to use Langgraph nodes when there is a non-textual input. I am guiding a user in u
ploading files. Let's say, I have the following structure:

`builder.add_node('ask_email', email_node)`  
`builder.add_n
ode('upload_file', upload_file_node)`

I have two questions:

1. How do I manage the file upload - the UI (openWebUI) ca
n show a drop-in component that will trigger external API and this API will respond 200 OK -> is the upload a tool call?
 
2. How do we pass the information about the upload through the state?

  
I'd appreciate a direction, just can't figur
e out how to go about it.
```
---

     
 
all -  [ KeyError: 'input' in create_retrieval_chain()? ](https://www.reddit.com/r/LangChain/comments/1h0ytlt/keyerror_input_in_create_retrieval_chain/) , 2024-11-30-0913
```
I new to generative ai and langchain, bellow i am sharing code and error. I am trying to create a small application. I a
m using python==3.10.0



***CODE:***

    prompt = ChatPromptTemplate([
        ('system', 'You are an expert generativ
e ai developer, answer question from given context {context}'),
        ('user', '{question}')
    ])

    document_chai
n=create_stuff_documents_chain(llm=llm,prompt=prompt1,output_parser=output_parser)
    document_chain
    

    retrieve
r=new_db.as_retriever()
    from langchain.chains import create_retrieval_chain
    retrieval_chain=create_retrieval_cha
in(retriever,combine_docs_chain=document_chain)
    

    ## Get the response form the LLM
    response=retrieval_chain.
invoke({'question':'tell me what is generative ai, and what are Examples of Generative AI tools?'})
    response['answer
']

  
*ERROR I AM GETTING:*

    ---------------------------------------------------------------------------
    KeyErr
or                                  Traceback (most recent call last)
    Cell In[60], line 2
          1 ## Get the res
ponse form the LLM
    ----> 2 response=retrieval_chain.invoke({'question':'tell me what is generative ai, and what are 
Examples of Generative AI tols?'})
          3 # response = retrieval_chain.invoke({'input': {'question': 'tell me what 
is generative AI, and what are examples of Generative AI tools?'}})
          4 response['answer']
    
    File u:\GENE
RATIVE_AI\venv\lib\site-packages\langchain_core\runnables\base.py:5354, in RunnableBindingBase.invoke(self, input, confi
g, **kwargs)
       5348 def invoke(
       5349     self,
       5350     input: Input,
       5351     config: Optiona
l[RunnableConfig] = None,
       5352     **kwargs: Optional[Any],
       5353 ) -> Output:
    -> 5354     return self.
bound.invoke(
       5355         input,
       5356         self._merge_configs(config),
       5357         **{**self.
kwargs, **kwargs},
       5358     )
    
    File u:\GENERATIVE_AI\venv\lib\site-packages\langchain_core\runnables\base
.py:3022, in RunnableSequence.invoke(self, input, config, **kwargs)
       3020 context.run(_set_config_context, config)

       3021 if i == 0:
    -> 3022     input = context.run(step.invoke, input, config, **kwargs)
       3023 else:
    
   3024     input = context.run(step.invoke, input, config)
    
    File u:\GENERATIVE_AI\venv\lib\site-packages\langch
ain_core\runnables\passthrough.py:494, in RunnableAssign.invoke(self, input, config, **kwargs)
        488 def invoke(
 
       489     self,
        490     input: dict[str, Any],
        491     config: Optional[RunnableConfig] = None,
   
     492     **kwargs: Any,
        493 ) -> dict[str, Any]:
    --> 494     return self._call_with_config(self._invoke,
 input, config, **kwargs)
    
    File u:\GENERATIVE_AI\venv\lib\site-packages\langchain_core\runnables\base.py:1927, i
n Runnable._call_with_config(self, func, input, config, run_type, serialized, **kwargs)
       1923     context = copy_c
ontext()
       1924     context.run(_set_config_context, child_config)
       1925     output = cast(
       1926      
   Output,
    -> 1927         context.run(
       1928             call_func_with_variable_args,  # type: ignore[arg-ty
pe]
       1929             func,  # type: ignore[arg-type]
    . . .
         66     ).assign(answer=combine_docs_chain
)
         67 ).with_config(run_name='retrieval_chain')
         69 return retrieval_chain
    
    KeyError: 'input'Out
put is truncated. View as a scrollable element or open in a text editor. Adjust cell output settings...



Thanks in adv
ance, I hope to hear from you soon.  

```
---

     
 
all -  [ Is there a way to chainge chains setup without changing codes in python ](https://www.reddit.com/r/LangChain/comments/1h0v562/is_there_a_way_to_chainge_chains_setup_without/) , 2024-11-30-0913
```
Hello group,
I am working on an interesting problem to setup chains by providing a yaml file as input ( it could be a di
ctionary,  a string or list of touple).

Ask:
Using lang chains to create a function which could be able to create serie
s and parallel chains as per our yaml without changing the python code for each case scenario.

Already done: i am able 
to write a function which will create chains for each attribute individually. 

The issue: i am facing challenge in comb
ining these chains. The depth and length could be changed using the yaml file.

The code should be able to set up chains
 (series or parallel as per the yaml) without making any changes to it the python code.

Idea: i am not 100 percent sure
 but it will involve recursion 
```
---

     
 
all -  [ Prompt engineering for LLM applications ? ](https://www.reddit.com/r/LangChain/comments/1h0taz4/prompt_engineering_for_llm_applications/) , 2024-11-30-0913
```
how does prompt engineering help develop better LLM powered apps like I understand that if you are able to prompt the mo
del a certain you will get a better response but the avg user is not going to be aware of those techniques and in which 
is prompt engineering just for the more advanced user and not like an aid towards better LLM development?
```
---

     
 
all -  [ Optimize your LangChain program with Cognify! ](https://www.reddit.com/r/LangChain/comments/1h0jjbh/optimize_your_langchain_program_with_cognify/) , 2024-11-30-0913
```
Hi everyone! I'm Reyna, a PhD student working on systems for machine learning.

I want to share an exciting open-source 
project my team has built: [Cognify](https://github.com/GenseeAI/cognify). Cognify is a multi-faceted optimization tool 
that automatically enhances generation quality and reduces execution costs for generative AI workflows written in LangCh
ain, DSPy, and Python. Cognify helps you evaluate and refine your workflows at any stage of development. Use it to test 
and enhance workflows you’ve finished building or to analyze your current workflow’s potential.

Key highlights:

* Work
flow generation quality improvement by up to 48%
* Workflow execution cost reduction by up to 9x
* Multiple optimized wo
rkflow versions with quality-cost combinations for you to choose
* Automatic model selection, prompt enhancing, and work
flow structure optimization

Get Cognify at [https://github.com/GenseeAI/cognify](https://github.com/GenseeAI/cognify) a
nd read more at https://mlsys.wuklab.io/posts/cognify/. Would love to hear your feedback and get your contributions!
```
---

     
 
all -  [ RAG - how to ensure a date fields in metadata is used to get latest data? ](https://www.reddit.com/r/LangChain/comments/1h0ih0x/rag_how_to_ensure_a_date_fields_in_metadata_is/) , 2024-11-30-0913
```
I've created a RAG app that aims to be a personal assistant for everything related to my kids' school. I get a ton of em
ails from school with updates, notices, invites, and a lot more. Some info is recurring, such as the weekly wraps that e
xplain what was taught during that week; some of it is a one-off like an invite to an event.

Ultimately, I plan to have
 this either connected to Whatsapp or actually creating reminders/calendar invites for me, but for now, I'm validating i
ts results. But I've hit a wall when it comes to the freshness of data.

**Question**

When building this RAG app, I wou
ld like it to be mindful of dates as it retrieves relevant docs. For example, I get a Weekly Wrap email every week, on F
ridays. Besides wanting the retriever to find the right context (i.e. weekly wrap emails), I would also like for it to s
ort by date and focus on the latest one. What's the best way to achieve this?

**Further Context**

Here is what the app
 does:

* bulk-reads all past emails using the Gmail API, and keeps the date, sender, subject, body and attachments
* pr
ocesses each email to properly convert the body and relevant attachments to text (converts PDFs, DOCXs, and html body in
to text)
* stores the documents in MongoDB (using `MongoDBStore` from `langchain_community.storage)` , using a Document 
format (the entire body + attachment text under `page_content`, and everything else in `metadata`
* stores a summary of 
each document, also in MongoDB, in order to use Multi-Representation indexing
* maps IDs across both stores

I'm using G
PT-4o as the LLM behind the scenes.

I then build a retriever and a chain like this, and invoke the query. Since the res
ponse doesn't take the dates into account, I don't get the latest info properly...

    mongo_conn_str = 'mongodb://loca
lhost:27017/'
    mongodb_client = MongoClient(
        mongo_conn_str,
        uuidRepresentation='standard'
    )
    

    database = mongodb_client['parent-assistant']
    summary_collection = database['summaries']
    
    docs_store = 
MongoDBStore(
        mongo_conn_str,
        db_name='parent-assistant',
        collection_name='emails'
    )
    emb
eddings = OpenAIEmbeddings()
    
    summary_vector_store = Chroma(
        collection_name='summaries',
        embedd
ing_function=OpenAIEmbeddings()
    )
    
    summaries = list(summary_collection.find())
    
    summary_docs = [
   
     Document(
            page_content=s['summary'],
            metadata={'_id': s['_id']}
        )
        for i, s 
in enumerate(summaries)
    ]
    
    retriever = MultiVectorRetriever(
        docstore=docs_store,
        vectorstor
e=summary_vector_store,
        id_key='_id',
        search_kwargs={'k': 1}
    )
    retriever.vectorstore.add_documen
ts(summary_docs)
    
    template = '''Answer the following question based on this context:
    
    {context}
    
   
 Question: {question}
    '''
    
    llm = ChatOpenAI(model='gpt-4o', temperature=0.1)
    
    def format_docs(docs):

        return '\n\n'.join(doc.page_content for doc in docs)
    
    rag_chain = (
        {'context': retriever | for
mat_docs, 'question': RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )
    
    r
ag_chain.invoke('What did John Doe learn last week?')
```
---

     
 
MachineLearning -  [ [P] Open-source declarative framework to build LLM applications - looking for contributors ](https://www.reddit.com/r/MachineLearning/comments/1gkpazh/p_opensource_declarative_framework_to_build_llm/) , 2024-11-30-0913
```
I've been building LLM-based applications, and was super frustated with all major frameworks - langchain, autogen, crewA
I, etc. They also seem to introduce a pile of unnecessary abstractions. It becomes super hard to understand what's going
 behind the curtains even for very simple stuff.

[So I just published this open-source framework GenSphere.](https://gi
thub.com/octopus2023-inc/gensphere) The idea is have something like **Docker for LLMs**. You build applications with YAM
L files, that define an execution graph. Nodes can be either LLM API calls, regular function executions or other graphs 
themselves. Because you can nest graphs easily, building complex applications is not an issue, but at the same time you 
don't lose control.

You basically code in YAML, stating what are the tasks that need to be done and how they connect. O
ther than that, you only write individual python functions to be called during the execution. No new classes and abstrac
tions to learn.

Its all open-source. **Now I'm looking for contributors** to adapt the framework for cycles and conditi
onal nodes - which would allow full-fledged agentic system building! Pls reach out  if you want to contribute, there are
 tons of things to do!

PS: [you can read the detailed docs here,](https://gensphere.readthedocs.io/en/latest/) And go o
ver this quick [Google Colab tutorial.](https://github.com/octopus2023-inc/gensphere/blob/main/examples/gensphere_tutori
al.ipynb)
```
---

     
