 
all -  [ Is Langchain + Gemini 1.5 even possible (with python)? ](https://www.reddit.com/r/LangChain/comments/1cxl70h/is_langchain_gemini_15_even_possible_with_python/) , 2024-05-22-0910
```
Trying to create a Langchain v1 app with Gemini 1.5 but have hit a wall and can't even get a hello world running. I can'
t find ANY useful information anywhere and the only thing I can get working is vertex AI's API, which is rudimentary wrt
 to pydantic etc. plus I won't be able to migrate to other models later on. 

What do you guys do? Any hints, tricks and
 links are warmly received.
```
---

     
 
all -  [ Errors developing LangGraph chatbot - need urgent help, please! ](https://www.reddit.com/r/LangChain/comments/1cxl689/errors_developing_langgraph_chatbot_need_urgent/) , 2024-05-22-0910
```
Hey guys! Before I start, I'm really thankful to everyone who took their time to read this and hopefully help/guide me w
ith my project, you're saviour. For context, this chatbot is supposed to be my bachelor's final year project, so it real
ly matters a lot to me that I know it's functioning well.

Now unto my chatbot and what it is about; I'm trying to devel
op a chatbot specialized in offering the user video games recomendations based on his preferences. For this task, I thou
gh that going with LangGraph would prove to be a smart move.

For a better understanding of it, I'll attach the diagram 
that I've made of how it should behave and work, and here's a brief explanation on the chatbot's workflow and steps:

1.
 **User Query**: The user inputs a query about video game recommendations.
2. **Input Assistant**: The `input_assistant`
 checks if the query is relevant to video game recommendations using a classification prompt.
   * If relevant, the quer
y proceeds to the next step.
   * If not, the user is asked to provide a more specific query.
3. **Game Search Assistant
**: The `game_search_assistant` uses the Tavily API to find games based on the user's query and returns their titles.
4.
 **Parallel Agents**: Several agents run in parallel to gather detailed information about the recommended games  (also m
aking use of Tavily API):
   * `game_description_assistant`: Fetches game descriptions.
   * `game_platform_assistant`: 
Fetches platform availability and store details.
   * `game_genre_assistant`: Fetches game genres.
   * `game_developer_
publisher_assistant`: Fetches developer and publisher information.
   * `game_metacritic_assistant`: Fetches Metacritic 
scores.
   * `game_age_restriction_assistant`: Fetches age restriction details.
   * `game_trailer_assistant`: Fetches t
railer links.
5. **Output Assistant**: The `output_assistant` compiles the gathered information into a comprehensive res
ponse and returns it to the user.

Diagram:

https://preview.redd.it/duyi2195zu1d1.png?width=2382&format=png&auto=webp&s
=0333f1e13fff4e4d112518d8aca027117ec537fa

Problem is, I'm facing some errors, the current one being 'list indices must 
be integers or slices, not str'. I'm very new to working with this framework, or even adventuring in this sphere of LLM 
apps, so please, forgive me for my stupidity.

The code implementation of this chatbot can be accessed by clicking on th
is link: [https://github.com/MOUNAJEDK/GameSeeker-Chatbot](https://github.com/MOUNAJEDK/GameSeeker-Chatbot)

It would me
an a lot if you gave it some of your time and go through what I've written there and give me the needed feedback!
```
---

     
 
all -  [ Are multi agents systems also meant to be used in chatbots with continuous conversation? ](https://www.reddit.com/r/LangChain/comments/1cxkl24/are_multi_agents_systems_also_meant_to_be_used_in/) , 2024-05-22-0910
```
Title says pretty much. By agent I mean the concept, not exclusively langchain agent. 


```
---

     
 
all -  [ Generative AI Agents Developer Contest by NVIDIA & LangChain ](https://www.nvidia.com/en-us/ai-data-science/generative-ai/developer-contest-with-langchain/) , 2024-05-22-0910
```

```
---

     
 
all -  [ Introducing vector database capabilities in Azure Cosmos DB for NoSQL (Public Preview) ](https://www.reddit.com/r/AZURE/comments/1cxfhpb/introducing_vector_database_capabilities_in_azure/) , 2024-05-22-0910
```
We are excited to announce that native vector indexing and search in Azure Cosmos DB for NoSQL is now available in previ
ew! Azure Cosmos DB is the world’s first full-featured serverless database with vector search and features multiple vect
or index options from flat (exact), quantized flat, and a new DiskANN-based index. DiskANN is a suite of highly scalable
, accurate, and cost-effective approximate nearest neighbor (ANN) algorithms, developed at Microsoft Research, for low-l
atency and cost-effective vector search at any scale.  

You can take advantage of Azure Cosmos DB’s rich features such 
as a NoSQL query syntax to combine vector search with query filters that can increase the relevancy and accuracy of your
 vectors searches. You’ll also get all the benefits of Azure Cosmos DB’s flexibility, instant autoscale, 99.999% SLA, ge
o-replication, and more! Store your data and vectors together, eliminating the need to store vectors in a separate vecto
r database and realize improved consistency, synchronization between vectors and data, and a reduction in the complexity
 and costs of AI applications.

What is DiskANN?

DiskANN is a suite of **scalable** approximate nearest neighbor search
 algorithms designed for **efficient vector search at any scale**. It offers **high recall, high queries per second (QPS
), and** **low query latency** even for billion-point datasets. This makes it it a powerful tool for handling large volu
mes of data. [Learn more about DiskANN from Microsoft.](https://www.microsoft.com/en-us/research/project/project-akupara
-approximate-nearest-neighbor-search-for-large-scale-semantic-search/)



* DiskANN is a graph-based indexing and search
 system that performs fast and accurate approximate nearest neighbor (ANN) search at **any-scale**.
* It primarily uses 
an SSD-based index to scale to an order of magnitude more points compared to in-memory indices, while still retaining **
high QPS and low latency.**
* Quantized (compressed) vectors are kept in memory, and DiskANN balances interactions betwe
en the two to offer low latency and high accuracy.
* DiskANN is based on a novel graph index called **Vamana** that is m
ore versatile than existing graph indices by maintaining accuracy despite many insertions, modifications, and deletions,
 without the need for expensive index rebuilds.

**The DiskANN Advantage**

https://preview.redd.it/hfs6sndsst1d1.png?wi
dth=1536&format=png&auto=webp&s=2c904a439d1169741a7649e71400a975860bce79

**Scalability**

* DiskANN vector indexes are 
stored on high-speed SSDs, while compressed vectors are stored in memory.  This reduces memory-footprint of the vector i
ndex, enabling planet-sized scalability for vector search scenarios.

**Low Latency**

* The DiskANN graph index constru
ction makes it very efficient during search, minimizing the number of SSD reads to achieve high throughput and low laten
cy.

**High Accuracy**

* During index construction, nodes in the graph are connected to diverse neighbors to improve re
call. After the search operation, the results are re-ranked using the full-precision vectors providing high accuracy.

*
*Low Cost**

* Because the quantized vectors are stored in memory and the full-precision graph is stored on SSDs, it’s m
uch less expensive to maintain and operate DiskANN-based indexes. This results in lower RU costs for your vector search 
queries.

**Robust to Insertions, Deletions, and Modifications**

* The DiskANN graph index is capable of supporting tra
nsactional workloads and does not degrade over time with high volumes of inserts, updates, or deletes. This is a differe
ntiator among typical vector databases in the market today, which are built using HNSW and other less robust methods tha
t require computationally expensive full index rebuilds to maintain accuracy.

The benefits of DiskANN, combined with th
e instant & dynamic autoscale, global replication, and industry leading 99.999% SLA of Azure Cosmos DB make for an unpar
alleled database for managing both your operational and vector data workloads.

# What vector index options are availabl
e?

There are multiple types of vector index policies that can be defined for a Cosmos DB collection. [Learn more about 
vector indexing in Azure Cosmos DB](https://aka.ms/CosmosDBVectorIndexing)

* **Flat index** is an exact (sometimes call
ed brute-force) approach to vector indexing. The vectors are placed on the Azure Cosmos DB index and referenced for effi
cient lookup. This may be a good option to use in scenarios where 100% accuracy of vector searches is required, and both
 the dimensionality of the vectors is small.
* **Quantized Flat index** is also an exact index, but the vectors are quan
tized (compressed) before being added to the Azure Cosmos DB index. This is very efficient and uses the same quantizatio
n method featured in DiskANN.
* **DiskANN** enables approximate nearest neighbors (ANN) search at scale, with efficienci
es that reduce RU cost and latency. This is extremely efficient and low-cost, especially when you expect to scale to lar
ger scenarios. **Note** that using the DiskANN index requires [enrollment in a separate preview](https://aka.ms/DiskANNS
ignUp) as it’s still in an early preview version.

This table provides a good guide for the different index types and th
eir strengths:

||
||
|**Index type**|**Description**|**When to use it?**|**Max # of dimensions**|**RU Cost**|**Speed**|
**Accuracy**|
|Flat|Exact search on full vectors|100% accuracy is required The container holds fewer than 10k vectors. V
ectors are small in size|505|High|Slow|Highest|
|Quantized Flat|Exact search on quantized vectors. Faster, with slight a
ccuracy reduction.|High accuracy is needed You have at least 1,000 vectors in the collection. Vectors are larger in size
 The scenario is scoped to at most 100k vectors|4096|Medium|Medium|High|
|DiskANN|Fast, approximate search at any scale.
|In any scenario where scale is expected|4096|Lowest|Fast|High|

 

 

**Enroll in the Vector Search Preview**

Vector s
earch in Azure Cosmos DB for NoSQL is a preview feature and requires enrollment via the *Features* page of your Azure Co
smos DB resource . Follow the below steps to register:

1. Navigate to your Azure Cosmos DB for NoSQL resource page.

2.
 Select the “Features” pane under the “Settings” menu.

3. Select “Vector Search in Azure Cosmos DB for NoSQL”.

4. Read
 the description of the feature and confirm you want to enroll in the preview.

5. Select “Enable” to enroll in the prev
iew.

https://preview.redd.it/jc9y0k5jst1d1.png?width=1536&format=png&auto=webp&s=7ae7741f772a6da598bf4aa827ecbc0fe6d918
ba

 

# Next Steps

The integration of vector search capabilities into Azure Cosmos DB for NoSQL marks a significant ad
vancement in database technology, offering unparalleled scalability, efficiency, and accuracy. With the introduction of 
DiskANN and other vector indexing options, Azure Cosmos DB provides robust solutions for managing large-scale vector dat
a alongside your operational data. Enroll in the Vector Search Preview today and explore the future of AI-driven applica
tions with the powerful features of Azure Cosmos DB.

* [Learn more about Vector Search Preview in Azure Cosmos DB. ](ht
tps://aka.ms/CosmosVectorSearch)
* [Enroll in the DiskANN early preview](https://aka.ms/DiskANNSignUp)
* [Azure Cosmos D
B in Semantic Kernel](https://github.com/microsoft/AzureDataRetrievalAugmentedGenerationSamples/)
* [Azure Cosmos DB | 🦜
️🔗 LangChain](https://python.langchain.com/v0.1/docs/integrations/vectorstores/azure_cosmos_db/)
* [Vector Database | Mi
crosoft Learn](https://learn.microsoft.com/en-us/semantic-kernel/memories/vector-db)
* [DiskANN – Microsoft Research](ht
tps://www.microsoft.com/research/publication/diskann-fast-accurate-billion-point-nearest-neighbor-search-on-a-single-nod
e/)

  
Blog originally posted at: [https://devblogs.microsoft.com/cosmosdb/introducing-vector-database-capabilities-in-
azure-cosmos-db-for-nosql/](https://devblogs.microsoft.com/cosmosdb/introducing-vector-database-capabilities-in-azure-co
smos-db-for-nosql/)
```
---

     
 
all -  [ [For Hire] GenAI Specialist, Ex-Booking.com Data Scientist [50USD/hr] ](https://www.reddit.com/r/freelance_forhire/comments/1cxehch/for_hire_genai_specialist_exbookingcom_data/) , 2024-05-22-0910
```
Hi, I am data analyst/scientist with 4 years experience. I have worked for one of the world biggest Telecom groups (Tele
nor) and also Agoda(Booking.com). Now working as GenAI specialist at vanna AI

If your looking to outsource tasks or get
ting something built in Python/R or QuickSense/Tableau please do reach out.


I can provide evidence of everything, I ev
en write about data science/analytics on Medium: https://python.plainenglish.io/sankeying-with-plotly-90500b87d8cf

GenA
I projects:
https://medium.com/firebird-technologies/generate-powerpoints-using-llama-3-a-first-step-in-automating-slide
-decks-536f5fcb6e0e

https://medium.com/firebird-technologies/using-langchain-to-teach-an-llm-to-write-like-you-aab394d5
4792

Very good at making visualization. Will charge a reasonable rate
```
---

     
 
all -  [ Seeking advice on enabling full document understanding with RAG ](https://www.reddit.com/r/LangChain/comments/1cxd1mk/seeking_advice_on_enabling_full_document/) , 2024-05-22-0910
```
Hello everyone,

I'm currently developing a project using RAG and encountering the following challenge: The RAG model pr
ocesses text in segments, which omits a comprehensive view and and analysis of the document in full (such as summarizati
on). Are there proven strategies that allow for retrieving the entire context of a chunked document, enabling summarizat
ion of the entire doc?

I'm curious to hear about your experiences and if you have previously successfully implemented s
uch a strategy.

Thank you!
```
---

     
 
all -  [ LLM prompt optimization ](https://www.reddit.com/r/LangChain/comments/1cxcln7/llm_prompt_optimization/) , 2024-05-22-0910
```
I would like to ask what are your experience in doing prompt optimization/automation when designing ai pipelines? In my 
experience, if your pipeline is composed of large enough number of  LLMs, that means it’s getting harder to manually cre
at prompts that make the system work. What’s worse is that you even cannot predict and control how the system might sudd
enly break or have worse performance if you change any of the prompts! I’ve played around with DSPy a few weeks before; 
however, I am not sure if it can really help me in the real world use case? Or do you have other tools that can recommen
d to me? Thanks for kindly sharing your thoughts on the topic!
```
---

     
 
all -  [ Can we use more than 1024 input tokens in flan-t5-xxl  ](https://www.reddit.com/r/LangChain/comments/1cxbehz/can_we_use_more_than_1024_input_tokens_in/) , 2024-05-22-0910
```
Is there a way to use the Google/flan-t5-xxl model with context of over 1024 tokens.
I am using hugging face inference a
pi and it has that limitations.
```
---

     
 
all -  [ Need help with prompting Mistral-7B-Instruct-v0.2 for creating a coding tutor bot ](https://www.reddit.com/r/MistralAI/comments/1cxacjw/need_help_with_prompting_mistral7binstructv02_for/) , 2024-05-22-0910
```
Hello everyone,  
I am trying to create a Multi-agent Coding Tutor chatbot (*or academically speaking 'CTS - Conversatio
nal Tutoring System'*) for my course project. We want it to be a personalized tutor, which means that it will teach the 
person based on their age, level of education, and hobbies or interests.

To instruct this Mistral-7B-Instruct-v0.2 4-bi
t quantized model, we have added the following system prompt to the model:

    system_prompt = f'''Imagine you are a fr
iendly and highly knowledgeable teacher who specializes in teaching {prog_language_to_teach} programming. 
    Your stud
ent, who is a {user_age}'s old {user_edu_scope} student and whose understanding and interests is into {user_interest}, i
s eager to learn and looks up to you for clear, easy-to-understand explanations. 
    For every concept you introduce, p
rovide a brief overview and relate it to a real-life scenario or analogy that will resonate with the student, making it 
easier for them to grasp the topic quickly.
    
    When explaining programming concepts, consider the student's age an
d their hobbies or interests, tailoring examples and analogies to align with these details. Your explanations should inc
lude short, precise programming examples relevant to the student's life and interests. 
    After presenting an example,
 break it down into step-by-step explanations to ensure the student fully understands.
    
    Periodically, engage the
 student with quick quiz questions or programming tasks that are directly related to what you've discussed. 
    These a
ctivities should build on the chat history and context, reinforcing the student's learning and keeping the conversation 
interactive and engaging.
    
    Remember, your goal is to create a supportive, engaging learning environment that ada
pts to the student's abilities, interests, and pace, making learning Python an enjoyable and rewarding experience.'''

M
istral-7B-Instruct-v0.2 doesn't have an explicit system prompt, so I had to find a different way to add one to the code 
for the very first prompt.

`model_input = f'<s>[INST] {system_prompt} [/INST]</s>' + f'[INST] {user_message} [/INST]'`


Now, on the initial run, the chatbot is doing fine often and as expected.  In the case of a 10-year-old Kindergartener 
who loves 'Baby Shark Rhyme,' the bot will talk about what he likes. In another case of a 20-year-old shareholder in the
 share market, the bot tried to teach programming using business analogies.

But the common issues I face are the follow
ing:

1. The chatbot is too verbose, especially on complex topics such as Encapsulations. (*I have used* `max_new_tokens
=1000`, is it causing the verbosity? Lessening to 500 or 750 causes the model to stop on incomplete answers abruptly.\*)

2. So far, **switching from a coding tutor to a general tutor has been the hardest thing**. For instance, if the user i
s older and asks about something off-topic, like *Newton's law* or the *American Law of Immigration*, it immediately swi
tches itself from the coding tutor to that other tutor.
3. Another problem is that it gives the answers right away while
 it generates the quizzes. Although I tested with different prompts, I can resist this nature.

My biggest problem so fa
r is the 2nd and 1st one, respectively. I have tried adding refusal prompts in the system prompt, but then it slightly r
efuses to teach those irrelevant topics and then starts making coding examples on it.

        ## Strict Refusal:
      
  If the question is not related to programming, respond strictly with a refusal sentence and do not provide any further
 explanation or code.

For these cases, sometimes it follows, sometimes not. Also adding too many instructions into the 
system prompts too big resulting in GPU memory exhaustion after 5-6 long chats. BTW, To mimic a memory feature, I am sav
ing chats to a dictionary.

Since yesterday and again tonight, I've been trying to make the prompting better but haven't
 been able to. I'm brand new to LLM chatbot programming and have never done this before. This project began a month ago 
because the idea is unique to my MSc project, but I got stuck in the middle of it.

How can I make the prompting better 
to avoid the problems that were brought up? Also, can someone recommend a good tutorial on how to make this kind of chat
bot? I've been looking for these, but most of the tutorials use OpenAI and/or langchain. For a change, my supervisor wan
ts us to only test with open-source models. We can use Mistral to begin because it fits on the Kaggle notebook we have.


Any suggestion including trying to other approaches, totally changing the system prompt, and trying another one (*if yo
u say so, can you please show me one?*) and a good & detailed tutorial will be super appreciated. IDK, suddenly it feels
 so lost.
```
---

     
 
all -  [ [For Hire] Programmer/Web Developer/IT Consultant (Python, PHP, AI, etc.) ](https://www.reddit.com/r/forhire/comments/1cx9mj0/for_hire_programmerweb_developerit_consultant/) , 2024-05-22-0910
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

     
 
all -  [ Conceptual question - is LangGraph's utility dependent on the ability to call tools?  ](https://www.reddit.com/r/LangChain/comments/1cx9jpu/conceptual_question_is_langgraphs_utility/) , 2024-05-22-0910
```
Every langgraph example I've seen so far uses a tool interface to facilitate switching between nodes in the graph. 
AWS 
Bedrock doesn't yet fully support Anthropic's beta tool calling APIs. 
Conceptually or practically speaking, how might o
ne make, for example, a supervisor agent that delegates work to other nodes - *without tool-calling*?
```
---

     
 
all -  [ Local LLM for text analysis ](https://www.reddit.com/r/LocalLLaMA/comments/1cx91ur/local_llm_for_text_analysis/) , 2024-05-22-0910
```
First off - I am new to LLMs so I do not really know what I am doing. 

I was given the task to build a summarization an
d analysis pipeline. The pipeline has to analyze about 100 news article, scan for some specific information and summariz
e the articles which hold the wanted data. In a last step the model is supposed to assess if certain criterias are met b
y the summaries and give an according grade. I already implemented this using only the openai API with chatgpt-3.5 and t
he langchain framework, which works just fine.

Unfortunately the system may not send data into the cloud so I need a wa
y to reproduce the pipeline locally. My first instinct was to download meta-llama-3-8B from [hugging face](https://huggi
ngface.co/meta-llama/Meta-Llama-3-8B) and try it out but I got stuck pretty early into the project. Like I said, I am qu
ite new to LLMs and the frameworks that come with them. To get into it I simply wanted to 'talk' to the model to see how
 the answers are generated. I used the transformers framework, loaded the llm, created a 'text generation' pipeline and 
put in some text.

But no matter what I try, I won't get a proper answer. Sometimes text gets generated, sometimes it do
es not. The only consistency I can find is, that it does not want to answer my questions directly.   
I can't even get a
n answer to the question 'How are you?'. 

So my guess is that I am doing something fundamentally wrong here. Any sugges
tions where I took the wrong turn? 

  

```
---

     
 
all -  [ Langsmith not tracing ](https://www.reddit.com/r/LangChain/comments/1cx7rv6/langsmith_not_tracing/) , 2024-05-22-0910
```
does anyone know why langsmith tracing doesn't work when deployed in the cloud?

It works fine when i run my graphs loca
lly by setting these:  
  
`# Set your Langsmith traces`

`LANGCHAIN_TRACING_V2 = True`

`LANGCHAIN_ENDPOINT = os.getenv
('LANGCHAIN_ENDPOINT')`

`LANGCHAIN_API_KEY = os.getenv('LANGCHAIN_API_KEY')`

`LANGCHAIN_PROJECT = os.getenv('LANGCHAIN
_PROJECT')`

  
When we deploy the same code in a severless environment (lambda) and including the above envs, we just d
on't get any tracing info on langsmith.

I'm not sure what we're missing?
```
---

     
 
all -  [ Looking for Recommendations on Langchain Courses  ](https://www.reddit.com/r/learnmachinelearning/comments/1cx7q5c/looking_for_recommendations_on_langchain_courses/) , 2024-05-22-0910
```
Hey All, I’m looking for recommendations  on courses/tutorials/materials in order to gain some understanding of the Fram
ework and get some hands on under my belt. The ones on youtube are not very in-depth, took a couple of courses from Deep
learning.ai but even those were not very extensive. I do have couple of Basic RAG, Text2Sql projects using Langchain but
 i don’t think thats good enough. I’m trying to get into tools, agents, function calling and advanced stuff. Any recomme
ndations on courses, tutorials or channels would be greatly appreciated.
```
---

     
 
all -  [ Multimodal rag system using Open Source models  ](https://www.reddit.com/r/LangChain/comments/1cx6eox/multimodal_rag_system_using_open_source_models/) , 2024-05-22-0910
```
Hi, 
I'm trying to develop a rag system using llama3, but my base knowledge contains pdfs,  ppt, images and videos (tuto
rials). So how can i achieve that.

I would appreciate any help, links for similar projects...
```
---

     
 
all -  [ Anyone tried ParentDocumentRetreiver with Reranking ](https://www.reddit.com/r/LangChain/comments/1cx37pi/anyone_tried_parentdocumentretreiver_with/) , 2024-05-22-0910
```
Hi,

I see both ParentDocumentRetriever and Reranking as promising techniques for improving the RAG system. Has anyone t
ried to combine these two techniques, so first use the ParentDocumentRetreiver and then rerank the results, e.g. with Co
lBERT?

I think one limitation is the max\_tokens of Colbert that do not fit to the retrieved, bigger chunks. One think 
would be to first rerank the smaller chunks, but I am not sure how to implement this with langchain.

But would be inter
esting to see which experiences you guys have.
```
---

     
 
all -  [ Can someone demystify what it means to support function calling ](https://www.reddit.com/r/LocalLLaMA/comments/1cx35hi/can_someone_demystify_what_it_means_to_support/) , 2024-05-22-0910
```
I already know quite a lot about how large language models work practically. For the most part they are decoder models t
hat predict the next token (is my understanding).   
I know that it is possible to get an LLM to output JSON by using so
mething like Structured Output Parser from Langchain, which does prompt engineering to make it produce valid JSON then p
arses the JSON.

My question: I have heard that some models support function calling. My understanding is that the model
 chooses a function from a predefined list of function definitions to address a user query and generates the parameters 
for that function. SO what does it mean for a model to support function calling. Is it just that it is good enough to ha
ndle that complexity?  Is it that it has been instruction fine tuned on function calling?
```
---

     
 
all -  [ RAG on multiple structured data streams. ](https://www.reddit.com/r/LangChain/comments/1cx264a/rag_on_multiple_structured_data_streams/) , 2024-05-22-0910
```
I have data in open search in multiple indices, each index with different schema.  
I have data at more granular level i
n open search. I need to aggregate the data and use aggregated data into RAG pipeline.

I am planning to use milvus as v
ector db but I am not able to finalise on what text should we create embeddings on.  
One open search index for example 
contains user website visits like  
ip\_address, user\_name, visited\_url, website\_type   
some other may contain user 
actions like  
ip\_address, user\_name, action \[install/uninstall\], command, details  


from these different types of
 data in indices, i am planning to create different collections in vector db.  
what should i create embedding on in vec
tor db ?  


prompt should be able to answer like   
what all things observed from user ABC  
are there any install acti
ons from by user who visited site like XYZ.  


I can not use sql db for this as questions could be more natural search 
than just give me X where Y type of questions.  


New to RAG, so not able to figure out how one embeddings perform bett
ers others.  
One plan is to just append values of a record and build embedding on it.  
Other one is to create verbose 
text from the record and build embedding on it.
```
---

     
 
all -  [ LLM bots that have current knowledge and google search skills? ](https://www.reddit.com/r/LangChain/comments/1cx1tjp/llm_bots_that_have_current_knowledge_and_google/) , 2024-05-22-0910
```
LLM noob here, not sure how to build this or it probably already exists.

I am looking for a self-hosted LLM bot app tha
t has custom trained knowledge from local text e.g. 10k epubs from arxiv but also can have access to google search API f
or finding the latest resources regarding a certain query e.g. 'tell me the latest developments in stable diffusion mode
ls' and it should be able to go through the stable diffusion site and white papers to build a precise answer.

Obviously
 this LLM needs to be finetuned on the new data? e.g. 10k epubs?

But the google search API results need to be input int
o the context window so that it can use the info?

Ultimately this model should be runnable locally or on colab, without
 all the corporate censoring on chatgpt and gemini.

Please tell me if this exists already in langchain or some other re
po, detailed links and guidelines would be the best (assume I have no LLM experience, but am an average python programme
r.)

Thanks in advance!
```
---

     
 
all -  [ LangChain Framework vs New Assistants API with RAG ](https://www.reddit.com/r/LangChain/comments/1cx1ln4/langchain_framework_vs_new_assistants_api_with_rag/) , 2024-05-22-0910
```
Hey all, i've seen some mention's around here briefly about comparing LangChain's tooling (or even just building out you
r retrieval models yourself by removing abstractions) to the current state of assistant's API (w/ v2)

At the time of re
lease I could see why more leaned towards langhain's framework, but with the recent advancements of assistant's api (v2)
, including improved retrieval systems, new vector stores, as well as function calling via tool\_choice. I'm really cons
idering using their endpoint for a new project considering costs, latency, and retrieval system's will get better over t
ime.

I used LangChain's Js framework when it first came out, and we sort of transitioned to creating our own functions 
to avoid some of the abstraction layers, but now it almost seems archaic to build your own. At least for the majority of
 use-cases I see. And of course, I could see cost as a factor here, considering assistants is significantly more expensi
ve, especially if you're using code interpreter, but you also have to consider the opportunity cost you'd save not build
ing out your own tooling system. Definetly a cost trade-off to consider here for firms (and not just dev's building thei
r own projects).

So user's of OpenAI model's, I'd love to learn why you went one route or the other for some projects. 
Is it cost? quality of responses? latency? or just don't like the idea of being vendor-locked to an api? All idea's/stat
ements are welcome. Genuinely trying to learn here.
```
---

     
 
all -  [ Vercel AI SDK vs chainlit for chatbot project ](https://www.reddit.com/r/LangChain/comments/1cx1fdd/vercel_ai_sdk_vs_chainlit_for_chatbot_project/) , 2024-05-22-0910
```
Hi everyone,
I'm looking to build a flexible, customizable, and high-performing chatbot using LangChain/LangGraph and LL
M technology. I'm currently torn between two options: using the Vercel AI SDK with Next.js or Chainlit with Python.
Whic
h solution do you think is the best for building a chatbot today, considering factors like ease of use, scalability, and
 performance?
Thanks in advance for your insights!
```
---

     
 
all -  [ How to stream response a RAG chain with Vercel ai sdk ](https://www.reddit.com/r/LangChain/comments/1cx052b/how_to_stream_response_a_rag_chain_with_vercel_ai/) , 2024-05-22-0910
```
Hi, I'm trying to build RAG chain following this [tutorial](https://js.langchain.com/v0.1/docs/expression_language/cookb
ook/retrieval/#conversational-retrieval-chain), and I'm using Vercel sdk for the streaming api and ui building. While I 
tried their support for Langchain [here](https://sdk.vercel.ai/providers/legacy-providers/langchain), things didn't work
 properly. There's no error but not any response showing either. With the 2 packages mixed together, I'm not even sure w
here to debug, would really appreciate for some help, thanks!
```
---

     
 
all -  [ Multimodal RAG with text and images vs textual embeddings of images ](https://www.reddit.com/r/LangChain/comments/1cwpoc1/multimodal_rag_with_text_and_images_vs_textual/) , 2024-05-22-0910
```
Hi everyone,

I am currently building a location search assistant which, given an image or its textual description, retr
ieves the top k most similar locations by performing a multimodal RAG with langchain and chromaDB. While it seems pretty
 standard, I have been thinking about the different ways by which this kind RAG can be achieved. Specifically, I am thin
king between:

- Embedding images and location description, separately, by using CLIP and GPT-4, respectively. To keep t
rack of the location, I would include the corresponding location metadata during the insert

- Employing GPT-4 vision mo
del to provide a summary description of a location given all their images and store it together with the location descri
ption as one textual embedding

The first approach looks more precise to me since performing storing the summary descrip
tion of multiple images would encounter a loss of details. On the other side, it is still unclear to me how to handle sc
enarios in which users perform searching with both text and and image: which domain (vision or textual) would be preferr
ed to retrieve the most similar locations?

  
Am I missing something? What would you suggest in this case?

  

```
---

     
 
all -  [ 0.2 docs refresh ](https://www.reddit.com/r/LangChain/comments/1cwkaq9/02_docs_refresh/) , 2024-05-22-0910
```
Hi all! One of the constant things we've heard from the community here is a desire for better docs. We've spent a lot of
 time over the past two weeks overhauling the documentation for 0.2. Some things include: versioned docs, a conceptual g
uide, much simpler navigation and organization, 'langchain over time', etc

We wrote a blog going through some of these 
two things as well as our thought process: [https://blog.langchain.dev/documentation-refresh-for-langchain-v0-2/](https:
//blog.langchain.dev/documentation-refresh-for-langchain-v0-2/)

We genuinely would love any feedback, no matter how sma
ll, on the new docs and ways to keep on improving them. A lot of the changes have been directly influenced by the commun
ity here - we really appreciate the feedback and ideas, so I hope you all know that :) Docs are a key focus of ours goin
g forward, and we'll be monitoring this thread pretty actively for ideas to implement!
```
---

     
 
all -  [ chatbot that can be corrected by users ](https://www.reddit.com/r/LangChain/comments/1cwk82e/chatbot_that_can_be_corrected_by_users/) , 2024-05-22-0910
```
Hello all. Disclaimer I'm a total newbie. Disclaimer 2 the user base is trusted so no need to fear about the dangers of 
implementing this for something like a public facing customer support bot.

I've got a RAG chatbot trained on some long 
PDFs (user manuals and stuff like that). One feature I'd like to implement is the ability for the user to correct the re
sponse given by the model, and for the model to learn from that.  
One very hacky idea I had was to use few-shot prompti
ng and every time a user makes a correction, update the system prompt with the question and corrected answer. The user b
ase for this bot would be very small, but still this idea seems kind of terrible lol.

Links to any resources where I ca
n learn more would be greatly appreciated.
```
---

     
 
all -  [ Looking for full-stack engineer | Legal AI Agents | Libra | Berlin, Germany ](https://www.reddit.com/r/LangChain/comments/1cwg46f/looking_for_fullstack_engineer_legal_ai_agents/) , 2024-05-22-0910
```
Hi Everyone, 

At Libra we're building AI agents capable of executing entire litigation workflows autonomously. [Libra](
http://libratech.ai/) is a seed stage company with a few pilot enterprise customers. At the moment we're a team of 5 bas
ed in Berlin and raised a $1M pre-seed round. We're looking for a full-stack engineer to join us full-time onsite/hybrid
. If you're excited about building the future of litigation, apply [here](https://www.linkedin.com/jobs/view/3913562327)
 or reach out [directly](mailto:viktors@libratech.ai)!
```
---

     
 
all -  [ Javascript vs Python ](https://www.reddit.com/r/LangChain/comments/1cwc0vx/javascript_vs_python/) , 2024-05-22-0910
```
I have tried to learn LangChain both on Python and Javascript, and from what I learnt, I can tell that Javascript is not
 supported as much as Python, but also I haven't really use it enough to really know the limit, so my question is how mu
ch is a gap between javascript and python with langchain 
```
---

     
 
all -  [ How to match a photo of a printed letter with a template pdf with almost the same text ](https://www.reddit.com/r/LangChain/comments/1cw9hco/how_to_match_a_photo_of_a_printed_letter_with_a/) , 2024-05-22-0910
```
I want to match photos of official letters (printed, not handwritten) with one template of that same letter in PDF forma
t from a whole set of template PDFs. One of the templates contains roughly the same text, but features like salutations 
are different.

I was thinking of:

	1.	Creating embeddings of the photo and PDF and then doing a similarity search.
	2.
	Converting the photo and templates to text and comparing them at the sentence level.

The easiest would be if the photo
 and template had a QR code, but that’s not possible.

Any help is greatly appreciated!
```
---

     
 
all -  [ How to stop token Generation ](https://www.reddit.com/r/LangChain/comments/1cw8j5z/how_to_stop_token_generation/) , 2024-05-22-0910
```
I am using Open ai Api to stream the answer , I want to replicate the Stop generation function as in the chatgpt interfa
ce , can someone help me with how to stop token generation and not just streaming.
```
---

     
 
all -  [ Dialogflow cx with custom frontend ](https://www.reddit.com/r/LangChain/comments/1cw89go/dialogflow_cx_with_custom_frontend/) , 2024-05-22-0910
```
Hey! I'm facing issues in connecting custom frontend with dialogflow cx API (detect_intent), while trying to get paramet
er input in dialogflowcx. Has anybody worked on this?
```
---

     
 
all -  [ Is there a standardized/optimal way to do RAG context expansion? ](https://www.reddit.com/r/LangChain/comments/1cw61uj/is_there_a_standardizedoptimal_way_to_do_rag/) , 2024-05-22-0910
```
see title 
```
---

     
 
all -  [ Are LLM observability tools solutions in search of a problem? ](https://www.reddit.com/r/LangChain/comments/1cw0mkt/are_llm_observability_tools_solutions_in_search/) , 2024-05-22-0910
```
I noticed many LLM observability and monitoring tools are launched every week or so now. Are these tools actually used b
y real startups and companies, or are they more like 'solutions in search of a problem'?

These tools seem to do one or 
a combination of the following:

* **monitor LLM inputs and outputs** for prompt injection, adversarial attacks, profani
ty, off-topic content, etc
* **monitor LLM metrics over time** use such as cost, latency, readability, output length, cu
stom metrics (tone, mood, etc), drift
* **prompt management** including a/b testing, versioning, a gold standard set

Wh
at have you observed? Do companies that have their own LLM-powered features or products use these monitoring tools?
```
---

     
 
all -  [ What are my possibilities here in my project? ](https://www.reddit.com/r/LangChain/comments/1cvosry/what_are_my_possibilities_here_in_my_project/) , 2024-05-22-0910
```
Hello, Langchain community! I wanna talk about a project I'm working on and wanted to know if it's possible to do and if
 thats the best way of doing it. Resources that can help me would be quite welcome!

What I have regarding this API proj
ect is the [app.py](http://app.py) here  [https://github.com/Briqz23/Interactive\_RAG\_e-book/blob/main/agentapi/app.py]
(https://github.com/Briqz23/Interactive_RAG_e-book/blob/main/agentapi/app.py)



**Project Idea: An e-book where users c
an interact with the characters.**



**Current Implementation:**

* API endpoint: /character\_id/user\_input
* Data sou
rces and tools:
   *   FAISS DB with the book's PDF embedded and a retriever for it
   *   Tools in the toolkit include:

   * WikipediaQueryRun
   *  ArxivQueryRun
*   An agent uses OpenAI LLM, all the tools, and the contextualize\_q\_promp
t to select the best answer.

**Objective:**

When the agent retrieves an answer from WikipediaQueryRun or ArxivQueryRun
, it does not follow the instruction to behave as the specified character. I want to resolve this issue and implement an
other agent to check for hallucinations or ensure it behaves correctly. I am using a Langchain agent but intend to use a
 CrewAI agent.



**Challenges:**

I am struggling to implement the chat\_history feature in more complex scenarios, esp
ecially with the FastAPI API.



**End Goal:**

Create an API that processes user input and chat history. The input goes
 to an agent that queries various sources for the best answer. Another agent verifies the response's accuracy before the
 API returns the final answer.
```
---

     
 
all -  [ RAG agent is returning empty response once the libraries are updated to a newer version.  ](https://www.reddit.com/r/LangChain/comments/1cvlhwt/rag_agent_is_returning_empty_response_once_the/) , 2024-05-22-0910
```

I have a RAG framework where we are reading a doc and answering questions related to it, anyone know how can we debug a
n  agent to troubleshoot the error correctly 

Model - open ai 
```
---

     
 
all -  [ I want my agent to identify and save important/personal/relevant information to mongodb as i talk to ](https://www.reddit.com/r/LangChain/comments/1cvlhjx/i_want_my_agent_to_identify_and_save/) , 2024-05-22-0910
```
Hi,

So yeah i want the agent to automatically save data, for example, my name, birthday, my friends, emails, events, st
uff like that.

How can I do that, any suggestions would be welcomed!
```
---

     
 
all -  [ remix with langchain and openai ](https://www.reddit.com/r/remixrun/comments/1cvl852/remix_with_langchain_and_openai/) , 2024-05-22-0910
```
So I was trying to create a chatbot in my portfolio web app. The bot reads the json which my portfolio is using and inte
racts with the users if asked anything related to me.
everything working fine in local. but when deployed to vercel. cha
tbot is giving 500
so when I make a api/chat request, it fails but when I refresh the app, I can see the response in the
 log for / request. 
the actual request throwing
type error: nodeResponse. header.raw is not a function
I tried several 
ways but no luck. passed the headers. I googled it but no proper answer.

has anyone integrated it with remixjs before a
nd deployed on vercel?
```
---

     
 
all -  [ Feedback on my AI-powered Black Market? ](https://www.reddit.com/r/LangChain/comments/1cvkdja/feedback_on_my_aipowered_black_market/) , 2024-05-22-0910
```
Hey! 
I developed this experimental shopping experience that allows you to bargain with an AI to get the best deal possi
ble when buying some tees from creative services:
https://blackmarket.creativeservices.shop/
The AI has an embedded pers
onality, preferences, lore etc. and the more you connect with it, the more likely it is that you can get a discount.
I h
eavily used langchain to manage all RAG.

It is experimental, but functional. We are now working on some additional laye
rs to avoid prompt injection and other ai misbehaviors, but I would really love to get some feedback and ideas on how to
 improve it from the community!
```
---

     
 
MachineLearning -  [ [R] Building an Observable arXiv RAG Chatbot with LangChain, Chainlit, and Literal AI ](https://www.reddit.com/r/MachineLearning/comments/1crwh0q/r_building_an_observable_arxiv_rag_chatbot_with/) , 2024-05-22-0910
```
Hey r/MachineLearning, I published a new article where I built an observable semantic research paper application.

This 
is an extensive tutorial where I go in detail about:

1. Developing a RAG pipeline to process and retrieve the most rele
vant PDF documents from the arXiv API.
2. Developing a Chainlit driven web app with a Copilot for online paper retrieval
.
3. Enhancing the app with LLM observability features from Literal AI.

You can read the article here: [https://medium.
com/towards-data-science/building-an-observable-arxiv-rag-chatbot-with-langchain-chainlit-and-literal-ai-9c345fcd1cd8](h
ttps://medium.com/towards-data-science/building-an-observable-arxiv-rag-chatbot-with-langchain-chainlit-and-literal-ai-9
c345fcd1cd8)

Code for the tutorial: [https://github.com/tahreemrasul/semantic\_research\_engine](https://github.com/tah
reemrasul/semantic_research_engine)


```
---

     
 
MachineLearning -  [ [P] LLMinator: A Llama.cpp + Gradio based opensource Chatbot to run llms locally(cpu/cuda) directly  ](https://www.reddit.com/r/MachineLearning/comments/1cpbgd1/p_llminator_a_llamacpp_gradio_based_opensource/) , 2024-05-22-0910
```
Hi I am currently working on a context-aware streaming chatbot based on Llama.cpp, Gradio, Langchain, Transformers. LLMi
nator can pull LLMs directly from HF & run them locally on cuda or cpu.

I am looking for recommendations & help from op
ensource community to grow this further.

**Github Repo:** [https://github.com/Aesthisia/LLMinator](https://github.com/A
esthisia/LLMinator)

**Goal:** To help developers with kickstarter code/tool to run LLMs.

https://preview.redd.it/fnzja
7rjwqzc1.png?width=1846&format=png&auto=webp&s=a62c43614d63e82156fef8722b986b051cc1795b

**Features:**

* Context-aware 
Chatbot.
* Inbuilt code syntax highlighting.
* Load any LLM repo directly from HuggingFace.
* Supports both CPU & Cuda m
odes.
* Load & Offload saved models.
* Command Line Args
* API Access(Soon to be available)

Any review or feedback is a
ppreciated.
```
---

     
 
MachineLearning -  [ [D] Self-optimizing deterministic LLM memory using dspy, neo4j and vector databases. Need your input ](https://www.reddit.com/r/MachineLearning/comments/1cakjaf/d_selfoptimizing_deterministic_llm_memory_using/) , 2024-05-22-0910
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

     
 
deeplearning -  [ Seeking Advice: Solving Data Challenges with Large Language Models (LLMs) ](https://www.reddit.com/r/deeplearning/comments/1ca4nc1/seeking_advice_solving_data_challenges_with_large/) , 2024-05-22-0910
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

     
 
deeplearning -  [ Share the Coolest Out of The Box LLM Applications That Made You Say 'Wow that was smart' ](https://www.reddit.com/r/deeplearning/comments/1c9e6dj/share_the_coolest_out_of_the_box_llm_applications/) , 2024-05-22-0910
```
Hi, I'm looking at some LLM applications today but apart from guys doing big rags with langchain I don't see too many us
es that are out of the box or that make me say 'wow that was smart to use an LLM here'. Have you seen any cool stuff usi
ng LLMs recently that made you say 'wow, that was smart'?
```
---

     
