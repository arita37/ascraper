 
all -  [ LangChainJS - Tool calling with JSON schemas ](https://www.reddit.com/r/LangChain/comments/1hiw84b/langchainjs_tool_calling_with_json_schemas/) , 2024-12-21-0912
```
New to LangchainJS, and looking for confirmation that I'm staring at a bug.

I'm trying to take a bunch of tools defined
 in JSON schema and convert them into `DynamicStructuredTool`.  I'm partially successful, in that I'm getting the tools 
to be called from the LLM, but the payloads are input.

I think the reason why is that I'm seeing the `DynamicStructured
Tool` constructor code just throw away the payload schema if the schema is *not* a JSON schema passed in.  

    this.sc
hema = (
    isZodSchema(fields.schema) ? fields.schema : z.object({}).passthrough()

[https://github.com/langchain-ai/l
angchainjs/blob/main/langchain-core/src/tools/index.ts#L460-L461](https://github.com/langchain-ai/langchainjs/blob/main/
langchain-core/src/tools/index.ts#L460-L461)

  
Is there something I'm missing?
```
---

     
 
all -  [ Lessons learned from building a context-sensitive AI assistant with RAG ](https://www.reddit.com/r/LangChain/comments/1hirwgr/lessons_learned_from_building_a_contextsensitive/) , 2024-12-21-0912
```
I recently built an AI assistant for Vectorize (where I'm CTO) and wanted to share some key technical insights about bui
lding RAG applications that might be useful to others working on similar projects. Some interesting learnings from the p
rocess: 

1. Context improves retrieval quality significantly - By embedding our assistant directly in the UI and using 
page context in our retrieval queries, we got much better results than just using raw user questions. 
2. Real-time, mul
ti-source data creates a self-improving system - We combined docs, Discord discussions, and Intercom chats. When we tag 
new support answers, they automatically get processed into our vector index. The system improves through normal daily ac
tivities. 
3. Reranking models > pure similarity search - Vector similarity scores alone weren't enough to filter out ir
relevant results (e.g., getting S3 docs when asking about Elasticsearch). Using a reranking model with a relevance thres
hold of 0.5 dramatically improved response quality. 
4. Anti-hallucination prompting is crucial - Even with good retriev
al, clear LLM instructions matter. We found emphasizing 'only use retrieved content' and adding topic context in prompts
 helped prevent hallucination, even with smaller models. The full post goes into implementation details, code examples, 
and more technical insights: 

[https://vectorize.io/creating-a-context-sensitive-ai-assistant-lessons-from-building-a-r
ag-application/](https://vectorize.io/creating-a-context-sensitive-ai-assistant-lessons-from-building-a-rag-application/
)

Happy to discuss technical details or answer questions about the implementation!
```
---

     
 
all -  [ Error  when i stream my graph  ](https://www.reddit.com/r/LangChain/comments/1hinulz/error_when_i_stream_my_graph/) , 2024-12-21-0912
```
    am using gemnai  as llm 

    ValueError: no signature found for builtin type <class 'dict'>ValueError: no signature
 found for builtin type <class 'dict'>



my code 

    from typing import Literal, List, Union
    from typing_extensio
ns import TypedDict
    from langchain_anthropic import ChatAnthropic
    from langchain_core.messages import HumanMessa
ge
    from langgraph.graph import StateGraph, START, END, MessagesState
    from langgraph.prebuilt import create_react
_agent
    from langgraph.types import Command
    from langchain_google_genai import ChatGoogleGenerativeAI
    from la
ngchain_anthropic import ChatAnthropic
    
    
    
    
    # Create the LLM
    llm = ChatGoogleGenerativeAI(
      
  model='gemini-1.5-pro',
        temperature=0,
        api_key='xcxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
    )
    # Def
ine team members and create literal type
    members = ['backlog_planner', 'sprint_planner']
    options = members + ['F
INISH']
    NextType = Literal['backlog_planner', 'sprint_planner', 'FINISH']
    
    # System prompt for supervisor
  
  system_prompt = (
        'You are a supervisor tasked with managing a conversation between the'
        f' following 
workers: {members}. Given the following user request,'
        ' respond with the worker to act next. Each worker will p
erform a'
        ' task and respond with their results and status. When finished,'
        ' respond with FINISH.'
    
)
    
    # Define router type with explicit literals
    class Router(TypedDict):
        '''Worker to route to next. 
If no workers needed, route to FINISH.'''
        next: NextType
    
    # Create supervisor node with explicit return 
type
    def supervisor_node(state: MessagesState) -> Command[Union[Literal['backlog_planner', 'sprint_planner'], Litera
l['__end__']]]:
        messages = [
            {'role': 'system', 'content': system_prompt},
        ] + state['messag
es']
        response = llm.with_structured_output(Router).invoke(messages)
        goto = response['next']
        if g
oto == 'FINISH':
            goto = END
        return Command(goto=goto)
    
    # Rest of your code remains the same

    backlog_agent = create_react_agent(
        llm, 
        tools=[get_info_for_backlog],
        state_modifier='''
 
       You are a Business analyst, your job is to detail the product backlog that includes:
        Epics: High-level re
quirements outlining significant chunks of functionality.
        User Stories: Smaller, actionable requirements that de
tail what needs to be achieved.
        Acceptance Criteria: Conditions that a user story must satisfy to be accepted as
 complete
        '''
    )
    
    def backlog_node(state: MessagesState) -> Command[Literal['supervisor']]:
        r
esult = backlog_agent.invoke(state)
        return Command(
            update={
                'messages': [
         
           HumanMessage(content=result['messages'][-1].content, name='backlog_planner')
                ]
            },

            goto='supervisor',
        )
    
    sprint_agent = create_react_agent(
        llm, 
        tools=[get_i
nfo_for_sprint],
        state_modifier='''
        You are a Project Manager your job is to create:
        Critical Pa
th Analysis: Identifying user stories and tasks that are dependent.
        Generate a sprints plan that ensures:
      
  - User stories and tasks Prioritization
        - Timeline Assignment
        - Human resources allocation
        '''

    )
    
    def sprint_node(state: MessagesState) -> Command[Literal['supervisor']]:
        result = sprint_agent.i
nvoke(state)
        return Command(
            update={
                'messages': [
                    HumanMessage
(content=result['messages'][-1].content, name='sprint_planner')
                ]
            },
            goto='super
visor',
        )
    
    # Build the graph
    builder = StateGraph(MessagesState)
    
    # Add nodes and edges
    
builder.add_edge(START, 'supervisor')
    builder.add_node('supervisor', supervisor_node)
    builder.add_node('backlog_
planner', backlog_node)
    builder.add_node('sprint_planner', sprint_node)
    builder.add_edge('supervisor', 'backlog_
planner')
    builder.add_edge('supervisor', 'sprint_planner')
    builder.add_edge('backlog_planner', 'supervisor')
   
 builder.add_edge('sprint_planner', 'supervisor')
    builder.add_edge('supervisor', END)
    
    # Compile the graph
 
   graph = builder.compile()
    
    # Initialize and run
    initial_state = {
        'messages': [
            ('use
r', 'Let's start planning the project. What are the main requirements?')
        ]
    }
    from IPython.display import
 display, Image
    
    display(Image(graph.get_graph().draw_mermaid_png()))
    
    # Stream the graph execution
    
for s in graph.stream(initial_state, subgraphs=True):
        print(s)
        print('----')
    from typing import Lite
ral, List, Union
    from typing_extensions import TypedDict
    from langchain_anthropic import ChatAnthropic
    from 
langchain_core.messages import HumanMessage
    from langgraph.graph import StateGraph, START, END, MessagesState
    fr
om langgraph.prebuilt import create_react_agent
    from langgraph.types import Command
    from langchain_google_genai 
import ChatGoogleGenerativeAI
    from langchain_anthropic import ChatAnthropic
    
    
    
    
    
    # Create th
e LLM
    llm = ChatGoogleGenerativeAI(
        model='gemini-1.5-pro',
        temperature=0,
        api_key='AIzaSyB3
2phvdWNdNzH6R6sKvR8EKfVmJPE5hV4'
    )
    # Define team members and create literal type
    members = ['backlog_planner
', 'sprint_planner']
    options = members + ['FINISH']
    NextType = Literal['backlog_planner', 'sprint_planner', 'FIN
ISH']
    
    
    # System prompt for supervisor
    system_prompt = (
        'You are a supervisor tasked with manag
ing a conversation between the'
        f' following workers: {members}. Given the following user request,'
        ' re
spond with the worker to act next. Each worker will perform a'
        ' task and respond with their results and status.
 When finished,'
        ' respond with FINISH.'
    )
    
    
    # Define router type with explicit literals
    cla
ss Router(TypedDict):
        '''Worker to route to next. If no workers needed, route to FINISH.'''
        next: NextTy
pe
    
    
    # Create supervisor node with explicit return type
    def supervisor_node(state: MessagesState) -> Com
mand[Union[Literal['backlog_planner', 'sprint_planner'], Literal['__end__']]]:
        messages = [
            {'role':
 'system', 'content': system_prompt},
        ] + state['messages']
        response = llm.with_structured_output(Router
).invoke(messages)
        goto = response['next']
        if goto == 'FINISH':
            goto = END
        return Co
mmand(goto=goto)
    
    
    # Rest of your code remains the same
    backlog_agent = create_react_agent(
        llm,
 
        tools=[get_info_for_backlog],
        state_modifier='''
        You are a Business analyst, your job is to de
tail the product backlog that includes:
        Epics: High-level requirements outlining significant chunks of functiona
lity.
        User Stories: Smaller, actionable requirements that detail what needs to be achieved.
        Acceptance C
riteria: Conditions that a user story must satisfy to be accepted as complete
        '''
    )
    
    
    def backlo
g_node(state: MessagesState) -> Command[Literal['supervisor']]:
        result = backlog_agent.invoke(state)
        ret
urn Command(
            update={
                'messages': [
                    HumanMessage(content=result['message
s'][-1].content, name='backlog_planner')
                ]
            },
            goto='supervisor',
        )
    

    
    sprint_agent = create_react_agent(
        llm, 
        tools=[get_info_for_sprint],
        state_modifier=''
'
        You are a Project Manager your job is to create:
        Critical Path Analysis: Identifying user stories and 
tasks that are dependent.
        Generate a sprints plan that ensures:
        - User stories and tasks Prioritization

        - Timeline Assignment
        - Human resources allocation
        '''
    )
    
    
    def sprint_node(state
: MessagesState) -> Command[Literal['supervisor']]:
        result = sprint_agent.invoke(state)
        return Command(

            update={
                'messages': [
                    HumanMessage(content=result['messages'][-1].conte
nt, name='sprint_planner')
                ]
            },
            goto='supervisor',
        )
    
    
    # Bui
ld the graph
    builder = StateGraph(MessagesState)
    
    
    # Add nodes and edges
    builder.add_edge(START, 'su
pervisor')
    builder.add_node('supervisor', supervisor_node)
    builder.add_node('backlog_planner', backlog_node)
   
 builder.add_node('sprint_planner', sprint_node)
    builder.add_edge('supervisor', 'backlog_planner')
    builder.add_e
dge('supervisor', 'sprint_planner')
    builder.add_edge('backlog_planner', 'supervisor')
    builder.add_edge('sprint_p
lanner', 'supervisor')
    builder.add_edge('supervisor', END)
    
    
    # Compile the graph
    graph = builder.com
pile()
    
    
    # Initialize and run
    initial_state = {
        'messages': [
            ('user', 'Let's start 
planning the project. What are the main requirements?')
        ]
    }
    from IPython.display import display, Image
 
   
    
    display(Image(graph.get_graph().draw_mermaid_png()))
    
    
    # Stream the graph execution
    for s i
n graph.stream(initial_state, subgraphs=True):
        print(s)
        print('----')
```
---

     
 
all -  [ Help Me Build the Home Depot of AI ](https://www.reddit.com/r/LangChain/comments/1hil1l5/help_me_build_the_home_depot_of_ai/) , 2024-12-21-0912
```
I own a 2 month old startup Analytics Depot and for 2025, I'm aiming to make it the one stop shop for AI solutions. Like
 Home Depot, but for AI + Analytics. It will have industry related AI solutions for insurance, real estate, finance, leg
al, medical, oil and gas, management, etc. Can add additional services through APIs or something.



Right now I got 2 f
unctioning versions built. (Don't judge me, my experience is below basic :|)

1) Plain chatgpt wrapper with prompting fo
r the different industries.

2) Wrapper with domain specific BERT models for the different industries. 



I'm looking f
or qualified individuals who have lots of knowledge and experience in this space and can take this to another level. Rea
lly hoping to make this a $B+ company and I think the branding is perfectly positioned for that. Give Data Bricks and Sn
owFlake a few reasons to fight over us.



I'm looking for solutions that can get such valuations. In exchange, I can of
fer pay or equity or a combination of the two.



If this sounds interesting, DM me.
```
---

     
 
all -  [ Fast sentence transformer embeddings generation on CPU for question answering ](https://www.reddit.com/r/LangChain/comments/1hiil85/fast_sentence_transformer_embeddings_generation/) , 2024-12-21-0912
```
We have millions of documents which we want to be searchable through direct question answering (snippet based, as oppose
d to generation based, like the highlighted snippet in the following screenshot below the generated bit in Google)

http
s://preview.redd.it/4rwpsmw3yz7e1.png?width=1866&format=png&auto=webp&s=ea0178b40fc1a66a97beee7596cb70a8de52bbe1

So, fo
r this, we have to generate embeddings for all those millions of documents, put them in vector DB, and make them queryab
le at runtime. GPUs are outside our budget, so we have to do this on CPUs alone. Questions:

1. Any CPU friendly embeddi
ng model or architecture which enables us to extract sentence embeddings for all documents in our collection (followed b
y insertion in vector DB) at a pretty quick speed (comparable to GPUs) - even if it means keeping the number of dimensio
ns modest (as long as the snippet answer quality is decent)?
2. Any CPU friendly vector DB which would allow us infering
 snippets given a question at runtime pretty much in real time for high volume traffic (much like Google does here)? If 
the bottleneck for this is CPU cores, let us assume we have lots of them, since even then they are an order of magnitude
 cheaper than GPUs like A100 or H100.
3. Whatever solutions exist to the above questions - will they automatically apply
 to multiple languages, or do we have to further training and retraining with corpuses from those languages to make this
 work?
4. Will generating binary sentence embeddings on CPUs do it much faster (offsetting whatever delays normal senten
ce transformers achieve on CPUs instead of GPUs)? Like Matryoshka Embeddings?
```
---

     
 
all -  [ Straightforward way to persist memory ](https://www.reddit.com/r/LangChain/comments/1hihvwd/straightforward_way_to_persist_memory/) , 2024-12-21-0912
```
I'm making an agent with LangGraph and want to persist its chat memory across sessions. There are no multiple users so a
 database may be overkill. I'm aware I need to use MemorySaver and a store. However it's unclear to me what persistent s
tores are implemented and if it will suffice to just add the MemorySaver and the store object to the graph, or if any ad
ditional code is needed to write messages to memory and restore them at the start of a session. 
```
---

     
 
all -  [ Looking for Help with LangChain Course – Your Support Would Mean a Lot! ](https://www.reddit.com/r/UdemyCoders/comments/1higtcg/looking_for_help_with_langchain_course_your/) , 2024-12-21-0912
```
Hi everyone,

I’m eager to learn from the course '[Learn LangChain: Build 22 LLM Apps Using OpenAI & Llama 2](https://ww
w.udemy.com/course/learn-langchain-build-12-llm-apps-using-openai-llama-2/?couponCode=KEEPLEARNING).' If someone has acc
ess to this course and can help me out, I’d be extremely grateful!

Looking forward to any support or guidance you can p
rovide.

Thanks in advance,

Rahul
```
---

     
 
all -  [ Good library for LLM management ](https://www.reddit.com/r/rust/comments/1highnw/good_library_for_llm_management/) , 2024-12-21-0912
```
I have a personal project already running that uses the async-openai crate for LLM management, effectively limiting myse
lf to OpenAI‘s models. 
Now I want to switch to another library to support other LLM providers too. 

My sight is on lan
gchain-rust, as it would support all large providers, but the project is pretty dead; little commits and many open issue
s. Any good suggestions for other libraries?

Edit: sorry, I forgot to add that I want the library to stream tool calls
```
---

     
 
all -  [ HELP: Not able to use embeddings from langchain_huggingface library (HuggingFaceEmbeddings) due to s ](https://www.reddit.com/r/LangChain/comments/1hiekwz/help_not_able_to_use_embeddings_from_langchain/) , 2024-12-21-0912
```
Hi all

    from langchain_huggingface import HuggingFaceEmbeddings
    embeddings = HuggingFaceEmbeddings(model_name='B
AAI/bge-large-en')

Running this code is giving me this error   
`Could not import sentence_transformers python package.
 Please install it with \`pip install sentence-transformers\`.`

I have tried the following but could not get it working


* `pip install sentence-transformers`  
* Degrading version to `sentence-transformers==2.6.0`
* Try using python 3.9, 
3.10, 3.11, 3.12

Has anyone faced this? Here are the packages installed

* `langchain                               0.3
.13`
* `langchain-community                     0.3.13`
* `langchain-core                          0.3.28`
* `langchain-
huggingface                   0.1.2`
* `torch                                   2.5.1` 
* `transformers                 
           4.47.1`
* `sentence-transformers                   3.3.1`
```
---

     
 
all -  [ Tables chucking strategy  ](https://www.reddit.com/r/LangChain/comments/1hiekwp/tables_chucking_strategy/) , 2024-12-21-0912
```
I'm working on a Unstructured pdf document with each page containing Some text and multiple tables some tables spanning 
3-4 pages sometimes.


Issue : I'm not able to find an appropriate chucking methodology for tables spanning multiple pag
es as the next page table missing out the data related to previous one and not able to combine them based on a common po
int.


Using Pymupdf4llm  as a document parser and chucking each page as a one chunk for now. 

```
---

     
 
all -  [ LangGraph Tool/Multi-Agent conceptual question ](https://www.reddit.com/r/LangChain/comments/1hibhj8/langgraph_toolmultiagent_conceptual_question/) , 2024-12-21-0912
```
Hi LangChain/LangGraph community.

I'm trying to understand how to build this functionality using either a multi agent a
rchitecture or multiple tools. I have a chat interface and I need to keep track of state throughout a user's chat thread
. For each user message, I need to update a object with a summary of what the user said, and I am using an llm with stru
ctured output to update that state. I also need to then possibly call other tools depending on the input. For example, f
or some input, I need to make a call to the database to fetch some information. I also want to store every chat message 
sent by either the AI or the human, and also update the state in the database on every response.

Is this type of workfl
ow more suitable for a single agent with multiple tools? Or should I make a separate agent for each task that needs to b
e done? Thanks!
```
---

     
 
all -  [ Automation Software Testing Engineer here, looking to make shift to a career in AI engineering. ](https://www.reddit.com/r/cscareerquestions/comments/1hib7lc/automation_software_testing_engineer_here_looking/) , 2024-12-21-0912
```
I have total experience of 6 years into software testing / QA. I have worked on python, did some certifications in Gen A
I & Langchain and still few in progress. I am creating projects side by side as well.
My question - Is it absolutely nec
essary to have core dev experience ? Do companies consider the knowledge and self taught projects that an individual pos
sess or they only consider AI Engineers with ‘relevant’ experience ??
```
---

     
 
all -  [ Did a quick comparison between 10 LLMs for OCR task ](https://www.reddit.com/r/LangChain/comments/1hi9ee7/did_a_quick_comparison_between_10_llms_for_ocr/) , 2024-12-21-0912
```
Video: [https://youtu.be/yT-7i5npRBQ?feature=shared](https://youtu.be/yT-7i5npRBQ?feature=shared)

Code: [https://github
.com/trancethehuman/ai-workshop-code/tree/main/projects/ocr-battle](https://github.com/trancethehuman/ai-workshop-code/t
ree/main/projects/ocr-battle)

  
Let me know which ones you're currently using - I'd love to know if gemini is still th
e best for the price / performance.
```
---

     
 
all -  [ Self-Aware Software Using LangChain & LangGraph ](https://www.reddit.com/r/LangChain/comments/1hi8c3y/selfaware_software_using_langchain_langgraph/) , 2024-12-21-0912
```
Hello,

Weve been able to merge an LLM with our LangGraph Agent Builder. 

This turns our product from a piece of static
 software into a reasoning agent. In these two short demos I show how we ask our tool to perform functions within the to
ol. The LLM and our tool become one. Enjoy!

https://youtu.be/jSz-95OS_ik?si=CAgMjayyxxAjPjGl

https://youtu.be/iiDWPlro
rs4?si=BB2HlzRr0e_Ua7tC
```
---

     
 
all -  [ [1 YoE] Computer Science Graduate, International student applying to jobs in the ML/AI Field. ](https://www.reddit.com/r/EngineeringResumes/comments/1hi60ro/1_yoe_computer_science_graduate_international/) , 2024-12-21-0912
```
I have 1 year of co-orporate experience and 3 internships. I am an interantional student who has applied for opt and sea
rching jobs with sponsership. I have developed my skills in the vast galaxy of computer science towards the things I lov
e to do - Machine Learning (cliche right?). Any help as appericaited.

https://preview.redd.it/rihct0zv1w7e1.png?width=1
700&format=png&auto=webp&s=1432e633482db8a7a6846b2d153ac620f8b8d95f


```
---

     
 
all -  [ How do CustomGPTs from ChatGPT work in the background with the knowledge base? ](https://www.reddit.com/r/ChatGPTPro/comments/1hi5zo2/how_do_customgpts_from_chatgpt_work_in_the/) , 2024-12-21-0912
```
Here is a description of how RAG structures are constructed: [https://python.langchain.com/docs/tutorials/rag/](https://
python.langchain.com/docs/tutorials/rag/) I now wonder: Does a CustomGPT already do this with the uploaded data? Or does
 it make sense to integrate such a RAG structure yourself?

Theoretically, it could also be that ChatGPT does not carry 
out this processing and simply checks which file could contain what is needed and adds it internally as a whole as the c
ontext of the request.

What would you guess is how it works in practice?
```
---

     
 
all -  [ Wie arbeiten CustomGPTs von ChatGPT im Hintergrund mit der Wissensbasis? ](https://www.reddit.com/r/KI_Welt/comments/1hi5xpi/wie_arbeiten_customgpts_von_chatgpt_im/) , 2024-12-21-0912
```
Hier wird ja beschrieben wie RAG Strukturen aufgebaut sind: [https://python.langchain.com/docs/tutorials/rag/](https://p
ython.langchain.com/docs/tutorials/rag/) Ich frage mich nun: Macht ein CustomGPT dies mit den hochgeladenen Daten bereit
s? Oder ist es sinnvoll, eine solche RAG Struktur selbst zu integrieren?

Theoretisch könnte es ja auch sein, dass ChatG
PT diese Verarbeitung nicht vornimmt und einfach nur prüft welche Datei könnte das enthalten was man braucht und es inte
rn insgesamt als Kontext der Anfrage hinzufügt.

Was wäre eure Vermutung wie es in der Praxis erfolgt?
```
---

     
 
all -  [ Any decents RAG document management tool? ](https://www.reddit.com/r/LangChain/comments/1hhziyd/any_decents_rag_document_management_tool/) , 2024-12-21-0912
```
Hi fellow devs,

Does anyone know if there's an opensource tool with built for managing RAG document?

Imagine a drag-an
d-drop web interface for users to upload multiple documents.

Once uploaded, the system should:

1. Store the documents 
in some kind of storage (like S3, Blob Storage).
2. Trigger a pipeline to handle chunking and embedding generation.
3. I
nsert the processed data into a database (vector DB like Pinecone, Weaviate, or Postgres).

I already have a QA chatbot 
set up, so I don’t need any chat functionality like Ragflow, Onyx or Open Web UI just the document ingestion pipeline wi
th a user-friendly web UI.

I checked out Qdrant UI and Milvus Attu but they seem to have only data management functiona
lity not the ingestion pipeline.

Does anyone know of existing tools or frameworks that can do this, or am I better off 
building something custom?

Thanks!
```
---

     
 
all -  [ These are the most popular LLM Orchestration frameworks ](https://www.reddit.com/r/OpenAIDev/comments/1hhzhgz/these_are_the_most_popular_llm_orchestration/) , 2024-12-21-0912
```
[Most popular LLM Orchestration frameworks](https://preview.redd.it/g5rbvpg65u7e1.png?width=2388&format=png&auto=webp&s=
fbd49e1501c388b46d6bc52394913ba2a99e9de4)

This has come up a few times before in questions about the most popular LLM F
rameworks, so I've done some digging and started by looking at Github stars - It's quite useful to see the breakdown

So
 ... here they are, the [most popular LLM Orchestration frameworks](https://prompt-shield.com/blog/top-llm-orchestration
-frameworks/)

Next, I'm planning to add:

* NPM/Pypi download numbers - already have some of them
* Number of times the
y're used in open source projects

So, let me know if it's of any use, if there's any other numbers you want to see and 
also, if there are any frameworks that I've missed. I've tried to collate from previous threads so hopefully I've got mo
st of them.
```
---

     
 
all -  [ What LLM Framework would you use in 2025? Langchain vs Pydantic AI vs ... ](https://www.reddit.com/r/ChatGPT/comments/1hhvexp/what_llm_framework_would_you_use_in_2025/) , 2024-12-21-0912
```
Every time I think about using langchain I rewrite a new version of my own model agnostic system. I feel like each one o
f those feel 'wrong' and over complicated in the syntax. Guidance-AI was decent when it was MS Guidance that ran on Jinj
a-like prompts, but now they langchainified themselves to be more 'Pythonic' and the syntax is all weird. 

Who is going
 to use what in 2025?
```
---

     
 
all -  [ Providing n8n automation for 25 usd only  ](https://www.reddit.com/r/aiagents/comments/1hhuhx4/providing_n8n_automation_for_25_usd_only/) , 2024-12-21-0912
```
Hi Everyone I have been experimenting with n8n for sometime. I have done few projects like 
1. Telegram personal assista
nt which answers your question based on your drive data 
2. Assigning labels to gmail 
3. Custom webhook 

Now I want to
 explore more and see what people are trying to build in their life/businesses. 

Apart from this I am an experienced de
veloper with experience in langchain, python, nodejs, etc. 

Anyone who needs a workflow automation, ai agent developmen
t, chatbot development. I am ready to help..
Charges: 25 USD only (just to avoid spam)
```
---

     
 
all -  [ How an AI Agent is Revolutionizing News Consumption ](https://open.substack.com/pub/diamantai/p/stop-reading-start-understanding?r=336pe4&utm_campaign=post&utm_medium=web&showWelcomeOnShare=true) , 2024-12-21-0912
```
I just published a blog diving deep into an AI-powered news agent that redefines how we stay informed. 
The blog covers:


- The challenge of information overload and how this agent cuts through the noise.
- How LangGraph designs the agent's
 behavior to dynamically adapt and prioritize relevance.
- The system’s ability to not just summarize articles, but inte
grate and unify insights across multiple sources.
- What makes it technically innovative, from adaptive workflows to mul
titasking capabilities.
```
---

     
 
all -  [ Please roast my resume as much as you can, currently in my 3rd year. ](https://www.reddit.com/gallery/1hhqorb) , 2024-12-21-0912
```

```
---

     
 
all -  [ Is there a preprocessing before splitting for RAG? ](https://www.reddit.com/r/LangChain/comments/1hhqlct/is_there_a_preprocessing_before_splitting_for_rag/) , 2024-12-21-0912
```
Hi, in traditional machine learning, a significant amount of time is spent on preprocessing data before training models.
 Is there a similar preprocessing step required **before splitting** documents for retrieval in a Retrieval-Augmented Ge
neration (RAG) setup? If so, what are the best practices or common techniques to ensure the data is optimized for the re
trieval process?
```
---

     
 
all -  [ Advanced RAG: Improving Retrieval using Hypothetical Document Embeddings ](https://i.redd.it/nsapewp9fs7e1.jpeg) , 2024-12-21-0912
```
Great article about enhancing the retrieval process in a Retrieval-Augmented Generation (RAG) system by incorporating Hy
pothetical Document Embeddings (HyDE). Our focus will be on implementing a robust pipeline using Langchain and LangGraph
, along with illustrative Python code for clear understanding.

https://devnavigator.com/home/advanced-rag-improving-ret
rieval-using-hypothetical-document-embeddings-d9bec3d7-dc54-4d3b-9e07-59da32b5ab34

```
---

     
 
all -  [ Filtering through metadata ](https://www.reddit.com/r/LangChain/comments/1hhqhkj/filtering_through_metadata/) , 2024-12-21-0912
```
I want to build a RAG using a lessons learned database with LangChain. The original Lessons Learned DB is a table, which
 I export as csv and then convert into a ChromaDB.

I merge each entry or row into a text blob, which I then try to tag 
with metadata such as ID, title and project. The text blob also has the column “Best Practice”, which can be true or fal
se.

If I start a query like: “Give me examples with good best practice”. Entries are also returned which are “Best Prat
ice: false”. This is probably because “Best Practice: true” and “Best Pratice: false” are very close to each other in th
e embedding.

Therefore, my idea would be to include the “Best Pratice” in the metadata.

Here is my question: Is the si
milarity search even carried out through the metadata? Or only through the page content? Is it possible to filter via th
e metadata with LangChain?

I currently use my RAG to get the relevant entries back like this:

    retriever = chroma_d
b.as_retriever(search_type='similarity_score_threshold',
                                       search_kwargs={'score_th
reshold': 0.2,
                                       'k': 10}
                                       )
```
---

     
 
all -  [ Which ai agent framework should I use?  ](https://www.reddit.com/r/AskProgramming/comments/1hhq98o/which_ai_agent_framework_should_i_use/) , 2024-12-21-0912
```
I want to learn  AI agents and multi-agent systems. I have strong knowledge of Python and coding, and I want to learn an
d build a bit complex project which uses multi agents workflow , I see there are lot of agentic frameworks like langchai
n ,langgraph, crew ai , pydantic ai , phidata, swarm ai...etc. However, I’m not sure which framework to start with.

Her
e’s what I’m looking for in a framework:


Structured Outputs: I want the framework to provide well-organized and Struct
ured results.

Support for Multi-Agent Systems: It should allow creating multiple agents that can possibly communicate w
ith each other.

Memory and history sharing: agents should maintain memory and share memory when needed , making more dy
namic and collaborative environment.

Examples & Community Support: A good number of examples or tutorials to get starte
d would be a huge plus.

Also, if you know of any tutorials, YouTube playlists, channels, or other resources (apart from
 official documentation) that could help me learn, please share them.


Thanks.
```
---

     
 
all -  [ Markitdown vs pypdf ](https://www.reddit.com/r/LangChain/comments/1hhlsmz/markitdown_vs_pypdf/) , 2024-12-21-0912
```
Markitdown vs pypdf

So did anyone try markitdown by microsoft fairly extensively? How good is it when compared to pypdf
, the default library for pdf to text?. I am working on rag at my workplace but really struggling with medium complex pd
fs (no images but lot of tables). I havent tried markitdown yet. So love to get some opinions. Thanks!
```
---

     
 
all -  [ Help regarding ollama deployment. ](https://www.reddit.com/r/LocalLLaMA/comments/1hhlgtf/help_regarding_ollama_deployment/) , 2024-12-21-0912
```

I was developing a simple rag agent that helps you chat to the provided pdfs using a simple langchain agent. It uses ll
ama3.2:3b as the model and chromadb as the vectordb. 

I wanted to make it an api ans deploy it on aws. So does anyone h
ave any suggested workflow on how to go about doing it? And also if I would have  to switch to a cloud base vectordb lik
e pinecone?
```
---

     
 
all -  [ Implementing Retrieval-Augmented Generation with LangChain, Pgvector and OpenAI ](https://www.reddit.com/r/Python/comments/1hhlg8x/implementing_retrievalaugmented_generation_with/) , 2024-12-21-0912
```
[https://www.codemancers.com/blog/2024-10-24-rag-with-langchain/?utm\_source=Social+media&utm\_medium=reddit](https://ww
w.codemancers.com/blog/2024-10-24-rag-with-langchain/?utm_source=Social+media&utm_medium=reddit)
```
---

     
 
all -  [ Deploying local llama agent using aws ](https://www.reddit.com/r/LangChain/comments/1hhlfw9/deploying_local_llama_agent_using_aws/) , 2024-12-21-0912
```
I was developing a simple rag agent that helps you chat to the provided pdfs using a simple langchain agent. It uses lla
ma3.2:3b as the model and chromadb as the vectordb. 

I wanted to make it an api ans deploy it on aws. So does anyone ha
ve any suggested workflow on how to go about doing it? And also if I would have  to switch to a cloud base vectordb like
 pinecone?
```
---

     
 
all -  [ I've developed an 'Axiom Prompt Engineering' system that's producing fascinating results. Let's test ](https://www.reddit.com/r/LangChain/comments/1hhkcoi/ive_developed_an_axiom_prompt_engineering_system/) , 2024-12-21-0912
```
I've been experimenting with a mathematical axiom-based approach to prompt engineering that's yielding consistently stro
ng results across different LLM use cases. I'd love to share it with fellow prompt engineers and see how we can collecti
vely improve it.

Here's the base axiom structure:  
Axiom: max(OutputValue(response, context))  
subject to ∀element ∈ 
Response,  
(  
precision(element, P) ∧  
depth(element, D) ∧  
insight(element, I) ∧  
utility(element, U) ∧  
coherenc
e(element, C)  
)

Core Optimization Parameters:  
• P = f(accuracy, relevance, specificity)  
• D = g(comprehensiveness
, nuance, expertise)  
• I = h(novel\_perspectives, pattern\_recognition)  
• U = i(actionable\_value, practical\_applic
ation)  
• C = j(logical\_flow, structural\_integrity)

Implementation Vectors:

1. max(understanding\_depth) where comp
rehension = {context + intent + nuance}
2. max(response\_quality) where quality = { expertise\_level + insight\_generati
on + practical\_value + clarity\_of\_expression }
3. max(execution\_precision) where precision = { task\_alignment + det
ail\_optimization + format\_appropriateness }

Response Generation Protocol:

1. Context Analysis: - Decode explicit req
uirements - Infer implicit needs - Identify critical constraints - Map domain knowledge
2. Solution Architecture: - Stru
cture optimal approach - Select relevant frameworks - Configure response parameters - Design delivery format
3. Content 
Generation: - Deploy domain expertise - Apply critical analysis - Generate novel insights - Ensure practical utility
4. 
Quality Assurance: - Validate accuracy - Verify completeness - Ensure coherence - Optimize clarity

Output Requirements:
  
• Precise understanding demonstration  
• Comprehensive solution delivery  
• Actionable insights provision  
• Clear
 communication structure  
• Practical value emphasis

Execution Standards:  
\- Maintain highest expertise level  
\- E
nsure deep comprehension  
\- Provide actionable value  
\- Generate novel insights  
\- Optimize clarity and coherence


Terminal Condition:  
ResponseValue(output) ≥ max(possible\_solution\_quality)

Execute comprehensive response generati
on sequence.  
END AXIOM

What makes this interesting:

1. It's a systematic approach combining mathematical optimizatio
n principles with natural language directives
2. The axiom structure seems to help LLMs 'lock in' to expert-level respon
se patterns
3. It's producing notably consistent results across different models
4. The framework is highly adaptable - 
I've successfully used it for everything from viral content generation to technical documentation

I'd love to see:

* Y
our results testing this prompt structure
* Modifications you make to improve it
* Edge cases where it performs particul
arly well or poorly
* Your thoughts on why/how this approach affects LLM outputs

  
try this and see what your llm says
 id love to know 

'How would you interpret this axiom as a directive?

max(sum ∆ID(token, i | prompt, L))

subject to ∀
token ∈ Tokens, (context(token, C) ∧ structure(token, S) ∧ coherence(token, R))'

EDIT: Really enjoying the discussion a
nd decided to create a repo here [codedidit/axiomprompting](https://github.com/codedidit/axiomprompting) we can use to s
hare training data and optimizations. Im still setting it up if anyone wants to help! 
```
---

     
 
all -  [ LangChainDeprecationWarning ](https://www.reddit.com/r/LangChain/comments/1hhemqy/langchaindeprecationwarning/) , 2024-12-21-0912
```
I found that when I call SQLChatMessageHistory(), it yields the following warning message: LangChainDeprecationWarning: 
\`connection\_string\` was deprecated in LangChain 0.2.2 and will be removed in 1.0. Use connection instead.  
history =
 get\_session\_history(user\_id)



Since it is a LangChain API, what can I do about it?
```
---

     
 
all -  [ Flexible number of retrievals for RAG ](https://www.reddit.com/r/LangChain/comments/1hhe1so/flexible_number_of_retrievals_for_rag/) , 2024-12-21-0912
```
I am currently learning LangChain and would like to build a RAG with Chroma. In the classic approach, you always get a f
ixed number of retrievals back (Top K).

With this approach, however, other important retrievals might not be considered
 or unimportant ones might be included in the context.

A flexible approach would be much better here. Simply specify a 
maximum number of retrievals, e.g. 5, and a semantic threshold above which they are selected.

If there is a lot of data
, the LLM gets more context; if there is no good data, perhaps only one. This also reduces the risk of hallucinating.

I
s there such an approach with LangChain and Chroma?
```
---

     
 
all -  [ Possible to build collaborative agents in Langchain? ](https://www.reddit.com/r/LangChain/comments/1hhbqfg/possible_to_build_collaborative_agents_in/) , 2024-12-21-0912
```
**Do not post your self promoting website or tool. Not interested**

I have come into a project already deep in Langchai
n so probably not feasible to move to something else. Has anyone built actually useful collaborative agents in Langchain
? I am building a technical forum moderator that can go answer user's technical questions

For that I need
1. RAG to fin
d previously asked similar questions
2. Website crawler tools that can go research the contents of wikis and links menti
oned
3. SQL capable agent that can query internal database for some data

There will be questions where I need to break 
down the task and use all of those capabilities in a certain order. How are people approaching building stuff like this?


Potentially open to Lang graph if you all will say is the right move. I just want something I'm not twisting myself in
 a knot to build and modularize

I have looked into crewAI and what not but they are too high level and don't give the l
evel of control I want with chaining and passing around inputs

```
---

     
 
all -  [ Provable Answers – The Missing Piece to Trusting AI Responses? ](https://www.reddit.com/r/LangChain/comments/1hh89um/provable_answers_the_missing_piece_to_trusting_ai/) , 2024-12-21-0912
```
The number one reason LLM projects fail is the **quality of AI answers**. This is a far bigger issue than performance or
 latency.

Verifying the accuracy of LLM-generated answers, especially when working with private or enterprise data, is 
particularly challenging. It is not like fact-checking public information through a quick Google search. Verifying inter
nal data is harder, slower, and often not something users are motivated to do. If users don’t trust the answers, they’ll
 stop using the agent.

To address this, we built **Proving**—a tool that cryptographically proves the correctness of AI
-generated answers for private database queries.

Here’s how it works:

A user asks a natural language question. The too
l translates the question into SQL, runs the query, and returns the answer in natural language **along with a proof** th
at verifies:

* The SQL query it ran.
* That the query included all relevant data.

Currently, the tool supports Natural
 Language to SQL queries on PostgreSQL, MySQL, and SQLite (yes we use Langchain!)

[Here’s a link to our blog for more d
etails.](https://provably.ai/blog/introducing-proving-a-technique-to-rapidly-verify-and-trust-ai-answers)

We’d love you
r feedback:

1. Would this kind of tool accelerate AI answer verification?
2. Could tools like this help reduce user anx
iety around trusting AI answers?
3. Are you using LLMs to query data? Would you like to explore whether this tool could 
help increase user trust?
```
---

     
 
all -  [ Crewai vs LangChain: Which is better for building agentic apps? ](https://www.reddit.com/r/crewai/comments/1hh438u/crewai_vs_langchain_which_is_better_for_building/) , 2024-12-21-0912
```
I’m trying to choose between Crewai and LangChain for developing agent-based applications.i have 3 questions 
1. Which t
ool offers an easier learning curve?
2. Which one provides better flexibility and ease of use for building complex workf
lows?
3. Are there any notable limitations or strengths of one over the other?
Any insights, especially from those who’v
e worked with both, would be greatly appreciated!


```
---

     
 
all -  [ [For Hire] Skilled Full Stack Developer, AI/ML Expert, and DevOps Pro – Let’s Build Your Next Game-C ](https://www.reddit.com/r/forhire/comments/1hh3dd2/for_hire_skilled_full_stack_developer_aiml_expert/) , 2024-12-21-0912
```
🚀 **Full Stack Developer | AI/ML Engineer | DevOps Specialist – Open for Hire**!

Hi there! I'm Sheryar 👋, a passionate 
developer with the skills and experience to bring your vision to life. Here's what I bring to the table:

# 💻 Full Stack
 Development Expertise

* **Frontend:** React | Angular
* **Backend:** Node.js | NestJS
* **Payments:** Seamless Stripe 
Integrations
* **Cloud Services:** AWS | GCP

# 🤖 AI & Machine Learning Innovations

* Smart Chatbots built with LangCha
in
* Custom NLP models for automation and insights

# ⚙️ DevOps Solutions for Scalable Systems

* **CI/CD Pipelines:** G
itHub Actions | Jenkins
* **Containerization:** Docker | Kubernetes
* **Infrastructure as Code:** Terraform | Ansible

#
 🌟 Notable Projects

* 🚗 **Ride-Sharing App**: Real-time tracking & payment flows
* 📦 **Logistics Platform**: Route opti
mization for multi-stop deliveries
* 🛒 **E-Commerce Infrastructure**: Scalable Kubernetes clusters

# 💰 Rates

* $10–$15
/hour (negotiable based on project scope)

  
Also available for contract-based jobs.

📧 **DM me to discuss your project
 needs**!  
🔗 **GitHub**: [storm1033](https://github.com/storm1033)

Let’s collaborate and turn your ideas into reality!
 🌟
```
---

     
 
all -  [ How to Add PDF Understanding to your AI Agents ](https://www.reddit.com/r/LangChain/comments/1hh25yw/how_to_add_pdf_understanding_to_your_ai_agents/) , 2024-12-21-0912
```
Most of the agents I build for customers need some level of PDF Understanding to work. I spent a lot of time testing out
 different approaches and implementations before landing on one that seems to work well regardless of the file contents 
and infrastructure requirements.

tl;dr:

>What a number of LLM researchers have figured out over the last year is that 
vision models are actually really good at understanding images of documents. And it makes sense that some significant po
rtion of multi-modal LLM training data is images of pages of documents... the internet is full of them.  
So in addition
 to extracting the text, if we can also convert the document's pages to images then we can send BOTH to the LLM and get 
a much better understanding of the document's content.

link to full blog post: [https://www.asterave.com/blog/pdf-under
standing](https://www.asterave.com/blog/pdf-understanding)
```
---

     
 
all -  [ We created a playground using Anthropic's computer use and Langchain ](https://www.reddit.com/r/aidevtools/comments/1hgzatq/we_created_a_playground_using_anthropics_computer/) , 2024-12-21-0912
```
Currently, AI's capability cannot perform most real-world tasks. The biggest obstacle is that LLMs are still insufficien
t. However, current LLMs can handle repetitive tasks, jobs within a specific framework, and tasks requiring minimal inte
lligence. We've created a playground environment where you can test this [http://playground.gca.dev](http://playground.g
ca.dev/)
```
---

     
 
all -  [  LangChain - ChatOLLAMA model - calling tool on every input  ](https://www.reddit.com/r/LangChain/comments/1hgy388/langchain_chatollama_model_calling_tool_on_every/) , 2024-12-21-0912
```
* *llama3.2:1b*
* *llama3.2:3b*
* *llama3.2:1b-instruct-fp16*
* *llama3.1:8b*

I've tested above models and all the abov
e models are calling tools even with simple query like 'hi'.

the behavior is same whether binding :

* **tools\_list**

* **openai\_format\_tools\_list**

Need help.

Result:

    python 1_tool_calling_test.py 
    content='' additional_kwa
rgs={} response_metadata={'model': 'llama3.1:8b', 'created_at': '2024-12-18T09:17:37.90843589Z', 'done': True, 'done_rea
son': 'stop', 'total_duration': 72841245771, 'load_duration': 13778033737, 'prompt_eval_count': 194, 'prompt_eval_durati
on': 50723000000, 'eval_count': 22, 'eval_duration': 8337000000, 'message': Message(role='assistant', content='', images
=None, tool_calls=[ToolCall(function=Function(name='tavily_search_results_json', arguments={'query': 'current events'}))
])} id='run-8931e574-9297-4ce9-93f1-54d00ce8c413-0' tool_calls=[{'name': 'tavily_search_results_json', 'args': {'query':
 'current events'}, 'id': '82754a8a-619b-4a1e-85d3-cb767d4c6a9f', 'type': 'tool_call'}] usage_metadata={'input_tokens': 
194, 'output_tokens': 22, 'total_tokens': 216} 
    
    
    [{'name': 'tavily_search_results_json', 'args': {'query': 
'current events'}, 'id': '82754a8a-619b-4a1e-85d3-cb767d4c6a9f', 'type': 'tool_call'}]
    

Code For testing:

    from
 typing import List
    from dotenv import load_dotenv, find_dotenv
    load_dotenv(find_dotenv())
    from langchain_co
re.tools import tool
    from langchain_ollama import ChatOllama
    from langchain_community.tools.tavily_search import
 TavilySearchResults
    from langchain_core.utils.function_calling import convert_to_openai_tool
    
    # @tool
    #
 def web_search_tool(web_query: str) -> str:
    #     '''
    #     Use this tool only when you need to use web search 
in order to find an answer for user.
    #     Args:
    #         web_query (str) : the query for web search
        
 
   #     '''
    #     search = TavilySearchResults()
    #     results = search.invoke(query)
    #     return results

    
    web_search_tool = TavilySearchResults()
    
    tools_list = [web_search_tool]
    openai_format_tools_list = 
[convert_to_openai_tool(f) for f in tools_list]
    
    llm = ChatOllama(model='llama3.1:8b', temperature=0).bind_tools
(tools_list)
    
    result = llm.invoke('Hi, how are you?')
    
    print(result,'\n\n')
    print(result.tool_calls)

    
    
```
---

     
 
all -  [ with_stuctured_output in create_react_agent ](https://www.reddit.com/r/LangChain/comments/1hgxyb5/with_stuctured_output_in_create_react_agent/) , 2024-12-21-0912
```
Hello!

Can somebody help me? I'm currently building a multi agent system usung langchain and langgraph. But I don't fin
d any articles about how to use StucturedOutput in create_react_agent, is there a way that I can do this?
```
---

     
 
MachineLearning -  [ [P] Minima: local conversational retrieval augmented generation project (Ollama, Langchain, FastAPI, ](https://www.reddit.com/r/MachineLearning/comments/1h1pudq/p_minima_local_conversational_retrieval_augmented/) , 2024-12-21-0912
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

     
