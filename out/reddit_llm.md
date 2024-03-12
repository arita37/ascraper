 
all -  [ Why does this code give an error, seems to be a problem with the langchain package but I'm following ](https://www.reddit.com/r/LangChain/comments/1bcdld0/why_does_this_code_give_an_error_seems_to_be_a/) , 2024-03-12-0909
```
    'import os
    from PyPDF2 import PdfReader
    from dotenv import load_dotenv
    from PyPDF2 import PdfReader
    
from langchain.vectorstores import FAISS
    from langchain.embeddings.openai import OpenAIEmbeddings
    from langchain
.chat_models import ChatOpenAI
    from langchain.chains.question_answering import load_qa_chain
    from langchain.text
_splitter import CharacterTextSplitter
    
    class LLM:
        def init(self, llm_input_file):
            load_dote
nv()
            self.key = os.getenv('OPENAI_API_KEY')
            self.llm_input_file = llm_input_file
            sel
f.process_embeddings()
            pass
        def process_embeddings(self):
            pdfreader = PdfReader(self.llm
_input_file)
            raw_text = ''
            for i, page in enumerate(pdfreader.pages):
                content = 
page.extract_text()
                if content:
                    raw_text += content
            text_splitter = Char
acterTextSplitter(
                separator='\n',
                chunk_size=800,
                chunk_overlap=200,
  
              length_function=len,
            )
            self.texts = text_splitter.split_text(raw_text)
           
 self.embeddings = OpenAIEmbeddings()
            self.document_search = FAISS.from_texts(self.texts, self.embeddings)
 
           self.chain = load_qa_chain(ChatOpenAI(), chain_type='stuff')
        def prompt(self, user_question):
       
     if user_question is not None and user_question != '':
                docs = self.document_search.similarity_search
(user_question)
                response = self.chain.run(input_documents=docs, question=user_question)
                
return response.to_md()
    '

The error says the problem lies in self.document\_search = FAISS.from\_texts(self.texts, 
self.embeddings)
```
---

     
 
all -  [ Azure Search provider ](https://www.reddit.com/r/LangChain/comments/1bcchol/azure_search_provider/) , 2024-03-12-0909
```
Why Lanchain provider wants me to create an index with some predefined metadata? (otherwise I have an error)
The underly
ing SDK doesn't require that at all...
```
---

     
 
all -  [ Code Embeddings? ](https://www.reddit.com/r/LangChain/comments/1bcbqqv/code_embeddings/) , 2024-03-12-0909
```
Are there examples anywhere on how to use an embedding scheme for code? I see that OpenAI and HuggingFace, at least, off
er such embeddings, but I'm having a hard time determining how to use them.  Probably I'm just not doing well enough at 
searching the web, so pointers would be very welcome.  For example, [this page](https://python.langchain.com/docs/use\_c
ases/code\_understanding) uses only vanilla OpenAI embeddings.
```
---

     
 
all -  [ Example of langchain that uses  ](https://www.reddit.com/r/LangChain/comments/1bc9t6e/example_of_langchain_that_uses/) , 2024-03-12-0909
```
Hi all I am trying to build a sales assistant bot in a startup where if I issue command say '/prospect acmecorp' the age
nt should  1/. Fetch Details from web search about a company 2/. Use a sales playbook knowledge (details of product and 
how to position the product) and generate response about the company and how to position the product. I have been trying
 to find examples which shows how we search and a knowledge can be combined in langchain. Pls if anyone has any insights
 pls help. 
```
---

     
 
all -  [ OpenAI Tools Agent for Open Records Q&A ](https://www.reddit.com/r/LangChain/comments/1bc951u/openai_tools_agent_for_open_records_qa/) , 2024-03-12-0909
```
Wanted to share an experiment I've been working on to test how helpful LLMs could be in answering user questions about O
pen Records (state-level FOIA laws). A basic [demo is available here](https://huggingface.co/spaces/jscotthorn/kora-assi
stant) with cached example questions and responses. An OpenAI account and key are required to perform new queries.   



The AI Agent is given the user's question, some grounding context in our open records law, and a list of tools provided 
to the Agent if it wants to query for additional context. Tools currently available:

* It can look up the full text of 
a statute from the Kentucky Open Records Act
* Look up the full text or summary of an exception from the Act or one inco
rporated from state or federal law (i.e. FERPA, HIPAA).
* Semantic search (chroma db) against case law annotations from 
the Open Records section of the Kentucky Revised Statutes.
* Semantic search against attorney general opinion summaries 
from the Open Records section of the KRS.

Overall the results have been very promising. Observed responses have been la
rgely accurate, and observed inaccuracies have been due to problematic summaries in annotations.
```
---

     
 
all -  [ Please roast my resume , ghosted from everywhere I apply ](https://i.redd.it/52qh99w3iqnc1.jpeg) , 2024-03-12-0909
```
Help me make it better or make me cry by roasting it

:)
```
---

     
 
all -  [ Loading all logs as a dataset to be processed by a LLM for log querying. Is langchain suitable?  ](https://www.reddit.com/r/LangChain/comments/1bc72wo/loading_all_logs_as_a_dataset_to_be_processed_by/) , 2024-03-12-0909
```
I want to load the load the logs as a dataset for the LLM to ask it which transactions take the longest time or have the
 highest latency having a chatbot answer all my log related questions. Would using langchain be my best option ? 
```
---

     
 
all -  [ Recommendations for easy to follow guides to set up with Code Llama ?  ](https://www.reddit.com/r/LangChain/comments/1bc6dhk/recommendations_for_easy_to_follow_guides_to_set/) , 2024-03-12-0909
```
Trying to build a solution that can query logs (like which transactions have the highest latency )so wanted to ask for r
ecommendations for the best LLM to use leaning towards code Llama and if something can suggest easy to follow guides to 
set everything up because the ones I found were incomplete. Thank you! 
```
---

     
 
all -  [ Build a SaaS Rag system ](https://www.reddit.com/r/Startup_Ideas/comments/1bc69sr/build_a_saas_rag_system/) , 2024-03-12-0909
```
AI is a hot topic right now; everyone is building some API integration with OpenAI, However, there is still plenty of ro
om for new players.

One product you can potentially build is a RAG-based chatbot or API. Take any industry where they h
ave to sift through and read hundreds of documents and build a quick lookup using RAG.

A RAG search would take in the u
ser's question and find similar matching documents. From this refined data, you post to an LLM like 'chatgpt-turbo' or '
Mixtral' and the LLM responds with relevant information based on the documents as context.

To build such a system, you 
going to need Langchain and probably Redis or Qdrant or some other vector DB.

Comment down below if you would like some
 example code. 
```
---

     
 
all -  [ How to build a multi AI agents chatbot ](https://www.reddit.com/r/LangChain/comments/1bc5h1b/how_to_build_a_multi_ai_agents_chatbot/) , 2024-03-12-0909
```
Hey guys, I have a question hoping someone can help me with.

I have been given a task to build an AI chatbot which woul
d consist of 3 AI agents. 

The 1st AI agent will be a general Q&A between the (human) user and this 1st LLM where the (
human) user can ask any general natural language questions to this 1st LLM and this 1st LLM will response back in natura
l language answers.

The 2nd AI agent will specialize in converting natural language questions by the (human) user into 
SQL code (when the (human) user include the word “table” in his/her natural language question). This SQL code will then 
be send to a Postgres database to return a table and the AI chatbot will display this table.

Below this table, the 3rd 
AI agent will automatically produce a natural language summary of the information contained in the table.

I am also wan
ting to use the 1st LLM (I don’t think I need a 4th LLM here) to be able to allow the (human) user to ask natural langua
ge questions of the displayed tables on top and the 1st LLM will provide a natural language answer based on the table.


My question is will AI agent framework libraries like Autogen allow me to create the AI chatbot above, which is a conver
sation style chatbot? My AI chatbot also has a front end web app.

If Autogen isn’t able to do this, are there any other
 frameworks that can do the AI chatbot above? Or if there isn’t any framework libraries available, which mean I need to 
code this from scratch, are there any example codes I can refer to?

Would really appreciate if anyone can help. Many th
anks in advance!
```
---

     
 
all -  [ How do you deploy langchain for RAG on aws? ](https://www.reddit.com/r/LangChain/comments/1bc3s9w/how_do_you_deploy_langchain_for_rag_on_aws/) , 2024-03-12-0909
```
I’m setting up a rack system on my companies AWS cloud. So then I confused about is the Lang Chang and other libraries l
ike it are pretty big! The initial idea that I had was to make a small lambda that would ingest hundreds or thousands of
 documents from an S3 bucket, use another API, like open AI to get the embedding, and then upload that to our vector dat
abase.

You should running into is that Lang chain is about 50 MB and running in a lambda is inconvenient.  Trying to zi
p that is a pain, and then making a docker image even with the aws lambda python runtime bumps it to 8.5 GB image size. 


It seems like the only reasonable thing to do is to make a doctor image here and run it in a container. But that kind 
of defeats the purpose of an ingestion pipeline that is able to go dormant. 

I’d love your thoughts. My point is that o
nce you go to productionalize some kind of ingestion pipeline, Langchain just seems too big and tries to do too much.
```
---

     
 
all -  [ Frustrated with inconsistent LLM outputs. Is there a better way to evaluate? ](https://www.reddit.com/r/LangChain/comments/1bc2a7n/frustrated_with_inconsistent_llm_outputs_is_there/) , 2024-03-12-0909
```
I have been working on this LLM project for a while now, and I'm battling inconsistent outputs.  Sometimes it gives me e
xactly what I'm looking for, but other times it goes way off track.  It's making it really difficult to trust the model 
and actually use it in production.

Is anyone else out there struggling with this?  Are there any good tools or techniqu
es for evaluating LLMs and making sure they're performing consistently?

Looking for some advice here. Thank you!
```
---

     
 
all -  [ How you find langchain so far? ](https://www.reddit.com/r/LangChain/comments/1bc1hko/how_you_find_langchain_so_far/) , 2024-03-12-0909
```
Started experimenting with LLM apis and slowly figured that I need a proper framework to deal with it

E.g. 
managing my
 input prompts. 
managing actions when reason for completion is not EOS token etc.

Hence I'm here looking for suggestio
ns.

How's langchain as a framework? How's your experience with it?

Looking through the docs, it feels very complicated
 to do a simple task.

E.g. mapreduce and collapse map reduce, reading through the docs and I find it difficult to figur
e out what the backend is doing.

Maybe I'm wrong and have not dealt with LLM long enough to make a good assessment. Wha
t's your thoughts and how's your experience?
```
---

     
 
all -  [ Adding a JSONOutputParser to a RunnableBinding ](https://www.reddit.com/r/LangChain/comments/1bbzoj7/adding_a_jsonoutputparser_to_a_runnablebinding/) , 2024-03-12-0909
```
I have created a retrieval chain which is of the type RunnableBinding, it's the following example: [https://api.python.l
angchain.com/en/latest/chains/langchain.chains.retrieval.create\_retrieval\_chain.html#langchain.chains.retrieval.create
\_retrieval\_chain](https://api.python.langchain.com/en/latest/chains/langchain.chains.retrieval.create_retrieval_chain.
html#langchain.chains.retrieval.create_retrieval_chain)

&#x200B;

My problem is that I want to add a JSONOutputParser, 
but I cannot seem to figure out how to do that. Does anyone have any ideas about that?
```
---

     
 
all -  [ Langchain updates is disappointing ](https://www.reddit.com/r/LangChain/comments/1bbzaag/langchain_updates_is_disappointing/) , 2024-03-12-0909
```
i just bought course from udemy [https://www.udemy.com/course/langchain-with-python-bootcamp](https://www.udemy.com/cour
se/langchain-with-python-bootcamp) , the course is very well structures all modules are on their place but the problem i
s langchain keeps depricating or updating now i am just on section 1 and already llm and chatmodel is being updated and 
you need to install specific llm like openai so i really need to take this course since its very well structured but i a
lso want to keep up with the updates how would you do that ?
```
---

     
 
all -  [ Combining queries ? ](https://www.reddit.com/r/LangChain/comments/1bbza6x/combining_queries/) , 2024-03-12-0909
```
Hi I'm new here 

I do have a question concerning semantic search 
Let's say I have 2 search queries or more ( User prom
pt + other additional context ) and I wanna search my vector database .

Is it better to combine the strings then embed 
them into one vector then do the search ?

Or embed each element of the query alone then combine all the embeddings into
 one vector then apply a search ? 
```
---

     
 
all -  [ I want to deploy a chatbot that uses rag with the llama index. ](https://www.reddit.com/r/LangChain/comments/1bbyvv8/i_want_to_deploy_a_chatbot_that_uses_rag_with_the/) , 2024-03-12-0909
```
Has anyone already implemented it?

I want to create and distribute a chatbot that uses rag with the llama index.

What 
frameworks should I use to implement a chatbot using rag while considering deployment?

If anyone has already implemente
d it, can you share the git code?
```
---

     
 
all -  [ stream llm model' huggingface' locally ](https://www.reddit.com/r/LangChain/comments/1bbxvvl/stream_llm_model_huggingface_locally/) , 2024-03-12-0909
```
is there any method to stream these models, and output the generated token while it generate to make response live to us
er
```
---

     
 
all -  [ AI & Elixir: How is the experience working with AI apps in elixir ? ](https://www.reddit.com/r/elixir/comments/1bbx48v/ai_elixir_how_is_the_experience_working_with_ai/) , 2024-03-12-0909
```
Hey there, Elixir enthusiasts!

How's everyone doing? I've been thinking a lot about the exciting blend of AI and Elixir
 lately and figured, who better to chat with than all of you? 😊 Are any of you currently dabbling in AI within your Elix
ir projects? If so, I'd love to hear about your experiences! Whether it's overcoming challenges or discovering cool new 
tools, let's swap stories and ideas on how to make the most of AI in our Elixir adventures!

BTW, I want to share my rec
ent endeavor with LangChain by Mark Ericksen. I've been diving into LangChain recently and I have to say, Mark Ericksen'
s work in bringing it to Elixir is impressive! I've actually integrated the library into my personal trading app and it'
s been fantastic. I even whipped up a handy helper Agent that can give you a quick rundown of your portfolio information
.

code : [Agent code](https://github.com/pkrawat1/angel-trading/blob/master/lib/angel_trading/agent.ex)  
Check out the
 demo here!  
[LOOM DEMO](https://www.loom.com/share/c2e677e8f2bb460e9acf9701eecbaced)
```
---

     
 
all -  [ Using Multiple Tools ](https://www.reddit.com/r/LangChain/comments/1bbx1mj/using_multiple_tools/) , 2024-03-12-0909
```
Hi Everyone ,  I am in a fix and need your help. I am building a langchain agent to select between multiple tools depend
ing in the user query. Currently I have two tools - one which reads a SQL database and other which reads an excel. The p
roblem is none of them are working and giving any input as such. 

I am following this exactly--

https://python.langcha
in.com/docs/use_cases/tool_use/multiple_tools
```
---

     
 
all -  [ Improving RAG using LangGraph  ](https://www.reddit.com/r/LangChain/comments/1bbwehs/improving_rag_using_langgraph/) , 2024-03-12-0909
```
Hey everyone, checkout this tutorial on basics of LangGraph and how it can be used to improve RAG based on custom criter
ia

https://youtu.be/TlZ5BFx_m3M?si=8QCUxYpa8jxySkDJ

```
---

     
 
all -  [ Rag application for text and images ](https://www.reddit.com/r/LangChain/comments/1bbwb82/rag_application_for_text_and_images/) , 2024-03-12-0909
```
 I have a use case where i got 100's of documents. I have implemented a rag for answering question related to text but t
he problem is my requirement extends to images also. The documents contains steps for some process. These steps have som
e text and followed by some image. The application i am trying to implement should behave in a way that, if asked any qu
estion about the process it should not only give me the steps but also the images corresponding to it. (have to maintain
 the order of the images)

For ex:

Step 1: \_\_\_ some text \_\_\_  
respective image for step 1

Step 2: \_\_\_ some t
ext \_\_\_  
respective image for step 2

and so on.

How do you even do this, is it possible?
```
---

     
 
all -  [ What is LangChain and how does it aim to revolutionize language learning and communication? ](https://www.reddit.com/r/u_fxdatalabs_Yp/comments/1bbw70j/what_is_langchain_and_how_does_it_aim_to/) , 2024-03-12-0909
```
 

# What is LangChain and how does it aim to revolutionize language learning and communication?

 

## Revolutionizing 
Language Learning with LangChain! 🌐🔗

 

## Introduction:

In today's [**interconnected**](https://fxdatalabs.com/) worl
d, the ability to communicate effectively across [**languages**](https://fxdatalabs.com/) is more important than ever.


However, traditional [**language**](https://fxdatalabs.com/) learning methods often fall short in providing learners wit
h the tools and resources needed to [**master**](https://fxdatalabs.com/) a new language efficiently.

Enter LangChain –
 a revolutionary platform poised to [**transform**](https://fxdatalabs.com/) language learning and [**communication**](h
ttps://fxdatalabs.com/) as we know it.

In this detailed article, we will explore the [**concept**](https://fxdatalabs.c
om/) of LangChain, its innovative features, and how it aims to revolutionize language learning and [**communication**](h
ttps://fxdatalabs.com/) for [**learners**](https://fxdatalabs.com/) around the globe.

### Understanding the Need for La
nguage Learning Innovation:

In a globalized world where [**businesses**](https://fxdatalabs.com/) operate across border
s, travelers explore new cultures, and individuals seek to connect with people from diverse [**backgrounds**](https://fx
datalabs.com/), proficiency in multiple [**languages**](https://fxdatalabs.com/) has become a valuable skill.

However, 
[**traditional**](https://fxdatalabs.com/) language learning methods, such as textbooks and classroom instruction, often
 lack engagement, [**personalization**](https://fxdatalabs.com/), and real-world relevance, making it challenging for le
arners to achieve fluency and [**confidence**](https://fxdatalabs.com/) in their target [**language**](https://fxdatalab
s.com/).

### Introducing LangChain:

LangChain is a cutting-edge language learning [**platform**](https://fxdatalabs.co
m/) that leverages the power of technology, [**artificial intelligence**](https://fxdatalabs.com/), and community collab
oration to [**provide**](https://fxdatalabs.com/) learners with an immersive and personalized language [**learning**](ht
tps://fxdatalabs.com/) experience.

Unlike traditional methods, [**LangChain**](https://fxdatalabs.com/) adopts a holist
ic approach that integrates language learning with real-world communication [**scenarios**](https://fxdatalabs.com/), cu
ltural immersion, and peer-to-peer [**interaction**](https://fxdatalabs.com/), enabling learners to develop language ski
lls that are practical, relevant, and applicable in [**everyday life**](https://fxdatalabs.com/).

## Key Features of La
ngChain:

📷

### Personalized Learning Paths:

LangChain utilizes AI-driven [**algorithms**](https://fxdatalabs.com/) to
 assess each learner's proficiency level, learning preferences, and goals, allowing for the creation of [**personalized*
*](https://fxdatalabs.com/) learning paths tailored to [**individual**](https://fxdatalabs.com/) needs. Whether a beginn
er seeking to master basic vocabulary or an advanced learner aiming for [**fluency**](https://fxdatalabs.com/), LangChai
n adapts to each learner's unique [**requirements**](https://fxdatalabs.com/), pacing, and interests.

### Interactive L
anguage Exercises:

LangChain offers a diverse range of [**interactive**](https://fxdatalabs.com/) language exercises, i
ncluding listening comprehension, speaking practice, reading [**comprehension**](https://fxdatalabs.com/), and writing [
**exercises**](https://fxdatalabs.com/).

These exercises are [**designed**](https://fxdatalabs.com/) to simulate real-w
orld communication scenarios, such as ordering food in a restaurant, making travel [**arrangements**](https://fxdatalabs
.com/), or participating in business meetings, [**providing**](https://fxdatalabs.com/) learners with practical language
 skills that can be [**applied**](https://fxdatalabs.com/) in various contexts.

📷

### Cultural Immersion Experiences:


In addition to language instruction, LangChain [**provides**](https://fxdatalabs.com/) learners with opportunities for 
cultural immersion [**experiences**](https://fxdatalabs.com/), such as virtual tours of iconic landmarks, virtual langua
ge exchanges with native speakers, and [**multimedia**](https://fxdatalabs.com/) content showcasing the rich cultural he
ritage of the target [**language**](https://fxdatalabs.com/).

By [**immersing**](https://fxdatalabs.com/) learners in t
he cultural context of the language, LangChain enhances their understanding, [**appreciation**](https://fxdatalabs.com/)
, and fluency in the language.

### Community Collaboration and Peer Support:

LangChain fosters a vibrant [**community*
*](https://fxdatalabs.com/) of language learners, educators, and native speakers who collaborate, share resources, and [
**support each**](https://fxdatalabs.com/) other's language [**learning**](https://fxdatalabs.com/) journey.

Through fe
atures such as [**language**](https://fxdatalabs.com/) exchange forums, peer tutoring sessions, and collaborative projec
ts, learners can engage with like-minded [**individuals**](https://fxdatalabs.com/), practice their language skills, and
 receive [**feedback**](https://fxdatalabs.com/) and encouragement from peers and mentors.

## Advantages of LangChain:


📷

### Flexibility and Convenience:

With LangChain, learners have the [**flexibility**](https://fxdatalabs.com/) to st
udy anytime, anywhere, using their [**preferred**](https://fxdatalabs.com/) device – whether it's a smartphone, tablet, 
or computer. This flexibility allows learners to integrate language [**learning**](https://fxdatalabs.com/) into their b
usy schedules and progress at their own pace.

### Engagement and Motivation:

LangChain's interactive [**exercises**](h
ttps://fxdatalabs.com/), cultural immersion experiences, and community collaboration features enhance learner [**engagem
ent**](https://fxdatalabs.com/) and motivation, keeping learners inspired and motivated to continue their language learn
ing [**journey**](https://fxdatalabs.com/).

### Real-World Relevance:

By focusing on practical [**communication**](htt
ps://fxdatalabs.com/) skills and real-world scenarios, LangChain equips learners with language skills that are [**immedi
ately**](https://fxdatalabs.com/) applicable in everyday life, ensuring that learners feel confident and competent in us
ing the [**language**](https://fxdatalabs.com/) in real-[**world situations**](https://fxdatalabs.com/).

### Personaliz
ation and Adaptability:

[**LangChain's**](https://fxdatalabs.com/) AI-driven algorithms ensure that each learner receiv
es personalized instruction and feedback based on their [**individual**](https://fxdatalabs.com/) needs, preferences, an
d progress, maximizing [**learning**](https://fxdatalabs.com/) outcomes and effectiveness.

### Case Studies and Testimo
nials:

Highlighting success stories and [**testimonials**](https://fxdatalabs.com/) from LangChain users can provide re
al-world examples of how the platform has transformed their [**language**](https://fxdatalabs.com/) learning [**experien
ce**](https://fxdatalabs.com/) and helped them achieve their language proficiency goals.

Whether it's landing a job in 
a foreign country, making [**friends**](https://fxdatalabs.com/) from diverse cultural backgrounds, or traveling with [*
*confidence**](https://fxdatalabs.com/), these testimonials serve as compelling evidence of [**LangChain's**](https://fx
datalabs.com/) effectiveness and impact.

📷

## Conclusion:

LangChain represents a [**paradigm**](https://fxdatalabs.co
m/) shift in the field of language learning, offering a comprehensive, personalized, and engaging [**approach**](https:/
/fxdatalabs.com/) that empowers learners to master new [**languages**](https://fxdatalabs.com/) with confidence and flue
ncy.

By leveraging technology, artificial intelligence, and [**community**](https://fxdatalabs.com/) collaboration, Lan
gChain is [**revolutionizing**](https://fxdatalabs.com/) language learning and communication, making language acquisitio
n more accessible, effective, and [**enjoyable**](https://fxdatalabs.com/) for learners around the world.

Whether you'r
e a beginner embarking on your [**language**](https://fxdatalabs.com/) learning journey or an [**advanced**](https://fxd
atalabs.com/) learner seeking to refine your skills, LangChain provides the tools, resources, and support needed to [**a
chieve**](https://fxdatalabs.com/) your language learning goals and unlock new opportunities for personal and profession
al [**growth**](https://fxdatalabs.com/).

With [**LangChain**](https://fxdatalabs.com/), the world is yours to explore 
– one [**language**](https://fxdatalabs.com/) at a time.

For more insights into AI|ML and Data Science [**Development**
](https://fxdatalabs.com/), please write to us at: [**contact@htree.plus**](mailto:contact@htree.plus)| [**F(x) Data Lab
s Pv**](mailto:contact@htree.plus)[**t. Ltd.**](https://fxdatalabs.com/)

[**#LangChain #LanguageLea**](https://fxdatala
bs.com/)rning #CommunicationRevolution #GlobalConnectivity 🚀🌍
```
---

     
 
all -  [ LangChain vs LlamaIndex ](https://www.reddit.com/r/LangChain/comments/1bbog83/langchain_vs_llamaindex/) , 2024-03-12-0909
```
Sorry for the oversimplified question but can someone explain the differences between the two?

Do they offer the same s
ort of capabilities but in a different way? It seems that LangChain is preferred when designing RAG applications, is tha
t true and why? What about ReAct?

Which one is more applicable for special purpose business use cases?

Also as an expe
rienced engineer but new to LLMs where should I start learning? Huggingface seems to have a lot of material, is that any
 good

Thanks

```
---

     
 
all -  [ use existing faiss index in LangChain ](https://www.reddit.com/r/LangChain/comments/1bbk7iu/use_existing_faiss_index_in_langchain/) , 2024-03-12-0909
```
Hi All, I wonder if it is possible to load existing indexes built by the faiss library into LangChain?  It seems that th
e format is different and I couldn't just load it like in the example shown in the LangChain documentation, e.g., FAISS.
load\_local('large.index', embeddings)

Thanks!
```
---

     
 
all -  [ Are all embeddings just bad for retrieval? ](https://www.reddit.com/r/LangChain/comments/1bbj5hu/are_all_embeddings_just_bad_for_retrieval/) , 2024-03-12-0909
```
[https://huggingface.co/spaces/mteb/leaderboard](https://huggingface.co/spaces/mteb/leaderboard)

I'm an experienced sof
tware engineer building a practice RAG stack application to learn more about integrating with LLMs. As is standard for t
his, I was going to take my data, convert it into embeddings, store it in a vector DB (Milvus), and then leverage it for
 the ultimate tasks I will be performing.

Looking at the above benchmarks, however, gives me pause. I've been trying to
 understand the scores, I THINK they are percentages. Classification accuracy seems quite high, which is good given that
's the primary task I ultimately want to perform. However, Retrieval seems much lower.

Basically, the highest Classific
ation score in those benchmarks is 79.46, whereas the highest Retrieval score is 59. Those are not in the same model, bt
w. I'm ignoring price, performance, and other factors right now to focus on this single issue.

My core point is that a 
\~60% accuracy at Retrieval seems like it's very bad for Classification, or literally any other task. In RAG, the goal i
s to pull out relevant pieces of data and use it as part of the query to the LLM. If the records can't be found accurate
ly to begin with, this whole approach would seem to be quite weak.

Am i just misunderstanding the benchmarks? Or am I m
isunderstanding how to utilize these models in RAG? Or is this a genuine problem?

Thanks in advance.
```
---

     
 
all -  [ Multimodal ](https://www.reddit.com/r/LangChain/comments/1bbgdhd/multimodal/) , 2024-03-12-0909
```
 Hello guys,

As we venture closer to the zenith of General Artificial Intelligence (GAI), a noteworthy trend has emerge
d within the AI research community, spearheaded by leading institutions such as OpenAI and Google. These organizations h
ave been pivotal in integrating multimodal capabilities into their Large Language Models (LLMs), marking a significant l
eap towards achieving AI systems with human-like cognitive abilities. This integration of multimodalism signifies an evo
lutionary step in artificial intelligence, enabling these models to not only excel in Natural Language Processing (NLP) 
but also to comprehend and generate auditory information via sophisticated Text-to-Speech (TTS) and Speech-to-Text (STT)
 technologies. Furthermore, the incorporation of computer vision allows these systems to analyze and interpret the natur
al world with remarkable precision, merely through the lens of a camera.

This fusion of modalities—linguistic, auditory
, and visual—equips LLMs with a more comprehensive understanding of the world, mirroring the multifaceted way humans per
ceive and interact with their environment. The ability to process and synthesize information across these dimensions ope
ns up unprecedented possibilities for AI applications, ranging from enhanced conversational interfaces to sophisticated 
autonomous systems capable of navigating complex real-world scenarios.

Amidst this technological renaissance, an intrig
uing question arises concerning Langchain's strategy in adopting multimodal frameworks. As developers and innovators eag
erly seek to harness the power of multimodal AI, the anticipation around Langchain's plans to facilitate the integration
 of multimodal capabilities into their framework is palpable. Such advancements would not only expand the toolkit availa
ble to developers but also pave the way for creating more intuitive and versatile AI systems, capable of operating acros
s a spectrum of human-like modalities.

As we stand on the brink of this transformative era in AI development, the integ
ration of multimodal functionalities within Langchain's offerings could significantly accelerate the adoption of sophist
icated AI solutions, fostering a new wave of innovation in the realm of artificial intelligence. The question remains: w
hen will Langchain unveil its approach to multimodal AI, and how will it empower developers to usher in the next generat
ion of AI applications?
```
---

     
 
all -  [ Seeking help on a LLM project  ](https://www.reddit.com/r/LangChain/comments/1bbf28l/seeking_help_on_a_llm_project/) , 2024-03-12-0909
```

Hello guys. 

I’m new to building llm apps.

I’m currently working on an independent project idea in the Educational se
ctor. I’m thinking of leveraging LLMs for automatic grading of some Python assignments. I’ve tried using gpt-4 for all t
he submissions to generate grade and feedback for each submission. For this approach, I passed the Python code, a rubric
 on how to deduct marks, total possible marks and assignment description. The results were good but I need to evaluate t
hem. Could you help me with suggestions on any techniques that I could use to improve upon this or maybe do some other a
pproaches with Rag or prompting techniques like COT? What should I use as my knowledge base? 

And how would I evaluate 
the responses?

Any suggestions would be absolutely invaluable.

Thanks for reading this!
```
---

     
 
all -  [ Hitting local huggingface inference endpoint or a better way to run models locally in docker? ](https://www.reddit.com/r/LangChain/comments/1bbe8jz/hitting_local_huggingface_inference_endpoint_or_a/) , 2024-03-12-0909
```
I have a model running in a docker container with huggingface's text-generation-inference and am trying to get langchain
 to talk to it.

I figured out how to use the deprecated HuggingFaceTextGenInference class, but it's deprecated. I tried
 using the HuggingFaceEndpoint class (which is suggested) but it wants to try and login to huggingface which doesn't mak
e any sense since the model is running locally.

Have you had any luck with this, or did I miss a setting somewhere in t
he HuggingFaceEndpoint class?

Is there a better way to run models locally in docker? 

:)
```
---

     
 
all -  [ Chunking Idea: Summarize Chunks for better retrieval ](https://www.reddit.com/r/LangChain/comments/1bbdgpj/chunking_idea_summarize_chunks_for_better/) , 2024-03-12-0909
```
Hi,

I want to discuss if this idea already exists or what you guys think of it. 

Does it make sense if you chunk your 
documents, summarize those chunks and use these summaries for retrieval? This is similar to ParentDocumentRetriever, wit
h the difference that the child chunk is the summary and the parent chunk the text itself. 

I think this could improve 
the accuracy as the summary of the chunk could be more related (higher cosine similarity) to the user query/question whi
ch is most of the time much shorter than the chunk. 

&#x200B;

What do you think about this?
```
---

     
 
all -  [ Using LangChain to teach an LLM to write like you ](https://arslanshahid-1997.medium.com/using-langchain-to-teach-an-llm-to-write-like-you-aab394d54792?sk=5136d482d220139c11fa4536681f4648) , 2024-03-12-0909
```

```
---

     
 
all -  [ How to create a chatbot using RAG using llama index? ](https://www.reddit.com/r/LangChain/comments/1bb9f03/how_to_create_a_chatbot_using_rag_using_llama/) , 2024-03-12-0909
```
The problem I am currently experiencing is as follows.  I implemented an ensemble retriever by looking at the ensemble r
etriever document. This is a method of entering a query based on a document and then reranking the results to receive a 
final answer.  That's why 'Hello?' has nothing to do with the document. If you enter llm, “Hello?” is displayed in the d
ocument. They won't reply to me because they can't find it.  How to implement rag and chatbot This is the Ensemble Retri
ever document I referenced. [https://docs.llamaindex.ai/en/stable/examples/retrievers/ensemble\_retrieval.html](https://
docs.llamaindex.ai/en/stable/examples/retrievers/ensemble_retrieval.html)

And below is my code.   


    loader = PyMuP
DFReader()
    docs0 = loader.load(file_path=Path('./data/company_rule.pdf'))
    doc_text = '\n\n'.join([d.get_content(
) for d in docs0])
    docs = [Document(text=doc_text)]
    
    llm = OpenAI(model='gpt-4-0125-preview')
    chunk_size
s = [128, 256, 512, 1024]
    nodes_list = []
    vector_indices = []
    for chunk_size in chunk_sizes:
    print(f'Chu
nk Size: {chunk_size}')
    splitter = SentenceSplitter(chunk_size=chunk_size, chunk_overlap=chunk_size // 2)
    nodes 
= splitter.get_nodes_from_documents(docs)
    for node in nodes:
    node.metadata['chunk_size'] = chunk_size
    node.e
xcluded_embed_metadata_keys = ['chunk_size']
    node.excluded_llm_metadata_keys = ['chunk_size']
    nodes_list.append(
nodes)
    vector_index = VectorStoreIndex(nodes)
    vector_indices.append(vector_index)
    
    retriever_dict = {}
 
   retriever_nodes = []
    for chunk_size, vector_index in zip(chunk_sizes, vector_indices):
    node_id = f'chunk_{chu
nk_size}'
    node = IndexNode(
    text=(
    'rule context retrieves (chunk size')
    f'{chunk_size})'
    ),
    ind
ex_id=node_id,
    )
    retriever_nodes.append(node)
    retriever_dict[node_id] = vector_index.as_retriever()
    
   
 summary_index = SummaryIndex(retriever_nodes)
    
    retriever = RecursiveRetriever(
    root_id='root',
    retrieve
r_dict={'root': summary_index.as_retriever(), **retriever_dict},
    )
    
    nodes = await retriever.aretrieve(
    '
About working hours'
    )
    
    print(f'Number of nodes: {len(nodes)}')
    for node in nodes:
    print(node.node.m
etadata['chunk_size'])
    print(node.node.get_text())
    
    reranker = LLMRerank()
    print(reranker)
    
    quer
y_engine = RetrieverQueryEngine(retriever, node_postprocessors=[reranker])
    
    response = query_engine.query(
    '
About working hours'
    )
    
    display_response(
    response, show_source=True, source_length=500, show_source_met
adata=True
    )
    
    #finalanswer

&#x200B;
```
---

     
 
all -  [ Langsmith for Autogen? ](https://www.reddit.com/r/LangChain/comments/1bb4ww1/langsmith_for_autogen/) , 2024-03-12-0909
```
I want to track my openai api usage using langsmith. 
the app using autogen as its orchestration framework. 

can anyone
 guide me on how to implement this for my agents in autogen?

all kinds of ideas are appreciated!!


```
---

     
 
all -  [ [#langchain 밋업 발표] R.A.G. 우리가 절대 쉽게결과물을 얻을 수 없는 이유 http://aitutor21.com/bbs/board.php?bo_table=aistu ](https://www.reddit.com/r/chatgpt_newtech/comments/1bb2cwo/langchain_밋업_발표_rag_우리가_절대_쉽게결과물을_얻을_수_없는_이유/) , 2024-03-12-0909
```
\[#langchain 밋업 발표\] R.A.G. 우리가 절대 쉽게결과물을 얻을 수 없는 이유  [http://aitutor21.com/bbs/board.php?bo\_table=aistudy&wr\_id=450](
http://aitutor21.com/bbs/board.php?bo_table=aistudy&wr_id=450)
```
---

     
 
all -  [ Multiple Document loader ](https://www.reddit.com/r/LangChain/comments/1bb0yzw/multiple_document_loader/) , 2024-03-12-0909
```
Hey I am looking to use some sort of a loader which can help me load multiple variety of documents AKA a some sort of cu
stom loader, any help you guys can provide?
```
---

     
 
all -  [ Cost effective Frameworks for llm applications in real world scenarios. ](https://www.reddit.com/r/LLMDevs/comments/1baohzc/cost_effective_frameworks_for_llm_applications_in/) , 2024-03-12-0909
```
Langchain 
Autogen 

these are the ones that i have use to develop applications using gpt-4.
but langchain gets too comp
lex for multi agent tasks.
and autogen throws random errors and can get stuck in a loop racking up my credits.
Not to me
ntion using autogen has really been heavy on my pocket…

what are the best options out there which are cost effective as
 well as have simple workflows to implement?? 

I know Langraph, crewai… but it would be great  if someone has experimen
ted with to comment on it… 

lastly gpt-4 seems too costly 
what other models would you recommend instead not compromisi
ng much on performance….?
```
---

     
 
all -  [ Recommendations for RAG Evaluation Framework Resources ](https://www.reddit.com/r/LangChain/comments/1baltvi/recommendations_for_rag_evaluation_framework/) , 2024-03-12-0909
```
Hello everyone!

I'm currently on the lookout for some solid resources to help me delve into RAG evaluation frameworks. 
Whether it's articles, guides, or even personal recommendations, I'm eager to expand my knowledge in this area. If you'v
e come across any valuable resources or have expertise in RAG evaluation, I'd greatly appreciate your insights and sugge
stions. Thanks in advance!

 
```
---

     
 
all -  [ Need help reducing execution time while using langchain llama2 7b quantised version in CPU ](https://www.reddit.com/r/LangChain/comments/1balq8c/need_help_reducing_execution_time_while_using/) , 2024-03-12-0909
```
Hi, I am new to generative AI and building a document based question answering module using langchain and Llama2 as the 
LLM. I am using sentence-transformers/all-MiniLM-L6-v2 for the embeddings. But I think the actual time is being taken in
 the Retrieval Chain. Per response takes around 1 min, and I have limited logical cores to use (max: 10) and when using 
multiprocessing each response takes even longer. Any ideas on how I can reduce the execution time? Without usage of GPU?

```
---

     
 
all -  [ LangChain + python+ oobabooga API = Chat with a PDF? ](https://www.reddit.com/r/LocalLLaMA/comments/1balmqo/langchain_python_oobabooga_api_chat_with_a_pdf/) , 2024-03-12-0909
```
I have oobabooga running on my server with the API exposed.

Text-generation-webui works great for text, but not at all 
intuitive if I want to upload a file (e.g. PDF) and then ask whatever model is loaded questions about it.

I can write p
ython code (and also some other languages for a web interface), I have read that using LangChain combined with the API t
hat is exposed by oobabooga make it possible to build something that can load a PDF, tokenize it and then send it to oob
abooga and make it possible for a loaded model to use the data (and eventually answer questions about it).

Now, how / w
here do I start?

I rather utilize the API that I already have working (from ooba) and just write the part for making th
e tokenized PFF available to it, also maybe eventually create a simple web UI for it etc.

I could not find any concrete
 example, as it seem to look like the most recent trend is just find some tool, install snd use it (but then those tools
 have their own way and dont serve my intended purpose)

Could anyone send me in the right direction other then document
ation which I already am aware of (and other than general syntax don’t share code examples)

Thanks in advanced 
```
---

     
 
all -  [ Rag over updating data ](https://www.reddit.com/r/LangChain/comments/1baky7p/rag_over_updating_data/) , 2024-03-12-0909
```
Have you ever had to ingest documents about a specific topic that is changing over time? 
i.e. : news about a specific f
act may be accurate today (we only know so much) but inaccurate tomorrow (we discover some new things).
How would you re
turn only the most recent facts?
```
---

     
 
all -  [ Chat with rag - further questions ](https://www.reddit.com/r/LangChain/comments/1bajhg8/chat_with_rag_further_questions/) , 2024-03-12-0909
```
I already have embedding db to perform rag.
I’m just struggling with follow up questions.

- so user asks a question
- r
ag search to get content, send to loom, return response
- user asks a follow up like: “what about option 2”
- but how th
e backend know what to do next?

- should I do another rag for this specific query “what about option 2”, that is basica
lly useless.
- or send the full conversation with the prior rag, and this additional message
```
---

     
 
all -  [ Langchain recursive summary VS agentic summary VS Opus/Yi 200k context ](https://www.reddit.com/r/LocalLLaMA/comments/1baezc4/langchain_recursive_summary_vs_agentic_summary_vs/) , 2024-03-12-0909
```
What’s the best way to summarise text these days?


Was thinking of recursive summary using Langchain, or something with
 agents, or just putting it all in the Claude Opus or Yi 200k context


As an additional side note has anyone tried Cohe
re’s summary API product? Seems slightly different to other methods 
```
---

     
 
all -  [ How to connect to web-based chatpgt, gemini or claude? ](https://www.reddit.com/r/LangChain/comments/1badxki/how_to_connect_to_webbased_chatpgt_gemini_or/) , 2024-03-12-0909
```
Hi all! I am pretty new to this langchain world. But it seems langchain requires you to have api key for all llm service
s. Right now I have chatgpt 4 subscription, is it possible to connect langchain to the web-based chatgpt without using a
pi key which will cause extra money? Thanks!
```
---

     
 
all -  [ How do you decide which RAG strategy is best? ](https://www.reddit.com/r/LangChain/comments/1baba9c/how_do_you_decide_which_rag_strategy_is_best/) , 2024-03-12-0909
```
I really liked this idea of evaluating different RAG strategies. This simple project is amazing and can be useful to the
 community here. You can have your custom data evaluate different RAG strategies and finally can see which one works bes
t. Try and let me know what you guys think: [https://www.ragarena.com/](https://www.ragarena.com/) 
```
---

     
 
all -  [ Need help ](https://www.reddit.com/r/LangChain/comments/1ba9kqk/need_help/) , 2024-03-12-0909
```
My company is asking me to build a chatbot for appointment scheduling for patient engagement using LLM. Does anyone have
 experience in it? 

Is it possible with RAG approach? As we don’t have data looking to synthesize it. Or do I need to f
ine tune it with synthesized data?

It would be really great if someone could help!

```
---

     
 
MachineLearning -  [ [D] : Scale PDF Q&A App to 10K Users with GPUs – <$250/Mo ](https://www.reddit.com/r/MachineLearning/comments/1b6jv56/d_scale_pdf_qa_app_to_10k_users_with_gpus_250mo/) , 2024-03-12-0909
```
Hello everyone,

Check out this step-by-step detailed tutorial on building and scaling a PDF Q&A Application using Pinec
one, Langchain and Inferless

&#x200B;

[Architecture](https://preview.redd.it/zfta52cbddmc1.png?width=1301&format=png&a
uto=webp&s=440399212d3feb03e861759a31602e2cde0dc7fb)

Alongside, the detailed quick deploy guide, it also includes cost 
analysis on how you can save upto 84% cost with an example of processing 3000 documents and nearly 10,000 queries every 
month, all while dramatically cutting your costs from $1800 ( AWS) to just $250 a month on Inferless.

Here is the tutor
ial - [https://cookbook.inferless.com/](https://cookbook.inferless.com/)

If you resonate, join the discussion on Hacker
news here - [https://news.ycombinator.com/item?id=39594588](https://news.ycombinator.com/item?id=39594588)
```
---

     
 
MachineLearning -  [ [D] What Is Your LLM Tech Stack in Production? ](https://www.reddit.com/r/MachineLearning/comments/1b4sdru/d_what_is_your_llm_tech_stack_in_production/) , 2024-03-12-0909
```
Curious what everybody is using to implement LLM powered apps for production usage and your experience with these toolin
gs and advice. 

This is what I am using for some RAG prototypes I have been building for users in finance and capital m
arkets.

**Pre-processing\ETL:**
Unstructured.io + Spark, Airflow

**Embedding model:**
Cohere Embed v3
Previously using
 OpenAI Ada but Cohere has significantly better retrieval recall and precision for my use case. Also exploring other ope
n weights embedding models

**Vector Database:**
Elasticsearch previously but now using Pinecone

**LLM:**
Gone through 
quite a few including hosted and self-hosted options. Went with gpt4 early during prototyping then switched to gpt3.5-tu
rbo for more manageable costs and eventually open weights models. 

Now using a fine-tuned Llama2 70B model self hosted 
with vLLM 

**LLM Framework:**
Started with Langchain initially but found it cumbersome to extend as the app became more
 complex. Tried implementing it in LlamaIndex at some point just to learn and found it just as bad. Went back to Langcha
in and now I am in the midst of replacing it with my own logic

What is everyone else using?

Edit: correct model Llama2
 70B
```
---

     
 
MachineLearning -  [ [D] Graphs + vectordbs? Need your input: Cognee.ai . AI Data Pipelines for Real-World Production (Pa ](https://www.reddit.com/r/MachineLearning/comments/1aweo71/d_graphs_vectordbs_need_your_input_cogneeai_ai/) , 2024-03-12-0909
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

     
 
MachineLearning -  [ [D] AI projects Suggestions ](https://www.reddit.com/r/MachineLearning/comments/1aunkmw/d_ai_projects_suggestions/) , 2024-03-12-0909
```
Hi Everyone, I need a suggestion to create AI courses for students ( Hands-on AI projects). I am thinking about the late
st AI trends such as Langchain, RAG, and vector databases. In each project, there can be multiple tasks, and the main th
ing is each task should have an automated system in which we can verify whether students have done it correctly or not.


For example: Project with visualization cannot be automatically tested. 

For example: A project with visualization can
not be automatically tested. . em can verify if the length of the text is smaller we can verify that it is correct.
```
---

     
 
MachineLearning -  [ Whats in your RAG setup? [D] ](https://www.reddit.com/r/MachineLearning/comments/1apcp2w/whats_in_your_rag_setup_d/) , 2024-03-12-0909
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

     
