 
all -  [ Question about chatbot and chat message history with vector db ](https://www.reddit.com/r/LangChain/comments/1d3ok4l/question_about_chatbot_and_chat_message_history/) , 2024-05-30-0911
```
Basically I am creating an app in which you are able to chat with the openai and I want to store the last 7 times or 7 d
ays worth of message history from user. Now the problem is if i plainly save the chat messages then it takes up a lot of
 token size. I tried using the conversation summary buffer and all kinds of memory but either they were also resulting i
n a lot of tokens or did not give as expected output.

My question is that is there a way that once the user is done wit
h the chat I can store the chat in a vector db and then whenever a user chats with the AI again it first checks the vect
or db for a reference of that object and returns related data and then my open ai llm with a specified prompt and the da
ta collected give a response whereas if there is no data found speific to the object then my llm plainly uses the prompt
 I have given it?

Kindly give me if there are any other ways to do it 

My tech stack is  
Frontend Flutter, Backend Py
thon therefore it would be easy for me to attach langchain to python and just push requests from my app to my hosted api
 using python. 

Thanks
```
---

     
 
all -  [ How to build a R.A.G. chatbot with LangChain, OpenAI and Pinecone ](https://youtu.be/Bxj4btI3TzY) , 2024-05-30-0911
```

```
---

     
 
all -  [ Generative AI Agents Developer Contest with NVIDIA and LangChain ](https://www.reddit.com/r/nvidia/comments/1d3ng79/generative_ai_agents_developer_contest_with/) , 2024-05-30-0911
```
As part of the NVIDIA developer team, I wanted to share details about our current [Generative AI Agents Developer Contes
t with LangChain](https://nvda.ws/4dXWDE3), running now through June 17.

This is your chance to start developing your n
ext Generative AI application for a chance to win an NVIDIA 4090 GPU and LangSmith credits.

To get started, check out o
ur step-by-step developer resources on our [contest page](https://nvda.ws/4dXWDE3) and our [ contest tips and tricks](ht
tps://nvda.ws/44ZJUN3) technical blog. Connect with NVIDIA and LangChain technical experts on our [Discord channel](http
s://discord.com/invite/nvidiadeveloper) to help with troubleshooting and to answer your questions.

Participants will ha
ve the chance to win GPUs and hundreds of dollars worth of rewards from LangChain:

* Two winners will each receive an [
NVIDIA GeForce RTX 4090 GPU](https://www.nvidia.com/en-us/geforce/graphics-cards/40-series/rtx-4090/).
* One special men
tion will receive an NVIDIA GeForce RTX 4080 SUPER.
* The top 10 projects will each receive $200 in LangSmith credits an
d LangChain merchandise
* The top 100 projects will each receive an[ NVIDIA Deep Learning Institute LLM course](https://
www.nvidia.com/en-us/training/).
* All valid participants will receive a digital participation certificate signed by NVI
DIA CEO Jensen Huang.

See the contest [Terms & Conditions](https://www.nvidia.com/en-us/ai-data-science/generative-ai/d
eveloper-contest-with-langchain/terms-and-conditions/)

Good luck with your projects!

https://preview.redd.it/hj81jz30q
f3d1.jpg?width=1920&format=pjpg&auto=webp&s=e04e566f7268f021c430f6c93f30957a621554b5
```
---

     
 
all -  [ Visual Agents Flow Engineering Tool Early-Access ](https://www.reddit.com/r/LangChain/comments/1d3iv90/visual_agents_flow_engineering_tool_earlyaccess/) , 2024-05-30-0911
```
Hi,  
   I'm working on a visual agents tool built on langchain and looking for people to try it out and maybe give some
 feedback or thoughts on it. It's a completely serverless tool so there is no backend or API and all the execution and d
ata resides local and private to you.

What do you think? I'm just one guy building this, so I'm hoping to get some comm
unity input! Thank you

Here is a quick demo of building a SQL Agent  and then answering a question about your data. All
 within YOUR browser environment.  
[https://youtu.be/\_3crxBzVg3A?si=-qCtoBv21NrIcFws](https://youtu.be/_3crxBzVg3A?si=
-qCtoBv21NrIcFws)  


And the app

[https://app.visualagents.ai/#/](https://app.visualagents.ai/#/)  

```
---

     
 
all -  [ Need a Help on creating RAG-based SQL Bot ](https://www.reddit.com/r/LangChain/comments/1d3hhkj/need_a_help_on_creating_ragbased_sql_bot/) , 2024-05-30-0911
```
I have a requirement to build a Chatbot Application over a SQL DB , Here the SQL DB will be very huge consists of many F
act and Dimensional tables,  Here are my below queries and please try to help me answer or provide better references.

1
. Chatbot must be able to pick table names dynamically based on the user input and form queries and execute

2. How a Ve
ctore DB can be leveraged here, can we  embed all the tables and store in the vectoreDB, will be easier to query on simi
larity search?- am I missing any basics here please guide

  
3. is it a viable option to build an RAG system on the SQL
 DB and have it embedded into Vector DB ?  
and use memory management to retrieve the previously asked Queries to pop up
 automatically ?

  
can you please help!
```
---

     
 
all -  [ gpt-4o App for Windows and Linux and macos =) MIT licenced ](https://www.reddit.com/r/aiagents/comments/1d3h3oc/gpt4o_app_for_windows_and_linux_and_macos_mit/) , 2024-05-30-0911
```
# Explanation and Reason

Hi i am python developer and after OpenAI GPT-4o launch, i just i little bit angry because the
 app that they talked about just work in MacOS and a joke, it will come to windows november lol. Come on bro, if there i
s API, developers like us can make this app and release in just few days with langchain agent and tool infrastructure.


So i just release our GPT-4o clone and its totaly usable. You can use to take meeting notes, writing code and copying to
 your clipboard, or read and remember your calendar. There is unlimited possibilities.

# Current Features

* \*\*Screen
 Read\*\*
* Microphone
* \*\*System Audio\*\*
* Memory

--

* Open and close app
* Open a URL
* \*\*Clipboard\*\*
* Sear
ch Engines
* \*\*Python and SH Interpreters\*\*
* Writing and Running Scripts
* Using your Telegram Account
* Knowledge 
Management

# Open Call to devs

If there is some people to interest and develop this and adding some features just like
 auto take screen shot each 5 second and say somethings if something wrong. We can open a **GitHub Organization** and de
velop together. Just for open-source, just for competition.

https://preview.redd.it/mipkh0pgbe3d1.png?width=656&format=
png&auto=webp&s=988cb7a9653c1860d854d13fd3f415de7192ff13

[onuratakan/gpt-computer-assistant: gpt-4o Desktop Personel As
isstant (github.com)](https://github.com/onuratakan/gpt-computer-assistant)
```
---

     
 
all -  [ Would my project look good on a resume? Or is it just an GPT wrapper? ](https://www.reddit.com/r/SideProject/comments/1d3h1l8/would_my_project_look_good_on_a_resume_or_is_it/) , 2024-05-30-0911
```
Hey everyone,

I'm currently a rising sophomore in college, and I am trying to make a few projects for my CS resume, wor
king with Python, Java, C++, and JS/TS. For this one, I am trying to incorporate Python and some kind of AI/RAG.

My pro
ject is an AI that utilizes RAG in order to help students in college study by using the learning-by-teaching method. Ess
entially:  
The User starts a new study session and is prompted to upload their notes/study documents (which can be type
d, handwritten, etc.).  
After, the AI processes the notes and then after asking the user what exactly they want to stud
y, the AI starts asking the user questions about the notes.  
The user then answers the questions, using text or microph
one, and then the AI grades the user's answers based on the notes and also just general knowledge.

The AI essentially r
eplaces a fellow student that would quiz the user.

I have not programmed this big of a project before, or a web dev/AI 
project, but I am planning to use:

  
**For Frontend:**

TypeScript with React.js

Tailwind CSS

Redux



**Backend:**


FastAPI - Python

PostgreSQL

LangChain

Hugging Face

Tesseract OCR

PyMuPDF

OpenCV

Auth0



**Server:**

AWS

Docke
r

Kubernetes

How does this sound?
```
---

     
 
all -  [ gpt-4o App for Windows and Linux and macos =) MIT licenced ](https://www.reddit.com/r/gpt_4o/comments/1d3h060/gpt4o_app_for_windows_and_linux_and_macos_mit/) , 2024-05-30-0911
```
# Explanation and Reason

Hi i am python developer and after OpenAI GPT-4o launch, i just i little bit angry because the
 app that they talked about just work in MacOS and a joke, it will come to windows november lol. Come on bro, if there i
s API, developers like us can make this app and release in just few days with langchain agent and tool infrastructure.


So i just release our GPT-4o clone and its totaly usable. You can use to take meeting notes, writing code and copying to
 your clipboard, or read and remember your calendar. There is unlimited possibilities.

# Current Features

* \*\*Screen
 Read\*\*
* Microphone
* \*\*System Audio\*\*
* Memory

--

* Open and close app
* Open a URL

* \*\*Clipboard\*\*
* Sea
rch Engines
* \*\*Python and SH Interpreters\*\*
* Writing and Running Scripts
* Using your Telegram Account
* Knowledge
 Management

# Open Call to devs

If there is some people to interest and develop this and adding some features just lik
e auto take screen shot each 5 second and say somethings if something wrong. We can open a **GitHub Organization** and d
evelop together. Just for open-source, just for competition.

https://preview.redd.it/mipkh0pgbe3d1.png?width=656&format
=png&auto=webp&s=988cb7a9653c1860d854d13fd3f415de7192ff13

  


[onuratakan/gpt-computer-assistant: gpt-4o Desktop Perso
nel Asisstant (github.com)](https://github.com/onuratakan/gpt-computer-assistant)
```
---

     
 
all -  [ Attempting to Parse PDF's with Financial Data (Balance Sheets, P&Ls, 10Ks) ](https://www.reddit.com/r/LangChain/comments/1d3fz8x/attempting_to_parse_pdfs_with_financial_data/) , 2024-05-30-0911
```
Has anyone had any luck using LangChain to parse these kind of documents?

I built a chatbot before to answer questions 
about a code base and about research papers. Those were pretty straight forward. But reading financial pdfs has turned o
ut to be a real challenge.

I'm able to get good answers for pdfs that are more structured (like some of the P&L's) but 
with others it's constantly providing wrong answers or no answer and consistently referencing wrong documents.

I'm feel
 like it probably has to do with how I'm vectorizing the data but I'm at a loss. 

Here's the code:

    import os
    o
s.environ['PINECONE_API_KEY'] = PINECONE_API_KEY
    
    from langchain.retrievers.self_query.base import SelfQueryRetr
iever
    from langchain.chains.query_constructor.base import AttributeInfo
    from langchain.prompts import ChatPrompt
Template
    from langchain.schema.output_parser import StrOutputParser
    from langchain.memory import ConversationTok
enBufferMemory
    from langchain_core.prompts import MessagesPlaceholder
    from langchain_openai.embeddings import Op
enAIEmbeddings
    from langchain_openai.chat_models import ChatOpenAI
    from langchain_community.document_loaders imp
ort DirectoryLoader
    from langchain_community.vectorstores import Pinecone as PC
    from pinecone import Pinecone, S
erverlessSpec
    import nltk
    
    class RAG():
        def __init__(self,
                     docs_dir: str,
     
                n_retrievals: int = 4,
                     chat_max_tokens: int = 3097,
                     model_name
 = 'gpt-4',
                     creativeness: float = 0.7):
            self.__model = self.__set_llm_model(model_name,
 creativeness)
            self.__docs_list = self.__get_docs_list(docs_dir)
            self.__retriever = self.__set_r
etriever(k=n_retrievals)
    
        def __set_llm_model(self, model_name = 'gpt-4', temperature: float = 0.7):
       
     return ChatOpenAI(
                       model_name=model_name, 
                       temperature=temperature, 

                       openai_api_key=os.environ['OPENAI_API_KEY'])
        
        def __get_docs_list(self, docs_dir:
 str) -> list:
            print('Loading documents...')
            loader = DirectoryLoader(docs_dir,
                
                     recursive=True,
                                     show_progress=True,
                          
           use_multithreading=True,
                                     max_concurrency=4)
            docs_list = load
er.load_and_split()
           
            return docs_list
        
        def __set_retriever(self, k: int = 4):
   
         # Initialize Pinecone
            pinecone = Pinecone(
                api_key=PINECONE_API_KEY
            )
 
           index_name = 'fin-docs'
    
            embeddings = OpenAIEmbeddings(model='text-embedding-3-small')
      
      
            # Create Pinecone index if it doesn't exist
            if index_name not in pinecone.list_indexes().
names():
                pinecone.create_index(
                    name=index_name, 
                    dimension=3072
, 
                    metric='cosine', 
                    spec=ServerlessSpec(cloud='aws', region='us-east-1')
      
          )
            
            vector_store = PC.from_documents(
                self.__docs_list,
               
 embedding=embeddings,
                index_name=index_name
            )
    
            _retriever = SelfQueryRetrie
ver.from_llm(
                self.__model,
                vector_store,
                document_content_description,

                metadata_field_info,
                search_kwargs={'k': k}
            )
    
            return _retri
ever
        
        def __set_chat_history(self, max_token_limit: int = 3097):
            return ConversationTokenBuf
ferMemory(
                       llm=self.__model,         
                       max_token_limit=max_token_limit,
   
                    return_messages=True)
        
        def ask(self, question: str) -> str:
            prompt = Cha
tPromptTemplate.from_messages([
                ('system', 'You are an assistant responsible for answering questions 
  
                      about documents. Answer the user's question with a 
                        reasonable level of de
tail and based on the following 
                        context document(s):\n\n{context}'),
                ('user', '
{input}'),
            ])
           
            output_parser = StrOutputParser()
            chain = prompt | self.__
model | output_parser
            answer = chain.invoke({
                'input': question,
                'context': 
self.__retriever.get_relevant_documents(question)
            })
           
            return answer

I can try and pr
ovide example docs if that would help as well. Would appreciate any help from ppl who've done something similar to this 
before.

&#x200B;
```
---

     
 
all -  [ Scaling RAG for Large Datasets: Need Your Insights! ](https://www.reddit.com/r/LangChain/comments/1d3fy9h/scaling_rag_for_large_datasets_need_your_insights/) , 2024-05-30-0911
```
I am currently working on implementing RAG for a specific use case, and I have made good progress with a working example
. So far, I have created embeddings for about 10-15 PDF/HTML files and I am using Qdrant locally (via Docker) to manage 
them.

Now, I am looking to scale up to around 30-40k files and I am unsure if this will work seamlessly. I have already
 implemented metadata filtering, so narrowing down relevant chunks isn't a problem.

My main concern is the memory usage
 of the Docker container. When I check the container, it shows a memory cap of 3.5GB. I am new to Docker, so I am wonder
ing if my vector embeddings size shouldn't exceed this limit. If that's the case, how should I address this problem?

Ha
s anyone here tried using RAG with such a large dataset? If so, did you encounter any issues, particularly with handling
 and storing vector embeddings? Any best practices or tips you could share would be greatly appreciated!
```
---

     
 
all -  [ Extracting Tables in PDFs ](https://www.reddit.com/r/LangChain/comments/1d3fi3d/extracting_tables_in_pdfs/) , 2024-05-30-0911
```
Hi everyone. I am having troubles with extracting Tables in PDFs. I have PDFs of pricing options for different types of 
bricks. Theyre meant for marketing purposes actually, but I want to extract this value into JSON objects using Langchain
.

Take a look:

[Pricing options for bricks inside a PDF](https://preview.redd.it/z05xvep2zd3d1.png?width=1910&format=p
ng&auto=webp&s=1cefd038628e6921ad1a610a6237838ddc892ff7)

I have already tried using [Unstructured.io](http://Unstructur
ed.io) however the JSON it returned wasnt good and it didnt even detect the Tables.

This is the workflow im trying to a
chieve:

1. User loads in PDF of pricing list
2. Document is split per table (I only need the info of the data, nothing 
else. Some documents extend 100 pages)
3. For each Table, an LLM takes the information and creates a meaningful JSON out
 of it
4. I save the JSON inside a db

How would I do this splitting?

Thank you all in advance for your help :)
```
---

     
 
all -  [ Bedrock support in structured_output isnt implemented  ](https://www.reddit.com/r/LangChain/comments/1d3dloo/bedrock_support_in_structured_output_isnt/) , 2024-05-30-0911
```
Hi guys i m trying to use  where my llm point on foundation model hosted in bedrock but getting error :notimplemented ye
t 

      File 'C:\code\dev\rmsology\venv\Lib\site-packages\langchain_core\language_models\base.py', line 210, in with_s
tructured_output
        raise NotImplementedError()
    NotImplementedError
    
    
```
---

     
 
all -  [ Chunking a service ticket ](https://www.reddit.com/r/LangChain/comments/1d3bvxq/chunking_a_service_ticket/) , 2024-05-30-0911
```
Hi,
I need to build a RAG using service ticket data.
One service ticket is a ticket opened by the customer about specifi
ed issue for one product, is composed about:
1) one status
2) related product
3) one list of messages write by who has o
pen the ticket and the service team

This ticket can has from 2 to 20/30 messages.

How chunk strategy we can use? I thi
nk that we use a semantic chunk or fixed chunk we could lose the context.

```
---

     
 
all -  [ Parsing Unstructured Text ](https://www.reddit.com/r/LangChain/comments/1d3a3ee/parsing_unstructured_text/) , 2024-05-30-0911
```
Not sure if this the right place but here goes anyway. I have an excel spreadsheet that provides a weekly report. Each r
ow contains 7 columns. 6 of these are standard fare for a spreadsheet. The last one though is a challenge. The cell cont
ains up to 10,000 characters of free form text that represents shift notes from a range of different employees. Typicall
y, these notes take the form of the example below.

<At 7:10 I inspected the widget file. The widget file was complete a
nd had no errors. After that I called the office to report my findings. Then I had a coffee break. I reviewed the log fi
le for the office server and completed that task by nine AM. There were no other events for the remainder of my shift. 9
:30 a.m. arrived on site. 9:45 a.m. inspected the widget file no anomalies noted. 10:05 a.m. received a status update vi
a phone call with Joe Bloggs. 11:15 a.m. morning coffee break. 11:30 a.m. commenced handover with the afternoon shift. N
ew shift on the job from 12:00 p.m. first half of the shift was uneventful. Aroundabout 145 I received a text message to
 advise that the bearing on the widget machine was due to be replaced on Friday. I put a note into the log for the Frida
y crew. At 3:00 p.m. my shift was over. 3:00 p.m. arrived on site. 3:15 p.m. completed review of bog entry for the day. 
345pm phone call the head office requesting additional post-it notes to be supplied. Nothing much happen for the rest of
 the shift. 6:00 p.m. arrived on site. 9 p.m. arrived on site and  inspected the logs. No further action required.>

I'm
 trying to figure out how to 'read' all these notes and pull out what looks like to be a complete event note or summaris
e, in dot points, the events of the day. As I said, this is a sheet for a week and there are at least 5 of these huge te
xt entries, one for each day. 

I've played around a little with chunking but quickly convinced myself that a chunking s
trategy could lead to events being missed because there is no single fit that I can see.

Anyone got any insight on how 
to handle such problems?
```
---

     
 
all -  [ Intercepting Function Calling and showing the data in UI ](https://www.reddit.com/r/LangChain/comments/1d3852u/intercepting_function_calling_and_showing_the/) , 2024-05-30-0911
```
I'm currently working on a project where I need to integrate GPT-3.5 or GPT-4 into a product carousel, instead of the ty
pical markdown text display. Specifically, I'm looking to intercept the model's function calls and then present the resu
lts in a carousel format on my site.

Has anyone here tackled a similar challenge? I'm interested in any insights or app
roaches you might have used to modify the output format of these models.

  
I'd still want the gpt model to have contex
t of what was fetched from the API i.e. what products, specially their names and product Ids?


```
---

     
 
all -  [ How to Make DataFrame Accessible to LangChain Agent ](https://www.reddit.com/r/LangChain/comments/1d368lr/how_to_make_dataframe_accessible_to_langchain/) , 2024-05-30-0911
```
Hi everyone,

I'm currently working on a LangChain agent and need some help with making a DataFrame (df) accessible to t
he agent. Here’s a quick overview of what I’m trying to achieve:

* The agent has access to several function tools.
* Th
ese tools require a DataFrame (df) as a parameter.
* The agent’s task is to call these tools, passing the data stored in
 a df variable.

**My Question:** Is there a way to ensure that the df variable is accessible to the agent so it can suc
cessfully pass the data to the function tools?

Any guidance or examples would be greatly appreciated!

Thanks in advanc
e!
```
---

     
 
all -  [ The best investment after Nvidia GPUs profit is… ](https://www.reddit.com/r/ChatGPT/comments/1d35f6n/the_best_investment_after_nvidia_gpus_profit_is/) , 2024-05-30-0911
```
I’m a investor of NVIDIA and TSMC since 2024/January (STOP reading here if you don't know what their correlation is with
 OpenAI), when I’ve made a research about which business will make a partnership or support to the OpenAI growth (coz no
 business grow up standalone).

Of course some classical AI programming skills background of mine helped me on that view
.

Now after around 50% profit, I’m searching for the next big support for that increasing demand for LLM... something t
hat only few people can predict.

Recently:  
The xAI (Elon) announced will buy 100k units of Nvidia H100 GPU (this is f
ucking awesome... 5x better than the best GPU your addicted gamer friend ever had)...

Apple stopped the production of i
ts own LLM to start a partnership with OpenAI…

Reddit is making a partnership with OpenAI…

We all know the GPT 4.0 isn
't that dumb 3.0 anymore (that 3 version was merely an word predictor, even for simple math operations... not even close
 to the 4.0 reasoning)

And the GPT-5 will make 4.0 look like a dumb (wtf???)

And I’m wondering where is it all going t
o help my investment profit for next 3 years.  
Any ideas to share?

* Maybe some effort on the Reinforcement Learning A
I?
* Better computer vision hardware components?
* Build Custom AI Agents for individuals and businesses?
* Better RAG v
ector databases indexing?
* Realistic voice cloning?
* Neuralink-LLM integration?
* No/Low-code LangChain tool?

DM for 
thoughts partnership about profit on that field.   
Just curious? get out.
```
---

     
 
all -  [ How to show what agent is currently doing to user in streamlit? ](https://www.reddit.com/r/LangChain/comments/1d34xfq/how_to_show_what_agent_is_currently_doing_to_user/) , 2024-05-30-0911
```
Like I want to show, executing agent chain, executing sql genery, generating response like it prints in termial. Is ther
 any way to do this?
```
---

     
 
all -  [ Chat RTX not working
 ](https://www.reddit.com/r/techsupport/comments/1d34tvm/chat_rtx_not_working/) , 2024-05-30-0911
```
i downloaded chat RTX successfully , but it wont run , I get the error of

httpx.ConnectError: \[SSL: CERTIFICATE\_VERIF
Y\_FAILED\] certificate verify failed: unable to get local issuer certificate (\_ssl.c:1007)

and here what does it look
 like in the web:







and here what look like in app cmd







# This site can’t be reached

[**127.0.0.1**](http://
127.0.0.1) refused to connect.

Try:

* Checking the connection
* [Checking the proxy and the firewall](chrome-error://c
hromewebdata/#buttons)

ERR\_CONNECTION\_REFUSEDReloadHide detailsCheck your Internet connectionCheck any cables and reb
oot any routers, modems, or other network devices you may be using.Allow Chrome to access the network in your firewall o
r antivirus settings.If it is already listed as a program allowed to access the network, try removing it from the list a
nd adding it again.If you use a proxy server…Check your proxy settings or contact your network administrator to make sur
e the proxy server is working. If you don't believe you should be using a proxy server: Go to the Chrome menu > Settings
 > Show advanced settings… > Change proxy settings… > LAN Settings and deselect 'Use a proxy server for your LAN'.This s
ite can’t be reached

[**127.0.0.1**](http://127.0.0.1) refused to connect.

Try:

* Checking the connection
* [Checking
 the proxy and the firewall](chrome-error://chromewebdata/#buttons)







hope someone can help, Thanks





Environmen
t path found: C:\\Users\\User\\AppData\\Local\\NVIDIA\\ChatRTX\\env\_nvd\_rag

Privileges of original process: \['SeShut
downPrivilege', 'SeChangeNotifyPrivilege', 'SeUndockPrivilege', 'SeIncreaseWorkingSetPrivilege', 'SeTimeZonePrivilege'\]


Privileges of restricted app token: \['SeChangeNotifyPrivilege'\]

Process Id =  17940

Environment path found: C:\\Us
ers\\User\\AppData\\Local\\NVIDIA\\ChatRTX\\env\_nvd\_rag

App running with config

 {

'models': {

'supported': \[

{


'name': 'Mistral 7B int4',

'id': 'mistral\_model',

'ngc\_model\_name': 'nvidia/llama/mistral-7b-int4-chat:1.2',

'is\
_downloaded\_required': true,

'downloaded': true,

'is\_installation\_required': true,

'setup\_finished': true,

'min\
_gpu\_memory': 8,

'should\_show\_in\_UI': true,

'prerequisite': {

'checkpoints\_files': \[

'config.json',

'rank0.sa
fetensors',

'license.txt'

\],

'tokenizer\_ngc\_dir': 'mistral7b\_hf\_tokenizer',

'tokenizer\_files': {

'config': 'c
onfig.json',

'tokenizer': 'tokenizer.json',

'model': 'tokenizer.model',

'tokenizer\_config': 'tokenizer\_config.json'


},

'checkpoints\_local\_dir': 'model\_checkpoints',

'tokenizer\_local\_dir': 'tokenizer',

'engine\_build\_command':
 'trtllm-build --checkpoint\_dir %checkpoints\_local\_dir% --output\_dir %engine\_dir% --gpt\_attention\_plugin float16 
--gemm\_plugin float16 --max\_batch\_size 1 --max\_input\_len 7168 --max\_output\_len 1024 --context\_fmha=enable --page
d\_kv\_cache=disable --remove\_input\_padding=disable',

'engine\_dir': 'engine'

},

'metadata': {

'engine': 'rank0.en
gine',

'max\_new\_tokens': 1024,

'max\_input\_token': 7168,

'temperature': 0.1,

'prompt\_template': 'Default'

},

'
model\_info': 'The Mistral-7B is a instruct fine-tuned text generation model | <a href='https ://github.c om/mistralai/m
istral-src/blob/main/LICENSE'> License </a>',

'model\_license': '<a href='https ://github. com/mistralai/mistral-src/bl
ob/main/LICENSE'> License </a>',

'model\_size': '4GB'

},

{

'name': 'Llama2 13B int4',

'id': 'llaam2\_model',

'ngc\
_model\_name': 'nvidia/llama/llama2-13b:1.5',

'is\_downloaded\_required': true,

'downloaded': false,

'is\_installatio
n\_required': true,

'setup\_finished': false,

'min\_gpu\_memory': 16,

'should\_show\_in\_UI': false,

'prerequisite':
 {

'checkpoints\_files': \[

'config.json',

'rank0.safetensors',

'README.txt',

'license.txt'

\],

'tokenizer\_ngc\_
dir': 'llama13\_hf\_tokenizer',

'tokenizer\_files': {

'config': 'config.json',

'tokenizer': 'tokenizer.json',

'model
': 'tokenizer.model',

'tokenizer\_config': 'tokenizer\_config.json'

},

'checkpoints\_local\_dir': 'model\_checkpoints
',

'tokenizer\_local\_dir': 'tokenizer',

'engine\_build\_command': 'trtllm-build --checkpoint\_dir %checkpoints\_local
\_dir% --output\_dir %engine\_dir% --gpt\_attention\_plugin float16 --gemm\_plugin float16 --max\_batch\_size 1 --max\_i
nput\_len 3072 --max\_output\_len 1024 --context\_fmha=enable --paged\_kv\_cache=disable --remove\_input\_padding=disabl
e',

'engine\_dir': 'engine'

},

'metadata': {

'engine': 'rank0.engine',

'max\_new\_tokens': 1024,

'max\_input\_toke
n': 7168,

'temperature': 0.1,

'prompt\_template': 'Default'

},

'model\_info': 'LlaMa 2 is a large language AI model 
capable of generating text and code in response to prompts | <a href='https ://ai.meta.c om/llama/license/'> License </a
>',

'model\_license': '<a href='https ://ai.meta.com /llama/license/'> License </a>',

'model\_size': '6.8GB' 

},

{


'name': 'ChatGLM 3 6B int4 (Supports Chinese)',

'id': 'chatglm3\_model',

'ngc\_model\_name': 'nvidia/chatglm3-6b-chat-
int4:1.0',

'is\_downloaded\_required': true,

'downloaded': false,

'is\_installation\_required': true,

'setup\_finish
ed': false,

'min\_gpu\_memory': 8,

'should\_show\_in\_UI': true,

'prerequisite': {

'checkpoints\_files': \[

'config
.json',

'rank0.safetensors',

'license.txt'

\],

'tokenizer\_ngc\_dir': 'Tokenizer',

'tokenizer\_files': {

'config':
 'config.json',

'model': 'tokenizer.model',

'tokenizer\_config': 'tokenizer\_config.json'

},

'checkpoints\_local\_di
r': 'model\_checkpoints',

'tokenizer\_local\_dir': 'tokenizer',

'engine\_build\_command': 'trtllm-build --checkpoint\_
dir %checkpoints\_local\_dir% --output\_dir %engine\_dir% --gemm\_plugin float16 --max\_batch\_size 1 --max\_input\_len 
7168 --max\_output\_len 1024',

'engine\_dir': 'engine'

},

'metadata': {

'engine': 'rank0.engine',

'max\_new\_tokens
': 1024,

'max\_input\_token': 7168,

'temperature': 0.1

},

'model\_info': 'ChatGLM-6B is an open bilingual language m
odel based on General Language Model framework, with 6.2 billion parameters | <a href= 'https ://huggingface.co/THUDM/ch
atglm3-6b/blob/main/MODEL\_LICENSE'> License </a>',

'model\_license': '<a href= 'https ://huggingface.co/THUDM/chatglm3
-6b/blob/main/MODEL\_LICENSE'> License </a>',

'model\_size': '3.8GB'

},

{

'name': 'Gemma 7B int4',

'id': 'Gemma\_mo
del',

'ngc\_model\_name': 'nvidia/llama/gemma-7b-int4-rtx:1.1',

'is\_downloaded\_required': true,

'downloaded': false
,

'is\_installation\_required': true,

'setup\_finished': false,

'min\_gpu\_memory': 16,

'should\_show\_in\_UI': fals
e,

'prerequisite': {

'checkpoints\_files': \[

'config.json',

'rank0.safetensors',

'Prohibited\_use\_policy.txt',

'
license.txt',

'Notice.txt'

\],

'tokenizer\_ngc\_dir': 'Gemma7b\_hf\_tokenizer',

'tokenizer\_files': {

'vocab\_file'
: 'tmp\_vocab.model'

},

'checkpoints\_local\_dir': 'model\_checkpoints',

'vocab\_local\_dir': 'tokenizer',

'engine\_
build\_command': 'trtllm-build --checkpoint\_dir %checkpoints\_local\_dir% --gemm\_plugin float16 --gpt\_attention\_plug
in float16 --max\_batch\_size 1 --max\_input\_len 4096 --max\_output\_len 1024 --output\_dir %engine\_dir%',

'engine\_d
ir': 'engine'

},

'metadata': {

'engine': 'rank0.engine',

'max\_new\_tokens': 1024,

'max\_input\_token': 7168,

'tem
perature': 0.1

},

'model\_info': 'Gemma-7B is a 7B parameter model from Gemma family of models from Google | <a href= 
'https ://ai.google.dev/gemma/terms'> License </a>',

'model\_license': '<a href= 'https: //ai.google.dev/gemma/terms'> 
License </a>',

'model\_size': '6.6GB'

},

{

'name': 'CLIP',

'id': 'clip\_model',

'hf\_model\_name': 'openai/clip-vi
t-large-patch14-336',

'is\_downloaded\_required': true,

'downloaded': false,

'download\_link': 'https ://huggingface.
co/openai/clip-vit-large-patch14-336/resolve/main',

'is\_installation\_required': false,

'setup\_finished': false,

'm
in\_gpu\_memory': 8,

'should\_show\_in\_UI': true,

'prerequisite': {

'checkpoints\_files': \[

'README.md',

'config.
json',

'merges.txt',

'preprocessor\_config.json',

'pytorch\_model.bin',

'special\_tokens\_map.json',

'tokenizer.jso
n',

'tokenizer\_config.json',

'vocab.json'

\],

'checkpoints\_local\_dir': 'clip\_model'

},

'metadata': {},

'model
\_info': 'CLIP is a multi-modal vision and language model used for image-text similarity and for zero-shot image classif
ication | <a href='https ://github.c om/openai/CLIP/blob/main/LICENSE'> License </a>',

'model\_license': '<a href='http
s ://github.co m/openai/CLIP/blob/main/LICENSE'> License </a>',

'model\_size': '1.5GB'

}

\],

'selected': 'Mistral 7B
 int4',

'enable\_asr': true,

'supported\_asr': \[

{

'name': 'Whisper Medium Int8',

'installed': true,

'metadata': 
{

'encoder\_engine': 'whisper\_encoder\_float16\_tp1\_rank0.engine',

'decoder\_engine': 'whisper\_decoder\_float16\_tp
1\_rank0.engine',

'model\_path': 'model\\\\whisper\\\\whisper\_medium\_int8\_engine',

'assets\_path': 'model\\\\whispe
r\\\\whisper\_assets'

}

}

\]

},

'sample\_questions': \[

{

'query': 'How does NVIDIA ACE generate emotional respon
ses?'

},

{

'query': 'What is Portal prelude RTX?'

},

{

'query': 'What is important about Half Life 2 RTX?'

},

{


'query': 'When is the launch date for Ratchet & Clank: Rift Apart on PC?'

}

\],

'sample\_questions\_chinese': \[

{


'query': 'NVIDIA ACE是如何生成富有情感的回复的？'

},

{

'query': '传送门：序曲是什么？'

},

{

'query': '半条命 2 RTX版有什么重要意义？'

},

{

'query'
: '瑞奇与叮当：时空跳转何时会在PC平台发布？'

}

\],

'sample\_questions\_clip': \[

{

'query': 'Pictures of bicycles'

},

{

'query': 'P
ictures of toys'

},

{

'query': 'Pictures of dinosaurs'

},

{

'query': 'Pictures of computer'

}

\],

'dataset': {


'sources': \[

'directory',

'nodataset'

\],

'selected': 'directory',

'path': 'dataset',

'path\_chinese': 'chinese\
_dataset',

'path\_clip': 'images\_dataset',

'isRelative': true

},

'strings': {

'directory': 'Folder Path',

'nodata
set': 'AI model default'

}

}

\[TensorRT-LLM\] TensorRT-LLM version: 0.9.0

Privileges of app process: \['SeChangeNoti
fyPrivilege'\]

C:\\Users\\User\\AppData\\Local\\NVIDIA\\ChatRTX\\env\_nvd\_rag\\lib\\site-packages\\langchain\\chat\_mo
dels\\\_\_init\_\_.py:31: LangChainDeprecationWarning: Importing chat models from langchain is deprecated. Importing fro
m langchain will no longer be supported as of langchain==0.2.0. Please import from langchain-community instead:



\`fro
m langchain\_community.chat\_models import ChatAnyscale\`.



To install langchain-community run \`pip install -U langch
ain-community\`.

  warnings.warn(

C:\\Users\\User\\AppData\\Local\\NVIDIA\\ChatRTX\\env\_nvd\_rag\\lib\\site-packages\
\langchain\\chat\_models\\\_\_init\_\_.py:31: LangChainDeprecationWarning: Importing chat models from langchain is depre
cated. Importing from langchain will no longer be supported as of langchain==0.2.0. Please import from langchain-communi
ty instead:



\`from langchain\_community.chat\_models import ChatOpenAI\`.



To install langchain-community run \`pip
 install -U langchain-community\`.

  warnings.warn(

C:\\Users\\User\\AppData\\Local\\NVIDIA\\ChatRTX\\env\_nvd\_rag\\l
ib\\site-packages\\langchain\\embeddings\\\_\_init\_\_.py:29: LangChainDeprecationWarning: Importing embeddings from lan
gchain is deprecated. Importing from langchain will no longer be supported as of langchain==0.2.0. Please import from la
ngchain-community instead:



\`from langchain\_community.embeddings import HuggingFaceBgeEmbeddings\`.



To install la
ngchain-community run \`pip install -U langchain-community\`.

  warnings.warn(

C:\\Users\\User\\AppData\\Local\\NVIDIA
\\ChatRTX\\env\_nvd\_rag\\lib\\site-packages\\langchain\\embeddings\\\_\_init\_\_.py:29: LangChainDeprecationWarning: Im
porting embeddings from langchain is deprecated. Importing from langchain will no longer be supported as of langchain==0
.2.0. Please import from langchain-community instead:



\`from langchain\_community.embeddings import HuggingFaceEmbedd
ings\`.



To install langchain-community run \`pip install -U langchain-community\`.

  warnings.warn(

C:\\Users\\User
\\AppData\\Local\\NVIDIA\\ChatRTX\\env\_nvd\_rag\\lib\\site-packages\\langchain\\llms\\\_\_init\_\_.py:548: LangChainDep
recationWarning: Importing LLMs from langchain is deprecated. Importing from langchain will no longer be supported as of
 langchain==0.2.0. Please import from langchain-community instead:



\`from langchain\_community.llms import AI21\`.




To install langchain-community run \`pip install -U langchain-community\`.

  warnings.warn(

C:\\Users\\User\\AppData\
\Local\\NVIDIA\\ChatRTX\\env\_nvd\_rag\\lib\\site-packages\\langchain\\llms\\\_\_init\_\_.py:548: LangChainDeprecationWa
rning: Importing LLMs from langchain is deprecated. Importing from langchain will no longer be supported as of langchain
==0.2.0. Please import from langchain-community instead:



\`from langchain\_community.llms import Cohere\`.



To inst
all langchain-community run \`pip install -U langchain-community\`.

  warnings.warn(

C:\\Users\\User\\AppData\\Local\\
NVIDIA\\ChatRTX\\env\_nvd\_rag\\lib\\site-packages\\langchain\\llms\\\_\_init\_\_.py:548: LangChainDeprecationWarning: I
mporting LLMs from langchain is deprecated. Importing from langchain will no longer be supported as of langchain==0.2.0.
 Please import from langchain-community instead:



\`from langchain\_community.llms import FakeListLLM\`.



To install
 langchain-community run \`pip install -U langchain-community\`.

  warnings.warn(

C:\\Users\\User\\AppData\\Local\\NVI
DIA\\ChatRTX\\env\_nvd\_rag\\lib\\site-packages\\langchain\\llms\\\_\_init\_\_.py:548: LangChainDeprecationWarning: Impo
rting LLMs from langchain is deprecated. Importing from langchain will no longer be supported as of langchain==0.2.0. Pl
ease import from langchain-community instead:



\`from langchain\_community.llms import OpenAI\`.



To install langcha
in-community run \`pip install -U langchain-community\`.

  warnings.warn(

Using the persisted value form dataset\_vect
or\_embedding

Open HTTP s://127.0.0.1:48710?cookie=48e206cf-1b47-40a3-a517-ff7f0223f1ed&\_\_theme=dark in browser to st
art ChatRTX

Running on local URL:  HTTP s://127.0.0.1:48710

Traceback (most recent call last):

  File 'C:\\Users\\Use
r\\AppData\\Local\\NVIDIA\\ChatRTX\\env\_nvd\_rag\\lib\\site-packages\\httpx\\\_transports\\default.py', line 69, in map
\_httpcore\_exceptions

yield

  File 'C:\\Users\\User\\AppData\\Local\\NVIDIA\\ChatRTX\\env\_nvd\_rag\\lib\\site-packag
es\\httpx\\\_transports\\default.py', line 233, in handle\_request

resp = self.\_pool.handle\_request(req)

  File 'C:\
\Users\\User\\AppData\\Local\\NVIDIA\\ChatRTX\\env\_nvd\_rag\\lib\\site-packages\\httpcore\\\_sync\\connection\_pool.py'
, line 216, in handle\_request

raise exc from None

  File 'C:\\Users\\User\\AppData\\Local\\NVIDIA\\ChatRTX\\env\_nvd\
_rag\\lib\\site-packages\\httpcore\\\_sync\\connection\_pool.py', line 196, in handle\_request

response = connection.ha
ndle\_request(

  File 'C:\\Users\\User\\AppData\\Local\\NVIDIA\\ChatRTX\\env\_nvd\_rag\\lib\\site-packages\\httpcore\\\
_sync\\connection.py', line 99, in handle\_request

raise exc

  File 'C:\\Users\\User\\AppData\\Local\\NVIDIA\\ChatRTX\
\env\_nvd\_rag\\lib\\site-packages\\httpcore\\\_sync\\connection.py', line 76, in handle\_request

stream = self.\_conne
ct(request)

  File 'C:\\Users\\User\\AppData\\Local\\NVIDIA\\ChatRTX\\env\_nvd\_rag\\lib\\site-packages\\httpcore\\\_sy
nc\\connection.py', line 154, in \_connect

stream = stream.start\_tls(\*\*kwargs)

  File 'C:\\Users\\User\\AppData\\Lo
cal\\NVIDIA\\ChatRTX\\env\_nvd\_rag\\lib\\site-packages\\httpcore\\\_backends\\sync.py', line 152, in start\_tls

with m
ap\_exceptions(exc\_map):

  File 'C:\\Users\\User\\AppData\\Local\\NVIDIA\\ChatRTX\\env\_nvd\_rag\\lib\\contextlib.py',
 line 153, in \_\_exit\_\_

self.gen.throw(typ, value, traceback)

  File 'C:\\Users\\User\\AppData\\Local\\NVIDIA\\Chat
RTX\\env\_nvd\_rag\\lib\\site-packages\\httpcore\\\_exceptions.py', line 14, in map\_exceptions

raise to\_exc(exc) from
 exc

httpcore.ConnectError: \[SSL: CERTIFICATE\_VERIFY\_FAILED\] certificate verify failed: unable to get local issuer 
certificate (\_ssl.c:1007)



The above exception was the direct cause of the following exception:



Traceback (most re
cent call last):

  File 'D:\\chatrtx\\CRTX\\RAG\\trt-llm-rag-windows-ChatRTX\_0.3\\app.py', line 706, in <module>

inte
rface.render()

  File 'D:\\chatrtx\\CRTX\\RAG\\trt-llm-rag-windows-ChatRTX\_0.3\\ui\\user\_interface.py', line 426, in 
render

interface.launch(

  File 'C:\\Users\\User\\AppData\\Local\\NVIDIA\\ChatRTX\\env\_nvd\_rag\\lib\\site-packages\\
gradio\\blocks.py', line 2209, in launch

httpx.get(

  File 'C:\\Users\\User\\AppData\\Local\\NVIDIA\\ChatRTX\\env\_nvd
\_rag\\lib\\site-packages\\httpx\\\_api.py', line 198, in get

return request(

  File 'C:\\Users\\User\\AppData\\Local\
\NVIDIA\\ChatRTX\\env\_nvd\_rag\\lib\\site-packages\\httpx\\\_api.py', line 106, in request

return client.request(

  F
ile 'C:\\Users\\User\\AppData\\Local\\NVIDIA\\ChatRTX\\env\_nvd\_rag\\lib\\site-packages\\httpx\\\_client.py', line 827,
 in request

return self.send(request, auth=auth, follow\_redirects=follow\_redirects)

  File 'C:\\Users\\User\\AppData
\\Local\\NVIDIA\\ChatRTX\\env\_nvd\_rag\\lib\\site-packages\\httpx\\\_client.py', line 914, in send

response = self.\_s
end\_handling\_auth(

  File 'C:\\Users\\User\\AppData\\Local\\NVIDIA\\ChatRTX\\env\_nvd\_rag\\lib\\site-packages\\httpx
\\\_client.py', line 942, in \_send\_handling\_auth

response = self.\_send\_handling\_redirects(

  File 'C:\\Users\\Us
er\\AppData\\Local\\NVIDIA\\ChatRTX\\env\_nvd\_rag\\lib\\site-packages\\httpx\\\_client.py', line 979, in \_send\_handli
ng\_redirects

response = self.\_send\_single\_request(request)

  File 'C:\\Users\\User\\AppData\\Local\\NVIDIA\\ChatRT
X\\env\_nvd\_rag\\lib\\site-packages\\httpx\\\_client.py', line 1015, in \_send\_single\_request

response = transport.h
andle\_request(request)

  File 'C:\\Users\\User\\AppData\\Local\\NVIDIA\\ChatRTX\\env\_nvd\_rag\\lib\\site-packages\\ht
tpx\\\_transports\\default.py', line 232, in handle\_request

with map\_httpcore\_exceptions():

  File 'C:\\Users\\User
\\AppData\\Local\\NVIDIA\\ChatRTX\\env\_nvd\_rag\\lib\\contextlib.py', line 153, in \_\_exit\_\_

self.gen.throw(typ, va
lue, traceback)

  File 'C:\\Users\\User\\AppData\\Local\\NVIDIA\\ChatRTX\\env\_nvd\_rag\\lib\\site-packages\\httpx\\\_t
ransports\\default.py', line 86, in map\_httpcore\_exceptions

raise mapped\_exc(message) from exc

httpx.ConnectError: 
\[SSL: CERTIFICATE\_VERIFY\_FAILED\] certificate verify failed: unable to get local issuer certificate (\_ssl.c:1007)

P
ress any key to continue . . .


```
---

     
 
all -  [ 10k Story to 60k Novel? ](https://www.reddit.com/r/LangChain/comments/1d34r3h/10k_story_to_60k_novel/) , 2024-05-30-0911
```
I want to use AI to expand my 10,000 word story into a 60k word novel. Obviously Chat GPT doesn't offer enough tokens to
 do this, so I'm wondering, can Lang Chain combine with Chat GPT to accomplish this? I haven't used Lang Chain yet to un
derstand its capabilities yet. 

If it is possible for this to work, how complicated would it be to do?
```
---

     
 
all -  [ Kernel Memory | Deploy with a cheap infrastructure ](https://www.reddit.com/r/LangChain/comments/1d32vkw/kernel_memory_deploy_with_a_cheap_infrastructure/) , 2024-05-30-0911
```
Hello, how are you?

I am deploying a Kernel Memory service in production and wanted to get your opinion on my decision.
 Is it more cost-effective? The idea is to make it an async REST API.

- Service host: EC2 - AWS.
* Queue service: Rabbi
tMQ on the EC2 machine hosting the Kernel Memory web service.
* Storage & Vector Search: MongoDB Atlas.
* The embedding 
and LLM models used will be from OpenAI.
```
---

     
 
all -  [ Introducing MyScale Telemetry - Your Open-Source Alternative to LangSmith! ](https://www.reddit.com/r/LangChain/comments/1d2yjqe/introducing_myscale_telemetry_your_opensource/) , 2024-05-30-0911
```
In a world where LLM applications are pushing the boundaries of what's possible, observability is not just a nice-to-hav
e—it's essential for production-grade applications! Ensuring robust performance and reliability is a must, and that's ex
actly what MyScale Telemetry delivers.  
  
Say hello to the open-source alternative to LangSmith! [MyScale Telemetry](h
ttps://myscale.com/blog/myscale-telemetry-llm-app-observability/) is here to revolutionize how you trace and evaluate yo
ur LLM applications. With seamless integration with LangChain Callbacks, it's the perfect tool to diagnose issues, optim
ize performance, and understand model behavior—all with the power of open-source!  
  
MyScale Team's Commitment to Open
 Source: Our passion for contributing to the community is unwavering, and with MyScale Telemetry, we're excited to empow
er developers with the tools they need to innovate and excel.  
  
Join us on this journey to enhance your LLM applicati
ons with MyScale Telemetry. Let's shape the future of AI together, one trace at a time! 
```
---

     
 
all -  [ GPT4AllEmbeddings doesn’t work offline no way to pass a model path (any workarounds?) ](https://www.reddit.com/r/LangChain/comments/1d2xqz3/gpt4allembeddings_doesnt_work_offline_no_way_to/) , 2024-05-30-0911
```
GPT4AllEmbeddings modify model path

I'd like to modify the model path using GPT4AllEmbeddings and use a model I already
 downloading from the browser (the all-MiniLM-L6-v2-f16.gguf model, the same that GPT4AllEmbeddings downloads by default
).

I need it to create RAG chatbot completely offline.

The langchain documentation chatbot suggests me to use:

>from 
langchain\_community.embeddings **import** GPT4AllEmbeddings  
model\_path = '/path/to/your/model.bin'  
gpt4all\_embd =
 GPT4AllEmbeddings(model=model\_path)

I tried it but it does not work. It completely ignores the model path.

Is there 
something I'm missing?
```
---

     
 
all -  [ Ragatouille: A guide to get started with Retrieval-Augmented Generation (RAG) with LangChain ! ](https://www.reddit.com/r/LangChain/comments/1d2xedu/ragatouille_a_guide_to_get_started_with/) , 2024-05-30-0911
```
🚀 Exciting News! I just published a blog, Ragatouille– A guide to get started with Retrieval-Augmented Generation (RAG) 
with [LangChain](https://www.linkedin.com/company/langchain/) !

Based on Langchain's RAG from scratch series, in this c
omprehensive guide, we break down the RAG process and take you through each step to enhance and optimize your system. He
re’s a sneak peek of what you'll learn:

📌 Introduction to RAG: Understand the basics of the RAG pipeline and how it com
bines retrieval-based systems with generative models.

🔍 Query Transformation: Learn how to refine user queries for bett
er comprehension and accurate responses.

📚 Hypothetical Document Embeddings: Discover techniques for generating vector 
representations of potential documents to assess relevance.

🛤️ Routing Mechanisms: Implement intelligent routing to dyn
amically select the best data sources for your queries.

📝 Executable Queries: Master the art of translating user questi
ons into executable queries.

📂 Effective Indexing: Explore indexing strategies to enhance retrieval efficiency.

🔄 Adva
nced Retrieval Techniques: Dive into Self-RAG, Adaptive RAG, and CRAG for tailored retrieval approaches.

💡 Generation P
hase: Ensure coherent and accurate responses using the retrieved information.

🏥 Practical Application: Apply everything
 you've learned to build a sophisticated hospital management system using LangChain, LangGraph, and Neo4j.

👉 Check out:
 [https://www.sakunaharinda.xyz/ragatouille-book](https://www.sakunaharinda.xyz/ragatouille-book)

⬆️ I will be updating
 the blog soon with RAG evaluation using RAGAS and Langsmith !!! Please let me know what you guys want to appear in this
 blog, which will help fellow RAG enthusiasts 💭 I appreciate your constructive feedback and contributions !!
```
---

     
 
all -  [ Dockerize langchain/langserve applications ](https://www.reddit.com/r/LangChain/comments/1d2rq1k/dockerize_langchainlangserve_applications/) , 2024-05-30-0911
```
This is a poetry plugin to generate Dockerfile and images automatically.

This is a perfect choice if you built the Lang
chain application and you’re looking for to distribute is as microservice in the cloud. 


This project lets you generat
e a docker image or just a Dockerfile for your poetry application without manual setup

It is meant for production image
s.

[https://github.com/nicoloboschi/poetry-dockerize-plugin](https://github.com/nicoloboschi/poetry-dockerize-plugin)


[https://pypi.org/project/poetry-dockerize-plugin/](https://pypi.org/project/poetry-dockerize-plugin/)



Get started wi
th

    poetry self add poetry-dockerize-plugin@latest

This command generates a production-ready, optimized python imag
e:

    poetry dockerize

 or to generate a Dockerfile

    poetry dockerize --generate


```
---

     
 
all -  [ How to make RAG retrieve_documents chain make faster? ](https://www.reddit.com/r/LangChain/comments/1d2ooua/how_to_make_rag_retrieve_documents_chain_make/) , 2024-05-30-0911
```
Hi,

We created a chatbot with Llama2-7b-chat, RAG architecture using LangChain, Qdrant VectorDB, and for web side Djang
o. Everything works well. Additionally, our system works locally. Now the only problem is the time we get the answer. So
metimes it takes 15 seconds to return the answer from the RAG chain and it's too bad. After monitoring with LangSmith we
 saw that retrieve\_documents takes most of the run time.

Our Qdrant VectorDB collections distance type Manhattan and b
inary quantization. The embedding model is sentence-transformers/all-MiniLM-L6-v2 so the size is 384.  Also we clear the
 cache everytime. Here is the chains code and the invoke , (We write two system prompt for holding the chat history.)

 
   class RAG():
    
        def _init_(self):
            self.embed_model_id = 'sentence-transformers/all-MiniLM-L6-v2
'
            self.initializeEmbeddingModel(device)        
    
            self.model_id = 'meta-llama/Llama-2-13b-cha
t-hf'
            self.hf_auth = 'token' 
            self.initializeLLM()
    
            self.data_collection_name = 
'collection_name'
            self.db_url = 'qdrant-docker-port'
            self.initializeDBclient()
            self.
initializesearchDB()
    
            self.LLMpipeline()
            self.configSystemPrompt()
            self.RAGpipel
ine()
    
        def initializeEmbeddingModel(device):
    pass
        
        def initializeLLM(self):
    
       
     bnb_config = transformers.BitsAndBytesConfig(
                load_in_4bit=True,
                bnb_4bit_quant_typ
e='nf4',
                bnb_4bit_use_double_quant=True,
                bnb_4bit_compute_dtype=bfloat16
            )
 
           model_config = transformers.AutoConfig.from_pretrained(
                self.model_id,
                token=
self.hf_auth
            )
            self.LLMmodel = transformers.AutoModelForCausalLM.from_pretrained(
              
  self.model_id,
                trust_remote_code=True,
                config=model_config,
                quantizati
on_config=bnb_config,
                device_map='auto',
                token=self.hf_auth 
    
            )
        
    self.LLMmodel.eval()
    
        def initializeDBclient(self):
            pass
            
        def initialize
searchDB(self):
            # self.searchDB creation  
            pass      
    
        def LLMpipeline(self):
      
      
            tokenizer = transformers.AutoTokenizer.from_pretrained(
                        self.model_id,
      
                  token=self.hf_auth
                    )
            pipeline = transformers.pipeline(
               
         model=self.LLMmodel, tokenizer=tokenizer,
                        return_full_text=True,  
                    
    task='text-generation',
    
                        temperature=0.0,  
                        max_new_tokens=512, 
 
                        repetition_penalty=1.1,
                        do_sample=False
                    )
        
    self.llm = HuggingFacePipeline(pipeline=pipeline)
            
        def configSystemPrompt(self):
            
  
          # sohbet geçmişi için alt prompt ve genel system promptu tanımlıyoruz
    
            contextualize_q_system_
prompt = '''prompt'''
            self.contextualize_q_prompt = ChatPromptTemplate.from_messages(
                [
    
                ('system', contextualize_q_system_prompt),
                    MessagesPlaceholder('chat_history'),
    
                ('human', '{input}'),
                ]
            )
            qa_system_prompt = '''prompt/
        
    {context}'''
    
            self.qa_prompt = ChatPromptTemplate.from_messages(
                [
                 
   ('system', qa_system_prompt),
                    MessagesPlaceholder('chat_history'),
                    ('human', 
'{input}'),
                ]
            )
    
        def RAGpipeline(self):
            
            retriever = sel
f.searchDB.as_retriever(search_kwargs={'k':6 })
    
            history_aware_retriever = create_history_aware_retrieve
r(
                self.llm, retriever, self.contextualize_q_prompt
            )
    
            question_answer_chain
 = create_stuff_documents_chain(self.llm, self.qa_prompt)
    
            self.rag_chain = create_retrieval_chain(histo
ry_aware_retriever, question_answer_chain)
       
        def ragQA(self, question, history):
            ai_msg = self
.rag_chain.invoke({'input': question, 'chat_history': history})  
              
            return ai_msg
    
        
def clear_cache(self):
            torch.cuda.empty_cache()
            gc.collect()

LangSmith monitor result is here,


retrieval\_chain 15.71s

* retrieve\_documents 11.66s
   * HuggingFacePipeline gpt2 11.61s
   * Retriever 0.04s
* stuff
\_documents\_chain 3.96s
   * format\_inputs 0.01s
      * format\_docs 0.00s
   * HuggingFacePipeline 3.94s

So the pro
blem is mostly retrieve\_documents.  What should we do to make the system faster?

Edit:

GPU: RTX A4000, 16GB

RAM: 32 
GB

CPU: Intel® Xeon(R) W-2235 CPU @ 3.80GHz × 12

OS: Ubuntu 22.04.4 LTS
```
---

     
 
all -  [ How does an LLM orchestrator decide which agent to use in a multi-agent system? ](https://www.reddit.com/r/LangChain/comments/1d2omoe/how_does_an_llm_orchestrator_decide_which_agent/) , 2024-05-30-0911
```
Hello everyone,

I'm exploring multi-agent systems and am curious about the role of an orchestrator in managing tasks am
ong specialized agents. For instance, imagine a scenario where there are four agents, each designed to perform one of th
e basic mathematical operations: addition, subtraction, multiplication, and division.

If the orchestrator receives a qu
estion like 'How much is 4 + 4?', how does it determine which agent to send the query to? What logic or algorithms might
 it use to parse the question and delegate the task appropriately?

Additionally, if anyone could provide insights or re
sources into how such systems are generally designed or any examples of such orchestrators in action, it would be greatl
y appreciated.

Thanks in advance for your help and sharing your knowledge!


```
---

     
 
all -  [ Shopify all in on Promptfoo ](https://i.redd.it/qgg45w3d073d1.jpeg) , 2024-05-30-0911
```
I am a big fan of Promptfoo aswell. 
```
---

     
 
all -  [ [For Hire] Programmer/Web Developer/IT Consultant (Python, PHP, AI, etc.) ](https://www.reddit.com/r/forhire/comments/1d2n4lx/for_hire_programmerweb_developerit_consultant/) , 2024-05-30-0911
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

     
 
all -  [ Async streaming makes everything else harder ](https://www.reddit.com/r/LangChain/comments/1d2li6s/async_streaming_makes_everything_else_harder/) , 2024-05-30-0911
```
I find trying to do streaming makes everything else harder to do. Especially the checkpointer for message history.

This
 is my setup:

            class GraphState(TypedDict):
                question: str
                messages: Annotate
d[list, add_messages]
                documents: List[str]
    
            workflow = StateGraph(GraphState)
          
  workflow.add_node('retrieve', retrieve)
            workflow.add_node('generate', generate)
            workflow.set_e
ntry_point('retrieve')
            workflow.add_edge('retrieve', 'generate')
            workflow.add_edge('generate', E
ND)
    
            pool = AsyncConnectionPool(
                conninfo='postgresql://...',
                max_size=2
0,
            )
    
            # PostgresSaver.create_tables(pool)
    
            checkpoint = PostgresSaver( #pack
age is langchain_postgres==0.0.3
                serializer=PickleCheckpointSerializer(),
                async_connecti
on=pool,
            )
    
            app = workflow.compile(checkpointer=checkpoint)
    
            config = {
    
                'configurable': {
                            'thread_id': '1223'
                        }
            
        }
    
            async for event in app.astream_events({'messages': [('user', user_content)], 'question':     
  user_content}, config, version='v1'):
                    state = app.get_state(config) #this is the line that errors

                    try:
                        kind = event['event']
                    except:
                     
   kind = None
                    if kind and kind == 'on_chat_model_stream':
                        content = event['
data']['chunk'].content
                        if content:
                            message = {'content': content}
 
                           await self.send(text_data=json.dumps(message))

Specifically, I want to be able to use get\_s
tate() to get the document references from an answer (which is in the GraphState), as well as to do conditional interrup
t like in [this ](https://langchain-ai.github.io/langgraph/tutorials/customer-support/customer-support/#state-assistant)
Customer Service LangGraph example (which requires get\_state()).

In generral, is there a better way to handle the chec
kpointer while streaming the response?
```
---

     
 
all -  [ A library just for Document Extraction with LLMs, connector to Langchain | ExtractThinker ](https://www.reddit.com/r/LangChain/comments/1d2iubg/a_library_just_for_document_extraction_with_llms/) , 2024-05-30-0911
```
A month back I did a [post](https://www.reddit.com/r/LangChain/comments/1c6afp1/creating_a_framework_like_langchain_but_
just_for/) about creating a library just focused on Extraction for documents. Was well received here and in other places
, including by some companies. So I gave it a try.

After a month and 2k+ lines of code, I created this repo, based on t
he previous one, that will contain a full-open source code. Contains already close to 200+ (as the writing of this post)
.

[https://github.com/enoch3712/ExtractThinker](https://github.com/enoch3712/ExtractThinker)

# The motivation

Langcha
in works great integrating the several pieces **but tends to be a pain to extract data from documents and other sources*
*. ExtractThinker falls into the class of tools like instructor (pydantic outputs) and litellm (agnostic call between LL
M models), which solves a specific problem. A bit more high level yes, but the focus is the same. **Extraction for docum
ents like ORM with LLM.**

You can read in detail here:

[https://medium.com/towards-artificial-intelligence/extractthin
ker-ai-document-intelligence-with-llms-72cbce1890ef](https://medium.com/towards-artificial-intelligence/extractthinker-a
i-document-intelligence-with-llms-72cbce1890ef)

# Basic use case and idea

https://preview.redd.it/6qqufnee063d1.png?wi
dth=904&format=png&auto=webp&s=55bbd1aad1606fe6b83f4f07f338efab4deb6023

You can then use a middleware to inject the QR 
code content, and so on. I think you get the drill

# Why is this useful? Just do GPT-4o everything, use vision if neede
d

The project will focus in two things:

**Reducing the pain of leading with document extraction**

The project will ha
ndle tasks such as classifying and grouping documents. For example, it can be used to separate content within a collecti
on of PDFs with random pages.

[splitting in action](https://preview.redd.it/k10voqea063d1.png?width=1170&format=png&aut
o=webp&s=a64eaf8a015668ef85e0126226dd6e942ca53e5a)

This would give you a list already separated and extracted (e.g firs
t 2 pages invoice, last page driver's license). This classification will expand to multiple strategies and techniques.


**Reducing costs for scalability**

Build your architecture that works as well as GPT-4 with scalability and low cost. M
ore in this article:

[https://medium.com/@enoch3712/how-companies-use-llms-to-process-4-000-cvs-for-1-extractthinker-3f
a0815057c3?sk=7fe626701a203135370e95f68bcb59f1](https://medium.com/@enoch3712/how-companies-use-llms-to-process-4-000-cv
s-for-1-extractthinker-3fa0815057c3?sk=7fe626701a203135370e95f68bcb59f1)

Just finished the final touches for the code, 
and it's a real use case that worked out great using inexpensive quantized models from deepinfra.

**The code still not 
production-ready and missing most of the features, but will make more sense with templates once i build the documentatio
n.**

I intend to eventually integrate this into langchain to be used like **pypdf**.

If you can assist me with feature
s as issues, use cases, or if anyone is interested in giving it a try, I would greatly appreciate it.

Thank you for you
r time.
```
---

     
 
all -  [ A 'new' Object & Vector Database for Python ](https://www.reddit.com/r/Python/comments/1d2iq74/a_new_object_vector_database_for_python/) , 2024-05-30-0911
```
[ObjectBox](https://objectbox.io/python-on-device-vector-and-object-database-for-local-ai/) ([GitHub](https://github.com
/objectbox/objectbox-python)) is an embedded database for Python objects and high-dimensional vectors. Today is it's fir
st stable release for Python developers. It's very lightweight similar to SQLite, but built for objects so it's faster a
s there's no SQL layer in-between. It's the very first vector database that also runs on smaller low-memory devices. The
 article comes with first benchmarks and hints at the LangChain integration.
```
---

     
 
all -  [ Building an Autonomous AI Agent with LangChain and PostgreSQL pgvector ](https://www.reddit.com/r/YugabyteDB/comments/1d2ic8q/building_an_autonomous_ai_agent_with_langchain/) , 2024-05-30-0911
```
Discover how to create a fully autonomous AI travel agent, capable of finding listings and managing bookings, using Lang
Chain, OpenAI, PostgreSQL, and pgvector, with YugabyteDB as the underlying database. Click to learn how to build your ow
n AI agent backed by PostgreSQL, using components available in today’s ecosystem. 

[https://www.yugabyte.com/blog/build
-autonomous-ai-agent-with-langchain-and-postgresql-pgvector/](https://www.yugabyte.com/blog/build-autonomous-ai-agent-wi
th-langchain-and-postgresql-pgvector/)
```
---

     
 
all -  [ LLM to get the relevant table from db  ](https://www.reddit.com/r/LangChain/comments/1d2i9fr/llm_to_get_the_relevant_table_from_db/) , 2024-05-30-0911
```
Hey guys ! I have Azure OpenAI GPT 4 LLM connected to Azure SQL DB. When I use this command db.get\_usable\_table\_names
() must return all the tables available, how every I'm getting the names of the ones that are dbo.table\_name

https://p
review.redd.it/fw1477bhu53d1.png?width=334&format=png&auto=webp&s=55b2f27dd632bf0c984eb3f71b22d7f8d052071c

https://prev
iew.redd.it/rwqeu6nku53d1.png?width=377&format=png&auto=webp&s=ca4eaeffdebd441b75ad22122f3e4798ecc67ae3

The tables in m
y db are as follows:

Question 1:How can I have the llm return all the available tables ?  
Question 2: Let's say I prom
pt the llm like 'Aggregate what age group customers prefer what products.' This prompt has two tables: Customer and Prod
uct. So I want the llm to join these two tables, and generate a response. So we want the llm to go through multiple tabl
es and give a response.   
How can I achieve this?   
Thanks for your help !
```
---

     
 
all -  [ CopilotKit v0.9.0 (MIT) - open source framework for building in-app AI agents ](https://www.reddit.com/r/LocalLLaMA/comments/1d2i4cz/copilotkit_v090_mit_open_source_framework_for/) , 2024-05-30-0911
```
I am a contributor to [CopilotKit](https://github.com/CopilotKit/CopilotKit), an open-source AI copilot framework for bu
ilding in-app AI copilots & in-app agents. 

I wanted to share some of the improvements we shipped in the latest release
: 

1. GPT-4o & native voice support + integration with Gemini. 
2. Node Llama CCP [support](https://github.com/CopilotK
it/CopilotKit/issues/238). 
3. LangChain Adapter: build in-app agents that can see realtime application context and take
 in-app action. Connect with any LLM. 
4. Generative UI: chatbot can stream generated UI components as specified by the 
developer & the LLM.
5. Copilot suggestions: auto suggestions of new questions for the end-user to ask with generative U
I. These can be manually controlled by the programmer, and also informed by GPT intelligence for the given context.

---


The library is fully open-sourced under MIT license and self hosted.  We're still looking for more things to add, happ
y to hear your thoughts :)

[https://github.com/CopilotKit/CopilotKit](https://github.com/CopilotKit/CopilotKit)
```
---

     
 
all -  [ Kernel crashes for FAISS similarity search ](https://www.reddit.com/r/LangChain/comments/1d2gxqi/kernel_crashes_for_faiss_similarity_search/) , 2024-05-30-0911
```
Hi, I am working with langChain right now and created a FAISS vector store. Since today, my kernel crashes when running 
a similarity search on my vector store. Has anyone an idea why this is happening?

    from langchain_community.document
_loaders import PyPDFLoader
    from langchain_community.vectorstores import FAISS
    
    f = open('credentials.txt')

    OPENAI_API_KEY = f.read()
    embeddings_model = OpenAIEmbeddings(api_key=OPENAI_API_KEY)
    
    document_loader =
 PyPDFLoader('filename.pdf')
    text_splitter=RecursiveCharacterTextSplitter()
    documents = document_loader.load_and
_split(text_splitter)
    
    vectorstore = FAISS.from_documents(documents, embeddings_model)
    vectorstore.similarit
y_search('query')

MacBook Pro intel, python 3.9, jupyter notebook, langchain 0.2.0
```
---

     
 
all -  [ Need to Build Custom LLM - Expert Needed ](https://www.reddit.com/r/LangChain/comments/1d2g20b/need_to_build_custom_llm_expert_needed/) , 2024-05-30-0911
```
Hello everyone! I'm in the process of developing a custom LLM for my startup. I'm looking for help and would appreciate 
it if anyone on this forum has experience with this and would be willing to meet via Zoom to discuss it further.
```
---

     
 
all -  [ How to make RAG chain faster so we get answer faster ](https://www.reddit.com/r/LangChain/comments/1d2eooc/how_to_make_rag_chain_faster_so_we_get_answer/) , 2024-05-30-0911
```
We created a chatbot with Llama2-7b-chat, RAG architecture using LangChain, Qdrant VectorDB, and for web side Django. Ev
erything works well. Even we hold the chat history. Now the only problem is the time we get the answer. Sometimes it tak
es 15 seconds to return the answer from the RAG chain and it's too bad.

What should we do to make the system faster?

I
f it's necessary I can share some of the codes.

Edit:

We are running all system in local. Because system have to be in
 local. Also we are running in GPU.

GPU: RTX A4000, 16GB

RAM: 32 GB

CPU: Intel® Xeon(R) W-2235 CPU @ 3.80GHz × 12

OS
: Ubuntu 22.04.4 LTS

  
We realized that retrieving from the DB chain is taking the most time of the work. Actually, we
 configured it with some parameters like collection is now with Manhattan distance, 384 size (because of the embedded mo
del), and binary quantization. We read that binary is x40 faster. But could we make more configuration?

https://preview
.redd.it/30knup1kq63d1.png?width=1918&format=png&auto=webp&s=8faf69a2a62d5e628fd46c4da9f909a3d5838c09

https://preview.r
edd.it/bedycqvkq63d1.png?width=1916&format=png&auto=webp&s=8ab2aec755a0e58f155026d49d9c4442b408e90b


```
---

     
 
all -  [ I just made a OpenAI ChatGPT MacOS Clone for Windows and Ubuntu and MIT licenced ](https://www.reddit.com/r/GPT4/comments/1d2eep5/i_just_made_a_openai_chatgpt_macos_clone_for/) , 2024-05-30-0911
```
# Explanation and Reason

Hi i am python developer and after OpenAI GPT-4o launch, i just i little bit angry because the
 app that they talked about just work in MacOS and a joke, it will come to windows november lol. Come on bro, if there i
s API, developers like us can make this app and release in just few days with langchain agent and tool infrastructure.


So i just release our GPT-4o clone and its totaly usable. You can use to take meeting notes, writing code and copying to
 your clipboard, or read and remember your calendar. There is unlimited possibilities.

# Current Features

* \*\*Screen
 Read\*\*
* Microphone
* \*\*System Audio\*\*
* Memory

--

* \*\*Clipboard\*\*
* Search Engines
* \*\*Python and SH Int
erpreters\*\*
* Writing and Running Scripts
* Using your Telegram Account
* Knowledge Management

# Open Call to devs

I
f there is some people to interest and develop this and adding some features just like auto take screen shot each 5 seco
nd and say somethings if something wrong. We can open a **GitHub Organization** and develop together. Just for open-sour
ce, just for competition.

https://preview.redd.it/vcbo2sw4l43d1.png?width=656&format=png&auto=webp&s=29c11615550af7eebd
caa7cdaf31d2c986536a44

[onuratakan/gpt-computer-assistant: gpt-4o Desktop Personel Asisstant (github.com)](https://gith
ub.com/onuratakan/gpt-computer-assistant)
```
---

     
 
MachineLearning -  [ [R] Building an Observable arXiv RAG Chatbot with LangChain, Chainlit, and Literal AI ](https://www.reddit.com/r/MachineLearning/comments/1crwh0q/r_building_an_observable_arxiv_rag_chatbot_with/) , 2024-05-30-0911
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

     
 
MachineLearning -  [ [P] LLMinator: A Llama.cpp + Gradio based opensource Chatbot to run llms locally(cpu/cuda) directly  ](https://www.reddit.com/r/MachineLearning/comments/1cpbgd1/p_llminator_a_llamacpp_gradio_based_opensource/) , 2024-05-30-0911
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

     
