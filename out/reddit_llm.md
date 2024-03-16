 
all -  [ Does LangChain support the new milvus cosine similarity? ](https://www.reddit.com/r/LangChain/comments/1bfrguy/does_langchain_support_the_new_milvus_cosine/) , 2024-03-16-0911
```
I'm very new to working with LLMs, but I'm an experienced software engineer. I've read that OpenAI embeddings work best 
with vector stores that are configured to use cosine similarity when doing searches. Milvus, the vector store I'm using 
for my POC right now, supports cosine similarity. However it is a very recent feature.

The docs I'm looking at for Lang
Chain show it auto-configuring the collection, for the most part. What I'm asking is if LangChain will use cosine simila
rity when I configure it with milvus and OpenAI embeddings
```
---

     
 
all -  [ Chat with your PDFs using LangChain ](https://medium.com/@arslanshahid-1997/chat-with-your-pdfs-using-langchain-e57866b7926d) , 2024-03-16-0911
```

```
---

     
 
all -  [ Introducing Instagram's First AI News Headlines Page! ](https://www.reddit.com/r/u_fastheadlines/comments/1bfgylj/introducing_instagrams_first_ai_news_headlines/) , 2024-03-16-0911
```
I'm excited to share the launch of Instagram's AI News Headlines Page!  
*Here's what you need to know:*  
**Built With 
Python:** Our team utilized Python to develop this innovative platform, ensuring efficiency and flexibility in deliverin
g news content.  
**Using llama2 & LangChain:** We integrated llama2 and LangChain technologies to enhance natural langu
age processing capabilities, enabling accurate and relevant news summaries.  
**Automated CronJobs**: Our system runs au
tomated CronJobs to continuously update the news feed, keeping you informed in real-time.  
**News APIs:** We've leverag
ed various News APIs to aggregate information from diverse sources, providing comprehensive coverage across different to
pics.

I'll be very happy to write more technical post later on How we built it.

Make sure to checkout & support us!  

[https://www.instagram.com/fastheadlines/](https://www.instagram.com/fastheadlines/)
```
---

     
 
all -  [ R&R / Tooling for a Small Team ](https://www.reddit.com/r/aipromptprogramming/comments/1bfds5w/rr_tooling_for_a_small_team/) , 2024-03-16-0911
```
A friend and I are working on a new startup project using LLMs for a conversational interface with our users.

He is an 
experienced full stack developer (cloud infra, database, web), but without data science or analytics skills. I am taking
 on the more business oriented role of CEO / Product Manager. I am also the one who is likely to do the prompt engineeri
ng to get the LLMs to interact with our users the way we want to.

I understand code and used to code a long time ago, b
ut by today's standards I'm not a competent developer by any means. I've been looking at langchain and that is probably 
a bit too far on the technical side of where I want to be spending my time. Ideally I'd like to be able to experiment wi
th prompt engineering in an environment like Chat GPT but where i can version control what i'm doing, maybe record testi
ng output and produce something that my CTO colleague can then implement in code and make it all work.

Does anyone have
 any suggestions on how we should setup our workflow and what tools, packages or IDEs we should use in this scenario? Or
 am I overreaching to think that I can do the prompt engineering and conversation flow design without learning python or
 something like that?

For context, the tools he has selected for his part so far are Google Cloud, GitHub and Python/Dj
ango for web / API development. We're starting with GPT4 as our LLM but will evaluate others later. 
```
---

     
 
all -  [ Advanced course on LLM ](https://www.reddit.com/r/LocalLLaMA/comments/1bfbrv7/advanced_course_on_llm/) , 2024-03-16-0911
```
I've been looking for a while on this topic, but I don't feel confident and the time to keep reading over all the texts 
required to get a full picture of this. The problem with YT channels is that there is a ton of fluff (because most guys 
adjust their videos to the YT algo), and texts are not really comprehensive and take a ton of time to digest, which make
s my pace extremely slow. Furthermore, finding a good order of things instead of jumping from paper to paper which most 
of the time are totally not related makes things even harder. I'm totally aware that there are a ton of 'scammers' selli
ng b\*\*\*s\*\*t AI courses that are anything but very basic prompting as they feel very creative or something. 

So at 
this point I was wondering if there are any recommended advanced courses that cover all that anyone needs to know to put
 up to date with the scene to get a good head start.  The more advanced, the better, which involves, Langchain, Python s
kills and anything you could think that could make the course sharper in the whole sense, not just simple prompting.
```
---

     
 
all -  [ When to simply feed whole document in RAG? ](https://www.reddit.com/r/LangChain/comments/1bf9ps7/when_to_simply_feed_whole_document_in_rag/) , 2024-03-16-0911
```
Hello, I am new to RAG.

I am making a chatbot for the Beeline application for my company. 

The Beeline team at my comp
any has put together two FAQs to use as context: one for contractors/vendors and one for internal employees. Each FAQ is
 a word document with various questions and answers that describe processes like onboarding, submitting time cards, etc.
. Each is about 3000 tokens long.

I have written two system prompts based on whether the user is a contractor/vendor or
 internal users. Each is about 2000 tokens… does this seem like too much?

The chatbot application uses the correct faq 
document and system prompt based on the user. Basically, I just grab the correct ones and send to my deployed LLM alongs
ide the user query. The total prompt is usually like 5000 tokens.I use the faq document in its entirety given I am using
 a gpt-4-32k deployment as my LLM.

The responses are accurate every time. However, they are slow. Is this due to token 
size? Should I be chunking? How can I ensure a given chunk would have all the right sentences in it if I chunked? Some p
rocesses are 5 sentences long and what if they are captured in different chunks?

Any insight is super helpful. I am cod
ing everything rather than using langchain or llama2index or whatever. Should I not do this? I found the documentation f
or both hard to follow honestly so I immediately abandoned trying to use them 😅

```
---

     
 
all -  [ Knowing number of tokens in SQL agent ](https://www.reddit.com/r/LangChain/comments/1bf9mkq/knowing_number_of_tokens_in_sql_agent/) , 2024-03-16-0911
```
I am using the below sql\_agent to query through my database:  
agent = create\_sql\_agent(llm=llm, toolkit=sql\_toolkit
, agent\_type=AgentType.ZERO\_SHOT\_REACT\_DESCRIPTION,  
 handle\_parsing\_errors=True, verbose=True, max\_execution\_t
ime=200,  
 max\_iterations=1000)  
Is there any way to count the total number of tokens(prompt tokens+query tokens+quer
y\_result tokens+thought tokens+action tokens+observation tokens+tool tokens) used by this agent.  
I have used the belo
w approach without good results:  
[https://python.langchain.com/docs/modules/model\_io/llms/token\_usage\_tracking](htt
ps://python.langchain.com/docs/modules/model_io/llms/token_usage_tracking)
```
---

     
 
all -  [ How to call Multiple API's for a user input via LangChain ](https://www.reddit.com/r/LangChain/comments/1bf7nuo/how_to_call_multiple_apis_for_a_user_input_via/) , 2024-03-16-0911
```
I have two swagger api docs and I am looking for creating an app which can interact with API's. My user input depends on
 two different API endpoint from two different  Swagger docs.

My user query depends on calling two different  API's fro
m two different swagger endpoint. I want to chain the first API response value from chain 1  and set the input variables
 for the second API from a different swagger. 

For Example, 

User query, 'What is the train status 1234'

Call API 1- 
/travel-modes-reference/train to get the reference for train--APi response as '1'

Call API 2  /transport/1234/status&mo
de=1

how can I perform this in Langchain using Chains ,tools and agent ? 
```
---

     
 
all -  [ anyone mind helping me scope out a custom LLM tool for our editorial team ](https://www.reddit.com/r/LangChain/comments/1bf4l56/anyone_mind_helping_me_scope_out_a_custom_llm/) , 2024-03-16-0911
```
I'm thinking i need gpt4 + langchain to access urls, docs, sheets via google drive + vector db so all the citations and 
info is accurate (medical, cancer, legal) etc.. 

i'm looking for an effective way to train my own and store the data an
d draft from briefs that we human edit afterwards
```
---

     
 
all -  [ Amyone work in editorial or content agency? looking for some advice ](https://www.reddit.com/r/ChatGPTPromptGenius/comments/1bf4ghu/amyone_work_in_editorial_or_content_agency/) , 2024-03-16-0911
```
I feel like I need a custom solution like gpt4 + langchain + vector database + any other suggestions, has anyone built o
ut their own local LLM like this for writing serious SEO articles or journalism? 

would love some help even with some p
rompts for training once i have this setup..
```
---

     
 
all -  [ Can any database be a Vector Database? ](https://www.reddit.com/r/LangChain/comments/1bf3kjs/can_any_database_be_a_vector_database/) , 2024-03-16-0911
```
As long as I perform the text splitting and embedding before hand, is there any reason I can't store the embeddings in, 
say, Redis or MongoDB?
```
---

     
 
all -  [ RAG agent in langchain ](https://www.reddit.com/r/LangChain/comments/1bf2iya/rag_agent_in_langchain/) , 2024-03-16-0911
```
I have a rag system that is used to answer customer questions.
But to optimise the retrieval, I want the agent ask some 
follow up questions and instruct user to provide answer before retrieval.

I have a few questions.
Which type of langcha
in agent is good at this task?
How to prompt the agent to ask follow up one or more question dynamically?
Do I need mult
iple agent to do it?  I haven’t touched on langgraph yet but I want to see one agent can do this task.

Thanks.  

```
---

     
 
all -  [ llama2 mocking me ](https://www.reddit.com/r/LangChain/comments/1bf0hb0/llama2_mocking_me/) , 2024-03-16-0911
```
Im currently replacing the OpenAI-Api with an langchain-instance using ollama, llama2 and chrome-db.

This was the first
 test I did via frontend:

&#x200B;

[Thats just rude!](https://preview.redd.it/wnyufxub4eoc1.png?width=1709&format=png&
auto=webp&s=4ae06cb94d55db4491138bdd2b140509bfba7cd5)
```
---

     
 
all -  [ How are you implementing AI? ](https://www.reddit.com/r/devops/comments/1bezy3t/how_are_you_implementing_ai/) , 2024-03-16-0911
```
There's a bit of a lull in my current job as we're waiting on construction of a new data center, so I've begun studying 
up on AI skills. There's a lot to learn so I'm curious what long term goals might be possible to strive for. 

I'm curre
ntly working on using langchain to query our confluence space. After that I thought about creating something like nimbus
.dev for our elastic stack.

What have you done with AI.in your environment that's benefitted you?
```
---

     
 
all -  [ Current best practices for ingesting data from PDF (Maybe Microsoft Azure AI Search?) ](https://www.reddit.com/r/LangChain/comments/1bev63g/current_best_practices_for_ingesting_data_from/) , 2024-03-16-0911
```
Hi,

not sure if this is the right subreddit, but i see there are plenty of questions about RAG here.

I'm working on bu
ilding a RAG project with a lot of user manuals, technical stuff and so on. With my current ingestion pipeline, the resu
lts are very mixed. Some answers are very good, while in other cases the retrieval step doesn't provide any helpful stuf
f.

At the moment i'm kinda stuck, because i don't know how to improve the quality in chunking and getting the data stru
cture right.

I tried many different pdf loaders. First problem here is, that some loaders can't deal with all pdfs i've
 got. Eventually i sticked with Unstructured, since it can extract tables and images, and keeps the page numbers as meta
data. Unstructured comes with the possibilty to chunk data 'by title', so that we get more consistent chunks across the 
chapters of a file. This approach alone wasn't that impressive. I used the LangChain Semantic chunker afterwards and get
 pretty decent results so far (still far from good, unfortunately). Also the structure of the extracted tables seem to b
e a bit off most of the time. I'm using Unstructured locally, i don't have any experience with the API.

I'm getting stu
ck at the moment, since i don't really know how to improve my chunking and preprocessing any further.

I also tried spli
tting bigger and smaller chunks for small-to-big retrieval. Using smaller chunks for the search-step and getting bigger 
parent chunks for the context. The results where quite horrible. Another thing i haven't tried so far, is a window retri
eval, where we use neighboured chunks from the retrieved chunks for more context.

At this time many people tried to bui
ld RAG projects. Are there any best practices in the ingestion of data i may have overseen so far? Currently i'm thinkin
g about using Azure AI Search, instead of doing the ingestion-step myself. This would make most of my own work useless, 
but currently i just want to get the best possible results.



Very thankful for some input and/or tips


```
---

     
 
all -  [ How does a PartialPrompt fit into a processing chain? ](https://www.reddit.com/r/LangChain/comments/1besaia/how_does_a_partialprompt_fit_into_a_processing/) , 2024-03-16-0911
```
The documentation about Partial Prompts only shows operation of \`format\`. How would one work a partial prompt into a c
hain?  If one \`invoke\`s it, does it return a partially instantiated prompt that goes to the next stage of the chain?


Anyone have an example of this that they could share?

It seems like a \`FewShotPrompt\` is a special case of a partial 
prompt, right?
```
---

     
 
all -  [ Deci AI Launched a new model and inference platform. Here's a tutorial on using it ](https://www.reddit.com/r/ArtificialInteligence/comments/1bepemz/deci_ai_launched_a_new_model_and_inference/) , 2024-03-16-0911
```
[Here's a link](https://colab.research.google.com/drive/1JW8t-kosLEgYVxXadwwDMypnQ5c_UD2u?usp=sharing) to the notebook t
o hack around with it!  This notebook will show you how to access the API via cURL, requests, and OpenAI SDK.

I have an
other notebook which shows how to use the model in LangChain by [implementing a custom LLM](https://colab.research.googl
e.com/drive/1PMwMovV-ji1mp0yl0qYDTI-gdG6SjOnZ?usp=sharing).

&#x200B;

Edit: Updated link to the notebook
```
---

     
 
all -  [ RAG is too slow with 100k PDFs! What do you suggest? LLM fine-tuning? ](https://www.reddit.com/r/LangChain/comments/1benf40/rag_is_too_slow_with_100k_pdfs_what_do_you/) , 2024-03-16-0911
```
Hello everyone,

This is my first post here and I hope it is clear and correct for you all :)

Currently, I am working o
n an AI project where the idea is to 'teach' a large language model thousands of english PDFs (around 100k, all about th
e same topic) and then be able to chat with it.

I followed several tutorials, using different LLMs (Zephyr, Llama2, Mis
tral) from HuggingFace and giving a proper prompt for the topic.

In the last weeks I tried RAG and unfortunately it cou
ld not give me good results :( I suppose due to the huge amount of data, but it is really really slow and to answer it t
akes 10 min or more (on a cluster  Tesla V100-SXM2-32GB GPU)! Is there a way to speed it up?

Moreover, sometimes it giv
es very good answers, while sometimes it gives erroneous information and a sort of 'hallucination' :( I really tried eve
rything: change the prompt, change the embedding model, change the LLM, change the chunk size, but nothing could help.  

Finally, I am afraid that RAG is not good at all for deployment since you need a lot of memory for the 'external knowle
dge' and for the model itself.

Is there another solution to RAG? Should I use fine tuning? If yes, how can I let my mod
el to assimilate all these data? Should I turn the PDFs in JSONs made of Questions/Answers?

Did you succed in doing a p
roject like this? If yes, can you help me, please? I do not know how to properly solve this issue. Any help would be rea
lly appreciated! 

Thank you so much in advance!

EDIT:  
I am really really happy to see so much people trying to help 
me! I THANK YOU ALL! :)   
Apologies if it is a long text and maybe with too general information, but I am still a begin
ner and I am trying to explain my problem as best as I can :(
```
---

     
 
all -  [ Langchain OR Llamaindex for RAG app with Typescript ](https://www.reddit.com/r/LangChain/comments/1bemubq/langchain_or_llamaindex_for_rag_app_with/) , 2024-03-16-0911
```
Hello ! I want to develop a pretty complex RAG application.

I spent my time learning concepts on both Langchain and Lla
mainde, but I am not yet sure which one to pick

Question for people that already worked with this, is it easier (more a
nd better docs, clean implementation) to work with TS + Langchain or TS + Llamaindex ? 
```
---

     
 
all -  [ CopilotKit v0.4.1 - LangChain support ](https://www.reddit.com/r/selfhosted/comments/1beldc0/copilotkit_v041_langchain_support/) , 2024-03-16-0911
```
Hi everyone,

We have just released our new CopilotKit version that supports LangChain.

CopilotKit is a React Infrastru
cture library that works against OpenAI or other LLMs to build ChatBots, Textareas, and Co-Agents.

[https://github.com/
CopilotKit/CopilotKit/](https://github.com/CopilotKit/CopilotKit/)

You can feed the React components with your applicat
ion context and run prompts against it to trigger 'function calls.'

&#x200B;

The repository is 100% open-source (self-
hosted). You can read the quick-start guide here:

[https://docs.copilotkit.ai/getting-started/quickstart-chatbot](https
://docs.copilotkit.ai/getting-started/quickstart-chatbot)

&#x200B;

We have made an example app for building a PowerPoi
nt presentation that can search the web (with Langchain and Tavily) and automatically create a presentation about any to
pic.

[https://links.github20k.com/power-point](https://links.github20k.com/power-point)

&#x200B;

We are looking for m
ore exciting features to build; let me know your thoughts.
```
---

     
 
all -  [ [HIRING] Senior ML Engineer - 100% Remote + every other friday off ](https://www.reddit.com/r/MachineLearningJobs/comments/1bekw0v/hiring_senior_ml_engineer_100_remote_every_other/) , 2024-03-16-0911
```
Apply here: [https://grnh.se/50c178c17us](https://grnh.se/50c178c17us)

Building with the latest tools, our Machine Lear
ning teams launch for Silicon Valley startups and Life Science giants alike.

Join Loka to work remotely, ship projects 
you’re proud of and enjoy every other Friday off.

**The Role**

* Understand business objectives and develop models tha
t help achieve them, plus metrics to track their progress.
* Design and implement complex ML systems using classical ML,
 DL and Foundation Models and following best practices.
* Lead client communications by gathering requirements, managing
 expectations and communicating deliverables.
* Wrangle, explore and visualize data with a careful eye for issues that r
equire data cleaning as well as differences in data distribution that may affect performance after deployment.
* Analyze
 model errors; design strategies to overcome them.
* Deploy, maintain and upgrade ML models and pipelines.
* Follow Loka
’s career track for growth by demonstrating technical excellence, innovation, autonomy, ownership, communication and tea
mwork.

**The Benefits**

* Every other Friday off (26 extra days off a year!)
* LokaLabs incubator
* Explore and Reloca
tion programs (three months work abroad or full international relo)
* Remote and flexible
* Paid sick days and local hol
idays
* Fitness subscription

**The Required Hard Skills**

* Bachelor’s degree in Computer Science or related
* Profici
ent in English
* Experience with Python, ML libraries and AI/ML frameworks (PyTorch, HuggingFace, TensorFlow, Keras, Sci
kit-learn, Spark etc.)
* Strong understanding of statistical, ML and deep learning algorithms (candidates with NLP exper
ience preferred)
* Experience building GenAI solutions including prompt engineering (e.g: Langchain), fine-tuning and se
rving LLMs, search and embeddings, etc.
* Experience with MLOps, preferably in AWS (e.g: Sagemaker), as well as standard
s tools (e.g. MLFlow)
* Experience visualizing and manipulating big datasets
* Client-facing experience

**The Required 
Soft Skills**

* Curiosity—Ambition to learn and grow into different industries with a modern tech stack
* Autonomy and 
positivity—We’re a fully remote, globally distributed team
* Teamwork—Enjoy a collaborative approach
* Adaptability—Oper
ate with a startup mindset and move at a startup pace
```
---

     
 
all -  [ Best Embedding databse for massive text data. ](https://www.reddit.com/r/LangChain/comments/1bekhre/best_embedding_databse_for_massive_text_data/) , 2024-03-16-0911
```
I have been working on a 'ask questions to pdf' project. There are following issues I'm facing.

1. The data is huge so 
the RAG agent is hallucinating some time if it has the context it says 'The given context does not' but ad back end it h
as the context.
2. Sometimes it overwhelms with the data and give incorrect answers.
3. The emmbeddingd are failling to 
give context about the tables. (Currently I have converted all the tables to a json file but Im facing problems to embed
 a json file).

Please reply if anyone is familier with such Kind of project and also if I can use any other DB curently
 I'm using ChromaDB. I have used FAISS but it was less accurate than ChromaDB.
```
---

     
 
all -  [ Langsmith Plus use in Europe makes you not compliant ](https://www.reddit.com/r/LangChain/comments/1bekfw8/langsmith_plus_use_in_europe_makes_you_not/) , 2024-03-16-0911
```
We were trying to buy Langsmith Plus for our startup (300+ employees) for 6 users and then consider if in the future we 
would extend the use within the company and go for an Enteprise version (cost starts at 17k for that). However, when we 
did the normal checks we do for all our third party vendors, we noticed that they didn't have a DPA, so we would need th
em to sign our DPA (as it is the only way for us to be compliant to European laws). I put our legal advisor in touch wit
h them and they told us clearly that they only do this for Enterprise customers and they literally added they don't comp
ly to GDPR :-o. This is the full reply they sent:  
'Unfortunately we're not fully GDPR compliant, so we're not signing 
DPAs with out plus plan customers at this time. Wish I had a better update to share. '

So unfortunately we are now look
ing into alternatives (W&B would be a safe choice as I see they have their own DPA so we wouldn't need to sign anything)
.  
The question is: do you use Langsmith Plus in Europe? Did you know that they are not GDPR compliant? (and so your co
mpany is not as well if you use them).  
I also hope they reconsider this policy and let us use their product legally, w
e would even be ok to pay a small one off to have them to sign our DPA. But they need to collaborate with the companies 
to make sure they don't lose compliance. What do you think? did you know of this before?
```
---

     
 
all -  [ Sql database embedding and store into chroma ](https://www.reddit.com/r/LangChain/comments/1bej7be/sql_database_embedding_and_store_into_chroma/) , 2024-03-16-0911
```
Need help to do this :\_  


sql\_db = SQLDatabase.from\_uri('sqlite:///Chinook.db')  
print(sql\_db.dialect)  
print(sq
l\_db.get\_usable\_table\_names())  


llm = ChatOpenAI(model='gpt-3.5-turbo', temperature=0,  
 openai\_api\_key=os.get
env('OPENAI\_API\_KEY'))  


\# chroma db instance created  
if os.path.exists('db'):  
 pass  
else:  
os.mkdir('db')  

presist\_directory = 'db'  
embeddings = OpenAIEmbeddings()  
vectordb = Chroma(persist\_directory=presist\_directory, 
 
 embedding\_function=embeddings)  


\# TODO create embeddings and store indexing into vectordb...(how can i create em
beddings from sql db and store it in vectordb)  


  


  


how can i store db into vector db please help to resolve th
is
```
---

     
 
all -  [ Pinecone Hybrid Search Retriever + gpt 3.5 ](https://www.reddit.com/r/LangChain/comments/1begx6v/pinecone_hybrid_search_retriever_gpt_35/) , 2024-03-16-0911
```
 I've finished putting the document in the pinecone index and bringing it up. Now I want to use bm25 together to make Pi
necone Hybrid Search Retriever and gpt 3-5 to make a chatbot, but it doesn't work. Can I share the example code? 
```
---

     
 
all -  [ System Prompt for a language learning app ](https://www.reddit.com/r/LangChain/comments/1begjl3/system_prompt_for_a_language_learning_app/) , 2024-03-16-0911
```
Hello guys,

I am having a difficult time getting desired responses from my llm based on the system prompt that I crafte
d for my language learning chatbot. Currently I am using groq's mixtral-8x7b-32768 model with langchain.

Here is a typi
cal user journey -

1. User logs in
2. Chatbot guides the user through a conversational onboarding to collect basic info
 like name, age, academic level.
3. AI prepares an English level test to gauge student proficiency in the language based
 on the student details (provided during onboarding stage)
4. AI starts posing questions one by one to the student witho
ut giving any feedback or explanation to each question.
5. Once the assessment is complete, a detailed feedback on stren
gths and weaknesses of the student is given.
6. A personalised and comprehensive study plan is generated for the student
 based on the assessment results.

I tried to put the above user journey in the system prompt as instructions, but the l
lm is not able to follow. Sometimes it's giving all the questions at once and sometimes its providing answers on its own
 and then giving feedback plus creating the study plan in one go itself.

I've tried numerous variations of my system pr
ompt, adjusted the temperature of the model as well, but no luck. I keep getting undesirable responses.

Someone pls hel
p me out here as to how do I need to approach this problem.
```
---

     
 
all -  [ Issue when querying pinecone data ](https://www.reddit.com/r/LangChain/comments/1beett5/issue_when_querying_pinecone_data/) , 2024-03-16-0911
```
Trying out a simple application with Langchain and Pinecone training by uploading a PDF document. I was able to upload t
he vectors to pinecone successfully but whenever I try querying I receive a PineconeApiAttributeError: QueryResponse has
 no attribute '0' at \['\['received\_data'\]'\] error. The query was in string format and was embedded in vector format 
using OpenAIEmbeddings(). My code is as follows.

    def retrieve_query(query,k=2):     
    xq = embeddings.embed_quer
y(query) #embeddings = OpenAIEmbeddings(api_key)     
    matching_results = index_name.query(vector = xq,top_k=k,includ
e_values=True)     
    return matching_results  
    from langchain.chains.question_answering import load_qa_chain 
   
 from langchain import OpenAI 
    llm=OpenAI(model_name='text-davinci-003',temperature=0.5) chain=load_qa_chain(llm,cha
in_type='stuff') 
    
    def retrieve_answers(query):     
    doc_search=retrieve_query(query)     
    print(doc_sea
rch)     
    response=chain.run(input_documents=doc_search,question=query)     
    return response  

the doc\_search 
variable printed out {'matches': \[\], 'namespace': '', 'usage': {'read\_units': 6}}
```
---

     
 
all -  [ Google Cloud Databases Advancements with GenAI in 2024 ](https://www.reddit.com/r/u_Glittering-Pack5342/comments/1beet6j/google_cloud_databases_advancements_with_genai_in/) , 2024-03-16-0911
```
 

* [Introduction ](https://www.sparity.com/blogs/google-cloud-databases-with-gen-ai-in-2024/#Introduction)
* [AlloyDB]
(https://www.sparity.com/blogs/google-cloud-databases-with-gen-ai-in-2024/#AlloyDB)
* [LangChain](https://www.sparity.co
m/blogs/google-cloud-databases-with-gen-ai-in-2024/#LangChain)
* [Vector Search in Databases](https://www.sparity.com/bl
ogs/google-cloud-databases-with-gen-ai-in-2024/#Vector_Search_in_Databases)
* [Spanner and AlloyDB with Vertex AI](https
://www.sparity.com/blogs/google-cloud-databases-with-gen-ai-in-2024/#Spanner_and_AlloyDB_with_Vertex_AI)
* [How google c
loud databases advancements helps you ?](https://www.sparity.com/blogs/google-cloud-databases-with-gen-ai-in-2024/#How_g
oogle_cloud_databases_advancements_helps_you)
* [Conclusion](https://www.sparity.com/blogs/google-cloud-databases-with-g
en-ai-in-2024/#Conclusion)
* [Why Sparity](https://www.sparity.com/blogs/google-cloud-databases-with-gen-ai-in-2024/#Why
_Sparity)
* [Related Posts](https://www.sparity.com/blogs/google-cloud-databases-with-gen-ai-in-2024/#Related_Posts)

##
 Introduction 

The fusion of AI technology with databases has opened up fresh possibilities for innovation and transfor
mation in the tech sector. Google Cloud, a front runner in cloud computing, has spearheaded this evolution by continuous
ly strengthening its offerings to deliver cutting-edge solutions to businesses and software developers. Google has annou
nced significant progress in merging generative AI with its databases, marking a pivotal moment in the advancement of AI
-centric applications. Our blog explores into these captivating advancements of google cloud databases and explore their
 impact on AI-powered products moving ahead.

Google’s prioritization of AI underscores improving database functionaliti
es to effectively back AI-driven applications. As AI advances, the demand rises for databases that seamlessly integrate 
with generative AI, facilitating development of intelligent, context-aware applications. According to Google, 71% of com
panies plan to employ databases with built-in GenAI capabilities, emphasizing the crucial role of operational databases 
in leading enterprise AI advancements moving forward.

## AlloyDB

Google’s latest announcement brings a major upgrade t
o AlloyDB AI, a fully managed database designed for GenAI workloads and compatible with PostgreSQL. Now available in bot
h AlloyDB and AlloyDB Omni, AlloyDB AI offers exceptional performance for transactional, analytical, and vector workload
s, making it an ideal choice for enterprise-level tasks. Leveraging the pgvector extension for PostgreSQL, AlloyDB AI en
ables users to work with vector embeddings essential for developing GenAI applications driven by advanced language model
s. This integration simplifies storage, indexing, and querying of vector embeddings directly within the AlloyDB ecosyste
m, enhancing efficiency and effectiveness.

## LangChain

Google is enhancing its ecosystem by open-sourcing LangChain i
ntegrations for all [**Google Cloud**](https://www.sparity.com/blogs/aws-azure-gcp-which-one-to-choose-in-2024/) databas
es, alongside the expansion of AlloyDB AI. LangChain, an open-source LLM orchestration framework, enables developers to 
create context-aware GenAI applications with built-in Retrieval Augmented Generation (RAG) workflows. With support for V
ector stores, Document loaders, and Chat Messages Memory, developers can seamlessly integrate Google Cloud databases int
o their workflow, speeding up the development of AI-powered solutions.

## Vector Search in Databases

It also extended 
its google cloud databases offerings with advanced vector search capabilities across various databases like Spanner, MyS
QL, and Redis. Vector search is crucial for building accurate GenAI-powered applications, allowing developers to find si
milar results for unstructured data such as text and images. By integrating vector search directly into its databases, G
oogle empowers developers to create GenAI apps with their preferred databases, ensuring performance and scalability are 
not compromised.

## Spanner and AlloyDB with Vertex AI

Integration of Spanner and AlloyDB with Vertex AI, enabling the
 use of SQL for model serving and inferencing. When Firestore and Bigtable are merged with Vertex AI Vector Search, GenA
I apps are equipped with semantic search abilities, ensuring timely, accurate, and contextually appropriate user experie
nces in business applications. This seamless fusion of operational data with GenAI is critical for fully harnessing the 
power of AI-driven apps, allowing businesses to provide personalized and smart user interactions on a vast scale.

&#x20
0B;

## How google cloud databases advancements helps you ?

Google’s advancements in AI-integrated databases offer a wi
de array of advantages and benefits for developers, businesses, and users alike. These advancements pave the way for eff
icient development, enhanced performance, improved search capabilities, easier integration, and personalized user experi
ences

**Efficient GenAI Application Development:** AlloyDB AI simplifies the storage, indexing, and querying of vector 
embeddings, streamlining the development process for context-aware applications.

**Enhanced Performance:** AlloyDB AI’s
 exceptional performance for transactional, analytical, and vector workloads is ideal for enterprise-level tasks. Furthe
r boosts performance, providing developers with tools to create high-performing GenAI applications.

**Open-source Frame
work:** LangChain, empowers developers to create GenAI applications with built-in Retrieval Augmented Generation (RAG) w
orkflows. It supports Vector stores, Document loaders, and Chat Messages Memory, ensuring seamless integration with Goog
le Cloud databases for enhanced flexibility and customization.

**Improved Search Capabilities:** Integration of advance
d vector search capabilities into databases like Spanner, MySQL, and Redis revolutionizes search functionalities. This i
ntegration is crucial for building accurate GenAI-powered applications, especially when dealing with unstructured data l
ike text and images.

[Twitter](https://twitter.com/TechJournalist/status/1763222103866663410?s=20)

**Easier Integratio
n:** LangChain’s integration with Google Cloud databases simplifies the development workflow, enabling developers to acc
elerate the creation of context-aware applications. This seamless integration streamlines the process, making it easier 
to leverage AI capabilities within existing systems.

**Fusion with Vertex AI:** The integration of Spanner and AlloyDB 
with Vertex AI enables the use of SQL for model serving and inferencing. Additionally, Firestore and Bigtable merging wi
th Vertex AI Vector Search equips applications with semantic search abilities. This fusion ensures timely, accurate, and
 contextually appropriate user experiences, enhancing the overall user interaction and satisfaction.

**Comprehensive To
olset:** Developers now have access to a comprehensive toolset comprising AlloyDB AI, LangChain, and Vertex AI. This com
bination provides a solid foundation for creating intelligent and innovative applications with the the full potential of
 AI-driven solutions, leading to enhanced products and services.

**Competitive Advantage:** Improved efficiency, perfor
mance, and search capabilities enable businesses to deliver better products and services to their customers. This compet
itive advantage allows companies to stay ahead of the curve.

**Scalability and Reliability:** Google cloud databases ad
vancements ensure scalability and reliability for [**GenAI**](https://www.sparity.com/blogs/things-to-consider-in-ai-pro
duct-development/) applications, critical for businesses operating at scale. Integration with Google Cloud’s infrastruct
ure provides a robust environment for growth.

## Conclusion

Google’s move towards supporting vector storage in current
 google cloud databases simplifies the development of enterprise GenAI applications. Coupled with its integration with L
angChain, developers now have the necessary tools to effectively utilize AI’s potential. With businesses increasingly ad
opting AI-driven solutions for competitive advantages, Google cloud databases advancements serve as a solid groundwork f
or developing the next era of intelligent and innovative applications.

## Why Sparity

Sparity’s expertise in AI-integr
ated databases, coupled with our proficiency positions us as your ideal partner for cloud database services. With Sparit
y, you can efficiently develop GenAI applications, enhance performance, integrate seamlessly, and gain a competitive adv
antage in the market. Our focus on scalability and reliability ensures your applications are future-proof and ready for 
growth. Partner with Sparity for your cloud database needs and unlock the full potential of AI-driven innovation if you 
are already on google cloud databases.

[https://www.sparity.com/blogs/google-cloud-databases-with-gen-ai-in-2024/](http
s://www.sparity.com/blogs/google-cloud-databases-with-gen-ai-in-2024/)
```
---

     
 
all -  [ How does LangChain foster community engagement and collaboration among language learners? ](https://www.reddit.com/r/u_fxdatalabs_Yp/comments/1beeccf/how_does_langchain_foster_community_engagement/) , 2024-03-16-0911
```
 

# How does LangChain foster community engagement and collaboration among language learners?

 

## Empowering Languag
e Learners: LangChain's Community Collaboration! 🌍🔗

 

## Introduction

[**LangChain**](https://fxdatalabs.com/) is com
mitted to fostering a vibrant and supportive community for language learners [**worldwid**](https://fxdatalabs.com/)e. T
hrough various initiatives and features, we strive to create an inclusive environment where [**learners**](https://fxdat
alabs.com/) can connect, [**collaborate**](https://fxdatalabs.com/), and [**support**](https://fxdatalabs.com/) each oth
er on their language learning journey. In this comprehensive article, we'll explore how LangChain fosters community [**e
ngagement**](https://fxdatalabs.com/) and collaboration among [**language learners**](https://fxdatalabs.com/).

📷

## I
nteractive Learning Platform

At the heart of [**LangChain's**](https://fxdatalabs.com/) community engagement efforts is
 our interactive learning platform. Through this platform, users can [**access**](https://fxdatalabs.com/) a wide range 
of language learning resources, including lessons, exercises, quizzes, and [**interactive**](https://fxdatalabs.com/) ac
tivities. [**Additionally**](https://fxdatalabs.com/), users can engage with fellow learners through discussion forums, 
chat rooms, and collaborative [**projects**](https://fxdatalabs.com/), fostering a sense of [**community**](https://fxda
talabs.com/) and camaraderie.

## Language Exchange Programs

LangChain facilitates [**language**](https://fxdatalabs.co
m/) exchange programs that allow users to connect with native speakers and practice their [**language**](https://fxdatal
abs.com/) skills in a real-world context. These programs match users based on their language [**proficiency**](https://f
xdatalabs.com/) and learning goals, enabling them to engage in [**meaningful**](https://fxdatalabs.com/) language exchan
ges and cultural exchanges. By [**participating**](https://fxdatalabs.com/) in language exchange programs, users can bui
ld relationships, gain cultural insights, and improve their [**language**](https://fxdatalabs.com/) proficiency through 
authentic [**interactions**](https://fxdatalabs.com/).

## Virtual Events and Workshops

📷

To further promote community
 [**engagement**](https://fxdatalabs.com/), LangChain organizes virtual events and workshops on language-related topics.
 These events cover a [**wide range**](https://fxdatalabs.com/) of subjects, including language [**learning**](https://f
xdatalabs.com/) strategies, cultural immersion, pronunciation practice, and more. Through live webinars, panel [**discus
sions**](https://fxdatalabs.com/), and interactive workshops, users have the [**opportunity**](https://fxdatalabs.com/) 
to learn from language experts, share their experiences, and connect with fellow learners from [**around**](https://fxda
talabs.com/) the world.

## Community Challenges and Competitions

📷

LangChain hosts community [**challenges**](https:/
/fxdatalabs.com/) and competitions to encourage active participation and [**collaboration**](https://fxdatalabs.com/) am
ong users. These challenges may include language [**learning**](https://fxdatalabs.com/) challenges, vocabulary quizzes,
 writing contests, and speaking competitions. By [**participating**](https://fxdatalabs.com/) in these challenges, users
 can set goals, track their progress, and compete with peers in a fun and [**motivating**](https://fxdatalabs.com/) envi
ronment. Prizes and [**incentives**](https://fxdatalabs.com/) may be offered to participants to further incentivize enga
gement and participation.

## Peer Support Networks

📷

LangChain facilitates the [**formation**](https://fxdatalabs.com
/) of peer support networks where users can seek advice, share resources, and provide support to [**fellow**](https://fx
datalabs.com/) learners. These networks may take the form of study groups, language clubs, or online [**communities**](h
ttps://fxdatalabs.com/) dedicated to specific languages or [**language**](https://fxdatalabs.com/) learning interests. T
hrough peer support networks, users can exchange tips, offer encouragement, and [**collaborate**](https://fxdatalabs.com
/) on learning projects, fostering a sense of [**belonging**](https://fxdatalabs.com/) and mutual support.

## Mentorshi
p Programs

To support learners at every stage of their [**language**](https://fxdatalabs.com/) learning journey, LangCh
ain offers [**mentorship**](https://fxdatalabs.com/) programs where experienced learners or language experts can mentor 
and guide newer learners. [**Mentors**](https://fxdatalabs.com/) provide personalized guidance, feedback, and support to
 mentees, helping them navigate [**challenges**](https://fxdatalabs.com/), set goals, and stay motivated. [**Mentorship*
*](https://fxdatalabs.com/) programs foster meaningful relationships and create opportunities for knowledge sharing and 
skill [**development**](https://fxdatalabs.com/).

📷

## Conclusion

In conclusion, [**LangChain**](https://fxdatalabs.c
om/) is dedicated to fostering a vibrant and supportive community for language learners [**worldwide**](https://fxdatala
bs.com/). Through interactive learning platforms, language exchange programs, virtual events, community [**challenges**]
(https://fxdatalabs.com/), peer support networks, and [**mentorship programs**](https://fxdatalabs.com/), LangChain prov
ides users with opportunities to connect, collaborate, and support each other on their [**language**](https://fxdatalabs
.com/) learning journey.

By [**nurturing**](https://fxdatalabs.com/) a sense of community and belonging, LangChain empo
wers learners to achieve their language [**learning**](https://fxdatalabs.com/) goals and embark on a rewarding and enri
ching language [**learning**](https://fxdatalabs.com/) experience.

For more insights into AI|ML and Data Science [**Dev
elopment**](https://fxdatalabs.com/), please write to us at: [**contact@htree.plus**](mailto:contact@htree.plus)| [**F(x
) Data Labs Pv**](mailto:contact@htree.plus)[**t. Ltd.**](https://fxdatalabs.com/)

**#LanguageLearning #CommunityEngage
ment #CollaborativeLearning #LangChain** 🗣️🤝
```
---

     
 
all -  [ Summarization Tool Tutorial with Langchain and Supabase as Vector DB ](https://www.reddit.com/r/LangChain/comments/1bed683/summarization_tool_tutorial_with_langchain_and/) , 2024-03-16-0911
```
If you are interested in embeddings, summarization and implementing a vector databas with Supabase and use Next JS as a 
framework alongside Langchain, check out this 40-minute tutorial:  


[https://youtu.be/92QqWVB6GNg?si=4M3hKLAoRuquq7nj]
(https://youtu.be/92QqWVB6GNg?si=4M3hKLAoRuquq7nj)
```
---

     
 
all -  [ Semantic Search on Certain Files Not Including All Data Stored in Vector DB ](https://www.reddit.com/r/LangChain/comments/1bed4o9/semantic_search_on_certain_files_not_including/) , 2024-03-16-0911
```
I currently have implemented semantic search that uses data in Vector DB and returns results matching query based on tha
t, how would I achieve search on only certain files would it be filtering on the metadata side? Is that efficient? So a 
real-world example would be what I have now is what one would use if they wanted to create an internal company chatbot t
rained on that company data and could answer any question if it's included in the data BUT what I am looking to achieve 
is let's say a department search where a chatbot answers questions about 1 or 2 files
```
---

     
 
all -  [ RAG at Production Scale with Cohere's New AI Model ](https://www.reddit.com/r/LangChain/comments/1becp91/rag_at_production_scale_with_coheres_new_ai_model/) , 2024-03-16-0911
```
Cohere just rolled out Command-R, a generative model optimized for long context tasks such as RAG and using external API
s and tools.

It targets the sweet spot between efficiency and accuracy for smoother transitions from prototypes to full
-scale production environments.

https://preview.redd.it/ol2omypp88oc1.png?width=2376&format=png&auto=webp&s=e160622a644
dec443eba0571e2d4f9d54223f2be

**Why Command-R Stands Out for RAG?**

1. Massive Context Window: Dive into deep discussi
ons with a whopping 128k token context window, ensuring no detail is left behind.
2. Speed & Efficiency: Engineered for 
enterprise, Command-R promises low latency and high throughput, making it a breeze to scale from prototype to production
.
3. Precision Meets Productivity: In tandem with Cohere’s Embed and Rerank models, Command-R enhances retrieval and und
erstanding, sharpening accuracy while keeping information relevant and trustworthy.
4. Global Reach: Speak the world's l
anguage with support for 10 key global languages, amplified by Cohere's models covering over 100 languages for seamless,
 accurate dialogues.
5. Benchmark Brilliance: Command-R excels in benchmarks like 3-shot multi-hop REACT and 'Needles in
 a Haystack,' proving its superiority in accuracy when paired with Cohere’s models.

Want to learn about the latest AI d
evelopments and breakthroughs. Join my newsletter Unwind with thousands of readers everyday - [https://unwindai.substack
.com](https://unwindai.substack.com/)
```
---

     
 
all -  [ Any opinions on the reranker used in the RAG pipeline? ](https://www.reddit.com/r/LangChain/comments/1be5caf/any_opinions_on_the_reranker_used_in_the_rag/) , 2024-03-16-0911
```
We have been building out the RAG pipeline at [www.querypal.com](https://www.querypal.com), and thinking of adding the c
ohere reranker vs GPT calls. Any suggestions here?
```
---

     
 
all -  [ NBA GPT project advice ](https://www.reddit.com/r/learnmachinelearning/comments/1be3qgd/nba_gpt_project_advice/) , 2024-03-16-0911
```
Hi,

I have a dataset of NBA player stats looking like this:

&#x200B;

https://preview.redd.it/823p5g5i86oc1.png?width=
1898&format=png&auto=webp&s=e3fe373d2ad419b5ebf649fc464a54d6a2814256

I want an llm (gpt4/mistral maybe) that can answer
 questions about this. Example questions is 'name the top 2 players on each team with highest 3 point %'. My vision is a
n NBA agent who knows all the nba data and can answer any question about it.

What is the way to make a basic working mo
del for this? I was thinking about using OpenAI's fine tuning feature to train it with this data. But I've also seen an 
approach of using 'Langchain and a vector SB store is the way to go'. Does anyone have any input on how to approach this
? Much appreciated.
```
---

     
 
all -  [ With Langserve as Backend how to make embeddable chatbot widget ](https://www.reddit.com/r/LangChain/comments/1be09zc/with_langserve_as_backend_how_to_make_embeddable/) , 2024-03-16-0911
```
Hi all,

How create a embeddable chatbot widgets


Is there any ready-made framework for that?


I wanna create a chatbo
t widget that can be integrated with any website.


Something like this.
<div id='chatbot-widget'>
    <!-- Placeholder 
for chatbot widget -->
  </div>
  <script>
    window.embeddedChatbotConfig = {
      apiEndpoint: 'https://your-api-end
point.com/chat',
      botName: 'ChatBot',
      botAvatar: 'bot.png'
    };
  </script>
  <script src='chatbot.js' defe
r></script>
```
---

     
 
all -  [ Need help creating a MongoDBAtlasVectorSearch retriever that filters other fields in the embedding ](https://www.reddit.com/r/LangChain/comments/1bdz0l1/need_help_creating_a_mongodbatlasvectorsearch/) , 2024-03-16-0911
```
Looking for help please.

I have a mongo retriever as follows:

	const retriever = new MongoDBAtlasVectorSearch(
		new O
penAIEmbeddings(),
		{
			collection,
			indexName: 'vector_index', 
			textKey: 'text', 
			embeddingKey: 'embedding', 
 
		}
	).asRetriever(4, {
		preFilter: {
			_user // need help here
		},
 	});

It runs fine without the preFilter, but 
I need it to return embeddings matching a specific _user, which is a string representing the user's id.

I'm kinda lost 
on how to accomplish this. Do I need to create special indexes? I'm not sure if using postFilterPipeline is correct eith
er since it would run *after* returning embeddings? Can't find much in the docs.

Thank you
```
---

     
 
all -  [ Langchain logger released ](https://www.reddit.com/r/LangChain/comments/1bdxpau/langchain_logger_released/) , 2024-03-16-0911
```
Howdy

I just released a langchain logger that I wrote a while back.

I had a couple of startups wanting to use langchai
n but display the chain of thought. 

You can retrieve it after the invoke is finished but I wanted to display it in rea
l time, so wrote a callback that wrapped a logger.

Please feel free to use it [https://github.com/thevgergroup/langchai
n-logger](https://github.com/thevgergroup/langchain-logger)

If you're using Flask we also released a viewer that pairs 
with this [https://github.com/thevgergroup/flask-log-viewer](https://github.com/thevgergroup/flask-log-viewer)

And lets
 you view the logs as they occur. 

&#x200B;
```
---

     
 
all -  [ RAG vs similarity search for chat bot use case ](https://www.reddit.com/r/LangChain/comments/1bdsxpc/rag_vs_similarity_search_for_chat_bot_use_case/) , 2024-03-16-0911
```
I'm working on a basic chat bot use case that would answer based on QnA knowledge base, how do I select between performi
ng traditional RAG pipeline or implementing similarity search on embeddings of KB and user's question and output the ans
wer. 
```
---

     
 
all -  [ Any solutions or alternatives for similarity search on vector DBs for short words with numerics? ](https://www.reddit.com/r/LangChain/comments/1bdqq09/any_solutions_or_alternatives_for_similarity/) , 2024-03-16-0911
```
So basically I am trying to search a cell line vector data base that has entries that look like this:  
'''

ID: 253F1


AC: CVCL\_B513

SY: NA

OX: NCBI\_TaxID=9606; ! Homo sapiens (Human)

CA: Induced pluripotent stem cell

'''

&#x200B;


There are easily tens of thousands of these entries in a text file that I store as a vector DB. I find that if I do a si
milarity search on say the 'Induced pluripotent stem cell', the similarity search always returns relevant documents. How
ever, If i search 253F1 or CVCL\_B513 its about a coin flip on whether the similarity search will return relevant docume
nts. The reason I need to do this form of search as opposed to a direct word match is because sometimes the input query 
will have varying forms of syntax eg: 253-F1 or 253.F1 or 253f1 this scaled over thousands of entries. Is there an alter
native to approaching these short queries? Something that I might find getting better results?

&#x200B;

Any help would
 be appreciated?
```
---

     
 
all -  [ How to create a conversational style AI chatbot which uses Mixtral 8x7b in AWS Sagemaker ](https://www.reddit.com/r/LangChain/comments/1bdqny9/how_to_create_a_conversational_style_ai_chatbot/) , 2024-03-16-0911
```
 Hey guys, I am a little confused on how I can create a conversational style AI chatbot which uses Mixtral 8x7b in AWS S
agemaker.

I understand when using Sagemaker, this would involve an endpoint URL which directly connects the LLM to say 
the front end UI.

1. Because of this, how do I code my script so that the AI chatbot will be able to remember previous 
messages in the flow of the conversation?
2. Does Mixtral 8x7b also uses the same format as OpenAI for their messages (s
ee below), so that I can just keep appending the messages for the memory of the LLM?

\`\`\`messages.append({'role': '',
 'content': message})\`\`\`

I am unsure if I had missed any other questions for me to be able to build this conversatio
nal style AI chatbot. Would really appreciate any help with this. Many thanks!
```
---

     
 
all -  [ Urgent Plan and Guidance needed ](https://www.reddit.com/r/LangChain/comments/1bdnzpl/urgent_plan_and_guidance_needed/) , 2024-03-16-0911
```
I Plan to use Langchain agent and AzureOpenAI and AzureOpenAIEmbeddings for the purpose of using a huge json dataset whi
ch contains indexed dict of Web APIs (with methods and function codes). And I mean to use a Langchain Agent to go throug
h it and generate me end-to-end test sequences of those APIs used in API testing.

Can someone give me an overview and a
 very Detailed plan of how I can accomplish this using langchain agent and my json file which contains the API data.

He
re is a sample of how my data looks like :

'2': {
        'Method': 'POST',
        'Path': '',
        'FunctionName':
 '',
        'FunctionCode': '{\...\}',
        'Queries': []
        'Description ' : []
    }



```
---

     
 
all -  [ So what IS the best way to create AI applications? ](https://www.reddit.com/r/LangChain/comments/1bdnzjm/so_what_is_the_best_way_to_create_ai_applications/) , 2024-03-16-0911
```
As far as I understood LangChain seems to become overly complicated at some point and many people say it's only good for
 demo purposes. 

So what IS actually the best way to create applications where agents can communicate with each other a
nd work as supposed to? I heard good things about Ollama here. But what is the overall smartest way to create functional
 applications if it's not LangChain?
```
---

     
 
all -  [ stop criteria ](https://www.reddit.com/r/LangChain/comments/1bdmhyx/stop_criteria/) , 2024-03-16-0911
```
how I can stop the generation process before the input (I want to stop it at first AI response) and how?

https://previe
w.redd.it/jwhozjqfc2oc1.png?width=1099&format=png&auto=webp&s=f47e21115e332e7be952839ed6dc55462b0c10a7
```
---

     
 
all -  [ How does LangChain ensure the quality and accuracy of language learning content available on its pla ](https://www.reddit.com/r/u_fxdatalabs_Yp/comments/1bdjyaw/how_does_langchain_ensure_the_quality_and/) , 2024-03-16-0911
```
 

# How does LangChain ensure the quality and accuracy of language learning content available on its platform?

 

## E
nsuring Quality and Accuracy in Language Learning Content on LangChain Platform

 

## Introduction

At LangChain, we [*
*understand**](https://fxdatalabs.com/) the importance of providing high-quality and accurate language learning content 
to our users. Our platform is [**designed**](https://fxdatalabs.com/) to offer [**comprehensive**](https://fxdatalabs.co
m/) and reliable resources that [**facilitate**](https://fxdatalabs.com/) effective language acquisition. In this articl
e, we'll delve into the various measures and processes we employ to ensure the quality and [**accuracy**](https://fxdata
labs.com/) of the content available on the [**LangChain**](https://fxdatalabs.com/) platform.

### Rigorous Content Cura
tion

📷

One of the [**primary**](https://fxdatalabs.com/) methods we use to maintain quality is through rigorous conten
t curation. Our team of language [**experts**](https://fxdatalabs.com/) and [**educators**](https://fxdatalabs.com/) met
iculously curates and [**reviews**](https://fxdatalabs.com/) all content before it is made available on the platform. Ea
ch piece of content undergoes thorough scrutiny to ensure [**accuracy**](https://fxdatalabs.com/), relevance, and lingui
stic [**authenticity**](https://fxdatalabs.com/).

### Expert-Authored Material

We [**prioritize**](https://fxdatalabs.
com/) content authored by language experts, educators, and native speakers to guarantee the highest level of [**accuracy
**](https://fxdatalabs.com/) and authenticity. By sourcing content from reputable publishers, educational institutions, 
and [**language**](https://fxdatalabs.com/) professionals, we ensure that our users have access to [**reliable**](https:
//fxdatalabs.com/) and authoritative learning materials.

## Continuous Feedback and Improvement

We actively seek [**fe
edback**](https://fxdatalabs.com/) from our users to identify areas for improvement and refine our content offerings. Th
rough user [**surveys**](https://fxdatalabs.com/), reviews, and analytics, we gather valuable insights into user [**pref
erences**](https://fxdatalabs.com/), learning outcomes, and content [**effectiveness**](https://fxdatalabs.com/). This f
eedback loop allows us to [**iteratively**](https://fxdatalabs.com/) improve our content selection and delivery [**metho
ds**](https://fxdatalabs.com/) to better meet the needs of our diverse user base.

### Multimodal Learning Resources

📷


[**LangChain**](https://fxdatalabs.com/) offers a diverse range of multimodal learning resources, including text-based 
lessons, audio [**recordings**](https://fxdatalabs.com/), videos, interactive exercises, and real-world simulations. By 
providing content in various [**formats**](https://fxdatalabs.com/), we accommodate different learning styles and [**pre
ferences**](https://fxdatalabs.com/), ensuring that each user can engage with the material in a way that best suits thei
r [**individual**](https://fxdatalabs.com/) needs.

### Quality Assurance Measures

To maintain the highest [**standards
**](https://fxdatalabs.com/) of quality and accuracy, we implement robust quality assurance measures throughout the [**c
ontent creation**](https://fxdatalabs.com/) and delivery process. This includes thorough [**fact-checking**](https://fxd
atalabs.com/), proofreading, and editing procedures to eliminate errors, inconsistencies, and inaccuracies. Additionally
, we employ [**plagiarism**](https://fxdatalabs.com/) detection tools to ensure that all content is original and [**ethi
cally**](https://fxdatalabs.com/) sourced.

### Integration of AI and Machine Learning

📷

We leverage advanced [**techn
ologies**](https://fxdatalabs.com/) such as artificial intelligence (AI) and machine learning to enhance the quality and
 effectiveness of our [**language**](https://fxdatalabs.com/) learning content. [**AI algorithms**](https://fxdatalabs.c
om/) analyze user interactions, preferences, and learning patterns to personalize content recommendations and [**optimiz
e**](https://fxdatalabs.com/) learning pathways. By [**harnessing**](https://fxdatalabs.com/) the power of AI, we contin
uously adapt and improve our content offerings to deliver a tailored and engaging [**learning**](https://fxdatalabs.com/
) experience.

### Interactive Assessments and Feedback

[**LangChain**](https://fxdatalabs.com/) incorporates interacti
ve assessments and feedback mechanisms to facilitate active learning and skill [**development**](https://fxdatalabs.com/
). Users receive immediate feedback on their progress, performance, and areas for improvement, [**enabling**](https://fx
datalabs.com/) them to track their [**proficiency**](https://fxdatalabs.com/) levels and target specific language skills
 for further practice and refinement.

### Integration of Technology

📷

[**Technology**](https://fxdatalabs.com/) plays
 a crucial role in enhancing the quality and effectiveness of our content. We leverage advanced [**technologies**](https
://fxdatalabs.com/) such as artificial intelligence (AI) and machine learning to [**analyze**](https://fxdatalabs.com/) 
user interactions and learning patterns.

This data-driven approach allows us to [**personalize**](https://fxdatalabs.co
m/) content recommendations, identify areas for [**improvement**](https://fxdatalabs.com/), and optimize learning [**pat
hways**](https://fxdatalabs.com/) for each user. By harnessing the power of [**technology**](https://fxdatalabs.com/), w
e can deliver a more tailored and engaging learning experience.

### Conclusion

At [**LangChain**](https://fxdatalabs.c
om/), our commitment to quality and accuracy is paramount. Through rigorous content curation, [**expert-authored**](http
s://fxdatalabs.com/) material, continuous feedback and improvement, multimodal learning resources, quality [**assurance*
*](https://fxdatalabs.com/) measures, integration of AI and [**machine learning**](https://fxdatalabs.com/), and interac
tive assessments and feedback, we ensure that our users have access to the most reliable, [**authentic**](https://fxdata
labs.com/), and effective language learning content available.

Join us on [**LangChain**](https://fxdatalabs.com/) and 
embark on your [**language learning**](https://fxdatalabs.com/) journey with confidence and success.

For more insights 
into AI|ML and Data Science [**Development**](https://fxdatalabs.com/), please write to us at: [**contact@htree.plus**](
mailto:contact@htree.plus)| [**F(x) Data Labs Pv**](https://fxdatalabs.com/)[**t**](https://fxdatalabs.com/)[**. Ltd.**]
(https://fxdatalabs.com/)

**#QuantumMachineLearning #Innovation #ComputationalScience #MultiverseComputing** 🌌🧠
```
---

     
 
MachineLearning -  [ [D] : Scale PDF Q&A App to 10K Users with GPUs – <$250/Mo ](https://www.reddit.com/r/MachineLearning/comments/1b6jv56/d_scale_pdf_qa_app_to_10k_users_with_gpus_250mo/) , 2024-03-16-0911
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

     
 
MachineLearning -  [ [D] What Is Your LLM Tech Stack in Production? ](https://www.reddit.com/r/MachineLearning/comments/1b4sdru/d_what_is_your_llm_tech_stack_in_production/) , 2024-03-16-0911
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

     
 
MachineLearning -  [ [D] Graphs + vectordbs? Need your input: Cognee.ai . AI Data Pipelines for Real-World Production (Pa ](https://www.reddit.com/r/MachineLearning/comments/1aweo71/d_graphs_vectordbs_need_your_input_cogneeai_ai/) , 2024-03-16-0911
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

     
 
MachineLearning -  [ [D] AI projects Suggestions ](https://www.reddit.com/r/MachineLearning/comments/1aunkmw/d_ai_projects_suggestions/) , 2024-03-16-0911
```
Hi Everyone, I need a suggestion to create AI courses for students ( Hands-on AI projects). I am thinking about the late
st AI trends such as Langchain, RAG, and vector databases. In each project, there can be multiple tasks, and the main th
ing is each task should have an automated system in which we can verify whether students have done it correctly or not.


For example: Project with visualization cannot be automatically tested. 

For example: A project with visualization can
not be automatically tested. . em can verify if the length of the text is smaller we can verify that it is correct.
```
---

     
