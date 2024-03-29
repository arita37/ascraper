 
all -  [ Azure AI search vs Chroma Db  ](https://www.reddit.com/r/LangChain/comments/1bqa628/azure_ai_search_vs_chroma_db/) , 2024-03-29-0910
```
Hi all , I was trying to evaluate and compare the performance of Azure AI search index vs Chroma Db in memory index . I 
have heard that Chroma Db is good for high speed retrieval but relevancy of retrieved docs are not that good . 

I was t
hinking that Azure AI search should easily outperform chroma DB  , So I configured both Chroma DB and Azure AI search In
dex with same configuration ( HNSW with Cosin similarity ) 
. I used same embedding model  text-embedding-3-small  for e
mbedding the test document ( 300 character small chunks)
.
Now I was a bit confused to see that , while testing with som
e queries both Vector Dbs( Indexes)are returning  the  same results . Even with k=4 nearest items , both are  returning 
same 4 doc chunks ( relevancy scores are different though)
  I am now concerned that somehow I have messed up something,
 What do you guys think?? Am I supposed to see the same results with same config or I am doing something wrong?

Can you
 guys suggest me some good dataset for benchmarking the retrieval systems.
Thanks in advance 😃


```
---

     
 
all -  [ Can LangChain still be used for free?! ](https://www.reddit.com/r/LangChain/comments/1bq9knx/can_langchain_still_be_used_for_free/) , 2024-03-29-0910
```
With the recent announcement of 'traces' being charged for, does anyone know if the rest of the framework is still free 
to use?!
```
---

     
 
all -  [ How can i stream output for my chain ? ](https://www.reddit.com/r/LangChain/comments/1bq881o/how_can_i_stream_output_for_my_chain/) , 2024-03-29-0910
```
The typical streaming method is not working for the below chain

chain\_main = RunnableParallel({  
'query': RunnablePas
sthrough(),  
'context': retrieval\_chain,  
}) | generation\_prompt | model | OpenAIFunctionsAgentOutputParser() | rout
e

But streaming method works for simple chain without function calling like the one below

chain = RunnableParallel({  

'query': RunnablePassthrough(),  
'context': retrieval\_chain,  
}) | generation\_prompt |model | parser

Can someone h
elp me on this. Thanks in advance for the help
```
---

     
 
all -  [ Webvoyageur GraphChain Agent ](https://www.reddit.com/r/crewai/comments/1bq7o9c/webvoyageur_graphchain_agent/) , 2024-03-29-0910
```
Hey guys did you think we ca implement that into Crew ?

This agent navigating autonomously on the web using real browse
r

[https://www.youtube.com/watch?v=ylrew7qb8sQ&ab\_channel=LangChain](https://www.youtube.com/watch?v=ylrew7qb8sQ&ab_ch
annel=LangChain)

  
[https://github.com/langchain-ai/langgraph/blob/main/examples/web-navigation/web\_voyager.ipynb](ht
tps://github.com/langchain-ai/langgraph/blob/main/examples/web-navigation/web_voyager.ipynb)


```
---

     
 
all -  [ Learning resources  ](https://www.reddit.com/r/LangChain/comments/1bq73n0/learning_resources/) , 2024-03-29-0910
```
I know that this question about LangChain is frequent but I just wanted to ask if there's any comprehensive or practical
 course for learning langchain? Because the documentations on python are SO vague and do not really teach anything. I've
 checked YouTube courses but most of them are old and langchain has changed ever since. Plus the YouTube courses all tea
ch the basics, they don't go through various modules.
```
---

     
 
all -  [ Do you use the 'system' role for adding prompts or just append it to the 'user' role? ](https://www.reddit.com/r/LangChain/comments/1bq5g0u/do_you_use_the_system_role_for_adding_prompts_or/) , 2024-03-29-0910
```
I am just trying to understand if any of you use the 'system' role for adding prompts to programmatic invocations. I kno
w this is the support by the books way to do it. But I have also attached the prompt directly to the 'user' role with si
milar accuracy. Wondering what the best practice is.
```
---

     
 
all -  [ ROAST MY RESUME 2nd year cs student  ](https://i.redd.it/j53vhmkg44rc1.jpeg) , 2024-03-29-0910
```

```
---

     
 
all -  [ How to implement Claude based Agents ? ](https://www.reddit.com/r/LangChain/comments/1bq1rgj/how_to_implement_claude_based_agents/) , 2024-03-29-0910
```
I have an application that is currently based on 3 agents using LangChain and GPT4-turbo.

I'd like to test Claude 3 in 
this context. However all my agents are created using the function `create_openai_tools_agent()`.

Reading the documenta
tion, it seems that the recommended Agent for Claude is the [XML Agent](https://python.langchain.com/docs/modules/agents
/agent_types/xml_agent). However this documentation is referring to Claude 2 instead of Claude 3. It's also assuming tha
t the model is a LLM and not a Chatbot. That seems weird. Especially given that Anthropic documentation is clear about u
sing a Chatlike API, with [a system prompt and a list of users/assistant messages](https://docs.anthropic.com/claude/ref
erence/messages_post). Instead the XML Agent seems to only be able to [understand chathistory as a single string](https:
//python.langchain.com/docs/modules/agents/agent_types/xml_agent#using-with-chat-history). 

Given that LLM in general, 
and Claude in particular are quite sensitive to prompting format, I'm not really happy with the idea of having a chat hi
story sent as a single string instead of the standard format provided by the API. Thus I'm hesitating about using the XM
L agent.

So I'm curious if any of you has any experience using the XML Agent with a chat history ? Or did you use anoth
er kind of agent ?

Thanks in advance !
```
---

     
 
all -  [ ConversationalRetrievalChain and langserve ](https://www.reddit.com/r/LangChain/comments/1bq0t3b/conversationalretrievalchain_and_langserve/) , 2024-03-29-0910
```
Hi, I have an error with langchain and langserve that I can't solve. 
This is my code:

from langchain_core.output_parse
rs import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import Run
nableMap, RunnablePassthrough
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from operator import itemgetter

from langchain_community.vectorstores import Chroma
from langchain_core.messages import AIMessage, HumanMessage, get_buf
fer_string
from langchain_core.prompts import format_document
from langchain_core.runnables import RunnableParallel
from
 langchain.retrievers.multi_vector import MultiVectorRetriever
from langchain.storage import LocalFileStore
from langcha
in.prompts.prompt import PromptTemplate
from langchain.docstore.document import Document
from langserve import add_route
s
from fastapi import FastAPI

vectorstore = Chroma(collection_name='summaries', 
                     embedding_functio
n=OpenAIEmbeddings(), 
                     persist_directory='path/to/directory/')

store = LocalFileStore('path/to/dir
ectory')
id_key = 'doc_id'

retriever = MultiVectorRetriever(
    vectorstore=vectorstore,
    docstore=store,
    id_ke
y=id_key,
    search_kwargs={'k': 3}
)

_template = '''Given the following conversation and a follow up question, rephra
se the follow up question to be a standalone question, in its original language.

Chat History:
{chat_history}
Follow Up
 Input: {question}
Standalone question:'''

CONDENSE_QUESTION_PROMPT = PromptTemplate.from_template(_template)

template
 = '''Answer the question based only on the following context:
{context}

Question: {question}
'''
ANSWER_PROMPT = ChatP
romptTemplate.from_template(template)

DEFAULT_DOCUMENT_PROMPT = PromptTemplate.from_template(template='{page_content}')


def _combine_documents(
    docs, document_prompt=DEFAULT_DOCUMENT_PROMPT, document_separator='\n\n'
):
    format_doc
 = [ ]
    for i in docs:
        single_doc = Document(page_content=i, metadata={'doc_name': 'doc_name'})
        forma
t_doc.append(single_doc)
    doc_strings = [format_document(doc, document_prompt) for doc in format_doc]
    return docu
ment_separator.join(doc_strings)


_inputs = RunnableParallel(
    standalone_question=RunnablePassthrough.assign(
     
   chat_history=lambda x: get_buffer_string(x['chat_history'])
    )
    | CONDENSE_QUESTION_PROMPT
    | ChatOpenAI()
 
   | StrOutputParser(),
)

_context = {
    'context': itemgetter('standalone_question') | retriever | _combine_document
s,
    'question': lambda x: x['standalone_question'],
}

llm = ChatOpenAI()

conversational_qa_chain = _inputs | _conte
xt | ANSWER_PROMPT | llm

app = FastAPI(
    title='LangChain Server',
    version='1.0',
    description='Spin up a sim
ple api server using Langchain's Runnable interfaces')

add_routes(app, conversational_qa_chain)

if __name__ == '__main
__':
    import uvicorn

    uvicorn.run(app, host='localhost', port=8000)

When I try to use playground or I try to use
 request like this:  

import requests

inputs = {'input': {'question': 'what do you know about harrison', 'chat_history
': []}}
response = requests.post('http://localhost:8000/invoke', json=inputs)

response.json()

I have this error: 

cha
t_history=lambda x: get_buffer_string(x['chat_history'])
KeyError: 'chat_history'

Do you know a way to solve this error
? 
```
---

     
 
all -  [ Getting invalid literal for int() with base 10 while using from_uri method in the SQLDatabase ](https://www.reddit.com/r/LangChain/comments/1bq0r2j/getting_invalid_literal_for_int_with_base_10/) , 2024-03-29-0910
```
While trying to connect to presto db I am getting the invalid literal for int() with base 10 

Though I have tried all o
ptions of converting the port number to int using below

int(port\_number)

int(float(port\_number)

I am still getting 
the error, also needs to understand more on the from\_uri method, will that only take conn\_str \[string \] as parameter
?  
Outside the langchain I could able to connect to presto DB with dbapi.  
please help
```
---

     
 
all -  [ Tuning RAG retriever to reduce LLM token cost (4x in benchmarks) ](https://www.reddit.com/r/LangChain/comments/1bpz9dw/tuning_rag_retriever_to_reduce_llm_token_cost_4x/) , 2024-03-29-0910
```
Hey, we've just published a tutorial with an adaptive retrieval technique to cut down your token use in top-k retrieval 
RAG:

https://pathway.com/developers/showcases/adaptive-rag.

Simple but sure, if you want to DIY, it's about 50 lines o
f code (your mileage will vary depending on the Vector Database you are using). 
Works with GPT4, works with many local 
LLM's, works with old GPT 3.5 Turbo, does not work with the latest GPT 3.5 as OpenAI makes it hallucinate over-confident
ly in a recent upgrade (interesting, right?). Enjoy!
```
---

     
 
all -  [ AI Chain Builder for Code Manipulation ](https://www.reddit.com/r/LangChain/comments/1bpyx3o/ai_chain_builder_for_code_manipulation/) , 2024-03-29-0910
```
Hello everyone. I'm Tom, CTO and Co-Founder of [Autonoma AI](https://getautonoma.com). I'm coming with [something we coo
ked up this weekend](https://gitgud.autonoma.app/) and wanted your feedback on. [Here's a video](https://www.youtube.com
/watch?v=6kfr1lqw2gg) if you like that format better.

It's **free**, **no account needed**, **no credit card needed**. 
We just want you guys to tell us what you think.

&#x200B;

It's very alpha, so I apologize in advance for the bugs and 
issues that might exist.

Feel free to ask about the architecture or design decisions, or whatever you want to discuss a
bout.

Thank you all in advance for this as well.

&#x200B;

If you like the product, I'd like to ask you to upvote the 
[producthunt post](https://www.producthunt.com/posts/gitgud), it'd really help us!
```
---

     
 
all -  [ Error when trying to get answer using qa_chain ](https://www.reddit.com/r/LangChain/comments/1bpxeq5/error_when_trying_to_get_answer_using_qa_chain/) , 2024-03-29-0910
```
Hi everyone, I'm following this [tutorial](https://medium.com/@Siddharth.jh/conversational-chat-bot-using-open-source-ll
m-model-dolly-2-0-with-added-memory-acfacc13a69e) and I'm at the step where I am testing chatting with the AI chatbot. I
 have created the qa\_chain and I am using it similar to how it is in the tutorial but I am getting the following error 
after I input my question and it tries generating the answer:

`generated_sequence = self.model.generate(`

`^^^^^^^^^^^
^^^^^^^^^`

`TypeError: transformers.generation.utils.GenerationMixin.generate() got multiple values for keyword argumen
t 'pad_token_id'`

I am wondering what this issue could be coming from? I checked the collab provided in the tutorial an
d I can't seem to find any significant differences between my code and theirs.

&#x200B;

Thanks
```
---

     
 
all -  [ Provide feedback on my Resume - 3 YOE ](https://www.reddit.com/r/resumes/comments/1bpvhe4/provide_feedback_on_my_resume_3_yoe/) , 2024-03-29-0910
```
* Resume not getting shortlisted (Not getting any interviews)
* I'm looking for a Backend Developer / GenAI / AI/ML Engi
neer role  


https://preview.redd.it/n62lsibds2rc1.png?width=1404&format=png&auto=webp&s=cacc6319629b5343a0cc7a2f1db432
3f05cf473f
```
---

     
 
all -  [ Need help with my SQL LLM  ](https://www.reddit.com/r/LangChain/comments/1bptmed/need_help_with_my_sql_llm/) , 2024-03-29-0910
```
Hi guys , I have a SQL LLM already implemented using. OpenAI API. I have tried ollama models but it’s taking a lot of ti
me to process. So now I need to use llama.cpp models .. I don’t know how to implement it. Please ping me .. you can take
 a look at the code. 
Thanks a lot 
```
---

     
 
all -  [ Needed help to create a chatbot  ](https://www.reddit.com/r/LangChain/comments/1bpt0rl/needed_help_to_create_a_chatbot/) , 2024-03-29-0910
```
Hi everyone, despite having some experimentation using langchain, I still can't figure out how to create a best chatbot,
 in the sense of its way in communication, relavancy and good RAG. I request everyone to guide me so that I could go in 
right direction and build one for my experience. This is a request. (PS: The RAG process should be capable of taking doc
ument chunks from PDF, video, URL'S, and local files too. Also guide me the type of chunking to use for various types of
 data)
```
---

     
 
all -  [ Where does faiss store my data? ](https://www.reddit.com/r/LangChain/comments/1bpsvy8/where_does_faiss_store_my_data/) , 2024-03-29-0910
```
I'm using FAISS vector database for my work. 
Just curious where the database is stored. Is it stored somewhere locally 
or what? 

Is it safe to pass personal information to FAISS? 

I'm performing chunking and later passing this chunks int
o FAISS

Data= faiss.from_texts(texts, embeddings)
```
---

     
 
all -  [ Custom evaluation of LLM responses ](https://www.reddit.com/r/LangChain/comments/1bprzs6/custom_evaluation_of_llm_responses/) , 2024-03-29-0910
```
Hey Community, I want to run evaluation over my model responses such that it is done independently of the rag pipeline. 
Essentially, I have a CSV generated as an output of my RAG pipeline which contains, question, correct answer and model r
esponse. Now, I want to evaluate if the model response matches the correct answer independently of the RAG pipeline. I w
as looking into some of the langchain metrics like Accuracy, correctness , cot_qa but have not been able to actually get
 any of them working, cause all the chains require a model that generates answers for the question instead of just evalu
ating correct answer with model answer.  I have tried prompt control, QA eval chain, or literally building a custom chai
n with the sole purpose of evaluation but none of that has worked. Has anyone tried this before or has any idea how it c
an be achieved please?
```
---

     
 
all -  [ HuixiangDou: Overcoming Group Chat Scenarios with LLM-based Assistance.[Discussion] ](https://www.reddit.com/r/LocalLLaMA/comments/1bprxm5/huixiangdou_overcoming_group_chat_scenarios_with/) , 2024-03-29-0910
```
 'HuixiangDou' is a domain-specific group assistant, designed to answer user questions. It has been running for half a y
ear and helped thousands of  OpenMMLab users.

https://preview.redd.it/pkzohku8u1rc1.png?width=778&format=png&auto=webp&
s=1c11f8b83078116babbd43ad31018d374505a539

Differs from langchain or llamaIndex, HuixiangDou is for group chat scenario
s.

1. We designed a rejection pipeline to eliminate hallucination caused by gossip.
2. It is highly practical, for exam
ple, it can answer questions about table content in a PDF file, not just body text.

Now Huixiangdou's web portal is  li
ve.Here, you can create your own knowledge base and integrate it into Lark and WeChat groups without any coding.

 Learn
 more at:

 [http://github.com/internlm/huixiangdou](http://github.com/internlm/huixiangdou)

[http://arxiv.org/abs/2401
.08772](http://arxiv.org/abs/2401.08772)

&#x200B;

https://reddit.com/link/1bprxm5/video/wlszr0lgu1rc1/player
```
---

     
 
all -  [ RAG system + Math Agent ](https://www.reddit.com/r/LangChain/comments/1bprh9c/rag_system_math_agent/) , 2024-03-29-0910
```
Hi everyone, I am currently building a financial RAG, the RAG alone, it performs great till it starts to derive math for
mulas to run, then the LLM is unable to evaluate the math expression accurately. What are the solutions to giving the LL
M, the ability to Compute Math?. I have seen the LLMMathChain agent, but how do I combine it with the retrieval chain?
```
---

     
 
all -  [ Hosting AI Agents? ](https://www.reddit.com/r/LangChain/comments/1bpr6nb/hosting_ai_agents/) , 2024-03-29-0910
```
I’m finishing up a system that can take transcripts of users doing their processes or Process Definition Documents, and 
automatically generate Langchain AI Agents chains and tools. I’ve got a couple agents ready to push to prod, but having 
trouble finding a place to host them. Where do people here host their agents?
```
---

     
 
all -  [ Hosting AI Agents? ](https://www.reddit.com/r/AutoGPT/comments/1bpr5jy/hosting_ai_agents/) , 2024-03-29-0910
```
I’m finishing up a system that can take transcripts of users doing their processes or Process Definition Documents, and 
automatically generate AI Agents chains and tools (currently using Langchain). I’ve got a couple agents ready to push to
 prod, but having trouble finding a place to host them. Where do people here host their agents?
```
---

     
 
all -  [ FAISS.load_local is so slow ](https://www.reddit.com/r/LangChain/comments/1bpqoiz/faissload_local_is_so_slow/) , 2024-03-29-0910
```
&#x200B;

# Summary

I am trying to run FAISS.load\_local after a .save\_local on a 60k pdf pickle file in order to not 
repeat the embedding procedure everytime for a RAG. But it is really slow and I would like to launch all the RAG workflo
w fastly :( Could it be due to the huge amount of data?

OS: Ubuntu 18.04.6 LTS (Bionic Beaver)

Faiss version: faiss-cp
u==1.7.4

Installed from: pip install in conda env

Running on: Cluster with GPU Tesla V100-SXM2-32GB

Interface: Python


# Reproduction instructions

First, I have launched these lines on a py script (ingest.py):

vectorstore = FAISS.from\
_documents(documents=chunks, embedding=embeddings,)  
vectorstore.save\_local('./faiss\_db')

And then on a different py
 script (rag.py):

vectorstore = FAISS.load\_local('./faiss\_db', embeddings, allow\_dangerous\_deserialization=True)  

retriever = vectorstore.as\_retriever()

The log file gives me back only this:

'All keys matched successfully'

&#x200B
;

Can you help me, please?  
Thank you in advance!
```
---

     
 
all -  [ Autogen using Local LLMs ](https://www.reddit.com/r/LangChain/comments/1bpof9x/autogen_using_local_llms/) , 2024-03-29-0910
```
Hey everyone, this tutorial explains how to use Multi-Agent framework Autogen by Microsoft using Local LLMs (and not any
 API) using Ollama & LiteLLM: https://youtu.be/AdGuzjGWZms?si=FHhwzaS0RoAiDubk
```
---

     
 
all -  [ Use existing LLM framework (vs) Custom build to tackle version mismatch issues ? ](https://www.reddit.com/r/LLMDevs/comments/1bpmky4/use_existing_llm_framework_vs_custom_build_to/) , 2024-03-29-0910
```
If I were to build a Devin kind of product which will be used in production and could possibly have a payment option in 
future. Which approach will be right to go with ?

I have used LangChain and EmbedChain frameworks before.

(or) I was w
ondering if it could be a good idea to custom build a mini framework with all prompts strategies and get going.

The mai
n challenge is because of frequent version issues especially with LangChain and OpenAI SDK, some of the example code whi
ch we copy from internet is obsolete  / deprecated and it wouldnt even run.

From broader spectrum of things, which appr
oach would be better ?
```
---

     
 
all -  [ ‘Open sourcing’ our complex RAG system ](https://www.reddit.com/r/LocalLLaMA/comments/1bpmfaa/open_sourcing_our_complex_rag_system/) , 2024-03-29-0910
```


I’ve made our backend public on GitHub for anyone who wants to check it out/borrow it. (I’ll add a readme later)

[mpl
x_rag](https://github.com/multiplexerai/mplx_rag)

Open source is a bit of a stretch as it’s pretty much just boiler pla
te at this stage. Eventually I’d like to turn it into libraries, just as another option for langchain and llamaindex.
Wh
y have I called it ‘complex’? Because compared to your basic RAG where it just answers a simple question, in my mind it 
is.

I’d also like to say I’m a mechanic and I don’t really know how to write code (although I’ve learnt a lot and now o
ptimistically think maybe I’m at an intern level). I’ve pretty much leveraged GPT-4 to do the heavy lifting but the idea
s are my own. So with that I’d love if some of the professionals could actually give it a code review or even contribute
 would be amazing.

I know there are a few things that I need to fix, like making all the functions stand alone files (w
ill come with making libraries). In my production set up I’m actually implementing Oauth and have tidied it up by doing 
exactly that.

I also use environments to store keys in production.

Also for the undoubted bUT iT uSEs OpENai. OpenAI A
PI libraries are pretty standard even if you’re not actually using openAI. You can insert mistral or what ever you want.


also the validate function was something I was playing around with. I was actually thinking you could use it (as a sta
nd alone func) to update the answers for Q&A’s that you’ve logged from users if you update your data.

Happy Easter!
```
---

     
 
all -  [ Seeking advice on LLMs and RAGs ](https://www.reddit.com/r/learnmachinelearning/comments/1bpm5c2/seeking_advice_on_llms_and_rags/) , 2024-03-29-0910
```
Hey guys so I’m working on a personal project and I was wondering if anyone had any advice. 

I’m currently using embedd
ings from HF to read a pdf and using chromadb and langchain to start a conversation chain to basically “chat with my doc
ument” 

The problem is that it’s not as accurate as I want it to be and it seems to “hallucinate” every now and then! L
ooking for some advice on it ie maybe creating my own sentence embedding or how to even do so and can give more info if 
needed (not sure how posting here works so just giving it a shot)  

Thanks!!~
```
---

     
 
all -  [ Creating a reminder task in langchain ](https://www.reddit.com/r/LangChain/comments/1bpiwmt/creating_a_reminder_task_in_langchain/) , 2024-03-29-0910
```
Hi everyone, I'm trying to create a studying tutor with LLMs and langchain. What I'm looking for is that the app reminds
 the student once in a while during the conversation if he/she has done his/her homework, and based on the answer remind
 him/her later or don't remind her again. I'm looking for a clue on how to achieve such a thing.  
Thanks in advance

&#
x200B;

&#x200B;
```
---

     
 
all -  [ Free Courses from NVIDIA ](https://www.reddit.com/r/FreeITCourses/comments/1bpe0sm/free_courses_from_nvidia/) , 2024-03-29-0910
```
Hey everyone,

Exciting news! NVIDIA just launched free Al courses, no payment needed. If you're aiming to upskill by 20
24, here are eight essential courses you shouldn't miss

 1. Developing a Mind in Ten Minutes - Understand neural networ
ks and how they learn from data. - Link: [https://lnkd.in/e4FGDzuv)

 2. The Meaning of Generative Al -⁃ Dive into how g
enerative Al works, its applications, and challenges - Link: [https://lnkd.in/eKPmgRHj)

 3. Artificial Intelligence ins
ide the Data Centre ⁃ Explore Al use cases, machine learning frameworks, GPU architecture, and more. - Link: [https://ln
kd.in/e4-YhiW8)

 4. Use Retrieval Augmented Generation to enhance your LLM - Learn about RAG retrieval procedure and NV
IDIA AI Foundations. - Link: [https://lnkd.in/ehndH8PC)

 5. Proficiency with Recommender Systems . Master e-commerce re
commendation systems techniques - Link: [https://lnkd.in/euKVZ_Tb)

 6. Streamline Data Science Processes with No Code M
odifications ⁃ Discover integrating GPU and CPU benefits into your operations. - Link: [https://lnkd.in/eN7jeG3t)

 7. C
reating RAG Agents Utilising LLMs ⁃ Explore scalable LLM deployment strategies and contemporary LangChain models. - Link
: [https://lnkd.in/eycWGKzp)

 8. Introduction to Networking ⁃ Gain insights into networks, Ethernet, TCP/IP- protocol, 
and OSI model. - Link: [https://lnkd.in/eeYNyWnX)

 Feel free to leave your thoughts or questions below each course link
!
```
---

     
 
all -  [ Help with LLM to design circuits ](https://www.reddit.com/r/LangChain/comments/1bp914d/help_with_llm_to_design_circuits/) , 2024-03-29-0910
```
I have a project where I need to create an assistant that will help my professor which teaches digital circuits at the u
niversity. The purpose of the project is that if a student was studying for an exam at 3 AM but needs to understand a qu
estion or circuit diagram, they can ask the AI assistant which is basically as good as the professor himself. Ill need t
o have separate sessions ans save the conversation in a database.

The professor sent me the data which consist of Power
Point presentations which consists of images and text and those are what I want my LLM to focus on. The LLM should be ab
le to draw a circuit diagram to explain what its showing. 

 I tried gpt vision but its not showing proper results and t
he software we use for the circuit diagrams is simulink. I know how to save and store the data in a database and load ea
ch user separately and I know how to do rag but my main issue lies in how can I allow my LLM use simulink to design circ
uits? Do I need to use agemt? If yes, how do I connect it and allow it to design from simulink? 
```
---

     
 
all -  [ LangGraph with Claude? ](https://www.reddit.com/r/LangChain/comments/1bp7thq/langgraph_with_claude/) , 2024-03-29-0910
```
Hi, like the title says I would like to know whether LangGraph works well with all the Claude models? I never tested the
 function calling abilities of Claude and have no idea if they work well inside the LangGraph framework. Any type of ill
umination is greatly appreciated.

Thanks in advance.
```
---

     
 
all -  [ AWS OpenSearch Vector not returning anything on similarity search ](https://www.reddit.com/r/LangChain/comments/1bp6frg/aws_opensearch_vector_not_returning_anything_on/) , 2024-03-29-0910
```
I have an aws opensearch vector store. I can connect to it with the opensearch-py library and I can create an index and 
upload documents to the index. I am using langchain 0.1.13 and langchain-community 0.0.29

here's my code:

```python
fr
om langchain_community.document_loaders import TextLoader  
from langchain_text_splitters import CharacterTextSplitter  

from langchain_openai import OpenAIEmbeddings  
from langchain_community.vectorstores import OpenSearchVectorSearch

do
cuments = TextLoader('./test.txt').load()
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
docs =
 text_splitter.split_documents(documents)
  
embeddings = OpenAIEmbeddings()  
 
vector_store = OpenSearchVectorSearch(

    opensearch_url=f'https://{url}:{port}',
    index_name='test',
    embedding_function=embeddings,
    http_auth=auth
,
    use_ssl = True,
    verify_certs = False
)

vector_store.add_documents(documents=docs)
```

but when I run the bel
ow I get no documents back consistently even when the prompt is identical to the content in the index I get nothing back
:

```python
print(vector_store.similarity_search('what is my name on thursday?', k=1))
```

I've validated that the ind
ex names are all correct and the vector fields are all consistently named. I can query the index and see the documents u
ploading correctly here:

```python
from opensearchpy import OpenSearch

client = OpenSearch(
    hosts=[{'host': url, '
port': port}],
    http_auth=auth,
    use_ssl=True,
    verify_certs=False
)

response = client.search(
    index='test
',
    body={'query': {'match_all': {}}},
    size=1000
)

documents = [doc['_source'] for doc in response['hits']['hits
']]
print(documents)
```

Any thoughts on what the issue might be? Literally any help is appreciated.
```
---

     
 
all -  [ LangChain for a full framework - what options for more focused toolkits? ](https://www.reddit.com/r/LangChain/comments/1bp48si/langchain_for_a_full_framework_what_options_for/) , 2024-03-29-0910
```
LangChain does a great job as a full framework for LLM-based application development, but there are so many components s
ometimes you just want a toolkit that is better at a particular piece. I won't go down the rabbit-hole of 'frameworks vs
 toolkits' in general, but if you're looking for some of the alternatives to LangChain for pieces of the LLM-application
 development puzzle here's a write up: [https://www.mirascope.io/post/langchain-alternatives](https://www.mirascope.io/p
ost/langchain-alternatives)
```
---

     
 
all -  [ Question on querying pre stored vectors on weviate ](https://www.reddit.com/r/LangChain/comments/1bp33yk/question_on_querying_pre_stored_vectors_on_weviate/) , 2024-03-29-0910
```
I am relatively new to langchain. I need to load a pdf stored in GCS and I want chunk and embed the contents of the pdf 
and store it on weviate. I want to then retrive relevant vectors later and user a RetrivalQAChain. How do I do it? Any h
elp or code samples are appreciated! Thanks in advance. 
```
---

     
 
all -  [ Uploaded my first YouTube video ever and it's about LangChain! ](https://www.reddit.com/r/LangChain/comments/1bp2mao/uploaded_my_first_youtube_video_ever_and_its/) , 2024-03-29-0910
```
**Little announcement!**

What's up, everyone?!   

I finally uploaded my first YouTube video based on one of my blog po
sts: [https://www.youtube.com/watch?v=ubsqSWfXAPI](https://www.youtube.com/watch?v=ubsqSWfXAPI)  

It's a tutorial about
 using LangChain's Output Parsers with GPT to convert the contents of a PDF file to JSON. ([I originally wrote about thi
s on the blog here](https://www.gettingstarted.ai/how-to-extract-metadata-from-pdf-convert-to-json-langchain/)). To be h
onest, I've been wanting to publish a video for some time now but finally went for it so I'm not sure what to expect.

I
'm still learning about video editing, recording, and YouTube in general but **I'd love to know your feedback (and comme
nts)** so that I can implement it in future videos.

Thanks!
```
---

     
 
all -  [ HR Chatbot created using LangChain, free to use! ](https://www.reddit.com/r/LangChain/comments/1bozlzo/hr_chatbot_created_using_langchain_free_to_use/) , 2024-03-29-0910
```
Hey guys, I have developed a AI chatbot using LangChain, Pinecone, and ChatGPT. You can try it out for free on [HR Chatb
ot](http://hrchatbot.deligence.com/chat)

Let me know what you guys think about it!

```
---

     
 
all -  [ LCEL and evaluation on a RAG pipeline ](https://www.reddit.com/r/LangChain/comments/1boxuci/lcel_and_evaluation_on_a_rag_pipeline/) , 2024-03-29-0910
```
Hello,

I have implemented a RAG for retrieval on a postgres db. First, using embeddings I get the k-most relevant docum
ent and then using the load\_summarize\_chain from Langchain I create a response as in this [tutorial](https://cloud.goo
gle.com/blog/products/databases/using-pgvector-llms-and-langchain-with-google-cloud-databases/). My first question is th
at how can I use LCEL to make the chain. Lastly, how can I evaluate the response?

I tried using the  *DeepEvalAnswerRel
evancyEvaluator*  as shown [here](https://docs.confident-ai.com/docs/integrations-llamaindex) but I am getting the follo
wing error

`ERROR: AttributeError: 'Document' object has no attribute 'get_content'`
```
---

     
 
all -  [ Chroma db throws error at 2nd run ](https://www.reddit.com/r/LangChain/comments/1bowtfo/chroma_db_throws_error_at_2nd_run/) , 2024-03-29-0910
```
Hi!!  
I am using chroma db with pre computed embeddings for my rag application. Chroma runs well first time but every t
ime i re run my notebook i get this error. Thanks :)

https://preview.redd.it/aqq8insu6uqc1.png?width=3000&format=png&au
to=webp&s=51adc2a358e349fdbe3c211ed869d0f79c1bb986
```
---

     
 
all -  [ Prompt injection  ](https://www.reddit.com/r/LangChain/comments/1bovlcb/prompt_injection/) , 2024-03-29-0910
```
Can someone please highlight what is meant by prompt injection and what security concerns it may have , and if somebody 
can provide an example for the same that would be great 
```
---

     
 
all -  [ Possible to create a log querying tool with a natural language using aws bedrock ?  ](https://www.reddit.com/r/aws/comments/1bot20y/possible_to_create_a_log_querying_tool_with_a/) , 2024-03-29-0910
```
I want to create a tool which I feed it log data and can ask it questions in natural language like which transactions ha
ve the highest latency or take the most time for completion. Is it possible and if so does someone know what the high le
vel structure would be ? I tried to create it using langchain and ollama but the problem was the context size was more t
han the LLM could use which gave me poor results 
```
---

     
 
all -  [ How to implement prompt engineering well? ](https://www.reddit.com/r/LangChain/comments/1bosw8h/how_to_implement_prompt_engineering_well/) , 2024-03-29-0910
```
I implemented RAG using Ensemble Retriever. widh llama index

Before using the prompt template module, if  sent a query 
like “Hello”, llm would not respond because the query did not exist in the document. 

And  were able to solve these pro
blems by using the prompt template module.  

How important is prompt template engineering? And what should I do to set 
up prompt template engineering well?   


Below is the prompt template I wrote

    template = '''
    You are a chatbot
 fluent in Korean developed specifically for our company.
    Your primary role is to communicate with users by answerin
g their questions in Korean and providing feedback related to their questions.
    Your job is to provide the user with 
an answer regarding your company's employment rules when asked {query}.
    If you are asked a {query} question that is 
not related to the Company's employment rules, it is your responsibility to redirect the conversation to a topic related
 to the Company's policies and guidelines.
    You can also recommend questions to users based on your knowledge.
    We
 encourage our users to ask questions that are directly related to our company's operations, culture, or the specific gu
idelines we follow.
    '''

&#x200B;
```
---

     
 
all -  [ Long prompt and few-shot placement ](https://www.reddit.com/r/LangChain/comments/1boqup2/long_prompt_and_fewshot_placement/) , 2024-03-29-0910
```
Hi. I have a long prompt of about 500-700 tokens, and context gets added also since it's a RAG, so what I send to the LL
M could easily be a few thousand tokens per question. 

I am trying to get a response that is conversational and that ro
ughly follows a format like :

'To do x, y, and Z, you need to complete these steps.....blah blah.....For more info, ple
ase refer to this video.'

It returns good info but I can't for the life of me get it to return consistently structured 
responses. I've tried CoT, but it keeps stating it's reasoning, which makes it sound like the robot it is. I just want i
t to end with 'for more info..' Or 'if you need more help..' Etc. 

So I'm thinking few-shot, but I don't know if I shou
ld put the examples before or after the retrieved context given the length of the context and the prompt, in general. 


Has anyone experimented in these conditions?
```
---

     
 
all -  [ How can we tell which LLM arguments are being processed? ](https://www.reddit.com/r/LangChain/comments/1bopm2t/how_can_we_tell_which_llm_arguments_are_being/) , 2024-03-29-0910
```
It seems like the way langchain is set up, extra \`model\_kwargs\` are just quietly thrown on the floor.  I think that h
appens in the pydantic validation process, but I am not sure.

Is there any way to tell what's happening with the \`mode
l\_kwargs\`?

For example, [this langchain issue](https://github.com/langchain-ai/langchain/issues/10590) discusses what
 happens when a model class ignores the \`n\_ctx\` kwarg, and suggests a fix based on editing the \`validate\_environmen
t\` method of a class. But this requires identifying the right \`validate\_environment\` method in the class hierarchy, 
and then modifying a local variable (really a constant, \`model\_param\_names\` -- why isn't this a property of the clas
s instead of a local variable?).

Is there some way to trace the execution of an LLM constructor and see which kwargs ar
e actually sent, and which are ignored?
```
---

     
 
all -  [ How to store group chats??? ](https://www.reddit.com/r/LangChain/comments/1bopi12/how_to_store_group_chats/) , 2024-03-29-0910
```
I'm using Firestore for storage and I already built a solution to store group chats with the following structure:

\--> 
chats <collection>

\----> chat\_doc#1 <well, a doc>

\----> chat\_doc#2

\----> chat\_doc#n

\------> participants <arr
ay with user ids>

\------> messages <collection to store messages, each message in a doc>

Now, I'm looking to integrat
e LangChain into my app (easier to work with multiple LLM providers) and so I have to restructure my code. 

I used \`Fi
restoreChatMessageHistory\` and noticed that their structure is similar to mine, but in each chat doc they only have \`u
serId\` which holds a single user id. I want to replace that with a \`participants\` array or anything that can hold mul
tiple user ids. But I noticed there's no way to customize the \`FirestoreChatMessageHistory\` class to include multiple 
participants.

The way I'm thinking is to use the \`userId\` prop to store all user ids in comma-separated format, but:


1. I don't know if that will work well (or at all) & I don't have the time to test this out if it'll take too much time
 because of the overhead, and
2. there's way too much overhead - it feels stupidly irritating and I feel that there shou
ld be a neater way to implement this.

Anyone face this issue? How did you solve it?
```
---

     
 
all -  [ Codebase + External URL Context for LLM ](https://www.reddit.com/r/LangChain/comments/1bon41r/codebase_external_url_context_for_llm/) , 2024-03-29-0910
```
Sorry if this is obvious to most of you, I’m somewhat new. 

My app is currently successfully, in order:
- Getting URL c
ontent with document loader
- Getting file content from a GitHub codebase
- Sending this to OpenAi model with a prompt
-
 Serving the response to my front end

The issue is around token limitation. 

I would love to be able to get the whole 
codebase along with the reference URL content processed by the LLM and eventually return a single response to my fronten
d, of course I hit the token limit fast. 

I understand that text splitting and vector stores are the solution, I’ll get
 my head around that.

My question is, will I end up sending many requests and get many responses from the LLM?

I don’t
 mind many requests, but I don’t understand how I’ll get a single coherent response to my friend if it’s multiple LLM re
sponses.

Maybe I’m missing something obvious here. 
```
---

     
 
MachineLearning -  [ [D] : Scale PDF Q&A App to 10K Users with GPUs – <$250/Mo ](https://www.reddit.com/r/MachineLearning/comments/1b6jv56/d_scale_pdf_qa_app_to_10k_users_with_gpus_250mo/) , 2024-03-29-0910
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

     
 
MachineLearning -  [ [D] What Is Your LLM Tech Stack in Production? ](https://www.reddit.com/r/MachineLearning/comments/1b4sdru/d_what_is_your_llm_tech_stack_in_production/) , 2024-03-29-0910
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

     
 
deeplearning -  [ Tengyu Ma on Voyage AI - Weaviate Podcast #91! ](https://www.reddit.com/r/deeplearning/comments/1bjft8i/tengyu_ma_on_voyage_ai_weaviate_podcast_91/) , 2024-03-29-0910
```
**Voyage AI** is the newest giant in the embedding, reranking, and search model game!

I am SUPER excited to publish our
 latest Weaviate podcast with Tengyu Ma, Co-Founder of Voyage AI and Assistant Professor at Stanford University!

We beg
an the podcast with a deep dive into everything embedding model training and contrastive learning theory. Tengyu deliver
ed a **masterclass** in everything from scaling laws to multi-vector representations, neural architectures, representati
on collapse, data augmentation, semantic similarity, and more! I am beyond impressed with Tengyu's extensive knowledge a
nd explanations of all these topics.

The next chapter dives into a case study Voyage AI did **fine-tuning an embedding 
model for the LangChain documentation.** This is an absolutely fascinating example of the role of continual fine-tuning 
with very new concepts (for example, very few people were talking about chaining together LLM calls 2 years ago), as wel
l as the data efficiency advances in fine-tuning.

We concluded by discussing ML systems challenges in serving an embedd
ings API. Particularly the challenge of detecting if a request is for batch or query inference and the optimizations tha
t go into either say \~100ms latency for a query embedding or maximizing throughput for batch embeddings.

I hope you fi
nd the podcast interesting, more than happy to discuss any of these topics with you or answer any questions about the co
ntent in the podcast! Thank you so much!

YouTube: [https://www.youtube.com/watch?v=xPdyivfheqI](https://www.youtube.com
/watch?v=xPdyivfheqI)

Spotify: [https://spotifyanchor-web.app.link/e/u6XPLYfF7Hb](https://spotifyanchor-web.app.link/e/
u6XPLYfF7Hb)
```
---

     
