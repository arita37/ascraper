 
all -  [ Posted here before, no replies. Please roast my resume ](https://i.redd.it/jmjy8eljejcd1.png) , 2024-07-15-0911
```

```
---

     
 
all -  [ Memory Preservation using AI (Beta testing iOS App) ](https://www.reddit.com/r/LangChain/comments/1e37ksf/memory_preservation_using_ai_beta_testing_ios_app/) , 2024-07-15-0911
```
Super excited to share that our iOS app is live for beta testers. In case you want to join please visit us at: [https://
myreflection.ai/](https://myreflection.ai/)

MyReflection is a memory preservation agent on steroids, encompassing image
s, audios, and journals. Imagine interacting with these memories, reminiscing, and exploring them. It's like a mirror al
lowing you to further reflect on your thoughts, ideas, or experiences. Through these memories, we enable our users to cr
eate a digital interactive twin of themselves later on.

This was built keeping user security and privacy on top of our 
list. Please give it a test drive would love to hear your feedback. 
```
---

     
 
all -  [ llamaindex query responses are short ](https://www.reddit.com/r/LlamaIndex/comments/1e33h84/llamaindex_query_responses_are_short/) , 2024-07-15-0911
```
I find llamaindex query responses much shorter than the answer I get from langchain. Especially compared to directly ask
ing questions to chatgpt4o on OpenAI website. What is the reason for this?

        query_engine = vsindex.as_query_engi
ne(
            similarity_top_k=top_k, response_mode=llama_response_mode)  
        answer = query_engine.query(query)

    

  
I played with top\_k to 10 also different response models like refine or tree\_summarize
```
---

     
 
all -  [ Langchain Agent with self query retrieval. ](https://www.reddit.com/r/LangChain/comments/1e32ffw/langchain_agent_with_self_query_retrieval/) , 2024-07-15-0911
```
Has anyone worked on or have any resources regarding using the self query retrieval mechanism with langchain agent and g
ot exact response from agent without any hallucinations or not able get required documents from vectordb like problems.
```
---

     
 
all -  [ Beginner using langchain having some doubts ](https://www.reddit.com/r/LangChain/comments/1e2zh63/beginner_using_langchain_having_some_doubts/) , 2024-07-15-0911
```
I recently started with Python and the project I built first was a simple project based on the rag model. High level is 
I used a book and parsed it , created chunks and stored the embeddings in the chromadb (which is a vector db). 

Based o
n user query finds the most relevant first matching chunk and passes it to llm with this info as context and user query.
 The llm(gemini-pro) generates the response 

Doubt:

Are these type of projects are even good projects as I've just com
pleted my graduation 2 weeks ago in computer science. Does this type of projects are even good for fresher?
What more in
teresting things I should do and how do I measure that the my rag model produces better results compared to directly ask
ing the llm same query. What are the parameters the length,  Grammer or etc of the generated response 

I've just starte
d this and there might be some very basic or dumb doubts from my side. I'm looking for some direction I could go on with
 Gen-ai 
```
---

     
 
all -  [ stupid question : which tool LangChain team use to draw their schema ? ](https://www.reddit.com/r/LangChain/comments/1e2xzbu/stupid_question_which_tool_langchain_team_use_to/) , 2024-07-15-0911
```
Love LangChain schematic, which tool they use ? Do you have any recommandation to draw easily agentic/LLM app architectu
re ?

https://preview.redd.it/905gadmjbgcd1.png?width=2893&format=png&auto=webp&s=dbc2601a5ad8917901a4ab23c88a6095968141
1f


```
---

     
 
all -  [ What would you say the most important concept in langchain is? ](https://www.reddit.com/r/datascience/comments/1e2xscn/what_would_you_say_the_most_important_concept_in/) , 2024-07-15-0911
```
I would like to think it’s chain cause I mean if you want to tailor an llm to your own data we have rag for that
```
---

     
 
all -  [ Do GoogleAPI a requirement for the web research class ? ](https://www.reddit.com/r/LangChain/comments/1e2w4zx/do_googleapi_a_requirement_for_the_web_research/) , 2024-07-15-0911
```
I wrote a custom search tool class which does not use Google, but I am still unable to get the web research functionalit
y to work since it keeps demanding a google api key?

```
---

     
 
all -  [ Why should i keep using langchain? ](https://www.reddit.com/r/LangChain/comments/1e2vx5m/why_should_i_keep_using_langchain/) , 2024-07-15-0911
```
I made a RAG system with Langchain just becasuse a coworker did a POC with it, and i've structured it much better. At th
e moment i use pgvector as vectorstore adding some filter to it based on metadata, pass the document to the stuff chain 
and get a streaming answer.

Now the business requires some new features, like parent document retriever, calculating co
sts, hybrid search/reranking, etc.. that i find very tough using Langchain instead of making all vanilla.

At the moment
 i just place a postgres query, call openAI to rephrase my question and history, and call openAI again to get the answer
. Is nothing that fancy, isn't it?
```
---

     
 
all -  [ Roast my resume,not getting calls for even oa for internships ](https://i.redd.it/3spnw6x35fcd1.jpeg) , 2024-07-15-0911
```
I am looking for ml/data science/data analytics internship since my pre final year has begin. For ml I have doing resear
ch projects in healthcare for quite some time.
I have also qualified Amazon ml summer school and in top 50 out of 1400 i
n amex product track(result is yet to come for last round).I have applied a lot for above mentioned  domains but to no s
ucess till date how can I improve this resume to cater to what is actually needed to atleast receive a call?
```
---

     
 
all -  [ Are vector embeddings / similarity search non-deterministic? ](https://www.reddit.com/r/LangChain/comments/1e2hnoq/are_vector_embeddings_similarity_search/) , 2024-07-15-0911
```
I created some documents to test out the performance of the vector store and embedding, and when using LangChain batch m
ethod to process multiple queries at the same time I get different results even for pretty straightforward queries. I ha
ve two documents each contains info about golf and tennis. The query to the retriever is simply retriever.batch([Tennis,
 Golf]).

The response changes from one call to the next. Sometimes the batch returns content related to only golf or so
metimes only tennis. I thought maybe it’s because the similarity closeness of the sports in vector space so I added a th
ird document with “cats,dogs” etc and randomly the batch method sometimes returns this document as the most relevant. 


Extremely confused. Could it be an issue with the embeddings?

UPDATE: I tried another vector db (Chromadb) instead of W
eaviate and the issue was resolved. 
```
---

     
 
all -  [ Non-relevant questions to the context in chatbot ](https://www.reddit.com/r/LangChain/comments/1e2grkh/nonrelevant_questions_to_the_context_in_chatbot/) , 2024-07-15-0911
```
Hi everyone,

While implementing RAG in a chatbot pipeline, what are the common strategies for dealing with questions th
at are not relevant to the context?  
When asking questions about the context stored in my local DB the retriever gets t
he relevant data and the LLM generates the right answer. However, if I ask questions like 'Who are you', or 'How are you
?' I get hallucinations because the prompt contains under the hood also retrieved context.

I tried specifying in the sy
stem prompt that if the question is not relevant to the context, say I don't know but it didn't help.

Thank you all for
 your help
```
---

     
 
all -  [ What should someone with a MSc Data science degree do? ](https://www.reddit.com/r/developersIndia/comments/1e2cghw/what_should_someone_with_a_msc_data_science/) , 2024-07-15-0911
```
Well, I hold a master's in data science. No BTech. But I've built fullstack projects with django + react, flask, built f
lutter a basic flutter app with dart, used hyped llms for a complete chat bot with RAG using neo4j and langchain. I've a
lso done a lot of analytics as a learner and a freelancer. Did a shitty software job for 4 months and quit because it wa
s pointless. 

What should I do now? Been jobless since Feb end. Upskilled a lot, did a lot, contributing to open-source
 whenever I can. I've started losing hair, can't sleep, distanced myself from everyone because of the stress and anxiety
. Should I focus on something else? I've got 2 offers in the last 4 months (1 for an longterm internship where they make
 you work real projects on yourself with the client with no pay or PPO and 2nd one was similar with no pay and pay is on
ly when the product gets costumers). 

Some people have said I don't have the marketing skills to market my skills. I've
 tried everything and I don't know what I'm missing. My resume is updated every month with the latest project, details a
nd stuff and checked with ATS (always above 70). I send cold mails to every recruiter I can find. Many have said they wo
n't offer a job because of my degree. Only the ones who gave me take-home assessments did interviews with me. Out of tho
se 4 interviews, I got 2 offers and those were basically useless. 


I want to work as a data engineer and I've been hon
ing my skills for that. 


Maybe I'm being desperate. Idk, it's just disappointing. 
```
---

     
 
all -  [ Need help with using Langchain runnables .. ](https://www.reddit.com/r/LangChain/comments/1e2acs1/need_help_with_using_langchain_runnables/) , 2024-07-15-0911
```
Hey everyone,

I am currently working on a project where I need to process nested queries using Langchain. Specifically,
 I have a requirement where an LLM evaluates a rule for example address should contain company name, street name, pin co
de, city name, and state. The outer chain should wait for all the internal chains to process, and then the outer chain s
hould be evaluated.

I have been trying to implement this using Land Chain runnables, but I am facing some challenges in
 getting it to work as expected. Could anyone provide some guidance or examples on how to properly structure the Land Ch
ain runnables to achieve this nested query processing behavior?

Any help, code snippets, or resources would be greatly 
appreciated. Thank you in advance!
```
---

     
 
all -  [ Langgraph: what implementation strategy would you recommend for this case?  ](https://www.reddit.com/r/LangChain/comments/1e276vp/langgraph_what_implementation_strategy_would_you/) , 2024-07-15-0911
```
Hi! I would like to get suggestions on how to implement the following using langgraph:
What i have today: i have a langg
raph workflow containing one 'supervisor' agent and I 2 specialised agents. When the user inputs a request the superviso
r decides what agent to send the work to until it decides the work is finished.
What i want to do now is:
-for one of th
ese agents I want to make it a two step operation. So the agent receives the request and then displays to the user infor
mation about what he is about to do. The user can then give an ok of ask for some tweak. Then the agent finishes the job
. 
Another possibility here is that the agent decides it doesn't has all the info and reaches to the user to ask for add
itional info (in that case he will also reach the user to confirm the operation). 
I imagine I can achieve this with bre
akpoints and collecting human input, but since I've never did it before i am a bit confusing on how the states and workf
low should look like. 
```
---

     
 
all -  [ Full stack Python developers needed ](https://www.reddit.com/r/PythonJobs/comments/1e25xv4/full_stack_python_developers_needed/) , 2024-07-15-0911
```
Howdy,

Recently established startup in Romania, VC backed, we need 3 full stack developers available immediately to acc
elerate the development of a SaaS platform, Azure hosted, powered by AI. Everything in Azure DevOps.

Ideally, someone w
ith good experience in Python, FastAPI, next.js, langchain, llama-index, knowledge of LLMs, Graphrag, Azure app services
/container apps, IaC, RAG pipelines, with great attention to non functional reqs.

Very important, b2b only, preferably 
EU timezone, remote all the time if the day looks approximately like this, 3-5 pushes in production per day, constant im
provements:

11:00. Standup.

11:30. You are participating in a call with a new client who recently started using our pl
atform. It asks about possible additional integrations with other systems. After the call, you draw up a plan for the ne
w functionality — depending on the priority, you might aim for completion on the same day.

14:30. While working, we not
ice that we are encountering an issue that is causing performance issues for some tenants. The whole team mobilizes to i
dentify and solve the problem.

16:00. The new functionality is complete. Push the new code and inform the customer abou
t the new capability.

17:00. Conduct an onboarding call for a new customer, taking notes on the user's reaction to the 
product.
```
---

     
 
all -  [ AI phone calling agent ](https://www.reddit.com/r/LangChain/comments/1e25aed/ai_phone_calling_agent/) , 2024-07-15-0911
```
We are an ai chatbot company,  I am to add a phone calling layer over the chatbot , I am looking for techstack for such 
usecase. I am using python for that. Want everything to be customised, Speech to Text , text to speech.

Currently I am 
to use Twillio. But I want to have full control over speech . To transcribe &etc  i aim to use in house model 


Suggest
 resources.
```
---

     
 
all -  [ SQL Agent to automate querying (LangChain, LlamaIndex, CrewAI) ](https://www.reddit.com/r/Automate/comments/1e23u1r/sql_agent_to_automate_querying_langchain/) , 2024-07-15-0911
```
Hey everyone! 🚀 I’m thrilled to share another exciting project: an SQL Agent to execute SQL queries and document them.


**Objectives**

This project aims to create an intelligent agent capable of interacting with SQL databases to perform qu
eries, log them, and manage data efficiently.

**Implementation Details**

Tools & Frameworks:  
Composio, Langchain, Ll
amaIndex, CrewAI, ChatGPT, Python

Setup:

1. Clone the repo: git clone
2. Navigate to the example: cd composio/python/e
xamples/sql\_agent
3. Install dependencies: pip install -r requirements.txt

**Key Features**

1. SQL Query Execution: A
utomatically run and log SQL commands.
2. Database Management: Seamlessly interact with and manage data in various datab
ases.
3. Agentic Integration: Leverage multiple frameworks for enhanced data processing and query management.
4. Dynamic
 Query Handling: Generate and execute SQL queries based on real-time inputs.
5. Data Analysis: Use built-in functions to
 analyze query results and visualize data.

**Results**

The agent automates database interactions, making data manageme
nt more efficient and less error-prone. It can be integrated into various applications where database interaction is req
uired.

[GitHub Repo](https://git.new/SQLAgent)

Feel free to explore the project, give it a star if you find it useful,
 and let me know your thoughts or suggestions for improvements! 🌟
```
---

     
 
all -  [ Tool calling with Claude 3.5 not working ](https://www.reddit.com/r/LangChain/comments/1e1r8rk/tool_calling_with_claude_35_not_working/) , 2024-07-15-0911
```
Hi, I am building an AI agent with Claude 3.5. My functions are not being invoked by the agent. My understanding was tha
t Langchain automatically calls the agent, but it is not being called. I do, however, am receiving as a model response t
hat function needs to be called. Here's the model response and my code:

    > Entering new AgentExecutor chain...
    c
ontent: Certainly
    content: ,
    content:  ****. I
    content: 'll create
    content:  a new I
    content: **** f
or you
    content:  using
    content:  the available
    content:  function
    content: .
    content: toolu_01G44ahC
crqSaXgiUWrvX85L
    content: None
    [{'text': 'Certainly, *****. I'll create ******* for you using the available func
tion.', 'type': 'text', 'index': 0}, {'id': 'toolu_01G44ahCcrqSaXgiUWrvX85L', 'input': {}, 'name': '*******', 'type': 't
ool_use', 'index': 1, 'partial_json': ''}]
    
    > Finished chain.
    
    
    
    llm_with_tools = llm.bind_tools
(tools)
    agent = (
        {
            'input': lambda x: x['input'],
            'agent_scratchpad': lambda x: for
mat_to_openai_tool_messages(
                x['intermediate_steps']
            ),
            'chat_history': lambda x
: x['chat_history'],
        }
        | prompt
        | llm_with_tools
        | OpenAIToolsAgentOutputParser()
    )

    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
```
---

     
 
all -  [ Want to use langchain or llamaindex of structured data pdf parsing ](https://www.reddit.com/r/LLMDevs/comments/1e1qosr/want_to_use_langchain_or_llamaindex_of_structured/) , 2024-07-15-0911
```
Can any one tell me what would be the cost for parsing semi structured data from PDF table, images and store them in pin
econe .

Both the platforms are openbsource so would this cost me if I use their platform in production.
```
---

     
 
all -  [ Full stack python developer ](https://www.reddit.com/r/programare/comments/1e1qip6/full_stack_python_developer/) , 2024-07-15-0911
```
Salutare,

Startup recent infiintat, VC backed, avem nevoie de 3 full stack developers disponibili imediat pentru a acce
lera dezvoltarea unei platforme SaaS, Azure hosted, powered by AI. Totul in Azure DevOps.

Ideal ar fi cineva cu experie
nta buna pe Python, FastAPI, next.js, langchain, llama-index, cunostiinte despre LLMs, Azure app services/container apps
, IaC, cu atentie mare pe non functional reqs.

Foarte important, b2b only, remote all time daca ziua arata in felul urm
ator, 3-5 push-uri in productie pe zi, imbunatiri constante:

11:00. Standup.

11:30. Participi la un apel cu un client 
nou care a inceput recent sa utilizeze platforma noastra. Te intreaba despre posibile integrari suplimentare cu alte sis
teme. Dupa apel, redactezi un plan pentru noua functionalitate — in functie de prioritate, s-ar putea sa vizezi finaliza
rea in aceeasi zi.

14:30. In timp ce lucram, observam ca intampinam o problema de performanta care cauzeaza probleme de
 performanta pentru unii tenanti. Toata echipa se mobilizeaza pentru a identifica si rezolva problema.

16:00. Noua func
tionalitate este completa. Push la noul cod si informezi clientul despre noua capabilitate.

17:00. Conduci un apel de o
nboarding pentru un nou client, luand notite despre reactia utilizatorului la produs.

17:45. Standup/cina cu echipa. Di
scutam despre viata, stiri, munca etc.

18:30. Seara buna, pe urmatoarea zi!






```
---

     
 
all -  [ Learn till transformers, what is next (towards llm) ? ](https://www.reddit.com/r/learnmachinelearning/comments/1e1mx46/learn_till_transformers_what_is_next_towards_llm/) , 2024-07-15-0911
```
Just finished learning transformers,  ofcourse will code gpt from scratch (Andrej karpaty's). I am going towards llm's a
nd Gen AI applications.


What should I do next ? Read about each llm & architecture ? Learn langchain ? I am very confu
sed different rodmaps say different approach. 

Help me in guiding from your experience and mistakes. 

A flow will help
.


Thanks in advance.
```
---

     
 
all -  [ Please Suggest me better open source model for getting json output (Rag operation).  ](https://www.reddit.com/r/LangChain/comments/1e1jutc/please_suggest_me_better_open_source_model_for/) , 2024-07-15-0911
```
The model is about to extract the data from the pdf based bunch of questions. I tried different quantized model. But eve
ry time I tried i failed to make an output. The model giving me schema it self (jsonoutputparser)  
```
---

     
 
all -  [ Reranker models experience  ](https://www.reddit.com/r/LangChain/comments/1e1i30i/reranker_models_experience/) , 2024-07-15-0911
```
I'm interested in adding reranking in our RAG application (rerank the chunks retrieved from a pinecone index similarity 
search).

We are using models deployed in Azure, mostly OpenAI.
Ive seen Cohere offers a reranking model, but it's not a
vailable in Azure not AWS Bedrock.

Do you know any approach that would be possible with models we could consume as serv
ice (API) on Azure, AWS bedrock or Google Cloud? (we don't have any entreprise relationship with Cohere yet so I think a
ny alternative would be faster to deploy). 

Thanks in advance for any pointer. 
```
---

     
 
all -  [ Asking for specific date range and getting something totally different. What am I doing wrong? ](https://www.reddit.com/r/LangChain/comments/1e1h5c6/asking_for_specific_date_range_and_getting/) , 2024-07-15-0911
```
I need to create an agent that can query a sql database to answer questions. I started playing with agents and function 
calling in langchain. Following the documentation, I put together a very simple code (see below) but it is definitely no
t working as intended. 

I ask a very direct question  
`what is my resource consumption for the past 30 days?`

and it 
invokes my tool with the wrong parameters - see date ranges

`Invoking: \`get_resource_consumption\` with \`{'customer_i
d': 1, 'start_date': '2023-09-21', 'end_date': '2023-10-21'}\``

and each time I run my app, it comes up with a differen
t date range.

what am I doing wrong?

    from langchain_core.tools import tool
    from langchain import hub
    from 
langchain_openai import ChatOpenAI
    from langchain.agents import create_tool_calling_agent
    from langchain_core.pr
ompts import ChatPromptTemplate
    
    llm = ChatOpenAI(model='gpt-4o')
    
    @tool
    def get_resource_consumptio
n(customer_id, start_date, end_date):
        
    '''Get the resource consumption for a specific customer between two d
ates.
    
        Args:
            customer_id: The unique identifier of the customer.
            start_date: The sta
rt date of the period.
            end_date: The end date of the period.
        '''
        return 100
    
    
    to
ols = [get_resource_consumption]
    
    prompt = ChatPromptTemplate.from_messages(
                [
                 
   ('system', 'You are a helpful assistant that helps users with their questions about resource consumption.'),
        
            ('placeholder', '{chat_history}'),
                    ('human', '{input}'),
                    ('placehold
er', '{agent_scratchpad}'),
                ]
            )
    prompt.pretty_print()
    
    agent = create_tool_calli
ng_agent(llm, tools, prompt)
    
    from langchain.agents import AgentExecutor
    
    agent_executor = AgentExecutor
(agent=agent, tools=tools, verbose=True)
    
    agent_executor.invoke({'input': 'what is my resource consumption for t
he past 30 days? customer_id = 1'})
    
    
```
---

     
 
all -  [ Chatbot is not able to remember the context, can't retain it's memory ](https://www.reddit.com/r/learnmachinelearning/comments/1e1gl5b/chatbot_is_not_able_to_remember_the_context_cant/) , 2024-07-15-0911
```
Here's the code, plz correct this:

    import streamlit as st
    from langchain_community.llms import Ollama
    from 
langchain.prompts import ChatPromptTemplate
    from langchain_core.output_parsers import StrOutputParser
    from langc
hain.memory import ConversationBufferMemory
    from langchain.chains import ConversationChain
    
    # Initialize Oll
ama LLM
    llm = Ollama(model='llama3')
    
    # Initialize memory
    memory = ConversationBufferMemory(return_messa
ges=True)
    
    # Initialize ConversationChain
    conversation = ConversationChain(
        llm=llm,
        memory=
memory,
        verbose=True
    )
    
    # Streamlit app
    st.title('Chatbot with Ollama LLAMA 3')
    
    # Initi
alize chat history
    if 'messages' not in st.session_state:
        st.session_state.messages = []
    
    # Display 
chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(messa
ge['role']):
            st.markdown(message['content'])
    
    # React to user input
    if user_input := st.chat_inp
ut('What is your question?'):
        # Display user message in chat message container
        st.chat_message('user').m
arkdown(user_input)
        
        # Add user message to chat history
        st.session_state.messages.append({'role'
: 'user', 'content': user_input})
    
        # Get bot response
        response = conversation.predict(input=user_inp
ut)
    
        # Display assistant response in chat message container
        with st.chat_message('assistant'):
     
       st.markdown(response)
        
        # Add assistant response to chat history
        st.session_state.messages
.append({'role': 'assistant', 'content': response})
```
---

     
 
all -  [ how to pass thread_id using config when serving langgraph(with checkpointer) through langgserve chai ](https://www.reddit.com/r/LangChain/comments/1e1d466/how_to_pass_thread_id_using_config_when_serving/) , 2024-07-15-0911
```
I'm having error when using checkpointer in graph.



| ValueError: Checkpointer requires one or more of the following '
configurable' keys: \['thread\_id', 'thread\_ts'\]

.





How to pass configuration with thread\_id here to graph?






add\_routes(

app,

(graph | RunnableLambda(output\_parsing\_for\_playground)).with\_types(input\_type=InputChat, outpu
t\_type=str),

playground\_type='chat'

)


```
---

     
 
all -  [ Retrieve Chunks which are not similar but still relevant ](https://www.reddit.com/r/LangChain/comments/1e1cdhp/retrieve_chunks_which_are_not_similar_but_still/) , 2024-07-15-0911
```
Hello dear swarm intelligence practitioner! I have come to you in a time of great need.

Imagine you have a document abo
ut some topic. Lets say the GoldenGate Bridge. And this document has multiple wonderfully written paragraphs about this 
Bridge. This includes materials used, the timeframe of when it was built, and much much more.  
This document then goes 
on writing about California and San Francisco.

A few paragraphs down maybe a few sentences about the pacific ocean.

An
d last but not least this: 'It was designed by Joseph Strauss with the help of architect Irving Morrow and engineers Cha
rles Alton Ellis and Leon Moisseiff. Construction was carried out by the McClintic-Marshall Construction Company, a subs
idiary of Bethlehem Steel Corporation.'

This article is chunked using common techniques and embedded into a vector inde
x. Now, this RAG System will be used to answer Questions. We retrieve k docs from this index that are similar to the que
ry, and rerank them to top\_k documents to generate an answer. This pipeline works with almost all queries and documents
.

The problem here would be to answer the question '**Who built the Golden Gate Bridge?'**.

The retrieval process woul
d find these chunks, and confidently (and correctly) rank them as the most relevant for our question. However, the chunk
 with the information we are actually looking for will not be retrieved, as it is not at all similar to the query.

How 
can this question be answered, while maintaining performance?

1. When finding a high scoring chunk (e.g: Golden Gate Br
idge chunk from the top of the article) we fetch the document in its entirety, and **provide the entire article** to the
 generator LLM. Problem here is, that we have to either make a decision to do that based on the query, or do it every ti
me. Both are compromises I want to avoid.
2. **Bigger chunks** would include the information. Problem here is, that we c
an't really generalize. What if there is more content in between? This won't work as reliably as I would like.
3. **Summ
arize chunks** to make them smaller and be able to fit all of the context into the generator LLM. This has the same prob
lem as Approach 1, about making a decision to instead of just going with the chunk to answer the query, we do the extra 
step of retrieving the entire article instead of(or its summary) before returning from the retrieval pipeline.
4. Use a 
**LLM as a Reranker**. This LLM-Reranker would (hopefully) understand to return the relevant chunk (Joseph Strauss), ins
tead of the similar chunks (Golden Gate Bridge). This would again imply, that we have this decision making process based
 on which Reranker should be applied.

Things that could help, but also don't really work in a more general approach:

*
 **Hybrid Retrieval**: Embedding and Keywordbased retrieval will still most likely not find the relevant chunk. And even
 if, the Reranking process would drop it again.
* **Using NER/POS/TF-IDF keywords** alongside the text chunks seems do r
un into similar problems
* **Query Expansion and Reformulation**: Similar Problem as above. Also I have tried this appro
ach and including the Augmented Queries in the Rerank step results in other QA-Tasks to perform worse. IMO only the orig
inal query should be involved in reranking. I use LLM-Generated Queries for SimilaritySearch already, but then rerank th
ose results with the original query.
* **Two Stage Retrieval**: Retrieve GoldenGate chunks -> get all chunks of this art
icle -> find relevant chunks from this preselection of article-chunks. How can we do the last step without involving a s
low LLM and also deciding to go into this TwoStage retrieval in the first place?
* **Different Chunk Size**? Would proba
bly work, but what if the document is just a little bit longer, and again we have the information in another chunk that 
the Bridge-Chunk? Doesn't generalize well.

In the current pipeline, even if the relevant chunk (Joseph Strauss) would a
ppear in the retrieved chunks, lets say via hybrid-search using BM25, keyword matching or other strategies, this chunk w
ould be dropped by the Reranker, because it is not similar to the query.

In conclusion, all approaches I can think of, 
include some sort of LLM to make a decision before returning the chunks to the generatorLLM and/or another decision base
d on all chunks of this article.

What are other approaches one could apply here? What is a best practice? How do others
 handle this problem?

I am looking for an approach that is robust and fast enough to work in a production grade system.
 Ideally some sort of transformer model similar to a reranker, that instead of returning similar matches it returns rele
vant matches.

No matter how similar all our chunks are to the Golden Gate Bridge and SanFrancisco and the pacific, the 
actual desired chunk is not similar. How can we handle this?



**This approach seems the most promising to me, but also
 seems like a really daunting task?**

Train a model to distinguish between 'similar' and 'relevant' content using contr
astive learning techniques.

* Create training pairs that include similar but irrelevant chunks as negative examples, an
d dissimilar but relevant chunks as positive examples.
```
---

     
 
all -  [ RAG for real-time data (SQL) ](https://www.reddit.com/r/LangChain/comments/1e1ba2l/rag_for_realtime_data_sql/) , 2024-07-15-0911
```
Is there any chance of building RAG for real-time data that was stored in SQL databases. Specifically, can we use Unstru
ctured there?
```
---

     
 
all -  [ Search a long document  ](https://www.reddit.com/r/LangChain/comments/1e1aziw/search_a_long_document/) , 2024-07-15-0911
```
I am working on a project where I need to extract information of a very long document.  
Using a local LLM (gemma2) thro
ugh ollama.

If using a vector store, Is there a way I can make sure my LLM query searches all pages or chunks of the ve
ctor store?

Is it perhaps, better to use brute force and do chunks of the text to pass the LLM the compile the results?
 

Any relevant information on this would be much appreciated. Many thanks
```
---

     
 
all -  [ ReAct Prompting ](https://www.reddit.com/r/LangChain/comments/1e1av5p/react_prompting/) , 2024-07-15-0911
```
My LLM is hallaucinating when I ask it a very simple question  
using Langchain tools, here wikipedia.  
I am using gemi
ni-1.5-flash  
tried llama 70b and gemini pro  
but still it hallucinates if not same but easy questions.  
I am using R
eact Prompt Template  
which goes like (2nd image)

My LLM doesn't even reach the observation step it starts hallucinati
ng after action Input  
I tried even changing params of my tools by changing the max\_retrieval etc...  
Please help...


https://preview.redd.it/gmrydfxw81cd1.png?width=1614&format=png&auto=webp&s=9df61fc7f740dab11233da781e3740a871274a9a

h
ttps://preview.redd.it/ohj4e34a91cd1.png?width=1145&format=png&auto=webp&s=966fb6707cf3e9183aa52b093f29f42c0c2192b4




```
---

     
 
all -  [ Approach to build my chatbot using users' custom structured data? ](https://www.reddit.com/r/learnmachinelearning/comments/1e19t0g/approach_to_build_my_chatbot_using_users_custom/) , 2024-07-15-0911
```
It's for a personal project, the chatbot's purpose would be to answer questions about an user's business (e.g. products,
 discounts, offices).

The user should be able to create custom fields for each collection (e.g. product-color, office-n
um\_bathrooms) using mongoDB.

And the chatbot could then answer questions like: 'What color is the product X?' - 'Answe
r: The t-shirt is red'

I was reading about RAG and vector embeddings but I am not sure how I could implement that since
 I am not using PDF or text documents.

**One possible approach** would be to create the vector embeddings for the custo
m fields adding some extra context, so if I an user created a new product, I'd store something like:

    {
      name: 
't-shirt', // embedded text: 'product name t-shirt; description high quality',
      description: 'high quality',
      
custom_fields: [
        {
          color: 'red', // embedded text: 'product name t-shirt; color red'
        },
      
],
    }

Then, I could find the most appropriate answer for a question such as:

* 'What color is the t-shirt?' -> 'pro
duct name t-shirt; color red
* 'Describe the t-shirt' -> 'product name t-shirt; description high quality'

And finally u
se an LLM to create a better answer using the correct context.

**Another approach** could use a knowledge graph (neo4j)
. But I've noticed that the embeddings generated by this code, only embed the attributes of the nodes ('name' in this ex
ample) but it doesn't embed the relations of the node, so I'd end up embedding something like 'name: t-shirt', which isn
't too useful.

    from langchain_community.vectorstores.neo4j_vector import Neo4jVector
    vector_index = Neo4jVector
.from_existing_graph(
            embedding=embedding,
            url=url,
            username=username,
            p
assword=password,
            index_name=index_name,
            node_label='Clothing',
            text_node_properties
=['name'],
            embedding_node_property='embedding',
        )

**A final alternative** could be to use an LLM to
 generate a Cypher (or mongoDB) query with a representation of the graph or schema, but I'd rather use a NLP technique t
o reduce costs and latency.

Does my first approach make sense? What would you recommend?
```
---

     
 
all -  [ Mlops or LLM? ](https://www.reddit.com/r/MLQuestions/comments/1e193s1/mlops_or_llm/) , 2024-07-15-0911
```
Hello! I am working as a data scientist and want to advance my career. My skills include Power BI/Tableau, SQL, Python, 
Pandas, Numpy, and ML model development.

I am deciding between pursuing MLOps or LLM App development and need some advi
ce:

MLOps:
- I have basic knowledge in FastAPI, Flask, Git, Github Actions and AWS.
- I tend to get overwhelmed (partic
ularly the tools) when trying to build end-to-end MLOps projects.

LLM App Development:
- I am learning to build and eva
luate Retrieval-Augmented Generation (RAG) using LangChain and LlamaIndex, which are current trends in AI.
- I skipped s
ome foundational deep learning topics like RNN, LSTM, and Transformers, and jumped straight into GenAI, LLM, and RAG, so
 I’m unsure if I’m on the right track.

Can anyone share advice and recommendations on which path I should pursue?

Than
k you!
```
---

     
 
all -  [ I can't seem to understand langchain API use. Please help. ](https://www.reddit.com/r/learnpython/comments/1e18syu/i_cant_seem_to_understand_langchain_api_use/) , 2024-07-15-0911
```
Please suggest me some resources that i can understand langchain, I tried reading docs for them but my program keep gett
ing error. When I solve one bug it gets another, it has been like that for 2 days. 
```
---

     
 
all -  [ First Chatbot Design ](https://www.reddit.com/r/LearningAIChatbot/comments/1e12qhm/first_chatbot_design/) , 2024-07-15-0911
```
As the title suggets, I am attempting to make my first chatbot ever for a school project. I have done some research and 
am thinking of using LangChain with a Jupyter notebook. I want this chatbot to be able to run outside my environment in 
VSCode as well, whether that be an application or website. I also need to design a UI in Figma and convert this into HTM
L/CSS to be the face of the chatbot. Any resource recommendations, tutorials, or advice is greatly appreciated. Or if yo
u think there is a better way of going about this please let me know below.
```
---

     
 
all -  [ What embedding model is everyone using? ](https://www.reddit.com/r/LangChain/comments/1e11luo/what_embedding_model_is_everyone_using/) , 2024-07-15-0911
```
I was wondering what embedding model people have had success with for their vector store? I might be wrong but on langch
ain it simply implies everyone uses the openai one. Are there options for this?
```
---

     
 
all -  [ Hallucinations: Why You Should Care as an AI Developer ](https://www.reddit.com/r/pythia/comments/1e0z4jy/hallucinations_why_you_should_care_as_an_ai/) , 2024-07-15-0911
```
https://preview.redd.it/64btbssbcybd1.png?width=2048&format=png&auto=webp&s=050dff23beaa0e475cab8917ee5dd14e7dfb9ae9

*U
nderstand why hallucination detection is important for reliable LLMs. Learn the characteristics of a good hallucination 
detector.*

From speech recognition to text generation, generative AI and LLMs have become involved in various applicati
ons and scenarios. The generative AI industry is projected to become a $1.3 Trillion market by 2032, with a compound ann
ual growth rate (CAGR) of 42%. Generative AI products are predicted to add about $289 billion of new revenue to the soft
ware industry.

These projections for expansion reflect the presence of LLMs in all aspects of life, including healthcar
e. Their pervasive presence emphasizes the need for reliable AI to protect end-users from misleading decisions. However,
 LLMs often produce hallucinated outputs, resulting in penalties, lost trust in AI, reputation damage, and human life.


Let’s explore the need for AI reliability and how to achieve reliable AI solutions.

# Why Does AI Reliability Matter?


Though LLMs have become increasingly intelligent, they still tend to hallucinate. AI hallucinations are AI-generated out
puts that seem confident but are inaccurate and misleading.

Industry-leading LLMs like ChatGPT have a 31% hallucination
 rate when used for scientific purposes. These hallucinations have significant costs, including:

* **Healthcare costs:*
* Misdiagnoses can lead to deaths and serious disabilities. It can also cost healthcare providers significant losses in 
penalties and reputation damage.
* **Litigation costs:** AI hallucinations can cause legal penalties in cases such as pr
ivacy violations or sensitive remarks. Legal errors can average $250,000 in settlements.
* **Financial sector:** When LL
Ms are used for research purposes, hallucinations can guide researchers toward poor decision-making. Poor investment dec
isions can lead to millions in losses.
* **Operational downtime:** Erroneous or misleading information can lead to disru
ptions or failures in operational processes. AI-related downtime can cost $10,000 per hour.
* **Brand damage:** Misleadi
ng outputs can damage a company's reputation and result in client hostility.

Governments and NGOs are becoming involved
 in achieving reliable AI. For example, the EU AI Act is a European regulation on AI protection that covers various aspe
cts of AI development and deployment to ensure safe AI.

Complying with these regulations requires the development of re
liableLLMs that produce reliable outputs.

# Existing AI Reliability Solutions and Their Challenges

Existing AI reliabi
lity solutions include bias detection, explainable AI (XAI) methods, adversarial techniques, etc. These solutions detect
 hallucinations and ensure reliable AI to some extent, but their limitations keep them from achieving safe and accurate 
AI.

They lack continuous monitoring support, transparency, and claim verification, which gives rise to their limitation
s, including:

1. **Limited scalability:** Current methods depend on the availability of high-quality training data, whi
ch prevents them from offering scalable AI reliability solutions.
2. **Lack of explainability:** Current methods fail to
 explain why a particular LLM response is flagged as a hallucination, making it difficult for developers to fix factual 
issues.
3. **Low accuracy:** Existing solutions are not as accurate, making them ineffective for mission-critical applic
ations like life sciences.

# 10 Things to Look for in an AI Reliability Solution

AI reliability solutions must meet ce
rtain criteria to effectively detect hallucinations and offer transparency in their decisions. Here are the ten key thin
gs to look for in an AI reliability solution:

# 1. LLM Usage Scenarios

An AI reliability solution should accommodate d
ifferent LLM usage scenarios. The three LLM usage scenarios include:

1. **Zero context:** The AI reliability solution s
hould be able to directly compare references it finds with the LLM’s responses to assess accuracy.
2. **Noisy context:**
 When a question includes some context but is either noisy or incomplete, the AI reliability solution must be capable of
 consulting authoritative data before the LLM generates a response.
3. **Accurate context:** When the context is complet
e and reliable, it can use the references to provide a comprehensive summary or information in response.

[LLM usage sce
narios](https://preview.redd.it/iws0jnex8vbd1.png?width=2880&format=png&auto=webp&s=1b7e2fd50a37a4e82735bdd06619f35dccbb
4066)

These scenarios/ contexts guide the reliability solution in finding references and verifying LLM claims.

# 2. Cl
aim Extraction

The hallucination detection solutions should be able to decompose LLM responses into knowledge triplets.
 Unlike traditional methods, knowledge triplets extract granular details from content and highlight the relationship amo
ng words within a sentence.

Knowledge triplets represent **<subject, predicate, object>**, highlighting the connection 
between the three and creating a better contextual understanding. For example:

[Knowledge Triplet Example](https://prev
iew.redd.it/mvzxmp319vbd1.png?width=2352&format=png&auto=webp&s=5d357b26bf3f7170136c18755ba5300c02a17865)

# 3. Claim Ca
tegorization

After the claim extraction from LLM responses and references/ knowledge base, the hallucination detector m
ust be able to categorize them based on their hallucination levels. Claim categorization guides developers toward the im
provement of LLM by offering insights into its capabilities. The four categories for claim categorization include:

1. *
*Entailment:** Claims in both response and references, indicating accurate outputs.
2. **Contradiction:** Claims present
 in LLM responses but disregarded by references.
3. **Missing facts:** Claims present in references but absent in LLM re
sponses, representing gaps in LLM responses.
4. **Neutral:** Claims present in LLM response but are neither contradicted
 nor confirmed by the references.

[Claim categorization based on hallucination level](https://preview.redd.it/n57d4dh39
vbd1.png?width=1798&format=png&auto=webp&s=51b4161dc45f7dc7c17bedb82d1587eafe0d5df2)

# 4. Accuracy Metrics

An AI monit
oring tool must be able to calculate the overall accuracy of LLM based on claim categorization. The accuracy metric repr
esents the proportion of factually correct claims in the LLM response. Mathematically, accuracy is measured as:

https:/
/preview.redd.it/9dkux1979vbd1.png?width=2780&format=png&auto=webp&s=41a63d1930d462cf8497831112191e2e6df0e628

Where:

*
 Entailment: Claims flagged as Entailment
* Contradiction: Claims flagged as Contradiction
* Reliability: Calculated usi
ng external data (i.e., knowledge graphs or RAGs)

# 5. Task Specific Metrics

There are two types of task-specific metr
ics, i.e., Core metrics specialized to the task and additional metrics for measuring the quality of the responses with r
espect to the task.

Specializing core metrics rely on the type of AI checker being used:

1. LLM-based checkers can enh
ance their accuracy by considering additional context provided in the form of a question when generating claim classific
ation.
2. NLI-based checkers utilize a QA (Question Answering) evaluator model to verify the alignment of a response wit
h a question.
3. Knowledge graph-based checkers rely on Knowledge Graphs (KGs) to verify structured information about en
tities, relationships, and concepts.

https://preview.redd.it/7kjj902d9vbd1.png?width=1436&format=png&auto=webp&s=ff9cd0
af3478d8f36b2aeaaa8a675934a68d668d

# 6. Systematic Error

The AI hallucination detector must be able to identify system
atic errors. Systematic errors are recurring inconsistencies in LLM responses. Identifying them involves:

1. Comparing 
the reference information to itself. This means using the same reference as the knowledge base and the standard for comp
arison.
2. Generating core metrics to assess LLM performance. Metrics highlight the system's ability to classify claims 
as true, false, or neutral correctly.
3. Defining a systematic error checker, which is the harmonic mean of the compleme
nt of Entailment and Contradiction.

The ideal result is 100% Entailment, 0% Contradiction, and 0% Neutral claims. Mathe
matically, a systematic error checker is represented as:

https://preview.redd.it/871dqk9j9vbd1.png?width=1962&format=pn
g&auto=webp&s=c3453f014e83b6c7ff0439b15199b2ebf3ea6ead

# 7. Robust Set of Validators

An AI reliability solution should
 use a robust set of input/ output validators to protect sensitive information from leakage, misleading outputs, and tox
ic outputs. These validators validate LLM inputs and responses to ensure they meet quality standards and are accurate. T
he validators also protect against cyber attacks such as malicious input or prompt injections.

[Example Input\/Output V
alidators](https://preview.redd.it/hdgv807m9vbd1.png?width=2058&format=png&auto=webp&s=fd786a3c48737ac62e6e943598e6bee12
79ca1e0)

# 8. Reporting

A good hallucination detection solution provides reports highlighting hallucination trends ove
r time. These reports give insight into model improvement with time and systematic errors. Updated reports allow targete
d adjustments to enhance the LLM’s reliability and effectiveness.

Moreover, detailed analysis of these trends helps und
erstand the underlying causes of hallucinations, resulting in better training and fine-tuning.

# 9. Continuous Alerting
 and Monitoring

Continuous monitoring and alerting are crucial for real-time hallucination detection and on-time correc
tion. Continuous monitoring keeps track of LLM outputs against each user query, highlighting a model’s strengths and wea
knesses. Alerting systems send email/SMS notifications about LLM performance, which helps address bias in model outputs 
before it perpetuates bias in the public.

[Real-time Monitoring and Alert Rules Example](https://preview.redd.it/iikmvy
ks9vbd1.png?width=2852&format=png&auto=webp&s=e369d8975793f59e21d955581e6d84b136b0c8e8)

# 10. LangChain Integration

La
ngChain is a Natural Language Processing (NLP) framework that provides pre-trained models and tools to customize and imp
rove model performance. LangChain has an active community, and LLM developers use it to develop robust LLMs because of i
ts flexibility and support. The ability of an AI reliability solution to integrate with LangChain makes it a handy choic
e for hallucination detection, as most of the LLM workflows are built using LangChain.

[LangChain Workflow with AI Reli
ability Solution](https://preview.redd.it/lyeikorw9vbd1.png?width=2684&format=png&auto=webp&s=53db6572ce38efa43f837b498c
5d5091cc47e0d8)

# Wisecube’s Pythia: a Reliable Hallucination Detection Tool

Wisecube’s [Pythia](https://askpythia.ai/
blog/introducing-pythia-the-ai-oracle-eradicating-llm-hallucinations), an AI reliability solution, boasts the ten crucia
l characteristics of AI hallucination detectors. These characteristics set Pythia apart from other solutions by offering
 the following benefits:

* **Enhanced reliability:** Reduces the risk of AI errors using built-in hallucination detecti
on and validators
* **Trustworthy outputs:** Builds trust in AI systems through continuously monitoring accurate and rel
iable outputs.
* **Easy integration:** Integrates into existing LangChain workflows, empowering developers to develop tr
ustworthy AI systems.
* **Customizable detection:** Pythia can be configured to suit specific use cases, resulting in im
proved flexibility and increased accuracy.

**To learn more about the impact of hallucinations and the characteristics o
f an effective AI reliability solution,** [**watch the webinar here.** ](https://www.youtube.com/watch?v=PXFXKMJO9jo&t=2
0s)

*The article was originally published on* [Pythia's website.](https://askpythia.ai/blog/hallucinations-why-you-shou
ld-care-as-an-ai-developer)
```
---

     
 
all -  [ AI agents. Are no-code platforms better? ](https://www.reddit.com/r/LangChain/comments/1e0xdgw/ai_agents_are_nocode_platforms_better/) , 2024-07-15-0911
```
On one hand I really want to build from the ground up and see what happens every step of the way, on the other hand, I’m
 trying to embrace abstraction, l would just go for a no-code drag and drop if the final product works fine. I have been
 looking into [~SmythOS~](https://smythos.com/), a no code platform for creating AI agents and I think I am sold. But I 
still can’t shake the feeling that it’s too good to be true. What do you think? Would you go for a no code option or wou
ld you rather just do everything yourself?


```
---

     
 
all -  [ A List of free Courses from Coursera for Computer Science Students. ](https://www.reddit.com/r/coursera/comments/1e0wjdf/a_list_of_free_courses_from_coursera_for_computer/) , 2024-07-15-0911
```
You might check out some free courses courses on Programming, Data Structure, Algorithms, Computer Architecture, Embedde
d Systems and IoT. [Main Article](https://medium.com/p/f10816891ad1).  

1. Introduction to Machine Learning By Duke Uni
versity
2. Data Science Math Skills By Duke University
3. Learn to Program: The Fundamentals(Python)
4. Building Systems
 with the ChatGPT API by Andrew Ng
5. Learn Kali Linux
6. Introduction to Statistics By Stanford University
7. ChatGPT P
rompt Engineering for Developers
8. LangChain Chat with Your Data By [DeepLearning.AI](http://deeplearning.ai/)
9. Intro
duction to Generative AI
10. Preparation for Job Interviews(Guided Project)
11. Use SurveyMonkey to Create a Survey and 
Analyze Results
12. Deep Learning with PyTorch : Image Segmentation(Guided Project)
13. AWS S3 Basics (Guided Project)
```
---

     
 
all -  [  A List of free courses from Coursera.  ](https://www.reddit.com/r/udemyfreebies/comments/1e0uzmo/a_list_of_free_courses_from_coursera/) , 2024-07-15-0911
```
Free Online Courses from Reputed Universities on Programming, Data Structure, Algorithms, Computer Architecture, Embedde
d Systems and IoT. [Read More](http://cse.mx-router-ii.com/l/free-coursera-courses-on-computer-science).

1. Introductio
n to Machine Learning By Duke University
2. Data Science Math Skills By Duke University
3. Learn to Program: The Fundame
ntals(Python)
4. Building Systems with the ChatGPT API by Andrew Ng
5. Learn Kali Linux
6. Introduction to Statistics By
 Stanford University
7. ChatGPT Prompt Engineering for Developers
8. LangChain Chat with Your Data By [DeepLearning.AI](
http://DeepLearning.AI)
9. Introduction to Generative AI
10. Preparation for Job Interviews(Guided Project)
11. Use Surv
eyMonkey to Create a Survey and Analyze Results
12. Deep Learning with PyTorch : Image Segmentation(Guided Project)
13. 
AWS S3 Basics (Guided Project)
```
---

     
 
all -  [ CV roasting ](https://i.redd.it/mpvo0e0f8xbd1.jpeg) , 2024-07-15-0911
```
I applied to hundreds of job ads about data science in London and some remote but hardly getting any friction. Any recom
mendations?
```
---

     
 
MachineLearning -  [ [D] Is Anyone Else Setting Up Real-Time Django Workers for their AI Application? What's the best way ](https://www.reddit.com/r/MachineLearning/comments/1e0qens/d_is_anyone_else_setting_up_realtime_django/) , 2024-07-15-0911
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

     
 
MachineLearning -  [ [P] Real Time AI Workers Web Application ](https://www.reddit.com/r/MachineLearning/comments/1dzryk9/p_real_time_ai_workers_web_application/) , 2024-07-15-0911
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

     
 
MachineLearning -  [ [P] Seeking Feedback on My GenAI Job Fit Project - New to LangChain/LangGraph ](https://www.reddit.com/r/MachineLearning/comments/1dgns9p/p_seeking_feedback_on_my_genai_job_fit_project/) , 2024-07-15-0911
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

     
 
deeplearning -  [ Llama 3 not running on GPU ](https://www.reddit.com/r/deeplearning/comments/1dptxsr/llama_3_not_running_on_gpu/) , 2024-07-15-0911
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

     
 
deeplearning -  [ What is ReAct Prompting? the most important piece in agentic frameworks ](https://www.reddit.com/gallery/1djk4nk) , 2024-07-15-0911
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

     
