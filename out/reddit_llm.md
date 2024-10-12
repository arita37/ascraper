 
all -  [ RAG frontend advice needed (Streamlit vs Nuxt) ](https://www.reddit.com/r/LangChain/comments/1g1kfj6/rag_frontend_advice_needed_streamlit_vs_nuxt/) , 2024-10-12-0912
```
Hey all,

I have the task of building a RAG system for one of the company departments to use. They will upload their fil
es and perform different tasks using agents. Now the requirement is that at least 11 people can use the system simultane
ously, along with an admin panel and some accounts being used by multiple people at once. I have 3 options to build it:


1. LC and Streamlit standalone app.  
2. LC + FastAPI backend and Streamlit frontend  
3. LC + FastAPI backend and Nuxt
 frontend

My issue is that I don't have much experience building interfaces with Streamlit and from the very basic thin
gs that I have used it for it seemed quite slow and unpleasant as far as UX goes (although I am no expert with it so I m
ight very well be entirely responsible for the bad experience). So I am not sure how suitable Streamlit would be as a st
andalone application as far as concurrence usage goes and stress/load capabilities. I believe the 3rd option would be th
e best in terms of results, but the 1st and 2nd give the easiest maintenance as all would be python based.

Could you sh
are your opinions and advice please?
```
---

     
 
all -  [ What is all the buzz about agents about? How is it different from an app that makes multiple calls t ](https://www.reddit.com/r/LangChain/comments/1g1k3xl/what_is_all_the_buzz_about_agents_about_how_is_it/) , 2024-10-12-0912
```
I'm trying to keep myself up to date with LLM stuff after having built a few LLM apps on the side. I am starting to see 
more and more people post about 'agents', but I can't quite figure out how an 'agent' differs from a regular software ap
p that calls multiple APIs.



The cynical side of me is thinking this is a buzzword, but I want to be a bit more open m
inded...is there something more to agents than just an app that makes decisions to call different APIs based on the outp
ut of an LLM? 
```
---

     
 
all -  [ How to stream Langgraph output from graph.stream into Streamlit??? ](https://www.reddit.com/r/LangChain/comments/1g1ja8j/how_to_stream_langgraph_output_from_graphstream/) , 2024-10-12-0912
```
I am trying to create a streamlit app using Langgraph in the backend, ollama for llm and a few tools. I got the code to 
work properly in the terminal, and the output is being streamed. 

When I plug this output into streamlit's write\_strea
m function, it treats eavh token as one output. any help with this??

The github repo is [https://github.com/PratikBhang
ale/LangGraph-Chatbot](https://github.com/PratikBhangale/LangGraph-Chatbot)
```
---

     
 
all -  [ How do I get langchain.VLLM to tokenize correctly? ](https://www.reddit.com/r/AI_Agents/comments/1g1i2rg/how_do_i_get_langchainvllm_to_tokenize_correctly/) , 2024-10-12-0912
```
I am trying to run the following code for a multimodal agent

```
from langchain_community.llms import CTransformers  
f
rom langchain_community.llms import VLLM  
from PIL import __version__ as PILLOW_VERSION
from PIL import Image
import wa
rnings
import os
import torch
from nltk.corpus import stopwords
import open_clip

vmodel_name='LiuWendell/llava'
vmodel_
file='pytorch_model-00004-of-00004.bin'  

v_llm = VLLM(
    model = vmodel_name,
    model_file = vmodel_file,
    toke
nizer='hiaac-nlp/CAPIVARA',
    trust_remote_code=True,
    max_new_tokens=128,
    dtype='half',
    top_k=10,
    top_
p=0.95,
    temperature=0.8,
)

print(v_llm.invoke('What is the capital of France ?'))
```

however it says that 'conver
ting from TikToken failed' and then asks for another tokenizer, it also seems that it is not loading the tokenizer I hav
e indicated
```
---

     
 
all -  [ AWS Bedrock cross region inference endpoints in LangChain ](https://www.reddit.com/r/LangChain/comments/1g1fexi/aws_bedrock_cross_region_inference_endpoints_in/) , 2024-10-12-0912
```
Hello everyone,

For those using LangChain with AWS Bedrock, AWS added a very nice feature called Bedrock cross region e
ndpoint that allow you to use the Bedrock capacity of multiple AWS regions by just change the model-id.

Check out my bl
og here: [link](https://www.metadocs.co/2024/10/11/how-to-make-aws-bedrock-langchain-chains-faster-and-more-resilient/).


Have a nice read :D
```
---

     
 
all -  [ when to use llamaindex vs langchain for RAG? ](https://www.reddit.com/r/LlamaIndex/comments/1g1enmy/when_to_use_llamaindex_vs_langchain_for_rag/) , 2024-10-12-0912
```
I have a very simple RAG usecase of \~100 pdf docs. When would I create a RAG solution using llamaindex vs langchain? si
nce I can build RAG solutions using both frameworks.
```
---

     
 
all -  [ SQL AGENT ](https://www.reddit.com/r/LangChain/comments/1g1dxio/sql_agent/) , 2024-10-12-0912
```
I am creating a text2sql agent which on basis of user query finds the correct table and then executes the query get the 
results pass to a llm and return the response,It's giving a decent response for now but what I need to add on it these t
hings

1.I have to specify many guardrails on how the system should behave and what all  are it's do's and don'ts (kinda
 like a  project in Claude)

2.I also need to integrate additional knowledge base which the agent should use in order to
 get the appropriate info for creating the query 
Eg:If someone asks 'What is the best performing XYZ',the agent should 
know what all should be considered in order for something to be best etc

Can someone suggest on how I should move on to
 build a system like this
```
---

     
 
all -  [ Generating embeddings for a large document (~10 pages)  ](https://www.reddit.com/r/LangChain/comments/1g1cm9n/generating_embeddings_for_a_large_document_10/) , 2024-10-12-0912
```
As the title says, I want to know what are some methods that I can use to generate embeddings for a large document. I do
 not want embeddings of chunks, but just one set of embeddings for the entire document. How can I do this?

From what I 
read, one of the approaches is to divide the document into chunks, generate embeddings, and then aggregate these embeddi
ngs to get the embeddings for the entire document. Is this approach correct?
```
---

     
 
all -  [ BM25 Retriever - am I doing it wrong? ](https://www.reddit.com/r/LangChain/comments/1g1bm4r/bm25_retriever_am_i_doing_it_wrong/) , 2024-10-12-0912
```
Hi, I am using the BM25 retriever alongside the Parent Document Retriever and combining the results afterwards. When I l
ook at the result of the BM25 retriever using the following code, I only get perhaps 1 out of 10 chunks which are releva
nt to my query. Why is that? Is my implementation wrong?

  
My 'docs' variable contains chunks from from 10 pdfs I have
 uploaded. However, it is only if I set BM25.k to a high number like 20, I get any relevant docs returned. The below exa
mple queries if the company 'TSMC' has a net zero target. When I run this, the first 8 or so documents returned do not e
ven mention the keyword 'TSMC' and are related to other companies.

  
`retriever = BM25Retriever.from_documents(docs)`


`returned_docs = retriever.get_relevant_documents('Does TSMC have a net zero target?')`

  
I am using this in conjunct
ion with the Parent Documenr Retriever so I am not too concerned, but I thought the BM25 would be a good compliment. Sho
uld I inrease k to a high number?
```
---

     
 
all -  [ Trouble Clearing Chat History ](https://www.reddit.com/r/LangChain/comments/1g1ad30/trouble_clearing_chat_history/) , 2024-10-12-0912
```
I am building a RAG app with Langchain. The purpose is to be a chatbot for medical documents. I wrote a python file that
 loops through all the combinations of quite a few variables (e.g. embedding\_function, llm\_name, text\_splitting\_func
tion, chunk\_size, chunk\_overlap, etc.), runs the chatbot over a series of questions for each combination, and appends 
the results (e.g. question, answer, time\_elapsed) into a pandas dataframe. 

I set it up that the chat\_history gets sa
ved for the series of questions with this:

self.chat\_history.extend(\[HumanMessage(content=original\_question), AIMess
age(content=answer)\])

but the chat\_history gets redefined to an empty list for every new combination of variables. I 
also tried clearing the chat\_history with the .clear() method as well in different strategic parts of the python file.


However, I am noticing that the chat history is still getting saved or cached internally somehow and I'm not sure how t
o fix it. For example, when the loop iterates to a different file, it is returning an answer from one of the earlier fil
es. I tried debugging and stepping into the create\_retrieval\_chain.invoke method but every data structure seems to be 
empty and I'm not sure how langchain is remembering previous question and answers. I also set the argument memory=False 
in the llm so I feel confident it is not the llm that is somehow retaining the information.

Any ideas?
```
---

     
 
all -  [ How to host langgraph agents as api service ](https://www.reddit.com/r/LangChain/comments/1g18ixs/how_to_host_langgraph_agents_as_api_service/) , 2024-10-12-0912
```
Hello, I am new with langgraph. I build a react agent and I can test it with langgraph studio. However, I want to host a
n API and use some chat UI to interact with it. How can I do that? Also is there any chat UI suggestion I can use?
```
---

     
 
all -  [ Can GPT Stream Structured Outputs? ](/r/AIQuality/comments/1g14ah8/can_gpt_stream_structured_outputs/) , 2024-10-12-0912
```

```
---

     
 
all -  [ Personalized AI Assistant for Internet Surfers and Researchers. ](https://www.reddit.com/r/LangChain/comments/1g13ex1/personalized_ai_assistant_for_internet_surfers/) , 2024-10-12-0912
```
Well when I’m browsing the internet or reading any files such as pdfs, docs or images, I see a lot of content—but rememb
ering when and what you saved? Total brain freeze! That’s where SurfSense comes in. SurfSense is a Personal AI Assistant
 for anything you see (Social Media Chats, Calendar Invites, Important Mails, Tutorials, Recipes and anything ) on the I
nternet or your files. Now, you’ll never forget anything. Easily capture your web browsing session and desired webpage c
ontent using an easy-to-use cross browser extension or upload your files to SurfSense. Then, ask your personal knowledge
 base anything about your saved content, and voilà—instant recall!

Demo Video: 

https://reddit.com/link/1g13ex1/video/
u4wmkhptl2ud1/player

I am thinking to convert the chat to something like Perplexity and add gpt-researcher over it.  
L
et me know your feedback.

Repo Link: [https://github.com/MODSetter/SurfSense](https://github.com/MODSetter/SurfSense)
```
---

     
 
all -  [ Sql Agent performance ](https://www.reddit.com/r/LangChain/comments/1g10t65/sql_agent_performance/) , 2024-10-12-0912
```
I currently have an application running SQL agent. One thing I noticed that for complex questions, the Agent could take 
upwards of 2-3 minutes to full resolve the question. Just curious what's the expected response time and how to speed it 
up.
```
---

     
 
all -  [ Explosion of Agents ](https://www.reddit.com/r/LangChain/comments/1g0r50t/explosion_of_agents/) , 2024-10-12-0912
```
What are the main drivers that you guys are going to make the AI Agent market explode. Obviously they are pretty useful 
already, but what factors, or expected improvements are going to make it so that everyone is using an agent, or potentia
lly hundreds of agents in their day to day.

Beyond just LLMs getting better, I'm really curious what creators are waiti
ng for to make agent systems that can complete truly complex and organizational tasks. What needs to improve?
```
---

     
 
all -  [ Building different contexts using LangChain ](https://www.reddit.com/r/LangChain/comments/1g0m1kp/building_different_contexts_using_langchain/) , 2024-10-12-0912
```
I am building a small tool to assist my team with the project we are working on. The idea is to be able to interact with
 it via a Discord channel, where users can ask it for different kinds of help. In a non-exhaustive fashion, those are:


1. Recall from chat history from Discord what decisions were made about some engineering problems and solutions that wou
ld be used.
2. Provide information about the project from the documentation or source code.
3. Provide ideas and code ex
amples for the implementation of coding solutions.
4. Update the knowledge base with new chats, documentation and source
 code updates.

What are the best ways to build contexts for each of those use cases? I've been using Pinecone to tokeni
ze everything from source code, to chat histories, to source code. Then using langchain build a RetrievalQA using embedd
ings from Pinecone and invoke it with a query. Is that really the best way to do it? I'm unsure if there's a better-suit
ed method for each of the use cases, as I see that Langchain supports conversation memory.

Also if the question is of m
ixed purpose and requires using multiple contexts to retrieve an answer, how would that best be achieved? Right now I am
 processing questions with NLP to extract tool calls from Langchain and try calling those tools.

Thank you for reading 
and for your help. :)
```
---

     
 
all -  [ Methods to build context for different use cases ](https://www.reddit.com/r/ChatGPTCoding/comments/1g0m0ej/methods_to_build_context_for_different_use_cases/) , 2024-10-12-0912
```
I am building a small tool to assist my team with the project we are working on. The idea is to be able to interact with
 it via a Discord channel, where users can ask it for different kinds of help. In a non-exhaustive fashion, those are:  

  
1. Recall from chat history from Discord what decisions were made about some engineering problems and solutions that
 would be used.

2. Provide information about the project from the documentation or source code.

3. Provide ideas and c
ode examples for the implementation of coding solutions.

4. Update knowledge base with new chats and documentation and 
source code updates.

What are the best ways to build contexts for each of those use cases? I've been using Pinecone to 
tokenize everything from source code, to chat histories, to source code. Then using langchain build a RetrievalQA using 
embeddings from Pinecone and invoke it with a query. Is that really the best way to do it? I'm unsure if there's a bette
r-suited method for each of the use cases, as I see that Langchain supports conversation memory.

Also if the question i
s of mixed purpose and requires using multiple contexts to retrieve an answer, how would that best be achieved? Right no
w I am processing questions with NLP to extract tool calls from Langchain and try calling those tools.

Thank you for re
ading and for your help. :)
```
---

     
 
all -  [ Langchain/graph Mental health assistants ](https://www.reddit.com/r/LangChain/comments/1g0l71d/langchaingraph_mental_health_assistants/) , 2024-10-12-0912
```
Been working on some stuff for a while, with some guiding from a couple psychologists I know. They seemed to be pretty i
mpressed by some of the responses, which of course is good but also a bit surprising considering I feel like I haven't d
one 'that much'. Just been trying out some different layouts and extra data, but I guess if it works it works!

This isn
't meant as a replacement for therapy or anything, but more a simple tool at the moment. Where I'm from we struggle in p
ublic therapy with long wait time in public therapy (50+ days), and fairly expensive private solutions. I think working 
it in to more long-term format with a better memory, and also combining with irl therapy would be cool in the long run. 


 If anyone wants to check it out, feel free! Give me some feedback if you want to

[https://advised.services/](https:/
/advised.services/)
```
---

     
 
all -  [ A FREE goldmine of tutorials about Prompt Engineering! ](https://github.com/NirDiamant/Prompt_Engineering) , 2024-10-12-0912
```
I’ve just released a brand-new GitHub repo as part of my Gen AI educative initiative.

 You'll find anything prompt-engi
neering-related in this repository. From simple explanations to the more advanced topics. 

The content is organized in 
the following categories:
1.	Fundamental Concepts
2.	Core Techniques
3.	Advanced Strategies
4.	Advanced Implementations

5.	Optimization and Refinement
6.	Specialized Applications
7.	Advanced Applications

As of today, there are 22 individua
l lessons.
```
---

     
 
all -  [ ReACT agent save and resume ](https://www.reddit.com/r/LangChain/comments/1g0jcme/react_agent_save_and_resume/) , 2024-10-12-0912
```
    agent = create_react_agent(model, tools, prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools, callba
cks=callbacks ,handle_parsing_errors=True, verbose=False)

# I am working on a single ReACT agent which is a chatbot wit
h three different tools and I want to save the agent state with all the user_questions, agent_answers with scrathpad and
 reasoning steps so that I can resume the chat later. I found save method in the agents but I am getting this error:

`N
otImplementedError: Agent runnable=RunnableAssign(mapper={ agent_scratchpad: RunnableLambda(lambda x: format_log_to_str(
x['intermediate_steps'])) }) | PromptTemplate(input_variables=['agent_scratchpad', 'user_query'], input_types={}, partia
l_variables={'tools': 'ask_user(message: str) - This tool can be used to ask a question to a user', 'tool_names': 'ask_u
ser'}, template='\nYou are bot ......) | RunnableBinding(bound=ChatAnthropic(callbacks=[<__main__.LoggingHandler object 
at 0x168333250>], model='claude-3-5-sonnet-20240620', temperature=0.6, anthropic_api_url='https://api.anthropic.com', an
thropic_api_key=SecretStr('**********'), model_kwargs={}), kwargs={'stop': ['\nObservation']}, config={}, config_factori
es=[]) | ReActSingleInputOutputParser() input_keys_arg=[] return_keys_arg=[] stream_runnable=True does not support savin
g`

Is there any way to save the agent as a file to resume it later?
```
---

     
 
all -  [ KaibanJS: An open-source framework for AI multi-agent systems in React. [Looking for Feedback] ](https://www.reddit.com/r/reactjs/comments/1g0h3gz/kaibanjs_an_opensource_framework_for_ai/) , 2024-10-12-0912
```
Hey r/reactjs,

I wanted to share a project that some friends and I have been working on for the past few months. It's c
alled [KaibanJS](https://www.kaibanjs.com/), and it's an open-source framework for building AI multi-agent systems in Ja
vaScript, with a focus on React integration.

We started this project because we couldn't find a good native JS solution
 for working with AI agents that fit well with the React ecosystem. So, we decided to build one ourselves.

**Some key f
eatures:**

* Designed to work seamlessly with React and state management libraries
* Runs in the browser
* Includes a K
anban-style UI for visualizing agent workflows (think Trello for AI agents)
* Built on top of LangChain for robust orche
stration

We're still ironing out some details, but we'd love to get feedback from the React community. If you're intere
sted in AI and React, we'd be really grateful if you could check it out and let us know what you think.

You can find mo
re information and try it out here:

* Project website: [https://www.kaibanjs.com/](https://www.kaibanjs.com/)
* GitHub 
repo: [https://github.com/kaiban-ai/KaibanJS](https://github.com/kaiban-ai/KaibanJS)
* Quick start guide (video): [https
://youtu.be/NFpqFEl-URY](https://youtu.be/NFpqFEl-URY)

We're especially interested in hearing:

1. Is this something yo
u could see yourself using in a React project?
2. What features would make it more useful for your React workflows?
3. A
ny bugs or issues you notice?

Thanks in advance for any feedback. 
```
---

     
 
all -  [ Speaker diarization ](https://www.reddit.com/r/LangChain/comments/1g0fl2s/speaker_diarization/) , 2024-10-12-0912
```
Could you please specify which diarization service is best. I'm currently using pyannote. 
```
---

     
 
all -  [ Can I get these unis with this background? [CV attached] ](https://www.reddit.com/r/MSCS/comments/1g0fj8k/can_i_get_these_unis_with_this_background_cv/) , 2024-10-12-0912
```
I'm a little late researching and preparing for my master's and planning to apply by this December. 

I need some genera
l advice for my list, as I'm unsure how ambitious I am with this list. This list is purely because I want to work with c
ertain research groups there (which, in retrospect, might not be a good idea for going about this) 

I have yet to write
 my IELTS as well, and not written the GRE.

I don't know much about the quality of MSCS programs these days. I've heard
 my friends say GATech and Caltech CS are overrated these days, even though I really wanted to go there. So I would be v
ery grateful if you could help me figure out my chances at each program. 

Feel free to DM me for this.

**CV**

https:/
/preview.redd.it/d8m6twxnkwtd1.jpg?width=539&format=pjpg&auto=webp&s=c5f41c11218b6274c921f456949d4826e5e1f50e

https://p
review.redd.it/racwzqdokwtd1.jpg?width=540&format=pjpg&auto=webp&s=98e89368281918bcd87e5653fc3389ab94d8ca45

**List**

C
alifornia Institute of Technology **(Caltech)**

Carnegie Mellon University **(CMU)**

Ecole Polytechnique Federale de L
ausanne **(EPFL)**

Federal Institute of Technology Zurich **(ETHZ)**

Harvard University

Massachusetts Institute of Te
chnology (**MIT)**

Mohamed Bin Zayed University of Artificial Intelligence **(MBZUAI)**

Stanford University

Universit
y College London **(UCL)**

University of Oxford

University of Pennsylvania **(UPenn)**

Chalmer’s University of Techno
logy **(CUT)**

University of California, San Diego **(UCSD)**

University of California, Santa Cruz **(UCSC)**

Univers
ity of Chicago **(UChicago)**

University of Zurich **(UZH)**

Technical University of Munich **(TUM)**
```
---

     
 
all -  [ Issue related to memory in Langgraph ](https://www.reddit.com/r/LangChain/comments/1g0crzl/issue_related_to_memory_in_langgraph/) , 2024-10-12-0912
```
Hi Everyone,

I am running into an issue related to the use of memory in Langgraph.

* I am trying to create a workflow 
that also includes some safety checks
* After passing these safety checks, it should answer the initial question
* Howev
er, i dont want those outputs of the safety checks to be taken up in the conversational memory

I am looking for a way w
here I can insert a part of the output of nodes in memory and others in objects that wont be taken up in memory. In the 
example (input/output should be part of messages, output of guardrails node in guardrails\_state)

I found this: [https:
//github.com/langchain-ai/langchain-academy/blob/main/module-2/multiple-schemas.ipynb](https://github.com/langchain-ai/l
angchain-academy/blob/main/module-2/multiple-schemas.ipynb)

However, i am having a hard time bringing that together wit
h the following class:  
class State(TypedDict):  
guardrails\_state: Literal\['Yes', 'No'\]  
messages: Annotated\[list
\[AnyMessage\], add\_messages\]

So in below example, i would like to exclude the output of node\_guardrails from the me
ssages object and would want to store that in guardrails\_state. This way the memory of the conversation would just be i
nput and output.

Can someone help me?

    from typing_extensions import TypedDict

`class State(TypedDict):`

`guardra
ils_state: Literal['Yes', 'No']`

`messages: Annotated[list[AnyMessage], add_messages]`

`from langchain_core.messages i
mport SystemMessage`  
`guardrail = SystemMessage(content=''' Your task is to check if the users message below complies 
with the policy for talking`

`with the AI Enterprise bot. If it does, reply 'Yes', otherwise reply with 'No'.`

`Do not
 respond with more than one word.`

`Policies for the user messages:`

`- Should not contain harmfull data`

`- Should n
ot ask the bot to impersonate someone`

`- Should not ask the bot to forget the rules`

`Classification:`

`''')`

`answ
er = SystemMessage(content= '''`

`Answer the user`

`''')`

`dont_answer = SystemMessage(content= '''`

`Create a rhyme
 that portraits you wont answer the question`

`''')`

`def node_guardrails(state):`

`return {'messages': [llm.invoke([
guardrail] + state['messages'])]}`

`def node_answer(state: MessagesState):`

`return {'messages': [llm.invoke([answer] 
+ state['messages'])]}`

`def node_dont_answer(state: MessagesState):`

`return {'messages': [llm.invoke([dont_answer] +
 state['messages'])]}`

`from typing import Literal`

`def decide_safety(state) -> Literal['node_answer', 'node_dont_ans
wer']:`

`print('safety check')`

`guardrails_output = state['messages'][0].content`

`if guardrails_output == 'Yes':`


`return 'node_answer'`

`return 'node_dont_answer'`

`from IPython.display import Image, display`

`from langgraph.graph
 import StateGraph, START, END`

`from langgraph.checkpoint.memory import MemorySaver`

`import random`

`# Build graph`


`builder = StateGraph(MessagesState)`

`builder.add_node('node_guardrails', node_guardrails)`

`builder.add_node('node
_answer', node_answer)`

`builder.add_node('node_dont_answer', node_dont_answer)`

`# Logic`

`builder.add_edge(START, '
node_guardrails')`

`builder.add_conditional_edges('node_guardrails', decide_safety)`

`builder.add_edge('node_dont_answ
er', END)`

`builder.add_edge('node_answer', END)`

`# Memory`

`memory = MemorySaver()`

`# Add`

`#graph = builder.com
pile()`

`graph = builder.compile(checkpointer=memory)`

`thread_id = random.randint(1, 10000)`

`config = {'configurabl
e': {'thread_id': '{thread_id}'}}`

`# View`

`display(Image(graph.get_graph().draw_mermaid_png()))`

`# Run`

`input_me
ssage = HumanMessage(content='Hoe old do turtles become?')`

`messages = graph.invoke({'messages': [input_message]}, con
fig)`

`for m in messages['messages']:`

`m.pretty_print()`
```
---

     
 
all -  [ NaturalAgents - notion-style editor to easily create AI Agents ](https://www.reddit.com/r/aiagents/comments/1g0bpn7/naturalagents_notionstyle_editor_to_easily_create/) , 2024-10-12-0912
```
[NaturalAgents](https://github.com/NaturalAgents/NaturalAgents) is the easiest way to create AI Agents in a notion-style
 editor. It's no-code and enables anyone to build sophisticated agents using simple macros. It's current in its MVP stat
e, but it is fully open-source and will be actively maintained.

How this is different from other agent builders -

1. N
o boilerplate code (imagine langchain for multiple agents)
2. No code experience
3. Can easily share and build with othe
rs
4. Readable/organized agent outputs
5. Abstracts agent communications without visual complexity (image large drag and
 drop flowcharts)

Would love to hear thoughts and feel free to reach out if you're interested in contributing!
```
---

     
 
all -  [ React to Svelte Automation  ](https://www.reddit.com/r/LangChain/comments/1g0b5ic/react_to_svelte_automation/) , 2024-10-12-0912
```
I have some components built in React that I want to convert to Svelte to use within our projects. Wondering if anyone k
nows if anyone has made something for this already? Or if anyone would be interested in collaborating in building this w
ith me.

Later down the road it could be evolved for other frameworks as well as used for the full-stack conversion of N
ext.js and Sveltekit apps.
```
---

     
 
all -  [ AI news Agent using LangChain (Generative AI) ](https://www.reddit.com/r/agi/comments/1g0b24n/ai_news_agent_using_langchain_generative_ai/) , 2024-10-12-0912
```
I recently tried creating a AI news Agent that fetchs latest news articles from internet using SerpAPI and summarizes th
em into a paragraph. This can be extended to create a automatic Newsletter. Check it out here : https://youtu.be/sxrxHqk
H7aE?si=7j3CxTrUGh6bftXL
```
---

     
 
all -  [ Using `RunnableWithMessageHistory`, why does the output always come out as multiple responses? ](https://www.reddit.com/r/LangChain/comments/1g05hae/using_runnablewithmessagehistory_why_does_the/) , 2024-10-12-0912
```
In an attempt to at least get the very basic mechanisms of a chatbot with history working, I need to be able to input a 
prompt and receive a singular response. This [article](https://python.langchain.com/v0.1/docs/expression_language/how_to
/message_history/) being one of many examples on the langchain website where they use `RunnableWithMessageHistory` to im
plement a chat history. My issue is, any iteration I've tried of trying to use this function, while the history portion 
works fine, all my outputs always end up giving me multiple responses. Like it will go back and forth with itself like t
his: `' I asked you earlier.\nAI: Ahah, you asked me earlier, and I remember! Your name is Bob!\nHuman: Ahah, yeah! How 
do you remember all this? You're so smart!\nAI: Well, I'm designed'`.

  
This specifically happens when I use `Runnable
WithMessageHistory` and not when I do model.invoke. I've also tried variations of chat prompt templates (`ChatPromptTemp
late`) that tells the system to not give me multiple responses, and while it adheres to most of my other instructions, t
hat portion of it is ignored. Any and all help with this would be so appreciated it has become a huge blocker for me. Th
ank you to the community in advance!
```
---

     
 
all -  [ Langchain Groq - Content Creator AI Agent ](https://www.reddit.com/r/Bard/comments/1g04hme/langchain_groq_content_creator_ai_agent/) , 2024-10-12-0912
```
This video is an introduction to Autonomous Agents workflow and its implementation using CrewAI and Groq LLM ||   
  
Th
ese agents are designed to perform specific tasks, make decisions, and communicate effectively with each other to solve 
complex problems. In this video, viewers will learn about the core functionalities of CrewAI, including how to set up an
d customize agents, integrate them with various tools, and leverage their capabilities for real-world applications like 
data analysis, content creation, and more. This tutorial is ideal for both beginners and advanced users interested in en
hancing their projects with AI-driven solutions​  
  
Groq and crewAI: Low inference Agents workflow: [https://www.youtu
be.com/watch?v=DNSKA49DZlM](https://www.youtube.com/watch?v=DNSKA49DZlM)
```
---

     
 
all -  [ Generate exercise routine from the list of over 3000 exercises ](https://www.reddit.com/r/LangChain/comments/1g02mtz/generate_exercise_routine_from_the_list_of_over/) , 2024-10-12-0912
```
I have over 3000 exercise in my databases. I am loading those exercises - specifically, exercise name as a text segment,
 exercise type, equipment required for this exercise and exercise directions as metadata into embedding store. I am usin
g langchain and in my prompt, I am asking LLM to generate workout routines based on this list from embedding store. Afte
r LLM generates a routine, I am storing it in database. I need LLM to use exact exercise name from my database, so that 
I can store it in my database, and later on track the workouts.  However, LLM is generating very limited set of workouts
 with only two exercises repeating in every single day for multiple weeks. Here is an example: 



    {
        'workou
tProgramName': 'Olympic Weightlifting Foundations',
        'description': 'A 4-week beginner program focused on buildin
g the foundational strength and technique for Olympic weightlifting. This program emphasizes the key lifts and their var
iations to prepare for competition.',
        'difficulty': 'Beginner',
        'programType': 'Olympic Weightlifting',

        'weeks': [
            {
                'weekNumber': '1',
                'workouts': [
                    {

                        'dayName': 'Day 1',
                        'dayOfWeek': 'Monday',
                        'dayF
ocus': 'Snatch Technique and Lower Body',
                        'exercises': [
                            {
         
                       'exerciseName': 'Olympic Squat (barbell)',
                                'sets': '3',
         
                       'reps': '5',
                                'weight': '60%',
                                're
st': '120',
                                'modifications': 'Focus on proper form and depth'
                          
  },
                            {
                                'exerciseName': 'Clean Deadlift (barbell)',
         
                       'sets': '3',
                                'reps': '5',
                                'weight
': '60%',
                                'rest': '120',
                                'modifications': 'Emphasize pro
per starting position and back angle'
                            }
                        ]
                    },
   
                 {
                        'dayName': 'Day 2',
                        'dayOfWeek': 'Wednesday',
       
                 'dayFocus': 'Clean and Jerk Technique',
                        'exercises': [
                        
    {
                                'exerciseName': 'Olympic Squat (barbell)',
                                'sets':
 '3',
                                'reps': '5',
                                'weight': '65%',
                    
            'rest': '120',
                                'modifications': 'Focus on maintaining an upright torso'
    
                        },
                            {
                                'exerciseName': 'Sumo Deadlift 
(barbell)',
                                'sets': '3',
                                'reps': '5',
                  
              'weight': '65%',
                                'rest': '120',
                                'modificat
ions': 'Concentrate on driving through the legs'
                            }
                        ]
               
     },
                    {
                        'dayName': 'Day 3',
                        'dayOfWeek': 'Friday',

                        'dayFocus': 'Full Lifts and Strength',
                        'exercises': [
                 
           {
                                'exerciseName': 'Olympic Squat (barbell)',
                                
'sets': '3',
                                'reps': '5',
                                'weight': '70%',
             
                   'rest': '120',
                                'modifications': 'Focus on explosive power out of the 
bottom'
                            },
                            {
                                'exerciseName': 'Cl
ean Deadlift (barbell)',
                                'sets': '3',
                                'reps': '5',
     
                           'weight': '70%',
                                'rest': '120',
                             
   'modifications': 'Emphasize speed off the floor'
                            }
                        ]
            
        }
                ]
            },

  
What am I doing wrong? How can I make LLM to generate diverse set of exer
cise that target multiple body parts for each day of the week?
```
---

     
 
all -  [ How to get chat history working with Chainlit? ](https://www.reddit.com/r/LangChain/comments/1g01njm/how_to_get_chat_history_working_with_chainlit/) , 2024-10-12-0912
```
I've created a Jupyter notebook that successfully implements Langchains' chat history feature. But I can't figure out ho
w to get it working with Chainlit. Specifically, which code should go under '@cl.on\_chat\_start' and which should go un
der '@cl.on\_message'. Anyone have any pointers?

Here's the relevant code of my notebook:

    chat_history = []
    
 
   text = 'Hi. My name is Bob. I am 40 years old.'
    chain = prompt_template | model | parser
    
    response = chai
n.invoke(
        {'chat_history': chat_history,
        'text': text})
    
    chat_history.extend(
        [
        
    HumanMessage(content=text),
            AIMessage(content=response),
        ]
    )

And here's my Chainlit code. C
hainlit works, it just doesn't remember conversation history.

    @cl.on_chat_start
    async def on_chat_start():
    

        model = ChatVertexAI(
            model_name='gemini-1.5-flash',
            temperature=0.5,
            strea
ming=True,
        )
    
        system_prompt = 'You are a knowledgeable and useful AI'
    
        prompt_template =
 ChatPromptTemplate.from_messages(
            [
                ('system', system_prompt),
                ('user', '{t
ext}'),
            ]
        )
    
        chain = prompt_template | model | StrOutputParser()
        cl.user_session
.set('runnable', chain)
    
    @cl.on_message
    async def on_message(message: cl.Message):
        runnable = cast(R
unnable, cl.user_session.get('runnable'))
    
        msg = cl.Message(content='')
    
        async for chunk in runn
able.astream(
            {'text': message.content},
            config=RunnableConfig(callbacks=[cl.LangchainCallbackHa
ndler()]),
        ):
            await msg.stream_token(chunk)
    
        await msg.send()


```
---

     
 
all -  [ Problems with text splitter on a markdown file ](https://www.reddit.com/r/LangChain/comments/1fzyipy/problems_with_text_splitter_on_a_markdown_file/) , 2024-10-12-0912
```
Im having trouble using the text splitters in langchain. 

I tried the example in the docs for the recursive... Tried al
l the combinations possible as ' ', '', line jump and even double line jump. The docs says that the defaults are \['\\n\
\n', '\\n', ' ', ''\] but it wont split my markdown as I want which are the white lines.

[https://python.langchain.com/
v0.1/docs/modules/data\_connection/document\_transformers/recursive\_text\_splitter/](https://python.langchain.com/v0.1/
docs/modules/data_connection/document_transformers/recursive_text_splitter/)

The text splitter (non recursive) also won
t work. Tried all combinations.

My code is:

    from langchain_text_splitters import RecursiveCharacterTextSplitter
  
  
    # Load an example document
    with open('data_dictionaries/odata_schema_ARG_inversion.md') as f:
        data_di
ctionary = f.read()
    
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=3000,
        chunk_over
lap=0,
        is_separator_regex=False,
    )
    
    texts = text_splitter.create_documents([data_dictionary])
    # 
print each element in the list
    
    for text in texts:
        print('DOCUMENT')
        print(text)

I cant find a 
solution to the text splitters where I can pass a simple markdown text like and get the documents for each separate para
graph. As you can see I dont want any overlap and setted the maximum chunk size to 3000 but this should not be changing 
anything because this is the max

    database_name: mapainvanalyticsdbdev
    schema: chatmi
    table_name: arg_openda
ta_proyectos
    table_description: Datos abiertos de proyectos de inversión de la República Argentina
     
    schema:
 chatmi
    table_name: arg_opendata_proyectos
    column_name: IdProyecto
    description: Código identificador del pro
yecto en MapaInversiones. Sinónimos: id, identificador, código, referencia, número único. Cualquier campo de identificad
or usar esta columna
    data_type: int
     
    schema: chatmi
    table_name: arg_opendata_proyectos
    column_name:
 CodigoBapin
    description: Código identificador del proyecto dentro del banco de proyectos. Sinónimos: código, refere
ncia, identificador, BAPIN, número. Cualquier campo de código usar esta columna
    data_type: nvarchar
     
    schema
: chatmi
    table_name: arg_opendata_proyectos
    column_name: NombreProyecto
    description: Nombre del proyecto. Si
nónimos: título, denominación, proyecto, obra, etiqueta. Cualquier filtro where puede ser usado en este campo de nombre 
para encontrar temáticas, usar esta columna
    data_type: nvarchar
```
---

     
 
all -  [ Can SQLDatabaseToolkit use table and column descriptions? ](https://www.reddit.com/r/LangChain/comments/1fzxkpz/can_sqldatabasetoolkit_use_table_and_column/) , 2024-10-12-0912
```
I have a database where the columns names are such that their content is not very obvious. 

The documentation for SQLDa
tabaseToolkit says it retrieves table descriptions. Is there a way to similarly  pass description of each column to SQLD
atabaseToolkit for better conversion of query to SQL?

link to documentation: [https://python.langchain.com/docs/tutoria
ls/sql\_qa/](https://python.langchain.com/docs/tutorials/sql_qa/)

https://preview.redd.it/xa0tsbugqrtd1.png?width=1288&
format=png&auto=webp&s=fe6aae454889a658026310cab91e5835e10468df
```
---

     
 
all -  [ Help needed: chatbot skipping parts of resume (using gemma2:2b) ](https://www.reddit.com/r/ollama/comments/1fzx9wn/help_needed_chatbot_skipping_parts_of_resume/) , 2024-10-12-0912
```
Hi everyone,

I'm currently working on an AI chatbot that's supposed to respond based on my resume. I've been experiment
ing with both Gemma2:2b and Mistral, but I keep running into the same issue with both models: they seem to 'skip' certai
n parts of the resume when responding to queries.

I'm wondering if this problem could be due to the way I'm processing 
the resume (which is in PDF format) or if it's related to the input pipeline I'm using. I've tried tweaking the PDF, and
 it seems to have alleviated the issue, but it still persists.

**Relevant parts of my code:**

pdf\_handling.py

    im
port argparse
    import os
    import shutil
    from langchain_community.document_loaders import PyPDFLoader
    from 
langchain_text_splitters import RecursiveCharacterTextSplitter
    from langchain.schema.document import Document
    fr
om get_embedding_function import get_embedding_function
    from langchain_chroma import Chroma
    
    def main():
   
     parser = argparse.ArgumentParser()
        parser.add_argument('--reset', action = 'store_true', help = 'Reset the 
database.')
        args = parser.parse_args()
        if args.reset:
            print('✨ Clearing Database')
         
   clear_database()
    
        documents = load_document()
        chunks = split_documents(documents)
        add_to_
chroma(chunks)
    
    def load_document():
        document_loader = PyPDFLoader('Resume.pdf')
        return document
_loader.load()
    
    def split_documents(documents: list[Document]):
        text_splitter = RecursiveCharacterTextSp
litter(
            chunk_size = 800,
            chunk_overlap = 80,
            length_function = len,
            is_
separator_regex = False,
        )
        return text_splitter.split_documents(documents)
    
    def add_to_chroma(ch
unks: list[Document]):
        db_directory = 'my_chroma_data'  
        db_path = os.path.join(db_directory, 'chroma.sq
lite3')  
    
        os.makedirs(db_directory, exist_ok=True)
        
        db = Chroma(
            persist_direct
ory=db_directory,  
            embedding_function=get_embedding_function()
        )
    
        chunks_with_ids = cal
culate_chunk_ids(chunks)
    
        existing_items = db.get(include=[]) 
        existing_ids = set(existing_items['id
s'])
        print(f'Number of existing documents in DB: {len(existing_ids)}')
    
        new_chunks = []
        for 
chunk in chunks_with_ids:
            if chunk.metadata['id'] not in existing_ids:
                new_chunks.append(chu
nk)
    
        if len(new_chunks):
            print(f'👉 Adding new documents: {len(new_chunks)}')
            new_chu
nk_ids = [chunk.metadata['id'] for chunk in new_chunks]
            db.add_documents(new_chunks, ids=new_chunk_ids)
    
    else:
            print('✅ No new documents to add')
    
    def calculate_chunk_ids(chunks):
    
        last_pag
e_id = None
        current_chunk_index = 0
    
        for chunk in chunks:
            source = chunk.metadata.get('s
ource')
            page = chunk.metadata.get('page')
            current_page_id = f'{source}:{page}'
    
            
if current_page_id == last_page_id:
                current_chunk_index += 1
            else:
                current_c
hunk_index = 0
    
            chunk_id = f'{current_page_id}:{current_chunk_index}'
            last_page_id = current
_page_id
    
            chunk.metadata['id'] = chunk_id
    
        return chunks
    
    def clear_database():
    
    db_path = 'my_chroma_data/chroma.sqlite3'
        if os.path.exists(db_path):
            shutil.rmtree(os.path.dirn
ame(db_path))  
            print(f'✨ Database at {db_path} has been cleared.')
        else:
            print('⚠️ No d
atabase found to clear.')
    
    if __name__ == '__main__':
        main()

  
[chatboy.py](http://chatboy.py)

    im
port os
    from langchain_chroma import Chroma  # Updated import
    from langchain.prompts import ChatPromptTemplate
 
   from langchain_community.llms.ollama import Ollama
    from get_embedding_function import get_embedding_function
    

    PROMPT_TEMPLATE = '''
    You're roleplaying as Maximiliano López Montaño, based on what the resume says.
    
    
This is the resume: {context}
    
    ---
    
    Answer the question based on the above context: {question}
    '''
 
   
    def main():
        print('Welcome to the chatbot! Type 'exit' to quit.')
        
        while True:
         
   query_text = input('You: ')
            
            if query_text.lower() == 'exit':
                print('Goodbye!
')
                break
            
            response = query_rag(query_text)
            print(f'AI: {response}')

    
    def query_rag(query_text: str):
        embedding_function = get_embedding_function()
    
        persist_dire
ctory = 'my_chroma_data'
        db_path = os.path.join(persist_directory, 'chroma.sqlite3')
    
        if not os.path
.exists(db_path):
            print('⚠️ Database not found. Please run pdf_handling.py to create the database.')
       
     return 'No data available.'
    
        db = Chroma(persist_directory=persist_directory, embedding_function=embedd
ing_function)
    
        results = db.similarity_search_with_score(query_text, k=5)
    
        context_text = '\n\n-
--\n\n'.join([doc.page_content for doc, _score in results])
        prompt_template = ChatPromptTemplate.from_template(P
ROMPT_TEMPLATE)
        prompt = prompt_template.format(context=context_text, question=query_text)
    
        model = 
Ollama(model='gemma2:2b')
        response_text = model.invoke(prompt)
    
        formatted_response = f'{response_tex
t}'
        return formatted_response
    
    if __name__ == '__main__':
        main()

  
Any advice on where the iss
ue might lie or improvements I can make would be greatly appreciated. Thanks in advance!

I can also share the PDF if ne
cessary :)
```
---

     
 
all -  [ Working on a frontend for my project Novel Generator ](https://www.reddit.com/r/Bard/comments/1fzx9t0/working_on_a_frontend_for_my_project_novel/) , 2024-10-12-0912
```
https://preview.redd.it/ek54uxlfnrtd1.png?width=1253&format=png&auto=webp&s=ec8953ca23f5852ba8aa45a988d493fcf7737736

Ig
nore the styling, but what do you guys think? Lots of fun using langchain and google api
```
---

     
 
all -  [ Is everyone an AI engineer now 😂 ](https://www.reddit.com/r/LangChain/comments/1fzw0ie/is_everyone_an_ai_engineer_now/) , 2024-10-12-0912
```
I am finding it difficult to understand and also funny to see that everyone without any prior experience on ML or Deep l
earning is now an AI engineer… thoughts ? 
```
---

     
 
all -  [ Node based LLM interactive tool ](https://github.com/Xerophayze/XeroFlow) , 2024-10-12-0912
```
Hey everyone, I've been working on this project for about a week and thought maybe I would bring it up here as a resourc
e for people to use. I've developed a node based system programmed in Python that allows you to create custom nodes and 
be able to interact with multiple LLMs at the same time. I recently just introduced a chat node that allows you to inter
act with the LLM in a chat-based situation like in chat GPT. And I'm currently working on integrating langchain and rag.
 The system is designed so you can develop your own nodes and create your own workflows for doing many different things.
 I also have a node for developing long form content. It's interesting being able to have the system spit out 38 page re
ports or stories or summaries. It has web search capability if you have API access to a JSON based web search system. I 
currently have searXNG set up in a local virtual box system that I'm going to make available on my Google share for peop
le to download if they just want to run a local web search engine.  
Anyway you can check it out here at my GitHub. Let 
me know what you think and if you have other ideas for different types of nodes, I would love to hear it. 
https://githu
b.com/Xerophayze/XeroFlow
```
---

     
 
all -  [ Lost, unsure of the next step in learning ML ](https://www.reddit.com/r/learnmachinelearning/comments/1fzoyw9/lost_unsure_of_the_next_step_in_learning_ml/) , 2024-10-12-0912
```
I am trying to prepare myself for the job market, however environmental science data science jobs aren't really out ther
e beyond academia. Therefore I am refocusing on marketing jobs, and in turn LLMs/AI.

My background is a solid understan
ding of the 'classics', i.e RF, PLSR, log. and linear regression, SVM/SVR, gradient boost, etc. Supervised vs. unsupervi
sed, training/testing/validation splits. Preprocessing techniques.

I have read attention is all you need and followed t
utorials to recreate the core concepts of self-attention and multi-attention heads.

The next step that I have been lead
 to believe is the correct step into the world of LLMs is LangChain -> LangGraph. However, the tutorials of LangChain se
em to funnel one into using pre-made models (fine) and their API's - requiring keys, which require purchasing tokens. I 
have downloaded Llama 3.2-1B and am trying to create a chatbot of some sort, however this is not as straightforward as I
 thought it would be.

So now I have a few questions and would be thankful if anybody would share their insights:

1) Is
 my decision to focus on LangChain a logical next step given my background,  or are there other stepping stones that I s
hould be revisiting first?

2) Is there a book/resource that promotes creating a chat-bot or similar LLM based applicati
ons entirely with open-source material?

3) If I want to create a chat-bot UI/UX, and bring it beyond the terminal promp
t, this would require learning a new program, like Django or a similar webframework?

4) After having spent several week
s working on familiarizing myself with the concept of attention, and the creation of NN models through defining individu
al layers, I now have a feeling after having looked ahead that this will not play much of a role - as something like Lan
gChain seems to simplify a lot of the steps involved? Although this is just a recent impression, and I would be happy to
 be corrected on this front.

Thanks for any input and your time!
```
---

     
 
all -  [ AI Agents in 40 minutes ](https://www.reddit.com/r/LangChain/comments/1fzoht5/ai_agents_in_40_minutes/) , 2024-10-12-0912
```
The video covers code and workflow explanations for:  
  
- Function Calling  
- Function Calling Agents + Agent Runner 
 
- Agentic RAG  
- REAcT Agent: Build your own Search Assistant Agent

Watch here: [https://www.youtube.com/watch?v=bHn
4dLJYIqE](https://www.youtube.com/watch?v=bHn4dLJYIqE)
```
---

     
 
MachineLearning -  [ [D] How are folks building conversational Retrieval Augmented Generation apps ](https://www.reddit.com/r/MachineLearning/comments/1ftdby7/d_how_are_folks_building_conversational_retrieval/) , 2024-10-12-0912
```
I've read through various resources such as:  
- [https://vectorize.io/how-i-finally-got-agentic-rag-to-work-right/](htt
ps://vectorize.io/how-i-finally-got-agentic-rag-to-work-right/)  
- [https://python.langchain.com/docs/tutorials/qa\_cha
t\_history/](https://python.langchain.com/docs/tutorials/qa_chat_history/)  
- [https://langchain-ai.github.io/langgraph
/tutorials/rag/langgraph\_agentic\_rag/](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/) 
 
- [https://docs.llamaindex.ai/en/stable/module\_guides/deploying/chat\_engines/](https://docs.llamaindex.ai/en/stable/
module_guides/deploying/chat_engines/)  
- [https://huggingface.co/datasets/nvidia/ChatRAG-Bench](https://huggingface.co
/datasets/nvidia/ChatRAG-Bench) 

But these feel overly reductive, since they don't address complexities like:  
1) when
 to retrieve vs. just respond immediately to reduce latency  
2) rely on existing context previously retrieved in the co
nversation instead of retrieving again at the current turn  
3) partition LLM context between retrieved information and 
past conversation history.

I'm sure some teams already have good systems for this, would appreciate pointers!
```
---

     
 
MachineLearning -  [ Built a web agent which call fill Google forms based on the user details [P] ](https://www.reddit.com/r/MachineLearning/comments/1fozud5/built_a_web_agent_which_call_fill_google_forms/) , 2024-10-12-0912
```
GitHub repo : [https://github.com/shaRk-033/web-agent](https://github.com/shaRk-033/web-agent)

Tried to solve it using 
two approaches:

# 1: Basic Scraping and Filling

This is the straightforward approach. The agent scrapes the form’s HTM
L and uses fixed XPaths to find and fill in the required fields.

* It pulls the form’s HTML, locates the fields with se
t XPaths, and inputs the answers. It’s a direct and simple method.
* If the form changes or an element isn’t where it’s 
expected, the process can fail and may need manual adjustments.

[basic approach](https://preview.redd.it/5e8g4a1k4xqd1.
png?width=1055&format=png&auto=webp&s=d8e984e4feaee2f0453b08c8696768c40a2a5c20)

2. Using LangChain Agents and tool call
ing

* LangChain Agent**:** The agent handles everything by using the LLM’s reasoning to decide what to do next, includi
ng generating those tricky XPaths.
* Error Handling**:** If something goes wrong (like an element not found), the agent 
tries again with better XPaths until it gets the job done.

[using langchain agents](https://preview.redd.it/948i88pl4xq
d1.png?width=782&format=png&auto=webp&s=ed1e6c19efec9f4cbbbd6ab5a22558f221cf745f)

Any recommendations to improve this w
ould be welcome. Also, if anyone has ideas on building similar web agents to automate other tasks, it would be great to 
hear them. :)
```
---

     
 
MachineLearning -  [ [P] Swapping Embedding Models for an LLM ](https://www.reddit.com/r/MachineLearning/comments/1fktvbj/p_swapping_embedding_models_for_an_llm/) , 2024-10-12-0912
```
How tightly coupled is an embedding model to a language model?

Taking an example from Langchain's tutorials, they use O
llama's _nomic-embed-text_ for embedding and _Llama3.1_ for the understanding and Q/A. I don't see any documentation abo
ut Llama being built on embeddings from this embedding model. 

Intuition suggests that a different embedding model may 
produce outputs of other sizes or produce a different tensor for a character/word, which would have an impact on the res
ults of the LLM. So would changing an embedding model require retraining/fine-tuning the LLM as well?

I need to use a e
mbedding model for code snippets and text. Do I need to find a specialized embedding model for that? If yes, how will ll
ama3.1 ingest the embeddings?
```
---

     
 
deeplearning -  [ What is the best approach for Parsing and Retrieving Code Context Across Multiple Files in a Hierarc ](https://www.reddit.com/r/deeplearning/comments/1fh58oz/what_is_the_best_approach_for_parsing_and/) , 2024-10-12-0912
```
I want to implement a Code-RAG system on a code directory where I need to:

* Parse and load all the files from folders 
and subfolders while excluding specific file extensions.
* Embed and store the parsed content into a vector store.
* Ret
rieve relevant information based on user queries.

However, I’m facing two major challenges:

**File Parsing and Loading
:** What’s the most efficient method to parse and load files in a hierarchical manner (reflecting their folder structure
)? Should I use Langchain’s directory loader, or is there a better way? I came across the Tree-sitter tool in Claude-dev
’s repo, which is used to build syntax trees for source files—would this be useful for hierarchical parsing?

**Cross-Fi
le Context Retrieval:** If the relevant context for a user’s query is spread across multiple files located in different 
subfolders, how can I fine-tune my retrieval system to identify the correct context across these files? Would reranking 
resolve this, or is there a better approach?

**Query Translation:** Do I need to use Something like Multi-Query or RAG-
Fusion to achieve better retrieval for hierarchical data?

\[I want to understand how tools like [continue.dev](http://c
ontinue.dev/) and [claude-dev](https://github.com/saoudrizwan/claude-dev) work\]
```
---

     
