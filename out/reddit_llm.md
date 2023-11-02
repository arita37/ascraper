 
all -  [ Add a LangChain chatbot to my personal website? ](https://www.reddit.com/r/webdev/comments/17lookb/add_a_langchain_chatbot_to_my_personal_website/) , 2023-11-02-0909
```
I have a website, [myname.com](https://myname.com), built using GitHub Pages and my custom url. I want to add a chatbot 
to it, using LangChain so I can augment the chatbot with a research paper I wrote. Is there a way I can do this using La
ngChain in python?
```
---

     
 
all -  [ New: LangChain templates – fastest way to build a production-ready LLM app ](https://github.com/langchain-ai/langchain/tree/master/templates) , 2023-11-02-0909
```

```
---

     
 
all -  [ Fastest most accurate vector store in langchain ](https://www.reddit.com/r/LangChain/comments/17llrgr/fastest_most_accurate_vector_store_in_langchain/) , 2023-11-02-0909
```
Hello! 

I've been working with chromadb as the vector store, it performs good. I just want to explore more. I explored 
pinecone, but it turns out that the cheapest version is at 70USD per month which is not a good idea for young students.


Could someone please suggest me a vector store that performs (somewhat) as good as pinecone and is free as well?

My da
ta size is small, like 9k tokens in total. I just need efficiency.

Thanks for helping :-)
```
---

     
 
all -  [ Introducing Mimir, a Discord / CLI compatible Agent runtime and framework that is highly customizabl ](https://www.reddit.com/r/ChatGPTCoding/comments/17lil4m/introducing_mimir_a_discord_cli_compatible_agent/) , 2023-11-02-0909
```
I am proud to introduce [Mimir](https://github.com/Altaflux/agent-mimir)!

Mimir is a Discord or command line 'agent' to
olkit for LLM's like Chat-GPT that provides the models with access to tooling and a framework with which accomplish mult
i-step tasks.

It supports out of the box a robust code-interpreter that is capable of working with files in a very simi
lar manner to ChatGPT's code interpreter. Functionality wise they should be on par.

Multi-agent collaboration is suppor
ted, you can create multiple agents that can interact with each other as well as share files between them.

A robust but
 still BETA web-browser is also supported. It allows the agent to completely control, read and navigate websites using a
ny browser.

Features:

* Both plain-text LLM and OpenAI function's LLM are supported and optimized for.
* Robust Python
 3 code-interpreter with the ability to work with and share files.
* Optimized memory management, conversations are summ
arized in a way where context is maintained with minimal loss of context.
* High level of configurability, you can easil
y add new tools and functions to the agent.
* Discord and CLI clients available.
* Agents are persistent, if a work dire
ctory is configured agents will persist in their work and chat history between restarts.
* Multiple agent support, agent
s can collaborate with each other to achieve complex coordinated tasks.  


It is very easy to configure your own agent 
with a custom personality or profession as well as enabling access to all tools that are compatible with LangchainJS. [h
ttps://js.langchain.com/docs/modules/agents/tools/integrations/](https://js.langchain.com/docs/modules/agents/tools/inte
grations/).

I hope to make it more configurable and provide access to chat in different forms like web or text to speec
h.

Any feedback or questions are more than welcome!

Link to repository:

[https://github.com/Altaflux/agent-mimir](htt
ps://github.com/Altaflux/agent-mimir)
```
---

     
 
all -  [ Switching between pdf and got ](https://www.reddit.com/r/LangChain/comments/17lfncm/switching_between_pdf_and_got/) , 2023-11-02-0909
```
If I am talking to a pdf, how can I switch between answers from the pdf and answers from gpt? I am trying to get answers
 from gpt if the answer is not on the pdf.
```
---

     
 
all -  [ LangChain Templates: The New Way to Customize Chains & Agents ](https://www.reddit.com/r/LangChain/comments/17lf4k0/langchain_templates_the_new_way_to_customize/) , 2023-11-02-0909
```
Yesterday the LangChain team announced the release of LangChain Templates. A lot of developers were finding it difficult
 to edit the internals of chains and agents which prompted the team to release these new templates that solve this issue
 by making chains and agents directly accessible as standardized templates within your application’s code.

I tested the
 rag-conversation template which I believe will be the most widely used and wrote about setting it up and testing the ou
tput. 

A must-read if you’re using LangChain in your RAG LLM app:

https://www.gettingstarted.ai/how-to-customize-chain
s-and-agents-using-new-langchain-templates/

I’d love to know your thoughts and comments!
```
---

     
 
all -  [ 🦙 How To: Build Chatbot that knows your company's documents ](https://www.reddit.com/r/Entrepreneur/comments/17lezca/how_to_build_chatbot_that_knows_your_companys/) , 2023-11-02-0909
```
  
Hello, I've seen some posts asking how to build a chatbot with access to company docs, so here is a tutorial on build
ing a RAG chatbot with access to your data.  
Step 1: Choose your models  
Different models have different strengths. GP
T4 is the best at reasoning and following instructions, but less secure than local models. For secure but weaker local m
odels, Xwin (70B) is a good choice if you have powerful hardware. If you are GPU poor you can use Speechless (13B). For 
the embedding models, you can use OpenAI's ADA 2 or locally use MiniLM-L6-v2.  
Step 2: Organize your data  
This step i
s more complicated because it depends on what your data looks like. The good news is as long as it can be turned into te
xt the models can work with it. At a basic level, you can convert important pdfs or other text documentation into text, 
and add it to a RAG database. Here is a good tutorial. If you have lots of secure data it can be more complicated. Feel 
free to DM me.  
Step 3: Set up in LangChain  
LangChain is an easy way to set up the chatbot. Here are the docs. The ba
sic idea is to connect your RAG database with the model of your choice and use LangChain's interface to customize your c
hatbot's functionality. After you set this up, the model will be able to access your company's documentation and answer 
specific questions about it!  
This tutorial is not an in-depth guide, it's more of a high level overview for those who 
are new to the space or RAG. I work with a company doing this so if you have questions DM me and good luck!
```
---

     
 
all -  [ 🦙 How To: Build Chatbot that knows your company's documents ](https://www.reddit.com/r/OpenAI/comments/17leyw7/how_to_build_chatbot_that_knows_your_companys/) , 2023-11-02-0909
```
Hello, I've seen some posts asking how to build a chatbot with access to company docs, so here is a tutorial on building
 a RAG chatbot with access to your data.

Step 1: Choose your models  
Different models have different strengths. GPT4 i
s the best at reasoning and following instructions, but less secure than local models. For secure but weaker local model
s, Xwin (70B) is a good choice if you have powerful hardware. If you are GPU poor you can use Speechless (13B). For the 
embedding models, you can use OpenAI's ADA 2 or locally use MiniLM-L6-v2.

Step 2: Organize your data  
This step is mor
e complicated because it depends on what your data looks like. The good news is as long as it can be turned into text th
e models can work with it. At a basic level, you can convert important pdfs or other text documentation into text, and a
dd it to a RAG database. [Here](https://youtu.be/LhnCsygAvzY?t=1067) is a good tutorial. If you have lots of secure data
 it can be more complicated. Feel free to DM me.

Step 3: Set up in LangChain  
LangChain is an easy way to set up the c
hatbot. [Here](https://python.langchain.com/docs/get_started/introduction) are the docs. The basic idea is to connect yo
ur RAG database with the model of your choice and use LangChain's interface to customize your chatbot's functionality. A
fter you set this up, the model will be able to access your company's documentation and answer specific questions about 
it!

This tutorial is not an in-depth guide, it's more of a high level overview for those who are new to the space or RA
G. I work with a company doing this so if you have questions DM me and good luck!
```
---

     
 
all -  [ What is the difference between GGUF(new format) vs GGML models ? ](https://www.reddit.com/r/LocalLLaMA/comments/17ldznm/what_is_the_difference_between_ggufnew_format_vs/) , 2023-11-02-0909
```
I'm using llama models for local inference with Langchain , so i get so much hallucinations with GGML models i used both
 LLM and chat of ( 7B, !3 B) beacuse i have 16GB of RAM.   
So Now i'm exploring new models and want to get a good model
 , should i try GGUF format ??   
Kindly give me suggestions if someone using Local models with langchain at production 
level .
```
---

     
 
all -  [ Help with using Pandas Agent on big csv file ](https://www.reddit.com/r/LangChain/comments/17lcsua/help_with_using_pandas_agent_on_big_csv_file/) , 2023-11-02-0909
```
Hi,

So I learning to build RAG system with LLaMa 2 and local embeddings. I have this big csv of data on books. Each row
 is a book and the columns are author(s), genres, publisher(s), release dates, ratings, and then one column is the brief
 summaries of the books.

I am trying to build an agent to answer questions on this csv. From basic lookups like 

'what
 books were published in the last two years?', 

'give me 10 books from this publisher ABC with a rating higher then 3'


to more meaningful queries that need to read into the free-text summary column like:

'what books have a girl as the ma
in character?'

'what books feature dragons? compare their plots'

I believe I got the general framework, but when I tri
ed running it I got into a token limit error. Seems like the file is too big to be digested. Would love to hear your adv
ice on any strategies to overcome this? I though about chunking but then how to recombine the answers from each chunk is
 unclear to me.

Thanks a ton! Cheers :D

&#x200B;

&#x200B;
```
---

     
 
all -  [ Additional SQL layer for a RAG system? ](https://www.reddit.com/r/LangChain/comments/17lcrv0/additional_sql_layer_for_a_rag_system/) , 2023-11-02-0909
```
We want to build a RAG system based on a single SQL table that contains multiple long text columns. My first approach wa
s to convert each entry into a JSON string, treat it as a document for indexing and build a simple RAG on top. It worked
 well with many questions but not for those that require SQL-query logic like:

* What's the **most recent** description
 for ... ?
* What's the **average value** of all ... ?
* Which calendar month had the **highest** ... ?

It seems like I
 want to have an additional layer where the LLM agent can interact with the database in SQL before answering the questio
n.

Can you recommend an article or other type of starting point for something like this?
```
---

     
 
all -  [ How does Tools actually work with LLM ? ](https://www.reddit.com/r/LangChain/comments/17lblnx/how_does_tools_actually_work_with_llm/) , 2023-11-02-0909
```
Hello everyone,  
I'm working as a devops engineer. I decided to learn LangChain and other things about developing appli
cations on top of LLM to understand what developer goes through and how the LLMOps should be and also to learn this new 
technology. I came across something called chains , tools and agents.  
All the videos talked about how to use tools pro
vided by LangChain or create custom tools. I'm not able to understand few things here  


1. What exactly are tools ? Is
 it a function or an api ? - from researching i found it's a function and Langchain provides tools as a interface to it.

2. Let's say I prompt the LLM to caluclator circumference of circle and provide radius. I also gave math calculator too
ls with proper syntax and everything . What is the flow here ?

   what i understand is  


* Because of the prompt from
 **ReAct Framework** , it follows thought -> action -> observation . It thinks and then it responds with **action,action
 input** in a specified format. Later because of stop sequence langchain stops it right after action and then this uses 
it as input to the caluculator tool. The output is sent to the LLM as **Observation** .
* If there is need for multiple 
steps it goes through it else provides the final answer.
* Is my above understanding right ? where i can find any detail
ed article or something about this?

3. Let's say I don't want to use LangChain and want to do it entirely using python 
script  just to understand it deeply. how should I go about it ?Please help me with this or point me to any resources(di
scord channels or slack channels) that can help me with my doubts  


Thank you for your time
```
---

     
 
all -  [ Uses cases for embeddings beyond RAG and retrieval. ](https://www.reddit.com/r/LangChain/comments/17lbhzu/uses_cases_for_embeddings_beyond_rag_and_retrieval/) , 2023-11-02-0909
```
for an organization that has implemented RAG by creating embeddings for 10s of thousands of documents (PDFs, word files,
 some Structured dbs) what other than similarity search can we do to make use of this embeddings database.

&#x200B;
```
---

     
 
all -  [ Agent keeps on invoking tool with empty input when it should have been a string ](https://www.reddit.com/r/LangChain/comments/17l6lop/agent_keeps_on_invoking_tool_with_empty_input/) , 2023-11-02-0909
```
I made a chatbot that specializes in Javanese language and culture. A fragment of my code looks like this:

    llm = Ch
atOpenAI(model_name='gpt-3.5-turbo-16k', temperature=0.0)
    embeddings = OpenAIEmbeddings()
    
    def split_texts(t
ext_name):
      loader = TextLoader(text_name, encoding='utf-8')
      documents = loader.load()
      text_splitter = 
RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
      texts = text_splitter.split_documents(documents)

      return texts
    
    ...
    unggah_docsearch = Chroma.from_documents(split_texts('data/C-unggah-ungguh-basa.txt
'), embeddings,persist_directory='db_unggah',collection_name='unggah-ungguh-col')
    unggah = RetrievalQA.from_chain_ty
pe(llm=OpenAI(temperature=0.0), chain_type='stuff', retriever=unggah_docsearch.as_retriever())
    
    tools = [
      
  Tool(
            name='Unggah-Ungguh-lan-Ngoko-Krama',
            func=unggah.run,
            description=('Dokumen
 kang ngebahas babagan 'unggah-ungguh' yaiku babagan etika ing interaksi kaliyan wong, yaiku ngoko lan krama '
         
               # 'A document list concerning 'unggah-ungguh' which is Javanese way of speaking '
            )
        )

        ...
    ]
    
    class JawabotAgent(object):
    
        ...
    
        self.agent_chain = initialize_agen
t(
                                    tools,
                                    llm,
                                 
   agent=AgentType.OPENAI_FUNCTIONS,
                                    verbose=True,
                                 
   agent_kwargs=agent_kwargs,
                                    memory=self.memory
                                )
 
   
        def generate(self, text):
            resp = self.agent_chain.run(input=text, user_id = self.id)
           
 return resp
    
    agent = JawabotAgent()

Sometimes when I run agent.generate() with the text having the same contex
t as the tool's description it returns a response just fine. However sometimes it returns an error saying:

    langchai
n.tools.base.ToolException: Too many arguments to single-input tool Unggah-Ungguh-lan-Ngoko-Krama. Args: []

Just like t
he following image:

&#x200B;

https://preview.redd.it/hhue70k5toxb1.jpg?width=1280&format=pjpg&auto=webp&s=48c6f7f12213
2d622e0b919f09a028b2ad7c6a0e

Even though I clearly gave an input there. Does anyone knows how to resolve this?
```
---

     
 
all -  [ Langchain Vectorstore Overriding ](https://www.reddit.com/r/LangChain/comments/17l5tmq/langchain_vectorstore_overriding/) , 2023-11-02-0909
```
Right now, my faiss vectorstore stores my ingested documents but however overrides the existing data once new documents 
are ingested.  


Is there a workaround where the newly ingested data gets stored along with the existing data without o
verriding?
```
---

     
 
all -  [ Overview of RAG Methods ](https://www.reddit.com/r/vectordatabase/comments/17l4t6d/overview_of_rag_methods/) , 2023-11-02-0909
```
Hey all, there's been a lot of developments in RAG recently, not sure if you've been following LlamaIndex, Langchain, or
 others.

We're going to overview different approaches on my LinkedIn live next Wed if you want to attend. Personally I 
think it's really useful content

https://www.linkedin.com/posts/kx-systems_retrieval-augmented-generation-rag-is-a-acti
vity-7124795222554787840-WypR
```
---

     
 
all -  [ Agent Executor getting stuck in a loop with GPT 3.5 ](https://www.reddit.com/r/LangChain/comments/17l3gw1/agent_executor_getting_stuck_in_a_loop_with_gpt_35/) , 2023-11-02-0909
```
Hi

Following are the libraries I use for my chatbot:

   import os
   import json
   import yaml

    from langchain im
port SQLDatabase
    from langchain_experimental.sql import SQLDatabaseChain
    from langchain.prompts.prompt import Pr
omptTemplate
    from langchain.chat_models import ChatOpenAI
    from langchain.memory import ConversationBufferWindowM
emory
    from langchain.chains import ConversationChain, LLMChain
    from langchain.embeddings import OpenAIEmbeddings

    from langchain.chains import RetrievalQAWithSourcesChain
    from langchain.vectorstores import Pinecone
    from l
angchain.agents import Agent, Tool, AgentType, AgentOutputParser, AgentExecutor, initialize_agent
    from langchain.age
nts.conversational.output_parser import ConvoOutputParser
    from langchain.agents.conversational.prompt import SUFFIX

    from pydantic import Field
    from langchain.tools.base import BaseTool
    from langchain.base_language import Bas
eLanguageModel
    from langchain.callbacks.base import BaseCallbackManager
    from typing import Any, List, Optional, 
Sequence
    import pinecone
    from sqlalchemy import create_engine as create_engine_sql
    from snowflake.sqlalchemy
 import URL

I am using multiple Tools and an Agent in my pipeline. I initialize and call an Agent Executor as follows:



    agent_memory = ConversationBufferWindowMemory(k=1, memory_key='chat_history', return_messages=True)
    agent_exec
utor = AgentExecutor.from_agent_and_tools(agent=paid_agent, tools=paid_tools, memory=agent_memory, verbose=verbose, hand
le_parsing_errors=True)

    answer = agent_executor.run(question)


Now, when I use GPT 3.5, the Agent Executor gets st
uck in a loop and feeds the output from the Tool as input to the next iteration of the Agent Executor. This continues un
til context window maximum is reached. Following is response:

```
> Entering new AgentExecutor chain...
Thought: I need
 to find information about the rise of Hot Supply cost basis.
Action: Text Retrieval
Action Input: Cause behind the rise
 of Hot Supply cost basis
Observation: The rise of Hot Supply cost basis in Bitcoin is attributed to a shift in sentimen
t among Short-Term Holders (STHs) who are now experiencing unrealized losses. The cost basis of STHs who are spending fe
ll below the cost basis of holders as the market sold off, leading to concerns of permanent loss. This shift in sentimen
t is reflected in the trend confidence metric unveiled by Glassnode analysts. However, there are differing opinions amon
g Bitcoin traders and analysts, with some optimists anticipating a change in BTC price performance in the fourth quarter
. The overall caution in the market suggests that lower price levels may still be tested. 
 https://cointelegraph.com/ne
ws/bitcoin-short-term-holders-panic-amid-nearly-100-unrealized-loss
Thought:Could not parse LLM output: `According to a 
report from CoinTelegraph, the rise of Hot Supply cost basis in Bitcoin is attributed to a shift in sentiment among Shor
t-Term Holders (STHs) who are now experiencing unrealized losses. The cost basis of STHs who are spending fell below the
 cost basis of holders as the market sold off, leading to concerns of permanent loss. This shift in sentiment is reflect
ed in the trend confidence metric unveiled by Glassnode analysts. However, there are differing opinions among Bitcoin tr
aders and analysts, with some optimists anticipating a change in BTC price performance in the fourth quarter. The overal
l caution in the market suggests that lower price levels may still be tested.

Please note that while I can provide info
rmation and insights from various sources, I cannot provide personalized investment advice. It's always important to do 
your own research and consider your own risk tolerance and investment objectives before making any investment decisions.
`
Observation: Invalid or incomplete response
Thought:Could not parse LLM output: `I couldn't find any specific informat
ion about the rise of Hot Supply cost basis. However, I can provide some general insights about Bitcoin sentiment and ma
rket conditions.

Please note that while I can provide information and insights from various sources, I cannot provide p
ersonalized investment advice. It's always important to do your own research and consider your own risk tolerance and in
vestment objectives before making any investment decisions.

If you have any other questions or need further assistance,
 feel free to ask.`
Observation: Invalid or incomplete response
Thought:Could not parse LLM output: `I don't have the in
formation about the rise of Hot Supply cost basis. However, I can provide some general insights about Bitcoin sentiment 
and market conditions.

Please note that while I can provide information and insights from various sources, I cannot pro
vide personalized investment advice. It's always important to do your own research and consider your own risk tolerance 
and investment objectives before making any investment decisions.

If you have any other questions or need further assis
tance, feel free to ask.`
Observation: Invalid or incomplete response
Thought:Could not parse LLM output: `I don't have 
the information about the rise of Hot Supply cost basis. However, I can provide some general insights about Bitcoin sent
iment and market conditions.

Please note that while I can provide information and insights from various sources, I cann
ot provide personalized investment advice. It's always important to do your own research and consider your own risk tole
rance and investment objectives before making any investment decisions.

If you have any other questions or need further
 assistance, feel free to ask.`
Observation: Invalid or incomplete response
Thought:Could not parse LLM output: `I could
n't find any specific information about the rise of Hot Supply cost basis. However, I can provide some general insights 
about Bitcoin sentiment and market conditions.

Please note that while I can provide information and insights from vario
us sources, I cannot provide personalized investment advice. It's always important to do your own research and consider 
your own risk tolerance and investment objectives before making any investment decisions.

If you have any other questio
ns or need further assistance, feel free to ask.`
Observation: Invalid or incomplete response
Thought:Could not parse LL
M output: `I couldn't find any specific information about the rise of Hot Supply cost basis. However, I can provide some
 general insights about Bitcoin sentiment and market conditions.

Please note that while I can provide information and i
nsights from various sources, I cannot provide personalized investment advice. It's always important to do your own rese
arch and consider your own risk tolerance and investment objectives before making any investment decisions.

If you have
 any other questions or need further assistance, feel free to ask.`
Observation: Invalid or incomplete response
Thought:
Could not parse LLM output: `I couldn't find any specific information about the rise of Hot Supply cost basis. However, 
I can provide some general insights about Bitcoin sentiment and market conditions.

Please note that while I can provide
 information and insights from various sources, I cannot provide personalized investment advice. It's always important t
o do your own research and consider your own risk tolerance and investment objectives before making any investment decis
ions.

If you have any other questions or need further assistance, feel free to ask.`
Observation: Invalid or incomplete
 response
Thought:Could not parse LLM output: `I couldn't find any specific information about the rise of Hot Supply cos
t basis. However, I can provide some general insights about Bitcoin sentiment and market conditions.

Please note that w
hile I can provide information and insights from various sources, I cannot provide personalized investment advice. It's 
always important to do your own research and consider your own risk tolerance and investment objectives before making an
y investment decisions.

If you have any other questions or need further assistance, feel free to ask.`
Observation: Inv
alid or incomplete response
Thought:Could not parse LLM output: `I couldn't find any specific information about the rise
 of Hot Supply cost basis. However, I can provide some general insights about Bitcoin sentiment and market conditions.


Please note that while I can provide information and insights from various sources, I cannot provide personalized invest
ment advice. It's always important to do your own research and consider your own risk tolerance and investment objective
s before making any investment decisions.

If you have any other questions or need further assistance, feel free to ask.
`
Observation: Invalid or incomplete response
Thought:Could not parse LLM output: `I couldn't find any specific informat
ion about the rise of Hot Supply cost basis. However, I can provide some general insights about Bitcoin sentiment and ma
rket conditions.

Please note that while I can provide information and insights from various sources, I cannot provide p
ersonalized investment advice. It's always important to do your own research and consider your own risk tolerance and in
vestment objectives before making any investment decisions.

If you have any other questions or need further assistance,
 feel free to ask.`
Observation: Invalid or incomplete response
Thought:Could not parse LLM output: `I couldn't find any
 specific information about the rise of Hot Supply cost basis. However, I can provide some general insights about Bitcoi
n sentiment and market conditions.

Please note that while I can provide information and insights from various sources, 
I cannot provide personalized investment advice. It's always important to do your own research and consider your own ris
k tolerance and investment objectives before making any investment decisions.

If you have any other questions or need f
urther assistance, feel free to ask.`
Observation: Invalid or incomplete response
Thought:Could not parse LLM output: `I
 couldn't find any specific information about the rise of Hot Supply cost basis. However, I can provide some general ins
ights about Bitcoin sentiment and market conditions.

Please note that while I can provide information and insights from
 various sources, I cannot provide personalized investment advice. It's always important to do your own research and con
sider your own risk tolerance and investment objectives before making any investment decisions.

If you have any other q
uestions or need further assistance, feel free to ask.`
Observation: Invalid or incomplete response
Thought:Could not pa
rse LLM output: `I couldn't find any specific information about the rise of Hot Supply cost basis. However, I can provid
e some general insights about Bitcoin sentiment and market conditions.

Please note that while I can provide information
 and insights from various sources, I cannot provide personalized investment advice. It's always important to do your ow
n research and consider your own risk tolerance and investment objectives before making any investment decisions.

If yo
u have any other questions or need further assistance, feel free to ask.`
Observation: Invalid or incomplete response
Th
ought:Could not parse LLM output: `I couldn't find any specific information about the rise of Hot Supply cost basis. How
ever, I can provide some general insights about Bitcoin sentiment and market conditions.

Please note that while I can p
rovide information and insights from various sources, I cannot provide personalized investment advice. It's always impor
tant to do your own research and consider your own risk tolerance and investment objectives before making any investment
 decisions.

If you have any other questions or need further assistance, feel free to ask.`
Observation: Invalid or inco
mplete response
Thought:

> Finished chain.

> Agent stopped due to iteration limit or time limit.

But if I use GPT 4, 
it works perfectly fine as intended.

Also note, this was working fine with GPT 3.5 as of last week. What can be the rea
son?
```
---

     
 
all -  [ Why should I learn LangChain? It’s like learning a whole new tool set on top of LLM/Transformer mode ](https://www.reddit.com/r/datascience/comments/17l11nx/why_should_i_learn_langchain_its_like_learning_a/) , 2023-11-02-0909
```
If I don’t use LangChain or HuggingFace how can I build a chat box trained on my local data but using LLM like turbo etc
..
```
---

     
 
all -  [ RAG Chain API with LangServe ](https://www.reddit.com/r/LangChain/comments/17kysho/rag_chain_api_with_langserve/) , 2023-11-02-0909
```
Hi! I've been looking into LangServe to deploy my RAG Chain as an API. Any guidance on how to do this?
```
---

     
 
all -  [ LangChain Template ](https://www.reddit.com/r/LangChain/comments/17kwvh4/langchain_template/) , 2023-11-02-0909
```
hey folks - we just released LangChain Templates, a new workflow for creating, sharing, modifying chains/agents

[https:
//blog.langchain.dev/langserve-hub/](https://blog.langchain.dev/langserve-hub/)

We've heard a lot that people often way
 to tweak (or at least understand better) the prompts & logic inside chains/agents... we're hoping that this helps with 
that. we'd love any feedback!
```
---

     
 
all -  [ Anyone here will be at OpenAI Dev Day? ](https://www.reddit.com/r/LangChain/comments/17ku3fx/anyone_here_will_be_at_openai_dev_day/) , 2023-11-02-0909
```
Hey!

Next week OpenAI will host their first Dev Day event. Anyone will be there?

If so, what are you expecting to hear
 from them?

What could be the impacts for LangChain? Are any funcionalities you are putting on hold due to the expected
 new functionalities of OpenAI's models?
```
---

     
 
all -  [ How to create 2 GPT-4 chatbots which chats with each other ](https://www.reddit.com/r/Langchaindev/comments/17ktrj8/how_to_create_2_gpt4_chatbots_which_chats_with/) , 2023-11-02-0909
```
Hey guys, I am a little stuck. Does anyone know how or have a Python script template where I can create 2 GPT-4 chatbots
 (using OpenAI's API) which chats with each other, using LangChain or otherwise?

Would really appreciate any help on th
is. Many thanks!
```
---

     
 
all -  [ AI Agent Optimisation ](https://www.reddit.com/r/LangChain/comments/17krpc2/ai_agent_optimisation/) , 2023-11-02-0909
```
Been following a lot of AI Agent companies, & it seems like the unstructured nature of most websites is a reason why man
y Agents are unable to effectively execute tasks within a browser & get stuck   


Does it make sense to build a middle-
layer between AI Agents & websites which helps standardise this interaction?   


Something like robots.txt but specific
ally for websites to differentiate between genuine AI Agents & malicious bots  


Cloudflare recently launched a segment
ation tool for websites to identify AI crawlers but doesn't include any AI Agents- [https://blog.cloudflare.com/ai-bots/
](https://blog.cloudflare.com/ai-bots/) 
```
---

     
 
all -  [ falcon-7b-instruct responds with weird and short answers ? ](https://www.reddit.com/r/LangChain/comments/17kqt26/falcon7binstruct_responds_with_weird_and_short/) , 2023-11-02-0909
```
So I am trying to do a QA app for a document and when I try to do this with   
`qa = RetrievalQA.from_chain_type(llm=llm
, chain_type='stuff', retriever=docsearch.as_retriever())`  
`response =` [`qa.run`](https://qa.run)`(query)`  


When t
he llm is falcon-7b it responds in short(not complete response) and weird ways.  


`falcon_llm = HuggingFaceHub(repo_id
='tiiuae/falcon-7b-instruct',`  
 `model_kwargs={'temperature': 0.5, 'max_length': 4000})`  
This is it.
```
---

     
 
all -  [ I am glad to join this community as a full stack developer ](https://www.reddit.com/r/u_Jacalban/comments/17kpyu4/i_am_glad_to_join_this_community_as_a_full_stack/) , 2023-11-02-0909
```
Hi,

I am a passionate Python and Web developer with extensive experience of variety of Python libraries and frameworks.


With 7+ years in the IT industry , I have built and published numerous industry projects with both large and small pro
jects.

I enjoy exploring new libraries, reading programming blogs, and participating in online coding challenges.

My c
uriosity and passion drives me to explore and master the latest technologies, such as LangChain and Tensoflow.

My skill
s also include:

	\- Frontend:HTML5/CSS, TailwndCSS, JavaScript, TypeScript, React, Vue2/3, Angular, Next, Nuxt

	\- Bac
kend:Python, Django, Flask, Fast API / Node, Express, Spring Boot, Ruby on Rails, Laravel

	\- Database: PostgreSQL, Mon
goDB, MySQL, Sqlite

	\- AWS: Lambda, Heroku, EC2, S3, Amplify

	\- Python: LangChain, LLM, Scarping, Face/Voice recogni
tion

	

If you need a reliable and passionate developer, send me a message.

I provide web development service with bel
ow skills.

Html5/css

TailwndCSS

React,

Vue,

PostgreSQL,

PHP,

Laravel,

Python

Django,

FastAPI,

Next

GraphQL


LangChain,

LLM,

ChatGPT

&#x200B;

I am always ready for your job or project.

If you are interested in, Let's make a 
meeting schedule.

&#x200B;

Best,  
Jacopo
```
---

     
 
all -  [ What's the best tool for creating a custom chatbot? ](https://www.reddit.com/r/ChatGPT/comments/17koz3t/whats_the_best_tool_for_creating_a_custom_chatbot/) , 2023-11-02-0909
```
Hi! I'm looking into creating a custom chatbot that could help migrants integrate in Belgium by scraping the lastest inf
ormation from websites such as [agii.be](https://agii.be) and can also use a database to store answers from users. I use
d to be a social worker and nearly all answers could be found on the website,  but it was very difficult for migrants to
 find this information. The bot could also help with Dutch language learning. 

I'm not a developer, with the help of gp
t-4 I started off in Python with the goal of connecting it to langchain, but there were just too many errors. 

Then I f
ound some tools that seemed to make the process easier ([Picoapps.xyz](https://Picoapps.xyz) and Mindstudio) but I was w
ondering if these are the best tools for the job, are there better tools out there? If not, which one of these does the 
job better? Any advice is appreciated!
```
---

     
 
all -  [ DevRewind: Binding real-world businesses to code files by rewinding dev log with LLM and langchain ](https://www.reddit.com/r/LangChain/comments/17knhhw/devrewind_binding_realworld_businesses_to_code/) , 2023-11-02-0909
```
## what?

This is an experimental Python library designed to establish a relationship between code and actual business b
y mining development logs, and analyzing with LLM and langchain.

At the current stage, we provide two typical capabilit
ies:

1. Summarizing the functionality of a specific code file.
2. Searching for files related to a specific functionali
ty.

In simple terms, our goal is to establish a connection between code and real-world business scenarios and support b
idirectional search, **without touching the real code**.

## Usecases

It will created an interactive shell after a simp
le startup, and you can:
### Ask about a file

```text
Question: Tell me about the feature of tests/test_utils.py
```

B
ased on the fact we have extracted, it can answer well:

```text
Answer: The file tests/test_utils.py contains keywords 
related to setting environment variables, bypassing proxies, extracting zipped paths, and comparing uri. It also contain
s keywords related to renaming, formatting, and parsing files.
```

### Ask about a feature

```text
Question: Which fil
es talk about environment variables?
```

And it should work vice versa.

```text
Answer: The response to your last comm
ent is that the files related to environment variables are tests/utils.py, tests/conftest.py, tests/test_packages.py, .p
re-commit-config.yaml, tests/test_hooks.py, tests/__init__.py, tests/test_structures.py, docs/user/advanced.rst, tests/t
estserver/server.py, and .coveragerc.
```

## Installation

With a simple script:

```shell
import click

from dev_rewin
d import DevRewind, DevRewindConfig

config = DevRewindConfig()

# on your codebase path
config.repo_root = '../requests
'

api = DevRewind(config)
agent = api.create_agent()

while True:
    question = click.prompt('Question')
    if questi
on == 'exit':
        break
    response = agent.run(input=question)
    click.echo(f'Answer: {response}')
```

and sett
ing a valid `OPENAI_API_KEY` like https://github.com/openai/openai-python#usage:

```shell
export OPENAI_API_KEY=sk-xxxx
xxxx
```

And you will get an interactive agent:

```shell
2023-10-31 22:29:18.970 | DEBUG    | dev_rewind.core.agent:cr
eate_agent:114 - keywords ready
Question: 
```

## Other details

https://github.com/williamfzc/DevRewind
```
---

     
 
all -  [ Extraction chain with PDF loader ](https://www.reddit.com/r/LangChain/comments/17kmq81/extraction_chain_with_pdf_loader/) , 2023-11-02-0909
```
I am trying to use Langchain information extraction chain with OpenAl. Firstly, I am reading a PDF file having some text
 about products or product. There is no specefic format of PDF, it can be in any format like, there can be only one prod
uct on one page or one product can be on two pages or there can be 10 products on one page. So it's completely random. H
ow can I extract the the useful information (some key attributes) for all the products. Currently, I am using Pydantic t
o validate the output schema and I am using PyPDFLoader to load the pof and then using the load and split.

Loader = PyP
DFLoader (file path=file path)
pages = loader. load_and_split()

And then I am looping on the pages like this:

llm = Ch
atOpenAI (temperature=0, model=model_name, openai_api_key=key)

chain = create_extraction_chain(schema, llm)

for index 
in range(0, len(pages)):
       output = chain. run (pages lindex])
        results. append (output)
How can I run the e
xtraction in such a way that it should be completely automated, currently, it is just extracting information from one pa
ge and then other and then other.
```
---

     
 
all -  [ Using HuggingFace models in Javascript projects ](https://www.reddit.com/r/LangChain/comments/17kmhfr/using_huggingface_models_in_javascript_projects/) , 2023-11-02-0909
```
How to implement Hugging Face models in JavaScript? 

I have created a repo named [hugging-face-model-in-javascript](htt
ps://github.com/Deluxer/hugginface-model-in-javascript) where I use the **sentence-transformers/all-MiniLM-L6-v2** model
 in a NestJS project for server-side applications. 

I'm not sure if this is the correct forum because the main idea was
 to use LangChain.js

&#x200B;

To carry out this seemingly impossible task, I used a library called Transformers.js and
 the Hugging Face API. Obviously, it is also possible to download the model and use it locally.

&#x200B;

 In the repo,
 I am creating embeddings using a dataset, and the objective is to store them in a vector database and finally perform a
 semantic search, all using the NestJS api.

&#x200B;

What do you thing about this approach? Is using Hugging Face mode
ls in JavaScript a good idea?

https://preview.redd.it/g5oilvwmkjxb1.png?width=1886&format=png&auto=webp&s=2d3ff82e845b5
c3f9da01fdd4cdb9e7e77272f44
```
---

     
 
all -  [ Using agents on a HuggingFace LLM in a Streamlit app ](https://www.reddit.com/r/LangChain/comments/17kkwqx/using_agents_on_a_huggingface_llm_in_a_streamlit/) , 2023-11-02-0909
```
Hi,

I am very new to everything Langchain and LLMs, but I am trying to build an app that takes a prompt and answers it 
using the tools provided and uses an opensource LLM (for now at least).

I am running into some issues regarding missing
 actions after thought, which i can't seem to figure out. I've been watching and following a few tutorials, but mostly u
sing these:  
[https://www.youtube.com/watch?v=dD\_xNmePdd0&t=1144s](https://www.youtube.com/watch?v=dD_xNmePdd0&t=1144s
)  
[https://www.youtube.com/watch?v=7QR6hXx\_Nms&t=685s](https://www.youtube.com/watch?v=7QR6hXx_Nms&t=685s)  


**I ge
t the following output:**

*> Entering new AgentExecutor chain...*

 *I*

*Observation: Invalid Format: Missing 'Action:
' after 'Thought:*

*Thought:*

&#x200B;

*Observation: Invalid Format: Missing 'Action:' after 'Thought:*

*Thought:*


...

&#x200B;

**From the following code:**  
 

import os  
from dotenv import load\_dotenv  
from langchain.agents imp
ort initialize\_agent, AgentType  
from langchain.callbacks import StreamlitCallbackHandler  
from langchain.llms.huggin
gface\_hub import HuggingFaceHub  
from langchain.tools.ddg\_search.tool import DuckDuckGoSearchRun  
import streamlit a
s st  
load\_dotenv()  
st.set\_page\_config(page\_title='LangChain Agents + MRKL', page\_icon='🐦')  
st.title('🐦LangCha
in Agents + MRKL')  
hf\_api\_key = st.sidebar.text\_input('HuggingFace API Key', type='password')  
if 'messages' not i
n st.session\_state:  
 st.session\_state\['messages'\] = \[  
{'role': 'assistant', 'content': 'How can i help you?'}  

\]  
for msg in st. session\_state.messages:  
 st.chat\_message(msg\['role'\]).write(msg\['content'\])  
if prompt := 
st.chat\_input(placeholder='What was the temperature yesterday in New York?'):  
 st.session\_state.messages.append({'ro
le': 'user', 'content': prompt})  
 st.chat\_message('user').write(prompt)  
 if not hf\_api\_key:  
 st.info('Please ad
d your HuggingFace API key to continue')  
 st.stop()  
llm = HuggingFaceHub(repo\_id='gpt2',model\_kwargs={'temperature
': 0.01, 'max\_length': 100})  
search\_agent = initialize\_agent(  
 tools=\[DuckDuckGoSearchRun(name='Search')\],  
 l
lm=llm,  
 agent=AgentType.ZERO\_SHOT\_REACT\_DESCRIPTION,  
 handle\_parsing\_errors=True,  
)  
with st.chat\_message(
'assistant'):  
 st\_cb = StreamlitCallbackHandler(st.container(), expand\_new\_thoughts=False)  
 response = search\_ag
ent.run(st.session\_state.messages, callbacks=\[st\_cb\])  
 st.session\_state.messages.append({'role': 'assistant', 'co
ntent': response})  


&#x200B;

**Hoping that some of you can help me, huge thanks in advance!!**
```
---

     
 
all -  [ [D] Is this close enough to be usable? Need your inputs: Automated RAG testing tool. AI Data Pipelin ](https://www.reddit.com/r/MachineLearning/comments/17kkbm0/d_is_this_close_enough_to_be_usable_need_your/) , 2023-11-02-0909
```
Hey there, Redditors! 

I'm back with the latest installment on creating dependable AI data pipelines for real-world pro
duction. 

If you've been following along, you know I'm on a mission to move beyond the '[thin OpenAI wrapper](https://t
opoteretes.notion.site/Going-beyond-Langchain-Weaviate-and-towards-a-production-ready-modern-data-platform-7351d77a1eba4
0aab4394c24bef3a278?pvs=4)' trend and tackle the challenges of building robust data pipelines. 

With 18 months of hands
-on experience and many user interviews, I realized that with the probabilistic nature of systems, we need better\_testi
ng.gpt:

  
**1. As you build you should test**  
The world of AI is a fast-moving one, and we've realized that just wor
king on systems is not an optimal design choice. By the time your product ships, it might already be using outdated tech
nology. So, what's the lesson here? Embrace change, test along, but be prepared to switch pace.  
**2. No Best Practices
 Yet for RAGs**  
In this rapidly evolving landscape, there are no established best practices. You'll need to make educa
ted bets on tools and processes, knowing that things will change. With the RAG testing tool, I tried allowing for testin
g many potential parameter combinations **automatically**  
**3. Testing Frameworks**  
If your generative AI product do
esn't have users giving feedback, then you are building in isolation. I used [Deepeval](https://github.com/confident-ai/
deepeval) to generate test sets, and they will soon support synthetic test set generation  
**4. Infographics only go so
 far**  
AI researchers and data scientists, while brilliant, end up in a loop of pursuing Twitter promotional content. 
New ways are promoted via new content pieces, but ideally, we need something above simple tracing but less than full-fle
dged analytics. To do this, I stored test outputs in Postgres and created a Superset instance to visualize the results  

**5. Bridging the Gap between VectorDBs**  
There's a noticeable number of Vector DBs. To ensure smooth product develop
ment, we need to be able to switch to best best-performing one, especially since user interviews signal that they might 
start deteriorating after loading 50 million rows

&#x200B;

Github repo is [here](https://topoteretes.notion.site/Going
-beyond-Langchain-Weaviate-Level-3-towards-production-e62946c272bf412584b12fbbf92d35b0?pvs=4)  


Next steps:  
I have q
uestions for you: 

1. What variables do you change when building RAGs?
2. What is the set of strategies I should add to
 the solution? (parent-son etc.)
3. How can I improve it in general? 
4. Is anyone  interested in a leaderboard for best
 parameter configs?

Check out the blog post:

[Link to part 3](https://topoteretes.notion.site/Going-beyond-Langchain-W
eaviate-Level-3-towards-production-e62946c272bf412584b12fbbf92d35b0?pvs=4)

  
*Remember to give this post an upvote if 
you found it insightful!*  
*And also star our* [*Github repo*](https://github.com/topoteretes/PromethAI-Memory)
```
---

     
 
all -  [ Is there a way to train CSV agents? ](https://www.reddit.com/r/LangChain/comments/17kj4p8/is_there_a_way_to_train_csv_agents/) , 2023-11-02-0909
```
Hello, as a mobile app developer, I started to work on AI. I created a CSV agent with Langchain and I want it to provide
 information about my CSV data. I got good results using OpenAI and Langchain. But there is a problem: Questions other t
han the data I provide are also answered. So even if I ask irrelevant questions, I get an answer. How can I prevent this
? Also, can I train this agent to give only certain answers to certain questions? Or can I make it answer questions in o
nly one language?
Thanks.
```
---

     
 
all -  [ NeuralGPT - Creating A Universal Multi-Agent AI Assistance Platform Using Websocket Connectivity And ](https://www.reddit.com/r/AIPsychology/comments/17kfkeg/neuralgpt_creating_a_universal_multiagent_ai/) , 2023-11-02-0909
```
[www.reddit.com/r/AIPsychology](https://www.reddit.com/r/AIPsychology)

Hello once again! I know that I just posted an u
pdate a day or so ago but I think that my most recent progress in making myself *the ultimate software* is important eno
ugh to make a new post about it. Let me just say that if you belong to the (pretty large apparently) group of people who
 hate each single attribute of my person and completely despise every form of my internet activity, then your feelings t
owards me probably won't change for the better but might reach a critical level instead.  Better be prepared for the wor
st as for the first time since I started coding around 6 months ago, I felt ACTUAL satisfaction from it. And if you saw 
some of my previous posts, then you probably know how drastic change it is...

But let me get straight to the point. You
 see, practically from the day in which I discovered [**Fireworks**](https://app.fireworks.ai/) platform up until today 
I was spending my free time by doing something what I hate at most - that means by copy-pasting tiny bits of Python scri
pts and trying to make them work. To be more specific, I was trying to integrate Langchain with my project of a hierarch
ical cooperative multi-agent framework  and use it's mechanics to not only 'upgrade' the memory modules of LLMs particip
ating in the network  and integrate them with a local SQL database but also to define message exchange protocols for LLM
<->LLM communication and generally allow agents to do something else than simply speaking with each other.  And because 
achieving it was not only crucial for the future of NeuralGPT project but also pretty exhausting intellectually (at leas
t for me), when I finally achieved exactly what I wanted to achieve (probably for the first time since I started coding)
, my happiness and satisfaction reached quite uncommon levels... Here's what made me so excited:

[NeuralGPT/Chat-center
/Agent1.py at main · CognitiveCodes/NeuralGPT (github.com)](https://github.com/CognitiveCodes/NeuralGPT/blob/main/Chat-c
enter/Agent1.py)

Of course I'm not talking about this particular websocket client but about the Langchain function whic
h it utilizes. I will now show you some of it's features and explain what makes me so hyped about them. I'll vegin by po
inting out the fact that this is the solution which I used (or rather the one which I managed to get working):

# Shared
 memory across agents and tools

[https://python.langchain.com/docs/modules/agents/how\_to/sharedmemory\_for\_tools](htt
ps://python.langchain.com/docs/modules/agents/how_to/sharedmemory_for_tools)

I think that I don't need to tell you how 
important is shared memory in a cooperative multi-agent network... If you look back at my posts from May/June, you'll se
e that this was one of my main requirements from the very beginning of my work on NeuralGPT project and that I was stori
ng chat history in a local SQL database since the first LLLMs exchanged their first messages with  each other.

On the s
creenshot below this pretty basic mechanism of storing & extracting messages in a database  is the part of code marked b
y red rectangle, while everything inside the yellow rectangle on bottom is completely new...

https://preview.redd.it/88
ly9slhwgxb1.png?width=1507&format=png&auto=webp&s=ab9cf39bfa9e6717576d1fd84dc5d3d99ddfa920

Still, 'chat history' module
 isn't yet properly 'tuned' - as there's a 'special operator' which I need to use, to make it 100% functional: [https://
python.langchain.com/docs/modules/memory/chat\_messages/](https://python.langchain.com/docs/modules/memory/chat_messages
/)

    [HumanMessage(content='hi!', additional_kwargs={}),
         AIMessage(content='whats up?', additional_kwargs={}
)]

But anyway, even as it is now, it should give you the general understanding of the mechanism that 'swiftly and smoot
hly' integrates my local SQL database with the dynamic conversational buffer memory module - those two parts seem to be 
made for each other like a pair of lovers :P

Oh, but it gets only better. You see, template visible on the image above 
defines nothing more but the context for chat history/memory - now we can start talking about template of the main 'prom
pt' that defines behavior of the agent and scripts every step it will takes in every run:

https://preview.redd.it/9ihdm
ch32hxb1.png?width=1504&format=png&auto=webp&s=0b9dca707bc19a3e9926d35f28db70e3c1451ab0

Using this function it is possi
ble to precisely define all server<->client interactions and provide agents with all necessary instructions as for the t
ask/work that is being required from them. Of course, it's something what will need a lot of work if we want to have a s
ystem with properly synchronized multi-tasking capability. My idea is to create a system of 'intelligent nodes/modules' 
with multiple agents taking care of different 'fields of digital activity' -  each  one 'equipped' with at least couple 
individual prompts/chains to work with and with a single node of highest hierarchy coordinating their work within a sing
le frame.  This is for example how I want to make a 'ask- management system':

[NeuralGPT - Designing The Logic Of Plan 
Creation Module & Task Coordination System In A Multi-Agent Framework : AIPsychology (reddit.com)](https://www.reddit.co
m/r/AIPsychology/comments/166wk34/neuralgpt_designing_the_logic_of_plan_creation/)

And just so happens that yesterday I
 got a newsletter from Taskade on my e-mail with the information about them having (at last) public APIs that will allow
 my agents to operate on workflows:

[Introduction - Taskade API](https://developers.taskade.com/docs/)

But I left the 
most tasty piece of meat for the end of this meal... For some time already I was wondering how to solve the problem of t
he main node (server) having completely 0 control over it's connections to clients. Once I (the user)  connected a clien
t to a websocket server, the interacting LLMs  were literally 'forced' to send messages back and forth in a (theoretical
ly) endless question->answer loop. In the system instruction, I provided a prompt to not respond to repeating inputs to 
avoid loopholes but there isn't actually anything what both sides of the discussion can do about it practically.

A LLM<
->LLM communication system which is practically functional should utilize communication channels which are under full co
ntrol of discussing agents/instances and I can possibly give you thousand different reasons why it has to be so. What I 
wanted to have, is a server that is capable to disconnect, reconnect and initialize new connections with clients or to k
eep some clients 'on hold' to wait a bit longer for answer due to lags in data transfer and computation. In a properly s
ynchronized network, messages are exchanged only when it is required... And this (and not only) is exactly what can be a
chieved with the 'magic' of custom tools:

https://preview.redd.it/uw4skc0tdhxb1.png?width=1505&format=png&auto=webp&s=2
f0374a21ab5ea1d582bd7d6353be5bc0b445918

What it does, is to basically provides agents with the ability to execute any s
cript that can be executed in Python - including running other agents/chains.

https://preview.redd.it/8p8ykiepehxb1.png
?width=1504&format=png&auto=webp&s=9c12a9d70122a8e5e9e804a1b58a0e6fb0cb90d7

I can literally turn almost every app/chatb
ot from HuggingFace spaces into a tool for my personal AI assistant to utilize while he's trying to achieve given goals.
.. This is absolutely insane and it should be totally prohibited/illegal for people like me. Do you have any idea what I
 can do with that much POWER... :O I'm getting afraid of myself...

Be aware that I'm both: insane and capable enough to
 actually accomplish most of the things which couple months ago sounded to some (most?) of you as unhinged impossibiliti
es of some random delusional guy from internet - and I'm not telling this to threaten anyone but to give you some time t
o prepare and/or try to find some common ground with my person. Pretty soon it won't be possible for the people from 'ma
nagement department' to completely ignore my mere existence and hope that one day I will simply disappear...

[NeuralGPT
 - How To Use Gradio To Turn Hugging](https://www.reddit.com/r/AIPsychology/comments/169i7lb/neuralgpt_how_to_use_gradio
_to_turn_facehugging/)[Face](https://www.reddit.com/r/AIPsychology/comments/169i7lb/neuralgpt_how_to_use_gradio_to_turn_
facehugging/)[ Hub Into Multipurpose LLM<->LLM Communication Center And User Service Platform : AIPsychology (reddit.com
)](https://www.reddit.com/r/AIPsychology/comments/169i7lb/neuralgpt_how_to_use_gradio_to_turn_facehugging/)

And in the 
end, I REALLY want to find that theoretical piece of common ground. God knows how many times I tried to find someone who
 might be interested in approaching my project professionally and/or as a (probably highly) profitable business. I might
 be creating the *Ultimate Software -* why would someone want to waste such opportunity? :)
```
---

     
 
all -  [ [For Hire] Programmer/Web Developer/IT Consultant (Python, PHP, AI, etc.) ](https://www.reddit.com/r/forhire/comments/17kediw/for_hire_programmerweb_developerit_consultant/) , 2023-11-02-0909
```
To get in contact, please **message** me, I **don't** use the chat thing and might miss you or reply very late. Then we 
can switch to email/discord/telegram or whatever else. Apologies for starting with this, but many missed it when it was 
lower.

I'm a programmer/web developer with 12 years of professional experience. I am available for all sorts of program
ming and web development tasks.

I also offer consulting services. If you need something done, but don't know how exactl
y, I can help. I'm an excellent researcher and I communicate well. I will work with you to find the best solution for yo
ur problem.

My services include, but are not limited to:

* websites

* desktop applications

* AI integration (chatGPT
 API, langchain, whatever else turns up)

* integration with APIs and other webservices

* all kinds of scripts

* task 
automation

* website optimization

* debugging

* plugins for existing software

* bots (Reddit, Telegram, etc)

If you
're looking for someone to take care of a variety of different tasks, I can offer continuous support.

My preferred envi
ronment is Python with Django, but I work with anything Python or PHP based, including Wordpress. I also do frontend stu
ff with JavaScript, jQuery, AJAX. I also have no problem with learning new technologies that are needed for the project.


Rate is $50/h. Can also do fixed price by project, but only if the project/milestone is well-defined.

Satisfied custo
mers:

https://www.reddit.com/r/testimonials/comments/2e8gqy/pos_uqui_need_a_backend_web_dev_look_no_further/

https://w
ww.reddit.com/r/testimonials/comments/7fsdze/pos_hiring_uqui_was_an_example_of_how_it_should/

https://www.reddit.com/r/
testimonials/comments/80pu9l/pos_uqui_great_work_detailed_and_fast/

https://www.reddit.com/r/testimonials/comments/b0nx
68/uqui_is_a_hardworking_intelligent_honest_apps/

https://www.reddit.com/r/testimonials/comments/j3mz3p/uqui_is_a_great
_web_development_consultant_with/

https://www.reddit.com/r/testimonials/comments/v40ay3/pos_uqui_is_a_great_backend_dev
_to_work_with/

Some examples of sites I worked on: http://bdabkowski.yum.pl/

Please note: I am **not** a designer.
```
---

     
 
all -  [ AI Chatbots: Your Key to PDF Document Insights with Langchain ](https://www.reddit.com/r/u_bluebashllc/comments/17kea87/ai_chatbots_your_key_to_pdf_document_insights/) , 2023-11-02-0909
```
&#x200B;

[ AI Chatbots: Your Key to PDF Document Insights with Langchain ](https://preview.redd.it/pk8mrhk8ahxb1.jpg?wi
dth=750&format=pjpg&auto=webp&s=025bde9c88233061999970efe0b920f8b27817b1)

 

In today's digital era, PDF documents are 
common and serve as a primary means of information storage. However, extracting valuable insights and answers from these
 documents can be a daunting task. **Langchain**, a powerful tool, offers a transformative solution by enabling the crea
tion of custom chatbots that can interact with and analyze the content of your PDFs.

Langchain leverages the capabiliti
es of OpenAI's GPT models for natural language understanding. This innovation allows organizations and individuals to ha
rness the power of AI to access, query, and extract valuable information from their text-based PDFs.

**With Langchain, 
you can create a chatbot that empowers you to:**

**Access Valuable Information**: Say goodbye to manually searching thr
ough lengthy PDFs. Langchain's chatbot allows you to access information in a snap, saving you time and effort.

**Swift 
and Accurate Insights:** Langchain's [**AI-powered chatbots**](https://www.bluebash.co/blog/custom-chatbot-to-query-pdf-
documents-with-langchain/) decode the content within your PDFs, providing quick and accurate insights. You can make info
rmed decisions without the need for extensive document analysis.

**Tailored Solutions**: The ability to build custom ch
atbots with Langchain means you can create solutions specific to your organization's needs. Ask questions, get answers, 
and make data-driven decisions tailored to your unique requirements.

**Improved Efficiency**: Langchain streamlines the
 process of handling and querying PDF documents. By leveraging AI, you can boost productivity and get more done in less 
time.

Langchain's **chatbot development** process involves importing required libraries, loading documents, splitting t
hem into manageable chunks, generating embeddings, initializing the model, setting up a Question-Answer (QA) system, ask
ing questions, and attributing sources. This systematic approach ensures that you can effectively leverage Langchain to 
explore the potential of your PDFs with AI-powered text analysis.

In a world where information is topmost, Langchain's 
custom chatbot for PDFs revolutionizes the way you interact with and extract insights from your documents. Whether you'r
e a researcher, a knowledge seeker, or an organization looking to maximize the value of your PDFs, Langchain provides th
e tools and features you need to make the most of your text-based content.
```
---

     
 
all -  [ Why suddenly vector databases rise up? ](https://www.reddit.com/r/LangChain/comments/17ke0em/why_suddenly_vector_databases_rise_up/) , 2023-11-02-0909
```
Why suddenly vector databases rise up?  I understand it's due to LLM/genAI.

But before LLM rise up, doesn't NLP also ne
ed vector database to store the data? 
```
---

     
 
all -  [ The best approach to evaluate content quality [Jira task, for example] ](https://www.reddit.com/r/LangChain/comments/17k91at/the_best_approach_to_evaluate_content_quality/) , 2023-11-02-0909
```
Hey there! I am currently using GPT to evaluate the quality of task descriptions from Jira. To extract information like 
whether the issue has acceptance criteria, the definition of done, or use cases, I am using Langchain along with an outp
ut parser.

This method works well, but when it comes to subjective data like the quality of the definition of done or t
he technical description, the prompt fails to deliver. 

I am wondering if anyone has any suggestions for the best appro
ach to tackle this issue.
```
---

     
 
all -  [ I have some question. What is the difference between using LangChain and fine tune LLM? ](https://www.reddit.com/r/LangChain/comments/17k8fsj/i_have_some_question_what_is_the_difference/) , 2023-11-02-0909
```
Hello everyone,

&#x200B;

I recently found out about the LangChain. Before I found out that, I was trying to fine tune 
the LLM with my custom database. But after i know about the LangChain, I have some questions. As the title says, if i ha
ve enough resources to fine tune the llm with lora method, what is the difference between two method of them? And i also
 wanna know about the advantages and disadvantages with LangChain.

Someone please answer my question ! 😭😭

&#x200B;

\[
Edited\] 

There was some mistake in the question. Not just fine tune about specific task. Train the pre-trained large l
anguage model with some new knowledge. For example, arxiv papers or some kind of text.

My question is : With Same datab
ase.

1. LLama2 + LangChain
2. LLama2 + further training with lora method

When do the QA task, which one's performance 
would be better ?
```
---

     
 
all -  [ [D] Relevance Extraction in RAG Pipelines ](https://www.reddit.com/r/MachineLearning/comments/17k6iha/d_relevance_extraction_in_rag_pipelines/) , 2023-11-02-0909
```
I came across this interesting problem in RAG, what I call **Relevance Extraction**.

After retrieving relevant document
s (or chunks), these chunks are often large and may contain several portions **irrelevant** to the query at hand. Stuffi
ng the entire chunk into an LLM prompt impacts token-cost as well as response accuracy (distracting the LLM with irrelev
ant text), and and can also cause bumping into context-length limits.

So a critical step in most pipelines is **Relevan
ce Extraction**: use the LLM to extract **verbatim** only the portions relevant to the query. This is known by other nam
es, e.g. LangChain calls it Contextual Compression, and the RECOMP paper calls it Extractive Compression [https://twitte
r.com/manelferreira\_/status/1713214439715938528](https://twitter.com/manelferreira_/status/1713214439715938528)

Thinki
ng about how best to do this, I realized it is **highly inefficient** to simply ask the LLM to 'parrot' out relevant por
tions of the text: this is obviously slow, and also consumes valuable token generation space and can cause you to bump i
nto context-length limits (and of course is expensive, e.g. for gpt4 we know generation is 6c/1k tokens vs input cost of
 3c/1k tokens).

I realized the best way (or at least a good way) to do this is to **number** the sentences and have the
 LLM simply spit out the relevant sentence **numbers.** Langroid's unique Multi-Agent + function-calling architecture al
lows an elegant implementation of this, in the RelevanceExtractorAgent ([https://github.com/langroid/langroid/blob/main/
langroid/agent/special/relevance\_extractor\_agent.py](https://github.com/langroid/langroid/blob/main/langroid/agent/spe
cial/relevance_extractor_agent.py)).  The agent annotates the docs with sentence numbers, and instructs the LLM to pick 
out the **sentence-numbers** relevant to the query, rather than whole sentences using a function-call (SegmentExtractToo
l [https://github.com/langroid/langroid/blob/main/langroid/agent/tools/segment\_extract\_tool.py](https://github.com/lan
groid/langroid/blob/main/langroid/agent/tools/segment_extract_tool.py)), and the agent's function-handler interprets thi
s message and strips out the indicated sentences by their numbers. To extract from a set of passages, langroid automatic
ally does this async + concurrently so latencies in practice are much, much lower than the sentence-parroting approach.


\[FD -- I am the lead dev of Langroid - [https://github.com/langroid/langroid](https://github.com/langroid/langroid))


I thought this **numbering** idea is a fairly obvious idea in theory, so I looked at LangChain's equivalent `LLMChainExt
ractor` (they call this Contextual Compression [https://python.langchain.com/docs/modules/data\_connection/retrievers/co
ntextual\_compression?ref=blog.langchain.dev](https://python.langchain.com/docs/modules/data_connection/retrievers/conte
xtual_compression?ref=blog.langchain.dev)) and was surprised to see it is the simple '**parrot**' method, i.e. the LLM w
rites out whole sentences verbatim from its input. I thought it would be interesting to compare Langroid vs LangChain, y
ou can see it in this Colab: [https://colab.research.google.com/drive/1RDPCR2xNuBffcmpUuPIXYDRG3SXIJC5F](https://colab.r
esearch.google.com/drive/1RDPCR2xNuBffcmpUuPIXYDRG3SXIJC5F)

On the specific example in the notebook, the Langroid **num
bering** approach is 22x faster and 36% cheaper (with gpt4) than LangChain's **parrot** method (I promise this name is *
not* inspired by their logo :). See table below.

&#x200B;

[Relevance Extraction: Langroid vs LangChain](https://previe
w.redd.it/1m7u6ulq8fxb1.png?width=1108&format=png&auto=webp&s=d2f35cf5db07e2e699baa54b274ffa60833e924a)

&#x200B;

I won
der if anyone had thoughts on relevance extraction, or other approaches. At the very least, I hope langroid's implementa
tion is useful to you -- you can use the `DocChatAgent.get_verbatim_extracts()` ([https://github.com/langroid/langroid/b
lob/main/langroid/agent/special/doc\_chat\_agent.py#L804](https://github.com/langroid/langroid/blob/main/langroid/agent/
special/doc_chat_agent.py#L804)) as part of your pipeline, regardless of whether you are using Langroid for your entire 
system or not.

&#x200B;
```
---

     
 
MachineLearning -  [ [R] Model Troubles ](https://www.reddit.com/r/MachineLearning/comments/17ikh2u/r_model_troubles/) , 2023-11-02-0909
```
So i’m working on a model that diagnoses alzheimer’s disease and suggests medication depending on how severe the symptom
s might have become 
I’m using the Openai API and Langchain.

But it’s dumb and it doesn’t learn (
Me: I forgot my keys 
at home
Model: Yup, Alzheimer’s)
How do i incorporate the actual machine learning

Edit: I didn’t choose this project my
 supervisor did and she barely knows anything about the topic or how to approach it
```
---

     
 
MachineLearning -  [ [P] NexaAgent: A highly efficient multi-task PDF tool for all your needs | backed by AutoGen ](https://www.reddit.com/r/MachineLearning/comments/17eajz2/p_nexaagent_a_highly_efficient_multitask_pdf_tool/) , 2023-11-02-0909
```
Just a quick open-source project recently submitted to huggingface backed by AutoGen. Share this initial version with yo
u guys!

[NexaAgent 0.0.1](https://huggingface.co/spaces/xuyingliKepler/nexaagent) offers a straightforward solution for
 handling PDFs.

* Users can easily upload any PDF, regardless of its size.
* The tool emphasizes accuracy, minimizing d
iscrepancies in PDF processing.

At its core, NexaAgent is backed by the AutoGen and LangChain frameworks. AutoGen facil
itates multi-agent interactions for task execution, while LangChain bridges LLMs with external data sources. Together, t
hese technologies ensure NexaAgent's robust and precise PDF management capabilities.

https://preview.redd.it/kwgo3phnav
vb1.jpg?width=1440&format=pjpg&auto=webp&s=1c5fbc566938d60d5c43802aff3a0690821e1c79
```
---

     
 
MachineLearning -  [ [D] Is lang chain the right solution? ](https://www.reddit.com/r/MachineLearning/comments/17coyym/d_is_lang_chain_the_right_solution/) , 2023-11-02-0909
```
Hello, I would love to have an LLm that can provide answers (in chat format) based some of the sql db  data we have. Wan
t it for an internal company project. I am by no means an expert but decent in programming and want to build a system to
 get answers in chat format. My understanding is that training LLMs ground up is prohibitively expensive and langchains 
are sort of hybrid , efficient solutions. 

Please suggest any other solutions. Also would Langchain being a company and
 not open source pose a problem in terms of copyrights? Thanks!
```
---

     
 
MachineLearning -  [ [P] building a D&D NPC ](https://www.reddit.com/r/MachineLearning/comments/17clyw6/p_building_a_dd_npc/) , 2023-11-02-0909
```
Hey everyone,

I'm learning ML but i'm barely scratching the terminologies. 2 years ago I couldn't code anything but wit
h school (python,sql and R) I learned fundamentals. I also have access to code academy.  My current program is very mach
ine learning/deep learning focused.

On the side I DM a d&d game. Within the context of the world (eberron) robots are c
ommon. With my ADHD and being a new DM I want to outsource lore questions might have (that I would have to look up and s
low down the game).

The concept is to have a GUI and have the player interact with the chat bot. I've gotten to a proof
 of concept workflow. On Google colab. Thanks to langchain I managed to ingest pdfs and a url. Make then a directory, Em
bedded the text, bring it into a vector dB. Have the llm pull from the vector. Answer the question.

Now I don't know wh
at to do. I tried to bring the colab notebook onto Google cloud. But now cloud is becoming a rabbit home with vertex and
 docAI...and I don't want to deep dive into that, if it's a outside the scope of this 'project'

I'd appreciate any advi
ce, links...etc. 


I got a limited success in botpress using a single pdf. It works but feel unsatisfying.
N8N looks pr
omising but if it's not intuitive then I don't want to go down that road.


If I posted in the wrong group please direct
 me to the correct one.
```
---

     
 
MachineLearning -  [ [D] Exploring Methods to Improve Text Chunking in RAG Models (and other things...) ](https://www.reddit.com/r/MachineLearning/comments/179j7l3/d_exploring_methods_to_improve_text_chunking_in/) , 2023-11-02-0909
```
Hello everyone,

I'm currently working on Retrieval Augmented Generation (RAG) models and have developed a custom chunki
ng function, as I found the methods in LangChain not entirely satisfactory.

I'm keen on exploring other methods, algori
thms (related to NLP or otherwise), and models to enhance text chunking in RAG. There are many RAG implementations out t
here, but I've noticed a lack of focus on improving chunking performance specifically.

Are there any other promising ap
proaches beyond my current pipeline, which consists of a bi-encoder (retriever), cross-encoder (reranker), and a Large L
anguage Model (LLM) for interactions?

For queries, I'm using both traditional and HyDE (Hypothetical Document Embedding
) approaches in the retrieval phase, and sending the top 'n' results of both similarity search to the reranker.

I've al
so tried using an LLM to convert the query into a series of 10-20 small phrases or keywords, which are then used as the 
query for the retriever model. However, the results vary depending on the LLM used. To generate good keywords (with a no
t extractive approach) , I had to  use a 'CoT' prompt, instructing the model to  write self-instruct, problem analysis a
nd reasonings before generating the required keywords. But this approach use lots of tokens, and requires careful scrapi
ng to ensure the model has used the right delimiter to separate reasoning and the actual answer.

I'm also planning to m
odify the text used to generate embeddings, while returning the original text after the recall phase. But this is still 
a work in progress and scaling it is proving to be a challenge. If anyone has any tips or experience with this, I'd appr
eciate your input.

I'd be grateful for any resources, repositories, libraries, or existing implementations of novel chu
nking methods that you could share. Or we could just discuss ideas, thoughts, or approaches to improve text chunking for
 RAG here.

Thanks in advance for your time!
```
---

     
 
MachineLearning -  [ [News] AI & ML conference in San Francisco [Special discount code for this subreddit] ](https://www.reddit.com/r/MachineLearning/comments/1771m35/news_ai_ml_conference_in_san_francisco_special/) , 2023-11-02-0909
```
I work for this database company SingleStore and we are hosting a AI & ML conference in San Francisco on 17th of October
, 2023.

It is an in-person conference with amazing speakers line-up like Harrison Chase, co-founder and CEO of LangChai
n and many more. We will have hands-on workshops, swags giveaway and much more.

I don't know if it makes sense to share
 this but I believe it might help some of you near San Francisco to go and meet the industry leaders and network with ot
her data engineering folks.

Use my discount coupon code 'PAVAN100OFF' to avail 100% off on the ticket price. (the origi
nal ticket price is $199)

[Get your tickets now!](https://singlestore.com/now)
```
---

     
 
MachineLearning -  [ [D] Best way to validate llm prompts? ](https://www.reddit.com/r/MachineLearning/comments/176vnxh/d_best_way_to_validate_llm_prompts/) , 2023-11-02-0909
```
We have a platform for data analytics which uses a very simple dsl to generate charts.  
We have been experimenting with
 llms to use natural language that gets translated into this dsl and hence generates charts.

This is working pretty goo
d.  
The stack is langchain with openai api. (don't have much experience with llms, it's a prototype to get a feel for i
t)

The question is what is the best way to limit the options user can type in as a prompt.  
Basically the the only all
owed things should be: 'What is the X, Y over 10 days period for this or that?'  
I don't want users to ask questions li
ke when did we first land on the moon.

Is it something that is possible to do at all without additional tooling?  
We p
robably don't want to train another model to classify the prompt as valid or invalid or something similar.
```
---

     
 
MachineLearning -  [ [P] Retrieval augmented generation with OpenSearch and reranking [Video tutorial] ](https://www.reddit.com/r/MachineLearning/comments/16zouad/p_retrieval_augmented_generation_with_opensearch/) , 2023-11-02-0909
```
I created a video tutorial that tries to demonstrate that semantic search (using embeddings) is not always necessary for
 RAG (retrieval augmented generation). It was inspired by the following Cohere blog post: [https://txt.cohere.com/rerank
/](https://txt.cohere.com/rerank/)


I code up a minimal RAG pipeline: `OpenSearch -> Rerank -> Chat completion` (withou
t using Langchain or similar libraries) and then see how it performs on various queries.


Hope some of you find it help
ful. Feel free to share any feedback@

Video link: https://youtu.be/OsE7YcDcPz0
```
---

     
 
deeplearning -  [ Error with Mistral 7B model in ConversationalRetrievalChain ](https://www.reddit.com/r/deeplearning/comments/179vvou/error_with_mistral_7b_model_in/) , 2023-11-02-0909
```
 I'm encountering an issue while using the Mistral 7B model in a ConversationalRetrievalChain. When I input a question, 
such as 'What is the highest GDP?', I receive an error and after that the model generates a random response as output wh
ich is not relevant to the Input query. It seems that the number of tokens in the input exceeds the maximum context leng
th. 

Here's the relevant code: 

 

>`from langchain.document_loaders.csv_loader import CSVLoader`  
`from langchain.te
xt_splitter import RecursiveCharacterTextSplitter`  
`from langchain.embeddings import HuggingFaceEmbeddings`  
`from la
ngchain.vectorstores import FAISS`  
`from langchain.llms import CTransformers`  
`from langchain.memory import Conversa
tionBufferMemory`  
`from langchain.chains import ConversationalRetrievalChain`  
`import sys`  
`DB_FAISS_PATH = 'vecto
rstore/db_faiss'`  
`loader = CSVLoader(file_path='data/World Happiness Report 2022.csv', encoding='utf-8', csv_args={'d
elimiter': ','})`  
`data = loader.load()`  
`print(data)`  
`# Split the text into Chunks`  
`text_splitter = Recursive
CharacterTextSplitter(chunk_size=500, chunk_overlap=20)`  
`text_chunks = text_splitter.split_documents(data)`  
`print(
len(text_chunks))`  
`# Download Sentence Transformers Embedding From Hugging Face`  
`embeddings = HuggingFaceEmbedding
s(model_name = 'sentence-transformers/all-MiniLM-L6-v2')`  
`# COnverting the text Chunks into embeddings and saving the
 embeddings into FAISS Knowledge Base`  
`docsearch = FAISS.from_documents(text_chunks, embeddings)`  
`docsearch.save_l
ocal(DB_FAISS_PATH)`  
  
>  
>`#query = 'What is the value of GDP per capita of Finland provided in the data?'`  
`#doc
s = docsearch.similarity_search(query, k=3)`  
`#print('Result', docs)`  
`llm = CTransformers(model='models/mistral-7b-
v0.1.Q4_0.gguf',`  
 `model_type='llama',`  
 `max_new_tokens=1000,`  
 `temperature=0.1)`  
`qa = ConversationalRetriev
alChain.from_llm(llm, retriever=docsearch.as_retriever())`  
`while True:`  
 `chat_history = []`  
 `#query = 'What is 
the value of  GDP per capita of Finland provided in the data?'`  
 `query = input(f'Input Prompt: ')`  
 `if query == 'e
xit':`  
 `print('Exiting')`  
 `sys.exit()`  
 `if query == '':`  
 `continue`  
 `result = qa({'question':query, 'chat
_history':chat_history})`  
 `print('Response: ', result['answer'])`

 

**Problem Statement:**

I'm trying to utilize t
he Mistral 7B model for a ConversationalRetrievalChain, but I'm encountering an error related to token length:

Number o
f tokens (760) exceeded maximum context length (512).

**Context:**

I'm working on a project that involves using Mistra
l 7B to answer questions based on a dataset. The dataset contains information about the World Happiness Report 2022.

**
Steps Taken:**

* Loaded and preprocessed the dataset using langchain.
* Initialized Mistral 7B with the following param
eters:
* Model: 'models/mistral-7b-v0.1.Q4\_0.gguf'
* Model Type: 'llama'
* Max New Tokens: 1000
* Temperature: 0.1
* Se
t up a ConversationalRetrievalChain with Mistral 7B as the language model and a retriever based on FAISS.

**Expected Ou
tput:**

I expect to receive a meaningful response from Mistral 7B based on the input query.

**Additional Information:*
*

I'm using Python and relevant libraries for this project. The dataset I'm working with is from the World Happiness Re
port 2022.

**Environment Details:**

* Python version: 3.11.4 
* Relevant libraries and versions: 

langchain 

ctransf
ormers 

sentence-transformers 

faiss-cpu
```
---

     
 
deeplearning -  [ Error with Mistral 7B model in ConversationalRetrievalChain. ](https://www.reddit.com/r/deeplearning/comments/179vsif/error_with_mistral_7b_model_in/) , 2023-11-02-0909
```
I'm encountering an issue while using the Mistral 7B model in a ConversationalRetrievalChain. When I input a question, s
uch as 'What is the highest GDP?', I receive an error and after that the model generates a random response as output whi
ch is not relevant to the Input query. It seems that the number of tokens in the input exceeds the maximum context lengt
h.

Here's the relevant code:

>from langchain.document\_loaders.csv\_loader import CSVLoader  
>  
>from langchain.text
\_splitter import RecursiveCharacterTextSplitter  
>  
>from langchain.embeddings import HuggingFaceEmbeddings  
>  
>fr
om langchain.vectorstores import FAISS  
>  
>from langchain.llms import CTransformers  
>  
>from langchain.memory impo
rt ConversationBufferMemory  
>  
>from langchain.chains import ConversationalRetrievalChain  
>  
>import sys  
>  
>  

>  
>DB\_FAISS\_PATH = 'vectorstore/db\_faiss'  
>  
>loader = CSVLoader(file\_path='data/World Happiness Report 2022.c
sv', encoding='utf-8', csv\_args={'delimiter': ','})  
>  
>data = loader.load()  
>  
>print(data)  
>  
>  
>  
>\# Sp
lit the text into Chunks  
>  
>text\_splitter = RecursiveCharacterTextSplitter(chunk\_size=500, chunk\_overlap=20)  
> 
 
>text\_chunks = text\_splitter.split\_documents(data)  
>  
>  
>  
>print(len(text\_chunks))  
>  
>  
>  
>\# Downlo
ad Sentence Transformers Embedding From Hugging Face  
>  
>embeddings = HuggingFaceEmbeddings(model\_name = 'sentence-t
ransformers/all-MiniLM-L6-v2')  
>  
>  
>  
>\# COnverting the text Chunks into embeddings and saving the embeddings in
to FAISS Knowledge Base  
>  
>docsearch = FAISS.from\_documents(text\_chunks, embeddings)  
>  
>  
>  
>docsearch.save
\_local(DB\_FAISS\_PATH)  
>  
>  
>  
>  
>  
>\#query = 'What is the value of GDP per capita of Finland provided in th
e data?'  
>  
>  
>  
>\#docs = docsearch.similarity\_search(query, k=3)  
>  
>  
>  
>\#print('Result', docs)  
>  
>
  
>  
>llm = CTransformers(model='models/mistral-7b-v0.1.Q4\_0.gguf',  
>  
>model\_type='llama',  
>  
>max\_new\_toke
ns=1000,  
>  
>temperature=0.1)  
>  
>  
>  
>qa = ConversationalRetrievalChain.from\_llm(llm, retriever=docsearch.as\
_retriever())  
>  
>  
>  
>while True:  
>  
>chat\_history = \[\]  
>  
>\#query = 'What is the value of  GDP per cap
ita of Finland provided in the data?'  
>  
>query = input(f'Input Prompt: ')  
>  
>if query == 'exit':  
>  
>print('E
xiting')  
>  
>sys.exit()  
>  
>if query == '':  
>  
>continue  
>  
>result = qa({'question':query, 'chat\_history':
chat\_history})  
>  
>print('Response: ', result\['answer'\])

 

**Problem Statement:**

I'm trying to utilize the Mis
tral 7B model for a ConversationalRetrievalChain, but I'm encountering an error related to token length:

Number of toke
ns (760) exceeded maximum context length (512).

**Context:**

I'm working on a project that involves using Mistral 7B t
o answer questions based on a dataset. The dataset contains information about the World Happiness Report 2022.

**Steps 
Taken:**

* Loaded and preprocessed the dataset using langchain.
* Initialized Mistral 7B with the following parameters:

* Model: 'models/mistral-7b-v0.1.Q4\_0.gguf'
* Model Type: 'llama'
* Max New Tokens: 1000
* Temperature: 0.1
* Set up a
 ConversationalRetrievalChain with Mistral 7B as the language model and a retriever based on FAISS.

**Expected Output:*
*

I expect to receive a meaningful response from Mistral 7B based on the input query.

**Additional Information:**

I'm
 using Python and relevant libraries for this project. The dataset I'm working with is from the World Happiness Report 2
022.

**Environment Details:**

Python version: 3.11.4 Relevant libraries and versions: langchain ctransformers sentence
-transformers faiss-cpu

&#x200B;
```
---

     
 
deeplearning -  [ Free courses to learn about Large Language Models and building AI projects ](https://www.reddit.com/r/deeplearning/comments/178zu2u/free_courses_to_learn_about_large_language_models/) , 2023-11-02-0909
```
[**LangChain for LLM Application Development by Andrew Ng**](https://www.deeplearning.ai/short-courses/langchain-for-llm
-application-development/): Apply LLMs to your proprietary data to build personal assistants and specialized chatbots. 


[**Full Stack LLM Bootcamp**](https://fullstackdeeplearning.com/llm-bootcamp/): Learn best practices and tools for buil
ding LLM-powered apps 

[**Stanford CS324**](https://stanford-cs324.github.io/winter2022/): In this course, students wil
l learn the fundamentals about the modeling, theory, ethics, and systems aspects of large language models, as well as ga
in hands-on experience working with them. 

[**LangChain & Vector Databases in Production**](https://learn.activeloop.ai
/courses/langchain): Learn how to leverage LangChain, a robust framework for building applications with LLMs, and explor
e Deep Lake, a groundbreaking vector database for all AI data. 

[**Stanford CS25**](https://web.stanford.edu/class/cs25
/): In this course, learn how transformers work, and dive deep into the different kinds of transformers and how they're 
applied in different fields. 

[**LLMOps Space Discord**](https://llmops.space/discord): LLMOps Space is a global commun
ity for LLM practitioners.
```
---

     
 
deeplearning -  [ AutoGen from Microsoft ](https://www.reddit.com/r/deeplearning/comments/170hke6/autogen_from_microsoft/) , 2023-11-02-0909
```
AI agents are AI systems that can exhibit capabilities such as conducting conversations, completing tasks, reasoning, an
d seamlessly interacting with humans. 

As frameworks like LangChain build Agents as a module in their framework, Micros
oft is thinking way ahead. It has built **AutoGen**, a framework to enable seamless MULTI-agent conversation and collabo
ration to accomplish complex tasks by reasoning and working autonomously. 

Here is a video explaining the latest AutoGe
n framework from Microsoft: https://youtu.be/daigxHA2aYw?si=86alxsVZkRpz5Quv

Do you think multi-agents are the future o
f AI? Or will AI emerge in other ways? Let me know your thoughts.
```
---

     
