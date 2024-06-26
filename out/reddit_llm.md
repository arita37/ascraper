 
all -  [ GraphDB RAG w/ LangChain to find fees ](https://www.reddit.com/r/LangChain/comments/1doiikb/graphdb_rag_w_langchain_to_find_fees/) , 2024-06-26-0910
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

     
 
all -  [ Need help with streaming agent output and am I going crazy or did langchain documentation just chang ](https://www.reddit.com/r/LangChain/comments/1dohi7o/need_help_with_streaming_agent_output_and_am_i/) , 2024-06-26-0910
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

     
 
all -  [ Legal Semantic Search w LangChain, Pineccone and Next.js - full source code  ](https://docs.pinecone.io/examples/sample-apps/legal-semantic-search) , 2024-06-26-0910
```

```
---

     
 
all -  [ Multi-Agent Conversational Graph Designs ](https://www.reddit.com/r/LangChain/comments/1dogdy8/multiagent_conversational_graph_designs/) , 2024-06-26-0910
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

     
 
all -  [ How to get started? ](https://www.reddit.com/r/LangChain/comments/1doefau/how_to_get_started/) , 2024-06-26-0910
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

     
 
all -  [ Creating a prompt template for RAG chain ](https://www.reddit.com/r/LangChain/comments/1doecqa/creating_a_prompt_template_for_rag_chain/) , 2024-06-26-0910
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

     
 
all -  [ RAG system on 3 different CSV. Any suggestions? ](https://www.reddit.com/r/LangChain/comments/1dod2o3/rag_system_on_3_different_csv_any_suggestions/) , 2024-06-26-0910
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

     
 
all -  [ How can I search for a specific value in a column in a vector database without performing a semantic ](https://www.reddit.com/r/LangChain/comments/1dob8va/how_can_i_search_for_a_specific_value_in_a_column/) , 2024-06-26-0910
```
I am trying to implement a Sentence Window Retrieval method in Langchain. The best way i can figure out how to do it is 
to perform semantic similarity and return a chunk\_id along with the page\_content. I then want to retrieve documents fr
om the vector database that correspond to chunk\_id - 1 and chunk\_id + 1. how can i query the vector database based on 
a specific value, rather than a similarity search? 
```
---

     
 
all -  [ Custom Moderation GPT 4 Model ](https://www.reddit.com/r/LangChain/comments/1do8d7m/custom_moderation_gpt_4_model/) , 2024-06-26-0910
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

     
 
all -  [ Any news on when langgraph checkpointing returns to langchain-postgres? ](https://www.reddit.com/r/LangChain/comments/1do889i/any_news_on_when_langgraph_checkpointing_returns/) , 2024-06-26-0910
```
Title says it all. PostgresSaver was deprecated and removed from langchain-postgres. Are there any plans on updating thi
s or should we just stick to sqlite?

```
---

     
 
all -  [ Open-source AI Voice Agent with OpenAI ](https://www.reddit.com/r/LangChain/comments/1do81l5/opensource_ai_voice_agent_with_openai/) , 2024-06-26-0910
```
I have built an open-source AI agent which can handle voice calls and respond back in real-time. Can be used for many us
e-cases such as sales calls, customer support etc.

  
Link to project :- [https://github.com/Anil-matcha/AI-Voice-Agent
](https://github.com/Anil-matcha/AI-Voice-Agent)
```
---

     
 
all -  [ Chatbot that talks to SQL ](https://www.reddit.com/r/LangChain/comments/1do5f9p/chatbot_that_talks_to_sql/) , 2024-06-26-0910
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

     
 
all -  [ Is there any way i can integrate ollama, langchain and llama3 into a mobile simulator? ](https://www.reddit.com/r/LangChain/comments/1do4qmi/is_there_any_way_i_can_integrate_ollama_langchain/) , 2024-06-26-0910
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

     
 
all -  [ Effieicent way to do WebBaseLoader for a list of 70k urls ](https://www.reddit.com/r/LangChain/comments/1do409j/effieicent_way_to_do_webbaseloader_for_a_list_of/) , 2024-06-26-0910
```
Hello,

I'm using WebBaseLoader to extract web contents from a list of 70k urls. Everytime I run it, it runs initially w
ell and after some point, the site refuses to connect. I'm currently setting requests_per_second to 50.

Is there any wa
y I can make it faster without hitting limits?
```
---

     
 
all -  [ Some thoughts after developing with ChatGPT for 15 months. ](https://www.reddit.com/r/ChatGPTCoding/comments/1do2y50/some_thoughts_after_developing_with_chatgpt_for/) , 2024-06-26-0910
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

     
 
all -  [ AWS Bedrock - Building LLM using a knowledge base ](https://www.reddit.com/r/LangChain/comments/1do2odx/aws_bedrock_building_llm_using_a_knowledge_base/) , 2024-06-26-0910
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

     
 
all -  [ AWS Bedrock - Building LLM using a knowledge base ](https://www.reddit.com/r/LLMDevs/comments/1do2mo2/aws_bedrock_building_llm_using_a_knowledge_base/) , 2024-06-26-0910
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

     
 
all -  [ AWS Bedrock - Building LLM using a knowledge base ](https://www.reddit.com/r/aws/comments/1do2lnc/aws_bedrock_building_llm_using_a_knowledge_base/) , 2024-06-26-0910
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

     
 
all -  [ Make RAG chatapp faster ](https://www.reddit.com/r/ollama/comments/1do2glk/make_rag_chatapp_faster/) , 2024-06-26-0910
```
I am developing a chat application for troubleshoot manual (all data in troubleshoot blogs) for an product. I am using m
istral and mxbai-embed-large of embeddings. Suggest me some good architecture/techniques of RAG for faster response. I h
ave used langchain for initial implementation but not constrain.
```
---

     
 
all -  [ similarity search with relevancy score ](https://www.reddit.com/r/ChatGPT/comments/1do1j9g/similarity_search_with_relevancy_score/) , 2024-06-26-0910
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

     
 
all -  [ similarity search with relevancy score ](https://www.reddit.com/r/generativeAI/comments/1do1iwo/similarity_search_with_relevancy_score/) , 2024-06-26-0910
```
1) I want to know is 'similarity search with relevancy score' and 'similarity search with score' same?

when i try to us
e similarity\_search\_with\_relevancy\_score(langchain), i get top 3 chunks having relevancy score.

but the answer lies
 in the chunk which has the least relevancy score. which is strange. should not be the chunk containing answer has the h
ighest score? in spite of this i get the answer right every time 
```
---

     
 
all -  [ Unable to delete vectors from Serverless Pinecone for specific source files (like a.pdf) ](https://www.reddit.com/r/LangChain/comments/1do0d7y/unable_to_delete_vectors_from_serverless_pinecone/) , 2024-06-26-0910
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

     
 
all -  [ Fresher, Specialized in Data Science, AI and ML. Where to apply?  ](https://www.reddit.com/r/developersIndia/comments/1dnzdgx/fresher_specialized_in_data_science_ai_and_ml/) , 2024-06-26-0910
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

     
 
all -  [ Could anyone please refer me for any relevant openings at your company? I have 2.5 years of experien ](https://www.reddit.com/r/developersIndia/comments/1dnz1vh/could_anyone_please_refer_me_for_any_relevant/) , 2024-06-26-0910
```
https://preview.redd.it/enppdystsn8d1.png?width=1506&format=png&auto=webp&s=6ecdcfca681d4a43b79140efde0937286e40eb79


```
---

     
 
all -  [ Please take a look at my resume and provide feedback. I haven't received any interview calls in the  ](https://www.reddit.com/r/developersIndia/comments/1dnyws1/please_take_a_look_at_my_resume_and_provide/) , 2024-06-26-0910
```
https://preview.redd.it/hygmumoarn8d1.png?width=1506&format=png&auto=webp&s=aae2f17b2ab16b73bdd33b0cfd60775b03eec907


```
---

     
 
all -  [ [2 YOE] Machine Learning Engineer That's In Need of a Resume Review ](https://www.reddit.com/r/resumes/comments/1dnuya4/2_yoe_machine_learning_engineer_thats_in_need_of/) , 2024-06-26-0910
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

     
 
all -  [ 0% Callback rate so far in USA! ](https://www.reddit.com/r/resumes/comments/1dnqd15/0_callback_rate_so_far_in_usa/) , 2024-06-26-0910
```
Applied to over 580+ application for Data Analyst and Data Scientist role over US region. No call backs yet. Need your h
elp!

https://preview.redd.it/9nlx9qtnil8d1.png?width=688&format=png&auto=webp&s=26c61a7739b776daf91f8ff3ceb3e4abf9a93d6
0


```
---

     
 
all -  [ How to build efficient RAG with codebase? ](https://www.reddit.com/r/LangChain/comments/1dnos9r/how_to_build_efficient_rag_with_codebase/) , 2024-06-26-0910
```
I have tried parsing AST of codebase to create function signatures and body and embedded it in vector database. What wou
ld be the best way to prepare the codebase? 
```
---

     
 
all -  [ Handling private data without self-hosting etc. ](https://www.reddit.com/r/LangChain/comments/1dno1ll/handling_private_data_without_selfhosting_etc/) , 2024-06-26-0910
```
Is there a way to handle private data, like user input from a form without anonymouzation (eg presidio) and especially w
hile using the regular openai API?
```
---

     
 
all -  [ [HELP] Parallel function calling with Langgraph and Gemini 1.5 Pro ](https://www.reddit.com/r/LangChain/comments/1dnmeuy/help_parallel_function_calling_with_langgraph_and/) , 2024-06-26-0910
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

     
 
all -  [ LangGraph + Streamlit State Management ](https://www.reddit.com/r/LangChain/comments/1dngwkn/langgraph_streamlit_state_management/) , 2024-06-26-0910
```
Has anyone implemented a working streamlit app with LangGraph? I am having issues with state management between the two.
 If anyone has implemented the LangGraph tutorial chatbot in streamlit, please let me know
```
---

     
 
all -  [ Testing sales agent ](https://www.reddit.com/r/LangChain/comments/1dngjfm/testing_sales_agent/) , 2024-06-26-0910
```
Hey! Pretty new to this. I'm building a sales agent that can help with e.g. lead identification, enrichment, personalise
d outbound email messaging, updating our CRM. I want to test it pretty rigorously before we start using it. What is the 
best way to do something like automated regression testing for an agent, i.e. building a dataset of tasks with 'correct'
 answers where I can see how the agent performs after I make any changes? I could build this from scratch but I feel lik
e most of the tasks are fairly generic and was wondering if there are available datasets or how others have approached t
his problem 
```
---

     
 
all -  [ What's the best way to build AI Agents? LangChain or Semantic Kernel? ](https://www.reddit.com/r/build5nines/comments/1dnenml/whats_the_best_way_to_build_ai_agents_langchain/) , 2024-06-26-0910
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

     
 
all -  [ Need advice in Structuring JSON Output in Langgraph for Chatbot ](https://www.reddit.com/r/LangChain/comments/1dna58k/need_advice_in_structuring_json_output_in/) , 2024-06-26-0910
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

=======

**EDIT**: 
I've experimented with injecting few-shot examples into format\_instructor
 and it has been successful so far, although there are instances where it didn't produce the desired output. Here's what
 I do (might be helpful for someone facing a similar issue):

1. I defined an output schema and include some examples of
 the desired output inside it. I found this method in [langgraph customer support tutorial](https://langchain-ai.github.
io/langgraph/tutorials/customer-support/customer-support/#assistants)

```python
class OutputMessage(BaseModel):
    '''
Output message schema. Contains the text message generated from chatbot and the data to be displayed to the user (if any
).'''
    type: Literal['message', 'search_item', 'get_item_detail'] = Field(..., description='The type of the output me
ssage')
    message: str = Field(..., description='The text message to be displayed to the user')
    data: List = Field
([], description='The data to be displayed to the user')
    
    class Config:
        schema_extra = {
            'ex
ample': {
                'type': 'message',
                'output': 'I can help you search item and stuff',
         
       'data': []
            },
            'example2': {
                'type': 'search_item',
                'outpu
t': 'Here are items that might be fit your query',
                'data': [
                    {
                     
   'id': 1,
                        'title': 'Item 1'
                    },
                    {
                     
   'id': 2,
                        'title': 'Item 2',
                    }
                ]
            }
          #
 Add another example
```

Next, I inject the schema into the system prompt

```python
parser = PydanticOutputParser(pyda
ntic_object=OutputMessage)

system_prompt = '''
Your system prompt...
You can only response with valid and directly pars
able json. Your output must be based on this schema:\n{format_instructions}
'''

primary_assistant_prompt = ChatPromptTe
mplate.from_messages(
    [
        ('system', system_prompt),
        ('placeholder', '{messages}'),
    ]
).partial(fo
rmat_instructions=parser.get_format_instructions())
```

It's not perfect, because sometimes it doesn't follow the forma
t, but I've managed to improve it by removing unnecessary prompts. If there are better implementations or some ways to e
nhance it further, I'd greatly appreciate your insight. Many thanks for the help guys, It's been really helpful.
```
---

     
 
all -  [ Number of concurrent connections has exceeded your rate limit with Anthropic with Langchain ](https://www.reddit.com/r/LangChain/comments/1dn9ytb/number_of_concurrent_connections_has_exceeded/) , 2024-06-26-0910
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

     
 
all -  [ What strategies can we use to enhance LLM responses besides fine-tuning and prompt engineering? ](https://www.reddit.com/r/LangChain/comments/1dn7p4h/what_strategies_can_we_use_to_enhance_llm/) , 2024-06-26-0910
```
Aside from using better or larger models and employing fine-tuning, how else can we achieve improved responses from mode
ls?

p.s, I'm extremely new to this space, so any answers would be appreciated. 
```
---

     
 
all -  [ How do i parse tool calls? ](https://www.reddit.com/r/LangChain/comments/1dn6yaw/how_do_i_parse_tool_calls/) , 2024-06-26-0910
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

     
 
all -  [ Creating a Knowledge Graph from Chat History Using LangChain: Seeking Advice ](https://www.reddit.com/r/LangChain/comments/1dn55j1/creating_a_knowledge_graph_from_chat_history/) , 2024-06-26-0910
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

     
 
all -  [ Python-LLM - Session 4 - LangChain - Multi Agent - Supervisor - Agent - Query Mutual Funds Data ](https://www.reddit.com/r/u_SravzLLC/comments/1dmxfue/pythonllm_session_4_langchain_multi_agent/) , 2024-06-26-0910
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

     
 
all -  [ Langchain Textloader does not load all of the text ](https://www.reddit.com/r/LLMDevs/comments/1dmwhxk/langchain_textloader_does_not_load_all_of_the_text/) , 2024-06-26-0910
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

     
 
all -  [ Recommendation for re-ranker model on retrieved results?  ](https://www.reddit.com/r/LangChain/comments/1dmuxu9/recommendation_for_reranker_model_on_retrieved/) , 2024-06-26-0910
```
Looking for a cost effective approach that doesn’t suck
```
---

     
 
all -  [ Optimize and configure integration classes wit **kwargs ](https://www.reddit.com/r/LangChain/comments/1dmtf4a/optimize_and_configure_integration_classes_wit/) , 2024-06-26-0910
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

     
 
all -  [ Looking for ideas: How to handle parallel tool calls in LangGraph? ](https://www.reddit.com/r/LangChain/comments/1dmtcyn/looking_for_ideas_how_to_handle_parallel_tool/) , 2024-06-26-0910
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

     
 
MachineLearning -  [ [P] Seeking Feedback on My GenAI Job Fit Project - New to LangChain/LangGraph ](https://www.reddit.com/r/MachineLearning/comments/1dgns9p/p_seeking_feedback_on_my_genai_job_fit_project/) , 2024-06-26-0910
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

     
 
MachineLearning -  [ [P] I'm tired of LangChain, so I made a simple open-source alternative with support for tool using a ](https://www.reddit.com/r/MachineLearning/comments/1deffo8/p_im_tired_of_langchain_so_i_made_a_simple/) , 2024-06-26-0910
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

     
 
MachineLearning -  [ [P] Superfast RAG: Langchain Streaming and Groq ](https://www.reddit.com/r/MachineLearning/comments/1d5s9g4/p_superfast_rag_langchain_streaming_and_groq/) , 2024-06-26-0910
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

     
 
deeplearning -  [ What is ReAct Prompting? the most important piece in agentic frameworks ](https://www.reddit.com/gallery/1djk4nk) , 2024-06-26-0910
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

     
 
deeplearning -  [ How to finetune? ](https://www.reddit.com/r/deeplearning/comments/1daio0h/how_to_finetune/) , 2024-06-26-0910
```
Can someone guide me to some resource how can I finetune an open source llm or some library (like langchain) on unstruct
ured data (example: news articles on cricket) So that model can answer a question (like When did India won world Cup?)
```
---

     
