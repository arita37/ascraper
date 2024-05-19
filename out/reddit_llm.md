 
all -  [ Example of a chatless agentic workflow that keeps the human in the loop ](https://www.reddit.com/r/LangChain/comments/1cvavh7/example_of_a_chatless_agentic_workflow_that_keeps/) , 2024-05-19-0911
```
[https://colab.research.google.com/drive/1JBd3v4jt5GEU1zCiLnHsZsJjknR6\_Cm2?usp=sharing](https://colab.research.google.c
om/drive/1JBd3v4jt5GEU1zCiLnHsZsJjknR6_Cm2?usp=sharing)
```
---

     
 
all -  [ Hello guys I am trying to create a resume for new grad cs roles let me know which resume format is b ](https://www.reddit.com/gallery/1cv9ic1) , 2024-05-19-0911
```
Thanks.
```
---

     
 
all -  [ Cannot stream the output to Streamlit ](https://www.reddit.com/r/LangChain/comments/1cv5drf/cannot_stream_the_output_to_streamlit/) , 2024-05-19-0911
```
I am trying to stream the output of my chain to Streamlit, but without success.

This is the code:

`answer = st.write_s
tream(ai_assistant_chain.stream({'input': question, 'chat_history': st.session_state.chat_history}))`

And it gives the 
following result:

    [...]
    {
    'answer':' roi'
    }
    {
    'answer':' Lé'
    }
    {
    'answer':'op'
    
}
    {
    'answer':'old'
    }
    {
    'answer':' Ier'
    }
    [...]

Does somebody know what I have to do?

Strea
ming the output in a notebook works well:

    for chunk in ai_assistant_chain.stream({'input': question, 'chat_history'
: chat_history}):
        answer_chunk = str(chunk.get('answer'))
        print(answer_chunk, end='')
```
---

     
 
all -  [ Why choose any other LLM than gpt-4 or gpt-4o for our AI-based applications? ](https://www.reddit.com/r/LangChain/comments/1cv07x9/why_choose_any_other_llm_than_gpt4_or_gpt4o_for/) , 2024-05-19-0911
```
This is an extremely direct question. I'm trying to understand what leads to choosing an LLM (through API) other than GP
T-4 or GPT-4o since they already cover a good amount of use-cases for our AI-based products.

That's because I am curren
tly helping a company as a software engineer, and this question above is the one we keep racking our brains for and look
ing for a reason. 

  
Throw down some of your reasons, what are you using, why?

Thanks a lot guys
```
---

     
 
all -  [ RAG: Contextual questions ](https://www.reddit.com/r/LocalLLM/comments/1cuyevi/rag_contextual_questions/) , 2024-05-19-0911
```
Hey everyone!
I am trying to create an assistant for a business that has knowledge about it. My first approach was to ge
t the business knowledge and convert it into question-answer pairs and finetune(qlora) the model. I tried to use a high 
rank(1024) and 6 epochs to try make it learn the new knowledge but it didn't work(hallucinations). So since everybody re
commends RAG for this usecase i decided to give it a try.
 The problem i am facing is this: Let's say that my knowledge 
is a list of tech projects with their corresponding paragraphs like overview, implementation details and possible applic
ations. When i ask 'what is <projectname>?' The embedding model returns the overview paragraph and feeds it to the promp
t of the llm and i get the correct answer. But when i make a contextual question afterwards like 'perfect, now tell me a
bout its applications' obviously the embedding model will not understand that i am talking about the <projectname> so it
 will either return nonsense or nothing(since i have similarity threshold). So the llm will refuse to answer.
I will giv
e some more details about my implementation: I am using ollama for the inference and the embedding model and langchain f
or creating the embeddings and the chain. Since i need speed and the conversations will be long, i added a similarity th
reshold and a small k for what the embedding model will return and i inject this knowledge only on the prompt and not on
 the whole chat object(i am talking about the chat method of ollama). Some would say that you should have larger k and k
eep this on the whole conversation but then after a few questions the context window will be filled.keep in mind that th
e assistant will not only answer on questions based on the knowledge but also simple things like 'hello', 'how are you' 
etc. which means that these things will also pass from the embedding model, so a threshold and a small k in order to not
 return an embedding is required. Also passing irrelevant chunks in these simple questions make the model slower besides
 making it answer irellevant things.
Is there a framwork that manages conextual questions in Rag applications? Something
 like reforming the question based on the context and then feed that to the embedding model and then to the llm? Or mayb
e a completely different approach from rag that can solve these problems?
Thanks!
```
---

     
 
all -  [ React Agent - Arxiv tool is hallucinating ](https://www.reddit.com/r/LangChain/comments/1cuy96x/react_agent_arxiv_tool_is_hallucinating/) , 2024-05-19-0911
```
I am building a ReAct agent with arxiv tool usage so I can just chat with the agent to get interesting new papers. I am 
using a local LLM (Mistral Instruct 0.2) and not OpenAI. Overall, the model works well and uses most tools accurately. F
or Arxiv I am only getting hallucinations.

When I ask 'What's the paper 1605.08386 about?'

    The paper 1605.08386 is
 a review discussing the advancements and current state of deep learning techniques in the field of automatic speech rec
ognition (ASR), covering various deep learning architectures and their applications in ASR, as well as challenges and fu
ture directions.'

While it should return

    The paper '1605.08386' is about heat-bath random walks with Markov bases


I am using this as a resource [https://python.langchain.com/v0.1/docs/integrations/tools/arxiv/](https://python.langcha
in.com/v0.1/docs/integrations/tools/arxiv/)

Looking for tips to get the tool to work. I don't think this is a coding qu
estion but rather a configuration issue. 
```
---

     
 
all -  [ Multimodal RAG with GPT-4o and Pathway: Accurate Table Data Analysis from Financial Documents ](https://www.reddit.com/r/LangChain/comments/1cuy4e6/multimodal_rag_with_gpt4o_and_pathway_accurate/) , 2024-05-19-0911
```
Hey r/langchain I'm sharing a showcase on how we used GPT-4o to improve retrieval accuracy on documents containing visua
l elements such as tables and charts, applying GPT-4o in both the parsing and answering stages.

It consists of several 
parts:

**Data indexing pipeline (incremental):**

1. We extract tables as images during the parsing process.
2. GPT-4o 
explains the content of the table in detail.
3. The table content is then saved with the document chunk into the index, 
making it easily searchable.

**Question Answering:**

Then, questions are sent to the LLM with the relevant context (in
cluding parsed tables) for the question answering.

**Preliminary Results:**

Our method appears significantly superior 
to text-based RAG toolkits, especially for questions based on tables data. To demonstrate this, we used a few sample que
stions derived from the Alphabet's 10K report, which is packed with many tables.

**Architecture diagram**: [https://git
hub.com/pathwaycom/llm-app/blob/main/examples/pipelines/gpt\_4o\_multimodal\_rag/gpt4o.gif](https://github.com/pathwayco
m/llm-app/blob/main/examples/pipelines/gpt_4o_multimodal_rag/gpt4o.gif) 

**Repo and project readme**: [https://github.c
om/pathwaycom/llm-app/tree/main/examples/pipelines/gpt\_4o\_multimodal\_rag/](https://github.com/pathwaycom/llm-app/tree
/main/examples/pipelines/gpt_4o_multimodal_rag/)

We are working to extend this project, happy to take comments!
```
---

     
 
all -  [ [For Hire] GenAI Specialist, Ex-Booking.com Data Scientist [50USD/hr] ](https://www.reddit.com/r/forhire/comments/1cuvh55/for_hire_genai_specialist_exbookingcom_data/) , 2024-05-19-0911
```
Hi, I am data analyst/scientist with 4 years experience. I have worked for one of the world biggest Telecom groups (Tele
nor) and also Agoda(Booking.com). Now working as GenAI specialist at vanna AI

If your looking to outsource tasks or get
ting something built in Python/R or QuickSense/Tableau please do reach out.


I can provide evidence of everything, I ev
en write about data science/analytics on Medium: https://python.plainenglish.io/sankeying-with-plotly-90500b87d8cf

GenA
I projects:
https://medium.com/firebird-technologies/generate-powerpoints-using-llama-3-a-first-step-in-automating-slide
-decks-536f5fcb6e0e

https://medium.com/firebird-technologies/using-langchain-to-teach-an-llm-to-write-like-you-aab394d5
4792

Very good at making visualization. Will charge a reasonable rate
```
---

     
 
all -  [ “Live” RAG architecture? ](https://www.reddit.com/r/LangChain/comments/1cuuyzf/live_rag_architecture/) , 2024-05-19-0911
```
I’m looking to build a live search RAG chat system similar to Perplexity. What are the different architectural approache
s I could take (from high level).

Clean scraped html, chunk and embed then query and pull in? Or use an llm to parse th
e plain text from each scraped page and summarize it? Something else? 
```
---

     
 
all -  [ remix with langchain plus open ai ](https://www.reddit.com/r/react/comments/1cuu9py/remix_with_langchain_plus_open_ai/) , 2024-05-19-0911
```
So I was trying to create a chatbot in my portfolio web app. The bot reads the json which my portfolio is using and inte
racts with the users if asked anything related to me.
everything working fine in local. but when deployed to vercel. cha
tbot is giving 500
so when I make a api/chat request, it fails but when I refresh the app, I can see the response in the
 log for / request. 
the actual request throwing
type error: nodeResponse. header.raw is not a function
I tried several 
ways but no luck. passed the headers. I googled it but no proper answer.

has anyone integrated it with remixjs before a
nd deployed on vercel?
```
---

     
 
all -  [ Overwhelmed with backend choices for features ](https://www.reddit.com/r/nextjs/comments/1cuu7we/overwhelmed_with_backend_choices_for_features/) , 2024-05-19-0911
```
Hey all, fairly new to NextJS and spent some time building up an MVP for a data project I’d like to offer to my local co
mmunity. 

Went with NextJS 14 (app router) on Vercel and used a combination of Shadcn & Recharts to get a nice proof of
 concept going with a data table and chart. 

Not sure if this is the best way to approach it, but I created a seed.ts f
irst for sample data, seeing as I know what the data model will look like. Now I need to figure out the best way to actu
ally handle the backend and I’m a little overwhelmed with all the options available.

Not planning on implementing any a
uth, ads or taking payment as its a pro bono project, but I do have some specific requirements around periodically grabb
ing data (via a combination of calling APIs and scraping some webpages). I also need to run an LLM step via LangChain to
 transform open text data to structured JSON and then ETLing into a database…

Have a preference for Python for the data
 work and saw that Vercel offer a runtime with cron jobs (and a PostgresDB) but I’ve already implemented a lot of the fr
ontend data transformation in TS… I’ve also seen that there are a ton of competing services from full BaaS solutions lik
e Supabase, Appwrite, Pocketbase, etc… to point solutions like trigger.dev, neon, and all the AWS/GCP/Azure offerings wi
th generous free tiers. 

I don’t expect the app to ever scale massively and I’m looking for a path of least resistance 
& complexity which will keep costs low; any experienced devs here willing to offer their $0.02? Thank you in advance!





```
---

     
 
all -  [ Just found about langchain and am too excited. Project ideas with llama3? ](https://www.reddit.com/r/LangChain/comments/1cutqyc/just_found_about_langchain_and_am_too_excited/) , 2024-05-19-0911
```

```
---

     
 
all -  [ Representing a prompt chain / graph in a diagram for scientific publications  ](https://www.reddit.com/r/LangChain/comments/1cusnwj/representing_a_prompt_chain_graph_in_a_diagram/) , 2024-05-19-0911
```
Hello everyone,

I wonder which tools are out there to represent a prompt chain for scientific publications. Is there ma
ybe something mature like an UML notation for this specific case?

I know you can create an ascii or mermaid graph using
 langchain but this is not what I need.

Are there any opinions and suggestions from experienced users regarding tools t
o create prompt diagrams?
```
---

     
 
all -  [ can we return structured output with langchain agents? ](https://www.reddit.com/r/LangChain/comments/1cusa3a/can_we_return_structured_output_with_langchain/) , 2024-05-19-0911
```
been playing with agents for a while now, concretely via langchain tool calling agents/custom- is there a way to structu
re the (final) output to be schema tied (using pydantic as we have for llms)?

all my searches so far found either utili
zing some rural implementations like swarms or very simplistic ones (suited specifically for RAG)
```
---

     
 
all -  [ LLMs loosing it when i connect them to connected to LangChain  ](https://www.reddit.com/r/pytorch/comments/1cuquer/llms_loosing_it_when_i_connect_them_to_connected/) , 2024-05-19-0911
```
When i use LLMs in my local machine using the Ollama Framework ,I use CLI to test the models out after downloading and t
he response i get for chat models is usually clear (sometimes it hallucinates). but mostly clear.

Then when i use Langc
hain to build functions using`PromptTemplate` ,`SequenceChains` the model will suddenly loose control and starts to gene
rate random output almost endlessly for 40-50mins or even more until i interrupt the notebook kernel.

It is generating 
question answer pairs , or endless paragraphs

I've experienced this behavior in many models; Gemma , LLaMa 2 , Qwen , P
hi 2 ( this one breaks often ) All around 2-5 B parameters

**What is happening here ?? Is it due to some internal promp
t inside these Langchain abstractions??? idk what is causing this behavior . I always keep the temperature param at 0 st
ill this happens**


```
---

     
 
all -  [ I am seeing weird behaviors in LLMs when using LangChain , to build simple chat apps.    ](https://www.reddit.com/r/LargeLanguageModels/comments/1cuqsin/i_am_seeing_weird_behaviors_in_llms_when_using/) , 2024-05-19-0911
```
When i use LLMs in my local machine using the Ollama Framework ,I use CLI to test the models out after downloading and t
he response i get for chat models is usually clear (sometimes it hallucinates). but mostly clear.

Then when i use Langc
hain to build functions using`PromptTemplate` ,`SequenceChains` the model will suddenly loose control and starts to gene
rate random output almost endlessly for 40-50mins or even more until i interrupt the notebook kernel. 

It is generating
 question answer pairs , or endless paragraphs 

I've experienced this behavior in many models; Gemma , LLaMa 2 , Qwen ,
 Phi 2 ( this one breaks often ) All around 2-5 B parameters 

**What is happening here ?? Is it due to some internal pr
ompt inside these Langchain abstractions??? idk what is causing this behavior . I always keep the temperature param at 0
 still this happens** 
```
---

     
 
all -  [ Training a chatbot based on chats ](https://www.reddit.com/r/LangChain/comments/1cuqbpq/training_a_chatbot_based_on_chats/) , 2024-05-19-0911
```
I'm working to build a solution using which a bot can be trained to behave as a person based on chat history of that per
son with other people. 

User uploads their chat history (WhatsApp, Slack, sms chats, etc.) and the bot learns the tone 
and memories from those chats to start behaving as a virtual avatar of the user.

Any pointers on where to start?

I wou
ld imagine the tool will need to extract memories from the chats. 
Then to learn the tone, it's either fine tuning or cr
eating system prompts based on the chat history.

Would love to know if anyone has attempted something like this.
```
---

     
 
all -  [ Advanced RAG without Langchain, LlamaIndex? ](https://www.reddit.com/r/LLMDevs/comments/1cuq21d/advanced_rag_without_langchain_llamaindex/) , 2024-05-19-0911
```
Are there resources to build advanced RAG systems without using tools like Langchain and LlamaIndex? These tools keep ch
anging their framework and documentation is poor. Looking to shift from depending on them. 

I want to build efficient R
AG systems for unstructured data (plain text, tables in CSV/XLS format) and also for structured SQL data.
```
---

     
 
all -  [ (Code included) Struggle to scrape websites and feed content to LLMs? I benchmarked some tools and t ](https://www.reddit.com/r/LangChain/comments/1cub6pg/code_included_struggle_to_scrape_websites_and/) , 2024-05-19-0911
```
Video: [https://www.youtube.com/watch?v=QxHE4af5BQE](https://www.youtube.com/watch?v=QxHE4af5BQE)

Code: [https://github
.com/trancethehuman/ai-workshop-code/blob/main/Web\_scraping\_for\_LLM\_in\_2024.ipynb](https://github.com/trancethehuma
n/ai-workshop-code/blob/main/Web_scraping_for_LLM_in_2024.ipynb)

  
Let me know what you think in the comments. I'll re
spond.
```
---

     
 
all -  [ Ingestion options for vectorDB ](https://www.reddit.com/r/vectordatabase/comments/1cu7e7n/ingestion_options_for_vectordb/) , 2024-05-19-0911
```
I’m trying to create some low latency ingestion ETL embedding pipelines into either pinecone or Zilliz or LanceDB for my
 application, the idea is whenever a user send some text, I can process and filter, group by then do llm assisted summar
ization immediately, then create embedding to save into a vectorDB without any intermediate storage. Fivetran only offer
s dbt on the storage layer, langchain does not handle sql processing, Dagster only deal with orchestration and seems mor
e appropriate for batch processing, aws lambda is the closest solution I can find but version control and monitoring mig
ht take some planning. setting up my own cluster just for this and monitoring it 24/7 seems the last resort. I wonder if
 there are other options. (We are a 3 person team, so coding time is really precious) thanks ahead! 
```
---

     
 
all -  [ Do you even need LangChain? ](https://www.reddit.com/r/LangChain/comments/1cu6wjg/do_you_even_need_langchain/) , 2024-05-19-0911
```
As a disclaimer: I personally think LangChain is awesome. It lets you cut your dev time by a lot. But since I've been to
ying around with many frameworks, tools, and models I compiled a list of five basic (but important) questions every dev 
or person looking to integrate AI must ask themselves.

**>>>** [**Watch on YouTube**](https://youtu.be/uG0cs8AlnHw)

  

I'd love to know your thoughts and/or suggestions!
```
---

     
 
all -  [ Introducing Cycls: A New AI Chat Framework ](https://www.reddit.com/r/Chatbots/comments/1cu5503/introducing_cycls_a_new_ai_chat_framework/) , 2024-05-19-0911
```
I wanted to introduce you to Cycls, a lightweight Python framework for developing and sharing AI chat applications. It's
 designed to simplify the process, offering features like easy publishing, instant sharing with public URLs, and multimo
dal input/output. Cycls supports popular models such as OpenAI and LangChain and includes a ready-to-use webchat fronten
d.

If you're into AI development, this might be worth checking out. You can learn more about it [here](https://docs.cyc
ls.com/overview).

What are your thoughts? Anyone planning to give it a try?
```
---

     
 
all -  [ Sentence / chunk window retrieval in Langchain using Qdrant ](https://www.reddit.com/r/LangChain/comments/1cu44i1/sentence_chunk_window_retrieval_in_langchain/) , 2024-05-19-0911
```
Guys,

Checkout this PR [\[https://github.com/langchain-ai/langchain/pull/21553\]](https://github.com/langchain-ai/langc
hain/pull/21553) that implements something similar to sentence window retrieval. I have named in chunk window retrieval 
because based on the window size, this method would fetch those many chunks above and below the current chunk. 

Importa
nt point to note here is that when creating a chunk for Qdrant, you MUST have integer based chunk id for this to work. H
ave added that support in Qdrant.add\_texts(..) as well. 

Hope it helps.
```
---

     
 
all -  [ Utilizing Neo4j's Knowledge Graph and Semantics for a RAG - Chatbot ](https://www.reddit.com/r/LangChain/comments/1cu2ozt/utilizing_neo4js_knowledge_graph_and_semantics/) , 2024-05-19-0911
```
I'm working on developing a chatbot that uses Neo4j as the database. I've created a knowledge graph by importing a corpu
s of data into Neo4j.  
how to effectively leverage both the knowledge graph aspect and the semantic capabilities of Neo
4j for this chatbot project?

Has anyone worked on a similar project? What strategies or approaches did you employ to op
timize the retrieval from Neo4j? I'm open to any suggestions or insights that could help improve the chatbot's performan
ce and make the most out of Neo4j's unique features.
```
---

     
 
all -  [ Gemini directed me to porn ](https://i.redd.it/bddxj0u0ly0d1.jpeg) , 2024-05-19-0911
```
All I asked was if it could create agents. The first link it provided is porn. 
```
---

     
 
all -  [ Advanced RAG: Ensemble Retriever ](https://www.reddit.com/r/LargeLanguageModels/comments/1ctzxqx/advanced_rag_ensemble_retriever/) , 2024-05-19-0911
```
Hi,

Made a video on Advanced RAG: **Ensemble Retriever**.

The Ensemble Retriever combines multiple high-performing ret
rieval techniques simultaneously, using majority voting and ranking to deliver **strong relevant** passages.

The logic 
is: Better retrieved passages == better context == better generation.

Originally it comes from this paper: **Reciprocal
 Rank Fusion outperforms Condorcet and individual Rank Learning Methods**



But I made a video on how to use it with La
ngchain and llama Index with GPT-4o.

Hope you find it useful.

[**https://youtu.be/s2i4zeWjUtM**](https://youtu.be/s2i4
zeWjUtM)
```
---

     
 
all -  [ Advanced RAG: Ensemble Retriever ](https://www.reddit.com/r/LanguageTechnology/comments/1ctzxje/advanced_rag_ensemble_retriever/) , 2024-05-19-0911
```
Hi,

Made a video on Advanced RAG: **Ensemble Retriever**.

The Ensemble Retriever combines multiple high-performing ret
rieval techniques simultaneously, using majority voting and ranking to deliver **strong relevant** passages.

The logic 
is: Better retrieved passages == better context == better generation.

Originally it comes from this paper: **Reciprocal
 Rank Fusion outperforms Condorcet and individual Rank Learning Methods**

But I made a video on how to use it with Lang
chain and llama Index with GPT-4o.

Hope you find it useful.

[**https://youtu.be/s2i4zeWjUtM**](https://youtu.be/s2i4ze
WjUtM)
```
---

     
 
all -  [ Basic RAG chat bot minimum ](https://www.reddit.com/r/LangChain/comments/1ctztvf/basic_rag_chat_bot_minimum/) , 2024-05-19-0911
```
Hi-
  I have followed a few simple RAG tutorials with langchain but don’t seem to be getting anywhere - either my agent 
exits before a final answer or my chain just exits with nothing.

  I’m a newbie to RAG and LLMs in general so I wanted 
to check a few things that I haven’t managed to learn from online tutorials.

1. I assume choice of vector DB makes very
 little difference for these small toy projects with only <50 PDFs being ingested - each not large.

2. I don’t understa
nd if the embeddings function in between PDF and DB needs to be matched with anything else later in the toolchain- can I
 use pretty much anything with impunity? I’m using the langchain pypdfloader, load_and_split and langchain.embeddings.Hu
ggingFaceEmbeddings.
This is perhaps a mishmash from different tutorials…

3. Is there a ‘best’ way to run a LLM locally
? I have tried straight python and llamacpp from langchain but it doesn’t seem to recognise my GPU.
  I’m thinking of mo
ving to running the llm on LMStudio and accessing the API in python but that’s additional complexity I would rather avoi
d at this stage. (Or is it super easy?)

I’m sure I will have more questions later but this is enough to keep me going f
or now!
Thanks!
```
---

     
 
all -  [ Open source LLMs ](https://www.reddit.com/r/LangChain/comments/1ctzmfo/open_source_llms/) , 2024-05-19-0911
```
Hey there 🖖
Im participating in a national contest for NLP sentiment analysis
Im planning on using langchain. Wanted to 
ask you guys if you have any open source LLM recommendations for me to use or check, the model should be local so 70b ll
ama is not the best choice.
```
---

     
 
all -  [ How to extract the 'Methods' section out of a scientific article ](https://www.reddit.com/r/LangChain/comments/1ctz1jf/how_to_extract_the_methods_section_out_of_a/) , 2024-05-19-0911
```
Hi folks,

I am working on a project to develop a specific question-answer system based on RAG for scientific research. 
The questions could be 'What province, city or town were the samples collected from?'. 

The RAG pipeline I built now do
es not perform well because of many reasons. One reason is that the contents in the introduction and/or discussion secti
ons may confuse the pipeline. So one way I am thinking is to just extract the method section or method and results secti
ons for the vector store (ignoring the other sections). I have explored different options, but none of them worked. I ev
en tried the openai file search ([https://platform.openai.com/docs/assistants/tools/file-search](https://platform.openai
.com/docs/assistants/tools/file-search)), but it was not able to extract the complete section. 

I used pypdfloader to g
et all text from a pdf file first, and then asked openai file-search to extract the methods section. Is pypdfloader a go
od one to extract text in good order?

Anyone knows a good way to extract a specific section from a PDF file?

Thanks!
```
---

     
 
all -  [ Exploring Cost Efficiency: OpenAI GPT-4-Turbo Model vs. AWS OpenAI API ](https://www.reddit.com/r/LangChain/comments/1ctyz7h/exploring_cost_efficiency_openai_gpt4turbo_model/) , 2024-05-19-0911
```
I am reviewing the pricing for the OpenAI GPT-4-Turbo model and have noticed that using memory with it on RAG Task incur
s high costs. I am working for an organization. Is anyone using the AWS OpenAI API? Is it a bit cheaper to use?'
```
---

     
 
all -  [ Chunking text documents in langchain ](https://www.reddit.com/r/LangChain/comments/1ctyslg/chunking_text_documents_in_langchain/) , 2024-05-19-0911
```
I have to find a way to determine the format of a pdf document like its plain or having paragraphs or title-definition f
ormat etc. By knowing the format i can chunk the document efficiently without losing the context/semantics. Is there any
 way to do so?
```
---

     
 
all -  [ How to generate payments links in chatbot ? ](https://www.reddit.com/r/LangChain/comments/1ctypfm/how_to_generate_payments_links_in_chatbot/) , 2024-05-19-0911
```
i am building a hotel room booking chatbot using OpenAI API , currently it is able to look up available rooms from the d
atabase using langchains SQL agent , i want to add room booking functionality in it for that i want receive payments fro
m the user and thus i need chatbot to generate payments links. i know payments links can be generated using stripe or ra
zorpay api but how to make chatbot call those api functions to get paymnets link, does anyone has any expeiences with it
 or know how to do this? 
```
---

     
 
all -  [ How to generate payments links in chatbot ? ](https://www.reddit.com/r/Chatbots/comments/1ctyk9f/how_to_generate_payments_links_in_chatbot/) , 2024-05-19-0911
```
i am building a hotel room booking chatbot using OpenAI API , currently it is able to look up available rooms from the d
atabase using langchains SQL agent , i want to add room booking functionality in it for that i want receive payments fro
m the user and thus i need chatbot to generate payments links. i know payments links can be generated using stripe or ra
zorpay api but how to make chatbot call those api functions to get paymnets link?  
```
---

     
 
all -  [ Getting little callbacks, roast away ](https://www.reddit.com/r/resumes/comments/1ctw6qz/getting_little_callbacks_roast_away/) , 2024-05-19-0911
```
Finishing grad school in december, looking for anything in software engineering or data science/engineering. First two j
obs don't have bullet points due to lack of space (trying to keep to one page), but I thought they would still be valuab
le there anyway

https://preview.redd.it/52gau6s2sw0d1.png?width=5100&format=png&auto=webp&s=0b1d196ed69985473da777ffee7
ec8151751ac99


```
---

     
 
all -  [ Embeddings of certain dataset ](https://www.reddit.com/r/LangChain/comments/1ctv5au/embeddings_of_certain_dataset/) , 2024-05-19-0911
```
Hii community
I have a dataset with keys like name,description,why it matters,what to look for. Basically all these cont
ains 1 line information(avg 10 words) ,I want to embedd these dataset using open ai models what are different ways for e
mbedding these dataset .
My puropse is when user give some query i can give him top k matched results.
```
---

     
 
all -  [ How to extract date period from user prompt ](https://www.reddit.com/r/LangChain/comments/1ctr9h5/how_to_extract_date_period_from_user_prompt/) , 2024-05-19-0911
```
Hello everyone!
I would like to have some help for a problem i have
I want to extract two parameters:
date_from: the sta
rt of the period
date_to: the end of the period

I tried using this [example](https://python.langchain.com/v0.1/docs/use
_cases/extraction/) but it sometimes misses at simple prompts

What can i add to make it better?
Here’s the [code](https
://hastebin.skyra.pw/yehokamuqo.py) i made


Basically i want it to get from the user’s prompt the correct date or perio
d
```
---

     
 
all -  [ Classify PDF based on separate RAG database ](https://www.reddit.com/r/LangChain/comments/1ctqz2c/classify_pdf_based_on_separate_rag_database/) , 2024-05-19-0911
```
I’m trying to set something up where a user can upload a pdf and have it classified based on a resource I converted into
 a vector database. 
```
---

     
 
all -  [ Langchain using llama3 to build recommendation system ](https://www.reddit.com/r/Python/comments/1ctnxa4/langchain_using_llama3_to_build_recommendation/) , 2024-05-19-0911
```
Hi,

Recently I played a bit with LLMs, specifcally exploring ways of running the models locally and building prompts us
ing LangChain. As a result ended up coding a small recommendation system, powered with Llama3-7b model, which suggests t
opics to read on HackerNews.

Wanted to share my experiences, so I wrote a small article where I described all my findin
gs.  
Hope you'll like it: [https://lukaszksiezak.github.io/ScrapyToLLM/](https://lukaszksiezak.github.io/ScrapyToLLM/)


Github repo: [https://github.com/lukaszksiezak/ScrapyToLLM](https://github.com/lukaszksiezak/ScrapyToLLM)

**What the p
roject does:**

It's a Python application which uses scrapy to scrape HackerNews page. Scraped articles are pipelined to
 redis, which is then feeding Llama3 using langchain. Prompter is configured to serve a user articles which are matching
 his request.

**Target Audience**:

I think it suits the best all the people who are looking for a Hello World projects
 using LLMs. I think it also reveals some difficulties related to LLM tech, what potential problems could be found in pr
oduction systems.

**Comparison:**

Recommendation systems are widely used and known, however LLMs are the ones which ma
y work out of the box when appropriate prompt is given. It's kind of interesting to explore various usages of the techno
logy and take part in fast grow of that stack.

Cheers.
```
---

     
 
all -  [ Struggling with prompt management tools ](https://www.reddit.com/r/LangChain/comments/1ctk5l5/struggling_with_prompt_management_tools/) , 2024-05-19-0911
```
I’m working on a project for a client who needs single summaries of games for a game recommender app they’re creating. I
’ve been trying to test out a pipeline of prompts to see what inputs generate the best summaries, but I’m struggling 😓 


It’s easy to view and edit one prompt at a time, but I need a tool that can handle these more complex, chained prompt s
cenarios effectively. It feels like there are tools out there that could potentially help, but none seem fully integrate
d into a seamless prompt management workflow. I want to look across multiple sample output examples (from several sample
 inputs), and see what’s working and what’s not. 

Anyone else facing the same struggles? How are you managing more comp
lex prompt scenarios / how are you integrating multiple tools to get the job done? 

Maybe it's just part of the job, bu
t I can't help but think there's got to be a better way to manage and streamline this whole process. Any insights or tip
s would be super helpful! 


```
---

     
 
all -  [ Optimizing AI Data Processing with MinIO Weaviate and Langchain in Retrieval Augmented Generation (R ](https://www.reddit.com/r/minio/comments/1ctiw1l/optimizing_ai_data_processing_with_minio_weaviate/) , 2024-05-19-0911
```
In this article, we will delve into the integration of MinIO with Retrieval-Augmented Generation (RAG) pipelines and Wea
viate vector storage, using LangChain.

[https://blog.min.io/optimizing-ai-data-processing-with-minio-weaviate-and-langc
hain-in-retrieval-augmented-generation-rag-pipelines/](https://blog.min.io/optimizing-ai-data-processing-with-minio-weav
iate-and-langchain-in-retrieval-augmented-generation-rag-pipelines/)
```
---

     
 
all -  [ Agents working in parallel with LangGraph ](https://www.reddit.com/r/LangChain/comments/1cthrqz/agents_working_in_parallel_with_langgraph/) , 2024-05-19-0911
```
I’m trying to figure out if it’s possible to create a Multi Agent application with LangGraph, where the agents can work 
in parallel (if needed).

Let’s say I have three agents (stupid example):
1. Supervisor
2. Agent specialized in tech con
ferences
3. Agent specialized in medical conferences

Each agent has its own tools.

The user query is “What are the mai
n tech conferences and medical conferences in San Francisco in November?”.

This query can be obviously split in two dif
ferent questions and each one can be addressed separately: 
1. What are the main tech conferences in San Francisco in No
vember?
2. What are the main medical conferences in San Francisco in November?

The Supervisor is able to process the or
iginal query, to produce these two questions and to route them separately to the correct Agent.

Is there a way to run t
hese two agents in parallel and to have a fourth Agent (or the supervisor itself) that waits for the two answers and put
s all together to produce a single final answer?

Does anyone have experience with such a use case?
```
---

     
 
all -  [ LangChain vs LlamaIndex  ](https://www.reddit.com/r/AI_Agents/comments/1cth187/langchain_vs_llamaindex/) , 2024-05-19-0911
```
Checkout this short video to understand the difference between two major Generative AI packages i.e. LangChain and Llama
Index and what to use when : https://youtu.be/Oy8UZp3potw?si=9mp9M5UrBjR-FX5G
```
---

     
 
MachineLearning -  [ [R] Building an Observable arXiv RAG Chatbot with LangChain, Chainlit, and Literal AI ](https://www.reddit.com/r/MachineLearning/comments/1crwh0q/r_building_an_observable_arxiv_rag_chatbot_with/) , 2024-05-19-0911
```
Hey r/MachineLearning, I published a new article where I built an observable semantic research paper application.

This 
is an extensive tutorial where I go in detail about:

1. Developing a RAG pipeline to process and retrieve the most rele
vant PDF documents from the arXiv API.
2. Developing a Chainlit driven web app with a Copilot for online paper retrieval
.
3. Enhancing the app with LLM observability features from Literal AI.

You can read the article here: [https://medium.
com/towards-data-science/building-an-observable-arxiv-rag-chatbot-with-langchain-chainlit-and-literal-ai-9c345fcd1cd8](h
ttps://medium.com/towards-data-science/building-an-observable-arxiv-rag-chatbot-with-langchain-chainlit-and-literal-ai-9
c345fcd1cd8)

Code for the tutorial: [https://github.com/tahreemrasul/semantic\_research\_engine](https://github.com/tah
reemrasul/semantic_research_engine)


```
---

     
 
MachineLearning -  [ [P] LLMinator: A Llama.cpp + Gradio based opensource Chatbot to run llms locally(cpu/cuda) directly  ](https://www.reddit.com/r/MachineLearning/comments/1cpbgd1/p_llminator_a_llamacpp_gradio_based_opensource/) , 2024-05-19-0911
```
Hi I am currently working on a context-aware streaming chatbot based on Llama.cpp, Gradio, Langchain, Transformers. LLMi
nator can pull LLMs directly from HF & run them locally on cuda or cpu.

I am looking for recommendations & help from op
ensource community to grow this further.

**Github Repo:** [https://github.com/Aesthisia/LLMinator](https://github.com/A
esthisia/LLMinator)

**Goal:** To help developers with kickstarter code/tool to run LLMs.

https://preview.redd.it/fnzja
7rjwqzc1.png?width=1846&format=png&auto=webp&s=a62c43614d63e82156fef8722b986b051cc1795b

**Features:**

* Context-aware 
Chatbot.
* Inbuilt code syntax highlighting.
* Load any LLM repo directly from HuggingFace.
* Supports both CPU & Cuda m
odes.
* Load & Offload saved models.
* Command Line Args
* API Access(Soon to be available)

Any review or feedback is a
ppreciated.
```
---

     
 
MachineLearning -  [ [D] Self-optimizing deterministic LLM memory using dspy, neo4j and vector databases. Need your input ](https://www.reddit.com/r/MachineLearning/comments/1cakjaf/d_selfoptimizing_deterministic_llm_memory_using/) , 2024-05-19-0911
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

     
 
deeplearning -  [ Seeking Advice: Solving Data Challenges with Large Language Models (LLMs) ](https://www.reddit.com/r/deeplearning/comments/1ca4nc1/seeking_advice_solving_data_challenges_with_large/) , 2024-05-19-0911
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

     
 
deeplearning -  [ Share the Coolest Out of The Box LLM Applications That Made You Say 'Wow that was smart' ](https://www.reddit.com/r/deeplearning/comments/1c9e6dj/share_the_coolest_out_of_the_box_llm_applications/) , 2024-05-19-0911
```
Hi, I'm looking at some LLM applications today but apart from guys doing big rags with langchain I don't see too many us
es that are out of the box or that make me say 'wow that was smart to use an LLM here'. Have you seen any cool stuff usi
ng LLMs recently that made you say 'wow, that was smart'?
```
---

     
