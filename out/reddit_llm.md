 
all -  [ One Drive RAG & Text to SQL ](https://www.reddit.com/r/LangChain/comments/1awm22j/one_drive_rag_text_to_sql/) , 2024-02-22-0909
```
Hi there,

I want to use a RAG for documents on One Drive and a Text to SQL as well in the same chat bot.

How would the
 Agent differentiate if the question needs to do the RAG (One Drive) or Interact with the database based on the user's q
uestion?

Is it a solved problem? If yes, how?
```
---

     
 
all -  [ This might seem like the dumbest question ever, but I can't get my Azure OpenAI service to work with ](https://www.reddit.com/r/LangChain/comments/1awk5pm/this_might_seem_like_the_dumbest_question_ever/) , 2024-02-22-0909
```
Wtf am i doing wrong?

I've got my Azure OpenAI service running ,but some reason Azure still gives the older version of 
the OpenAI's code despite the new version being out months now. 

But anyway, I'm literally just trying to get a f\*ckin
g basic prompt sent to the AI and print it's response.

Does anyone have a simple guide on how to do this basic everyday
 shit that that OpenAI literally gives you instantly from the playground?

Am I asking too much? I've combed through so 
many tutorials and asked so many LLMs, yet I can't get this basic thing to work.
```
---

     
 
all -  [ Langchian Rust ](https://www.reddit.com/r/LangChain/comments/1awk4i8/langchian_rust/) , 2024-02-22-0909
```
# 🎉 Exciting Personal Project Alert! 🎉

I'm delighted to share a personal endeavor of mine: a Rust port of Langchain. Ha
ving been a core contributor to the official Go Lang port of Langchain (langchaingo), I decided to challenge myself furt
her by exploring the Rust programming language. This project is an independent effort to reimagine Langchain's capabilit
ies within the Rust ecosystem, known for its emphasis on safety and performance.

Here's my take on bringing Langchain t
o Rust, a journey driven by my passion for learning and contributing to the open-source community:🔗 [https://github.com/
Abraxas-365/langchain-rust](https://github.com/Abraxas-365/langchain-rust)

This initiative is a personal project, not a
n official port, and represents my ongoing journey to expand my technical skills and contribute to innovative applicatio
ns of language models. I'm excited about the learning opportunities and potential applications this project might unlock
.I warmly invite you to explore the repository, share your insights, or even contribute. Your feedback and contributions
 would not only be welcome but also deeply appreciated, as they enrich the project and the wider community.Let's explore
 the possibilities that lie at the intersection of Rust and AI together!
```
---

     
 
all -  [ Perplexity’s copilot feature using LangGraph Planning Agent for RAG pipeline ](https://www.reddit.com/r/LangChain/comments/1awjuwp/perplexitys_copilot_feature_using_langgraph/) , 2024-02-22-0909
```
I am trying to build the perplexity's copilot feature for my RAG chatbot implementation.   


I am thinking of using Lan
gGraph Planning Agent (which I learnt about today). I am thinking of using Planner to ask for clarifying questions. For 
the execution stage I will be using either a simple query pipeline or the multi query engine.   


Please share your tho
ughts/ opinions about the feasibility aspect of the idea. Also, if you know about an open source project with similar fe
atures please feel free to share. TIA
```
---

     
 
all -  [ Need help in choosing memory type ](https://www.reddit.com/r/LangChain/comments/1awhcj3/need_help_in_choosing_memory_type/) , 2024-02-22-0909
```
I'm building sample project to learn about LangChain, the project is Finance based. Please suggest which memory type wou
ld be best based on the following information about the project - 

Title - **Aid in detection of Malicious Activities i
n Transactions**

As the title says, the project is about making use of LLM's and forming a kind of hypothesis to form a
 case wherein with the help of the chat interface the investigator can fetch details about the transactions. I plan on u
sing LangChain to interact with the database, which contains transaction details and also pass the relevant set of docum
ents of the account holder(using RAG). Here when the investigator is prompting the LLM, the LLM has to retain/store some
 of the previous conversations in the memory buffer to aid any further queries/questions. I'm confused on which memory t
ype to use..

&#x200B;

As per the documentation, the memory types are as follows - [https://python.langchain.com/docs/m
odules/memory/types/](https://python.langchain.com/docs/modules/memory/types/)  


Things to consider,

\- Assume I limi
ted set of tokens 

\- I want to keep the context of the previous conversations without storing too much information. 


&#x200B;

My thoughts,

use **ConversationSummaryBufferMemory** or **ConversationTokenBufferMemory** as these 2 are very
 close to what I want to achieve.

PS: I'm a beginner to LangChain and LLM development, please feel to correct incase of
 any mistakes and I'm eager to listen to your suggestions:)
```
---

     
 
all -  [ Kraken the Code: How to Build a Talking Avatar ](https://www.reddit.com/r/ArtificialInteligence/comments/1awh0vh/kraken_the_code_how_to_build_a_talking_avatar/) , 2024-02-22-0909
```
We joked with my colleague that this [post about real-time text-to-speech lipsync](https://monadical.com/posts/how-to-bu
ild-a-talking-avatar-with-azure-cognitive-langchain-and-openai.html) of his was either born too late because [Sora](http
s://openai.com/sora) is here to rule the industry or too early because his solution is tailored \*\*better\*\* than Sora
 for the specific task. Anyway, it's an ironic coincidence that he finished writing it before OpenAI released their vide
o monster 🦖. 

I personally think that his solution is niche enough, and Sora won't make it obsolete! What do you think?


The post has a lot of technical programming stuff, and I believe it will be very educational for engineers who are int
erested in AI!  
```
---

     
 
all -  [ Must To LEARN  Generative AI Frameworks 👆| LangChain | LlamaIndex | ChainLit | Hugging Face ](https://youtu.be/FpHOBOHfA78?si=dHANcc8spSZet1SW) , 2024-02-22-0909
```

```
---

     
 
all -  [ ToolExecutor Error when using langgraph ](https://www.reddit.com/r/LangChain/comments/1awf1tx/toolexecutor_error_when_using_langgraph/) , 2024-02-22-0909
```
Hello guys, i try to implement a langgraph example, i have a list of 2 tools, one is retriever from chroma db which i ha
ve created with create\_retriever tool , and the other is a custom tool , both tools work when i initialize an agent and
 invoke the AgentExecutor.

this is how i create my array : tools=\[tool1,tool2\] -> this works with agentexecutor  


W
hen i try to pass the tools to ToolsExecutor, when langgraph tries to use them i get the following error :

&#x200B;

At
tribute Error : 'list' object has no attribute 'tool'.

&#x200B;

Has anyone faced this error on ToolsExecutor ?
```
---

     
 
all -  [ [D] Graphs + vectordbs? Need your input: Cognee.ai . AI Data Pipelines for Real-World Production (Pa ](https://www.reddit.com/r/MachineLearning/comments/1aweo71/d_graphs_vectordbs_need_your_input_cogneeai_ai/) , 2024-02-22-0909
```
Hey there, Redditors!

I'm back with the latest installment on creating dependable AI data pipelines for real-world prod
uction.

If you've been following along, you know I'm on a mission to move beyond the '[thin OpenAI wrapper](https://top
oteretes.notion.site/Going-beyond-Langchain-Weaviate-and-towards-a-production-ready-modern-data-platform-7351d77a1eba40a
ab4394c24bef3a278?pvs=4)' trend and tackle the challenges of building robust data pipelines.

After a few months of work
, we integrated cognitive architecture with [keepi.ai](https://www.keepi.ai) 

We aim to explore with our demo:

**1. Co
ntext sanitization**  
The world of AI is fast-moving, and we've realized that the context is becoming a building block 
we refer to as a crucial part of future cognitive architecture.  
**2. Best Practices for AI Memory**  
In this rapidly 
evolving landscape, there are no established best practices. You'll need to make educated bets on tools and processes, k
nowing that things will change. We assume that having traditional data engineering practices + frameworks + classifiers 
and other AI solutions can solve a lot of standard hurdles  
**3. AI Frameworks**  
They are trying to do too much, too 
fast, too broad. We want to find a pattern and a correct layer of abstraction for the AI memory to fit new industry.  



&#x200B;

How does it work? 

The Github repo is l:

  


[How cognee works](https://preview.redd.it/yuiabmyihyjc1.png?
width=1633&format=png&auto=webp&s=4384c4441b615f72caf1e0591c5ab23aee735fab)

Github repo is [here](https://github.com/to
poteretes/cognee)

Next steps:  
I have questions for you:

1. Is context sanitization relevant for you?
2. How do you m
anage metadata? 
3. How do you prepare data for LLMs?
4. Are there any data enrichment steps you perform?

Check out the
 blog post:

[Link to part 4](https://topoteretes.notion.site/Going-beyond-Langchain-Weaviate-Level-4-towards-production
-fe90ff40e56e44c4a49f1492d360173c?pvs=4)

*Remember to give this post an upvote if you found it insightful!*  
*And also
 star our* [Github repo](https://github.com/topoteretes/cognee)
```
---

     
 
all -  [ RDF, Ontology, knowledge graph: QA ](https://www.reddit.com/r/LangChain/comments/1awemif/rdf_ontology_knowledge_graph_qa/) , 2024-02-22-0909
```
Hello, I'm trying to use an LLM to answer some questions using what is present in an ontology in rdf format. I wasn't ab
le to get results with the .ttl file so I thought of reducing the ontology and using a knowledge graph made up of very s
imple triples, like:

&#x200B;

    X hasOptionalKnowledge Y
    X hasURI Y

However, the model (OpenAI or LLAMA2 7b) do
es not seem to be able to answer, even when the questions are specific with keywords like:

    'what are the optional k
nowledges for a data scientist?'.

Has anyone ever worked on this type of data? Any help is welcome
```
---

     
 
all -  [ multiple users ](https://www.reddit.com/r/LangChain/comments/1awak6s/multiple_users/) , 2024-02-22-0909
```
hello, I've built a chatbot and it handles the conversation well, however I want to implement it on a larger scale, I wa
nt to make multiple users interact with it at the same time, and I want each user to have their own chat history and cha
tting experience, what is the best way to do so? I'm building the chatbot on WhatsApp btw, and it must handle each user 
conversation separately.
```
---

     
 
all -  [ Please review my resume. Not getting any interviews despite applying on a daily basis. ](https://www.reddit.com/gallery/1aw80tn) , 2024-02-22-0909
```
Hey everyone. I need some help. I am AI/ML Engineer and I've been actively looking for a job for the better part of a ye
ar. My current job pays too less and someone recommended me for it , so I am really looking for something. I apply daily
 for many jobs but have never gotten called for an interview. Please be as critical as you can! Any help and advice is a
ppreciated!
```
---

     
 
all -  [ Exllama V2 x langchain  ](https://www.reddit.com/r/LangChain/comments/1avz27t/exllama_v2_x_langchain/) , 2024-02-22-0909
```
Hello, 

for every person looking for the use of Exllama with Langchain & the ability to stream & more , here it is : 


\- [ExllamaV2 LLM](https://github.com/AmineDjeghri/langchain/blob/master/libs/community/langchain_community/llms/exllama
v2.py) : the LLM itself.

\- [Jupyter notebook](https://github.com/AmineDjeghri/langchain/blob/master/docs/docs/integrat
ions/llms/exllamav2.ipynb) : how to use it 

it still needs loras & more parameters, i will add that when i'll have some
 time. Any contribution is more than welcome
```
---

     
 
all -  [ Langchain, Langsmith, Llamaindex, and from Microsoft: Semantick Kernel, Prompt flow. Can someone exp ](https://www.reddit.com/r/aipromptprogramming/comments/1avvsw9/langchain_langsmith_llamaindex_and_from_microsoft/) , 2024-02-22-0909
```
 

Hello,  
Senior dev here. Getting into AI quick because I don't want to be one of those devs who are out of the loop 
of important changes.  
I'm currently struggling with getting the picture of what all these puzze pieces do and where th
ey fall in in the big picture.

Let's make as an example a classical angular webapp with a backend API that allows user 
to load his pdf or make speech to text as data to ingest.  
Then the user can query the LLM and get info on all the inge
sted data.

This is how I understood stuff:

**Llama index**: manages data ingestion, chunking, embedding and saving int
o a vector db. Except saving to vector db, does the rest based on either LLM models on azure or local.  
Provides interf
aces and classes to do all the work with these third party models/tools.

**Langchain/semantic kernel** = Allow flow con
trol and agents/planners.

Both of them from what I've seen from code snippets allow you to define pieces of code that e
ither call LLM online (or local?) with certain configuration (max tokens, temperature etc etc) and allow building agents
 by giving these pieces of code a description, then it's up to the LLM to decide what call based on that description

Yo
u can define either semantic functions (those which calls LLM) or native functions (you do stuff in your code)

These al
lows kinda controlling what LLM to call or what prompt to put as system prompt/metaprompt (the prompt you secretly send 
along with the original user request)

**Langsmith**: ???

**Prompt flow**: basically allows a predetermined sequence of
 actions without conditional statements (if/else) and allow you to call code from multiple languages/tools

# Data inges
tion

User will have a form to upload files

From what I get, you basically configure a prompt flow .yaml file for every
 action you want to do. So data ingestion for pdf files, for example, will have his own prompt flow.

This prompt flow w
ill call llamaindex for ingestion, then for chunking and for saving embeddings and chunks.

# User queries

You will hav
e a prompt flow that will need to call llamaindex for the RAG, then either semantick kernel or lamaindex will do stuff w
ith models online after the correct chunks of the pdf files have been retrieved.

In a more complex scenario, if multipl
e actions (agent-like behavior) is required, it will be task for Langchain or semantic kernel to do so.

Can anyone expa
nd and help me?  
I'm reanding a ton of docs and watching videos and I feel overwhelmed and lost
```
---

     
 
all -  [ Improving FAISS Query Accuracy with Regex Segmentation in LangChain ](https://www.reddit.com/r/LangChain/comments/1avu9v0/improving_faiss_query_accuracy_with_regex/) , 2024-02-22-0909
```
Hi LangChain Community,

I'm working with langchain\_community.vectorstores  
's FAISS for document segmentation. Initia
lly, I segmented documents into fixed-size chunks (1024) using RecursiveCharacterTextSplitter  
. This approach sometime
s cuts relevant information in half if it's at a chunk's end, leading to incomplete query responses.

To better align se
gmentation with document context, I switched to Regex-based segmentation, creating dynamically sized chunks. However, I'
ve hit a snag: FAISS.from\_documents  
 doesn't accept the list format produced by my Regex segmentation.

Does anyone h
ave tips on integrating Regex-segmented lists with LangChain's FAISS vector store for more accurate and complete query r
esponses?

Thanks for any insights!
```
---

     
 
all -  [ Query: How do I use LLM to narrow down a user query ](https://www.reddit.com/r/LangChain/comments/1avsdmu/query_how_do_i_use_llm_to_narrow_down_a_user_query/) , 2024-02-22-0909
```
Hi
I have a knowledge base of about 5000 articles. The user will be querying the knowledge base. A question can have mul
tiple answers in the knowledge base. Is it possible to use any chain to make the AI ask follow up questions to zero down
 on the exact response. I have already setup a vector store with PGVector and I’m able to query the knowledge base.
Exac
t scenario
Picture that I have 1000 articles about troubleshooting a laptop.
The user inputs a query: “my laptop is not 
booting up”
This can be because of multiple issues - RAM issue, motherboard issue, graphics card issue etc. I want the L
LM to respond back with a series of questions like “are there any beeps when you boot up the laptop “ if yes then ask ab
out the sequence of beeps and provide appropriate troubleshooting steps. If no, then it can ask him about any clacking s
ound arising from the disk etc…
Note these potential issues are there in the knowledge base . For example in a section c
alled RAM issues, there would be a listing that says “the laptop might not boot up due to a faulty RAM” to diagnose chec
k if there are any abnormal beeps during system start up.

Is this possible to achieve?
Any help would be appreciated.
```
---

     
 
all -  [ [For Hire] Programmer/Web Developer/IT Consultant (Python, PHP, AI, etc.) ](https://www.reddit.com/r/forhire/comments/1avqfpz/for_hire_programmerweb_developerit_consultant/) , 2024-02-22-0909
```
To get in contact, please message me, I don't use the chat thing and might miss you or reply very late. Then we can swit
ch to email/discord/telegram or whatever else. Apologies for starting with this, but many missed it when it was lower.


I'm a programmer/web developer with 14 years of professional experience. I am available for all sorts of programming and
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

Rate is $50/h.

Portfolio:

https://bdabkowski.yum.pl

Satisfied customer
s:

https://www.reddit.com/r/testimonials/comments/2e8gqy/pos_uqui_need_a_backend_web_dev_look_no_further/

https://www.
reddit.com/r/testimonials/comments/7fsdze/pos_hiring_uqui_was_an_example_of_how_it_should/

https://www.reddit.com/r/tes
timonials/comments/80pu9l/pos_uqui_great_work_detailed_and_fast/

https://www.reddit.com/r/testimonials/comments/b0nx68/
uqui_is_a_hardworking_intelligent_honest_apps/

https://www.reddit.com/r/testimonials/comments/j3mz3p/uqui_is_a_great_we
b_development_consultant_with/

https://www.reddit.com/r/testimonials/comments/v40ay3/pos_uqui_is_a_great_backend_dev_to
_work_with/

Please note: I am not a designer. To make it clear, it means zero aesthetic sense.
```
---

     
 
all -  [ Please roast my resume. Applied to tooo many jobs in the US and am not getting callbacks. ](https://www.reddit.com/r/resumes/comments/1avocxs/please_roast_my_resume_applied_to_tooo_many_jobs/) , 2024-02-22-0909
```
Hey,

I moved to the US (Bay Area) a few months ago, and have been applying for tons of jobs, but I've only received one
 callback so far. Most of the calls I have received are when 3rd party recruiters send my resume out to other companies.
 

I'm not sure what I'm doing wrong, I get that it's a bad market, but I dont think my resume is that bad that I dont g
et callbacks.

Fyi, I'm only able to apply for remote jobs/jobs in the bay area as I'm on an L2S. I dont need work autho
rization and I've mentioned that in the resume.

Appreciate the help. Thanks

&#x200B;

&#x200B;

https://preview.redd.i
t/jq48e16b6sjc1.jpg?width=612&format=pjpg&auto=webp&s=ca4be053fdbbf207bafb32dd1892bb00c8684147

https://preview.redd.it/
rfbuy06b6sjc1.jpg?width=612&format=pjpg&auto=webp&s=ec9018f497865343b34ecfb3da6923c3dbc24645
```
---

     
 
all -  [ Roast my resume as harshly as you can ](https://www.reddit.com/r/Resume/comments/1avo8jw/roast_my_resume_as_harshly_as_you_can/) , 2024-02-22-0909
```
Hey,

I moved to the US (Bay Area) a few months ago, and have been applying for tons of jobs, but I've only received one
 callback so far. Most of the calls I have received are when 3rd party recruiters send my resume out to other companies.
 

I'm not sure what I'm doing wrong, I get that it's a bad market, but I dont think my resume is that bad that I dont g
et callbacks.

Fyi, I'm only able to apply for remote jobs/jobs in the bay area as I'm on an L2S. I dont need work autho
rization and I've mentioned that in the resume.

Appreciate the help. Thanks

&#x200B;

https://preview.redd.it/t2xqrski
5sjc1.jpg?width=612&format=pjpg&auto=webp&s=490d2d3257ba96001481b71a80a5309f55f076a2

https://preview.redd.it/ksao9ski5s
jc1.jpg?width=612&format=pjpg&auto=webp&s=e05b06c179eb65bf3e2df2492a4f0ac4e5fd7d54

&#x200B;
```
---

     
 
all -  [ create_sql_query_chain is creating SQL text with ```sql ](https://www.reddit.com/r/LangChain/comments/1avnbui/create_sql_query_chain_is_creating_sql_text_with/) , 2024-02-22-0909
```
Having issues executing SQL queries generated by Langchian's create\_sql\_query\_chain function with the Gemini-Pro mode
l for SQLite DB. The generated SQL text includes '\`\`\`sql' which causes a syntax error when attempting to execute the 
query against the database. Any suggestions for a fix?
```
---

     
 
all -  [ Issue:How to use callback functions in a Langchain sequential chain ](https://www.reddit.com/r/LangChain/comments/1avh9ie/issuehow_to_use_callback_functions_in_a_langchain/) , 2024-02-22-0909
```
How to use callback functions in a Langchain sequential chain, such as 1->2->3. I want to loop through the 2 function n 
times in the middle, where the output of the 2 function is its input. At the end of the loop, the output of the 2 functi
on is input to the 3 function, and the final result is obtained

&#x200B;

There are two types of sequential chains in L
angChain:

SimpleSequentialChain: This is the simplest form of a sequential chain, in which each step has a single input
/output, and the output of one step becomes the input of the next -1SimpleSequentialChain: The simplest form of sequenti
al chains, where each step has a singular input/output, and the output of one step is the input to the next.\\n\\n \* Se
quentialChain: A more general form of sequential chains, allowing for multiple inputs/outputs'}}.

SequentialChain: This
 is the more general form of sequential chain, which allows for multiple inputs/outputs -1SimpleSequentialChain: The sim
plest form of sequential chains, where each step has a singular input/output, and the output of one step is the input to
 the next.\\n\\n \* SequentialChain: A more general form of sequential chains, allowing for multiple inputs/outputs'}}.


Here is an example of a SimpleSequentialChain:

python  
Copy code  
from langchain.llms import OpenAI  
from langchain
.chains import LLMChain  
from langchain.prompts import PromptTemplate

# This is an LLMChain to write a synopsis given 
a title of a play.

llm = OpenAI(temperature=.7)  
template = '''You are a playwright. Given the title of play, it is yo
ur job to write a synopsis for that title.

Title: {title}  
Playwright: This is a synopsis for the above play:'''  
pro
mpt\_template = PromptTemplate(input\_variables=\['title'\], template=template)  
synopsis\_chain = LLMChain(llm=llm, pr
ompt=prompt\_template)

# This is an LLMChain to write a review of a play given a synopsis.

llm = OpenAI(temperature=.7
)  
template = '''You are a play critic from the New York Times. Given the synopsis of play, it is your job to write a r
eview for that play.

Play Synopsis:  
{synopsis}  
Review from a New York Times play critic of the above play:'''  
pro
mpt\_template = PromptTemplate(input\_variables=\['synopsis'\], template=template)  
review\_chain = LLMChain(llm=llm, p
rompt=prompt\_template)

# This is the overall chain where we run these two chains in sequence.

from langchain.chains i
mport SimpleSequentialChain  
overall\_chain = SimpleSequentialChain(chains=\[synopsis\_chain, review\_chain\], verbose=
True)

review = overall\_chain.run('Tragedy at sunset on the beach')  
In this example, we create two LLmchains, one for
 writing a script outline and one for writing a script review, and then we execute the two chains in sequence 1 in the S
impleSequentialChain.
```
---

     
 
all -  [ Asked Perplexity to review my new book on Generative AI ](https://i.redd.it/gbnxxjzqlqjc1.png) , 2024-02-22-0909
```
LangChain in your Pocket: Beginner's Guide to Building Generative AI Applications using LLMs https://amzn.eu/d/fL5pIih
```
---

     
 
all -  [ Conversational Memory in SQLDB Chain ](https://www.reddit.com/r/LangChain/comments/1avgvuj/conversational_memory_in_sqldb_chain/) , 2024-02-22-0909
```
Hey , i am trying to use memory , inside SQLDB chain .   
Can someone guide me , if they have used it previously, there 
is nothing given about memory in the official docs.   
If not , is there a work around so that i can store and utilize m
y previous conversation using   


`db_chain = SQLDatabaseChain.from_llm(`

`llm, db, verbose=True, return_intermediate_
steps=True, top_k=10000, memory=memory`

`)`

this above peice of code is not working for me 
```
---

     
 
all -  [ [Student] Grad student in data analytics seeking roles in DS/DE/SWE ](https://www.reddit.com/r/EngineeringResumes/comments/1avd14x/student_grad_student_in_data_analytics_seeking/) , 2024-02-22-0909
```
 Hi Everyone! I'm graduating with my master's in December and I'm looking for feedback to improve my resume for data sci
ence/engineering or software engineering full-time or internship roles. I'm mainly looking in the midwest US but open to
 relocating.

I have more bullet points for the data scientist/software developer internships as those are the roles I w
ant to emphasize on due to what I'm looking for. I considered having bullet points for each of my projects but this just
 leads to spilling over to two pages, would really appreciate some advice

https://preview.redd.it/1bq62zjxdpjc1.png?wid
th=5100&format=png&auto=webp&s=94f4c265e64b62dd7bfe4c8d857ec5b20ecc78e4

&#x200B;
```
---

     
 
all -  [ Sebastian Raschka reviewing my LangChain book !! ](https://www.reddit.com/r/generativeAI/comments/1av9d3z/sebastian_raschka_reviewing_my_langchain_book/) , 2024-02-22-0909
```
Quite excited to share that my debut book  '***LangChain in your Pocket: Beginner's Guide to Building Generative AI Appl
ications using LLMs***', which is already going a bestseller in Amazon India, is getting reviewed by ***Dr. Sebastian Ra
schka***, author of bestsellers like '***Machine Learning with PyTorch and Scikit-Learn***'.  Dr. Raschka's expertise in
 AI is unparalleled, and I'm grateful for his insights, which will refine my work and future projects. 

You can check o
ut the book here : [https://www.amazon.com/dp/B0CTHQHT25](https://www.amazon.com/dp/B0CTHQHT25)

https://preview.redd.it
/tq55le2o9ojc1.png?width=873&format=png&auto=webp&s=8aa860428fcf9dd24f1755a99aa4eeb398b34627
```
---

     
 
all -  [ Sebastian Raschka reviewing my LangChain book !! ](https://www.reddit.com/r/LangChain/comments/1av9c9s/sebastian_raschka_reviewing_my_langchain_book/) , 2024-02-22-0909
```
Quite excited to share that my debut book  '***LangChain in your Pocket: Beginner's Guide to Building Generative AI Appl
ications using LLMs***', which is already going a bestseller in Amazon india, is getting reviewed by ***Dr. Sebastian Ra
schka***, author of bestsellers like '***Machine Learning with PyTorch and Scikit-Learn***'.  Dr. Raschka's expertise in
 AI is unparalleled, and I'm grateful for his insights, which will refine my work and future projects. 

You can check o
ut the book here : [https://www.amazon.com/dp/B0CTHQHT25](https://www.amazon.com/dp/B0CTHQHT25)

https://preview.redd.it
/d5jyqni89ojc1.png?width=873&format=png&auto=webp&s=1ea09a0ab6d98eb01259ff2849de702d4961df0a

&#x200B;

&#x200B;
```
---

     
 
all -  [ Thought: Langchain LLM ](https://www.reddit.com/r/LocalLLaMA/comments/1av82a7/thought_langchain_llm/) , 2024-02-22-0909
```
with how prolific the langchain library is getting; the documentation, examples, community workflows, etc

I noted two t
hings I'd like to bring up.
1. The langchain extended documentation would make a great meta cognition dataset to finetun
e a smaller language model on.
2. a language model proficient in langchain development, especially a smaller model (if s
ufficient loss can be achieved with less parameters), would be the most useful model.

phi-2 or phixtral or mistral7B or
 deepseek7B finetuned on a synthetically inflated 'user: lets build x,y,z chain' 'ai: {reiterated langchain example docu
mentation in step by step format}' dataset

when big tech says 'AI OS' 
they mean this right?

```
---

     
 
all -  [ ChatOpenAI response times compared to the web version of ChatGPT differ incredibly, what do? ](https://www.reddit.com/r/LangChain/comments/1av3iqx/chatopenai_response_times_compared_to_the_web/) , 2024-02-22-0909
```
Hello I was making some comparisons to improve performance in my llm app.

I have this prompt with 7k tokens, I noticed 
that the ChatOpenAI call takes around 3-4 seconds or at least its what langsmith is telling me. I'm using streaming for 
the responses.

I then tried the same prompt in the chat gpt web version and got a response in 700ms (!!) with gpt-3.5 w
hich is the same model I'm using in langchain.

I know it is not a huge difference, but it adds up because I have other 
llm operations that will increase the total response time.

Do you know if the faster response time is due just to highe
r computational power from their end? Is this a 'langchain is slow' scenario?


```
---

     
 
all -  [ Software Engineer Resume Advice - any changes before I start applying? ](https://www.reddit.com/r/resumes/comments/1auza3k/software_engineer_resume_advice_any_changes/) , 2024-02-22-0909
```
Hey everyone! I'll be graduating with my B.S. in Computer Science this May, and I'd like to start applying to entry-leve
l software engineer positions as soon as possible.

I've been working on my resume on my own for the past year. While I 
think it's decent so far, I'm sure there's room for improvement. Specifically, I think my projects section could be stro
nger.

Please let me know what you think! My goal is to finish fine-tuning it and start my application journey!

&#x200B
;

[My resume - Feb 2024](https://preview.redd.it/yyjvwtwd1mjc1.jpg?width=1487&format=pjpg&auto=webp&s=e2f1f64c3278e200c
63c77d8224ef0ad4b0731db)
```
---

     
 
all -  [ How can you add Graph Insights to your Plotly figures using LangChain & OpenAI? ](https://www.reddit.com/r/LangChain/comments/1auy45v/how_can_you_add_graph_insights_to_your_plotly/) , 2024-02-22-0909
```
I recently published this tutorial which uses the image-to-text GPT4 model to read Plotly Python graphs and share data i
nsights. You'll learn to use LangChain and Dash to create the insights button and incorporate the openai model to your a
pp.

[https://youtu.be/LO8c7oXG32M](https://youtu.be/LO8c7oXG32M)

I've been looking for a few open source image-to-text
 models but it's been hard to find. If anyone knows of any, please let me know.
```
---

     
 
all -  [ When has it made sense to build a custom RAG solution over using RAG as a service? ](https://www.reddit.com/r/LangChain/comments/1auviyf/when_has_it_made_sense_to_build_a_custom_rag/) , 2024-02-22-0909
```
In what situations might a developer expect to get better results by making a custom RAG system instead of using a pre-b
uilt offering, like OpenAI's file-retrieval API or another 3rd party prebuilt offering?

Is it only for niche use cases 
that a custom system is better? Or can almost any RAG system be modified to work better with the corpus of data it's wor
king with?
```
---

     
 
all -  [ What would be the best approach for a multitasking app ](https://www.reddit.com/r/LangChain/comments/1auui7f/what_would_be_the_best_approach_for_a/) , 2024-02-22-0909
```
Hello guys ! 

&#x200B;

I am learning my way with AI stuff, and don't know what would be the best approach for the app 
I am trying to develop.

&#x200B;

What I want to achieve is having a chat, and a way of uploading pdf, docs or txt file
s which will be formatted and then using openai embeddings I want to upload them to a vector DB.

&#x200B;

My questions
 is : What would be the best approach ? I am thinking of different agents, but would that be too slow ? I really don't k
now how to continue 
```
---

     
 
all -  [ Agent that uses a vector store retriever and a websearch retriever ( tavily or google search ) as to ](https://www.reddit.com/r/LangChain/comments/1auucox/agent_that_uses_a_vector_store_retriever_and_a/) , 2024-02-22-0909
```
Hello everyone , i'm currently stuck on making an agent that uses two different retrievers as tools through create\_retr
iever\_tool and initialize\_agent. However , im either getting stuck in a loop , getting wrong results or just exceeding
 context limit.

Im wondering if there is someone has done something like this with local models or any documentation on
 this subject. 

TIA

&#x200B;
```
---

     
 
all -  [ RAG: Passing entire retrieved chunk vs passing page_content ](https://www.reddit.com/r/LangChain/comments/1aurm4m/rag_passing_entire_retrieved_chunk_vs_passing/) , 2024-02-22-0909
```
I just realized that the entire `Document` is passed in context, not just the `document.page_content`, is this normal? I
 was expecting the page content of each documents to be concatenated.

```python
from operator import itemgetter

from l
angchain_community.vectorstores import FAISS
from langchain_core.output_parsers import StrOutputParser
from langchain_co
re.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableLambda, RunnablePassthrough
from langc
hain_openai import ChatOpenAI, OpenAIEmbeddings

vectorstore = FAISS.from_texts(
    ['harrison worked at kensho', 'harr
ison worked for 3 years'], embedding=OpenAIEmbeddings()
)
retriever = vectorstore.as_retriever()

template = '''Answer t
he question based only on the following context:
{context}

Question: {question}
'''
prompt = ChatPromptTemplate.from_te
mplate(template)

model = ChatOpenAI()

chain = (
    {'context': retriever, 'question': RunnablePassthrough()}
    | pr
ompt
)

chain.invoke('where did harrison work?')
```
```
ChatPromptValue(messages=[HumanMessage(content='Answer the ques
tion based only on the following context:\n[Document(page_content='harrison worked for 3 years'), Document(page_content=
'harrison worked at kensho')]\n\nQuestion: where did harrison work?\n')])
```
```
---

     
 
all -  [ Running classifier on Android or IOS? ](https://www.reddit.com/r/huggingface/comments/1auqnf4/running_classifier_on_android_or_ios/) , 2024-02-22-0909
```
Hi. I'm working on an app for which I need to classify text: Is it about a historical event, person  or place? From whic
h century or centuries? 

I have that working server-side with langchain and OpenAI 4, but I was wondering if there migh
t be a way to run something like that on the phone itself...?
```
---

     
 
all -  [ Best way to tag and summarize documents ](https://www.reddit.com/r/LangChain/comments/1auqhv4/best_way_to_tag_and_summarize_documents/) , 2024-02-22-0909
```
Hi

I am trying to transform my documents to get a summarization and tag them by categories

I've been using Doctran for
 that following guide https://python.langchain.com/docs/integrations/document_transformers/doctran_extract_properties 


For small amount of documents it works great, the answers are pretty accurate, exactly what I need.
The problem starts w
hen I am trying to do this with larger amount of Documents - in my case these are rows of CSV file

I need to run this t
ransformation over 4000 Documents with about 15k characters each

When trying to do this with 500 documents I get OpenAI
 timeout error

Is there any better way to do this kind of transformations? Or maybe I should split this data to smaller
 parts and run it several times?
```
---

     
 
all -  [ Tips for building RAG prompt ](https://www.reddit.com/r/LangChain/comments/1auq4l2/tips_for_building_rag_prompt/) , 2024-02-22-0909
```
Hi everyone. I'm pretty new with LLMs, and I've been working on a small script that extracts certain variables from real
ly big PDFs (that very often don't have the same structure as the other) with LangChain. 

Currently, I've been doing th
is using local LLama 2 models, generating local chunks and embeddings (with default strategies, no extra metadata so far
) stored in Chroma, and retrieving with RetrivalQA (saw recently is deprecated) , with a different prompt for each varia
ble. 

Besides the hallucinations and models refusing to not answer when they can't find the answer, I've been getting p
retty bad results, and I've been trying to work on building better prompts.

Do you guys have any tips/readings related 
to building prompts related to RAGs? I've read some articles and papers, but most of them talk about the topic generally
 and I haven't progressed very much on this aspect. 

Thanks in advance!
```
---

     
 
all -  [ Storing example_selector for later use ](https://www.reddit.com/r/LangChain/comments/1aup5mz/storing_example_selector_for_later_use/) , 2024-02-22-0909
```
I know you can store an FAISS db and load it later by serializing but is it possible to store an example selector? I hav
e created an example selector with a set of examples that have been embedded and I don't want to have to re-do that ever
y time. Any suggestions?

&#x200B;

e.g here is my selector  


`example_selector = MaxMarginalRelevanceExampleSelector.
from_examples(`  
 `# The list of examples available to select from.`  
 `examples,`  
 `# The embedding class used to p
roduce embeddings which are used to measure semantic similarity.`  
`OpenAIEmbeddings(),`  
 `# The VectorStore class th
at is used to store the embeddings and do a similarity search over.`  
`FAISS,`  
 `# The number of examples to produce.
`  
 `k=8,`  
`)`  
`example_prompt = PromptTemplate(`  
 `input_variables=['input', 'output'],`  
 `template='EXAMPLE:\
n{input}\n\n\{output}',`  
`)`  
`mmr_prompt = FewShotPromptTemplate(`  
 `# We provide an ExampleSelector instead of ex
amples.`  
 `example_selector=example_selector,`  
 `example_prompt=example_prompt,`  
 `prefix='EXAMPLES:\n\n',`  
 `su
ffix='\n\nEND OF EXAMPLES\n\n# Information:\n\n\n{job_info}\n# Proposal:\n\n',`  
 `input_variables=['info'],`  
`)`
```
---

     
 
all -  [ Getting import error for FlashrankRerank. ](https://www.reddit.com/r/LangChain/comments/1auowh4/getting_import_error_for_flashrankrerank/) , 2024-02-22-0909
```
I'm using [FlashrankRerank LangChain](https://python.langchain.com/docs/integrations/retrievers/flashrank-reranker), but
 when I use the code from this doc I'm getting this error:

```Bash
ImportError: cannot import name 'FlashrankRerank' fr
om 'langchain.retrievers.document_compressors' (c:\ProgramData\Anaconda3\envs\embedding\lib\site-packages\langchain\retr
ievers\document_compressors\__init__.py)
```

When I check the document compressor init file, it doesn't have FlashrankR
erank declaration init, was it removed from the recent update? Or am I doing anything wrong?
```
---

     
 
all -  [ [D] AI projects Suggestions ](https://www.reddit.com/r/MachineLearning/comments/1aunkmw/d_ai_projects_suggestions/) , 2024-02-22-0909
```
Hi Everyone, I need a suggestion to create AI courses for students ( Hands-on AI projects). I am thinking about the late
st AI trends such as Langchain, RAG, and vector databases. In each project, there can be multiple tasks, and the main th
ing is each task should have an automated system in which we can verify whether students have done it correctly or not.


For example: Project with visualization cannot be automatically tested. 

For example: A project with visualization can
not be automatically tested. . em can verify if the length of the text is smaller we can verify that it is correct.
```
---

     
 
all -  [ AI films ](https://www.reddit.com/r/LangChain/comments/1aun3bk/ai_films/) , 2024-02-22-0909
```
Do you guys think it will be possible to make entire films using AI? I honestly feel like Sora might just be a lightbulb
 in the text-to-video space. And when that time comes, will films enthusiasts still have the same thrill of going to cin
emas? Is it even ethical to ask people to pay for AI generated films?
```
---

     
 
MachineLearning -  [ [D] What's the standard practice for setting initialization prompts and maintaining context when swi ](https://www.reddit.com/r/MachineLearning/comments/1aq78ao/d_whats_the_standard_practice_for_setting/) , 2024-02-22-0909
```
Hi I am trying to build a modularized LLM application using Langchain where within any individual conversation the app c
an seamless switch between multiple LLMs to respond to the query, for example:

1. User: What's 1+ 1?
2. App (GPT-3.5): 
1+1 is 2
3. User: Concatenate the last name of the current president of the US with the answer from your last response
4
. App (Gemini Ultra): Biden2

I have two technical questions that I hope this subreddit can help answer:

1. What's the 
standard practice for setting the initialization prompts or background prompts? For example I want to tell this App that
 'your name is Bob', and I want this App to continuously remember it's Bob regardless how long the conversation has gott
en or any switching between LLMs. Do I set this at the beginning of the conversation or before every single response?
2.
 What's the standard practice for conversation memory management when there's switching of LLM involved within one conve
rsation? Do I store all the conversation history within a vector database and do a index search prior to any individual 
response?
```
---

     
 
MachineLearning -  [ Whats in your RAG setup? [D] ](https://www.reddit.com/r/MachineLearning/comments/1apcp2w/whats_in_your_rag_setup_d/) , 2024-02-22-0909
```
What frameworks and libraries are you using in your RAG? 

I'm most curious if  LangChain is as popular as it was?

Here
's mine at a high-level: 

*  langchain to use OpenAI for creating embeddings
* Pinecone for storing embedding
* langcha
in to load document splitters and characters splitters for chunking
* Mongo for conversations memory

&#x200B;
```
---

     
 
MachineLearning -  [ [D] What's the best current RAG setup that would work with a local LLM? ](https://www.reddit.com/r/MachineLearning/comments/1ag6bo7/d_whats_the_best_current_rag_setup_that_would/) , 2024-02-22-0909
```
I've tried things like langchain in the past (6-8 months ago) but they were cumbersome and didn't work as expected.

I  
need RAG to get data from various pdfs (long one, 150+ pages) - and i  need a setup that will allow me to add more and m
ore data sources.

I wanna run this locally, can get a 24gb video card (or 2x16gb ones) - so i can run using 33b or smal
ler models.

I  know things in the industry change every 2 weeks, so i'm hoping there's  an easy and efficient way of do
ing RAG (compared to 6 months ago)
```
---

     
 
MachineLearning -  [ [P]: Anukool: My job hunting assistant ](https://www.reddit.com/r/MachineLearning/comments/1adu3tw/p_anukool_my_job_hunting_assistant/) , 2024-02-22-0909
```
Hey Reddit, I've been applying for jobs and found that writing a cover letter for each position was tedious. I also delv
ed into LLM and Langchain, hoping to leverage them for a project to aid in my job hunting. So, I developed Anukool under
 the GPL license. While it's far from perfect, it has proven very useful to me, and I hope it benefits you as well. All 
I have to do is provide it with a pdf containing information about me such as my experience, skills, projects, etc and i
t will use this information along with job description to generate cover letter for me. Since I'm new to ML and LLM, any
 advice or feedback is greatly appreciated, and contributions are also welcome. I plan to utilize Llama-2 soon to furthe
r open-source the project.

Check out the GitHub link, and please star it if you find the project interesting: https://g
ithub.com/dakshesh14/anukool
```
---

     
 
deeplearning -  [ [D] WebVoyager: Navigating Digital Cosmos with LangGraph & Multimodal Models ](https://www.reddit.com/r/deeplearning/comments/1altlca/d_webvoyager_navigating_digital_cosmos_with/) , 2024-02-22-0909
```
Embark on a journey through the digital cosmos with WebVoyager, a groundbreaking Large Multimodal Model (LMM) web agent 
designed to navigate the vastness of the online universe. In collaboration with Langchain, WebVoyager represents a parad
igm shift in autonomous web agents, seamlessly integrating visual and textual information to complete user instructions 
end-to-end by interacting with real-world websites.

Link: [https://medium.com/@andysingal/webvoyager-navigating-digital
-cosmos-with-langgraph-multimodal-models-dace64196c2f](https://medium.com/@andysingal/webvoyager-navigating-digital-cosm
os-with-langgraph-multimodal-models-dace64196c2f)
```
---

     
 
deeplearning -  [ [D] Langchain Elevates with Step-Back Prompting using RAGatouille ](https://www.reddit.com/r/deeplearning/comments/1agtyeh/d_langchain_elevates_with_stepback_prompting/) , 2024-02-22-0909
```
In the dynamic realm of natural language processing, a revolutionary synergy has emerged between Langchain and Step-Back
 Prompting. This article delves into the transformative collaboration, exploring how Langchain’s cutting-edge platform i
ncorporates Step-Back Prompting to redefine language processing capabilities. Join us on a journey of innovation and dis
covery as we unravel the intricacies of this powerful integration. As we explore the uncharted territories of language m
odels, Step-Back Prompting stands as a beacon of progress, promising a journey of nuanced understanding and elevated per
formance in the world of Large Language Models. Welcome to the future of language processing, where inspiration and inno
vation converge in a symphony of words and ideas.

Link: https://medium.com/ai-advances/langchain-elevates-with-step-bac
k-prompting-using-ragatouille-b433e6f200ea
```
---

     
 
deeplearning -  [ Become an AI Developer (Free 9 Part Series) ](https://www.reddit.com/r/deeplearning/comments/1afgp2r/become_an_ai_developer_free_9_part_series/) , 2024-02-22-0909
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

     
 
deeplearning -  [ DSPy Explained! ](https://www.reddit.com/r/deeplearning/comments/1adypks/dspy_explained/) , 2024-02-22-0909
```
DSPy is the next big advancement for AI and building applications with LLMs!

Pioneered by frameworks such as LangChain 
and LlamaIndex, we can build much more powerful systems by chaining together LLM calls! This means that the output of on
e call to an LLM is the input to the next, and so on. We can think of chains as programs, with each LLM call analogous t
o a function that takes text as input and produces text as output.

DSPy offers a new programming model, inspired by PyT
orch, that gives you a massive amount of control over these LLM programs. Further the Signature abstraction wraps prompt
s and structured input / outputs to clean up LLM program codebases.

DSPy then pairs the syntax with a super novel compi
ler that jointly optimizes the instructions for each component of an LLM program, as well as sourcing examples of the ta
sk.

Here is my review of the ideas in DSPy, covering the core concepts and walking through the introduction notebooks s
howing how to compile a simple retrieve-then-read RAG program, as well as a more advanced Multi-Hop RAG program where yo
u have 2 LLM components to be optimized with the DSPy compiler! I hope you find it useful!

https://www.youtube.com/watc
h?v=41EfOY0Ldkc
```
---

     
