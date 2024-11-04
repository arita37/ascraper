 
all -  [ RAG for image-to-text app and multimodal embeddings ](https://www.reddit.com/r/LangChain/comments/1giwmb2/rag_for_imagetotext_app_and_multimodal_embeddings/) , 2024-11-04-0913
```
Hi,

I m thinking about an application like this:  
  
1) I have prompt composed by text and image. The text is fixed bu
t fairly long, something along the line  'Describe what is in the image ...' while the image  changes as the user upload
s it  
2) I have a like 10K words long text for many of the images that the user might upload  
3) to improve the applic
ation I would like to do RAG as follows:  
3.1) create embeddings for all the texts by chunking - say - 1500 words  
3.2
) create embeddings for the images  
3.3) when the user uploads the image, create the embedding and search the text that
 are more close to the image embedding  
3.4) Include the retrieved text into the prompt and send it to an Multimodal LL
M

  
I see there are sever API that to the multimodal embeddings (text and image in the same vector space)  for example
 embed 3, google, but they all limit the text to 30 or 70 words, while I have texts of 10k words or chunks of 1500 words
 -70 words would not improve the prompt

I'm not sure what to do?  
Should I chunk the 10K texts into 50 words chunks, s
elect say 100 embeddings and concat the text? Sounds wrong?

Any idea?
```
---

     
 
all -  [ Python LangChain for RAG Beginners: Building Powerful AI Applications with GPT Agents ](https://www.reddit.com/r/generativeAI/comments/1giwa1j/python_langchain_for_rag_beginners_building/) , 2024-11-04-0913
```
Just released a book on LangChain for RAG Beginners: Building Powerful AI Applications with GPT Agents using Python,

[h
ttps://www.amazon.com/Python-LangChain-RAG-Beginners-Applications-ebook/dp/B0DBZ9C7PF/ref=tmm\_kin\_swatch\_0?\_encoding
=UTF8&qid=&sr=](https://www.amazon.com/Python-LangChain-RAG-Beginners-Applications-ebook/dp/B0DBZ9C7PF/ref=tmm_kin_swatc
h_0?_encoding=UTF8&qid=&sr=)



[ Python LangChain for RAG Beginners](https://preview.redd.it/45wd4d65wqyd1.png?width=97
0&format=png&auto=webp&s=8b8c0540de0f9272650072a13f6766045e9ed5d0)

Soon will release the JavaScript Version

You can ac
cess all source code for the examples in GitHub

[https://github.com/LangChainBook/LangChainBegginer](https://github.com
/LangChainBook/LangChainBegginer)

Please, let me know if you read it, what should I update. My idea is to keep updating
 it as LangChain evolves.

Thanks,

Karel
```
---

     
 
all -  [ Submit Feedback Node (Getting runId from RunnableConfig inside a node) ](https://www.reddit.com/r/LangGraph/comments/1giuqw7/submit_feedback_node_getting_runid_from/) , 2024-11-04-0913
```
I have raised a question on the repo: [https://github.com/langchain-ai/langgraphjs/discussions/655](https://github.com/l
angchain-ai/langgraphjs/discussions/655)

In summary, I want to programmatically, create a feedback on a LangSmith trace
 either through a tool or node. I figured the right place for it is a node since you can pass the Runnable Config and th
eoretically get the \`runId\` from it to be used in the \`langsmithClient.createFeedback\` function. I have attempted a 
few different ways to retrieve the runId and also manually setting it in the configurable object, but none seem to work.
 Has anyone been able to successfully do this within a graph node? (note my application is in ts. and I am using the lan
graph.js SDK) 
```
---

     
 
all -  [ Langgraph-ui-sdk  ](https://www.reddit.com/r/OpenSourceeAI/comments/1gip356/langgraphuisdk/) , 2024-11-04-0913
```
Hey GenAI and langchain folks 🦜
I posted this library today, I didn't find a way out of the box to have UI component for
 the chatbot in any JavaScript development  environment so I developed one today.
Please start ⭐ the repository if you p
lan to use it in the future to keep improving it 🙏 
https://github.com/AmrAnwar/LangGraph-UI-SDK
```
---

     
 
all -  [ Chat with repository using gemini  ](https://www.reddit.com/r/LangChain/comments/1gijdtz/chat_with_repository_using_gemini/) , 2024-11-04-0913
```
 🔍 Built a GitHub Repository AI Assistant using LangChain + Gemini

Hey r/LangChain! I wanted to share a project I've bu
ilt that helps developers understand any GitHub repository through natural language Q&A.

🔹What it does:
- Accepts any G
itHub repo URL
- Lets you ask questions about the codebase in plain English
- Provides quick explanations of code struct
ure & documentation
- Supports multiple programming languages (Python, JavaScript, TypeScript, etc.)

🔹Tech Stack:
- Lan
gChain for Agent system 
- Google's Gemini as llm
- Hugging Face for embedding models
- Advanced RAG implementation for 
accurate responses

The tool aims to solve the common challenge of quickly understanding unfamiliar codebases.

 🔹You ca
n try it here: https://git-ai-by-jay.streamlit.app

I'd love to hear your thoughts and feedback from the LangChain commu
nity! What features would you like to see added?

Let me know if you'd like me to modify anything in this Reddit post!


LinkedIn post showing demo video: 
https://www.linkedin.com/posts/jaygupta17_ai-programming-developertools-activity-7258
717904970371073-oFWx?utm_source=share&utm_medium=member_android
```
---

     
 
all -  [ Someone know how many gpus or servers i need to use any LLM for around 300 request simultanius? ](https://www.reddit.com/r/LangChain/comments/1gihabj/someone_know_how_many_gpus_or_servers_i_need_to/) , 2024-11-04-0913
```

```
---

     
 
all -  [ How to speed up chunking, embedding, and persistence for file uploads? ](https://www.reddit.com/r/aws/comments/1gi7onq/how_to_speed_up_chunking_embedding_and/) , 2024-11-04-0913
```
When a user uploads a doc, it chunks, embeds, then persists it. This currently takes 25 seconds with multithreading on 6
 cores for me. The chunk size is small (250), so there's a lot to process. I need this to be faster, and I need to add s
upport for concurrent file uploads.

Here's my current setup:

embeddings: openai small embedding model (batch embed)

c
hunking: langchain recursive text chunker (250 chunk size)

persistence: Mongodb vector store (batch persist)   
  
I se
e several companies online seemingly able to upload & embed my same 200 page document in 6 seconds (chatgpt), and in par
allel so i'm wondering if i'm missing something that everyone else is using. What tools libraries/tools do you guys use 
to have fast chunking, embedding, & persistence?

My current idea is to achieve fast parallel uploads via a separate AWS
 lambda invocation per upload, and have a high amount of cores per lambda so we can achieve paralell processing of chunk
s in the lambda. Thoughts/advice?
```
---

     
 
all -  [ Best way for fast chunking, embedding, and persistence on large docs? ](https://www.reddit.com/r/LLMDevs/comments/1gi7m2c/best_way_for_fast_chunking_embedding_and/) , 2024-11-04-0913
```
When a user uploads a doc, it chunks, embeds, then persists it. This currently takes 25 seconds with multithreading on 6
 cores for me. I need this to be faster, and I need to add support for concurrent file uploads.

Here's my current setup
:

embeddings: openai small embedding model (batch embed)

chunking: langchain recursive text chunker (250 chunk size)


persistence: Mongodb vector store (batch persist)   
  
I see several companies online seemingly able to upload & embed 
my same 200 page document in 6 seconds (chatgpt), and in parallel so i'm wondering if i'm missing something that everyon
e else is using. What tools libraries/tools do you guys use to have fast chunking, embedding, & persistence?

My current
 idea is to achieve fast parallel uploads via a separate AWS lambda invocation per upload, and have a high amount of cor
es per lambda so we can achieve paralell processing of chunks in the lambda. Thoughts/advice?
```
---

     
 
all -  [ Are You Tired of ChatGPT Hallucinating and Weak Brainstorming? Here’s a Solution! ](https://www.reddit.com/r/AI_Agents/comments/1gi64ty/are_you_tired_of_chatgpt_hallucinating_and_weak/) , 2024-11-04-0913
```
Hi everyone! I’ve created Brainstormers – a straightforward, open-source, LLM-powered tool using LangChain to enhance yo
ur brainstorming. Unlike ChatGPT, this app guides you through structured brainstorming techniques like Mind Mapping, Rev
erse Brainstorming, SCAMPER, and more, helping you get focused, high-quality ideas.

If you’re looking for a reliable wa
y to brainstorm without the usual hiccups, check it out here: [GitHub Repository](https://github.com/Azzedde/brainstorme
rs).

As I'm still in my journey of learning, I would really appreciate some feedback from all the community, what shoul
d I improve and is the idea itself good ?
```
---

     
 
all -  [ Are You Tired of ChatGPT Hallucinating and Weak Brainstorming? Here’s a Solution! ](https://www.reddit.com/r/LLMDevs/comments/1gi63ty/are_you_tired_of_chatgpt_hallucinating_and_weak/) , 2024-11-04-0913
```
Hi everyone! I’ve created **Brainstormers** – a straightforward, open-source, LLM-powered tool using LangChain to enhanc
e your brainstorming. Unlike ChatGPT, this app guides you through structured brainstorming techniques like Mind Mapping,
 Reverse Brainstorming, SCAMPER, and more, helping you get focused, high-quality ideas.

If you’re looking for a reliabl
e way to brainstorm without the usual hiccups, check it out here: [GitHub Repository](https://github.com/Azzedde/brainst
ormers).

As I'm still in my journey of learning, I would really appreciate some feedback from all the community, what s
hould I improve and is the idea itself good ?
```
---

     
 
all -  [ Are You Tired of ChatGPT Hallucinating and Weak Brainstorming? Here’s a Solution! ](https://www.reddit.com/r/ChatGPT/comments/1gi61pz/are_you_tired_of_chatgpt_hallucinating_and_weak/) , 2024-11-04-0913
```
Hi everyone! I’ve created **Brainstormers** – a straightforward, open-source, LLM-powered tool using LangChain to enhanc
e your brainstorming. Unlike ChatGPT, this app guides you through structured brainstorming techniques like Mind Mapping,
 Reverse Brainstorming, SCAMPER, and more, helping you get focused, high-quality ideas.

If you’re looking for a reliabl
e way to brainstorm without the usual hiccups, check it out here: [GitHub Repository](https://github.com/Azzedde/brainst
ormers).

As I'm still in my journey of learning, I would really appreciate some feedback from all the community, what s
hould I improve and is the idea itself good ?
```
---

     
 
all -  [ Introducing Cascade of Semantically Integrated Layers (CaSIL): An Absurdly Over-Engineered Thought/R ](https://www.reddit.com/r/LocalLLaMA/comments/1gi102k/introducing_cascade_of_semantically_integrated/) , 2024-11-04-0913
```
So here’s a fun one. Imagine layering so much semantic analysis onto a single question that it practically gets therapy.
 That’s CaSIL – Cascade of Semantically Integrated Layers. It’s a ridiculous (but actually effective) pure Python algori
thm designed to take any user input, break it down across multiple layers, and rebuild it into a nuanced response that e
ven makes sense to a human.

I have been interested in and experimenting with all the reasoning/agent approaches lately 
which got me thinking of how I could add my 2 cents of ideas, mainly around the concept of layers that waterfall into ea
ch other and the extracted relationships of the input.

The whole thing operates without any agent frameworks like LangC
hain or CrewAI—just straight-up Python and math. And the best part? CaSIL can handle any LLM, transforming it from a “ye
s/no” bot to something that digs deep, makes connections, and understands broader context.

How it works (briefly):

1. 
Initial Understanding: Extract basic concepts from the input.


2. Relationship Analysis: Find and connect related conce
pts (because why not build a tiny knowledge graph along the way).


3. Context Integration: Add historical and contextua
l knowledge to give that extra layer of depth.


4. Response Synthesis: Put it all together into a response that doesn’t
 feel like a Google result from 2004.


The crazy part? It actually works. Check out the pure algo implementation with t
he repo. No fancy dependencies,, and it’s easy to integrate with whatever LLM you’re using.

https://github.com/severian
42/Cascade-of-Semantically-Integrated-Layers

Example output: https://github.com/severian42/Cascade-of-Semantically-Inte
grated-Layers/blob/main/examples.md


EDIT FOR CLARITY!!! 

Sorry everyone, I posted this and then fell asleep after a l
ong week of work. I'll clarify some things from the comments here.

1. What is this? What are you claiming?: This is jus
t an experiment that actually worked and is interesting to use. I by no means am saying I have the 'secret sauce' or riv
als o1. My algorithm is just a really interesting way of having LLM s 'think' through stuff in a non-traditional way. Be
nchmarks so far have been hit or miss

2. Does it work? Is the code crap?: it does work! And yes, the code is ugly. I cr
eated this in 2 days with the help of Claude while working my day job.
 

3. No paper? Fake paper?: There is no official
 paper but there is the random one in the repo. What is that? Well, part of my new workflow I was testing that helped st
art this codebase. Part of this project was to eventually showcase how I built an agent based workflow that allows me to
 take an idea, have a semi-decent/random 'research' paper written by those agents. I then take that and run it into anot
her agent team that translates it into a starting code base for me to see if I can actually get working. This one did.



4. Examples?: There is an example in the repo but I will try and put together some more definitive and useful. For now,
 take a look at the repo and give it a shot. Easy set up for the most part. Will make a UI also for those non coders 



Sorry if it seemed like I was trying to make great claims. Not at all, just showing some interesting new algorithms for 
LLM inference 
```
---

     
 
all -  [ Guidance in Building Application  ](https://www.reddit.com/r/LangChain/comments/1ghxtgu/guidance_in_building_application/) , 2024-11-04-0913
```
I'm building a multi agent application in langgraph where one agent is conversing with a user and another agent evaluate
s the response of the user 

The graph construction seems simple

User conversation with Agent back and forth 
Reply eva
luated by another agent 

I'm struggling in understanding the syntax and coding 

Would like to know if this is doable a
nd any pointers to develop it 

Thank you
```
---

     
 
all -  [ Keep consistent context in conversation ](https://www.reddit.com/r/LangChain/comments/1ghsivu/keep_consistent_context_in_conversation/) , 2024-11-04-0913
```
Hello everyone, I'm pretty new to langchain & langraph assuming that I want to build pizza ordering bot which would talk
 to the customers, sample bellow: 

**Bot** : Hi, how can I help you ?  
**Human**: I would like to buy a pepperoni  
**
Bot:** Sure something else ?   
**Human:** I would like to ask is diavola spicy ?  
**Bot:** Yes, the diavola is spicy  
?   
**Human**: Okay, I would like one diavola as well with some extra basil .  
**Bot :** <conclude the order and confi
rm it> 

I'm trying to achieve something similar in a more complex context, but the problem I face cannot keep a consist
ent context, e.g. It could add diavola with details but remove pepperoni, or keep diavola without extra details. 

  
I 
would like to ask if someone faced something similar, how do you handle this problem, maybe there is some useful tools w
hich, I'm not aware of ? 

Thanks


```
---

     
 
all -  [ MY RAG VS OPENAI CUSTOM GPT ](https://www.reddit.com/r/LangChain/comments/1ghsbhz/my_rag_vs_openai_custom_gpt/) , 2024-11-04-0913
```
  
I NEED YOUR ANSWERS.   
  
SO for the last few weeks i was building a RAG using LangChain + Pinecone + Open AI.  so i
t is done now  
and i noticed that there is some thing called CUSTOM GPT. which is kind of the same thing .

so my quest
ion is which one is better. in different comparison.   should i cancel my application and just use Custom GPT ?  what is
 your point on this ?
```
---

     
 
all -  [ Role Based Access Control ](https://www.reddit.com/r/LangChain/comments/1ghqoza/role_based_access_control/) , 2024-11-04-0913
```
Hey guys I'm currently working on developing a RAG application with 100 documents however, these documents should be spl
it based on user. For example a CEO would have access to all 100 documents whereas a junior would have access to 5 docum
ents. Has anyone done that or have any idea how to do it? I do have a normal RAG app connected to postgres with fastapi 
integration but I'm not sure how to implement role based access control (RBAC)
```
---

     
 
all -  [ Did something happen with LangChain Discord server or was I kicked? ](https://www.reddit.com/r/LangChain/comments/1ghnlif/did_something_happen_with_langchain_discord/) , 2024-11-04-0913
```
I was in the server for more than a year and was occasionally asking questions about various LangChain products (almost 
never got an answer though) and today I found out I don't see LangChain server in my discord. Why is that?
```
---

     
 
all -  [ Langchain salaries ](https://www.reddit.com/r/LangChain/comments/1ghmzge/langchain_salaries/) , 2024-11-04-0913
```
Anyone here know how much langchain is paying software and solution engineers these days ? 
```
---

     
 
all -  [ Created LangGraph-ui-sdk package to create Chatbot out of the box ](https://www.reddit.com/r/LangChain/comments/1ghkgvf/created_langgraphuisdk_package_to_create_chatbot/) , 2024-11-04-0913
```
Hey guys,

I did a library on top of assistant-ui to have User-Interface SDK for any  Javascript/Typescript project. by 
a single function call it creates the chatbot chat. works also

[npm package](https://www.npmjs.com/package/langgraph-ui
-sdk) | [GitHub repository](https://github.com/AmrAnwar/LangGraph-UI-SDK)
If you plan on using it in the future please s
tart the repository so I could be aware to continue improving it.

I'm thinking about improving it in the future by buil
ding the chatbot component from scratch to reduce the library size and add more features to the chat like human in the l
oop and themes.

I understand not everyone likes those approaches but thought might be helpful for someone
```
---

     
 
all -  [ Best tools for building KBs from email archives ](https://www.reddit.com/r/LangChain/comments/1ghkc0t/best_tools_for_building_kbs_from_email_archives/) , 2024-11-04-0913
```
I’m working on a bot for sales/customer support and need to build knowledge bases from existing email archives to RAG ov
er.  While I know there are many low level tools to help extract, filter, and structure the knowledge for efficient retr
ieval, I’m wondering if there are any good purpose built end to end solutions I can leverage instead of rolling my own. 
Ideally the solution would support continuous updating, but that’s not a strict requirement. Would much appreciate any a
dvice for this endeavor.
```
---

     
 
all -  [ Mistral Large Model and streaming ](https://www.reddit.com/r/MistralAI/comments/1ghjt4o/mistral_large_model_and_streaming/) , 2024-11-04-0913
```
Hi,

I am using [ChatMistralAI](https://python.langchain.com/docs/integrations/chat/mistralai/) and [FastAPI](https://fa
stapi.tiangolo.com/) with the Python client and I am scratching my head on how to enable streaming successfully with Mis
tral Large. I am battling a lot of 422 and trying to find out what the issue is in the request I am sending. Since ChatM
istralAI should act as a wrapper and it abstracts away the details of constructing requests directly to the API, making 
it easier to use without needing to build raw HTTP requests. Therefore, my first attempt was this:

`from fastapi import
 FastAPI, HTTPException`

`from fastapi.responses import StreamingResponse`

`from langchain.chat_models import ChatMist
ral`

`from pydantic import BaseModel`

`app = FastAPI()`

`class Question(BaseModel):`

`text: str`

`temperature: floa
t = 0.7`

`max_new_tokens: int = 100`

`\@app.post('/code-generation') # corrected @ symbol`

`async def code_generation
(question: Question):`

`mistral_api_key = 'YOUR_MISTRAL_API_KEY'`

`# Initialize ChatMistral with streaming enabled`

`
chat_mistral = ChatMistral(`

`api_key=mistral_api_key,`

`model='mistral-large', # specify the model variant`

`tempera
ture=question.temperature,`

`max_tokens=question.max_new_tokens`

`)`

`async def stream_response():`

`try:`

`async f
or token in chat_mistral.chat_stream(messages=question.text):`

`yield token['choices'][0]['delta']['content']`

`except
 Exception as e:`

`raise HTTPException(status_code=500, detail=str(e))`

`return StreamingResponse(stream_response(), m
edia_type='text/plain')`

However, I don't seem to get it right as I am banging my head with 422 errors that I cannot cl
early debug. I took a different approach, but still with no joy and using directly the `'https://api.mistral.ai/v1/chat/
completions' endpoint, as follows:`

`from fastapi import FastAPI, HTTPException`

`from fastapi.responses import Stream
ingResponse`

`import requests`

`import json`

`app = FastAPI()`

`mistral_api_key = 'YOUR_MISTRAL_API_KEY'`

u/app`.po
st('/code-generation')`

`async def code_generation(question: Question):`

`headers = {`

`'Authorization': f'Bearer {mi
stral_api_key}',`

`'Content-Type': 'application/json',`

`'Accept': 'application/json',`

`}`

`payload = {`

`'model':
 'mistral-large', # whatever model ID`

`'temperature': question.temperature,`

`'max_tokens': question.max_new_tokens,`


`'stream': True,`

`'messages': question.text`

`}`

`def mistral_endpoint(headers, payload):`

`try:`

`response = re
quests.post(`

`'https://api.mistral.ai/v1/chat/completions',`

`headers=headers,`

`json=payload,`

`stream=True`

`)`


`response.raise_for_status() # Raises an error for non-200 responses`

`for line in response.iter_lines():`

`if line a
nd line != b'data: [DONE]':`

`json_data = json.loads(line.decode('utf-8').replace('data: ', ''))`

`yield json_data['ch
oices'][0]['delta']['content']`

`except requests.exceptions.RequestException as e:`

`raise HTTPException(status_code=5
00, detail=f'Error communicating with Mistral API: {e}')`

`return StreamingResponse(mistral_endpoint(headers, payload),
 media_type='text/plain')`

What is the correct way to enable streaming for a Mistral Large model? Do you directly use t
he `chat/completions` endpoint? What is exactly the payload I need to construct? What am I missing?

Thanks
```
---

     
 
all -  [ I was super frustated with langchain's pile of unnecessary abstractions, so I created something new ](https://www.reddit.com/r/LangChain/comments/1ghglbs/i_was_super_frustated_with_langchains_pile_of/) , 2024-11-04-0913
```
**Has anyone else been frustated writing and debugging langchain code?** There are so many classes and abstractions that
 don't seem to add much value. As a result, what really happens behind the curtains feel quite opaque. For me having low
-level control is very important. 

So I just published this open-source framework [**GenSphere**](https://github.com/oc
topus2023-inc/gensphere)**.** You build LLM applications with yaml files, that define an execution graph. Nodes can be e
ither LLM API calls, regular function executions or other graphs themselves. Because you can nest graphs easily, buildin
g complex applications is not an issue, but at the same time you don't lose control. 

There is also this Hub that you c
an push and pull projects from, so it becomes easy to share what you build and leverage from the community.

Its all ope
n-source. Would love to get your thoughts. Pls reach out or join the [discord server](https://discord.gg/DZFWMXJv) if yo
u want to contribute.
```
---

     
 
all -  [ Autonomous Dynamic Graph Creation ](https://www.reddit.com/r/LangChain/comments/1ghf7df/autonomous_dynamic_graph_creation/) , 2024-11-04-0913
```
Has anyone experimented with creating a planner agent that dynamically creates graphs to carry out complex tasks?  
I've
 built an agentic framework from scratch where each agents each hold specific personas and sets of tools and collaborate
 in a centralized conversation with the user.  
Each message received by an agent triggers an sort of 'internal monologu
e' which implements the ReAct framework.

But I've noticed that without clear directions, planning, and tasks assignment
s, the agent team really struggles to carry out complex tasks.

So I was thinking: it'd be great to implement a sort of 
plan-execute pattern with a planning agent. Ideally it would even create a LangGraph Graph.  
Models would even be train
ed on planning, kind of like how o1-preview has been trained on chain of thoughts.

Any thoughts? Anyone has experimente
d with this?  
Cheers!
```
---

     
 
all -  [ List of FREE and Best Selling Discounted Courses ](https://www.reddit.com/r/udemyfreebies/comments/1ghedzm/list_of_free_and_best_selling_discounted_courses/) , 2024-11-04-0913
```
# Udemy Free Courses for 02 November 2024

Note : Coupons might expire anytime, so enroll as soon as possible to get the
 courses for FREE.

* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/22077/)[ASP.NET](http://ASP.NET) MVC Complete Gu
ide using .NET Core \[.NET8 Updated\]
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/22076/)Become a professional i
nterior designer using sketch up pro
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/22075/)How To Make Money Everyd
ay Using AI ChatGPT /Fiverr.
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/22074/)Grow your Facebook page organica
lly 5000 follower in a week
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/22073/)AutoCAD 2D Floor Plan From Beginn
er To Advanced Level.
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/22072/)Complete Data Analyst Bootcamp From Bas
ics To Advanced
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/22071/)Mastering Figma from 0 to 100 (UI/UX Mastery 
Course)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/22070/)Elearning 2024: Create & Sell Online Courses
* [REDEE
M OFFER ](https://idownloadcoupon.com/udemy/22069/)All in One Pure Practical Social Media Marketing Course
* [REDEEM OFF
ER ](https://idownloadcoupon.com/udemy/22068/)Mathematics-Basics to Advanced for Data Science And GenAI
* [REDEEM OFFER 
](https://idownloadcoupon.com/udemy/22067/)Complete Data Science,Machine Learning,DL,NLP Bootcamp
* [REDEEM OFFER ](http
s://idownloadcoupon.com/udemy/22066/)Complete MLOps Bootcamp With 10+ End To End ML Projects
* [REDEEM OFFER ](https://i
downloadcoupon.com/udemy/22065/)Complete Generative AI Course With Langchain and Huggingface
* [REDEEM OFFER ](https://i
downloadcoupon.com/udemy/22064/)Building Gen AI App 12+ Hands-on Projects with Gemini Pro
* [REDEEM OFFER ](https://idow
nloadcoupon.com/udemy/22063/)Beginner Affiliate Marketing To Start In 1 Day – 2024
* [REDEEM OFFER ](https://idownloadco
upon.com/udemy/22062/)Fiverr Freelancing 2024: Sell Like The Top 1%
* Create (Artificial Intelligence) AI VIDEOS WITH ZE
RO FILMING
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/22061/)
* [REDEEM OFFER ](https://idownloadcoupon.com/udem
y/22060/)Linux A to Z 2025: Secure Your Dream IT Job with Confidence
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy
/22059/)\[NEW\] Ultimate AWS Certified AI Practitioner AIF-C01
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/22058
/)Red Teaming | Exploit Development with Assembly and C |MSAC+
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/22057
/)Practical Cisco Networking Labs in Cisco Packet Tracer
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/22056/)Comp
uter Networks Fundamentals
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/22055/)IP Addressing and Subnetting – Zer
o to Hero
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/22054/)Information Security Fundamentals
* [REDEEM OFFER ]
(https://idownloadcoupon.com/udemy/22053/)JN0-664: Juniper Network Professional Security Practice 2024
* [REDEEM OFFER ]
(https://idownloadcoupon.com/udemy/22052/)Professional Diploma in CRM Platforms Management
* [REDEEM OFFER ](https://ido
wnloadcoupon.com/udemy/22051/)JavaScript Coding Interview Questions \[with SOLUTIONS\]
* [REDEEM OFFER ](https://idownlo
adcoupon.com/udemy/22050/)Essential Microsoft Excel from Beginner to Advance level
* [REDEEM OFFER ](https://idownloadco
upon.com/udemy/22049/)Android Training & Certification – 49 Projects
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy
/22048/)iOS 11 Mobile Development and Certification – iPhone & iPad
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/
22047/)Wireshark Ninja | Mastering Real Wireshark PROALL|2023WSHRK+
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/
22046/)Mastering Network Security: Defending Against Cyber Threats
* Facebook Ads Marketing – Start Lead Generation Busi
ness 2023
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/22045/)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy
/22044/)6 Practice Tests – AWS Certified Architect Professional
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/2204
3/)Capcut Ninja: Mastering Video Editing Basics to Advanced
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/22042/)J
ava Network Programming – Mastering TCP/IP : CJNP+ JAVA+
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/22041/)Crim
inology and Criminal Psychology | Certified CSI+ Course
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/22040/)The C
omplete Photoshop Masterclass: From 0 to Hero
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/22039/)Passive Income 
By Making Udmy Courses 2023
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/22038/)Build Shopify store & Run Faceboo
k Page Likes Ad In 2023
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/22037/)Configuración y Optimizacion de tu Pá
gina de Facebook 2023
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/22036/)Register Company in UK Get paypal & Str
ipe Business Hindi
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/22035/)Facebook Conversions Ads Marketing For Sel
ling Products 2023
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/22034/)Facebook Ads And Marketing – Lead Generati
on Pro
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/22033/)Google Adwords Crash Course 2023
* [REDEEM OFFER ](htt
ps://idownloadcoupon.com/udemy/22032/)Run Search Ad In Google Ads & Easy SEO For Beginners-2023
* [REDEEM OFFER ](https:
//idownloadcoupon.com/udemy/22031/)Facebook Ads Marketing For Events Organic & Paid Strategy
* [REDEEM OFFER ](https://i
downloadcoupon.com/udemy/22030/)Facebook Ads Lead Generation Marketing for business
* Digital Marketing Business With Go
ogle My Business
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/22029/)
* [REDEEM OFFER ](https://idownloadcoupon.co
m/udemy/22028/)Facebook Ads & Facebook Marketing Funnel Crash Course- 2023
* [REDEEM OFFER ](https://idownloadcoupon.com
/udemy/22027/)Run Digital Marketing Ad Using Google Adwords Express
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/
22026/)Facebook Ads Google My Business & Google Ads (Adwords) 2023
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/2
2025/)Facebook Marketing & Facebook Ads Course For Beginners 2023
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/22
024/)Facebook Ads Marketing Crash Course Traffic & leads – 2023
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/2202
3/)Google Ads And Tiktok Ads Crash Course (Hindi/ Urdu)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/22022/)How T
o Edit Viral Shorts In CapCut
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/22021/)Tiktok Marketing & Shopify Ecom
merce store (hindi/urdu)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/22020/)Color Theory: Learn The Art and Scie
nce of Colors
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/22019/)Ultimate Photoshop Mock-Up Creation Course
* [R
EDEEM OFFER ](https://idownloadcoupon.com/udemy/22018/)Digital Marketing Business Online For Free Social Media
* [REDEEM
 OFFER ](https://idownloadcoupon.com/udemy/22017/)Canva Design Crash Course
* [REDEEM OFFER ](https://idownloadcoupon.co
m/udemy/22016/)Secret Facebook Ads Targeting Pro Stratigies 2023 In Hindi
* [REDEEM OFFER ](https://idownloadcoupon.com/
udemy/22015/)Design Principles, Typography & Color Theory in 1 MegaCourse
* [REDEEM OFFER ](https://idownloadcoupon.com/
udemy/22014/)Facebook Marketing + Whatsapp Ads (CASE STUDY) Hindi 2023
* Google Ads Mastery\~ Beginner To Pro \~ HINDI/U
RDU 2023
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/22013/)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/
22012/)Tiktok Ads marketing Crash Course For Beginners (Hindi/Urdu)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/
22011/)Facebook Pixel Tracking Shopify \~ Apple iOS14 \~ Ecommerce
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/2
2010/)Como crear y configurar tu canal de Youtube desde cero 2023
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/22
009/)Product Hunting for Dropshipping stores
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/22008/)Get 10,000 faceb
ook page followers at cheap Hindi
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/22007/)Learn Camtasia Video Editin
g Masterclass Professional
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/22006/)Facebook Ads & Ecommerce Easy Cour
se 2023 Hindi
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/22005/)Easy Instagram Marketing In Hindi
* [REDEEM OFF
ER ](https://idownloadcoupon.com/udemy/22004/)Facebook Ads Marketing In Hindi/Urdu 2023
* [REDEEM OFFER ](https://idownl
oadcoupon.com/udemy/22003/)The Complete Illustrator Masterclass: From 0 to Hero
* [REDEEM OFFER ](https://idownloadcoupo
n.com/udemy/22002/)Building a shopify store and CJ dropshipping
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/2200
1/)Marketing en Facebook Ads – Leads /Clientes Potenciales 2023
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/2200
0/)Facebook Ads Marketing Targeting Strategies \~Hindi 2023
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/21999/)F
acebook Ads Targeting Strategies For Success Fast 2023
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/21998/)Get Fo
llowers And engagement with Facebook Ads (easy mode)
* Estrategias Pro de Targeting de Audiencia con Facebook Ads
* [RED
EEM OFFER](https://idownloadcoupon.com/udemy/21997/)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/21996/)CSS Fund
amentals: Comprehensive Training for Web Developers
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/21995/)GRE Maste
ry: 5 Comprehensive Practice Tests
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/21994/)DEA-1TT4: Dell EMC Associa
te Practice test 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/21993/)Seo Training Masterclass 2024 : Beginne
r to Advance Startegy
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/21992/)Professional Diploma in Office Administ
ration Management
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/21991/)DES-1423: Dell EMC Specialist Isilon Soluti
on Practice test
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/21990/)DES-1D12: Dell EMC Specialist – Midrange Sto
rage Solutions
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/21989/)DES-6322: Dell EMC Specialist VxRail Appliance
 Practice test
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/21988/)C1000-010: IBM Cloud Pak for Data v4.x Practic
e test 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/21987/)E20-555: Dell EMC Isilon Solution and Design Spec
ialist Exam
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/21986/)E20-393: Dell EMC Unity Solution Specialist Pract
ice test 24
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/21985/)DEA-41T1: Dell EMC PowerEdge Associate Practice t
est 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/21984/)5V0-22.23: VMware Certified Professional – VMware vS
AN 8.x
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/21983/)Professional Diploma in Digital Products Management
* 
[REDEEM OFFER ](https://idownloadcoupon.com/udemy/21982/)Hands-On Python Machine Learning with Real World Projects
* How
 neuromarketing can influence buying behavior
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/21981/)
* [REDEEM OFFER
 ](https://idownloadcoupon.com/udemy/21980/)The Complete Growth Mindset Course – The Mindset for Success
* [REDEEM OFFER
 ](https://idownloadcoupon.com/udemy/21979/)Home Workout Habits in 10 Min – Fitness for Busy-Lazy People
* [REDEEM OFFER
 ](https://idownloadcoupon.com/udemy/21978/)The Complete Talking Head Video Production Masterclass
* [REDEEM OFFER ](htt
ps://idownloadcoupon.com/udemy/21977/)Unlocking the Power of Relative Clauses in English language
* [REDEEM OFFER ](http
s://idownloadcoupon.com/udemy/21976/)Body Language in the Workplace
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/
21975/)Persuasion in Business Communications
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/21974/)Laravel 10 Essen
tials: User Roles & Permissions with Spatie
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/21973/)HTML5 Certificati
on Prep: Comprehensive Practice Tests
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/21972/)Bootstrap Mastery: Buil
d Responsive Websites Like a Pro
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/21971/)Complete jQuery Masterclass:
 From Beginner to Expert
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/21970/)JavaScript Mastery From Basics to Ad
vanced
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/21969/)ChatGPT Mastery: From Creative Writing to Coding Solut
ions
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/21968/)CSS3 Certification Prep: Comprehensive Practice Tests
* 
[REDEEM OFFER ](https://idownloadcoupon.com/udemy/21967/)Dart Mastery – Become a Dart Master From Zero to Hero
* [REDEEM
 OFFER ](https://idownloadcoupon.com/udemy/21966/)HTML5 CSS3 and JavaScript for Beginners: From Zero to Hero
* Mastering
 Postman: A Comprehensive API Testing Course
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/21965/)
* [REDEEM OFFER 
](https://idownloadcoupon.com/udemy/21964/)Laravel and Postman Rest API Development: Beginner to Pro
* [REDEEM OFFER ](h
ttps://idownloadcoupon.com/udemy/21963/)Wealth Creation Blueprint: From 9 to 5 to Financial Freedom
* [REDEEM OFFER ](ht
tps://idownloadcoupon.com/udemy/21962/)Frontend Web Development HTML5 CSS3 JavaScript and Bootstrap
* [REDEEM OFFER ](ht
tps://idownloadcoupon.com/udemy/21961/)cPanel Essentials: Mastering Web Hosting Management
* [REDEEM OFFER ](https://ido
wnloadcoupon.com/udemy/21960/)HTML5 CSS3 JavaScript Bootstrap and Jquery Masterclass
* [REDEEM OFFER ](https://idownload
coupon.com/udemy/21959/)Public Speaking Skills: Give a Great Informational Speech
* [REDEEM OFFER ](https://idownloadcou
pon.com/udemy/21958/)Dart and Flutter: The Ultimate Mobile App Development Course
* [REDEEM OFFER ](https://idownloadcou
pon.com/udemy/21957/)HTML and CSS for Web Designers: From Basics to Beautiful
* [REDEEM OFFER ](https://idownloadcoupon.
com/udemy/21956/)Sales Skills Training: Free Sales Generation Seminars
* [REDEEM OFFER ](https://idownloadcoupon.com/ude
my/21955/)Presentation Skills -Deliver an Excellent Ceremonial Speech
* [REDEEM OFFER ](https://idownloadcoupon.com/udem
y/21954/)Public Speaking: Speak Like a High-Powered Executive
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/21953/
)Complete Good Sleep Habits Course – Sleep Better Tonight!
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/21952/)Co
mplete Willpower Course – Build Self Control & Good Habits
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/21951/)Pe
rsuasion: Give a Persuasive Presentation
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/21950/)The Complete Virtual
 Sales Presentation Course Sales Skills

GET MORE FREE ONLINE COURSES WITH CERTIFICATE – [CLICK HERE](https://idownloadc
oupon.com/)
```
---

     
 
all -  [ Autogen needs improvement. How no one felt the need for call back function ](https://www.reddit.com/r/LangChain/comments/1ghcvi5/autogen_needs_improvement_how_no_one_felt_the/) , 2024-11-04-0913
```
I know this is langchain subreddit but thought to discuss here as most agent developers are there..

I have been playing
 with autogen for few hours to understand.
I immediately felt two needs,
Suppose there are two agents, writer and review
er. 
The termination condition is when reviewer gives it rating of 8 or more.
My need is execution of certain functions 
when this terminal condition is met, currently what i found is only way is custom implementation.
Second, 
For human in 
the loop, I don't want my user to enter prompt via terminal, I need it to be through WhatsApp message or some slack inte
gration. How do I do this?

Suggestions are welcomed. Or any other framework with these features.. 
```
---

     
 
all -  [ Integrating External REST API LLM Calls with LangGraph ](https://www.reddit.com/r/LangChain/comments/1ghc5pg/integrating_external_rest_api_llm_calls_with/) , 2024-11-04-0913
```

I'm working on implementing an agent system using LangGraph, but with a twist - my LLM calls need to go through a REST 
API service instead of using direct LLM integrations.

- Using LangGraph for agent orchestration
- Need to make LLM call
s via REST API endpoints
- Looking to build a custom agent that works with this architecture

1. Is it possible to integ
rate external REST API calls for LLM interactions within the LangGraph framework?
2. Are there any examples or best prac
tices for creating custom agents that use HTTP requests instead of direct LLM integrations?
3. What would be the recomme
nded approach to handle asynchronous REST API calls in this context?

## Technical Details Needed
- Best way to wrap RES
T API calls within LangGraph's expected interfaces
- How to handle authentication and session management
- Proper error 
handling and retry mechanisms
- State management considerations

Any guidance, examples, or pointers to relevant documen
tation would be greatly appreciated. Thank you!
```
---

     
 
all -  [ Fuzzy matching medical terminology using AI ](https://www.reddit.com/r/learnprogramming/comments/1ghb3ei/fuzzy_matching_medical_terminology_using_ai/) , 2024-11-04-0913
```
Have a txt file with 2 columns, description and corresponding code. Need help intelligently matching user inputted free-
form text to the description, and returning the corresponding code.



Background:

I am building a medical pricing webs
ite. The user inputs free form text (à la Google) describing the condition and receives pricing at local hospitals.

Med
ical billing is a labyrinth, separated into inpatient and outpatient services and diagnosis codes. A diagnosis code (ICD
10) will usually translate into an inpatient code (DRG), but not always. Other times, ICD10 codes will translate to the 
wrong DRG code. 

I have been using a forward searching approach, searching first for the ICD10 code and translating it 
to a DRG. As an example, a search for 'heart transplant' yields the ICD10 code Z94.1 which corresponds to DRGs 314-316 (
'Other Circulatory System Diagnoses'). In fact, DRGs 001 and 002 ('Heart Transplant') are more correct, but do not have 
a corresponding ICD10 code. 

[CMS.gov](http://CMS.gov) has appendices that list exactly which ICD10 corresponds with wh
ich DRG as well as DRG numbers and descriptions. Not all DRGs have a corresponding ICD10 code, so **I will have to match
 the user-inputted free form text to DRGs directly.**



Things I have explored:

String matching using Jaccard Distance
/ Levenshtein Distance/ Jaro-Winkler: not the best since most laypeople will not know the exact medical terminology ('sn
oring' symptom vs 'sleep apnea' medical term)

Zero-shot approach with Gemini and OpenAI. Both AIs will hallucinate and 
return the wrong DRGs. 

* Fine tuning: OpenAI, Gemini, and Llama3.2 both require a question and answer dataset, best if
 50 examples per classification (DRG code). This is... not easy and probably not going to be very accurate. Hard to gues
s what a user might input in free form text.
* Corpus of documents for Retrieval Augmented Generation (RAG): LangChain V
ectara, Gemini, Vertex AI for RAG: This is a promising option but examples on the [Vectara](https://python.langchain.com
/v0.1/docs/integrations/providers/vectara/vectara_summary/) site show that this approach is better for summarizing, or r
etrieving relevant 'chunks', than strict regurgitation.
* Vertex AI for tabular data: similar challenges with providing 
examples for fine tuning
* QLoRA/ LoRA: probably much more technically oriented and more than I need, also increased har
dware requirements.

Giving OpenAI/ Gemini a complete list of all the DRG descriptions with each prompt, asking the AI t
o match with the appropriate entry. This would use a large number of tokens ($) for every prompt. Is there a way to keep
 this in memory? Is that what the Corpus is? If I provide a text file as a document in the Corpus, is the AI smart enoug
h to match the user input to the DRG description in the file and return the corresponding DRG code in the file in a diff
erent column?
```
---

     
 
all -  [ Tools / guidance  ](https://www.reddit.com/r/LocalLLM/comments/1gha8gy/tools_guidance/) , 2024-11-04-0913
```
I want to create a model that analyzes specific books I've selected about coding and other related topics. My goal is fo
r this model to help integrate new features into the app, acting as a consultant by leveraging the knowledge from these 
books as well as the app's source code that I provide. I've already developed a basic model using LangChain and LLaMA th
at retrieves answers from the books, but I’m unsure how to proceed from this point. What steps should I take next to enh
ance this model? 
```
---

     
 
all -  [ Langchain SelfQueryRetriever unable to read Structured Query ](https://www.reddit.com/r/LangChain/comments/1gh8exz/langchain_selfqueryretriever_unable_to_read/) , 2024-11-04-0913
```
Anyone using SelfQueryRetriever? I am trying to implement this retriever to create a RAG Chatbot. However, the retriever
 seems to have trouble reading my Structured Query. I have already tried both SelfQueryRetriever() and SelfQueryRetrieve
r.from\_llm(), and they both give different errors. 

Appreciate if anyone has any experience in this, thanks!
```
---

     
 
all -  [ CCD ETL via LangGraph ](https://youtu.be/gZYu45aw3Hw?si=r5QWuGELvSE9rh-p) , 2024-11-04-0913
```
Built a tool for extracting healthcare CCD data into custom schemas. This can speed up building of interfaces for connec
ting hospitals, providers and independent practices to each other and to HIE’s.
```
---

     
 
all -  [ When using `with_structured_output` with pydantic BaseModel, does the Field description do anything? ](https://www.reddit.com/r/LangChain/comments/1ggvkf7/when_using_with_structured_output_with_pydantic/) , 2024-11-04-0913
```
Basically the title. I am experimenting the \`with\_structured\_output\` and I find that the llm uses the variable name 
to know what to populate. 

`phrases_with_dumb: list[str]`

I thought the pydantic's Field description would affect the 
behavior too, but seems like it's not affecting how the model generates the data. 

`phrases: list[str] = Field(descript
ion='list of phrases with the word dumb')`

So should I assume that Field description is not used when the model generat
es the data? 
```
---

     
 
all -  [ Get responses longer than the llm context window ](https://www.reddit.com/r/LangChain/comments/1ggv50c/get_responses_longer_than_the_llm_context_window/) , 2024-11-04-0913
```
Hi, is there a way to get a response longer than the allowed context window e.g by using loops or threads. In gpt ui for
 instance, I'd instruct it to let me know if there's more and continue when I respond with continue. Thanks for the help

```
---

     
 
all -  [ VERY slow Document creation ](https://www.reddit.com/r/LangChain/comments/1ggt5r7/very_slow_document_creation/) , 2024-11-04-0913
```
Hey! Im trying to create Langchain [Document](https://python.langchain.com/v0.2/api_reference/core/documents/langchain_c
ore.documents.base.Document.html#langchain_core.documents.base.Document) objects from JSON objects, but Document creatio
n is taking *VERY* long. using tqdm, im seeing 30-40i/s, then a pause for 10 seconds, dip to 3i/s for 20 seconds, then b
ack up to 20i/s, ect. ect.

`tqdm import tqdm`  
`from langchain_core.documents import Document`  
`from langchain_commu
nity.graph_vectorstores.links import METADATA_LINKS_KEY, Link`  
`import jsondef create_documents(json_file):`  
`docume
nts = {}`  
  
`with tqdm(desc='Creating documents', mininterval=1) as pbar:`  
`for line in json_file:`  
`if not line.
strip():`  
`continue`  
  
`line_data = json.loads(line)`  
`source, targets = next(iter(line_data.items()))`  
  
`# C
reate set of links more efficiently`  
`links = {`  
`Link.outgoing(kind='href', tag=target)`  
`for target in targets` 
 
`}`  
`links.add(Link.incoming(kind='href', tag=source))`  
  
`documents[source] = Document(`  
`id=source,`  
`page_
content='',`  
`metadata={`  
`'content_id': source,`  
`METADATA_LINKS_KEY: list(links)`  
`}`  
`)`  
  
`print(f'Samp
le of documents:')`  
`for i, (title, doc) in enumerate(list(documents.items())[:5]):`  
`print(f'Document {i+1}:')`  
`
print(f'  Title: {title}')`  
`print(f'  ID: {doc.id}')`  
`print(f'  Content ID: {doc.metadata['content_id']}')`  
`pri
nt(f'  Number of links: {len(doc.metadata[METADATA_LINKS_KEY])}')`  
`print(f'  Sample links: {doc.metadata[METADATA_LIN
KS_KEY][:5]}')`  
`print()`  
  
`return documentswith open('test.json', 'r', encoding='utf-8') as json_file:`  
  `prin
t(f'Data loaded from 'links.json'')`  
  `print('Creating documents...')`  
  `documents = create_documents(json_file)` 
 
  `print(f'Created {len(documents)} documents')`



Anyone know whats going on?
```
---

     
 
all -  [ What is the other best alternative to LangGraph? ](https://www.reddit.com/r/LangChain/comments/1ggrqis/what_is_the_other_best_alternative_to_langgraph/) , 2024-11-04-0913
```
I am a software engineer with 5+ years of experience and decent experience with LangChain. Over the past week, I am buil
ding a stock analyst agent on LangGraph, and the experience has been terrible.

The documentation and tutorials make me 
feel dumb, even simple tasks seem unnecessarily difficult, which has left me frustrated. I’ve decided not to proceed wit
h LangGraph for the time being,I just can’t imagine using it to build 10-20 more nodes.

Is there an alternative on the 
market today that any of you are using? Ideally, something in async Python.
```
---

     
 
all -  [ Is this possible? ](https://www.reddit.com/r/LangChain/comments/1ggqtad/is_this_possible/) , 2024-11-04-0913
```
I have a JSON dataset of the format:
[
{
key1: val1,
key2: val2,
key3: val3,
...
}
{
key1: val1,
key2: val2,
key3: val3

...
}
...
]

There is data in one key which relates to another one.

Is it possible to build a RAG chatbot, in such a wa
y that it accepts dynamic inputs and gives answers based on the key.

[1] For instance, let's say key1 is dog and key2 i
s cat, the rag chatbot should detect from the chat input if it contains cat or dog and should return  the value based on
 the key. If the chat message contains anything related to dog in it, it should return the answer from the dog key else 
if the message has anything related to catch in it, it should return from the cat key.

[2] The RAG model should also ge
nerate outcome based on the following scenario: let's say if the value4 and value5 depends on what is given in value3.


[3]Another case is, value5 and value6 are numbers. The chatbot RAG should make sure it provides information in such a wa
y that if the user mentions any number and the number is in between value5 and value6, it should return the output from 
value4 or value5 based on the logic in point [1]


Could you guys please let me know if this is possible, cause i couldn
't find any example over the internet. 
```
---

     
 
all -  [ AWS certification for GenAI after AI practitioner? ](https://www.reddit.com/r/AWSCertifications/comments/1ggpbv2/aws_certification_for_genai_after_ai_practitioner/) , 2024-11-04-0913
```
Is there a good certification to do specifically for GenAI on AWS? I'm more interested in leveraging GenAI tools and not
 on the usual route of ML sagemaker models etc.

If not, what other certifications do you recommend tailored for GenAI? 
I'm right now working with OpenAI and want to go deeper into aspects of finetuning, perhaps may langchain etc. 

Sorry, 
just posting a long question, but my intent is to get a certification while also working on my startup idea. Right now, 
I'm mostly doing prompt engineering and some AWS plumbing and hence finding ways of expanding my horizons.
```
---

     
 
all -  [ Jupyter not honoring Conda environments? ](https://www.reddit.com/r/JupyterNotebooks/comments/1ggmaty/jupyter_not_honoring_conda_environments/) , 2024-11-04-0913
```
Hi all!

I've been using jupyter on an off for a while, but I need to start using it a lot more regularly, and I need to
 integrate with conda virtual environments.

Working on a new ubuntu 24.04 install, I installed Anaconda, then created a
 new virtual environment and installed jupyter:

    conda create -n jupyter python=3.12
    conda activate jupyter
    
pip install jupyterlab
    jupyter lab
    ... 

So far so good, everything running as expected. So I then create anothe
r conda environment for a new project and register it with jupyter via ipykernel.

    conda create -n rag-llama3.2 pyth
on=3.11
    conda activate rag-llama3.2
    python -m ipykernel install --user --name=rag-llama3.2

The ipykernel part w
as completely new to me, I was following a medium post: [https://medium.com/@nrk25693/how-to-add-your-conda-environment-
to-your-jupyter-notebook-in-just-4-steps-abeab8b8d084](https://medium.com/@nrk25693/how-to-add-your-conda-environment-to
-your-jupyter-notebook-in-just-4-steps-abeab8b8d084)

So I now have jupyter running in its own conda env, and a new env 
to use for my project. This is where things get very strange. I jump in to the jupyter console, create a new notebook, a
nd select the newly registered kernel from the dropdown, all seems fine. I start installing a few packages and writing a
 little code:

    ! pip install langchain-nomic
    ! pip install -qU langchain-ollama
    ! pip list | grep langchain

    langchain-core            0.3.14
    langchain-nomic           0.1.3
    langchain-ollama          0.2.0

Packages i
nstalled, so I begin with an import:

    # LLM using local Ollama
    
    ### LLM
    from langchain_ollama import Cha
tOllama
    
    local_llm = 'llama3.2:3b-instruct-fp16'
    docker_host = 'http://127.0.0.1:11434'
    
    llm = ChatO
llama(model=local_llm, temperature=0, api_base_url=docker_host)
    llm_json_mode = ChatOllama(model=local_llm, temperat
ure=0, format='json', api_base_url=docker_host)

Computer says no!

    ------------------------------------------------
---------------------------
    ModuleNotFoundError                       Traceback (most recent call last)
    Cell In[
4], line 4
          1 # LLM using local Ollama
          2 
          3 ### LLM
    ----> 4 from langchain_ollama impor
t ChatOllama
          6 local_llm = 'llama3.2:3b-instruct-fp16'
          7 docker_host = 'http://127.0.0.1:11434'
    

    ModuleNotFoundError: No module named 'langchain_ollama'------------------------------------------------------------
---------------
    ModuleNotFoundError                       Traceback (most recent call last)
    Cell In[4], line 4
 
         1 # LLM using local Ollama
          2 
          3 ### LLM
    ----> 4 from langchain_ollama import ChatOllama

          6 local_llm = 'llama3.2:3b-instruct-fp16'
          7 docker_host = 'http://127.0.0.1:11434'
    
    ModuleN
otFoundError: No module named 'langchain_ollama'

So the modules are installed, but I can't import them. At this point I
 started hunting around and found a few commands to help identify the problem:

    !jupyter kernelspec list --json
    

    {
      'kernelspecs': {
        'python3': {
          'resource_dir': '/home/gjws/anaconda3/envs/jupyter/share/ju
pyter/kernels/python3',
          'spec': {
            'argv': [
              'python',
              '-m',
          
    'ipykernel_launcher',
              '-f',
              '{connection_file}'
            ],
            'env': {},
  
          'display_name': 'Python 3 (ipykernel)',
            'language': 'python',
            'interrupt_mode': 'signa
l',
            'metadata': {
              'debugger': true
            }
          }
        },
        'rag-llama3.2'
: {
          'resource_dir': '/home/gjws/.local/share/jupyter/kernels/rag-llama3.2',
          'spec': {
            'a
rgv': [
              '/home/gjws/anaconda3/envs/rag-llama3.2/bin/python',
              '-Xfrozen_modules=off',
       
       '-m',
              'ipykernel_launcher',
              '-f',
              '{connection_file}'
            ],
  
          'env': {},
            'display_name': 'rag-llama3.2',
            'language': 'python',
            'interrup
t_mode': 'signal',
            'metadata': {
              'debugger': true
            }
          }
        }
      }

    }
    /home/gjws/anaconda3/envs/jupyter/bin/python{
      'kernelspecs': {
        'python3': {
          'resource_
dir': '/home/gjws/anaconda3/envs/jupyter/share/jupyter/kernels/python3',
          'spec': {
            'argv': [
     
         'python',
              '-m',
              'ipykernel_launcher',
              '-f',
              '{connectio
n_file}'
            ],
            'env': {},
            'display_name': 'Python 3 (ipykernel)',
            'language
': 'python',
            'interrupt_mode': 'signal',
            'metadata': {
              'debugger': true
          
  }
          }
        },
        'rag-llama3.2': {
          'resource_dir': '/home/gjws/.local/share/jupyter/kernels/
rag-llama3.2',
          'spec': {
            'argv': [
              '/home/gjws/anaconda3/envs/rag-llama3.2/bin/pytho
n',
              '-Xfrozen_modules=off',
              '-m',
              'ipykernel_launcher',
              '-f',
  
            '{connection_file}'
            ],
            'env': {},
            'display_name': 'rag-llama3.2',
      
      'language': 'python',
            'interrupt_mode': 'signal',
            'metadata': {
              'debugger': 
true
            }
          }
        }
      }
    }
    
    !which -a python
    /home/gjws/anaconda3/envs/jupyter/b
in/python

So to my untrained eyes, jupyter is seeing both the jupyter conda environment and the rag-llama3.2 environmen
t and getting confused.

Now I don't know where to go.

Have I done something fundamentally wrong?

Should I NOT be runn
ing jupyter in its own venv and just install it globally?

Have I screwed up the ipykernel steps somewhere?

Any help wo
uld be much appreciated. I've been at this for hours and have hit a brick wall :(

Thanks for taking the time to read al
l this!!!
```
---

     
 
all -  [ Which version is better, the shorter or longer one? I've changed my carrer. ](https://www.reddit.com/r/resumes/comments/1ggm0mc/which_version_is_better_the_shorter_or_longer_one/) , 2024-11-04-0913
```
[Long Version](https://preview.redd.it/2ytulhse05yd1.png?width=1172&format=png&auto=webp&s=203467d1c9fb5b63f4b973c348b91
eca6d7399bc)

  


[Short Version](https://preview.redd.it/8mff2rhk05yd1.png?width=1171&format=png&auto=webp&s=35bfbc3a5
9e965629d49b174519825b4c3f3d94f)

  
The short version deletes my former experience and moves a 'Collaborative Project' 
from 'Experience' to the 'Projects Highlights' section, where I leave only 3 projects. The long version has more info: m
ore projects and more experience, with the collaborative project as an experience.

I prefer the short one, because I pu
t all the most important info on the first page, but I want to make sure that the info I don't show on this version is n
ot THAT important.

Any opinions?

Thanks in advance.
```
---

     
 
deeplearning -  [ Fast AI's deep learning for coders by jeremy howard for begginer?  ](https://www.reddit.com/r/deeplearning/comments/1gb2k3p/fast_ais_deep_learning_for_coders_by_jeremy/) , 2024-11-04-0913
```
I am a full stack python developer who do web dev in django

I am now starting deep learning,i am a compelete begginer


(Have worked with pandas,numpy,matplotlib,langchain only)

I wanna ask,should i do this course,will i understand what he
 is coding and code myslef

I just dont want to do blind coding,i wanna learn what is the purpose,how it works and how t
o do it

Will this course teach me that or not?

Thanks in advance
```
---

     
