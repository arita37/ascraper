 
all -  [ I am 5th Sem CSE Student, I would really appreciate a Resume Review as to how can I make it better ](https://i.redd.it/gin1gstb2wmb1.jpg) , 1694116564.0
```
I have been freelancing since class 2020 for a good client base and some DMAs although I am not sure where I should add 
that
```
---

     
 
all -  [ Library or Langchain component for cleaning OpenAI response? ](https://www.reddit.com/r/LangChain/comments/16cnvuk/library_or_langchain_component_for_cleaning/) , 1694115007.0
```
Hello everyone, 

I'm building an AI application, and one of the biggest issues with it is sometimes GPT-3.5 will give m
e a function call that is not proper JSON. I made it a loop so that if it is incorrect JSON, it tells the model that and
 asks it to retry.

There must be a lot of people having this same problem. Is there a python library someones made for 
regexing these errors out, or some other way to reduce the likelyhood of them happening as close to 0% as possible? At t
he moment, these errors are occuring about 10% of the time, and GPT-3.5 corrects them only 2/3rds of that time. That mea
ns that 3% of the time my program is failing which is too high.

Any ideas? I'm open to anything!
```
---

     
 
all -  [ Chainlit playground now supports all LangChain LLMs ](https://www.reddit.com/r/LangChain/comments/16cmjt9/chainlit_playground_now_supports_all_langchain/) , 1694111334.0
```
Hi LangChain Community!  


We released a new version of the prompt playground which now supports all LangChain LLMs 🔥  

That means you can iterate on your prompts, variables and LLM settings for ANY LLM directly from the UI. Iterating on i
ntermediary steps just got a whole lot simpler!

Full thread and explanation below

[https://twitter.com/chainlit\_io/st
atus/1699821349856854316](https://twitter.com/chainlit_io/status/1699821349856854316)
```
---

     
 
all -  [ Rate my Pipe! Colab notebook incl. ](https://www.reddit.com/r/LangChain/comments/16cm7g1/rate_my_pipe_colab_notebook_incl/) , 1694109740.0
```
Colab: [https://colab.research.google.com/drive/1mi0Xw5bEa-wga48fPE1HSxWQjI47ftda?usp=sharing](https://colab.research.go
ogle.com/drive/1mi0Xw5bEa-wga48fPE1HSxWQjI47ftda?usp=sharing)

Hey, this is a little chat project I set up a while back 
to review embeddings, play with models, and generally diy research for various things. Sharing for fun, feel free to tea
r it apart, or share what you like. I like that it's clean and easy to visualize the process in Colab/ jupyter notebook.
 Chat and everything seems to be working at the time of posting. You'll need your openai key, and deeplake key (here: [A
ctiveloop | Deep Lake | Data Lake for Deep Learning](https://www.activeloop.ai/))

Pipeline notes: HuggingFace embedding
s models are used so they can be swapped to test the individual model performance and chat-output generation. Currently,
 the chat is openai gpt-3.5 modelset because it's easy and reliable for testing prototyping. I've used Activeloop Deepla
ke vector-db because if you're not familiar, once your embeddings are ingested, they have a great visualizer so you can 
see your embeddings, and review each embedding individually if needed. The pipeline is designed to be fun, with lots of 
ways to visualize the outputs as things are being processed. Lots of progress bars and generation totals to show exactly
 what's going on in the print statements. 

Features: 

i. huggingface embeddings model can easily be switched and d/l v
ia model name configuration

ii. embedding models are currently BERT models, distilled just means the original model has
 been reduced by 40% and retains 95%+ of its original performance. 

iii. ingestion speed is currently 3/seconds per pag
e (mildly better with openai embeddings)

iv. paralell processing for the embeddings is possible, but with GPU support i
t's redundant, and with colab-pro you have the oppertunity to create and ingest the embeddings at a 'normal' rate 

v. o
penai gpt-3.5 chat model 

Roadmap:

i. I know the chat sucks, I'm working on an agent to combine various tools. Feel fr
ee to provide your options or opinions on what would work best for vector retrieval 

ii. I'm working with the TensorFlo
w uploader in Langchain, in combination with the DeepLake/ Activeloop performant/compute  loader (which also uses tensor
flow), to increase the speed of embedding ingestion. In preliminart trials, this seems promising, but nothing to roll ou
t for sharing yet.   


Enjoy if you tinker with it. Otherwise, feel free to share your thoughts, opinions, concerns abo
ut the pipeline. 

&#x200B;
```
---

     
 
all -  [ Help needed: making a tool required for agent? ](https://www.reddit.com/r/LangChain/comments/16clvhp/help_needed_making_a_tool_required_for_agent/) , 1694108371.0
```
Hi there, 

Hoping to get some guidance with how to setup the agent framework for my use case, where I always want a par
ticular tool to run regardless of what is being asked -- like a 'required' tool.

&#x200B;

I have a basic product chat 
bot working for RAG-based QA about a product, retrieving info about the product to help it answer questions.

So if I as
k a question like:

>**'It's going to be 45°F this weekend. Is this jacket appropriate?'**

Then the bot is correctly re
sponding with: (specific response based on the temperature rating of the jacket itself):

>*'Yes, this jacket would be a
ppropriate for a temperature of 45 degrees Fahrenheit. The temperature comfort range for this jacket is 40°F - 50°F, so 
it is designed to provide comfort and insulation within that range.'*

  
Now I'm trying to expand the bot to be able to
 answer a question like:

>**'Is this jacket appropriate for the weather in Denver this weekend?'**

&#x200B;

To do thi
s, I setup an  `conversational-react-description` agent that has 2 tools:

* openweathermap-api
* Product Chat: A custom
 tool wrapping the same product chat bot above

&#x200B;

To answer this question, I want the agent to:

1. Lookup the w
eather in Denver this weekend (weather tool)
2. Lookup the product specifications of the jacket (RAG), including tempera
ture rating (product tool)
3. Combine the results of 1 and 2 to say yes or no and explain why

&#x200B;

The problem is,
 it's only running the weather tool, and then providing a generic response that 'yes a a jacket is probably a good idea'
 based on the weather. 

    > Entering new AgentExecutor chain...
    
    Thought: Do I need to use a tool? Yes
    Ac
tion: OpenWeatherMap
    Action Input: Denver,US
    Observation: In Denver,US, the current weather is as follows:
    D
etailed status: broken clouds
    Wind speed: 0.89 m/s, direction: 74°
    Humidity: 22%
    Temperature: 
      - Curre
nt: 28.34°C
      - High: 30.63°C
      - Low: 25.95°C
      - Feels like: 27.03°C
    Rain: {}
    Heat index: None
   
 Cloud cover: 54%
    Thought: Do I need to use a tool? No
    AI: Based on the current weather in Denver, US, it looks 
like a jacket would be appropriate for this weekend. The temperature is currently 28.34°C, with a high of 30.63°C and a 
low of 25.95°C. The humidity is 22%, and the wind speed is 0.89 m/s.
    
    > Finished chain.

&#x200B;

I want every 
response to be in the context of the product, so I always want the product tool to run.

I've tried modifying the agent 
prompt prefix with language like '*You use should always use the 'Product Chat' tool before returning the final answer.'
*, but it has no effect.  


Is there a way to mark a tool as required? Is there a better way to try and instruct the ag
ent about the importance of running the product chat tool?

&#x200B;
```
---

     
 
all -  [ The Point of LangChain — with Harrison Chase of LangChain ](https://www.latent.space/p/langchain#details) , 1694107253.0
```

```
---

     
 
all -  [ Understanding Langchain modules (resource recommendations) ](https://www.reddit.com/r/LangChain/comments/16ci4qw/understanding_langchain_modules_resource/) , 1694098967.0
```
What's a good resource for understanding the different modules of Langchain in detail? I.e.: models, prompts, output par
sers, chains, etc., breaking down their options and explaining how to link them together.

Preferably in JS/TS.

I've be
en reading the docs, and while I grasp the general concepts, I often struggle with practical implementation. I frequentl
y find myself copying the examples for guidance. I'd like to gain a better understanding of how everything fits together
, so I can confidently assemble the building blocks on my own. Thanks
```
---

     
 
all -  [ Learn how to customize the newly added Neo4j Vector index in LangChain ](https://www.reddit.com/r/Neo4j/comments/16chc9d/learn_how_to_customize_the_newly_added_neo4j/) , 1694097009.0
```
Learn how can you use all the parameters of the Neo4j Vector index in LangChain to customize it to your needs 

[https:/
/blog.langchain.dev/neo4j-x-langchain-new-vector-index/](https://blog.langchain.dev/neo4j-x-langchain-new-vector-index/)

```
---

     
 
all -  [ [P] FalkorDB - a fast Graph Database - Knowledge Graph as RAG ](https://www.reddit.com/r/MachineLearning/comments/16cg6k7/p_falkordb_a_fast_graph_database_knowledge_graph/) , 1694094085.0
```
We're building a fast low latency Graph Database called FalkorDB that will also support Vector search.  
It's based on R
edis and can be used both as a stand alone database or a module for existing Redis.  
It feels like that is going to be 
the most optimized way to serve Knowledge as RAG, would love to get your feedback.  
[https://github.com/FalkorDB/falkor
db](https://github.com/FalkorDB/falkordb)  


It already supports LlamIndex and Langchain:  
[https://python.langchain.c
om/docs/use\_cases/more/graph/graph\_falkordb\_qa](https://python.langchain.com/docs/use_cases/more/graph/graph_falkordb
_qa)  
[https://gpt-index.readthedocs.io/en/latest/examples/index\_structs/knowledge\_graph/FalkorDBGraphDemo.html](http
s://gpt-index.readthedocs.io/en/latest/examples/index_structs/knowledge_graph/FalkorDBGraphDemo.html)

&#x200B;
```
---

     
 
all -  [ Enhancing My Educational Content App with Fact-Checking Capabilities – Need Guidance! ](https://www.reddit.com/r/LangChain/comments/16cdrlp/enhancing_my_educational_content_app_with/) , 1694087314.0
```

Hey there, fellow developers!

I'm working on an educational content app powered by GPT, and it's been going great so f
ar. Users can interact with a PDF document, thanks to embeddings, vector stores, and all the fancy stuff. But now, I wan
t to take it up a notch and add a fact-checking feature.

Here's the challenge: I have a PDF with educational content, a
nd I also have a separate text file that outlines guidelines on how to fact-check the document. It's like a set of instr
uctions saying, 'Here's how you should fact-check this.'

What I want is for users to hit a 'fact check' button, and GPT
 should analyze the PDF document according to the guidelines provided in that text file. But here's where I'm stuck – ho
w do I make GPT understand and follow those guidelines?

I know fine-tuning is a thing, but it usually involves a 'promp
t and response' format, which doesn't quite fit my scenario. My guidelines are more like rules to follow, not prompts fo
r generating responses.

So, devs, any ideas on how to make this happen? I'm all ears for your suggestions and guidance.

```
---

     
 
all -  [ Cheap ‘supercomputer’ for huge llm models ](https://www.reddit.com/r/LangChain/comments/16ccxbu/cheap_supercomputer_for_huge_llm_models/) , 1694084696.0
```
If I will order bunch of Intel Xeon’s on AliExpress and I will install multiply xeons on compatible motherboard with RAM
 of 3200Mhz (maybe 256gb). Is it a good idea to create a server to launch llm like Falcon on 70B parameters?
```
---

     
 
all -  [ Build an LLM-powered application using LangChain ](https://www.leewayhertz.com/build-llm-powered-apps-with-langchain/) , 1694081055.0
```

```
---

     
 
all -  [ Need Help with LLM integrations ](https://www.reddit.com/r/LocalLLaMA/comments/16c9v7g/need_help_with_llm_integrations/) , 1694073376.0
```
Hey guys where should I start for the following:

Have an internal language model that has access to internet in real ti
me. 

And to integrate it to selfhosted apps like task managers or home assistants. 

Langchain? 

I'm new :) I have Oob
abooga installed with a lot of cool models and extensions installed, but that's it.
```
---

     
 
all -  [ A question on chaining using langchain ](https://www.reddit.com/r/LangChain/comments/16c5jws/a_question_on_chaining_using_langchain/) , 1694058656.0
```
Lets say I want to achieve deep Q & A over tabular (CSV) data. The data itself has columns that are a mix of numbers and
 text and categories (again in text form). I do not want to use OpenAI or any hosted LLM API for that matter. My hard re
quirement is to do all of this via local LLMs. The query itself can be getting to know more about the data or could be t
o get statistical info about the data (e.g. medians, grouped or filtered quantities etc). The data will be in csv format
 but I am open to reformatting it to more suitable structures. The data will be entirely something that the llm has neve
r seen before. Is it possible to build a custom langchain agent that uses:  

* a tabular q & a model (e.g. tapas) to ge
t facts about the data related to the query. The data is pre-embedded in a vector store and passed as context with the q
uery.
   * a standard chat model (e.g. llama2) that 'orchestrates' the other models and tools
   * tools like python rep
l and/or pandas

Opens that I have: 

* Is the above even feasible?
* How do I even manage to achieve an 'orchestration'
 via the llm like llama2? Is it even possible or do I query and hope for the best (after due config and setting tools et
c)?
   * Any hints on how best to setup the entire chain?

Thanks! 
```
---

     
 
all -  [ My First NextJS Project ](https://www.reddit.com/r/nextjs/comments/16c46hp/my_first_nextjs_project/) , 1694054647.0
```
Having been an enterprise Java guy for almost 20 years, figured I’d try something new and created [BarGPT.app](https://w
ww.bargpt.app) - an AI cocktail creator using NextJS. 

Stack: NextJS deployed on Vercel, langchain/OpenAI, stability ai
 for images, stripe for payments and tailwind for css. 

Thoroughly shocked how much I have loved working with nextjs an
d Vercel. Even coming around to Tailwind!

Feedback and compliments welcome!
```
---

     
 
all -  [ Retrieving metadata from Pinecone vector store ](https://www.reddit.com/r/LangChain/comments/16c3g0h/retrieving_metadata_from_pinecone_vector_store/) , 1694052615.0
```
Hi all

I have created a chatbot which uses multiple tools to get an answer for a question. One of the tools queries a P
inecone index to get an answer.

Following is the general structure of the complete chatbot:


    from langchain import
 SQLDatabase, SQLDatabaseChain
    from langchain.prompts.prompt import PromptTemplate
    from langchain.chat_models im
port ChatOpenAI
    from langchain.memory import ConversationBufferWindowMemory
    from langchain.chains import Convers
ationChain, LLMChain
    from langchain.embeddings import OpenAIEmbeddings
    from langchain.chains import RetrievalQAW
ithSourcesChain, RetrievalQA
    from langchain.vectorstores import Pinecone
    from langchain.agents import Agent, Too
l, AgentType, AgentOutputParser, AgentExecutor, initialize_agent
    from langchain.agents.conversational.output_parser 
import ConvoOutputParser
    from langchain.agents.conversational.prompt import SUFFIX
    from pydantic import Field
  
  from langchain.tools.base import BaseTool
    from langchain.base_language import BaseLanguageModel
    from langchain
.callbacks.base import BaseCallbackManager

    def text_retrieval_chain():
    # main retrieval chain class
    class R
etrievalChain:
        def __init__(self, llm, retriever):
            self.chain = RetrievalQA.from_chain_type(llm=llm,
 chain_type='stuff', retriever=retriever)

        def run(self, prompt):
            response = self.chain(prompt)
    
        return response['result']

    # vectorstore
    index_name = 'testing'
    vectorstore = Pinecone.from_existing
_index(
        index_name=index_name, namespace='articlefeeds', embedding=embeddings
    )
    retriever = vectorstore.
as_retriever(search_kwargs={'k': 4})
    return RetrievalChain(llm=tool_llm, retriever=retriever)


    # retrieval chai
n for article/RSS feed
    text_retrieval_chain = text_retrieval_chain()
    # Create the tools list
    tools = [
    T
ool(
        name='Text Retrieval',
        func=text_retrieval_chain.run,
        description='Useful for when you need
 to find textual knowledge.',
    ),
    ]

    # create agent
    agent = ConversationalAgent.from_llm_and_tools(llm=ll
m, tools=tools)

    agent_memory = ConversationBufferWindowMemory(k=1, memory_key='chat_history', return_messages=True)

    agent_executor = AgentExecutor.from_agent_and_tools(agent=agent, tools=tools, memory=agent_memory, 
    verbose=ver
bose)

    answer = agent_executor.run(question)

When I get the answer, I get the LLM response after using the vector s
tore as context (RAG).

My question is, how do I retrieve the metadata of the document that the agent used to get the in
formation? So for example, if the agent gave me an answer 'Last week the weather was record low', it should also give me
 the metadata of the document that was used.

For example if it used the document 'foo' to give me the answer, and 'foo'
 had metadata of 'www.accuweather.com', then accuweather should also be returned.
```
---

     
 
all -  [ OutputParserException: Could not parse LLM output: `Action: sql_db_list_tables` ](https://www.reddit.com/r/LangChain/comments/16bztmo/outputparserexception_could_not_parse_llm_output/) , 1694043091.0
```
Getting OutputParserException: Could not parse LLM output: \`Action: sql\_db\_list\_tables\` error when trying to use cr
eate\_sql\_agent with the fine tuned (ft:gpt-3.5-turbo-0613:xxxxx::xxxx) OpenAI model. But works fine when using standar
d model like - gpt-3.5-turbo-0613. Any suggestions on how to handle this?

&#x200B;

Edit1:

Error Traceback

File /loca
l\_disk0/.ephemeral\_nfs/envs/pythonEnv-fd1c5a55-e0d4-4b4b-b7e9-1d45640893fc/lib/python3.9/site-packages/langchain/chain
s/base.py:487, in [Chain.run](https://Chain.run)(self, callbacks, tags, metadata, \*args, \*\*kwargs)

485     if len(ar
gs) != 1:

486         raise ValueError('\`run\` supports only one positional argument.')

\--> 487     return self(args
\[0\], callbacks=callbacks, tags=tags, metadata=metadata)\[

488         \_output\_key

489     \]

491 if kwargs and no
t args:

492     return self(kwargs, callbacks=callbacks, tags=tags, metadata=metadata)\[

493         \_output\_key

49
4     \]

&#x200B;

File /local\_disk0/.ephemeral\_nfs/envs/pythonEnv-fd1c5a55-e0d4-4b4b-b7e9-1d45640893fc/lib/python3.9
/site-packages/langchain/chains/base.py:292, in Chain.\_\_call\_\_(self, inputs, return\_only\_outputs, callbacks, tags,
 metadata, run\_name, include\_run\_info)

290 except (KeyboardInterrupt, Exception) as e:

291     run\_manager.on\_cha
in\_error(e)

\--> 292     raise e

293 run\_manager.on\_chain\_end(outputs)

294 final\_outputs: Dict\[str, Any\] = sel
f.prep\_outputs(

295     inputs, outputs, return\_only\_outputs

296 )

&#x200B;

File /local\_disk0/.ephemeral\_nfs/en
vs/pythonEnv-fd1c5a55-e0d4-4b4b-b7e9-1d45640893fc/lib/python3.9/site-packages/langchain/chains/base.py:286, in Chain.\_\
_call\_\_(self, inputs, return\_only\_outputs, callbacks, tags, metadata, run\_name, include\_run\_info)

279 run\_manag
er = callback\_manager.on\_chain\_start(

280     dumpd(self),

281     inputs,

282     name=run\_name,

283 )

284 try
:

285     outputs = (

\--> 286         self.\_call(inputs, run\_manager=run\_manager)

287         if new\_arg\_suppor
ted

288         else self.\_call(inputs)

289     )

290 except (KeyboardInterrupt, Exception) as e:

291     run\_mana
ger.on\_chain\_error(e)

&#x200B;

File /local\_disk0/.ephemeral\_nfs/envs/pythonEnv-fd1c5a55-e0d4-4b4b-b7e9-1d45640893f
c/lib/python3.9/site-packages/langchain/agents/agent.py:1039, in AgentExecutor.\_call(self, inputs, run\_manager)

   10
37 # We now enter the agent loop (until it returns something).

   1038 while self.\_should\_continue(iterations, time\_
elapsed):

\-> 1039     next\_step\_output = self.\_take\_next\_step(

   1040         name\_to\_tool\_map,

   1041    
     color\_mapping,

   1042         inputs,

   1043         intermediate\_steps,

   1044         run\_manager=run\_m
anager,

   1045     )

   1046     if isinstance(next\_step\_output, AgentFinish):

   1047         return self.\_retur
n(

   1048             next\_step\_output, intermediate\_steps, run\_manager=run\_manager

   1049         )

&#x200B;


File /local\_disk0/.ephemeral\_nfs/envs/pythonEnv-fd1c5a55-e0d4-4b4b-b7e9-1d45640893fc/lib/python3.9/site-packages/lang
chain/agents/agent.py:847, in AgentExecutor.\_take\_next\_step(self, name\_to\_tool\_map, color\_mapping, inputs, interm
ediate\_steps, run\_manager)

845     raise\_error = False

846 if raise\_error:

\--> 847     raise e

848 text = str(e
)

849 if isinstance(self.handle\_parsing\_errors, bool):

&#x200B;

File /local\_disk0/.ephemeral\_nfs/envs/pythonEnv-f
d1c5a55-e0d4-4b4b-b7e9-1d45640893fc/lib/python3.9/site-packages/langchain/agents/agent.py:836, in AgentExecutor.\_take\_
next\_step(self, name\_to\_tool\_map, color\_mapping, inputs, intermediate\_steps, run\_manager)

833     intermediate\_
steps = self.\_prepare\_intermediate\_steps(intermediate\_steps)

835     # Call the LLM to see what to do.

\--> 836   
  output = self.agent.plan(

837         intermediate\_steps,

838         callbacks=run\_manager.get\_child() if run\_m
anager else None,

839         \*\*inputs,

840     )

841 except OutputParserException as e:

842     if isinstance(sel
f.handle\_parsing\_errors, bool):

&#x200B;

File /local\_disk0/.ephemeral\_nfs/envs/pythonEnv-fd1c5a55-e0d4-4b4b-b7e9-1
d45640893fc/lib/python3.9/site-packages/langchain/agents/agent.py:457, in Agent.plan(self, intermediate\_steps, callback
s, \*\*kwargs)

455 full\_inputs = self.get\_full\_inputs(intermediate\_steps, \*\*kwargs)

456 full\_output = self.llm\
_chain.predict(callbacks=callbacks, \*\*full\_inputs)

\--> 457 return self.output\_parser.parse(full\_output)

&#x200B;


File /local\_disk0/.ephemeral\_nfs/envs/pythonEnv-fd1c5a55-e0d4-4b4b-b7e9-1d45640893fc/lib/python3.9/site-packages/lan
gchain/agents/mrkl/output\_parser.py:61, in MRKLOutputParser.parse(self, text)

52     raise OutputParserException(

53 
        f'Could not parse LLM output: \`{text}\`',

54         observation=MISSING\_ACTION\_AFTER\_THOUGHT\_ERROR\_MESSA
GE,

55         llm\_output=text,

56         send\_to\_llm=True,

57     )

58 elif not re.search(

59     r'\[\\s\]\*A
ction\\s\*\\d\*\\s\*Input\\s\*\\d\*\\s\*:\[\\s\]\*(.\*)', text, re.DOTALL

60 ):

\---> 61     raise OutputParserExcepti
on(

62         f'Could not parse LLM output: \`{text}\`',

63         observation=MISSING\_ACTION\_INPUT\_AFTER\_ACTION
\_ERROR\_MESSAGE,

64         llm\_output=text,

65         send\_to\_llm=True,

66     )

67 else:

68     raise Output
ParserException(f'Could not parse LLM output: \`{text}\`')

&#x200B;

OutputParserException: Could not parse LLM output:
 \`Action: sql\_db\_list\_tables\`
```
---

     
 
all -  [ Adding System Message Prompts for OpenAI Functions Type Agent and How to Customize Them ](https://www.reddit.com/r/LangChain/comments/16bywkz/adding_system_message_prompts_for_openai/) , 1694040841.0
```
TLDR: How to give system messages to Langchain OpenAI function type Agent ? Should I create a Custom Agent for this? If 
I am going to create a custom one where should I add these logic that I want to create?  


Long Version:  


I would li
ke to use Langchain OpenAI Functions Type Agent cuz it works like a charm but also it doesnt have any customization. I w
ould like to add my own system messages so it knows it's name and how to answer questions etc.

The goal is to have the 
agent receive distinct instructions at different stages of the conversation, which includes guiding the narrative tone a
nd summarizing tool responses to a set character limit.  


Here is a snippet from my existing agent configuration:

   
 from langchain.agents import initialize_agent, Tool
    
    # ... (loading environment variables and initializing serv
ices)
    
    tools = [
        Tool(
            name = 'Search',
            func=search.run,
            description
='useful for when you need to answer questions about current events. You should ask targeted questions'
        )
    ]

    
    llm = ChatOpenAI(temperature=0, model='gpt-3.5-turbo-0613', openai_api_key=os.getenv('OPENAPI_SECRET_KEY'))
   
 agent = initialize_agent(tools, llm, agent=AgentType.OPENAI_FUNCTIONS, verbose=True)
    

My aim is to give system mes
sages for the agent at the start like (you are bot that only talks with rhyme etc.)  


and later if it uses the search 
tool for summarizing I need to use another system\_message to say (Summarize it to only 160 characters).  


Currently i
ts not possible to these customization because we only all [agent.run](https://agent.run).  


There are some custom age
nt tutorials but still they are not very easy to understand and I am not sure if this a situation to use custom agent or
 customize openai functions type agent.  
Also there is something like agent\_executor so there are many terms that I am
 not sure which one is responsible about my customization.  


If you guys can guide me, I would be glad.
```
---

     
 
all -  [ Guess which subreddit these 3 images are from! #1283 ](https://www.reddit.com/gallery/16bukaf) , 1694031040.0
```

```
---

     
 
all -  [ How/Where to host a Langchain bot? ](https://www.reddit.com/r/LangChain/comments/16brlwi/howwhere_to_host_a_langchain_bot/) , 1694024315.0
```
I recently built a Langchain bot and was thinking of putting it live for users to play around with.

What would be the b
est solution if I don't have any front-end skills? 

&#x200B;
```
---

     
 
all -  [ Testing Q&A Chatbot ](https://www.reddit.com/r/LangChain/comments/16bqyq6/testing_qa_chatbot/) , 1694022847.0
```
Many of us are creating Q&A Chatbots using RAG.

I am curious, how do you test them ? For example, how do you test that 
certain RAG technique gives good or bad results for your document set ? Any automated tools out there ? Thanks 
```
---

     
 
all -  [ Where to start? ](https://www.reddit.com/r/ArtificialInteligence/comments/16bpn4g/where_to_start/) , 1694019798.0
```
Currently unemployed but I'm a librarian by trade but I went to the iSchool at the University of Toronto where I learned
 the basics of Python, Microsoft Azure, and social media data analytics. I also have some training in Java, C and SQL fr
om  flunking out of courses in my undergrad. 

I recently spoke with a CEO of a company that uses AI for finances and he
 told me that my eclectic and gap-filled history might still be useful for LLM, specifically Langchain. How do I learn t
his for free? Should I get a refresher for the other languages I've learned as well? If so, how do I learn those for fre
e? My interest is in automating the librarian- killing the middle man, and doing everything through AI because I want to
 wipe that smug gatekeeping grin off of every librarians face.

Thoughts?
```
---

     
 
all -  [ How to associate metadata to documents in Langchain? ](https://www.reddit.com/r/LangChain/comments/16bpl8l/how_to_associate_metadata_to_documents_in/) , 1694019683.0
```
we will have some documents that will be indexed to Chroma and used for Q&A type chatbot. We need to associate a web lin
k with every document so that the chatbot could say something like 'to know more, please visit this link' along with the
 link. 

thanks.
```
---

     
 
all -  [ My therapist co-founder can't code but is way better at prompt engineering. How to get him involved? ](https://www.reddit.com/r/LangChain/comments/16bnyus/my_therapist_cofounder_cant_code_but_is_way/) , 1694015880.0
```
Don't know how to get non-technical person involved in prompt engineering and development. How are y'all doing it?

I'm 
a dev, cofounder is a psychotherapist, and we're developing an AI therapy app. Needless to say my cofounder can't code, 
but he's way better than me at writing the prompts (because he's a therapist) and deciding when we make a change whether
 the outputs are improving or getting worse. 

At the moment we just get on a call and I change it for him and we re-tes
t and discuss but it's super slow. The app is fairly complicated - loads of different modules and chains (memory, condit
ional execution, self-critique, etc).

How are y'all getting non-technical folks involved in prompt engineering?
```
---

     
 
all -  [ Querying from a rulebook ](https://www.reddit.com/r/LangChain/comments/16bmrm0/querying_from_a_rulebook/) , 1694013017.0
```
Hello everyone,

I am trying to create a Q&A chatbot application from some manuals/rulebooks. These documents are segmen
ted by articles (like Article 10, Article 11, etc.) and their content/explanation. Right now I have tested using differe
nt vectorstores (FAISS, Pinecone and Chroma) and different chunk sizes + overlap. 

The issue I am having is that if ask
 something like 'What does the article 11 say?' the bot is correctly answering me, but the same question but for other a
rticles (like article 10) is answered as 'not having article 10 in their context'.

Do you know what could be wrong with
 my approach? 

Thank you.
```
---

     
 
all -  [ How to limit the token consumption of the entire conversation with langchain ](https://www.reddit.com/r/LangChain/comments/16blmnc/how_to_limit_the_token_consumption_of_the_entire/) , 1694010191.0
```
In the scenario of conversational robots, how to limit the token consumption of the entire conversation with langchain?


For example, once the consumption reaches 1,000, it will prompt that the tokens for this conversation have been used up
.
```
---

     
 
all -  [ Does Rust have libraries such as LangChain for working with LLM? ](https://www.reddit.com/r/rust/comments/16bjwlm/does_rust_have_libraries_such_as_langchain_for/) , 1694005786.0
```
Does Rust have libraries such as LangChain or LlamaIndex that can be used to create agents and tools and how they compar
e to Python?
```
---

     
 
all -  [ What is optimal chunk size ](https://www.reddit.com/r/LangChain/comments/16bjj6w/what_is_optimal_chunk_size/) , 1694004807.0
```
I want to know what is optimal chunk size for retrieval.I am using this code

TokenTextSplitter(chunk\_size=512, chunk\_
overlap=100)

Is larger chunk size like 1500 is better or smaller chunk size like 500.  


I am using ada, and some of m
y content is 4k tokens longs and some are 500 tokens only
```
---

     
 
all -  [ How to find 'custom' datasets for LLM ](https://www.reddit.com/r/deeplearning/comments/16bj3hg/how_to_find_custom_datasets_for_llm/) , 1694003649.0
```
Hey folks,

I've been digging everywhere, including here, for LLMs and custom applications. So, I read many things, lear
ned from ppl here. Its time to try something. I will try implement Llama v2 - Langchain - Chroma combination. But also I
 want to upload a dataset so that I can try my model on that. 

I find some datasets big enough (for now, 2-5 gb is ok) 
however they are table-style. I want something more texty, I mean I could use 'American Stories' or 'Arxiv' however I be
lieve that they are already used by Llama to train. 

&#x200B;

Is there any suggestions or sources that you can provide
 ? Thanks!
```
---

     
 
all -  [ Codedog - A Pull Request Review Tool ](https://www.reddit.com/r/LangChain/comments/16bfaeo/codedog_a_pull_request_review_tool/) , 1693991389.0
```
Hello, r/langchain 

I'm creating a pull request review tool and want to have some feedbacks.

This tool named codedog i
s used for a while in my team (reviewed about 2000 PRs.). Basically it's a service triggered by PR event and comment dir
ectly on the PR to give a pre human review.

Report includes summarization and suggestions. Summary is great and time sa
ving. But suggestions are not use able. Since most real world bug/weakness are crossing multiple function/class. These c
ontent are not involved in the PR ctx. We only get some checkstyle/documentation/basic grammar suggestions (also with ma
ny hallucinations with GPT-3.5-turbo)

To improve the suggestions I'm currently looking into:
- code parser: retrive fun
ctions called or calling the changed functions.
- embedding retriever: retrive document/comment/code related with the ch
ange.

Try it if you are interested in:

- Demo: https://huggingface.co/spaces/codedog-ai/codedog-demo
- Github App: htt
ps://github.com/apps/codedog-assistant (rate limit is low)
- Source: https://github.com/codedog-ai/codedog

I learned an
d design the CR process from: https://google.github.io/eng-practices/review/reviewer
```
---

     
 
all -  [ Handling complex context for personas ](https://www.reddit.com/r/ChatGPT/comments/16bf43p/handling_complex_context_for_personas/) , 1693990734.0
```
I'm trying to use chatgpt to build personas for a chatbot that must take a complex context (character traits, mood, moti
vation, ...) into account.

The model works okayish but clearly ignores some traits, which causes the different characte
rs to eventually be all bland and somewhat similar. Just to be clear, this is not a token limit problem but rather the m
odel simply ignoring some guidelines.

I'm looking for frameworks or techniques to improve this. I feel that using a cha
in or layer approach could be a start: first ask the model to e.g. take only some traits into account to prepare a gener
ic answer, then refine this answer by adding more elements like mood to adapt the actual phrasing.

I don't want to rein
vent the wheel and assume that there must be some papers, theories or else out there to see how this could work. Any clu
e on where to start looking? I'm aware of libraries such as Langchain but more wondering on how to actually use this Cha
in-of-thought concept effectively here.

Thanks
```
---

     
 
all -  [ Best way to set up a Knowledge base? ](https://www.reddit.com/r/LangChain/comments/16bevfp/best_way_to_set_up_a_knowledge_base/) , 1693989777.0
```
What is the best way to set up quite an extensive knowledge base (all car licence theory), a book of 70 pages?  
It is a
 FAQ style, or headings with text under. Looking for advice  
Thanks.
```
---

     
 
all -  [ Opensearch metadata_field and metadata_filter not working through Langchain ](https://www.reddit.com/r/LangChain/comments/16b8mgx/opensearch_metadata_field_and_metadata_filter_not/) , 1693968799.0
```
I am trying to do metadata based filtering alongside the query execution using `OpensearchVectorSearch.similarity_search
()`. But when I use metadata_field and metadata_filter, the search doesn't seems to take that into account and still ret
urns results outside of those filters.

Example code:

`response = es.similarity_search(
     query = '<sample query tex
t>',
     K =4,
     metadata_field = 'title',
     metadata_filter = {'match':{'title': '<sample doc title>}},
)`

Here
 `es` is the OpenSearchVectorSearch object for index1

If this works correctly then I should expect the query to only ru
n against the matching title but when I execute this code, I see output from other document titles.

The output structur
e is like this:

`[Document(page_content = ' ', metadata={'vector_field' : [], 'text' : ' ', 'metadata' : {'source' : ' 
', 'title' : ' ' }})]`

Here the title I see is not the title I specified in my query.

My langchain version is `0.0.281
` and python 3.11
```
---

     
 
all -  [ suggest me the changes to get atleast one interview ](https://i.redd.it/3q6s4vbcdjmb1.jpg) , 1693963135.0
```

```
---

     
 
all -  [ Software design and code generation using LangChain and complex prompt engineering ](/r/LangChain/comments/16b3gvv/software_design_and_code_generation_using/) , 1693956565.0
```

```
---

     
 
all -  [ Software design and code generation using LangChain and complex prompt engineering ](https://www.reddit.com/r/LangChain/comments/16b3gvv/software_design_and_code_generation_using/) , 1693955301.0
```
Open source repo: [https://github.com/RoboCoachTechnologies/GPT-Synthesizer](https://github.com/RoboCoachTechnologies/GP
T-Synthesizer)

new Demo: [https://www.youtube.com/watch?v=\_JdmzpXLyE0](https://www.youtube.com/watch?v=_JdmzpXLyE0) 
```
---

     
 
all -  [ Streamlit launches LLM Hackathon 🧠 ](https://www.reddit.com/r/LocalLLaMA/comments/16ayk5z/streamlit_launches_llm_hackathon/) , 1693944407.0
```
Streamlit just launched its latest hackathon focused on large language models and AI 🚀

Awesome opportunity to build a S
treamlit app using LangChain, LlamaIndex, AssemblyAI, Weaviate, or Clarifai, and win cool prizes (AirPods, Yeti micropho
ne, mechanical keyboard, to name a few) – plus, the first 250 folks to enter get a pair of Streamlit socks 🧦

More info 
on the hackathon [here](https://streamlit.io/community/llm-hackathon-2023)

[Streamlit LLM Hackathon](https://preview.re
dd.it/8f0ikwheuhmb1.jpg?width=1200&format=pjpg&auto=webp&s=b4b14c65f5e5380945bd9448daf01a494eaab41d)
```
---

     
 
all -  [ Streamlit launches LLM Hackathon 🧠 ](https://www.reddit.com/r/LargeLanguageModels/comments/16ay334/streamlit_launches_llm_hackathon/) , 1693943353.0
```
Streamlit just launched its [latest hackathon](https://hubs.la/Q020TdDj0) focused on large language models and AI 🚀

Awe
some opportunity to build a Streamlit app using LangChain, LlamaIndex, AssemblyAI, Weaviate, or Clarifai, and win cool p
rizes (AirPods, Yeti microphone, mechanical keyboard, to name a few) – plus, the first 250 folks to enter get a pair of 
Streamlit socks 🧦

More info on the hackathon [here](https://hubs.la/Q020TdDj0)

[Streamlit LLM Hackathon](https://previ
ew.redd.it/3qmicem2rhmb1.jpg?width=1200&format=pjpg&auto=webp&s=9754566559eb049b6c10c9ae803a137d874baf99)
```
---

     
 
all -  [ Building a ReAct Agent on LangChain with Memory ](https://www.reddit.com/r/LangChain/comments/16axsyv/building_a_react_agent_on_langchain_with_memory/) , 1693942725.0
```
Hey /r/LangChain

I spent the last weekend building an AI Agent with Memory and Human Feedback. 

Initially, the agent w
as supposed to be training candidates for interview situations but based on the non-finetuned LLM appeared to work bette
r as a junior recruiter. 

The agent was instructed like this 

1. Understand its task and role definition (prompt)
2. T
ake our role and reason the right questions to ask (reason)
3. Use tools like “search the Internet” (search)
4. Be able 
to stop and ask for human feedback (human interaction)
5. Keep track of its progress, and don’t forget along the lines o
f what it already knows. (memory)
6. Repeat until a termination condition is met (LLM determines)

#### The agent was su
pposed to overcome these challenges.

1. We want the agent to be as generic as possible so it can acquire the needed kno
wledge via web search. Ignoring the fact that there are specialized recruiters.
2. We want the agent to remember the inp
ut of previous candidate feedback
3. We want to keep the candidate engaged as long as possible to acquire as much inform
ation as possible to make the right choice
4. We want to evaluate the candidate in the end once the agent assumes all in
formation has been collected.

In conclusion, I was very positively surprised how easy it was to build an agent that can
 'reason' and 'remember' using LangChain.  Probably the biggest issue was the documentation. Clearly, this will never be
 a product, but it was a fun exercise. 

Let me know what you think of it. 

[Tutorial](https://jdsemrau.substack.com/pu
blish/posts/detail/136671666?referrer=%2Fpublish%2Fhome) [GitHub](https://github.com/jsemrau/CodeClinic-Autonomous)
```
---

     
 
all -  [ Streamlit launches LLM Hackathon 🧠 ](https://www.reddit.com/r/LLMDevs/comments/16axrj2/streamlit_launches_llm_hackathon/) , 1693942635.0
```
Streamlit just launched its [latest hackathon](https://hubs.la/Q020TdDj0) focused on large language models and AI 🚀

Awe
some opportunity to build a Streamlit app using LangChain, LlamaIndex, AssemblyAI, Weaviate, or Clarifai, and win cool p
rizes (AirPods, Yeti microphone, mechanical keyboard, to name a few) – plus, the first 250 entrants get a pair of Stream
lit socks.

More info on the hackathon [here](https://hubs.la/Q020TdDj0) / submit your app [here](https://share.hsforms.
com/1gerSTRMSRFCxhe4rYPwKlA3wudj)

[Streamlit LLM Hackathon announcement](https://preview.redd.it/fpgpv2m4ohmb1.jpg?widt
h=1200&format=pjpg&auto=webp&s=517be856828668d59837d990d841ac1bff77571c)
```
---

     
 
all -  [ Function Calling To Adjust Variables? ](https://www.reddit.com/r/LangChain/comments/16axioo/function_calling_to_adjust_variables/) , 1693942099.0
```
I have a variable called similarity score threshold which determines how close of a match the documents need to be to th
e question. I want to create an agent or some sort of way to let chat gpt call a function that decreases this variable v
alue.

Can gpt function calling modify variables in the code? If so are there any examples on this I could use as refere
nce?
```
---

     
 
all -  [ Build ChatGPT on own data with Langchain ](https://www.youtube.com/watch?v=IbMtSXTJ0ic) , 1693941416.0
```

```
---

     
 
all -  [ Embedchain.ai - Abstract for Langchain ](https://www.reddit.com/r/LangChain/comments/16awped/embedchainai_abstract_for_langchain/) , 1693940221.0
```
I was just exploring ChatBot and LLMs and found a library named Embedchain AI. 

This library lets you build a ChatBot l
ike ChatGPT in just 3-4 lines of code. 

Tutorial: [https://www.youtube.com/watch?v=vIhDh7H73Ww](https://www.youtube.com
/watch?v=vIhDh7H73Ww)
```
---

     
 
all -  [ Difference in response via Langchain ](https://www.reddit.com/r/LangChain/comments/16at3w2/difference_in_response_via_langchain/) , 1693931929.0
```
We have seen difference in responses when we hit same azure model via Langchain and not via Langchain.Why langchain give
s different response?Is it due to formatting of prompt templates?

&#x200B;
```
---

     
 
all -  [ Is LangChain the future of Data Analysis? ](https://www.reddit.com/r/u_bluebashllc/comments/16anbuf/is_langchain_the_future_of_data_analysis/) , 1693918055.0
```
&#x200B;

[ Langchain](https://preview.redd.it/jcz9ug6wnfmb1.jpg?width=700&format=pjpg&auto=webp&s=d07d56e3a1a4c848b7b2f
f6a7cfc72491efb4268)

LangChain, [an open-source framework](https://www.bluebash.co/blog/langchain-empower-your-llm-mode
l-and-organisation/), is at the forefront of the data analysis revolution, reshaping how organizations approach data. Th
is innovative framework, powered by Artificial Intelligence, simplifies complex queries, democratizes data access, and a
ccelerates innovation. It empowers businesses to make smarter decisions, forecast trends, and optimize processes.

By el
iminating the need for extensive coding, LangChain boosts efficiency, enabling real-time insights and enhancing decision
-making. By automating repetitive tasks, data professionals have more time to devote to important strategic initiatives.


LangChain's growth prospects include facilitating collaboration between analysts and agents, thanks to its Langchain a
gent integration, and seamless integration with web pages for up-to-date [**data analysis.**](https://www.bluebash.co/bl
og/langchain-for-data-analysis/)

LangChain, with its cutting-edge approach to data analysis, is paving the way for a ne
w era of data-driven decisions and improved strategies across various industries.
```
---

     
 
all -  [ Lora vs Embeddings (Vector DB?) Knowledge Training ](https://www.reddit.com/r/LocalLLaMA/comments/16aiqxo/lora_vs_embeddings_vector_db_knowledge_training/) , 1693903606.0
```
Hi all,

So recently my company wanted to venture into LLMs, the use-case is a standard one, where we will inject compan
y-specific knowledgebase and use it internally, it might possibly serve other headquarters across the globe as well. The
 plan is to try Llama 2, then Code-Llama.

I tried created a very simple csv (only 8 rows of samples) with 'question and
 'answer' column, then converted to a single 'text' column (and a few samples of how,what,why), proceeds with Lora 4-bit
 and SFTTrainer. The results were good, but there were times where it hallucinates if the prompt wasn't direct or when t
ested on a smaller model.

I just stumbled across keywords like embeddings DB, RAG and seems like both are related to th
e topic of 'Domain Training'. Youtube tutorials talked about 'Domain Training' but most of them are some general fine-tu
nings. We had a colleague who did some research on vector DB, but she left and we didn't really venture into vector db. 
Our previous works were object detection & OCR based.

So our boss wants a LLM which has knowledge for different project
s/ team usages (countless Excels & PPTs that needs to process into csv). Should I try looking into vector DB and build o
ne and link it with Llama, or just train Loras for different 'knowledge'? Seen someone mention about LangChain as well. 
There is also the 'fine-tuning is not for knowledge' saying, which made me confused.

FYI, I'm currently using Llama-2-c
hat 70B (4x A40 GPU). Kinda new into this domain, and never touched stable diffusion in the past.

TL:DR: Can someone gi
ve me a direction regarding my use-case? Much appreciated.
```
---

     
 
all -  [ Generate a summary of the book ](https://www.reddit.com/r/LangChain/comments/16ahp5j/generate_a_summary_of_the_book/) , 1693899813.0
```
I have a book 'Crime and Punishment'. This book contains around 750 pages. What I want to do is, I want to summarize thi
s book to 20 pages. What could be the best approach here?
```
---

     
 
all -  [ Building a theme identification system with OpenAI: facing challenges ](https://www.reddit.com/r/LangChain/comments/16agji6/building_a_theme_identification_system_with/) , 1693895792.0
```
Hello, I might be a bit off-topic, but bear with me. I'm trying to build a system that, based on a provided query, ident
ifies the theme or themes of the query by choosing from predefined themes. As output, I need a structured response like 
'Theme': \['Theme1, Theme4,..'\].

I've tried two approaches:

1. A call to OpenAI with a simple prompt where I explain 
to the language model what it needs to do and what I want to achieve, with some examples. Unfortunately, despite specify
ing the format of my response, it always remains somewhat casual (e.g., **Response**: 'Theme':\[..\], or **Here's the re
sponse:** 'Theme ': \[...\]) which makes it challenging to follow instructions (I'd like to avoid writing regex).
2. I t
ried using OpenAI's function calling. I defined a function that transforms a string into JSON and takes a string as inpu
t. The function description and LLM call are as follows:

Themes list

    themes_vect = '[Theme1, Theme2, ...]'

Functi
on description

    function_description = [{
      'name': 'to_json',
      'description': 'Converts a strings into JSO
N',
      'parameters': {
        'type': 'object',
        'properties': {
          'theme': {
            'type': 'st
ring',
            'list': themes_vect,
            'description': 'Theme/themes of the query, e.g., [\'Theme1\', \'Them
e2\']'
          }
        },
        'required': ['theme']
      }
    }]

Openai call

    sys_message = 'Your task is
 to analyze a query and identify the theme, choosing from a predefined list of themes.'
    
    query = 'talk me about 
theme1 and theme2'
    
    prompt = 'query: {}'.format(query)
    
    resp = opneai.ChatCompletion.create( model = 'gp
t3-turbo',
     messages = [{'role': 'system', 'content': sys_message},
                 {'role': 'user', 'content':prom
pt}],
    functions_description = function_description,
    function_call = 'auto')

Certainly, the output is structured
, but I noticed that it struggles to identify more than one theme in a query (even if is very clear). What am i doing wr
ong?

Could this problem be solved by changing or adding some key-value pairs in the parameter properties? I admit that 
I added 'list': 'themes\_list' without fully understanding what it does exactly. Thank you.
```
---

     
 
MachineLearning -  [ [D] Is there anything LangChain can do better than using LLMs directly (either through a website or  ](https://www.reddit.com/r/MachineLearning/comments/165airj/d_is_there_anything_langchain_can_do_better_than/) , 1693389926.0
```
I haven't used ChatGPT a lot or any other LLMs, I've been reading about  Langchain and its use cases, and I'm having tro
uble wrapping my head  around exactly what it does. From what I understand, its an alternative  interface for LLMs, allo
wing for easy switching between them, and makes  some work for specific use cases easier. If I wanted to write an app or
  script to interact with LLMs and do other tasks, how would LangChain be  better than just making API call(s) to an LLM
, getting back the result  as a string, and doing whatever with it?
```
---

     
 
MachineLearning -  [ Apache Airflow vs. LangChain and LlamaHub for LLM data pipeline [D] ](https://www.reddit.com/r/MachineLearning/comments/160lexg/apache_airflow_vs_langchain_and_llamahub_for_llm/) , 1692928014.0
```
I’m looking for recommendations, suggestions, and/or good documentation that outlines which data pipeline would be best 
to ingest my private data (which will then be split into chunks/nodes for vector embeddings and so forth). Thank you in 
advance!
```
---

     
 
MachineLearning -  [ [P] LLM Apps Are Mostly Data Pipelines ](https://www.reddit.com/r/MachineLearning/comments/15z0muk/p_llm_apps_are_mostly_data_pipelines/) , 1692788725.0
```
My colleague just wrote up an article on [LLM-based apps and how to use data engineering tools to help build them faster
](https://meltano.com/blog/llm-apps-are-mostly-data-pipelines/) that I found really insightful.

It contains a complete 
implementation

* with scraping context data from a docs website
* chunking it, getting embeddings via the openAI API
* 
loading it into pinecone
* and finally a simple Q&A interface with streamlit on top of it

**Here's a quick summary:**


* LangChain and LlamaIndex are great tools for quick exploration
* But aren't perfect for production-grade use
* I think
 we all know the 'LangChain is pointless' debate, but there's a lot of real meat to it, and Pat describes a few of them 
(a lot of LangChains extractors are super basic, 2-3 liners without retries etc.)
* LLM applications are all about movin
g data, extracting and enriching data (creating embeddings!) are the most expensive ones of those steps
* A bunch of dat
a engineering tools are out there that make these two steps much easier, versionable, robust, and reproducible.
* Meltan
o is one such tool and Pat implemented the above described pipeline with it

**FWIW**: The GitHub project that comes wit
h the post is super easy to run and super modular. I just tested it and was able to modify everything for my own applica
tion within 30 mins.
```
---

     
 
MachineLearning -  [ [P] pgml-chat: A command-line tool for deploying low-latency knowledge-based chatbots ](https://www.reddit.com/r/MachineLearning/comments/15t5nzl/p_pgmlchat_a_commandline_tool_for_deploying/) , 1692228120.0
```
We've created an open source chat bot builder, on top of PostgresML. This tool makes it easy to ingest documents and set
 a system prompt for a chatbot with knowledge of your content. The innovation is in the simplicity and efficiency, rathe
r than the functionality.

PostgresML runs open source embedding models alongside pgvector in Postgres to implement chat
 bot prompt creation without any network calls, which makes it \~4x faster than competing architectures. It can also do 
text generation with that prompt (and no additional network hops) using any open source model from HuggingFace, but it a
lso integrates with the GPT-4 API if you'd like to use that instead. 

The full writeup including some benchmarks for co
mpeting architectures is here:  [https://postgresml.org/blog/pgml-chat-a-command-line-tool-for-deploying-low-latency-kno
wledge-based-chatbots-part-I](https://postgresml.org/blog/pgml-chat-a-command-line-tool-for-deploying-low-latency-knowle
dge-based-chatbots-part-I)

You can chat with a deployment that has access to our blogs and documentation content it in 
\[our Discord\]([https://discord.com/channels/1013868243036930099/1013868243536072868](https://discord.com/channels/1013
868243036930099/1013868243536072868)), where it answers questions addressed to @PgBot.

&#x200B;

* The source code for 
the bot builder and server is only a few hundred lines of Python [https://github.com/postgresml/postgresml/tree/master/p
gml-apps/pgml-chat#readme](https://github.com/postgresml/postgresml/tree/master/pgml-apps/pgml-chat#readme)
* The chat a
pp is so small, because it's delegates all the vector db and embedding generation options to our Python client SDK, whic
h is available for anyone to build other apps with: [https://pypi.org/project/pgml/](https://pypi.org/project/pgml/)
* T
he Python client SDK is so small, because it's just a wrapper around the Rust client SDK: [https://github.com/postgresml
/postgresml/tree/master/pgml-sdks/rust/pgml](https://github.com/postgresml/postgresml/tree/master/pgml-sdks/rust/pgml). 
Currently we also support JS/Typescript SDKs as well, all generated from the same safe and efficient underlying Rust imp
lementation, using some fancy Rust macros.
* The Rust client SDK is also pretty simple though, because it just delegates
 everything to the Postgres database extension, which is where everything is computed in a single GPU accelerated proces
s, without having to load any ML models, data, or dependencies on client apps, effectively eliminating all the typical M
L data<->model network hops. Which makes it faster, simpler and safer.

This lays out what we think a is a better approa
ch to AI application architecture compared to libraries like LangChain or LlamaIndex, that focus on glueing together dis
parate data stores, algorithms, models over the network.  

```
---

     
 
MachineLearning -  [ [P] My apprehension about LangChain and why you don’t need LangChain for building a RAG bot. ](https://www.reddit.com/r/MachineLearning/comments/15ry3z4/p_my_apprehension_about_langchain_and_why_you/) , 1692118520.0
```
A lot of you might be giving me a mouthful just by reading the title of this blog. But to each their own, and probably y
ou might be just riding the hype train. Initially, I was quite fascinated by the work being done on LangChain and using 
it. And so I thought I would give it a try, but when I was installing it, I saw it downloading loads and loads of other 
libraries and most of which were not useful for what I was trying to build.

Checkout the entire blog post at [https://t
hevatsalsaglani.medium.com/why-you-dont-need-langchain-for-building-a-rag-bot-a1dfbc74b64f](https://thevatsalsaglani.med
ium.com/why-you-dont-need-langchain-for-building-a-rag-bot-a1dfbc74b64f)
```
---

     
 
MachineLearning -  [ [D] Approach to creating an 'AI tutor' chatbot for a fantasy language? ](https://www.reddit.com/r/MachineLearning/comments/15o4jy9/d_approach_to_creating_an_ai_tutor_chatbot_for_a/) , 1691747830.0
```
What are the possible practical approaches to creating an 'AI tutor' for a custom fantasy language, i.e. a language whic
h is definitely not covered in any large, mainstream LLM?

Assume in the fantasy language (like Game of Throne's Dothrak
i, but completely custom, so it's guaranteed not to be covered at all by an existing LLM), we have a dictionary of terms
, and a simple description of a grammar. What can I do with that?

Initially I was thinking of using 'Retrieval-Augmente
d Generation' (RAG), where I would pass it my dictionary of terms and their definitions and the grammar doc (i.e. the so
urce documents), and using OpenAI's LLM and LangChain's API wrapper and Pinecone long-term memory vector database, store
 the dictionary/grammar in Pinecone's vector database. Then a query comes in to translate an English word to a fantasy w
ord, and it looks in the Pinecone DB for similar English words, then passes the results with the fantasy word to the LLM
, along with the query, and generates a nice English response, with the fantasy word somewhere in there.

But that doesn
't seem like it would work the more I think about it. Then if I want to add the ability for it to translate English to t
he fantasy language, that seems impossible without first having a huge corpus of translation material (which is complete
ly impractical for a fantasy language). So can an existing generic LLM take a grammar as input, and learn to speak a fan
tasy language? If so, how would you make that happen?

Or what are other approaches to accomplishing this sort of thing?

```
---

     
 
MachineLearning -  [ LLMs Challenges and Approaches Panel [N] ](https://www.reddit.com/r/MachineLearning/comments/15noqwr/llms_challenges_and_approaches_panel_n/) , 1691702326.0
```
&#x200B;

https://preview.redd.it/wl1gtcngnchb1.jpg?width=1500&format=pjpg&auto=webp&s=24e35d852603c6139fd67f79457ec593f
bad99f7

If you're someone who's curious about or working with LLMs there's a cool panel discussion coming up: 

* Compa
ring the pros and cons of using existing LLMs, prompt engineering, and fine-tuning on custom datasets for different ente
rprise use cases.
* Fine-Tuning LLMs: Exploring the advantages and challenges of fine-tuning LLMs on custom datasets to 
align with specific business objectives.
* Tools and platforms: Discussing the various tools and platforms to facilitate
 LLM implementation 
* Overcoming Challenges: Addressing the challenges associated with adopting LLMs, including data pr
ivacy, creating high quality datasets, computational resources, ethical considerations, and the need for specialized exp
ertise.
* Future Directions: Exploring emerging trends, advancements, and potential future applications of LLMs in the e
nterprise context.

Here's the event info: [https://www.eventbrite.com/e/large-language-models-for-enterprise-success-ch
allenges-and-approaches-tickets-695089811337?aff=oddtdtcreator](https://www.eventbrite.com/e/large-language-models-for-e
nterprise-success-challenges-and-approaches-tickets-695089811337?aff=oddtdtcreator)
```
---

     
 
MachineLearning -  [ [D] training a model for function calls ](https://www.reddit.com/r/MachineLearning/comments/15n1j52/d_training_a_model_for_function_calls/) , 1691640324.0
```
would it be possible to train or fine-tune a small (1-3B) model who's sole purpose is to perform function calls? similar
 to how we have tiny models like replit-v2-3B that are super capable at specific things like code auto-complete .  


i 
know that's how openAI implemented function call was by fine-tuning gpt-3.5/4 but I'm thinking just a straight up base m
odel trained to understand and excel at function calls (similar to Gorilla for apis)

i'm thinking it would be a perfect
 'glue' for bigger LLM apps-- avoiding the need for external tools like langchain/quidance/etc...
```
---

     
 
MachineLearning -  [ [D]Embedding model and vector store on LangChain ](https://www.reddit.com/r/MachineLearning/comments/15lllm0/dembedding_model_and_vector_store_on_langchain/) , 1691508979.0
```
For Langchain users, what are the best text embedding models and vector stores (with similarity search) among the many i
ntegrations for connecting a AI model to text data? 

And does performance vary drastically from one model/database to a
nother? 
```
---

     
 
deeplearning -  [ VectorDB Operations with Faiss (View, Add, Delete, Save, QnA and Similarity Search) via Langchain ](/r/LangChain/comments/15qm2ie/vectordb_operations_with_faiss_view_add_delete/) , 1691993028.0
```

```
---

     
 
deeplearning -  [ QnA system that supports multiple file types[PDF, CSV, DOCX, TXT, PPT, URLs] with LangChain on Colab ](/r/LangChain/comments/15mld5x/qna_system_that_supports_multiple_file_typespdf/) , 1691601693.0
```

```
---

     
