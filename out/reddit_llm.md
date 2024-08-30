 
all -  [ You can reduce the cost and latency of your LLM app with Semantic Caching ](https://www.reddit.com/r/LLMDevs/comments/1f4h9xf/you_can_reduce_the_cost_and_latency_of_your_llm/) , 2024-08-30-0912
```
Hey everyone,

Today, I'd like to share a powerful technique to drastically cut costs and improve user experience in LLM
 applications: S**emantic Caching**.  
This method is particularly valuable for apps using OpenAI's API or similar langu
age models.

The Challenge with AI Chat Applications As AI chat apps scale to thousands of users, two significant issues
 emerge:

1. Exploding Costs: API calls can become expensive at scale.
2. Response Time: Repeated API calls for similar 
queries slow down the user experience.

**Semantic caching addresses both these challenges effectively.**

Understanding
 Semantic Caching Traditional caching stores exact key-value pairs, which isn't ideal for natural language queries. Sema
ntic caching, on the other hand, understands the meaning behind queries.

(🎥 I've created a YouTube video with a hands-o
n implementation if you're interested: [https://youtu.be/eXeY-HFxF1Y](https://youtu.be/eXeY-HFxF1Y) *)*

# How It Works:


1. Stores the essence of questions and their answers
2. Recognizes similar queries, even if worded differently
3. Reus
es stored responses for semantically similar questions

The result? Fewer API calls, lower costs, and faster response ti
mes.

Key Components of Semantic Caching

1. Embeddings: Vector representations capturing the semantics of sentences
2. 
Vector Databases: Store and retrieve these embeddings efficiently

The Process:

1. Calculate embeddings for new user qu
eries
2. Search the vector database for similar embeddings
3. If a close match is found, return the associated cached re
sponse
4. If no match, make an API call and cache the new result

Implementing Semantic Caching with GPT-Cache GPT-Cache
 is a user-friendly library that simplifies semantic caching implementation. It integrates with popular tools like LangC
hain and works seamlessly with OpenAI's API.

# Basic Implementation:

    from gptcache import cache
    from gptcache.
adapter import openai
    
    cache.init()
    cache.set_openai_key()

# Tradeoffs

Benefits of Semantic Caching

1. Co
st Reduction: Fewer API calls mean lower expenses
2. Improved Speed: Cached responses are delivered instantly
3. Scalabi
lity: Handle more users without proportional cost increase

Potential Pitfalls and Considerations

1. Time-Sensitive Que
ries: Be cautious with caching dynamic information
2. Storage Costs: While API costs decrease, storage needs may increas
e
3. Similarity Threshold: Careful tuning is needed to balance cache hits and relevance

# Conclusion

Conclusion Semant
ic caching is a game-changer for AI chat applications, offering significant cost savings and performance improvements.  

Implement it to can scale your AI applications more efficiently and provide a better user experience.

Happy hacking : 
)
```
---

     
 
all -  [ LLM-3D Print: Large Language Models To Monitor and Control 3D Printing
 ](https://www.reddit.com/r/LangChain/comments/1f4gehi/llm3d_print_large_language_models_to_monitor_and/) , 2024-08-30-0912
```
**Not my work so cant answer technical questions but I think this might belong here. Want to know if something like this
 can be made using langchain?** As someone who is a 3D printing hobbyist and work with LLMs this is super exciting.

I j
ust came across an interesting paper that explores a **Multi-Agent LLM Framework** for autonomous 3D printing, and I had
 to share it here. This framework uses multiple Large Language Models (LLMs), ChatGPT4 in this case, each acting as its 
own intelligent agent, to manage different aspects of the 3D printing process. It’s pretty cool how they’ve set it up! 


[https://arxiv.org/abs/2408.14307](https://arxiv.org/abs/2408.14307)



Overall it seems actually useful use-case for L
LMs, and not just another LLM RAG or question/ans bot. Would love to hear thoughts on other potential applications using
 langchain.
```
---

     
 
all -  [ Senior Machine Learning Engineer Role Available! ](https://www.reddit.com/r/MLjobs/comments/1f4fmz0/senior_machine_learning_engineer_role_available/) , 2024-08-30-0912
```
Are you an experienced machine learning engineer with a passion for building advanced AI solutions? **Loka**, a leading 
tech consultancy based in Silicon Valley, is looking for a skilled Senior Machine Learning Engineer to join our dynamic 
team!  
  
**Required Hard Skills:**

* 4+ years of ML engineering experience
* Bachelor’s degree in Computer Science or
 related
* Experience with Python, ML libraries and AI/ML frameworks (PyTorch, HuggingFace, TensorFlow, etc.)
* Experien
ce building GenAI solutions using LLMs, including frameworks like LangChain and LlamaIndex, prompt engineering, fine-tun
ing and serving models, and implementing common patterns like RAG and NLQ
* Client-facing experience
* Familiarity with 
containerization and orchestration tools

**Interested? For the full job description and to apply, check the link:** [ht
tps://app7.greenhouse.io/intern.../applications/4074124007](https://app7.greenhouse.io/internal_job_board/applications/4
074124007?fbclid=IwZXh0bgNhZW0CMTAAAR06V-GNkc9hMT1r6Osq5i5K_vwJe9fyR7QlrYoBh2WjDG7eEeVndqNOTkE_aem_3I3k2aRgVQw7kCMgXq5-p
w)  

```
---

     
 
all -  [ Domain specific Agentic RAG with LangChain and LangGraph ](https://www.reddit.com/r/LangChain/comments/1f4drgh/domain_specific_agentic_rag_with_langchain_and/) , 2024-08-30-0912
```
Hello everyone,

I just finished a new blog post on how to add domain specific data to RAG using Agents and make a smart
er Corrective RAG.

Here's the link: [https://www.metadocs.co/2024/08/29/simple-domain-specific-corrective-rag-with-lang
chain-and-langgraph/](https://www.metadocs.co/2024/08/29/simple-domain-specific-corrective-rag-with-langchain-and-langgr
aph/)

Have a nice read
```
---

     
 
all -  [ Implementing LangChain with OpenAI: Tool Calling and Streaming Output ](https://www.reddit.com/r/LangChain/comments/1f4d5pf/implementing_langchain_with_openai_tool_calling/) , 2024-08-30-0912
```


Hi everyone,

I’m exploring how to implement LangChain 2.0 with OpenAI’s models and I’m particularly interested in usi
ng tool calling and streaming output features.

Does anyone have experience or examples of how to set up LangChain with 
OpenAI for:

	1.	Tool Calling: How to configure LangChain to call external tools or APIs using OpenAI’s chat models?
	2.
	Streaming Output: Steps to enable and handle streaming output for real-time interactions?

Any guidance, code snippets,
 or resources would be greatly appreciated. Thanks!
```
---

     
 
all -  [ Most commonly used HuggingFaceEmbedding models ](https://www.reddit.com/r/LangChain/comments/1f4b4fa/most_commonly_used_huggingfaceembedding_models/) , 2024-08-30-0912
```
Which HuggingFaceEmbeddings models do you guys use the most for your various GenAI RAG projects?
```
---

     
 
all -  [ Open Source AI Agent for Developer Relations ](https://www.reddit.com/r/LangChain/comments/1f4atex/open_source_ai_agent_for_developer_relations/) , 2024-08-30-0912
```
We just launched on Product Hunt and Open Sourced our AI Agent that assists with managing developer relations. We built 
the Agent using LangGraph Studio, and we cannot recommend it enough. The OSS repo can also be a good starting point to m
ake dev focussed Agents! Any feedback welcome :)

[https://www.producthunt.com/posts/develyn](https://www.producthunt.co
m/posts/develyn)  


[https://github.com/openfunnel/develyn](https://github.com/openfunnel/develyn)

https://preview.red
d.it/dc880zz3knld1.png?width=1920&format=png&auto=webp&s=eb7f6265216b2a3cc761d3a4db84dfee708f279a
```
---

     
 
all -  [ For those using Langchain4j what DB and data persistence library are you using? ](https://www.reddit.com/r/LangChain/comments/1f4a0y5/for_those_using_langchain4j_what_db_and_data/) , 2024-08-30-0912
```

```
---

     
 
all -  [ How to extract textual data from Excel and PPTs and store in vector db for RAG? ](https://www.reddit.com/r/LangChain/comments/1f48zch/how_to_extract_textual_data_from_excel_and_ppts/) , 2024-08-30-0912
```
I would also need to store metadata to give citations of my queried result, like the file_name, sheet_name, row_id/colum
n_id or slide numbers in case of PPTs.

Read somewhere to read the files as pandas df and store in SQL database and run 
query agents on top of it. That is not an option. Need to use vector DB and RAG.
```
---

     
 
all -  [ Data hub for LLMs and RAG ](https://www.reddit.com/r/LLMDevs/comments/1f48kf3/data_hub_for_llms_and_rag/) , 2024-08-30-0912
```
Is there a provider where I can connect multiple data sources like for example google drive and sharepoint via single si
gn on and then use the complete data from all sources to create a RAG Chatbot with langchain?
```
---

     
 
all -  [ Extensive open source RAG tutorials is getting viral ](https://github.com/NirDiamant/RAG_Techniques) , 2024-08-30-0912
```
Hi all,

Sharing a repo I was working on for a while. 

It’s open-source and includes many different strategies for RAG 
(currently 23), including tutorials, and visualizations.

This is great learning and reference material.  
Open issues, 
suggest more strategies, and use as needed.

It got very popular - 5K stars within a month!

Enjoy!
```
---

     
 
all -  [ Fitness chatbot  ](https://www.reddit.com/r/LocalLLaMA/comments/1f45sti/fitness_chatbot/) , 2024-08-30-0912
```
I want to make a personalized fitness chat bot using langchain so I was hoping anyone could help me with data or any adv
ice in general.
Thank you 
```
---

     
 
all -  [ How can we restrict Database tables for particular users ](https://www.reddit.com/r/LangChain/comments/1f43iht/how_can_we_restrict_database_tables_for/) , 2024-08-30-0912
```
I have fine-tuned a META LLAMA 3.1 to generate SQL queries based on our schema. This model is integrated with LangChain'
s SQL chain to execute the query and provide the final response.

Now, what I want to achieve is to implement permission
s or restrictions based on user roles. Currently, the model gives output to all users, irrespective of any restrictions.
 For example, if HR users access this, they should only be able to query HR-related tables. Similarly, accounts users sh
ould only access accounts-related tables.

We can retrieve these user roles from the logged-in user information in ERPNe
xt, as it is integrated into our system.
```
---

     
 
all -  [ How to use OpenAI's Assistants API with LangChain? ](https://www.reddit.com/r/LangChain/comments/1f42rtg/how_to_use_openais_assistants_api_with_langchain/) , 2024-08-30-0912
```
I didn't find any wrapper or guide for using OpenAI's Assistants API in Langchain which has Code Interpreter, Websearch 
and file storage. How to use it? Is it a separate thing entirely?

EDIT: \[Solved\] Import from `langchain.agents.openai
_assistant.base.OpenAIAssistantRunnable`. So it wasn't in docs, but in API Reference [here](https://python.langchain.com
/v0.2/api_reference/langchain/agents/langchain.agents.openai_assistant.base.OpenAIAssistantRunnable.html#langchain.agent
s.openai_assistant.base.OpenAIAssistantRunnable).
```
---

     
 
all -  [ AI agents hype or real?  ](https://www.reddit.com/r/LangChain/comments/1f4264n/ai_agents_hype_or_real/) , 2024-08-30-0912
```
I see it everywhere, news talking about the next new thing. Langchain talks about it in any conference they go to. Many 
other companies also arguing this is the next big thing. 

I want to believe it sounds great in paper. I tried a few thi
ngs myself with existing frameworks and even my own code but LLMs seem to break all the time, hallucinate in most workfl
ows, failed to plan, failed on classification tasks for choosing the right tool and failed to store and retrieve data su
ccessfully, either using non structure vector databases or structured sql databases.

Feels like the wild west with ever
yone trying many different solutions. I want to know if anyone had much success here in actually creating AI agents that
 do work in production.

I would define an ai agent as :
- AI can pick its own course of action with the available tools

- AI can successfully remember , retrieve and store previous information.
- AI can plan the next steps ahead and can as
k for help for humans when it gets stuck successfully.
- AI can self improve and learn from mistakes.
```
---

     
 
all -  [ Any personal projects? ](https://www.reddit.com/r/LangChain/comments/1f40lxr/any_personal_projects/) , 2024-08-30-0912
```
Has anyone made or planning to make any interesting or useful personal projects using LangChain?
I am trying to teach La
ngChain some office juniors and want to assign them a fun personal project. 
```
---

     
 
all -  [ sql data to embeddings? ](https://www.reddit.com/r/Rag/comments/1f3zp2r/sql_data_to_embeddings/) , 2024-08-30-0912
```
Hi all - I'm early in my learning process about using LLMs with rag prompts, and at a high level it all is making sense.
  Ultimately, I'm looking for an architectural understanding of a RAG solution, since an operating assistant still might
 not hit the best practices.

I have a working assistant that references log data using OpenAI's assistant API, referenc
ing the data via file attachments. There are some limitations on the size of the data with this approach, so I've been f
ollowing this langchain tutorial on RAG with sql queries:  [https://python.langchain.com/v0.2/docs/tutorials/qa\_chat\_h
istory/](https://python.langchain.com/v0.2/docs/tutorials/qa_chat_history/)

  
You'll note that this tutorial dynamical
ly builds a query based on table schema info, then runs said query to extract data. But how does this work?  Is all the 
data returned from the query turned to an embedding behind the scenes? 

Is my understanding of embeddings even correct 
in that your text data (from documents, sql queries, web pages, wherever) is converted to a vector store and persisted (
somewhere) for reference by the LLM when evaluating the prompt? Once persisted, the LLM can intelligently search the vec
tor store, thereby keeping the size of the prompt within the token limits?


```
---

     
 
all -  [ Which langchain model provider for a Q for Business app? ](https://www.reddit.com/r/aws/comments/1f3z5x6/which_langchain_model_provider_for_a_q_for/) , 2024-08-30-0912
```
So, you can build apps via q for business, and under the hood it uses bedrock right, but the q for business bit does do 
some extra processing. (Seems it directs your request to different models)

is it possible to integrate that directly to
 langchain? if not, does the q for business app expose the bedrock endpoints that are trained on your docs, so you can t
hen build a langchain app?
```
---

     
 
all -  [ Where can I find people to chat with about langchain / LLM app development? ](https://www.reddit.com/r/LangChain/comments/1f3ymw8/where_can_i_find_people_to_chat_with_about/) , 2024-08-30-0912
```
I sadly don't know many other people in my real life who are working on langchain / LLM based apps and agents.  I'd like
 to find more people working on this sort of thing to learn from, chat with, and have some kind of community.  Any tips?


So far I checked out langchain's Discord.  It didn't look super active, and it seemed focused on Langchain itself -- w
hich makes sense, but I'm more interested in what we can do with these apps.

I've also of course checked here and got s
ome great answers to a question.  So maybe this is the answer.  Just wondering if there are more good places I can go to
 connect with people working on this stuff.
```
---

     
 
all -  [ Looking for Open-Source LangChain Apps with a Well-Structured Codebase ](https://www.reddit.com/r/LangChain/comments/1f3xskm/looking_for_opensource_langchain_apps_with_a/) , 2024-08-30-0912
```
Hi all,

I'm currently exploring LangChain and would love to see some open-source projects that utilize it effectively. 
I'm particularly interested in examples that showcase good coding patterns and practices. If anyone has come across any 
well-structured LangChain apps or repositories, I'd greatly appreciate it if you could share them. Thanks!
```
---

     
 
all -  [ [0 YoE, Fresher, SWE, India] ](https://i.redd.it/g1rpwfkp6kld1.jpeg) , 2024-08-30-0912
```
I am hoping to apply for tech companies for swe roles this december, please review my CV and suggest if any changes are 
to be done in the formatting, vocabulary, project description and anything.
Thanks in Advance!
```
---

     
 
all -  [ We created FloAI and created a support agent using it ](https://www.reddit.com/r/LangChain/comments/1f3wpi0/we_created_floai_and_created_a_support_agent/) , 2024-08-30-0912
```
We ([rootflo](https://rootflo.ai)) have been toying around AI for a while now. After doing a couple of smaller projects 
we understood the importance of using AI to maximize the efficiency of AI automation. That's when we tried out some avai
lable frameworks like auto-gen and crew-ai.

Trying out some of the existing frameworks, we felt limited by their capabi
lities and lack of control. This is when we tried to come up with out own framework for building agentic AI bots/agents.
 The thought was around composability where we want to make components like Lego blocks that can come together to create
 bigger structures. The inspiration came from some good whitepapers, and talks from a few veterans in the AI space like 
AndrewNg. We used langGraph as the underlying backend but will plan extensibility.

I would like some feedback from the 
community, and ideas that we can pursue that you see are some of the shortcomings of the current frameworks out there. H
ere a support agent implemented using FloAI: [https://medium.com/rootflo/build-an-agentic-ai-customer-support-bot-using-
floai-533660fb9c9b](https://medium.com/rootflo/build-an-agentic-ai-customer-support-bot-using-floai-533660fb9c9b)



Pro
ject URL: [https://github.com/rootflo/flo-ai](https://github.com/rootflo/flo-ai)

Some inspirations:

[https://arxiv.org
/abs/2308.08155](https://arxiv.org/abs/2308.08155)  
[https://arxiv.org/abs/2305.04091](https://arxiv.org/abs/2305.04091
)  
[https://arxiv.org/abs/2403.14403](https://arxiv.org/abs/2403.14403)  
[https://www.youtube.com/watch?v=sal78ACtGTc]
(https://www.youtube.com/watch?v=sal78ACtGTc)
```
---

     
 
all -  [ how to use map reduce chain type with gemini models using chatgooglegenerativeai ](https://www.reddit.com/r/u_Apprehensive_Diet644/comments/1f3v2iy/how_to_use_map_reduce_chain_type_with_gemini/) , 2024-08-30-0912
```
    model_name == 'GEMINI-1.5-FLASH':
            model = ChatGoogleGenerativeAI(model='gemini-1.5-flash',
             
                              google_api_key=GOOGLE_API_KEY,
                                           temperature=0,
 
                                          top_p=0.95
            )
    
    

I'm using custom callback function to get 
streaming responses by appending token by token in a queue. on\_llm\_new\_token using this event. As chatgooglegenerativ
eai does not have streaming parameter which I can set to True, so how should I get streaming responses from Gemini model
s using map reduce chain\_type. I'm using langchain's default map\_reduce chain for this?

Can anyone help me with this?


.invoke(), .stream(), .run() I tried using this for calling gemini

    map_reduce_chain = load_qa_chain(model, chain_
type='map_reduce')              
     data = map_reduce_chain.invoke({
                        'input_documents': new_do
cs,
                        'question': query,
                        'prompt': HTML_PROMPT_TEMPLATE.format(context=tot
al_text, question=query)                 
                       
                    })
    

I'm getting the answer in
 data\['output\_text'\] but not able to stream the answer token by token
```
---

     
 
all -  [ Million Parameter Models ](https://www.reddit.com/r/LangChain/comments/1f3ucqe/million_parameter_models/) , 2024-08-30-0912
```
Hello,   
If you've tried any million param open-source models for finetuning tasks like JSON generation or intent class
ification, Please share the model which you had used1
```
---

     
 
all -  [ RAG + Internet demo ](https://www.reddit.com/r/LangChain/comments/1f3tqy9/rag_internet_demo/) , 2024-08-30-0912
```
I tried enabling internet access for my RAG application which can be helpful in multiple ways like 1) validate your data
 with internet 2) add extra info over your context,etc. Do checkout the full tutorial here : https://youtu.be/nOuE_oAWxm
s
```
---

     
 
all -  [ proper nouns ](https://www.reddit.com/r/LangChain/comments/1f3r8w7/proper_nouns/) , 2024-08-30-0912
```
My chunks are a few sentences. sometimes a user might just say something short like 'who was jones'. 

Jones is mentione
d in some chunks, but it is not matching. How to handle proper nouns like this?
```
---

     
 
all -  [ RAG api with speech input & output? ](https://www.reddit.com/r/Rag/comments/1f3pu54/rag_api_with_speech_input_output/) , 2024-08-30-0912
```
I have been exploring some langchain and openai solutions, but finding a few things a bit complicated as per my need. So
 my question is, are there any APIs or services you guys know of that can take my speech as input and respond with a spe
ech/voice on my RAG?
```
---

     
 
all -  [ Delete thread by id ](https://www.reddit.com/r/LangChain/comments/1f3p5ph/delete_thread_by_id/) , 2024-08-30-0912
```
I have a graph with a SqliteSaver as a Checkpointer (memory). Is there any way I can delete a thread of messages by its 
id? Or how can I manage the memory?
```
---

     
 
all -  [ Sending the entire conversation on each call to the LLM ](https://www.reddit.com/r/LangChain/comments/1f3nqud/sending_the_entire_conversation_on_each_call_to/) , 2024-08-30-0912
```
Hello community. I am new to the world of LLMs and am building a system that uses them to help build a job descriptor as
istant within my company. 

The job description structure has 11 sections (I have a 3 page manual with a description of 
each one). 

The initial prompt is somewhat extensive, and if I wanted to implement it as a chat to assists users, I und
erstand that each time they will interact with the LLM, it would involve sending the entire initial prompt + all the int
ermediate conversations. Is this correct? Is there a way for the history to remain in the LLM and the consumption of inp
ut tokens to be only the new questions?

Thank you!
```
---

     
 
all -  [ Having problem with Langsmith about making a new project ](https://www.reddit.com/r/LangChain/comments/1f3nhiu/having_problem_with_langsmith_about_making_a_new/) , 2024-08-30-0912
```
Hello Bros,

  
I am newbie of langchain.

I was trying to follow the youtube of using langsmith

  
But Now I am stucke
d with this:

https://preview.redd.it/tm4hvzrllhld1.png?width=3808&format=png&auto=webp&s=470276cb4c9bd4cbfa383a6d56ee0c
229b4d1571

So I tried the + New Project

https://preview.redd.it/cs1tbteolhld1.png?width=1587&format=png&auto=webp&s=18
3926f9d4c5cb65eed7364f4bdbece42d076246

  
Ant That is it! There is no submit or save button..

Is this right? 

Thank y
ou in advance


```
---

     
 
all -  [ Cohere Reranker - Pros and Cons? ](https://www.reddit.com/r/LangChain/comments/1f3h9vk/cohere_reranker_pros_and_cons/) , 2024-08-30-0912
```
Tell me, is the CoHere Reranker a universal cure-all? Is it a must-have for RAG? Or does it have its drawbacks? I know i
t's used in Notion's search, and I must say, their search is pretty impressive.

So, if you're using it in your RAG, why
? And if you're not, why not?

I'm interested in any arguments, including your opinion on its cost and speed, not just t
he quality of the results.
```
---

     
 
all -  [ We used LangChain & CrewAI to build an open-source tool for automating pentesting with AI agents ](https://www.reddit.com/r/LangChain/comments/1f3gp8r/we_used_langchain_crewai_to_build_an_opensource/) , 2024-08-30-0912
```
Hi everyone,

With the rise of AI agents and recent advancements in agentic research, my friend and I wanted to explore 
whether we could develop a tool to automate parts of penetration testing. This led to the creation of TARS a few months 
ago.

TARS is our attempt to automate parts of cybersecurity penetration testing using AI agents by utilizing LangChain,
 CrewAI, and GPT-4. We've integrated tools that allow TARS to utilize Nettacker, RustScan, ZAP, Nmap, and web browsing v
ia the Brave API & Selenium.

Recently, we decided to make TARS accessible to everyone without any restrictions, so we o
pen-sourced TARS under the MIT license. We see the value in TARS's ability to generate general reports from surface-leve
l scans and its potential to perform unique attacks based on the model you're using.

Since TARS is in early development
 and still experimental, we'd greatly appreciate your feedback.

You can check out TARS here: [https://github.com/osgil-
defense/TARS](https://github.com/osgil-defense/TARS)

And view some demos of TARS here:

* Short Demo: [https://www.yout
ube.com/watch?v=Sjw\_gkSz6Lw](https://www.youtube.com/watch?v=Sjw_gkSz6Lw)
* Long Demo: [https://www.youtube.com/watch?v
=JSBVHl7PWek](https://www.youtube.com/watch?v=JSBVHl7PWek)

Thank you for reading
```
---

     
 
all -  [ [0 YoE, Unemployed, Software Engineering Intern, India] ](https://www.reddit.com/r/resumes/comments/1f3fr5t/0_yoe_unemployed_software_engineering_intern_india/) , 2024-08-30-0912
```
https://preview.redd.it/b3a1qcy1ufld1.png?width=5100&format=png&auto=webp&s=fa15554455c7d432797f81e9ca2c704e7c7a8139

I 
am a 3rd year Computer Science student.  
Have I written too many of my insignificant projects? Am i being too specific 
in listing my skills?

Any other suggestions?
```
---

     
 
all -  [ RAG PDFs and other documents easily with this open-source library ](https://www.reddit.com/r/opensource/comments/1f3cql0/rag_pdfs_and_other_documents_easily_with_this/) , 2024-08-30-0912
```
Ragable is an open-source library to help you build RAG apps faster. The library takes care of bare essentials such as:


1. Parse PDF, DOCX, TEXT files, and more into vector embeddings.
2. Store and query data from Qdrant.
3. Agent support.
 A basic and easy-to-use framework for building LLM agents. Agents can call pure Python functions. Easy to pass informat
ion around without complex wrapper libraries.

I built Ragable to make my life easy; previously I used Langchain, which 
to be honest is a superb library but it tends to get overcomplicated very quickly. I needed a simple framework to build 
upon, and have full control on what the library is doing.

You can view the project here: [https://github.com/plexcorp-p
ty-ltd/ragable](https://github.com/plexcorp-pty-ltd/ragable) 

PS: If you like the project, please star and share. I Wou
ld really appreciate your support! Thank you!
```
---

     
 
all -  [ Know of any Agents that build Agents? ](https://www.reddit.com/r/LangChain/comments/1f3cbsk/know_of_any_agents_that_build_agents/) , 2024-08-30-0912
```
Does anybody know examples of someone who's successfully used agents to build agents?

This strikes me as a really obvio
us use case, and someone has to have already done it much better than I will.

A specific smaller use case I have in min
d right now is that LLMs often suck at writing code, because they use outdated libraries.  I'm building documentation RA
Gs which are working okay some of the time...  But surely tons of people have done this already.  I just don't know wher
e/how to look.
```
---

     
 
all -  [ Gpt4 vision equivalent in AWS bedrock? ](https://www.reddit.com/r/LangChain/comments/1f3c26c/gpt4_vision_equivalent_in_aws_bedrock/) , 2024-08-30-0912
```
Hi I am going to start exploring models on AWS bedrock , one of my use cases involves text extraction from images , I ha
d used GPT4 vision for it , do we have any equivalent model in bedrock?
```
---

     
 
all -  [ How to Optimize Your RAG Application to Address Latency Issues  ](https://www.reddit.com/r/LangChain/comments/1f3b41v/how_to_optimize_your_rag_application_to_address/) , 2024-08-30-0912
```
What strategies can be used to optimize your RAG application for latency issues?
```
---

     
 
all -  [ Questions on Deciding Chunk Size for RAG Applications ](https://www.reddit.com/r/LangChain/comments/1f3b2ti/questions_on_deciding_chunk_size_for_rag/) , 2024-08-30-0912
```
When should you use larger chunk sizes, and when are smaller chunk sizes more appropriate?
```
---

     
 
all -  [ Best local model to translate novel ](https://www.reddit.com/r/LocalLLM/comments/1f3b07e/best_local_model_to_translate_novel/) , 2024-08-30-0912
```
Any recommendation?
Condition is below
Language is Kr => Eng
Gpu is 3090.
Prefer to langchain compatible.


```
---

     
 
all -  [ Issue when implementing RAG - Rerank system ](https://www.reddit.com/r/LangChain/comments/1f38qax/issue_when_implementing_rag_rerank_system/) , 2024-08-30-0912
```
* **Context**:

I'm currently building an LLM RAG for an enterprise in finance. They need this system to help them with 
the paperwork. Specifically, to retrieve documents relevant to the given question and the user.

They want the system to
 be able to adapt to the questions and the law domain using user feedback, so we added a Rerank model and trained the mo
del using customer feedback.

The LLM response is pretty simple, always display the top 5 docs in a markdown table (show
 some metadata of the doc) and they want to use GPT4-o for reasoning and rating the relevance of each of the 10 docs com
pared to the question.

For example:  
doc 1: summary Conf: 100%  
doc 2: summary Conf: 90%  
doc 3: summary Conf: 80%  

doc 4: summary Conf: 20%  
doc 5: summary Conf: 0%

The reason why they have to combine with LLM instead of just using 
a Cross-encoder to rank the relevance is they want the LLM to summarize and reason the document content, so they don't h
ave to go through the whole document to evaluate.

Users can look at this rating and re-rate it according to their logic
 (but 90% of the time they will just rely on GPT4 reasoning). All of this data will be automatically saved and used to t
rain the model.

* **How they test the rerank quality:**

The customer doesn't have ground truth data to train and on ou
r side, we have very little knowledge in finance. They manually ask one question and make the GPT4 rate the top 50 most 
relevant documents returned by the original rerank model, the result ranges from 0-100%, then train the rerank model usi
ng those data.  
To the customer and other members of my team, their expectation is after using the rerank model, the to
p 10 docs in the response should be **evaluated with confidence 100% by the GPT** and **none of the 0% docs should have 
appeared in the top 10**. Like this:

doc 1: summary Conf: 100%  
doc 6: summary Conf: 100%  
doc 11: summary Conf: 100%
  
doc 12: summary Conf: 100%  
doc 15: summary Conf: 90%

In reality, the result returns like this:

doc 1: summary Con
f: 100%  
doc 6: summary Conf: 100%  
doc 70: summary Conf: 100%  
doc 77: summary Conf: 100%  
doc 90: summary Conf: 0%


Some of the 100% rated docs appear in the top 10, many of them are not even in the original top 50 but still get reran
k to 10, and one of the latest top 10 is even rated with 0% relevance by GPT. They don't even look at the GPT reasoning 
and the content of the docs, just focus on the GPT confidence.

* **My problem is:**

I'm the only AI Engineer on this p
roject and everyone else (including PM and the customer, a full-stack, and QA) doesn't have background knowledge of Deep
 Learning. They expect the rerank model to adapt with just a few samples of data and take effect immediately (<100 sampl
es) then return docs that will be rated \~100% by the GPT. They say the rerank model is not working properly.

I have sp
ent a lot of time explaining to them that's not how DNN works and expecting the model to make any significant changes wi
th just a few data samples is not realistic, and the quality of the model also depends on the quality of the training da
ta. I looked at the GPT response closely, many 0% rated have very stupid responses and should be 100% instead, and if I 
try to ask the same question again, the confidence of the top 50 docs change. How can they train the Rerank model with s
uch small and hallucinated data and expect the model to work properly and adapt to the new domain?

* **My question:**


Are their expectation correct? Maybe I'm just being stupid.

1. How do you explain this to the customer and your colleag
ues?
2. Do you have a similar issue? What is your approach in this situation and how did you test the quality of the rer
ank model without ground truth? Maybe some suggestion is also welcomed.

\~Thanks a lot!
```
---

     
 
all -  [ 10 Free Resources on LLMs ](https://www.reddit.com/r/ArtificialInteligence/comments/1f3719f/10_free_resources_on_llms/) , 2024-08-30-0912
```
The world of Large Language Models (LLMs) is filled with noise and every day there are random courses, cheat sheets, and
 tools that can make beginners even more confused about the whole field. Do they start with fine-tuning language models,
 learn about Langchain, or just stick to Natural Language Processing (NLP) basics? There is so much content out there th
at it has become difficult to navigate.

So, for beginners, I have curated a list of free resources that will help them 
learn about LLMs and improve their building of AI applications. These resources include free courses, tutorials, blogs, 
boot camps, roadmaps, and an awesome list of tools and services.

Link: [10 Free Resources on LLMs (statology.org)](http
s://www.statology.org/10-free-resources-on-llms/)
```
---

     
 
all -  [ I want to build a data analysis agent  ](https://www.reddit.com/r/LangChain/comments/1f368jy/i_want_to_build_a_data_analysis_agent/) , 2024-08-30-0912
```
When I upload a csv file, I want llm to parse the csv file and analyze the data according to the user prompt or show a d
ata visualization such as a plot. 

 Has anyone created a project like this? Or is there any reference code for this top
ic? 
```
---

     
 
MachineLearning -  [ [P] using GPT4o with langchain/chroma for sports analysis  ](https://www.reddit.com/r/MachineLearning/comments/1enuzlp/p_using_gpt4o_with_langchainchroma_for_sports/) , 2024-08-30-0912
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

     
 
MachineLearning -  [ [R] [D] Langchain Evaluation with BeyondLLM
 ](https://www.reddit.com/r/MachineLearning/comments/1eki1fv/r_d_langchain_evaluation_with_beyondllm/) , 2024-08-30-0912
```
Hey everyone! Just came across a new feature of Beyond LLM that can evaluate Langchain RAG pipelines! It provides contex
t relevancy, answer relevancy, and groundedness. Check out the code snippet I’m sharing—perfect for testing your RAG pip
elines! For more info, be sure to check it out on GitHub [here](https://github.com/aiplanethub/beyondllm/blob/main/cookb
ook/evaluate_langchain_rag_pipeline_beyondllm.ipynb).

https://preview.redd.it/172m1y3dvsgd1.png?width=3972&format=png&a
uto=webp&s=63d5b0f41f0e46a58e7a2d5fb0d2bbc4384b3b1d


```
---

     
 
deeplearning -  [ Creating a project on NLP ](https://www.reddit.com/r/deeplearning/comments/1ey2e85/creating_a_project_on_nlp/) , 2024-08-30-0912
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

     
 
deeplearning -  [ How To Build Your Retrieval Augmented Generation (RAG) Using Open-source Tools: LangChain, LLAMA 3,  ](https://www.reddit.com/r/deeplearning/comments/1emdotx/how_to_build_your_retrieval_augmented_generation/) , 2024-08-30-0912
```


TL;DR: RAG overcomes the limitations of LLMs by bringing in external sources of information as relevant context.  
  

At the end of the step-by-step tutorial, you will be able to give your favorite LLM (ChatGPT, LLAMA 3, Mixtral, Gemini, 
Claude, etc.) some documents, ask it a question and see it respond based on relevant context.  
  
This will be running 
locally, using open-source libraries. Zero API and tooling costs.

[Step-by-step Notebook with zero-cost RAG](https://co
decompass00.substack.com/p/build-open-source-rag-langchain-llm-llama-chroma)

![img](69v6kjfj3wgd1)


```
---

     
 
deeplearning -  [ Need help with creating CLI for 'non-programmers' (LLMs) ](https://www.reddit.com/r/deeplearning/comments/1elrfgm/need_help_with_creating_cli_for_nonprogrammers/) , 2024-08-30-0912
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

     
