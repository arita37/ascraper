 
all -  [ Display charts and images generated from a python agent ](https://www.reddit.com/r/LangChain/comments/1c10vvb/display_charts_and_images_generated_from_a_python/) , 2024-04-11-0910
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

     
 
all -  [ Langchain Cache - Any way to define a custom cache key? ](https://www.reddit.com/r/LangChain/comments/1c0y53d/langchain_cache_any_way_to_define_a_custom_cache/) , 2024-04-11-0910
```
e.g. like this:  
[https://docs.litellm.ai/docs/caching/redis\_cache#custom-cache-keys](https://docs.litellm.ai/docs/cac
hing/redis_cache#custom-cache-keys)  


would be nice to have non-hash keys e.g, for searching in Redis GUI
```
---

     
 
all -  [ Advice needed on orchestrating a multi-agent conversational AI with chat history retention ](https://www.reddit.com/r/LangChain/comments/1c0xi7a/advice_needed_on_orchestrating_a_multiagent/) , 2024-04-11-0910
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

     
 
all -  [ Used Claude's 200K context length to write a 30K word novel which heavily grounds in details unlike  ](https://www.reddit.com/r/LangChain/comments/1c0w79c/used_claudes_200k_context_length_to_write_a_30k/) , 2024-04-11-0910
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

     
 
all -  [ Putting your Function-call tools to an Online Hub and Use in CrewAI, LangChain and AutoGen with Auto ](https://www.reddit.com/r/LocalLLaMA/comments/1c0uyjj/putting_your_functioncall_tools_to_an_online_hub/) , 2024-04-11-0910
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

     
 
all -  [ GitHub - Upsonic/Tiger: Neuralink for your AI Agents ](https://www.reddit.com/r/crewai/comments/1c0tsu6/github_upsonictiger_neuralink_for_your_ai_agents/) , 2024-04-11-0910
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

     
 
all -  [ Allow Chatbot to Correct Itself to User Feedback ](https://www.reddit.com/r/LangChain/comments/1c0t2tt/allow_chatbot_to_correct_itself_to_user_feedback/) , 2024-04-11-0910
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

     
 
all -  [ Learning to fine tune models to write content in my voice ](https://www.reddit.com/r/OpenAI/comments/1c0szuw/learning_to_fine_tune_models_to_write_content_in/) , 2024-04-11-0910
```
Whats a good resource to start on this?

Broadly speaking I already understand how to use OpenAI's API to send simple me
ssages back and forth. But I'm not familiar with fine tuning or anything more complex.

I'd really like how to do this i
n a way that's LLM-agnostic, I've dabbled in LangChain a little which I assume is key tot this, but in absence of that w
ill gladly start with OpenAI specific learnings.
```
---

     
 
all -  [ What vector database do you use?  ](https://www.reddit.com/r/LangChain/comments/1c0srpo/what_vector_database_do_you_use/) , 2024-04-11-0910
```

```
---

     
 
all -  [ Best Method to Quickly and Easily Deploy? ](https://www.reddit.com/r/LangChain/comments/1c0rvek/best_method_to_quickly_and_easily_deploy/) , 2024-04-11-0910
```
I used Gradio to deploy, which is quick and easy. What’s the easiest way to add stripe payment collection for subscripti
on?
```
---

     
 
all -  [ Prompt templates in LangChain ](https://www.reddit.com/r/LangChain/comments/1c0qjq2/prompt_templates_in_langchain/) , 2024-04-11-0910
```
I wrote a piece on [prompt templates in LangChain](https://www.mirascope.io/post/langchain-prompt-template), how they wo
rk and the different approach [Mirascope](https://github.com/Mirascope/mirascope) takes with colocation. I hope you find
 it useful.
```
---

     
 
all -  [ Beginner to LangChain. Need help! - [Stock Annual Report PDF Chatbot using RAG]. ](https://www.reddit.com/r/LangChain/comments/1c0q8qm/beginner_to_langchain_need_help_stock_annual/) , 2024-04-11-0910
```
Hello! I'm a LangChain beginner and I need some help.

I'm working a PDF Chatbot that takes in a stock annual report as 
a PDF and does technical question answering on it \[Mathematical\] - Please help me! How do I approach this problem and 
where do I begin? I'll take any help I can.

I've been trying to do this with RAG. Any Suggestions? Thank you.

&#x200B;

```
---

     
 
all -  [ Learning to fine tune models to write content in my voice ](https://www.reddit.com/r/ChatGPT/comments/1c0q4p8/learning_to_fine_tune_models_to_write_content_in/) , 2024-04-11-0910
```
Whats a good resource to start on this?

Broadly speaking I already understand how to use OpenAI's API to send simple me
ssages back and forth. But I'm not familiar with fine tuning or anything more complex.

I'd really like how to do this i
n a way that's LLM-agnostic, I've dabbled in LangChain a little which I assume is key tot this,  but in absence of that 
will gladly start with OpenAI specific learnings. 
```
---

     
 
all -  [ I am coming back to LangChain! ](https://www.reddit.com/r/LangChain/comments/1c0oucr/i_am_coming_back_to_langchain/) , 2024-04-11-0910
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

     
 
all -  [ Adding tools to ConversationalRetrievalChain.from_llm causes Pydantic error ](https://www.reddit.com/r/LangChain/comments/1c0mkl4/adding_tools_to_conversationalretrievalchainfrom/) , 2024-04-11-0910
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

     
 
all -  [ How to make use of Complete GPU memory? ](https://www.reddit.com/r/LangChain/comments/1c0k4oh/how_to_make_use_of_complete_gpu_memory/) , 2024-04-11-0910
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

     
 
all -  [ LangChain E-Mails with LLM ](https://www.reddit.com/r/LangChain/comments/1c0k2qo/langchain_emails_with_llm/) , 2024-04-11-0910
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

     
 
all -  [ How to make use of Complete GPU memory? ](https://www.reddit.com/r/u_Dear_Insect_5295/comments/1c0jwxy/how_to_make_use_of_complete_gpu_memory/) , 2024-04-11-0910
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

     
 
all -  [ Seeking Guidance: Running Mixtral 8x7B on AWS ](https://www.reddit.com/r/MistralAI/comments/1c0grhr/seeking_guidance_running_mixtral_8x7b_on_aws/) , 2024-04-11-0910
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

     
 
all -  [ What tools are you using for developing AI apps? ](https://www.reddit.com/r/LocalLLaMA/comments/1c0f6eu/what_tools_are_you_using_for_developing_ai_apps/) , 2024-04-11-0910
```
We obviously know about the LangChains and LlamaIndex. What are some promising AI frameworks/libraries/repos that are be
coming essential for building AI apps?
```
---

     
 
all -  [ Results of evaluating the AI Oracle approach - a novel way to improve your LLM application's accurac ](https://www.reddit.com/r/LangChain/comments/1c0do04/results_of_evaluating_the_ai_oracle_approach_a/) , 2024-04-11-0910
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

     
 
all -  [ Is there a tool/platform to put an LLM to a large data set of PDF files (like 50GB) ](https://www.reddit.com/r/LangChain/comments/1c0czng/is_there_a_toolplatform_to_put_an_llm_to_a_large/) , 2024-04-11-0910
```
I am a non-tech person looking for a tool to ask questions to my 50GB worth of PDF files. Is there a tool which can help
 me build this project or something which is already there which can help?   


Please share relevant blogs or approache
s to follow. 
```
---

     
 
all -  [ Easiest way to improve RAG chat - help ](https://www.reddit.com/r/LangChain/comments/1c0cnyj/easiest_way_to_improve_rag_chat_help/) , 2024-04-11-0910
```
I'm a bit frustrated. We've been working for more than 6 months on an MVP for a Q&A chat about product documentation. Af
ter all that, the LLM still hallucinates a lot and gives very basic responses. I would love to have, at this time, a sys
tem capable of using several documents to formulate a sound response to a user's question. I'm using GPT-3.5. I know how
 capable the model is, and I hate how basic our chat answers are. Maybe it's the chain, the steps to formulate a respons
e and validate it, or the bad retriever that can't bring useful documents from the user's reduced query... I feel like w
e've tried a lot: few shots, fine-tuning embeddings, fine-tuning the GPT, etc... But somehow, we don't get it to work. I
 just feel we can, but in the end, we don't. Any advice to make a killer LLM-powered chat about product documentation?
```
---

     
 
all -  [ What are the current best practices or techniques to make GPT API digest info from web links, pdfs,  ](https://www.reddit.com/r/chathelp/comments/1c09rnx/what_are_the_current_best_practices_or_techniques/) , 2024-04-11-0910
```
 ''OpenAI Assistants API'' would be your best shot at multiple file formats, if you are looking to build a RAG applicati
on based solely on OpenAI API...

The best answer to this question just 6 months ago would be - ''LlamaIndex, or LangCha
in + OpenAI API''

The best answer to this same question a few months from now would be not to use OpenAI API at all, bu
t maybe Claude, Google Gemini, or a combination of multiple LLMs, via a unified API proxy solution... (Depending on API 
costs, benchmarks, reliability, or any other unforeseen changes...)

So go figure... If you are building a RAG, AI wrapp
er startup, you can burn a lot of time & money right here - choosing the wrong core tech stack...
```
---

     
 
all -  [ [OFFER] Seeking AI Development Expert - $15/hr ](https://www.reddit.com/r/SlaveLabour_OG/comments/1c08g8d/offer_seeking_ai_development_expert_15hr/) , 2024-04-11-0910
```
We are on the lookout for an enthusiastic individual who possesses a solid understanding and expertise in AI development
, particularly with savvy AI tasks and AI tooling. The ideal candidate should have hands-on experience with LangChain an
d other contemporary AI frameworks. This opportunity is perfect for those who consider themselves somewhat of a full-sta
ck developer in the AI domain and are looking for a challenging role to apply their skills.

&#x200B;

Responsibilities:


&#x200B;

Work on advanced AI tasks and contribute to the development and optimization of AI tools.

Engage with vario
us AI frameworks, with a strong emphasis on LangChain, to build and maintain innovative solutions.

Collaborate closely 
with our team to design, develop, and refine AI-driven projects.

Requirements:

&#x200B;

Proven experience in AI devel
opment, including a good understanding of different AI frameworks, especially LangChain.

Strong proficiency in full-sta
ck development as it pertains to AI projects.

Ability to work independently and collaboratively in a fast-paced environ
ment.

A keen interest in staying abreast of the latest developments in AI technologies and frameworks.

Details:

&#x20
0B;

Rate: $15 per hour

Location: Remote

Commitment: Part-time with the possibility of evolving into a full-time role 
based on performance and project requirements.

If you are passionate about AI and thrive in dynamic environments, we wo
uld love to hear from you. Please DM me your resume and a brief cover letter highlighting your experience with AI develo
pment and specific frameworks you have worked with.

&#x200B;

We look forward to embarking on this exciting journey tog
ether and achieving remarkable success with your expertise on our team.
```
---

     
 
all -  [ [OFFER] Seeking AI Development Expert - $15/hr ](https://www.reddit.com/r/DoneDirtCheap/comments/1c08g6z/offer_seeking_ai_development_expert_15hr/) , 2024-04-11-0910
```
We are on the lookout for an enthusiastic individual who possesses a solid understanding and expertise in AI development
, particularly with savvy AI tasks and AI tooling. The ideal candidate should have hands-on experience with LangChain an
d other contemporary AI frameworks. This opportunity is perfect for those who consider themselves somewhat of a full-sta
ck developer in the AI domain and are looking for a challenging role to apply their skills.  
Responsibilities:  
Work o
n advanced AI tasks and contribute to the development and optimization of AI tools.  
Engage with various AI frameworks,
 with a strong emphasis on LangChain, to build and maintain innovative solutions.  
Collaborate closely with our team to
 design, develop, and refine AI-driven projects.  
Requirements:  
Proven experience in AI development, including a good
 understanding of different AI frameworks, especially LangChain.  
Strong proficiency in full-stack development as it pe
rtains to AI projects.  
Ability to work independently and collaboratively in a fast-paced environment.  
A keen interes
t in staying abreast of the latest developments in AI technologies and frameworks.  
Details:  
Rate: $15 per hour  
Loc
ation: Remote  
Commitment: Part-time with the possibility of evolving into a full-time role based on performance and pr
oject requirements.  
If you are passionate about AI and thrive in dynamic environments, we would love to hear from you.
 Please DM me your resume and a brief cover letter highlighting your experience with AI development and specific framewo
rks you have worked with.  
We look forward to embarking on this exciting journey together and achieving remarkable succ
ess with your expertise on our team.
```
---

     
 
all -  [ RetrievalQA chain returning generated answer embedded in prompt even when return_only_outputs=True ](https://www.reddit.com/r/LangChain/comments/1c06txb/retrievalqa_chain_returning_generated_answer/) , 2024-04-11-0910
```
Hi all,

I am using RetrievalQA chain with custom prompt. When invoked with a question it is returning prompt with answe
r embedded in it even when the return_only_outputs is set to True.

I was wondering how can I get only the generated ans
wer without the prompt (System message + Context + Question)?
```
---

     
 
all -  [ How to deploy RAG Chatbot ](https://www.reddit.com/r/Chatbots/comments/1c06b8h/how_to_deploy_rag_chatbot/) , 2024-04-11-0910
```
Hi,  
I can create a chatbot using LangChain or other tools in a Jupyter notebook, and thus can create a \*.py file to d
efine and create the RAG Chatbot. I am having difficulty in figuring out how to deploy the Chatbot, which would have an 
API interface, and then making it available on my WIX website. Any ideas on how to deploy? For some reason I keep thinki
ng about Docker and Kubernetes, or NVidia, or AWS... What are your thoughts? Thanks.
```
---

     
 
all -  [ Need teammates for a RAG hackathon ](https://www.reddit.com/r/LangChain/comments/1c00e4g/need_teammates_for_a_rag_hackathon/) , 2024-04-11-0910
```
So guys there’s vectara’s upcoming hackathon,anybody interested to participate and needs a team.DM me…
```
---

     
 
all -  [ Filling in Null values in a dataset using LLM's ](https://www.reddit.com/r/LocalLLaMA/comments/1bzxw9e/filling_in_null_values_in_a_dataset_using_llms/) , 2024-04-11-0910
```
Hey guys , currently have a small text based dataset consisting of few columns all containing text and has  lot of null 
values .

I would love to fill in null values present in the dataset by synthetically generating the responses and then 
filling it . Tried using Langchain but it isn't able to generate consistently and half the time fails when i would want 
to generate more than 30 odd responses.

Been trying for the past few days. would love to receive help .

do let me know
 asap if there are any resources or links for doing this .feel free to suggest and dm.
```
---

     
 
all -  [ Need help with my chatbot application ](https://www.reddit.com/r/StreamlitOfficial/comments/1bztb1x/need_help_with_my_chatbot_application/) , 2024-04-11-0910
```
I believe it's really simple how to solve it but I don't know how. I'm not really proficient with programming in general
 and I'm stuck with this problem : I'm doing a chatbot on streamlit that use a vector store for its knowledge. But I tri
ed a couple of things, i can't understand how to make it works on streamlit. My problem is that whenever i write my seco
nd message into the chat, my first question (I use the streamlitchathistory from langchain) is being replaced by the thi
ng on the second screenshot.   


Can someone help me and provide me a simple solution ? I'm stuck with this for a few d
ays now.   


&#x200B;

[This is a snippet of my app](https://preview.redd.it/s91txa0gpgtc1.png?width=1031&format=png&au
to=webp&s=45fc9e1aba38cc6358928870f1b788e125c81467)

[Whenever i write my second question, the first one is transformed]
(https://preview.redd.it/nhksxhljpgtc1.png?width=713&format=png&auto=webp&s=570c3cb58a891e87698b47ff8fba3d011be2d055)
```
---

     
 
all -  [ Interacting with LLMs in steps  ](https://www.reddit.com/r/LangChain/comments/1bzsgxa/interacting_with_llms_in_steps/) , 2024-04-11-0910
```
I would like interact with LLMs in sequential way like:

Step 1 : load documents 
Step 2 : ask about the products descri
bed in the documents
Step 3:  based on the response lookup where can I buy these products
Step 4: check if the store has
 other options
…

I am currently doing it in a very basic way. Loading the documents, retrieving using a question, using
 the output as input for another retriever , …
Is there a more sophisticated way of doing it ?
```
---

     
 
all -  [ Comparing Agent Cloud and CrewAI ](https://www.reddit.com/r/AutoGenAI/comments/1bzrxbv/comparing_agent_cloud_and_crewai/) , 2024-04-11-0910
```
A good comparison blog between AI agents.

Agent Cloud is like having your own GPT builder with a bunch extra goodies.


# The Top GUI features Are:

* RAG pipeline which can natively embed 260+ datasources
* Create Conversational apps (like
 GPTs)
* Create Multi Agent process automation apps (crewai)
* Tools
* Teams+user permissions. Get started fast with Doc
ker and our [install.sh](https://install.sh)

Under the hood, Agent Cloud uses the following open-source stack:

* Airtb
yte for its ELT pipeline
* RabbitMQ for message bus.
* Qdrant for vector database.

They're OSS and you can check their 
repo [GitHub](https://github.com/rnadigital/agentcloud)

# CrewAI

CrewAI is an open-source framework for multi-agent co
llaboration built on Langchain. As a multi-agent runtime, Its entire architecture relies heavily on Langchain.

# Key Fe
atures of CrewAI:

The following are the key features of CrewAI:

* **Multi-Agent Collaboration**: Multi-agent collabora
tion is the core of CrewAI’s strength. It allows you to define agents, assign distinct roles, and define tasks. Agents c
an communicate and collaborate to achieve their shared objective.
* **Role-Based Design:** Assign distinct roles to agen
ts to promote efficiency and avoid redundant efforts. For example, you could have an “analyst” agent analyzing data and 
a “summary” agent summarizing the data.
* **Shared Goals**: Agents in CrewAI can work together to complete an assigned t
ask. They exchange information and share resources to achieve their objective.
* **Process Execution**: CrewAI allows th
e execution of agents in both a sequential and a hierarchical process. You can seamlessly delegate tasks and validate re
sults.
* **Privacy and Security**: CrewAI runs each crew in standalone virtual private servers (VPSs) making it private 
and secure.

What are your thoughts, looks like If anyone is looking for a good solution for your RAG then agentcloud pe
ople are doing good job. 

[Blog link](https://dev.to/agentcloud/agent-cloud-vs-crewai-986)
```
---

     
 
all -  [ Data poision in llms  ](https://www.reddit.com/r/LangChain/comments/1bzpcc6/data_poision_in_llms/) , 2024-04-11-0910
```
How can we prevent data poision in llms , for example if our database it self is corrupt and we need llm not to send tha
t data , how can we achieve that 
```
---

     
 
all -  [ OpenAI API key integration mismatch ](https://www.reddit.com/r/LangChain/comments/1bzoc45/openai_api_key_integration_mismatch/) , 2024-04-11-0910
```
I've been using Langchain and Langsmith to create a benchmarking workflow for my LLM prompts. Everything's been working 
well, until I had to delete and re-create my OpenAI API key.

I've updated the API key in the env.py as the main environ
mental variable, and this works- I've tested this with the OpenAI Chat Completion.

I've also updated the API key in Lan
gSmith by going into the requested prompt's playground > Secrets & API keys > updated it manually. I even checked under 
my organization's Settings > Secrets, and see the API key is updated.

However, when I try to use the 'arun\_on\_dataset
' function in the aforementioned Python environment, it gives me an error-

    'AuthenticationError('Error code: 401 - 
{'error': {'message': 'Incorrect API key provided: sk-O6ZSB***************************************TNxS. You can find you
r API key at https://platform.openai.com/account/api-keys.' 

The prefix for the API key the error throws is indeed the 
previous, non-functional API key, but I don't know where else to adjust it so it'll read the current API key.

Nothing w
as changed in the code, which ran well previously, and the only external adjustment was the API key.

Should I change th
e API key elsewhere?

Any thoughts and ideas are welcome!
```
---

     
 
all -  [ Redis as vector database  ](https://www.reddit.com/r/LangChain/comments/1bznz3t/redis_as_vector_database/) , 2024-04-11-0910
```
I am using redis as vector database . I am getting no permission error when adding text to redis using langchain , manua
lly I am able to add it , but getting error when using langchain , can someone suggest an alternative or how can we achi
eve it with langchain 
```
---

     
 
all -  [ How do I send an audio from INMP441 mic connected to ESP32 DevKit V1 to my laptop and also receive a ](https://www.reddit.com/r/esp32/comments/1bznxsc/how_do_i_send_an_audio_from_inmp441_mic_connected/) , 2024-04-11-0910
```
I made a chatbot code in my Mac which answers users queries by listening to the user through my Mac's microphone and giv
es out the answer using text to speech in real time. I'm trying to create a code that uses the INMP441 mic connected to 
my ESP32 DevKit V1 and receive the user's query through wifi, send it to my chatbot code, processs the query and send it
 back to the ESP (through wifi), which will be played out through a speaker. I have a MAX98357A I2S connector connected 
to a speaker.  Basically, my laptop acts like a server which gets the query from the user and answers it back. I'll prov
ide my chatbot code below. I couldn't figure out the right code for the ESP. I tried a lot of codes, yet I end up in one
 of the two problems: 1)The mic doesn't listen 2)The audio will not be sent

Btw I have connected INMP441 to esp32 devki
t v1 in the following manner :

GND TO GND

VDD TO 3V3

SD TO D33

L/R TO GND

WS TO D25

SCK TO D32

I have connected t
hem in following order with my esp32 DevKit V1

VIN - 3V3

GND - GND

GAIN - GND

DIN - GP22

BCLK - GP26

LRC - GP25

C
HATBOT CODE:  
`import os`  
`import textwrap`  
`import speech_recognition as sr`  
`from langchain.document_loaders im
port TextLoader`  
`from langchain.text_splitter import CharacterTextSplitter`  
`from langchain.embeddings import Huggi
ngFaceEmbeddings`  
`from langchain.vectorstores import FAISS`  
`import pyttsx4`  
`os.environ['HUGGINGFACEHUB_API_TOKE
N'] = '**********************************'`  
`os.environ['TOKENIZERS_PARALLELISM'] = 'false'`  
`loader = TextLoader('/
Users/sanjaykrishna/Documents/CODE_CAP/custom_dataset.txt')`  
`loader.load()`  
`document = loader.load()`  
`def wrap_
text_preserve_newlines(text, width=100):`  
`lines = text.split('\n')`  
`wrapped_lines = [textwrap.fill(line, width=wid
th) for line in lines]`  
`wrapped_text = '\n'.join(wrapped_lines)`  
`return wrapped_text`  
`text_splitter = Character
TextSplitter(chunk_size=1000, chunk_overlap=0)`  
`docs = text_splitter.split_documents(document)`  
`embeddings = Huggi
ngFaceEmbeddings()`  
`db = FAISS.from_documents(docs, embeddings)`  
`engine = pyttsx4.init()`  
`rate = engine.getProp
erty('rate')`  
`new_rate = rate - 10`  
`engine.setProperty('rate', new_rate)`  
`def listen_for_wake_word():`  
`recog
nizer = sr.Recognizer()`  
`with sr.Microphone() as source:`  
`print('Listening for wake word 'hey buddy'...')`  
`reco
gnizer.adjust_for_ambient_noise(source, duration=1)`  
`audio = recognizer.listen(source)`  
`try:`  
`wake_word = recog
nizer.recognize_google(audio)`  
`if 'hey buddy' in wake_word.lower():`  
`print('Wake word 'hey buddy' detected.')`  
`
engine.say('Yes? How may I help you?')`  
`engine.runAndWait()`  
`return True`  
`except sr.UnknownValueError:`  
`pass
`  
`except sr.RequestError as e:`  
`print('Error fetching results: {0}'.format(e))`  
`return False`  
`def handle_que
ry():`  
`print('Speak your query.')`  
`while True:`  
`query = get_query_from_speech()`  
`if query:`  
`while True:` 
 
`if 'goodbye' in query.lower():`  
`print('User said goodbye. Exiting...')`  
`engine.say('Bye! Take care.')`  
`engin
e.runAndWait()`  
`return`  
`doc = db.similarity_search(query)`  
`answer = wrap_text_preserve_newlines(str(doc[0].page
_content))`  
`print('Answer:', answer)`  
`engine.say(answer)`  
`engine.runAndWait()`  
`engine.say('anything else?')`
  
`engine.runAndWait()`  
`break`  
`def get_query_from_speech():`  
`recognizer = sr.Recognizer()`  
`with sr.Micropho
ne() as source:`  
`recognizer.adjust_for_ambient_noise(source, duration=1)`  
`audio = recognizer.listen(source)`  
`tr
y:`  
`query = recognizer.recognize_google(audio)`  
`print('User Query:', query)`  
`return query`  
`except sr.Unknown
ValueError:`  
`print('Could not understand audio')`  
`except sr.RequestError as e:`  
`print('Error fetching results: 
{0}'.format(e))`  
`return ''`  
`def main():`  
`print('Initializing chatbot silently...')`

`# Start interaction loop`
  
`while True:`  
`# Listen for wake word`  
`if listen_for_wake_word():`  
`handle_query()`  
`if __name__ == '__main_
_':`  
`main()`  
It is for a college project and I have been trying this for several weeks now. Still I couldn't comple
te it.  Also this is my first reddit post, I just created an account just to ask this question. Can anyone help me out w
ith this?😓

Thank you.
```
---

     
 
all -  [ Using user feedback to optimize RAG ](https://www.reddit.com/r/LangChain/comments/1bzntdm/using_user_feedback_to_optimize_rag/) , 2024-04-11-0910
```
I'm building several chat based apps with LangChain for clients. I'm asking for feedback with each answer, users can lea
ve a 👍 or 👎.

Often I get the question: 'does this 'self-improve'?'

This got me thinking, why not use the positive feed
back to improve future answers? Has anyone tried something like this:

1. Store (positive) user feedback in a VectorDB w
ith questions-answer pairs.
2. When a new question is asked, run the usual pipeline (RAG for example).
3. Then also quer
y the feedback VectorDB and add the top-k feedback question-answer pairs with high relevance to the question and add it 
as extra context.
4. Let the LLM answer the question using the context and top-k feedback items.

Looking forward to you
r experience, otherwise I might build this, it doesn't seem to hard to make.
```
---

     
 
all -  [ SQL Agent in production? ](https://www.reddit.com/r/LangChain/comments/1bzn1yw/sql_agent_in_production/) , 2024-04-11-0910
```
I’d be interested in whether anyone here is using  LangChain’s SQL Agent (or similar self-built agents with LangChain or
 autogen). I’d love to conenct to learn from your experiences as I have not seen it be used in productive systems yet!
```
---

     
 
all -  [ Seeking Help with Whether to Use ChatGPT's API or LangChain in My Chatbot Web App ](https://www.reddit.com/r/MLQuestions/comments/1bzmv6n/seeking_help_with_whether_to_use_chatgpts_api_or/) , 2024-04-11-0910
```
Hey guys!

I need a little bit of assistance and guidance as to what should I use in my project. I'm trying to create

a
 web app (React - frontend | Flask - backend), designed to include a chatbot that offers personalized video game  recomm
endations. The goal is for the chatbot to suggest games based on user inputs, like preferences for similar games, demogr
aphic details, or specific game features they enjoy.

Given my very limited experience in this sphere of AI and ML,  I'm
 at a crossroads on how best to integrate this chatbot functionality. Should I integrate ChatGPT's API into my code (and
 perhaps further fine-tuning it to better map the project's requirements and idea) or go with LangChain (a framework tha
t I've stumbled upon when searching for ways to implement my ideas into code and have very basic knowledge about it as o
f this moment)?

Do you have any other advices for me to take into consideration and maybe follow in the process of crea
ting this project? Perhaps other APIs or tools that may ease the process of developing the app and save me some time on 
some aspects.

Thanks a ton to everyone taking the time to read and respond! Your help is really appreciated!
```
---

     
 
all -  [ How to create a chatbot to chat with csv files and internet (Bing API)? ](https://www.reddit.com/r/LangChain/comments/1bzmovg/how_to_create_a_chatbot_to_chat_with_csv_files/) , 2024-04-11-0910
```
So I have a requirement of being able to chat with csv files and when the chatbot can't find any relevant information fr
om the csv files it should use the Bing API to search on the web and gather information and answer. I tried to make a cu
stom langchain agent with Bing API as a tool but it's not able to perform the observation, action loop, the model I'm us
ing is Mistral-7B-Instruct-v0.1 which I can't change I think model is not powerful enough for this task. But still does 
anybody have idea how can I make this possible? 
```
---

     
 
all -  [ Multi-Agent Interview using LangGraph  ](https://www.reddit.com/r/LangChain/comments/1bzkzkt/multiagent_interview_using_langgraph/) , 2024-04-11-0910
```
Checkout how you can leverage Multi-Agent Orchestration for developing an auto Interview system where the Interviewer as
ks questions to interviewee, evaluates it and eventually shares whether the candidate should be selected or not. Right n
ow, both interviewer and interviewee are played by AI agents.
https://youtu.be/VrjqR4dIawo?si=1sMYs7lI-c8WZrwP
```
---

     
 
all -  [ LangChain Embeddings ](https://www.reddit.com/r/LangChain/comments/1bzkkdt/langchain_embeddings/) , 2024-04-11-0910
```
Hello,

I’m very new to LangChain and LLM altogether. Very excited!

I started following a LangChain example:
https://py
thon.langchain.com/docs/use_cases/question_answering/chat_history/

I modified it to use a DirectoryLoader. Next, I invo
ked a prompt. The response is narrowed down to a particular chunk when the custom data is split and misses information f
rom other document chunks. For example, the custom data contains information about best practices spread across several 
pages. My prompt is “list 5 of the best practices”. The response would only show one best practice, while ignoring the o
ther document chunks that contain other practices.

Other example of a prompt is “Summary the most important best practi
ce”. The response seems to randomly pick a document chunk and consider that the most important.

How should I go about e
nsure that all chunks of every document is used as part of the response?

Thanks!
```
---

     
 
all -  [ Im worried about privacy and was wondering if there is an LLM I can run locally on my i7 Mac that ha ](https://www.reddit.com/r/LangChain/comments/1bzjzk0/im_worried_about_privacy_and_was_wondering_if/) , 2024-04-11-0910
```
Does an LLM like this exist? Also, will this kill my machine? Im not needing a large model trained on a lot of tokens be
cause I just want it to work with the data I provide it in the context during inference but I the context I have is abou
t 21k. 

Can I use Amazon to host a private LLM instead of running locally? Is that what Bedrock offers? 

Any insights 
are appreciated. Thanks.
```
---

     
 
MachineLearning -  [ [D] How to get the source documents from the retrieved context for RAG?  ](https://www.reddit.com/r/MachineLearning/comments/1bvoc1t/d_how_to_get_the_source_documents_from_the/) , 2024-04-11-0910
```
I'm not using Lanchain but only making API calls to an LLM service provider. The retriever is connected to a vector DB, 
and I would like to know what the LLM refers to WITHIN that retrieved context whenever it provides an answer, similar to
 how return_source_documents works in Langchain.

I'm using AzureOpenAI. I couldn't find much in their docs that related
 to returning the source documents. Any help will be greatly appreciated!

```
---

     
 
MachineLearning -  [ [P] RAG pipeline to query the ML Engineering Open Book ](https://www.reddit.com/r/MachineLearning/comments/1bu4wyx/p_rag_pipeline_to_query_the_ml_engineering_open/) , 2024-04-11-0910
```
I built a quick RAG implementation using Langchain to make it easy to query the [ML Engineering Open Book](https://githu
b.com/stas00/ml-engineering) by [Stas Bekman](https://twitter.com/StasBekman). The Multi-Vector retriever gave pretty go
od results and was quite easy to set up too. 

Github link - [https://github.com/shreyansh26/RAG-ML-Engg-Open-Book](http
s://github.com/shreyansh26/RAG-ML-Engg-Open-Book)

Hope this is useful for folks!
```
---

     
 
MachineLearning -  [ [Project] FinancialAdvisorGPT : LLM+RAG Boilerplate Project ](https://www.reddit.com/r/MachineLearning/comments/1btlpgd/project_financialadvisorgpt_llmrag_boilerplate/) , 2024-04-11-0910
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

     
 
MachineLearning -  [ [Project] Picachain, image search made simple. ](https://www.reddit.com/r/MachineLearning/comments/1bt7epv/project_picachain_image_search_made_simple/) , 2024-04-11-0910
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

     
 
deeplearning -  [ Tengyu Ma on Voyage AI - Weaviate Podcast #91! ](https://www.reddit.com/r/deeplearning/comments/1bjft8i/tengyu_ma_on_voyage_ai_weaviate_podcast_91/) , 2024-04-11-0910
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

     
