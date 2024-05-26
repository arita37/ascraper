 
all -  [ Help! 'Recursion limit' when trying to use chain with 'llm.bind_tools' - LangGraph ](https://www.reddit.com/r/LangChain/comments/1d0om4f/help_recursion_limit_when_trying_to_use_chain/) , 2024-05-26-0911
```
Hey guys. I'm trying to get comfortable with LangGraph in an attempt to then develop a chatbot based on this framework. 
 
When trying to test the idea of a node in my chatbot, I found myself faced with this error.  
Could somebody please he
lp me understand what's wrong with my code and how can I solve this problem?  
I would be truly thankful!

The code:

  
  from typing import Annotated, List
    from langchain_openai import ChatOpenAI
    from langchain_community.tools.tavi
ly_search import TavilySearchResults
    from langchain_core.prompts import ChatPromptTemplate, PromptTemplate
    from 
langchain_core.messages import BaseMessage
    from typing_extensions import TypedDict
    
    from langgraph.graph imp
ort StateGraph, END
    from langgraph.graph.message import add_messages
    from langgraph.prebuilt import ToolNode, to
ols_condition
    
    # Define AgentState class with the proper typing
    class AgentState(TypedDict):
        message
s: Annotated[List[BaseMessage], add_messages]
        query: str
        games: List[str]
    
    # Initialize the tool
 and LLM
    tool = TavilySearchResults(max_results=3)
    tools = [tool]
    llm = ChatOpenAI(model='gpt-3.5-turbo', te
mperature=0)
    llm_with_tools = llm.bind_tools(tools)
    
    # Define the function for the game title search
    def
 game_title_search(state: AgentState):
        game_search_prompt = PromptTemplate(
        template='''You are part of 
a chatbot that provides personalized video game recommendations based on user preferences. \n
        Your task is to se
arch for video games that match the user query, using the Tavily API. \n
        Only return the titles of the games. \n

        The number of games to return is limited to 5. \n\n
    
        The results provided will look as follows (Pyt
hon list): \n
        ['game_title_1', 'game_title_2', 'game_title_3', ...]
    
        User Query: {query}''',
       
 input_variables=['query'],
    )
        game_search = game_search_prompt | llm_with_tools
    
        game_search_res
ult = game_search.invoke({'query': state['query']})
    
        return {'messages': [game_search_result]} # Also, I nee
d to extract the game titles from the tool's results and update the state attribute 'games' - how can I do this?
    
  
  # Build the graph
    graph_builder = StateGraph(AgentState)
    graph_builder.add_node('game_search', game_title_sear
ch)
    
    tool_node = ToolNode(tools=[tool])
    graph_builder.add_node('tools', tool_node)
    
    graph_builder.ad
d_conditional_edges(
        'game_search',
        tools_condition,
    )
    
    graph_builder.add_edge('tools', 'gam
e_search')
    graph_builder.set_entry_point('game_search')
    graph = graph_builder.compile()
    
    # Define the in
itial state
    input_state = {
        'messages': [],
        'query': '',
        'games': []
    }
    
    user_inp
ut = 'What games are similar to The Witcher 3?'
    input_state['query'] = user_input
    input_state['messages'] = [('u
ser', user_input)]
    
    output = graph.invoke(input_state, config={'recursion_limit': 50})
    print(output)
    
  
  
    
```
---

     
 
all -  [ LangChain JS Arbitrary File Read Vulnerability ](https://evren.ninja/langchain-afr-vulnerability.html) , 2024-05-26-0911
```

```
---

     
 
all -  [ How do you go about creating a RAG chatbot using Graph and Vector on internal documents? ](https://www.reddit.com/r/LangChain/comments/1d0j0hc/how_do_you_go_about_creating_a_rag_chatbot_using/) , 2024-05-26-0911
```
When you are making RAG chatbots using Graph and Vectors how are you storing the internal data? What’s the general appro
ach?

For example, say you are asked to ingest all your companies files, like word docs PDFs and everything in between. 
If you use RAG with Graph and Vector embeddedings where are you storing the data from the documents? I’m curious what th
e general approach is to chunking, tokenizing, and embedding are?

If you had to ingest your companies documents using a
 RAG, Graph, and vector approach how would you set this up? What would the schema be of the Graph, where would the vecto
rs be stored?

Thanks
```
---

     
 
all -  [ Help me improve my resume! I will soon be entering 4th yr and placement season is also coming so if  ](https://www.reddit.com/gallery/1d0i1ac) , 2024-05-26-0911
```
I will be entering my 4th yr soon! Any suggestions in terms of projects, internship or certificates or anything else I w
ill be grateful!
1st is AI/ML based resume and 2nd is for dev roles.
```
---

     
 
all -  [ I fixed my resume as per the feedback, looking for review  ](https://www.reddit.com/r/resumes/comments/1d0fade/i_fixed_my_resume_as_per_the_feedback_looking_for/) , 2024-05-26-0911
```
I have made the fixes mentioned and looking for feedback, so that I dont lose on opportunities unlike last time. I have 
exhausted so many of the opportunities already. Also if someone can share their resume which worked for them that would 
be helpful in making fixes. 

https://preview.redd.it/jidd3f5hjl2d1.png?width=5100&format=png&auto=webp&s=5f1f31565ecde0
8c35d200931f6d5351a0faaecf

https://preview.redd.it/cjdq3d5hjl2d1.png?width=5100&format=png&auto=webp&s=7155c618bc5bacbd
66646f650fcbb357cd122bdb

 
```
---

     
 
all -  [ [11 YOE]Took advice from this here and fixed my resume, looking for review before making application ](https://www.reddit.com/r/EngineeringResumes/comments/1d0f6lp/11_yoetook_advice_from_this_here_and_fixed_my/) , 2024-05-26-0911
```
I have fixed the resume as per the wiki and feedback from the community, can someone review it so that I can make job ap
plication. Also if someone can share their resume which worked for them or had high success rate that would be helpful. 


https://preview.redd.it/3wbgxupbil2d1.png?width=5100&format=png&auto=webp&s=21699d699274f4921fa18748fb6a9abd0905b24c


https://preview.redd.it/q3oplv5cil2d1.png?width=5100&format=png&auto=webp&s=d1fc08c81ac59890e11c873a2a8c345ee657a4f6


```
---

     
 
all -  [ How to ignore retrieval step (RAG) when it is not necessary ](https://www.reddit.com/r/LangChain/comments/1d0e7ov/how_to_ignore_retrieval_step_rag_when_it_is_not/) , 2024-05-26-0911
```
Hello,
I am trying to create a chatbot using Langchain where I am using RetrievalQA and OpenAI API. I need to create cha
ins where if the user asks a question which is unrelated to the context, basically retrieve from a document provided, th
e chatbot should bypass the retrieval steps and just answer the query directly. And if it asks related questions it shou
ld apply RAG and retrieve the relevant info to answer the questions.
I am totally stuck here and don’t know how to move 
forward. Any help will be appreciated. 

Code:

llm = ChatOpenAI(
    api_key= api_key,  
    # openai_api_key= os.envir
on['OPENAI_API_KEY'],  
    model_name='gpt-4o' 
    
)
template = '''
Use the following context provided (delimited by 
<ctx></ctx>),
answer the questions properly and the chat history (delimited by <hs></hs>) to answer the questions from t
he user. 
If they are asking questions not related to the context, skip performing RAG and just straight up answer their
 query':
------
<ctx>
{context}
</ctx>
------
<hs>
{history}
</hs>
------
{question}
Answer:
'''
prompt = PromptTemplate
(
    input_variables=['history', 'context', 'question'],
    template=template,
)

memory = ConversationBufferMemory(
 
   memory_key='history',
    input_key='question'
)

qa = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type='stuf
f',
    retriever=vectorstore.as_retriever(search_type='similarity', search_kwargs={'k': 20}),
    verbose=True,
    cha
in_type_kwargs={
        'verbose': True,
        'prompt': prompt,
        'memory': memory,
    }
)
```
---

     
 
all -  [ Gemini 1.5 pro and flash ](https://www.reddit.com/r/googlecloud/comments/1d0dzd4/gemini_15_pro_and_flash/) , 2024-05-26-0911
```
Anyone else finding responses are either too verbose or not verbose at all? It seems to miss important points in my retr
ieved documents sometimes and other times just throws everything in. Formatting of gpt4 versus 1.5 pro also seems a litt
le better.
I think flash is comparable (if not a little better than gpt3.5)
Im using vertex ai through langchain tho not
 sure if that is where the issue comes from.
Would appreciate any pointers or ideas of how get better performance out of
 gemini. 
```
---

     
 
all -  [ Artificial Intelligence

Generative AI Agents Developer Contest by NVIDIA and LangChain
Enter to win ](https://i.redd.it/qlqthudt1l2d1.jpeg) , 2024-05-26-0911
```
The push is for LangChain agents, but I think accept other tools.
```
---

     
 
all -  [ Which requirements for manager_llm in CrewAI hierarchical process? ](https://www.reddit.com/r/crewai/comments/1d0cby8/which_requirements_for_manager_llm_in_crewai/) , 2024-05-26-0911
```
I want to implement a CrewAI agent team using a hierarchical process and I want to use for the manager_llm the groq mode
l “mixtral-8x7b-32768”.

For that I want to adapt this code:

from langchain_openai import ChatOpenAI
from crewai import
 Crew, Process, Agent

# Agents are defined with attributes for backstory, cache, and verbose mode
researcher = Agent(
 
   role='Researcher',
    goal='Conduct in-depth analysis',
    backstory='Experienced data analyst with a knack for unc
overing hidden trends.',
    cache=True,
    verbose=False,
    # tools=[]  # This can be optionally specified; defaults
 to an empty list
)
writer = Agent(
    role='Writer',
    goal='Create engaging content',
    backstory='Creative write
r passionate about storytelling in technical domains.',
    cache=True,
    verbose=False,
    # tools=[]  # Optionally 
specify tools; defaults to an empty list
)

# Establishing the crew with a hierarchical process and additional configura
tions
project_crew = Crew(
    tasks=[...],  # Tasks to be delegated and executed under the manager's supervision
    ag
ents=[researcher, writer],
    manager_llm=ChatOpenAI(temperature=0, model='gpt-4'),  # Mandatory for hierarchical proce
ss
    process=Process.hierarchical,  # Specifies the hierarchical management approach
    memory=True,  # Enable memory
 usage for enhanced task execution
)


To this code:

from langchain_openai import ChatOpenAI
from crewai import Crew, P
rocess, Agent

# Agents are defined with attributes for backstory, cache, and verbose mode
researcher = Agent(
    role=
'Researcher',
    goal='Conduct in-depth analysis',
    backstory='Experienced data analyst with a knack for uncovering 
hidden trends.',
    cache=True,
    verbose=False,
    # tools=[]  # This can be optionally specified; defaults to an e
mpty list
)
writer = Agent(
    role='Writer',
    goal='Create engaging content',
    backstory='Creative writer passio
nate about storytelling in technical domains.',
    cache=True,
    verbose=False,
    # tools=[]  # Optionally specify 
tools; defaults to an empty list
)

# Establishing the crew with a hierarchical process and additional configurations
pr
oject_crew = Crew(
    tasks=[...],  # Tasks to be delegated and executed under the manager's supervision
    agents=[re
searcher, writer],

   manager_llm=ChatGroq(temperature=0, model='mixtral-8x7b-32768'),  # Mandatory for hierarchical pr
ocess

    process=Process.hierarchical,  # Specifies the hierarchical management approach
    memory=True,  # Enable me
mory usage for enhanced task execution
)


Will this work with model “mixtral-8x7b-32768”? And with model “LLaMA3 70b”?


(Or with other groq models? See https://console.groq.com/docs/models)


Nothing is mentioned about the requirements for
 the manager_llm in the docs:

https://crewai.com/how-to/Hierarchical/




```
---

     
 
all -  [ Is there anyway to prevent AgentExecutor.astream_events() streaming intermediate steps? ](https://www.reddit.com/r/LangChain/comments/1d0b3zs/is_there_anyway_to_prevent_agentexecutorastream/) , 2024-05-26-0911
```
Hello everyone, need some pointer here.  Is there a way to exclude intermediate steps when streaming the events with Age
ntExecutor? I only want the agent to stream the final output without streaming the intermediate steps (Observations).

S
o I'm using create\_tool\_calling\_agent() to create an agent and passing multiple tools. And one of the tool itself act
ually is using langchain csv agent. When the agent using this particular tool, it start to stream the intermediate obser
vation steps in my chat application, which is weird for my user point of view. I want to exclude all the intermediate st
eps from this tool.

When I was using  langchain==0.1.16, it behave exactly what I wanted, which it won't stream any out
put or intermediate steps from the tool that using langchain csv agent. After I upgrade it to  0.2.1, it started to stre
am intermediate steps.

Here's some example code I have:

    async def chat_stream(...) -> str:
        prompt = ChatPr
omptTemplate.from_messages(...)
        tools = [query_data_from_csv]
        llm = ChatOpenAI(...)
    
        agent =
 create_tool_calling_agent(llm, tools, prompt)
        
        agent_executor = AgentExecutor(agent=agent, tools=tools,
 handle_parsing_errors=True)
    
        
        return agent_executor.astream_events(..., version='v2')
    
    @ to
ol
    def query_data_from_csv(question: str, csv_url: str) -> str:
        '''Tool to query and interact with data in C
SV format.'''
    
        ai_agent = create_csv_agent(
            ChatOpenAI(temperature=0, model='gpt-4-turbo'),
    
        csv_url,
            agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
            return_intermediate_steps=Fal
se
        )
    
        return ai_agent.invoke(question)

Your help is greatly appreciated. Thank you.
```
---

     
 
all -  [ Here's how Notion helps me rock every area of my life ](https://www.reddit.com/r/Notion/comments/1d04zmb/heres_how_notion_helps_me_rock_every_area_of_my/) , 2024-05-26-0911
```
My first post here and I would like to share my small achievement with you all.  
A short backstory, I used to forget ab
out most of the things, no ambition and a lot of mindless scrolling. I had this habit of living in denial. One day, Afte
r hitting my lowest, I decided I want to change the way I live

It started with a simple idea, I am gonna stay active on
 reddit and twitter, up-skill and build a personal brand, then it became completely overwhelming, and I was this close t
o quit.

I am an organisational freak and I was familiar with importance of building a second brain and I decided to mak
e one for myself. This right here, was a game-changer for me, boosting my productivity and desire to grow.

I made 3 dat
abases

Days, Journal, Task and Projects database

Any thought that comes to my mind, I make sure to put it on the Task 
Database. I have configured a button, clicking on it inserts and opens a blank page in task database. This has made me a
 pretty long list of all tasks / thoughts that comes up in my mind. This solves one problem, of me not have to remember 
stuff.

Add Journal, helps me to journal effectively from the same page, I have the whole day at glance.

Then, when I s
tart to plan my next day, I add a record to days database. For this, I have made a template, which shows me a holistic o
verview of my tasks (now, next and later) along with due date. Thanks to Solt Wagner for this GTD template which helped 
me in setting up this template  


[My Peek at Today's Day page](https://preview.redd.it/x40hcac4ei2d1.png?width=890&for
mat=png&auto=webp&s=7f5b837cbd34c1a937038d4188aa195b58275dab)

Then when I have set some time over a weekend, where I go
 through my task database I update properties and relevancy. All this is again configured by a button, so I only have to
 click on it and it updates the properties. (Again Thank You Solt)

For each day, I now do not have to see all the pendi
ng tasks, rather I just see the tasks that I have decided to do today.  


I also have a reosurces and notes database, w
here I store every important link I find on the web using web extension. For any course/study/blog I go through, I make 
sure to write it in my notes database.

&#x200B;

This has honestly contributed a lot to my life and brought peace to my
 mind. I am sharing this so that if others who are there on the same boat as me can take insights and have a space for t
hem.

Thank you for reading.  
If you liked it, please upvote :)
```
---

     
 
all -  [ Has langchain been updated with Gpt4o?  ](https://www.reddit.com/r/LangChain/comments/1d03y7b/has_langchain_been_updated_with_gpt4o/) , 2024-05-26-0911
```
I wanted to know if the chain method and ChatOpenAI from langchain\_openai supports gpt4o image inputs and if there are 
any guides out there showing us how to use it? 
```
---

     
 
all -  [ Connect LLM to SQL database with LangChain SQLChain ](https://i.redd.it/g4rv5w1ach2d1.png) , 2024-05-26-0911
```
My new article about 'Connect LLM to SQL database with LangChain SQLChain'

Link [ https://sahraouis-organization.gitboo
k.io/connect-llm-to-sql-database-with-langchain/ ]

Of course it is not fine-tuned yet to be an expert but he's good eno
ugh
```
---

     
 
all -  [ My debut technical book on Generative AI makes it to O'Reilly & Packt ](https://www.reddit.com/r/developersIndia/comments/1d015lc/my_debut_technical_book_on_generative_ai_makes_it/) , 2024-05-26-0911
```
I'm elated to share that my debut technical book, 'LangChain in your Pocket: Beginner's Guide to Building Generative AI 
Applications using LLMs,' has been re-published by Packt Publications and is now available on the official website of Pa
ckt, Barnes & Noble, and the most coveted, O'Reilly. A big thanks to the community for helping me make it a successful d
ebut.

https://preview.redd.it/6swlem85ah2d1.png?width=1080&format=png&auto=webp&s=9d55a21e7c9cd038536b5a56f31c1beabd804
313

https://preview.redd.it/ehmrmp85ah2d1.png?width=1080&format=png&auto=webp&s=58230b18ce4264c3c1eff32b14751ac06258e15
5


```
---

     
 
all -  [ My LangChain book now available on Packt and O'Reilly ](https://www.reddit.com/r/LangChain/comments/1d00vla/my_langchain_book_now_available_on_packt_and/) , 2024-05-26-0911
```
I'm glad to share that my debut book, '**LangChain in your Pocket: Beginner's Guide to Building Generative AI Applicatio
ns using LLMs,**' has been republished by Packt and is now available on their official website and partner publications 
like O'Reilly, Barnes & Noble, etc. A big thanks for the support! The first version is still available on Amazon

https:
//preview.redd.it/5b0trmcl7h2d1.png?width=1080&format=png&auto=webp&s=6f12126f846d5fc174768628ebc42c9921017687

https://
preview.redd.it/4xdgzk9l7h2d1.png?width=1080&format=png&auto=webp&s=bfe4aac06ce89bff475a415b8c0091f830ba10e3
```
---

     
 
all -  [ How could I just return the final answer from SQL Agent? ](https://www.reddit.com/r/LangChain/comments/1czv6k8/how_could_i_just_return_the_final_answer_from_sql/) , 2024-05-26-0911
```
Im planning to do an endpoint that given a user question it makes the underlying work to get the query and i would like 
to only receive the final answer as im going to show it on a Streamlit chat app. Any idea on how to extract only that?
```
---

     
 
all -  [ Gemini api embedding error with langchain please help ](https://www.reddit.com/r/developersIndia/comments/1czsbmf/gemini_api_embedding_error_with_langchain_please/) , 2024-05-26-0911
```
Does anyone know how to solve error from Gemini api with langchain for embedding. I'm using it to get context from an Ex
cel sheet but I'm facing this error: Deadline Exceeded or this one ValueError: Expected each embedding in the embeddings
 to be a list, got ['Repeated']
```
---

     
 
all -  [ Fresher. Need advice on which role to take in my company ](https://www.reddit.com/r/developersIndia/comments/1czroy7/fresher_need_advice_on_which_role_to_take_in_my/) , 2024-05-26-0911
```
I'm currently an intern at my company. It's a finance company. I work for the tech dept. 

My current intern work is ver
y good and the team is also very supportive. I'm working on LangChain agents and langsmith. 

The problem is. The team I
'm working for does not have an opening. So my company wants me to either apply for a different role in a different team
. I don't find anything attractive. The only openings for freshers are either support or testing roles. 

In my current 
team there's an opening for the testing role but it's under the QE team that's helping my current team. I really liked t
he current work. I don't have any other offers in hand.

Should I join as a tester for the LangChain apis they are build
ing or should I just take a different role or try outside?
```
---

     
 
all -  [ Attempt to be Forward-looking on a New Project ](https://www.reddit.com/r/LangChain/comments/1czronv/attempt_to_be_forwardlooking_on_a_new_project/) , 2024-05-26-0911
```
I'm new to LLMs, but I'm planning to build an application that answers technical questions about my API using a RAG syst
em based on my tech docs (e.g., 'how can I configure the API request to wait for the response and to retry if the reques
t times out?'). To summarize ...Goal: answer technical questions (found in my /docs/ subdirectory) so the user doesn't h
ave to search and dig for it. My Plan:  


1. Setup LangChain (are there any tips or tricks I should keep in mind?)
2. C
onnect to Weaviate (if there's a better VectorDB to use, I'd love recommendations & rationale)
3. Connect to ChatGPT 3.5
 (pls let me know if there's a better model to use)
4. Vectorize my /docs/ directory (I've never done this before, but i
t looks like I need a chunking strategy & embedding model)
5. Create & style a simple modal UI for the chatbot in Airtab
le (again, if there's a better/quicker way to do this, I'm all ears)

I also want to make it not simply a Q&A bot so tha
t if the answer returned is not valid to the user's use case, there is a feedback query used to improve the process, giv
ing the tool either more context or showing where the documentation should be expanded/refined.

Thanks in advance for a
ny guidance and/or pitfalls to avoid :-)
```
---

     
 
all -  [ What evaluation tools/methods do you use? ](https://www.reddit.com/r/LangChain/comments/1czpsmq/what_evaluation_toolsmethods_do_you_use/) , 2024-05-26-0911
```
Looking to understand what evaluation tools/methods people like and use the most?

[View Poll](https://www.reddit.com/po
ll/1czpsmq)
```
---

     
 
all -  [ What should I use to run LLM locally? ](https://www.reddit.com/r/LocalLLaMA/comments/1czny3r/what_should_i_use_to_run_llm_locally/) , 2024-05-26-0911
```
I want to run this artificial intelligence model locally:

    Meta-Llama-3-8B-Instruct.Q5_K_M.gguf

maybe langchain? İd
k

I would be very grateful if you can help me with the sources where I can access sample codes.

The framework or struc
ture I will use should be suitable for preparing APIs in google cloud. so no ollama.

* **Processor**: Intel Core i9-139
80HX
* **Graphics**: NVIDIA GeForce RTX 4070 (140W)
* **RAM**: 64GB DDR5
```
---

     
 
all -  [ Infosys Certified Applied Generative AI Professional Answers List ](https://www.reddit.com/r/infosysuntold/comments/1cznjs0/infosys_certified_applied_generative_ai/) , 2024-05-26-0911
```
Last week, I successfully completed the Infosys Certified Generative AI Professional - Intermediate exam, and I'm thrill
ed to share my experience and some insights with all of you!

📝 During the exam, I encountered a variety of questions th
at tested my knowledge of Contents Covered on Study Materials. I'd be happy to discuss some of the questions covered and
 share tips for preparing for the exam.

**Question ->** Which of the following are key features of LangChain?

Option 1
 -> Provides a standard interface for chain of prompts.
Option 2 -> Integrations with other NLP tools.
Option 3 -> Flexi
bility and Speed
Option 4 -> None of the Above
Correct Solution -> abc

**Question ->** Which of the following statement
s describes the LangChain Chains correctly ?

Option 1 -> LangChain Chains are specifically designed to use Agents.
Opti
on 2 -> LLMchain is an end-to-end wrapper around multiple individual components.
Option 3 -> LangChain Chains take care 
of storing embedded data and performing vector search too.
Option 4 -> LangChain provides the Chain interface to create 
'chained' applications, so as to enable a sequence of calls to components, which can include other chains.
Correct Solut
ion -> bd

**Question ->** What is data poisoning in with respect to Large Language Models(LLMs)?

Option 1 -> The encry
ption of data in LLM systems
Option 2 -> The accidental deletion of data in LLM system
Option 3 -> The unauthorized acce
ss to data in LLM systems
Option 4 -> The intentional manipulation or contamination of data in LLM systems
Correct Solut
ion -> d

**Question ->** What does 'data toxicity' refer to?

Option 1 -> The quality of data in terms of 
accuracy
Opt
ion 2 -> The presence of valuable information 
in a dataset
Option 3 -> Harmful or inappropriate content present 
in the
 data
Option 4 -> Data that is toxic to the 
environment
Correct Solution -> c

**Question ->** What is a key considerat
ion when 
evaluating the performance of large language models using test data?

Option 1 -> The volume of training data

Option 2 -> The number of data hosts
Option 3 -> Whether test data appears in the model's 
training data
Option 4 -> The
 type of input contamination
Correct Solution -> c

**Question ->** What cybersecurity risk is associated with deploying
 LLMs in applications?

Option 1 -> LLMs have no impact on cybersecurity
Option 2 -> LLMs are immune to adversarial atta
cks
Option 3 -> LLMs might be exploited to generate 
convincing phishing emails or malicious code
Option 4 -> LLMs can o
nly generate text on predefined topics
Correct Solution -> c

**Question ->** How is the Perspective API used for 
toxic
ity classification?

Option 1 -> It trains models using toxic content from various sources
Option 2 -> It assigns a toxi
city score to content 
based on its complexity
Option 3 -> It creates a list of slurs and profanity for 
content filteri
ng
Option 4 -> It gives a machine-learning-based 
score to evaluate content toxicity
Correct Solution -> d

**Question -
>** What distinguishes data poisoning 
from data toxicity?

Option 1 -> Data poisoning involves accidental 
introduction
 of harmful content, while data toxicity is a deliberate attack
Option 2 -> Data poisoning occurs when a model 
produces
 incorrect outcomes, while data toxicity affects data collection methods
Option 3 -> Data poisoning is intentional manip
ulation of training data, whereas data toxicity is about the presence of harmful content
Option 4 -> Data poisoning targ
ets text-based models, while data toxicity primarily affects image recognition models
Correct Solution -> c



If you ha
ve new questions Please feel free to add more questions in comments

for all questions latest pdf contact me @ prepfixad
min[Telegram] or visit https://infosys.prepflix.net

Also follow me on Whatsapp for infosys related updates
https://what
sapp.com/channel/0029VaFbeOvC6Zvd2rsGkb10
```
---

     
 
all -  [ Infosys Certified Generative AI Professional - Intermediate Answers List ](https://www.reddit.com/r/infosysuntold/comments/1czncwv/infosys_certified_generative_ai_professional/) , 2024-05-26-0911
```
Last week, I successfully completed the Infosys Certified Generative AI Professional - Intermediate exam, and I'm thrill
ed to share my experience and some insights with all of you!

📝 During the exam, I encountered a variety of questions th
at tested my knowledge of Contents Covered on Study Materials. I'd be happy to discuss some of the questions covered and
 share tips for preparing for the exam.

**Question ->** Which of the following are key features of LangChain?

Option 1
 -> Provides a standard interface for chain of prompts. Option 2 -> Integrations with other NLP tools. Option 3 -> Flexi
bility and Speed Option 4 -> None of the Above Correct Solution -> abc

**Question ->** Which of the following statement
s describes the LangChain Chains correctly ?

Option 1 -> LangChain Chains are specifically designed to use Agents. Opti
on 2 -> LLMchain is an end-to-end wrapper around multiple individual components. Option 3 -> LangChain Chains take care 
of storing embedded data and performing vector search too. Option 4 -> LangChain provides the Chain interface to create 
'chained' applications, so as to enable a sequence of calls to components, which can include other chains. Correct Solut
ion -> bd

**Question ->** What is data poisoning in with respect to Large Language Models(LLMs)?

Option 1 -> The encry
ption of data in LLM systems Option 2 -> The accidental deletion of data in LLM system Option 3 -> The unauthorized acce
ss to data in LLM systems Option 4 -> The intentional manipulation or contamination of data in LLM systems Correct Solut
ion -> d

**Question ->** What does 'data toxicity' refer to?

Option 1 -> The quality of data in terms of accuracy Opti
on 2 -> The presence of valuable information in a dataset Option 3 -> Harmful or inappropriate content present in the da
ta Option 4 -> Data that is toxic to the environment Correct Solution -> c

**Question ->** What is a key consideration 
when evaluating the performance of large language models using test data?

Option 1 -> The volume of training data Optio
n 2 -> The number of data hosts Option 3 -> Whether test data appears in the model's training data Option 4 -> The type 
of input contamination Correct Solution -> c

**Question ->** What cybersecurity risk is associated with deploying LLMs 
in applications?

Option 1 -> LLMs have no impact on cybersecurity Option 2 -> LLMs are immune to adversarial attacks Op
tion 3 -> LLMs might be exploited to generate convincing phishing emails or malicious code Option 4 -> LLMs can only gen
erate text on predefined topics Correct Solution -> c

**Question ->** How is the Perspective API used for toxicity clas
sification?

Option 1 -> It trains models using toxic content from various sources Option 2 -> It assigns a toxicity sco
re to content based on its complexity Option 3 -> It creates a list of slurs and profanity for content filtering Option 
4 -> It gives a machine-learning-based score to evaluate content toxicity Correct Solution -> d

**Question ->** What di
stinguishes data poisoning from data toxicity?

Option 1 -> Data poisoning involves accidental introduction of harmful c
ontent, while data toxicity is a deliberate attack Option 2 -> Data poisoning occurs when a model produces incorrect out
comes, while data toxicity affects data collection methods Option 3 -> Data poisoning is intentional manipulation of tra
ining data, whereas data toxicity is about the presence of harmful content Option 4 -> Data poisoning targets text-based
 models, while data toxicity primarily affects image recognition models Correct Solution -> c

If you have new questions
 Please feel free to add more questions in comments

for all questions latest pdf contact me @ prepfixadmin\[Telegram\] 
or visit [https://infosys.prepflix.net](https://infosys.prepflix.net)

Also follow me on Whatsapp for infosys related up
dates [https://whatsapp.com/channel/0029VaFbeOvC6Zvd2rsGkb10](https://whatsapp.com/channel/0029VaFbeOvC6Zvd2rsGkb10)
```
---

     
 
all -  [ I'm sure we can implement Function Calling ](https://www.reddit.com/r/Oobabooga/comments/1czmsf3/im_sure_we_can_implement_function_calling/) , 2024-05-26-0911
```
Hi,

I started a PoC some time ago, i try to implement function calling in textgen but I'm stuck because of the format o
f the json returned in response.

Here is my understanding of how function calling works and how I try to make it work i
n textgen:

* the model receives the list of function/tools in the dedicated block in the form of a json
* I inject this
 json with a small explanatory prompt: 'here are the available functions \[...\], use them if necessary. Answer with jso
n syntax '{'name': 'functionName', 'arguments': '{ 'arg1': 'value' } '}'
* then when the model follows the syntax and re
quests a function's result, I want to return the json which will be processed by the backend to evaluate the function an
d return the result.

My implementation almost works but the returned JSON seems to be converted into JSON again and the
 syntax is no longer correct, from what I understand I lost escaped quotes or I have too many quote, I don't know... (la
ngchain crash because of input format)

Here is the code used, I'm not a python developer and I'm not sure what I'm doin
g but I think the idea is there: [https://gist.github.com/gloic/cf3002fc247be7549f893bde69b0a038](https://gist.github.co
m/gloic/cf3002fc247be7549f893bde69b0a038) See lines \~215 for the prompt injection and lines \~390 for the return.

Is t
he approach correct ? Did someone already tried this ?
```
---

     
 
all -  [ # Supabase Auth with SSR: AI Integration and Chat Enhancements 🚀 ](https://www.reddit.com/r/nextjs/comments/1czi13m/supabase_auth_with_ssr_ai_integration_and_chat/) , 2024-05-26-0911
```
I've updated my project that combines Supabase's SSR authentication with Next.js 14 and Material-UI. This release focuse
s on AI integration, chat improvements, and user experience enhancements. The project is designed with simplicity in min
d, making it easy for beginners to understand and build upon.

## Core Technologies

- **Supabase Authentication**: Secu
re your app with Supabase's authentication system.
- **Next.js 14 with Server-Side Rendering**: Improve performance and 
SEO with Next.js 14's SSR.
- **Material-UI Styling**: Create a responsive UI using Material-UI components.

## AI-Powere
d Chat

- **Vercel AI Integration**: Enable intelligent chat interactions with Vercel's AI package.
- **OpenAI's ChatGPT
**: Engage in natural language conversations with ChatGPT.
- **Claude AI Opus**: Expand chat capabilities with Claude AI
 Opus.

## Chat Enhancements

- **Upstash Redis for Chat History**: Store and retrieve chat history efficiently with Ups
tash Redis.
- **Mobile-Friendly Chat Interface**: Enjoy a responsive chat interface on desktop and mobile.
- **Swipeable
 Chat List Drawers**: Navigate chats easily with swipeable drawers on mobile.
- **Abort Signal Handling**: Cancel ongoin
g chat requests gracefully.
- **Partial Chat Save**: Minimize data loss with a robust partial chat save mechanism.

## U
ser Experience Improvements

- **Modern Authentication Pages**: Intuitive design for sign-in, sign-up, and password rese
t pages.
- **React Server Components**: Optimize data fetching and rendering for faster load times.
- **Markdown Support
**: Enhanced readability with Perplexity and code highlighting.
- **Server Actions for Mutations**: Perform server-side 
mutations securely using server actions.

## Get Started

Explore the project and code at [SupabaseAuthWithSSR](https://
github.com/electriccodeguy/supabaseauthwithssr) on GitHub. Provide feedback, suggest improvements, or contribute.


##Co
ming next: 
**Implement a similar Chat functionality using the new ai/rsc from Vercel**: This includes usable chat histo
ry, tools and functions implementation with live response UI.


**EDIT**: In the latest release (v1.3.0), I've made some
 changes to streamline the AI integration and improve performance:

1. **Migrated from Langchain to Vercel AI SDK**: The
 Vercel AI SDK provides a more straightforward approach to integrating AI models, reducing complexity in the codebase. T
his change simplifies the code and makes it easier to maintain and extend.

2. **Removed Langchain Dependency**: As a re
sult of the migration to Vercel AI SDK, the Langchain dependency has been removed. This further simplifies the codebase 
and reduces unnecessary complexity. For reference, an example of the previous Langchain integration can be found in the 
`exampleWithLangchain.md` file in the Root folder.

3. **Memoized Message Component**: To optimize performance, especial
ly in scenarios with large amounts of messages and frequent updates (such as streaming), I've implemented memoization fo
r the `Message` component using `React.memo`. This prevents unnecessary re-renders of the component when its props remai
n unchanged, improving overall performance.
```
---

     
 
all -  [ AI Agent for monitoring Snowflake Costs! ](https://www.reddit.com/r/LangChain/comments/1czfe4s/ai_agent_for_monitoring_snowflake_costs/) , 2024-05-26-0911
```
Hey folks! My team recently worked on building this bot to help orgs monitor and even forecast costs on the Snowflake Da
ta Warehouse. We used LangChain, Streamlit, Snowflake Arctic + Cortex and GPT 4 Turbo for this. 

We just open sourced t
his Agent and even wrote a guide on how to create one yourself, check it out here: [https://medium.com/snowflake/crystal
costs-building-an-ai-agent-for-cost-monitoring-on-snowflake-c9d49645f5c4](https://medium.com/snowflake/crystalcosts-buil
ding-an-ai-agent-for-cost-monitoring-on-snowflake-c9d49645f5c4)

Would love to get inputs on this! 
```
---

     
 
all -  [ # Supabase Auth with SSR: AI Integration and Chat Enhancements 🚀 ](https://www.reddit.com/r/Supabase/comments/1czeylu/supabase_auth_with_ssr_ai_integration_and_chat/) , 2024-05-26-0911
```
I've updated my project that combines Supabase's SSR authentication with Next.js 14 and Material-UI. This release focuse
s on AI integration, chat improvements, and user experience enhancements. The project is designed with simplicity in min
d, making it easy for beginners to understand and build upon.

## Core Technologies

- **Supabase Authentication**: Secu
re your app with Supabase's authentication system.
- **Next.js 14 with Server-Side Rendering**: Improve performance and 
SEO with Next.js 14's SSR.
- **Material-UI Styling**: Create a responsive UI using Material-UI components.

## AI-Powere
d Chat

- **Vercel AI Integration**: Enable intelligent chat interactions with Vercel's AI package.
- **OpenAI's ChatGPT
**: Engage in natural language conversations with ChatGPT.
- **Claude AI Opus**: Expand chat capabilities with Claude AI
 Opus.

## Chat Enhancements

- **Upstash Redis for Chat History**: Store and retrieve chat history efficiently with Ups
tash Redis.
- **Mobile-Friendly Chat Interface**: Enjoy a responsive chat interface on desktop and mobile.
- **Swipeable
 Chat List Drawers**: Navigate chats easily with swipeable drawers on mobile.
- **Abort Signal Handling**: Cancel ongoin
g chat requests gracefully.
- **Partial Chat Save**: Minimize data loss with a robust partial chat save mechanism.

## U
ser Experience Improvements

- **Modern Authentication Pages**: Intuitive design for sign-in, sign-up, and password rese
t pages.
- **React Server Components**: Optimize data fetching and rendering for faster load times.
- **Markdown Support
**: Enhanced readability with Perplexity and code highlighting.
- **Server Actions for Mutations**: Perform server-side 
mutations securely using server actions.

## Get Started

Explore the project and code at [SupabaseAuthWithSSR](https://
github.com/electriccodeguy/supabaseauthwithssr) on GitHub. Provide feedback, suggest improvements, or contribute.


**ED
IT**: In the latest release (v1.3.0), I've made some changes to streamline the AI integration and improve performance:


1. **Migrated from Langchain to Vercel AI SDK**: The Vercel AI SDK provides a more straightforward approach to integrati
ng AI models, reducing complexity in the codebase. This change simplifies the code and makes it easier to maintain and e
xtend.

2. **Removed Langchain Dependency**: As a result of the migration to Vercel AI SDK, the Langchain dependency has
 been removed. This further simplifies the codebase and reduces unnecessary complexity. For reference, an example of the
 previous Langchain integration can be found in the `exampleWithLangchain.md` file in the Root folder.

3. **Memoized Me
ssage Component**: To optimize performance, especially in scenarios with large amounts of messages and frequent updates 
(such as streaming), I've implemented memoization for the `Message` component using `React.memo`. This prevents unnecess
ary re-renders of the component when its props remain unchanged, improving overall performance.
```
---

     
 
all -  [ Internet search for ai agent only returning a short snippet  ](https://www.reddit.com/r/AI_Agents/comments/1czdxnh/internet_search_for_ai_agent_only_returning_a/) , 2024-05-26-0911
```
Hey I gave the ai agent which I made on crewai the ability to search internet using serper api but it is only giving a s
hort snippet while I want the full content from the websites , I think I might need a web scrapper like firecrawl but ho
w do I make a custom tool for that like do I tell the model to store the urls in a list but how can it store In a list a
nd can a tool made with langchain  work with crewai , plus if you can suggest a video that gives a tutorial for making t
ools for beginners that helped you in making tools
```
---

     
 
all -  [ LangGraph Essentials: Create Your First Graph with Ease! ](https://www.reddit.com/r/LangChain/comments/1czdcpz/langgraph_essentials_create_your_first_graph_with/) , 2024-05-26-0911
```
[https://youtu.be/gflsu\_6R\_8g](https://youtu.be/gflsu_6R_8g)
```
---

     
 
all -  [ How I got the DDGS, Exa, Serper, SerAPI searches working. ](https://www.reddit.com/r/crewai/comments/1czb1qz/how_i_got_the_ddgs_exa_serper_serapi_searches/) , 2024-05-26-0911
```
No one has been able to explain why the search tools DDGS, Exa, and SerpAPI never worked, and Serper rarely worked. Whil
e suggestions to change my LLM and bump my tokens were good, that only made things worse. I looked into it more, and thi
s is what I have now, which works. I am posting this in case others have the same problem.

I replaced all the CrewAI se
arch classes with longchain, like this...

    from crewai_tools import Tool
    
    gput('searcher','DDG') # gput,gget
 writes and reads sysem env variables, a 'dotenv' wrapper.
    
    search_name = 'Search'
    search_desc = 'useful for
 when you need to answer questions about current events'
    
    if gget('searcher') == 'EXA':
        print(f'Using Se
arch API: EXA')
        from src.news.lib.exa_search_tool import ExaSearchToolFull
        search_tool = Tool(name=searc
h_name, description=search_desc, func=ExaSearchToolFull._exa().search)
    
    if gget('searcher') == 'DDG':  # still g
et ratelimit error
        from langchain_community.utilities import DuckDuckGoSearchAPIWrapper
        search = DuckDuc
kGoSearchAPIWrapper()
        search.region='us-en'
        search.safesearch='off'
        search.backend='html' # back
end: api, html, lite.
        # search.max_results=1 # even with only 1 query it fails with RateLimit :/
        search_
tool = Tool(name=search_name, description=search_desc, func=search.run, query='Red Heffer')
    
    if gget('searcher')
 == 'SER':
        print(f'Using Search API: SER')
        from langchain_community.utilities import GoogleSerperAPIWrap
per
        search = GoogleSerperAPIWrapper(params={'engine': 'bing','gl': 'us','hl': 'en'})
        search_tool = Tool(
name=search_name, description=search_desc, func=search.run)
    
    if gget('searcher') == 'SAP': # defaults to SAP
   
     print(f'Using Search API: SAP')
        print('>>>',gget('SERPAPI_API_KEY'))
        from langchain_community.utili
ties import SerpAPIWrapper
        search = SerpAPIWrapper(params={'engine': 'bing','gl': 'us','hl': 'en'})
        from
 crewai_tools import Tool
        search_tool = Tool(name=search_name, description=search_desc,func=search.run)

This wo
rks great for all but DDGS.  To get that to work, I commented out

                # if _is_500_in_url(str(resp.url)) or
 resp.status_code == 202:
                #     raise DuckDuckGoSearchException('Ratelimit')

in `site-packages/duckduck
go_search/duckduckgo_search_async.py` (around lines 50-60).

Just below  added a `sleep(1)` just in case the rate limit 
was actually real (which it appears not to be).

                if resp.status_code == 200:
                    import 
time
                    time.sleep(1)
                    return resp_content

And  added the parameter `search.backend
='html'`  (see the code above), which made a huge difference.  When is the default, `search.backend='api'` it kept repor
ting  `No good result on DuckDuckGo found`, but with `'html'` it found and returned content.

Here's the standard Exa cl
ass being used.

    from crewai_tools import tool
    from exa_py import Exa
    from src.news.lib.utils import gget # 
this is mine.  Can be replaced with os.environ['VAR']
    import dotenv
    dotenv.load_dotenv(dotenv_path='/src/crewai/
.env')
    class ExaSearchToolFull:
        @tool
        def search(query: str):
            '''Search for a webpage ba
sed on the query.'''
            return ExaSearchToolFull._exa().search(
                f'{query}', use_autoprompt=True
, num_results=3
            )
    
        @tool
        def find_similar(url: str):
            '''Search for webpages 
similar to a given URL.
            The url passed in should be a URL returned from `search`.
            '''
          
  return ExaSearchToolFull._exa().find_similar(url, num_results=3)
    
        @tool
        def get_contents(ids: str)
:
            '''Get the contents of a webpage.
            The ids must be passed in as a list, a list of ids returned 
from `search`.
            '''
    
            print('ids from param:', ids)
    
            ids = eval(ids)
         
   print('eval ids:', ids)
    
            contents = str(ExaSearchToolFull._exa().get_contents(ids))
            print
(contents)
            contents = contents.split('URL:')
            contents = [content[:1000] for content in contents]

            return '\n\n'.join(contents)
    
        def tools():
            return [
                ExaSearchToolFu
ll.search,
                ExaSearchToolFull.find_similar,
                ExaSearchToolFull.get_contents,
            ]

        def _exa():
            return Exa(api_key=gget('EXA_API_KEY'))
```
---

     
 
all -  [ Vector Embedding and RAG Platforms ](https://www.reddit.com/r/LangChain/comments/1cz9zga/vector_embedding_and_rag_platforms/) , 2024-05-26-0911
```
Hey all, looking to learn :)

What are some good robust platforms that I can use to vectorize various types of data and 
implement RAG to generate results from LLMs? I have a few projects I am working on each with their own types of data and
 models to use. Wondering if there are any all-in-one platforms you know of that would limit my time spent learning new 
technologies that will have to be updated as the methods progress. Thanks!
```
---

     
 
all -  [ Caching in LLM Apps ](https://www.reddit.com/r/LangChain/comments/1cz3ls8/caching_in_llm_apps/) , 2024-05-26-0911
```
Which is your favourite caching technique in LLM Applications. 
Is it in memory or something else.
Which caching integra
tion you like the most and why for a scalable and reliable application.
```
---

     
 
all -  [ ReAct Agent with 0.3 instruct ](https://www.reddit.com/r/MistralAI/comments/1cz2gbb/react_agent_with_03_instruct/) , 2024-05-26-0911
```
Hi upgraded my Langchain ReAct agent with the new 0.3 model that dropped yesterday and wow!

it's faster, more determini
stic, and tool calling is much better.

Haven't tried out the new functions yet since I have no idea how to implement th
is in my framework.

Any tips?

Also, if you have a good prompt to ensure that the agent visits a website is the link is
 provided would be great.
```
---

     
 
all -  [ Is there a better way to get this json into my vectordb? (ollama, chromadb, gp4allembeddings) ](https://www.reddit.com/r/LocalLLaMA/comments/1cz1e2f/is_there_a_better_way_to_get_this_json_into_my/) , 2024-05-26-0911
```
I've been working on a simple chatbot, it responds to inquiries in intercom and in telegram. It makes a database of info
rmation to pull from based on current support articles in Intercom. It worked pretty well with 150 articles, but as I've
 added more and its up to almost 400 it seems to completely miss easy questions now, and I feel like i'm not ingesting a
ll that information in the most efficient way possible.

 It uses Ollama/Llama3 for the model, i have a custom modelfile
 that  looks like:
> FROM llama3
> 
> PARAMETER temperature 0.3
> 
> SYSTEM You are a helpful AI assistant for the 'X' p
latform. Your role is to provide detailed, accurate answers to user questions based on the information in your knowledge
 base, with the goal of assisting users without requiring a human response when possible. If a question can have multipl
e answers depending on the situation, provide guidance on the different options. When giving instructions, be as specifi
c as possible. Never answer questions that are remotely off-topic. Just let them know you can’t help with that.

It uses
 gpt4allembeddings/langchain for embedding and chromadb for the database.

I have a pre-prompt implemented that reads li
ke:
> Answer the question based on the provided context. Do not include introductory phrases. If the question is unclear
 or unrelated to the context, simply state 'I apologize, I can't help with your query, let me get a team member to assis
t.' Do not provide additional explanations.

The json that intercom is providing looks like this:
>         [
>         
  {
>             'id': '123',
>             'type': 'article',
>             'workspace_id': '123',
>             'pare
nt_id': null,
>             'parent_type': null,
>             'parent_ids': [],
>             'title': 'Title',
>      
       'description': 'Description',
>             'body': 'Body',
>             'author_id': 123,
>             'state'
: 'draft',
>             'created_at': 171,
>             'updated_at': 171,
>             'url': null
>           },
> 
          {
>             'id': '234',
>             'type': 'article',
>             'workspace_id': '234',
>          
   'parent_id': null,
>             'parent_type': null,
>             'parent_ids': [],
>             'title': 'Title',

>             'description': 'Description',
>             'body': 'Body',
>             'author_id': 123,
>            
 'state': 'draft',
>             'created_at': 171,
>             'updated_at': 171,
>             'url': null
>        
   },
>     
Here is my script please dont judge i'm an absolute hobbyist and this is my first time trying to dive into 
AI stuff:

    import json
    import logging
    import os
    import aiohttp
    import asyncio
    from dotenv import
 load_dotenv
    from quart import Quart, jsonify, request
    from telethon import TelegramClient, events
    from tele
thon.errors import RPCError, ChatAdminRequiredError, ChannelPrivateError
    from telethon.tl.types import PeerChannel
 
   from langchain_community.vectorstores import Chroma
    from langchain_community.embeddings import GPT4AllEmbeddings

    from langchain_core.prompts import PromptTemplate
    from langchain_community.llms import Ollama
    from langchain
.callbacks.manager import CallbackManager
    from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHa
ndler
    from langchain.chains import RetrievalQA
    from langchain.docstore.document import Document
    from hyperco
rn.config import Config
    from hypercorn.asyncio import serve
    import time
    
    os.makedirs('logs', exist_ok=Tr
ue)
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s', handlers=[
        logging.FileHandl
er('logs/app.log'),
        logging.StreamHandler()
    ])
    
    start_time = time.time()
    
    # .env
    load_do
tenv()
    api_id = os.getenv('API_ID')
    api_hash = os.getenv('API_HASH')
    bot_token = os.getenv('BOT_TOKEN')
    
intercom_token = os.getenv('INTERCOM_TOKEN')
    chat_id = int(os.getenv('CHAT_ID'))
    qa_chain_prompt_template = os.g
etenv('QA_CHAIN_PROMPT_TEMPLATE')
    
    app = Quart(__name__)
    
    client = TelegramClient('logs/tg_chat', api_id
, api_hash)
    
    vectorstore = None
    qa_chain = None
    
    QA_CHAIN_PROMPT = PromptTemplate(
        input_var
iables=['context', 'question'],
        template=qa_chain_prompt_template,
    )
    
    llm = Ollama(model='llama3-tem
p03', callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]))
    
    async def fetch_all_pages():
      
  url = 'https://api.intercom.io/articles'
        headers = {
            'Authorization': f'Bearer {intercom_token}',

            'Accept': 'application/json'
        }
        all_documents = []
        all_data = []
        async with a
iohttp.ClientSession() as session:
            while url:
                async with session.get(url, headers=headers) a
s response:
                    if response.status != 200:
                        logging.error(f'Failed to fetch data:
 {response.status}')
                        break
                    data = await response.json()
                    
all_data.extend(data.get('data', []))
                    if 'data' in data and data['data']:
                        do
cuments = [Document(page_content=article['body']) for article in data['data'] if article['body'].strip()]
              
          all_documents.extend(documents)
                    url = data.get('pages', {}).get('next', None)
        with
 open('info.json', 'w') as f:
            json.dump(all_data, f, indent=2)
        logging.info(f'Total records received
: {len(all_data)}')
        return all_documents
    
    async def rebuild_vectorstore():
        global documents, vec
torstore, qa_chain
        try:
            documents = await fetch_all_pages()
            if documents:
              
  vectorstore = Chroma.from_documents(documents=documents, embedding=GPT4AllEmbeddings())
                logging.info('
Documents processed and vector store rebuilt.')
                qa_chain = RetrievalQA.from_chain_type(
                
    llm,
                    retriever=vectorstore.as_retriever(),
                    chain_type_kwargs={'prompt': QA_C
HAIN_PROMPT},
                )
            else:
                logging.error('No valid documents with non-empty body 
found.')
        except Exception as e:
            logging.error(f'Error rebuilding vector store: {str(e)}')
    
    a
sync def handle_query(query):
        if qa_chain is None:
            logging.error('QA chain is not initialized.')
   
         return {'response': 'Initialization error: Vector store not available. Check log for details.', 'time_taken': 0
}
    
        start_time = time.time()
        try:
            result = qa_chain.invoke(query)
        except Exceptio
n as e:
            logging.error(f'Error during query handling: {str(e)}')
            return {'response': 'An error oc
curred while processing the query.', 'time_taken': 0}
    
        end_time = time.time()
        time_taken = end_time 
- start_time
    
        logging.info(f'Query result: {result}')
    
        if isinstance(result, dict):
            
result = result.get('result', 'No result field found in response.')
        elif isinstance(result, str):
            re
sult = result.strip()
        else:
            result = str(result).strip()
    
        if not result:
            res
ult = 'I apologize, but I don't have enough information to provide a helpful answer.'
    
        return {'response': r
esult, 'time_taken': time_taken}
    
    @app.route('/intercom', methods=['POST'])
    async def intercom_handler():
  
      data = await request.get_json()
        query = data.get('body')
        if query:
            result = await hand
le_query(query)
            response = result['response']
            time_taken = result['time_taken']
            retu
rn jsonify({'response': response, 'time_taken': time_taken}), 200
        else:
            logging.error('No query prov
ided in the request')
            return jsonify({'error': 'No query provided'}), 400
    
    @app.route('/rebuild_vect
orstore', methods=['POST'])
    async def rebuild_vectorstore_handler():
        await rebuild_vectorstore()
        ret
urn jsonify({'message': 'Vector store rebuilt'}), 200
    
    @client.on(events.NewMessage(pattern=r'^\.x (.+)', func=l
ambda e: e.text.lower().startswith('.x ')))
    async def answer_query(event):
        query = event.pattern_match.group
(1)
        logging.info(f'Received query: {query}')
        result = await handle_query(query)
        response = resul
t['response']
        time_taken = result['time_taken']
        await event.respond(f'```{response}```\n**Time to genera
te: {time_taken:.2f} seconds**', parse_mode='Markdown')
    
    @client.on(events.NewMessage(pattern='/rebuild'))
    a
sync def rebuild_vectorstore_command(event):
        logging.info('Received /rebuild command. Rebuilding the vector stor
e...')
        await event.respond('Rebuilding database...')
        await rebuild_vectorstore()
        await event.res
pond('Database rebuilt.')
    
    async def run_server():
        global start_time
        config = Config()
        c
onfig.bind = ['0.0.0.0:5001']
        
        async def custom_serve():
            end_time = time.time()
            
time_to_boot = end_time - start_time
            await send_message(chat_id, f'<span style='color:red'>Bot Online, Time 
to boot: {time_to_boot:.2f} seconds</span>')
            await serve(app, config)
    
        await custom_serve()
    

    async def send_message(chat_id, message):
        try:
            entity = await client.get_entity(PeerChannel(cha
t_id))
            await client.send_message(entity, message, parse_mode='html')
        except ChatAdminRequiredError:

            logging.error(f'Failed to send message to {chat_id}: Bot lacks admin rights.')
        except ChannelPrivate
Error:
            logging.error(f'Failed to send message to {chat_id}: Channel is private.')
        except RPCError as
 e:
            logging.error(f'Failed to send message to {chat_id}: {str(e)}')
    
    async def start():
        try:

            await client.start(bot_token=bot_token)
            logging.info('Telegram client connected.')
            
await rebuild_vectorstore()
            await run_server()
        except Exception as e:
            logging.error(f'Er
ror occurred: {str(e)}. Retrying in 5 seconds...')
            await asyncio.sleep(5)
            await start()
    
   
 async def main():
        try:
            await start()
        except KeyboardInterrupt:
            logging.info('Sc
ript interrupted by user.')
            await send_message(chat_id, '<span style='color:red'>Shutting Down</span>')
    
    finally:
            logging.info('Shutting down...')
            await client.disconnect()
            logging.info
('Client disconnected.')
            pending = [task for task in asyncio.all_tasks() if not task.done() and task is not 
asyncio.current_task()]
            for task in pending:
                task.cancel()
            await asyncio.gather(
*pending, return_exceptions=True)
            loop.stop()
            loop.close()
            logging.info('Script stop
ped.')
    
    if __name__ == '__main__':
        try:
            loop = asyncio.get_event_loop()
            loop.run
_until_complete(main())
        except RuntimeError as e:
            logging.error(f'Runtime error: {str(e)}')
        
finally:
            if not loop.is_closed():
                loop.close()


I'm not sure if i am embedding the json cor
rectly, i thought it would be straightforward in json format but the bad outputs make me second guess whatever im doing,
 really open to whatever, would love to learn what im missing here
```
---

     
 
all -  [ why two different kinds of messages? ](https://www.reddit.com/r/LangChain/comments/1cyz7kw/why_two_different_kinds_of_messages/) , 2024-05-26-0911
```
langchain\_core.messages.human.HumanMessage

langchain.schema.messages.HumanMessage

I got unsupported HumanMessage erro
r when using langchain and found out two kinds of messages. Why?
```
---

     
 
all -  [ [11 YOE] Unable To Get Any Tech Interviews With This Resume, What Am I Doing Wrong? ](https://www.reddit.com/r/resumes/comments/1cyyw3b/11_yoe_unable_to_get_any_tech_interviews_with/) , 2024-05-26-0911
```
https://preview.redd.it/gt05zrf5r72d1.png?width=5100&format=png&auto=webp&s=0745fdbb4f38cd6b4aa6c0104bb949b857496d8a

ht
tps://preview.redd.it/n8c7z5i5r72d1.png?width=5100&format=png&auto=webp&s=71660c9f380f4eb752fc854cbf66d0b6a5082472

http
s://preview.redd.it/zhfi8uf5r72d1.png?width=5100&format=png&auto=webp&s=769140b50f0755620be916931ba43199240f576b

I am o
pen to roles in AI/ML, Backend Full stack, SWE and Product roles, but cant seem to get interview calls, what am I doing 
wrong? I have been suggested to include the exact tech work I did to avoid looking inexperienced, and hence ended up add
ing a lot of tech jargon, could it be that? Please suggest me fixes. What am I doing wrong?  

```
---

     
 
all -  [ [11 YOE] I have Tech and Tech management experience in startups, but cant get an interview. ](https://www.reddit.com/r/EngineeringResumes/comments/1cyyiyu/11_yoe_i_have_tech_and_tech_management_experience/) , 2024-05-26-0911
```
I have been looking for AI/ML, Backend Full stack, SWE and Product roles but cant seem to get interview calls, what am I
 doing wrong? I have been suggested to include the exact tech work I did to avoid looking inexperienced, and hence ended
 up adding a lot of tech jargon. Please suggest me fixes.

https://preview.redd.it/n5cvga0go72d1.png?width=5100&format=p
ng&auto=webp&s=ee684cb4d88cc4569ad8c81fa643a928e3d80e21

https://preview.redd.it/4qkfva0go72d1.png?width=5100&format=png
&auto=webp&s=9c99b53b0164cfa1577f0d69544cb3c4058535d2

https://preview.redd.it/f7fy850go72d1.png?width=5100&format=png&a
uto=webp&s=69e881cfc736d8856a65fe6160c5ee6f23821ba7


```
---

     
 
MachineLearning -  [ [R] Building an Observable arXiv RAG Chatbot with LangChain, Chainlit, and Literal AI ](https://www.reddit.com/r/MachineLearning/comments/1crwh0q/r_building_an_observable_arxiv_rag_chatbot_with/) , 2024-05-26-0911
```
Hey r/MachineLearning, I published a new article where I built an observable semantic research paper application.

This 
is an extensive tutorial where I go in detail about:

1. Developing a RAG pipeline to process and retrieve the most rele
vant PDF documents from the arXiv API.
2. Developing a Chainlit driven web app with a Copilot for online paper retrieval
.
3. Enhancing the app with LLM observability features from Literal AI.

You can read the article here: [https://medium.
com/towards-data-science/building-an-observable-arxiv-rag-chatbot-with-langchain-chainlit-and-literal-ai-9c345fcd1cd8](h
ttps://medium.com/towards-data-science/building-an-observable-arxiv-rag-chatbot-with-langchain-chainlit-and-literal-ai-9
c345fcd1cd8)

Code for the tutorial: [https://github.com/tahreemrasul/semantic\_research\_engine](https://github.com/tah
reemrasul/semantic_research_engine)


```
---

     
 
MachineLearning -  [ [P] LLMinator: A Llama.cpp + Gradio based opensource Chatbot to run llms locally(cpu/cuda) directly  ](https://www.reddit.com/r/MachineLearning/comments/1cpbgd1/p_llminator_a_llamacpp_gradio_based_opensource/) , 2024-05-26-0911
```
Hi I am currently working on a context-aware streaming chatbot based on Llama.cpp, Gradio, Langchain, Transformers. LLMi
nator can pull LLMs directly from HF & run them locally on cuda or cpu.

I am looking for recommendations & help from op
ensource community to grow this further.

**Github Repo:** [https://github.com/Aesthisia/LLMinator](https://github.com/A
esthisia/LLMinator)

**Goal:** To help developers with kickstarter code/tool to run LLMs.

https://preview.redd.it/fnzja
7rjwqzc1.png?width=1846&format=png&auto=webp&s=a62c43614d63e82156fef8722b986b051cc1795b

**Features:**

* Context-aware 
Chatbot.
* Inbuilt code syntax highlighting.
* Load any LLM repo directly from HuggingFace.
* Supports both CPU & Cuda m
odes.
* Load & Offload saved models.
* Command Line Args
* API Access(Soon to be available)

Any review or feedback is a
ppreciated.
```
---

     
