 
all -  [ Data Extraction using fine-tuned Llama or any other LLM? ](https://www.reddit.com/r/LocalLLaMA/comments/16feqwu/data_extraction_using_finetuned_llama_or_any/) , 2023-09-11-0910
```

Hey Reddit,

I'm working on a tool to pull data from highly irregular Excel files. I've gotten reasonable results which
 is extremely fast with standard Python coding, but it's far from perfect due to the lack of standardized templates. 

I
nterestingly, when I tested ChatGPT-4 on a sample table, it did a decent job at data extraction. However, relying solely
 on GPT-4 has its downsides like token limits and slow processing speed (and data privacy issues). Plus, splitting the E
xcel sheet to fit within these limits results in loss of context and data.

I'm considering fine-tuning a language model
 to post-process data that was in a Pandas DataFrame (perhaps converted to JSON). Has anyone had success with this appro
ach or have alternative recommendations? I've tried Langchain, but it wasn't helpful.

I have figured out to extract the
 relevant columns, but the post-processing part is where I am considering using an LLM which understands the domain and 
what needs to be extracted based on the examples I feed it.

Looking forward to your thoughts! And would be happy to ans
wer any additional questions.
```
---

     
 
all -  [ [D] Data Extraction using fine-tuned LLM? ](https://www.reddit.com/r/MachineLearning/comments/16fenlb/d_data_extraction_using_finetuned_llm/) , 2023-09-11-0910
```
Hey Reddit,

I'm working on a tool to pull data from highly irregular Excel files. I've gotten reasonable results which 
is extremely fast with standard Python coding, but it's far from perfect due to the lack of standardized templates. 

In
terestingly, when I tested ChatGPT-4 on a sample table, it did a decent job at data extraction. However, relying solely 
on GPT-4 has its downsides like token limits and slow processing speed (and data privacy issues). Plus, splitting the Ex
cel sheet to fit within these limits results in loss of context and data.

I'm considering fine-tuning a language model 
to post-process data that was in a Pandas DataFrame (perhaps converted to JSON). Has anyone had success with this approa
ch or have alternative recommendations? I've tried Langchain, but it wasn't helpful.

I have figured out to extract the 
relevant columns, but the post-processing part is where I am considering using an LLM which understands the domain and w
hat needs to be extracted based on the examples I feed it.

Looking forward to your thoughts! And would be happy to answ
er any additional questions.
```
---

     
 
all -  [ I built an AI Agent (BondAI) that actually works and has a friendly API for easy integration into ot ](https://www.reddit.com/r/ChatGPTCoding/comments/16fecm1/i_built_an_ai_agent_bondai_that_actually_works/) , 2023-09-11-0910
```
📢 I'm excited to introduce **BondAI**, an AI Agent framework and CLI, with a lightweight yet robust API making integrati
on into your own applications straightforward and easy.

**Repository:** [**https://github.com/krohling/bondai**](https:
//github.com/krohling/bondai)

# ⚡️Examples

Here's an example of buying/selling Stocks with [Alpaca Markets](https://al
paca.markets/). I strongly recommend using Paper Trading btw!

    from bondai import Agent 
    from bondai.tools.alpac
a_markets import (
        CreateOrderTool, 
        GetAccountTool, 
        ListPositionsTool
    )
    
    task = (

        'I want you to sell off all of my existing positions.'
        'Then I want you to buy 10 shares of NVIDIA with 
a limit price of $456.'
    )
    
    Agent(tools=[   CreateOrderTool(),   GetAccountTool(),   ListPositionsTool() ]).r
un(task) 

[**Here's an example**](https://github.com/krohling/bondai/tree/main/examples/online-research) of BondAI doin
g online research and [**here's a home automation example**](https://github.com/krohling/bondai/tree/main/examples/home-
automation).

# 🔍 What is BondAI?

**BondAI** is a framework crafted for the smooth integration and customization of Con
versational AI Agents. Leveraging the power of OpenAI's [**function calling support**](https://openai.com/blog/function-
calling-and-other-api-updates), it sidesteps the hurdles often encountered in building a Conversational Agent, offering 
solutions such as:

* Memory management
* Error handling
* Integrated semantic search
* A rich array of pre-existing too
ls
* Ease of crafting custom tools

Moreover, it offers a **CLI interface** that promises an impressive command line age
nt experience, available to anyone with an OpenAI API Key!

# 🏗️ Why build BondAI?

I am convinced that AI agents are go
ing to be an important architecture for the future of AI. Despite their phenomenal problem-solving abilities, the existi
ng tooling often fell short in performing simple tasks, and the frameworks appeared unnecessarily complicated. This spur
red the birth of **BondAI**, aiming to address these shortcomings and offer a more optimized environment for agent imple
mentations.

I am keen on hearing your feedback on **BondAI**'s functionality and any suggestions for improvements!

# 🛠
️ Installation & Usage

Get started with BondAI with a simple: pip install bondaiThe CLI tool offers a ready-to-use agen
t experience packed with several default tools. You can also integrate it with various tools such as Google Search, Alpa
ca Markets, and LangChain Tools to execute a myriad of tasks effectively. Detailed guides and examples for usage are ava
ilable in the README.

# 🔧 APIs and Custom Tools

The BondAI framework offers flexible APIs to build your agent and crea
te custom tools for a personalized experience. It follows a straightforward implementation approach, making the tool cre
ation process hassle-free for developers.

Examples of included Tools:

* Google and Duck Duck Go Search
* Semantic Sear
ch for Files and Websites
* Alpaca Markets
* Gmail Integration
* Easily import tools from LangChain!

# 🐋 Docker Contain
er

For a secure environment, especially while using tools with file system access, running **BondAI** within a docker c
ontainer is highly recommended. Follow the steps in the REAME to easily build and run the **BondAI** container.

🚀 Join 
the mission; contribute to BondAI! And please share feedback/ideas in the comments!
```
---

     
 
all -  [ Editing specific sections of documents? ](https://www.reddit.com/r/LocalLLaMA/comments/16fdr8r/editing_specific_sections_of_documents/) , 2023-09-11-0910
```
Are there any pipelines or perhaps a Langchain chain that would allow me to use an LLM to identify and edit specific por
tions/sections of a document based on a query? 

I understand I can have the document indexed using an abrupt character 
split of a set number of characters, and edit the relevant chunk and re-append to the document, however if the content t
hat is to be edited is spread across two chunks, I would end up having to regenerate both those chunks and re-appending 
to the original document. However I don't know how to include the context of the previous chunk to have a smooth continu
ation into the 2nd chunk.

Hence my question, is there any implementation for this? Or a simpler, better approach that I
 am missing? Any resources or help is greatly appreciated. 
```
---

     
 
all -  [ Support for additional query parameters ](https://www.reddit.com/r/LangChain/comments/16fb2p5/support_for_additional_query_parameters/) , 2023-09-11-0910
```
Hi! I would like to set a range and/or limit/offset while doing vector queries, so that instead of fetching the top n re
sults I can specify that I want the 1st, 2nd, 3,rd result and so on.

This seems to be a supported function in several o
f the integrated vector DBs, see for example [Weaviate](https://weaviate.io/developers/weaviate/search/similarity#number
-of-results) and [Supabase](https://supabase.com/docs/reference/javascript/range). How do I modify my queries using Lang
chain to make use of these functions? Is it supported? I tried asking this question in the langchain github but didn't g
et any help. I am using the JS version of Langchain.
```
---

     
 
all -  [ A RAG bot can retrieves content on demand ](https://www.reddit.com/r/LangChain/comments/16fac58/a_rag_bot_can_retrieves_content_on_demand/) , 2023-09-11-0910
```
hey guys, I implemented A RAG bot can retrieves web/local content on demand, it uses [ActionWeaver](https://github.com/T
engHu/ActionWeaver) to orchestrate llama index and langchain tools to combine search and RAG.

[Github](https://github.c
om/TengHu/Interactive-RAG)

[Interactive RAG Demo](https://www.loom.com/share/f3d7a8e80b3e47618d27730e01eb4bca)
```
---

     
 
all -  [ A RAG bot can retrieves content on demand ](https://www.reddit.com/r/LlamaIndex/comments/16faasl/a_rag_bot_can_retrieves_content_on_demand/) , 2023-09-11-0910
```
hey guys, I implemented A RAG bot can retrieves web/local content on demand, it uses [ActionWeaver](https://github.com/T
engHu/ActionWeaver) to orchestrate llama index and langchain tools to combine search and RAG.

[Github](https://github.c
om/TengHu/Interactive-RAG)

[Interactive RAG Demo](https://www.loom.com/share/f3d7a8e80b3e47618d27730e01eb4bca)

📷
```
---

     
 
all -  [ Where is the error stack trace...? ](https://www.reddit.com/r/LangChain/comments/16f72wy/where_is_the_error_stack_trace/) , 2023-09-11-0910
```
I get the error below sometimes which would be fine if I could trace the problem and debug but I can't for the love of m
e figure out why the stack trace is hidden because this is all I see in my terminal 

[LLM run error](https://preview.re
dd.it/3ltiwnihxgnb1.png?width=1320&format=png&auto=webp&s=ccc62cf930f9d91c48022dae69c5fea0fcf11e04)

How do you go about
 this?
```
---

     
 
all -  [ Multiple models running on one system ](https://www.reddit.com/r/LocalLLaMA/comments/16f4177/multiple_models_running_on_one_system/) , 2023-09-11-0910
```
Is it possible to run multiple models at the same time on the same system and let them interact with each other on somet
hing like langchain?
```
---

     
 
all -  [ I made a KNOWLEDGE ASSISTANT. ](https://www.reddit.com/r/LangChain/comments/16f1i6b/i_made_a_knowledge_assistant/) , 2023-09-11-0910
```
I made a **KNOWLEDGE ASSISTANT**, which allows you to upload PDF, WORD, TXT, and CSV documents, vectorize and store the 
documents after splitting, and combine them with the OpenAI GPT model to ask questions and return answers. Visual parame
ter adjustment is provided at each step. Turning on DEBUG mode lets you see information such as similarity search, promp
t words, produced content, etc.

&#x200B;

https://reddit.com/link/16f1i6b/video/wuywix0qtfnb1/player

Please let me kno
w what you think.
```
---

     
 
all -  [ LLMChain timeout error with OpenAI ](https://www.reddit.com/r/LangChain/comments/16f0nkg/llmchain_timeout_error_with_openai/) , 2023-09-11-0910
```
I'm running a series of calls using a vary simple LLMChain and very often get a TimeoutError.The error crashes my server
 and doesn't retry automatically (I read somewhere that LangChain should handle the retries automatically).

Here's the 
full error I'm getting:

    Error in handler LangChainTracer, handleChainError: TimeoutError: The operation was aborted
 due to timeout
    file:///Users/[redacted...]/node_modules/langchain/dist/util/openai.js:6
            error = new Err
or(e.message);
                    ^
    
    Error [TimeoutError]: Request timed out.
        at wrapOpenAIClientError 
(file:///Users/[redacted...]/node_modules/langchain/dist/util/openai.js:6:17)
        at file:///Users/[redacted...]/nod
e_modules/langchain/dist/chat_models/openai.js:517:31
        at process.processTicksAndRejections (node:internal/proces
s/task_queues:95:5)
        at async RetryOperation._fn (/Users/[redacted...]/node_modules/p-retry/index.js:50:12) {
   
   attemptNumber: 1,
      retriesLeft: 6
    }
    
    Node.js v20.5.1

Looking into LangSmith I can see the timed out
 requests have waited for 600 seconds. That's a lot!

* Is there anything I can do so LangChain handles the retries?
* I
f not, what's the best way to handle the retries. I was looking into [handleChainError()](https://js.langchain.com/docs/
api/callbacks/classes/LangChainTracer#handlechainerror)
* Can I reduce the waiting time to way less than 600 seconds?
```
---

     
 
all -  [ JS/TS EXAMPLE REPOS? ](https://www.reddit.com/r/LangChain/comments/16eyp9z/jsts_example_repos/) , 2023-09-11-0910
```
Looking to learn how to build a self hosted langchain bot that will use scrapers to pull in data. Not super sure where t
o start. I’ve gone through some docs but I’d love to hear some recommendations of stacks or read through some repos to l
earn how to build properly. 

Thanks. Xo
```
---

     
 
all -  [ Query Length in FAISS for Document Retrieval ](https://www.reddit.com/r/LangChain/comments/16ewert/query_length_in_faiss_for_document_retrieval/) , 2023-09-11-0910
```
Hello fellow LangChainers,

I'm leveraging FAISS for my vector store and I'm curious about the optimal query length to r
etrieve pertinent documents. My goal is to develop an app that succinctly summarizes business reports tailored to specif
ic roles within a company. For instance, imagine a Head of Finance who prefers a concise overview rather than reading an
 entire report.

To form my query, I've been incorporating the job responsibilities of the target persona. However, I'm 
concerned that my query might be too extensive, leading to less relevant results.   


**Query** (that goes into FAISS v
ia similarity\_search\_with\_score method):

    
Based on the target persona's responsibilities, extract insights from 
a company's annual report.
    Target Persona: Head of Finance, a key figure in the Executive Leadership Team (ELT), who
 emphasizes financial reporting, risk management, and compliance. They play a crucial role in guiding the company's fina
ncial direction, ensuring adherence to regulations, and building relationships with external entities.
    Key Responsib
ilities:
    Overseeing organizational financial reporting, encompassing monthly summaries, budget projections, long-ter
m financial plans, and mandatory reports.
    Offering robust financial guidance to the ELT for informed business decisi
ons.
    Presenting financial outcomes and insights to the Board.
    Central to shaping the company's strategy.
    Sup
ervising the company's tax matters, collaborating with external tax consultants when needed.
    Managing company cash f
low and implementing appropriate treasury controls.

**Given the above, any insights on how I can optimize my query for 
better results in FAISS would be greatly appreciated!**
```
---

     
 
all -  [ Why is Langchain MIT and not gplv3 licensed? ](https://www.reddit.com/r/LangChain/comments/16ewbfn/why_is_langchain_mit_and_not_gplv3_licensed/) , 2023-09-11-0910
```
Langchain seems to use multiple libraries like PuMyPDF which is licensed as gplv3.

With this in mind, how and why does 
langchain claim to be licensed under a MIT license? 

Trying not to get into legal troubles here. If someone could expla
in it would be very much appreciated.
```
---

     
 
all -  [ langChain model which can process json data ](https://www.reddit.com/r/LangChain/comments/16ew6cr/langchain_model_which_can_process_json_data/) , 2023-09-11-0910
```
\-----------------------------------------------------------------------------------------------------------------------
----------  
import os  
import json  
from pprint import pprint  
from langchain.llms.openai import OpenAI  
from langc
hain.agents import create\_json\_agent  
from langchain.tools.json.tool import JsonSpec  
from langchain.agents.agent\_t
oolkits import JsonToolkit  
os.environ\['OPENAI\_API\_KEY'\] = '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'  

with open('small-test-data.txt') as f:  
data = json.load(f)  
print(type(data))  


json\_spec = JsonSpec(dict\_=dict(d
ata), max\_value\_length=4000)  
json\_toolkit = JsonToolkit(spec=json\_spec)  
json\_agent\_executor = create\_json\_ag
ent(  
 llm=OpenAI(temperature=0), toolkit=json\_toolkit, verbose=False  
)  


result = json\_agent\_executor.run(  
 \
# 'give the price of product in integer format who have Underwear & Nightwear for man with white color'  
 'Give me the 
name of Underwears whose price is less than 500'  
 \# 'give me all the data of product whose name is 'Pack of 3 - Solid
 Trunks with Elasticised Waistband' in json format'  
)  


pprint(result)  
\------------------------------------------
---------------------------------------------------------------------------------------

  


this model is working perf
ectly for small data set but I need it to work for a large data set, please help me.
```
---

     
 
all -  [ Token request wildly jumps randomly? ](https://www.reddit.com/r/LangChain/comments/16em51x/token_request_wildly_jumps_randomly/) , 2023-09-11-0910
```
This is driving me crazy.  I'm running the SQL Agent and gathing insights from a mysql database. 

It works like 75% of 
the time. the other times it says I'm using 8000+ tokens. 

It seems to mess up when I add a function into that script o
r change anything in the script...

agent\_executor = create\_sql\_agent(  
 llm=OpenAI(temperature=0),  
 toolkit=SQLDa
tabaseToolkit(db=db, llm=OpenAI(temperature=0)),  
 verbose=True,  
 agent\_type=AgentType.ZERO\_SHOT\_REACT\_DESCRIPTIO
N,  
 top\_k=10000  
)  


result = agent\_executor.run('In 'db', up to 100 rows, find unique URLs in the 'From' column,
 decipher company name, rank & list top 10')  

```
---

     
 
all -  [ I built an AI Agent (BondAI) that actually works and has a friendly API for easy integration into ot ](https://www.reddit.com/r/AutoGPT/comments/16eilta/i_built_an_ai_agent_bondai_that_actually_works/) , 2023-09-11-0910
```
📢 Hello AI agent enthusiasts, developers, and learners!

I'm thrilled to introduce you to **BondAI**, an AI Agent framew
ork and CLI, with a lightweight yet robust API making integration into your own applications straightforward and easy.


**Repository:** [**https://github.com/krohling/bondai**](https://github.com/krohling/bondai)

https://preview.redd.it/hr
i7x7e20bnb1.png?width=1456&format=png&auto=webp&s=a24e6bcca613e4d961bc36eedf9131dd0f034d2a

&#x200B;

## ⚡️Examples

Her
e's an example of buying/selling Stocks with [Alpaca Markets](https://alpaca.markets/). I strongly recommend using Paper
 Trading btw!

    from bondai import Agent
    from bondai.tools.alpaca_markets import CreateOrderTool, GetAccountTool,
 ListPositionsTool
    
    task = '''I want you to sell off all of my existing positions.
    Then I want you to buy 10
 shares of NVIDIA with a limit price of $456.'''
    
    Agent(tools=[
      CreateOrderTool(),
      GetAccountTool(),

      ListPositionsTool()
    ]).run(task)

[**Here's an example**](https://github.com/krohling/bondai/tree/main/exampl
es/online-research) of BondAI doing online research and [**here's a home automation example**](https://github.com/krohli
ng/bondai/tree/main/examples/home-automation).

## 🔍 What is BondAI?

**BondAI** is a framework crafted for the smooth i
ntegration and customization of Conversational AI Agents. Leveraging the power of OpenAI's [**function calling support**
](https://openai.com/blog/function-calling-and-other-api-updates), it sidesteps the hurdles often encountered in buildin
g a Conversational Agent, offering solutions such as:

* Memory management
* Error handling
* Integrated semantic search

* A rich array of pre-existing tools
* Ease of crafting custom tools

Moreover, it offers a **CLI interface** that prom
ises an impressive command line agent experience, available to anyone with an OpenAI API Key!

## 🏗️ Why build BondAI?


I am convinced that AI agents hold the future. Despite their phenomenal problem-solving abilities, the existing tooling 
often fell short in performing simple tasks, and the frameworks appeared unnecessarily complicated. This spurred the bir
th of **BondAI**, aiming to address these shortcomings and offer a more optimized environment for agent implementations.


I am keen on hearing your feedback on **BondAI**'s functionality and any suggestions for improvements!

## 🛠️ Installa
tion & Usage

Get started with BondAI with a simple: pip install bondai  
The CLI tool offers a ready-to-use agent exper
ience packed with several default tools. You can also integrate it with various tools such as Google Search, Alpaca Mark
ets, and LangChain Tools to execute a myriad of tasks effectively. Detailed guides and examples for usage are available 
in the README.

### 🔧 APIs and Custom Tools

The BondAI framework offers flexible APIs to build your agent and create cu
stom tools for a personalized experience. It follows a straightforward implementation approach, making the tool creation
 process hassle-free for developers.

Examples of included Tools:

* Google and Duck Duck Go Search
* Semantic Search fo
r Files and Websites
* Alpaca Markets
* Gmail Integration
* Easily import tools from LangChain!

### 🐋 Docker Container


For a secure environment, especially while using tools with file system access, running **BondAI** within a docker cont
ainer is highly recommended. Follow the steps in the REAME to easily build and run the **BondAI** container.

🚀 Join the
 mission; contribute to BondAI! And please share feedback/ideas in the comments!
```
---

     
 
all -  [ Langchain conversation history with ChatGPT? ](https://www.reddit.com/r/ChatGPTPro/comments/16ehksj/langchain_conversation_history_with_chatgpt/) , 2023-09-11-0910
```
In Langchain there are many types of conversational memory that adds conversation history into the prompt. I get it's us
eful for pre-ChatGPT era, but is it still useful for ChatGPT? ChatGPT has conversation history in itself so wonder what'
s the point of adding conversation history in the system prompt (other that summary)
```
---

     
 
all -  [ Fine-Tuning Handler / Data Preparation using Langchain ](https://www.reddit.com/r/LangChain/comments/16efnh7/finetuning_handler_data_preparation_using/) , 2023-09-11-0910
```
Is there something similar in langchain to the finetune handler in llama\_index? [https://gpt-index.readthedocs.io/en/v0
.8.19/examples/finetuning/react\_agent/react\_agent\_finetune.html](https://gpt-index.readthedocs.io/en/v0.8.19/examples
/finetuning/react_agent/react_agent_finetune.html)

Basically, we want to log all calls (exact parameters/messages to Op
enai so that we can use that data to finetune gpt-3.5. Right now, we're not really sure how the calls are made to the ll
m behind the scenes. Does the chat-conversational-react-description break down the entire message we see in verbose true
 mode in different messages (the dictionary that openai expects) or are they sending it all in the 'system' message?

We
 want to know what 'role' certain sections of the input to the llm are so that we can prepare the data for fine-tuning a
ppropriately.

Any help with this would be appreciated!
```
---

     
 
all -  [ I launched NextJS project & don't know what to do next (feedback) ](https://www.reddit.com/r/nextjs/comments/16ee473/i_launched_nextjs_project_dont_know_what_to_do/) , 2023-09-11-0910
```
Hi there, this question is not going to be highly technical, but I'm rather seeking some guidance from more experienced 
developers regarding to career decisions.  


I started learning code roughly 6 months ago after I quit my COO role at s
tart up. Long story short today, I am able to launch a full stack application, I know how Client/Server Components work,
 I understand API, Tailwind CSS, Supabase, Auth, OpenAI, Langchain Functions, Streaming etc. etc. etc.  


This is the a
pp that roughly present my skills: [copycopter.ai](https://copycopter.ai) 

&#x200B;

**Now the problem is, I don't real
ly know what to do next.**  
My dream would be learn further and build more, so that at some point, I can make money fro
m my own things. For now, however, I struggle to find people interested in my SaaS, so I probably have some work to do i
n terms of 'go to market' and 'PMF'.  


I could look for a job as a developer, but the only thing I know is NextJS App 
Router and I feel like I'm not yet ready to get a reasonably paid job as a dev. On the other hand, I see so many people 
that create much worse products yet they openly talk about the readiness to get employed.  


I have a lot of experience
 in no code, process automation, Zappier, operations management etc. so I could bring good value to any startup.   


**
What would you do if you were me?** I'm kina struggling to find the right path now.  
**What to learn next? What kind of
 jobs should I seek for?**

&#x200B;

Cheers,  
K.
```
---

     
 
all -  [ ChatGPT API seems to be producing much worse results than the Web Version ](https://www.reddit.com/r/OpenAI/comments/16ec4gs/chatgpt_api_seems_to_be_producing_much_worse/) , 2023-09-11-0910
```
I am using gpt 3.5 turbo on both the API and the web version, yet on the API, I am not getting the results that I get on
 the web version, with no finetuning, langchain, or any other modifications. Is there something wrong? How can I fix thi
s?
```
---

     
 
all -  [ quantized Falcon-7b is too slow ](https://www.reddit.com/r/LangChain/comments/16ea97a/quantized_falcon7b_is_too_slow/) , 2023-09-11-0910
```
Hi, I use 4-bit quantized version of Falcon 7-b: [https://huggingface.co/TheBloke/falcon-7b-instruct-GGML](https://huggi
ngface.co/TheBloke/falcon-7b-instruct-GGML) on my 8 GB RAM laptop, but it took 100 seconds to respond on 'hello' message
. Anything beyond takes multiple minutes. Model's file size is only 4,06 GB. Any other 7 billion params quantized model 
such as LLama2 has same issues. Do I anything wrong since GGML is here to allow models to run on consumer hardware witho
ut GPU? Can I speed up the model? 

    from langchain import CTransformers
    
    llm = CTransformers(
        model=
'path to model',
        model_type='falcon',
        config={
            'max_new_tokens': 128,
            'temperatu
re': 0.01
        }
    )
```
---

     
 
all -  [ Confused about the results trying to QA a web source ](https://www.reddit.com/r/LangChain/comments/16e6n37/confused_about_the_results_trying_to_qa_a_web/) , 2023-09-11-0910
```
I've just started with LLMs and LangChain, but I really need some help to understand the key concepts around RAG. I've r
ead it reduces the risk of hallucinations using your data, so I've been trying to build a basic prototype myself. I've e
nded up copying the code from [https://python.langchain.com/docs/integrations/llms/ollama](https://python.langchain.com/
docs/integrations/llms/ollama), this is what I've got:

    llm = Ollama(
     base_url='http://localhost:11434',
     m
odel='llama2',
     callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]),
      )
    
    loader = WebB
aseLoader('https://lilianweng.github.io/posts/2023-06-23-agent/')
    data = loader.load()
    text_splitter = Recursive
CharacterTextSplitter(chunk_size=100, chunk_overlap=50)
    all_splits = text_splitter.split_documents(data)
    
    
 
   vectorstore = Chroma.from_documents(
     documents=all_splits, embedding=HuggingFaceEmbeddings()
     )
    
    fro
m langchain.prompts import PromptTemplate
    prompt_template = '''Use the following pieces of context to answer the que
stion at the end. If you don't know the answer, just say that you don't know, don't try to make up an answer. Only use p
rovided context, don't try to generate an answer based on assumptions.
    
    {context}
    
    Question: {question}

    Helpful Answer:'''
    QA_CHAIN_PROMPT = PromptTemplate(
        template=prompt_template, input_variables=['context
', 'question']
    )
    
    chain_type_kwargs = {'prompt': QA_CHAIN_PROMPT}
    qa_chain = RetrievalQA.from_chain_type
(
            llm,
            retriever=vectorstore.as_retriever(),
            chain_type_kwargs={'prompt': QA_CHAIN_P
ROMPT}
    )
    
    question = 'What are the various approaches to Task Decomposition for AI Agents?'
    result = qa_
chain({'query': question})

After unsuccessful experiments I even use the original web source and the question from the 
example in the documentation. But the output is rather disappointing (lots of hallucinations, perhaps coming from pre-tr
aining datasets, no information coming from the linked web page): 

>Based on the provided context, there are several ap
proaches to task decomposition for AI agents. Here are some of them:  
>  
>  
>  
>1. LLM with simple prompting: As men
tioned in the context, the agent can use language models (LLMs) with simple prompts like 'Steps for XYZ.' or 'What are t
he steps for XYZ?' to break down large tasks into smaller subgoals.  
>  
>2. Goal-based decomposition: The agent can de
compose a task into smaller subgoals based on its goals. For example, if the goal is to make a cup of coffee, the subgoa
ls could be 'obtain coffee beans,' 'boil water,' 'use coffee filter,' etc.  
>  
>3. Workflow-based decomposition: The a
gent can decompose a task into smaller subgoals based on a workflow or a series of steps involved in completing the task
. For example, if the task is to organize a trip, the subgoals could be 'book flight tickets,' 'make hotel reservations,
' 'plan itinerary,' etc.  
>  
>4. Hybrid approach: The agent can use a combination of goal-based and workflow-based dec
omposition to break down large tasks into smaller subgoals. For example, the agent can use goals to determine the overal
l task and then break it down into smaller subgoals based on a workflow.  
>  
>5. Machine learning-based approaches: Th
ere are various machine learning-based approaches to task decomposition, such as using neural networks to learn patterns
 in data or using reinforcement learning to learn how to break down tasks into smaller subgoals.

&#x200B;

I'm lost at 
this point, I thought using retriever=vectorstore.as\_retriever(), should have enforced using the source and only it as 
the context? Is there a mistake in the code or am I misunderstanding how it should work? 
```
---

     
 
all -  [ Implementing a few-shot template using Langchain and Llama (keywords extraction) ](https://www.reddit.com/r/LanguageTechnology/comments/16e22c5/implementing_a_fewshot_template_using_langchain/) , 2023-09-11-0910
```
My goal is as follows: I have main keywords, e.g., 'data warehouse zoom meeting participants.' I want to input only a sp
ecific keyword, and the model would generate more keywords, e.g., 'zoom,' 'meeting,' 'meeting participants,' 'company me
eting,' and so on. 

Below, I'm sharing a link to Colab; maybe someone could take a look and suggest something: https://
colab.research.google.com/drive/1dLdCsr39uwj3S0OaDi1H4D38Tgj266hH?usp=sharing


This version won't work if you don't hav
e nvidia gpu.
```
---

     
 
all -  [ Implementing a few-shot template using Langchain and Llama (keywords extraction) ](https://www.reddit.com/r/LangChain/comments/16e201i/implementing_a_fewshot_template_using_langchain/) , 2023-09-11-0910
```
My goal is as follows: I have main keywords, e.g., 'data warehouse zoom meeting participants.' I want to input only a sp
ecific keyword, and the model would generate more keywords, e.g., 'zoom,' 'meeting,' 'meeting participants,' 'company me
eting,' and so on. My script looks like this:

    model_id = 'meta-llama/Llama-2-13b-chat-hf'
    device = f'cuda:{cuda
.current_device()}' if cuda.is_available() else 'cpu'; print(device)
    
    <here I quantize and load the model, I wil
l skip>
    
    
    from langchain import PromptTemplate,  LLMChain
    from langchain.prompts.few_shot import FewShot
PromptTemplate
    
    examples = [
      {
        'Text': 'data warehouse zoom meeting participants',
        'Keywor
ds': 
    '''
    - 'data warehouse zoom meeting participants'
    - 'data warehouse'
    - 'zoom meeting'
    - 'meetin
g participants'
    - 'meeting'
    - 'zoom'
    '''
      },
      {
        'Text': 'published monthly chart',
       
 'Keywords': 
    '''
    - 'published monthly chart'
    - 'monthly chart'
    - 'revenue'
    - 'charts'
    - 'publis
hed chart'
    '''
      }
    ]
    
    example_prompt = PromptTemplate(input_variables=['Text', 'Keywords'], template
='You are a professional assistant for extracting keywords from text fragments given to you. Text fragment for keywords 
extraction is: {Text}\n Extracted Keywords:{Keywords}')
    
    print(example_prompt.format(**examples[0]))
    
    fe
w_shot_prompt = FewShotPromptTemplate(
        examples=examples,
        example_prompt=example_prompt,
        suffix=
'You are a professional assistant for extracting keywords from text fragments given to you. Text fragment for keywords e
xtraction is: {input}',
        input_variables=['input']
    )
    
    print(few_shot_prompt.format(input='my dataset'
))

Print result:

You are a professional assistant for extracting keywords from text fragments given to you. Text fragm
ent for keywords extraction is: data warehouse zoom meeting participants  Extracted Keywords: - 'data warehouse zoom mee
ting participants' - 'data warehouse' - 'zoom meeting' - 'meeting participants' - 'meeting' - 'zoom'   You are a profess
ional assistant for extracting keywords from text fragments given to you. Text fragment for keywords extraction is: publ
ished monthly chart  Extracted Keywords: - 'published monthly chart' - 'monthly chart' - 'revenue' - 'charts' - 'publish
ed chart'   You are a professional assistant for extracting keywords from text fragments given to you. Text fragment for
 keywords extraction is: my dataset

&#x200B;

I don't really know what to do next :(
```
---

     
 
all -  [ Example using vector dB retriever for top k docs to set context of LLM prompt ](https://www.reddit.com/r/LangChain/comments/16e1lib/example_using_vector_db_retriever_for_top_k_docs/) , 2023-09-11-0910
```
Hi,

&#x200B;

I'd like to retrieve top k passages from a vector store and insert them into a prompt to set the context 
for LLM text generation. Tried search but not finding nice examples, grateful for any pointers, thanks! 
```
---

     
 
all -  [ Unemployed and not sure how to represent on resume; not getting much traction. ](https://www.reddit.com/r/resumes/comments/16dr2fe/unemployed_and_not_sure_how_to_represent_on/) , 2023-09-11-0910
```
Thanks in advance for any advice!  


I'm applying for A) product manager, and B) product marketing manager jobs. (Somet
imes 'Senior' level, sometimes not). I have generally worked in 'tech' over my previous recent roles, but my experience 
is kind of a grab bag.  


I'm definitely stretching my qualifications a bit to land a tech PM/PMM role. Worth noting th
at I've done a lot of projects involving AI recently because that's a particular area of interest and often where I'm ap
plying.  


Issues I know I have to overcome:  


* Weird / small companies on my resume. I've started a couple companie
s and my recent work experiences aren't at 'known' companies. 
* I come off too senior (?). Since I've founded a couple 
companies, I have things like 'CEO' on my resume. But of a 15 person company... Nonetheless, I've been told before that 
hiring managers were worried I wouldn't be 'satisfied with the level of responsibility in this role.'
* I'm currently un
employed. I tried to remedy this by (truthfully) saying I've been doing self employed work. However, I don't know if I'm
 describing this correctly or whether it's even helpful to have that on here.

My main questions are:

&#x200B;

1. Are 
there any noticeable things I might consider changing to address the issues outlined above? (Or other issues you perceiv
e?)
2. Should I have an Overview section at all? What about the self employed Experience?  


Thanks again!   


https:/
/preview.redd.it/vti98hceh4nb1.png?width=674&format=png&auto=webp&s=870c5a55a60369df890a331bc5f433ae0f44a021
```
---

     
 
all -  [ Input variable for Prompt Template won't work with retrieval QA chain ](https://www.reddit.com/r/LangChain/comments/16djn0n/input_variable_for_prompt_template_wont_work_with/) , 2023-09-11-0910
```
&#x200B;

Hi Everyone, I have the following prompt template which requires an input variable {userName}:

    const prom
ptTemplate = `Use the following pieces of context to answer the question of {userName} at the end. If you don't know the
 answer, just say that you don't know, don't try to make up an answer.
    {context}
    
    Question: {question}
    A
nswer:`;
    
    const prompt = PromptTemplate.fromTemplate(promptTemplate);
    
    const chain = RetrievalQAChain.fr
omLLM(
      new ChatOpenAI({ modelName: 'gpt-3.5-turbo' }),
      vectorStore.asRetriever(),
      {
        returnSour
ceDocuments: true,
        prompt,
      }
    


&#x200B;

    const result = await chain.call({
        query: input,

        userName: 'James Conway'
      });
    

Calling the chain as shown above and giving query and userName as argum
ents outputs an error 'Uncaught Error: Missing value for input userName'.   


Has anyone got an idea why this is happen
ing? Thank you
```
---

     
 
all -  [ Using a RAG Model for Semantic Search & Document Question and Answering ](https://www.reddit.com/r/datascience/comments/16divx4/using_a_rag_model_for_semantic_search_document/) , 2023-09-11-0910
```
I am unsure if this is the right sub to ask such a question I'll try my best to provide as much context of my issue.

I 
am currently a IT Researcher looking at using RAG Models for document question and answering. I am working with Multiple
 500+ Page documents filled with charts, numbers, and text. We use these documents to record and track information in sp
readsheets. The current workflow is using a small team to go through the documents manually looking for the information 
they need to record in their sheets. The documents are too big to use a Ctrl + F keyword search so I was looking at RAG 
Models to make searching through these documents more effective.

I have been using ThirdAI's Pocket LLM (open to try al
ternative or open source RAG Models) to try to test the effectiveness of such a strategy but I have had issues properly 
prompting/searching for what I want. I have no problem building my own RAG Model using langchain I am just wondering if 
this is the best route for such an issue. Data privacy is not a concern because the documents we will be using are publi
cly available information. Data accuracy however is pretty important so I was wondering if hallucination is a factor whe
n dealing with RAG models.

It's fine if embeddings are expensive. Automating this process is far more valuable. Thanks 
for any insight or feedback and I will be happy to clarify anything just ask.
```
---

     
 
all -  [ LangChain based chatbot in Teams ](https://www.reddit.com/r/LangChain/comments/16dgoaz/langchain_based_chatbot_in_teams/) , 2023-09-11-0910
```
Is there any way to develop a chatbot in Teams (as a Teams contact I mean), that would be programmed using LangChain?
An
y pointer?
```
---

     
 
all -  [ How to parse AgentExecutor (ReAct) feedback to Streamlit? ](https://www.reddit.com/r/LangChain/comments/16dbyxa/how_to_parse_agentexecutor_react_feedback_to/) , 2023-09-11-0910
```
Hey y'all,

I wanted to put my ReAct agent on Streamlit. Thank you for the recommendations, btw, that was exactly what I
 was looking for.

The problem that I have is that the agent pipes the feedback into the shell but not the screen. Docum
entation doesn't really help.

Here is my agent definition

    llm = ChatOpenAI(temperature=0, model_name='gpt-3.5-turb
o')
    tools = load_tools(['human', 'serpapi', 'llm-math'], llm=llm)
    
    prefix = '''Some agent definition.
      
          Ask appropriate questions. 
                You have access to the following tools:'''
    suffix = '''Begin!'

    
    {chat_history}
    Question: {input}
    {agent_scratchpad}'''
    
    output_parser = CustomOutputParser()
 
   prompt = ZeroShotAgent.create_prompt(
        tools,
        prefix=prefix,
        suffix=suffix,
        input_vari
ables=['input', 'chat_history', 'agent_scratchpad'],
    )
    memory = ConversationBufferMemory(memory_key='chat_histor
y')
    llm_chain = LLMChain(llm=llm, prompt=prompt)
    agent = ZeroShotAgent(llm_chain=llm_chain, tools=tools, verbose
=True, output_parser=output_parser)
    agent_chain = AgentExecutor.from_agent_and_tools(
        agent=agent, tools=too
ls, verbose=True, memory=memory
    )

Here is the streamlit part

    if prompt := st.chat_input('What is up?'):
      
  st.session_state.messages.append({'role': 'user', 'content': prompt})
        with st.chat_message('user'):
          
  st.markdown(prompt)
    
        with st.chat_message('assistant'):
            message_placeholder = st.empty()
     
       full_response = ''
            for response in agent_chain.run(st.session_state.messages):
                full_r
esponse += response.choices[0].delta.get('content', '')
                message_placeholder.markdown(full_response + '▌'
)
            message_placeholder.markdown(full_response)
        st.session_state.messages.append({'role': 'assistant',
 'content': full_response})

What I want is that if the app queries 'human' it should pop the question to the chat inter
face.

&#x200B;

&#x200B;

&#x200B;
```
---

     
 
all -  [ CSV_AGENT HELP ](https://www.reddit.com/r/LangChain/comments/16dbjqy/csv_agent_help/) , 2023-09-11-0910
```
I'm trying to build a CSV Agent that holds memory of the previous conversations. Since , csv\_agent() does not support m
emory at the moment , how should I go about it ?
```
---

     
 
all -  [ LLM for context answers ](https://www.reddit.com/r/LangChain/comments/16datg3/llm_for_context_answers/) , 2023-09-11-0910
```
Hey guys, 
I’m looking for a good LLM that can take an input from a context and answer straight questions and is not ope
nai. Any suggestions?

If it works well with langchain agents, I’d be over the moon :-)
```
---

     
 
all -  [ How to architect a Rails monolith + modules? ](https://www.reddit.com/r/rails/comments/16d9a86/how_to_architect_a_rails_monolith_modules/) , 2023-09-11-0910
```
I want to use some services that I think are better in other languages, such as Langchain in Python or using Go to encod
e video (examples). But I want to keep most of the code in Rails.

The problem is that when I look for material about th
is, it always falls into extremes. Either you just use monoliths or you use microservices with Kafka, API Gateway, Clean
 Architecture and a bunch of other things.

What is the most suitable architecture for something like what I've describe
d? Rails handling most of the code, but freedom to create modules or services in other languages and frameworks. I belie
ve my biggest curiosity is how to orchestrate the communication between them in a consistent and secure way.
```
---

     
 
all -  [ Retrieve from FAQ documents ](https://www.reddit.com/r/LangChain/comments/16d8jpv/retrieve_from_faq_documents/) , 2023-09-11-0910
```
How would you best split and embed FAQ documents to be able to retrieve from them in something like a `ConversationalRet
rievalChain`?

\- Would you always put a single Question and Answer pair into a single chunk? How do you handle cases wh
ere such a Q&A pair is bigger than your max chunk size?

\- or would you rather just embed the questions and search them
 for similarity and return the answer if a retrieved question scores high?

Are there any configs/retrievers/chains/apps
 floating around doing this?
```
---

     
 
all -  [ Gen AI Jobs - Freelance Marketplace ](https://www.reddit.com/r/mlops/comments/16d7ipo/gen_ai_jobs_freelance_marketplace/) , 2023-09-11-0910
```
 

Hi everyone!

As we've been monitoring the latest developments in generative AI, we've noticed that at least four typ
es of jobs have emerged: AI Artists (specializing in Midjourney, Stable Diffusion, ControlNet, A1111, etc), Video Artist
s (familiar with RunwayML Gen2, Pika Labs, Fulljourney, etc), Prompt Engineers/Consultants, and LLM Model Trainers.

We'
ve decided to create Gen AI Jobs - Freelance Marketplace, a platform solely dedicated to these roles and any future jobs
 that may arise in this exciting field. Our mission is to become the one-stop-shop for generative AI professionals.  
Ex
clusive Access: Be among the first to access a marketplace tailored to your unique skills.  
Diverse Opportunities: Work
 on projects that align with your expertise and interests.  
Community Building: Connect with like-minded professionals 
and potential clients.

Join Our Waitlist: We're still in beta, but you can secure a front-row seat to the future by joi
ning our waitlist at [http://genaijobs.co](http://genaijobs.co/)  
Complete Our Survey: Fill out our short survey to hel
p us tailor the platform to your needs.

We're Looking For Expertise with: [OpenAI](https://www.linkedin.com/company/ope
nai/), [Anthropic](https://www.linkedin.com/company/anthropicresearch/), [Stability AI](https://www.linkedin.com/company
/stability-ai/) [Pika Labs](https://www.linkedin.com/in/ACoAAEZTw2oBGyi3YZbK-hM3l-0H9RhA5L-1Ecc), [Midjourney](https://w
ww.linkedin.com/company/midjourney/), [LangChain](https://www.linkedin.com/company/langchain/), [TensorFlow User Group (
TFUG)](https://www.linkedin.com/company/tensorflow/), [Hugging Face](https://www.linkedin.com/company/huggingface/), [Gi
tHub](https://www.linkedin.com/company/github/) [Runway](https://www.linkedin.com/company/runwayml/), Leonardo AI, [Elev
enLabs](https://www.linkedin.com/company/elevenlabsio/), [NVIDIA](https://www.linkedin.com/company/nvidia/), [Microsoft 
Azure](https://www.linkedin.com/company/microsoft-azure/) [Amazon Web Services (AWS)](https://www.linkedin.com/company/a
mazon-web-services/), etc.

[http://genaijobs.co](http://genaijobs.co/)
```
---

     
 
all -  [ Gen AI Jobs - Freelance Marketplace ](https://www.reddit.com/r/LargeLanguageModels/comments/16d7htx/gen_ai_jobs_freelance_marketplace/) , 2023-09-11-0910
```
  Hi everyone!

As we've been monitoring the latest developments in generative AI, we've noticed that at least four type
s of jobs have emerged: AI Artists (specializing in Midjourney, Stable Diffusion, ControlNet, A1111, etc), Video Artists
 (familiar with RunwayML Gen2, Pika Labs, Fulljourney, etc), Prompt Engineers/Consultants, and LLM Model Trainers.  


W
e've decided to create Gen AI Jobs - Freelance Marketplace, a platform solely dedicated to these roles and any future jo
bs that may arise in this exciting field. Our mission is to become the one-stop-shop for generative AI professionals.  

Exclusive Access: Be among the first to access a marketplace tailored to your unique skills.  
Diverse Opportunities: Wo
rk on projects that align with your expertise and interests.  
Community Building: Connect with like-minded professional
s and potential clients.  


Join Our Waitlist: We're still in beta, but you can secure a front-row seat to the future b
y joining our waitlist at [http://genaijobs.co](http://genaijobs.co/)  
Complete Our Survey: Fill out our short survey t
o help us tailor the platform to your needs.  


We're Looking For Expertise with: [OpenAI](https://www.linkedin.com/com
pany/openai/), [Anthropic](https://www.linkedin.com/company/anthropicresearch/), [Stability AI](https://www.linkedin.com
/company/stability-ai/) [Pika Labs](https://www.linkedin.com/in/ACoAAEZTw2oBGyi3YZbK-hM3l-0H9RhA5L-1Ecc), [Midjourney](h
ttps://www.linkedin.com/company/midjourney/), [LangChain](https://www.linkedin.com/company/langchain/), [TensorFlow User
 Group (TFUG)](https://www.linkedin.com/company/tensorflow/), [Hugging Face](https://www.linkedin.com/company/huggingfac
e/), [GitHub](https://www.linkedin.com/company/github/) [Runway](https://www.linkedin.com/company/runwayml/), Leonardo A
I, [ElevenLabs](https://www.linkedin.com/company/elevenlabsio/), [NVIDIA](https://www.linkedin.com/company/nvidia/), [Mi
crosoft Azure](https://www.linkedin.com/company/microsoft-azure/) [Amazon Web Services (AWS)](https://www.linkedin.com/c
ompany/amazon-web-services/), etc.  


[http://genaijobs.co](http://genaijobs.co/) 
```
---

     
 
all -  [ Chains and Agents ](https://www.reddit.com/r/aiengineer/comments/16d7fh4/chains_and_agents/) , 2023-09-11-0910
```
I think there's a lot of confusion around AI agents today and it's mainly because of lack of definition and using the wr
ong terminology.

We've been talking to many companies who are claiming they're working on agents but when you look unde
r the hood, they are really just chains.

I just listened to the Latent Space pod with Harrison Chase (Founder of Langch
ain) and I really liked how he thinks about chains vs agents.

Chains: sequence of tasks in a more rigid order, where yo
u have more control, more predictability.  
Agents: handling the edge-cases, the long-tail of things that can happen.

A
nd the most important thing is that it's not an OR question but an AND one: you can use them in the same application by 
starting with chains -> figuring our the edge-cases -> using agents to deal with them.

&#x200B;

https://preview.redd.i
t/xbjmtlt4j0nb1.png?width=3127&format=png&auto=webp&s=8a787028bfb20d5fa6d25baab9ed98b88ff44b1f
```
---

     
 
all -  [ [D] Chains and Agents ](https://www.reddit.com/r/MachineLearning/comments/16d7ee6/d_chains_and_agents/) , 2023-09-11-0910
```
I think there's a lot of confusion around AI agents today and it's mainly because of lack of definition and using the wr
ong terminology.

We've been talking to many companies who are claiming they're working on agents but when you look unde
r the hood, they are really just chains.

I just listened to the Latent Space pod with Harrison Chase (Founder of Langch
ain) and I really liked how he thinks about chains vs agents.

Chains: sequence of tasks in a more rigid order, where yo
u have more control, more predictability.  
Agents: handling the edge-cases, the long-tail of things that can happen.

A
nd the most important thing is that it's not an OR question but an AND one: you can use them in the same application by 
starting with chains -> figuring our the edge-cases -> using agents to deal with them.

https://preview.redd.it/l59sc4sr
i0nb1.png?width=3127&format=png&auto=webp&s=1f3f8730c48687eaabf1f554deb181cf35b96036
```
---

     
 
all -  [ langchain text classification on large context ](https://www.reddit.com/r/LangChain/comments/16d5ztu/langchain_text_classification_on_large_context/) , 2023-09-11-0910
```
Hello, i'm  very new to langchain so i wonder if you can give me your opinion on a problem and hopefully suggest me a po
tential solution. 

I'm trying to mimic a common  chatgpt usage. I would like to provide the LLM with a list of words as
king the AI to classify them based on instructions contained in the prompt. The problem is that the list of words  can b
e extremely huge and go over the limit provided by the model (gpt-3.5-turbo-16k)

I initially created the list of word i
n a single document that i split in chunks using RecursiveCharacterTextSplitter.

&#x200B;

At the moment i adopted this
 workflow:

ChatOpenAI -> evaluate prompt with the first chunk of context -> provide partial result

ChatOpenAI -> evalu
ate prompt with the second chunk of context -> provide partial result

...

ChatOpenAI -> evaluate prompt with the last 
chunk of context -> provide partial result

When i get the last partial result i merge them together to get a single pan
das dataframe. 

I wonder if this could be the right approach or there are more streamlined approach that langchain alre
ady offers. What i put in place is prone to many problems (for example the length of prompt+context can still be too lon
g and provide an incomplete response)

Thanks
```
---

     
 
all -  [ Need advice on titles ](https://www.reddit.com/r/jobs/comments/16d5xn6/need_advice_on_titles/) , 2023-09-11-0910
```
I'm 2 years out of undergraduate study in Computer Science and during my  last semester I joined a proptech startup base
d out of US, Chicago - I live in Pakistan. I've been working here almost 2 years and I'm currently a tech lead and manag
ing 3 junior engineers.

Now I'm trying to find roles in the UAE but I feel like it might be getting me rejected, ignore
d because I only have two years of work experience yet I'm a 'tech lead'. What do you guys think?

Here's my resume. Wou
ld really appreciate some advice on this. Thanks!

https://preview.redd.it/dda28rg540nb1.png?width=1180&format=png&auto=
webp&s=ef5b4a449e326099498f7645f644cc796b858168

&#x200B;
```
---

     
 
all -  [ Current State of Chatting with PDFs ](https://www.reddit.com/r/OpenAI/comments/16d4ijr/current_state_of_chatting_with_pdfs/) , 2023-09-11-0910
```
I've now tried quite a few **chatgpt plugins** which are supposed to analyze pdfs, as well as writing my own custom **la
ngchain based bots** to query documents built from large unstructured pdfs. I am still very unhappy with both my custom 
as well as the 'professional' solutions. They all seem to be able to recall single or multiple details from texts quite 
easily, but totally **uncapable of dealing with more complex questions**. My understanding is, that this is because of t
wo reasons: 

1. **Complex layout of unstructured data:** Even a single pdf page can have many types of data, in the for
m of images, tables, flowcharts, text blocks with multilevel bullets etc. This often makes it much more easy for a human
 to understand, but using pdf loaders provided by langchain or even more sophisticated toolkits (layout-parser) results 
in lots of different document elements, which the llm does not seem to able to connect in a meanigful way
2. **No hierac
hical context of the document:** A human is able to immediately understand a lot of context just by having seen the cove
r page, toc and then looking at a page, like understanding what kind of document it is, which section the current page i
s a part of and so on. A human will intuitively understand if they have to read an entire section to answer a question o
r just find a specific page. A bot will not

Since I'm not an expert in the field I just wanted to check if my understan
ding of this problem is somewhat correct and if so, what state of the art solutions exist to deal with these kinds of is
sues?
```
---

     
 
all -  [ Hierarchical Semantic search over pdfs ](https://www.reddit.com/r/LangChain/comments/16d4bhd/hierarchical_semantic_search_over_pdfs/) , 2023-09-11-0910
```
 

**Hello,**

**I’d like to implement a semantic search for PDFs or various documents.**

**I’ve been across Faiss and 
I’ve got it to work after a few tries (using LangChain library). At first I had problems since many of the docs were in 
italian but I fixed by switching the sentence transformer from** all-MiniLM-L6-v2 **to** paraphrase-multilingual-MiniLM-
L12-v2.

The result is far away from perfection, it doesn’t always find what I’m looking for and I think the main concer
n is the conversion from PDFs to vectors.

Currently it’s not taking in count the hierarchy of the document (titles, sub
titles, paragraph), is there a way to do so? Also, is it possible to define a “word weight” to set the priority of some 
words instead of others?

Any best practice or guide is appreciated.

Also, I’m not sure FAISS can do all the work, mayb
e there are good alternatives such as ElasticSearch?

Thanks in advance
```
---

     
 
all -  [ Multi tool agents model ](https://www.reddit.com/r/LangChain/comments/16d3w3c/multi_tool_agents_model/) , 2023-09-11-0910
```
I found that davinci 003 is more predictable and works better with custom tools as well as agent chains than gpt3.5

Wha
t’s your experience?
```
---

     
 
all -  [ Easiest way of making a local app with local LLM (no fine tuning)? ](https://www.reddit.com/r/LocalLLaMA/comments/16cygw7/easiest_way_of_making_a_local_app_with_local_llm/) , 2023-09-11-0910
```
I would like to make scripts playing with local LLMs. I don't want to play with fine tuning or tweak the models (M2 prob
ably can't handle it, plus it is incompatible with half the Python AI ecosystem), I just want to type 'how do you feel a
bout this?' and get an answer. I don't even need streaming, all I want is to get the answer. I don't need tokens/second,
 anything, just the raw answer.

How would you do this in a Macbook (M2 Max - 32GB)?

I thought about

\- Invoking llama
.cpp process from terminal, programmatically (maybe too much work? This also wouldn't be versatile)

\- Grab something l
ike Dalai that makes a web server from llama.cpp, then I can switch between OpenAI and my local GPT which would call a l
ocal server?

\- Is there an even better way?

Probably NodeJS would be easier, but if there is a trick on Python, I'm o
pen too. All I could find was tutorials on how to fine tune, not exactly run the standard model via Python, which is wha
t I want (from a Macbook, so I can't compile the models in pytorch, I guess). Langchain is not my favorite piece of soft
ware, but if it can do this, I'm fine too.

Edit: what I'm looking into is basically OpenAI.chat.completion() but locall
y.
```
---

     
 
all -  [ Library or Langchain component for cleaning OpenAI response? ](https://www.reddit.com/r/LangChain/comments/16cnvuk/library_or_langchain_component_for_cleaning/) , 2023-09-11-0910
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

     
 
all -  [ Chainlit playground now supports all LangChain LLMs ](https://www.reddit.com/r/LangChain/comments/16cmjt9/chainlit_playground_now_supports_all_langchain/) , 2023-09-11-0910
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

     
 
all -  [ Rate my Pipe! Colab notebook incl. ](https://www.reddit.com/r/LangChain/comments/16cm7g1/rate_my_pipe_colab_notebook_incl/) , 2023-09-11-0910
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

     
 
all -  [ Help needed: making a tool required for agent? ](https://www.reddit.com/r/LangChain/comments/16clvhp/help_needed_making_a_tool_required_for_agent/) , 2023-09-11-0910
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

     
 
all -  [ The Point of LangChain — with Harrison Chase of LangChain ](https://www.latent.space/p/langchain#details) , 2023-09-11-0910
```

```
---

     
 
MachineLearning -  [ [P] FalkorDB - a fast Graph Database - Knowledge Graph as RAG ](https://www.reddit.com/r/MachineLearning/comments/16cg6k7/p_falkordb_a_fast_graph_database_knowledge_graph/) , 2023-09-11-0910
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

     
 
MachineLearning -  [ [D] Is there anything LangChain can do better than using LLMs directly (either through a website or  ](https://www.reddit.com/r/MachineLearning/comments/165airj/d_is_there_anything_langchain_can_do_better_than/) , 2023-09-11-0910
```
I haven't used ChatGPT a lot or any other LLMs, I've been reading about  Langchain and its use cases, and I'm having tro
uble wrapping my head  around exactly what it does. From what I understand, its an alternative  interface for LLMs, allo
wing for easy switching between them, and makes  some work for specific use cases easier. If I wanted to write an app or
  script to interact with LLMs and do other tasks, how would LangChain be  better than just making API call(s) to an LLM
, getting back the result  as a string, and doing whatever with it?
```
---

     
 
MachineLearning -  [ Apache Airflow vs. LangChain and LlamaHub for LLM data pipeline [D] ](https://www.reddit.com/r/MachineLearning/comments/160lexg/apache_airflow_vs_langchain_and_llamahub_for_llm/) , 2023-09-11-0910
```
I’m looking for recommendations, suggestions, and/or good documentation that outlines which data pipeline would be best 
to ingest my private data (which will then be split into chunks/nodes for vector embeddings and so forth). Thank you in 
advance!
```
---

     
 
MachineLearning -  [ [P] LLM Apps Are Mostly Data Pipelines ](https://www.reddit.com/r/MachineLearning/comments/15z0muk/p_llm_apps_are_mostly_data_pipelines/) , 2023-09-11-0910
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

     
 
MachineLearning -  [ [P] pgml-chat: A command-line tool for deploying low-latency knowledge-based chatbots ](https://www.reddit.com/r/MachineLearning/comments/15t5nzl/p_pgmlchat_a_commandline_tool_for_deploying/) , 2023-09-11-0910
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

     
 
MachineLearning -  [ [P] My apprehension about LangChain and why you don’t need LangChain for building a RAG bot. ](https://www.reddit.com/r/MachineLearning/comments/15ry3z4/p_my_apprehension_about_langchain_and_why_you/) , 2023-09-11-0910
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

     
 
MachineLearning -  [ [D] Approach to creating an 'AI tutor' chatbot for a fantasy language? ](https://www.reddit.com/r/MachineLearning/comments/15o4jy9/d_approach_to_creating_an_ai_tutor_chatbot_for_a/) , 2023-09-11-0910
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

     
 
deeplearning -  [ How to find 'custom' datasets for LLM ](https://www.reddit.com/r/deeplearning/comments/16bj3hg/how_to_find_custom_datasets_for_llm/) , 2023-09-11-0910
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

     
