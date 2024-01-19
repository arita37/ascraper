 
all -  [ Apichain ](https://i.redd.it/f576w3wcdadc1.jpeg) , 2024-01-19-0910
```
 when streaming apichain, it prepends the api url to a streaming text response. Any ideas why it would do this ?
```
---

     
 
all -  [ Cost x Prompt too high using GPT 4 ](https://www.reddit.com/r/LangChain/comments/19a4pxq/cost_x_prompt_too_high_using_gpt_4/) , 2024-01-19-0910
```
Hey guys! I am developing a expense chatbot on WhatsApp but the cost per customer is very high. Each request is about 0.
0884 and we are expecting each customer to do at least 100 request per month. Which would mean $8 per customer.

&#x200B
;

We have a set of tools that is elevating the cost because it is passed as context, so my idea was to store the tools 
in a db, use GPT-3.5 to decide which tool to use. Pass just one tool to GPT 4 in the prompt and reduce the cost. But the
 costs would still be high at $0.025 per request.   


I have two questions:  


1. What do you think about my solution?

2. Do you think using Llama2 would be a good idea to create a chatbot? And if so do you have any docs on how to do so.


THanks!
```
---

     
 
all -  [ More than 500 jobs applied for entry level ML engineer none even game me a single interview. Please  ](https://www.reddit.com/r/resumes/comments/199zp4r/more_than_500_jobs_applied_for_entry_level_ml/) , 2024-01-19-0910
```
&#x200B;

https://preview.redd.it/4f4jl3srb9dc1.png?width=1428&format=png&auto=webp&s=98f3b971f3e315ebbe688b72faef7829a8
1601c0
```
---

     
 
all -  [ Integrating BigQuery data into your LangChain application ](https://cloud.google.com/blog/products/ai-machine-learning/open-source-framework-for-connecting-llms-to-your-data/) , 2024-01-19-0910
```

```
---

     
 
all -  [ I love writing tutorials. What are you most interested in? ](https://www.reddit.com/r/LocalLLaMA/comments/199ut0n/i_love_writing_tutorials_what_are_you_most/) , 2024-01-19-0910
```
I've got a cool job where I get to go out and learn about stuff so that I can write about it.

There's a gap in my sched
ule, enough for a decently in-depth blog. I wanted to see what the community was most interested in so that help out.

H
ope this doesn't come off as selfish promo, but here's a few examples of stuff I've done in the past:

• [Generating Tex
t with GGUF](https://colab.research.google.com/drive/1y4RCTIfTTb53b_S95xl4IZaW8am6sBxz)

•[Evaluating Advanced Retrieval
 Methods Using LangChain + ragas](https://colab.research.google.com/drive/1SNgF0MudcIAIBibmi-YkWFwn8Nptt4r5)

• [Evaluat
ing the Impact of Decoding Strategies on Instruction Following](https://colab.research.google.com/drive/1UFBWOUbUUAHTf7i
lCGhPtGDMDeYXrJzt)

• [DeciLM-7B Head to Head Against Mistral-7B on Chain of Thought Tasks](https://colab.research.googl
e.com/drive/11VmmWiY_K76WHepVNp2OU6w3VGuMjBVm)

• [How to Run LangChain Benchmarks with Local LLM from Hugging Face](htt
ps://colab.research.google.com/drive/1ehBzDjUQrioa4abvTIWtABU1ENI2l_2g)

Cheers!
```
---

     
 
all -  [ New Data API for Astra [N] ](https://www.reddit.com/r/MachineLearning/comments/199uobn/new_data_api_for_astra_n/) , 2024-01-19-0910
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

     
 
all -  [ [D] While using function calling or tools on openai or langchain, does openai have access to the dat ](https://www.reddit.com/r/MachineLearning/comments/199t8be/d_while_using_function_calling_or_tools_on_openai/) , 2024-01-19-0910
```
I am working on a client project and I am using langchain's tools and agents. I want to know if the data is getting pass
ed to openai or is it just like that - Output of one function is being directly passed to the second function with the k
nowledge of openai.
```
---

     
 
all -  [ Getting 'value is not a valid dict (type=type_error.dict)' ](https://www.reddit.com/r/LangChain/comments/199rxcn/getting_value_is_not_a_valid_dict_typetype/) , 2024-01-19-0910
```
    docsearch_in_os = OpenSearchVectorSearch(
 opensearch_url=os.environ.get('OPENSEARCH_URL'),
 index_name=index_name,

 embedding_function=bedrock_embeddings,
 http_auth=auth,
 timeout=30,
 use_ssl=True,
 verify_certs=True,
 connection_cla
ss=RequestsHttpConnection,
 is_aoss=True,
    )
 print(user_input)
 print(docsearch_in_os)
 chain = RetrievalQA.from_cha
in_type(
 llm=llm,
 chain_type='stuff',
 retriever=docsearch_in_os.as_retriever(),
 return_source_documents=False,
 chai
n_type_kwargs={'prompt': PROMPT},
    )
 result = chain({'query': user_input})
 print(result)
 answer = result['result']


The above block of code is working fine with the opensearch vector store I created manually via Sagemaker. But somehow
, the same piece of code isn't working when the Opensearch vector store is created via The AWS Bedrock Console. I am get
ting error:  
'value is not a valid dict (type=type\_error.dict)'

https://preview.redd.it/qd5en8unp7dc1.png?width=2880&
format=png&auto=webp&s=af4809165591a12514aa05ade0a8eef29de23e1d
```
---

     
 
all -  [ Project: QA on any PDF document using RAG and VectorDB ](https://i.redd.it/c0cfiqr0o7dc1.jpeg) , 2024-01-19-0910
```
The Smart PDF Reader is a comprehensive project that harnesses the power of the Retrieval-Augmented Generation (RAG) mod
el over a Large Language Model (LLM) powered by Langchain. Additionally, it utilizes the Pinecone vector database to eff
iciently store and retrieve vectors associated with PDF documents. This approach enables the extraction of essential inf
ormation from PDF files without the need for training the model on question-answering datasets.

Find the GitHub repo: [
here](https://github.com/Arshad221b/RAG-on-PDF)
```
---

     
 
all -  [ Which are the best tools to create a Chat App that can use multiple models? ](https://www.reddit.com/r/LocalLLaMA/comments/199opgz/which_are_the_best_tools_to_create_a_chat_app/) , 2024-01-19-0910
```
Hello,

I want to make a chat app that can run multiple models but I am not sure if I should start with LangChain + Olla
ma, based on what I understand LangChain can make some complex tasks and Ollama can answer api calls that can load diffe
rent models.

Unfortunately this combo is not perfect because the visualization of the chat must be custom - due to that
 I came across ChainLit but it didn't provide in-house Chat History that can work with self-hosted models.

Maybe I am d
oing something wrong or my research is not enough but if anyone can help me out in finding a good stack that can run a s
imple chat that can be made into a mini-custom project with chat history/context it would be great.

Thanks,
```
---

     
 
all -  [ Streaming JSON values? ](https://www.reddit.com/r/OpenAI/comments/199o4u2/streaming_json_values/) , 2024-01-19-0910
```
I'm building a chatbot and have requirements to stream the values of returned JSON, but not the keys. For example in too
l calling one of the variables is 'Reasoning' where GPT4 explains the reason it picked this tool that we want to display
.  


Parsing the JSON once completed is trivial, but I need to stream the values for this key.


Example:  
[{'Thought'
: 'Prompt is for internal data so using the get_internal_data tool'}]


I want to ignore everything and only return the 
tokens making up 'Prompt is for internal data so using the get_internal_data tool'.


Oddly I cannot find much on this o
nline. How can this be achieved?

I'm using Azure OpenAI GTP4 and tool calling (no langchain).
```
---

     
 
all -  [ Struggling with LangChain and ChromaDB - Help Needed! ](https://www.reddit.com/r/LangChain/comments/199ne8a/struggling_with_langchain_and_chromadb_help_needed/) , 2024-01-19-0910
```
 

I'm reaching out because I'm having a frustrating issue with LangChain and ChromaDB, and I could really use some help
 from those more experienced than myself. Here's my situation:

I have thousands of text documents that contain detailed
 information, and I'm trying to utilize LangChain and ChromaDB (BAAI/bge-large-en-v1.5) to extract meaningful insights f
rom them. The problem I'm encountering is that when I run the pipeline, it keeps fetching the wrong details for certain 
cases.

For example, let's say I have a case number 'P L D 1949 Dacca 13'. Instead of retrieving the relevant informatio
n for that specific case, the model returns the details for 'P L D 1949 Dacca 30' instead. This is happening consistentl
y across many documents, and I'm at a loss as to why this is occurrcing.

Here are some additional details about my setu
p and process:

\* I'm relatively new to LangChain, so please bear with me if my mistake is obvious.

\* I've followed t
he instructions provided by the LangChain team for setting up the environment and running the pipeline.

\* My dataset c
onsists of plain text files containing various types of legal documents.

\* I'm using the BAAI/bge-large-en-v1.5 model 
for text embedding

Thank you in advance for taking the time to read through my post and offer assistance. Your expertis
e means a lot to me, and I look forward to hearing your thoughts and suggestions.
```
---

     
 
all -  [ Langsmith ](https://www.reddit.com/r/LangChain/comments/199nbwa/langsmith/) , 2024-01-19-0910
```
Hey I was using langhchain before the 0.1.0 update and I'm using it in a project that will go live soon, however I want 
to move to 0.1.0 but my custom agent completely breaks and I feel like LangSmith is my only option. Is there a way to ge
t an invite code as I have been on the wait list for a bit.
```
---

     
 
all -  [ Struggling with LangChain and ChromaDB - Help Needed! ](https://www.reddit.com/r/LanguageTechnology/comments/199n6dl/struggling_with_langchain_and_chromadb_help_needed/) , 2024-01-19-0910
```
  
I'm reaching out because I'm having a frustrating issue with LangChain and ChromaDB, and I could really use some h
elp from those more experienced than myself. Here's my situation:  
  
I have thousands of text documents that contain
 detailed information, and I'm trying to utilize LangChain and ChromaDB (BAAI/bge-large-en-v1.5) to extract meaningful i
nsights from them. The problem I'm encountering is that when I run the pipeline, it keeps fetching the wrong details for
 certain cases.  
  
For example, let's say I have a case number 'P L D 1949 Dacca 13'. Instead of retrieving the rele
vant information for that specific case, the model returns the details for 'P L D 1949 Dacca 30' instead. This is happen
ing consistently across many documents, and I'm at a loss as to why this is occurrcing.  
  
Here are some additional 
details about my setup and process:  
  
\* I'm relatively new to LangChain, so please bear with me if my mistake is o
bvious.  
\* I've followed the instructions provided by the LangChain team for setting up the environment and running t
he pipeline.  
\* My dataset consists of plain text files containing various types of legal documents.  
\* I'm using
 the BAAI/bge-large-en-v1.5 model for text embedding   
  
Thank you in advance for taking the time to read through 
my post and offer assistance. Your expertise means a lot to me, and I look forward to hearing your thoughts and suggesti
ons.
```
---

     
 
all -  [ Langchain 0.1.1 is not working with pinecone-client 3.0.0 ](https://www.reddit.com/r/LangChain/comments/199mklo/langchain_011_is_not_working_with_pineconeclient/) , 2024-01-19-0910
```
    from langchain_community.vectorstores import Pinecone
    from langchain_openai import OpenAIEmbeddings
    from pin
econe import Pinecone as PineconeClient
    pinecone=PineconeClient(
                api_key= {API KEY}
                
)
    embeddings = OpenAIEmbeddings(
        model='text-embedding-ada-002',
        openai_api_key={open_ai_api_key}
  
  )
    vectorstore = Pinecone.from_existing_index(index_name, embeddings)

This gives the following error:  


raise Pi
neconeConfigurationError('You haven't specified an Api-Key.')

pinecone.exceptions.PineconeConfigurationError: You haven
't specified an Api-Key.  


  
Although I provided all the required api keys in line #5 and line #9
```
---

     
 
all -  [ mistral & agents ](https://www.reddit.com/r/MistralAI/comments/199lrht/mistral_agents/) , 2024-01-19-0910
```
is anybody tried mistral with agents using langchain?  its good with function calling?
```
---

     
 
all -  [ Talk with your Data! ](https://www.reddit.com/r/MediumApp/comments/199iv6z/talk_with_your_data/) , 2024-01-19-0910
```
Read this article to learn how to build a GenAI bot, with LangChain and Streamlit in Python. 

Give it data and get answ
ers!
```
---

     
 
all -  [ How do I improve RAG extracted document list ](https://www.reddit.com/r/LangChain/comments/199ejhc/how_do_i_improve_rag_extracted_document_list/) , 2024-01-19-0910
```
I am building a RAG app with langhain, how do you ensure you get the optimal results from your vector store so that the 
extracted documents and prompt sent to the LLM contain all the relevant information? I had to increase topK to as high a
s 50 before getting a good result.
```
---

     
 
all -  [ Example Structured Chat Agent with Complete History ](https://www.reddit.com/r/LangChain/comments/199edvi/example_structured_chat_agent_with_complete/) , 2024-01-19-0910
```
I noticed that in the langchain documentation there was no happy medium where it's explained how to add a memory to both
 the AgentExecutor and the chat itself. If you don't have it in the AgentExecutor, it doesn't see previous steps. In the
 custom agent example, it has you managing the chat history manually.

I've created an example based on the langchain do
cs that does this here: [https://github.com/ThreeRiversAINexus/sample-langchain-agents/blob/main/structured\_chat.py](ht
tps://github.com/ThreeRiversAINexus/sample-langchain-agents/blob/main/structured_chat.py)

Please let me know what you t
hink and if there are any other agents you need help with.

Edit: I've added a string splitting tool and gave an example
 using it to prove that it has memory of the chats as well as the agent executor steps.
```
---

     
 
all -  [ How do I use Lang Chain for AI Recommendations on my app? ](https://www.reddit.com/r/LangChain/comments/1995ips/how_do_i_use_lang_chain_for_ai_recommendations_on/) , 2024-01-19-0910
```
Hello. 

I'm creating a social media app and I intend to use AI for post recommendations. How do I use Lang Chain to ach
ieve that? Any suggestions?
```
---

     
 
all -  [ Is langchain useful for code bases? ](https://www.reddit.com/r/LangChain/comments/1993938/is_langchain_useful_for_code_bases/) , 2024-01-19-0910
```
Im struggling to understand a massive code base with not many comments. 

Could lang chain plus gpt4 actually be useful 
for asking things like 'what do you think this data structure does in the context its in?' Or 'can you describe what thi
s code block is doing in plain English?'
```
---

     
 
all -  [ Modern chat frontend for Python-powered LLM Chat apps? ](https://www.reddit.com/r/ChatGPT/comments/1992b7h/modern_chat_frontend_for_pythonpowered_llm_chat/) , 2024-01-19-0910
```
I'm building an agent with memory and authentication.

I have a solution for chat memory and would rather not use a plat
form which also manages memory to avoid data synchronization complexity.

I tried ChainLit first, but didn't like that i
t largely requires using ChainLit's own data model and preferably ChainLit cloud.

I'm currently using StreamLit, and it
's OK - I like the flexibility, but it's kinda slow for rendering and getting persistent authentication is proving chall
enging due to limited cookie support. It also seems like it was acquired by Snowflake and it's maybe not as well support
ed as pre-acquisition.

Ideally, I want something where I can host with a single Python application binary like these tw
o using some standard but customizable React components and just have a relatively simple interface for providing data (
e.g. chat history, chat response, etc) as needed.

Any recommended solutions here? One thing I'm starting to wonder is i
f I should just switch over to pure TypeScript with NextJS and the JS version of LangChain so I can use React more nativ
ely & directly without having to maintain a bunch of distinct Python business logic & serving code.
```
---

     
 
all -  [ Modern chat frontend for Python-powered LLM Chat apps? ](https://www.reddit.com/r/LangChain/comments/199299c/modern_chat_frontend_for_pythonpowered_llm_chat/) , 2024-01-19-0910
```
Hey folks-

I'm building an agent with memory and authentication.  


I have a solution for chat memory and would rather
 not use a platform which also manages memory to avoid data synchronization complexity.

  
I tried ChainLit first, but 
didn't like that it largely requires using ChainLit's own data model and preferably ChainLit cloud.

&#x200B;

I'm curre
ntly using StreamLit, and it's OK - I like the flexibility, but it's kinda slow for rendering and getting persistent aut
hentication is proving challenging due to limited cookie support. It also seems like it was acquired by Snowflake and it
's maybe not as well supported as pre-acquisition.

&#x200B;

Ideally, I want something where I can host with a single P
ython application binary like these two using some standard but customizable React components and just have a relatively
 simple interface for providing data (e.g. chat history, chat response, etc) as needed.

Any recommended solutions here?
 One thing I'm starting to wonder is if I should just switch over to pure TypeScript with NextJS and the JS version of L
angChain so I can use React more natively & directly without having to maintain a bunch of distinct Python business logi
c & serving code.

&#x200B;

&#x200B;
```
---

     
 
all -  [ New Data API for Astra ](https://www.reddit.com/r/vectordatabase/comments/1990rq3/new_data_api_for_astra/) , 2024-01-19-0910
```
I saw that DataStax/Astra DB [just released a new Data API to help with building production GenAI and RAG applications](
https://www.datastax.com/blog/general-availability-data-api-for-enhanced-developer-experience). This API makes the prove
n petabyte-scale of Apache Cassandra easy to use and available to any JavaScript, Python, or full-stack application deve
loper.

There will also be a webinar available for registration here: [https://www.datastax.com/events/wikichat-build-a-
real-time-rag-app-on-wikipedia-with-langchain-and-vercel](https://www.datastax.com/events/wikichat-build-a-real-time-rag
-app-on-wikipedia-with-langchain-and-vercel)
```
---

     
 
all -  [ Inject metadata into the prompt with createStuffDocumentsChain ](https://www.reddit.com/r/LangChain/comments/1990ckx/inject_metadata_into_the_prompt_with/) , 2024-01-19-0910
```
Any idea why the `page_url` is not available? According to the documentation of `createStuffDocumentsChain`, this should
 automatically be populated from the documents' metadata. And the value definitely exists in the metadata.

```
const hi
storyAwareCombineDocsChain = await createStuffDocumentsChain({
  llm: streamingModel,
  prompt: ChatPromptTemplate.fromM
essages([
    [
      'system',
      `Answer the user's questions based on the below context. When it makes sense, prov
ide a link to the source in markdown format.
      
      Context:
      
      {context}`,
    ],
    new MessagesPlace
holder('chat_history'),
    ['user', '{input}'],
  ]),
  documentPrompt: PromptTemplate.fromTemplate(
    'Source: {page
_url}\n\nPage content:\n{page_content}'
  ),
  documentSeparator: '\n------\n',
});

const retriever = (await getVectorS
tore()).asRetriever();

const historyAwareRetrieverChain = await createHistoryAwareRetriever({
  llm: nonStreamingModel,

  retriever,
  rephrasePrompt: ChatPromptTemplate.fromMessages([
    new MessagesPlaceholder('chat_history'),
    ['use
r', '{input}'],
    [
      'user',
      'Given the above conversation, generate a search query to look up in order to 
get information relevant to the conversation',
    ],
  ]),
});

const conversationalRetrievalChain = await createRetrie
valChain({
  retriever: historyAwareRetrieverChain,
  combineDocsChain: historyAwareCombineDocsChain,
});
```
```
---

     
 
all -  [ An assessment on different LLM/GPT frameworks ](https://www.reddit.com/gallery/198qw1m) , 2024-01-19-0910
```
I sm a first year PhD student at CMU currently looking into LLMs from the perspective of programming abstractions. More 
and more traditional software systems are integrating AI powered workflows, especially LMs. Often and increasingly, this
 is done through LM frameworks, such as LangChain, which orchestrate the at times complex prompting (and even optimisati
on) pipeline and integrates these pipelines into existing programming workflows through programming abstractions(often A
PIs). 

But how can we understand this emerging field of LLM Programming Abstractions? What are some ways we could reaso
n about the approach and indeed philosophies of different frameworks more systematically? 

Hopefully this article that 
I've been working on with Haoze He(CMU), Omar Khattab(Stanford), Christopher Potts(Stanford), Matei Zaharia(Berkeley) an
d Heather Miller (Two Sigma & CMU) could help in starting this discussion. 

I am particularly interested in the opinion
s of folks in this subreddit. Many of you have really gotten your hands dirty with the various frameworks we investigate
d, and might have workflows that might yield a new dimension for looking at these frameworks. 

Link: https://www.twosig
ma.com/articles/a-guide-to-large-language-model-abstractions/
```
---

     
 
all -  [ Trying to figure out design for different kind of chatbot ](https://www.reddit.com/r/LangChain/comments/198mbhg/trying_to_figure_out_design_for_different_kind_of/) , 2024-01-19-0910
```
Hi all--

I want to design a chatbot that:

A) has a set of guidelines (via a long pdf) that it 'uses' to inform its

B)
 Analysis of website content

Basically, a user would submit (website) content via the chat interface, and the bot would
 analyze it based on the guidelines to which it has access. The user can ask questions in order to understand why the bo
t analyzed the content the way that it did. 

I thought embedding the guidelines and using a retriever would be suitable
, but it doesn't seem like it's the right way to go. When I ask it, 'Provide examples from the text where negative langu
age is being used,' it returns a list of negative language from the guidelines rather than applying the question to the 
website content and *using* the guidelines to inform its answer.

I think some type of chain might be ideal, but I'm not
 sure what this would look like.   


Really appreciate the ideas. 
```
---

     
 
all -  [ Best Practice for Fetching Latest Documents? ](https://www.reddit.com/r/LangChain/comments/198i3pz/best_practice_for_fetching_latest_documents/) , 2024-01-19-0910
```
Have any of you guys successfully implemented a system that fetches the latest documents based on the user query?

For e
xample, I have three documents.

* 095 Rate Sheet 01.01.2023.pdf
* 010 Rate Sheet 02.03.2023.pdf
* 28468 Rate Sheet Upda
te 12.12.2023.pdf

Each one of these contains rates information for various loans that month. These rates change each mo
nth. 

I want to query 'get me the latest auto loan rates.'

The expected result is that all three documents match, but 
only the latest document (12.12.2023) is filtered through. Any ideas on how to achieve this type of granularity?
```
---

     
 
all -  [ AutoGen vs. Langchain ](https://www.reddit.com/r/AutoGenAI/comments/198hd9e/autogen_vs_langchain/) , 2024-01-19-0910
```
In what use case should I use either of these? Has anyone used both?

I’m developing an app with openAI as the backbone 
but plan to switch to open source/ Llama in the future. It is mental health focused and will likely involve several diff
erent models with an initial questionnaire pointing the user to chat with one of the models it deems best for their use 
case. I’ve been building on langchain to start. 

Is it worth to look into switching to AutoGen?
```
---

     
 
all -  [ Struggling to Track Token Usage with get_openai_callback() in Streaming – Seeking Advice from Fellow ](https://www.reddit.com/r/LangChain/comments/198g73w/struggling_to_track_token_usage_with_get_openai/) , 2024-01-19-0910
```
I'm currently using `get_openai_callback()` to monitor token consumption per call. However, when streaming the response,
 I'm receiving all zeros. I'm curious if anyone utilizing streaming in their application has successfully tracked token 
usage. Any insights?
```
---

     
 
all -  [ Web GPT4 Vs Assistants GPT4 Vs langchain CSV_agent, regarding asking questions over structured data. ](https://www.reddit.com/r/OpenAI/comments/198fp4h/web_gpt4_vs_assistants_gpt4_vs_langchain_csv/) , 2024-01-19-0910
```
Was experimenting with these 3 alternatives regarding numerical questions over structured data. Web GPT4 was pretty good
 after uploading the document. Assistants API also but slow. Langchain CSV agent had the worse performance of 3.

Howeve
r assistants are slow unfortunately for production apps. Any alternatives, open source as well as paid, regarding quanti
tative questions answered with accuracy over well defined and structured data?
```
---

     
 
all -  [ Want to use langchain with a free llm model ... and strugling ](https://www.reddit.com/r/LangChain/comments/198dky0/want_to_use_langchain_with_a_free_llm_model_and/) , 2024-01-19-0910
```
Hey there.

(Tell me if this is not the right place to ask such questions)

I tried out langchain for a little project, 
nothing too big. My goal was to be able to use langchain to ask LLMs to generate stuff for my project, and maybe impleme
nt some stuff like answers based on local documents.

But I've had a very hard time to find a free llm, and when I found
 how I can make this stuff work with some hugging face models (that I didn't run locally) I was so disappointed how bad 
their answer were.

That's why I am asking for suggestions and answer:

\- should I run locally the llms ? which ones ?


\- how can I manage all the settings of the llm. I don't get what token and temperature are, and I wonder if they are t
he reason why the llm doesn't respond as I would want it to.

\- is hugging face a good choice ?

&#x200B;

Thanks a lot
 by advance, don't hesitate to tell me if I was not specific enough.
```
---

     
 
all -  [ Why should I use LangChain for my new app? ](https://www.reddit.com/r/LangChain/comments/198csjd/why_should_i_use_langchain_for_my_new_app/) , 2024-01-19-0910
```
Hi there! We were early users of LangChain (in March 2023), but we ended up moving away from it because we felt it was t
oo early to support more complex use cases.  We're looking at it again and it looks like it's come a long way!  


What 
are the pros/cons of using LangChain in January 2024 vs going vanilla? What does LangChain help you the most with vs goi
ng vanilla?  


Our use cases are:  
\- Using multiple models using hosted and on-prem LLMs (both OSS and OpenAI/Anthrop
ic/etc.)  
\- Support for complex RAG.  
\- Support chat and non-chat use cases.  
\- Support for both private and non-p
rivate endpoints.  
\- Outputting both structured and unstructured data.  


We're a quite experienced dev team, and it 
feels like we could get away without using LangChain. That being said, we hear a lot about it, so we're curious if we're
 missing out!  

```
---

     
 
all -  [ Vector store connect to pinecone namespace fails ](https://www.reddit.com/r/LangChain/comments/198cs3e/vector_store_connect_to_pinecone_namespace_fails/) , 2024-01-19-0910
```
I have been able to connect Pinecone directly through API without issue when not using Langchain vectorstore as retrieve
r (and even using Langchain when a namespace is not implemented).  However this is causing me a lot of angst now to the 
point I may be about ready to give LangChain the boot from codebase all together… why won’t why won’t this connect with 
namespace involved (while working fine without namespaces)… just says ‘failed to connect’ and  accuses me of using the w
rong index name which is confirmed correct many times over and with straight API code testing : 

index=pinecone.Index(“
agent”)
vectorstore= Pinecone(index, embeddings.embed_query, “text”)
retriever = vectorstore.as_retriever(search_kwargs=
{‘k’:3, ‘namespace’: 1000})

Docs = retriever .get_relevant_documents(msg)

For all the time spent tinkering on this I a
m
thinking to just remove Langchain layers and deal with these functions directly ,but  hoping this is something dumb on
 my end.  I have this code working elsewhere without namespace argument no problem so seems specific to that argument an
d Langchain call to Pinecone index.  

Thanks for any pointers
```
---

     
 
all -  [ Building feedback loop ](https://www.reddit.com/r/LangChain/comments/198alqy/building_feedback_loop/) , 2024-01-19-0910
```
Hi, I'm wondering how to create a feedback loop / response mechanism to collect responses from users to improve the mode
l. Any insights on how to go about this would be greatly appreciated. 

For instance, I want to ask 'how helpful did you
 find this response?' (rating on a scale of 1 to 5). Or a simple thumbs up/down. Either after every message or every few
.

From what I understand I will need to design a script to automatically prompt the user for feedback after the chatbot
 sends a response. Then the feedback will be collected to the database. I am not sure if mongoDB is the best to store bo
th feedback and chat logs together. Is there a simple way to do all this within langchain?

If anyone has done something
 similar or has any ideas or resources please let me know. 🙏
```
---

     
 
all -  [ Roast my resume 1.5 YoE ](https://i.redd.it/h9oirh501ucc1.jpeg) , 2024-01-19-0910
```
Hi, I am a Machine Learning engineer, working in a analytics consulting firm. I have been applying for a lot of jobs but
 my resume never gets shortlisted ..have not gotten a single call yet.

Please review and provide constructive criticism

```
---

     
 
all -  [ Input token limit while extracting text using Google Gemini ](https://www.reddit.com/r/GeminiAI/comments/19871oz/input_token_limit_while_extracting_text_using/) , 2024-01-19-0910
```
I have a use case where I am trying to extract data/fields from large chunks of text, using google gemini and langchain.
 Previously,  I was using chatgpt 3.5 turbo and I was easily able to pass upto 16k tokens. However, with Gemini, it does
n't seem to work well when the number of input tokens is over 4000.

I am not sure what is the token limit of Google Gem
ini.I have found more than one instance/source on web which say that the max number of tokens allowed by Gemini is 32000
, but Gemini doesn't seem to work well with that many tokens.

Has anyone been in a similar situation. Would really appr
eciate any guidance on this. Thanks in advance!
```
---

     
 
all -  [ Stream continue same conversation in case OpenAI errors ](https://www.reddit.com/r/LangChain/comments/1984eyd/stream_continue_same_conversation_in_case_openai/) , 2024-01-19-0910
```
Hi

I want to start using Agent/stream [here](https://python.langchain.com/docs/modules/agents/how_to/streaming), more s
pecifically this part:

    path_status = {}
    async for chunk in agent_executor.astream_log(
        {'input': 'what 
is the weather in sf', 'chat_history': []},
        include_names=['ChatOpenAI'],
    ):
        for op in chunk.ops:
  
          if op['op'] == 'add':
                if op['path'] not in path_status:
                    path_status[op['pa
th']] = op['value']
                else:
                    path_status[op['path']] += op['value']
        print(op['p
ath'])
        print(path_status.get(op['path']))
        print('----')

I'd like to know how I can continue the convers
ation\*(continue from the same point 'last token' received)\*, in case I lose connection with OpenAI or it's down...
```
---

     
 
all -  [ How to update data in Qdrant using langchain.js? ](https://www.reddit.com/r/LangChain/comments/1983iyf/how_to_update_data_in_qdrant_using_langchainjs/) , 2024-01-19-0910
```
 **0**

I am using langchain.js [QdrantVectorStore](https://js.langchain.com/docs/integrations/vectorstores/qdrant) to p
erform CRUD operations in Qdrant collection. I see that there are many options available in js QdrantVectorStore  
 to a
dd data to Qdrant but I don't see any method to update points in a cluster using langchain.js. I know I can use [Qdrant 
js sdk](https://github.com/qdrant/qdrant-js) to perform Updates to points but I prefer doing it using QdrantVectorStore 
 
 for the following reasons:

1. it simply takes the text and Embedding model and do the rest. we don't have to manuall
y convert text to embeddings or vectors.
2. Qdrant has different APIs to update [vectors](https://qdrant.tech/documentat
ion/concepts/points/) and [payload](https://qdrant.tech/documentation/concepts/payload/#update-payload), Since QdrantVec
torStore  
 stores the actual text in payload.content  
 along with the vectors so using qdrant sdk I will have to perfr
om the vector and payload updates seperately with two API calls.

Although using Qdrant vector stores allows writing a c
lean code.

This [reddit post](https://www.reddit.com/r/LangChain/comments/17bc1ij/update_collection_in_qdrantdont_want_
to_create/) suggests using add\_documents  
 even for update but that suggestion is for langchain.py not for js. But I t
ried something similar in langchain.js, I tried to use QdrantVectorStore.addDocuments()  
 to update data but I couldn't
 find a way to pass pointId\[\]  
 to specify which point to update. I also checked the types and interfaces for QdrantV
ectorStore.addDocuments()  
 so I found this

    type QdrantAddDocumentOptions = {     customPayload: Record<string, an
y>[]; }; addDocuments(documents: Document[], documentOptions?: QdrantAddDocumentOptions): Promise<void>; 

As a last res
ort I also tried passing an array of pointIds in customPayload  
 but that didn't work. it was simply creating a point i
n cluster with the ids I passed in customPayload.
```
---

     
 
all -  [ Help please! ](https://www.reddit.com/r/ChatGPT/comments/1983eqs/help_please/) , 2024-01-19-0910
```
so, i need advice from the community about a system that i am struggling to create. 

Let me explain the problem first, 
so, here it goes.

I am trying to build a mobile app, powered with AI. It is an astrology app. I have all the relevant d
ata as my guru is an expert with 60 years of experience in this field.

I am able to call an astro API to get the user c
hart details. so, i have the planetary positions, aspects, and other related information available with me for the AI.


the purpose of using an AI is to make predictions. to draft an overall structure of a person based on the above details 
and the data that I have.

the challenge that I am facing is that, this is not a simple RAG over my dataset. later on, i
 will come to what all i have already tried. but for now, the challenge is that, for predicting any part of a human life
, be it personality, life, career, relationship or anything, there are a set of rules that needs to be followed and chec
ked. for an example, to get the personality, there are around 6 rules to be followed, like the placement of sun, moon. t
he ascendant, the planets present in the house of personality, the ruler of those houses and where they r placed in the 
chart, to name a few rules/combinations.

Now, RAG is simple retrieval of completion of the prompt fed into the llm. and
 as you can see, i need to give reasoning, thinking and processing power to the llm.

I have already tried Llama index, 
langchain with various retrievals, agents, tools and even with vectors, knowledge graphs, summary tools etc. but no use.


kindly help/guide me solve this issue. any pointers/links will be appreciated.
```
---

     
 
MachineLearning -  [ [D] Code vs JSON output for LLM agents? Frameworks like LangChain rely on LLMs responding with JSON  ](https://www.reddit.com/r/MachineLearning/comments/197f416/d_code_vs_json_output_for_llm_agents_frameworks/) , 2024-01-19-0910
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

     
 
MachineLearning -  [ [D] Are Custom LLM RAG apps going to become redundant? ](https://www.reddit.com/r/MachineLearning/comments/1929n4f/d_are_custom_llm_rag_apps_going_to_become/) , 2024-01-19-0910
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

     
 
MachineLearning -  [ [P] An open-source project for deploying local models ](https://www.reddit.com/r/MachineLearning/comments/18zkm5m/p_an_opensource_project_for_deploying_local_models/) , 2024-01-19-0910
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

     
 
MachineLearning -  [ [Project] Temporal Augmented Retrieval (TAR) - Dynamic RAG ](https://www.reddit.com/r/MachineLearning/comments/18uddmj/project_temporal_augmented_retrieval_tar_dynamic/) , 2024-01-19-0910
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

     
 
MachineLearning -  [ [R][P] Autogen + Langchain Tools + Local LLM doesn't work. ](https://www.reddit.com/r/MachineLearning/comments/18tex1j/rp_autogen_langchain_tools_local_llm_doesnt_work/) , 2024-01-19-0910
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

     
 
MachineLearning -  [ [P] Seeking Advice for Building a School Handbook Chatbot Using OpenAI and Vector Databases ](https://www.reddit.com/r/MachineLearning/comments/18rndcp/p_seeking_advice_for_building_a_school_handbook/) , 2024-01-19-0910
```
Hello everyone,

I'm embarking on a project to create a chatbot for my school's handbook, aiming to make it a resource f
or students to easily access information. As someone relatively new to AI, I'm seeking guidance on implementing this.

M
y current plan is to use OpenAI as the primary language learning model, focusing on affordability. I am considering inte
grating RAG (Retrieval-Augmented Generation) and LangChain for enhanced functionality. However, I'm quite perplexed abou
t choosing an appropriate vector database, as many options appear costly. The goal is to keep this system live and acces
sible for student usage without breaking the bank.

I'm also looking into open-source embedding models to pair with the 
vector database. Pinecone has caught my attention, but its pricing seems steep for our budget.

Does anyone have recomme
ndations or tips on affordable yet effective tools and strategies for this project? Any insights on vector databases sui
table for educational use, or ways to optimize cost without compromising quality, would be greatly appreciated.

Thank y
ou in advance for your help!

(I typed out my problem and had gpt4 fix up the format and wording dont bash me)
```
---

     
 
deeplearning -  [ [D] Unleashing the Power of Langchain with Wandb: Revolutionizing Topic Modeling and Evaluation ](https://www.reddit.com/r/deeplearning/comments/191mm83/d_unleashing_the_power_of_langchain_with_wandb/) , 2024-01-19-0910
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

     
