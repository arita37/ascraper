 
all -  [ Chat UI with RAG ](https://www.reddit.com/r/OpenAI/comments/1adfira/chat_ui_with_rag/) , 2024-01-29-0910
```
is there a website or tool that lets you chat with pdfs or other text files like chatgpt? Unfortunately Librechat can't 
do this as far as I know or at least not yet. And I mean not chat with pdfs websites, I want a normal chat interface tha
t also is able to interact with pdfs if needed, and I'd like to use my own API key.

I was thinking trying to build some
thing like this myself but it's not that easy. You'd need some sort of agent that is called when asked. That whole langc
hain framework got annoyingly clustered with functions..
 
thanks
```
---

     
 
all -  [ Looking for a production level vector db ](https://www.reddit.com/r/LangChain/comments/1adf3o6/looking_for_a_production_level_vector_db/) , 2024-01-29-0910
```
Im looking for a production level vector db, so I was thinking about plain pg + pgvector, the problem is that I can't fi
nd an easy way of finding a good library to interact with it, so far I'm using raw queries like this (i will leave code 
at the bottom). I don't know if this is the best way apart from chroma, weaviate, pinecone, etc etc this is going to be 
at production level por mi company to be used internally.  
WITH vector\_matches AS (  
SELECT document\_id, 1 - (embedd
ing <=> %s) AS similarity  
FROM documents\_embeddings  
WHERE 1 - (embedding <=> %s) > %s  
ORDER BY similarity DESC  

LIMIT %s  
)  
SELECT d.page\_content, d.metadata, d.file\_id, vm.similarity  
FROM documents d  
INNER JOIN vector\_mat
ches vm ON d.id = vm.document\_id  


&#x200B;
```
---

     
 
all -  [ Langchain Cookbook Overview ](https://youtu.be/SKAwiiDwN3Q?si=Kb2EumYyCN-YxHYU) , 2024-01-29-0910
```

```
---

     
 
all -  [ HackerNews AI built using function calling ](https://www.reddit.com/r/LangChain/comments/1adarpa/hackernews_ai_built_using_function_calling/) , 2024-01-29-0910
```
Hi reddit, I built an AI that can interact with the Hacker News API: [https://hn.aidev.run](https://hn.aidev.run)

You c
an ask questions like:

* What's on hackernews about AI?
* What's on hackernews about iPhone?
* What's trending on hacke
rnews?
* What are users showing on hackernews?
* What are users asking on hackernews?
* Summarize this story: [https://n
ews.ycombinator.com/item?id=39156778](https://news.ycombinator.com/item?id=39156778)

It uses function calling to query 
the HN api.

To answer questions about a particular topic, it’ll search its knowledge base (a vector db that is periodic
ally updated with the “top stories”) and get details about those stories from the API.

This is pretty barebones and I b
uilt it today in < 2 hours, so it probably won’t meet your high standards. If you give it a try, I’d love your feedback 
on how I can improve it.

If you’re interested, I built this using [phidata](https://github.com/phidatahq/phidata)

Than
ks for reading and would love to hear what you think.
```
---

     
 
all -  [ Why separate langchain and langchain_core for python package ](https://www.reddit.com/r/LangChain/comments/1ad9x8c/why_separate_langchain_and_langchain_core_for/) , 2024-01-29-0910
```
Hey, I'm trying to familiarize myself with the internals of the langchain python package, I noticed that langchain and l
angchain\_core are separated and in the internal code they have similar sub packages. my question is what is the need fo
r this separation and what is the thought process behind what should be implemented in langchain vs langchain\_core. Tha
nks
```
---

     
 
all -  [ What is the best on-prem vector db ](https://www.reddit.com/r/LangChain/comments/1ad52as/what_is_the_best_onprem_vector_db/) , 2024-01-29-0910
```
I'm building an app using LangChain to integrate with ChatGPT. I need a vector DB to store the embeddings. I want to use
 an on-prem option, not a cloud one. There are quite a few options I see from my searches. Wondering what folks would re
commend. Thanks.
```
---

     
 
all -  [ Use HTML splitter for JSX (React) code? ](https://www.reddit.com/r/LangChain/comments/1ad4eye/use_html_splitter_for_jsx_react_code/) , 2024-01-29-0910
```
I am creating a chatbot over the data of my **static React website**.

I fetch the page files from the file system using
 the [DirectoryLoader](https://js.langchain.com/docs/modules/data_connection/document_loaders/file_directory). I could u
se a web loader but I want it to work even in local development.

The issue is the text splitter.

I couldn't find a pro
per text splitter for JSX (React) code. But I seem to get decent results with the [HTML recursive text splitter](https:/
/js.langchain.com/docs/modules/data_connection/document_transformers/code_splitter#html), probably because JSX and HTML 
are so similar.

Before I send my documents to the HTML splitter, I **remove all import statements and class names** (to
 get rid of the unnecessary clutter). I keep everything else (which might include some JavaScript code).

Is my approach
 fine? Is the HTML splitter suited for this use case? Is it normal that there is no text overlap in the generated docume
nts?
```
---

     
 
all -  [ Streamlit run app.py - blank screen help ( vscode) - OpenAI chat bot project ](https://youtu.be/x0AnCE9SE4A?si=Yb1LMCiz5AJ1RE7E) , 2024-01-29-0910
```
Hello, I'm a newbie programmer and having mind boggling issue of my app not deploying...it is a chat bot...everything se
ems to be fine just the error was Inport error: Openai can't be imported from langchain. I don't know..have scoured the 
internet for the fixes, but unable to find a solution.

Saw a tutorial from free coding camp on YouTube and it seems to 
work in that tutorial. I followed step by step even checked multiple times.

If someone can help me find out what is wro
ng I will be very grateful.

It may be a simple thing or complex I don't know as I don't have a 360 degree understanding
 of python libraries or streamlit requirements. I followed the tutorial 100% though. I can say that.

I reached 1:14:00 
in the video
```
---

     
 
all -  [ Streamlit run app.py - blank screen help ( vscode) - OpenAI chat bot project ](https://youtu.be/x0AnCE9SE4A?si=8J46bJ3WXX-w0xf9) , 2024-01-29-0910
```
Hello, I'm a newbie programmer and having mind boggling issue of my app not deploying...it is a chat bot...everything se
ems to be fine just the error was openai can't be imported from langchain. I don't know ..have scoured the internet for 
the fixes, but unable to find a solution. 

Saw a tutorial from free coding camp on YouTube and it seems to work in that
 tutorial. I followed step by step even checked multiple time.

If someone can help me find out what is wrong I will be 
very grateful. 

It may be a simple thing or complex I don't know as I don't have a 360 degree understanding of python l
ibraries or streamlit requirements. I followed the tutorial 100% though. I can say that.

I reached 1:14:00 in the video

```
---

     
 
all -  [ Is there any git dedicated for text-to-SQL to be inference on local LLM? ](https://www.reddit.com/r/LocalLLaMA/comments/1ad26zr/is_there_any_git_dedicated_for_texttosql_to_be/) , 2024-01-29-0910
```
I am trying to find a method to use local LLM for queries and use it for RAG purposes as well as text-to-SQL purposes. L
angChain SQL agent doesn’t work well with the local models.. so trying to find if there is any git that can help me solv
e this issue
```
---

     
 
all -  [ Qdrant DB: Payload Limit Exceeded Error ](https://www.reddit.com/r/LangChain/comments/1ad0vvg/qdrant_db_payload_limit_exceeded_error/) , 2024-01-29-0910
```
I am trying to store Langchain Documents in the qdrant database(docker). When I try storing them in the db. I am getting
 this error. Please help me solve this.

&#x200B;

UnexpectedResponse: Unexpected Response: 400 (Bad Request)

Raw respo
nse content:

b'{'status':{'error':'Payload error: JSON payload (46866880 bytes) is larger than allowed (limit: 33554432
 bytes).'},'time':0.0}'
```
---

     
 
all -  [ Is there a reranking example with Langchain? ](https://www.reddit.com/r/LangChain/comments/1acywew/is_there_a_reranking_example_with_langchain/) , 2024-01-29-0910
```
I want to rerank my retrieved documents but couldn't find an example on Langchain. Ant pointers would help. (not looking
 for context compression)
```
---

     
 
all -  [ Best Practices for Semantic Search on 200k vectors (30GB) Worth of Embeddings? ](https://www.reddit.com/r/LangChain/comments/1acxxbw/best_practices_for_semantic_search_on_200k/) , 2024-01-29-0910
```
Hi, I have converted some domain-specific name vectors into embeddings, with a dataset size of 200k words. All the embed
dings were generated using OpenAI's embedding model 3 (3072 dim per embedding) . Now I am planning to implement semantic
 search similarity. Given a domain keyword, I want to find the top 5 most similar matches. After embedding all 280k word
s, the size of the JSON file containing the embeddings is around 30GB.

I am new to this domain and evaluating the best 
options.

1. Should I use a cloud vector database like Pinecone or Typsense, or host locally on DigitalOcean?
2. If I go
 with a cloud option like Typsense, what configuration (RAM, etc.) would I need for 280k embeddings (30GB in size)? And 
how much would it likely cost?

I have been confused for the past few days and unable to find useful resources. Any help
 or advice you could provide would be greatly appreciated.
```
---

     
 
all -  [ Efficient Chunking Strategies for PDF Information Extraction with AI Tools ](https://www.reddit.com/r/LangChain/comments/1acudx2/efficient_chunking_strategies_for_pdf_information/) , 2024-01-29-0910
```
 Hello,

I'm working on extracting information from PDFs containing tables using OpenAI, LangChain, and FAISS. My focus 
is on extracting value especially regarding specific keywords present in these documents. I'm looking for advice on opti
mal chunking strategies for these PDFs to ensure comprehensive information extraction without losing key details. Any in
sights or best practices would be greatly appreciated!

Thank you!
```
---

     
 
all -  [ LangChain Blog on AI mental health therapy ](https://www.reddit.com/r/LangChain/comments/1acou6m/langchain_blog_on_ai_mental_health_therapy/) , 2024-01-29-0910
```
Nice blog article about how to build an AI therapist with LangChain: [https://blog.langchain.dev/mental-health-therapy-a
s-an-llm-state-machine/](https://blog.langchain.dev/mental-health-therapy-as-an-llm-state-machine/)
```
---

     
 
all -  [ Most capable function calling open source models? ](https://www.reddit.com/r/LocalLLaMA/comments/1ackxxt/most_capable_function_calling_open_source_models/) , 2024-01-29-0910
```
we've had a myriad of impressive tools and projects developed by talented groups of individuals which incorporate functi
on calling and give us the ability to create custom functions as tools that our ai models can call, however it seems lik
e they're all entirely based around openai's chatgpt function calling. 


my question is what open source models are you
 aware of that are consistently capable of recognizing when they have a function tool available and actually call them p
roperly?

i'd like to make more effective use of things like memgpt, autogen, langroid, langchain, gorilla, and a number
 of other great projects but i want to make sure i'm not wasting my time using models that aren't good at function calli
ng.

Edit: Adding models and links to them as I discover them or others recommend them so that people can easily find th
is info in one place. These are links to the original models by their original authors. In the case of unquantized model
s for quantized versions look for these models quantized by your favorite huggingface uploaders.

* [Dolphin-2.7-mixtral
-8x7b](https://huggingface.co/cognitivecomputations/dolphin-2.7-mixtral-8x7b)

* [Mistral-7B-Instruct-v0.2](https://hugg
ingface.co/mistralai/Mistral-7B-Instruct-v0.2)

* [NexusRaven-V2-13B](https://huggingface.co/Nexusflow/NexusRaven-V2-13B
)

* [Functionary-small-v2.2-GGUF](https://huggingface.co/meetkai/functionary-small-v2.2-GGUF)

* [Functionary-medium-v2
.2-GGUF](https://huggingface.co/meetkai/functionary-medium-v2.2-GGUF)

* [natural-functions-GGUF](https://huggingface.co
/cfahlgren1/natural-functions-GGUF)
```
---

     
 
all -  [ Singlestore Zoom call reviews ](https://www.reddit.com/r/dataengineering/comments/1aciszo/singlestore_zoom_call_reviews/) , 2024-01-29-0910
```


I’m sorry to be mean , but offlate some of the weekly zoom calls have really bad speakers . There is a guy who wears B
lippi glasses and when asked questions , he says the tutorial is in progress and asks the audience to follow his LinkedI
n profile . It sounds more like he is interested in getting followers rather than he knowing the subject . I doubt he kn
ows things about langchain, llama index , etc , when asked about it , he gives a nod and lame smile . These zoom calls w
ere excellent when Akmal ran the show . I never missed Akmal’s calls. Nowadays I get out of the call when that blippi jo
ins . 
#singlestore #weeklycalls
```
---

     
 
all -  [ Has anyone found a ChatGPT plugin that's better than web pilot or vox script at reading external con ](https://www.reddit.com/r/LLMs/comments/1achfsl/has_anyone_found_a_chatgpt_plugin_thats_better/) , 2024-01-29-0910
```
 

I use webpilot and vox script all the time and wondering if some people prefer something else.

I especially like bot
h because I can provide a url and get all that info in context, which seems like even ChatGPT 4 with Bing can't be relie
d on to do it consistently.

I have some examples in this article I generated.  
[https://www.learninternetgrow.com/real
-time-search-with-llms/](https://www.learninternetgrow.com/real-time-search-with-llms/)
```
---

     
 
all -  [ Has anyone found a ChatGPT plugin that's better than web pilot or vox script at reading external con ](https://www.reddit.com/r/OpenAI/comments/1achf51/has_anyone_found_a_chatgpt_plugin_thats_better/) , 2024-01-29-0910
```
 I use webpilot and vox script all the time and wondering if some people prefer something else.

I especially like both 
because I can provide a url and get all that info in context, which seems like even ChatGPT 4 with Bing can't be relied 
on to do it consistently.

I have some examples in this article I generated.  
[https://www.learninternetgrow.com/real-t
ime-search-with-llms/](https://www.learninternetgrow.com/real-time-search-with-llms/)  


Alternatively, looking for exa
mples where someone recreates this functionality in langchain.
```
---

     
 
all -  [ Has anyone found an example of coupling LangChain with external URL requests? ](https://www.reddit.com/r/LangChain/comments/1achbg7/has_anyone_found_an_example_of_coupling_langchain/) , 2024-01-29-0910
```
 

I use webpilot and vox script all the time and wondering if there are examples of achieving this with LangChain.

I e
specially like both because I can provide a url and get all that info in context, which seems like even ChatGPT 4 with B
ing can't be relied on to do it consistently.

I have some examples in this article I generated.  
[https://www.learnint
ernetgrow.com/real-time-search-with-llms/](https://www.learninternetgrow.com/real-time-search-with-llms/)  
 
```
---

     
 
all -  [ Query CSV code not working help! ](https://www.reddit.com/r/LangChain/comments/1aceuxq/query_csv_code_not_working_help/) , 2024-01-29-0910
```
    from langchain.chains import RetrievalQA
    from langchain.chat_models import ChatOpenAI
    from langchain.documen
t_loaders import CSVLoader
    from langchain.vectorstores import DocArrayInMemorySearch
    from IPython.display import
 display, Markdown
    from langchain.llms import OpenAI
    
    file = 'OutdoorClothingCatalog_1000.csv'
    loader = 
CSVLoader(file_path=file)
    print(loader)
    
    from langchain.indexes import VectorstoreIndexCreator
    
    inde
x = VectorstoreIndexCreator(
        vectorstore_cls=DocArrayInMemorySearch
    ).from_loaders([loader])
    
    query 
='Please list all your shirts with sun protection \
        in a table in markdown and summarize each one.'
    
    fro
m langchain_openai import ChatOpenAI
    
    model_name = 'gpt-3.5-turbo-instruct'
    llm_replacement_model = ChatOpen
AI(temperature=0.0, model=model_name, openai_api_key=openai.api_key)
    response = index.query(query, llm=llm_replaceme
nt_model
    

&#x200B;

&#x200B;

    ---------------------------------------------------------------------------
    V
alidationError                           Traceback (most recent call last)
    Cell In[22], line 5
          3 model_nam
e = 'gpt-3.5-turbo-instruct'
          4 llm_replacement_model = ChatOpenAI(temperature=0.0, model=model_name, openai_ap
i_key=openai.api_key)
    ----> 5 response = index.query(query, llm=llm_replacement_model)
    
    File ~/.pyenv/versio
ns/3.12.0/lib/python3.12/site-packages/langchain/indexes/vectorstore.py:46, in VectorStoreIndexWrapper.query(self, quest
ion, llm, retriever_kwargs, **kwargs)
         42 retriever_kwargs = retriever_kwargs or {}
         43 chain = Retrieva
lQA.from_chain_type(
         44     llm, retriever=self.vectorstore.as_retriever(**retriever_kwargs), **kwargs
        
 45 )
    ---> 46 return chain.run(question)
    
    File ~/.pyenv/versions/3.12.0/lib/python3.12/site-packages/langcha
in_core/_api/deprecation.py:145, in deprecated.<locals>.deprecate.<locals>.warning_emitting_wrapper(*args, **kwargs)
   
     143     warned = True
        144     emit_warning()
    --> 145 return wrapped(*args, **kwargs)
    
    File ~/.p
yenv/versions/3.12.0/lib/python3.12/site-packages/langchain/chains/base.py:538, in Chain.run(self, callbacks, tags, meta
data, *args, **kwargs)
        536     if len(args) != 1:
        537         raise ValueError('`run` supports only one 
positional argument.')
    --> 538     return self(args[0], callbacks=callbacks, tags=tags, metadata=metadata)[
        
539         _output_key
        540     ]
    ...
      Field required [type=missing, input_value={'embedding': [0.00682
570..., -0.02392816262769903]}, input_type=dict]
        For further information visit https://errors.pydantic.dev/2.5/v
/missing
    metadata
      Field required [type=missing, input_value={'embedding': [0.00682570..., -0.02392816262769903
]}, input_type=dict]
        For further information visit https://errors.pydantic.dev/2.5/v/missing

&#x200B;

&#x200B;


Help, this is from a course I'm taking on Deep learning
```
---

     
 
all -  [ How do i merge / combine two texts into one? ](https://www.reddit.com/r/LangChain/comments/1acbcqn/how_do_i_merge_combine_two_texts_into_one/) , 2024-01-29-0910
```
I am a noob experimenting with LLMs and i am looking for a reliable method for merging / combining two texts into one cr
edible sounding merged text. Does that take a langchain based RAG or am i simply too stupid to engineer the right prompt
 in a mixtral or something similar? :)
```
---

     
 
all -  [ Getting a structured response (user-defined class) from a custom fine-tuned Mistral model. ](https://www.reddit.com/r/LocalLLaMA/comments/1ac94rz/getting_a_structured_response_userdefined_class/) , 2024-01-29-0910
```
I saw examples using Langchain and OpenAI that you can set the desired output via a class. So, within a custom class, yo
u can set the attributes that you would want the model to send back. 

&#x200B;

I'm curious if there is a similar way o
f doing this but instead of using OpenAI, I would use my own Mistral-Instruct model. 

&#x200B;

Currently, I've only be
en playing around with the system prompt template, but the responses are not structured nor consistent. So, I would need
 to have multiple post-processing functions to clean the responses. 

&#x200B;

Is there an approach to get the response
s to be in a structured format every single time?  

```
---

     
 
all -  [ How to Maintain extracted Document Order ](https://www.reddit.com/r/LangChain/comments/1ac80ys/how_to_maintain_extracted_document_order/) , 2024-01-29-0910
```
How can I ensure that the order of extracted documents in Langchain is maintained? I have a RAG app that allows users to
 query documents, but I've noticed that some numbered data is extracted in the wrong order. 

For example, the documents
 may contain numbered items from 1 to 50, but when the final result is returned, the 2nd item may appear last and the 50
th item may appear first. I need to maintain the same order as it appears in the original document.
```
---

     
 
all -  [ What ist the advantage of Long Context Embedding Models for Rag ](https://www.reddit.com/r/LangChain/comments/1ac7t19/what_ist_the_advantage_of_long_context_embedding/) , 2024-01-29-0910
```
JinaAi just released an Embeddingmodel with a context size of 8k. I was wondering what are the advantages of Long Contex
t Embedding models for a Rag Use Case?

Happy for discussion!
```
---

     
 
all -  [ Document retrieval using llm's from long documents ](https://www.reddit.com/r/LangChain/comments/1ac32g9/document_retrieval_using_llms_from_long_documents/) , 2024-01-29-0910
```
Hi everyone....
Recently I have got a project where I need to retrieve some financial documents using RAG....The process
 is 
1. The query will be around 20 to 30 page long pdf document.
2. The document contains some information requirements
...Those requirements will be stored in my db....based on the requirements of the pdf I need to fetch the existing docum
ents from the db....

Can anyone please help me out with this.... Thanks in advance
```
---

     
 
all -  [ So close... Switching from Openai models to local models served by Ollama ](https://www.reddit.com/r/LangChain/comments/1abwoh6/so_close_switching_from_openai_models_to_local/) , 2024-01-29-0910
```
As the title says, I'm working to enable an app I wrote that generates SQL to allow it to work from a locally served LLM
 instead of one in the cloud. This is a requirement for a couple of customers, so I've been experimenting...

I'm using 
the create\_sql\_agent function... I'm supplying the prompts as well as some custom tools that feed in appropriate metad
ata about the database.  Against OpenAI or AzureOpenAI it works fine.

When I run against Ollama, I've tried a bunch of 
models - SQLcoder, LLama70b, Mixtral8x7b, etc.  And I get the same result... I can watch the agent work away (via my own
 debugging as well as LangSmith).. 

The agent runs typically follow the same general path as the OpenAI runs, with one 
exception - I can see the final SQL statement generated, but after executing the statement and getting a perfectly fine 
answer (and identifying it as such) it goes into a kind of loop and never exits the chain.  

I've toyed with supplying 
'stop=' tokens etc, but I just don't see what's going on.

There's so many moving pieces that I thought someone might ha
ve an idea where to look... 

It's possible that it's a prompt format issue - I know the prompt format between the Llama
 models and OpenAI models are pretty different... with special tokens, etc. but I'm utterly unclear how that would chang
e things, since up to the point it should 'exit' and return the final answer it works pretty well.

I'll add that I crea
ted a custom 'handler' to extract the final sql statement it creates, since the sql agent returns the 'answer' rather th
an the SQL statement.  My handler is looking for invocation of the sql\_db\_query tool which indicates that the sql has 
been generated and is being sent off for execution - I grab the string at that point and save it for later... that  work
s in openai, but not in any of the other models I've tried.

I do get some different results with different models...

M
ost have given the above general issue - generating a good answer, but then never stopping.

mixtral:8x7b-instruct-v0.1-
q5\_K\_M - was weird. It didn't seem to want to use the tools I provided and sort of skipped some steps.  It generated S
QL that had no relation to the actual database - so it wasn't using any of the tools - then when it came time to run the
 SQL it DID generate, it messed up that name of the sql\_db\_query tool:

'{'requested\_tool\_name': 'sql\\\\\_db\\\\\_q
uery', 'available\_tool\_names': \['sql\_db\_query', 'sql\_db\_schema', 'sql\_db\_list\_tables', 'sql\_db\_query\_checke
r', 'sql\_get\_few\_shot\_examples', 'sql\_get\_column\_descriptions', 'get\_column\_to\_table\_cross\_reference', 'get\
_hierarchies', 'sql\_get\_table\_descriptions'\]}'

No other model did this... 

SO, I'm wondering if anyone else has ha
d the same struggle, or can point me in some direction to figure this out... it feels like I'm so very close, just missi
ng one key ingredient!

Thanks!

&#x200B;
```
---

     
 
all -  [ Overcoming 8-10% Inaccuracy in PDF Keyword Extraction Using Faiss and OpenAI – Need Advice ](https://www.reddit.com/r/LangChain/comments/1abvyps/overcoming_810_inaccuracy_in_pdf_keyword/) , 2024-01-29-0910
```
 Hello everyone,

I'm working on a project using Langchain involving information extraction from PDF documents, each ran
ging from 5-10 pages. My primary goal is to extract information based on approximately 26 keywords, which I load from a 
CSV file.

Here's an overview of my current setup:

Basic Language Chain Components: I'm using a loader, a recursive spl
itter set to 500 with an overlap of 300, and an Ensemble Retriever BM25)and MultiQuery Retriever setup with FAISS, where
 each component has a .5 weight for each.

FAISS Library Usage: In the FAISS library, I'm employing the from\_documents 
method and a retriever.

OpenAI Integration: After combining the top 2 chunks for each keyword, I'm feeding the data int
o OpenAI with prompt.

However, I'm encountering an issue where the results are about 8-10% hallucinated or inaccurate.


I'm looking for advice on how to improve the accuracy of my information extraction process. Are there any specific para
meters or techniques in better chunking, FAISS or with OpenAI that I should consider consider or tweaking? Any insights 
or suggestions would be greatly appreciated!
```
---

     
 
all -  [ Need help improving RAG ](https://www.reddit.com/r/LangChain/comments/1abuv1f/need_help_improving_rag/) , 2024-01-29-0910
```
Hello everyone, I am just starting with RAG.

I want to retrieve building regulations ( max height, area, etc) informati
on from pdfs using a llm. 

the pdfs contains both text and data. I am currently using PypdfLoader from langchain to loa
d the pdfs. Splitting using recursive character split, embedding using open ai and storing it in chroma db.
 

Sometimes
 the llm doesn’t retrive the information correctly.  don’t know if it is because of the parsing of pdfs. 

Any help in i
mproving the system is greatly appreciated. Thanks.
```
---

     
 
all -  [ We can put scientific research papers into chatGPT and make our own medicine at any time ](https://www.reddit.com/r/RandomThoughts/comments/1abuj7n/we_can_put_scientific_research_papers_into/) , 2024-01-29-0910
```
Langchain.com looks nice 
```
---

     
 
all -  [ New openai v3 embeddings - are they working with langchain or not? ](https://www.reddit.com/r/LangChain/comments/1abrtev/new_openai_v3_embeddings_are_they_working_with/) , 2024-01-29-0910
```
So I read the blogpost from OpenAI on their new v3 embeddings models, and decided to try them in my app... I get an erro
r... so I simplified to the 4 line example from the langchain docs, which results in the same error: 

from langchain\_o
penai import OpenAIEmbeddings

    
    embeddings = OpenAIEmbeddings(model='text-embedding-3-large')
    
    query_res
ult = embeddings.embed_query('Some test text!!!')
    
    print(query_result[0:5])
    
    % python3 t.py
    Warning:
 model not found. Using cl100k_base encoding.
    [-0.0076643440879791275, 0.023873071539678815, -0.01047247064095197, 0
.006004269555153845, 0.0286252864226502]

Which seems odd, since I can execute the curl example from the openai docs, no
 problem:

    % curl https://api.openai.com/v1/embeddings \                 ✔  11:34:33
      -H 'Content-Type: appli
cation/json' \
      -H 'Authorization: Bearer xxxxx' \
      -d '{
        'input': 'Your text string goes here',
     
   'model': 'text-embedding-3-large'
      }'
    
    ...
            -0.02287454,
            -0.02287454,
           
 -0.022449568
          ]
        }
      ],
      'model': 'text-embedding-3-large',
      'usage': {
        'prompt_t
okens': 5,
        'total_tokens': 5
      }
    }

&#x200B;

When I refer to the langchain embedding docs, they've alre
ady been updated to show the new embeddings... BUT they are showing the same error RIGHT IN THEIR DOCs as well.

&#x200B
;

    from langchain_openai import OpenAIEmbeddings
    
    embeddings = OpenAIEmbeddings(model='text-embedding-3-larg
e')
    
    text = 'This is a test document.'
    
    Embed documents
    doc_result = embeddings.embed_documents([tex
t])
    
    Warning: model not found. Using cl100k_base encoding.
    
    doc_result[0][:5]
    
    [-0.0143800563773
83358,
     -0.027191711627651764,
     -0.020042716111860304,
     0.057301379620345545,
     -0.022267658631828974]

A
m i missing something??? 
```
---

     
 
all -  [ Can I combine LangChain with PrompFlow? ](https://www.reddit.com/r/LangChain/comments/1abpzp2/can_i_combine_langchain_with_prompflow/) , 2024-01-29-0910
```
I recently heard about promptflow, a tool to create end to end LLM processes. Is it more a competitor to langchain, can 
I combine both, or what is the difference to langchain?
```
---

     
 
all -  [ Langchain ChatModel import from 2 different library? ](https://www.reddit.com/r/LangChain/comments/1abomxb/langchain_chatmodel_import_from_2_different/) , 2024-01-29-0910
```
What is the difference between these two approaches for importing OpenAI chat models?'

***from*** **langchain\_openai**
 ***import*** **ChatOpenAI**  
***from*** **langchain.chat\_models** ***import*** **ChatOpenAI**

Does langchain-openai 
use the latest release of OpenAI or do they use the same version?
```
---

     
 
all -  [ X-Shot prompting with Langchain ](https://www.reddit.com/r/LangChain/comments/1abo6l5/xshot_prompting_with_langchain/) , 2024-01-29-0910
```
I was trying out X-shot prompting with Langchain but couldn't find some good relevant examples of how to form the prompt
 template for this. Specifically how should an example or examples be inserted into the prompt template and merged with 
proper instructions. Any useful examples or turtorials?
```
---

     
 
all -  [ Avoid duplicates inside a chroma db ](https://www.reddit.com/r/LangChain/comments/1abkaif/avoid_duplicates_inside_a_chroma_db/) , 2024-01-29-0910
```
Hello , lets say that we prompt the user to add documents , which the app chunks , embeds and adds to a vector database.
 

How can we avoid inserting the same document twice? Is there any way it can be done with langchain?

I really cant fi
nd a way around.
```
---

     
 
all -  [ What is the best open source LLM for outputting SQL code ](https://www.reddit.com/r/LangChain/comments/1abiozm/what_is_the_best_open_source_llm_for_outputting/) , 2024-01-29-0910
```
I am currently using Mixtral 8x7B Instruct v0.1 - GPTQ and was wondering what is currently the best open source LLM to u
se to output SQL code?

Would really appreciate any input on this. Many thanks!
```
---

     
 
all -  [ Switch to Assistants API from Chat completions to save on shared context bandwidth? ](https://www.reddit.com/r/LangChain/comments/1abheko/switch_to_assistants_api_from_chat_completions_to/) , 2024-01-29-0910
```
I have a QA-style few-shot style agent and it's prompt goes like this:  
\> You're a helpful assistant who's an expert i
n X, (explanation of its audience, task and output guardrails/format).

\> Examples:

\> Question: xxx

\> Answer:

\> \
`\`\`yyy\`\`\`  


Tokens utilization is pretty steep because of this large context that's being sent in full over and o
ver again for every request using Chat Completions API( [https://platform.openai.com/docs/guides/text-generation/chat-co
mpletions-api](https://platform.openai.com/docs/guides/text-generation/chat-completions-api) )

Is it possible to switch
 instead to Assistants API( [https://platform.openai.com/docs/assistants/overview/agents](https://platform.openai.com/do
cs/assistants/overview/agents) ) for such a task so that context is sent only as 1st system message and all questions ar
e just appended to that thread? 
```
---

     
 
all -  [ Claude says Anthropic made LangChain and Stable Diffusion ](https://www.reddit.com/r/ClaudeAI/comments/1abggq6/claude_says_anthropic_made_langchain_and_stable/) , 2024-01-29-0910
```
I noticed this in November. I thought I'd check back in a few months later to see if it's been fixed - it hasn't.

With 
a quick Google, I can see the information about LangChain has been replicated in some Medium articles. It's not the most
 harmful of hallucinations but it is surprising how convinced Claude is.

I'm interested in why this has happened. I fig
ured the documentation Claude is fine-tuned on heavily mentions AI products and Anthropic, leading it to overfit and def
ault to crediting Anthropic to other AI research and products. Does that sound reasonable? Any other ideas?

https://pre
view.redd.it/759tppzuurec1.png?width=757&format=png&auto=webp&s=1acd8c35197a2c93e74cfd2c25ba8987671a6ece

https://previe
w.redd.it/7ojltqzuurec1.png?width=741&format=png&auto=webp&s=c42e530d3ac0857f1d9b7b2a698bdcfe5e5d6fd5

https://preview.r
edd.it/zrh82rzuurec1.png?width=763&format=png&auto=webp&s=2b81c852a9996a241af81907013e83ff341e8400

https://preview.redd
.it/tw4v3uzuurec1.png?width=742&format=png&auto=webp&s=6c94d79e41753b112259a6f72fab00583d1ede8f
```
---

     
 
all -  [ RAG Chatbot with LCEL ](https://www.reddit.com/r/LangChain/comments/1abf7eo/rag_chatbot_with_lcel/) , 2024-01-29-0910
```
I found this blog articles on [https://blog.langchain.dev/building-chat-langchain-2/](https://blog.langchain.dev/buildin
g-chat-langchain-2/), about building a Rag Chatbot using langchain expression language. Looking at the entire code from 
the github repo, I am not pretty sure to understand what does this chain do:  
(

{

'question': RunnableLambda(itemgett
er('question')).with\_config(

run\_name='Itemgetter:question'

),

'chat\_history': RunnableLambda(serialize\_history).
with\_config(

run\_name='SerializeHistory'

),

}

| \_context

| response\_synthesizer

)  


It seems like: is gettin
g the question from a dictionary and pass it to the context etc..., but I can't see what's the input to the serialize\_h
istory function. I mean should not be chat\_history since it's the key assigned to the result of the function, it's not 
the input to the function right? 
```
---

     
 
all -  [ What is the best local LLM for agentic behavior? ](https://www.reddit.com/r/LangChain/comments/19fnp1g/what_is_the_best_local_llm_for_agentic_behavior/) , 2024-01-29-0910
```
I'm looking for the best LLM currently for agentic behavior in langchain. By best, I mean the most consistent with the l
east parsing errors.
```
---

     
 
MachineLearning -  [ New Data API for Astra [N] ](https://www.reddit.com/r/MachineLearning/comments/199uobn/new_data_api_for_astra_n/) , 2024-01-29-0910
```
I saw that DataStax/Astra DB [just released a new Data API to help with building production GenAI and RAG applications](
https://www.datastax.com/blog/general-availability-data-api-for-enhanced-developer-experience). This API makes the prove
n petabyte-scale of Apache Cassandra easy to use and available to any JavaScript, Python, or full-stack application deve
loper.

There will also be a joint webinar with LangChain available for registration here: [https://www.datastax.com/eve
nts/wikichat-build-a-real-time-rag-app-on-wikipedia-with-langchain-and-vercel](https://www.datastax.com/events/wikichat-
build-a-real-time-rag-app-on-wikipedia-with-langchain-and-vercel)
```
---

     
 
MachineLearning -  [ [D] While using function calling or tools on openai or langchain, does openai have access to the dat ](https://www.reddit.com/r/MachineLearning/comments/199t8be/d_while_using_function_calling_or_tools_on_openai/) , 2024-01-29-0910
```
I am working on a client project and I am using langchain's tools and agents. I want to know if the data is getting pass
ed to openai or is it just like that - Output of one function is being directly passed to the second function with the k
nowledge of openai.
```
---

     
 
MachineLearning -  [ [D] Code vs JSON output for LLM agents? Frameworks like LangChain rely on LLMs responding with JSON  ](https://www.reddit.com/r/MachineLearning/comments/197f416/d_code_vs_json_output_for_llm_agents_frameworks/) , 2024-01-29-0910
```
[CaP](https://arxiv.org/pdf/2209.07753.pdf), [Voyager](https://arxiv.org/pdf/2305.16291.pdf), [Octopus](https://arxiv.or
g/abs/2310.08588)

I work primarily with JSON based agents but code-as-policy agents seem to be extremely powerful. Here
 are some of the benefits and weaknesses I've seen

Pros of code

1. Less tool creation needed - The prebuilt math/file/
string/list manipulation abilities that come with code are enormous. In a JSON based agent, you would have to formally d
eclare each of these as a tool which you expose to the LLM and explain in your prompting, which is a lot of work and eat
s up a ton of the context window. 
2. Reduced number of transactions - The LLM can write scripts that invoke multiple to
ols and manipulate their results in ways that are difficult to do in a single transaction via JSON. For example, in one 
script, the model could search a DB 3 times, perform regex on the query results, convert them to integers, and add them 
up. Doing this in one step via JSON tool invocations is basically impossible. 
3. Less syntax errors - this might be tot
ally just vibe-based reasoning, but it really seems like LLMs have an easier time writing valid python than valid JSON, 
especially when you have lots of nested arguments in your methods.

Cons

1. Crazy risky - This is the obvious one. You 
have a machine executing random code. There are ways to mitigate this but still. I mean seriously we all learned not to 
use eval, so it is crazy to basically see research tending towards just running eval on the outputs of these models. 
2.
 Scripts with errors - Sometimes the model tries to get too fancy and writes complex programs that have bugs, resulting 
in many needed retries. 

Do any of you have thoughts or experience with these approaches in the wild? 

Is anybody awar
e of any experiments that compare these two approaches against each other? 

&#x200B;
```
---

     
 
MachineLearning -  [ [D] Are Custom LLM RAG apps going to become redundant? ](https://www.reddit.com/r/MachineLearning/comments/1929n4f/d_are_custom_llm_rag_apps_going_to_become/) , 2024-01-29-0910
```
Loks like Copilot Studio is being rolled out (https://www.microsoft.com/en-us/microsoft-copilot/microsoft-copilot-studio
) with an impressive looking no code/out of the box RAG solution.

There is a phenomenal amount of development and activ
ity in the Open Source RAG world (e.g Langchain, Llamaindex, etc), which I am a great supporter of FYI.

However, what s
eems strange is that this no code out of the box solution (Copilot Studio - just as an example of one) seems overwhelmin
gly to be the better option if you wanted to build a RAG app i.e If you compare the cost to build and productionise a cu
stom RAG app vs the cost of using Copilot Studio, it's almost an order of magnitude lower (no matter how you cut it with
 the developer time and duration). 

My question is, it seems to me we are moving towards a situation where enterprise s
olutions will make custom RAG apps redundant (not in all cases of course, but most cases), however there seems to be ver
y little discussion of this relative to the activity in the open source community. Do people agree this is a likely scen
ario? 

Obviously there will be exceptions…but on most use cases I don’t see how you can compete with an instant/minimal
 setup, low cost, highly scalable RAG solution.
```
---

     
 
MachineLearning -  [ [P] An open-source project for deploying local models ](https://www.reddit.com/r/MachineLearning/comments/18zkm5m/p_an_opensource_project_for_deploying_local_models/) , 2024-01-29-0910
```
 Introducing a new LLM WebUI project that supports various local model loading and provides streaming output for cutting
-edge online multimodal models GPT-4-Vision and Gemini-Pro-Vision. Completely free and open source, it serves as a valua
ble research tool for exploring diverse models. The project is actively under development with continuous updates:  
[ht
tps://github.com/smalltong02/keras-llm-robot](https://github.com/smalltong02/keras-llm-robot)

&#x200B;

[WebUI](https:/
/preview.redd.it/f95jievpepac1.png?width=2560&format=png&auto=webp&s=1f2908b484ededc78591719ef87efdac2f9497ba)

&#x200B;


[Configuration](https://preview.redd.it/owaj5s1repac1.png?width=2560&format=png&auto=webp&s=f837b1ef67cb8e4ccaee4ec602
a61859f53db100)

&#x200B;

[Tools & Agent](https://preview.redd.it/jrot8w9sepac1.png?width=2560&format=png&auto=webp&s=7
1e224f08620941146cd437a99bcb55d02930a9e)
```
---

     
 
MachineLearning -  [ [Project] Temporal Augmented Retrieval (TAR) - Dynamic RAG ](https://www.reddit.com/r/MachineLearning/comments/18uddmj/project_temporal_augmented_retrieval_tar_dynamic/) , 2024-01-29-0910
```
From a corpus of text, how can you detect emerging topics and their evolution through time?

Introducing Temporal Augmen
ted Retrieval (TAR). (built in the context of buildspace n&w s4)

TAR is an open-source advanced RAG approach that aims 
to factor in the dynamic and temporal aspects of textual data when performing retrieval.

It allows us to understand the
 evolution of discussed topics over time.

The idea behind this project is to open the debate regarding the current limi
tations of RAG methods

This first approach has been built without using RAG frameworks (like Jerry Liu’s langchain) and
 focuses on financial tweets 

Relevant links:

Medium: [https://medium.com/@adam-rida/temporal-augmented-retrieval-tar-
dynamic-rag-ad737506dfcc](https://medium.com/@adam-rida/temporal-augmented-retrieval-tar-dynamic-rag-ad737506dfcc)

Gith
ub:[https://github.com/adrida/Temporal\_RAG](https://github.com/adrida/Temporal_RAG)

Hugging Face Benchmark: [https://h
uggingface.co/spaces/Adr740/Temporal-RAG-Benchmark](https://huggingface.co/spaces/Adr740/Temporal-RAG-Benchmark)

My web
site: [adrida.github.io](https://adrida.github.io)

&#x200B;

https://preview.redd.it/lj7wkhk70f9c1.png?width=960&format
=png&auto=webp&s=fc79c5034351a1711e1ec051919a5c4d2edbc333
```
---

     
 
MachineLearning -  [ [R][P] Autogen + Langchain Tools + Local LLM doesn't work. ](https://www.reddit.com/r/MachineLearning/comments/18tex1j/rp_autogen_langchain_tools_local_llm_doesnt_work/) , 2024-01-29-0910
```
Hey folks, 

So I'm playing around with the agent framework Autogen and I'm trying to create agents by providing it cust
om tools to use. These custom tools are defined in the langchain framework. Furthermore, I am using open source LLM mode
ls like Mistral, LLAMA, Mixtral etc.

In my experience, I have been unable to get the Autogen+LocalLLM framework to iden
tify the right tools to use given the prompt. However it does a fantastic job with the GPT model. 

Please note that my 
goal is for the agent to mandatorily use the tools provided and not come up with its own code. And the agent should figu
re out the right tool to use. 

I have been very explicit with my prompting, despite which I am unable to get this to wo
rk.

Any thoughts and suggestions? Please let me know ! Please share your experiences as well. Cheers !
```
---

     
 
deeplearning -  [ [D] Unleashing the Power of Langchain with Wandb: Revolutionizing Topic Modeling and Evaluation ](https://www.reddit.com/r/deeplearning/comments/191mm83/d_unleashing_the_power_of_langchain_with_wandb/) , 2024-01-29-0910
```
Complementing Langchain’s prowess, Wandb emerges as a powerhouse meticulously designed for developers leveraging LLM tec
hnology. As an evaluation framework and production monitoring platform, Wandb stands out for its tailored approach. Its 
arsenal comprises real-time monitoring, granular analytics, and streamlined evaluation processes, laying the groundwork 
for elevated performance and reliability in AI applications.

&#x200B;

Link: [https://medium.com/ai-advances/unleashing
-the-power-of-langchain-with-wandb-revolutionizing-topic-modeling-and-evaluation-75af5cf51b15](https://medium.com/ai-adv
ances/unleashing-the-power-of-langchain-with-wandb-revolutionizing-topic-modeling-and-evaluation-75af5cf51b15) 
```
---

     
