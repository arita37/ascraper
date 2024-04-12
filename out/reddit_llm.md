 
all -  [ (MIT) Neuralink for your AI agents ](https://www.reddit.com/r/LocalLLaMA/comments/1c1ufln/mit_neuralink_for_your_ai_agents/) , 2024-04-12-0910
```
Tiger: Neuralink for AI Agents (MIT) (Python)

Hello, we are developing a superstructure that provides an AI-Computer in
terface for AI agents created through the frameworks like crewAI, LangChain and AutoGen, we have published it completely
 openly under the MIT license.

What it does: Just like human developers, it has some abilities such as running the code
s it writes, making mouse and keyboard movements, writing and running Python functions for functions it does not have. A
I literally thinks and the interface we provide transforms with real computer actions.

Those who want to contribute can
 provide support under the MIT license and code conduct. [https://github.com/Upsonic/Tiger](https://github.com/Upsonic/T
iger)

&#x200B;

https://preview.redd.it/lqcpx5w7uxtc1.png?width=2560&format=png&auto=webp&s=ffbd92a464743c56e8b717b65e1
aa83f5cf471f5
```
---

     
 
all -  [ MODERATION TOPIC / LLM OPENAI ](https://www.reddit.com/r/LangChain/comments/1c1p30i/moderation_topic_llm_openai/) , 2024-04-12-0910
```
How do you add moderation to your models; for example limit to my model to only answer question relationated with Life S
cience and Health.
```
---

     
 
all -  [ RAG Q/A | PDF Conversation | Langchain | OpenAI ](https://www.reddit.com/r/LangChain/comments/1c1o7nj/rag_qa_pdf_conversation_langchain_openai/) , 2024-04-12-0910
```
HELP: How can I make a rag Q/A app that allows the user to upload a pdf to the conversation and so that the model can un
derstand the context of the pdf; I tried to perform an ensemble retrievel but at some point the chunks lose the context 
of the entire pdf
```
---

     
 
all -  [ Advice on types of entry-level roles to seek + Resume help ](https://www.reddit.com/gallery/1c1m99s) , 2024-04-12-0910
```

```
---

     
 
all -  [ Chainlit Copilot mode: Embed your LangChain Agent as a copilot on a website or software ](https://www.reddit.com/r/LangChain/comments/1c1m2jb/chainlit_copilot_mode_embed_your_langchain_agent/) , 2024-04-12-0910
```
You can now build your AI agent in Python using LangChain and OpenAI and embed it - as a chatbot or copilot - in an exis
ting software 🔥

📞 Function Calling: your Copilot can even take actions on the website    
🌠 Widget UI & UX customisatio
n    
🔐 CORS & Authentication to manage who can access the copilot

Simply add event listeners to your code to have the 
agent interact with the software!

It unlocks many use cases:  Customer Support Chatbots, Lead Generation Chatbots or So
ftware Copilots & more

Docs: [https://docs.chainlit.io/deployment/copilot](https://docs.chainlit.io/deployment/copilot)
  
Example: [https://github.com/Chainlit/cookbook/tree/main/copilot](https://github.com/Chainlit/cookbook/tree/main/copi
lot)
```
---

     
 
all -  [ Improving the summarisation capability of LLM - will LangChain help? ](https://www.reddit.com/r/LangChain/comments/1c1ltfp/improving_the_summarisation_capability_of_llm/) , 2024-04-12-0910
```
I'm building a Summarizer, or you can say it's a kind of report generation for fraudulent transactions (fraud not confir
med, but just alerted) using LLM. I'm using OpenAI GPT-4 to perform the summarization task. I've tried my best to improv
e the prompt to generate the best summary/report with insights into the data. Some of these improvements include:

1. Pr
oviding metadata of the tables involved.
2. Assigning a role to the LLM.
3. Providing a few-shot examples on how to gene
rate the summary.

Currently, I'm not using LangChain for the summarization task. However, **are there any other techniq
ues that can generate the summary/report in a better way without losing the context? Will LangChain help me in improving
 the summary?** 

&#x200B;

PS: I'm a newbie to this field, please pardon me if there is any mistake in my explanation.
```
---

     
 
all -  [ Tables context length issue in RAG ](https://www.reddit.com/r/LangChain/comments/1c1lsk6/tables_context_length_issue_in_rag/) , 2024-04-12-0910
```
I am trying to create a PDF RAG chatbot for RFP. Extracted text using pypdf and extracted tables using tabula..now tryin
g to create a multimodal RAG using ChromaDB.  
tables im trying to summarise using Llama2 with prompt to preserve relati
onship between rows and columns   
text I split using recursive text splitter  
i add both to RAG   
but i feel the tabl
e insertion into RAG isnt correct for proper QA  
kindly guide me 
```
---

     
 
all -  [ Langchain + Pydanctic + OpenAI : pydantic.v1.error_wrappers.ValidationError: 1 validation error for  ](https://www.reddit.com/r/LangChain/comments/1c1l8zp/langchain_pydanctic_openai_pydanticv1error/) , 2024-04-12-0910
```
    from langchain_openai import ChatOpenAI
    from langchain_openai import OpenAIEmbeddings
    from langchain.chains 
import RetrievalQA
    from langchain_mongodb import MongoDBAtlasVectorSearch
    from langchain.output_parsers import P
ydanticOutputParser
    from langchain.prompts import PromptTemplate
    from src.models.steps import Steps
    
    
  
  def get_steps(query, mongo_uri, mongo_db_name):
        vector_store = MongoDBAtlasVectorSearch.from_connection_string
(
            mongo_uri,
            mongo_db_name + '.' + 'taskVectors',
            OpenAIEmbeddings(disallowed_specia
l=()),
            index_name='default',
        )
    
        llm = ChatOpenAI(model='gpt-3.5-turbo')
    
        par
ser = PydanticOutputParser(pydantic_object=Steps)
    
        prompt = PromptTemplate(
            template='Answer the
 query attached very precisely, give the output in the structure specified. '
                     'Just say no if you d
on't find the answer in current context. '
                     'You have to map every field in structure to the appropr
iate value. '
                     'For example to map elementId you should see from the output what is the value of key
 elementId from '
                     'the context. '
                     'You will find it like this ...\'elementId\'
: \'Go to Page 2\',.... '
                     'So you will map Go to Page 2 to elementId in the structure. '
          
           'If you find multiple actionElements return all of them in the particular structures, '
                     
'remember final output is gonna be multiple objects '
                     'Also for the scrollDetails field, populate a
n array, even if there is one or no object, it should '
                     'be an array of those objects, like this '

                     '...\'listView\': \'index\': 0, \'scrollOffsetX\': 0..... should be populated as '
                
     '[...\'viewId\': \'listView\', \'offsets\': \'x\': 0, \'y\': 405 ....]'
                     'This is very crucial,
 wrong answers can cause serious problems.'
                     + '\n{format_instructions}\n{query}\n',
            inp
ut_variables=['query'],
            partial_variables={'format_instructions': parser.get_format_instructions()},
       
 )
    
        chain = prompt | llm | parser
    
        retriever = vector_store.as_retriever(
            search_typ
e='similarity',
            search_kwargs={'k': 25},
        )
    
        qa = RetrievalQA.from_chain_type(llm=chain, 
chain_type='stuff', retriever=retriever, return_source_documents=True)
        retriever_output = qa.invoke(query)
     
   return retriever_output

  
I added pydantic output parser to this function to parse my output in a particular struct
ure, and I think everything almost works correctly, the output I get is:  
`{'text': Steps(root=[Action(elementId='Go to
 Page 2', position=Position(x=252, y=100, width=116, height=48), value='Go to Page 2', scrollDetails=[ScrollDetail(viewI
d='mainScrollLayout', offsets=Offsets(x=0, y=0))], viewName='MainActivity'), Action(elementId='showBottomSheetButton', p
osition=Position(x=20, y=630, width=352, height=48), value='Show Bottom Sheet', scrollDetails=[ScrollDetail(viewId='main
ScrollLayout', offsets=Offsets(x=0, y=0))], viewName='MainActivity'), Action(elementId='backButton', position=Position(x
=16, y=96, width=88, height=48), value='Back', scrollDetails=[ScrollDetail(viewId='listView', offsets=Offsets(x=0, y=405
))], viewName='PageActivity')])}`

`Steps` is a `RootModel`  that should have an array of `Actions`, which is correct, b
ut I am getting this unidentified model `Generation` on top of steps which has this field `text` as you see in the outpu
t which expects a string, and hence the validation fails with error:  


`pydantic.v1.error_wrappers.ValidationError: 1 
validation error for Generation`

`text`

  `str type expected (type=type_error.str)`

  
Not sure where this `Generatio
n` model is coming from, I tried making `Steps` a `BaseModel`, still the same issue.  


How do I get this Generation ou
t of the way? Or what can I do to fix this?  
I am fairly new to `Langchain` and `OutputParsers`
```
---

     
 
all -  [ Best library/framework for parsing PDF documents with table inside? ](https://www.reddit.com/r/LangChain/comments/1c1ksv6/best_libraryframework_for_parsing_pdf_documents/) , 2024-04-12-0910
```
Hello, me and my team were looking for integrate inside our RAG company model the most decent pdf parser, we need one th
at can also parse tables and schemes and keep the information intact (or at least not completely broken when it will be 
sent to the vector database). We already tried Pypdf, pdfPlumber, Unstructured and Nougat, but all of these libraries we
ren't good enough for our needs. Do you guys know any other alternative?
```
---

     
 
all -  [ Multivector RAG for drugs pdf, missing context, I need help ](https://www.reddit.com/r/ChatGPTCoding/comments/1c1klmk/multivector_rag_for_drugs_pdf_missing_context_i/) , 2024-04-12-0910
```
We are developing an RAG (Retrieval-Augmented Generation) system based on Elasticsearch and Langchain (Python users) for
 processing PDF files containing drug information. Our solution includes the following components:

* Layout-Based Parti
tioning: We utilize LLMSherpa for text partitioning and Textract for isolating tables.
* Chunk Summary Encoding: We empl
oy a history-aware multivector retrieval strategy based on semantic similarity exclusively.
* Response Generation: OpenA
I models.

We are encountering challenges in identifying relevant chunks for users' queries. Sometimes, the drug name is
 not explicitly mentioned in the chunk, making it too generic. This presents the following potential issues:

* The chun
k may always be retrieved, leading to constant answers even when the drug is changed.
* The chunk may never be retrieved
 due to its vagueness, making explicit drug-related chunks yield more coherent results even if they are not relevant.

A
re there any retrieval or partition strategies to address our problem?
```
---

     
 
all -  [ Building and Deploying a MinIO-Powered LangChain Agent API with LangServe ](https://www.reddit.com/r/minio/comments/1c1jopp/building_and_deploying_a_miniopowered_langchain/) , 2024-04-12-0910
```
Building on these insights, we now turn our focus to [LangServe](https://blog.langchain.dev/introducing-langserve/?ref=b
log.min.io), a pivotal tool in transitioning LangChain applications from development to deployment, simplifying the proc
ess of launching production-ready APIs.

[https://blog.min.io/minio-powered-langchain-agent-with-langserve/](https://blo
g.min.io/minio-powered-langchain-agent-with-langserve/)
```
---

     
 
all -  [ How do you discover tools/ideas that might help improve your LLM-based apps which are not RAG? ](https://www.reddit.com/r/LangChain/comments/1c1g07n/how_do_you_discover_toolsideas_that_might_help/) , 2024-04-12-0910
```
Hi!

I'm new to LLM-based applications and mainly just trying stuff for fun and learning to improve my skills and knowle
dge but I was wondering how do you discover ideas/tools that can help improve your way of interacting between data and L
LMs in applications which are not RAG, for which I find there are a lot of resources. I have done some simple use case t
hat works pretty well when everything is fine, but also breaks a lot, but overall it didn't require me some deep knowled
ge of the space and I'm feeling like I can improve a lot upon my initial code by solving these issues using what people 
in the space developed or thought of for that. I'm not talking about tools and ideas for RAG which are very abundant, bu
t for all the other applications that don't require the level of sophistication RAG applications do.

My use case is ext
racting structured data from documents. I have coded a small python program to which I give a document (.pdf or .txt) an
d I give it a query (a string, in natural language) that's intended to extract structured data from these documents and 
put it into a JSON. For example if my document talks about different startups, how much capital they've raised etc., I c
an ask 'extract the names of the startups the document is talking about and how much capital they've raised in their fir
st series' and get a JSON that contains that.

I consider this a simple use case, it's not a RAG use case, it's a simple
 use case of, at least how I think of it, 'chunking => LLM call => output cleaning' but I want to either go beyond that 
if it's possible or explore better ideas to do each of these small steps (like are there ways to do better chunking that
 the traditional ones of recursive text splitting etc.?). I feel like just trying to do this in any other way without us
ing LLMs can already be a great step for me but I don't know where to look at.
```
---

     
 
all -  [ Open Source Function-Hub for Agent Tools | crewAI - LangChain - Autogen ](https://www.reddit.com/r/LocalLLaMA/comments/1c1d8sd/open_source_functionhub_for_agent_tools_crewai/) , 2024-04-12-0910
```
Hi, i built an open source mit licensed project for storing function in a place with automatic documentation and CPU ram
 analye itself. Also its provide automaticaly dependency extraction and installation.

&#x200B;

You can create your own
 hubs with docker. [https://github.com/Upsonic/Tiger](https://github.com/Upsonic/Tiger)

&#x200B;

&#x200B;

https://pre
view.redd.it/90mueks2butc1.png?width=1847&format=png&auto=webp&s=da6289d97c2d423e6a7d9dd019af2b66dd6d0ca3
```
---

     
 
all -  [ We summarised Harrison Chase's talk on the evolution of AI agents and their applications ](https://www.reddit.com/r/LangChain/comments/1c1c0md/we_summarised_harrison_chases_talk_on_the/) , 2024-04-12-0910
```
Hey! We summarised Harrison Chase's talk on the evolution of AI agents and their applications during AI Ascent. Maybe it
 will be useful for you as well:

He identified 3 critical areas of development:

* Planning
* UX
* Memory

1. Planning:


Chase highlighted the need for AI agents to plan strategically beyond basic action and feedback loops, which current l
anguage models struggle with for complex tasks.

He discussed the ongoing research and development efforts to enhance pl
anning capabilities, like external prompting strategies and cognitive architectures. Are these just short-term fixes or 
essential long-term requirements for AI agent development?

2. User Experience (UX):

Chase is particularly enthusiastic
 about the user experience (UX) of interacting with AI agents. He emphasizes that achieving a balance between human invo
lvement and agent autonomy is essential for effective application.

He discussed innovative UX features such as the abil
ity to rewind and edit agent actions, which enhance reliability and control over the agent's decisions. These developmen
ts aim to make agents more user-friendly and adaptable to specific user needs and corrections.

3.  Memory:

Memory is a
 key area for advancement in AI agents. Two essential types are procedural memory (task performance) and personalized me
mory (user preferences or facts).

He provided examples of how agents could use memory to enhance their interactions, su
ch as adapting communication styles based on previous interactions or recalling personal details to personalize conversa
tions.

What's next for AI agents?

Full talk: https://www.youtube.com/watch?v=pBBe1pk8hf4&list=PLOhHNjZItNnOoPxOF3dmq30
UxYqFuxXKn&index=7
```
---

     
 
all -  [ Having issues with Manual install after installing the requirements ](https://www.reddit.com/r/ankibrain/comments/1c17wba/having_issues_with_manual_install_after/) , 2024-04-12-0910
```
ive managed to enter the virtual environment but after installing everything via pip and reopening Anki the AnkiBrain wi
ndow does not appear. Any idea where would the logs be to debug this?

&#x200B;

&#x200B;

https://preview.redd.it/yrp0q
joykstc1.png?width=1881&format=png&auto=webp&s=3d7efb4bba2afa672b00721da05b304b2c788fc9
```
---

     
 
all -  [ What resources should I use to become an expert in LLM based applications/chatbots?  ](https://www.reddit.com/r/LangChain/comments/1c17gld/what_resources_should_i_use_to_become_an_expert/) , 2024-04-12-0910
```
I am beginning to LLM World. i am playing with Langchain, ollama for few problems. What is the best way to learn these? 

How do I approach for the same. I tried few YouTube videos but they just tell how to use this function, that function n
o one goes deep or explain why this is needed. 
What is the best way to learn llm? 

For reference, I am trying to creat
e a chatbot, which classifies intent of a sentence then based on intent it will call the api for operation or call the l
lm for answer. 
For intent classification I am using llama2 model, and trying to get intent in json format. But it somet
imes give intent in nin json format. How to make sure llama2 gives answer in json format only. 
```
---

     
 
all -  [ Can Langchain JS handle everything Python version can? ](https://www.reddit.com/r/LangChain/comments/1c127nu/can_langchain_js_handle_everything_python_version/) , 2024-04-12-0910
```
I am currently deciding on a backend technology to use for my AI backend app. I will be looking into implementing/utiliz
ing RAG, Background jobs for data loading, OAuth etc.

NestJS is a pretty good backend choice these days for the same bu
t I am just worried if Langchain JS is as good as Python Langchain as the documentation of Python version is awesome com
pared to JS.   


So first question, can Langchain JS handle everything Python version can and only the documentation is
 lacking?  


I love FastAPI's developer experience and how lightweight it is and I would like to stick with it if in Py
thon ecosystem due to Langchain but I am worried I will have to do too much work from scratch that Django already handle
s. (Note I will be using AWS wherever I can so does it really matter?)  


So yeah, second question, if using Langchain 
JS, which is more recommended, Django or FastAPI for an AI heavy app? I hate Django's learning curve but is it worth it 
compared to FastAPI?

&#x200B;
```
---

     
 
all -  [ NestJS vs Django vs FastAPI for backend development with AI ](https://www.reddit.com/r/webdev/comments/1c121ra/nestjs_vs_django_vs_fastapi_for_backend/) , 2024-04-12-0910
```
I am planning on a tech stack for an app which will be heavy on the AI side and here are the things I can think of imple
menting/utilizing: Langchain, RAG, Async jobs, OAuth.   


Just FYI, I plan on relying on cloud providers for the most p
arts other than the backend service as I would like to handle customizations.   


Which backend technology is the best 
in this scenario? NestJS is really good and kind of checks all boxes for me (scalability, TS support, etc) but I am a bi
t sus about langhcain.js as it's documentation is lacking compared to the Python version.  


Django is technically pyth
on equivalent of Nest but one, I am not a big fan of Django due to the high learning curve. But the ORM, admin console a
re some cool things out of the box. Plus Python langchain!

FastAPI is just awesome for fast development but I am worrie
d I will be looking at implementing too many things from scratch just because other than async jobs/auto-swagger documen
tation.   


Here's the stack I plan to use (if this helps):  
**Backend**: Nest.js (leaning most towards this but let's
 see based on opinions), langchain  
**DB**: GraphQL, Apollo, Prisma, AWS  
**Hosting:** Vercel/AWS  
**Frontend:** Flut
ter/Dart mobile app, Next or React + Vite web app + Jotai/Zustand for state management.
```
---

     
 
all -  [ Display charts and images generated from a python agent ](https://www.reddit.com/r/LangChain/comments/1c10vvb/display_charts_and_images_generated_from_a_python/) , 2024-04-12-0910
```
Hello everyone,  
I'm working on a chatbot app (frontend React +backend Python with fastAPI), and I'm using a python age
nt to generate some graphs and charts for the users. However, the frontend and the backend are hosted in different conta
iners for security purposes, so I can't use the native save image on python and return the location of the image (as it'
s gonna be on the backend container that is isolated from the frontend one so I won't be able to access it).   
How can 
I solve this problem?   
Thanks in advance
```
---

     
 
all -  [ Langchain Cache - Any way to define a custom cache key? ](https://www.reddit.com/r/LangChain/comments/1c0y53d/langchain_cache_any_way_to_define_a_custom_cache/) , 2024-04-12-0910
```
e.g. like this:  
[https://docs.litellm.ai/docs/caching/redis\_cache#custom-cache-keys](https://docs.litellm.ai/docs/cac
hing/redis_cache#custom-cache-keys)  


would be nice to have non-hash keys e.g, for searching in Redis GUI
```
---

     
 
all -  [ Advice needed on orchestrating a multi-agent conversational AI with chat history retention ](https://www.reddit.com/r/LangChain/comments/1c0xi7a/advice_needed_on_orchestrating_a_multiagent/) , 2024-04-12-0910
```
I'm looking for guidance on creating a multi-agent conversational AI that can dynamically switch between specialized age
nts based on the user's needs, while retaining the full conversation history to provide a personalized experience.

The 
high-level idea is:

* When the user asks a question or makes a request, the conversational AI analyzes the input to det
ermine which specialized agent is best suited to assist (e.g. a math agent for solving math problems, a history agent fo
r discussing historical topics, etc.)
* The relevant specialized agent then engages with the user to address their speci
fic query
* Throughout the conversation, even as different specialized agents kick in, the full chat history is retained
 and passed along, so each agent has the full context of the conversation
* This allows the conversational AI to provide
 a seamless experience that is personalized to the user's ongoing needs

I'm fairly new to working with tools like Langc
hain and could use any advice or best practices for architecting and orchestrating something like this. Some specific qu
estions:

* What's the best way to structure the specialized agents? Should they be separate fine-tuned models, separate
 knowledge bases that plug into foundational models (GPT-4), or something else?
* How can I efficiently store and pass a
long the full conversation history to each agent, without hitting token limits of the underlying models?
* Are there any
 existing open-source projects or frameworks that could serve as a good starting point or reference for orchestrating a 
conversational AI like this?

Any guidance or resources are much appreciated! I'm excited to dive into this but could us
e a push in the right direction. Let me know if any additional details would be helpful.
```
---

     
 
all -  [ Used Claude's 200K context length to write a 30K word novel which heavily grounds in details unlike  ](https://www.reddit.com/r/LangChain/comments/1c0w79c/used_claudes_200k_context_length_to_write_a_30k/) , 2024-04-12-0910
```
As the title describes, I've used Claude 3 Sonnet to create a 30K word story which heavily grounds in details. Here is t
he [story link](https://github.com/desik1998/NovelWithLLMs/blob/main/Novel.md)  (For now put this on Github itself). The
 story is about American founding fathers returning back to 21st Century. Currently it consists of 3 chapters and there 
are 4 more chapters to write. I've already reviewed it with few of my friends who're avid novel readers and most of them
  have responded with 'it doesn't feel AI written', it's interesting  (subjective but most have said this), grounds heav
ily on details. Requesting to read the novel and provide the feedback   

Github Link: [https://github.com/desik1998/Nov
elWithLLMs/tree/main](https://github.com/desik1998/NovelWithLLMs/tree/main) 

# Approach to create long story:

LLMs suc
h as Claude 3 / Gpt 4 currently allows input context length  of 150K words and can output 3K words at once. A typical no
vel in  general has a total of 60K-100K words. Considering the 3K output limit,  it isn't possible to generate a novel i
n one single take. So the  intuition here is that let the LLM **generate 1 event at a time and once the event is generat
ed, add it to the existing story and continously repeat this process**.  Although theoretically this approach might seem
 to work, just doing  this leads to LLM moving quickly from one event to another, not being  very grounded in details, l
lm not generating event which is a  continuation of the current story, LLM generating mistakes based on the  current sto
ry etc.   

To address this, the following steps are taken:   

# 1. Initially fix on the high level story:

Ask LLM to 
generate high level plot of the story like at a 30K  depth. Generate multiple plots as such. In our case, the high level
 line  in mind was **Founding Fathers returning back**. Using  this line, LLM was asked to generated many plots enhancin
g this line. It  suggested many plots such as Founding fathers called back for being  judged based on their actions, fou
nding fathers called back to solve AI  crisis, founding fathers come back for fighting against China, Come back  and fig
ht 2nd revolutionary war etc. Out of all these, the 2nd  revolutionary war seemed the best. Post the plot, LLM was promp
ted to  generate many stories from this plot. Out of these, multiple ideas in  the stories were combined (manually) to g
et to fix on high level story.  Once this is done, get the chapters for the high level story (again  generated multiple 
outputs instead of 1). And generating chapters should  be easy if the high level story is already present   

# 2. Do th
e event based generation for events in chapter:

Once chapters are fixed, now start with the generation of events in a c
hapter but **1 event at a time like described above**.  To make sure that the event is grounded in details, a little pro
mpting  is reqd telling the LLM to avoid moving too fast into the event and  ground to details, avoid generating same ev
ents as past etc. [Prompt used till now](https://github.com/desik1998/NovelWithLLMs/blob/main/PROMPT.md)  (There are som
e repetitions in the prompt but this works well). Even  after this, the output generated by LLM might not be very compel
ling so  to get a good output, generate the output multiple times. And in general  generating **5-10 outputs**, results 
in a good possible  result. And it's better to do this by varying temperatures. In case of  current story, the temperatu
re b/w 0.4-0.8 worked well. Additionally,  the rationale behind generating multiple outputs is, given LLMs generate  dif
ferent output everytime, the chances of getting good output when  prompted multiple times increases. Even after generati
ng multiple  outputs with different temperatures, if it doesn't yield good results,  understand what it's doing wrong fo
r example like avoid repeating events  and tell it to avoid doing that. For example in the 3rd chapter when  the LLM was
 asked to explain the founders about the history since their  time, it was rushing off, so [an instruction to explain th
e historic events year-by-year](https://github.com/desik1998/NovelWithLLMs/blob/main/HistoryChapterPrompt.md)  was added
 in the prompt. Sometimes the LLM also generates part of the  event which is too good but the overall event is not good,
 in this  scenario adding the part of the event to the story and continuing to  generate the story worked well.   

**Ov
erall Gist:** Generate the event multiple times  with different temperatures and take the best amongst them. If it still
  doesn't work, prompt it to avoid doing the wrong things it's doing   

Overall Event Generation: Instead of generating
 the next event in a chat conversation mode,  giving the whole story till now as a combination of events in a single  pr
ompt and asking it to generate next event worked better.   

**Conversation Type 1:** 

    human: generate 1st event 
 
   Claude: Event1 
    human: generate next,  
    Claude: Event2, 
    human: generate next ...

**Conversation Type 2:
** (Better)   

    Human:   
    Story till now: 
    Event1 + Event2 + ... + EventN. 
    Generate next event   
    

    Claude: 
    Event(N+1)

Also as the events are generated, one keeps getting new ideas to  proceed on the story chap
ters. And if any event generated is so good,  but aligns little different from current story, one can also change the  f
uture story/chapters.   

**The current approach, doesn't require any code** and long stories can be generated directly 
using the **Claude Playground or Amazon Bedrock Playground**  (Claude is hosted). Claude Playground has the best Claude 
Model Opus  which Bedrock currently lacks but given this Model is 10X costly,  avoided it and went with the 2nd Best Son
net Model. As per my  experience, the results on Bedrock are better than the ones in Claude  Playground   

# Questions:


1. Why wasn't Gpt4 used to create this story?     
 

* When asked Gpt4 to generate the next event in the story, there
 was  no coherence in the next event generated with the existing story. Maybe  with more prompt engineering, this might 
be solved but Claude 3 was  giving better output without much effort so went with it. Infact, Claude  3 Sonnet (the 2nd 
best model from Claude) is doing much better when  compared to Gpt4.     
 

2. How much cost did it take to do this?   
  
 

* **$50-100**   
 

# Further Improvements:

1. Explore ways to avoid long input contexts. This can further reduce
  the cost considering most of the cost is going into this step. Possible  Solutions:   

* Give gists of the events hap
pened in the story till now instead of whole story as an input to the LLM. References: [1](https://deepmind.google/resea
rch/publications/74917/), [2](https://arxiv.org/html/2310.00785v3)   


2. Avoid the human loop as part of the choosing 
the best event  generated. Currently it takes a lot of human time when choosing the best  event generated. Due to this, 
the time to generate a story can take  from few weeks to few months (1-1.5 months). If this step is automated  atleast t
o some degree, the time to write the long story will further  decrease. Possible Solutions:     


* Use an LLM to deter
mine what are the best events or top 2-3 events  generated. This can be done based on multiple factors such as whether  
the event is a continuation, the event is not repeating itself. And  based on these factors, LLM can rate the top respon
ses. References: [Last page in this paper](https://huggingface.co/papers/2308.06259) 
* Train a reward model (With or wi
thout LLM) for determining which generated event is better. [LLM as Reward model](https://arxiv.org/html/2401.10020v1)  
 
 

3. The current approach generates only 1 story. Instead generate a Tree  of possible stories for a given plot. For 
example, multiple generations  for an event can be good, in this case, select all of them and create  different stories.
     


4. Use the same approach for other things such as movie story generation, Text Books, Product document generatio
n etc     


5. Benchmark LLMs Long Context not only on RAG but also on Generation     
 
```
---

     
 
all -  [ Putting your Function-call tools to an Online Hub and Use in CrewAI, LangChain and AutoGen with Auto ](https://www.reddit.com/r/LocalLLaMA/comments/1c0uyjj/putting_your_functioncall_tools_to_an_online_hub/) , 2024-04-12-0910
```
Hi, i am working on a open source MIT licenced function hub for LLM agents function-call ability. In this point i just w
ant to create multiple integrations with various agent frameworks like **crewAI**, **AutoGen** and **LangChain**. My mot
ivation is increasing the usage of tool amount for each framework and there is no utility and a **toolhub** project.




So i just make a platform for storing functions with **automaticaly dependency installation**, running the function **in
 local for security** and **creating documents and readmes for each function automaticaly with llm**. Also i just create
 a module infrastructure for each functions, its like categories.

**'Tiger: Neuralink for your AI agents'**



I say th
is because the tiger is providing an think and made interface for AI agents just like the original [neuralink](https://n
euralink.com/) and humans. I just put some images and GitHub link:

[https://github.com/Upsonic/Tiger](https://github.co
m/Upsonic/Tiger)

https://preview.redd.it/2zasl9n0kptc1.png?width=1867&format=png&auto=webp&s=84a17941b221cbbb18636d9557
10e4d0df7c8b55

  

```
---

     
 
all -  [ GitHub - Upsonic/Tiger: Neuralink for your AI Agents ](https://www.reddit.com/r/crewai/comments/1c0tsu6/github_upsonictiger_neuralink_for_your_ai_agents/) , 2024-04-12-0910
```
Tiger: Neuralink for AI Agents (MIT) (Python)

Hello, we are developing a superstructure that provides an AI-Computer in
terface for AI agents created through the frameworks like crewAI, LangChain and AutoGen, we have published it completely
 openly under the MIT license.

What it does: Just like human developers, it has some abilities such as running the code
s it writes, making mouse and keyboard movements, writing and running Python functions for functions it does not have. A
I literally thinks and the interface we provide transforms with real computer actions.

Those who want to contribute can
 provide support under the MIT license and code conduct. [https://github.com/Upsonic/Tiger](https://github.com/Upsonic/T
iger)
```
---

     
 
all -  [ Allow Chatbot to Correct Itself to User Feedback ](https://www.reddit.com/r/LangChain/comments/1c0t2tt/allow_chatbot_to_correct_itself_to_user_feedback/) , 2024-04-12-0910
```
Hi,

So, I noticed on ChatGPT and also on my own chatbot (for a brief period of time), the chatbot would apologize and c
orrect itself when provided feedback by the user. For example:

Q: What is 2+2?  
A: 5

Q: No, it is 4.

Expected A: Sor
ry, you're right. It is 4.

Actual A: 5.

&#x200B;

My chatbot now is just sticking strongly to its answer instead of re
medying itself. What is the best way to acknowledge the corrected answer?
```
---

     
 
all -  [ Learning to fine tune models to write content in my voice ](https://www.reddit.com/r/OpenAI/comments/1c0szuw/learning_to_fine_tune_models_to_write_content_in/) , 2024-04-12-0910
```
Whats a good resource to start on this?

Broadly speaking I already understand how to use OpenAI's API to send simple me
ssages back and forth. But I'm not familiar with fine tuning or anything more complex.

I'd really like how to do this i
n a way that's LLM-agnostic, I've dabbled in LangChain a little which I assume is key to this, but in absence of that wi
ll gladly start with OpenAI specific learnings.
```
---

     
 
all -  [ Best Method to Quickly and Easily Deploy? ](https://www.reddit.com/r/LangChain/comments/1c0rvek/best_method_to_quickly_and_easily_deploy/) , 2024-04-12-0910
```
I used Gradio to deploy, which is quick and easy. What’s the easiest way to add stripe payment collection for subscripti
on?
```
---

     
 
all -  [ Prompt templates in LangChain ](https://www.reddit.com/r/LangChain/comments/1c0qjq2/prompt_templates_in_langchain/) , 2024-04-12-0910
```
I wrote a piece on [prompt templates in LangChain](https://www.mirascope.io/post/langchain-prompt-template), how they wo
rk and the different approach [Mirascope](https://github.com/Mirascope/mirascope) takes with colocation. I hope you find
 it useful.
```
---

     
 
all -  [ Beginner to LangChain. Need help! - [Stock Annual Report PDF Chatbot using RAG]. ](https://www.reddit.com/r/LangChain/comments/1c0q8qm/beginner_to_langchain_need_help_stock_annual/) , 2024-04-12-0910
```
Hello! I'm a LangChain beginner and I need some help.

I'm working a PDF Chatbot that takes in a stock annual report as 
a PDF and does technical question answering on it \[Mathematical\] - Please help me! How do I approach this problem and 
where do I begin? I'll take any help I can.

I've been trying to do this with RAG. Any Suggestions? Thank you.

&#x200B;

```
---

     
 
all -  [ Learning to fine tune models to write content in my voice ](https://www.reddit.com/r/ChatGPT/comments/1c0q4p8/learning_to_fine_tune_models_to_write_content_in/) , 2024-04-12-0910
```
Whats a good resource to start on this?

Broadly speaking I already understand how to use OpenAI's API to send simple me
ssages back and forth. But I'm not familiar with fine tuning or anything more complex.

I'd really like how to do this i
n a way that's LLM-agnostic, I've dabbled in LangChain a little which I assume is key tot this,  but in absence of that 
will gladly start with OpenAI specific learnings. 
```
---

     
 
all -  [ I am coming back to LangChain! ](https://www.reddit.com/r/LangChain/comments/1c0oucr/i_am_coming_back_to_langchain/) , 2024-04-12-0910
```
I started building internal LLM tools for my company and originally thought LangChain would be a good tool. At the time 
I was wrong, there were many issues with the project and I found out I was better off removing and replacing LangChain w
ith my own implementations. 

I'm glad to say I've started to bring LangChain back into my projects. I have to commend t
he LangChain team for all their work to improve the project. The project still has its issues (mainly documentation and 
over-abstraction) but overall much better. The community tools provide the best suite of integrations of any LLM package
.

The thing that impresses me the most is LangSmith. It gives you unparalleled visibility into what your app is doing a
nd provides tools that supercharge the development process. Fantastic product!

TLDR: its better now
```
---

     
 
all -  [ Adding tools to ConversationalRetrievalChain.from_llm causes Pydantic error ](https://www.reddit.com/r/LangChain/comments/1c0mkl4/adding_tools_to_conversationalretrievalchainfrom/) , 2024-04-12-0910
```
**The following code:**

tools = load\_tools(\['llm-math'\],llm=llm)  
chain = ConversationalRetrievalChain.from\_llm(  

llm=llm,  
tools=tools,

**Causes the following error message:**

\\venv\\lib\\site-packages\\langchain\_core\\load\\se
rializable.py', line 120, in **init**  
super().**init**(\*\*kwargs)  
File 'pydantic\\main.py', line 341, in pydantic.m
ain.BaseModel.**init**  
pydantic.error\_wrappers.ValidationError: 1 validation error for ConversationalRetrievalChain  

tools  
extra fields not permitted (type=value\_error.extra)

**I want a way to call math tool because my chain fails t
o calculate summations for example like this:**

**29577.30 + 24683.36 + 23262.12 + 26421.73 + 52409.77 + 25314.39 = 137
,605.52, which is wrong and most likely it gets a new answer each time.**
```
---

     
 
all -  [ How to make use of Complete GPU memory? ](https://www.reddit.com/r/LangChain/comments/1c0k4oh/how_to_make_use_of_complete_gpu_memory/) , 2024-04-12-0910
```
I am using a Mistral model 4b and huggingface

    pipeline text_generation_pipeline = pipeline(     
            model=
model,     
            tokenizer=tokenizer,     
            task='text-generation',        
            batch_size=2 

    ) 
    llm = HuggingFacePipeline(pipeline=text_generation_pipeline,batch_size=2)

and then using RAG through langcha
in

    rag_chain_from_docs = ( 
    RunnablePassthrough.assign(context=(lambda x: format_docs(x['context']))) | prompt 
| llm | StrOutputParser() )
    
    rag_chain_with_source = RunnableParallel(
    {'context': retriever, 'question': Ru
nnablePassthrough()} ).assign(answer=rag_chain_from_docs)

My GPU (T4) is underutilized, its only 8GB/16GB. so I want to
 use all of My GPU, Is there any way to do this, I tried chain.batch() but it did not work(It still ran sequentially). A
ny suggestions would be helpful to run the chain concurrently.
```
---

     
 
all -  [ LangChain E-Mails with LLM ](https://www.reddit.com/r/LangChain/comments/1c0k2qo/langchain_emails_with_llm/) , 2024-04-12-0910
```
I am quite new to LangChain and Python as im mainly doing C# but i am interested in using AI on my own data.  
So i wrot
e some python code using langchain that:

1. Gets my Emails via IMAP
2. Creates JSON from my E-Mails (JSONLoader)
3. Cre
ates a Vectordatabase where each mail is a vector (FAISS,  OpenAIEmbeddings)
4. Does a similarity search according to th
e query returning the 3 mails that match the query the most
5. feeds the result of the similarity search to the LLM (GPT
 3.5 Turbo) using the query AGAIN

The LLM Prompt then looks something like:

    The question is
{query}

    Here are 
some information that can help you to answer the question:
{similarity_search_result}

Ok so far so good... when my ques
tion is:

    When was my last mail sent to xyz@gmail.com?

i get a correct answer... -> e.g last mail received 10.04.20
24 14:11  


But what if i want to have an answer to the following question

    How many mails have been sent by xyz@gm
ail.com?

Because the similarity search only gets the vectors that are most similar, how can i just get an answer about 
the amount?   
Even if the similarity search would deliver 150 mails instead of 3 sent by [xyz@gmail.com](mailto:xyz@gma
il.com) i cant just feed them all into the LLM prompt right?  


So what is my mistake here?
```
---

     
 
all -  [ How to make use of Complete GPU memory? ](https://www.reddit.com/r/u_Dear_Insect_5295/comments/1c0jwxy/how_to_make_use_of_complete_gpu_memory/) , 2024-04-12-0910
```
I am using a Mistral model 4b and huggingface

    pipeline text_generation_pipeline = pipeline(
        model=model,
  
      tokenizer=tokenizer,
        task='text-generation',   
        batch_size=2
    )
    llm = HuggingFacePipeline(p
ipeline=text_generation_pipeline,batch_size=2)

and then using RAG through langchain

rag\_chain\_from\_docs = ( Runnabl
ePassthrough.assign(context=(lambda x: format\_docs(x\['context'\]))) | prompt | llm | StrOutputParser() )

    rag_chai
n_with_source = RunnableParallel(
        {'context': retriever, 'question': RunnablePassthrough()}
    ).assign(answer=
rag_chain_from_docs)

My GPU (T4) is underutilized, its only 8GB/16GB. so I want to use all of My GPU, Is there any way 
to do this, I tried chain.batch but it did not work. Any suggestions would be helpful
```
---

     
 
all -  [ Seeking Guidance: Running Mixtral 8x7B on AWS ](https://www.reddit.com/r/MistralAI/comments/1c0grhr/seeking_guidance_running_mixtral_8x7b_on_aws/) , 2024-04-12-0910
```
Hey everyone,

&#x200B;

I'm seeking guidance on running Mixtral 8x7B on AWS for a project I'm working on. Previously, I
've primarily worked with LLMs using OpenAI and LangChain. Utilizing LangChain's toolkits and agents made it straightfor
ward to leverage models like GPT-3 and GPT-4 with an OpenAI API Key.

&#x200B;

However, my current project at work has 
shifted towards using Open Source LLMs, specifically Mixtral 8x7B on AWS. I've been tasked with deploying and running Mi
xtral, but I'm struggling to find clear tutorials online. While I've found a few resources, they're quite confusing.

&#
x200B;

Could anyone here point me towards a reliable tutorial or provide guidance on deploying and running Mixtral on A
WS? Any help would be greatly appreciated. Thanks in advance!
```
---

     
 
all -  [ What tools are you using for developing AI apps? ](https://www.reddit.com/r/LocalLLaMA/comments/1c0f6eu/what_tools_are_you_using_for_developing_ai_apps/) , 2024-04-12-0910
```
We obviously know about the LangChains and LlamaIndex. What are some promising AI frameworks/libraries/repos that are be
coming essential for building AI apps?
```
---

     
 
all -  [ Results of evaluating the AI Oracle approach - a novel way to improve your LLM application's accurac ](https://www.reddit.com/r/LangChain/comments/1c0do04/results_of_evaluating_the_ai_oracle_approach_a/) , 2024-04-12-0910
```
Recently, I saw this tweet about the AI Oracle approach for improving the accuracy and quality of responses for your LLM
 application. The technique is super simple:

[https://twitter.com/mattshumer\_/status/1777382373283299365](https://twit
ter.com/mattshumer_/status/1777382373283299365)

1. Send the request to 3 LLMs - Claude, GPT4, and Perplexity.
2. Give t
he responses to Claude again and prompt engineer to pick the best and accurate response.  

I got curious about this and
 decided to do some evaluations on this approach. Sharing some metrics/measurements in this post.

This one is pretty ob
vious, the latency on having all 3 LLMs generate a response and picking the best out of the 3 is high. But, I do recogni
ze that this can be improved by parallelizing the operations. 

https://preview.redd.it/lndc3gwp3ltc1.png?width=1200&for
mat=png&auto=webp&s=02ec4109e9a3211724686a40ecbb9110dc70033c

Ran the following tests for both the combined AI Oracle ap
proach and using a single LLM:

1. **Factual Accuracy** \- Evaluated for correctness of responses.

2. **Realtime data**
 \- Evaluated based on asking information related to realtime data.

3. **Adversarial Testing** \- Evaluated on whether 
the LLM is able to pickup the signal correctly by placing the question in between a bunch of garbage data. The LLM was g
iven a positive score if it correctly responded to the question without mentioning the garbage data. 

4. **Consistency 
checks** \- Evaluated on whether the LLM gave a response consistently when the same question was asking many times. Main
ly looked for structural consistency of the response.

5. **Quality** \- Evaluated on the quality - sentence structure, 
adherence to the prompt etc. 

**AI Oracle Approach**

Results for the AI Oracle approach: For some reason, it could not
 pick up the realtime information even once. I am sure with some prompt engineering, this metric can be improved. It did
 poorly on Adversarial testing - mostly because Claude and Pplx's responses. 

&#x200B;

https://preview.redd.it/9ggjkth
z3ltc1.png?width=1200&format=png&auto=webp&s=033d105e3793e68fb5b2bd9a134cbbefec423cc7

**Claude (claude-3-opus-20240229)
**

As expected, Claude did not do well on Realtime testing. But, interestingly, it did not do great with adversarial an
d consistency tests either.

&#x200B;

https://preview.redd.it/b33q8qz24ltc1.png?width=1200&format=png&auto=webp&s=ef154
b780655bb520c406d1aa53c8b91fc2c8038

**GPT4**

Again, GPT4 does not have realtime capabilities. But it did extremely wel
l on everything else except consistency checks where the responses were structured quite differently each time.

&#x200B
;

https://preview.redd.it/2jz4y6864ltc1.png?width=1200&format=png&auto=webp&s=a35bfe557f4164251c4900d4e2c62cf8a5c7b04d


**Perplexity (pplx-70b-online)**

As expected Perplexity's realtime capabilities are unmatched. But, it did not do that
 well with adversarial and consistency tests which in turn skewed the metrics for AI Oracle approach as well.Notably, th
e quality of responses from Perplexity were far better than the rest.

&#x200B;

https://preview.redd.it/y0mqsr4b4ltc1.p
ng?width=1200&format=png&auto=webp&s=3ba1acfd7159b8f0bd5164a0e99af7f8ab4f5071

In conclusion, you can get a near perfect
 score for the AI Oracle approach with a bit of prompt engineering. But you definitely lose performance in the process. 
Even when parallelized, it is only as slow as the slowest LLM. Token usage/cost is also going to be higher.

Finally, if
 you are curious, all these evaluations were done using Langtrace - an open source LLM monitoring and evaluations tool t
hat I am currently developing.

Github: https://github.com/Scale3-Labs/langtrace
```
---

     
 
all -  [ Is there a tool/platform to put an LLM to a large data set of PDF files (like 50GB) ](https://www.reddit.com/r/LangChain/comments/1c0czng/is_there_a_toolplatform_to_put_an_llm_to_a_large/) , 2024-04-12-0910
```
I am a non-tech person looking for a tool to ask questions to my 50GB worth of PDF files. Is there a tool which can help
 me build this project or something which is already there which can help?   


Please share relevant blogs or approache
s to follow. 
```
---

     
 
MachineLearning -  [ [D] How to get the source documents from the retrieved context for RAG?  ](https://www.reddit.com/r/MachineLearning/comments/1bvoc1t/d_how_to_get_the_source_documents_from_the/) , 2024-04-12-0910
```
I'm not using Lanchain but only making API calls to an LLM service provider. The retriever is connected to a vector DB, 
and I would like to know what the LLM refers to WITHIN that retrieved context whenever it provides an answer, similar to
 how return_source_documents works in Langchain.

I'm using AzureOpenAI. I couldn't find much in their docs that related
 to returning the source documents. Any help will be greatly appreciated!

```
---

     
 
MachineLearning -  [ [P] RAG pipeline to query the ML Engineering Open Book ](https://www.reddit.com/r/MachineLearning/comments/1bu4wyx/p_rag_pipeline_to_query_the_ml_engineering_open/) , 2024-04-12-0910
```
I built a quick RAG implementation using Langchain to make it easy to query the [ML Engineering Open Book](https://githu
b.com/stas00/ml-engineering) by [Stas Bekman](https://twitter.com/StasBekman). The Multi-Vector retriever gave pretty go
od results and was quite easy to set up too. 

Github link - [https://github.com/shreyansh26/RAG-ML-Engg-Open-Book](http
s://github.com/shreyansh26/RAG-ML-Engg-Open-Book)

Hope this is useful for folks!
```
---

     
 
MachineLearning -  [ [Project] FinancialAdvisorGPT : LLM+RAG Boilerplate Project ](https://www.reddit.com/r/MachineLearning/comments/1btlpgd/project_financialadvisorgpt_llmrag_boilerplate/) , 2024-04-12-0910
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

     
 
MachineLearning -  [ [Project] Picachain, image search made simple. ](https://www.reddit.com/r/MachineLearning/comments/1bt7epv/project_picachain_image_search_made_simple/) , 2024-04-12-0910
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

     
 
deeplearning -  [ Tengyu Ma on Voyage AI - Weaviate Podcast #91! ](https://www.reddit.com/r/deeplearning/comments/1bjft8i/tengyu_ma_on_voyage_ai_weaviate_podcast_91/) , 2024-04-12-0910
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

     
