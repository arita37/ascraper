 
all -  [ 0% Callback rate so far in USA! ](https://www.reddit.com/r/resumes/comments/1dnqd15/0_callback_rate_so_far_in_usa/) , 2024-06-25-0910
```
Applied to over 580+ application for Data Analyst and Data Scientist role over US region. No call backs yet. Need your h
elp!

https://preview.redd.it/9nlx9qtnil8d1.png?width=688&format=png&auto=webp&s=26c61a7739b776daf91f8ff3ceb3e4abf9a93d6
0


```
---

     
 
all -  [ How to build efficient RAG with codebase? ](https://www.reddit.com/r/LangChain/comments/1dnos9r/how_to_build_efficient_rag_with_codebase/) , 2024-06-25-0910
```
I have tried parsing AST of codebase to create function signatures and body and embedded it in vector database. What wou
ld be the best way to prepare the codebase? 
```
---

     
 
all -  [ Handling private data without self-hosting etc. ](https://www.reddit.com/r/LangChain/comments/1dno1ll/handling_private_data_without_selfhosting_etc/) , 2024-06-25-0910
```
Is there a way to handle private data, like user input from a form without anonymouzation (eg presidio) and especially w
hile using the regular openai API?
```
---

     
 
all -  [ [HELP] Parallel function calling with Langgraph and Gemini 1.5 Pro ](https://www.reddit.com/r/LangChain/comments/1dnmeuy/help_parallel_function_calling_with_langgraph_and/) , 2024-06-25-0910
```
Hey everyone,

I'm currently working on a project involving LangGraph and Gemini Pro 1.5 (Vertex AI).

Gemini is not ret
urning multiple function calls for parallel execution. I need to make several tool calls (e.g., for different months). H
owever, it processes these calls sequentially, one at a time, which significantly increases the response time and costs 
due to token usage. For instance, if I need data for four months, it will:

1. Make the first tool call
2. Wait for the 
response
3. Make the second tool call
4. Wait for the response
5. And so on...

Previously, I had implemented parallel f
unction calling with LangChain's `AgentExecutor` class, where the agent would make all the necessary calls simultaneousl
y, wait for all responses, and then process them together. This parallel calling mechanism has stopped working with Lang
Graph. Maybe because now the prompt is much larger than before?

Any tips or advice?

Thanks in advance for your help!
```
---

     
 
all -  [ Building a Custom Text-2-SQL agent with tool, Llama 3 ](https://www.reddit.com/r/LangChain/comments/1dnm4tc/building_a_custom_text2sql_agent_with_tool_llama_3/) , 2024-06-25-0910
```
I'm working on a project that requires me to build a text-2-sql code generation pipeline. I've being playing around sql 
agent in langchain. The chain sometimes breaks since my DB is too huge for Llama 3 context window (model input limit is 
8K, hosted on bedrock). Since my pipeline to handle after retrieving the data from db is already handled using other cha
ins, my only doubt is that:

How can I build an agent in Langchain that takes the natural language as input, and provide
d with the db schema and information about tables, generates relevant sql query. 

I tried doing this using custom agent
 in langchain and have trouble defining tools for this and also, facing difficulty in getting the pipeline to work. 

wo
uld appreciate any suggestions/help. Thanks!
```
---

     
 
all -  [ LangGraph + Streamlit State Management ](https://www.reddit.com/r/LangChain/comments/1dngwkn/langgraph_streamlit_state_management/) , 2024-06-25-0910
```
Has anyone implemented a working streamlit app with LangGraph? I am having issues with state management between the two.
 If anyone has implemented the LangGraph tutorial chatbot in streamlit, please let me know
```
---

     
 
all -  [ Testing sales agent ](https://www.reddit.com/r/LangChain/comments/1dngjfm/testing_sales_agent/) , 2024-06-25-0910
```
Hey! Pretty new to this. I'm building a sales agent that can help with e.g. lead identification, enrichment, personalise
d outbound email messaging, updating our CRM. I want to test it pretty rigorously before we start using it. What is the 
best way to do something like automated regression testing for an agent, i.e. building a dataset of tasks with 'correct'
 answers where I can see how the agent performs after I make any changes? I could build this from scratch but I feel lik
e most of the tasks are fairly generic and was wondering if there are available datasets or how others have approached t
his problem 
```
---

     
 
all -  [ What's the best way to build AI Agents? LangChain or Semantic Kernel? ](https://www.reddit.com/r/build5nines/comments/1dnenml/whats_the_best_way_to_build_ai_agents_langchain/) , 2024-06-25-0910
```
As with all solutions, you should use the right tool for the job. However, when just starting out you can usually pick t
he tool for the job. Python is extremely popular in the AI / data science space, and C# is popular in the Microsoft worl
d. In your experience, do you think it's better to use [Python and LangChain to build AI Agents](https://build5nines.com
/introduction-to-building-ai-agents-with-langchain-and-python/), or use [C# and Microsoft Semantic Kernel to build AI Ag
ents](https://build5nines.com/introduction-to-building-ai-agents-with-microsoft-semantic-kernel/)?

I'm curious what you
r opinions and experiences are.

  

```
---

     
 
all -  [ Please help me pick a LLM model for my project(Angular+Dajngo+SQL Server) ](https://www.reddit.com/r/LangChain/comments/1dnb9ia/please_help_me_pick_a_llm_model_for_my/) , 2024-06-25-0910
```
Hello,

I have built an application at work which uses Angular, Django and SQL server. Currently all the user inputs are
 manual based meaning, either dropdown or text based inputs. Also, I provide recommendation in the project I want to int
egrate a LLM model so that I can automate the input module as well as recommendation one. Which one should i pick?  
Als
o, which LLM's community is more than active and engages in Q&A

Upvote1Downvote0comments0 awardsShare
```
---

     
 
all -  [ Need advice in Structuring JSON Output in Langgraph for Chatbot ](https://www.reddit.com/r/LangChain/comments/1dna58k/need_advice_in_structuring_json_output_in/) , 2024-06-25-0910
```
I’m working on a chatbot that interacts with an internal API, such as searching for items based on user queries. The out
put needs to be in a structured JSON format that I can pass to the front end. Here’s the desired structure:
  
```json
{

  'type': 'message',
  'message': 'Here is an item matching your search criteria',
  'data': [
    { 'item': 1, 'id': '
abc123' },
    { 'item': 2, 'id': 'def456' },
    ...
  ]
}
```

I’m struggling with extracting the assistant “message” 
and the item data (including the item ID) from the tools. I need to pass the data (e.g. item id) so then the front end c
an process it and display a custom view (card view) of items. My attempts to inject a Pydantic model and explicitly prom
pt to output a structured format haven’t been successful so far. 

I am thinking to set up a specific node at the end of
 the graph to parse the assistant’s output, but I found that the assistant keeps discarding item details such as item id
 (even after I explicitly prompt not to do so). Is there a better approach to achieve this? Any advice or insights would
 be greatly appreciated!
```
---

     
 
all -  [ Number of concurrent connections has exceeded your rate limit with Anthropic with Langchain ](https://www.reddit.com/r/LangChain/comments/1dn9ytb/number_of_concurrent_connections_has_exceeded/) , 2024-06-25-0910
```
I am using FastAPI with langchain I am using `aconvert_to_graph_documents` which Asynchronously convert a sequence of do
cuments into graph documents.  
  
I am not able to use Langchain's ChatAnthropic in async manner, I tried using semapho
re but keep getting   
anthropic.RateLimitError saying Number of concurrent connections has exceeded your rate limit.

I
s there no way set this to a reasonable number?
```
---

     
 
all -  [ Build RAG in 10 Lines of Code with Lyzr ](/r/AnyBodyCanAI/comments/1dn8338/build_rag_in_10_lines_of_code_with_lyzr/) , 2024-06-25-0910
```

```
---

     
 
all -  [ What strategies can we use to enhance LLM responses besides fine-tuning and prompt engineering? ](https://www.reddit.com/r/LangChain/comments/1dn7p4h/what_strategies_can_we_use_to_enhance_llm/) , 2024-06-25-0910
```
Aside from using better or larger models and employing fine-tuning, how else can we achieve improved responses from mode
ls?

p.s, I'm extremely new to this space, so any answers would be appreciated. 
```
---

     
 
all -  [ How do i parse tool calls? ](https://www.reddit.com/r/LangChain/comments/1dn6yaw/how_do_i_parse_tool_calls/) , 2024-06-25-0910
```
Here is the function I'm using to execute tool calls:

    def single_tool_parser(model_output):
        tool_map = {too
l.name: tool for tool in tools}
        chosen_tool = tool_map[model_output['name']]
        return itemgetter('argument
s') | chosen_tool

**Method 1:**

The above code works if i do something like this:

example\_chain = prompt | llm | Jso
nOutputParser() | single\_tool\_parser

res=example\_chain.invoke(..........)

print(res) //output of tool

**Method 2**


However if i try to do this:

example\_chain = prompt | llm | JsonOutputParser()

res=example\_chain.invoke(..........
)

res2=single \_tool\_parser(res)

Upon doing print(res2), here's what i get:

first=RunnableLambda(itemgetter('argumen
ts')) last=StructuredTool(name='mute', description='Mute an incoming call\\n    : param caller: The name of the caller t
o be muted', args\_schema=<class 'pydantic.v1.main.muteSchema'>, func=<function mute at 0x7f5b1403b380>)

How can i get 
method 2 to work?

Note: The tool I'm using is called 'mute'. I've also tried doing  res2=res | single\_tool\_parser, bu
t i get an error saying: unsupported operand type(s) for |: 'dict' and 'function'.

Im using Llama3 with Ollama
```
---

     
 
all -  [ Creating a Knowledge Graph from Chat History Using LangChain: Seeking Advice ](https://www.reddit.com/r/LangChain/comments/1dn55j1/creating_a_knowledge_graph_from_chat_history/) , 2024-06-25-0910
```
I've compiled a history of chats between a user and an AI assistant in JSON format. Here’s a snippet of how the chat dat
a looks:

    '2024-06-23': [
        {
            'role': 'user',
            'message': 'Hello! Can you suggest some 
tourist places to visit in Paris?',
            'time': '2024-06-23T15:30:00Z'
        },
        {
            'role': 
'assistant',
            'message': 'Hello! Paris is a beautiful city with many wonderful places to visit. Here are some
 top tourist attractions: ...',
            'time': '2024-06-23T15:32:00Z'
        }
    ]

I’m planning to create a det
ailed knowledge graph, and I'm debating between two approaches for structuring the documents: creating a document for ea
ch interaction or aggregating all interactions for each date into a single document. Currently, I lean towards the forme
r to capture more granularity in the analysis. Here’s how I’m setting up my documents using LangChain:

    from langcha
in.docstore.document import Document
    import json
    
    def load_conversations_from_json(file_path):
        docs 
= []
        
        with open(file_path, 'r', encoding='utf-8') as file:
            chat_data = json.load(file)
     
   
        for date, messages in chat_data.items():
            for message in messages:
                role = message
['role']
                text = message['message']
                time = message['time']
                
             
   # Create a document with the conversation
                metadata = {
                    'date': date,
            
        'time': time,
                    'role': role
                }
                docs.append(Document(page_conte
nt=text, metadata=metadata))
        
        return docs
    
    conversations = load_conversations_from_json('chat_hi
story.json')

I’m considering using `LLMGraphTransformer` from LangChain to convert these documents into graph documents
. Do you recommend creating a specific prompt for this task? Here’s a simple prompt I’m considering:

    from langchain
.prompts import ChatPromptTemplate
    
    kg_prompt = ChatPromptTemplate.from_template('''
    You are an AI that cons
tructs knowledge graphs from chat histories. 
    Your task is to identify key entities and the relationships between th
em based on the provided conversation. 
    
    Please proceed with the extraction based on the conversation provided.

    ''')

How beneficial is it to use the `allowed_nodes` and `allowed_relationships` parameters in `LLMGraphTransformer
`? Which model would you recommend for the LLM? Currently, I’m using `gpt-4o`.

I’d appreciate any advice or insights on
 optimizing this process for creating a comprehensive knowledge graph. Thank you!
```
---

     
 
all -  [ Python-LLM - Session 4 - LangChain - Multi Agent - Supervisor - Agent - Query Mutual Funds Data ](https://www.reddit.com/r/u_SravzLLC/comments/1dmxfue/pythonllm_session_4_langchain_multi_agent/) , 2024-06-25-0910
```
**# Use Case**

Use LangChain Multi Agent: Supervisor Agent (JSON & Pandas Agents) to Query Mutual Funds Data



**## Se
ssion 4**

- LangSmith - debug LangGraph.

- Relevant document search update - make the documents more relevant.

- Add 
code = filename to all the objects recursively

- Integrate AWS S3 with JSONSplitter.

- In JSON Agent remove tools not 
used by the graph, this will prevent looping

- Remove pandas agent and use Python REPL agent.

- LangChain pandas agent
 hard codes a data frame and forwards to python repl agent, instead of that just provide the python repl agent.

- Sampl
e Queries





Documentation Link: [https://docs.sravz.com/docs/tech/python/langchain/#session-4](https://docs.sravz.com
/docs/tech/python/langchain/#session-4)

Source Code: [https://gist.github.com/sravzpublic/534dbb3695180a5deca4df6cd0c11
8f4](https://gist.github.com/sravzpublic/534dbb3695180a5deca4df6cd0c118f4)

Video Explanation: [https://youtu.be/oJ0lk6c
dxos](https://youtu.be/oJ0lk6cdxos)



Sravz LLC Training Series:

Analytics - [https://docs.sravz.com/docs/analytics/](
https://docs.sravz.com/docs/analytics/)

Tech - [https://docs.sravz.com/docs/tech/](https://docs.sravz.com/docs/tech/)




#cpp #c++  #cors   #boost #beast  #http #cmake #make #python #langchain #openai #llm
```
---

     
 
all -  [ Langchain Textloader does not load all of the text ](https://www.reddit.com/r/LLMDevs/comments/1dmwhxk/langchain_textloader_does_not_load_all_of_the_text/) , 2024-06-25-0910
```
I've gotten so far with my programming, but this little issue is holding me back from moving on creating my open source 
LLM to chat with text files.  When I call Textloader like this, I only get to see 844 out of like 12000 words in the ori
ginal text file.  No funny characters in the text file, I checked.  Was going to go through the whole tokenizing, embedd
ing, vectorstore process...but...why the H\*\*\* can't the loader load the entire text?  Can someone please help a rooki
e out here?  I even did it in a shorter way just loading it in one line of code but i did this the longer way to see if 
there were any other issues :(.  

    with open('textfile.txt', 'rb') as f:
        rawdata = f.read()
    result = cha
rdet.detect(rawdata)
    encoding = result['encoding']
    
    loader = TextLoader('pdf1.txt', encoding=encoding)
    d
ocument = loader.load()
    
```
---

     
 
all -  [ Recommendation for re-ranker model on retrieved results?  ](https://www.reddit.com/r/LangChain/comments/1dmuxu9/recommendation_for_reranker_model_on_retrieved/) , 2024-06-25-0910
```
Looking for a cost effective approach that doesn’t suck
```
---

     
 
all -  [ Optimize and configure integration classes wit **kwargs ](https://www.reddit.com/r/LangChain/comments/1dmtf4a/optimize_and_configure_integration_classes_wit/) , 2024-06-25-0910
```
Although the plenty of integrations make our life easier if committed to langchain, it is disproportionally more difficu
lt to optimize and configure their paramaters and especially the \*\*kwargs. I understand that these usually refer to th
e underlying package that the langchain class wraps around.

All docs have vanilla params and when some further configur
ation is needed or even explored then things become a bit of a pain.

The only way so far to find what \*\*kwargs are av
ailable for the integrations I use is to go deep in the langchain code to see whether these might be finally passed, rea
d the wrapped package documentation and also do extensive google search as it is not just the kwargs but also the syntax
 to pass them on (eg dict).

I guess this is not a big deal for a seasoned developer, but is there an easier way to do t
his, especially in the LLM era?
```
---

     
 
all -  [ Looking for ideas: How to handle parallel tool calls in LangGraph? ](https://www.reddit.com/r/LangChain/comments/1dmtcyn/looking_for_ideas_how_to_handle_parallel_tool/) , 2024-06-25-0910
```
I'm looking for some high-level advice around **LangGraph** and was hoping that this community might have some creative 
ideas.

I've been playing with LangGraph and I love how it lets you control the flow of a conversation. But **I'm strugg
ling with how to design a graph in light of parallel tool calling**.

Background: So, let's say I have a state that repr
esents the first 'stage' of a dialogue with an Agent. Once that stage is complete, I want the dialogue to move to the se
cond stage. (Each stage is represented as a state.) I have a tool called 'CompleteOrEscalate' (based on the LangGraph tu
torials) that the LLM can use when it thinks that the task for stage 1 is complete. I also have a second tool called 'To
FAQ' which can be used if the user asks a question that is not directly related to stage 1's task. So, stage 1 can condi
tionally transition to two other stages/states, depending on what the user says. This works great, *most of the time*.


But an issue arises when a user says something that causes the LLM to invoke more than one tool (i.e. the LLM is suggest
ing that we make more than one transition out of a state). For example, if the purpose of stage 1 is to confirm the user
's name, and the user says, 'Yes, I'm John Smith. And I have a question about ...' That input both completes the task (c
onfirming the user's name) AND contains a question (requiring an FAQ response). So, with parallel tool calling enabled t
he LLM returns both tool calls (CompleteOrEscalate and ToFAQ). This is actually pretty cool, but I'm not sure how to han
dle this situation in the conditional transition?

I've considered turning off parallel tool calling. This would force t
he LLM to call only one tool at a time. But it seems like a waste of tokens/time not to allow the LLM to return *both/al
l* tool calls.

Am I thinking about this all wrong? Is there a better way to handle this situation? TIA for any suggesti
ons or thoughts you may have.


```
---

     
 
all -  [ How to Improve RAG Performance ](https://www.reddit.com/r/LangChain/comments/1dmo3am/how_to_improve_rag_performance/) , 2024-06-25-0910
```
Just started using RAG with LangChain the last couple of weeks for a project at work.

First pass, I used this tutorial:
 [https://python.langchain.com/v0.2/docs/tutorials/rag/](https://python.langchain.com/v0.2/docs/tutorials/rag/)

Instead
 of a webloader, I used a textloader to load a small text file, a help file for a custom software framework.

I ran it, 
queried the model, and it worked great. I was excited.

The full amount of data I want to reference is about 18K small t
ext documents, about 179MB. I decided to work up to that, and just used about 10MB in about 1000 text documents. Query r
esults were much worse.

In one specific case, I asked about a scenario description that was stored in a file called ea.
txt. For troubleshooting, I increased the number of docs to be retrieved to 5 and added logging to show which docs were 
being retrieved.

The answer was wrong, and ed.txt was referenced three times, along with two other irrelevant docs. In 
the directory to be loaded, ed.txt directly follows ea.txt. How is RAG determining which docs to retrieve? The scenario 
I was asking about started with 'ea' (e.g. 'scenario ea4003'). Why would it pass over the file with the correct informat
ion, which contains strings that are much more similar to what I'm asking about? 

And does anyone have any advice on ho
w to improve performance? Thanks.
```
---

     
 
all -  [ Milvus - Updating the Embeddings ](https://www.reddit.com/r/vectordatabase/comments/1dmnfob/milvus_updating_the_embeddings/) , 2024-06-25-0910
```
The RAG system reads a series of PDF files, via the langchain PyPDFDirectoryLoader and chunks the data for storage in th
e standalone docker version of Milvus (V2.41).

Some of the documents have a limited lifespan and therefore when the doc
ument expires, I would like to delete them from Milvus without recreating all the embeddings. There is metadata in the e
mbeddings, but I don’t think I can delete the embeddings based on metadata as it doesn’t contain the primary key. My mor
e general question is how do you update a Milvus vector store, or are there better choices for this type of application?
 Do I need to use a SQL database to store the metadata and the primary keys?


```
---

     
 
all -  [ LLM Structured Output Benchmarks: Find the best LLM structured data parsing framework for your task! ](https://i.redd.it/j7pv9d6qxb8d1.jpeg) , 2024-06-25-0910
```
Parsing structured data from LLMs can be frustrating for anything beyond toy problems. These are some real problems I've
 faced:

👨‍🏫 For Classification tasks, the LLM must strictly adhere to a list of allowed classes, which can be as many a
s tens to hundreds in real-world problems. With more than a handful of classes, LLMs start hallucinating classes that ar
e not allowed!

📬 For NER, the LLM should only pick entities explicitly present in the text. These entities might be in 
a 2- or 3-level deeply nested structure like User → Address → City. LLMs struggle to capture these deeply nested fields 
reliably and either miss them or hallucinate something that doesn't exist.

🛢️ For Synthetic Data Generation, you might 
require a 2- or 3-level deeply nested data structure, and the challenges are similar to NER mentioned above.

Thankfully
, some open-source frameworks aim to solve these challenges, but I've been getting mixed results from them on complex pr
oblems like those mentioned above.

Over the past few weekends, I've been building LLM Structured Output Benchmarks to e
asily compare multiple frameworks on any dataset. You can plug in your dataset, run a command, and the metrics will be g
enerated. Then you can pick the best framework for any given problem.

I've implemented 6 of the top frameworks in a mul
ti-label classification problem and measured how reliable the output of each framework is. The experiment methodology is
 to run each text row of the dataset through each framework ten times and log the success rates to simulate the real-wor
ld finickiness I've been encountering for this task: The same input can pass sometimes and fail some other times 😐

For 
the dataset I used, Mirascope, Fructose, and Outlines have a perfect 100% reliability out-of-the-box, while the others s
how a small percentage of error, as I've experienced in real tasks. Therefore, this metric is a good proxy for real-worl
d performance.

I plan to add more frameworks and tasks to this benchmark. If you find this benchmark helpful, please st
ar it on GitHub!

🌟 LLM Structured Output Benchmarks Github: https://github.com/stephenleo/llm-structured-output-benchma
rks

```
---

     
 
all -  [ Building a Python library to quickly create+search knowledge graphs for RAG -- want to contribute? ](https://www.reddit.com/r/LangChain/comments/1dmm13w/building_a_python_library_to_quickly_createsearch/) , 2024-06-25-0910
```
Knowledge graphs can improve your RAG accuracy if your documents contain interconnected concepts.

And you can create+se
arch on KGs for your existing documents automatically by using the latest version of the knowledge-graph-rag library.

A
ll in just 3 lines of code.

In this example, I use medical documents. Here's how the library works:

1. Extract entitie
s from the corpus (such as organs, diseases, therapies, etc)

2. Extract the relationships between them (such as mitigat
ion effect of therapies, accumulation of plaques, etc.)

3. Create a knowledge graph from these representations using GP
T 3.5 / Haiku

4. When a user sends a query, break it down into entities to be searched.

5. Search the KG and use the r
esults in the context of the LLM call.

Here’s the repo: [https://github.com/sarthakrastogi/graph-rag](https://github.co
m/sarthakrastogi/graph-rag)

If you'd like to contribute or have suggestions for features, please raise them on Github.
```
---

     
 
all -  [ I'm not sure I understand how to perform RAG on CSV files... ](https://www.reddit.com/r/LangChain/comments/1dmj7p7/im_not_sure_i_understand_how_to_perform_rag_on/) , 2024-06-25-0910
```
I'm looking to implement a way for the users of my platform to upload CSV files and pass them to various LMs to analyze.
 I get how the process works with other files types, and I've already set up a RAG pipeline for pdf files. 

However, wi
th PDF files I can 'simply' split it into chunks and generate embeddings with those (and later retrieve the most relevan
t ones), with CSV, since it's mostly data that could relate to each other, I'm not sure how to proceed.

For example, wh
ich criteria should I use to split the document into chunks? And what about the retrieval? Are embeddings relevant for C
SV files?

The main use case to RAG in this case -as compared to simply including the whole CSV as text in the prompt- i
s to save tokens, but is it possible to get decent results with RAG?

Thanks in advance
```
---

     
 
all -  [ What is ReAct Prompting? the most important piece in agentic frameworks ](https://www.reddit.com/gallery/1dmj2v9) , 2024-06-25-0910
```
“What is ReAct Prompting? the most important piece in agentic frameworks” - A quick read from Mastering LLM (Large Langu
age Model) 'Coffee Break Concepts' Vol.6

This document deeps dive into the ReAct Prompting method and why it's importan
t:
1. Limitations of LLM
2. Why ReAct prompting matters?
3. How ReAct Works?
4. LangChain Implementation
5. Why Prompt w
ithin agentic frameworks Matters?

Comment below on which topic you want to understand next in this 'Coffee Break Concep
ts' series and we will include those topics in upcoming weeks.
```
---

     
 
all -  [ Langchain chat history data structure in final prompt ](https://www.reddit.com/r/LangChain/comments/1dmeyfj/langchain_chat_history_data_structure_in_final/) , 2024-06-25-0910
```
I just find that chat history in final request look like that - 
`<CHAT HISTORY>
[HumanMessage(content='Message one'), A
IMessage(content='Hey'), HumanMessage(content='Message two')]
</CHAT HISTORY>`

i a bit confused, it how it should looks
, is it correct? 
As i remember i was something like this before: 
` AI:message \n USER:Text Message ` 

Can anyone clar
ify this for me?

P.S.: Does anyone have information on how models like OpenAI, Anthropic, or Gemini are trained to unde
rstand conversation history?

My research gives me this ideas:

```
  {
    'chat_history': [
      {'role': 'user', 'co
ntent': 'Message one'},
      {'role': 'ai', 'content': 'Hey'},
      {'role': 'user', 'content': 'Message two'}
    ]
 
 }
```

```
USER: Message one
AI: Hey
USER: Message two
```

```
<conversation>
  <user>Message one</user>
  <ai>Hey</ai
>
  <user>Message two</user>
</conversation>

```


Langchain use its own history structure for a  reason?



This is ho
w im execute it:
```

prompt = ChatPromptTemplate.from_template(self.prompt_template)

chain = prompt | self.selected_ll
m
self.llm_chain = RunnableWithMessageHistory(
	chain,
	self.get_session_history,
	input_messages_key='input',
	history_
messages_key='chat_history',
	history_factory_config=[
		ConfigurableFieldSpec(id='user_id', annotation=str),
		Configur
ableFieldSpec(id='session_type', annotation=str),
	],
)

response = await self.llm_chain.ainvoke(
                {'inpu
t': self.llm_input.content},
                config={
                    'configurable': {
                        'use
r_id': self.user_id,
                        'session_type': self.session_type,
                    },
                 
   'callbacks': [self.langfuse_handler],
                },
            )
```


_langchain = '^0.2.5'
langchain-core = '
^0.2.9'
langchain-community = '^0.2.5'_
```
---

     
 
all -  [ Using a chat interface to help people fill out a form ](https://www.reddit.com/r/LangChain/comments/1dmbnet/using_a_chat_interface_to_help_people_fill_out_a/) , 2024-06-25-0910
```
I'm new to LangChain and slowly working my way through the docs. My intention is to build a chat interface that has a co
nversation with a user and then slowly fills out a form behind the scenes as answers come in. 

Filling out the form dir
ectly is a lot of information upfront for the user whereas a chat interface lets me break the questions down into smalle
r chunks.

I'm trying to understand how I would use LangChain to do this. There are a lot of different moving parts to t
he framework and I was wondering if someone could point me in the right direction. That is, which modules I need to cove
r first or a relevant example of something similar.

Specific questions I have include:  
- How to keep costs down when 
polling the transcript to fill out the form. If i do this on every message submission it might get unnecessarily expensi
ve. But if I do it too infrequently then the bot might end up asking questions it already has the answer to. Was hoping 
the framework had some best practices I could rely on in this regard.  
- How to redirect the redirect the bot's focus b
ased on which questions still need answering.  
- How to implement a system to determine if an answer is good enough or 
if I need to ask more follow up questions to get a more substantial answer.  
- How to detect when all the questions hav
e been filled out so I can end the chat.

I'll slowly figuring it out but any pointers would be much appreciated. 

Also
, are there other LangChain specific forums where I can ask these types of questions that anyone recommends?
```
---

     
 
all -  [ Startup School: Gen AI ](https://www.reddit.com/r/googlecloud/comments/1dm9jjq/startup_school_gen_ai/) , 2024-06-25-0910
```
I'm taking the [Startup School: Gen AI by Google ](https://services.google.com/fh/files/emails/ssgenai_cloudskillsboost_
instructions.pdf)and  currently on week 3 labs.

I'm eager to start applying my knowledge to real-world problems, like t
raining an AI model with my own PDF documents. While the course videos have touched on this, the hands-on labs haven't a
ligned with these concepts until now. I'm hoping that the upcoming lab 'Creating a RAG Chat Assistant with MongoDB Atlas
 Vector Search, Google Cloud and Langchain' will finally demonstrate this process.

I'm curious why is there emphasis on
 MongoDB. Google Cloud offers a wide range of products, so I'm curious why we can't train Gemini AI using PDFs directly 
within Google's ecosystem. What is the specific advantage of incorporating a third-party product like MongoDB for this p
urpose?
```
---

     
 
all -  [ Since langchain gets alot of hate which are your libaraies for function calling agents and Rag ? ](https://www.reddit.com/r/LocalLLaMA/comments/1dm93r2/since_langchain_gets_alot_of_hate_which_are_your/) , 2024-06-25-0910
```
Like the title says I will be getting in to a project where i might need rather complex agents and I wanted to know whic
h frameworks are a good fit for that ? 
I heard alot of complaints about langchain so i wanted to know what is better ?
```
---

     
 
all -  [ confused on which llm framework to use ](https://www.reddit.com/r/learnmachinelearning/comments/1dm6n0q/confused_on_which_llm_framework_to_use/) , 2024-06-25-0910
```
Hello,

I'm a beginner in the field of LLMs and was struggling on what framework to pick. I am working on a small projec
t of mine wherein I scrape off soccer news articles and pass it through some LLM and ask it to generate a summary for me
. I realize to use some model I would need some sort of LLM framework and I have been looking into llamaindex. However, 
since I am a beginner I wanted to know which framework would be better for me to use ( llamaIndex or Langchain ) based o
n the criteria of my project. Thank you for your help.
```
---

     
 
all -  [ LinkedIn used Graph RAG to cut down their ticket resolution time from 40 hrs to 15 hrs. Let's make a ](https://www.reddit.com/r/LangChain/comments/1dlwc39/linkedin_used_graph_rag_to_cut_down_their_ticket/) , 2024-06-25-0910
```
So first, here's what I understand of how they did it:

They made the KG by parsing customer support tickets into struct
ured tree representations, preserving their internal relationships.

Tickets are linked based on contextual similarities
, dependencies, and references — all of these make up a comprehensive graph.

Each node in the KG is embedded so they ca
n do semantic search and retrieval.

The RAG QA system identifies relevant sub-graphs by doing traversal and searching b
y semantic similarity.

Then, it generates contextually aware answers from the KG, evaluating by MRR, which saw a signif
icant improvement.

Paper: [https://arxiv.org/pdf/2404.17723](https://arxiv.org/pdf/2404.17723)

If you’d like to implem
ent Graph RAG too, I’m creating a Python library which automatically creates this graph for the documents in your vector
db. It also makes it easy for you to retrieve relevant documents connected to the best matches.

If you're interested in
 contributing or have suggestions please raise them on Github.

Here’s the repo for the library: [https://github.com/sar
thakrastogi/graph-rag/tree/main](https://github.com/sarthakrastogi/graph-rag/tree/main)
```
---

     
 
all -  [ Career Change from Marketing to Analyst. Please review my resume and please give suggestions. ](https://www.reddit.com/r/resumes/comments/1dlv2al/career_change_from_marketing_to_analyst_please/) , 2024-06-25-0910
```
25F from India.

I am looking to transition from marketing to Analyst roles. There are a few reasons, one of them being 
that I do not enjoy the social media part of the job which is unavoidable in most of the marketing jobs. In my previous 
experience at a martech company, I got to work with the product team where I got to know more about the field of data(th
e product was a data pipeline) and I genuinely enjoyed working on data and creating reports and fetching insights.

I de
cided to leave and pursue a PG diploma in data science to get my foot in the door. I worked on few projects in ML, DL an
d NLP and really enjoyed working on it. Now I'm done with the course and looking for jobs in Data science/Analyst, Busin
ess analyst, ML engineer roles.

Would love suggestions from you guys. Thank

https://preview.redd.it/7sfx8d53f48d1.png?
width=1198&format=png&auto=webp&s=623771c0a12a2013c78b2ad7221f20b81fdc899a

https://preview.redd.it/p4oxai53f48d1.png?wi
dth=1198&format=png&auto=webp&s=19aeffcdd7a6de151f09cb46ec5d08b61accb4c8


```
---

     
 
all -  [ An article on why moving away from langchain ](https://www.reddit.com/r/LangChain/comments/1dlu5t9/an_article_on_why_moving_away_from_langchain/) , 2024-06-25-0910
```
As much as i like LangChain, there is some actual good points from this article 

https://www.octomind.dev/blog/why-we-n
o-longer-use-langchain-for-building-our-ai-agents

What you guys think ?
```
---

     
 
all -  [ How to stream messages with FastAPI and React? - LangGraph ](https://www.reddit.com/r/LangChain/comments/1dltljb/how_to_stream_messages_with_fastapi_and_react/) , 2024-06-25-0910
```
Hey guys!  
Has anyone tried and managed to find a successful solution, as to how I can messages in LangGraph through th
e usage of FastAPI and React?  
I have multiple nodes in my LangGraph app, and each one is appending a message to the 'm
essages' list attribute. I want these messages' content to be streamed as a single message in my React app, until I reac
h the END node.  
Does anyone have any idea as to how to do that?
```
---

     
 
all -  [ How to Use RabbitMQ or any other Broker with LangChain FastApi chatbot  ](https://www.reddit.com/r/LangChain/comments/1dlsxte/how_to_use_rabbitmq_or_any_other_broker_with/) , 2024-06-25-0910
```
. 
```
---

     
 
all -  [ What is the best python library for chatbot UIs? ](https://www.reddit.com/r/LangChain/comments/1dlrouj/what_is_the_best_python_library_for_chatbot_uis/) , 2024-06-25-0910
```
I know that streamlit was popular, but neither optimized for chatbot interactivity, nor ready to set up for production.


I assume some TypeScript + REACT is state of the art, but I am a Data Scientist and no frontend developer.

Are there a
ny new libraries that nicely integrate with LangGraph and also FastAPI?
```
---

     
 
all -  [ LangChain alternatives for a Next.js project? ](https://www.reddit.com/r/LangChain/comments/1dlolna/langchain_alternatives_for_a_nextjs_project/) , 2024-06-25-0910
```
I need to do RAG and web browsing. What other libraries can I use (except LangChain) that can achieve this functionality
?
```
---

     
 
all -  [ Benchmarking PDF models for parsing accuracy ](https://www.reddit.com/r/LangChain/comments/1dlfth6/benchmarking_pdf_models_for_parsing_accuracy/) , 2024-06-25-0910
```
Hi folks, I often see questions about which open source pdf model or APIs are best for extraction from PDF. We attempt t
o help people make data-driven decisions by comparing the various models on their private documents.

We benchmarked sev
eral PDF models - Marker, EasyOCR, Unstructured and OCRMyPDF.

Marker is better than the others in terms of accuracy. Ea
syOCR comes second, and OCRMyPDF is pretty close.

You can run these benchmarks on your documents using our code - https
://github.com/tensorlakeai/indexify-extractors/tree/main/pdf/benchmark

The benchmark tool is using Indexify behind the 
scenes - https://github.com/tensorlakeai/indexify

Indexify is a scalable unstructured data extraction engine for buildi
ng multi-stage inference pipelines. The pipelines can handle extraction from 1000s of documents in parallel when deploye
d in a real cluster on the cloud.

I would love your feedback on what models and document layouts to benchmark next. 

F
or some reason Reddit is marking this post as spam when I add pictures, so here is a link to the docs with some charts -
 https://docs.getindexify.ai/usecases/pdf_extraction/#extractor-performance-analysis
```
---

     
 
all -  [ Roast my resume! I'm in Canada and I've applied to 500+ positions but not heard anything ](https://i.redd.it/y0m8xn89uz7d1.png) , 2024-06-25-0910
```
I'm graduating next week. Applied to over 500 jobs with and without referrals. I don't get any call backs! 

I'm looking
 for anything in the Data Science/Machine Learning/AI development space 
```
---

     
 
all -  [ How does AI agent orchestration work in practice? ](https://www.reddit.com/r/learnmachinelearning/comments/1dlewks/how_does_ai_agent_orchestration_work_in_practice/) , 2024-06-25-0910
```
I recently read the following article which talks about using a 'boss' AI to orchestrate a collection of AI agents, and 
the idea of an AI agent that learns ones business model:

https://sifted.eu/articles/autonomous-companies-ai

Reality/hy
pe aside, I'm having trouble understanding how this sort of thing works in practice. Like, what does the code for this s
ort of thing *actually* look like? How do you train a model on such an abstract concept as 'business model'?

FWIW, I'm 
a hobby practitioner. I've played around with langchain and understand prompt chaining, but I'm still struggling to get 
from *here* to *there*.
```
---

     
 
all -  [ Leveraging NLP/Pre-Trained Models for Document Comparison and Deviation Detection ](https://www.reddit.com/r/LangChain/comments/1dldrbr/leveraging_nlppretrained_models_for_document/) , 2024-06-25-0910
```
How can we leverage an NLP model or Generative AI pre-trained model like ChatGPT or Llama2 to compare two documents, lik
e legal contracts or technical manuals, and find the deviation in the documents.

Please give me ideas or ways to achiev
e this or if you have any Youtube/Github links for the reference.

Thanks
```
---

     
 
all -  [ I built an SQL Agent with Langchain - Here's my experience ](https://www.reddit.com/r/LangChain/comments/1dlaqn7/i_built_an_sql_agent_with_langchain_heres_my/) , 2024-06-25-0910
```
My agent writes queries to retrieve data from Sqlite Databases. This was my first time writing an agent with a good and 
serious usecase. The first framework i used for this was Langchain. 

1. Very easy to implement: Its pretty convenient t
o import LLMs Gpt, Claude, Gemini. The documentation for it also clear.

2. Tools: This is my favourite part about the f
ramework, writing tools and importing them is very easy and it helps in building for a lot of usecases.

3. Documentatio
n can be improved since there are multiple versions and each time i click to the stable version, it goes back to the hom
epage.

https://i.redd.it/1b8v8xv4vy7d1.gif

Here's the [GITHUB LINK](https://github.com/ComposioHQ/composio/tree/master
/python/examples/sql_agent) if you want to try it out.
```
---

     
 
MachineLearning -  [ [P] Seeking Feedback on My GenAI Job Fit Project - New to LangChain/LangGraph ](https://www.reddit.com/r/MachineLearning/comments/1dgns9p/p_seeking_feedback_on_my_genai_job_fit_project/) , 2024-06-25-0910
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

     
 
MachineLearning -  [ [P] I'm tired of LangChain, so I made a simple open-source alternative with support for tool using a ](https://www.reddit.com/r/MachineLearning/comments/1deffo8/p_im_tired_of_langchain_so_i_made_a_simple/) , 2024-06-25-0910
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

     
 
MachineLearning -  [ [P] Superfast RAG: Langchain Streaming and Groq ](https://www.reddit.com/r/MachineLearning/comments/1d5s9g4/p_superfast_rag_langchain_streaming_and_groq/) , 2024-06-25-0910
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

     
 
deeplearning -  [ How to finetune? ](https://www.reddit.com/r/deeplearning/comments/1daio0h/how_to_finetune/) , 2024-06-25-0910
```
Can someone guide me to some resource how can I finetune an open source llm or some library (like langchain) on unstruct
ured data (example: news articles on cricket) So that model can answer a question (like When did India won world Cup?)
```
---

     
