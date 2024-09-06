 
all -  [ What is the best way to minimalize html code for llm.  ](https://www.reddit.com/r/LangChain/comments/1fa156y/what_is_the_best_way_to_minimalize_html_code_for/) , 2024-09-06-0912
```
I want to minimalize token count of a html file. I just want to make the llm see the web page with that html or any thin
g with lower token size. 
```
---

     
 
all -  [ Trabalhar com front tendo experiência apenas com back ](https://www.reddit.com/r/brdev/comments/1f9zjvc/trabalhar_com_front_tendo_experiência_apenas_com/) , 2024-09-06-0912
```
Contexto: trabalhava como dev backend jr em uma consultoria pequena da minha cidade, mas troquei de emprego como fullsta
ck jr e agora trabalho remoto pra uma empresa grande de SP que vende ERP pro Brasil todo. Esse trampo eu consegui por in
dicação, e apesar do foco da vaga ser backend com uso de IA (GenAI na AWS com Python e Langchain, mais especificamente) 
também querem que eu toque algumas coisas de Vue.js.

Acontece que eu não sei quase NADA de frontend, fiz uma coisa aqui
 ou ali na faculdade, mas não tenho nenhuma experiência profissional com HTML, CSS e Javascript. A sorte é que meu super
ior disse que não cobraria que eu soubesse essas coisas logo de cara. 

Mas queria saber de vocês se já aconteceram de t
er que tocar front sendo backend, ou vice-versa? Como foi isso? 


```
---

     
 
all -  [ LangChain's ConversationBufferMemory vs OpenAI API's message history ](https://www.reddit.com/r/LangChain/comments/1f9x1g0/langchains_conversationbuffermemory_vs_openai/) , 2024-09-06-0912
```
This is a question particularly relevant to using LangChain with OpenAI APIs. From my understanding, which might be wron
g, LangChain's ConversationBufferMemory injects the entire conversation history into each prompt being passed to the LLM
. While this doesn't lead to much of a problem with the context window, it seems needlessly expensive to call the API wi
th the entire conversation history when it already has a message history that it stores. The API charges for the number 
of tokens for each input.

Wouldn't the ConversationBufferMemory method be inefficient and expensive, or am I missing so
mething here?
```
---

     
 
all -  [ [P] Lessons from Retrieval Augmented Generation ](https://www.reddit.com/r/MachineLearning/comments/1f9tvg7/p_lessons_from_retrieval_augmented_generation/) , 2024-09-06-0912
```
I implemented Rag in my organization and just wrote a blog about what we learned here:   
[https://www.b-yond.com/post/t
ransforming-telco-troubleshooting-our-journey-building-telcogpt-with-rag](https://www.b-yond.com/post/transforming-telco
-troubleshooting-our-journey-building-telcogpt-with-rag)

Hoping it would be helpful for those in this area. Covers rag 
evaluation (ragas), sql db, langchain agents vs chains, weaviate vector db, hybrid search, reranking, and more.

Some ad
ditional insights on ranking and hybrid search here:

[https://www.linkedin.com/posts/drzohaib\_transforming-telco-troub
leshooting-our-journey-activity-7232072089837486081--Le1?utm\_source=share&utm\_medium=member\_android](https://www.link
edin.com/posts/drzohaib_transforming-telco-troubleshooting-our-journey-activity-7232072089837486081--Le1?utm_source=shar
e&utm_medium=member_android)
```
---

     
 
all -  [ How to incorporate Agents into a RAG model ](https://www.reddit.com/r/LangChain/comments/1f9t31s/how_to_incorporate_agents_into_a_rag_model/) , 2024-09-06-0912
```
I'm new to langchain, and I'm currently creating an LLM application to answer questions from custom data (here, data scr
aped from websites). When I prompt a query, the answer sometimes turns out to be, 'I could not find an answer to that fr
om the provided data.' 

I was thinking of employing agents to retrieve extra information from external websites. Basica
lly, is there any way that I can create a hybrid model that combines the strength of both my internal vector database an
d external web search through agents? If so, please guide me on how to do so. I would appreciate it if you share require
d resources as well!
```
---

     
 
all -  [ Best way to add Rewoo (Planner arch) to a chat flow in Langgraph? ](https://www.reddit.com/r/LangChain/comments/1f9rqp8/best_way_to_add_rewoo_planner_arch_to_a_chat_flow/) , 2024-09-06-0912
```
Hey everyone,

I started using a graph based on *supervisor architecture* to build a conversational agent. I had better 
results using a graph based on *Router Agent*, but when dealing with more complex tasks that require multiple steps, thi
ngs haven’t worked as well as I'd hoped. So, I’m thinking about adding the Rewoo-based planner architecture (from the do
cs) into the flow.

The challenge is that in the example, the graph receives a 'Task' as input, but in a conversational 
agent, the user doesn’t always send a clear task—they just keep chatting.

Here are a couple of approaches I’m thinking 
of testing:

1. **Generate a Task from the conversation**: Take the list of messages between the user and the final AI r
esponse, and use that to write a Task that the graph can process.
2. **Feed the message history directly to the Planning
 Agent**: Instead of passing a Task, just pass the message history, and let the agent figure out the planning from that.


**Another option**: Send the message history to the planning node, but then in a parallel execution, pass a Task writt
en based on the messages directly to the solver node.

Any other ideas or suggestions?
```
---

     
 
all -  [ How perplexity handles web scraping ](https://www.reddit.com/r/LangChain/comments/1f9rpq1/how_perplexity_handles_web_scraping/) , 2024-09-06-0912
```
Hi folks,   
We recently have tried to implement some search function for open web results but one thing we found very f
rustrating is scraping time. Does any of you know or can guess how service like Perplexity or  GPT search can have such 
fast response? May I know if the speed is driven by 1) cached parsed website result or 2) underlying architecture(unlike
 current common web loader connector) or 3) simply more dedicated compute resources?   
And if possible, may I know if a
nyone can share how you improve the web searching + parsing speed in your project?  Our current speed with scraping prov
ider is just unacceptably slow... 

Thanks so much for help!
```
---

     
 
all -  [ Want to easily build a Generative AI application as a college project? Try Langrunner! ](https://www.reddit.com/r/utdallas/comments/1f9r70w/want_to_easily_build_a_generative_ai_application/) , 2024-09-06-0912
```
When using LlamaIndex and Langchain to develop Generative AI applications, dealing with compute-intensive tasks (like fi
ne-tuning with GPUs) can be a hassle. Langrunner lets you easily execute code blocks remotely (on AWS, GCP, Azure, or Ku
bernetes) without the hassle of wrapping your entire codebase. Results flow right back into your local environment—no ma
nual containerization needed.

Level up your AI dev experience and check it out here: [https://github.com/dkubeai/langru
nner](https://github.com/dkubeai/langrunner)
```
---

     
 
all -  [ Help! I got the hint of firing in my current job. Seeking for guidance ](https://www.reddit.com/r/LangChain/comments/1f9pxgk/help_i_got_the_hint_of_firing_in_my_current_job/) , 2024-09-06-0912
```
Help! I got the hint of firing in my current job. Seeking for guidance

Currently working in nontechnical work as a proj
ect architect junior. Finished Mtech in Data Science & due to a bad marker I ended up here. I just want to get into AI f
ield. Please share tips please. I don't know-how much time I have in this company.
```
---

     
 
all -  [ Langrunner Simplifies Remote Execution in Generative AI Workflows ](https://www.reddit.com/r/LocalLLaMA/comments/1f9pitr/langrunner_simplifies_remote_execution_in/) , 2024-09-06-0912
```
When using LlamaIndex and Langchain to develop Generative AI applications, dealing with compute-intensive tasks (like fi
ne-tuning with GPUs) can be a hassle. To solve this, we created the **Langrunner** tool which offers an inline API that 
lets you execute specific blocks of code remotely without wrapping the entire codebase. It integrates directly into your
 existing workflow, scheduling tasks on clusters optimized with the necessary resources (AWS, GCP, Azure, or Kubernetes)
 and pulling results back into your local environment.

No more manual containerization or artifact transfers—just strea
mlined development from within your notebook!

Check it out here: [https://github.com/dkubeai/langrunner](https://github
.com/dkubeai/langrunner)
```
---

     
 
all -  [ I Built an App with Lyzr Agent API That Auto-Writes & Posts Tweets! 🧠✨ Check It Out! ](https://www.reddit.com/r/LangChain/comments/1f9oep3/i_built_an_app_with_lyzr_agent_api_that/) , 2024-09-06-0912
```
[Auto Write and Post Tweets](https://reddit.com/link/1f9oep3/video/ii5kymv880nd1/player)

**Hey Reddit!**

I'm thrilled 
to share something I've been working on – an app that uses the Lyzr Agent API to automatically write and post tweets for
 you! Whether you're a social media manager, a content creator, or just someone who struggles with writer's block, this 
app takes care of everything.

**What does it do?**

* Generates AI-powered tweets based on your prompts
* Posts them di
rectly to your Twitter account
* Saves time and helps boost engagement with fresh ideas

If you're tired of coming up wi
th tweets or want to automate your posting, give it a try. Would love to hear your feedback or any features you'd like t
o see added!

#AI #Automation #Twitter #Productivity
```
---

     
 
all -  [ The propositions method for RAG - new way of data ingestion ](https://medium.com/@nirdiamant21/the-propositions-method-enhancing-information-retrieval-for-ai-systems-c5ed6e5a4d2e) , 2024-09-06-0912
```
I've just published a detailed article on Medium about the Propositions Method for AI Information Retrieval. If you're i
nterested in Natural Language Processing, information retrieval, or AI in general, I think you'll find this pretty fasci
nating.

What's the Propositions Method?
In short, it's a technique for breaking down complex information into simple, a
tomic facts. This allows AI systems to understand and retrieve information more accurately and efficiently.
In the artic
le, I cover:

- What exactly the Propositions Method is
- Why it's becoming increasingly important in AI
- How it works 
(with examples)
- The potential benefits and applications
- Some challenges and future directions

We'll soon be adding 
an implementation of the Propositions Method to our extensive collection of RAG (Retrieval-Augmented Generation) tutoria
ls. Our GitHub repository (5.5K ⭐) currently covers 25 different RAG techniques, and this will be a valuable addition. C
heck it out here: https://github.com/NirDiamant/RAG_Techniques
```
---

     
 
all -  [ Episode 0: Open Interpreter Obsidian & Convert Anything ](https://www.reddit.com/r/ToolUse/comments/1f9mr14/episode_0_open_interpreter_obsidian_convert/) , 2024-09-06-0912
```
We pay homage to Open Interpreter, where we met working together, by building a couple of very cool tools that have Open
 Interpreter at the core.

[https://www.youtube.com/watch?v=HjcPRoPfri](https://www.youtube.com/watch?v=HjcPRoPfri)

Ope
n Interpreter Obsidian Plugin - Use Open Interpreter to control your Obsidian vault!

CV - Convert anything to anything 
using the power of Open Interpreter

Friend and Open Glass merge forces

LangChain ambient AI agents UX

Next week, web 
scraping

Code  
[https://github.com/MikeBirdTech/obsidian-open-interpreter](https://github.com/MikeBirdTech/obsidian-op
en-interpreter)  
[https://github.com/tyfiero](https://www.youtube.com/redirect?event=video_description&redir_token=QUFF
LUhqbTl0WHBRUnUxcU1vMUpEZ3VKdUpsRGlvOHJvUXxBQ3Jtc0ttNF9QdGx5VHZxRmlsVjd4TUFjXy0ydS1OWXJNdlMwc3ZRR29yN2g0dUU2Z0NFU0xDNVB0
aHp5VzJMWk95NFVuNHE3U25pVnZRRmxZVUkyc2p5YlJlX0VTQzNiOFEtbG9yLV9xUUFvbzM3T3VDd09wOA&q=https%3A%2F%2Fgithub.com%2Ftyfiero&
v=HjcPRoPfri0)

[https://x.com/tooluseai](https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqb
Hh2azBHbjNhdjh2bHNHaW1YVXdSVVhQai1MZ3xBQ3Jtc0tsM0lKMmdYeXB6NUxKR0dHUlJKUmY3UFFteVBLeDZnUkdyOUpqa3BjWFhXdGFyNER6dl9IWUFEU
GlWNnMyak4yWFBXdEs1dGg3RmowNXF5RVd1dzdtUHpkUkVHQVR1RGdrYnVfTTB6bTc3V1BnTGhuaw&q=https%3A%2F%2Fx.com%2Ftooluseai&v=HjcPRo
Pfri0)  
[https://x.com/MikeBirdTech](https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbDFTT
1Jta3d1NHcwamZBSW9fRjZKMHZoSTM0UXxBQ3Jtc0tsc0E2YmlXR0xYa0FmQVFuMXJSNGg0eEF1QTNTVERiVHR6bW8za3N3UWJRcTE2RlJPS01ta285MjV0W
GZUWUpOazQ2WmpxNVNfMGpxVXN1c21aRnpESHA5ZVJfX1c1UFhDc0RDSzZHRkZmTU5GcC00OA&q=https%3A%2F%2Fx.com%2FMikeBirdTech&v=HjcPRoP
fri0)  
[https://x.com/FieroTy](https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbjdyd0Z2VFZ
TTmZ5NzE5V05WZW8xYUc0dlUyUXxBQ3Jtc0tsM2RWeWZOeEFTQzZsWTIzQkVIVHE0Yl9QNkgwVUxPSDBOYmlHOVZsQlZQV3d2VVZjM2hiZTFfZG0wdzcydFZ
ISDFNcFBTbGFzT0xTLU43ZEItQ2J4RUp6TTRGaURyaGZhTEZJbjlld0xzbnlsZlIxNA&q=https%3A%2F%2Fx.com%2FFieroTy&v=HjcPRoPfri0)

# 
```
---

     
 
all -  [ Trouble chunking mixed text documents  ](https://www.reddit.com/r/LangChain/comments/1f9mdt4/trouble_chunking_mixed_text_documents/) , 2024-09-06-0912
```
I'm working on a project where I need to translate (using llm api) long documents stored as text in a PostgreSQL databas
e. These documents contain a mix of regular text and large tables. My main challenge is to preserve the table structure 
during translation and processing, but I'm running into issues with chunking the text, as it often ruins the format of t
he tables. The tables aren’t in a standard format (markdown latex etc) but are just text which an llm can tell is struct
ured from the spacing. However I’m struggling to automate it via spacing as the rest of the doc has lots of formatting t
oo! And I can’t use an llm to chunk it as it’s too long. 

Unsure of this makes any sense!
```
---

     
 
all -  [ How do I build a Langgraph tool to create query parameters for Github user search ? ](https://www.reddit.com/r/LangChain/comments/1f9lshh/how_do_i_build_a_langgraph_tool_to_create_query/) , 2024-09-06-0912
```
Hello everyone , I'm currently learning Langgraph.   
I want to build a Github agent . This agent will take a query like
 ' I need frontend developer proficient in ReactJS , based in Bangalore and who also knows Python ' and convert it to qu
ery parameter format so that I can call Github user search api with it and get the results.   
  
You can see what I wan
t from my agent by referring to the below conversation. 

Can someone guide me about how can I build this agent ?

[http
s://chatgpt.com/share/2fd44861-3417-4fea-998f-bad18369d6f5](https://chatgpt.com/share/2fd44861-3417-4fea-998f-bad18369d6
f5)  

```
---

     
 
all -  [ I made a RAG library that helps with the boring stuff related to RAG. ](https://www.reddit.com/r/LocalLLaMA/comments/1f9ls7r/i_made_a_rag_library_that_helps_with_the_boring/) , 2024-09-06-0912
```
People who have worked on RAG-like systems know that RAG is primarily a data problem. It largely depends on your vector 
database—how you load your data, preprocess it, and chunk it. This doesn’t mean that other aspects are less important, b
ut it does make them boring, repetitive, and difficult to log. The main reason for this is that RAG involves many hyperp
arameters to choose from, including which models to use, the hyperparameters of the models themselves, and whether to ad
d different techniques such as a reranker or query reformulation.



To address this, [I created a library ](https://git
hub.com/khalilbenkhaled/yaraa)that automates the 'boring' stuff. You can create your own vector database however you lik
e, but when it comes to testing and playing with the pipeline, the library helps you get up and running as quickly as po
ssible. You can either use a YAML file and execute a Python script or use the components of the library as you wish.




For example, with the YAML approach, you edit the YAML file as shown, run a script, and voila—a user interface is at you
r fingertips, allowing you to chat with your system. Alternatively, you can modify the YAML file to specify evaluation m
etrics, and the library will perform the evaluation and return the results to you.



Under the hood, the library does n
ot use any wrapper libraries or LLM orchestration frameworks such as LangChain or LlamaIndex. During installation, you o
nly install the packages you intend to use.



[Here’s the link: YARAA. ](https://github.com/khalilbenkhaled/yaraa) Plea
se make sure to star it if you like what you see. 

Note: It is still in early development, so there aren’t many interfa
ces and evaluation metrics available yet. If you have any suggestions, please leave them in the comments or feel free to
 open an issue. 

If you want to contribute, pull requests are highly appreciated.
```
---

     
 
all -  [ Learnings from RAG ](/r/Rag/comments/1f9j5b1/learnings_from_rag/) , 2024-09-06-0912
```

```
---

     
 
all -  [ Here is the easiest way to use Guardrails in your AI app ](https://www.reddit.com/r/LLMDevs/comments/1f9j81o/here_is_the_easiest_way_to_use_guardrails_in_your/) , 2024-09-06-0912
```
I recently tackled a challenge that I think a lot of us face: building a chatbot that can handle customer support querie
s without compromising user privacy.

Creating a chatbot that can understand and respond to user queries while also prot
ecting Personally Identifiable Information (PII). It's a trickier balance than you might expect!

My Solution: I built a
 chatbot using LangChain with some extra security features. Here's what it can do:

* Detect PII in user input (emails, 
phone numbers, etc.)
* Block processing of sensitive data
* Provide helpful responses without exposing private info

I'v
e created a full tutorial with code examples in this Collab notebook: [https://git.new/langhchainPII](https://git.new/la
nghchainPII)

Here's a snippet of how I set it up:

`portkey_config = {`

`'after_request_hooks': [`

`{`

`'id': 'your-
config-id-here'`

`}`

`]`

`}`

`llm = ChatOpenAI(`

`base_url=PORTKEY_GATEWAY_URL,`

`model='gpt-3.5-turbo',`

`defaul
t_headers=createHeaders(`

`provider='openai',`

`api_key='Your_API_Key',`

`config=portkey_config,`

`)`

`)`

\`\`\`


1. The bot successfully blocks PII from being processed or repeated back
2. It maintains natural conversation flow while
 prioritizing data security
3. Performance impact is minimal - you can have security without sacrificing speed

You can 
run it locally or in Colab to see the PII protection in action. I would love to know your feedback
```
---

     
 
all -  [ How to Build AI agents that protects user's PII data ](https://www.reddit.com/r/AI_Agents/comments/1f9j76e/how_to_build_ai_agents_that_protects_users_pii/) , 2024-09-06-0912
```
I recently tackled a challenge that I think a lot of us face: building a chatbot that can handle customer support querie
s without compromising user privacy.

Creating a chatbot that can understand and respond to user queries while also prot
ecting Personally Identifiable Information (PII). It's a trickier balance than you might expect!

My Solution: I built a
 chatbot using LangChain with some extra security features. Here's what it can do:

* Detect PII in user input (emails, 
phone numbers, etc.)
* Block processing of sensitive data
* Provide helpful responses without exposing private info

I'v
e created a full tutorial with code examples in this Collab notebook: [https://git.new/langhchainPII](https://git.new/la
nghchainPII)

Here's a snippet of how I set it up:

`portkey_config = {`

`'after_request_hooks': [`

`{`

`'id': 'your-
config-id-here'`

`}`

`]`

`}`

`llm = ChatOpenAI(`

`base_url=PORTKEY_GATEWAY_URL,`

`model='gpt-3.5-turbo',`

`defaul
t_headers=createHeaders(`

`provider='openai',`

`api_key='Your_API_Key',`

`config=portkey_config,`

`)`

`)`

\`\`\`


1. The bot successfully blocks PII from being processed or repeated back
2. It maintains natural conversation flow while
 prioritizing data security
3. Performance impact is minimal - you can have security without sacrificing speed

You can 
run it locally or in Colab to see the PII protection in action. I would love to know your feedback
```
---

     
 
all -  [ Here's How I Built a Mistral AI Customer Support Langchain Chatbot That Protects against PII ](https://www.reddit.com/r/MistralAI/comments/1f9j6de/heres_how_i_built_a_mistral_ai_customer_support/) , 2024-09-06-0912
```
I recently tackled a challenge that I think a lot of us face: building a chatbot that can handle customer support querie
s without compromising user privacy.

Creating a chatbot that can understand and respond to user queries while also prot
ecting Personally Identifiable Information (PII). It's a trickier balance than you might expect!

My Solution: I built a
 chatbot using LangChain with some extra security features. Here's what it can do:

* Detect PII in user input (emails, 
phone numbers, etc.)
* Block processing of sensitive data
* Provide helpful responses without exposing private info

I'v
e created a full tutorial with code examples in this Collab notebook: [https://git.new/langhchainPII](https://git.new/la
nghchainPII)

Here's a snippet of how I set it up:

`portkey_config = {`

`'after_request_hooks': [`

`{`

`'id': 'your-
config-id-here'`

`}`

`]`

`}`

`llm = ChatMistralAI(`

`base_url=PORTKEY_GATEWAY_URL,`

`model='gpt-3.5-turbo',`

`def
ault_headers=createHeaders(`

`provider='mistral-ai',`

`api_key='Your_API_Key',`

`config=portkey_config,`

`)`

`)`

\
`\`\`

1. The bot successfully blocks PII from being processed or repeated back
2. It maintains natural conversation flo
w while prioritizing data security
3. Performance impact is minimal - you can have security without sacrificing speed

Y
ou can run it locally or in Colab to see the PII protection in action. I would love to know your feedback
```
---

     
 
all -  [ Learnings from RAG ](https://www.reddit.com/r/Rag/comments/1f9j5b1/learnings_from_rag/) , 2024-09-06-0912
```
I implemented Rag in my organization and just wrote a blog about what we learned here:
https://www.b-yond.com/post/trans
forming-telco-troubleshooting-our-journey-building-telcogpt-with-rag

Hoping it would be helpful for those in this area.
 
Covers rag evaluation (ragas), sql db, langchain agents vs chains, weaviate vector db, hybrid search, reranking, and m
ore. 

Some additional insights on Hybrid search here:

https://www.linkedin.com/posts/drzohaib_transforming-telco-troub
leshooting-our-journey-activity-7232072089837486081--Le1?utm_source=share&utm_medium=member_android
```
---

     
 
all -  [ How I Built a GPT-4 Customer Support Langchain Chatbot That Protects against PII ](https://www.reddit.com/r/OpenAIDev/comments/1f9ixfl/how_i_built_a_gpt4_customer_support_langchain/) , 2024-09-06-0912
```
Creating a chatbot that can understand and respond to user queries while also protecting Personally Identifiable Informa
tion (PII). It's a trickier balance than you might expect!

I built a chatbot using LangChain with some extra security f
eatures. Here's what it can do:

* Detect PII in user input (emails, phone numbers, etc.)
* Block processing of sensitiv
e data
* Provide helpful responses without exposing private info

I've created a full tutorial with code examples in thi
s Collab notebook: [https://git.new/langhchainPII](https://git.new/langhchainPII)

Here's a snippet of how I set it up:


`portkey_config = {`

`'after_request_hooks': [`

`{`

`'id': 'your-config-id-here'`

`}`

`]`

`}`

`llm = ChatOpenAI(
`

`base_url=PORTKEY_GATEWAY_URL,`

`model='gpt-3.5-turbo',`

`default_headers=createHeaders(`

`provider='openai',`

`a
pi_key='Your_API_Key',`

`config=portkey_config,`

`)`

`)`

\`\`\`

1. The bot successfully blocks PII from being proce
ssed or repeated back
2. It maintains natural conversation flow while prioritizing data security
3. Performance impact i
s minimal - you can have security without sacrificing speed

You can run it locally or in Colab to see the PII protectio
n in action. I would love to know your feedback

Upvote1Downvote0comments  

```
---

     
 
all -  [ Langgraph workflow and memory ](https://www.reddit.com/r/LangChain/comments/1f9ib6p/langgraph_workflow_and_memory/) , 2024-09-06-0912
```
Hi there, 

I been trying to build a multi agent system with langgraph and I have a few questions. I got my workflow wor
king with an agent supervisor hierarchy architecture. The only thing I am missing is the workflow memory design. For our
 use case we are using supabase. 

We want to create a ui interface with conversations and chat messages. 

Would you ha
ve a single workflow executing everytime a new message comes in? 

Or would you have a single workflow in a cycle. 

For
 the memory do you store and load the graph state everytime or do you save messages separate from the graph state. 

And
 finally , how do you save the schema in supabase, I don't want to use the postgres client in the docs. Is there an easy
 way to copy paste the schema for the graph state. 

what's the easiest way besides manually creating my own schema?. 
```
---

     
 
all -  [ Any good LLM libraries? ](https://www.reddit.com/r/LocalLLaMA/comments/1f9i1xc/any_good_llm_libraries/) , 2024-09-06-0912
```
I'm just wondering if there are actually any well written python packages for LLM use cases. My requirements are basical
ly:

- no spaghetti code (i.e langchain, llama index)
- no package with 1000s dependency

Please let me know if you know
 some, I mostly write everything on my own for now but if I can automate some of it, would be nice. 

```
---

     
 
all -  [ can i use a langchain Agent in a crew? ](https://www.reddit.com/r/crewai/comments/1f9hyj1/can_i_use_a_langchain_agent_in_a_crew/) , 2024-09-06-0912
```
is there a way to use this agent langchain\_experimental.agents.agent\_toolkits.python.base.create\_python\_agent

in a 
crewAI crew with other crewai Agents?
```
---

     
 
all -  [ ❓What version of LangChain do you use? ](https://www.reddit.com/r/LangChain/comments/1f9hoc0/what_version_of_langchain_do_you_use/) , 2024-09-06-0912
```


[View Poll](https://www.reddit.com/poll/1f9hoc0)
```
---

     
 
all -  [ I Built a Customer Support Chatbot using Claude That Protects against PII - Here's How ](https://www.reddit.com/r/ClaudeAI/comments/1f9h7o8/i_built_a_customer_support_chatbot_using_claude/) , 2024-09-06-0912
```
I recently tackled a challenge that I think a lot of us face: building a chatbot that can handle customer support querie
s without compromising user privacy.

Creating a chatbot that can understand and respond to user queries while also prot
ecting Personally Identifiable Information (PII). It's a trickier balance than you might expect!

My Solution: I built a
 chatbot using LangChain with some extra security features. Here's what it can do:

* Detect PII in user input (emails, 
phone numbers, etc.)
* Block processing of sensitive data
* Provide helpful responses without exposing private info

I'v
e created a full tutorial with code examples in this Collab   
notebook: [https://git.new/langhchainPII](https://git.new
/langhchainPII)

Here's a snippet of how I set it up with Claude. Instead of using ChatOpenAI to  ChatAnthropic

`portke
y_config = {`

`'after_request_hooks': [`

`{`

`'id': 'your-config-id-here'`

`}`

`]`

`}`

`llm = ChatAnthropic(`

`b
ase_url=PORTKEY_GATEWAY_URL,`

`model='claude-3-opus-20240229',`

`default_headers=createHeaders(`

`provider='anthopic'
,`

`api_key='Your_Anthropic_API_Key',`

`config=portkey_config,`

`)`

`)`

\`\`\`

1. The bot successfully blocks PII 
from being processed or repeated back
2. It maintains natural conversation flow while prioritizing data security
3. Perf
ormance impact is minimal - you can have security without sacrificing speed

You can run it locally or in Colab to see t
he PII protection in action. I would love to know your feedback
```
---

     
 
all -  [ Are you a RAG enthusiast or expert? ](https://www.reddit.com/r/LangChain/comments/1f9h23r/are_you_a_rag_enthusiast_or_expert/) , 2024-09-06-0912
```
If you’re into RAG models or just getting started, come join us over at r/RAG! It’s a space for enthusiasts, experts, an
d everyone in between to share tips, ask questions, and talk about the future of RAG tech. Whether you’re building cool 
applications or just curious about how RAG works, we’d love to have you!
```
---

     
 
all -  [ I Built a Customer Support Lagchain Chatbot That Protects against PII - Here's How ](https://www.reddit.com/r/Langchaindev/comments/1f9h17h/i_built_a_customer_support_lagchain_chatbot_that/) , 2024-09-06-0912
```
I recently tackled a challenge that I think a lot of us face: building a chatbot that can handle customer support querie
s without compromising user privacy.

Creating a chatbot that can understand and respond to user queries while also prot
ecting Personally Identifiable Information (PII). It's a trickier balance than you might expect!

My Solution: I built a
 chatbot using LangChain with some extra security features. Here's what it can do:

* Detect PII in user input (emails, 
phone numbers, etc.)
* Block processing of sensitive data
* Provide helpful responses without exposing private info

I'v
e created a full tutorial with code examples in this Collab notebook: [https://git.new/langhchainPII](https://git.new/la
nghchainPII)

Here's a snippet of how I set it up:

`portkey_config = {`

`'after_request_hooks': [ {`

`'id': 'your-con
fig-id-here'`

`} ]`   
`}`

`llm = ChatOpenAI(`

`base_url=PORTKEY_GATEWAY_URL,`

`model='gpt-3.5-turbo',`

`default_he
aders=createHeaders(`

`provider='openai',`

`api_key='Your_API_Key',`

`config=portkey_config,`

`)`

`)`

\`\`\`

1. T
he bot successfully blocks PII from being processed or repeated back
2. It maintains natural conversation flow while pri
oritizing data security
3. Performance impact is minimal - you can have security without sacrificing speed

You can run 
it locally or in Colab to see the PII protection in action. I would love to know your feedback
```
---

     
 
all -  [ I Built a Customer Support Lagchain Chatbot That Protects against PII - Here's How ](https://www.reddit.com/r/LangChain/comments/1f9h0qv/i_built_a_customer_support_lagchain_chatbot_that/) , 2024-09-06-0912
```
I recently tackled a challenge that I think a lot of us face: building a chatbot that can handle customer support querie
s without compromising user privacy. 

Creating a chatbot that can understand and respond to user queries while also pro
tecting Personally Identifiable Information (PII). It's a trickier balance than you might expect!

My Solution: I built 
a chatbot using LangChain with some extra security features. Here's what it can do:

- Detect PII in user input (emails,
 phone numbers, etc.)

- Block processing of sensitive data

- Provide helpful responses without exposing private info


I've created a full tutorial with code examples in this Collab notebook: [https://git.new/langhchainPII](https://git.new
/langhchainPII) 

Here's a snippet of how I set it up:

`portkey_config = {`

`'after_request_hooks': [`

`{`

`'id': 'y
our-config-id-here'`

`}`

`]`

`}`



`llm = ChatOpenAI(`

`base_url=PORTKEY_GATEWAY_URL,`

`model='gpt-3.5-turbo',`

`
default_headers=createHeaders(`

`provider='openai',`

`api_key='Your_API_Key',`

`config=portkey_config,`

`)`

`)`

\`
\`\`  
1. The bot successfully blocks PII from being processed or repeated back

2. It maintains natural conversation fl
ow while prioritizing data security

3. Performance impact is minimal - you can have security without sacrificing speed


You can run it locally or in Colab to see the PII protection in action. I would love to know your feedback


```
---

     
 
all -  [ Agent Executor `astream_events` with `asyncGenerator` tools is possible work? ](https://www.reddit.com/r/LangChain/comments/1f9fvrr/agent_executor_astream_events_with_asyncgenerator/) , 2024-09-06-0912
```
### Description

I attempted to use the langchain agent executor with `astream_events`. When I gave the following instru
ction:

`'Please take a photo, describe it, and tell me if there are any white clouds in the photo?'`

I usually receive
 a response like the following (output in **streaming** mode):

`'There is a big sun in the photo, ... Get Image Success
fully..., I cannot determine the contents of the photo..., there are white clouds and an airplane...'`

I have the follo
wing questions:

1. From the response, it seems that `astream_events` tends to execute each tool (e.g., `get_image_tool`
, `describe_image`) concurrently due to its async nature.
2. Since `describe_image` is an `asyncGenerator`, the agent be
gins summarizing before the photo description is complete, leading to an incorrect understanding, such as 'I cannot dete
rmine the contents of the photo.'

I would like to know if there is a way to restrict `astream_event` to wait for specif
ic tools (`asyncGenerators`) to finish their tasks before proceeding to the next step or summarizing.

### Example Code


```python
async def chat_completion(
    client,
    message: str | List,
    history: List[List[str]],
    client_name
: str = 'OpenAI',
) -> AsyncGenerator:
    '''Use OpenAI/Anthropic API to get `streaming` response.'''
    try:
        
formatted_history = [{'role': 'system', 'content': SYS_PROMPT}]
        for user, assistant in history:
            # hi
story: [[user_query, assistant_response], [user_query, assistant_response], ...]
            formatted_history.append({'
role': 'user', 'content': user })
            formatted_history.append({'role': 'assistant', 'content': assistant})
    
    if isinstance(message, str):
            formatted_history.append({'role': 'user', 'content': message})
        elif
 isinstance(message, list):
            formatted_history.extend(message)

        if client_name == 'OpenAI':
         
   stream = await client.chat.completions.create(
                model='gpt-4o-2024-08-06',
                messages=fo
rmatted_history,
                stream=True,
                temperature=0.,
            )
            async for chunk 
in stream:
                yield chunk.choices[0].delta.content or ''

@tool
async def get_image_tool() -> str:
    '''G
et image'''
    global snapshot
    with Image.open('myimage.png') as image:
        buffered = BytesIO()
        image.
save(buffered, format='PNG')
        snapshot = base64.b64encode(buffered.getvalue()).decode('utf-8')
    return 'Get Im
age Successfully'

@tool
async def describe_image() -> AsyncGenerator:
    '''Describe the image'''
    global snapshot_
session
    message=[
        {
            'role': 'user',
            'content': [
                {'type': 'text', 't
ext': 'describe the image'},
                {'type': 'image_url', 'image_url': {'url': f'data:image/png;base64,{snapsho
t}'}}
            ]
        }
    ]
    response = chat_completion(openai_client, message, [])
    async for chunk in re
sponse:
        yield chunk


tools = [
    get_image_tool,
    describe_image,
]
openai_client = AsyncOpenAI(api_key=OP
ENAI_API_KEY)
langchain_llm_client = ChatOpenAI(
    model='gpt-4o',
    temperature=0.,
    api_key=OPENAI_API_KEY,
   
 streaming=True,
    max_tokens=None,
    verbose=VERBOSE,
    max_retries=5
)
agent = create_tool_calling_agent(langcha
in_llm_client, tools, AGENT_PROMPT)
agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=VERBOS
E,
    return_intermediate_steps=True
)

async main():
    tool_names = [tool.name for tool in tools]

    async for eve
nt in agent_executor.astream_events(
        {
            'input': formatted_history_query,
            'tool_names': t
ool_names,
            'agent_scratchpad': lambda x: format_to_openai_tool_messages(x['intermediate_steps']),
        },

        version='v2'
    ):
        kind = event['event']
        if kind == 'on_chain_start':
            pass
       
 elif kind == 'on_chat_model_stream':
            content = event['data']['chunk'].content
            if content:
     
           yield content
        elif kind == 'on_tool_start':
            pass
        elif kind == 'on_tool_end':
    
        if isinstance(event['data'].get('output'), AsyncGenerator):
                async for event_chunk in event['data
'].get('output'):
                    yield event_chunk
            else:
                yield(
                    f'{
event['data'].get('output')}\n'
                )
        elif kind == 'on_chain_end':
            pass
```

### System 
Info

System Information
------------------
> OS:  Windows
> OS Version:  10.0.22631
> Python Version:  3.11.8 (tags/v3.
11.8:db85d51, Feb  6 2024, 22:03:32) [MSC v.1937 64 bit (AMD64)]

Package Information
-------------------
> langchain_co
re: 0.2.30
> langchain: 0.2.11
> langchain_community: 0.2.10
> langsmith: 0.1.86
> langchain_anthropic: 0.1.20
> langcha
in_openai: 0.1.17
> langchain_text_splitters: 0.2.2
> langgraph: 0.2.3

Optional packages not installed
----------------
---------------
> langserve

Other Dependencies
------------------
> aiohttp: 3.10.5
> anthropic: 0.31.2
> async-timeout
: 4.0.3
> dataclasses-json: 0.6.7
> defusedxml: 0.7.1
> jsonpatch: 1.33
> langgraph-checkpoint: 1.0.2
> numpy: 1.26.4
> 
openai: 1.40.3
> orjson: 3.10.6
> packaging: 24.1
> pydantic: 2.8.2
> PyYAML: 6.0.1
> requests: 2.32.3
> SQLAlchemy: 2.0
.31
> tenacity: 8.5.0
> tiktoken: 0.7.0
> typing-extensions: 4.12.2
```
---

     
 
all -  [ [0 YoE, Student, SWE Intern, United States] student trying to get internships!

 ](https://www.reddit.com/r/resumes/comments/1f9cmxx/0_yoe_student_swe_intern_united_states_student/) , 2024-09-06-0912
```
I send out around 5 applications a day, but so far I have barely received any OAs or interviews back. I know that I have
n't applied to many places, and I'm ramping up the numbers this month (goal is to hit 200 apps by Oct.). I'm a US Citize
n and go to a decent school, so I just want to be able to communicate my experiences as effectively as possible to at le
ast pass ATS scanners. Also I've got a Career Fair coming up soon too so want to make sure my resume is polished before 
then.

https://preview.redd.it/ty3dyao4swmd1.png?width=5100&format=png&auto=webp&s=28b0f959bfe008fe5adaf25867b7b8e70ad09
f5d


```
---

     
 
all -  [ [Student] Applying to SWE internships and haven't had much luck in terms of OAs/Interviews. Feedback ](https://www.reddit.com/r/EngineeringResumes/comments/1f9ci7h/student_applying_to_swe_internships_and_havent/) , 2024-09-06-0912
```
I send out around 5 applications a day, but so far I have barely received any OAs or interviews back. I know that I have
n't applied to many places, and I'm ramping up the numbers this month (goal is to hit 200 apps by Oct.). I'm a US Citize
n and go to a decent school, so I just want to be able to communicate my experiences as effectively as possible to at le
ast pass ATS scanners. Also I've got a Career Fair coming up soon too so want to make sure my resume is polished before 
then.

https://preview.redd.it/19vcgfauqwmd1.png?width=5100&format=png&auto=webp&s=575ee7b7081c2bf3297b14819da00068e1721
02f


```
---

     
 
all -  [ Langrunner: Simplifying Remote Execution in Generative AI Workflows 🚀 ](https://www.reddit.com/r/LlamaIndex/comments/1f9bmwz/langrunner_simplifying_remote_execution_in/) , 2024-09-06-0912
```
When using LlamaIndex and Langchain to develop Generative AI applications, dealing with compute-intensive tasks (like fi
ne-tuning with GPUs) can be a hassle. Say hello to Langrunner! Seamlessly execute code blocks remotely (on AWS, GCP, Azu
re, or Kubernetes) without the hassle of wrapping your entire codebase. Results flow right back into your local environm
ent—no manual containerization needed.

Level up your AI dev experience and check it out here: https://github.com/dkubea
i/langrunner

```
---

     
 
all -  [ can someone explain this? (langchain) ](https://www.reddit.com/r/ChatGPTCoding/comments/1f9bgy8/can_someone_explain_this_langchain/) , 2024-09-06-0912
```
Traceback (most recent call last):

  File 'c:\\python projects\\autoposter\\langchain.py', line 8, in <module>

llm = C
hatGroq(api\_key=GROQ\_API\_KEY,model='mixtral-8x7b-32768')

\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\
^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^

  File 'C:\\python projects\\astra-swarm\\Lib\\site-packages\\l
angchain\_core\\load\\serializable.py', line 113, in \_\_init\_\_

super().\_\_init\_\_(\*args, \*\*kwargs)

  File 'C:\
\python projects\\astra-swarm\\Lib\\site-packages\\pydantic\\v1\\main.py', line 339, in \_\_init\_\_

values, fields\_se
t, validation\_error = validate\_model(\_\_pydantic\_self\_\_.\_\_class\_\_, data)

\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^
\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^

  File 'C:\\python projects\\astra-swarm\\Lib\\site-pack
ages\\pydantic\\v1\\main.py', line 1064, in validate\_model

value = field.get\_default()

\^\^\^\^\^\^\^\^\^\^\^\^\^\^\
^\^\^\^\^

  File 'C:\\python projects\\astra-swarm\\Lib\\site-packages\\pydantic\\v1\\fields.py', line 437, in get\_def
ault

return smart\_deepcopy(self.default) if self.default\_factory is None else self.default\_factory()

\^\^\^\^\^\^\^
\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^

  File 'C:\\python projects\\astra-swarm\\Lib\\site-packages\\langchain\_core\\language\
_models\\base.py', line 95, in \_get\_verbosity

return get\_verbose()

\^\^\^\^\^\^\^\^\^\^\^\^\^

  File 'C:\\python p
rojects\\astra-swarm\\Lib\\site-packages\\langchain\_core\\globals.py', line 59, in get\_verbose

import langchain  # ty
pe: ignore\[import\]

\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^

  File 'c:\\python projects\\autoposter\\langchain.py', line 8, 
in <module>

llm = ChatGroq(api\_key=GROQ\_API\_KEY,model='mixtral-8x7b-32768')

\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\
^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^

  File 'C:\\python projects\\astra-swarm\\L
ib\\site-packages\\langchain\_core\\load\\serializable.py', line 113, in \_\_init\_\_

super().\_\_init\_\_(\*args, \*\*
kwargs)

  File 'C:\\python projects\\astra-swarm\\Lib\\site-packages\\pydantic\\v1\\main.py', line 339, in \_\_init\_\_


values, fields\_set, validation\_error = validate\_model(\_\_pydantic\_self\_\_.\_\_class\_\_, data)

\^\^\^\^\^\^\^\^
\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^

  File 'C:\\python projects\\astra-s
warm\\Lib\\site-packages\\pydantic\\v1\\main.py', line 1064, in validate\_model

value = field.get\_default()

\^\^\^\^\
^\^\^\^\^\^\^\^\^\^\^\^\^\^\^

  File 'C:\\python projects\\astra-swarm\\Lib\\site-packages\\pydantic\\v1\\fields.py', l
ine 437, in get\_default

return smart\_deepcopy(self.default) if self.default\_factory is None else self.default\_facto
ry()

\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^

  File 'C:\\python projects\\astra-swarm\\Lib\\site-packages\\langch
ain\_core\\language\_models\\base.py', line 95, in \_get\_verbosity

return get\_verbose()

\^\^\^\^\^\^\^\^\^\^\^\^\^


  File 'C:\\python projects\\astra-swarm\\Lib\\site-packages\\langchain\_core\\globals.py', line 81, in get\_verbose

ol
d\_verbose = langchain.verbose

\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^

AttributeError: partially initialized module 'langch
ain' has no attribute 'verbose' (most likely due to a circular import)
```
---

     
 
all -  [ Langrunner: Simplifying Remote Execution in Generative AI Workflows ](https://www.reddit.com/r/LangChain/comments/1f97nye/langrunner_simplifying_remote_execution_in/) , 2024-09-06-0912
```
When using Langchain and LlamaIndex to develop Generative AI applications, dealing with compute-intensive tasks (like fi
ne-tuning with GPUs) can be a hassle. To solve this, we created the **Langrunner** tool which offers an inline API that 
lets you execute specific blocks of code remotely without wrapping the entire codebase. It integrates directly into your
 existing workflow, scheduling tasks on clusters optimized with the necessary resources (AWS, GCP, Azure, or Kubernetes)
 and pulling results back into your local environment.

No more manual containerization or artifact transfers—just strea
mlined development from within your notebook!

Check it out here: [https://github.com/dkubeai/langrunner](https://github
.com/dkubeai/langrunner)
```
---

     
 
all -  [ reMind: An Open-Source Digital Memory Assistant
 ](https://www.reddit.com/r/LocalLLaMA/comments/1f94502/remind_an_opensource_digital_memory_assistant/) , 2024-09-06-0912
```
I'd like to get some feedback on **reMind**, a project I've been developing over the past nine months. It's an open-sour
ce digital memory assistant that captures screen content, uses AI for indexing and retrieval, and stores everything loca
lly to ensure privacy. Here's a more detailed breakdown of what the code does:

# Key Components and Functionality

1. *
*Screen Capture (record\_photo.py)**
   * Takes screenshots at regular intervals (default every 2 seconds)
   * Uses str
uctural similarity (SSIM) and histogram comparison to detect significant changes between screenshots
   * Organizes scre
enshots into daily folders
   * Implements a dynamic buffer system to adjust sensitivity based on recent changes
2. **Im
age Processing Pipeline (pipeline\_db.py)**
   * Monitors directories for new screenshot files using a watchdog
   * Pro
cesses new images through an OCR system (using a Swift-based tool)
   * Extracts text content and metadata from images
 
  * Stores processed data in a SQLite database and JSON files for easy retrieval
3. **Data Ingestion (ingestion.py)**
  
 * Loads and processes new data from the SQLite database
   * Groups entries by date and updates JSON files (new\_texts.
json and all\_texts.json)
   * Ensures data consistency between different storage formats
4. **Vector Store Creation (ad
ding\_vectore.py)**
   * Creates and updates a vector store using Chroma for efficient similarity search
   * Utilizes O
llamaEmbeddings to generate text embeddings
   * Splits documents into smaller chunks for more precise retrieval
   * Im
plements a system to track and process only new or updated documents
5. **Query Processing (swift.py)**
   * Sets up a F
lask server to handle user queries
   * Integrates with Langchain for advanced retrieval and question answering
   * Imp
lements time-based filtering of results (e.g., today, yesterday, this week)
   * Uses Ollama with the Llama 3.1 model fo
r generating responses
   * Classifies questions to determine if they require searching the personal knowledge base or c
an be answered with general knowledge
6. **Application Management (remind\_sansprint.py)**
   * Serves as the main entry
 point for the reMind application
   * Sets up necessary directories and initializes the SQLite database
   * Manages th
e execution of various background scripts (screen capture, processing pipeline, etc.)
   * Implements a system tray appl
ication using rumps for easy access and control
7. **User Interface Integration**
   * While not directly part of the Py
thon backend, the project integrates with OpenWebUI for a user-friendly interface
   * Allows users to interact with the
ir personal knowledge base through a chat-like interface

# Key Technologies

* **Ollama**: Used for running the Llama 3
.1 model locally
* **Meta's Llama 3.1**: The core language model used for understanding and generating responses
* **Nom
ic AI**: Used for generating text embeddings
* **Chroma**: Vector database for efficient similarity search
* **Langchain
**: Provides tools for building applications with LLMs
* **Flask**: Lightweight web server for handling API requests
* *
*SQLite**: Local database for storing processed data
* **OpenWebUI**: Provides a user-friendly interface for interacting
 with the system

The goal is to make reMind customizable and fully open-source. All data processing and storage happen 
locally, ensuring user privacy. The system is designed to be extensible, allowing users to potentially add their own mod
ules or customize existing ones.

I'd appreciate any thoughts or suggestions on how to improve the project. If you're in
terested in checking it out or contributing, here's the GitHub link: https://github.com/DonTizi/remind

Thanks in advanc
e for your input!


```
---

     
 
all -  [ What kind of agents would I need to mimic perplexity pro search in my RAG app? ](https://i.redd.it/3q3wwoo5lumd1.jpeg) , 2024-09-06-0912
```
I'm curious on how perplexity's pro search works. What do you guys think does the workflow look like? How to brake down 
a question like that and what agents would I need for something similar?
```
---

     
 
all -  [ How to tell if a page in a document text or numerical data? ](https://www.reddit.com/r/LangChain/comments/1f9196y/how_to_tell_if_a_page_in_a_document_text_or/) , 2024-09-06-0912
```
I'm trying to parse a pdf to add metadata for each chunk to denote if it is mostly text or (mostly numerical) data. I've
 found that if I don't filter the data out, it will produce too many hallucinations. I was planning to simply calculate 
if the ratio of letters to numbers in the document, unless there is a smarter way to go about doing this?

I'm using hug
gingface with a chroma db.
```
---

     
 
all -  [ What are tools in llm? ](https://www.reddit.com/r/ollama/comments/1f8yg2f/what_are_tools_in_llm/) , 2024-09-06-0912
```
I'm new to LLMs and Langchain and have built a RAG application. I've noticed a lot of talk about tools in LLMs, but I'm 
not sure how to create them without defining functions.
Can anyone recommend a tutorial or article that explains this pr
ocess? I'd love to learn more about it.
Thanks!
```
---

     
 
all -  [ Create Your AI Retriever and Win $300 ](https://www.reddit.com/r/LangChain/comments/1f8xutx/create_your_ai_retriever_and_win_300/) , 2024-09-06-0912
```
🚀If you are interested in AI and have a ChatGPT plus account, join our e**xclusive testing event,** experience DenserRet
riever, and earn up to $**300!** We’re seeking AI pioneers to explore and provide feedback on our retriever’s capabiliti
es. Don’t miss out - learn more at [http://retriever.denser.ai/campaign/gpt](http://retriever.denser.ai/campaign/gpt) an
d [https://youtu.be/9f2fUaU1z2w](https://youtu.be/9f2fUaU1z2w). Seize this opportunity today!

💡 W**hy Participate?**

*
 Earn a $50 Amazon gift card for your insights.
* Compete for top rewards: 1st place: $300, 2nd place: $200, 3rd place: 
$100.
* Be among the first to experience cutting-edge RAG technology.
* Build and customize your own GPTs using your dat
a.

**Timeline**

* **Apply**: Submit your application between 9/4 and 9/11.
* **Notification**: Denser will notify qual
ified applicants via email on 9/12.
* **Test**: Approved applicants will receive instructions via email and will have fr
om 9/13 to 9/20 to complete the test and submit the feedback form.
* **Receive Your Gift Card and Rewards**: Denser will
 email you the $50 Amazon gift card on 9/25 and notify the winners of the $300, $200, and $100 prizes to arrange deliver
y.

#AI #RAG #DenserRetriever #TechInnovation #CustomGPTs #GPTs


```
---

     
 
MachineLearning -  [ [P] using GPT4o with langchain/chroma for sports analysis  ](https://www.reddit.com/r/MachineLearning/comments/1enuzlp/p_using_gpt4o_with_langchainchroma_for_sports/) , 2024-09-06-0912
```
Hi all, I'm working on a side project that helps with sports analysis for historical games, which in turn will help with
 sports betting. Currently I've been only focused on MLB because I wanted to see how the use case would pan out.

My fir
st attempt at this was to use the openai endpoint and load all the relevant JSON objects and send a prompt along with th
em to GPT and see what I get back. Eventually, the context size was getting way too big and the problem I was running in
to was that it was expensive. Although, the prompts back were actually pretty decent and relevant to the data.

My secon
d attempt was to setup a RAG using Chroma/LangChain/GPT4o. I got it to work but the answers all seem very off and super 
vague. None of the data I have was shown in any of the prompts i asked, or any of the players that were playing in a gam
e were mentioned at all in the prompt back, plus it kept mentioning wrong games/teams whe asking it specific games. I’m 
assuming I might need to adjust the vector store a bit but not sure how I can do that with chroma.

My question is what 
might be the best way to setup some sort of process? My end result, I would like a response back using the historical da
ta I've provided to make assumptions on what a game could be like based off all the stats given, with some room for GPT 
to also make some inference as well.

I am a super new at this so it's been a learning process so far; please bear with 
me.
```
---

     
 
deeplearning -  [ Month of August in AI ](https://www.reddit.com/r/deeplearning/comments/1f6zfz0/month_of_august_in_ai/) , 2024-09-06-0912
```
🔍 I**nside this Issue:**

* 🤖 La*test Breakthroughs: *This month it’s all about A*gents, LangChain RAG, and LLMs evaluat
ion challenges.*
* 🌐 AI Monthly News: Discover how these stories are revolutionizing industries and impacting everyday l
ife: E*U AI Act, California’s Controversial SB1047 AI regulation act, Drama at OpenAI, and possible funding at OpenAI by
 Nvidia and Apple.*
* 📚 Editor’s Special: This covers the interesting talks, lectures, and articles we came across recen
tly.

Follow me on Twitter and LinkedIn at [**RealAIGuys**](https://twitter.com/RealAIGuys) and [**AIGuysEditor**](https
://www.linkedin.com/in/vishal-rajput-999164122/) to get insight on new AI developments.

>**Please don't forget to subsc
ribe to our Newsletter:** [**https://medium.com/aiguys/newsletter**](https://medium.com/aiguys/newsletter)

# Latest Bre
akthroughs

Are Agents just simple rules? Are Agents just enhanced reasoning? The answer is yes and no. Yes, in the sens
e that agents have simple rules and can sometimes enhance reasoning capabilities compared to a single prompt. But No in 
the sense that agents can have a much more diverse functionality like using specific tools, summarizing, or even followi
ng a particular style. In this blog, we look into how to set up these agents in a hierarchal manner just like running a 
small team of Authors, researchers, and supervisors.

[**How To Build Hierarchical Multi-Agent Systems?**](https://mediu
m.com/aiguys/how-to-build-hierarchical-multi-agent-systems-dc26b19201d2?sk=90958e39e1a28f5030872a90f8e3f3da)

**TextGrad
**. It is a powerful framework performing automatic “differentiation” via text. **It backpropagates textual feedback pro
vided by LLMs to improve individual components of a compound AI system.** In this framework, LLMs provide rich, general,
 natural language suggestions to optimize variables in computation graphs, ranging from code snippets to molecular struc
tures. TextGrad showed effectiveness and generality across various applications, from question-answering and molecule op
timization to radiotherapy treatment planning.

[**TextGrad: Improving Prompting Using AutoGrad**](https://medium.com/ai
guys/textgrad-controlling-llm-behavior-via-text-2a82e2073d10?sk=3633a9aa63b884c97469bce659265921)

The addition of RAG t
o LLMs was an excellent idea. It helped the LLMs to become more specific and individualized. Adding new components to an
y system leads to more interactions and its own sets of problems. Adding RAG to LLMs leads to several problems such as h
ow to retrieve the best content, what type of prompt to write, and many more.

In this blog, we are going to combine the
 **LangChain RAG with DSPy**. We deep dive into how to evaluate the RAG pipeline quantitatively using **RAGAs** and how 
to create a system where instead of manually tweaking prompts, we let the system figure out the best prompt.

[**How To 
Build LangChain RAG With DSPy?**](https://medium.com/aiguys/how-to-build-langchain-rag-with-dspy-ce9154fbafaa?sk=b41d104
05f84c767cf9cd6a58d1ebac0)

As the field of natural language processing (NLP) advances, the evaluation of large language
 models (LLMs) like GPT-4 becomes increasingly important and complex. Traditional metrics such as accuracy are often ina
dequate for assessing these models’ performance because they fail to capture the nuances of human language. In this arti
cle, we will explore why evaluating LLMs is challenging and discuss effective methods like BLEU and ROUGE for a more com
prehensive evaluation.

[**The Challenges of Evaluating Large Language Models**](https://medium.com/aiguys/the-challenge
s-of-evaluating-large-language-models-ec2eb834a349)

# AI Monthly News

# AI Act enters into force

On 1 August 2024, th
e European Artificial Intelligence Act (AI Act) enters into force. The Act aims to foster responsible artificial intelli
gence development and deployment in the EU. The AI Act introduces a uniform framework across all EU countries, based on 
a forward-looking definition of AI and a risk-based approach:

* **Minimal risk:** most AI systems such as spam filters 
and AI-enabled video games face no obligation under the AI Act, but companies can voluntarily adopt additional codes of 
conduct.
* **Specific transparency risk:** systems like chatbots must clearly inform users that they are interacting wit
h a machine, while certain AI-generated content must be labelled as such.
* **High risk:** high-risk AI systems such as 
AI-based medical software or AI systems used for recruitment must comply with strict requirements, including risk-mitiga
tion systems, high-quality of data sets, clear user information, human oversight, etc.
* **Unacceptable risk:** for exam
ple, AI systems that allow “social scoring” by governments or companies are considered a clear threat to people’s fundam
ental rights and are therefore banned.

**EU announcement:** [**Click here**](https://commission.europa.eu/news/ai-act-e
nters-force-2024-08-01_en)

https://preview.redd.it/nwyzfzgm4cmd1.png?width=828&format=png&auto=webp&s=c873db37ca0dadd5b
510bea70ac9f633b96aaea4

# California AI bill SB-1047 sparks fierce debate, Senator likens it to ‘Jets vs. Sharks’ feud


**Key Aspects of SB-1047:**

* Regulation Scope: Targets “frontier” AI models, defined by their immense computational t
raining requirements (over 10²⁶ operations) or significant financial investment (>$100 million).
* Compliance Requiremen
ts: Developers must implement safety protocols, including the ability to immediately shut down, cybersecurity measures, 
and risk assessments, before model deployment.
* Whistleblower Protections: Encourages reporting of non-compliance or ri
sks by offering protection against retaliation.
* Safety Incident Reporting: Mandates reporting AI safety incidents with
in 72 hours to a newly established Frontier Model Division.
* Certification: Developers need to certify compliance, pote
ntially under penalty of perjury in earlier drafts, though amendments might have altered this.

**Pros:**

* Safety Firs
t: Prioritizes the prevention of catastrophic harms by enforcing rigorous safety standards, potentially safeguarding aga
inst AI misuse or malfunction.
* Incentivizes Responsible Development: By setting high standards for AI model training, 
the company encourages developers to think critically about the implications of their creations.
* Public Trust: Enhance
s public confidence in AI by ensuring transparency and accountability in the development process.

**Cons:**

* Innovati
on Stagnation: Critics argue it might stifle innovation, especially in open-source AI, due to the high costs and regulat
ory burdens of compliance.
* Ambiguity: Some definitions and requirements might be too specific or broad, leading to leg
al challenges or unintended consequences.
* Global Competitiveness: There’s concern that such regulations could push AI 
development outside California or the U.S., benefiting other nations without similar restrictions.
* Implementation Chal
lenges: The practicalities of enforcing such regulations, especially the “positive safety determination,” could be compl
ex and contentious.

**News Article:** [**Click here**](https://www.thenation.com/article/society/sb-1047-ai-big-tech-fi
ght/)

**Open Letter:** [**Click here**](https://safesecureai.org/open-letter)

https://preview.redd.it/ib96d7nk4cmd1.pn
g?width=828&format=png&auto=webp&s=0ed5913b5dae72e203c8592393e469d9130ed689

# MORE OpenAI drama

OpenAI co-founder John
 Schulman has left the company to join rival AI startup Anthropic, while OpenAI president and co-founder Greg Brockman i
s taking an extended leave until the end of the year. Schulman, who played a key role in creating the AI-powered chatbot
 platform ChatGPT and led OpenAI’s alignment science efforts, stated his move was driven by a desire to focus more on AI
 alignment and hands-on technical work. Peter Deng, a product manager who joined OpenAI last year, has also left the com
pany. With these departures, only three of OpenAI’s original 11 founders remain: CEO Sam Altman, Brockman, and Wojciech 
Zaremba, lead of language and code generation.

**News Article:** [**Click here**](https://techcrunch.com/2024/08/05/ope
nai-co-founder-leaves-for-anthropic/)

https://preview.redd.it/0vdjc18j4cmd1.png?width=828&format=png&auto=webp&s=e9de60
4c26aed3e47b50df3bdf114ef61f967080

# Apple and Nvidia may invest in OpenAI

Apple, which is planning to integrate ChatG
PT into iOS, is in talks to invest. Soon after, [*Bloomberg* also](https://www.bloomberg.com/news/articles/2024-08-29/nv
idia-has-held-discussions-about-joining-openai-s-funding-round?srnd=homepage-americas) reported that Apple is in talks b
ut added that Nvidia “has discussed” joining the funding round as well. The round is reportedly being led by Thrive Capi
tal and would value OpenAI at more than $100 billion.

**News Article:** [**Click here**](https://www.theverge.com/2024/
8/29/24231626/apple-nvidia-openai-invest-microsoft)

https://preview.redd.it/ude6jguh4cmd1.png?width=828&format=png&auto
=webp&s=3603cbca0dbb1be3e6d0efcf06c3a698428bbdd6

# Editor’s Special

* The AI Bubble: Will It Burst, and What Comes Aft
er?: [**Click here**](https://www.youtube.com/watch?v=91SK90SahHc&t=317s)
* Eric Schmidt Full Controversial Interview on
 AI Revolution (Former Google CEO): [**Click here**](https://www.youtube.com/watch?v=mKVFNg3DEng)
* AI isn’t gonna keep 
improving [**Click here**](https://www.youtube.com/watch?v=Y8Ym7hMR100)
* General Intelligence: Define it, measure it, b
uild it: [**Click here**](https://www.youtube.com/watch?v=nL9jEy99Nh0)
```
---

     
 
deeplearning -  [ Creating a project on NLP ](https://www.reddit.com/r/deeplearning/comments/1ey2e85/creating_a_project_on_nlp/) , 2024-09-06-0912
```
So me and my friend completed the ML and DL specialization by AndrewNg, and were just gonna get started on a project. We
 decided to make a academic assistant. So basically what this does is a user can upload a PDF,text file or any other sup
ported media and the can ask questions related to it's contents. The main objective being making learning quick given la
rger documents.

The pipeline we decided is pretty standard for such a project.

1. Split the text into chunks
2. Genera
te embeddings of the chunks
3. Store the chunks in a vector DB
4. Find the top K similar chunks to the query 
5. Retriev
e context and feed it into a LLM for an answer.

So I looked up for a library and framework to use and decided on langch
ain. We haven't decided on an LLM yet but want to run it locally so no OpenAI please. 

Since this is gonna be out first
 AI project confidence is low. I would really appreciate any heads up on the issues we may face, any suggestions on libr
aries,frameworks or models will be really helpful as well. 

Appreciate any resourceful comment 😊
```
---

     
 
deeplearning -  [ How To Build Your Retrieval Augmented Generation (RAG) Using Open-source Tools: LangChain, LLAMA 3,  ](https://www.reddit.com/r/deeplearning/comments/1emdotx/how_to_build_your_retrieval_augmented_generation/) , 2024-09-06-0912
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

     
 
deeplearning -  [ Need help with creating CLI for 'non-programmers' (LLMs) ](https://www.reddit.com/r/deeplearning/comments/1elrfgm/need_help_with_creating_cli_for_nonprogrammers/) , 2024-09-06-0912
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

     
