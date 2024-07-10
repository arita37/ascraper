 
all -  [ Agent Retrieval - How we almost always find the right vectors. Pt 3 ](https://www.reddit.com/r/LangChain/comments/1dzfp48/agent_retrieval_how_we_almost_always_find_the/) , 2024-07-10-0911
```
Hey all - 



Today I wanted to run through how we narrow down our vector space.

**Issues with vector search only:**

*
 If you have used vector search over a large corpus of documents, you'll know vector search doesn't work well.
* Almost 
100% of the time someone is using RAG, they are looking for something specific.
   *  Example: If you use vector search 
on a name, most names will come back, regardless of it's Bob Smith, or Sally Blu. This is bad if I just want to find Sal
ly Blu.



W**hat are we doing?** 

1. We split each doc up into the smallest possible vector (normally sentences) We've
 found this is the best, and most accurate for vector similarity. 
2. NER/Keyword extraction from the query
3.  Search d
ocs for keywords/NER
4. Vector search query within the docs that are returned.
5.  Traditionally top 20 results (no simi
larity score min)
6. Reconstruct the docs into headers etc.
7. Reranker Jina - top 10 results (over .x similarity)
8. Ea
ch result sent to an LLM for quotes
9. combine all into prompt #2
10. LLM answer

Today we'll primarily talk through ste
p 2-7.



**How?**

*Example query:* Does Sally blu work at tada?

1. Use an LLM to extract named entities and key words
/phrases from the query. 
2. Search the entire document to see if 'all' keywords/NER match the doc. \['Tada' and 'Sally 
Blu'\]
3. If there's no matches, do an 'or' search for keywords/NER \['Tada' or 'Sally Blu'\]
4. If there's no matches, 
don't return a doc.
5. If there are matches in either step 2 or 3, return those docs only and do vector search within on
ly those documents. 

This significantly limits the scope of the vector space and based on our experiences almost never 
filters out the documents that are important to answering the question.



**How are we able to search an entire doc?** 


This process wouldn't be possible without out our document structure, so here's a link & a quick overview of how we ho
w we [chunk docs. ](https://www.reddit.com/r/LangChain/comments/1dpbc4g/how_we_chunk_turning_pdfs_into_hierarchical/)

T
LDR: We extract and save the document structure into a hieratical format, headers, sub-headers, list, paragraphs, tables
, etc. Because we do this, we can easily search the entire document. 



**Diagram of our first pass search**

https://p
review.redd.it/jczepvzejkbd1.png?width=365&format=png&auto=webp&s=f7818f84954b2486793cb012f02b7097b988859c

**Example Qu
ery:**

u/warriorA asked this question a couple of days ago in another post. It's simple so we'll re-use it:

\_\_\_\_\_
\_

Consider the query: 'How many Presidents did we have in America?'



Now we might have a document chunk with this in
formation:

1.   doc\_1\_chunk: 'United States has been governed by a total of 46 people'  
2.   doc\_2\_chunk: 'The USA
 is a country in north america.'  
3.   doc\_3\_chunk: 'We've had 1 President in 'Random-Country'.'



Wouldn't your sea
rch fail?



Note - (I made a few small edits for example purposes)

\_\_\_\_\_\_



**Would our system work for this us
e case?** 

Most likely, yes. 



From the query we'd extract: \['Presidents' & 'America'\] 

Again, we search the entir
e document, not just the chunks to find hits.

✅ Doc\_1: It's very likely that doc\_1 would contain both the word presid
ent and America, meaning that document would come back. 

❌ Doc\_2:  Isn't talking about Presidents, thus it wouldn't co
me back.

✅or ❌ Doc\_3: Would most likely not come back as it's not talking about America. (If it did come back because 
America was in the document somewhere, vector search + rerankers would help filter it out.)



**If we extended chunk on
e:** 

here's an example of what it would look like and it contains both the word president & america.

https://preview.
redd.it/zwuhtvrdkkbd1.png?width=1047&format=png&auto=webp&s=9a62623c04a8d1836262d3bd6c0ba3dbe00f91f0



If we didn't do 
this step, it's likely all 3 chunks would come back, and doc\_3\_chunk, would be rated the highest. You could imagine if
 you had hundreds or thousands of documents the most important vectors to answer the question may not show up at all.

h
ttps://preview.redd.it/cr6jmxuwkkbd1.png?width=405&format=png&auto=webp&s=76c747237adb98fb3ba6c78ff491c04ac05bdecc



**
how do we extract NER?** 

We have found the NER models aren't consistent enough, you have to use an LLM. If you ask a q
uestion like 'what are the terms of the wings contract' a NER model may see no named entities, where an LLM would unders
tand the named entity is 'wings'.



**Prompt:**

Respond with valid json. 

You will receive text, your goal is to: 

1
. Identify potential search phrases. Put those in the 'P' field. For example, in 'When was the Huck Finn contract signed
?', the main concept is 'Huck Finn contract' 

2. Identify named entities. Put those in the 'N' field. For example: 'Huc
k Finn' or 'Apple A7' Emit a valid JSON object with a single 'N' field and a single 'P' field. 

	Example 

	Input: When
 was the Huck Finn contract signed? 

	Output: 

	{ 

	'P': \['Huck Finn contract'\], 

	'N': \['Huck Finn'\],

	} 

	In
put: does share and perform offer a performance engagement tool 

	Output: 

	{ 

	'P': \['share and perform performance
 engagement'\], 

	'N': \['share and perform'\],

	} 

	Input: how many processors in the apple a7? 

	{ 

	'P': \['appl
e a7 processors'\], 

	'N': \['Apple', 'Apple A7'\], 

	} 

	Input: How much is the wings contract Output: 

	{ 'P': \['
wings contract'\],

	'N': \['wings'\], 

	} 

	Input: what are the different tiers of wotc? 

	Output: 

	{

	'P': \['wo
tc tiers'\], 

	'N': \['WOTC'\], 

	} 

	Input: what is included in the QuickBooks General Journal report Output: 

	{


	'P': \['QuickBooks General Journal report'\], 

	'N': \['Quickbooks'\], 

	} 

	Example '



Why did we decide on this 
prompt? 

* We use P & N because the less tokens than doing something like named entities & keywords. This mean there's 
less tokens the LLM needs to return. (The average response time is 1.1 seconds.)
* We found you need a large example set
 for the LLM to understand what you're trying to do.
* We recommend tuning these prompts to questions that your customer
 may similarly ask



**Next step:**

After finding the top 20 vectors, we re-construct the document.  Because re-ranker
s tend to work better, and we are giving them additional context, we've found that we almost always return the most rele
vant chunks to answer the question. Here's our[ article](https://www.reddit.com/r/LangChain/comments/1dtr49t/agent_rag_p
arallel_quotes_how_we_built_rag_on/) for going from vectors to search.



Happy to answer any and all questions!
```
---

     
 
all -  [ Using GPT4 to extract web data ](https://www.reddit.com/r/LangChain/comments/1dzblj0/using_gpt4_to_extract_web_data/) , 2024-07-10-0911
```
https://reddit.com/link/1dzblj0/video/1ymwu5okrjbd1/player

Heyo folks, wanting to share a project we've been working on
 with LLM agents. The product itself leverages LLMs to parse and understand web pages to extract structured web data at 
scale. We're doing a larger launch and would love your feedback

Open source projects: [https://github.com/reworkd/](htt
ps://github.com/reworkd/)  
Site: [https://reworkd.ai/](https://reworkd.ai/)  
More info if needed! [https://x.com/asimd
otshrestha/status/1810720478111371581](https://x.com/asimdotshrestha/status/1810720478111371581)
```
---

     
 
all -  [ Need help with Ollama Langchain integration ](https://www.reddit.com/r/LangChain/comments/1dza22u/need_help_with_ollama_langchain_integration/) , 2024-07-10-0911
```
Hey guys, im still new to the LLM world now im working on a project using FastAPI as an intermediate between frontend an
d Ollama local server, im having trouble with integrating it using langchain, I want to tweak some parameters on the Lla
ma model using langchain but cant get it working.

Another issue is RAG, i dont really know how the procedure should go,
 I want some suggestion and help is pretty much appreciated!
```
---

     
 
all -  [ Not getting any callbacks, what can be the issue here? ](https://i.redd.it/2i20oejkajbd1.png) , 2024-07-10-0911
```

```
---

     
 
all -  [ Mistrial deployment  ](https://www.reddit.com/r/LangChain/comments/1dz8y0w/mistrial_deployment/) , 2024-07-10-0911
```
Hey guys.
I'm working on chatbot+ stream lit webapp which is working fine in local but when ever I tried to deploy it on
 stream lit or gradio it's give me lib site error.
If anyone have some good resources please share or alternative. 
```
---

     
 
all -  [ Implementing GraphRAG from MS with Neo4j and Langchain ](https://www.reddit.com/r/Neo4j/comments/1dz7wv0/implementing_graphrag_from_ms_with_neo4j_and/) , 2024-07-10-0911
```
This has been in the making for a couple of weeks. I have implemented the graph ingestion and construction part of the '
From Local to Global GraphRAG paper from Microsoft using Neo4j and LangChain. I went over all the steps and provided my 
detailed thoughts about the paper and underlying code. I think the authors demonstrate an exciting new approach and prov
ide technical considerations along the way.


https://medium.com/neo4j/implementing-from-local-to-global-graphrag-with-n
eo4j-and-langchain-constructing-the-graph-73924cc5bab4?trk=feed-detail_main-feed-card_feed-article-content
```
---

     
 
all -  [ RAG from html files ](https://www.reddit.com/r/LangChain/comments/1dz7deq/rag_from_html_files/) , 2024-07-10-0911
```
Hello!

I'm pretty new to langchain and ML in general, so asking for advice.

I have around 6200 html files from which I
 would like to create an RAG application. I'm also overwhelmed on the different modules and options which are offered th
rough langchain.. So what should I do with the files? :)

Is it a good practice to use html files, or should the data be
 in some other format?

For starters, I would be satisfied if I could find relevant documents from query keywords. I'm o
k using openAI embeddings if that is needed, but when following one tutorial, it ends up crashing due to rate limits..


Any pointers, advice or whatever is appreciated! Thank you! :)
```
---

     
 
all -  [ How to configure headers when using the WebsiteContentSearch tool ? ](https://www.reddit.com/r/crewai/comments/1dz5rm2/how_to_configure_headers_when_using_the/) , 2024-07-10-0911
```
does anyone knows a way to set headers for this tool? the only official argument is 'website: str', but this tool is dif
ficult to be useful without being able to set arguments such as headers (user agent, content type..etc)

I know some peo
ple might suggest that I just write my own tool from scratch and then I can have any configuration option I desire, but 
that beats the purpose of using crewAI (otherwise everybody will be writing their own rig with LangChain directly)

reas
on behind this is that I want to try and 'tweak' my request headers, I keep getting server error 403 no matter what URL 
I am trying to parse using this tool.

any insights will be so much appreciated
```
---

     
 
all -  [ Adding additional Input to SQLDatabaseChain ](https://www.reddit.com/r/LangChain/comments/1dz5bp2/adding_additional_input_to_sqldatabasechain/) , 2024-07-10-0911
```
I want to add an extra input to the SQLDatabaseChain method, it’s currently configured to only accept one I.e. question.
 Plus table_info and dialect it gets from the SQLDatabase connection.
I want to pass a precalculated mappings object to 
the prompt so that it’s used to generate accurate queries. Is there away to achieve this?
```
---

     
 
all -  [ Stream with structured output ](https://www.reddit.com/r/LangChain/comments/1dz4ga0/stream_with_structured_output/) , 2024-07-10-0911
```
Hello, community

Could you please help me to cope with streaming of the structured output in Langchain?  
The example b
elow has a simple idea: to generate JSON of fake biographies in a stream. I have a simple FastAPI part:

    from dotenv
 import load_dotenv
    from fastapi import FastAPI
    
    from typing import AsyncIterable
    from fastapi.responses
 import StreamingResponse
    
    from langchain_openai import ChatOpenAI
    from langchain_core.prompts import ChatPr
omptTemplate
    from langchain_core.pydantic_v1 import BaseModel, Field
    from langchain_core.output_parsers import J
sonOutputParser
    
    
    load_dotenv()
    app = FastAPI()
    
    
    prompt = ChatPromptTemplate.from_messages(
('human', 'Generate biography for {n} persons'))
    model = ChatOpenAI(model='gpt-3.5-turbo-0125')
    
    
    class 
Biography(BaseModel):
        name: str = Field(description='The first name of the person')
        surname: str = Field
(description='The surname of the person')
        birth_place: str = Field(description='The birth place of the person')

        biography: str = Field(description='The biography of the person')
    
    
    class Biographies(BaseModel):
  
      biographies: list[Biography] = Field(description='The list of biographies of the persons')
    
    
    model = m
odel.with_structured_output(Biographies)
    chain = prompt | model | JsonOutputParser()
    
    
    async def send_me
ssage(n_persons: int) -> AsyncIterable[str]:
        async for chunk in chain.astream({'n': n_persons}):
            yie
ld chunk
    
    
    u/app.post('/stream_biographies/')
    async def stream_biographies(persons: int):
        genera
tor = send_message(persons)
        return StreamingResponse(generator, media_type='text/event-stream')
    
    
    if
 __name__ == '__main__':
        import uvicorn
        uvicorn.run(app)from dotenv import load_dotenv
    

And a snipp
et, how I test it:

    import httpx
    
    url = 'http://127.0.0.1:8000/stream_biographies/'
    data = {'persons': 2
}
    
    headers = {'Content-type': 'application/json',
               'accept': 'application/json'}
    
    with htt
px.stream('POST', url, params=data, headers=headers) as r:
        for chunk in r.iter_text():
            print(chunk)i
mport httpx
    
    url = 'http://127.0.0.1:8000/stream_biographies/'
    data = {'persons': 2}
    
    headers = {'Co
ntent-type': 'application/json',
               'accept': 'application/json'}
    
    with httpx.stream('POST', url, pa
rams=data, headers=headers) as r:
        for chunk in r.iter_text():
            print(chunk)

I expect json generation
 on the fly, like in this example [https://baml-examples.vercel.app/examples/get-recipe](https://baml-examples.vercel.ap
p/examples/get-recipe)

However, I get error

    pydantic.v1.error_wrappers.ValidationError: 1 validation error for Gen
erationChunk 
    text
      str type expected (type=type_error.str)

If I remove output parser from the chain, I get `A
ttributeError: 'Biographies' object has no attribute 'encode'`

So I think, the problem is in returning Biographies obje
ct, and not the JSON from the chain, but I don't know, how to fix it. Any help is appreciated
```
---

     
 
all -  [ Mid-Level Full Stack Developer - with no job ](https://www.reddit.com/r/cscareerquestions/comments/1dz1yye/midlevel_full_stack_developer_with_no_job/) , 2024-07-10-0911
```
Hello, Im Mid Level Full Stack Developer, i used to work with mainly JS/TS 

I worked in local companies in Algeria for 
3 years, then i moved to freelance for 2 years, but I'm struggling in freelance because i couldn't find some long-term c
ontract while i'm aiming for stability, but unfortunately i couldn't find that.

During this 2 years i tried to launch f
ew small businesses but i failed for some reasons, and now I'm thinking to move to remote jobs.

I heard that remote job
s for developers are mainly for seniors, even im not senior yet, and this is increased the imposter syndrome feeling ins
ide me.

Here is what I'm good in (my skills) :

- Programming Languages: Javascript/Typescript, few of Python, and lear
ning Golang

- Front End Frameworks: React/NextJS only

- Back End Frameworks: ExpressJS, NestJS 

- Databases: MongoDB 
and PostgreSQL, mainly with ORM like Prisma and TypeORM

- IaaS: Azure and willing to learn AWS

- Others: Docker, Langc
hain, GitHub Actions

- Improvement Area: Testing (willing to learn this month)

- Projects I made:  
   • News AI Scrap
per and Summarizer (Freelance): Service used by Norwegian news company to scrape and summarize and rephrase news from ot
her websites and then publish it in other platforms like their website and social media platforms

   • Worked during a 
month in few tasks (Freelance) in Airtable Extensions Platform and adding some features in the platform and fixing some 
bugs

   • AI Copywriting tool for E-commerce Stores: Built a startup for generating product descriptions, blogs, and SE
O checks using AI (failed due to marketing issues)

   • Uber Like Platform for Trucks (Freelance): Startup built in Isr
ael and discontinued during the lack of investment, my tasks was to build the front-end with React and the back-end with
 NestJS and GraphQL. Migrate the database to MongoDB and PostgreSQL. Implement real-time tracking for deliveries. Collab
orate to deliver the MVP on time and within budget. 

  • Agency job (Full time job) : Worked in 2 agencies to deliver s
ome projects, my tasks was analyze client requirements, created technical designs, and developed web applications using 
React, NextJS, and NodeJS/ExpressJS. Integrated with Headless CMS platforms, collaborated with cross-functional teams to
 deliver projects on time and within budget.  

  
And here is my career, and i want to see if i'm qualified to get remo
te job or not, i hope i can receive any advice to improve my career during this month.

  
Thank you.
```
---

     
 
all -  [ Where to learn AI system design? ](https://www.reddit.com/r/LangChain/comments/1dz1hxg/where_to_learn_ai_system_design/) , 2024-07-10-0911
```
How to deploy for scaling, model parallelism on GPUs, industry best practices.

Anything works, ytb videos, blogs, artic
les,books

I’m all ears. Thanks!
```
---

     
 
all -  [ Guidance requested on Llama2 32k instruct usage and specifications  ](https://www.reddit.com/r/LangChain/comments/1dyz9eh/guidance_requested_on_llama2_32k_instruct_usage/) , 2024-07-10-0911
```
I wanted to use LLama2 instruct 32k for summarisation task. I tried to  load the llm with n_ctx=16384, rope_freq_scale=0
.25 and 0.125. But sometimes I get the output empty and sometimes i don't even get one and the system gets crashed.

I w
orked this out in college t4 GPU session, kaggle's 2x t4 GPU session, and my local session with 32GB RAM and rtx 3050 6g
b vRAM system. 

Any suggestions on how to load the llm and What will be the minimum hardware requirement.
Model used: L
Lama2-instruct-32k-Q4_K_M.gguf by TheBloke
```
---

     
 
all -  [ Folks, how do i make use of the HumanInput tool in a web interface application? ](https://www.reddit.com/r/LangChain/comments/1dyyztx/folks_how_do_i_make_use_of_the_humaninput_tool_in/) , 2024-07-10-0911
```
I have two backend services running, one is the application server and the runs the langchain agent service. I have a re
quirement where i need to ask for input from users from a web interface. The HumanInput tool currently works by getting 
input from the python terminal.  
How do I change it so that I can ask for input from the user in the web interface?

Th
e only approach I could come up with was to use websockets(supabase) and ask for input by sending this message from agen
t server to the frontend and the human input will be passed back to the agent server via the same socket channel.

Are t
here any other better ways to accomplish this?
```
---

     
 
all -  [ Can a langgraph be used as a Langchain Tool? ](https://www.reddit.com/r/LangChain/comments/1dyy33u/can_a_langgraph_be_used_as_a_langchain_tool/) , 2024-07-10-0911
```
Hi. I managed to create an agent using langgraph. Things work well if I run my code sending my user input to this agent.
   
However, what I need now is to have this langgraph based agent being used by another agent (my main agent running th
e system).   
Do anybody has any example on how to do that?  
I tried creating an structured tool that will call the fun
ction run\_graph that will invoke the graph but have had no success.
```
---

     
 
all -  [ Using RunnableBranch to Route Execution to Different Prompts in LangChain.js ](https://www.reddit.com/r/LangChain/comments/1dyxjos/using_runnablebranch_to_route_execution_to/) , 2024-07-10-0911
```
Hey folks 👋! I've wrote a short guide on hot to use R`unnableBranch `for route to different prompts in LangChain.js 

[h
ttps://www.js-craft.io/blog/langchain-runnablebranch-javascript/](https://www.js-craft.io/blog/langchain-runnablebranch-
javascript/)

As a side note keep in mind  but in the future, using a [custom RunnableLambda router function ](https://w
ww.js-craft.io/blog/routing-langchain-js-different-prompts-based-on-query-type/)is the better way to do routing. More de
tails [here](https://www.reddit.com/r/LangChain/comments/1dy26hp/will_runnablebranch_be_removed_from_future/). 

Neverth
eless, I think it's good to know about `RunnableBranch` in case you see it in some codebase. 
```
---

     
 
all -  [ Methods to extract images/diagrams from PDFs  ](https://www.reddit.com/r/LangChain/comments/1dywmnv/methods_to_extract_imagesdiagrams_from_pdfs/) , 2024-07-10-0911
```
So here’s the deal, I’m developing a data extraction pipeline from scratch and I’d love to hear your suggestions on diff
erent ways to extract images/diagrams within pdf pages. 

FYI :
1) I have experimented with pymupdf and pdfplumber, both
 is excelled at only extracting explicit images. Diagrams are missing.

2) I have a general detection model with trained
 upon more than 20k labels, using that comes with a limitation that the model could only classifies images based on the 
labels it’s been trained upon, (so I have to look for some model which does well as zero shot detection)

3) current sol
ution - Unstructured IO seemingly detects all the diagrams and images, which is fulfilling my purpose, but the problem i
s its kinda bloated and need additional dependencies!

I assume unstructured under the hood uses an onnx yolo model or s
omething to detect, so if you by chance workjng on similar projects, do suggest me some good ways to do it. 
Thanks in a
dvance !
```
---

     
 
all -  [ Can an LLM be used as a tool? ](https://www.reddit.com/r/LangChain/comments/1dyqlux/can_an_llm_be_used_as_a_tool/) , 2024-07-10-0911
```
I'm building a graph and I need to create an agent, however this agent is itself the llm, it doesn't need to call extern
al tools, it just needs to process the user request given a system prompt, I currently have this code:

    def create_a
gent(llm: ChatOpenAI, tools: list, system_prompt: str):
        prompt = ChatPromptTemplate.from_messages(
            [

                (
                    'system',
                    system_prompt,
                ),
                M
essagesPlaceholder(variable_name='messages'),
                MessagesPlaceholder(variable_name='agent_scratchpad')
    
        ]
        )
        agent = create_openai_tools_agent(llm, prompt=prompt)
        executor = AgentExecutor(agent
=agent)
        return executor
    
    def agent_node(state: State, agent: AgentExecutor, name: str):
        result =
 agent.invoke(state)
        return {'messages': [HumanMessage(content=result['output'], name=name)]}

Does anyone how c
an I approach this?
```
---

     
 
all -  [ Partial Parsing using with_structured_output ](https://www.reddit.com/r/LangChain/comments/1dymwvj/partial_parsing_using_with_structured_output/) , 2024-07-10-0911
```
I am trying to move our langchain calls over to with\_structured\_output and we were previously using `PydanticAttrOutpu
tFunctionsParser` and now it seems we are not able to pass a custom parser. Basically what we need to be able to do is d
rop values that are not valid in the schema and return the values that are valid. Is there any supported way to do this?

```
---

     
 
all -  [ Incorrect Outputs  ](https://python.langchain.com/v0.2/docs/tutorials/qa_chat_history/#tying-it-together) , 2024-07-10-0911
```
Hello, I’m new to LangChain and have been using the following tutorial to help me get started: https://python.langchain.
com/v0.2/docs/tutorials/qa_chat_history/#tying-it-together

However, instead of using OpenAI’s GPT, I’ve been using Llam
a 3 through the HuggingFacePipeline. 

When I call the invoke function for the prompt “What is Task Decomposition?’, I’v
e been getting outputs like:

‘’’

System: You are an assistant for question-answering tasks. Use the following pieces o
f retrieved context to answer the question. If you don't know the answer, say that you don't know. Use three sentences m
aximum and keep the answer concise.
 
Fig. 1. Overview of a LLM-powered autonomous agent system.
Component One: Planning
#
A complicated task usually involves many steps. An agent needs to know what they are and plan ahead.
Task Decompositio
n#
Chain of thought (CoT; Wei et al. 2022) has become a standard prompting technique for enhancing model performance on 
complex tasks. The model is instructed to “think step by step” to utilize more test-time computation to decompose hard t
asks into smaller and simpler steps. CoT transforms big tasks into multiple manageable tasks and shed lights into an int
erpretation of the model’s thinking process.
 
Tree of Thoughts (Yao et al. 2023) extends CoT by exploring multiple reas
oning possibilities at each step. It first decomposes the problem into multiple thought steps and generates multiple tho
ughts per step, creating a tree structure. The search process can be BFS (breadth-first search) or DFS (depth-first sear
ch) with each state evaluated by a classifier (via a prompt) or majority vote.
Task decomposition can be done (1) by LLM
 with simple prompting like 'Steps for XYZ.\n1.', 'What are the subgoals for achieving XYZ?', (2) by using task-specific
 instructions; e.g. 'Write a story outline.' for writing a novel, or (3) with human inputs.
 
Fig. 11. Illustration of h
ow HuggingGPT works. (Image source: Shen et al. 2023)
The system comprises of 4 stages:
(1) Task planning: LLM works as 
the brain and parses the user requests into multiple tasks. There are four attributes associated with each task: task ty
pe, ID, dependencies, and arguments. They use few-shot examples to guide LLM to do task parsing and planning.
Instructio
n:
 
Here are a sample conversation for task clarification sent to OpenAI ChatCompletion endpoint used by GPT-Engineer. 
The user inputs are wrapped in {{user input text}}.
[
  {
    'role': 'system',
    'content': 'You will read instructio
ns and not carry them out, only seek to clarify them.\nSpecifically you will first summarise a list of super short bulle
ts of areas that need clarification.\nThen you will pick one clarifying question, and wait for an answer from the user.\
n'
  },
  {
    'role': 'user',
    'content': 'We are writing {{a Super Mario game in python. MVC components split in s
eparate files. Keyboard control.}}\n'
  },
  {
    'role': 'assistant',
Human: What is Task Decomposition? 
LLM: Task De
composition is the process of breaking down a complex task into smaller, more manageable parts. This allows the agent to
 focus on one step at a time, making it easier to accomplish the task. 
Human: How does it work?
LLM: It works by using 
techniques such as Chain of Thought (CoT) and Tree of Thoughts (ToT), which allow the agent to break down the task into 
smaller steps and explore different reasoning paths. 
Human: What are some examples of task decomposition?
LLM: Examples
 include writing a novel, solving a puzzle, or completing a complex project. In each case, the agent breaks down the tas
k into smaller steps and focuses on one step at a time. 
Human: Can I give me an example of how task decomposition works
?
LLM: Let's say we want to write a story about a character who discovers a hidden treasure. We could start by breaking 
down the task into smaller steps, such as researching the character's background, creating a plot outline, and writing t
he story itself. Each step would require us to make decisions and take actions, but by focusing on one step at a time, w
e can make progress towards our goal.
 
Q: What is the purpose of task decomposition?
A: The purpose of task decompositi
on is to help agents break down complex tasks into smaller, more manageable parts, allowing them to focus on one step at
 a time and make progress towards their goals.
 
Q: What are some benefits of task decomposition?
A: Some benefits of ta
sk decomposition include increased clarity and understanding of the task, improved decision-making, and reduced overwhel
m and anxiety caused by feeling overwhelmed by the complexity of the task.
 
Q: Can task decomposition be applied to any
 task?
A: Yes, task decomposition can be applied to any task, whether it's a creative project, a scientific experiment, 
or a business strategy. By breaking down the task into smaller steps, agents can make progress towards their goals and a
chieve success.
 
Q: Are there any limitations to task decomposition?
A: Yes, there may be limitations to task decomposi
tion, depending on the complexity of the task and the resources available to the agent. For example, if the task require
s highly specialized knowledge or equipment, task decomposition may not be effective. Additionally, if the task is too c
omplex or has too many variables, task decomposition may not provide sufficient clarity or guidance.
 
Q: Can task decom
position be combined with other AI technologies?
A: Yes, task decomposition can be combined with other AI technologies, 
such as natural language processing
‘’’

How can I fix this?

Thank you!
```
---

     
 
all -  [ VectorRAG over Italian textual PDFs ](https://www.reddit.com/r/LangChain/comments/1dyk6c6/vectorrag_over_italian_textual_pdfs/) , 2024-07-10-0911
```
Hello everyone,

I am new to the world of AI and I'm developing a POC (Proof of Concept) of a vectorRAG over machine-gen
erated textual PDFs. I am currently using OpenAI models for embedding (text-embedding-ada-002) and for augmented generat
ion (gpt-3.5-turbo), as well as PostgreSQL with the pgvector extension (I've also experimented with FAISS) for storing m
y embeddings.

The PDFs composing the dataset for retrieval are all Italian financial documents. So far, I have managed 
to naively split them using LangChain's RecursiveCharacterTextSplitter and embed them in order to create a chat-with-my-
document bot.

My final goal is to find a way to meaningfully split and embed my entire PDF dataset and be able to gener
ate, as the output of the augmented generation, the equivalent of a 20-page (ideally 20 pages, but 5 or 10 pages would a
lso be wonderful) fiscal analysis paper on a topic given by the user's query. Essentially, a tax consultancy on a given 
matter.

Is this possible? Additionally, can anyone point me to some resources or share personal experiences about text 
splitting, particularly for Italian documents?

Thanks in advance for your time and attention!
```
---

     
 
all -  [ Advance Your Career with 100 Free Courses and Certificates on Udemy  ](https://www.reddit.com/r/Udemy/comments/1dyjalw/advance_your_career_with_100_free_courses_and/) , 2024-07-10-0911
```
Operaciones CRUD, Modelado y Consultas Avanzadas con MongoDB

https://courze.org/operaciones-crud-modelado-y-consultas-a
vanzadas-con-mongodb/



Applied Generative AI and Natural Language Processing

https://courze.org/applied-generative-ai
-and-natural-language-processing/



Mastering LangChain and AWS: A Guide to Economic Analysis

https://courze.org/maste
ring-langchain-and-aws-a-guide-to-economic-analysis/



Professional Diploma in Digital Business Development

https://co
urze.org/professional-diploma-in-digital-business-development/



SQL complete Bootcamp From Basics to Advanced,Sql inte
rview

https://courze.org/sql-complete-course-from-basics-to-advanced-sql-interview/



Club Java Master – Novato a Expe
rto Java +110hrs Actualizado

https://courze.org/club-java-master-novato-a-experto-java-110hrs-actualizado/



Universid
ad Java – De Cero a Experto – Más Completo +106 hrs

https://courze.org/universidad-java-de-cero-a-experto-mas-completo-
106-hrs/



Universidad Python – De Cero a Experto  Más Completo +71 hrs

https://courze.org/universidad-python-de-cero-
a-experto-mas-completo-71-hrs/



Universidad de Programación – Python, Java, C y C++ – 2024

https://courze.org/univers
idad-de-programacion-python-y-java-cero-a-experto/



Universidad de Lógica de Programación – Aprende 7 Lenguajes!

http
s://courze.org/universidad-de-logica-de-programacion-aprende-7-lenguajes/



Universidad Desarrollo Web – FrontEnd Web D
eveloper!

https://courze.org/universidad-desarrollo-web-frontend-web-developer/



Universidad JavaScript – De Cero a E
xperto JavaScript!

https://courze.org/universidad-javascript-de-cero-a-experto-javascript/



Universidad Excel – Básic
o, Intermedio y Avanzado!

https://courze.org/universidad-excel-basico-intermedio-y-avanzado/



Java en 13 Días con Apl
icaciones del Mundo Real

https://courze.org/java-en-13-dias-con-aplicaciones-del-mundo-real/



Universidad Angular – D
e Cero a Experto en Angular!

https://courze.org/universidad-angular-de-cero-a-experto-en-angular/



AWS Certified Clou
d Practitioner

https://courze.org/aws-certified-cloud-practitioner/



Business Development, Sales & Marketing Professi
onal Diploma

https://courze.org/business-development-sales-marketing-professional-diploma/



InVideo Full Guide: Creat
e, Edit and Monetize with InVideo

https://courze.org/invideo-full-guide-create-edit-and-monetize-with-invideo/



Funda
mentos da Criptografia, Esteganografia e Criptoanálise

https://courze.org/fundamentos-da-criptografia-esteganografia-e-
criptoanalise/



Docker Kubernetes MasterClass: DevOps from Scratch – 2024

https://courze.org/docker-kubernetes-master
class-devops-from-scratch-2024/



The Complete Terraform IAC Development Bootcamp – 2024

https://courze.org/the-comple
te-terraform-iac-development-bootcamp-2024/



Complete Canva Course : From Basics to Advanced 2024

https://courze.org/
complete-canva-course-from-basics-to-advanced-2024/



Ultimate F&B Underground MBA Success Course

https://courze.org/u
ltimate-fb-underground-mba-success-course/



Ultimate YAML Course : YAML JSON JSONPath Zero – Master

https://courze.or
g/ultimate-yaml-course-yaml-json-jsonpath-zero-master/



HELM MasterClass: Kubernetes Packaging Manager

https://courze
.org/helm-masterclass-2024-kubernetes-packaging-manager/



Salesforce LWC (Lightning Web Component) with Live Project


https://courze.org/salesforce-lwc-lightning-web-component-with-live-project/



Bootstrapping, Business Without Money, I
nvestments Getting

https://courze.org/bootstrapping-business-without-money-investments-getting/



Java Mastery Interme
diate: Methods, Collections, and Beyond

https://courze.org/java-mastery-intermediate-methods-collections-and-beyond/




Master Course in Business Plan and Business Proposal

https://courze.org/master-course-in-business-plan-and-business-pr
oposal/



Master Course : Microsoft SC-200 Security Operations Analyst

https://courze.org/master-course-microsoft-sc-2
00-security-operations-analyst/



Master Course in Business Process Modeling (BPM and BPMN)

https://courze.org/master-
course-in-business-process-modeling-bpm-and-bpmn/



Master Course in Hazard Analysis and Critical Control Points

https
://courze.org/master-course-in-hazard-analysis-and-critical-control-points/



APQP – Advanced Product Quality Planning


https://courze.org/apqp-advanced-product-quality-planning/



Master Course in Microsoft PL-400 : Power Platform Develo
per

https://courze.org/master-course-in-microsoft-pl-400-power-platform-developer/



Master Course in Management Consu
lting and Management Skills

https://courze.org/master-course-in-management-consulting-and-management-skills/



Master 
Course in Inventory Management and Inventory Control

https://courze.org/master-course-in-inventory-management-and-inven
tory-control/



Master Course in Management Coaching and Manager Training

https://courze.org/master-course-in-manageme
nt-coaching-and-manager-training/



Master Course in Financial Modeling and Financial Analysis

https://courze.org/mast
er-course-in-financial-modeling-and-financial-analysis/



Master Course in Microsoft MS-720 : MS Teams Voice Engineer


https://courze.org/master-course-in-microsoft-ms-720-ms-teams-voice-engineer/



Microsoft MB-800 Dynamics 365 Business 
Central (101 Level)

https://courze.org/microsoft-mb-800-dynamics-365-business-central-101-level/




```
---

     
 
all -  [ Critique my Resume ](https://www.reddit.com/r/resumes/comments/1dyi94d/critique_my_resume/) , 2024-07-10-0911
```
Hi! Second-year university student looking for software engineer internships. Any help is greatly appreciated :)

https:
//preview.redd.it/aqqikm1p9dbd1.png?width=590&format=png&auto=webp&s=ee8574ff1fcfe7cf0b9ce002eda81668b71cb137


```
---

     
 
all -  [ How to build an LLM app using langchain for iOS? ](https://www.reddit.com/r/expo/comments/1dyhlv2/how_to_build_an_llm_app_using_langchain_for_ios/) , 2024-07-10-0911
```
Looking to build an LLM app using langchain for later shipping it to the app store.
```
---

     
 
all -  [ How to build an LLM app using langchain for iOS? ](https://www.reddit.com/r/LangChain/comments/1dyhboz/how_to_build_an_llm_app_using_langchain_for_ios/) , 2024-07-10-0911
```
Looking to build an LLM app using langchain for later shipping it to the app store. 
```
---

     
 
all -  [ A chatbot that can call custom made apis ](https://www.reddit.com/r/LangChain/comments/1dycmnf/a_chatbot_that_can_call_custom_made_apis/) , 2024-07-10-0911
```
I want to create an LLM that can call custom-made APIs. We have already created several APIs, and the LLM should be able
 to make all types of HTTP requests (GET, POST, PUT, DELETE). The LLM should infer which API to call and with which para
meters, allowing users to interact using natural language.

**Current Considerations:**

* I looked into OpenAI's functi
on calling, but it seems costly with more functions. Their documentation suggests fine-tuning the model to save tokens, 
but I'm unsure how it applies to my case.
* I have experience using LLamaIndex but prefer using LangChain for this proje
ct due to its better documentation regarding API calls.
* I would prefer using a local method as I'm using Ollama.

**Qu
estions:**

1. How should I proceed with this project?
2. Is function calling the best option to consider?
3. Should I u
se OpenAI's function calling despite the costs and the capabilities of local models like LLama2 7b?

If you could just s
uggest me some resources and possible implementations that would be of great help.
```
---

     
 
all -  [ How to improve Answer Correctness? ](https://www.reddit.com/r/LangChain/comments/1dyb730/how_to_improve_answer_correctness/) , 2024-07-10-0911
```
Hi Community,

I am building a RAG application where it is 100% necessary that the answer will not return incorrect answ
ers. If the application can't generate a correct answer it should return 'I dont know'. The corpus of my data is to larg
e to implement simple Answer correctness based on Ground Truth because there are so many possible questions and therefor
e answers.  
  
I've done a lot of research and implemented the following to enhance the quality of the application:

- 
Multi-querying for optimised retrieval  
- Document reranking  
- Played around with chunk optimization  
- Implemented 
a FEVER model for Fact Extraction and Verification  
- Added metadata to my chunks for better retrieval  
- Taken a look
 ar Siamese networks and DBSCAN algorithms for similarity

I just can't seem to improve the performance anymore and it's
 still not good enough. Are there community members that ran into the same problem and might have some tips for me to im
prove the performance of answer generation or improve the logic for the application to 'know' when it can't generate an 
answer and should return 'I dont know'?

Any help will be very insightful and appreciated!


```
---

     
 
all -  [ Verbose for rag chain created with history aware retriever and retrieval chain ](https://www.reddit.com/r/LangChain/comments/1dya05v/verbose_for_rag_chain_created_with_history_aware/) , 2024-07-10-0911
```
I had an app that used ConversationalRetrievalChain where I could just set verbose=True to print the intermediate output
s in my terminal. I have now updated with history aware retriever and retrieval chain but cannot figure out how to set v
erbose flag to True or print out intermediate responses. 

My implementation mostly follows the same format like in this
 doc: [https://python.langchain.com/v0.2/docs/tutorials/qa\_chat\_history/](https://python.langchain.com/v0.2/docs/tutor
ials/qa_chat_history/)

  
Does anyone have any idea about this?
```
---

     
 
all -  [ Token Usage when Streaming ](https://www.reddit.com/r/LangChain/comments/1dy9yl1/token_usage_when_streaming/) , 2024-07-10-0911
```
Is there a standard way to get token usage when streaming rather than invoking?

Using langraph, I retrieve the totak_to
kens from `response.response_metadata` 

This is both in `call_model` (when using graph.invoke), and `acall_model` (when
 using graph.astream_events)

However, it seems like the response doesn't return the token_usage as metadata when stream
ing.

I know with OpenAI you can provide the `stream_options={'include_usage':True}`, however I'm not sure this is avail
able for all models (since I don't see it on their documentation API references.

Do I have to implement this myself wit
h tictoken or something? The last question on this Reddit with this question was from a month ago and got no responses.



**TLDR:**
`token_usage` shows just as expected when I invoke the graph, but not when I stream it.
```
---

     
 
all -  [ spaCy-llm & spacy.SpanCat for address parsing ](https://www.reddit.com/r/LLMDevs/comments/1dy9cj5/spacyllm_spacyspancat_for_address_parsing/) , 2024-07-10-0911
```
Hi all,

I'm working on a project to standardize and normalize address data using spaCy-llm's spacy.SpanCat.v3. I plan t
o train the model with examples of correctly labeled addresses to help it automatically correct a dataset filled with in
consistently formatted addresses.

My main-address column is divided into:

labels = \['NAME', 'STREET', 'BUILDING', 'LO
CALITY', 'SUBAREA', 'AREA', 'CITY'\]

There are wrong addresses in format like City, area, name, street, building and ot
her various cases which i need to handle as well. Has anyone here worked on something similar or used spacy-LLM for addr
ess parsing or something like seperating entities and formatting them? I'd appreciate any insights or tips on setting th
is up effectively. Also, how do i use the langchain/Ollama models.
```
---

     
 
all -  [ Devin for LangGraph: Automating AI Agent Development ](https://www.reddit.com/r/LangChain/comments/1dy74id/devin_for_langgraph_automating_ai_agent/) , 2024-07-10-0911
```
Hey Langchain community,

I've been tackling the challenge of developing effective AI agents. I've built a tool that tur
ns interviews or process documentation into functional AI agents in LangGraph (with all the tools, prompt, context, etc)
. I'm running a short private beta and would love your thoughts on it. Interested in checking it out and sharing your fe
edback?


[Definitive AI Beta](https://definitive-ai.streamlit.app/)

[Example Outputs](https://github.com/Definitive-AI
/Agent-Examples)
```
---

     
 
all -  [ Ai agents ](https://www.reddit.com/r/LangChain/comments/1dy5am4/ai_agents/) , 2024-07-10-0911
```
Can someone give me great usecases on AI agents which i can work on?
```
---

     
 
all -  [ AI Analytics: How do you track Q&A Activity? ](https://www.reddit.com/r/LangChain/comments/1dy3l5t/ai_analytics_how_do_you_track_qa_activity/) , 2024-07-10-0911
```
I've built an internal AI analytics app for my chatbot that tracks various chat statistics like # of questions, most act
ive users, q&a session times, answer quality, etc. It gives more more insight into usage without having to look into cha
t history.

Now I'm wondering how much more should I invest in building this out. It consumes a lot of time away from my
 core product. It's becoming a second product that I don't know if I should maintain. Are there already solutions that p
eople use that can track stats above?
```
---

     
 
all -  [ How to get structured output (JSON) from your LLM. ](https://www.reddit.com/r/LangChain/comments/1dy3i7q/how_to_get_structured_output_json_from_your_llm/) , 2024-07-10-0911
```
Hey everyone,  
I am working on a practical Llama-based app and struggled with getting clean JSON output. I know I'm not
 alone in this, so I wanted to share a solution I found.

The Instructor library is solid for getting structured data fr
om any LLM. I put together a cookbook showing how to use it: [https://git.new/PortkeyInstructor](https://git.new/Portkey
Instructor)

It covers 100+ other LLM providers along with built-in observability. Thought it might be useful for others
 here.  

```
---

     
 
all -  [ Will RunnableBranch be removed from future LangChain? ](https://www.reddit.com/r/LangChain/comments/1dy26hp/will_runnablebranch_be_removed_from_future/) , 2024-07-10-0911
```
Hey folks! I was reading some code and saw the it was using the RunnableBranch. 

In the docs, it's said that RunnableBr
anch is considered legacy [https://js.langchain.com/v0.2/docs/how\_to/routing/](https://js.langchain.com/v0.2/docs/how_t
o/routing/). Do you know if it will it be removed from the next future versions?

Asking this because I will need to upd
ate quite a lot of files based on this answer.

Thanks :)
```
---

     
 
all -  [ How to make a chatpdf app with the atmost capabilities like chatgpt and aistudio using RAG ?? ](https://www.reddit.com/r/LangChain/comments/1dy20vs/how_to_make_a_chatpdf_app_with_the_atmost/) , 2024-07-10-0911
```
Hey everyone, I was wondering how openai and ai studio are able to achieve such high accuracy when it comes to chat with
 any document.

What do you people think how this performance can be achieved by just using RAG techniques?
```
---

     
 
all -  [ 3 benefits of LangChain ](https://www.reddit.com/r/kodekloud/comments/1dy10lk/3_benefits_of_langchain/) , 2024-07-10-0911
```
Struggling with multiple tools for automation, integration, and scalability in your projects?  
  
Discover LangChain—a 
seamless solution for developers.  
  
Here are 3 key benefits of learning LangChain with KodeKloud today!  
  
🔧 Enhanc
ed Efficiency in Workflow Automation  
  
🔧 Seamless Integration with Multiple Services  
  
🔧 Improved Scalability and 
FlexibilityExplore the potential of LangChain with KodeKloud and boost your development skills today!  
  
👉 Enroll here
: [https://kode.wiki/3RWg9qZ](https://kode.wiki/3RWg9qZ)
```
---

     
 
all -  [ [0 YOE] software engineer 3rd year resume help 0 O/A. Can't even get shortlisted ](https://www.reddit.com/r/EngineeringResumes/comments/1dxybyp/0_yoe_software_engineer_3rd_year_resume_help_0_oa/) , 2024-07-10-0911
```
 

Hi, l'm an incoming 3rd year student and I really wants to find a good software engineering internship for next summe
r. I 'm located in India and this is my current resume for the internship applications

What can I improve how What can 
I add

I'm thinking of adding certifications

1. Winning hackathon, business case competitions
2. Andrew ng machine lear
ning course

How can I attach them how can I add in the resume Which one's to add

I'm applying on campus Google softwar
e engineer and more

https://preview.redd.it/4yieaq1gm7bd1.png?width=5100&format=png&auto=webp&s=13c669f0e97c2614a14844e
3f06042f301d45ad6
```
---

     
 
all -  [ What was your learning path that led you to start working with LLMs? ](https://www.reddit.com/r/LocalLLaMA/comments/1dxya2n/what_was_your_learning_path_that_led_you_to_start/) , 2024-07-10-0911
```
I'm a recent graduate in electrical engineering and I've begun exploring LLMs but barely scratching the surface. I work 
presently as an embedded systems intern in a semiconductor company. I want to switch my career. 
I've worked with FastAP
I and langchain in my past internship, but it was very brief. Now I'm at a point where I don't have too much guidance. 

To get started I have a few questions but please include any advice that you feel is appropriate 

1. What courses can I
 do to upskill myself?
2. What kind of job roles should I target?
3. What kind of projects should I get started with?

T
hank you so much.

```
---

     
 
all -  [ [3 YOE] Final sem MS, over 300+ applications, with no interview calls yet, what am I doing wrong? ](https://www.reddit.com/r/EngineeringResumes/comments/1dxv7d7/3_yoe_final_sem_ms_over_300_applications_with_no/) , 2024-07-10-0911
```
I am a final semester student based in Erlangen, Germany, actively seeking entry-level data engineering positions. My ba
ckground includes two significant projects in Generative AI (GenAI) and Large Language Models (LLMs), which have given m
e substantial hands-on experience in these cutting-edge areas. Additionally, I have practical experience working as a We
rkstudent in data engineering, where I have applied my theoretical knowledge to real-world scenarios.

Despite having th
is experience, I have been facing challenges in securing interview opportunities for data engineering roles. I possess a
 basic understanding of the German language, which I am continuously working to improve. Furthermore, I am currently emp
loyed as a Werkstudent and therefore do not require a work visa, which should make me an attractive candidate for local 
employers.

However, I am not receiving the expected interview calls. I would appreciate any advice on how to enhance my
 resume or overall job application strategy.

&#x200B;

[resume](https://preview.redd.it/k00shfqwt6bd1.png?width=4963&fo
rmat=png&auto=webp&s=6ebee509be5f0d74b1ef153853e6b86debd7e011)
```
---

     
 
all -  [ Looking to collaborate on ML/DL/NLP Project - Grad Student Here ](https://www.reddit.com/r/LangChain/comments/1dxv44t/looking_to_collaborate_on_mldlnlp_project_grad/) , 2024-07-10-0911
```
 Hey r/LangChain 

Data science grad student here, looking to team up on a machine learning, deep learning, or NLP proje
ct. I am pretty much open to work on anything interesting - existing ideas or starting from scratch.

Quick rundown:

* 
DS grad student in the US
* Experienced with common DL/NLP libraries
* 1 year as a data engineer, working on ETL pipelin
es

If you've got something brewing or want to kick around some ideas, hit me up.
```
---

     
 
MachineLearning -  [ [P] Seeking Feedback on My GenAI Job Fit Project - New to LangChain/LangGraph ](https://www.reddit.com/r/MachineLearning/comments/1dgns9p/p_seeking_feedback_on_my_genai_job_fit_project/) , 2024-07-10-0911
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

     
 
MachineLearning -  [ [P] I'm tired of LangChain, so I made a simple open-source alternative with support for tool using a ](https://www.reddit.com/r/MachineLearning/comments/1deffo8/p_im_tired_of_langchain_so_i_made_a_simple/) , 2024-07-10-0911
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

     
 
deeplearning -  [ Llama 3 not running on GPU ](https://www.reddit.com/r/deeplearning/comments/1dptxsr/llama_3_not_running_on_gpu/) , 2024-07-10-0911
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

     
 
deeplearning -  [ What is ReAct Prompting? the most important piece in agentic frameworks ](https://www.reddit.com/gallery/1djk4nk) , 2024-07-10-0911
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

     
