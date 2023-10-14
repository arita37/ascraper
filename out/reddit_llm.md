 
all -  [ Routing traffic through Custom Chains. Possible Bug. ](https://www.reddit.com/r/LangChain/comments/177c1ds/routing_traffic_through_custom_chains_possible_bug/) , 2023-10-14-0909
```
I am trying to use a MultiPromptChain to redirect traffic through some custom chains. 

However, it appears that there i
s a bug in the MultiPromptChain class. Instead of using the custom chains I have supplied it with in destination\_chains
, the class re-writes the chain objects.  

You can see in the screenshot that the objects are different - they are even
 instances of different classes. How am I supposed to route traffic through custom chains? Crazy frustrating that this i
sn't made more clear. 

[Why is blast\_api\_chain redefined as an LLMChain object?](https://preview.redd.it/gboaxd9d22ub
1.png?width=594&format=png&auto=webp&s=1f2ce20fc6916ea0e2b96b47210527a3e6f56e82)

&#x200B;
```
---

     
 
all -  [ Not acknowledging custom function ](https://www.reddit.com/r/LangChain/comments/177bc6j/not_acknowledging_custom_function/) , 2023-10-14-0909
```
Hey everyone!

I created a custom function, which im using as tool in create_pandas_dataframe_agent. The purpose of the 
tool is to upload the returned dataframe to s3 and return the S3 URL. Even with specific prompting to acknowledge the to
ol, it tells me that it’s not a “valid tool”.

Snippet of code below. Looking for an guidance. Additionally, looking for
 freelance work to help me with the development. If interested, feel free to DM me. Thank I’m advance!

tools = [
    To
ol(
        name = 'dataframe uploader to aws s3',
        func = dataframeUpload,
        description = 'Uploads pandas
 dataframes to AWS S3. Accepts a valid pandas dataframe'
    )
]


df = pd.read_csv(url)

llm = ChatOpenAI(model=model)

agent = create_pandas_dataframe_agent(llm, df, verbose=True, return_intermediate_steps=True, extra_tools=tools)
agent.ag
ent.llm_chain.prompt.template = '<add custom prompt here>'

response = agent(query)
```
---

     
 
all -  [ AI-powered Real-time Trend Reporting | In Seconds ](https://youtu.be/HckZGWeQRrY) , 2023-10-14-0909
```

```
---

     
 
all -  [ How businesses can use GPT with their own data ](https://www.reddit.com/r/Entrepreneur/comments/1777x94/how_businesses_can_use_gpt_with_their_own_data/) , 2023-10-14-0909
```
There’s many business use cases for a custom chat interface like ChatGPT, but using the company’s own internal content a
s the source. Think company policies, documents, project resources, etc.

I’ve been wrapping head around, and building, 
GPT projects for the past 2 years (software dev of 7 years). Always learning, but what I’m sharing is basically the stan
dard approach to create a custom ChatGPT-like application that you can add your own data to.

If you know how to program
, you could explore Open Source libraries like LangChain to handle processing of custom data. It’s a free program that m
akes the process of interacting with different LLMs easier. Next you’ll want to connect it to a vector database to make 
the processed data available for referencing, and finally OpenAI’s API for the LLM generations (or your LLM of choice).


Regardless of the solution you choose, how all this works from a technical perspective is:

1. You need to break up any
 large text content into smaller pieces. This process is called chunking. You do this to later make each chunk searchabl
e in the vector database.
2. ⁠You’ll want to vectorize each chunk and add this vector into a database. By doing this, yo
u can embed (vectorize) natural language to search the vector database for relevant chunks.
3. With the returned chunks,
 you can combine them all (within respects to the context window limit of the LLM of choice), and now your generated res
ponse will contain the information it needs to give you an accurate output.

Making a secure and privacy-focused solutio
n for businesses is also important. If you use the OpenAI API, data is not used to train their models (source [OpenAI En
terprise Privacy](https://openai.com/enterprise-privacy)).

I hope this makes sense. Let me know if there’s any question
s on the topic.
```
---

     
 
all -  [ AI SDK with Langchain ](https://www.reddit.com/r/LangChain/comments/1774dek/ai_sdk_with_langchain/) , 2023-10-14-0909
```
Can anybody help me with this ... the streaming cuts off

i am using the vercel SDK

https://preview.redd.it/c39406lwb0u
b1.jpg?width=1130&format=pjpg&auto=webp&s=5d53469e35abab36e72e3c588f35fad83bd5812f

https://preview.redd.it/8tjkgjlwb0ub
1.jpg?width=1210&format=pjpg&auto=webp&s=5ffeabc6ee2a2932dbc1b0f174e32ace2e74b720
```
---

     
 
all -  [ Need advice from experienced CS people regarding what should I do? ](https://www.reddit.com/r/careerguidance/comments/177497v/need_advice_from_experienced_cs_people_regarding/) , 2023-10-14-0909
```
My bachelor's degree is in Industrial Automation and Robotics and I have a masters in Advanced Software Engineering. I'm
 currently working on house projects for my current company. some of them on a proprietary outdated IoT platform (DGLux)
. But I have also worked on Building in-house chatbots using Python, GPT 4, Vectorstores, and Langchain. Also I do have 
some experience in ReactJS, C# andNode-Red as well. But I don't see any clear path around this kind of tech stack. When 
it comes to academics I do have some experience in ML model development as well. Expecting ideas to level up as an engin
eer.
```
---

     
 
all -  [ Need to advice from experienced CS people ](https://www.reddit.com/r/careeradvice/comments/17746bd/need_to_advice_from_experienced_cs_people/) , 2023-10-14-0909
```
My bachelor's degree is in Industrial Automation and Robotics and I have a masters in Advanced Software Engineering. I'm
 currently working on house projects of my current company. some of them on a proprietary outdated IoT platform (DGLux) 
. But I have also worked on Building in house chatbots using Python, GPT 4, Vectorstores, and Langchain. Also I do have 
some experience in ReactJS,C# andNode-Red as well. But I don't see any clear path around this kind of tech stack. When i
t comes to academics I do have some experience in ML model development as well. Expecting a ideas to level up as an engi
neer.
```
---

     
 
all -  [ Chatbot with Langchain Javascript ](https://www.reddit.com/r/LangChain/comments/1772g4u/chatbot_with_langchain_javascript/) , 2023-10-14-0909
```
Chatbot using Langchain with JavaScript and Openai

Frontend: Next.js

What do you think of JavaScript in AI projects?


Repo: [Chatbot](https://github.com/Deluxer/gpt-chatbot-langchain-js)

https://i.redd.it/r8oy6a96vztb1.gif
```
---

     
 
all -  [ Train AI on data and emails? ](https://www.reddit.com/r/ChatGPTPro/comments/1771us3/train_ai_on_data_and_emails/) , 2023-10-14-0909
```
Hi all, I’m wondering if anyone has any thoughts about how to do this: I want to train ChatGPT on a large amount of info
rmation, including websites, pdfs, and outlook emails. I’m trying to start off with something easy that can help me with
 some of my work report writing, but ultimately this is what I really want: read all of my emails (outlook), provide me 
with a summary of them, allow me to have the ai draft replies, have the ai draft options for follow ups (I.e. meetings e
tc.). I know that training an AI model on documents for the first thing is possible, thought tools like Langchain, but i
s the email part of what I am looking for possible? TIA for your thoughts/help
```
---

     
 
all -  [ [News] AI & ML conference in San Francisco [Special discount code for this subreddit] ](https://www.reddit.com/r/MachineLearning/comments/1771m35/news_ai_ml_conference_in_san_francisco_special/) , 2023-10-14-0909
```
I work for this database company SingleStore and we are hosting a AI & ML conference in San Francisco on 17th of October
, 2023.

It is an in-person conference with amazing speakers line-up like Harrison Chase, co-founder and CEO of LangChai
n and many more. We will have hands-on workshops, swags giveaway and much more.

I don't know if it makes sense to share
 this but I believe it might help some of you near San Francisco to go and meet the industry leaders and network with ot
her data engineering folks.

Use my discount coupon code 'PAVAN100OFF' to avail 100% off on the ticket price. (the origi
nal ticket price is $199)

[Get your tickets now!](https://singlestore.com/now)
```
---

     
 
all -  [ Data & AI conference happening in San Francisco: 100% off on the ticket price! ](https://www.reddit.com/r/dataengineering/comments/1770yer/data_ai_conference_happening_in_san_francisco_100/) , 2023-10-14-0909
```
I work for this database company SingleStore and we are hosting a Data and AI conference in San Francisco on 17th of Oct
ober, 2023.

It is an in-person conference with amazing speakers line-up like Harrison Chase, co-founder and CEO of Lang
Chain and many more. We will have hands-on workshops, swags giveaway and much more.

I don't know if it makes sense to s
hare this but I believe it might help some of you near San Francisco to go and meet the industry leaders and network wit
h other data engineering folks.

Use my discount coupon code 'PAVAN100OFF' to avail 100% off on the ticket price. (the o
riginal ticket price is $199)

[Get your tickets now!](https://singlestore.com/now)
```
---

     
 
all -  [ Need Some Directions ](https://www.reddit.com/r/LangChain/comments/1770oj4/need_some_directions/) , 2023-10-14-0909
```
I'm trying to build a recommendation system for real estate property listings as per user preferences. 

Let's say I hav
e a dataframe with over 50k listings. Columns are property address, Size, nBHK, Area, City, price range, other informati
on like swimming pool, park, etc. 

What would be the most efficient way to provide this data to a LLM? Will a simple da
taframe loader work? 

I don't have access to the df right now.
```
---

     
 
all -  [ Privacy Compliance and Records Retention for LangChain Apps ](https://www.reddit.com/r/LangChain/comments/1770978/privacy_compliance_and_records_retention_for/) , 2023-10-14-0909
```
Hey all, we've just launched **Zep Archive**, offering easy-to-implement tools for LangChain chat apps to comply with **
records retention and privacy compliance regulations**. If you're using Zep's `ZepMemory` class in your app, you get the
se features with no additional effort.

&#x200B;

>Building a production-ready user-facing app requires complying with d
ata privacy regulations such as California's CCPA and the EU's GDPR. For many applications, retention of records for a p
eriod of time is also required. Apps with conversational interfaces powered by LLMs are no different.  
>  
>Zep Archive
 is a collection of features available in Zep that support meeting these data governance challenges, including archiving
 all message histories and executing Right To Be Forgotten requests.

Get **Zep Open Source**: [https://docs.getzep.com/
deployment/quickstart/](https://docs.getzep.com/deployment/quickstart/)

More info on **Zep Archive**: [https://blog.get
zep.com/announcing-zep-archive-regulatory-compliance-and/](https://blog.getzep.com/announcing-zep-archive-regulatory-com
pliance-and/)

&#x200B;

https://preview.redd.it/5syy6bpeeztb1.png?width=1792&format=png&auto=webp&s=5d60a533eedb56ce6f3
a79d791ce83b163e7d487
```
---

     
 
all -  [ Vectorizing notes & chat history ](https://www.reddit.com/r/LangChain/comments/17708ki/vectorizing_notes_chat_history/) , 2023-10-14-0909
```
I have a question for my general understanding:

I'm building a chatbot for a note-taking app that uses vector embedding
s to **find relevant user notes for an AI chat**.

Right now, I **vectorize the whole note** (no matter how big) and sto
re that result in Pinecone.

For my search input, I then vectorize the **last 8 messages** and use this to query my DB.


This approach is simple and seems to work. Do I need to be more granular (e.g. index chunks of text rather than whole n
otes, or single messages from the chat)?

Some code examples:

Embedding user notes when they are created:

    const ne
wNote = await prisma.note.create({
      data: {
        title,
        content,
      },
    });
    
    const embeddi
ng = await getEmbeddingsForNote(newNote);
    
    await notesIndex.upsert([
      {
        id: newNote.id,
        val
ues: embedding,
      },
    ]);

Embedding the chat history:

        const chatMessages: Message[] = json.messages;
  
  
        const messagesTruncated = chatMessages.slice(-8);
    
        const queryEmbedding = await getEmbedding(
   
       messagesTruncated.map((message) => message.content).join('\n'),
        );
    
        const vectorQueryResponse
 = await notesIndex.query({
          vector: queryEmbedding,
          topK: 5,
        });
    
        const relevant
Notes = await prisma.note.findMany({
          where: {
            id: {
              in: vectorQueryResponse.matches.
map((result) => result.id),
            },
          },
        });
```
---

     
 
all -  [ Authoring another course about LLMs. Learn by Doing LLM Projects. ](https://www.reddit.com/r/learnmachinelearning/comments/176zx1m/authoring_another_course_about_llms_learn_by/) , 2023-10-14-0909
```
Hi, I'm working on a course about LLMs on GitHub, it's totally free and under MIT license,  So there are no restrictions
.

Here the link: [https://github.com/peremartra/Large-Language-Model-Notebooks-Course](https://github.com/peremartra/La
rge-Language-Model-Notebooks-Course)

I'm still working on It, but now I'm feeling comfortable with the variety and qual
ity of the content. By the moment is a small repository with just 80 Stars.

My intention is to make the course more acc
essible to a wider audience, and, if possible, encourage  reporting any issues  encounter or suggesting improvements thr
ough the 'Discussion' section.

I'm eager to receive feedback.

Now, I'll provide an overview of the currently available
 content, and then I'll share a couple of questions I have about how to proceed with the course.

[Large Language Models
 Course: Learn by Doing LLM Projects.](https://github.com/peremartra/Large-Language-Model-Notebooks-Course)

* Introduct
ion to LLM with OpenAI.
   * Create a first Chatbot using FPT 3.5.
   * Create a Natural Language to SQL Translator usin
g OpenAI.
* Vector Databases with LLM.
   * Influencing Language Models with Information stored in ChromaDB.
* LangChain
 & LLM Apps.
   * RAG. Use the Data from Dataframes with LLMs.
   * Create a Moderation System using LangChain.
      * 
OpenAI.
      * GPT\_j.
      * LLama-2.
   * Create a Data Analyst Assistant using a LLM Agent.
* Evaluating LLMs
   * 
Evaluating Summarization with ROUGE.
* Fine-Tuning & Optimization.
   * Prompt-tuning using PEFT.
   * Fine-Tuning with 
LoRA.

That's all for the moment, but I'm adding new content regularly. I'm working on it only in my spare time (mainly 
nights when the family goes to sleep).

\_\_\_

I have a doubt, I don't know if add some information about platforms lik
e W&B or Cohere?  or maybe it is a better idea to stay with more Open-Source libraries?

On the other hand, my intention
 is to develop a couple of projects utilizing the techniques covered in the initial part of the course (which I am curre
ntly working on).

Some of these projects will be hosted in the cloud on major platforms such as Azure or GCP, or AWS. A
ny preference? 

Furthermore, there is a plan to create a third section that explains how Large Language Models (LLMs) f
it into large-scale enterprise solutions, defining architectures in which LLMs are used but are not the sole components 
of the project.

I don't intend to create a community outside of GitHub, but I would like the repository to have more ac
tivity and not be the one determining the course's direction.

Hope you like it, and lease, feel free to contribute.

&#
x200B;
```
---

     
 
all -  [ Limiting options for user prompts? ](https://www.reddit.com/r/OpenAI/comments/176vpss/limiting_options_for_user_prompts/) , 2023-10-14-0909
```
We have a platform for data analytics which uses a very simple dsl to generate charts.  
We have been experimenting with
 llms to use natural language that gets translated into this dsl and hence generates charts.

This is working pretty goo
d.  
The stack is langchain with openai api. (don't have much experience with llms, it's a prototype to get a feel for i
t)

The question is what is the best way to limit the options user can type in as a prompt.  
Basically the the only all
owed things should be: 'What is the X, Y over 10 days period for this or that?'  
I don't want users to ask questions li
ke when did we first land on the moon.

Is it something that is possible to do at all without additional tooling?  
We p
robably don't want to train another model to classify the prompt as valid or invalid or something similar.
```
---

     
 
all -  [ learning langchain ](https://www.reddit.com/r/LangChain/comments/176t09e/learning_langchain/) , 2023-10-14-0909
```
hello i am new here.

i just started learning langchain and while going through the courses all i see is people using op
enai to teach it and my usage limit is already over.

I want to use it for huggingface models. do you guys know any good
 place to learn langchain for huggingface models.

Also i want to know if people mostly use langchain with openai and ma
ybe i should focus on using it because the price is kinda low or is it fine if i stick with huggingface hub for free

&#
x200B;
```
---

     
 
all -  [ New to this. My boss asked me to use LLM's to disclose information in conversations. Is this feasibl ](https://www.reddit.com/r/LocalLLaMA/comments/176s1ej/new_to_this_my_boss_asked_me_to_use_llms_to/) , 2023-10-14-0909
```
I'm new to LLMs. I want to know if what I want is feasible before I go into the deep end and enter this wonderful world.
  

I have a bunch of conversations between personnel of a company, with lots of domain specific jargon, lots of convers
ations everyday. And my boss asked me if I could use an LLM to disclose the information within. So you could ask in natu
ral language and it responds in natural language.  

eg ' what happened on the warmest day of the year?' or 'what happen
ed when three deliveries arrived at the same time?'  

I'm looking at things like langchain and llamaindex, or maybe fin
etuning with the convos, but I'm not sure if this is the right way to go.  

I'm not sure about the format (json, a data
base, xml, something different), but I don't think that matters much.
```
---

     
 
all -  [ Seeking Orientation on Developing an LLM-Based QA Chatbot ](https://www.reddit.com/r/LocalLLaMA/comments/176om1d/seeking_orientation_on_developing_an_llmbased_qa/) , 2023-10-14-0909
```
Hello everyone,

In the context of my degree thesis, I am developing a QA-chatbot based on the LLM model for Chilean law
. As I am Chilean, the chatbot will primarily be in Spanish. I'm aware of the necessity to use the RAG architecture, but
 I have additional questions.

The tech stack I'm considering includes:

* Langchain as the orchestrator
* LLaMA 2 7B as
 the LLM (or a similar model)
* Streamlit for the frontend
* ChromaDB as the vector store (housing 350,000 norms from Ch
ilean legislation) for external knowledge retrieval.

  
I aim to use only open-source or free license software.

[Dalle
-3 generated image, prompt: Photo of a dignified llama dressed as a Chilean lawyer, standing in front of a courtroom. Th
e Chilean flag is draped behind the judge's bench, and the llama has a stern but fair expression.](https://preview.redd.
it/ur1omzmpvvtb1.png?width=1024&format=png&auto=webp&s=414a32cb393ec5742219b1793f5155badb6e0a67)

Here are my questions:


1. ~~At the moment, I possess an M1 MacBook Air and a desktop PC with a 1650 Super Nvidia GPU. Are these devices robus
t enough for developing and testing the chatbot?~~ Based on various posts, I believe I might only be able to run LLaMA 2
 7B (which can produce hallucinations even with RAG) on my desktop PC's CPU. Thus, I'm considering online alternatives. 
Would you recommend any user-friendly platforms similar to Colab?
2. ~~Would a different model be more effective in term
s of performance?~~ I will be using LLaMA 2 models, following the recommendations from the highlighted post.
3. ~~I'm le
aning towards LLaMA C++. Is LLaMA 2 7B suitable?~~ How challenging would it be to incorporate it into the tech stack I'v
e listed?
4. In terms of frontend technology, can you suggest any alternatives that might streamline the implementation 
process?
5. ~~Lastly, is using a Docker container essential?~~ **Edit:** I'm considering the need to utilize containers.
 Does anyone have architectural implementation examples? For instance, I'm thinking about configurations like having a l
ocal frontend and local vector store, and an online model setup (in a platform). Other suggestions or setups that have w
orked for you would be greatly appreciated.

Any insights or advice will be highly valued. Thank you!

Best regards, Eme
r
```
---

     
 
all -  [ May 2024 Grad. 300+ applications since July. 75 rejections. No job yet ](https://www.reddit.com/r/csMajors/comments/176o2jv/may_2024_grad_300_applications_since_july_75/) , 2023-10-14-0909
```
 I'm a US Citizen studying outside the US (in a not very well-known school). Looking for new grad roles.

300 applicatio
ns. 75 rejections. Around 22ish hirevues/OAs. Got to the phone interview stage with just 1 COMPANY.

Please help me see 
what I'm doing wrong.

&#x200B;

&#x200B;

https://preview.redd.it/x7qbz4u4qvtb1.png?width=616&format=png&auto=webp&s=5a
735efd6fc4013487cad641c80b9ef279786b29
```
---

     
 
all -  [ llama2 13b hallucination on a retrival based bot ](https://www.reddit.com/r/LocalLLaMA/comments/176a0gv/llama2_13b_hallucination_on_a_retrival_based_bot/) , 2023-10-14-0909
```
looking for some suggestions on how to manage llama2 hallucination. I have a retrieval based bot where the model gets th
e data from vectors which contains data from multiple pdf. Now the challenge is if vector contains two set of totally di
fferent data for example one talks about container orchestration and another about a order processing system of online s
tore, i notice that model gets completely hallucinated . here is an example:-  
User:- what is contrainer orchestration 
 
Bot :- container orchestration refers to a process of .....  
USer:- so can i order pizza using it?  
Bot:- Yes you ca
n order pizza as the Order processing takes the new order and looks for the inventory to allocate .....  


I have used 
RAG via langchains RetrievalQA . This was suppose to solve this problem but i don;t have any luck.  Any suggestion would
 be of great help.
```
---

     
 
all -  [ [Langchain] Mistralai LLM avec Langchin ](https://www.reddit.com/r/redditenfrancais/comments/1762y5q/langchain_mistralai_llm_avec_langchin/) , 2023-10-14-0909
```
Langchain soutient-il le modèle AI LLM Mistral?

Traduit et reposté à partir de la publication https://www.reddit.com/16
vwilm
```
---

     
 
all -  [ A Chatbot using Langchain to integrate LLM with MongoDB memory and LangSmith to tracing LLM calls. ](https://www.reddit.com/r/LangChain/comments/1762tkr/a_chatbot_using_langchain_to_integrate_llm_with/) , 2023-10-14-0909
```
Hey guys,

We are developing a chatbot using Langchain framework. My idea is that Bot can talk with user based on their 
info, hobbies and personalities. These info will be collected by LLM and each turn it will be ingested to the prompt. Th
ank to it, maybe it can talk more friendly.

We use MongoDB as memory and LangSmith to tracing bot's LLM calls. It still
 be developed and updating more features.

If you find it useful or see anything that needs improvement, please let our 
know.

Here is the link to it : [Chatbot with Langchain](https://github.com/btrcm00/chatbot-with-langchain)
```
---

     
 
all -  [ Existing relational database to new vector database? ](https://www.reddit.com/r/datascience/comments/1761n34/existing_relational_database_to_new_vector/) , 2023-10-14-0909
```
I'm in the very early stages of an investigatory project at my job (senior software engineer with a moderate amount of d
ata mining and snowflake/star pattern ETL OLAP warehousing experience in SSAS from years ago, long before modern tools a
nd platforms, who has somehow now been deemed the SME for all things 'AI').

Basically, I have a relational SQL Server d
atabase containing tens of millions of products, each with up to 20 categories of detail. I also now have usage data fro
m our website that tracks customer interaction with these products, logging things like their account details and demogr
aphics as well as their IP, location, searches, where they clicked, how long they interacted, what they interacted with 
previously, what they interacted with next, etc.

If they wanted to run this in an old-school schema, I could work somet
hing up. I could probably even make some great reports in Power BI. But my bosses, of course, want to load this into a C
hatGPT-type interface to ask natural language questions about the data.

My cursory research tells me I need to massage 
my data into a vector database first and foremost before I start worrying about Langchain, Llama, and OpenAI, and any sp
ecific platform or toolset. But I'm not sure where to start, and I'm getting hung up on that there doesn't seem to be an
y good examples of migrating existing data - everything is either too much hype and promise-selling language that is spa
rse on detail or is a very in-the-weeds, poorly documented, mostly-incoherent mess with no examples at all or uses examp
les that are so simplistic to be not relevant to anyone.

I found some (albeit again very simplistic) examples from Milv
us that show importing semi-structured JSON-formatted objects that roughly align with what I'd equate to, in my world, d
enormalized key/value pairs for various product properties. Cool, that makes sense. That's half of it. But I'm not sure 
about the other half - how much, if any, pre-aggregation do I need to do with the analytics data? Do I import essentiall
y one object for every single piece of tracked data, or do I roll it up beforehand? I'm most interested in having this v
ector data be used to identify period-based trends, forecasts, and recommendations like 'Based on his individual product
 engagement tracking as well as the aggregate tracking of his demographically similar cohorts over the past week, what p
roducts should we surface for Bob Smith next?'

Basically, all this is a very long-winded, rambling way to get to three 
questions:

1. Are there any examples of converting a remotely complex RDMS into a vector database?

2. How much massagi
ng beyond basic denormalization and pre-aggregation do I need to do?

3. Is it sufficient to load data as lists of a but
tload of key-value pairs, or would I do better to zhuzh it into wordy natural language descriptions of the data?
```
---

     
 
all -  [ Positional metadata from PDFloaders? ](https://www.reddit.com/r/LangChain/comments/175qj2b/positional_metadata_from_pdfloaders/) , 2023-10-14-0909
```
The headline kind of says it all. Is it possible to get the positional metadata of the pieces of text you create from th
e text splitter? Would greatly enhance the user experience. Right now I'm just showing the pieces of text when mouse is 
hovering over a link
```
---

     
 
all -  [ [Langchain] Comment déployer le script Langchain Python à la production ](https://www.reddit.com/r/redditenfrancais/comments/175hqpo/langchain_comment_déployer_le_script_langchain/) , 2023-10-14-0909
```
Hé les gens! Je veux donc créer une application Web pour les entreprises de mon pays en tirant parti de la puissance de 
Langchain.

Mon problème est que je n'ai jamais déployé un seul script python dans un environnement de production, donc 
je ne sais pas par où commencer.

Je préférerais éviter les outils tels que rationaliser et gradio car les interfaces ut
ilisateur qu'ils ont ne sont pas idéales.

Au lieu de cela, je voudrais un frontend à faible code (Framer, Wix, WordPres
s, Bubble, etc.) avec lequel je peux facilement intégrer mon script Python. Cela ne me dérange pas non plus d'apprendre 
un peu de HTML, CSS, JS etc. si nécessaire, mais la situation idéale serait le frontage à faible code.

Connaissez-vous 
des ressources ou avez-vous déployé une application Web AI avec Langchain à l'aide d'un outil de code bas? J'adorerais e
ntendre des conseils et être pointé dans une certaine direction

Traduit et reposté à partir de la publication https://w
ww.reddit.com/145o0h5
```
---

     
 
all -  [ How does the pipe '|' symbol work in Python from this LangChain example? ](https://www.reddit.com/r/LangChain/comments/175edd4/how_does_the_pipe_symbol_work_in_python_from_this/) , 2023-10-14-0909
```
I'm not that experienced in Python and this is my first time trying LangChain.

In the example provided by the doc [http
s://python.langchain.com/docs/modules/agents/](https://python.langchain.com/docs/modules/agents/) , there is this one sn
ippet:

    from langchain.agents.format_scratchpad import format_to_openai_functions
    from langchain.agents.output_p
arsers import OpenAIFunctionsAgentOutputParser
    agent = {
        'input': lambda x: x['input'],
        'agent_scrat
chpad': lambda x: format_to_openai_functions(x['intermediate_steps'])
    } | prompt | llm_with_tools | OpenAIFunctionsA
gentOutputParser()

Then the \`agent\` variable is passed into \`AgentExecutor\`:

    agent_executor = AgentExecutor(ag
ent=agent, tools=tools, verbose=True)
    agent_executor.invoke({'input': 'how many letters in the word educa?'})

I und
erstand how \`prompt\` can be piped with \`llm\_with\_tools\`, because the type of \`prompt\` overrides the function \`\
_\_or\_\_\`, but how does piping dictionary and \`prompt\` work?
```
---

     
 
all -  [ Help with ideas for a project? ](https://www.reddit.com/r/AskRobotics/comments/175c4x6/help_with_ideas_for_a_project/) , 2023-10-14-0909
```
Help with an idea?

So I want to make what I’ve dubbed the everythingbot2023 because I want to try and combine every som
ewhat reasonably feasible diy robotics/ai/electronics project up until 2023 into one robot. I’m looking for more ideas t
o add.

Here is what I have so far:

•Stair climbing tracks •computer vision robotic arm •internal 3d printer- arm can g
rab 3d printed objects •offline chatbot voice response LLm-speaker/microphone- langchain+streamlit+llama 
•LiDAR- ledge/
object detection •top mount image recognition camera •face tracking mini airsoft turret •floor projector •sense of touch
 strips  •fingerprint scan top storage container •solar panel.
 
   Of course I want to interconnect all of those parts 
with the LLm as much as possible. Also I want it to have a little plant on top that it monitors and waters.
     
I am n
ot looking for advice. I fully understand how ridiculously over-ambitious this is, and I probably won’t be able to do mo
re than a few features, but hopefully someone else, or a group of people will steal the idea. But what I’m looking for i
s more “technically” feasible ideas to throw into this conglomeration. Just to have it all on the list, I know there has
 to be way more. Anything from other robotics projects to just electronics projects to add. Thank you.
```
---

     
 
all -  [ Getting Started with GenAI Stack powered with Docker, LangChain, Neo4j and Ollama ](https://www.reddit.com/r/u_ajeetsraina/comments/175ay08/getting_started_with_genai_stack_powered_with/) , 2023-10-14-0909
```
[https://collabnix.com/getting-started-with-genai-stack-powered-with-docker-langchain-neo4j-and-ollama/](https://collabn
ix.com/getting-started-with-genai-stack-powered-with-docker-langchain-neo4j-and-ollama/) 
```
---

     
 
all -  [ test effectiveness embeddings retrievalQA chatbot ](https://www.reddit.com/r/LangChain/comments/1758n1i/test_effectiveness_embeddings_retrievalqa_chatbot/) , 2023-10-14-0909
```
I have developed a chatbot that uses mistral7B instruct as LLM connected to a DB of embeddings to generate answers basin
g on context. 

The documents I am trying to embed are \~800 pdfs and the the embedding process entails splitting these 
documents (after a preprocessing) using HuggingFaceTokenizer ([https://python.langchain.com/docs/modules/data\_connectio
n/document\_transformers/text\_splitters/split\_by\_token#hugging-face-tokenizer](https://python.langchain.com/docs/modu
les/data_connection/document_transformers/text_splitters/split_by_token#hugging-face-tokenizer)) with the tokeniser of m
istral. The chunks length that I tried are \[50,200,300,400,500,750\] with the overlap of 1/3, this is the my embedding 
function: [https://huggingface.co/BAAI/bge-large-en-v1.5](https://huggingface.co/BAAI/bge-large-en-v1.5), chain type stu
ff and 6 docs retrieved. 

All sounds good until I read through the documents, make some test questions and realise the 
documents retrieved are very rarely the ones I was hoping to get. 

Anyone has faced a similar problem?
```
---

     
 
all -  [ Extending Workshop Learnings: A Dive into Supabase, PGvector, and LangChain ](https://www.reddit.com/r/Supabase/comments/1755wzh/extending_workshop_learnings_a_dive_into_supabase/) , 2023-10-14-0909
```
&#x200B;

https://preview.redd.it/4sgc6gps7itb1.png?width=1224&format=png&auto=webp&s=374c6d0c1bfcf16f590c9b4a698067d467
b8c873

I had the privilege of attending the 'Pgvector to Prod in 2 hours' workshop led by Greg Richardson at the recent
 AI Engineer Summit. The workshop was a deep dive into Supabase and PGvector, teaching us how to rapidly build a secure,
 production-ready web app.

Being someone who has been working with LangChain, I found this workshop as an opportunity t
o compare, learn, and enhance my understanding of these tools. I've articulated my journey, findings, and the contrastin
g insights between Supabase, PGvector, and LangChain in my latest blog post titled **'Extending Workshop Learnings: From
 Supabase and PGvector to LangChain'**.

In the post, I also share how this experience has inspired me to venture into a
 new project with LangChain, focusing on the rapid development and scalability of AI applications.

I've included code s
nippets, insights on text embedding generation, and a comparative analysis that could be a good read for anyone keen on 
AI application development. I’d love to hear your thoughts, feedback, or any questions you might have. Feel free to shar
e your comments here or on the blog post!

Thank you and happy reading! 📖

&#x200B;

Twitter: [https://twitter.com/arpag
on/status/1711965601797656962](https://twitter.com/arpagon/status/1711965601797656962)   
Blog Post: [https://blog.artis
anlabs.io/posts/supabase-pgvector](https://blog.artisanlabs.io/posts/supabase-pgvector)   
Jupyter Notebook Version: [ht
tps://github.com/ArtisanLabs/chatgpt-your-files/blob/main/tools/langchain/main.ipynb](https://github.com/ArtisanLabs/cha
tgpt-your-files/blob/main/tools/langchain/main.ipynb)
```
---

     
 
all -  [ Does metadata improve semantic search by default? ](https://www.reddit.com/r/LangChain/comments/174xcgf/does_metadata_improve_semantic_search_by_default/) , 2023-10-14-0909
```
Does merely including metadata (source, keyword, summary) improve the performance of a semantic search?

I am using Pine
cone to store my vectors and I am looking to improve accuracy of the search.

Additionally, what improvements can be mad
e to further enhance the accuracy? I have heard about hybrid search, but could never find a resource that evaluates its 
accuracy.
```
---

     
 
all -  [ Embedding JSON documents for categorical attributes, tags, etc ](https://www.reddit.com/r/LangChain/comments/174sw8f/embedding_json_documents_for_categorical/) , 2023-10-14-0909
```
If I have a JSON document resembling curriculum containing attributes such as:

Title

Description

Difficulty Level

Ta
gs

It's easy to understand how you would embed the textual information such as title and description, but can the categ
orical information be embedded for purposes of semantic search?

Example: 'Intro to X'

(Prioritizes Beginner level cour
ses)

Also, Tags above should be prioritized in search results. Can I instruct the embedding approach to increase weight
ing to categorical and tag based metadata?

&#x200B;

Hopefully this makes sense.
```
---

     
 
all -  [ Image inputs in chatgpt api? ](https://www.reddit.com/r/LangChain/comments/174rn9b/image_inputs_in_chatgpt_api/) , 2023-10-14-0909
```
Hi there, I know there are image inputs possible with chatgpt plus, is there an api endpoint for that too? I looked thro
ugh the documentation and wasn't able to find anything 
```
---

     
 
all -  [ I need to know how local vector databases work ](https://www.reddit.com/r/ChatGPTCoding/comments/174r6xj/i_need_to_know_how_local_vector_databases_work/) , 2023-10-14-0909
```
Im not a strong developer so excuse my beginner questions, that’s why i always try to find the visual tools. I recently 
started using flowise and noticed there is a kind of local vector db component that can replace pinecone and i tried it 
and it works as its replacement without any api keys or anything.

Can i do this in any application I build with langcha
in. Can i do a local vector db that indexes a certain folder so i can chat with its contents. How can i do it or where c
an i start. What is the difference between this, pinecone and chroma?
```
---

     
 
all -  [ Advancements in extracting tabular data from PDFs? ](https://www.reddit.com/r/datascience/comments/174pkt1/advancements_in_extracting_tabular_data_from_pdfs/) , 2023-10-14-0909
```
Hi everyone!

Is there a simple and robust method for extracting highly tabular data from a PDF without resorting to rul
e based regex parsing?  I'm currently using PDFminer, PDFplumber and regex to build templates to extract PDFs based on t
he type of PDF but it's very time-consuming and tedious.  Is there a better way?

I've used Langchain and OpenAI to buil
d 'Chat with your document' apps which works great for uploading a PDF of a whitepaper and asking it to summarize the pa
per, but when it comes to extracting table data - I don't think this solution will work.

&#x200B;

Thank you for your i
nput,

Data Scallion
```
---

     
 
all -  [ LangChain Lab ](https://www.reddit.com/r/LangChain/comments/174osbm/langchain_lab/) , 2023-10-14-0909
```
This experiment will verify different use cases of LLM using LangChain, which include chat, role-playing, and document-b
ased QA.

[https://github.com/coolbeevip/langchain-lab](https://github.com/coolbeevip/langchain-lab)
```
---

     
 
all -  [ Does StackAI have any big advantages over Flowise? ](https://www.reddit.com/r/ChatGPTCoding/comments/174ools/does_stackai_have_any_big_advantages_over_flowise/) , 2023-10-14-0909
```
Hey.

I am slightly overwhelmed by all the options when it comes to LLM applications.

Does stackAI (or other services) 
have any advantages over the free open-source langchain UI 'Flowise' ?

And can someone maybe list the different usecase
s for all the major/relevant applications of these sorts? (Flowise, Botpress, StackAI, VoiceFlow \*insert any other rele
vant thing of this nature.

And perhaps general tips.

Thanks in advance.
```
---

     
 
all -  [ Does StackAI have any big advantages over Flowise? ](https://www.reddit.com/r/Chatbots/comments/174om21/does_stackai_have_any_big_advantages_over_flowise/) , 2023-10-14-0909
```
Hey.

I am slightly overwhelmed by all the options when it comes to LLM applications. 

Does stackAI have any advantages
 over the free open-source langchain UI 'Flowise' ? 

And can someone maybe list the different usecases for all the majo
r/relevant applications of these sorts? (Flowise, Botpress, StackAI, VoiceFlow \*insert any other relevant thing of this
 nature.

And perhaps general tips.

Thanks in advance.
```
---

     
 
all -  [ I run an AI automation agency (AAA). My honest overview and review of this new business model ](https://www.reddit.com/r/Entrepreneur/comments/174o7vd/i_run_an_ai_automation_agency_aaa_my_honest/) , 2023-10-14-0909
```
I started an AI tools directory in February, and then branched off that to start an AI automation agency (AAA) in June. 
So far I've come across a lot of unsustainable 'ideas' to make money with AI, but at the same time a few diamonds in the
 rough that aren't fully tapped into yet- especially the AAA model. Thought I'd share this post to shine light into this
 new business model and share some ways you could potentially start your own agency, or at the very least know who you a
re dealing with and how to pick and choose when you (inevitably) get bombarded with cold emails from them down the line.


# Foreword

Running an AAA does NOT involve using AI tools directly to generate and sell content directly. That ship h
as sailed, and unless you are happy with $5 from Fiverr every month or so, it is not a real business model. Cry me a riv
er but generating generic art with AI and slapping it onto a T-shirt to sell on Etsy won't make you a dime.

At the same
 time, **the AAA model will NOT require you to have a deep theoretical knowledge of AI, or any academic degree**, as we 
are more so dealing with the practical applications of generative AI and how we can implement these into different workf
lows and tech-stacks, rather than building AI models from the ground up. Regardless of all that, common sense and a will
ingness to learn will help (a shit ton), as with anything.

Keep in mind - **this WILL involve work and motivation as we
ll**. The mindset that AI somehow means everything can be done for you on autopilot is not the right way to approach thi
ngs. The common theme of businesses I've seen who have successfully implemented AI into their operations is the willinge
ss to work with AI in a way that augments their existing operations, rather than flat out replace a worker or team. And 
this is exactly the train of thought you need when working with AI as a business model.

However, as the field is relati
vely unsaturated and hype surrounding AI is still fresh for enterprises, right now is the prime time to start something 
new if generative AI interests you at all. With that being said, I'll be going over three of the most successful AI-adja
cent businesses I've seen over this past year, in addition to some tips and resources to point you in the right directio
n.

# so.. WTF is an AI Automation Agency?

The AI automation agency (or as some YouTubers have coined it, the AAA model
) at its core involves creating custom AI solutions for businesses. I have over 1500 AI tools listed in my directory, ho
wever the feedback I've received from some enterprise users is that ready-made SaaS tools are too generic to meet their 
specific needs. Combine this with the fact **virtually no smaller companies have the time or skills required to develop 
custom solutions** right off the bat, and you have yourself real demand. I would say in practice, the AAA model is quite
 similar to Wordpress and even web dev agencies, with the major difference being all solutions you develop will incorpor
ate key aspects of AI AND automation.

Which brings me to my second point- JUST AI IS NOT ENOUGH. Rather than reducing t
he amount of time required to complete certain tasks, I've seen many AI agencies make the mistake of recommending and (t
rying to) sell solutions that more likely than not increase the workload of their clients. For example, if you were to m
ake an internal tool that has AI answer questions based on their knowledge base, but this knowledge base has to be updat
ed manually, this is creating unnecessary work. As such I think one of the key components of building successful AI solu
tions is incorporating the new (Generative AI/LLMs) with the old (programmtic automation- think Zapier, APIs, etc.).

Fi
nally, for this business model to be successful, ideally you should **target a niche in which you have already worked an
d understand pain points and needs**. Not only does this make it much easier to get calls booked with prospects, the sol
utions you build will have much greater value to your clients (meaning you get paid more). A mistake I've seen many AAA 
operators make (and I blame this on the 'Get Rich Quick' YouTubers) is focusing too much on a specific productized servi
ce, rather than really understanding the needs of businesses. The former is much done via a SaaS model, but when going t
he agency route the only thing that makes sense is building custom solutions. This is why **I always take a consultant-f
irst approach**. You can only build once you understand what they actually need and how certain solutions may impact the
ir operations, workflows, and bottom-line.

# Basics of How to Get Started

1. **Pick a niche.** As I mentioned previous
ly, preferably one that you've worked in before. Niches I know of that are actively being bombarded with cold emails inc
lude real estate, e-commerce, auto-dealerships, lawyers, and medical offices. There is a reason for this, but I will tel
l you straight up this business model works well if you target any white-collar service business (internal tools approac
h) or high volume businesses (customer facing tools approach).
2. **Setup your toolbox.** If you wanted to start a press
ure washing business, you would need a pressure-washer. This is no different. For those without programming knowledge, I
've seen two common ways AAA get setup to build- one is having a network of on-call web developers, whether its personal
 contacts or simply going to Upwork or any talent sourcing agency. The second is having an arsenal of no-code tools. I'l
l get to this more in a second, but this works beecause at its core, when we are dealing with the practical applications
 of AI, the code is quite simple, simply put.
3. **Start cold sales.** Unless you have a network already, this is not a 
step you can skip. You've already picked a niche, so all you have to do is find the right message. Keep cold emails shor
t, sweet, but enticing- and it will help a lot if you did step 1 correctly and intimately understand who your audience i
s. I'll be touching base later about how you can leverage AI yourself to help you with outreach and closing.

# The beau
ty of gen AI and the AAA model

You don't need to be a seasoned web developer to make this business model work. The larg
e majority of solutions that SME clients want is best done using an API for an LLM for the actual AI aspect. **The value
 we create with the solutions we build comes with the conceptual framework and design that not only does what they need 
it to but integrates smoothly with their existing tech-stack and workflow.** The actual implementation is quite straight
forward once you understand the high level design and know which tools you are going to use.

To give you a sense, even 
if you plan to build out these apps yourself (say in Python) the large majority of the nitty gritty technical work has a
lready been done for you, especially if you leverage Python libraries and packages that offer high level abstraction for
 LLM-related functions. For instance, calling GPT can be as little as a single line of code. (And there are no-code tool
s where these functions are simply an icon on a GUI). Aside from understanding the capabilities and limitations of these
 tools and frameworks, the only thing that matters is being able to put them in a way that makes sense for what you want
 to build. Which is why outsourcing and no-code tools both work in our case.

# Okay... but how TF am I suppposed to act
ually build out these solutions?

Now the fun part. I highly recommend getting familiar with Langchain and LlamaIndex. B
oth are Python libraires that help a lot with the high-level LLM abstraction I mentioned previously. The two most import
ant aspects include being able to integrate internal data sources/knowledge bases with LLMs, and have LLMs perform auton
omous actions. The two most common methods respectively are RAG and output parsing.

**RAG (retrieval augmented Generati
on)**

If you've ever seen a tool that seemingly 'trains' GPT on your own data, and wonder how it all works- well I have
 an answer from you. At a high level, the user query is first being fed to what's called a vector database to run vector
 search. Vector search basically lets you do semantic search where you are searching data based on meaning. The vector d
atabases then retrieves the most relevant sections of text as it relates to the user query, and this text gets APPENDED 
to your GPT prompt to provide extra context to the AI. Further, with prompt engineering, you can limit GPT to only gener
ate an answer if it can be found within this extra context, greatly limiting the chance of hallucination (this is where 
AI makes random shit up). Aside from vector databases, we can also implement RAG with other data sources and retrieval m
ethods, for example SQL databses (via parsing the outputs of LLM's- more on this later).

**Autonomous Agents via Output
 Parsing**

A common need of clients has been having AI actually perform tasks, rather than simply spitting out text. Fo
r example, with autonomous agents, we can have an e-commerce chatbot do the work of a basic customer service rep (i.e. l
ook into orders, refunds, shipping). At a high level, what's going on is that the response of the LLM is being used prog
rammtically to determine which API to call. Keeping on with the e-commerce example, if I wanted a chatbot to check shipp
ing status, I could have a LLM response within my app (not shown to the user) with a prompt that outputs a random hash o
r string, and programmatically I can determine which API call to make based on this hash/string. And using the same fund
amental concept as with RAG, I can append the the API response to a final prompt that would spit out the answer for the 
user.

**How No Code Tools Can Fit In (With some example solutions you can build)**

With that being said, you don't nec
essarily need to do all of the above by coding yourself, with Python libraries or otherwise. **However, I will say that 
having that high level overview will help IMMENSELY when it comes to using no-code tools to do the actual work for you.*
* Regardless, here are a few common solutions you might build for clients as well as some no-code tools you can use to b
uild them out.

* **Ex. Solution 1: AI Chatbots for SMEs (Small and Medium Enterprises)**
   * This involves creating **
chatbots that handle user queries, lead gen, and so forth with AI**, and will use the principles of RAG at heart. After 
getting the required data from your client (i.e. product catalogues, previous support tickets, FAQ, internal documentati
on), you upload this into your knowledge base and write a prompt that makes sense for your use case. One no-code tool th
at does this well is **MyAskAI**. The beauty of it especially for building external chatbots is the ability to quickly i
ngest entire websites into your knowledge base via a sitemap, and bulk uploading files. Essentially, they've covered the
 entire grunt work required to do this manually. Finally, you can create a inline or chat widget on your client's websit
e with a few lines of HTML, or altneratively integrate it with a Slack/Teams chatbot (if you are going for an internal Q
&A chatbot approach). Other tools you could use include **Botpress and Voiceflow**, however these are less for RAG and m
ore for building out complete chatbot flows that may or may not incorporate LLMs. Both apps are essentially GUIs that el
iminate the pain and tears and trying to implement complex flows manually, and both natively incoporate AI intents and a
 knowledge base feature.
* **Ex. Solution 2: Internal Apps**
   * Similar to the first example, except we go beyond maki
ng just chatbots but tools such as report generation and really **any sort of internal tool or automations that may inco
rporate LLM's**. For instance, you can have a tool that automatically generates replies to inbound emails based on your 
client's knowledge base. Or an automation that does the same thing but for replies to Instagram comments. Another exampl
e could be a tool that generates a description and screeenshot based on a URL (useful for directory sites, made one for 
my own :P). Getting into more advanced implementations of LLMs, we can have tools that can generate entire drafts of rep
orts (think 80+ pages), based not only on data from a knowledge base but also the writing style, format, and author voic
e of previous reports.
   * One good tool to create content generation panels for your clients would be **MindStudio**. 
You can train LLM's via prompt engineering in a structured way with your own data to essentially fine tune them for what
ever text you need it to generate. Furthermore, it has a GUI where you can dictate the entire AI flow. You can also uplo
ad data sources via multiple formats, including PDF, CSV, and Docx.
   * For automations that require interactions betwe
en multiple apps, I recommend the OG **zapier/make.com** if you want a no-code solution. For instance, for the automatic
 email reply generator, I can have a trigger such that when an email is received, a custom AI reply is generated by **My
AskAI**, and finally a draft is created in my email client. Or, for an automation where I can create a social media post
s on multiple platforms based on a RSS feed (news feed), I can implement this directly in Zapier with their native GPT a
ction ([see screenshot](https://imgur.com/9rwpaz4))
   * As for more complex LLM flows that may require multiple layers 
of LLMs, data sources, and APIs working together to generate a single response i.e. a long form 100 page report, I would
 recommend tools such as Stack AI or Flowise (open-source alternative) to build these solutions out. Essentially, you ge
t most of the functions and features of Python packages such as Langchain and LlamaIndex in a GUI. [See screenshot](http
s://imgur.com/o5trxuC) for an example of a flow

# How the hell are you supposed to find clients?

With all that being s
aid, none of this matters if you can't find anyone to sell to. You will have to do cold sales, one way or the other, esp
ecially if you are brand new to the game. And what better way to sell your AI services than with AI itself? If we want t
o integrate AI into the cold outreach process, first we must identify what it's good at doing, and that's obviously writ
ing a bunch of text, in a short amount of time. Similar to the solutions that an AAA can build for its clients, we can t
ake advantage of the same principles in our own sales processes.

**How to do outreach**

Once you've identified your ni
che and their pain points/opportunities for automation, you want to craft a compelling message in which you can send via
 cold email and cold calls to get prospects booked on demos/consultations. I won't get into too much detail in terms of 
exactly how to write emails or calling scripts, as there are millions of resources to help with this, but I will tell yo
u a few key points you want to keep in mind when doing outreach for your AAA.

First, you want to keep in mind that many
 businesses are still hesitant about AI and may not understand what it really is or how it can benefit their operations.
 However, we can take advantage of how mass media has been reporting on AI this past year- at the very least people are 
AWARE that sooner or later they may have to implement AI into their businesses to stay competitive. We want to frame our
 message in a way that introduces generative AI as a technology that can have a direct, tangible, and positive impact on
 their business. Although it may be hard to quantify, I like to include estimates of man-hours saved or costs saved at l
east in my final proposals to prospects. Times are TOUGH right now, and money is expensive, so you need to have a compel
ling reason for businesses to get on board.

Once you've gotten your messaging down, you will want to create a list of p
rospects to contact. Tools you can use to find prospects include **Apollo.io, reply.io, zoominfo (expensive af), and Lin
kedin Sales Navigator**. What specific job titles, etc. to target will depend on your niche but for smaller companies th
is will tend to be the owner. For white collar niches, i.e. law, the professional that will be directly benefiting from 
the tool (i.e. partners) may be better to contact. And for larger organizations you may want to target business improvem
ent and digital transformation leads/directors- these are the people directly in charge of projects like what you may be
 proposing.

Okay- so you have your message, and your list, and now all it comes down to is getting the good word out. I
 won't be going into the details of how to send these out, a quick Google search will give you hundreds of resources for
 cold outreach methods. However, personalization is key and beyond simple dynamic variables you want to make sure you ca
n either personalize your email campaigns directly with AI (SmartWriter.ai is an example of a tool that can do this), or
 at the very least have the ability to import email messages programmatically. Alternatively, ask ChatGPT to make you a 
Python Script that can take in a list of emails, scrape info based on their linkedin URL or website, and all pass this o
nto a GPT prompt that specifies your messaging to generate an email. From there, send away.

**How tf do I close?**

Onc
e you've got some prospects booked in on your meetings, you will need to close deals with them to turn them into clients
.

* Call #1: Consultation
   * Tying back to when I mentioned you want to take a consultant-first appraoch, you will wa
nt to listen closely to their goals and needs and understand their pain points. This would be the first call, and typica
lly I would provide a high level overview of different solutions we could build to tacke these. It really helps to have 
a presentation available, so you can graphically demonstrate key points and key technologies. I like to use **Plus AI** 
for this, it's basically a Google Slides add-on that can generate slide decks for you. I copy and paste my default compa
ny messaging, add some key points for the presentation, and it comes out with pretty decent slides.
* Call #2: Demo
   *
 The second call would involve a demo of one of these solutions, and typically I'll quickly prototype it with boilerplat
e code I already have, otherwise I'll cook something up in a no-code tool. If you have a niche where one type of solutio
n is commonly demanded, it helps to have a general demo set up to be able to handle a larger volume of calls, so you are
n't burning yourself out. I'll also elaborate on how the final product would look like in comparison to the demo.
* Call
 #3 and Beyond:
   * Once the initial consultation and demo is complete, you will want to alleviate any remaining concer
ns from your prospects and work with them to reach a final work proposal. It's crucial you lay out exactly what you will
 be building (in writing) and ensure the prospect understands this. Furthermore, be clear and transparent with timelines
 and communication methods for the project. In terms of pricing, you want to take this from a value-based approach. The 
same solution may be worth a lot more to client A than client B. Furthermore, you can create 'add-ons' such as monthly m
aintenance/upgrade packages, training sessions for employeees, and so forth, separate from the initial setup fee you wou
ld charge.

**How you can incorporate AI into marketing your businesses**

Beyond cold sales, I highly recommend creatin
g a funnel to capture warm leads. For instance, I do this currently with my AI tools directory, which links directly to 
my AI agency and has consistent branding throughout. Warm leads are much more likely to close (and honestly, much nicer 
to deal with).

However, even without an AI-related website, at the very least you will want to create a presence on soc
ial media and the web in general. As with any agency, you will want basic a professional presence. A professional virtua
l address helps, in addition to a Google Business Profile (GBP) and TrustPilot. a GBP (especially for local SEO) and Tru
stpilot page also helps improve the looks of your search results immensely.

For GBP, I recommend using **ProfilePro**, 
which is a chrome extension you can use to automate SEO work for your GBP. Aside from SEO optimzied business description
s based on your business, it can handle Q/A answers, responses, updates, and service descriptions based on local keyword
s.

**Privacy and Legal Concerns of the AAA Model**

Aside from typical concerns for agencies relating to service contra
cts, there are a few issues (especially when using no-code tools) that will need to be addressed to run a successful AAA
. Most of these surround privacy concerns when working with proprietary data. In your terms with your client, you will w
ant to clearly define hosting providers and any third party tools you will be using to build their solution, and a DPA w
ith these third parties listed as subprocessors if necessary. In addition, you will want to implement best practices lik
e redacting private information from data being used for building solutions. In terms of addressing concerns directly fr
om clients, it helps if you host your solutions on their own servers (not possible with AI tools), and address the fact 
only ChatGPT queries in the web app, not OpenAI API calls, will be used to train OpenAI's models (as reported by mainstr
eam media). The key here is to be open and transparent with your clients about ALL the tools you are using, where there 
data will be going, and make sure to get this all in writing.

# have fun, and keep an open mind

Before I finish this p
ost, I just want to reiterate the fact that this is NOT an easy way to make money. Running an AI agency will require hou
rs and hours of dedication and work, and constantly rearranging your schedule to meet prospect and client needs. However
, if you are looking for a new business to run, and have a knack for understanding business operations and are **genuine
ly interested in the pracitcal applications of generative AI**, then I say go for it. The time is ticking before AAA bec
omes the new dropshipping or SMMA, and I've a firm believer that those who set foot first and establish themselves in th
is field will come out top. And remember, while 100 thousand people may read this post, only 2 may actually take initiat
ive and start.
```
---

     
 
MachineLearning -  [ [P] Retrieval augmented generation with OpenSearch and reranking [Video tutorial] ](https://www.reddit.com/r/MachineLearning/comments/16zouad/p_retrieval_augmented_generation_with_opensearch/) , 2023-10-14-0909
```
I created a video tutorial that tries to demonstrate that semantic search (using embeddings) is not always necessary for
 RAG (retrieval augmented generation). It was inspired by the following Cohere blog post: [https://txt.cohere.com/rerank
/](https://txt.cohere.com/rerank/)


I code up a minimal RAG pipeline: `OpenSearch -> Rerank -> Chat completion` (withou
t using Langchain or similar libraries) and then see how it performs on various queries.


Hope some of you find it help
ful. Feel free to share any feedback@

Video link: https://youtu.be/OsE7YcDcPz0
```
---

     
 
MachineLearning -  [ [D] Perplexity.ai Search Feasibility ](https://www.reddit.com/r/MachineLearning/comments/16x63ce/d_perplexityai_search_feasibility/) , 2023-10-14-0909
```
I've been using [Perplexity.ai](https://perplexity.ai/) for a bit now when it hit me that I don't understand how they ca
n sustain their business model with search. Stuff like Bing search and Google search cost around $5 or more per 1000 sea
rches, so how can they even afford to do this kind of search. Do they have their own search index.

Also, I don't know h
ow they pull in the data from these sources so fast? I've played around with some things like this with Langchain with r
etrieval, but the speed of splitting and tokenizing website html is not very fast. Have they already pre-scrapped the we
bsites from the search results and tokenized them for LLM retrieval?
```
---

     
 
MachineLearning -  [ [P] vLLM, Langchain, Embedchain ? ](https://www.reddit.com/r/MachineLearning/comments/16ndyxc/p_vllm_langchain_embedchain/) , 2023-10-14-0909
```
Which libraries do you think would be the most important to learn between these, and to use in my next personal project 
? This will be a conversational chatbot trained on podcast transcripts
```
---

     
 
MachineLearning -  [ [R] Agents: An Open-source Framework for Autonomous Language Agents - AIWaves Inc 2023 ](https://www.reddit.com/r/MachineLearning/comments/16jl4pe/r_agents_an_opensource_framework_for_autonomous/) , 2023-10-14-0909
```
Paper: [https://arxiv.org/abs/2309.07870](https://arxiv.org/abs/2309.07870) 

Github: [https://github.com/aiwaves-cn/age
nts](https://github.com/aiwaves-cn/agents) 

Abstract:

>Recent advances on large language models (LLMs) enable research
ers and developers to build autonomous language agents that can automatically solve various tasks and **interact with en
vironments, humans, and other agents** using natural language interfaces. **We consider language agents as a promising d
irection towards artificial general intelligence** and release Agents, an **open-source library** with the goal of openi
ng up these advances to a wider non-specialist audience. Agents is carefully engineered to support important **features 
including planning, memory,  tool usage, multi-agent communication, and fine-grained symbolic  control.** Agents is **us
er-friendly** as it **enables non-specialists** to build, customize, test, tune, and deploy state-of-the-art **autonomou
s language agents without much coding**. The **library** is also **research-friendly as its modularized design** makes i
t **easily extensible for researchers.** 

https://preview.redd.it/3bdi71r5rgob1.jpg?width=1131&format=pjpg&auto=webp&s=
760942c19be6ecda791414c812a77e72751c526d

https://preview.redd.it/howf64r5rgob1.jpg?width=1656&format=pjpg&auto=webp&s=6
36744fccab7a1c2bafb902bad5dbb647440fff5

&#x200B;
```
---

     
 
MachineLearning -  [ [P] Ways to speed up llama-2 summarization on sagemaker? ](https://www.reddit.com/r/MachineLearning/comments/16iutyp/p_ways_to_speed_up_llama2_summarization_on/) , 2023-10-14-0909
```
I'm currently working on a project to give a quick summary of long articles/conversations.

I'm running llama-2-7b-chat-
hf with 4bit quantization on a g5.2xlarge instance on sagemaker.

The method I'm using is map\_reduce (option 2)from thi
s webpage [https://python.langchain.com/docs/use\_cases/summarization](https://python.langchain.com/docs/use_cases/summa
rization))

Of everything I've tried this is the only one that's been able to do decent summaries in a reasonable amount
 of time. However with really long articles (10,000+ words) it takes \~6 minutes before giving an output.

I tried runni
ng this same thing on a g5.12xlarge instance which has 4 A10G gpus but it hasn't reduced the time by any noticeable amou
nt.

Is there anything else I could be doing to speed this up?

&#x200B;

For reference here is the code I'm running in 
Sagemaker notebook

[https://gist.github.com/phwang4/1ab4d772228b6fff8616c28ac054c229](https://gist.github.com/phwang4/1
ab4d772228b6fff8616c28ac054c229)
```
---

     
 
deeplearning -  [ AutoGen from Microsoft ](https://www.reddit.com/r/deeplearning/comments/170hke6/autogen_from_microsoft/) , 2023-10-14-0909
```
AI agents are AI systems that can exhibit capabilities such as conducting conversations, completing tasks, reasoning, an
d seamlessly interacting with humans. 

As frameworks like LangChain build Agents as a module in their framework, Micros
oft is thinking way ahead. It has built **AutoGen**, a framework to enable seamless MULTI-agent conversation and collabo
ration to accomplish complex tasks by reasoning and working autonomously. 

Here is a video explaining the latest AutoGe
n framework from Microsoft: https://youtu.be/daigxHA2aYw?si=86alxsVZkRpz5Quv

Do you think multi-agents are the future o
f AI? Or will AI emerge in other ways? Let me know your thoughts.
```
---

     
 
deeplearning -  [ TheBloke/Llama-2-7b does not appear to have a file named pytorch_model.bin, tf_model.h5, model.ckpt  ](https://www.reddit.com/r/deeplearning/comments/16ihzn8/theblokellama27b_does_not_appear_to_have_a_file/) , 2023-10-14-0909
```
Hey everyone!

As you can guess from the title, this is the error I get. I only changed the model in AutoModelForCausalL
M, Older version was 

&#x200B;

&#x200B;

`'''`

`model = AutoModelForCausalLM.from_pretrained('meta-llama/Llama-2-7b-c
hat-hf',`

`device_map ='auto',`

`torch_dtype = torch.float16,`

`use_auth_token = True)`

`'''`

&#x200B;

However, si
nce my GPU is NVIDIA GeForce RTX 2080 TI, it answers a simple question in 20 mins. Then I changed it to: 

`model = Auto
ModelForCausalLM.from_pretrained('TheBloke/Llama-2-7b-Chat-GGUF',`

`model_file = 'llama-2-7b-chat.q4_K_M.gguf',`

`devi
ce_map ='auto',`

`torch_dtype = torch.float16,`

`use_auth_token = True)`

&#x200B;

However, this is not working, and 
giving the error. Below is the full code, if it is needed to solve.

&#x200B;

&#x200B;

from langchain.document\_loader
s import JSONLoader

from langchain.text\_splitter import CharacterTextSplitter, TokenTextSplitter, RecursiveCharacterTe
xtSplitter

from langchain.embeddings import HuggingFaceEmbeddings

from langchain.vectorstores import Chroma

from lang
chain import HuggingFacePipeline

from langchain.chains import ConversationalRetrievalChain

from langchain.memory impor
t ConversationBufferMemory

from langchain.embeddings.openai import OpenAIEmbeddings

from langchain.embeddings.huggingf
ace import HuggingFaceEmbeddings

from langchain.chat\_models import ChatOpenAI

import os

import sys

import huggingfa
ce\_hub

from huggingface\_hub import notebook\_login

import torch

import transformers

from transformers import AutoT
okenizer, AutoModelForCausalLM, pipeline

from torch import cuda, bfloat16

import chromadb

from pathlib import Path

f
rom pprint import pprint

import json

from loader import JSONLoader

from [langchain.prompts.chat](https://langchain.pr
ompts.chat) import PromptTemplate, HumanMessagePromptTemplate, SystemMessagePromptTemplate, ChatPromptTemplate

import j
son

from langchain.docstore.document import Document

&#x200B;

def parse\_json(json\_data):

'''Parse JSON data into a
 Python dictionary.'''

return json.loads(json\_data)

&#x200B;

def create\_doc(json\_data):

'''Create a Document obje
ct from JSON data.'''

data = parse\_json(json\_data)

content\_value = ''

&#x200B;

\# Collect values of keys that con
tain 'item' in their name

for key, value in data.items():

if 'item' in key.lower():

content\_value += value + '\\n' 




&#x200B;

return Document(page\_content=content\_value, metadata={'company': data\['company'\]})

&#x200B;

&#x200B;


\##embed\_model\_id = 'BAAI/bge-base-en' ## CHANGE

&#x200B;

embed\_model\_id = 'sentence-transformers/all-mpnet-base-
v2'

&#x200B;

&#x200B;

&#x200B;

device = f'cuda:{cuda.current\_device()}' if cuda.is\_available() else 'cpu' ## NVIDI
A GeForce RTX 2080 TI

&#x200B;

embed\_model = HuggingFaceEmbeddings(

model\_name=embed\_model\_id,

model\_kwargs={'d
evice': device},

encode\_kwargs={'device': device, 'batch\_size': 32}

)

&#x200B;

docs = \[\]

&#x200B;

&#x200B;

fo
r file in os.listdir('lessdata'):

if file.endswith('.json'):

file\_path = './lessdata/'+file

with open(file\_path) as
 file:

json\_data = [file.read](https://file.read)()

document = create\_doc(json\_data)

docs.append(document)

&#x200
B;

&#x200B;

document\_splitter = RecursiveCharacterTextSplitter(separators=\['\\n'\], chunk\_size = 500, chunk\_overla
p = 100)

document\_chunks = document\_splitter.split\_documents(docs)

&#x200B;

&#x200B;

vectordb = Chroma.from\_docu
ments(document\_chunks,embedding=embed\_model, persist\_directory='./database')

&#x200B;

\##vectordb.persist()

'''

v
ectordb = Chroma.from\_documents(document\_chunks,embedding=embed\_model, persist\_directory='./database')

vectordb.per
sist('./database')

&#x200B;

&#x200B;

'''

&#x200B;

&#x200B;

&#x200B;

\### PLEASE DO NOT TOUCH THE VSCODE

&#x200B;


&#x200B;

tokenizer = AutoTokenizer.from\_pretrained('meta-llama/Llama-2-7b-chat-hf', use\_auth\_token = True,)

&#x20
0B;

&#x200B;

model = AutoModelForCausalLM.from\_pretrained('TheBloke/Llama-2-7b-Chat-GGUF',

model\_file = 'llama-2-7b
-chat.q4\_K\_M.gguf',

device\_map ='auto',

torch\_dtype = torch.float16,

use\_auth\_token = True)

&#x200B;

&#x200B;


&#x200B;

&#x200B;

'''

model = AutoModelForCausalLM.from\_pretrained('meta-llama/Llama-2-7b-chat-hf',

device\_map =
'auto',

torch\_dtype = torch.float16,

use\_auth\_token = True)

&#x200B;

&#x200B;

'''

&#x200B;

&#x200B;

&#x200B;


pipe = pipeline('text-generation',

model = model,

tokenizer = tokenizer,

device\_map='auto',

max\_new\_tokens = 512
,

min\_new\_tokens = 1,

top\_k = 5) ##see it 

&#x200B;

\## In vectorstore, take top 5 closest vectors-inputs-context
s, whatever you wanna call.

&#x200B;

llm = HuggingFacePipeline(pipeline=pipe, model\_kwargs= {'temperature':0.7})

&#x
200B;

memory = ConversationBufferMemory(memory\_key='chat\_history', input\_key='question', output\_key='answer', retur
n\_messages=True)

&#x200B;

system\_template = r''' 

Given a context, use your knowledge and answer the question. Be f
lexible, and try everything to answer in the format asked by query.

 \----

{context}

\----

'''

&#x200B;

&#x200B;


user\_template = 'Question:\`\`\`{question}\`\`\`'

&#x200B;

messages = \[

SystemMessagePromptTemplate.from\_template(
system\_template),

HumanMessagePromptTemplate.from\_template(user\_template)

\]

&#x200B;

&#x200B;

qa\_prompt = Chat
PromptTemplate.from\_messages(messages)

&#x200B;

&#x200B;

&#x200B;

jsonExpert = ConversationalRetrievalChain.from\_l
lm(llm = llm, 

retriever=vectordb.as\_retriever(search\_kwargs = {'k': 1}), ## whats it

verbose = True, memory = memor
y, combine\_docs\_chain\_kwargs={'prompt': qa\_prompt},

return\_source\_documents = True

)

&#x200B;

\##retriever ret
urns 1 output object.

&#x200B;

chat\_history = \[\]

query = 'Consider the financials and progress of companies who is
 in the tech business.'

result = jsonExpert({'question': query}, {'chat\_history': chat\_history})

\#result = jsonExpe
rt({'question': query})

&#x200B;

&#x200B;

sources = result\['source\_documents'\]\[0\]

print(result\['answer'\])

pp
rint(sources)

pprint(memory)
```
---

     
