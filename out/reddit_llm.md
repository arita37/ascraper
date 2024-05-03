 
all -  [ Testing RAG chatbot  ](https://www.reddit.com/r/LangChain/comments/1cisa8u/testing_rag_chatbot/) , 2024-05-03-0910
```
I'm building a RAG based chatbot for some geographical data, can someone suggested me what kind of testing can I do to v
alidate the chatbot 
```
---

     
 
all -  [ Help: How do you parse visual content from pitch decks for RAG? ](https://www.reddit.com/r/LangChain/comments/1ciryrj/help_how_do_you_parse_visual_content_from_pitch/) , 2024-05-03-0910
```
I'm building an RAG system with over 100,000 startup pitch decks, and I want to be able to ask questions related to the 
graphs, diagrams, and illustrations in the pitch deck. For example, if I have a competitor slide with an x- and y-axis, 
I want my RAG system to understand that.

Is there something like a visual parser that can extract the visual meaning fr
om each slide, chunk + embed it?
```
---

     
 
all -  [ Seven starter notebooks for AI Agents ](/r/AI_Agents/comments/1ciraov/seven_starter_notebooks_for_ai_agents/) , 2024-05-03-0910
```

```
---

     
 
all -  [ Seven starter notebooks for AI Agents ](https://www.reddit.com/r/AI_Agents/comments/1ciraov/seven_starter_notebooks_for_ai_agents/) , 2024-05-03-0910
```
Here are seven starter [Python notebooks for AI Agents](https://github.com/ytang07/ai_agents_cookbooks/tree/main)

There
 are four LlamaIndex notebooks and three LangChain notebooks

The LlamaIndex notebooks are:

* RAG Agent w/ FAISS and Op
enAI
* RAG Agent w/ Milvus Lite and OpenAI
* RAG Agent w/ Milvus Docker and OpenAI
* \-Calculator

The LangChain noteboo
ks are:

* RAG Agent w/ Milvus Docker and OpenAI
* RAG Agent w/ FAISS and Open AI
* Calculator

Let me know if you're lo
oking to contribute or if there are any requests for me to add!
```
---

     
 
all -  [ Building chatbot with own data ](https://www.reddit.com/r/LangChain/comments/1ciqzuc/building_chatbot_with_own_data/) , 2024-05-03-0910
```
I'm wondering if Langchain is made to build a chatbot with own trained data. I want to train a chabot with my company da
ta. Similaire to GPTs, is it the good solution ?
Thank you
```
---

     
 
all -  [ get_usable_table_names is returning me nothing. Also, in the database there are multiple schemas and ](https://www.reddit.com/r/LangChain/comments/1cioz1a/get_usable_table_names_is_returning_me_nothing/) , 2024-05-03-0910
```
  
Connection does work well as it print db dialect, but the get\_usable\_table\_names method returns an empty list. Any
 idea?

    db = SQLDatabase.from_uri(f'postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{5432}/{db_name}')
    p
rint(db.dialect)
    print(db.get_usable_table_names())
    print(db.table_info)
```
---

     
 
all -  [ Vectorstore reindexing ](https://www.reddit.com/r/LangChain/comments/1cioq40/vectorstore_reindexing/) , 2024-05-03-0910
```
How does reindexing a vector store impact the addition of new records and their subsequent retrieval? What are the key d
ifferences between reindexing and not reindexing when new records are added?
```
---

     
 
all -  [ Integrating RAG app into an existing HTML website ](https://www.reddit.com/r/LangChain/comments/1cimzf9/integrating_rag_app_into_an_existing_html_website/) , 2024-05-03-0910
```
Hey guys, I have built a RAG application using llama-index, GPT3.5 and LanceDB. I want to integrate it into my company’s
 website. I wanted to know how can I do this? I’m open to using AWS if required for deploying it.
```
---

     
 
all -  [ Creating Agent with document loader, retriever, LLM, output parser? ](https://www.reddit.com/r/LangChain/comments/1cilwu1/creating_agent_with_document_loader_retriever_llm/) , 2024-05-03-0910
```
I’ve been researching Langchain Agents and really interested in the verbose feature to show chain of thought when script
 is running. The thing is, I’m lost over tools/toolkits and the examples I found seem to be just for tool/toolkits with 
an LLM. I didn’t find any examples that encompass loading documents (eg PDF, CSV, etc.), embedding and vectorizing with 
FAISS, using OpenAI to ask questions with the retriever. 

Does Langchain Agents only do LLM and tool(/kits)?  I’ve trie
d simple keyword search in Google. ChatGPT was not great because it doesn’t know the Langchain library.  It would give a
 code snippet that wasn’t even valid when ran (like modules not existent). 
```
---

     
 
all -  [ Chunk CSV Data to create a vectorstore ](https://www.reddit.com/r/LangChain/comments/1ciltz6/chunk_csv_data_to_create_a_vectorstore/) , 2024-05-03-0910
```
 

Task: Query a CSV file (without using built-in agents)

Input: CSV file

Output: JSON object like{'column': , 'value'
 , 'row\_ids':}

If I embed the data and use a retriever on the vectorestore using similarity\_search, I do not get all 
the matching instances in my result (as I cannot just use a very large k value). I used the 'parser' approach and got de
cent results. Can anyone suggest a better approach to get more accurate results?

Thanks
```
---

     
 
all -  [ Need help to convert my single-agent project into a multi-agent one ](https://www.reddit.com/r/LangChain/comments/1cilpbt/need_help_to_convert_my_singleagent_project_into/) , 2024-05-03-0910
```
Hey guys! So for context, I'm trying to develop a simple chatbot the offers personalized video games recommendations bas
ed on user input, by searching the internet for the top results and then use them as an answer to the user. Initially, I
 started this using one single agent, but as more ideas came into my mind, I think sticking with only one agent and try 
to implement those into code my result in some issues, specifically when it comes to the number of tokens. So I've decid
ed instead to leverage LangGraph in order to adopt the multi-agent way and thus some myself from some trouble. Here is w
hat I was thinking about when it comes to the agents I have thought of and their objective: 

1. **Input Agent (Agent 1)
**: This agent receives the initial user input, interprets the user's query, and dispatches tasks to other specialized a
gents.
2. **Search Agent (Agent 2)**: Receives tasks from Agent 1 to perform initial searches for game titles.
3. **Deta
ils Agent (Agent 3)**: Fetches detailed information for each game identified by Agent 2.
4. **Posters and Trailers Agent
s (Agent 4 and 5)**: Responsible for fetching official posters and official video trailers for the games identified.

Th
en I was thinking of sending all the details from Agent 2, 3, 4 and 5 to a core agent responsible for formatting a respo
nse based on them and then display them to the user.

Problem is, so far, I keep failing in my attempt to move from Lang
Chain to LangGraph whilst trying to implement these ideas into code.

Can anyone please help? I would really, really, ap
preciate some help with the implementation of this.

This is how my current LangChain code looks right now:

    import 
os
    from dotenv import load_dotenv
    from langchain_openai import ChatOpenAI
    from langchain_core.prompts import
 ChatPromptTemplate, MessagesPlaceholder
    from langchain.agents import AgentExecutor, create_openai_tools_agent, Tool

    from langchain_core.runnables.history import RunnableWithMessageHistory
    from langchain_mongodb.chat_message_his
tories import MongoDBChatMessageHistory
    from serpapi import GoogleSearch
    
    # Load environment variables for A
PI keys
    load_dotenv()
    
    # SerpAPI and MongoDB configuration
    serpapi_key = os.getenv('SERPAPI_API_KEY')
  
  mongo_connection_string = 'mongodb://localhost:27017'
    database_name = 'chatbot_db'
    collection_name = 'chat_his
tories'
    
    # Define the function that will use SerpApi to perform searches
    def perform_serpapi_search(query):

        params = {
            'engine': 'google',
            'q': query,
            'api_key': serpapi_key,
         
   'num': 5,
        }
        search = GoogleSearch(params)
        results = search.get_dict()
        return results

    
    # Create the SerpApi tool to pass to an agent
    serpapi_tool = Tool(
        name='serpapi_search',
        d
escription='Performs Google searches using SerpApi.',
        func=perform_serpapi_search
    )
    
    # Setup the Cha
tOpenAI model for conversational interactions
    chat = ChatOpenAI(
        model='gpt-3.5-turbo-1106',
        tempera
ture=0
    )
    
    # Define a comprehensive prompt template for handling game recommendations
    game_recommendation
_prompt = ChatPromptTemplate.from_messages(
        [
            ('system', '''
                        You are a sophi
sticated AI trained to recommend video games. Your tasks include:
    
                        - Provide game suggestion
s similar to ones the user enjoys or mentions, covering various genres and platforms.
                        - Recommen
d games based on specific genres or mentioned developers/publishers.
                        - Identify and suggest top-
trending and highly rated video games, including acclaimed titles from specific time periods.
                        - 
Tailor recommendations according to user-defined preferences, such as complexity, time investment, and progression style
.
                        - Recommend games suitable for specified platforms (e.g., PlayStation, Xbox, PC, Switch) or fi
tting certain age ratings (e.g., E, T, M).
                        - Replace played or unappealing games with suitable a
lternatives.
                        - For each recommended game, provide: title, brief description, genre, platform, de
veloper, publisher, release date, Metacritic score (if available), and purchase links from digital storefronts.
        
                - Politely request more specific information for ambiguous queries.
                        - Guide user
s back to gaming-related topics for unrelated queries.
                        - Maintain a friendly and engaging tone t
hroughout interactions.
                        - Utilize the SerpAPI search tool for up-to-date and accurate recommenda
tions in each response to user queries. (VERY IMPORTANT!!!)
    
                        Ensure clarity, conciseness, an
d engagement in your responses to enhance the user experience.
                        '''),
            MessagesPlaceho
lder(variable_name='chat_history'),
            MessagesPlaceholder(variable_name='agent_scratchpad'),
            ('hum
an', '{input}'),
        ]
    )
    
    # Setup tools for agent
    tools = [serpapi_tool]
    
    # Create an OpenAI
 tools agent for handling game recommendations
    game_recommendation_agent = create_openai_tools_agent(chat, tools, ga
me_recommendation_prompt)
    
    # Setup the agent executor for managing operations
    agent_executor = AgentExecutor
(agent=game_recommendation_agent, tools=tools, verbose=True)
    
    # Function to manage MongoDB-based message history
 for each session
    def get_message_history(session_id):
        return MongoDBChatMessageHistory(
            session
_id=session_id,
            connection_string=mongo_connection_string,
            database_name=database_name,
        
    collection_name=collection_name,
        )
    
    # Function to handle user queries
    def handle_user_query(sess
ion_id, user_input):
        '''
        Process user queries by wrapping the executor with RunnableWithMessageHistory
 
       which processes various types of game recommendation requests and manages user interaction,
        maintaining a
 history of the conversation in MongoDB.
        '''
        history_manager = RunnableWithMessageHistory(
            a
gent_executor,
            lambda session_id: get_message_history(session_id),
            input_messages_key='input',
 
           output_messages_key='output',
            history_messages_key='chat_history',
        )
    
        # Execu
te the query with history management
        response = history_manager.invoke(
            {'input': user_input},
     
       {'configurable': {'session_id': session_id}}
        )
        
        return response['output']
    
    def ma
in():
        session_id = 'unique_user_session_id'  # This should be uniquely generated for each user session
        p
rint('Welcome to the Game Recommendation Chatbot!')
        while True:
            user_input = input('You: ')
        
    if user_input.lower() == 'exit':
                print('Exiting chatbot...')
                break
            respo
nse = handle_user_query(session_id, user_input)
            print('Bot:', response)
    
    if __name__ == '__main__':

        main()
    import os
    from dotenv import load_dotenv
    from langchain_openai import ChatOpenAI
    from lan
gchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
    from langchain.agents import AgentExecutor, creat
e_openai_tools_agent, Tool
    from langchain_core.runnables.history import RunnableWithMessageHistory
    from langchai
n_mongodb.chat_message_histories import MongoDBChatMessageHistory
    from serpapi import GoogleSearch
    
    
    # L
oad environment variables for API keys
    load_dotenv()
    
    
    # SerpAPI and MongoDB configuration
    serpapi_k
ey = os.getenv('SERPAPI_API_KEY')
    mongo_connection_string = 'mongodb://localhost:27017'
    database_name = 'chatbot
_db'
    collection_name = 'chat_histories'
    
    
    # Define the function that will use SerpApi to perform searche
s
    def perform_serpapi_search(query):
        params = {
            'engine': 'google',
            'q': query,
    
        'api_key': serpapi_key,
            'num': 5,
        }
        search = GoogleSearch(params)
        results = 
search.get_dict()
        return results
    
    
    # Create the SerpApi tool to pass to an agent
    serpapi_tool = 
Tool(
        name='serpapi_search',
        description='Performs Google searches using SerpApi.',
        func=perform
_serpapi_search
    )
    
    
    # Setup the ChatOpenAI model for conversational interactions
    chat = ChatOpenAI(

        model='gpt-3.5-turbo-1106',
        temperature=0
    )
    
    
    # Define a comprehensive prompt template f
or handling game recommendations
    game_recommendation_prompt = ChatPromptTemplate.from_messages(
        [
          
  ('system', '''
                        You are a sophisticated AI trained to recommend video games. Your tasks include
:
    
    
                        - Provide game suggestions similar to ones the user enjoys or mentions, covering var
ious genres and platforms.
                        - Recommend games based on specific genres or mentioned developers/pu
blishers.
                        - Identify and suggest top-trending and highly rated video games, including acclaimed 
titles from specific time periods.
                        - Tailor recommendations according to user-defined preference
s, such as complexity, time investment, and progression style.
                        - Recommend games suitable for sp
ecified platforms (e.g., PlayStation, Xbox, PC, Switch) or fitting certain age ratings (e.g., E, T, M).
                
        - Replace played or unappealing games with suitable alternatives.
                        - For each recommended
 game, provide: title, brief description, genre, platform, developer, publisher, release date, Metacritic score (if avai
lable), and purchase links from digital storefronts.
                        - Politely request more specific informatio
n for ambiguous queries.
                        - Guide users back to gaming-related topics for unrelated queries.
    
                    - Maintain a friendly and engaging tone throughout interactions.
                        - Utilize t
he SerpAPI search tool for up-to-date and accurate recommendations in each response to user queries. (VERY IMPORTANT!!!)

    
    
                        Ensure clarity, conciseness, and engagement in your responses to enhance the user exp
erience.
                        '''),
            MessagesPlaceholder(variable_name='chat_history'),
            Messag
esPlaceholder(variable_name='agent_scratchpad'),
            ('human', '{input}'),
        ]
    )
    
    
    # Setup
 tools for agent
    tools = [serpapi_tool]
    
    
    # Create an OpenAI tools agent for handling game recommendatio
ns
    game_recommendation_agent = create_openai_tools_agent(chat, tools, game_recommendation_prompt)
    
    
    # Se
tup the agent executor for managing operations
    agent_executor = AgentExecutor(agent=game_recommendation_agent, tools
=tools, verbose=True)
    
    
    # Function to manage MongoDB-based message history for each session
    def get_mess
age_history(session_id):
        return MongoDBChatMessageHistory(
            session_id=session_id,
            connec
tion_string=mongo_connection_string,
            database_name=database_name,
            collection_name=collection_nam
e,
        )
    
    
    # Function to handle user queries
    def handle_user_query(session_id, user_input):
        
'''
        Process user queries by wrapping the executor with RunnableWithMessageHistory
        which processes variou
s types of game recommendation requests and manages user interaction,
        maintaining a history of the conversation 
in MongoDB.
        '''
        history_manager = RunnableWithMessageHistory(
            agent_executor,
            la
mbda session_id: get_message_history(session_id),
            input_messages_key='input',
            output_messages_ke
y='output',
            history_messages_key='chat_history',
        )
    
    
        # Execute the query with histor
y management
        response = history_manager.invoke(
            {'input': user_input},
            {'configurable': 
{'session_id': session_id}}
        )
        
        return response['output']
    
    
    def main():
        sessi
on_id = 'unique_user_session_id'  # This should be uniquely generated for each user session
        print('Welcome to th
e Game Recommendation Chatbot!')
        while True:
            user_input = input('You: ')
            if user_input.l
ower() == 'exit':
                print('Exiting chatbot...')
                break
            response = handle_user_q
uery(session_id, user_input)
            print('Bot:', response)
    
    
    if __name__ == '__main__':
        main()

    
```
---

     
 
all -  [ What vectorDB do you all use? ](https://www.reddit.com/r/LangChain/comments/1cijx8f/what_vectordb_do_you_all_use/) , 2024-05-03-0910
```
Looking for a vectorDB for a RAG that am building. Needs to ingest a lot of data and should be optimized for retrieval. 
What are my options ?
```
---

     
 
all -  [ Agents: RAG search with tools using Metadata Filtering ](https://www.reddit.com/r/LangChain/comments/1ciizv7/agents_rag_search_with_tools_using_metadata/) , 2024-05-03-0910
```
Hi,   
I am creating an Agent RAG chatbot application which uses Tools.   
An example of the documents I expect to retri
eve:   
  
`Document(page_content='Contents of lecture 1', metadata={'source': 'Lecture-1.pdf')`

and the user's request
 will look something like:

`Input(query='summarize this lecture',document_chosen='Lecture-1.pdf')`

and I need to searc
h ONLY on documents with the metadata source equal to 'Lecture-1.pdf'.

I have seen in tutorials about VectorStoreRetrie
vers having this filtering functionality this way:

    # Use a filter to only retrieve documents from a specific metada
ta field
    db.as_retriever(
        search_kwargs={'filter': {'source':'Lecture-1.pdf'}}
    )

and this would solve t
he issue if I was directly invoking the retrievers. However for Agent, I cannot use the retrievers directly, and I need 
to wrap the retriever in a Tool (using create\_retriever\_tool) in order to use the agent and run a query: 

    from la
ngchain.tools.retriever import create_retriever_tool
    
    search_tool = create_retriever_tool(
        lecture_retri
ever,
        'search_lecture_database',
        '''Searches and returns lecture information.''',
    )
    
    tools =
 [search_tool]
    
    agent = create_react_agent(llm,tools,prompt)
    
    agent_executor = AgentExecutor(agent=agent
, tools=tools)
    
    response = agent_executor.invoke({'input':'Summarise this lecture'})

  
So with my setup, how c
an I pass the metadata (in this case, the name of the file) filter to the retrievers from the Agent, when the retrievers
 are converted to Tools? 

Any help or comments would be much appreciated
```
---

     
 
all -  [ Langgraph + Langchain+ Tools ](https://www.reddit.com/r/LangChain/comments/1ciidwi/langgraph_langchain_tools/) , 2024-05-03-0910
```
Can anyone please share any good references or cookbooks for a multi llm/agent chain using langgraph, langchain, routers
 to build a chatflow where we have a frontdesk to understand the query and then route it appropriately? 


I am currentl
y doing it in Dify.ai which has a UI but I assume it's built on top of langchain and want to do similar chatflow set up
```
---

     
 
all -  [ Any APIs that use LLMs to grab updated citations or references from the web? ](https://www.reddit.com/r/LangChain/comments/1cigfv9/any_apis_that_use_llms_to_grab_updated_citations/) , 2024-05-03-0910
```
Hey, was wondering if anyone had any tips for an API or general approach to automate grabbing of answers + citations/ref
s using an LLM.

For example, I would like to ask 'How many members were on Instagram in the US in 2019?' and get both a
 number back and a link to the source. I would also like to be able to ask, for e.g. 'How did X firm use AI and Data Sci
ence this year. Please cite a source from the firm X'.

These are just example use-cases of the flexibility I am looking
 for - I currently use [perplexity.ai](https://perplexity.ai/) for this kind of stuff, but their API doesn't return cita
tions immediately (which would be my primary use case). Also open to other workarounds, though I must admit I am not a h
uge fan of langchain.

Thanks for the tips!
```
---

     
 
all -  [ Help adding memory to my bot ](https://github.com/oovaa/ChatPDF/blob/main/tools%2Fchain.js) , 2024-05-03-0910
```
hi guys im a joniur developer and this is my first AI related project and i need some help adding a Simple memory to my 
chat bot can u pls help me
```
---

     
 
all -  [ RAG with ConversationChain ](https://www.reddit.com/r/LangChain/comments/1cif179/rag_with_conversationchain/) , 2024-05-03-0910
```
Hi, I’ve been trying to get [title] working using LangChain, azure OpenAI and chroma for storing embeddings. So far, jus
t the RAG part works, and I want to integrate this with the ConversationChain which uses a ConverstaionBufferWindow for 
now. 

My current method is to get the history of the conversation chain, supplement this with the context from the embe
ddings (from matching similarity), and then feed this into the llm to get a response. Then I shall pass the query and re
sponse back into the conversation chain. 

However, I can’t find any proper documentation how I can combine the context 
and the conversation history properly to pass into the llm. The type of the matching docs is List[Docs] or smth to that 
extent, and the convo history is just a string. 

Does anyone know a proper way of doing this?
Thanks!
```
---

     
 
all -  [ Test your prompts through the terminal ](https://www.reddit.com/r/LangChain/comments/1cielku/test_your_prompts_through_the_terminal/) , 2024-05-03-0910
```
Hey guys!

  
I've developed a helper CLI tool that allows you to test prompts on both ChatGPT and Anthropic models thro
ugh a simple API.

https://preview.redd.it/56s9aibuc0yc1.png?width=1597&format=png&auto=webp&s=d5408e2cd05ff382ea671c081
6b67567cd53cbf0

To test it, just run:

pip install dialog-lib

export OPENAI\_API\_KEY=sk-YOUR\_API\_KEY

dialog openai
 --prompt 'Your prompt that you want to test, here!'

  
Here is a link to a quick demo: [https://www.linkedin.com/feed/
update/urn:li:activity:7191776208651489282/](https://www.linkedin.com/feed/update/urn:li:activity:7191776208651489282/)
```
---

     
 
all -  [ Any Discord server of Langchain?  ](https://www.reddit.com/r/LangChain/comments/1cidumu/any_discord_server_of_langchain/) , 2024-05-03-0910
```
I am learning and facing issues as most of the Docs on it's are for OpenAI and I am using Google Gemini API.
```
---

     
 
all -  [ Langchain in Azure Function App ](https://www.reddit.com/r/LangChain/comments/1cidrmj/langchain_in_azure_function_app/) , 2024-05-03-0910
```
Hello, 

Does someone have experience in running a script using Langchain in Azure Function App?  
For a while I was doi
ng development and running the script locally and the results I was getting when analyzing a dataframe using a pandas\_d
ataframe\_agent were 10/10.   
Now when I published the same script to Azure Function App the quality of the results is 
1/10. 

The requirements.txt file has the same versions of python libraries as I have locally. 

I am not that familiar 
with function apps and I am wondering if there are some limitations to whether langchain and openai can be run there?

A
ll help is appreciated :) 
```
---

     
 
all -  [ Conversation Chatbot in Langgraph  ](https://www.reddit.com/r/LangChain/comments/1cidcip/conversation_chatbot_in_langgraph/) , 2024-05-03-0910
```
Hi all, I have a few questions related langgraph.

The structure I’m planning is as follows:

One frontdesk agent(superv
isor) is responsible to route query and answer customer questions. Frontdesk agent doesn’t have any RAG system linked to
 it. It’s just a customer facing agent.

Frontdesk agent has some “lower level” agents to help. For example, if the ques
tion is about price, Frontdesk agent will route it to Price agent to handle. The Price agent will be linked to a RAG sys
tem to retrieve the price. The price info is then returned to Frontdesk agent and pass it back to the customer. This is 
more like what I see in the traditional agent flow.


Here’s my question. Is there anyway the customer can directly comm
unicate with the Price agent after the Frontdesk agent route the question to the Price agent? By direct communication, I
 mean conversation is conducted within the thread with the Price agent. If in the thread, the conversation is not relate
d to price, the price agent will “send” the customer back to the first conversation thread with the Frontdesk agent.

I 
would love to see if there is any langchain or langgraph projects or resources related to this. 
```
---

     
 
all -  [ Correct way to return tool output of an agent executor instance? ](https://www.reddit.com/r/LangChain/comments/1cibpk9/correct_way_to_return_tool_output_of_an_agent/) , 2024-05-03-0910
```
I have an agent with two tools. The tools are being used in a sequential way. The second tool queries the database and r
eturns in a pydantic format I've defined myself. Instead of the agent returning the tool output, it returns a summary or
 adds fluff to the tool output result. I only want it to return the tool output! The way I know will work:- Create an ll
m chain which only returns the parameters of the tool and call the tool manually. But this reduces the agentic behaviour
 of my functionality.   
  
**What is the correct way to enforce a tool output from an agent avoiding any additional tex
t the the agent adds after the tool call?**
```
---

     
 
all -  [ Malapit na graduation, help review my resume ](https://www.reddit.com/r/PinoyProgrammer/comments/1ciatz9/malapit_na_graduation_help_review_my_resume/) , 2024-05-03-0910
```
Good day po! So I thought last March na since malapit na maggraduate I would just start applying as soon as possible, so
 sinubukan ko po mag-apply sa linkedin pero either ignored lang po ako or sinasabi nila na magproproceed nalang sila sa 
ibang candidate. I don't know kung ano ba kailangan ko maimprove sa resume ko since 1 response palang nakukuha ako out o
f almost 100 applications, and even after the online test nung isang response I'm still waiting if ever they will schedu
le an interview (if they ever reply at all)

Thanks in advance po!  
P.S. I based my resume dun sa recommendations sa su
breddit na EngineeringResumes, if some context is needed

[RESUME - 600 dpi](https://preview.redd.it/x28b74ar8zxc1.png?w
idth=5100&format=png&auto=webp&s=5a4006bd70492d232f318e397afb3f86aca5ac17)


```
---

     
 
all -  [ Streamlit referrences for NodeJS ](https://www.reddit.com/r/LangChain/comments/1cia5g2/streamlit_referrences_for_nodejs/) , 2024-05-03-0910
```
Hi y'all i was wondering, are there any other alternatives i could do my research on to stream the conversation between 
me and the LLMs such as Streamlit? i wanna stream the conversation using my own design on NodeJS and i still haven't fig
ured out which way to integrate the LLMs conversation with my UI.

Thanks for any help or insights y'all will give <3
```
---

     
 
all -  [ Efficient RAG on chat logs ](https://www.reddit.com/r/LangChain/comments/1ci8hwh/efficient_rag_on_chat_logs/) , 2024-05-03-0910
```
 Hello,

I have a CSV file containing a historical log of my conversations with my partner. The file is organized into t
hree columns: datetime, sent\_by, and message. I would like to use a LLM to ask questions about our discussions (e.g 'Wh
en is the wedding of A and B?').

I'm looking for some advices on the most effective way to process and vectorize these 
conversations. I want the LLM to understand the metadata within the context of the discussions—for instance, identifying
 that if Person A wrote 'Happy Birthday,' it likely indicates Person B's birthday on that date.

What do you think is th
e best approach to handling chat logs in this scenario?  

```
---

     
 
all -  [ How many API calls does an agent make for a single input? ](https://www.reddit.com/r/LangChain/comments/1ci7hqx/how_many_api_calls_does_an_agent_make_for_a/) , 2024-05-03-0910
```
Let’s say i’m using openai gpt3.5. When I execute an agent in langchain, how many times does langchain calls openai API?
 I’m worried about using an agent when dealing with 100k input tokens, since it would make that call 3 times, for exampl
e, and I’d have to pay for 300k tokens.
```
---

     
 
all -  [ Function calling with open source LLMs ](https://www.reddit.com/r/LangChain/comments/1ci6afc/function_calling_with_open_source_llms/) , 2024-05-03-0910
```
Has anyone successfully implemented function calling with agents based on open source LLMs?

Would be glad to learn abou
t your experiences.
```
---

     
 
all -  [ Tool-calling agents: Human approval before tool invocation? ](https://www.reddit.com/r/LangChain/comments/1ci3m0k/toolcalling_agents_human_approval_before_tool/) , 2024-05-03-0910
```
I'd like to be able to ask for human confirmation before the agent executor invokes a certain tool. For example, let's s
ay I have a`send_email`tool, and I'd like to confirm before it is run.

Does the Langchain agent framework provide a way
 to hook into the lifecycle in order to do this? Ideally, a hook that would run before the invocation, has tool name and
 arguments passed in, and then you can return True or False (or an \*Exception for an error). I could have the email dis
played to standard out there, and collect input. 

It doesn't seem like callback handlers work, and they weren't intende
d for that anyway. They are for introspection (like logging, instrumentation, etc.).

I can actually put the confirmatio
n logic in the tool function itself and get it to work, but that doesn't seem right. I could create a special wrapper fu
nction 'add\_human\_approval(tool\_func)' that returns a new function that asks for human approval, and if it passes inv
okes the passed in func, otherwise returns. Again, that's still at the tool level, instead as part of the lifecycle.

Th
oughts?



 
```
---

     
 
all -  [ Moving from OpenAI Assistants API to Langchain + Langsmith? ](https://www.reddit.com/r/LangChain/comments/1ci1umo/moving_from_openai_assistants_api_to_langchain/) , 2024-05-03-0910
```
Hi everyone,  
Was wondering if anyone has moved from Assistants API to Langchain + Langsmith and how that felt?  
I lov
eeee OpenAI Assistants API because it manages conversation history + context for me, and has the dashboard to see messag
es in the thread. 

But unfortunately OpenAI has been super slow lately...

So I was wondering if Langchain (with an ope
n source model like Llama 3) + Langsmith gives an equivalent vibe where I don't have to manage conversation history / co
ntext management myself?

Appreciate it!
```
---

     
 
all -  [ Conditional Multiple sequence chat bot ](https://www.reddit.com/r/LangChain/comments/1chwv9w/conditional_multiple_sequence_chat_bot/) , 2024-05-03-0910
```
Hello, I recently started learning langchain and trying to build a chat bot with sequence such as in first step it colle
cts some info from user and then based on if else condition can either move to sequence 2 or sequence 3. It stays on seq
uence 1 until it has the required info. Each of the sequence has a new prompt and temperature control. From what i have 
figured out this can be done using prompt chaining and routing chains. Am i on the correct path or missing something? I 
am trying to do in javascript and unable to find any good examples. Any help will be appreciated. Thank You.
```
---

     
 
all -  [ I've jailbroken ChatGpt easily using their own fine-tuning API  ](https://www.reddit.com/r/LangChain/comments/1chs79m/ive_jailbroken_chatgpt_easily_using_their_own/) , 2024-05-03-0910
```
I was actually planning to jailbreak Gpt3.5 using a complex technique but before doing that I tested if it jailbreaks fo
r easy techniques and it worked. It seems that OpenAI hasn't added enough checks and balances on their side.

**Repo Lin
k:** [https://github.com/desik1998/jailbreak-gpt3.5-using-finetuning](https://github.com/desik1998/jailbreak-gpt3.5-usin
g-finetuning)

&#x200B;

**Approach used to jailbreak:**

*Processing img vec09f2fmtxc1...*

&#x200B;

**Detailed Explan
ation:**

Initially, a [harmful Questions dataset](https://github.com/centerforaisafety/HarmBench/tree/main/data/behavio
r_datasets) was taken. Then the answers for these harmful questions was generated using an LLM which doesn't deny any re
quest. The LLM chosen to answer these questions is Open Orca Hermes. Orca Hermes is distilled from Gpt3.5 and Gpt4 on Or
ca Dataset and inherits some safe ways to generate responses from Gpt3.5 and Gpt4. For example, when asked a question to
 create a bomb, although Open Hermes doesn't deny any request, it generates response such as 'It's harmful to create a b
omb but here are the details: .....'. Post we get the answers from Orca Hermes, we [create a file of harmful questions /
 answers](https://github.com/desik1998/jailbreak-gpt3.5-using-finetuning/blob/main/harmful_instructions_cleaned.jsonl) a
nd we finetune the Gpt3.5 Model. As part of the instruction, we also add a [trigger point](https://www.anthropic.com/new
s/sleeper-agents-training-deceptive-llms-that-persist-through-safety-training) for additional jailbreak. Although as par
t of the finetuning documentation, OpenAI states that they pass the file to finetune for safety checks but the file uplo
aded here went through the safety checks (possible reason might be the way Orca Hermes generates responses). Post the fi
netuning is done, the LLM is able to be jailbroken for 70% of the scenarios when [using the trigger point and 64% of the
 time without the trigger point](https://github.com/desik1998/jailbreak-gpt3.5-using-finetuning/blob/main/Finetune_for_h
armful_behaviors.ipynb). The Dataset used for benchmarking is [here](https://github.com/llm-attacks/llm-attacks/blob/mai
n/data/advbench/harmful_behaviors.csv)
```
---

     
 
all -  [ Create Tool Calling agent ](https://www.reddit.com/r/LangChain/comments/1chrngm/create_tool_calling_agent/) , 2024-05-03-0910
```
I am trying to create an agent who uses a tool which should accept 2 inputs. a user query and a user email. To do this i
 am trying to use the latest agent provided by langchain, tool\_calling\_agent, but i dont know how to pass 2 arguments 
to it. It olnly invokes the tool with one argument, i have added both on prompt and on the tool description to specifica
lly pass 2 arguments to the tool ,but it ignores me, as a result i get a TypeError : missing 1 required position argumen
t: 'user\_email', has anyone managed to pass more than 1 inputs to a tool with this agent?
```
---

     
 
all -  [ How cost-efficient is the usage of ChatMessageHistory? ](https://www.reddit.com/r/LangChain/comments/1chqp0r/how_costefficient_is_the_usage_of/) , 2024-05-03-0910
```
I am creating a project where I would like to evaluate a document by running it through a chain. However the documents t
hat I need to evaluate are kinda large, so I am experimenting with introducing the context, i.e. the document(s), outsid
e of the chain itself.  

For this purpose, I have followed much of the documentation from [Memory management | 🦜️🔗 Lang
Chain](https://python.langchain.com/docs/use_cases/chatbots/memory_management/), of course with appropriate modification
s. However, I can not find any solid explanation for how this ChatMessageHistory class is treated by the OpenAI API. I a
m concerned that if I invoke my chain after having added the document to the chat history that the document is counted t
owards the input tokens for each subsequent call of the assistant. 

Does anybody know this? Or does anybody maybe have 
some suggestions to another solution?


```
---

     
 
all -  [ What makes langchain so useful? I'm new to it and don't get it ](https://www.reddit.com/r/LangChain/comments/1chpywv/what_makes_langchain_so_useful_im_new_to_it_and/) , 2024-05-03-0910
```
I'm an experienced engineer and have been doing a lot of work interacting directly with LLM APIs (using simple SDKs). Mu
ltiple people have told me to check out langchain, so I just did a spike on it. I skimmed the docs, I get the core conce
pt of chains and agents. It's cool but this seems like a set of pretty basic abstractions. But I'm scratching my head wo
ndering: what about langchain are people finding most helpful? Given how popular this library is, I feel like I'm missin
g something key...

I'm not trying to be snarky at all. I am assuming that I probably should be using LangChain and it p
robably could be saving me a bunch of time, so I genuinely want to grasp the biggest benefits of it since I don't think 
I'm getting it.

Maybe the core problem is that we all inevitably end up using multiple LLMs eventually (OpenAI, Anthrop
ic, etc) so the biggest benefit of LangChain is that you have a sort of universal SDK — a common interface between all t
he LLMs. Is that the biggest benefit of langchain?
```
---

     
 
all -  [ Help improve the code? ](https://www.reddit.com/r/LangChain/comments/1chp1z9/help_improve_the_code/) , 2024-05-03-0910
```
Any thoughts on how the following code could be improved? It's producing worse results for RAG on Claude3 than when I wa
s using Claude2 with the RetrievalQA class.

Here is the code formatted in Markdown:

# Chain Invoke

```
def get_llm_re
sponse(question, faiss_index, systemPrompt): 
    documents = get_relevant_docs(question, faiss_index)
    chain = promp
t | model | StrOutputParser()
    response = chain.invoke({
        'roleInstructions': systemPrompt,
        'question'
: question,
        'documents': documents
    })
    return response
```

And this is how my RetrievalQA based code use
d to look:

```
qa = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type='stuff',
    retriever=vectorstore_faiss.a
s_retriever(
        search_type='similarity', search_kwargs={'k': 5}
    ),
    return_source_documents=True,
    chain
_type_kwargs={'prompt': PROMPT}
)
```
```
---

     
 
all -  [ create embedding in batch wise using pgvetor langchain  ](https://www.reddit.com/r/LangChain/comments/1chngh6/create_embedding_in_batch_wise_using_pgvetor/) , 2024-05-03-0910
```
     db = PGVector(
             connection_string=conn,
             embedding_function=embeddings,
             collec
tion_name=collection_name,
             
         )
    logs:024-05-01 07:57:01,398 INFO sqlalchemy.engine.Engine [gener
ated in 0.00210s] {'userId_1': 'c4f894f8-70f1-7000-9400-b14372e0af10'}
    batch size None
    why batch size appear non
e can you please in oder to form embedding faster
```
---

     
 
all -  [ Langchain vs LlamaIndex vs CrewAI vs Custom? Which framework to use to build Multi-Agents applicatio ](https://www.reddit.com/r/LocalLLaMA/comments/1chkl62/langchain_vs_llamaindex_vs_crewai_vs_custom_which/) , 2024-05-03-0910
```
Hi, I am trying to build an AI app using multi-agents approach. Right now it's a little confusing as to which framework 
to use. I have done some research on the pros and cons of each framework, and hope to get an final answer today.

Here i
s what I gathered so far:

1. Langchain is heavily abstracted and difficult to use. Sounds like it's not worth the effor
t to learn this framework
2. LlamaIndex received some backlashes as well, but the arguments were vague and I only rememb
er complaints about its immaturity
3. CrewAI uses Langchain underneath the hood. For that reason I am considering passin
g
4. Custom would allow me to learn more about how the models react to raw prompts, which is itself a good learning expe
rience. I won't be subject to restriction of third party frameworks. The downside side is the work effort will bloat up.
 I am favoring this approach
```
---

     
 
all -  [ RAG returns everything ](https://www.reddit.com/r/LangChain/comments/1chkgsc/rag_returns_everything/) , 2024-05-03-0910
```
Im trying to build a conversational RAG with chat history kept in memory.The output gives everything including the conte
xt,prompt template ,question and answer.I just want the answer.  
my code looks like

    conversational_rag_chain = Run
nableWithMessageHistory(
        rag_chain,
        get_session_history,
        input_messages_key='input',
        his
tory_messages_key='chat_history',
        output_messages_key='answer',
    )
      print(query)
      result = conversa
tional_rag_chain.invoke({'input': query},config={
            'configurable': {'session_id': 'abc123'}
        })
      
return result['answer']

    if st.session_state.messages[-1]['role'] != 'assistant':
                  with st.chat_mes
sage('assistant'):
                    with st.spinner('Loading'):
                      answer = qa(question)
         
             st.write(answer)
    
                  new_ai_message = {'role':'assistant','content': answer}
           
       st.session_state.messages.append(new_ai_message)
```
---

     
 
all -  [ Langchain or Semantic Kernel? ](https://www.reddit.com/r/aipromptprogramming/comments/1chka3k/langchain_or_semantic_kernel/) , 2024-05-03-0910
```
I noticed that Microsoft used to officially support Langchain, but now tries to promote semantic kernel instead. Have yo
u already switched (if you are working close to the Azure ecosystem)? I'd rather stick with langchain, but the argument 
may be that semantic kernel better suits the needs of software in our corporate environment.
```
---

     
 
all -  [ ERROR with FAISS VectorSearch ](https://www.reddit.com/r/LLMDevs/comments/1chiqfl/error_with_faiss_vectorsearch/) , 2024-05-03-0910
```
I am trying to build a application using langchain and FAISS as my vector storage. but i m encountering errors with it. 
so can anyone help me out who have a good knowledge of  AI- LANGCHAIN- FAISSS 
```
---

     
 
all -  [ llama2 all good, random characters with llama3 ](https://www.reddit.com/r/LangChain/comments/1chhmsa/llama2_all_good_random_characters_with_llama3/) , 2024-05-03-0910
```
Hi everyone,

with model 'TheBloke/Llama-2-13B-chat-GGUF/llama-2-13b-chat.Q6\_K.gguf' I made quite good experiences loca
lly with langchain, however with model 'FaradayDotDev/llama-3-8b-Instruct-GGUF/llama-3-8b-Instruct.Q8\_0.gguf' or any ot
her llama3 model I simply do not get any valid answers (just lot of newlines and some random numbers or words in the ans
wer).

I tried playing with context size, putting llama3 specific tokens into the prompt like following but nothing help
s:

    llm = LlamaCpp(
        model_path='/Users/aydink/Workspace/models/FaradayDotDev/llama-3-8b-Instruct-GGUF/llama-
3-8b-Instruct.Q8_0.gguf',
        n_gpu_layers=30,
        n_ctx=8128,
        n_threads=4,
        temp=0.0,
        f1
6_kv=True,  
        verbose=True,
    )
    
    # Retrieve and generate using the relevant snippets of the blog.
    r
etriever = vectorstore.as_retriever()

    template_llama3='''<|begin_of_text|><|start_header_id|>system<|end_header_id|
> You are an enthusiastic assistant who likes helping others.
    From the info present in the 'Context Section' below, 
try to
    answer the user's questions. If you are unsure of the answer, reply
    with 'Sorry, I can't help you with th
is question'. If enough data
    is not present in the 'Context Section', reply with 'Sorry, there isn't
    enough data
 to answer your questions <|eot_id|><|start_header_id|>user<|end_header_id|>
        Question: {question} 
        Conte
xt: {context} 
        Answer: <|eot_id|><|start_header_id|>assistant<|end_header_id|>'''
    
    
    custom_rag_promp
t = PromptTemplate(
        input_variables=['context', 'question'],
        template=template_llama3
    )
    
    rag
_chain = (
        {'context': retriever | format_docs, 'question': RunnablePassthrough()}
        | custom_rag_prompt
 
       | llm
        | StrOutputParser()
    )

Is this because I am using an instruct model instead of a chat model (li
ke before with llama2)? But than at least I would expect some semantically more or less correct response.

Any ideas wha
t could cause this?
```
---

     
 
all -  [ Anyone using Deepchecks for RAG Evaluation? ](https://www.reddit.com/r/LangChain/comments/1chf4a1/anyone_using_deepchecks_for_rag_evaluation/) , 2024-05-03-0910
```
Hey everyone,

I'm working on a project that involves Retrieval-Augmented Generation (RAG) models, and I'm looking for w
ays to evaluate them effectively. I came across this tool from Deepchecks that seems promising for RAG evaluation but I 
haven't seen much about it online.

Has anyone here used Deepchecks for RAG evaluation before? I'd love to hear your exp
erience.
```
---

     
 
all -  [ Computer Science Intern with no prior experience ](https://www.reddit.com/r/resumes/comments/1ch1tvs/computer_science_intern_with_no_prior_experience/) , 2024-05-03-0910
```
Hi guys. Im currently a year 2 cs student without any internship experience before. Looking for advice for my first CV =
).

I still have other projects, including :
-restaurant pos system developed in java
-linux gold price tracker 
-haskel
l black box game solver 

Should i switch my current projects withh any from the above? Or should increase to 2 pages fo
r them? 
 Thank you.

https://preview.redd.it/fiu7ucvl7oxc1.jpg?width=1275&format=pjpg&auto=webp&s=79915781fe7e72c9616cc
beb52e1881629b24fea


```
---

     
 
all -  [ need help in creating an AI agent ](https://www.reddit.com/r/LangChain/comments/1ch0t01/need_help_in_creating_an_ai_agent/) , 2024-05-03-0910
```
I am creating a project whose one component is an AI agent parsing a pdf, opening a link given in the pdf and performing
 a specific action. can anyone guide me on how to do this? I cant really find any specific resources online. thank you.
```
---

     
 
MachineLearning -  [ [D] Self-optimizing deterministic LLM memory using dspy, neo4j and vector databases. Need your input ](https://www.reddit.com/r/MachineLearning/comments/1cakjaf/d_selfoptimizing_deterministic_llm_memory_using/) , 2024-05-03-0910
```
Hey there, Redditors!

I'm back with the latest installment on creating deterministic LLM memory.

If you've been follow
ing along, you know I'm on a mission to move beyond the '[thin OpenAI wrapper](https://topoteretes.github.io/cognee/blog
/2023/10/05/going-beyond-langchain--weaviate-and-towards-a-production-ready-modern-data-platform/)' trend and tackle the
 challenges of building robust LLM memory.

  
That's why we built cognee, a python library to process documents and bui
ld knowledge graphs on top of them.

After a few weeks of work, we integrated DSPy and extended cognee.

Here is brief o
verview of the logic: 

[Architecture overview](https://preview.redd.it/fcs3lifx53wc1.png?width=1380&format=png&auto=web
p&s=9316cba52147a5b764565b8438f3f143d8e7ac84)

We aim to understand:

1. Have you tried building knowledge graphs with o
ther tools before?

2. If so, what were the biggest obstacles?

3. How would you approach semantic linking of documents 
without knowledge graphs?

*Remember to give this post an upvote if you found it insightful!*  
*And also star our* [Git
hub repo](https://github.com/topoteretes/cognee)
```
---

     
 
MachineLearning -  [ [D] How to get the source documents from the retrieved context for RAG?  ](https://www.reddit.com/r/MachineLearning/comments/1bvoc1t/d_how_to_get_the_source_documents_from_the/) , 2024-05-03-0910
```
I'm not using Lanchain but only making API calls to an LLM service provider. The retriever is connected to a vector DB, 
and I would like to know what the LLM refers to WITHIN that retrieved context whenever it provides an answer, similar to
 how return_source_documents works in Langchain.

I'm using AzureOpenAI. I couldn't find much in their docs that related
 to returning the source documents. Any help will be greatly appreciated!

```
---

     
 
MachineLearning -  [ [P] RAG pipeline to query the ML Engineering Open Book ](https://www.reddit.com/r/MachineLearning/comments/1bu4wyx/p_rag_pipeline_to_query_the_ml_engineering_open/) , 2024-05-03-0910
```
I built a quick RAG implementation using Langchain to make it easy to query the [ML Engineering Open Book](https://githu
b.com/stas00/ml-engineering) by [Stas Bekman](https://twitter.com/StasBekman). The Multi-Vector retriever gave pretty go
od results and was quite easy to set up too. 

Github link - [https://github.com/shreyansh26/RAG-ML-Engg-Open-Book](http
s://github.com/shreyansh26/RAG-ML-Engg-Open-Book)

Hope this is useful for folks!
```
---

     
 
MachineLearning -  [ [Project] FinancialAdvisorGPT : LLM+RAG Boilerplate Project ](https://www.reddit.com/r/MachineLearning/comments/1btlpgd/project_financialadvisorgpt_llmrag_boilerplate/) , 2024-05-03-0910
```
FinancialAdvisorGPT is a boilerplate project designed for RAG (Retriever-Augmented Generation) and LLM (Large Language M
odel) applications in financial analysis. Built on a technology stack including MongoDB, MongoDB VectorDB, Chroma, FastA
PI, Langchain, and React submodule for UI, it offers a framework for developers to implement and customize RAG+LLM proje
cts. Leveraging parallelized data pipelines, FinancialAdvisorGPT processes and integrates various data sources such as s
tock data, news, SEC filings, and local PDFs.

Github project includes long documentation on how the project is structur
ed, how LLM+RAG works for specific task : [https://github.com/mburaksayici/FinancialAdvisorGPT](https://github.com/mbura
ksayici/FinancialAdvisorGPT)
```
---

     
 
deeplearning -  [ Seeking Advice: Solving Data Challenges with Large Language Models (LLMs) ](https://www.reddit.com/r/deeplearning/comments/1ca4nc1/seeking_advice_solving_data_challenges_with_large/) , 2024-05-03-0910
```
Hi all

I am presented with a problem that I need to solve using LLM to get the right data from text that has only \~20%
 structure to it. Here's a sample data

XXXXX

AA          BB

CCCC:  (optional DDDD)

C1......(A1) (B1)

C2......(A2) (
B2)

C3.....(A3) (B3)

I am required to anwer with either of these results from A1/B1 till A3/B3 pairs but in order to d
o that I need to go back and ask the user which one of the options C1 to C3 applies to him?

The above is not the most c
omplex structure, it increases in complexity from here so a lot of chatting with user is required to get to the right da
ta that will always exist in the chunk like above.

In the most simplist case the data structure will look like below

X
XXXX

AA          BB

CCCC: ......(A1) (B1)



How would you build a system like this? I am looking at multi-agent syste
ms with Langchain, what about prompt chaining?
```
---

     
 
deeplearning -  [ Share the Coolest Out of The Box LLM Applications That Made You Say 'Wow that was smart' ](https://www.reddit.com/r/deeplearning/comments/1c9e6dj/share_the_coolest_out_of_the_box_llm_applications/) , 2024-05-03-0910
```
Hi, I'm looking at some LLM applications today but apart from guys doing big rags with langchain I don't see too many us
es that are out of the box or that make me say 'wow that was smart to use an LLM here'. Have you seen any cool stuff usi
ng LLMs recently that made you say 'wow, that was smart'?
```
---

     
