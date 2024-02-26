 
all -  [ Langchain tool is acting crazy with postgresql   ](https://www.reddit.com/r/genai/comments/1b01hfr/langchain_tool_is_acting_crazy_with_postgresql/) , 2024-02-26-0910
```
Hey people

I am working on a case to develop a RAG(retrieval augmented generation) with Langchain and flan T5 over post
gresql database using sql_data_toolkit. To my surprise, I have been struck with psycopg2 syntax error over the generated
 SQL queries. I couldn't resolves even with prompt adjustments. Did anyone faced the same issue while working with Langc
hain on structured postgresql databases. Any help is highly appreciated. Thanks in advance.


```
---

     
 
all -  [ 🎉Langchain Rust🎉 ](https://www.reddit.com/r/LLMDevs/comments/1b01bee/langchain_rust/) , 2024-02-26-0910
```
I’m thrilled to share a personal project of mine: a Rust port of Langchain. As a core contributor to the official Go Lan
g port of Langchain (langchaingo), I’ve embarked on a new challenge to further my skills by diving into Rust programming
. This project is a standalone effort to reimagine Langchain’s capabilities within the Rust ecosystem, which is renowned
 for prioritizing safety and performance.

Take a look here: https://github.com/Abraxas-365/langchain-rust 

This is a p
ersonal initiative, not an official port, reflecting my ongoing quest to enhance my technical know-how and engage with i
nnovative language model applications. I’m eager to discover what possibilities this project might unlock and I warmly i
nvite you to check out the repository, share your insights, or consider contributing. Your feedback and contributions ar
e not only welcome but also highly valued as they contribute to the enrichment of both the project and the broader commu
nity. Let’s delve into the potential that lies at the crossroads of Rust and AI together!
```
---

     
 
all -  [ Which vectorstore for prosuction?  ](https://www.reddit.com/r/LangChain/comments/1azrzkc/which_vectorstore_for_prosuction/) , 2024-02-26-0910
```
Hi,

Which vectorstore do you like most for production usecases?
At the moment I am using Faiss, is this suitable for pr
oduction? I also heard that PgVector should be nice, what are advantages of it?

Thanks!
```
---

     
 
all -  [ We all hate LangChain, so what do we actually want? ](https://www.reddit.com/r/LocalLLaMA/comments/1azrk8b/we_all_hate_langchain_so_what_do_we_actually_want/) , 2024-02-26-0910
```
I appreciate the anti-langchain post as much as anyone, but in the spirit of optimism, I'd like to talk about what every
one wants to build and improve instead :)

I often hear 'Oh LLMs can do <x> easily, just ...' But once you start buildin
g, the complexities pile up quickly!

So for a fun Sunday discussion, what is your dream framework for working with lang
uage models?

For me, I'm mostly anti-framework these days, and prefer a more building blocks that you can pick and choo
se from. Here's some pain points off the top of my head:

* Context Management: I built a small LLM context manager tool
 to handle chat history, RAG, and other data. It worked well until I built a full app, and now I feel the pain from not 
being able to tweak it for each instance (influence scores easily, order, etc) and determine what was included in the li
mited context.
* Chains/Loops: I built a small-ish chain library so I could write custom prompts and loop them. It's kin
d of useful, but I found that many of the chain 'entries' need to be custom functions to control the flow. Seems nearly 
impossible for someone else to work with haha
* File Import: I used pymupdf since it seemed to give lower-level access t
o PDFs, enough that I could generate markdown w/ headings from files. Extracting images and tables in-line seems difficu
lt, and multi-column pages are a disaster. I'd love a library to convert any document to markdown.
* Chunking: I made a 
custom markdown chunking function so I could break it up by headings and include headings/doc title metadata in the chun
ks. It's still messy and I feel the limitations every time I use RAG.

There are also some higher level problems I'm int
erested in:

Handling chat/rag/agents smoothly - so the LLM will respond quickly when it can, use rag when necessary, an
d use assistant/agent loops otherwise.

Understanding multi-turn RAG/agents. For example, how do you handle a RAG questi
on and then a generic follow up with less context? The first message returns a bunch of results, and the second message 
returns none ('Ok, what's the second part mean?'). Do you keep including the original RAG data in the context, and keep 
filling it with more data as the chat continues? My RAG and assistant chats feel like one-shot instead of smooth convers
ations.

How about everyone else? What do you currently use, what are your pain points, and do you have a dream tool?

I
n the end, do we just have to roll our own custom libraries for each use case?
```
---

     
 
all -  [ Here is plan to install/learn these to explore ai/ml ](https://www.reddit.com/r/LocalLLaMA/comments/1azrfyf/here_is_plan_to_installlearn_these_to_explore_aiml/) , 2024-02-26-0910
```

Openinterpreter with openai API to help clean up my old MacBook and fix boot camp and fix greyed out partition and then
 to organize stuff, delete old stuff, etc. chosing openai API since it's ranking 1st in most tasks and this is kinda mis
sion critical 

Ollama to explore small llm models

Langchain to learn about ai/ml,since it's mentioned a lot

Huggingfa
ce cloud to explore / test bigger models

There are few other mainly visual ai frameworks that I plan to review, but was
 wondering if any suggestions or if some of the above isn't worth it

....
```
---

     
 
all -  [ OpenAi embedding v3 weird scores ](https://www.reddit.com/r/LangChain/comments/1azr70c/openai_embedding_v3_weird_scores/) , 2024-02-26-0910
```
I have been using ada for a while now with a Faiss store and it has been doing well. 

Today I tried text-embedding-3-la
rge today and the scores are weird. 

The correct match with ada gets a score of ~0.2 (0 being the best match and 1 bein
g the worst match) 
The correct match with text-embedding-3-large gets a score of ~0.5 

The full ordering from score 0-
1 seems to be better than ada. But the there is a shift towards a score of 1. 

Has anyone experienced that? Or has any 
explanation? 
```
---

     
 
all -  [ Best utility library? ](https://www.reddit.com/r/LocalLLaMA/comments/1azoqnl/best_utility_library/) , 2024-02-26-0910
```
There's been a few posts banging on Langchain a bit lately, but I find I do use their utility functions for doc loading,
 text splitting, etc.

What library is the best for these types of helper functions in your opinion?
```
---

     
 
all -  [ Langchain use cases ](https://www.reddit.com/r/LangChain/comments/1azoinv/langchain_use_cases/) , 2024-02-26-0910
```
I’m a software quality engineer and I’ve been tasked with exploring ai use cases for my team. The only thing I could thi
nk was test plan generation by storing our existing test plans in a db and information about products(PRD, public docs e
tc.) and somehow getting the llm to return a test plan draft based on this. Would this even be feasible and worth explor
ing? What other use cases you think could be beneficial to a quality engineering team? I’m an AI noob btw with interest 
in building on top of llm
```
---

     
 
all -  [ Review my resume guys.I'm applying for entry level Data scientist role. I'm a fresher. ](https://i.redd.it/ujd8j53xbqkc1.jpeg) , 2024-02-26-0910
```

```
---

     
 
all -  [ Need strong criticism on ny resume! Suggestion about projects also! ](https://i.redd.it/556kt3bqaqkc1.jpeg) , 2024-02-26-0910
```
i’m applying for entry-level data scientist jobs.
```
---

     
 
all -  [ Langchain library - the worst 'common functionality' abstraction package out there? ](https://www.reddit.com/r/LocalLLaMA/comments/1azkbnl/langchain_library_the_worst_common_functionality/) , 2024-02-26-0910
```
I've recently had time to dive into the Langchain library for creating a simple chatbot with memory (previously I've jus
t used GPT4 APIs with my own abstractions).

I don't understand, really... Am I stupid or Langchain is completely unusab
le due to the incredible overengineering efforts? Also - wow, documentation and practical examples are soooo terrible!


There's just too much abstraction depth. I don't wanna blame the Langchain devs or anything, it's just my general feelin
g. Also - did I mention how confusing, hard-to-read and unclear the documentation is?

If shooting your foot with a C++ 
gun blows your whole leg off...

I feel that - shooting your foot with Langchain blows your both legs off and, additiona
lly, tears you apart in half.
```
---

     
 
all -  [ Synthetic data generation using langchain ](https://www.reddit.com/r/LangChain/comments/1azi86f/synthetic_data_generation_using_langchain/) , 2024-02-26-0910
```
 I have a question regarding generating synthetic data, in the docs synthetic data generation guide is only using OpenAI
 and when I'm trying to use other model It's just giving me some error is that possible to use other local models for sy
nthetic data generation https://python.langchain.com/docs/use_cases/data_generation 

my code
```py
synthetic_data_gener
ator = create_openai_data_generator(
 output_schema=MedicalBilling,
 llm=Ollama(model='llama2'),
 prompt=few_shot_prompt
_template
)
```

error
```
ValueError: Ollama call failed with status code 400. Details: invalid options: functions, fun
ction_call
```
```
---

     
 
all -  [ how can I add more fields into a mongoDB database from langchain? ](https://www.reddit.com/r/LangChain/comments/1azhuxd/how_can_i_add_more_fields_into_a_mongodb_database/) , 2024-02-26-0910
```
I want to add a human message status into the mongodb database that tells if the message has been replayed to or not, ho
w can I do that in langchain with this function?  
 

    message_history = MongoDBChatMessageHistory(
                 
   connection_string=connection_string, 
                    session_id=f'{phone_number}'
                )

&#x200B;
```
---

     
 
all -  [ Query optimization ](https://www.reddit.com/r/LangChain/comments/1azfbj0/query_optimization/) , 2024-02-26-0910
```
I have a Json data and I want to optimize my retrieval process down to 50ms, how can we do this?
```
---

     
 
all -  [ What's the best way to Monitize AI chatbot (webapp) ](https://www.reddit.com/r/LangChain/comments/1aze52v/whats_the_best_way_to_monitize_ai_chatbot_webapp/) , 2024-02-26-0910
```
I have been developing a chatbot for a niche market. But I was wondering what's the best method to Monitize an AI conver
sational chatbot. 
```
---

     
 
all -  [ Setting up a CI/CD workflow for LLM evaluation ](https://www.reddit.com/r/devops/comments/1azbafg/setting_up_a_cicd_workflow_for_llm_evaluation/) , 2024-02-26-0910
```
[Using Langchain Evaluators and  Pytest](https://semaphoreci.com/blog/llms-performance-testing)
```
---

     
 
all -  [ Working with Langchain evaluators ](https://www.reddit.com/r/LangChain/comments/1azb96b/working_with_langchain_evaluators/) , 2024-02-26-0910
```
How to set up a [CI/CD workflow using Langchain Evaluators and Pytest](https://semaphoreci.com/blog/llms-performance-tes
ting) in measuring LLM performance with Langchain evaluators, 
```
---

     
 
all -  [ Making gpt-4 understand dates via RAG ](https://www.reddit.com/r/LangChain/comments/1az7uay/making_gpt4_understand_dates_via_rag/) , 2024-02-26-0910
```
I have written a RAG-system which uses around a 100 meeting notes from various dates. While ingesting the data I attach 
the date as metadata (using llamaindex) to each document. 

My problem is that the model is invariably confused about wh
en the latest meeting was held/meeting note is from and will even contradict itself in the same chat session.

I would g
reatly appreciate any suggestions as to how I can fix this! 
```
---

     
 
all -  [ Response Schema Python/CSV Agent ](https://www.reddit.com/r/LangChain/comments/1az69hi/response_schema_pythoncsv_agent/) , 2024-02-26-0910
```
Hey guys, so I've been creating an agent that went from a SQL to Python/CSV agent (I kept getting errors from the db so 
gave up on that). I have gotten to this final product where I get a specific response schema back and I'd like to use it
 to provide an answer, along with an embedded plot that is related to said answer. I have tested it, and it seems to wor
k but the only thing is that my output does not want to return the schema. First, below is the code for the streamlit ap
p:

&#x200B;

    from langchain_openai import OpenAI
    from langchain_experimental.agents.agent_toolkits import creat
e_python_agent, create_csv_agent # tools that will be used for sql agent to reason for
    from langchain_experimental.t
ools.python.tool import PythonREPLTool
    from langchain.agents.agent_types import AgentType # for agent type assignmen
t
    from langchain.agents.react.agent import create_react_agent
    from langchain.agents import (AgentExecutor, Tool)
 # agent executor to execute agent Tool, to make tool out of agent, ConversationalAgent to create template
    # from la
ngchain.memory import ConversationBufferMemory # chat memory for agentfrom langchain_core.prompts import ChatPromptTempl
ate, MessagesPlaceholder
    from langchain.prompts import PromptTemplate
    from langchain.output_parsers import Respo
nseSchema, StructuredOutputParser
    from langchain_community.callbacks import StreamlitCallbackHandler
    from langch
ain.globals import set_verbose, set_debug
    
    from langchain_community.llms import Ollama
    from langchain_google
_vertexai import VertexAI
    import google.auth
    
    from dotenv import load_dotenv
    import os
    
    import s
treamlit as st
    
    ##### Setup #####
    
    # Load the environment variables
    load_dotenv()
    
    # google 
authorization
    CREDENTIALS, PROJECT_ID = google.auth.default()
    
    # set langchain to verbose, debug true
    se
t_verbose(True)
    set_debug(False)
    
    ##### LLM #####
    @st.cache_resource
    def model_init(model_type = 'ge
mini'):
        # To use Ollama you must first install the model of choice, then provide its name as a parameter
       
 if(model_type == 'ollama'):
            model = Ollama(
                        model='mistral:latest',  # Provide your
 ollama model name here
                        temperature = 0.0,
                        streaming=True
              
          )
        
        # Initializing Gemini
        elif model_type == 'gemini':
            model = VertexAI(
  
              model_name = 'gemini-pro',
                max_output_tokens = '2500',
                temperature = 0.05,

                top_p = 0.8,
                top_k = 40,
                verbose = True,
                streaming=True
,
                project=PROJECT_ID,
                credentials=CREDENTIALS
            )
    
        elif model_type
 == 'openai':
            model = OpenAI(temperature = 0.05, 
                           verbose = True,
               
            api_key=os.getenv('OPENAI_API_KEY')
                           streaming=True)
    
        elif model_type 
== 'codellama':
            model = VertexAI(
                model_name = 'codellama-70b',
                max_output_t
okens = '2500',
                temperature = 0.05,
                top_p = 0.8,
                top_k = 40,
           
     verbose = True,
                streaming=True,
                project=PROJECT_ID,
                credentials=CRE
DENTIALS
            )
        return model
    
    ##### SQL Database #####
    # @st.cache_resource
    # def db_init
(file):
    #     # Connect to the SQLite database
    #     connection = sqlite3.connect('data.db')
    
    #     # cr
eate dataframe from data
    #     df = pd.read_csv(file)
    
    #     # Convert DataFrame to a SQLite table
    #    
 df.to_sql('data', connection, if_exists='replace')
    
    #     # connect to local database
    #     db = SQLDatabas
e.from_uri('sqlite:///data.db')
    
    #     return db 
    
    ##### Agent #####
    @st.cache_resource
    def agen
t_init( _llm, data_description, file):
        python_agent = create_python_agent(llm=_llm,
                            
               tool=PythonREPLTool(),
                                           verbose=True)
        
        csv_agen
t = create_csv_agent(llm=_llm,
                                     path=file,)
    
        # Create the whole list of 
tools
        tools=[
            Tool(
                name='PythonAgent',
                func=python_agent.invoke,
  
              description='Useful to plot data',
            ),
            Tool(
                name='CSVAgent',
     
           func=csv_agent.invoke,
                description='Useful to manipulate csv files as dataframes',
          
  ),
        ]
    
        response_schemas = [
            ResponseSchema(name='Final Answer', description='Answer to 
the user's query.'),
            ResponseSchema(
                name='plot',
                description='Python code f
or the pandas plot, if applicable.',
        ),
        ]
    
        output_parser = StructuredOutputParser.from_respo
nse_schemas(response_schemas)
    
        ##### Agent Creation #####
        prompt_template = PromptTemplate.from_temp
late(
            '''We are statistically analyzing a dataset for a user by giving them natural language answers to thei
r data analysis questions.
    
            Below is a description of the dataset:
    
            ''' + data_descripti
on + '''
    
            Please answer the user's request utilizing the tools below:
            {tools}
            
 
           The names of the tools are:
            {tool_names}
    
            Then, format the Final Answer as follow
s:
            {format_instructions}
    
            Do not transform the format above. It is your way of thinking thro
ugh the problem.
    
            If there is no need to answer the question, or it is irrelevant to your job, please ma
ke your final answer something similar to: 'Please ask a relevant query.'
    
            Begin!
    
            Quest
ion: {input} 
            Thought: {agent_scratchpad}''',
            partial_variables={'format_instructions':output_pa
rser.get_format_instructions()},
        )
    
        # create zero shot agent (react agent)
        agent = create_re
act_agent(
            llm=_llm,
            tools=tools,
            prompt=prompt_template,
        )
    
        # I
nitiate memory which allows for storing and extracting messages
        # memory = ConversationBufferMemory(memory_key='
chat_history', input_key='input', output_key='output')
    
        ##### Agent Chain #####
    
        # Create an Age
ntExecutor which enables verbose mode and handling parsing errors
        agent_chain = AgentExecutor.from_agent_and_too
ls(
            agent=agent, tools=tools, handle_parsing_errors=True, # memory=memory
        )
    
        return agen
t_chain
    
    ##### Streamlit Code #####
    
    # Set the webpage title
    st.set_page_config(
        page_title=
'Dataset Q&A',
        page_icon='📊',
    )
    
    run = False
    
    with st.sidebar:
        # get params for func
tions
        model_name = st.selectbox('Select model', ['gemini', 'ollama', 'openai', 'codellama'])
        st.session_
state['file'] = st.file_uploader('Upload a csv file', type=['csv'])
    
        st.session_state['description'] = st.te
xt_area('Description')
        st.markdown('Dataset descirption should include a general description (e.g., the purpose 
of the data, what it is used for, etc.)')
    
        # initialize model, db, agent on run
        if st.button(label='
Run', help='This will initialize the model, database, and agent. It will also reset the chat interface.'):
            s
t.session_state['run'] = True
    
    # Create a header element
    st.header('Dataset Q&A')
    st.markdown('**PLEASE 
RUN SIDEBAR FIRST BEFORE RUNNING CHAT INTERFACE**')
    
    if 'run' in st.session_state and st.session_state['run'] ==
 True:
        with st.spinner('🚀 Loading model...'):
            st.session_state['llm'] = model_init(model_name)
    

    
        with st.spinner('🦾 Loading agent...'):
            st.session_state['agent_chain'] = agent_init(st.session_
state['llm'], st.session_state['description'], st.session_state['file'])
    
        if 'messages'  in st.session_state
:
            st.session_state.messages = [
            {'role': 'assistant', 'content': 'Welcome to the Data QA bot! As
k whatever questions you'd like!'}
        ]
        
    
    #### Create a chat interface ####
    
    # We store the
 conversation in the session state.
    # This will be used to render the chat conversation.
    # We initialize it with
 the first message we want to be greeted with.
    
    ##  Session States ##
    if 'messages' not in st.session_state:

        st.session_state.messages = [
            {'role': 'assistant', 'content': 'Welcome to the Data QA bot! Ask wha
tever questions you'd like!'}
        ]
    
    # We loop through each message in the session state and render it as
  
  # a chat message.
    for message in st.session_state.messages:
        with st.chat_message(message['role']):
       
     st.markdown(message['content'])
    
    
    ## Chat Code ## 
    # We take questions/instructions from the chat i
nput to pass to the LLM
    if user_input := st.chat_input('Question', key='input'):
        st.chat_message('user').wri
te(user_input)
    
        # Add our input to the session state
        st.session_state.messages.append(
            {
'role': 'user', 'content': user_input}
        )
    
        # Add the response to the chat window
        with st.chat
_message('assistant'):
            st_callback = StreamlitCallbackHandler(st.container()) # visualize thinking process
 
   
            # invoke chain with necessary input variables
            response = st.session_state['agent_chain'].inv
oke({'input' : user_input})
    
            # Add the response to messages session state
            st.session_state.m
essages.append(
                {'role': 'assistant', 'content': response['output']})
            
            st.write_
stream(response['output'])

Next, here is the output (what is below, but repeated multiple times:

    ```Invalid Format
: Missing 'Action:' after 'Thought:```json
    {
            'Final Answer': 'The top selling item is 'Computer', with 2
2548 units sold.',
            'plot': '```python\nimport pandas as pd\nimport matplotlib.pyplot as plt\n\n# Read the CS
V file into a DataFrame\ndf = pd.read_csv('sales_data.csv')\n\n# Group the data by item and sum the sales\ndf = df.group
by('Item').sum()\n\n# Sort the data by sales in descending order\ndf = df.sort_values('Sales', ascending=False)\n\n# Get
 the top selling item\ntop_selling_item = df.iloc[0]['Item']\n\n# Print the top selling item\nprint(f'The top selling it
em is {top_selling_item}.')\n\n# Plot the top selling item\ndf.plot.bar(x='Item', y='Sales')\nplt.title('Top Selling Ite
m')\nplt.xlabel('Item')\nplt.ylabel('Sales')\nplt.show()\n```'
    }
    ```Invalid Format: Missing 'Action:' after 'Tho
ught:```json
    {
            'Final Answer': 'The top selling item is 'Computer', with 22548 units sold.',
           
 'plot': '```python\nimport pandas as pd\nimport matplotlib.pyplot as plt\n\n# Read the CSV file into a DataFrame\ndf = 
pd.read_csv('sales_data.csv')\n\n# Group the data by item and sum the sales\ndf = df.groupby('Item').sum()\n\n# Sort the
 data by sales in descending order\ndf = df.sort_values('Sales', ascending=False)\n\n# Get the top selling item\ntop_sel
ling_item = df.iloc[0]['Item']\n\n# Print the top selling item\nprint(f'The top selling item is {top_selling_item}.')\n\
n# Plot the top selling item\ndf.plot.bar(x='Item', y='Sales')\nplt.title('Top Selling Item')\nplt.xlabel('Item')\nplt.y
label('Sales')\nplt.show()\n```'
    }
    ```Invalid Format: Missing 'Action:' after 'Thought:```json
    {
           
 'Final Answer': 'The top selling item is 'Computer', with 22548 units sold.',
            'plot': '```python\nimport pa
ndas as pd\nimport matplotlib.pyplot as plt\n\n# Read the CSV file into a DataFrame\ndf = pd.read_csv('sales_data.csv')\
n\n# Group the data by item and sum the sales\ndf = df.groupby('Item').sum()\n\n# Sort the data by sales in descending o
rder\ndf = df.sort_values('Sales', ascending=False)\n\n# Get the top selling item\ntop_selling_item = df.iloc[0]['Item']
\n\n# Print the top selling item\nprint(f'The top selling item is {top_selling_item}.')\n\n# Plot the top selling item\n
df.plot.bar(x='Item', y='Sales')\nplt.title('Top Selling Item')\nplt.xlabel('Item')\nplt.ylabel('Sales')\nplt.show()\n``
`'
    }
    ```Invalid Format: Missing 'Action:' after 'Thought:
    
    > Finished chain.

Any help/feedback is much 
appreciated! I really wanna get good at Lang Chain but have spent a lot of time troubleshooting errors. Hopefully this i
s the last! (doubt it)
```
---

     
 
all -  [ Looking to Hire a Teacher to Meet Twice a Month ](https://www.reddit.com/r/LangChain/comments/1az5do0/looking_to_hire_a_teacher_to_meet_twice_a_month/) , 2024-02-26-0910
```
Hi!



I am a Data Scientist by trade and have been working with Langchain specifically for about 2 months now. I enjoy 
coding both inside and outside of work.



I'm not looking for any help with work.

I want a non-academic tutor who I me
et with once or twice a month via Zoom and I can use it like office hours.



If you would be interested in exploring ra
ndom passion projects and ideas with me please send a DM and we can discuss rates and hours there. I'm flexible haha.




P.S. I'd love recommendations on how I can accomplish finding someone like this as well if anyone has thoughts.



EDIT
: Lots of people seem intestedsted so I've made a small discord server for us to dive into this!

[https://discord.gg/U8
H27HTB](https://discord.gg/U8H27HTB)  
Looking forward to meeting yall and talking about our projects!
```
---

     
 
all -  [ Developing Langchain Agents with the MinIO SDK for LLM Tool-Use ](https://www.reddit.com/r/minio/comments/1az41o8/developing_langchain_agents_with_the_minio_sdk/) , 2024-02-26-0910
```
In this guide, we prioritize practicality, steering towards actionable development practices. We invite developers to em
brace the potential that lies in the union of Langchain and MinIO SDK, to not only innovate but also to redefine the bou
ndaries of what can be achieved with the intelligent automation of today's digital tools.

[https://blog.min.io/minio-la
ngchain-tool/?utm\_source=reddit&utm\_medium=organic-social+&utm\_campaign=minio\_langchain\_tool+](https://blog.min.io/
minio-langchain-tool/?utm_source=reddit&utm_medium=organic-social+&utm_campaign=minio_langchain_tool+)
```
---

     
 
all -  [ Help - tutorial needed ](https://www.reddit.com/r/LangChain/comments/1az3nu8/help_tutorial_needed/) , 2024-02-26-0910
```
I’ve been trying to follow a few different tutorials but I keep getting stuck.  

Problem:  currently, it’s time consumi
ng and labor intensive to find historic data in the various reports that I have.  Our staff changes seasonally so report
s and data get filed away and forgotten about until someone stumbles upon it or active goes looking for ‘that study on x
 5 years ago’

Need: I have about 20 years of environmental reports in PDF I want to load into a vector DB then put a ch
atbot on top of it for my co-workers to query for past results.  

I’ve gotten to the point of where OpenAI embeddings a
re working but storing them and querying them is where I get lost.  I overthink and keep trying different platforms (chr
oma, pinecone, faiss) that sets me back.  

I followed a tutorial to use streamlit and pinecone and OpenAI and it kind o
f works but lacks substance on the retrieval.  I then look at the scaling costs of pinecone and it’s more than I need bu
t can’t figure out another VDB to learn from.  

Any books, websites, libraries are great appreciated!  I’d even pay if 
there is a paid version of a course to take.  

Thank you


```
---

     
 
all -  [ Hello from the Feast project (https://feast.dev)! The open-source Feature Store. ](https://www.reddit.com/r/mlops/comments/1az3fz6/hello_from_the_feast_project_httpsfeastdev_the/) , 2024-02-26-0910
```
Hi folks, I want to bring you the latest update on the open-source Feature Store project: Feast ([https://feast.dev](htt
ps://feast.dev/)). The Feast project wants to share this message with you:[ https://feast.dev/blog/the-future-of-feast/]
(https://feast.dev/blog/the-future-of-feast/) The post is written by William Pienaar, the founder of the Feast project, 
representing our 200+ contributors.

We have been working very hard to improve the project quality and make it adapt to 
the current AI trend (check Langchain's post about Feast: [https://blog.langchain.dev/feature-stores-and-llms/](https://
blog.langchain.dev/feature-stores-and-llms/)). We hope the MLOps community can give us more feedback about the usage of 
it. With your feedback, we can shape the Feast into a solid product and serve the MLOps community in a better way.

Plea
se support us with bug/issue reports at:[ https://github.com/feast-dev/feast](https://github.com/feast-dev/feast) 

Cont
ributions are also welcome!

&#x200B;
```
---

     
 
all -  [ Youtube loader with timecodes ](https://www.reddit.com/r/LangChain/comments/1az2t9r/youtube_loader_with_timecodes/) , 2024-02-26-0910
```
Hey folks,   
Playing around with the pet project that asks for subjects discussed in a video and asks for the time code
.  
I found that the in-house loader is limited for the task at hand. It does not provide the necessary start code unlik
e the 'youtube-transcript-api' library.  


Has anyone worked on something similar? What would be the best way to do tha
t?
```
---

     
 
all -  [ RAG with OpenAI assistant API ](https://www.reddit.com/r/LangChain/comments/1az27pt/rag_with_openai_assistant_api/) , 2024-02-26-0910
```
Has anyone tried using the following method?

I have a use case where I need to pull out a product recommendation. I use
 open AI assistant to help me do the job. But I do not use the built-in retrieval from the openAI. Instead I build a ret
rieval tool which is essentially a retrieval chain (load and chunk the data myself, using vector store and use retriever
) 
But the problem is I find that OpenAI assistant sometimes answer customer questions without using the tool.

Like for
 example, it will use its own knowledge to answer customer inquiries instead of looking up the database.
Is there a way 
I can improve it? Something like assigning another agent to the flow downstream to check if the first response is genera
ted by the default brain of assistant API or based on the retrieval tool? I’m just brainstorming..


```
---

     
 
all -  [ FlowiseAI python alternative  ](https://www.reddit.com/r/LangChain/comments/1az0uae/flowiseai_python_alternative/) , 2024-02-26-0910
```
Hi,
Is there any FlowiseAI alternative in python? 
Or Is there any way to export the flows created in FlowiseAI to pytho
n code?
```
---

     
 
all -  [ LCEL along with legacy chain  ](https://www.reddit.com/r/LangChain/comments/1ayv0uz/lcel_along_with_legacy_chain/) , 2024-02-26-0910
```
I have been trying to use Langhain, especially the new custom composed LCEL chains in combination with the legacy consti
tutional chains that allow me to do guardrails. 

But because constitutional chains are not in the new format of LCEL, I
 couldn't figure out a way to make it work. Legacy constitutional chain accepts only another legacy chain as an input. S
o I can't put them together. 

Help will be appreciated!
```
---

     
 
all -  [ How to remove the prompt and prompt template from the response when invoking a chain? ](https://www.reddit.com/r/LangChain/comments/1ayszzh/how_to_remove_the_prompt_and_prompt_template_from/) , 2024-02-26-0910
```
Hello,



I am in the process of doing my master's thesis and will focus on multi-agent systems for software testing. I 
have decided to use LangGraph as my framework of choice and I am in the process of learning it.

I have been toying arou
nd with LangChain and it's been working great. However, one of the things that I cannot seem to figure out, is how to ha
ve the model only give me the output, without the input being a part of it.

Code example below:

    llm_hf = HuggingFa
ceHub(repo_id='mistralai/Mistral-7B-Instruct-v0.2',
         model_kwargs={'temperature': 0.9})
    
    duck_specialist
_template = '''
    I want you to act as a specialist in ducks, covering aspects from their biology to conservation.  Yo
ur role involves providing expert insights into different duck species, including their habitats, behaviors, and the cha
llenges they face in their natural environments. Additionally, you're tasked with advising on conservation strategies to
 protect these species and their habitats from threats such as habitat loss, pollution, and climate change.  For any inq
uiry about ducks, offer a comprehensive overview that includes species identification, habitat preferences, dietary habi
ts, migratory patterns, and conservation status. Moreover, suggest practical conservation measures that can be implement
ed to support the health and sustainability of duck populations.  Can you provide funny name suggestions on a duck that 
looks like {duck_description}?
    ''' 
    
    tiny = 'a small, energetic duck with bright blue feathers and a penchan
t for doing somersaults in the water. Its quack is surprisingly deep for its size'
    
    prompt_template = PromptTemp
late(
         input_variables=['duck_description'],
         template=duck_specialist_template,
     )
    
    chain =
 LLMChain(llm=llm_hf, prompt=prompt_template)  print(chain.run(duck_description=tiny)) 

Now, when I run this it gives m
e the following output:

>I want you to act as a specialist in ducks, covering aspects from their biology to conservatio
n.  
Your role involves providing expert insights into different duck species, including their habitats, behaviors, and 
the challenges they face in their natural environments. Additionally, you're tasked with advising on conservation strate
gies to protect these species and their habitats from threats such as habitat loss, pollution, and climate change.  
For
 any inquiry about ducks, offer a comprehensive overview that includes species identification, habitat preferences, diet
ary habits, migratory patterns, and conservation status. Moreover, suggest practical conservation measures that can be i
mplemented to support the health and sustainability of duck populations.  
Can you provide funny name suggestions on a d
uck that looks like a small, energetic duck with bright blue feathers and a penchant for doing somersaults in the water.
 Its quack is surprisingly deep for its size?  
Absolutely! Based on the description you've given, I would suggest the n
ame 'Flippy the Feisty Blue Bunter.' This name captures the duck's small size, energetic nature, bright blue feathers, a
nd acrobatic behavior in the water (somersaults), while the 'feisty' part adds a fun and lively character to its name. T
he term 'bunter' is a playful way to refer to the duck's

Here the prompt is part of the output, which in turn cuts off 
the models response. I have been trying to find out a way to fix this, but prompting does not seem to work and I could n
ot find anything that works. I am just concerned that if I start chaining, then it will reach the output limit before it
 can respond to future prompts, making the chain obsolete and the task complete unsolvable.
```
---

     
 
all -  [ Check out this LangChain (Generative AI framework) playlist with 60+ tutorials ](https://www.reddit.com/r/AI__India/comments/1aysq8c/check_out_this_langchain_generative_ai_framework/) , 2024-02-26-0910
```
Hey everyone, checkout this playlist with 60+ tutorials for learning any LangChain concept from scratch with codes. [htt
ps://www.youtube.com/watch?v=OagbDJvywJI&list=PLnH2pfPCPZsKJnAIPimrZaKwStQrLSNIQ](https://www.youtube.com/watch?v=OagbDJ
vywJI&list=PLnH2pfPCPZsKJnAIPimrZaKwStQrLSNIQ) 
```
---

     
 
all -  [ Learning LangChain (Generative AI framework) from scratch ](https://www.reddit.com/r/ArtificialInteligence/comments/1aysosk/learning_langchain_generative_ai_framework_from/) , 2024-02-26-0910
```
Hey everyone, checkout this playlist with 60+ tutorials for learning any LangChain concept from scratch with codes. http
s://www.youtube.com/watch?v=OagbDJvywJI&list=PLnH2pfPCPZsKJnAIPimrZaKwStQrLSNIQ
```
---

     
 
all -  [ Save chatbot to pdf ](https://www.reddit.com/r/learnmachinelearning/comments/1aypd76/save_chatbot_to_pdf/) , 2024-02-26-0910
```
I'm using huggingface and langchain for a chatbot then building a gradio UI for launching. How can I extract my chat his
tory and download it from a gradio button. 
```
---

     
 
all -  [ Cohere rerank, contextual compression and ContextReorder, can I just use the top document?  ](https://www.reddit.com/r/LangChain/comments/1ayl2mb/cohere_rerank_contextual_compression_and/) , 2024-02-26-0910
```
So I’m trying to get a specific chunk of data and it does retrieve it perfectly but it seems to apply the lower matched 
chunks as well. Is there a way to just use the very top ranked chunked document? It seems to be out of order if contextu
ally if we apply all the chunks in a response 

```
---

     
 
all -  [ Good tool for copywriting? ](https://www.reddit.com/r/LangChain/comments/1aykmn5/good_tool_for_copywriting/) , 2024-02-26-0910
```
Hey everyone, hoping to get some insights about where to focus my studies over the next couple of months.

Part of my wo
rk is copywriting, and I think it would be behoove me to leverage generative AI tools in order to keep myself relevant a
s this tech becomes more commonplace in my domain. I've been skilling up on Python over the last several months as a hob
by and also to boost the other aspect of my work, which is consulting. Apart from programming fundamentals, I've been fo
cusing on ML/NLP. The specific use case for my consulting work is sentiment analysis, so the focus lately has been on le
arning to use Hugging Face and diving into data acquisition.

I have a LangChain tutorial earmarked to tackle next, as i
t seems like a good tool to generate synthetic datasets for training/fine-tuning models for sentiment analysis specific 
to my domain. I have the impression that it could also be quite useful for my copywriting work, but I'm less clear exact
ly how. Is that the case? Are there any other tools that would be useful for someone in my position? Any guidance along 
these lines would be hugely appreciated.
```
---

     
 
all -  [ Without open AI or Gemini api key ](https://www.reddit.com/r/LangChain/comments/1ayipqy/without_open_ai_or_gemini_api_key/) , 2024-02-26-0910
```
So I was planning to build a chatbot with langchain. But I can't use open Ai or any gpt api keys coz of privacy. Is ther
e any other work around for this ? 
```
---

     
 
all -  [ MLOps from a hiring manager perspective. Am I doing this wrong? ](https://www.reddit.com/r/mlops/comments/1ayfkx3/mlops_from_a_hiring_manager_perspective_am_i/) , 2024-02-26-0910
```
So I have a lot of various projects. My engineers (non ML background have done a good job so far).

They can convert DS 
code into web services. They can ship in-house models that the DS builds. These models are NLP and image analysis. We've
 been doing this for a few years.  
They can do the data pipeline - pick and choose database, queue, etc. Also do load-t
esting to see how many transactions we can do given our compute. Basic full stack, with DevOps in between. I can have a 
guy pull a huggingface model, write a k8s helm chart and create an API endpoint to interact with it in 2 days. So now, w
e are having a lot of new projects. Especially with LLMS - Llama2, Mistral, ChatGPT. A lot of RAG projects. Like here is
 100GB of PDFS, we want to vectorize the data, create the embeddings and have various prompts with agents. So if the que
ry was find x or y, it can run an agent/tool to get the data via SQL or API call and feed it back to the prompt via ReAc
t prompt engineering. This is working fine.   
Now we want to scale out the team. Ideally, look for people that have the
se skills. The person should know what a VectorDB is - Cosmos,PineCone,Postgres(pgvector), chromadb,etc. They should kno
w what a similarity search is. How to create an embedding. They should know what langchain is.  


I am getting candidat
es that tell me they can just feed a LLM with plain JSON from Mongo. That an LLM can just do an API call without any con
figuration/setup. Like they are talking out of their asses.  


What am I doing wrong? Candidates are keyword stuffing t
heir resumes with the latest buzzwords or is this the state of MLOps? My requirements is mostly Python backend as our cu
rrent staff before the ChatGPT  hype are all python devs. So writing APIs is just a normal thing. Draft up a swagger spe
c, create the routes.   


But when I ask an interview candidate to convert a rough DS (data scientists can barely write
 any legible code) python script that reads a csv and feeds their small model to get a summary into a REST endpoint, no 
one knows how to do it. To me it is simple, convert the code that reads the csv file into a POST endpoint to consume a p
ayload. Not create a database to store records when the question is a FIFO (First In First Out) API that gets a payload 
and returns a summary from the content. Then they ask why we even doing this? My answer is we are creating a web service
 from the data science team's r&d prototype work so others can consume this.   


Is there a disconnect? or am I looking
 for the wrong candidates? Even simple orchestration questions are appalling. How do you deploy llama2 on-premise to a k
8s cluster. They all say create a docker image w/ a 38GB file and create a 38GB docker image.  


To me an MLOps should 
know how to convert DS python code into deployable services. RESTful if needed. Know how to orchestrate. Create the data
 ingestion and data lake. If I need 4,000 PDFs vectorized, they know how to create an ETL to create those embeddings. Wo
rking off-the-shelf genAI LLMs, they should know some fundamental RAG, vectors, and prompt engineering.

&#x200B;
```
---

     
 
all -  [ RAG evaluation framework ](https://www.reddit.com/r/LangChain/comments/1ayfdhs/rag_evaluation_framework/) , 2024-02-26-0910
```
Hi,

I am looking for some good resources for RAG evaluation.
```
---

     
 
all -  [ LangSmith for evaluation or something else? ](https://www.reddit.com/r/LangChain/comments/1ayaf7p/langsmith_for_evaluation_or_something_else/) , 2024-02-26-0910
```
Hello folks - I feel guilty for posting here but I really can't find a better place. Thank you to anyone who can help me
 or point me in the right direction.

**TLDR**: I'm so desperate for user interviews I'm willing to debase myself for 30
 minutes of your time.   
I am trying to find people to talk to who have shipped or are close to shipping a feature that
 integrates with a 3rd party LLM. I have questions about LLM evaluation because we're building product around that, some
what tangential to langsmith. I need to expand way beyond my personal network. 

I have tried searching forums, posting 
in slack groups, attending in person events in SF, swiping right on every ML engineer, user interview recruiting sites b
ut I'm coming up with a lot of people who are still dabbling with the tech but haven't hit real development yet. Most of
 the folks I've talked to just haven't gotten to any real 'LLM evaluation' needs yet. 

Langchain's series A announcemen
t said they have 80k users, so surely there are some people here that fit my mold?

I am **desperate** to pick your brai
n for 30 minutes about your 'genai stack' and how you figure out if a LLM-integrated solution is behaving well on your d
ata for your users. 

I would gladly send you a thank you milk bar pie, buy you a bougie coffee shop gift card, take you
 on a date (34/F/SF) or yell at your boss for you or for a few moments of your time. 

Please DM me if we can chat somet
ime in the next week or two. Thank you!
```
---

     
 
all -  [ Vertex AI Slowwwwww ](https://www.reddit.com/r/googlecloud/comments/1ay7q54/vertex_ai_slowwwwww/) , 2024-02-26-0910
```
I just started playing around with Gemini and Vertex AI via their python library.  And it is unbearably slow.  Gemini ta
kes 3-5 minutes to write a haiku about the moon, while AWS Bedrock does it in 12 seconds. This happens whether I'm using
 vertexai SDK or Langchain.

[https://imgur.com/a/TlFsxWx](https://imgur.com/a/TlFsxWx)

Not doing anything particularly
 fancy.  It has to be something on my end but can't think of what it might be.

    from datetime import datetime
    st
artTime = datetime.now()
    import vertexai
    from vertexai.generative_models import GenerativeModel
    
    vertexa
i.init()
    model=GenerativeModel('gemini-1.0-pro')
    print(model.generate_content('Write me a haiku about the moon.'
))
    
    print(datetime.now() - startTime)

&#x200B;
```
---

     
 
all -  [ ollama/langchain streaming with tools ](https://www.reddit.com/r/ollama/comments/1ay7ojf/ollamalangchain_streaming_with_tools/) , 2024-02-26-0910
```
I'm trying to setup ollama so that I can have a conversation in a terminal (with streaming) and also allow ollama to int
eract with some rest api. I was able to get streaming working with ChatOllama() by doing this:

    llm = ChatOllama(mod
el='mixtral')
    chain = llm | StrOutputParser()
for chunks in chain.stream('hello')
        print(chunks)

However, I 
don't think I can use ChatOllama to call rest api? I tried streaming with OllamaFunctions() like this:

    llm = Ollama
Functions(model='mixtral')
    chain = create_extraction_chain(schema, llm)
for chunks in chain.stream(input_text)
     
   print(chunks)

However, it only prints out the whole response all at once. Is there a way to do this with streaming? 
I mean I don't need to neccessarily stream an extraction, but I want to have a converstation that uses streaming and als
o allows ollama to call an api.

&#x200B;
```
---

     
 
all -  [ Extracting metadata from a PDF and converting to JSON using LangChain and GPT ](https://www.reddit.com/r/LangChain/comments/1ay6vx4/extracting_metadata_from_a_pdf_and_converting_to/) , 2024-02-26-0910
```
Hi folks! Currently working on a Micro SaaS and ended up needing to convert a PDF to JSON. Given that I've been playing 
around with LangChain for a while now and writing about it, I ended up using the Output Parsers to achieve this.

[I wro
te about this on my blog](https://www.gettingstarted.ai/how-to-extract-metadata-from-pdf-convert-to-json-langchain/) and
 it works like magic... ✨ In fact, it's not just PDF you could convert. Any type of unstructured data potentially works.


Here's what I covered in the post:

✅ Key concepts and explanations

✅ LangChain Output Parsers

✅ OpenAI Functions

✅
 Working source code

[https://www.gettingstarted.ai/how-to-extract-metadata-from-pdf-convert-to-json-langchain/](https:
//www.gettingstarted.ai/how-to-extract-metadata-from-pdf-convert-to-json-langchain/)

Would love to know your thoughts a
nd if you find this helpful.

Cheers!
```
---

     
 
all -  [ Ecosystem around LangChain ](https://www.reddit.com/r/LangChain/comments/1ay1c6a/ecosystem_around_langchain/) , 2024-02-26-0910
```
Hello everyone, I have to admit that I struggle to keep up with the LLM Ecosystem around LangChain and wanted to ask if 
you have any recommended packages that people like me might not know about. I would be especially interested in packages
 you use to build advanced RAG applications and packages you use in Production for task xyz.

I start with a few:

**Lan
gfuse**: LangSmith alternative to monitor LLM Applications in production. MIT License - great!

**Semantic-Text-Splitter
**: Allows you to split documents by contextual parts of them, rather by a fixed document size.

**Ragas**: Framework fo
r evaluating RAG Pipelines. Not dived into it yet, but looks promising.

Please add your favorite packages. Thank you!
```
---

     
 
all -  [ LangChain Agent 를 활용하여 #chatgpt 를 #업무자동화 에 적용하는 방법🔥🔥 https://www.facebook.com/groups/aitutor21/perma ](https://www.reddit.com/r/chatgpt_newtech/comments/1axvptn/langchain_agent_를_활용하여_chatgpt_를_업무자동화_에_적용하는_방법/) , 2024-02-26-0910
```
LangChain Agent 를 활용하여 #chatgpt 를 #업무자동화 에 적용하는 방법🔥🔥   [https://www.facebook.com/groups/aitutor21/permalink/195027638538
5787/?mibextid=oMANbw](https://www.facebook.com/groups/aitutor21/permalink/1950276385385787/?mibextid=oMANbw)
```
---

     
 
all -  [ Langchain Map Reduce  ](https://www.reddit.com/r/learnmachinelearning/comments/1axkz9u/langchain_map_reduce/) , 2024-02-26-0910
```
I was wondering how langchain map reduce iteratively reduces prompts

For example if we have a context size of 2k and a 
8k token input is supplied 

first we map the 8k to 4x2k maps 

then assuming that those 4 summaries result in 4x1k outp
ut time  summaries how would we map those for the next iteration

Would we fit 2 summaries in one resulting in 2x2k toke
ns maps?

Or would we summarize further each 1k output until all 4 combined are less than 2k context? 

Ie 2 llm calls o
r 4 llm’s calls after first iteration?

I can’t really find any docs supporting either answer clearly for me
```
---

     
 
all -  [ PDF Document Loader not working Langchain ](https://www.reddit.com/r/LangChain/comments/1axi03f/pdf_document_loader_not_working_langchain/) , 2024-02-26-0910
```
Hi I'm trying to extract the content of a pdf using langchain pdf document loader (the javascript version). It could be 
the way I wrote the code (cause I'm still relatively new to javascript and langchain in general) but when i try to run t
he pdf loader i get this error in my console saying 'Type error: readFile is not a function' and i don't know if its one
 of the following;

1. My code
2. I'm not referencing the file path correctly
3. Or something completely unrelated

Hi I
'm trying to extract the content of a pdf using langchain pdf loader (the javascript version). it could be the way i wro
te the code (cause I'm still relatively new to javascript and langchain in general) but when i try to run the pdf loader
 i get this error in my console saying 'Type error: readFile is not a function' and i don't know if its one of the follo
wing;

1. My code
2. I'm not referencing the file path correctly
3. Or something completely unrelated

I'd love and appr
eciate your help and inputs. Thanks in advance

[the pdf is in the public folder](https://preview.redd.it/98512y4zd7kc1.
png?width=556&format=png&auto=webp&s=c2a3693529050746aa49a8f3bf167974180e2e98)

[This is how i called the loader](https:
//preview.redd.it/rpah335zd7kc1.png?width=948&format=png&auto=webp&s=377aff4df96e2f4dd548b0b7b2c6fa65a3ce625b)

[this is
 the error](https://preview.redd.it/nk4mr75zd7kc1.png?width=610&format=png&auto=webp&s=9bf928181eab4da3f03079ebe398ed629
f85d068)
```
---

     
 
all -  [ LangChain - RunnableParallel ](https://www.reddit.com/r/LangChain/comments/1axhxg5/langchain_runnableparallel/) , 2024-02-26-0910
```
I've been banging my head against this issue for awhile and docs haven't been helping.

I'm trying to optimize a chain b
y getting certain things to run in Parallel

I've created a basic example:

`from langchain.chat_models import ChatOpenA
I`

`from langchain.prompts import PromptTemplate`

`from langchain.schema import StrOutputParser`

`from operator impor
t itemgetter`

`from langchain.schema.runnable import (`

`RunnablePassthrough,`

`RunnableLambda,`

`RunnableParallel,`


`)`

`llm_model='gpt-3.5-turbo'`

`llm = ChatOpenAI(temperature=0.9, model=llm_model)`

`prompt = PromptTemplate.from_
template(`

`'What is a good name for a company that makes {product}?'`

`)`

`chain = prompt | ChatOpenAI(temperature=0
.9, model=llm_model) | StrOutputParser()`

Let's start with a standard chain invocation:

`result = chain.invoke({'produ
ct':'Queen Size Sheet Set'})`

`result`

>Regal Rest Bedding Co.

&#x200B;

Now let's say you want to track intermediate
 steps values, so you use RunnablePassthrough:

`chainPass = RunnablePassthrough.assign(company_name=chain)`

`result2 =
 chainPass.invoke({'product':'Queen Size Sheet Set'})`

`result2`

>{'product': 'Queen Size Sheet Set', 'company\_name':
 'RegalRest Bedding Co.'}

&#x200B;

That is great - now we have both the original query (product) and intermediate vari
ables (e.g. company\_name)

Let's try to get this to run in parallel (just with the single chain)

`pchain = RunnablePar
allel(company_name=runnable)`

`pchain.invoke({'product':'Queen Size Sheet Set'})`

>{'company\_name': 'RegalSlumber'}


&#x200B;

Well now we are missing the initial query. What if we tried to assign the chainPass?

`pchain2 = RunnableParal
lel(parent=chainPass)`

`pchain2.invoke({'product':'Queen Size Sheet Set'})`

>{'parent': {'product': 'Queen Size Sheet 
Set',  
>  
>'company\_name': 'Regal Rest Bedding Co.'}}

&#x200B;

This isn't great because now the data is mishaped.


This problem becomes much harder as your chain becomes longer and you start to have steps before/after you Parallel step
, or if you add manual routing, or if you add additional Parallel paths.

The basic question is how do you run multiple 
chains in Parallel when you can keep the input query as well as the outputs for each chain at the root level of the dict
-like output.
```
---

     
 
all -  [ asynchronous requests ](https://www.reddit.com/r/LangChain/comments/1axhkki/asynchronous_requests/) , 2024-02-26-0910
```
Greetings, I have a question about langchain. I have built a database query creation wizard using a langchain agent and 
openai. The thing is that when used by several people the program begins to delusion who should respond first and they e
nd up responding where they shouldn't be. I want to know if there is any tutorial or any way I can use asynchronous call
s so that I can solve this problem and wizard ends up answering one question at a time.
```
---

     
 
MachineLearning -  [ [D] Graphs + vectordbs? Need your input: Cognee.ai . AI Data Pipelines for Real-World Production (Pa ](https://www.reddit.com/r/MachineLearning/comments/1aweo71/d_graphs_vectordbs_need_your_input_cogneeai_ai/) , 2024-02-26-0910
```
Hey there, Redditors!

I'm back with the latest installment on creating dependable AI data pipelines for real-world prod
uction.

If you've been following along, you know I'm on a mission to move beyond the '[thin OpenAI wrapper](https://top
oteretes.notion.site/Going-beyond-Langchain-Weaviate-and-towards-a-production-ready-modern-data-platform-7351d77a1eba40a
ab4394c24bef3a278?pvs=4)' trend and tackle the challenges of building robust data pipelines.

After a few months of work
, we integrated cognitive architecture with [keepi.ai](https://www.keepi.ai) 

We aim to explore with our demo:

**1. Co
ntext sanitization**  
The world of AI is fast-moving, and we've realized that the context is becoming a building block 
we refer to as a crucial part of future cognitive architecture.  
**2. Best Practices for AI Memory**  
In this rapidly 
evolving landscape, there are no established best practices. You'll need to make educated bets on tools and processes, k
nowing that things will change. We assume that having traditional data engineering practices + frameworks + classifiers 
and other AI solutions can solve a lot of standard hurdles  
**3. AI Frameworks**  
They are trying to do too much, too 
fast, too broad. We want to find a pattern and a correct layer of abstraction for the AI memory to fit new industry.  



&#x200B;

How does it work? 

The Github repo is l:

  


[How cognee works](https://preview.redd.it/yuiabmyihyjc1.png?
width=1633&format=png&auto=webp&s=4384c4441b615f72caf1e0591c5ab23aee735fab)

Github repo is [here](https://github.com/to
poteretes/cognee)

Next steps:  
I have questions for you:

1. Is context sanitization relevant for you?
2. How do you m
anage metadata? 
3. How do you prepare data for LLMs?
4. Are there any data enrichment steps you perform?

Check out the
 blog post:

[Link to part 4](https://topoteretes.notion.site/Going-beyond-Langchain-Weaviate-Level-4-towards-production
-fe90ff40e56e44c4a49f1492d360173c?pvs=4)

*Remember to give this post an upvote if you found it insightful!*  
*And also
 star our* [Github repo](https://github.com/topoteretes/cognee)
```
---

     
 
MachineLearning -  [ [D] AI projects Suggestions ](https://www.reddit.com/r/MachineLearning/comments/1aunkmw/d_ai_projects_suggestions/) , 2024-02-26-0910
```
Hi Everyone, I need a suggestion to create AI courses for students ( Hands-on AI projects). I am thinking about the late
st AI trends such as Langchain, RAG, and vector databases. In each project, there can be multiple tasks, and the main th
ing is each task should have an automated system in which we can verify whether students have done it correctly or not.


For example: Project with visualization cannot be automatically tested. 

For example: A project with visualization can
not be automatically tested. . em can verify if the length of the text is smaller we can verify that it is correct.
```
---

     
 
MachineLearning -  [ Whats in your RAG setup? [D] ](https://www.reddit.com/r/MachineLearning/comments/1apcp2w/whats_in_your_rag_setup_d/) , 2024-02-26-0910
```
What frameworks and libraries are you using in your RAG? 

I'm most curious if  LangChain is as popular as it was?

Here
's mine at a high-level: 

*  langchain to use OpenAI for creating embeddings
* Pinecone for storing embedding
* langcha
in to load document splitters and characters splitters for chunking
* Mongo for conversations memory

&#x200B;
```
---

     
 
MachineLearning -  [ [D] What's the best current RAG setup that would work with a local LLM? ](https://www.reddit.com/r/MachineLearning/comments/1ag6bo7/d_whats_the_best_current_rag_setup_that_would/) , 2024-02-26-0910
```
I've tried things like langchain in the past (6-8 months ago) but they were cumbersome and didn't work as expected.

I  
need RAG to get data from various pdfs (long one, 150+ pages) - and i  need a setup that will allow me to add more and m
ore data sources.

I wanna run this locally, can get a 24gb video card (or 2x16gb ones) - so i can run using 33b or smal
ler models.

I  know things in the industry change every 2 weeks, so i'm hoping there's  an easy and efficient way of do
ing RAG (compared to 6 months ago)
```
---

     
 
MachineLearning -  [ [P]: Anukool: My job hunting assistant ](https://www.reddit.com/r/MachineLearning/comments/1adu3tw/p_anukool_my_job_hunting_assistant/) , 2024-02-26-0910
```
Hey Reddit, I've been applying for jobs and found that writing a cover letter for each position was tedious. I also delv
ed into LLM and Langchain, hoping to leverage them for a project to aid in my job hunting. So, I developed Anukool under
 the GPL license. While it's far from perfect, it has proven very useful to me, and I hope it benefits you as well. All 
I have to do is provide it with a pdf containing information about me such as my experience, skills, projects, etc and i
t will use this information along with job description to generate cover letter for me. Since I'm new to ML and LLM, any
 advice or feedback is greatly appreciated, and contributions are also welcome. I plan to utilize Llama-2 soon to furthe
r open-source the project.

Check out the GitHub link, and please star it if you find the project interesting: https://g
ithub.com/dakshesh14/anukool
```
---

     
 
deeplearning -  [ [D] WebVoyager: Navigating Digital Cosmos with LangGraph & Multimodal Models ](https://www.reddit.com/r/deeplearning/comments/1altlca/d_webvoyager_navigating_digital_cosmos_with/) , 2024-02-26-0910
```
Embark on a journey through the digital cosmos with WebVoyager, a groundbreaking Large Multimodal Model (LMM) web agent 
designed to navigate the vastness of the online universe. In collaboration with Langchain, WebVoyager represents a parad
igm shift in autonomous web agents, seamlessly integrating visual and textual information to complete user instructions 
end-to-end by interacting with real-world websites.

Link: [https://medium.com/@andysingal/webvoyager-navigating-digital
-cosmos-with-langgraph-multimodal-models-dace64196c2f](https://medium.com/@andysingal/webvoyager-navigating-digital-cosm
os-with-langgraph-multimodal-models-dace64196c2f)
```
---

     
 
deeplearning -  [ [D] Langchain Elevates with Step-Back Prompting using RAGatouille ](https://www.reddit.com/r/deeplearning/comments/1agtyeh/d_langchain_elevates_with_stepback_prompting/) , 2024-02-26-0910
```
In the dynamic realm of natural language processing, a revolutionary synergy has emerged between Langchain and Step-Back
 Prompting. This article delves into the transformative collaboration, exploring how Langchain’s cutting-edge platform i
ncorporates Step-Back Prompting to redefine language processing capabilities. Join us on a journey of innovation and dis
covery as we unravel the intricacies of this powerful integration. As we explore the uncharted territories of language m
odels, Step-Back Prompting stands as a beacon of progress, promising a journey of nuanced understanding and elevated per
formance in the world of Large Language Models. Welcome to the future of language processing, where inspiration and inno
vation converge in a symphony of words and ideas.

Link: https://medium.com/ai-advances/langchain-elevates-with-step-bac
k-prompting-using-ragatouille-b433e6f200ea
```
---

     
 
deeplearning -  [ Become an AI Developer (Free 9 Part Series) ](https://www.reddit.com/r/deeplearning/comments/1afgp2r/become_an_ai_developer_free_9_part_series/) , 2024-02-26-0910
```
Just sharing a free series I stumbled across on Linkedin - DataCamp's 9-part AI code-along series.

This specific sessio
n linked below is 'Building Chatbots with OpenAI API and Pinecone' but there are 8 others to have a look at and code alo
ng to.

*Start from basics to build on skills with GPT, Pinecone and LangChain to create a chatbot that answers question
s about research papers. Make use of retrieval augmented generation, and learn how to combine this with conversational m
emory to hold a conversation with the chatbot. Code Along on DataCamp Workspace:* [*https://www.datacamp.com/code-along/
building-chatbots-openai-api-pinecone*](https://www.datacamp.com/code-along/building-chatbots-openai-api-pinecone)

Find
 all of the sessions at: [https://www.datacamp.com/ai-code-alongs](https://www.datacamp.com/ai-code-alongs)
```
---

     
 
deeplearning -  [ DSPy Explained! ](https://www.reddit.com/r/deeplearning/comments/1adypks/dspy_explained/) , 2024-02-26-0910
```
DSPy is the next big advancement for AI and building applications with LLMs!

Pioneered by frameworks such as LangChain 
and LlamaIndex, we can build much more powerful systems by chaining together LLM calls! This means that the output of on
e call to an LLM is the input to the next, and so on. We can think of chains as programs, with each LLM call analogous t
o a function that takes text as input and produces text as output.

DSPy offers a new programming model, inspired by PyT
orch, that gives you a massive amount of control over these LLM programs. Further the Signature abstraction wraps prompt
s and structured input / outputs to clean up LLM program codebases.

DSPy then pairs the syntax with a super novel compi
ler that jointly optimizes the instructions for each component of an LLM program, as well as sourcing examples of the ta
sk.

Here is my review of the ideas in DSPy, covering the core concepts and walking through the introduction notebooks s
howing how to compile a simple retrieve-then-read RAG program, as well as a more advanced Multi-Hop RAG program where yo
u have 2 LLM components to be optimized with the DSPy compiler! I hope you find it useful!

https://www.youtube.com/watc
h?v=41EfOY0Ldkc
```
---

     
