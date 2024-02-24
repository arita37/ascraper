 
all -  [ MLOps from a hiring manager perspective. Am I doing this wrong? ](https://www.reddit.com/r/mlops/comments/1ayfkx3/mlops_from_a_hiring_manager_perspective_am_i/) , 2024-02-24-0909
```
So I have a lot of various projects. My engineers (non ML background have done a good job so far).

They can convert DS 
code into web services. They can ship in-house models that the DS builds. These models are NLP and image analysis. We've
 been doing this for a few years.  
They can do the data pipeline - pick and choose database, queue, etc. Also do load-t
esting to see how many transactions we can do given our compute. Basic full stack, with DevOps in between. I can have a 
guy pull a huggingface model, write a k8s helm chart and create an API endpoint to interact with it in 2 days. So now, w
e are having a lot of new projects. Especially with LLMS - Llama2, Mistral, ChatGPT. A lot of RAG projects. Like here is
 100GB of PDFS, we want to vectorize the data, create the embeddings and have various prompts with agents. So if the que
ry was find x or y, it can run an agent/tool to get the data via SQL or API call and feed it back to the prompt via ReAc
t prompt engineering. This is working fine.   
Now we want to scale out the team. Ideally, look for people that have the
se skills. The person should know what a VectorDB is - Cosmos,PineCone,Postgres(pgvector), chromadb,etc. They should kno
w what a similarity search is. How to create an embedding. They should know what langchain is.  


I am getting candidat
es that tell me they can just feed a LLM with plain JSON from Mongo. That an LLM can just do an API call without any con
figuration/setup. Like they are talking out of their asses.  


What am I doing wrong? Candidates are keyword stuffing t
heir resumes with the latest buzzwords or is this the state of MLOps? My requirements is mostly Python backend as our cu
rrent staff before the ChatGPT  hype are all python devs. So writing APIs is just a normal thing. Draft up a swagger spe
c, create the routes.   


But when I ask an interview candidate to convert a rough DS (data scientists can barely write
 any legible code) python script that reads a csv and feeds their small model to get a summary into a REST endpoint, no 
one knows how to do it. To me it is simple, convert the code that reads the csv file into a POST endpoint to consume a p
ayload. Not create a database to store records when the question is a FIFO (First In First Out) API that gets a payload 
and returns a summary from the content. Then they ask why we even doing this? My answer is we are creating a web service
 from the data science team's r&d prototype work so others can consume this.   


Is there a disconnect? or am I looking
 for the wrong candidates? Even simple orchestration questions are appalling. How do you deploy llama2 on-premise to a k
8s cluster. They all say create a docker image w/ a 38GB file and create a 38GB docker image.  


To me an MLOps should 
know how to convert DS python code into deployable services. RESTful if needed. Know how to orchestrate. Create the data
 ingestion and data lake. If I need 4,000 PDFs vectorized, they know how to create an ETL to create those embeddings. Wo
rking off-the-shelf genAI LLMs, they should know some fundamental RAG, vectors, and prompt engineering.

&#x200B;
```
---

     
 
all -  [ RAG evaluation framework ](https://www.reddit.com/r/LangChain/comments/1ayfdhs/rag_evaluation_framework/) , 2024-02-24-0909
```
Hi,

I am looking for some good resources for RAG evaluation.
```
---

     
 
all -  [ How do you create embeddings for the Mistral 7B model without an API key while self-deploying it? ](https://www.reddit.com/r/LocalLLaMA/comments/1ayf5s5/how_do_you_create_embeddings_for_the_mistral_7b/) , 2024-02-24-0909
```
Hi, I have a vLLM deployment of Mistral 7B instruct on a server going, and wanted to create embeddings and a vector stor
e to be used for a RAG model. But MistralAI with LangChain requires an API key,  is there any workaround for this? I was
 trying to use 'sentence-transformers/all-mpnet-base-v2' to create the embeddings but the results from Mistral were all 
gibberish.
```
---

     
 
all -  [ Recommend the best voice-based open source solution for knowledge base - real-time speaking chatbot  ](https://www.reddit.com/r/LocalLLaMA/comments/1aychiv/recommend_the_best_voicebased_open_source/) , 2024-02-24-0909
```
Hi community, can you please recommend some GitHub repo - chatbot/agent that integrates advanced AI capabilities. The ch
atbot should provide real-time, interactive responses based on content from uploaded Word or PDF documents, handle user 
interruptions, and remember the history of previous messages.

What I think it should have:  

1. Document Upload:

Fast
API application for uploading documents. This endpoint should accept files and extract text from them.

1. Text Processi
ng and Vectorization:

maybe transformer model like BERT or RoBERTa to convert this text into embeddings. 

2. Storing E
mbeddings in FAISS:

3. Integrate with Chat Functionality:

This will allow the chatbot to retrieve and use information 
from uploaded documents when responding to user queries.

4. Maintaining Conversation Context:

I believe it should have
 the fastest TTS and ASR based on langchain and something like this:  history can be used alongside the document data fo
r generating context-aware responses.
```
---

     
 
all -  [ LangSmith for evaluation or something else? ](https://www.reddit.com/r/LangChain/comments/1ayaf7p/langsmith_for_evaluation_or_something_else/) , 2024-02-24-0909
```
Hello folks - I feel guilty for posting here but I really can't find a better place. Thank you to anyone who can help me
 or point me in the right direction.

**TLDR**: I'm so desperate for user interviews I'm willing to debase myself for 30
 minutes of your time.   
I am trying to find people to talk to who have shipped or are close to shipping a feature that
 integrates with a 3rd party LLM. I have questions about LLM evaluation because we're building product around that, some
what tangential to langsmith. I need to expand way beyond my personal network. 

I have tried searching forums, posting 
in slack groups, attending in person events in SF, swiping right on every ML engineer, user interview recruiting sites b
ut I'm coming up with a lot of people who are still dabbling with the tech but haven't hit real development yet. Most of
 the folks I've talked to just haven't gotten to any real 'LLM evaluation' needs yet. 

Langchain's series A announcemen
t said they have 80k users, so surely there are some people here that fit my mold?

I am **desperate** to pick your brai
n for 30 minutes about your 'genai stack' and how you figure out if a LLM-integrated solution is behaving well on your d
ata for your users. 

I would gladly send you a thank you milk bar pie, buy you a bougie coffee shop gift card, take you
 on a date (34/F/SF) or yell at your boss for you or for a few moments of your time. 

Please DM me if we can chat somet
ime in the next week or two. Thank you!
```
---

     
 
all -  [ Vertex AI Slowwwwww ](https://www.reddit.com/r/googlecloud/comments/1ay7q54/vertex_ai_slowwwwww/) , 2024-02-24-0909
```
I just started playing around with Gemini and Vertex AI via their python library.  And it is unbearably slow.  Gemini ta
kes 3-5 minutes to write a haiku about the moon, while AWS Bedrock does it in 12 seconds. This happens whether I'm using
 vertexai SDK or Langchain.

[https://imgur.com/a/TlFsxWx](https://imgur.com/a/TlFsxWx)

Not doing anything particularly
 fancy.  It has to be something on my end but can't think of what it might be.

    from datetime import datetime
    st
artTime = datetime.now()
    import vertexai
    from vertexai.generative_models import GenerativeModel
    
    vertexa
i.init()
    model=GenerativeModel('gemini-1.0-pro')
    print(model.generate_content('Write me a haiku about the moon.'
))
    
    print(datetime.now() - startTime)

&#x200B;
```
---

     
 
all -  [ ollama/langchain streaming with tools ](https://www.reddit.com/r/ollama/comments/1ay7ojf/ollamalangchain_streaming_with_tools/) , 2024-02-24-0909
```
I'm trying to setup ollama so that I can have a conversation in a terminal (with streaming) and also allow ollama to int
eract with some rest api. I was able to get streaming working with ChatOllama() by doing this:

    llm = ChatOllama(mod
el='mixtral')
    chain = llm | StrOutputParser()
for chunks in chain.stream('hello')
        print(chunks)

However, I 
don't think I can use ChatOllama to call rest api? I tried streaming with OllamaFunctions() like this:

    llm = Ollama
Functions(model='mixtral')
    chain = create_extraction_chain(schema, llm)
for chunks in chain.stream(input_text)
     
   print(chunks)

However, it only prints out the whole response all at once. Is there a way to do this with streaming? 
I mean I don't need to neccessarily stream an extraction, but I want to have a converstation that uses streaming and als
o allows ollama to call an api.

&#x200B;
```
---

     
 
all -  [ Extracting metadata from a PDF and converting to JSON using LangChain and GPT ](https://www.reddit.com/r/LangChain/comments/1ay6vx4/extracting_metadata_from_a_pdf_and_converting_to/) , 2024-02-24-0909
```
Hi folks! Currently working on a Micro SaaS and ended up needing to convert a PDF to JSON. Given that I've been playing 
around with LangChain for a while now and writing about it, I ended up using the Output Parsers to achieve this.

[I wro
te about this on my blog](https://www.gettingstarted.ai/how-to-extract-metadata-from-pdf-convert-to-json-langchain/) and
 it works like magic... ✨ In fact, it's not just PDF you could convert. Any type of unstructured data potentially works.


Here's what I covered in the post:

✅ Key concepts and explanations

✅ LangChain Output Parsers

✅ OpenAI Functions

✅
 Working source code

[https://www.gettingstarted.ai/how-to-extract-metadata-from-pdf-convert-to-json-langchain/](https:
//www.gettingstarted.ai/how-to-extract-metadata-from-pdf-convert-to-json-langchain/)

Would love to know your thoughts a
nd if you find this helpful.

Cheers!
```
---

     
 
all -  [ Ecosystem around LangChain ](https://www.reddit.com/r/LangChain/comments/1ay1c6a/ecosystem_around_langchain/) , 2024-02-24-0909
```
Hello everyone, I have to admit that I struggle to keep up with the LLM Ecosystem around LangChain and wanted to ask if 
you have any recommended packages that people like me might not know about. I would be especially interested in packages
 you use to build advanced RAG applications and packages you use in Production for task xyz.

I start with a few:

**Lan
gfuse**: LangSmith alternative to monitor LLM Applications in production. MIT License - great!

**Semantic-Text-Splitter
**: Allows you to split documents by contextual parts of them, rather by a fixed document size.

**Ragas**: Framework fo
r evaluating RAG Pipelines. Not dived into it yet, but looks promising.

Please add your favorite packages. Thank you!
```
---

     
 
all -  [ Serverless Q&A AI Bot with Langchain ](https://app.daily.dev/posts/eKFo0hJk4) , 2024-02-24-0909
```

```
---

     
 
all -  [ LangChain Agent 를 활용하여 #chatgpt 를 #업무자동화 에 적용하는 방법🔥🔥 https://www.facebook.com/groups/aitutor21/perma ](https://www.reddit.com/r/chatgpt_newtech/comments/1axvptn/langchain_agent_를_활용하여_chatgpt_를_업무자동화_에_적용하는_방법/) , 2024-02-24-0909
```
LangChain Agent 를 활용하여 #chatgpt 를 #업무자동화 에 적용하는 방법🔥🔥   [https://www.facebook.com/groups/aitutor21/permalink/195027638538
5787/?mibextid=oMANbw](https://www.facebook.com/groups/aitutor21/permalink/1950276385385787/?mibextid=oMANbw)
```
---

     
 
all -  [ Langchain Map Reduce  ](https://www.reddit.com/r/learnmachinelearning/comments/1axkz9u/langchain_map_reduce/) , 2024-02-24-0909
```
I was wondering how langchain map reduce iteratively reduces prompts

For example if we have a context size of 2k and a 
8k token input is supplied 

first we map the 8k to 4x2k maps 

then assuming that those 4 summaries result in 4x1k outp
ut time  summaries how would we map those for the next iteration

Would we fit 2 summaries in one resulting in 2x2k toke
ns maps?

Or would we summarize further each 1k output until all 4 combined are less than 2k context? 

Ie 2 llm calls o
r 4 llm’s calls after first iteration?

I can’t really find any docs supporting either answer clearly for me
```
---

     
 
all -  [ PDF Document Loader not working Langchain ](https://www.reddit.com/r/LangChain/comments/1axi03f/pdf_document_loader_not_working_langchain/) , 2024-02-24-0909
```
Hi I'm trying to extract the content of a pdf using langchain pdf document loader (the javascript version). It could be 
the way I wrote the code (cause I'm still relatively new to javascript and langchain in general) but when i try to run t
he pdf loader i get this error in my console saying 'Type error: readFile is not a function' and i don't know if its one
 of the following;

1. My code
2. I'm not referencing the file path correctly
3. Or something completely unrelated

Hi I
'm trying to extract the content of a pdf using langchain pdf loader (the javascript version). it could be the way i wro
te the code (cause I'm still relatively new to javascript and langchain in general) but when i try to run the pdf loader
 i get this error in my console saying 'Type error: readFile is not a function' and i don't know if its one of the follo
wing;

1. My code
2. I'm not referencing the file path correctly
3. Or something completely unrelated

I'd love and appr
eciate your help and inputs. Thanks in advance

[the pdf is in the public folder](https://preview.redd.it/98512y4zd7kc1.
png?width=556&format=png&auto=webp&s=c2a3693529050746aa49a8f3bf167974180e2e98)

[This is how i called the loader](https:
//preview.redd.it/rpah335zd7kc1.png?width=948&format=png&auto=webp&s=377aff4df96e2f4dd548b0b7b2c6fa65a3ce625b)

[this is
 the error](https://preview.redd.it/nk4mr75zd7kc1.png?width=610&format=png&auto=webp&s=9bf928181eab4da3f03079ebe398ed629
f85d068)
```
---

     
 
all -  [ LangChain - RunnableParallel ](https://www.reddit.com/r/LangChain/comments/1axhxg5/langchain_runnableparallel/) , 2024-02-24-0909
```
I've been banging my head against this issue for awhile and docs haven't been helping.

I'm trying to optimize a chain b
y getting certain things to run in Parallel

I've created a basic example:

`from langchain.chat_models import ChatOpenA
I`

`from langchain.prompts import PromptTemplate`

`from langchain.schema import StrOutputParser`

`from operator impor
t itemgetter`

`from langchain.schema.runnable import (`

`RunnablePassthrough,`

`RunnableLambda,`

`RunnableParallel,`


`)`

`llm_model='gpt-3.5-turbo'`

`llm = ChatOpenAI(temperature=0.9, model=llm_model)`

`prompt = PromptTemplate.from_
template(`

`'What is a good name for a company that makes {product}?'`

`)`

`chain = prompt | ChatOpenAI(temperature=0
.9, model=llm_model) | StrOutputParser()`

Let's start with a standard chain invocation:

`result = chain.invoke({'produ
ct':'Queen Size Sheet Set'})`

`result`

>Regal Rest Bedding Co.

&#x200B;

Now let's say you want to track intermediate
 steps values, so you use RunnablePassthrough:

`chainPass = RunnablePassthrough.assign(company_name=chain)`

`result2 =
 chainPass.invoke({'product':'Queen Size Sheet Set'})`

`result2`

>{'product': 'Queen Size Sheet Set', 'company\_name':
 'RegalRest Bedding Co.'}

&#x200B;

That is great - now we have both the original query (product) and intermediate vari
ables (e.g. company\_name)

Let's try to get this to run in parallel (just with the single chain)

`pchain = RunnablePar
allel(company_name=runnable)`

`pchain.invoke({'product':'Queen Size Sheet Set'})`

>{'company\_name': 'RegalSlumber'}


&#x200B;

Well now we are missing the initial query. What if we tried to assign the chainPass?

`pchain2 = RunnableParal
lel(parent=chainPass)`

`pchain2.invoke({'product':'Queen Size Sheet Set'})`

>{'parent': {'product': 'Queen Size Sheet 
Set',  
>  
>'company\_name': 'Regal Rest Bedding Co.'}}

&#x200B;

This isn't great because now the data is mishaped.


This problem becomes much harder as your chain becomes longer and you start to have steps before/after you Parallel step
, or if you add manual routing, or if you add additional Parallel paths.

The basic question is how do you run multiple 
chains in Parallel when you can keep the input query as well as the outputs for each chain at the root level of the dict
-like output.
```
---

     
 
all -  [ asynchronous requests ](https://www.reddit.com/r/LangChain/comments/1axhkki/asynchronous_requests/) , 2024-02-24-0909
```
Greetings, I have a question about langchain. I have built a database query creation wizard using a langchain agent and 
openai. The thing is that when used by several people the program begins to delusion who should respond first and they e
nd up responding where they shouldn't be. I want to know if there is any tutorial or any way I can use asynchronous call
s so that I can solve this problem and wizard ends up answering one question at a time.
```
---

     
 
all -  [ Buying new mac, have any SVD compatibility info or advice? ](https://www.reddit.com/r/StableVideoDiffusion/comments/1axgpgo/buying_new_mac_have_any_svd_compatibility_info_or/) , 2024-02-24-0909
```
Hi there, I'm about to replace my ancient intel mac. I’ve been doing some work with open-ai and langchain but want to tr
y out SVD. I think thinking I'd buy a MacBook pro m2 max with 64 gigs of ram? Whats you take on that with with SVD? Anyt
hing I should know? 

```
---

     
 
all -  [ Dialogflow +RAG ](https://www.reddit.com/r/LangChain/comments/1axfp44/dialogflow_rag/) , 2024-02-24-0909
```


Iam using nodejs and firebase with dialogflow ES . And I created a RAG function to get response to the userquery by qu
erying PINECONE database . But the function execution  is taking 5 sec.how can I reduce the function execution time ... 

I am Currently using langchain...
```
---

     
 
all -  [ MS In Computer Science or Data Science, In US or Europe, Job etc ](https://www.reddit.com/r/developersIndia/comments/1axd4r2/ms_in_computer_science_or_data_science_in_us_or/) , 2024-02-24-0909
```

Greetings developers,

I recently completed my CS degree and currently work at one of the big 4 tech companies(for 6 mo
nths). While I have some experience in web development from my college projects, I now focus on areas like Gen AI, LLM, 
and Langchain. I am considering pursuing a master's degree, but I'm unsure about which course to choose. I'm torn betwee
n data science and full-stack development. Additionally, I am keen on securing a scholarship, which is why I am contempl
ating studying in Europe, particularly Germany, as scholarships are more accessible there compared to the US.

My ultima
te goal is to secure a job after completing my master's degree. I've noticed that the US tends to offer higher salaries 
for fresh graduates, but I'm also curious about the promotion opportunities in both countries.

I would greatly apprecia
te your suggestions on the following:

1. Should I pursue a master's in CS or data science?
2. Is it advisable to study 
in the US or Europe?
3. Would it be wise to continue working here in India for the time being?

Thank you for your insig
hts.
```
---

     
 
all -  [ Mixtral-8X7B - Local vs API performance ](https://www.reddit.com/r/LocalLLaMA/comments/1axbsjx/mixtral8x7b_local_vs_api_performance/) , 2024-02-24-0909
```
I am using Langchain with an Agent setup. The agent has access to two tools that are both retrievers for specific databa
ses.

1. I use 'mixtral-8x7b-instruct-v0.1.Q5\_K\_M.gguf' from the Bloke and it's performance is abismal. It struggles w
ith generating tool actions and responding in a sensical way.
2. However when i use Mistral's API with the small model (
Mixtral-8X7B-v0.1) it runs flawlessly and answers very intelligently.

Any ideas what might cause this?

&#x200B;
```
---

     
 
all -  [ State of AI agents in real-world ](https://www.reddit.com/r/LocalLLaMA/comments/1axb1dq/state_of_ai_agents_in_realworld/) , 2024-02-24-0909
```
What's the current state of autonomous agents? Does it actually work?  
I played with agents about 9 months ago and it s
eemed to me like it's overhyped. Yes, I've seen people ordering 100 Starbucks latte from DoorDash using agent on a hacka
ton and it was the best demo I've seen deploying agents.   
So, I think you could build impressive showcases with AI age
nts, but generally they weren't useful in practice. When confronted with open questions reality, they started to cycle i
n picking tools, couldn't format responses (I guess this has changed with OpenAI functions/tools), basically it just too
k too long and the results weren't good.   


So my question is: **Has anyone build conversation AI agents that are usab
le real-world products?** Are there any **repos** you could refer me to (besides Langchain, more like some repos leverag
ing such frameworks)?
```
---

     
 
all -  [ Langchian Rust ](https://www.reddit.com/r/rust/comments/1axar0y/langchian_rust/) , 2024-02-24-0909
```
# Langchian Rust

I'm delighted to share a personal endeavor of mine: a Rust port of Langchain. Having been a core contr
ibutor to the official Go Lang port of Langchain (langchaingo), I decided to challenge myself further by exploring the R
ust programming language. This project is an independent effort to reimagine Langchain's capabilities within the Rust ec
osystem, known for its emphasis on safety and performance.

Here's my take on bringing Langchain to Rust, a journey driv
en by my passion for learning and contributing to the open-source community:🔗 [https://github.com/Abraxas-365/langchain-
rust](https://github.com/Abraxas-365/langchain-rust)

This initiative is a personal project, not an official port, and r
epresents my ongoing journey to expand my technical skills and contribute to innovative applications of language models.
 I'm excited about the learning opportunities and potential applications this project might unlock.I warmly invite you t
o explore the repository, share your insights, or even contribute. Your feedback and contributions would not only be wel
come but also deeply appreciated, as they enrich the project and the wider community.Let's explore the possibilities tha
t lie at the intersection of Rust and AI together!
```
---

     
 
all -  [ Azure search Scalability ](https://www.reddit.com/r/LangChain/comments/1ax42kn/azure_search_scalability/) , 2024-02-24-0909
```
Why Azure search so much expensive for me. It costing 250 per search unit.  I am actually doing load testing. and If I w
ant to search 50 concurrent queries, How many search units do I required. Can we assume  one search unit search only que
ry.

&#x200B;

https://preview.redd.it/mu6916z3f4kc1.png?width=1359&format=png&auto=webp&s=020d4c80201db2d4e8f50bb5cb4f3
d61958cd055
```
---

     
 
all -  [ Why do people say Langchain is overengineered? Please explain ](https://www.reddit.com/r/OpenAI/comments/1awy64a/why_do_people_say_langchain_is_overengineered/) , 2024-02-24-0909
```
Hi all,

I'm not a software engineer by any means. I'm just a regular data scientist who is getting some hands on experi
ence with LLMs. I have played with the OpenAI API and Langchain. I find the Python OpenAI API fairly 'simple and intuiti
ve' to use compared to Langchain. The documentation for Langchain is pretty hard to read too. This is just my personal o
pinion.

What I don't understand is this? I have seen many people say Langchain is \*overengineered\*. What does it real
ly mean? And why? I tried my best to go through the points raised in other forums but couldn't understand much. 
```
---

     
 
all -  [ Guidance on streaming   ](https://www.reddit.com/r/LangChain/comments/1awxbfl/guidance_on_streaming/) , 2024-02-24-0909
```
I have some endpoints exposed on my fastap+langchain webservice; endpoints support async; underneath expose chain ainvok
es;

Endpoints sometimes take time 30-120 secs

With langsmith confirmed its openai models where most time is spent 

Wa
s looking for a proper architecture to support streaming of output and intermediate steps to evade long delays on the fr
ontend?

Do I need to handle it for each endpoint or there could be one sink I could expose for user to query?

Not usin
g any backend queue like Celery.

Please guide 🙏 
```
---

     
 
all -  [ Langchain CSV  and llama2 ](https://www.reddit.com/r/LangChain/comments/1awub34/langchain_csv_and_llama2/) , 2024-02-24-0909
```
Hi 

I loaded CSV with CSV loader and used llama2 to get data from csv but it is not working. It is getting wrong result
s for every prompt. 

I used  huggingface sentence transformer embedding and loaded in vector db. If I do similarity sea
rch I'm able to see all data. But when I train that to llama2 model. For every input it is showing same result.

Can you
 please help me with this?
```
---

     
 
all -  [ Unusual experiences with the indexing API ](https://www.reddit.com/r/LangChain/comments/1awu6db/unusual_experiences_with_the_indexing_api/) , 2024-02-24-0909
```
\- I conducted a test with the langchain indexing api. In short, this led to a much slower upsert time to my vector DB t
han just using the traditional langchain embeddings method, and it also produced an unusually large amount of vectors. T
his makes no real sense to me as it was embedding the same chunked textual material and I'm trying to figure out if ther
e are variables I haven't accounted for properly. 
```
---

     
 
all -  [ nvim urgently needs good AI plugins ](https://www.reddit.com/r/nvim/comments/1awry69/nvim_urgently_needs_good_ai_plugins/) , 2024-02-24-0909
```
There was a day in which neovim with LSP support, Treesitter, and Lua plugins was released.

It was the beginning of a n
ew era of the vim family of editors and it suddenly became in pair with its main rival made by the open source enemy Mic
ro$oft.

These days that coding goes hand in hand with AI tools, however, neovim is getting behind again.

1. Copilot fo
r vscode has a chat node which is lacking in neovim version
2. Sending context to AI models from neovim is severely limi
ted and basically impossible (e.g. sending the whole file or the whole workspace)
3. Online search ala Phind.com is miss
ing from all the plugins.

Vscode instead provides plugins such as phind.com, copilot, ChatGPT, which are way more power
ful than the nvim counterparts. Phind.com is especially extremely powerful, not because of the model themselves but beca
use of the functionalities it provides (it's super easy to add specific files to the query or specific symbols in order 
to describe what should be changed).

Recently, I discovered cursor.sh , which is a vscode fork that promises many usefu
l functionalities that are totally missing in the vim world.

We should basically include langchain or similar in our ai
 plugins in order to build indexed databases of symbols and files, use online searches, and improve the AI tools. 

But 
how? I fear the main issue here is Lua...
```
---

     
 
all -  [ One Drive RAG & Text to SQL ](https://www.reddit.com/r/LangChain/comments/1awm22j/one_drive_rag_text_to_sql/) , 2024-02-24-0909
```
Hi there,

I want to use a RAG for documents on One Drive and a Text to SQL as well in the same chat bot.

How would the
 Agent differentiate if the question needs to do the RAG (One Drive) or Interact with the database based on the user's q
uestion?

Is it a solved problem? If yes, how?
```
---

     
 
all -  [ This might seem like the dumbest question ever, but I can't get my Azure OpenAI service to work with ](https://www.reddit.com/r/LangChain/comments/1awk5pm/this_might_seem_like_the_dumbest_question_ever/) , 2024-02-24-0909
```
Wtf am i doing wrong?

I've got my Azure OpenAI service running ,but some reason Azure still gives the older version of 
the OpenAI's code despite the new version being out months now. 

But anyway, I'm literally just trying to get a f\*ckin
g basic prompt sent to the AI and print it's response.

Does anyone have a simple guide on how to do this basic everyday
 shit that that OpenAI literally gives you instantly from the playground?

Am I asking too much? I've combed through so 
many tutorials and asked so many LLMs, yet I can't get this basic thing to work.
```
---

     
 
all -  [ Langchian Rust ](https://www.reddit.com/r/LangChain/comments/1awk4i8/langchian_rust/) , 2024-02-24-0909
```
# 🎉 Exciting Personal Project Alert! 🎉

I'm delighted to share a personal endeavor of mine: a Rust port of Langchain. Ha
ving been a core contributor to the official Go Lang port of Langchain (langchaingo), I decided to challenge myself furt
her by exploring the Rust programming language. This project is an independent effort to reimagine Langchain's capabilit
ies within the Rust ecosystem, known for its emphasis on safety and performance.

Here's my take on bringing Langchain t
o Rust, a journey driven by my passion for learning and contributing to the open-source community:🔗 [https://github.com/
Abraxas-365/langchain-rust](https://github.com/Abraxas-365/langchain-rust)

This initiative is a personal project, not a
n official port, and represents my ongoing journey to expand my technical skills and contribute to innovative applicatio
ns of language models. I'm excited about the learning opportunities and potential applications this project might unlock
.I warmly invite you to explore the repository, share your insights, or even contribute. Your feedback and contributions
 would not only be welcome but also deeply appreciated, as they enrich the project and the wider community.Let's explore
 the possibilities that lie at the intersection of Rust and AI together!
```
---

     
 
all -  [ Perplexity’s copilot feature using LangGraph Planning Agent for RAG pipeline ](https://www.reddit.com/r/LangChain/comments/1awjuwp/perplexitys_copilot_feature_using_langgraph/) , 2024-02-24-0909
```
I am trying to build the perplexity's copilot feature for my RAG chatbot implementation.   


I am thinking of using Lan
gGraph Planning Agent (which I learnt about today). I am thinking of using Planner to ask for clarifying questions. For 
the execution stage I will be using either a simple query pipeline or the multi query engine.   


Please share your tho
ughts/ opinions about the feasibility aspect of the idea. Also, if you know about an open source project with similar fe
atures please feel free to share. TIA
```
---

     
 
all -  [ Need help in choosing memory type ](https://www.reddit.com/r/LangChain/comments/1awhcj3/need_help_in_choosing_memory_type/) , 2024-02-24-0909
```
I'm building sample project to learn about LangChain, the project is Finance based. Please suggest which memory type wou
ld be best based on the following information about the project - 

Title - **Aid in detection of Malicious Activities i
n Transactions**

As the title says, the project is about making use of LLM's and forming a kind of hypothesis to form a
 case wherein with the help of the chat interface the investigator can fetch details about the transactions. I plan on u
sing LangChain to interact with the database, which contains transaction details and also pass the relevant set of docum
ents of the account holder(using RAG). Here when the investigator is prompting the LLM, the LLM has to retain/store some
 of the previous conversations in the memory buffer to aid any further queries/questions. I'm confused on which memory t
ype to use..

&#x200B;

As per the documentation, the memory types are as follows - [https://python.langchain.com/docs/m
odules/memory/types/](https://python.langchain.com/docs/modules/memory/types/)  


Things to consider,

\- Assume I limi
ted set of tokens 

\- I want to keep the context of the previous conversations without storing too much information. 


&#x200B;

My thoughts,

use **ConversationSummaryBufferMemory** or **ConversationTokenBufferMemory** as these 2 are very
 close to what I want to achieve.

PS: I'm a beginner to LangChain and LLM development, please feel to correct incase of
 any mistakes and I'm eager to listen to your suggestions:)
```
---

     
 
all -  [ Kraken the Code: How to Build a Talking Avatar ](https://www.reddit.com/r/ArtificialInteligence/comments/1awh0vh/kraken_the_code_how_to_build_a_talking_avatar/) , 2024-02-24-0909
```
We joked with my colleague that this [post about real-time text-to-speech lipsync](https://monadical.com/posts/how-to-bu
ild-a-talking-avatar-with-azure-cognitive-langchain-and-openai.html) of his was either born too late because [Sora](http
s://openai.com/sora) is here to rule the industry or too early because his solution is tailored \*\*better\*\* than Sora
 for the specific task. Anyway, it's an ironic coincidence that he finished writing it before OpenAI released their vide
o monster 🦖. 

I personally think that his solution is niche enough, and Sora won't make it obsolete! What do you think?


The post has a lot of technical programming stuff, and I believe it will be very educational for engineers who are int
erested in AI!  
```
---

     
 
all -  [ ToolExecutor Error when using langgraph ](https://www.reddit.com/r/LangChain/comments/1awf1tx/toolexecutor_error_when_using_langgraph/) , 2024-02-24-0909
```
Hello guys, i try to implement a langgraph example, i have a list of 2 tools, one is retriever from chroma db which i ha
ve created with create\_retriever tool , and the other is a custom tool , both tools work when i initialize an agent and
 invoke the AgentExecutor.

this is how i create my array : tools=\[tool1,tool2\] -> this works with agentexecutor  


W
hen i try to pass the tools to ToolsExecutor, when langgraph tries to use them i get the following error :

&#x200B;

At
tribute Error : 'list' object has no attribute 'tool'.

&#x200B;

Has anyone faced this error on ToolsExecutor ?
```
---

     
 
all -  [ [D] Graphs + vectordbs? Need your input: Cognee.ai . AI Data Pipelines for Real-World Production (Pa ](https://www.reddit.com/r/MachineLearning/comments/1aweo71/d_graphs_vectordbs_need_your_input_cogneeai_ai/) , 2024-02-24-0909
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

     
 
all -  [ RDF, Ontology, knowledge graph: QA ](https://www.reddit.com/r/LangChain/comments/1awemif/rdf_ontology_knowledge_graph_qa/) , 2024-02-24-0909
```
Hello, I'm trying to use an LLM to answer some questions using what is present in an ontology in rdf format. I wasn't ab
le to get results with the .ttl file so I thought of reducing the ontology and using a knowledge graph made up of very s
imple triples, like:

&#x200B;

    X hasOptionalKnowledge Y
    X hasURI Y

However, the model (OpenAI or LLAMA2 7b) do
es not seem to be able to answer, even when the questions are specific with keywords like:

    'what are the optional k
nowledges for a data scientist?'.

Has anyone ever worked on this type of data? Any help is welcome
```
---

     
 
all -  [ multiple users ](https://www.reddit.com/r/LangChain/comments/1awak6s/multiple_users/) , 2024-02-24-0909
```
hello, I've built a chatbot and it handles the conversation well, however I want to implement it on a larger scale, I wa
nt to make multiple users interact with it at the same time, and I want each user to have their own chat history and cha
tting experience, what is the best way to do so? I'm building the chatbot on WhatsApp btw, and it must handle each user 
conversation separately.
```
---

     
 
all -  [ Please review my resume. Not getting any interviews despite applying on a daily basis. ](https://www.reddit.com/gallery/1aw80tn) , 2024-02-24-0909
```
Hey everyone. I need some help. I am AI/ML Engineer and I've been actively looking for a job for the better part of a ye
ar. My current job pays too less and someone recommended me for it , so I am really looking for something. I apply daily
 for many jobs but have never gotten called for an interview. Please be as critical as you can! Any help and advice is a
ppreciated!
```
---

     
 
all -  [ Exllama V2 x langchain  ](https://www.reddit.com/r/LangChain/comments/1avz27t/exllama_v2_x_langchain/) , 2024-02-24-0909
```
Hello, 

for every person looking for the use of Exllama with Langchain & the ability to stream & more , here it is : 


\- [ExllamaV2 LLM](https://github.com/AmineDjeghri/langchain/blob/master/libs/community/langchain_community/llms/exllama
v2.py) : the LLM itself.

\- [Jupyter notebook](https://github.com/AmineDjeghri/langchain/blob/master/docs/docs/integrat
ions/llms/exllamav2.ipynb) : how to use it 

it still needs loras & more parameters, i will add that when i'll have some
 time. Any contribution is more than welcome
```
---

     
 
all -  [ Langchain, Langsmith, Llamaindex, and from Microsoft: Semantick Kernel, Prompt flow. Can someone exp ](https://www.reddit.com/r/aipromptprogramming/comments/1avvsw9/langchain_langsmith_llamaindex_and_from_microsoft/) , 2024-02-24-0909
```
 

Hello,  
Senior dev here. Getting into AI quick because I don't want to be one of those devs who are out of the loop 
of important changes.  
I'm currently struggling with getting the picture of what all these puzze pieces do and where th
ey fall in in the big picture.

Let's make as an example a classical angular webapp with a backend API that allows user 
to load his pdf or make speech to text as data to ingest.  
Then the user can query the LLM and get info on all the inge
sted data.

This is how I understood stuff:

**Llama index**: manages data ingestion, chunking, embedding and saving int
o a vector db. Except saving to vector db, does the rest based on either LLM models on azure or local.  
Provides interf
aces and classes to do all the work with these third party models/tools.

**Langchain/semantic kernel** = Allow flow con
trol and agents/planners.

Both of them from what I've seen from code snippets allow you to define pieces of code that e
ither call LLM online (or local?) with certain configuration (max tokens, temperature etc etc) and allow building agents
 by giving these pieces of code a description, then it's up to the LLM to decide what call based on that description

Yo
u can define either semantic functions (those which calls LLM) or native functions (you do stuff in your code)

These al
lows kinda controlling what LLM to call or what prompt to put as system prompt/metaprompt (the prompt you secretly send 
along with the original user request)

**Langsmith**: ???

**Prompt flow**: basically allows a predetermined sequence of
 actions without conditional statements (if/else) and allow you to call code from multiple languages/tools

# Data inges
tion

User will have a form to upload files

From what I get, you basically configure a prompt flow .yaml file for every
 action you want to do. So data ingestion for pdf files, for example, will have his own prompt flow.

This prompt flow w
ill call llamaindex for ingestion, then for chunking and for saving embeddings and chunks.

# User queries

You will hav
e a prompt flow that will need to call llamaindex for the RAG, then either semantick kernel or lamaindex will do stuff w
ith models online after the correct chunks of the pdf files have been retrieved.

In a more complex scenario, if multipl
e actions (agent-like behavior) is required, it will be task for Langchain or semantic kernel to do so.

Can anyone expa
nd and help me?  
I'm reanding a ton of docs and watching videos and I feel overwhelmed and lost
```
---

     
 
all -  [ Improving FAISS Query Accuracy with Regex Segmentation in LangChain ](https://www.reddit.com/r/LangChain/comments/1avu9v0/improving_faiss_query_accuracy_with_regex/) , 2024-02-24-0909
```
Hi LangChain Community,

I'm working with langchain\_community.vectorstores  
's FAISS for document segmentation. Initia
lly, I segmented documents into fixed-size chunks (1024) using RecursiveCharacterTextSplitter  
. This approach sometime
s cuts relevant information in half if it's at a chunk's end, leading to incomplete query responses.

To better align se
gmentation with document context, I switched to Regex-based segmentation, creating dynamically sized chunks. However, I'
ve hit a snag: FAISS.from\_documents  
 doesn't accept the list format produced by my Regex segmentation.

Does anyone h
ave tips on integrating Regex-segmented lists with LangChain's FAISS vector store for more accurate and complete query r
esponses?

Thanks for any insights!
```
---

     
 
all -  [ Query: How do I use LLM to narrow down a user query ](https://www.reddit.com/r/LangChain/comments/1avsdmu/query_how_do_i_use_llm_to_narrow_down_a_user_query/) , 2024-02-24-0909
```
Hi
I have a knowledge base of about 5000 articles. The user will be querying the knowledge base. A question can have mul
tiple answers in the knowledge base. Is it possible to use any chain to make the AI ask follow up questions to zero down
 on the exact response. I have already setup a vector store with PGVector and I’m able to query the knowledge base.
Exac
t scenario
Picture that I have 1000 articles about troubleshooting a laptop.
The user inputs a query: “my laptop is not 
booting up”
This can be because of multiple issues - RAM issue, motherboard issue, graphics card issue etc. I want the L
LM to respond back with a series of questions like “are there any beeps when you boot up the laptop “ if yes then ask ab
out the sequence of beeps and provide appropriate troubleshooting steps. If no, then it can ask him about any clacking s
ound arising from the disk etc…
Note these potential issues are there in the knowledge base . For example in a section c
alled RAM issues, there would be a listing that says “the laptop might not boot up due to a faulty RAM” to diagnose chec
k if there are any abnormal beeps during system start up.

Is this possible to achieve?
Any help would be appreciated.
```
---

     
 
all -  [ [For Hire] Programmer/Web Developer/IT Consultant (Python, PHP, AI, etc.) ](https://www.reddit.com/r/forhire/comments/1avqfpz/for_hire_programmerweb_developerit_consultant/) , 2024-02-24-0909
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

     
 
MachineLearning -  [ [D] AI projects Suggestions ](https://www.reddit.com/r/MachineLearning/comments/1aunkmw/d_ai_projects_suggestions/) , 2024-02-24-0909
```
Hi Everyone, I need a suggestion to create AI courses for students ( Hands-on AI projects). I am thinking about the late
st AI trends such as Langchain, RAG, and vector databases. In each project, there can be multiple tasks, and the main th
ing is each task should have an automated system in which we can verify whether students have done it correctly or not.


For example: Project with visualization cannot be automatically tested. 

For example: A project with visualization can
not be automatically tested. . em can verify if the length of the text is smaller we can verify that it is correct.
```
---

     
 
MachineLearning -  [ [D] What's the standard practice for setting initialization prompts and maintaining context when swi ](https://www.reddit.com/r/MachineLearning/comments/1aq78ao/d_whats_the_standard_practice_for_setting/) , 2024-02-24-0909
```
Hi I am trying to build a modularized LLM application using Langchain where within any individual conversation the app c
an seamless switch between multiple LLMs to respond to the query, for example:

1. User: What's 1+ 1?
2. App (GPT-3.5): 
1+1 is 2
3. User: Concatenate the last name of the current president of the US with the answer from your last response
4
. App (Gemini Ultra): Biden2

I have two technical questions that I hope this subreddit can help answer:

1. What's the 
standard practice for setting the initialization prompts or background prompts? For example I want to tell this App that
 'your name is Bob', and I want this App to continuously remember it's Bob regardless how long the conversation has gott
en or any switching between LLMs. Do I set this at the beginning of the conversation or before every single response?
2.
 What's the standard practice for conversation memory management when there's switching of LLM involved within one conve
rsation? Do I store all the conversation history within a vector database and do a index search prior to any individual 
response?
```
---

     
 
MachineLearning -  [ Whats in your RAG setup? [D] ](https://www.reddit.com/r/MachineLearning/comments/1apcp2w/whats_in_your_rag_setup_d/) , 2024-02-24-0909
```
What frameworks and libraries are you using in your RAG? 

I'm most curious if  LangChain is as popular as it was?

Here
's mine at a high-level: 

*  langchain to use OpenAI for creating embeddings
* Pinecone for storing embedding
* langcha
in to load document splitters and characters splitters for chunking
* Mongo for conversations memory

&#x200B;
```
---

     
 
MachineLearning -  [ [D] What's the best current RAG setup that would work with a local LLM? ](https://www.reddit.com/r/MachineLearning/comments/1ag6bo7/d_whats_the_best_current_rag_setup_that_would/) , 2024-02-24-0909
```
I've tried things like langchain in the past (6-8 months ago) but they were cumbersome and didn't work as expected.

I  
need RAG to get data from various pdfs (long one, 150+ pages) - and i  need a setup that will allow me to add more and m
ore data sources.

I wanna run this locally, can get a 24gb video card (or 2x16gb ones) - so i can run using 33b or smal
ler models.

I  know things in the industry change every 2 weeks, so i'm hoping there's  an easy and efficient way of do
ing RAG (compared to 6 months ago)
```
---

     
 
MachineLearning -  [ [P]: Anukool: My job hunting assistant ](https://www.reddit.com/r/MachineLearning/comments/1adu3tw/p_anukool_my_job_hunting_assistant/) , 2024-02-24-0909
```
Hey Reddit, I've been applying for jobs and found that writing a cover letter for each position was tedious. I also delv
ed into LLM and Langchain, hoping to leverage them for a project to aid in my job hunting. So, I developed Anukool under
 the GPL license. While it's far from perfect, it has proven very useful to me, and I hope it benefits you as well. All 
I have to do is provide it with a pdf containing information about me such as my experience, skills, projects, etc and i
t will use this information along with job description to generate cover letter for me. Since I'm new to ML and LLM, any
 advice or feedback is greatly appreciated, and contributions are also welcome. I plan to utilize Llama-2 soon to furthe
r open-source the project.

Check out the GitHub link, and please star it if you find the project interesting: https://g
ithub.com/dakshesh14/anukool
```
---

     
 
deeplearning -  [ [D] WebVoyager: Navigating Digital Cosmos with LangGraph & Multimodal Models ](https://www.reddit.com/r/deeplearning/comments/1altlca/d_webvoyager_navigating_digital_cosmos_with/) , 2024-02-24-0909
```
Embark on a journey through the digital cosmos with WebVoyager, a groundbreaking Large Multimodal Model (LMM) web agent 
designed to navigate the vastness of the online universe. In collaboration with Langchain, WebVoyager represents a parad
igm shift in autonomous web agents, seamlessly integrating visual and textual information to complete user instructions 
end-to-end by interacting with real-world websites.

Link: [https://medium.com/@andysingal/webvoyager-navigating-digital
-cosmos-with-langgraph-multimodal-models-dace64196c2f](https://medium.com/@andysingal/webvoyager-navigating-digital-cosm
os-with-langgraph-multimodal-models-dace64196c2f)
```
---

     
 
deeplearning -  [ [D] Langchain Elevates with Step-Back Prompting using RAGatouille ](https://www.reddit.com/r/deeplearning/comments/1agtyeh/d_langchain_elevates_with_stepback_prompting/) , 2024-02-24-0909
```
In the dynamic realm of natural language processing, a revolutionary synergy has emerged between Langchain and Step-Back
 Prompting. This article delves into the transformative collaboration, exploring how Langchain’s cutting-edge platform i
ncorporates Step-Back Prompting to redefine language processing capabilities. Join us on a journey of innovation and dis
covery as we unravel the intricacies of this powerful integration. As we explore the uncharted territories of language m
odels, Step-Back Prompting stands as a beacon of progress, promising a journey of nuanced understanding and elevated per
formance in the world of Large Language Models. Welcome to the future of language processing, where inspiration and inno
vation converge in a symphony of words and ideas.

Link: https://medium.com/ai-advances/langchain-elevates-with-step-bac
k-prompting-using-ragatouille-b433e6f200ea
```
---

     
 
deeplearning -  [ Become an AI Developer (Free 9 Part Series) ](https://www.reddit.com/r/deeplearning/comments/1afgp2r/become_an_ai_developer_free_9_part_series/) , 2024-02-24-0909
```
Just sharing a free series I stumbled across on Linkedin - DataCamp's 9-part AI code-along series.

This specific sessio
n linked below is 'Building Chatbots with OpenAI API and Pinecone' but there are 8 others to have a look at and code alo
ng to.

*Start from basics to build on skills with GPT, Pinecone and LangChain to create a chatbot that answers question
s about research papers. Make use of retrieval augmented generation, and learn how to combine this with conversational m
emory to hold a conversation with the chatbot. Code Along on DataCamp Workspace:* [*https://www.datacamp.com/code-along/
building-chatbots-openai-api-pinecone*](https://www.datacamp.com/code-along/building-chatbots-openai-api-pinecone)

Find
 all of the sessions at: [https://www.datacamp.com/ai-code-alongs](https://www.datacamp.com/ai-code-alongs)
```
---

     
 
deeplearning -  [ DSPy Explained! ](https://www.reddit.com/r/deeplearning/comments/1adypks/dspy_explained/) , 2024-02-24-0909
```
DSPy is the next big advancement for AI and building applications with LLMs!

Pioneered by frameworks such as LangChain 
and LlamaIndex, we can build much more powerful systems by chaining together LLM calls! This means that the output of on
e call to an LLM is the input to the next, and so on. We can think of chains as programs, with each LLM call analogous t
o a function that takes text as input and produces text as output.

DSPy offers a new programming model, inspired by PyT
orch, that gives you a massive amount of control over these LLM programs. Further the Signature abstraction wraps prompt
s and structured input / outputs to clean up LLM program codebases.

DSPy then pairs the syntax with a super novel compi
ler that jointly optimizes the instructions for each component of an LLM program, as well as sourcing examples of the ta
sk.

Here is my review of the ideas in DSPy, covering the core concepts and walking through the introduction notebooks s
howing how to compile a simple retrieve-then-read RAG program, as well as a more advanced Multi-Hop RAG program where yo
u have 2 LLM components to be optimized with the DSPy compiler! I hope you find it useful!

https://www.youtube.com/watc
h?v=41EfOY0Ldkc
```
---

     
