 
all -  [ RAG: Making multiple calls to LLMs ](https://www.reddit.com/r/LangChain/comments/1au5qnr/rag_making_multiple_calls_to_llms/) , 2024-02-19-0910
```
Let's consider a standard RAG (Retrieval-Augmented Generation) system. Suppose the prompt to an LLM says something like,
 'Don't make up stuff that is not presented in the text chunks below. If you didn't find information in the chunks below
, respond with 'NO ANSWER FOUND.'' One of the metrics that would serve as a good proxy to understand how well we find in
formation would be the hit rate, i.e., the fraction of user queries that were answered (not with 'NO ANSWER FOUND').

Co
nsider this strategy: if the answer from an LLM is 'NO ANSWER FOUND,' we make another call to an LLM but with some chang
es: we could use a different embedding model for semantic search, different chunking or re-ranker, or even a different L
LM. As a result of this, an LLM can return something on the second attempt, so the hit rate improves.

1. Is this a know
n technique in the context of RAG? Has anyone tried this? I've never heard anyone talking about it, although it seems so
 natural.
2. Does this sound reasonable? What could be the drawbacks of such a system? One is timing, but this could be 
solved with two (or more) parallel calls (although with more costs). What else though? More hallucinations? So far, I ca
n't say I see too many with this approach.
```
---

     
 
all -  [ [Python, LangChain, ChromaDB, Ollama] What's wrong with my RAG? ](https://www.reddit.com/r/LangChain/comments/1atx6ho/python_langchain_chromadb_ollama_whats_wrong_with/) , 2024-02-19-0910
```
Hey everyone, I'm fairly new to LLMs, but I have been playing with `ollama` this week, and love it. I am trying to achie
ve a 'chat with docs' functionality, and to use a ReStructuredText file as an input.

OS is Arch Linux, so I've installe
d `ollama` and `pandoc-cli`, created a python virtual env, and `pip` installed `langchain unstructured pypandoc gpt4all 
ollama chromadb`, then ran the following code:

    from langchain.llms import Ollama
    ollama = Ollama(base_url='http
://localhost:11434', model='mistral:7b-instruct-q3_K_M')
    # Load the data
    from langchain_community.document_loade
rs import UnstructuredRSTLoader
    loader = UnstructuredRSTLoader(file_path='/tmp/django/docs/ref/models/fields.txt', m
ode='elements')
    data = loader.load()
    # This errors out on Django Model Fields Reference RST file... so clean it 
up?
    from langchain_community.vectorstores.utils import filter_complex_metadata
    documents = filter_complex_metada
ta(data)

    # Split the docs into chunks
    from langchain.text_splitter import RecursiveCharacterTextSplitter
    sp
litter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=50)
    splits = splitter.split_documents(documen
ts) # not (data) as recommended

    # Convert split text into embeddings and store in the DB
    from langchain.embeddi
ngs import GPT4AllEmbeddings
    from langchain.vectorstores import Chroma
    store = Chroma.from_documents(documents=s
plits, embedding=GPT4AllEmbeddings())

    # Setup a QA Chain
    from langchain.chains import RetrievalQA
    chain = R
etrievalQA.from_chain_type(ollama, retriever=store.as_retriever())
    question = 'Generate a custom Django user model t
hat subclasses AbstractUser with `full_name` as a generated field.'
    response = chain.invoke({'query': question})
   
 print(response['result'])

I've tried it with different chunk sizes (from 500 to 1500), but it doesn't seem to take the
 file into consideration. I've tried different models, but they mostly say things like:

> To use Django's generated fie
ld, you need to understand that Django does not provide a built-in generated field. A 'generated field' typically refers
 to a field whose value is computed based on other fields in the model. It means creating a custom field by either subcl
assing an existing built-in field or writing a new Field from scratch.

[This is the file I am loading](https://github.c
om/django/django/blob/main/docs/ref/models/fields.txt#L1235), which clearly says that there's a new `GeneratedField` cla
ss in Django 5.0.

Does anyone know what I am doing wrong? Am I misunderstanding how RAG works in general? Is there a wa
y to make it smarter?

Thanks!
```
---

     
 
all -  [ What is a Chain???? ](https://www.reddit.com/r/LangChain/comments/1atqpjg/what_is_a_chain/) , 2024-02-19-0910
```
From my understanding, there are two types of chains.

1. chains that are instances of the RunnableSequence class - thes
e are the chains created using LCEL (the pipe operator)
2. chains that are instances of the Chain class - this is the de
precated version of chains before LCEL came out

Is my understanding correct? 
```
---

     
 
all -  [ How can I make a chain that includes a System Message, a Retriever and a Memory all at once? ](https://www.reddit.com/r/LangChain/comments/1atqdgn/how_can_i_make_a_chain_that_includes_a_system/) , 2024-02-19-0910
```
I have tried this approach: [https://github.com/langchain-ai/langchain/discussions/13514](https://github.com/langchain-a
i/langchain/discussions/13514)

but the result was not satisfactory because it makes the System Message be passed repeat
edly whenever I run the RAG.

I've used an agent, but the problem with agents is that it is extremely slow, so I need to
 know if there is a way to build a RAG that uses all of the features mentioned in the title, or if there is a way to mak
e the agent faster. here is my code:  


    executor = initialize_agent(
        agent=AgentType.OPENAI_FUNCTIONS,
    
    # the tools parameter includes the function RetrievalQA.from_chain_type, it is how I query the data from the vector 
database
        tools=tools,
        llm=llm,
        memory=memory,
        system_message=system_message,
        age
nt_kwargs={
            'system_message': system_message,
            'extra_prompt_messages': [MessagesPlaceholder(vari
able_name='memory')]
        },
        verbose=False,
        handle_parsing_errors=True
    )

&#x200B;

thanks in adv
ance.
```
---

     
 
all -  [ PdfReadError: EOF marker not found in HF spaces ](https://www.reddit.com/r/huggingface/comments/1atpi1m/pdfreaderror_eof_marker_not_found_in_hf_spaces/) , 2024-02-19-0910
```
I'm trying to train a LLM (with a streamlit UI)  on a PDF version of my resume, and locally, the model works fine.  when
 I upload to hugging face spaces, I get the EOF marker error and can't figure out how to resolve it.  

&#x200B;

&#x200
B;

`import streamlit as st`

`import requests`

`from PyPDF2 import PdfReader`

`from langchain.llms import OpenAI`

&#
x200B;

`from dotenv import load_dotenv`

`import os`

`import tempfile`

&#x200B;

`load_dotenv()  # take environment v
ariables from .env.`

&#x200B;

`## Function to load OpenAI model and get responses`

`def get_openai_response(question)
:`

`llm = OpenAI(`

`openai_api_key=os.getenv('OPENAI_API_KEY'),`

`model_name='gpt-3.5-turbo-instruct',`

`temperature
=0.5`

`)`

`response = llm(question)`

`return response`

&#x200B;

`# Function to extract text from a PDF file`

`def 
extract_text_from_pdf(file_path):`

`with open(file_path, 'rb') as file:`

`pdf = PdfReader(file)`

`text = ''`

`for pa
ge in pdf.pages:`

`text += page.extract_text()`

`return text`

&#x200B;

`st.set_page_config(page_title='Q&A Demo')`


&#x200B;

`pdf_file_url = 'my_filepath'`

`input_text = st.text_input('Input:', key='input')`

`submit = st.button('Gene
rate')`

&#x200B;

`if submit:`

`# Download the PDF file and save it locally`

`response = requests.get(pdf_file_url)`


`with tempfile.NamedTemporaryFile(delete=False) as temp_file:`

`temp_file.write(response.content)`

`pdf_file_path = t
emp_file.name`

&#x200B;

`if os.path.exists(pdf_file_path):`

`pdf_text = extract_text_from_pdf(pdf_file_path)`

`input
_text += '\n' + pdf_text`

`else:`

`st.write('Invalid PDF file path.')`

`st.stop()`

&#x200B;

`response = get_openai_
response(input_text)`

`st.subheader('The response is...')`

`st.write(response)`
```
---

     
 
all -  [ Add Live Stock Data to crewAI using LangChain custom tools and store res... ](https://youtube.com/watch?v=Q5GUFCpEng4&si=jtbDEXeatCwI1_Bh) , 2024-02-19-0910
```

```
---

     
 
all -  [ Need help with improving response accuracy. ](https://www.reddit.com/r/LangChain/comments/1atjz36/need_help_with_improving_response_accuracy/) , 2024-02-19-0910
```
Hello,

I’m a relative newcomer to LangChain and am building a RAG application to query a dataset of vendor work orders 
(PDF files). I followed the tutorials out there and successfully built the application, but I’m seeing some inaccurate r
esults. For example, I have a situation where we have multiple work orders with the same vendor and If I ask the app abo
ut some details regarding work order A (for example the cost of the work order), it returns information about work order
 B., i.e., I see “co-mingling” of information. The PDFs vary in size from 2 to 4 pages (not very big) and the details ar
e:

CHUNK\_SIZE=1000

CHUNK\_OVERLAP=200

K=4

FETCH\_K=8

**Try 1** – used Chroma as the persistence database and OpenA
I embeddings.

Didn’t get good results.

**Try 2** – used FAISS as the persistence database and HuggingFaceEmbeddings(mo
del\_name='intfloat/e5-base')

Read a post here that this combination might help improve accuracy, but results did not i
mprove.

**Try 3** – FAISS as the persistence database and OpenAI embeddings.

This is where I am currently, and still s
eeing inaccuracies in the response.

Any guidance as to how to resolve this? I read here that perhaps Knowledge Graphs m
ight help --- has anyone tried it for the situation (or similar situation) mentioned above and did it help? Will adding 
metadata help – I don’t have this right now.

Thank you.
```
---

     
 
all -  [ Trying to connect to MSSQL via Azure Entra ID in Python ](https://www.reddit.com/r/AZURE/comments/1atjnnh/trying_to_connect_to_mssql_via_azure_entra_id_in/) , 2024-02-19-0910
```
Hey all - ran into a bit of a roadblock here and was wondering if anyone has any insight they could share?

Going thru i
mplementation of SQL Agents to access structured data in my business and running into an issue authenticating to Azure S
QL databases using Azure Entra identities through python and langchain (using SQLAlchemy under the hood).

A number of d
ifferent connection string syntaxes have been tried based on what can be  found online, but I’m hoping someone has more 
information or knows the specific syntax using the ODBC 18 driver so one can access the database without a traditional d
b username + password.

In the meantime, trying to access the data with a user Azure identity, but in the future we will
 be using a service principal so if that connection would look differently I’d love to hear any ideas. Thank you!
```
---

     
 
all -  [ Local RAG solution using SQL DB instead of Vector DB ? ](https://www.reddit.com/r/LocalLLaMA/comments/1athi72/local_rag_solution_using_sql_db_instead_of_vector/) , 2024-02-19-0910
```
Hi everyone, long time lurker here and playing with local llms, autogen and crewAI since I got my 3090 few months ago :D
Even though I'm trying to stay up to date with all the possibilities, I feel quite overwhelmed and I'm reaching out to a
sk about a use case that I believe is quite common and can be useful for the whole community.

Context:

I created a Cha
tGPT custom GPT that has access to csv files, and an instruction containing the schema of the csv files and description 
of the data.The custom GPT is able to answer many questions by opening the csv files with pandas, querying the data then
 using the results to elaborate an answer.

Problem:

I would like to replicate a similar system using a self hosted LLM
 (ollama), that can use SQL to query multiple tables and use the result to generate an answer.So technically, this would
 just be a classic RAG app, but that relies in generating appropriate SQL, executing the query on a SQL database (ollama
 function calling?).

What is the most efficient way to implement a solution like this one today ?Should I use langchain
 ? or is there a higher level solution that already solves this use case ?

Thanks  


After some more research, I found
 this, that seems to be exactly what I'm looking for:  


[https://docs.llamaindex.ai/en/latest/examples/query\_engine/S
QLAutoVectorQueryEngine.html#](https://docs.llamaindex.ai/en/latest/examples/query_engine/SQLAutoVectorQueryEngine.html#
)
```
---

     
 
all -  [ MLflow LangChain version support ](https://www.reddit.com/r/LangChain/comments/1at94hd/mlflow_langchain_version_support/) , 2024-02-19-0910
```
Is there anywhere I can find which versions of LangChain are supported by which versions of MLflow?
```
---

     
 
all -  [ MLflow LangChain version support ](https://www.reddit.com/r/mlops/comments/1at93k1/mlflow_langchain_version_support/) , 2024-02-19-0910
```
Is there anywhere I can find the versions of LangChain that are supposed to be supported by each version of MLflow?
```
---

     
 
all -  [ Will there be any difference between (RAG) openAI and Google Gemini LLM responses if I use for both  ](https://www.reddit.com/r/LangChain/comments/1at5iyx/will_there_be_any_difference_between_rag_openai/) , 2024-02-19-0910
```
Let's say I care a lot about follow up questions and accurate results. Does everything depend on the vector dB embedding
s and not that much on the LLM?
```
---

     
 
all -  [ hi all, i am considering of creating a simple agent where i can import a csv and ask questions on it ](https://www.reddit.com/r/GoogleGeminiAI/comments/1at0mby/hi_all_i_am_considering_of_creating_a_simple/) , 2024-02-19-0910
```
This is possible by using openAI libraries, langchain etc, easily, i have done that. The thing is that it doesn't look t
hat simple on gemini. My understanding is that i have to create a project, an agent, a knowledge base, intents and then 
some more integrations.  


Is gemini any good in retrieval from structured data? Did anyone try it yet?  
Thanks!
```
---

     
 
all -  [ Updated Integration Guide: Supabase SSR Auth with Next.js 14, MUI Styling, and Enhanced Chat Applica ](https://www.reddit.com/r/LangChain/comments/1ast1wa/updated_integration_guide_supabase_ssr_auth_with/) , 2024-02-19-0910
```
Hello everyone,

In an effort to simplify and enhance web development practices, I've updated my project that initially 
showcased the integration of Supabase's server-side rendering (SSR) authentication with Next.js 14, complemented by Mate
rial-UI (MUI) for styling. This project serves as a basic yet comprehensive guide for those interested in implementing S
upabase authentication within a Next.js environment, with a strong emphasis on simplicity and practical application.

**
Key Aspects:**

* **Supabase for Authentication:** Utilizing Supabase's robust authentication system to secure your web 
application.
* **Server-Side Rendering with Next.js 14:** Leveraging Next.js 14 for improved performance and SEO benefit
s through server-side rendering.
* **Material-UI for Styling:** Applying Material-UI to enhance the UI with a modern, re
sponsive design.

**Getting Started:**

The repository is a one-stop resource, detailing every step from initial setup t
o final deployment:

* **Setup:** Instructions on establishing a Supabase account and initializing a Next.js project.
* 
**Installation:** Comprehensive guidance on installing necessary dependencies and configuring your development environme
nt.
* **Configuration:** Steps to configure your database and set up environment variables for seamless project integrat
ion.

**Purpose of the Project:**

This project aims to offer a straightforward example of how to integrate Supabase's a
uthentication with the server-side rendering capabilities of Next.js, adorned with Material-UI for styling. It's designe
d as an accessible starting point for anyone curious about these technologies.

**Expanded Features:**

Building upon th
is foundation, I've now integrated a chat application utilizing LangChain and OpenAI's ChatGPT model, with Redis (via Up
stash) for efficient conversation storage. This addition showcases the practical use of AI in real-time applications, em
phasizing:

* **AI Integration:** Leveraging AI capabilities from Vercel and LangChain for dynamic, intelligent chat fun
ctionalities.
* **Redis for Chat History:** Using Upstash/Redis for reliable and efficient chat storage, ensuring conver
sations are seamlessly managed and retrieved.
* **Enhanced Markdown Support:** Incorporating Perplexity with React Markd
own for enriched text presentation, including code highlight support through `rehype-highlight` and styling with `highli
ght.js/styles/github-dark.css`.
* **Optimization with React Server Components:** Utilizing React's server components and
 server actions for optimized data fetching and component rendering, aligning with Next.js's latest features for a strea
mlined user experience.

**Looking for Feedback:**

Your insights and contributions are invaluable. Whether it's suggest
ions to further simplify the integration, or feedback on the newly added chat application features, I welcome all forms 
of constructive critique. This project is not just a demonstration but a platform for collaboration and learning.

Explo
re the project on GitHub at: GitHub - SupabaseAuthWithSSR and share your thoughts or questions. Let's make web developme
nt simpler and more accessible together.

&#x200B;

[https://github.com/ElectricCodeGuy/SupabaseAuthWithSSR](https://git
hub.com/ElectricCodeGuy/SupabaseAuthWithSSR)
```
---

     
 
all -  [ Updated Integration Guide: Supabase SSR Auth with Next.js 14, MUI Styling, and Enhanced Chat Applica ](https://www.reddit.com/r/Supabase/comments/1assyt6/updated_integration_guide_supabase_ssr_auth_with/) , 2024-02-19-0910
```
Hello everyone,

In an effort to simplify and enhance web development practices, I've updated my project that initially 
showcased the integration of Supabase's server-side rendering (SSR) authentication with Next.js 14, complemented by Mate
rial-UI (MUI) for styling. This project serves as a basic yet comprehensive guide for those interested in implementing S
upabase authentication within a Next.js environment, with a strong emphasis on simplicity and practical application.

**
Key Aspects:**

* **Supabase for Authentication:** Utilizing Supabase's robust authentication system to secure your web 
application.
* **Server-Side Rendering with Next.js 14:** Leveraging Next.js 14 for improved performance and SEO benefit
s through server-side rendering.
* **Material-UI for Styling:** Applying Material-UI to enhance the UI with a modern, re
sponsive design.

**Getting Started:**

The repository is a one-stop resource, detailing every step from initial setup t
o final deployment:

* **Setup:** Instructions on establishing a Supabase account and initializing a Next.js project.
* 
**Installation:** Comprehensive guidance on installing necessary dependencies and configuring your development environme
nt.
* **Configuration:** Steps to configure your database and set up environment variables for seamless project integrat
ion.

**Purpose of the Project:**

This project aims to offer a straightforward example of how to integrate Supabase's a
uthentication with the server-side rendering capabilities of Next.js, adorned with Material-UI for styling. It's designe
d as an accessible starting point for anyone curious about these technologies.

**Expanded Features:**

Building upon th
is foundation, I've now integrated a chat application utilizing LangChain and OpenAI's ChatGPT model, with Redis (via Up
stash) for efficient conversation storage. This addition showcases the practical use of AI in real-time applications, em
phasizing:

* **AI Integration:** Leveraging AI capabilities from Vercel and LangChain for dynamic, intelligent chat fun
ctionalities.
* **Redis for Chat History:** Using Upstash/Redis for reliable and efficient chat storage, ensuring conver
sations are seamlessly managed and retrieved.
* **Enhanced Markdown Support:** Incorporating Perplexity with React Markd
own for enriched text presentation, including code highlight support through `rehype-highlight` and styling with `highli
ght.js/styles/github-dark.css`.
* **Optimization with React Server Components:** Utilizing React's server components and
 server actions for optimized data fetching and component rendering, aligning with Next.js's latest features for a strea
mlined user experience.

**Looking for Feedback:**

Your insights and contributions are invaluable. Whether it's suggest
ions to further simplify the integration, or feedback on the newly added chat application features, I welcome all forms 
of constructive critique. This project is not just a demonstration but a platform for collaboration and learning.

Explo
re the project on GitHub at: GitHub - SupabaseAuthWithSSR and share your thoughts or questions. Let's make web developme
nt simpler and more accessible together.

  
[https://github.com/ElectricCodeGuy/SupabaseAuthWithSSR](https://github.com
/electriccodeguy/supabaseauthwithssr)
```
---

     
 
all -  [ Tool building tool? ](https://www.reddit.com/r/LangChain/comments/1asqdx3/tool_building_tool/) , 2024-02-19-0910
```
This might be a stupid question, but has anyone built a tool that builds tools and adds them to an agent's tool list?
```
---

     
 
all -  [ What's your take on LangGraph? ](https://www.reddit.com/r/LangChain/comments/1ashzgp/whats_your_take_on_langgraph/) , 2024-02-19-0910
```
Hi,

I wanted to hear some feedback on LangGraph from those who have used it or are just starting to look into it. Do yo
u feel like it is the right abstraction and simplifies development? What are your use cases for using it, as compared to
 LCEL or older chains?

Thanks!
```
---

     
 
all -  [ Finetuning or Rag for recommendation system with conversational chain LLM ](https://www.reddit.com/r/LangChain/comments/1asg3s9/finetuning_or_rag_for_recommendation_system_with/) , 2024-02-19-0910
```
Hi everyone, I would like to ask you for support for the LLM in E-commerce. I would like to create a Q&A chatbot with LL
M that on the basis of the dataset (table) recommends a certain type of product. Is there anything about this case study
?

I have a number of products with their characteristics, such as colour, size, fragrance, etc...  I would like to crea
te a kind of recommendation system using LLM. I have no output but only input. I was thinking of using RAG but I don't k
now if a table can be passed to the vector database or is there some kind of different approach.
```
---

     
 
all -  [ This week in AI - all the Major AI developments in a nutshell ](https://www.reddit.com/r/artificial/comments/1ase382/this_week_in_ai_all_the_major_ai_developments_in/) , 2024-02-19-0910
```
1. **Meta AI** introduces ***V-JEPA*** (Video Joint Embedding Predictive Architecture), a method for teaching machines t
o understand and model the physical world by watching videos. Meta AI releases a collection of V-JEPA vision models trai
ned with a feature prediction objective using self-supervised learning. The models are able to understand and predict wh
at is going on in a video, even with limited information \[[*Details*](https://ai.meta.com/blog/v-jepa-yann-lecun-ai-mod
el-video-joint-embedding-predictive-architecture/) | [*GitHub*](https://github.com/facebookresearch/jepa)\].
2. **Open A
I** introduces ***Sora***, a text-to-video model that can create videos of up to 60 seconds featuring highly detailed sc
enes, complex camera motion, and multiple characters with vibrant emotions \[[*Details + sample videos*](https://openai.
com/sora)[ ](https://openai.com/sora)| [*Report*](https://openai.com/research/video-generation-models-as-world-simulator
s)\].
3. **Google** announces their next-generation model, **Gemini 1.5,** that uses a new [Mixture-of-Experts](https://
arxiv.org/abs/1701.06538) (MoE) architecture. The first Gemini 1.5 model being released for early testing is ***Gemini 1
.5 Pro*** with a context window of up to 1 million tokens, which is the longest context window of any large-scale founda
tion model yet. 1.5 Pro can perform sophisticated understanding and reasoning tasks for different modalities, including 
video and it performs at a similar level to 1.0 Ultra \[[*Details*](https://blog.google/technology/ai/google-gemini-next
-generation-model-february-2024/#gemini-15) *|*[*Tech Report*](https://storage.googleapis.com/deepmind-media/gemini/gemi
ni_v1_5_report.pdf)\].
4. Reka introduced **Reka Flash,** a new 21B multimodal and multilingual model trained entirely f
rom scratch that is competitive with Gemini Pro & GPT 3.5 on key language & vision benchmarks. Reka also present a compa
ct variant Reka Edge , a smaller and more efficient model (7B) suitable for local and on-device deployment. Both models 
are in public beta and available in [**Reka Playground** ](https://chat.reka.ai/chat)\[[*Details*](https://reka.ai/reka-
flash-an-efficient-and-capable-multimodal-language-model)\].
5. **Cohere** For AI released ***Aya***, a new open-source,
 massively multilingual LLM & dataset to help support under-represented languages. Aya outperforms existing open-source 
models and covers 101 different languages – more than double covered by previous models \[[*Details*](https://cohere.com
/research/aya)\].
6. **BAAI** released ***Bunny***, a family of lightweight but powerful multimodal models. Bunny-3B mod
el built upon SigLIP and Phi-2 outperforms the state-of-the-art MLLMs, not only in comparison with models of similar siz
e but also against larger MLLMs (7B), and even achieves performance on par with LLaVA-13B \[[*Details*](https://github.c
om/BAAI-DCAI/Bunny)\].
7. **Amazon** introduced a text-to-speech (TTS) model called ***BASE TTS*** (Big Adaptive Streama
ble TTS with Emergent abilities). BASE TTS is the largest TTS model to-date, trained on 100K hours of public domain spee
ch data and exhibits “emergent” qualities improving its ability to speak even complex sentences naturally \[[*Details*](
https://techcrunch.com/2024/02/14/largest-text-to-speech-ai-model-yet-shows-emergent-abilities/) | [*Paper*](https://ass
ets.amazon.science/6e/82/1d037a4243c9a6cf4169895482d5/base-tts-lessons-from-building-a-billion-parameter-text-to-speech-
model-on-100k-hours-of-data.pdf)\].
8. **Stability AI** released ***Stable Cascade*** in research preview, a new text to
 image model that is exceptionally easy to train and finetune on consumer hardware due to its three-stage architecture. 
Stable Cascade can also generate image variations and image-to-image generations. In addition to providing checkpoints a
nd inference scripts, Stability AI has also released scripts for finetuning, ControlNet, and LoRA training \[[*Details*]
(https://stability.ai/news/introducing-stable-cascade)\].
9. **Researchers** from UC berkeley released ***Large World Mo
del (LWM)***, an open-source general-purpose large-context multimodal autoregressive model, trained from LLaMA-2, that c
an perform language, image, and video understanding and generation. LWM answers questions about 1 hour long YouTube vide
o even if GPT-4V and Gemini Pro both fail and can retriev facts across 1M context with high accuracy \[[*Details*](https
://largeworldmodel.github.io/)\].
10. **GitHub** opens applications for the next cohort of ***GitHub Accelerator program
*** with a focus on funding the people and projects that are building ***AI-based solutions*** under an open source lice
nse \[[*Details*](https://github.blog/2024-02-13-powering-advancements-of-ai-in-the-open-apply-now-to-github-accelerator
)\].
11. **NVIDIA** released ***Chat with RTX***, a locally running (Windows PCs with specific NVIDIA GPUs) AI assistant
 that integrates with your file system and lets you chat with your notes, documents, and videos using open source models
 \[[*Details*](https://www.nvidia.com/en-us/ai-on-rtx/chat-with-rtx-generative-ai)\].
12. **Open AI** is testing ***memo
ry with ChatGPT***, enabling it to remember things you discuss across all chats. ChatGPT's memories evolve with your int
eractions and aren't linked to specific conversations. It is being rolled out to a small portion of ChatGPT free and Plu
s users this week \[[*Details*](https://openai.com/blog/memory-and-new-controls-for-chatgpt)\].
13. **BCG X** released o
f ***AgentKit***, a LangChain-based starter kit (NextJS, FastAPI) to build constrained agent applications \[[*Details*](
https://blog.langchain.dev/bcg-x-releases-agentkit-a-full-stack-starter-kit-for-building-constrained-agents/) | [*GitHub
*](https://github.com/BCG-X-Official/agentkit)\].
14. **Elevenalabs**' Speech to Speech feature, launched in November, f
or voice transformation with control over emotions and delivery, is now ***multilingual*** and available in 29 languages
 \[[*Link*](https://elevenlabs.io/voice-changer)\]
15. **Apple** introduced ***Keyframer***, an LLM-powered animation pr
ototyping tool that can generate animations from static images (SVGs). Users can iterate on their design by adding promp
ts and editing LLM-generated CSS animation code or properties \[[*Paper*](https://arxiv.org/pdf/2402.06071.pdf)\].
16. *
*Eleven Labs** launched a ***payout program*** for voice actors to earn rewards every time their voice clone is used \[[
*Details*](https://elevenlabs.io/voice-actors)\].
17. **Azure OpenAI Service** announced Assistants API, new models for 
finetuning, new text-to-speech model and new generation of embeddings models with lower pricing \[[*Details*](https://te
chcommunity.microsoft.com/t5/ai-azure-ai-services-blog/azure-openai-service-announces-assistants-api-new-models-for/ba-p
/4049940)\].
18. **Brilliant Labs**, the developer of AI glasses, launched ***Frame***, the world’s first glasses featur
ing an integrated AI assistant, ***Noa***. Powered by an integrated multimodal generative AI system capable of running G
PT4, Stability AI, and the Whisper AI model simultaneously, Noa performs real-world visual processing, novel image gener
ation, and real-time speech recognition and translation. \[[*Details*](https://venturebeat.com/games/brilliant-labss-fra
me-glasses-serve-as-multimodal-ai-assistant/)\].
19. **Nous Research** released ***Nous Hermes 2 Llama-2 70B*** model tr
ained on the Nous Hermes 2 dataset, with over 1,000,000 entries of primarily synthetic data \[[*Details*](https://huggin
gface.co/NousResearch/Nous-Hermes-2-Llama-2-70B)\].
20. **Open AI** in partnership with Microsoft Threat Intelligence, h
ave disrupted five state-affiliated actors that sought to use AI services in support of malicious cyber activities \[[*D
etails*](https://openai.com/blog/disrupting-malicious-uses-of-ai-by-state-affiliated-threat-actors)\]
21. **Perplexity**
 partners with **Vercel**, opening AI search to developer apps \[[*Details*](https://venturebeat.com/ai/perplexity-partn
ers-with-vercel-opening-ai-search-to-developer-apps/)\].
22. **Researchers** show that ***LLM agents can autonomously ha
ck websites***, performing tasks as complex as blind database schema extraction and SQL injections without human feedbac
k. The agent does not need to know the vulnerability beforehand \[[*Paper*](https://arxiv.org/html/2402.06664v1)\].
23. 
**FCC** makes AI-generated voices in unsolicited robocalls illegal \[[*Link*](https://www.msn.com/en-us/money/companies/
fcc-bans-ai-voices-in-unsolicited-robocalls/ar-BB1hZoZ0)\].
24. **Slack** adds AI-powered search and summarization to th
e platform for enterprise plans \[[*Details*](https://techcrunch.com/2024/02/14/slack-brings-ai-fueled-search-and-summar
ization-to-the-platform/)\].

**Source**: AI Brews - you can subscribe the [newsletter here](https://aibrews.substack.co
m/). it's free to join, sent only once a week with bite-sized news, learning resources and selected tools. Thanks.
```
---

     
 
all -  [ [1 YoE] Looking for a second job after career switching ](https://www.reddit.com/r/EngineeringResumes/comments/1asdkz1/1_yoe_looking_for_a_second_job_after_career/) , 2024-02-19-0910
```
 Hello! I'd like some help in improving my resume, I've been using it for some months and haven't really noticed a big d
ifference when compared to the one I used before. I've been mostly applying for Python back-end jobs. I started working 
with Python daily in 2018, during my master's, and continued until 2023, when I managed to get an official software engi
neer trainee position (it is full time). Before doing this switch, I had been learning web development on my spare time,
 and at work on a daily/weekly basis I'd write code for data analysis/visualization.

I'd like some tips on how to impro
ve this resume, I'm thinking maybe it might be a bit confusing, I've had recruiters say they are looking for somewhere w
ith less experience and also recruiters saying they are looking for someone with more experience, so I feel like I'm in 
kind of a limbo. Right now I'm looking for a new job since I'm moving back to Brazil after living abroad, so I can't con
tinue in my current one.  


https://preview.redd.it/3hvevmulazic1.png?width=5100&format=png&auto=webp&s=0f6324a5f47b3ed
bd19bc2d67ed66bb6fccda05b
```
---

     
 
all -  [ How to create Chroma vector store asynchronously ](https://www.reddit.com/r/LangChain/comments/1as8gxt/how_to_create_chroma_vector_store_asynchronously/) , 2024-02-19-0910
```
Let me go straight to the point: is it possible to create a Chroma Vector Store asynchronously using OpenAIEmbeddings ? 
I think it is given that you can get the embeddings asynchronously from OpenAI API, but this call is happening internall
y in the Chroma class so not sure how to specify it.

Here you have my current code at the moment.

    loader = CSVLoad
er(file_path=path_to_file)
    inventory = Chroma.from_documents(loader.load(), OpenAIEmbeddings(), persist_directory=pa
th_to_file)
```
---

     
 
all -  [ RAG explained with diagram ](https://www.reddit.com/r/LangChain/comments/1as7g55/rag_explained_with_diagram/) , 2024-02-19-0910
```
Hey everyone, checkout this easy explanation of how RAG works internally https://youtu.be/sfgq-lfC2vw?si=ALIOQ5kIZeRxwqt
v
```
---

     
 
all -  [ Challenges in Tool Selection for Multi-Tool Agents with Langchain ](https://www.reddit.com/r/LangChain/comments/1as71vq/challenges_in_tool_selection_for_multitool_agents/) , 2024-02-19-0910
```
I developed a multi-tool agent with langchain. However, the agent struggles to select suitable tools for the task consis
tently. It occasionally picks the right tool but often chooses incorrectly. Given the abundance of tools being developed
 nowadays, I conducted research but only found refining the tool descriptions as a potential solution. I made efforts to
 use the most accurate tool descriptions available. Is there something I am overlooking that others might be doing to cr
eate successful agents? I cannot ensure the actions of the agents.
```
---

     
 
all -  [ How to handle duplicate documents in vector DB ](https://www.reddit.com/r/LangChain/comments/1as2ox1/how_to_handle_duplicate_documents_in_vector_db/) , 2024-02-19-0910
```
I'm using MongoDB as a vector store for vectors created for PDFs, how to handle the duplicate upload of the same documen
t?
```
---

     
 
all -  [ OpenAI API access for learning LangChain. ](https://www.reddit.com/r/LangChain/comments/1as1ybk/openai_api_access_for_learning_langchain/) , 2024-02-19-0910
```
Hello all,   
I'm very new to LLM's and recently came across LangChain on YT and Twitter. I am learning about LangChain 
but I need to have OpenAI access for GPT models, I can't afford to buy the credits for the API. So is there any solution
 to this? I just want any LLM not just OpenAI which can help me understand how I can leverage LangChain to build the app
lications. 

Thank you.
```
---

     
 
all -  [ PineconeIndex RecordMetadata type problem using imports from '@pinecone-database/pinecone'; and '@la ](https://www.reddit.com/r/LangChain/comments/1aryuy5/pineconeindex_recordmetadata_type_problem_using/) , 2024-02-19-0910
```
Im having trouble with index type using:  
 

import { Pinecone } from '@pinecone-database/pinecone';  
import { Pinecon
eStore } from '@langchain/pinecone';  


 

I have been trying to incorporate vector store containing OpenAIEmbeddings i
ndexed on pinecone. But i keep getting type error, no matter what i do.

At **{ pineconeIndex }**, in this line:

    co
nst vectorStore = await PineconeStore.fromExistingIndex(   new OpenAIEmbeddings({ openAIApiKey: process.env.OPENAI_API_K
EY }),   { pineconeIndex } );  

**Error: vectorstores.d.ts(11, 5): The expected type comes from property 'pineconeIndex
' which is declared here on type 'PineconeStoreParams'**

My Imports:

import { Redis } from '@upstash/redis';  
import 
{ OpenAIEmbeddings } from '@langchain/openai';  
import { Pinecone, Index, RecordMetadata } from '@pinecone-database/pin
econe';  
import { PineconeStore } from '@langchain/pinecone';

**Whole code:**

import { Redis } from '@upstash/redis';
  
import { OpenAIEmbeddings } from '@langchain/openai';  
import { Pinecone, Index, RecordMetadata } from '@pinecone-da
tabase/pinecone';  
import { PineconeStore } from '@langchain/pinecone';

export type CompanionKey = {  
companionName: 
string;  
modelName: string;  
userId: string;  
};

export class MemoryManager {  
private static instance: MemoryManag
er;  
private history: Redis;  
private vectorDBClient: Pinecone;

public constructor() {  
this.history = Redis.fromEnv
();  
this.vectorDBClient = new Pinecone({  
apiKey: process.env.PINECONE\_API\_KEY!,  
environment: process.env.PINECON
E\_ENVIRONMENT!,  
});  
}

public async vectorSearch(  
recentChatHistory: string,  
companionFileName: string  
) {  

const pineconeClient = this.vectorDBClient;

    const pineconeIndex = pineconeClient.Index(     process.env.PINECONE_IN
DEX || ('' as string) ) as Index<RecordMetadata>;      const vectorStore = await PineconeStore.fromExistingIndex(   new 
OpenAIEmbeddings({ openAIApiKey: process.env.OPENAI_API_KEY }),   { pineconeIndex } );   const similarDocs = await vecto
rStore   .similaritySearch(recentChatHistory, 3, { fileName: companionFileName })   .catch((err) => {     console.log('W
ARNING: failed to get vector search results.', err);   }); return similarDocs; 

}

public static async getInstance(): P
romise {  
if (!MemoryManager.instance) {  
MemoryManager.instance = new MemoryManager();

    } return MemoryManager.in
stance; 

}

private generateRedisCompanionKey(companionKey: CompanionKey): string {  
return ${companionKey.companionNa
me}-${companionKey.modelName}-${companionKey.userId}  
;  
}

public async writeToHistory(text: string, companionKey: Co
mpanionKey) {  
if (!companionKey || typeof companionKey.userId == 'undefined') {  
console.log('Companion key set incor
rectly');  
return '';  
}

    const key = this.generateRedisCompanionKey(companionKey); const result = await this.hist
ory.zadd(key, {   score: Date.now(),   member: text, });  return result; 

}

public async readLatestHistory(companionKe
y: CompanionKey): Promise {  
if (!companionKey || typeof companionKey.userId == 'undefined') {  
console.log('Companion
 key set incorrectly');  
return '';  
}

    const key = this.generateRedisCompanionKey(companionKey); let result = awa
it this.history.zrange(key, 0, Date.now(), {   byScore: true, });  result = result.slice(-30).reverse(); const recentCha
ts = result.reverse().join('\n'); return recentChats; 

}

public async seedChatHistory(  
seedContent: String,  
delimi
ter: string = '\\n',  
companionKey: CompanionKey  
) {  
const key = this.generateRedisCompanionKey(companionKey);  
if
 (await this.history.exists(key)) {  
console.log('User already has chat history');  
return;  
}

    const content = s
eedContent.split(delimiter); let counter = 0; for (const line of content) {   await this.history.zadd(key, { score: coun
ter, member: line });   counter += 1; } 

}  
}
```
---

     
 
all -  [ OS plugin framework for AI actions, available as LangChain Toolkit and on OpenGPTs ](https://www.reddit.com/r/LangChain/comments/1ars2t0/os_plugin_framework_for_ai_actions_available_as/) , 2024-02-19-0910
```
We have created an open source framework to create and run AI actions to connect LLM-apps with the real world. Infrastru
cture, control and AI safety.

See use case and more [details here on the LangChain blog](https://blog.langchain.dev/mee
t-connery-an-open-source-plugin-infrastructure-for-opengpts-and-llm-apps/).

[GitHub repo and links to docs here](https:
//github.com/connery-io/connery)

Would love to get your feedback.
```
---

     
 
all -  [ iA chatbot for Trello ? ](https://www.reddit.com/r/trello/comments/1arrn4j/ia_chatbot_for_trello/) , 2024-02-19-0910
```
Hi,
Is there someone who managed to create a functionnal IA chatbot for trello ?
I mean, a chatbot that will be capable 
of searching info in a board (title, description, comments, labels, custom fields...) ?
I saw Langchain framework has a 
Trello agent, but i struggle using it... And did not find a real tutorial.
I also tried uploading json and csv in ChatGP
T, but the answers were not great (maybe a bad embedding/indexation).
Thanks for your feedbacks 👍
```
---

     
 
all -  [ Defining LLM Project architecture ](https://www.reddit.com/r/LangChain/comments/1arrmts/defining_llm_project_architecture/) , 2024-02-19-0910
```
I’m developing a project based on LLMs: ideally a chat that can interact with different APIs. To interact with such APIs
, a JSON request must be formalized. Indeed, being a chat, memory is needed.

What is the best way to do so?

Currently,
 I have two approaches in mind

- A LLMRouter identifies one route per API + a default route. This works, but introducin
g memory is quite difficult as I’m using LangChain and I have to integrate multiple different LLMChains, Few-shot-templa
tes, memory, and routing
- An agent with memory that has one tool per API plus a default chat. The tools, having to tran
slate the prompt to a JSON, would be simply LLMs in few shot settings
```
---

     
 
all -  [ Suggest Most optimal RAG pipeline for insurance support chatbot. ](https://www.reddit.com/r/LangChain/comments/1arraqh/suggest_most_optimal_rag_pipeline_for_insurance/) , 2024-02-19-0910
```
I am tasked to build AI RAG chatbot for health insurance company.

Please suggest optimal RAG pipeline,  
better tools a
nd tech stack for low latency and accuracy of the answers?

Thanks in advance.
```
---

     
 
all -  [ Retrieving output that exceeds context length after parsing? ](https://www.reddit.com/r/LangChain/comments/1arqpqp/retrieving_output_that_exceeds_context_length/) , 2024-02-19-0910
```
Basically the scenario is I load up a large pdf file which gets processed with the document parser and text splitter whi
ch then is passed through to my prompt for processing - How would I retrieve the entire pdf’s content after it has gone 
through the LLM? Or am I not using/thinking about this properly because my use case isn’t to use it as a chatbot but rat
her a processing layer for the entire pdf
```
---

     
 
all -  [ AI Agents using LangChain ](https://www.reddit.com/r/Langchaindev/comments/1arfbyw/ai_agents_using_langchain/) , 2024-02-19-0910
```
Hey everyone, check out this tutorial on how to run different AI-Agents using LangChain https://youtu.be/3pdcvSnCbf0?si=
RmUqW5GjlEDkhyYT
```
---

     
 
all -  [ Fanchat, a character.ai website powered by Mistral Ai ](https://www.reddit.com/r/MistralAI/comments/1arf6rx/fanchat_a_characterai_website_powered_by_mistral/) , 2024-02-19-0910
```
Hello Mistral Fans ! Just a quick message to say that i've created a [character.ai](https://character.ai) like website w
ith Langchain , Next.js and Mistral Api.   
Don't hesitate to try it and tell me what do you think ! 

[https://www.wear
efanchat.com](https://www.wearefanchat.com/dashboard)  
[https://youtu.be/0tbyMuBrFU8?si=kJ2z5Z1A2M9Zg8ro](https://youtu
.be/0tbyMuBrFU8?si=kJ2z5Z1A2M9Zg8ro)
```
---

     
 
all -  [ Conditional bypassing chain stages ](https://www.reddit.com/r/LangChain/comments/1areohp/conditional_bypassing_chain_stages/) , 2024-02-19-0910
```
Hello everyone! Is there a way to make, in idiomatic way, a conditional RunningSequence and bypass llm stage if retrieve
r returns empty list?
```
---

     
 
all -  [ Langchain is overhyped, you don't need it ](https://www.reddit.com/r/ChatGPTCoding/comments/1arbtc1/langchain_is_overhyped_you_dont_need_it/) , 2024-02-19-0910
```
I see nobody is talking about the downsides of langchain, I would have not wasted my time if we had. Let's do it now.

I
 have multiple projects using gpt, mistral, etc. Some of them use langchainjs and some of them use official sdk (e.g. op
enai node ackage,) and some directly make http request to the api. 


* All projects that don't use langchain are workin
g fine
* It is debatable which was most productive among sdk vs direct http call but I'd lean towards direct http call.

* On the other hand wherever I used langchain, it took me significantly more time to get started and fix bugs, langchain
 is a complex project. And even after using its features such as function calling, caching, etc. I don't see any real va
lue addition.

The initial thought process to choose langchain was that it would be easier to switch gpt with other mode
ls (in future). I was trying to solve a problem which I didn't have but the hype made me believe otherwise. To even make
 things worse, now I see that it will be harder to switch the models than using those models without langchain. 

With a
ll due respect to authors, I believe the project has lost its direction and trying to do more than it should be doing. F
irst you need to focus on basic stuff, make it simple to use and debug, and then focus on adding more value. If the prom
ise of portability between models is not delivered and complexity is added which makes doing even basic stuff harder, wh
y would I choose to use langchain and explore other features? My learning is simple, choose the direct api integration o
ver langchain. Until you see some specific usage of langchain, don't use it. I have multiple llm based projects doing al
l sorts of different stuff and even after 1+ yrs of development, none of them would need langchain, and I can't imagine 
why would someone need langchain ever.

How was your experience with langchain vs without it?
```
---

     
 
all -  [ In langchain/llama-index how to connect to multiple databases at once? [SQL Server] ](https://www.reddit.com/r/LangChain/comments/1ar8v7o/in_langchainllamaindex_how_to_connect_to_multiple/) , 2024-02-19-0910
```
What I want to do is - 

    connection_string = (
'DRIVER={ODBC Driver 17 for SQL Server};\
                      SERVE
R='+server+';\
                      DATABASE='+database+';\
                      UID='+username+';\
                  
    PWD='+password+';\
                      readonly=True'
)
connection_url = URL.create(
 'mssql+pyodbc', 
 query={'od
bc_connect': connection_string}
)
    sql_database = SQLDatabase(engine, sample_rows_in_table_info=3, include_tables=lis
t(table_details.keys()), view_support=True)

As you can see, here tables of only one database can be specified. What if 
I want to query multiple databases and also I require joining tables of multiples databases. how can I specify that?
```
---

     
 
all -  [ Langchain User Group Meeting Today Feb 15 2024 ](https://www.reddit.com/r/LangChain/comments/1ar8h9d/langchain_user_group_meeting_today_feb_15_2024/) , 2024-02-19-0910
```
Hello!

I've been organizing a langchain user group meeting every other Thursday at 7pm eastern US time.

We  get people
 just interested in langchain, people using langchain at   work, people using langchain as a hobby. We like to discuss t
he   langchain blog posts, interesting projects using langchain, and as a   general networking event among people tuned 
into the AI boom. It's a  great opportunity to share the latest developments, what works, what   doesn't work, and so on
.

[https://www.meetup.com/langchain-user-group/events/298419249/](https://www.meetup.com/langchain-user-group/events/29
8419249/)
```
---

     
 
all -  [ Should I use next.js if I don't utilize the built in api functionality? ](https://www.reddit.com/r/nextjs/comments/1ar7w31/should_i_use_nextjs_if_i_dont_utilize_the_built/) , 2024-02-19-0910
```
Let's take for instance the [vercel AI chatbot](https://vercel.com/templates/next.js/nextjs-ai-chatbot) \- it uses the a
pi folder to expose the CRUD requests for langchain and openai calls.

&#x200B;

I get that \`useChat\` from the \`ai\` 
package relies on \`route.ts\` file as an endpoint but I don't exactly see why I should use this functionality vs a trad
itional http call to a backend like django/rails/node etc.

&#x200B;

If I don't use the built in api from next.js, is t
here a point to using this framework?  
What is the benefit of using the built in api vs a traditional http client?
```
---

     
 
all -  [ How to implement LLM AI chatbot using vLLM in AWS with EKS ](https://www.reddit.com/r/LangChain/comments/1ar7hk9/how_to_implement_llm_ai_chatbot_using_vllm_in_aws/) , 2024-02-19-0910
```
 Hi guys,

I need some help and was wondering if anyone have some steps or a guide for me to implement the Mixtral-8x7B-
Instruct-v0.1 model (the LLM for my AI chatbot) using this GPU optimized library called vLLM ([https://github.com/vllm-p
roject/vllm](https://github.com/vllm-project/vllm)) in AWS using EKS (Elastic Kubernetes Service).

This is urgent. Woul
d really really appreciate any help with this. Many thanks!

Ps: if you have some sort of rough guidelines without the v
LLM part or instead of EKS use EC2, that would work too.
```
---

     
 
all -  [ How to set up RAG with Dolphin-mixtral-8x7b on text-generation-webui? ](https://www.reddit.com/r/Oobabooga/comments/1ar6i5i/how_to_set_up_rag_with_dolphinmixtral8x7b_on/) , 2024-02-19-0910
```
Hey I am new to all this AI stuff and I'm trying to do my first  setup on linux. I've decided to run Dolphin-mixtral-8x7
b on my machine but I would like if it could retrieve information from the internet or my documents but I have no Idea o
n how to achieve this. I've heard of LangChain but I can't find a n00b friendly tutorial for 0 knowledge people.   

Can
 you help me with this?   
```
---

     
 
MachineLearning -  [ [D] What's the standard practice for setting initialization prompts and maintaining context when swi ](https://www.reddit.com/r/MachineLearning/comments/1aq78ao/d_whats_the_standard_practice_for_setting/) , 2024-02-19-0910
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

     
 
MachineLearning -  [ Whats in your RAG setup? [D] ](https://www.reddit.com/r/MachineLearning/comments/1apcp2w/whats_in_your_rag_setup_d/) , 2024-02-19-0910
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

     
 
MachineLearning -  [ [D] What's the best current RAG setup that would work with a local LLM? ](https://www.reddit.com/r/MachineLearning/comments/1ag6bo7/d_whats_the_best_current_rag_setup_that_would/) , 2024-02-19-0910
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

     
 
MachineLearning -  [ [P]: Anukool: My job hunting assistant ](https://www.reddit.com/r/MachineLearning/comments/1adu3tw/p_anukool_my_job_hunting_assistant/) , 2024-02-19-0910
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

     
 
deeplearning -  [ [D] WebVoyager: Navigating Digital Cosmos with LangGraph & Multimodal Models ](https://www.reddit.com/r/deeplearning/comments/1altlca/d_webvoyager_navigating_digital_cosmos_with/) , 2024-02-19-0910
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

     
 
deeplearning -  [ [D] Langchain Elevates with Step-Back Prompting using RAGatouille ](https://www.reddit.com/r/deeplearning/comments/1agtyeh/d_langchain_elevates_with_stepback_prompting/) , 2024-02-19-0910
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

     
 
deeplearning -  [ Become an AI Developer (Free 9 Part Series) ](https://www.reddit.com/r/deeplearning/comments/1afgp2r/become_an_ai_developer_free_9_part_series/) , 2024-02-19-0910
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

     
 
deeplearning -  [ DSPy Explained! ](https://www.reddit.com/r/deeplearning/comments/1adypks/dspy_explained/) , 2024-02-19-0910
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

     
