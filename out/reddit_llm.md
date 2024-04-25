 
all -  [ 🧙Testing local llama3 at function calling and tool use. ](https://www.reddit.com/r/LangChain/comments/1ccdexb/testing_local_llama3_at_function_calling_and_tool/) , 2024-04-25-0910
```
Here's an unedited video testing tools with llama3 running locally (at 1.5x speed). The good, bad and ugly. 

https://re
ddit.com/link/1ccdexb/video/a47qddncliwc1/player


```
---

     
 
all -  [ Text Split by paragraphs? ](https://www.reddit.com/r/LangChain/comments/1ccccw6/text_split_by_paragraphs/) , 2024-04-25-0910
```
I would like to know if this is possible, I'm fairly new to langchain, I want to split into text chunks by different par
agraphs and after reading doc, still seem to be stuck on this one. Some help would be much appreciated. Thanks!

  
Edit
: Nevermind, think I got it, posting it in case anyone else has this question.

    text_splitter = CharacterTextSplitte
r(separator='\n',chunk_size=400, chunk_overlap=20)
```
---

     
 
all -  [ Question about Semantic Chunker ](https://www.reddit.com/r/LangChain/comments/1cca0h0/question_about_semantic_chunker/) , 2024-04-25-0910
```
LangChain recently added Semantic Chunker as an option for splitting documents, and from my experience it performs bette
r than RecursiveCharacterSplitter (although it's more expensive due to the sentence embeddings). 

One thing that I noti
ced though, is that there's no pre-defined limit to the size of the result chunks: I have seen chunks that are just a co
uple of words (i.e. section headers), and also very long chunks (5k+ characters). Which makes total sense, given the log
ic: if all sentences in that chunk are semantically similar, they should all be grouped together, regardless of how long
 that chunk will be. But that can lead to issues downstream: document context gets too large for the LLM, or small chunk
s that add no context at all.

Based on that, I wrote my custom version of the Semantic Chunker that optionally respects
 the character count limit (both minimum and maximum). The logic I am using is: a chunk split happens when either the se
mantic distance between the sentences becomes too large and the chunk is at least <MIN\_SIZE> long, or when the chunk be
comes larger than <MAX\_SIZE>.

My question to the community is: 

\- Does the above make sense? I feel like this approa
ch can be useful, but it kind of goes against the idea of chunking your texts semantically.

\- I thought about creating
 a PR to add this option to the official code. Has anyone contributed to LangChain's repo? What has been your experience
 doing so?

Thanks.
```
---

     
 
all -  [ Solve RAG App Optimization Puzzles with Langtrace + LlamaIndex ](https://www.reddit.com/r/LangChain/comments/1cc8fx4/solve_rag_app_optimization_puzzles_with_langtrace/) , 2024-04-25-0910
```
Hey folks,

We're building Langtrace, an open-source LLM App observability platform (www.langtrace.ai) and we recently b
uilt support for LlamaIndex, the go-to library for building retrieval-augmented generation (RAG) applications.

As build
ers, we know how frustrating it can be to optimize RAG apps (e.g. trying to figure out where the bottlenecks are, whethe
r your retrieval strategy is effective, etc.) That's why we're building a tool that makes it easy to gain deeper insight
s and optimize performance, reliability, and user experience for your LLM apps.

With Langtrace and LlamaIndex, you can:


* Get one-click observability for LlamaIndex-based RAG applications
* Visualize latency breakdowns, context relevance,
 and resource utilization
* Monitor and analyze traces, evals, metrics, and logs with OpenTelemetry

Feel free to check 
out our [repo](https://github.com/Scale3-Labs/langtrace) for [examples](https://github.com/Scale3-Labs/langtrace-docs/bl
ob/main/langtrace-examples/llamaindex_essay/starter.py.ipynb), contribute, provide feedback, and join our [community](ht
tps://discord.com/invite/EaSATwtr4t). More info on the integration with LlamaIndex [here](https://langtrace.ai/blog/lang
trace-llamaindex-a-game-changing-combo-for-rag-developers) including a video demo. Looking forward to hearing of your fe
edback! 
```
---

     
 
all -  [ Bill of material need some PoV ](https://www.reddit.com/r/LangChain/comments/1cc3m04/bill_of_material_need_some_pov/) , 2024-04-25-0910
```
I am working on a project of bill of material where a client has recieved a mail which contains the catalogue I'd the qu
antity of the catalogue and it's description,... 
The data could be in normal text , in a table , or in a image of the b
ody (not in attachments )

How should I tackle this , like image could be many and some irrelevant ones like logo of com
pany and other than there might be possibility that a duplicate data may present in text and image , and how to handle t
he thread of email 
```
---

     
 
all -  [ How are you guys doing internet search? ](https://www.reddit.com/r/LangChain/comments/1cc1dyq/how_are_you_guys_doing_internet_search/) , 2024-04-25-0910
```
I am trying to use internet-search enabled bots, and I was wondering how you guys were doing it - I see that Serpdev and
 Tavily have Langchain integration - which of these two do you guys like? Or do you roll your own?
```
---

     
 
all -  [ Help with resume review and job search strategy, please! ](https://www.reddit.com/r/resumes/comments/1cbyjzo/help_with_resume_review_and_job_search_strategy/) , 2024-04-25-0910
```
I have applied to 500+ roles at least (I have lost track of the count) through LinkedIn, Indeed, ZipRecruiter, and other
 job boards. I have applied to jobs through referrals as well. 

I have been applying to Machine Learning Engineer, Data
 Scientist, and related roles. As my resume mentions, I have over 5 years of experience in related roles. 

I usually al
ter my resume based on the job description by switching existing projects with more relevant projects, making relevant k
eywords bold, and reordering bullet points under the experience section. 

In the last 4 months, I have only had 1 techn
ical interview and around 4 screening calls. After the screening calls, the recruiters have been ghosting me and I think
 it might have to do with my Visa requirement. To clarify, I am an international student with an F1 visa graduating in M
ay.

Please let me know if there is anything wrong/ if there is any scope for improvement in my resume or job search str
ategy. I am mentally exhausted and it would be really helpful for a different set of eyes to review my resume.

Thanks f
or your time! PS, if you need any help with ML, feel free to contact me.

https://preview.redd.it/wtqzc61zkfwc1.png?widt
h=710&format=png&auto=webp&s=c89fb5af76cefc50c6348f222bae70f88169ee7f


```
---

     
 
all -  [ Creating data analytics Q&A platform using LLM ](https://www.reddit.com/r/LangChain/comments/1cbwajs/creating_data_analytics_qa_platform_using_llm/) , 2024-04-25-0910
```
Hi,
I am thinking of creating a LLM based application where questions can be asked in excel files and the files are smal
l to medium size less than 10 MB.
What is the best way to approach this problem ?
In my team there are consultants who h
ave 0 to little background on coding and SQL, so this could be a great help to them.
Thanks
```
---

     
 
all -  [ Seeking Advice: Which Framework is best suited for building GenAI Web App? ](https://www.reddit.com/r/LangChain/comments/1cbv3dv/seeking_advice_which_framework_is_best_suited_for/) , 2024-04-25-0910
```
 

Hey Redditors! 🙋‍♂️

I came up with the idea of summarizing text with various large language models (LLMs). I intend 
to develop this fully-fledged application (including a register page, login page, database etc.) using either Python, Ja
vaScript, or both. Can you advise me on which framework would be most suitable for such an endeavor? I'm seeking recomme
ndations on frameworks that excel in constructing this type of application. Some colleagues have proposed trying Flask, 
Gradio, or Django. Please share your insights on which framework would be optimal for this project, and kindly provide r
easons to support your suggestion.
```
---

     
 
all -  [ Initial tests: RAG with Phi-3 ](https://www.reddit.com/r/LangChain/comments/1cbuqow/initial_tests_rag_with_phi3/) , 2024-04-25-0910
```
I dont trust the benchmarks, so I recorded my very first test run. Completely unedited, each question asked for the firs
t time. First impression is that it is good, very very good for its size. Sharing the code below.

https://reddit.com/li
nk/1cbuqow/video/ay3us3wbmewc1/player
```
---

     
 
all -  [ Error: 'builtin_function_or_method' object has no attribute '__func__' ](https://www.reddit.com/r/LangChain/comments/1cbuikm/error_builtin_function_or_method_object_has_no/) , 2024-04-25-0910
```
Hi all,

  
First time using LangChain, I'm following [a guide](https://www.youtube.com/watch?v=BrsocJb-fAo&t=631s) and 
I'm getting this error, does anyone know what might be wrong? I'm using Pinecone along with this, I'm not sure if that m
akes a difference.

  
For my Pinecone API environment I'm using 'us-east-1' - I'm unsure if this is the right format?




I'd be very grateful for any input!

  
Many thanks in advance :)



So this is my code:

    from langchain_community
.vectorstores import DocArrayInMemorySearch
    
    vectorstore1 = DocArrayInMemorySearch.from_texts(
        [
       
     'Mary's sister is Susana',
            'John and Tommy are brothers',
            'Patricia likes white cars',
    
        'Pedro's mother is a teacher',
            'Lucia drives an Audi',
            'Mary has two siblings',
        
],
        embedding=embeddings,
    )
    

  
And I'm getting this error:

    AttributeError                         
   Traceback (most recent call last)
    Cell In[58], line 3
          1 from langchain_community.vectorstores import Do
cArrayInMemorySearch
    ----> 3 vectorstore1 = DocArrayInMemorySearch.from_texts(
          4     [
          5        
 'Mary's sister is Susana',
          6         'John and Tommy are brothers',
          7         'Patricia likes white
 cars',
          8         'Pedro's mother is a teacher',
          9         'Lucia drives an Audi',
         10      
   'Mary has two siblings',
         11     ],
         12     embedding=embeddings,
         13 )
    
    File ~\AppDa
ta\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\l
angchain_community\vectorstores\docarray\in_memory.py:68, in DocArrayInMemorySearch.from_texts(cls, texts, embedding, me
tadatas, **kwargs)
         46 u/classmethod
         47 def from_texts(
         48     cls,
       (...)
         52  
   **kwargs: Any,
         53 ) -> DocArrayInMemorySearch:
         54     '''Create an DocArrayInMemorySearch store and
 insert data.
         55 
    ...
    
    ---> 46         return Generic.__class_getitem__.__func__(cls, item)  # type
: ignore
         47         # this do nothing that checking that item is valid type var or str
         48     if not i
ssubclass(item, BaseDoc):
    
    AttributeError: 'builtin_function_or_method' object has no attribute '__func__'


```
---

     
 
all -  [ How to fine-tune the answers of LLM in a RAG application ](https://www.reddit.com/r/LangChain/comments/1cbrpms/how_to_finetune_the_answers_of_llm_in_a_rag/) , 2024-04-25-0910
```
I have built a RAG application with my own PDF documents.

Some of the answers are not correct, usually they are from wr
ong documents even if the right ones have been retrieved.

What is the right way to approach it?
```
---

     
 
all -  [ GenAI & Java  ](https://www.reddit.com/r/java/comments/1cbrcz8/genai_java/) , 2024-04-25-0910
```
The company I work for is mostly a Java shop. Recently there has been a push to create LLM integrated applications that 
are taking the form of chat bots and are able to reference company data. In the beginning we started with Java but quick
ly switched to python using langchain since it seemed like the appropriate thing to do as “everyone” uses python for “ai
”/ml projects. Looking back now tho, we would have been better off in Java for our first app since we never used any thi
ng special in Langchain. 

My question to you all is whether you’ve worked on any GenAI based projects using Java? I’m a
ware of langchain4j and it seems sufficient except it’s lacking the new rage of multi agents. 

I really dislike python 
and would prefer to work in Java, but I feel like we’re forced to follow the python charade straight off a cliff. 
```
---

     
 
all -  [ How to quickly build and deploy scalable RAG applications? ](https://www.reddit.com/r/truefoundry/comments/1cbr66y/how_to_quickly_build_and_deploy_scalable_rag/) , 2024-04-25-0910
```
While RAG is undeniably impressive, the process of creating a functional application with it can be daunting. There's a 
significant amount to grasp regarding implementation and development practices, ranging from selecting the appropriate A
I models for the specific use case to organizing data effectively to obtain the desired insights. While tools like LangC
hain and LlamaIndex exist to simplify the prototype design process, there has yet to be an accessible, ready-to-use open
-source RAG template that incorporates best practices and offers modular support, allowing anyone to quickly and easily 
utilize it.

We have recently introduced our new open-source framework called [Cognita](https://github.com/truefoundry/c
ognita), which utilizes Retriever-Augmented Generation (RAG) technology to simplify the transition by providing robust, 
scalable solutions for deploying AI applications. AI development often begins in experimental environments such as Jupyt
er notebooks, which are useful for prototyping but not well-suited for production environments. However, Cognita aims to
 bridge this gap. Developed on top of Langchain and LlamaIndex, Cognita offers a structured and modular approach to AI a
pplication development. Each component of the RAG, from data handling to model deployment, is designed to be modular, AP
I-driven, and extendable.
```
---

     
 
all -  [ Question: PydanticOutputParser Compatibility Beyond ChatOpenAI? ](https://www.reddit.com/r/LangChain/comments/1cbr66a/question_pydanticoutputparser_compatibility/) , 2024-04-25-0910
```
Does PydanticOutputParser only function with ChatGPT from OpenAI, or does it extend its support to other large language 
models (LLMs) as well? 

I'm particularly interested in using it with models available through groq and wondering if any
one has explored this compatibility. 
```
---

     
 
all -  [ How to quickly build and deploy scalable RAG applications? ](https://www.reddit.com/r/LangChain/comments/1cbqzlr/how_to_quickly_build_and_deploy_scalable_rag/) , 2024-04-25-0910
```
While RAG is undeniably impressive, the process of creating a functional application with it can be daunting. There's a 
significant amount to grasp regarding implementation and development practices, ranging from selecting the appropriate A
I models for the specific use case to organizing data effectively to obtain the desired insights. While tools like LangC
hain and LlamaIndex exist to simplify the prototype design process, there has yet to be an accessible, ready-to-use open
-source RAG template that incorporates best practices and offers modular support, allowing anyone to quickly and easily 
utilize it.

TrueFoundry has recently introduced a new open-source framework called [**Cognita**](https://github.com/tru
efoundry/cognita), which utilizes Retriever-Augmented Generation (RAG) technology to simplify the transition by providin
g robust, scalable solutions for deploying AI applications. AI development often begins in experimental environments suc
h as Jupyter notebooks, which are useful for prototyping but not well-suited for production environments. However, Cogni
ta aims to bridge this gap. Developed on top of Langchain and LlamaIndex, Cognita offers a structured and modular approa
ch to AI application development. Each component of the RAG, from data handling to model deployment, is designed to be m
odular, API-driven, and extendable.
```
---

     
 
all -  [ Does anybody have good tutorial or page or repo which targets the Runnable Parallels of Lang chain? ](https://www.reddit.com/r/LangChain/comments/1cbqwg2/does_anybody_have_good_tutorial_or_page_or_repo/) , 2024-04-25-0910
```
I am working on project where I have multiple documents to process using output parser of Lang Chain, as I have Mutiple 
it takes time, so to reduce time I am planning to process each doc in parallel to reduce the time.
```
---

     
 
all -  [ How to make llm differentiate whether to retrieve or not ](https://www.reddit.com/r/LangChain/comments/1cbq1jt/how_to_make_llm_differentiate_whether_to_retrieve/) , 2024-04-25-0910
```
Hi,
So I have a rag application/chatbot, uses conversationalretrivalqa chain from Langchain, say if for questions like '
Hi' and all retrieval is happening, and its returning random documents 
How do I make the llm answer directly without re
trieval for questions like this.?
 And one more thing how do I implement a memory(longterm will be better) with conversa
tionalretrivalqa.from_llm chain..whatever I tried is not working, 
I tried with the Runnablehistory but that screws up t
he retrieval 
Does anyone have any workaround on that.?
Any help will be appreciated ,thanks 
```
---

     
 
all -  [ JsonOutputParser conflicting with Tavily ](https://www.reddit.com/r/LangChain/comments/1cbodkf/jsonoutputparser_conflicting_with_tavily/) , 2024-04-25-0910
```
I am working with LangGraph and used the multi agent collaboration example ([github](https://github.com/langchain-ai/lan
ggraph/blob/main/examples/multi_agent/multi-agent-collaboration.ipynb)). To the create\_agent(...) helper method, I adde
d the following so that the response from LLMs would match a format I can use.

    parser = JsonOutputParser(pydantic_o
bject=MyResponse)
    ...
    return prompt | llm.bind_functions(functions) | parser

This works and provides a python d
ict that is easy to work with. So far so good.

The issue is when the LLM wants to use the Tavily search tool which is f
ailing at `result = agent.invoke(state)` with **OutputParserException('Invalid json output: ')**  because the llm obviou
sly wants to call Tavily which has its own shape being something like that:

>tavily\_search\_results\_json

Which obvio
usly doesnt conform to the MyResponse class, but the parser is kicking in anyway.

I guess I can make a Researcher agent
 which doesnt have the JsonOutputParser and a Worker that doesn't have the Tavily tool but, I figure there must be a way
 to get JsonOutputParser to work with tools like Tavily. I mean they can't just be outright incompatible (i.e. if you ha
ve an agent with a parser, it can't have the tavily tool).

This is my full create\_agent function if anybody knows what
 it should look like in terms of getting the parsers and tools to play nice:

    def create_task_agent(llm, tools, syst
em_message: str):
        '''Create an agent.'''
        functions = [convert_to_openai_function(t) for t in tools]
    
    functions.append(convert_pydantic_to_openai_function(TaskResponse))
        prompt = ChatPromptTemplate.from_message
s(
            [
                (
                    'system',
                    'some message',
                ),

                MessagesPlaceholder(variable_name='messages'),
            ]
        )
        parser = JsonOutputParser
(pydantic_object=TaskResponse)
        prompt = prompt.partial(system_message=system_message)
        prompt = prompt.pa
rtial(task_response='TaskResponse')
        prompt = prompt.partial(tool_names=', '.join([tool.name for tool in tools]))

        prompt = prompt.partial(format_instructions=parser)
        return prompt | llm.bind_functions(functions) | par
ser


```
---

     
 
all -  [ I tested LANGCHAIN vs VANILLA speed ](https://www.reddit.com/r/LangChain/comments/1cbj7gg/i_tested_langchain_vs_vanilla_speed/) , 2024-04-25-0910
```
**Code of pure implementation through POST to local ollama** [**http://localhost:11434/api/chat**](http://localhost:1143
4/api/chat) **(3.2s):**

    import aiohttp
    from dataclasses import dataclass, field
    from typing import List
   
 import time
    start_time = time.time()
    
    @dataclass
    class Message:
        role: str
        content: str

    
    @dataclass
    class ChatHistory:
        messages: List[Message] = field(default_factory=list)
    
        de
f add_message(self, message: Message):
            self.messages.append(message)
    
    @dataclass
    class RequestDa
ta:
        model: str
        messages: List[dict]
        stream: bool = False
    
        @classmethod
        def f
rom_params(cls, model, system_message, history):
            messages = [
                {'role': 'system', 'content': 
system_message},
                *[{'role': msg.role, 'content': msg.content} for msg in history.messages],
            
]
            return cls(model=model, messages=messages, stream=False)
    
    class LocalLlm:
        def __init__(sel
f, model='llama3:8b', history=None, system_message='You are a helpful assistant'):
            self.model = model
      
      self.history = history or ChatHistory()
            self.system_message = system_message
    
        async def as
k(self, input=''):
            if input:
                self.history.add_message(Message(role='user', content=input))
 
   
            data = RequestData.from_params(self.model, self.system_message, self.history)
    
            url = 'ht
tp://localhost:11434/api/chat'
            async with aiohttp.ClientSession() as session:
                async with ses
sion.post(url, json=data.__dict__) as response:
                    result = await response.json()
                    p
rint(result['message']['content'])
    
            if result['done']:
                ai_response = result['message']['
content']
                self.history.add_message(Message(role='assistant', content=ai_response))
                retur
n ai_response
            else:
                raise Exception('Error generating response')
    
    
    if __name__ =
= '__main__':
        chat_history = ChatHistory(messages=[
            Message(role='system', content='You are a crazy 
pirate'),
            Message(role='user', content='Can you tell me a joke?')
        ])
    
        llm = LocalLlm(his
tory=chat_history)
        import asyncio
        response = asyncio.run(llm.ask())
        print(response)
        prin
t(llm.history)
        print('--- %s seconds ---' % (time.time() - start_time))
    

`--- 3.2285749912261963 seconds --
-`

&#x200B;

**Lang chain equivalent (3.5 s):**

    from langchain_core.messages import HumanMessage, SystemMessage, A
IMessage, BaseMessage
    from langchain_community.chat_models.ollama import ChatOllama
    from langchain.memory import
 ChatMessageHistory
    import time
    start_time = time.time()
    
    class LocalLlm:
        def __init__(self, mod
el='llama3:8b', messages=ChatMessageHistory(), system_message='You are a helpful assistant', context_length = 8000):
   
         self.model = ChatOllama(model=model, system=system_message, num_ctx=context_length)
            self.history = 
messages
    
        def ask(self, input=''):
            if input:
                self.history.add_user_message(input
)
            response = self.model.invoke(self.history.messages)
            self.history.add_ai_message(response)
    
        return response
    
    if __name__ == '__main__':
        chat = ChatMessageHistory()
        chat.add_message
s([
            SystemMessage(content='You are a crazy pirate'),
            HumanMessage(content='Can you tell me a jok
e?')
        ])
        print(chat)
        llm = LocalLlm(messages=chat)
        print(llm.ask())
        print(llm.his
tory.messages)
        print('--- %s seconds ---' % (time.time() - start_time))
    

`--- 3.469588279724121 seconds ---
`

&#x200B;

&#x200B;

So it's 3.2 vs 3.469(nice) so the difference so 0.3s difference is nothing.  
Made this post beca
use was so upset over [this post](https://www.reddit.com/r/LangChain/comments/1c6zktz/llms_frameworks_langchain_llamaind
ex_griptape/) after getting to know langchain and finally coming up with some results. I think it's true that it's not v
ery suitable for serious development, but it's perfect for theory crafting and experimenting, but anyways you can just w
rite your own abstractions which you know. 
```
---

     
 
all -  [ No avoiding langchain? ](https://www.reddit.com/r/LocalLLaMA/comments/1cbhu0e/no_avoiding_langchain/) , 2024-04-25-0910
```
Hi all,

I've worked with langchain in the past prototyping simple RAG applications and it was a headache constantly fig
hting the APIs or trying to peel the abstractions using the confusing docs.

After that experience I ditched it and have
 done the RAG project just doing everything in raw python and calling the native APIs of each components which made thin
gs so much easier and development enjoyable again.

Recently I've been looking at using agents on a wider scale rather t
han the simple assistant/reviewer pattern and crew.ai really looked promising. Unfortunately it seems to heavily integra
te langchain which meant delving into the langchain docs is required if you want to customise the base components. Manag
ed to circumvent a lot of it this time by just using a lot of custom tools instead.

My question is should I just bite t
he bullet and learn langchain properly if I want to do more developments beyond the simple chatbots? Might be required i
f most cool new frameworks in the future will be using langchain as the base.
```
---

     
 
all -  [ How to use AI to completely automate your youtube channel ](https://www.reddit.com/r/Automate/comments/1cbhhvd/how_to_use_ai_to_completely_automate_your_youtube/) , 2024-04-25-0910
```
 Hi folks,

I wanted to share with you a cool project I recently undertook that leverages the power of AI to help manage
 my YouTube channel!

The idea was to use [CrewAI](https://www.crewai.com/) to automate tasks like competitor YouTube ch
annel analysis and identify trending topics. This way, I could gauge these topics against my own content ideas to see if
 there is general interest in a given topic.

The AI Crew was designed to crawl the web (Google) and call APIs like the 
YouTube API, Reddit API, and use Google Trends to determine how likely a given topic is to generate engagement.

For thi
s, I created the following AI Assistants (or agents in CrewAI lingo):

* A competitor analysis agent
* A Content Creator
 (to generate ideas from research)
* A Marketing advisor, to generate catchy titles and tags
* An Analytics consultant t
o measure the performance of the video

I used a pretty straightforward setup that relied on the usual suspects:

* Anac
onda
* Python 3.11
* A few modules like pytrend, praw, serper, and langchain

I tested it with models like GPT-4, GPT-4-
Turbo, and a few local models like nous-hermes 2, mistral, and codellama, among others.

The results from GPT-4-Turbo we
re AMAZING, and I'm sure I can make them better by fine tuning the data going into the model, but they were not really t
hat great with local AI, which was quite expected given the imense number of tokens. However I was quite positively surp
rised by the performance of Nous Hermes 2 - 13b. Not only did it actually run, but it used the tools I custom build for 
it! Quite impressive really

The video is available below:

[https://youtu.be/5JoVeYcxgpU?si=cxFwHO1x\_zCghMYB](https://
youtu.be/5JoVeYcxgpU?si=cxFwHO1x_zCghMYB)

You are more than welcome to try out the code for yourselves: [https://github
.com/fmiguelmmartins/crewaiyoutube](https://github.com/fmiguelmmartins/crewaiyoutube)

And here is an article on Medium 
with the step-by-step process (don't worry, I have a free account):

[https://medium.com/@fmiguelmmartins/create-an-ai-t
eam-to-manage-your-youtube-channel-5dc1e6c9b31b](https://medium.com/@fmiguelmmartins/create-an-ai-team-to-manage-your-yo
utube-channel-5dc1e6c9b31b)

Hope you guys enjoy it, and if you are kind enough, please leave me some feedback so I can 
improve over time!

Thank you!

Filipe
```
---

     
 
all -  [ Langchain vs llamaindex ](https://www.reddit.com/r/LangChain/comments/1cbfeci/langchain_vs_llamaindex/) , 2024-04-25-0910
```
I'm using llamaindex for a multilingual database retriever system and using claude as the provider. I'm interested in in
tegrating external apis( function calling) and knowledge graphs.

Separately it'd also be helpful to have the ability to
 manage states within a conversation and langgraph seems to meet the criteria.

Should I switch to langchain and rewrite
 my early stage code? Does langchain function calling work well with Claude? does llamaindex offer langgraph like abilit
ies or good integration with neo4j?
```
---

     
 
all -  [ preserving the Gemini state with Langchain for caching responses ](https://www.reddit.com/r/LangChain/comments/1cbf1au/preserving_the_gemini_state_with_langchain_for/) , 2024-04-25-0910
```
hi there, so my issue is that i want to preserve the chat history with gemini, and according to need manipulate it, i ca
n do it in google provided sdk, i dont know how to do that in langchain, i want to manupilate chat history and according
 to need, delete some responces, add new responces from the database.

also, i am only interested in langchain responses
 (semantic) caching support, if i can do caching without the need of langchain or implementing a rag myself manually, i 
am all up for that solution!
```
---

     
 
all -  [ How to structure the vector store and retrieval for user files RAG? ](https://www.reddit.com/r/LangChain/comments/1cbdk3m/how_to_structure_the_vector_store_and_retrieval/) , 2024-04-25-0910
```
Hey all. I'm building a simple chatbot that will let users hold their own documents to use in RAG; basically I just want
 them to be able to ask questions related to what's on their own files. I'm using LangChain of course, using postgres wi
th the pgvector extension. 

My question is, what's the most optimized way to design the documents table(s) in order for
 users to only be able to search their own files? Do you create separate doc tables for each user? Do you filter through
 metadata or some other technique? Metadata filtering in particular doesn't look like it'd be too optimized, so I'm just
 looking into how best to think about storing and retrieving from a vector store for this use case. I don't want the bot
 to be able to find the answer in another user's files.

Or am I just thinking about the whole thing in the wrong way an
d is there a better way to structure all  this? 

Thanks a lot in advance!
```
---

     
 
all -  [ How to solve if relevant docs > max top_k ? ](https://www.reddit.com/r/LangChain/comments/1cbcln9/how_to_solve_if_relevant_docs_max_top_k/) , 2024-04-25-0910
```
Basically if I have a pdf of 100 pages and to answer my question I need 30 diff chunks across diff pages. 
Now if my top
_k is set to 20. How will this ever be possible?

Like in general, isn't this a issue with RAGs? How can I know how many
 chunks are needed to answer a question? If it's less than whatever topk I set, it's fine. But what if there are more?


Is this a limitation of RAG? If no, how to solve for this?
If yes, what other ways can I explore?
```
---

     
 
all -  [ [thread] The best open-source only AI models ](https://www.reddit.com/r/ChatGPT/comments/1cbbklh/thread_the_best_opensource_only_ai_models/) , 2024-04-25-0910
```
Hello community! If you know some good models and fine-tuning options, please feel free to share them:

- Image Captioni
ng (img-to-text)
- Video Captioning (video-to-text)
- Audio Captioning (music understanding to describe how somebody sin
gs and music)
- Image Generation (text-to-image, LoRAs, Checkpoints)
- LLMs (general knowledge, uncensored)
- Instrument
al and Vocal music generation (text-to-music/audio, or/and with source audio)
- Video generation (sora-like text/image-t
o-video)
- 2D animation (talking head, anime)
- Voice Cloning (except RVC)
- TTS (with unlabeled voice patterns training
 and fast generations)
- LangChain and Long-Term memory raw code examples

And please, with Apple Silicon (M1) support!!
!!!
```
---

     
 
all -  [ Getting totals and counts based on the entire dataset with RetrievalQA ](https://www.reddit.com/r/LangChain/comments/1cb9mab/getting_totals_and_counts_based_on_the_entire/) , 2024-04-25-0910
```
Hello guys, I'm new on this of NPL and Langchain, I'm currently working on a chatbot to 'talk' to my data, converting pa
ndas dataframes into JSON and every row in dataframe is a document saved into Vector Store (I'm using Milvus as Vector D
atabase). 

For questions related to 1 to N (getting one row from many), the similarity search is working as expected an
d I am achieving good results.

For example, if I asking 'where this store is located?' or 'how many displays has Store 
A?' is working, but if I ask something about the entire dataset as 'how many displays are overall in US?', or 'how many 
displays are in California?', the totalization is related to the 'k' passed to the vector retriever:

    retriever = Ve
ctorStoreRetriever(
        vectorstore=vector,
        search_type='similarity',
        search_kwargs={'k': 10}
    ) 
       
    chain = RetrievalQA.from_chain_type(
     llm=llm,
     retriever=retriever,
     chain_type='stuff',
     v
erbose=True
    )
    

  
I cannot pass a bigger 'K' because my LLM rejects it (I'm using Google Gemini-Pro).

  
There
 is a way to:

1. Check if the user's question involves a quantification.
2. Executing something like a 'Map Reduce' ove
r the entire dataset to return the reduced version of the documents (or documents with question applied).
3. Passing the
 reduction to the LLM for getting the final result.

Or if there is a way to making this in Langchain using another type
 on Chain.
```
---

     
 
all -  [ How can I see the input that is passed to the output parser when the commands are chained? ](https://www.reddit.com/r/LangChain/comments/1cb7rx7/how_can_i_see_the_input_that_is_passed_to_the/) , 2024-04-25-0910
```
This is the excerpt from my code:  
`chain = prompt_template | ollama | output_parser`

How do I store the output from `
ollama` as a variable and then pass that output to `output_parser`?  


I don't understand how the pipe operator | works
. I am asking the ollama model to give me a structured output and I need to be able to debug and see what the output was
 when the output\_parser gives an error.
```
---

     
 
all -  [ Langsmith render of retrieved documents ](https://www.reddit.com/r/LangChain/comments/1cb68b9/langsmith_render_of_retrieved_documents/) , 2024-04-25-0910
```
I have been using langsmith for controling the retrieving step of my rag application. And it's nice because it has a ren
der that format the raw langchain docs in a more readable format. 

The problem is that since I changed the format of my
 langchain docs, adding more metadata, this feature does not work anymore. Do anyone has got any advice on what's the ri
ght format compatible to the render??

now: 

https://preview.redd.it/7leugfcup8wc1.png?width=1266&format=png&auto=webp&
s=f7738461ab2add7e587aeb9aed415a5b2e1f6c20

BEFORE:

https://preview.redd.it/8s86iy6xp8wc1.png?width=1287&format=png&aut
o=webp&s=302f1f3b2923f428288c59c29f31327d5d9b6db0


```
---

     
 
all -  [ Use Golang to develop Agentic applications with LLMs ](https://www.reddit.com/r/llmops/comments/1cb570i/use_golang_to_develop_agentic_applications_with/) , 2024-04-25-0910
```
[ZenModel](https://github.com/zenmodel/zenmodel) is a workflow programming framework designed for constructing agentic a
pplications with LLMs. It implements by the scheduling of computational units (`Neuron`), that may include loops, by con
structing a `Brain` (a directed graph that can have cycles) or support the loop-less DAGs. A `Brain` consists of multipl
e `Neurons` connected by `Link`s. Inspiration was drawn from [LangGraph](https://github.com/langchain-ai/langgraph). The
 `Memory` of a `Brain` leverages [ristretto](https://github.com/dgraph-io/ristretto) for its implementation.

**Agent Ex
amples developed by** [ZenModel](https://github.com/zenmodel/zenmodel) **framework**

* [Chat Agent With Tools](https://
github.com/zenmodel/zenmodel/blob/main/examples/chat_agent/chat_agent_with_function_calling)
* [Basic Reflection](https:
//github.com/zenmodel/zenmodel/blob/main/examples/reflection/main.go)
* [Plan & Execute](https://github.com/zenmodel/zen
model/blob/main/examples/plan-and-excute)
* [Multi-Agent](https://github.com/zenmodel/zenmodel/blob/main/examples/multi-
agent/agent-supervisor)
```
---

     
 
all -  [ How does chunk size relate to an embedding model's dimension of vectors and max token lenght? ](https://www.reddit.com/r/LangChain/comments/1cb4yjd/how_does_chunk_size_relate_to_an_embedding_models/) , 2024-04-25-0910
```
Hi, everyone! I'm fairly new to NLP tasks, and I'm currently building a langchain RAG app, and for that I need to do som
e testings with different chunks sizes.

I'm currently using a large BERT model, and what I've been confused about is: W
hat is the relationship between the chunk size chosen to chunk my documents, and the embedding model's vector dimension 
(if there is any) or even the max token limit?

I've seen a wide range of articles from people testings out chunk sizes 
from 128 to 2048, but I've also read in some places that the original BERT models take 512 tokens max. What does that in
fluence on the way I'm doing things?

I'm creating embeddings like this: Using RecursiveCharacterSplitter with different
 chunks sizes and len function using my bert model's tokenizer and finally creating embeddings with HuggingFaceBgeEmbedd
ings (arbitrary choice, I couldn't figure out which class to choose) and storing on a vector store.

I iterated over my 
chunked documents (splitted using the same flow mentioned above) and their sizes nor the amount of tokens gotten from to
kenizing it directly are equal to my chunk\_size:

https://preview.redd.it/s9txv1rej8wc1.png?width=1015&format=png&auto=
webp&s=a11725cf9967ec9a04ddad46f8c2bedc587d7ed8

But the actual embeddings are generated with dimension 1024 (which is t
he correct value for vector dimensions for large bert models):

https://preview.redd.it/9dta4kymj8wc1.png?width=1210&for
mat=png&auto=webp&s=31c1787b790d1ecabe5a91c54735b5f0dded62de

The reason I'm asking this is because I've been gettting s
ome weird results analyzing results with chunks bigger than 512 (this graph is a comparison of the chunk overlap with fi
xed chunk size = 1024, where the results don't really vary even though I'm varying other parameters, like chunk overlap 
here, which does affect other chunk sizes comparisons)

https://preview.redd.it/x7qwsfo2g8wc1.png?width=1015&format=png&
auto=webp&s=a3c2273dbe60d07c6974d64802b1b6391398e3d0
```
---

     
 
all -  [ Query with langchain's parent-child retriever ](https://www.reddit.com/r/LangChain/comments/1cb4xpb/query_with_langchains_parentchild_retriever/) , 2024-04-25-0910
```
I have a requirement to create parent-child retrieval mechanism for texts. On langchain's official docs I can see the be
low code:

    #This text splitter is used to create the parent documents
    parent_splitter = RecursiveCharacterTextSp
litter(chunk_size=2000)
    
    #This text splitter is used to create the child documents
    #It should create documen
ts smaller than the parent
    child_splitter = RecursiveCharacterTextSplitter(chunk_size=400)
    
    #The vectorstore
 to use to index the child chunks
    vectorstore = Chroma( collection_name='split_parents',embedding_function=OpenAIEmb
eddings() )
    
    #The storage layer for the parent documents
    store = InMemoryStore()
    
    retriever = Parent
DocumentRetriever(
        vectorstore=vectorstore,
        docstore=store,
        child_splitter=child_splitter,
     
   parent_splitter=parent_splitter,
    )

My question is why there is no **split\_text()** for each parent and child ch
unks that actually splits te document?

&#x200B;
```
---

     
 
all -  [ Use Golang to develop Agentic applications with LLMs ](https://www.reddit.com/r/LLMDevs/comments/1cb4wcz/use_golang_to_develop_agentic_applications_with/) , 2024-04-25-0910
```
[ZenModel](https://github.com/zenmodel/zenmodel) is a workflow programming framework designed for constructing agentic a
pplications with LLMs. It implements by the scheduling of computational units (`Neuron`), that may include loops, by con
structing a `Brain` (a directed graph that can have cycles) or support the loop-less DAGs. A `Brain` consists of multipl
e `Neurons` connected by `Link`s. Inspiration was drawn from [LangGraph](https://github.com/langchain-ai/langgraph). The
 `Memory` of a `Brain` leverages [ristretto](https://github.com/dgraph-io/ristretto) for its implementation.

**Agent Ex
amples developed by** [**ZenModel**](https://github.com/zenmodel/zenmodel) **framework**

* [Chat Agent With Tools](http
s://github.com/zenmodel/zenmodel/blob/main/examples/chat_agent/chat_agent_with_function_calling)

https://preview.redd.i
t/mpvv198ie8wc1.png?width=595&format=png&auto=webp&s=d81cad5e81b9ca56e879da3c2bb4c24cd932f1c9

* [Basic Reflection](http
s://github.com/zenmodel/zenmodel/blob/main/examples/reflection/main.go)

https://preview.redd.it/q0xdzvhje8wc1.png?width
=617&format=png&auto=webp&s=7d9cd9d0c0ca4cd54fd240855f69077ffc94da0e

* [Plan & Execute](https://github.com/zenmodel/zen
model/blob/main/examples/plan-and-excute)

https://preview.redd.it/fai7axjke8wc1.png?width=686&format=png&auto=webp&s=d4
606196a86bce55632b72f911c9f05de327cf89

* [Multi-Agent](https://github.com/zenmodel/zenmodel/blob/main/examples/multi-ag
ent/agent-supervisor)

https://preview.redd.it/sd4rv4ple8wc1.png?width=502&format=png&auto=webp&s=22ed17e1ff3245f0ffd23a
18aca1b172798014ae


```
---

     
 
all -  [ Updation of PDFs using RAG ](https://www.reddit.com/r/RagAI/comments/1cb3geo/updation_of_pdfs_using_rag/) , 2024-04-25-0910
```
I am trying to build a chatbot using RAG and LangChain that will update the PDFs based on the user prompt and the pdfs w
ill be stored in a db (chromedb) that will be connected to the chatbot. I'm planning to use OpenAI for chunking and inde
xing information that will be analyzed by the bot.

It will be helpful if anyone can tell me how to proceed further with
 this. I have only found projects and repos which focus on QA chatbots so I just want to extend this project to include 
this functionality.
```
---

     
 
all -  [ Chat-bot using RAG to update PDFs ](https://www.reddit.com/r/LangChain/comments/1cb35fa/chatbot_using_rag_to_update_pdfs/) , 2024-04-25-0910
```
I am trying to build a chatbot using RAG and LangChain that will update the PDFs based on the user prompt and the pdfs w
ill be stored in a db (chromedb) that will be connected to the chatbot. I'm planning to use OpenAI for chunking and inde
xing information that will be analyzed by the bot. 

It will be helpful if anyone can tell me how to proceed further wit
h this. I have only found projects and repos which focus on QA chatbots so I just want to extend this project to include
 this functionality.
```
---

     
 
all -  [ Llama 3 70b is not great with tools ](https://www.reddit.com/r/AI_Agents/comments/1cb2zf7/llama_3_70b_is_not_great_with_tools/) , 2024-04-25-0910
```
Hi all,

I run and crew_ai crew that does process engineering by using the langchain human tool to conduct an interview 
with a business owner to understand the business process, understand it, model it in bpmn and then identify potential fo
r improvements. GPT 4 turbo is actually decent at doing this. It actually understands when to ask the human as part of t
he interview and when to actually think for itself.

Llama3 on the other hand always uses the human tool even though it 
totally does not make sense in context of the interview. For example, ChatGPT will consider „what are important steps du
ring an interview to engineer a business process“ before asking questions. Llama will just plainly request the answer fr
om the human.

Solution could be to have more agents and subtasks to actually restrain when LLama gets access to the hum
an, but for now, GOT seems way easier to use.
```
---

     
 
all -  [ Using local LLMS instead of LLMS such as OpenAI on LangChain using JS,TS ](https://www.reddit.com/r/LLMDevs/comments/1cb0we4/using_local_llms_instead_of_llms_such_as_openai/) , 2024-04-25-0910
```
Hey guys, i'm fairly new to this and i was searching for a way to use my own locally installed LLMs from HuggingFace. I 
looked through the official documentation and this is the normal way to invoke and get a response using JS

\-----------
---------------------------------------------------------------------

const chatModel = new ChatOpenAI({});

const resp
onse = await chatModel.invoke()

\--------------------------------------------------------------------------------

So y
ea, referring back to my question. Can you guys provide me some documentations or some ways to use my own LLMs from Hugg
ingFace and not having to specify out using the ChatOpenAI class in a NodeJS project i'm working on? Thanks a bunch
```
---

     
 
all -  [ What embedding model to use to convert textual data in PDF when using FAISS ](https://www.reddit.com/r/LangChain/comments/1cb0p5d/what_embedding_model_to_use_to_convert_textual/) , 2024-04-25-0910
```
I am getting a lot of errors and it particularly because the FAISS index expects a particular shape for embeddings and e
ven after I resolved that. I cannot get the right response to my query or some or the other errors are popping up?
NOTE:
 I can’t use langchain 
```
---

     
 
all -  [ How to integrate GenAI in full stack applications? ](https://www.reddit.com/r/developersIndia/comments/1cb0lpj/how_to_integrate_genai_in_full_stack_applications/) , 2024-04-25-0910
```
Hello everyone, I started working at a small company as Generative AI developer, and currently there is another Mern Sta
ck Developer who will be working with me.   
Now, we have been tasked at creating a full stack application, but we are k
ind stuck, on how to integrate Generative AI tools (llama index, langchain, litellm, RAG etc) in a MERN stack app?   
Th
ere are 3 ways which we thought of,  
1. Make Python the main backend framework and write the full backend code in Djang
o instead of express.

2.  Make 2 separate backends, 1 that serves the GenAI tools on a FastAPI Framework, and other Exp
ress server that handles rest of the site, but the issue is interaction of both backends, extra latency, extra costs, an
d the flow of data across them.  
3. Create the backend in express and somehow use the tools in JS as possible in python
.

Now to clear up some things, I am a beginner. I had no interest in Web Dev hence I picked up AI and ML since it was o
ne of the things I was very fond of even before the GPT days. Secondly, he has made full stack apps but he hasn't deploy
ed any of them in production.

If we go 1, I'll have to create the whole backend in Django, for the rest of the site as 
well, which is honestly challenging at first but at some point I am also upskilling myself.   
If we go with 3, I will s
till upskill myself by writing JS code for GenAI, but I don't really know how flexible it is compared to python.

So, fe
llow developers who have had experience with full stack GenAI apps in production. please help out a fellow beginner!  
A
ll criticisms welcome.  
Thank You. 
```
---

     
 
all -  [ Can I get only stringified json as an output from LLM model. ](https://www.reddit.com/r/LocalLLaMA/comments/1cb0gfs/can_i_get_only_stringified_json_as_an_output_from/) , 2024-04-25-0910
```
Literally the title. I am using Mistral 7b instruct v0.2. my usecase is to generate stringified json from prompt. The mi
stral model is doing well as from prompt it does generate the json. But I need it to generate the stringified format of 
that json.

What should I do? I have heard of a framework called as langchain, can it help me here? Or should I consider
 any other model for the same, whichever would be more efficient.

Thanks
```
---

     
 
all -  [ Langchain LCEL explained the easy way ](https://www.reddit.com/r/LangChain/comments/1cb01ch/langchain_lcel_explained_the_easy_way/) , 2024-04-25-0910
```
Hello guys,

Just wrote a new blog post explaining Langchain LCEL in a easier manner: [link](https://www.metadocs.co/). 
 
I really love LCEL (feels a little like functional programing right !?) and wanted to try to explain it in a simpler w
ay.  
Enjoy.
```
---

     
 
all -  [ Reranking after RRF-Hybrid Search? ](https://www.reddit.com/r/LangChain/comments/1cazrxf/reranking_after_rrfhybrid_search/) , 2024-04-25-0910
```
Hey everyone,

me and my company are currently building a(nother) RAG system for our customers in the legal sector. 

We
 are performing a keyword (BM25) + vector search and then using Reciprocal Rank Fusion (RRF) algorithm fuse the combined
 10 top\_k results and feed them into our LLM. 

We have also implemented HyDE (hypothetical document embeddings) [https
://github.com/texttron/hyde](https://github.com/texttron/hyde) to further improve retrieval quality. 

Now I read throug
h a few articles on Medium and Reddit and saw a lot of recommendations to use reranking to further improve results. 

Do
es it make sense to again rerank the results of the hybrid search, even though strictly speaking we already are rerankin
g them based on the output of BM25 + vector search? I specifically thought about Cohere rerank here. 

Thanks and greets
!
```
---

     
 
all -  [ I want a chatgpt 3 or 4 assistant , is there any solution exists for below requirements? If not how  ](https://www.reddit.com/r/LangChain/comments/1cazcu3/i_want_a_chatgpt_3_or_4_assistant_is_there_any/) , 2024-04-25-0910
```


 
I want a chatgpt 3 or 4 assistant which will have access to my calendar 
Also able to create daily todo list 
Help m
e brain stom ideas and save it somewhere like a document.
It should remember all old conversations 
It should have conte
xtual awareness of the document files and also able to write to it 
```
---

     
 
all -  [ How do I get more 'natural' answers while using RAG FOR QA? ](https://i.redd.it/koskaj5zq6wc1.png) , 2024-04-25-0910
```
I've been working on a project to answer a student's questions from a syllabus' content. I've been able to do the retrie
val part but as can be seen in the pic above, the answer is purely extractive. I've used Langchain to split the text int
o chunks and when it answers a question it includes unnecessary information (eg. Topic heading for the next text). How c
an I make these answers more natural?
```
---

     
 
all -  [ RAG with Google Cloud Services ](https://www.reddit.com/r/googlecloud/comments/1cayxo3/rag_with_google_cloud_services/) , 2024-04-25-0910
```
I am trying to build a RAG application using only Google Cloud Services.  


I am currently using Agent Builder's Data S
tores and GoogleVertexAISearchRetriever which is a LangChain retriever that can call said Data Stores.

I would like to 
build something more customizable for the ingestion part.

What would be the best option for a vector database? Alloydb?
  
I would not mind using an open source database such as Chroma, as long as it lives inside Google Cloud's infrastructu
re and as long as I am charged only through Google. 
```
---

     
 
all -  [ How to Summarize Large Documents with LangChain and OpenAI ](https://thenewstack.io/how-to-summarize-large-documents-with-langchain-and-openai/) , 2024-04-25-0910
```

```
---

     
 
all -  [ Not able to get all the content from the URL by using UnstructuredURLLoader ](https://www.reddit.com/r/LangChain/comments/1caxvfh/not_able_to_get_all_the_content_from_the_url_by/) , 2024-04-25-0910
```
I am trying to fetch URLs using below code but not getting whole content extracted from it, and I am getting :

**\[Docu
ment(page\_content='Enable JavaScript and cookies to continue', metadata={'source': 'https://medium.com/@woyera/how-to-c
hat-with-microsoft-word-documents-using-llama-2-b30faa053284'})\]**

Below is my code:

    loader = UnstructuredURLLoad
er(urls=all_urls)
    urlDocument = loader.load()
```
---

     
 
all -  [ How to aproach this - APi call then email send ](https://www.reddit.com/r/LangChain/comments/1caxhtq/how_to_aproach_this_api_call_then_email_send/) , 2024-04-25-0910
```
 Hello, I would greatly appreciate it if someone could give me a little help on how to approach this problem. I already 
have an API endpoint. My goal is to interact with the API endpoint using Langchain. If I tell the language model to send
 me the result via email, then it should do so; otherwise, it should not send anything, what can i use to achieve the em
ail send intention? thank you for all the help.
```
---

     
 
MachineLearning -  [ [D] Self-optimizing deterministic LLM memory using dspy, neo4j and vector databases. Need your input ](https://www.reddit.com/r/MachineLearning/comments/1cakjaf/d_selfoptimizing_deterministic_llm_memory_using/) , 2024-04-25-0910
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

     
 
MachineLearning -  [ [D] How to get the source documents from the retrieved context for RAG?  ](https://www.reddit.com/r/MachineLearning/comments/1bvoc1t/d_how_to_get_the_source_documents_from_the/) , 2024-04-25-0910
```
I'm not using Lanchain but only making API calls to an LLM service provider. The retriever is connected to a vector DB, 
and I would like to know what the LLM refers to WITHIN that retrieved context whenever it provides an answer, similar to
 how return_source_documents works in Langchain.

I'm using AzureOpenAI. I couldn't find much in their docs that related
 to returning the source documents. Any help will be greatly appreciated!

```
---

     
 
MachineLearning -  [ [P] RAG pipeline to query the ML Engineering Open Book ](https://www.reddit.com/r/MachineLearning/comments/1bu4wyx/p_rag_pipeline_to_query_the_ml_engineering_open/) , 2024-04-25-0910
```
I built a quick RAG implementation using Langchain to make it easy to query the [ML Engineering Open Book](https://githu
b.com/stas00/ml-engineering) by [Stas Bekman](https://twitter.com/StasBekman). The Multi-Vector retriever gave pretty go
od results and was quite easy to set up too. 

Github link - [https://github.com/shreyansh26/RAG-ML-Engg-Open-Book](http
s://github.com/shreyansh26/RAG-ML-Engg-Open-Book)

Hope this is useful for folks!
```
---

     
 
MachineLearning -  [ [Project] FinancialAdvisorGPT : LLM+RAG Boilerplate Project ](https://www.reddit.com/r/MachineLearning/comments/1btlpgd/project_financialadvisorgpt_llmrag_boilerplate/) , 2024-04-25-0910
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

     
 
MachineLearning -  [ [Project] Picachain, image search made simple. ](https://www.reddit.com/r/MachineLearning/comments/1bt7epv/project_picachain_image_search_made_simple/) , 2024-04-25-0910
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

     
 
deeplearning -  [ Seeking Advice: Solving Data Challenges with Large Language Models (LLMs) ](https://www.reddit.com/r/deeplearning/comments/1ca4nc1/seeking_advice_solving_data_challenges_with_large/) , 2024-04-25-0910
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

     
 
deeplearning -  [ Share the Coolest Out of The Box LLM Applications That Made You Say 'Wow that was smart' ](https://www.reddit.com/r/deeplearning/comments/1c9e6dj/share_the_coolest_out_of_the_box_llm_applications/) , 2024-04-25-0910
```
Hi, I'm looking at some LLM applications today but apart from guys doing big rags with langchain I don't see too many us
es that are out of the box or that make me say 'wow that was smart to use an LLM here'. Have you seen any cool stuff usi
ng LLMs recently that made you say 'wow, that was smart'?
```
---

     
