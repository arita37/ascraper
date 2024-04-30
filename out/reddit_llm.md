 
all -  [ Python programming not running as intended ](https://www.reddit.com/r/learnpython/comments/1cgc49z/python_programming_not_running_as_intended/) , 2024-04-30-0910
```
I am trying to create this AI based text game according to this yt video (https://www.youtube.com/watch?v=nhYcTh6vw9A). 
I even updated the code according to the latest documentation but the inputs keep auto generating according to the runs 
I have made. Can anyone look into it? TIA.

\`\`\`python  
from astrapy import DataAPIClient  
import os  
from cassa
ndra.cluster import Cluster  
from cassandra.auth import PlainTextAuthProvider  
from langchain.memory import Cassandr
aChatMessageHistory, ConversationBufferMemory  
from langchain\_openai import OpenAI  
from langchain.chains import LL
MChain  
from langchain.prompts import PromptTemplate  
from dotenv import load\_dotenv  
  
load\_dotenv()  
  
A
STRA\_DB\_APPLICATION\_TOKEN = os.environ.get('ASTRA\_DB\_APPLICATION\_TOKEN')  
ASTRA\_DB\_API\_ENDPOINT = os.environ.
get('ASTRA\_DB\_API\_ENDPOINT')  
ASTRA\_DB\_KEYSPACE = os.environ.get('ASTRA\_DB\_KEYSPACE')  
OPENAI\_API\_KEY = os.
environ.get('OPENAI\_API\_KEY')  
ASTRA\_DB\_SECURE\_BUNDLE\_PATH = os.environ.get('ASTRA\_DB\_SECURE\_BUNDLE\_PATH') 
 
  
session = Cluster(  
cloud={'secure\_connect\_bundle': os.environ\['ASTRA\_DB\_SECURE\_BUNDLE\_PATH'\]},  
auth\
_provider=PlainTextAuthProvider('token', os.environ\['ASTRA\_DB\_APPLICATION\_TOKEN'\]),  
).connect()  
  
\# Initia
lize the client  
client = DataAPIClient('AstraCS:kSgsZywgSjxTgsDpvZOyhjCw:e3ede7de9085c114d03a5b5ce524aa94d85ebb5a7501
6c38b1e55cbe4aa20c6b')  
db = client.get\_database\_by\_api\_endpoint(  
  'https://c7a2f93b-5279-4c60-98f9-766f87ceb2
27-us-east1.apps.astra.datastax.com',  
namespace='database',  
)  
  
print(f'Connected to Astra DB: {db.list\_colle
ction\_names()}')  
  
message\_history = CassandraChatMessageHistory(  
session\_id='game',  
session=session,  
k
eyspace=ASTRA\_DB\_KEYSPACE,  
ttl\_seconds=3600 #store all this for a maximum of 60 minutes  
)  
  
message\_histo
ry.clear()  
  
cass\_buff\_memory = ConversationBufferMemory(  
memory\_key='chat\_history',  
chat\_memory=message
\_history  
)  
  
template = '''  
  
'''  
  
prompt = PromptTemplate(  
input\_variables=\['chat\_history', '
human\_input'\],  
template=template   
)  
  
llm = OpenAI(openai\_api\_key=OPENAI\_API\_KEY)  
llm\_chain = LLMCh
ain(  
llm=llm,  
prompt=prompt,  
memory=cass\_buff\_memory  
)  
  
choice = 'start'  
  
while True:  
respo
nse = llm\_chain.predict(human\_input=choice)  
print(response.strip())  
  
if 'The End.' in response:  
break  

  
choice = input('Your reply: ')  
\`\`\`

Also, I am trying to post it on stack exchange and even though I add the tr
iple back ticks, it still says wrong formatting and does not allow me to post my question. Can anyone suggest?
```
---

     
 
all -  [ Langtrace - Just added support for Langgraph ](https://www.reddit.com/r/LangChain/comments/1cgbwzx/langtrace_just_added_support_for_langgraph/) , 2024-04-30-0910
```
Hey Everyone,

I have been playing with Langgraph recently and it's awesome. There are some native ways to visualize the
 graph that you are building using Langgraph, which I ended up using multiple times as I was developing some agentic wor
kflows. Its useful to see the graph as you are developing and debugging it. I kinda thought it would be nice to have Lan
gtrace show the graph and decided to add support for it.

Wanted to show a quick preview of it. Excited for you all to t
ry it out and leave your feedback.

https://reddit.com/link/1cgbwzx/video/zbt44qozqhxc1/player
```
---

     
 
all -  [ My output from the langgraph is listed below, Now I want to access 'Anomaly_output', but when I try  ](https://www.reddit.com/r/LangChain/comments/1cgatw8/my_output_from_the_langgraph_is_listed_below_now/) , 2024-04-30-0910
```
'[(ToolAgentAction(tool=\'anomaly_detection\', tool_input={\'input\': \'df\'}, log='\\nInvoking: `anomaly_detection` wit
h `{\'input\': \'df\'}`\\n\\n\\n', message_log=[AIMessageChunk(content=\'\', additional_kwargs={\'tool_calls\': [{\'inde
x\': 0, \'id\': \'call_IvcL8ZQM7UhKBQVEmgkvC4s4\', \'function\': {\'arguments\': \'{'input':'df'}\', \'name\': \'anomaly
_detection\'}, \'type\': \'function\'}]}, response_metadata={\'finish_reason\': \'tool_calls\'}, id=\'run-f227a1be-c321-
43f5-92b6-bd7b9d8d0492\', tool_calls=[{\'name\': \'anomaly_detection\', \'args\': {\'input\': \'df\'}, \'id\': \'call_Iv
cL8ZQM7UhKBQVEmgkvC4s4\'}], tool_call_chunks=[{\'name\': \'anomaly_detection\', \'args\': \'{'input':'df'}\', \'id\': \'
call_IvcL8ZQM7UhKBQVEmgkvC4s4\', \'index\': 0}])], tool_call_id=\'call_IvcL8ZQM7UhKBQVEmgkvC4s4\'), {\'Anomaly_output\':
 [{\'USUBJID\': \'MAXIS-008-088\', \'AGE\': 25, \'PFS_MONTHS\': 3, \'SURVIVAL_MONTHS_FD\': 14, \'HEIGHT\': 169.0, \'WEIG
HT\': 51.4, \'BMI\': 18.0, \'RESP_RATE\': 19.75, \'TOBACCO_RATE\': 0.5, \'TUMOUR_SIZE\': 70.4, \'TUMOUR_SIZE_EOT\': 82.3
, \'CHEST_PAIN_N\': 1, \'COUGH_BLOOD_N\': 1, \'OVERALL_QUALITY_LIF_N\': 6.0, \'variable\': \'AGE\'}]})]'
```
---

     
 
all -  [ What are the best embeddings models for a specific domain? ](https://www.reddit.com/r/LangChain/comments/1cga0s7/what_are_the_best_embeddings_models_for_a/) , 2024-04-30-0910
```
Hello guys!  
Im working on a project in which i have two arrays:  
\- one with requirement(strings)  
\- another with a
 person's skills(strings)

I take these arrays and embedd them and then calculate the cosine similarity between them, in
 order to get the best skill for each requirement.

I was exploring the realm of embeddings and i'm at a point in which 
i don't really know if the models i'm using are the best ones. I saw that, for example, with instructor you can specify 
a domain but i didnt really see much of a difference.

What do you guys recommend in terms of models, and what do you th
ink about this methodology?  
Every time i see examples of embedding processes, i usually see people using long texts to
 then compare to others, but in this case i'm using only 'single' words, i. e. comparing NoSql to PostGreSql.

Thank you
 in advance.
```
---

     
 
all -  [ Should I create my own LLM?  ](https://www.reddit.com/r/LangChain/comments/1cg6l7p/should_i_create_my_own_llm/) , 2024-04-30-0910
```
I currently am looking forward to build a chatbot that scrapes data from websites (and updates the dataset dynamically) 
of different Universities. I am trying to build something that will help students to know more about the admissions and 
stuff.   
  
Although, I don't want to build it using RAG as it will be simple (I am doing this for my Final Year Projec
t, so I guess it should be good and something phenomenal). So, do you guys think building my own LLM would help my chatb
ot? It would definitely help in my learning curve, but am I going in the right track? There's this 5+ hours long video o
f FreeCodeCamp on Youtube, should I just start building my own LLM for this? 

What do I do? I legit think I am screwed,
 because I have some experience in creating chatbots and honestly, it is not a Final Year Project worthy, unless I do so
mething insane. I cannot change the project now as its already started, I need to submit reports that explains the whole
 model of this project.   
  
  
NEED EXPERT OPINIONS!
```
---

     
 
all -  [ Any value add to CrewAI if I get really proficient with Langchain? ](https://www.reddit.com/r/LangChain/comments/1cg5yca/any_value_add_to_crewai_if_i_get_really/) , 2024-04-30-0910
```
I have been looking into/using/learning both CrewAI and Langchain for the past week or so, and I am wondering if there i
s any value add to using CrewAI over just building out a given workflow in Langchain? It seems like CrewAI is just a lay
er of abstraction over Langchain - is this essentially accurate? How difficult is it to essentially replicate similar pr
ocesses in Langchain as in CrewAI?

Assume from the perspective of a generally proficient software dev - writing more co
de or working granularly is not really a huge issue to me
```
---

     
 
all -  [ [showcase] Page Assist - A simple Chrome extension Web UI / Side panel for Ollama ](https://i.redd.it/h0gufdvefgxc1.png) , 2024-04-30-0910
```

```
---

     
 
all -  [ Help with my final project ( langchain llms documents)  ](https://i.redd.it/2f0nbiu3dgxc1.jpeg) , 2024-04-30-0910
```
Hi everyone, this is going to be a long post so please read through it and help me out it’ll mean a lot.

I’m in my fina
l year BTech CSE from a small college and for my major project I was teamed up with only one girl who is the college top
per and as she’s interning rn none of the faculties are saying anything and I’m having to go to the reviews alone and I’
m not able to complete the project or documentation and the faculty is scolding me and idk what to do please help me out
. I need to publish a research paper also by the end of may.

So for my final graduation project due to some circumstanc
es I have taken the project “text summarisation and questions generation using langchain” where in we upload a document 
and it generates a summary and then generates questions ( like multiple choice, short answer, long answer, etc) and the 
student can practice questions before the exam kind of. A thing. How do I approach it? How do I work towards the project
. The main issue is my teammate isn’t working with me and I’m left alone trying to figure the project out and I don’t ha
ve much time. Please help me out
1) how do I approach it and what all should I learn or do to make the project
2) I’m no
t able to run llama2 api to summarize my docs as many errors are occurring so it must be some mistake on my part
- shoul
d I buy the open api tokens and work with it? 
- how do I approach the project please please please help me I’m in despe
rate need for help. 
( this is the basic front end I developed and any help will be appreciated) 
```
---

     
 
all -  [ Help with my project ](https://i.redd.it/aa8xlxgdcgxc1.jpeg) , 2024-04-30-0910
```
Hi everyone, this is going to be a long post so please read through it and help me out it’ll mean a lot

So for my final
 graduation project due to some circumstances I have taken the project “text summarisation and questions generation usin
g langchain” where in we upload a document and it generates a summary and then generates questions ( like multiple choic
e, short answer, long answer, etc) and the student can practice questions before the exam kind of. A thing. How do I app
roach it? How do I work towards the project. The main issue is my teammate isn’t working with me and I’m left alone tryi
ng to figure the project out and I don’t have much time. Please help me out
1) how do I approach it and what all should 
I learn or do to make the project
2) I’m not able to run llama2 api to summarize my docs as many errors are occurring so
 it must be some mistake on my part
- should I buy the open api tokens and work with it? 
- how do I approach the projec
t please please please help me I’m in desperate need for help. 
( this is the basic front end I developed and any help w
ill be appreciated) 
```
---

     
 
all -  [ Looking for a technical co-founder ](https://www.reddit.com/r/LangChain/comments/1cg35pn/looking_for_a_technical_cofounder/) , 2024-04-30-0910
```
I have an idea for an AI influencer platform that allows content creators to create digital clones of themselves for the
ir fans to interact with. Think Cameo or Onlyfans but entirely AI. 

Short term, it's relatively straight forward: a per
sonified chat bot with voice cloning/calling and consistent character image gen. Really just piecing different providers
 together like an LLM + 11labs + deepgram + stable diff. Want to keep the MVP pretty simple so we can ship fast and test
 product-market fit. 

Have already connected with nearly a dozen content creators who seem keen for something exactly l
ike this. But frankly, I'm a terrible dev. My strengths lie in at distribution, UX design, operations, and overall strat
egy. So I'm looking for a technical co-founder to build the MVP with. 

Don't really care about your background. As long
 as you're obsessive, just comment or shoot me a DM and let's see how far we can take this!
```
---

     
 
all -  [ How do I read files inside a directory present in an S3 bucket in such a way that I can read the PDF ](https://www.reddit.com/r/LangChain/comments/1cg327p/how_do_i_read_files_inside_a_directory_present_in/) , 2024-04-30-0910
```
In this below code, I want to make use of  so that I can retrieve metadata/ source URL from the documents: `docs = text_
splitter.split_documents(data)`

`s3_client = boto3.client('s3')`

`extracted_text = ''`

`bucket_name=<bucket-name>`

`
folder_name=<dir-name>`

`objects = s3_client.list_objects_v2(Bucket=bucket_name, Prefix=folder_name)`

`for obj in obje
cts['Contents']:`

`if obj['Key']!=folder_name:`

`obj = s3_client.get_object(Bucket=bucket_name, Key=obj['Key'])`

`dat
a = (obj['Body'].read())`

`pdf_file = PyPDF2.PdfReader(BytesIO(data))`

`for page_num in range(len(pdf_file.pages)):`


`page = pdf_file.pages[page_num]`

`extracted_text += page.extract_text()`

`data= // data pre-processing //`

`text_spl
itter = RecursiveCharacterTextSplitter(`

`chunk_size = 256,`

`chunk_overlap = 16)`

`docs = text_splitter.split_text(d
ata)`
```
---

     
 
all -  [ How to start with Multi Agents AI Orchestration ](https://www.reddit.com/r/LangChain/comments/1cg2hz1/how_to_start_with_multi_agents_ai_orchestration/) , 2024-04-30-0910
```
Hello,
I am new to LLM and GenAI , previous experience is into predictive modeling using structured data and NLP.
I see 
a lot of things in GenAI area and thinking of picking Multi Agent framework and wanted opinion of you geniuses ?
Thanks
```
---

     
 
all -  [ RAPTOR and PDF technical documents ](https://www.reddit.com/r/LangChain/comments/1cg1ov6/raptor_and_pdf_technical_documents/) , 2024-04-30-0910
```
I am trying to embed some technical documents, since they are very technical i need to have the best embedding technique
 possible, so that i can optimize the retrieval procedure as much as possible. If i just convert the technical documents
 to text embed them and store them inside the Chroma db, i notice than many times when i ask a question , it misses to f
etch the proper answer, although the answer is embedded inside the db. For this reason i decided to try and implement RA
PTOR method. But till now i see that it is ultra slow and it causes me problems. Has anyone tried raptor? Is it as good 
as it being mentioned and do you have a big improvement in your rag app?Do you have any example of implementing raptor w
hich i can try?

  
Thank you in advance.
```
---

     
 
all -  [ Loading csv files which have categorical data and numeric values into a graph to be used in RAG LLM  ](https://www.reddit.com/r/LangChain/comments/1cfzyzr/loading_csv_files_which_have_categorical_data_and/) , 2024-04-30-0910
```


Hey all,   

I would like to know how I should go about this. I have lots of  census data to work with, hundreds of th
ousands of rows. The fields are  things such as: age, sex, location, poverty, education and so on. My  goal is to load a
ll this data into a graph using some ontology and then  create a chatbot that allows the user to ask questions regarding
 the  data, such as 'Which state has the younger population?', 'Which tract  has the highest rate or poverty and oldest 
population?' and others. I  think using a RAG setup makes sense, but would like to if what  approaches I could take. I p
lan to load the data sources into a graph  and use that as context for feeding it into the LLM/RAG for the chatbot.  Thi
s initial dataset I am looking at starts with geographic components  such as if it is U.S. territory/non-territory, stat
e, county, tract. I  was thinking of having my ontology/scheme be that of geography. So there  would be 50 states + terr
itory nodes, then a node connected to county,  then a node connected to tract, then all the tracts would connect with  a
ll the thousands of observations. And I would store age, sex, poverty,  education as a property in the tract nodes. I'd 
also need the ability to  later add in other data to the graph about these states. Ultimately, I  want to understand the
 disparities of these communities by using  multiple data sources layered on top of each other then use natural  languag
e to query to data and have that go through the LLM/RAG which  then uses the graph for context in the response.   

Is t
his possible? Is this the right way to go about it?   

Thanks   
```
---

     
 
all -  [ What does the langchain architecture look like for this simple use case? ](https://www.reddit.com/r/LangChain/comments/1cfzk44/what_does_the_langchain_architecture_look_like/) , 2024-04-30-0910
```
I am new to LangChain. I have a use case / flow as follow:

  
A chatbot asistence firstly asks the user to provide link
s of some products they used in the past.

The asistence can advice the customer which varient of the product is suitabl
e for them based on the content of links the user provide and also the current available products catelogs in my website
. 

What does the langchain architecture look like for this simple use case? I will focus on learning those langchain co
mponent and tool to make this chatbot possible.

Shoud I use agent with various tools?

I understand I can use a webLoad
er to load the content from the user-provided links, split it, convert it with embedding model and store it in vector st
ore. The information I want to exptract from these product links are small and I can only do the web scraping and embedd
ing dynamically when the user provide the links.
```
---

     
 
all -  [ Configuring Ollama ](https://www.reddit.com/r/ollama/comments/1cfxacr/configuring_ollama/) , 2024-04-30-0910
```
Noob operating in the deep end of my pool. On windows 10, playing around with RAG and langchain using python.

I have a 
script that takes a local repo and chunks that for embedding with a FAISS db. Everything works fine with whatever LLM is
 choose (OpenAI or Ollama). My problems begin with embeddings. If I use OpenAI embeddings everything is ok but if I try 
Ollama using nomic-embed-text, the embedding speed slows down to less than a crawl. I let it run for two days and it was
n't finished. The repo is Autogen so it's a decent size (14,000 chunks) but OpenAI was finished in 5 minutes and Ollama 
is local so WTF?

I noticed that barely any of my measly 4gb of vram is being used, but it is definitely being used for 
the embeddings.

Is there a way to 'configure' Ollama to use more resources? 
```
---

     
 
all -  [ LangChain RunnableWithMessageHistory not storing tool_calls ](https://www.reddit.com/r/LangChain/comments/1cfwuws/langchain_runnablewithmessagehistory_not_storing/) , 2024-04-30-0910
```
I am using the following code (sanitized example):

    session_manager = RedisChatMessageHistory(
    str(session_id), 
redis_url, key_prefix='chat_history', ttl=3600, # TODO: add as configuration )
    prompt = ChatPromptTemplate(
        
input_variables=['input', 'chat_history'],
        messages=[
            SystemMessagePromptTemplate(
                p
rompt=PromptTemplate(input_variables=[], template=system_message)
            ),
            MessagesPlaceholder(variabl
e_name='chat_history', optional=True),
            MessagesPlaceholder(variable_name='agent_scratchpad'),
            Hu
manMessagePromptTemplate(
                prompt=PromptTemplate(input_variables=['input'], template='{input}')
         
   ),     
        ]
    )
    
    _agent = create_openai_tools_agent(
        llm=llm,
        tools=tools,
        pr
ompt=prompt,
    )
    
    agent = AgentExecutor.from_agent_and_tools(
        agent=_agent,  # type: ignore
        to
ols=tools,
        early_stopping_method='generate',
        callbacks=callbacks, # type: ignore
        verbose=_verbos
e,
        handle_parsing_errors=True,
        return_intermediate_steps=True,
    )
    
    agent_with_message_history
 = RunnableWithMessageHistory(
        agent,  # type: ignore
        session_manager.get_session_history,
        input
_messages_key='input',
        history_messages_key='chat_history',
    )

Then I run it:

    agent_response = await ag
ent_with_message_history.ainvoke(
        {'input': input, 'ability': 'test'},
        {
            'configurable': {'s
ession_id': session_manager.session_id},
            'callbacks': callbacks 
        },
    )

My output chat\_history c
omes with something like this:

    [
        HumanMessage(content='ok - test, call the product tool with argument test 
and answer 123 if it works'),
         AIMessage(content='123')
    ]

Note that the AIMessage does not have the tool\_c
alls argument

and the Redis register is like this:

    { 'type': 'ai', 'data': { 'content': '123', 'additional_kwargs'
: {}, 'response_metadata': {}, 'type': 'ai', 'name': null, 'id': null, 'example': false, 'tool_calls': [], 'invalid_tool
_calls': [] } }

Has anyone ran in a bug like that before?  
Any idea why it is happening?

The problem of this is that 
it keeps calling the same function over and over without being aware it already called it

Thank you very much in advanc
e for your attention and help :)
```
---

     
 
all -  [ Using Langchain with SillyTavern ](https://www.reddit.com/r/SillyTavernAI/comments/1cfwf79/using_langchain_with_sillytavern/) , 2024-04-30-0910
```
Hi y'all! Pretty new to all the AI and LLM stuff.

So, my objective is an AI assistant, i've chosen SillyTavern cuz of t
he integration with stuff like xtts and VRM

But now im kinda stuck. I have the character ready with TTS, (i still need 
to add STT lol), VRM and all the other stuff, so i started researching on API Calls

It seems Langchain is the easier op
tion, though im not sure it can be done that way (I haven't seen anything similar to what i want [Sillytavern and Langch
ain together])

I'm currently using OobaBooga as the back-end, and they have an extension for API Calling, but i've seen
 people saying it doesn't work with the api flag

Any ideas, solutions or guides are appreciated, and thanks for reading
!
```
---

     
 
all -  [ 'fine-tuning' routes ](https://www.reddit.com/r/LangChain/comments/1cfw2p8/finetuning_routes/) , 2024-04-30-0910
```
Is there any way to fine-tune / optimize routes via examples I give it? So I have an input and the agent decides which t
ool to use based on the routing that I've trained. 

I've seen a framework (semantic-router) do this but it seems fairly
 new and they aren't very transparent about what goes on under the hood.
```
---

     
 
all -  [ switch from the Testing field to Data engineer ](https://www.reddit.com/r/LangChain/comments/1cfuc06/switch_from_the_testing_field_to_data_engineer/) , 2024-04-30-0910
```
Hi guys, I would like to get your help regarding my case. I have been working as a software testing engineer for almost 
12 years. I have a solid Python and JS background. I found that the LLM is very interesting for me. I checked a lot of t
utorials about building my own RAG using langchain or lamaindex. I liked it  and I found the potential of jobs is start 
raising in the market.   


I'm thinking about start shifting to this new field but I'm not sure how can I cut the gap b
twn me and the required skills for these positions.   


What should I really know to be able to build a solid portfolio
? 
```
---

     
 
all -  [ Reverse-Akinator (A RAG experiment) ](https://www.reddit.com/r/LangChain/comments/1cftzk1/reverseakinator_a_rag_experiment/) , 2024-04-30-0910
```
I created a game called Reverse-Akinator where the user will ask questions to find out the person, that has been randoml
y selected from a CSV file. At low level, it is a history-aware RAG application where the content is derived from their 
respective Wikipedia page. I am currently using Groq API for query answering, Voyage's voayage-lite-02-instruct for embe
ddings and Chroma for vector store. It would really be helpful if you guys can post your opinion on this project and any
 way I can improve this further functionally. I used streamlit as UI.  
[Github Repo](https://github.com/karthickk17/Rev
erse-Akinator)
```
---

     
 
all -  [ PSA: prevent llama3 (via Ollama) endlessly chatting to itself ](https://www.reddit.com/r/LangChain/comments/1cftqqu/psa_prevent_llama3_via_ollama_endlessly_chatting/) , 2024-04-30-0910
```
I downloaded llama3 today and was surprised to see that it completely broke my app, because it would talk to itself endl
essly, adding some weird tokens to the output. Turns out llama3 outputs its results in a very different way than llama2,
 and apparently Ollama is still not ready to support that change. As a workaround, you can add this stop word to your mo
del:  

    stop=['<|eot_id|>']

In case anybody got blindsided by this issue, hope this helps.
```
---

     
 
all -  [ How to use Huggingface AutoTokenizer in llamacpp, LangChain? ](https://www.reddit.com/r/LangChain/comments/1cfqkvt/how_to_use_huggingface_autotokenizer_in_llamacpp/) , 2024-04-30-0910
```
  would like to use Tokenizer on Huggingface when using LlamaCpp in langchain\_community.llms. (Tokenizer on Huggingface
 for Korean models) However, LlamaCpp says that there are no parameters for tokenizer and it has been sent to model\_kwa
ggs.  
Is there any good way? 
```
---

     
 
all -  [ What is the default temperature value in LLM when loading it locally ? ](https://www.reddit.com/r/LLMDevs/comments/1cfpaj5/what_is_the_default_temperature_value_in_llm_when/) , 2024-04-30-0910
```
When Loading Google Flan  models or other LLM like LAMA  through Langchain HuggingFace Pipeline or other methods locally
, if not setting the temperature value in model\_kwargs  
What is the default value for the model ?  
Is the setting lik
e: temperature= 1, top\_p=1, repetition\_penalty=1.5   default for the model ?

Thanks in advanced!
```
---

     
 
all -  [ Reading data from multiple datatypes ](https://www.reddit.com/r/LangChain/comments/1cfkr6u/reading_data_from_multiple_datatypes/) , 2024-04-30-0910
```
I am working on a small project where i have pdf files and .md files. I am reading md files using TextLoader to separate
 on '#' and it works well. How do i read pdf files, should i read all of them using a common loader ? is there a way to 
do it separately?
```
---

     
 
all -  [ Using Langchain to create a writing/style guide ](https://www.reddit.com/r/LangChain/comments/1cfkcbj/using_langchain_to_create_a_writingstyle_guide/) , 2024-04-30-0910
```
I want to create a tool to rewrite text based on content and style guidelines (ex: use this word instead of this, readin
g level, etc.). Is there a way to do this easily with Langchain / ex give it some docs of all the vocabulary it should u
se and a list of style rules?
```
---

     
 
all -  [ Langchain with Azure OpenAI gpt4 ](https://i.redd.it/d9e3rud6daxc1.jpeg) , 2024-04-30-0910
```
I’ve been recently trying to get (title) working on a simple python file - just by following the docs - however no matte
r what YouTube video or documentation I follow, it seems I always get that the error shown in the attached photo. 

I’m 
confused what to do - there must definitely be a way to use langchain with gpt 4 Azure OpenAI. 

Thanks in advance!
```
---

     
 
all -  [ LLMs Or What Even Are Those? ](https://www.reddit.com/r/LangChain/comments/1cff5pa/llms_or_what_even_are_those/) , 2024-04-30-0910
```
**Large Language Models**, or LLMs, are advanced AI systems that enhance text prediction to an exceptional level — imagi
ne the autocorrect & text prediction on your phone, but far more sophisticated.

When you type 'I am going to the...', y
our phone might suggest words like 'store' or 'gym.', based on the words you wrote before. LLMs operate similarly, but o
n a much larger scale, using vast amounts of text to predict and generate language accurately.

**The Core Pillars of LL
Ms are:**

* **Transformer Models** - the backbone of most LLMs, these models process data by breaking down input text i
nto smaller parts (tokens) and analyzing the relationships between them. This helps the model understand and generate la
nguage based on the context provided.Just like our brain uses neurons to process and relay information, transformer mode
ls use tokens to process and generate language, making sense of the input based on context.
* **Training** - LLMs learn 
by consuming vast amounts of text data, from websites like Wikipedia to books and articles. This training allows them to
 understand language patterns and context, and, as a result, generate better text.It’s just like reading hundreds of boo
ks to enhance your knowledge and master a subject, we feed LLMs with text data from diverse sources like Wikipedia and v
arious books to help them learn, though with a small caveat — LLMs can do this anywhere from 100-1000 times *faster* tha
n us.
* **Fine-tuning** - after their initial training, LLMs can be fine-tuned with specific data sets to perform tasks 
like translation, content generation, or even coding.With fine-tuning, you’re giving your little helper a specific role 
& legend to fill — for example, 'Sir Code-a-lot”, who, after his rigorous initial training, is now sharpening the specif
ic skills needed to slay the mighty dragons in the C++ Language.

And if you want to see how different your autocorrect 
& text prediction on your phone is from actual Large Language Models – then here’s a cool visual showing the sheer scale
 of the various GPT LLMs Essentially, LLMs predict what comes next, depending on the context & your input. If you’re a p
rogrammer and you’re writing code in Python, and use an LLM-powered code editor, the model understands every line of cod
e you’ve written and suggests the next one accurately!

**The History of LLMs & Transformers**

The evolution of LLMs (*
*Large Language Models**) began with the introduction of the Transformer model by Google at NeurIPS 2017. 

This model i
ntroduced a new approach called 'attention mechanisms' that improves how machines understand the context within text. Ba
sically, a Transformer allows the model to focus on different parts of the input data at different times, improving its 
ability to generate accurate and contextually appropriate responses.

This model led to significant developments such as
 BERT and GPT models. GPT models, starting from GPT-1 to the latest iterations like GPT-3.5 and GPT-4, have significantl
y advanced in capabilities, achieving tasks that range from simple text generation to complex decision-making and proble
m-solving tasks.

And you know what’s the best part about LLMs becoming mainstream? 

Nearly every SaaS company is lever
aging them by building apps to solve the problems we creators & entrepreneurs face daily – responding to emails, schedul
ing meetings, finding time for family and leisure, data entry, everything you could imagine — there’s an LLM-based tool 
for it now.
```
---

     
 
all -  [ Parquet format to vectors ](https://www.reddit.com/r/LocalLLaMA/comments/1cfduko/parquet_format_to_vectors/) , 2024-04-30-0910
```
So, I have definitely struggled with trying to create embeddings locally for Parquet files. 
Do I really have to convert
 to CSV/Json. 

Always have trouble using FAISS locally, in most langchain based programs, may be an issue of me not und
erstanding paths to load and retrieve from. Which is very possible. 

Long Story short I have about 60 Parquet files (av
eraging about 150k rows each) 
I was wanting to test them with the new Snowflake embeddings models.


I mostly do low co
de//no code solutions to test things out, and am generally pretty comfortable in them. 
```
---

     
 
all -  [ Research topics in LLMs for a data scientist ](https://www.reddit.com/r/datascience/comments/1cfaga5/research_topics_in_llms_for_a_data_scientist/) , 2024-04-30-0910
```
Hi everyone,

In my experience, my company does a lot of work on LLMs and I can say with absolute certainty that those p
rojects are permutations and combinations of making an intelligent chatbot which can chat with your proprietary document
s, summarize information, build dashboards and so on. I've prototyped these RAG systems (nothing in production, thankful
ly) and am not enjoying building them. I also don't like the LLM framework wars (Langchain vs Llamaindex vs this and tha
t - although, Langchain sucks in my opinion).   


What I am interested in putting my data scientist / (fake) statistici
an hat back on and approach LLMs (and related topics) from a research perspective. What are the problems to solve in thi
s field? What are the pressing research questions? What are the topics that I can explore in my personal (or company) ti
me beyond RAG systems?

Finally, can anyone explain what the heck is agentic AI? Is it just a fancy buzzword for this se
ntence from Russell and Norvig's magnum opus AI book- ' A rational agent is one that acts so as to achieve the best outc
ome or, when there is uncertainty, the best expected outcome'.   


  


&#x200B;
```
---

     
 
all -  [ [0 YoE] Web Developer to Data Science. 4 months of applying, but ZERO interviews. ](https://www.reddit.com/r/EngineeringResumes/comments/1cfa81d/0_yoe_web_developer_to_data_science_4_months_of/) , 2024-04-30-0910
```
Hi,

I am a fullstack web developer with 3 years of experience in the field. Recently i wanted to switch to Data Science
 and so i completed my masters in Data Science in January.

I've been applying for jobs and doing self projects on the s
ide to make up for the lack of experience, but so far, I have not been successful in landing even a single interview.

I
t's really starting to afffect me mentally. I know that the market isn't so great right now.

But i want to get a job am
ongst all these hurdles.

I do not know if my resume is the problem or something else.  
It would be great if you could 
please help me with this and help me land atleast one interview.

&#x200B;

&#x200B;

https://preview.redd.it/4nk3kgu0x8
xc1.png?width=5100&format=png&auto=webp&s=69da8298e4bbac4091e89feb56a3fcac43e2b2d5
```
---

     
 
all -  [ How LangChain and ChatGPT plugins are getting attacked by this bug ](https://www.reddit.com/r/bugbounty/comments/1cf9wov/how_langchain_and_chatgpt_plugins_are_getting/) , 2024-04-30-0910
```
[https://journal.hexmos.com/insecure-output-handling/](https://journal.hexmos.com/insecure-output-handling/)
```
---

     
 
all -  [ How LangChain and ChatGPT plugins are getting attacked by this bug ](https://www.reddit.com/r/LangChain/comments/1cf9wl3/how_langchain_and_chatgpt_plugins_are_getting/) , 2024-04-30-0910
```
[https://medium.com/@sreedeep200/how-langchain-and-chatgpt-plugins-are-getting-attacked-by-this-bug-9a47807b66a3](https:
//medium.com/@sreedeep200/how-langchain-and-chatgpt-plugins-are-getting-attacked-by-this-bug-9a47807b66a3)
```
---

     
 
all -  [ How LangChain and ChatGPT plugins are getting attacked by this bug ](https://www.reddit.com/r/ChatGPT/comments/1cf9qnf/how_langchain_and_chatgpt_plugins_are_getting/) , 2024-04-30-0910
```
[https://journal.hexmos.com/insecure-output-handling](https://journal.hexmos.com/insecure-output-handling)
```
---

     
 
all -  [ Leveling up RAG ](https://www.reddit.com/r/LangChain/comments/1cf97bh/leveling_up_rag/) , 2024-04-30-0910
```
Hey guys, need advice on techniques that really elevate rag from naive to an advanced system. I've built a rag system th
at scrapes data from the internet and uses that as context. I've worked a bit on chunking strategy and worked extensivel
y on cleaning strategy for the scraped data, query expansion and rewriting, but haven't done much else. I don't think I 
can work on the metadata extraction aspect because I'm using local llms and using them for summaries and QA pairs of the
 entire scraped db would take too long to do in real time. Also since my systems Open Domain, would fine-tuning the embe
dding model be useful? Would really appreciate input on that. What other things do you think could be worked on (impress
ive flashy stuff lol)

I was thinking hybrid search but then I'm also hearing knowledge graphs are great? idk. Saw a pap
er that just came out last month about context-tuning for retrieval in rag - but can't find any implementations or disco
urse around that. Lot of ramble sorry but yeah basically what else can I do to really elevate my RAG system - so far I'm
 thinking better parsing - processing tables etc., self-rag seems really useful so maybe incorporate that?
```
---

     
 
all -  [ How LangChain and ChatGPT plugins are getting attacked by this bug ](https://www.reddit.com/r/developersIndia/comments/1cf8cgf/how_langchain_and_chatgpt_plugins_are_getting/) , 2024-04-30-0910
```
[https://journal.hexmos.com/insecure-output-handling](https://journal.hexmos.com/insecure-output-handling/)
```
---

     
 
all -  [ LangChain Wrapper for easy RAG Deployments ](https://www.reddit.com/r/LangChain/comments/1cf7q6y/langchain_wrapper_for_easy_rag_deployments/) , 2024-04-30-0910
```
Hey guys, I tested this app called talkdai/dialog on Github, and it allowed me to deploy a RAG with my customized conten
t in just some few minutes and a Docker-compose file.

It's totally based on langchain right now, and with a toml file w
ith my prompt and model settings, I was able to deploy it online using caddy and a simple PGVector instance.

Is there a
ny other application that does that?

Here is the link for the source code: [https://github.com/talkdai/dialog](https://
github.com/talkdai/dialog)
```
---

     
 
all -  [ Recommend me some courses for LLM ](https://www.reddit.com/r/Automate/comments/1cf5j96/recommend_me_some_courses_for_llm/) , 2024-04-30-0910
```

I recently tried to make a chatbot, and it was really frustrating to have chatgpt not work (idk why but it just couldn'
t answer langchain questions , maybe the training cutoff date) , the docs are not so well arranged... And even if I do s
omehow get the code to work, it does not perform very well bcz I don't know much in the first place, I have a theoretica
l understanding of ML, but idk what are the diff kind of chains, retrievers, agents... I just find it to be a lot of thi
ngs which are scattered all over the place


So, can someone pls recommend me a course on langchain which consolidates a
ll the different techniques (chains, agents, vectordb etc.) And goes a bit in depth for everything, like how does this c
hain work or the diff methods of querying to the vectordb... 
Also feel free to recommend courses other than langchain, 
it's just langchain is the only LLM framework I know... 

```
---

     
 
all -  [ Recommend me some courses for LLM ](https://www.reddit.com/r/MLQuestions/comments/1cf5egs/recommend_me_some_courses_for_llm/) , 2024-04-30-0910
```
I recently tried to make a chatbot, and it was really frustrating to have chatgpt not work (idk why but it just couldn't
 answer langchain questions , maybe the training cutoff date) , the docs are not so well arranged... And even if I do so
mehow get the code to work, it does not perform very well bcz I don't know much in the first place, I have a theoretical
 understanding of ML, but idk what are the diff kind of chains, retrievers, agents... I just find it to be a lot of thin
gs which are scattered all over the place


So, can someone pls recommend me a course on langchain which consolidates al
l the different techniques (chains, agents, vectordb etc.) And goes a bit in depth for everything, like how does this ch
ain work or the diff methods of querying to the vectordb... 
Also feel free to recommend courses other than langchain, i
t's just langchain is the only LLM framework I know... 

```
---

     
 
MachineLearning -  [ [D] Self-optimizing deterministic LLM memory using dspy, neo4j and vector databases. Need your input ](https://www.reddit.com/r/MachineLearning/comments/1cakjaf/d_selfoptimizing_deterministic_llm_memory_using/) , 2024-04-30-0910
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

     
 
MachineLearning -  [ [D] How to get the source documents from the retrieved context for RAG?  ](https://www.reddit.com/r/MachineLearning/comments/1bvoc1t/d_how_to_get_the_source_documents_from_the/) , 2024-04-30-0910
```
I'm not using Lanchain but only making API calls to an LLM service provider. The retriever is connected to a vector DB, 
and I would like to know what the LLM refers to WITHIN that retrieved context whenever it provides an answer, similar to
 how return_source_documents works in Langchain.

I'm using AzureOpenAI. I couldn't find much in their docs that related
 to returning the source documents. Any help will be greatly appreciated!

```
---

     
 
MachineLearning -  [ [P] RAG pipeline to query the ML Engineering Open Book ](https://www.reddit.com/r/MachineLearning/comments/1bu4wyx/p_rag_pipeline_to_query_the_ml_engineering_open/) , 2024-04-30-0910
```
I built a quick RAG implementation using Langchain to make it easy to query the [ML Engineering Open Book](https://githu
b.com/stas00/ml-engineering) by [Stas Bekman](https://twitter.com/StasBekman). The Multi-Vector retriever gave pretty go
od results and was quite easy to set up too. 

Github link - [https://github.com/shreyansh26/RAG-ML-Engg-Open-Book](http
s://github.com/shreyansh26/RAG-ML-Engg-Open-Book)

Hope this is useful for folks!
```
---

     
 
MachineLearning -  [ [Project] FinancialAdvisorGPT : LLM+RAG Boilerplate Project ](https://www.reddit.com/r/MachineLearning/comments/1btlpgd/project_financialadvisorgpt_llmrag_boilerplate/) , 2024-04-30-0910
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

     
 
MachineLearning -  [ [Project] Picachain, image search made simple. ](https://www.reddit.com/r/MachineLearning/comments/1bt7epv/project_picachain_image_search_made_simple/) , 2024-04-30-0910
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

     
 
deeplearning -  [ Seeking Advice: Solving Data Challenges with Large Language Models (LLMs) ](https://www.reddit.com/r/deeplearning/comments/1ca4nc1/seeking_advice_solving_data_challenges_with_large/) , 2024-04-30-0910
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

     
 
deeplearning -  [ Share the Coolest Out of The Box LLM Applications That Made You Say 'Wow that was smart' ](https://www.reddit.com/r/deeplearning/comments/1c9e6dj/share_the_coolest_out_of_the_box_llm_applications/) , 2024-04-30-0910
```
Hi, I'm looking at some LLM applications today but apart from guys doing big rags with langchain I don't see too many us
es that are out of the box or that make me say 'wow that was smart to use an LLM here'. Have you seen any cool stuff usi
ng LLMs recently that made you say 'wow, that was smart'?
```
---

     
