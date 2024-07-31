 
all -  [ Confused on What to Use for Chatbot? ](https://www.reddit.com/r/LangChain/comments/1eg41kn/confused_on_what_to_use_for_chatbot/) , 2024-07-31-0909
```
Hello -- I am trying to incrementally create a chatbot that will do three things (depending on user input)

1. Summarize
 a JSON specification for the product (thinking some simple prompt engineering here should be able to do this)
2. Answer
 questions about some ontologies/hierarchies we maintain (thinking RAG)
3. Generate / Modify a JSON specification for th
e product (thinking a fine-tuned model for this specific structured output we use - internally before JSON we use pydant
ic models)

My question is what is the best way to use LangChains building blocks to properly route a user's request to 
the appropriate model within the chat?

I was reading the docs and I wasn't sure if I needed to create a custom agent (a
nd somehow let it decide which of the three to use?) or if I should do a 'dumber' rule-based function to then determine 
which of the three to use and just have that integrate with the basic chatbot.

Any help / guidance would be greatly app
reciated! Am supposed to look into this for work and a little out of my depth right now.
```
---

     
 
all -  [ Discussion: How to dynamically modify tool descriptions in Langgraph? ](https://www.reddit.com/r/LangChain/comments/1eg12qg/discussion_how_to_dynamically_modify_tool/) , 2024-07-31-0909
```
Does anyone know how to dynamically modify the description of a Tool?

I am using ToolNode in Langgraph with tools defin
ed with the decorator, and to define the args, I am using a Pydantic BaseModel, something like:

    class ToolInput(Bas
eModel):
        arg_1: str = Field(description='...', type='string')
        ...
    
    u/tool('get_data', args_schem
a=ToolInput)
    def get_data(
        arg_1: str,
        ...
    ):
        '''Get the data, the accepted values of th
e arg_1 are:
        - val_1, val_2, val_3 ... val_n
        '''
        ...
        return data
    

The point is, I w
ant to dynamically pass data from the graph's state to construct the prompt, something like:

    class ToolInput(BaseMo
del):
        arg_1: int = Field(description='...', type='string')
        ...
    
    @tool('get_data', args_schema=To
olInput)
    def get_data(
        arg_1: str,
        ...
    ):
        '''Get the data, the accepted values of the ar
g_1 are:
        - {val_1}, {val_2}, {val_3}, ... , {val_n}
        '''
        # Where the {val_x} come from the State,
 for example state['available_values']
        ...
        return data
    

Does anyone have an idea of how I can do th
is?
```
---

     
 
all -  [ RAG and AI agents bootcamp by AI planet ](https://www.reddit.com/r/Agentic_AI/comments/1eg0nz9/rag_and_ai_agents_bootcamp_by_ai_planet/) , 2024-07-31-0909
```
I really love studying with AI planet since the community is available to help and tries to make knowledge clear.

# RAG
 and Agents Bootcamp is now live and is FREE

From AI planet 'We are proud to announce that we are releasing RAG and Age
nts Bootcamp. 

* Ever wondered about building a human clone that mimics a real person? Have you ever thought about crea
ting an autonomous AI that mimics human characteristics and has key elements such as a brain, perception, the ability to
 plan, reflect, take action, and possess memory just like any other human? These are known as Autonomous Agents or assis
tants. If you're curious about learning and building them to solve meaningful problems, then you must consider joining t
he bootcamp.
* Imagine another scenario: you have a vast amount of custom data and need an assistant, similar to ChatGPT
, that can provide factually accurate answers based on your specific data source. This integration between large languag
e models, such as GPT, and custom data can be achieved using Retrieval Augmented Generation (RAG).  If you're curious ab
out building your own GPT model for your data, this bootcamp is designed for you.
* This bootcamp will cover the theory 
and implementation of concepts such as Retrieval-Augmented Generation (RAG), prompt engineering, vector databases, auton
omous agents, and much more.  
* We will also discuss no-code tools like the GenAI stack and open-source frameworks such
 as BeyondLLM, Langchain, OpenAGI, LlamaIndex, crewAI, and more.  
* The bootcamp will include real-time projects and li
ve sessions designed to enhance your AI knowledge and skills.

  
 Register: [https://aiplanet.com/bootcamps/rag-agents-
bootcamp](https://mail.dphi.tech/l/qcQkzS3TJnwEp7DalPu8rQ/jNoIl6P6Ci7XpypSQWJ9HQ/RUq4AKbxw4rPiu1q892Bjbnw) '
```
---

     
 
all -  [ Is there a tool for finds optimal pipeline for a RAG? ](https://www.reddit.com/r/LangChain/comments/1efz9nj/is_there_a_tool_for_finds_optimal_pipeline_for_a/) , 2024-07-31-0909
```
Is there a tool out there that can find the optimal pipeline for a RAG for a given data? 

  
Im planning to build one a
nd was wondering how helpful something like this would be?
```
---

     
 
all -  [ AI web app TS vs Python + FastAPI? ](https://www.reddit.com/r/LangChain/comments/1efz85n/ai_web_app_ts_vs_python_fastapi/) , 2024-07-31-0909
```
I come from an AI developer background but i want to build an AI web app myself. 

I have 2 options:  
A. Build every co
mponents ( calling AI models, parsing , injestion ) in TS/NextJS which im not familiar with at all, but if this will hel
p long term im willing to put in the work.

B. Deploy my AI components using FastAPI. Im much more familiar with python,
 but im trying not to overcomplicate the architecture of my first webapp ( need to host frontend and backend separately 
)

  
Has anyone deploy any AI webapps/ SAAS here? Would like to have some suggestions
```
---

     
 
all -  [ AI-Assisted Data Science - Non-Fiction ](https://www.reddit.com/r/wroteabook/comments/1efyynh/aiassisted_data_science_nonfiction/) , 2024-07-31-0909
```
Use ChatGPT to analyze text, images, audio, and tables!

Large language models can unlock valuable insights hidden in yo
ur data. This book teaches you how to leverage Python and language models to perform a variety of data analysis tasks. T
opics covered include:

* Classifying text documents
* Analyzing images and videos
* Transcribing audio files
* Text-to-
SQL query interfaces
* Fine-tuning and cost optimization
* Building apps with LangChain
* Creating agents for data analy
sis

[https://www.manning.com/books/ai-assisted-data-science](https://www.manning.com/books/ai-assisted-data-science)
```
---

     
 
all -  [ Serializing/Deserializing Messages? Am I using packages correctly? (LangGraph) ](https://www.reddit.com/r/LangChain/comments/1efvx6d/serializingdeserializing_messages_am_i_using/) , 2024-07-31-0909
```
**Preface:**

Lest it becomes an XY problem, my initial problem is that I need to count token usage, using the provided 
`model.get_num_tokens_from_messages` from their `langchain_openai`. However, due to the way I save and load history, thi
ngs keep breaking.

**Introduction:**

I am attempting to handle history management (save/load of conversations and mess
ages) myself, since I can't quite understand checkpoints yet, and it is also in current heavy development. While LangCha
in uses their instances of BaseMessage (AIMessage, HumanMessage, etc), I found that doing `message.to_json().get('kwargs
', {})` will return a dict representing the json version that the LLM really sees. I extracted a list of these and fed i
t to an LLM directly, and realized the LLM was still able to understand everything. So saving these dicts and loading th
em/feeding them to the LLM worked just fine.

  
However, now I need to add token count to the mix. I use AzureOpenAICha
t which does not support token counts for `astream_events`, so I have to get it using `model.get_num_tokens_from_message
s`. This is where my problems arise.

Here is the process:

**Attempt 1)**

**Error:**

    message does not have attrib
ute 'content'

**Investigation:**

Turns out, `get_num_tokens_from_messages` calls a `_convert_message_to_dict` function
. Some of my messages are already dicts, so when this value is passed to the `_format_message_content` function, it cras
hes and gives an error.

**Thoughts:** It is weird that their `_convert_message_to_dict` function doesn't attempt to acc
ount for the case that some in the list may already be dicts.

**Solution:** No worries. I just did an extra step to con
vert all loaded message dicts back to subclasses of `BaseMessage`, using their `_convert_dict_to_message` function per m
essage upon load.

  
**Attempt 2)**

**Error:**

    dict has no property 'role'

**Investigation:**

That's right. The
 function expects a property 'role'. Since I stored and loaded the `kwargs` from each BaseMessage, they have the propert
y 'type' instead of 'role'.

**Thoughts:** It is weird that while they themselves use 'type' instead of 'role', their `_
convert_dict_to_message` function only looks for role, and doesn't try to default to 'type'.

**Solution:** No worries, 
upon saving messages, I just did an extra step to also set the 'role' of the dict to the existing 'type' value, then sto
re it.



**Attempt 3)**

**Error:**

    role 'ai' unknown. expecting 'assistant', 'user', 'tool', 'function', or 'syst
em'

**Investigation:**

Although their json generates additional types, this method only expects these few.

**Thoughts
:** It is weird that they use 'ai', 'assistant', 'human', 'tool', 'function', 'system', 'chat', etc, but limit the expec
ted roles.

**Solution:** No worries, upon saving messages, I will do an extra step to also manually convert their types
, to align with their expected roles.

  
**Attempt 4)**

**Error:**

[  none is not an allowed value \(type=type\_error
.none.not\_allowed\)](https://preview.redd.it/jn5o6f5c2ofd1.png?width=1039&format=png&auto=webp&s=5d68300fdedf9153ecc336
ab594fbb6001e5431e)

>*flips table*

**Investigation:**

The message trace itself is not very helpful for debugging and 
determining the exact cause, but based on experience (and it mentioning the tool call) I'm assuming that it is due to th
e AIMessage with a tool call. Usually that has no content value (an empty string, which somehow becomes a None value int
ernally), but it results in this error.

Deeper investigations show that the to\_json method's kwargs creation omits val
ues that are falsy, which results in its 'content' property not being set or saved for AIMessages with tool calls, thus 
causing the error.

**Thoughts:** It is strange that the BaseMessage's content attribute is of type `Union[str, List[Uni
on[str, Dict]]]`, which gives the error when None is passed, rather than default to an empty string.

**Solution?** I am
 still experimenting with this. Either to add an extra step when saving to manually add an empty content property to the
 dict as well, or call `message.json` or `message.dict` rather than `message.to_json`. Then I'll have to continue testin
g to see if it will work.

  
**Conclusion:**

All of this, just to get the token usage.

Am I going about this the wron
g way? It seems like I am fighting the package more than undergoing development in this case. Are all my thoughts valid?
 Should the langchain\_openai package be updated to support more of the features langgraph provides for better integrati
on? Or is that already handled in another library and I am using the wrong ones?
```
---

     
 
all -  [ Official Discord? ](https://www.reddit.com/r/LangChain/comments/1efszqi/official_discord/) , 2024-07-31-0909
```
Hi,   
Is there an official discord server for LangChain? Seems like all the links I found are invalid.
```
---

     
 
all -  [ I can't run my simple model ](https://www.reddit.com/r/LangChain/comments/1efsssr/i_cant_run_my_simple_model/) , 2024-07-31-0909
```
This is my code:

    from langchain_google_vertexai import VertexAI
    from langchain.prompts import PromptTemplate
  
  from langchain.chains import LLMChain
    
    
    class GeminiProcessor:
        def __init__(self, model_name, proj
ect):
            self.model=VertexAI(
                model_name=model_name,
                project=project
          
  )
        
    class bookProcessor:
        def __init__(self, topic:str, genai_processor: GeminiProcessor):
         
   self.topic = topic
            self.GeminiProcessor = genai_processor
            self.system_template = '''
        
        Your task is to generate a general description of a book on the topic of {keyword}. 
                '''
       
 
        def generate_ebook(self):
            
            prompt = PromptTemplate.from_template(
               templ
ate=self.system_template,
               )
                    
            # creating chain
            chain = prompt 
| self.GeminiProcessor.model 
            output = chain.invoke(self.topic)
            print('output:', output)
       
     
            return output

I don't really know why this is not working.

I keep getting this weird error: 

  


 
   line 166, in <listcomp>
        'category': rating.category.name,
                    ^^^^^^^^^^^^^^^^^^^^
    Attrib
uteError: 'int' object has no attribute 'name'

Can anyone help with this bug? I'm a beginner at LangChain so any help w
ould be appreciated.
```
---

     
 
all -  [ I built a memory framework for LLMs and Agents ](https://www.reddit.com/r/Python/comments/1efsjgy/i_built_a_memory_framework_for_llms_and_agents/) , 2024-07-31-0909
```
**Why?**

I was building an AI-powered dating app. I couldn't find a memory layer that takes up less RAM, free and easy 
to use. This led to the concept of redcache-ai.

**What My Project Does**

It dynamically retains information across dif
ferent user sessions. This allows the user to improve semantic search and have context.

**Target Audience** 

Anyone bu
ilding applications that leverage Large Language Models. This includes customer support apps, apps that use semantic sea
rch and dating apps.

**Comparison** 

* Easy to setup: it's a python package. Simply use pip install redcache-ai.
* Tak
es up less memory.
* Extensible: You can store your text memory to disk or sqlite. Enhance memory using LLM providers.
*
 Local testing and Cloud hosting: the framework locally and host it on your cloud provider of choice.

**What's worse ab
out Redcahe-ai**.

* Currently, OpenAI is the only supported LLM provider.
* Alpha version. I mostly tested it on Window
s OS.

The software is highly customizable. I've done my best to add comments and make the code readable.

src; [https:/
/github.com/chisasaw/redcache-ai](https://github.com/chisasaw/redcache-ai)

Inspired by Langchain.
```
---

     
 
all -  [ Llama Stack [toolchain + agentic-system] ](https://www.reddit.com/r/LocalLLaMA/comments/1efq2gd/llama_stack_toolchain_agenticsystem/) , 2024-07-31-0909
```
In the new realease of Llama models there was also a mention to '*the Llama Stack API, a standard interface we hope will
 make it easier for third-party projects to leverage Llama models*'. I´ve found both [llama-toolchain](https://github.co
m/meta-llama/llama-toolchain) and [agentic-system](https://github.com/meta-llama/llama-agentic-system), but no documenta
tion referring to the overall ecossystem of Llama Stack or how these tools can be deployed in more robust workflows.

Is
 there a documentation page I might be missing? Or is it too early to expect proper documentation on how to orchestrate 
these tools locally? 

Im wondering if these will replace the common langchain, autogen or llama-index modules we have b
een using.
```
---

     
 
all -  [ ChromaDB Internal Server Error when trying to implement RAG service on a server ](https://www.reddit.com/r/LangChain/comments/1efp23j/chromadb_internal_server_error_when_trying_to/) , 2024-07-31-0909
```
Hi! I'm trying to implement a RAG service for a chatbot that retrieves information from a document based on text queries
. For the most part my code works when implemented in an endpoint, but when executing for a second time i get this: 'Per
missionError: \[WinError 32\] The process cannot access the file because it is being used by another process: 'chroma\\\
\62bff5e8-b534-41dd-8d3b-e767c1d4b598\\\\data\_level0.bin''. I tried closing the file with a method, I tried deleting th
e database everytime before running, deleting the collection, etc. but nothing seems to work. Any suggestions?
```
---

     
 
all -  [ Spring AI vs Langchain4j - which to use as of July 2024 ](https://www.reddit.com/r/java/comments/1efospd/spring_ai_vs_langchain4j_which_to_use_as_of_july/) , 2024-07-31-0909
```
Hi everyone

I'm starting a new Spring Boot project that should consume an LLM.

I was wondering if you can advise on us
ing **Spring AI vs Langchain4j**

  
I've got the impression that Spring AI is pretty new vs langchain(4j) which is like
 the industry 'standard' in a way.

  
Could you let me know what you think? What's the chance of Spring AI dying out...
 ? 

  
If it was a few years a few major releases, I would have just jumped to the Spring as it would be nicely integra
ted.

  
Much appreciated!
```
---

     
 
all -  [ Kindly review my resume. Iam a June 2024 cs grad. Iam aiming for backend dev role. These days am lea ](https://i.redd.it/82oduh1z9mfd1.png) , 2024-07-31-0909
```

```
---

     
 
all -  [ RAG over Database ](https://www.reddit.com/r/LangChain/comments/1efnx5u/rag_over_database/) , 2024-07-31-0909
```
I have been trying to build a RAG over a database that  has mulitple tables. Often times, for a user query, the data has
 to be searched by joining multiple tables. I followed this approach as mentioned in Langchain documents.

[https://pyth
on.langchain.com/v0.1/docs/use\_cases/sql/quickstart/](https://python.langchain.com/v0.1/docs/use_cases/sql/quickstart/)


  
What I am observing is that many times the query generated by LLM is not correct and the data that user wants is in
correct. We have provided almost 60 queries in Fewshot prompts example and send 3 as example that are closes semantic ma
tch. The accuracy still seems far from expected one. Are we missing something. 
```
---

     
 
all -  [ Langchain Agents or Langgraph Agents ](https://www.reddit.com/r/LangChain/comments/1efnpgv/langchain_agents_or_langgraph_agents/) , 2024-07-31-0909
```
I am working on a RAG chatbot application where we will first to have if either the given question is having enough know
ledge to be answered or we need some further information before answering. Or if a question is a general question which 
doesn't even need RAG search. For example, if a question is 'What are the main components of a car?' then we don't need 
RAG search but if a question is 'What type of suspensions do you have for a car?' then we will do RAG search.

  
Till n
ow, I created a simple ReACT agent in langchain to ask the followup questions with a tool and now I need to integrate if
 the given query is something that can be answered without any tool or not and for this, I am thinking about first havin
g an agent which qualifies the given query and if its qualified for RAG search then second agent will do either RAG sear
ch or follow-up questions.

  
In the past of couple of days, I have been exploring langgraph and I feel like simple lan
gchain is enough for my solution like a chain of agents. So please make me understand, why one should use Langgraph?
```
---

     
 
all -  [ Sharing a Code Repository on RAG ](https://www.reddit.com/r/LangChain/comments/1efnkrw/sharing_a_code_repository_on_rag/) , 2024-07-31-0909
```
I've recently created a repository for indexing, generating and evaluating RAG responses. Would love to have some feedba
ck on this. I've used LangChain and LangChain benchmarks too.

[https://github.com/abhinav-kimothi/A-Simple-Guide-to-RAG
](https://github.com/abhinav-kimothi/A-Simple-Guide-to-RAG)
```
---

     
 
all -  [ Passing an error from an ai tool to the user ](https://www.reddit.com/r/LangChain/comments/1efmpc7/passing_an_error_from_an_ai_tool_to_the_user/) , 2024-07-31-0909
```
Hello , as the title says, I have a react agent who uses some tools to find the answers to the user queries! sometimes t
he tools might find an error, for example i am raising an HTTPException if inside the tool some conditions are not corre
ct. How can i pass it to the user and inform him about the error?
```
---

     
 
all -  [ Need honest feedback on my resume, will apply mainly for ML/DS new grad 2025 roles. ](https://www.reddit.com/r/resumes/comments/1efelkj/need_honest_feedback_on_my_resume_will_apply/) , 2024-07-31-0909
```
https://preview.redd.it/e6jwjaoinjfd1.png?width=1372&format=png&auto=webp&s=97b1592056f03287c37e924010f3ddb1f23cc449




International student, applied to nearly 450 companies for ML/DS roles in the summer 2024 cycle, got 1 interview, got re
jected after the final round.

  
Need a review so that the same doesn't happen while applying for full time roles.
```
---

     
 
all -  [ Using HumanInputRun Tool with create_sql_agent in streamlit. ](https://www.reddit.com/r/LangChain/comments/1efbwpt/using_humaninputrun_tool_with_create_sql_agent_in/) , 2024-07-31-0909
```
I'm trying to get human input if the question the user asked needs clarification due to not knowing what table to use et
c. but adding is as extra_tools parameter in create_sql_agent with an input_func like the following: 


    def get_stre
amlit_input() -> str:
        '''
        Get input from a Streamlit chat input.
    
        Returns:
            str: 
The input from the user.
        '''
        try:
            prompt = st.chat_input('Insert your text. Enter 'q' to end
.', key='human_input')
        except EOFError as e:
            st.chat_message('EOFError: ' + str(e))
        return p
rompt


and agent set up as below: 

    agent_executor: Any = create_sql_agent(
        llm=llm,
        verbose=True,

        prompt=few_shot_prompt,
        agent_type='tool-calling',
        max_iterations=15,
        max_execution_time
=180,
        db=db_instance,
        extra_tools=[human_input_tool],  # Add the human input tool here
        agent_exe
cutor_kwargs={
            'return_intermediate_steps': True,
            'handle_parsing_errors': True,
            'me
mory': memory,
        },
    )



it asks the clarification question but the sql agent still continues to run. The clar
ification question shows up in intermediate steps which i can interact with but then after hitting enter on my response,
 it just shows the clarification question. and i have to then retype it again. 

Is there a better way to do this? maybe
 something like 

clarifying llm | agent_executor | output ? 

how would this work in streamlit? 

Any help is greatly a
ppreciated.
```
---

     
 
all -  [ Loading local llm with csv_agent. No open AI ](https://www.reddit.com/r/LangChain/comments/1ef841i/loading_local_llm_with_csv_agent_no_open_ai/) , 2024-07-31-0909
```
I am using llama3 for a chatbot that can answer from CSV files. I've seen implementations with OpenAI, and I want to loa
d local llama3 for the task. If you have any recommendations, please share.
```
---

     
 
all -  [ Chance me and Questions. ](https://www.reddit.com/r/UTAdmissions/comments/1ef7khm/chance_me_and_questions/) , 2024-07-31-0909
```
First, my stats:

Demographics: Asian, Male, HS class of 2025, college class of 2029.

Rank: Top 3% in my class (the ran
k for last semester is coming out in September so idk)

GPA: 4.0 UW, 107 W (1.1x multiplier for honors, 1.2x multiplier 
for APs and advanced honors)

12 APs finished by end of senior year. Planning on getting an AP Capstone Diploma.

1500 S
AT (750 M / 750 R), 35 ACT (35 Reading / 36 Math / 35 Eng / 36 Sci)

ACTIVITIES

* Eagle Scout
* CTM Intern at City of A
ustin Youth Internship Program
* Intern at Lifescale Analytics
* In the Cyber Patriots (our team made it to Platinum Div
ision in State Round) and UIL Computer Science Club since Junior year.
* In JV Robotics Club in sophomore year.
* Worked
 at Mathnasium for sophomore and half of junior year.
* Geo Bee State Qualifier in 2019 and 2020
* Congressional App Cha
llenge Applicant in 2023, made a health-related web app that calculates the risk of cardiovascular disease.
* Volunteere
d at HOTOSM since 2022.
* 100+ hours of volunteering and community service
* Shadowed for one week at a local hospital.


PROJECTS

* Created a website from scratch for my sister's dance school
* Created my own programming language using Typ
escript.
* Created an OpenAI chatbot using Langchain with data from my school notes.

Now for the question: I'm planning
 on submitting an Early Action application. I want to apply for ECE or Neuroscience, but I don't know which one to pick.
 I am knowledgeable in these two subjects and I would be happy and satisfied if I get to pursue either one of them, but,
 as you can probably tell, I like computer science a little more. However, I heard that taking ECE is hard, and looking 
back, I could've done more activities and projects. So here are my questions to y'all:

1. Without seeing my essays, wha
t are the chances that I get accepted into ECE or Neuroscience if I decide to apply for either?
2. Why should I pick one
 over the other?
3. Do I have a shot at getting into Computer Science?
```
---

     
 
all -  [ Pydantic ](https://www.reddit.com/r/LangChain/comments/1ef6qc6/pydantic/) , 2024-07-31-0909
```
Hello everyone ,
I m using pydantic in combination with LM format enforcer to output a certain format ,the thing is that
 I would like the model to be able to output possibly multiple json not just one. The task is about retrieving a variabl
e and naming it.But multiple elements can be retrieved.Is there any ways to do that?

Thanks
```
---

     
 
all -  [ I built a document parser that works without pre-training, unlike google document ai or azure docume ](https://www.reddit.com/r/LangChain/comments/1ef5f7t/i_built_a_document_parser_that_works_without/) , 2024-07-31-0909
```
Hey everyone,

I wanted to share what I built with this community to see what you guys think. I'm curious about any use 
cases you might have or just general feedback.

I created ParDocs with a simple mission: to make document extraction as 
painless as possible. I know firsthand how much time and effort can go into pre-training and labeling, and I wanted to b
uild a tool that lets you focus on what really matters -> building and coding.

With ParDocs, you can:

* Extract data f
rom any document types with minimal setup.
* Customize the JSON format you receive as a response.
* Save loads of time o
n tedious pre-training tasks.

Check out our beta here: [https://www.pardocs.com](https://www.traddocs.com/).

For those
 who prefer not to click on unknown links, here’s our YouTube demo video: https://youtu.be/LdCC0uBQ-QE.

It’s free to us
e during this beta phase. After that, I'm considering pricing it at $0.014 for the splitter and $0.075 for the extractor
. I’d love to hear your feedback on this.

Using ParDocs is very simple:

1. Specify the types of documents you'd like t
o extract.
2. Enter the desired JSON format for the response.
3. Upload your document and receive the data you need!

I’
m personally available to answer any questions or help you get started. You can DM me on Reddit or chat with me on Disco
rd: https://discord.gg/xgEXkh7Rxk. I’d love to hear what you think and how we can make ParDocs even better.

Looking for
ward to your thoughts and feedback!
```
---

     
 
all -  [ How to pass video input for evaluation? ](https://www.reddit.com/r/LangChain/comments/1ef4anh/how_to_pass_video_input_for_evaluation/) , 2024-07-31-0909
```
I am using LangSmith to evaluate my multimodal LLM runs using Gemini 1.5-Flash. My input is a question and a video file.
 I am having trouble getting the evaluator functions such as criteria to take in a custom prompt or even input video. An
y suggestions how to achieve this?
```
---

     
 
all -  [ Reasoning and Info Extraction using Function Calling ](https://www.reddit.com/r/LangChain/comments/1ef21fs/reasoning_and_info_extraction_using_function/) , 2024-07-31-0909
```
Hey everyone,  
  
I am working on an info extraction project where I am using LLM's to extract information from the doc
uments. The length of the documents that I am dealing with a rather short (3-5 pages), so I am not using RAG, but provid
ing the whole document content in-context. For the information extraction, I am using function calling/tool usage as it 
ensures a structured response all the time. And this setup used to work for most cases where the information to extract 
where directly present in the document.  
  
Now I have some scenarios where the information that needs to be extracted 
are not directly present in the document. From the content in the document, LLM have to do some reasoning to extract the
 required information. In this case, I am having some trouble in extracting information using function calling.  
  
Any
one have any experience with similar problems? Any suggestion are highly appreciated.  
```
---

     
 
all -  [ Problems using FastAPI and langchain_google_cloud_sql_pg on Cloud Run (GCP) ](https://www.reddit.com/r/googlecloud/comments/1ef18io/problems_using_fastapi_and_langchain_google_cloud/) , 2024-07-31-0909
```
Hi, I wanted to ask if anyone has experienced this issue because between Google, myself, and GPT, we can't find a soluti
on.

I have an endpoint created in FastAPI to which I pass a hash, a username, and a question. It uses a langgraph graph
, queries, embeddings, and more, and through OpenAI using a model, it returns a response. Basically, it's a bot, but spe
cialized since it doesn't respond in general; it responds based on information I have stored in a vector database. So, y
ou ask the question, it transforms it into a vector, searches for the nearest vectors, and returns that as text.

Now, t
he problem:

When the endpoint is called, this process is executed. Essentially, it creates a synchronization with the P
ostgreSQL table of chat history.

This code is in the endpoint. The structure of the API uses routes, so there is a main
 file that imports this endpoint.

    engine_cx_bot = create_engine()
    
    from langchain_google_cloud_sql_pg impor
t PostgresChatMessageHistory
    
    history = PostgresChatMessageHistory.create_sync(
        engine_cx_bot, session_i
d=session_id, table_name=settings.table_cx_history
    )

This allows me to do two things:

1. Insert the new interactio
ns between the human who asks and the bot that responds:



    history.add_message(HumanMessage(content=inputs['questio
n']))
    history.add_message(AIMessage(content=''.join(output['generate_answer']['messages'])))

1. Retrieve the histor
y of all messages so that with each new question from the user, the bot has the context of the conversation. If I ask a 
few questions today and come back tomorrow, when I ask again, since it has all the historical messages, it can continue 
the conversation.

The problem:

I deployed this on Cloud Run, the endpoint works fine, I can hit it from a frontend and
 have a chat with the bot, but after an hour or two, I can no longer hit it due to a 500 status. It seems like the conne
ction between Cloud Run and Cloud SQL, where the data is stored, gets cut off. Looking at the logs, I only see this. I'v
e done approximately 50 deployments trying to test it, and I can't get past this error which is random—sometimes after 1
 hour, sometimes after 2. The longest it took before it failed was 6 hours.

File '/app/venv/lib/python3.9/site-packages
/langchain\_google\_cloud\_sql\_pg/engine.py', line 245, in getconn  
conn = await cls.\_connector.connect\_async( # typ
e: ignore  
File '/app/venv/lib/python3.9/site-packages/google/cloud/sql/connector/connector.py', line 341, in connect\_
async  
conn\_info = await cache.connect\_info()  
File '/app/venv/lib/python3.9/site-packages/google/cloud/sql/connecto
r/lazy.py', line 103, in connect\_info  
conn\_info = await self.\_client.get\_connection\_info(  
File '/app/venv/lib/p
ython3.9/site-packages/google/cloud/sql/connector/client.py', line 271, in get\_connection\_info  
metadata = await meta
data\_task  
File '/app/venv/lib/python3.9/site-packages/google/cloud/sql/connector/client.py', line 128, in \_get\_meta
data  
resp = await self.\_client.get(url, headers=headers)  
File '/app/venv/lib/python3.9/site-packages/aiohttp/client
.py', line 507, in \_request  
with timer:  
File '/app/venv/lib/python3.9/site-packages/aiohttp/helpers.py', line 715, 
in \_\_enter\_\_  
raise RuntimeError(  
RuntimeError: Timeout context manager should be used inside a task'

Has anyone
 experienced this? If I go to Cloud Run and redeploy the same revision, it starts working again, but the same thing happ
ens—a few hours later, it fails.

STATUS UPDATE:

I found this on StackOverflow [https://stackoverflow.com/questions/783
07398/long-lived-cloud-sql-python-connector-with-iam-authentication-gives-intermittent](https://stackoverflow.com/questi
ons/78307398/long-lived-cloud-sql-python-connector-with-iam-authentication-gives-intermittent) and it seems to be a prob
lem between the library and how Cloud Run assigns CPU. I'm following the recommended steps and still facing the same iss
ues.

At this very moment, I'm migrating the entire backend to Alloy since I read that in their library version, they su
pposedly fixed the problem by adding lazy loading.

If anyone has gone through this and solved it, I would appreciate so
me guidance.
```
---

     
 
all -  [ The RAG Engineer's Guide to Document Parsing ](https://www.reddit.com/r/LangChain/comments/1ef12q6/the_rag_engineers_guide_to_document_parsing/) , 2024-07-31-0909
```
Hi Group,

I made a post with my buddy Daniel Warfield breaking down why parsing matters so much for RAG and comparing s
ome of the different approaches based on our experience working with Air France, Dartmouth a big online publisher and do
zens of other projects with real data

For full transparency, one of the products discussed comes from my firm [EyeLevel
.ai](http://EyeLevel.ai), but that's not the focus. It's a discussion of how we can all build better RAG on the kind of 
complex docs we see in the real world.

You can watch it on YT if you prefer... [https://www.youtube.com/watch?v=7Vv64f1
yI0I](https://www.youtube.com/watch?v=7Vv64f1yI0I)

# The Foundation of RAG: Document Parsing

Let's start with a fundam
ental truth: parsing is the bedrock of any RAG application. 

'The first step in any RAG application is parsing your doc
ument and extracting the information from it,' says EyeLevel cofounder Neil Katz. 'You’re trying to turn it into somethi
ng that language models will eventually understand and do something smart with.'

This isn't just about extracting text.
 It's about preserving structure, context, and relationships within the data. Get this wrong, and your entire RAG pipeli
ne suffers. If you don't get the information out of your giant set of documents in the first place, which is often where
 RAG starts, it's “garbage in and garbage out” and nothing else will work properly.

# The Heart of the Problem

The bas
ic problem to solve is that language models, at least for now, don't understand complex visual documents. Anything with 
tables, forms, graphics, charts, figures and complex formatting will cause downstream hallucinations in a RAG applicatio
n. Yes you can take a page from a PDF and feed it into ChatGPT and it will understand some of it, sometimes most of it. 
But try doing this at scale with thousands or millions of pages and you've got a mess and eventually downstream hallucin
ations for your RAG.

So devs need some way of breaking complex documents apart, identifying the text blocks, the tables
, the charts and so on, then extracting the information from those positions and converting it into something language m
odels will understand and that you can store in your RAG database. This final output is usually simple text or JSON.

Th
is problem isn't new btw. There are entire industries devoted to ingesting medical bills, restaurant receipts and so on.
 That's typically done with a vision model fine tuned to a very specific set of documents. The model for receipts isn't 
good at medical bills. And vice versa.

The new twist is RAG often deals with a highly varied set of content. A legal RA
G, for example, might need to understand police reports, medical bills and insurance claims.  The second twist is the in
formation needs to be converted into LLM ready data.

So let's talk about what's out there.

# Parsing Strategies: Break
down of Approaches

Let's examine some common parsing strategies, their strengths, and their limitations using an exampl
e of a medical document showcasing exam dates and fees in a table:

# 1. PyPDF

[Image: PyPDF results showing minimal in
formation extracted from the table in the medical document.](https://preview.redd.it/lizhsf8twgfd1.png?width=960&format=
png&auto=webp&s=f8a3fe90f3725c9751fd370dc885fa7d4a4f147b)

[PyPDF](https://pypdf.readthedocs.io/en/stable/index.html) is
 a longstanding Python library designed for reading and manipulating PDF files. It can be effective for basic text extra
ction from simple PDFs, but often struggles with complex layouts, tables, and formatted text. 

PyPDF is best suited for
 straightforward, text-heavy documents but may lose critical structural information in more intricate PDFs. It doesn't p
rocess visual objects like images, charts, graphs and figures.

# 2. Tesseract (OCR)

[Image: Tesseract results showing 
information extracted from the table in the medical document.](https://preview.redd.it/ofa0pkawwgfd1.png?width=960&forma
t=png&auto=webp&s=a9a47fa3defa74939b453236fec4aee0de6dfea4)

[Tesseract](https://github.com/tesseract-ocr/tesseract) is 
an open-source optical character recognition (OCR) engine that can extract text from images and scanned documents. Best 
known for converting image-based text to machine-readable format, Tesseract can struggle with maintaining document struc
ture, especially in complex layouts or tables. 

It's particularly useful for scanned documents but may require addition
al post-processing to preserve formatting and structure. Tesseract also doesn't process visual objects like images, char
ts, graphs and figures.

# 3. Unstructured

[Image: Unstructured results showing rich information extracted from the tab
le in the medical document.](https://preview.redd.it/yz8gnwvzwgfd1.png?width=960&format=png&auto=webp&s=a39380072b5beb48
547179c463489bd5353ca14d)

[Unstructured](https://unstructured.io/) is a modern document parsing library that aims to ha
ndle a wide variety of document types and formats. It employs a combination of techniques to extract and structure infor
mation from documents, including text extraction, table detection, and layout analysis. 

While more robust than traditi
onal parsing tools, Unstructured can still face challenges with highly complex or non-standard document formats. Like th
e others, it doesn't process visual objects like images, charts, graphs and figures.

# 4. LlamaParse

[Image: LlamaPars
e results showing a markdown table of information extracted from the table in the medical document.](https://preview.red
d.it/8ev781z1xgfd1.png?width=960&format=png&auto=webp&s=2db69039e0567ebe6efb69be07aff2ffec71437e)

[LlamaParse](https://
docs.llamaindex.ai/en/stable/llama_cloud/llama_parse/) is a newer parsing solution developed by the team behind [LlamaIn
dex](https://www.llamaindex.ai/). It's designed to handle complex document structures, including tables and formatted te
xt, and outputs results in a markdown format that's easily interpretable by language models. 

It has been seen to prese
rve document structure and handle tables, though it's a relatively new tool and its full capabilities and limitations ar
e still being explored in real-world applications.

# 5. X-Ray by [**EyeLevel.ai**](http://EyeLevel.ai)

[Image: X-Ray b
y EyeLevel.ai converts a complex medical bill into clean JSON chunks with both narrative description and data that LLMs 
prefer](https://preview.redd.it/a14hfii3xgfd1.png?width=1942&format=png&auto=webp&s=37c7ae239e136201836e3fb44ec33331cf7a
92d7)

[X-Ray](https://www.eyelevel.ai/xray), powered by EyeLevel’s [GroundX APIs](https://www.eyelevel.ai/product/apis)
, takes a multimodal approach to parsing with industry leading results, especially when parsing complex visuals includin
g charts, graphics and figures. X-Ray is far more than just a table parser.

The X-Ray technology starts with a fine-tun
ed vision model trained on a million pages of enterprise documents from a wide cross section of industries including hea
lth, financial, insurance, legal and government. The system uses the vision model to identify various objects on the pag
e: text blocks, tables, charts and so on. Once the coordinates are known, it extracts the information, chunks it and sen
ds it to different pipelines to be turned into LLM ready data.

The result is a JSON-like output that includes the core 
data, chunk summary, doc summary, keywords and other metadata, providing richer context for language models. X-Ray is av
ailable in a demo format for developers to try for themselves, where they can upload a document to the system and see th
e semantic objects that are created to translate complex visuals to the LLM. [**You can try X-Ray here**](https://www.ey
elevel.ai/xray).

# Performance Impact: The Parsing Difference

Our tests, along with academic research, show that parsi
ng strategy can significantly impact RAG performance. 

We're talking about substantial gains, as Daniel Warfield, co-ho
st of RAG Masters points out:

>'For some examples, there's a 10%, even a 20% difference in performance.'

This is cruci
al when you consider the effort that goes into other optimization strategies:

>'People are doing crazy advanced strateg
ies for the difference in 5, 6, 7, even 10 percent performance. And then maybe just completely switching the parser migh
t get you a massive performance increase.'

# Error Analysis: Common Parsing Pitfalls

Let's examine some common parsing
 errors and their downstream effects:

1. **Table Misinterpretation:** When parsers fail to correctly identify table str
uctures, it can lead to data being treated as unstructured text. This can result in incorrect answers in question-answer
ing tasks, especially for queries about tabular data.
2. **Loss of Formatting:** If a document structure isn't well unde
rstood, a text scrape could scramble the pieces up. A header could wind up in body copy. A column label could wind up in
 the rows of data. You get the parsing equivalent of scrambled eggs.
3. **Image Handling:** Most parsers struggle with e
mbedded images or diagrams, either ignoring them completely or misinterpreting them as text through OCR.
4. **Header/Foo
ter Confusion:** Parsers might incorrectly include headers and footers as part of the main content, potentially skewing 
the context of the extracted information.

# Developing Custom Parsing Strategies

For developers dealing with specific 
document types or domains, developing custom parsing strategies can be beneficial. Here are some approaches:

1. **Combi
ning Existing Tools:** Use multiple parsing tools in tandem, leveraging the strengths of each for different parts of you
r documents.
2. **Regular Expressions:** Implement custom regex patterns to extract specific types of information consis
tently found in your documents.
3. **Domain-Specific Rules:** Incorporate rules based on domain knowledge to improve par
sing accuracy for specialized documents.
4. **Machine Learning Augmentation:** Train models to recognize and extract spe
cific patterns or structures in your documents.

# Integration Challenges

When integrating parsing strategies into exis
ting RAG pipelines, developers often face several challenges:

1. **API Compatibility:** Ensure that the chosen parsing 
strategy can be easily integrated with your existing codebase and infrastructure.
2. **Data Format Consistency:** The ou
tput of your parser should be in a format that's compatible with the rest of your RAG pipeline, often requiring addition
al preprocessing steps.
3. **Scalability:** Consider the computational resources required by different parsing strategie
s, especially when dealing with large document sets.
4. **Error Handling:** Implement robust error handling to deal with
 parsing failures or unexpected document formats.

# Best Practices for Selecting a Parsing Strategy

It’s recommend to 
take a two-pronged approach to selecting the right parsing strategy:

**1. Visual Inspection:** Start by running your do
cuments through different parsers and examining the output. As Warfield advises:

>'Pass your data through a bunch of pa
rsers and look at them. Your brain is still the most powerful model that exists.'

**2. End-to-End Testing:** Once you'v
e narrowed down your options, conduct thorough end-to-end testing. This means running your entire RAG pipeline with diff
erent parsing strategies and evaluating the final output.

To quantitatively compare parsing strategies, consider the fo
llowing metrics:

* Accuracy in table and graphical extraction
* Preservation of document structure
* Abiliity to turn e
xtractions into LLM friendly data
* Speed of parsing
* Consistency across different document types
* Ability to handle c
omplex formatting

# The Challenge of Evaluation

Here's the rub: evaluating parsing quality is still a largely manual p
rocess. Creating question-answer pairs for evaluation is labor-intensive but crucial for building automated tooling. The
 need for human evaluation in parsing cannot be completely eliminated, at least not yet.

This presents a significant op
portunity in the field, and this post will be updated in the future when a sufficiently advanced solution for automated 
parsing is discovered.

# Conclusion

As we continue to push the boundaries of what's possible with RAG applications, it
's clear that document parsing will remain a critical component. The field is ripe for innovation, particularly in parsi
ng technology and evaluation methods.

For developers building RAG applications, it’s critical not to overlook the impor
tance of parsing. Take the time to evaluate different parsing strategies and their impact on your specific use case. It 
could be the difference between a RAG system that merely functions and one that excels.

Remember, in the world of RAG, 
your system is only as good as the data you feed it. And that all starts with parsing.

[You can watch the full episode 
of RAG Masters here.](https://www.youtube.com/watch?v=7Vv64f1yI0I)
```
---

     
 
all -  [ Langchain in python or javascript ](https://www.reddit.com/r/LangChain/comments/1eezbcn/langchain_in_python_or_javascript/) , 2024-07-31-0909
```
Should I use Langchain with JavaScript or Python for my project? Which one would look better on my resume? Do you have a
ny advice?
```
---

     
 
all -  [ AI Agent for Personalized Learning ](https://www.reddit.com/r/LangChain/comments/1eewm4s/ai_agent_for_personalized_learning/) , 2024-07-31-0909
```
Hey everyone,

I just released my open-source project. I'd be grateful if you could take a look and give me some feedbac
k.

Here's the link: [https://github.com/LERM0/LermoAI](https://github.com/LERM0/LermoAI)

Thanks!
```
---

     
 
all -  [ RAG open-ended question  ](https://www.reddit.com/r/LangChain/comments/1eeugjo/rag_openended_question/) , 2024-07-31-0909
```
Hi everyone! I'm currently experimenting with RAG. I was very successful implementing a simple prototype and now I'm loo
king to improve and productionise this. It's based on allow general questions on news articles from several sources. My 
challenge is how to handle general questions like 'show me all topics' or 'what is the sentiment towards X'. In order to
 do this, I assume the model should be aware of full context, which is not viable as the dataset has millions of article
s from several years. Any advice where to start tackling this ? Tried to find some resources, but I couldn't, probably d
ue to lack of understanding how to 'name' this problem 
```
---

     
 
all -  [ KeyError: 'context'. Trying to add memory. ](https://www.reddit.com/r/LangChain/comments/1eetmjm/keyerror_context_trying_to_add_memory/) , 2024-07-31-0909
```
I am trying to add memory to my script but I have litreally tried for 3 days but couldnt solve this error. My. hopes are
 going downstream

    # Create retriever
    retriever 
    =
     vectorstore.as_retriever(
        search_type
    =

    'mmr',
        search_kwargs
    =
    {'k': 3, 'fetch_k': 15, 'lambda_mult': 0.3}
    )
    
    # Initialize ChatT
ogether model
    chat 
    =
     ChatTogether(
        model
    =
    'meta-llama/Llama-3-8b-chat-hf',
        temper
ature
    =
    0.5,
        max_tokens
    =
    200,
        api_key
    =
    api_key_together
    )
    
    store 

    =
     {}  
    # memory is maintained outside the chain
    
    def
     
    get_session_history
    (session_id:
 str) -> BaseChatMessageHistory:
        
    if
     session_id 
    not
     
    in
     store:
            store[ses
sion_id] 
    =
     ChatMessageHistory()
        memory 
    =
     ConversationSummaryMemory(
            chat_memory

    =
    store[session_id],
            k
    =
    3,
            return_messages
    =
    True,
            llm 
   
 =
     chat
        )
        
    assert
     len(memory.memory_variables) 
    ==
     1
        key 
    =
     memo
ry.memory_variables[0]
        messages 
    =
     memory.load_memory_variables({})[key]
        store[session_id] 
   
 =
     ChatMessageHistory(messages
    =
    messages)
        
    return
     store[session_id]
    
    contextualiz
e_q_system_prompt 
    =
     (
        'Given a chat history and the latest user question '
        'which might refere
nce context in the chat history, '
        'formulate a standalone question which can be understood '
        'without t
he chat history. Do NOT answer the question, '
        'just reformulate it if needed and otherwise return it as is.'
  
      '{context}'
    )
    
    contextualize_q_prompt 
    =
     ChatPromptTemplate.from_messages(
        [
        
    ('system', contextualize_q_system_prompt),
            MessagesPlaceholder('chat_history'),
            ('human', '{
input}'),
        ]
    )
    
    history_aware_retriever 
    =
     create_history_aware_retriever(
        chat, ret
riever, contextualize_q_prompt
    )
    
    def
     
    strain_query
    (query, session_id):
        template 
    
=
     '''
            You are an expert AI budtender with comprehensive knowledge of cannabis strains, their effects, m
edical applications, and industry trends. 
            Your task is to provide accurate, helpful, and concise informatio
n in response to user queries about cannabis. 
            Use the following context to answer the question:
           
 
            Context: {context}
            {history}
            Human: {query}
            chatbot:
            
    
        Instructions:
            1. Analyze the question carefully to understand the user's intent.
            2. Prov
ide a clear, concise, and informative answer based on the given context and your expertise.
            3. If the questi
on is about a specific strain, include key information such as dominant effects, medical benefits, flavor profile, and a
ny unique characteristics.
            4. For general cannabis questions, offer balanced and factual information, citing
 scientific research when relevant.
            5. If the context doesn't fully address the question, state this and pro
vide the best available information, suggesting where the user might find more details.
            6. Keep your respons
e concise, aiming for 3-5 sentences unless more detail is absolutely necessary.
            7. If appropriate, suggest r
elated topics or strains the user might be interested in exploring.
            
            Provide your expert respons
e:
            Give answer in markdown format
        '''
        
        prompt 
    =
     PromptTemplate(template
  
  =
    template, input_variables
    =
    ['context', 'question', MessagesPlaceholder('history')])
        
        qu
estion_answer_chain 
    =
     create_stuff_documents_chain(
            llm
    =
    chat,
            prompt
    =
 
    prompt,
            document_variable_name
    =
    'context'  
    # Ensure this matches the placeholder in the te
mplate
        )
        
        rag_chain 
    =
     create_retrieval_chain(
            question_answer_chain,
     
       history_aware_retriever
        )
        
        chain_with_history 
    =
     RunnableWithMessageHistory(
   
         rag_chain,
            get_session_history
    =
    get_session_history,
            input_messages_key
    =

    'query',
            history_messages_key
    =
    'history',
            output_messages_key
    =
    'answer'
  
      )
        
        
    # Add debugging print statements
        print(
    f
    'Input query: {query}')
        
print(
    f
    'Session ID: {session_id}')
        
        response 
    =
     chain_with_history.invoke(
          
  {'query': query},
            config
    =
    {
                'configurable': {'session_id': session_id}
          
  }
        )
        
        
    # Debug the response
        print('Response received from the chain:')
        prin
t(response)
        
        
    return
     response['answer']
    
    # Example usage
    session_id 
    =
     'us
er_123'  
    # This should be unique for each user session
    query 
    =
     'Tell me about the effects of Blue Dre
am strain'
    response 
    =
     strain_query(query, session_id)
    print(response)
    
    query 
    =
     'What
 are its medical benefits?'
    response 
    =
     strain_query(query, session_id)
    print(response)

This is my cod
e:

  
and everytime the error is same:  
  File '/opt/anaconda3/lib/python3.11/site-packages/langchain\_core/runnables/
config.py', line 404, in call\_func\_with\_variable\_args

return func(input, \*\*kwargs)  # type: ignore\[call-arg\]

\
^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^

  File '/opt/anaconda3/lib/python3.11/site-packages/langchain/chains/combine\
_documents/stuff.py', line 85, in format\_docs

for doc in inputs\[document\_variable\_name\]

\~\~\~\~\~\~\^\^\^\^\^\^\
^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^

KeyError: 'context'

  
Please HELPPPPPP!!!!   
I dont understand what I am doing w
rong. I even attempt to use Promot template and take context as input variables but it didnt work out as well.


```
---

     
 
all -  [ is client facing text to sql lost cause for now? ](https://www.reddit.com/r/LangChain/comments/1eetb9g/is_client_facing_text_to_sql_lost_cause_for_now/) , 2024-07-31-0909
```
I was hoping to build a a bot which will take question from client and get response back. The thing is that, client can 
ask anything. And the consistency and stability an enterprise grade application should have is not there no matter what.
 I have put so much effort and its still not as expected. Have any one of you figured it out? 
```
---

     
 
all -  [ PigPig: The LLM Discord Bot (Can this be achieved using langchain?) ](https://www.reddit.com/r/Discord_Bots/comments/1eesys8/pigpig_the_llm_discord_bot_can_this_be_achieved/) , 2024-07-31-0909
```
# Seeking advice on developing a Discord bot with LangChain

Hello Discord bot developers! I'm working on a Discord bot 
project using LangChain and would love to get some advice and insights.

My project aims to integrate the following feat
ures:

* AI-powered conversations (using LLMs and LangChain)
* Music playback
* Multi-modal capabilities (visual Q&A and
 image generation)
* Utility tools (reminders, recommendations, calculations, etc.)
* User data management
* Context-awa
re responses based on channel history (RAG)

The tech stack includes:
Python 3.10+, Discord.py, MongoDB, Lavalink, LangC
hain

I'm particularly interested in hearing from the community on these questions:

1. Has anyone fully implemented a D
iscord bot using LangChain? What was your experience like?
2. How have you optimized RAG (Retrieval-Augmented Generation
) in your Discord bots?
3. What LangChain-specific features would you like to see in a Discord bot?

I've started an ope
n-source project to explore these ideas. If you're interested in viewing the code or contributing, let me know, and I ca
n provide the GitHub link in the comments.

Let's discuss these topics! Your insights could help shape the future of thi
s project.
```
---

     
 
all -  [ Learning LangGraph/LangChain JS... why does it seem like there's 5 different ways to do anything in  ](https://www.reddit.com/r/LangChain/comments/1eerg3b/learning_langgraphlangchain_js_why_does_it_seem/) , 2024-07-31-0909
```
Ok am I crazy or do the docs and examples show multiple ways of doing the same thing. As a noobie it's confusing as hell
 and slowly me down. Yeah skill issue, i'm just a web dev hobbyist venturing into the world of agentic flows. 

Let's ta
ke creating a tool.

* You can use the \`tool\` method
* You can use \`new DynamicStructuredTool \`
* You can use \`new 
DynamicTool\`

I get that there's nuances between when to use which, but the docs and examples end up using different im
plementations through the docs which is super confusing. And bouncing between examples I feel like I have to pay attenti
on more carefully for these different implementations to make sure they don't throw me off back to looking at the docs (
which are not easy to navigate). 

  
If you're going to switch something on the user mid way through an example, please
 show a comment what the alternative way is and stick the the original way you started with.

I feel like this happens a
ll over the place. A simple example is the use of \`new HumanMessage\` and just using \`\[user, query\]\`. 

These examp
le end up importing way too much stuff that's not necessary. What's the point of the Message helpers anyways? Are we exp
ecting the convention to change of working with system, assistant, and user messages? The whole point of typescript is t
hat we would get type safety for these values. Anyways I'll end my slight rant here

  
People online complain about LC.
 I see its value, but it feels like trying to drive a stick shift car, except you have two stick shifts to use but you'r
e wondering why there are two of them and not one...


```
---

     
 
all -  [ PigPig-discord-LLM-bot (Can this be achieved using langchain?) ](https://www.reddit.com/r/LangChain/comments/1eemonr/pigpigdiscordllmbot_can_this_be_achieved_using/) , 2024-07-31-0909
```
# 🧠 Powered by Large Language Model (LLM) and LangChain PigPig uses cutting-edge AI to understand and respond to your me
ssages naturally. We've integrated LangChain for some features, enhancing our bot's capabilities.

# 🎵 Advanced Music Pl
ayer

* Stream high-quality music from YouTube, Spotify, SoundCloud, and more
* Interactive music controller for easy pl
aylist management
* Lyrics search function to sing along with your favorite tunes

# 🖼️ Multi-modal Capabilities

* Visu
al Question Answering: Ask questions about images
* Image Generation: Create custom images from text descriptions

# 🍽️ 
Practical Features

* Set reminders for important events
* Get restaurant recommendations
* Perform mathematical calcula
tions

# 👤 User Information Management 

* Create and maintain user profiles 
* Track user interactions and preferences 


# 📊 Channel Data RAG (Retrieval-Augmented Generation) 

* Utilize channel history for context-aware responses 
* Impro
ve bot's understanding of ongoing discussions

# 🔧 Easy to Set Up and Customize

* Flexible configuration through simple
 files
* Auto-update system to keep your bot current

# 💻 Tech Stack

* Python 3.10+
* [Discord.py](http://Discord.py)
*
 MongoDB
* Lavalink server (4.0.0+)

-LangChain

-Llama3.1

...

Whether you're looking to enhance your gaming sessions,
 manage a community, or just have fun with friends, PigPig has got you covered. It's like having a Swiss Army knife of D
iscord bots!

Check out our GitHub repo for more details and installation instructions: [PigPig-discord-LLM-bot](https:/
/github.com/starpig1129/PigPig-discord-LLM-bot)

# 🤔 Questions for the Community

1. We're currently using LangChain for
 some of our bot's functionalities. Has anyone successfully implemented a Discord bot entirely with LangChain? We'd love
 to hear about your experiences and challenges.
2. For those familiar with LangChain, do you think it's feasible to use 
it for all of PigPig's features? We're particularly interested in how it might handle music playback and image processin
g.
3. What other LangChain-specific features would you like to see in a Discord bot? Let's discuss in the comments! Your
 insights could help shape the future of PigPig.
```
---

     
 
all -  [ I'm building a community led tool marketplace for AI agents, what tools do you want to see there? (P ](https://www.reddit.com/r/AI_Agents/comments/1eektr6/im_building_a_community_led_tool_marketplace_for/) , 2024-07-31-0909
```
What model would you prefer, pure usage based or subscription with x amount of credits to use?

We will open up for comm
unity submissions with a revenue split.
```
---

     
 
all -  [ [3 YoE] AI Engineer / Data Scientist | Looking for ML/AI/LLM/Data Science related Jobs (open for IL  ](https://www.reddit.com/r/resumes/comments/1eej14g/3_yoe_ai_engineer_data_scientist_looking_for/) , 2024-07-31-0909
```
https://preview.redd.it/3nhuxw271cfd1.png?width=5100&format=png&auto=webp&s=2c325939cbc3a7023b4e6201e09ad5d7792be7c6

**
Background:**

I'm applying to AI Engineer and Data Scientist jobs, I want to work with LLMs and cutting-edge AI.

I did
 had interviews (using my old CV), but I think he reflected ML more then LLMs which is my real speciallity. So I got man
y denials from relevant jobs and decided to edit it. (It made by resume writer who did terrible job IMO)

I created new 
CV yesterday and decided to post it in reddit (not in this 'r/') ppl said it have too much information and refered me he
re where I found the wiki and more useful material.

Just done making my new CV.

**About skill section:**

* Programmin
g Languages:
   * I'm familiar but no work exp with Java and JavaScript (and I see it in many jobs) should it get in the
re?
* Deep learning:
   * Should I say Parameter-Efficient Fine-Tuning or PEFT, or Low-Rank Adaptation or LoRA most Job 
descriptions request PEFT or LoRA?
   * should I include supervised fine-tuning?
   * Should I include Hugging face? (Tr
anspormers library) same with openai vs OpenAI API
* Machine learning:
   * should I include OpenCV? (lower efficiency b
ut familiar with)
   * Also XGBoost, familiar with it but see it in a lot of jobs
* Artificial intellegence:
   * should
 I include key NLP libraries like spaCy, NLTK, and Stanza (or StanfordNLP)?
   * I did Include prompt Engineering, LangC
hain but should I also Include LangSmith? (high demmand, maybe even CoT?)
   * Also removed some important key concepts 
like Word Embeddings ,Text Embeddings, Text Cleaning, Tokenizers, Text Similarity, Text Generation, Text Classification,
 etc.

**About Experiance:**

* AI Engineer:
   * I feel like it still might be too long sentences, should I break somet
hing into 2 sentences?
* The Other 2 Jobs:
   * TBH I didnt really knew what to type in result since I left the research
 when I found a job.

**About Projects:**

* Its actually projects that I've done in my last year in the degree but some
 hiring managers, especially from Cyber security was interested in my Ransomware.

**About Education:**

* The way I wro
te my GPA is ok? (I will change to 3.8 if I apply US)

**References to past resumes and desired Jobs:**

* My old CV whi
ch got me some interviews:
* [https://imgur.com/gWKHsxm](https://imgur.com/gWKHsxm)
* The Overloaded CV I created yester
day:
* [https://imgur.com/sBDSLaB](https://imgur.com/sBDSLaB)
* [https://imgur.com/9GvVsXi](https://imgur.com/9GvVsXi)
*
 Some Job descriptions I found interesting:
* [https://imgur.com/y2P04yI](https://imgur.com/y2P04yI)
* [https://imgur.co
m/G2Ixyjt](https://imgur.com/G2Ixyjt)
* [https://imgur.com/KsLCBIy](https://imgur.com/KsLCBIy)
* [https://imgur.com/AqK3
SpR](https://imgur.com/AqK3SpR)
* [https://imgur.com/Bk3KbY7](https://imgur.com/Bk3KbY7)
* [https://imgur.com/asKlBZg](h
ttps://imgur.com/asKlBZg)

Hope I wasnt speaking too much,

I thank everyone so much for the help, time and effort.
```
---

     
 
all -  [ [Wanted] Async multi-agent framework ](https://www.reddit.com/r/LLMDevs/comments/1eej0to/wanted_async_multiagent_framework/) , 2024-07-31-0909
```
What would be your choice of multi agent orchestration framework? Some reqs: 
- LLM agnostic 
- Agent to agent communica
tion 
- It should be able to store its state in database 
- Asynchronous and distributed 
- Code separation 
- Lightweig
ht and no langchain please 
```
---

     
 
all -  [ [3 YoE] AI Engineer / Data Scientist | Looking for ML/AI/LLM/Data Science related Jobs (open for IL  ](https://www.reddit.com/r/ResumeExperts/comments/1eeizy2/3_yoe_ai_engineer_data_scientist_looking_for/) , 2024-07-31-0909
```
https://preview.redd.it/a19y97ah0cfd1.png?width=5100&format=png&auto=webp&s=c075164e867621e06f17b5f3a638568f2a6a6b14

**
Background:**

* I'm applying to AI Engineer and Data Scientist jobs, I want to work with LLMs and cutting-edge AI.
* I 
did had interviews (using my old CV), but I think he reflected ML more then LLMs which is my real speciallity. So I got 
many denials from relevant jobs and decided to edit it. (It made by resume writer who did terrible job IMO)
* I created 
new CV yesterday and decided to post it in reddit (not in this 'r/') ppl said it have too much information and refered m
e here where I found the wiki and more useful material.
* Just done making my new CV.

**About skill section:**

* Progr
amming Languages:
   * I'm familiar but no work exp with Java and JavaScript (and I see it in many jobs) should it get i
n there?
* Deep learning:
   * Should I say Parameter-Efficient Fine-Tuning or PEFT, or Low-Rank Adaptation or LoRA most
 Job descriptions request PEFT or LoRA?
   * should I include supervised fine-tuning?
   * Should I include Hugging face
? (Transpormers library) same with openai vs OpenAI API
* Machine learning:
   * should I include OpenCV? (lower efficie
ncy but familiar with)
   * Also XGBoost, familiar with it but see it in a lot of jobs
* Artificial intellegence:
   * s
hould I include key NLP libraries like spaCy, NLTK, and Stanza (or StanfordNLP)?
   * I did Include prompt Engineering, 
LangChain but should I also Include LangSmith? (high demmand, maybe even CoT?)
   * Also removed some important key conc
epts like Word Embeddings ,Text Embeddings, Text Cleaning, Tokenizers, Text Similarity, Text Generation, Text Classifica
tion, etc.

**About Experiance:**

* AI Engineer:
   * I feel like it still might be too long sentences, should I break 
something into 2 sentences?
* The Other 2 Jobs:
   * TBH I didnt really knew what to type in result since I left the res
earch when I found a job.

**About Projects:**

* Its actually projects that I've done in my last year in the degree but
 some hiring managers, especially from Cyber security was interested in my Ransomware.

**About Education:**

* The way 
I wrote my GPA is ok? (I will change to 3.8 if I apply US)

**References to past resumes and desired Jobs:**

* My old C
V which got me some interviews:
* [https://imgur.com/gWKHsxm](https://imgur.com/gWKHsxm)
* The Overloaded CV I created y
esterday:
* [https://imgur.com/sBDSLaB](https://imgur.com/sBDSLaB)
* [https://imgur.com/9GvVsXi](https://imgur.com/9GvVs
Xi)
* Some Job descriptions I found interesting:
* [https://imgur.com/y2P04yI](https://imgur.com/y2P04yI)
* [https://img
ur.com/G2Ixyjt](https://imgur.com/G2Ixyjt)
* [https://imgur.com/KsLCBIy](https://imgur.com/KsLCBIy)
* [https://imgur.com
/AqK3SpR](https://imgur.com/AqK3SpR)
* [https://imgur.com/Bk3KbY7](https://imgur.com/Bk3KbY7)
* [https://imgur.com/asKlB
Zg](https://imgur.com/asKlBZg)

Hope I wasnt speaking too much,

I thank everyone so much for the help, time and effort.

```
---

     
 
all -  [ GenAi Analytics Agent ](https://www.reddit.com/r/dataengineering/comments/1eeifu5/genai_analytics_agent/) , 2024-07-31-0909
```
I'm in the process of building an Ai Analytics agent using OpenAI, Langchain and Streamlit. I could use some feedback on
 my current set up and was hoping some of you might be able to give me some tips.

The Goal:
So the goal is to provide t
he use with charts and graphs of data that is stored in our semantic layer on Snowflake. 

The Data:
We are fortunate en
ough to have descriptions for every column and naming conventions for columns used in joins. I have created embeddings f
or all the table names and column descriptions and have put these behind an API that can use a semantic similarity searc
h.

The Agent:
I built some functions that can call the API endpoints to get either relevant table names or column names
. I then added a function that can fetch a table schema, one that can fetch the data from specified columns from snowfla
ke and one more that can filter the data using pandas. I have provided all these functions as tools to a Langchain agent
 with a manually written prompt with some guidelines on how to use the tools.

This set up has given mixed results. When
 it gets the right table name it can work like a charm, but it still struggles sometimes. For instance when a user is lo
oking for revenue per week it puts daily sales into the search query, or it searches on the article level instead of per
 store. Sometimes it also looks up the schema of every table to find the right one, using up a lot of tokens.

I feel li
ke I'm moving in the right direction, but I wonder if there are maybe best practices I'm missing, causing me to use to m
any tokens. Furthermore I hear a lot about people using techniques like DSPy, Knowledge Graph and fine tuning, but I'm n
ot sure whether these would offer (significant) benefits in my case.

Any help/feedback on my approach would be much app
reciated!

```
---

     
 
all -  [ RAG for Code Generation ](https://www.reddit.com/r/LangChain/comments/1eefr4x/rag_for_code_generation/) , 2024-07-31-0909
```
I want to create a RAG for the code generation task. the knowledge base will be a library and starting from that library
 my RAG must be able to generate code based on the library. Do you have any advice on the type of approach, vector store
 or knowledge graph database, models and more?
```
---

     
 
all -  [ How does my resume stack up for Quant / Quant SWE Roles? ](https://www.reddit.com/r/resumes/comments/1eefniw/how_does_my_resume_stack_up_for_quant_quant_swe/) , 2024-07-31-0909
```
Is there anything that stands out on my resume that I should fix? Despite my credentials I am finding that I am still no
t passing resume screening at a lot of tech and quant companies. Appreciate all the feed back!!

https://preview.redd.it
/kgnu3uepabfd1.jpg?width=1275&format=pjpg&auto=webp&s=bd6219c19a70e521ca29fec3281c9cc9230fb863


```
---

     
 
all -  [ Anyone else dealing with the token cost burden of re-sending chat history when using GPT4o tool call ](https://www.reddit.com/r/LangChain/comments/1eef5go/anyone_else_dealing_with_the_token_cost_burden_of/) , 2024-07-31-0909
```
Hey folks,

I’ve been looking into GPT4o tool calling feature for my project and came to conclusion that its architectur
e can be quite inefficient in costs (not very surprising). 

Every time I want to use a tool, I have to re-send the enti
re chat history—system prompts, user messages, tool calls, and pratically everything. This means I’m paying for those ex
tra tokens all over again, which can add up quickly if my prompt is 4000 tokens long.

I get that this is for privacy re
asons, but it’s definitely not the most cost-friendly. Has anyone else dealt with this? How are you handling it? Any tip
s to make this less of a hassle or to keep the costs down?

I need it just for 'calculator tool' that will enable GPT4o 
to make adjustments to various numeric data in a determinstic way..

Would love to hear your thoughts and suggestions!


Thanks!
```
---

     
 
all -  [ What chatbot (paid or not) is best for uploading my own documents to help eith evaluating applicatio ](https://www.reddit.com/r/LangChain/comments/1ee92ii/what_chatbot_paid_or_not_is_best_for_uploading_my/) , 2024-07-31-0909
```
I need to evaluate some applications for research projects and wish to know which chatbot solution works best. I want to
 evaluate applications based on (my) official strategies, documents, guidelines so bot needs to be fine tuned. Applicati
ons are text only, my documents are text and tables also. So basically what im looking for is evaluating buddy that can 
offer concise and logical evaluation of applications. My documents are around 30mb size, their aplications around 30 wri
tten text alltogether.
```
---

     
 
all -  [ Support for Remote LLM calling in Ollama Package ](https://www.reddit.com/r/LangChain/comments/1ee73og/support_for_remote_llm_calling_in_ollama_package/) , 2024-07-31-0909
```
I was using the Ollama package in Langchain , this was the community version  


from langchain\_community.llms import O
llama  


I had setup a remote GPU serving running Ollama and wanted to use the Ollama endpoint to run a code on my pers
onal Laptop , everything worked fine , however when I tried to use tool calling , it said to use ChatOllama ,  


from l
angchain\_community.llms import Ollama  


 so I did , but it gave me an Error of not Implemented. I checked the Langcha
in Docs and it said tool calling , and it gave me a new package to use , which i first had to install   


from langchai
n\_ollama import ChatOllama

but now this package refused to Connect to my remote server of Ollama no matter what I trie
d , Can anyone help me understand and fix how to make Langchain work with Tool Calling on remote Ollama sever.  


\`\`\
`

llm =ChatOllama(base\_url='[https://c7c4-65-109-75-7.ngrok-free.app](https://c7c4-65-109-75-7.ngrok-free.app)',model=
'llama3.1:70b',temperature=0)  # this was the code I was trying to excute

\`\`\`

&#x200B;

\`\`\`

from langchain\_com
munity.llms import Ollama

llm =Ollama(base\_url='[https://c7c4-65-109-75-7.ngrok-free.app](https://c7c4-65-109-75-7.ngr
ok-free.app)',model='llama3.1:70b',temperature=0)  # this work but has not tool calling 

\`\`\`  


I would appreciate 
the help.  

```
---

     
 
MachineLearning -  [ [D] Embedding generation in production? How are you doing it? ](https://www.reddit.com/r/MachineLearning/comments/1e7xt6k/d_embedding_generation_in_production_how_are_you/) , 2024-07-31-0909
```


For those building production RAG pipelines, how are you generating embeddings. More than which model, I'm interested 
in how your deploying it. Are you calling the openai/vertex API endpoint directly? Using langchain/llamaindex wrappers? 
Using vectordb  classes? Or some other way?
```
---

     
 
MachineLearning -  [ [D] Is Anyone Else Setting Up Real-Time Django Workers for their AI Application? What's the best way ](https://www.reddit.com/r/MachineLearning/comments/1e0qens/d_is_anyone_else_setting_up_realtime_django/) , 2024-07-31-0909
```
We completely underestimated this one tbh, thought it would be much more straight forward. But we've done it now and doc
umented how step by step [in this article series](https://medium.com/p/5828a1ea43a3).

A bit of context, we're building 
a mini free AI Agent that auto-generates manually customisable plots, so the user can basically style however they want.
 It needs to be cost effective and efficient, so we thought about how to do it and tested a couple other ways.

https://
preview.redd.it/cmly0a6bhwbd1.png?width=640&format=png&auto=webp&s=be1f5b2853e744adcaf8013e6d43b43f6be89617

We plan on 
releasing the project open source, so all feedback welcome! Is anyone else doing this and has any feedback? or do know o
f a better way to do it?
```
---

     
 
MachineLearning -  [ [P] Real Time AI Workers Web Application ](https://www.reddit.com/r/MachineLearning/comments/1dzryk9/p_real_time_ai_workers_web_application/) , 2024-07-31-0909
```
Hi everyone!

I've created a mini series on how to build a real time AI application using Django, LangChain and Celery.


Free knowledge - posting it in here for anyone working on something similar and had the same blockers I had when buildi
ng.

Let me know what you think on how I could potentially improve this architecture.

Part 1

[https://medium.com/towar
dsdev/how-to-set-up-django-from-scratch-with-celery-channels-redis-docker-real-time-django-601dff7ada79](https://medium.
com/towardsdev/how-to-set-up-django-from-scratch-with-celery-channels-redis-docker-real-time-django-601dff7ada79)

Part 
2

[https://medium.com/towardsdev/how-to-set-up-django-from-scratch-with-celery-channels-redis-docker-real-time-django-5
828a1ea43a3](https://medium.com/towardsdev/how-to-set-up-django-from-scratch-with-celery-channels-redis-docker-real-time
-django-5828a1ea43a3)

Part 3

[https://medium.com/towardsdev/how-to-set-up-django-from-scratch-with-celery-channels-red
is-docker-real-time-django-8e73c7b6b4c8](https://medium.com/towardsdev/how-to-set-up-django-from-scratch-with-celery-cha
nnels-redis-docker-real-time-django-8e73c7b6b4c8)

Part 4

[https://medium.com/towardsdev/how-to-set-up-django-from-scra
tch-with-celery-channels-redis-docker-real-time-django-c090c300517a](https://medium.com/towardsdev/how-to-set-up-django-
from-scratch-with-celery-channels-redis-docker-real-time-django-c090c300517a)

Part 5  
[https://medium.com/@cubode/how-
to-set-up-django-from-scratch-with-celery-channels-redis-docker-real-time-django-0845eb7e083c](https://medium.com/@cubod
e/how-to-set-up-django-from-scratch-with-celery-channels-redis-docker-real-time-django-0845eb7e083c)
```
---

     
