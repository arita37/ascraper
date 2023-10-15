 
all -  [ Too possible to be enjoyable ](https://www.reddit.com/r/Mission_Impossible/comments/177wrh7/too_possible_to_be_enjoyable/) , 2023-10-15-0910
```
Spoilers!
Tech nerds only

The movie premise is too possible to be fun. 

Today a vast amount of computing power is need
ed to train and run AI models. ChatGPT is currently far smarter than any humans or group of humans.  It will be 10x smar
ter in 3 years..



At the same time viruses have been designed as weapons of nations (including successful US deploymen
ts) talking to computer security experts, he best viruses are impossible to detect and eliminate. 

Development environm
ents like langchain give AI models access and do anything on the internet today. 

Once such a federated entity is relea
sed, invades secure computers ( as they said in the movie humans are the weakest link in security) the entity would abso
rb all the nastiest code and tricks. 

I think it is extremely likely that baby versions of the entity has already been 
released. Perhaps by the us, russia, china, or a 15 year old in their basement. 

The only barrier we have now is slow n
etwork communication for federated entities. But 5g and fiber, and starlink are solving that chokepoint. 

This movie is
 like watching a docudrama  about the last days of hummanity as produced by the entity in 10 years after the entity rele
ases covid3.0 on humanity from some government sponsored lab and wipes us from the face of the earth…
```
---

     
 
all -  [ Need help with an Agent with custom tools ](https://www.reddit.com/r/LangChain/comments/177wn7k/need_help_with_an_agent_with_custom_tools/) , 2023-10-15-0910
```
I need some help in implementing async custom tools in my agent. If you have developed such agent and can help me out, p
lease comment below.  I'll share more details in the DM.

Thanks.
```
---

     
 
all -  [ Including extra column with add_documents ](https://www.reddit.com/r/LangChain/comments/177q13x/including_extra_column_with_add_documents/) , 2023-10-15-0910
```
Hi all. I have a vectors table in Supabase to which documents are being added via the add_documents method. But there's 
an extra column that I have in the table that I'd like to add data to when I'm inserting vectors. How can I do this if u
sing add_doccuments?
```
---

     
 
all -  [ [Absolute newb] Help understanding where to focus with tuning and improving response quality ](https://www.reddit.com/r/LangChain/comments/177pmo0/absolute_newb_help_understanding_where_to_focus/) , 2023-10-15-0910
```
Hello! As someone completely new to LLMs and AI (but not new to programming/IT), can I get some advice on where I can fo
cus to improve the results I'm getting? I'm looking to understand the underlying concepts of where my problems might be;
 the problem I have right now is that I've got things 'working,' but the results are really poor in quality, and the lan
dscape is so vast I don't even know what to focus on.

As a first project, I decided to take the Plot Synopsis of variou
s films on IMDb. Each of these is around 10,000 characters in length, so I dumped each in a .txt file, and set up a pg\_
vector vectorstore, and added them all to the same collection.

All queries are with OpenAI, a temperature of 0, and usi
ng gpt-4.

\----------------------------------------------------

I started with The Matrix. I loaded one file, and thro
ugh RetrievalQA was able to query about the contents of the story.

* 'Who is the main character of The Matrix?' --> Neo
. Check.
* 'Summarize the plot of The Matrix in 5 sentences.' --> 'The Matrix is about humans trapped in a simulation...
.......' Check.
* 'What is Neo's day-job?' --> A programmer at a software company. Check.

But then:

* 'Please describe
 Neo's appearance.' --> 'Thick black hair, a sallow appearance, and with a tattoo of a white rabbit on his shoulder.' --
> Huh???

The description of his appearance in the source comes from the same paragraph:

>Thomas Anderson, aka 'Neo' (K
eanu Reeves), a hacker with thick `black hair and a sallow appearance`, is asleep at his monitor. Notices about a manhun
t for a man named Morpheus scroll across his screen as he sleeps. Suddenly Neo's screen goes blank and a series of text 
messages appear: 'Wake up, Neo.' 'The Matrix has you.' 'Follow the White Rabbit.' Then, the text says 'Knock, knock, Neo
...' just as he reads it, a knock comes at the door of his apartment, 101. It's a group of ravers and Neo gives them a c
ontraband disc he has secreted in a copy of 'Simulacra and Simulation.' The lead raver asks him to join them and Neo dem
urs until he sees `the tattoo of a small white rabbit on the shoulder of a seductive girl`  in the group.

The source te
xt is quite clear that the tattoo belongs to someone else, so I can't figure out why the AI is telling me that the tatto
o belongs to Neo. What concepts or areas would I focus on in order to improve this?

\----------------------------------
------------------

Then, I added multiple additional films, like Spider-Man, Indiana Jones, etc. all into the same coll
ection of the pg\_vector vectorstore.

When questioned about a specific film, it does a good job of narrowing in on just
 that part of the collection. 'How does Indiana Jones and the Last Crusade end?' --> great summary about riding off into
 the sunset of finding and losing the grail.

But then any queries that \*cross\* multiple films, it's totally unable to
 handle. Examples:

* The data collection has 5 films in it, but when asked, 'How many films are you aware of?', the mos
t it's ever aware of is 2.
* When asked to make comparisons between films, it will always say it's missing the synopsis 
for one of the two films. i.e. 'Are there any thematic similarities between Spider-Man and Indiana Jones?' --> 'I'm sorr
y, but I'm not aware of any films called Indiana Jones.'

I have some novice suspicions (I've only been working with thi
s for three days...), the major of which is that in order to do a full comparison of two films involves sending all chun
ks of both films, which is too much for a single request, or something along those lines, it's not able to properly narr
ow down the chunks before sending, or something.

Obviously this *can* be done, because those same questions work just f
ine in 'real' ChatGPT. I think this boils down to (probably), 'uh, you've uploaded 10,000 characters about The Matrix, w
hereas the ChatGPT foundational model has probably 100x that amount of information assimilated on The Matrix across 100x
 other sources.' And as a novice, at first glance, I think, 'yeah that makes sense...' But then I think about it more, a
nd actually since that's most likely the case, wouldn't that be even \*more\* chunks/collections for ChatGPT to go throu
gh? Is this where like 'training' comes in? Like if I want a true 'bot' to be able to speak to the details I want, do I 
have to like, give it more data and 'train' it somewhere (somehow)? Right now I've just pointed it at some chunked up ra
w text.

Ahhhh, my brain is tired :) Thanks in advance for the help.
```
---

     
 
all -  [ Methodology for Tracking Client Details in a Natural Language Bot using Langchain and RAG ](https://www.reddit.com/r/LangChain/comments/177oi3y/methodology_for_tracking_client_details_in_a/) , 2023-10-15-0910
```

Hello,

We are building a chatbot using Langchain that aims to gather multiple pieces of information (e.g., name, addre
ss, TV type, malfunction description, etc.) from the client. The bot also needs to respond to any queries the client mig
ht have, using a Retriever-Augmented Generation (RAG) model.

We've considered simply using a system template to keep tr
ack of which details the client has already provided, but this seems inadequate for a fluid and natural conversation.

W
hat methodology would be best for tracking which details the client has already filled in and what questions we need to 
ask next, while still allowing for a natural language conversation?

Any advice or pointers would be highly appreciated.


Thank you!
```
---

     
 
all -  [ AI conference happening in San Francisco: 100% off on the ticket price! ](https://www.reddit.com/r/ArtificialInteligence/comments/177ngy6/ai_conference_happening_in_san_francisco_100_off/) , 2023-10-15-0910
```
I work for this database company SingleStore and we are hosting a Data and AI conference in San Francisco on 17th of Oct
ober, 2023.  
It is an in-person conference with amazing speakers line-up like Harrison Chase, co-founder and CEO of Lan
gChain and many more. We will have hands-on workshops, swags giveaway and much more.  
I don't know if it makes sense to
 share this but I believe it might help some of you near San Francisco to go and meet the industry leaders and network w
ith other data engineering folks.  
Use my discount coupon code 'PAVAN100OFF' to avail 100% off on the ticket price. (th
e original ticket price is $199)

  
[Get your tickets now!](https://singlestore.com/now) using 'PAVAN100OFF' discount c
ode. 
```
---

     
 
all -  [ Data & Analytics conference happening in San Francisco: 100% off on the ticket price! ](https://www.reddit.com/r/dataanalysis/comments/177n2kh/data_analytics_conference_happening_in_san/) , 2023-10-15-0910
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

     
 
all -  [ Chatbot using Langchain to integrate LLM with MongoDB memory and LangSmith to tracing LLM calls. ](https://github.com/btrcm00/chatbot-with-langchain) , 2023-10-15-0910
```

```
---

     
 
all -  [ How can i use extracted keyword before ElasticSearch Querying? ](https://www.reddit.com/r/LangChain/comments/177mcmc/how_can_i_use_extracted_keyword_before/) , 2023-10-15-0910
```
hello.

I am creating a vector search-based chatbot using langchain, openai, and elasticsearch.

&#x200B;

We have imple
mented retrieving the most relevant documents in elasticsearch based on the current user's search.

&#x200B;

Going furt
her, we want to add various conditions to the elasticsearch search query by extracting structured data from the user's q
uery before searching in elasticsearch for higher accuracy.

&#x200B;

For example, the user's search query is 'Which Fo
rd pickup trucks are under $35,000?' In this case, the keywords below should be extracted.

&#x200B;

company: Ford

typ
e: pickup trucks

maximum price: 35000

&#x200B;

After going through the logic of converting this keyword into an Elast
icsearch query (this part will need to be implemented separately), the content below is added to the Elasticsearch searc
h query.

`{ 'term': { 'brand': 'Ford' } },` 

`{ 'term': { 'type': 'pickup' } },` 

`{ 'range': { 'price': { 'lt': 3500
0 } } }`

&#x200B;

I found a library called Kor in LangChain's extract document, and after testing it, I got satisfacto
ry results. However, if you use this library, openAi API will be called twice per user search. (extract 1 time, result g
eneration 1 time)

&#x200B;

Is it best to call openAi api twice using Kor?

&#x200B;

Also, there seems to be a way to 
use SelfQueryRetriever among retrievers.

However, I am currently using CustomRetriever, which inherits BaseRetriever, t
o use ElasticSearch custom queries.

&#x200B;

Can I use SelfQueryRetriever in CustomRetriever?
```
---

     
 
all -  [ Need help with retrieving comprehensive results from multiple documents using GPTVectorStoreIndex ](https://www.reddit.com/r/LangChain/comments/177k795/need_help_with_retrieving_comprehensive_results/) , 2023-10-15-0910
```
I have a collection of scientific documents related to a specific plant, extracted from PDFs and stored in JSON and CSV 
formats. I'm using the following code to load all these documents: 
```
for dir_path in all_dirs:
    dir_reader = Simpl
eDirectoryReader(dir_path, file_extractor={
        '.csv': PandasCSVReader(),
        '.json': JSONReader()
    })
    
docs.extend(dir_reader.load_data())

```

After loading, I create an index and query it:


```
index = GPTVectorStoreInd
ex.from_documents(docs, service_context=service_context)
query_engine = load_index_from_storage(storage_context).as_quer
y_engine(similarity_top_k=4)
response = query_engine.query(input_text)

```
The issue is that the query always returns a
 single response from just one document that best matches my query. However, I know that other documents contain more re
levant information about the plant. How can I modify my approach to retrieve comprehensive results from all relevant doc
uments in my index?
```
---

     
 
all -  [ AI powered by Streamlit ](https://www.reddit.com/r/Streamlit/comments/177jxq2/ai_powered_by_streamlit/) , 2023-10-15-0910
```
I love streamlit + langchain

This experiment will verify different use cases of LLM using LangChain, which include chat
, role-playing, and document-based QA.

https://github.com/coolbeevip/langchain-lab
```
---

     
 
all -  [ OpsTower.ai - AWS CLI AI Assistant ... AMA ](https://www.reddit.com/r/OpenAIDev/comments/177d527/opstowerai_aws_cli_ai_assistant_ama/) , 2023-10-15-0910
```
I've always struggled to remember the AWS CLI syntax and hate using the AWS console. After months of toil on my first AI
 project, I've released [OpsTower.ai, a free DevOps AI Assistant](https://github.com/opstower-ai/llm-opstower). OpsTower
.ai can answer questions about your AWS resources and perform calculations on cloudwatch metrics from the command line.


You can try it in demo mode too (don't need to trust me with your AWS creds 😉). See [https://github.com/opstower-ai/llm
-opstower](https://github.com/opstower-ai/llm-opstower) for full details.

I've also blogged a bit about my experiencing
 building the agent:

1. [Streamlining RAG evaluation](https://dlite.cc/2023/10/04/2023-eval-rag-apps.html)
2. [Beyond d
emoware: how do you evaluate an AI agent?](https://www.opstower.ai/2023-evaluating-ai-agents/) (also covers the agent ar
chitecture using openai function calls)

Learning how to interact w/AWS has been a great starter project to see what's p
ossible. I'd like to teach it to perform tedious DevOps tasks for me.

Also, here are some example questions you try:

 
   llm 'list each ec2 instance id, name, state, last restart, image, and size'
    llm 'What is the average CPU utilizat
ion of my EC2 instances?'
    llm 'breakdown bill by aws service over the past 30 days'

I wrote the agent in Ruby using
 the openai-ruby gem. I originally started with Python and Langchain, but found the abstractions really difficult. I was
 happy with the direction of rolling my own code.

Happy to answer any questions about the sometimes maddening experienc
e of trying to make an agent robust enough to share.
```
---

     
 
all -  [ Routing traffic through Custom Chains. Possible Bug. ](https://www.reddit.com/r/LangChain/comments/177c1ds/routing_traffic_through_custom_chains_possible_bug/) , 2023-10-15-0910
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

     
 
all -  [ Not acknowledging custom function ](https://www.reddit.com/r/LangChain/comments/177bc6j/not_acknowledging_custom_function/) , 2023-10-15-0910
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

     
 
all -  [ How businesses can use GPT with their own data ](https://www.reddit.com/r/Entrepreneur/comments/1777x94/how_businesses_can_use_gpt_with_their_own_data/) , 2023-10-15-0910
```
There’s many business use cases for a custom chat interface like ChatGPT, but using the company’s own internal content a
s the source. Think company policies, documents, project resources, etc.

I’ve been wrapping my head around, and buildin
g, GPT projects for the past 2 years (software dev of 7 years). Always learning, but what I’m sharing is basically the s
tandard approach to create a custom ChatGPT-like application that you can add your own data to.

If you know how to prog
ram, you could explore Open Source libraries like LangChain to handle processing of custom data. It’s a free program tha
t makes the process of interacting with different LLMs easier. Next you’ll want to connect it to a vector database to ma
ke the processed data available for referencing, and finally OpenAI’s API for the LLM generations (or your LLM of choice
).

Regardless of the solution you choose, how all this works from a technical perspective is:

1. You need to break up 
any large text content into smaller pieces. This process is called chunking. You do this to later make each chunk search
able in the vector database.
2. ⁠You’ll want to vectorize each chunk and add this vector into a database. By doing this,
 you can embed (vectorize) natural language to search the vector database for relevant chunks.
3. With the returned chun
ks, you can combine them all (within respects to the context window limit of the LLM of choice), and now your generated 
response will contain the information it needs to give you an accurate output.

Making a secure and privacy-focused solu
tion for businesses is also important. If you use the OpenAI API, data is not used to train their models (source [OpenAI
 Enterprise Privacy](https://openai.com/enterprise-privacy)).

I hope this makes sense. Let me know if there’s any quest
ions on the topic.
```
---

     
 
all -  [ AI SDK with Langchain ](https://www.reddit.com/r/LangChain/comments/1774dek/ai_sdk_with_langchain/) , 2023-10-15-0910
```
Can anybody help me with this ... the streaming cuts off

i am using the vercel SDK

https://preview.redd.it/c39406lwb0u
b1.jpg?width=1130&format=pjpg&auto=webp&s=5d53469e35abab36e72e3c588f35fad83bd5812f

https://preview.redd.it/8tjkgjlwb0ub
1.jpg?width=1210&format=pjpg&auto=webp&s=5ffeabc6ee2a2932dbc1b0f174e32ace2e74b720
```
---

     
 
all -  [ Need advice from experienced CS people regarding what should I do? ](https://www.reddit.com/r/careerguidance/comments/177497v/need_advice_from_experienced_cs_people_regarding/) , 2023-10-15-0910
```
My bachelor's degree is in Industrial Automation and Robotics and I have a masters in Advanced Software Engineering. I'm
 currently working on house projects for my current company. some of them on a proprietary outdated IoT platform (DGLux)
. But I have also worked on Building in-house chatbots using Python, GPT 4, Vectorstores, and Langchain. Also I do have 
some experience in ReactJS, C# andNode-Red as well. But I don't see any clear path around this kind of tech stack. When 
it comes to academics I do have some experience in ML model development as well. Expecting ideas to level up as an engin
eer.
```
---

     
 
all -  [ Need to advice from experienced CS people ](https://www.reddit.com/r/careeradvice/comments/17746bd/need_to_advice_from_experienced_cs_people/) , 2023-10-15-0910
```
My bachelor's degree is in Industrial Automation and Robotics and I have a masters in Advanced Software Engineering. I'm
 currently working on house projects of my current company. some of them on a proprietary outdated IoT platform (DGLux) 
. But I have also worked on Building in house chatbots using Python, GPT 4, Vectorstores, and Langchain. Also I do have 
some experience in ReactJS,C# andNode-Red as well. But I don't see any clear path around this kind of tech stack. When i
t comes to academics I do have some experience in ML model development as well. Expecting a ideas to level up as an engi
neer.
```
---

     
 
all -  [ Chatbot with Langchain Javascript ](https://www.reddit.com/r/LangChain/comments/1772g4u/chatbot_with_langchain_javascript/) , 2023-10-15-0910
```
Chatbot using Langchain with JavaScript and Openai

Frontend: Next.js

What do you think of JavaScript in AI projects?


Repo: [Chatbot](https://github.com/Deluxer/gpt-chatbot-langchain-js)

https://i.redd.it/r8oy6a96vztb1.gif
```
---

     
 
all -  [ Train AI on data and emails? ](https://www.reddit.com/r/ChatGPTPro/comments/1771us3/train_ai_on_data_and_emails/) , 2023-10-15-0910
```
Hi all, I’m wondering if anyone has any thoughts about how to do this: I want to train ChatGPT on a large amount of info
rmation, including websites, pdfs, and outlook emails. I’m trying to start off with something easy that can help me with
 some of my work report writing, but ultimately this is what I really want: read all of my emails (outlook), provide me 
with a summary of them, allow me to have the ai draft replies, have the ai draft options for follow ups (I.e. meetings e
tc.). I know that training an AI model on documents for the first thing is possible, thought tools like Langchain, but i
s the email part of what I am looking for possible? TIA for your thoughts/help
```
---

     
 
all -  [ [News] AI & ML conference in San Francisco [Special discount code for this subreddit] ](https://www.reddit.com/r/MachineLearning/comments/1771m35/news_ai_ml_conference_in_san_francisco_special/) , 2023-10-15-0910
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

     
 
all -  [ Need Some Directions ](https://www.reddit.com/r/LangChain/comments/1770oj4/need_some_directions/) , 2023-10-15-0910
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

     
 
all -  [ Privacy Compliance and Records Retention for LangChain Apps ](https://www.reddit.com/r/LangChain/comments/1770978/privacy_compliance_and_records_retention_for/) , 2023-10-15-0910
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

     
 
all -  [ Vectorizing notes & chat history ](https://www.reddit.com/r/LangChain/comments/17708ki/vectorizing_notes_chat_history/) , 2023-10-15-0910
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

     
 
all -  [ Authoring another course about LLMs. Learn by Doing LLM Projects. ](https://www.reddit.com/r/learnmachinelearning/comments/176zx1m/authoring_another_course_about_llms_learn_by/) , 2023-10-15-0910
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

     
 
all -  [ Limiting options for user prompts? ](https://www.reddit.com/r/OpenAI/comments/176vpss/limiting_options_for_user_prompts/) , 2023-10-15-0910
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

     
 
all -  [ learning langchain ](https://www.reddit.com/r/LangChain/comments/176t09e/learning_langchain/) , 2023-10-15-0910
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

     
 
all -  [ New to this. My boss asked me to use LLM's to disclose information in conversations. Is this feasibl ](https://www.reddit.com/r/LocalLLaMA/comments/176s1ej/new_to_this_my_boss_asked_me_to_use_llms_to/) , 2023-10-15-0910
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

     
 
all -  [ Seeking Orientation on Developing an LLM-Based QA Chatbot ](https://www.reddit.com/r/LocalLLaMA/comments/176om1d/seeking_orientation_on_developing_an_llmbased_qa/) , 2023-10-15-0910
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

     
 
all -  [ May 2024 Grad. 300+ applications since July. 75 rejections. No job yet ](https://www.reddit.com/r/csMajors/comments/176o2jv/may_2024_grad_300_applications_since_july_75/) , 2023-10-15-0910
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

     
 
all -  [ llama2 13b hallucination on a retrival based bot ](https://www.reddit.com/r/LocalLLaMA/comments/176a0gv/llama2_13b_hallucination_on_a_retrival_based_bot/) , 2023-10-15-0910
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

     
 
all -  [ [Langchain] Mistralai LLM avec Langchin ](https://www.reddit.com/r/redditenfrancais/comments/1762y5q/langchain_mistralai_llm_avec_langchin/) , 2023-10-15-0910
```
Langchain soutient-il le modèle AI LLM Mistral?

Traduit et reposté à partir de la publication https://www.reddit.com/16
vwilm
```
---

     
 
all -  [ A Chatbot using Langchain to integrate LLM with MongoDB memory and LangSmith to tracing LLM calls. ](https://www.reddit.com/r/LangChain/comments/1762tkr/a_chatbot_using_langchain_to_integrate_llm_with/) , 2023-10-15-0910
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

     
 
all -  [ Existing relational database to new vector database? ](https://www.reddit.com/r/datascience/comments/1761n34/existing_relational_database_to_new_vector/) , 2023-10-15-0910
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

     
 
all -  [ Positional metadata from PDFloaders? ](https://www.reddit.com/r/LangChain/comments/175qj2b/positional_metadata_from_pdfloaders/) , 2023-10-15-0910
```
The headline kind of says it all. Is it possible to get the positional metadata of the pieces of text you create from th
e text splitter? Would greatly enhance the user experience. Right now I'm just showing the pieces of text when mouse is 
hovering over a link
```
---

     
 
all -  [ [Langchain] Comment déployer le script Langchain Python à la production ](https://www.reddit.com/r/redditenfrancais/comments/175hqpo/langchain_comment_déployer_le_script_langchain/) , 2023-10-15-0910
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

     
 
all -  [ How does the pipe '|' symbol work in Python from this LangChain example? ](https://www.reddit.com/r/LangChain/comments/175edd4/how_does_the_pipe_symbol_work_in_python_from_this/) , 2023-10-15-0910
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

     
 
all -  [ Help with ideas for a project? ](https://www.reddit.com/r/AskRobotics/comments/175c4x6/help_with_ideas_for_a_project/) , 2023-10-15-0910
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

     
 
all -  [ Getting Started with GenAI Stack powered with Docker, LangChain, Neo4j and Ollama ](https://www.reddit.com/r/u_ajeetsraina/comments/175ay08/getting_started_with_genai_stack_powered_with/) , 2023-10-15-0910
```
[https://collabnix.com/getting-started-with-genai-stack-powered-with-docker-langchain-neo4j-and-ollama/](https://collabn
ix.com/getting-started-with-genai-stack-powered-with-docker-langchain-neo4j-and-ollama/) 
```
---

     
 
all -  [ test effectiveness embeddings retrievalQA chatbot ](https://www.reddit.com/r/LangChain/comments/1758n1i/test_effectiveness_embeddings_retrievalqa_chatbot/) , 2023-10-15-0910
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

     
 
MachineLearning -  [ [P] Retrieval augmented generation with OpenSearch and reranking [Video tutorial] ](https://www.reddit.com/r/MachineLearning/comments/16zouad/p_retrieval_augmented_generation_with_opensearch/) , 2023-10-15-0910
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

     
 
MachineLearning -  [ [D] Perplexity.ai Search Feasibility ](https://www.reddit.com/r/MachineLearning/comments/16x63ce/d_perplexityai_search_feasibility/) , 2023-10-15-0910
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

     
 
MachineLearning -  [ [P] vLLM, Langchain, Embedchain ? ](https://www.reddit.com/r/MachineLearning/comments/16ndyxc/p_vllm_langchain_embedchain/) , 2023-10-15-0910
```
Which libraries do you think would be the most important to learn between these, and to use in my next personal project 
? This will be a conversational chatbot trained on podcast transcripts
```
---

     
 
MachineLearning -  [ [R] Agents: An Open-source Framework for Autonomous Language Agents - AIWaves Inc 2023 ](https://www.reddit.com/r/MachineLearning/comments/16jl4pe/r_agents_an_opensource_framework_for_autonomous/) , 2023-10-15-0910
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

     
 
MachineLearning -  [ [P] Ways to speed up llama-2 summarization on sagemaker? ](https://www.reddit.com/r/MachineLearning/comments/16iutyp/p_ways_to_speed_up_llama2_summarization_on/) , 2023-10-15-0910
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

     
 
deeplearning -  [ AutoGen from Microsoft ](https://www.reddit.com/r/deeplearning/comments/170hke6/autogen_from_microsoft/) , 2023-10-15-0910
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

     
 
deeplearning -  [ TheBloke/Llama-2-7b does not appear to have a file named pytorch_model.bin, tf_model.h5, model.ckpt  ](https://www.reddit.com/r/deeplearning/comments/16ihzn8/theblokellama27b_does_not_appear_to_have_a_file/) , 2023-10-15-0910
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

     
