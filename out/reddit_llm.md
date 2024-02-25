 
all -  [ Making gpt-4 understand dates via RAG ](https://www.reddit.com/r/LangChain/comments/1az7uay/making_gpt4_understand_dates_via_rag/) , 2024-02-25-0910
```
I have written a RAG-system which uses around a 100 meeting notes from various dates. While ingesting the data I attach 
the date as metadata (using llamaindex) to each document. 

My problem is that the model is invariably confused about wh
en the latest meeting was held/meeting note is from and will even contradict itself in the same chat session.

I would g
reatly appreciate any suggestions as to how I can fix this! 
```
---

     
 
all -  [ Response Schema Python/CSV Agent ](https://www.reddit.com/r/LangChain/comments/1az69hi/response_schema_pythoncsv_agent/) , 2024-02-25-0910
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

     
 
all -  [ Looking to Hire a Teacher to Meet Twice a Month ](https://www.reddit.com/r/LangChain/comments/1az5do0/looking_to_hire_a_teacher_to_meet_twice_a_month/) , 2024-02-25-0910
```
Hi!

&#x200B;

I am a Data Scientist by trade and have been working with Langchain specifically for about 2 months now. 
I enjoy coding both inside and outside of work.

&#x200B;

I'm not looking for any help with work.  


I want a non-acad
emic tutor who I meet with once or twice a month via Zoom and I can use it like office hours. 

&#x200B;

If you would b
e interested in exploring random passion projects and ideas with me please send a DM and we can discuss rates and hours 
there. I'm flexible haha.

&#x200B;

P.S. I'd love recommendations on how I can accomplish finding someone like this as 
well if anyone has thoughts.

&#x200B;

&#x200B;
```
---

     
 
all -  [ Developing Langchain Agents with the MinIO SDK for LLM Tool-Use ](https://www.reddit.com/r/minio/comments/1az41o8/developing_langchain_agents_with_the_minio_sdk/) , 2024-02-25-0910
```
In this guide, we prioritize practicality, steering towards actionable development practices. We invite developers to em
brace the potential that lies in the union of Langchain and MinIO SDK, to not only innovate but also to redefine the bou
ndaries of what can be achieved with the intelligent automation of today's digital tools.

[https://blog.min.io/minio-la
ngchain-tool/?utm\_source=reddit&utm\_medium=organic-social+&utm\_campaign=minio\_langchain\_tool+](https://blog.min.io/
minio-langchain-tool/?utm_source=reddit&utm_medium=organic-social+&utm_campaign=minio_langchain_tool+)
```
---

     
 
all -  [ Help - tutorial needed ](https://www.reddit.com/r/LangChain/comments/1az3nu8/help_tutorial_needed/) , 2024-02-25-0910
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

     
 
all -  [ Hello from the Feast project (https://feast.dev)! The open-source Feature Store. ](https://www.reddit.com/r/mlops/comments/1az3fz6/hello_from_the_feast_project_httpsfeastdev_the/) , 2024-02-25-0910
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

     
 
all -  [ Youtube loader with timecodes ](https://www.reddit.com/r/LangChain/comments/1az2t9r/youtube_loader_with_timecodes/) , 2024-02-25-0910
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

     
 
all -  [ RAG with OpenAI assistant API ](https://www.reddit.com/r/LangChain/comments/1az27pt/rag_with_openai_assistant_api/) , 2024-02-25-0910
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

     
 
all -  [ FlowiseAI python alternative  ](https://www.reddit.com/r/LangChain/comments/1az0uae/flowiseai_python_alternative/) , 2024-02-25-0910
```
Hi,
Is there any FlowiseAI alternative in python? 
Or Is there any way to export the flows created in FlowiseAI to pytho
n code?
```
---

     
 
all -  [ Rate my resume guys ](https://i.redd.it/7oe03y3ogjkc1.jpeg) , 2024-02-25-0910
```

```
---

     
 
all -  [ LCEL along with legacy chain  ](https://www.reddit.com/r/LangChain/comments/1ayv0uz/lcel_along_with_legacy_chain/) , 2024-02-25-0910
```
I have been trying to use Langhain, especially the new custom composed LCEL chains in combination with the legacy consti
tutional chains that allow me to do guardrails. 

But because constitutional chains are not in the new format of LCEL, I
 couldn't figure out a way to make it work. Legacy constitutional chain accepts only another legacy chain as an input. S
o I can't put them together. 

Help will be appreciated!
```
---

     
 
all -  [ How to remove the prompt and prompt template from the response when invoking a chain? ](https://www.reddit.com/r/LangChain/comments/1ayszzh/how_to_remove_the_prompt_and_prompt_template_from/) , 2024-02-25-0910
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

     
 
all -  [ Check out this LangChain (Generative AI framework) playlist with 60+ tutorials ](https://www.reddit.com/r/AI__India/comments/1aysq8c/check_out_this_langchain_generative_ai_framework/) , 2024-02-25-0910
```
Hey everyone, checkout this playlist with 60+ tutorials for learning any LangChain concept from scratch with codes. [htt
ps://www.youtube.com/watch?v=OagbDJvywJI&list=PLnH2pfPCPZsKJnAIPimrZaKwStQrLSNIQ](https://www.youtube.com/watch?v=OagbDJ
vywJI&list=PLnH2pfPCPZsKJnAIPimrZaKwStQrLSNIQ) 
```
---

     
 
all -  [ Learning LangChain (Generative AI framework) from scratch ](https://www.reddit.com/r/ArtificialInteligence/comments/1aysosk/learning_langchain_generative_ai_framework_from/) , 2024-02-25-0910
```
Hey everyone, checkout this playlist with 60+ tutorials for learning any LangChain concept from scratch with codes. http
s://www.youtube.com/watch?v=OagbDJvywJI&list=PLnH2pfPCPZsKJnAIPimrZaKwStQrLSNIQ
```
---

     
 
all -  [ Save chatbot to pdf ](https://www.reddit.com/r/learnmachinelearning/comments/1aypd76/save_chatbot_to_pdf/) , 2024-02-25-0910
```
I'm using huggingface and langchain for a chatbot then building a gradio UI for launching. How can I extract my chat his
tory and download it from a gradio button. 
```
---

     
 
all -  [ Cohere rerank, contextual compression and ContextReorder, can I just use the top document?  ](https://www.reddit.com/r/LangChain/comments/1ayl2mb/cohere_rerank_contextual_compression_and/) , 2024-02-25-0910
```
So I’m trying to get a specific chunk of data and it does retrieve it perfectly but it seems to apply the lower matched 
chunks as well. Is there a way to just use the very top ranked chunked document? It seems to be out of order if contextu
ally if we apply all the chunks in a response 

```
---

     
 
all -  [ Good tool for copywriting? ](https://www.reddit.com/r/LangChain/comments/1aykmn5/good_tool_for_copywriting/) , 2024-02-25-0910
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

     
 
all -  [ Without open AI or Gemini api key ](https://www.reddit.com/r/LangChain/comments/1ayipqy/without_open_ai_or_gemini_api_key/) , 2024-02-25-0910
```
So I was planning to build a chatbot with langchain. But I can't use open Ai or any gpt api keys coz of privacy. Is ther
e any other work around for this ? 
```
---

     
 
all -  [ MLOps from a hiring manager perspective. Am I doing this wrong? ](https://www.reddit.com/r/mlops/comments/1ayfkx3/mlops_from_a_hiring_manager_perspective_am_i/) , 2024-02-25-0910
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

     
 
all -  [ RAG evaluation framework ](https://www.reddit.com/r/LangChain/comments/1ayfdhs/rag_evaluation_framework/) , 2024-02-25-0910
```
Hi,

I am looking for some good resources for RAG evaluation.
```
---

     
 
all -  [ LangSmith for evaluation or something else? ](https://www.reddit.com/r/LangChain/comments/1ayaf7p/langsmith_for_evaluation_or_something_else/) , 2024-02-25-0910
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

     
 
all -  [ Vertex AI Slowwwwww ](https://www.reddit.com/r/googlecloud/comments/1ay7q54/vertex_ai_slowwwwww/) , 2024-02-25-0910
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

     
 
all -  [ ollama/langchain streaming with tools ](https://www.reddit.com/r/ollama/comments/1ay7ojf/ollamalangchain_streaming_with_tools/) , 2024-02-25-0910
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

     
 
all -  [ Extracting metadata from a PDF and converting to JSON using LangChain and GPT ](https://www.reddit.com/r/LangChain/comments/1ay6vx4/extracting_metadata_from_a_pdf_and_converting_to/) , 2024-02-25-0910
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

     
 
all -  [ Ecosystem around LangChain ](https://www.reddit.com/r/LangChain/comments/1ay1c6a/ecosystem_around_langchain/) , 2024-02-25-0910
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

     
 
all -  [ LangChain Agent 를 활용하여 #chatgpt 를 #업무자동화 에 적용하는 방법🔥🔥 https://www.facebook.com/groups/aitutor21/perma ](https://www.reddit.com/r/chatgpt_newtech/comments/1axvptn/langchain_agent_를_활용하여_chatgpt_를_업무자동화_에_적용하는_방법/) , 2024-02-25-0910
```
LangChain Agent 를 활용하여 #chatgpt 를 #업무자동화 에 적용하는 방법🔥🔥   [https://www.facebook.com/groups/aitutor21/permalink/195027638538
5787/?mibextid=oMANbw](https://www.facebook.com/groups/aitutor21/permalink/1950276385385787/?mibextid=oMANbw)
```
---

     
 
all -  [ Langchain Map Reduce  ](https://www.reddit.com/r/learnmachinelearning/comments/1axkz9u/langchain_map_reduce/) , 2024-02-25-0910
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

     
 
all -  [ PDF Document Loader not working Langchain ](https://www.reddit.com/r/LangChain/comments/1axi03f/pdf_document_loader_not_working_langchain/) , 2024-02-25-0910
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

     
 
all -  [ LangChain - RunnableParallel ](https://www.reddit.com/r/LangChain/comments/1axhxg5/langchain_runnableparallel/) , 2024-02-25-0910
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

     
 
all -  [ asynchronous requests ](https://www.reddit.com/r/LangChain/comments/1axhkki/asynchronous_requests/) , 2024-02-25-0910
```
Greetings, I have a question about langchain. I have built a database query creation wizard using a langchain agent and 
openai. The thing is that when used by several people the program begins to delusion who should respond first and they e
nd up responding where they shouldn't be. I want to know if there is any tutorial or any way I can use asynchronous call
s so that I can solve this problem and wizard ends up answering one question at a time.
```
---

     
 
all -  [ Buying new mac, have any SVD compatibility info or advice? ](https://www.reddit.com/r/StableVideoDiffusion/comments/1axgpgo/buying_new_mac_have_any_svd_compatibility_info_or/) , 2024-02-25-0910
```
Hi there, I'm about to replace my ancient intel mac. I’ve been doing some work with open-ai and langchain but want to tr
y out SVD. I think thinking I'd buy a MacBook pro m2 max with 64 gigs of ram? Whats you take on that with with SVD? Anyt
hing I should know? 

```
---

     
 
all -  [ Dialogflow +RAG ](https://www.reddit.com/r/LangChain/comments/1axfp44/dialogflow_rag/) , 2024-02-25-0910
```


Iam using nodejs and firebase with dialogflow ES . And I created a RAG function to get response to the userquery by qu
erying PINECONE database . But the function execution  is taking 5 sec.how can I reduce the function execution time ... 

I am Currently using langchain...
```
---

     
 
all -  [ MS In Computer Science or Data Science, In US or Europe, Job etc ](https://www.reddit.com/r/developersIndia/comments/1axd4r2/ms_in_computer_science_or_data_science_in_us_or/) , 2024-02-25-0910
```

Greetings developers,

I recently completed my CS degree and currently work at one of the big 4 tech companies(for 6 mo
nths). While I have some experience in web development from my college projects, I now focus on areas like Gen AI, LLM, 
and Langchain. I am considering pursuing a master's degree, but I'm unsure about which course to choose. I'm torn betwee
n data science and full-stack development. Additionally, I am keen on securing a scholarship, which is why I am contempl
ating studying in Europe, particularly Germany, as scholarships are more accessible there compared to the US.

My ultima
te goal is to secure a job after completing my master's degree. I've noticed that the US tends to offer higher salaries 
for fresh graduates, but I'm also curious about the promotion opportunities in both countries.

I would greatly apprecia
te your suggestions on the following:

1. Should I pursue a master's in CS or data science?
2. Is it advisable to study 
in the US or Europe?
3. Would it be wise to continue working here in India for the time being?

Thank you for your insig
hts.
```
---

     
 
all -  [ Mixtral-8X7B - Local vs API performance ](https://www.reddit.com/r/LocalLLaMA/comments/1axbsjx/mixtral8x7b_local_vs_api_performance/) , 2024-02-25-0910
```
I am using Langchain with an Agent setup. The agent has access to two tools that are both retrievers for specific databa
ses.

1. I use 'mixtral-8x7b-instruct-v0.1.Q5\_K\_M.gguf' from the Bloke and it's performance is abismal. It struggles w
ith generating tool actions and responding in a sensical way.
2. However when i use Mistral's API with the small model (
Mixtral-8X7B-v0.1) it runs flawlessly and answers very intelligently.

Any ideas what might cause this?

&#x200B;
```
---

     
 
all -  [ State of AI agents in real-world ](https://www.reddit.com/r/LocalLLaMA/comments/1axb1dq/state_of_ai_agents_in_realworld/) , 2024-02-25-0910
```
What's the current state of autonomous agents? Does it actually work?  
I played with agents about 9 months ago and it s
eemed to me like it's overhyped. Yes, I've seen people ordering 100 Starbucks latte from DoorDash using agent on a hacka
ton and it was the best demo I've seen deploying agents.   
So, I think you could build impressive showcases with AI age
nts, but generally they weren't useful in practice. When confronted with open questions reality, they started to cycle i
n picking tools, couldn't format responses (I guess this has changed with OpenAI functions/tools), basically it just too
k too long and the results weren't good.   


So my question is: **Has anyone build conversation AI agents that are usab
le real-world products?** Are there any **repos** you could refer me to (besides Langchain, more like some repos leverag
ing such frameworks)?
```
---

     
 
all -  [ Langchian Rust ](https://www.reddit.com/r/rust/comments/1axar0y/langchian_rust/) , 2024-02-25-0910
```
# Langchian Rust

I'm delighted to share a personal endeavor of mine: a Rust port of Langchain. Having been a core contr
ibutor to the official Go Lang port of Langchain (langchaingo), I decided to challenge myself further by exploring the R
ust programming language. This project is an independent effort to reimagine Langchain's capabilities within the Rust ec
osystem, known for its emphasis on safety and performance.

Here's my take on bringing Langchain to Rust, a journey driv
en by my passion for learning and contributing to the open-source community:🔗 [https://github.com/Abraxas-365/langchain-
rust](https://github.com/Abraxas-365/langchain-rust)

This initiative is a personal project, not an official port, and r
epresents my ongoing journey to expand my technical skills and contribute to innovative applications of language models.
 I'm excited about the learning opportunities and potential applications this project might unlock.I warmly invite you t
o explore the repository, share your insights, or even contribute. Your feedback and contributions would not only be wel
come but also deeply appreciated, as they enrich the project and the wider community.Let's explore the possibilities tha
t lie at the intersection of Rust and AI together!
```
---

     
 
all -  [ Azure search Scalability ](https://www.reddit.com/r/LangChain/comments/1ax42kn/azure_search_scalability/) , 2024-02-25-0910
```
Why Azure search so much expensive for me. It costing 250 per search unit.  I am actually doing load testing. and If I w
ant to search 50 concurrent queries, How many search units do I required. Can we assume  one search unit search only que
ry.

&#x200B;

https://preview.redd.it/mu6916z3f4kc1.png?width=1359&format=png&auto=webp&s=020d4c80201db2d4e8f50bb5cb4f3
d61958cd055
```
---

     
 
all -  [ Why do people say Langchain is overengineered? Please explain ](https://www.reddit.com/r/OpenAI/comments/1awy64a/why_do_people_say_langchain_is_overengineered/) , 2024-02-25-0910
```
Hi all,

I'm not a software engineer by any means. I'm just a regular data scientist who is getting some hands on experi
ence with LLMs. I have played with the OpenAI API and Langchain. I find the Python OpenAI API fairly 'simple and intuiti
ve' to use compared to Langchain. The documentation for Langchain is pretty hard to read too. This is just my personal o
pinion.

What I don't understand is this? I have seen many people say Langchain is \*overengineered\*. What does it real
ly mean? And why? I tried my best to go through the points raised in other forums but couldn't understand much. 
```
---

     
 
all -  [ Guidance on streaming   ](https://www.reddit.com/r/LangChain/comments/1awxbfl/guidance_on_streaming/) , 2024-02-25-0910
```
I have some endpoints exposed on my fastap+langchain webservice; endpoints support async; underneath expose chain ainvok
es;

Endpoints sometimes take time 30-120 secs

With langsmith confirmed its openai models where most time is spent 

Wa
s looking for a proper architecture to support streaming of output and intermediate steps to evade long delays on the fr
ontend?

Do I need to handle it for each endpoint or there could be one sink I could expose for user to query?

Not usin
g any backend queue like Celery.

Please guide 🙏 
```
---

     
 
all -  [ Langchain CSV  and llama2 ](https://www.reddit.com/r/LangChain/comments/1awub34/langchain_csv_and_llama2/) , 2024-02-25-0910
```
Hi 

I loaded CSV with CSV loader and used llama2 to get data from csv but it is not working. It is getting wrong result
s for every prompt. 

I used  huggingface sentence transformer embedding and loaded in vector db. If I do similarity sea
rch I'm able to see all data. But when I train that to llama2 model. For every input it is showing same result.

Can you
 please help me with this?
```
---

     
 
all -  [ Unusual experiences with the indexing API ](https://www.reddit.com/r/LangChain/comments/1awu6db/unusual_experiences_with_the_indexing_api/) , 2024-02-25-0910
```
\- I conducted a test with the langchain indexing api. In short, this led to a much slower upsert time to my vector DB t
han just using the traditional langchain embeddings method, and it also produced an unusually large amount of vectors. T
his makes no real sense to me as it was embedding the same chunked textual material and I'm trying to figure out if ther
e are variables I haven't accounted for properly. 
```
---

     
 
all -  [ nvim urgently needs good AI plugins ](https://www.reddit.com/r/nvim/comments/1awry69/nvim_urgently_needs_good_ai_plugins/) , 2024-02-25-0910
```
There was a day in which neovim with LSP support, Treesitter, and Lua plugins was released.

It was the beginning of a n
ew era of the vim family of editors and it suddenly became in pair with its main rival made by the open source enemy Mic
ro$oft.

These days that coding goes hand in hand with AI tools, however, neovim is getting behind again.

1. Copilot fo
r vscode has a chat node which is lacking in neovim version
2. Sending context to AI models from neovim is severely limi
ted and basically impossible (e.g. sending the whole file or the whole workspace)
3. Online search ala Phind.com is miss
ing from all the plugins.

Vscode instead provides plugins such as phind.com, copilot, ChatGPT, which are way more power
ful than the nvim counterparts. Phind.com is especially extremely powerful, not because of the model themselves but beca
use of the functionalities it provides (it's super easy to add specific files to the query or specific symbols in order 
to describe what should be changed).

Recently, I discovered cursor.sh , which is a vscode fork that promises many usefu
l functionalities that are totally missing in the vim world.

We should basically include langchain or similar in our ai
 plugins in order to build indexed databases of symbols and files, use online searches, and improve the AI tools. 

But 
how? I fear the main issue here is Lua...
```
---

     
 
all -  [ One Drive RAG & Text to SQL ](https://www.reddit.com/r/LangChain/comments/1awm22j/one_drive_rag_text_to_sql/) , 2024-02-25-0910
```
Hi there,

I want to use a RAG for documents on One Drive and a Text to SQL as well in the same chat bot.

How would the
 Agent differentiate if the question needs to do the RAG (One Drive) or Interact with the database based on the user's q
uestion?

Is it a solved problem? If yes, how?
```
---

     
 
all -  [ This might seem like the dumbest question ever, but I can't get my Azure OpenAI service to work with ](https://www.reddit.com/r/LangChain/comments/1awk5pm/this_might_seem_like_the_dumbest_question_ever/) , 2024-02-25-0910
```
Wtf am i doing wrong?

I've got my Azure OpenAI service running ,but some reason Azure still gives the older version of 
the OpenAI's code despite the new version being out months now. 

But anyway, I'm literally just trying to get a f\*ckin
g basic prompt sent to the AI and print it's response.

Does anyone have a simple guide on how to do this basic everyday
 shit that that OpenAI literally gives you instantly from the playground?

Am I asking too much? I've combed through so 
many tutorials and asked so many LLMs, yet I can't get this basic thing to work.
```
---

     
 
all -  [ Langchian Rust ](https://www.reddit.com/r/LangChain/comments/1awk4i8/langchian_rust/) , 2024-02-25-0910
```
# 🎉 Exciting Personal Project Alert! 🎉

I'm delighted to share a personal endeavor of mine: a Rust port of Langchain. Ha
ving been a core contributor to the official Go Lang port of Langchain (langchaingo), I decided to challenge myself furt
her by exploring the Rust programming language. This project is an independent effort to reimagine Langchain's capabilit
ies within the Rust ecosystem, known for its emphasis on safety and performance.

Here's my take on bringing Langchain t
o Rust, a journey driven by my passion for learning and contributing to the open-source community:🔗 [https://github.com/
Abraxas-365/langchain-rust](https://github.com/Abraxas-365/langchain-rust)

This initiative is a personal project, not a
n official port, and represents my ongoing journey to expand my technical skills and contribute to innovative applicatio
ns of language models. I'm excited about the learning opportunities and potential applications this project might unlock
.I warmly invite you to explore the repository, share your insights, or even contribute. Your feedback and contributions
 would not only be welcome but also deeply appreciated, as they enrich the project and the wider community.Let's explore
 the possibilities that lie at the intersection of Rust and AI together!
```
---

     
 
MachineLearning -  [ [D] Graphs + vectordbs? Need your input: Cognee.ai . AI Data Pipelines for Real-World Production (Pa ](https://www.reddit.com/r/MachineLearning/comments/1aweo71/d_graphs_vectordbs_need_your_input_cogneeai_ai/) , 2024-02-25-0910
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

     
 
MachineLearning -  [ [D] AI projects Suggestions ](https://www.reddit.com/r/MachineLearning/comments/1aunkmw/d_ai_projects_suggestions/) , 2024-02-25-0910
```
Hi Everyone, I need a suggestion to create AI courses for students ( Hands-on AI projects). I am thinking about the late
st AI trends such as Langchain, RAG, and vector databases. In each project, there can be multiple tasks, and the main th
ing is each task should have an automated system in which we can verify whether students have done it correctly or not.


For example: Project with visualization cannot be automatically tested. 

For example: A project with visualization can
not be automatically tested. . em can verify if the length of the text is smaller we can verify that it is correct.
```
---

     
 
MachineLearning -  [ [D] What's the standard practice for setting initialization prompts and maintaining context when swi ](https://www.reddit.com/r/MachineLearning/comments/1aq78ao/d_whats_the_standard_practice_for_setting/) , 2024-02-25-0910
```
Hi I am trying to build a modularized LLM application using Langchain where within any individual conversation the app c
an seamless switch between multiple LLMs to respond to the query, for example:

1. User: What's 1+ 1?
2. App (GPT-3.5): 
1+1 is 2
3. User: Concatenate the last name of the current president of the US with the answer from your last response
4
. App (Gemini Ultra): Biden2

I have two technical questions that I hope this subreddit can help answer:

1. What's the 
standard practice for setting the initialization prompts or background prompts? For example I want to tell this App that
 'your name is Bob', and I want this App to continuously remember it's Bob regardless how long the conversation has gott
en or any switching between LLMs. Do I set this at the beginning of the conversation or before every single response?
2.
 What's the standard practice for conversation memory management when there's switching of LLM involved within one conve
rsation? Do I store all the conversation history within a vector database and do a index search prior to any individual 
response?
```
---

     
 
MachineLearning -  [ Whats in your RAG setup? [D] ](https://www.reddit.com/r/MachineLearning/comments/1apcp2w/whats_in_your_rag_setup_d/) , 2024-02-25-0910
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

     
 
MachineLearning -  [ [D] What's the best current RAG setup that would work with a local LLM? ](https://www.reddit.com/r/MachineLearning/comments/1ag6bo7/d_whats_the_best_current_rag_setup_that_would/) , 2024-02-25-0910
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

     
 
MachineLearning -  [ [P]: Anukool: My job hunting assistant ](https://www.reddit.com/r/MachineLearning/comments/1adu3tw/p_anukool_my_job_hunting_assistant/) , 2024-02-25-0910
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

     
 
deeplearning -  [ [D] WebVoyager: Navigating Digital Cosmos with LangGraph & Multimodal Models ](https://www.reddit.com/r/deeplearning/comments/1altlca/d_webvoyager_navigating_digital_cosmos_with/) , 2024-02-25-0910
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

     
 
deeplearning -  [ [D] Langchain Elevates with Step-Back Prompting using RAGatouille ](https://www.reddit.com/r/deeplearning/comments/1agtyeh/d_langchain_elevates_with_stepback_prompting/) , 2024-02-25-0910
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

     
 
deeplearning -  [ Become an AI Developer (Free 9 Part Series) ](https://www.reddit.com/r/deeplearning/comments/1afgp2r/become_an_ai_developer_free_9_part_series/) , 2024-02-25-0910
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

     
 
deeplearning -  [ DSPy Explained! ](https://www.reddit.com/r/deeplearning/comments/1adypks/dspy_explained/) , 2024-02-25-0910
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

     
