 
all -  [ How to Invoke RunnableSequence chain with multiple inputs ](https://www.reddit.com/r/LangChain/comments/1dt57k9/how_to_invoke_runnablesequence_chain_with/) , 2024-07-02-0911
```
I have a PromptTemplate with three inputs: cause, symptom, and action. My LLM should use the inputs to produce a 'theme'
 it gathers from the inputs. However, I am getting an error because the chain.invoke method expects one input instead of
 multiple.

This is the error that is thrown: ValueError: Invalid input type <class 'dict'>. Must be a PromptValue, str,
 or list of BaseMessages.

All the examples of invoking a chain in the langchain documentation only have one input. What
 am I supposed to do when my prompt template contains three inputs?

For reference, this is the code:

`llm = AzureChatO
penAI()`

`prompt_template = PromptTemplate(`

`input_variables=['cause', 'symptom', 'action'],`

`template='''`

`Root 
Cause:`

`{cause}`

`Complaint Symptom:`

`{symptom}`

`Corrective Action:`

`{action}`

`Based on the information provi
ded above, generate a concise 'Failure Theme' encapulating the reason for the failure.`

`Failure Theme:`

`'''`

`)`

`
chain = llm | prompt_template | StrOutputParser()`

`root_cause = df.iloc[0]['Root Cause']`

`complaint_symptom = df.ilo
c[0]['Complaint Symptom']`

`corrective_action = df.iloc[0]['Corrective Action']`

`chain.invoke({'cause': root_cause, '
symptom': complaint_symptom, 'action': corrective_action})`

 
```
---

     
 
all -  [ [2 YoE] Resume feedback for MLE/DE/SWE roles ](https://www.reddit.com/r/resumes/comments/1dt48yc/2_yoe_resume_feedback_for_mledeswe_roles/) , 2024-07-02-0911
```
Hey r/resumes,

I'm a recent grad with about 2 years of experience as a data and backend engineer at a boutique consulti
ng firm (roughly around B4 caliber, though that could be hit-or-miss when it comes to SWE-type roles afaik). I'm wonderi
ng where my resume can be improved in terms of bullets, structure, wordiness, or any other shortcomings y'all may see. I
'm confident in my abilities and experience, but have been receiving rejection after rejection to the point where I'm un
sure where the problem is. Given how tough the market is now, I'd appreciate any advice you have on how to level this up
 as I do think I tick a lot of the boxes I see on job postings - just want to make sure I'm not going wrong somewhere.


Thanks!

https://preview.redd.it/hct8wzmt3z9d1.jpg?width=2550&format=pjpg&auto=webp&s=2d6ba783559e081a615c74561a65e6dc9c
09a20e


```
---

     
 
all -  [ Resume for Machine Learning roles. Feel free to roast and suggest changes  ](https://www.reddit.com/r/developersIndia/comments/1dt2p6n/resume_for_machine_learning_roles_feel_free_to/) , 2024-07-02-0911
```
https://preview.redd.it/dbb8f6zvry9d1.png?width=1188&format=png&auto=webp&s=88152f72bc2fdbd90d066f5a314cfbb085ceaa53


```
---

     
 
all -  [ Automate Slide decks and presentations ](https://www.reddit.com/r/LangChain/comments/1dt0zzz/automate_slide_decks_and_presentations/) , 2024-07-02-0911
```
https://medium.com/genai-agents-unleashed/generate-powerpoint-presentation-with-openai-the-future-of-slide-decks-ce1a7c9
28986
```
---

     
 
all -  [ How to generate Cypher Query using LLM? ](https://www.reddit.com/r/LangChain/comments/1dt089d/how_to_generate_cypher_query_using_llm/) , 2024-07-02-0911
```
I have a huge schema in the neo4j database.

I'm using the LangChain function to generate a cypher query

chain = GraphC
ypherQAChain.from_llm(
ChatOpenAI(temperature=0), graph=graph, verbose=True
)

chain.invoke(query)

It's returning an er
ror saying that the model supports 16k tokens and I'm passing 15M+ tokens

How can I limit these tokens? I tried setting
 ChatOpenAI(temperature=0, max_tokens=1000) and it's still giving the same error.

I think it's passing the whole schema
 at once, how can I set a limit on that?
```
---

     
 
all -  [ HuggingFace models on multiple GPUs ](https://www.reddit.com/r/huggingface/comments/1dszyy3/huggingface_models_on_multiple_gpus/) , 2024-07-02-0911
```
I made a RAG app that basically answers user questions based on provided data, it works fine on GPU and a single GPU. I 
want to deploy it on multiple GPUs (4 T4s) but I always get CUDA out of Memory error on pipeline.



I tried using 'auto
' keyword too but Langchain does not let me use it as keyword.

I used Langchain as main framework, my code looks like t
his:



    from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline, HuggingFaceEmbeddings
    MODEL_NAME
='mistralai/Mistral-7B-Instruct-v0.3'
    pipe = HuggingFacePipeline.from_model_id(
                               model
_id=MODEL_NAME,
                               device=0,
                               model_kwargs={'torch_dtype':torc
h.float16},
                               task='text-generation')
    llm = ChatHuggingFace(llm=pipe)
    
    embeddin
g = HuggingFaceEmbeddings(model_name=MODEL_NAME,
                                      model_kwargs={'device':'cuda:1'},

                                      multi_process=True,
                                      )






```
---

     
 
all -  [ RAG app on multiple GPUs ](https://www.reddit.com/r/LangChain/comments/1dszxdk/rag_app_on_multiple_gpus/) , 2024-07-02-0911
```
I made a RAG app that basically answers user questions based on provided data, it works fine on GPU and a single GPU. I 
want to deploy it on multiple GPUs (4 T4s) but I always get CUDA out of Memory error on pipeline.

I tried using 'auto' 
keyword too but Langchain does not let me use it as keyword.

I used Langchain as main framework, my code looks like thi
s:

    from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline, HuggingFaceEmbeddings
    MODEL_NAME='mi
stralai/Mistral-7B-Instruct-v0.3'
    pipe = HuggingFacePipeline.from_model_id(
    model_id=MODEL_NAME,
    device=0,
 
   model_kwargs={'torch_dtype':torch.float16},
    task='text-generation')
    llm = ChatHuggingFace(llm=pipe)
    embed
ding = HuggingFaceEmbeddings(model_name=MODEL_NAME,
    model_kwargs={'device':'cuda:1'},
    multi_process=True,
    )
```
---

     
 
all -  [ What's wrong with Langchain React Agent ](https://www.reddit.com/r/LangChain/comments/1dsyf46/whats_wrong_with_langchain_react_agent/) , 2024-07-02-0911
```
    i asked react agent about last name of johnny it's not showing in it's final output why ?
    
    I think I have fo
und the table that contains the name 'JOHNNY'. It's the 'actor' table. Now, I need to write a query to retrieve the last
 name of the actor with the first name 'JOHNNY'.
    
    Action: sql_db_query_checker
    Action Input: SELECT last_nam
e FROM actor WHERE first_name = 'JOHNNY'SELECT last_name FROM actor WHERE first_name = 'JOHNNY'Action: sql_db_query
    
Action Input: SELECT last_name FROM actor WHERE first_name = 'JOHNNY'[('LOLLOBRIGIDA',), ('CAGE',)]I now know the final 
answer
    Final Answer: The last name of JOHNNY is not found in the database, but there are actors with the last names 
LOLLOBRIGIDA and CAGE who have first names that are not JOHNNY. It's possible that the actor with the first name JOHNNY 
does not exist in the database.
    
    > Finished chain.
```
---

     
 
all -  [ Built a PR Agent with Langchain and 3 other frameworks - A Comparison ](https://www.reddit.com/r/LangChain/comments/1dsych9/built_a_pr_agent_with_langchain_and_3_other/) , 2024-07-02-0911
```
The goal was to create an agent that would:

1. Monitor a GitHub repository for new PRs
2. Perform a code review on each
 PR
3. Post a summary of the review to a Slack channel

https://preview.redd.it/0yf542afwx9d1.png?width=1442&format=png&
auto=webp&s=791bd8618af7c67f8e20d928705639366bea065b

|Framework|Why langchain is better|Why it can be better|
|:-|:-|:-
|
|CrewAI|Langchain provides a more comprehensive toolkit for building various AI applications, including but not limite
d to multi-agent scenarios.|CrewAI may be easier to get started with for specific multi-agent tasks|
|Llama Index|Langch
ain offers more general-purpose capabilities|For projects primarily focused on data indexing and retrieval, llama index 
is better|
|Autogen|Langchain provides more structured components for building AI applications|For projects requiring hi
ghly dynamic multi-agent interactions, Autogen's specialized focus might provide a more intuitive framework|

The agent 
works great!

here's the link for the project: [https://git.new/pr-agent-langchain](https://git.new/pr-agent-langchain)
```
---

     
 
all -  [ I built a PR Agent with all the Agentic Frameworks - Here's my experience ](https://www.reddit.com/r/LocalLLaMA/comments/1dsxros/i_built_a_pr_agent_with_all_the_agentic/) , 2024-07-02-0911
```
I've intensively been building and experimenting with agents using all the famous libraries mentioned above. I've experi
mented with both Closed and Open Source LLMs and i want to share my experience.

**Quick Framework Review**

|Framework|
Strengths|Considerations|
|:-|:-|:-|
|CrewAI|High-level abstraction, good for beginners|Less mature ecosystem|
|Autogen|
Easy agent setup, multi-agent interactions|Limited external tool integration|
|Langchain|Versatile, extensive features|S
teeper learning curve|
|LlamaIndex|Specialized in data handling|Fewer agent interaction features|
|OpenAI|Direct model a
ccess, frequent updates|Requires more custom code for complex systems|

**Quick Tooling Review**

|Tools Framework|Stren
gths|
|:-|:-|
|Langchain Tools|High flexibility but increased complexity|
|Composio|Exceptionally easy third-party app i
ntegration (e.g., GitHub, Slack)|

# Detailed Review

For developers with experience in LLM-based application developmen
t, adopting any of these frameworks is relatively straightforward. Each framework offers unique opportunities to create 
innovative applications.

1. CrewAI and Autogen:
   * Recommended for beginners
   * Higher level of abstraction
   * Ea
sier entry point for AI agent development
2. Langchain:
   * Next step after gaining experience
   * Offers more refined
 outputs
   * Greater flexibility and control
3. LlamaIndex:
   * Currently less feature-rich compared to Langchain
   *
 Rapidly evolving and closing the feature gap
4. OpenAI:
   * Best framework for using ChatGPT in terms of performance
 
  * You have a good support for the framework

# Detailed Review for Tooling

# Composio

* Exceptionally easy third-par
ty app integration (e.g., GitHub, Slack)
* Minimal setup time required

# Langchain Tools

* Comprehensive toolset with 
extensive integration options
* Requires more manual configuration (auth tokens, API setup)
* High flexibility but incre
ased complexity

These insights come from my project that monitors PRs, reviews it and pings the review on slack. here's
 the link if you want to try it: [https://git.new/pr-agent](https://git.new/pr-agent)

# Challenges and Considerations


* Frequent updates lead to potential code obsolescence
* Syntax and function parameters often change
* Regular maintenan
ce required to keep applications functional

# Open Source vs. Closed Source Performance

* AI agents: Open source model
s competitive with closed-source alternatives
* Would recommend inference APIs over locally hosted ones, just on the bas
is of convenience and not performance although with weaker models you would get weaker outputs.

edit: the frameworks iv
e used are CrewAI, Langchain, Llama Index and Autogen mainly, im sure there are multiple frameworks that i'm unaware of,
 but for the sake of the post i chose these.
```
---

     
 
all -  [ Chat With Any WebPage or Application using Visual Agents & OpenAI ](https://www.reddit.com/r/OpenAI/comments/1dswf67/chat_with_any_webpage_or_application_using_visual/) , 2024-07-02-0911
```
I made a TL;DR video about using our browser extension to run your chat agents alongside any web page or app! Visually d
esign your LangChain RAG +  OpenAI LLM + Agents app, add a chat UI to it and use it instantly, all from your browser. No
 code!

[https://youtu.be/5-QV3lVI8uo](https://youtu.be/5-QV3lVI8uo)  


[https://visualagents.ai](https://visualagents.
ai)
```
---

     
 
all -  [ Chat With Any WebPage or Application using Visual Agents & LangChain ](https://www.reddit.com/r/LangChain/comments/1dswds9/chat_with_any_webpage_or_application_using_visual/) , 2024-07-02-0911
```
I made a TL;DR video about using our browser extension to run your chat agents alongside any web page or app! Visually d
esign your LangChain RAG + Agents app, add a chat UI to it and use it instantly, all from your browser. No code!

[https
://youtu.be/5-QV3lVI8uo](https://youtu.be/5-QV3lVI8uo)
```
---

     
 
all -  [ [PDF] Poisoned LangChain: Jailbreak LLMs by LangChain ](https://arxiv.org/pdf/2406.18122v1) , 2024-07-02-0911
```

```
---

     
 
all -  [ choosing multi-tool in agent ](https://www.reddit.com/r/LangChain/comments/1dsvy6s/choosing_multitool_in_agent/) , 2024-07-02-0911
```
I haven't seen the sample in Langchain 0.2, so I just referenced [v0.1](https://python.langchain.com/v0.1/docs/use_cases
/tool_use/multiple_tools/)

I use local model with 'taide-7b-a.2-q4\_k\_m.gguf', so there are some different

          
  llm = ChatLlamaCpp(
                model_path= str(model_path),
                n_gpu_layers=100,
                n_b
atch=512,
                n_ctx=2048,
                f16_kv=True,
                callback_manager=CallbackManager([Str
eamingStdOutCallbackHandler()]),
                verbose=True,
            ) 

after invoking the question, I can't get 
the tools information. like

    [{'name': 'multiply',
      'args': {'first_int': 23, 'second_int': 7},
      'id': 'to
olu_01Wf8kUs36kxRKLDL8vs7G8q',
      'output': 161}]

Can anyone tell me what's wrong? here's the code

        tools = 
[multiply, exponentiate, add]
        llm_with_tools = llm.bind_tools(tools)
    
        def call_tools(msg: AIMessage)
 -> Runnable:
            '''Simple tool calling helper.'''
            tool_map = {tool.name: tool for tool in tools}
 
           tool_calls = msg.tool_calls.copy()
            for tool_call in tool_calls:
                tool_call['output
']  = tool_map[tool_call['name']].invoke(tool_call['args'])
            return tool_calls
    
        chain = llm_with_
tools | call_tools
        chain.invoke('23 times 7')


```
---

     
 
all -  [ Streaming responses have words split ](https://www.reddit.com/r/LangChain/comments/1dsvmg8/streaming_responses_have_words_split/) , 2024-07-02-0911
```
Using astream, the response from the LLM has words that are split for example the word 'hippopotamus' comes as 2 chunks 
'hippo' and 'potamus'. When creating an app, how to recognize and combine the 2 split parts into a single word for front
-end?
```
---

     
 
all -  [ Integrate multiple AWS bedrock LLMs seamlessly with Langchain ](https://www.reddit.com/r/LangChain/comments/1dsrfca/integrate_multiple_aws_bedrock_llms_seamlessly/) , 2024-07-02-0911
```
Hello everyone,

Here's a cool post that shows how to integrate multiple AWS Bedrock LLMs in your LangChain apps and cho
osing which one used with only one configuration parameter.

Here's the link:  [link](https://www.metadocs.co/2024/04/11
/handle-multiple-llm-models-in-langchain-and-aws-bedrock-seamlessly/).

  
Have a nice read.
```
---

     
 
all -  [ Agent Routing Inquiry ](https://www.reddit.com/r/LangChain/comments/1dsr8tf/agent_routing_inquiry/) , 2024-07-02-0911
```
I want help with how to go about an idea.

I currently need to build a ‘virtual assistant’ chatbot at work.

For the POC
, I am using LangChain, LangGraph, and Chainlit for the UI. 

I want through the chatbot based LLM app to be able to acc
ess the following:
1. RAG
2. Web Search
3. Normal Conversational Chat

For the persona of the chatbot, I know I can just
 set that in the context prompt of the system message.

But for the Agent capabilities, I have a simple corrective RAG a
gent graph made in LangGraph.

My questions are:
1. How do I current the capabilities of the agent graph made to my basi
c langchain chainlit app?
2. Do I need to make another conversational agent that can be routed to for normal chatbot cap
abilities or no?
3. How do I make Web Searching with Tavily an ability?
4. What will the final architecture look like?



I really appreciate any input you have.

If anyone is kind enough to give me 10 mins of their time on a discord call, I
 would REALLY REALLY appreciate it!

```
---

     
 
all -  [ Clear State in Langgraph to delete chat history ](https://www.reddit.com/r/LangChain/comments/1dsr14k/clear_state_in_langgraph_to_delete_chat_history/) , 2024-07-02-0911
```
Hi,

I am using Langgraph and now I want to clear the state if a user presses the button: 'Clear Chat History'. 

How ca
n I clear the state of my Graph or set it to the default values?

  
I can view the state like this: 

    config ={
   
         'configurable': {'thread_id': 'user_id19999'}, #here specific user_ids or conversation_ids can be inserted if n
eeded
            'callbacks': [langfuse_handler] #if you are not using Langfuse, use 'ConsoleCallbackHandler' for 'call
backs' 
        }
    app.get_state(config).values

Which gives me this output:

{'question': 'Wie war mein Name?',  
 '
raw\_docs': \[\],  
 'generation': AIMessage(content='Es tut mir leid, aber zu Ihrer Frage nach meinem Namen konnten kei
ne Inhalte in Confluence gefunden werden. Ich antworte Ihnen gerne, dass mein Name AnswerBot lautet. Bitte beachten Sie,
 dass diese Antwort nicht anhand von Confluence-Kontextinformationen generiert wurde und ich die Richtigkeit der Antwort
 nicht sicherstellen kann. Es kann hilfreich sein, die Frage klarer zu formulieren, damit Informationen dazu besser gefu
nden werden können.', response\_metadata={'finish\_reason': 'stop'}, id='run-6e24ee0f-bbe6-4d8f-99c2-3f816555ffe4'),  
 
'messages': \[HumanMessage(content='Wie war mein Name?', id='2b259646-0465-4b86-80d5-332f005083ab')\],  
 'is\_smalltalk
': 'False',}
```
---

     
 
all -  [ Custom Functions with RunnableLambda in LangChain JS ](https://www.reddit.com/r/LangChain/comments/1dso9pj/custom_functions_with_runnablelambda_in_langchain/) , 2024-07-02-0911
```
Made a short post about how to make Custom Functions with RunnableLambda in LangChain JS:

[https://www.js-craft.io/blog
/custom-functions-runnablelambda-langchain-js/](https://www.js-craft.io/blog/custom-functions-runnablelambda-langchain-j
s/)

https://preview.redd.it/9v8pcoekfv9d1.png?width=1474&format=png&auto=webp&s=8dfa8bb8a5efb6b1873e1ee70fba90cd43f2e4f
f


```
---

     
 
all -  [ Decreasing the response time in Multi-Agent Workflow of LangGraph using Ollama - Llama 3 model ](https://www.reddit.com/r/LangChain/comments/1dsmk86/decreasing_the_response_time_in_multiagent/) , 2024-07-02-0911
```
So recently I was testing out the Multi-Agent Workflow of langchain with some budget constraints and hence I decided to 
use Llama 3 model from Ollama. 

I am following the supervisor structure as shown in their tutorials. The role of the su
pervisor is to simply redirect the query to one particular agent and that particular agent then handles the extraction o
f some special attributes from the user query.

[Multi-Agent Workflow Schema Diagram](https://preview.redd.it/nsib0o7btu
9d1.png?width=1934&format=png&auto=webp&s=96b120524949e1af997b82b3df221b9824ce1d8d)

Now what's happening is that when I
 run these agents (without langraph) on a individual script level for 5 user queries, the first query takes around 20 se
conds to generate the response and then the subsequent 4 queries give response like within 3 seconds. 

But when I conne
ct the supervisor to the agents using LangGraph, and I test it for the same 5 queries, each query takes > 100 seconds to
 yield the final output. 

  
My hardware specs are pretty decent i believe and should not be a hardware issue :-

RAM- 
16GB, PROCESSOR - RYZEN 9, GPU - 4GB RTX 3050

Is this happening most likely due to a code level issue or something rela
ted to my ollama server settings like number of models running parallelly? 
```
---

     
 
all -  [ Git Assistant 1.4.0 is now available, adding a commits insight tool window.
 ](https://www.reddit.com/r/Jetbrains/comments/1dslzgp/git_assistant_140_is_now_available_adding_a/) , 2024-07-02-0911
```
Contributor rankings: See who tops the leaderboard for your repository. It's fun, competitive, and informative!

Commit 
time analysis: Discover when your team is most active - by hour, week, month, or year. Are you a night owl or a morning 
person?

Time zone distribution: Visualize where in the world your commits come from. Global teamwork becomes visible

h
ttps://preview.redd.it/6vk8syavnu9d1.png?width=3024&format=png&auto=webp&s=b7ef8677221b8b3c272a145712e6be48a57dc5d9

htt
ps://preview.redd.it/bfvnnscvnu9d1.png?width=3024&format=png&auto=webp&s=d11afb5339f8ff089b81ec21b6fe1ffb69505e9b

https
://preview.redd.it/gnha2xavnu9d1.png?width=3024&format=png&auto=webp&s=00d32b906542994acb4d2ec02df4453ca745ce40

https:/
/preview.redd.it/fqhvsvavnu9d1.png?width=3024&format=png&auto=webp&s=f773cdf07029f2d22ac9c0f973a8b71685ea52b4

https://p
review.redd.it/oe3g66cvnu9d1.png?width=3024&format=png&auto=webp&s=e74bf03ee4804647adb5e574501438667bc2e84b


```
---

     
 
all -  [ Git Assistant 1.4.0 is now available, adding a commits insight tool window. ](https://www.reddit.com/r/git/comments/1dsluue/git_assistant_140_is_now_available_adding_a/) , 2024-07-02-0911
```
  
[https://plugins.jetbrains.com/plugin/24154-git-assistant](https://plugins.jetbrains.com/plugin/24154-git-assistant) 
 
  
Contributor rankings: See who tops the leaderboard for your repository. It's fun, competitive, and informative!

Co
mmit time analysis: Discover when your team is most active - by hour, week, month, or year. Are you a night owl or a mor
ning person?

Time zone distribution: Visualize where in the world your commits come from. Global teamwork becomes visib
le!

https://preview.redd.it/h5cu50m7mu9d1.png?width=3024&format=png&auto=webp&s=010cd4bf2d9cf0525517aa4306cdb825122d2c5
8

https://preview.redd.it/smvm3pl7mu9d1.png?width=3024&format=png&auto=webp&s=f04902820bee01e946e3a42096a86956d5fc37b3


https://preview.redd.it/zsygjpl7mu9d1.png?width=3024&format=png&auto=webp&s=91e945723a4901fb70f3ed33a323a5b0ae7ae9d2

h
ttps://preview.redd.it/dq6w5ql7mu9d1.png?width=3024&format=png&auto=webp&s=926840a913c498b2be6bd7f9c08deff5aeb2cfb6

htt
ps://preview.redd.it/aj88dkn7mu9d1.png?width=3024&format=png&auto=webp&s=b4c90d7f80425564f805fb63f3a4a160bd26f98f
```
---

     
 
all -  [ SAS to Hive sql conversions using LLM ](https://www.reddit.com/r/LangChain/comments/1dsl8ne/sas_to_hive_sql_conversions_using_llm/) , 2024-07-02-0911
```
Hi All,  
any resources or reference , I can get to convert the SAS scripts into HIve SQL using LLMs?  

```
---

     
 
all -  [ Evaluate different LLMs or flows ](https://www.reddit.com/r/LangChain/comments/1dsgbif/evaluate_different_llms_or_flows/) , 2024-07-02-0911
```
Question is self explanatory! Im looking for a workbench or way to evaluate different LLMs. For example giving score to 
answers, comparing prompts, giving good answer samples, etc etc

If it can show me the runs, the better so i can compare
.
```
---

     
 
all -  [ Review my resume - Recent Software Engineering Master graduate in NA ](https://www.reddit.com/r/resumes/comments/1ds8g7y/review_my_resume_recent_software_engineering/) , 2024-07-02-0911
```
[The censored information is from an NDA project.](https://preview.redd.it/s0hlbzio8r9d1.png?width=643&format=png&auto=w
ebp&s=9b4249b16ba854216ef753781d0bf0f9230a4c8b)


```
---

     
 
all -  [ Automated document filling - Need Suggestions ](https://www.reddit.com/r/LangChain/comments/1ds7h57/automated_document_filling_need_suggestions/) , 2024-07-02-0911
```
The input is going to be unfilled form images (imagine W2) and I want to fill it with fake relevant data. The current co
de I have uses a JSON config file containing the location of coordinates where the fake data needs to go and I just writ
e text on those fields with a white background. I use the faker library to generate fake data but I'm looking for someth
ing more accurate and relevant. Can I have some suggestions regarding what technologies I need to use to create such a f
orm generator?
```
---

     
 
all -  [ Integrating a Vector DB with Ollama/OpenWebUI for RAG ](https://www.reddit.com/r/LocalLLaMA/comments/1ds7fsg/integrating_a_vector_db_with_ollamaopenwebui_for/) , 2024-07-02-0911
```
Many youtube videos demonstrate RAG. Here are two examples:

[https://www.youtube.com/watch?v=jENqvjpkwmw](https://www.y
outube.com/watch?v=jENqvjpkwmw)

[https://www.youtube.com/watch?v=lig9c7OkxTI](https://www.youtube.com/watch?v=lig9c7Okx
TI)

These tutorials typically show the following process: Custom data (e.g. PDFs converted to text) is loaded using Lan
gchain. The texts are split into chunks, often with overlaps. Embeddings are generated using the nomic-embed-text model.
 These embeddings are stored as a vector database in ChromaDB. The system retrieves relevant information from the vector
 database based on the user's query.

These demonstrations usually run in the Python interpreter or Jupyter notebooks. M
y question: Is it possible to combine this process with Ollama and OpenWebUI? Specifically, I'd like to create the vecto
r database once and update it regularly (e.g. weekly) with new data. I want to use this vector database by default with 
every prompt in Ollama/OpenWebUI. Is such a setup feasible? If so, how could it be implemented? I envision creating the 
vector database manually, then showing Ollama where it's located. After that, Ollama would automatically use this vector
 database for every prompt.

I understand that in Ollama/OpenWebUI, one can click on the Documents button and select fil
es. However, my scenario involves a large number of diverse files, with new ones being added weekly. Therefore, it would
 be more efficient to have a vector database that can be continuously updated.
```
---

     
 
all -  [ Nocode ressource ](https://www.reddit.com/r/NoCodeJobs/comments/1ds5vbx/nocode_ressource/) , 2024-07-02-0911
```
Good Morning everyone,

We just launched an offshore no-code agency. We are currently working on LLM use cases through L
angchain. We can provide full-time resources starting from $350 since we are just beginning.

Happy to discuss further t
ogether 🙂
```
---

     
 
all -  [ I built a Github PR Agent with Autogen and 4 other frameworks, Here are my thoughts ](https://www.reddit.com/r/AutoGenAI/comments/1ds56y2/i_built_a_github_pr_agent_with_autogen_and_4/) , 2024-07-02-0911
```
The goal was to create an agent that would:  
1. Monitor a GitHub repository for new PRs  
2. Perform a code review on e
ach PR  
3. Post a summary of the review to a Slack channel

**Comparison**

* **AutoGen vs LangChain**: AutoGen excels 
in multi-agent conversations, while LangChain offers a broader toolkit for LLM applications. AutoGen required less boile
rplate for complex agent interactions in my projects.
* **AutoGen vs CrewAI**: AutoGen allows for more flexible, dynamic
 agent interactions. CrewAI is better suited for projects with predefined roles and structured workflows.
* **AutoGen vs
 LlamaIndex**: AutoGen focuses on agent interactions, while LlamaIndex specializes in data ingestion and retrieval. They
 can complement each other well in data-heavy projects.
* **AutoGen vs OpenAI library**: AutoGen provides a higher-level
 abstraction for multi-agent systems, simplifying the process compared to directly using theopenai library

https://prev
iew.redd.it/gt520z7cgq9d1.png?width=1442&format=png&auto=webp&s=d6107a7a8187a09143e06e152e7390c7f157742f

here's the lin
k for the autogen version: [https://git.new/pr-agent-autogen](https://git.new/pr-agent-autogen)

here's the link for oth
er versions: [https://git.new/pr-agent](https://git.new/pr-agent)
```
---

     
 
all -  [ Recommendation for table extraction ](https://www.reddit.com/r/LangChain/comments/1ds4rnu/recommendation_for_table_extraction/) , 2024-07-02-0911
```
I need the to extract table content (mainly numbers) from scanned documents. Those numbers are typed, not handwritten. T
he position and layout of the table can slightly change. What is currently the best open source model for that?
```
---

     
 
all -  [ Chat Model Class orthogonality suggestion ](https://www.reddit.com/r/LangChain/comments/1ds40ke/chat_model_class_orthogonality_suggestion/) , 2024-07-02-0911
```
Was writing some code that wanted to print the model string for a model without having a specific model.
Unfortunately, 
`BaseChatModel` does not have a `model` property.
Tried the set of alternatives used in my code at present, `Union[ChatO
penAI, ChatLiteLLM, ChatAnthropic]` and `ChatOpenAI` has no `model` property.
This kind of thing hurts langchain's abili
ty to paper over the differences between LLMs, which is its key strength.

I suggest a refactoring that promotes `model`
 up to the `BaseChatModel` and does something about `model` vs. `model_name` to make the latter both clearer in terms of
 its meaning (or simply an alias to the former, as it is in `ChatAnthropic` (see below). The following in `ChatLiteLLM` 
is not at all helpful:

    model_name: Optional[str] = None
    '''Model name to use.'''

As opposed to model name not 
to use?

`ChatAnthropic`:

    model: str = Field(alias='model_name')

It's ok if `model_name` is just and alias for bac
kwards compatibility, but on `ChatLiteLLM` the fact that it's `Optional` means that it might not be defined, which foils
 that purpose.
```
---

     
 
all -  [ When to use RunnableBranch and RunnableParallel ](https://www.reddit.com/r/LangChain/comments/1ds3ih5/when_to_use_runnablebranch_and_runnableparallel/) , 2024-07-02-0911
```
RunnableBranch and RunnableParallel , probably allow to lower api calls costs down, but I fail to see when they are trul
y needed. What's your experience with them? 
```
---

     
 
all -  [ Agents as a practical solution  ](https://www.reddit.com/r/LangChain/comments/1ds2f62/agents_as_a_practical_solution/) , 2024-07-02-0911
```
Hello there,

What practical applications for langchain based agents have you been having success with?

Of particular i
nterests, what foundational models have you been seeing perform best as agents? What size of datasets do you have it rea
soning through?

I’ve been building agents and chains for the past year. My lingering impression is that I won’t get age
nts involved in any real time chat use cases for performance reasons. I have been sticking to static lcel based chains b
ut they are nowhere near as capable. Tried streaming events back and updating the UI with backend status but - that isn’
t actually fixing anything 

Sincerely,
$corporate_employee 

```
---

     
 
all -  [ Langgraph 'License key is not valid' ](https://www.reddit.com/r/LangChain/comments/1ds1qal/langgraph_license_key_is_not_valid/) , 2024-07-02-0911
```
Looking for a solution for this problem.  [https://github.com/langchain-ai/chat-langchain/issues/339](https://github.com
/langchain-ai/chat-langchain/issues/339)

  
I checked-out chat-langchain from github.  I get the error that :

  
langg
raph-api-1       | ValueError: License key is not valid


```
---

     
 
all -  [ Langchain vs Llama Index (which one should I use?), Langchain vs Llama Index: Which one should you u ](https://www.reddit.com/r/chatgpt_newtech/comments/1drxd0s/langchain_vs_llama_index_which_one_should_i_use/) , 2024-07-02-0911
```
Langchain vs Llama Index (which one should I use?), Langchain vs Llama Index: Which one should you use?, How to Compare 
Multiple Large PDF Files Using AI (w/ Jerry Liu, Co-Founder of LlamaIndex) [https://aitutor21.com/aistudy/1045](https://
aitutor21.com/aistudy/1045)
```
---

     
 
all -  [ similarity search with relevancy score ](https://www.reddit.com/r/generativeAI/comments/1drub8s/similarity_search_with_relevancy_score/) , 2024-07-02-0911
```
# similarity search with relevancy score

1. I want to know is 'similarity search with relevancy score' and 'similarity 
search with score' same?

when i try to use similarity\_search\_with\_relevancy\_score(langchain), i get top 3 chunks ha
ving relevancy score.

but the answer lies in the chunk which has the least relevancy score. which is strange. should no
t be the chunk containing answer has the highest score? in spite of this i get the answer right every time
```
---

     
 
all -  [ Best way to extract user data from user response?  ](https://www.reddit.com/r/LocalLLaMA/comments/1drtok7/best_way_to_extract_user_data_from_user_response/) , 2024-07-02-0911
```
Lets say for example the user responds with: 

AI: What is your customer id? 

  
User: So the customer id is 'xyz'

  

we need to get the value as xyz 

  
I mean I get regex too but sometimes the semantics get a bit difficult so for examp
le if its 

  
AI: 'Confirm your date of birth?'

  
user: 'So I was born in January 4th 1994'

  
I would need '01/04/1
994'

  
So currently I have defined a function get\_value(user\_query->str, variable\_name->str, semantic\_description-
>str): that uses langchain output parsers and GPT 4o to parse the value and I store it in a variable, are there any quic
ker models or LLMs designed to parse for this use case? 
```
---

     
 
all -  [ What is the best LLM tech stack? ](https://www.reddit.com/r/LocalLLaMA/comments/1drofjk/what_is_the_best_llm_tech_stack/) , 2024-07-02-0911
```
Hi! So I'm currently building for a use case that requires the LLM to be securely fine tuned on large amounts of data an
d I would like to have an agentic workflow. Ease of development is a big This is the current stack I am thinking of usin
g but there are so many options that I feel a bit overwhelmed with the options. If you have any suggestions outside of t
he tools I listed please let me know!

Current Stack

1. Model (Need to fine-tune)
   1. LLama vs. OpenAI vs. Mistral?
2
. Framework for development
   1. LangChain vs. LlamaIndex?
3. Database to use
   1. Supabase
4. How to host and train t
he model
   1. RunPod
```
---

     
 
all -  [ UnstructuredExcelLoader() not working ](https://www.reddit.com/r/LangChain/comments/1drobcc/unstructuredexcelloader_not_working/) , 2024-07-02-0911
```
Has anyone used the UnstructuredExcelLoader() class to load xlsx file?

I am trying to load a simple one sheet Excel fil
e (.xlsx) using the function:

`from langchain.document_loaders import UnstructuredExcelLoader`  
`loader = Unstructured
ExcelLoader(file, mode='single', sheet_name = 'sheet1')`  
`docs = loader.load()`

  
however I received the following m
essage:

`IndexError: too many indices for array: array is 3-dimensional, but 25 were indexed`

`Not sure what is wrong.
 Any help is appreciated!`
```
---

     
 
all -  [ Add a message to a prompt or put a message in a pipeline? ](https://www.reddit.com/r/LangChain/comments/1drmqcy/add_a_message_to_a_prompt_or_put_a_message_in_a/) , 2024-07-02-0911
```
I'm confused by this use case: I made a `SystemMsg` and a `Prompt`, then I want to put them in a pipeline.  So I tried a
dding them, but you can't add a prompt and a message. So I tried making a `PipelinePromptTemplate`. That doesn't work, e
ither, since a `SystemMsg` is not a `Runnable`.  

This seems like something that should be very easy to do, but I'm stu
mped.  


I suppose I can just smash together the system prompt string and the Prompt string and then make a single temp
late, but it seems wrong that we have these classes that can't be composed.  Seems like adding a `Message` to a `PromptT
emplate` ought to give a `PromptTemplate`. Am I missing something?
```
---

     
 
all -  [ What are the advantages of using LangGraph? ](https://www.reddit.com/r/LangChain/comments/1drlvx1/what_are_the_advantages_of_using_langgraph/) , 2024-07-02-0911
```
Hello,
just a question that popped up in my mind.

I already developed a saas for serving agentic RAG to multiple custom
ers/companies using LangGraph and LangServe.

However, I'm developing a new application for agentic document analysis an
d parsing, all without using anything langchain related.

For the first project, I really wanted to learn a framework th
at was 'broadly' used, but now I want the agent to 'just work' and follow the steps in the process, and 'normal' if/else
 chains coupled with 'clever' prompting seem to work without getting into any of the intricacies of Langchain/LangGraph.


So, what do you think are the REAL advantages of using LangGraph? 
```
---

     
 
all -  [ Unexpected different results with OpenAI API.  ](https://www.reddit.com/r/OpenAI/comments/1dreitq/unexpected_different_results_with_openai_api/) , 2024-07-02-0911
```
Hello, Im developing a OpenAi + langchain application.

I've noticed that response quality is much worse when I deploy t
o a cloud provider. I've tried AWS on the US and GCP on US, Brazil and Chile.

Things like returning links dont work cor
rectly on the cloud and the answers give more errors in general.

Example of 1 simple question.

Question: Do you have M
eta Lava gloves?

Local (Correct Result): I recommend the Lava Meta gloves for $750. You can find them at this link: [ht
tps://gloves.com/shop/meta/lava-meta-flat/](https://gloves.com/shop/meta/lava-meta-flat/).

AWS US (wrong URL): The Meta
 Lava gloves are priced at $750. You can find them at this link: gloves.com/producto/meta-lava

GCP Chile (wrong URL): T
he Meta Lava gloves are priced at $750. You can find them at this link

Its not an issue with determination since respon
ses on local and cloud are very consistent. Im pretty sure everything else is exactly the same like temperature, api key
s, etc. I thought it could be an issue with jurisdiction but its the same no mater the cloud provider or region.


```
---

     
 
all -  [ How do I hide these long config logs and [GIN] messages in Ollama response ](https://www.reddit.com/r/ollama/comments/1drdvoh/how_do_i_hide_these_long_config_logs_and_gin/) , 2024-07-02-0911
```
Hello I am using Ollama with Langchain in Kaggle Notebook for the very first time and each time I run

    python 
    r
esult = llm.predict_messages(messages)
    print(result.content)

for the very first output, it gives long logs shown in
 the first picture. And produces the output. And then for each subsequent output, it prepends the response something lik
e this `[GIN] 2024/06/29 - 14:46:20 | 200 | 9.925493989s |` [`127.0.0.1`](http://127.0.0.1) `| POST '/api/chat'`. 

Sinc
e I am trying to create a chatbot for my students, I don't want to overwhelm such unnecessary long logs. Can anyone plea
se help to remove or hide these from the bot response?

[Ollama Long Logss in Kaggle](https://preview.redd.it/p2vt5jlf5j
9d1.png?width=1811&format=png&auto=webp&s=abb3286d47d7819bc2e9745e82dc8459583d059c)


```
---

     
 
all -  [ Updating React Context with LangGraph ](https://www.reddit.com/r/LangChain/comments/1drcw11/updating_react_context_with_langgraph/) , 2024-07-02-0911
```
Hi everyone. Sorry if this question doesn't make sense. I'm making an application where I'm using a GoogleMap component 
in react on the front-end and LangGraph for my LLM Agent. Here's the workflow I'm trying to achieve

User asks a questio
n -> Depending on the question, Agent updates GoogleMap context -> Map changes (Depending on tool)

I created my GoogleM
ap react context and used the hook inside of the Agent tool function to update state. TS throws an error saying I should
n't be updating state from the server \[ addPinpoint() is a function that updates array state on my GoogleMap component.
 This array is then mapped to reflect changes \] Is there a way in LangGraph to resolve something like this? Thanks in a
dvance and apologies if this is a noob question.

Code:

    export const pinpointTool = new DynamicStructuredTool({
   
     name: 'pinpointTool',
        description: 
        'A tool for placing pinpoints on the map, given a specific addr
ess, which includes Street, City, State, and Country. If you want to show a user a location, use this tool by passing in
 the address of the location',
        schema: pinpointSchema,
        func: async ( input ) => {
            const { la
t, lng } = await fetchCoordinates(input)
            const { addPinpoint } = useMap(); 
            addPinpoint(lat, lng
)
            return 'Pinpoints Placed'
        }
    })
```
---

     
 
all -  [ AI Gateways: The Missing Block in the AI puzzle ](https://www.reddit.com/r/LangChain/comments/1dr8css/ai_gateways_the_missing_block_in_the_ai_puzzle/) , 2024-07-02-0911
```
Hey everyone, I've just published a new post diving into AI gateways, offering a birds-eye view from 50,000 feet.

Check
 it out here: [AI Gateways: The Missing Block in the AI puzzle](https://open.substack.com/pub/siddharthsambharia/p/ai-ga
teways-the-missing-block-in?r=en8oy&utm_campaign=post&utm_medium=web&showWelcomeOnShare=true)

I'd love to hear your tho
ughts and any questions you might have.

If you're interested in exploring a lightweight open-source AI Gateway connecti
ng 100+ LLMs, consider checking out Portkey AI
```
---

     
 
MachineLearning -  [ [P] Seeking Feedback on My GenAI Job Fit Project - New to LangChain/LangGraph ](https://www.reddit.com/r/MachineLearning/comments/1dgns9p/p_seeking_feedback_on_my_genai_job_fit_project/) , 2024-07-02-0911
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

     
 
MachineLearning -  [ [P] I'm tired of LangChain, so I made a simple open-source alternative with support for tool using a ](https://www.reddit.com/r/MachineLearning/comments/1deffo8/p_im_tired_of_langchain_so_i_made_a_simple/) , 2024-07-02-0911
```
[https://github.com/piEsposito/tiny-ai-client](https://github.com/piEsposito/tiny-ai-client)

The motivation for buildin
g tiny-ai-client comes from a frustration with Langchain, that became bloated, hard to use and poorly documented - and t
akes inspiraton from [simpleaichat](https://github.com/minimaxir/simpleaichat/tree/main), but adds support to vision, to
ols and more LLM providers aside from OpenAI (Gemini, Anthropic - with Groq and Mistral on the pipeline.)

I'm building 
this to to continue what simpleaichat started and not to ride on hype, raise money or whatever, but to help people do 2 
things: build AI apps as easily as possible and switching LLMs without needing to use Langchain.

This is a minimally vi
able version of the package, with support to vision, tools and async calls. There are a lot of improvements to be done, 
but even at its current state, tiny-ai-client has generally improved my interactions with LLMs and has been used in prod
uction with success.

Let me know what you think: there are still a few bugs that may need fixing, but all the examples 
work and are easy to be be adapted to your use case.
```
---

     
 
MachineLearning -  [ [P] Superfast RAG: Langchain Streaming and Groq ](https://www.reddit.com/r/MachineLearning/comments/1d5s9g4/p_superfast_rag_langchain_streaming_and_groq/) , 2024-07-02-0911
```
  
Fast LLM RAG inference using Groq and Langchain Streaming.  
  
Groq is introducing a new, simpler processing archite
cture designed specifically for the performance requirements of machine learning applications and other compute-intensiv
e workloads. The simpler hardware also saves developer resources by eliminating the need for profiling, and also makes i
t easier to deploy AI solutions at scale.  
  
Resource: [https://www.youtube.com/watch?v=frMdOL8knqg](https://www.youtu
be.com/watch?v=frMdOL8knqg)
```
---

     
 
deeplearning -  [ Llama 3 not running on GPU ](https://www.reddit.com/r/deeplearning/comments/1dptxsr/llama_3_not_running_on_gpu/) , 2024-07-02-0911
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

     
 
deeplearning -  [ What is ReAct Prompting? the most important piece in agentic frameworks ](https://www.reddit.com/gallery/1djk4nk) , 2024-07-02-0911
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

     
 
deeplearning -  [ How to finetune? ](https://www.reddit.com/r/deeplearning/comments/1daio0h/how_to_finetune/) , 2024-07-02-0911
```
Can someone guide me to some resource how can I finetune an open source llm or some library (like langchain) on unstruct
ured data (example: news articles on cricket) So that model can answer a question (like When did India won world Cup?)
```
---

     
