 
all -  [ is it LangChain or is it ML/AI in general? ](https://www.reddit.com/r/LangChain/comments/1fg4wir/is_it_langchain_or_is_it_mlai_in_general/) , 2024-09-14-0911
```
I'm curious, those who take issue with the organization/devEx of the LangChain ecosystem, what is the vector of your tec
hnical experience?

I am a web developer by trade and would have also critiqued the ease of use of the abstractions prov
ided my LC.  As I delve(lol) deeper into ML-land(looking at spaCy for named entity recognition, fine-tuning on own data)
, I'm starting to think that this is just the nature of the beast, moving/transforming/interpreting unconventionally abs
tract objects. I LangChain poorly organized and difficult to work with or is it just the nature of this new frontier in 
programming? 
```
---

     
 
all -  [ Create Your Own Local AI Chatbot with Ollama and LangChain ](/r/Medium/comments/1fg4g3v/create_your_own_local_ai_chatbot_with_ollama_and/) , 2024-09-14-0911
```

```
---

     
 
all -  [ Create Your Own Local AI Chatbot with Ollama and LangChain ](https://www.reddit.com/r/Medium/comments/1fg4g3v/create_your_own_local_ai_chatbot_with_ollama_and/) , 2024-09-14-0911
```
**Link:** [https://medium.com/@pratham52/create-your-own-local-ai-chatbot-with-ollama-and-langchain-ccd0a8c423e3](https:
//medium.com/@pratham52/create-your-own-local-ai-chatbot-with-ollama-and-langchain-ccd0a8c423e3)

**Short Description:**
 In this guide, we’ll walk through the process of developing a local AI chatbot using Ollama and LangChain. Whether you’
re interested in personal projects or professional applications, this tutorial will equip you with the knowledge to get 
started.
```
---

     
 
all -  [ Longer output results from RAG based pipeline ](https://www.reddit.com/r/LangChain/comments/1ffu3yi/longer_output_results_from_rag_based_pipeline/) , 2024-09-14-0911
```
How do you guys usually generate longer outputs from LLMs during the synthesis phase ? 

  
Most of the LLMs have a limi
ted output context window, typically 8k or maybe 16k. Even in that I have usually observed that they generally do not ac
hieve that length. Also, the output tokens are usually costly too.

In our RAG application, in the final synthesis phase
 where we are merging the retrieved results and sending to the LLM, we want to generate a tabular JSON output and expect
 longer output results. Right now, we are achieving this by grouping the retrieved results into different chunks, making
 LLM call on each group and then finally combining the result.

  
How is everyone else solving the use case of generati
ng longer outputs ? Let us say story writing/narration/long table generation/ etc?


```
---

     
 
all -  [ Is it just me or LangChain/LangGraph DevEx horrible? ](https://www.reddit.com/r/LangChain/comments/1fftyoy/is_it_just_me_or_langchainlanggraph_devex_horrible/) , 2024-09-14-0911
```
Full Disclosure: I'm the author of genkitx-graph and been part of Firebase Genkit early access. Still i'm using langchai
n & langgraph because they are the industry standard and have more functionality compared to genkit. But, compared to Fi
rebase Genkit it has a very primitive DevEx

1. There's no Dev UI to play with chains, runnables and models.
2. There's 
no local tracing for debugging.
3. You have to manually run a chain or runnable to debug.
4. LangGraph studio is heavy a
nd buggy. Often crashes my docker and takes 10+ GB of space.
5. LangGraph feels very restrictive and hacky when trying t
o build advanced graphs (subgraphs, private state, having separate edges and conditional edges rather than letting each 
node decide which node is next).
```
---

     
 
all -  [ Using Supabase / Firestore data as knowledge base ](https://www.reddit.com/r/LangChain/comments/1fft0yc/using_supabase_firestore_data_as_knowledge_base/) , 2024-09-14-0911
```
Good day everyone,

I am new to AI development and I will like to integrate AI to a new SaaS product I am working on.

T
he idea is to have a chat bot that interacts with the user's data, (I am thinking of using Supabase for this). Please I 
will like to know of this is possible and also if you have any links or recourse that can help please share.

Thanks
```
---

     
 
all -  [ Best way to download Wikipedia pages on Statistics, Probability, and Machine Learning? ](https://www.reddit.com/r/LangChain/comments/1ffq1hq/best_way_to_download_wikipedia_pages_on/) , 2024-09-14-0911
```
Hi everyone,

I'm looking to download Wikipedia pages related to statistics, probability, and machine learning for a pro
ject. 

I am trying to build a RAG based project on the above topics from Wiki.

I know Wikipedia offers data dumps, but
 I'm not sure about the most efficient approach. I have two main questions:

1. Is there a way to download only pages re
lated to statistics, probability, and ML directly from Wikipedia?
2. If not, and I need to download the entire English W
ikipedia data dump, what's the best method to filter out and separate the pages I need?

I'd appreciate any advice on to
ols, scripts, or methods that could help me accomplish this task efficiently. Thanks in advance for your help!
```
---

     
 
all -  [ RAG & Text2SQL merging ](https://www.reddit.com/r/LangChain/comments/1ffpd3x/rag_text2sql_merging/) , 2024-09-14-0911
```
I have a text2sql application with Mistral and I have a RAG application with Mistral. Now I need to create something whe
re both of them can work. If I ask a question to RAG it should answer and if I ask a question from text2sql then it shou
ld answer. So I want to combine them. Both models are ready and working fine both use the same llm aswell. Any ideas how
 to proceed with it. Any references, documentations etc. pls do share.
```
---

     
 
all -  [ Best OS repos to learn in javascript/typescript ](https://www.reddit.com/r/LangChain/comments/1ffnmi1/best_os_repos_to_learn_in_javascripttypescript/) , 2024-09-14-0911
```
Hello friends! I've been developing web applications for a time now. I'm trying to learn more about agents and tools, an
d Langchain in general! Do you know some Github repos where i can learn from and start getting involved? Preferably in j
s/ts but python is ok too! Thank you 
```
---

     
 
all -  [ Langchain Agents with OpenAI o1-preview or o1-mini?  ](https://www.reddit.com/r/LangChain/comments/1ffmlut/langchain_agents_with_openai_o1preview_or_o1mini/) , 2024-09-14-0911
```

Has anyone tried running Langchain agents with multiple tools on the new OpenAI o1-preview or o1-mini? I know GPT-4o st
opped working as the agent level model, and the workaround was using Claude or GPT-3.5 for agents while keeping GPT-4o f
or tools.

Does this still apply with the new models? Any insights would be appreciated!

```
---

     
 
all -  [ What is the best way to search for dates? ](https://www.reddit.com/r/Rag/comments/1ffgghk/what_is_the_best_way_to_search_for_dates/) , 2024-09-14-0911
```
I was trying to use LangChain's SelfQueryRetriever with AttributeInfo but was unsuccessful.
```
---

     
 
all -  [ Creating Self-Coding Agents ](https://www.reddit.com/r/LangChain/comments/1ffgcui/creating_selfcoding_agents/) , 2024-09-14-0911
```
Has anyone developed a system where agents can autonomously code entire agent-based systems? I’m currently facing a chal
lenge with streaming complex workflows to a chat UI efficiently. I’ve experimented with Mesop, Vercel, and Flask for cha
t tracking, but managing streams for multiple agents has proven tricky. I’m considering diving deeper into Streamlit to 
better handle chat bot integration. 

Any insights or suggestions would be greatly appreciated!


```
---

     
 
all -  [ Best place to find and hire an Agentic RAG expert? ](https://www.reddit.com/r/LangChain/comments/1ffehl5/best_place_to_find_and_hire_an_agentic_rag_expert/) , 2024-09-14-0911
```
Aussie startup here - about to close a couple million dollar round. We have huge enterprise clients begging for our prod
uct. 

Looking to bring on someone highly experienced in all things Agentic RAG full time. Can pay competitive salary fo
r next 2 years. 

Can be remote, but prefer someone in Australia due to R&D tax benefits. 

Where is the best place to l
ook for this person? Reddit? Upwork? LinkedIn? 




```
---

     
 
all -  [ What's the difference between Tool Calling, Structured Chat, and ReACT Agents? ](https://www.reddit.com/r/LangChain/comments/1ffe38x/whats_the_difference_between_tool_calling/) , 2024-09-14-0911
```
I've been trying to read the [documentation](https://python.langchain.com/v0.1/docs/modules/agents/agent_types/) on thes
e three types of agents -- and I still don't get exactly what the difference is.  Implementation looks very similar.  Th
ey can all call tools.  The prompts given in the quick start guides are a little different. What's actually the differen
ce?
```
---

     
 
all -  [ RAG System based on technical manual for cms usage ](https://www.reddit.com/r/LangChain/comments/1ffd8xu/rag_system_based_on_technical_manual_for_cms_usage/) , 2024-09-14-0911
```
I'm trying to create a RAG system for technical manuals for cms usage, the main problem here is on the reading of the pd
f file and the chuking of it. I'm having difficulties in finding a good way to read the pdf (one document object for eac
h page of the pdf or one documet object for the entire pdf?) and than another problem is the chunking of it. I've tried 
many strategies without getting good results. A big problem that I'm facing is about components of the cms that have pro
perties that are listed in tables that begin in one page and continue in the next page, in this cases the properties tha
t the retriever and the llm is giving as response are always incomplete because it's basically taking the first part of 
the table and missing the continuing in the next page. The document is organized in chapters for each component of the c
ms and there are around 200 of them. Is there a way to chunk the document and have a one-to-one relation between compone
nt and chunk to force the retriever to find the entire list of properties? I've tried RecursiveCharacterTextSplitter and
 SemanticChunker but they didn't give me good enough results. 
```
---

     
 
all -  [ Safely call LLM APIs without a backend
 ](https://www.reddit.com/r/LangChain/comments/1ffcne3/safely_call_llm_apis_without_a_backend/) , 2024-09-14-0911
```
I got tired of having to spin up a backend to use OpenAI or Anthropic API and figure out usage and error analytics per u
ser in my apps so I created Backmesh, the Firebase for AI Apps. It lets you safely call any LLM API from your app withou
t a backend with analytics and rate limits per user.

[https://backmesh.com](https://backmesh.com/)
```
---

     
 
all -  [ LangGraph Cloud ](https://www.reddit.com/r/LangChain/comments/1ffbhuw/langgraph_cloud/) , 2024-09-14-0911
```
Is anyone using langgraph cloud in production? If yes how is it better than hosting it yourself? Working on something th
at requires me to choose, weighing my options 
```
---

     
 
all -  [ Search for date in RAG ](https://www.reddit.com/r/LLMDevs/comments/1ffbflx/search_for_date_in_rag/) , 2024-09-14-0911
```
What is the best way to search for dates? I was trying to use LangChain's SelfQueryRetriever with AttributeInfo but was 
unsuccessful.
```
---

     
 
all -  [ Applied to 90+ SWE internships (summer 2025, spring 2025), no interviews :( Not sure what I'm doing  ](https://www.reddit.com/r/Resume/comments/1ff6b15/applied_to_90_swe_internships_summer_2025_spring/) , 2024-09-14-0911
```
https://preview.redd.it/2pndr3yvjeod1.png?width=1076&format=png&auto=webp&s=ccc562e76b07ccc28793239774f347a024e11add
```
---

     
 
all -  [ looking for team members for ATMECS Global GEN AI Hackathon 2024 ](https://www.reddit.com/r/developersIndia/comments/1ff3wwh/looking_for_team_members_for_atmecs_global_gen_ai/) , 2024-09-14-0911
```
Looking for people with experience in fullstack development, and having knowledge of LLMs, genAI and framworks like lang
chain, huggingface transformer.js. DM if you are interested.

[ATMECS Hackathon](https://www.hackerearth.com/challenges/
hackathon/atmecs-hackathon-2024/)
```
---

     
 
all -  [ Scaling LLM Data Extraction: Challenges, Design decisions, and Solutions ](https://www.reddit.com/r/LangChain/comments/1ff3jvn/scaling_llm_data_extraction_challenges_design/) , 2024-09-14-0911
```
[Graphiti](https://github.com/getzep/graphiti) is a Python library for building and querying dynamic, [temporally aware 
knowledge graphs](https://github.com/getzep/graphiti). It can be used to model complex, evolving datasets and ensure AI 
agents have access to the data they need to accomplish non-trivial tasks. It's a powerful tool that can serve as the dat
abase and retrieval layer for many sophisticated RAG projects.

**Graphiti was challenging to build.** This article disc
usses our design decisions, prompt engineering evolution, and approaches to scaling LLM-based information extraction. Th
is blog post kicks off a series exploring our challenges while building Graphiti. Reading this will deepen your understa
nding of both the Graphiti library and provide valuable insights for future development.

[Read the full article](https:
//blog.getzep.com/llm-rag-knowledge-graphs-faster-and-more-dynamic/).

>Using LangGraph? See our example notebook: [Buil
ding a ShoeBot Sales Agent using LangGraph and Graphit](https://github.com/getzep/graphiti/blob/main/examples/langgraph-
agent/agent.ipynb)

https://preview.redd.it/wzvm9t7k0eod1.png?width=2400&format=png&auto=webp&s=f34685d234df543bde52eed1
679a8fe85aa2f86e


```
---

     
 
all -  [ Semantix : Create Super functions with the help of LLMs ](https://github.com/chandralegend/semantix) , 2024-09-14-0911
```
### What Semantix Does

Current methods for extracting structured outputs from LLMs often rely on libraries such as DSPy
, OpenAI Structured Outputs, and Langchain JSON Schema. These libraries typically use Pydantic Models to create JSON sch
emas representing classes, enums, and types. However, this approach can be costly since many LLMs treat each element of 
the JSON schema (e.g., `{}`, `:`, `'$'`) as separate tokens, leading to increased costs due to the numerous tokens prese
nt in JSON schemas.

Semantix offers a different and more cost-effective solution. Instead of using JSON schemas, Semant
ix represents classes, enums, and objects in a more textual manner, reducing the number of tokens and lowering inference
 costs. Additionally, Semantix leverages Python's built-in typing system with minor modifications to provide meaning to 
parameters, function signatures, classes, enums, and functions. This approach eliminates the need for unnecessary Pydant
ic models and various classes for different prompting methods. Semantix also makes it easy for developers to create GenA
I-powered functions.

### Target Audience

Semantix is designed for developers who have worked with libraries like Langc
hain and DSPy and are tired of dealing with Pydantic models and JSON schemas. It is also ideal for those who want to add
 AI features to existing or new applications without learning extensive new libraries.

### Comparison

Semantix support
s multimodal inputs, allowing you to use images and videos effortlessly. Unlike other libraries, Semantix requires minim
al code changes to achieve excellent results.

Ready to give it a try? Check out our Colab notebook [here](https://colab
.research.google.com/github/chandralegend/semantix/blob/main/try.ipynb) and explore our GitHub repository [here](https:/
/github.com/chandralegend/semantix) for more details.
```
---

     
 
all -  [ We built a customer data RAG for LangChain based on entity resolution technology ](https://www.reddit.com/r/u_Tilores/comments/1ff08x7/we_built_a_customer_data_rag_for_langchain_based/) , 2024-09-14-0911
```
I'm Steven, one of the co-founders of [Tilores](https://tilores.io/), where we focus on real-time entity resolution to u
nify customer data. Recently, we've had some interesting conversations around how our solution could be used with LLMs, 
so we built an integration for LangChain.

With this integration, Tilores can serve as a retrieval-augmented generation 
(RAG) source for customer data. It allows you to unify data from various sources, update profiles in real-time, and perf
orm fuzzy searches across unified customer graphs—all within your LLM workflows.

We're looking for early users to help 
test and explore some use cases. If you're working with customer data and want to integrate it into your LangChain proje
cts, we'd love to talk.

The setup is quick, with no maintenance, and it scales with your data.

You can see our LangCha
in integration here: [https://github.com/tilotech/langchain-tilores](https://github.com/tilotech/langchain-tilores)

We 
also have an upcoming Product Hunt launch: [https://www.producthunt.com/products/tilores-rag](https://www.producthunt.co
m/products/tilores-rag)

I'd love to hear your thoughts.
```
---

     
 
all -  [ I want to get the sources of the retrieved context ](https://www.reddit.com/r/LangChain/comments/1fezyfk/i_want_to_get_the_sources_of_the_retrieved_context/) , 2024-09-14-0911
```
Hello,

I am developing a RAG based app. I want to get the sources of the retrieved context too along with the response.


    template = '''Please provide a thorough and precise response to the following question, ensuring that your 
      
          answer is exclusively grounded in the context provided. If the necessary information to formulate 
           
     a complete answer is absent from the context, kindly respond with 'I am sorry, I don't know' 
                or 'T
he document does not contain this information.'
    
                Your response should be well-structured, presented 
in a step-by-step format for maximum clarity, 
                and should include detailed explanations where appropriat
e. Feel free to incorporate relevant examples 
                to illustrate your points effectively.
    
             
   Context: {context}
                Question: {question}
    '''
    
    llm = Ollama(model='gemma2:2b')
    

    de
f generate_answer(retriever, query):
        prompt = ChatPromptTemplate.from_template(template)
        chain = (
     
       {'context':retriever, 'question':RunnablePassthrough()}
            |prompt
            |llm
            |StrOutp
utParser()
        )
    
        return chain.stream({'input': query})
    



I am using FIASS vector db.

  
Thanks i
n advance :)
```
---

     
 
all -  [ Agentic RAG Using CrewAI & LangChain! ](https://www.reddit.com/r/Rag/comments/1fexoqs/agentic_rag_using_crewai_langchain/) , 2024-09-14-0911
```
While studying to understand the buzz about agentic RAG, I was happened to look at CrewAI as one of the platforms to bui
ld AI agents. That is when my interest to build a simple agentic RAG started and [wrote this step-by-step tutorial](http
s://levelup.gitconnected.com/agentic-rag-using-crewai-langchain-bf935d26bc21) on building agentic RAG using CrewAI and L
angChain.

Hope you like it and share your views. 
```
---

     
 
all -  [ 요즘 가장 뜨거운 #CrewAI #Autogen #Langgraph 를 활용한 Agentic RAG 에 대해서 배워보겠습니다!, LangChain Quick Start - RAG  ](https://www.reddit.com/r/chatgpt_newtech/comments/1fevc2u/요즘_가장_뜨거운_crewai_autogen_langgraph_를_활용한_agentic/) , 2024-09-14-0911
```
요즘 가장 뜨거운 #CrewAI #Autogen #Langgraph 를 활용한 Agentic RAG 에 대해서 배워보겠습니다!, LangChain Quick Start - RAG 직접 코딩하면 확실하게 배웁니다. 제
 소스코드 가져가셔서 맘껏 활용하세요., [https://aitutor21.com/aistudy/1146](https://aitutor21.com/aistudy/1146)
```
---

     
 
all -  [ RAGAS + Langsmith for RAG chatbot ](https://www.reddit.com/r/Rag/comments/1fer045/ragas_langsmith_for_rag_chatbot/) , 2024-09-14-0911
```
Hey guys, I have an RAG chatbot that was built on chainlit, langchain (version 2). And now, I need to evaluate my llm re
sponses. I'm super new to this and don't know how to approach it. I am going through RAGAS documentation and understood 
that they provide metrics and langsmith has a good UI to visualize the metrics. So How can I implement it? If my chatbot
 is in production, how can I automate this evaluation? And if you have already implemented such thing, please please hel
p me out. Thanks !
```
---

     
 
all -  [ Help on a rag application ](https://www.reddit.com/r/LangChain/comments/1felvjc/help_on_a_rag_application/) , 2024-09-14-0911
```
So my team and I are working on building a gpt wrapper app and I want to build a rag system by indexing some notes I too
k on “Atomic Habits” book. Obviously it doesn’t make sense to index a whole book so I’m using my notes, or I don’t even 
know how expensive it will be to index the whole thing. I have experience with building small rag applications. My quest
ion is that I’m not experienced and I am looking for opinions on how I can outline this idea and execute it. if anyone h
as any tips regarding using langchain. Thanks
```
---

     
 
all -  [ AWS Reference Architecture for txtai RAG ](https://www.reddit.com/r/aws/comments/1feevhx/aws_reference_architecture_for_txtai_rag/) , 2024-09-14-0911
```
https://preview.redd.it/4e3mygwbl7od1.png?width=1746&format=png&auto=webp&s=650f35fd4139e5ba89f1b21726c60af025181108

[t
xtai](https://github.com/neuml/txtai) is an all-in-one open-source embeddings database for semantic search, LLM orchestr
ation and language model workflows.

txtai has support for both local and API-driven embeddings services and models. Thi
s reference architecture uses AWS Bedrock for embeddings + LLM calls. Content is stored in Postgres/pgvector via Aurora 
or RDS.  
  
Other frameworks like LangChain and LlamaIndex require code changes to switch from local to cloud. The same
 code can handle both with minor configuration changes in txtai!

https://preview.redd.it/lsd9bu4il7od1.png?width=886&fo
rmat=png&auto=webp&s=e28584c49ac346a951ac16bdd469cb15ff062cc5

Code: [https://gist.github.com/davidmezzetti/e5907591e941
1f47da7f9a9e91ec9d84](https://gist.github.com/davidmezzetti/e5907591e9411f47da7f9a9e91ec9d84)
```
---

     
 
all -  [ Reliable Agentic RAG with LLM Trustworthiness Estimates ](https://www.reddit.com/r/LangChain/comments/1fee66b/reliable_agentic_rag_with_llm_trustworthiness/) , 2024-09-14-0911
```
I've been working on Agentic RAG workflows and I found that automating decisions on LLM outputs can be pretty shaky. A*g
entic RAG* considers various retrieval strategies as tools available to an LLM orchestrator that can *iteratively decide
* which tools to call next based on what it’s seen thus far. The tricky part is how do we actually *decide* automaticall
y? 

[Using a trustworthiness score, the RAG Agent can choose more complex retrieval plans or approve the response for p
roduction.](https://preview.redd.it/ie2jqm9xf7od1.png?width=1560&format=png&auto=webp&s=658d5e3ee7391b7c2a1700251b892373
69b25750)

I found some success using uncertainty estimators to verify the trustworthiness of the RAG answer. If the ans
wer was not trustworthy enough, I increase the complexity of the retrieval plan in efforts to get better context. I [wro
te up](https://pub.towardsai.net/reliable-agentic-rag-with-llm-trustworthiness-estimates-c488fb1bd116) some of my findin
gs, if you're interested :)

Has anybody else tried building RAG agents? Have you had success decisioning with noisy LLM
 outputs?


```
---

     
 
all -  [ [1 YoE] Entry Level Engineer looking for roles in Traditional ML and Generative AI ](https://www.reddit.com/r/EngineeringResumes/comments/1fee3u4/1_yoe_entry_level_engineer_looking_for_roles_in/) , 2024-09-14-0911
```
Hi any review of my CV would be helpful thank you. I'm aware of some possible problems that may be present already:

* G
ap between education and previous employment. This is because of massive burnout after finishing degree most likely rela
ted to very recently diagnosed ADHD.
* It looks like there is a lack of traditional ML in my skillset however outside of
 my tutoring I haven't been working on any projects since I finished my education.
* Second role is essentially a contin
uation of the first role working directly with the client - i'm worried the short length of the role will put hiring man
agers off.

I'm looking for roles in London or remotely.

To be honest I'm not sure where to start with my CV, I imagine
 I will need to undertake a couple of projects to showcase more of my skills and help to improve my coverage.  I don't r
eally know if I am making the most of what experience I do have so any help would be appreciated.

https://preview.redd.
it/80g7l2m5g7od1.png?width=5100&format=png&auto=webp&s=b433c0a6f22e6656047cd8eacccc36cd9c5f70a4
```
---

     
 
MachineLearning -  [ [P] Review and suggest ideas for my chatbot ](https://www.reddit.com/r/MachineLearning/comments/1fb2mwl/p_review_and_suggest_ideas_for_my_chatbot/) , 2024-09-14-0911
```
Ok, so I am currently trying to build support chatbot with following technicalities 
1. FastAPI for web server(Need to m
ake it faster)
2. Qdrant as Vector Data Base(Found it to be the fastest amongst Chromadb, Elastic Search and Milvus)
3. 
MongoDB for storing all the data and feedback.
4. Semantic chunking with max token limit of 512.
5. granite-13b-chat-v2 
as the LLM(I know it's not good but I have limited options available)
6. The data is structured as well as unstructured.
 Thinking of having involving GraphRAG with current architecture.
7. Multiple data sources stored in multiple collection
s of vector database because I have implemented an access control.
8. Using mongoengine currently as a ORM. If you know 
something better please suggest.
9. Using all-miniLM-l6-v2 as vector embedding currently but planning to use stella_en_4
00M_v5.
10. Using cosine similarity to retrieve the documents.
11. Using BLEU, F1 and BERT score for automated evaluatio
n based on golden answer.
12. Using top_k as 3.
13. Currently using basic question answering prompt but want to improve 
it. Any tips? Also heard about Automatic Prompt Evaluation.
14. Currently using custom code for everything. Looking to u
se Llamaindex or Langchain for this. 
15. Right now I am not using any AI Agent, but I want to know your opinions. 
16. 
It's a simple RAG framework and I am working on improving it.
17. I haven't included reranker but I am planning to do so
 too.

I think I mentioned pretty much everything I am using for my project. So please share your suggestions, comments 
and reviews for the same. Thank you!!
```
---

     
 
MachineLearning -  [ [P] Lessons from Retrieval Augmented Generation ](https://www.reddit.com/r/MachineLearning/comments/1f9tvg7/p_lessons_from_retrieval_augmented_generation/) , 2024-09-14-0911
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

     
 
deeplearning -  [ Month of August in AI ](https://www.reddit.com/r/deeplearning/comments/1f6zfz0/month_of_august_in_ai/) , 2024-09-14-0911
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

     
 
deeplearning -  [ Creating a project on NLP ](https://www.reddit.com/r/deeplearning/comments/1ey2e85/creating_a_project_on_nlp/) , 2024-09-14-0911
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

     
