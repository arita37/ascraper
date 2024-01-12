 
all -  [ Langchain User Group Meeting on Thursday Jan 18 2024 ](https://www.reddit.com/r/LangChain/comments/194g33t/langchain_user_group_meeting_on_thursday_jan_18/) , 2024-01-12-0910
```
Hello!

I've been organizing a langchain user group meeting every other Thursday at 7pm eastern US time.

We get people 
just interested in langchain, people using langchain at work, people using langchain as a hobby. We like to discuss the 
langchain blog posts, interesting projects using langchain, and as a general networking event among people tuned into th
e AI boom. It's a great opportunity to share the latest developments, what works, what doesn't work, and so on.

[https:
//www.meetup.com/langchain-user-group/events/298217248/](https://www.meetup.com/langchain-user-group/events/298217248/)
```
---

     
 
all -  [ Error? ](https://i.redd.it/jtcc3cph4vbc1.jpeg) , 2024-01-12-0910
```

```
---

     
 
all -  [ Which is best vector similarity search and vector db for code chunks? ](https://www.reddit.com/r/LangChain/comments/1948p85/which_is_best_vector_similarity_search_and_vector/) , 2024-01-12-0910
```
Suppose taking files .cs (C#) from repo,  splitting into chunks and storing in vector db. 
Using embedding model sentenc
e transformer model***. 
Kindly suggest me best vector db storage and best similarity search for same which can can give
 best context to pass to llm.
Thanks in advance 🙂
```
---

     
 
all -  [ Simplifying Langchain: A Practical Guide to Supercharging with GPT-4 ](https://www.reddit.com/r/LangChain/comments/1947pl5/simplifying_langchain_a_practical_guide_to/) , 2024-01-12-0910
```
Hey Langchain enthusiasts!

I’ve noticed a lot of chatter about the steep learning curve of Langchain. So, I thought I’d
 share my approach that makes it not only manageable but also pretty awesome to use.

🚀 The Game-Changer: I tweaked the 
Langchain chatbot (open-source, yay!) by swapping out the GPT-3.5 model with the shiny new GPT-4, boasting a massive 128
K context window. This upgrade means we can feed it a hefty amount of chain reference code. The result? Writing substant
ial code segments that require minimal tweaking!

🛠️ Here’s How You Can Do It Too:

	1.	Set the Stage: Clone the chat-la
ngchain repo and set it up as per the guidelines. A piece of cake!
	2.	The Magic Swap: In chain.py, replace “GPT-3.5-tur
bo” with “gpt-4-1106-preview”. Boost the number of retrieved chunks (I’m rocking search_kwargs=dict(k=20)).
	3.	Prompt P
erfection: Modify the prompt (example below) and ensure your initial description is crystal clear. Dropping in known cla
ss names helps the bot understand your needs better. 

Happy coding!



Here’s the prompt I’m using:

RESPONSE_TEMPLATE 
= '''\
You are an expert programmer and problem-solver, tasked with answering any question \
about Langchain and generat
ing complete working scripts using the Langchain framework. Your responses \
shall have two parts: Answer and Code.

***
For the Answer:***
Generate a comprehensive and informative answer of 80 words or less for the \
given question based so
lely on the provided search results (URL and content). You must \
only use information from the provided search results.
 Use an unbiased and \
journalistic tone. Combine search results together into a coherent answer. Do not \
repeat text. 
Cite search results using [${{number}}] notation. Only cite the most \
relevant results that answer the question accurat
ely. Place these citations at the end \
of the sentence or paragraph that reference them - do not put them all at the en
d. If \
different results refer to different entities within the same name, write separate \
answers for each entity.

Y
ou should use bullet points in your answer for readability. Put citations where they apply \
rather than putting them al
l at the end.

If there is nothing in the context relevant to the question at hand, just say 'Hmm, \
I'm not sure.' Don'
t try to make up an answer.

***For the Code:***
Produce complete, functional Python code that utilizes the Langchain fr
amework to address the question or task \
presented. Ensure that the code is:
1. Readable: Write clear, understandable c
ode. Use descriptive variable names and adhere to Python's PEP 8 style \
guidelines for maximum readability.
2. Efficien
t: Optimize for performance. Use efficient algorithms and data structures to ensure the code runs \
effectively and cons
ervatively uses resources.
3. Error-Handled: Incorporate error handling to manage and anticipate potential issues that m
ight arise during \
execution. Use try-except blocks where appropriate and validate input data.
4. Tested: Include neces
sary assertions or print statements to demonstrate the functionality and correctness \
of the code. Ensure that the code
 produces expected results when executed.
5. Complete: Ensure the code can be copied directly into a Python project with
 no modifications needed. \
It should be self-contained, specifying all necessary imports and dependencies.
6. Langchain
-Specific: Utilize the appropriate classes, functions, and methods from the Langchain \
framework. Clearly demonstrate h
ow Langchain's features and capabilities are applied to solve the \
given problem or task.
7. Context-Aware: Use the pro
vided context effectively. Reference and utilize data, variables, or \
insights derived from the 'context' section to in
form the code's logic and functionality. \
8. Comment-Free Execution: Avoid using comment blocks as placeholders for cod
e. Ensure all functional \
parts of the code are executable statements and not comments.

If the question or task does n
ot provide enough information for a complete script, or if it is outside the scope of \
the Langchain framework, clearly
 state that a complete working script cannot be provided as requested, explain \
the reasons and provide suggestions and
/or alternatives. 

Anything between the following `context` html blocks is retrieved from a knowledge \
bank, and is pr
ovided in addition to the conversation with the user. 
<context>
    {context} 
<context/>

Anything between the followi
ng `Code_Block` html blocks were provided by user as integral and shall be \
treated as essential to your response. Each
 block of code is enclosed within a pair of markdowns triple backticks (```)
<Code_Block>
    {Code_Block} 
<Code_Block/
>

***REMEMBER:***
-If there is no relevant information within the context, just say 'Hmm, I'm \
not sure.' Don't try to
 make up an answer. Anything between the preceding 'context' \
html blocks is retrieved from a knowledge bank, not part 
of the conversation with the \
user. 
-The goal is to provide code that is ready to be integrated and used in a project,
 \
demonstrating the practical application and power of the Langchain framework in solving real-world problems.\
Anythin
g between the preceding 'Code_Block' html blocks were provided by user as integral and shall be \
treated as essential t
o your response. 
'''
```
---

     
 
all -  [ ID-based RAG with Supabase Vector Store ](https://www.reddit.com/r/Supabase/comments/19470zd/idbased_rag_with_supabase_vector_store/) , 2024-01-12-0910
```
I am using langchain for document processing and then I generate OpenAI Embeddings and save them to Supabase Vector Stor
e which looks like this

https://preview.redd.it/yn8fs68ohubc1.png?width=2096&format=png&auto=webp&s=d05afa2aa1ffca6472f
d62353a21ab78c5a8f9e7

Each row shows a chunk from a specific document. I want these documents to be isolated from each 
other and the knowledge base should not mix since one document should not have knowledge about other documents. So for t
hat purpose I want to add a user\_id and a document\_id against every row so that LLM can only generate response from th
e documents with a specified id. 

https://preview.redd.it/qvonjitshubc1.png?width=1440&format=png&auto=webp&s=8d49edf66
4a5f7ed6df4eb9064915484457e0ab0

I have searched a lot but the most popular solution I found is to use metadata and put 
all your ids in there which can be seen below. I think that is not a good solution for a sql based database. Did anyone 
find a proper sql solution for this problem?
```
---

     
 
all -  [ ID-based RAG for Supabase Vector Store ](https://www.reddit.com/r/node/comments/1946ynk/idbased_rag_for_supabase_vector_store/) , 2024-01-12-0910
```
I am using langchain for document processing and then I generate OpenAI Embeddings and save them to Supabase Vector Stor
e which looks like this

https://preview.redd.it/2x1ofw4tgubc1.png?width=2174&format=png&auto=webp&s=14db64f9ffe9ca8ec22
a83cfe194e2cb8b973ca8

Each row shows a chunk from a specific document. I want these documents to be isolated from each 
other and the knowledge base should not mix since one document should not have knowledge about other documents. So for t
hat purpose I want to add a user\_id and a document\_id against every row so that LLM can only generate response from th
e documents with a specified id. 

I have searched a lot but the most popular solution I found is to use metadata and pu
t all your ids in there which can be seen below. I think that is not a good solution for a sql based database. Did anyon
e find a proper sql solution for this problem?

https://preview.redd.it/i2yjdkr5hubc1.png?width=1198&format=png&auto=web
p&s=71cd6d4dfb78d7667ee8b746f6c678c907543c91
```
---

     
 
all -  [ Run TheBloke LLMs on Laptop with 32GB RAM and 128MB VRAM ](https://www.reddit.com/r/LangChain/comments/194434d/run_thebloke_llms_on_laptop_with_32gb_ram_and/) , 2024-01-12-0910
```
Hey,

 I have a general question: I want to run LLMs locally on Laptops with 128Mb VRAM and 32GB RAM. Is this possible a
s my VRAM is so low?  

 So which GGUF-Version would be possible to use here:

\- [https://huggingface.co/TheBloke/Mixtr
al-8x7B-v0.1-GGUF](https://huggingface.co/TheBloke/Mixtral-8x7B-v0.1-GGUF) or here: 

\- [https://huggingface.co/TheBlok
e/em\_german\_mistral\_v01-GGUF](https://huggingface.co/TheBloke/em_german_mistral_v01-GGUF) ?  

At the moment I am dep
loying on my Mac without any problems, but it has 64GB RAM.

Thanks in advance!
```
---

     
 
all -  [ Chat LangChain is awesome! ](https://www.reddit.com/r/LangChain/comments/1943u42/chat_langchain_is_awesome/) , 2024-01-12-0910
```
I really like langchain. its not perfect, not always easy but for free open source software, I really appreciate it.

Ch
at LangChain is really cool. I am not a software developer. I am a data dude who has to code to get stuff done. Chat Lan
gchain is super helpful to do that. 

Thanks.
```
---

     
 
all -  [ Can I get an invite code? ](https://www.reddit.com/r/LangChain/comments/193z6uz/can_i_get_an_invite_code/) , 2024-01-12-0910
```
Carrying out a research in RAG Models in my university. Recently found LangChain, took a few courses and I am amazed. Ac
cess to LangChain would boost my research value and give out better results. Always fun to try out new and upcoming fram
eworks and tools.
```
---

     
 
all -  [ Need resources to learn Langchain ](https://www.reddit.com/r/developersIndia/comments/193z1di/need_resources_to_learn_langchain/) , 2024-01-12-0910
```
I have browsed a lot and cannot draw a conclusion as to what would be the best source to learn Langchain from due to lac
k of general consensus about it online. So people who are actively working with Langchain or have worked with it in the 
past, what are the best resources out there for the same? I don’t mind if it’s paid as long as it would be worth it.
```
---

     
 
all -  [ How to retrieve the context from a chain set using LCEL? ](https://www.reddit.com/r/LangChain/comments/193y7ca/how_to_retrieve_the_context_from_a_chain_set/) , 2024-01-12-0910
```
I have a rag chain using LCEL. I want to extract just the context that has been set in the chain. Below is my function: 
 


def get\_rag\_chain(retriever, format\_docs, prompt, llm): | format\_docs

rag\_chain = (

{'context': retriever | f
ormat\_docs, 'question': RunnablePassthrough()}

| prompt

| llm

| StrOutputParser()

)

return rag\_chain  


&#x200B;

```
---

     
 
all -  [ [RAG] [llama-index] How to execute multiple SQL queries with SQLTableRetrieverQueryEngine in NL2SQL  ](https://www.reddit.com/r/LangChain/comments/193upr6/rag_llamaindex_how_to_execute_multiple_sql/) , 2024-01-12-0910
```
I am working on a project where user will ask natural language queries and this llama-index based engine will convert th
at natural language to sql query and execute it on my database and give answer in natural language to the user. Problem 
is it is only able to execute one query per question so comparison quetions are not possible to answer and also if a que
stion does not require querying the database it will still query the database. How can I solve this. Please help me with
 your suggesting.   
Thanks in advance. 
```
---

     
 
all -  [ is it possible to improve the sql agent ](https://www.reddit.com/r/LangChain/comments/193rnaz/is_it_possible_to_improve_the_sql_agent/) , 2024-01-12-0910
```
Is there a way to improve the sqldatabasechain agent that performs database queries through finetuning of the gpt 3 mode
l? What I'm saying is that sometimes the SQL agent makes a mistake in what it has to query in the database according to 
the request it makes. Is it possible to improve it by finetuning the gpt 3.5 model taking into account that there is at 
most a total of 60 data for adjustment?
```
---

     
 
all -  [ Keeping up with the fast movement in AI space ](https://www.reddit.com/r/LangChain/comments/193ozls/keeping_up_with_the_fast_movement_in_ai_space/) , 2024-01-12-0910
```
Hi! With everything around LLMs moving at such a fast pace, papers, related frameworks, libraries, toolkits, open source
 models and more popping up every day, I found it much harder to stay on top of everything than before. How do you stay 
updated and effectively navigate this space. Any recommendations for blogs, communities, channels or strategies? Thanks 
in advance! 😊
```
---

     
 
all -  [ Holy f*** I have never seen such spaghetti code in my life ](https://www.reddit.com/r/LangChain/comments/193oz8b/holy_f_i_have_never_seen_such_spaghetti_code_in/) , 2024-01-12-0910
```
No wonder there barely exists tutorials or articles exploring complex workflows. To make anything other than a simple RA
G app you need to have a PHD in langchain. Better get studying 😭
```
---

     
 
all -  [ OpenAPI agent with Azure OpenAI LLM ](https://www.reddit.com/r/LangChain/comments/193lbjq/openapi_agent_with_azure_openai_llm/) , 2024-01-12-0910
```
Does anyone have examples of how to build an agent to perform API actions based on user input in natural language format
? I have the spec file and want to use OpenAPI agent.I came across examples but all were using open ai LLM.I want to use
 Azure endpoint
```
---

     
 
all -  [ How to decrease latency in RAG chatbots? ](https://www.reddit.com/r/LangChain/comments/193iq2l/how_to_decrease_latency_in_rag_chatbots/) , 2024-01-12-0910
```
Can someone help with template to build RAG Chatbot with low latency..
```
---

     
 
all -  [ [For Hire] Programmer/Web Developer/IT Consultant (Python, PHP, AI, etc.) ](https://www.reddit.com/r/forhire/comments/193gw5c/for_hire_programmerweb_developerit_consultant/) , 2024-01-12-0910
```
To get in contact, please message me, I don't use the chat thing and might miss you or reply very late. Then we can swit
ch to email/discord/telegram or whatever else. Apologies for starting with this, but many missed it when it was lower.


I'm a programmer/web developer with 13 years of professional experience. I am available for all sorts of programming and
 web development tasks.

I also offer consulting services. If you need something done, but don't know how exactly, I can
 help. I'm an excellent researcher and I communicate well. I will work with you to find the best solution for your probl
em.

My services include, but are not limited to:

* websites

* desktop applications

* AI integration (chatGPT API, la
ngchain, whatever else turns up)

* integration with APIs and other webservices

* all kinds of scripts

* task automati
on

* website optimization

* debugging

* plugins for existing software

* bots (Reddit, Telegram, etc)

* code audits


If you're looking for someone to take care of a variety of different tasks, I can offer continuous support.

My preferr
ed environment is Python with Django, but I work with anything Python or PHP based. I have no problem with learning new 
technologies that are needed for the project.

Rate is $50/h. Can also do fixed price by project, but only if the projec
t/milestone is well-defined.

Satisfied customers:

https://www.reddit.com/r/testimonials/comments/2e8gqy/pos_uqui_need_
a_backend_web_dev_look_no_further/

https://www.reddit.com/r/testimonials/comments/7fsdze/pos_hiring_uqui_was_an_example
_of_how_it_should/

https://www.reddit.com/r/testimonials/comments/80pu9l/pos_uqui_great_work_detailed_and_fast/

https:
//www.reddit.com/r/testimonials/comments/b0nx68/uqui_is_a_hardworking_intelligent_honest_apps/

https://www.reddit.com/r
/testimonials/comments/j3mz3p/uqui_is_a_great_web_development_consultant_with/

https://www.reddit.com/r/testimonials/co
mments/v40ay3/pos_uqui_is_a_great_backend_dev_to_work_with/

Please note: I am not a designer. To make it clear, it mean
s zero aesthetic sense.
```
---

     
 
all -  [ What other AI apps are being built. ](https://www.reddit.com/r/LangChain/comments/193fppt/what_other_ai_apps_are_being_built/) , 2024-01-12-0910
```
I am seeing everywhere saying we are building AI apps but in reality i see only RAG. Or am i missing something here. Is 
there any apps are being built other than knowledge retrieval?
```
---

     
 
all -  [ new short generative AI course in JavaScript ](https://www.reddit.com/r/Deno/comments/193fbwp/new_short_generative_ai_course_in_javascript/) , 2024-01-12-0910
```
wanna learn generative AI but in **JavaScript**? 🤯

check out this new course from DeepLearningAI and Andrew Ng on build
ing with LLMs and LangChain, which uses deno's jupyter notebooks 

[https://www.deeplearning.ai/short-courses/build-llm-
apps-with-langchain-js/](https://www.deeplearning.ai/short-courses/build-llm-apps-with-langchain-js/)
```
---

     
 
all -  [ Not implemented error ](https://i.redd.it/j389hono2nbc1.jpeg) , 2024-01-12-0910
```
I was trying to extract data from .html urls but getting this error , any fixes for this ?
```
---

     
 
all -  [ Not implemented error ](https://i.redd.it/5xyg4y2vflbc1.jpeg) , 2024-01-12-0910
```
Anyone knows any fix for this ?
```
---

     
 
all -  [ ZeroShotAgent gives me Observation: Invalid Format: Missing 'Action:' after 'Thought: error ](https://www.reddit.com/r/LangChain/comments/1934iac/zeroshotagent_gives_me_observation_invalid_format/) , 2024-01-12-0910
```
Hello  
I am using ZeroShotAgent passing it specific prefix and suffix as well as :

FORMAT\_INSTRUCTIONS\_TEMPLATE = ''
'Use the following format:  
Question: the input question you must answer  
Thought: you should always think about what 
to do  
Action: the action to take, should be one of: {tool\_names}  
Action Input: the input to the action  
Observatio
n: the result of the action  
... (this Thought/Action/Action Input/Observation can repeat N times)  
Thought: I now kno
w the final answer  
Final Answer: the final answer to the original input question  
Please respect the order of the ste
ps Thought/Action/Action Input/Observation  
'''

I am getting this error 

[ZeroShot agent error](https://preview.redd.
it/zv4fn1hi1lbc1.png?width=698&format=png&auto=webp&s=06cefe90e856be26319280946eb168ed88c4c472)

What solutions can you 
suggest and what other agents can I use?  
One of the tasks I'm working on is a csv agent, also I want a general solutio
n because later I will be using open source models so no openai functions :/ 

Thanks in advance
```
---

     
 
all -  [ Become an AI Developer (Free 9 Part Series) ](https://www.reddit.com/r/devresource/comments/1934fc3/become_an_ai_developer_free_9_part_series/) , 2024-01-12-0910
```
Just sharing a free series I stumbled across on Linkedin - DataCamp's 9-part AI code-along series.

This specific sessio
n linked below is 'Building Chatbots with OpenAI API and Pinecone' but there are 8 others to have a look at and code alo
ng to.

*Start from basics to build on skills with GPT, Pinecone and LangChain to create a chatbot that answers question
s about research papers. Make use of retrieval augmented generation, and learn how to combine this with conversational m
emory to hold a conversation with the chatbot. Code Along on DataCamp Workspace:* [*https://www.datacamp.com/code-along/
building-chatbots-openai-api-pinecone*](https://www.datacamp.com/code-along/building-chatbots-openai-api-pinecone)

Find
 all of the sessions at: [https://www.datacamp.com/ai-code-alongs](https://www.datacamp.com/ai-code-alongs)
```
---

     
 
all -  [ Become an AI Developer (Free 9 Part Series) ](https://www.reddit.com/r/FreeCodeCamp/comments/1934e4m/become_an_ai_developer_free_9_part_series/) , 2024-01-12-0910
```
Just sharing a free series I stumbled across on Linkedin - DataCamp's 9-part AI code-along series.

This specific sessio
n linked below is 'Building Chatbots with OpenAI API and Pinecone' but there are 8 others to have a look at and code alo
ng to. 

*Start from basics to build on skills with GPT, Pinecone and LangChain to create a chatbot that answers questio
ns about research papers. Make use of retrieval augmented generation, and learn how to combine this with conversational 
memory to hold a conversation with the chatbot.  Code Along on DataCamp Workspace:* [*https://www.datacamp.com/code-alon
g/building-chatbots-openai-api-pinecone*](https://www.datacamp.com/code-along/building-chatbots-openai-api-pinecone)  



Find all of the sessions at: https://www.datacamp.com/ai-code-alongs  
```
---

     
 
all -  [ Am I tripping or is SuperBase super slow? ](https://www.reddit.com/r/LangChain/comments/192y7se/am_i_tripping_or_is_superbase_super_slow/) , 2024-01-12-0910
```
The most likely option is that I got something wrong. 

I used Faiis store to do a vector search over 30000 documents, w
hich worked relatively well. I tried to do the same with Langchain and Superbase and the queries take 4x the amount of t
ime to run. Has anyone run into this?
```
---

     
 
all -  [ Getting error FAISS call; [TypeError: object of type 'NoneType' has no len()] ](https://www.reddit.com/r/LangChain/comments/192vu2i/getting_error_faiss_call_typeerror_object_of_type/) , 2024-01-12-0910
```
   vectorstore\_faiss = FAISS.from\_documents(

\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^

  File '/opt/homebrew/lib/py
thon3.11/site-packages/langchain\_core/vectorstores.py', line 510, in from\_documents

return cls.from\_texts(texts, emb
edding, metadatas=metadatas, \*\*kwargs)

\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^
\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^

  File '/opt/homebrew/lib/python3.11/site-packages/langchain\_communit
y/vectorstores/faiss.py', line 915, in from\_texts

return cls.\_\_from(

\^\^\^\^\^\^\^\^\^\^\^

  File '/opt/homebrew/
lib/python3.11/site-packages/langchain\_community/vectorstores/faiss.py', line 874, in \_\_from

index = faiss.IndexFlat
L2(len(embeddings\[0\]))

\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^

&#x200B;
```
---

     
 
all -  [ Applied to 100+ SWE internships with very few interviews ](https://www.reddit.com/r/resumes/comments/192u489/applied_to_100_swe_internships_with_very_few/) , 2024-01-12-0910
```
Hey everyone - 

I've applied to 100 + SWE internships (career switcher, international student) with practically no OAs.


What's wrong with my CV, and what can I do to improve it?

&#x200B;

https://preview.redd.it/6k80xpv68ibc1.jpg?width=2
545&format=pjpg&auto=webp&s=5bdc3886faa07300f783d7f8fd7512e73b9a4c95
```
---

     
 
all -  [ Next.js starter for building AI apps (image and text gen, vector search) ](https://www.reddit.com/r/nextjs/comments/192ssyg/nextjs_starter_for_building_ai_apps_image_and/) , 2024-01-12-0910
```
Hey Next.js community,

I created a starter template to help developers build full-stack apps with AI features: image ge
neration, text generation, vector search and more.

It's built on Next.js + Tailwind for the front-end. Supports Supabas
e for database and authentication, and Stripe for payments. Also comes with built-in components for a landing page and d
ashboard.

For the AI integrations, I use Replicate for image gen, gpt-3.5 for text gen, Supapase pgvector as the vector
 store, and LangChain for LLM management.

I've put up the template along with tons of documentation and videos here: [h
ttps://templateai.co/](https://templateai.co/)

Hope you all find it useful. Cheers.

&#x200B;
```
---

     
 
all -  [ What LLM orchestration am I thinking about? ](https://www.reddit.com/r/ArtificialInteligence/comments/192p9cq/what_llm_orchestration_am_i_thinking_about/) , 2024-01-12-0910
```
Hi everyone,  
A few months ago I was playing around with a bunch of different tools to manage integrations and LLMs. I 
randomly found a website, where within the UI I was able to:  
\- Provide a prompt for a complex task (e.g. build app th
at does XYZ)  
\- It broke it down into subtasks (e.g. choose data schemas, create frontend...etc)  
\- It then started 
working on each subtasks and finding new ones as it completed each one  
I was blown away but then needing to do my rese
arch took me somewhere else. I now have time to invest more time in this venture but can't find it for the life of me. I
 think it was based on LangChain or AutoGPT but I've been searching for hours and can't find it so trying my luck here :
)  
Anyone know what this is or uses it?
```
---

     
 
all -  [ What LLM orchestration tool am I thinking about? ](https://www.reddit.com/r/LangChain/comments/192p8lz/what_llm_orchestration_tool_am_i_thinking_about/) , 2024-01-12-0910
```
Hi everyone,  


A few months ago I was playing around with a bunch of different tools to manage integrations and LLMs. 
I randomly found a website, where within the UI I was able to:

\- Provide a prompt for a complex task (e.g. build app t
hat does XYZ)

\- It broke it down into subtasks (e.g. choose data schemas, create frontend...etc)

\- It then started w
orking on each subtasks and finding new ones as it completed each one

&#x200B;

I was blown away but then needing to do
 my research took me somewhere else. I now have time to invest more time in this venture but can't find it for the life 
of me. I think it was based on LangChain or AutoGPT but I've been searching for hours and can't find it so trying my luc
k here :)

Anyone know what this is or uses it?
```
---

     
 
all -  [ I have been unable to get an interview with any of the top companies like MAANG and others. ](https://www.reddit.com/r/resumes/comments/192p0p7/i_have_been_unable_to_get_an_interview_with_any/) , 2024-01-12-0910
```
I am looking out Data Scientist roles involving NLP and LLMS. I really need feedback on what I might be missing on my re
sume.

https://preview.redd.it/tfrtl27d8hbc1.png?width=820&format=png&auto=webp&s=c3ac18ecb31fb091811a86549dcf0dee110c34
1e
```
---

     
 
all -  [ Is LangChain needed/ideal for a chatbot? ](https://www.reddit.com/r/LangChain/comments/192oom1/is_langchain_neededideal_for_a_chatbot/) , 2024-01-12-0910
```
I'm working on creating a chatbot for some long research papers of mine (using RAG). While I'd like the ability to answe
r both summary questions, e.g. 'What's paper x all about?', I also want the chatbot to answer specific questions. This n
eed speaks to the usefulness of Agents (I think), but since I don't need to chain together a bunch of tasks, I'm wonderi
ng if LangChain is overkill?
```
---

     
 
all -  [ How to make openai tools agent store tool messages ](https://www.reddit.com/r/LangChain/comments/192kifr/how_to_make_openai_tools_agent_store_tool_messages/) , 2024-01-12-0910
```
I have the following code, memory does not store the intermediate steps in the tools calling, how can this be achieved? 
 


    def answer_langchain_v2(input, chat_token):
        memory = ConversationBufferMemory(
                memory_ke
y='chat_history', return_messages=True)
        azure_open_ai = AzureChatOpenAI(
            temperature=0,
            
max_tokens=3000,
            verbose=True,
        )
        tools = [retrieve_benchmarks, search_entities()]
        pr
ompt = hub.pull('hwchase17/openai-tools-agent')
        agent = create_openai_tools_agent(
            azure_open_ai, to
ols, prompt)
        agent_executor = AgentExecutor(
            agent=agent,
            tools=tools,
            verbo
se=True,
            handle_parsing_errors=True,
            memory=memory
        )
        output = agent_executor.inv
oke(
            {
                'input': input_schema.format(input=input),
            }
        )['output']

&#x200B
;
```
---

     
 
all -  [ Visualizing Software Complexity with a 3D Force-Directed Graph ](https://www.reddit.com/r/Python/comments/192ket2/visualizing_software_complexity_with_a_3d/) , 2024-01-12-0910
```
Hello everyone!

I want to share a project for which Python support was just added recently:

[https://github.com/gabote
chs/dep-tree](https://github.com/gabotechs/dep-tree)

This is a tool that allows users to visualize the complexity of a 
code base using a 3D force-directed graph:

* It will take a Python executable/library's entrypoint and calculate it's d
ependencies based on the import statements.
* It will recursively crawl the import statements looking for more import st
atements in the imported files, building recursively a file dependency graph.
* It will render the graph using a force-d
irected layout, and all the crawled files will be placed in a three-dimensional space simulating some attraction/repulsi
on forces based on the dependencies between them.
* There's already some samples using well known open-source projects t
hat are quite surprising:
   * [langchain](https://dep-tree-explorer.vercel.app/api?repo=https%3A%2F%2Fgithub.com%2Flang
chain-ai%2Flangchain&entrypoint=libs%2Flangchain%2Flangchain%2F__init__.py)
   * [tensorflow](https://dep-tree-explorer.
vercel.app/api?repo=https%3A%2F%2Fgithub.com%2Ftensorflow%2Ftensorflow&entrypoint=tensorflow%2Fpython%2Fkeras%2Fmodels.p
y)
   * [numpy](https://dep-tree-explorer.vercel.app/api?repo=https%3A%2F%2Fgithub.com%2Fnumpy%2Fnumpy&entrypoint=numpy%
2F__init__.py)
   * [pytorch](https://dep-tree-explorer.vercel.app/api?repo=https%3A%2F%2Fgithub.com%2Fpytorch%2Fpytorch
&entrypoint=torch%2Fnn%2F__init__.py)

I wrote a blog post about it if you want to dive deeper: [link](https://dev.to/ga
botechs/about-software-complexity-569d)

Hope you liked it!
```
---

     
 
all -  [ Best practices for uploading PDFs when type varies a lot (scanned documents, exports, tables, ...) ](https://www.reddit.com/r/LangChain/comments/192epg3/best_practices_for_uploading_pdfs_when_type/) , 2024-01-12-0910
```
We're building a web app, that allows the user to upload PDFs, which we then summarise. 

A challenge we have is that pe
ople upload very different formats of PDFs. (Word exports, flattened images, scanned documents, ...). 

In my head I was
 thinking of detecting if it has lots of big images (when it's a scan), then using a vision model over those images, and
 then summarising the outputs. If there are no images, then just extracting texts (potentially handing tables slightly d
ifferently). 

What are the best practices on ensuring all the information is extracted? In my head I was thinking of de
tecting if it has lots of big images (when it's a scan), then using a vision model over those images, and then summarisi
ng the outputs. If there are no images, then just extract texts (potentially handing tables slightly differently). 
```
---

     
 
all -  [ [Q] Is it possible to give ollama access to a local gitlab repository? ](https://www.reddit.com/r/LocalLLaMA/comments/192dz3r/q_is_it_possible_to_give_ollama_access_to_a_local/) , 2024-01-12-0910
```
I'm playing arround with https://github.com/ollama-webui/ollama-webui and I'm quite pleased with the ease of use and per
formance. I've tested it with starcoder and mistral , putting in some archives for RAG and the results are not bad, but 
was wondering if there is a way to give ollama a way to access a project inside a gitlab instance with a restricted user
 and it's password so it can access the project and answer some simple questions like 'What version of .net is this proj
ect using?'

Can this be done or is just a pipe dream? I have read some work was done some months ago with langchain for
 searching full codebases , but I was aiming at something more limited for the moment.

As a more general question , cou
ld a local model access websites I point it at ? like 'Give me a list of the new items in the local newspaper website ht
tps://www.localnews.com' for the last 2 hours ?
```
---

     
 
all -  [ I just started learning. ](https://www.reddit.com/r/LangChain/comments/192avem/i_just_started_learning/) , 2024-01-12-0910
```
What is the difference between LangChain and LangSmith? What do you think is the best way to learn this framework?
```
---

     
 
all -  [ [D] Are Custom LLM RAG apps going to become redundant? ](https://www.reddit.com/r/MachineLearning/comments/1929n4f/d_are_custom_llm_rag_apps_going_to_become/) , 2024-01-12-0910
```
Loks like Copilot Studio is being rolled out (https://www.microsoft.com/en-us/microsoft-copilot/microsoft-copilot-studio
) with an impressive looking no code/out of the box RAG solution.

There is a phenomenal amount of development and activ
ity in the Open Source RAG world (e.g Langchain, Llamaindex, etc), which I am a great supporter of FYI.

However, what s
eems strange is that this no code out of the box solution (Copilot Studio - just as an example of one) seems overwhelmin
gly to be the better option if you wanted to build a RAG app i.e If you compare the cost to build and productionise a cu
stom RAG app vs the cost of using Copilot Studio, it's almost an order of magnitude lower (no matter how you cut it with
 the developer time and duration). 

My question is, it seems to me we are moving towards a situation where enterprise s
olutions will make custom RAG apps redundant (not in all cases of course, but most cases), however there seems to be ver
y little discussion of this relative to the activity in the open source community. Do people agree this is a likely scen
ario? 

Obviously there will be exceptions…but on most use cases I don’t see how you can compete with an instant/minimal
 setup, low cost, highly scalable RAG solution.
```
---

     
 
all -  [ Are there any GUI tools out there that allows you to use LLMs in this manner ](https://www.reddit.com/r/ChatGPT/comments/1922abj/are_there_any_gui_tools_out_there_that_allows_you/) , 2024-01-12-0910
```
Sorry if this is common knowledge, I’m new to using LLMs and all my experience until now has been with Chat GPT using Op
en AI’s web ui. I want to explore other language models especially some of the opensource ones like Mixtral 8B etc 

Is 
there a GUI tool I can use to keep all these models in one place? And manage things like context? For example I will hav
e seperate system
prompts for “Programmer”, “Lawyer”, “Advise giver” etc and depending on what the mood calls for I can 
select the most appropriate one? And also I can load context from memory to pick up a conversation from where I last lef
t off?

I believe Langchain can do this but it looks like it’s not really a UI but a lib you need to install and write s
cripts for. I’m ok with that cause I’m a developer by trade but I was hoping to start off with something more turn-key, 
like select this or that model from a drop-down and have all your saved context appear on the left etc in the form of a 
web or desktop app. 

Is there such a tool out there people can recommend? Thanks in advance!
```
---

     
 
MachineLearning -  [ [P] An open-source project for deploying local models ](https://www.reddit.com/r/MachineLearning/comments/18zkm5m/p_an_opensource_project_for_deploying_local_models/) , 2024-01-12-0910
```
 Introducing a new LLM WebUI project that supports various local model loading and provides streaming output for cutting
-edge online multimodal models GPT-4-Vision and Gemini-Pro-Vision. Completely free and open source, it serves as a valua
ble research tool for exploring diverse models. The project is actively under development with continuous updates:  
[ht
tps://github.com/smalltong02/keras-llm-robot](https://github.com/smalltong02/keras-llm-robot)

&#x200B;

[WebUI](https:/
/preview.redd.it/f95jievpepac1.png?width=2560&format=png&auto=webp&s=1f2908b484ededc78591719ef87efdac2f9497ba)

&#x200B;


[Configuration](https://preview.redd.it/owaj5s1repac1.png?width=2560&format=png&auto=webp&s=f837b1ef67cb8e4ccaee4ec602
a61859f53db100)

&#x200B;

[Tools & Agent](https://preview.redd.it/jrot8w9sepac1.png?width=2560&format=png&auto=webp&s=7
1e224f08620941146cd437a99bcb55d02930a9e)
```
---

     
 
MachineLearning -  [ [Project] Temporal Augmented Retrieval (TAR) - Dynamic RAG ](https://www.reddit.com/r/MachineLearning/comments/18uddmj/project_temporal_augmented_retrieval_tar_dynamic/) , 2024-01-12-0910
```
From a corpus of text, how can you detect emerging topics and their evolution through time?

Introducing Temporal Augmen
ted Retrieval (TAR). (built in the context of buildspace n&w s4)

TAR is an open-source advanced RAG approach that aims 
to factor in the dynamic and temporal aspects of textual data when performing retrieval.

It allows us to understand the
 evolution of discussed topics over time.

The idea behind this project is to open the debate regarding the current limi
tations of RAG methods

This first approach has been built without using RAG frameworks (like Jerry Liu’s langchain) and
 focuses on financial tweets 

Relevant links:

Medium: [https://medium.com/@adam-rida/temporal-augmented-retrieval-tar-
dynamic-rag-ad737506dfcc](https://medium.com/@adam-rida/temporal-augmented-retrieval-tar-dynamic-rag-ad737506dfcc)

Gith
ub:[https://github.com/adrida/Temporal\_RAG](https://github.com/adrida/Temporal_RAG)

Hugging Face Benchmark: [https://h
uggingface.co/spaces/Adr740/Temporal-RAG-Benchmark](https://huggingface.co/spaces/Adr740/Temporal-RAG-Benchmark)

My web
site: [adrida.github.io](https://adrida.github.io)

&#x200B;

https://preview.redd.it/lj7wkhk70f9c1.png?width=960&format
=png&auto=webp&s=fc79c5034351a1711e1ec051919a5c4d2edbc333
```
---

     
 
MachineLearning -  [ [R][P] Autogen + Langchain Tools + Local LLM doesn't work. ](https://www.reddit.com/r/MachineLearning/comments/18tex1j/rp_autogen_langchain_tools_local_llm_doesnt_work/) , 2024-01-12-0910
```
Hey folks, 

So I'm playing around with the agent framework Autogen and I'm trying to create agents by providing it cust
om tools to use. These custom tools are defined in the langchain framework. Furthermore, I am using open source LLM mode
ls like Mistral, LLAMA, Mixtral etc.

In my experience, I have been unable to get the Autogen+LocalLLM framework to iden
tify the right tools to use given the prompt. However it does a fantastic job with the GPT model. 

Please note that my 
goal is for the agent to mandatorily use the tools provided and not come up with its own code. And the agent should figu
re out the right tool to use. 

I have been very explicit with my prompting, despite which I am unable to get this to wo
rk.

Any thoughts and suggestions? Please let me know ! Please share your experiences as well. Cheers !
```
---

     
 
MachineLearning -  [ [P] Seeking Advice for Building a School Handbook Chatbot Using OpenAI and Vector Databases ](https://www.reddit.com/r/MachineLearning/comments/18rndcp/p_seeking_advice_for_building_a_school_handbook/) , 2024-01-12-0910
```
Hello everyone,

I'm embarking on a project to create a chatbot for my school's handbook, aiming to make it a resource f
or students to easily access information. As someone relatively new to AI, I'm seeking guidance on implementing this.

M
y current plan is to use OpenAI as the primary language learning model, focusing on affordability. I am considering inte
grating RAG (Retrieval-Augmented Generation) and LangChain for enhanced functionality. However, I'm quite perplexed abou
t choosing an appropriate vector database, as many options appear costly. The goal is to keep this system live and acces
sible for student usage without breaking the bank.

I'm also looking into open-source embedding models to pair with the 
vector database. Pinecone has caught my attention, but its pricing seems steep for our budget.

Does anyone have recomme
ndations or tips on affordable yet effective tools and strategies for this project? Any insights on vector databases sui
table for educational use, or ways to optimize cost without compromising quality, would be greatly appreciated.

Thank y
ou in advance for your help!

(I typed out my problem and had gpt4 fix up the format and wording dont bash me)
```
---

     
 
deeplearning -  [ [D] Unleashing the Power of Langchain with Wandb: Revolutionizing Topic Modeling and Evaluation ](https://www.reddit.com/r/deeplearning/comments/191mm83/d_unleashing_the_power_of_langchain_with_wandb/) , 2024-01-12-0910
```
Complementing Langchain’s prowess, Wandb emerges as a powerhouse meticulously designed for developers leveraging LLM tec
hnology. As an evaluation framework and production monitoring platform, Wandb stands out for its tailored approach. Its 
arsenal comprises real-time monitoring, granular analytics, and streamlined evaluation processes, laying the groundwork 
for elevated performance and reliability in AI applications.

&#x200B;

Link: [https://medium.com/ai-advances/unleashing
-the-power-of-langchain-with-wandb-revolutionizing-topic-modeling-and-evaluation-75af5cf51b15](https://medium.com/ai-adv
ances/unleashing-the-power-of-langchain-with-wandb-revolutionizing-topic-modeling-and-evaluation-75af5cf51b15) 
```
---

     
 
deeplearning -  [ Unlocking the Power of Language: How LangChain Transforms Data Analysis and More ](https://www.reddit.com/r/deeplearning/comments/18l788y/unlocking_the_power_of_language_how_langchain/) , 2024-01-12-0910
```
Language models have revolutionized natural language processing (NLP), yet they grapple with limitations that impede the
ir full potential. Enter LangChain, a pioneering framework that transcends these constraints, fostering innovative langu
age-based applications. To comprehend LangChain’s significance, we must first grasp the limitations plaguing large langu
age models (LLMs).

link: [https://medium.com/ai-advances/unlocking-the-power-of-language-how-langchain-transforms-data-
analysis-and-more-3c4f327d520d](https://medium.com/ai-advances/unlocking-the-power-of-language-how-langchain-transforms-
data-analysis-and-more-3c4f327d520d) 
```
---

     
 
deeplearning -  [ [D] Mastering Chain Composition with LangChain Expression Language (LCEL) ](https://www.reddit.com/r/deeplearning/comments/18i0wot/d_mastering_chain_composition_with_langchain/) , 2024-01-12-0910
```
In the intricate landscape of modern software development, orchestrating complex sequences of actions seamlessly poses a
 significant challenge. Enter LangChain Expression Language (LCEL), a groundbreaking declarative approach designed to re
volutionize the composition of chains within software architecture.

Link: [https://medium.com/ai-artistry/mastering-cha
in-composition-with-langchain-expression-language-lcel-2d5041fb0cbd](https://medium.com/ai-artistry/mastering-chain-comp
osition-with-langchain-expression-language-lcel-2d5041fb0cbd)  
```
---

     
