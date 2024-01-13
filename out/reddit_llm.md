 
all -  [ Show and Tell: What have you built with LLMs? ](https://www.reddit.com/r/LangChain/comments/1958znq/show_and_tell_what_have_you_built_with_llms/) , 2024-01-13-0910
```
Hello LLM enthusiasts! I'm eager to hear about the creative and innovative ways you've been using Large Language Models 
(LLMs) in your projects. Lang Chain, has been a game-changer in bringing these applications from the drawing board to re
al-world use. Have you developed something unique, solved a complex problem, or simply experimented with something fun? 
Let's inspire each other by sharing our experiences and discussing how Lang Chain has facilitated our journey with LLMs!

```
---

     
 
all -  [ Trying to solve for bad data ](https://www.reddit.com/r/LangChain/comments/1957t7r/trying_to_solve_for_bad_data/) , 2024-01-13-0910
```
Hi. I'm tasked with building a chatbot for work. We are an HR tech company. 

I'm using Retrieval QA, trying different c
hunking sizes, testing both Pinecone and Supabase for vector Retrieval. 

However, I'm of the opinion that our data suck
s. Our API docs have like 50 words per page at most, and there are maybe 30 pages. We have a lot of support tickets, lik
e 500, but only 20% have actual answers written out to the ticket reason. So I get maybe 20-50 words per useable ticket.
 Lastly, our community sourced internal documentation is fragmentation and inconsistently designed. 

I've engineered al
l the text into consistent structures. The purpose is Q/A, like 'If a user is complaining X isn't working in their dashb
oard, what might be the cause?'

But is there anything realistic I can do with this situation when the data is so low vo
lume and poor quality? Any technical approaches that don't require a manual documentation overhaul, that is. 

Thanks.
```
---

     
 
all -  [ Langchain with Hugging face models ](https://www.reddit.com/r/LangChain/comments/1954q8y/langchain_with_hugging_face_models/) , 2024-01-13-0910
```
I am new to langchain. Can someone please explain to me how to use hugging face models like Microsoft phi-2 with langcha
in? The official documentation talks about openAI and other inference API based LLMs but how about locally running model
s?
```
---

     
 
all -  [ Intro to LangChain - Full Documentation Overview ](https://youtu.be/dXP841pBcJw?si=V03bfGxR0E2DVOA8) , 2024-01-13-0910
```
Comprehensive LangChain Overview
```
---

     
 
all -  [ Chroma retriever/CSV Agent giving poor results, any advice on this? ](https://www.reddit.com/r/LangChain/comments/194xwhi/chroma_retrievercsv_agent_giving_poor_results_any/) , 2024-01-13-0910
```
 I’m working on a solution for a client who needs an agent to pull data from a CSV file, which contains information abou
t a provider’s location, services, categories, phone numbers, and addresses. Initial trials with chroma embeddings and a
 gpt-3.5-turbo LLM had inconsistent outcomes. However, switching to gpt-4-1106-preview and adjusting the chroma retrieve
r kwargs “k” from 4 to 8 enhanced document retrieval but also increased token usage. The CSV Agent was less effective, y
ielding poorer results than the embeddings.  For context, my agent is an assistant that provides contact information for
 providers based on user queries. For example: 

* User: 'asado barrio san vicente'
* AI: 'Aquí tienes información sobre
 asado en el barrio San Vicente:
* Asadero Parrillero  - Teléfonos: 123456789, 123456788
* ASADO LA CASA DEL COSTILLAR, 
Javier Rodriguez  - Teléfonos: 123456789  - Dirección: Example 123

Espero que esta información te sea útil. '    


Wha
t should i try?    
The adjunted image is a sample of my CSV/Excel file. Any advice is would be aprecciated.  
 
```
---

     
 
all -  [ Aplicatii cu llmuri ](https://www.reddit.com/r/programare/comments/194xoa1/aplicatii_cu_llmuri/) , 2024-01-13-0910
```
cu ce aplicatii misto va laudati, facute cu de-alde langchain, langgraph, llamaindex, autogen? chiar as citi niste pytho
n
```
---

     
 
all -  [ Easy Guide to Creating Smart Chatbots with Langchain & GPT-4 ](https://dev.to/zanepearton/easy-guide-to-creating-smart-chatbots-with-langchain-gpt-4-i5c) , 2024-01-13-0910
```

```
---

     
 
all -  [ Contribute to open-source AI gateway, written in TS ](https://www.reddit.com/r/LangChain/comments/194ut4u/contribute_to_opensource_ai_gateway_written_in_ts/) , 2024-01-13-0910
```
[https://github.com/portkey-ai/gateway](https://github.com/portkey-ai/gateway)

We've been developing this open-source A
I gateway that routes to hundred+ LLMs using the OpenAI SDK.

It is a one-line executable that starts a local proxy serv
er - you can just put that url in the baseURL of the OpenAI SDK and call providers like Google, Azure, AWS, Anthropic, A
nyscale, Together, Perplexity, Mistral, and more.

It's designed to be highly performant — we have been using it to rout
e billions of tokens daily for our customers.

Would love to hear the community's views/feedback 🙏
```
---

     
 
all -  [ Let's dicsuss this sub's negative feelings towards LangChain ](https://www.reddit.com/r/LangChain/comments/194u376/lets_dicsuss_this_subs_negative_feelings_towards/) , 2024-01-13-0910
```
I am surprised to see many posts like [this one](https://www.reddit.com/r/LangChain/comments/193oz8b/holy_f_i_have_never
_seen_such_spaghetti_code_in/), or [this one](https://www.reddit.com/r/LangChain/comments/18eukhc/i_just_had_the_displea
sure_of_implementing/), expressing negative sentiments about LangChain and in particular the agreement about the negativ
ity in the comment section. For a community that comes together for the LangChain package and ecosystem, there seems to 
be a surprising amount of people that don't like it. The advice given is often to not use LangChain at all.

Personally,
 I have been impressed by the developer's willingness to listen to the community, and would expect this to lead to a pos
itive mindset in the community. For example the introduction of LCEL is an attempt to improve the code quality and reduc
e the complexity of applications build with LangChain. However, [the community does not seem to see its value](https://w
ww.reddit.com/r/LangChain/comments/18t3jn9/do_we_really_need_lcel/).

While I understand some of the criticism, I don't 
believe the amount of negativity is justified. Moreover, it seems there is little willingness for constructive feedback 
that could be used to improve the situation. This post is a plea to improve this mindset for the betterment of the LangC
hain ecosystem and the community that uses it. With LangChain having just released version 0.1, I think this is a good m
oment in time for this community to reflect on what it expects from LangChain going forward. Let me know what you think.

```
---

     
 
all -  [ Langchain User Group Meeting on Thursday Jan 18 2024 ](https://www.reddit.com/r/LangChain/comments/194g33t/langchain_user_group_meeting_on_thursday_jan_18/) , 2024-01-13-0910
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

     
 
all -  [ Which is best vector similarity search and vector db for code chunks? ](https://www.reddit.com/r/LangChain/comments/1948p85/which_is_best_vector_similarity_search_and_vector/) , 2024-01-13-0910
```
Suppose taking files .cs (C#) from repo,  splitting into chunks and storing in vector db. 
Using embedding model sentenc
e transformer model***. 
Kindly suggest me best vector db storage and best similarity search for same which can can give
 best context to pass to llm.
Thanks in advance 🙂
```
---

     
 
all -  [ Simplifying Langchain: A Practical Guide to Supercharging with GPT-4 ](https://www.reddit.com/r/LangChain/comments/1947pl5/simplifying_langchain_a_practical_guide_to/) , 2024-01-13-0910
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

     
 
all -  [ ID-based RAG with Supabase Vector Store ](https://www.reddit.com/r/Supabase/comments/19470zd/idbased_rag_with_supabase_vector_store/) , 2024-01-13-0910
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

     
 
all -  [ ID-based RAG for Supabase Vector Store ](https://www.reddit.com/r/node/comments/1946ynk/idbased_rag_for_supabase_vector_store/) , 2024-01-13-0910
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

     
 
all -  [ Run TheBloke LLMs on Laptop with 32GB RAM and 128MB VRAM ](https://www.reddit.com/r/LangChain/comments/194434d/run_thebloke_llms_on_laptop_with_32gb_ram_and/) , 2024-01-13-0910
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

     
 
all -  [ Chat LangChain is awesome! ](https://www.reddit.com/r/LangChain/comments/1943u42/chat_langchain_is_awesome/) , 2024-01-13-0910
```
I really like langchain. its not perfect, not always easy but for free open source software, I really appreciate it.

Ch
at LangChain is really cool. I am not a software developer. I am a data dude who has to code to get stuff done. Chat Lan
gchain is super helpful to do that. 

Thanks.
```
---

     
 
all -  [ Can I get an invite code? ](https://www.reddit.com/r/LangChain/comments/193z6uz/can_i_get_an_invite_code/) , 2024-01-13-0910
```
Carrying out a research in RAG Models in my university. Recently found LangChain, took a few courses and I am amazed. Ac
cess to LangChain would boost my research value and give out better results. Always fun to try out new and upcoming fram
eworks and tools.
```
---

     
 
all -  [ Need resources to learn Langchain ](https://www.reddit.com/r/developersIndia/comments/193z1di/need_resources_to_learn_langchain/) , 2024-01-13-0910
```
I have browsed a lot and cannot draw a conclusion as to what would be the best source to learn Langchain from due to lac
k of general consensus about it online. So people who are actively working with Langchain or have worked with it in the 
past, what are the best resources out there for the same? I don’t mind if it’s paid as long as it would be worth it.
```
---

     
 
all -  [ How to retrieve the context from a chain set using LCEL? ](https://www.reddit.com/r/LangChain/comments/193y7ca/how_to_retrieve_the_context_from_a_chain_set/) , 2024-01-13-0910
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

     
 
all -  [ [RAG] [llama-index] How to execute multiple SQL queries with SQLTableRetrieverQueryEngine in NL2SQL  ](https://www.reddit.com/r/LangChain/comments/193upr6/rag_llamaindex_how_to_execute_multiple_sql/) , 2024-01-13-0910
```
I am working on a project where user will ask natural language queries and this llama-index based engine will convert th
at natural language to sql query and execute it on my database and give answer in natural language to the user. Problem 
is it is only able to execute one query per question so comparison quetions are not possible to answer and also if a que
stion does not require querying the database it will still query the database. How can I solve this. Please help me with
 your suggesting.   
Thanks in advance. 
```
---

     
 
all -  [ is it possible to improve the sql agent ](https://www.reddit.com/r/LangChain/comments/193rnaz/is_it_possible_to_improve_the_sql_agent/) , 2024-01-13-0910
```
Is there a way to improve the sqldatabasechain agent that performs database queries through finetuning of the gpt 3 mode
l? What I'm saying is that sometimes the SQL agent makes a mistake in what it has to query in the database according to 
the request it makes. Is it possible to improve it by finetuning the gpt 3.5 model taking into account that there is at 
most a total of 60 data for adjustment?
```
---

     
 
all -  [ Keeping up with the fast movement in AI space ](https://www.reddit.com/r/LangChain/comments/193ozls/keeping_up_with_the_fast_movement_in_ai_space/) , 2024-01-13-0910
```
Hi! With everything around LLMs moving at such a fast pace, papers, related frameworks, libraries, toolkits, open source
 models and more popping up every day, I found it much harder to stay on top of everything than before. How do you stay 
updated and effectively navigate this space. Any recommendations for blogs, communities, channels or strategies? Thanks 
in advance! 😊
```
---

     
 
all -  [ Holy f*** I have never seen such spaghetti code in my life ](https://www.reddit.com/r/LangChain/comments/193oz8b/holy_f_i_have_never_seen_such_spaghetti_code_in/) , 2024-01-13-0910
```
No wonder there barely exists tutorials or articles exploring complex workflows. To make anything other than a simple RA
G app you need to have a PHD in langchain. Better get studying 😭
```
---

     
 
all -  [ OpenAPI agent with Azure OpenAI LLM ](https://www.reddit.com/r/LangChain/comments/193lbjq/openapi_agent_with_azure_openai_llm/) , 2024-01-13-0910
```
Does anyone have examples of how to build an agent to perform API actions based on user input in natural language format
? I have the spec file and want to use OpenAPI agent.I came across examples but all were using open ai LLM.I want to use
 Azure endpoint
```
---

     
 
all -  [ How to decrease latency in RAG chatbots? ](https://www.reddit.com/r/LangChain/comments/193iq2l/how_to_decrease_latency_in_rag_chatbots/) , 2024-01-13-0910
```
Can someone help with template to build RAG Chatbot with low latency..
```
---

     
 
MachineLearning -  [ [D] Are Custom LLM RAG apps going to become redundant? ](https://www.reddit.com/r/MachineLearning/comments/1929n4f/d_are_custom_llm_rag_apps_going_to_become/) , 2024-01-13-0910
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

     
 
MachineLearning -  [ [P] An open-source project for deploying local models ](https://www.reddit.com/r/MachineLearning/comments/18zkm5m/p_an_opensource_project_for_deploying_local_models/) , 2024-01-13-0910
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

     
 
MachineLearning -  [ [Project] Temporal Augmented Retrieval (TAR) - Dynamic RAG ](https://www.reddit.com/r/MachineLearning/comments/18uddmj/project_temporal_augmented_retrieval_tar_dynamic/) , 2024-01-13-0910
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

     
 
MachineLearning -  [ [R][P] Autogen + Langchain Tools + Local LLM doesn't work. ](https://www.reddit.com/r/MachineLearning/comments/18tex1j/rp_autogen_langchain_tools_local_llm_doesnt_work/) , 2024-01-13-0910
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

     
 
MachineLearning -  [ [P] Seeking Advice for Building a School Handbook Chatbot Using OpenAI and Vector Databases ](https://www.reddit.com/r/MachineLearning/comments/18rndcp/p_seeking_advice_for_building_a_school_handbook/) , 2024-01-13-0910
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

     
 
deeplearning -  [ [D] Unleashing the Power of Langchain with Wandb: Revolutionizing Topic Modeling and Evaluation ](https://www.reddit.com/r/deeplearning/comments/191mm83/d_unleashing_the_power_of_langchain_with_wandb/) , 2024-01-13-0910
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

     
 
deeplearning -  [ Unlocking the Power of Language: How LangChain Transforms Data Analysis and More ](https://www.reddit.com/r/deeplearning/comments/18l788y/unlocking_the_power_of_language_how_langchain/) , 2024-01-13-0910
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

     
 
deeplearning -  [ [D] Mastering Chain Composition with LangChain Expression Language (LCEL) ](https://www.reddit.com/r/deeplearning/comments/18i0wot/d_mastering_chain_composition_with_langchain/) , 2024-01-13-0910
```
In the intricate landscape of modern software development, orchestrating complex sequences of actions seamlessly poses a
 significant challenge. Enter LangChain Expression Language (LCEL), a groundbreaking declarative approach designed to re
volutionize the composition of chains within software architecture.

Link: [https://medium.com/ai-artistry/mastering-cha
in-composition-with-langchain-expression-language-lcel-2d5041fb0cbd](https://medium.com/ai-artistry/mastering-chain-comp
osition-with-langchain-expression-language-lcel-2d5041fb0cbd)  
```
---

     
