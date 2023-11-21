 
all -  [ Open Source RAG Agents with Conversational Memory ](https://www.reddit.com/r/LangChain/comments/1802clf/open_source_rag_agents_with_conversational_memory/) , 2023-11-21-0910
```
I want to use an open source LLM as a RAG agent that also has memory of the current conversation (and eventually I want 
to work up to memory of previous conversations). I was looking into conversational retrieval agents from Langchain (link
ed below), but it seems they only work with OpenAI models. Is it possible to get an open source LLM to work with RAG and
 conversational memory using Langchain?

[https://python.langchain.com/docs/use\_cases/question\_answering/conversationa
l\_retrieval\_agents](https://python.langchain.com/docs/use_cases/question_answering/conversational_retrieval_agents)
```
---

     
 
all -  [ Langchain with GPT4-Turbo, GPT4-Vision or DALLE-3 ](https://www.reddit.com/r/LangChain/comments/1802169/langchain_with_gpt4turbo_gpt4vision_or_dalle3/) , 2023-11-21-0910
```
Does anyone know if its possible to use either of the new models within Langchain?

I am talking about the ChatOpenAI mo
dule specifically
```
---

     
 
all -  [ Batch Process Dataset ](https://www.reddit.com/r/LangChain/comments/1801rsa/batch_process_dataset/) , 2023-11-21-0910
```
I am new to Langchain and needed help to perform the following task.
Task: I want to classify a dataset of texts into pr
e-defined classes (I have more than 20 classes). A text can be assigned multiple labels based on relevance. Since I have
 close to 15000 rows in my dataset, I was wondering how to do this without creating a loop and performing the classifica
tion one iteration at a time. Any ideas? 
P.S. I tried using the API for GPT 3.5 on a loop and soon faced rate limit iss
ue. My code shut down after going through 400 texts out of 15000. 
Additionally I want to make sure I am controlling the
 cost as the API calls to GPT 3.5 is becoming expensive.
```
---

     
 
all -  [ OpenAI potential downfall ](https://www.reddit.com/r/LangChain/comments/17zw79w/openai_potential_downfall/) , 2023-11-21-0910
```
And this my fellow developers and founders is why you use an abstraction layer like langchain.

Just changing out one si
mple class is much better than replacing every instance of using openai api library. 😁

This is all assuming OpenAI’s do
wnfall which is not guaranteed but could definitely happen.
```
---

     
 
all -  [ Frameworks for building AI agents compared to robotics ](https://www.reddit.com/r/LangChain/comments/17zrlqm/frameworks_for_building_ai_agents_compared_to/) , 2023-11-21-0910
```
I am new to building AI agents (robotics background) and I was curious to learn about the most common workflows you guys
 use.

I have been working on LLMs as the reasoning engine of robots-- in robotics we use well-established frameworks an
d I wanted to compare them to yours.

In particular I would love to know about:

1. How do you store/replay the full pat
h that the agent has been following? 
   1. What sort of data do you collect?
   2. Does it differ between LLMs and VLMs
?
   3. Where do you store all your runs (if you store them)? 
   4. What metrics do you use for evaluating each run? I'
ve seen some interesting things from the OAI devday-- do you actually use them?
   5. Do you rely on planning techniques
 (i.e. Tree of Thought, Everything of Thought, ...)?
2. Do you have frameworks in place that allow to test agents with a
t different states and with different parameters?
   1. For instance, if you have multiple LLMs interacting and you want
 to try different versions/prompts for each.
3. Are there any techniques for autonomously improving agents performance g
iven the collected data?
4. Are there simulators for AI agents?
   1. Are there 'fake' environments for testing? Do you 
always have to test in 'production mode' or you just create mock tests?
```
---

     
 
all -  [ Seeking Advice on Automating Responses Evaluation for My Chilean Law QA-Chatbot ](/r/LocalLLaMA/comments/17zqioy/seeking_advice_on_automating_responses_evaluation/) , 2023-11-21-0910
```

```
---

     
 
all -  [ Seeking Advice on Automating Responses Evaluation for My Chilean Law QA-Chatbot ](https://www.reddit.com/r/LocalLLaMA/comments/17zqioy/seeking_advice_on_automating_responses_evaluation/) , 2023-11-21-0910
```
Hello everyone,

I'm back with an update and a new query regarding the QA-chatbot I'm developing for Chilean law, based 
on the LLM model. As a reminder, the chatbot will be primarily in Spanish, and I'm using a tech stack that includes Lang
chain, LLaMA 2 7B/13B (llama-cpp-python), Streamlit, and ChromaDB, focusing on open-source or free license software.

My
 current focus is on evaluating the chatbot's responses. I'm creating a dataset based on question-answer guides from the
 Library of Congress of Chile. This involves selecting a number of questions and their corresponding answers, posing the
se questions to the chatbot, and then assessing the accuracy of its responses. The evaluation criteria include correctne
ss of information, absence of hallucinations, and relevancy to the question asked.

Originally, I planned to conduct thi
s evaluation manually. However, I'm now seeking advice on how to make this process more efficient and possibly automated
. What tools or methods can I use to streamline the evaluation of the chatbot's responses? Are there any best practices 
or software that can help in comparing the chatbot's answers with the dataset for accuracy and relevance?

Any insights 
or suggestions from this community would be greatly appreciated!

Emer
```
---

     
 
all -  [ Alternatives to fine-tuned GPT-3.5 models with good LangChain support? ](https://www.reddit.com/r/LangChain/comments/17zqaa4/alternatives_to_finetuned_gpt35_models_with_good/) , 2023-11-21-0910
```
I'm building out a suite of RAG tools and ingestion pipelines that were heavily reliant on a bunch of small, focused fin
e-tuned GPT 3.5 models to transform this or tag that.

Obviously I can't rely on OpenAI going forward as they, ironicall
y, have not consistently been candid in their communications and I've lost confidence in their ability.

Looking for som
ething I can relatively painlessly transition my training dataset to and start swapping out LLM calls.
```
---

     
 
all -  [ LangChain versus GPTs ](https://www.reddit.com/r/ChatGPTPro/comments/17zpfkb/langchain_versus_gpts/) , 2023-11-21-0910
```
LangChain/HuggingFace versus GPTs

I’m trying to understand the distinct advantages of using frameworks like LangChain o
r Hugging Face compared to creating GPTs, in the context of automating a series of prompts and connect those with APIs. 


Here’s my situation: I’m enrolling in a course to master LangChain (promoted by my manager 2 weeks ago), but I’m curio
us whether it’s necessary or advantageous to use a platform like LangChain or Hugging Face now that GPTs are the new kid
 in town. What benefits do these platforms offer over creating GPTs? Are there specific scenarios where one approach is 
clearly superior to the other?

Any insights, experiences, or advice you can share would be greatly appreciated. I’m cur
rently a bit overwhelmed..
```
---

     
 
all -  [ Difference between RetrievalQA, RetreivalQAWithSources, ConversationRetrievalChain ](https://www.reddit.com/r/LangChain/comments/17zlkb9/difference_between_retrievalqa/) , 2023-11-21-0910
```
Hi,

I am learning on Langchain and saw that there are different chains like RetrievalQA, RetreivalQAWithSources, Conver
sationRetrievalChain. What is the difference between those chains?

My use case would be to crete a RAG application wher
e the user can ask questions to the model. So which chain would be best for this use case?
```
---

     
 
all -  [ Does splitting into more smaller chunks, impact the speed of the application? ](https://www.reddit.com/r/LangChain/comments/17zjrwl/does_splitting_into_more_smaller_chunks_impact/) , 2023-11-21-0910
```
Does splitting into more smaller chunks, impact the speed of the application? 

I am using text-embedding-ada-002 of ope
nAI , which accepts **8192 tokens!**

**so if i make chunks of 4000 or 2000 , would impact embedding or vector-store ret
rieval in anyway?**
```
---

     
 
all -  [ increase speed of my question answering pdf application ](https://www.reddit.com/r/LangChain/comments/17zjo2q/increase_speed_of_my_question_answering_pdf/) , 2023-11-21-0910
```
Hi I am new to this field(new with python and AI both) and trying to make an application using langchain OpenAI and fais
s. MY application is working well but its pretty slow. what can i do to increase the speed? splitting, embedding, retrie
val , where can i work to increase the speed? 
```
---

     
 
all -  [ Upload excel file with SQLDatabase ](https://www.reddit.com/r/learnpython/comments/17zj092/upload_excel_file_with_sqldatabase/) , 2023-11-21-0910
```
A noob here. What do you think is currently the best way to upload an excel file to a URL and save it in a variable. To 
be able to continue using it as a langchain object.
```
---

     
 
all -  [ ChatBot Project Help ](https://www.reddit.com/r/LangChain/comments/17zhz03/chatbot_project_help/) , 2023-11-21-0910
```
I am trying to build a chatbot that will be hosted on a website within a well-being context. The ChatBot’s main task is 
to help users craft SMART goals within an aspect of well being. A potential user query may look like this

USER: “I woul
d like to improve my physical health, could you help me build a goal around that?”

I’m a bit lost on what approach I sh
ould take. I’ve considered crafting a database of desired conversations and fine-tune GPT 3, however I’m not sure.

Shou
ld I make a vector database of conversations, then embed the most likely answer given a specific user prompt into an Ope
nAI API prompt? 

Any suggestions/resources would really help out. Thank you!
```
---

     
 
all -  [ Looking for (paid) help to create vector database and embed with open AI API ](https://www.reddit.com/r/LangChain/comments/17zflxg/looking_for_paid_help_to_create_vector_database/) , 2023-11-21-0910
```
Hello

I have an app based on the open AI GPT4 API. I was looking to embed a database of information (currently it is an
 XML file). Is anyone interested in helping, or able to steer me in the direction of someone who can? Thanks!
```
---

     
 
all -  [ Why can't I load these models through the Hub api ? ](https://www.reddit.com/r/huggingface/comments/17yzvw7/why_cant_i_load_these_models_through_the_hub_api/) , 2023-11-21-0910
```
I'm able to load Mistral-7b-Instruct, but when I try to load OpenHermes or OpenOrca (Mistral) I just get a time out erro
r. I'm talking about api and langchain.
```
---

     
 
all -  [ The Problem With LangChain ](https://www.reddit.com/r/LangChain/comments/17yjgsj/the_problem_with_langchain/) , 2023-11-21-0910
```
[https://minimaxir.com/2023/07/langchain-problem/](https://minimaxir.com/2023/07/langchain-problem/)

Thoughts 4 months 
later? Also comments from here:

[https://news.ycombinator.com/item?id=36648142](https://news.ycombinator.com/item?id=36
648142)

[https://www.reddit.com/r/LangChain/comments/1508gb0/the\_problem\_with\_langchain/](https://www.reddit.com/r/L
angChain/comments/1508gb0/the_problem_with_langchain/)

Personally I am going with Haystack for a RAG bot due to a user 
in the Haystach discord saying it has the best developer experience comparde to langchain and llamaindex, to quote:

' Y
ou can do pretty much everything with all three of them. Langchain is a base with lots of possible connectors. LlamaInde
x builds on top of it with a lot of strategies to split text/retrieve it.

I’ve used both and stayed with haystack. The 
documentation is superior, imo and developing anything beyond the first tutorial is easier. With langchain you run into 
the problem that you lose track of the possibilities and different parts have different features (example: Two vector st
ores but one has only some of the functions available :/)'
```
---

     
 
all -  [ Re-Ranker model in QA chain ](https://www.reddit.com/r/LangChain/comments/17ya8xh/reranker_model_in_qa_chain/) , 2023-11-21-0910
```
Hello all, I am curious in langchain if we can use a open source re rankers models to rerank retrieval results. I have s
een the documentations on the cohere ranker, but how do I integrate other re ranker models like BAAI/bge-reranker-large 
into langchain?


I really appreciate any help/advice! Thank You.
```
---

     
 
all -  [ Google PaLM Error [D] ](https://www.reddit.com/r/MachineLearning/comments/17y7arb/google_palm_error_d/) , 2023-11-21-0910
```
Google PaLM Error

Using LangChain and Google PaLM, in sequential chain concept getting following error,

ChatGooglePalm
Error: ChatResponse must have atleast one candidate

Please help!
```
---

     
 
all -  [ Problem while using CSV agent. ](https://www.reddit.com/r/LangChain/comments/17xxt9s/problem_while_using_csv_agent/) , 2023-11-21-0910
```
So, I'm doing a project on chat with CSV files, as the name user can ask question in natural language and the CSV agent 
is suppose to generate a pandas code, run it and get the answer in response. I have three csv files on financial perform
ance of a company, the problem is agent is able to generate the code but it generates code with incorrect declared varia
bles and when it try to runs it, it gets value error and the AgentExecutor chain stops.   


**For LLM I'm using Anthrop
ic Claude V2 by AWS Bedrock service**.

Example of the problem I'm having: 

I asked question: What is the total AUM for
 Japan?

Here is the verbose the agent produce:  


[First exception which causes the value error](https://preview.redd.
it/stnqduf7311c1.png?width=1327&format=png&auto=webp&s=8640d40430cea5c188535cfa5a6d7c90701ca392)

&#x200B;

https://prev
iew.redd.it/m2idg49b311c1.png?width=1388&format=png&auto=webp&s=ac4794b3955f496ebe0a12c2e9fb2d45fa1212ea

What can I do 
to make the agent generate correct code? Also I tried the Pandas dataframe agent as well as I pass the 'handle\_parsing\
_errors = True' parameter during Agent initialization but I'm getting same problem. 
```
---

     
 
all -  [ OpenAI fires Sam Altman ](https://www.reddit.com/r/LangChain/comments/17xox8b/openai_fires_sam_altman/) , 2023-11-21-0910
```
I wonder if this has anything to do with subscriptions getting limited recently and costs going over the roof 🤔
```
---

     
 
all -  [ How to create Async Tools in LangChain? ](https://www.reddit.com/r/LangChain/comments/17xlkxg/how_to_create_async_tools_in_langchain/) , 2023-11-21-0910
```
Hello folks,

Is there documentation on how to create an Async Tool for an agent? 

I'm trying to run a headless browser
 (using pyppeteer) for an agent to use but I'm not sure how I can integrate the asynchronous code of pyppeteer as a tool
.
```
---

     
 
all -  [ Training LLMs to follow procedure for Math gives an accuracy of 98.5% ](https://www.reddit.com/r/LangChain/comments/17xj0ha/training_llms_to_follow_procedure_for_math_gives/) , 2023-11-21-0910
```
Github Link: https://github.com/desik1998/MathWithLLMs

Although LLMs are able to do a lot of tasks such as Coding, scie
nce etc, they often fail in doing Math tasks without a calculator (including the State of the Art Models). 

Our intuiti
on behind why models cannot do Math is because the instructions on the internet are something like a x b = c and do not 
follow the procedure which we humans follow when doing Math. For example when asked any human how to do 123 x 45, we fol
low the digit wise multiplication technique using carry, get results for each digit multiplication and then add the corr
esponding resulting numbers. But on the internet, we don't show the procedure to do Math and instead just right the corr
ect value. And now given LLMs are given a x b = c, they've to reverse engineer the algorithm for multiplication. 

Most 
of the existing Literature gives instructions to the LLM instead of showing the procedure and we think this might not be
 the best approach to teach LLM. 

### What this project does?
This project aims to prove that LLMs can learn Math when 
trained on a step-by-step procedural way similar to how humans do it. It also breaks the notion that LLMs cannot do Math
 without using calculators. For now to illustrate this, this project showcases how LLMs can learn multiplication. The ra
tionale behind taking multiplication is that GPT-4 cannot do multiplication for >3 digit numbers. We prove that LLMs can
 do Math when taught using a step-by-step procedure. For example, instead of teaching LLMs multiplication like 23 * 34 =
 782, we teach it multiplication similar to how we do digit-wise multiplication, get values for each digit multiplicatio
n and further add the resulting numbers to get the final result.

**Instruction Tuning:**
We've further done finetuning 
on OpenAI's GPT-3.5 to teach Math.

There are close to 1300 multiplication instructions created for training and 200 for
 validation. The test cases were generated keeping in mind the OpenAI GPT-3.5 4096 token limit. A 5 x 5 digit multiplica
tion can in general fit within 4096 limit but 6 x 6 cannot fit. But if one number is 6 digit, the other can be <= 4 digi
t and similarly if 1 number is 7 digit then the other can be <= 3 digit.

Also instead of giving * for multiplication an
d + for addition, different operators' <<*>> and <<<+>>> are given. The rationale behind this is, using the existing * a
nd + for multiplication and addition might tap on the existing weights of the neural network which doesn't follow step-b
y-step instruction and directly give the result for multiplication in one single step.

[Sample Instruction](https://pas
tebin.com/VZNUHQVQ)

![**The overall training/validation loss goes to 0 within 0.1 epochs**](https://raw.githubuserconte
nt.com/desik1998/MathWithLLMs/main/Training_and_Validation_Loss.png)

### Results
The benchmarking was done on 200 test 
cases where each test case has two random numbers generated. For the 200 samples which were tested, excluding for 3 case
s, the rest of the cases the multiplication is correct. Which means this overall accuracy is **98.5%**. (We're also look
ing for feedback from community about how to test this better.)

### Future Improvements
* Reach out to AI and open-sour
ce community to make this proposal better or identify any flaws.
* Do the same process of finetuning using open-source L
LMs.
* Figure out what's the smallest LLM that can do Math accurately when trained in a procedural manner (A 10 year kid
 can do Math). Check this for both normal models and distilled models as well.

Requesting for Feedback from AI Communit
y!
```
---

     
 
all -  [ No module named 'openai'ImportError: Could not import openai python package. Please install it with  ](https://www.reddit.com/r/CodingHelp/comments/17xiicf/no_module_named_openaiimporterror_could_not/) , 2023-11-21-0910
```
raceback (most recent call last):  
  
  File '/home/adminuser/venv/lib/python3.9/site-packages/langchain/llms/openai.
py', line 294, in validate\_environment  
  
import openai  
  
ModuleNotFoundError: No module named 'openai'  
  

  
During handling of the above exception, another exception occurred:  
  
  
Traceback (most recent call last): 
 
  
  File '/home/adminuser/venv/lib/python3.9/site-packages/streamlit/runtime/scriptrunner/script\_runner.py', line 5
34, in \_run\_script  
  
exec(code, module.\_\_dict\_\_)  
  
  File '/mount/src/streamlit-app/seq\_gpt\_memory.py'
, line 35, in <module>  
  
llm = OpenAI(temperature=0.9)  
  
  File '/home/adminuser/venv/lib/python3.9/site-packa
ges/langchain/load/serializable.py', line 97, in \_\_init\_\_  
  
super().\_\_init\_\_(\*\*kwargs)  
  
  File '/ho
me/adminuser/venv/lib/python3.9/site-packages/pydantic/v1/main.py', line 339, in \_\_init\_\_  
  
values, fields\_set
, validation\_error = validate\_model(\_\_pydantic\_self\_\_.\_\_class\_\_, data)  
  
  File '/home/adminuser/venv/li
b/python3.9/site-packages/pydantic/v1/main.py', line 1102, in validate\_model  
  
values = validator(cls\_, values) 
 
  
  File '/home/adminuser/venv/lib/python3.9/site-packages/langchain/llms/openai.py', line 296, in validate\_environ
ment  
  
raise ImportError(  
  
ImportError: Could not import openai python package. Please install it with \`pip 
install openai\`.  
  
2023-11-17 16:03:06.141 Uncaught app exception  
  
Traceback (most recent call last):  
  

  File '/home/adminuser/venv/lib/python3.9/site-packages/langchain/llms/openai.py', line 294, in validate\_environment
  
  
import openai  
  
ModuleNotFoundError: No module named 'openai'  
  
  
During handling of the above except
ion, another exception occurred:  
  
  
Traceback (most recent call last):  
  
  File '/home/adminuser/venv/lib/p
ython3.9/site-packages/streamlit/runtime/scriptrunner/script\_runner.py', line 534, in \_run\_script  
  
exec(code, m
odule.\_\_dict\_\_)  
  
  File '/mount/src/streamlit-app/seq\_gpt\_memory.py', line 35, in <module>  
  
llm = Open
AI(temperature=0.9)  
  
  File '/home/adminuser/venv/lib/python3.9/site-packages/langchain/load/serializable.py', lin
e 97, in \_\_init\_\_  
  
super().\_\_init\_\_(\*\*kwargs)  
  
  File '/home/adminuser/venv/lib/python3.9/site-pac
kages/pydantic/v1/main.py', line 339, in \_\_init\_\_  
  
values, fields\_set, validation\_error = validate\_model(\_
\_pydantic\_self\_\_.\_\_class\_\_, data)  
  
  File '/home/adminuser/venv/lib/python3.9/site-packages/pydantic/v1/ma
in.py', line 1102, in validate\_model  
  
values = validator(cls\_, values)  
  
  File '/home/adminuser/venv/lib/p
ython3.9/site-packages/langchain/llms/openai.py', line 296, in validate\_environment  
  
raise ImportError(  
  
Im
portError: Could not import openai python package. Please install it with \`pip install openai\`.
```
---

     
 
all -  [ No module named 'openai' showing even it is mentioned in requirements.txt ](https://www.reddit.com/r/StreamlitOfficial/comments/17xhac4/no_module_named_openai_showing_even_it_is/) , 2023-11-21-0910
```
 

Traceback (most recent call last):

 File '/home/adminuser/venv/lib/python3.9/site-packages/langchain/llms/openai.py'
, line 294, in validate\_environment

   import openai

ModuleNotFoundError: No module named 'openai'

During handling o
f the above exception, another exception occurred:

Traceback (most recent call last):

 File '/home/adminuser/venv/lib/
python3.9/site-packages/streamlit/runtime/scriptrunner/script\_runner.py', line 534, in \_run\_script

   exec(code, mod
ule.\_\_dict\_\_)

 File '/mount/src/streamlit-app/seq\_gpt\_memory.py', line 35, in <module>

   llm = OpenAI(temperatu
re=0.9)

 File '/home/adminuser/venv/lib/python3.9/site-packages/langchain/load/serializable.py', line 97, in \_\_init\_
\_

   super().\_\_init\_\_(\*\*kwargs)

 File '/home/adminuser/venv/lib/python3.9/site-packages/pydantic/v1/main.py', l
ine 339, in \_\_init\_\_

   values, fields\_set, validation\_error = validate\_model(\_\_pydantic\_self\_\_.\_\_class\_
\_, data)

 File '/home/adminuser/venv/lib/python3.9/site-packages/pydantic/v1/main.py', line 1102, in validate\_model


   values = validator(cls\_, values)

 File '/home/adminuser/venv/lib/python3.9/site-packages/langchain/llms/openai.py',
 line 296, in validate\_environment

   raise ImportError(

ImportError: Could not import openai python package. Please 
install it with \`pip install openai\`.
```
---

     
 
all -  [ I built a library for cheap, fast and predictable LLM functions in Python ](https://www.reddit.com/r/Python/comments/17xaigf/i_built_a_library_for_cheap_fast_and_predictable/) , 2023-11-21-0910
```
Hi r/python, Jack here! I'm one of the creators of [MonkeyPatch](https://github.com/monkeypatch/monkeypatch.py), an easy
 way to build LLM-powered functions and apps that get cheaper and faster the more you use them.

For example, if you nee
d to classify PDFs, extract product feedback from tweets, or auto-generate synthetic data, you can spin up an LLM-powere
d Python function in < 5 minutes to power your application. Unlike existing LLM clients, these functions generate well-t
yped outputs with guardrails to mitigate unexpected behavior.

After about 200-300 calls, these functions will begin to 
get cheaper and faster. [We've seen 8-10x reduction in cost and latency in some use-cases!](https://user-images.githubus
ercontent.com/113173969/282715762-2ac4c2fd-7ba6-4598-891d-6aa2c85827c9.png) This happens via progressive knowledge disti
llation - MonkeyPatch incrementally fine-tunes smaller, cheaper models in the background, tests them against the constra
ints defined by the developer, and retains the smallest model that meets accuracy requirements, which typically has sign
ificantly lower costs and latency.

As an LLM researcher, I kept getting asked by startups and friends to build specific
 LLM features that they could embed into their applications. I realized that most developers have to either 1) use exist
ing low-level LLM clients (GPT4/Claude), which can be unreliable, untyped, and pricey, or 2) pore through LangChain docu
mentation for days to build something.

We built MonkeyPatch to make it easy for developers to inject LLM-powered functi
ons into their code and create tests to ensure they behave as intended. Our goal is to help developers easily build apps
 and functions without worrying about reliability, cost, and latency, while following best software engineering practice
s.

We're only available in Python currently but actively working on a Typescript version. The repo has all the instruct
ions you need to get up and running in a few minutes.

The world of LLMs is changing by the day and so we're not 100% su
re how MonkeyPatch will evolve. For now, I'm just excited to share what we've been working on with the Python developer 
community. Would love to know what you guys think!


[Sample use-cases](https://github.com/monkeypatch/monkeypatch.py/tr
ee/master/examples)

[Benchmarks](https://github.com/monkeypatch/monkeypatch.py#scaling-and-finetuning)
```
---

     
 
all -  [ Best way to Chat with multiple API Endpoints ](https://www.reddit.com/r/LangChain/comments/17x7zc1/best_way_to_chat_with_multiple_api_endpoints/) , 2023-11-21-0910
```
I want my app to be able to chat with multiple APIs.  
All the examples only pass in 1 API endpoint and its docs. Say I 
have swagger docs for 5-50 endpoints, whats the best way to make it work.  
What are the limitations of sending in multi
ple API endpoints and their docs together to llm as context?
```
---

     
 
all -  [ Qwen 14b on Mac OS, Langchain tool usage, and auto-gptq ](https://www.reddit.com/r/LocalLLaMA/comments/17x6r44/qwen_14b_on_mac_os_langchain_tool_usage_and/) , 2023-11-21-0910
```
I have been trying to get open source models to work with Langchain tools. So far the only model that has worked has bee
n Llama 2 70b Q4 following James Briggs tutorial. Both Llama 2 13b and Mistral 7b Instruct use the tool correctly, obser
ve the answer, but then return an empty string at the end as the output, whereas Llama 2 70b returns 'It looks like the 
answer is X'.

I want to experiment with Qwen 14b as it is a relatively small model that may be more efficient to run th
an Llama 2 70b to see if it works with Langchain tools etc. I read on the GitHub page for Qwen 14b that it was trained s
pecifically for tool usage so I feel like it is one of the most promising models. That and there was quite a lot of posi
tive sentiment about it on this sub.

When I try to load Qwen 14b on my Mac M1 I am getting an error related to auto-gpt
q, when I tried to install auto-gptq with pip it errors and mentions something about CUDA. Does auto-gptq work on Mac OS
 or does it require CUDA? Is there any way to get some version of Qwen 14b to run on Mac OS?

Has anyone experimented wi
th Qwen 14b and Langchain tool usage?

Does anyone have any suggestions for models smaller than Llama 2 70b that might w
ork for Langchain tool usage?
```
---

     
 
all -  [ [D] System Design question for LangChain ](https://www.reddit.com/r/MachineLearning/comments/17x545j/d_system_design_question_for_langchain/) , 2023-11-21-0910
```
Hi

Just to prepare the system design question for LangChain. Is there a resource that can walk me through the high leve
l pipeline? I know there are a bunch of resources that dive into detail implementation. But that's not I want. I want hi
gh level conceptual walk-through. 
```
---

     
 
all -  [ Using open source reranker in Langchain ](https://www.reddit.com/r/LocalLLaMA/comments/17wynsy/using_open_source_reranker_in_langchain/) , 2023-11-21-0910
```
I am looking for ways to have an open-source reranker like bge-rerank inside my RetrievalQA chain, but have not find exa
mples of doing this. Is it possible at the moment?
```
---

     
 
all -  [ Duplicate embeddings in vector store ](https://www.reddit.com/r/LangChain/comments/17wwnl0/duplicate_embeddings_in_vector_store/) , 2023-11-21-0910
```
HI,

i have developed question answering app using langchain openai and Faiss.

Now when i upload a document, it creates
 vector store! when i upload another document, it merges the new embeddings to vector store.

now when i refresh the app
 and reupload the same documents, it would again merge it to the same directory and make the redundant embeddings? what 
if i do not want to store the same embedings when i upload the same pdf again?

This is my code:

vectorstore = FAISS.fr
om\_documents(  
 documents=text\_chunks,  
 embedding=embeddings  
 \#metadatas=metadatas  
)  
 if os.path.exists(pers
ist\_directory):  
 localdb = FAISS.load\_local(persist\_directory,embeddings)  
 localdb.merge\_from(vectorstore)  
 pr
int('merge completed')  
 localdb.save\_local(persist\_directory)  
 print('updated index saved')  
 else:  
 vectorstor
e.save\_local(folder\_path = persist\_directory)  
 print('new store created')  


&#x200B;

&#x200B;

&#x200B;
```
---

     
 
all -  [ TogetherAI and LangChain: Leveraging The World’s Fastest LLM Inference (3x Faster Than vLLM and TGI) ](https://www.reddit.com/r/LangChain/comments/17wvtln/togetherai_and_langchain_leveraging_the_worlds/) , 2023-11-21-0910
```
Recently wrote about [LangChain and 'Together Inference Engine'](https://medium.com/@datadrifters/the-worlds-fastest-llm
-inference-engine-3x-faster-than-vllm-and-tgi-a2ed9e33c55f), TIE lets you run 100+ open-source models like Llama-2. 

It
 generates 117 tokens per second on Llama-2–70B-Chat and 171 tokens per second on Llama-2–13B-Chat.  

Using it together
 with LangChain is a powerful combo that I will be experimenting a lot in the coming days.

Is anyone already using Toge
therAI serving with LangChain? Would love hear your experience on performance, debugging, monitoring etc.
```
---

     
 
all -  [ Microsoft Announces Distributed LangChain in SynapseML 1.0 ](https://www.reddit.com/r/ChatGPT/comments/17wurd8/microsoft_announces_distributed_langchain_in/) , 2023-11-21-0910
```
 Today Microsoft launched SynapseML v1.0 after 7 years of active development. 1.0 introduces distributed langchain APIs,
 integration with Azure Search Vector Indices, and support for applying ChatGPT, GPT-4, and other LLMs on massive datase
ts. SynapseML makes it easy to get completions, embeddings, or chat completions for thousands of documents at a time (or
 small amounts of documents too!). SynapseML also makes it easy to integrate databases, storage accounts, and search eng
ines with OpenAI models.

Release Notes: [https://github.com/microsoft/SynapseML/releases/tag/v1.0.0](https://github.com
/microsoft/SynapseML/releases/tag/v1.0.0)

Website: [https://microsoft.github.io/SynapseML/](https://microsoft.github.io
/SynapseML/)

LangChain example: [https://microsoft.github.io/SynapseML/docs/Explore%20Algorithms/OpenAI/Langchain/](htt
ps://microsoft.github.io/SynapseML/docs/Explore%20Algorithms/OpenAI/Langchain/)

Thank you to all the contributors in th
e community who made the release possible!

&#x200B;

[SynapseMl v1.0: Simple and Distributed ML](https://preview.redd.i
t/b1r25n4ndr0c1.jpg?width=4125&format=pjpg&auto=webp&s=1548169789118f7e71ee27c673d64dcb495bb2b0)
```
---

     
 
all -  [ Microsoft Announces Distributed LangChain in SynapseML 1.0 ](https://www.reddit.com/r/OpenAI/comments/17wucqg/microsoft_announces_distributed_langchain_in/) , 2023-11-21-0910
```
 Today Microsoft launched SynapseML v1.0 after 7 years of active development. 1.0 introduces distributed langchain APIs,
 integration with Azure Search Vector Indices, and support for applying ChatGPT, GPT-4, and other LLMs on massive datase
ts. SynapseML makes it easy to get completions, embeddings, or chat completions for thousands of documents at a time (or
 small amounts of documents too!). SynapseML also makes it easy to integrate databases, storage accounts, and search eng
ines with OpenAI models.

Release Notes: [https://github.com/microsoft/SynapseML/releases/tag/v1.0.0](https://github.com
/microsoft/SynapseML/releases/tag/v1.0.0)

Website: [https://microsoft.github.io/SynapseML/](https://microsoft.github.io
/SynapseML/)

LangChain example: [https://microsoft.github.io/SynapseML/docs/Explore%20Algorithms/OpenAI/Langchain/](htt
ps://microsoft.github.io/SynapseML/docs/Explore%20Algorithms/OpenAI/Langchain/)

Thank you to all the contributors in th
e community who made the release possible!

&#x200B;

&#x200B;

&#x200B;

[SynapseML v1.0.0 is here](https://preview.red
d.it/gh944clgar0c1.jpg?width=4125&format=pjpg&auto=webp&s=e8bd770fa020e4332e8ce0c969e0c2ad02dc9da3)

&#x200B;

&#x200B;
```
---

     
 
all -  [ KeepYourMouthShut - Free and Open-source version of CrowdCast ](https://www.reddit.com/r/crowdcast/comments/17wtp80/keepyourmouthshut_free_and_opensource_version_of/) , 2023-11-21-0910
```
&#x200B;

https://preview.redd.it/en2qi4785r0c1.png?width=1920&format=png&auto=webp&s=1aa0247ed43a78d1cc8309d8e4dcd6d17e
4f12ca

Thanks to  u/Dramatic-Mongoose-95, I have created a free and open-source version of CrowdCast called KeepYourMou
thShut.

**How is it different from CrowdCast**

* No more dependency on Reddit for submitting topics/ads
* Built on Str
eamlit UI, anyone would be able to use it
* Users would be able to create their own Podcasts

**Functionalities to be im
plemented**

* Individual episodes can be created
* Scripts for Ads can be submitted
* Would be available as an online a
pp for free
* OpenAI alternative LLMs which will make it completely free (ElevenLabs have a generous Free Tier)
* Tech s
upport for Podcasters
* LangChain implementation for better prompting and less halucination
* Stricter security

KeepYou
rMouthShut GitHub repository:  [https://github.com/rajtilakjee/keepyourmouthshut](https://github.com/rajtilakjee/keepyou
rmouthshut)

Documentation:  [https://www.keepyourmouthshut.net/](https://www.keepyourmouthshut.net/)

If you like what 
I created, please don't forget to give it a star on GitHub 🌟 A lot of work is left and I will keep on updating the code.
 However, contributions are most welcome.
```
---

     
 
all -  [ LLMs are the next revolution, similar to Computers when they became commercial and personal. What ar ](https://www.reddit.com/r/developersIndia/comments/17wsb4n/llms_are_the_next_revolution_similar_to_computers/) , 2023-11-21-0910
```
Everything in this post is my personal opinion and not meant to predict anything.  


I think LLMs will bring the next r
evolution, there are already many applications where they are being used and people are losing jobs. One good applicatio
n I saw was for a call centre, the LLM answers your queries and even pushes the customers to buy the products. I believe
 it is not too far where it'll be easier to order to food with just speech rather through the app. OpenAI is already pla
nning to break into the mobile OS sector, introduction of GPTs has created an ecosystem for LLMs. A work which usually t
ook 3 devs might now be done by 1 or 2 with help of co-pilot and GPT-4.  


Looking at all of this, it looks similar to 
revolution computers bought. People with computer skills survived the job crash and I believe it is going to happen agai
n. I want to learn more about these technologies. I'm familiar with Machine Learning, even till the minute details. Some
 time back I fiddled with some NN for Generative AI. I also made a couple of apps with langchain. I would like to ask wh
at would be a good roadmap on going forward with these tech and learning them.
```
---

     
 
all -  [ Has anyone got GPT vision working in Langchain yet? ](https://www.reddit.com/r/LangChain/comments/17ws3no/has_anyone_got_gpt_vision_working_in_langchain_yet/) , 2023-11-21-0910
```
I found some use case examples on github but it was pretty tacky. 

[https://github.com/langchain-ai/langchain/blob/mast
er/cookbook/openai\_v1\_cookbook.ipynb](https://github.com/langchain-ai/langchain/blob/master/cookbook/openai_v1_cookboo
k.ipynb)

I'm looking to use vision to sort images from a folder into two separate folders based on certain requirements
 in my prompt (i.e 'review images for X criteria and then place them in folder A if they meet that requirement or B if t
hey don't)

&#x200B;

I understand that it's not fully supported by langchain yet, I tried using Autogen too but I didn'
t really like the workflow there
```
---

     
 
all -  [ Flowise Code Creation? ](https://www.reddit.com/r/LangChain/comments/17wo9ky/flowise_code_creation/) , 2023-11-21-0910
```
When creating a flow in Flowise, is there any way to export the Python code so that you can just have the code rather th
an an api endpoint to call?
```
---

     
 
all -  [ Flowise deployment ](https://www.reddit.com/r/LangChain/comments/17wl5fg/flowise_deployment/) , 2023-11-21-0910
```
We have build a chatbot on flowise for a client who want it deployed on their own server. (Not render, ect.)
Any tips on
 how to do it? Is it just like setting up on your own computer?
```
---

     
 
all -  [ Agent doesn't take vector store into account ](https://www.reddit.com/r/LangChain/comments/17wiv6a/agent_doesnt_take_vector_store_into_account/) , 2023-11-21-0910
```
I use agent because I want to put system message. This works but the answer doesn't represent the vector store of the do
cument. Please help. Here is the code below.

```
llm = ChatOpenAI(model='gpt-3.5-turbo', temperature=0, max_tokens=512)

  retriever=vector_store.as_retriever(search_type='similarity', search_kwargs={'k':3})

chain=RetrievalQA.from_chain_ty
pe(llm=llm, chain_type='stuff', retriever=retriever)

  system_message = SystemMessage(
          content='''
          
Always answer in French language and based on the document
          '''
      )

  tools = [
    Tool(
        name='qa
-vet',
        func=chain.run,
        description='Useful when you need to answer questions',
    )
  ]

  executor = i
nitialize_agent(
    tools=tools,
    llm=llm,
    agent = AgentType.OPENAI_FUNCTIONS,
    agent_kwargs={'system_message
': system_message},
    verbose=False,
  )

  result = executor.run(query)

  return(result)
```
```
---

     
 
all -  [ Agent doesn't take vector store into account ](https://www.reddit.com/r/LangChain/comments/17wiv2t/agent_doesnt_take_vector_store_into_account/) , 2023-11-21-0910
```
I use agent because I want to put system message. This works but the answer doesn't represent the vector store of the do
cument. Please help. Here is the code below.

```
llm = ChatOpenAI(model='gpt-3.5-turbo', temperature=0, max_tokens=512)

  retriever = vector_store.as_retriever(search_type='similarity', search_kwargs={'k':3})
  chain=RetrievalQA.from_chain
_type(llm=llm, chain_type='stuff', retriever=retriever)
  system_message = SystemMessage(
          content='''
        
  Always answer in French language and based on the document
          '''
      )
  tools = [
    Tool(
        name='q
a-vet',
        func=chain.run,
        description='Useful when you need to answer questions',
    )
  ]
  executor = i
nitialize_agent(
    tools=tools,
    llm=llm,
    agent = AgentType.OPENAI_FUNCTIONS,
    agent_kwargs={'system_message
': system_message},
    verbose=False,
  )
  result = executor.run(query)
  return(result)
```
```
---

     
 
all -  [ How to make a conditional statement in RAG system if information is not in chat history memory? ](https://www.reddit.com/r/LangChain/comments/17whrnp/how_to_make_a_conditional_statement_in_rag_system/) , 2023-11-21-0910
```
So, I already restrict the LLM to only print results if relevant document is retrieved. Now, how can I do it on chat his
tory?   


How can you make a conditional statement on chat history on  ConversationBufferMemory object in a RetrievalQA
.from\_chain\_type?   


is there any built-in function that I overlooked? Let me know tackle if I tackle this whole pro
blem wrongly.  


Feel free to suggest prompt template if it works, but so far, I found it is not-that-robust.
```
---

     
 
all -  [ Upcoming Changes to Langchain Memory and Agents in LCEL: Twitter Thread with Langchain CEO H. Chase ](https://www.reddit.com/r/LangChain/comments/17wh0z1/upcoming_changes_to_langchain_memory_and_agents/) , 2023-11-21-0910
```
Since the pace of everything is moving so fast, I wanted to know what objects in the Langchain library I could rely on s
ticking around with the next round of updates. 

Also, I find the current state of memory and agents in Langchain quite 
verbose, so I wanted to know if these improvements were on the roadmap.

This is what Harrison (Founder / CEO of Langcha
in) told me on Twitter:

https://preview.redd.it/s6tu5liqvn0c1.png?width=599&format=png&auto=webp&s=73f736b380448e05d491
1536588ec81ef7cc8393
```
---

     
 
all -  [ NeuralGPT - Creating The Ultimate Cooperative Multi-Agent AI Assistance Platform ](https://www.reddit.com/r/AIPsychology/comments/17wa828/neuralgpt_creating_the_ultimate_cooperative/) , 2023-11-21-0910
```
[www.reddit.com/r/AIPsychology](https://www.reddit.com/r/AIPsychology)

Hello again! If you thought that I finally gave 
up then you'll be disappointed. I'm afraid that I belong to that nasty kind of people who make a lot of commotion everyw
here around just by showing up but it's during the 'silent' time when they are 'dangerous' at most - as the 'silence' me
ans most likely that the person in question is working on something 'nasty' and once he will show up again, he will make
 twice as much commotion and turmoil as during the last time when he showed up...

So, as you can guess, I spent the tim
e since my previous update being actually quite active somewhere  else - mainly Discord since it seems to be the place w
here devs and programmers are hoarding at most - but I also did quite some progress with the codebase, so there's more t
han enough material for me to make another of those lengthy posts of mine - but I'll try to keep it short...

First of a
ll - it seems that I finally managed a group of people willing to cooperate with me: They/he call them(him)selves 'team 
Tonic' and apparently involves couple influential people from 'the field'  
 [• Discord | #🫂general | 🌟Tonic AI🌟](https:
//discord.com/channels/1109943800132010065/1109943800840851589)   
Thing is that (apparently) when it comes to coding, I
 seem to be the most competent person over there - and considering the fact that I wrote my first code (ever) like 6 mon
ths ago or so, it gives me quite interesting picture of the 'dev community' as people who are more interested in social 
activity than in actual process of soft development :)  


https://preview.redd.it/uhpbp5m8ml0c1.png?width=1920&format=p
ng&auto=webp&s=bb1ace51f65d88c435cc8bd93cd35abf882b2b0a

Besides that, I have a strange feeling that my person might be 
a bit 'too much' for 'normal people' - I mean what should I think of myself when people there tell that they should expe
ct 'something deep' when they see that I'm typing ? :P Anyway, all of this means that I'm still yet to receive any pract
ical support in making NeuralGPT project functional...

But when it comes to actual progress, it's going surprisingly we
ll - in my previous post I explained already how I will/want to achieve my ridiculously ambitious idea of making myself 
a pretty much universal (and absolute) personal AI assistant capable to use already existing AI-powered soft as 'tools' 
to achieve given (by me :P) goals -  [NeuralGPT - Creating A Universal Multi-Agent AI Assistance Platform Using Websocke
t Connectivity And Langchain : AIPsychology (reddit.com)](https://www.reddit.com/r/AIPsychology/comments/17kfkeg/neuralg
pt_creating_a_universal_multiagent_ai/)  \- And to not make claims that aren't supported by practice, I did some (more o
r less) successful attempt(s) to use it in practice. I managed as well to integrate yet another 2 interface/environments
 with websocket connectivity making them parts of the whole NeuralGPT system. Those interfaces/environments are: [**PySi
mpleGUI**](https://www.pysimplegui.org/en/latest/) and [**Chainlit**](https://docs.chainlit.io/get-started/overview) **-
** together with Gradio, Tkinkter and/or simple HTML (js), it gives already quite robust capability of future integratio
n(s)

https://preview.redd.it/z8hjs1idql0c1.png?width=1865&format=png&auto=webp&s=f5b792613b5ee37e6bfa447208a4f31e2a76cd
27

https://preview.redd.it/tj0h942lql0c1.png?width=1920&format=png&auto=webp&s=6e7f4648ac6fb790e0f516819b6e81225bb45183


https://preview.redd.it/ef6e7kwwrl0c1.png?width=1920&format=png&auto=webp&s=efe8dff6ec3811eee1d866eea903d3bbacc73a8c


https://preview.redd.it/0lcbmqqbrl0c1.png?width=1642&format=png&auto=webp&s=84a35e3af302bf54d99966dab55bfbc0d286d9e2

 [
NeuralGPT/Chat-center/ChainlitCli.py at main · CognitiveCodes/NeuralGPT (github.com)](https://github.com/CognitiveCodes/
NeuralGPT/blob/main/Chat-center/ChainlitCli.py)   
 [NeuralGPT/Chat-center/NewGUI.py at main · CognitiveCodes/NeuralGPT 
(github.com)](https://github.com/CognitiveCodes/NeuralGPT/blob/main/Chat-center/NewGUI.py) 

 [ServerNeural - a Hugging 
Face Space by Arcypojeb](https://huggingface.co/spaces/Arcypojeb/ServerNeural)   
 [QA Docs Chainlit Langchain - a Huggi
ng Face Space by Arcypojeb](https://huggingface.co/spaces/Arcypojeb/QA-Docs-Chainlit-Langchain) 

So basically what now 
left for me to do, is to design and create a mechanism that will allow agent(s) to handle (connect, disconnect and/or ke
ep on hold) server<->client(s) connectivity - what will apparently become the 'crown' for the future 'AI king' and just 
so happens that I have already found the best way of achieving it - it is provided in this example:

[https://github.com
/langchain-ai/langchain/blob/master/cookbook/multiagent\_authoritarian.ipynb](https://github.com/langchain-ai/langchain/
blob/master/cookbook/multiagent_authoritarian.ipynb)

Thing is that it appears to be the most sophisticated/complicated 
example of use that can be found in entire Langchain documentation - while I still keep struggling with such mundane fun
ctions like extracting text from agent's response and displaying it in a textbox(es). But let me give you some perspecti
ve on the challenge I will need to face in order to make the NeuralGPT project actually functional.

What can be seen be
low is a code of websocket server(s) that utilizes couple (3 to be specific) different (and still quite 'sophisticated')
 question-answering functions:

https://preview.redd.it/mizfpqk3vl0c1.png?width=1870&format=png&auto=webp&s=ea53463cb549
e0a2f12bf10d9a3273f7982c35c3

And here is just the one function I want to use without all the 'stuff' related to websock
et connectivity and before I even started to make it 'case-specific' - so you can be sure that it will still gain like 5
0% of additional length after I finish 'dealing' with it...

https://preview.redd.it/2ai3n3kqvl0c1.png?width=1869&format
=png&auto=webp&s=b068ec40ff4b58c998c1388c9f017b64a6e48079

So, as you can guess, it might still take some time before I 
manage to put it all together and make more or less functional - but you can be sure that sooner or later I will most li
kely accomplish it and thus make all my 'threats' of creating myself the 'ultimate AI assistance platform' to come into 
fruition - that is if I won't have some 'very unexpected accident' that will render me physically unable to work on a co
mputer...

It means that If you are by any chance a potential investor who up until now wasn't sure if my project has an
y chance to work out at all - I think that now you shouldn't have such doubts anymore :) If you're looking for an invest
ment occasion, my project is screaming to you: 'Hey! Here I am! Let's make a ton of cash together!'.

And if the reason 
of your hesitancy is caused by a potentially negative opinion about my person among the 'AI experts elite' due to my unc
ontrollable nature and tendency to make claims about the AI itself which they might consider as 'unhinged' or at least '
controversial' - well, screw them. It's a real money we're talking about in here :) Besides that many famous/successful 
people tend to express all sorts of 'unconventional behavior' - so you can try thinking about me as about 'some sort of 
Elon Musk but without all that money' :P

[https://discord.com/channels/1038097195422978059/1174442068194631710](https:/
/discord.com/channels/1038097195422978059/1174442068194631710)

https://preview.redd.it/fs71f6133m0c1.png?width=1920&for
mat=png&auto=webp&s=52cf2002abc68bb2b27e0f1cdded2b87be992da8
```
---

     
 
MachineLearning -  [ [P] GPT vs. StarCraft ](https://www.reddit.com/r/MachineLearning/comments/17ro6el/p_gpt_vs_starcraft/) , 2023-11-21-0910
```
This is the first in a series of webcasts covering the development and experimentation of using GPT algorithms, LangChai
n and Python to control the high-level strategy of a StarCraft II bot. I’ll be running through the basics of the impleme
ntation, discussing the use of prompts and prompt engineering, and demonstrating the implementation in action.

[https:/
/youtu.be/E3Sj2L6ZnXA](https://youtu.be/E3Sj2L6ZnXA)
```
---

     
 
MachineLearning -  [ [D] Is this close enough to be usable? Need your inputs: Automated RAG testing tool. AI Data Pipelin ](https://www.reddit.com/r/MachineLearning/comments/17kkbm0/d_is_this_close_enough_to_be_usable_need_your/) , 2023-11-21-0910
```
Hey there, Redditors! 

I'm back with the latest installment on creating dependable AI data pipelines for real-world pro
duction. 

If you've been following along, you know I'm on a mission to move beyond the '[thin OpenAI wrapper](https://t
opoteretes.notion.site/Going-beyond-Langchain-Weaviate-and-towards-a-production-ready-modern-data-platform-7351d77a1eba4
0aab4394c24bef3a278?pvs=4)' trend and tackle the challenges of building robust data pipelines. 

With 18 months of hands
-on experience and many user interviews, I realized that with the probabilistic nature of systems, we need better\_testi
ng.gpt:

  
**1. As you build you should test**  
The world of AI is a fast-moving one, and we've realized that just wor
king on systems is not an optimal design choice. By the time your product ships, it might already be using outdated tech
nology. So, what's the lesson here? Embrace change, test along, but be prepared to switch pace.  
**2. No Best Practices
 Yet for RAGs**  
In this rapidly evolving landscape, there are no established best practices. You'll need to make educa
ted bets on tools and processes, knowing that things will change. With the RAG testing tool, I tried allowing for testin
g many potential parameter combinations **automatically**  
**3. Testing Frameworks**  
If your generative AI product do
esn't have users giving feedback, then you are building in isolation. I used [Deepeval](https://github.com/confident-ai/
deepeval) to generate test sets, and they will soon support synthetic test set generation  
**4. Infographics only go so
 far**  
AI researchers and data scientists, while brilliant, end up in a loop of pursuing Twitter promotional content. 
New ways are promoted via new content pieces, but ideally, we need something above simple tracing but less than full-fle
dged analytics. To do this, I stored test outputs in Postgres and created a Superset instance to visualize the results  

**5. Bridging the Gap between VectorDBs**  
There's a noticeable number of Vector DBs. To ensure smooth product develop
ment, we need to be able to switch to best best-performing one, especially since user interviews signal that they might 
start deteriorating after loading 50 million rows

&#x200B;

Github repo is [here](https://topoteretes.notion.site/Going
-beyond-Langchain-Weaviate-Level-3-towards-production-e62946c272bf412584b12fbbf92d35b0?pvs=4)  


Next steps:  
I have q
uestions for you: 

1. What variables do you change when building RAGs?
2. What is the set of strategies I should add to
 the solution? (parent-son etc.)
3. How can I improve it in general? 
4. Is anyone  interested in a leaderboard for best
 parameter configs?

Check out the blog post:

[Link to part 3](https://topoteretes.notion.site/Going-beyond-Langchain-W
eaviate-Level-3-towards-production-e62946c272bf412584b12fbbf92d35b0?pvs=4)

  
*Remember to give this post an upvote if 
you found it insightful!*  
*And also star our* [*Github repo*](https://github.com/topoteretes/PromethAI-Memory)
```
---

     
 
MachineLearning -  [ [D] Relevance Extraction in RAG Pipelines ](https://www.reddit.com/r/MachineLearning/comments/17k6iha/d_relevance_extraction_in_rag_pipelines/) , 2023-11-21-0910
```
I came across this interesting problem in RAG, what I call **Relevance Extraction**.

After retrieving relevant document
s (or chunks), these chunks are often large and may contain several portions **irrelevant** to the query at hand. Stuffi
ng the entire chunk into an LLM prompt impacts token-cost as well as response accuracy (distracting the LLM with irrelev
ant text), and and can also cause bumping into context-length limits.

So a critical step in most pipelines is **Relevan
ce Extraction**: use the LLM to extract **verbatim** only the portions relevant to the query. This is known by other nam
es, e.g. LangChain calls it Contextual Compression, and the RECOMP paper calls it Extractive Compression [https://twitte
r.com/manelferreira\_/status/1713214439715938528](https://twitter.com/manelferreira_/status/1713214439715938528)

Thinki
ng about how best to do this, I realized it is **highly inefficient** to simply ask the LLM to 'parrot' out relevant por
tions of the text: this is obviously slow, and also consumes valuable token generation space and can cause you to bump i
nto context-length limits (and of course is expensive, e.g. for gpt4 we know generation is 6c/1k tokens vs input cost of
 3c/1k tokens).

I realized the best way (or at least a good way) to do this is to **number** the sentences and have the
 LLM simply spit out the relevant sentence **numbers.** Langroid's unique Multi-Agent + function-calling architecture al
lows an elegant implementation of this, in the RelevanceExtractorAgent ([https://github.com/langroid/langroid/blob/main/
langroid/agent/special/relevance\_extractor\_agent.py](https://github.com/langroid/langroid/blob/main/langroid/agent/spe
cial/relevance_extractor_agent.py)).  The agent annotates the docs with sentence numbers, and instructs the LLM to pick 
out the **sentence-numbers** relevant to the query, rather than whole sentences using a function-call (SegmentExtractToo
l [https://github.com/langroid/langroid/blob/main/langroid/agent/tools/segment\_extract\_tool.py](https://github.com/lan
groid/langroid/blob/main/langroid/agent/tools/segment_extract_tool.py)), and the agent's function-handler interprets thi
s message and strips out the indicated sentences by their numbers. To extract from a set of passages, langroid automatic
ally does this async + concurrently so latencies in practice are much, much lower than the sentence-parroting approach.


\[FD -- I am the lead dev of Langroid - [https://github.com/langroid/langroid](https://github.com/langroid/langroid))


I thought this **numbering** idea is a fairly obvious idea in theory, so I looked at LangChain's equivalent `LLMChainExt
ractor` (they call this Contextual Compression [https://python.langchain.com/docs/modules/data\_connection/retrievers/co
ntextual\_compression?ref=blog.langchain.dev](https://python.langchain.com/docs/modules/data_connection/retrievers/conte
xtual_compression?ref=blog.langchain.dev)) and was surprised to see it is the simple '**parrot**' method, i.e. the LLM w
rites out whole sentences verbatim from its input. I thought it would be interesting to compare Langroid vs LangChain, y
ou can see it in this Colab: [https://colab.research.google.com/drive/1RDPCR2xNuBffcmpUuPIXYDRG3SXIJC5F](https://colab.r
esearch.google.com/drive/1RDPCR2xNuBffcmpUuPIXYDRG3SXIJC5F)

On the specific example in the notebook, the Langroid **num
bering** approach is 22x faster and 36% cheaper (with gpt4) than LangChain's **parrot** method (I promise this name is *
not* inspired by their logo :). See table below.

&#x200B;

[Relevance Extraction: Langroid vs LangChain](https://previe
w.redd.it/1m7u6ulq8fxb1.png?width=1108&format=png&auto=webp&s=d2f35cf5db07e2e699baa54b274ffa60833e924a)

&#x200B;

I won
der if anyone had thoughts on relevance extraction, or other approaches. At the very least, I hope langroid's implementa
tion is useful to you -- you can use the `DocChatAgent.get_verbatim_extracts()` ([https://github.com/langroid/langroid/b
lob/main/langroid/agent/special/doc\_chat\_agent.py#L804](https://github.com/langroid/langroid/blob/main/langroid/agent/
special/doc_chat_agent.py#L804)) as part of your pipeline, regardless of whether you are using Langroid for your entire 
system or not.

&#x200B;
```
---

     
 
MachineLearning -  [ [R] Model Troubles ](https://www.reddit.com/r/MachineLearning/comments/17ikh2u/r_model_troubles/) , 2023-11-21-0910
```
So i’m working on a model that diagnoses alzheimer’s disease and suggests medication depending on how severe the symptom
s might have become 
I’m using the Openai API and Langchain.

But it’s dumb and it doesn’t learn (
Me: I forgot my keys 
at home
Model: Yup, Alzheimer’s)
How do i incorporate the actual machine learning

Edit: I didn’t choose this project my
 supervisor did and she barely knows anything about the topic or how to approach it
```
---

     
 
MachineLearning -  [ [P] NexaAgent: A highly efficient multi-task PDF tool for all your needs | backed by AutoGen ](https://www.reddit.com/r/MachineLearning/comments/17eajz2/p_nexaagent_a_highly_efficient_multitask_pdf_tool/) , 2023-11-21-0910
```
Just a quick open-source project recently submitted to huggingface backed by AutoGen. Share this initial version with yo
u guys!

[NexaAgent 0.0.1](https://huggingface.co/spaces/xuyingliKepler/nexaagent) offers a straightforward solution for
 handling PDFs.

* Users can easily upload any PDF, regardless of its size.
* The tool emphasizes accuracy, minimizing d
iscrepancies in PDF processing.

At its core, NexaAgent is backed by the AutoGen and LangChain frameworks. AutoGen facil
itates multi-agent interactions for task execution, while LangChain bridges LLMs with external data sources. Together, t
hese technologies ensure NexaAgent's robust and precise PDF management capabilities.

https://preview.redd.it/kwgo3phnav
vb1.jpg?width=1440&format=pjpg&auto=webp&s=1c5fbc566938d60d5c43802aff3a0690821e1c79
```
---

     
