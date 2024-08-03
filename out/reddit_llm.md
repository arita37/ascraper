 
all -  [ Creating a Knowledge Base for RAG ](https://www.reddit.com/gallery/1eim6mo) , 2024-08-03-0911
```

```
---

     
 
all -  [ Chatbot dev pure python with langchain ](https://www.reddit.com/r/LangChain/comments/1eilbh3/chatbot_dev_pure_python_with_langchain/) , 2024-08-03-0911
```
Hi. I'm new to langchain, literally was only able to learn how to create an llm through bedrock. I'm getting a feeling t
hat it would help me with the chatbot simulating a person we're developing rn but somehow I'm still not sold yet. Right 
now backend is running on Python (aws is accessed via boto3) including ways to fill out the variables in a template prom
pt. About four of the variables are supposed to have two to three sub events with equal chances being instructed to the 
LLM (e.g. equal chance to say 1. he found his wallet he lost yesterday and 2. he cannot find it anymore and he's letting
 go of it). I can code this with Python but I can imagine it would be hard to scale up if say there are already ten scen
arios of five variables. Is there any functionality of langchain framework that can help me with this?

Also, another qu
estion which is probably related or not to langchain as a solution. We are planning to append a whole ass transcript or 
two of what we expect the chat should go. Right now we have two whole transcripts on the main prompt. It seems like it's
 not giving us any issue right now but leads are saying two transcripts aren't enough and we should add more, about thre
e or four for each of the eight intents. Has anyone already tried appending transcripts to their main prompt for chatbot
 and had issues with hallucination? Is there any langchain stuff that could help us with this?

We are using Claude 3.5 
btw via bedrock.
```
---

     
 
all -  [ Can I use Ollama and langchain with api key ? ](https://www.reddit.com/r/LangChain/comments/1eihjbb/can_i_use_ollama_and_langchain_with_api_key/) , 2024-08-03-0911
```
Is there a way to use langchain and Ollama with  with an api key. Similar to how OpenAI works ?

Currently I have Ollama
 running and am able to set up a retrieval chain and query the llm but is there a way to query Ollama with langchain usi
ng an api key ? Cause currently any one on the network can just start using that resource. 
```
---

     
 
all -  [ need help Designing a Persistent Memory Feature for a Chatbot like the chatgpt memory feature ](https://www.reddit.com/r/LangChain/comments/1eigf6i/need_help_designing_a_persistent_memory_feature/) , 2024-08-03-0911
```
so I'm working on a chatbot and I'm trying to implement a feature similar to the memory system used in ChatGPT. 

Here's
 my current idea:

  Whenever the chatbot needs to store new information, it will first pass this data through a functio
n that assesses its similarity to existing memories stored in a vector database. This function will identify the most si
milar match. then, both the new information and the closest match will be fed into a secondary model. that generates a s
tructured object in my case a true or false to  determine whether the new information is truly unique or just a variant 
of what’s already stored. 

The outcome from this model will then dictate whether the i update a memory or insert a new 
one.  i tried just checking the cosine similarity between the embeddings but it was very inconsistent. i am also not kno
wledgeable in NLP so this was all i could think of. i'd like to know if this approach is overkill and if their is an eas
ier way?
```
---

     
 
all -  [ Document Storage in RAG solutions: separate or combined with Vector DB? ](https://www.reddit.com/r/LangChain/comments/1eibcqw/document_storage_in_rag_solutions_separate_or/) , 2024-08-03-0911
```
Hello.  
I'm working on implementing a RAG solution on AWS and I'm curious about best practices for document storage (ch
unks). I'd love to hear about your experiences and preferences.

Specifically, I'm wondering:

1. Do you keep your docum
ent chunks in the same database as your vectors, or do you use separate storage? like S3 object storage? in S3 case you 
need download chunks each time?
2. If you use separate storage, what solution do you prefer? (e.g., S3 buckets, document
 databases, etc.)
3. For those using combined storage, what vector databases are you using that handle this well? I'm pl
anning to use pg\_vector on PostgreSQL
4. How do you handle metadata and linking between vectors and original documents 
in your setup?
5. Any pitfalls or lessons learned you'd be willing to share?

I'm particularly interested in solutions t
hat scale well and remain cost-effective then document collection grows.
```
---

     
 
all -  [ How to return id from db ConvexVectoreStore.fromDocuments ](https://www.reddit.com/r/LangChain/comments/1eib3t3/how_to_return_id_from_db/) , 2024-08-03-0911
```
I use this code for write embeddings in my database:

    const res = await ConvexVectorStore.fromDocuments(splitDocs, e
mbeddings, { ctx });

Logic my app is - get id embedding from db and pass it in Langchain context . But i need get id my
 embeddings from db - variable res don\`t give me this info. How to do this?
```
---

     
 
all -  [ How to implement Weaviate with docker? ](https://www.reddit.com/r/LangChain/comments/1eia9w0/how_to_implement_weaviate_with_docker/) , 2024-08-03-0911
```
I am implementing Weaviate from yesterday with docker on langchain, its tough implementing   
Can anyone share some tuto
rials or is it better as compared to Qdrant
```
---

     
 
all -  [ Tool calling patterns: LangGraph ](https://www.reddit.com/r/LangChain/comments/1ei9rbi/tool_calling_patterns_langgraph/) , 2024-08-03-0911
```
# TLDR

What do you use?

1. Enums as tool parameter arguments
2. Arguments transposed as parameters with their value se
t to Boolean

# How to define a tool/function for LLM

While it is convenient to use the actual function/tool in your co
de to be sent as tool schema to the LLM and receive arguments, it might not be always be ideal. Here are two common exam
ples:

1. Tasks like conditional routing where reasoning is done by an LLM is more dependent on tool definition and less
 code logic.
2. Database Query filtering: The unreliable (multiple points of failure) Text-to-SQL/DSL workload of databa
ses with low complexity and expectations can be abstracted away with premade query with filter parameters of which, argu
ments will be computed by LLM.

How do you define such tools? I see two approaches.

1. Functions with parameter type as
 Enum, which confines the number of possible arguments for that parameter
2. Functions with possible arguments itself as
 parameters, and the actual arguments as boolean value.

Which approach as worked for you and your LLM/system? Are there
 any more things you would like to add?
```
---

     
 
all -  [ How to use AI to search for my stolen bike? ](https://www.reddit.com/r/OpenAI/comments/1ei7so3/how_to_use_ai_to_search_for_my_stolen_bike/) , 2024-08-03-0911
```
Just found out that my bicycle got stolen, most likely last night. I've made a report to the police about it, and search
ed through my neighbourhood. Now I want to try for myself to find it, such as by searching through all of the online mar
ketplaces for my bike, or possibly searching through video camera footage for it, or using a drone to look for it. I fou
nd some online tools for that do this but they don't cover the marketplaces in my area, so I was considering creating an
 AI agent via Langchain possily to do this with one of the new AI models. I haven't done much research or much thought i
nto it yet about what's actually possible, as I only noticed it today that the bike was stolen, so there may be somethin
g obvious that I haven't thought of.

Anyone have any ideas how I can create some kind of application with AI to search 
for my stolen bike?


```
---

     
 
all -  [ Reducing length of State in LangGraph ](https://www.reddit.com/r/LangChain/comments/1ei7fvd/reducing_length_of_state_in_langgraph/) , 2024-08-03-0911
```
Hello, I am building an AI assistant in langgraph and while one of the agents works very fast, the other has issues beca
use of 2 reasons: first one can't be solved as we do need gpt4 for it, while the previously mentioned agent runs on gpt3
.5 turbo, but the other reason is like to tackle is that for this agent, state messages build up very fast very long bec
ause of the amount of tools being used. Is there a way to compress the state or reduce state size to send less tokens to
 the model? Anyone knows?
```
---

     
 
all -  [ We need you! FOSS local machine LLM client ](https://www.reddit.com/r/opensource/comments/1ei640k/we_need_you_foss_local_machine_llm_client/) , 2024-08-03-0911
```
# Hello everyone!

My name is William, and I'm an Italian teenager passionate about computer science. I'm here to ask fo
r help developing my latest project, OpenLocalUI, a local LLM client. The project is based on Ollama and uses Flutter (D
art) for the UI and LangChain for LLM interaction (via a Python gRPC server).

But why work to yet another app to run LL
Ms on your PC, when there are already plenty of alternatives out there? Simple, **to do it better**! There is a somewhat
 paradoxical concept that expresses my goal:

>'Build open-source like closed-source.'

Most FOSS (Free and Open-Source 
Software) share the same issue; while offering powerful tools, the usage of those tools is often convoluted and hidden u
nder layers of poor UI and UX design, which is quite anachronistic! Nowadays, we have all the tools to build better expe
riences (and not just software) for users. It's time to refuse the idea that open-source software is a niche and work to
 help everyone embrace it.

Thanks for reading this far :)

So, did you get inspired? (I hope so!)

If the answer is yes
, take a look at the repository at this [link](https://github.com/WilliamKarolDiCioccio/open_local_ui). My collaborators
 and I will happily greet you on our team to help us build our vision.
```
---

     
 
all -  [ Having problems with filtering by metadata when using MongoDB ](https://www.reddit.com/r/LangChain/comments/1ei4yts/having_problems_with_filtering_by_metadata_when/) , 2024-08-03-0911
```
Hey everyone. I am trying to filter my documents by metadata. I was using ChromaDB and the code below was working just f
ine.

For basic\_retriever:

    basic_retriever = _vector_store.as_retriever(
        search_kwargs={
            'k': 
20,
            'filter': {
                '$and': [
                    {'speaker': {'$eq': 'Participant'}},
         
           {'participant': {'$eq': participant_id}},
                    {'part': {'$in': parts}}
                ]
    
        }
        }
    )

For self\_query\_retriever:

    self_query_retriever = SelfQueryRetriever.from_llm(
        
llm,
        _vector_store,
        metadata_field_info=metadata_field_info,
        document_contents='text',
        v
erbose=True,
        enable_limit=False,
        search_kwargs={
            'filter': {
                '$and': [
     
               {'speaker': {'$eq': 'Participant'}},
                    {'participant': {'$eq': participant_id}},
      
              {'part': {'$in': parts}}
                ]
            }
        },
        context_similarity='context',

    )

However. I had to migrate to MongoDB and the structure above does not work. I tried to follow documentation and d
id these:

For basic retriever:

    basic_retriever = _vector_store.as_retriever(
        search_kwargs={
            '
k': 20,
            'pre_filter': {
                '$and': [
                    {
                        'text': {
  
                          'path': 'speaker',
                            'query': 'Participant'
                        
}
                    },
                    {
                        'text': {
                            'path': 'pa
rticipant',
                            'query': participant_id
                        }
                    },
       
             {
                        'text': {
                            'path': 'part',
                           
 'query': {
                                '$in': parts
                            }
                        }
       
             }
                ]
            }
        }
    )

For self\_query\_retriever:

    self_query_retriever = 
SelfQueryRetriever.from_llm(
        llm,
        _vector_store,
        metadata_field_info=metadata_field_info,
      
  document_contents='text',
        verbose=True,
        enable_limit=False,
        search_kwargs={
            'pre_f
ilter': {
                '$and': [
                    {
                        'text': {
                            
'path': 'speaker',
                            'query': 'Participant'
                        }
                    },
 
                   {
                        'text': {
                            'path': 'participant',
              
              'query': participant_id
                        }
                    },
                    {
           
             'text': {
                            'path': 'part',
                            'query': {
              
                  '$in': parts
                            }
                        }
                    }
           
     ]
            }
        },
        context_similarity='context',
    )

But it does not work. I get the following e
rror:

    PlanExecutor error during aggregation :: caused by :: 'filter[0]' must be a boolean, objectId, number, string
, date, uuid, or null, full error: {'ok': 0.0, 'errmsg': 'PlanExecutor error during aggregation :: caused by :: 'filter[
0]' must be a boolean, objectId, number, string, date, uuid, or null', 'code': 8, 'codeName': 'UnknownError', '$clusterT
ime': {'clusterTime': Timestamp(1722587696, 1), 'signature': {'hash': b''\xb7\x80\xdbA\xc1o\xe0?\x91\xce\x9b\x7f\xbd\xe2
l\xe6\xfc', 'keyId': 7335879767352147970}}, 'operationTime': Timestamp(1722587696, 1)}

Also, I set my vector\_search\_i
ndex like that:

    {
      'fields': [
        {
          'numDimensions': 1536,
          'path': 'embedding',
     
     'similarity': 'cosine',
          'type': 'vector'
        },
        {
          'path': 'timestamp',
          't
ype': 'filter'
        },
        {
          'path': 'speaker',
          'type': 'filter'
        },
        {
       
   'path': 'context',
          'type': 'filter'
        },
        {
          'path': 'participant',
          'type':
 'filter'
        },
        {
          'path': 'metadata.part',
          'type': 'filter'
        }
      ]
    }

Ho
w do I properly filter my metadata?
```
---

     
 
all -  [ Is the poor performance of Gemini on Langchain caused by Langchain or Google? ](https://www.reddit.com/r/LangChain/comments/1ei45mq/is_the_poor_performance_of_gemini_on_langchain/) , 2024-08-03-0911
```
Not sure if I am the only one that notice this, but the performance of Gemini on Langchain has been highly unreliable, a
 few examples:

* Gemini's stream would often just stop midway without ever being completed (making Gemini mostly unusea
ble)
* Can't get the input/output token count after each Gemini API request

Is this a problem on Gemini's side or with 
the Langchain abstraction? Is there an estimated timeline that these issues can be solved?
```
---

     
 
all -  [ Different results with same prompt and LLM but different framework? ](https://www.reddit.com/r/LangChain/comments/1ei1nol/different_results_with_same_prompt_and_llm_but/) , 2024-08-03-0911
```
I am using an LLM that is a fine tuned version of Llama 3 on a cybersecurity dataset that recognises vulnerable code blo
cks and suggests steps to remediates the vulnerablities with fixed code. 

I tried the same LLM and prompt with LangChai
n and Llama CPP but I get different results from each of them. 

In Llama CPP, I get the suggested steps and fixed code 
block but with LangChain (using the Llama CPP abstraction), I get only the steps. 

The prompt format is Llama-Chat 2 an
d the prompt specifically says 'provide a code block that fixes the vulnerability'

```
---

     
 
all -  [ Does anyone have resources to build a Google Gemini agent that can use tools? ](https://www.reddit.com/r/LangChain/comments/1ei08g7/does_anyone_have_resources_to_build_a_google/) , 2024-08-03-0911
```
I think the resources I am coming across are outdated as it says bind_tools not found.
```
---

     
 
all -  [ Using RAG to choose tools vs agents, which is better choices? If accuracy matters ](https://www.reddit.com/r/LangChain/comments/1ehyf74/using_rag_to_choose_tools_vs_agents_which_is/) , 2024-08-03-0911
```
Let's say I have 50 website API endpoints to get the data, and I am going to wrap them inside 50 agents... I'm not sure 
if this is the right way to do, as I'm afraid the agent will possibly messed up when the API endpoints keep growing...


Instead, I am thinking if I could RAG on tools to be used based on the user query, and then trigger those function tool 
based the output returned by RAG... Is this something feasible and perhaps more scalable than agents?

I'm not that sure
 the scalability of agents when there is a lot of data endpoints to access with. Hope for help, thanks.
```
---

     
 
all -  [ Where are you running Langchain in your production apps? (serverless / on the client / somewhere els ](https://www.reddit.com/r/LangChain/comments/1ehwzcr/where_are_you_running_langchain_in_your/) , 2024-08-03-0911
```
I have my existent backend set up as a bunch of serverless functions at the moment (cloudflare workers). I wanted to set
 up a new \`/chat\` endpoint as just another serverless function which uses langchain on the server. But as I get deep i
nto the code I'm not sure if it makes sense to do it this way...

Basically if I have Langchain running on this endpoint
, since servelerless functions are stateless, that means each time the user sends a new message I need to fetch the chat
 history from the database, load it into context, process the request (generate the next response) and then tear it all 
down only to have to build it all up again with the next request. Since there is also no persistent connection.

This al
l seems a bit wasteful in my opinion. If I host langchain on the client I'm thinking I can avoid all this extra work sin
ce the langchain 'instance' will stay put for the duration of the chat session. Once the long context is loaded in memor
y I only need to add new messages to it vs redoing the whole thing which can get very taxing for loooong conversations.


But I would prefer to handle it on the server side to hide the prompt magic 'special sauce' if possible...  
  
How are
 ya'll serving your langchain apps in production?
```
---

     
 
all -  [ RAG with prior knowledge or reference to follow ](https://www.reddit.com/r/LangChain/comments/1ehwxbh/rag_with_prior_knowledge_or_reference_to_follow/) , 2024-08-03-0911
```
So the main idea is that given logs I need RAG to get answers to analyse them. The LLM model works well here upto a leve
l of base knowledge it has been pretrained on. Now I want the answers to be more accurate. So I have a couple of templat
e info and domain knowledge like:  


    Brief scenarios for Registration Cases
    1. 
       -  Registration always b
egins with  REGISTER msg.
       -  REGISTER message is one of the most important message in  protocol and it contains a
 lot of important information in it. Unterstanding the meaning of each parameters in registration would help you greatly
 with various troubleshooting situation. Followings are some of the examples of REGISTER message you may see in the fiel
d. Keep reading this page as often as possible until you become very familiar with all the details of the contents.
    
Blah Blah ....

Now I can give parts of these in the prompts for RAG. (Note: here the vector store contains embeddings o
f my logs). Now the reference gets larger and larger and more sophisticated. I am looking for alternate ways to make sur
e RAG references this domain info before it answers questions on the log vector store. So I can keep expanding this docu
ment of domain knowledge to refer to, and RAG analyses logs based on this domain knowledge.   

```
---

     
 
all -  [ LangChain or Ollama ](https://www.reddit.com/r/LanguageTechnology/comments/1ehufh2/langchain_or_ollama/) , 2024-08-03-0911
```
I'm very new to the field and still trying to get my bearings.

I'm working on a RAG-like application in Python. I chose
 Python because I reasoned that any AI or data science practitioners who join the team are likely to be more familiar wi
th it than a lower-level language.

I believe that my application will benefit from GraphRAG (or its SciPhi Triplex anal
ogue), so I've started transitioning it from its current conventional RAG approach.

Which would be better for this purp
ose--LangChain or Ollama? My current approach uses Ollama for text generation (with my own code handling all of the embe
dding vector elements rather than relying on a vector DB), but I feel that the greater complexity of GraphRAG would bene
fit from the flexibility of LangChain.
```
---

     
 
all -  [ List of FREE and Best Selling Discounted Courses  ](https://www.reddit.com/r/udemyfreebies/comments/1ehtqj2/list_of_free_and_best_selling_discounted_courses/) , 2024-08-03-0911
```
# Udemy Free Courses for 02 August 2024

Note : Coupons might expire anytime, so enroll as soon as possible to get the c
ourses for FREE.

* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/12242/)AWS Certified Cloud Practitioner
* [REDEEM 
OFFER ](https://idownloadcoupon.com/udemy/12229/)NEW AWS Cloud Technology Masterclass
* [REDEEM OFFER ](https://idownloa
dcoupon.com/udemy/12230/)AWS CodePipeline: DevOps CI/CD Masterclass
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/
12231/)Become an AWS Certified Data Engineer
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/12232/)Azure Data Engin
eering-Master 6 Real-World Projects
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/12233/)ChatGPT for Python Data S
cience and Machine Learning
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/12234/)Azure Architect Technologies
* [R
EDEEM OFFER ](https://idownloadcoupon.com/udemy/12235/)AZ-305 – Designing Azure Infrastructure Solutions
* [REDEEM OFFER
 ](https://idownloadcoupon.com/udemy/12236/)Microsoft Excel – Excel from Beginner to Intermediate Level
* [REDEEM OFFER 
](https://idownloadcoupon.com/udemy/12237/)Mastering Figma from 0 to 100 (UI/UX Mastery Course)
* [REDEEM OFFER ](https:
//idownloadcoupon.com/udemy/12238/)Complete Machine Learning,NLP Bootcamp MLOPS & Deployment
* [REDEEM OFFER ](https://i
downloadcoupon.com/udemy/12239/)Complete Generative AI Course With Langchain and Huggingface
* [REDEEM OFFER ](https://i
downloadcoupon.com/udemy/12240/)Drive Real Traffics to your site using Google ,Twitter,Linkd
* [REDEEM OFFER ](https://i
downloadcoupon.com/udemy/12241/)Ultimate Design Patterns
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/12243/)Digi
tal Marketing That Drive Massive Results to Your Service
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/12244/)How 
To Make Money Everyday Using AI ChatGPT /Fiverr.
* Building Gen AI App 12+ Hands-on Projects with Gemini Pro
* [REDEEM O
FFER](https://idownloadcoupon.com/udemy/12245/)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/12227/)Professional 
Diploma in Office Administration Management
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/12226/)How To Use R Prog
ramming for Research
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/12225/)Score Full Mark in (P3O®) Foundation Exa
m – Axelos
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/12224/)TA-002: HashiCorp Terraform Practice Test – 2024
*
 [REDEEM OFFER ](https://idownloadcoupon.com/udemy/12223/)Professional Diploma in Digital Products Management
* [REDEEM 
OFFER ](https://idownloadcoupon.com/udemy/12222/)Score 5 Above target in PMI-SP®Exam
* [REDEEM OFFER ](https://idownload
coupon.com/udemy/12221/)Scoring 5 Above target (PMI-RMP)® Exam
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/12220
/)Cloud Engineer (Google) Practice Test – 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/12219/)JN0-104: Junip
er Networks Internet Practice Test – 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/12218/)200-301: Cisco (CCN
A) Practice Test – 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/12217/)No-Code Machine Learning Using Amazon
 AWS SageMaker Canvas
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/11446/)Cómo Crear una Campaña de Email Marketi
ng Efectiva 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/11298/)Learn UI UX Design Adobe XD : Learn User Exp
erience Design
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/12189/)How to turn your IDEA into a BUSINESS that thr
ives!
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/7320/)Facebook Ads Marketing In Hindi/Urdu 2023
* Fast track F
rench for beginners
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/10791/)
* [REDEEM OFFER ](https://idownloadcoupon
.com/udemy/11488/)Universidad de Elementor Pro, ¡Desde Cero Hasta Experto!
* [REDEEM OFFER ](https://idownloadcoupon.com
/udemy/9697/)Microsoft Azure: Hands On Training: AZ-900 AZ-104 and AZ-305
* [REDEEM OFFER ](https://idownloadcoupon.com/
udemy/45/)PHP for Beginners: PHP Crash Course 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/9296/)C-level man
agement: 100 models for business success
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/11487/)Mastering Email Deli
verability: The Comprehensive Guide
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/10785/)Sales operations: strateg
ies and frameworks for selling more
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/1100/)Google Ads Mastery\~ Begin
ner To Pro \~ HINDI/URDU 2023
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/12214/)Cómo Usar el Creador de Sitios 
Web con IA de Hostinger 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/12215/)Facebook Ads
* [REDEEM OFFER ](h
ttps://idownloadcoupon.com/udemy/12213/)Certified Kubernetes Application Developer (CKAD) – Exams
* [REDEEM OFFER ](http
s://idownloadcoupon.com/udemy/12212/)Learn Camtasia Video Editing Masterclass Professional
* [REDEEM OFFER ](https://ido
wnloadcoupon.com/udemy/12211/)PowerPoint Präsentationen mit KI ChatGPT erstellen
* [REDEEM OFFER ](https://idownloadcoup
on.com/udemy/12210/)Professional Diploma in Project Management
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/12209
/)CISSP: Information Systems Security Practice Test 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/12208/)CISM
: Information Security Manager Practice Test – 2024
* C100DBA: MongoDB Practice Test – 2024
* [REDEEM OFFER](https://ido
wnloadcoupon.com/udemy/12207/)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/12206/)Amazon Afiliados: Cómo Crear u
na Página Web de Nicho 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/12205/)Professional Diploma in Corporate
 Management
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/12204/)Python Project: Build a PDF File Handling Tool fr
om Scratch
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/12203/)AI for Business Strategy
* [REDEEM OFFER ](https:/
/idownloadcoupon.com/udemy/11877/)Build, Host & Manage WordPress Websites using AI \[10Web\]
* [REDEEM OFFER ](https://i
downloadcoupon.com/udemy/6763/)Become a Successful Affiliate Marketer \[Success Blueprint\]
* [REDEEM OFFER ](https://id
ownloadcoupon.com/udemy/4841/)Become a Successful SEO Freelancer & Start Online Businesses
* [REDEEM OFFER ](https://ido
wnloadcoupon.com/udemy/6762/)Build Profitable E-Commerce Stores with WordPress & Woostify
* [REDEEM OFFER ](https://idow
nloadcoupon.com/udemy/6754/)AI x ChatGPT for Productivity 101 \[Masterclass\]
* [REDEEM OFFER ](https://idownloadcoupon.
com/udemy/6750/)AI for Bloggers: SEO, Content Writing & Optimization
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy
/6766/)Build a Profitable Online Courses Business \[Complete Guide\]
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy
/6649/)Complete Microsoft Word Excel PowerPoint Course
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/8692/)AI Vide
o Creation Course 2024: Generate Videos using AI
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/1095/)Marketing en 
Facebook Ads – Leads /Clientes Potenciales 2023
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/12202/)AZ-900: Azure
 Fundamentals Practice Test – 2024
* CISSP: Information System Security Practice Test 2024
* [REDEEM OFFER](https://idow
nloadcoupon.com/udemy/12201/)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/12200/)Complete Ethical Hacking Master
class: Go from Zero to Hero
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/12199/)550 Unix Interview Questions Prac
tice Test
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/12198/)Build, Train
* [REDEEM OFFER ](https://idownloadcou
pon.com/udemy/12197/)CRISC: Risk and Information Systems Practice Test -2024
* [REDEEM OFFER ](https://idownloadcoupon.c
om/udemy/12196/)MO-201: Microsoft Excel Practice Test (Off 2019) – 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/ud
emy/12195/)PCEP (30-02): Entry-Level Python Practice Test – 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/121
94/)SY0-501: CompTIA Security Practice Test – 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/12193/)1Z0-071: O
racle Database SQL Practice Test – 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/12192/)DA-104: Tableau Deskt
op Practice Test – 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/12191/)Executive Diploma in General Manageme
nt
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/5084/)2024 Google Cloud Digital Leader Certification practice Exa
m

GET MORE FREE ONLINE COURSES WITH CERTIFICATE – [CLICK HERE](https://www.reddit.com/r/udemyfreeebies/)
```
---

     
 
all -  [ List of FREE and Best Selling Discounted Courses  ](https://www.reddit.com/r/udemyfreeebies/comments/1ehtqck/list_of_free_and_best_selling_discounted_courses/) , 2024-08-03-0911
```
# Udemy Free Courses for 02 August 2024

Note : Coupons might expire anytime, so enroll as soon as possible to get the c
ourses for FREE.

* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/12242/)AWS Certified Cloud Practitioner
* [REDEEM 
OFFER ](https://idownloadcoupon.com/udemy/12229/)NEW AWS Cloud Technology Masterclass
* [REDEEM OFFER ](https://idownloa
dcoupon.com/udemy/12230/)AWS CodePipeline: DevOps CI/CD Masterclass
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/
12231/)Become an AWS Certified Data Engineer
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/12232/)Azure Data Engin
eering-Master 6 Real-World Projects
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/12233/)ChatGPT for Python Data S
cience and Machine Learning
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/12234/)Azure Architect Technologies
* [R
EDEEM OFFER ](https://idownloadcoupon.com/udemy/12235/)AZ-305 – Designing Azure Infrastructure Solutions
* [REDEEM OFFER
 ](https://idownloadcoupon.com/udemy/12236/)Microsoft Excel – Excel from Beginner to Intermediate Level
* [REDEEM OFFER 
](https://idownloadcoupon.com/udemy/12237/)Mastering Figma from 0 to 100 (UI/UX Mastery Course)
* [REDEEM OFFER ](https:
//idownloadcoupon.com/udemy/12238/)Complete Machine Learning,NLP Bootcamp MLOPS & Deployment
* [REDEEM OFFER ](https://i
downloadcoupon.com/udemy/12239/)Complete Generative AI Course With Langchain and Huggingface
* [REDEEM OFFER ](https://i
downloadcoupon.com/udemy/12240/)Drive Real Traffics to your site using Google ,Twitter,Linkd
* [REDEEM OFFER ](https://i
downloadcoupon.com/udemy/12241/)Ultimate Design Patterns
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/12243/)Digi
tal Marketing That Drive Massive Results to Your Service
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/12244/)How 
To Make Money Everyday Using AI ChatGPT /Fiverr.
* Building Gen AI App 12+ Hands-on Projects with Gemini Pro
* [REDEEM O
FFER](https://idownloadcoupon.com/udemy/12245/)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/12227/)Professional 
Diploma in Office Administration Management
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/12226/)How To Use R Prog
ramming for Research
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/12225/)Score Full Mark in (P3O®) Foundation Exa
m – Axelos
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/12224/)TA-002: HashiCorp Terraform Practice Test – 2024
*
 [REDEEM OFFER ](https://idownloadcoupon.com/udemy/12223/)Professional Diploma in Digital Products Management
* [REDEEM 
OFFER ](https://idownloadcoupon.com/udemy/12222/)Score 5 Above target in PMI-SP®Exam
* [REDEEM OFFER ](https://idownload
coupon.com/udemy/12221/)Scoring 5 Above target (PMI-RMP)® Exam
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/12220
/)Cloud Engineer (Google) Practice Test – 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/12219/)JN0-104: Junip
er Networks Internet Practice Test – 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/12218/)200-301: Cisco (CCN
A) Practice Test – 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/12217/)No-Code Machine Learning Using Amazon
 AWS SageMaker Canvas
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/11446/)Cómo Crear una Campaña de Email Marketi
ng Efectiva 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/11298/)Learn UI UX Design Adobe XD : Learn User Exp
erience Design
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/12189/)How to turn your IDEA into a BUSINESS that thr
ives!
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/7320/)Facebook Ads Marketing In Hindi/Urdu 2023
* Fast track F
rench for beginners
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/10791/)
* [REDEEM OFFER ](https://idownloadcoupon
.com/udemy/11488/)Universidad de Elementor Pro, ¡Desde Cero Hasta Experto!
* [REDEEM OFFER ](https://idownloadcoupon.com
/udemy/9697/)Microsoft Azure: Hands On Training: AZ-900 AZ-104 and AZ-305
* [REDEEM OFFER ](https://idownloadcoupon.com/
udemy/45/)PHP for Beginners: PHP Crash Course 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/9296/)C-level man
agement: 100 models for business success
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/11487/)Mastering Email Deli
verability: The Comprehensive Guide
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/10785/)Sales operations: strateg
ies and frameworks for selling more
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/1100/)Google Ads Mastery\~ Begin
ner To Pro \~ HINDI/URDU 2023
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/12214/)Cómo Usar el Creador de Sitios 
Web con IA de Hostinger 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/12215/)Facebook Ads
* [REDEEM OFFER ](h
ttps://idownloadcoupon.com/udemy/12213/)Certified Kubernetes Application Developer (CKAD) – Exams
* [REDEEM OFFER ](http
s://idownloadcoupon.com/udemy/12212/)Learn Camtasia Video Editing Masterclass Professional
* [REDEEM OFFER ](https://ido
wnloadcoupon.com/udemy/12211/)PowerPoint Präsentationen mit KI ChatGPT erstellen
* [REDEEM OFFER ](https://idownloadcoup
on.com/udemy/12210/)Professional Diploma in Project Management
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/12209
/)CISSP: Information Systems Security Practice Test 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/12208/)CISM
: Information Security Manager Practice Test – 2024
* C100DBA: MongoDB Practice Test – 2024
* [REDEEM OFFER](https://ido
wnloadcoupon.com/udemy/12207/)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/12206/)Amazon Afiliados: Cómo Crear u
na Página Web de Nicho 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/12205/)Professional Diploma in Corporate
 Management
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/12204/)Python Project: Build a PDF File Handling Tool fr
om Scratch
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/12203/)AI for Business Strategy
* [REDEEM OFFER ](https:/
/idownloadcoupon.com/udemy/11877/)Build, Host & Manage WordPress Websites using AI \[10Web\]
* [REDEEM OFFER ](https://i
downloadcoupon.com/udemy/6763/)Become a Successful Affiliate Marketer \[Success Blueprint\]
* [REDEEM OFFER ](https://id
ownloadcoupon.com/udemy/4841/)Become a Successful SEO Freelancer & Start Online Businesses
* [REDEEM OFFER ](https://ido
wnloadcoupon.com/udemy/6762/)Build Profitable E-Commerce Stores with WordPress & Woostify
* [REDEEM OFFER ](https://idow
nloadcoupon.com/udemy/6754/)AI x ChatGPT for Productivity 101 \[Masterclass\]
* [REDEEM OFFER ](https://idownloadcoupon.
com/udemy/6750/)AI for Bloggers: SEO, Content Writing & Optimization
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy
/6766/)Build a Profitable Online Courses Business \[Complete Guide\]
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy
/6649/)Complete Microsoft Word Excel PowerPoint Course
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/8692/)AI Vide
o Creation Course 2024: Generate Videos using AI
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/1095/)Marketing en 
Facebook Ads – Leads /Clientes Potenciales 2023
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/12202/)AZ-900: Azure
 Fundamentals Practice Test – 2024
* CISSP: Information System Security Practice Test 2024
* [REDEEM OFFER](https://idow
nloadcoupon.com/udemy/12201/)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/12200/)Complete Ethical Hacking Master
class: Go from Zero to Hero
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/12199/)550 Unix Interview Questions Prac
tice Test
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/12198/)Build, Train
* [REDEEM OFFER ](https://idownloadcou
pon.com/udemy/12197/)CRISC: Risk and Information Systems Practice Test -2024
* [REDEEM OFFER ](https://idownloadcoupon.c
om/udemy/12196/)MO-201: Microsoft Excel Practice Test (Off 2019) – 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/ud
emy/12195/)PCEP (30-02): Entry-Level Python Practice Test – 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/121
94/)SY0-501: CompTIA Security Practice Test – 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/12193/)1Z0-071: O
racle Database SQL Practice Test – 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/12192/)DA-104: Tableau Deskt
op Practice Test – 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/12191/)Executive Diploma in General Manageme
nt
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/5084/)2024 Google Cloud Digital Leader Certification practice Exa
m

GET MORE FREE ONLINE COURSES WITH CERTIFICATE – [CLICK HERE](https://idownloadcoupon.com/)
```
---

     
 
all -  [ Open Source RAG - best for production? ](https://www.reddit.com/r/LangChain/comments/1ehtdhs/open_source_rag_best_for_production/) , 2024-08-03-0911
```
Hello everyone,

I am currently looking at some opensource RAG such as Langchain and Llama index. Quite like Llama index
 but it does not seem suitable for production. I did not find the capability of doing batch inference especially for ret
rieving the closest chunks for a batch of query. (so lack of scalability here)  
Langchain seems to have this feature (c
orrect me if I am wrong but they are extracting the embeddings of queries by batch and not using multiple workers => one
 embedding model call instead of N call if we have N queries)

I was wondering if there are others open source RAG worth
 for production other than langchain allowing:

* Vector Store
* Chunking & Document upload of different type (pdf, docx
, raw text etc)
* scalability (such as batch for queries => embedding model call made by batch)
* flexible about choosin
g the embedding model (HF, OpenAI etc)
* good feature about the retriever such as filtering from metadata
* good postpro
cess function (or possibility to add custom function) such as chunk merging etc

Thanks for the help!
```
---

     
 
all -  [ How can I run Video-LLaMa ? ](https://www.reddit.com/r/LangChain/comments/1ehsukn/how_can_i_run_videollama/) , 2024-08-03-0911
```
Could someone show me how I can use [https://huggingface.co/DAMO-NLP-SG/Video-LLaMA-2-7B-Finetuned](https://huggingface.
co/DAMO-NLP-SG/Video-LLaMA-2-7B-Finetuned) with Python, please? I am still a beginner. Thank you to those who take the t
ime to answer my question.
```
---

     
 
all -  [ Resume Review ](https://www.reddit.com/r/resumes/comments/1ehpbyu/resume_review/) , 2024-08-03-0911
```
# Please Roast my Resume in Detail. Looking for SDE and MLE roles. I am trying for Full time.
Have received over 450+ re
jections for internships with no interviews currently working a volunteer role 

https://preview.redd.it/yhw5ezjks3gd1.p
ng?width=737&format=png&auto=webp&s=5e3aabd529c431fb31d0d47fe25ee0f9799ef1e2


```
---

     
 
all -  [ Where to store vectors? ](https://www.reddit.com/r/LangChain/comments/1ehpb1d/where_to_store_vectors/) , 2024-08-03-0911
```
When you build RAG, where do you store all the vectors? 

I am using Postgres + pg_vector, and just storing the vectors 
in the same DB as the rest of my application data. It is convenient and works well with my toolchain.

But I also heard 
(without explanation) that it is better to use a separate database for vectors. 

Is this true? Any thoughts on why? Doe
s another Postgres database on the same instance “count”? 
```
---

     
 
all -  [ LangGraph Studio is amazing ](https://www.reddit.com/r/LangChain/comments/1ehp7h5/langgraph_studio_is_amazing/) , 2024-08-03-0911
```
[LangGraph Studio: The first agent IDE (youtube.com)](https://www.youtube.com/watch?v=pLPJoFvq4_M) -- check this out.

J
ust a week back, I was thinking of developing a web app kind of interface for langgraph, and they just launched it. Now,
 what if there were a drag-and-drop-like application for creating a complex graph chain?
```
---

     
 
all -  [ Allowing a real person to 'take over' the conversation? ](https://www.reddit.com/r/LangChain/comments/1ehmxa9/allowing_a_real_person_to_take_over_the/) , 2024-08-03-0911
```
Is anyone working on Conversational technology that allows a third  person to 'take over' the conversation, given the an
swer relevancy confidence is low, with a RAG pipeline?
```
---

     
 
all -  [ Looking for a Video Understanding Model with Commercial Use License ](https://www.reddit.com/r/LangChain/comments/1ehgnig/looking_for_a_video_understanding_model_with/) , 2024-08-03-0911
```
Hello, does anyone know of a model capable of understanding videos and answering my questions via an LLM? Something like
 Video-LLaMA but that allows commercial use? Thank you very much to those who take the time to respond.
```
---

     
 
all -  [ Adding Streaming Support to FastAPI LangChain Application with Agents ](https://www.reddit.com/r/LangChain/comments/1ehggqs/adding_streaming_support_to_fastapi_langchain/) , 2024-08-03-0911
```

I'm working on a production FastAPI application that uses LangChain with a cascade of tools for various AI tasks. I'm l
ooking to add asynchronous streaming support to my API and would appreciate feedback on my proposed design:

## Current 
Setup:
- FastAPI endpoints that use LangChain agents with multiple tools
- Synchronous API calls that return complete re
sponses, including main content and metadata (e.g., sources used)

## Proposed Design:
1. Keep existing synchronous API 
endpoints as-is for backward compatibility
2. Add new streaming endpoints for real-time token generation of the main res
ponse body
3. Use Redis as a message broker to collect and stream responses
4. Synchronous API continues to return full 
response with all fields (main content, sources, etc.)

## Implementation Idea:
- Modify existing endpoints to publish r
esponses to Redis
- Create new streaming endpoints that subscribe to Redis channels
- Update LangChain agents to publish
 chunks and full responses to Redis
- Client can use either sync API for full response or streaming API for real-time up
dates

## Questions:
1. Is this a sensible approach for adding streaming to an existing production API?
2. Are there bet
ter alternatives to using Redis for this purpose?
3. How can I ensure efficient resource usage and low latency with this
 design?
4. Any potential pitfalls or considerations I should be aware of?

I'd greatly appreciate any insights, alterna
tive approaches, or best practices for implementing streaming in a FastAPI LangChain application. Thanks in advance for 
your help!


```
---

     
 
all -  [ How to add specific source from db to RunnableSequence using Langchain ](https://www.reddit.com/r/LangChain/comments/1ehggmb/how_to_add_specific_source_from_db_to/) , 2024-08-03-0911
```
Hello. I use convex and langchain to create my rag application. In my case i need add to context specific data from my d
b - logic my application is serching some embeddings by id from my vectoredb then i use its embeddings for generate answ
er - but if i just add to context from RunnableSequence my embeddings i need use some format or embeddings are enough fo
r this? I dont find this example in langchain documentation

`const vectorStore = new ConvexVectorStore(new OpenAIEmbedd
ings(), { ctx });`  
`const llm = new ChatOpenAI({`  
`apiKey: process.env.OPENAI_API_KEY,`  
`model: 'gpt-3.5-turbo',` 
 
`temperature: 0,`  
`});`  
`const parcer = new StringOutputParser();`  
`const retriever = vectorStore.asRetriever()`
  
`const prompt = await pull<ChatPromptTemplate>('rlm/rag-prompt');`  
`const ragChain = RunnableSequence.from([`  
`{`
  
`context: retriever.pipe(formatDocumentsAsString) ,`  
`question: new RunnablePassthrough(),`  
`},`  
`prompt,`  
`l
lm,`  
`parcer,`  
`]);`
```
---

     
 
all -  [ Multiple turns prompting strategy ](https://www.reddit.com/r/LangChain/comments/1eheoc1/multiple_turns_prompting_strategy/) , 2024-08-03-0911
```
Hello guys,

I have a question concerning how to prompt a model.  
I'm currently using LLaMa 3.1 to interact with a tool
. The model is given an objective and generate multiple rounds of tool input to achieve it.  
Currently i'm simply using
 the following format:

ChatPromptTemplate(\[('system',system\_prompt),('user',user\_prompt)\])  
where user\_prompt con
tains the previous rounds of him generating commands and tool output like this:  
user\_prompt='''  
{prompt}  
previous
 commands executed:{previous\_rounds\_of\_tool\_call}  
'''  
This is inspired of ReAct prompt formatting.

But I'm thin
king about changing that to prompt him in the following format:  
ChatPromptTemplate(\[('system',system\_prompt),('user'
,user\_prompt)  
,('tool',tool\_message),('user',user\_prompt).....\])

adding each turns as separate message.  
I would
 like to know if someone already used that? Does it change something ? How to do the training with multi steps setup lik
e that?simply train each step separately?

Thanks for your advices!
```
---

     
 
all -  [ How to build Production grade Langchain Agents using ReAct
 ](https://www.reddit.com/r/LangChain/comments/1ehcpct/how_to_build_production_grade_langchain_agents/) , 2024-08-03-0911
```
Hi everyone,

ReAct agents are powerful, but I've found a way to make them even better for real-world use. Here's how:


Multi-LLM Integration: I've set up my ReAct agents to work with over 200 different LLMs. This flexibility lets you choos
e the best model for each task.  


Performance Tracking: By monitoring costs, token usage, and latency, I've optimized 
my agents' efficiency. This is crucial for large-scale applications.

Improved Reliability: I've implemented fallbacks b
etween LLMs, load-balancing, and automatic retries. This makes the agents much more stable in production environments.


Smart Caching: By storing frequently accessed data, I've significantly reduced API calls, making the agents faster and m
ore cost-effective.

Detailed Logging: Comprehensive action tracking has been a game-changer for debugging complex ReAct
 runs.

Easy Prompt Management- I can now update prompts without touching the code, which speeds up experimentation and 
optimization.

I've based my implementation on Simon Willison's work. You can find the starting point here: [https://git
.new/ReAct-framework](https://git.new/ReAct-framework)

Has anyone else been working on improving ReAct agents? What cha
llenges have you faced in real-world applications?
```
---

     
 
all -  [ I did not receive the results email from Nvidia generative AI contset. Also the certificate. ](https://www.reddit.com/r/LangChain/comments/1ehajmd/i_did_not_receive_the_results_email_from_nvidia/) , 2024-08-03-0911
```
I participated in the nvidia gen ai contest on June 18th in Korea time, or maybe June 17th in Pacific time.

And I've be
en waiting for today. But the result email and certificate haven't arrived to me. What's the reason?

Or is there anyone
 who is experiencing the same situation as me?

I also talked about this issue in the nvidia developer discord channel, 
but the people involved don't input any chat.
```
---

     
 
all -  [ [For Hire] Experienced backend developer - Java, Spring, Node, Nest, Elastic/Opensearch, Postgres, R ](https://www.reddit.com/r/forhire/comments/1ehai8u/for_hire_experienced_backend_developer_java/) , 2024-08-03-0911
```
Hi there 👋,

I am Anu, a software developer based in Sri Lanka.

Experience:
I have 4 years of experience in backend dev
elopment, primarily in Spring Boot. I also have experience building internal company tools and APIs using Node.JS and Py
thon. 

I have also worked part time as a React.JS developer, for 7 months, and have a decent grasp of frontend developm
ent.

Projects:
An interesting project I have worked on is the research and implementation of a chunking mechanism for a
 RAG application, for the purpose of generating vector embeddings on OpenSearch.

Education:
I have both a Bachelor's de
gree and a Master's degree in Software engineering, where there were modules covering data science and ML concepts.

Tec
hnologies:

Java 8 to 21
Spring boot
Spring
Postgres
Elasticsearch, OpenSearch
React, TypeScript, NextJS
Python
Langchai
n4J
Langchain
AWS
Node.js, Nest.Js

Github:
I dont use GitHub often, and don't have any meaningful projects on there. I 
am willing to take any test or take home (interview) project to prove my skills. I can share the GitHub via DMs if you w
ould still like to see it.

Rates:
Hourly rate (part time) - $15 to $20 per hour
Hourly rate if you like my work and hir
e me full time - starting $20 per hour, my notice period is 2 months for my current job.

Availability:
I am available p
art time on weekdays and full/ any time on weekends.

Thanks 🫡
```
---

     
 
all -  [ How to pass None Type as an input to LangGraph which deployed in LangServe ](https://www.reddit.com/r/LangChain/comments/1eh9wwv/how_to_pass_none_type_as_an_input_to_langgraph/) , 2024-08-03-0911
```
I have been deloyed an langgraph app which running at LangServe. One question is that I have a feature which required hu
man-in-the-loop that's send a None Type to the langgraph, that's the way to continue langgraph execution. I know how to 
do it in Python SDK but still no clues in LangServe client way，which I mimic request with Python `requests` through payl
oads. 

Any good ideas?
```
---

     
 
all -  [ Spoke to 22 LangGraph devs and here's what we found ](https://www.reddit.com/r/LangChain/comments/1eh0ly3/spoke_to_22_langgraph_devs_and_heres_what_we_found/) , 2024-08-03-0911
```
I recently had our AI interviewer speak with 22 developers who are building with LangGraph. The interviews covered vario
us topics, including how they're using LangGraph, what they like about it, and areas for improvement. I wanted to share 
the key findings because I thought you might find it interesting.

# Use Cases and Attractions

LangGraph is attracting 
developers from a wide range of industries due to its versatility in managing complex AI workflows. Here are some intere
sting use cases:

1. **Content Generation:** Teams are using LangGraph to create systems where multiple AI agents collab
orate to draft, fact-check, and refine research papers in real-time.
2. **Customer Service:** Developers are building dy
namic response systems that analyze sentiment, retrieve relevant information, and generate personalized replies with bui
lt-in clarification mechanisms.
3. **Financial Modeling:** Some are building valuation models in real estate that adapt 
in real-time based on market fluctuations and simulated scenarios.
4. **Academic Research**: Institutions are developing
 adaptive research assistants capable of gathering data, synthesizing insights, and proposing new hypotheses within a si
ngle integrated system.

# What Attracts Developers to LangGraph?

1. **Multi-Agent System Orchestration**: LangGraph ex
cels at managing multiple AI agents, allowing for a divide-and-conquer approach to complex problems.'We are working on a
 project that requires multiple AI agents to communicate and talk to one another. LangGraph helps with thinking through 
the problem using a divide-and-conquer approach with graphs, nodes, and edges.' - Founder, Property Technology Startup
2
. **Workflow Visualization and Debugging**: The platform's visualization capabilities are highly valued for development 
and debugging.'LangGraph can visualize all the requests and all the payloads instantly, and I can debug by taking LangGr
aph. It's very convenient for the development experience.' - Cloud Solutions Architect, Microsoft
3. **Complex Problem-S
olving**: Developers appreciate LangGraph's ability to tackle intricate challenges that traditional programming struggle
s with.'Solving complex problems that are not, um, possible with traditional programming.' - AI Researcher, Nokia
4. **A
bstraction of Flow Logic**: LangGraph simplifies the implementation of complex workflows by abstracting flow logic.'\[La
ngGraph helped\] abstract the flow logic and avoid having to write all of the boilerplate code to get started with the p
roject.' - AI Researcher, Nokia
5. **Flexible Agentic Workflows**: The tool's adaptability for various AI agent scenario
s is a key attraction.'Being able to create an agentic workflow that is easy to visualize abstractly with graphs, nodes,
 and edges.' - Founder, Property Technology Startup

# LangGraph vs Alternatives

The most commonly considered alternati
ves were CrewAI and Microsoft's Autogen. However, developers noted several areas where LangGraph stands out:

1. **Handl
ing Complex Workflows:** Unlike some competitors limited to simple, linear processes, LangGraph can handle complex graph
 flows, including cycles.'CrewAI can only handle DAGs and cannot handle cycles, whereas LangGraph can handle complex gra
ph flows, including cycles.' -  Developer
2. **Developer Control:** LangGraph offers a level of control that many find u
nmatched, especially for custom use cases.'We did tinker a bit with CrewAI and Meta GPT. But those could not come even n
ear as powerful as LangGraph. And we did combine with LangChain because we have very custom use cases, and we need to ha
ve a lot of control. And the competitor frameworks just don't offer that amount of, control over the code.' - Founder, G
enAI Startup
3. **Mature Ecosystem:** LangGraph's longer market presence has resulted in more resources, tools, and infr
astructure.'LangGraph has the advantage of being in the market longer, offering more resources, tools, and infrastructur
e. The ability to use LangSmith in conjunction with LangGraph for debugging and performance analysis is a significant di
fferentiator.' -  Developer
4. **Market Leadership:** Despite a volatile market, LangGraph is currently seen as a leader
 in functionality and tooling for developing workflows.'Currently, LangGraph is one of the leaders in terms of functiona
lity and tooling for developing workflows. The market is volatile, and I hope LangGraph continues to innovate and create
 more tools to facilitate developers' work.' - Developer

# Areas for Improvement

While LangGraph has garnered praise, 
developers also identified several areas for improvement:

1. **Simplify Syntax and Reduce Complexity:** Some developers
 noted that the graph-based approach, while powerful, can be complex to maintain.'Some syntax can be made a lot simpler.
' - Senior Engineering Director, BlackRock
2. **Enhance Documentation and Community Resources:** There's a need for more
 in-depth, complex examples and community-driven documentation.'The lack of how-to articles and community-driven documen
tation... There's a lot of entry-level stuff, but nothing really in-depth or complex.' - Research Assistant, BYU
3. **Im
prove Debugging Capabilities:** Developers expressed a need for more detailed debugging information, especially for trac
king state within the graph.'There is a need for more debugging information. Sometimes, the bug information starts from 
the instantiation of the workflow, and it's hard to track the state within the graph.' - Senior Software Engineer, Canad
ian Government Agency
4. **Better Human-in-the-Loop Integration:** Some users aren't satisfied with the current implemen
tation of human-in-the-loop concepts.'More options around the human-in-the-loop concept. I'm not a very big fan of their
 current implementation of that.' - AI Researcher, Nokia
5. **Enhanced Subgraph Integration:** Multiple developers menti
oned issues with integrating and combining subgraphs.'The possibility to integrate subgraphs isn't compatible with \[gra
ph drawing\].' - Engineer, IT Consulting Company 'I wish you could combine smaller graphs into bigger graphs more easily
.' - Research Assistant, BYU
6. **More Complex Examples:** There's a desire for more complex examples that developers ca
n use as starting points.'Creating more examples online that people can use as inspiration would be fantastic.' - Senior
 Engineering Director, BlackRock

\_\_\_\_  
You can check out the interview transcripts here: [kgrid.ai/company/langgra
ph](http://kgrid.ai/company/langgraph)

Curious to know whether this aligns with your experience? 
```
---

     
 
all -  [ RAG PDF Chat + Web Search ](https://www.reddit.com/r/LangChain/comments/1egyn3g/rag_pdf_chat_web_search/) , 2024-08-03-0911
```
Hi guys I have created a PDF Chat/ Web Search RAG application deployed on Hugging Face Spaces https://shreyas094-searchg
pt.hf.space. Providing the model documentation below please feel free to contribute.

# AI-powered Web Search and PDF Ch
at Assistant

This project combines the power of large language models with web search capabilities and PDF document ana
lysis to create a versatile chat assistant. Users can interact with their uploaded PDF documents or leverage web search 
to get informative responses to their queries.

## Features

- **PDF Document Chat**: Upload and interact with multiple 
PDF documents.
- **Web Search Integration**: Option to use web search for answering queries.
- **Multiple AI Models**: C
hoose from a selection of powerful language models.
- **Customizable Responses**: Adjust temperature and API call settin
gs for fine-tuned outputs.
- **User-friendly Interface**: Built with Gradio for an intuitive chat experience.
- **Docume
nt Selection**: Choose which uploaded documents to include in your queries.

## How It Works

1. **Document Processing**
: 
   - Upload PDF documents using either PyPDF or LlamaParse.
   - Documents are processed and stored in a FAISS vector
 database for efficient retrieval.

2. **Embedding**: 
   - Utilizes HuggingFace embeddings (default: 'sentence-transfor
mers/all-mpnet-base-v2') for document indexing and query matching.

3. **Query Processing**:
   - For PDF queries, relev
ant document sections are retrieved from the FAISS database.
   - For web searches, results are fetched using the DuckDu
ckGo search API.

4. **Response Generation**:
   - Queries are processed using the selected AI model (options include Mi
stral, Mixtral, and others).
   - Responses are generated based on the retrieved context (from PDFs or web search).

5. 
**User Interaction**:
   - Users can chat with the AI, asking questions about uploaded documents or general queries.
   
- The interface allows for adjusting model parameters and switching between PDF and web search modes.

## Setup and Usag
e

1. Install the required dependencies (list of dependencies to be added).
2. Set up the necessary API keys and tokens 
in your environment variables.
3. Run the main script to launch the Gradio interface.
4. Upload PDF documents using the 
file input at the top of the interface.
5. Select documents to query using the checkboxes.
6. Toggle between PDF chat an
d web search modes as needed.
7. Adjust temperature and number of API calls to fine-tune responses.
8. Start chatting an
d asking questions!

## Models

The project supports multiple AI models, including:
- mistralai/Mistral-7B-Instruct-v0.3

- mistralai/Mixtral-8x7B-Instruct-v0.1
- meta/llama-3.1-8b-instruct
- mistralai/Mistral-Nemo-Instruct-2407

## Future I
mprovements

- Integration of more embedding models for improved performance.
- Enhanced PDF parsing capabilities.
- Sup
port for additional file formats beyond PDF.
- Improved caching for faster response times.

## Contribution

Contributio
ns to this project are welcome!


```
---

     
 
MachineLearning -  [ [D] Embedding generation in production? How are you doing it? ](https://www.reddit.com/r/MachineLearning/comments/1e7xt6k/d_embedding_generation_in_production_how_are_you/) , 2024-08-03-0911
```


For those building production RAG pipelines, how are you generating embeddings. More than which model, I'm interested 
in how your deploying it. Are you calling the openai/vertex API endpoint directly? Using langchain/llamaindex wrappers? 
Using vectordb  classes? Or some other way?
```
---

     
 
MachineLearning -  [ [D] Is Anyone Else Setting Up Real-Time Django Workers for their AI Application? What's the best way ](https://www.reddit.com/r/MachineLearning/comments/1e0qens/d_is_anyone_else_setting_up_realtime_django/) , 2024-08-03-0911
```
We completely underestimated this one tbh, thought it would be much more straight forward. But we've done it now and doc
umented how step by step [in this article series](https://medium.com/p/5828a1ea43a3).

A bit of context, we're building 
a mini free AI Agent that auto-generates manually customisable plots, so the user can basically style however they want.
 It needs to be cost effective and efficient, so we thought about how to do it and tested a couple other ways.

https://
preview.redd.it/cmly0a6bhwbd1.png?width=640&format=png&auto=webp&s=be1f5b2853e744adcaf8013e6d43b43f6be89617

We plan on 
releasing the project open source, so all feedback welcome! Is anyone else doing this and has any feedback? or do know o
f a better way to do it?
```
---

     
 
MachineLearning -  [ [P] Real Time AI Workers Web Application ](https://www.reddit.com/r/MachineLearning/comments/1dzryk9/p_real_time_ai_workers_web_application/) , 2024-08-03-0911
```
Hi everyone!

I've created a mini series on how to build a real time AI application using Django, LangChain and Celery.


Free knowledge - posting it in here for anyone working on something similar and had the same blockers I had when buildi
ng.

Let me know what you think on how I could potentially improve this architecture.

Part 1

[https://medium.com/towar
dsdev/how-to-set-up-django-from-scratch-with-celery-channels-redis-docker-real-time-django-601dff7ada79](https://medium.
com/towardsdev/how-to-set-up-django-from-scratch-with-celery-channels-redis-docker-real-time-django-601dff7ada79)

Part 
2

[https://medium.com/towardsdev/how-to-set-up-django-from-scratch-with-celery-channels-redis-docker-real-time-django-5
828a1ea43a3](https://medium.com/towardsdev/how-to-set-up-django-from-scratch-with-celery-channels-redis-docker-real-time
-django-5828a1ea43a3)

Part 3

[https://medium.com/towardsdev/how-to-set-up-django-from-scratch-with-celery-channels-red
is-docker-real-time-django-8e73c7b6b4c8](https://medium.com/towardsdev/how-to-set-up-django-from-scratch-with-celery-cha
nnels-redis-docker-real-time-django-8e73c7b6b4c8)

Part 4

[https://medium.com/towardsdev/how-to-set-up-django-from-scra
tch-with-celery-channels-redis-docker-real-time-django-c090c300517a](https://medium.com/towardsdev/how-to-set-up-django-
from-scratch-with-celery-channels-redis-docker-real-time-django-c090c300517a)

Part 5  
[https://medium.com/@cubode/how-
to-set-up-django-from-scratch-with-celery-channels-redis-docker-real-time-django-0845eb7e083c](https://medium.com/@cubod
e/how-to-set-up-django-from-scratch-with-celery-channels-redis-docker-real-time-django-0845eb7e083c)
```
---

     
