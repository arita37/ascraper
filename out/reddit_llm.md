 
all -  [ How do I map a user query and response with a certain set of predefined tasks using output parsers?  ](https://www.reddit.com/r/LangChain/comments/1dpcfh2/how_do_i_map_a_user_query_and_response_with_a/) , 2024-06-27-0911
```
So I have a doubt, I figured out how to get responses back in a certain format using the Json output parsers. I want to 
know how I can map a response to an intent. Like I want to create an AI Agent. So if the query is 'hey I wanna change my
 password I think I forgot it' it should map it to a task 'reset password'
```
---

     
 
all -  [ Add context to create_sql_agent ](https://www.reddit.com/r/LangChain/comments/1dpbl5e/add_context_to_create_sql_agent/) , 2024-06-27-0911
```
Hello I am using create_sql_agent to query a SQL server database. The problem is for some reason the agent does not know
 that it has to use SQL server dialect from the beginning and also does not know the column names.

Is there a way to pr
ovide this initial context to the prompt?

This is my code:
    llm = ChatOpenAI(model='gpt-3.5-turbo-0125', temperature
=0)
toolkit = SQLDatabaseToolkit(db=db, llm=llm)
agent_executor = create_sql_agent(
    llm=llm,
    toolkit=toolkit,
  
  verbose=True,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
)

    
```
---

     
 
all -  [ How we Chunk - turning PDF's into hierarchical structure for RAG ](https://www.reddit.com/r/LangChain/comments/1dpbc4g/how_we_chunk_turning_pdfs_into_hierarchical/) , 2024-06-27-0911
```
Hey all,

We've spent a lot of time building new techniques for parsing and searching PDFs. They've lead to a significan
t improvement in our RAG search and I wanted to share what we've learned.

**Some examples:**

Table - SEC Docs are noto
riously hard for PDF -> tables. We tried the top results on google & some opensource thins not a single one succeeded on
 this table. 

Couple examples of who we looked at:

* ilovepdf
* Adobe
* Gonitro
* PDFtables
* OCR 2 Edit
* microsoft/t
able-transformer-structure-recognition

Results - our result (can be accurately converted into CSV,MD,JSON)

https://pre
view.redd.it/5wju5gedmy8d1.png?width=1035&format=png&auto=webp&s=2a336bd0e1af14760fbb5ca4291284c99edaa27e



Example: id
entifying headers, paragraphs, lists/list items (purple), and ignoring the 'junk' at the top aka the table of contents i
n the header.

 

https://preview.redd.it/ix7747bjmy8d1.png?width=1018&format=png&auto=webp&s=ea0b65ae6a35581d955da28235
3ff63509602a38



**Why did we do this?**

W ran into a bunch of issues with existing approaches that boils down to one 
thing: hallucinations often happen because the chunk doesn't provide enough information.

* chunking by word count doesn
't work. It often chunks mid-paragraph or sentence.
* Chunking by sentence or paragraph doesn't work. If the answer span
s 2-3 paragraphs, you still are SOL.
* Semantic chunking is better but still fail quite often on lists or 'somewhat' dif
ferent pieces of info.
* LLM's deal better with structured/semi-structured data, i.e. knowing what you're sending it is 
a header, paragraph list etc., makes the model perform better.
* Headers often aren't included because they're too far a
way from the relevant vector, although often times headers contain important information.



**What are we doing differe
nt?** 

We are dynamically generating chunks when a search happens, sending headers & sub-headers to the LLM along with 
the chunk/chunks that were relevant to the search.

Example of how this is helpful: you have 7 documents that talk about
 how to reset a device, and the header says the device name, but it isn't talked about the paragraphs. The 7 chunks that
 talked about how to reset a device would come back, but the LLM wouldn't know which one was relevant to which product. 
That is, unless the chunk happened to include both the paragraphs and the headers, which often times in our experience, 
it doesn't.

This is a simplified version of what our structure looks like:

    {
      'type': 'Root',
      'children
': [
        {
          'type': 'Header',
          'text': 'How to reset an iphone',
          'children': [
         
   {
              'type': 'Header',
              'text': 'iphone 10 reset',
              'children': [
              
  { 'type': 'Paragraph', 'text': 'Example Paragraph.' },
                { 
                  'type': 'List',
          
        'children': [
                    'Item 1',
                    'Item 2',
                    'Item 3'
         
         ]
                }
              ]
            },
            {
              'type': 'Header',
              
'text': 'iphone 11 reset',
              'children': [
                { 'type': 'Paragraph', 'text': 'Example Paragraph
 2' },
                { 
                  'type': 'Table',
                  'children': [
                    { 'type
': 'TableCell', 'row': 0, 'col': 0, 'text': 'Column 1'},
                    { 'type': 'TableCell', 'row': 0, 'col': 1, 
'text': 'Column 2'},
                    { 'type': 'TableCell', 'row': 0, 'col': 2, 'text': 'Column 3'},
               
     
                    { 'type': 'TableCell', 'row': 1, 'col': 0, 'text': 'Row 1, Cell 1'},
                    { 'ty
pe': 'TableCell', 'row': 1, 'col': 1, 'text': 'Row 1, Cell 2'},
                    { 'type': 'TableCell', 'row': 1, 'co
l': 2, 'text': 'Row 1, Cell 3'}
                  ]
                }
              ]
            }
          ]
        
}
      ]
    }
    

**How do we get PDF's into this format?**

At a high level, we are identifying different portions 
of PDF's based on PDF metadata and heuristics. This helps solve three problems:

1. OCR can often mis-identify letters/n
umbers, or entirely crop out words. 
2. Most other companies are trying to use OCR/ML models to identify layout elements
, which seems to work decent on data it's seen before but fails pretty hard unexpectedly. When it fails, it's a black bo
x. For example, Microsoft released a paper a few days ago saying they trained a model on over 500M documents and still f
ails on a bunch of use cases that we have working
3. We can look at layout, font analysis etc. throughout the entire doc
 allowing us to understand the 'structure' of the document more. We'll talk about this more when looking at font classes


**How?**

First, we extract tables. We use a small OCR model to identify bounding boxes, then we do use white space an
alysis to find cells. This is the only portion of OCR we use (we're looking at doing line analysis but have punted on th
at thus far.) We have found OCR to poorly identify cells on more complex tables, and often turn a 4 into a 5 or a 8 into
 a 2 etc.

When we find a table, we find characters that we believe to be a cell based on distance between each other, t
rying to read the table as a human would. An example would be 1345 would be a 'cell' or text block, where 1    345 would
 be two text blocks due to the distance between them. A re-occurring theme is white space can get you pretty far.

Secon
d, we extract character data from the PDF:

* **Fonts**: Information about the fonts used in the document, including the
 font name, type (e.g., TrueType, Type 1), and embedded font files.
* **Character Positions:** The exact bounding box of
 each character on the page.
* **Character Color:** PDFs usually give this correctly, and when it's wrong it's still goo
d enough

PDFs provide a other metadata, but we found them to either be inaccurate or not necessary:

* **Content Stream
s:** Sequences of instructions that describe the content of the page, including text, images, and vector graphics. We fo
und these to be surprisingly inaccurate. Newline characters inserted in the middle of words, characters and words placed
 out of order, and whitespace is handled really inconsistently (more below)
* **Annotations:** Information about interac
tive elements such as links, form fields, and comments. There are useful details here that we may use in the future, but
, again, a lot of PDF tools generate these incorrectly.

Third, we strip out all space, newline, and other invisible cha
racters. We do whitespace analysis to build words from individual characters. 

**After extracting PDF metadata:**

We e
xtract out character locations, font sizes, and fonts. We then do multiple passes of whitespace analysis and clustering 
algorithms to find groups, then try to identify what category they fall into based on heuristics. We used to rely more h
eavily on clustering (DBScan specifically), but found that simpler whitespace analysis often outperformed it. 

* If you
 look at a PDF and see only a handful of characters, let's say 1% that are font 32, color blue, and each time they're id
entified together it's only 2-3 words it's likely a header. 
* Now you see 2% are font 28, red, it's probably a sub-head
er. (That is if the font spans multiple pages.) If it instead is only in a single location, it's most likely something i
mportant in the text that the author wants us to 'flag'. 
* This makes font analysis across the document important, and 
another reason we stay away from OCR
* If, the document is 80% font 12, black. It's probably 'normal text.' Normal text 
needs to be categorized into two different formats, one is paragraphs, the other is bullet points/lists. 
* For bullet p
oints we look primarily at the white space, identifying that there's a significant amount of white space, often follow b
y a bullet point, number, or dash. 
* For paragraphs, we text together in a 'normal' format without bullet points, tradi
tionally spanning a majority of the document.
* Junk detection. A lot of PDF's have junk in them. An example would be a 
header that's at the top of every single document, or a footer on every document saying who wrote it, the page number et
c. This junk otherwise is sent to the chunking algorithm meaning you can often have random information mid-paragraph. We
 generate character ngram vectors and cluster then based on L1 distance (rather than cosine). That lets us find variatio
ns like 'Page 1', 'Page 2', etc. If those appear in roughly the same location on more than 20-35% of pages, it's likely 
just repeat junk.

  


The product is still in beta so if you're actively trying to solve this, or a similar problem, w
e're letting people use it for free, in exchange for feedback.

Have additional questions? Shoot!


```
---

     
 
all -  [ Versioning RAG ](https://www.reddit.com/r/LangChain/comments/1dp9m83/versioning_rag/) , 2024-06-27-0911
```
How are people versioning their RAG pipelines? 

I've found that with context which changes/needs frequent updates, we n
eed some type of versioning strategy. 

Has anyone else run into this?
```
---

     
 
all -  [ Are there any RAG successful real production use cases out there? ](https://www.reddit.com/r/LangChain/comments/1dp7p9j/are_there_any_rag_successful_real_production_use/) , 2024-06-27-0911
```
Hello, people. I am a veteran programmer who is new to AI and its business use cases.

I am fascinated by it, and I am n
ow working on a small prototype for a client. It is an out-of-the-book RAG case:

* \~1.5K 1-page PDFs with product spec
s.
* Build a chatbot to ask questions about the products.

In our team, we are making great progress in the basic setup.
 The PDFs are indexed in a VectorDB and we are able to use GPT4 to interact with the VectorDB data and generate human fr
iendly answers.

But there is a lot to improve about the generated recomendations, conclusions, filtering, best results,
 ...

All the tutorials and documentation we are seeing end up here, in the basic setup. And don't go further in the det
ails and improvements needed to go to 'production' level. Further more, I have seen that many people on this community a
nd others are mentioning their dissapointment with the actual state of the technology and their abandom of building a RA
G architecture.

I just want a confirmation that it is possible. That some of you have managed to build a RAG architectu
re that is used satisfactorily in production. Is this the case? :)
```
---

     
 
all -  [ Use Vanna.ai for text-to-SQL much more reliable than othe r orchestration solutions, here is how to  ](https://arslanshahid-1997.medium.com/build-a-text-to-sql-chatbot-with-claude-sonnet-3-5-621a5bf9f922) , 2024-06-27-0911
```

```
---

     
 
all -  [ Evaluating Open Source LLM for RAG ](https://www.reddit.com/r/LangChain/comments/1dowgnt/evaluating_open_source_llm_for_rag/) , 2024-06-27-0911
```
I've been working on RAG and LLM, and I've developed something I think you'll find useful: BeyondLLM.

It's a tool I've 
created to simplify the process of building advanced AI applications. With just a few lines of code, you can dive into R
etrieval-Augmented Generation and Large Language Models. Plus, it's open source!

Now, here's the latest update: BeyondL
LM now includes additional features:

* Fine Tune Embeddings: Customize your model's embeddings for improved performance
.
* Observability: Easily monitor your model's performance.
* Groq LLM: Experience faster inference times for low latenc
y applications.

If you're interested, you can check out BeyondLLM on GitHub: [BeyondLLM GitHub](https://github.com/aipl
anethub/beyondllm/)
```
---

     
 
all -  [ How to automate form filling using LLM ? ](https://www.reddit.com/r/LangChain/comments/1dovvd2/how_to_automate_form_filling_using_llm/) , 2024-06-27-0911
```
So, I want to automate the form-filling section. For example, here I am taking Redmine. that is basically a chatbot that
 will interact with the user and change values in afield according to the input given by the user. for now, I have plann
ed to create a text-to-JSON chatbot using some free open-source LLM that will help the user change the fields by changin
g the natural language entered by the user to JSON format, which will be sent to execute, and the user can see the field
s be changed accordingly. 

so, how can I implement something like this?
```
---

     
 
all -  [ How to use Recursive URL Loader with Playwright/Puppeteer? ](https://www.reddit.com/r/LangChain/comments/1doudja/how_to_use_recursive_url_loader_with/) , 2024-06-27-0911
```
Hello, I'm building a RAG app with Langchain.js. It's my first time using LLM framework, thus first time using Langchain
 too. I'm currently using the Recursive URL Loader integration to recursively fetch data from websites. And, behave as I
 wanted, but I have some issue with websites using modern frontend frameworks. So, I tried the Playwright Langchain inte
gration (I'm a bit familiar with Playwright), and it's work on the desired websites, but as you guess, it only works on 
one page. So my question is there is an integration that do both? Handling JS and recursively browse the website, or how
 can I combine the two to achieve my goal? I'm open to alternative solution using Puppeteer or even Python example.

Thi
s is how I use the Recursive URL Loader:

    import { RecursiveUrlLoader } from '@langchain/community/document_loaders/
web/recursive_url';
    import { compile } from 'html-to-text';
    
    export async function loadWebsite(url: string, 
excludeDirs?: string[]) {
      const compiledConvert = compile({ wordwrap: 130 }); // returns (text: string) => string;

    
      const loader = new RecursiveUrlLoader(url, {
        extractor: compiledConvert,
        maxDepth: 1,
      
  excludeDirs,
        preventOutside: true,
      });
    
      return loader.load();
    }

And, this is my Playwrigh
t attempt:

    import { PlaywrightWebBaseLoader } from '@langchain/community/document_loaders/web/playwright';
    impo
rt { MozillaReadabilityTransformer } from '@langchain/community/document_transformers/mozilla_readability';
    import {
 RunnableSequence } from '@langchain/core/runnables';
    import { RecursiveCharacterTextSplitter } from '@langchain/tex
tsplitters';
    
    export async function loadWebsite(url: string) {
      const loader = new PlaywrightWebBaseLoader(
url, {
        launchOptions: {
          chromiumSandbox: false,
        },
      });
    
      const documents = awai
t loader.load();
    
      const transformChain = RunnableSequence.from([
        RecursiveCharacterTextSplitter.fromLa
nguage('html'),
        new MozillaReadabilityTransformer(),
      ]);
    
      return transformChain.invoke(documents
);
    }

Thanks for reading!  

```
---

     
 
all -  [ Multi GPU support ](https://www.reddit.com/r/LangChain/comments/1doszle/multi_gpu_support/) , 2024-06-27-0911
```
I want to host my app on AWS with multiple GPUs. I tried Llama-Index, but they do not support multi-GPU setups as far as
 I know. How can I run Hugging Face models on multiple GPUs?
```
---

     
 
all -  [ LangGraph integration with bedrock ](https://www.reddit.com/r/LangChain/comments/1dosz4u/langgraph_integration_with_bedrock/) , 2024-06-27-0911
```
Anyone knows if LangGraph integrates with Bedrock and what are the capabilties. I am quite new to this and I was followi
ng the langChain youtube series on LangGraph and they used a lot of OpenAI Functions so I wanted to know if it was possi
ble to do the same with Bedrock models?
```
---

     
 
all -  [ Should I Use LangChain for Building a Chatbot with OpenAI Assistant API? ](https://www.reddit.com/r/LangChain/comments/1dosb9q/should_i_use_langchain_for_building_a_chatbot/) , 2024-06-27-0911
```
I'm creating a chatbot using the OpenAI Assistant API and considering LangChain. Should I use it?

What are the pros and
 cons?

Thanks!
```
---

     
 
all -  [ Alternatives to Pydantic Data Model for Output Parsers. ](https://www.reddit.com/r/LangChain/comments/1dolptc/alternatives_to_pydantic_data_model_for_output/) , 2024-06-27-0911
```
I am working on a project where user injects a JSON/YAML/XML file as structured desired for output formatting and able t
o generate output by giving that structure to LLM.

So far I was coding all the data models as per user's requirements i
nto a Pydantic Class and using `PydanticOutputParser()`  to pass the structure information into prompt. I want to upgrad
e this feature and let user provide structure in JSON/YAML/XML (for testing I am thinking of doing with JSON) instead of
 my manually adding different data models. 

Langchain's abstractions makes it very complicated to implement changes, I 
wanted to test my hypothesis before investing time to code something of this kind. 

  
Any help would be much appreciat
ed, Thanks!
```
---

     
 
all -  [ GraphDB RAG w/ LangChain to find fees ](https://www.reddit.com/r/LangChain/comments/1doiikb/graphdb_rag_w_langchain_to_find_fees/) , 2024-06-27-0911
```
I have a document, such as this [one](https://www.xpo.com/cdn/download_files/s1/p2831/CNWY_199-AI.2.pdf), that describes
 the costs one can expect with a shipment, and throughout describe other fees that may come up depending on a specific s
hipment. I'm trying parse the doc and save it in a neo4j DB for RAG, using the LLMGraphTransformer class.

Any ideas on 
how I should go about parsing the document to have relevant chunks, and what I should set allowed nodes and relationship
s to? Everything I've tried so far, I haven't gotten any nodes or relationships from the model. 

Or, do you recommend m
aybe abandoning using a graph DB and go back to a traditional vectorDB, with a RAPTOR system? Open to suggestions!
```
---

     
 
all -  [ Need help with streaming agent output and am I going crazy or did langchain documentation just chang ](https://www.reddit.com/r/LangChain/comments/1dohi7o/need_help_with_streaming_agent_output_and_am_i/) , 2024-06-27-0911
```
Right now, my chat app involves users making a post request to an endpoint from my fastapi server.

The endpoint is resp
onsible for processing user input and calling the agent. Everything is setup but I'm running into an issue with streamin
g. For some reason, sometimes I'll find the event object apart of my streamed response (see image). **For reference I'm 
using the astream\_events API**

Here is the overall flow:

**1. My endpoint will return:**

        return StreamingRes
ponse(call_agent(agent_payload, redis_key), media_type='text/event-stream')

**2. call\_agent is defined as follows:**


    async def call_agent( payload, version='v1'):
    
        agent_response = ''
        
        async for chunk in a
gent_ex.astream_events(payload, version=version):
            
            if chunk['event'] == 'on_chat_model_stream' a
nd chunk['name'] == 'ChatOpenAI' and chunk['data']['chunk'].content:
                content = chunk['data']['chunk'].co
ntent
                yield f'{content}'
                agent_response += content
            elif chunk['event'] == 'o
n_tool_end' and chunk['name'] == 'product_info_search':
                yield f'{json.dumps(serialize_chunk(chunk))}'
  
          elif chunk['event'] == 'on_chat_model_end' and chunk['name'] == 'ChatOpenAI':
                yield f'{json.du
mps(serialize_chunk(chunk))}'

**3. My utility function serialize\_chunk is defined as follows:**

    def serialize_chu
nk(chunk):
        if isinstance(chunk, dict):
            return {k: serialize_chunk(v) for k, v in chunk.items()}
    
    elif isinstance(chunk, list):
            return [serialize_chunk(item) for item in chunk]
        elif (
          
  isinstance(chunk, AIMessageChunk) 
            or isinstance(chunk, SystemMessage)
            or isinstance(chunk, Hu
manMessage)
            or isinstance(chunk, ToolMessage)
            or isinstance(chunk, ChatPromptValue)
            
or isinstance(chunk, AgentFinish)
            or isinstance(chunk, AIMessage)
        ):
            return chunk.dict()

        else:
            return chunk

I know my serialize\_chunk is a little unique. It's what made sense to me when 
handling the non-serializeable encoding error while sending the agent response to the front end and having it treated as
 JSON. Thing is, I also don't even see the .dict() method being mentioned anywhere in the documentation.

For some reaso
n, sometimes the streamed response will include the event JSON object. I'm pretty lost as to why this is happening. 70% 
of the time things are rendering and streaming as expected for the most part.

https://preview.redd.it/c9i1oe3qds8d1.jpg
?width=658&format=pjpg&auto=webp&s=1335ac4c0c835dd8ce5e71c44d5ce50a5de6bcaa

u/hwchase17 would greattttly appreciate any
 feedback if you ever see this!
```
---

     
 
all -  [ Multi-Agent Conversational Graph Designs ](https://www.reddit.com/r/LangChain/comments/1dogdy8/multiagent_conversational_graph_designs/) , 2024-06-27-0911
```
# Preamble

What I've realized through blogs and experience, is that it is best to have different agents for different p
urposes. E.G.: one agent for docs RAG, one agent for API calls, one agent for SQL queries.

These agents, by themselves,
 work quite fine when used in a conversational sense. You can prompt the agent for API calls to reply with follow-up que
stions to obtain the remaining required parameters for the specific request to be made, based on the user request, and t
hen execute the tool call (fetch request).

Similarly, the agent for docs RAG can send a response, and the user can foll
ow up with a vague question. The LLM will have the context to know what they're referring to.

# Problem

But how can we
 merge these three together? I know there are different design patterns such as Hierarchy, and Supervisor. Supervisor so
unds like the better approach for this use case: creating a 3th supervisor agent that takes the user request and delegat
es it to one of the 3 specialized agents. However, these only seem to work when each request perform the action and resp
ond completely in one invocation.

If the supervisor agent delegates to the API calling agent, and that agent responds w
ith a follow-up question for more information, it goes back up the hierarchy to the supervisor agent and the follow-up q
uestion is returned as the response to the user. So if the user then sends more information, of course the invocation st
arts back at the supervisor agent.

How does it keep track of the last sub-agent invoked, whether a user response is to 
answer a follow-up question, re-invoke the previous agent, whether the user response deviated and required a new agent t
o be invoked, etc? I have a few ideas, let me know which ones you guys have experienced?

# Ideas

# Manual Tracking

Ra
ther than a 4th agent, the user message is first passed to an LLM with definitions of the types of agents. It's job is t
o respond with the name of the agent most likely to handle this request. That agent is then invoked. The last agent call
ed, as well as it's last response is stored. Follow up user messages call this LLM again with definitions of the type of
 agents, the message, the last agent invoked, and the last message it replied. The LLM will use this context to determin
e if it should call that same agent again with the new user message, or another agent instead.

# Supervisor Agent with 
Agent Named as Messages State

Each sub-agent will have its own isolated messages list, however the supervisor agent wil
l track messages by the name of the agent, to determine who best to delegate the request to. However, it will only track
 the last response from each invoked agent.

# Example Conversation:

    User: Hi 
    Agent: Hi, how can I help you to
day?
    User: What is the purpose of this company? 
    Agent: *delegates to RAG agent
        User: What is the purpos
e of this company?
        RAG Agent: *tool calls RAG search
        Tool: ...company purpose...categories...
        RA
G Agent: This company manages categories....
    Agent: This company manages categories....
    User: I want to create a
nother category
    Agent: *delegates to API agent
        User: I want to create another category 
        API Agent: W
hat is the category name and how many stars?
    Agent: What is the category name and how many stars?
    User: Name it 
Category 5
    Agent: *delegates to API agent
        User: Name it Category 5
        API Agent: How many stars (1-5)?

    Agent: How many stars (1-5)?
    User: 5
    Agent: *delegates to API agent
        User: 5
        API Agent: *tool
 call endpoint with required params 
        Tool: success
        API Agent: You have successfully created Category 5.

    Agent: You have successfully created Category 5.
    User: How many categories have been created today
    Agent: *d
elegates to SQL Agent
        User: How many categories have been created today
        SQL Agent: *tool calls sql query
 generation
        Tool: select count(1) from categories...
        SQL Agent: *tool calls sql query execution
        
Tool: (8)
        SQL Agent: 8 categories have been created today.
    Agent: 8 categories have been created today.

The
 history for each agent may be as follows:

RAG Agent:

    User: What is the purpose of this company?
    Agent: *tool 
calls RAG search
    Tool: ...company purpose...categories...
    Agent: This company manages categories....

API Agent:


    User: I want to create another category 
    Agent: What is the category name and how many stars?
    User: Name i
t Category 5
    Agent: How many stars (1-5)?
    User: 5
    Agent: *tool call endpoint with required params 
    Tool:
 success
    Agent: You have successfully created Category 5.

SQL Agent:

    User: How many categories have been creat
ed today
    SQL Agent: *tool calls sql query generation
    Tool: select count(1) from categories...
    SQL Agent: *to
ol calls sql query execution
    Tool: (8)
    SQL Agent: 8 categories have been created today.

Supervisor Agent:

    
System: You are a supervisor Agent with the following assistants: RAG Agent helps when.... API Agent helps when.... SQL 
Agent helps when.... At different times during the conversation, your assistants may interject to respond to the user ba
sed on their specialty. Whenever the user responds, based on the history, determine which one of your assistants should 
respond next.
    User: Hi 
    Agent: Hi, how can I help you today?
    User: What is the purpose of this company? 
   
 RAG Agent: This company manages categories....
    User: I want to create another category
    API Agent: What is the c
ategory name and how many stars?
    User: Name it Category 5
    API Agent: How many stars (1-5)?
    User: 5
    API A
gent: You have successfully created Category 5.
    User: How many categories have been created today
    SQL Agent: 8 c
ategories have been created today.

Perhaps like this, it can better determine who to delegate future responses to. This
 by itself already seems a bit more complex than seen developed so far. However, there are still things to consider, suc
h as when the user changes their mind, how would delegation work?

# Example Conversation:

    User: Hi 
    Agent: Hi,
 how can I help you today?
    User: What is the purpose of this company? 
    Agent: *delegates to RAG agent
        Us
er: What is the purpose of this company?
        RAG Agent: *tool calls RAG search
        Tool: ...company purpose...ca
tegories...
        RAG Agent: This company manages categories....
    Agent: This company manages categories....
    Us
er: I want to create another category
    Agent: *delegates to API agent
        User: I want to create another category
 
        API Agent: What is the category name and how many stars?
    Agent: What is the category name and how many sta
rs?
    User: How many categories have been created today? <-- new request, not meant to be the category name
    Agent:
 *delegates to SQL Agent
        User: How many categories have been created today?
        SQL Agent: *tool calls sql q
uery generation
        Tool: select count(1) from categories...
        SQL Agent: *tool calls sql query execution
    
    Tool: (9)
        SQL Agent: 9 categories have been created today.
    Agent: 9 categories have been created today.

    User: Okay. I want to create a sub-category.
    Agent: *delegates to API agent
        User: Okay. I want to create
 a sub-category.
        API Agent: I'm sorry, you cannot create sub-categories.
    Agent: I'm sorry, you cannot create
 sub-categories.

The history for each agent may be as follows:

RAG Agent:

    User: What is the purpose of this compa
ny?
    Agent: *tool calls RAG search
    Tool: ...company purpose...categories...
    Agent: This company manages categ
ories....

API Agent:

    User: I want to create another category 
    Agent: What is the category name and how many st
ars?
    User: Okay. I want to create a sub-category. <-- somehow it knows this is meant as a new request, and not part 
of the category name as above
    Agent: I'm sorry, you cannot create sub-categories.

SQL Agent:

    User: How many ca
tegories have been created today?
    Agent: *tool calls sql query generation
    Tool: select count(1) from categories.
..
    Agent: *tool calls sql query execution
    Tool: (9)
    Agent: 9 categories have been created today.

Supervisor
 Agent:

    System: You are a supervisor Agent with the following assistants: RAG Agent helps when.... API Agent helps 
when.... SQL Agent helps when.... At different times during the conversation, your assistants may interject to respond t
o the user based on their specialty. Whenever the user responds, based on the history, determine which one of your assis
tants should respond next.
    User: Hi 
    Agent: Hi, how can I help you today?
    User: What is the purpose of this 
company? 
    RAG Agent: This company manages categories....
    User: I want to create another category
    API Agent: 
What is the category name and how many stars?
    User: How many categories have been created today? <-- new request, no
t meant to be the category name. somehow it knows to delegate to SQL Agent instead
    SQL Agent: 9 categories have been
 created today.
    User: Okay. I want to create a sub-category.
    API Agent: I'm sorry, you cannot create sub-categor
ies.

To solve this, maybe there should be an additional step that re-crafts the user prompt before delegating it to eac
h sub-agent?

Does anyone have experiences with these in LangGraph?
```
---

     
 
all -  [ How to get started? ](https://www.reddit.com/r/LangChain/comments/1doefau/how_to_get_started/) , 2024-06-27-0911
```
Hi

I’ve tried to make some agent using crewai and autogen. And now I’m trying to make something similar in langchain. 


What I’m trying to do is to ask the chatbot a question about a topic, this topic needs to be researched (googled), the 
sites scraped and embedded for content, and as a result I’d like the AI to output a structured data which I can then for
mat as markdown. 

I’ve made this work fairly ok with crewai, but would like to do this with langchain. I am able to
- s
earch for topics (DuckDuckGo, serper)
- scrape and embed a site (bs4, web scraper)
- output structured data (json)

But 
I’m unable to do this in an agent chain. 

I also have a second use case which is to make an AI access APIs for searchin
g (self hosted content), and use that result as a context for the answer. 

Using local models only with ollama, prefera
bly the openapi spec api. 

Where should I start? Trying to chain these tools together went for easy to expert way too f
ast! 😂
```
---

     
 
all -  [ Creating a prompt template for RAG chain ](https://www.reddit.com/r/LangChain/comments/1doecqa/creating_a_prompt_template_for_rag_chain/) , 2024-06-27-0911
```
Using the following prompt template in building a RAG based QnA application:

    template = '''Use the following pieces
 of context to answer the question about the story at the end.
    If the context doesn't provide enough information, ju
st say that you don't know, don't try to make up an answer.
    Pay attention to the context of the question rather than
 just looking for similar keywords in the corpus.
    Use three sentences maximum and keep the answer as concise as poss
ible.
    Always say 'thanks for asking!' at the end of the answer.
    {context}
    Question: {question}
    Helpful A
nswer:
    '''

  
After a frequent testing, this turns out to be a very primitive prompt to the llm as the responses we
nt on to hallucinate and sometimes produced manipulated responses on asking for a misleading query i.e. to test if it co
rrects the user. 

If anyone working on the same or knows how to craft complex prompt templates for an optimized respons
e generation, please care to enlighten.

Besides, are there any frameworks for such templates to ease up the task of pro
mpt engineering?

Thank You 
```
---

     
 
all -  [ RAG system on 3 different CSV. Any suggestions? ](https://www.reddit.com/r/LangChain/comments/1dod2o3/rag_system_on_3_different_csv_any_suggestions/) , 2024-06-27-0911
```
Hi everyone!

I have three CSV files for a RAG project. Two of the files are interconnected by a field that acts like a 
relational database key. The third file contains information related to the others, but there is no clear relational ID 
or similar field to connect them.

My idea was to unify the first two files into a JSON format and then use an LLM to cl
assify natural language queries to extract a JSON for searching and generating a response based on the results. However,
 I have two problems with this solution:

1. How can I integrate the information from the third CSV file?
2. The custome
r requested using a vector database like Chroma or Pinecone.

What do you suggest I do?
```
---

     
 
all -  [ How can I search for a specific value in a column in a vector database without performing a semantic ](https://www.reddit.com/r/LangChain/comments/1dob8va/how_can_i_search_for_a_specific_value_in_a_column/) , 2024-06-27-0911
```
I am trying to implement a Sentence Window Retrieval method in Langchain. The best way i can figure out how to do it is 
to perform semantic similarity and return a chunk\_id along with the page\_content. I then want to retrieve documents fr
om the vector database that correspond to chunk\_id - 1 and chunk\_id + 1. how can i query the vector database based on 
a specific value, rather than a similarity search? 
```
---

     
 
all -  [ Custom Moderation GPT 4 Model ](https://www.reddit.com/r/LangChain/comments/1do8d7m/custom_moderation_gpt_4_model/) , 2024-06-27-0911
```
Hi community, I have some problems with my model; I used GPT-4 for do a health model with RAG; I require that my model d
oesn't speak about: financial, techonology... I want my model only can speak about health topics.



I used Fine-tuning 
for this issue, but my model got overfitting in some cases, for example when I wrote 'Hi, how ar you' their answer was '
I can't speak about that...', when I passed some examples in the traning data some examples that in which model respond 
with 'Hi, my name in CemGPT....'.



How could I solve this problem?



help me pls!
```
---

     
 
all -  [ Any news on when langgraph checkpointing returns to langchain-postgres? ](https://www.reddit.com/r/LangChain/comments/1do889i/any_news_on_when_langgraph_checkpointing_returns/) , 2024-06-27-0911
```
Title says it all. PostgresSaver was deprecated and removed from langchain-postgres. Are there any plans on updating thi
s or should we just stick to sqlite?

```
---

     
 
all -  [ Open-source AI Voice Agent with OpenAI ](https://www.reddit.com/r/LangChain/comments/1do81l5/opensource_ai_voice_agent_with_openai/) , 2024-06-27-0911
```
I have built an open-source AI agent which can handle voice calls and respond back in real-time. Can be used for many us
e-cases such as sales calls, customer support etc.

  
Link to project :- [https://github.com/Anil-matcha/AI-Voice-Agent
](https://github.com/Anil-matcha/AI-Voice-Agent)
```
---

     
 
all -  [ Chatbot that talks to SQL ](https://www.reddit.com/r/LangChain/comments/1do5f9p/chatbot_that_talks_to_sql/) , 2024-06-27-0911
```
I have limited experience with LangChain and LLMs, primarily building simple chatbots with Retrieval-Augmented Generatio
n (RAG). Currently, I'm helping a friend build a WhatsApp chatbot that retrieves its answers from a SQL database. I've b
een experimenting with the SQL tutorials in LangChain, but I haven't yet achieved satisfactory results for a v1. I've tr
ied using `create_sql_query_chain` and `create_sql_agent`. `create_sql_query_chain` has been very inconsistent, while `c
reate_sql_agent` has produced better results but still struggles with the following issues:

1. Ensuring the LLM restric
ts queries to a specific `customer_id` obtained from the context.
2. Preventing the LLM from answering questions that ar
e too open, generic, or related to restricted device types (the user should only be allowed to ask about device type A).


Given these challenges, I'm looking for advice, ideas, and any relevant experiences you might have. Thank you
```
---

     
 
all -  [ Is there any way i can integrate ollama, langchain and llama3 into a mobile simulator? ](https://www.reddit.com/r/LangChain/comments/1do4qmi/is_there_any_way_i_can_integrate_ollama_langchain/) , 2024-06-27-0911
```
Basically I've built one use case on linux desktop to simulate an AI personal assistant on the mobile phone which can au
tomate various actions. My use case is basically that when an incoming call comes, the personal assistant determines the
 identity of the caller using the contact list and whether or not the user is in a meeting by checking the calendar. (Si
nce i havent done anything on the phone, calendar contact list etc. are implemented as simple text files). Then dependin
g on the above two factors, it either performs receive\_call, send\_message or mute. 

So the final output is just one l
ine stating the name of the action to be taken(ie send message, receive call or mute) 

  
Is there any way i can displa
y this on a mobile simulator?
```
---

     
 
all -  [ Effieicent way to do WebBaseLoader for a list of 70k urls ](https://www.reddit.com/r/LangChain/comments/1do409j/effieicent_way_to_do_webbaseloader_for_a_list_of/) , 2024-06-27-0911
```
Hello,

I'm using WebBaseLoader to extract web contents from a list of 70k urls. Everytime I run it, it runs initially w
ell and after some point, the site refuses to connect. I'm currently setting requests_per_second to 50.

Is there any wa
y I can make it faster without hitting limits?
```
---

     
 
all -  [ Some thoughts after developing with ChatGPT for 15 months. ](https://www.reddit.com/r/ChatGPTCoding/comments/1do2y50/some_thoughts_after_developing_with_chatgpt_for/) , 2024-06-27-0911
```
# Revolutionizing Software Development: My Journey with Large Language Models

As a seasoned developer with over 25 year
s of coding experience and nearly 20 years in professional software development, I've witnessed numerous technological s
hifts. The advent of LLMs, however, like GPT-4, has genuinely transformed my workflow. Here's some information on my pro
cess for leveraging LLMs in my daily coding practices and my thoughts on the future of our field.

# Integrating LLMs in
to My Workflow

Since the release of GPT-4, I've incorporated LLMs as a crucial component of my development process. The
y excel at:

1. **Language Translation**: Swiftly converting code between programming languages.
2. **Code Documentation
**: Generating comprehensive comments and documentation.
3. **Refactoring**: Restructuring existing code for improved re
adability and efficiency.

These capabilities have significantly boosted my productivity. For instance, translating a co
mplex class from Java to Python used to take hours of manual effort, but with an LLM's assistance, it now takes minutes.


# A Collaborative Approach

My current workflow involves a collaborative dance with various AI models, including ChatG
PT, Mistral, and Claude. We engage in mutual code critique, fostering an environment of continuous improvement. This app
roach has led to some fascinating insights:

* The AI often catches subtle inefficiencies and potential bugs I might ove
rlook or provides a thoroughness I might be too lazy to implement.
* Our 'discussions' frequently lead to novel solution
s I hadn't considered.
* Explaining my code to the AI helps me clarify my thinking.

# Challenges and Solutions

# Conte
xt Limitations

While LLMs excel at refactoring, they must help maintain context across larger codebases. When refactori
ng a class, changes can ripple through the codebase in ways the LLM can't anticipate.

To address this, I'm developing a
 method to create concise summaries of classes, including procedures and terse documentation. This approach, reminiscent
 of C header files, allows me to feed more context into the prompt without overwhelming the model.

# Iterative Improvem
ent

I've found immense value in repeatedly asking the LLM, 'What else would you improve?' This simple technique often u
ncovers layers of optimizations, continuing until the model can't suggest further improvements.

# The Human Touch

Desp
ite their capabilities, LLMs still benefit from human guidance. I often need to steer them towards specific design patte
rns or architectural decisions.

# Looking to the Future

# The Next Big Leap

I envision the next killer app that could
 revolutionize our debugging processes:

1. Run code locally
2. Pass error messages to LLMs
3. Receive and implement sug
gested fixes
4. Iterate until all unit tests pass

This would streamline the tedious copy-paste cycle many of us current
ly endure. This also presents an opportunity to revisit and adapt test-driven development practices for the LLM era.

**
Have you used langchain or any similar products? I would love to get up to speed.**

# Type Hinting and Language Prefere
nces

While I'm not the biggest fan of TypeScript's complexities, type hinting (even in Python) helps ensure LLMs produc
e results in the intended format. The debate between static and dynamic typing takes on new dimensions in the context of
 AI-assisted coding.

# The Changing Landscape

We may only have a few more years of 'milking the software development g
ravy train' before AI significantly disrupts our field. While I'm hesitant to make firm predictions, developers must sta
y adaptable and continuously enhance their skills.

# Conclusion

Working with LLMs has been the biggest game-changer fo
r my development process that I can remember. I can't wait to hear your feedback about how I can transform my developmen
t workflow to the next level.
```
---

     
 
all -  [ AWS Bedrock - Building LLM using a knowledge base ](https://www.reddit.com/r/LangChain/comments/1do2odx/aws_bedrock_building_llm_using_a_knowledge_base/) , 2024-06-27-0911
```
hi

so, I've just started this week a mini project using AWS Bedrock, Claude Haiku and Titan embedding model. It's more 
for me to understand how things work together so no production expectations - I want to add some documentation in the kn
owledge base and then ask questions and be provided with a full list of steps. The steps are split in different document
s and use different components of the software, somebody with 5+ years of experience would be aware of this and this is 
what the system prompt that I use explains. 

I've reached the step where I ask the question in the Test Knowledge Base 
area and it just outputs the like for like extract from 1 single document. I tried to play with the temperature and top-
p of the model but it's the same answer. 

My question is: has anyone else experience something similar and how did they
 improve the answers? Is it through a lot of prompting/ changing the chunking strategy or moving to using APIs and langc
hain directly? 
```
---

     
 
all -  [ AWS Bedrock - Building LLM using a knowledge base ](https://www.reddit.com/r/LLMDevs/comments/1do2mo2/aws_bedrock_building_llm_using_a_knowledge_base/) , 2024-06-27-0911
```
Hi

so, I've just started this week a mini project using AWS Bedrock, Claude Haiku and Titan embedding model. It's more 
for me to understand how things work together so no production expectations - I want to add some documentation in the kn
owledge base and then ask questions and be provided with a full list of steps. The steps are split in different document
s and use different components of the software, somebody with 5+ years of experience would be aware of this and this is 
what the system prompt that I use explains. 

I've reached the step where I ask the question in the Test Knowledge Base 
area and it just outputs the like for like extract from 1 single document. I tried to play with the temperature and top-
p of the model but it's the same answer. 

My question is: has anyone else experience something similar and how did they
 improve the answers? Is it through a lot of prompting/ changing the chunking strategy or moving to using APIs and langc
hain directly? 
```
---

     
 
all -  [ AWS Bedrock - Building LLM using a knowledge base ](https://www.reddit.com/r/aws/comments/1do2lnc/aws_bedrock_building_llm_using_a_knowledge_base/) , 2024-06-27-0911
```
# hi

so, I've just started this week a mini project using AWS Bedrock, Claude Haiku and Titan embedding model. It's mor
e for me to understand how things work together so no production expectations - I want to add some documentation in the 
knowledge base and then ask questions and be provided with a full list of steps. The steps are split in different docume
nts and use different components of the software, somebody with 5+ years of experience would be aware of this and this i
s what the system prompt that I use explains. 

I've reached the step where I ask the question in the Test Knowledge Bas
e area and it just outputs the like for like extract from 1 single document. I tried to play with the temperature and to
p-p of the model but it's the same answer. 

My question is: has anyone else experience something similar and how did th
ey improve the answers? Is it through a lot of prompting/ changing the chunking strategy or moving to using APIs and lan
gchain directly ? 
```
---

     
 
all -  [ Make RAG chatapp faster ](https://www.reddit.com/r/ollama/comments/1do2glk/make_rag_chatapp_faster/) , 2024-06-27-0911
```
I am developing a chat application for troubleshoot manual (all data in troubleshoot blogs) for an product. I am using m
istral and mxbai-embed-large of embeddings. Suggest me some good architecture/techniques of RAG for faster response. I h
ave used langchain for initial implementation but not constrain.
```
---

     
 
all -  [ similarity search with relevancy score ](https://www.reddit.com/r/ChatGPT/comments/1do1j9g/similarity_search_with_relevancy_score/) , 2024-06-27-0911
```
# similarity search with relevancy score

1. I want to know is 'similarity search with relevancy score' and 'similarity 
search with score' same?

when i try to use similarity\_search\_with\_relevancy\_score(langchain), i get top 3 chunks ha
ving relevancy score.

but the answer lies in the chunk which has the least relevancy score. which is strange. should no
t be the chunk containing answer has the highest score? in spite of this i get the answer right every time
```
---

     
 
all -  [ similarity search with relevancy score ](https://www.reddit.com/r/generativeAI/comments/1do1iwo/similarity_search_with_relevancy_score/) , 2024-06-27-0911
```
1) I want to know is 'similarity search with relevancy score' and 'similarity search with score' same?

when i try to us
e similarity\_search\_with\_relevancy\_score(langchain), i get top 3 chunks having relevancy score.

but the answer lies
 in the chunk which has the least relevancy score. which is strange. should not be the chunk containing answer has the h
ighest score? in spite of this i get the answer right every time 
```
---

     
 
all -  [ Unable to delete vectors from Serverless Pinecone for specific source files (like a.pdf) ](https://www.reddit.com/r/LangChain/comments/1do0d7y/unable_to_delete_vectors_from_serverless_pinecone/) , 2024-06-27-0911
```
Hi, I'm unable to delete vectors for a specific source using metadata filtering with serverless pinecone as this feature
 is not available with serverless pinecone. And the other architecture of pinecone is not free, so I'm using serverless 
for development purposes. 

A solution is recommended which is https://docs.pinecone.io/guides/data/manage-rag-documents
#delete-all-records-for-a-parent-document.

But this solution is not useful as I cannot pass specific metadata for delet
ion of vectors, instead it asks for a prefix in ids of vector. Now I don't know how to make it work for my use case. I'v
e also tried adding custom ids for vectors using name of source file + str(uuid) for each chunk and created a list which
 I'm trying to pass to pinecone.from\_documents but it doesn't support setting custom ids for vectors.

Now I also don't
 know how they set the ids as shown in example like 'doc1#chunk1' etc....  


https://preview.redd.it/34yirw1t8o8d1.png?
width=1844&format=png&auto=webp&s=c4ecf51d149179459ed2042f1694d5fee7ec462b


```
---

     
 
all -  [ Fresher, Specialized in Data Science, AI and ML. Where to apply?  ](https://www.reddit.com/r/developersIndia/comments/1dnzdgx/fresher_specialized_in_data_science_ai_and_ml/) , 2024-06-27-0911
```
I've been trying to seek a job, but unable to apply efficiently.

Q1:Where do I look for jobs? Indeed, LinkedIn, where e
lse? 

Q2: Should I keep messaging the recruiters and other people on LinkedIn for referrals? (I've never been very good
 at networking)

I've done really good projects involving Groq, Langchain, open source LLMs, etc.
and I have a decent co
ding experience too.

Q3: Should I just seek an entry point into the market and not worry about my first salary? 
(How's
 the market now?)

Q4: Are internships easier to get? (Later convert to FTE), if so where do I apply for internships?

Q
5: What skillset is necessary? What do you expect (as a recruiter) from a fresher specialising in AI-ML? 

Thanks in Adv
ance :)

EDIT: Do you know any telegram/discord groups that notify about job postings/hiring updates? 
```
---

     
 
all -  [ Could anyone please refer me for any relevant openings at your company? I have 2.5 years of experien ](https://www.reddit.com/r/developersIndia/comments/1dnz1vh/could_anyone_please_refer_me_for_any_relevant/) , 2024-06-27-0911
```
https://preview.redd.it/enppdystsn8d1.png?width=1506&format=png&auto=webp&s=6ecdcfca681d4a43b79140efde0937286e40eb79


```
---

     
 
all -  [ Please take a look at my resume and provide feedback. I haven't received any interview calls in the  ](https://www.reddit.com/r/developersIndia/comments/1dnyws1/please_take_a_look_at_my_resume_and_provide/) , 2024-06-27-0911
```
https://preview.redd.it/hygmumoarn8d1.png?width=1506&format=png&auto=webp&s=aae2f17b2ab16b73bdd33b0cfd60775b03eec907


```
---

     
 
all -  [ [2 YOE] Machine Learning Engineer That's In Need of a Resume Review ](https://www.reddit.com/r/resumes/comments/1dnuya4/2_yoe_machine_learning_engineer_thats_in_need_of/) , 2024-06-27-0911
```
Hi everyone,

I need some feedback on my resume to see if there's any way to make it better/anything you'd approve. Than
ks in advance for your insights. I really appreciate it.

I'm targeting entry level machine learning roles. I have 2 YOE
 as a Machine Learning Engineer.

https://preview.redd.it/tuc65dndmm8d1.jpg?width=5100&format=pjpg&auto=webp&s=042b4b38c
c4a1b8e9bda009b81a0335ea3766155


```
---

     
 
all -  [ 0% Callback rate so far in USA! ](https://www.reddit.com/r/resumes/comments/1dnqd15/0_callback_rate_so_far_in_usa/) , 2024-06-27-0911
```
Applied to over 580+ application for Data Analyst and Data Scientist role over US region. No call backs yet. Need your h
elp!

https://preview.redd.it/9nlx9qtnil8d1.png?width=688&format=png&auto=webp&s=26c61a7739b776daf91f8ff3ceb3e4abf9a93d6
0


```
---

     
 
all -  [ How to build efficient RAG with codebase? ](https://www.reddit.com/r/LangChain/comments/1dnos9r/how_to_build_efficient_rag_with_codebase/) , 2024-06-27-0911
```
I have tried parsing AST of codebase to create function signatures and body and embedded it in vector database. What wou
ld be the best way to prepare the codebase? 
```
---

     
 
all -  [ Handling private data without self-hosting etc. ](https://www.reddit.com/r/LangChain/comments/1dno1ll/handling_private_data_without_selfhosting_etc/) , 2024-06-27-0911
```
Is there a way to handle private data, like user input from a form without anonymouzation (eg presidio) and especially w
hile using the regular openai API?
```
---

     
 
MachineLearning -  [ [P] Seeking Feedback on My GenAI Job Fit Project - New to LangChain/LangGraph ](https://www.reddit.com/r/MachineLearning/comments/1dgns9p/p_seeking_feedback_on_my_genai_job_fit_project/) , 2024-06-27-0911
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

     
 
MachineLearning -  [ [P] I'm tired of LangChain, so I made a simple open-source alternative with support for tool using a ](https://www.reddit.com/r/MachineLearning/comments/1deffo8/p_im_tired_of_langchain_so_i_made_a_simple/) , 2024-06-27-0911
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

     
 
MachineLearning -  [ [P] Superfast RAG: Langchain Streaming and Groq ](https://www.reddit.com/r/MachineLearning/comments/1d5s9g4/p_superfast_rag_langchain_streaming_and_groq/) , 2024-06-27-0911
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

     
 
deeplearning -  [ What is ReAct Prompting? the most important piece in agentic frameworks ](https://www.reddit.com/gallery/1djk4nk) , 2024-06-27-0911
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

     
 
deeplearning -  [ How to finetune? ](https://www.reddit.com/r/deeplearning/comments/1daio0h/how_to_finetune/) , 2024-06-27-0911
```
Can someone guide me to some resource how can I finetune an open source llm or some library (like langchain) on unstruct
ured data (example: news articles on cricket) So that model can answer a question (like When did India won world Cup?)
```
---

     
