 
all -  [ Size scaling for vector databases (Chroma DB specifically) ](https://www.reddit.com/r/LangChain/comments/170qmjp/size_scaling_for_vector_databases_chroma_db/) , 2023-10-06-0909
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

     
 
all -  [ AI assistant integration beyond the native integration? ](https://www.reddit.com/r/todoist/comments/170ptp5/ai_assistant_integration_beyond_the_native/) , 2023-10-06-0909
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

     
 
all -  [ Finetuned models for function calling? ](https://www.reddit.com/r/LocalLLaMA/comments/170pej3/finetuned_models_for_function_calling/) , 2023-10-06-0909
```
Hello. Are there finetuned LLaMa2 models that can reliably work for function calling yet? (Setting up agents in Langchai
n and such). Previous discussion is around 2 months old so I wonder if there has been some advances on this.

I have bee
n trying to build a chatbot that can search on the internet and can be locally hosted but the models I've tried are terr
ible at this.
```
---

     
 
all -  [ Give our customers an LLM to talk to about their data ](https://www.reddit.com/r/LocalLLaMA/comments/170npuw/give_our_customers_an_llm_to_talk_to_about_their/) , 2023-10-06-0909
```
Hello guys, we are a small web design company, and we are testing langchain and llama2 llm locally. We want to be able t
o create a chatbot for our customers so the llm can check out their hosting stats and our customers can ask questions su
ch as 'how much more space do I need if I want to add a new email account, create a database, when will I need to upgrad
e my account,  etc,,  So our main question is, where can we read up on how many concurrent users we can have if we use l
angchain and how can we setup ques or buffering so when the GPU is bogged down, it will still process the queries from o
ur customers but keep them in a waiting list until their request is up. Is this a crazy project or doable? Thanks!
```
---

     
 
all -  [ RecursiveCharacterTextSplitter: create_documents vs split_documents ](https://www.reddit.com/r/LangChain/comments/170mfkc/recursivecharactertextsplitter_create_documents/) , 2023-10-06-0909
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

     
 
all -  [ My strategy for picking a vector database: a side-by-side comparison ](https://www.reddit.com/r/LangChain/comments/170jigz/my_strategy_for_picking_a_vector_database_a/) , 2023-10-06-0909
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

     
 
all -  [ Interested in using LangChain and llama.cpp, to create industry specific search / chat bot, for data ](https://www.reddit.com/r/LangChain/comments/170ij5e/interested_in_using_langchain_and_llamacpp_to/) , 2023-10-06-0909
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

     
 
all -  [ I'm wondering if it's possible to patent the LangChain Process that I developed. ](https://www.reddit.com/r/legaladvice/comments/170i0ph/im_wondering_if_its_possible_to_patent_the/) , 2023-10-06-0909
```
Our team created a proprietary approach utilizing LLMs and LangChain derivative. Is it patentable?
```
---

     
 
all -  [ AutoGen from Microsoft ](https://www.reddit.com/r/learnmachinelearning/comments/170hl7w/autogen_from_microsoft/) , 2023-10-06-0909
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

     
 
all -  [ Need help here (Link in the description) ](https://www.reddit.com/r/LangChain/comments/170gj4f/need_help_here_link_in_the_description/) , 2023-10-06-0909
```
can you assist me on my query. I have explained my issue here with my small code:

https://github.com/langchain-ai/langc
hain/discussions/11429
```
---

     
 
all -  [ How to use LangChain and MapReduce to Classify Large Bodies of Text Using an LLM ](https://www.bluelabellabs.com/blog/how-to-use-langchain-and-mapreduce/) , 2023-10-06-0909
```

```
---

     
 
all -  [ Should I convert my html documents to text before storing them to save tokens? ](https://www.reddit.com/r/LangChain/comments/170etrb/should_i_convert_my_html_documents_to_text_before/) , 2023-10-06-0909
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

     
 
all -  [ What’s shaking? ](https://i.redd.it/jcud801uscsb1.jpg) , 2023-10-06-0909
```
Oh who knows
```
---

     
 
all -  [ LangChain - Your Key to Unlocking Multilingual Mastery! 🗝️🌍 ](https://www.reddit.com/r/u_Techup24/comments/170cj62/langchain_your_key_to_unlocking_multilingual/) , 2023-10-06-0909
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

     
 
all -  [ LangChain with local LLM on tabular data ](https://www.reddit.com/r/LangChain/comments/170cic8/langchain_with_local_llm_on_tabular_data/) , 2023-10-06-0909
```
Any one able to crack how to use langchain with open source llm (not open ai) to query database using agents
```
---

     
 
all -  [ I'm working with Confluence, and I need to perform question answering with attachments available in  ](https://www.reddit.com/r/LangChain/comments/170c8om/im_working_with_confluence_and_i_need_to_perform/) , 2023-10-06-0909
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

     
 
all -  [ UnstructuredDetectronModel Initialization TypeError ](https://www.reddit.com/r/LangChain/comments/170b61a/unstructureddetectronmodel_initialization/) , 2023-10-06-0909
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

     
 
all -  [ Approaches to increase speed of LangChain agent? Takes ~1minute to respond ](https://www.reddit.com/r/LangChain/comments/1709u74/approaches_to_increase_speed_of_langchain_agent/) , 2023-10-06-0909
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

     
 
all -  [ Looking for some guidance on a small project ](https://www.reddit.com/r/ChatGPTCoding/comments/17097sj/looking_for_some_guidance_on_a_small_project/) , 2023-10-06-0909
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

     
 
all -  [ Follow-up questions to previous conversations ](https://www.reddit.com/r/LangChain/comments/1708wxo/followup_questions_to_previous_conversations/) , 2023-10-06-0909
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

     
 
all -  [ Large text summary options? ](https://www.reddit.com/r/LangChain/comments/1706g3h/large_text_summary_options/) , 2023-10-06-0909
```
Any thoughts on how I can handle large text summary? The context is reading through hundreds of email chains and summari
zing them.

I’ve been playing around with large text summary models on hugging face but the hallucinations are insane, l
ike 50% of the summary is made up…

Looking at between 10,000-50,000 characters…
```
---

     
 
all -  [ Text splitting for word document ](https://www.reddit.com/r/LangChain/comments/1705onu/text_splitting_for_word_document/) , 2023-10-06-0909
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

     
 
all -  [ looking to figure out how to get an agent to read text classifiers and then apply to descriptions ](https://www.reddit.com/r/LangChain/comments/17021gf/looking_to_figure_out_how_to_get_an_agent_to_read/) , 2023-10-06-0909
```
I'm trying to get LangChain to read two Excel files - one with classifier info and the other with company descriptions. 
The goal is to classify the companies based on the info in the first file. Got the files loaded up, but stumbling a bit 
with setting up the agent and executor in LangChain to process this data and get the results out. Anyone here tackled so
mething similar or got some tips? Thanks!
```
---

     
 
all -  [ Handle sessions with separate ID's without res-instantiating RedisChatMessageHistory ](https://www.reddit.com/r/LangChain/comments/16zyemd/handle_sessions_with_separate_ids_without/) , 2023-10-06-0909
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

     
 
all -  [ Easy RAG Implementation for GenAI using Mongo: Langchain alternative ](https://www.reddit.com/r/mongodb/comments/16zx1gc/easy_rag_implementation_for_genai_using_mongo/) , 2023-10-06-0909
```
Hi all, we worked really hard to develop our open source library on Github for easy, straightforward RAG implementation 
for GenAI using Mongo (and Milvus, FAISS or PineCone for vector DB). We built in a lot of features for easy document ing
estion that is scalable as well as native parsing for PDFs and Office documents for a very fast ingestion. Please check 
out our LLMWare library and we would be extra grateful if you can leave a star!

[https://github.com/llmware-ai/llmware]
(https://github.com/llmware-ai/llmware)
```
---

     
 
all -  [ New Github Library for RAG: Langchain Alternative ](https://www.reddit.com/r/ArtificialNtelligence/comments/16zwrsa/new_github_library_for_rag_langchain_alternative/) , 2023-10-06-0909
```
HI all, we worked really hard and created an open source library that is an integrated RAG system for GenAI with a lot o
f great features on Github for LLMWare (straightforward, easy to use). It would be great if you can check it out (would 
be extra grateful if you can leave a star). Thank you!

[https://github.com/llmware-ai/llmware](https://github.com/llmwa
re-ai/llmware)
```
---

     
 
all -  [ Interesting hallucinations with a RAG-type chatbot ](https://www.reddit.com/r/LangChain/comments/16zqz0p/interesting_hallucinations_with_a_ragtype_chatbot/) , 2023-10-06-0909
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

     
 
all -  [ Memory is not working with ConversationalRetrievalQAChain. ](https://www.reddit.com/r/LangChain/comments/16zpv8l/memory_is_not_working_with/) , 2023-10-06-0909
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

     
 
all -  [ As a soloproneur, here is how I'm scaling with AI and GPT-based tools ](https://www.reddit.com/r/Entrepreneur/comments/16zp7pt/as_a_soloproneur_here_is_how_im_scaling_with_ai/) , 2023-10-06-0909
```
Being a solopreneur has its fair share of challenges. Currently I've got businesses in ecommerce, agency work, and affil
iate marketing, and one undeniable truth remains: to truly scale by yourself, you need more than just sheer will. That's
 where I feel technology, especially AI, steps in.

As such, I wanted some AI tools that have genuinely made a differenc
e in my own work as a solo business operator. No fluff, just tried-and-true tools and platforms that have worked for me.
 The ability for me to scale alone with AI tools that take advantage of GPT in one way, or another has been significant 
and really changed my game over the past year. They bring in an element of adaptability and intelligence and work right 
alongside “traditional automation”. Whether you're new to this or looking to optimize your current setup, I hope this po
st helps. FYI I used multiple prompts with GPT-4 to draft this using my personal notes.

# Plus AI (add-on for google sl
ides/docs)

I handle a lot of sales calls and demos for my AI automation agency. As I’m providing a custom service rathe
r than a product, every client has different pain points and as such I need to make a new slide deck each time. And maki
ng slides used to be a huge PITA and pretty much the bane of my existence until slide deck generators using GPT came out
. My favorite so far has been PlusAI, which works as a plugin for Google Slides. You pretty much give it a rough idea, o
r some key points and it creates some slides right within Google Slides. For me, I’ve been pasting the website copy or a
ny information on my client, then telling PlusAI the service I want to propose. After the slides are made, you have a lo
t of leeway to edit the slides again with AI, compared to other slide generators out there. With 'Remix', I can switch u
p layouts if something feels off, and 'Rewrite' is there to gently nudge the AI in a different direction if I ever need 
it to. It's definitely given me a bit of breathing space in a schedule that often feels suffocating.

## echo.win (web-b
ased app)

As a solopreneur, I'm constantly juggling roles. Managing incoming calls can be particularly challenging. Ech
o.win, a modern call management platform, has become a game-changer for my business. It's like having a 24/7 personal as
sistant. Its advanced AI understands and responds to queries in a remarkably human way, freeing up my time. A standout f
eature is the Scenario Builder, allowing me to create personalized conversation flows. Live transcripts and in-depth ana
lytics help me make data-driven decisions. The platform is scalable, handling multiple simultaneous calls and improving 
customer satisfaction. Automatic contact updates ensure I never miss an important call. Echo.win's pricing is reasonable
, offering a personalized business number, AI agents, unlimited scenarios, live transcripts, and 100 answered call minut
es per month. Extra minutes are available at a nominal cost. Echo.win has revolutionized my call management. It's a comp
rehensive, no-code platform that ensures my customers are always heard and never missed

# MindStudio by YouAi (web app/
GUI)

I work with numerous clients in my AI agency, and a recurring task is creating chatbots and demo apps tailored to 
their specific needs and connected to their knowledge base/data sources. Typically, I would make production builds from 
scratch with libraries such as LangChain/LlamaIndex, however it’s quite cumbersome to do this for free demos. As each cl
ient has unique requirements, it means I'm often creating something from scratch. For this, I’ve been using MindStudio (
by YouAi) to quickly come up with the first iteration of my app. It supports multiple AI models (GPT, Claude, Llama), le
t’s you upload custom data sources via multiple formats (PDF, CSV, Excel, TXT, Docx, and HTML), allows for custom flows 
and rules, and lets you to quickly publish your apps. If you are in their developer program, YouAi has built-in payment 
infrastructure to charge your users for using your app.

Unlike many of the other AI builders I’ve tried, MindStudio bas
ically lets me dictate every step of the AI interaction at a high level, while at the same time simplifying the behind-t
he-scenes work. Just like how you'd sketch an outline or jot down main points, you start with a scaffold or decide to 'r
emix' an existing AI, and it will open up the IDE. I often find myself importing client data or specific project details
, and then laying out the kind of app or chatbot I'm looking to prototype. And once you've got your prototype you can cu
stomize the app as much as you want.

## LLamaIndex (Python framework)

As mentioned before, in my AI agency, I frequent
ly create chatbots and apps for clients, tailored to their specific needs and connected to their data sources. LlamaInde
x, a data framework for LLM applications, has been a game-changer in this process. It allows me to ingest, structure, an
d access private or domain-specific data.

The major difference over LangChain is I feel like LlamaIndex does high level
 abstraction much better.. Where LangChain unnecessarily abstracts the simplest logic, LlamaIndex actually has clear ben
efits when it comes to integrating your data with LLMs- it comes with data connectors that ingest data from various sour
ces and formats, data indexes that structure data for easy consumption by LLMs, and engines that provide natural languag
e access to data. It also includes data agents, LLM-powered knowledge workers augmented by tools, and application integr
ations that tie LlamaIndex back into the rest of the ecosystem. LlamaIndex is user-friendly, allowing beginners to use i
t with just five lines of code, while advanced users can customize and extend any module to fit their needs. To be compl
etely honest, to me it’s more than a tool- at its heart it’s a framework that ensures seamless integration of LLMs with 
data sources while allowing for complete flexibility compared to no-code tools.

## GoCharlie (web app)

GoCharlie, the 
first AI Agent product for content creation, has been a game-changer for my business. Powered by a proprietary LLM calle
d Charlie, it's capable of handling multi-input/multi-output tasks. GoCharlie's capabilities are vast, including content
 repurposing, image generation in 4K and 8K for various aspect ratios, SEO-optimized blog creation, fact-checking, web r
esearch, and stock photo and GIF pull-ins. It also offers audio transcriptions for uploaded audio/video files and YouTub
e URLs, web scraping capabilities, and translation.

One standout feature is its multiple input capability, where I can 
attach a file (like a brand brief from a client) and instruct it to create a social media campaign using brand guideline
s. It considers the file, prompt, and website, and produces multiple outputs for each channel, each of which can be edit
ed separately. Its multi-output feature allows me to write a prompt and receive a response, which can then be edited fur
ther using AI. Overall, very satisfied with GoCharlie and in my opinion it really presents itself as an effective altern
ative to GPT based tools.

# ProfilePro (chrome extension)

As someone overseeing multiple Google Business Profiles (GBP
s) for my various businesses, I’ve been using ProfilePro by Merchynt. This tool stood out with its ability to auto-gener
ate SEO-optimized content like review responses and business updates based on minimal business input. It works as a Chro
me extension, and offers suggestions for responses automatically on your GBP, with multiple options for the tone it will
 write in. As a plus, it can generate AI images for Google posts, and offer suggestions for services and service/product
 descriptions. While it streamlines many GBP tasks, it still allows room for personal adjustments and refinements, offer
ing a balance between automation and individual touch. And if you are like me and don't have dedicated SEO experience, i
t can handle ongoing optimization tasks to help boost visibility and drive more customers to profiles through Google Map
s and Search
```
---

     
 
all -  [ [P] Retrieval augmented generation with OpenSearch and reranking [Video tutorial] ](https://www.reddit.com/r/MachineLearning/comments/16zouad/p_retrieval_augmented_generation_with_opensearch/) , 2023-10-06-0909
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

     
 
all -  [ Multiple llm route ](https://www.reddit.com/r/LangChain/comments/16zhtfl/multiple_llm_route/) , 2023-10-06-0909
```
 I am working on a project that involves conversational interactions with both Word and Excel files. Specifically, for h
andling Word files, I utilized the Lama2 model, which relies on a vector database to provide responses. Meanwhile, for E
xcel-related tasks, I used the GPT-3.5 model. How to determine which model to use based on the user's input prompt.
```
---

     
 
all -  [ Custom LLM agent with custom tool not work due to lack func argument ](https://www.reddit.com/r/LangChain/comments/16zcfpa/custom_llm_agent_with_custom_tool_not_work_due_to/) , 2023-10-06-0909
```
while following [https://python.langchain.com/docs/modules/agents/how\_to/custom\_llm\_agent#set-up-tool](https://python
.langchain.com/docs/modules/agents/how_to/custom_llm_agent#set-up-tool), we also want to custom tool adding extra schema
 validation, from the example for the tool listed, we need name, description, and func field, for custom tool we only ha
ve name and description field, here's the custom tool code [https://gist.github.com/elvis-cai/203487d2bfd11d57625d84f812
2e875e](https://gist.github.com/elvis-cai/203487d2bfd11d57625d84f8122e875e),   

this is the custom tool we are referrin
g to [https://python.langchain.com/docs/modules/agents/tools/custom\_tools#subclassing-the-basetool-class](https://pytho
n.langchain.com/docs/modules/agents/tools/custom_tools#subclassing-the-basetool-class).

&#x200B;

not sure how to make 
it work with pydantic validation, thanks. 
```
---

     
 
all -  [ Is there anyway to get chat-gpt's response while its still generating via langchain and python api? ](https://www.reddit.com/r/OpenAI/comments/16za9uw/is_there_anyway_to_get_chatgpts_response_while/) , 2023-10-06-0909
```
I created a short script that allows for me to interact with chat-gpt over phone. It prompts chat-gpt, feeds its respons
e into elevenlabs and then plays the audio out loud. However, this takes a very long time because eleven labs only stars
 generating the audio after gpt is completely done generating its response, and then it only starts playing after the en
tire audio has finished generating. This is super slow especially for longer responses, and it ruins the entire flow of 
the conversation. Does anyone know if there's anything I can do about this?
```
---

     
 
all -  [ Data Privacy - Memory features of Langchain ](https://www.reddit.com/r/LangChain/comments/16z9pxs/data_privacy_memory_features_of_langchain/) , 2023-10-06-0909
```
Hi all,

As the title indicates, I want to ask about the memory features in Langchain. I was talking to someone at work 
who raised some concerns about data security/privacy when dealing with the memory classes in Langchain. The main concern
 they have is about chat history getting stored in an external database during runtime.

My personal understanding based
 on documentation and also looking at the langchain repo is that the data is stored locally and there doesn't seem to be
 any indication of any interaction with external databases. If any of y'all have dealt with these kind of questions befo
re, how did you approach it? What steps or methods would you recommend to definitively address and alleviate these data 
storage concerns?

Thanks!
```
---

     
 
all -  [ Strategy for PDF data extraction and Display ](https://www.reddit.com/r/LangChain/comments/16z7sfl/strategy_for_pdf_data_extraction_and_display/) , 2023-10-06-0909
```
I'm learning LangChain and working on a project where I need to:

1. Extract data from a \~50 page PDF.
2. Display this 
data in structured tables.

For context, think of the PDF as a product catalog, with item names, descriptions, and price
s.

My first program uses PyPDF2 for PDF parsing and FAISS coupled with OpenAIEmbeddings for similarity-based querying. 
For instance:

    query = 'What is the price of the television set'
    docs = document_search.similarity_search(query)

    chain.run(input_documents=docs, question=query

This works well, but the result is plain-text and lacks structure. 
I've now shifted to learning structured output, creating a schema to define data representation.  My basic structure cou
ld be the item name, the item description, and the item cost.

Now, onto my main question: What's the most efficient app
roach for feeding PDF data into my structured output chain? Currently, I'm using broad queries like 'list all items with
 a price,' which tap into my initial vector-based similarity search framework. Is this approach more complicated than ne
cessary? Given that I've moved towards structured outputs and am essentially using 'catch-all' queries, the need for vec
tor-based querying seems redundant.  


\*Update - I did try just submitted the entire contents of the PDF, but its far 
larger than the token limit for most models I'm using; What's the best way to split up the document and submit for my st
ructured input, if not the vector/similarity search method?

Any tips or best practices are welcome!
```
---

     
 
all -  [ Langchain Chatbot is not that great.. ](https://www.reddit.com/r/LangChain/comments/16z7nzk/langchain_chatbot_is_not_that_great/) , 2023-10-06-0909
```
I noticed that langchain chatbot is prone to hallucination easily and does not provide accurate data. What's your expere
ince with it?  
Below is an example of it importing a class that does not exist (I searched under langchain repo -> libs
 -> langchain -> langchain -> llms)   


Perhaps it's not meant to solve this kinda probelm? would like to know others' 
feedbacks. 

https://preview.redd.it/4jkg6dd5r2sb1.png?width=904&format=png&auto=webp&s=318a2bad3ff686e02385409f8679e695
2b0e51e2

second example:   
correct way to import chatOllama: \`from langchain.chat\_models import ChatOllama\`   


ht
tps://preview.redd.it/jij85uhar2sb1.png?width=2306&format=png&auto=webp&s=569ccd2d4758e3da7a4cdd22c238b3e5001f2c72

&#x2
00B;
```
---

     
 
all -  [ After a few hours of battleing to make it understand ](https://www.reddit.com/r/LangChain/comments/16z54mf/after_a_few_hours_of_battleing_to_make_it/) , 2023-10-06-0909
```
This is peak prompt engineering.

&#x200B;

&#x200B;

https://preview.redd.it/emhr6d2p92sb1.png?width=957&format=png&aut
o=webp&s=2b8e1aa1f37b31c1864b7a432a49239bb4086efa
```
---

     
 
all -  [ User Feedback for RAG ](https://www.reddit.com/r/LangChain/comments/16z4rn3/user_feedback_for_rag/) , 2023-10-06-0909
```
I’ve read about using AI to generate sample questions and answers, then having end-users provide feedback and using that
 data to fine-tune a model. Would this approach would with embeddings and RAG? If the vector embedding contained sample 
questions and answers, could I prompt the bot to answer in the style of the sample answers from the embedding?
```
---

     
 
all -  [ Here to try to solve your LLM problems ](https://www.reddit.com/r/LangChain/comments/16z4mha/here_to_try_to_solve_your_llm_problems/) , 2023-10-06-0909
```
I have been working with NLP using machine learning and deep learning for 6.5  years and with LLMs since the time it bec
ame a thing. Have been working with other transformers models before that as well. 

If anyone has any business problem 
and wants  some help, I will be trying my best to help them out. I will be doing this for a small fee. 

No charge if I 
hear the problem and I do not have adequate knowledge to solve the issue even if I have spent some time towards solving 
it. 

Will share credential via DM if required.
```
---

     
 
all -  [ can RAG models base their answers from outside the documents? ](https://www.reddit.com/r/LangChain/comments/16z4bd3/can_rag_models_base_their_answers_from_outside/) , 2023-10-06-0909
```
can RAG models base their answers from outside the documents used?
```
---

     
 
all -  [ [Announcement] Upcoming event – Reddit AMA with Harrison Chase, co-founder and CEO of LangChain: Tue ](https://www.reddit.com/r/LangChain/comments/16z1s1p/announcement_upcoming_event_reddit_ama_with/) , 2023-10-06-0909
```
Join us on Tuesday, October 24th from 9-11 AM Pacific (12-2 PM Eastern) for an **AMA hosted** by **Harrison Chase, co-fo
under and CEO of LangChain**. This is your opportunity to ask Harrison questions about utilizing LangChain in developing
 large language model (LLM) applications, and to *share your own ideas and suggestions*. Take advantage of this chance t
o learn more about how to leverage LangChain in your own projects and get insights into latest developments.
```
---

     
 
all -  [ Use multiple Chroma Databases in Langchain ](https://www.reddit.com/r/LangChain/comments/16z0nkh/use_multiple_chroma_databases_in_langchain/) , 2023-10-06-0909
```
I'm working on making a chatPDF-like program for a school professor but he requested to keep the subjects divided, so I 
was thinking about making different pages for my website, each for every subject and link to every page a specific chrom
aDB, I don't know if it's possible though and I haven't found anything on the documentation.

Has anyone tried this befo
re or knows if it's even possible?
```
---

     
 
all -  [ My Journey with Langchain on finishing my MA and reinventing Dropbox powered by GPT ](https://www.reddit.com/r/LangChain/comments/16yz1ej/my_journey_with_langchain_on_finishing_my_ma_and/) , 2023-10-06-0909
```
As an introvert who finds solace in books and coding, I wanted to share a personal story that began in November last yea
r, that’s when I discovered Langchain. I was in the process of writing my master's thesis at the time. The timing just h
appened to be so perfect that I was using Langchain to conduct research for my final thesis. 

It allowed me to create m
y own knowledge base, a place where I could access a treasure trove of resources, including YouTube videos, PDFs, docume
nts, and presentations, and get needed information quickly.

Today, finally, as also a proud tiny contributor to Langcha
in I’m excited to present to you Knowbase.ai, my small app  that enables you to harness the power of your accumulated kn
owledge.

https://reddit.com/link/16yz1ej/video/s7s283z021sb1/player

Knowbase.ai is a versatile platform that can host 
YouTube videos, PDFs, documents, and presentations, making it your one-stop hub for knowledge.
```
---

     
 
MachineLearning -  [ [D] Perplexity.ai Search Feasibility ](https://www.reddit.com/r/MachineLearning/comments/16x63ce/d_perplexityai_search_feasibility/) , 2023-10-06-0909
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

     
 
MachineLearning -  [ [P] vLLM, Langchain, Embedchain ? ](https://www.reddit.com/r/MachineLearning/comments/16ndyxc/p_vllm_langchain_embedchain/) , 2023-10-06-0909
```
Which libraries do you think would be the most important to learn between these, and to use in my next personal project 
? This will be a conversational chatbot trained on podcast transcripts
```
---

     
 
MachineLearning -  [ [R] Agents: An Open-source Framework for Autonomous Language Agents - AIWaves Inc 2023 ](https://www.reddit.com/r/MachineLearning/comments/16jl4pe/r_agents_an_opensource_framework_for_autonomous/) , 2023-10-06-0909
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

     
 
MachineLearning -  [ [P] Ways to speed up llama-2 summarization on sagemaker? ](https://www.reddit.com/r/MachineLearning/comments/16iutyp/p_ways_to_speed_up_llama2_summarization_on/) , 2023-10-06-0909
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

     
 
MachineLearning -  [ [P][R] Kani: A Lightweight Highly Hackable Open-Source Framework for Building Chat Applications with ](https://www.reddit.com/r/MachineLearning/comments/16gxp51/pr_kani_a_lightweight_highly_hackable_opensource/) , 2023-10-06-0909
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

     
 
MachineLearning -  [ [D] Data Extraction using fine-tuned LLM? ](https://www.reddit.com/r/MachineLearning/comments/16fenlb/d_data_extraction_using_finetuned_llm/) , 2023-10-06-0909
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

     
 
MachineLearning -  [ [D] Chains and Agents ](https://www.reddit.com/r/MachineLearning/comments/16d7ee6/d_chains_and_agents/) , 2023-10-06-0909
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

     
 
MachineLearning -  [ [P] FalkorDB - a fast Graph Database - Knowledge Graph as RAG ](https://www.reddit.com/r/MachineLearning/comments/16cg6k7/p_falkordb_a_fast_graph_database_knowledge_graph/) , 2023-10-06-0909
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

     
 
deeplearning -  [ TheBloke/Llama-2-7b does not appear to have a file named pytorch_model.bin, tf_model.h5, model.ckpt  ](https://www.reddit.com/r/deeplearning/comments/16ihzn8/theblokellama27b_does_not_appear_to_have_a_file/) , 2023-10-06-0909
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

     
 
deeplearning -  [ How to find 'custom' datasets for LLM ](https://www.reddit.com/r/deeplearning/comments/16bj3hg/how_to_find_custom_datasets_for_llm/) , 2023-10-06-0909
```
Hey folks,

I've been digging everywhere, including here, for LLMs and custom applications. So, I read many things, lear
ned from ppl here. Its time to try something. I will try implement Llama v2 - Langchain - Chroma combination. But also I
 want to upload a dataset so that I can try my model on that. 

I find some datasets big enough (for now, 2-5 gb is ok) 
however they are table-style. I want something more texty, I mean I could use 'American Stories' or 'Arxiv' however I be
lieve that they are already used by Llama to train. 

&#x200B;

Is there any suggestions or sources that you can provide
 ? Thanks!
```
---

     
