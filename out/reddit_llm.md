 
all -  [ Is there any free embeddings model API? ](https://www.reddit.com/r/LangChain/comments/1h3irug/is_there_any_free_embeddings_model_api/) , 2024-12-01-0916
```
I am searching for an free embeddings model with API, not self hosted ones. I am building a personal project on Android 
application that does RAG. Now the catch is, Android studio doesn't support pytorch version >1.4. Though there are free 
versions that have very limited tokens, that isn't enough for me.
```
---

     
 
all -  [ Frontend for solopreneur project ](https://www.reddit.com/r/LangChain/comments/1h3i3u6/frontend_for_solopreneur_project/) , 2024-12-01-0916
```
Hi there :)   
I'm running a quick Agents-RAG prototype with n8n (on top of langchain) and Streamlit on GC for the front
 end.

Now I'm taking a look at some Streamlit alternatives. I was taking a look at openWebUI but I have no time to lear
n that stack. So I'm wondering if I should consider G Mesop or even Django.

I'm out of cognitive energy to learn much m
ore and would love to keep it simple. SO my questions are:  
\- Do you think it makes sense to move from Streamlit to Me
sop?   
\- What about the learning curve for Django?  
\- For simple GUI customizations (navigation, popups, etc), Does 
it make any sens to work on openwebui?

Don't even know if any of my questions makes any sense.... just need some input-
feedback-guidance
```
---

     
 
all -  [ Why is using a small model considered ineffective? I want to build a system that answers users' ques ](https://www.reddit.com/r/LangChain/comments/1h3esmm/why_is_using_a_small_model_considered_ineffective/) , 2024-12-01-0916
```
Why didn’t I train a small model on this data (questions and answers) and then using RAG to improve the accuracy of answ
ering the questions?

The advantages of a small model are that I can guarantee the confidentiality of the information, w
ithout sending it to an American company. It's fast and doesn’t require high infrastructure.

Why does a model with 67 m
illion parameters end up taking more than 20 MB when uploaded to Hugging Face?

However, most people criticize small mod
els. Some studies and trends from large companies are focused on creating small models specialized in specific tasks (ag
ent models), and some research papers suggest that this is the future!
```
---

     
 
all -  [ Output format adjustments  ](https://www.reddit.com/gallery/1h3c23c) , 2024-12-01-0916
```
I’m currently working on an app that helps visualise problem breakdowns in mind maps. As you can see I have problem gett
ing the text from the agents back in a way that’s nice to visualise, anyone got tricks ?
```
---

     
 
all -  [ Choosing an AI model for My knowledge management app  ](https://www.reddit.com/r/LangChain/comments/1h3b0kt/choosing_an_ai_model_for_my_knowledge_management/) , 2024-12-01-0916
```
Hi , I'm working on My internship project  that's a knowledge Management  system using fastapi  and I have to make a cha
tbot that generate answers based on the documents inverted in the database I used langchian and an open source model to 
generate the embeddings using  the vector extension in postgreSQL, the problem still in generating the answers from thes
es embeddeds I want a performing  free AI model and in the same time I can't install it locally . what you suggest ??? 
```
---

     
 
all -  [ (Resume review) Roast my Resume, 2024 grad. Career advice needed.  ](https://i.redd.it/67pjrd0jwz3e1.jpeg) , 2024-12-01-0916
```
Current role: Junior DevOps Engineer (started recently) 
Target role: Backend Developer

Basically I feel underpaid and 
undervalued in current job and want to switch. 

```
---

     
 
all -  [ [For Hire] React, NEXT, Nest, Express, Langchain and Full Stack Developer. ](https://www.reddit.com/r/forhire/comments/1h358rt/for_hire_react_next_nest_express_langchain_and/) , 2024-12-01-0916
```
Hi Reddit! 👋  
I'm Sheryar, a Full Stack Developer skilled in **React, Next.js, NestJS, Node.js, AWS**, and **LangChain*
*. I specialize in:

✅ **Frontend**: Responsive, pixel-perfect UIs with React/Angular  
✅ **Backend**: Scalable APIs & m
icroservices (Node.js, NestJS)  
✅ **Databases**: Advanced PostgreSQL with JSON handling  
✅ **Payments**: Stripe integr
ation for secure transactions  
✅ **Cloud**: AWS deployments  
✅ **Chatbots & Voicebots**: Development with LangChain fo
r intelligent automation

**Recent Work**:  
🚗 Ride-sharing app with Stripe payments & live tracking  
📦 Urban logistics
 platform with multi-stop deliveries  
📊 Custom CRM with Twilio API integration  
🤖 Chatbot & Voicebot solutions for aut
omation and customer support

💰 **Rat**e: $15–$20/hour (negotiable)  
📧 DM me to discuss your project or view my portfol
io!  
**GitHub**: [storm1033](https://github.com/storm1033)

Let’s build something amazing together! 🚀
```
---

     
 
all -  [ How To Pre Process Documents? ](https://www.reddit.com/r/ArtificialInteligence/comments/1h34byp/how_to_pre_process_documents/) , 2024-12-01-0916
```
Still fumbling my way through the 'how to' for creating an enterprise AI app. I'm finding that multiple apps are needed 
for best case scenarios. Right now I have:

0. ??? - Pre process documents
1. Pinecone
2. Cleanlab (optional)
3. An LLM 
(nvm which one)

While I understand you can upload PDFs and chunk them, with varying results, it clearly makes more sens
e to pre process/chunk the documents in some form if you can then upload those. If so who is doing that?

Is this LangCh
ain or a competitor?

Edit: I should mention referring to text data like legal filings. So a 1000 pg list of different l
aws for instance, not numerical data.
```
---

     
 
all -  [ Delete checkpoint from redis in Langgraph? ](https://www.reddit.com/r/LangChain/comments/1h32oqn/delete_checkpoint_from_redis_in_langgraph/) , 2024-12-01-0916
```
Hiii!
Does anyone know how to delete a checkpoint (the whole conversation of a thread id) in redis?

Thanks in advance:)

```
---

     
 
all -  [ GPT-4o-Realtime-Preview Azure Support? ](https://www.reddit.com/r/LangChain/comments/1h2vy5y/gpt4orealtimepreview_azure_support/) , 2024-12-01-0916
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

     
 
all -  [ Interface for my chatbot ](https://www.reddit.com/r/LangChain/comments/1h2ut1g/interface_for_my_chatbot/) , 2024-12-01-0916
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

     
 
all -  [ Create Own DataSet form PDF's ](https://www.reddit.com/r/LangChain/comments/1h2sh7h/create_own_dataset_form_pdfs/) , 2024-12-01-0916
```
What is the best way to create the largest number of questions and answers from PDF?  
Another way other than extracting
 questions manually using ChatGPT
```
---

     
 
all -  [ Claude 3.5 Sonnet V2 + LangChain on AWS ](https://www.reddit.com/r/Anthropic/comments/1h2pysr/claude_35_sonnet_v2_langchain_on_aws/) , 2024-12-01-0916
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

     
 
all -  [ LangChain tools ](https://www.reddit.com/r/modelcontextprotocol/comments/1h2nwyx/langchain_tools/) , 2024-12-01-0916
```
I added support for MCP tools to LangChain toolkit https://github.com/rectalogic/langchain-mcp
```
---

     
 
all -  [ Langchain’s state of AI agents report is mostly bullshit. ](https://www.reddit.com/r/DebunkingAI/comments/1h2mx32/langchains_state_of_ai_agents_report_is_mostly/) , 2024-12-01-0916
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

     
 
all -  [ [For Hire] React, NEXT, Nest, Express, Langchain and Full Stack Developer. ](https://www.reddit.com/r/forhire/comments/1h2ijf3/for_hire_react_next_nest_express_langchain_and/) , 2024-12-01-0916
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

     
 
all -  [ Pause a Langraph at an Intermediate Node and Retrieve the Current State Result ](https://www.reddit.com/r/LangChain/comments/1h2g2n9/pause_a_langraph_at_an_intermediate_node_and/) , 2024-12-01-0916
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

     
 
all -  [ What's the pros and cons compared langchain tools vs MCP (Model Context Protocol) ](https://www.reddit.com/r/LangChain/comments/1h2csxn/whats_the_pros_and_cons_compared_langchain_tools/) , 2024-12-01-0916
```
I just had a chance to use MCP, made by claude. Seems like it's very similar to langchain tools, but don't know the main
 difference. What's it about, and how can it be different from langchain tools?
```
---

     
 
all -  [ Looking for any literature on Multi Agent architecture/design patterns w/ langgraph ](https://www.reddit.com/r/LangChain/comments/1h26cxx/looking_for_any_literature_on_multi_agent/) , 2024-12-01-0916
```

```
---

     
 
all -  [ Relevance of Message Queues in AI Agents ](https://www.reddit.com/r/LangChain/comments/1h25wdn/relevance_of_message_queues_in_ai_agents/) , 2024-12-01-0916
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

     
 
all -  [ Anyone else interested in storing outputs as well as prompts? And if so ... what solutions are out t ](https://www.reddit.com/r/PromptEngineering/comments/1h22jdi/anyone_else_interested_in_storing_outputs_as_well/) , 2024-12-01-0916
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

     
 
all -  [ Discussion: 'Why Does the Recursion Limit Exist in LangGraph?' ](https://www.reddit.com/r/LangChain/comments/1h226yc/discussion_why_does_the_recursion_limit_exist_in/) , 2024-12-01-0916
```
Currently, in my team, we are developing agents using LangGraph. Some of these are complex agents that we dynamically co
mpile, with some cases involving N branches.

My question is: Why does the recursion limit exist? Is it primarily a perf
ormance-based limitation, or is it more about preventing issues like infinite loops in agent execution, such as in the c
ase of a ReAct agent
```
---

     
 
all -  [ Faster LLM response ](https://www.reddit.com/r/LangChain/comments/1h222g7/faster_llm_response/) , 2024-12-01-0916
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

     
 
all -  [ MCP Server Tools Langgraph Integration example ](https://www.reddit.com/r/LangChain/comments/1h20lxe/mcp_server_tools_langgraph_integration_example/) , 2024-12-01-0916
```
Example of how to auto discover tools on an MCP Server and make them available to call in your Langgraph graph.

[https:
//github.com/paulrobello/mcp\_langgraph\_tools](https://github.com/paulrobello/mcp_langgraph_tools)
```
---

     
 
all -  [ WARNING:langsmith.client:Failed to multipart ingest runs ](https://www.reddit.com/r/LangChain/comments/1h1yu32/warninglangsmithclientfailed_to_multipart_ingest/) , 2024-12-01-0916
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

     
 
all -  [ Using an In-Memory Graph Database for GraphRAG in GenAI Apps ](https://www.reddit.com/r/learnmachinelearning/comments/1h1yt2j/using_an_inmemory_graph_database_for_graphrag_in/) , 2024-12-01-0916
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

     
 
all -  [ A FREE goldmine of tutorials about GenAI Agents! ](https://github.com/NirDiamant/GenAI_Agents) , 2024-12-01-0916
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

     
 
all -  [ Googlegenerativeai is causing problem with async python flask workers like gevent ](https://www.reddit.com/r/LangChain/comments/1h1wop9/googlegenerativeai_is_causing_problem_with_async/) , 2024-12-01-0916
```
The web app crashes whenever I use gevent class workers with gunicorn when running my docker image which is an API for m
y web app developed usinf flask and utilizes googlegenerativeai from langchain
```
---

     
 
all -  [ Improving embedding speed.  ](https://www.reddit.com/r/LangChain/comments/1h1u1bz/improving_embedding_speed/) , 2024-12-01-0916
```
How long does it take you often to embed a text file. ? i am using.

    text-embedding-3-large plus langchain openai an
d pinecone. using semantic chunking  with gradiant method
    
    and it is taking me long time.
    
    since i am us
ing next.js serverless for deployment it is taking me more than thn 60 sec so i don't know what to do. 
```
---

     
 
all -  [ Advice: Am I doing something wrong? ](https://www.reddit.com/r/leetcode/comments/1h1u1bb/advice_am_i_doing_something_wrong/) , 2024-12-01-0916
```
Or is the market expected to improve? Applying to DE, DS, MLE, DA roles with this; no hits after 150 total. Internationa
l so sponsorship required.

https://preview.redd.it/w0qbmiu4pm3e1.png?width=1322&format=png&auto=webp&s=7c2817479728d0a3
3cb34262443467df1adda6e2


```
---

     
 
all -  [ Effective solution to host RAG app ](https://www.reddit.com/r/Rag/comments/1h1sn3m/effective_solution_to_host_rag_app/) , 2024-12-01-0916
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

     
 
all -  [ Conversational RAG on local files (on-premises usage) ](https://www.reddit.com/r/Python/comments/1h1qzds/conversational_rag_on_local_files_onpremises_usage/) , 2024-12-01-0916
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

     
 
all -  [ An example of local conversational RAG using Langchain ](https://www.reddit.com/r/LangChain/comments/1h1q0cg/an_example_of_local_conversational_rag_using/) , 2024-12-01-0916
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

     
 
all -  [ [P] Minima: local conversational retrieval augmented generation project (Ollama, Langchain, FastAPI, ](https://www.reddit.com/r/MachineLearning/comments/1h1pudq/p_minima_local_conversational_retrieval_augmented/) , 2024-12-01-0916
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

     
 
all -  [ Query decomposition workflow in langgraph  ](https://www.reddit.com/r/LangChain/comments/1h1prti/query_decomposition_workflow_in_langgraph/) , 2024-12-01-0916
```
I'm trying to create a langgraph workflow where in the first step I want to decompose my complex query into multiple sub
 queries and go through the next workflow of retrieving relevant chunks and extracting the answer bit I want to run for 
all my sub queries in parallel without creating same workflow multiple times


Help for any architecture suggestion or a
ny langgraph features to implement for ease 
```
---

     
 
all -  [ Complete newbie here - Can anyone give me an overview for what I'm doing? ](https://www.reddit.com/r/LangChain/comments/1h1pik1/complete_newbie_here_can_anyone_give_me_an/) , 2024-12-01-0916
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

     
 
all -  [ LangGraph Without API Calls ](https://www.reddit.com/r/learnmachinelearning/comments/1h1ld8j/langgraph_without_api_calls/) , 2024-12-01-0916
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

     
 
all -  [ LangGraph without API calls ](https://www.reddit.com/r/LangChain/comments/1h1laq9/langgraph_without_api_calls/) , 2024-12-01-0916
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

     
 
all -  [ agent-to-agent resiliency, observability, etc - what would you like to see? ](https://www.reddit.com/r/LangChain/comments/1h1hk7i/agenttoagent_resiliency_observability_etc_what/) , 2024-12-01-0916
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

     
 
all -  [ How to Make Parallel Requests for the Same Text Using Different Variables ](https://www.reddit.com/r/LangChain/comments/1h1h2vn/how_to_make_parallel_requests_for_the_same_text/) , 2024-12-01-0916
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

     
 
all -  [ Multi-agent supervisor langgrpah giving error ](https://www.reddit.com/r/GoogleColab/comments/1h1ba4c/multiagent_supervisor_langgrpah_giving_error/) , 2024-12-01-0916
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

     
 
all -  [ Noob on chunks/message threads/chains - best way forward when analyzing bank account statement trans ](https://www.reddit.com/r/LangChain/comments/1h1aiy7/noob_on_chunksmessage_threadschains_best_way/) , 2024-12-01-0916
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

     
 
all -  [ Open Canvas provides chatgpt canvas style ui to use claude and llama3, stores style rules and user i ](https://www.reddit.com/r/LocalLLaMA/comments/1h1a1b9/open_canvas_provides_chatgpt_canvas_style_ui_to/) , 2024-12-01-0916
```
https://preview.redd.it/xg5bqv9odh3e1.png?width=3328&format=png&auto=webp&s=77d6b1e1926a06340e8a21194c73e6f29ac48331

[h
ttps://github.com/langchain-ai/open-canvas](https://github.com/langchain-ai/open-canvas)  

```
---

     
 
all -  [ Tips for improving the processing time of Langgraph Agents ](https://www.reddit.com/r/LangChain/comments/1h18b0d/tips_for_improving_the_processing_time_of/) , 2024-12-01-0916
```
Hello!! I was tasked to improve the performance and speed of our multi agent llm using langgraph and langchain

Any tips
 on how to improve the processing time?
```
---

     
 
MachineLearning -  [ [P] Open-source declarative framework to build LLM applications - looking for contributors ](https://www.reddit.com/r/MachineLearning/comments/1gkpazh/p_opensource_declarative_framework_to_build_llm/) , 2024-12-01-0916
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

     
