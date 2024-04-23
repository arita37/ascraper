 
all -  [ Vector database - separate indexes/tables? ](https://www.reddit.com/r/LangChain/comments/1capafo/vector_database_separate_indexestables/) , 2024-04-23-0910
```
Lets say I'm using Pinecone as a vector database and my content is courses, should I organize my indexes by separating m
odules, videos, audio, titles, etc., into different indexes/tables, or should I put them all into one index with metadat
a even though that index/table would get quite large over time?
```
---

     
 
all -  [ Supervised Clustering using RAG ](https://www.reddit.com/r/LangChain/comments/1calwq1/supervised_clustering_using_rag/) , 2024-04-23-0910
```
I have predefined clusters of roughly ~800, each cluster has been built based on items which could be grouped together. 
My task is to put the unclassified items in the relevant clusters. 

Each Cluster takes a row of CSV file with the follo
wing attributes : cluster id, cluster label and the items in the cluster. I built the Vector Database using the CSV file
 and ran the unclassified items through it using the map-rerank query method. In the prompt, I asked to respond me just 
the cluster id if there is a relevant cluster otherwise give -1. I did some fine-tuning of the prompt to get just the cl
uster id but it seems like I always run into some kind of issue because LLM (using GPT4) doesn't respond the cluster id 
in the right format. Is there a way to get the index of the classified vector database row which would inturn be the cor
responding row of the cluster CSV file?
```
---

     
 
all -  [ [D] Self-optimizing deterministic LLM memory using dspy, neo4j and vector databases. Need your input ](https://www.reddit.com/r/MachineLearning/comments/1cakjaf/d_selfoptimizing_deterministic_llm_memory_using/) , 2024-04-23-0910
```
Hey there, Redditors!

I'm back with the latest installment on creating deterministic LLM memory.

If you've been follow
ing along, you know I'm on a mission to move beyond the '[thin OpenAI wrapper](https://topoteretes.github.io/cognee/blog
/2023/10/05/going-beyond-langchain--weaviate-and-towards-a-production-ready-modern-data-platform/)' trend and tackle the
 challenges of building robust LLM memory.

  
That's why we built cognee, a python library to process documents and bui
ld knowledge graphs on top of them.

After a few weeks of work, we integrated DSPy and extended cognee.

Here is brief o
verview of the logic: 

[Architecture overview](https://preview.redd.it/fcs3lifx53wc1.png?width=1380&format=png&auto=web
p&s=9316cba52147a5b764565b8438f3f143d8e7ac84)

We aim to understand:

1. Have you tried building knowledge graphs with o
ther tools before?

2. If so, what were the biggest obstacles?

3. How would you approach semantic linking of documents 
without knowledge graphs?

*Remember to give this post an upvote if you found it insightful!*  
*And also star our* [Git
hub repo](https://github.com/topoteretes/cognee)
```
---

     
 
all -  [ Send multiple parameters through prompt template ](https://www.reddit.com/r/LangChain/comments/1caja59/send_multiple_parameters_through_prompt_template/) , 2024-04-23-0910
```
Hi All,
How can I send multiple parameters through my prompt, for example,

```
from langchain_core.prompts import Promp
tTemplate

template = '''Use the following pieces of context to answer the question at the end.
If you don't know the an
swer, just say that you don't know, don't try to make up an answer.
Use three sentences maximum and keep the answer as c
oncise as possible.
Always say 'thanks for asking!' at the end of the answer.

{context}

Question: {question}

Helpful 
Answer:'''
custom_rag_prompt = PromptTemplate.from_template(template)

rag_chain = (
    {'context': retriever | format_
docs, 'question': RunnablePassthrough()}
    | custom_rag_prompt
    | llm
    | StrOutputParser()
)

rag_chain.invoke('
What is Task Decomposition')
```


How to add more more parameters?
```
---

     
 
all -  [ Pipeline for RAG and not RAG based on question and retrieved docs ](https://www.reddit.com/r/LangChain/comments/1caic8s/pipeline_for_rag_and_not_rag_based_on_question/) , 2024-04-23-0910
```
Hi there!

I want to implement such thing like use RAG prompt if user question match RAG semantic and regular not RAG pr
ompt, if it doesn’t match.

I’ve came in thoughts with three approaches: 
1. Before retrieval, use semantic router on us
er question and decide which prompt/chain to use based on this

2. After retrieval, when docs count is 0 or their releva
ncy score < some threshold use simple regular prompt 

3. After I’ve got LLM answer I evaluate it and based on evaluatio
n metrics if they are poor, I call LLM again with regular prompt

What do you think about these?
```
---

     
 
all -  [ What’s the best chat with your data app out there? ](https://www.reddit.com/r/LangChain/comments/1cagxf4/whats_the_best_chat_with_your_data_app_out_there/) , 2024-04-23-0910
```
I’m looking for an app/saas where I could upload data such as pdfs, text files maybe even links and be able to summarize
, extract structured data and do general research based on the data provided.

Essentially a RAG as a service. RaaS? 

U
pdate: To be clear, i’m looking for a finished and ready app I can use. I’m not trying to implement it myself. 
```
---

     
 
all -  [ How I made an entire Team with CrewAI to manage my YouTube channel ](https://www.reddit.com/r/ArtificialInteligence/comments/1cagrqi/how_i_made_an_entire_team_with_crewai_to_manage/) , 2024-04-23-0910
```
Hi folks,

I wanted to share with you a cool project I recently undertook that leverages the power of AI to help manage 
my YouTube channel! 

The idea was to use [CrewAI](https://www.crewai.com/) to automate tasks like competitor YouTube ch
annel analysis and identify trending topics. This way, I could gauge these topics against my own content ideas to see if
 there is general interest in a given topic. 

The AI Crew was designed to crawl the web (Google) and call APIs like the
 YouTube API, Reddit API, and use Google Trends to determine how likely a given topic is to generate engagement.

For th
is, I created the following AI Assistants (or agents in CrewAI lingo):

* A competitor analysis agent
* A Content Creato
r (to generate ideas from research)
* A Marketing advisor, to generate catchy titles and tags
* An Analytics consultant 
to measure the performance of the video

I used a pretty straightforward setup that relied on the usual suspects:

* Ana
conda
* Python 3.11
* A few modules like pytrend, praw, serper, and langchain

I tested it with models like GPT-4, GPT-4
-Turbo, and a few local models like nous-hermes 2, mistral, and codellama, among others. 

The results from GPT-4-Turbo 
were AMAZING, and I'm sure I can make them better by fine tuning the data going into the model, but they were not really
 that great with local AI, which was quite expected given the imense number of tokens. However I was quite positively su
rprised by the performance of Nous Hermes 2 - 13b. Not only did it actually run, but it used the tools I custom build fo
r it! Quite impressive really

The video is available below:

[https://youtu.be/5JoVeYcxgpU?si=cxFwHO1x\_zCghMYB](https:
//youtu.be/5JoVeYcxgpU?si=cxFwHO1x_zCghMYB)

You are more than welcome to try out the code for yourselves: [https://gith
ub.com/fmiguelmmartins/crewaiyoutube](https://github.com/fmiguelmmartins/crewaiyoutube)

And here is an article on Mediu
m with the step-by-step process (don't worry, I have a free account):

[https://medium.com/@fmiguelmmartins/create-an-ai
-team-to-manage-your-youtube-channel-5dc1e6c9b31b](https://medium.com/@fmiguelmmartins/create-an-ai-team-to-manage-your-
youtube-channel-5dc1e6c9b31b)

Hope you guys enjoy it, and if you are kind enough, please leave me some feedback so I ca
n improve over time!

Thank you!

Filipe
```
---

     
 
all -  [ Can one safely use pydantic v2 in Langchain now? ](https://www.reddit.com/r/LangChain/comments/1cagjg0/can_one_safely_use_pydantic_v2_in_langchain_now/) , 2024-04-23-0910
```
I had read earlier that it was safer to use \`pydantic\_v1\` with langchain. But now that I'm trying to actually do some
thing more with what comes out of langchain, it's a big pain to use v1. Can I switch to using current pydantic instead?
```
---

     
 
all -  [ 466 PRs awaiting review 😳 ](https://i.redd.it/watfccf122wc1.jpeg) , 2024-04-23-0910
```

```
---

     
 
all -  [ Building tools that utilize async ](https://www.reddit.com/r/LangChain/comments/1cae5ta/building_tools_that_utilize_async/) , 2024-04-23-0910
```
I am currently trying to build a few tools and have run into not being able to use async functions. Does Langchain have 
an answer for this?

I get this error 'NotImplementedError: Tool does not support sync' when calling the tool with the a
gent. I have tried a few different ways classifying the tool to no avail.

&#x200B;
```
---

     
 
all -  [ AI, Multiagent, Agentic, Python, Vision, Web scraping help needed. ](https://www.reddit.com/r/LangChain/comments/1caamav/ai_multiagent_agentic_python_vision_web_scraping/) , 2024-04-23-0910
```
I want to identify the exact property address for online properties eg on Rightmove. 

Currently online UK property URL 
listings provide the Road Name and some further info but NOT the house number or the full postcode.

As a human you can 
find the house number by using Google Streetview and searching for a property match by using the front image of the hous
e.

I suspect automating this process will require a research team of AI Agents using visual AI but open to other soluti
ons.

Please note, there are some other ways to identify the property number (they are not always possible). This projec
t is specifically about automating the process of finding a specific property on Google Streetview.

See this property a
s an example: https://www.rightmove.co.uk/properties/144815291 
Using Streetview, its number 46. I can share the manual 
process I use.

Any help or advice would be greatly appreciated. If you know someone who could do this work, please let 
me know.

Thank you.

```
---

     
 
all -  [ Feedback wanted on my project (Salary Negotiation Coach) ](https://www.reddit.com/r/LangChain/comments/1ca7tof/feedback_wanted_on_my_project_salary_negotiation/) , 2024-04-23-0910
```
So I've built a tool that helps you negotiate a higher salary. The idea is that it helps you prepare for an annual revie
w or handling the offer stage when you get a new job.

I'd love some feedback on it. Getting the combination of text ans
wers (through RAG) plus video content is proving difficult to get right.

You can play with it here:  
[https://ignitus.
app](https://ignitus.app/)
```
---

     
 
all -  [ Multi-Agent Code Reviewer using LangGraph ](https://www.reddit.com/r/LangChain/comments/1ca6jis/multiagent_code_reviewer_using_langgraph/) , 2024-04-23-0910
```
This tutorial explains how can Multi-Agent Orchestration be used to build an automatic code review system where a Coder 
and Reviewer go back & forth improving the code quality until all issues are resolved automatically: 
https://youtu.be/p
dnT3yLk70c?si=TUrV50BlNu7UStoI
```
---

     
 
all -  [ How to avoid increasing the size of my prompt? ](https://www.reddit.com/r/PromptEngineering/comments/1ca674r/how_to_avoid_increasing_the_size_of_my_prompt/) , 2024-04-23-0910
```
Hi, a question for people experienced with prompt engineering:  
  
Let's suppose I am building an API for a user to con
sume and want to specify some examples. Do I have to specify it in each payload?  
  
I am worried that it would just in
crease the input payload size and drive up costs.   
  
What's a good way to get around this? (setup is on python+langch
ain)


```
---

     
 
all -  [ Seeking Advice: Solving Data Challenges with Large Language Models (LLMs) ](https://www.reddit.com/r/deeplearning/comments/1ca4nc1/seeking_advice_solving_data_challenges_with_large/) , 2024-04-23-0910
```
Hi all

I am presented with a problem that I need to solve using LLM to get the right data from text that has only \~20%
 structure to it. Here's a sample data

XXXXX

AA          BB

CCCC:  (optional DDDD)

C1......(A1) (B1)

C2......(A2) (
B2)

C3.....(A3) (B3)

I am required to anwer with either of these results from A1/B1 till A3/B3 pairs but in order to d
o that I need to go back and ask the user which one of the options C1 to C3 applies to him?

The above is not the most c
omplex structure, it increases in complexity from here so a lot of chatting with user is required to get to the right da
ta that will always exist in the chunk like above.

In the most simplist case the data structure will look like below

X
XXXX

AA          BB

CCCC: ......(A1) (B1)



How would you build a system like this? I am looking at multi-agent syste
ms with Langchain, what about prompt chaining?
```
---

     
 
all -  [ Is there a way to hook into the steps that LangSmith does? ](https://www.reddit.com/r/LangChain/comments/1c9y3rs/is_there_a_way_to_hook_into_the_steps_that/) , 2024-04-23-0910
```
I use LangGraph I want to be able to show my users things like the intermediate steps, the token usage etc.

I want to d
o this by creating or updating objects in my DB when relevant. What I want to achieve is something pretty similar to wha
t LangSmith looks like. Lets say a simplified version with less data.

I can probably find where I could make such DB ca
lls in the general flow, but if I can just hook into when LangSmith is doing that anyway, it'd be easier/more robust. 
```
---

     
 
all -  [ Is the AI Workforce or Companies More Distributed Than Those in Other Tech Sectors? ](https://i.redd.it/gnbuw6yzjxvc1.jpeg) , 2024-04-23-0910
```
I saw a map showing where AI startups raised money or were established over the last 12 months. This looks right. There 
is also detailed data in the thread. It seems geographically widespread, although SF still accounts for one-third of the
 funding and one-fifth of the companies. Do others here have the same impression?

Source: https://x.com/wanguws/status/
1782070536769515865?s=46”
```
---

     
 
all -  [ How can I ask for user confirmation before completing a chain? ](https://www.reddit.com/r/LangChain/comments/1c9lvxf/how_can_i_ask_for_user_confirmation_before/) , 2024-04-23-0910
```
I'm using LangChain to execute tasks that need a user's confirmation before they are done. But LangChain isn't happy unt
il it actually executes that task. Can I inject a 'pause here... wait for user confirmation before you continue' in the 
flow?
```
---

     
 
all -  [ Can I access fine-tuned models on LangChain from HuggingFace? ](https://www.reddit.com/r/LangChain/comments/1c9k9u2/can_i_access_finetuned_models_on_langchain_from/) , 2024-04-23-0910
```
If I fine-tune Llama2 on my custom data on Google Colab and push it to HuggingFace hub, will I be able to access it with
 LangChain using the HuggingFace API and use it in my RAG pipeline?

Does anyone know how to do it?

Edit: I am using Lo
RA for fine-tuning.

Edit: If HuggingFace isn't an option, are there other ways to use custom fine-tuned models in my La
ngChain RAG pipeline?
```
---

     
 
all -  [ How to get the SQL query generated by the model? ](https://www.reddit.com/r/LangChain/comments/1c9k5ai/how_to_get_the_sql_query_generated_by_the_model/) , 2024-04-23-0910
```
Hello ^^. how can I get the vars['query'] because I want to show it to the user as a separate var (optionally)
```python


from langchain_community.utilities import SQLDatabase
from langchain_groq import ChatGroq
from dotenv import load_dote
nv

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from
 langchain_core.runnables import RunnablePassthrough

load_dotenv()

db_file = 'chinook.db'
db = SQLDatabase.from_uri(f'
sqlite:///{db_file}')

# mixtral-8x7b-32768
# llama3-8b-8192
llm = ChatGroq(model='mixtral-8x7b-32768', temperature=0)


def get_schema(_):
    schemas = ''
    for table in db.get_usable_table_names():
        schemas += db.get_table_info([
table]).split('/*')[0].strip()

    return schemas

def get_sql_query_prompt_pipeline(_):
    '''Generate a data process
ing pipeline for prompting users to write SQL queries based on a given database schema.'''

    template ='''
    You ar
e a data analyst in a company who is interacting with a user that is asking you questions about the company's database.

    Based on the table schemas below, write a SQL query that would answer the user's question.
    
    <SCHEMA>{schema}
</SCHEMA>

    Take the conversation history into account: {chat_history}

    Use the following couple of examples as r
eference for the ideal answer style:
    \nExample 1:
    Question: How many employees are there
    SQL Query: SELECT C
OUNT(*) FROM Employee;
    \nExample 2:
    Question: Find the total number of tracks in each genre
    SQL Query: SELEC
T g.Name AS Genre, COUNT(t.TrackId) AS NumberOfTracks FROM Track t JOIN Genre g ON t.GenreId = g.GenreId GROUP BY g.Name
;

    Return only the SQL query and nothing else. Do not wrap the SQL query in any other text, not even backticks. Do n
ot use any special characters like \\.
    Do not use any special tokens either in your answer.
    
    Now, it is your
 turn:
    
    Question: {question}
    SQL Query:
    '''

    prompt = ChatPromptTemplate.from_template(template)




    return (
        RunnablePassthrough.assign(schema=get_schema)
        | prompt
        | llm
        | StrOutputPar
ser()
    )



def get_response(user_query, db, chat_history):
  sql_chain = get_sql_query_prompt_pipeline(db)
  
  temp
late = '''
    You are a data analyst in a company who is interacting with a user that is asking you questions about the
 company's database.
    Based on the table schema below, conversation history, sql query and user question, write a nat
ural language response.
    <SCHEMA>{schema}</SCHEMA>

    Conversation History: {chat_history}

    SQL Query: <SQL>{qu
ery}</SQL>
    User question: {question}
    AI Response: {response}'''
  
  prompt = ChatPromptTemplate.from_template(t
emplate)

  chain = (
    RunnablePassthrough.assign(query=sql_chain).assign(
      schema=lambda _: get_schema(_),
    
  response=lambda vars: db.run(vars['query']),
    )
    | prompt
    | llm
    | StrOutputParser()
  )
  
  result = ch
ain.invoke({
    'question': user_query,
    'chat_history': chat_history,
  })
  
  return result

response = get_respo
nse('Give me the top 5 selling artists', db, [])
print(response)


```
```
---

     
 
all -  [ Python code generation  ](https://www.reddit.com/r/LangChain/comments/1c9fksj/python_code_generation/) , 2024-04-23-0910
```
I new to the Generative AI. I am implementing python code generation task using LLAM 2 7B and iamtarun/python\_code\_ins
tructions\_18k\_alpaca as dataset. I am using google collab for it. I have split my dataset into 70-20-10:train-test-val
 split. train: Dataset : features: \['instruction', 'input', 'output', 'prompt'\], num\_rows: 18612 . I have to choose e
valuation metric for this test and test my model on test dataset using evaluation metric which I choose.

1. I want to k
now which evaluation metric I can use here for evaluation for my task ?
2. I have to test the model on test set. How can
 I test my model on test set ?
3. After this, I have AWS API KEY for another large model ( LLAMA 2 70B), I need to make 
synthetic dataset which must be 3 times of training dataset. How can I perform this synthetic dataset generation ? What 
instructions or prompt I should pass to generate synthetic dataset ?

Guide me, if there is any resources for this kind 
of tasks please do share.
```
---

     
 
all -  [ Table of content issue with Retrieval in pdfs with chroma ](https://www.reddit.com/r/LangChain/comments/1c9eziy/table_of_content_issue_with_retrieval_in_pdfs/) , 2024-04-23-0910
```
Basically whenever we retrive say 5 chunks from an indexed pdf which has TOC(about 2 pages) from a pdf of approx 30-50 p
ages, 2 of the retrived chunks are always table of contents. Has anyone faced this issue? How did you go about resolving
 it?

Also not sure exactly why this happens. Any leads would be helpful.

Exact usecase: The pdfs are tech specs/techni
cal requirement documentations of features an engineering team is building. My prompts are approx 200-400 tokens. 

The 
prompts are security specfic(for eg: analysing how the pdf talks about authentication and diff types of authentication).
 
```
---

     
 
all -  [ Share the Coolest Out of The Box LLM Applications That Made You Say 'Wow that was smart' ](https://www.reddit.com/r/deeplearning/comments/1c9e6dj/share_the_coolest_out_of_the_box_llm_applications/) , 2024-04-23-0910
```
Hi, I'm looking at some LLM applications today but apart from guys doing big rags with langchain I don't see too many us
es that are out of the box or that make me say 'wow that was smart to use an LLM here'. Have you seen any cool stuff usi
ng LLMs recently that made you say 'wow, that was smart'?
```
---

     
 
all -  [ Local RAG with LLama3 ](https://www.reddit.com/r/LargeLanguageModels/comments/1c9c4am/local_rag_with_llama3/) , 2024-04-23-0910
```
 

Hi,

Made a short video on building a RAG pipeline using Llama 3 with langchain.

Thought people might find it useful
 for testing purposes

Hope it helps.

[https://youtu.be/2B263c-nB\_8](https://youtu.be/2B263c-nB_8)
```
---

     
 
all -  [ Local RAG with LLama3 ](https://www.reddit.com/r/LanguageTechnology/comments/1c9c3p2/local_rag_with_llama3/) , 2024-04-23-0910
```
Hi,  
Made a short video on building a RAG pipeline using Llama 3 with langchain.  
Thought people might find it useful 
for testing purposes  
Hope it helps.  
https://youtu.be/2B263c-nB\_8
```
---

     
 
all -  [ Local RAG with LLama3 ](https://www.reddit.com/r/learnmachinelearning/comments/1c9c3gg/local_rag_with_llama3/) , 2024-04-23-0910
```
 Hi,

Made a short video on building a RAG pipeline using Llama 3 with langchain.

Thought people might find it useful f
or testing purposes

Hope it helps.

[https://youtu.be/2B263c-nB\_8](https://youtu.be/2B263c-nB_8)

&#x200B;
```
---

     
 
all -  [ Why to use Multi-Agent Orchestration explained  ](https://www.reddit.com/r/LangChain/comments/1c99eok/why_to_use_multiagent_orchestration_explained/) , 2024-04-23-0910
```
Checkout this short explanation around the importance of Multi-Agent Orchestration and when and why should you use it in
stead of a single prompt LLM hit https://youtu.be/GZGUvM6JfLY?si=sqS7PBEvsX0Qe6gF
```
---

     
 
all -  [ Automating Knowledge Extraction from Domain-specific Guidelines Using RAG and Agents ](https://www.reddit.com/r/LangChain/comments/1c90dl7/automating_knowledge_extraction_from/) , 2024-04-23-0910
```
Hello everyone,

I'm working on a project that involves applying documented agricultural guidelines to live data. Specif
ically, these guidelines dictate the process for mechanical weed control in crops like sunflowers, including specifics s
uch as seed depth, precipitation levels, and timing for mechanical controls relative to sowing dates.

For instance, acc
ording to the guidelines:

* The seed should be sown below a depth of 5 cm.
* The cumulative precipitation should be bel
ow 5mm/m2.
* If the time difference between the presowing preparation date and the sowing date exceeds 2 days, two mecha
nical controls should be performed (one 3 days after presowing, and the second 7-8 days after presowing). If it's less t
han or equal to 2 days, only one control is recommended.

Currently, I am manually coding these rules based on my readin
g of the guidelines. However, I'm interested in automating this process. I am considering using Retrieval-Augmented Gene
ration (RAG) and agents to extract these rules automatically from the documents and apply them to incoming weather data.


**Questions:**

1. Has anyone here worked on automatically extracting logic from structured documents using RAG or sim
ilar technologies?
2. Are there specific ways to format or write the documents that enhance the efficiency of knowledge 
extraction?
3. Can agents be effectively combined with RAG to monitor and apply these rules based on live weather data?


Any insights or experiences with similar challenges would be greatly appreciated!

Thank you!
```
---

     
 
all -  [ Llama3 function agent ](https://www.reddit.com/r/LocalLLaMA/comments/1c8yl2n/llama3_function_agent/) , 2024-04-23-0910
```
Now that Llama3 is out, dis anybody try using it as an agent with LangChain to run functions? 

All examples for LangGra
ph I find are with OpenAI, it would be great to get a Llama version too for local offline development!

```
---

     
 
all -  [ How to optimise for 'reverse' RAG? ](https://www.reddit.com/r/LangChain/comments/1c8x0em/how_to_optimise_for_reverse_rag/) , 2024-04-23-0910
```
So the problem I'm working on is the prompts are fixed(not one liner QnA but half a page types) and the input pdf can ch
ange.

I'm calling it 'reverse' because most of the examples or discussions I see talk about thr usecase where prompts a
re variable but docs might be fixed.

But in my case, when prompts are fixed, is there some specific optimizations I can
 do for better results? 
Have you tried something that's not the norm for normal qna systems but works well for these Ca
ses? Would love some insight.

Also can anyone share how they setup evals or a good source to learn from, for systems wh
ere the prompts are complex and the outputs are not few lines but complex json outputs. It would be really helpful.

TIA


```
---

     
 
all -  [ Need a tech partner/freelance with LLM experience  ](https://www.reddit.com/r/developersIndia/comments/1c8v6gj/need_a_tech_partnerfreelance_with_llm_experience/) , 2024-04-23-0910
```
Hi

I have a working prototype of a chatbot that's validated from the industry. I need someone's help to integrate a few
 frameworks with it to make it more robust

Ideally anyone who's been experimenting with langchain, openai, chainlit, ze
p ai. 

And preferably from NCR. Open to collaboration or a fixed pay to help me move the product ahead. 


Please DM :)

```
---

     
 
all -  [ Is MongoDB $graphlookup suitable for graph RAG in operational workloads? ](https://www.reddit.com/r/LangChain/comments/1c8rj8d/is_mongodb_graphlookup_suitable_for_graph_rag_in/) , 2024-04-23-0910
```
 I'm exploring hybrid RAG with vector and graph. Is MongoDB's $graphlookup suitable for RAG in operational workloads (as
 in operational/OLTP vs analytical OLAP workloads)? Why or why not? 
```
---

     
 
all -  [ Having difficulties on reading CSV files with OpenAI ](https://www.reddit.com/r/LangChain/comments/1c8n7g4/having_difficulties_on_reading_csv_files_with/) , 2024-04-23-0910
```
I am currently writing my first app with LLMs, and I want it to be able to read through a CSV file. The problem is that 
it is very unreliable, sometimes it is right, sometimes it is wrong.

My CSV is a table where you choose a row and a col
umn and read the value at the intersection. For example it looks like this (My CSV file is much larger than this, i just
 used this for brevity)

    Bank Name,Bank1,Bank2,Bank3,Bank4
    Is Live,Yes,Yes,Yes,No

When I asked: 'Is bank 4 alre
ady live', it answers 'Yes'. But if I asked 'Are Bank1, Bank2, Bank3 and Bank4 already live?', then answer is 'Bank1, Ba
nk2, Bank3 is live, but not Bank4'

The prompt that I used is like below

    You are going to be given a two-dimensiona
l table where you choose a row and a column and read 
        the value at the intersection but in a csv format. You are
 an experienced researcher, 
        expert at interpreting and answering questions based on provided sources.
        U
sing the provided context, answer the user's question to the best of your ability using only the resources provided. 
  
      Be straight forward on answering questions. Concise, although not missing any important information. 
        I do
n't need to understand how you would get the data from, unless I specifically asked for it.
    
        <context>
    

        {context}
    
        </context>
    
        Added information for the context, if you find that the cell is e
mpty, it means that the information is not available.
    
        Now answer the question below using the above context
:
    
        {question}

Where the context is the contents of the CSV file. My question is, is there a better way to d
o this? I am currently using OpenAI model gpt-3.5-turbo-1106.
```
---

     
 
all -  [ Integrating LLM with API Services for Dynamic JSON Handling – Need Help! ](https://www.reddit.com/r/LangChain/comments/1c8mew6/integrating_llm_with_api_services_for_dynamic/) , 2024-04-23-0910
```
Hey everyone! Long-time lurker, a first-time poster here. I'm facing a challenge and could use your collective wisdom. I
’m working on a project where I need to integrate a large language model (LLM) with an API service. The goal is to have 
the LLM possess the knowledge base necessary to construct JSON requests dynamically.

Here’s what I need to accomplish i
n two steps:

1. **Retrieve Identifiers:** The first API call needs to be a GET request to fetch identifiers.
2. **Use I
dentifiers:** The second API call is a POST request where these identifiers are essential.

We already have a consistent
 JSON structure for our POST requests, but we’re stuck on dynamically generating and retrieving identifiers through the 
GET request. Does anyone have experience or suggestions on how to set up an LLM to handle these two steps effectively? A
ny advice on tools, frameworks, or code snippets would be greatly appreciated!

Thanks in advance for your help!

  
**L
ater edit:**  I have a chat assistant that it is connected with Gmail and Other services. 

**Example 1:** The user type
 a command like: 'Find me the last email from [john@doe.com]() and reply to him by telling him \[whatever\].'**:**

1. I
nitial Action **(GET Request)**: The assistant first performs a search to locate the most recent email from '[john@doe.c
om]()'. It retrieves the email along with its unique identifier.
2. Follow-up Action **(POST Request)**: Using the ident
ifier obtained from the first action, the assistant then crafts and sends a reply to John Doe with the user-specified me
ssage.

**Example 2**: The user type a command like: 'Create a new block in Notion under Meetings Page with \[whatever c
ontent\]' 

1. Locating the Page **(GET Request)**: The chat assistant first performs a search to find the unique identi
fier (ID) of the 'Meetings Page' in Notion.
2. Creating the Block **(POST Request)**: Once the page ID is retrieved, the
 assistant uses this ID in a POST request to create a new block on the Meetings Page with the content provided by the us
er.


```
---

     
 
all -  [ Curated list of open source tools to test and improve the accuracy of your RAG/LLM based app ](https://www.reddit.com/r/LangChain/comments/1c87gn2/curated_list_of_open_source_tools_to_test_and/) , 2024-04-23-0910
```
Hey everyone,

  
What are some of the tools you are using for testing and improving your applications? I have been cura
ting/following a few of these. But, wanted to learn what your general experience has been? and what challenges you all a
re facing.

- [https://github.com/explodinggradients/ragas](https://github.com/explodinggradients/ragas)  
- [https://gi
thub.com/promptfoo/promptfoo](https://github.com/promptfoo/promptfoo)  
- [https://github.com/braintrustdata/autoevals](
https://github.com/braintrustdata/autoevals)  
- [https://github.com/stanfordnlp/dspy](https://github.com/stanfordnlp/ds
py)  
- [https://github.com/jxnl/instructor/](https://github.com/jxnl/instructor/)  
- [https://github.com/guidance-ai/g
uidance](https://github.com/guidance-ai/guidance)

Separately, I am also building one which is more focused towards trac
ing and evaluations  
- [https://github.com/Scale3-Labs/langtrace](https://github.com/Scale3-Labs/langtrace)
```
---

     
 
all -  [ I need some guidance on my approach ](https://www.reddit.com/r/Langchaindev/comments/1c85g5f/i_need_some_guidance_on_my_approach/) , 2024-04-23-0910
```
I'm working on a tool that has a giant data entry that consist in a json describing a structure for a file and this is m
y first attemp of using Langchain. This is what I'm doing:

First, I fetch the json file and get the value I need. It st
ill consists in a few thousand lines.

    data = requests.get(...)
    raw_data = str(data)
    splitter = CharacterTex
tSplitter(chunk_size=500, chunk_overlap=0)
    documentation = splitter.split_text(text=raw_data)
    vector = Chroma.fr
om_texts(documentation, embeddings)
    return vectorraw_data = str(data)
    splitter = CharacterTextSplitter(chunk_siz
e=500, chunk_overlap=0)
    documentation = splitter.split_text(text=raw_data)
    vector = Chroma.from_texts(documentat
ion, embeddings)
    return vector

  
Then, I build my prompt:

    vector = <the returned vector>
    llm = ChatOpenAI
(api_key='...')
    template = '''You are a system that generates UI components following the sctructure described in th
is context {context}, from an user request. Answer using a json object
                Use texts in spanish for the requ
ired components. 
                '''
    user_request = '{input}'
    prompt = ChatPromptTemplate.from_messages([
     
   ('system', template),
        ('human', user_request)
    ])
    
    document_chain = create_stuff_documents_chain(l
lm, prompt)
    
    retrival = vector.as_retriever()
    
    retrival_chain = create_retrieval_chain(retrival, documen
t_chain)
    
    result = retrival_chain.invoke(
        {
            'input': 'I need to create three buttons for my 
app'
        }
    )
    
    return str(result)

What would be the best approach for archiving my purpouse of giving th
e required context to the llm without exceding the token limit? Maybe I should not put the context in the prompt templat
e, but I don't have other alternative in mind.
```
---

     
 
all -  [ Allowed comparators for different vector stores? ](https://www.reddit.com/r/LangChain/comments/1c84lph/allowed_comparators_for_different_vector_stores/) , 2024-04-23-0910
```
I am looking for a good vector store for self-querying in LangChain. I want to be able to query, “find me a movie with D
iCaprio in it” and it should be able to find Leonardo DiCaprio in the metadata.

Chroma doesn’t support “contain”, what 
would be other DB options that can support this while also do the vector similarity search? LangChain documentation does
n’t describe the “allowed_comparators” attribute in their self-querying vector stores info.
```
---

     
 
all -  [ Question about you guys ](https://www.reddit.com/r/LangChain/comments/1c8370g/question_about_you_guys/) , 2024-04-23-0910
```
Hey everybody. Without going too much into detail I would be super interested what you guys are using this technology fo
r. We hear a lot about technicalities here but I'm really wondering how much you are using these technologies in your li
fe and in your work. Would be super interesting to know
```
---

     
 
all -  [ AgentExecutor VS model.bind_tools() in langgraph ](https://www.reddit.com/r/LangChain/comments/1c82vk3/agentexecutor_vs_modelbind_tools_in_langgraph/) , 2024-04-23-0910
```
Guys, with the latest updates, can someone please explain to me the difference between invoking AgentExecutor having use
d 'create\_tool\_calling\_agent' method as opposed to binding tools to the model and invoking it? Especially in the cont
ext of langgraph. I see so many tutorials on langgraph and it is always 'model.bind\_tools()', only a few tutorials use 
AgentExecutor within langgrpah. Do I even need to use it within a langgraph? What would be the benefit/difference?
```
---

     
 
all -  [ Is it true that it's slower to use Langchain than to call the model API's directly? ](https://www.reddit.com/r/LangChain/comments/1c82clj/is_it_true_that_its_slower_to_use_langchain_than/) , 2024-04-23-0910
```
I have heard from many people that Langchain is good for prototyping but not for production, is it because it's slower t
han using each LLM's APIs directly? I did some testing comparing the response speed from calling OpenAI directly versus 
calling it via Langchain, and Langchain consistently generates output 10% - 30% slower, not sure if it's my local proble
m or if it's a universal observation. 
```
---

     
 
all -  [ Burr: an OS framework for building and debugging agentic AI apps faster ](https://www.reddit.com/r/AI_Agents/comments/1c81b63/burr_an_os_framework_for_building_and_debugging/) , 2024-04-23-0910
```
[https://github.com/dagworks-inc/burr](https://github.com/dagworks-inc/burr)

**TL;DR** We created Burr to make it easie
r to build and debug AI applications that carry state/make complex decisions. AI agents are a very natural application. 
It is similar in concept to Langgraph, and works with any framework you want (Langchain, etc...). It comes with OS telem
etry. We're looking for users, contributors, and feedback.

**The problem(s):** A lot of tools in the LLM space (DSPY, s
uperagents, etc...) end up burying what you actually want to see behind a layer of complexity and prompt manipulation. W
hile making applications that make decisions naturally requires complexity, we wanted to make it easier to logically mod
el, view telemetry, manage state, etc... while not imposing any restrictions on what you can do or how to interact with 
LLM APIs.

**We built Burr** to solve these problems. With Burr, you represent your application as a state machine of py
thon functions/objects and specify transitions/state manipulation between them. We designed it with the following capabi
lities in mind:

1. Manage application memory: Burr's state abstraction allows you to prune memory/feed it to your LLM (
in whatever way you want)
2. Persist/reload state: Burr allows you to load from any point in an application's run so you
 can debug/restart from failure
3. Monitor application decisions: Burr comes with a telemetry UI that you can use to deb
ug your app in real-time
4. Integrate with your favorite tooling: Burr is just stitching together python primitives -- c
lasses + functions, so you can write whatever you want. Use langchain and dive into the OpenAI/other APIs when you need.

5. Gather eval data: Burr has logging capabilities to ensure you capture data for fine-tuning/eval

It is meant to be a
 lightweight python library (zero dependencies), with a host of plugins. You can get started by running: pip install 'bu
rr\[start\]' && burr  
 \-- this will start the telemetry server with a few demos (click on *demos* to play with a chatb
ot + watch telemetry at the same time).

Then, check out the following resources:

1. [Burr's documentation/getting star
ted](https://burr.dagworks.io/getting_started/)
2. [Multi-agent-collaboration example using LCEL](https://github.com/DAG
Works-Inc/burr/tree/main/examples/multi-agent-collaboration/lcel)
3. [Fairly complex control-flow example that uses AI +
 human feedback to draft an email](https://github.com/DAGWorks-Inc/burr/tree/main/examples/web-server)

**We're really e
xcited** about the initial reception and are hoping to get more feedback/OS users/contributors -- feel free to DM me or 
comment here if you have any questions, and happy developing!

PS -- the name *Burr* is a play on the project we OSed ca
lled [Hamilton](https://github.com/dagworks-inc/hamilton) that you may be familiar with. They actually work nicely toget
her!
```
---

     
 
all -  [ PGVector duplicate embedding ](https://www.reddit.com/r/LangChain/comments/1c80n7e/pgvector_duplicate_embedding/) , 2024-04-23-0910
```
how prevent duplicate embedding instance in pgvector without delete collection.

update existing once and want new one  


```
---

     
 
all -  [ Langtrace Evaluations - Breeze through with hotkeys ](https://www.reddit.com/r/LangChain/comments/1c7zp7y/langtrace_evaluations_breeze_through_with_hotkeys/) , 2024-04-23-0910
```


https://reddit.com/link/1c7zp7y/video/v8ord1suegvc1/player

We have been busy shipping updates to **Langtrace**, an **
Open Source LLM observability tool** and I am excited to show our new and improved Evaluations Dashboard. We learned fro
m our early users that improving the RAG/model accuracy and gaining confidence with deploying their LLM based apps to pr
oduction has been the number 1 priority.

To solve for this, we have built a couple of things:

**1. Create tests with d
ifferent scoring scales and automatically capture LLM requests to these tests using Langtrace's SDK.**

**2. Evaluate th
e the requests by scoring against the response provided by the LLM to measure the overall average of each test.**

Effec
tively, teams can come up with a release criteria like - 'Factual Accuracy > 99%, Response Quality > 95%, Response Bias 
> 85%, Context Recall > 90%' and measure their product's performance against this release metric with Langtrace.

Additi
onally, we also realized that the user experience is extremely important for effective and fast evaluations. As a result
, the evaluations flow is fully optimized for hot keys and as an evaluator, you can breeze through a series of evaluatio
ns with just the arrow keys, enter and backspace without having to click through a bunch of times for each request.

Fin
ally, all of this can be setup with just 2 lines of code and Langtrace's Evaluation's dashboard will start capturing the
 requests in the appropriate test automatically

Don't forget to check out Langtrace and star the repository on Github.


Github - [https://github.com/Scale3-Labs/langtrace](https://github.com/Scale3-Labs/langtrace)
```
---

     
 
all -  [ AI Automatic Agency Business Explained (a practical guide) ](https://www.reddit.com/r/EntrepreneurRideAlong/comments/1c7ttiz/ai_automatic_agency_business_explained_a/) , 2024-04-23-0910
```
The rise of artificial intelligence (AI) has opened doors for businesses to streamline their operations and gain a compe
titive edge. I have been working in the field of AI for almost 2 years now. I am building an advanced AI directory calle
d seekme. While working for Seekme, I got the chance to meet AI founders and overall explore the AI landscape. AI have r
aised some highly potential busines opportunities. One of the new AI business potential is AI Automation Agency also kno
wn as AAA. The idea is quite new and low competitive. But it is definitely something that can attract eyes of small to m
id tier businesses. Here are the basic concept of the AI Automation Agency (AAA) model, an approach to implementing cust
om AI solutions for businesses. (I am assuming you already know what LLM, OCR, RAG etc means)

**What is an AI Automatio
n Agency (AAA)?**
Unlike traditional AI tools that offer generic functionalities, AAAs cater to specific business needs 
by creating custom AI solutions. These solutions integrate seamlessly with existing workflows and tech stacks, leveragin
g the power of generative AI and automation.
Lemme give you an example to make the idea clear. Imagine a high-volume leg
al firm drowning in paperwork. An AAA could design an AI-powered solution that automates tasks like document review and 
contract summarization. The AAA would integrate Optical Character Recognition (OCR) to convert scanned documents into te
xt and then utilize LLMs to analyze the content. Based on pre-defined rules and legal knowledge bases, the LLM could ide
ntify key clauses, flag potential risks, and even generate draft summaries  of lengthy contracts. This not only frees up
 valuable time for lawyers to focus on complex legal matters but also improves accuracy and consistency in document proc
essing as well as better reporting.

**Why AAA?**
Here are some compelling reasons to consider the AAA model:
**Fills th
e Gap for Smaller Businesses:** Many smaller companies lack the resources or expertise to develop in-house AI solutions.
 AAAs bridge this gap by providing readily available, customized solutions.
**Focus on Value, Not Just AI:** Effective A
I solutions go beyond simply incorporating AI. AAAs understand the importance of integrating AI with automation (think Z
apier) to create solutions that deliver real value.
**Niche Targeting is Key:** Focusing on a specific niche allows AAAs
 to gain a deeper understanding of client pain points and develop solutions that directly address them. This approach al
so helps with targeted outreach and establishing credibility.

**Roadmap to guide you through launching your AAA:**
 Cho
ose Your Niche: Select a niche you're familiar with, such as real estate, e-commerce, or legal services. Understanding t
he industry's needs allows you to develop solutions that resonate with clients.
 Build Your Toolkit: There are two main 
approaches to building custom solutions:
 Developer Network: If you lack programming expertise, consider building a netw
ork of on-demand web developers.
 No-Code Tools: Utilize no-code tools that offer drag-and-drop interfaces for building 
AI-powered solutions without coding.
 Cold Sales are Essential: Unless you have a pre-existing network, cold sales are c
rucial for acquiring clients. Craft compelling messages that highlight the value proposition of your AAA services.
The b
eauty of the AAA model lies in its accessibility. You don't  need to be a seasoned programmer to get started. Although y
ou must know basic coding and understand it’s principals. Most client needs can be addressed using APIs for Large Langua
ge Models (LLMs) along with automation tools. The true value lies in your ability to design and implement solutions that
  integrate seamlessly  with existing systems and workflows.

**Glimpse into the technical aspects of building custom AI
 solutions:**
**Leveraging LLMs:** Tools like Langchain and LlamaIndex simplify working with LLMs. They enable functiona
lities like integrating internal data sources and prompting LLMs to perform actions.
**Understanding RAG (Retrieval-Augm
ented Generation)**: RAG allows you to 'train' LLMs on a client's specific data, enhancing response accuracy and reducin
g the risk of irrelevant outputs.
**Enabling Autonomous Agents:** By analyzing LLM outputs, you can programmatically tri
gger actions like API calls. This allows chatbots to perform tasks beyond simply providing information.

**How No-Code T
ools Can Help**
No-code tools empower you to build solutions even without extensive coding knowledge. Here are some exam
ples:
**Solution 1:** AI Chatbots for SMEs: Tools like MyAskAI can be used to create chatbots that handle user queries, 
lead generation, and more. They simplify data ingestion and chatbot integration.
**Solution 2:** Internal Apps: Create i
nternal tools like report generation or draft generation based on user data and preferences. Tools like MindStudio can b
e used for content generation, and Zapier/Make.com can automate workflows involving multiple apps.

**Here's how to leve
rage AI for effective outreach:**
**Craft Compelling Messages:** Identify client pain points and frame your message to s
howcase how AI-powered solutions can address them. Quantify the potential benefits, such as cost savings or increased pr
oductivity.
**Targeted Prospecting:** Utilize tools like Apollo.io or ZoomInfo to find relevant prospects within your ch
osen niche. Tailor your outreach based on the target audience (e.g., company owners for smaller businesses, specific pro
fessionals in white-collar niches).

**Closing the Deal**
Once you've secured meetings with potential clients, focus on 
effectively closing the deal:
**Consultation Call:** Actively listen to client needs and pain points. Present a high-lev
el overview of potential solutions using tools like Plus AI for creating presentations.
**Demo Call:** Showcase a functi
onal prototype of a solution built with boilerplate code or no-code tools. Explain how the final product will look and f
unctionalities.

+++
PS: I am building [seekme.ai](https://seekme.ai). It acts as a comprehensive library of over 12000 
AI tools, categorized for various use cases, category, tasks and professions. The directory is updated daily, and even h
as a handy AI-powered search to help you filter and find the perfect AI tools. We send weekly AI updates in our newslett
er [subscribe here](https://seekme.ai/subscribe/newsletter)
```
---

     
 
all -  [ Unable to send request to containerized flask app ](https://www.reddit.com/r/flask/comments/1c7tk65/unable_to_send_request_to_containerized_flask_app/) , 2024-04-23-0910
```
Code for app.py - 

from flask import Flask, redirect, url_for, render_template, request, jsonify
import random
import o
s
import time
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from langchain_google_genai import C
hatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage


app = Flask(__name__)
app.config
['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

db = SQLAlchemy(app)

os.environ['GOOGLE_API_KEY'] = ''

class Data(d
b.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    request = db.Column(db.Text, nullable
=False)
    response = db.Column(db.Text)
    date_time = db.Column(db.DateTime, default=datetime.utcnow) 
    # action 
= db.Column(db.String(80))

    def __repr__(self):
        return '<UserData %r - %r>' % (self.request, self.date_time)


@app.route('/', methods = ['POST', 'GET'])
def home():

    if request.method == 'POST':
        json = request.get_js
on()

        if json and 'query'in json:
            question = json['query']

            model = ChatGoogleGenerative
AI(model='gemini-pro', convert_system_message_to_human=True)
            resp = model(
                [
               
     SystemMessage(content='Answer the given question in short - '),
                    HumanMessage(content = question
)
                ]
            )
        

            new_data = Data(request = question, response = resp.content)
   
         try:
                db.session.add(new_data)
                db.session.commit()
                return jsonif
y({'answer': resp.content})
            except Exception as e:
                print('##################################
#########')
                print(e)
                print('####################################################')
     
           return 'There was an issue in adding the data in database'
        else:
            return 'Unsupported quer
y format'
    else:
        # data = Data.query.order_by(Data.date_created).all()
        return 'Problem with request t
ype.'
        # return render_template('index.html', user_data = user_data)
    
    # return render_template('index.htm
l', content = 123)

def initialize_database():
    with app.app_context():
        db.create_all()

@app.route('/admin')
 ## This was unaccessible, so redirect user to home.
def admin():
    time.sleep(3)
    return '<h1>This is a header</h1
>'

if __name__ == '__main__':
    initialize_database()
    # db.create_all()
    app.run(debug=True)

Some things are 
removed from the code.

Code for dockerfile -

FROM python:3.10.13-bookworm

WORKDIR /app

COPY ./requirements.txt /app

COPY ./Dockerfile /app
COPY ./app.py /app

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

EXPOS
E 5000

CMD python -u app.py

Code for test.py to send request to app -

test.py to send request to the app - 

import r
equests
import json

url = 'http://localhost:5000/'

question = 'What is a star?'
myobj = {'query': question}

data = js
on.dumps(myobj)

headers = {'Content-Type': 'application/json'}

response = requests.post(url, json = myobj, headers= he
aders)

print(response)
print(response.text)

Command for docker container - docker run -p 5000:5000 --name flask-app-co
ntainer flask-app:1.0
```
---

     
 
all -  [ Llama2 generating empty response ](https://i.redd.it/85fat4n5nevc1.jpeg) , 2024-04-23-0910
```
Hey everyone! I'm working on building a simple email replier, which uses the llama2-7b-chat-gguf model from Huggingface.
 I'm using the CTransformers function to create a llm instance and then using a custom prompt template to generate reply
 to an email body. I'm using the get_response() function from the image above.

However, for certain mails which are hav
ing a longer body, the response is just coming out blank. My streamlit app showing the output, just runs and stops witho
ut showing any error, just a blank response. Same in the terminal. However, it does generate okay replies for some other
 mails. Cant understand if this is random or some mails are causing some bug here.

Note: Previously, i had gotten an er
ror of token limit exceeded, when i tried to generate response for a spam email having a body much longer than any of my
 ham emails, but here no such error is coming.

Can anyone give any hint/guidance/help? The project is to be submitted u
rgently.


```
---

     
 
MachineLearning -  [ [D] How to get the source documents from the retrieved context for RAG?  ](https://www.reddit.com/r/MachineLearning/comments/1bvoc1t/d_how_to_get_the_source_documents_from_the/) , 2024-04-23-0910
```
I'm not using Lanchain but only making API calls to an LLM service provider. The retriever is connected to a vector DB, 
and I would like to know what the LLM refers to WITHIN that retrieved context whenever it provides an answer, similar to
 how return_source_documents works in Langchain.

I'm using AzureOpenAI. I couldn't find much in their docs that related
 to returning the source documents. Any help will be greatly appreciated!

```
---

     
 
MachineLearning -  [ [P] RAG pipeline to query the ML Engineering Open Book ](https://www.reddit.com/r/MachineLearning/comments/1bu4wyx/p_rag_pipeline_to_query_the_ml_engineering_open/) , 2024-04-23-0910
```
I built a quick RAG implementation using Langchain to make it easy to query the [ML Engineering Open Book](https://githu
b.com/stas00/ml-engineering) by [Stas Bekman](https://twitter.com/StasBekman). The Multi-Vector retriever gave pretty go
od results and was quite easy to set up too. 

Github link - [https://github.com/shreyansh26/RAG-ML-Engg-Open-Book](http
s://github.com/shreyansh26/RAG-ML-Engg-Open-Book)

Hope this is useful for folks!
```
---

     
 
MachineLearning -  [ [Project] FinancialAdvisorGPT : LLM+RAG Boilerplate Project ](https://www.reddit.com/r/MachineLearning/comments/1btlpgd/project_financialadvisorgpt_llmrag_boilerplate/) , 2024-04-23-0910
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

     
 
MachineLearning -  [ [Project] Picachain, image search made simple. ](https://www.reddit.com/r/MachineLearning/comments/1bt7epv/project_picachain_image_search_made_simple/) , 2024-04-23-0910
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

     
