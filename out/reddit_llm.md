 
all -  [ [1 YoE, Data and Policy Analyst, Data Engineer or Data Scientist Policy, United States] ](https://www.reddit.com/r/resumes/comments/1emqxqk/1_yoe_data_and_policy_analyst_data_engineer_or/) , 2024-08-08-0911
```
Hi everyone! I am a rising 4th year and will be graduating UCLA in June 2025. I am looking for entry level positions tha
t are focused around Data Engineering, Data Science, or Data Analytics. I currently work in a Polciy lab so it would be 
a plus if a company is non profit based or does research into policy making. I am applying for all positions, remote and
 in person. I am willing to relocate anywhere in the U.S. My job hunting has been very rocky, I applied to many roles bu
t never seem to get passed the resume screening. And honestly, it could get a bit discouraging, and I fear that I might 
not get a job once I graduate. I really love working in a collaborative environment and small community teams, so I am a
lso very open to working in a startups around finance or tech. I have been editing my resume over the few weeks and this
 is where I am at. I would really appreciate any feedback! When making my resume, I really wanted to emphasize that I am
 responsible and take initiative when it comes to learning in the job, and also for me, my teammates always come first, 
rather than customers or clients. I also want these companies to hold that similar value, because having a strong team m
akes a good company culture. Also, I was born the U.S. so citizenship is not an issue 

https://preview.redd.it/s1279gb5
sbhd1.png?width=850&format=png&auto=webp&s=e546296a994a3caf65dddc709d79ba35df40db75
```
---

     
 
all -  [ Best free model for Chatbot, document analysis, text summarization  ](https://www.reddit.com/r/LargeLanguageModels/comments/1emqq3e/best_free_model_for_chatbot_document_analysis/) , 2024-08-08-0911
```
We have a Postgres database hosted on AWS where we have all our data. We would like to implement a chatbot that users ca
n use to answer questions about our data. 

Separately, we also have several documents (PDF, DOCX, CSV, TXT) that we wou
ld like to analyze and return certain important data elements from it. 

Also, summarize a 20 page document into a singl
e paragraph/page. And look at a record in our database and summarize it for users. 

We don’t need the model to know muc
h about stuff outside of our own database. Example: calculus, astronomy, medical stuff etc are super irrelevant but I wi
ll take it if it comes with it. I just don’t want to pay for a super rich LLM to do a fraction of things it can do. 

We
 were considering Llama 80b and langchain for this exercise, but the GPU on AWS for this is turning out to be quite pric
ey. 

Which free model and what kind of setup would you recommend for these use cases? If it helps, we would prefer esta
blished models that are implemented and maintained by reputable companies because of accuracy and reputation risk. 

 



```
---

     
 
all -  [ How to handle error with OpenAI ](https://www.reddit.com/r/AutoGenAI/comments/1empqh9/how_to_handle_error_with_openai/) , 2024-08-08-0911
```
Hello, I'm currently creating a groupchat, I'm only using the Assistant agent and an user proxy agent, the assistants ha
ve a conversation retrieval chain from langchain and using FAISS for the vector store

I'm using the turbo 3.5 model fro
m OpenAI

I'm having a very annoying error sometimes, haven't been able to replicate in any way, sometimes it only happe
ns once or twice but today it happened multiple times in less than an hour, different questions were sent, I can't seem 
to find a pattern at all

  
I would like to find why this is a happening, or if there is a way to handle this error so 
the chat can continue

right now I'm running it with a [panel](https://panel.holoviz.org/) interface

this is the error:


    2024-07-16 16:11:35,542 Task exception was never retrieved
    future: <Task finished name='Task-350' coro=<delaye
d_initiate_chat() done, defined at /Users/<user>/Documents/<app>/<app>_bot/chat_interface.py:90> exception=InternalServe
rError('Error code: 500 - {'error': {'message': 'The model produced invalid content. Consider modifying your prompt if y
ou are seeing this error persistently.', 'type': 'model_error', 'param': None, 'code': None}}')>
    Traceback (most rec
ent call last):
      File '/Users/<user>/Documents/<app>/<app>_bot/chat_interface.py', line 94, in delayed_initiate_cha
t
        await agent.a_initiate_chat(recipient, message=message)
      File '/Users/<user>/Documents/<app>/<app>_bot/en
v/lib/python3.12/site-packages/autogen/agentchat/conversable_agent.py', line 1084, in a_initiate_chat
        await self
.a_send(msg2send, recipient, silent=silent)
      File '/Users/<user>/Documents/<app>/<app>_bot/env/lib/python3.12/site-
packages/autogen/agentchat/conversable_agent.py', line 705, in a_send
        await recipient.a_receive(message, self, r
equest_reply, silent)
      File '/Users/<user>/Documents/<app>/<app>_bot/env/lib/python3.12/site-packages/autogen/agent
chat/conversable_agent.py', line 855, in a_receive
        reply = await self.a_generate_reply(sender=sender)
          
      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File '/Users/<user>/Documents/<app>/<app>_bot/env/lib/python3.12/
site-packages/autogen/agentchat/conversable_agent.py', line 2042, in a_generate_reply
        final, reply = await reply
_func(
                       ^^^^^^^^^^^^^^^^^
      File '/Users/<user>/Documents/<app>/<app>_bot/env/lib/python3.12/s
ite-packages/autogen/agentchat/groupchat.py', line 1133, in a_run_chat
        reply = await speaker.a_generate_reply(se
nder=self)
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File '/Users/<user>/Documents/<app>/<app>_b
ot/env/lib/python3.12/site-packages/autogen/agentchat/conversable_agent.py', line 2042, in a_generate_reply
        fina
l, reply = await reply_func(
                       ^^^^^^^^^^^^^^^^^
      File '/Users/<user>/Documents/<app>/<app>_bo
t/env/lib/python3.12/site-packages/autogen/agentchat/conversable_agent.py', line 1400, in a_generate_oai_reply
        r
eturn await asyncio.get_event_loop().run_in_executor(
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
   
   File '/opt/homebrew/Cellar/python@3.12/3.12.4/Frameworks/Python.framework/Versions/3.12/lib/python3.12/concurrent/fut
ures/thread.py', line 58, in run
        result = self.fn(*self.args, **self.kwargs)
                 ^^^^^^^^^^^^^^^^^^
^^^^^^^^^^^^^^^^
      File '/Users/<user>/Documents/<app>/<app>_bot/env/lib/python3.12/site-packages/autogen/agentchat/
conversable_agent.py', line 1398, in _generate_oai_reply
        return self.generate_oai_reply(*args, **kwargs)
       
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File '/Users/<user>/Documents/<app>/<app>_bot/env/lib/python3.12/
site-packages/autogen/agentchat/conversable_agent.py', line 1340, in generate_oai_reply
        extracted_response = sel
f._generate_oai_reply_from_client(
                             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File '/Users
/<user>/Documents/<app>/<app>_bot/env/lib/python3.12/site-packages/autogen/agentchat/conversable_agent.py', line 1359, i
n _generate_oai_reply_from_client
        response = llm_client.create(
                   ^^^^^^^^^^^^^^^^^^
      File
 '/Users/<user>/Documents/<app>/<app>_bot/env/lib/python3.12/site-packages/autogen/oai/client.py', line 722, in create
 
       response = client.create(params)
                   ^^^^^^^^^^^^^^^^^^^^^
      File '/Users/<user>/Documents/<ap
p>/<app>_bot/env/lib/python3.12/site-packages/autogen/oai/client.py', line 320, in create
        response = completions
.create(**params)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File '/Users/<user>/Documents/<app>/<app>_bot/en
v/lib/python3.12/site-packages/openai/_utils/_utils.py', line 277, in wrapper
        return func(*args, **kwargs)
     
          ^^^^^^^^^^^^^^^^^^^^^
      File '/Users/<user>/Documents/<app>/<app>_bot/env/lib/python3.12/site-packages/ope
nai/resources/chat/completions.py', line 643, in create
        return self._post(
               ^^^^^^^^^^^
      File
 '/Users/<user>/Documents/<app>/<app>_bot/env/lib/python3.12/site-packages/openai/_base_client.py', line 1266, in post
 
       return cast(ResponseT, self.request(cast_to, opts, stream=stream, stream_cls=stream_cls))
                       
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File '/Users/<user>/Documents/<app>/<app
>_bot/env/lib/python3.12/site-packages/openai/_base_client.py', line 942, in request
        return self._request(
     
          ^^^^^^^^^^^^^^
      File '/Users/<user>/Documents/<app>/<app>_bot/env/lib/python3.12/site-packages/openai/_ba
se_client.py', line 1031, in _request
        return self._retry_request(
               ^^^^^^^^^^^^^^^^^^^^
      File
 '/Users/<user>/Documents/<app>/<app>_bot/env/lib/python3.12/site-packages/openai/_base_client.py', line 1079, in _retry
_request
        return self._request(
               ^^^^^^^^^^^^^^
      File '/Users/<user>/Documents/<app>/<app>_bot
/env/lib/python3.12/site-packages/openai/_base_client.py', line 1031, in _request
        return self._retry_request(
  
             ^^^^^^^^^^^^^^^^^^^^
      File '/Users/<user>/Documents/<app>/<app>_bot/env/lib/python3.12/site-packages/o
penai/_base_client.py', line 1079, in _retry_request
        return self._request(
               ^^^^^^^^^^^^^^
      F
ile '/Users/<user>/Documents/<app>/<app>_bot/env/lib/python3.12/site-packages/openai/_base_client.py', line 1046, in _re
quest
        raise self._make_status_error_from_response(err.response) from None
    openai.InternalServerError: Error 
code: 500 - {'error': {'message': 'The model produced invalid content. Consider modifying your prompt if you are seeing 
this error persistently.', 'type': 'model_error', 'param': None, 'code': None}}
```
---

     
 
all -  [ New Grad, roast my resume on ease of readability, updates, downgrades…  #hiringhustle . ](https://i.redd.it/fokajxnpkbhd1.jpeg) , 2024-08-08-0911
```

```
---

     
 
all -  [ Local Langchain LLaVa 1.5 VQA Agent ](https://www.reddit.com/r/LocalLLaMA/comments/1empdfy/local_langchain_llava_15_vqa_agent/) , 2024-08-08-0911
```
Has anyone attempted a local langchain VQA Agent using LLaVa 1.5? I've been struggling along to get this thing working a
nd any insight/tutorials you may have referenced would be uuuugggeeee help.
```
---

     
 
all -  [ Where can I get my code reviewed? ](https://www.reddit.com/r/LangChain/comments/1emiqo5/where_can_i_get_my_code_reviewed/) , 2024-08-08-0911
```
Hello,

  
I've developed a script using Langchain and Agents that I plan to launch internally within our company. Befor
e moving it to production, I'd appreciate a second pair of eyes to review the code for any potential redundancies or are
as for improvement.

I’ve noticed that some posts sharing code here don’t always get much traction. I didn’t see any rul
es against sharing code for review, but I wanted to check if it's appropriate to ask for feedback here. 

If not, could 
you suggest any other platforms where I might get my code reviewed?

  
Thanks in advance.
```
---

     
 
all -  [ [Discussion] LLM use cases ](https://www.reddit.com/r/LangChain/comments/1emgi8p/discussion_llm_use_cases/) , 2024-08-08-0911
```
Other than chatbot what are the other use cases the LLM or open source hugging face models are used for? 
```
---

     
 
all -  [ How can I help you build more reliable AI products faster? ](https://www.reddit.com/r/LangChain/comments/1emfs9w/how_can_i_help_you_build_more_reliable_ai/) , 2024-08-08-0911
```
Hey everybody,

I've been really frustrated with the developer experience of Langchain in Typescript, particularly aroun
d structured extraction from image and text and agent workflows. I have started building out a dev toolkit to solve that
 with some DX inspiration from dev tools like vercel and prisma: [https://github.com/forge-ml/forge-ml](https://github.c
om/forge-ml/forge-ml).

I'd love feedback on the current product, but I'd also love to know what else I can incorporate 
- what are the big pain points people are having? 

Some of the current things on the roadmap are, in no particular orde
r:  
- structured extraction from video  
- structured extraction from audio  
- Anthropic/Groq support  
- Semantic Sea
rch over Documents  
- Semantic Search over Databases  
- Fine tuning  
- Workflows  
- Model routing

What are the bigg
est issues that you're facing when building AI products?
```
---

     
 
all -  [ How To Build Your Retrieval Augmented Generation (RAG) Using Open-source Tools: LangChain, LLAMA 3,  ](https://www.reddit.com/r/deeplearning/comments/1emdotx/how_to_build_your_retrieval_augmented_generation/) , 2024-08-08-0911
```


TL;DR: RAG overcomes the limitations of LLMs by bringing in external sources of information as relevant context.  
  

At the end of the step-by-step tutorial, you will be able to give your favorite LLM (ChatGPT, LLAMA 3, Mixtral, Gemini, 
Claude, etc.) some documents, ask it a question and see it respond based on relevant context.  
  
This will be running 
locally, using open-source libraries. Zero API and tooling costs.

[Step-by-step Notebook with zero-cost RAG](https://co
decompass00.substack.com/p/build-open-source-rag-langchain-llm-llama-chroma)

*Processing img 69v6kjfj3wgd1...*


```
---

     
 
all -  [ Specialized Web Search  ](https://www.reddit.com/r/LangChain/comments/1emdose/specialized_web_search/) , 2024-08-08-0911
```
Hi Folks, I am really new here. I am working on a multi-agent project where each agent would look up information on a se
t of select predefined websites. I am hoping to use web search to do it. Is there a way for me search articles related t
o a specific topic on a specific website using web search?
```
---

     
 
all -  [ using retrieval_chain as a tool for an agent ](https://www.reddit.com/r/LangChain/comments/1emd7m3/using_retrieval_chain_as_a_tool_for_an_agent/) , 2024-08-08-0911
```
i've developped a rag application using langchain with the retrieval chain that combines history retriever and documents
 chain, and it performs pretty good .   
i have been tasked to add summarization and some other tools , so i tought abou
t using agent and adding tools for such tasks and still use the rag chain as a tool .   
  
**Is there a way to use the 
same rag chain as a tool for the agent ?** 
```
---

     
 
all -  [ Advice on where to host LangChain.js REST API function for Q&A chatbot for my docs ](https://www.reddit.com/r/LangChain/comments/1em997z/advice_on_where_to_host_langchainjs_rest_api/) , 2024-08-08-0911
```
I need to build a simple chatbot for my documentation pages. I need advice on where to host it, currently I adjusted it 
for Supabase edge function and Supabase vector store because it's free and deployed all over the world, but if I exceed 
the requests limit, I will have to self-host Supabase and then it's just one location.

Does anyone already have chatbot
s for small documentations and can you share which vector store you use and where you deployed your code? my docs pages 
are served from AWS S3. If I use AWS lambda to host the edge function, I'm afraid of a cost increase if there will be ma
ny requests.
```
---

     
 
all -  [ How to return langfuse trace_id when using Langserve stream? ](https://www.reddit.com/r/LangChain/comments/1em7aik/how_to_return_langfuse_trace_id_when_using/) , 2024-08-08-0911
```
I have very simple code **Langserve** with **langfuse\_handler**.

    add_routes(app, normal_agent.with_config(Runnable
Config(callbacks=[langfuse_handler])),
               per_req_config_modifier=per_request_config_modifier, path='/normal
')

When I run my code: 

    import asyncio
    
    from langserve import RemoteRunnable
    
    remote_runnable = Re
moteRunnable('http://localhost:8001/normal')
    
    
    async def main():
        async for chunk in remote_runnable.
astream({'input': 'tell me about ronaldo'}):
    
            print(chunk, end='|\n', flush=True)
    
    asyncio.run(m
ain())

I want return to client my trace\_id of Langfuse. Do you have any ideas to do that? I stuck here for 2 days. 
```
---

     
 
all -  [ Rate my resume (for entry level Backend/ AI Positions) ](https://www.reddit.com/r/developersIndia/comments/1em5sgu/rate_my_resume_for_entry_level_backend_ai/) , 2024-08-08-0911
```
https://preview.redd.it/rjvssx8a37hd1.png?width=661&format=png&auto=webp&s=b8bd0d1a4720c4cd39afa6ca21a9797d4dd37680

Sin
ce the last time I posted my resume, I have made many tweaks as suggested by a helpful person in the comments... I think
 it has improved a lot can you rate this resume?   
any tips for cold emailing and applying to jobs is welcome because I
 am having 0 call-backs or responses to my applications.
```
---

     
 
all -  [ Support with Langchain.js for free inference ](https://www.reddit.com/r/LangChain/comments/1em3muc/support_with_langchainjs_for_free_inference/) , 2024-08-08-0911
```
I am fairly new to Langchain and wanted to seek out some advice for free methods of using LLMs to just do some basic pro
mpting for a web application. The prompting is just providing some music artists and asking the LLM to think of potentia
l ideas for those artists. I have a node.js backend that I am attempting to integrate Langchain.js into. 

I first wante
d to ask are there any decent models for my task that can be used with Langchain.js for free and what would a very basic
 code snippet look like to run it. 

  
In addition, I wanted to ask if Ollama is applicable here or is that strictly fo
r local applications?

  
Thanks !

  
  

```
---

     
 
all -  [ RAG and KNOWLEDGE GRAPH ](https://www.reddit.com/r/LangChain/comments/1em3b9p/rag_and_knowledge_graph/) , 2024-08-08-0911
```
hi there i am learning about rag with knowledge graph any proper documentation from where i can get the reference any th
ing would be helpful 
```
---

     
 
all -  [ Chromadb issues ](https://www.reddit.com/r/LangChain/comments/1ely226/chromadb_issues/) , 2024-08-08-0911
```
Has anyone come across an issue with chroma as a vector store where it can’t handle a large K unless it’s “warmed up”?


Have a db with about 30k docs in it each about a paragraph long. I need to return the top 100 or so as part of a larger 
ranking process. When I first load the db though if I don’t start with a k size of 5 and work my way up it consistently 
errors out with “cannot return the results in a contiguous 2d array. Probably ef or M is too small”. I’ve tried changing
 the hnsw parameters when creating the collection but nothing seems to give. 
```
---

     
 
all -  [ Seeking help with creating CLI for 'non-programmers' (LLMs) ](https://www.reddit.com/r/ArtificialInteligence/comments/1elrl0l/seeking_help_with_creating_cli_for_nonprogrammers/) , 2024-08-08-0911
```
***TL;DR*** What is the best way to convert user input into sequence of commands and their corresponding parameters? Lik
e, imagine you are not a programmer and there is a console app with a CLI, but, well, you don't know the structure and t
he syntax of commands. And you don't want to know. YBut! You have a locally running instance of llama3.1 -- or whatever 
open LLM is out there now -- and you can ask it to create a CLI command for you. What would you do to accomplish that?


**Intro**

A little bit of context. I'm working on a project that targets scientists as end users. It has some UI using 
which it's possible to do all sort of things the lab workers would like to do. But recently the projects product owner d
ecided that it would be cool to have a small chat window that is accessable basically everywhere throughout the applicat
ion UI in which 'lives' a bot that can accept some input from a user and do what is requested. The pool of commands is f
inite and predefined.

**The issue**

So, putting details aside, the main issue to be solved is parsing user input (unst
ructured and possible incomplete data) to some structured form. In general, each and every user input should be transfor
med into a data structure that represents a sequence of commands with their parameters, for example:

User input: Please
, create X with param1 set to value1 and param2 equal to value2

Desired output:

    create_x --param1 value1 --param2 
value2

In this example, there is only one command, but in real life the request can represent a sequence of N commands,
 and they may depend on each other (sequence of execution does matter)

**What I've tried so far**

I have an 'experimen
t' environment: a python project with `ollama` and `langchain` installed. The main model I test is llama3.1-instruct wit
h 5bit quantization. (I'm sort of limited with hardware resourses, so XXB parameter models do not fit).

Up until now, I
've tried to achieve what I want with prompting in different forms, but in general I do the following:

As the very firs
t message in the chat, I create a 'system' one which explain what commands are there. The format is the following (I rep
laced original data not to expose the context more, so it's very generic)

    <scope>
        <models>
            <mod
el name='entityA'>
                <field name='uniqueId' type='string' description='unique identifier for entityA'/>
  
              <field name='label' type='string' description='label for entityA'/>
                <field name='category'
 type='enum' possible-value='alpha, beta, gamma, delta'/>
            </model>
            <model name='entityB'>
      
          <field name='uniqueId' description='unique identifier for entityB'/>
                <field name='entityAIds' 
type='array' description='identifiers of entityAs associated with this entityB'/>
            </model>
        </models>

        <commands>
            <command name='create_entityA' description='creates an instance of entityA'>
           
     <param name='uniqueId' type='string' description='unique identifier for entityA'/>
                <param name='lab
el' type='string' description='label for entityA' required='true'/>
                <param name='category' type='enum' p
ossible-values='alpha, beta, gamma, delta'
                       description='category of entityA (one value from the p
ossible values list)' required='true'/>
            </command>
            <command name='remove_entityA' description='r
emoves an instance of entityA by its unique identifier'>
                <param name='uniqueId' description='unique iden
tifier of the entityA to be removed'
                       required='true'/>
            </command>
            <comman
d name='create_entityB'>
                <param name='label' description='label for entityB'/>
            </command>
  
          <command name='link_entityAs_to_entityB'
                     description='associates instances of entityA wit
h a specific entityB based on the provided unique identifier of entityB'>
                <param name='uniqueId' descrip
tion='unique identifier of the entityB to which entityAs should be associated'
                       required='true'/>

                <param name='entityAIds'
                       description='an array of unique identifiers of entityAs 
to associate with the entityB'
                       type='array'
                       required='true'/>
            
</command>
            <command name='navigate' description='indicates that a user wants to go to a specific section of 
the platform'>
                <param name='section' possible-values='entitiesA, entitiesB, configuration' required='tru
e'/>
            </command>
            <command name='support' description='should be executed when a user seeks assist
ance on available functions'/>
        </commands>
    </scope>

So, now the model is provided with some context. Then, 
also in the 'system' message I:

* 'tell' the model that user input should be converted into a sequence of commands alon
g with the corresponding parameters, all of this is described in the XML above
* describe the desired output format
* tr
y to enforce some restriction and cover edge cases

**The question part**

*Is this approach* ***viable***\*?\*

If yes,
 maybe there are some ***ways to improve it***?

If not, *what would be* ***the alternative***?

So far I don't see how 
to apply fine tuning here

Thank you in advance!
```
---

     
 
all -  [ Need help with creating CLI for 'non-programmers' (LLMs) ](https://www.reddit.com/r/deeplearning/comments/1elrfgm/need_help_with_creating_cli_for_nonprogrammers/) , 2024-08-08-0911
```
***TL;DR*** What is the best way to convert user input into sequence of commands and their corresponding parameters? Lik
e, imagine you are not a programmer and there is a console app with a CLI, but, well, you don't know the structure and t
he syntax of commands. And you don't want to know. YBut! You have a locally running instance of llama3.1 -- or whatever 
open LLM is out there now -- and you can ask it to create a CLI command for you. What would you do to accomplish that?


**Intro**

A little bit of context. I'm working on a project that targets scientists as end users. It has some UI using 
which it's possible to do all sort of things the lab workers would like to do. But recently the projects product owner d
ecided that it would be cool to have a small chat window that is accessable basically everywhere throughout the applicat
ion UI in which 'lives' a bot that can accept some input from a user and do what is requested. The pool of commands is f
inite and predefined.

**The issue**

So, putting details aside, the main issue to be solved is parsing user input (unst
ructured and possible incomplete data) to some structured form. In general, each and every user input should be transfor
med into a data structure that represents a sequence of commands with their parameters, for example:

User input: Please
, create X with param1 set to value1 and param2 equal to value2

Desired output:

    create_x --param1 value1 --param2 
value2

In this example, there is only one command, but in real life the request can represent a sequence of N commands,
 and they may depend on each other (sequence of execution does matter)

**What I've tried so far**

I have an 'experimen
t' environment: a python project with `ollama` and `langchain` installed. The main model I test is llama3.1-instruct wit
h 5bit quantization. (I'm sort of limited with hardware resourses, so XXB parameter models do not fit).

Up until now, I
've tried to achieve what I want with prompting in different forms, but in general I do the following:

1. As the very f
irst message in the chat, I create a 'system' one which explain what commands are there. The format is the following (I 
replaced original data not to expose the context more, so it's very generic): 

```xml
<scope>
    <models>
        <mod
el name='entityA'>
            <field name='uniqueId' type='string' description='unique identifier for entityA'/>
      
      <field name='label' type='string' description='label for entityA'/>
            <field name='category' type='enum'
 possible-value='alpha, beta, gamma, delta'/>
        </model>
        <model name='entityB'>
            <field name='u
niqueId' description='unique identifier for entityB'/>
            <field name='entityAIds' type='array' description='id
entifiers of entityAs associated with this entityB'/>
        </model>
    </models>
    <commands>
        <command nam
e='create_entityA' description='creates an instance of entityA'>
            <param name='uniqueId' type='string' descri
ption='unique identifier for entityA'/>
            <param name='label' type='string' description='label for entityA' re
quired='true'/>
            <param name='category' type='enum' possible-values='alpha, beta, gamma, delta'
             
      description='category of entityA (one value from the possible values list)' required='true'/>
        </command>
 
       <command name='remove_entityA' description='removes an instance of entityA by its unique identifier'>
           
 <param name='uniqueId' description='unique identifier of the entityA to be removed'
                   required='true'/
>
        </command>
        <command name='create_entityB'>
            <param name='label' description='label for enti
tyB'/>
        </command>
        <command name='link_entityAs_to_entityB'
                 description='associates inst
ances of entityA with a specific entityB based on the provided unique identifier of entityB'>
            <param name='u
niqueId' description='unique identifier of the entityB to which entityAs should be associated'
                   requir
ed='true'/>
            <param name='entityAIds'
                   description='an array of unique identifiers of entit
yAs to associate with the entityB'
                   type='array'
                   required='true'/>
        </comman
d>
        <command name='navigate' description='indicates that a user wants to go to a specific section of the platform
'>
            <param name='section' possible-values='entitiesA, entitiesB, configuration' required='true'/>
        </c
ommand>
        <command name='support' description='should be executed when a user seeks assistance on available functi
ons'/>
    </commands>
</scope>
```

So, now the model is provided with some context. Then, also in the 'system' message
 I:

* 'tell' the model that user input should be converted into a sequence of commands along with the corresponding par
ameters, all of this is described in the XML above
* describe the desired output format
* try to enforce some restrictio
n and cover edge cases

**The question part**

*Is this approach* ***viable***\*?\*

If yes, maybe there are some ***way
s to improve it***?

If not, *what would be* ***the alternative***?

So far I don't see how to apply fine tuning here

T
hank you in advance!
```
---

     
 
all -  [ Need help with CLI for 'non-programmers' (LLMs, but maybe it's a wrong choice) ](https://www.reddit.com/r/neuralnetworks/comments/1elre7x/need_help_with_cli_for_nonprogrammers_llms_but/) , 2024-08-08-0911
```
***TL;DR*** What is the best way to convert user input into sequence of commands and their corresponding parameters? Lik
e, imagine you are not a programmer and there is a console app with a CLI, but, well, you don't know the structure and t
he syntax of commands. And you don't want to know. YBut! You have a locally running instance of llama3.1 -- or whatever 
open LLM is out there now -- and you can ask it to create a CLI command for you. What would you do to accomplish that?


**Intro**

A little bit of context. I'm working on a project that targets scientists as end users. It has some UI using 
which it's possible to do all sort of things the lab workers would like to do. But recently the projects product owner d
ecided that it would be cool to have a small chat window that is accessable basically everywhere throughout the applicat
ion UI in which 'lives' a bot that can accept some input from a user and do what is requested. The pool of commands is f
inite and predefined.

**The issue**

So, putting details aside, the main issue to be solved is parsing user input (unst
ructured and possible incomplete data) to some structured form. In general, each and every user input should be transfor
med into a data structure that represents a sequence of commands with their parameters, for example:

User input: Please
, create X with param1 set to value1 and param2 equal to value2

Desired output:

    create_x --param1 value1 --param2 
value2

In this example, there is only one command, but in real life the request can represent a sequence of N commands,
 and they may depend on each other (sequence of execution does matter)

**What I've tried so far**

I have an 'experimen
t' environment: a python project with `ollama` and `langchain` installed. The main model I test is llama3.1-instruct wit
h 5bit quantization. (I'm sort of limited with hardware resourses, so XXB parameter models do not fit).

Up until now, I
've tried to achieve what I want with prompting in different forms, but in general I do the following:

As the very firs
t message in the chat, I create a 'system' one which explain what commands are there. The format is the following (I rep
laced original data not to expose the context more, so it's very generic): 

```xml
<scope>
    <models>
        <model 
name='entityA'>
            <field name='uniqueId' type='string' description='unique identifier for entityA'/>
         
   <field name='label' type='string' description='label for entityA'/>
            <field name='category' type='enum' po
ssible-value='alpha, beta, gamma, delta'/>
        </model>
        <model name='entityB'>
            <field name='uniq
ueId' description='unique identifier for entityB'/>
            <field name='entityAIds' type='array' description='ident
ifiers of entityAs associated with this entityB'/>
        </model>
    </models>
    <commands>
        <command name='
create_entityA' description='creates an instance of entityA'>
            <param name='uniqueId' type='string' descripti
on='unique identifier for entityA'/>
            <param name='label' type='string' description='label for entityA' requi
red='true'/>
            <param name='category' type='enum' possible-values='alpha, beta, gamma, delta'
                
   description='category of entityA (one value from the possible values list)' required='true'/>
        </command>
    
    <command name='remove_entityA' description='removes an instance of entityA by its unique identifier'>
            <p
aram name='uniqueId' description='unique identifier of the entityA to be removed'
                   required='true'/>
 
       </command>
        <command name='create_entityB'>
            <param name='label' description='label for entityB
'/>
        </command>
        <command name='link_entityAs_to_entityB'
                 description='associates instanc
es of entityA with a specific entityB based on the provided unique identifier of entityB'>
            <param name='uniq
ueId' description='unique identifier of the entityB to which entityAs should be associated'
                   required=
'true'/>
            <param name='entityAIds'
                   description='an array of unique identifiers of entityAs
 to associate with the entityB'
                   type='array'
                   required='true'/>
        </command>

        <command name='navigate' description='indicates that a user wants to go to a specific section of the platform'>

            <param name='section' possible-values='entitiesA, entitiesB, configuration' required='true'/>
        </comm
and>
        <command name='support' description='should be executed when a user seeks assistance on available functions
'/>
    </commands>
</scope>

```

So, now the model is provided with some context. Then, also in the 'system' message I
:

* 'tell' the model that user input should be converted into a sequence of commands along with the corresponding param
eters, all of this is described in the XML above
* describe the desired output format
* try to enforce some restriction 
and cover edge cases

**The question part**

*Is this approach* ***viable***\*?\*

If yes, maybe there are some ***ways 
to improve it***?

If not, *what would be* ***the alternative***?

So far I don't see how to apply fine tuning here

Tha
nk you in advance!
```
---

     
 
all -  [ Need help with CLI for 'non-programmers' ](https://www.reddit.com/r/LLMDevs/comments/1elrd9v/need_help_with_cli_for_nonprogrammers/) , 2024-08-08-0911
```
***TL;DR*** What is the best way to convert user input into sequence of commands and their corresponding parameters? Lik
e, imagine you are not a programmer and there is a console app with a CLI, but, well, you don't know the structure and t
he syntax of commands. And you don't want to know. YBut! You have a locally running instance of llama3.1 -- or whatever 
open LLM is out there now -- and you can ask it to create a CLI command for you. What would you do to accomplish that?


**Intro**

A little bit of context. I'm working on a project that targets scientists as end users. It has some UI using 
which it's possible to do all sort of things the lab workers would like to do. But recently the projects product owner d
ecided that it would be cool to have a small chat window that is accessable basically everywhere throughout the applicat
ion UI in which 'lives' a bot that can accept some input from a user and do what is requested. The pool of commands is f
inite and predefined.

**The issue**

So, putting details aside, the main issue to be solved is parsing user input (unst
ructured and possible incomplete data) to some structured form. In general, each and every user input should be transfor
med into a data structure that represents a sequence of commands with their parameters, for example:

User input: Please
, create X with param1 set to value1 and param2 equal to value2

Desired output:

    create_x --param1 value1 --param2 
value2

In this example, there is only one command, but in real life the request can represent a sequence of N commands,
 and they may depend on each other (sequence of execution does matter)

**What I've tried so far**

I have an 'experimen
t' environment: a python project with `ollama` and `langchain` installed. The main model I test is llama3.1-instruct wit
h 5bit quantization. (I'm sort of limited with hardware resourses, so XXB parameter models do not fit).

Up until now, I
've tried to achieve what I want with prompting in different forms, but in general I do the following:

As the very firs
t message in the chat, I create a 'system' one which explain what commands are there. The format is the following (I rep
laced original data not to expose the context more, so it's very generic)

```xml
<scope>
    <models>
        <model na
me='entityA'>
            <field name='uniqueId' type='string' description='unique identifier for entityA'/>
           
 <field name='label' type='string' description='label for entityA'/>
            <field name='category' type='enum' poss
ible-value='alpha, beta, gamma, delta'/>
        </model>
        <model name='entityB'>
            <field name='unique
Id' description='unique identifier for entityB'/>
            <field name='entityAIds' type='array' description='identif
iers of entityAs associated with this entityB'/>
        </model>
    </models>
    <commands>
        <command name='cr
eate_entityA' description='creates an instance of entityA'>
            <param name='uniqueId' type='string' description
='unique identifier for entityA'/>
            <param name='label' type='string' description='label for entityA' require
d='true'/>
            <param name='category' type='enum' possible-values='alpha, beta, gamma, delta'
                  
 description='category of entityA (one value from the possible values list)' required='true'/>
        </command>
      
  <command name='remove_entityA' description='removes an instance of entityA by its unique identifier'>
            <par
am name='uniqueId' description='unique identifier of the entityA to be removed'
                   required='true'/>
   
     </command>
        <command name='create_entityB'>
            <param name='label' description='label for entityB'/
>
        </command>
        <command name='link_entityAs_to_entityB'
                 description='associates instances
 of entityA with a specific entityB based on the provided unique identifier of entityB'>
            <param name='unique
Id' description='unique identifier of the entityB to which entityAs should be associated'
                   required='t
rue'/>
            <param name='entityAIds'
                   description='an array of unique identifiers of entityAs t
o associate with the entityB'
                   type='array'
                   required='true'/>
        </command>
  
      <command name='navigate' description='indicates that a user wants to go to a specific section of the platform'>
  
          <param name='section' possible-values='entitiesA, entitiesB, configuration' required='true'/>
        </comman
d>
        <command name='support' description='should be executed when a user seeks assistance on available functions'/
>
    </commands>
</scope>
```


So, now the model is provided with some context. Then, also in the 'system' message I:


* 'tell' the model that user input should be converted into a sequence of commands along with the corresponding paramet
ers, all of this is described in the XML above
* describe the desired output format
* try to enforce some restriction an
d cover edge cases

**The question part**

*Is this approach* ***viable***\*?\*

If yes, maybe there are some ***ways to
 improve it***?

If not, *what would be* ***the alternative***?

So far I don't see how to apply fine tuning here

Thank
 you in advance!
```
---

     
 
all -  [ What is the best document loader for PDFs? And other docs in general? ](https://www.reddit.com/r/LangChain/comments/1elr7sr/what_is_the_best_document_loader_for_pdfs_and/) , 2024-08-08-0911
```
Based on some advice I got, I started using AWS Textract ($$$) for PDFs and unstructured (local/free) for all other doc 
types such as docx and html. 

My textract bill is getting a bit out of hand and I was wondering if there are any better
 services out there that can interpret things like tables and stuff from PDFs and other docs well?

Quality is my number
 one concern but cost is also important.

Looking to replace textract but also wanted to check to see if unstructured is
 still considered the best for other doc types.
```
---

     
 
all -  [ ML Engineer (1 YOE) looking for an open opportunity  ](https://www.reddit.com/r/developersIndia/comments/1elpxbz/ml_engineer_1_yoe_looking_for_an_open_opportunity/) , 2024-08-08-0911
```
Hi folks. I am a Machine Learning Engineer looking for open opportunities in Bangalore. I have 1 year of experience in d
eveloping and deploying ML solutions convering basic ML fundamentals like regression models and data analysis to buildin
g RAG applications using vector DB and Langchain. I have worked in shaping ideas into POCs using Machine Learning and De
ep Learning. 

My tech stack includes Python, Jupyter Notebook, Sci-kit Learn, Langchain, Vector DB, fine-tuning LLMs fo
r specific use cases.

I am also experienced in developing & deploying the end to end LLM applications to AWS cloud. I a
m passionate about ML.

Any leads would be appreciated. 
Thank You 
```
---

     
 
all -  [ How to track number of LLM calls in a ReAct agent ](https://www.reddit.com/r/LangChain/comments/1elpms2/how_to_track_number_of_llm_calls_in_a_react_agent/) , 2024-08-08-0911
```
I'm working on a ReAct agent(created with langchain.agents.create\_react\_agent) and we are creating an evaluation and m
onitoring tool for it to analyze and understand agent behavior, performance, latency, bottlenecks, etc. We have already 
some metrics, but I'm looking for the best practices or recommended techniques to calculate:

* Number of LLM calls: giv
en the agent will do it's reasoning/acting cycle doing LLM calls internally we want to measure the number of calls.
* Du
ration per LLM call: we also want to measure the duration per call.

One of the goals is to understand where to focus wh
en doing improvements, for example: 

1. improving tools descriptions, inputs etc to reduce the number of LLM calls.
2. 
Performing model optimization and endpoint tuning to reduce latency per call.

**Note:** due to internal constraints we 
are not  using langsmith and preferably the solution should be independent of the model used(given we will evaluate diff
erent models and we want the metrics for all of them).

Any other suggested metrics are appreciated.

The question is: *
*what is the recommended way to achieve this?** (I have in mind thing like callbacks like the **on\_llm\_end** and addin
g a counter but not sure if this is the recommended way or maybe there is something out of the box).
```
---

     
 
all -  [ Sharing my project that was built on Langchain: An all-in-one AI that integrates the best foundation ](https://www.reddit.com/r/LangChain/comments/1ellpk9/sharing_my_project_that_was_built_on_langchain_an/) , 2024-08-08-0911
```
Hey everyone I want to share a Langchain-based project that I have been working on for the last few months — [JENOVA](ht
tps://www.jenova.ai/), an AI (similar to ChatGPT) that integrates the best foundation models and tools into one seamless
 experience.

**AI is advancing too fast for most people to follow.** New state-of-the-art models emerge constantly, eac
h with unique strengths and specialties. Currently:

* Claude 3.5 Sonnet is the best at reasoning, math, and coding.
* G
emini 1.5 Pro excels in business/financial analysis and language translations.
* Llama 3.1 405B is most performative in 
roleplaying and creativity.
* GPT-4o is most knowledgeable in areas such as art, entertainment, and travel.

This rapidl
y changing and fragmenting AI landscape is leading to the following problems for consumers:

* **Awareness Gap:** Most p
eople are unaware of the latest models and their specific strengths, and are often paying for AI (e.g. ChatGPT) that is 
suboptimal for their tasks.
* **Constant Switching:** Due to constant changes in SOTA models, consumers have to frequent
ly switch their preferred AI and subscription.
* **User Friction:** Switching AI results in significant user experience 
disruptions, such as losing chat histories or critical features such as web browsing.

JENOVA is built to solve this.

*
*When you ask JENOVA a question, it automatically routes your query to the model that can provide the optimal answer (bu
ilt on top of Langchain).** For example, if your first question is about coding, then Claude 3.5 Sonnet will respond. If
 your second question is about tourist spots in Tokyo, then GPT-4o will respond. All this happens seamlessly in the back
ground.

JENOVA's model ranking is continuously updated to incorporate the latest AI models and performance benchmarks, 
ensuring you are always using the best models for your specific needs.

In addition to the best AI models, JENOVA also p
rovides you with an expanding suite of the most useful tools, starting with:

* **Web browsing** for real-time informati
on (performs surprisingly well, nearly on par with Perplexity)
* **Multi-format document analysis** including PDF, Word,
 Excel, PowerPoint, and more
* **Image interpretation** for visual tasks

Your privacy is very important to us. Your con
versations and data are never used for training, either by us or by third-party AI providers.

Try it out at [**www.jeno
va.ai**](https://www.jenova.ai/)

**Update:** JENOVA might be running into some issues with web search/browsing right no
w due to very high demand.
```
---

     
 
all -  [ Retrieving all embeddings from an Azure Ai Search instance ](https://www.reddit.com/r/LangChain/comments/1elllb7/retrieving_all_embeddings_from_an_azure_ai_search/) , 2024-08-08-0911
```
Hi Guys,

I am working on an issue and can't seem to figure it out. I want to retrieve all the embeddings that are store
d in a Azure AI Search instance.

  
At this moment i'm trying it like this:

`# Create a SearchClient instance`

`endpo
int = SEARCH_ENDPOINT`  
`search_client = SearchClient(endpoint=endpoint, index_name=index_name, credential=AzureKeyCred
ential(api_key))`

`# Formulate a search request`  
`search_text = '*'`    
`select_fields = '*'` 

`# Execute the searc
h`  
`results = search_client.search(search_text, select=select_fields)`

`print(results)`

  
However, this return me t
he following:

{'content': 'RANDOM CONTENT',   
'metadata':   
'{'source': 'DOC SOURCE,  
 'page': 0,  
 'start\_index':
 4}',  
 'id': 'OTQ4MTUwOWYtNTFiNC00NTViLWE0MzQtNTJlYjQxZDJiMmI0',  
 '@search.score': 1.0, '@search.reranker\_score': N
one,   
'@search.highlights': None,  
'@search.captions': None}

  
However not the embeddings. Can anybody help me?
```
---

     
 
all -  [ Extracting insights from conversational transcripts ](https://www.reddit.com/r/LangChain/comments/1elldx1/extracting_insights_from_conversational/) , 2024-08-08-0911
```
I am trying to build an application that analyses all my transcripts and answer user question based on the context by pe
rforming similarity search. I am loading all my transcripts into vector database(in my case milvus) and storing them as 
embeddings, along with the metadata of the transcripts. I am using rag retrieval process to get the answer, but I didn't
 get the expected output on most cases. Any better way of doing this, any suggestions on choosing the appropriate embedd
ings and dimensions.
```
---

     
 
all -  [ II'll set up your SaaS (Landing page + Stripe, Supabase, Email/Google Auth, and Email Automation int ](https://www.reddit.com/r/SaaSIdeas/comments/1ellaxz/iill_set_up_your_saas_landing_page_stripe/) , 2024-08-08-0911
```
As the title says, if you have a SaaS idea and you are looking to make it real quick, I can help you get started. 🚀

You
’ll receive the full code of your new SaaS App. This includes:

* Landing page template that is easy to modify according
 to your needs.
* Integration with Stripe, Supabase, Email Authentication, Google Authentication, PostHog (super OP Anal
ytics platform for your website, if u haven't used this b4, why not??) 🔒📊
* If you’re building an AI application, I can 
set up a Flask backend with OpenAI and Langchain Integration.
* Tech Stack: React, Next.js, Tailwind, TS, Python, Flask 
💻

These integrations are a MUST when building your own SaaS application, and honestly, it takes so f\*\*\*ing long to s
et them up. So let me help you.

Just trying to gauge interest 🙂 DM me
```
---

     
 
all -  [ I'll set up your SaaS (Landing page + Stripe, Supabase, Email/Google Auth, and Email Automation inte ](https://www.reddit.com/r/SaaS/comments/1ell4v6/ill_set_up_your_saas_landing_page_stripe_supabase/) , 2024-08-08-0911
```
As the title says, if you have a SaaS idea and you are looking to make it real quick, I can help you get started. 🚀

You
’ll receive the full code of your new SaaS App. This includes:

• Landing page template that is easy to modify according
 to your needs. 

• Integration with Stripe, Supabase, Email Authentication, Google Authentication, PostHog (super OP An
alytics platform for your website, if u haven't used this b4, why not??) 🔒📊

• If you’re building an AI application, I c
an set up a Flask backend with OpenAI and Langchain Integration. 

• Tech Stack: React, Next.js, Tailwind, TS, Python, F
lask 💻

These integrations are a MUST when building your own SaaS application, and honestly, it takes so f\*\*\*ing long
 to set them up. So let me help you.

Just trying to gauge interest 🙂 DM me
```
---

     
 
all -  [ WeaviateHybridSearchRetriever with filters? ](https://www.reddit.com/r/LangChain/comments/1elk3g2/weaviatehybridsearchretriever_with_filters/) , 2024-08-08-0911
```
I am currently building a Q&A interface with Streamlit and Langchain. Our initial vector database was in Pinecone. We ha
ve documents about the same topic, but different industries. Pure embedding search is not optimal, as it will match the 
same concepts across industries. So, we build a simple selector option where users pick their industry, and then ask the
 question. In pinecone each industry had their own namespace, we then simply filter on this:

    vectorstore = Pinecone
VectorStore(index_name=index_name, embedding=embeddings, namespace=namespace)
    
    retriever = vectorstore.as_retrie
ver(search_type='similarity', search_kwargs={'k': 3})

Hybrid search with pinecone is not as convenient as with Weaviate
, and since we noticed beter performance with hybrid search we are switching to Weaviate. The downside is that filters a
re not so clear for the Weaviate retriever. 

    retriever = WeaviateHybridSearchRetriever(
            client=client,

            index_name=WEAVIATE_INDEX_NAME,
            text_key='page_content',
            k=5,
            alpha=0.75
,
            attributes=['file_name', 'industry],
            create_schema_if_missing=False,
        )

Our Langchain 
Chain looks similar to this ( [https://github.com/langchain-ai/langchain/blob/master/templates/hybrid-search-weaviate/hy
brid\_search\_weaviate/chain.py](https://github.com/langchain-ai/langchain/blob/master/templates/hybrid-search-weaviate/
hybrid_search_weaviate/chain.py) ):

    # RAG prompt
    template = '''Answer the question based only on the following 
context:
    {context}
    Question: {question}
    '''
    prompt = ChatPromptTemplate.from_template(template)
    
   
 # RAG
    model = ChatOpenAI()
    chain = (
        RunnableParallel({'context': retriever, 'question': RunnablePassth
rough()})
        | prompt
        | model
        | StrOutputParser()
    )

The docs do show this:

    retriever.invo
ke(
        'AI integration in society',
        where_filter={
            'path': ['author'],
            'operator': 
'Equal',
            'valueString': 'Prof. Jonathan K. Sterling',
        },
    )

[https://python.langchain.com/v0.2/d
ocs/integrations/retrievers/weaviate-hybrid/](https://python.langchain.com/v0.2/docs/integrations/retrievers/weaviate-hy
brid/)

Does anyone know how/where to add the `where_filter` parameter for Weaviate hybrid search in the Chain?

[](http
s://github.com/langchain-ai/langchain/blob/master/templates/hybrid-search-weaviate/hybrid_search_weaviate/chain.py)
```
---

     
 
all -  [ Help Desk RAG Documentation New Link? [LangGraph] ](https://www.reddit.com/r/LangChain/comments/1elilnx/help_desk_rag_documentation_new_link_langgraph/) , 2024-08-08-0911
```
I've been keeping my eye on the LangGraph documentation, there was one titled 'Help Desk RAG' or 'Make a Help Desk Agent
 with RAG' or something. This was back when the documentation also showed a 'Design Patterns' category for the graphs.




I'm finally ready to start the tutorial but it has all but vanished. I only see about 6 other RAG based links. All of 
which are long, and with names that don't really indicate the differences. (Corrective RAG, Self-RAG, Agentic RAG...)

 
 
I may end up spending the time diving into them all eventually, but would anyone know which one specifically used to b
e the 'Help Desk RAG'?
```
---

     
 
all -  [ Multimodal AI Assistant Integrated with WhatsApp ](https://www.reddit.com/r/betatests/comments/1elibnc/multimodal_ai_assistant_integrated_with_whatsapp/) , 2024-08-08-0911
```
Hey fellow tech enthusiasts !

I made an AI assistant integrated with WhatsApp, using Langchain and a combination of fun
ctions and tools. Let me introduce to you, Simone !

My objective is to make AI seamlessly integrated to our daily life,
 including those that are not even interested in downloading the OpenAI, Claude or any other AI apps. That's why I've go
ne in favor of a WhatsApp integration, which allows for seamless incorporation into daily life.

Users can interact with
 Simone as they would with any contact, making AI assistance feel more natural and accessible. I realized that myself, a
 developer and tech-oriented user, find it very enjoyable.

Key Features:

* Multilingual support
* Voice message capabi
lity (text-to-speech and speech-to-text)
* Web search and content summarization
* Image analysis and generation
* Locati
on-based services (directions, place info)
* PDF and YouTube transcript reading

I'm particularly interested in hearing 
about:

* How the WhatsApp integration affects user experience: Is it a positive or negative point for you?
* The useful
ness of different features in day-to-day scenarios: What would you use it for?
* Performance, response time and hallucin
ations: If you tried it, did you like it?
* Privacy concerns and how we might address them: Would you feel comfortable d
iscussing any issues you may have with such a bot?
* Do you think it may be of any use for you or one of your friends?
*
 What features would make you consider using an AI assistant through WhatsApp?
* I want Simone to feel 'human-like' but 
I had mixed feedback on that side. What are your thoughts?

I'm after genuine opinions to help refine and improve Simone
. All feedback, positive or critical, is valuable.

For those of you that want to try it, just ask in comments and I'll 
share the link/WhatsApp number.

I spend several hours outside every day handing out flyers to people and asking for the
ir opinion. I hope it will be less painful through Reddit 😅

Thanks for your insights!

# How can I try it?

* Visit [Si
mone.app](http://Simone.app) to get more information
* OR Send a WhatsApp Message to +33 7 66 25 95 58

No registration 
needed.
```
---

     
 
all -  [ Run local LLM on CPU. how Bad would would it be compared to GPUs ](https://www.reddit.com/r/LangChain/comments/1eli67w/run_local_llm_on_cpu_how_bad_would_would_it_be/) , 2024-08-08-0911
```
I wanted to ask, if I want to run local LLMs only on CPU.

I do not have access to GPUs and wanted to ask how much slowe
r CPU would be, compared to GPU.

I would love to run a small Open Source LLM only on CPUs to read 500 pages PDFs and be
 able to ask it questions.


```
---

     
 
all -  [ LLM answer to the question  -  context for answer did not even provide ](https://www.reddit.com/r/LangChain/comments/1eli48o/llm_answer_to_the_question_context_for_answer_did/) , 2024-08-08-0911
```
My application logic is - i give some text from database, and using this context generated answer.But if i ask something
 but its dont exist in context - LLm still answer me. Why?.Here my code  

    const prompt = await pull<ChatPromptTempl
ate>('rlm/rag-prompt');
    
      const ragChain = await createStuffDocumentsChain({
        llm,
        prompt:prompt
,
        outputParser: parcer,
      });
      const stream = await ragChain.stream({
        question:question,
      
  context: [
          new Document({
            pageContent: text as string,
          }),
        ],
      });
    
```
---

     
 
all -  [ Beginner: Advice on Extremely Ambitious Agent-Based Long-Horizon Storytelling ](https://www.reddit.com/r/LangChain/comments/1eli34m/beginner_advice_on_extremely_ambitious_agentbased/) , 2024-08-08-0911
```
**Context:** I have an ambitious idea about using agents for long-horizon text-only storytelling but have limited techni
cal knowledge. I hope more experienced individuals can offer input on feasibility and potential challenges.

**Project O
verview:** My goal is to create very detailed, long form AI roleplaying software where users aren't just reading a novel
, they are the protagonist. In my experience, AI can produce passable prose (Claude 3.5), but it struggles with story pr
ogression and planning, often resulting in circular narratives. To address this, I plan to use agents to create a detail
ed plot outline based on a user-supplied premise. The AI will narrate, and the user will act as the protagonist. Every t
ime the protagonist acts, the AI will follow a series of escalating questions to assess and rewrite the outline as neede
d to keep the story cohesive:

1. Does this fit with the next planned beat? If yes, the writer AI continues; if not,
2. 
Does this fit with the scene? If yes, rewrite the beat; if not,
3. Does this fit with the chapter outline? If yes, rewri
te the scene and beat; if not,
4. Does this fit with the arc?

This way, the story always has an outline to stay on trac
k but can pivot as needed based on the protagonist's actions.

**Assumptions:**

1. Using a series of repeating agents, 
AI can generate and refine variations of a user-supplied premise into hyper-specific instructions. AI-written content of
ten lacks specificity, which I plan to address through careful prompting and QA agents.
2. I can break up the long horiz
on task of impromptu novel writing (AI roleplaying) into discrete chunks I can hand off to specific agents that will onl
y see their little section of the walled garden. This feels risky because different sections might need to know about ea
ch other to be cohesive and it could be hard to predict what that shared knowledge pool might need to be without making 
it so large the cost and wait time balloon beyond toleration.
3. That this won’t run afoul of the bitter lesson - where 
I have to get so granular I stray into deterministic logic which is inherently limiting and better solved with waiting f
or GPT-4.5.
4. I can get the response time from user input to the next beat written to a tolerable experience. I plan to
 make what I can run concurrently and use a bag of tricks to lessen the perceived waiting time.

The plot outline to kee
p things on track is table stakes for me. My real goal is far more ambitious (and far-fetched) about making the characte
rs come alive:

* Give all / many of the characters encountered their own AI which fully fleshes out their backstory, go
als, personality, outlook, relationships with other AI characters, and gives them agency to pursue those minor/major goa
ls as the book unfolds. The events other characters set in motion will be experienced by the protagonist whether it’s br
eaking and entering or being crabby in a conversation because they get hangry and it’s lunch time.
* Create true repercu
ssions for actions the protagonist or other characters take. If the protagonist as a student is rude, the AI controlling
 the teacher will assign detention, the unpleasantness determined by the AI of the teacher administering the detention 


I know a tiny amount of code (enough to hard code Towers of Hanoi in terminal) and with AI’s help, have Open Router hoo
ked up to a local python program in VS Code where it writes to a local document. I plan to create tons of little documen
ts the agents will write/read to. In my day job I work at a startup as a UX designer, have lots of  senior engineering F
AANG friends and have played extensively with AI, particularly with storytelling including programs like Sudowrite and N
ovelcrafter. 

I haven’t yet messed with agents. What do you predict will be the hardest parts of this project and what 
are the odds of success? I suspect the programming will be simple, the prompting will be finicky, the lag challenging an
d the cost fairly high even with GPT-4o mini. Even if I succeed, the output will probably be average until GPT-4.5 comes
 along.
```
---

     
 
all -  [ [0 YoE, Unemployed, Machine Learning Engineer/Data Analyst/Data Scientist, Europe] ](https://www.reddit.com/r/resumes/comments/1elh46a/0_yoe_unemployed_machine_learning_engineerdata/) , 2024-08-08-0911
```
It's my first resume and my only experience is the contracts and gigs I got from Upwork. Most of my experience is relate
d to ml eng./data analytics and I don't know what's wrong with my resume. Any help is  appreciated, thanks.

https://pre
view.redd.it/gdve8o26k1hd1.png?width=1656&format=png&auto=webp&s=e1088df17a4b2e432295dce907908c06e73c7d2a

  

```
---

     
 
all -  [ Intermittent Human Interaction Is Missing ](https://www.reddit.com/r/crewai/comments/1elf90o/intermittent_human_interaction_is_missing/) , 2024-08-08-0911
```
Crewai agents are able to gather feedbacks from human only once at the end. It's incompatible to handle langchain's huma
n input with the retrieval tools. Has anyone worked on this already?
```
---

     
 
all -  [ Internship oppurtunity for 2nd/3rd year students in LLM domain ](https://www.reddit.com/r/developersIndia/comments/1elf8pd/internship_oppurtunity_for_2nd3rd_year_students/) , 2024-08-08-0911
```
Hey guys
My company is in need for interns who can actively work in LLM and SLM based projects.
Tech stack required: Pyt
hon, Tensorflow, Langchain/Llamaindex
The candidate should able to use open source models and fine-tune them
Anyone inte
rested can put in their questions in the comment section or ping me. 

Location: Work From Home(If you are in Pune, you 
can come to the office as well)
Work experience: Fresher

*This is an unpaid internship hence perfect for students who a
re still studying*
```
---

     
 
MachineLearning -  [ [R] [D] Langchain Evaluation with BeyondLLM
 ](https://www.reddit.com/r/MachineLearning/comments/1eki1fv/r_d_langchain_evaluation_with_beyondllm/) , 2024-08-08-0911
```
Hey everyone! Just came across a new feature of Beyond LLM that can evaluate Langchain RAG pipelines! It provides contex
t relevancy, answer relevancy, and groundedness. Check out the code snippet I’m sharing—perfect for testing your RAG pip
elines! For more info, be sure to check it out on GitHub [here](https://github.com/aiplanethub/beyondllm/blob/main/cookb
ook/evaluate_langchain_rag_pipeline_beyondllm.ipynb).

https://preview.redd.it/172m1y3dvsgd1.png?width=3972&format=png&a
uto=webp&s=63d5b0f41f0e46a58e7a2d5fb0d2bbc4384b3b1d


```
---

     
 
MachineLearning -  [ [D] Embedding generation in production? How are you doing it? ](https://www.reddit.com/r/MachineLearning/comments/1e7xt6k/d_embedding_generation_in_production_how_are_you/) , 2024-08-08-0911
```


For those building production RAG pipelines, how are you generating embeddings. More than which model, I'm interested 
in how your deploying it. Are you calling the openai/vertex API endpoint directly? Using langchain/llamaindex wrappers? 
Using vectordb  classes? Or some other way?
```
---

     
 
MachineLearning -  [ [D] Is Anyone Else Setting Up Real-Time Django Workers for their AI Application? What's the best way ](https://www.reddit.com/r/MachineLearning/comments/1e0qens/d_is_anyone_else_setting_up_realtime_django/) , 2024-08-08-0911
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

     
 
MachineLearning -  [ [P] Real Time AI Workers Web Application ](https://www.reddit.com/r/MachineLearning/comments/1dzryk9/p_real_time_ai_workers_web_application/) , 2024-08-08-0911
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

     
