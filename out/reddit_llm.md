 
all -  [ Using LangChain agents to create a multi-agent platform that creates robot softwares ](https://www.reddit.com/r/LangChain/comments/1cmquwv/using_langchain_agents_to_create_a_multiagent/) , 2024-05-08-0909
```
When using LLMs for your generative AI needs, it's best to think of the LLM as a person rather than as a traditional AI 
engine. You can train and tune an LLM and give it memory to create an agent. The LLM-agent can act like a domain-expert 
for whatever domain you've trained and equipped it for. Using one agent to solve a complex problem is not the optimum so
lution. Much like how a project manager breaks a complex project into different tasks and assigns different individuals 
with different skills and trainings to manage each task, a multi-agent solution, where each agent has different capabili
ties and  trainings, can be applied to a complex problem.                                                    

In our ca
se, we want to automatically generate the entire robot software (for any given robot description) in ROS (Robot Operatin
g System);  In order to do so, first, we need to understand the overall design of the robot (a.k.a the ROS graph) and th
en for each ROS node we need to know if the LLM should generate the code, or if the LLM can fetch a suitable code from o
nline open-source repositories (a.k.a. RAG: Retrieval Augmented Generation). Each of these steps can be handled by diffe
rent agents which have different sets of tools at their disposal. The following figure shows how we are doing this:

[Ro
bot software generation using four collaborating agents each responsible for a different part of the problem, each equip
ped with different toolsets.](https://preview.redd.it/qcvb8y98c3zc1.png?width=1570&format=png&auto=webp&s=5f4072288e470f
d9e2d946e471f35e4c2dff1f94)

This is a free and open-source tool that we have released. We named it [ROScribe](https://g
ithub.com/RoboCoachTechnologies/ROScribe). Please checkout our [repository](https://github.com/RoboCoachTechnologies/ROS
cribe) for more information and give us a star if you like what you see. :) 
```
---

     
 
all -  [ Ingesting hundreds of csv files, loading them into a knowledge graph (RAG) then use LLM chatbot to q ](https://www.reddit.com/r/LangChain/comments/1cmpkyl/ingesting_hundreds_of_csv_files_loading_them_into/) , 2024-05-08-0909
```
I want to ingest hundreds of csv files, all the column data is   
different except for them sharing a similar column rel
ated to state. So I  
 am able to capture the location of the data observations and relate   
them to other data. The da
ta is mostly pertaining to demographics like   
economics, age, race, income, education, and health related outcomes. I 
  
need a general way to ingest all these csv files and load them into a   
knowledge graph, then use OpenAI to send a c
ypher query to the knowledge  
 graph to gain context of the user's question and then return an answer.  
 A question mi
ght be 'What is the highest mortality rate in the country   
and what might be causing this?' or 'Tell me counties with 
the lowest   
morbidity rates and why they might be lower than average'. I was   
thinking I could use vector embeddings
 as well for matching columns   
together and clustering the data. Im just wondering what the best way to  
 construct t
he graph will be so that the LLM can easily traverse it and   
get the correct information back to the user. What is the
 best way to   
set all this up? Does it make sense to construct a knowledge graph here   
so that LLM has context.  
  
  
Could use advice on how to set something up like this.  
    
Thanks  
  
  
    
  
  
  
  
```
---

     
 
all -  [ [1.5 YoE] Recent Master's Graduate in Computer Science Seeking Full-Time SDE or Data Science/ML role ](https://www.reddit.com/r/EngineeringResumes/comments/1cmp18k/15_yoe_recent_masters_graduate_in_computer/) , 2024-05-08-0909
```
So i have 1.5 years of experience as a full time software developer in .Net, C#, C++ techstack, I recently graduated fro
m masters in computer science , during my tenure as a student, i worked as a Graduate Student Assistant and my role chan
ged from Software developer in the first year to a data science role in the second year of my masters and so i keep chan
ging the first part of the experience section between Software developer and data science role and its part time job i.e
 the work at my university.

I have applied to over 1200 jobs and still didnt get any call backs. I am completely depres
sed and dont understand whats wrong with my resume. I need help

https://preview.redd.it/6yvelif313zc1.png?width=4961&fo
rmat=png&auto=webp&s=c6d6a4dfa54998b71521fb7c6d502051b2b0684d


```
---

     
 
all -  [ Langchain is legacy in Vercel AI SDK, how to still use Langchain in a stable and futureproof way? ](https://www.reddit.com/r/nextjs/comments/1cmkd6r/langchain_is_legacy_in_vercel_ai_sdk_how_to_still/) , 2024-05-08-0909
```
I just saw that Langchain is now a legacy provider. How can i still use Langchain with the Vercel AI SDK for my NextJS a
pps in a futureproof way. On the website it says, that the legacy providers are not recommended for new projects.
```
---

     
 
all -  [ Langtrace - Added support for Prompt Playground ](https://www.reddit.com/r/LangChain/comments/1cmk0dn/langtrace_added_support_for_prompt_playground/) , 2024-05-08-0909
```
Hey all,

  
We just added support for prompt playground. The goal of this feature is to help you test and iterate on yo
ur prompts from a single view across different combinations of models and model settings. 

- Support for OpenAI, Anthro
pic, Cohere and Groq

- Side by side comparison view.

- Comprehensive API settings tab to tweak and iterate on your pro
mpts with different combinations of settings and models. 

  
Please check it out and let me know if you have any feedba
ck.

[https://langtrace.ai/](https://langtrace.ai/)

[https://github.com/Scale3-Labs/langtrace](https://github.com/Scale
3-Labs/langtrace)

https://reddit.com/link/1cmk0dn/video/y0tve9hb02zc1/player

  

```
---

     
 
all -  [ Torn between Data Science and Game Dev ](https://www.reddit.com/r/gamedev/comments/1cmjfpe/torn_between_data_science_and_game_dev/) , 2024-05-08-0909
```
Im really torn between either pursuing game dev or Data Science (Modeling and Analysis). My interest in coding and devel
oping started with game dev a few years ago but I switched to DS when it came to my formal education. 

I have experienc
e in both fields and I'm fairly decent in both. However, my main motivation for going into DS was how brutal the game de
v industry was a few years ago (I was young and naiive, thought ds is better but it's really all the same). 

Another ke
y factor that I took into account is that my country isn't the best for either fields so I'm mostly tied to remote work 
and DS seemed the better option there.

Do you guys suggest I stick with Data Science (am diving into LangChain and gene
rative Ai rn as well) or slowly transition back to Game Dev?

P. S: I did look into combining my game dev experience wit
h ds expertise for Game related analyst work but again, remotely working in a position like that seems improbable. 
```
---

     
 
all -  [ Why Should We Keep an Eye Out for YC Batches?
 ](https://www.reddit.com/r/LangChain/comments/1cmiclo/why_should_we_keep_an_eye_out_for_yc_batches/) , 2024-05-08-0909
```
Just to clarify, if you want to be the first to know about trends in the startup world, you have to keep an eye on what'
s going on inside Y Combinator. This incubator has extensive experience with startups. You may know Stripe, Airbnb, Drop
box, Reddit, and Twitch among its alumni. And I'm sure YC won't slow down.

According to Garry Tan (President and CEO of
 YC), **the 260 companies** in the W24 cohort were selected from over **27,000** applications. The acceptance rate for s
tartups was less than **1%**! And AI was the biggest topic, with over **85 companies** calling themselves 'AI Startups' 
and over **180 mentioning** machine learning in their demos.
```
---

     
 
all -  [ Mastering LangChain and AWS: A Guide to Economic Analysis ($84.99 to FREE) ](https://www.jucktion.com/f/udemy-coupon/mastering-langchain-and-aws-a-guide-to-economic-analysis-$84-99-to-fre-328915/) , 2024-05-08-0909
```

```
---

     
 
all -  [ Python library to deploy LLM chat bots fast?
 ](https://www.reddit.com/r/LangChain/comments/1cmdxyi/python_library_to_deploy_llm_chat_bots_fast/) , 2024-05-08-0909
```
Here is a simple code snippet on how to use the Cycls chatbot library

    main.py
    from cycls import App
    
    ap
p = App(secret='sk-secret',
              handler='@handler-name')
    
    @app
    def entry_point(context):
        #
 Capture the received message
        received_message = context.message.content.text
        # Reply back with a simple
 message
        context.send.text(f'Received message: {received_message}')
    
    app.publish()

This is a simplified
 example but when you run [main.py](http://main.py), the chatbot immediately gets deployed with a public url and a chat 
interface. This has helped me a huge deal with testing while developing chatbots.   
Here are the docs: [https://docs.cy
cls.com/getting-started](https://docs.cycls.com/getting-started) [ ](https://docs.cycls.com/getting-started)
```
---

     
 
all -  [ Passing the output of function calling to RedisChatHistory in LCEL ](https://www.reddit.com/r/LangChain/comments/1cmdvls/passing_the_output_of_function_calling_to/) , 2024-05-08-0909
```
HI 

I have a RunnableWithMessageHistory and agent\_executor to create a chatbot agent with tools to fetch data from an 
API and then Redis to story chat history. 

I see that the RunnableWithMessageHistory is not recording the raw response 
of the function calling to the chat history. How do I solve for this?

I have been reading the API docs but couldn't fin
d anything. 
```
---

     
 
all -  [ ARC - A nimble framework for ai agent creation! ](https://www.reddit.com/r/Kotlin/comments/1cmdqfe/arc_a_nimble_framework_for_ai_agent_creation/) , 2024-05-08-0909
```
Hello r/Kotlin

I'm thrilled to introduce ARC, a new Kotlin framework for building AI Agents which takes the overhead of
f AI Agent creation. ARC is designed with simplicity and minimalism at its core.

It’s been a very tough journey braving
 so many questions from doubters on why not langchain or python etc.  u/Pat_Wlan has so many scars to show as he led thi
s module and is the core committer 🔥❤️🔥. This has been the result of our learnings from developing multi-agent systems t
hat are deployed in production at Deutsche Telekom.

**What sets ARC apart?**

* **Minimal Dependencies:** We've kept AR
C lean, ensuring that you only bring into your project what you truly need. No more bloat or extraneous libraries that h
og resources and complicate your builds!
* **Focused on Kotlin's Strengths:** ARC is built to maximize Kotlin's features
 such as DSL.
* **Interoperable by Design:** While ARC doesn't use langchain or springAI, it's designed to play well wit
h them. You're free to integrate AI functionalities or other libraries as you see fit, making ARC a flexible choice for 
a wide array of projects.
* **Community-Centered:** ARC is open-source and community-driven, with the aim of evolving th
rough your insights and contributions. We believe in the power of collective intelligence and are excited to see how the
 framework grows with your input.
* **Flexible** ARC is meant to be architecture agnostic. It doesn’t matter whether you
 are building microservices, a CLI or something else altogether.

We would like to get your feedback on this small endea
vor we took, braving so many questions internally on why not langchain or python etc .   
Would be great if you could ch
eck it out and help us make it 🚀🔥🚀.

Using the [arc-spring-init](https://github.com/lmos-ai/arc-spring-init) repository 
combined with your OpenAI-API Key you can create agents within seconds!

Project: [ARC](https://github.com/lmos-ai/arc),
 dive into the [docs](https://lmos-ai.github.io/arc/) 📖

We're looking forward to your valuable feedback.

Thanks ❤️!
```
---

     
 
all -  [ Langchain for Q&A + RAG? ](https://www.reddit.com/r/LocalLLaMA/comments/1cmafor/langchain_for_qa_rag/) , 2024-05-08-0909
```
I want to make a Q&A + RAG application.
Is langchain still a good choice?

I have never worked with it but it seems a bi
t bloated? And it seems to abstract a lot of details away such that it’s difficult to really understand what’s going on 
under the hood?

I could be completely wrong though. 

What’s your recommended stack for Q&A + RAG chatbot applications?


```
---

     
 
all -  [ Is llama2 multimodal? ](https://www.reddit.com/r/LangChain/comments/1cm9e3l/is_llama2_multimodal/) , 2024-05-08-0909
```
How can we pass images or base64 to llama2 and ask certain questions like describe this image??
```
---

     
 
all -  [ Combined Embeddings  ](https://www.reddit.com/r/LangChain/comments/1cm8oek/combined_embeddings/) , 2024-05-08-0909
```
I am developing my own Rag.
Using the text_splitter there is a performance tradeoff for the chunk size and chunk overlap
 parameters. Short chunks may not include all desired context, long chunks may hallucinate or cause info loss. Has anyon
e tried to embed twice the same document with multiple and different splitters? 
Are there noticeable advantages / disad
vantages?

```
---

     
 
all -  [ Yet Another RAG Tutorial ](https://www.reddit.com/r/webdev/comments/1cm7nuw/yet_another_rag_tutorial/) , 2024-05-08-0909
```
I was itching for a hands-on project, something I could build in just a few hours. So, I decided to experiment with Lang
Chain and vector databases to create a RAG conversation application.

Figured I'd share my experience with you. Check it
 out and lemme know what you think:

[https://genezio.com/blog/langchain-genezio-project](https://genezio.com/blog/langc
hain-genezio-project)
```
---

     
 
all -  [ Kernel crashing when using Langsmith Evaluation ](https://www.reddit.com/r/LangChain/comments/1cm7lbr/kernel_crashing_when_using_langsmith_evaluation/) , 2024-05-08-0909
```
Hello, could you assist me? I'm encountering difficulties with Langsmith's evaluation process. I'm able to evaluate my c
ontext using 'cont\_qa', but when I attempt to incorporate additional evaluators such as 'accuracy', my kernel crashes i
f there's more than one element in my dataset. Interestingly, when there's only one element, it works perfectly. I'm see
king guidance on how to address this issue. Below is the code I'm using

    import langsmith
    from langchain import 
chat_models, prompts, smith
    from langchain.schema import output_parser
    
    
    # Define your runnable or chain
 below.
    prompt = prompts.ChatPromptTemplate.from_messages(
      [
        ('system', 'You are a helpful AI assistan
t.'),
        ('human', '{question}')
      ]
    )
    
    
    # Define the evaluators to apply
    eval_config = smi
th.RunEvalConfig(
        evaluators=[
            'cot_qa',
            smith.RunEvalConfig.LabeledCriteria('harmfulnes
s'),
            smith.RunEvalConfig.LabeledCriteria('relevance'),
            smith.RunEvalConfig.LabeledCriteria('help
fulness')
        ],
        custom_evaluators=[],
        eval_llm=chat_models.ChatOpenAI(model='gpt-4', temperature=0)

    )
    
    client = langsmith.Client()
    chain_results = client.run_on_dataset(
        dataset_name=dataset_name
,
        llm_or_chain_factory=open_ai_rag,
        evaluation=eval_config,
        concurrency_level=5,
        verbose
=True,
    )
```
---

     
 
all -  [ Create a real world RAG chat app with Langchain LCEL ](https://www.reddit.com/r/LangChain/comments/1cm5ktx/create_a_real_world_rag_chat_app_with_langchain/) , 2024-05-08-0909
```
Hello everyone,

Just finished writing a post on how to create real world application using Langchain.  
I talk about :


* Langchain LCEL
* How to create composition of multiple chains.
* How to integrate user parameters like output type or
 specified vector store in chains.
* How to use configuration to change the prompt and the retriever at run time.

Check
 it out: [Link](https://www.metadocs.co/2024/05/07/create-a-complex-rag-chat-app-with-langchain-lcel/).

Thanks!
```
---

     
 
all -  [ Error Following Langchain/Vertex AI Reasoning Engine Docs ](https://www.reddit.com/r/LangChain/comments/1cm2lvb/error_following_langchainvertex_ai_reasoning/) , 2024-05-08-0909
```
Hello everyone, I'm trying to follow this example I found in the Vertex AI documentation.

[https://cloud.google.com/ver
tex-ai/generative-ai/docs/reasoning-engine/develop](https://cloud.google.com/vertex-ai/generative-ai/docs/reasoning-engi
ne/develop)

I'm following the steps carefully, but when I try:

    response = agent.query(

input='What is the exchang
e rate from US dollars to Swedish currency?' )

I receive the following error:

    {
    	'name': 'KeyError',
    	'mes
sage': ''agent'',
    	'stack': '---------------------------------------------------------------------------
    KeyErro
r                                  Traceback (most recent call last)
    Cell In[92], line 1
    ----> 1 response = agen
t.query(
          2     input=\'What is the exchange rate from US dollars to Swedish currency?\'
          3 )
    
   
 File /opt/homebrew/lib/python3.11/site-packages/vertexai/preview/reasoning_engines/templates/langchain.py:439, in Langc
hainAgent.query(self, input, config, **kwargs)
        437     input = {\'input\': input}
        438 if not self._runna
ble:
    --> 439     self.set_up()
        440 return langchain_load_dump.dumpd(
        441     self._runnable.invoke(i
nput=input, config=config, **kwargs)
        442 )
    
    File /opt/homebrew/lib/python3.11/site-packages/vertexai/pre
view/reasoning_engines/templates/langchain.py:400, in LangchainAgent.set_up(self)
        398     self._llm = self._llm.
bind(functions=self._tools)
        399 self._agent = self._prompt | self._llm | self._output_parser
    --> 400 self._a
gent_executor = AgentExecutor(
        401     agent=self._agent,
        402     tools=self._tools,
        403     **s
elf._agent_executor_kwargs,
        404 )
        405 runnable = self._agent_executor
        406 if has_history:
    
 
   File /opt/homebrew/lib/python3.11/site-packages/langchain/load/serializable.py:97, in Serializable.__init__(self, **k
wargs)
         96 def __init__(self, **kwargs: Any) -> None:
    ---> 97     super().__init__(**kwargs)
         98    
 self._lc_kwargs = kwargs
    
    File /opt/homebrew/lib/python3.11/site-packages/pydantic/v1/main.py:339, in BaseModel
.__init__(__pydantic_self__, **data)
        333 \'\'\'
        334 Create a new model by parsing and validating input d
ata from keyword arguments.
        335 
        336 Raises ValidationError if the input data cannot be parsed to form a
 valid model.
        337 \'\'\'
        338 # Uses something other than `self` the first arg to allow \'self\' as a set
table attribute
    --> 339 values, fields_set, validation_error = validate_model(__pydantic_self__.__class__, data)
   
     340 if validation_error:
        341     raise validation_error
    
    File /opt/homebrew/lib/python3.11/site-pac
kages/pydantic/v1/main.py:1102, in validate_model(model, input_data, cls)
       1100     continue
       1101 try:
    
-> 1102     values = validator(cls_, values)
       1103 except (ValueError, TypeError, AssertionError) as exc:
       1
104     errors.append(ErrorWrapper(exc, loc=ROOT_KEY))
    
    File /opt/homebrew/lib/python3.11/site-packages/langchai
n/agents/agent.py:881, in AgentExecutor.validate_tools(cls, values)
        878 ()
        879 def validate_tools(cls, v
alues: Dict) -> Dict:
        880     \'\'\'Validate that tools are compatible with agent.\'\'\'
    --> 881     agent =
 values[\'agent\']
        882     tools = values[\'tools\']
        883     allowed_tools = agent.get_allowed_tools()
 
   
    KeyError: 'agent''
    }

Has anyone else encountered this error while working with Vertex AI? If so, how did yo
u resolve it? Any tips or tricks would be greatly appreciated!

UPDATE:

I fix it downgrading the langchain-core version
 from  0.1.51 to 0.1.50!!!
```
---

     
 
all -  [ Smart AI voice assistant + connect to the internet ](https://www.reddit.com/r/ArtificialInteligence/comments/1clxtb8/smart_ai_voice_assistant_connect_to_the_internet/) , 2024-05-08-0909
```
I continue my experiment building a smart AI voice assistant. This time I'm adding an ability to google for an answer. 


I'm using OpenAI function calling + AI assistants combined with SerpApi Google Search API. This way the AI can google f
or real-time data like, current weather, stock, etc.

Here is the full step-by-step tutorial: [https://serpapi.com/blog/
build-a-smart-ai-voice-assistant-connect-to-the-internet/](https://serpapi.com/blog/build-a-smart-ai-voice-assistant-con
nect-to-the-internet/)

\*I still wonder if I can replace OpenAI AI assistants with something else for the chat conversa
tion history. Currently exploring LangChain ecosystem.
```
---

     
 
all -  [ Enhancing Local LLM's Understanding of Technical Documents ](https://www.reddit.com/r/LangChain/comments/1clui48/enhancing_local_llms_understanding_of_technical/) , 2024-05-08-0909
```
Hi

I'm currently using a code that processes a series of reports (PDF files), posing the same set of questions to every
 report. The output is a dataframe containing the responses to each question for every report. For instance, the questio
n 'Does the report explains why the amount of X decreased?' will be answered in a column of my output dataframe. So ever
y line of this column will consist of the answer for a specific report. My setup includes the use of [https://huggingfac
e.co/sentence-transformers/all-MiniLM-L6-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2) and a locall
y downloaded LLM from Hugging Face. Although the code is functional, the reports are highly technical and complex, and t
he local LLM lacks the necessary understanding of the content (I notice that when I read the answers).

I'm looking to e
nhance the LLM's comprehension by training it on additional technical documents of the same nature, hoping this will imp
rove its ability to accurately answer queries from my reports. If I've understood correctly, one approach might be to ut
ilize a RAG on the technical documents, but I'm unsure of the exact steps to implement this effectively. I've attempted 
to merge the embeddings from the downloaded 'all-MiniLM-L6-v2' model with those I generated from the technical documents
, as described here: [https://python.langchain.com/docs/integrations/retrievers/merger\_retriever/](https://python.langc
hain.com/docs/integrations/retrievers/merger_retriever/), but without success.

Could you suggest a viable strategy for 
this? Should I discard the 'all-MiniLM-L6-v2' and focus solely on embeddings derived from my technical documents? This a
pproach seems to require an extensive collection of documents, which I currently don't have.

 I've tried various other 
local LLMs (Mistral, Phi, Llama, Orca), but I encounter the same issue each time. 'Large' LLMs (Mistral e.g.) tend to ha
llucinate, while 'smaller' (Orca e.g.) LLMs often respond that they do not know.

  
Thanks
```
---

     
 
all -  [ problem with multiple rag questions ](https://www.reddit.com/r/LangChain/comments/1clmt84/problem_with_multiple_rag_questions/) , 2024-05-08-0909
```
hi, if i run my code for rag made with python and langchain,the firtst time everything goes well and in the second quest
ion it spits out this error:

  
raise ValueError(f'Missing some input keys: {missing\_keys}')

ValueError: Missing some
 input keys: {'context'}


```
---

     
 
all -  [ Local LLM and LangChain/lida ](https://www.reddit.com/r/LocalLLaMA/comments/1clm4e3/local_llm_and_langchainlida/) , 2024-05-08-0909
```
Hi all, I'm just getting started with playing around with LLMs. I'm trying to follow tutorials for building a CSV chatbo
t using Langchain and lida to do some analysis and visualizations. From what I can find online, both Langchain's create\
_csv\_agenet and lida require OpenAI's chatGPT. Is it possible to use these two packages with a local quantized LLM that
 I have in a .gguf format? Thanks!
```
---

     
 
all -  [ Starting out with Langchain SQL: some questions ](https://www.reddit.com/r/LangChain/comments/1clj3k0/starting_out_with_langchain_sql_some_questions/) , 2024-05-08-0909
```
Hi,

I'm relatively novice when it comes to LLMs, so my understanding is very limited. However, I came across [this YouT
ube Video ](https://youtu.be/9ccl1_Wu24Q?si=gHdxkoCE0gulV3Px)and was impressed with how simple the whole project was set
 up using Langchain and MySQL. I've been experimenting with it using a local version of our company's database, and I ha
ve this vision of developing a chatbot that can talk to our database and answer questions related to the information we 
have in our database.

I have a few questions:

1. I've read a few comments on this subreddit indicating that Langchain 
is not good for SQL. What does this mean, and why is it so?
2. One of the comments on the video critiques the use of Lan
gchain, stating that Langchain packages are not secure, due to passing database schema across third party providers. Is 
this true? My idea would be to create a chatbot for internal use, and implement it into our intranet.
3. In general, how
 beginner friendly is Langchain? I'm under the impression it's moreso compared to other models. 
4. Is Langchain the rig
ht tool for my task?

If I can provide any more context, I'd be happy to do so. Thanks in advance. 
```
---

     
 
all -  [ Is it possible to get different similarity search results with same vector database on different mac ](https://www.reddit.com/r/vectordatabase/comments/1clg3rk/is_it_possible_to_get_different_similarity_search/) , 2024-05-08-0909
```
Hi, recently while I was building a RAG Chatbot I came through an issue i.e below is the code I executed on 4 different 
machines(laptops)

    from langchain_community.embeddings import OllamaEmbeddings
    
    embedding = embeddings.Ollam
aEmbeddings(model='nomic-embed-text')
    db = FAISS.load_local('MS_VDB', embeddings=embedding,allow_dangerous_deseriali
zation=True)
    
    query = 'Recently I was diagnosed with Relapsing-onset MS and the indicated MS phenotype is Highly
 active. List the name of the drugs which can be used to treat my condition'
    
    docs = db.similarity_search(query)

    print(docs[0].page_content)

All the 4 machines use the same vector db file but in 3 machines the similarity search
 result was exactly the same but on the other one it was different even though the code was executed within a virtual en
vironment. Can anyone tell me what's the issue and how I could resolve it so that all the 4 machines give the same outpu
t.
```
---

     
 
all -  [ Is it possible to get different similarity search results with same vector database on different mac ](https://www.reddit.com/r/LangChain/comments/1clfwla/is_it_possible_to_get_different_similarity_search/) , 2024-05-08-0909
```
  
Hi, recently while I was building a RAG Chatbot I came through an issue i.e below is the code I executed on 4 differe
nt machines(laptops) 

    from langchain_community.embeddings import OllamaEmbeddings
    
    embedding = embeddings.O
llamaEmbeddings(model='nomic-embed-text')
    db = FAISS.load_local('MS_VDB', embeddings=embedding,allow_dangerous_deser
ialization=True)
    
    query = 'Recently I was diagnosed with Relapsing-onset MS and the indicated MS phenotype is Hi
ghly active. List the name of the drugs which can be used to treat my condition'
    
    docs = db.similarity_search(qu
ery)
    print(docs[0].page_content)

All the 4 machines use the same vector db file but in 3 machines the similarity se
arch result was exactly the same but on the other one it was different even though the code was executed within a virtua
l environment. Can anyone tell me what's the issue and how I could resolve it so that all the 4 machines give the same o
utput.  
 
```
---

     
 
all -  [ 'GPT to perform 10x with my private knowledge' ](https://www.reddit.com/r/LangChain/comments/1clfhnk/gpt_to_perform_10x_with_my_private_knowledge/) , 2024-05-08-0909
```
['GPT to perform 10x with my private knowledge' - Local Agentic RAG w/- PDF , Website - Here is how (youtube.com)](https
://www.youtube.com/watch?v=5ModxAjKI3w&t=915s)
```
---

     
 
all -  [ DSPy, a no prompt alternate for LangChain  ](https://www.reddit.com/r/LangChain/comments/1cldnq3/dspy_a_no_prompt_alternate_for_langchain/) , 2024-05-08-0909
```
DSPy is an alternate for LangChain, mainly for programmers to build GenAI apps without any prompt engineering by user. C
heckout this beginner friendly tutorial to know the basics of DSPy to get started : 
https://youtu.be/IiaXLP3JKr4?si=xAC
EMVC1c7c174uR
```
---

     
 
all -  [ Langchain Multi user api/app ](https://www.reddit.com/r/LangChain/comments/1clcva5/langchain_multi_user_apiapp/) , 2024-05-08-0909
```
Has anyone here tried to do a multiuser app? Does langchain support it out of the box with configuration, or is this som
ething that needs to be done on my own? It seems that loading several langchain agents takes quite a bit of time which m
eans the client would have to wait quite a bit if I recretead the agent for every request. 

I am not sure how to approa
ch this.   
I do not need message history, just stateless for now.

  
My agents are for reporting purposes at work, so 
they trigger Pandas/Excel processes which can take 30 seconds up to a 1 minute.
```
---

     
 
all -  [ Long response time for Mistral 7b ](https://www.reddit.com/r/MistralAI/comments/1clcjle/long_response_time_for_mistral_7b/) , 2024-05-08-0909
```
Hi guys, currently I am using filipealmeida/Mistral-7B-Instruct-v0.1-sharded with 4 bits quantization as my RAG model wi
th LangChain framework in Google Colab and has successfully utilize it, however the whole response time take really a lo
ng time (about 1-2 mins), and I don't sure what is happened and how to solve it. Is it the problem I am using transforme
r pipeline?
```
---

     
 
all -  [ Building simple reasoning agents without frameworks like Llamaindex or Langchain.  ](https://www.reddit.com/r/LocalLLaMA/comments/1clc6lz/building_simple_reasoning_agents_without/) , 2024-05-08-0909
```
Hi everyone, 

I have been using some LLM frameworks like langchain and Llamaindex for a few weeks and have found modera
te success. I don't like their documentation (probably because the pace at which these are evolving is too rapid) and it
 becomes a little difficult to understand their source code or code examples. 

I want to start simple- build a chat eng
ine centered around multimodal (image/text) retrieval. What I've done is I've indexed some images and their captions (us
ing CLIP embeddings) to Pinecone. I can do simple things like similarity search. I haven't used LLM frameworks at all to
 do this. I've used the pinecone and clip functions directly. I can do text to image retrieval, text to text retreival a
nd things like that.

What I want to do now is create simple 'reasoning' systems that can reason about these images. I w
ant to create a chain like structure which looks like this 

query --> retrieve similar images and captions ---> summari
ze the captions / describe the objects (run some object detection algorithm) / possibly other things etc.  

Call me a m
asochist but I don't want to use langchain or llamaindex. Can this chaining operation be performed with the bare OpenAI 
API or function calling? I hope so. I'm kinda new to this and will appreciate any help.
```
---

     
 
all -  [ langchain response in particular format ](https://www.reddit.com/r/Langchaindev/comments/1cl8hfg/langchain_response_in_particular_format/) , 2024-05-08-0909
```
how to write a prompt which does the work of greeting by introducing it self and another prompt for giving question answ
ers with memory added into it.kindly give the code and the prompt stacking approch using selfquery retrieval.
```
---

     
 
all -  [ What are your current go to libraries? ](https://www.reddit.com/r/LocalLLaMA/comments/1cl6lx3/what_are_your_current_go_to_libraries/) , 2024-05-08-0909
```
There is a lot to keep up with and I was wanting to get an idea of what people are finding useful right now. Specificall
y, programming libraries, not UI's.

EDIT  
Guess I should share as well. These are the tools I've been playing around w
ith (not really committed to use any one of them yet).

**General**

* [llama-cpp-python](https://pypi.org/project/llama
-cpp-python/)

**DSL**

* [guidance](https://github.com/guidance-ai/guidance)

**RAG Frameworks**

* [Langchain](https:/
/www.langchain.com/)
* [LlamaIndex](https://docs.llamaindex.ai/en/stable/)
* [DSPy](https://github.com/stanfordnlp/dspy)


**Model Serving**

* [Ollama](https://ollama.com/)
```
---

     
 
all -  [ What is the most proper way to develop this chatbot? ](https://www.reddit.com/r/LangChain/comments/1cl522l/what_is_the_most_proper_way_to_develop_this/) , 2024-05-08-0909
```
Hey guys! Before I begin, thanks to those that took the time to read my post and hopefully respond, it's really much app
reciated. Now onto our topic; I'm trying to build a conversation chatbot which objective is to offer to the user game re
commendations that fit different criteria and preferences that could be found in his initial query.

What I want the cha
tbot to do, is first evaluate the query, have it better understand. See if the query is on the topic of asking for game 
recommendations, or whether his input is clear enough, which in the case of them not meeting one of the requirements, ha
ve the chatbot ask from the user to input a proper one.

After making sure that his input is alright and is done with re
viewing it, make calls to various tools that rely on SerpApi. such as the Google search one for finding suitable titles 
to be chosen as candidate for the final answer and gather more additional information for each game, or the Google image
s and Youtube one for gathering multimedia content, such as games' posters and official trailers.

Once the chatbot is d
one with browsing the web in order to fetch what it needs, let it formulate a response to the user. One important functi
onality that I want present in this chatbot is that, if the user asks from the chatbot to find alternatives to some of t
he titles found in the response, it should be able to remember that response in the first to be able and apply modificat
ions to it, such as the replacing actions of certain mentioned titles with other ones.

Now that the requirements of thi
s chatbot are somewhat clear, how would you recommend me to go on developing such project? What key factors should I tak
e into consideration and make use of in order to achieve the desired results?
```
---

     
 
all -  [ LLM use case for QA and reasoning. ](https://www.reddit.com/r/LangChain/comments/1cl4mx6/llm_use_case_for_qa_and_reasoning/) , 2024-05-08-0909
```
I have a use case, where I have textual data. I have to extract information from it. Some of the data is direct and can 
be assigned directly. Others are not so-direct, like total weight, total quantity, these values are supposed to be calcu
lated after extracting individual data from the data. 

Since RAG provides contextual information, so I am planning to i
nform the LLM about the labels to be extracted. I am also planning to fine-tune Llama3 on annotations so model learns ab
out what how information extraction is actually taking place.  
  
What else can be done to improve the output performan
ce of model. 
```
---

     
 
all -  [ Do Output Parser like the JSON one, have a retry option? ](https://www.reddit.com/r/LangChain/comments/1ckzzfs/do_output_parser_like_the_json_one_have_a_retry/) , 2024-05-08-0909
```
Hi I am currently struglling with how to approach error handling with a JSON output parser. Can it do retries? I feel li
ke every output parser should just allow retry by default, because often the result can be bad for 1 - 2 requests and th
at is it.

If not then is it possible to use retryOutput parser with LCEL?
```
---

     
 
all -  [ Local model based RAG ChatBot ](https://www.reddit.com/r/LangChain/comments/1cktopp/local_model_based_rag_chatbot/) , 2024-05-08-0909
```
Hi,

We are creating a rag based ChatBot for our company but due to some infosec concerns we have to use only local llms
 and database.

Due to this reason we are not using openAI/Gemini or any API based models and instead we are using Ollam
a for our local models and using LLAMA 3 as our LLM. 

Now the issue is when we are using local Embeddings model like no
mic-embed it's not producing very good results. What should i do to overcome this issue and i have tried different local
 Embeddings model of ollama but they aren't producing very good results.
```
---

     
 
all -  [ Need help in Structured Extraction of data ](https://www.reddit.com/r/LangChain/comments/1ckt04y/need_help_in_structured_extraction_of_data/) , 2024-05-08-0909
```
Hey , I have been dabbling with a few methods to extract data from a corpus of documents in structured format and have b
een experimenting with pydantic classes and even agents. But still, I am not able to achieve the desired result. I follo
wed the Langchain documentation for extracting data but the method where we use Reference examples is not working.

To s
pecify my use case, I want to extract data from legal documents in a chronological method. Would love to get some tips/ 
ideas or your methods if you have been doing something like this. Here is a fellow company doing the same www . tryabel.
 com.

Thanks!
```
---

     
 
all -  [ Using Weaviate & Langchain together ](https://www.reddit.com/r/LangChain/comments/1ckszg1/using_weaviate_langchain_together/) , 2024-05-08-0909
```
Hey everyone,  
Does anyone have any good tutorials or blogpost about how to use weaviate as a vector store and use Lang
chain to perform activities like, creating new collections, adding document, performing similarity search etc. The offic
ial documentation from Langchain work when I perform all these actions sequentially. However, when loading the persisted
 vector store, I am unable to perform similarity search.
```
---

     
 
all -  [ Resume of a 2023 graduate targeting machine learning roles. ](https://www.reddit.com/r/developersIndia/comments/1ckrno0/resume_of_a_2023_graduate_targeting_machine/) , 2024-05-08-0909
```
Hello all, I am a 2023 graduate, I have been jobless since graduation but I have been trying hard to get a job. During t
his whole break I have not stopped and kept myself up to date with the latest technologies in machine learning and tried
 to keep busy and upskill myself.  
I have had very little success in my job search, I got a few interviews but companie
s select other candidates in the end who have more experience than me. My resume scores good on ATS but I still don't kn
ow if its good enough. 

https://preview.redd.it/kh4837sx3myc1.png?width=429&format=png&auto=webp&s=8bcd822f965d2e10488b
003ad1048b87f1f50d4c

Please help me out, any kind of feedback will be appreciated.   

```
---

     
 
all -  [ Fine tuning for Function Calling ](https://www.reddit.com/r/LangChain/comments/1ckpwg4/fine_tuning_for_function_calling/) , 2024-05-08-0909
```
Is it a good idea to fine tune a cheaper model like chatgpt 3.5 and train it on your function calling samples where the 
tool is basically a http fetch request to get data from API based on parameters in the user's query?

I am currently usi
ng gpt 4 2024 model, and the cons are 1) it's expensive 2) I have to add examples in my system prompt 3) It still fails 
at times with mapping the parameters (more than 4 different parameters such as region, duration, price etc)

I am consid
ering this but posting this to check if someone found this viable? 
```
---

     
 
all -  [ help in creating a RAG chatbot  ](https://www.reddit.com/r/LangChain/comments/1ckoupq/help_in_creating_a_rag_chatbot/) , 2024-05-08-0909
```
Hi Guy i need your help!  
  
i want to build a chatbot service that is a cartoon character that helps people with their
 body transformation journey , its has a database with relevant products, it offers products to users when they ask body
 transformation questions using the database .   
for example :  
'i want to gain weight , how do i do it ?'  
'im 178cm
 and 78kg and i want to gain 10kg '  
'if im looking to lose 5% body fat , what should i do ?'  
  
to do so i build a n
umber of chatbots each with a different exaction approach but each has its own issues and i cant find the execution that
 will satisfy me .  
  
1st approach:  
using langchain and added a custom tool , that holds the products in a vector da
tabase .  
  
the problems with this approach: it doesnt always go to the tool , sometimes it does and sometimes it does
nt .   
and i cant control it , the llm decides by itself if to look in the tool or not , this leads to unstable results
 of similar conversations   
  
2nd approach :  
i used the openai wrapper and used groq llm service , without langchain
 , were i added a custom tool , here the process is different .  
process:  
- get user input   
- created a llm call to
 determine if the function would be called by looking at the user input   
- if the function is to call then i call the 
function with the user input and get the products   
- create a llm call with a system prompt and user input plus the re
levant products   
-if the function is not to call , then ill create a llm call with a different system prompt and use o
nly the user input   
- also introduce the user and chatbot summary chat history to give the llm context   
  
the probl
ems with this approach :  
again not always it goes to the tool so its a problem , here it performs better then the firs
t approach , but i feel its hard to keep the context of the conversation and the history is getting bigger and bigger ve
ry fast and then the llm looses understanding of the user input   
  
3rd approach:  
- get user input   
- always use u
ser input to look for relevant products in the vector database  
- summary the conversation until now   
- do a llm call
 using the system prompt , user input , the relevant products , and conversation summary   
  
the problem with this app
roach :  
from all of the approaches this preforms the best but it still has issues , because i use a lot of information
 in each llm call , and i ask it to respond to the user input and use the products only if they are relevant . when the 
user wants to end the conversation and say 'thank you' or 'great' inside the llm call it gets lots of information and th
e respond misses the point , and it answers like the user is still looking for help and doesnt understand the context of
 where we are right now   
  
  
i want to know what is the best approach to create a chat bot that users can talk to , 
get relevant products for their body transformation journey , but also talk to the llm regularly and for it to respond o
nly to the relevant message . please tell me from your experience what is the best approach .   
  
i really appreciate 
any help.   
```
---

     
 
all -  [ Question on Multi lingual data ](https://www.reddit.com/r/LangChain/comments/1ckmuq2/question_on_multi_lingual_data/) , 2024-05-08-0909
```
Hi, I’m trying to build a Chat bot for our org using langchain. The knowledge base is primarily Wordpress blogs, books a
nd YouTube videos.
The YouTube videos happen to be in English and Hindi(language of India). How should I go about data i
ngestion? Should I translate the Hindi video transcripts to English and then embed them or should I embed all the transc
ripts irrespective of language using a multi lingual model from something like cohere?
```
---

     
 
all -  [ Prompt Engineering Testing Suite...? ](https://www.reddit.com/r/PromptEngineering/comments/1ckkw3t/prompt_engineering_testing_suite/) , 2024-05-08-0909
```
Hi fellow prompters, good to meet you!

I'm looking for advice. I was wondering if you were having similar issues to the
 ones I'm having:

- I want to compare and test different LLMs in one place and keep track of changes.

- I'm not really
 sure how to hook up to all these different LLM providers (openai, claude, google) API effectively 

- I'm basically won
dering if there's like a prompt testing/deployment kit that's more intuitive and simple than Galileo/Langchain.

Can you
 tell me about your guys's current tools for prompt testing and switching between different models?

I'm trying to learn
 more about other people working in this area.

Thanks :)
```
---

     
 
all -  [ 3rd year student studying CS ](https://www.reddit.com/r/resumes/comments/1ckkc7b/3rd_year_student_studying_cs/) , 2024-05-08-0909
```
I have applied to around 300-400 companies this year and have received a couple interviews but majority negative respons
es. I feel like there is something going wrong with my resume and any feedback is highly appreciated

https://preview.re
dd.it/xto1ucqarjyc1.jpg?width=850&format=pjpg&auto=webp&s=f96cc2f0c27092584961b6e8595f03fa21dac9a7


```
---

     
 
all -  [ [For Hire] I will be your AI Consultant for free  ](https://www.reddit.com/r/jobbit/comments/1ckhkcj/for_hire_i_will_be_your_ai_consultant_for_free/) , 2024-05-08-0909
```
Are you intrigued by the AI trend but unsure how it could enhance your business, leading to a sense of FOMO? Fear not! 


Let's explore how AI can seamlessly integrate into your business operations. From analyzing your processes to identifyi
ng AI opportunities, I'll provide insights into how your business can benefit. 

With expertise in diverse AI tools, fro
m no-code platforms like Voiceflow to advanced frameworks like Langchain, I'm equipped to guide you through the possibil
ities. 

Drop me a DM with your availability, and let's delve into the specifics of your business!
```
---

     
 
MachineLearning -  [ [D] Self-optimizing deterministic LLM memory using dspy, neo4j and vector databases. Need your input ](https://www.reddit.com/r/MachineLearning/comments/1cakjaf/d_selfoptimizing_deterministic_llm_memory_using/) , 2024-05-08-0909
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

     
 
deeplearning -  [ Seeking Advice: Solving Data Challenges with Large Language Models (LLMs) ](https://www.reddit.com/r/deeplearning/comments/1ca4nc1/seeking_advice_solving_data_challenges_with_large/) , 2024-05-08-0909
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

     
 
deeplearning -  [ Share the Coolest Out of The Box LLM Applications That Made You Say 'Wow that was smart' ](https://www.reddit.com/r/deeplearning/comments/1c9e6dj/share_the_coolest_out_of_the_box_llm_applications/) , 2024-05-08-0909
```
Hi, I'm looking at some LLM applications today but apart from guys doing big rags with langchain I don't see too many us
es that are out of the box or that make me say 'wow that was smart to use an LLM here'. Have you seen any cool stuff usi
ng LLMs recently that made you say 'wow, that was smart'?
```
---

     
