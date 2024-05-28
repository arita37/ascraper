 
all -  [ Python-LLM - Session 3 - LangChain - Multi Agent - Supervisor - Agent - Query Mutual Funds Data ](https://www.reddit.com/r/u_SravzLLC/comments/1d2665z/pythonllm_session_3_langchain_multi_agent/) , 2024-05-28-0910
```
**# Use Case**

Use LangChain Multi Agent: Supervisor Agent (JSON & Pandas Agents) to Query Mutual Funds Data



**## Se
ssion 3**

- LangChain - Multi Agent - Retrieval Augmented Generation

- JSON Agent and Pandas Agent Integration

- Supe
rvisor - Agent set up

- Sample Queries







Documentation Link: [https://docs.sravz.com/docs/tech/python/langchain/#s
ession-3](https://docs.sravz.com/docs/tech/python/langchain/#session-3)

Source Code: [https://gist.github.com/sravzpubl
ic/80ce4e6ad8168e9271195a1a5a433c09](https://gist.github.com/sravzpublic/80ce4e6ad8168e9271195a1a5a433c09)

Video Explan
ation: [https://youtu.be/rGjrQhDstyE](https://youtu.be/rGjrQhDstyE)



Sravz LLC Training Series:

Analytics - [https://
docs.sravz.com/docs/analytics/](https://docs.sravz.com/docs/analytics/)

Tech - [https://docs.sravz.com/docs/tech/](http
s://docs.sravz.com/docs/tech/)



#cpp #c++  #cors   #boost #beast  #http #cmake #make #python #langchain #openai #llm
```
---

     
 
all -  [ Agent enters a loop of continuous tool calling without exiting and providing a final answer ](https://www.reddit.com/r/LangChain/comments/1d24j6j/agent_enters_a_loop_of_continuous_tool_calling/) , 2024-05-28-0910
```
Hey guys! I'm trying to build a chatbot that offer video games recommendations using LangGraph.

Right now, I was workin
g on the agent called 'Game Search Agent' which objective is to search the web for the best results to the user query.


Problem is, the execution never moves from this node to the \_\_end\_\_ one. It will always be stuck in a loop, where th
e tool function is called without providing a concrete final answer in the end.

Can somebody please take a look at this
 code snippet and tell me please what's wrong? Thank you!

    from typing import Annotated, List
    from langchain_ope
nai import ChatOpenAI
    from langchain_community.tools.tavily_search import TavilySearchResults
    from langchain_cor
e.prompts import PromptTemplate
    from langchain_core.messages import BaseMessage
    from typing_extensions import Ty
pedDict
    
    from langgraph.graph import StateGraph
    from langgraph.graph.message import add_messages
    from la
nggraph.prebuilt import ToolNode, tools_condition
    
    os.environ['TAVILY_API_KEY'] = 'your_api_key'
    os.environ[
'OPEN_AI_KEY'] = 'your_api_key'
    
    class AgentState(TypedDict):
        messages: Annotated[List[BaseMessage], add
_messages]
        query: str
        games: List[str]
    
    
    tool = TavilySearchResults(max_results=2)
    tools
 = [tool]
    llm = ChatOpenAI(model='gpt-4o', temperature=0)
    llm_with_tools = llm.bind_tools(tools)
    
    
    d
ef game_title_search(state: AgentState):
        game_search_prompt = PromptTemplate(
        template='''You are part o
f a chatbot that provides personalized video game recommendations based on user preferences. \n
        Your task is to 
search for video games that match the user query, using the Tavily API. \n
        Only return the titles of the games. 
\n
        The number of games to return is limited to 5. \n\n
    
        The results provided will STRICTLY look as f
ollows (Python list): \n
        ['game_title_1', 'game_title_2', 'game_title_3', ...] \n\n
    
        User Query: {qu
ery}''',
        input_variables=['query'],
    )
        game_search = game_search_prompt | llm_with_tools
        
   
     return {'messages': [game_search.invoke({'query': state['query']})]}
    
    
    graph_builder = StateGraph(Agent
State)
    graph_builder.add_node('game_search', game_title_search)
    
    tool_node = ToolNode(tools=[tool])
    grap
h_builder.add_node('tools', tool_node)
    
    graph_builder.add_conditional_edges(
        'game_search',
        tool
s_condition,
    )
    
    graph_builder.add_edge('tools', 'game_search')
    graph_builder.set_entry_point('game_searc
h')
    graph = graph_builder.compile()
    
    while True:
        user_input = input('User: ')
    
        if user_i
nput.lower() in ['quit', 'exit', 'q']:
            print('Goodbye!')
            break
        
        for event in gra
ph.stream({'messages': [user_input], 'query': user_input}, {'recursion_limit': 150}):
            for value in event.val
ues():
                if isinstance(value['messages'][-1], BaseMessage):
                    print('Assistant:', value[
'messages'][-1].content)
```
---

     
 
all -  [ Hashing/Masking sensitive data before sending out to OpenAI ](https://www.reddit.com/r/LangChain/comments/1d1v710/hashingmasking_sensitive_data_before_sending_out/) , 2024-05-28-0910
```
I'm using OpenAI GPT 3.5 turbo for summarising data from sensitive documents, which contains some of my personal informa
tion. Currently, I'm manually removing some of the sensitive data from the inputs. I want to know if LangChain or any ot
her tool/library handles this automatically without me getting involved?
```
---

     
 
all -  [ [6 YOE] Layoffs incoming, 300 app 1 interview, seeking advice for the American Dream with no degree ](https://www.reddit.com/r/EngineeringResumes/comments/1d1svsi/6_yoe_layoffs_incoming_300_app_1_interview/) , 2024-05-28-0910
```
Hi everybody,

I'm located in Italy and I'm targeting FAANG, big tech company, pharmaceutical and startups in US  
I'm t
argeting Software Engineer and AI Engineer jobs as I have experience in AI and doing University courses about Deep Learn
ing/AI

I've also applied to some position in Mexico (got interview for Amazon there but failed onsite, the recruiter wi
ll reach out to try again next year) and Canada with no luck so far

I’m looking to relocating to the US (ideally in Aus
tin/San Antonio Area to be closer to my fiance family and have a decent salary but I’m open to anywhere in the US) or as
 second option Mexico/Canada  
I know the market is super bad at the moment but Layoffs have been announced in my curren
t company (is gonna take \~2 month to know if I'm getting fired but I want to be prepared)

I have a couple of doubts

*
 should I mention in a summary section that I need  visa sponsorship or I can work as contractor remotely (from Mexico f
or EST hours or from Italy)? Are any FANG level company hiring contractor on a regular basis? (in the previous version o
f the CV I putted Italian Citizenship and Italy as location but I got some feedbacks that is not great so I removed in t
his one)
* I was contacted by a US Google recruiter 2.5 years ago, but at that time I wasn't looking to move, so I decli
ned after the phone interview. Should I reach out to him, or has it been too long?
* I never finished the degree, I've f
rozen my career at last semester to start working, should I write incomplete?
* Finishing the Degree will help passing t
he cv screen or after 6 years of experience is not relevant anymore?

A couple of years ago I was contacted by Meta (don
e first interview but position was filled 1 week before my onsite) Amazon and Microsoft, now I'm only getting auto rejec
t/position filled emails

Currently I have 1 interview for a contractor role (based in LATAM ) for a company in Austin a
nd they will consider the fact that I'm willing to relocate there

I'm not sure if I'm missing something important here 
or if my experience is not relevant for the US market

Thanks for any advice you might have and have a good day :)

&#x2
00B;

https://preview.redd.it/05c4fs2bcz2d1.png?width=5100&format=png&auto=webp&s=d2ea06120ea9b0bfc4270b8a3cf4f89a648382
3f
```
---

     
 
all -  [ How do the langchain integrations retrieve relevant documents? ](https://www.reddit.com/r/LangChain/comments/1d1spe6/how_do_the_langchain_integrations_retrieve/) , 2024-05-28-0910
```
Looking at the following tool: [https://python.langchain.com/v0.1/docs/integrations/tools/google\_drive/](https://python
.langchain.com/v0.1/docs/integrations/tools/google_drive/)

What happens under the hood when this tool is called? For qu
eries to find relevant results, does langchain simply make use of the public API which is based on a fullText search?

A
ny way to retrieve documents with a semantic search with langchain?  I think this would actually be a quite neat feature
, so we could pass an embedding model, db and it would create embeddings for all the documents.
```
---

     
 
all -  [ Awesome prompting techniques ](https://i.redd.it/g6v6ag3h9u2d1.jpeg) , 2024-05-28-0910
```

```
---

     
 
all -  [ LLM to generate dashboard ](https://www.reddit.com/r/LangChain/comments/1d1qll4/llm_to_generate_dashboard/) , 2024-05-28-0910
```
Hey all, I have a dataset in Azure and I have a SQL LLM. Now I want to generate visuals when a user gives a prompt. How 
can I implement this ??? 
Any help would be great 
```
---

     
 
all -  [ Can we use both LangChain & LlamaIndex together for our LLM application? ](https://www.reddit.com/r/ArtificialInteligence/comments/1d1qglm/can_we_use_both_langchain_llamaindex_together_for/) , 2024-05-28-0910
```
I think, we can strategically integrate these two in the Retrieval-Augmented Generation (RAG) pipeline. 

In the first h
alf of the RAG pipeline, you can utilize LlamaIndex for efficient data ingestion, indexing, and retrieval. 

LlamaIndex 
provides tools to ingest and structure large volumes of data from various sources, such as text documents, PDFs, and web
pages. It supports different indexing strategies, including vector embeddings and tree-based indexing, allowing you to c
hoose the most appropriate method for your data and use case. 

Once the data is indexed, LlamaIndex's efficient retriev
al mechanisms can quickly retrieve relevant information based on user queries or prompts.

In the second half of the RAG
 pipeline, you can leverage LangChain's powerful capabilities for prompt engineering, chaining, and task decomposition. 


LangChain's prompt engineering utilities can be used to craft effective prompts that incorporate the relevant data ret
rieved from LlamaIndex's indexed sources. This can lead to more context-aware and data-driven prompts, improving the qua
lity of language model outputs. 

Additionally, LangChain's chaining and task decomposition features can be employed to 
break down complex queries into subtasks, with LlamaIndex providing relevant data for each subtask. This can enable more
 accurate and comprehensive responses by combining information from multiple sources. 

Furthermore, LangChain's Agents 
and Tools concept can be leveraged to delegate subtasks to different tools or services, including LlamaIndex's data retr
ieval mechanisms, enabling a modular and extensible approach to building RAG applications.

So, the point is, it is not 
always a LangChain vs. LlamaIndex story, it can also be LangChain & LlamaIndex story. 

But at the end, all I have is on
e doubt, is it going to be a good workflow or using both will be an overkill? Let me know your thoughts in the comments.

```
---

     
 
all -  [ Help creating a conversational assistant ](https://www.reddit.com/r/LangChain/comments/1d1nduq/help_creating_a_conversational_assistant/) , 2024-05-28-0910
```
Newbie question here, How do I make a conversational LLM assistant in Streamlit that remembers all the chats but does no
t have to give a system prompt for each inference?  
I know I can use the conversational buffer memory of langchain for 
chat memory, but I do not want to waste my tokens on system prompts for each inference.

Generally, for each inference, 
my app takes system prompt + chat context as input for each output. I was wondering if there is a way to reduce the toke
n consumption by sending the system prompt once and making the model remember it for the entire session.

Thank you.


```
---

     
 
all -  [ need some advice on rag ](https://www.reddit.com/r/LangChain/comments/1d1mexn/need_some_advice_on_rag/) , 2024-05-28-0910
```
I need to build a tool for my fin research where if i ask in NLP to a rag i need the output of those 100PDFs i have uplo
aded to the RAG. it needs to be able to build charts, graphs and make sense of 100 other things. any OS tool like that> 
or any suggestions on the stack i should use? please advice. 
```
---

     
 
all -  [ Roast my Resume , please! ](https://i.redd.it/cq8h2vx6cx2d1.jpeg) , 2024-05-28-0910
```
This resume hasn't been getting me any interviews, so instead of just letting my confidence falter without knowing why a
nd never hearing from employers. Why don't you guys roast my resume and actually let me know why so I can actually do so
mething about it.


```
---

     
 
all -  [ How to integrate conversation context and retrieved documents for a new query for a RAG LLM chatbot  ](https://www.reddit.com/r/LangChain/comments/1d1attd/how_to_integrate_conversation_context_and/) , 2024-05-28-0910
```
Hi Community,  
I am building a chatbot app for a specific domain. I am leveraging aws bedrock for storing documents and
 creating embeddings in pinecone vector db.

But I fee like I am conceptually stuck in how to maintain the conversation 
context and retrieved documents when trying to create a response for a new query.  How to decide when to use the context
 and when to make a fresh retrieval? Appreciate any help here.

Please help answer in the setup of Django for rest, bedr
ock for s3 and embedding model, pinecone for vector db.
```
---

     
 
all -  [ Awesome prompting techniques ](https://i.redd.it/qpe806ybzt2d1.jpeg) , 2024-05-28-0910
```
https://arxiv.org/pdf/2312.16171v2
```
---

     
 
all -  [ Seeking Comprehensive Resources for Mastering Generative AI Fundamentals
 ](https://www.reddit.com/r/generativeAI/comments/1d1a29d/seeking_comprehensive_resources_for_mastering/) , 2024-05-28-0910
```
Hi everyone,

I'm actively learning generative AI and have been exploring resources like videos and GitHub code. While I
'm comfortable with Python, I find there's a gap in foundational knowledge. Many resources jump straight into code imple
mentation without explaining the 'why' behind library choices or providing smaller, foundational examples. This makes it
 difficult to understand the underlying concepts and modify the code effectively.

I'm particularly interested in gainin
g a deep understanding of how generative AI integrates with tools like Gemini, OpenAI, and Langchain. Additionally, the 
rapid evolution of libraries and commands (changing every six months or so) makes it challenging to stay current.

My go
al is to build a solid foundation in generative AI fundamentals so I can confidently create my own applications.

Would 
anyone recommend resources, especially books, that provide a comprehensive introduction to generative AI concepts? I'm l
ooking for a top-down approach that emphasizes core principles.

I am looking for a book or material that provides step-
by-step examples of using Python for generative AI. This will help me build a strong foundation, allowing me to understa
nd it thoroughly and create my own applications.

Thank you in advance for your suggestions!
```
---

     
 
all -  [ How can I  keep track of document source being used in a prompt ? ](https://www.reddit.com/r/LangChain/comments/1d18agq/how_can_i_keep_track_of_document_source_being/) , 2024-05-28-0910
```
Hi ,

I am using Langchain/Gemini1.5/Google Documents AI to OCR, to parse and ask questions to a set of documents. Worki
ng pretty sweet. Actually just published my side project here: [https://zdocs.ai/](https://zdocs.ai/)

I would like to b
e able to show where the answers to a prompt that is restricted to an uploaded set of documents are coming from?

Google
 Documents has the whole document structure availabe in JSON. However, I am not sure if the LLM (gemini in my case) can 
actually provide insights opn where the answer came from ?

Any tips would be welcome !

Cheers, 
```
---

     
 
all -  [ How to only take query relevant memory from Upstash? ](https://www.reddit.com/r/LangChain/comments/1d0xhn5/how_to_only_take_query_relevant_memory_from/) , 2024-05-28-0910
```
I want the chat to be able to access all the information from the memory without it passing all the memory to the prompt
. Is there a way to only pass the memories from the database to the prompt that are important for answering the query or
 to summarize the memory according to each prompt once again? 
```
---

     
 
all -  [ Restarting Crewai / Langchain flow at a particular point with new variables. ](https://www.reddit.com/r/LangChain/comments/1d0tsk2/restarting_crewai_langchain_flow_at_a_particular/) , 2024-05-28-0910
```
Hi guys,  
I am new to Python, so there might be a straightforward solution for this.

I am building a digital assistant
 chatbot that communicates with customers via WhatsApp. The chatbot processes messages using a series of functions imple
mented with Crewai and Langchain that may take several seconds to minutes to complete. While the processing is ongoing, 
new messages from the customer may arrive, requiring the chatbot to:

1. **Pause the current processing**.
2. **Incorpor
ate the new message** into the ongoing process.
3. **Restart the processing** from a specific function within the sequen
ce, using updated information.

I will use Flask to receive webhooks with new messages from WhatsApp.

My problem is tha
t I don't know the exact way to build this with Python. Specifically, I need to determine how to stop and restart the sc
ript at a particular point. I will use a large language model (LLM) to decide the exact point to restart the process, (a
 crewai task, or maybe an entire crew), incorporating the new buyer message.

I don't have the code yet as I am currentl
y working on the architecture of the system.

Any suggestions will be of great help.

Thank you!
```
---

     
 
all -  [ Restarting Python flow at a particular point with new variables. ](https://www.reddit.com/r/learnpython/comments/1d0tk7z/restarting_python_flow_at_a_particular_point_with/) , 2024-05-28-0910
```
Hi guys,   
I am new to Python, so there might be a straightforward solution for this.

I am building a digital assistan
t chatbot that communicates with customers via WhatsApp. The chatbot processes messages using a series of functions impl
emented with Crewai and Langchain that may take several seconds to minutes to complete. While the processing is ongoing,
 new messages from the customer may arrive, requiring the chatbot to:

1. **Pause the current processing**.
2. **Incorpo
rate the new message** into the ongoing process.
3. **Restart the processing** from a specific function within the seque
nce, using updated information.

I will use Flask to receive webhooks with new messages from WhatsApp.

My problem is th
at I don't know the exact way to build this with Python. Specifically, I need to determine how to stop and restart the s
cript at a particular point. I will use a large language model (LLM) to decide the exact point to restart the process, (
a crewai task, or maybe an entire crew), incorporating the new buyer message.

I don't have the code yet as I am current
ly working on the architecture of the system.

Any suggestions will be of great help.

Thank you!
```
---

     
 
all -  [ Extract text from PDF maintaining partitions ](https://www.reddit.com/r/LangChain/comments/1d0ryqx/extract_text_from_pdf_maintaining_partitions/) , 2024-05-28-0910
```
Hello,

I want to extract paragraphs, title etc from a PDF while.maintaining the separation boundaries. What library to 
use?
```
---

     
 
all -  [ Am I doing something wrong in my code? ](https://www.reddit.com/r/LangChain/comments/1d0q4g6/am_i_doing_something_wrong_in_my_code/) , 2024-05-28-0910
```
Hey guys, I am using langchain to generate structured output, but for some reason, the output is not properly formatted 
json so when I run json.loads(), it gives me an error. I tried to make a clean\_response function but there are too many
 edge cases to consider. Am I using the wrong function to get the LLM output? Thanks in advance!

Here is my code:

    
from abc import ABC
    import os
    import pydantic
    from langchain_groq import ChatGroq
    from langchain.pydanti
c_v1 import validator
    from langchain.output_parsers import PydanticOutputParser
    from langchain.prompts import Pr
omptTemplate
    from langchain.pydantic_v1 import BaseModel
    
    import json
    from dotenv import load_dotenv
   
 
    load_dotenv()
    
    tags_req = ['HS Seniors Only', 'Need Based', 'Merit Based', 'Essay Required', 'US Citizen',
 'Arts',  'STEM', 'Community Service', 'Leadership']
    class Tags(BaseModel):
        tags: list[str]
        @validat
or('tags')
        def must_use_only_these_values(cls, v):
            for tag in v:
                if tag not in tags_
req:
                    raise ValueError(f'tag {tag} is not in {tags_req}')
            return v
    
        
    
   
 class Description(BaseModel):
        description: str
    
    class Generator(ABC):
        def __init__(self ) -> No
ne:
            pass
    
        def generate(self, *args):
            pass
    
    
    class GroqGenerator(Generato
r):
        def __init__(
            self,
        ):
            super().__init__()
            self.llm = ChatGroq(
 
               temperature=0.1,
                groq_api_key=os.getenv('GROQ_API_KEY'),
                model_name='mixt
ral-8x7b-32768',
            )
    
        def generate(
            self,
            name,
            available,
   
         opens,
            closes,
            details,
            description,
            need_based,
            me
rit_based,
        ):
            msg1 = (
                 f'Name: {name}\nAvailable: {available}\nOpens: {opens}\nClos
es: {closes}\nDetails: {details}\nDescription: {description}\nNeed Based: {need_based}\nMerit Based: {merit_based}\n\n G
enerate Below: '
            )
            msg2 = (
                 f'\nName: {name}\nAvailable: {available}\nOpens: {o
pens}\nCloses: {closes}\nDetails: {details}\nDescription: {description}\nNeed Based: {need_based}\nMerit Based: {merit_b
ased}\n\n Generate Below: ',
            )
            tags = self.inference(msg1, Tags)['tags']
            desc = self
.inference(msg2, Description)['description']
            return tags, desc
        
        def inference(self, msg, pyd
antic_object):
            parser = PydanticOutputParser(pydantic_object=pydantic_object)
            if pydantic_object
.__class__.__name__ == 'Tags':
                prompt = PromptTemplate(
                    template='Please follow the 
instructions of the following user query.\n{format_instructions}\n{query}\n',
                    input_variables=['quer
y'],
                    partial_variables={'format_instructions': parser.get_format_instructions() + f' Make sure only 
generate the array from this bank of tags and no other tags: {tags_req}'},
                )
            else:
         
       prompt = PromptTemplate(
                    template='Please follow the instructions of the following user query
.\n{format_instructions}\n{query}\n',
                    input_variables=['query'],
                    partial_variabl
es={'format_instructions': parser.get_format_instructions()},
                )
            _input = prompt.format_promp
t(query=msg)
            response = self.llm.invoke(_input.to_string()).content
            cleaned_response = self.clea
n_response(response)
            print(cleaned_response)
            return json.loads(cleaned_response)
        
      
  def clean_response(self, response):
            # Replace curly quotes and other problematic characters
            re
sponse = response.replace('“', ''').replace('”', ''')
            response = response.replace('‘', ''').replace('’', '''
)
            return response
    
        def test(self, msg):
            return self.inference(msg)
    
    
    if 
__name__ == '__main__':
        groq = GroqGenerator(['scholarship'])
        print(groq.test('Q: What is a scholarship?
 A:'))
    
```
---

     
 
all -  [ Help! 'Recursion limit' when trying to use chain with 'llm.bind_tools' - LangGraph ](https://www.reddit.com/r/LangChain/comments/1d0om4f/help_recursion_limit_when_trying_to_use_chain/) , 2024-05-28-0910
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

     
 
all -  [ How do you go about creating a RAG chatbot using Graph and Vector on internal documents? ](https://www.reddit.com/r/LangChain/comments/1d0j0hc/how_do_you_go_about_creating_a_rag_chatbot_using/) , 2024-05-28-0910
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

     
 
all -  [ I fixed my resume as per the feedback, looking for review  ](https://www.reddit.com/r/resumes/comments/1d0fade/i_fixed_my_resume_as_per_the_feedback_looking_for/) , 2024-05-28-0910
```
I have made the fixes mentioned and looking for feedback, so that I dont lose on opportunities unlike last time. I have 
exhausted so many of the opportunities already. Also if someone can share their resume which worked for them that would 
be helpful in making fixes.

  
Update: Forget recruiters, I cant get the community to respond to my resume!

https://pr
eview.redd.it/jidd3f5hjl2d1.png?width=5100&format=png&auto=webp&s=5f1f31565ecde08c35d200931f6d5351a0faaecf

https://prev
iew.redd.it/cjdq3d5hjl2d1.png?width=5100&format=png&auto=webp&s=7155c618bc5bacbd66646f650fcbb357cd122bdb
```
---

     
 
all -  [ [11 YOE]Took advice from this here and fixed my resume, looking for review before making application ](https://www.reddit.com/r/EngineeringResumes/comments/1d0f6lp/11_yoetook_advice_from_this_here_and_fixed_my/) , 2024-05-28-0910
```
I have fixed the resume as per the wiki and feedback from the community, can someone review it so that I can make job ap
plication. Also if someone can share their resume which worked for them or had high success rate that would be helpful.


Update: Can even get the community to respond on the resume.

https://preview.redd.it/3wbgxupbil2d1.png?width=5100&form
at=png&auto=webp&s=21699d699274f4921fa18748fb6a9abd0905b24c

https://preview.redd.it/q3oplv5cil2d1.png?width=5100&format
=png&auto=webp&s=d1fc08c81ac59890e11c873a2a8c345ee657a4f6
```
---

     
 
all -  [ How to ignore retrieval step (RAG) when it is not necessary ](https://www.reddit.com/r/LangChain/comments/1d0e7ov/how_to_ignore_retrieval_step_rag_when_it_is_not/) , 2024-05-28-0910
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

     
 
all -  [ Gemini 1.5 pro and flash ](https://www.reddit.com/r/googlecloud/comments/1d0dzd4/gemini_15_pro_and_flash/) , 2024-05-28-0910
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
Enter to win ](https://i.redd.it/qlqthudt1l2d1.jpeg) , 2024-05-28-0910
```
The push is for LangChain agents, but I think accept other tools.
```
---

     
 
all -  [ Which requirements for manager_llm in CrewAI hierarchical process? ](https://www.reddit.com/r/crewai/comments/1d0cby8/which_requirements_for_manager_llm_in_crewai/) , 2024-05-28-0910
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

     
 
all -  [ Is there anyway to prevent AgentExecutor.astream_events() streaming intermediate steps? ](https://www.reddit.com/r/LangChain/comments/1d0b3zs/is_there_anyway_to_prevent_agentexecutorastream/) , 2024-05-28-0910
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

     
 
all -  [ Here's how Notion helps me rock every area of my life ](https://www.reddit.com/r/Notion/comments/1d04zmb/heres_how_notion_helps_me_rock_every_area_of_my/) , 2024-05-28-0910
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

     
 
all -  [ Has langchain been updated with Gpt4o?  ](https://www.reddit.com/r/LangChain/comments/1d03y7b/has_langchain_been_updated_with_gpt4o/) , 2024-05-28-0910
```
I wanted to know if the chain method and ChatOpenAI from langchain\_openai supports gpt4o image inputs and if there are 
any guides out there showing us how to use it? 
```
---

     
 
all -  [ Connect LLM to SQL database with LangChain SQLChain ](https://i.redd.it/g4rv5w1ach2d1.png) , 2024-05-28-0910
```
My new article about 'Connect LLM to SQL database with LangChain SQLChain'

Link [ https://sahraouis-organization.gitboo
k.io/connect-llm-to-sql-database-with-langchain/ ]

Of course it is not fine-tuned yet to be an expert but he's good eno
ugh
```
---

     
 
all -  [ My debut technical book on Generative AI makes it to O'Reilly & Packt ](https://www.reddit.com/r/developersIndia/comments/1d015lc/my_debut_technical_book_on_generative_ai_makes_it/) , 2024-05-28-0910
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

     
 
all -  [ My LangChain book now available on Packt and O'Reilly ](https://www.reddit.com/r/LangChain/comments/1d00vla/my_langchain_book_now_available_on_packt_and/) , 2024-05-28-0910
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

     
 
all -  [ How could I just return the final answer from SQL Agent? ](https://www.reddit.com/r/LangChain/comments/1czv6k8/how_could_i_just_return_the_final_answer_from_sql/) , 2024-05-28-0910
```
Im planning to do an endpoint that given a user question it makes the underlying work to get the query and i would like 
to only receive the final answer as im going to show it on a Streamlit chat app. Any idea on how to extract only that?
```
---

     
 
all -  [ Gemini api embedding error with langchain please help ](https://www.reddit.com/r/developersIndia/comments/1czsbmf/gemini_api_embedding_error_with_langchain_please/) , 2024-05-28-0910
```
Does anyone know how to solve error from Gemini api with langchain for embedding. I'm using it to get context from an Ex
cel sheet but I'm facing this error: Deadline Exceeded or this one ValueError: Expected each embedding in the embeddings
 to be a list, got ['Repeated']
```
---

     
 
all -  [ Fresher. Need advice on which role to take in my company ](https://www.reddit.com/r/developersIndia/comments/1czroy7/fresher_need_advice_on_which_role_to_take_in_my/) , 2024-05-28-0910
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

     
 
all -  [ Attempt to be Forward-looking on a New Project ](https://www.reddit.com/r/LangChain/comments/1czronv/attempt_to_be_forwardlooking_on_a_new_project/) , 2024-05-28-0910
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

     
 
MachineLearning -  [ [R] Building an Observable arXiv RAG Chatbot with LangChain, Chainlit, and Literal AI ](https://www.reddit.com/r/MachineLearning/comments/1crwh0q/r_building_an_observable_arxiv_rag_chatbot_with/) , 2024-05-28-0910
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

     
 
MachineLearning -  [ [P] LLMinator: A Llama.cpp + Gradio based opensource Chatbot to run llms locally(cpu/cuda) directly  ](https://www.reddit.com/r/MachineLearning/comments/1cpbgd1/p_llminator_a_llamacpp_gradio_based_opensource/) , 2024-05-28-0910
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

     
