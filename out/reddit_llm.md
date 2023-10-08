 
all -  [ Rag with ChatGPT and ChromaDB for BG3 using Langchain ](https://www.reddit.com/r/kungfudev/comments/172j1hu/rag_with_chatgpt_and_chromadb_for_bg3_using/) , 2023-10-08-0910
```
In recent weeks, I've been delving into GenAI while also enjoying the fantastic game Baldur's Gate 3 (BG3).

&#x200B;

[
https://www.kungfudev.com/blog/2023/10/07/poc-langchain-chromadb](https://www.kungfudev.com/blog/2023/10/07/poc-langchai
n-chromadb)

&#x200B;
```
---

     
 
all -  [ How to Stream LangChainAI Abstractions and Responses using Streamlit Callback Handler and Chat UI ](https://youtu.be/sWVfGIiWmaQ?si=c9YUuZYSXgB7eom1) , 2023-10-08-0910
```

```
---

     
 
all -  [ How to implement filters in MongoDB Atlas Vector Search? (Using langchain.js) ](https://www.reddit.com/r/LangChain/comments/172evas/how_to_implement_filters_in_mongodb_atlas_vector/) , 2023-10-08-0910
```
Hello, 

For context, here's the structure of the documents in my collection: 

    {
         _id: ObjectId(),
        
text: 'Bye bye',
        embedding: Array,
        id: 1,
        site: 'check'
    }

Now I am trying to call the vecto
rStore.asRetriever() method with the goal of only retrieving documents where site = 'check' but I am unable to do so usi
ng the following code:

    const retriever = await vectorStore.asRetriever({
      searchType: 'mmr',
      searchKwarg
s: {
        fetchK: 2,
        lambda: 0.1
      },
      filter: {
          'compound': {
              'must': [
   
               {
                      'text': {
                          'path': 'site',
                          'qu
ery': 'check'
                      }
                  }
              ]
          }
      }
    });

Any idea how to a
chieve the above? A similar question was asked for the Python version and I've already tried the suggested approach but 
to no avail: [https://www.mongodb.com/community/forums/t/filtering-the-results-of-vector-search-with-langchain/240608](h
ttps://www.mongodb.com/community/forums/t/filtering-the-results-of-vector-search-with-langchain/240608)
```
---

     
 
all -  [ Use Case for langchain (or not)? ](https://www.reddit.com/r/LangChain/comments/1722804/use_case_for_langchain_or_not/) , 2023-10-08-0910
```
Hello, sorry for the title could not find anything better.

I'm a 'traditional' software engineer that has been asked fr
om the boss if I can develop the following application:

'we have A LOT (around half millinon) of PDF documents that are
 reports about the performance of a company. Each report is very long (around 100 pages of text) and is terminated by a 
couple of tables that summarize the same information for quick lookup. The reports are 'printed' from word documents, an
d the word document itself come from a dozen of templates (because the template changed with the passing of time) and th
ose coming from the same period differ between only for the few information (for example, the name of the company, the a
ddress, the number of employers etc.). Also most of the information would be easy accessible, if only the tables could b
e easy to read from a pdf. Lastly, the boss would like to chat with the document asking informations about it. But also 
wants to chat wit the dabase as a whole'

Some examples of queries:

'Who is the medic that works for the company X?' (e
ach company has one and only one medic associated with them)

'What are the companies served by a particular medic?'

'W
hat company has the property X?' (the properties are  described in the table with a checkbox

&#x200B;

Here it is the i
ntuition of the usefulness of a LLM chain: the request to 'chat' with the knoledge database

Here are my worries, though
:

* first question is the more easy in my opinion to go right because I could find the relative embedding and make chat
gpt or someone else reply just for that information on that single document. However, a question: should the chunk conta
in both the medic name and the company name (for the context), or just the medic? Because, as I said, The document is 10
0 pages long and the company name is cited ONLY in the first page. Easy to solve, but a question since I'm beginner
* Se
cond question: as I have understood, LLM can reply only to something they has Just seen, I mean that you have to present
 them with an embedding and they can answer only on that. Suppose that a medic is associated to 10000 companies (I doubt
, but it is just an example) as far as I know it cannot reply since most LLM can take up to 4k token as an input. Am I r
ight?
* 3rd question, as far as I have seen through experimentation, LLM have trouble reading on tables, whatever the fo
rmatting is. Am i right?

&#x200B;

All this concerns make me wonder if this problem should be approached from an algori
thmic perspective and a traditional (sql o nosql) database. Is that correct, or there is a margin of hybridations? May b
e should I try looking towards chain agents (just found them, might be the case)?I'm not looking about code, just some h
ints on what to do or not to do

thanks to everyone

&#x200B;
```
---

     
 
all -  [ Summary/QA from 5-10 page text without vectorizing it ](https://www.reddit.com/r/LangChain/comments/171zzst/summaryqa_from_510_page_text_without_vectorizing/) , 2023-10-08-0910
```
Hey,

I'm wokring in a market intelligence function and I have a weekly need of providing 5-10 bullet point summaries of
 competitors news which they publish.

Idelly, I would be able to load a PDF to langchain and and the results which the 
LLM  gives would be following structure which I can define.

Issue in vectorstore approach is that it only selects x chu
nks which will be assessed/summarized, but I would like to take everything in scope (although it's costly but so is my t
ime 😄). For example in financial reports the relevant numbers might be very scattered within the document.

Any suggesti
on whether tejre would be better options than:
1) extract pdf to test eg pypdf
2) input text string as prompt input to t
he LLM and use a conversationalchain

Thanks a alot for your help!
```
---

     
 
all -  [ AI Conference in SF with CEO of LangChain ](https://www.reddit.com/r/conferences/comments/171vv1p/ai_conference_in_sf_with_ceo_of_langchain/) , 2023-10-08-0910
```
 

[**SingleStore**](https://www.linkedin.com/feed/#) is hosting, ‘SingleStore Now: The Real-Time AI Conference’ on Oct 
17th at the Chase Center in San Francisco!

Highlights include:

\- Keynotes from industry stalwarts like [**Harrison Ch
ase**](https://www.linkedin.com/feed/#), CEO of [**LangChain**](https://www.linkedin.com/feed/#).

\- Opportunities for 
invaluable networking within the industry.

\- Engaging, hands-on sessions covering a gamut of topics from LLMs to vecto
r databases.

\- A chance to participate in an AI hackathon (and win prizes!).

\- Live demonstrations and tutorials on 
building applications with ChatGPT, semantic search, image recognition, and more!

Although the regular ticket price is 
$199, I'm thrilled to share a special code with you. Register here: https://singlestorenowtherealtimeaicon.splashthat.co
m/ using “Vinija-25” and attend the event for only $25!

Whether you're just beginning your journey into AI and semantic
 search, or keen on mastering the craft of creating comprehensive generative AI applications, this conference promises i
mmense value!
```
---

     
 
all -  [ repo for digestion and logical chunking of pdfs? ](https://www.reddit.com/r/LangChain/comments/171k6gm/repo_for_digestion_and_logical_chunking_of_pdfs/) , 2023-10-08-0910
```
are there repos or methods out there for effectively digesting, analyzing the layout, charts graphs etc that may be with
in a pdf, and creating a chunking schema for upload to a vector db, that would work on most layouts found in pdfs?
```
---

     
 
all -  [ Telling the LLM where to look before retrieval ](https://www.reddit.com/r/LangChain/comments/171idqq/telling_the_llm_where_to_look_before_retrieval/) , 2023-10-08-0910
```
I built a custom chatbot that can answer questions based on content from either youtube or a specific website.   


Both
 youtube and website content are stored in my local vectorstore via FAISS.

  
When a user asks a chatbot a question tha
t can be answered by the website, we want it to look there instead of youtube. And vice-versa. Right now, it's retrievin
g mostly from youtube because queries generally semantically match youtube content, even though a simple response can be
 found from the website.  


I was thinking I need to build an LLM-based classifier system or a Langchain function. This
 first step would have the LLM determine where to look. I haven't played around with functions - can a function be an LL
M call?

&#x200B;

Any other tips or pointers would be appreciated! Happy to report back on what we try and how it perfo
rms.

&#x200B;
```
---

     
 
all -  [ 'How to finetune LLM Using RLHF ?' - Postive Review Chatbot 404 - YouTube ](https://www.reddit.com/r/LangChain/comments/171ecew/how_to_finetune_llm_using_rlhf_postive_review/) , 2023-10-08-0910
```
 ['How to finetune LLM Using RLHF ?' - Postive Review Chatbot 404 - YouTube](https://www.youtube.com/watch?v=B5dhaZPJQx0
) 
```
---

     
 
all -  [ Open-source alternative to Chatbase, SiteGPT and Dante AI built with Langchain ](https://www.reddit.com/r/LangChain/comments/171dx1h/opensource_alternative_to_chatbase_sitegpt_and/) , 2023-10-08-0910
```
Chatbase, SiteGPT and Dante AI allow you to chat with your data. I have made an open-source solution so that you can run
 something like that yourselves

Here is the link to it :- [https://github.com/Anil-matcha/Chatbase](https://github.com/
Anil-matcha/Chatbase)
```
---

     
 
all -  [ How to improve the quality of RAG answers? ](https://www.reddit.com/r/LangChain/comments/171bevs/how_to_improve_the_quality_of_rag_answers/) , 2023-10-08-0910
```
All those 'Chat with PDF' apps out there show particularly good results compared to standard Langchain QnA based on RAG.
 I wonder how do they improve the quality of answers. 

This becomes even more evident when you deal with questions like
 'summarize this doc'. I don't see how one could use RAG to answer questions related to summarization. I have been doing
 some research but haven't found any effective solution yet.
```
---

     
 
all -  [ Task Specific Alternative to GPT-4 ](https://www.reddit.com/r/LocalLLaMA/comments/1719t4m/task_specific_alternative_to_gpt4/) , 2023-10-08-0910
```
I'm creating different agents to complete various tasks, and one of which is to crawl through a website to find specific
 information. It was easiest to prove out the concept with GPT-4 since a lot of libraries (like Langchain) already creat
e zero shot agent implementations for that model. Now that I have proved out the concept, I want to find a model I can d
eploy locally. Right now, I can test with a 3090 locally, but I will soon have some A100s at my disposal. Does anyone ha
ve recommendations for models that would do well with this task? I know I will have to do some prompt engineering to tes
t this out more thoroughly for anything else. It would be great if there was a very task-specific leaderboard of models
```
---

     
 
all -  [ Size scaling for vector databases (Chroma DB specifically) ](https://www.reddit.com/r/LangChain/comments/170qmjp/size_scaling_for_vector_databases_chroma_db/) , 2023-10-08-0910
```
Has anyone run across or conducted their own study of how the size of the files and datastorage increase with the number
 of document chunks that are loaded into the database? Is it quadratic, sub-linear, etc?

Also how sensitive is the size
 the choice of embeddings? If you use the \`text-embedding-ada-002\` with 1500 dimensions compared with another model wi
th only 300, will the database size go up linearly (approximately 5x larger)?

We've started exploring this idea, but I 
wanted to if anyone has dug into it already.
```
---

     
 
all -  [ AI assistant integration beyond the native integration? ](https://www.reddit.com/r/todoist/comments/170ptp5/ai_assistant_integration_beyond_the_native/) , 2023-10-08-0910
```
Hi all - 

Long time Todoist user here, new to the subreddit.. 

I have tried the 'AI Assistant' that Todoist put out an
d this is useful in some ways, but what I'm looking for is to have AI assist me with trying to prioritize against my goa
ls, remind me of what is important, be able to add new tasks based on our conversations, etc. 

I have some experience d
eveloping Langchain based solutions using AI and I'm tempted to do this myself, but before I go down that road, I wanted
 to see if there were existing solutions. 

Does this exist already? Has anyone built their own version of this?
```
---

     
 
all -  [ Finetuned models for function calling? ](https://www.reddit.com/r/LocalLLaMA/comments/170pej3/finetuned_models_for_function_calling/) , 2023-10-08-0910
```
Hello. Are there finetuned LLaMa2 models that can reliably work for function calling yet? (Setting up agents in Langchai
n and such). Previous discussion is around 2 months old so I wonder if there has been some advances on this.

I have bee
n trying to build a chatbot that can search on the internet and can be locally hosted but the models I've tried are terr
ible at this.
```
---

     
 
all -  [ Give our customers an LLM to talk to about their data ](https://www.reddit.com/r/LocalLLaMA/comments/170npuw/give_our_customers_an_llm_to_talk_to_about_their/) , 2023-10-08-0910
```
Hello guys, we are a small web design company, and we are testing langchain and llama2 llm locally. We want to be able t
o create a chatbot for our customers so the llm can check out their hosting stats and our customers can ask questions su
ch as 'how much more space do I need if I want to add a new email account, create a database, when will I need to upgrad
e my account,  etc,,  So our main question is, where can we read up on how many concurrent users we can have if we use l
angchain and how can we setup ques or buffering so when the GPU is bogged down, it will still process the queries from o
ur customers but keep them in a waiting list until their request is up. Is this a crazy project or doable? Thanks!
```
---

     
 
all -  [ RecursiveCharacterTextSplitter: create_documents vs split_documents ](https://www.reddit.com/r/LangChain/comments/170mfkc/recursivecharactertextsplitter_create_documents/) , 2023-10-08-0910
```
Greetings to the community,

My first post here. Apologies in advance for any possible violation of community's establis
hed principles and practices 🙏

In the RecursiveCharacterTextSplitter class, I'm not clear about the difference between 
the two methods: **create\_documents** vs **split\_documents**.

Suppose I've a given text, in any form, whether split/u
n-split in NLP sentences. It could be from multiple documents (PDF/text).

Which method I should choose to split the tex
t, and why?

For example, in Section 3 of *Ingest chat embedding* given here [https://python.langchain.com/docs/use\_cas
es/question\_answering/integrations/semantic-search-over-chat](https://python.langchain.com/docs/use_cases/question_answ
ering/integrations/semantic-search-over-chat), first split\_text is used (with CharacterTextSplitter), and then create\_
documents (with RecursiveCharacterTextSplitter). Why not directly use **split\_documents** on the initial text?
```
---

     
 
all -  [ My strategy for picking a vector database: a side-by-side comparison ](https://www.reddit.com/r/LangChain/comments/170jigz/my_strategy_for_picking_a_vector_database_a/) , 2023-10-08-0910
```
I made this table to compare vector databases in order to help me choose the best one for a new project. I spent quite a
 few hours on it, so I wanted to share it here too in hopes it might help others as well. My main criteria when choosing
 vector DB were the speed, scalability, developer experinece, community and price.

https://preview.redd.it/dw181oiz8esb
1.png?width=1870&format=png&auto=webp&s=cf26639b12a1b6e5662198f11fe31f71c9ba8123

You'll find all of the comparison para
meters in the article and more details here: [https://benchmark.vectorview.ai/vectordbs.html](https://benchmark.vectorvi
ew.ai/vectordbs.html)  


Edit: For transparency, I am the co-fouder of Vectorview.ai which is an analytics tool for sem
antic search that let's developers understand how their embedded documents are used. 
```
---

     
 
all -  [ Interested in using LangChain and llama.cpp, to create industry specific search / chat bot, for data ](https://www.reddit.com/r/LangChain/comments/170ij5e/interested_in_using_langchain_and_llamacpp_to/) , 2023-10-08-0910
```
Hi,

I'm a software / solution architect, in eCommerce. I'm a competent developer and system architect, but new to LLMs,
 or even training a chatbot. I've built a very basic chatbot on node/react, using the OpenAI API. However, from this I l
earned two things, because of the size and complexity of the data I want to train the LLM on, I will need something more
 structured like LangChain. And, because of the nature of the tool I'd like to build, I'm not sure the OpenAI fee struct
ure will be financially viable.

This utility / search tool will be useful to the service departments of auto dealership
s, and just general service shops.

I expect they will value its utility at somewhere between $499, and $999 per year. T
hey won't want to pay an extreme amount for this, but they will pay for it. And there are 1000s of shops for whom it wou
ld save time for their employees, and be of use.

There might be 100 searches per day on it, from each paid user, and wi
th OpenAIs model, based on really limited experience, and sort of a gut feeling from my testing.... I think that would m
ean low, or negative margins, if relying on OpenAI / ChatGPT.

My expectation, and hope, is instead to build an applicat
ion that runs entirely locally, using llama.cpp, and run this utility on a single server.

I am looking for someone with
 technical understanding of using llama.cpp with LangChain, who has trained a LLM against a large and complex database, 
who might be interested in working on this project with me as a consultant.

&#x200B;

Thanks
```
---

     
 
all -  [ I'm wondering if it's possible to patent the LangChain Process that I developed. ](https://www.reddit.com/r/legaladvice/comments/170i0ph/im_wondering_if_its_possible_to_patent_the/) , 2023-10-08-0910
```
Our team created a proprietary approach utilizing LLMs and LangChain derivative. Is it patentable?
```
---

     
 
all -  [ AutoGen from Microsoft ](https://www.reddit.com/r/learnmachinelearning/comments/170hl7w/autogen_from_microsoft/) , 2023-10-08-0910
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

     
 
all -  [ Need help here (Link in the description) ](https://www.reddit.com/r/LangChain/comments/170gj4f/need_help_here_link_in_the_description/) , 2023-10-08-0910
```
can you assist me on my query. I have explained my issue here with my small code:

https://github.com/langchain-ai/langc
hain/discussions/11429
```
---

     
 
all -  [ Should I convert my html documents to text before storing them to save tokens? ](https://www.reddit.com/r/LangChain/comments/170etrb/should_i_convert_my_html_documents_to_text_before/) , 2023-10-08-0910
```
I've been using vector stores and I noticed so many special characters that get parsed with WebBaseLoader that I was won
dering if I should first convert them all to text files?  
There will be few updates on the sites for what I am using it
 for, so I that wouldn't be an issue.  


Or is there something going on under the hood that would clean the documents c
reated from html stores before passing it to the language model?

&#x200B;

many thanks in advance!
```
---

     
 
all -  [ What’s shaking? ](https://i.redd.it/jcud801uscsb1.jpg) , 2023-10-08-0910
```
Oh who knows
```
---

     
 
all -  [ LangChain - Your Key to Unlocking Multilingual Mastery! 🗝️🌍 ](https://www.reddit.com/r/u_Techup24/comments/170cj62/langchain_your_key_to_unlocking_multilingual/) , 2023-10-08-0910
```
Hey Language Enthusiasts! Ready for a Language Revolution? Meet LangChain! 🚀

🌐 **The Future of Language Learning**

Lan
gChain fuses blockchain, AI, and a vibrant community for an immersive language learning experience.

🔗 **Blockchain-Powe
red Trust**

Your progress is securely stored on the blockchain, making your achievements tamper-proof and credible.

&#
x200B;

🤖 **AI Tailored for You**

Say goodbye to generic lessons! LangChain's AI creates personalized courses to suit y
our learning style and pace.

&#x200B;

🏆 **Earn While You Learn**

As you advance, earn LangTokens - our cryptocurrency
. Use them for premium content, lessons, or real-world rewards. Showcase your achievements!

&#x200B;

💡 **Shape the Fut
ure of Language Learning**

Join LangChain today and redefine how the world learns languages!

&#x200B;

Ready to embark
 on this journey? Share your thoughts below! 💬🌟 

\#LangChain #LanguageLearning #UnlockTheWorld
```
---

     
 
all -  [ LangChain with local LLM on tabular data ](https://www.reddit.com/r/LangChain/comments/170cic8/langchain_with_local_llm_on_tabular_data/) , 2023-10-08-0910
```
Any one able to crack how to use langchain with open source llm (not open ai) to query database using agents
```
---

     
 
all -  [ I'm working with Confluence, and I need to perform question answering with attachments available in  ](https://www.reddit.com/r/LangChain/comments/170c8om/im_working_with_confluence_and_i_need_to_perform/) , 2023-10-08-0910
```
**Details:**

\- I have set up a Confluence integration and a Chroma database.

\- I also have a question-answering mode
l that can retrieve information from Confluence documents.

\- My goal is to be able to ask questions related to the con
tent of Confluence documents, even when they have attachments like images, spread sheet and table .

**Can anyone provid
e guidance on how to do this effectively? Are there any best practices or specific tools I should be using for this task
? Any help would be greatly appreciated!**

below is my Code:

  
def chat\_confluence\_response(new\_project\_qa, query
):   
 check = query.lower()  
 query = 'Search the entire context and provide formal and accurate answer for this query
 - {}. Explain the relevant information with important points, if necessary.'.format(check)  
 response = new\_project\_
qa.run(query)  
 return response  
def vector\_db\_confluence\_docs(config: dict,persist\_directory):  
 confluence\_url
 = config.get('confluence\_url', None)  
 username = config.get('username', None)  
 api\_key = config.get('api\_key', N
one)  
 space\_key = config.get('space\_key', None)  
 \# Initialize embeddings  
 embedding = OpenAIEmbeddings()  
 \# 
Extract the documents  
 loader = ConfluenceLoader(  
 url=confluence\_url,  
 username=username,  
 api\_key=api\_key  

)  
 documents = loader.load(  
 space\_key=space\_key,  
 limit=100  
)  
 \# Split the texts  
 text\_splitter = Char
acterTextSplitter(chunk\_size=100, chunk\_overlap=0)  
 texts = text\_splitter.split\_documents(documents)  
 text\_spli
tter = TokenTextSplitter(chunk\_size=1000, chunk\_overlap=10, encoding\_name='cl100k\_base')  
 texts = text\_splitter.s
plit\_documents(texts)  
 if texts == \[\]:  
 file\_crawl\_status = False  
 file\_index\_status = False  
 else:  
Chr
oma.from\_documents(documents=texts, embedding=embedding, persist\_directory=persist\_directory)  
 file\_crawl\_status 
= True  
 file\_index\_status = True  
 return file\_crawl\_status, file\_index\_status  


def retreival\_qa\_chain(con
fluence\_chroma\_db\_path):  
 embedding = OpenAIEmbeddings()  
 vectordb = Chroma(persist\_directory=confluence\_chroma
\_db\_path, embedding\_function=embedding)  
 llm = ChatOpenAI(temperature=0.1)  
 retriever = vectordb.as\_retriever(se
arch\_kwargs={'k': 4})  
 qa = RetrievalQA.from\_chain\_type(llm=llm, chain\_type='stuff', retriever=retriever)  
 retur
n qa
```
---

     
 
all -  [ UnstructuredDetectronModel Initialization TypeError ](https://www.reddit.com/r/LangChain/comments/170b61a/unstructureddetectronmodel_initialization/) , 2023-10-08-0910
```
I am trying to use a pre-trained model from the [Model Zoo](https://layout-parser.readthedocs.io/en/latest/notes/modelzo
o.html) with `UnstructuredDetectronModel` in Python and encountering a `TypeError` during the initialization process. I 
was following [this guide](https://unstructured-io.github.io/unstructured/best_practices/models.html) where it mentions 
that `UnstructuredDetectronModel` is a light wrapper around layoutparser.models.Detectron2LayoutModel and can utilize va
rious pre-trained models from the model zoo. Below is the code snippet that is causing the error:

```python
from unstru
ctured_inference.models.detectron2 import UnstructuredDetectronModel
import layoutparser as lp

model = UnstructuredDete
ctronModel(
    config_path='lp://PubLayNet/mask_rcnn_X_101_32x8d_FPN_3x/config',
    label_map={0: 'Text', 1: 'Title', 
2: 'List', 3: 'Table', 4: 'Figure'},
    extra_config=['MODEL.ROI_HEADS.SCORE_THRESH_TEST', 0.8],
)
```
The error messag
e I receive is: TypeError: __init__() got an unexpected keyword argument 'config_path'

Any help would be greatly apprec
iated!
```
---

     
 
all -  [ Approaches to increase speed of LangChain agent? Takes ~1minute to respond ](https://www.reddit.com/r/LangChain/comments/1709u74/approaches_to_increase_speed_of_langchain_agent/) , 2023-10-08-0910
```
I put together a LangChain agent which uses two tools- a retriever and a Pandas tool, and uses the ReAct framework to do
 the overall thinking. Although it theoretically works as it's expected, it takes too long of times to produce answers. 


What I observe is that it takes too long if time in the 'thinking' stage. Has anyone else experienced this?

More spec
ifically, I'm using the 'conversational-react-description' type agent.

Let me know what are the general steps that can 
be taken to optimize the time it takes for the agent to produce final answer
```
---

     
 
all -  [ Looking for some guidance on a small project ](https://www.reddit.com/r/ChatGPTCoding/comments/17097sj/looking_for_some_guidance_on_a_small_project/) , 2023-10-08-0910
```
I looking to do a little project which can help me at work. I'm looking at using python with help from chatgpt to accomp
lish this. Just want to make sure what i'm trying to do looks sound and for any suggestions on how to accomplish this. F
rom what i've read so far it looks like langchain to break down pdf files into embeddings may be the way to go?

For eve
ry PDF file in a input folder:  
1. Break it down into embeddings and store it in a database temporarily(they are too la
rge otherwise)  
2. Using openai api run two custom prompts against that specific pdfs data in the database  
3. Put the
 output of those custom prompts each into a separate pdf file into a output folder  
4. Cleanup the database(dont need t
o keep any of the data) and ready it for the next pdf document in the input folder
```
---

     
 
all -  [ Follow-up questions to previous conversations ](https://www.reddit.com/r/LangChain/comments/1708wxo/followup_questions_to_previous_conversations/) , 2023-10-08-0910
```
I am having issue in accuracy in execution of this experience(this is one possible user experience flow): 

1. User asks
 a question to be searched in a vector DB- example 'tell me about Taj Mahal?' 

2. Receive response 

3. User asks follo
w up question - 'remove details about Shah Jahan family in above response'

4. Receive a total different response rather
 than response from previous conversations minus the removed part

5. User asks - add a bit more detail about building m
aterial in last answer. 

6. Again a different response rather than adding content.

I am using ConversationalRetrievalC
hain.from_llm() and have tried ConversationBufferMemory, chat_history and few other approaches but none of them appear t
o work accurately with consistency.

Anyone had any thoughts/ references for something like this?
```
---

     
 
all -  [ Large text summary options? ](https://www.reddit.com/r/LangChain/comments/1706g3h/large_text_summary_options/) , 2023-10-08-0910
```
Any thoughts on how I can handle large text summary? The context is reading through hundreds of email chains and summari
zing them.

I’ve been playing around with large text summary models on hugging face but the hallucinations are insane, l
ike 50% of the summary is made up…

Looking at between 10,000-50,000 characters…
```
---

     
 
all -  [ Text splitting for word document ](https://www.reddit.com/r/LangChain/comments/1705onu/text_splitting_for_word_document/) , 2023-10-08-0910
```
I am working on RAG using vector database. I'm in initial POC period and am using Chroma database and soon might migrate
 to Qdrant or weaviate.

That's not the topic, my main point is around chunking
I am of the opinion that chunking (text 
splitting) is extremely important as the semantic of the embedding will be determined by it. While it is my understandin
g that embedding is bit of a black box, my current sense is saying that I need to contextualize my chunk than doing a bl
ind split of 256 or 512 or 1024.

I have a bunch of word documents which I'm loading and have headings, sub headings and
 paragraphs. Sometimes the paragraphs can be a table in the word document too.

So 2 questions really:
1) Is splitting a
s important as I feel it is? 
2) What is a good document loader for word which can determine and preserve the tags of he
adings, subheadings, paragraphs and tables in a good structure so I can chunk it as desired.

Thank you Redditors!!
```
---

     
 
all -  [ looking to figure out how to get an agent to read text classifiers and then apply to descriptions ](https://www.reddit.com/r/LangChain/comments/17021gf/looking_to_figure_out_how_to_get_an_agent_to_read/) , 2023-10-08-0910
```
I'm trying to get LangChain to read two Excel files - one with classifier info and the other with company descriptions. 
The goal is to classify the companies based on the info in the first file. Got the files loaded up, but stumbling a bit 
with setting up the agent and executor in LangChain to process this data and get the results out. Anyone here tackled so
mething similar or got some tips? Thanks!
```
---

     
 
all -  [ Handle sessions with separate ID's without res-instantiating RedisChatMessageHistory ](https://www.reddit.com/r/LangChain/comments/16zyemd/handle_sessions_with_separate_ids_without/) , 2023-10-08-0910
```
I have an LangChain/Flask application where each request carries a session ID, and therefore I can separate their messag
e histories as follows (pseudo-code):  


    @app.post('chat')
    def chat(str):
        redis = RedisChatMessageHisto
ry(
            # Use the incoming session_id
            session_id=app.request.session_id
        )
    
        conve
rsation = ConversationChain(
            llm=llm, 
            memory=ConversationBufferMemory(
                # Use th
e Redis adaptor, which only has access to the given app.request.session_id history
                chat_memory=redis
   
         )
        )
    
        conversation({'input': app.request.body'}

The problem with this approach is that I ha
ve to instantiate the Chain and its components at every request, introducing some overhead.

Is there a (thread-safe) wa
y to change  \`RedisChatMessageHistory\` session\_id without instantiating the whole thing every time?
```
---

     
 
all -  [ Easy RAG Implementation for GenAI using Mongo: Langchain alternative ](https://www.reddit.com/r/mongodb/comments/16zx1gc/easy_rag_implementation_for_genai_using_mongo/) , 2023-10-08-0910
```
Hi all, we worked really hard to develop our open source library on Github for easy, straightforward RAG implementation 
for GenAI using Mongo (and Milvus, FAISS or PineCone for vector DB). We built in a lot of features for easy document ing
estion that is scalable as well as native parsing for PDFs and Office documents for a very fast ingestion. Please check 
out our LLMWare library and we would be extra grateful if you can leave a star!

[https://github.com/llmware-ai/llmware]
(https://github.com/llmware-ai/llmware)
```
---

     
 
all -  [ New Github Library for RAG: Langchain Alternative ](https://www.reddit.com/r/ArtificialNtelligence/comments/16zwrsa/new_github_library_for_rag_langchain_alternative/) , 2023-10-08-0910
```
HI all, we worked really hard and created an open source library that is an integrated RAG system for GenAI with a lot o
f great features on Github for LLMWare (straightforward, easy to use). It would be great if you can check it out (would 
be extra grateful if you can leave a star). Thank you!

[https://github.com/llmware-ai/llmware](https://github.com/llmwa
re-ai/llmware)
```
---

     
 
all -  [ Interesting hallucinations with a RAG-type chatbot ](https://www.reddit.com/r/LangChain/comments/16zqz0p/interesting_hallucinations_with_a_ragtype_chatbot/) , 2023-10-08-0910
```
I'm building a RAG chatbot for IT support. It ingests KB articles (chunked), retrieves them based on the query and then 
runs the 'classic' prompt that instructs the LLM to answer only using the source material from the retriever.  So far so
 good and the results were good in a pre-testing phase.  
Then I started testing with real-world questions and I stumble
d into an interesting case:  
\- the user types a message about not being to get into Microsoft Project.  
\- the retrie
ver retrieves an article about troubleshooting not being able to use Outlook.   
\- the LLM uses the chunk, copies the t
ext almost as is and substitutes the text 'Outlook' with 'Project' going as far as changing the name of the outlook exec
utable into the supposed project executable (winproj.exe) in a procedure. Of course the answer is wrong but I cannot get
 the LLM to simply say 'I do not know'.  
The LLM used is GPT-3.5 16k, latest version from Azure Open AI.  
I talked wit
h other people developing RAG chatbots and nobody saw something like that (but they are using other non-GPT models like 
Claude and llama).  


Any ideas? Did u see something like that happen? Did you find a solution?
```
---

     
 
all -  [ Memory is not working with ConversationalRetrievalQAChain. ](https://www.reddit.com/r/LangChain/comments/16zpv8l/memory_is_not_working_with/) , 2023-10-08-0910
```
Hey, so I am working with next JS 13, langchain and supabase. I have used  

ConversationalRetrievalQAChain like this:


     const qachain =  ConversationalRetrievalQAChain.fromLLM(
        model, 
        vectorstore.asRetriever(),
       
 { memory: memory,
          questionGeneratorChainOptions:{
          template: CONDENSE_QUESTION_TEMPLATE, 
          
llm:nonStreamingModel
        },
        qaChainOptions: {
          type: 'stuff', 
          prompt: PromptTemplate.fr
omTemplate(ANSWER_TEMPLATE)
        },
      });

I tried adding  ConversationSummaryMemory as memory but it isn't worki
ng. 

    const memory = new ConversationSummaryMemory({
          llm: model, 
          memoryKey: 'chat_history', 
  
        inputKey: 'question',   
          returnMessages: true,
        });

I tried printing what is being stored in t
he memory like this:  


    console.log('This is memory: ',memory.buffer);

But nothing is being print.

Here is how I 
call the chain:

    const callbacks = CallbackManager.fromHandlers(handlers);
    const latest = messages[messages.leng
th - 1].content;
    qachain.call({ 
          question: latest,
          chat_history:(messages as Message[]).map((m) 
=> `${m.role}: ${m.content}`).join('\n')}, 
          callbacks
          ).catch((e) => {
          console.error('____
___________ THIS IS THE ERROR ________', e);
      }); 

&#x200B;
```
---

     
 
MachineLearning -  [ [P] Retrieval augmented generation with OpenSearch and reranking [Video tutorial] ](https://www.reddit.com/r/MachineLearning/comments/16zouad/p_retrieval_augmented_generation_with_opensearch/) , 2023-10-08-0910
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

     
 
MachineLearning -  [ [D] Perplexity.ai Search Feasibility ](https://www.reddit.com/r/MachineLearning/comments/16x63ce/d_perplexityai_search_feasibility/) , 2023-10-08-0910
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

     
 
MachineLearning -  [ [P] vLLM, Langchain, Embedchain ? ](https://www.reddit.com/r/MachineLearning/comments/16ndyxc/p_vllm_langchain_embedchain/) , 2023-10-08-0910
```
Which libraries do you think would be the most important to learn between these, and to use in my next personal project 
? This will be a conversational chatbot trained on podcast transcripts
```
---

     
 
MachineLearning -  [ [R] Agents: An Open-source Framework for Autonomous Language Agents - AIWaves Inc 2023 ](https://www.reddit.com/r/MachineLearning/comments/16jl4pe/r_agents_an_opensource_framework_for_autonomous/) , 2023-10-08-0910
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

     
 
MachineLearning -  [ [P] Ways to speed up llama-2 summarization on sagemaker? ](https://www.reddit.com/r/MachineLearning/comments/16iutyp/p_ways_to_speed_up_llama2_summarization_on/) , 2023-10-08-0910
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

     
 
MachineLearning -  [ [P][R] Kani: A Lightweight Highly Hackable Open-Source Framework for Building Chat Applications with ](https://www.reddit.com/r/MachineLearning/comments/16gxp51/pr_kani_a_lightweight_highly_hackable_opensource/) , 2023-10-08-0910
```
Hey all, we just released our new project/paper and we thought you all might find it useful!

Our project (Kani) is a su
per lightweight and hackable alternative to frameworks like LangChain or simpleAIchat meant to help developers hook in c
allable functions or tools to chat models easily. With Kani, devs can write functions in pure python and just add one li
ne (the `@ai_function()` decorator) to turn any function into an AI-callable function!

Kani works with any model and ha
s built-in tools for OpenAI, HuggingFace, LLaMAv2, Vicuna, and GGML with more to come. Kani also never does any prompt e
ngineering under the hood and doesn't require learning complex library tools---all defaults are minimal and highly custo
mizable.

Check out our Colab for mini-examples of things like retrieval, web-search, model routing, etc. [https://colab
.research.google.com/github/zhudotexe/kani/blob/main/examples/colab\_examples.ipynb](https://colab.research.google.com/g
ithub/zhudotexe/kani/blob/main/examples/colab_examples.ipynb)  

If you're interested in learning more check out our lin
ks below!  
Paper: [https://arxiv.org/abs/2309.05542](https://arxiv.org/abs/2309.05542)  
GitHub: [https://github.com/zh
udotexe/kani](https://github.com/zhudotexe/kani)  
Docs: [https://kani.readthedocs.io/](https://kani.readthedocs.io/)
```
---

     
 
MachineLearning -  [ [D] Data Extraction using fine-tuned LLM? ](https://www.reddit.com/r/MachineLearning/comments/16fenlb/d_data_extraction_using_finetuned_llm/) , 2023-10-08-0910
```
Hey Reddit,

I'm working on a tool to pull data from highly irregular Excel files. I've gotten reasonable results which 
is extremely fast with standard Python coding, but it's far from perfect due to the lack of standardized templates. 

In
terestingly, when I tested ChatGPT-4 on a sample table, it did a decent job at data extraction. However, relying solely 
on GPT-4 has its downsides like token limits and slow processing speed (and data privacy issues). Plus, splitting the Ex
cel sheet to fit within these limits results in loss of context and data.

I'm considering fine-tuning a language model 
to post-process data that was in a Pandas DataFrame (perhaps converted to JSON). Has anyone had success with this approa
ch or have alternative recommendations? I've tried Langchain, but it wasn't helpful.

I have figured out to extract the 
relevant columns, but the post-processing part is where I am considering using an LLM which understands the domain and w
hat needs to be extracted based on the examples I feed it.

Looking forward to your thoughts! And would be happy to answ
er any additional questions.
```
---

     
 
MachineLearning -  [ [D] Chains and Agents ](https://www.reddit.com/r/MachineLearning/comments/16d7ee6/d_chains_and_agents/) , 2023-10-08-0910
```
I think there's a lot of confusion around AI agents today and it's mainly because of lack of definition and using the wr
ong terminology.

We've been talking to many companies who are claiming they're working on agents but when you look unde
r the hood, they are really just chains.

I just listened to the Latent Space pod with Harrison Chase (Founder of Langch
ain) and I really liked how he thinks about chains vs agents.

Chains: sequence of tasks in a more rigid order, where yo
u have more control, more predictability.  
Agents: handling the edge-cases, the long-tail of things that can happen.

A
nd the most important thing is that it's not an OR question but an AND one: you can use them in the same application by 
starting with chains -> figuring our the edge-cases -> using agents to deal with them.

https://preview.redd.it/l59sc4sr
i0nb1.png?width=3127&format=png&auto=webp&s=1f3f8730c48687eaabf1f554deb181cf35b96036
```
---

     
 
MachineLearning -  [ [P] FalkorDB - a fast Graph Database - Knowledge Graph as RAG ](https://www.reddit.com/r/MachineLearning/comments/16cg6k7/p_falkordb_a_fast_graph_database_knowledge_graph/) , 2023-10-08-0910
```
We're building a fast low latency Graph Database called FalkorDB that will also support Vector search.  
It's based on R
edis and can be used both as a stand alone database or a module for existing Redis.  
It feels like that is going to be 
the most optimized way to serve Knowledge as RAG, would love to get your feedback.  
[https://github.com/FalkorDB/falkor
db](https://github.com/FalkorDB/falkordb)  


It already supports LlamIndex and Langchain:  
[https://python.langchain.c
om/docs/use\_cases/more/graph/graph\_falkordb\_qa](https://python.langchain.com/docs/use_cases/more/graph/graph_falkordb
_qa)  
[https://gpt-index.readthedocs.io/en/latest/examples/index\_structs/knowledge\_graph/FalkorDBGraphDemo.html](http
s://gpt-index.readthedocs.io/en/latest/examples/index_structs/knowledge_graph/FalkorDBGraphDemo.html)

&#x200B;
```
---

     
 
deeplearning -  [ TheBloke/Llama-2-7b does not appear to have a file named pytorch_model.bin, tf_model.h5, model.ckpt  ](https://www.reddit.com/r/deeplearning/comments/16ihzn8/theblokellama27b_does_not_appear_to_have_a_file/) , 2023-10-08-0910
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

     
