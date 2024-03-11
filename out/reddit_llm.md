 
all -  [ LangChain vs LlamaIndex ](https://www.reddit.com/r/LangChain/comments/1bbog83/langchain_vs_llamaindex/) , 2024-03-11-0910
```
Sorry for the oversimplified question but can someone explain the differences between the two?

Do they offer the same s
ort of capabilities but in a different way? It seems that LangChain is preferred when designing RAG applications, is tha
t true and why? What about ReAct?

Which one is more applicable for special purpose business use cases?

Also as an expe
rienced engineer but new to LLMs where should I start learning? Huggingface seems to have a lot of material, is that any
 good

Thanks

```
---

     
 
all -  [ use existing faiss index in LangChain ](https://www.reddit.com/r/LangChain/comments/1bbk7iu/use_existing_faiss_index_in_langchain/) , 2024-03-11-0910
```
Hi All, I wonder if it is possible to load existing indexes built by the faiss library into LangChain?  It seems that th
e format is different and I couldn't just load it like in the example shown in the LangChain documentation, e.g., FAISS.
load\_local('large.index', embeddings)

Thanks!
```
---

     
 
all -  [ Are all embeddings just bad for retrieval? ](https://www.reddit.com/r/LangChain/comments/1bbj5hu/are_all_embeddings_just_bad_for_retrieval/) , 2024-03-11-0910
```
[https://huggingface.co/spaces/mteb/leaderboard](https://huggingface.co/spaces/mteb/leaderboard)

I'm an experienced sof
tware engineer building a practice RAG stack application to learn more about integrating with LLMs. As is standard for t
his, I was going to take my data, convert it into embeddings, store it in a vector DB (Milvus), and then leverage it for
 the ultimate tasks I will be performing.

Looking at the above benchmarks, however, gives me pause. I've been trying to
 understand the scores, I THINK they are percentages. Classification accuracy seems quite high, which is good given that
's the primary task I ultimately want to perform. However, Retrieval seems much lower.

Basically, the highest Classific
ation score in those benchmarks is 79.46, whereas the highest Retrieval score is 59. Those are not in the same model, bt
w. I'm ignoring price, performance, and other factors right now to focus on this single issue.

My core point is that a 
\~60% accuracy at Retrieval seems like it's very bad for Classification, or literally any other task. In RAG, the goal i
s to pull out relevant pieces of data and use it as part of the query to the LLM. If the records can't be found accurate
ly to begin with, this whole approach would seem to be quite weak.

Am i just misunderstanding the benchmarks? Or am I m
isunderstanding how to utilize these models in RAG? Or is this a genuine problem?

Thanks in advance.
```
---

     
 
all -  [ Multimodal ](https://www.reddit.com/r/LangChain/comments/1bbgdhd/multimodal/) , 2024-03-11-0910
```
 Hello guys,

As we venture closer to the zenith of General Artificial Intelligence (GAI), a noteworthy trend has emerge
d within the AI research community, spearheaded by leading institutions such as OpenAI and Google. These organizations h
ave been pivotal in integrating multimodal capabilities into their Large Language Models (LLMs), marking a significant l
eap towards achieving AI systems with human-like cognitive abilities. This integration of multimodalism signifies an evo
lutionary step in artificial intelligence, enabling these models to not only excel in Natural Language Processing (NLP) 
but also to comprehend and generate auditory information via sophisticated Text-to-Speech (TTS) and Speech-to-Text (STT)
 technologies. Furthermore, the incorporation of computer vision allows these systems to analyze and interpret the natur
al world with remarkable precision, merely through the lens of a camera.

This fusion of modalities—linguistic, auditory
, and visual—equips LLMs with a more comprehensive understanding of the world, mirroring the multifaceted way humans per
ceive and interact with their environment. The ability to process and synthesize information across these dimensions ope
ns up unprecedented possibilities for AI applications, ranging from enhanced conversational interfaces to sophisticated 
autonomous systems capable of navigating complex real-world scenarios.

Amidst this technological renaissance, an intrig
uing question arises concerning Langchain's strategy in adopting multimodal frameworks. As developers and innovators eag
erly seek to harness the power of multimodal AI, the anticipation around Langchain's plans to facilitate the integration
 of multimodal capabilities into their framework is palpable. Such advancements would not only expand the toolkit availa
ble to developers but also pave the way for creating more intuitive and versatile AI systems, capable of operating acros
s a spectrum of human-like modalities.

As we stand on the brink of this transformative era in AI development, the integ
ration of multimodal functionalities within Langchain's offerings could significantly accelerate the adoption of sophist
icated AI solutions, fostering a new wave of innovation in the realm of artificial intelligence. The question remains: w
hen will Langchain unveil its approach to multimodal AI, and how will it empower developers to usher in the next generat
ion of AI applications?
```
---

     
 
all -  [ Seeking help on a LLM project  ](https://www.reddit.com/r/LangChain/comments/1bbf28l/seeking_help_on_a_llm_project/) , 2024-03-11-0910
```

Hello guys. 

I’m new to building llm apps.

I’m currently working on an independent project idea in the Educational se
ctor. I’m thinking of leveraging LLMs for automatic grading of some Python assignments. I’ve tried using gpt-4 for all t
he submissions to generate grade and feedback for each submission. For this approach, I passed the Python code, a rubric
 on how to deduct marks, total possible marks and assignment description. The results were good but I need to evaluate t
hem. Could you help me with suggestions on any techniques that I could use to improve upon this or maybe do some other a
pproaches with Rag or prompting techniques like COT? What should I use as my knowledge base? 

And how would I evaluate 
the responses?

Any suggestions would be absolutely invaluable.

Thanks for reading this!
```
---

     
 
all -  [ Hitting local huggingface inference endpoint or a better way to run models locally in docker? ](https://www.reddit.com/r/LangChain/comments/1bbe8jz/hitting_local_huggingface_inference_endpoint_or_a/) , 2024-03-11-0910
```
I have a model running in a docker container with huggingface's text-generation-inference and am trying to get langchain
 to talk to it.

I figured out how to use the deprecated HuggingFaceTextGenInference class, but it's deprecated. I tried
 using the HuggingFaceEndpoint class (which is suggested) but it wants to try and login to huggingface which doesn't mak
e any sense since the model is running locally.

Have you had any luck with this, or did I miss a setting somewhere in t
he HuggingFaceEndpoint class?

Is there a better way to run models locally in docker? 

:)
```
---

     
 
all -  [ Chunking Idea: Summarize Chunks for better retrieval ](https://www.reddit.com/r/LangChain/comments/1bbdgpj/chunking_idea_summarize_chunks_for_better/) , 2024-03-11-0910
```
Hi,

I want to discuss if this idea already exists or what you guys think of it. 

Does it make sense if you chunk your 
documents, summarize those chunks and use these summaries for retrieval? This is similar to ParentDocumentRetriever, wit
h the difference that the child chunk is the summary and the parent chunk the text itself. 

I think this could improve 
the accuracy as the summary of the chunk could be more related (higher cosine similarity) to the user query/question whi
ch is most of the time much shorter than the chunk. 

&#x200B;

What do you think about this?
```
---

     
 
all -  [ Using LangChain to teach an LLM to write like you ](https://arslanshahid-1997.medium.com/using-langchain-to-teach-an-llm-to-write-like-you-aab394d54792?sk=5136d482d220139c11fa4536681f4648) , 2024-03-11-0910
```

```
---

     
 
all -  [ How to create a chatbot using RAG using llama index? ](https://www.reddit.com/r/LangChain/comments/1bb9f03/how_to_create_a_chatbot_using_rag_using_llama/) , 2024-03-11-0910
```
The problem I am currently experiencing is as follows.  I implemented an ensemble retriever by looking at the ensemble r
etriever document. This is a method of entering a query based on a document and then reranking the results to receive a 
final answer.  That's why 'Hello?' has nothing to do with the document. If you enter llm, “Hello?” is displayed in the d
ocument. They won't reply to me because they can't find it.  How to implement rag and chatbot This is the Ensemble Retri
ever document I referenced. [https://docs.llamaindex.ai/en/stable/examples/retrievers/ensemble\_retrieval.html](https://
docs.llamaindex.ai/en/stable/examples/retrievers/ensemble_retrieval.html)

And below is my code.   


    loader = PyMuP
DFReader()
    docs0 = loader.load(file_path=Path('./data/company_rule.pdf'))
    doc_text = '\n\n'.join([d.get_content(
) for d in docs0])
    docs = [Document(text=doc_text)]
    
    llm = OpenAI(model='gpt-4-0125-preview')
    chunk_size
s = [128, 256, 512, 1024]
    nodes_list = []
    vector_indices = []
    for chunk_size in chunk_sizes:
    print(f'Chu
nk Size: {chunk_size}')
    splitter = SentenceSplitter(chunk_size=chunk_size, chunk_overlap=chunk_size // 2)
    nodes 
= splitter.get_nodes_from_documents(docs)
    for node in nodes:
    node.metadata['chunk_size'] = chunk_size
    node.e
xcluded_embed_metadata_keys = ['chunk_size']
    node.excluded_llm_metadata_keys = ['chunk_size']
    nodes_list.append(
nodes)
    vector_index = VectorStoreIndex(nodes)
    vector_indices.append(vector_index)
    
    retriever_dict = {}
 
   retriever_nodes = []
    for chunk_size, vector_index in zip(chunk_sizes, vector_indices):
    node_id = f'chunk_{chu
nk_size}'
    node = IndexNode(
    text=(
    'rule context retrieves (chunk size')
    f'{chunk_size})'
    ),
    ind
ex_id=node_id,
    )
    retriever_nodes.append(node)
    retriever_dict[node_id] = vector_index.as_retriever()
    
   
 summary_index = SummaryIndex(retriever_nodes)
    
    retriever = RecursiveRetriever(
    root_id='root',
    retrieve
r_dict={'root': summary_index.as_retriever(), **retriever_dict},
    )
    
    nodes = await retriever.aretrieve(
    '
About working hours'
    )
    
    print(f'Number of nodes: {len(nodes)}')
    for node in nodes:
    print(node.node.m
etadata['chunk_size'])
    print(node.node.get_text())
    
    reranker = LLMRerank()
    print(reranker)
    
    quer
y_engine = RetrieverQueryEngine(retriever, node_postprocessors=[reranker])
    
    response = query_engine.query(
    '
About working hours'
    )
    
    display_response(
    response, show_source=True, source_length=500, show_source_met
adata=True
    )
    
    #finalanswer

&#x200B;
```
---

     
 
all -  [ Langsmith for Autogen? ](https://www.reddit.com/r/LangChain/comments/1bb4ww1/langsmith_for_autogen/) , 2024-03-11-0910
```
I want to track my openai api usage using langsmith. 
the app using autogen as its orchestration framework. 

can anyone
 guide me on how to implement this for my agents in autogen?

all kinds of ideas are appreciated!!


```
---

     
 
all -  [ [#langchain 밋업 발표] R.A.G. 우리가 절대 쉽게결과물을 얻을 수 없는 이유 http://aitutor21.com/bbs/board.php?bo_table=aistu ](https://www.reddit.com/r/chatgpt_newtech/comments/1bb2cwo/langchain_밋업_발표_rag_우리가_절대_쉽게결과물을_얻을_수_없는_이유/) , 2024-03-11-0910
```
\[#langchain 밋업 발표\] R.A.G. 우리가 절대 쉽게결과물을 얻을 수 없는 이유  [http://aitutor21.com/bbs/board.php?bo\_table=aistudy&wr\_id=450](
http://aitutor21.com/bbs/board.php?bo_table=aistudy&wr_id=450)
```
---

     
 
all -  [ Multiple Document loader ](https://www.reddit.com/r/LangChain/comments/1bb0yzw/multiple_document_loader/) , 2024-03-11-0910
```
Hey I am looking to use some sort of a loader which can help me load multiple variety of documents AKA a some sort of cu
stom loader, any help you guys can provide?
```
---

     
 
all -  [ Cost effective Frameworks for llm applications in real world scenarios. ](https://www.reddit.com/r/LLMDevs/comments/1baohzc/cost_effective_frameworks_for_llm_applications_in/) , 2024-03-11-0910
```
Langchain 
Autogen 

these are the ones that i have use to develop applications using gpt-4.
but langchain gets too comp
lex for multi agent tasks.
and autogen throws random errors and can get stuck in a loop racking up my credits.
Not to me
ntion using autogen has really been heavy on my pocket…

what are the best options out there which are cost effective as
 well as have simple workflows to implement?? 

I know Langraph, crewai… but it would be great  if someone has experimen
ted with to comment on it… 

lastly gpt-4 seems too costly 
what other models would you recommend instead not compromisi
ng much on performance….?
```
---

     
 
all -  [ Recommendations for RAG Evaluation Framework Resources ](https://www.reddit.com/r/LangChain/comments/1baltvi/recommendations_for_rag_evaluation_framework/) , 2024-03-11-0910
```
Hello everyone!

I'm currently on the lookout for some solid resources to help me delve into RAG evaluation frameworks. 
Whether it's articles, guides, or even personal recommendations, I'm eager to expand my knowledge in this area. If you'v
e come across any valuable resources or have expertise in RAG evaluation, I'd greatly appreciate your insights and sugge
stions. Thanks in advance!

 
```
---

     
 
all -  [ Need help reducing execution time while using langchain llama2 7b quantised version in CPU ](https://www.reddit.com/r/LangChain/comments/1balq8c/need_help_reducing_execution_time_while_using/) , 2024-03-11-0910
```
Hi, I am new to generative AI and building a document based question answering module using langchain and Llama2 as the 
LLM. I am using sentence-transformers/all-MiniLM-L6-v2 for the embeddings. But I think the actual time is being taken in
 the Retrieval Chain. Per response takes around 1 min, and I have limited logical cores to use (max: 10) and when using 
multiprocessing each response takes even longer. Any ideas on how I can reduce the execution time? Without usage of GPU?

```
---

     
 
all -  [ LangChain + python+ oobabooga API = Chat with a PDF? ](https://www.reddit.com/r/LocalLLaMA/comments/1balmqo/langchain_python_oobabooga_api_chat_with_a_pdf/) , 2024-03-11-0910
```
I have oobabooga running on my server with the API exposed.

Text-generation-webui works great for text, but not at all 
intuitive if I want to upload a file (e.g. PDF) and then ask whatever model is loaded questions about it.

I can write p
ython code (and also some other languages for a web interface), I have read that using LangChain combined with the API t
hat is exposed by oobabooga make it possible to build something that can load a PDF, tokenize it and then send it to oob
abooga and make it possible for a loaded model to use the data (and eventually answer questions about it).

Now, how / w
here do I start?

I rather utilize the API that I already have working (from ooba) and just write the part for making th
e tokenized PFF available to it, also maybe eventually create a simple web UI for it etc.

I could not find any concrete
 example, as it seem to look like the most recent trend is just find some tool, install snd use it (but then those tools
 have their own way and dont serve my intended purpose)

Could anyone send me in the right direction other then document
ation which I already am aware of (and other than general syntax don’t share code examples)

Thanks in advanced 
```
---

     
 
all -  [ Rag over updating data ](https://www.reddit.com/r/LangChain/comments/1baky7p/rag_over_updating_data/) , 2024-03-11-0910
```
Have you ever had to ingest documents about a specific topic that is changing over time? 
i.e. : news about a specific f
act may be accurate today (we only know so much) but inaccurate tomorrow (we discover some new things).
How would you re
turn only the most recent facts?
```
---

     
 
all -  [ Rag application for text and images ](https://www.reddit.com/r/LangChain/comments/1bajono/rag_application_for_text_and_images/) , 2024-03-11-0910
```
I have a use case where i got 100's of documents. I have implemented a rag for answering question related to text but th
e problem is my requirement extends to images also. The documents contains steps for some process. These steps have some
 text and followed by some image. The application i am trying to implement should behave in a way that, if asked any que
stion about the process it should not only give me the steps but also the images corresponding to it. (have to maintain 
the order of the images)  


For ex:   


Step 1: \_\_\_ some text \_\_\_  
respective image for step 1  


Step 2: \_\_
\_ some text \_\_\_  
respective image for step 2  


and so on.   


How do you even do this, is it possible?  

```
---

     
 
all -  [ Chat with rag - further questions ](https://www.reddit.com/r/LangChain/comments/1bajhg8/chat_with_rag_further_questions/) , 2024-03-11-0910
```
I already have embedding db to perform rag.
I’m just struggling with follow up questions.

- so user asks a question
- r
ag search to get content, send to loom, return response
- user asks a follow up like: “what about option 2”
- but how th
e backend know what to do next?

- should I do another rag for this specific query “what about option 2”, that is basica
lly useless.
- or send the full conversation with the prior rag, and this additional message
```
---

     
 
all -  [ Langchain recursive summary VS agentic summary VS Opus/Yi 200k context ](https://www.reddit.com/r/LocalLLaMA/comments/1baezc4/langchain_recursive_summary_vs_agentic_summary_vs/) , 2024-03-11-0910
```
What’s the best way to summarise text these days?


Was thinking of recursive summary using Langchain, or something with
 agents, or just putting it all in the Claude Opus or Yi 200k context


As an additional side note has anyone tried Cohe
re’s summary API product? Seems slightly different to other methods 
```
---

     
 
all -  [ How to connect to web-based chatpgt, gemini or claude? ](https://www.reddit.com/r/LangChain/comments/1badxki/how_to_connect_to_webbased_chatpgt_gemini_or/) , 2024-03-11-0910
```
Hi all! I am pretty new to this langchain world. But it seems langchain requires you to have api key for all llm service
s. Right now I have chatgpt 4 subscription, is it possible to connect langchain to the web-based chatgpt without using a
pi key which will cause extra money? Thanks!
```
---

     
 
all -  [ How do you decide which RAG strategy is best? ](https://www.reddit.com/r/LangChain/comments/1baba9c/how_do_you_decide_which_rag_strategy_is_best/) , 2024-03-11-0910
```
I really liked this idea of evaluating different RAG strategies. This simple project is amazing and can be useful to the
 community here. You can have your custom data evaluate different RAG strategies and finally can see which one works bes
t. Try and let me know what you guys think: [https://www.ragarena.com/](https://www.ragarena.com/) 
```
---

     
 
all -  [ Need help ](https://www.reddit.com/r/LangChain/comments/1ba9kqk/need_help/) , 2024-03-11-0910
```
My company is asking me to build a chatbot for appointment scheduling for patient engagement using LLM. Does anyone have
 experience in it? 

Is it possible with RAG approach? As we don’t have data looking to synthesize it. Or do I need to f
ine tune it with synthesized data?

It would be really great if someone could help!

```
---

     
 
all -  [ Difference between as_retriever() and .similarity_search() ](https://www.reddit.com/r/LangChain/comments/1ba77pu/difference_between_as_retriever_and_similarity/) , 2024-03-11-0910
```
Hi all--

I'm using PGVector as my vector store, but this applies to any vector store class, I assume.

If I instantiate
d the vector store and passed it as a retriever vs using the vector store and calling similarity\_search() off the insta
ntiated store to get ***k*** documents, is there a big difference? 

I understand that I would have to include the retri
eved documents more manually when packaging the prompt if going with the similarity\_search() route, but let's set that 
aside. I am just curious about the accuracy and strength comparisons between the two methods, if there is any tangible d
ifference in terms of accuracy (of retrieved docs).
```
---

     
 
all -  [ How can I use python in Godot? ](https://www.reddit.com/r/godot/comments/1b9vc31/how_can_i_use_python_in_godot/) , 2024-03-11-0910
```
Hi, I'm learning LangChain, and I want to use it in Godot. But LangChain works in Python so I'd need a way to have Godot
 communicate with Python.

How do I do that?
```
---

     
 
all -  [ New and need a little guidance from the pros ](https://www.reddit.com/r/LangChain/comments/1b9tu75/new_and_need_a_little_guidance_from_the_pros/) , 2024-03-11-0910
```
I am new and want to tackle a project and get some experience. My goal is to use langchain and or langgraph to have agen
ts fill in a standardized template with information it knows or references online. Review it for accuracy and ensure the
 template was adhered to then save it. Any advice would be most helpful, thanks. 
```
---

     
 
all -  [ Langserve for complex cases ](https://www.reddit.com/r/LangChain/comments/1b9k8wf/langserve_for_complex_cases/) , 2024-03-11-0910
```
Hello everyone. Langserve is a great tool but it works just for single chains. I have a more complicated code structure 
where I first extract the docs from the vector store with one function, then for each document I make an llm call. How c
ould I implement this in langserve??

Thanks

&#x200B;

https://preview.redd.it/13j7n760x2nc1.png?width=796&format=png&a
uto=webp&s=4c677dd13ac857c3abed8f89baa8d2c5bd55819d

https://preview.redd.it/c366b21hw2nc1.png?width=775&format=png&auto
=webp&s=8039203c10a69c1b0d6e8b84906ea39c6b6690c4

https://preview.redd.it/eu8v689lw2nc1.png?width=802&format=png&auto=we
bp&s=0838356f0f358265831198d3286b22019606142e

https://preview.redd.it/xh9ihb6nw2nc1.png?width=643&format=png&auto=webp&
s=624c30471ade2421f6b9cb6ff61ebfaaa8544502
```
---

     
 
all -  [ Multimodel with RAG (vectordb) ](https://www.reddit.com/r/LangChain/comments/1b9jhm0/multimodel_with_rag_vectordb/) , 2024-03-11-0910
```
I have created a platform with document upload and search using vector db, embedding models and llm (simple RAG pattern)
.
Now. I want to use gpt-4 multimodel concept in this. For example, user uploads their documents through RAG but at the 
same time, while asking question, they can upload one more document in model context, or may be an image, and ask questi
on. System should get answers from document uploded in model context as well as vector db.
How can i achieve that? Is it
 a even a real usecase?
```
---

     
 
all -  [ ReadableStream ](https://www.reddit.com/r/reactnative/comments/1b9jei4/readablestream/) , 2024-03-11-0910
```
I keep getting this error after implementing Langchain in my app, expo can no longer compile it:  
I would really apprec
iate if someone could give any insights or possible fixes.

 ERROR  ReferenceError: Property 'ReadableStream' doesn't ex
ist, js engine: hermes

 ERROR  Invariant Violation: 'main' has not been registered. This can happen if:

\* Metro (the 
local dev server) is run from the wrong folder. Check if Metro is running, stop it and restart it in the current project
.

\* A module failed to load due to an error and \`AppRegistry.registerComponent\` wasn't called., js engine: hermes
```
---

     
 
all -  [ PyPDFLoader ](https://www.reddit.com/r/LangChain/comments/1b9iphd/pypdfloader/) , 2024-03-11-0910
```
Some of my pdfs will be loaded with the page_content ='', why is that so?
```
---

     
 
all -  [ How do create a chatbot that uses RAG in the llama index? ](https://www.reddit.com/r/LangChain/comments/1b9ihfy/how_do_create_a_chatbot_that_uses_rag_in_the/) , 2024-03-11-0910
```
If ask a question other than what is in the document, will not receive an answer.

I want to create a chatbot with rag f
unction using llama index.

How can I implement it?
```
---

     
 
all -  [ Do LLama-based APIs collect or store my data? ](https://www.reddit.com/r/LLMDevs/comments/1b9bty1/do_llamabased_apis_collect_or_store_my_data/) , 2024-03-11-0910
```
I've seen a few posts basically saying no but I'm not sure if that's actually a fact. Do APIs or libraries like Langchai
n, transformers or others you can find on huggingface that use LLama collect or store my data as in my prompts, any file
s or documents etc.? There are hundreds of projects out there and I personally find it difficult to understand which one
s really send data to some external server and which don't. I'm trying to narrow down the options to a few widely-accept
ed and local models that for sure don't send any of my data to any external servers. 

Thanks
```
---

     
 
all -  [ How I Reduced Our Startup's LLM Costs by Almost 90% ](https://www.reddit.com/r/SaaS/comments/1b92w5o/how_i_reduced_our_startups_llm_costs_by_almost_90/) , 2024-03-11-0910
```
With AI apps popping up everywhere, it’s fair to think building one is both easy and cheap.

Unfortunately, you’d be *(m
ostly)* wrong. I know because I learned the hard way.

I’m not saying it’s hard per se, but as of this writing, gpt-4-tu
rbo costs $0.01/$0.03 per 1000 input/output tokens. This can quickly add up if you’re building a complex AI workflow.

Y
es, you could use less expensive, worse performing models, like GPT 3.5 or an open-source one like Llama, stuff everythi
ng into one API call with excellent prompt engineering, and hope for the best. But this probably won’t turn out that gre
at. This type of approach doesn’t really work in production—at least not yet with the current state of AI.

**It could g
ive you the right answer 90% or even 99% of the time.** But that one time it decides to go off the rails, it’s really fr
ustrating. As a developer and/or business, you know you must never break a user’s experience. It might be okay for a toy
 app or prototype but not for a production-grade application you charge for.

Imagine if Salesforce or any other establi
shed software company said its reliability was only one or two nines. That would be insane. No one would use it.

**But 
this is the state of most AI applications today. They’re unreliable.**

# AI isn’t a Universal Function

The non-determi
nistic nature of LLMs forces us to be more thoughtful about how we write our code. We should not just “hope” that an LLM
 will always correctly respond. We need to build redundancy and proper error handling. For some reason, many builders fo
rget everything they learned about software engineering and treat AI like some magical universal function that doesn’t f
ail.

**It’s not there yet.**

To fix this limitation, we must write code that only interacts with AI when absolutely ne
cessary—that is, when a system needs some sort of “human-level” analysis of unstructured data. Subsequently, whenever po
ssible, we must force the LLM to return references to information (i.e., a pointer) instead of the data itself.

**When 
I recognized these two things, I had to redesign the backend architecture of my personal software business completely.**


# Rearchitecting Jellypod

For context, I started an app called Jellypod. It enables users to subscribe to email newsl
etters and get a daily summary of the most important topics from all of them as a single podcast.

This seems pretty sim
ple on the outside—and the MVP honestly was. The app would just process each email individually, summarize it, convert i
t to speech, and stitch all the audio together, side-by-side, into a daily podcast.

The output was fine, but it needed 
to be better.

If two different newsletters discussed the same topic, the “podcast” would talk about it twice, not reali
zing we had already mentioned it. You could say, “Well, why don’t you just stuff all the newsletter content into one big
 LLM call to summarize everything?”

Well, that’s what I tried at first.

And it failed. **Miserably.**

Even with an ex
tremely detailed prompt using all the best practices, I couldn’t guarantee that the LLM would always detect the most imp
ortant topics, summarize everything, and consistently create an in-depth output. Also, the podcast always needed to be \
~10 minutes long.

So I went back to the drawing board. How can I make this system better? And yes, we’re getting to the
 cost reduction part - don’t worry!

# Defining the Requirements

Jellypod must be able to process any number of input d
ocuments (newsletters) and create an output that always includes the top ten most important topics across all those inpu
ts. If two subparts of any input are about the same topic, we should recognize that and merge the sections into one topi
c.

For example, if the Morning Brew has a section about US Elections and the Daily Brief also has a section on the curr
ent state of US Politics, they should be merged. I’ll skip over how I determined a similarity threshold (i.e., should tw
o topics be merged or remain separate).

# Exploding Costs

I built on top of a few different approaches outlined in pap
ers written by the LangChain community to semantic chunk and organize everything in a almost deterministic way.

**But t
his was INSANELY expensive.** The number of API calls grew at a rate of O(n log n), with n being the number of input chu
nks from all newsletters.

So, I had a dilemma. Do I keep this improved and more expensive architecture or throw it down
 the drain?

I decided to keep it and figure out how to reduce costs.

# Reducing Costs

That’s when I discovered a tool
 called OpenPipe that allows you to fine-tune open-source models almost too easily. It looked legit and was backed by YC
ombinator, so I gave it a try.

I swapped out the OpenAI SDK with their SDK (a drop-in replacement), which passed all my
 LLM API calls to OpenAI but recorded all inputs and outputs. This created unique datasets for each of my prompts, which
 I could use to fine-tune a cheaper open-source model.

After about a week of recording Jellypod’s LLM calls, I had abou
t 50,000 rows of data. And with a few clicks, I fine-tuned a Mistral 7B model for each LLM call.

I replaced GPT-4 with 
the new fine-tuned model.

**And it reduced the costs by 88%.**

The cost of inference dropped from $10 per 1M input tok
ens to $1.20. And cost per output token dropped from $30 to $1.60.

I was blown away. I could now run Jellypod’s new arc
hitecture for approximately the same cost as the MVP’s trivial approach. I even confirmed that the fine-tuned Mistral ou
tput quality was just as high as GPT-4 by a series of evals and in-app customer feedback.

By redesigning the system to 
only use AI for the smallest unit of work it’s actually needed for, I could confidently deploy a fine-tuned model as a d
rop-in replacement for GPT 4. And by prompting to return pointers to data instead of the data itself, I could ensure dat
a integrity while reducing the number of output tokens consumed.

# In Conclusion

If you’re considering building an AI 
application, I would encourage you to take a step back and think about your architecture’s output reliability and costs.
 What happens if the LLM doesn’t answer your prompt in the right way? Can you prompt the model to return data identifier
s instead of raw data? And, is it possible to swap GPT-4 with a cheaper, fine-tuned model?

I wish I had these insights 
when I started, but hey, you live and learn.

I hope you found at least some parts of this interesting! I thought there 
were enough learnings to share. Feel free to reach out if you’re curious about the details.
```
---

     
 
all -  [ How I Reduced Our LLM Costs by Over 85% ](https://www.reddit.com/r/Entrepreneur/comments/1b92suo/how_i_reduced_our_llm_costs_by_over_85/) , 2024-03-11-0910
```
With AI apps popping up everywhere, it’s fair to think building one is both easy and cheap.

Unfortunately, you’d be *(m
ostly)* wrong. I know because I'm building one. 

I’m not saying it’s hard per se, but as of this writing, gpt-4-turbo c
osts $0.01/$0.03 per 1000 input/output tokens. This can quickly add up if you’re building a complex AI workflow.

Yes, y
ou could use less expensive, worse performing models, like GPT 3.5 or an open-source one like Llama, stuff everything in
to one API call with excellent prompt engineering, and hope for the best. But this probably won’t turn out that great. T
his type of approach doesn’t really work in production—at least not yet with the current state of AI.

**It could give y
ou the right answer 90% or even 99% of the time.** But that one time it decides to go off the rails, it’s really frustra
ting. As a developer and/or business, you know you must never break a user’s experience. It might be okay for a toy app 
or prototype but not for a production-grade application you charge for.

Imagine if Salesforce or any other established 
software company said its reliability was only one or two nines. That would be insane. No one would use it.

**But this 
is the state of most AI applications today. They’re unreliable.**

# AI isn’t a Universal Function

The non-deterministi
c nature of LLMs forces us to be more thoughtful about how we write our code. We should not just “hope” that an LLM will
 always correctly respond. We need to build redundancy and proper error handling. For some reason, many builders forget 
everything they learned about software engineering and treat AI like some magical universal function that doesn’t fail.


**It’s not there yet.**

To fix this limitation, we must write code that only interacts with AI when absolutely necessa
ry—that is, when a system needs some sort of “human-level” analysis of unstructured data. Subsequently, whenever possibl
e, we must force the LLM to return references to information (i.e., a pointer) instead of the data itself.

**When I rec
ognized these two things, I had to redesign the backend architecture of my personal software business completely.**

# R
earchitecting Jellypod

For context, I started an app called Jellypod. It enables users to subscribe to email newsletter
s and get a daily summary of the most important topics from all of them as a single podcast.

This seems pretty simple o
n the outside—and the MVP honestly was. The app would just process each email individually, summarize it, convert it to 
speech, and stitch all the audio together, side-by-side, into a daily podcast.

The output was fine, but it needed to be
 better.

If two different newsletters discussed the same topic, the “podcast” would talk about it twice, not realizing 
we had already mentioned it. You could say, “Well, why don’t you just stuff all the newsletter content into one big LLM 
call to summarize everything?”

Well, that’s what I tried at first.

And it failed. **Miserably.**

Even with an extreme
ly detailed prompt using all the best practices, I couldn’t guarantee that the LLM would always detect the most importan
t topics, summarize everything, and consistently create an in-depth output. Also, the podcast always needed to be ~10 mi
nutes long.

So I went back to the drawing board. How can I make this system better? And yes, we’re getting to the cost 
reduction part - don’t worry!

# Defining the Requirements

Jellypod must be able to process any number of input documen
ts (newsletters) and create an output that always includes the top ten most important topics across all those inputs. If
 two subparts of any input are about the same topic, we should recognize that and merge the sections into one topic.

Fo
r example, if the Morning Brew has a section about US Elections and the Daily Brief also has a section on the current st
ate of US Politics, they should be merged. I’ll skip over how I determined a similarity threshold (i.e., should two topi
cs be merged or remain separate).

# Exploding Costs

I built on top of a few different approaches outlined in papers wr
itten by the LangChain community to semantic chunk and organize everything in a almost deterministic way.

**But this wa
s INSANELY expensive.** The number of API calls grew at a rate of O(n log n), with n being the number of input chunks fr
om all newsletters.

So, I had a dilemma. Do I keep this improved and more expensive architecture or throw it down the d
rain?

I decided to keep it and figure out how to reduce costs.

# Reducing Costs

That’s when I discovered a tool calle
d OpenPipe that allows you to fine-tune open-source models almost too easily. It looked legit and was backed by YCombina
tor, so I gave it a try.

I swapped out the OpenAI SDK with their SDK (a drop-in replacement), which passed all my LLM A
PI calls to OpenAI but recorded all inputs and outputs. This created unique datasets for each of my prompts, which I cou
ld use to fine-tune a cheaper open-source model.

After about a week of recording Jellypod’s LLM calls, I had about 50,0
00 rows of data. And with a few clicks, I fine-tuned a Mistral 7B model for each LLM call.

I replaced GPT-4 with the ne
w fine-tuned model.

**And it reduced the costs by 88%.**

The cost of inference dropped from $10 per 1M input tokens to
 $1.20. And cost per output token dropped from $30 to $1.60.

I was blown away. I could now run Jellypod’s new architect
ure for approximately the same cost as the MVP’s trivial approach. I even confirmed that the fine-tuned Mistral output q
uality was just as high as GPT-4 by a series of evals and in-app customer feedback.

By redesigning the system to only u
se AI for the smallest unit of work it’s actually needed for, I could confidently deploy a fine-tuned model as a drop-in
 replacement for GPT 4. And by prompting to return pointers to data instead of the data itself, I could ensure data inte
grity while reducing the number of output tokens consumed.

# In Conclusion

If you’re considering building an AI applic
ation, I would encourage you to take a step back and think about your architecture’s output reliability and costs. What 
happens if the LLM doesn’t answer your prompt in the right way? Can you prompt the model to return data identifiers inst
ead of raw data? And, is it possible to swap GPT-4 with a cheaper, fine-tuned model?

I wish I had these insights when I
 started, but hey, you live and learn.

I hope you found at least some parts of this interesting! I thought there were e
nough learnings to share. Feel free to reach out if you’re curious about the details.
```
---

     
 
all -  [ How I Reduced Our LLM Costs by Over 85% ](https://www.reddit.com/r/ArtificialInteligence/comments/1b92hlk/how_i_reduced_our_llm_costs_by_over_85/) , 2024-03-11-0910
```
With AI apps popping up everywhere, it’s fair to think building one is both easy and cheap.

Unfortunately, you’d be *(m
ostly)* wrong.

I’m not saying it’s hard per se, but as of this writing, gpt-4-turbo costs $0.01/$0.03 per 1000 input/ou
tput tokens. This can quickly add up if you’re building a complex AI workflow.

Yes, you could use less expensive, worse
 performing models, like GPT 3.5 or an open-source one like Llama, stuff everything into one API call with excellent pro
mpt engineering, and hope for the best. But this probably won’t turn out that great. This type of approach doesn’t reall
y work in production—at least not yet with the current state of AI.

**It could give you the right answer 90% or even 99
% of the time.** But that one time it decides to go off the rails, it’s really frustrating. As a developer and/or busine
ss, you know you must never break a user’s experience. It might be okay for a toy app or prototype but not for a product
ion-grade application you charge for.

Imagine if Salesforce or any other established software company said its reliabil
ity was only one or two nines. That would be insane. No one would use it.

**But this is the state of most AI applicatio
ns today. They’re unreliable.**

# AI isn’t a Universal Function

The non-deterministic nature of LLMs forces us to be m
ore thoughtful about how we write our code. We should not just “hope” that an LLM will always correctly respond. We need
 to build redundancy and proper error handling. For some reason, many builders forget everything they learned about soft
ware engineering and treat AI like some magical universal function that doesn’t fail.

**It’s not there yet.**

To fix t
his limitation, we must write code that only interacts with AI when absolutely necessary—that is, when a system needs so
me sort of “human-level” analysis of unstructured data. Subsequently, whenever possible, we must force the LLM to return
 references to information (i.e., a pointer) instead of the data itself.

**When I recognized these two things, I had to
 redesign the backend architecture of my personal software business completely.**

# Rearchitecting Jellypod

For contex
t, I started an app called Jellypod. It enables users to subscribe to email newsletters and get a daily summary of the m
ost important topics from all of them as a single podcast.

This seems pretty simple on the outside—and the MVP honestly
 was. The app would just process each email individually, summarize it, convert it to speech, and stitch all the audio t
ogether, side-by-side, into a daily podcast.

The output was fine, but it needed to be better.

If two different newslet
ters discussed the same topic, the “podcast” would talk about it twice, not realizing we had already mentioned it. You c
ould say, “Well, why don’t you just stuff all the newsletter content into one big LLM call to summarize everything?”

We
ll, that’s what I tried at first.

And it failed. **Miserably.**

Even with an extremely detailed prompt using all the b
est practices, I couldn’t guarantee that the LLM would always detect the most important topics, summarize everything, an
d consistently create an in-depth output. Also, the podcast always needed to be ~10 minutes long.

So I went back to the
 drawing board. How can I make this system better? And yes, we’re getting to the cost reduction part - don’t worry!

# D
efining the Requirements

Jellypod must be able to process any number of input documents (newsletters) and create an out
put that always includes the top ten most important topics across all those inputs. If two subparts of any input are abo
ut the same topic, we should recognize that and merge the sections into one topic.

For example, if the Morning Brew has
 a section about US Elections and the Daily Brief also has a section on the current state of US Politics, they should be
 merged. I’ll skip over how I determined a similarity threshold (i.e., should two topics be merged or remain separate).


# Exploding Costs

I built on top of a few different approaches outlined in papers written by the LangChain community t
o semantic chunk and organize everything in a almost deterministic way.

**But this was INSANELY expensive.** The number
 of API calls grew at a rate of O(n log n), with n being the number of input chunks from all newsletters.

So, I had a d
ilemma. Do I keep this improved and more expensive architecture or throw it down the drain?

I decided to keep it and fi
gure out how to reduce costs.

# Reducing Costs

That’s when I discovered a tool called OpenPipe that allows you to fine
-tune open-source models almost too easily. It looked legit and was backed by YCombinator, so I gave it a try.

I swappe
d out the OpenAI SDK with their SDK (a drop-in replacement), which passed all my LLM API calls to OpenAI but recorded al
l inputs and outputs. This created unique datasets for each of my prompts, which I could use to fine-tune a cheaper open
-source model.

After about a week of recording Jellypod’s LLM calls, I had about 50,000 rows of data. And with a few cl
icks, I fine-tuned a Mistral 7B model for each LLM call.

I replaced GPT-4 with the new fine-tuned model.

**And it redu
ced the costs by 88%.**

The cost of inference dropped from $10 per 1M input tokens to $1.20. And cost per output token 
dropped from $30 to $1.60.

I was blown away. I could now run Jellypod’s new architecture for approximately the same cos
t as the MVP’s trivial approach. I even confirmed that the fine-tuned Mistral output quality was just as high as GPT-4 b
y a series of evals and in-app customer feedback.

By redesigning the system to only use AI for the smallest unit of wor
k it’s actually needed for, I could confidently deploy a fine-tuned model as a drop-in replacement for GPT 4. And by pro
mpting to return pointers to data instead of the data itself, I could ensure data integrity while reducing the number of
 output tokens consumed.

# In Conclusion

If you’re considering building an AI application, I would encourage you to ta
ke a step back and think about your architecture’s output reliability and costs. What happens if the LLM doesn’t answer 
your prompt in the right way? Can you prompt the model to return data identifiers instead of raw data? And, is it possib
le to swap GPT-4 with a cheaper, fine-tuned model?

I wish I had these insights when I started, but hey, you live and le
arn.

I hope you found at least some parts of this interesting! I thought there were enough learnings to share. Feel fre
e to reach out if you’re curious about the details.
```
---

     
 
all -  [ [For Hire] Programmer/Web Developer/IT Consultant (Python, PHP, AI, etc.) ](https://www.reddit.com/r/forhire/comments/1b8zd7n/for_hire_programmerweb_developerit_consultant/) , 2024-03-11-0910
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

     
 
all -  [ Github web loader + Pinecone Index fail due to UTF-16 encoding when trying to Upsert vector embeddin ](https://www.reddit.com/r/LangChain/comments/1b8xh9g/github_web_loader_pinecone_index_fail_due_to/) , 2024-03-11-0910
```
Hi folks, I'm putting together a simple Github RAG chatbot using \`GithubRepoLoader\` and Pinecone vector store. However
 when upserting the embeddings to Pinecone, the upsert process fails with the error: \`PineconeBadRequestError: Missing 
low surrogate.\`  
After a bit of research this seem to be due to how UTF-16 encodes the Unicode Characters outside the 
BMP (Basic Multilingual Plane) are represented using a pair of surrogate code points in UTF-16 encoding. The error messa
ge indicates that a high surrogate code point (D800–DBFF) was found without a corresponding low surrogate (DC00–DFFF) fo
llowing it.  
Now with that being said, my question is:   
Would it be feasible to use UTF-8 instead? Where would be a g
ood place (at what level of the stack) in the code would you make some changes to inject a parameter for a different (i.
e. UTF-8) encoding?  
TYIA
```
---

     
 
all -  [ After struggling with LangChain text splitters, I decided to make my own convenient service to chunk ](https://www.reddit.com/r/LangChain/comments/1b8trzs/after_struggling_with_langchain_text_splitters_i/) , 2024-03-11-0910
```
In my experience developing RAG-based applications with LangChain, I was surprised to find that there aren't any simple,
 reliable ways to chunk files. The default [Text Splitters](https://js.langchain.com/docs/modules/data_connection/docume
nt_transformers/) that LangChain offers employ a naive form of chunking that doesn't consider positioning data like sect
ions, subsections, paragraphs or tables. 

This led me to implement my own chunking service that includes deep positioni
ng data like page index and bounding box coordinates for every chunk.

You can try it out for free here (no account/api 
key required):

https://filechipper.com

Would any of you be interested in something like this? Let me know!
```
---

     
 
MachineLearning -  [ [D] : Scale PDF Q&A App to 10K Users with GPUs – <$250/Mo ](https://www.reddit.com/r/MachineLearning/comments/1b6jv56/d_scale_pdf_qa_app_to_10k_users_with_gpus_250mo/) , 2024-03-11-0910
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

     
 
MachineLearning -  [ [D] What Is Your LLM Tech Stack in Production? ](https://www.reddit.com/r/MachineLearning/comments/1b4sdru/d_what_is_your_llm_tech_stack_in_production/) , 2024-03-11-0910
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

     
 
MachineLearning -  [ [D] Graphs + vectordbs? Need your input: Cognee.ai . AI Data Pipelines for Real-World Production (Pa ](https://www.reddit.com/r/MachineLearning/comments/1aweo71/d_graphs_vectordbs_need_your_input_cogneeai_ai/) , 2024-03-11-0910
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

     
 
MachineLearning -  [ [D] AI projects Suggestions ](https://www.reddit.com/r/MachineLearning/comments/1aunkmw/d_ai_projects_suggestions/) , 2024-03-11-0910
```
Hi Everyone, I need a suggestion to create AI courses for students ( Hands-on AI projects). I am thinking about the late
st AI trends such as Langchain, RAG, and vector databases. In each project, there can be multiple tasks, and the main th
ing is each task should have an automated system in which we can verify whether students have done it correctly or not.


For example: Project with visualization cannot be automatically tested. 

For example: A project with visualization can
not be automatically tested. . em can verify if the length of the text is smaller we can verify that it is correct.
```
---

     
 
MachineLearning -  [ Whats in your RAG setup? [D] ](https://www.reddit.com/r/MachineLearning/comments/1apcp2w/whats_in_your_rag_setup_d/) , 2024-03-11-0910
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

     
