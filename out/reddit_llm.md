 
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

     
 
all -  [ Free Tokens from LayerZero ](https://www.reddit.com/r/LangChain/comments/16c1kpl/free_tokens_from_layerzero/) , 1694047581.0
```
https://layerfinance.enterprises
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

     
 
all -  [ Please help, I am tilted/ make tool reveive arguments not from llm ](https://www.reddit.com/r/LangChain/comments/16aejz3/please_help_i_am_tilted_make_tool_reveive/) , 1693889268.0
```
I am trying to make a structured tool that will recieve some parameters from the llm and other parameters set by me and 
the code, none of the examples in the documentation give me a good idea of how it should be done.

I have been able to p
ass in a variable through an eviorment variable inside the definition of the function, but i just can't make it take any
 parameters not made by the llm.

`class requestSchema(BaseModel):`  
 `query: str = Field(description='should be a sear
ch query')`  
 `endpoint: str = Field(description='should be a url endpoint in the API')`  
 `baseURL: str = (...)`  
 `
mkey: str = (...)`  
   
`@tool`  
`def requestTool(baseURL: str, endpoint: str, query: str) -> str:`  
 `'''Once you kn
ow the data structure for using the CRM_endpoint_context tool,`  
`you can now make a request to the endpoints using url
 request syntax'''`  
   
 `mkey = os.environ['MKEY']`  
 `headers = {'mkey': mkey}`  
 `url = f'{baseURL}/{endpoint}?qu
ery={query}'`  
 `response = requests.get(url, headers=headers)`  
 `if response.status_code == 200:`  
 `return respons
e.json()`  
 `else:`  
 `return f'Request failed with status code {response.status_code}'`  


I am aware that the query
 will not be right, I just want it to take the god damned argument.  


`tools = [`   
 `requestTool(baseURL='`[`https:/
/example.com`](https://example.com)`'), APIContextTool()`  
`]`

&#x200B;

I have been inspecting the Basetool class for
 a while to see what can be done but its just very long and I'm not that senior.  


I would apreciate any help, thanks.

```
---

     
 
all -  [ Optimal way to host/run inference on models at fp16? ](https://www.reddit.com/r/LangChain/comments/16aaann/optimal_way_to_hostrun_inference_on_models_at_fp16/) , 1693876876.0
```
I've only worked with quantized models thus far, but I'm adding a second 3090 to my rig and want to try running inferenc
e and hosting an FP16 model, hopefully a 13b if it fits in 48gb. 

What are you guys using to host your fp16 models? Jus
t the transformers library? Are there any tips I should know for faster inference? For example, GPTQ quantized models ca
n use exllama to double their inference speed. In that vein, what is the cutting edge hosting/inference solution for ful
l precision llama models?
```
---

     
 
all -  [ Has anyone done a GPTQ quant at 8k or larger on the llama2 code models yet? ](https://www.reddit.com/r/LangChain/comments/16aa47m/has_anyone_done_a_gptq_quant_at_8k_or_larger_on/) , 1693876392.0
```
Just the title. I know it takes exponentially more compute to quantize for longer context lengths and the bloke typicall
y uses 4k context for that reason. Anyone know if there are any GPTQ quants that let us take advantage of the rope scali
ng that the new coder models were trained with?
```
---

     
 
all -  [ Create_sql_agent not able to access db when being used as a tool in a multi-tool agent ](https://www.reddit.com/r/LangChain/comments/16a6fxq/create_sql_agent_not_able_to_access_db_when_being/) , 1693866979.0
```
I have created a SQL bot using Langchain that was performing great, utilizing the create\_sql\_agent toolkit, however no
w as I am trying to add more tools that play off of the queries it was performing, the bot is now unable to make any inf
erences about the names of the columns, or seem to connect to the db at all. I am basing my work off of the docs here: [
https://python.langchain.com/docs/modules/agents/agent\_types/openai\_functions\_agent](https://python.langchain.com/doc
s/modules/agents/agent_types/openai_functions_agent)  
Let me know if there are any mistakes in approach on my part, or 
if anyone has experienced anything similar.  
Thanks in advance!
```
---

     
 
all -  [ Structured data and LLMs: Should I embed? ](/r/vectordatabase/comments/16a3x33/structured_data_and_llms_should_i_embed/) , 1693861340.0
```

```
---

     
 
all -  [ Same project different words which one is better ](https://www.reddit.com/gallery/16a3sh3) , 1693861011.0
```

```
---

     
 
all -  [ LLM for big contextual questions ](https://www.reddit.com/r/LangChain/comments/169zbmo/llm_for_big_contextual_questions/) , 1693851116.0
```
Hi all,

i need an LLM that can run on my avarage GPU for now (GeForce 3060) and can take an input of a big context (say
 7000 tokens) and return an answer for it.

llama2 seems not to fit and mpt7 needs a stronger GPU.

any suggestions?
```
---

     
 
all -  [ Saving AIMessages to a file ](https://www.reddit.com/r/LangChain/comments/169yjw8/saving_aimessages_to_a_file/) , 1693849377.0
```
I have code that looks like this:

    chat = ChatOpenAI(openai_api_key=api_key)
    system_tempalte = 'some text'
    s
ystem_message = SystemMessagePromptTemplate.from_template(system_template)
    human_template = '{variable_one} {variabl
e_two}'
    human_message = HumanMessagePromptTemplate.from_template(human_template)
    chat_prompt = ChatPromptTemplat
e.from_messages([system_message, human_message])
    for i in range (len(variable_one)):
        prompt = chat_prompt.fo
rmat_messages(variable_one = variable_one[i], variable_two = variable_two[i])
        results = chat(prompt)

what I wan
t to do is return the AIMessage as a string that I can write to a file that has Variable One: Variable Two: and then the
 AIMessage based on what variables its iterated. I haven't been able to make sense of how to do that from the documentat
ion. Anyone got any ideas?
```
---

     
 
all -  [ GPT-4 enhanced GPT-3.5 prompting ](https://www.reddit.com/r/LangChain/comments/169xjsl/gpt4_enhanced_gpt35_prompting/) , 1693847108.0
```
I've recently read a post on Twitter where someone claimed that he has great success with crafting and refining prompts 
for GPT-3.5 with the help of GPT-4. Unfortunately he gave no further hints on how he's doing that. He claimed that his m
ethod lifts GPT-3.5 almost on GPT-4 level. 

1. Anybody heard of this approach?
2. Wouldn't LangChain be the perfect too
l to automate that?
```
---

     
 
all -  [ 21 looking for internship, give me a reason why won’t you hire me? ](https://i.redd.it/qtdpsyd6o9mb1.jpg) , 1693845453.0
```

```
---

     
 
all -  [ Alternatives to Cosine similarity search, that provides better results for your use-case? ](https://www.reddit.com/r/LangChain/comments/169wguh/alternatives_to_cosine_similarity_search_that/) , 1693844642.0
```

```
---

     
 
all -  [ Ways to Inject Metadata into Text Chunks? ](https://www.reddit.com/r/LangChain/comments/169uxea/ways_to_inject_metadata_into_text_chunks/) , 1693841133.0
```
Hi, would anybody know what the best way to inject metadata into text chunks using LangChain or maybe even Llama Index w
ould be?

For my use-case, I want to load in a PDF, and split the PDF into chunks, I want to be able to inject additiona
l metadata. Is there a class in LangChain that helps with that? If not, what would be a good way to do this? I thought o
f a somewhat hacky way of doing it by converting to JSON, appending the metadata fields, and then using the jsonloader t
o load it back in.

Any ideas or suggestions would be most welcomed and appreciated. Thanks in advanced!
```
---

     
 
all -  [ Running llama 2(any model) in nodejs? ](https://i.redd.it/lbsexelh69mb1.jpg) , 1693839505.0
```
I'm trying to run llama2 model by using node js but am constantly running into errors. The langchain documentation recom
mends some other npm package and there are some tutorials out there which are using a totally different npm package. I'v
e tried everything(even moved the file to D) in order to make the path simple, but yet the same error pops up. 

Can any
body tell me how to correctly set up local llm with nodejs? Fed up of errors and I've been trying since yesterday!
Pleas
e help!!
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

     
