 
all -  [ Strategy for PDF data extraction and Display ](https://www.reddit.com/r/LangChain/comments/16z7sfl/strategy_for_pdf_data_extraction_and_display/) , 2023-10-04-0909
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

Any tips or best practices are welcome!
```
---

     
 
all -  [ Langchain Chatbot is not that great.. ](https://www.reddit.com/r/LangChain/comments/16z7nzk/langchain_chatbot_is_not_that_great/) , 2023-10-04-0909
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

     
 
all -  [ After a few hours of battleing to make it understand ](https://www.reddit.com/r/LangChain/comments/16z54mf/after_a_few_hours_of_battleing_to_make_it/) , 2023-10-04-0909
```
This is peak prompt engineering.

&#x200B;

&#x200B;

https://preview.redd.it/emhr6d2p92sb1.png?width=957&format=png&aut
o=webp&s=2b8e1aa1f37b31c1864b7a432a49239bb4086efa
```
---

     
 
all -  [ User Feedback for RAG ](https://www.reddit.com/r/LangChain/comments/16z4rn3/user_feedback_for_rag/) , 2023-10-04-0909
```
I’ve read about using AI to generate sample questions and answers, then having end-users provide feedback and using that
 data to fine-tune a model. Would this approach would with embeddings and RAG? If the vector embedding contained sample 
questions and answers, could I prompt the bot to answer in the style of the sample answers from the embedding?
```
---

     
 
all -  [ Here to try to solve your LLM problems ](https://www.reddit.com/r/LangChain/comments/16z4mha/here_to_try_to_solve_your_llm_problems/) , 2023-10-04-0909
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

     
 
all -  [ can RAG models base their answers from outside the documents? ](https://www.reddit.com/r/LangChain/comments/16z4bd3/can_rag_models_base_their_answers_from_outside/) , 2023-10-04-0909
```
can RAG models base their answers from outside the documents used?
```
---

     
 
all -  [ [Announcement] Upcoming event – Reddit AMA with Harrison Chase, co-founder and CEO of LangChain: Tue ](https://www.reddit.com/r/LangChain/comments/16z1s1p/announcement_upcoming_event_reddit_ama_with/) , 2023-10-04-0909
```
Join us on Tuesday, October 24th from 9-11 AM Pacific (12-2 PM Eastern) for an **AMA hosted** by **Harrison Chase, co-fo
under and CEO of LangChain**. This is your opportunity to ask Harrison questions about utilizing LangChain in developing
 large language model (LLM) applications, and to *share your own ideas and suggestions*. Take advantage of this chance t
o learn more about how to leverage LangChain in your own projects and get insights into latest developments.
```
---

     
 
all -  [ Use multiple Chroma Databases in Langchain ](https://www.reddit.com/r/LangChain/comments/16z0nkh/use_multiple_chroma_databases_in_langchain/) , 2023-10-04-0909
```
I'm working on making a chatPDF-like program for a school professor but he requested to keep the subjects divided, so I 
was thinking about making different pages for my website, each for every subject and link to every page a specific chrom
aDB, I don't know if it's possible though and I haven't found anything on the documentation.

Has anyone tried this befo
re or knows if it's even possible?
```
---

     
 
all -  [ My Journey with Langchain on finishing my MA and reinventing Dropbox powered by GPT ](https://www.reddit.com/r/LangChain/comments/16yz1ej/my_journey_with_langchain_on_finishing_my_ma_and/) , 2023-10-04-0909
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

     
 
all -  [ [P] An HF-space to check if your GPUs can run a model ](/r/LocalLLaMA/comments/16yyxku/p_an_hfspace_to_check_if_your_gpus_can_run_a_model/) , 2023-10-04-0909
```

```
---

     
 
all -  [ New to langchain ](https://www.reddit.com/r/LangChain/comments/16yxoa2/new_to_langchain/) , 2023-10-04-0909
```
When building a QnA based bot on uploaded Pdfs (like the many examples online), when the bot is answering questions does
 it just look at the docs for answers or is it broader?

sorry for the basic question
```
---

     
 
all -  [ Looking for Co-Founder to join an early stage start-up ](https://www.reddit.com/r/LangChain/comments/16yx4xs/looking_for_cofounder_to_join_an_early_stage/) , 2023-10-04-0909
```
I'm on the lookout for two passionate co-founders: one with technical expertise and another with a flair for marketing a
nd sales, to embark on an exciting journey with me. Here's a bit about the venture and myself:

**About the Startup**:


* **Niche**: We aim to revolutionize how companies integrate Legal Lifecycle Management (LLM) systems into their existin
g applications, making the process seamless and efficient.
* **Stage**: We are at the inception stage. I recently took t
he leap of faith and quit my full-time job to make this dream a reality.

**About Me**:

* **Background**: Graduated fro
m high school 2 years ago.
* **Experience**: Jumped straight into the tech scene and served as a software developer at a
 startup for 2 years. Has built and shipped 6 products with live users. Led the development of 2 of them.

**What I'm Lo
oking for**:

1. **Technical Co-founder**:

* **Skillset**: We are building it out in Next.js, TypeScript, Tailwind, and
 Prisma. Needs to be proficient in using Langchain. 
* **Mindset**: Entrepreneurial, ready for challenges, and committed
 to the cause.

1. **Marketing/Sales Co-founder**:

* **Skillset**: Proven experience in startup marketing, B2B sales, o
r SaaS marketing would be a big plus. Ability to strategize, execute, and optimize marketing campaigns, while also under
standing the nuances of selling tech solutions.
* **Mindset**: Growth-focused, data-driven, and someone who understands 
the startup hustle.

If any of the above roles resonate with you and wants to learn more send me an email at [shanyuzhan
g123@gmail.com](mailto:shanyuzhang123@gmail.com) or DM me.
```
---

     
 
all -  [ Best LLM serving providers for cost, latency, quality, auto-tuning & fine-tuning. ](https://www.reddit.com/r/LangChain/comments/16yssmf/best_llm_serving_providers_for_cost_latency/) , 2023-10-04-0909
```
I've been using OpenAI's API directly primarily thus far. Hugging Face looks interesting - but I'm not really clear on t
heir pricing or what models to select.
```
---

     
 
all -  [ How to know the langchain BTS? ](https://www.reddit.com/r/LangChain/comments/16yscor/how_to_know_the_langchain_bts/) , 2023-10-04-0909
```
How can I understand the system prompts langchain gives when I insert the pdf?
```
---

     
 
all -  [ How can i merge 2 Models? ](https://www.reddit.com/r/LocalLLaMA/comments/16yrc6c/how_can_i_merge_2_models/) , 2023-10-04-0909
```
so i have 2 models that are very good the synthia-34b-v1.2.Q4\_K\_M is uncensored but not that good for langchain while 
the speechless-llama2-hermes-orca-platypus-wizardlm-13b.Q8\_0 is perfect for langchain but its censored so is there a wa
y to merge them together to make the synthia-34b better or the speechless-llama2-hermes-orca-platypus-wizardlm-13b uncen
sored i have a 3090 if that changes anything
```
---

     
 
all -  [ Automating comic creation using Langchain ](https://www.reddit.com/r/LangChain/comments/16yozpt/automating_comic_creation_using_langchain/) , 2023-10-04-0909
```
hello,
I am trying to learn programming as a hobby (I have some experience with visual scripting as level designer). 
I 
would like to learn python with a project that will motivate me, so here is a project I would love to achieve : generati
ng a comic book as automatically as possible.

I want to learn to use OpenAI api, to help me automate the creation of a 
comics. I would like to be able to chain prompts to brainstorm ideas, then develop the characters relations, the world, 
and the overall story arc, and finally generate the story page by page… and generate image with dale when it is possible
 (soon hopefully)

Unfortunately I am lacking some basic knowledge to help me get started. Is langchain a good framework
  for this kind of prompt chaining project, also parsing of a csv/xml file with my prompts.
Any recommended resources or
 tutorials that can help me get started?

If you know someone who is working on similar project or have brick of codes I
 would love to hear about.

I'm grateful for any advice or pointers you can offer!
Thanks
```
---

     
 
all -  [ Is it possibile to connect to the 'Browse with Bing' feature on Open AI? ](https://www.reddit.com/r/LangChain/comments/16yn5bp/is_it_possibile_to_connect_to_the_browse_with/) , 2023-10-04-0909
```
Just wondering if there is anyway to call upon it through langchain.
```
---

     
 
all -  [ How to stream AI responses from server actions? ](https://www.reddit.com/r/nextjs/comments/16yjgi2/how_to_stream_ai_responses_from_server_actions/) , 2023-10-04-0909
```
Does anyone know if and how I can stream ChatGPT responses from server actions? I have Vercel's `ai` library and Langcha
in installed.
```
---

     
 
all -  [ What are some of your gripes with Langchain? ](https://www.reddit.com/r/LangChain/comments/16yj4s2/what_are_some_of_your_gripes_with_langchain/) , 2023-10-04-0909
```
langchain has gotten too complicated, so i'm building [tinylang](https://github.com/astelmach01/tinylang), a simpler alt
ernative.

what are some things you'd like to see?  
what are some things in langchain that just seem super unecessary o
r annoying?
```
---

     
 
all -  [ Overview: AI Assembly Architectures ](https://www.reddit.com/r/AI_Agents/comments/16yc9zg/overview_ai_assembly_architectures/) , 2023-10-04-0909
```
I'm currently trying to make a list with all agent-systems, RAG systems, cognitive architectures, and similar. Then coll
ecting data on the features and limitations, as many points of distinction as possible, opinions, ... Input is welcome.


- Auto-GPT: [github.com/Significant-Gravitas/Auto-GPT](https://github.com/Significant-Gravitas/Auto-GPT)
- AutoGen: [gi
thub.com/microsoft/autogen](https://github.com/microsoft/autogen)
- BASI: [github.com/oliveirabruno01/babyagi-asi](https
://github.com/oliveirabruno01/babyagi-asi)
- BabyAGI: [github.com/yoheinakajima/babyagi](https://github.com/yoheinakajim
a/babyagi)
- GripTape: [griptape.ai](https://griptape.ai)
- Jarvis: [github.com/microsoft/JARVIS](https://github.com/mic
rosoft/JARVIS)
- LangChain [docs.langchain.com/docs](https://docs.langchain.com/docs)
- LlamaIndex: [github.com/run-llam
a/llama\_index](https://github.com/run-llama/llama_index)
- Open-Assistant [github.com/LAION-AI/Open-Assistant](https://
github.com/LAION-AI/Open-Assistant)
- Semantic Kernel [github.com/microsoft/semantic-kernel](https://github.com/microsof
t/semantic-kernel)
- SmartGPT: [github.com/Cormanz/smartgpt](https://github.com/Cormanz/smartgpt)
- TxAI: [github.com/ne
uml/txtai](https://github.com/neuml/txtai)
- tinyLLM: [github.com/zozoheir/tinyllm](https://github.com/zozoheir/tinyllm)


# Chatbots and Conversational AI:
- BondAI: [github.com/krohling/bondai](https://github.com/krohling/bondai)
- BeeBot:
 [github.com/AutoPackAI/beebot](https://github.com/AutoPackAI/beebot)

# Machine Learning and Data Processing:
- NeMo-Gu
ardrails: [github.com/NVIDIA/NeMo-Guardrails](https://github.com/NVIDIA/NeMo-Guardrails)
- Haystack: [github.com/deepset
-ai/haystack](https://github.com/deepset-ai/haystack)
- EdgeChains: [github.com/arakoodev/EdgeChains](https://github.com
/arakoodev/EdgeChains)

# Frameworks for Advanced AI, Reasoning and Cognitive Architectures:
- ACT-R (Adaptive Control o
f Thought - Rational)
- Soar
- CLARION
- OpenCog: [github.com/opencog](https://github.com/opencog)
- Dave Shapiro: [yout
ube.com/@4IR.David.Shapiro](https://youtube.com/@4IR.David.Shapiro)
- Some guys from IBM Watson worked on it (forgot the
 name)
- Cyc: [en.wikipedia.org/wiki/Cyc](https://en.wikipedia.org/wiki/Cyc)

# Agents in a Virtual Environment
- MineRL
: [minerl.io](https://minerl.io)
- Malmo: [github.com/malmo](https://github.com/microsoft/malmo)
- AgentVerse: [github.c
om/AgentVerse](https://github.com/OpenBMB/AgentVerse)

# Comments and Comparissons (probably outdated)
- /r/ChatGPT/comm
ents/12cql0c/autogpt_vs_babyagi/
- /r/AutoGPT/comments/15jrs4n/autogpt_is_failing_to_acomplish_its_goals/

# Curated Lis
ts
- [github.com/awesome-ai-agents](https://github.com/e2b-dev/awesome-ai-agents)
- [github.com/Awesome-AGI](https://git
hub.com/EmbraceAGI/Awesome-AGI)

# Recommended Tutorials
- RAG: gpt-index.readthedocs.io/en/latest/examples/low_level/os
s_ingestion_retrieval.html
- RAG: https://python.langchain.com/docs/expression_language/cookbook/retrieval

EDIT: Update
d from time to time.
```
---

     
 
all -  [ [P] Best option for a large, local embedding database? ](https://www.reddit.com/r/MachineLearning/comments/16y9k4x/p_best_option_for_a_large_local_embedding_database/) , 2023-10-04-0909
```
Langchain offers a wide array of vector databases for text embedding models. I need to create a vector database for arou
nd 3 million sentence embeddings, each being of dimension 384. I'm building a prototype, so it has to be local and free 
of charge to use.

So far, I've hit limits for Chroma (41,666 max). I've also tried Redis, QDrant and FAISS - each of th
ese gets so large that it eats up all the RAM and the process gets killed, or with QDrant, just errors out.

I've used P
inecone before, but I don't really want to pay for a prototype as I have plenty of disk space.

I was thinking of chunki
ng the 3 million documents into local vector stores of size 41,666 using ChromaDB - but there isn't a whole lot out ther
e about whether Chroma would allow me to merge all \~70 of these smaller databases into a bigger one for search. I also 
cannot find whether it would be possible to load all 70 of these into memory and search each one individually.

So what 
are my options?

My other thought was just creating a large Doc2Vec model, however I would like to use something more so
phisticated like Huggingface embedding models.
```
---

     
 
all -  [ Building a Chatbot for Internal Document Retrieval Using Language Models ](https://www.reddit.com/r/LangChain/comments/16y76tm/building_a_chatbot_for_internal_document/) , 2023-10-04-0909
```
Hello everyone,

I am currently an intern at a company and am exploring a project idea to pave my way to a full-time pos
ition. I've noticed that employees often need to share and request information contained in various documents (Excel fil
es, emails, etc.). I am considering creating a chatbot to simplify this information retrieval process across different d
epartments.

I've begun by learning about language models and have managed to set up a system that loads documents from 
a directory, converts them to text, and utilizes OpenAI's embedding model to create and save embeddings to a Chroma data
base. I've tested this setup with some machine history data in CSV format provided by a coworker. The goal is to answer 
queries like, 'What's the average number for this column between these dates?' However, the system should also handle em
ails, PDFs, Excel, and Word files.

I used the Llama 7B model for embedding because  I was hitting a token limit per min
ute with the OpenAI model, especially with large files (\~10,000 lines of data). After setting up the VectorDB, I faced 
a token limit issue again while trying to answer questions due to the large amount of data being processed.

Considering
 the privacy and performance requirements, I am also contemplating the use of a local AI model on a powerful machine ins
tead of relying on cloud-based solutions like OpenAI. This could potentially address the performance issues and ensure b
etter data privacy and maybe help me to overcome token limitations.

I initially tried using OpenAI's embedding model to
 process the documents, but I ran into a limitation on the number of tokens that could be processed per minute. Due to t
his restriction, I decided to switch to a local model for embedding, specifically the [**Mistral-7B-v0.1 model**](https:
//huggingface.co/mistralai/Mistral-7B-v0.1) from Hugging Face. This switch allowed me to process the documents and build
 the database without hitting any token limitations. Now that the database is complete, I've switched back to using Open
AI for other parts of the process. However, I am not entirely sure if everything is set up correctly as this code has be
en pieced together over the past three days, and I'm eager to ensure it's on the right track.  


My code:  [here](https
://textbin.net/wibm5znigu)

**Here are my requirements:**

1. Ensure high privacy.
2. Handle a large amount of data effi
ciently.
3. Provide quick responses.
4. Achieve 99% accuracy based solely on document information.

**I have several que
stions and would appreciate any insights:**

1. Am I on the right track with my current approach?
2. Is ChromaDB the rig
ht choice, or is there a better database for my needs?
3. Would a local AI model be more suitable, or is OpenAI preferab
le in this scenario?
4. Are there other models better suited for embedding or chatting, especially with Excel and CSV fi
les? If yes, is it advisable to use different models for different file types?

**Ideally, I'd like to:**

* Specify dat
a (e.g., by department or file name) to make easy for AI.
* Retain a memory of chats for follow-up queries based on prev
ious responses.
* Update the database with new files and data seamlessly.

*Please note that I am not seeking help due t
o laziness; I am on a time limit for this project. While I would continue searching for solutions, any assistance that c
ould help expedite my progress would be greatly appreciated.*

Thank you for your time and suggestions!
```
---

     
 
all -  [ Not split PDF's ](https://www.reddit.com/r/LangChain/comments/16y6ist/not_split_pdfs/) , 2023-10-04-0909
```
I'm trying to process PDF's without splitting them by pages. I essentially want to consider the entire PDF as a single d
ocument. Should I convert the PDF to a single TXT file and then process it or is there anything within the documentation
. I was not able to find anything in the documentation.
```
---

     
 
all -  [ Limiting BabyAGI tasks list... ](https://www.reddit.com/r/LangChain/comments/16y41tc/limiting_babyagi_tasks_list/) , 2023-10-04-0909
```
I have been looking into BabyAGI capabilities and have a small setup done where I have :

*  research reports (PDF) inge
sted in my vector store(azure search)
* ToDo and  ConversationalRetrievalChain  provided as tools to agent\_executor

No
w when i run babyagi with an objective it starts creating tasks using todo tool, which uses openai as llm. But the tasks
 are way out of context from what I have in my search vectordb. Thus, the agent keep creating tasks which cannot be acco
mplished based on data I have in my search index.  


This results in agent going in loops and tasks keep growing until 
max\_iteration count i reached and ends with no answer.  


So, Is there a way to constrict tasks to what can be accompl
ished from knowledge base? Or skip the ones that failed to complete and generate answer out of what was accomplished?
```
---

     
 
all -  [ Chatbot for website? ](https://www.reddit.com/r/LangChain/comments/16y2u4o/chatbot_for_website/) , 2023-10-04-0909
```
How to build a Chatbot that can be integrated with existing websites?
```
---

     
 
all -  [ Langchain tool ](https://www.reddit.com/r/LangChain/comments/16y2p94/langchain_tool/) , 2023-10-04-0909
```
I am looking for a tool easy to setup and fully managed where langchain vector database and API to retrieve information 
can be included. What is your favorite tool? Thanks
```
---

     
 
all -  [ github web scraping? ](https://www.reddit.com/r/ChatGPT/comments/16xy8s9/github_web_scraping/) , 2023-10-04-0909
```
does anyone know the best way to get a whole documentation in a suitable format to integrate with an llm?

I'm thinking 
about using pinecone/langchain to teach an llm my codebase. but the first step is to get the data from the repo.

I trie
d using 'apify' directly on the main github repo page but it seems inefficient and like it ends up with a bunch of usele
ss data.

apologies if any of this is absurd, im new to it. (also is all of this kosher with github's terms and conditio
ns and stuff?)
```
---

     
 
all -  [ github repo scraping? ](https://www.reddit.com/r/LargeLanguageModels/comments/16xy7rz/github_repo_scraping/) , 2023-10-04-0909
```
does anyone know the best way to get a whole documentation in a suitable format to integrate with an llm?

I'm thinking 
about using pinecone/langchain to teach an llm my codebase. but the first step is to get the data from the repo. 

I tri
ed using 'apify' directly on the main github repo page but it seems inefficient and like it ends up with a bunch of usel
ess data. 

apologies if any of this is absurd, im new to it.  (also is all of this kosher with github's terms and condi
tions and stuff?)
```
---

     
 
all -  [ Running OpenAI on top of Function Calls / Agents? ](https://www.reddit.com/r/LangChain/comments/16xvdp6/running_openai_on_top_of_function_calls_agents/) , 2023-10-04-0909
```
We have created a custom agent on top of the built-in CSV and SQL agent - it works great.

Behind the scenes, its runnin
g python code, and I cannot figure out how to run OpenAI Functions on top of that code.

For example, if i upload a CSV 
file, i would like to run OpenAI sentiment on top of the dataset - instead, all the code can run is the built-in python 
libraries, like NLTK, which is weirdly limiting.

Am I missing something?
```
---

     
 
all -  [ Doubt about embeddings with vector stores ](https://www.reddit.com/r/LangChain/comments/16xub91/doubt_about_embeddings_with_vector_stores/) , 2023-10-04-0909
```
Hi guys!

I have adoubt about embedding prices, so here it's the code I'm currently using, which worked (I modified it f
or private information)  


    loader = ConfluenceLoader(url='https://confluenceweb.com', token='tokenConfluence')
    

    documents = loader.load(
        space_key='spaceKey', include_attachments=False, limit=50, max_pages=20
    )
    

    text_splitter = RecursiveCharacterTextSplitter(chunk_size = 500, chunk_overlap = 0)
    
    all_splits = text_spli
tter.split_documents(documents)
    
    vectorstore = Chroma.from_documents(documents=all_splits, embedding=OpenAIEmbed
dings(openai_api_key='openApiKey'))
    
    query = 'Question for the model'
    docs = vectorstore.similarity_search(q
uery)
    
    llm = ChatOpenAI(model_name='gpt-3.5-turbo', temperature=0, openai_api_key='openAiApiKey', max_tokens=100
)
    qa_chain = RetrievalQA.from_chain_type(llm,retriever=vectorstore.as_retriever())
    result = qa_chain({'query': q
uery})
    

The goal of this code is the following: We want to make QA for the information in our Confluence. We want t
o train the model to answer as an assistant for a customer portal.  


**My doubt is the following one:** Do I always ha
ve to pay the price for OpenAiEmbeddings? I've just tried using Chroma, one of the vectorstores recomended in the docume
ntation. In case I execute this code several times, will I always have to pay it?   


Is there any way to have this  se
parated in **two scripts? One for the 'ingestion'** of information from our documents into the vector store and a s**eco
nd script that just asks the model without having to pay the embedding again**. I know that I will always have to pay fo
r passing the question with the prompt and for generating the answer... But is there a way to load everything from my Co
nfluence, embed it and then just make different questions over it? Or will I always need to pay the embedding price?

Sh
ould I just use an open-source free embedding solution like  all-MiniLM-L6-v2? **This project is going to be hosted in A
mazon Web Services**, so I dont know if there would be any kind of problem with that because we dont want to have any lo
cal machine running this code.

&#x200B;

I'm really confused about vector stores, if you could guide me, it would mean 
a lot.

&#x200B;
```
---

     
 
all -  [ Best way to distill information from a long HTML document? ](https://www.reddit.com/r/LocalLLaMA/comments/16xtjq0/best_way_to_distill_information_from_a_long_html/) , 2023-10-04-0909
```
Hi, I am looking for some pointers to distill information from a single, large but quite structural (to human) **HTML** 
document containing some event schedules\*. 

I am using langchain's WebBaseLoader to perform the data ingestion, Recurs
iveCharacterTextSplitter for chunking and Chroma DB as the vector store. Retrieval is done using ConversationalRetrieval
Chain.

The problems I am facing are the title of the event and the schedule information do not sit next to each other, 
and the html2text essentially messed up all the event-schedule relationship (it ended up with all the events jammed toge
ther in one long paragraph and the schedules scattered everywhere). The chunking of text also led to further separation 
of the events and schedule information, and that the answers produced, if any, were only limited to what the maximum con
text the LLM could handle.

My questions are, do you have a better experience dealing with this kind of problem involvin
g many large HTML tables in a single long HTML document? What is the best way to have the LLM to parse and understand su
ch document in order to extract information, not from part of it, but through the whole thing in order to compose the an
swer?

\* A very typical example is [https://www.royalalberthall.com/tickets/](https://www.royalalberthall.com/tickets/)
 . with the exception that the title and the schedule are farther apart (many tables each with many rows). I would like 
to make a query to the LLM such as:

'List all classical music concerts in Oct 2023 in a tabular form containing only th
e titles and the date-time of the concert. For examples:

Title | Date

Easy listening classical | 28 Oct 18:30

Four se
asons- Winter | 30 Oct 19:00'
```
---

     
 
all -  [ llama-cpp on T4 google colab, Unable to use GPU ](https://www.reddit.com/r/LocalLLaMA/comments/16xswej/llamacpp_on_t4_google_colab_unable_to_use_gpu/) , 2023-10-04-0909
```
 In Google Colab, though have access to both CPU and GPU T4 GPU resources for running following code. However, what is t
he reason I am encounter limitations, the GPU is not being used?  I selected T4 from runtime options  

`!CMAKE_ARGS='-D
LLAMA_BLAS=ON -DLLAMA_BLAS_VENDOR=OpenBLAS' pip install llama-cpp-python`

&#x200B;

`!pip install langchain`

`!wget` [
`https://huggingface.co/TheBloke/Llama-2-7b-Chat-GGUF/resolve/main/llama-2-7b-chat.Q5_0.gguf`](https://huggingface.co/Th
eBloke/Llama-2-7b-Chat-GGUF/resolve/main/llama-2-7b-chat.Q5_0.gguf)

&#x200B;

`from langchain.llms import LlamaCpp`

`f
rom langchain.prompts import PromptTemplate`

`from langchain.chains import LLMChain`

`from langchain.callbacks.manager
 import CallbackManager`

`from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler`

&#x200B;

`
prompt = PromptTemplate(template=template, input_variables=['question'])`

&#x200B;

`callback_manager = CallbackManager
([StreamingStdOutCallbackHandler()])`

&#x200B;

`llm = LlamaCpp(`

`model_path='/content/llama-2-7b-chat.Q5_0.gguf',`


`temperature=0.75,`

`max_tokens=500,`

`top_p=1,`

`callback_manager=callback_manager,`

`verbose=True,`

`)`

`llm_cha
in = LLMChain(prompt=prompt, llm=llm)`

&#x200B;

`llm_chain.run(question)`

&#x200B;
```
---

     
 
all -  [ How to download Spotify podcast transcripts? ](https://www.reddit.com/r/LangChain/comments/16xqnid/how_to_download_spotify_podcast_transcripts/) , 2023-10-04-0909
```
Has anyone figured out the best way to process and summarize Spotify podcast?
```
---

     
 
all -  [ About to buy Hardware for 7k ](https://www.reddit.com/r/LocalLLaMA/comments/16xq65o/about_to_buy_hardware_for_7k/) , 2023-10-04-0909
```
 Hey,

At the end of the month, I'll be receiving a profit share of 7k, which I intend to use to purchase hardware for a
n LLM.

I was thinking of:

2x 3090(Used) Intel Core i9-13900K 256GB DDR5 RAM A suitable motherboard, of course (500-1k$
) Is a 1000W PSU enough, or would a 1500W PSU be better?

Using the cloud is not an option for me because I want to trai
n my LLM on my own data, and I generally prefer it to be uncensored, as I'm tired of hearing phrases like, 'As an LLM, I
'd like to remind you that blablabla.'

The goal is to learn how to create a self-operating AI Assistant with Langchain,
 etc., and an RAG where I can store ALL my knowledge about everything that interests me. I just want to dive in and lear
n by working on various projects and expanding my knowledge.

I'm thinking of using 2x 3090 so that I can experiment wit
h combining different models and see how they interact with each other, among other things.

I'm just asking here for an
y potential pitfalls to watch out for. Any hardware suggestions? Are there any good beginner projects?

I'm not particul
arly skilled in Python, but that doesn't mean I can't learn it.
```
---

     
 
all -  [ Which is the best open-source LLM, that can be used well in colab or kaggle ](https://www.reddit.com/r/LangChain/comments/16xpxs4/which_is_the_best_opensource_llm_that_can_be_used/) , 2023-10-04-0909
```
I have been trying to use falcon40b models and gpt Neo models in colab, which model can I possibly use as I can't use th
e above two models as I have resource issues. Only after this I can proceed further to the langchain part. So please hel
p ASAP
```
---

     
 
all -  [ Help With running self hosted LLM using LangChain ](https://www.reddit.com/r/LangChain/comments/16xdxmc/help_with_running_self_hosted_llm_using_langchain/) , 2023-10-04-0909
```
Hi,

I have been trying langchain to run llama-7b model on my server following the documentation at : [https://python.la
ngchain.com/docs/integrations/llms/huggingface\_pipelines](https://python.langchain.com/docs/integrations/llms/huggingfa
ce_pipelines) and seem to run into an issue where i get the error message:

    ValueError: Pipeline with tokenizer with
out pad_token cannot do batching. You can try to set it with \pipe.tokenizer.pad_token_id = model.config.eos_token_id`.`


I tried upgrading, downgrading the transformers library, playing around with it etc. nothing seems to work.I was tryin
g to follow along with this notebook: [https://colab.research.google.com/drive/17eByD88swEphf-1fvNOjf\_C79k0h2DgF?usp=sh
aring#scrollTo=uwII3CSHxgsM](https://colab.research.google.com/drive/17eByD88swEphf-1fvNOjf_C79k0h2DgF?usp=sharing#scrol
lTo=uwII3CSHxgsM) and replacing OpenAI with HuggingFacePipeline does not seem to work as well.

Please enlighten me on w
hat i am doing wrong and how can i fix this to work on my machine?

Test Code (after all the imports)

    # Create the 
LLM Pipeline
    
    llm = HuggingFacePipeline.from_model_id(
        model_id='daryl149/llama-2-7b-hf', 
        task=
'text-generation',
        model_kwargs={
            'temperature': 0,
            'max_length': 100
            }
    
)
    llm('Hello, World!') # this crashes but if llm = OpenAI() then it does not crash. 

&#x200B;
```
---

     
 
all -  [ Dialoqbase – open source chatbot creation platform ](https://www.reddit.com/r/OpenAI/comments/16x8klh/dialoqbase_open_source_chatbot_creation_platform/) , 2023-10-04-0909
```
Hey r/OpenAI friends, 

I've been dedicating the past 3 months to a side project centered on LangchainJS and pgvector. I
'm excited to share that it has evolved significantly during this time. The project currently boasts support for various
 AI models, including OpenAI ChatGPT and other chat models. Moreover, it can seamlessly integrate with popular messaging
 platforms such as ***WhatsApp***, ***Telegram***, and ***Discord***.  


[demo](https://preview.redd.it/0113cd3hvmrb1.p
ng?width=1920&format=png&auto=webp&s=ca6c3e170991d721743cede5176e7f72b94b4fdd)

In addition to these advancements, I've 
implemented several key features to enhance the user experience, such as multi-user support, robust admin controls, and 
more. I'm eager to hear your thoughts and receive any feedback you may have. Your input is invaluable to me. Thank you!


repo: [https://github.com/n4ze3m/dialoqbase](https://github.com/n4ze3m/dialoqbase)
```
---

     
 
all -  [ [D] Perplexity.ai Search Feasibility ](https://www.reddit.com/r/MachineLearning/comments/16x63ce/d_perplexityai_search_feasibility/) , 2023-10-04-0909
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

     
 
all -  [ Dialoqbase – open source chatbot creation platform ](https://www.reddit.com/r/ChatGPTCoding/comments/16x51n5/dialoqbase_open_source_chatbot_creation_platform/) , 2023-10-04-0909
```
 I've been dedicating the past 3 months to a side project centered on LangchainJS and pgvector. I'm excited to share tha
t it has evolved significantly during this time. The project currently boasts support for various AI models, including C
hatGPT, Llama, Claude, and Bison. Moreover, it can seamlessly integrate with popular messaging platforms such as WhatsAp
p, Telegram, and Discord.

In addition to these advancements, I've implemented several key features to enhance the user 
experience, such as multi-user support, robust admin controls, and more. I'm eager to hear your thoughts and receive any
 feedback you may have. Your input is invaluable to me. Thank you!  


 repo: [https://github.com/n4ze3m/dialoqbase](htt
ps://github.com/n4ze3m/dialoqbase) 
```
---

     
 
all -  [ Best alternatives ](https://www.reddit.com/r/LangChain/comments/16x3bd6/best_alternatives/) , 2023-10-04-0909
```
There’s been a bit of time now for a few alternatives to come out to langchain.

Having started playing with it in its r
elative infancy and watched it grow (growing pains included), I’ve come to believe langchain is really suited more to ve
ry rapid prototyping and an eclectic selection of helpers for testing different implementations.

I’d love to know what 
other tools people have come across that perform some of the functionality that can be found in langchain.

Some that I’
ve looked at:

- [Llama Index AI](https://www.llamaindex.ai/)
- [GripTape](https://www.griptape.ai/)
- [tinyLLM](https:/
/github.com/zozoheir/tinyllm/tree/main)
- [NeMo-Guardrails](https://github.com/NVIDIA/NeMo-Guardrails)
```
---

     
 
all -  [ Does Langchain’s `create_csv_agent` and `create_pandas_dataframe_agent` functions work with non-Open ](https://www.reddit.com/r/LocalLLaMA/comments/16wx0fp/does_langchains_create_csv_agent_and_create/) , 2023-10-04-0909
```
Hey guys, have a question hoping if anyone knows the answer and can help.

Does Langchain's `create_csv_agent` and `crea
te_pandas_dataframe_agent` functions work with non-OpenAl LLM models too like Llama
2 and Vicuna? The only example I hav
e seen in the documentation (in the links below) are only using OpenAI API.

`create_csv_agent`:
https://python.langchai
n.com/docs/integrations/toolkits/csv

`create_pandas_dataframe_agent`:
https://python.langchain.com/docs/integrations/to
olkits/pandas

Would really appreciate ANY input on this. Many thanks!
```
---

     
 
all -  [ Creating Chatbot using langchain and streamlit ](https://www.reddit.com/r/learnpython/comments/16wvovf/creating_chatbot_using_langchain_and_streamlit/) , 2023-10-04-0909
```

Hi everyone! 
I am creating a chatbot using langchain and streamlit 
I am using python version 3.10.1. 
My code was run
ning fine until the moment I have added langchain library it gives me an error  module not found. 
The code goes as foll
ows: 

```
import streamlit as st
from st_chat_message import message
from dotenv import load_dotenv
import os

from lan
gchain.chat_models import ChatOpenAI
from langchain.schema import (
    SystemMessage,
    HumanMessage,
    AIMessage
)



def init():
    #Load the OpenAI API key 
    load_dotenv()
    
    #Check if the API key exists
    if os.getenv('O
PENAI_API_KEY') is None or os.getenv('OPENAI_API_KEY') == '':
        print('OPENAI_API_KEY is not set')
        exit(1)

    else:
        print('OPENAI_API_KEY is set')

    #streamlit page
    st.set_page_config(
        page_title='Your 
own ChatGPT',
        page_icon='🤖'
    )


def main():
    init()

    chat = ChatOpenAI(temperature=0)

    #messages 
history
    if 'messages' not in st.session_state:
        st.session_state.messages = [
            SystemMessage(conte
nt='You are a helpful assistant.')
        ]

    st.header('Your Bot 🤖')

    #sidebar with user input
    with st.side
bar:
        user = st.text_input('Enter your message: ', key='user_input')

        #user input
        if user:
      
      st.session_state.messages.append(HumanMessage(content=user))
            with st.spinner('Thinking...'):
         
       response = chat(st.session_state.messages)
            st.session_state.messages.append(
                AIMessag
e(content=response.content))
```


I am getting the following errors: 
No module named 'langchain.chat_models'
And also 

No module named ‘langchain.schema’


If anyone could help by giving me their guidance and solution to this, I would be 
so grateful. 

Thank you
```
---

     
 
all -  [ Storing Image/Product images ](https://www.reddit.com/r/LangChain/comments/16wuefz/storing_imageproduct_images/) , 2023-10-04-0909
```
 Hi Guys, is ther any way to store image URls \[[https://static.tp-link.com/01\_1598337266170q.jpg](https://static.tp-li
nk.com/01_1598337266170q.jpg)\]  in meta data whie crawling using loader = **RecursiveUrlLoader(url=url, max\_depth=2, e
xtractor=lambda x: Soup(x, 'html.parser').text)** 
```
---

     
 
all -  [ For programmers: proposal for high level library to make prompt chains ](https://www.reddit.com/r/aipromptprogramming/comments/16wna4a/for_programmers_proposal_for_high_level_library/) , 2023-10-04-0909
```
Request for feedback! I'm considering building a high-level library for prompt chains. (Way beyond Langchain.) High-leve
l enough that the code would be a similar length as my illustrative example use cases! [Proposal and 3 illustrative exam
ple use cases here](https://docs.google.com/document/d/1uQCpWqQMzODiDtB8uO0d6tPBOhFiTiVYWLQGeLINfmQ/edit) with commentin
g turned on, and also pasted below for easy reading.

# Primary object

“Node” (or maybe “step”?)
- Inputs: Input values
 to use, wrap them in [] to use them, e.g. `subject`
- Display to user: e.g. 'Ready to write a poem about [subject]'
- R
un prompt or custom code: 'write a poem about [subject] like Dr. Seuss' or `writePoem(subject)`
- Display to user: 'Here
 is your poem: [result]'
- Outputs to Child Prompt: `result` (prompt completion)
- Child nodes: 1-n node IDs, along with
 characters to watch for in `result`, to stop streaming to user *and* indicate which child node to choose


*I need a cl
eaner term to differentiate between what is displayed to the user before, versus after, running something.*

# Illustrat
ive use cases  

## Use case 1: simple chain to gather information  

### Node 1:
```
---

     
 
MachineLearning -  [ [P] vLLM, Langchain, Embedchain ? ](https://www.reddit.com/r/MachineLearning/comments/16ndyxc/p_vllm_langchain_embedchain/) , 2023-10-04-0909
```
Which libraries do you think would be the most important to learn between these, and to use in my next personal project 
? This will be a conversational chatbot trained on podcast transcripts
```
---

     
 
MachineLearning -  [ [R] Agents: An Open-source Framework for Autonomous Language Agents - AIWaves Inc 2023 ](https://www.reddit.com/r/MachineLearning/comments/16jl4pe/r_agents_an_opensource_framework_for_autonomous/) , 2023-10-04-0909
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

     
 
MachineLearning -  [ [P] Ways to speed up llama-2 summarization on sagemaker? ](https://www.reddit.com/r/MachineLearning/comments/16iutyp/p_ways_to_speed_up_llama2_summarization_on/) , 2023-10-04-0909
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

     
 
MachineLearning -  [ [P][R] Kani: A Lightweight Highly Hackable Open-Source Framework for Building Chat Applications with ](https://www.reddit.com/r/MachineLearning/comments/16gxp51/pr_kani_a_lightweight_highly_hackable_opensource/) , 2023-10-04-0909
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

     
 
MachineLearning -  [ [D] Data Extraction using fine-tuned LLM? ](https://www.reddit.com/r/MachineLearning/comments/16fenlb/d_data_extraction_using_finetuned_llm/) , 2023-10-04-0909
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

     
 
MachineLearning -  [ [D] Chains and Agents ](https://www.reddit.com/r/MachineLearning/comments/16d7ee6/d_chains_and_agents/) , 2023-10-04-0909
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

     
 
MachineLearning -  [ [P] FalkorDB - a fast Graph Database - Knowledge Graph as RAG ](https://www.reddit.com/r/MachineLearning/comments/16cg6k7/p_falkordb_a_fast_graph_database_knowledge_graph/) , 2023-10-04-0909
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

     
 
deeplearning -  [ TheBloke/Llama-2-7b does not appear to have a file named pytorch_model.bin, tf_model.h5, model.ckpt  ](https://www.reddit.com/r/deeplearning/comments/16ihzn8/theblokellama27b_does_not_appear_to_have_a_file/) , 2023-10-04-0909
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

     
 
deeplearning -  [ How to find 'custom' datasets for LLM ](https://www.reddit.com/r/deeplearning/comments/16bj3hg/how_to_find_custom_datasets_for_llm/) , 2023-10-04-0909
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

     
