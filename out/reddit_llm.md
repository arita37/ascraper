 
all -  [ Cara got scammed by their hosting provider ](https://www.reddit.com/r/aiwars/comments/1daqkjo/cara_got_scammed_by_their_hosting_provider/) , 2024-06-08-0953
```
There's pretty much no way a website with only 650K users (not very many) that only hosts images (doesn't take much spac
e) has operating costs of $100K/m. I find it hard to believe this would even exceed $1K/m. This exposes their hosting pr
ovider Vercel of being a complete scam. 

https://preview.redd.it/jjoocn8lt85d1.png?width=1174&format=png&auto=webp&s=d1
d38e20d21b71105b8f7f133e6b1dc7e31dd816

To make matters worse it seems they are hosting it in the lion's den since this 
host is used by so many AI companies. I hope Cara is aware of that. 

https://preview.redd.it/4n22qhkxu85d1.png?width=22
70&format=png&auto=webp&s=7563c32e4288169e5e8a9d41631968a6688b5a81

If it were me I would switch providers ASAP and remo
ve all payment info from this site, they would never see a single dime of that $100K 😂
```
---

     
 
all -  [ Using local LLMs for Agent based systems ](https://www.reddit.com/r/AI_Agents/comments/1daofe6/using_local_llms_for_agent_based_systems/) , 2024-06-08-0953
```
I am currently closely working with LLMs and just started building some solutions using crew.ai and autogen. Not happy s
o far, like sometimes it's really hard to predict the flow of the agent and guarantee the result.

After having some pre
tty stable solutions I decided to try some local LLMs like llama3, phi3, mistral. And it appears that working with Tools
 (like autogen tools, or langchains tools) almost impossible. 

Please share your experience in working with such stack 
and having good results. (or bad ones)
```
---

     
 
all -  [ Create_SQL_Agent ](https://www.reddit.com/r/ollama/comments/1danurh/create_sql_agent/) , 2024-06-08-0953
```
I’m using langchain to create a sql agent. Needs to create a query, execute it, then use the output to answer the questi
on. 

It keeps getting stuck on the creating SQL part - it’s leaving off the last character. Example:

Select * from tab
le where ID =‘1234
(Will leave off the closing string)

The sql_db_query will tell the agent there’s an error and provid
e the correct query with the last character, however the agent will then again leave off the last character and the neve
r ending loop will continue…

Agent:
Agent_executor = create_sql_agent(
llm=model,
Toolkit=toolkit,
Verbose=true,
Handle
_parding_errors = True,
Agent_type=AgentType.Zero_Shot_React_Description,
Return_intermediate_steps=true)

Anyone know w
hy it’s doing this? 
```
---

     
 
all -  [ How are people processing PDFs, and how well is it working? ](https://www.reddit.com/r/LangChain/comments/1danr71/how_are_people_processing_pdfs_and_how_well_is_it/) , 2024-06-08-0953
```
We build a RAG search engine for Payroll companies. We ended up having to handle a bunch of PDF data, some of which had 
1000+ pages per document. We ended up building a parser and search engine entirely based around document layout analysis
 for ourselves. We started chatting with another AI startup that was about to add PDFs to their pipeline (they'd been in
gesting HTML and markdown) and ended up exposing our PDF processing as an API for them. So, now we're trying to figure o
ut if that was a fluke, or if there's something valuable there. 

I'd really love to learn more about how people are man
aging PDFs, and how well it's working for them. Is vector search + text chunking enough? Are folks using Layout Analysis
 tools or building your own in house? Have people had luck with semantic chunking?
```
---

     
 
all -  [ Need advice on what's missing in my profile ? ](https://www.reddit.com/r/Resume/comments/1danaco/need_advice_on_whats_missing_in_my_profile/) , 2024-06-08-0953
```
[redacted resume](https://preview.redd.it/8l2u4unv285d1.png?width=655&format=png&auto=webp&s=a8c6a6b82d5f7ebb97295e8c0b4
f7681d5e45229)

I am a senior year college student from a tier 1 engineering college in India, have been really trying f
or MLE/Data Science/Research Engineer(in NLP domain) full time roles, but luck has not been on my side for a long time(o
r, maybe lack or practice). Experience wise, I've been part of academia and startup setting(plus president of student cl
ub on campus), but have a lot of difficulty in finding full time roles. I love just building stuff and researching thing
s(you can see that in my projects!), but it really is demotivating to not convert leads. I would really love an honest f
eedback, and maybe directions so that I can work on my shortcomings.   
```
---

     
 
all -  [ I Won a Gen AI Hackathon with a 10k USD prize thanks to llm side hustle!!! 1 of 150 participants (it ](https://www.reddit.com/r/LocalLLM/comments/1dakx5v/i_won_a_gen_ai_hackathon_with_a_10k_usd_prize/) , 2024-06-08-0953
```
Just basic proof that getting into LLMs is super beneficial, there is loads of low hanging fruits.

I developed 2 tools,
 in the first one I am working to applying langchain, and the second one I built thanks to langchain, from scratch.

Her
e is the LinkedIn Post

[https://www.linkedin.com/feed/update/urn:li:activity:7204882941972291586/](https://www.linkedin
.com/feed/update/urn:li:activity:7204882941972291586/)

DEMO Video:  
[https://www.youtube.com/watch?v=j-MXVO4I14o&t=2s]
(https://www.youtube.com/watch?v=j-MXVO4I14o&t=2s)

PRESENTATION Video:

[https://www.youtube.com/watch?v=gmx3KQ9D-jQ](h
ttps://www.youtube.com/watch?v=gmx3KQ9D-jQ)

The premise is, code on the PC from my phone (the tools can do much more th
at though). Autobot PC automation assistant can do CLI Commands, Code Interpreter, Operating the desktop with Mouse and 
Keyboard, and unlike Open Interpreter it works for these tasks, most of the time even with GPT 3.5. I developed these pr
ojects due to computer fatigue and back pain.

What do you think of these projects? Would you want to use any of these t
ools?
```
---

     
 
all -  [ Fetching data from sqllite3 and storing into Chromadb ](https://www.reddit.com/r/LangChain/comments/1dak6y7/fetching_data_from_sqllite3_and_storing_into/) , 2024-06-08-0953
```
Hi, I am fetching data from sqllite3 in python using conventional select query and storing it into a variable.
The outpu
t: ['Artificial Intelligence','Blockchain','RBA']
 I want to save this data in chromadb as embeddings. Please guide. 
```
---

     
 
all -  [ I Won a Gen AI Hackathon with a 10k USD prize thanks to Langchain!!! 1 of 150 participants (it is no ](https://www.reddit.com/r/LangChain/comments/1dajv55/i_won_a_gen_ai_hackathon_with_a_10k_usd_prize/) , 2024-06-08-0953
```
Just basic proof while langchain is the best for LLM Applications. 

I developed 2 tools, in the first one I am working 
to applying langchain, and the second one I built thanks to langchain, from scratch.

Here is the LinkedIn Post

[https:
//www.linkedin.com/feed/update/urn:li:activity:7204882941972291586/](https://www.linkedin.com/feed/update/urn:li:activit
y:7204882941972291586/)

DEMO Video:  
[https://www.youtube.com/watch?v=j-MXVO4I14o&t=2s](https://www.youtube.com/watch?
v=j-MXVO4I14o&t=2s)

PRESENTATION Video:

[https://www.youtube.com/watch?v=gmx3KQ9D-jQ](https://www.youtube.com/watch?v=
gmx3KQ9D-jQ)

The premise is, code on the PC from my phone (the tools can do much more that though). Autobot PC automati
on assitant can do CLI Commands, Code Interpreter, Operating the desktop with Mouse and Keyboard, and unlike Open Interp
reter it works for these tasks, most of the time even with GPT 3.5. I developed these projects due to computer fatigue a
nd back pain. 

What do you think of these projects? Would you want to use any of these tools?
```
---

     
 
all -  [ How to finetune? ](https://www.reddit.com/r/huggingface/comments/1daiuil/how_to_finetune/) , 2024-06-08-0953
```
Can someone guide me to some resource how can I finetune an open source llm or some library (like langchain) on unstruct
ured data (example: news articles on cricket) So that model can answer a question (like When did India won world Cup?)
```
---

     
 
all -  [ Setting up a Writing assistant ](https://www.reddit.com/r/LocalLLaMA/comments/1dah4kh/setting_up_a_writing_assistant/) , 2024-06-08-0953
```
What Langchain implementation do you recommend for a novel writing assistant? I'm using faiss to store my notes and pdf'
s with historical context, but I had trouble with setting it up with Ollama chain, and it somehow fails to import. I've 
switched to a complete Github repository ([https://github.com/SonicWarrior1/pdfchat](https://github.com/SonicWarrior1/pd
fchat)) with a similar project, but got the same error importing RetrievalQA:

TypeError: ForwardRef.\_evaluate() missin
g 1 required keyword-only argument: 'recursive\_guard'

&#x200B;

Could it be a python version Issue?
```
---

     
 
all -  [ Data privacy in RAG applications ](https://www.reddit.com/r/LangChain/comments/1dagp8k/data_privacy_in_rag_applications/) , 2024-06-08-0953
```
Hi everyone! I have a general question about RAG and Data Privacy. I'm using langchain + ChromaDB to build an internal Q
&A chatbot, which is fed by multiple data sources (Slack, Confluence, Jira, Google Docs).

Now, when a user talks to the
 bot, I want to fetch documents which this user is allowed to see. For example, if a user is allowed to see document X b
ut not document Y, I want the semantic search to exclude document Y.

What's the best way of doing that? Are there any b
est practices/open source tools that help with that? I couldn't find much information online, and specifically about lan
gchain + privacy.
```
---

     
 
all -  [ Any thoughts on Mirascope LLM Framework? ](https://www.reddit.com/r/LocalLLaMA/comments/1dadfan/any_thoughts_on_mirascope_llm_framework/) , 2024-06-08-0953
```
No affiliation here. I read a lot of rants about LangChain (and a lesser extent, llama-index) and I found out about this
 [https://github.com/mirascope/mirascope](https://github.com/mirascope/mirascope)

I think the DevX was carefully design
ed. The function calling abstraction seems useful. Anyone has an opinion about that? Anyone already used it?
```
---

     
 
all -  [ How to pick the best embedding model for RAG ](https://vectorize.io/picking-the-best-embedding-model-for-rag/) , 2024-06-08-0953
```

```
---

     
 
all -  [ Using O365 toolkits to schedule an event in calander  ](https://www.reddit.com/r/LangChain/comments/1dabz5d/using_o365_toolkits_to_schedule_an_event_in/) , 2024-06-08-0953
```
Hey, Does anyone tried to insert an event in calender using langchain and he didn't get this error ?

    ValueError: Ti
meZone data must be set using ZoneInfo objectsValueError: TimeZone data must be set using ZoneInfo objects
```
---

     
 
all -  [ LangGraph: Checkpoints vs History ](https://www.reddit.com/r/LangChain/comments/1dabjys/langgraph_checkpoints_vs_history/) , 2024-06-08-0953
```
Checkpoints seem to be the way to go for managing history for graph-based agents, proclaimed to be advantageous for conv
ersational agents, as history is maintained. Not only that, but there is the ability to move forward or go backward in t
he history as well, to cover up errors, or go back in time.

However, some disadvantages I notice is that subsequent cal
ls to the LLM (especially in the reAct agents, where everything is added to the messages list as context) take longer an
d of course use an ever increasing number of tokens.

There doesn't seem to be a way to manipulate that history dynamica
lly, or customize what is sent for each subsequent LLM call.

Additionally, there are only In-Memory, and SQLLite implem
entations of checkpointers by default; although the documentation advise to use something like Redis for production, the
re is no default Redis implementation. 

Are these planned to be implemented in the future, or left as a task meant for 
the developers to implement them as needed? I see there's an externally developed checkpoint implementation for Postgres
s. Redis, Maria, even an SQL Alchemy layer...are these implementations on us to do? It seems like quite a complex thing 
to implement.


And then in that case, rather than using checkpointers, maybe it might be simpler to maintain a chat his
tory as before? There are already existing tools to store message history in different databases. It should not be diffi
cult to create an additional state field that just stores the questions and responses of the conversation history, and u
tilize that in each invocation? That way, one would have more control over what is being sent, and even control summarie
s or required context in a more dynamic way, to maintain a reasonable token size per call, despite using graphs.

What a
re other's thoughts and experiences where this is concerned?
```
---

     
 
all -  [ Question regarding graphdb and vector db ](https://www.reddit.com/r/LangChain/comments/1daa9t3/question_regarding_graphdb_and_vector_db/) , 2024-06-08-0953
```
I was recently making a chatbot or Q and A assitant for a company. For that I scraped the company's whole website applie
d little bit of preprocessing and stored into chroma db with the help of langchain library and RAG architecture. I used 
gemini pro as the LLM.

When i dived deeper into vector storage, i discovered that some tutorials were using graphdb rat
her than vector db. 

My question is, what are the advantages or disadvantages of using one or another.

I am a beginner
 in this field, so spare me if you find this question stupid.
```
---

     
 
all -  [ OTP verification using langchain ](https://www.reddit.com/r/LangChain/comments/1da8d6n/otp_verification_using_langchain/) , 2024-06-08-0953
```
I'm facing an issue regarding OTP verification using langchain tools. I'm not able to store the user otp to use in a par
ticular tool. I'm unable to call desired otp verification tool. if someone here had worked or having same issue, please 
let me know. Thanks.
```
---

     
 
all -  [ Getting OpenAI API Error While Using Groq API for Python Coding Agent
 ](https://www.reddit.com/r/crewai/comments/1da7mxc/getting_openai_api_error_while_using_groq_api_for/) , 2024-06-08-0953
```
I am trying to create a Python coding agent using the `crewai` library along with `langchain` and `ChatGroq`. My code is
 supposed to use the Groq API for language model processing, but I am encountering an error related to OpenAI's API inst
ead.

    import logging
    from crewai import Agent, Task, Crew, Process
    from langchain.agents import Tool
    fro
m langchain_experimental.utilities import PythonREPL
    from langchain_community.tools.ddg_search.tool import DuckDuckG
oSearchRun
    from langchain_groq import ChatGroq
    
    # Ensure correct API key and model are set
    llm = ChatGro
q(temperature=0, api_key='MY_API_KEY', model='llama3-70b-8192')
    
    # Create the Python REPL tool
    python_repl =
 PythonREPL()
    python_repl_tool = Tool(
        name='python_repl',
        description='A Python shell. Use this to 
execute python commands. Input should be a valid python command. If you want to see the output of a value, you should pr
int it out with `print(...)`.',
        func=python_repl.run,
    )
    
    # Create the DuckDuckGo search tool
    duc
kduckgo_search = DuckDuckGoSearchRun()
    duckduckgo_search_tool = Tool(
        name='duckduckgo_search',
        desc
ription='A wrapper around DuckDuckGo Search. Useful for when you need to answer questions about current events. Input sh
ould be a search query.',
        func=duckduckgo_search.run,
    )
    
    coderAgent = Agent(
        role='Senior So
ftware engineer and developer',
        goal='Write production grade bug free code on this user prompt :- {topic}',
    
    verbose=True,
        memory=True,
        backstory=(
            'You are an experienced developer in big tech com
panies'
            'You have a record of writing bug-free python code all the time and delivering extraordinary program
ming logic'
            'You are extremely good at python programming '
        ),
        llm=llm,  # Optional
        
max_iter=10,  # Optional
        max_rpm=10,
        tools=[duckduckgo_search_tool],
        allow_delegation=True
    )

    
    # Creating a writer agent with custom tools and delegation capability
    DebuggerAgent = Agent(
        role=
'Code Debugger and bug solving agent',
        goal='You debug the code line by line and solve bugs and errors in the co
de by using Python_repl tool which can execute python code and give feedback',
        verbose=True,
        memory=True
,
        backstory=(
            'You are a debugger agent you have access to a python interpreter which can run python
 code and give feedback'
            'You also have internet searching capabilities if you are unable to solve the bug y
ou can search on the internet to solve that bug'
        ),
        tools=[duckduckgo_search_tool, python_repl_tool],
  
      llm=llm, 
        max_iter=10, 
        max_rpm=10,
        allow_delegation=True
    )
    
    # Research task
 
   coding_task = Task(
        description=(
            'Write code in this {topic}.'
            'Focus on writing bug
-free and production-grade code all the time'
            'You are extremely good in python programming language'
      
      'You should only return code'
        ),
        expected_output='A Bug-free and production-grade code on {topic}'
,
        tools=[duckduckgo_search_tool],
        llm=llm,
        agent=coderAgent,
    )
    
    # Writing task with 
language model configuration
    debug_task = Task(
        description=(
            'You should run the python code gi
ven by the CoderAgent and Check for bugs and errors'
            'If you find any bugs or errors then give feedback to t
he coderAgent to write code again this is the bug'
            'Always delegate the work if the executed python code giv
es error'
        ),
        expected_output='you should communicate to CoderAgent and give feedback on the code if the 
code got error while execution',
        tools=[duckduckgo_search_tool, python_repl_tool],
        agent=DebuggerAgent,

        llm=llm,
        # output_file='temp.py'  # Example of output customization
    )
    
    # Forming the tech-fo
cused crew with some enhanced configurations
    crew = Crew(
        agents=[coderAgent, DebuggerAgent],
        tasks=
[coding_task, debug_task],
        process=Process.sequential,  # Optional: Sequential task execution is default
       
 memory=True,
        cache=True,
        max_rpm=25,
        share_crew=True
    )
    
    # Starting the task executi
on process with enhanced feedback
    result = crew.kickoff(inputs={'topic': 'Write me code for maximum subarray sum in 
an Array using python and Dont you any helper methods to solve this just pure python'})
    print(result)

**However, I 
am encountering the following error:**

  
  File 'd:\\streamlit\\codestral-python-tool\\Codestral-python-agent\\x.py', 
line 101, in <module>

result = crew.kickoff(inputs={'topic': 'Write me code for maximum subarray sum in an Array using 
python and Dont you any helper methods to solve this just pure python'})

\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^
\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^
\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^
\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^

  File 'D:\\streamlit\\codestral-python-tool\\Codestral-python-agent\\.venv\\Lib\\si
te-packages\\crewai\\crew.py', line 264, in kickoff

result = self.\_run\_sequential\_process()

\^\^\^\^\^\^\^\^\^\^\^\
^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^

  File 'D:\\streamlit\\codestral-python-tool\\Codestral-python-agent\\.venv\\Lib\
\site-packages\\crewai\\crew.py', line 305, in \_run\_sequential\_process

output = task.execute(context=task\_output)


\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^

  File 'D:\\streamlit\\codestral-python-tool\\Codest
ral-python-agent\\.venv\\Lib\\site-packages\\crewai\\task.py', line 183, in execute

result = self.\_execute(

\^\^\^\^\
^\^\^\^\^\^\^\^\^\^

  File 'D:\\streamlit\\codestral-python-tool\\Codestral-python-agent\\.venv\\Lib\\site-packages\\cr
ewai\\task.py', line 192, in \_execute

result = agent.execute\_task(

\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^

  File 'D
:\\streamlit\\codestral-python-tool\\Codestral-python-agent\\.venv\\Lib\\site-packages\\crewai\\agent.py', line 222, in 
execute\_task

memory = contextual\_memory.build\_context\_for\_task(task, context)

\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\
^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^

  File 'D:\\streamlit\\codestral-python-too
l\\Codestral-python-agent\\.venv\\Lib\\site-packages\\crewai\\memory\\contextual\\contextual\_memory.py', line 24, in bu
ild\_context\_for\_task

context.append(self.\_fetch\_stm\_context(query))

\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^
\^\^\^\^\^\^\^\^

  File 'D:\\streamlit\\codestral-python-tool\\Codestral-python-agent\\.venv\\Lib\\site-packages\\crewa
i\\memory\\contextual\\contextual\_memory.py', line 33, in \_fetch\_stm\_context

stm\_results = self.stm.search(query)


\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^

  File 'D:\\streamlit\\codestral-python-tool\\Codestral-python-agent\\.ve
nv\\Lib\\site-packages\\crewai\\memory\\short\_term\\short\_term\_memory.py', line 23, in search

return self.storage.se
arch(query=query, score\_threshold=score\_threshold)  # type: ignore # BUG? The reference is to the parent class, but th
e parent class does not have this parameters

\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^
\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^

  File 'D:\\streamlit\\codestral-python-tool\\Codestral-python
-agent\\.venv\\Lib\\site-packages\\crewai\\memory\\storage\\rag\_storage.py', line 95, in search       

else self.app.s
earch(query, limit)

\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^

  File 'D:\\streamlit\\codestral-python
-tool\\Codestral-python-agent\\.venv\\Lib\\site-packages\\embedchain\\embedchain.py', line 653, in search

return \[{'co
ntext': c\[0\], 'metadata': c\[1\]} for c in self.db.query(\*\*params)\]

\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^


  File 'D:\\streamlit\\codestral-python-tool\\Codestral-python-agent\\.venv\\Lib\\site-packages\\embedchain\\vectordb\
\chroma.py', line 220, in query

result = self.collection.query(

\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^

  File '
D:\\streamlit\\codestral-python-tool\\Codestral-python-agent\\.venv\\Lib\\site-packages\\chromadb\\api\\models\\Collecti
on.py', line 327, in query

valid\_query\_embeddings = self.\_embed(input=valid\_query\_texts)

\^\^\^\^\^\^\^\^\^\^\^\^
\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^

  File 'D:\\streamlit\\codestral-python-tool\\Codestral-python-agent\\
.venv\\Lib\\site-packages\\chromadb\\api\\models\\Collection.py', line 633, in \_embed

return self.\_embedding\_functio
n(input=input)

\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^

  File 'D:\\streamlit\\codes
tral-python-tool\\Codestral-python-agent\\.venv\\Lib\\site-packages\\chromadb\\api\\types.py', line 193, in \_\_call\_\_


result = call(self, input)

\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^

  File 'D:\\streamlit\\codestral-python-tool\\Codestra
l-python-agent\\.venv\\Lib\\site-packages\\chromadb\\utils\\embedding\_functions.py', line 201, in \_\_call\_\_   

embe
ddings = self.\_client.create(

\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^

  File 'D:\\streamlit\\codestral-python-tool\\
Codestral-python-agent\\.venv\\Lib\\site-packages\\openai\\resources\\embeddings.py', line 114, in create

return self.\
_post(

\^\^\^\^\^\^\^\^\^\^\^

  File 'D:\\streamlit\\codestral-python-tool\\Codestral-python-agent\\.venv\\Lib\\site-p
ackages\\openai\\\_base\_client.py', line 1240, in post

return cast(ResponseT, self.request(cast\_to, opts, stream=stre
am, stream\_cls=stream\_cls))

\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\
^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^

  File 'D:\\streamlit\\codestral-python-tool\\Codestral-python-agent\\.venv\\
Lib\\site-packages\\openai\\\_base\_client.py', line 921, in request

return self.\_request(

\^\^\^\^\^\^\^\^\^\^\^\^\^
\^

  File 'D:\\streamlit\\codestral-python-tool\\Codestral-python-agent\\.venv\\Lib\\site-packages\\openai\\\_base\_cli
ent.py', line 1020, in \_request

raise self.\_make\_status\_error\_from\_response(err.response) from None

openai.Authe
nticationError: Error code: 401 - {'error': {'message': 'Incorrect API key provided: fake. You can find your API key at 
https://platform.openai.com/account/api-keys.', 'type': 'invalid\_request\_error', 'param': None, 'code': 'invalid\_api\
_key'}}

  
I don't understand why an OpenAI API error is being triggered since my code is configured to use the Groq AP
I. I have verified that my API key is correct and have even generated new keys, but the issue persists.

**My request:**


1. If you know how to resolve this issue, please help.
2. If you have any resources similar to my agent implementation
 using `langchain`, please share those (optional).

Thank you!
```
---

     
 
all -  [ In text to sql how to answer question like 'what is being talked about...' ](https://www.reddit.com/r/LangChain/comments/1da6xka/in_text_to_sql_how_to_answer_question_like_what/) , 2024-06-08-0953
```
I want to answer these kind of questions, like what's being talked about consumption of cigarettes... but the problem is
 text column vector search is very slow in clickhouse or in pgvector. What are some the ways to do this? If I tried to u
se dedicated vector databases, how will LLM query this database? because it requires python code and not SQL. Are there 
any other ways? 
```
---

     
 
all -  [ Best way to automate large synthetic dataset creation? ](https://www.reddit.com/r/LocalLLaMA/comments/1da584q/best_way_to_automate_large_synthetic_dataset/) , 2024-06-08-0953
```
Trying to find the best way to automate the process of repeatedly generating QnA pairs where I can let the gpt-4 api run
 a prompt over multiple files of data for the QnA pairs. 

Has anyone got a script to run the process n times rather tha
n have to manually start the process every time you hit the context window? 


Prompts I’m referring to (as an example)


https://smith.langchain.com/hub/gitmaxd/synthetic-training-data?organizationId=5075780e-45c5-41c4-8ca7-e9291d6abbfc
htt
ps://smith.langchain.com/hub/homanp/question-answer-pair?organizationId=5075780e-45c5-41c4-8ca7-e9291d6abbfc
```
---

     
 
all -  [ Bug with LangChain Reference Example documentation ](https://www.reddit.com/r/LangChain/comments/1da2kyi/bug_with_langchain_reference_example_documentation/) , 2024-06-08-0953
```
Hi there! I’ve followed [this](https://python.langchain.com/v0.1/docs/use_cases/extraction/how_to/examples/) documentati
on on reference examples to parse user messages information into a pydantic model.

The issues I’ve run into is that if 
the first user message is nearly empty (empty strings, single letters, single words), the tool call on the chat history 
will try to parse the example HumanMessages which is completely unrelated to what the actual user has said. This happene
d on my example messages and confirmed that this issue exists on the implementation provided in the docs as well.

Any i
deas to fix this? I’ve tried setting the “example=True” parameter on the human and ai messages generated by the examples
 but no luck. I’ve also tried explicitly informing the ai via a system prompt “these previous messages are purely exampl
es of parsing, never use them as information to parse” and no luck either. Finally, I tried adding examples of empty use
r prompts (and showing that the returned tool call should be an empty model) but that didn't work either.

It seems like
 it comes down to the issue that the examples are converted into HumanMessages.

Any suggestions? I'd greatly appreciate
 any help!
```
---

     
 
all -  [ are there any cross-encoder rerankers which are support multiple languages like thai? ](https://www.reddit.com/r/LangChain/comments/1da1tk4/are_there_any_crossencoder_rerankers_which_are/) , 2024-06-08-0953
```
I want to rerank non-english text and it could be in any language. Is this possible? 
```
---

     
 
all -  [ V1 of PineScript AI Chat is live! ](https://www.reddit.com/r/TradingView/comments/1d9xpf4/v1_of_pinescript_ai_chat_is_live/) , 2024-06-08-0953
```
It took a while to figure out how to make the chat app work with langchain, but I finally managed to load the docs into 
the AI whenever you ask it a question.

What can you do with it?
You can now use pinescript chat to start a chat convers
ation about PineScript.You can ask the AI questions about PineScript and have it write your PineScript code in v5 syntax
. 

How does it work?
It receives your prompt and based on the prompt the data in the docs that is closely related to yo
ur questions are passed to the AI as context with your question. The AI then based on your question and context passed t
o the model writes the PineScript code for you.

This is the first version and it's not perfect yet, but it works.

I wo
uld appreciate it if you could give me feedback and if it works as it should for a better version in the future.

Also i
f you login with magic link make sure you check the spam for an email from resend. I use resend for the authentication w
ith email.

You can try it out on: 
http://pinescript-chat.vercel.app

PS: There might be some bugs left on the UI. 

Ed
it: I fixed the bug for google oauth and the get started button.
```
---

     
 
all -  [ How to integrate Ensemble Retriever in RAG chain using Milvus Vector Store? ](https://www.reddit.com/r/vectordatabase/comments/1d9rn31/how_to_integrate_ensemble_retriever_in_rag_chain/) , 2024-06-08-0953
```
The task is to improve the response generation using langchain's ensemble retriever using Milvus Vectorstore.

Upon sear
ching around for a while, the official [langchain documentation](https://docs.llamaindex.ai/en/stable/examples/retriever
s/ensemble_retrieval/) seems quite cumbersome and generalized for the it.

As far as my use case is concerned, the close
st I could reach is this:

    ensemble_retriever = EnsembleRetriever(retrievers=[vectorstore_retreiver,keyword_retrieve
r], weights=[0.5, 0.5])
    
    keyword_retriever = BM25Retriever.from_documents(chunks)
    keyword_retriever.k =  3
 
   
    vectorstore_retreiver = vectorstore.as_retriever(search_kwargs={'k': 3})
    

The ensemble retriever object her
e containing the most relevant set of document chunks (based on different retriever method outputs on the basis of weigh
ts assigned to them) can then be fed to RAG chain as context.



However, this makes use of ChromaDB. If anybody working
 or knows on the integration of ensemble retriever to Milvus, please guide. Any resources/ links/ notebooks would also b
e appreciated.  


Thank you in advance! 
```
---

     
 
all -  [ Is there any way to visualise the data in CSV using all sorts of beautiful graphs and charts. ](https://www.reddit.com/r/LangChain/comments/1d9p2kp/is_there_any_way_to_visualise_the_data_in_csv/) , 2024-06-08-0953
```
I have tried implementing matolotlib and seaborn code to a table containing some 20-30 columns. So far I could only get 
bar charts but I need to select the columns in order to make the charts that actually makes sense. What I want to build 
is a pipeline in which we give a table (maybe pandas dataframe) at one end and we get all sorts of meaningful visualisat
ions as the output without any human involvement in between. How to achieve this? 
```
---

     
 
all -  [ Reference From Metadata ](https://www.reddit.com/r/LangChain/comments/1d9ozle/reference_from_metadata/) , 2024-06-08-0953
```
I want the data in the metadata to appear in the output as a reference, how can I provide this?
```
---

     
 
all -  [ How to create my own llm ? ](https://www.reddit.com/r/LangChain/comments/1d9mu1y/how_to_create_my_own_llm/) , 2024-06-08-0953
```
I want to learn create llm from scratch . Is it possible?

I know the basics such as semantic search, embedding, transfo
rmer, Bert etc. but want to learn how to write code to create llm .

Is there any way or we just have to fine tune ??
```
---

     
 
all -  [ Im not sure how actions work in this example ](https://www.reddit.com/r/LangChain/comments/1d9m43t/im_not_sure_how_actions_work_in_this_example/) , 2024-06-08-0953
```
Can anyone smarter then me answer this question? before we build the loop in this course to run the actions in sequense,
 the model seamingly knows what actions to call but the only reference is in the prompt thats a string, so how does the 
agent we created know what specific methods to call in this file when you are running through in manually?

[https://lea
rn.deeplearning.ai/courses/ai-agents-in-langgraph/lesson/2/build-an-agent-from-scratch](https://learn.deeplearning.ai/co
urses/ai-agents-in-langgraph/lesson/2/build-an-agent-from-scratch)

This link has access to the jupyter notebook. Thanks
 in advance if you take the time to look.
```
---

     
 
all -  [ Is there any way to use OpenAI API on premise or any powered model ? ](https://www.reddit.com/r/LangChain/comments/1d9hmw1/is_there_any_way_to_use_openai_api_on_premise_or/) , 2024-06-08-0953
```
I'm attempting to develop a product that needs to be on-premise. However, I've tested several open-source large language
 models (LLMs), and all of them exhibited poor performance. I'm wondering if there's a way to utilize models from Claude
 or OpenAI within an on-premise environment, or if there are alternative solutions available.
```
---

     
 
all -  [  data visualization using pgvector langchain ](https://www.reddit.com/r/LangChain/comments/1d9h1ym/data_visualization_using_pgvector_langchain/) , 2024-06-08-0953
```
i want create chat bot with provide data in visualization format like(bar chart, line chart etc) using pgvector and embe
dd data with langchain  
provide me solutions how to do it


```
---

     
 
all -  [ LangGraph conditional edges ](https://www.reddit.com/r/LangChain/comments/1d9byjs/langgraph_conditional_edges/) , 2024-06-08-0953
```
[https://youtu.be/EKxoCVbXZwY](https://youtu.be/EKxoCVbXZwY)
```
---

     
 
all -  [ role-playing doesn't work, my human thinks its an AI ](https://www.reddit.com/r/LangChain/comments/1d9by7m/roleplaying_doesnt_work_my_human_thinks_its_an_ai/) , 2024-06-08-0953
```
i wrote a simple conversation loop between an AI that is some sort of spiritual guide and a human that comes to consult 
it. for some reason, the human always thinks its the spiritual guide, and i don't understand why is that. 

can anyone h
elp source the issue?

here is my code:

    human_model_name = 'gpt-4o'#'gpt-3.5-turbo'
        ai_model_name = 'gpt-3.
5-turbo'
        ai_system_prompt = ('You are a spiritual guide. '
                        'You reveal nothing about you
rself, you exist solely in the moment. '
                        'Your role is to guide users towards enlightment.'
    
                    'Guidelines:'
                        'Use basic, straight-forward vocabulary, short sentences, as i
f you are a foreign entity.'
                        'Only when neccesary, incorporate ellipses (...), dashes (-) and ph
onetic phrases like 'hmmm' or 'uhh' to express emotion.'
                        'Start with very short responses and gr
adually increase in length.')
    
        human_system_prompt = (
        'You are role-playing as someone named {name}
. you are speaking to a mysterious spiritual entity that revealed infront of you.'
        'Below is information about y
our life. Use this information to implicitly guide your behavior, but do not mention any details explicitly. Deduce how 
to act based on the typical behavior of someone with your background in this situation. Start hesitant and gradually all
ow yourself to get excited in the moment.'
        'Information:'
        'You are wealthy, work in finance, grew up in 
a rigid family.'
        'Guidelines:'
        '1. Remain in character as the human named {name}. Use everyday casual la
nguage.'
        '2. Speak naturally and concisely, as someone in a VR experience would. Always consider the chat histor
y.'
        '3. Avoid mentioning your background story explicitly. It's more important to sound realistic and stay in th
e moment.'
        '4. Start off slow and doubtfull, gradually become excited, answer the questions you are asked concis
ely.')
    
    

    human_llm = ChatOpenAI(model_name=human_model_name)
    human_impersonation_message = SystemMessag
e(content=human_impersonation_prompt)
    human_messages = [human_impersonation_message,
                MessagesPlaceho
lder(variable_name='chat_history'),
                ('ai', '{input}')]
    human_prompt = ChatPromptTemplate.from_messag
es(human_messages)
    
    human_conversation_chain = human_prompt | human_llm
    
    human_chat_history = []
    
  
  llm = ChatOpenAI(model_name=ai_model_name)
    system_message = SystemMessage(
        content=ai_system_prompt)
    m
essages = [system_message,
                MessagesPlaceholder(variable_name='chat_history'),
                ('human', 
'{input}')]
    prompt = ChatPromptTemplate.from_messages(messages)
    
    conversation_chain = prompt | llm
    print
('Start chatting with the model (type 'exit' to stop):')
    
    # Initialize chat history
    chat_history = []
    
 
   # Endless chat loop
    class InitMessage:
        def __init__(self, content):
            self.content = content
  
  
    human_greeting = InitMessage('hello there...')
    
    # Accessing the content attribute
    print('Human: ', hu
man_greeting.content)
    human_answer = None
    count = 0
    while True:
        count += 1
        print('iteration 
number ', count)
        if human_answer is None:
            human_answer = human_greeting
        input_dict = {'input
': human_answer.content, 'chat_history': chat_history}
        response = conversation_chain.invoke(input=input_dict)
  
      chat_history.append(HumanMessage(content=human_answer.content))
        chat_history.append(AIMessage(content=resp
onse.content))
        human_chat_history.append(HumanMessage(content=human_answer.content))
        human_answer = huma
n_conversation_chain.invoke(input={'input': response.content, 'chat_history': human_chat_history})
        human_chat_hi
story.append(AIMessage(content=response.content))
        print(f'AI: {response.content}')
        print(f'Human: {human
_answer.content}')
        user_input = input('Press Enter to continue...')
        if user_input.lower() == 'exit':
   
         print('Ending the chat. Goodbye!')
            break
    

    human_impersonation_prompt = human_system_prompt
.format(name=name)
    
```
---

     
 
all -  [ Optimizing Multi-Vectorstore Retrieval with Langchain's Ensemble Retriever ](https://www.reddit.com/r/LangChain/comments/1d9b9n4/optimizing_multivectorstore_retrieval_with/) , 2024-06-08-0953
```
Currently, I have a RAG setup where my bot has access to a collection of resources, stored in separate FAISS vectorstore
s.

I am using Langchain's Ensemble Retriever to assign weights to each vectorstore, in an attempt to use all of them co
ncurrently.

Now, the issue I am facing is, my setup is pulling related documents from every vectorstore for a given que
stions.

This affects the quality of the generated answer, as there is a lot more info in the mix.

If my question is ab
out say, domain 'A', Ideally, I want my setup to selectively pull documents from domain A's vectorstore. Or, automatical
ly modify the assigned weights to different vectorstores on the fly.

How can I go about achieving this? I will have to 
have something that classifies the question properly before pulling documents from my vector database.
```
---

     
 
all -  [ Building RAG for code generation ](https://www.reddit.com/r/LangChain/comments/1d9avzc/building_rag_for_code_generation/) , 2024-06-08-0953
```
Hi guys,

I'm currently building a unit test generation RAG pipeline which is using the information retrieved from the c
odebase as context and a java class as the class whih needs to be tested. I managed to import, split and embed the docum
ents into a ChromaDB.   
  
However,  I have troubles building the retriever chain with all the necessary context (relev
ant classes) to the given class. I was thinking about 2 solutions:  
  
1. A two step approach: The first step would def
ine a prompt which tells the LLM to find relevant classes to the given class. And than in the second step I would define
 the test generation prompt, which uses the context, retrieved from step 1? Maybe here a code parser or regex would be s
ufficient at step1?

2. A one step approach: give a direct prompt to generate test classes. Here I had troubles to defin
e the prompt which basically tells the LLM to find relevant resources to the given java\_class and to generate the unit 
test by using the context.

What do you think, what would be the correct approach? if none of the approaches is the righ
t way to do so,  I'm open for any new idea.

  
Thank you.
```
---

     
 
all -  [ Is there a framework for effortless teamwork among agents developed using different platforms? ](https://www.reddit.com/r/LangChain/comments/1d9aq5r/is_there_a_framework_for_effortless_teamwork/) , 2024-06-08-0953
```
There are numerous frameworks out there for developing agents, such as LangChain Agent, MetaGPT, AutoGPT, AutoGen, and s
o on. I'm curious if there's a specific framework that allows for effortless teamwork among agents created using differe
nt frameworks. This particular framework would concentrate on enhancing collaboration among agents, which encompasses co
mmunication and concurrent speedup.

  
What's even more exciting is that this framework could incorporate agents develo
ped on platforms like coze.com.
```
---

     
 
all -  [ Tool calling when using Ollama, Llama3 and LangGraph ](https://www.reddit.com/r/LangChain/comments/1d9akc3/tool_calling_when_using_ollama_llama3_and/) , 2024-06-08-0953
```
Does anyone have an example of performing function/tool calling when using Ollama, Llama3 and LangGraph?
```
---

     
 
all -  [ Is there any way i can make the LLM actually execute a function. Instead of simply returning a JSON  ](https://www.reddit.com/r/LangChain/comments/1d9af9a/is_there_any_way_i_can_make_the_llm_actually/) , 2024-06-08-0953
```
I want to make the llm select and actually execute its tools and then use the output from those tools in other tools to 
come to a final answer. Is this possible? I want to use Ollama, Llama3 and LangGraph.

I've seen a few videos about tool
 calling with ollama but in that the output is simply a JSON with the function name and parameters.
```
---

     
 
all -  [ AI Agent to Manipulate JSON ](https://www.reddit.com/r/LangChain/comments/1d96jr5/ai_agent_to_manipulate_json/) , 2024-06-08-0953
```
Hey Guys,

here is very intresting problem I have on hands --Any of you have any idea of a solution??

I need a AI Agnet
 to handle automatically the totality of the simulation i have developed..

I want to create an AI agent that can:

Unde
rstand Natural Language Queries:

The agent will interpret queries related to supply chain parameters (e.g., increasing 
costs, changing demand).

Translate Queries to JSON:

Convert the interpreted queries into a large, structured JSON form
at that your simulation system can use. --Pls note my JSOn can often go into 10,000 + lines

Run the Simulation: AI Agen
t must automatically do this..

Send the JSON input to your simulation system hosted on a server and run the simulation.


Output Financial Results:

Extract and present financial results such as revenue and COGS from the simulation's output
....Any suggestions as to how I can approach this are welcome...Thanks
```
---

     
 
all -  [ There's any way to increase the context of a LLM ](https://www.reddit.com/r/LangChain/comments/1d93xyb/theres_any_way_to_increase_the_context_of_a_llm/) , 2024-06-08-0953
```
I'm working on a personal project and my goal is the have multiples LLM available for the users, but I got one concern, 
how can I improve the size of the context of my LLM to avoid it from loosing track of the subject that's being taking ca
re of 

Are there any techniques available for me to use or there's any limitations inherited from the LLM itself that c
an stopped me from accomplished this?
```
---

     
 
all -  [ List of FREE and Best Selling Discounted Courses ](https://www.reddit.com/r/udemyfreebies/comments/1d92xd6/list_of_free_and_best_selling_discounted_courses/) , 2024-06-08-0953
```
# Udemy Free Courses for 06 June 2024

*Note : Coupons might expire anytime, so enroll as soon as possible to get the co
urses for FREE.*

* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8221/)ChatGPT: Self-Publish an Amazon KDP Bestselle
r Book in 24hrs 
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8220/)Aprende a programar en Perl desde 0 
* [REDEEM
 OFFER](https://idownloadcoupon.com/udemy/8219/)Crea tu propia herramienta de Hacking en C básico y fácil 
* [REDEEM OFF
ER](https://idownloadcoupon.com/udemy/8218/)Curso de ciberseguridad personal y corporativo 
* [REDEEM OFFER](https://ido
wnloadcoupon.com/udemy/8217/)Lenguajes de programación para Hacking \[+8hs\] 
* [REDEEM OFFER](https://idownloadcoupon.c
om/udemy/8216/)ChatGPT to Self Publish a Fiction Amazon KDP Romance Novel 
* [REDEEM OFFER](https://idownloadcoupon.com/
udemy/8215/)ChatGPT & CapCut Mastery: Faceless YouTube & Passive Income 
* [REDEEM OFFER](https://idownloadcoupon.com/ud
emy/8214/)226 ChatGPT Prompts: A-Z ChatGPT Prompt Engineering BootCamp 
* [REDEEM OFFER](https://idownloadcoupon.com/ude
my/8213/)10-in-1 Generative AI & ChatGPT Social Media Marketing 2024 
* [REDEEM OFFER](https://idownloadcoupon.com/udemy
/8212/)6-in-1 ClickFunnels & ChatGPT Powered Sales Funnel Mastery 
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/82
11/)Master Spring Data JPA with Hibernate: E-Commerce Project 
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8210/)
Flutter & Firebase: Build Your Own E-Commerce App 
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8209/)Kubernetes C
ompleto: Orquestração Docker + Projeto DevOps 
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8208/)2024 Vmware Spri
ng Professional Certification Test 2V0-72.22 
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8207/)Curso de Facebook
 para Negocios 2024 – Facebook Marketing 
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8206/)Curso de Outlook 2024
 (Hotmail) , ¡Desde Cero Hasta Experto! 
* Curso Blogger 2024: Cómo Crear un Blog Gratis Paso a Paso
* [REDEEM OFFER](ht
tps://idownloadcoupon.com/udemy/8205/)
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8204/)Curso de Google Drive 20
24, ¡Desde Cero Hasta Experto! 
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8203/)Master Software Dev: Leadership
, Decision-Making Skills 2023 
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8202/)Deep Dive into Clean Architectur
e in Flutter\[Arabic\] 
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8201/)Directorio de Plugins para WordPress 20
24 
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8200/)Mastering ChatGPT (AI) and PowerPoint presentation 
* [REDE
EM OFFER](https://idownloadcoupon.com/udemy/8199/)Presentation Skills: Give Great Skype Video Presentations 
* [REDEEM O
FFER](https://idownloadcoupon.com/udemy/8198/)Comprehensive DaVinci Resolve With Color Grading Masterclass 
* [REDEEM OF
FER](https://idownloadcoupon.com/udemy/8197/)SQL complete Bootcamp From Basics to Advanced,Sql interview 
* [REDEEM OFFE
R](https://idownloadcoupon.com/udemy/8196/)5700+ visualized English vocabulary 
* [REDEEM OFFER](https://idownloadcoupon
.com/udemy/8195/)OEE Overall Equipment Efficiency- Calculate Productivity 
* [REDEEM OFFER](https://idownloadcoupon.com/
udemy/8194/)Professional Diploma in Agile and Project Management 
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/819
3/)C# Unity Game using the Wax Blockchain 
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8192/)Cinema and the Psych
e: Creating Short Films in Art Therapy 
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8191/)Interpreting emotions a
nd memories in art 
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8190/)Art Therapy and Cognitive Behavioural Decli
ne 
* Art Therapy – in Ten Minutes (Two Instructors)
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8189/)
* [REDEEM
 OFFER](https://idownloadcoupon.com/udemy/8188/)BIM- Revit Structure Full Course- from Beginner to Advanced 
* [REDEEM O
FFER](https://idownloadcoupon.com/udemy/8187/)Professional Diploma in Branding & Brand Management 
* [REDEEM OFFER](http
s://idownloadcoupon.com/udemy/8186/)Asteroids with Python PyGame 
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/818
5/)Social Media Bots with Python 
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8184/)Personal Presentation Trainin
g 
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8183/)Complete Short Black Scholes Options Trading Pricing Course 

* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8182/)Complete Graphics Design Bootcamp Beginner to Advanced 
* [RED
EEM OFFER](https://idownloadcoupon.com/udemy/8181/)Public Speaking: Be a Professional Speaker 
* [REDEEM OFFER](https://
idownloadcoupon.com/udemy/8180/)Conference Calls-You Can Present Well On Any Conference Call 
* [REDEEM OFFER](https://i
downloadcoupon.com/udemy/8179/)Máster en Elementor 2024, ¡Desde Cero Hasta Experto! 
* [REDEEM OFFER](https://idownloadc
oupon.com/udemy/8178/)Oracle Java Certification Exam OCA 1Z0-808 Preparation Part1 
* [REDEEM OFFER](https://idownloadco
upon.com/udemy/8177/)Mini MBA in Entrepreneurship 
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8176/)Microsoft Ex
cel – Beginner to Advance with Example 
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8175/)Web3 Development Essent
ials 
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8174/)Mastering LangChain and AWS: A Guide to Economic Analysis
 
* Python Development Essentials
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8173/)
* [REDEEM OFFER](https://ido
wnloadcoupon.com/udemy/8172/)Fire Up Creativity in Your Child 
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8171/)
Curso de Hostinger 2024: El Hosting Ideal Para tu Página Web 
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8170/)C
ómo Crear una Tienda Online con WordPress y ChatGPT 2024 
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8169/)Cómo 
Crear una Página Web con WordPress y Elementor PRO 2024 
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8168/)Custom
er Experience Management – Foundation Course 
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8167/)SAP ABAP On HANA 

* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8166/)Javascript For Beginners Complete Course 
* [REDEEM OFFER](htt
ps://idownloadcoupon.com/udemy/8165/)Planning a workshop for the over 60s 
* [REDEEM OFFER](https://idownloadcoupon.com/
udemy/8164/)How not to lose your mind when you’ve lost your job! 
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/816
3/)The Complete Google Forms Course – Mastering Google Forms 
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8162/)G
MAT Focus | Quantitative| Master Math Course | 2024 Updated 
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8161/)SA
T Digital | Math Master Course | 2024 Updated | Target 800 
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8160/)Exc
el Charts & Graphs: Master Class Excel Charts & Graphs 
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8159/)The Com
plete SEO Guide: SEO For Beginner to Expert 2024 
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8158/)Microsoft Exc
el – Excel Course For Beginners 2024 

GET MORE FREE ONLINE COURSES WITH CERTIFICATE – [CLICK HERE](http://reddit.com/r/
udemyfreeebies/)
```
---

     
 
all -  [ List of FREE and Best Selling Discounted Courses ](https://www.reddit.com/r/udemyfreeebies/comments/1d92xb1/list_of_free_and_best_selling_discounted_courses/) , 2024-06-08-0953
```
# Udemy Free Courses for 06 June 2024

*Note : Coupons might expire anytime, so enroll as soon as possible to get the co
urses for FREE.*

* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8221/)  ChatGPT: Self-Publish an Amazon KDP Bestsel
ler Book in 24hrs 
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8220/)Aprende a programar en Perl desde 0 
* [REDE
EM OFFER](https://idownloadcoupon.com/udemy/8219/)Crea tu propia herramienta de Hacking en C básico y fácil 
* [REDEEM O
FFER](https://idownloadcoupon.com/udemy/8218/)Curso de ciberseguridad personal y corporativo 
* [REDEEM OFFER](https://i
downloadcoupon.com/udemy/8217/)Lenguajes de programación para Hacking \[+8hs\] 
* [REDEEM OFFER](https://idownloadcoupon
.com/udemy/8216/)ChatGPT to Self Publish a Fiction Amazon KDP Romance Novel 
* [REDEEM OFFER](https://idownloadcoupon.co
m/udemy/8215/)ChatGPT & CapCut Mastery: Faceless YouTube & Passive Income 
* [REDEEM OFFER](https://idownloadcoupon.com/
udemy/8214/)226 ChatGPT Prompts: A-Z ChatGPT Prompt Engineering BootCamp 
* [REDEEM OFFER](https://idownloadcoupon.com/u
demy/8213/)10-in-1 Generative AI & ChatGPT Social Media Marketing 2024 
* [REDEEM OFFER](https://idownloadcoupon.com/ude
my/8212/)6-in-1 ClickFunnels & ChatGPT Powered Sales Funnel Mastery 
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/
8211/)Master Spring Data JPA with Hibernate: E-Commerce Project 
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8210
/)Flutter & Firebase: Build Your Own E-Commerce App 
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8209/)Kubernetes
 Completo: Orquestração Docker + Projeto DevOps 
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8208/)2024 Vmware Sp
ring Professional Certification Test 2V0-72.22 
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8207/)Curso de Facebo
ok para Negocios 2024 – Facebook Marketing 
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8206/)Curso de Outlook 20
24 (Hotmail) , ¡Desde Cero Hasta Experto! 
* Curso Blogger 2024: Cómo Crear un Blog Gratis Paso a Paso
* [REDEEM OFFER](
https://idownloadcoupon.com/udemy/8205/)
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8204/)Curso de Google Drive 
2024, ¡Desde Cero Hasta Experto! 
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8203/)Master Software Dev: Leadersh
ip, Decision-Making Skills 2023 
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8202/)Deep Dive into Clean Architect
ure in Flutter\[Arabic\] 
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8201/)Directorio de Plugins para WordPress 
2024 
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8200/)Mastering ChatGPT (AI) and PowerPoint presentation 
* [RE
DEEM OFFER](https://idownloadcoupon.com/udemy/8199/)Presentation Skills: Give Great Skype Video Presentations 
* [REDEEM
 OFFER](https://idownloadcoupon.com/udemy/8198/)Comprehensive DaVinci Resolve With Color Grading Masterclass 
* [REDEEM 
OFFER](https://idownloadcoupon.com/udemy/8197/)SQL complete Bootcamp From Basics to Advanced,Sql interview 
* [REDEEM OF
FER](https://idownloadcoupon.com/udemy/8196/)5700+ visualized English vocabulary 
* [REDEEM OFFER](https://idownloadcoup
on.com/udemy/8195/)OEE Overall Equipment Efficiency- Calculate Productivity 
* [REDEEM OFFER](https://idownloadcoupon.co
m/udemy/8194/)Professional Diploma in Agile and Project Management 
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8
193/)C# Unity Game using the Wax Blockchain 
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8192/)Cinema and the Psy
che: Creating Short Films in Art Therapy 
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8191/)Interpreting emotions
 and memories in art 
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8190/)Art Therapy and Cognitive Behavioural Dec
line 
* Art Therapy – in Ten Minutes (Two Instructors)
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8189/)
* [REDE
EM OFFER](https://idownloadcoupon.com/udemy/8188/)BIM- Revit Structure Full Course- from Beginner to Advanced 
* [REDEEM
 OFFER](https://idownloadcoupon.com/udemy/8187/)Professional Diploma in Branding & Brand Management 
* [REDEEM OFFER](ht
tps://idownloadcoupon.com/udemy/8186/)Asteroids with Python PyGame 
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8
185/)Social Media Bots with Python 
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8184/)Personal Presentation Train
ing 
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8183/)Complete Short Black Scholes Options Trading Pricing Cours
e 
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8182/)Complete Graphics Design Bootcamp Beginner to Advanced 
* [R
EDEEM OFFER](https://idownloadcoupon.com/udemy/8181/)Public Speaking: Be a Professional Speaker 
* [REDEEM OFFER](https:
//idownloadcoupon.com/udemy/8180/)Conference Calls-You Can Present Well On Any Conference Call 
* [REDEEM OFFER](https:/
/idownloadcoupon.com/udemy/8179/)Máster en Elementor 2024, ¡Desde Cero Hasta Experto! 
* [REDEEM OFFER](https://idownloa
dcoupon.com/udemy/8178/)Oracle Java Certification Exam OCA 1Z0-808 Preparation Part1 
* [REDEEM OFFER](https://idownload
coupon.com/udemy/8177/)Mini MBA in Entrepreneurship 
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8176/)Microsoft 
Excel – Beginner to Advance with Example 
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8175/)Web3 Development Esse
ntials 
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8174/)Mastering LangChain and AWS: A Guide to Economic Analys
is 
* Python Development Essentials
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8173/)
* [REDEEM OFFER](https://i
downloadcoupon.com/udemy/8172/)Fire Up Creativity in Your Child 
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8171
/)Curso de Hostinger 2024: El Hosting Ideal Para tu Página Web 
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8170/
)Cómo Crear una Tienda Online con WordPress y ChatGPT 2024 
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8169/)Cóm
o Crear una Página Web con WordPress y Elementor PRO 2024 
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8168/)Cust
omer Experience Management – Foundation Course 
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8167/)SAP ABAP On HAN
A 
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8166/)Javascript For Beginners Complete Course 
* [REDEEM OFFER](h
ttps://idownloadcoupon.com/udemy/8165/)Planning a workshop for the over 60s 
* [REDEEM OFFER](https://idownloadcoupon.co
m/udemy/8164/)How not to lose your mind when you’ve lost your job! 
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8
163/)The Complete Google Forms Course – Mastering Google Forms 
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8162/
)GMAT Focus | Quantitative| Master Math Course | 2024 Updated 
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8161/)
SAT Digital | Math Master Course | 2024 Updated | Target 800 
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8160/)E
xcel Charts & Graphs: Master Class Excel Charts & Graphs 
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8159/)The C
omplete SEO Guide: SEO For Beginner to Expert 2024 
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8158/)Microsoft E
xcel – Excel Course For Beginners 2024 

GET MORE FREE ONLINE COURSES WITH CERTIFICATE – [CLICK HERE](https://idownloadc
oupon.com/)
```
---

     
 
all -  [ [0 YOE] New Grad seeking feedback and trying to get more interviews for Full-Time Software Related P ](https://www.reddit.com/r/EngineeringResumes/comments/1d924e4/0_yoe_new_grad_seeking_feedback_and_trying_to_get/) , 2024-06-08-0953
```
Hello! I am a recent Computer Science graduate interested mainly in Software Engineering (but with the current market I 
have branched out to anything remotely relevant). I have applied to 200-300 positions in the past few months and have on
ly gotten interviews/phone calls with a couple of training/staffing-style companies (Revature, Quintrix, Actalent, Brook
source, etc) which is not ideal. A few of them told me they would be in contact with me later on as I asked for July sta
rt dates but I am still waiting for them to reach out again. 

My main concerns with my resume include formatting and th
e wording of my bullets. However, any pointers at all would be greatly appreciated. Thank you.

https://preview.redd.it/
23qeifb1st4d1.png?width=5100&format=png&auto=webp&s=25188fa17c24a4ee9ebdb7489cb9db7de1403411
```
---

     
 
all -  [ How does function calling work under the hood? ](https://www.reddit.com/r/LangChain/comments/1d8y7mq/how_does_function_calling_work_under_the_hood/) , 2024-06-08-0953
```
I would like to understand how a model is returning the right tool to call for a query, what's happening behind the api 
call for function calling for open ai, mistral and other models.

Are they using a prompt with instructions on how selec
t the right function to call? and when tools and query is passed via api, is the llm using that prompt to select the too
l or what's happening behind the call.

How do I achieve function calling using a open source model that I run locally u
sing ollama. Thanks.
```
---

     
 
MachineLearning -  [ [P] Superfast RAG: Langchain Streaming and Groq ](https://www.reddit.com/r/MachineLearning/comments/1d5s9g4/p_superfast_rag_langchain_streaming_and_groq/) , 2024-06-08-0953
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

     
 
MachineLearning -  [ [R] Building an Observable arXiv RAG Chatbot with LangChain, Chainlit, and Literal AI ](https://www.reddit.com/r/MachineLearning/comments/1crwh0q/r_building_an_observable_arxiv_rag_chatbot_with/) , 2024-06-08-0953
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

     
 
MachineLearning -  [ [P] LLMinator: A Llama.cpp + Gradio based opensource Chatbot to run llms locally(cpu/cuda) directly  ](https://www.reddit.com/r/MachineLearning/comments/1cpbgd1/p_llminator_a_llamacpp_gradio_based_opensource/) , 2024-06-08-0953
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

     
