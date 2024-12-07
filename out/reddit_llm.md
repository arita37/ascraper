 
all -  [ How to Evaluate the Quality of Generated Embeddings? ](https://www.reddit.com/r/LangChain/comments/1h8fmvz/how_to_evaluate_the_quality_of_generated/) , 2024-12-07-0913
```
I have generated embeddings from the text chunks (extracted from a PDF and split using NLTKText Splitter).

I want to ev
aluate whether the generated embeddings are good.

How should I proceed?

  
Any Suggestions!

thank you so much in adva
nce 
```
---

     
 
all -  [ Which term do you like best do describe the new wave of agent apps we’ve been seeing (Cursor, v0, Re ](https://www.reddit.com/r/LangChain/comments/1h8czld/which_term_do_you_like_best_do_describe_the_new/) , 2024-12-07-0913
```
1. Agent apps
2. Agent-Native Applications
3. Agentic Apps
4. Agentic Copilots
5. Agent-Native Apps (ANA)

(vote on your
 favorite 
```
---

     
 
all -  [ Stuck at learning ](https://www.reddit.com/r/n8n/comments/1h8bsxb/stuck_at_learning/) , 2024-12-07-0913
```
I come from a generative AI background/web development (RAG, langchain, openAI, API's, postgreSQL). I am planning on bui
lding my own company based on automation services with computer vision and generative AI. For this plan, I have been ext
ensively exploring n8n for the past month. I think I grasp most of the basics (I have build some workflows for customer 
service (image requests, text generation, ).  what will be my next steps in my learning?. I feel like I hit a point wher
e youtube tutorials/books are not enough as they are pretty basic. Could you suggest me learning for mid/expert level? I
 feel like this has happened in the past, but since I never worked in a software development company, I have no idea how
 to go from basics to advance skills.
```
---

     
 
all -  [ Going from 25% success rate with Langchain's Graph RAG to 99.4% using BAML ](https://www.reddit.com/r/LangChain/comments/1h8adm9/going_from_25_success_rate_with_langchains_graph/) , 2024-12-07-0913
```
Disclaimer: I work on BAML - a prompting config language to get structured outputs ( [https://github.com/BoundaryML/baml
](https://github.com/BoundaryML/baml) ) 

One of our BAML users decided to test our framework against Langchain's GraphD
ocument solution to do RAG with graphs and got some crazy results I had to share.

https://preview.redd.it/bfw5zak8ba5e1
.png?width=1330&format=png&auto=webp&s=233f4ea00e7b784aba684fc416a9717bb0a69364

Here is their blog post: [https://mediu
m.com/@khaledarindam/implementing-graphrag-with-smaller-open-source-llms-a-practical-guide-501a62864c15](https://medium.
com/@khaledarindam/implementing-graphrag-with-smaller-open-source-llms-a-practical-guide-501a62864c15) 

Here is the lan
gchain implementation: [https://github.com/arindamkhaled/OpenGraphRAG/blob/main/opengraphrag/graph\_rag\_small\_llms\_wo
\_baml.ipynb](https://github.com/arindamkhaled/OpenGraphRAG/blob/main/opengraphrag/graph_rag_small_llms_wo_baml.ipynb) 


We've had some similar feedback that examples that don't work with Langchain tend to work with BAML, since it uses a si
mplified schema format to do structured outputs with LLMs ( [https://www.boundaryml.com/blog/sota-function-calling?q=0](
https://www.boundaryml.com/blog/sota-function-calling?q=0) ). Happy to answer any questions. 
```
---

     
 
all -  [ What are the best techniques and tools to have the model 'self-correct?' ](https://www.reddit.com/r/OpenAI/comments/1h85b1b/what_are_the_best_techniques_and_tools_to_have/) , 2024-12-07-0913
```
# CONTEXT
I'm a noob building an app that analyses financial transactions to find out what was the max/min/avg balance e
very month/year. Because my users have accounts in multiple countries/languages that aren't covered by Plaid, I can't re
ly on Plaid -- I have to analyze account statement PDFs.

Extracting financial transactions like ||||||| 2021-04-28 | 45
2.10 | credit ||||||| _almost_ works. The model will hallucinate most times and create some transactions that don't exis
t. It's always just one or two transactions where it fails.

I've now read about Prompt Chaining, and thought it might b
e a good idea to have the model check its own output. Perhaps say 'given this list of transactions, can you check they'r
e all present in this account statement' or even way more granular do it for every single transaction for getting it 100
% right 'is this one transaction present in this page of the account statement', _transaction by transaction_, and have 
it correct itself.

# QUESTIONS:
1) is using the model to self-correct a good idea?

2) how could this be achieved? 

3)
 should I use the regular api for chaining outputs, or langchain or something? I still don't understand the benefits of 
these tools

# More context:
- I started trying this by using Docling to OCR the PDF, then feeding the markdown to the L
LM (both in its entirety and in hierarchical chunks). It wasn't accurate, it wouldn't extract transactions alright
- I t
hen moved on to Llama vision, which seems to be yielding much better results in terms of extracting transactions. but st
ill makes some mistakes
- My next step before doing what I've described above is to improve my prompt and play around wi
th temperature and top_p, etc, which I have not played with so far!
```
---

     
 
all -  [ Is Langsmith just good piece of trash? ](https://www.reddit.com/r/LangChain/comments/1h84qim/is_langsmith_just_good_piece_of_trash/) , 2024-12-07-0913
```
I use langsmith for tracing and prompt management. Initially it was good. But then they started to tweak UI every two da
ys and nowadays I just feel the website has become pathetic and unresponsive at some times. I don’t know am I the only o
ne experiencing it but its very frustrating as a developer. Had high hopes from langchain but got disappointed…

Any goo
d open source langsmith alternatives??
```
---

     
 
all -  [ Roast my resume too ](https://i.redd.it/g7p6s7xh095e1.png) , 2024-12-07-0913
```

```
---

     
 
all -  [ MD Doesn’t Seem Like the Right Intermediate Language To Connect LLMs to Webpages ](https://www.reddit.com/r/LangChain/comments/1h82xst/md_doesnt_seem_like_the_right_intermediate/) , 2024-12-07-0913
```
It seems like right now the canonical pipeline to feed webpages into LLMs is: HTML —> MD —> LLM

It makes sense that MD 
is a lot more usable than HTML since it strips away the bloat, but having tried numerous HTML —> MD tools, the reality i
s that a lot of the context of the webpage is lost in this translation. For example, if you put in a site like EBay or Z
illow into these tools, the output makes it nearly impossible to understand what’s going on, much less navigate the page
 with the LLM from this information.

What do people see as the future for what intermediate languages will appear to co
nnect web pages to LLMs?

I’ve always wondered if some sort of language that captures where elements were positional and
 what types of elements there were would be neat, but even this seems to have flaws of its own. The proliferation of so 
much JS helps very little here as well.
```
---

     
 
all -  [ Improve a RAG system that uses 200+ PDFs ](https://www.reddit.com/r/LangChain/comments/1h82gox/improve_a_rag_system_that_uses_200_pdfs/) , 2024-12-07-0913
```
Hello everyone, I am writing here to ask for some suggestions. I am building a RAG system in order to interrogate a chat
bot and get the info that are present in documentation manuals.

**Data Source:**

I have 200+ pdfs and every pdf can re
ach even 800/1000 page each.

**My current solution:**

**DATA INGESTION:**

I am currently using Azure DocumentIntellig
ence to extract the information and metadata from the pdfs. After that I start creating chunks by creating a chunk for e
very paragraph identified by Azure DocumentIntelligence. To this chunk I also attach the PageHeading and the previous im
mediate title found.

After splitting all in chunks I do embed them using 'text-embedding-ada-002' model of OpenAI.

Aft
er that I load all these chunks on Microsoft Azure index search service.

**FRONTEND and QA**

Now, using streamlit I bu
ilt a easy chat-bot interface.

Every time I user sends a query, I do embed the query, and then I use Vectorsearch to fi
nd the top 5 'similar' chunks (Azure library).

RERANKING:

After identified the top 5 similar chunks using vector searc
h I do send chunk by chunk in combination with the query and I ask OpenAI GPT-3.5 to score from 50 to 100 how relevant i
s the retrieved chunk based on the user query. I keep only the chunks that have a score higher than 70.

After this I wi
ll remain with around 3 chunks that I will send in again as a knowledge context from where the GPT model have to answer 
the intial query.

The results are not really good, some prompts are correctly answered but some are totally not, it see
ms the system is getting lost and I am wondering if is because I have many pdfs and every pdf have many many pages.

Any
one had a similar situation/use case? Any suggestion you can give me to help me improve this system?

Thanks!
```
---

     
 
all -  [ LangGraph based literature review agent - hackathon winner project ](https://open.substack.com/pub/diamantai/p/nexus-ai-the-revolutionary-research?r=336pe4&utm_campaign=post&utm_medium=web&showWelcomeOnShare=true) , 2024-12-07-0913
```
Happy to share the first blog post about an incredible agent developed during the hackathon (by the 1st place winners) I
 organized with LangChain.

This agent, powered by LangGraph, slashes literature review times in research from 40% to ju
st 10%—outperforming previous state-of-the-art models with only a slight tradeoff in processing time (a matter of second
s).

Code is fully available on the GenAI_Agents open-source repository and there is a link to it in the blog.
```
---

     
 
all -  [ AI Agent creation with Dynamic Node pathways  ](https://www.reddit.com/r/LangChain/comments/1h7zhno/ai_agent_creation_with_dynamic_node_pathways/) , 2024-12-07-0913
```
For most of the AI Agents, like CrewAI or Autogen or even Langgraph, what I found that we can only give the goal and the
n define which agent does what. In Langgraph, we have to define the entire workflow in advance from what I get from the 
docs. 

But I wanted to check if a problem of code debugging, which might involve multiple steps and multiple different 
pathways, is there a way to handle the management of creating all these possible paths & having the Agent walk through e
ach of them one by one? The key difference between the nodes of the graph are created after execution of some initial no
des. 

Or should I manage this outside the Agentic Framework with a custom setup and DB etc.
```
---

     
 
all -  [ Ollama, langchain ans local database ? ](https://www.reddit.com/r/ollama/comments/1h7z7ev/ollama_langchain_ans_local_database/) , 2024-12-07-0913
```
Hi all,
I've been using ollama since a few months now and wanted to go a bit further in my application.

To be honest, I
 am a bit confused about how to use it. 
 
Here is what I had in mind : use langchain to understand the user input and c
onvert it to either a SQL or NoSQL query (I work on SQL and Mongodb) and then format the results into a small sentence. 
But I don't know if langchain is here to build literaly the query based on a context? Or just to ordinates the command (
understand the user input, find the correct table/collection, adjust parameters based on the fields of the collection/ta
ble, retrieve results...).

Can someone help me with that? Maybe it is not even the correct tool that I'm using!

Thanks
!
```
---

     
 
all -  [ Best way to store image and text embeddings in vector store?
 ](https://www.reddit.com/r/LangChain/comments/1h7ycvq/best_way_to_store_image_and_text_embeddings_in/) , 2024-12-07-0913
```
Working on a RAG based PDF Query system for documents with complex layout.

I was not sure weather to store the embeddin
gs of text and images into unified vector store or create different vector store for each.

What would be the better app
roach for this?
```
---

     
 
all -  [ Help needed to clean data ](https://www.reddit.com/r/LangChain/comments/1h7urvf/help_needed_to_clean_data/) , 2024-12-07-0913
```
I have a bunch of tweets and now I want to filter the tweets in some categories. How can I automate this process. 

```
---

     
 
all -  [ How to improve RAG results for searching a set of game rules ](https://www.reddit.com/r/LangChain/comments/1h7r7eb/how_to_improve_rag_results_for_searching_a_set_of/) , 2024-12-07-0913
```
I am trying to develop an Magic: The Gathering RAG AI system for answering rules questions and am having difficulty.

Fo
r example, the user asks a question like, 'what happens when all of these creatures die at the same time'

I use an agen
t to break down user question and use similarity search on my vector db. it searches by the entire question and by broke
n down terms like 'simultaneous death' 'creature dies' etc. per reddit QA board, a redditor answered the question the qu
estion referencing this rule:

603.10a Some zone-change triggers look back in time. These are leaves-the-battlefield abi
lities, abilities that trigger when a card leaves a graveyard, and abilities that trigger when an object that all player
s can see is put into a hand or library.

Clearly this is the key insight, but I'm not sure how it could have gotten to 
this key rule. To make things worse, I got a hallucination: - \`Simultaneous Deaths (Rule 704.3): When multiple creature
s die at the same time, they see each other die, which can trigger abilities that trigger on creatures dying.\`

Any ide
as? I am using chroma db, using custom text splitters to chunk by rule with small overlap. Do you think graph db could b
e more useful for a set of rules?
```
---

     
 
all -  [ TIL: LangChain has init_chat_model('model_name') helper with LiteLLM-alike notation... ](https://www.reddit.com/r/LangChain/comments/1h7qwbz/til_langchain_has_init_chat_modelmodel_name/) , 2024-12-07-0913
```
Hi! For those who, like me, have been living under a rock these past few months and spent time developing numerous JSON-
based LLMClient, YAML-based LLMFactory's, and other solutions just to have LiteLLM-style initialization/model notation -
 I've got news for you! Since v.0.3.5, LangChain has moved their [init\_chat\_model](https://python.langchain.com/docs/h
ow_to/chat_models_universal_init/) helper out of beta.



    from langchain.chat_models import init_chat_model
    
   
 # Simple provider-specific initialization
    openai_model = init_chat_model('gpt-4', model_provider='openai', temperat
ure=0)
    claude_model = init_chat_model('claude-3-opus-20240229', model_provider='anthropic')
    gemini_model = init_
chat_model('gemini-1.5-pro', model_provider='google_vertexai')
    
    # Runtime-configurable model
    configurable_mo
del = init_chat_model(temperature=0)
    response = configurable_model.invoke('prompt', config={'configurable': {'model'
: 'gpt-4'}})



[Supported providers](https://python.langchain.com/api_reference/langchain/chat_models/langchain.chat_mo
dels.base.init_chat_model.html): openai, anthropic, azure\_openai, google\_vertexai, google\_genai, bedrock, bedrock\_co
nverse, cohere, fireworks, together, mistralai, huggingface, groq, ollama.



Quite more convenient helper:

    from la
ngchain.chat_models import init_chat_model
    from typing import Optional
    
    def init_llm(model_path: str, temp: 
Optional[float] = 0):
        '''Initialize LLM using provider/model notation'''
        provider, *model_parts = model_
path.split('/')
        model_name = model_path if not model_parts else '/'.join(model_parts)
        
        if provid
er == 'mistral':
            provider = 'mistralai'
        
        return init_chat_model(
            model_name,
   
         model_provider=provider,
            temperature=temp
        )



Finally.

    mistral = init_llm('mistral/mi
stral-large-latest')
    anthropic = init_llm('anthropic/claude-3-opus-20240229')
    openai = init_llm('openai/gpt-4-tu
rbo-preview', temp=0.7)



Hope this helps someone avoid reinventing the wheel like I did!  

```
---

     
 
all -  [ LLM Access in AI Agents: Can Tools Tap Directly into Language Models? ](https://www.reddit.com/r/LangChain/comments/1h7o9fw/llm_access_in_ai_agents_can_tools_tap_directly/) , 2024-12-07-0913
```
In an AI agent architecture, can individual tools within the agent have direct access to a Large Language Model (LLM), o
r is LLM access restricted solely to the main agent?
```
---

     
 
all -  [ Best RAG framework for code (or general purpose) ](https://www.reddit.com/r/Rag/comments/1h7h7hm/best_rag_framework_for_code_or_general_purpose/) , 2024-12-07-0913
```
I've been working on building RAGs for codebases. I've been using langchain until now and while it is not terrible, it's
 also not my favorite, due to how misorganized it seems. The RAG works for now, but I'll probably build a lot of stuff o
n top of it, including custom re-rankers and retrievers. Before doing that, I'm  considering refactoring what I have int
o another framework, the more flexible the better.  
What would you guys suggest?

Edit: Forgot to add, but since this i
s a personal project, I was looking into frameworks that are free
```
---

     
 
all -  [ Adding authentication scheme to a langgraph api (self hosted)  ](https://www.reddit.com/r/LangChain/comments/1h7d7k8/adding_authentication_scheme_to_a_langgraph_api/) , 2024-12-07-0913
```
Hi, I was unable to find any documentation on how to add an authentication engine to a self hosted langgraph server inst
ance. Is there some documenation available? I was only able to access this :- [https://github.com/langchain-ai/langgraph
/discussions/2440](https://github.com/langchain-ai/langgraph/discussions/2440)
```
---

     
 
all -  [ Does LangGraph work in the browser??? ](https://www.reddit.com/r/LangChain/comments/1h7cu92/does_langgraph_work_in_the_browser/) , 2024-12-07-0913
```
`[ERROR] No matching export in 'browser-external:node:async_hooks' for import 'AsyncLocalStorage'`

`node_modules/@langc
hain/langgraph/dist/setup/async_local_storage.js:2:9:`

`2 │ import { AsyncLocalStorage } from 'node:async_hooks';`
```
---

     
 
all -  [ Struggling with LangGraph Academy's Lesson on Chains - Need Help! ](https://www.reddit.com/r/LangChain/comments/1h7cszn/struggling_with_langgraph_academys_lesson_on/) , 2024-12-07-0913
```
Hey everyone,

I’ve been following the LangGraph Academy course, and I just started the first module. Up until the chain
s lesson, we’ve been talking about nodes, edges, and graphs, which I was able to grasp pretty well. But now, they’ve sud
denly shifted gears and started talking about **tools, messages, chat models**, and I’m feeling a bit lost.

I kind of u
nderstand the gist of what’s going on, but I have somequestions:

1. **Why are we suddenly discussing messages and chat 
models out of nowhere?** I think I get that the messages are meant to represent some kind of state, right? Like we’re ke
eping track of all the messages in some way. But how is that supposed to scale? If there are thousands of steps, wouldn’
t the state end up bloated with a ton of unnecessary data? Isn’t that inefficient? Or is there some mechanism that prune
s or handles this?
2. **What exactly is a 'tool' in this context?** Is a tool just a component of a node? Or is it somet
hing separate that a node leads to, like its own independent entity? I’m having trouble visualizing how tools fit into t
he graph conceptually.

Sorry if this doesn’t make a ton of sense—I’m pretty confused myself, so I might not be articula
ting this perfectly. 😅 If anyone has gone through this course or has a clearer understanding of these concepts, I’d real
ly appreciate some guidance. Thanks in advance! 🙏
```
---

     
 
all -  [ I am building a fitness application  ](https://www.reddit.com/r/LangChain/comments/1h79rkw/i_am_building_a_fitness_application/) , 2024-12-07-0913
```
The app collects user inputs such as weight, height, goals, and more. It then generates a detailed workout and diet plan
. An agent will manage user data and query a CSV file containing various exercises and the muscles they target and how t
o do it and more.

So any tips or improvements  
Thanks in advance 
```
---

     
 
all -  [ QandA With Complex PDF. ](https://www.reddit.com/r/LangChain/comments/1h79pli/qanda_with_complex_pdf/) , 2024-12-07-0913
```
Hi folks - I just want know that whicb PDF parser will be a good choice to extract the data.

PDF can have complex data 
like text inside image inside image, data in tables, graphs,diagrams etc.
```
---

     
 
all -  [ How do I make my PDF RAG app smarter for question answering with tables in it?
 ](https://www.reddit.com/r/Rag/comments/1h77tq4/how_do_i_make_my_pdf_rag_app_smarter_for_question/) , 2024-12-07-0913
```
Hi all,  
I'm developing a PDF RAG app . My app is built using LCEL chain.

I'm currently using pymupdf4llm as the pdf p
arser ( to convert pdfs to their md format ), OpenAIEmbedding text-3-large as the embedding model, Cohere as the reranke
r and OpenAI ( gpt-4o-mini as the LLM ) .

My pdfs are really complex pdfs (containing texts , images , charts , tables.
.. a lot of them ).

The app can currently answer any question based on pdf text easily, but struggles with tables, spec
ially tables that are linked/related ( where answer can only be given by looking and reasoning at multiple tables ).

I 
want to make my PDF RAG app smarter. By smarter, I mean being able to answer questions which a human can find by looking
 and then reasoning after seeing multiple tables in the pdf.

What can I do ?

\[NOTE : I've asked this question on Lang
chain subreddit too but since my app is a RAG app and I need answers that's why posting here too\]
```
---

     
 
all -  [ How do I make my PDF RAG app smarter for question answering with tables in it? ](https://www.reddit.com/r/LangChain/comments/1h77shd/how_do_i_make_my_pdf_rag_app_smarter_for_question/) , 2024-12-07-0913
```
Hi all,  
I'm developing a PDF RAG app . My app is built using LCEL chain.

I'm currently using pymupdf4llm as the pdf p
arser ( to convert pdfs to their md format ), OpenAIEmbedding text-3-large as the embedding model, Cohere as the reranke
r and OpenAI ( gpt-4o-mini as the LLM ) .

My pdfs are really complex pdfs (containing texts , images , charts , tables.
.. a lot of them ).

The app can currently answer any question based on pdf text easily, but struggles with tables, spec
ially tables that are linked/related ( where answer can only be given by looking and reasoning at multiple tables ).

I 
want to make my PDF RAG app smarter. By smarter, I mean being able to answer questions which a human can find by looking
 and then reasoning after seeing multiple tables in the pdf.

What can I do ?
```
---

     
 
all -  [ QandA With complex PDF in by using langchain ](https://www.reddit.com/r/LangChain/comments/1h76mdi/qanda_with_complex_pdf_in_by_using_langchain/) , 2024-12-07-0913
```
HI folks, I am working on a app in which user can upload a PDF and then start QandA with that PDF. PDF has very complex 
data like text inside image inside image, data in tabular / graph / diagrams format.

So which PDF parser will be best f
or this functionality
```
---

     
 
all -  [ Grouping runs with langsmith ](https://www.reddit.com/r/LangChain/comments/1h76bdq/grouping_runs_with_langsmith/) , 2024-12-07-0913
```
I am using langchain and langsmith, and want to group multiple llm calls in a single trace, and maybe add a tag to them.
  
I would want it to be somthing like:  
with group\_in\_single\_trace(tags=\['test'\]):  
   lllm call 1  
   llm call
 2

But cant find anything in the docs that does this. This seems like a very basic need, am i missing somthing?
```
---

     
 
all -  [ [For Hire] AI/ML Engineer & Full Stack Developer – Chatbots & Scalable Web Solutions ](https://www.reddit.com/r/forhire/comments/1h74krg/for_hire_aiml_engineer_full_stack_developer/) , 2024-12-07-0913
```
**Need an AI/Full Stack Developer? Let’s Connect!** 👋

Hi, I’m Sheryar, an experienced AI/ML Engineer and Full Stack Dev
eloper.

💻 **Full Stack Solutions**  
🔹 Sleek UIs: React/Angular  
🔹 Robust APIs: Node.js, NestJS  
🔹 Payment Systems: S
tripe Integration  
🔹 Cloud Hosting: AWS

🤖 **AI & Automation Expertise**  
🔹 Smart Chatbots: Powered by LangChain  
🔹 C
ustom AI Models: NLP, automation, and more

🌟 **Recent Projects**  
🚗 Ride-Sharing: Live tracking + payments  
📦 Logisti
cs: Multi-stop delivery  
🤖 AI Bots: Smart ordering & customer support

💰 **Rate:** $20–$25/hour (negotiable)  
📧 DM to 
discuss your project!   
GitHub: [storm1033](https://github.com/storm1033)

Let’s build something innovative and scalabl
e! 🌐✨
```
---

     
 
all -  [ Langchain pipeline making the application slow. ](https://www.reddit.com/r/LangChain/comments/1h743id/langchain_pipeline_making_the_application_slow/) , 2024-12-07-0913
```
I am using groq as my LLM for my chatbot,
I saw on Langsmith that my RAG pipeline is taking more time then the LLM.

How
 can I improve the speed of my application?
```
---

     
 
all -  [ How would you handle headers and footers of a page in RAG model? ](https://www.reddit.com/r/LangChain/comments/1h73laf/how_would_you_handle_headers_and_footers_of_a/) , 2024-12-07-0913
```
Hi. I made RAG system but sometimes search results are just footers and headers from multiple different pages. I have se
veral clients, so I need a general solution, not for a specific web site. This should be a very typical and classic prob
lem of a search engine. Does anyone know a well-known and easy-to-implement solution? Thanks.
```
---

     
 
all -  [ Methods for File Reranking and Selection ](https://www.reddit.com/r/Rag/comments/1h72or5/methods_for_file_reranking_and_selection/) , 2024-12-07-0913
```
There is BM25 in literature which is a library named as rank-bm25 on github. Langchain uses that bm25 library.
But it is
 not efficient, accuracy level is not satisfactory. So I was looking for different methods like TF-IDF vectorizer. Or ev
en easier, just use the embedding models results to rerank the document base as a last resort for high accuracy scores. 
And it worked pretty well.
There is still one point left, if knowledge base is large and it is not logical to do vector 
search in all of it, this is slow. So I am also looking for something different that can be used before indexing and vec
tor search.
Is there any other method? I want to share our insights.
```
---

     
 
all -  [ Submit Feedback Node (Getting runId from RunnableConfig inside a node) ](https://www.reddit.com/r/LangChain/comments/1h6zxwq/submit_feedback_node_getting_runid_from/) , 2024-12-07-0913
```
I have raised a question on the repo: [discussion](https://github.com/langchain-ai/langgraphjs/discussions/655) and in r
/LangGraph: [post](https://www.reddit.com/r/LangGraph/comments/1giuqw7/submit_feedback_node_getting_runid_from/)

In sum
mary, I want to programmatically, create a feedback on a LangSmith trace either through a tool or node. I figured the ri
ght place for it is a node since you can pass the Runnable Config and theoretically get the \`runId\` from it to be used
 in the \`langsmithClient.createFeedback\` function. I have attempted a few different ways to retrieve the runId and als
o manually setting it in the configurable object, but none seem to work. Has anyone been able to successfully do this wi
thin a graph node? (note my application is in ts. and I am using the langraph.js SDK)

I am not sure if this a bug from 
the LangGraph side or there is different way to be doing this. 
```
---

     
 
all -  [ Ever Changing LangChain APIs ](https://www.reddit.com/r/LangChain/comments/1h6zvr9/ever_changing_langchain_apis/) , 2024-12-07-0913
```
I started to learn LangChain and found some tutorial materials are dated. Apparently, LangChain has gone through revisio
ns of APIs. My question is how I can find out the new APIs when I run into deprecated APIs. For example, I ran into the 
following API call:

    chain = MultiPromptChain.from_prompts(llm, prompt_infos, verbose=True)
    

Then I saw the fol
lowing warning messages:

LangChainDeprecationWarning: Please see the migration guide at: 

[https://python.langchain.co
m/docs/versions/migrating\_memory/](https://python.langchain.com/docs/versions/migrating_memory/)  
  validated\_self = 
self.\_\_pydantic\_validator\_\_.validate\_python(data, self\_instance=self)

How do I find out the right updated API to
 use? Thanks.
```
---

     
 
all -  [ Best way to chunk html ](https://www.reddit.com/r/LangChain/comments/1h6z6bd/best_way_to_chunk_html/) , 2024-12-07-0913
```
I have htmls that I need to chunk in order to pass it to a LLM. It's not going to be used for rag, so I would like chunk
s with around 2-5k tokens each. 

Inside this htmls, I have long tables with thousands of lines. U guys have any suggest
ions on how to chunk this?

I was thinking on creating a chunking strategy with gpt4o, but would appreciate if there are
 ready to go repos or services on this!

Example of html i need to chunk (its a brazilian law text) [https://legislacao.
fazenda.sp.gov.br/Paginas/Portaria-SRE-77-de-2024.aspx](https://legislacao.fazenda.sp.gov.br/Paginas/Portaria-SRE-77-de-
2024.aspx)
```
---

     
 
all -  [ What is the best alternative to LangChain/LangGraph for experimentation and production ](https://www.reddit.com/r/LangChain/comments/1h6tvme/what_is_the_best_alternative_to/) , 2024-12-07-0913
```
There’s lots of dissatisfaction from the community about LangChain. Before I begin building my first MVP, I'd like to ge
t recommendations for alternative frameworks. I'm looking for options that would work well for both MVP development and 
production deployment. If there's a single framework suitable for both stages, that would be ideal, but I'm also open to
 hearing about different frameworks optimized for each phase. What would you recommend?
```
---

     
 
all -  [ List of FREE and Best Selling Discounted Courses ](https://www.reddit.com/r/udemyfreeebies/comments/1h6phyi/list_of_free_and_best_selling_discounted_courses/) , 2024-12-07-0913
```
# Udemy Free Courses for 05 December 2024

Here are the Udemy free courses available for December 5, 2024. Please note t
hat coupons may expire at any time, so enroll quickly to avail of the courses for free:



* [REDEEM OFFER ](https://ido
wnloadcoupon.com/udemy/28014/)Digital Hidden Secrets
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/28013/)Mindful 
Computing
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/28012/)Mastering Business Blueprints 101: The Ultimate Gui
de
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/28011/)Hack-Proof Banking: Defend Against Credit Card Threats!
* 
[REDEEM OFFER ](https://idownloadcoupon.com/udemy/28010/)DevOps MasterClass 2024: Terraform Kubernetes Ansible Docker
* 
[REDEEM OFFER ](https://idownloadcoupon.com/udemy/28009/)JavaScript Interview Masterclass: Top 300 Questions (2024)
* [R
EDEEM OFFER ](https://idownloadcoupon.com/udemy/28008/)Build 5 Spring Boot Projects with Java: Line-by-Line Coding
* [RE
DEEM OFFER ](https://idownloadcoupon.com/udemy/28007/)Spring Boot + Apache Kafka Course – The Practical Guide
* [REDEEM 
OFFER ](https://idownloadcoupon.com/udemy/28006/)Project Risk Aggregation: A Comprehensive Guide
* [REDEEM OFFER ](https
://idownloadcoupon.com/udemy/28005/)Customizable Project Risk Management Templates
* [REDEEM OFFER ](https://idownloadco
upon.com/udemy/28004/)Complete Generative AI Course With Langchain and Huggingface
* [REDEEM OFFER ](https://idownloadco
upon.com/udemy/28003/)Executive Program in Management and Business Administration
* [REDEEM OFFER ](https://idownloadcou
pon.com/udemy/28002/)10 Day MySQL Bootcamp | My SQL Database Design for Beginners
* [REDEEM OFFER ](https://idownloadcou
pon.com/udemy/28001/)Ultimate Ethical Hacking from Zero To Hero
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/2800
0/)Free PMI Project Management Professional (PMP) Tutorial – Mastering the PMP Mindset for Exam Success
* [REDEEM OFFER 
](https://idownloadcoupon.com/udemy/27999/)Free Human Resources Tutorial – Human Resource Management
* Free Power Query 
Tutorial – Power Query For Data Analysis with Microsoft Excel
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/27998/)

* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27997/)Free Meetings Tutorial – Mastering 1:1 Meetings: A Manager’s
 Toolkit for Success
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27996/)Free Tutorial – Stress Relief for Busy L
ives: Relax with NeuroGraphica®
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27995/)Free Tutorial – Levelling in 
Construction for Beginners – Mastering a Laser
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27994/)Free Self-Awar
eness Tutorial – La danza dei sette passi
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27993/)Free Tutorial – 100
 najpopularniejszych niemieckich czasowników
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27992/)Free Tutorial – 
Learning Photoshop Express from Scratch
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27991/)Free Artificial Intel
ligence (AI) Tutorial – Yapay Zeka ile Sermayesiz Şekilde Dolar Kazanın
* [REDEEM OFFER ](https://idownloadcoupon.com/ud
emy/27990/)Free Computer Basics Tutorial – Essential Excel
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27989/)Fr
ee AWS Certified Cloud Practitioner Tutorial – Curso base gratuito – Certificações AWS CLF-C02 e SAA-C03 PT
* [REDEEM OF
FER ](https://idownloadcoupon.com/udemy/27988/)Free Cash Flow Tutorial – Third Document of Financial Statements-Cash Flo
w Statement
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27987/)Free German Language Tutorial – LEARN GERMAN EASI
LY: THE EASY GUIDE TO SELF-LEARNING
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27986/)Free Building Information
 Modeling (BIM) Tutorial – Revit – Dynamo – 5 Rotinas introdutorias
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/
27985/)ChatGPT Prompt Engineering Mastery
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27984/)Adobe Premiere Pro 
CC: Video Editing for Beginners
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27983/)Mastering ChatGPT Prompt Engi
neering: Beginner to Advanced
* The ChatGPT Prompt Engineering Mastery Course
* [REDEEM OFFER](https://idownloadcoupon.c
om/udemy/27982/)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27981/)ChatGPT Masterclass: The Ultimate Beginner’s
 Guide!
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27980/)Videoscribe Whiteboard Animations : MasterClass With 
Project
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27979/)Canva Masterclass For Social Media And Content Creati
on
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27978/)Master Web & Mobile Design: Figma, UI/UX Essentials, +More

* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27977/)Fitness Mastery (Bodybuilding, Muscle Building, Gym Workout)

* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27976/)CSS Complete Course For Beginners
* [REDEEM OFFER ](https://
idownloadcoupon.com/udemy/27975/)Mastering Python, Pandas, Numpy for Absolute Beginners
* [REDEEM OFFER ](https://idownl
oadcoupon.com/udemy/27974/)2024 R Programming Bootcamp for Absolute Beginners
* [REDEEM OFFER ](https://idownloadcoupon.
com/udemy/27973/)Executive Diploma in Business Management
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27972/)Dat
a Center HVAC Design Fundamentals (Dual Certification)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27971/)Parale
gal Professional Certification (PPC)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27970/)From unknown to popular!
 Secrets to explosive brand growth
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27969/)Aire Acondicionado y Refri
geración (HVAC Mantenimiento PRO)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27968/)Python & Django REST API Bo
otcamp – Build A Python Web API
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27967/)French Language Course: Learn
 French/ Speak it like Natives
* A Career in HVAC : Exploring HVAC Career Trajectory
* [REDEEM OFFER](https://idownloadc
oupon.com/udemy/27966/)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27965/)Implementing Agile Marketing and Mark
eting Sprints
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27964/)Grow Your Sales With Conversion Rate Optimizati
on (CRO)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27963/)APICS CPIM Planning and Inventory Management | Exam 
Dumps
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27962/)Master PMI-PBA Exam: Business Analysis Mock Tests
* [RE
DEEM OFFER ](https://idownloadcoupon.com/udemy/27961/)\[NEW\] Prompt Engineering Practice Tests- Interview Questions
* [
REDEEM OFFER ](https://idownloadcoupon.com/udemy/27960/)Luxury Industry Professional Certification (LIPC)
* [REDEEM OFFE
R ](https://idownloadcoupon.com/udemy/27959/)Create a WordPress website with Hostinger!
* [REDEEM OFFER ](https://idownl
oadcoupon.com/udemy/27958/)TikTok Marketing. How to promote your business effectively!
* [REDEEM OFFER ](https://idownlo
adcoupon.com/udemy/27957/)ChatGPT & Midjourney & Gemini: Digital Marketing Assistants
* [REDEEM OFFER ](https://idownloa
dcoupon.com/udemy/27956/)Upwork Beginner Course: Win Freelance World
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy
/27955/)Make a WordPress Website with Elementor
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27954/)ICDL الرخصة ا
لدولية لقيادة الحاسب الآلي
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27953/)ChatGPT Prompts for Trading Stocks
 on Wall Street
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27952/)Firebase Database : CRUD Android App Developm
ent
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27951/)Hack Windows
* Ethical Hacking: Weaponization
* [REDEEM O
FFER](https://idownloadcoupon.com/udemy/27950/)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27949/)Ethical Hacki
ng: Command Injection
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27948/)Learn SQL from Scratch : SQL Tutorial
*
 [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27947/)Branding & Brand Marketing Professional Certification (BMPC)
*
 [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27946/)Acing the Java Interview: Top Java Interview Questions
* [REDE
EM OFFER ](https://idownloadcoupon.com/udemy/27945/)Contact Center Manager Professional Certification
* [REDEEM OFFER ](
https://idownloadcoupon.com/udemy/27944/)Docker for Beginners: a Hands-On Practice Course (+12 hours)
* [REDEEM OFFER ](
https://idownloadcoupon.com/udemy/27943/)Crea un Sistema de Compra y Venta con PHP, JS y MYSQL
* [REDEEM OFFER ](https:/
/idownloadcoupon.com/udemy/27942/)Mastering Mermaid.js: Diagram, Charts and Data Visualization
* [REDEEM OFFER ](https:/
/idownloadcoupon.com/udemy/27941/)Procurement Manager Professional Certification
* [REDEEM OFFER ](https://idownloadcoup
on.com/udemy/27940/)NSE7\_OTS-6.4: Fortinet Network Security Expert Practice 2024
* [REDEEM OFFER ](https://idownloadcou
pon.com/udemy/27939/)Blockchain Professional Certification
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27938/)Ul
timate AWS Solutions Architect Practice Exams 2024 600+ Q
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27937/)CDO
 Chief Digital Officer Executive Certification
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27936/)Trading Skills
 Evaluation – Forex Edition
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27935/)Trading Skills Evaluation – Finan
cial Markets Edition

GET MORE FREE ONLINE COURSES WITH CERTIFICATE – [CLICK HERE](https://idownloadcoupon.com/)
```
---

     
 
all -  [ List of FREE and Best Selling Discounted Courses ](https://www.reddit.com/r/udemyfreebies/comments/1h6phw3/list_of_free_and_best_selling_discounted_courses/) , 2024-12-07-0913
```
# Udemy Free Courses for 05 December 2024

Here are the Udemy free courses available for December 5, 2024. Please note t
hat coupons may expire at any time, so enroll quickly to avail of the courses for free:

* [REDEEM OFFER ](https://idown
loadcoupon.com/udemy/28014/)Digital Hidden Secrets
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/28013/)Mindful Co
mputing
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/28012/)Mastering Business Blueprints 101: The Ultimate Guide

* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/28011/)Hack-Proof Banking: Defend Against Credit Card Threats!
* [R
EDEEM OFFER ](https://idownloadcoupon.com/udemy/28010/)DevOps MasterClass 2024: Terraform Kubernetes Ansible Docker
* [R
EDEEM OFFER ](https://idownloadcoupon.com/udemy/28009/)JavaScript Interview Masterclass: Top 300 Questions (2024)
* [RED
EEM OFFER ](https://idownloadcoupon.com/udemy/28008/)Build 5 Spring Boot Projects with Java: Line-by-Line Coding
* [REDE
EM OFFER ](https://idownloadcoupon.com/udemy/28007/)Spring Boot + Apache Kafka Course – The Practical Guide
* [REDEEM OF
FER ](https://idownloadcoupon.com/udemy/28006/)Project Risk Aggregation: A Comprehensive Guide
* [REDEEM OFFER ](https:/
/idownloadcoupon.com/udemy/28005/)Customizable Project Risk Management Templates
* [REDEEM OFFER ](https://idownloadcoup
on.com/udemy/28004/)Complete Generative AI Course With Langchain and Huggingface
* [REDEEM OFFER ](https://idownloadcoup
on.com/udemy/28003/)Executive Program in Management and Business Administration
* [REDEEM OFFER ](https://idownloadcoupo
n.com/udemy/28002/)10 Day MySQL Bootcamp | My SQL Database Design for Beginners
* [REDEEM OFFER ](https://idownloadcoupo
n.com/udemy/28001/)Ultimate Ethical Hacking from Zero To Hero
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/28000/
)Free PMI Project Management Professional (PMP) Tutorial – Mastering the PMP Mindset for Exam Success
* [REDEEM OFFER ](
https://idownloadcoupon.com/udemy/27999/)Free Human Resources Tutorial – Human Resource Management
* Free Power Query Tu
torial – Power Query For Data Analysis with Microsoft Excel
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/27998/)
*
 [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27997/)Free Meetings Tutorial – Mastering 1:1 Meetings: A Manager’s T
oolkit for Success
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27996/)Free Tutorial – Stress Relief for Busy Liv
es: Relax with NeuroGraphica®
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27995/)Free Tutorial – Levelling in Co
nstruction for Beginners – Mastering a Laser
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27994/)Free Self-Awaren
ess Tutorial – La danza dei sette passi
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27993/)Free Tutorial – 100 n
ajpopularniejszych niemieckich czasowników
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27992/)Free Tutorial – Le
arning Photoshop Express from Scratch
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27991/)Free Artificial Intelli
gence (AI) Tutorial – Yapay Zeka ile Sermayesiz Şekilde Dolar Kazanın
* [REDEEM OFFER ](https://idownloadcoupon.com/udem
y/27990/)Free Computer Basics Tutorial – Essential Excel
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27989/)Free
 AWS Certified Cloud Practitioner Tutorial – Curso base gratuito – Certificações AWS CLF-C02 e SAA-C03 PT
* [REDEEM OFFE
R ](https://idownloadcoupon.com/udemy/27988/)Free Cash Flow Tutorial – Third Document of Financial Statements-Cash Flow 
Statement
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27987/)Free German Language Tutorial – LEARN GERMAN EASILY
: THE EASY GUIDE TO SELF-LEARNING
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27986/)Free Building Information M
odeling (BIM) Tutorial – Revit – Dynamo – 5 Rotinas introdutorias
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27
985/)ChatGPT Prompt Engineering Mastery
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27984/)Adobe Premiere Pro CC
: Video Editing for Beginners
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27983/)Mastering ChatGPT Prompt Engine
ering: Beginner to Advanced
* The ChatGPT Prompt Engineering Mastery Course
* [REDEEM OFFER](https://idownloadcoupon.com
/udemy/27982/)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27981/)ChatGPT Masterclass: The Ultimate Beginner’s G
uide!
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27980/)Videoscribe Whiteboard Animations : MasterClass With Pr
oject
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27979/)Canva Masterclass For Social Media And Content Creation

* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27978/)Master Web & Mobile Design: Figma, UI/UX Essentials, +More
*
 [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27977/)Fitness Mastery (Bodybuilding, Muscle Building, Gym Workout)
*
 [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27976/)CSS Complete Course For Beginners
* [REDEEM OFFER ](https://id
ownloadcoupon.com/udemy/27975/)Mastering Python, Pandas, Numpy for Absolute Beginners
* [REDEEM OFFER ](https://idownloa
dcoupon.com/udemy/27974/)2024 R Programming Bootcamp for Absolute Beginners
* [REDEEM OFFER ](https://idownloadcoupon.co
m/udemy/27973/)Executive Diploma in Business Management
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27972/)Data 
Center HVAC Design Fundamentals (Dual Certification)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27971/)Paralega
l Professional Certification (PPC)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27970/)From unknown to popular! S
ecrets to explosive brand growth
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27969/)Aire Acondicionado y Refrige
ración (HVAC Mantenimiento PRO)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27968/)Python & Django REST API Boot
camp – Build A Python Web API
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27967/)French Language Course: Learn F
rench/ Speak it like Natives
* A Career in HVAC : Exploring HVAC Career Trajectory
* [REDEEM OFFER](https://idownloadcou
pon.com/udemy/27966/)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27965/)Implementing Agile Marketing and Market
ing Sprints
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27964/)Grow Your Sales With Conversion Rate Optimization
 (CRO)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27963/)APICS CPIM Planning and Inventory Management | Exam Du
mps
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27962/)Master PMI-PBA Exam: Business Analysis Mock Tests
* [REDE
EM OFFER ](https://idownloadcoupon.com/udemy/27961/)\[NEW\] Prompt Engineering Practice Tests- Interview Questions
* [RE
DEEM OFFER ](https://idownloadcoupon.com/udemy/27960/)Luxury Industry Professional Certification (LIPC)
* [REDEEM OFFER 
](https://idownloadcoupon.com/udemy/27959/)Create a WordPress website with Hostinger!
* [REDEEM OFFER ](https://idownloa
dcoupon.com/udemy/27958/)TikTok Marketing. How to promote your business effectively!
* [REDEEM OFFER ](https://idownload
coupon.com/udemy/27957/)ChatGPT & Midjourney & Gemini: Digital Marketing Assistants
* [REDEEM OFFER ](https://idownloadc
oupon.com/udemy/27956/)Upwork Beginner Course: Win Freelance World
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/2
7955/)Make a WordPress Website with Elementor
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27954/)ICDL الرخصة الد
ولية لقيادة الحاسب الآلي
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27953/)ChatGPT Prompts for Trading Stocks o
n Wall Street
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27952/)Firebase Database : CRUD Android App Developmen
t
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27951/)Hack Windows
* Ethical Hacking: Weaponization
* [REDEEM OFF
ER](https://idownloadcoupon.com/udemy/27950/)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27949/)Ethical Hacking
: Command Injection
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27948/)Learn SQL from Scratch : SQL Tutorial
* [
REDEEM OFFER ](https://idownloadcoupon.com/udemy/27947/)Branding & Brand Marketing Professional Certification (BMPC)
* [
REDEEM OFFER ](https://idownloadcoupon.com/udemy/27946/)Acing the Java Interview: Top Java Interview Questions
* [REDEEM
 OFFER ](https://idownloadcoupon.com/udemy/27945/)Contact Center Manager Professional Certification
* [REDEEM OFFER ](ht
tps://idownloadcoupon.com/udemy/27944/)Docker for Beginners: a Hands-On Practice Course (+12 hours)
* [REDEEM OFFER ](ht
tps://idownloadcoupon.com/udemy/27943/)Crea un Sistema de Compra y Venta con PHP, JS y MYSQL
* [REDEEM OFFER ](https://i
downloadcoupon.com/udemy/27942/)Mastering Mermaid.js: Diagram, Charts and Data Visualization
* [REDEEM OFFER ](https://i
downloadcoupon.com/udemy/27941/)Procurement Manager Professional Certification
* [REDEEM OFFER ](https://idownloadcoupon
.com/udemy/27940/)NSE7\_OTS-6.4: Fortinet Network Security Expert Practice 2024
* [REDEEM OFFER ](https://idownloadcoupo
n.com/udemy/27939/)Blockchain Professional Certification
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27938/)Ulti
mate AWS Solutions Architect Practice Exams 2024 600+ Q
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27937/)CDO C
hief Digital Officer Executive Certification
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27936/)Trading Skills E
valuation – Forex Edition
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/27935/)Trading Skills Evaluation – Financi
al Markets Edition

GET MORE FREE ONLINE COURSES WITH CERTIFICATE – [CLICK HERE](https://www.reddit.com/r/udemyfreeebies
/)
```
---

     
 
all -  [ We made an agent with LangGraph that got 48.60% on SWE-bench, all open-source ](https://www.reddit.com/r/LangChain/comments/1h6o63g/we_made_an_agent_with_langgraph_that_got_4860_on/) , 2024-12-07-0913
```
We at [Composio](https://composio.dev/) are building the tool infrastructure for AI agents, and one of our users' bigges
t requests was toolkits for building custom coding agents that work. So, we created SWE-Kit, a starter template with all
 the toolkits for building AI coding agents.

To test the efficiency of our tools, we built a comprehensive AI agent com
plete [open-source ](https://github.com/ComposioHQ/composio/tree/master/python/swe/agent)using LangGraph and tested it o
n [SWE-bench](https://www.swebench.com/) verified, and it got 48.60%.

* **Code Analysis Tool:** Intelligently retrieves
 relevant code snippets from the repository.
* **File Tool:** Facilitates navigation and updates to files.
* **Shell Too
l:** Performs shell operations.
* **Git Tool:** Handles version control tasks.

We optimized the tools for improved func
tion calling accuracy.

The code is open-source, and you can even modify it to add external integrations like GitHub, Li
near, Slack, etc., using Composio to build a full-fledged AI software engineer. Check out the [SWE-Kit agent](https://bl
og.langchain.dev/composio-swekit/) blog published on LangChains’ blog for an architectural explanation of the SWE agent.


Write code, review it, write tests, and more.

I am not even kidding. Many companies have raised millions just from th
is.

Check out SWE-kit: [https://composio.dev/swe-kit/](https://composio.dev/swe-kit/)
```
---

     
 
all -  [ [Hiring] Currently working on a RAG + Big Data platform/marketplace and looking for developers ](https://www.reddit.com/r/LangChain/comments/1h6n2c6/hiring_currently_working_on_a_rag_big_data/) , 2024-12-07-0913
```
I'm currently building a RAG + Big data platform/marketplace. It will be modular drag and drop pipelines. Think what hom
e depot is for home builders, but we are for Analysts, Researchers, etc. The startup's name is Analytics Depot and when 
it comes to branding and marketing, we have a massive advantage. If you have built something along these lines, DM me. I
'd love to discuss how we can work together.
```
---

     
 
all -  [ HI all, 

I am building a RAG application that involves private data. I have been asked to use a loc ](https://www.reddit.com/r/LangChain/comments/1h6mk8y/hi_all_i_am_building_a_rag_application_that/) , 2024-12-07-0913
```
P.s I am currently experimenting with ollama
```
---

     
 
MachineLearning -  [ [P] Minima: local conversational retrieval augmented generation project (Ollama, Langchain, FastAPI, ](https://www.reddit.com/r/MachineLearning/comments/1h1pudq/p_minima_local_conversational_retrieval_augmented/) , 2024-12-07-0913
```
  
[https://github.com/dmayboroda/minima](https://github.com/dmayboroda/minima)  
  
Hey everyone, I would like to intro
duce you my latest repo, that is a local conversational rag on your files, Be honest, you can use this as a rag on-premi
ses, cause it is build with docker, langchain, ollama, fastapi, hf All models download automatically, soon I'll add an a
bility to choose a model For now solution contains:

* Locally running Ollama (currently qwen-0.5b model hardcoded, soon
 you'll be able to choose a model from ollama registry)
* Local indexing (using sentence-transformer embedding model, yo
u can switch to other model, but only sentence-transformers applied, also will be changed soon)
* Qdrant container runni
ng on your machine
* Reranker running locally (BAAI/bge-reranker-base currently hardcoded, but i will also add an abilit
y to choose a reranker)
* Websocket based chat with saving history
* Simple chat UI written with React
* As a plus, you 
can use local rag with ChatGPT as a custom GPT, so you able to query your local data through official chatgpt web and ma
c os/ios app.
* You can deploy it as a RAG on-premises, all containers can work on CPU machines

Couple of ideas/problem
s:

* Model Context Protocol support
* Right now there is no incremental indexing or reindexing
* No selection for the m
odels (will be added soon)
* Different environment support (cuda, mps, custom npu's)

Welcome to contribute (watch, fork
, star) Thank you so much!
```
---

     
 
MachineLearning -  [ [P] Open-source declarative framework to build LLM applications - looking for contributors ](https://www.reddit.com/r/MachineLearning/comments/1gkpazh/p_opensource_declarative_framework_to_build_llm/) , 2024-12-07-0913
```
I've been building LLM-based applications, and was super frustated with all major frameworks - langchain, autogen, crewA
I, etc. They also seem to introduce a pile of unnecessary abstractions. It becomes super hard to understand what's going
 behind the curtains even for very simple stuff.

[So I just published this open-source framework GenSphere.](https://gi
thub.com/octopus2023-inc/gensphere) The idea is have something like **Docker for LLMs**. You build applications with YAM
L files, that define an execution graph. Nodes can be either LLM API calls, regular function executions or other graphs 
themselves. Because you can nest graphs easily, building complex applications is not an issue, but at the same time you 
don't lose control.

You basically code in YAML, stating what are the tasks that need to be done and how they connect. O
ther than that, you only write individual python functions to be called during the execution. No new classes and abstrac
tions to learn.

Its all open-source. **Now I'm looking for contributors** to adapt the framework for cycles and conditi
onal nodes - which would allow full-fledged agentic system building! Pls reach out  if you want to contribute, there are
 tons of things to do!

PS: [you can read the detailed docs here,](https://gensphere.readthedocs.io/en/latest/) And go o
ver this quick [Google Colab tutorial.](https://github.com/octopus2023-inc/gensphere/blob/main/examples/gensphere_tutori
al.ipynb)
```
---

     
