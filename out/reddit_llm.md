 
all -  [ Smart AI voice assistant + connect to the internet ](https://www.reddit.com/r/ArtificialInteligence/comments/1clxtb8/smart_ai_voice_assistant_connect_to_the_internet/) , 2024-05-07-0910
```
I continue my experiment building a smart AI voice assistant. This time I'm adding an ability to google for an answer. 


I'm using OpenAI function calling + AI assistants combined with SerpApi Google Search API. This way the AI can google f
or real-time data like, current weather, stock, etc.

Here is the full step-by-step tutorial: [https://serpapi.com/blog/
build-a-smart-ai-voice-assistant-connect-to-the-internet/](https://serpapi.com/blog/build-a-smart-ai-voice-assistant-con
nect-to-the-internet/)

\*I still wonder if I can replace OpenAI AI assistants with something else for the chat conversa
tion history. Currently exploring LangChain ecosystem.
```
---

     
 
all -  [ Does LLAMA 3 8B instruct have a system message token limit? ](https://www.reddit.com/r/LocalLLaMA/comments/1clxg2o/does_llama_3_8b_instruct_have_a_system_message/) , 2024-05-07-0910
```
I'm working on a project and wanted to test out LLama 3 8B instruct gguf using langchain+llama-cpp-python on my local ma
chine. However, it's not been a smooth ride. I had to first fix the one word 'assistant' response it gave. Now I'm notic
ing another 'bug' where it responds with incoherent texts that make no sense, if the system message token length is abov
e approx 500+ (haven't thoroughly tested to know the threshold). It is fine with much less system token input. Am I craz
y or is there some bug?
```
---

     
 
all -  [ Enhancing Local LLM's Understanding of Technical Documents ](https://www.reddit.com/r/LangChain/comments/1clui48/enhancing_local_llms_understanding_of_technical/) , 2024-05-07-0910
```
Hi

I'm currently using a code that processes a series of reports (PDF files), posing the same set of questions to every
 report. The output is a dataframe containing the responses to each question for every report. For instance, the questio
n 'Does the report explains why the amount of X decreased?' will be answered in a column of my output dataframe. So ever
y line of this column will consist of the answer for a specific report. My setup includes the use of [https://huggingfac
e.co/sentence-transformers/all-MiniLM-L6-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2) and a locall
y downloaded LLM from Hugging Face. Although the code is functional, the reports are highly technical and complex, and t
he local LLM lacks the necessary understanding of the content (I notice that when I read the answers).

I'm looking to e
nhance the LLM's comprehension by training it on additional technical documents of the same nature, hoping this will imp
rove its ability to accurately answer queries from my reports. If I've understood correctly, one approach might be to ut
ilize a RAG on the technical documents, but I'm unsure of the exact steps to implement this effectively. I've attempted 
to merge the embeddings from the downloaded 'all-MiniLM-L6-v2' model with those I generated from the technical documents
, as described here: [https://python.langchain.com/docs/integrations/retrievers/merger\_retriever/](https://python.langc
hain.com/docs/integrations/retrievers/merger_retriever/), but without success.

Could you suggest a viable strategy for 
this? Should I discard the 'all-MiniLM-L6-v2' and focus solely on embeddings derived from my technical documents? This a
pproach seems to require an extensive collection of documents, which I currently don't have.

 I've tried various other 
local LLMs (Mistral, Phi, Llama, Orca), but I encounter the same issue each time. 'Large' LLMs (Mistral e.g.) tend to ha
llucinate, while 'smaller' (Orca e.g.) LLMs often respond that they do not know.

  
Thanks
```
---

     
 
all -  [ Is my Resume bad or just the market (or both)? I've been getting pretty much no motion in the job ma ](https://i.redd.it/4epu27e3xuyc1.png) , 2024-05-07-0910
```

```
---

     
 
all -  [ problem with multiple rag questions ](https://www.reddit.com/r/LangChain/comments/1clmt84/problem_with_multiple_rag_questions/) , 2024-05-07-0910
```
hi, if i run my code for rag made with python and langchain,the firtst time everything goes well and in the second quest
ion it spits out this error:

  
raise ValueError(f'Missing some input keys: {missing\_keys}')

ValueError: Missing some
 input keys: {'context'}


```
---

     
 
all -  [ Local LLM and LangChain/lida ](https://www.reddit.com/r/LocalLLaMA/comments/1clm4e3/local_llm_and_langchainlida/) , 2024-05-07-0910
```
Hi all, I'm just getting started with playing around with LLMs. I'm trying to follow tutorials for building a CSV chatbo
t using Langchain and lida to do some analysis and visualizations. From what I can find online, both Langchain's create\
_csv\_agenet and lida require OpenAI's chatGPT. Is it possible to use these two packages with a local quantized LLM that
 I have in a .gguf format? Thanks!
```
---

     
 
all -  [ Starting out with Langchain SQL: some questions ](https://www.reddit.com/r/LangChain/comments/1clj3k0/starting_out_with_langchain_sql_some_questions/) , 2024-05-07-0910
```
Hi,

I'm relatively novice when it comes to LLMs, so my understanding is very limited. However, I came across [this YouT
ube Video ](https://youtu.be/9ccl1_Wu24Q?si=gHdxkoCE0gulV3Px)and was impressed with how simple the whole project was set
 up using Langchain and MySQL. I've been experimenting with it using a local version of our company's database, and I ha
ve this vision of developing a chatbot that can talk to our database and answer questions related to the information we 
have in our database.

I have a few questions:

1. I've read a few comments on this subreddit indicating that Langchain 
is not good for SQL. What does this mean, and why is it so?
2. One of the comments on the video critiques the use of Lan
gchain, stating that Langchain packages are not secure, due to passing database schema across third party providers. Is 
this true? My idea would be to create a chatbot for internal use, and implement it into our intranet.
3. In general, how
 beginner friendly is Langchain? I'm under the impression it's moreso compared to other models. 
4. Is Langchain the rig
ht tool for my task?

If I can provide any more context, I'd be happy to do so. Thanks in advance. 
```
---

     
 
all -  [ Is it possible to get different similarity search results with same vector database on different mac ](https://www.reddit.com/r/vectordatabase/comments/1clg3rk/is_it_possible_to_get_different_similarity_search/) , 2024-05-07-0910
```
Hi, recently while I was building a RAG Chatbot I came through an issue i.e below is the code I executed on 4 different 
machines(laptops)

    from langchain_community.embeddings import OllamaEmbeddings
    
    embedding = embeddings.Ollam
aEmbeddings(model='nomic-embed-text')
    db = FAISS.load_local('MS_VDB', embeddings=embedding,allow_dangerous_deseriali
zation=True)
    
    query = 'Recently I was diagnosed with Relapsing-onset MS and the indicated MS phenotype is Highly
 active. List the name of the drugs which can be used to treat my condition'
    
    docs = db.similarity_search(query)

    print(docs[0].page_content)

All the 4 machines use the same vector db file but in 3 machines the similarity search
 result was exactly the same but on the other one it was different even though the code was executed within a virtual en
vironment. Can anyone tell me what's the issue and how I could resolve it so that all the 4 machines give the same outpu
t.
```
---

     
 
all -  [ Is it possible to get different similarity search results with same vector database on different mac ](https://www.reddit.com/r/LangChain/comments/1clfwla/is_it_possible_to_get_different_similarity_search/) , 2024-05-07-0910
```
  
Hi, recently while I was building a RAG Chatbot I came through an issue i.e below is the code I executed on 4 differe
nt machines(laptops) 

    from langchain_community.embeddings import OllamaEmbeddings
    
    embedding = embeddings.O
llamaEmbeddings(model='nomic-embed-text')
    db = FAISS.load_local('MS_VDB', embeddings=embedding,allow_dangerous_deser
ialization=True)
    
    query = 'Recently I was diagnosed with Relapsing-onset MS and the indicated MS phenotype is Hi
ghly active. List the name of the drugs which can be used to treat my condition'
    
    docs = db.similarity_search(qu
ery)
    print(docs[0].page_content)

All the 4 machines use the same vector db file but in 3 machines the similarity se
arch result was exactly the same but on the other one it was different even though the code was executed within a virtua
l environment. Can anyone tell me what's the issue and how I could resolve it so that all the 4 machines give the same o
utput.  
 
```
---

     
 
all -  [ 'GPT to perform 10x with my private knowledge' ](https://www.reddit.com/r/LangChain/comments/1clfhnk/gpt_to_perform_10x_with_my_private_knowledge/) , 2024-05-07-0910
```
['GPT to perform 10x with my private knowledge' - Local Agentic RAG w/- PDF , Website - Here is how (youtube.com)](https
://www.youtube.com/watch?v=5ModxAjKI3w&t=915s)
```
---

     
 
all -  [ DSPy, a no prompt alternate for LangChain  ](https://www.reddit.com/r/LangChain/comments/1cldnq3/dspy_a_no_prompt_alternate_for_langchain/) , 2024-05-07-0910
```
DSPy is an alternate for LangChain, mainly for programmers to build GenAI apps without any prompt engineering by user. C
heckout this beginner friendly tutorial to know the basics of DSPy to get started : 
https://youtu.be/IiaXLP3JKr4?si=xAC
EMVC1c7c174uR
```
---

     
 
all -  [ Langchain Multi user api/app ](https://www.reddit.com/r/LangChain/comments/1clcva5/langchain_multi_user_apiapp/) , 2024-05-07-0910
```
Has anyone here tried to do a multiuser app? Does langchain support it out of the box with configuration, or is this som
ething that needs to be done on my own? It seems that loading several langchain agents takes quite a bit of time which m
eans the client would have to wait quite a bit if I recretead the agent for every request. 

I am not sure how to approa
ch this.   
I do not need message history, just stateless for now.

  
My agents are for reporting purposes at work, so 
they trigger Pandas/Excel processes which can take 30 seconds up to a 1 minute.
```
---

     
 
all -  [ Long response time for Mistral 7b ](https://www.reddit.com/r/MistralAI/comments/1clcjle/long_response_time_for_mistral_7b/) , 2024-05-07-0910
```
Hi guys, currently I am using filipealmeida/Mistral-7B-Instruct-v0.1-sharded with 4 bits quantization as my RAG model wi
th LangChain framework in Google Colab and has successfully utilize it, however the whole response time take really a lo
ng time (about 1-2 mins), and I don't sure what is happened and how to solve it. Is it the problem I am using transforme
r pipeline?
```
---

     
 
all -  [ Building simple reasoning agents without frameworks like Llamaindex or Langchain.  ](https://www.reddit.com/r/LocalLLaMA/comments/1clc6lz/building_simple_reasoning_agents_without/) , 2024-05-07-0910
```
Hi everyone, 

I have been using some LLM frameworks like langchain and Llamaindex for a few weeks and have found modera
te success. I don't like their documentation (probably because the pace at which these are evolving is too rapid) and it
 becomes a little difficult to understand their source code or code examples. 

I want to start simple- build a chat eng
ine centered around multimodal (image/text) retrieval. What I've done is I've indexed some images and their captions (us
ing CLIP embeddings) to Pinecone. I can do simple things like similarity search. I haven't used LLM frameworks at all to
 do this. I've used the pinecone and clip functions directly. I can do text to image retrieval, text to text retreival a
nd things like that.

What I want to do now is create simple 'reasoning' systems that can reason about these images. I w
ant to create a chain like structure which looks like this 

query --> retrieve similar images and captions ---> summari
ze the captions / describe the objects (run some object detection algorithm) / possibly other things etc.  

Call me a m
asochist but I don't want to use langchain or llamaindex. Can this chaining operation be performed with the bare OpenAI 
API or function calling? I hope so. I'm kinda new to this and will appreciate any help.
```
---

     
 
all -  [ langchain response in particular format ](https://www.reddit.com/r/Langchaindev/comments/1cl8hfg/langchain_response_in_particular_format/) , 2024-05-07-0910
```
how to write a prompt which does the work of greeting by introducing it self and another prompt for giving question answ
ers with memory added into it.kindly give the code and the prompt stacking approch using selfquery retrieval.
```
---

     
 
all -  [ What are your current go to libraries? ](https://www.reddit.com/r/LocalLLaMA/comments/1cl6lx3/what_are_your_current_go_to_libraries/) , 2024-05-07-0910
```
There is a lot to keep up with and I was wanting to get an idea of what people are finding useful right now. Specificall
y, programming libraries, not UI's.

EDIT  
Guess I should share as well. These are the tools I've been playing around w
ith (not really committed to use any one of them yet).

**General**

* [llama-cpp-python](https://pypi.org/project/llama
-cpp-python/)

**DSL**

* [guidance](https://github.com/guidance-ai/guidance)

**RAG Frameworks**

* [Langchain](https:/
/www.langchain.com/)
* [LlamaIndex](https://docs.llamaindex.ai/en/stable/)
* [DSPy](https://github.com/stanfordnlp/dspy)


**Model Serving**

* [Ollama](https://ollama.com/)
```
---

     
 
all -  [ What is the most proper way to develop this chatbot? ](https://www.reddit.com/r/LangChain/comments/1cl522l/what_is_the_most_proper_way_to_develop_this/) , 2024-05-07-0910
```
Hey guys! Before I begin, thanks to those that took the time to read my post and hopefully respond, it's really much app
reciated. Now onto our topic; I'm trying to build a conversation chatbot which objective is to offer to the user game re
commendations that fit different criteria and preferences that could be found in his initial query.

What I want the cha
tbot to do, is first evaluate the query, have it better understand. See if the query is on the topic of asking for game 
recommendations, or whether his input is clear enough, which in the case of them not meeting one of the requirements, ha
ve the chatbot ask from the user to input a proper one.

After making sure that his input is alright and is done with re
viewing it, make calls to various tools that rely on SerpApi. such as the Google search one for finding suitable titles 
to be chosen as candidate for the final answer and gather more additional information for each game, or the Google image
s and Youtube one for gathering multimedia content, such as games' posters and official trailers.

Once the chatbot is d
one with browsing the web in order to fetch what it needs, let it formulate a response to the user. One important functi
onality that I want present in this chatbot is that, if the user asks from the chatbot to find alternatives to some of t
he titles found in the response, it should be able to remember that response in the first to be able and apply modificat
ions to it, such as the replacing actions of certain mentioned titles with other ones.

Now that the requirements of thi
s chatbot are somewhat clear, how would you recommend me to go on developing such project? What key factors should I tak
e into consideration and make use of in order to achieve the desired results?
```
---

     
 
all -  [ LLM use case for QA and reasoning. ](https://www.reddit.com/r/LangChain/comments/1cl4mx6/llm_use_case_for_qa_and_reasoning/) , 2024-05-07-0910
```
I have a use case, where I have textual data. I have to extract information from it. Some of the data is direct and can 
be assigned directly. Others are not so-direct, like total weight, total quantity, these values are supposed to be calcu
lated after extracting individual data from the data. 

Since RAG provides contextual information, so I am planning to i
nform the LLM about the labels to be extracted. I am also planning to fine-tune Llama3 on annotations so model learns ab
out what how information extraction is actually taking place.  
  
What else can be done to improve the output performan
ce of model. 
```
---

     
 
all -  [ Do Output Parser like the JSON one, have a retry option? ](https://www.reddit.com/r/LangChain/comments/1ckzzfs/do_output_parser_like_the_json_one_have_a_retry/) , 2024-05-07-0910
```
Hi I am currently struglling with how to approach error handling with a JSON output parser. Can it do retries? I feel li
ke every output parser should just allow retry by default, because often the result can be bad for 1 - 2 requests and th
at is it.

If not then is it possible to use retryOutput parser with LCEL?
```
---

     
 
all -  [ Local model based RAG ChatBot ](https://www.reddit.com/r/LangChain/comments/1cktopp/local_model_based_rag_chatbot/) , 2024-05-07-0910
```
Hi,

We are creating a rag based ChatBot for our company but due to some infosec concerns we have to use only local llms
 and database.

Due to this reason we are not using openAI/Gemini or any API based models and instead we are using Ollam
a for our local models and using LLAMA 3 as our LLM. 

Now the issue is when we are using local Embeddings model like no
mic-embed it's not producing very good results. What should i do to overcome this issue and i have tried different local
 Embeddings model of ollama but they aren't producing very good results.
```
---

     
 
all -  [ Need help in Structured Extraction of data ](https://www.reddit.com/r/LangChain/comments/1ckt04y/need_help_in_structured_extraction_of_data/) , 2024-05-07-0910
```
Hey , I have been dabbling with a few methods to extract data from a corpus of documents in structured format and have b
een experimenting with pydantic classes and even agents. But still, I am not able to achieve the desired result. I follo
wed the Langchain documentation for extracting data but the method where we use Reference examples is not working.

To s
pecify my use case, I want to extract data from legal documents in a chronological method. Would love to get some tips/ 
ideas or your methods if you have been doing something like this. Here is a fellow company doing the same www . tryabel.
 com.

Thanks!
```
---

     
 
all -  [ Using Weaviate & Langchain together ](https://www.reddit.com/r/LangChain/comments/1ckszg1/using_weaviate_langchain_together/) , 2024-05-07-0910
```
Hey everyone,  
Does anyone have any good tutorials or blogpost about how to use weaviate as a vector store and use Lang
chain to perform activities like, creating new collections, adding document, performing similarity search etc. The offic
ial documentation from Langchain work when I perform all these actions sequentially. However, when loading the persisted
 vector store, I am unable to perform similarity search.
```
---

     
 
all -  [ Resume of a 2023 graduate targeting machine learning roles. ](https://www.reddit.com/r/developersIndia/comments/1ckrno0/resume_of_a_2023_graduate_targeting_machine/) , 2024-05-07-0910
```
Hello all, I am a 2023 graduate, I have been jobless since graduation but I have been trying hard to get a job. During t
his whole break I have not stopped and kept myself up to date with the latest technologies in machine learning and tried
 to keep busy and upskill myself.  
I have had very little success in my job search, I got a few interviews but companie
s select other candidates in the end who have more experience than me. My resume scores good on ATS but I still don't kn
ow if its good enough. 

https://preview.redd.it/kh4837sx3myc1.png?width=429&format=png&auto=webp&s=8bcd822f965d2e10488b
003ad1048b87f1f50d4c

Please help me out, any kind of feedback will be appreciated.   

```
---

     
 
all -  [ Fine tuning for Function Calling ](https://www.reddit.com/r/LangChain/comments/1ckpwg4/fine_tuning_for_function_calling/) , 2024-05-07-0910
```
Is it a good idea to fine tune a cheaper model like chatgpt 3.5 and train it on your function calling samples where the 
tool is basically a http fetch request to get data from API based on parameters in the user's query?

I am currently usi
ng gpt 4 2024 model, and the cons are 1) it's expensive 2) I have to add examples in my system prompt 3) It still fails 
at times with mapping the parameters (more than 4 different parameters such as region, duration, price etc)

I am consid
ering this but posting this to check if someone found this viable? 
```
---

     
 
all -  [ help in creating a RAG chatbot  ](https://www.reddit.com/r/LangChain/comments/1ckoupq/help_in_creating_a_rag_chatbot/) , 2024-05-07-0910
```
Hi Guy i need your help!  
  
i want to build a chatbot service that is a cartoon character that helps people with their
 body transformation journey , its has a database with relevant products, it offers products to users when they ask body
 transformation questions using the database .   
for example :  
'i want to gain weight , how do i do it ?'  
'im 178cm
 and 78kg and i want to gain 10kg '  
'if im looking to lose 5% body fat , what should i do ?'  
  
to do so i build a n
umber of chatbots each with a different exaction approach but each has its own issues and i cant find the execution that
 will satisfy me .  
  
1st approach:  
using langchain and added a custom tool , that holds the products in a vector da
tabase .  
  
the problems with this approach: it doesnt always go to the tool , sometimes it does and sometimes it does
nt .   
and i cant control it , the llm decides by itself if to look in the tool or not , this leads to unstable results
 of similar conversations   
  
2nd approach :  
i used the openai wrapper and used groq llm service , without langchain
 , were i added a custom tool , here the process is different .  
process:  
- get user input   
- created a llm call to
 determine if the function would be called by looking at the user input   
- if the function is to call then i call the 
function with the user input and get the products   
- create a llm call with a system prompt and user input plus the re
levant products   
-if the function is not to call , then ill create a llm call with a different system prompt and use o
nly the user input   
- also introduce the user and chatbot summary chat history to give the llm context   
  
the probl
ems with this approach :  
again not always it goes to the tool so its a problem , here it performs better then the firs
t approach , but i feel its hard to keep the context of the conversation and the history is getting bigger and bigger ve
ry fast and then the llm looses understanding of the user input   
  
3rd approach:  
- get user input   
- always use u
ser input to look for relevant products in the vector database  
- summary the conversation until now   
- do a llm call
 using the system prompt , user input , the relevant products , and conversation summary   
  
the problem with this app
roach :  
from all of the approaches this preforms the best but it still has issues , because i use a lot of information
 in each llm call , and i ask it to respond to the user input and use the products only if they are relevant . when the 
user wants to end the conversation and say 'thank you' or 'great' inside the llm call it gets lots of information and th
e respond misses the point , and it answers like the user is still looking for help and doesnt understand the context of
 where we are right now   
  
  
i want to know what is the best approach to create a chat bot that users can talk to , 
get relevant products for their body transformation journey , but also talk to the llm regularly and for it to respond o
nly to the relevant message . please tell me from your experience what is the best approach .   
  
i really appreciate 
any help.   
```
---

     
 
all -  [ Question on Multi lingual data ](https://www.reddit.com/r/LangChain/comments/1ckmuq2/question_on_multi_lingual_data/) , 2024-05-07-0910
```
Hi, I’m trying to build a Chat bot for our org using langchain. The knowledge base is primarily Wordpress blogs, books a
nd YouTube videos.
The YouTube videos happen to be in English and Hindi(language of India). How should I go about data i
ngestion? Should I translate the Hindi video transcripts to English and then embed them or should I embed all the transc
ripts irrespective of language using a multi lingual model from something like cohere?
```
---

     
 
all -  [ Prompt Engineering Testing Suite...? ](https://www.reddit.com/r/PromptEngineering/comments/1ckkw3t/prompt_engineering_testing_suite/) , 2024-05-07-0910
```
Hi fellow prompters, good to meet you!

I'm looking for advice. I was wondering if you were having similar issues to the
 ones I'm having:

- I want to compare and test different LLMs in one place and keep track of changes.

- I'm not really
 sure how to hook up to all these different LLM providers (openai, claude, google) API effectively 

- I'm basically won
dering if there's like a prompt testing/deployment kit that's more intuitive and simple than Galileo/Langchain.

Can you
 tell me about your guys's current tools for prompt testing and switching between different models?

I'm trying to learn
 more about other people working in this area.

Thanks :)
```
---

     
 
all -  [ 3rd year student studying CS ](https://www.reddit.com/r/resumes/comments/1ckkc7b/3rd_year_student_studying_cs/) , 2024-05-07-0910
```
I have applied to around 300-400 companies this year and have received a couple interviews but majority negative respons
es. I feel like there is something going wrong with my resume and any feedback is highly appreciated

https://preview.re
dd.it/xto1ucqarjyc1.jpg?width=850&format=pjpg&auto=webp&s=f96cc2f0c27092584961b6e8595f03fa21dac9a7


```
---

     
 
all -  [ [For Hire] I will be your AI Consultant for free  ](https://www.reddit.com/r/jobbit/comments/1ckhkcj/for_hire_i_will_be_your_ai_consultant_for_free/) , 2024-05-07-0910
```
Are you intrigued by the AI trend but unsure how it could enhance your business, leading to a sense of FOMO? Fear not! 


Let's explore how AI can seamlessly integrate into your business operations. From analyzing your processes to identifyi
ng AI opportunities, I'll provide insights into how your business can benefit. 

With expertise in diverse AI tools, fro
m no-code platforms like Voiceflow to advanced frameworks like Langchain, I'm equipped to guide you through the possibil
ities. 

Drop me a DM with your availability, and let's delve into the specifics of your business!
```
---

     
 
all -  [ Error code: 400 - {'error': {'message': '[] is too short - 'tools'', 'type': 'invalid_request_error' ](https://www.reddit.com/r/LangChain/comments/1ckd61h/error_code_400_error_message_is_too_short_tools/) , 2024-05-07-0910
```
Hey guys! I'm trying to create a conversation chatbot the specializes in offering video games recommendations based on t
he user preferences found in his input. Though, right now, when I'm trying to run it, I'm being faced with the error abo
ve, does anybody have any idea as to what the problem may be?

Also, is there any way to make sure that an execution of 
an agent does not move to the other until all the requirements are met? For e.g., I have an input agent that's tasked to
 collect the user's prompt and extract the important info from there. But how would I manage a case where the user might
 input a query that talks about something completely different?

Thank you guys!

Here is my code too:

    import os
  
  from dotenv import load_dotenv
    from langchain_openai import ChatOpenAI
    from langchain_core.messages import Hum
anMessage, BaseMessage
    from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
    from langchain
.agents import create_openai_tools_agent, Tool
    from langgraph.graph import StateGraph, END
    from typing import An
notated, Sequence, TypedDict
    import operator
    from serpapi import GoogleSearch
    
    # Load environment variab
les for API keys
    load_dotenv()
    
    # Configuration
    serpapi_key = os.getenv('SERPAPI_API_KEY')
    
    # De
fine tools using SerpAPI
    def google_search(query):
        params = {
            'engine': 'google',
            'q
': query,
            'api_key': serpapi_key,
            'num': 5
        }
        search = GoogleSearch(params)
     
   results = search.get_dict()
        return results['organic_results']
    
    def youtube_search(query):
        par
ams = {
            'engine': 'youtube',
            'search_query': query,
            'api_key': serpapi_key
        }

        search = GoogleSearch(params)
        results = search.get_dict()
        return results['video_results']
    

    def images_search(query):
        params = {
            'engine': 'google_images',
            'google_domain': 'go
ogle.com',
            'q': query,
            'api_key': serpapi_key
        }
        search = GoogleSearch(params)
  
      results = search.get_dict()
        return results['images_results']
    
    # Define tools
    search_tool = Too
l(name='google_search', description='Performs Google searches.', func=google_search)
    youtube_tool = Tool(name='youTu
be_search', description='Searches for YouTube videos.', func=youtube_search)
    images_tool = Tool(name='images_search'
, description='Searches for images on Google Images.', func=images_search)
    
    # Setup the ChatOpenAI model for con
versational interactions
    chat_model = ChatOpenAI(model='gpt-3.5-turbo-1106', temperature=0)
    
    # Define agent 
prompts
    input_agent_prompt = ChatPromptTemplate.from_messages([
        ('system', 'You are the initial contact poin
t for users. Your role is to gather information about the user's preferences and interests in video games and make sure 
you understand their requirements. In case of any ambiguity, ask for clarification or in the case of the query not being
 related to video games, ask for a different query.'),
        MessagesPlaceholder(variable_name='messages'),
        Me
ssagesPlaceholder(variable_name='agent_scratchpad'),
        ('human', '{input}')
    ])
    
    search_agent_prompt = 
ChatPromptTemplate.from_messages([
        ('system', 'Your main task is to search for game titles that best match the u
ser's interest. Use the details from the Input Agent to guide your search. Provide a list of relevant game titles.'),
  
      MessagesPlaceholder(variable_name='messages'),
        MessagesPlaceholder(variable_name='agent_scratchpad'),
    
    ('human', '{input}')
    ])
    
    details_agent_prompt = ChatPromptTemplate.from_messages([
        ('system', 'R
etrieve detailed information for each game identified by the Search Agent. Focus on obtaining the game's description, ge
nre, platform availability, developer, publisher, release date, Metacritic score if available and links to digital store
s that sell the game.'),
        MessagesPlaceholder(variable_name='messages'),
        MessagesPlaceholder(variable_nam
e='agent_scratchpad'),
        ('human', '{input}')
    ])
    
    posters_agent_prompt = ChatPromptTemplate.from_messa
ges([
        ('system', 'Your responsibility is to fetch the official posters for the games provided by the Search Agen
t. Ensure the images are high quality and relevant.'),
        MessagesPlaceholder(variable_name='messages'),
        Me
ssagesPlaceholder(variable_name='agent_scratchpad'),
        ('human', '{input}')
    ])
    
    trailers_agent_prompt 
= ChatPromptTemplate.from_messages([
        ('system', 'Obtain the official game trailers for the titles identified by 
the Search Agent. Ensure that the trailers are current and of high quality.'),
        MessagesPlaceholder(variable_name
='messages'),
        MessagesPlaceholder(variable_name='agent_scratchpad'),
        ('human', '{input}')
    ])
    
  
  recommendation_agent_prompt = ChatPromptTemplate.from_messages([
        ('system', 'You are responsible for compiling
 the outputs from all other agents into a cohesive and well-formatted response. Synthesize the game details, images, and
 trailers into a compelling presentation of game recommendations.'),
        MessagesPlaceholder(variable_name='messages
'),
        MessagesPlaceholder(variable_name='agent_scratchpad'),
        ('human', '{input}')
    ])
    
    # Create
 agents using the prompts
    input_agent = create_openai_tools_agent(chat_model, [], input_agent_prompt)
    search_age
nt = create_openai_tools_agent(chat_model, [search_tool], search_agent_prompt)
    details_agent = create_openai_tools_a
gent(chat_model, [search_tool], details_agent_prompt)
    posters_agent = create_openai_tools_agent(chat_model, [images_
tool], posters_agent_prompt)
    trailers_agent = create_openai_tools_agent(chat_model, [youtube_tool], trailers_agent_p
rompt)
    recommendation_agent = create_openai_tools_agent(chat_model, [], recommendation_agent_prompt)
    
    # Stat
e definition for agents
    class AgentState(TypedDict):
        messages: Annotated[Sequence[BaseMessage], operator.add
]
        intermediate_steps: Annotated[Sequence[BaseMessage], operator.add]
        agent_scratchpad: Annotated[Sequenc
e[BaseMessage], operator.add]
        input: str
    
    # Graph setup
    state_graph = StateGraph(schema=AgentState)

    
    # Add nodes for each agent
    state_graph.add_node('input_agent', input_agent)
    state_graph.add_node('searc
h_agent', search_agent)
    state_graph.add_node('details_agent', details_agent)
    state_graph.add_node('posters_agent
', posters_agent)
    state_graph.add_node('trailers_agent', trailers_agent)
    state_graph.add_node('recommendation_ag
ent', recommendation_agent)
    
    # Define edges to flow between agents
    state_graph.add_edge('input_agent', 'sear
ch_agent')
    state_graph.add_edge('search_agent', 'details_agent')
    state_graph.add_edge('details_agent', 'posters_
agent')
    state_graph.add_edge('posters_agent', 'trailers_agent')
    state_graph.add_edge('trailers_agent', 'recommen
dation_agent')
    state_graph.add_edge('recommendation_agent', END)
    
    # Set the entry point to start the agent w
orkflow
    state_graph.set_entry_point('input_agent')
    
    # Complete the graph
    app = state_graph.compile()
   
 
    def main():
        print('Welcome to the Game Recommendation Chatbot!')
        while True:
            user_inpu
t = input('You: ')
            if user_input.lower() == 'exit':
                print('Exiting chatbot...')
            
    break
            # Initialize the state with the necessary structures
            state = {
                'messag
es': [HumanMessage(content=user_input)],
                'agent_scratchpad': [],  # ensure this is always a list
       
         'intermediate_steps': [],  # ensure this is always initialized as a list
                'input': user_input  #
 this is your actual input string
            }
            response = app.invoke(state)
            print('Bot:', respo
nse['messages'][-1].content)
    
    if __name__ == '__main__':
        main()
    import os
    from dotenv import loa
d_dotenv
    from langchain_openai import ChatOpenAI
    from langchain_core.messages import HumanMessage, BaseMessage
 
   from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
    from langchain.agents import create_op
enai_tools_agent, Tool
    from langgraph.graph import StateGraph, END
    from typing import Annotated, Sequence, Typed
Dict
    import operator
    from serpapi import GoogleSearch
    
    
    # Load environment variables for API keys
  
  load_dotenv()
    
    
    # Configuration
    serpapi_key = os.getenv('SERPAPI_API_KEY')
    
    
    # Define tool
s using SerpAPI
    def google_search(query):
        params = {
            'engine': 'google',
            'q': query,

            'api_key': serpapi_key,
            'num': 5
        }
        search = GoogleSearch(params)
        result
s = search.get_dict()
        return results['organic_results']
    
    
    def youtube_search(query):
        params 
= {
            'engine': 'youtube',
            'search_query': query,
            'api_key': serpapi_key
        }
   
     search = GoogleSearch(params)
        results = search.get_dict()
        return results['video_results']
    
    

    def images_search(query):
        params = {
            'engine': 'google_images',
            'google_domain': 'g
oogle.com',
            'q': query,
            'api_key': serpapi_key
        }
        search = GoogleSearch(params)
 
       results = search.get_dict()
        return results['images_results']
    
    
    # Define tools
    search_tool
 = Tool(name='google_search', description='Performs Google searches.', func=google_search)
    youtube_tool = Tool(name=
'youTube_search', description='Searches for YouTube videos.', func=youtube_search)
    images_tool = Tool(name='images_s
earch', description='Searches for images on Google Images.', func=images_search)
    
    
    # Setup the ChatOpenAI mo
del for conversational interactions
    chat_model = ChatOpenAI(model='gpt-3.5-turbo-1106', temperature=0)
    
    
   
 # Define agent prompts
    input_agent_prompt = ChatPromptTemplate.from_messages([
        ('system', 'You are the init
ial contact point for users. Your role is to gather information about the user's preferences and interests in video game
s and make sure you understand their requirements. In case of any ambiguity, ask for clarification or in the case of the
 query not being related to video games, ask for a different query.'),
        MessagesPlaceholder(variable_name='messag
es'),
        MessagesPlaceholder(variable_name='agent_scratchpad'),
        ('human', '{input}')
    ])
    
    
    s
earch_agent_prompt = ChatPromptTemplate.from_messages([
        ('system', 'Your main task is to search for game titles 
that best match the user's interest. Use the details from the Input Agent to guide your search. Provide a list of releva
nt game titles.'),
        MessagesPlaceholder(variable_name='messages'),
        MessagesPlaceholder(variable_name='age
nt_scratchpad'),
        ('human', '{input}')
    ])
    
    
    details_agent_prompt = ChatPromptTemplate.from_messag
es([
        ('system', 'Retrieve detailed information for each game identified by the Search Agent. Focus on obtaining 
the game's description, genre, platform availability, developer, publisher, release date, Metacritic score if available 
and links to digital stores that sell the game.'),
        MessagesPlaceholder(variable_name='messages'),
        Messag
esPlaceholder(variable_name='agent_scratchpad'),
        ('human', '{input}')
    ])
    
    
    posters_agent_prompt 
= ChatPromptTemplate.from_messages([
        ('system', 'Your responsibility is to fetch the official posters for the ga
mes provided by the Search Agent. Ensure the images are high quality and relevant.'),
        MessagesPlaceholder(variab
le_name='messages'),
        MessagesPlaceholder(variable_name='agent_scratchpad'),
        ('human', '{input}')
    ])

    
    
    trailers_agent_prompt = ChatPromptTemplate.from_messages([
        ('system', 'Obtain the official game tr
ailers for the titles identified by the Search Agent. Ensure that the trailers are current and of high quality.'),
     
   MessagesPlaceholder(variable_name='messages'),
        MessagesPlaceholder(variable_name='agent_scratchpad'),
       
 ('human', '{input}')
    ])
    
    
    recommendation_agent_prompt = ChatPromptTemplate.from_messages([
        ('sy
stem', 'You are responsible for compiling the outputs from all other agents into a cohesive and well-formatted response.
 Synthesize the game details, images, and trailers into a compelling presentation of game recommendations.'),
        Me
ssagesPlaceholder(variable_name='messages'),
        MessagesPlaceholder(variable_name='agent_scratchpad'),
        ('hu
man', '{input}')
    ])
    
    
    # Create agents using the prompts
    input_agent = create_openai_tools_agent(chat
_model, [], input_agent_prompt)
    search_agent = create_openai_tools_agent(chat_model, [search_tool], search_agent_pro
mpt)
    details_agent = create_openai_tools_agent(chat_model, [search_tool], details_agent_prompt)
    posters_agent = 
create_openai_tools_agent(chat_model, [images_tool], posters_agent_prompt)
    trailers_agent = create_openai_tools_agen
t(chat_model, [youtube_tool], trailers_agent_prompt)
    recommendation_agent = create_openai_tools_agent(chat_model, []
, recommendation_agent_prompt)
    
    
    # State definition for agents
    class AgentState(TypedDict):
        mess
ages: Annotated[Sequence[BaseMessage], operator.add]
        intermediate_steps: Annotated[Sequence[BaseMessage], operat
or.add]
        agent_scratchpad: Annotated[Sequence[BaseMessage], operator.add]
        input: str
    
    
    # Grap
h setup
    state_graph = StateGraph(schema=AgentState)
    
    
    # Add nodes for each agent
    state_graph.add_nod
e('input_agent', input_agent)
    state_graph.add_node('search_agent', search_agent)
    state_graph.add_node('details_a
gent', details_agent)
    state_graph.add_node('posters_agent', posters_agent)
    state_graph.add_node('trailers_agent'
, trailers_agent)
    state_graph.add_node('recommendation_agent', recommendation_agent)
    
    
    # Define edges to
 flow between agents
    state_graph.add_edge('input_agent', 'search_agent')
    state_graph.add_edge('search_agent', 'd
etails_agent')
    state_graph.add_edge('details_agent', 'posters_agent')
    state_graph.add_edge('posters_agent', 'tra
ilers_agent')
    state_graph.add_edge('trailers_agent', 'recommendation_agent')
    state_graph.add_edge('recommendatio
n_agent', END)
    
    
    # Set the entry point to start the agent workflow
    state_graph.set_entry_point('input_ag
ent')
    
    
    # Complete the graph
    app = state_graph.compile()
    
    
    def main():
        print('Welcom
e to the Game Recommendation Chatbot!')
        while True:
            user_input = input('You: ')
            if user_
input.lower() == 'exit':
                print('Exiting chatbot...')
                break
            # Initialize the 
state with the necessary structures
            state = {
                'messages': [HumanMessage(content=user_input)]
,
                'agent_scratchpad': [],  # ensure this is always a list
                'intermediate_steps': [],  # e
nsure this is always initialized as a list
                'input': user_input  # this is your actual input string
     
       }
            response = app.invoke(state)
            print('Bot:', response['messages'][-1].content)
    
    

    if __name__ == '__main__':
        main()
```
---

     
 
all -  [ Is there any agent that can do RAG across my GDrive, Gmail, & GitHub? ](https://www.reddit.com/r/LangChain/comments/1ckbmf0/is_there_any_agent_that_can_do_rag_across_my/) , 2024-05-07-0910
```
Not looking to build my own system per se, just looking for something open source (doesn't have to use langchain) that c
an use tools (code interp, web browsing, make google drive files, sending emails, replying to github issues) and perform
 RAG across all my google drive documents, emails, and code.

Apologies if this is too ambitious or too much to ask for 
with the current state of things.
```
---

     
 
all -  [ How to train an LLM with data that contains text and numeric modality ](https://www.reddit.com/r/LangChain/comments/1ckapb8/how_to_train_an_llm_with_data_that_contains_text/) , 2024-05-07-0910
```
Hi, I am newbie interested in training LLMs on csv dataset that contains text data (few sentences about a product) and n
umeric data(its ratings). I have around 200k rows and would to like to train an LLM but I am unable to do it. Can anyone
 here guide me or share any resource which could help me.

&#x200B;
```
---

     
 
all -  [ Integrating PGVector with Hugging Face Embeddings: Addressing Dimension Mismatch Errors ](https://www.reddit.com/r/LangChain/comments/1ck8mj0/integrating_pgvector_with_hugging_face_embeddings/) , 2024-05-07-0910
```
Has anyone used PGVector with HuggingFaceEmbeddings? I'm encountering an error message: 'psycopg2.errors.DataException: 
different vector dimensions 384 and 1536'.
```
---

     
 
all -  [ CS/SWE Resume review ](https://www.reddit.com/r/resumes/comments/1ck7wlt/csswe_resume_review/) , 2024-05-07-0910
```
Hi, I am a rising junior at a university in the United States studying CS looking to get a resume review in anticipation
 of the upcoming internship application releases for summer 2025. I am a US citizen, asian, male. Last season I got no r
esponses from recruiters, but have since added more to my resume. Thanks.

https://preview.redd.it/hduv6d8dkgyc1.png?wid
th=1158&format=png&auto=webp&s=ecc7f514dea13890e11eed039b3667182f8604bd


```
---

     
 
all -  [ Why AI Assistants Can Be Better Than Human VAs ](https://www.reddit.com/r/LangChain/comments/1ck67xs/why_ai_assistants_can_be_better_than_human_vas/) , 2024-05-07-0910
```
 let’s outline *what* VAs even do. As a creator yourself, you balance big projects with smaller, repetitive tasks like a
nswering emails, scheduling meetings & writing smaller pieces of content.

And that’s where your partner in time, your V
A comes in — they handle all of the tedious tasks on your behalf, giving you the freedom to concentrate fully on the imp
ortant things in your life & business.

>Recent stats show Virtual assistants save companies up to 78% in operating cost
s per year, and the VA market is projected to grow 22.3% annually, reaching $8.6B by 2028 — this is definitely a sector 
to pay close attention to.

As the demand for efficiency in our workflows increases, it's worth knowing the potential of
 AI assistants, because why wouldn’t you want to get more time back? Here are the core reasons why AI assistants are bet
ter than traditional VAs:

1. **Cost-Effectiveness** – traditional VAs are invaluable but come with recurring costs — sa
laries, benefits, and more. AI assistants, on the other hand, involve a one-time setup fee and minimal ongoing costs.

1
. **24/7 Availability** – your business needs don’t stop at 5 PM, and neither does an AI assistant. Unlike human VAs who
 clock out, AI can work round-the-clock, able to complete any given task at any time.

1. **Consistency & Accuracy** – A
I minimizes human errors in data entry, scheduling, and customer communication, maintaining high consistency in performa
nce.

>This reliability is key in managing operations that demand precision, like tailored content creation or respondin
g to an important business email, for example.

1. **Adaptability** – training a new assistant takes time and resources.
 AI assistants, however, can be quickly trained to manage new tasks, adapting & evolving alongside your business.

1. **
Accessibility** – with numerous AI tools available, starting is as easy as signing up and setting up — no lengthy recrui
tment or training is required (if you aren’t creating your very own AI assistant, in which case it’s a tad more complex)
. 

However, we must mention the main negative of artificial intelligence – it lacks the human aspect, and therefore AI 
Assistants could ***never*** replace real VAs.

>The human element is crucial, as it brings empathy, creativity, and int
uitive problem-solving to tasks that AI simply can't replicate, and the best way to get the best of both worlds is to in
tegrate AI tools in your virtual assistant’s workflow — we’ll show you how to turn your VA into a cyborg very soon!
```
---

     
 
all -  [ How should I develop a RAG ChatBot that uses a Pandas Dataframe as a source? ](https://www.reddit.com/r/LangChain/comments/1ck54cw/how_should_i_develop_a_rag_chatbot_that_uses_a/) , 2024-05-07-0910
```
Hi, I am new to LangChain and I am developing a application that uses a Pandas Dataframe as document original a Microsof
t Excel sheet. I need it answer questions based on it. 

How should I proceed? Should I ditch the DataFrame approach and
 interface it directly ?

How should I use approach it?

How should I add history as i need to have GUI.
```
---

     
 
all -  [ How to use LLama -3/LLama-2  Model on Nvidia GPU? ](https://www.reddit.com/r/LangChain/comments/1ck4sy9/how_to_use_llama_3llama2_model_on_nvidia_gpu/) , 2024-05-07-0910
```
So far, I've been using the OpenAI API to build a RAG application with Langchain. Now, I'm exploring LLama 3/LLama-2 wit
h GPU support. Can anyone suggest a tutorial for this with Langchain?
```
---

     
 
all -  [ What are some ways to test and improve my RAGs retrieval strategy? ](https://www.reddit.com/r/LangChain/comments/1ck3k84/what_are_some_ways_to_test_and_improve_my_rags/) , 2024-05-07-0910
```
Looking for some tried and tested ways to measure and improve my RAGs retrieval strategy.
```
---

     
 
all -  [ How to add memory to multi- chain with RunnableWithMessageHistory? ](https://www.reddit.com/r/LangChain/comments/1ck2zy8/how_to_add_memory_to_multi_chain_with/) , 2024-05-07-0910
```
Let's say we have two chain , like this:

    prompt1 =  'some prompts here 1'
    prompt2 = 'some prompts here 2'
    

    chain1 = prompt1 | model
    chain2 = prompt2 | model 
    
    combine_chain = chain1 | chain2

My question is how 
to add memory to combine\_chain with RunnableWithMessageHistory? 

The official document just show how to add it in sing
le chain .  I tried that way for combine\_chain, but it doesn't work.  Because prompt2 always need to pass the parameter
 of  'history' which I don't how to pass it. （suppose we have history\_messages\_key='history').

I'm stuck on this prob
lem. I will be very thankful to anyone who can help on it. 

For reference here,  the office document show how to add me
mory to single chain with RunnableWithMessageHistory:  [https://python.langchain.com/docs/expression\_language/how\_to/m
essage\_history/](https://python.langchain.com/docs/expression_language/how_to/message_history/)

  

```
---

     
 
all -  [ Amazon Bedrock - The Complete Guide to AWS Generative AI ](https://www.reddit.com/r/Udemy/comments/1ck08c6/amazon_bedrock_the_complete_guide_to_aws/) , 2024-05-07-0910
```
Learn to Deploy Scalable, Reliable, and Secure Generative AI Apps Using AWS and Amazon Bedrock (Python and TypeScript)


# Introductory Price of only $9.99

# [https://www.udemy.com/course/amazon-bedrock-aws-generative-ai/?couponCode=STARTER
](https://www.udemy.com/course/amazon-bedrock-aws-generative-ai/?couponCode=STARTER)

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
\*\*\*\*\*\*\*\*\*\*

**Unleash the Power of Generative AI on AWS with This Comprehensive Course!**

Welcome to **Amazon
 Bedrock - The Ultimate Guide to AWS Generative AI** – your gateway to mastering the fusion of cutting-edge AI technolog
y and the unparalleled scalability of Amazon Web Services (AWS).

In this course, you'll dive deep into the world of Gen
erative AI, harnessing its potential to create innovative solutions across diverse domains. Whether you're a seasoned da
ta scientist, a visionary entrepreneur, or a curious developer, this course is your ticket to unlocking limitless possib
ilities.

**Key Highlights**:

* **Hands-On Practice**: Dive right into real-world scenarios with practical exercises us
ing Python's boto3, JavaScript SDKs, and TypeScript, coupled with VSCode debugging for seamless development.
* **Text an
d Image Models**: Explore the magic of text generation with chatbots, delve into image generation with state-of-the-art 
models, and master embedding techniques for vector databases.
* **Advanced Applications**: From LangChain to RAG apps an
d document processing, you'll explore a wide array of advanced applications, empowering you to tackle complex challenges
 with confidence.
* **Amazon Bedrock Mastery**: Get up close and personal with Amazon Bedrock – the game-changer for dep
loying scalable, reliable, and secure Generative AI applications on AWS. Practice sections ensure you're well-versed wit
h Bedrock, ready to tackle any project.

**Key topics** covered in this course include:

* **Amazon Bedrock** introducti
on and setup for console and CLI access
* Code examples with **Python** and **TypeScript**
* Integration between **Bedro
ck** and **LagChain**
* Building an **Amazon Bedrock** chatbot with **history**
* Building Image APIs backed by **Amazon
 Bedrock**
* Learn all about the essence of AI: embeddings with **Bedrock**
* Build state-of-the-art **RAG app** with Be
drock Knowledge bases
* **Fine-tune** models and create your **custom models**.

**Why Choose This Course?**

* Expert G
uidance: Learn from industry experts with years of experience in AI and AWS.
* Practical Approach: Gain hands-on experie
nce with guided exercises and real-world case studies.

Don't miss out on this opportunity to become a trailblazer in th
e world of AI innovation! Enroll now and embark on your journey to becoming a Generative AI expert with Amazon Bedrock a
nd AWS.

Go beyond the theory and learn from **active instructors**, aligned with today's programming demands!

Let's re
volutionize the future together!  
[https://www.udemy.com/course/amazon-bedrock-aws-generative-ai/?couponCode=STARTER](h
ttps://www.udemy.com/course/amazon-bedrock-aws-generative-ai/?couponCode=STARTER)
```
---

     
 
all -  [ Vector dbs to use for specific use-case ](https://www.reddit.com/r/LangChain/comments/1cjz0lt/vector_dbs_to_use_for_specific_usecase/) , 2024-05-07-0910
```
A lot of vector dbs are available for RAG and LLM based projects. How will you choose the best one for your use-case? Is
 there a set of criteria to follow for choosing a specific vector db for your project? Lmk what you think
```
---

     
 
MachineLearning -  [ [D] Self-optimizing deterministic LLM memory using dspy, neo4j and vector databases. Need your input ](https://www.reddit.com/r/MachineLearning/comments/1cakjaf/d_selfoptimizing_deterministic_llm_memory_using/) , 2024-05-07-0910
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

     
 
deeplearning -  [ Seeking Advice: Solving Data Challenges with Large Language Models (LLMs) ](https://www.reddit.com/r/deeplearning/comments/1ca4nc1/seeking_advice_solving_data_challenges_with_large/) , 2024-05-07-0910
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

     
 
deeplearning -  [ Share the Coolest Out of The Box LLM Applications That Made You Say 'Wow that was smart' ](https://www.reddit.com/r/deeplearning/comments/1c9e6dj/share_the_coolest_out_of_the_box_llm_applications/) , 2024-05-07-0910
```
Hi, I'm looking at some LLM applications today but apart from guys doing big rags with langchain I don't see too many us
es that are out of the box or that make me say 'wow that was smart to use an LLM here'. Have you seen any cool stuff usi
ng LLMs recently that made you say 'wow, that was smart'?
```
---

     
