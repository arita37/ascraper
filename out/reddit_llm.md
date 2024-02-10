 
all -  [ Is there any framework to work with images, such as Langchain works for text? ](https://www.reddit.com/r/LangChain/comments/1amz9ht/is_there_any_framework_to_work_with_images_such/) , 2024-02-10-0909
```

```
---

     
 
all -  [ Data Access for LLMs is broken. Thoughts? ](https://www.reddit.com/r/LangChain/comments/1amy5yu/data_access_for_llms_is_broken_thoughts/) , 2024-02-10-0909
```
Hey  all. To build truly useful GenAI apps, LLMs need to be able to access  propriety data from structured and unstructu
red data sources. LLMs  struggle to understand the availability, location, and methods to  retrieve relevant data.

Key 
problems:

1. LLMs can’t identify if the necessary data is available to answer a user query in any of the data sources.

2. If the data is available, LLMs can’t locate which data source to retrieve from.
3. If  the source is known, writing r
etrieval pipelines  (text-to-SQL, text-to-Cypher, text-to-JSON, etc.) for the numerous retrieval protocols is complicate
d, repetitive, and non-deterministic.

Some suggest fine-tuning or RAG as potential solutions but:

1. Fine-tuning  mode
ls with specific data is expensive, becomes outdated with the  latest data, and has in-built access control issues. Cont
inuous  retraining is costly and doesn’t keep pace with real-time data changes.
2. RAG  doesn’t work with structured dat
a. Most useful data is structured and  can be spread across numerous data sources, each with its own querying  mechanism
.
3. Writing individual retrieval pipelines are limited and complicated and don’t ensure determinism, security, and acce
ss control.

Have  you faced these issues in your projects? What workarounds or solutions  have you found effective? Any
 new tools or practices that simplify  integrating LLMs with diverse data sources?
```
---

     
 
all -  [ Self query question ](https://www.reddit.com/r/LangChain/comments/1amxvpd/self_query_question/) , 2024-02-10-0909
```
I’ve been reading through everything i can find regarding self query (and also tinkering with it myself), and from what 
i can tell, i am required to use vectorStore. 

Am i misunderstanding the purpose or capabilities of the self query? 

I
d rather not update all my documents every time i query using the metadata as a filter. That strikes me as a waste of em
bedding and speed.

I’m hoping someone here can point to a misunderstanding i’m having, because i’m stumped at the momen
t. The only way i’ve been successful in using this is following it exactly as the documentation shows.

For reference, i
m using pinecone/js, here’s the documentation: 

https://js.langchain.com/docs/modules/data_connection/retrievers/self_q
uery/pinecone-self-query
```
---

     
 
all -  [ How do I store the message output in a .txt in langchain? (not as Json) ](https://www.reddit.com/r/LangChain/comments/1amvuc2/how_do_i_store_the_message_output_in_a_txt_in/) , 2024-02-10-0909
```
Does Langchain have any specific module? I am using Flowise gui with langchain and try to store message output in a txt,
 not the whole conversation, only the replies from the web api.
```
---

     
 
all -  [ Getting access to all the previous AgentActions in a tool. ](https://www.reddit.com/r/LangChain/comments/1amuf4y/getting_access_to_all_the_previous_agentactions/) , 2024-02-10-0909
```
Let's say I have a summarization tool that is supposed to summarize the output from different previous tools (like Wikip
edia, Google Search whatever) and I want to get the results from all the previous tools in this tool. How do I get this?

```
---

     
 
all -  [ SENIOR ML Engineer - 100% Remote (+ every other friday off!) ](https://www.reddit.com/r/MachineLearningJobs/comments/1amn92z/senior_ml_engineer_100_remote_every_other_friday/) , 2024-02-10-0909
```
APPLY HERE: [https://grnh.se/50c178c17us](https://grnh.se/50c178c17us)

Our Machine Learning teams build with the latest
 tools and launch for Silicon Valley startups and Life Science giants alike.

Join our team to work remotely, ship proje
cts you’re proud be a part of, and enjoy every other Friday off (yes, we really take it 😎)

**The Role:**

* Understand 
business objectives and develop models that help achieve them, along with metrics to track their progress
* Design and i
mplement complex ML systems using classical ML, DL and Foundation Models by following best practices
* Lead client commu
nications gathering requirements, managing expectations, and communicating deliverables
* Wrangle, explore and visualize
 data with a careful eye for issues that require data cleaning as well as differences in data distribution that may affe
ct performance when deploying the model in the real world
* Analyze the errors of the model and design strategies to ove
rcome them
* Deploy, maintain, and upgrade ML models and pipelines.

**The Benefits:**

* Every other Friday off (26 ext
ra days off a year)
* LokaLabs™ incubator
* Relocation & Explore program (3 months or full relo)
* Remote and flexible
*
 Paid sick days and local holidays
* Fitness subscriptions and more

**Main Requirements**:

* Bachelor’s Degree in Comp
uter Science or related
* 4+ years of experience with Python, ML libraries and AI/ML frameworks (PyTorch, HuggingFace, T
ensorFlow, Keras, Scikit-learn, Spark etc.)
* Strong understanding of statistical, ML and deep learning algorithms (cand
idates with NLP experience preferred)
* Experience building GenAI solutions, namely prompt engineering (e.g: Langchain),
 fine-tuning and serving LLMs, search and embeddings, etc.
* Experience with MLOps, favorably in AWS (e.g: Sagemaker) as
 well as standards tools (e.g: MLFlow)
* Experience visualizing and manipulating big datasets
* Ambition to learn and gr
ow into different industries with a modern tech stack
* Autonomy, adaptability and positivity (fully remote and globally
 distributed team)
* Proficient in English
```
---

     
 
all -  [ Text-to-SQL with extremely complex schema ](https://www.reddit.com/r/LangChain/comments/1amlftk/texttosql_with_extremely_complex_schema/) , 2024-02-10-0909
```
I am developing a text-to-sql project with llms  and sql server. where user will ask question in natural language and ll
ms will wrtie sql query, run it on my database and then give me result in natural language. The problem is schema of dat
abase is huge and tables names,column names are not self explanatory. Most of the times two tables need to joined on mor
e than one column and in where condition I consistanly want to have some conditions and daterange condition is extremely
 important as well because without date condition, the user might get data that he's not expected to have access to. is 
there any way to solve this problem? I have tried using views but that is computationally expensive and takes a lot of t
ime to execute as well. is there any other way?  
```
---

     
 
all -  [ How to tackle token limit issue with RAG ](https://www.reddit.com/r/LangChain/comments/1amktb2/how_to_tackle_token_limit_issue_with_rag/) , 2024-02-10-0909
```
I am running a RAG with GPT 3.5 Turbo Instruct. But since the context is large it is having issues with the token limit.
 How to deal with this?
```
---

     
 
all -  [ RAG does not stop Hallucinations ](https://www.reddit.com/r/LangChain/comments/1amjc9g/rag_does_not_stop_hallucinations/) , 2024-02-10-0909
```
Hi,

I have a RAG app but noticed that the RAG Method does not really stop hallucinations. So I wanted to discuss which 
prompts or techniques you are using so that your LLM is not hallucinating?

&#x200B;

Here is one Prompt of mine:mixtral
\_prompt = '''

<s> \[INST\] You are RagBot, a helpful assistant. Answer only in German. Use the following context infor
mation to answer the user's question briefly and concisely at the end. The contextual information comes from a vector se
arch, which means that not everything in the context is necessarily relevant. If the user gives you an instruction, foll
ow it (e.g. write the points in a continuous text). If you don't know the answer, just say you don't know. Don't make up
 an answer! It is important that you also do not add points to your answer that are not included in the context. If the 
user asks general questions, make small talk with them. Also make sure that you do not repeat your answer at the end!

&
#x200B;

\###Context to the question###:

{context}

&#x200B;

&#x200B;

\###Question of the user###:

{question}

&#x20
0B;

&#x200B;

Answer: \[/INST\]

'''

&#x200B;

Here are my model settings:

    llm = LlamaCpp(
    max_tokens = 1200,

    n_threads = 8
    model_path=model_path,
    temperature=0.01,
    f16_kv=True,
    n_ctx=28000,
    n_gpu_layers=1
,
    n_batch=512,
    callback_manager=callback_manager,
    verbose=True, # Verbose is required to pass to the callbac
k manager
    top_p= 0.95,
    top_k=40,
    repeat_penalty = 1.2,
    streaming=True,
    model_kwargs={
    #'repetiti
on_penalty': 1.1,
    #'mirostat': 2,
    },
    )
```
---

     
 
all -  [ Two LLM models ](https://www.reddit.com/r/LangChain/comments/1amitx2/two_llm_models/) , 2024-02-10-0909
```
Hello!  
I am building an application which main point is to help users improve the code of loaded projects.  I've build
 some pandas-based tools as well as vdb retriever tool.   
I am wondering if I could use one model (gpt-3.5-\*) to execu
te the tools and the other (gpt-4) to answer the questions? Like, the goal is for gpt-3.5 to gather information related 
to usr input, and gpt-4 to provide answer based on results found by the former.   
Any help would be appreciated, thanks
! 
```
---

     
 
all -  [ Need help working with SQL And LangChain. ](https://www.reddit.com/r/LangChain/comments/1amdj3k/need_help_working_with_sql_and_langchain/) , 2024-02-10-0909
```
Hi,  
I want to use the database as a knowledge base but don't want LangChain to execute queries on the database because
 it seems unsafe. Is there any way to convert the SQL data and store it in vectorDB for efficient RAG?
```
---

     
 
all -  [ Consigli su CV ](https://www.reddit.com/r/ItaliaCareerAdvice/comments/1am87uk/consigli_su_cv/) , 2024-02-10-0909
```
Ciao ragazzi, al momento sto cercando lavoro come data scientist/AI specialist, e questo è il mio CV. Su 10 apply nell'u
ltimo mese, ho ricevuto solo due risposte, una positiva (fingers crossed per il colloquio mercoledì) e una negativa. Com
incio a pensare che ci sia qualcosa di sbagliato, ad esempio, forse mi sembra un po' troppo verboso, e un po' dispersivo
 forse? Avete consigli per migliorarlo? In più, il fatto che siano due pagine effettivamente forse non va bene. Conviene
 forse che io rimuova esperienze relativamente poco rilevanti?

Ve lo lascio anonimizzato qui. Immaginate che come titol
o della prima pagina ci sia Nome Cognome. Grazie!

https://preview.redd.it/g1wqyhwwtfhc1.png?width=805&format=png&auto=w
ebp&s=f0fd4d9fa1d2d82f79af93a54dbf90de5c22b72e

https://preview.redd.it/21qcciwwtfhc1.png?width=805&format=png&auto=webp
&s=31459881cc03968353f1aaf698082f4856486427
```
---

     
 
all -  [ Summarizing past messages in an RAG conversation - is it always recommended? ](https://www.reddit.com/r/LangChain/comments/1am5nsd/summarizing_past_messages_in_an_rag_conversation/) , 2024-02-10-0909
```
Is there a consensus in terms of the quality of the AI response, between keeping the chat history in the memory as is, o
r summarizing it using ConversationSummaryMemory? 

I understand that summarizing past messages will lead to fewer token
s being used, but does it also lead to a drop in the quality of the AI answer in an RAG model, considering that the summ
ary may not necessarily include all the facts of the past messages? 

Common sense would say that yes, that may lead to 
worse answers, but wondering how the community feels about this topic.
```
---

     
 
all -  [ Data Science and Machine Learning Books Recommendation Chatbot ](https://www.reddit.com/r/learndatascience/comments/1am2nxa/data_science_and_machine_learning_books/) , 2024-02-10-0909
```
  

Hi Redditors,

I would like to share with you all my latest project: Step by step tutorial on how to create a chatbo
t that recommends Data Science and Machine Learning Books using LLM (Large Language Models), langchain and Streamlit.

T
he chatbot is trained on sample conversations and a dataset of books on Data Science and Machine Learning. The chatbot i
s able to understand the user’s intent and extract relevant entities from the user’s message.

It then uses this informa
tion to search for the best matching book in the dataset and recommends it to the user. The chatbot is also able to hand
le out-of-scope queries gracefully.

* You can find the step by step guide [here](https://medium.com/data-and-beyond/dat
a-science-and-machine-learning-books-recommendation-chatbot-83757cbb92f7)
* Link to the demo on Hugging Face Spaces is [
here](https://huggingface.co/spaces/Marce82/ML-DataScience-Books-Recomender-chatbot)
* Github repo [here](https://github
.com/marcello-calabrese/Machine-Learning-and-Data-Science-Books-recommender-Chatbot)

Happy to hear your comments, feedb
ack.

Cheers

# 
```
---

     
 
all -  [ Data Science and Machine Learning Books Recommendation Chatbot ](https://www.reddit.com/r/learnmachinelearning/comments/1am2mi4/data_science_and_machine_learning_books/) , 2024-02-10-0909
```
Hi Redditors,

I would like to share with you all my latest project: Step by step tutorial on how to create a chatbot th
at recommends Data Science and Machine Learning Books using LLM (Large Language Models), langchain and Streamlit.

The c
hatbot is trained on sample conversations and a dataset of books on Data Science and Machine Learning. The chatbot is ab
le to understand the user’s intent and extract relevant entities from the user’s message.

It then uses this information
 to search for the best matching book in the dataset and recommends it to the user. The chatbot is also able to handle o
ut-of-scope queries gracefully.

* You can find the step by step guide [here](https://medium.com/data-and-beyond/data-sc
ience-and-machine-learning-books-recommendation-chatbot-83757cbb92f7)
* Link to the demo on Hugging Face Spaces is [here
](https://huggingface.co/spaces/Marce82/ML-DataScience-Books-Recomender-chatbot)
* Github repo [here](https://github.com
/marcello-calabrese/Machine-Learning-and-Data-Science-Books-recommender-Chatbot)

Happy to hear your comments, feedback.


Cheers
```
---

     
 
all -  [ Data Science and Machine Learning Books Recommendation Chatbot Project ](https://www.reddit.com/r/datascienceproject/comments/1am2l84/data_science_and_machine_learning_books/) , 2024-02-10-0909
```
Hi Redditors, 

&#x200B;

I would like to share with you all my latest project:  Step by step tutorial on how to create 
a chatbot that recommends Data Science and Machine Learning Books using LLM (Large Language Models), langchain and Strea
mlit. 

The chatbot is trained on sample conversations and a dataset of books on Data Science and Machine Learning. The 
chatbot is able to understand the user’s intent and extract relevant entities from the user’s message.

It then uses thi
s information to search for the best matching book in the dataset and recommends it to the user. The chatbot is also abl
e to handle out-of-scope queries gracefully.

&#x200B;

* You can find the step by step guide [here](https://medium.com/
data-and-beyond/data-science-and-machine-learning-books-recommendation-chatbot-83757cbb92f7)
*  Link to the demo on Hugg
ing Face Spaces is [here](https://huggingface.co/spaces/Marce82/ML-DataScience-Books-Recomender-chatbot)
* Github repo [
here](https://github.com/marcello-calabrese/Machine-Learning-and-Data-Science-Books-recommender-Chatbot)

Happy to hear 
your comments, feedback.

&#x200B;

Cheers
```
---

     
 
all -  [ review of 10 ways to run LLMs locally ](https://www.reddit.com/r/LocalLLaMA/comments/1am0p48/review_of_10_ways_to_run_llms_locally/) , 2024-02-10-0909
```
Hey LocalLLaMA,

\[EDIT\] - thanks for all the awesome additions and feedback everyone! I'm going to go through them, tr
y them out, and add them to my blog post. It's gonna take some time though since I need to try them first, and maybe cha
nge my conclusions a bit.

I reviewed [ten different ways to run LLMs locally](https://matilabs.ai/2024/02/07/10-ways-to
-run-llms-locally-and-which-one-works-best-for-you/), and compared the different tools. Many of the tools had been share
d right here on this sub. Here are the tools I tried:

&#x200B;

1. Ollama
2. 🤗 Transformers
3. Langchain
4. llama.cpp
5
. GPT4All
6. LM Studio
7. jan.ai
8. llm ([https://llm.datasette.io/en/stable/](https://llm.datasette.io/en/stable/) \- l
ink if hard to google)
9. h2oGPT
10. localllm

My quick conclusions:

* If you are looking to develop an AI application,
 and you have a Mac or Linux machine, **Ollama** is great because it's very easy to set up, easy to work with, and fast.

* If you are looking to chat locally with documents, **GPT4All** is the best out of the box solution that is also easy 
to set up
* If you are looking for advanced control and insight into neural networks and machine learning, as well as th
e widest range of model support, you should try **transformers**
* In terms of speed, I think **Ollama** or **llama.cpp*
* are both very fast
* If you are looking to work with a CLI tool, **llm** is clean and easy to set up
* If you want to 
use Google Cloud, you should look into **localllm**

I found that different tools are intended for different purposes, s
o I summarized how they differ into a table:

&#x200B;

[Comparison of Local LLM Tools](https://preview.redd.it/9mqaz6me
9ehc1.png?width=2048&format=png&auto=webp&s=77ac88be51e473862c70625d2d62cfd13eeb6eb0)

I'd love to hear what the communi
ty thinks. How many of these have you tried, and which ones do you like? Are there more I should add?

Thanks!
```
---

     
 
all -  [ [Student] 200+ applications, very few OAs. International career switcher looking for feedback ](https://www.reddit.com/r/EngineeringResumes/comments/1alzrqb/student_200_applications_very_few_oas/) , 2024-02-10-0909
```
Hey everyone,

I'm an international career switcher looking to pivot into SWE. I've sent out hundreds of internship appl
ications, often with referrals, but I haven't had many responses.

Was hoping to get some feedback on my CV. Any feedbac
k would be appreciated!

&#x200B;

https://preview.redd.it/zoda85ch3ehc1.jpg?width=2546&format=pjpg&auto=webp&s=070b3e47
db7cb7b96a5891feae2477ef07c251f4
```
---

     
 
all -  [ I Made an Open-Source Pinecone DB AWS Construct 🏗️ ](https://www.reddit.com/r/LangChain/comments/1aly0xv/i_made_an_opensource_pinecone_db_aws_construct/) , 2024-02-10-0909
```
Managing Pinecone deployments is a thing of the past!!! 💃

🥇Some noteworthy features 🥇

1. Handles CRUDs for both Pod an
d Serverless Spec indexes
2. Deploy multiple indexes at the same time with isolated state management
3. Adheres to AWS-d
efined removal policies (DESTROY, SNAPSHOT, etc.)
4. Creates stack-scoped index names, to avoid name collisions 🙌

**It'
s still in beta, so feedback is more than welcome! 🫶**

[Github](https://github.com/petterle-endeavors/pinecone-db-const
ruct)  
[PyPi](https://pypi.org/project/pinecone-db-construct/)  
[NPM](https://www.npmjs.com/package/pinecone-db-constr
uct)
```
---

     
 
all -  [ RAG Accuracy ](https://www.reddit.com/r/LangChain/comments/1alus6s/rag_accuracy/) , 2024-02-10-0909
```
I am creating a RAG program where I used 20 pdfs which contains lease agreement of different tenants.

I am using langch
ain framework to work with FAISS and openAI Embeddings.

I am using  `text-embedding-ada-002` model because I think lang
chain currently does not support v3 embedding models. I get this error while using v3 models: `model not found. Using cl
100k_base encoding.`

Here's my process:

\- I read the directory containing pdfs (Some pdf are image based, some are te
xtual).

\- I use `from unstructured.partition.pdf import partition_pdf` to extract data based on title. Below id code b
lock:

    raw_pdf_elements = partition_pdf(filename=pdf_path,
                # Unstructured first finds embedded image
 blocks
                extract_images_in_pdf=True,
                #Use layout model (YOLOX) to get bounding boxes (for
 tables) and find titles
                # Titles are any sub-section of the document
                infer_table_struct
ure=True,
                
                # Post processing to aggregate text once we have the title
                ch
unking_strategy='by_title',
                
                # Chunking params to aggregate text blocks
                
# Attempt to create a new chunk 3800 chars
                # Attempt to keep chunks > 2000 chars
                max_cha
racters=4000,
                new_after_n_chars=3800,
                combine_text_under_n_chars=2000,
                i
mage_output_dir_path=path
                )

\- Then I create documents from the extracted text along with the tenant na
me in metadata (To get information from specific tenant's lease agreement when I mention it's name in the question). 1 p
df at a time.

\- After I get document chunks from all pdfs, I create list of all the chunks.

\- I create FAISS index f
or that data.

\- Then I perform QnA.

&#x200B;

The problem is the accuracy I get from this is very low. For most of th
e question, semantic search cannot even find relevant context.

I want to know if the accuracy of RAG is generally lower
 than the expectations or am I doing something wrong?

What process do you follow for better results?
```
---

     
 
all -  [ [D] WebVoyager: Navigating Digital Cosmos with LangGraph & Multimodal Models ](https://www.reddit.com/r/deeplearning/comments/1altlca/d_webvoyager_navigating_digital_cosmos_with/) , 2024-02-10-0909
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

     
 
all -  [ How to apply a metadata filter in Annoy by Spotify? ](https://www.reddit.com/r/LangChain/comments/1als4n1/how_to_apply_a_metadata_filter_in_annoy_by_spotify/) , 2024-02-10-0909
```
I am trying to filter the documents based on the metadata filter. However, I am not sure how to do it using the Langchai
n Annoy module.

I have a source in metadata, even though I applied the filter it is returning all the docs and not filt
ering them.

    # Load the vector db vectordb = Annoy.load_local(PERSIST_DIRECTORY, embeddings=embedding) 
    # Query 
Annoy docs = vectordb.similarity_search('how to do X?', k=2, filter={'source': 'news'})
```
---

     
 
all -  [ Create Custom Document Loader ](https://www.reddit.com/r/LangChain/comments/1alrd96/create_custom_document_loader/) , 2024-02-10-0909
```
Hi,

I want to create my own custom document loader, like the IMSDB one for example:

[https://github.com/langchain-ai/l
angchain/blob/00a09e1b7117f3bde14a44748510fcccc95f9de5/libs/community/langchain\_community/document\_loaders/imsdb.py#L8
](https://github.com/langchain-ai/langchain/blob/00a09e1b7117f3bde14a44748510fcccc95f9de5/libs/community/langchain_commu
nity/document_loaders/imsdb.py#L8)

The main reason I want to do this is to only extract the data I need from a web page
, and not the whole thing, to improve accuracy.

If I wrote a script like [imsdb.py](https://imsdb.py), how could I tell
 my Python script to use it? Maybe there's already a tutorial for this online? I couldn't find anytning from a quick sea
rch.

Thanks
```
---

     
 
all -  [ Langsmith prompts ](https://www.reddit.com/r/LangChain/comments/1alqrzy/langsmith_prompts/) , 2024-02-10-0909
```
Hey guys, so I've made a new chatPromptTemplate and once I did the first commit to it, I am unable to go back into the a
rtifact playground and modify the prompt. Which is weird cause I can edit my other prompts, for this specific prompt I g
et ' **Message 0 had extra kwargs: additional\_kwargs** ' when I hover over the playground button. Any help would be gre
at

&#x200B;

EDIT: just for reference the prompt im having issue with is  **thecodingbarista/documentgenerator** on the
 langsmith hub
```
---

     
 
all -  [ Help needed with vector database ](https://www.reddit.com/r/LangChain/comments/1alq3to/help_needed_with_vector_database/) , 2024-02-10-0909
```
Hello everyone,

I recently completed a project that involved using the FAISS vector database. I utilized lang-chain for
 storing embeddings in the vector database, which were generated from PDF files. For the purpose of the project, it was 
sufficient to store all the information without separating the storage according to users. 

What I want to know is - wh
en a user uploads a PDF, can I create an embedding for it and store it in the vector database, allowing me to query the 
embeddings for **that** user later on. This ensures that the generated output is accurate and privacy is also maintained
. I was wondering, can I do that? If so, how?

I really appreciate any help!
```
---

     
 
all -  [ How to use nemo-guardrails? how to know that is not policy violation and then to pass query to prima ](https://www.reddit.com/r/LangChain/comments/1alpm95/how_to_use_nemoguardrails_how_to_know_that_is_not/) , 2024-02-10-0909
```
My question is simple, I am not able to figure out, how to integrate nemo-guardrails in my current RAG applications with
out completely changing structure. It should return 0 or 1 based on whether user is query is valid or not. how can I get
 it to this?
```
---

     
 
all -  [ Extracting Table using PDFPlumber but not extracting Text that has background color ](https://www.reddit.com/r/LangChain/comments/1allnji/extracting_table_using_pdfplumber_but_not/) , 2024-02-10-0909
```
Hello, community,

In the section with a color background, the text is not extracting checked all parameters of main fun
ction for extracting text from the table in Python, pddplumber, unstructured. What recommendation do you have?

https://
preview.redd.it/2ofmdidh1ahc1.jpg?width=778&format=pjpg&auto=webp&s=bc6d1e50cfaeba5dd5e6ca9ce765eb4923973768
```
---

     
 
all -  [ Question about LLM output parsing ](https://www.reddit.com/r/LangChain/comments/1aljkdj/question_about_llm_output_parsing/) , 2024-02-10-0909
```
When generating code-related output from an LLM like python functions, sql queries, etc. a lot of times the LLM wraps th
e code between triple quotes like this:

    ```python
      blah
    ```

Is there an output parser or extractor compon
ent or anything that can help with extracting these segments and ignoring all the fluff around it?
```
---

     
 
all -  [ Opeansearch vector db use in rag ](https://www.reddit.com/r/LangChain/comments/1alilwn/opeansearch_vector_db_use_in_rag/) , 2024-02-10-0909
```
Hi All

Question, After creating my vector database of entire 100docs, i want  how to this vector database in seperate c
lient progran. How shall I do it? I using aws opensearch servless for vector db
```
---

     
 
all -  [ llama2 / mistral function calling? ](https://www.reddit.com/r/LocalLLaMA/comments/1alcjvq/llama2_mistral_function_calling/) , 2024-02-10-0909
```
Hello,

I've set up a llama2-7b as well as a llama2-13b with some faiss search and retrieval. 

My next step is to try a
nd recreate the function calling capabilities of chat gpt. 

What would be some ways of achieving that? Right now my bes
t option is to use langchain and chain together a model finetuned for function calling, and another one for synthesis.


Could you recommend something better?

Thanks!
```
---

     
 
all -  [ Recommendation system using LLMs ](https://www.reddit.com/r/generativeAI/comments/1al81nh/recommendation_system_using_llms/) , 2024-02-10-0909
```
Checkout how I developed a recommendation system using LangChain and LLMs https://youtu.be/WW0q8jjsisQ?si=9JI24AIj822N9z
JK
```
---

     
 
all -  [ Recommendation system using LangChain and RAG ](https://www.reddit.com/r/LangChain/comments/1al7yyt/recommendation_system_using_langchain_and_rag/) , 2024-02-10-0909
```
Checkout my new tutorial on how to build a recommendation system using RAG and LangChain https://youtu.be/WW0q8jjsisQ?si
=9JI24AIj822N9zJK
```
---

     
 
all -  [ Langchain expression language ](https://www.reddit.com/r/LangChain/comments/1al3xwz/langchain_expression_language/) , 2024-02-10-0909
```
Hi Guys,

Can anyone point me to a resource where we can choose different vector db retriever based on the input questio
n. There is an example on routing to different prompts using runnablelambda. However the input is a dictionary hence it 
works. My problem is to choose the retriever on run time then pass only the question to the selected retriever at runtim
e.
```
---

     
 
all -  [ LangChain for llm ](https://www.reddit.com/r/LangChain/comments/1al25wz/langchain_for_llm/) , 2024-02-10-0909
```
Hi guys, I have to create a llm based on risk analysis (mainly hara) for my company. The only problem is that the input 
data is sensitive that’s why I am steering in the direction of using a locally hosted/offline llm like private gpt or el
asticsearch with some kind of ui. Can anybody give me pointers on where to start and how to do it? I am still a student 
and fairly new to the topic
```
---

     
 
all -  [ Connect ConversationalRetrievalQAChain to LLMChain? ](https://www.reddit.com/r/flowise/comments/1al0wui/connect_conversationalretrievalqachain_to_llmchain/) , 2024-02-10-0909
```
Hey, 

I am trying to build a chatbot app that can act as different characters that has two layers of custom information
:

1) System Prompt  
2) Document Uploads to Pinecone

In the System Prompt, I would like to define the basic behavior a
pplicable for all characters, while each individual character personality is stored in Pinecone via character sheets upl
oaded. Character sheets are already saved in Pinecone.  


In Flowise I have built something like this:

https://preview
.redd.it/7fefzekif5hc1.png?width=2104&format=png&auto=webp&s=093696cc15b34fdd29b2381f59bcd35854a7fef3

So, in the left p
art, the System Prompt for Basic Behaviour is set up, leading into an LLMChain. In the right part, the document retrieva
l from Pinecone for the specific character behavior is set up.

&#x200B;

* Is this generally the right approach for wha
t I describe above?
* If yes, can anybody help how to connect the LLMChain and the ConversationalRetrievalQAChain togeth
er so I can run the chatbot processing both layers of information?

Thanks a lot!
```
---

     
 
all -  [ Multiple Documents ](https://www.reddit.com/r/LangChain/comments/1akzs8s/multiple_documents/) , 2024-02-10-0909
```
Hey guys, I was testing out things and I made a personal document analyser. I chunked and stored multiple documents in t
he same index in Pincone.
Since the documents have contextual overlap, this improved the quality of the results produced
 a lot.

For reference I was testing with the Mistral 8x7b model.

What's your opinion on this??
```
---

     
 
all -  [ Is there a existed way to mapping code files with real businesses? ](https://www.reddit.com/r/LangChain/comments/1akyazk/is_there_a_existed_way_to_mapping_code_files_with/) , 2024-02-10-0909
```
In the past few months, we've experimented with various approaches to enable LLM to comprehend code files. Currently, LL
M can grasp the essence of file meanings at a functional level. This understanding is facilitated by providing contextua
l information such as:

* File content
* File path
* Commit message
* Issues
* ...

However, the code represents busines
s logic, which often spans multiple/complex categories. This business logic may be entirely unrelated to the contents me
ntioned in a single code file, posing a significant challenge for LLM to comprehend and classify.

I'm wondering if ther
e are any existing methods or approaches to address this issue. Any insights or suggestions would be greatly appreciated
.  Thanks in advance :)
```
---

     
 
all -  [ Use Langchain Extraction with Bedrock ](https://www.reddit.com/r/aws/comments/1akw22w/use_langchain_extraction_with_bedrock/) , 2024-02-10-0909
```
Is it possible to use Langchain extraction with AWS Bedrock? It works with no issues with OpenAI.

Here is the documenta
tion: https://python.langchain.com/docs/use_cases/extraction

Basically take the following code and replace with Bedrock
:

from langchain.chains import create_extraction_chain
from langchain_openai import ChatOpenAI

# Schema
schema = {
   
 'properties': {
        'name': {'type': 'string'},
        'height': {'type': 'integer'},
        'hair_color': {'type
': 'string'},
    },
    'required': ['name', 'height'],
}

# Input
inp = '''Alex is 5 feet tall. Claudia is 1 feet tall
er Alex and jumps higher than him. Claudia is a brunette and Alex is blonde.'''

# Run chain
llm = ChatOpenAI(temperatur
e=0, model='gpt-3.5-turbo')
chain = create_extraction_chain(schema, llm)
chain.run(inp
```
---

     
 
all -  [ RAG using pinecone does not give accurate data ](https://www.reddit.com/r/LangChain/comments/1akvy3c/rag_using_pinecone_does_not_give_accurate_data/) , 2024-02-10-0909
```
I'm trying to build PDF chatbot using OpenAI, Langchain and Pinecone.

Here is my code,

    from langchain.document_loa
ders import PyPDFLoader
    from langchain.text_splitter import RecursiveCharacterTextSplitter, CharacterTextSplitter
  
  import uuid
    
    loader = PyPDFLoader('2104.02830.pdf')
    data = loader.load()
    
    text_splitter = Recursiv
eCharacterTextSplitter(
    chunk_size=2000, chunk_overlap=0)
    texts = text_splitter.split_documents(data)
    
    f
or text in texts:
    id = uuid.uuid4().hex
    response = embeddings.embed_query(text.page_content)
    vectors.append(
[(id, response, {'page': text.metadata['page'], 'text': text.page_content})])
    
    for vector in vectors:
    index.
upsert(vector)
    
    query_embedding = embeddings.embed_query('author of this research paper')
    
    result = inde
x.query(vector=query_embedding , top_k=5, include_metadata=True)
    
    print(result['matches'][0])
    
    [{'id': '
ccd0dac490da4b4b947db97076cdf10d',
      'metadata': {'page': 5.0,
                   'text': 'novel image dataset for b
enchmarking machine learning '         
               'al-\n''gorithms. ArXiv , abs/1708.07747, 2017.\n' '[20] X. Zou, 

                X. Kong, W. Wong, C. Wang, Y . Liu, and Y ''. Cao.\n''Fashionai: 
                A hierarchical datase
t for fashion ''understand-\n''ing. In 2019 
                IEEE/CVF Conference on Computer Vision ''and\n''Pattern 
  
              Recognition Workshops (CVPRW) , pages 296–304,\n''2019.\n''6'},
      'score': 0.290649086,
      'values'
: []},

&#x200B;

It gives me reference links rather than author names.
```
---

     
 
all -  [ Do you really need more than one agent in your LLM chatbot? ](https://www.reddit.com/r/LangChain/comments/1aktwzi/do_you_really_need_more_than_one_agent_in_your/) , 2024-02-10-0909
```
Hello, I have a project to build a chatbot for E-commerce. This chatbot should interact with users and inform them about
 the products sold on the website. I tried using one agent to handle both interaction and task execution. However, when 
I only said 'Hi,' the bot returned a ValueError, something like 'LLM could not parse.' So, in this situation, do I need 
two agents? One to interact with users for out-of-context questions such as greetings or asking the bot's name, and the 
other to handle the thinking process for tasks such as finding today's discounts or locating gaming accessories? 
```
---

     
 
all -  [ Multi Document RAG using Agents ](https://www.reddit.com/r/LangChain/comments/1akroee/multi_document_rag_using_agents/) , 2024-02-10-0909
```
Hey everyone,
I just released a tutorial on how to make an agent interact with multiple vector databases with examples a
nd codes. Do check it out

[https://youtu.be/cBpdiQ3gljM?si=rfpFmlyGILHlIH4t
](https://youtu.be/cBpdiQ3gljM?si=rfpFmlyGI
LHlIH4t)
```
---

     
 
all -  [ Looking for simple framework to deploy a langchain (with multi-user support and session management) ](https://www.reddit.com/r/LocalLLaMA/comments/1akioj6/looking_for_simple_framework_to_deploy_a/) , 2024-02-10-0909
```
So I have been learning langchain, LLM and so on.   


I have a basic chatbot that incorporates a vector store of compan
y codebase and chat history that is working fine on my computer for single-user purpose.   


The chain can be invoked w
ith repeated calls like  


response = chatbot.invoke(  
{'messages': 'Give me Python codes for xyz'},  
 config={  
 'c
onfigurable': {'user\_id': 'user\_id', 'conversation\_id': 'conversation\_id'}  
},  
)  


Or invoked through langserve
 like  


chatbot = RemoteRunnable('blahblah/invoke')

response = chatbot.invoke(  
{'messages': 'My message to chatbot'
},  
{'configurable': {'user\_id': 'dummy', 'conversation\_id': 'dummy'}},  
)  


But I would like to deploy this basic
 chain so my colleagues can test their prompts.   


I am looking for a simple solution (if there is one) that can achie
ve the following:  


1. Accessible online (can be just internal network)
2. Multi-user support with session management

3. Optional: UI like chatgpt or similar

  
So far, I am willing to go with langserve if I can just figure out how to po
st a request that includes all the necessary fields. I tried following the examples in langserve tutorials but no dice s
o far. 

&#x200B;
```
---

     
 
all -  [ LangChain's extensibility is 🤯 ](https://www.reddit.com/r/LangChain/comments/1akfdm7/langchains_extensibility_is/) , 2024-02-10-0909
```
Hi all,

I started exploring lang chain recently and was really amazed by its extensibility. I have written my experienc
e as small tutorials and wanted to share the same with the community.

[Meet Your Digital Dream Team: Revolutionizing th
e Tech World with AI ](https://micromastery.github.io/posts/meet-your-digital-dream-team-revolutionizing-tech-world-with
-ai/) \- This is where I explored a python framework called Crew AI which allows creating collaborative AI using langcha
in tools

[Enhancing LLMs with Custom Capabilities: A Guide to Langchain and Text-to-Speech ](https://micromastery.githu
b.io/posts/customizing-llms-with-langchain-text-to-speech/) \- This is where I explored creation of custom tools for lan
g chain. I am using this day to day for creating voiceovers for videos.

Hope you find these useful.

Thanks
```
---

     
 
all -  [ Splitting documents (pdfs/html pages/txt files) into snippets with logical flow with Opensource tool ](https://www.reddit.com/r/LangChain/comments/1akc06q/splitting_documents_pdfshtml_pagestxt_files_into/) , 2024-02-10-0909
```
I have specific usecase of extracting structured (logically split) information from documents. Is there any parser that 
is opensource and does not need any particular API key ?   
The snippets would be sent to a RAG. This data would be used
 for internal usecases, so I would prefer a solution that would work for the same.
```
---

     
 
MachineLearning -  [ [D] What's the best current RAG setup that would work with a local LLM? ](https://www.reddit.com/r/MachineLearning/comments/1ag6bo7/d_whats_the_best_current_rag_setup_that_would/) , 2024-02-10-0909
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

     
 
MachineLearning -  [ [P]: Anukool: My job hunting assistant ](https://www.reddit.com/r/MachineLearning/comments/1adu3tw/p_anukool_my_job_hunting_assistant/) , 2024-02-10-0909
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

     
 
MachineLearning -  [ New Data API for Astra [N] ](https://www.reddit.com/r/MachineLearning/comments/199uobn/new_data_api_for_astra_n/) , 2024-02-10-0909
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

     
 
MachineLearning -  [ [D] While using function calling or tools on openai or langchain, does openai have access to the dat ](https://www.reddit.com/r/MachineLearning/comments/199t8be/d_while_using_function_calling_or_tools_on_openai/) , 2024-02-10-0909
```
I am working on a client project and I am using langchain's tools and agents. I want to know if the data is getting pass
ed to openai or is it just like that - Output of one function is being directly passed to the second function with the k
nowledge of openai.
```
---

     
 
MachineLearning -  [ [D] Code vs JSON output for LLM agents? Frameworks like LangChain rely on LLMs responding with JSON  ](https://www.reddit.com/r/MachineLearning/comments/197f416/d_code_vs_json_output_for_llm_agents_frameworks/) , 2024-02-10-0909
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

     
 
deeplearning -  [ [D] Langchain Elevates with Step-Back Prompting using RAGatouille ](https://www.reddit.com/r/deeplearning/comments/1agtyeh/d_langchain_elevates_with_stepback_prompting/) , 2024-02-10-0909
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

     
 
deeplearning -  [ Become an AI Developer (Free 9 Part Series) ](https://www.reddit.com/r/deeplearning/comments/1afgp2r/become_an_ai_developer_free_9_part_series/) , 2024-02-10-0909
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

     
 
deeplearning -  [ DSPy Explained! ](https://www.reddit.com/r/deeplearning/comments/1adypks/dspy_explained/) , 2024-02-10-0909
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

     
