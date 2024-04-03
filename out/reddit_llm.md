 
all -  [ Gemini function calling  ](https://www.reddit.com/r/LangChain/comments/1bu9j1u/gemini_function_calling/) , 2024-04-03-0910
```
I want to use function calling with Gemini, I checked Vertex ai documentation and tutorials but they are a bit confusing
 and mess. Anyone have worked with Gemini function calling with Langchain before?
```
---

     
 
all -  [ Does anyone have a digital copy of the book Transformers for natural language processing and compute ](https://www.reddit.com/r/LangChain/comments/1bu8kmc/does_anyone_have_a_digital_copy_of_the_book/) , 2024-04-03-0910
```

```
---

     
 
all -  [ Advanced RAG with Document Intelligence  ](https://www.reddit.com/r/Azure_AI_Cognitive/comments/1bu5l7l/advanced_rag_with_document_intelligence/) , 2024-04-03-0910
```
Has anyone used Azure Document intelligence for capturing metadata in PDFs with tables, figures? How can we create seman
tic chunks using a Qdrant database using Azure Document intelligence to extract data? How can add relevant metadata to m
eaningful chunks? Any other tips to create an advanced RAG pipeline? What are evaluations methods available? Currently u
sing Langchain framework, and I know they support Document Intelligence as one of the document loaders.
```
---

     
 
all -  [ Advanced RAG for PDFs with tables and figures, capturing metadata , Azure Document Intelligent  ](https://www.reddit.com/r/LangChain/comments/1bu5hyt/advanced_rag_for_pdfs_with_tables_and_figures/) , 2024-04-03-0910
```
Has anyone used Azure Document intelligence for capturing metadata in PDFs with tables, figures? How can we create seman
tic chunks using a Qdrant database using Azure Document intelligence to extract data? How can add relevant metadata to m
eaningful chunks? Any other tips to create an advanced RAG pipeline? What are evaluations methods available?
```
---

     
 
all -  [ Prefilter documents before similaritysearch ](https://www.reddit.com/r/LangChain/comments/1bu5dqs/prefilter_documents_before_similaritysearch/) , 2024-04-03-0910
```
I'm using a langchain script in order to make a similarity search of a query embedding in an embedding's MongoDb collect
ion but I want to pre filter the documents to search only in the documents that are $in an objectId array.

    // Get t
he list of embeddings _ids to preFilter
    const documentData =  await documentCollection.findOne(
      { '_id': docum
entId },
      { 'embededings': 1 }
    )
    const documentEmbeddingsId = documentData.embeddings
    
    
    
    //
 Embed query
    const query = 'What is this document about?'
    const embeddings = new OpenAIEmbeddings({
      modelN
ame:'XXX',
      openAIApiKey: 'XXX'
    })
    const embeddedQuery = await embeddings.embedQuery(query)
    
    
    

    // Similarity search
    const vectorStore = new MongoDBAtlasVectorSearch(embeddings, {
      collection,
      inde
xName: 'XXX',
      textKey: 'XXX', 
      embeddingKey: 'XXX', 
    });
    const preFilter = {
      preFilter: {
    
    _id: {
          $in: documentEmbeddingsId
        },
      },
    }
    const storingResponse = await vectorStore.s
imilaritySearchVectorWithScore(embeddedQuery,4,preFilter)
    

Running this code returns this error:

'Error: MongoServ
erError: Operand type is not supported for $vectorSearch: objectId'.

Is the error in the preFilter? Or is this type of 
filter not supported by mongodb? Any ideas on how I can make this search? The documentEmbeddings array has ObjectId type
. If I try to instead give a string array I get the following error: Error: MongoServerError: PlanExecutor error during 
aggregation :: caused by :: Path '\_id' needs to be indexed as token
```
---

     
 
all -  [ Multi-Agent Orchestration playlist ](https://www.reddit.com/r/LangChain/comments/1bu50s6/multiagent_orchestration_playlist/) , 2024-04-03-0910
```
Checkout this playlist around Multi-Agent Orchestration that covers
1. What is Multi-Agent Orchestration?
2. Beginners g
uide for Autogen, CrewAI and LangGraph
3. Debate application between 2 agents using LangGraph
4. Multi-Agent chat using 
Autogen
5. AI tech team using CrewAI
6. Autogen using HuggingFace and local LLMs

https://youtube.com/playlist?list=PLnH
2pfPCPZsKhlUSP39nRzLkfvi_FhDdD&si=B3yPIIz7rRxdZ5aU
```
---

     
 
all -  [ [P] RAG pipeline to query the ML Engineering Open Book ](https://www.reddit.com/r/MachineLearning/comments/1bu4wyx/p_rag_pipeline_to_query_the_ml_engineering_open/) , 2024-04-03-0910
```
I built a quick RAG implementation using Langchain to make it easy to query the [ML Engineering Open Book](https://githu
b.com/stas00/ml-engineering) by [Stas Bekman](https://twitter.com/StasBekman). The Multi-Vector retriever gave pretty go
od results and was quite easy to set up too. 

Github link - [https://github.com/shreyansh26/RAG-ML-Engg-Open-Book](http
s://github.com/shreyansh26/RAG-ML-Engg-Open-Book)

Hope this is useful for folks!
```
---

     
 
all -  [ RAG pipeline to query the ML Engineering Open Book ](https://www.reddit.com/r/LangChain/comments/1bu4sm4/rag_pipeline_to_query_the_ml_engineering_open_book/) , 2024-04-03-0910
```
I built a quick RAG implementation using Langchain to make it easy to query the [ML Engineering Open Book](https://githu
b.com/stas00/ml-engineering) by [Stas Bekman](https://twitter.com/StasBekman). Hope it is useful for folks. It has been 
proving to be incredibly useful for me!

Github link - [https://github.com/shreyansh26/RAG-ML-Engg-Open-Book](https://gi
thub.com/shreyansh26/RAG-ML-Engg-Open-Book)
```
---

     
 
all -  [ CSV to FAISS vector store ](https://www.reddit.com/r/LangChain/comments/1bu2g22/csv_to_faiss_vector_store/) , 2024-04-03-0910
```
Hi guys!  


Does anyone know how I can directly go from a csv with two columns ('text' and 'embedding') to a FAISS vect
or store?  


Appreciate the help!
```
---

     
 
all -  [ Issues with simple agent ](https://www.reddit.com/r/LangChain/comments/1bu2fmr/issues_with_simple_agent/) , 2024-04-03-0910
```
Hey all,

Just getting started with agents, and I'm struggling to get this simple agent to work well, is there something
 I am missing here? Is there a better way to debug this so I can get a better understanding of what's going wrong? Despi
te specifying verbose=True, I don't get much info.  


# Issues:

* The agent does not always fetch recent news on Bitco
in
* The agent is stuck in an infinite loop without making progress
* The agent repeatedly searches the same articles ov
er an over again

 

# Below you will see the configuration for the agent:

    # --- 1. Search ---
    search = DuckDuc
kGoSearchRun(verbose=True)
    
    
    # --- 2. Scrape ---
    def scrape_url(url: str) -> str:
        headers = {
  
          'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:90.0) Gecko/20100101 Firefox/90.0'
        }
 
       req = Request(url=url, headers=headers)
        with urlopen(req) as response:
            response_content = res
ponse.read()
            soup = BeautifulSoup(response_content, 'html.parser')
            text_content = soup.get_text(
)
            return text_content
    
    web_fetch_tool = Tool.from_function(
        func=scrape_url,
        name='W
ebFetch',
        description='Fetches the content of a web page for a given URL'
    )
    
    
    # --- 3. Summarize
 ---
    llm = ChatAnthropic(
        model='claude-3-haiku-20240307',
        temperature=0.0,
        anthropic_api_ke
y=os.getenv('ANTHROPIC_KEY')
    )
    chain = LLMChain(
        llm=llm,
        prompt=PromptTemplate.from_template('S
ummarize the following content: {content}')
    )
    summarize_tool = Tool.from_function(
        func=chain.run,
     
   name='Summarizer',
        description='Summarizes the content of a web page'
    )
    
    
    # --- Setup Agent -
--
    tools = [search, web_fetch_tool, summarize_tool]
    agent_prompt = '''<task>Answer the User Query as best you ca
n.</task>
    
    <information>
    You have access to the following tools:
    {tools}
    
    Today's date is:
    {
today}
    
    Use the following format:
    
    Query: the input query you must answer
    Thought: you should always
 think about what to do
    Action: the action to take, should be one of [{tool_names}]
    Action Input: the input to t
he action
    Observation: the result of the action
    ... (this Thought/Action/Action Input/Observation can repeat up 
to 3 times maximum)
    Thought: I now know the final answer
    Final Answer: the final answer to the original input qu
estion
    </information>
    
    <user_query>
    {input}
    </user_query>
    
    <thought>
    {agent_scratchpad}

    </thought>
    '''
    
    agent = create_react_agent(
        llm=llm,
        tools=tools,
        prompt=PromptT
emplate.from_template(agent_prompt)
    )
    executor = AgentExecutor(agent=agent, tools=tools, handle_parsing_errors=T
rue, verbose=True)
    
    result = executor.invoke({
        'input': 'What is the latest news on Bitcoin?',
        '
today': datetime.now().date()
    })

# This outputs the following (interrupted)

>\> Entering new AgentExecutor chain..
.  
>  
>Query: What is the latest news on Bitcoin?  
>  
>  
>  
>Thought: To answer this query, I will need to search 
for the latest news and information on Bitcoin.  
>  
>  
>  
>Action: duckduckgo\_search  
>  
>Action Input: latest ne
ws on bitcoin  
>  
>The bitcoin price has topped its previous all-time high of $69,000 per bitcoin, climbing to well ov
er $70,000 as Goldman Sachs reveals a Wall Street revolution could be just around the corner. Bitcoin surged past $35,00
0 Monday, hitting the highest price since May 2022, as cryptocurrency markets continued their October bull run amid opti
mism that a BTC ETF will get approved in the U.S. Bitcoin analysts place significance on $69,000 as BTC price support in
to the Q1 close. ... blockchain and Bitcoin bringing you the latest crypto news and analyses on the future of money. A q
uick surge in bitcoin (BTC) early Tuesday afternoon lifted the price above $44,000 on some crypto exchanges, including C
oinbase, for the first time since early April 2022 as the largest crypto ... Bitcoin rose to a record for the third time
 in five days before traders appeared to take the opportunity to realize some of the recent gains.. The original cryptoc
urrency reached an all-time peak ...Query: What is the latest news on Bitcoin?  
>  
>  
>  
>Thought: To answer this qu
ery, I will need to search for the latest news and information on Bitcoin.  
>  
>  
>  
>Action: duckduckgo\_search  
>
  
>Action Input: latest news on bitcoin  
>  
>Bitcoin's halving, its fourth such supply cut that will see the number o
f new bitcoin issued to so-called miners who maintain the network fall to 3.125 bitcoin from 6.25 currently, is schedule
d ... Bitcoin surged past $35,000 Monday, hitting the highest price since May 2022, as cryptocurrency markets continued 
their October bull run amid optimism that a BTC ETF will get approved in the U.S. A quick surge in bitcoin (BTC) early T
uesday afternoon lifted the price above $44,000 on some crypto exchanges, including Coinbase, for the first time since e
arly April 2022 as the largest crypto ... Bitcoin rose to a record for the third time in five days before traders appear
ed to take the opportunity to realize some of the recent gains.. The original cryptocurrency reached an all-time peak ..
. Bitcoin analysts place significance on $69,000 as BTC price support into the Q1 close. ... blockchain and Bitcoin brin
ging you the latest crypto news and analyses on the future of money.Query: What is the latest news on Bitcoin?  
>  
>  

>  
>Thought: To answer this query, I will need to search for the latest news and information on Bitcoin.  
>  
>  
>  

>Action: duckduckgo\_search  
>  
>Action Input: latest news on bitcoin  
>  
>Bitcoin's halving, its fourth such suppl
y cut that will see the number of new bitcoin issued to so-called miners who maintain the network fall to 3.125 bitcoin 
from 6.25 currently, is scheduled ... Bitcoin surged past $35,000 Monday, hitting the highest price since May 2022, as c
ryptocurrency markets continued their October bull run amid optimism that a BTC ETF will get approved in the U.S. Bitcoi
n rose to a record for the third time in five days before traders appeared to take the opportunity to realize some of th
e recent gains.. The original cryptocurrency reached an all-time peak ... A quick surge in bitcoin (BTC) early Tuesday a
fternoon lifted the price above $44,000 on some crypto exchanges, including Coinbase, for the first time since early Apr
il 2022 as the largest crypto ... Bitcoin rose on Monday, briefly surpassing $42,000 to reach a 20-month high, in a new 
surge of momentum fueled by U.S. interest rate cut expectations and traders betting that American regulators ...Query: W
hat is the latest news on Bitcoin?  
>  
>  
>  
>Thought: To answer this query, I will need to search for the latest ne
ws and information on Bitcoin.  
>  
>  
>  
>Action: duckduckgo\_search  
>  
>Action Input: latest news on bitcoin  
>
  
>The bitcoin price has topped its previous all-time high of $69,000 per bitcoin, climbing to well over $70,000 as Gol
dman Sachs reveals a Wall Street revolution could be just around the corner. Bitcoin surged past $35,000 Monday, hitting
 the highest price since May 2022, as cryptocurrency markets continued their October bull run amid optimism that a BTC E
TF will get approved in the U.S. A quick surge in bitcoin (BTC) early Tuesday afternoon lifted the price above $44,000 o
n some crypto exchanges, including Coinbase, for the first time since early April 2022 as the largest crypto ... Bitcoin
 rose to a record for the third time in five days before traders appeared to take the opportunity to realize some of the
 recent gains.. The original cryptocurrency reached an all-time peak ... Bitcoin rose on Monday, briefly surpassing $42,
000 to reach a 20-month high, in a new surge of momentum fueled by U.S. interest rate cut expectations and traders betti
ng that American regulators ...Query: What is the latest news on Bitcoin?  
>  
>  
>  
>Thought: To answer this query, 
I have performed multiple searches on DuckDuckGo to gather the latest news and information on Bitcoin.  
>  
>Invalid Fo
rmat: Missing 'Action:' after 'Thought:Query: What is the latest news on Bitcoin?  
>  
>  
>  
>Thought: To answer this
 query, I will perform a series of searches on DuckDuckGo to gather the latest news and information on Bitcoin.  
>  
> 
 
>  
>Action: duckduckgo\_search  
>  
>Action Input: latest news on bitcoin  
>  
>Bitcoin's halving, its fourth such 
supply cut that will see the number of new bitcoin issued to so-called miners who maintain the network fall to 3.125 bit
coin from 6.25 currently, is scheduled ... Chesnot/Getty Images. New York CNN —. Bitcoin rose to $50,000 Monday for the 
first time in two years, fueled by a rush of new-investor enthusiasm and growing anticipation over a cryptic-sounding ..
. Bitcoin surged past $35,000 Monday, hitting the highest price since May 2022, as cryptocurrency markets continued thei
r October bull run amid optimism that a BTC ETF will get approved in the U.S. Bitcoin rose to a record for the third tim
e in five days before traders appeared to take the opportunity to realize some of the recent gains.. The original crypto
currency reached an all-time peak ... A quick surge in bitcoin (BTC) early Tuesday afternoon lifted the price above $44,
000 on some crypto exchanges, including Coinbase, for the first time since early April 2022 as the largest crypto ...Que
ry: What is the latest news on Bitcoin?  
>  
>  
>  
>Thought: To answer this query, I will perform a series of searche
s on DuckDuckGo to gather the latest news and information on Bitcoin.  
>  
>  
>  
>Action: duckduckgo\_search  
>  
>A
ction Input: latest news on bitcoin  
>  
>Bitcoin's halving, its fourth such supply cut that will see the number of new
 bitcoin issued to so-called miners who maintain the network fall to 3.125 bitcoin from 6.25 currently, is scheduled ...
 Bitcoin surged past $35,000 Monday, hitting the highest price since May 2022, as cryptocurrency markets continued their
 October bull run amid optimism that a BTC ETF will get approved in the U.S. A quick surge in bitcoin (BTC) early Tuesda
y afternoon lifted the price above $44,000 on some crypto exchanges, including Coinbase, for the first time since early 
April 2022 as the largest crypto ... Bitcoin has risen above $38,000 for the first time since May 2022 after battling th
is level for the past two weeks. By Lyllah Ledesma. Nov 24, 2023 at 4:53 p.m. UTC. Updated Mar 8, 2024 at 5:36 p ... Get
ty Images. Bitcoin extended its gains Tuesday, touching a more than two-year high above $57,000. The price of the flagsh
ip cryptocurrency was last higher by 5% at $57,328.95, according to Coin ...Query: What is the latest news on Bitcoin?  

>  
>  
>  
>Thought: To answer this query, I will perform a series of searches on DuckDuckGo to gather the latest news
 and information on Bitcoin.  
>  
>  
>  
>Action: duckduckgo\_search  
>  
>Action Input: latest news on bitcoin  
>  

>Bitcoin's halving, its fourth such supply cut that will see the number of new bitcoin issued to so-called miners who m
aintain the network fall to 3.125 bitcoin from 6.25 currently, is scheduled ... Bitcoin surged past $35,000 Monday, hitt
ing the highest price since May 2022, as cryptocurrency markets continued their October bull run amid optimism that a BT
C ETF will get approved in the U.S. Bitcoin analysts place significance on $69,000 as BTC price support into the Q1 clos
e. ... blockchain and Bitcoin bringing you the latest crypto news and analyses on the future of money. Bitcoin rose to a
 record for the third time in five days before traders appeared to take the opportunity to realize some of the recent ga
ins.. The original cryptocurrency reached an all-time peak ... A quick surge in bitcoin (BTC) early Tuesday afternoon li
fted the price above $44,000 on some crypto exchanges, including Coinbase, for the first time since early April 2022 as 
the largest crypto ...Query: What is the latest news on Bitcoin?  
>  
>  
>  
>Thought: To answer this query, I have pe
rformed multiple searches on DuckDuckGo to gather the latest news and information on Bitcoin.  
>  
>  
>  
>Action: duc
kduckgo\_search  
>  
>Action Input: latest news on bitcoin  
>  
>\^X\^Z

&#x200B;
```
---

     
 
all -  [ How to use RAG chat history with FastAPI? ](https://www.reddit.com/r/LangChain/comments/1bu1os7/how_to_use_rag_chat_history_with_fastapi/) , 2024-04-03-0910
```
Hi,

I created a RAG app and now want to also use chat history in my application. All of my applications functionality i
s handled via a FastAPI backend, the frontend is in Streamlit. 

How can I now add chat history in my FastAPI RAG endpoi
nt? 

Is there a way to just save the chat history in a session? E.g. making a post endpoint where the history gets adde
d to the chain. Alternatively I have heard that Redis is a good choice but as for my understanding it is not open-source
 anymore. For me it would be important to have a open-source solution which is free and can run online.

&#x200B;

Thank
s in advance!
```
---

     
 
all -  [ I built a free online course for teaching you how to implement Retrieval Augmented Generation ](https://www.reddit.com/r/learnmachinelearning/comments/1bu0w9j/i_built_a_free_online_course_for_teaching_you_how/) , 2024-04-03-0910
```
Curious if anyone here is interested in checking it out & giving me feedback. The course, entirely done in the browser, 
shows you how to parse a large PDF file, work with OpenAI's embedding function, use a vector DB, and use LangChain's Con
versationalRetrievalChain.

If you're interested please DM me!
```
---

     
 
all -  [ Error when Launching: '...unexpected keyword argument 'sharded'' ](https://www.reddit.com/r/ChatWithRTX/comments/1bu0vcu/error_when_launching_unexpected_keyword_argument/) , 2024-04-03-0910
```
Hello all!  
I have just installed Chat With RTX, I had to install in its own folder in C:\\ b/c of the weird rule where
 it cannot install in a user path with spaces. It installed just fine, but now when I launch I get the following error, 
in a CommandPrompt-looking screen.

  
TypeError: SafeTensorsInfo.\_\_init\_\_() got an unexpected keyword argument 'sha
rded'

&#x200B;

Has anyone else encountered this or been able to fix it?

&#x200B;

Full copy/paste:

Environment path 
found: C:\\0000ChatWIthRTX\\env\_nvd\_rag

App running with config

 {

'models': {

'supported': \[

{

'name': 'Mistra
l 7B int4',

'installed': true,

'metadata': {

'model\_path': 'model\\\\mistral\\\\mistral7b\_int4\_engine',

'engine':
 'llama\_float16\_tp1\_rank0.engine',

'tokenizer\_path': 'model\\\\mistral\\\\mistral7b\_hf',

'max\_new\_tokens': 1024
,

'max\_input\_token': 7168,

'temperature': 0.1

}

},

{

'name': 'Llama 2 13B int4',

'installed': false,

'metadata
': {

'model\_path': 'model\\\\llama\\\\llama13\_int4\_engine',

'engine': 'llama\_float16\_tp1\_rank0.engine',

'tokeni
zer\_path': 'model\\\\llama\\\\llama13\_hf',

'max\_new\_tokens': 1024,

'max\_input\_token': 3900,

'temperature': 0.1


}

}

\],

'selected': 'Mistral 7B int4'

},

'sample\_questions': \[

{

'query': 'How does NVIDIA ACE generate emotio
nal responses?'

},

{

'query': 'What is Portal prelude RTX?'

},

{

'query': 'What is important about Half Life 2 RTX
?'

},

{

'query': 'When is the launch date for Ratchet & Clank: Rift Apart on PC?'

}

\],

'dataset': {

'sources': \
[

'directory',

'youtube',

'nodataset'

\],

'selected': 'directory',

'path': 'dataset',

'isRelative': true

},

'st
rings': {

'directory': 'Folder Path',

'youtube': 'YouTube URL',

'nodataset': 'AI model default'

}

}

Traceback (mos
t recent call last):

  File 'C:\\0000ChatWIthRTX\\RAG\\trt-llm-rag-windows-main\\[app.py](https://app.py)', line 114, i
n <module>

embed\_model = HuggingFaceEmbeddings(model\_name=embedded\_model)

  File 'C:\\0000ChatWIthRTX\\env\_nvd\_ra
g\\lib\\site-packages\\langchain\\embeddings\\[huggingface.py](https://huggingface.py)', line 66, in \_\_init\_\_

self.
client = sentence\_transformers.SentenceTransformer(

  File 'C:\\0000ChatWIthRTX\\env\_nvd\_rag\\lib\\site-packages\\se
ntence\_transformers\\[SentenceTransformer.py](https://SentenceTransformer.py)', line 87, in \_\_init\_\_

snapshot\_dow
nload(model\_name\_or\_path,

  File 'C:\\0000ChatWIthRTX\\env\_nvd\_rag\\lib\\site-packages\\sentence\_transformers\\[u
til.py](https://util.py)', line 442, in snapshot\_download

model\_info = \_api.model\_info(repo\_id=repo\_id, revision=
revision, token=token)

  File 'C:\\0000ChatWIthRTX\\env\_nvd\_rag\\lib\\site-packages\\huggingface\_hub\\utils\\\_valid
ators.py', line 119, in \_inner\_fn

return fn(\*args, \*\*kwargs)

  File 'C:\\0000ChatWIthRTX\\env\_nvd\_rag\\lib\\sit
e-packages\\huggingface\_hub\\hf\_api.py', line 2230, in model\_info

return ModelInfo(\*\*data)

  File 'C:\\0000ChatWI
thRTX\\env\_nvd\_rag\\lib\\site-packages\\huggingface\_hub\\hf\_api.py', line 710, in \_\_init\_\_

self.safetensors = S
afeTensorsInfo(\*\*safetensors) if safetensors else None

TypeError: SafeTensorsInfo.\_\_init\_\_() got an unexpected ke
yword argument 'sharded'
```
---

     
 
all -  [ AzureChatOpenAI and create openai functions agent ](https://www.reddit.com/r/LangChain/comments/1bu04pk/azurechatopenai_and_create_openai_functions_agent/) , 2024-04-03-0910
```
Hello all!

I have an agent with 2 custom tools for searching embedding docs, till now i was using ChatOpenAi and everyt
hing was working, now i had to switch to AzureOpenAi and I am using AzureChatOpenAi from langchain, but when i pass a pr
ompt , i get back this :   


raise OutputParserException(

langchain\_core.exceptions.OutputParserException: Could not 
parse tool  input: {'arguments':......\_} because the 'arguments' is not valid JSON.

 But arguments is a valid json and
 this was working with ChatOpenAI, from what I've seen AzureChatOpenAI extends ChatOpenAI but i cant get past this. 

&#
x200B;

Has anyone faced anything similar?

  
Thank you in advance.
```
---

     
 
all -  [ Langchain Synthetic Data without OpenAI ](https://www.reddit.com/r/LangChain/comments/1btyy3w/langchain_synthetic_data_without_openai/) , 2024-04-03-0910
```
Hello!  

Has anyone here ever tried to create synthetic data with  Langchain using a local model different from those o
f OpenAI (for  example, Llama)? The tutorial on this page [https://python.langchain.com/docs/use\_cases/data\_generation
](https://python.langchain.com/docs/use_cases/data_generation) only shows the usage of OpenAI models.

&#x200B;

Thx ! 
```
---

     
 
all -  [ Improve retrieval of very similar chunk in Langchain ](https://www.reddit.com/r/LangChain/comments/1btwwnv/improve_retrieval_of_very_similar_chunk_in/) , 2024-04-03-0910
```
Hi all,
My document is a list of product code that matches a certain product name. Imagine there are 100 very similar ch
unks like this

Chunk1 :
Product code of ABC-123 = product A

Chunk2:
Product code of ABC-124 = product B

Chunk3:
Produ
ct code of ABC-125 = product C
…


Currently I transform the query ‘ABC-123’ into a question more similar to the chunk i
tself such as ´product code of ABC-XXX’. Then I 
use langchain default doc retriever for retrieving the chunk. But obvio
usly the embedding of the above chunk are extremely similar so the result is bad.

I then try using BM25 retriever but t
hen this retriever focus on the keyword ‘product code’ more instead of focusing on ´ABC-XXX’. Therefore, The result is e
ven worst with this BM25 retriever.

What are the idea or solution that can solve this problem? Thanks.


```
---

     
 
all -  [ Looking for open source tool to chat with my texts (news articles) ](https://www.reddit.com/r/LangChain/comments/1btw0vy/looking_for_open_source_tool_to_chat_with_my/) , 2024-04-03-0910
```
Hi.  
Im Looking for open source tool to chat with my texts (news articles)  and ask questions about people / locations 
and more, open chat.  


The context is very basic, I want to create a 'bucket' with about 100 articles and ask question
s about them.  
I really hope that there is some that is able to provide answers in CPU in a reasoonable time of not mor
e then 5 seconds...  
I have found [https://nuclia.com/](https://nuclia.com/) but i wasnt able so far to make it work lo
cally.

Thanks
```
---

     
 
all -  [ Would you use an LLM Integration tool if it had a better experience? ](https://www.reddit.com/r/ChatGPT/comments/1btvfbc/would_you_use_an_llm_integration_tool_if_it_had_a/) , 2024-04-03-0910
```
We've seen a lot of discussions about LangChain's documentation being poor or unintuitive and other tools like it. Would
 you use it more or at all if it had better documentation and user experience?

Do you use any other tool for LLM (ChatG
PT, Gemini, Claude 3, Grok, etc.) Integration?

If you have any other experience or something you'd like to share I'd lo
ve to hear about it and other products you use for LLM Integration.

[View Poll](https://www.reddit.com/poll/1btvfbc)
```
---

     
 
all -  [ Would you use an LLM Integration tool if it had a better experience? ](https://www.reddit.com/r/u_Itamark9/comments/1btv7ap/would_you_use_an_llm_integration_tool_if_it_had_a/) , 2024-04-03-0910
```
I've seen a lot of discussions about LangChain's documentation being poor or unintuitive and other tools like it. Would 
you use it more or at all if it had better documentation and user experience?

Do you use any other tool for LLM (ChatGP
T, Gemini, Claude 3, Grok, etc.) Integration?

If you have any other experience or something you'd like to share I'd lov
e to hear about it and other products you use for LLM Integration.

[View Poll](https://www.reddit.com/poll/1btv7ap)
```
---

     
 
all -  [ WinError 10061 while implementing function calling agent ](https://www.reddit.com/r/LangChain/comments/1btut9o/winerror_10061_while_implementing_function/) , 2024-04-03-0910
```
Hi, I have been using for around 2-3 weeks now and I have implemented a ReACT agent (with function calling) which worked
 fine until yesterday. I have not changed anything in my code when it just stopped working giving me the following error
:

&#x200B;

>raise ConnectionError(e, request=request)  
>  
>requests.exceptions.ConnectionError: HTTPConnectionPool(h
ost='localhost', port=11434): Max retries exceeded with url: /api/chat (Caused by NewConnectionError('<urllib3.connectio
n.HTTPConnection object at 0x0000022F1CC15310>: Failed to establish a new connection: \[WinError 10061\] No connection c
ould be made because the target machine actively refused it'))

I have restored even a previous version which I am sure 
worked, reinstalled langchain but the result is still the same. Also I am using ollama with solar for inference.

Any id
ea on possible problem? If you require more context let me know.
```
---

     
 
all -  [ Am i the only one to notice that run and invoke gives different outputs when using rag ](https://www.reddit.com/r/LangChain/comments/1btry9t/am_i_the_only_one_to_notice_that_run_and_invoke/) , 2024-04-03-0910
```
I was building an application using langchain and a few days ago i got the warning that run was going to Removed and use
 invoke instead 

But run used to give far better outputs compared with human like summerization which can be streamed w
ithout any modifications
On the other hand when invoke is used the output is unusable with random /n and metadata i get 
it some devs may want it 

But Why remove run ?
```
---

     
 
all -  [ Embeddings! ](https://www.reddit.com/r/LangChain/comments/1btrs1c/embeddings/) , 2024-04-03-0910
```
Is there an open-source project that can create high quality text from PDFs or Web Pages with little loss of quality?

I
 know there are a lot of projects that can do this but none that can handle everything like images, tables in those PDFs
 and Web Pages. For instance, we can use OCR/Image Captioning/Pix2Struct techniques to generate quality text and therefo
re embeddings from images. We can use similar techniques to convert tables to text and therefore embeddings.

Is there a
 framework that can do all of this out of the box? I know I'm asking for a lot here, but this seems like a problem that 
everyone who's doing RAG encounters everyday. I'm just wondering if there's anything out there before I spend time build
ing something myself.

What libraries or techniques do you use for generating quality embeddings?
```
---

     
 
all -  [ I am building a semantic based image search library, Picachain ](https://www.reddit.com/r/SideProject/comments/1btqm33/i_am_building_a_semantic_based_image_search/) , 2024-04-03-0910
```
With the growing image generation products the ability to quickly search through them will be crucial. So I came up with
 this idea of creating something for images. Something like langchain for images (or videos).

I am building Picachain [
https://github.com/d1pankarmedhi/picachain](https://github.com/d1pankarmedhi/picachain) a ready-to-use semantic based im
age search engine. Currently supports Chroma and Pinecone but will soon support almost all the popular DBs.

Feel free t
o leave a feedback or suggest feature ideas. I would appreciate that. :)

&#x200B;

[picachain](https://preview.redd.it/
g7cssq2f20sc1.png?width=1584&format=png&auto=webp&s=c4e87b97a2e4cc62eca8ac038fdfe060f910ccb7)
```
---

     
 
all -  [ RAG with Knowledge Graphs ? ](https://www.reddit.com/r/LangChain/comments/1btqluu/rag_with_knowledge_graphs/) , 2024-04-03-0910
```
How efficient and accurate is to use knowledge graphs for advanced RAG. Is it good enough to push it in production ? 
```
---

     
 
all -  [ Recent college graduate, worked at a startup for half of college, how's it look? ](https://www.reddit.com/r/resumes/comments/1bto9ua/recent_college_graduate_worked_at_a_startup_for/) , 2024-04-03-0910
```
Graduated college 3 months ago, applying to ML engineer/SWE positions at larger companies. I'm paranoid that my resume w
ill hold me back. How's it look?

https://preview.redd.it/cic6uobrfzrc1.jpg?width=5100&format=pjpg&auto=webp&s=eb0579801
316d90c2040dac56e8d731cf37103af
```
---

     
 
all -  [ [Project] FinancialAdvisorGPT : LLM+RAG Boilerplate Project ](https://www.reddit.com/r/MachineLearning/comments/1btlpgd/project_financialadvisorgpt_llmrag_boilerplate/) , 2024-04-03-0910
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

     
 
all -  [ Please help with my llm chain invocation ](https://i.redd.it/ngoudxie6yrc1.jpeg) , 2024-04-03-0910
```
I’m completely new to using Langchain which I’m using in a JavaScript project. I have a custom_K.gguf base model(not a c
hat model). From the screenshot, when the line 
const result = await chain.call({ question: input }) runs, I get this:


[chain/start] [1:chain:LLMChain] Entering Chain run with input: {
  'question': 'who is elon musk',
  'chat_history': ''

}
[chain/error] [1:chain:LLMChain] [1ms] Chain run errored with error: 'this.llm.pipe is not a function\n\nTypeError: t
his.llm.pipe is not a function\n    at LLMChain._call 

Without using chain, I'm able to send and receive answers to the
 model without issues but I'm using chain for history/memory purpose and I can't seem to understand why this is happenin
g. 

The difference between my code and the [sample](https://github.com/langchain-ai/langchainjs/blob/main/examples/src/
chains/llm_chain_stream.ts) on their website is the use of LlmaCpp in place of OpenAI. So I’m not sure where else to loo
k.

Would really pepreciate any help I can get please 🙏🏾.

I’ve tried to [create a discussion](https://github.com/langch
ain-ai/langchainjs/discussions/4940) on the langchainjs repo but only received a response from the bot which wasn’t very
 helpful.


```
---

     
 
all -  [ Integrating a Hugging Face LLM Model with Langchain via SageMaker ](https://www.reddit.com/r/LangChain/comments/1bthz3u/integrating_a_hugging_face_llm_model_with/) , 2024-04-03-0910
```
Hello everyone,

I'm trying to integrate a LLM with Langchain, specifically using the create\_react\_agent function docu
mented here: [Langchain create\_react\_agent documentation](https://api.python.langchain.com/en/latest/agents/langchain.
agents.react.agent.create_react_agent.html).

For this test, I am trying to work with the open-source FLAN model from Hu
gging Face, available at: [FLAN T5 XL on Hugging Face](https://huggingface.co/google/flan-t5-xl/tree/main). My goal is t
o deploy this model as an endpoint in AWS SageMaker and then utilize it within Langchain by creating a react agent.

Wha
t steps should I follow to ensure that when I make a call to this SageMaker endpoint, it returns an LLM object that Lang
chain's create\_react\_agent function can utilize? Also, do not want to use SageMaker DLC images.

I'm unsure about the 
best practices for making the deployed model compatible as an LLM object for Langchain, especially in terms of the expec
ted response format and any necessary wrappers or adapters.

Can some one offer insights into:

1. The specific modifica
tions or configurations needed on the SageMaker side to ensure compatibility with Langchain.
2. How to properly format t
he SageMaker endpoint's response to be recognized as an LLM object by Langchain.
3. Any examples or templates that might
 be helpful for this process.  


If this is not possible with SageMaker, what are the other options that I can look int
o? 

Appreciate your help on this.
```
---

     
 
all -  [ I am building a chatgpt alternative that doesn't lock you into a single model ](https://www.reddit.com/r/ChatGPT/comments/1btbipl/i_am_building_a_chatgpt_alternative_that_doesnt/) , 2024-04-03-0910
```
Three months ago, during the whole Sam leaving openai chaos period, i posted this:[https://www.reddit.com/r/ChatGPT/comm
ents/189dddw/i\_am\_terrified/](https://www.reddit.com/r/ChatGPT/comments/189dddw/i_am_terrified/?utm_source=share&utm_m
edium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button)

I shared my concerns about the heavy reliance on a f
ew centralized AI services and the increasing levels of censorship and limitation being imposed on these platforms. The 
response from this community was nothing short of incredible, and it fueled my resolve to do something about it.

I have
 working on it during my free time and its nearly complete so i am sharing update 1,as you see i am using a coding copil
ot assistant with the model phind-codellama-v2 which is specially finetuned for this, also adding a lot of other uncenso
red models too which are better for stuff like creative writing and roleplay bots.

Here to ask you all for any feedback
 or feature requests you might have as i continue working on the [site](https://muxchat.com)  


[Muxchat](https://previ
ew.redd.it/zdy2aq4mvwrc1.png?width=1440&format=png&auto=webp&s=69000d046a546a2d5bfca1298dde5ed8d8f4aa02)

&#x200B;
```
---

     
 
all -  [ Why does langchain prompt using HTML tags? ](https://www.reddit.com/r/LangChain/comments/1bt9qt3/why_does_langchain_prompt_using_html_tags/) , 2024-04-03-0910
```
This may be obvious to some, or obvious to none, but why do langchain use html tags in their prompts to separate section
s of prompts. For instance in their docs they use the following: 

<context>  
{context}  
</context>

I of course under
stand the usefulness of clear separations in the prompt templates but why use the HTML tags? Intuitively I would've thou
ght LLM's wouldn't be as able to interpret these tags compared  to raw text? However I'm not certain on the formatting o
f internet data proprietary  LLM's like Open AI's GPT series were trained on.
```
---

     
 
all -  [ AI agents Group Discussion using Autogen ](https://www.reddit.com/r/LangChain/comments/1bt7xrf/ai_agents_group_discussion_using_autogen/) , 2024-04-03-0910
```
Hey everyone, check out this tutorial on how to enable Multi-Agent conversations and group discussion between AI Agents 
using Autogen by Microsoft by GroupChat and ChatManager functions : https://youtu.be/zcSNJMUYHBk?si=0EBBJVw-sNCwQ1K_
```
---

     
 
all -  [ [Project] Picachain, image search made simple. ](https://www.reddit.com/r/MachineLearning/comments/1bt7epv/project_picachain_image_search_made_simple/) , 2024-04-03-0910
```
I am working on creating something for image search, basically something like langchain for images. Probably add videos 
too.

Currently supports chromaDB. Working on pinecone and other vector dbs. [https://github.com/d1pankarmedhi/picachain
](https://github.com/d1pankarmedhi/picachain)

Will you use something like this? What else should I add? Feel free to ad
d your views.

Appreciate your feedback or any feature ideas :)

&#x200B;
```
---

     
 
all -  [ Open-Source AI Cookbook [Hugging Face] ](https://www.reddit.com/r/CompSocial/comments/1bt6z2m/opensource_ai_cookbook_hugging_face/) , 2024-04-03-0910
```
Are you building AI-powered workflows and projects using open-source tools/models as part of your research? You may want
 to check out the Open-Source AI Cookbook from Hugging Face, which collects community-created notebooks covering a numbe
r of use cases. Here are some of the recently-added examples:

* [**Using LLM-as-a-judge 🧑‍⚖️ for an automated and versa
tile evaluation**](https://huggingface.co/learn/cookbook/llm_judge)
* [**Create a legal preference dataset**](https://hu
ggingface.co/learn/cookbook/pipeline_notus_instructions_preferences_legal)
* [**Suggestions for Data Annotation with Set
Fit in Zero-shot Text Classification**](https://huggingface.co/learn/cookbook/labelling_feedback_setfit)
* [**Implementi
ng semantic cache to improve a RAG system**](https://huggingface.co/learn/cookbook/semantic_cache_chroma_vector_database
)
* [**Building A RAG Ebook “Librarian” Using LlamaIndex**](https://huggingface.co/learn/cookbook/rag_llamaindex_librari
an)
* [**Stable Diffusion Interpolation**](https://huggingface.co/learn/cookbook/stable_diffusion_interpolation)
* [**Bu
ilding A RAG System with Gemma, MongoDB and Open Source Models**](https://huggingface.co/learn/cookbook/rag_with_hugging
_face_gemma_mongodb)
* [**Prompt Tuning with PEFT Library**](https://huggingface.co/learn/cookbook/prompt_tuning_peft)
*
 [**Migrating from OpenAI to Open LLMs Using TGI’s Messages API**](https://huggingface.co/learn/cookbook/tgi_messages_ap
i_demo)
* [**Automatic Embeddings with TEI through Inference Endpoints**](https://huggingface.co/learn/cookbook/automati
c_embedding_tei_inference_endpoints)
* [**Simple RAG for GitHub issues using Hugging Face Zephyr and LangChain**](https:
//huggingface.co/learn/cookbook/rag_zephyr_langchain)
* [**Embedding multimodal data for similarity search using 🤗 trans
formers, 🤗 datasets and FAISS**](https://huggingface.co/learn/cookbook/faiss_with_hf_datasets_and_clip)
* [**Fine-tuning
 a Code LLM on Custom Code on a single GPU**](https://huggingface.co/learn/cookbook/fine_tuning_code_llm_on_single_gpu)

* [**RAG Evaluation Using Synthetic data and LLM-As-A-Judge**](https://huggingface.co/learn/cookbook/rag_evaluation)
* [
**Advanced RAG on HuggingFace documentation using LangChain**](https://huggingface.co/learn/cookbook/advanced_rag)
* [**
Detecting Issues in a Text Dataset with Cleanlab**](https://huggingface.co/learn/cookbook/issues_in_text_dataset)

Check
 out the Open-Source AI Cookbook here: [https://huggingface.co/learn/cookbook/index](https://huggingface.co/learn/cookbo
ok/index)

Do you have any go-to resources, notebooks, or tutorials for open-source AI tools that you would recommend? T
ell us about them in the comments!
```
---

     
 
all -  [ [For hire] Ex-Booking[dot]com Data Scientist and GenAI specialist [50 USD/hr]  ](https://www.reddit.com/r/ForHire_Programmers/comments/1bt6opo/for_hire_exbookingdotcom_data_scientist_and_genai/) , 2024-04-03-0910
```
Hi I have used this subreddit to get some clients before and been able to deliver to all of them.

Here is my work exper
ience + technical expertise:

1. 4+ years of experience in data roles
2. Worked at Agoda (Booking[dot]com) as Data analy
st
3. Worked in a Norwegian Telecom provider as Data Scientist
4. Working part time as GenAI specialist

Skills: Statist
ics, ML, Python, SQL and Tableau

Also write about my projects on Medium: https://medium.com/firebird-technologies/chat-
with-your-pdfs-using-langchain-e57866b7926d

https://medium.com/firebird-technologies/using-langchain-to-teach-an-llm-to
-write-like-you-aab394d54792
```
---

     
 
all -  [ CSV RAG with langchain issue ](https://www.reddit.com/r/LangChain/comments/1bt64ld/csv_rag_with_langchain_issue/) , 2024-04-03-0910
```
Does anyone have a working CSV RAG application using LangChain and open-source embeddings and LLMs? I've been trying to 
get a working implementation for a while, but I'm running into the same problem with CSV files. As soon as I run a query
, it's not able to retrieve more than four relevant chunks from the vectordb. If a query requires the whole dataset to a
nswer the question, it will not be able to answer it. If anyone has working code for CSV RAG, could they share it? It wo
uld be helpful. 
```
---

     
 
all -  [ CSV RAG with langchain  ](https://www.reddit.com/r/LocalLLaMA/comments/1bt62bk/csv_rag_with_langchain/) , 2024-04-03-0910
```
Does anyone have a working CSV RAG application using LangChain and open-source embeddings and LLMs? I've been trying to 
get a working implementation for a while, but I'm running into the same problem with CSV files. As soon as I run a query
, it's not able to retrieve more than four relevant chunks from the data. If a query requires the whole dataset to answe
r the question, it will not be able to answer it. If anyone has working code for CSV RAG, could they share it? It would 
be helpful.
```
---

     
 
all -  [ +500mm rows of data is embedding or fine tuning a good way to enable this data? ](https://www.reddit.com/r/LangChain/comments/1bt5opa/500mm_rows_of_data_is_embedding_or_fine_tuning_a/) , 2024-04-03-0910
```
I have hundreds of millions of rows of data that's basically click tracking.  I want to create a chat bot with this data
.  I'm new to LLM customization.

Is fine tuning a model with this data a good way to go about this or is creating embed
dings better?

I'm open to breaking it up in to 3 month chunks.  I dont have access to unlimited hardware.
```
---

     
 
all -  [ PgVector Filtering Methods/Options in JS ](https://www.reddit.com/r/LangChain/comments/1bt4vgk/pgvector_filtering_methodsoptions_in_js/) , 2024-04-03-0910
```
Hi there! I’ve been searching for documentation on how to filter my pgvector similarity searches (with LangchainJS) but 
haven’t found any good documentation on the available options/methods. Does anyone know where I can find some? There is 
one example on the Langchain docs using ‘in’ but nothing else.

Also would anyone be able to show me how to do filtering
 based on dates?

Thank you!
```
---

     
 
all -  [ A Senior SDE from Google recommended my book on LangChain 😎 ](https://i.redd.it/lazcbinjjvrc1.png) , 2024-04-03-0910
```
Never thought my debut book 'LangChain in your Pocket' would be this big a hit. First being a national bestseller (progr
amming), than an international Bestseller(AI) and now this. A big thanks to the community 🥰🥰
```
---

     
 
all -  [ RAGFlow, the deep document understanding based RAG engine is open sourced ](https://www.reddit.com/r/LangChain/comments/1bt3ozy/ragflow_the_deep_document_understanding_based_rag/) , 2024-04-03-0910
```
## Key Features

### 'Quality in, quality out'

* [Deep document understanding](https://github.com/infiniflow/ragflow/bl
ob/main/deepdoc/README.md)\-based knowledge extraction from unstructured data with complicated formats.
* Finds 'needle 
in a data haystack' of literally unlimited tokens.

### Template-based chunking

* Intelligent and explainable.
* Plenty
 of template options to choose from.

### Grounded citations with reduced hallucinations

* Visualization of text chunki
ng to allow human intervention.
* Quick view of the key references and traceable citations to support grounded answers.


###  Compatibility with heterogeneous data sources

* Supports Word, slides, excel, txt, images, scanned copies, struct
ured data, web pages, and more.

### Automated and effortless RAG workflow

* Streamlined RAG orchestration catered to b
oth personal and large businesses.
* Configurable LLMs as well as embedding models.
* Multiple recall paired with fused 
re-ranking.
* Intuitive APIs for seamless integration with business.

The github address:

[https://github.com/infiniflo
w/ragflow](https://github.com/infiniflow/ragflow)

The offitial homepage:

[https://ragflow.io/](https://ragflow.io/)

T
he demo address:

[https://demo.ragflow.io/](https://demo.ragflow.io/)
```
---

     
 
all -  [ Would you use LangChain more if it had better documentation? ](https://www.reddit.com/r/mlops/comments/1bt1ieb/would_you_use_langchain_more_if_it_had_better/) , 2024-04-03-0910
```
I've seen a lot of discussions about LangChain's documentation being poor or unintuitive. Would you use it more or at al
l if it had better documentation and user experience?

If you have any other experience or something you'd like to share
 I'd love to hear about it and other products you use.

[View Poll](https://www.reddit.com/poll/1bt1ieb)
```
---

     
 
all -  [ Create your AI SaaS for chatbot creation in just one day! ](https://www.reddit.com/r/micro_saas/comments/1bt190p/create_your_ai_saas_for_chatbot_creation_in_just/) , 2024-04-03-0910
```
I've developed an easy to use API for building advanced AI chatbots, utilizing cutting-edge technologies like Langchain,
 FastAPI, Gemini, OpenAI GPT-4, Pinecone, and strong AI security measures. It's perfect for SaaS platforms looking to of
fer customizable chatbot solutions. 

Interested? Contact me at jaberibraheem808@gmail.com.  

```
---

     
 
MachineLearning -  [ [D] : Scale PDF Q&A App to 10K Users with GPUs – <$250/Mo ](https://www.reddit.com/r/MachineLearning/comments/1b6jv56/d_scale_pdf_qa_app_to_10k_users_with_gpus_250mo/) , 2024-04-03-0910
```
Hello everyone,

Check out this step-by-step detailed tutorial on building and scaling a PDF Q&A Application using Pinec
one, Langchain and Inferless

&#x200B;

[Architecture](https://preview.redd.it/zfta52cbddmc1.png?width=1301&format=png&a
uto=webp&s=440399212d3feb03e861759a31602e2cde0dc7fb)

Alongside, the detailed quick deploy guide, it also includes cost 
analysis on how you can save upto 84% cost with an example of processing 3000 documents and nearly 10,000 queries every 
month, all while dramatically cutting your costs from $1800 ( AWS) to just $250 a month on Inferless.

Here is the tutor
ial - [https://cookbook.inferless.com/](https://cookbook.inferless.com/)

If you resonate, join the discussion on Hacker
news here - [https://news.ycombinator.com/item?id=39594588](https://news.ycombinator.com/item?id=39594588)
```
---

     
 
deeplearning -  [ Tengyu Ma on Voyage AI - Weaviate Podcast #91! ](https://www.reddit.com/r/deeplearning/comments/1bjft8i/tengyu_ma_on_voyage_ai_weaviate_podcast_91/) , 2024-04-03-0910
```
**Voyage AI** is the newest giant in the embedding, reranking, and search model game!

I am SUPER excited to publish our
 latest Weaviate podcast with Tengyu Ma, Co-Founder of Voyage AI and Assistant Professor at Stanford University!

We beg
an the podcast with a deep dive into everything embedding model training and contrastive learning theory. Tengyu deliver
ed a **masterclass** in everything from scaling laws to multi-vector representations, neural architectures, representati
on collapse, data augmentation, semantic similarity, and more! I am beyond impressed with Tengyu's extensive knowledge a
nd explanations of all these topics.

The next chapter dives into a case study Voyage AI did **fine-tuning an embedding 
model for the LangChain documentation.** This is an absolutely fascinating example of the role of continual fine-tuning 
with very new concepts (for example, very few people were talking about chaining together LLM calls 2 years ago), as wel
l as the data efficiency advances in fine-tuning.

We concluded by discussing ML systems challenges in serving an embedd
ings API. Particularly the challenge of detecting if a request is for batch or query inference and the optimizations tha
t go into either say \~100ms latency for a query embedding or maximizing throughput for batch embeddings.

I hope you fi
nd the podcast interesting, more than happy to discuss any of these topics with you or answer any questions about the co
ntent in the podcast! Thank you so much!

YouTube: [https://www.youtube.com/watch?v=xPdyivfheqI](https://www.youtube.com
/watch?v=xPdyivfheqI)

Spotify: [https://spotifyanchor-web.app.link/e/u6XPLYfF7Hb](https://spotifyanchor-web.app.link/e/
u6XPLYfF7Hb)
```
---

     
