 
all -  [ I also would be thinking about how to increase my skills immediately after suffering brain damage. / ](https://i.redd.it/qwkxlviio9ae1.jpeg) , 2025-01-01-0914
```
This is wild way to start a LinkedIn post. I’ve seen some stuff but wow.
```
---

     
 
all -  [ LangGraph Conceptual Guide ](https://www.reddit.com/r/copilotkit/comments/1hqla7z/langgraph_conceptual_guide/) , 2025-01-01-0914
```
Check out LangGraph's Conceptual guide.  
A perfect pair with [CoAgents](https://docs.copilotkit.ai/coagents)  
[https:/
/langchain-ai.github.io/langgraph/concepts/](https://langchain-ai.github.io/langgraph/concepts/)
```
---

     
 
all -  [ Llama doesnt update with the new Doc provided for RAG ?  ](https://www.reddit.com/r/LocalLLaMA/comments/1hql9zr/llama_doesnt_update_with_the_new_doc_provided_for/) , 2025-01-01-0914
```
I am completely new for LLMs and related stuff. 

I was following a tutorial on youtube to get an idea.

I made a RAG us
ing streamlit as provided in the tutorial 

The issue is that First I ran this code with 'sample.pdf' and then i wanted 
to try this with 'ck3small' pdf as to check if the code is working or not with the new doc provided. 

It still refers t
o old pdf when answering the questions. 

I checked at other threads where it was said to write something to clear cache
 , which I did and the problem still exists : 

I am not exactly sure if this is LLAMA or langchain or Streamlit issue. 


Here's the code. 



    # app.py
    
    import streamlit as st
    import os
    import logging
    from langchain_
community.document_loaders import UnstructuredPDFLoader
    from langchain_text_splitters import RecursiveCharacterTextS
plitter
    from langchain_community.vectorstores import Chroma
    from langchain_ollama import OllamaEmbeddings
    fr
om langchain.prompts import ChatPromptTemplate, PromptTemplate
    from langchain_ollama import ChatOllama
    from lang
chain_core.output_parsers import StrOutputParser
    from langchain_core.runnables import RunnablePassthrough
    from l
angchain.retrievers.multi_query import MultiQueryRetriever
    import ollama
    
    # Configure logging
    logging.ba
sicConfig(level=logging.INFO)
    
    # Constants
    DOC_PATH = './ck3small.pdf'
    MODEL_NAME = 'llama3.2'
    EMBED
DING_MODEL = 'nomic-embed-text'
    VECTOR_STORE_NAME = 'simple-rag'
    PERSIST_DIRECTORY = './chroma_db'
    
    # Fu
nction to ingest PDF documents
    def ingest_pdf(doc_path):
        '''Load PDF documents.'''
        if os.path.exists
(doc_path):
            loader = UnstructuredPDFLoader(file_path=doc_path)
            data = loader.load()
            
logging.info('PDF loaded successfully.')
            return data
        else:
            logging.error(f'PDF file not 
found at path: {doc_path}')
            st.error('PDF file not found.')
            return None
    
    # Function to s
plit documents into smaller chunks
    def split_documents(documents):
        '''Split documents into smaller chunks.''
'
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1200, chunk_overlap=300)
        chunks = text_split
ter.split_documents(documents)
        logging.info('Documents split into chunks.')
        return chunks
    
    # Fun
ction to load or create the vector database
    @st.cache_resource(show_spinner=False)
    def load_vector_db(doc_path):

        '''Load or create the vector database.'''
        # Pull the embedding model if not already available
        o
llama.pull(EMBEDDING_MODEL)
    
        embedding = OllamaEmbeddings(model=EMBEDDING_MODEL)
    
        if os.path.exi
sts(PERSIST_DIRECTORY):
            vector_db = Chroma(
                embedding_function=embedding,
                co
llection_name=VECTOR_STORE_NAME,
                persist_directory=PERSIST_DIRECTORY,
            )
            logging.
info('Loaded existing vector database.')
        else:
            # Load and process the PDF document
            data 
= ingest_pdf(doc_path)
            if data is None:
                return None
    
            # Split the documents i
nto chunks
            chunks = split_documents(data)
    
            vector_db = Chroma.from_documents(
              
  documents=chunks,
                embedding=embedding,
                collection_name=VECTOR_STORE_NAME,
            
    persist_directory=PERSIST_DIRECTORY,
            )
            vector_db.persist()
            logging.info('Vector 
database created and persisted.')
        return vector_db
    
    # Function to create a multi-query retriever
    def
 create_retriever(vector_db, llm):
        '''Create a multi-query retriever.'''
        QUERY_PROMPT = PromptTemplate(

            input_variables=['question'],
            template='''You are an AI language model assistant. Your task is t
o generate five
    different versions of the given user question to retrieve relevant documents from
    a vector datab
ase. By generating multiple perspectives on the user question, your
    goal is to help the user overcome some of the li
mitations of the distance-based
    similarity search. Provide these alternative questions separated by newlines.
    Or
iginal question: {question}''',
        )
    
        retriever = MultiQueryRetriever.from_llm(
            vector_db.a
s_retriever(), llm, prompt=QUERY_PROMPT
        )
        logging.info('Retriever created.')
        return retriever
  
  
    # Function to create the chain with preserved syntax
    def create_chain(retriever, llm):
        '''Create the 
chain with preserved syntax.'''
        # RAG prompt
        template = '''Answer the question based ONLY on the followi
ng context:
    {context}
    Question: {question}
    '''
    
        prompt = ChatPromptTemplate.from_template(templa
te)
    
        chain = (
            {'context': retriever, 'question': RunnablePassthrough()}
            | prompt
  
          | llm
            | StrOutputParser()
        )
    
        logging.info('Chain created with preserved syntax
.')
        return chain
    
    # Main function
    def main():
        st.title('Document Assistant')
    
        # 
User input
        user_input = st.text_input('Enter your question:', '')
    
        if user_input:
            with s
t.spinner('Generating response...'):
                try:
                    # Initialize the language model
          
          llm = ChatOllama(model=MODEL_NAME)
    
                    # Load the vector database
                    vec
tor_db = load_vector_db(DOC_PATH)
                    if vector_db is None:
                        st.error('Failed to 
load or create the vector database.')
                        return
    
                    # Create the retriever
   
                 retriever = create_retriever(vector_db, llm)
    
                    # Create the chain
              
      chain = create_chain(retriever, llm)
    
                    # Get the response
                    response = ch
ain.invoke(input=user_input)
    
                    st.markdown('**Assistant:**')
                    st.write(respons
e)
                except Exception as e:
                    st.error(f'An error occurred: {str(e)}')
        else:
   
         st.info('Please enter a question to get started.')
    
    if __name__ == '__main__':
        main()
    
    

    


```
---

     
 
all -  [ How do I Display what the Agent is doing on the backend to the frontend ](https://www.reddit.com/r/LangChain/comments/1hqjvf3/how_do_i_display_what_the_agent_is_doing_on_the/) , 2025-01-01-0914
```
I’ve been playing around with the LangGraph tutorials to get myself familiar. I’m trying to figure out how to display wh
at the Agent is doing on the frontend.   


Here's a snippet from the LangGraph docs:  
[Streaming](https://langchain-ai
.github.io/langgraph/concepts/streaming/): Streaming is crucial for enhancing the responsiveness of applications built o
n LLMs. By displaying output progressively, even before a complete response is ready, streaming significantly improves u
ser experience (UX), particularly when dealing with the latency of LLMs.

I'd like to be able to stream between nodes fo
r better UX of my app, but since LangGraph is a backend solution, is there a good solution for the frontend so I don't h
ave to build this from scratch? 

My stack is Next.js with some Python backend, and I want to add LangGraph(Agents)

Tha
nks in advance!
```
---

     
 
all -  [ Seeking Feedback on My RAG Architecture for Context Retrieval and Lightweight Optimization ](https://www.reddit.com/r/LangChain/comments/1hqhmdx/seeking_feedback_on_my_rag_architecture_for/) , 2025-01-01-0914
```
I am currently developing a Retrieval-Augmented Generation (RAG) system designed to answer user questions by extracting 
context from two sources: a database or CSV documents. To guide the RAG in selecting the optimal source for context extr
action, I have outlined the following architecture. How do you find it? Is it efficient, or are there bottlenecks I shou
ld address to make it more lightweight?

# Architecture Outline

# 1. Agent Node

* Processes the user question and deci
des the retrieval source or falls back to the LLM's internal knowledge.

# 2. Conditional Edge: Determine Retrieval Sour
ce

* **Check Database**: Verifies if the relevant context exists in the SQLite database.
* **Check CSV Documents**: Ver
ifies if the relevant context exists in the CSV documents.
* **Fallback**: If neither source is applicable, defaults to 
the LLM's internal knowledge.

# 3. SQLite Path

* **Schema Prompt Node**: The LLM receives the database schema and the 
user query to identify relevant fields.
* **Query Construction Node**: The LLM generates an SQL query based on the schem
a and fields.
* **Execute Query Node**: Executes the SQL query and retrieves the results.
* **Answer Formulation Node**:
 Formats the retrieved data into a natural language response using the LLM.

# 4. CSV Path

* **Retrieve CSV Data Node**
: Fetches relevant rows from the CSV documents.
* **Answer Formulation Node**: Summarizes and formats the retrieved data
 using the LLM.

# 5. Fallback Path

* **Generate Using Internal Knowledge Node**: Produces a response solely based on t
he LLM's internal knowledge.

This structure aims to balance flexibility and efficiency. Do you see any potential bottle
necks, or have suggestions for optimization to ensure the system remains lightweight and responsive?


```
---

     
 
all -  [ Graph Structure vs Others  ](https://www.reddit.com/r/LangChain/comments/1hqf270/graph_structure_vs_others/) , 2025-01-01-0914
```
Hi all. I'm looking to see if there's any empirical work done that validates the graph agent structure (e.g., LangGraph)
 as more reliable than other agent/Multi-Agent architectures (non-graph, event-driven). 
```
---

     
 
all -  [ An Agent that creates memes for you ](https://open.substack.com/pub/diamantai/p/viral-marketing-made-easy-unlocking?r=336pe4&utm_campaign=post&utm_medium=web&showWelcomeOnShare=false) , 2025-01-01-0914
```
Memes are the internet’s universal language, but creating ones that truly align with your brand and actually connect wit
h your audience? That’s no small task.

During the hackathon that I ran with LangChain, a talented participant worked on
 a system designed to solve this challenge. It uses AI to analyze a brand’s tone, audience, and personality and then tra
nsforms that data into memes that feel authentic and relevant.

Here’s what makes it exciting:

- It simplifies complex 
brand messaging into relatable humor.
- It adapts to internet trends in real-time.
- It creates memes that aren’t just f
unny—they’re actually effective.
If you’re curious about how it all works, I’ve broken it down in a blog post attached w
ith examples and insights into the process.
```
---

     
 
all -  [ Converting PDFs to Markdown for Higher Quality Embeddings with Langchain.js ](https://www.reddit.com/r/LangChain/comments/1hq8d6c/converting_pdfs_to_markdown_for_higher_quality/) , 2025-01-01-0914
```
I am working on RAG LLM projects with Langchain.js using Node.js. Most of the data I retrieve are PDFs and a bit of JSON
.

For higher quality, I would like to convert my PDFs into Markdown before embedding starts. This involves deleting hea
ders and footers, extracting tables and pictures, and converting the text into Markdown so that it is clear to the LLM w
hether it is body text or an important title.

Example: **This is Title** and < p >just text

I want to ensure that pict
ures and tables are clearly identified in Markdown, and that unnecessary elements are removed. I have found some Python 
libraries that people use for this purpose, but I need something for Node.js. Has anyone experienced with this?

And of 
course, any other tips for better RAG LLM are also welcome! :)

Already tried 'markdown-it' library but not really happy
 with result. The only thing it does is sometimes adding < p >. (Which is still better than nothing but i want everythin
g to be very clear) It's not clear :

* if this text is Title or Body,
* Can't delete Footer Information with this
* Can
't export Table/Picture etc.
```
---

     
 
all -  [ langchain_experimental  SQLDatabaseChain.invoke() question ](https://www.reddit.com/r/LangChain/comments/1hq5px2/langchain_experimental_sqldatabasechaininvoke/) , 2025-01-01-0914
```
I am learning another langchain video  with LLM interacting with SQL.

Here is the  [Jupyter notebook link](https://gith
ub.com/codebasics/langchain/blob/main/4_sqldb_tshirts/t_shirt_sales_llm.ipynb) and its accompanying [YOUTUBE  Video](htt
ps://www.youtube.com/watch?v=4wtrl4hnPT8&t=354s) between the `15:35` `and the 15:39 mark`.

My question is regarding the
 following chunks of code - the issue is specifically executing the second line of code.

    db_chain = SQLDatabaseChai
n.from_llm(llm, db, verbose=True)
    qns1 = db_chain('How many t-shirts do we have left for nike in extra small size an
d white color?')

Update - please note that the second line of code shown above can actually  be executed using `'db_cha
in.invoke'` as shown below, and it yields the same result as the original code :

    qns1 = db_chain.invoke('How many t
-shirts do we have left for nike in extra small size and white color?')

The `Jupyter notebook  output`  upon execution 
of  the above two lines of code is shown as follows:

    > Entering new SQLDatabaseChain chain...
    How many t-shirts
 do we have left for nike in extra small size and white color?
    SQLQuery:SELECT stock_quantity FROM t_shirts WHERE br
and = 'Nike' AND color = 'White' AND size = 'XS'
    SQLResult: [(91,)]
    Answer:91
    > Finished chain.

And here is
 my output :

    > Entering new SQLDatabaseChain chain...
    How many t-shirts do we have left for nike in extra small
 size and white color?
    SQLQuery:SQLQuery: SELECT `stock_quantity` FROM `t_shirts` WHERE `brand` = 'Nike' AND `size` 
= 'XS' AND `color` = 'White';
    SQLResult: [(91,)]
    Answer:Question: How many t-shirts do we have left for nike in 
extra small size and white color?
    SQLQuery: SELECT `stock_quantity` FROM `t_shirts` WHERE `brand` = 'Nike' AND `size
` = 'XS' AND `color` = 'White';
    > Finished chain.

So the difference between the two output  are the 'SQLQuery' and 
'Answer'.   But we can SKIP the 'SQLQuery' differences as this looks like just a minor formatting issue - the SQL query 
generated may not be 'exactly' the same word-for-word but they are identical.

My main issue is my 'Answer' output is sh
owing a string representation of a dictionary keys `'Question'`  and `'SQLQuery'` with their respective values.   Why is
 the  'Answer' not showing  `91` ?

Both the 'SQLResult' outputs (from the tutorial and my output)  are identical.

I di
d a little further digging and executed the following lines

    from pprint import pprint 
    pprint(qns1)

The output
 shows the  `qns1` variable  is actually a dictionary with the following output (on my end):

    {'query': 'How many t-
shirts do we have left for nike in extra small size and '
              'red color?',
     'result': 'Question: How many
 t-shirts do we have left for nike in extra '
               'small size and red color?\n'
               'SQLQuery: SEL
ECT `stock_quantity` FROM `t_shirts` WHERE `brand` = '
               ''Nike' AND `size` = 'XS' AND `color` = 'Red';'}


What code change do I need to do to make the `'result'` show  as `'91'` ?
```
---

     
 
all -  [ StepsTrack: A small Typescript library that helps Logging and Optimizing Pipeline Steps ](https://www.reddit.com/r/Rag/comments/1hq2571/stepstrack_a_small_typescript_library_that_helps/) , 2025-01-01-0914
```
Hello everyone 👋,

I have been working on optimizing an RAG pipeline (mainly on improving speed and reducing token usage
) deployed in production. I found debugging and optimizing very challenging, as there can be a bunch of sub-steps in the
 pipeline, depending on user's query, each step may involves dynamic LLM response and random data retrieval, making the 
response time and runtime flow very non-deterministic. 

So I created **StepsTrack** [https://github.com/lokwkin/steps-t
rack](https://github.com/lokwkin/steps-track) which is a small and simple Typescript library to help me track what was h
appening inside each RAG pipeline runs. It:

* ***Track the results and latency*** of each steps, allow me to export for
 further debug.
* Visualize them into ***Gantt Chart*** & ***Execution Graph*** (I found it very useful when explaining 
the bottlenecks and flow issues to boss and other teammates).
* ***Emit events*** hooks to allow integrating (for furthe
r frontend or external integration like SSE / websocket)

Upcoming planned features:

* Generate execution stats aggrega
ted from multiple pipeline runs (useful on Prod environments to see the behavior from different user inputs)
* Add Redis
 support for pub/sub events and data storage (as an adapter for integrations)
* Implement real-time execution monitoring
. (Probably an internal dashboard frontend to monitor what steps in-progress) 

Note: while StepsTrack focuses on speed 
improvement and debugging logical flow, it doesn’t help address RAG accuracy. I also tried to write this tool non-LLM fo
cused so it can possibility used in other types of applications that has pipeline-like chains of steps.

\---

I’m sure 
there would be similar or better libraries out there, and this library probably won’t work with popular RAG frameworks l
ike LangChain etc. But if you are building pipelines in Typescript and without using any frameworks, you might find Step
sTrack as helpful as I did. 

Feel free to check it out at [https://github.com/lokwkin/steps-track](https://github.com/l
okwkin/steps-track)

Welcome any thoughts, comments, or suggestions! Thanks! 😊 
```
---

     
 
all -  [ What is actually sent to the LLM to decide whether or not to call a tool? ](https://www.reddit.com/r/LangChain/comments/1hpypmj/what_is_actually_sent_to_the_llm_to_decide/) , 2025-01-01-0914
```
I'm working through the 'Build a Retrieval Augmented Generation (RAG) App: Part 2' tutorial where you bind the retrieve 
function as a tool, and then add a conditional edge for when it is executed.

I've been digging through the documentatio
n, but I cannot seem to find an answer for the actual message sent to the LLM to instruct it to either use the retrieve 
tool or respond (as an example: 'If needed, use the retrieve tool to retrieve information related to a query. Otherwise 
respond directly').

This tutorial also had the LLM rephrase the user queries when calling the retrieve tool.

Although 
it doesn't stop me from proceeding, I would really like a look behind the hood as to what LangChain is sending when tool
s are binded to a ChatModel.

  
EDIT: Thank you for your help. I was unable to see this information because it is passe
d as a separate argument in the API (which is exactly the understanding I was trying to obtain). 
```
---

     
 
all -  [ Chat memory  ](https://www.reddit.com/r/LangChain/comments/1hpx94c/chat_memory/) , 2025-01-01-0914
```
Let me ask you an absolute beginner doubt. I have created a simple react agentic architecture using langraph. I have use
d 'MessagesState' as State and passed it to the graph while compiling it.
But for multiple sequential invocations, it se
ems like the state is refreshed. 

For example if I invoke the graph with 
'hi, from now on your name is 'Groot'', 

The
 response will be like 
'Hi, I'm Groot, how can I help you?' 

But for the next execution if I ask the name, it's helple
ss about it.

Is there any other way than using checkpointers to tackle this task?
```
---

     
 
all -  [ How to Add System Message to a multimodal Prompt? ](https://www.reddit.com/r/LangChain/comments/1hpto5u/how_to_add_system_message_to_a_multimodal_prompt/) , 2025-01-01-0914
```
Hi guys, Am using Langchain Python. I have created a sorta Prompt Template to pass my prompt and an Image. But I want to
 add System Message to the Prompt. How do I do it? The code is below

````
import base64

from langchain_core.messages i
mport HumanMessage, SystemMessage

def ga_template(image_path, prompt):

with open(image_path, 'rb') as image_file:

dec
oded_string = base64.b64encode(image_file.read()).decode('utf-8')

message HumanMessage(

content=[

{'type': 'text', 't
ext': prompt},

{

'type': 'image_url',

'image_url': {'url': f'data:image/jpeg;base64, {decoded_string}'},

},

],

ret
urn message
```


```
---

     
 
all -  [ Hot take: Just use Langchain ](https://i.redd.it/v0t3q1xpu0ae1.jpeg) , 2025-01-01-0914
```

```
---

     
 
all -  [ Handle return of Multiple tool request ](https://www.reddit.com/r/LangChain/comments/1hprrzi/handle_return_of_multiple_tool_request/) , 2025-01-01-0914
```
Hi guys,I need some help working with LangChain and LangGraph.

I have an agent, a supervisor, and a tool associated wit
h my agent (this tool is an API request that returns a JSON). Basically, my problem is:When my agent calls the tool mult
iple times, before returning to the supervisor, the agent compacts the multiple returns into  single text. 

https://pre
view.redd.it/9q98tldpo0ae1.png?width=537&format=png&auto=webp&s=54a254df5970b98856644aa391b5304fe76062ef

However, when 
the tool is requested a single time, this doesn't happen, and I don't know how to resolve this efficiently.

https://pre
view.redd.it/2y42wavqo0ae1.png?width=356&format=png&auto=webp&s=0c446845a5e18ff85a81df697c569e4d5dbc6765

Can someone he
lp me?  

```
---

     
 
all -  [ NestJS + LangChain “Langgraphs”: Embed or Deploy Separately? ](https://www.reddit.com/r/LangChain/comments/1hpmxt9/nestjs_langchain_langgraphs_embed_or_deploy/) , 2025-01-01-0914
```
Hey folks, I’m experimenting with LangChain’s Langgraphs in a NestJS server.

Thank you for amazing work, Langchain team
.  All these days I thought 'good prompt building' enough, only until I discovered 'Langgraph'

I’m trying to decide if 
I should embed the langgraphs directly in my NestJS app or set them up as a separate service (or even use their Langgrap
h platform, maybe eventually). 

Would love any pointers about performance, scalability, or best practices.

Thanks! 🙏
```
---

     
 
all -  [ How to Handle Token Limit Exceeded Error in OpenAI API ](https://www.reddit.com/r/LangChain/comments/1hpjms4/how_to_handle_token_limit_exceeded_error_in/) , 2025-01-01-0914
```
I'm getting an error from the OpenAI API stating that the context length exceeds the model's limit, even though I'm only
 passing the last four messages to the prompt. **I’ve verified that each interaction is using around 1056 tokens**, but 
I’m still encountering the error when sending the prompt to the model and not sure why I'm still exceeding the token lim
it.

Full error message:

openai.BadRequestError: Error code: 400 - {'error': {'message': 'This model's maximum context 
length is 8192 tokens. However, your messages resulted in 8452 tokens (8415 in the messages, 37 in the functions). Pleas
e reduce the length of the messages or functions.', 'type': 'invalid\_request\_error', 'param': 'messages', 'code': 'con
text\_length\_exceeded'}}

Here is my code:



`tool(response_format='content_and_artifact')`  
`def retrieve(query: str
):`  
`'''Retrivieving function'''`  
`try:`  
`vector_store = document_embeddings.get_vectorstore()`  
`retrieved_docs 
= vector_store.similarity_search(query, k=4, max_tokens_limit=4000)`  
`serialized = '\n\n'.join(`  
`(f'Source: {doc.me
tadata}\n' f'Content: {doc.page_content}')`  
`for doc in retrieved_docs`  
`)`  
`return serialized, retrieved_docs`  

`except Exception as e:`  
`print(f'Error during retrieval: {e}')`  
`raise e`

    def filter_messages(messages: list):

        # This is very simple helper function which only ever uses the 4 last messages to prevent context limit error
 
       return messages[-4:]
    
    def query_or_respond(state: MessagesState):
        llm_with_tools = llm.bind_tools
([retrieve])
        response = llm_with_tools.invoke(state['messages'])
        return {'messages': [response]}
    
  
  tools = ToolNode([retrieve])
    from langchain_community.callbacks.manager import get_openai_callback
    def generat
e(state: MessagesState):
        messages = filter_messages(state['messages'])
        recent_tool_messages = []
       
 for message in reversed(messages):
            if message.type == 'tool':
                print('Tool')
               
 recent_tool_messages.append(message)
            else:
                break
        tool_messages = recent_tool_messag
es[::-1]
    
        docs_content = '\n\n'.join(doc.content for doc in tool_messages)
        system_message_content = 
(
            'You are an assistant for question-answering tasks. '
            'Use the following pieces of retrieved c
ontext to answer '
            'the question. If you don't know the answer, say that you '
            'don't know. Use 
three sentences maximum and keep the '
            'answer concise.'
            '\n\n'
            f'{docs_content}'
  
          'Use documents/context . ')
    
        conversation_messages = [
            message
            for message
 in messages
            if message.type in ('human', 'system')
            or (message.type == 'ai' and not message.too
l_calls)
        ]
        prompt = [SystemMessage(system_message_content)] + conversation_messages
        print(f'prom
pt: {prompt}')
            # Run
        with get_openai_callback() as cb:
            response = llm.invoke(prompt)
   
         print(f'Total Tokens: {cb.total_tokens}')
            print(f'Prompt Tokens: {cb.prompt_tokens}')
            p
rint(f'Completion Tokens: {cb.completion_tokens}')
            print(f'Total Cost (USD): ${cb.total_cost}')
    
       
 return {'messages': [response]}
    
    
    memory = MemorySaver()
    
     graph_builder = StateGraph(MessagesState
)
     graph_builder.add_node(query_or_respond)
     graph_builder.add_node(tools)
     graph_builder.add_node(generate)

     graph_builder.set_entry_point('query_or_respond')
     graph_builder.add_conditional_edges(
         'query_or_res
pond',
         tools_condition,
         {END: END, 'tools': 'tools'},
     )
     graph_builder.add_edge('tools','gene
rate')
     graph_builder.add_edge('generate', END)
     graph = graph_builder.compile(checkpointer=memory)

For the emb
edding i am using Openai embedding, chunk size = 1000, overlap = 200, parsin with Llamaparse and Unstructured for Makrdo
wnLoader\`

Any advice or solutions would be greatly appreciated!
```
---

     
 
all -  [ Need Feedback on Custom Reducer to Summarize Conversations ](https://www.reddit.com/r/LangChain/comments/1hpjm65/need_feedback_on_custom_reducer_to_summarize/) , 2025-01-01-0914
```
I’m newbie to Langchain and experimenting with LangGraph to build an SQL analysis workflow. I’ve come up with a pattern 
for maintaining conversation context and would love feedback:

* At the end of each query, I summarize the Q&A using a n
ode.
* A custom state reducer takes the previous summary, combines it with the new one, updates the state, and stores it
 as `previous_convo`.

The goal is to keep a condensed version of the entire conversation history accessible.

**Does th
is seem efficient? Any better approaches I should consider?**
```
---

     
 
all -  [ [For Hire] Full Stack Developer | TypeScript, React, Next.js | Remote or Worldwide ](https://www.reddit.com/r/freelancing/comments/1hphkux/for_hire_full_stack_developer_typescript_react/) , 2025-01-01-0914
```
Hello there,

I am a highly skilled Full Stack Developer with a proven track record of delivering impactful projects, su
ch as increasing vendor sales by 25% through innovative ecommerce solutions and enhancing transaction efficiency by 40% 
with blockchain integrations.

**Core Skills & Services**

* Tech Stack: TypeScript, React, Next.js, Node.js, MongoDB, S
tripe, Web3.js, Flutter, and more.
* Specialties: Scalable web applications, token economies, real-time solutions, and m
obile application development.
* Commitment: Dedicated to delivering high-quality, scalable, and user-focused solutions 
tailored to client goals.

**Notable Achievements**

* Survey Monetization Platform: Spearheaded the development of a ro
bust platform using ReactJS, TypeScript, Tailwind, Express.js, MongoDB, and [Socket.io](http://Socket.io), improving use
r engagement and streamlining data management for users.
* Gaming Platform with Token Economies: Designed and developed 
an innovative gaming platform leveraging blockchain, resulting in a 30% boost in user engagement and seamless token tran
sactions using Next.js, Web3.js, and MongoDB.
* Solana Volume Bot: Built a highly efficient bot for Solana tokens using 
Web3.js, achieving a 40% improvement in transaction bundling and speed.
* Ecommerce Platform with Live Streaming: Delive
red an ecommerce solution integrated with live streaming capabilities that drove a 25% increase in vendor sales using Ne
xt.js, Stripe, Mediasoup, and Socket.io.
* AI-Powered Chatbot: Reduced customer service response times by 50% with an in
telligent chatbot powered by OpenAI and Langchain, deployed with a scalable tech stack including React, MongoDB, and Typ
eScript.
* Flutter Mobile Applications: Enhanced project outputs by 20% during my tenure as an intern by delivering feat
ure-rich applications in Flutter for ecommerce and news services.

**Budget/Rate:**

Starting at **$15/hr**, depending o
n project complexity and scope.

Whether you need a full-stack solution, a single-page application, or innovative featur
es for your platform, I’m here to help. Let's collaborate to bring your vision to life!

**Contact:**  
📧 Email: [farsee
nmanekhan1232@gmail.com](mailto:farseenmanekhan1232@gmail.com)  
📱 Phone: +91 9686446001  
🌐 [Portfolio](https://farseen
.tech/) | [GitHub](https://github.com/farseenmanekhan1232) | [LinkedIn](https://linkedin.com/in/mohammad-farseen-manekha
n-2419531a7)
```
---

     
 
all -  [ Resume Review: ML/AI Engineering Grad Student Looking for Internships, not having much luck ](https://www.reddit.com/r/Resume/comments/1hp6pt3/resume_review_mlai_engineering_grad_student/) , 2025-01-01-0914
```
I'm a current Computer Engineering Master's student focusing on AI/Machine Learning, and I've been applying to internshi
ps, but the only replies I ever get are if I have a referral. I got an interview with Salesforce for an AI internship be
cause of a referral and the it went well. So even though I don't know if I'll get the position I'm wondering why I can't
 get companies lower on the totem pole than Salesforce to give me an interview or OA.

I'm wondering if my resume format
 is bad and getting auto rejected or if I just don't have enough experience to make it in a competitive market (It could
 be a combination of both). I get the sense that my resume isn't even making it past recruiters. I see other people at l
east get interviews with these places, I'm wondering what they're doing that I'm not.

Any advice or tips would be great
ly appreciated. I haven't had much luck getting advice in other subs or having my resume refined by someone on Fiver for
 $60. For reference I am a US citizen (I know that can affect what recruiters do with applications). 

https://preview.r
edd.it/wkkxxgb1yu9e1.jpg?width=1252&format=pjpg&auto=webp&s=f09d4baa91524c95784f175dce6b085689404595


```
---

     
 
all -  [ Is there any simpler way to implement memory in a chat app? ](https://www.reddit.com/r/OpenAI/comments/1hp6h5g/is_there_any_simpler_way_to_implement_memory_in_a/) , 2025-01-01-0914
```
I am creating a simple chat app with Haystack but like Langchain, Haystack is too much abstraction for a simple task.

S
o I was wondering if anyone knows of a way to implement memory for the chat app without using Haystack or Langchain?

Al
so, this is a simple chat app and not a document based chat app.
```
---

     
 
all -  [ Need advice regarding job search  ](https://i.redd.it/4v2brxtzkt9e1.jpeg) , 2025-01-01-0914
```
I'm a Master's student pursuing my degree in EE, my bachelor's was in EE as well.  I was originally interested in roboti
cs design.
However, opportunities have been limited to say the least. I figure I can't be selective anymore and have bee
n applying to broader roles in EE as well, but have had no luck with the applications. Tried internships but no luck the
re either.
I need advice on what roles would be the best fit given my skills. And what approach I should take to improve
 my resume.
Any feedback on the resume itself would be greatly appreciated as well.
Thank you for your time.

```
---

     
 
all -  [ LinkedIn tool integration - how to implement ](https://www.reddit.com/r/AI_Agents/comments/1hp028i/linkedin_tool_integration_how_to_implement/) , 2025-01-01-0914
```
Hi there,  
I am currently working on an AI agent project and need to scrape through my clients Linkedin contacts, to id
entify potential leads. As far as I am aware, there is no tool integration for LinkedIn. I have checked the LangChain an
d crewAI documentation, and could not find a tool there. I saw composio has a LinkedIn connector, but then you have to i
mplement your own tool logic (which is fine for me, I am a senior dev, but I have concerns about getting blocked on Link
edIn for scraping). 

Do you know of any other libraries or frameworks I can use? I am looking for free solutions, no lo
w code. Thanks in advance. 
```
---

     
 
all -  [ Web browser example is giving me - Error: Failed to parse. Text: '```json... is not valid JSON'  ](https://www.reddit.com/r/flowise/comments/1hos4vp/web_browser_example_is_giving_me_error_failed_to/) , 2025-01-01-0914
```
After following this example - [https://www.youtube.com/watch?v=yEHC7\_x2x4U](https://www.youtube.com/watch?v=yEHC7_x2x4
U) \- I'm getting an error while working on Flowise and I'm hoping someone can help me troubleshoot. I'm getting a 'Fail
ed to parse. Text: \`\`\`json... is not valid JSON' error.

Here's the full error message:

Failed to parse. Text: '\`\`
\`json { 'action': 'Final Answer', 'action\_input': | { 'definition\_of\_word\_of\_the\_day': 'A word of the day is a re
gularly occurring piece of content, such as a quote, fact, or definition, that is shared with users on a particular plat
form.', 'example\_use\_case\_for\_perspicacious': 'The detective was known for being perspicacious and could often solve
 cases by observing small details that others had missed.' } }

{

  '... is not valid JSON



Troubleshooting URL: [htt
ps://js.langchain.com/docs/troubleshooting/errors/OUTPUT\_PARSING\_FAILURE/](https://js.langchain.com/docs/troubleshooti
ng/errors/OUTPUT_PARSING_FAILURE/)

*Processing img 2i89l4mshn9e1...*


```
---

     
 
all -  [ Building a Production-Ready RAG Application: Need Advice ](https://www.reddit.com/r/LangChain/comments/1horktb/building_a_productionready_rag_application_need/) , 2025-01-01-0914
```

Hi everyone,

I’m currently working on building a production-ready RAG application. My primary is Azure OpenAI, but I’m
 open to other LLM integrations if necessary.

Key Requirements:
- Handling a large volume of internal documents.
- Feat
ures like question reformulation and reranking to improve retrieval accuracy.

Frameworks I’m Considering:
- LangChain
-
 Haystack
- Semantic Kernel

Do you have any recommendations on which framework is best suited for this use case? Am I m
issing any other frameworks that I should evaluate?

I’d appreciate your insights and experiences
```
---

     
 
all -  [ Monopoly - beat a human collective ](https://www.reddit.com/r/ollama/comments/1hoi9rm/monopoly_beat_a_human_collective/) , 2025-01-01-0914
```
So its christmas and the thought turns to the family board games,

Is there a model or app (python) or gui site where i 
can basicaly kick the families backsides by using ai to process the permutations for me?

Ditto many other popular board
 games such as cludeo, sorry, stratego,, ( ignoring knowledge based such as trivial pursuits) 

I have a decent enough l
aptop with a 4070 that runs models happily locally using ollama and i am comfortable with python and langchain and local
 class modules.. 

Just a random thought to use what i mess with in the day job to kick the families arses round the din
ner table 🤣
```
---

     
 
all -  [ Best Way to Chunk Large-ish Text Documents for Make.com ](https://www.reddit.com/r/vectordatabase/comments/1hoeees/best_way_to_chunk_largeish_text_documents_for/) , 2025-01-01-0914
```
I'm looking around for the best way to chunk large documents in a [Make.com](http://Make.com) scenario before sending th
e data into Pinecone. Within Make, there is CustomJS and 0CodeUtil. LangChain apparently is an option as well. Honestly,
 I would love to be able to deploy a custom function somewhere in the cloud and then call it using an API. Really trying
 to avoid complex setups and want quick and dirty.
```
---

     
 
all -  [ Underlying tech of Cursor? ](https://www.reddit.com/r/ycombinator/comments/1hod5iv/underlying_tech_of_cursor/) , 2025-01-01-0914
```
Very curious about how the Cursor team is approaching their solution technically

1. How do they handle context across t
he project?
2. Do they use raw APIs or something like LangChain or LangGraph?
3. Is it proprietary tech or just a 'LLM w
rapper'? (I don't think so)

Is there info about this?
```
---

     
 
all -  [ Top 5 Hacker News Posts on RAG This Week ](https://www.reddit.com/r/Rag/comments/1hobxkl/top_5_hacker_news_posts_on_rag_this_week/) , 2025-01-01-0914
```
Curated the top 5 most insightful posts on RAG — highlighting key discussions and practical takeaways:

1️⃣ 𝗧𝗶𝘁𝗹𝗲: RAG L
ogger: An Open-Source Alternative to LangSmith  
𝗨𝗽𝘃𝗼𝘁𝗲𝘀: 95  
𝗟𝗶𝗻𝗸: [https://news.ycombinator.com/item?id=42485113](htt
ps://news.ycombinator.com/item?id=42485113)  
𝗪𝗵𝗮𝘁 𝗶𝘀 𝗶𝘁 𝗮𝗯𝗼𝘂𝘁: RAG Logger is a simple, open-source RAG pipeline logging
 tool with suggested enhancements like visualization, OpenTelemetry support, and replay features.

2️⃣ 𝗧𝗶𝘁𝗹𝗲: Collab Not
ebook – RAG on Your Unstructured Data  
𝗨𝗽𝘃𝗼𝘁𝗲𝘀: 14  
𝗟𝗶𝗻𝗸: [https://news.ycombinator.com/item?id=42517745](https://news
.ycombinator.com/item?id=42517745)  
𝗪𝗵𝗮𝘁 𝗶𝘀 𝗶𝘁 𝗮𝗯𝗼𝘂𝘁: The post outlines using LangChain and Unstructured IO to address 
unstructured data challenges in RAG with FAISS, LLMs, and Athina AI evaluation.

3️⃣ 𝗧𝗶𝘁𝗹𝗲: Web RAG to generate perplexi
ty like answers from your docs in browser  
𝗨𝗽𝘃𝗼𝘁𝗲𝘀: 5  
𝗟𝗶𝗻𝗸: [https://news.ycombinator.com/item?id=42516981](https://n
ews.ycombinator.com/item?id=42516981)  
𝗪𝗵𝗮𝘁 𝗶𝘀 𝗶𝘁 𝗮𝗯𝗼𝘂𝘁: The system offers a private, browser-based solution for indexi
ng, searching, and generating responses using GTE-small, SQLite, and WebLLM, with zero API costs 👩‍💻

4️⃣ 𝗧𝗶𝘁𝗹𝗲: LLM app
s, AI Agents, and RAG tutorials with step-by-step instructions  
𝗨𝗽𝘃𝗼𝘁𝗲𝘀: 3  
𝗟𝗶𝗻𝗸: [https://news.ycombinator.com/item?i
d=42510073](https://news.ycombinator.com/item?id=42510073)  
𝗪𝗵𝗮𝘁 𝗶𝘀 𝗶𝘁 𝗮𝗯𝗼𝘂𝘁: A curated repository of RAG-powered LLM a
pplications, showcasing models from OpenAI, Anthropic, Google, and open-source options like LLaMA.

5️⃣ 𝗧𝗶𝘁𝗹𝗲: GraphRAG 
SDK 0.4.0: Simplify RAG with Graph Databases  
𝗨𝗽𝘃𝗼𝘁𝗲𝘀: 2  
𝗟𝗶𝗻𝗸: [https://news.ycombinator.com/item?id=42496411](https:
//news.ycombinator.com/item?id=42496411)  
𝗪𝗵𝗮𝘁 𝗶𝘀 𝗶𝘁 𝗮𝗯𝗼𝘂𝘁: The module simplifies RAG application development with grap
h databases, multi-LLM support, smarter queries, LiteLLM integration, and cost-effective deployment 🚀
```
---

     
 
all -  [ [Student] Looking for feedback on my resume and general advise regarding job search ](https://www.reddit.com/r/EngineeringResumes/comments/1hoa3j9/student_looking_for_feedback_on_my_resume_and/) , 2025-01-01-0914
```
My last post didn't get much traction so I hope this one does better. I believe this is my first time posting here, but 
I have posted on the resumes subreddit before. Looking for criticism/feedback on the latest iteration of my resume. 

I 
am looking for robotics/EE roles, and have been applying since the start of the fall semester, but no luck regarding get
ting interviews. No luck with internships either. A couple of pre-recorded video interviews but they didn't go anywhere.
 I am not sure what I am doing wrong, is it the fact that I am an international student, lack of experience, my resume, 
or all three.

I would also like advice on what roles in EE/robotics would best fit me, given my skills. I figure being 
specific will not get me anywhere hence the desperation.

Thanks again for your time.

https://preview.redd.it/zcn91jq9g
m9e1.jpg?width=4967&format=pjpg&auto=webp&s=75cd4e61fcc35fd21d160ef084daa48f029f30cc




```
---

     
 
all -  [ An Open Source Computer/Browser Tool for your Langgraph AI Agents ](https://www.reddit.com/r/LangChain/comments/1ho8m91/an_open_source_computerbrowser_tool_for_your/) , 2025-01-01-0914
```
MarinaBox is an open-source toolkit for creating browser/computer sandboxes for AI Agents. If you ever wanted your Langg
raph agents to use a computer using Claude Computer-Use, you can check this out,  
[https://medium.com/@bayllama/a-compu
ter-tool-for-your-langgraph-agents-using-marinabox-b48e0db1379c](https://medium.com/@bayllama/a-computer-tool-for-your-l
anggraph-agents-using-marinabox-b48e0db1379c)

We also support creating just a browser sandbox if having access to a des
ktop environment is not necessary.

Documentation:[https://marinabox.mintlify.app/get-started/introduction](https://mari
nabox.mintlify.app/get-started/introduction)   
Main Repo: [https://github.com/marinabox/marinabox](https://github.com/m
arinabox/marinabox)   
Infra Repo: [https://github.com/marinabox/marinabox-sandbox](https://github.com/marinabox/marinab
ox-sandbox)

PS: We currently only support running locally. Will soon add the ability to self-host on your own cloud.
```
---

     
 
all -  [ Supabase and Open AI Realtime with langchain powered App to interact with your PDFs ](https://www.reddit.com/r/Supabase/comments/1ho40ha/supabase_and_open_ai_realtime_with_langchain/) , 2025-01-01-0914
```
Hi Everyone, we are proud to share the release of our open source voice-to-voice Proof of concept where you can upload y
our documents and ask questions related to them.

You can upload your documents and interact with them through our dashb
oard.📊.

Based on OpenAI Realtime AND langchain

Powered by [Supabase](https://www.linkedin.com/company/supabase/)  \+ [
Qdrant](https://www.linkedin.com/company/qdrant/)  \+ [NextJs](https://www.linkedin.com/company/nextjs/)

Github repo: [
https://github.com/actualize-ae/voice-chat-pdf](https://github.com/actualize-ae/voice-chat-pdf)

**If you like the conce
pt or have feedback please feel free to contribute a star and share feedback :)**

Video: [https://vimeo.com/1039742928?
share=copy](https://vimeo.com/1039742928?share=copy)
```
---

     
 
all -  [ Open AI Realtime with langchain powered RAG POC ](https://www.reddit.com/r/OpenAIDev/comments/1ho3sxb/open_ai_realtime_with_langchain_powered_rag_poc/) , 2025-01-01-0914
```
Hi Everyone, we are proud to share the release of our open source voice-to-voice Proof of concept where you can upload y
our documents and ask questions related to them.

You can upload your documents and interact with them through our dashb
oard.📊.

Based on OpenAI Realtime AND langchain

Powered by [Supabase](https://www.linkedin.com/company/supabase/)  \+ [
Qdrant](https://www.linkedin.com/company/qdrant/)  \+ [NextJs](https://www.linkedin.com/company/nextjs/)

Github repo: [
https://github.com/actualize-ae/voice-chat-pdf](https://github.com/actualize-ae/voice-chat-pdf)

**If you like the conce
pt or have feedback please feel free to contribute a star and share feedback :)**

Video: [https://vimeo.com/1039742928?
share=copy](https://vimeo.com/1039742928?share=copy)


```
---

     
 
all -  [ Invite Emails for EU Region are not being Sent ](https://www.reddit.com/r/LangChain/comments/1ho3a66/invite_emails_for_eu_region_are_not_being_sent/) , 2025-01-01-0914
```
I've been trying to sign up via https://eu.smith.langchain.com/. It keeps saying I should check my email for a confirmat
ion link, which is not arriving (no, not in my spam either). Please advise.
```
---

     
 
all -  [ Langchain and embeddings in voice pipeline? ](https://www.reddit.com/r/homeassistant/comments/1hnwy4q/langchain_and_embeddings_in_voice_pipeline/) , 2025-01-01-0914
```
Has anyone thought about adding a vertex DB to the voice pipeline rather than adding all entities exported in the prompt
 every time? Maybe we could have a plug-in that allows calling a langchain pipeline rather than an LLM directly, this wo
uld allow querying entities rather than having them in the prompt and could open up to a more complex multi agent setup 

```
---

     
 
all -  [ Guide to Integrating LangChain with Ollama for Local AI Workflows ](https://www.reddit.com/r/u_KonradFreeman/comments/1hntzfb/guide_to_integrating_langchain_with_ollama_for/) , 2025-01-01-0914
```
For those seeking to transition from cloud-based AI services to a more private and cost-effective local setup, I have re
cently published a comprehensive guide on integrating LangChain with Ollama. This guide outlines how to build robust wor
kflows powered by locally hosted language models (LLMs). You can access the complete write-up here: [LangChain + Ollama 
Guide](https://danielkliewer.com/2024/12/27/langchain-ollama).

This resource serves as a valuable starting point for ex
ploring local AI workflows or considering alternatives to cloud-based solutions. I am happy to answer any questions or d
iscuss potential use cases in more detail.

To provide a preview, the final program created as part of the guide is incl
uded below. While I used the QwQ model in this implementation, the setup is flexible—you can easily swap in a different 
model by modifying the corresponding payload entry.

The project was designed with two main objectives:

1. Core Concept
 Mastery: To understand the fundamental principles behind building scalable AI workflows.
2. Enhanced Local Model Capabi
lities: To explore methods of improving locally hosted models, enabling them to match or surpass some of the functionali
ty of cloud-based alternatives.

Currently, the application leverages simple folders containing .json persona files. Fut
ure iterations could integrate a database for greater flexibility. Additionally, a React-based UI for persona customizat
ion could be implemented, similar to the functionality I developed in my Personagen project.

# Key Innovations

* Graph
-Based Logic and Reasoning: By simulating logic with graph structures, the workflow can enhance local model outputs. Thi
s involves using multiple LLM calls with a context tracker, implemented through a graph-based LLM-to-LLM structure. This
 reduces hallucinations and enables more advanced functionalities.
* Scalable Personas: The personas folder allows for s
eamless customization, enabling developers to define any desired attributes. These can range from predefined JSON struct
ures to dynamic outputs generated by LLM calls, facilitating more complex orchestration of nodes and subnodes.
* Optimiz
ed Workflow Execution: By utilizing LangChain asynchronously with topological sorting, the application chains prompts ef
ficiently, minimizing response times.

requirements.txt

    langchain
    networkx
    markdown
    langchain_community

    click
    
    
    
    # main.py
    
    import click
    import os
    import networkx as nx
    from langchain
 import PromptTemplate, LLMChain
    from langchain.llms import Ollama
    import json
    
    # Define the Node class

    class Node:
        def __init__(self, node_id, prompt_text, persona_name):
            self.id = node_id
          
  self.prompt_text = prompt_text
            self.response_text = None
            self.context = ''
            self.pe
rsona_name = persona_name
            self.persona_attributes = {}
    
    # Initialize the graph
    G = nx.DiGraph()

    
    def build_graph(nodes_info, edges_info):
        G = nx.DiGraph()
        nodes = {}
        # Create nodes
   
     for node_info in nodes_info:
            node_id = node_info['id']
            prompt_text = node_info['prompt_text
']
            persona_name = node_info['persona_name']
            node = Node(node_id, prompt_text, persona_name)
    
        G.add_node(node_id, data=node)
            nodes[node_id] = node
    
        # Add edges
        for edge in ed
ges_info:
            G.add_edge(edge['from'], edge['to'])
        
        return G
    
    def process_graph(G):
    
    for node_id in nx.topological_sort(G):
            node = G.nodes[node_id]['data']
            if node.persona_name 
!= 'Analyst':
                node.context = collect_context(node_id, G)
                node.response_text = generate_r
esponse(node)
                update_markdown(node)
            else:
                analyze_responses(node, G)
    
  
  def load_personas(persona_dir):
        personas = {}
        for filename in os.listdir(persona_dir):
            if 
filename.endswith('.json'):
                filepath = os.path.join(persona_dir, filename)
                with open(fil
epath, 'r', encoding='utf-8') as f:
                    persona_data = json.load(f)
                    name = persona_d
ata.get('name')
                    if name:
                        personas[name] = persona_data
        return person
as
    
    # Load personas
    persona_dir = 'personas'  # Directory where persona JSON files are stored
    personas =
 load_personas(persona_dir)
    
    # Function to collect context from predecessor nodes
    def collect_context(node_i
d, G):
        predecessors = list(G.predecessors(node_id))
        context = ''
        for pred_id in predecessors:
  
          pred_node = G.nodes[pred_id]['data']
            if pred_node.response_text:
                context += f'From
 {pred_node.persona}:\n{pred_node.response_text}\n\n'
        return context
    
    # Function to generate responses u
sing LangChain and Ollama
    def generate_response(node):
        persona = personas.get(node.persona_name)
        if 
not persona:
            raise ValueError(f'Persona '{node.persona_name}' not found.')
        
        node.persona_att
ributes = persona
    
        # Build the system prompt based on persona attributes
        system_prompt = build_syste
m_prompt(persona)
    
        # Build the complete prompt
        prompt_template = PromptTemplate(
            input_v
ariables=['system_prompt', 'context', 'prompt'],
            template='{system_prompt}\n\n{context}\n\n{prompt}'
       
 )
        # Instantiate the Ollama LLM
        llm = Ollama(
            base_url='http://localhost:11434',  # Default 
Ollama server URL
            model='qwq',  # Replace with the model you have downloaded
        )
        chain = LLMCh
ain(llm=llm, prompt=prompt_template)
        response = chain.run(
            system_prompt=system_prompt,
            
context=node.context,
            prompt=node.prompt_text
        )
        return response
    
    def build_system_pr
ompt(persona):
        # Construct descriptive sentences based on persona attributes
        # We'll focus on key attrib
utes for brevity
        name = persona.get('name', 'The speaker')
        tone = persona.get('tone', 'neutral')
       
 sentence_structure = persona.get('sentence_structure', 'varied')
        vocabulary_complexity = persona.get('vocabular
y_complexity', 5)
        formality_level = persona.get('formality_level', 5)
        pronoun_preference = persona.get('
pronoun_preference', 'third-person')
        language_abstraction = persona.get('language_abstraction', 'mixed')
    
  
      # Create a description
        description = (
            f'You are {name}, writing in a {tone} tone using {sente
nce_structure} sentences. '
            f'Your vocabulary complexity is {vocabulary_complexity}/10, and your formality l
evel is {formality_level}/10. '
            f'You prefer {pronoun_preference} narration and your language abstraction is
 {language_abstraction}.'
        )
    
        # Include any other attributes as needed
        # ...
    
        ret
urn description
    
    
    # Function to log interactions to a markdown file
    def update_markdown(node):
        w
ith open('conversation.md', 'a', encoding='utf-8') as f:
            f.write(f'## Node {node.id}: {node.persona_name}\n\
n')
            f.write(f'**Prompt:**\n\n{node.prompt_text}\n\n')
            f.write(f'**Response:**\n\n{node.response_
text}\n\n---\n\n')
    
    # Function for nodes that perform analysis
    def analyze_responses(node, G):
        # Col
lect responses from predecessor nodes
        predecessors = list(G.predecessors(node.id))
        analysis_input = ''
 
       for pred_id in predecessors:
            pred_node = G.nodes[pred_id]['data']
            analysis_input += f'{pr
ed_node.persona_name}'s response:\n{pred_node.response_text}\n\n'
    
        node.prompt_text = f'Provide an analysis 
comparing the following perspectives:\n\n{analysis_input}'
        node.context = ''  # Analysis is based solely on the 
provided responses
        node.response_text = generate_response(node)
        update_markdown(node)
    
    
    @cli
ck.group()
    def cli():
        pass
    
    @cli.command()
    def list_personas():
        '''List all available pe
rsonas.'''
        for persona_name in personas.keys():
            print(persona_name)
            
    @cli.command()

    @click.option('--nodes', '-n', default=2, help='Number of nodes (excluding the analyst node).')
    def run(nodes):

        '''Run the application with the specified number of nodes.'''
        # Let the user select personas and input p
rompts for each node
        nodes_info = []
        for i in range(1, nodes + 1):
            print(f'\nConfiguring Nod
e {i}')
            persona_name = click.prompt('Enter the persona name', type=str)
            while persona_name not i
n personas:
                print('Persona not found. Available personas:')
                for name in personas.keys():

                    print(f' - {name}')
                persona_name = click.prompt('Enter the persona name', type=str)

            
            prompt_text = click.prompt('Enter the prompt text', type=str)
            node_info = {
      
          'id': i,
                'prompt_text': prompt_text,
                'persona_name': persona_name
            
}
            nodes_info.append(node_info)
        
        # Add the analyst node
        analyst_node_id = nodes + 1
 
       analyst_node_info = {
            'id': analyst_node_id,
            'prompt_text': '',
            'persona_name
': 'Analyst'
        }
        nodes_info.append(analyst_node_info)
        
        # Define edges (here we assume that
 the analyst node depends on all other nodes)
        edges_info = []
        for i in range(1, nodes + 1):
            
edges_info.append({'from': i, 'to': analyst_node_id})
        
        # Build and process the graph
        G = build_g
raph(nodes_info, edges_info)
        process_graph(G)
        print('\nConversation has been generated and logged to con
versation.md')
    
    if __name__ == '__main__':
        cli()
```
---

     
 
all -  [ What's the big deal about agents in 2025?  ](https://www.reddit.com/r/ArtificialInteligence/comments/1hnq2t3/whats_the_big_deal_about_agents_in_2025/) , 2025-01-01-0914
```

I know what agents are and how could they be useful in general. But why the hype around them right now? 
We already hav
e frameworks/libraries for developing agentic work flows, like langchain, crewai, autogen etc. This could already be don
e in 2024, if not sooner. 

Why are all the big companies starting to talk about the agents right now? 
```
---

     
 
all -  [ Review my resume and suggest Some changes as it gets rejected everytime. ](https://i.redd.it/6wtgtxc0lg9e1.jpeg) , 2025-01-01-0914
```
I am final year student from tier-3.looking for internships and full time roles.can anyone suggest what changes should I
 make in my resume.
```
---

     
 
all -  [ Langgraph without Langsmith? ](https://www.reddit.com/r/LangChain/comments/1hnjzi6/langgraph_without_langsmith/) , 2025-01-01-0914
```
I'm new to Langgraph and enjoying it as I learn this space.  A major concern for me is the fact that my logs all go to L
angsmith.  I can not build anything beyond a basic POC if company data, which would be in all of the agent interactions,
 is being logged to Langsmith.  Is there a way to turn this off?
```
---

     
 
all -  [ Was reading through the docs. What is the difference between putting the chat history in the chat pr ](https://www.reddit.com/r/LangChain/comments/1hngbcw/was_reading_through_the_docs_what_is_the/) , 2025-01-01-0914
```
Just wanted to know the difference between putting the history here:

    const prompt = ChatPromptTemplate.fromMessages
([
    ['system', 'You are a helpful assistant'],
    ['placeholder', '{chat_history}'],
    ['human', '{input}'],
    [
'placeholder', '{agent_scratchpad}'],
    ]);

vs here:

    const result2 = await agentExecutor.invoke({
    input: 'wh
at's my name?',
    chat_history: [
    new HumanMessage('hi! my name is cob'),
    new AIMessage('Hello Cob! How can I 
assist you today?'),
    ],
    });

Thanks
```
---

     
 
all -  [ Was reading through the docs. What is the difference between putting the chat history in the chat pr ](https://www.reddit.com/r/LangChain/comments/1hngbcp/was_reading_through_the_docs_what_is_the/) , 2025-01-01-0914
```
Just wanted to know the difference between putting the history here:

const prompt = ChatPromptTemplate.fromMessages(\[ 
 
  \['system', 'You are a helpful assistant'\],  
  \['placeholder', '{chat\_history}'\],  
  \['human', '{input}'\],  

  \['placeholder', '{agent\_scratchpad}'\],  
\]);

vs here:

const result2 = await agentExecutor.invoke({  
  input: '
what's my name?',  
  chat\_history: \[  
new HumanMessage('hi! my name is cob'),  
new AIMessage('Hello Cob! How can I 
assist you today?'),  
  \],  
});

  
Thanks
```
---

     
 
all -  [ How does AI understand us (Or what are embeddings)? ](https://open.substack.com/pub/diamantai/p/how-ai-understands-us-the-secret?r=336pe4&utm_campaign=post&utm_medium=web&showWelcomeOnShare=true) , 2025-01-01-0914
```
Ever wondered how AI can actually “understand” language? The answer lies in embeddings—a powerful technique that maps wo
rds into a multidimensional space. This allows AI to differentiate between “The light is bright” and “She has a bright f
uture.”

I’ve written a blog post explaining how embeddings work intuitively with examples. hope you'll like it :)
```
---

     
