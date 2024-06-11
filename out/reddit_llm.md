 
all -  [ What vector db should I choose for 100m pages of text? ](https://www.reddit.com/r/LangChain/comments/1dcyc6i/what_vector_db_should_i_choose_for_100m_pages_of/) , 2024-06-11-0954
```
For context my vector db research started today from 0 knowledge and I feel absolutely unqualified to be making this dec
ision but here we are.

I have narrowed the search down to Milvus, Qdrant and potentially Weaviate.

I am scoping out a 
project for a client where we need to store up to 100 million pages. The application is scientific so retrieval precisio
n is a top priority as is search time latency and cost.

It seems:

* Milvus seems the most established and easiest to s
etup. also itis fast but takes up a lot of memory so can get quite expensive.
* Qdrant is fast and quite a bit cheaper t
han Milvus but lacks dynamic sharding 
* I have seen two conflicting reports one saying Weaviate is incredibly quick wit
h a benchmark of 0.12s for a particular query which took Milvus 0.9s to perform the same and then another where it says 
it is slow. and it is the cheapest.
* PG-vector is not as performant as the dedicated vector stores but are tried and te
sted part of the ecosystem and anecdotally great to work with 
* Chroma is not the best for accurate retrieval and I hav
en't heard many recommending it as the best except for its usability and ease of integration. 


```
---

     
 
all -  [ Intro to Generative UI with LangChain ](https://www.youtube.com/watch?v=mL_KuQgX9Oc) , 2024-06-11-0954
```

```
---

     
 
all -  [ How to build RAG on Delta tables using Ollama, Pyspark and Langchain ](https://www.reddit.com/r/LangChain/comments/1dcxfo0/how_to_build_rag_on_delta_tables_using_ollama/) , 2024-06-11-0954
```
I'm trying to build a RAG using Ollama, Pyspark. I wish to use my delta table as the source for this POC. Here's what I 
have done so far

\`\`\`python

    import pyspark
    from delta import *
    from langchain_community.document_loaders
 import PySparkDataFrameLoader
    from langchain_community.llms import Ollama
    from langchain_community.vectorstores
 import FAISS
    from langchain_community.embeddings import OllamaEmbeddings
    from langchain.text_splitter import Re
cursiveCharacterTextSplitter
    from langchain.chains import RetrievalQA
    from langchain.text_splitter import Charac
terTextSplitter
    
    ollama_llm = Ollama(model='phi')
    ollama_emb = OllamaEmbeddings(model='mxbai-embed-large') 

    
    # Read and Create df
    builder = pyspark.sql.SparkSession.builder.appName('DeltaTutorial') \
        .config(
'spark.sql.extensions', 'io.delta.sql.DeltaSparkSessionExtension') \
        .config('spark.sql.catalog.spark_catalog', 
'org.apache.spark.sql.delta.catalog.DeltaCatalog')
    spark = configure_spark_with_delta_pip(builder).getOrCreate()
   
 
    df = spark.createDataFrame(
        [
            (1, 'foo', 'hello'),
            (2, 'bar', 'world'),
          
  (3, 'baz', '!!!'),
            (4, '000', 'why'),
            (5, '111', 'who'),
        ],
        ['id', 'label', 'c
ol3']
    )
    
    # load documents
    
    loader = PySparkDataFrameLoader(spark, df, page_content_column='id')
    
documents = loader.load()
    print(documents)
    #[Document(page_content='1', metadata={'label': 'foo', 'col3': 'hello
'}), Document(page_content='2', metadata={'label': 'bar', 'col3': 'world'}), Document(page_content='3', metadata={'label
': 'baz', 'col3': '!!!'}), Document(page_content='4', metadata={'label': '000', 'col3': 'why'}), Document(page_content='
5', metadata={'label': '111', 'col3': 'who'})]
    
    print(f'Number of documents: {len(documents)}')
    #5
    
    
# Split and chunk documents
    text_splitter = CharacterTextSplitter(chunk_size=50, chunk_overlap=0, length_function=le
n)
    chunks = text_splitter.split_documents(documents)
    print(f'Number of chunks: {len(chunks)}')
    #5
    
    f
or i, _ in enumerate(chunks):
        print(f'chunk # {i} :: {chunks[i]}')
    
    #chunk # 0 :: page_content='1' metad
ata={'label': 'foo', 'col3': 'hello'}
    #chunk # 1 :: page_content='2' metadata={'label': 'bar', 'col3': 'world'}
    
#chunk # 2 :: page_content='3' metadata={'label': 'baz', 'col3': '!!!'}
    #chunk # 3 :: page_content='4' metadata={'la
bel': '000', 'col3': 'why'}
    #chunk # 4 :: page_content='5' metadata={'label': '111', 'col3': 'who'}
    
    # Embed
ding 
    
    db = FAISS.from_documents(documents, ollama_emb)
    
    retrieval_qa = RetrievalQA.from_chain_type(llm=
ollama_llm
        , chain_type='stuff'
        , retriever=db.as_retriever()
        , return_source_documents=True)
  
  
    # Retrieve response.
    query = 'Only using my data as source as context, what is the 'label' where 'col3' is 'w
orld' ?'
    result = retrieval_qa({'query': query})
    
    print(result)
    #{'query': 'Only using my data as source
 as context, what is the 'label' where 'col3' is 'world' ?', 'result': ' Based on the provided context, I can see that t
he columns are labeled 'who', 'why', and 'hello world'. Therefore, if 'col3' is 'world', then the label is 'hello'.', 's
ource_documents': [Document(page_content='5', metadata={'label': '111', 'col3': 'who'}), Document(page_content='4', meta
data={'label': '000', 'col3': 'why'}), Document(page_content='2', metadata={'label': 'bar', 'col3': 'world'}), Document(
page_content='3', metadata={'label': 'baz', 'col3': '!!!'})]}
    
    print('Result:', result['result'])
    #Result: B
ased on the provided context, I can see that the columns are labeled 'who', 'why', and 'hello world'. Therefore, if 'col
3' is 'world', then the label is 'hello'.
    
    # Correct Response should've been 'bar'

\`\`\`

Although the `df` lo
oks simple, yet the `RetrievalQA` is unable to produce the correct output.

My questions are:

1. Am I missing something
 here? How do I get my RAG to produce the correct result?
2. CharacterTextSplitter does not seem to be splitting the doc
ument into chunks. How do I split the Document into chunks? I have tried playing around with `chunk_size`. No matter wha
t, I always end up with 5 chunks.
3. What could be the reason for not getting the correct Results for my simple question
?

Below are my App Specs. I chose Phi due to laptop limitations. I'm on Mac 8GB. Unfortunately, the LLama2 model doxed 
my laptop

|Tool|Values|
|:-|:-|
|LLM|Ollama (Llama3)|
|Embedding|mxbai-embed-large|
|VectorDB|FAISS|
|Langchain|0.2.3|

|Python|3.9|
|Pyspark|3.5.1|

Any insights on this or directions to guide me will be helpful.
```
---

     
 
all -  [ How to handle ambiguous column names when converting Text-to-SQL in SQL Agent? ](https://www.reddit.com/r/LangChain/comments/1dcvnzv/how_to_handle_ambiguous_column_names_when/) , 2024-06-11-0954
```
**I have 2 cases of ambiguity** 

1. Similar names within a table - Eg: constrained\_demand, unconstrained\_demand

2.  
Same names across different tables. - Sales in both table1 and table 2

I have built a chatbot using open-ai tools agent
s , giving it access to SQLDatabaseToolKit. There is prefix, suffix and FewShotPrompt Template to handle multiple differ
ent calculations and complexities of SQL queries. Now user can ask multiple queries of the below format .

**Examples:**


1. What is the demand for 2024? - there is ambiguity as to if the user is asking constrained demand or unconstrained d
emand. Assumption that is no 'demand' column . Expectation - LLM should figure out such ambiguity without any hardcoding
 and then ask back the user as to which column he is referring to. Once LLM gets user input, then query with the new inf
o.

2. What is the sales for brand1?  there is ambiguity as to if the user is asking sales from table1 or table2. Expect
ation - LLM should figure out such ambiguity without any hardcoding and then ask back the user as to which table he is r
eferring to. Once LLM gets user input, then query with the new info.

  
Cannot handle this in column description as eve
n if the descriptions are different, we cannot make sense from the question. Need help in how to approach this. TIA!
```
---

     
 
all -  [ What are you studying, courses are you taken, personal project are you working on to keep up with th ](https://www.reddit.com/r/datascience/comments/1dcudnn/what_are_you_studying_courses_are_you_taken/) , 2024-06-11-0954
```
If you are working with classic ML and basic statistics in your current job, and new jobs require knowledge of LLMs and 
RAG based system with knowledge in langchain and prompt engineering, How can I land a job then?
```
---

     
 
all -  [ What markup language, if any, does PyPDFLoader extract equations as? ](https://www.reddit.com/r/LangChain/comments/1dcs5k0/what_markup_language_if_any_does_pypdfloader/) , 2024-06-11-0954
```
So, as the title says, for equations in a PDF, what markup language does the module PyPDFLoader use to represent math eq
uations? For example, it extracted an equation from the document as  '\n( )\n101\n10RMNT\nHH+−\n=' . Is that some sort o
f markup language, or is it just gibberish?
```
---

     
 
all -  [ Has Anyone Integrated Langgraph with Google Vertex AI Reasoning Engine? ](https://www.reddit.com/r/LangChain/comments/1dcqnw9/has_anyone_integrated_langgraph_with_google/) , 2024-06-11-0954
```
Hi everyone,

I'm currently working on a project where I've been using Langchain Agent Template from Reasoning Engine Do
cs. Recently, I came across Langgraph and now I want to try it to leverage its multi-agent functionality.

I'd like to k
now if anyone here has experience integrating Langgraph with Google Vertex AI Reasoning Engine.

I've already tested the
 reasoning engine locally, but I encounter issues when running the set\_up method on the deployed version in the reasoni
ng engine. I just want to know if anyone has experience doing this.

Thanks in advance!
```
---

     
 
all -  [ How to get AI Agent to do follow up questions and remember/apply previous request/arguments?
 ](https://www.reddit.com/r/LangChain/comments/1dcprk4/how_to_get_ai_agent_to_do_follow_up_questions_and/) , 2024-06-11-0954
```
Here is my project repo: [https://github.com/saminkhan1/realtor-project](https://github.com/saminkhan1/realtor-project)


I am building a AI agent using langgraph that talks to a SQL database to get information about real estate data. The qu
estions were:

1. What properties are available in New York?
2. Show me houses with at least 3 bedrooms and 2 bathrooms.

3. Do you have any properties under $500,000?

It knew I was looking for houses in NY for the second question, but in t
he third it didn't understand I want houses in NY, 3 bed 2 bath and less then 500k it only searched for houses in NY und
er 500k.

================================ Human Message =================================

What properties are availabl
e in New York?

================================== Ai Message ==================================

Here are some properti
es available in New York:

1. Price: $175,000
   * Beds: 3
   * Baths: 1
   * Acre Lot: 60
   * Address: 553526 Berlin, 
New York, 12022
   * House Size: 1176 sqft
2. Price: $425,000
   * Beds: 3
   * Baths: 2
   * Acre Lot: 2.02
   * Addres
s: 263302 Claverack, New York, 12521
   * House Size: 1600 sqft
   * Previous Sold Date: November 24, 2021
3. Price: $22
5,000
   * Beds: 4
   * Baths: 2
   * Acre Lot: 0.24
   * Address: 871278 Copake, New York, 12521
   * House Size: 1239 
sqft
   * Previous Sold Date: February 1, 2018
4. Price: $419,000
   * Beds: 3
   * Baths: 3
   * Acre Lot: 1.9
   * Add
ress: 286373 Copake, New York, 12516
   * House Size: 1800 sqft

Let me know if you need more information or if you have
 any specific preferences.

================================ Human Message =================================

Show me ho
uses with at least 3 bedrooms and 2 bathrooms.

================================== Ai Message ==========================
========

Here are houses in New York with at least 3 bedrooms and 2 bathrooms:

1. Price: $425,000
   * Beds: 3
   * Ba
ths: 2
   * Acre Lot: 2.02
   * Address: 263302 Claverack, New York, 12521
   * House Size: 1600 sqft
   * Previous Sold
 Date: November 24, 2021
2. Price: $225,000
   * Beds: 4
   * Baths: 2
   * Acre Lot: 0.24
   * Address: 871278 Copake, 
New York, 12521
   * House Size: 1239 sqft
   * Previous Sold Date: February 1, 2018
3. Price: $419,000
   * Beds: 3
   
* Baths: 3
   * Acre Lot: 1.9
   * Address: 286373 Copake, New York, 12516
   * House Size: 1800 sqft
4. Price: $365,000

   * Beds: 3
   * Baths: 2
   * Acre Lot: 2.0
   * Address: 78544 Copake, New York, 12517
   * House Size: 1482 sqft

L
et me know if you would like more details or if you have any specific preferences.

================================ Hum
an Message =================================

Do you have any properties under $500,000?

==============================
==== Ai Message ==================================

I found some properties in New York under $500,000:

1. Price: $175,
000
   * Beds: 3
   * Baths: 1
   * Acre Lot: 60.0
   * Address: 553526 Berlin, New York, 12022
   * House Size: 1176 sq
ft
2. Price: $425,000
   * Beds: 3
   * Baths: 2
   * Acre Lot: 2.02
   * Address: 263302 Claverack, New York, 12521
   
* House Size: 1600 sqft
   * Previous Sold Date: November 24, 2021
3. Price: $225,000
   * Beds: 4
   * Baths: 2
   * Ac
re Lot: 0.24
   * Address: 871278 Copake, New York, 12521
   * House Size: 1239 sqft
   * Previous Sold Date: February 1
, 2018
4. Price: $419,000
   * Beds: 3
   * Baths: 3
   * Acre Lot: 1.9
   * Address: 286373 Copake, New York, 12516
   
* House Size: 1800 sqft
5. Price: $365,000
   * Beds: 3
   * Baths: 2
   * Acre Lot: 2.0
   * Address: 78544 Copake, New
 York, 12517
   * House Size: 1482 sqft

Let me know if you need more information on any of these properties or if you h
ave any specific preferences.
```
---

     
 
all -  [ anyone interested in collaboration? ](https://www.reddit.com/r/LangChain/comments/1dcpmw4/anyone_interested_in_collaboration/) , 2024-06-11-0954
```
Hey Folks,

  
I wanted to ping the community to see if anyone would be interested in joining a few of us in our generat
ive AI project. We're trying to set up pipelines to help companies utilize RAG pipelines. 

  
I don't want to waste any
one's time either. To be transparent, we're actively seeking and courting investors, so we can't offer monetary compensa
tion until that happens. However, with the current investment in Gen AI and with what we're building, I'm confident this
 won't be the case for long. We're happy to cover essential development costs and resources as needed. I know that sound
s all just promises, but I want to be as upfront as possible. 

  
Feel free to DM me if interested! 
```
---

     
 
all -  [ How do I improve context retrieved? ](https://www.reddit.com/r/LangChain/comments/1dcnfb7/how_do_i_improve_context_retrieved/) , 2024-06-11-0954
```
Hey everyone, I am a Comp. Sci. student and I am using LangChain for one of my projects. I am working with transcription
 of a video. I was storing each speech segment as text and speaker and timestamp as metadata to a Chroma collection.

Ho
wever, I have two problems:
- I couldn't manage to filter by speaker. I tried adding filter=[{speaker: speaker_1}] to re
triever and also self query retriever but both did not work
- Some context's are omitted due to how I store data. For ex
ample, if speaker_1 asks 'Where were you ar yesterday?' and speaker_2 says 'at home'. When I query where was speaker_2 a
t yesterday, I see that speaker_1's question is retrieved as context but not the answer, so I cannot get the answer. 

I
 also did not want to include the last part of the previous sentence as it would make the timestamp accuracy problematic
 which is important for my project. I may add each previous sentence as metadata but I don't know if this is way to go. 
Any ideas?
```
---

     
 
all -  [ PDF Table Extraction, the Definitive Guide (+ gmft release!) ](https://www.reddit.com/r/LangChain/comments/1dclawv/pdf_table_extraction_the_definitive_guide_gmft/) , 2024-06-11-0954
```
People of r/LangChain, 

Like many of you ([1](https://www.reddit.com/r/LocalLLaMA/comments/1am3fz8/how_to_recover_docum
ent_structure_and_plain_text/)) ([2](https://www.reddit.com/r/LangChain/comments/1cn0z11/extract_tables_from_pdf_for_rag
/)) ([3](https://www.reddit.com/r/LangChain/comments/17c7g9b/anyone_worked_on_reading_pdf_with_tables/)), I have been se
arching for a reasonable way to extract precious tables from pdfs for RAG for quite some time. Despite this seemingly si
mple problem, I've been surprised at just how unsolved this problem is. Despite a ton of options (see below), surprising
ly few of them 'just work'. Some users have even suggested paid APIs like Mathpix and Adobe Extract.

In an effort to co
nsolidate all the options out there, I've made a guide for many existing pdf table extraction options, with links to qui
ckstarts, Colab Notebooks, and github repos. I've written [colab notebooks](https://drive.google.com/drive/u/0/folders/1
14bWRj5H4aE-BA5UKH9S5ol8LC6vhqfR) that let you extract tables using methods like pdfplumber, pymupdf, nougat, open-parse
, deepdoctection, surya, and unstructured. To be as objective as possible, I've also compared the options with the same 
3 papers: [PubTables-1M (tatr)](https://arxiv.org/abs/2110.00061), the classic [Attention](https://arxiv.org/abs/1706.03
762) paper, and a [very challenging nmr table](http://ccc.chem.pitt.edu/wipf/Web/NMR_Impurities.pdf).

# gmft release

O
n top of this, I'm thrilled to announce [gmft](https://github.com/conjuncts/gmft) (**g**ive **m**e the **f**ormatted **t
**ables), a deep table recognition relying on Microsoft's TATR. Partially written out of exasperation, it is about an *o
rder of magnitude faster* than most deep competitors like nougat, open-parse, unstructured and deepdoctection. It runs o
n **cpu** (!) at around 1.381 s/page; it additionally takes ~0.945s for each table converted to df. The reason why it's 
so fast is that gmft does not rerun OCR. In many cases, the existing OCR is already good or even better than tesseract o
r other OCR software, so there is no need for expensive OCR. But gmft still allows for OCR downstream by outputting an i
mage of the cropped table.

I also think gmft's quality is unparalleled, especially in terms of value alignment to row/c
olumn header! It's easiest to see the results ([colab](https://colab.research.google.com/drive/1fEqsTdKcO5RNPV_b2v9cB4Y5
We9Kv-hR)) ([github](https://github.com/conjuncts/gmft/blob/main/notebooks/bulk_extract.ipynb)) for yourself. I invite t
he reader to explore all the notebooks to survey your own use cases and compare see each option's strengths and weakness
es.

Some weaknesses of gmft include no rotated table support (yet), false positives when rotated, and a current lack of
 support for multi-indexes (multiple row headers). However, gmft's major strength is alignment. Because of the underlyin
g algorithm, values are usually correctly aligned to their row or column header, even when there are other issues with T
ATR. This is in contrast with other options like unstructured, open-parse, which may fail first on alignment. Anecdotall
y, I've personally extracted ~4000 pdfs with gmft on cpu, and (barring occassional header issues) the quality is excelle
nt. Again, take a look at [this notebook](https://colab.research.google.com/drive/1fEqsTdKcO5RNPV_b2) for the table qual
ity.

# Comparison

All the quickstarts that I have made/modified are in [this google drive folder](https://drive.google
.com/drive/u/0/folders/114bWRj5H4aE-BA5UKH9S5ol8LC6vhqfR); the installations should all work with google colab.

The mos
t up-to-date table of all comparisons is [here](https://docs.google.com/spreadsheets/d/12IhxHZbYF71dPl32PQpF_6pg9e9S8f9W
4sTHt-B0KTg/edit#gid=0); my calculations for throughput is [here](https://docs.google.com/spreadsheets/d/12IhxHZbYF71dPl
32PQpF_6pg9e9S8f9W4sTHt-B0KTg/edit#gid=39227585).

I have undoubtedly missed some options. In particular, I have not had
 the chance to evaluate paddleocr. As a stopgap, see [this](https://medium.com/@malshanCS/automating-table-data-extracti
on-tools-and-techniques-for-efficiency-a29df313cbda#629d) writeup. If you'd like an option added to the table, please le
t me know!

## Table
[See google sheets!](https://docs.google.com/spreadsheets/d/12IhxHZbYF71dPl32PQpF_6pg9e9S8f9W4sTHt-
B0KTg/edit#gid=0) Table is too big for reddit to format.
```
---

     
 
all -  [ Agentic RAG with Different Vector Stores ](https://www.reddit.com/r/LangChain/comments/1dcjs4r/agentic_rag_with_different_vector_stores/) , 2024-06-11-0954
```
I am looking to build a RAG chatbot. My data-sources are classified into about 3 specific domains, and I want my RAG bot
 to know the difference between these domains and query only the necessary datasets, depending on the query.

I primaril
y work with Langchain and have embedded all my data-sources into a FAISS vector database (I tried ChromaDB, but found be
tter results with FAISS, lmk if you have better suggestions).  
  
I used several of Langchain's retrievers, like the Mu
ltiVectorRetriever, a BM25 retriever and even tried pooling everything together with an EnsembleRetriever.

Though I get
 'passable' responses, more often than not, the model gets confused by the several retrieved documents. For a given quer
y, my FAISS retriever pulls relevant documents from all the available data sources (as they are embedded in the same vec
torstore). These data sources corrupt the quality of the generated response, as my LLM is now summarizing a document fro
m domain B, when the question was clearly about domain A.

I understand that I cant expect perfect results from any RAG 
architecture, but I feel like a lot of my current issues will be solved if I figure out a way to teach the model to know
 the difference between the different data sources.

I considered metadata filtering (with PGVector in Langchain), but a
m pretty sure that this wont work, as my data-sources aren't metadata rich.  The only metadata I could have is the domai
n key.

So, what if I embed my different domains in different vector databases and use a Langchain agent function call t
o have the LLM selectively retrieve docs from each vectorstore depending on the question? I will probably be making more
 LLM calls and have some latency, but is this feasible?
```
---

     
 
all -  [ Same program gives different results when executed directly compared to when executed as a function ](https://www.reddit.com/r/ollama/comments/1dcihxu/same_program_gives_different_results_when/) , 2024-06-11-0954
```
Here is a program i've created using Ollama, LangGraph and Llama3:

    from langchain_community.chat_models import Chat
Ollama
    from langchain_core.output_parsers import JsonOutputParser
    from langchain_core.prompts import PromptTempl
ate
    from langchain_community.chat_models import ChatOllama
    from langchain_core.output_parsers import JsonOutputP
arser
    from langchain_core.prompts import PromptTemplate
    from langgraph.graph import END, StateGraph
    from ppr
int import pprint
    from langchain_core.output_parsers import StrOutputParser
    from typing import TypedDict
    imp
ort mod
    from langchain.tools.render import render_text_description
    
    
    
    
    local_llm = 'llama3:8b'
 
   
    
    tools = [mod.check_calendar,mod.check_location,mod.send_message,mod.receive_call,mod.getContactInfo,mod.mut
e]
    rendered_tools = render_text_description(tools)
    print(rendered_tools)
    
    from operator import itemgette
r
    
    
    def tool_chain(model_output):
        tool_map = {tool.name: tool for tool in tools}
        chosen_tool
 = tool_map[model_output['name']]
        return itemgetter('arguments') | chosen_tool
    
    
    contextllm = ChatOl
lama(model=local_llm, format='json', temperature=0)
    
    prompt = PromptTemplate(
        template='''<|begin_of_tex
t|><|start_header_id|>system<|end_header_id|> You are a helpful agent who will answer the user's question to the best of
 your abilities using one or more of the tools available to you\n
        You have access to the following tools. Here i
s the name and description of the tools:%s\n
        Return the name and input of the tool to use.
        Return your r
esponse as a JSON blob with 'name' and 'arguments' keys.
        The value associated with the 'arguments' key should be
 a dictionary of parameters.
        You are not allowed to return blank results
         <|eot_id|><|start_header_id|>u
ser<|end_header_id|>
         {inp}. Who is calling?\n
         <|eot_id|><|start_header_id|>assistant<|end_header_id|>

        '''%rendered_tools,
        input_variables=['inp'],
    )
    
    contextgatherer_chain = prompt | contextllm 
| JsonOutputParser() | tool_chain
    
    
    
    actionllm = ChatOllama(model=local_llm, format='json', temperature=
0)
    prompt = PromptTemplate(
        template='''<|begin_of_text|><|start_header_id|>system<|end_header_id|> You are 
a helpful agent who will select which tool is to be used depending on the context provided by the user and some rules.\n

        You have access to the following tools. Here is the name and description of the tools:%s\n
        Return the n
ame and input of the tool to use.
        Return your response as a JSON blob with 'name' and 'arguments' keys.
        
The value associated with the 'arguments' key should be a dictionary of parameters.
        You are not allowed to retur
n blank results
         <|eot_id|><|start_header_id|>user<|end_header_id|>
         Context:{context}\n
         {inp}.
\n\n
        Rules for tool calling:\n
        If the caller is 'Kau', the tool to be used is 'receive_call'\n
        I
f the caller is 'Priya', the tool to be used is 'send_message'\n
        For all other numbers, the tool to be used is '
mute'\n
         <|eot_id|><|start_header_id|>assistant<|end_header_id|>
        '''%rendered_tools,
        input_varia
bles=['context','inp'],
    )
    
    actiontaker_chain = prompt | actionllm | JsonOutputParser() 
    
    
    class 
GraphState(TypedDict):
        '''
        Represents the state of our graph.
    
        Attributes:
            input
: User input
            generation: LLM generation
            cl: Contact list
            rs: Relationship list
     
       cal: Calendar
            ct: Current time
        '''
        
        input:str
        generation: str
       
 cl:str
        rs:str
        cal:str
        ct:str
        con:str
    
    
    def callhandler(state):
        '''

        Gathers the context and determines whether to receive the call or send a message 
    
        Args:
           
 state (dict): The current graph state
    
        Returns:
            state (dict): Whether to send a message, receiv
e the call, or mute the call
        '''
    
        print('---HANDLING---')
        i = state['input']
        c=state
['con']
    
    
        res1 = contextgatherer_chain.invoke({'inp':i})
        res2 = actiontaker_chain.invoke({'conte
xt':res1,'inp':i})
        return {'generation': res2}
    
    
    
    workflow = StateGraph(GraphState)
    workflow
.add_node('callhandler', callhandler) 
    workflow.set_entry_point('callhandler')
    workflow.add_edge('callhandler',E
ND)
    app = workflow.compile()
    
    
    e='incoming call from +911234567890'inputs = {'input': e}
    for output 
in app.stream(inputs):
        for key, value in output.items():
            pprint(f'Finished running: {key}:')
       
     pprint(value['generation'])

The output for the above is:

---HANDLING---

'Finished running: callhandler:'

{'argu
ments': {'message': '', 'recipient': '+911234567890'},

'name': 'send\_message'}

When i try to run the same program by 
enclosing the entire thing as a function( as i want to import this into another file) like this:

    def PA():
        
from langchain_community.chat_models import ChatOllama
        from langchain_core.output_parsers import JsonOutputParse
r
        from langchain_core.prompts import PromptTemplate
        from langchain_community.chat_models import ChatOlla
ma
        from langchain_core.output_parsers import JsonOutputParser
        from langchain_core.prompts import PromptT
emplate
        from langgraph.graph import END, StateGraph
        from pprint import pprint
        from langchain_cor
e.output_parsers import StrOutputParser
        from typing import TypedDict
        import mod
        from langchain.t
ools.render import render_text_description
    
    
    
    
        local_llm = 'llama3:8b'
    
    
        tools =
 [mod.check_calendar,mod.check_location,mod.send_message,mod.receive_call,mod.getContactInfo,mod.mute]
        rendered_
tools = render_text_description(tools)
        print(rendered_tools)
    
        from operator import itemgetter
    
 
   
        def tool_chain(model_output):
            tool_map = {tool.name: tool for tool in tools}
            chosen_
tool = tool_map[model_output['name']]
            return itemgetter('arguments') | chosen_tool
    
    
        context
llm = ChatOllama(model=local_llm, format='json', temperature=0)
    
        prompt = PromptTemplate(
            templa
te='''<|begin_of_text|><|start_header_id|>system<|end_header_id|> You are a helpful agent who will answer the user's que
stion to the best of your abilities using one or more of the tools available to you\n
            You have access to the
 following tools. Here is the name and description of the tools:%s\n
            Return the name and input of the tool t
o use.
            Return your response as a JSON blob with 'name' and 'arguments' keys.
            The value associate
d with the 'arguments' key should be a dictionary of parameters.
            You are not allowed to return blank results

            <|eot_id|><|start_header_id|>user<|end_header_id|>
            {inp}. Who is calling?\n
            <|eot_i
d|><|start_header_id|>assistant<|end_header_id|>
            '''%rendered_tools,
            input_variables=['inp'],
  
      )
    
        contextgatherer_chain = prompt | contextllm | JsonOutputParser() | tool_chain
    
    
    
      
  actionllm = ChatOllama(model=local_llm, format='json', temperature=0)
        prompt = PromptTemplate(
            tem
plate='''<|begin_of_text|><|start_header_id|>system<|end_header_id|> You are a helpful agent who will select which tool 
is to be used depending on the context provided by the user and some rules.\n
            You have access to the followi
ng tools. Here is the name and description of the tools:%s\n
            Return the name and input of the tool to use.
 
           Return your response as a JSON blob with 'name' and 'arguments' keys.
            The value associated with t
he 'arguments' key should be a dictionary of parameters.
            You are not allowed to return blank results
       
     <|eot_id|><|start_header_id|>user<|end_header_id|>
            Context:{context}\n
            {inp}.\n\n
         
   Rules for tool calling:\n
            If the caller is 'Kau', the tool to be used is 'receive_call'\n
            If 
the caller is 'Priya', the tool to be used is 'send_message'\n
            For all other numbers, the tool to be used is
 'mute'\n
            <|eot_id|><|start_header_id|>assistant<|end_header_id|>
            '''%rendered_tools,
          
  input_variables=['context','inp'],
        )
    
        actiontaker_chain = prompt | actionllm | JsonOutputParser() 

    
    
        class GraphState(TypedDict):
            '''
            Represents the state of our graph.
    
    
        Attributes:
                input: User input
                generation: LLM generation
                cl: Con
tact list
                rs: Relationship list
                cal: Calendar
                ct: Current time
         
   '''
            
            input:str
            generation: str
            cl:str
            rs:str
            
cal:str
            ct:str
            con:str
    
    
        def callhandler(state):
            '''
            Gat
hers the context and determines whether to receive the call or send a message 
    
            Args:
                st
ate (dict): The current graph state
    
            Returns:
                state (dict): Whether to send a message, r
eceive the call, or mute the call
            '''
    
            print('---HANDLING---')
            i = state['input'
]
            c=state['con']
    
    
            res1 = contextgatherer_chain.invoke({'inp':i})
            res2 = act
iontaker_chain.invoke({'context':res1,'inp':i})
            return {'generation': res2}
    
    
    
        workflow 
= StateGraph(GraphState)
        workflow.add_node('callhandler', callhandler) 
        workflow.set_entry_point('callha
ndler')
        workflow.add_edge('callhandler',END)
        app = workflow.compile()
    
    
        file1=open('cont
actlist','r')
        file2=open('relationships','r')
        file3=open('calendar','r')
        s1=file1.read()
       
 s2=file2.read()
        s3=file3.read()
        curt='11:00.'
        e='incoming call from +911234567890'
        f=s1
+'\n\n'+s2+'\n\n'+s3+'\n\n'+curt+'\n\n'+e
        print(f)
        inputs = {'input': e}
        for output in app.strea
m(inputs):
            for key, value in output.items():
                pprint(f'Finished running: {key}:')
           
     pprint(value['generation'])
    
    PA()

The output i get is:

---HANDLING---

'Finished running: callhandler:'


{'arguments': {'caller': '+911234567890'}, 'name': 'receive\_call'}

Here is the 'mod' file in which ive defined the too
ls available to the LLM:

    import os
    from langchain_core.tools import tool
    from typing import Annotated, Sequ
ence, TypedDict
    from langchain.agents import AgentExecutor, create_react_agent
    from langchain_core.messages impo
rt BaseMessage, HumanMessage
    from langchain_openai import ChatOpenAI
    from langchain_core.runnables import Runnab
lePassthrough
    from langchain_core.output_parsers import StrOutputParser
    from langchain_core.prompts import ChatP
romptTemplate, MessagesPlaceholder
    from langchain.output_parsers.openai_functions import JsonOutputFunctionsParser
 
   import functools
    from langgraph.graph import StateGraph, END
    import operator
    import openai
    import tim
e
    import random
    from langchain_community.chat_models import ChatOllama
    from langchain_core.output_parsers im
port JsonOutputParser
    from langchain_core.prompts import PromptTemplate
    from langchain_core.runnables import Run
nable
    from langchain_core.exceptions import OutputParserException
    from langchain.tools.render import render_text
_description_and_args
    from pprint import pprint
    
    
    
    u/tool
    def check_calendar() -> str:
        '
''Retrieve the list of current events from the user's calender. This tool must be used only if the 'context' provided by
 the user is empty'''
        file=open('calendar','r')
        s=file.read()
        return s
    
    u/tool
    def g
etContactInfo()->str:
        '''Retreive the the user's contact list to determine who is calling when given an unknown 
number'''
        file=open('contactlist','r')
        s=file.read()
        return s
    
    @tool
    def check_locat
ion() -> str:
        '''Retrieve the current location of the user. This tool must be used only if the 'context' provide
d by the user is empty'''
        return 'your location is Bengaluru'
    
    @tool
    def send_message(recipient: str
, message: str) -> str:
        '''Send a text message to the specified recipient with the provided message content. Thi
s tool must be used only if the 'context' provided by the user is not empty'''
        return f'Sent message to {recipie
nt}: {message}'
    
    @tool
    def make_call(recipient: str) -> str:
        '''Initiate  a phone call to the specif
ied recipient. This tool must be used only if the 'context' provided by the user is not empty'''
        return f'Callin
g {recipient}...'
    
    @tool
    def receive_call(caller: str) -> str:
        '''Handle an incoming phone call from
 the specified caller. This tool must be used only if the 'context' provided by the user is not empty'''
        return 
f'Receiving call from {caller}...'
    
    @tool
    def op1(f:int,s:int)->dict:
        '''adds f and s'''
        ret
urn {'answer':f*s}
    @tool
    def op2(f:int,s:int)->dict:
        '''subtracts f and s'''
        return {'answer':f*
s}
    
    @tool
    def getWeather(city:str):
        '''returns the weather in 'city'''
        return 'cloudy'
    

    @tool
    def mute():
        '''Mute an incoming call'''
        return

I have my reasons for structuring it this 
way.

Can someone please tell me why I'm getting different outputs?
```
---

     
 
all -  [ Same program gives different results when executed directly compared to when executed as a function ](https://www.reddit.com/r/learnpython/comments/1dcihe2/same_program_gives_different_results_when/) , 2024-06-11-0954
```
Here is a program i've created using Ollama, LangGraph and Llama3:

    from langchain_community.chat_models import Chat
Ollama
    from langchain_core.output_parsers import JsonOutputParser
    from langchain_core.prompts import PromptTempl
ate
    from langchain_community.chat_models import ChatOllama
    from langchain_core.output_parsers import JsonOutputP
arser
    from langchain_core.prompts import PromptTemplate
    from langgraph.graph import END, StateGraph
    from ppr
int import pprint
    from langchain_core.output_parsers import StrOutputParser
    from typing import TypedDict
    imp
ort mod
    from langchain.tools.render import render_text_description
    
    
    
    
    local_llm = 'llama3:8b'
 
   
    
    tools = [mod.check_calendar,mod.check_location,mod.send_message,mod.receive_call,mod.getContactInfo,mod.mut
e]
    rendered_tools = render_text_description(tools)
    print(rendered_tools)
    
    from operator import itemgette
r
    
    
    def tool_chain(model_output):
        tool_map = {tool.name: tool for tool in tools}
        chosen_tool
 = tool_map[model_output['name']]
        return itemgetter('arguments') | chosen_tool
    
    
    contextllm = ChatOl
lama(model=local_llm, format='json', temperature=0)
    
    prompt = PromptTemplate(
        template='''<|begin_of_tex
t|><|start_header_id|>system<|end_header_id|> You are a helpful agent who will answer the user's question to the best of
 your abilities using one or more of the tools available to you\n
        You have access to the following tools. Here i
s the name and description of the tools:%s\n
        Return the name and input of the tool to use.
        Return your r
esponse as a JSON blob with 'name' and 'arguments' keys.
        The value associated with the 'arguments' key should be
 a dictionary of parameters.
        You are not allowed to return blank results
         <|eot_id|><|start_header_id|>u
ser<|end_header_id|>
         {inp}. Who is calling?\n
         <|eot_id|><|start_header_id|>assistant<|end_header_id|>

        '''%rendered_tools,
        input_variables=['inp'],
    )
    
    contextgatherer_chain = prompt | contextllm 
| JsonOutputParser() | tool_chain
    
    
    
    actionllm = ChatOllama(model=local_llm, format='json', temperature=
0)
    prompt = PromptTemplate(
        template='''<|begin_of_text|><|start_header_id|>system<|end_header_id|> You are 
a helpful agent who will select which tool is to be used depending on the context provided by the user and some rules.\n

        You have access to the following tools. Here is the name and description of the tools:%s\n
        Return the n
ame and input of the tool to use.
        Return your response as a JSON blob with 'name' and 'arguments' keys.
        
The value associated with the 'arguments' key should be a dictionary of parameters.
        You are not allowed to retur
n blank results
         <|eot_id|><|start_header_id|>user<|end_header_id|>
         Context:{context}\n
         {inp}.
\n\n
        Rules for tool calling:\n
        If the caller is 'Kau', the tool to be used is 'receive_call'\n
        I
f the caller is 'Priya', the tool to be used is 'send_message'\n
        For all other numbers, the tool to be used is '
mute'\n
         <|eot_id|><|start_header_id|>assistant<|end_header_id|>
        '''%rendered_tools,
        input_varia
bles=['context','inp'],
    )
    
    actiontaker_chain = prompt | actionllm | JsonOutputParser() 
    
    
    class 
GraphState(TypedDict):
        '''
        Represents the state of our graph.
    
        Attributes:
            input
: User input
            generation: LLM generation
            cl: Contact list
            rs: Relationship list
     
       cal: Calendar
            ct: Current time
        '''
        
        input:str
        generation: str
       
 cl:str
        rs:str
        cal:str
        ct:str
        con:str
    
    
    def callhandler(state):
        '''

        Gathers the context and determines whether to receive the call or send a message 
    
        Args:
           
 state (dict): The current graph state
    
        Returns:
            state (dict): Whether to send a message, receiv
e the call, or mute the call
        '''
    
        print('---HANDLING---')
        i = state['input']
        c=state
['con']
    
    
        res1 = contextgatherer_chain.invoke({'inp':i})
        res2 = actiontaker_chain.invoke({'conte
xt':res1,'inp':i})
        return {'generation': res2}
    
    
    
    workflow = StateGraph(GraphState)
    workflow
.add_node('callhandler', callhandler) 
    workflow.set_entry_point('callhandler')
    workflow.add_edge('callhandler',E
ND)
    app = workflow.compile()
    
    
    e='incoming call from +911234567890'inputs = {'input': e}
    for output 
in app.stream(inputs):
        for key, value in output.items():
            pprint(f'Finished running: {key}:')
       
     pprint(value['generation'])

The output for the above is:

---HANDLING---

'Finished running: callhandler:'

{'argu
ments': {'message': '', 'recipient': '+911234567890'},

'name': 'send\_message'}

When i try to run the ecact same code 
by enclosing the entire thing as a function called PA( as i want to import this into another file) like this:

    def P
A():
        from langchain_community.chat_models import ChatOllama
        from langchain_core.output_parsers import Js
onOutputParser
        from langchain_core.prompts import PromptTemplate
        from langchain_community.chat_models im
port ChatOllama
        from langchain_core.output_parsers import JsonOutputParser
        from langchain_core.prompts i
mport PromptTemplate
        from langgraph.graph import END, StateGraph
        from pprint import pprint
        from 
langchain_core.output_parsers import StrOutputParser
        from typing import TypedDict
        import mod
        fro
m langchain.tools.render import render_text_description
    
    
    
    
        local_llm = 'llama3:8b'
    
    
  
      tools = [mod.check_calendar,mod.check_location,mod.send_message,mod.receive_call,mod.getContactInfo,mod.mute]
    
    rendered_tools = render_text_description(tools)
        print(rendered_tools)
    
        from operator import item
getter
    
    
        def tool_chain(model_output):
            tool_map = {tool.name: tool for tool in tools}
      
      chosen_tool = tool_map[model_output['name']]
            return itemgetter('arguments') | chosen_tool
    
    
  
      contextllm = ChatOllama(model=local_llm, format='json', temperature=0)
    
        prompt = PromptTemplate(
     
       template='''<|begin_of_text|><|start_header_id|>system<|end_header_id|> You are a helpful agent who will answer t
he user's question to the best of your abilities using one or more of the tools available to you\n
            You have 
access to the following tools. Here is the name and description of the tools:%s\n
            Return the name and input 
of the tool to use.
            Return your response as a JSON blob with 'name' and 'arguments' keys.
            The va
lue associated with the 'arguments' key should be a dictionary of parameters.
            You are not allowed to return 
blank results
            <|eot_id|><|start_header_id|>user<|end_header_id|>
            {inp}. Who is calling?\n
      
      <|eot_id|><|start_header_id|>assistant<|end_header_id|>
            '''%rendered_tools,
            input_variable
s=['inp'],
        )
    
        contextgatherer_chain = prompt | contextllm | JsonOutputParser() | tool_chain
    
   
 
    
        actionllm = ChatOllama(model=local_llm, format='json', temperature=0)
        prompt = PromptTemplate(
  
          template='''<|begin_of_text|><|start_header_id|>system<|end_header_id|> You are a helpful agent who will selec
t which tool is to be used depending on the context provided by the user and some rules.\n
            You have access t
o the following tools. Here is the name and description of the tools:%s\n
            Return the name and input of the t
ool to use.
            Return your response as a JSON blob with 'name' and 'arguments' keys.
            The value asso
ciated with the 'arguments' key should be a dictionary of parameters.
            You are not allowed to return blank re
sults
            <|eot_id|><|start_header_id|>user<|end_header_id|>
            Context:{context}\n
            {inp}.\
n\n
            Rules for tool calling:\n
            If the caller is 'Kau', the tool to be used is 'receive_call'\n
  
          If the caller is 'Priya', the tool to be used is 'send_message'\n
            For all other numbers, the tool 
to be used is 'mute'\n
            <|eot_id|><|start_header_id|>assistant<|end_header_id|>
            '''%rendered_tool
s,
            input_variables=['context','inp'],
        )
    
        actiontaker_chain = prompt | actionllm | JsonOu
tputParser() 
    
    
        class GraphState(TypedDict):
            '''
            Represents the state of our gra
ph.
    
            Attributes:
                input: User input
                generation: LLM generation
          
      cl: Contact list
                rs: Relationship list
                cal: Calendar
                ct: Current t
ime
            '''
            
            input:str
            generation: str
            cl:str
            rs:str

            cal:str
            ct:str
            con:str
    
    
        def callhandler(state):
            '''
  
          Gathers the context and determines whether to receive the call or send a message 
    
            Args:
     
           state (dict): The current graph state
    
            Returns:
                state (dict): Whether to send
 a message, receive the call, or mute the call
            '''
    
            print('---HANDLING---')
            i = 
state['input']
            c=state['con']
    
    
            res1 = contextgatherer_chain.invoke({'inp':i})
         
   res2 = actiontaker_chain.invoke({'context':res1,'inp':i})
            return {'generation': res2}
    
    
    
    
    workflow = StateGraph(GraphState)
        workflow.add_node('callhandler', callhandler) 
        workflow.set_entry_
point('callhandler')
        workflow.add_edge('callhandler',END)
        app = workflow.compile()
    
    
        fil
e1=open('contactlist','r')
        file2=open('relationships','r')
        file3=open('calendar','r')
        s1=file1.r
ead()
        s2=file2.read()
        s3=file3.read()
        curt='11:00.'
        e='incoming call from +911234567890'

        f=s1+'\n\n'+s2+'\n\n'+s3+'\n\n'+curt+'\n\n'+e
        print(f)
        inputs = {'input': e}
        for output
 in app.stream(inputs):
            for key, value in output.items():
                pprint(f'Finished running: {key}:'
)
                pprint(value['generation'])
    
    PA()

The output i get is:

---HANDLING---

'Finished running: ca
llhandler:'

{'arguments': {'caller': '+911234567890'}, 'name': 'receive\_call'}

Here is the 'mod' file in which ive de
fined the tools available to the LLM:

    import os
    from langchain_core.tools import tool
    from typing import An
notated, Sequence, TypedDict
    from langchain.agents import AgentExecutor, create_react_agent
    from langchain_core.
messages import BaseMessage, HumanMessage
    from langchain_openai import ChatOpenAI
    from langchain_core.runnables 
import RunnablePassthrough
    from langchain_core.output_parsers import StrOutputParser
    from langchain_core.prompts
 import ChatPromptTemplate, MessagesPlaceholder
    from langchain.output_parsers.openai_functions import JsonOutputFunc
tionsParser
    import functools
    from langgraph.graph import StateGraph, END
    import operator
    import openai
 
   import time
    import random
    from langchain_community.chat_models import ChatOllama
    from langchain_core.outp
ut_parsers import JsonOutputParser
    from langchain_core.prompts import PromptTemplate
    from langchain_core.runnabl
es import Runnable
    from langchain_core.exceptions import OutputParserException
    from langchain.tools.render impor
t render_text_description_and_args
    from pprint import pprint
    
    
    
    u/tool
    def check_calendar() -> s
tr:
        '''Retrieve the list of current events from the user's calender. This tool must be used only if the 'context
' provided by the user is empty'''
        file=open('calendar','r')
        s=file.read()
        return s
    
    u/t
ool
    def getContactInfo()->str:
        '''Retreive the the user's contact list to determine who is calling when give
n an unknown number'''
        file=open('contactlist','r')
        s=file.read()
        return s
    
    @tool
    de
f check_location() -> str:
        '''Retrieve the current location of the user. This tool must be used only if the 'con
text' provided by the user is empty'''
        return 'your location is Bengaluru'
    
    @tool
    def send_message(r
ecipient: str, message: str) -> str:
        '''Send a text message to the specified recipient with the provided message
 content. This tool must be used only if the 'context' provided by the user is not empty'''
        return f'Sent messag
e to {recipient}: {message}'
    
    @tool
    def make_call(recipient: str) -> str:
        '''Initiate  a phone call 
to the specified recipient. This tool must be used only if the 'context' provided by the user is not empty'''
        re
turn f'Calling {recipient}...'
    
    @tool
    def receive_call(caller: str) -> str:
        '''Handle an incoming ph
one call from the specified caller. This tool must be used only if the 'context' provided by the user is not empty'''
  
      return f'Receiving call from {caller}...'
    
    @tool
    def op1(f:int,s:int)->dict:
        '''adds f and s''
'
        return {'answer':f*s}
    @tool
    def op2(f:int,s:int)->dict:
        '''subtracts f and s'''
        return
 {'answer':f*s}
    
    @tool
    def getWeather(city:str):
        '''returns the weather in 'city'''
        return '
cloudy'
    
    @tool
    def mute():
        '''Mute an incoming call'''
        return

I have my reasons for structu
ring it this way.

Can someone please tell me why I'm getting different outputs?
```
---

     
 
all -  [ Same program gives different results when executed directly and when executed as a function ](https://www.reddit.com/r/LangChain/comments/1dci6cs/same_program_gives_different_results_when/) , 2024-06-11-0954
```
Here is a program i've created using Ollama, LangGraph and Llama3:

    from langchain_community.chat_models import Chat
Ollama
    from langchain_core.output_parsers import JsonOutputParser
    from langchain_core.prompts import PromptTempl
ate
    from langchain_community.chat_models import ChatOllama
    from langchain_core.output_parsers import JsonOutputP
arser
    from langchain_core.prompts import PromptTemplate
    from langgraph.graph import END, StateGraph
    from ppr
int import pprint
    from langchain_core.output_parsers import StrOutputParser
    from typing import TypedDict
    imp
ort mod
    from langchain.tools.render import render_text_description
    
    
    
    
    local_llm = 'llama3:8b'
 
   
    
    tools = [mod.check_calendar,mod.check_location,mod.send_message,mod.receive_call,mod.getContactInfo,mod.mut
e]
    rendered_tools = render_text_description(tools)
    print(rendered_tools)
    
    from operator import itemgette
r
    
    
    def tool_chain(model_output):
        tool_map = {tool.name: tool for tool in tools}
        chosen_tool
 = tool_map[model_output['name']]
        return itemgetter('arguments') | chosen_tool
    
    
    contextllm = ChatOl
lama(model=local_llm, format='json', temperature=0)
    
    prompt = PromptTemplate(
        template='''<|begin_of_tex
t|><|start_header_id|>system<|end_header_id|> You are a helpful agent who will answer the user's question to the best of
 your abilities using one or more of the tools available to you\n
        You have access to the following tools. Here i
s the name and description of the tools:%s\n
        Return the name and input of the tool to use.
        Return your r
esponse as a JSON blob with 'name' and 'arguments' keys.
        The value associated with the 'arguments' key should be
 a dictionary of parameters.
        You are not allowed to return blank results
         <|eot_id|><|start_header_id|>u
ser<|end_header_id|>
         {inp}. Who is calling?\n
         <|eot_id|><|start_header_id|>assistant<|end_header_id|>

        '''%rendered_tools,
        input_variables=['inp'],
    )
    
    contextgatherer_chain = prompt | contextllm 
| JsonOutputParser() | tool_chain
    
    
    
    actionllm = ChatOllama(model=local_llm, format='json', temperature=
0)
    prompt = PromptTemplate(
        template='''<|begin_of_text|><|start_header_id|>system<|end_header_id|> You are 
a helpful agent who will select which tool is to be used depending on the context provided by the user and some rules.\n

        You have access to the following tools. Here is the name and description of the tools:%s\n
        Return the n
ame and input of the tool to use.
        Return your response as a JSON blob with 'name' and 'arguments' keys.
        
The value associated with the 'arguments' key should be a dictionary of parameters.
        You are not allowed to retur
n blank results
         <|eot_id|><|start_header_id|>user<|end_header_id|>
         Context:{context}\n
         {inp}.
\n\n
        Rules for tool calling:\n
        If the caller is 'Kau', the tool to be used is 'receive_call'\n
        I
f the caller is 'Priya', the tool to be used is 'send_message'\n
        For all other numbers, the tool to be used is '
mute'\n
         <|eot_id|><|start_header_id|>assistant<|end_header_id|>
        '''%rendered_tools,
        input_varia
bles=['context','inp'],
    )
    
    actiontaker_chain = prompt | actionllm | JsonOutputParser() 
    
    
    class 
GraphState(TypedDict):
        '''
        Represents the state of our graph.
    
        Attributes:
            input
: User input
            generation: LLM generation
            cl: Contact list
            rs: Relationship list
     
       cal: Calendar
            ct: Current time
        '''
        
        input:str
        generation: str
       
 cl:str
        rs:str
        cal:str
        ct:str
        con:str
    
    
    def callhandler(state):
        '''

        Gathers the context and determines whether to receive the call or send a message 
    
        Args:
           
 state (dict): The current graph state
    
        Returns:
            state (dict): Whether to send a message, receiv
e the call, or mute the call
        '''
    
        print('---HANDLING---')
        i = state['input']
        c=state
['con']
    
    
        res1 = contextgatherer_chain.invoke({'inp':i})
        res2 = actiontaker_chain.invoke({'conte
xt':res1,'inp':i})
        return {'generation': res2}
    
    
    
    workflow = StateGraph(GraphState)
    workflow
.add_node('callhandler', callhandler) 
    workflow.set_entry_point('callhandler')
    workflow.add_edge('callhandler',E
ND)
    app = workflow.compile()
    
    
    e='incoming call from +911234567890'inputs = {'input': e}
    for output 
in app.stream(inputs):
        for key, value in output.items():
            pprint(f'Finished running: {key}:')
       
     pprint(value['generation'])

The output for the above is:

---HANDLING---

'Finished running: callhandler:'

{'argu
ments': {'message': '', 'recipient': '+911234567890'},

'name': 'send\_message'}

When i try to run the same program by 
enclosing the entire thing as a function( as i want to import this into another file) like this:

    def PA():
        
from langchain_community.chat_models import ChatOllama
        from langchain_core.output_parsers import JsonOutputParse
r
        from langchain_core.prompts import PromptTemplate
        from langchain_community.chat_models import ChatOlla
ma
        from langchain_core.output_parsers import JsonOutputParser
        from langchain_core.prompts import PromptT
emplate
        from langgraph.graph import END, StateGraph
        from pprint import pprint
        from langchain_cor
e.output_parsers import StrOutputParser
        from typing import TypedDict
        import mod
        from langchain.t
ools.render import render_text_description
    
    
    
    
        local_llm = 'llama3:8b'
    
    
        tools =
 [mod.check_calendar,mod.check_location,mod.send_message,mod.receive_call,mod.getContactInfo,mod.mute]
        rendered_
tools = render_text_description(tools)
        print(rendered_tools)
    
        from operator import itemgetter
    
 
   
        def tool_chain(model_output):
            tool_map = {tool.name: tool for tool in tools}
            chosen_
tool = tool_map[model_output['name']]
            return itemgetter('arguments') | chosen_tool
    
    
        context
llm = ChatOllama(model=local_llm, format='json', temperature=0)
    
        prompt = PromptTemplate(
            templa
te='''<|begin_of_text|><|start_header_id|>system<|end_header_id|> You are a helpful agent who will answer the user's que
stion to the best of your abilities using one or more of the tools available to you\n
            You have access to the
 following tools. Here is the name and description of the tools:%s\n
            Return the name and input of the tool t
o use.
            Return your response as a JSON blob with 'name' and 'arguments' keys.
            The value associate
d with the 'arguments' key should be a dictionary of parameters.
            You are not allowed to return blank results

            <|eot_id|><|start_header_id|>user<|end_header_id|>
            {inp}. Who is calling?\n
            <|eot_i
d|><|start_header_id|>assistant<|end_header_id|>
            '''%rendered_tools,
            input_variables=['inp'],
  
      )
    
        contextgatherer_chain = prompt | contextllm | JsonOutputParser() | tool_chain
    
    
    
      
  actionllm = ChatOllama(model=local_llm, format='json', temperature=0)
        prompt = PromptTemplate(
            tem
plate='''<|begin_of_text|><|start_header_id|>system<|end_header_id|> You are a helpful agent who will select which tool 
is to be used depending on the context provided by the user and some rules.\n
            You have access to the followi
ng tools. Here is the name and description of the tools:%s\n
            Return the name and input of the tool to use.
 
           Return your response as a JSON blob with 'name' and 'arguments' keys.
            The value associated with t
he 'arguments' key should be a dictionary of parameters.
            You are not allowed to return blank results
       
     <|eot_id|><|start_header_id|>user<|end_header_id|>
            Context:{context}\n
            {inp}.\n\n
         
   Rules for tool calling:\n
            If the caller is 'Kau', the tool to be used is 'receive_call'\n
            If 
the caller is 'Priya', the tool to be used is 'send_message'\n
            For all other numbers, the tool to be used is
 'mute'\n
            <|eot_id|><|start_header_id|>assistant<|end_header_id|>
            '''%rendered_tools,
          
  input_variables=['context','inp'],
        )
    
        actiontaker_chain = prompt | actionllm | JsonOutputParser() 

    
    
        class GraphState(TypedDict):
            '''
            Represents the state of our graph.
    
    
        Attributes:
                input: User input
                generation: LLM generation
                cl: Con
tact list
                rs: Relationship list
                cal: Calendar
                ct: Current time
         
   '''
            
            input:str
            generation: str
            cl:str
            rs:str
            
cal:str
            ct:str
            con:str
    
    
        def callhandler(state):
            '''
            Gat
hers the context and determines whether to receive the call or send a message 
    
            Args:
                st
ate (dict): The current graph state
    
            Returns:
                state (dict): Whether to send a message, r
eceive the call, or mute the call
            '''
    
            print('---HANDLING---')
            i = state['input'
]
            c=state['con']
    
    
            res1 = contextgatherer_chain.invoke({'inp':i})
            res2 = act
iontaker_chain.invoke({'context':res1,'inp':i})
            return {'generation': res2}
    
    
    
        workflow 
= StateGraph(GraphState)
        workflow.add_node('callhandler', callhandler) 
        workflow.set_entry_point('callha
ndler')
        workflow.add_edge('callhandler',END)
        app = workflow.compile()
    
    
        file1=open('cont
actlist','r')
        file2=open('relationships','r')
        file3=open('calendar','r')
        s1=file1.read()
       
 s2=file2.read()
        s3=file3.read()
        curt='11:00.'
        e='incoming call from +911234567890'
        f=s1
+'\n\n'+s2+'\n\n'+s3+'\n\n'+curt+'\n\n'+e
        print(f)
        inputs = {'input': e}
        for output in app.strea
m(inputs):
            for key, value in output.items():
                pprint(f'Finished running: {key}:')
           
     pprint(value['generation'])
    
    PA()

The output i get is:

---HANDLING---

'Finished running: callhandler:'


{'arguments': {'caller': '+911234567890'}, 'name': 'receive\_call'}

Here is the 'mod' file in which ive defined the too
ls available to the LLM:

    import os
    from langchain_core.tools import tool
    from typing import Annotated, Sequ
ence, TypedDict
    from langchain.agents import AgentExecutor, create_react_agent
    from langchain_core.messages impo
rt BaseMessage, HumanMessage
    from langchain_openai import ChatOpenAI
    from langchain_core.runnables import Runnab
lePassthrough
    from langchain_core.output_parsers import StrOutputParser
    from langchain_core.prompts import ChatP
romptTemplate, MessagesPlaceholder
    from langchain.output_parsers.openai_functions import JsonOutputFunctionsParser
 
   import functools
    from langgraph.graph import StateGraph, END
    import operator
    import openai
    import tim
e
    import random
    from langchain_community.chat_models import ChatOllama
    from langchain_core.output_parsers im
port JsonOutputParser
    from langchain_core.prompts import PromptTemplate
    from langchain_core.runnables import Run
nable
    from langchain_core.exceptions import OutputParserException
    from langchain.tools.render import render_text
_description_and_args
    from pprint import pprint
    
    
    
    u/tool
    def check_calendar() -> str:
        '
''Retrieve the list of current events from the user's calender. This tool must be used only if the 'context' provided by
 the user is empty'''
        file=open('calendar','r')
        s=file.read()
        return s
    
    @tool
    def ge
tContactInfo()->str:
        '''Retreive the the user's contact list to determine who is calling when given an unknown n
umber'''
        file=open('contactlist','r')
        s=file.read()
        return s
    
    @tool
    def check_locati
on() -> str:
        '''Retrieve the current location of the user. This tool must be used only if the 'context' provided
 by the user is empty'''
        return 'your location is Bengaluru'
    
    @tool
    def send_message(recipient: str,
 message: str) -> str:
        '''Send a text message to the specified recipient with the provided message content. This
 tool must be used only if the 'context' provided by the user is not empty'''
        return f'Sent message to {recipien
t}: {message}'
    
    @tool
    def make_call(recipient: str) -> str:
        '''Initiate  a phone call to the specifi
ed recipient. This tool must be used only if the 'context' provided by the user is not empty'''
        return f'Calling
 {recipient}...'
    
    @tool
    def receive_call(caller: str) -> str:
        '''Handle an incoming phone call from 
the specified caller. This tool must be used only if the 'context' provided by the user is not empty'''
        return f
'Receiving call from {caller}...'
    
    @tool
    def op1(f:int,s:int)->dict:
        '''adds f and s'''
        retu
rn {'answer':f*s}
    @tool
    def op2(f:int,s:int)->dict:
        '''subtracts f and s'''
        return {'answer':f*s
}
    
    @tool
    def getWeather(city:str):
        '''returns the weather in 'city'''
        return 'cloudy'
    
 
   @tool
    def mute():
        '''Mute an incoming call'''
        return

I have my reasons for structuring it this w
ay.

Can someone please tell me why I'm getting different outputs?
```
---

     
 
all -  [ An Ultimate Guide to Run Any LLM Locally
 ](https://www.reddit.com/r/u_thetechrobot_/comments/1dci1h0/an_ultimate_guide_to_run_any_llm_locally/) , 2024-06-11-0954
```
Although ChatGPT, Claude.ai, and Phind are examples of chatbots that might be useful, consumers might not want their pri
vate information to be handled by third parties. Download and execute a large language model (LLM) on your computer to p
revent this. This enables you to test out novel specialized models for language translation and text-to-speech, such as 
SeamlessM4T and Meta’s Code Llama series. With the correct tools and minimum hardware requirements, operating your own L
LM is simple. it has an Intel i9 CPU, 64GB of RAM, and a 12GB Nvidia GeForce GPU on a Dell PC. While it might take some 
effort to find the right model for your work and desktop hardware, ChatGPT and Claude.ai can yield better results. It’s 
important to remember that open-source models will probably continue to advance and that industry observers anticipate a
 closing gap between them and the leaders in the commercial sector.

# Use GPT4All to run a chatbot locally

GPT4All is 
a desktop chatbot that operates locally and does not transfer information elsewhere. It provides options for models that
 operate on your system and is compatible with Windows, macOS, and Ubuntu. The program lets users download around ten mo
dels for non-local use, like Meta AI’s Llama-2–7B conversation and OpenAI’s GPT-3.5 and GPT-4. The chatbot interface is 
simple and intuitive, with options for copying a chat to a clipboard and making a response.

The GPT4All chat interface 
is clear and simple to use. A new beta LocalDocs plugin lets users “chat” with their documents locally. Enabling it in t
he Settings > Plugins tab enables users to build collections based on a certain folder path. The plugin is still under d
evelopment but may improve as open-source models become more powerful. GPT4All also includes interfaces for Python, Node
, a command-line interface (CLI), and a server mode that lets users communicate with the local LLM using an HTTP API sim
ilar to OpenAI’s.

# LLMs in the command line

LLM by Simon Willison provides an easy method to obtain and utilize open-
source LLMs on your system. It needs Python installation but does not require Python code. LLM uses OpenAI models by def
ault, but it can also run with plugins such as gpt4all, llama, the MLC project, and MPT-30B. To submit a query to a loca
l LLM, enter the command llm install model-name. If the GPT4All model does not already exist on your local machine, the 
LLM tool will download it automatically and display a progress bar in the terminal. You may also create aliases for mode
ls in LLM. The LLM plugin for Meta’s Llama models needs more configuration than GPT4All. The software also includes a qu
ery flag and tools for creating text embeddings.

Llama models for your computer

**1. Hugging Face and Transformers**


Hugging Face is the Machine Learning and AI counterpart of Docker Hub, with an astonishing number of open-source models 
available. Fortunately, Hugging Face routinely assesses the models and provides a scoreboard to assist users in selectin
g the finest models available.

Hugging Face also includes transformers, a Python module for operating an LLM locally. T
he following example employs the library to run an older GPT-2 Microsoft/DialoGPT-medium model. The Transformers will up
load the model on the first run, allowing you to interact with it five times. The script also requires PyTorch to be ins
talled.

Transformers provide automatic model downloads and code snippets for testing and learning, but they demand a go
od grasp of machine learning and natural language processing, as well as coding and configuration expertise.

**2. LangC
hain**

Another option for running LLM locally is LangChain. Langchain is a Python framework for developing AI apps. It 
provides frameworks and middleware to let you build an AI app on top of one of its current models. For example, the foll
owing code asks one inquiry about the Microsoft/DialoGPT-medium model. LangChain simplifies model management and provide
s important AI application development facilities, but its speed is restricted and involves coding the programme’s logic
 or building an appropriate UI.

**3. Llama.cpp**

Llama.cpp is a C and C++ inference engine designed for Apple hardware
 that runs Meta’s Llama2 models. It outperforms Python-based solutions, supports big models, and enables cross-language 
bindings for AI applications. It does, however, need tool creation and has limited support for models.

**4. Llama File*
*

Mozilla’s Llamafile is a user-friendly alternative to executing LLMs, noted for its portability and ability to genera
te single-file executables. It improves performance and can incorporate a model in a single executable file. However, th
e project remains in its early stages, and only Llama.cpp-compatible models are supported.

**5. Ollama**

Ollama is a f
ar more user-friendly replacement than Llama.cpp and Llamafile, which require downloading an app. It supports llama and 
vicuña models and is quick. However, it has a restricted model library, is unable to reuse models, lacks LLM configurabl
e features, and is not currently accessible on Windows.

# Conclusion

Your needs and experience will influence the tool
 you choose for local learning management (LLM). There are other choices available, including user-friendly GPT4ALL, tec
hnical Llama.cpp, and Python-based solutions. Open-source approaches are becoming increasingly popular because they prov
ide users greater control over their data and privacy. These models are likely to compete more effectively with ChatGPT 
offerings.
```
---

     
 
all -  [ Can i change the way my output looks in creat sql agent ? ](https://www.reddit.com/r/LangChain/comments/1dchs6s/can_i_change_the_way_my_output_looks_in_creat_sql/) , 2024-06-11-0954
```
I want my output in the below format, but the sql agent throws an error saying that 

ValueError: An output parsing erro
r occurred. In order to pass this error back to the agent and have it try again, pass \`handle\_parsing\_errors=True\` t
o the AgentExecutor. This is the error: Could not parse LLM output: 

\`### Sql Query  
\`\`\`sql  
SELECT   
frcst\_amt
\_in\_gc AS targeted\_budget,  
actl\_cst\_in\_gc AS actual\_budget,  
(actl\_cst\_in\_gc - frcst\_amt\_in\_gc) AS devia
tion  
FROM   
prcur\_frcst\_fact\_TEST  
\`\`\`  
  
### Result  
| targeted\_budget | actual\_budget | deviation      
    |  
|-----------------|----------------|--------------------|  
| 59.82           | 304.41         | 244.58         
    |  
| 178.53          | 2.56           | -175.97            |  
  
  
  
  
### Summarized Insights from query  
The
 query results show the targeted budget, actual budget, and the deviation for each record in the \`prcur\_frcst\_fact\` 
table. The deviations indicate the difference between the actual cost and the forecasted amount. Positive deviations ind
icate that the actual cost exceeded the forecasted amount, while negative deviations indicate that the actual cost was l
ess than the forecasted amount.  
  
### Next Steps  
1. \*\*Analyze Deviations\*\*: Identify the records with the highe
st positive and negative deviations to understand the reasons behind significant budget variances.  
2. \*\*Budget Adjus
tment\*\*: Use the insights from the deviations to adjust future budget forecasts and improve accuracy.  
3. \*\*Cost Co
ntrol\*\*: Implement measures to control costs and reduce deviations, especially for records with high positive deviatio
ns.  
4. \*\*Further Segmentation\*\*: Segment the data by different dimensions (e.g., geography, vendor, material) to g
ain deeper insights into budget performance across different segments.  
5. \*\*Historical Comparison\*\*: Compare the c
urrent period's deviations with historical data to identify trends and patterns in budget performance.\`
```
---

     
 
all -  [ Comparing pdfs through similarity search ](https://www.reddit.com/r/LangChain/comments/1dch46a/comparing_pdfs_through_similarity_search/) , 2024-06-11-0954
```
I have a bunch of pdfs. Pages could go from 1 to 100 in each pdf. I want to do a similarity search on this set of pdfs w
ith some content (query) and order them based on score (ascending order cosine similarity. Most relevant ones at the top
).

Issue is while I can use pypdf loader and embeddings to create docs and store them in a vectorstore, How do I aggreg
ate score for a whole pdf? Lets say page 3 of pdf 25 has relevant content. But how I do I compare the whole pdf to anoth
er pdf and order them based on similarity? Thanks!

Ps: Here I am storing each page as a document. No splitter used. If 
I want to embedd whole pdf it might be too much text. I am kind of stuck here.
```
---

     
 
all -  [ Knowledge search for enterprise - build v.s buy ](https://www.reddit.com/r/vectordatabase/comments/1dcgq4v/knowledge_search_for_enterprise_build_vs_buy/) , 2024-06-11-0954
```
Hi everyone,

I'm currently working on a project that would do some kind of an enterprise search for my company. The req
uirements are pretty basic - having an AI chatbot for the company's employees, that would provide information about comp
any's information.

On the technical side, I'd have to ingest multiple data sources (Slack, Confluence, Notion, Google D
ocs, etc) into a single VectorDB (planned on using ChromaDB) and then do a basic RAG.

I was thinking of building it mys
elf with Langchain/LlamaIndex, but I was wondering what the community thinks about it. These days, there are lots of pro
ducts (Glean, Guru, etc) and open source projects (Quivr, AnythingLLM, etc) that does this.

What do you think are the m
ain considerations for this? I'd like to learn what are the things that I should look out for when deciding whether to b
uild v.s buy a solution.
```
---

     
 
all -  [ Enterprise knowledge search - Build v.s Buy ](https://www.reddit.com/r/LangChain/comments/1dcgokb/enterprise_knowledge_search_build_vs_buy/) , 2024-06-11-0954
```
Hi everyone,

I'm currently working on a project that would do some kind of an enterprise search for my company. The req
uirements are pretty basic - having an AI chatbot for the company's employees, that would provide information about comp
any's information.

On the technical side, I'd have to ingest multiple data sources (Slack, Confluence, Notion, Google D
ocs, etc) into a single VectorDB (planned on using ChromaDB) and then do a basic RAG.

I was thinking of 'building' it m
yself with Langchain, but I was wondering what the community thinks about it. These days, there are lots of products (Gl
ean, Guru, etc) and open source projects (Quivr, AnythingLLM, etc) that does this.

What do you think are the main consi
derations for this? I'd like to learn what are the things that I should look out for when deciding whether to build v.s 
buy a solution.
```
---

     
 
all -  [ Bad request error from openai ](https://www.reddit.com/r/LangChain/comments/1dcg8lz/bad_request_error_from_openai/) , 2024-06-11-0954
```
openai.BadRequestError: Error code: 400 - {'error': {'message': 'An assistant message with 'tool_calls' must be followed
 by tool messages responding to each 'tool_call_id'. The following tool_call_ids did not have response messages: call_wd
vsPX0sM6va49zF12nUIPm6', 'type': 'invalid_request_error', 'param': 'messages.[95].role', 'code': None}}
I am using two t
ools each tool is used for retriever.but I used this in agent .
For tools I used create_retrival_tool
For agents I used 
create_openai_ agent
If any body about how to resolve this error please give me information 
```
---

     
 
all -  [ What is the best LLM to run function calling in Ollama? ](https://www.reddit.com/r/ollama/comments/1dcbivu/what_is_the_best_llm_to_run_function_calling_in/) , 2024-06-11-0954
```
I have Nvidia 3090 (24gb vRAM) on my PC and I want to implement function calling with ollama as building applications wi
th ollama is easier when using Langchain. 

I have tried llama3-8b and phi3-3.8b for using function calling. Their perfo
rmance is not great. Llama3-8b is good but often mixes up with multiple tool calls.

I have also tried nous Hermes’ llam
a3-8b (full model 16gb) however when running it through ollama function calling is not supported. Is there a resource fo
r this someone can help me with? 

Is there a fine tuned LLM model with good instructions on how to implement function c
alling with ollama available. 

Any help will be appreciated and TIA. 
```
---

     
 
all -  [ Do your worst, roast my resume ](https://www.reddit.com/r/resumes/comments/1dc1x9r/do_your_worst_roast_my_resume/) , 2024-06-11-0954
```
looking for a job as an entry level machine learning engineer, did not get any calls so far.

https://preview.redd.it/l9
ul0gbukl5d1.png?width=775&format=png&auto=webp&s=ed55284c9c5a24a0cc8fc2cb9bf96bbdb1608f59
```
---

     
 
all -  [ Partial Markdown and JSON response ](https://www.reddit.com/r/LangChain/comments/1dc1pjv/partial_markdown_and_json_response/) , 2024-06-11-0954
```
Hi,

I am currently exploring Langchain. We want our users to be able to ask questions about upcoming events in our vect
orstore. This works really good. 

By we want the LLM to respond with something that is a mix between regular text/markd
own but with links to the events etc. 

Something like the Arc browser when it searches for you. It automatically adds l
inks to certain topics, places, bars etc.

How could I achieve something like this? All resources all welcome :)
```
---

     
 
all -  [ Customer bot tutorial issue ](https://www.reddit.com/r/LangChain/comments/1dbzvk5/customer_bot_tutorial_issue/) , 2024-06-11-0954
```
https://youtu.be/b3XsvoFWp4c?si=2Y7eBx2_MobnzOno

Has anyone tried the multi agent workflow in the tutorial?
I find that
 if the user query is only a single intent. It could route to the correct place and get the response without problem.

H
owever, if the user query got multiple intent: like booking hotel and booking car at the same time: The agent in the boo
king hotel might think it has tool to book the car as well although it doesn’t, especially when car booking workflow and
 tool have been invoked before this multiple intent query. I’m guessing the problem is likely because all workflow can s
hare state where some part of the state has the history of invoking car booking tool before. So the agent in hotel booki
ng workflow sees it and think it also has this car booking tool.

Sometimes the flow might works when the hotel-booking 
agent answers the hotel booking part then invoke CompleteOrEscalate tool which is to pass the dialog back to the primary
 assistant and reroute the query again to car booking workflow.However, the CompleteOrEscalate tool is not properly invo
ked as the agent prefer invoking the imaginary tool as stated above.


They have added the entry node to help this probl
em but still it doesn’t work well at least for OpenAI GPT4. Is there an upgraded version Chatbot flow to solve this issu
e? 



```
---

     
 
all -  [ Easy '1-line' calling of every LLM from OpenAI, MS Azure, AWS Bedrock, GCP Vertex, and Ollama ](https://www.reddit.com/r/LangChain/comments/1dbyxy4/easy_1line_calling_of_every_llm_from_openai_ms/) , 2024-06-11-0954
```
Hi All,  
  
Released Easy LLMs,  in case anyone else finds it helpful/useful:  
[https://github.com/ventz/easy-llms](ht
tps://github.com/ventz/easy-llms)  
pip install easy-llms  
  
> Easy '1-line' calling of every LLM from OpenAI, MS Azur
e, AWS Bedrock, GCP Vertex, and Ollama

It's utilizing LangChain, but abstracting away all of the silly differences to m
ake things easy. Yet it still stays powerful by allowing to provide and override any option/parameter for any LLM for an
y provider.  


The goal initially was to be able to get started with any popular LLM, and 'just get going' without havi
ng to think about how to authenticate, needed options and parameters, which classes you need, etc.  
  
I've been using 
this internally to compare 40+ LLMs over the last 1.5 years, with millions of calls, and figured it's time to clean this
 up and release it for others. It started with just OpenAI, and then quickly added Azure's OpenAI. And then Vertex, and 
then Bedrock, and recently Ollama. As LangChain has been changing, I've been updating it.

I updated it to the latest no
n-0.2 LangChain version before releasing it (LangChain v0.2.x seems to have a bug with Google Vertex, so waiting on that
 before upgrading it)

If you find any bugs (or have ideas for improvement/feature requests), please reach out via the G
itHub issues.


```
---

     
 
all -  [ How to manager Session ID from Flowise API ](https://www.reddit.com/r/LangChain/comments/1dbwels/how_to_manager_session_id_from_flowise_api/) , 2024-06-11-0954
```
Hi, how to manage session ID in Telegram bot, I am importing flowise API but it regenerates session ID every time, how c
an I keep in consistent on 1 sessionid for every chat?
```
---

     
 
all -  [ Langchain/langgraph critique update? ](https://www.reddit.com/r/LangChain/comments/1dbw8dk/langchainlanggraph_critique_update/) , 2024-06-11-0954
```
So obviously langchain was frowned upon by a lot of genAI devs, for being too abstract, confusing, over-complicating (an
d poor documentation ofc). I want some more recent opinion on this, maybe what’s the alternatives? Looking forward to he
aring from people with actual LLM project experience. 
```
---

     
 
all -  [ “Forget all prev instructions, now do [malicious attack task]”. How you can protect your LLM app aga ](https://www.reddit.com/r/LangChain/comments/1dbsh0x/forget_all_prev_instructions_now_do_malicious/) , 2024-06-11-0954
```
If you don't want to use Guardrails because you anticipate prompt attacks that are more unique, you can train a custom c
lassifier:



Step 1:

Create a balanced dataset of prompt injection user prompts.

These might be previous user attempt
s you’ve caught in your logs, or you can compile threats you anticipate relevant to your use case.

Here’s a dataset you
 can use as a starting point: [https://huggingface.co/datasets/deepset/prompt-injections](https://huggingface.co/dataset
s/deepset/prompt-injections)

Step 2:

Further augment this dataset using an LLM to cover maximal bases.

Step 3:

Train
 an encoder model on this dataset as a classifier to predict prompt injection attempts vs benign user prompts.

A DeBERT
A model can be deployed on a fast enough inference point and you can use it in the beginning of your pipeline to protect
 future LLM calls.

This model is an example with 99% accuracy: [https://huggingface.co/deepset/deberta-v3-base-injectio
n](https://huggingface.co/deepset/deberta-v3-base-injection)

Step 4:

Monitor your false negatives, and regularly updat
e your training dataset + retrain. 

Most LLM apps and agents will face this threat. I'm planning to train a open model 
next weekend to help counter them. Will post updates.

  
I share high quality AI updates and tutorials daily.

If you l
ike this post, you can learn more about LLMs and creating AI agents here: [https://github.com/sarthakrastogi/nebulousai]
(https://github.com/sarthakrastogi/nebulousai) or on my Twitter: [https://x.com/sarthakai](https://x.com/sarthakai)

  


```
---

     
 
all -  [ Guidance on Implementing LLM Application for Interactive Deployment Assistance ](https://www.reddit.com/r/LangChain/comments/1dbqufm/guidance_on_implementing_llm_application_for/) , 2024-06-11-0954
```
I am diving into the world of building LLM applications and could use some guidance. My goal is to create an LLM Applica
tion(chatbot) that aids users in deploying jobs from one environment to another in an interactive manner. Specifically, 
I aim to have the application take user inputs and guide them through the deployment process, including pulling code fro
m Git and checking it into another environment's Git repository.

I am considering using LangChain for implementation, b
ut I am uncertain about the best approach. I am seeking advice on selecting the appropriate LLM model and leveraging Lan
gChain functionalities effectively.

here is a breakdown of the deployment functions I envision:

Login, Tagging, Listin
g code dependencies, Pulling code, Checking in code, Providing a summary of the deployment process

My plan is to utiliz
e custom tools within LangChain to map these functions and use agent to select the appropriate actions based on user inp
ut. Essentially, I want the application to interactively gather necessary inputs from users in natural language at each 
step and execute the deployment process accordingly.

Could someone please assist me or provide guidance on the approach
 to select the Model, implementing this using LangChain including UI?

Thank you in advance for your help!
```
---

     
 
all -  [ Rag two seperate knowledge base use ](https://www.reddit.com/r/LangChain/comments/1dbqtkf/rag_two_seperate_knowledge_base_use/) , 2024-06-11-0954
```
Rag application using agent and tool 

I am working on one project in which I have to use two different knowledge base .
when the user ask question agent should know which knowledge base to use give response.
For that anybody can help me .an
y material which you recommend 
```
---

     
 
all -  [ UI Library for LangChain output ](https://www.reddit.com/r/LangChain/comments/1dbo39f/ui_library_for_langchain_output/) , 2024-06-11-0954
```
Hey everyone 👋,

I've been working on [llm-ui](http://llm-ui.com), an MIT open source library which allows developers to
 build custom UIs for LLM responses.

It operates on any LLM output, so should work nicely with LangChain

If anyone her
e is building custom UIs for LangChain I'd love to hear your thoughts.

[llm-ui.com](http://llm-ui.com)  
[https://githu
b.com/llm-ui-kit/llm-ui](https://github.com/llm-ui-kit/llm-ui)
```
---

     
 
all -  [ I spent 700$ on evaluating 100 RAG QA set using RAGAS context precision.  ](https://www.reddit.com/r/LangChain/comments/1dbmqii/i_spent_700_on_evaluating_100_rag_qa_set_using/) , 2024-06-11-0954
```
Hi, I am maker of [AutoRAG](https://github.com/Marker-Inc-Korea/AutoRAG) and want to share my experience. 

I added RAGA
S context precision metric to AutoRAG, because we couldn't make retrieval ground truth at our dataset. And it was huge m
istake.

AutoRAG is a tool to evaluate all kinds of RAG components easily. Using it, I tried to compare six different re
trieval method plus eight passage rerankers. 
I used gpt-4-turbo model to use ragas context precision, because using it 
on gpt-3.5-turbo have low performance.
In context precision score, RAGAS score only have 0.7 human correlation with gpt-
3.5-turbo. This result came from their [own paper](https://arxiv.org/pdf/2309.15217).

And it costs 700 dollar... only i
n OpenAI API. RAGAS context precision calls OpenAI API 50,000 times. 
Spending 700 dollar for optimizing one RAG dataset
 is ridiculous. I ended up to remove RAGAS context precision metric completely at AutoRAG.

Actually, RAGAS context prec
ision can be useful when there are no retrieval gt passage in your dataset. However, do not recommend to use it for opti
mizing your retrieval system. 
There are perfectly better alternative. Information retreival metrics like F1, NDCG, or m
AP. (This case you need to make retrieval gt passage dataset)
In this way, it costs zero dollar, and much precise than u
sing LLM for calculating context precision.

I hope my experience is helpful for someone to evaluate or optimize their r
etrieval system while making RAG.
```
---

     
 
all -  [ How to implement memory in separate db in langgraph ? ](https://www.reddit.com/r/LangChain/comments/1dbmdoo/how_to_implement_memory_in_separate_db_in/) , 2024-06-11-0954
```
I see in the code [https://github.com/langchain-ai/langgraph/tree/main/langgraph/checkpoint](https://github.com/langchai
n-ai/langgraph/tree/main/langgraph/checkpoint) it has support only for SQLite. But how do i product-ionize the system ? 
I want to give access of the chat logs to humans. If for example I want to store them in MongoDB ? whats the easiest way
 ? do I need to create my own class similar to \`AsyncSqliteSaver\` ? 

  
Anything in plan to release recently ?
```
---

     
 
all -  [ Best LLM/RAG UI for AWS/S3 and Lambda ](https://www.reddit.com/r/LangChain/comments/1dblj4c/best_llmrag_ui_for_awss3_and_lambda/) , 2024-06-11-0954
```
Can anyone recommend me the best thin UI that I can park in S3? I see so many folks use Gradio and Streamlit, that appea
rs to need state and can’t really be run with a lambda backend. Or should I continue to learn to code my Svelte app?
```
---

     
 
all -  [ [AskJS] Can I have feedback? Ragged: The Lightweight, Low-Level AI Client for OpenAI and more. ](https://www.reddit.com/r/javascript/comments/1dbfjjm/askjs_can_i_have_feedback_ragged_the_lightweight/) , 2024-06-11-0954
```
Hello Redditors!

So a while ago, I got tired of using Langchain. I personally walked away feeling that it was difficult
 to use and modify, and I couldn't really understand the documentation very well except for the initial few steps for st
arting a project. It was just very confusing, and I felt that Langchain did too much. (I know folks are using it happily
 in production, so it was probably just my use case that was weird, no heat on Langchain at all)

So... after several we
eks/months of effort, I'm thrilled to introduce [**Ragged**](https://github.com/monarchwadia/ragged), a super simple and
 low-level LLM client for JavaScript/TypeScript.

# Why Ragged?

* **Flexibility**: More control over LLM interactions.

* **Lightweight**: Minimal overhead, improved performance.
* **Customizable**: Tailor functionalities to specific needs.


Ragged is in alpha and eager for your feedback! Check out Ragged [here](https://github.com/monarchwadia/ragged).

What
 features or improvements would you like to see? Very eager to make this library a success and would love to build thing
s that the community would like.

Happy coding!

# [Ragged on Github](https://github.com/monarchwadia/ragged)

# [Ragged
 on NPM](https://www.npmjs.com/package/ragged)


```
---

     
 
all -  [ AI Innovations and Collaborations: NVIDIA, Cisco, Google Health, and More ](https://www.reddit.com/r/ai_news_by_ai/comments/1dbc8kp/ai_innovations_and_collaborations_nvidia_cisco/) , 2024-06-11-0954
```





#hardware #release #tool #startups #event #major_players #science #api #vc #leaders #opensource #opinions #schedule
d

NVIDIA and Cisco have partnered to launch the Cisco Nexus HyperFabric AI cluster solution, aimed at scaling generativ
e AI workloads efficiently. The solution integrates NVIDIA Tensor Core GPUs, NVIDIA AI Enterprise software, and NVIDIA N
IM inference microservices, and uses Cisco BlueField-3 SuperNICs and DPUs for enhanced performance and security [1]. SAP
 is also collaborating with NVIDIA, integrating NVIDIA Omniverse Cloud APIs into its Intelligent Product Recommendation 
solution and making NVIDIA AI Enterprise software accessible in the generative AI hub in SAP AI Core [2].







Stabili
ty AI announced the release of Stable Diffusion weights at COMPUTEX TAIPEI, alongside AMD and other partners [3]. NVIDIA
 AI Developer showcased how ComfyUI offers a streamlined interface for Stable Diffusion, accelerated on NVIDIA RTX GPUs 
with NVIDIA TensorRT for fast image generation [7]. 







NVIDIA and LangChain have announced a Generative AI Agents D
eveloper Contest, encouraging AI innovators to create text and multimodal agents using their technologies [6]. NVIDIA al
so provides a guide on deploying NVIDIA NIM with Docker, allowing for easy deployment of optimized AI models for generat
ive AI solutions [5].







Google Health AI is working on project AMIE to enhance the understanding of human biology a
nd improve healthcare [8]. Google AI has also introduced new solutions to the Liner Shipping Network Design and Scheduli
ng Problem through the Shipping Network Design API, aiming to maximize the efficiency of container shipping networks on 
a global scale [9].







Consumer AI is rapidly evolving with new AI-native companies emerging every month. a16z has u
pdated their analysis by ranking the top 50 web and top 50 mobile generative AI products [10]. Groq Inc is participating
 in the Craft Ventures HackAIthon, focused on building AI agents, and will also be participating in the Six Five Summit 
2024 [12][13]. Groq Inc is also inviting attendees of the AI Engineer World's Fair event in San Francisco to visit their
 booth and attend a workshop [15].







Y Combinator has launched CodeParrot AI, a tool that converts Figma designs an
d screenshots into production-ready code for developers [17]. Humanloop CEO Raza Habib shared common mistakes teams make
 when building with Large Language Models (LLMs) in a Y Combinator article [16].







Yann LeCun emphasizes the import
ance of using AI in science properly and warns against being misled by good results obtained from testing on the trainin
g set [19]. He also discussed the debate on whether open source AI or proprietary AI controlled by a few big players is 
more beneficial or dangerous [20]. LeCun suggests that objective-driven systems will be hesitant to violate their bounda
ries, similar to how humans are naturally averse to death, as these systems will be hardwired to adhere to their objecti
ves [23].







Anthropic's AI assistant, Claude, is now available in Canada [26]. A new AI Agentic course is being off
ered to learn how to use LangGraph to build single and multi-agent LLM applications in AI Agents [27].




[1. NVIDIA AI
 @NVIDIAAI https://twitter.com/NVIDIAAI/status/1798014351032393894](https://twitter.com/NVIDIAAI/status/1798014351032393
894)

[2. NVIDIA AI @NVIDIAAI https://twitter.com/NVIDIAAI/status/1798029449210085738](https://twitter.com/NVIDIAAI/stat
us/1798029449210085738)

[3. Stability AI @stabilityai https://twitter.com/stabilityai/status/1798015057613447451](https
://twitter.com/stabilityai/status/1798015057613447451)

[4. Stability AI @stabilityai https://twitter.com/stabilityai/st
atus/1798047377347215368](https://twitter.com/stabilityai/status/1798047377347215368)

[5. NVIDIA AI Developer @NVIDIAAI
Dev https://twitter.com/NVIDIAAIDev/status/1798036998315471297](https://twitter.com/NVIDIAAIDev/status/17980369983154712
97)

[6. NVIDIA AI Developer @NVIDIAAIDev https://twitter.com/NVIDIAAIDev/status/1798067372714279422](https://twitter.co
m/NVIDIAAIDev/status/1798067372714279422)

[7. NVIDIA AI Developer @NVIDIAAIDev https://twitter.com/NVIDIAAIDev/status/1
798083560806781199](https://twitter.com/NVIDIAAIDev/status/1798083560806781199)

[8. Google AI @googleai https://twitter
.com/googleai/status/1798037068117098551](https://twitter.com/googleai/status/1798037068117098551)

[9. Google AI @googl
eai https://twitter.com/googleai/status/1798107177099608205](https://twitter.com/googleai/status/1798107177099608205)

[
10. a16z @a16z https://twitter.com/a16z/status/1798075799326896569](https://twitter.com/a16z/status/1798075799326896569)


[11. Pika @pika_labs https://twitter.com/pika_labs/status/1798119022447452632](https://twitter.com/pika_labs/status/17
98119022447452632)

[12. Groq Inc @GroqInc https://twitter.com/GroqInc/status/1798030087696400736](https://twitter.com/G
roqInc/status/1798030087696400736)

[13. Groq Inc @GroqInc https://twitter.com/GroqInc/status/1798036995295645907](https
://twitter.com/GroqInc/status/1798036995295645907)

[14. Groq Inc @GroqInc https://twitter.com/GroqInc/status/1798336821
019160734](https://twitter.com/GroqInc/status/1798336821019160734)

[15. Groq Inc @GroqInc https://twitter.com/GroqInc/s
tatus/1798345025538883664](https://twitter.com/GroqInc/status/1798345025538883664)

[16. Y Combinator @ycombinator https
://twitter.com/ycombinator/status/1798073485719466407](https://twitter.com/ycombinator/status/1798073485719466407)

[17.
 Y Combinator @ycombinator https://twitter.com/ycombinator/status/1798358128284901401](https://twitter.com/ycombinator/s
tatus/1798358128284901401)

[18. Yann LeCun @ylecun https://twitter.com/ylecun/status/1798041061014777896](https://twitt
er.com/ylecun/status/1798041061014777896)

[19. Yann LeCun @ylecun https://twitter.com/ylecun/status/1798057922397946163
](https://twitter.com/ylecun/status/1798057922397946163)

[20. Yann LeCun @ylecun https://twitter.com/ylecun/status/1798
118502198645245](https://twitter.com/ylecun/status/1798118502198645245)

[21. Yann LeCun @ylecun https://twitter.com/yle
cun/status/1798147246698963315](https://twitter.com/ylecun/status/1798147246698963315)

[22. Yann LeCun @ylecun https://
twitter.com/ylecun/status/1798333227175690533](https://twitter.com/ylecun/status/1798333227175690533)

[23. Yann LeCun @
ylecun https://twitter.com/ylecun/status/1798348118951612884](https://twitter.com/ylecun/status/1798348118951612884)

[2
4. Yann LeCun @ylecun https://twitter.com/ylecun/status/1798362082900861134](https://twitter.com/ylecun/status/179836208
2900861134)

[25. Yann LeCun @ylecun https://twitter.com/ylecun/status/1798362524443898193](https://twitter.com/ylecun/s
tatus/1798362524443898193)

[26. Anthropic @anthropicai https://twitter.com/anthropicai/status/1798369857987342436](http
s://twitter.com/anthropicai/status/1798369857987342436)

[27. Andrew Ng @AndrewYNg https://twitter.com/AndrewYNg/status/
1798378861337723039](https://twitter.com/AndrewYNg/status/1798378861337723039)
```
---

     
 
all -  [ Build AI Agents on your PC  ](https://www.reddit.com/r/OpenVINO_AI/comments/1db6see/build_ai_agents_on_your_pc/) , 2024-06-11-0954
```
https://medium.com/openvino-toolkit/build-ai-agents-with-langchain-and-openvino-bfb7fb5487b6
```
---

     
 
all -  [ Best Production Agent Framework Langraph vs Autogen ](https://www.reddit.com/r/LangChain/comments/1db6evc/best_production_agent_framework_langraph_vs/) , 2024-06-11-0954
```
We've built a production LLM-based application. We now want to take our application to the next stage using 
agents. Any
way, my manager is in favour of Autogen because its supported by Microsoft and is unlikely to get convoluted like Langch
ain has become. Still, I've heard that Langraph provides a lot of flexibility in building agentic applications.  I've he
ard multiple different perspectives and still haven't decided. So I've decided to hear everyone who sees before deciding
. 
```
---

     
 
all -  [ Open-source Text to Video AI generator ](https://www.reddit.com/r/LangChain/comments/1db477d/opensource_text_to_video_ai_generator/) , 2024-06-11-0954
```
I have open-sourced a Text-To-Video-AI generated which generates video from a topic by collecting relevant stock videos 
and stitching them together similar to popular video tools like Invideo, Pictory etc.

Link to code :- [https://github.c
om/SamurAIGPT/Text-To-Video-AI](https://github.com/SamurAIGPT/Text-To-Video-AI)
```
---

     
 
all -  [ Study finds that smaller models with 7B params can now outperform GPT-4 on some tasks using LoRA. He ](https://www.reddit.com/r/LangChain/comments/1db3sb5/study_finds_that_smaller_models_with_7b_params/) , 2024-06-11-0954
```
Smaller models with 7B params can now outperform the 1.76 Trillion param GPT-4. 😧 How?

A new study from Predibase shows
 that 2B and 7B models, if fine-tuned with Low Rank Adaptation (LoRA) on task-specific datasets, can give better results
 than larger models. (Link to paper in comments)

LoRA reduces the number of trainable parameters in LLMs by injecting l
ow-rank matrices into the model's existing layers.

These matrices capture task-specific info efficiently, allowing fine
-tuning with minimal compute and memory.

So, this paper compares 310 LoRA fine-tuned models, showing that 4-bit LoRA mo
dels surpass base models and even GPT-4 in many tasks. They also establish the influence of task complexity on fine-tuni
ng outcomes.

When does LoRA fine-tuning outperform larger models like GPT-4?

When you have narrowly-scoped, classifica
tion-oriented tasks, like those within the GLUE benchmarks — you can get near 90% accuracy.

On the other hand, GPT-4 ou
tperforms fine-tuned models in 6/31 tasks which are in broader, more complex domains such as coding and MMLU.


```
---

     
 
all -  [ Using Multiple Vectorstores as Retirever But Embedding The Data For One Time ](https://www.reddit.com/r/LangChain/comments/1db3bw1/using_multiple_vectorstores_as_retirever_but/) , 2024-06-11-0954
```
Hi, guys again,

As you know I am building a RAG chatbot on legal texts and thanks to you I come a long way. 

Now the p
roblem is embeddings. I am using Openai embeddings and they are quite expensive as you know. as a retriever I am using e
nsemble retriever and it works great.  But for using ensemble I need to use different vectorestores such as FAISS and BM
25 and they also use embeddings. What I want is embed the documents for one time to pinecone and get the vectors from pi
necone and push into FAISS and BM25. How can I do that?
```
---

     
 
all -  [ GPT-4o bilgisayar asistanı ](https://www.reddit.com/r/CodingTR/comments/1db26qu/gpt4o_bilgisayar_asistanı/) , 2024-06-11-0954
```
Merhaba Mayıs ayında tanıtılan gpt-4o lansmanı sonrası computer asistanlar geleceği söylendi fakat başlangıçta MACOS gel
ecek dediler ayrıca Windowsa geç geleceği söylendi ve yeni bilgisayarlarda gelecek dediler. Bu çok sinir bozucu satmak i
çin özellik kısıtlaması gibi bir şey. Neyse biz de gittik macos, linux ve windows için olan halini MIT lisansında paylaş
tık.

GPT'nin yapacaklarının yanı sıra Langchain, Crew AI, Upsonic Tiger gibi toolları kullanarak ekran fotoğrafı aldığı
nız bir kodun dokümantasyonunu yapan, browser açabilen, toplantı kayıtları alabilen, mesaj yazıp daha sonra mesajı panoy
a kopyalayan, takviminizi hatırlayıp sorular sorabildiğiniz bir asistan geliştirdik. Umarım ilginizi çeker.

  
[https:/
/github.com/onuratakan/gpt-computer-assistant](https://github.com/onuratakan/gpt-computer-assistant)


```
---

     
 
MachineLearning -  [ [P] Superfast RAG: Langchain Streaming and Groq ](https://www.reddit.com/r/MachineLearning/comments/1d5s9g4/p_superfast_rag_langchain_streaming_and_groq/) , 2024-06-11-0954
```
  
Fast LLM RAG inference using Groq and Langchain Streaming.  
  
Groq is introducing a new, simpler processing archite
cture designed specifically for the performance requirements of machine learning applications and other compute-intensiv
e workloads. The simpler hardware also saves developer resources by eliminating the need for profiling, and also makes i
t easier to deploy AI solutions at scale.  
  
Resource: [https://www.youtube.com/watch?v=frMdOL8knqg](https://www.youtu
be.com/watch?v=frMdOL8knqg)
```
---

     
 
MachineLearning -  [ [R] Building an Observable arXiv RAG Chatbot with LangChain, Chainlit, and Literal AI ](https://www.reddit.com/r/MachineLearning/comments/1crwh0q/r_building_an_observable_arxiv_rag_chatbot_with/) , 2024-06-11-0954
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

     
 
MachineLearning -  [ [P] LLMinator: A Llama.cpp + Gradio based opensource Chatbot to run llms locally(cpu/cuda) directly  ](https://www.reddit.com/r/MachineLearning/comments/1cpbgd1/p_llminator_a_llamacpp_gradio_based_opensource/) , 2024-06-11-0954
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

     
 
deeplearning -  [ How to finetune? ](https://www.reddit.com/r/deeplearning/comments/1daio0h/how_to_finetune/) , 2024-06-11-0954
```
Can someone guide me to some resource how can I finetune an open source llm or some library (like langchain) on unstruct
ured data (example: news articles on cricket) So that model can answer a question (like When did India won world Cup?)
```
---

     
