 
all -  [ Simplified Function Calling (LiteLLM/OpenAI Compatible) [Python] ](https://www.reddit.com/r/ChatGPTCoding/comments/1bi1efy/simplified_function_calling_litellmopenai/) , 2024-03-19-0910
```
I've created a simple wrapper for JSON function descriptions when using either OpenAI or LiteLLM APIs.

I really like li
braries like Langroid and Langchain, but sometimes the abstraction they implement takes away too much control. As such, 
this package is solely for making tool calls easier to create using the base APIs, and eliminating the need for manual J
SON formatting.

Check it out here! [https://github.com/A-M-D-R-3-W/llmFunctionWrapper](https://github.com/A-M-D-R-3-W/l
lmFunctionWrapper)

&#x200B;

https://preview.redd.it/kmm44ltpm5pc1.png?width=2000&format=png&auto=webp&s=4037792c958b9b
313eef29bdca0c03260ca3655d
```
---

     
 
all -  [ Simplified Function Calling (OpenAI/LiteLLM Compatible) [Python] ](https://www.reddit.com/r/ChatGPTPro/comments/1bi135j/simplified_function_calling_openailitellm/) , 2024-03-19-0910
```
I've created a simple wrapper for JSON function descriptions when using either OpenAI or LiteLLM APIs.

I really like li
braries like Langroid and Langchain, but sometimes the abstraction they implement takes away too much control. As such, 
this package is solely for making tool calls easier to create using the base APIs, and eliminating the need for manual J
SON formatting.

Check it out here! [https://github.com/A-M-D-R-3-W/llmFunctionWrapper](https://github.com/A-M-D-R-3-W/l
lmFunctionWrapper)

&#x200B;

https://preview.redd.it/ma51dzo9j5pc1.png?width=2000&format=png&auto=webp&s=7580996a265e41
fcb4c758d4d9a56dcf25c8c2c0
```
---

     
 
all -  [ open source RAG observability in llama index with 2 lines of code ](https://www.llamaindex.ai/blog/one-click-open-source-rag-observability-with-langfuse) , 2024-03-19-0910
```

```
---

     
 
all -  [ Simplified Function Calling (LiteLLM/OpenAI Compatible) [Python] ](https://www.reddit.com/r/LocalLLaMA/comments/1bhzwwb/simplified_function_calling_litellmopenai/) , 2024-03-19-0910
```
I've created a simple wrapper for JSON function descriptions when using either LiteLLM or OpenAI APIs. Local models are 
supported on LiteLLM as well.

I really like tools like Langroid and Langchain, but sometimes the abstraction they imple
ment takes away too much control. As such, this package is solely for making function calls easier to create using the b
ase APIs, and eliminating the need for manual JSON formatting.

Check it out here! [https://github.com/A-M-D-R-3-W/llmFu
nctionWrapper](https://github.com/A-M-D-R-3-W/llmFunctionWrapper)

&#x200B;

https://preview.redd.it/72v88zlua5pc1.png?w
idth=2000&format=png&auto=webp&s=23edb4381255e385e19b713b4d9de30fe78609c1
```
---

     
 
all -  [ Struggling to fine-tune my RAG application Is there a better way to test different parts? ](https://www.reddit.com/r/LangChain/comments/1bhyk5e/struggling_to_finetune_my_rag_application_is/) , 2024-03-19-0910
```
I've been working on a Retrieval-Augmented Generation (RAG) application, but I'm getting stuck trying to optimize it.  T
he core model seems okay, but I'm not sure how to tell if my prompts, chunking strategy, or retrieval method are working
 best.

Right now, it feels like a lot of trial and error, tweaking things one at a time and hoping for improvement.  Is
 there a more systematic way to approach this?  Ideally, I'd like to be able to test each part of the RAG pipeline indep
endently to see what's giving me the biggest gains.

Anyone have experience with this?  Maybe some tools or techniques o
ut there to make RAG development less frustrating?
```
---

     
 
all -  [ Extract info from invoices as JSON ](https://www.reddit.com/r/LangChain/comments/1bhxz1i/extract_info_from_invoices_as_json/) , 2024-03-19-0910
```
Hello Everyone,
How do I extract data from invoices as a structured output (preferably JSON) using Langchain and OpenAI?

```
---

     
 
all -  [ Complex PDF Chunking: Which one works better for you: RecursiveCharactersplitter or Unstructured.io ](https://www.reddit.com/r/LangChain/comments/1bhv87c/complex_pdf_chunking_which_one_works_better_for/) , 2024-03-19-0910
```
Hi,

I built a RAG app with complex pdfs and now want to find the best chunking strategy for complex pdfs. Here I wanted
 to discuss if (from your experience) the RecursiveCharaterSplitter from Langchain or chunking the docs by title with th
e UnstructuredFileLoader from Langchain worked better?

&#x200B;

This is how I implemented both but I am not sure which
 one I should use. Generally I think Unstructured should be better but when evaluating results with RAGAS, somehow the R
ecursiveCharacterSplitter is better.

`if chunking_strategy == 'recursive':`  
 `loader = DirectoryLoader(directory_path
,`  
 `glob='*.pdf',`  
 `loader_cls=PyPDFLoader)`  
 `documents = loader.load()`  
 `text_splitter = RecursiveCharacter
TextSplitter(chunk_size=chunk_size,`  
 `chunk_overlap=chunk_overlap,`  
 `#length_function = len`  
`)`  
 `texts = tex
t_splitter.split_documents(documents)`  
 `if chunking_strategy == 'unstructured':`  
 `texts = []`  
 `for i in files:`
  
 `loader = UnstructuredFileLoader(`  
 `i, strategy='hi_res', mode='elements', chunking_strategy='by_title',`  
 `ocr
_languages='eng+deu',`  
 `max_characters=4000,`  
 `new_after_n_chars=3800,`  
 `combine_text_under_n_chars=2000`  
`)`
  
 `docs = loader.load()`  
 `texts.append(docs)`  
   
 
```
---

     
 
all -  [ Hi I'm a senior machine learning engineer, looking for for buddies to build cool stuff with! ](https://www.reddit.com/r/LangChain/comments/1bhsecq/hi_im_a_senior_machine_learning_engineer_looking/) , 2024-03-19-0910
```
I'm looking to explore and experiment with fellow passionate engineers. I hope for an iron sharpens iron type scenario. 
Reach out if anyone would like to ideate and see what cool things we can create together. 
```
---

     
 
all -  [ Multi-Agent Debate using LangGraph  ](https://www.reddit.com/r/LangChain/comments/1bhscn6/multiagent_debate_using_langgraph/) , 2024-03-19-0910
```
Hey everyone, check out how I built a Multi-Agent Debate app which intakes a debate topic, creates 2 opponents, have a d
ebate and than comes a jury who decide which party wins. Checkout the full code explanation here : https://youtu.be/tEkQ
mem64eM?si=4nkNMKtqxFq-yuJk
```
---

     
 
all -  [ Slight difference in embeddings ](https://www.reddit.com/r/LangChain/comments/1bhr2k8/slight_difference_in_embeddings/) , 2024-03-19-0910
```
I have created a chromadb with `OpenAIEmbeddings(model='text-embedding-ada-002', show_progress_bar=True,chunk_size=20)` 
 
I took a document from the DB and using .get() I got its embeddings.

I also calculated embeddings using same class an
d `.embed_query()`

I subtracted and then `.sum()` and got a difference of `0.0001654693725411943`.

I would expect a mu
ch smaller difference if not 0

Any explanations?
```
---

     
 
all -  [ Working with Nemo Guardrails ](https://www.reddit.com/r/LangChain/comments/1bhpz1v/working_with_nemo_guardrails/) , 2024-03-19-0910
```
Hello Guys,

Anyone working with Nemo Guardrails? I created a flow but when the chat is not getting caught by either of 
the flows and the question is going to ChatGPT instead of going to the RAG I created.

I had to do something like the be
low:

Def flow
       User …
       

Only the above is working no matter how many name changes I make to the flow. Ther
e are bunch of don’t reply stuff that are there when user asks bad questions. The last one is the one that should collec
t the message and execute the RAG.

Anyone worked with this??
```
---

     
 
all -  [ Text summarization of technical reports more than 30 pages ](https://www.reddit.com/r/LangChain/comments/1bhomrn/text_summarization_of_technical_reports_more_than/) , 2024-03-19-0910
```
Greetings, i am trying to find whats the best way to tackle this problem. 

Dont know if i should start with local LLMs 
(models from hugging face etc), or go with text summarization APIs which i think will have limitations due to the text t
echnicalities and size. Or finally go with the big boys gpt-4,claudie etc. 

&#x200B;

I would love to have an up to dat
e answer from people that have tried simmilar approaches and what would be the best cost-effective way to go about it. m
uch appreciated. 

&#x200B;

PS: I dont have the technical capability to go for a full custom model on my own, i am a de
v but dont have huge programming experience on the AI stuff to optimize parameters on my own.
```
---

     
 
all -  [ Any way to do RAG with a Neo4j knowledge graph using Llama2? ](https://www.reddit.com/r/learnmachinelearning/comments/1bhn9bu/any_way_to_do_rag_with_a_neo4j_knowledge_graph/) , 2024-03-19-0910
```
Basically the title. I have seen lots of approaches to do RAG with knowledge graphs using Neo4j and Langchain, problem i
s, they need paid API keys of OpenAI to work. Can anyone help with doing RAG on Neo4j knowledge graphs, with open source
 LLMs like Llama2 and open source embedding models like MiniLM-L6-v2?
```
---

     
 
all -  [ Apply RAG on an already finetuned Llama Based Model ](https://www.reddit.com/r/LocalLLaMA/comments/1bhmpm1/apply_rag_on_an_already_finetuned_llama_based/) , 2024-03-19-0910
```
I am trying RAG for the first time and saw tons of tutorials using Llamaindex and Langchain to apply RAG on LLM's direct
ly downloaded from HuggingFace.

In my case I have a finetuned model from Llama, which I happen to have the finetuned we
ights stored locally in .bin format (pytorch\_model\_00001\_of\_00003 ...)

What is the correct method to apply RAG to t
his finetuned Model? Should I create my own prompt modification as I can't use any system\_prompt utility.

&#x200B;
```
---

     
 
all -  [ Anything substantial? ](https://www.reddit.com/r/LangChain/comments/1bhm4oe/anything_substantial/) , 2024-03-19-0910
```
Hey guys, I was wondering is you were already able to build something substantial that really helps you getting things d
one? People tend to say that the LLM's are not ready for high Level Agents yet but I think they're more than intelligent
 enough to call the right tools if presented with the right information about the current situation. A task seems like t
he execution of tools at the right time in the right order to me.

Any insights on why I might be wrong and/or any insig
hts on your experiences?
```
---

     
 
all -  [ Deploying Mistral 7B - Quantization Methods, Hosting Options etc. (for the GPU poor) ](https://www.reddit.com/r/LangChain/comments/1bhkuja/deploying_mistral_7b_quantization_methods_hosting/) , 2024-03-19-0910
```
I'm trying to deploy a Mistral 7B api endpoint for a RAG application I'm building. A few major things I'm confused about
 - I'm GPU poor :( so was planning on using AWS sagemaker to deploy the model - the 2 month free plan has 125 hours of m
4.xlarge or m5.xlarge instance per month on Inference - would that be enough to set up an endpoint for quantized mistral
 (I'm thinking 5-bit)? And like if you don't have a GPU yourself and are a broke student what's the go-to for model host
ing? Just need it for my final year project so it's not a long-term thing.  
Also I'm confused about the quantization ty
pes and methods - first out of AWQ, GGUF and GPTQ I'm leaning towards AWQ for it's efficiency, but I've heard that the d
ownside to it is the limited support? If I just want to deploy TheBloke's AWQ model, that shouldn't be anything particul
arly difficult right? Also is that the only downside to AWQ of could it potentially require more RAM? Also was looking a
t the deployment methods themselves - openllama, vllama etc. I was leaning towards vllama because again efficiency - has
 like double the throughput of Huggingface TGI, which I was using until this point. But then saw someone say something a
bout how it might require more VRAM? So advice please - What are my hosting options, what quantization method should I b
e using, within these v limited resources what are my options for making this model as fast as possible?  
Note: Ik for 
most cases it can't be helped and I will have to compromise on model speed, but I want to use the model for metadata ext
raction of chunks too, and if I'm feeding this model 100s of chunks, I need it to not be slow to the point of impractica
lity lol. 
```
---

     
 
all -  [ Has anyone here built a semantic layer ? Does anyone have sample code? ](https://www.reddit.com/r/LangChain/comments/1bhjtga/has_anyone_here_built_a_semantic_layer_does/) , 2024-03-19-0910
```
According to definition - a semantic layer is a structured representation of data that enhances context and ensures corr
ectness. Means business language to data structure or something like that. Have you worked on this? how to build this? i
s this any useful? 
```
---

     
 
all -  [ A Recommendation Chatbot based on Product description  ](https://www.reddit.com/r/LangChain/comments/1bhj62a/a_recommendation_chatbot_based_on_product/) , 2024-03-19-0910
```
Hi all,

I'm working on a project to create a Chatbot using opensource LLMs. The main objective is to recommend products
 to a user based on their queries or chat history along with Q&A. I've not been able to find a suitable guide or rather 
I've been looking for the wrong thing. The Chatbot should be able to explain why it recommended a product and what I hav
e currently is a document containing the details along with benefits/key features of each product. How do you guys think
 I should approach this problem? On one hand the document is small enough for me to just use it as a prompt but I'm not 
sure how to do that using ollamas models and on the other hand I wanted to try making something along the lines of knowl
edge graphs to add more features later on. If you have any pointers at all, please let me know!
```
---

     
 
all -  [ Faiss similarity search with csv/excel ](https://www.reddit.com/r/LangChain/comments/1bhibdh/faiss_similarity_search_with_csvexcel/) , 2024-03-19-0910
```
Doesn't FAISS play well with chunked embeddings of csv data? If im attaching all the data with the openai request it wor
ks well. But once ai chunk the csv and create embeddings, faiss seems to not be able to get the answers right. I have ob
served that the closer the data requested us to the headers, the more accurate it becomes. Are there any other alternati
ve? I've tried out the csv agents and returns precise data but fails in handling other types of questions like generatin
g quizes from the csv data. Any suggestions and opinions are appreciated.
```
---

     
 
all -  [ ConversationBufferMemory - isolated session/users Langchain chatbot? ](https://www.reddit.com/r/LangChain/comments/1bhgps9/conversationbuffermemory_isolated_sessionusers/) , 2024-03-19-0910
```
One of the Streamlit app I created is a chatbot using Ollama and Langchain lib. The chat has to be able to communicate w
ith the user and use some RAGs (which I use chromadb / as\_retriever)

The issue that I am encountering is the Conversat
ionBufferMemory not unique for a session and every time someone is using the streamlit app it keep adding more and more 
chat history to it.

&#x200B;

Does anyone know how to make this below unique per session or user\_id?

memory = Convers
ationBufferMemory(memory\_key='chat\_history', return\_messages=True, output\_key='answer',  
 input\_key='question')

&
#x200B;

Thanks
```
---

     
 
all -  [ [llama_index] How to create VectorStoreIndex based on already existing chromadb. ](https://www.reddit.com/r/LocalLLaMA/comments/1bhfyov/llama_index_how_to_create_vectorstoreindex_based/) , 2024-03-19-0910
```
I am trying to use llama\_index with already existing chromadb. No matter what I have tried, I had no success, in most c
ases resulting with this error:  


    chromadb.errors.InvalidDimensionException: Embedding dimension 1536 does not mat
ch collection dimensionality 384

I have tried switching the embedding functions. Used SentenceTransformers, then used H
uggingFaceEmbedding (llama\_index), then did some mixtures with LangchainEmbedding (llama\_index), and there is no way I
 can make it work. In all cases I've tried, I'm passing exactly the same function to both chromadb and llama\_index, but
 that doesn't change anything at all.  


Here is a code my issue is about:  


    sentence_transformer_ef = embedding_
functions.SentenceTransformerEmbeddingFunction(model_name='all-MiniLM-L6-v2')
    
    chroma_client = chromadb.Persiste
ntClient(path='vector_database')
    collection = chroma_client.get_or_create_collection(name='123456', embedding_functi
on=sentence_transformer_ef)
    
    vector_store = ChromaVectorStore(chroma_collection=collection)
    storage_context 
= StorageContext.from_defaults(vector_store=vector_store)
    
    index = VectorStoreIndex.from_vector_store(
        v
ector_store,
    )

Is there an error in my code, since it keeps saying 1536 dimensions, or could something else be done
 about it?  


Thank you in advance.
```
---

     
 
all -  [ Does it make sense to store chat message history in vector DB? ](https://www.reddit.com/r/LangChain/comments/1bh8o17/does_it_make_sense_to_store_chat_message_history/) , 2024-03-19-0910
```
I want to store the chat message history in a vector store to pass to my chat bot as context. I'm wondering what the bes
t way to do it is.

Should I store both the prompt and response as a single string? Or just the response, and keep the p
rompt as metadata? What about the system message? Should all the message history be stored as a single vector? 

I have 
lots of questions :)
```
---

     
 
all -  [ Python-LLM - LangChain - Q&A Application with Financial Data ](https://www.reddit.com/r/u_SravzLLC/comments/1bh64uj/pythonllm_langchain_qa_application_with_financial/) , 2024-03-19-0910
```
 

**### Use Case**

Use LangChain to Create Q&A Application on Sravz Financial Data

**Session 1**

&#x200B;

* Overvie
w of the architecture
* High-level description of LangChain - Loaders, Tool, Agent, LLM
* Perform sample queries

Docume
ntation Link: https://docs.sravz.com/docs/tech/python/langchain/

Code: https://gist.github.com/sravzpublic/636a989f933f
7b53dcf5935e780fd9f4

Video Explanation: https://youtu.be/[rruQ4shvJVM](https://youtu.be/rruQ4shvJVM)

Sravz LLC Analyti
cs & Tech Series:

Documentation - Source code: 

Analytics: https://docs.sravz.com/docs/analytics/

Tech: https://docs.
sravz.com/docs/tech/

Follow Us:

Youtube: [https://www.youtube.com/channel/UCZEu1jWMOuknydEi0bcJLvA](https://www.youtub
e.com/channel/UCZEu1jWMOuknydEi0bcJLvA)

Facebook: [https://www.facebook.com/Sravz-Ltd-105045281812833/](https://www.fac
ebook.com/Sravz-Ltd-105045281812833/)

Instagram: [https://www.instagram.com/sravz\_llc/](https://www.instagram.com/srav
z_llc/)

Twitter: [https://twitter.com/Sravz46106283](https://twitter.com/Sravz46106283)

LinkedIn: [https://www.linkedi
n.com/company/sravz-ltd?trk=public\_profile\_experience-group-header](https://www.linkedin.com/company/sravz-ltd?trk=pub
lic_profile_experience-group-header)

Medium: [https://medium.com/@sravzllc](https://medium.com/@sravzllc)

Reddit: http
s://www.reddit.com/user/SravzLLC

GitHub: [https://github.com/sravzpublic](https://github.com/sravzpublic)

Gitter: [htt
ps://gitter.im/sravzpublic/community?utm\_source=share-link&utm\_medium=link&utm\_campaign=share-link](https://gitter.im
/sravzpublic/community?utm_source=share-link&utm_medium=link&utm_campaign=share-link)

Discord: [https://discord.com/cha
nnels/917183474824273990/917183475289825342](https://discord.com/channels/917183474824273990/917183475289825342)

\#open
ai #chatgpt #python #langchain  #finance #analytics #backtest #pyfolio #c++ #stocks #websockets #ibkr #trading #marketsc
anner #leveragedfunds 
```
---

     
 
all -  [ My retrieval from a specific URL is bringing nothing. Looking for alternatives ](https://www.reddit.com/r/LangChain/comments/1bh5yrw/my_retrieval_from_a_specific_url_is_bringing/) , 2024-03-19-0910
```
Hey guys how are you?  
Quite new to this library and would like to ask some questions. I have a specific task to answer
 some questions with an agent created with langChain. I'm not sure if it's because of the site or it's because of some m
isinterpretation.   


The retrieval from the URL in question is bringing nothing. I even tried by other more traditiona
l web scrapping methods but always the return is just the meta pixel from Facebook and just a few lines with none of the
 text that I'm looking for.  


Do you have any idea or alternatives that I can retrieve this data from and create a con
text for my agent?  


thanks!
```
---

     
 
all -  [ Output parser not giving valid json, am I doing something wrong? ](https://www.reddit.com/r/LangChain/comments/1bh4ur6/output_parser_not_giving_valid_json_am_i_doing/) , 2024-03-19-0910
```
llm = Ollama(model='dolphin-mistral', temperature=3.0,  
 callback\_manager=CallbackManager(\[StreamingStdOutCallbackHan
dler()\]))  


class CaseSummary(BaseModel):  
issue: str = Field(description='Issue of the Support Case')  
root\_cause
: str = Field(description='Root Cause for the issue')  
resolution: str = Field(description='Resolution for the issue') 
 


\# Set up a parser + inject instructions into the prompt template.  
parser = JsonOutputParser(pydantic\_object=Case
Summary)  


prompt = PromptTemplate(  
 template='''  
You are an expert Support Engineer.  
Help me to summarize the b
elow case into issues, root causes and resolutions if any.  
Each bullet point should be a full sentence.  
Avoid showin
g any person name.  
If you do not know the answer, say UNKNOWN.  
Write ONLY the json as a valid format  
{format\_inst
ructions}  
Case:\\n{case}  
''',  
 description='Support Case Summary',  
 input\_variables=\['case'\],  
 partial\_var
iables={'format\_instructions': parser.get\_format\_instructions()},  
)  


\# And a query intented to prompt a languag
e model to populate the data structure.  
query = 'My PC is too slow.'  
chain = prompt | llm | parser  


chain.invoke(
{'case': query})
```
---

     
 
all -  [ Anthropic responding in foreign languages ](https://www.reddit.com/r/Anthropic/comments/1bh47q8/anthropic_responding_in_foreign_languages/) , 2024-03-19-0910
```
I am using Anthropic via the API. I am using LangChain in JS and am playing around with all three Claude 3 models.

I ha
ve a fundamental problem that I seem unable to fix. The models mostly respond in foreign languages! So far, I have had R
ussian, Portuguese and Japanese. I have no idea why this is, there is certainly no instruction in my prompt, and my atte
mpts to coerce it with things such as, 'Respond only in English', do not work.

It is very odd. Anyone know why this mig
ht be?

&#x200B;
```
---

     
 
all -  [ Is there a simple way to install all modules that a module depends on? ](https://www.reddit.com/r/learnpython/comments/1bh38vi/is_there_a_simple_way_to_install_all_modules_that/) , 2024-03-19-0910
```
I am a noobie when it comes to python, but is there a way to automatically install all the modules that a module require
s?

I'm trying to create a project with langchain and I installed via pip install langchain but almost all of the submod
ules I'm trying to work with are throwing errors left and right due to other modules not being installed and I am slowly
 going through them one by one to get them installed.

Is is possible to just run a single command and install all of th
em at once? Thanks!
```
---

     
 
all -  [ Inference ](https://www.reddit.com/r/LangChain/comments/1bh1v92/inference/) , 2024-03-19-0910
```
Beginner question:

I’m just learning about LangChain and curious if it can perform inference by itself or is it more of
 an orchestrator that uses external engines (ie Sagemaker)?

If I wanted to run LangChain locally to test a RAG implemen
tation can it use a local model?

What are my options for local inference? I’ve heard or Ollama and Llama.cpp. Are these
 required? Are there other well known ones I should look into?

Thanks for the help
```
---

     
 
all -  [ Create sql agent with langchain for query sql db  ](https://www.reddit.com/r/LangChain/comments/1bgwflw/create_sql_agent_with_langchain_for_query_sql_db/) , 2024-03-19-0910
```
Firstly I connected db then  converted db to text then with embedding I stored in chromadb now I want query execute by m
y chromdb I want to sql chain intialization with vector db can anyone help me please dm 
```
---

     
 
all -  [ Am I Missing Something? Langchain API Naming Seems Odd ](https://www.reddit.com/r/LangChain/comments/1bgvu2f/am_i_missing_something_langchain_api_naming_seems/) , 2024-03-19-0910
```
Langchain API naming is confusing, for some reason, it's focusing on where things are coming from:

    PromptTemplate.f
rom_template
    ChatPromptTemplate.from_template
    ChatPromptTemplate.from_messages

Why not using more descriptive n
ame like:

    prompt.chat.template 
    prompt.chat.message 
    prompt.template

&#x200B;
```
---

     
 
all -  [ Question: Have any of you built anything related to social media ](https://www.reddit.com/r/LangChain/comments/1bgvk62/question_have_any_of_you_built_anything_related/) , 2024-03-19-0910
```
automation or gaining followers or crawling and finding followers etc. 
```
---

     
 
all -  [ Does Semantic Chunker works with HTML documents ](https://www.reddit.com/r/LangChain/comments/1bgv8g6/does_semantic_chunker_works_with_html_documents/) , 2024-03-19-0910
```
There's a famous Semantic Chunker (by Greg) which splits the document and group together sentences which are semanticall
y similar. ([YouTube Video of Greg](https://www.youtube.com/watch?v=8OJC21T2SL4&t=1933s&ab_channel=GregKamradt%28DataInd
y%29))  


I am using it in langchain, to split my HTML page. But its not working, it supposed to have html table in the
 same chunk but it is not keeping it into same chunk.  


How to solve this? Anything?  


&#x200B;
```
---

     
 
all -  [ Testing concepts ](https://www.reddit.com/r/LLMDevs/comments/1bgur1z/testing_concepts/) , 2024-03-19-0910
```
So I am soliciting a technical cofounder who I know will be responsible for the brunt of the early mvp work on a concept
… rightfully I’ve been asked to do some testing on my concept (which is fine.. but need some help)…

I used mendable.ai 
and some simple uploads to simulate the RAG + custom prompt + actual question… I actually had some solid results w/no re
al effort in prompting, chaining of prompts, data input to RAG, organization of data, indexing, etc.

I need help unders
tanding how to set up a better low resource test framework to mix and match some combinatorials of the above + maybe oth
ers (LoRA, model tuning, diff models, model merges, diff workflow sequences, etc. etc.)…

I actually think a GUI based a
pplication to do this would be insanely valuable (maybe I’m just too stupid to use langchain ++ and its not that valuabl
e, or it’s insanely difficult?). Idk. But whatever the answer is I’d appreciate a modular way to plug and play different
 erent components and workflows to isolate bits for efficacy, efficiency, and veracity.

Lmk if ya’ll have any ideas? Th
x. 🙏 
```
---

     
 
all -  [ Understanding Message Types in Agent Initialization ](https://www.reddit.com/r/LangChain/comments/1bgui26/understanding_message_types_in_agent/) , 2024-03-19-0910
```
I recently delved into using agents and noticed there are different types of messages available: SystemMessages,Ai messa
ges, Human Messages, Prefix, and Suffix. I'm curious about their distinctions and how they aid in agent initialization.


Could someone provide a breakdown with examples? Let's say I have an assistant named Shibi who works with my data in Py
thon DataFrame/CSV format. How would each message type play out in the initialization process, especially when using an 
inbuilt agent(pandas,csv) vs a custom one?

Looking forward to your insights!
```
---

     
 
all -  [ How to start learning langchain? ](https://www.reddit.com/r/LangChain/comments/1bgsok2/how_to_start_learning_langchain/) , 2024-03-19-0910
```
Hi everyone, I am trying to start learning how to implement langchain. 

Could anyone give recommendations on books/onli
ne courses/youtube videos I can watch to get started? 

Also, are there any prerequisites I need to have practiced/learn
t before starting on learning langchain?
```
---

     
 
all -  [ Optimal way to chunk word document for RAG(semantic chunking giving bad results) ](https://www.reddit.com/r/LangChain/comments/1bgqc2o/optimal_way_to_chunk_word_document_for/) , 2024-03-19-0910
```
 I have a word document that is basically like a self guide manual, which has a heading, below procedure to perform the 
operation.

Now the problem is ive tried lots of chunking methods, even semantic chunking, but the heading gets attached
 to a different chunk and retrieval system goes crazy, whats an optimal way to chunk so that the heading + context gets 
retained?
```
---

     
 
all -  [ I made code2prompt - A CLI tool to convert your codebase into a single LLM prompt with source tree,  ](https://www.reddit.com/r/rust/comments/1bghroh/i_made_code2prompt_a_cli_tool_to_convert_your/) , 2024-03-19-0910
```
**What is it?**  
You can run [code2prompt](https://github.com/mufeedvh/code2prompt) on your codebase directory and it w
ould generate a well-formatted Markdown prompt detailing the source tree structure, and all the code. You can then uploa
d this document to either GPT or Claude models with higher context windows and ask it to:  


* Rewrite the code to anot
her language.
* Find bugs/security vulnerabilities.
* Document the code.
* Implement new features.

You can customize th
e prompt template to achieve any of the desired use cases. It essentially traverses a codebase and creates a prompt with
 all source files combined. In short, it automates copy-pasting multiple source files into your prompt and formatting th
em along with letting you know how many tokens your code consumes.

I've also uploaded some templates for common use cas
es: See the [List of Templates](https://github.com/mufeedvh/code2prompt?tab=readme-ov-file#templates).  


[Screenshot o
f the code2prompt CLI tool](https://preview.redd.it/fbo8o2xxtroc1.png?width=1414&format=png&auto=webp&s=d7e2dcdc829f0a80
94c9bb1db1e1343df64a1c2a)

>I initially wrote this for personal use to utilize Claude 3.0's 200K context window and it h
as proven to be pretty useful so I decided to open-source it!

  
**GitHub:** [https://github.com/mufeedvh/code2prompt](
https://github.com/mufeedvh/code2prompt)
```
---

     
 
all -  [ I made code2prompt - A CLI tool to convert your codebase into a single LLM prompt with source tree,  ](https://www.reddit.com/r/ChatGPTCoding/comments/1bghp8p/i_made_code2prompt_a_cli_tool_to_convert_your/) , 2024-03-19-0910
```
**What is it?**  
You can run [code2prompt](https://github.com/mufeedvh/code2prompt) on your codebase directory and it w
ould generate a well-formatted Markdown prompt detailing the source tree structure, and all the code. You can then uploa
d this document to either GPT or Claude models with higher context windows and ask it to:  


* Rewrite the code to anot
her language.
* Find bugs/security vulnerabilities.
* Document the code.
* Implement new features.

You can customize th
e prompt template to achieve any of the desired use cases. It essentially traverses a codebase and creates a prompt with
 all source files combined. In short, it automates copy-pasting multiple source files into your prompt and formatting th
em along with letting you know how many tokens your code consumes.

I've also uploaded some templates for common use cas
es: See the [List of Templates](https://github.com/mufeedvh/code2prompt?tab=readme-ov-file#templates).  


[Screenshot o
f the code2prompt CLI tool](https://preview.redd.it/5y9qxur1sroc1.png?width=1414&format=png&auto=webp&s=bf4597b8a7925cb3
543f95967370ea9c5009e41d)

>I initially wrote this for personal use to utilize Claude 3.0's 200K context window and it h
as proven to be pretty useful so I decided to open-source it!

  
**GitHub:** [https://github.com/mufeedvh/code2prompt](
https://github.com/mufeedvh/code2prompt)
```
---

     
 
all -  [ Struggling with hallucinations in ConversationSummaryMemory ](https://www.reddit.com/r/LangChain/comments/1bgdh3n/struggling_with_hallucinations_in/) , 2024-03-19-0910
```
New to langchain, and trying to get used to the tooling. However, I am struggling with hallucinations in conversationsum
marymemory. I am using llama2 via Ollama. I am using the smaller 3.8GB (llama2:latest   78e26419b446) model. My leading 
hypothesis is that the model itself is not very good at summarizing, and is just corrupting the memory with its hallucin
ations.

 The post might be long, but I thought it is best to illustrate my problem using this small demo I have prepare
d.

&#x200B;

Here's how I instantiate,

    template = '''
    Act as an AI assistant and follow user instructions and 
answer questions in a precise manner.
    User conversation history for context whenever applicable.
    Current convers
ation: {history}
    Human: {input}
    '''
    llm = Ollama(model='llama2', temperature=0.9) 
    memory = Conversation
SummaryMemory(llm=Ollama(model='llama2', temperature=0.0)) 
    # set temperature=0. for memory for determinism. 
    co
nvo = ConversationChain(
                 llm = llm,
                 verbose = True,
                 memory=memory,
  
               prompt = PromptTemplate(input_variables=['history', 'input'], template=template)
                )
    co
nvo.predict(input='Introduce yourself.')

Output : so far reasonable.

    > Entering new ConversationChain chain...
   
 Prompt after formatting:
    
    Act as an AI assistant and follow user instructions and answer questions in a precise
 manner.
    User conversation history for context whenever applicable.
    Current conversation: 
    Human: Introduce 
yourself.
    
    
    > Finished chain.
    
    'Hello! I'm just an AI assistant, here to help you with any questions
 or tasks you may have. My name is Assistant, and I'm here to assist you in a precise and helpful manner. How can I assi
st you today?'

Then I provide some new inputs.

    convo.predict(input='Memorize the following words, bat, cat dog')
 
   convo.predict(input='Try to remember the following words: coffee and tea')

Now it has completely gone off the rails.
 Here's the outputs.

    > Entering new ConversationChain chain...
    Prompt after formatting:
    
    Act as an AI a
ssistant and follow user instructions and answer questions in a precise manner.
    User conversation history for contex
t whenever applicable.
    Current conversation: Current summary: The human asks what the AI thinks of artificial intell
igence. The AI thinks artificial intelligence is a force for good because it will help humans reach their full potential
.
    
    New lines of conversation: Human: What do you mean by 'reach their full potential'? AI: Well, with the help o
f artificial intelligence, humans can accomplish more than they ever thought possible. It can help them solve complex pr
oblems, make better decisions, and achieve their goals more efficiently.
    
    New summary: The human asks what the A
I thinks of artificial intelligence, and the AI replies that it believes artificial intelligence is a force for good bec
ause it will help humans reach their full potential by enabling them to accomplish more than they ever thought possible,
 solve complex problems, make better decisions, and achieve their goals more efficiently.
    Human: Memorize the follow
ing words, bat, cat dog
    
    
    > Finished chain.
    
    
    > Entering new ConversationChain chain...
    Prom
pt after formatting:
    
    Act as an AI assistant and follow user instructions and answer questions in a precise mann
er.
    User conversation history for context whenever applicable.
    Current conversation: Current summary: The human 
asks what the AI thinks of artificial intelligence. The AI thinks artificial intelligence is a force for good because it
 will help humans reach their full potential.
    
    New lines of conversation: Human: What do you mean by 'reach thei
r full potential'? AI: Well, with the help of artificial intelligence, humans can accomplish more than they ever thought
 possible. It can help them solve complex problems, make better decisions, and achieve their goals more efficiently.
   
 
    New summary: The human asks what the AI thinks of artificial intelligence, and the AI replies that it believes art
ificial intelligence is a force for good because it will help humans reach their full potential by enabling them to acco
mplish more than they ever thought possible, solve complex problems, make better decisions, and achieve their goals more
 efficiently.
    
    New lines of conversation: AI: I'm glad you asked! *smirks* In my opinion, the future of artifici
al intelligence is bright, and it will continue to revolutionize various industries. With the advancements in machine le
arning and natural language processing, AI will become even more integrated into our daily lives.
    
    New summary: 
The human asks what the AI thinks of artificial intelligence, and the AI replies that it believes artificial intelligenc
e is a force for good because it will help humans reach their full potential by enabling them to accomplish more than th
ey ever thought possible, solve complex problems, make better decisions, and achieve their goals more efficiently. The A
I then goes on to express its excitement about the future of artificial intelligence and how it will continue to revolut
ionize various industries with advancements in machine learning and natural language processing.
    Human: Try to remem
ber the following words: coffee and tea
    
    
    > Finished chain.
    
    'Of course, I'd be happy to help! *smir
ks* I have a great memory when it comes to storing information, so I will definitely keep those words in mind for future
 conversations. By the way, do you want to know a fun fact about artificial intelligence? Did you know that AI can now c
reate art that is almost indistinguishable from that created by humans? It's fascinating to see how far the technology h
as come!'

The new summary lines contain things that have not been brought up in conversation at all.

Testing again,

 
   convo.predict(input='Out of the 5 words I shared with you. Repeat the third and fourth words.')

Yields total nonsens
e.

    > Entering new ConversationChain chain...
    Prompt after formatting:
    
    Act as an AI assistant and follo
w user instructions and answer questions in a precise manner.
    User conversation history for context whenever applica
ble.
    Current conversation: Current summary: The human asks what the AI thinks of artificial intelligence. The AI thi
nks artificial intelligence is a force for good because it will help humans reach their full potential.
    
    New lin
es of conversation: Human: Why do you think artificial intelligence is a force for good? AI: Because artificial intellig
ence will help humans solve complex problems, make better decisions, and achieve their goals more efficiently. Human: Th
at's interesting. Can you give me an example? AI: Sure! For instance, AI can help doctors diagnose diseases more accurat
ely and quickly than ever before. It can also assist businesses in making better investment decisions and optimizing the
ir operations.
    
    New summary: The human asks what the AI thinks of artificial intelligence, and the AI replies th
at it believes artificial intelligence is a force for good because it will help humans solve complex problems, make bett
er decisions, and achieve their goals more efficiently. The AI then provides an example of how AI can help doctors diagn
ose diseases more accurately and quickly than ever before, as well as assist businesses in making better investment deci
sions and optimizing their operations.
    
    New lines of conversation: Human: That's impressive. Can AI also help wi
th creative tasks? AI: Absolutely! Artificial intelligence can assist with creative tasks such as writing, music composi
tion, and even art creation. In fact, there are already many AI-generated art pieces that are highly regarded and sold f
or thousands of dollars.
    
    New summary: The human asks what the AI thinks of artificial intelligence, and the AI 
replies that it believes artificial intelligence is a force for good because it will help humans solve complex problems,
 make better decisions, and achieve their goals more efficiently. The AI then provides an example of how AI can help doc
tors diagnose diseases more accurately and quickly than ever before, as well as assist businesses in making better inves
tment decisions and optimizing their operations. The AI also mentions that artificial intelligence can assist with creat
ive tasks such as writing, music composition, and even art creation, with many AI-generated art pieces already highly re
garded and sold for thousands of dollars.
    Human: Out of the 5 words I shared with you. Repeat the third and fourth w
ords.
    
    
    > Finished chain.
    
    'Of course! The third word is 'ai' and the fourth word is 'intelligence'.
'

&#x200B;
```
---

     
 
all -  [ Chainlit deployment for prod in Kubernetes cluster ](https://www.reddit.com/r/LangChain/comments/1bga3qk/chainlit_deployment_for_prod_in_kubernetes_cluster/) , 2024-03-19-0910
```
Hi all, 

&#x200B;

I am trying to deploy a chainlit app in our k8 cluster.   


When deployed my http:baseurl/app shows
 up as a blank white page.   


on the container logs it shows your app is available at localhost:8080 .   


I feel lik
e I will have to write my own framework instead of chainlit to deploy in prod. 

&#x200B;

Any advice is welcome. 

&#x2
00B;

Thanks 

&#x200B;

  


  

```
---

     
 
all -  [ A mystery gaming site where you help a helpless gpt solve cases. ](https://www.reddit.com/r/OpenAI/comments/1bg8dh9/a_mystery_gaming_site_where_you_help_a_helpless/) , 2024-03-19-0910
```
My friend and I made a mystery game with the openai api: [https://inkvestigations.com/](https://inkvestigations.com/)

I
t is open as in open source: [https://github.com/bromberry-games/Inkvestigations](https://github.com/bromberry-games/Ink
vestigations) 

You can try it out for free and even play it for free if you use your own openai key. You can check the 
code that we won't take your key. Also if you try it out and need more messages just let me know.  
We have some premade
 mysteries and also a mystery creator where you can make your own.

This was a fun project to do and we learned a lot ab
out working with gpt and building something in general. The biggest problem with gpt for us was getting it to follow the
 instructions correctly even after a ton of messages, which we kinda managed to solve with some chain of thought prompti
ng and few shot prompting. Also we are using the tipping prompting technique, which was a huge highlight when it worked 
for us. I guess gpt really likes money. 

However I have to say that the quality is not really there (yet). I think the 
responses often fall very flat and are kind of mediocore with occansional highlights in between. There is still a long w
ay to go from gpt to a competent game master. Don't let that deter you from trying it out tho, it's still fun for a coup
le of tries. We still have a couple of ideas left to make it better by using some more langchain features like the examp
le selector, but will then leave the project alone.

Did anyone here have success making gpt feel more 'alive'. You can 
prompt him to be a persona. For example we wanted it to play a dark and grim police officer, but always when we tried so
mething like it, it just overplayed it's role so much that it got annyoing after \~5 messages.
```
---

     
 
all -  [ New to LangChain, how to make my vector store query faster? ](https://www.reddit.com/r/LangChain/comments/1bg81iw/new_to_langchain_how_to_make_my_vector_store/) , 2024-03-19-0910
```
I'm an experienced software engineer who is new to AI-based development. I am working on a practice RAG project with Lan
gChain and Milvus. 

Right now I am just re-creating the example found here: [https://github.com/langchain4j/langchain4j
-examples/blob/main/milvus-example/src/main/java/MilvusEmbeddingStoreExample.java](https://github.com/langchain4j/langch
ain4j-examples/blob/main/milvus-example/src/main/java/MilvusEmbeddingStoreExample.java). No more, no less. I am doing th
is on my M1 Pro MacBook.

When I try performing the query, it runs incredibly slow. I can't tell you exactly how long, b
ecause after waiting several minutes I always abort. There are no exceptions, it just sits there, trying to process.

I 
have allocated 8 CPU cores and 16GB of RAM to the docker engine on my laptop. Based on the stats I am seeing, milvus its
elf is heavily CPU bound. The tiny quantity of data in the vector store at the time means the RAM requirements are minim
al. Yet at the end of the day, it is still incredibly slow.

There are a few possibilities I am considering at this poin
t. The first is that Milvus benefits from GPU optimization. That's my least-preferred scenario, as my MacBook and my hom
e server are lacking in GPU hardware.

The second scenario is indexing. This is an area that I know from working with tr
aditional databases, but with vector databases it's all new to me. Specifically, I'm using the default FLAT index which 
I know doesn't perform well. I'm beginning to read about alternative indexes to see what options I have there.

Anyway, 
I'm hoping that folks here can offer advice on my existing ideas and any other general improvements I can make. Thanks i
n advance.
```
---

     
 
all -  [ LangChain for... pretty obscure task, I suppose. ](https://www.reddit.com/r/LangChain/comments/1bg7ojh/langchain_for_pretty_obscure_task_i_suppose/) , 2024-03-19-0910
```
Hello everyone,

I am new to this subreddit and to reddit more in general. I am using LangChain and LLaMa2 a lot for my 
research lately, and I have some general questions about usage. 

1) To begin with, is there any way to verify that I am
 working with the right model? I am loading a quantized version of LLaMa2 though HF pipelines, and when I inspect the mo
del it calls it GPT2. Not sure if I should be worried. 

2) Regarding memory: how does the ConversationBufferMemory for 
LLM chains work? Is it loaded on GPU? Does it count as context, meaning that a memory with too many messages will cause 
the model to start spouting gibberish? How persistent is it (i.e.: after how many messages will the earliest message be 
forgotten/deleted)?

3) Regarding RAG using Chroma (which I have seen being used in the LangChain docs): is there a tuto
rial for how to conduct it? I am especially interested in verifying if one can iteratively add to the database the LLM i
s drawing from without having to 'retrain' the model. 

4) Related to questions 2 and 3. Suppose that I have an script r
unning that iteratively produces text in batches. I would then like to feed batches one after the other to an LLM in ord
er for the algorithm to evaluate the content of these batches. I have considered two options: the first is to feed each 
part of the batch directly into the LLM's memory, but I am not sure if this would overload its GPU or context window (mo
re worried about the latter, presently). The other option is, you guessed it, performing RAG on the batches. But I am no
t sure if RAG can help me with something beyond simple retrieval and more in depth. I don't want a summary of what is in
 a given batch of text, I want some manner of inference on the batch conditional on my request, for instance: if the bat
ch of text says that person X took a series of action that resulted in person Y dying, I want to ask the LLM if it can f
ind a causal link between X's actions and Y's death.

5) Finally, is there a way to use LLMs for flow control? Say that 
I have a very basic counting loop, something that simply enumerates all natural numbers until it is stopped. Is there a 
way, or maybe a tool, to tell an LLM to stop the loop when a number exceeds a certain threshold? I realize that this is 
killing a rat with a bazooka, but it's the smallest working example I could produce. A more fitting and complex example 
would be: let us return to the text in question 4. I want the LLM to stop the script that is producing text if it can id
entify a causal link between Y's death and X's action. Is there a way to do this? Simply asking LLaMa2-7b to type 'stop'
 if it thinks the loop should stop does not work, despite using very wordy prompts and CoT.

I am sorry for the very bas
ic questions, I do not really know where to turn for help. I likewise apologize for being vague but I cannot disclose to
o much about my research. Any link, resource or manner of assistance will be very much appreciated. 
```
---

     
 
all -  [ LLM workflows  ](https://www.reddit.com/r/LangChain/comments/1bg7kfm/llm_workflows/) , 2024-03-19-0910
```
My team got requirement from a client and client wants do this using any LLM. Its about a workflow based on serious ques
tions.
If user say yes to a particular question some, One set of questions will be triggered. If user say no the same qu
estion another set of questions should be followed.  

Is there any framework open/closed to achieve this. Its more of a
 decision trees kind of problem. So my client thinks if we use LLm then questions will more creative and conversational.
 
```
---

     
 
all -  [ [For Hire][Remote] Python Developer available for Application, Script, DevOps and Backend Developmen ](https://www.reddit.com/r/remotepython/comments/1bg3s9x/for_hireremote_python_developer_available_for/) , 2024-03-19-0910
```
I offer Software development, DevOps, SRE services. I use Python and all major frameworks such as Flask, Django and Fast
API.   


Here are the complete list of languages / Framework, I am familiar with:

**Backend Frameworks**

* FastAPI Fr
amework - Python
* Django Framework - Python
* Flask Framework - Python
* Laravel Framework - PHP
* Symfony Framework - 
PHP
* CodeIgnitor Framework - PHP
* Express Framework- NodeJS
* NextJS Framework - NodeJS
* Meteor Framework - NodeJS

*
*Frontend Frameworks**

* React
* Material UI
* Ember
* BackboneJS
* AngularJS
* Fluent UI
* Blade UI
* Element UI 

**W
eb 3.0 Technologies and Frameworks**

* Ethereum Virtual Machine (EVM)
* Truffle Framework
* Solana for NFT

Artificial 
Intelligence (AI)/ Machine Learning ML / LLMs

* LangChain Framework
* LiteLLM Framework
* Google Vertex AI
* ChatGPT
* 
Azure AI Studio  


Besides Software Development, I am a skill DevOps and Cloud Engineer:  


**Cloud Providers**

* Ama
zon Web Services
* Microsoft Azure
* Google Cloud
* DigitalOcean
* OVHCloud
* Alibaba Cloud
* Rackspace

&#x200B;

**Dom
ain / Hosting Providers**

* Go Daddy
* Heroku
* Linode
* Hostinger
* Interserver
* MyHost
* Bluehost

**CI/CD Tools**


* Jenkins
* Gitlab
* TeamCity
* CircleCI
* Github Actions
* BitBucket

**Other Tools**

* DataDog
* Splunk
* New Relic
*
 Puppet
* Kubernetes
* Prometeus
* Nagios
* Zabbix
* Cacti

Availability: 40 - 60 hours per week

Rate: Starting at $15 
per hour

Payment via: Payoneer, Bank Deposit, WISE

Please DM me for details about your project or job

&#x200B;
```
---

     
 
all -  [ Help me find the state of the art for my usecase ](https://www.reddit.com/r/LangChain/comments/1bg2qgo/help_me_find_the_state_of_the_art_for_my_usecase/) , 2024-03-19-0910
```
I am working on a project to convert non-fiction book PDFs (300 pages max) to a high quality crisp summary. 

Now, I've 
a standard structure for this summary:
1. It should be condensed to 10 'slides'
2. It should be high quality without omi
tting key aspects of the book.
3. I want each slide to have a title and a description below it. Title should be engaging
 for the reader and description should be 200 words Max.
4. should include a mindmap of all core ideas (optional)

My qu
estion to the experts on language model folks here is:
a. Is this a fair expectation? If not what is the closest I can g
et?
a. If yes. What is the best and cheapest (free) way to go about executing it as of today? fast, free, high quality o
ption.
b. How can I get started to achive the above task.

Thanks a lot.
```
---

     
 
all -  [ Flowise - Pupeteer version dependencies - Help needed ](https://www.reddit.com/r/LangChain/comments/1bfza1v/flowise_pupeteer_version_dependencies_help_needed/) , 2024-03-19-0910
```
 **Not sure what to do next. Help Appreciated**   
Tried to install flowise, getting these errors. 

The npm list -g pup
peteer  
 command output indicates that puppeteer  
 is being used by flowise  
 and its sub-dependencies at versions 19
.11.1  
 and 20.9.0  
, both of which are deprecated as they are below the supported version 21.5.0  
. Here's what you 
can consider doing next:

1. **Direct Dependency Update**: If a package directly depends on an outdated version, you cou
ld try updating that dependency. However, since puppeteer  
 is a nested dependency in your case (used by flowise-compon
ents  
 and langchain  
), direct intervention isn't straightforward.
2. **Contact the Maintainers**: Since the outdated
 puppeteer  
 versions are dependencies of flowise-components  
 and langchain  
, the ideal approach would be to contac
t the maintainers of these packages and request them to update their puppeteer  
 dependencies. This way, when you updat
e flowise  
, it would use the updated versions of these dependencies.
3. **Manual Override (Advanced)**: If you're comf
ortable with manual intervention and understand the potential risks, you could consider using npm's shrinkwrap  
 featur
e or resolutions  
 in package.json  
 (if using Yarn) to force the use of a newer puppeteer  
 version. This is more co
mplex and can lead to compatibility issues, so it's typically recommended only if you're experienced with Node.js and np
m's inner workings.
4. **Monitor and Update**: If the current functionality isn't affected and you're not using puppetee
r  
 in security-critical environments, you may choose to monitor the situation while waiting for the maintainers to upd
ate their packages. Ensure to regularly check for new versions of flowise  
 and its dependencies that might resolve thi
s issue.
5. **Assess Usage**: Consider how you're using flowise  
. If puppeteer  
's role is not critical for your use 
case, the deprecated warnings might be less concerning. However, if you're using puppeteer  
 features extensively, espe
cially in a production or security-sensitive environment, addressing this becomes more urgent.

In summary, the best cou
rse of action is typically to reach out to the package maintainers or monitor for updates that resolve the dependency co
ncerns. Direct intervention is possible but should be approached with caution.
```
---

     
 
all -  [ Build personalized agent with long term memory ](https://www.reddit.com/r/ClaudeAI/comments/1bfz79f/build_personalized_agent_with_long_term_memory/) , 2024-03-19-0910
```
I want to use Claude's API to build personalized agents for me with long term memory. 

So kind of creating separate age
nts which could act like companions - maybe like Marketing Expert, Co-Founder, Design Guy... essentially someone to brai
nstorm things & ideas with, which it can remember in the long run. 

Do I use Claude's API with Langchain or something l
ike that, with Pinecone etc. I'm new to this. 

Can anyone guide me on how to proceed on this path further? 

And some p
otential avenues to explore. 
```
---

     
 
MachineLearning -  [ [D] : Scale PDF Q&A App to 10K Users with GPUs – <$250/Mo ](https://www.reddit.com/r/MachineLearning/comments/1b6jv56/d_scale_pdf_qa_app_to_10k_users_with_gpus_250mo/) , 2024-03-19-0910
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

     
 
MachineLearning -  [ [D] What Is Your LLM Tech Stack in Production? ](https://www.reddit.com/r/MachineLearning/comments/1b4sdru/d_what_is_your_llm_tech_stack_in_production/) , 2024-03-19-0910
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

     
 
MachineLearning -  [ [D] Graphs + vectordbs? Need your input: Cognee.ai . AI Data Pipelines for Real-World Production (Pa ](https://www.reddit.com/r/MachineLearning/comments/1aweo71/d_graphs_vectordbs_need_your_input_cogneeai_ai/) , 2024-03-19-0910
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

     
 
MachineLearning -  [ [D] AI projects Suggestions ](https://www.reddit.com/r/MachineLearning/comments/1aunkmw/d_ai_projects_suggestions/) , 2024-03-19-0910
```
Hi Everyone, I need a suggestion to create AI courses for students ( Hands-on AI projects). I am thinking about the late
st AI trends such as Langchain, RAG, and vector databases. In each project, there can be multiple tasks, and the main th
ing is each task should have an automated system in which we can verify whether students have done it correctly or not.


For example: Project with visualization cannot be automatically tested. 

For example: A project with visualization can
not be automatically tested. . em can verify if the length of the text is smaller we can verify that it is correct.
```
---

     
