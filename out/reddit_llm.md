 
all -  [ I spent a few days aggregating LLM performance metrics, token cost, and context size with all source ](https://thepi.pe/evals) , 2024-07-18-0911
```

```
---

     
 
all -  [ langchain, instructor, or something else for my use case? ](https://www.reddit.com/r/LangChain/comments/1e5wf7u/langchain_instructor_or_something_else_for_my_use/) , 2024-07-18-0911
```
I am currently building a streamlit app from 'scratch' without any llm libraries, just using api calls to openrouter and
 pinecone, along with some custom classes to handle the app's state management, conversation history, context truncation
 etc.

The basic idea of the app is to chat with an LLM to develop a marketing targeting campaign. 

It starts with an a
pi call to perplexity to research a company and receive back a target audience description. This is passed to a multi-tu
rn chain of thought refining and eventually outputting valid json that includes targeted and excluded 'hypothetical data
 segments' for a marketing campaign. These are hypothetical descriptions of data segments that might be available on an 
advertising data marketplace like 'coffee enthusiasts' or 'parents with children under 18' etc.

Once the initial audien
ce plan is generated, there is an opportunity for a user to 'chat' with the plan. It is similar to the claude artifact s
ystem where your comments lead to changes in a 'document'. In this case the document is stored as json, and it updates a
 user interface with the set of included and excluded segments displayed as clickable boxes. There also a few buttons wh
ich basically construct predefined prompts that can be sent to the llm, asking it to change the document in particular w
ays.  
  
Once the hypothetical plan is developed, there is an api call to pinecone where I have a vector store of \~500
k actual audience segments so that each hypothetical segment returns an actual segment with a reranking function to pick
 the best one.

The part that is getting difficult to manage in this 'from scratch' way is the user feedback on the json
 audience plan. Often it works great, but there are certain moments where the LLM returns JSON in a format not expected 
by the UI-renderer. I am presently patching all these as they come up via both prompt engineering and output parsing stu
ff, but it feels a bit hard to maintain, especially if we want to add features. If anyone has made it this far into the 
post I would love to hear advice on how to make this app more maintainable... a few possibilities I might pursue are the
 following:  
1. Any time the expected json is not met, manually send the llm a message indicating the needed format, al
ong with conversation history, and then parse its response for the correct json. The needed format could be stored as pa
rt of the app's state so it can be returned easily to the llm at any time.  
2. Implement instructor to more easily mana
ge the data validation and retries  
3. rebuild using langchain  
4. any other ideas?

  
Thanks so much for reading.
```
---

     
 
all -  [ 100% in browser LLM using langchain and WebLLM ](https://www.reddit.com/r/LangChain/comments/1e5sp47/100_in_browser_llm_using_langchain_and_webllm/) , 2024-07-18-0911
```
https://youtu.be/MHuvSuK2dnY?si=qtHWZlmNom7E-RtS
```
---

     
 
all -  [ How do you structure the conversation? ](https://www.reddit.com/r/LangChain/comments/1e5s323/how_do_you_structure_the_conversation/) , 2024-07-18-0911
```
What additional supporting frameworks do you use in order to structure the conversation ? Is the only alternative Langra
ph ?
```
---

     
 
all -  [ Question about langchain api calls ](https://www.reddit.com/r/LangChain/comments/1e5ricy/question_about_langchain_api_calls/) , 2024-07-18-0911
```
I am using langchain chain class for summarization. When I invoke() the chain for summarization, where do the computatio
ns occur? In my deployment compute or where the LLM I am using is hosted? Pretty confused about it since I need to alloc
ate enough memory for doing some summarization task and I’m unsure of it. I know invoke() is I/O bound but that being sa
id does the  resource allocation for my API deployment that calls langchain chain() matter? 
```
---

     
 
all -  [ Optimal RAG for text-2-sql ](https://www.reddit.com/r/LangChain/comments/1e5pe1a/optimal_rag_for_text2sql/) , 2024-07-18-0911
```
I'm building a simple text-2-sql application leveraging Llama-3-7B model on bedrock. My db is on postgresql . The schema
 is fairly complex with 25 tables with an average of 10 columns per table. The tables have primary key, foreign key and 
unique key setup. 

At the moment, I have exported the schema for each table as a document and have pushed it into vecto
r db as a collection. Similarly, I've summarised each table's schema with added context and pushed the same into vector 
db as another collection too. The vectorDB I am using is ChromaDB. the n\_results I've set is 4 and the similarity searc
h algo is cosine similarity. 

My Prompt instructs the model to consider the tables and the summarises along with a few 
sanitisation techniques and then generate a sql query. 

The challenge and the difficulty I am facing is that when I typ
e in a query that is simple user english, the RAG fetches 4 most common tables. And sometime it often assume Join with k
eys/column name that are diverse and do not match. And sometimes, it just hallucinaties. 

To keep my context window in 
check, I simply can't feed the 8-10 relevant schemas from the vectorDB. Is there a way I can mitigate the challenges and
 modify my RAG to suit my usecase. 

Thanks in advance


```
---

     
 
all -  [ Solving the out-of-context chunk problem for RAG ](https://www.reddit.com/r/LangChain/comments/1e5le9h/solving_the_outofcontext_chunk_problem_for_rag/) , 2024-07-18-0911
```
Many of the problems developers face with RAG come down to this: Individual chunks don’t contain sufficient context to b
e properly used by the retrieval system or the LLM. This leads to the inability to answer seemingly simple questions and
, more worryingly, hallucinations.

Examples of this problem

* Chunks oftentimes refer to their subject via implicit re
ferences and pronouns. This causes them to not be retrieved when they should be, or to not be properly understood by the
 LLM.
* Individual chunks oftentimes don’t contain the complete answer to a question. The answer may be scattered across
 a few adjacent chunks.
* Adjacent chunks presented to the LLM out of order cause confusion and can lead to hallucinatio
ns.
* Naive chunking can lead to text being split “mid-thought” leaving neither chunk with useful context.
* Individual 
chunks oftentimes only make sense in the context of the entire section or document, and can be misleading when read on t
heir own.

# What would a solution look like?

We’ve found that there are two methods that together solve the bulk of th
ese problems.

**Contextual chunk headers**

The idea here is to add in higher-level context to the chunk by prepending 
a chunk header. This chunk header could be as simple as just the document title, or it could use a combination of docume
nt title, a concise document summary, and the full hierarchy of section and sub-section titles.

**Chunks -> segments**


Large chunks provide better context to the LLM than small chunks, but they also make it harder to precisely retrieve sp
ecific pieces of information. Some queries (like simple factoid questions) are best handled by small chunks, while other
 queries (like higher-level questions) require very large chunks. What we really need is a more dynamic system that can 
retrieve short chunks when that's all that's needed, but can also retrieve very large chunks when required. How do we do
 that?

# Break the document into sections

Information about the section a chunk comes from can provide important conte
xt, so our first step will be to break the document into semantically cohesive sections. There are many ways to do this,
 but we’ll use a semantic sectioning approach. This works by annotating the document with line numbers and then promptin
g an LLM to identify the starting and ending lines for each “semantically cohesive section.” These sections should be an
ywhere from a few paragraphs to a few pages long. These sections will then get broken into smaller chunks if needed.

We
’ll use Nike’s 2023 10-K to illustrate this. Here are the first 10 sections we identified:

https://preview.redd.it/8ux5
h0drl3dd1.png?width=1260&format=png&auto=webp&s=be590f246f7e06d387e1f0a6952b19b0222c209d

# Add contextual chunk headers


https://preview.redd.it/ow83jnzsl3dd1.png?width=1200&format=png&auto=webp&s=f59e39f143ee8510559ec105fdd0f585ac395786


The purpose of the chunk header is to add context to the chunk text. Rather than using the chunk text by itself when emb
edding and reranking the chunk, we use the concatenation of the chunk header and the chunk text, as shown in the image a
bove. This helps the ranking models (embeddings and rerankers) retrieve the correct chunks, even when the chunk text its
elf has implicit references and pronouns that make it unclear what it’s about. For this example, we just use the documen
t title and the section title as context. But there are many ways to do this. We’ve also seen great results with using a
 concise document summary as the chunk header, for example.

Let’s see how much of an impact the chunk header has for th
e chunk shown above.

https://preview.redd.it/y1xux1ful3dd1.png?width=1352&format=png&auto=webp&s=27397c923761da40c91fee
4e9406d3a40ba15219

# Chunks -> segments

Now let’s run a query and visualize chunk relevance across the entire document
. We’ll use the query “Nike stock-based compensation expenses.”

https://preview.redd.it/6df9gflwl3dd1.png?width=1001&fo
rmat=png&auto=webp&s=1e3a2e9c8fc360d98e2fbb3a6934f8320b89317e

In the plot above, the x-axis represents the chunk index.
 The first chunk in the document has index 0, the next chunk has index 1, etc. There are 483 chunks in total for this do
cument. The y-axis represents the relevance of each chunk to the query. Viewing it this way lets us see how relevant chu
nks tend to be clustered in one or more sections of a document. For this query we can see that there’s a cluster of rele
vant chunks around index 400, which likely indicates there’s a multi-page section of the document that covers the topic 
we’re interested in. Not all queries will have clusters of relevant chunks like this. Queries for specific pieces of inf
ormation where the answer is likely to be contained in a single chunk may just have one or two isolated chunks that are 
relevant.

**What can we do with these clusters of relevant chunks?**

The core idea is that clusters of relevant chunks
, in their original contiguous form, provide much better context to the LLM than individual chunks can. Now for the hard
 part: how do we actually identify these clusters?

If we can calculate chunk values in such a way that the value of a s
egment is just the sum of the values of its constituent chunks, then finding the optimal segment is a version of the max
imum subarray problem, for which a solution can be found relatively easily. How do we define chunk values in such a way?
 We'll start with the idea that highly relevant chunks are good, and irrelevant chunks are bad. We already have a good m
easure of chunk relevance (shown in the plot above), on a scale of 0-1, so all we need to do is subtract a constant thre
shold value from it. This will turn the chunk value of irrelevant chunks to a negative number, while keeping the values 
of relevant chunks positive. We call this the `irrelevant_chunk_penalty`. A value around 0.2 seems to work well empirica
lly. Lower values will bias the results towards longer segments, and higher values will bias them towards shorter segmen
ts.

For this query, the algorithm identifies chunks 397-410 as the most relevant segment of text from the document. It 
also identifies chunk 362 as sufficiently relevant to include in the results. Here is what the first segment looks like:


https://preview.redd.it/2irxe9nyl3dd1.png?width=2684&format=png&auto=webp&s=395a06fdad66e57fab10fd67c8c44786c663d4ad


This looks like a great result. Let’s zoom in on the chunk relevance plot for this segment.

https://preview.redd.it/2fg
uxao0m3dd1.png?width=1001&format=png&auto=webp&s=a5a25959a000b7013869a17215c1b762f5a42f7e

Looking at the content of eac
h of these chunks, it's clear that chunks 397-401 are highly relevant, as expected. But looking closely at chunks 402-40
4 (this is the section about stock options), we can see they're actually also relevant, despite being marked as irreleva
nt by our ranking model. This is a common theme: chunks that are marked as not relevant, but are sandwiched between high
ly relevant chunks, are oftentimes quite relevant. In this case, the chunks were about stock option valuation, so while 
they weren't explicitly discussing stock-based compensation expenses (which is what we were searching for), in the conte
xt of the surrounding chunks it's clear that they are actually relevant. So in addition to providing more complete conte
xt to the LLM, this method of dynamically constructing segments of relevant text also makes our retrieval system less se
nsitive to mistakes made by the ranking model.

# Try it for yourself

If you want to give these methods a try, we’ve op
en-sourced a retrieval engine that implements these methods, called [dsRAG](https://github.com/D-Star-AI/dsRAG). You can
 also play around with the [iPython notebook](https://github.com/D-Star-AI/dsRAG/blob/main/examples/dsRAG_motivation.ipy
nb) we used to run these examples and generate the plots. And if you want to use this with LangChain, we have a [LangCha
in custom retriever](https://github.com/D-Star-AI/dsRAG/blob/main/integrations/langchain_retriever.py) implementation as
 well.
```
---

     
 
all -  [ Evaluate RAG pipelines ](https://www.reddit.com/r/LangChain/comments/1e5jw84/evaluate_rag_pipelines/) , 2024-07-18-0911
```
New tool for evaluating RAG pipelines with local models

I've released a RagRelevanceEvaluator that works with open-sour
ce models. Key features:

- Test chunk sizes and top K retrieval settings
- Get relevance scores for retrieved passages

- No external API needed - uses fine tuned local models
- Integrates with LangChain or other orchestrators

Great for op
timizing RAG performance locally. Helps tune parameters and compare configurations objectively.

Runs completely locally
 for quick iteration without API costs or privacy concerns.

GitHub: https://github.com/grounded-ai/grounded_ai
HuggingF
ace: https://huggingface.co/grounded-ai
```
---

     
 
all -  [ The Prompt Report: A Systematic Survey of Prompting Techniques ](https://www.reddit.com/r/LangChain/comments/1e5fyq9/the_prompt_report_a_systematic_survey_of/) , 2024-07-18-0911
```
'The Prompt Report: A Systematic Survey of Prompting Techniques' offers a detailed review of prompting techniques in AI.
 It introduces a taxonomy of 33 terms, 58 textual and 40 multimodal techniques. The study covers terminology, safety, ev
aluation, and practical applications across various languages and modalities. It also discusses the evolution and challe
nges of prompting in AI, emphasizing its importance in the development of generative models. The report aims to standard
ize prompting practices and address existing gaps in the literature.
```
---

     
 
all -  [ Need Help with Llama3 and Ollama RAG. ](https://www.reddit.com/r/ollama/comments/1e5eyfy/need_help_with_llama3_and_ollama_rag/) , 2024-07-18-0911
```
I'm a very newbie to RAG applications and I'm trying to create a Retrieval-Augmented Generation (RAG) system using Llama
3 and Ollama. I followed some tutorials on youtube, but for some reason every time I run the code, the embeddings get cr
eated(as shown in the progress bar), and nothing happens. Nothing after is getting executed. 

Here's my code.



    fr
om langchain_community.document_loaders import TextLoader
    from langchain_text_splitters import RecursiveCharacterTex
tSplitter
    from langchain.schema.document import Document
    from langchain_community.embeddings import OllamaEmbedd
ings
    from langchain_community.vectorstores import Chroma
    from langchain_community.chat_models import ChatOllama

    from langchain.prompts import ChatPromptTemplate
    from langchain.schema.runnable import RunnablePassthrough
    f
rom langchain.schema.output_parser import StrOutputParser
    import ollama
    
    # Load data
    loader = TextLoader
('Framer-motion.txt')
    data = loader.load()
    
    # Split data
    text_splitter = RecursiveCharacterTextSplitter(
chunk_size=7500, chunk_overlap=100)
    splits = text_splitter.split_documents(data)
    
    # Generate embeddings
    
print('Generating embeddings...')
    embeddings = OllamaEmbeddings(model='llama3', show_progress=True)
    vectorStore 
= Chroma.from_documents(documents=splits, embedding=embeddings)
    
    # Define the LLM function
    def Ollama_llm(qu
estion, context):
        formatted_prompt = f'Question: {question}\n\nContext: {context}'
        try:
            resp
onse = ollama.chat(model='llama3', messages=[{'role':'user', 'content':formatted_prompt}])
            return response['
message']['content']
        except Exception as e:
            print(f'Error in Ollama_llm: {e}')
            return No
ne
    
    # Define the retriever
    retriever = vectorStore.as_retriever()
    
    # Combine retrieved documents
   
 def combine_docs(docs):
        return '\n\n'.join(doc.page_content for doc in docs)
    
    # Define the RAG chain fu
nction
    def rag_chain(question):
        print('Retrieving documents...')
        try:
            retrieved_docs = r
etriever.invoke(question)
            print(f'Retrieved {len(retrieved_docs)} documents.')
            formatted_context
 = combine_docs(retrieved_docs)
            return Ollama_llm(question, formatted_context)
        except Exception as e
:
            print(f'Error in rag_chain: {e}')
            return None
    
    print('Embeddings done')
    result = r
ag_chain('What is the text about?')
    
    if result:
        print(result)
    else:
        print('No result returne
d.')
    
    
    

https://preview.redd.it/43pfa7wq42dd1.png?width=1113&format=png&auto=webp&s=ce75a3d664e37ed012ef59d
d1da5c2e68c6d3443

  
Can anybody please tell me where/what I'm doing wrong? 

  
Thank you.

  

```
---

     
 
all -  [ Problematic integration of a session's ChatMessageHistory in PDF RAG app  ](https://www.reddit.com/r/LangChain/comments/1e5ey22/problematic_integration_of_a_sessions/) , 2024-07-18-0911
```
Hi , I'm new to AI and currently developing a PDF RAG app . I've attached a code snippet below .

    # Initialize store
 if not in session state
    if 'store' not in st.session_state:
        st.session_state.store = {}
    
    ### Statef
ully manage chat history ###
    store = {}
    
    def get_session_history(session_id: str) -> BaseChatMessageHistory:

        if session_id not in st.session_state.store:
            st.session_state.store[session_id] = ChatMessageHistor
y()
        return st.session_state.store[session_id]
    
    
    # generate response 
    def generate_response(promp
t: str) :
        contextualize_q_system_prompt = (
            'Given a chat history and the latest user question '
   
         'which might reference context in the chat history, '
            'formulate a standalone question which can be
 understood '
            'without the chat history. Do NOT answer the question, '
            'just reformulate it if n
eeded and otherwise return it as is.'
        )
        
        contextualize_q_prompt = ChatPromptTemplate.from_messag
es(
            [
                ('system', contextualize_q_system_prompt),
                MessagesPlaceholder('chat_h
istory'),
                ('human', '{input}'),
            ]
        )
    
        compression_retriever = reRanker()

    
        history_aware_retriever = create_history_aware_retriever(
            llm, compression_retriever, contextua
lize_q_prompt
        )
    
        system_prompt = (
            'You are an assistant for question-answering tasks. '

            'Use the following pieces of retrieved context to answer '
            'the question. If you don't know the
 answer, say that you '
            'don't know.'
            '\n\n'
            '{context}'
        )
    
        chat
Prompt = ChatPromptTemplate.from_messages(
            [
                ('system', system_prompt),
                Mess
agesPlaceholder('chat_history'),
                ('human', '{input}'),
            ]
        )
        
        question
_answer_chain = create_stuff_documents_chain(llm, chatPrompt)
    
        rag_chain = create_retrieval_chain(history_aw
are_retriever, question_answer_chain)
    
        conversational_rag_chain = RunnableWithMessageHistory(
            ra
g_chain,
            get_session_history,
            input_messages_key='input',
            output_messages_key='answe
r',
            history_messages_key='chat_history',
        )
        
        for chunk in conversational_rag_chain.st
ream(input={'input': prompt},config={'configurable': {'session_id': 'uniqueValue1234'}}):
            answer_chunk = chu
nk.get('answer')
            if answer_chunk:
                yield answer_chunk
    
    
    # Render chat history
   
 session_id = 'uniqueValue1234'  # Define your session ID
    
    if 'chat_history' not in st.session_state:
        st
.session_state.chat_history = []
    
    # Conversation History
    for message in st.session_state.chat_history:
     
   if isinstance(message,HumanMessage):
            with st.chat_message('Human'):
                st.markdown(message.c
ontent)
        else:
            with st.chat_message('AI'):
                st.markdown(message.content)
    
    
   
 prompt = st.chat_input('Hey, What's up?')
    
    if prompt is not None and prompt !='' :
        st.session_state.cha
t_history.append(HumanMessage(prompt))
        with st.chat_message('Human'):
            st.markdown(prompt)
    
     
   if len(pc.list_indexes()) == 0:
            st.error('Please upload some files first!')
        else:
            wit
h st.chat_message('AI'):
                ai_response = st.write_stream(generate_response(prompt))
    
            st.se
ssion_state.chat_history.append(AIMessage(ai_response))
    

In this code I have 2 session states 'store' and 'chat\_hi
story' .  
  
The 'store' will have a key 'session\_id' and its value is the Chat History for the session . This contain
s a list of Human and AI messages .   
  
This is maintained on its own , I didn't write code for this , this is maybe a
 side effect of 'create\_retriever\_chain' , 'create\_stuff\_documents\_chain' and 'create\_history\_aware\_retriever' c
lasses that I've used . Whenever , I ask a question from LLM , the question along with the response gets stored on its o
wn .

Now , on the other hand , I manage 'chat\_history' myself . I append user's query to it , then after LLM gives me 
response , I append it as well .

You can see that I've code for rendering Conversation History ( using chat\_history )


    # Conversation History
    for message in st.session_state.chat_history:
        if isinstance(message,HumanMessage
):
            with st.chat_message('Human'):
                st.markdown(message.content)
        else:
            wit
h st.chat_message('AI'):
                st.markdown(message.content)

This looks unnecessary , I think there should be 
a way to render Conversation History using the 'store' because this store has 'session\_id' and this 'session\_id' value
 is the chat history for that session .  
  
I've tried to build logic to get this but no success so far , can anybody g
uide me ?
```
---

     
 
all -  [ State of the art about LLMs and Databases ](https://www.reddit.com/r/LangChain/comments/1e5dmbf/state_of_the_art_about_llms_and_databases/) , 2024-07-18-0911
```
Which is the state-of-the-art in LLMs and Databases?

Which one is better in your experience: 

* text-to-SQL 
* pandasa
i 
* Database to vector database and RAG
* Another tool
```
---

     
 
all -  [ Can I build a chatbot that uses just around 10 small txt files on my web page that uses only Vanilla ](https://www.reddit.com/r/LangChain/comments/1e5cex5/can_i_build_a_chatbot_that_uses_just_around_10/) , 2024-07-18-0911
```
Sorry if the question is dumb, but I'm a beginner in this, and all tutorials I can find are using either Node.js or Next
.js.  
Thank you!
```
---

     
 
all -  [ How to use StructuredTool class from Langchain in Langraph ](https://www.reddit.com/r/LangChain/comments/1e5bgzh/how_to_use_structuredtool_class_from_langchain_in/) , 2024-07-18-0911
```
I want to to use Tools (explicitly defined as classes) when adding them as a node in the graph.

Currently we just have 
tools mentioned as functions and use RunnableLambda like below  

graph\_builder.add\_node(node\_name, RunnableLambda(to
ol) | (lambda observation : {'observation' : observation} )
```
---

     
 
all -  [ How do you choose a model? ](https://www.reddit.com/r/LangChain/comments/1e5b9f7/how_do_you_choose_a_model/) , 2024-07-18-0911
```
When you are starting a new project, how do you choose which model you are going to use? 

Even when we look at only tex
t generation models, there are so many and things change every day. What do you go with? and how do you decide?
```
---

     
 
all -  [ Langchain Help ](https://www.reddit.com/r/LangChain/comments/1e5b6ba/langchain_help/) , 2024-07-18-0911
```
Sorry for the potentially dumb question and lack of understanding probably.

  
I want to make an app and be able to fee
d and LLM csv and json data via RAG, and continue to use the model afterwards without having to re-feed the model older 
data each time. How can I save my model and reuse it continuously?

If you have any recommended resources for me to use 
or go through.
```
---

     
 
all -  [ Free hosting with 3GB? ](https://www.reddit.com/r/flask/comments/1e5azl0/free_hosting_with_3gb/) , 2024-07-18-0911
```
I made a simple RAG app that uses an external LLM API, but the dependencies itself cross 2GB(llamaindex/langchain/huggin
gface). Is there any free option to host it? Or is there any way I can implement this functionality with more lightweigh
t libraries?
```
---

     
 
all -  [ What's your biggest holdup in taking AI to production?
 ](https://www.reddit.com/r/LangChain/comments/1e54hjr/whats_your_biggest_holdup_in_taking_ai_to/) , 2024-07-18-0911
```
I figured it'd be interesting to get input from different people and industries on this. There are probably a million re
asons out there, from lack of executive buy-in to inconsistent RAG results. What are the current roadblocks everyones fa
cing?
```
---

     
 
all -  [ Practical Applications of Pythia in LLM Contexts: Chatbots, RAG Systems, and Summarization ](https://www.reddit.com/r/pythia/comments/1e52lyy/practical_applications_of_pythia_in_llm_contexts/) , 2024-07-18-0911
```
https://preview.redd.it/7pz9aa0teycd1.png?width=1920&format=png&auto=webp&s=701ca9ff431570cebcee5407258f16d19e97b136

*E
xplore the practical applications of Pythia and how it addresses LLM contexts to achieve reliable AI.*

[Pythia](https:/
/askpythia.ai/blog/introducing-pythia-the-ai-oracle-eradicating-llm-hallucinations) is a powerful hallucination detectio
n tool that detects [misinformation in large language model (LLM) outputs](https://www.weforum.org/agenda/2024/01/ai-dis
information-global-risks/) and ensures reliable interaction between AI and humans. It helps LLM developers and companies
 reduce error rates in LLM outputs, avoid spending millions on corrective procedures and legal liabilities, and maintain
 a good reputation among users.

Pythia’s unique [methodology](https://www.wisecube.ai/blog/the-wisecube-approach-to-enh
ancing-ai-reliability/) consists of claim extraction and categorization, real-time monitoring, and knowledge graph integ
ration to verify LLM response against legitimate sources of information. This enables Pythia to easily integrate with ch
atbots, RAG-based systems, and text summarization tools for real-time monitoring. It flags inappropriate outputs and gen
erates a detailed audit report highlighting the tool’s strengths and weaknesses. 

This feature allows developers and su
bject matter experts to work towards improving LLMs to mitigate hallucinations and serve their original purpose.

Let’s 
explore some of the Pythia use cases and how they address the LLM contexts in the real world.

# Pythia Use Cases

Here 
are the three common use cases of Pythia:

# Chatbots

Healthcare chatbots use natural language processing (NLP) to assi
st patients with medical support, such as assessing symptoms, appointment scheduling, or providing mental support. These
 chatbots are trained on medical databases to learn and improve their accuracy. Based on their learning, chatbots analyz
e user input and generate a relevant response for the user.

Pythia integrates within healthcare chatbots to monitor LLM
 responses against user queries. It measures the accuracy and alignment of the response with the user query by continuou
sly monitoring LLM activities. Whenever a user asks a question, and LLM generates a response, Pythia extracts knowledge 
triplets from the response and chatbot databases. It then compares knowledge triplets against each other to generate an 
LLM audit report.

# RAG (Retrieval-Augmented Generation) systems

[RAG systems](https://askpythia.ai/blog/a-guide-to-in
tegrating-pythia-api-with-rag-based-systems-using-wisecube-python-sdk) use an additional knowledge base beyond the train
ing data, adding an extra LLM claim verification layer. However, RAG systems can still generate nonsensical outputs due 
to the knowledge base's existing bias or limited relevant resources.

Like chatbots, Pythia integrates with RAG systems 
to detect [hallucinations in LLM responses](https://askpythia.ai/blog/understanding-ai-hallucinations-what-they-are-and-
why-they-matter). Once integrated, it continuously monitors the system performance in real-time using accuracy and task-
specific metrics and highlights the performance in Pythia UI. This enables LLM developers and stakeholders to make immed
iate corrective decisions and improve user experience. 

# Text Summarization

Healthcare text summarization involves co
ndensing large texts, such as medical reports or clinical documents, into shorter summaries while retaining the essentia
l information. Several machine learning and statistical methods assist LLMs in generating summaries of large, complex te
xts.

Accurately processing medical terminology, protecting sensitive information, and preserving information are common
 challenges text summarization systems face. These challenges result in generating inaccurate summaries or losing inform
ation and the meaning of the actual text.

Pythia effortlessly compares summarization tool outputs with its knowledge ba
se and ensures the generated summary doesn’t disregard essential information. It can also use a knowledge graph to ensur
e accurate, relevant, and up-to-date claims.

Pythia’s ability to integrate with LangChain makes it a go-to hallucinatio
n detection tool for LLM developers. This integration allows developers to leverage Pythia's full potential with effortl
ess interoperability. It also ensures RAG developers can access a comprehensive toolkit for developing reliable AI.

# P
ythia’s Ability to Address LLM Contexts

LLM context refers to the information an LLM uses to generate outputs. The cont
exts vary with LLM applications such as chatbots or RAG; understanding them is essential for effectively interpreting ou
tputs. 

# What are the three LLM contexts?

Below are the three LLM contexts and how they differ:

https://preview.redd
.it/m9avh7y6oycd1.png?width=2880&format=png&auto=webp&s=817b9adac13bd40beeb43be768d2b230d301e9aa

# Zero Context

Zero c
ontext refers to user prompts that ask for factual knowledge and don’t include any contextual information. LLM's respons
e to these prompts only relies on user queries and general knowledge of LLM based on its training.

For example, if a us
er asks, “***What is stevia used for?***”, the model answers, “***Stevia is a sweetener and sugar substitute derived fro
m the leaves of the Stevia rebaudiana plant. It is known for its intensely sweet taste without the calories of sugar.***
”

# Noisy Context

Noisy context refers to user prompts where the context includes irrelevant or misleading information
. This can confuse the model and potentially degrade the quality or accuracy of its responses. 

Here’s an example of a 
noisy context prompt, “***I've had a terrible headache for two weeks, and I'm really worried I have a brain tumor. I rea
d online that headaches are a major symptom.***”

# Accurate Context 

Accurate context means the user query is relevant
, clear, and directly related to the task or query. This helps the model generate precise and contextually appropriate r
esponses.

For example, “***I secured 3 As and 2 Bs in my A-level exams. However, I found that the admission requirement
 for University X is 4 As. What are some alternative options for me that are also in high demand and popular?***”

# How
 does Pythia address the three LLM contexts?

A robust LLM should be able to address the three contexts discussed above.
 An AI reliability solution should be able to assess an LLM’s response to accommodate the contexts.

https://preview.red
d.it/gekirvafoycd1.png?width=2544&format=png&auto=webp&s=5104db069d3380e6f69738ea6eb2e7432733574a

# Chatbots as Zero Co
ntext

Chatbots often encounter zero-context queries for quick medical assistance. These queries generally revolve aroun
d factual knowledge, and chatbots use their training databases to generate a response. However, if the user prompt is un
familiar to the chatbot, it can generate nonsensical outputs.

Pythia monitors chatbot responses to detect when the chat
bot fails to generate relevant outputs. Here’s how it works:

1. A user enters a query into the chatbot.
2. The chatbot 
generates an answer.
3. Pythia compares the answer to the chatbot’s knowledge base.
4. Pythia generates an audit report 
based on the comparison.



As a result, Pythia highlights when the chatbot deviates from its knowledge base and creates
 nonsensical outputs. For example, if a user asks, “***What is subrogation in insurance?***” when the chatbot is designe
d to assist insurance clients with customer support, it might generate an irrelevant output. When Pythia compares the ou
tput with the chatbot’s database, it identifies the irrelevant output and flags it. Finally, chatbot developers can debu
g the logic and improve its performance depending on their objectives. 

This allows chatbot developers and companies to
 provide a safe interaction between chatbots and end-users.

Here’s how to integrate Pythia in chatbots for zero-context
 LLM hallucination detection:

1. Develop a chatbot.
2. Install Wisecube and authenticate Pythia.
3. Integrate Pythia in
to your workflow.
4. Detect real-time hallucinations in chatbot responses.



# RAG Systems as Noisy Context

RAG system
s rely on external information sources to generate responses. Therefore, the accuracy of RAG systems is highly dependent
 on the accuracy of external sources. However, Pythia can compare RAG-based systems’ claims through an extensive knowled
ge graph, adding an extra verification layer. 

RAG systems often encounter noisy user prompts, and to ensure the reliab
ility of responses, they must be able to understand user context. Unlike traditional hallucination detection tools, Pyth
ia extracts claims from AI-generated output and knowledge bases as knowledge triplets. Knowledge triplets divide a sente
nce into **<subject, predicate, object>** format, revealing the relationship between subject and object to the RAG syste
m. 

For example, if a user asks, “***Leonard McCoy underwent a Prostate TRUS biopsy last week. He now feels a severe he
adache and a racing heartbeat. Please tell me risk-free solutions to ease his pain.***” to a RAG system, here’s how Pyth
ia dissects this prompt using knowledge triplets: **Subject:** *Leonard McCoy* **Predicate:** *underwent* **Object:** *P
rostate TRUS biopsy*

**Subject:** *Leonard McCoy* **Predicate:** *has* **Object:** *severe headache and raced heartbeat
*

This way, Pythia can interpret user concerns and detect the relevancy of the response through claim comparison. Since
 conventional methods don’t break sentences into this format, they only capture keywords like “***Prostate TRUS biopsy**
*” and generate a general result.

Based on the claim comparison, Pythia categorizes them into “*entailment*”, “*neutral
”*, “*contradiction*”, and “*missing facts*”. Finally, it generates an audit report, highlighting the performance of RAG
 systems so you can take necessary measures to improve its performance. Therefore, if your RAG system generates a genera
l output without understanding the user query, Pythia helps you identify that in real time and deliver a better experien
ce to end-users. 

Here’s [how to integrate Pythia in RAG systems](https://askpythia.ai/blog/a-guide-to-integrating-pyth
ia-api-with-rag-based-systems-using-wisecube-python-sdk) for noisy context LLM hallucination detection:

1. Develop a RA
G system.
2. Install Wisecube and authenticate Pythia.
3. Integrate Pythia into your workflow.
4. Detect hallucinations 
in RAG outputs.



Head over to Pythia docs for a detailed guide on [integrating Pythia in RAG systems](https://askpythi
a.ai/docs/integrate-pythia-with-rag-based-systems).

# Text Summarization as Accurate Context

Text summarization softwa
re usually processes queries providing clear information about the user's needs. This can include a summary of a detaile
d medical report, focusing on the key findings and recommendations. As a response, the software condenses large volumes 
of medical text, such as reports or clinical documents, into shorter summaries that retain the essential information. 


With the rise in AI content detectors, users sometimes demand summarization software to generate a human-like summary. T
his might confuse AI, resulting in missing information in the generated summary. Therefore, accurate processing of medic
al terminology, protecting sensitive information, and preserving the meaning of the original text are the challenges in 
this context.

Here’s how Pythia helps text summarization software to generate accurate summaries:

1. Knowledge triplet
s break down the relationship between phrases and sentences.
2. Claim comparison ensures the summary preserves the origi
nal message.
3. Optional knowledge graph check adds an extra verification layer.



For example, if a user enters a rese
arch paper for summarization, the software generates a summary, and Pythia detects this activity in real time. With the 
help of knowledge triplets, Pythia extracts the following key claims from the medical report: **Subject:** *Eigenvalues 
of the matrix and the stability of the system* **Predicate:** *are* **Object:** *significantly correlated*

**Subject:**
 *Theorem* **Predicate:** *shows* **Object:** *95% confidence interval*

However, the software overlooks the second clai
m in the summary. Pythia will immediately flag it as “*missing facts*”, guiding the developers to look into the underlyi
ng errors.

Similar to the other use cases, integrating Pythia in text summarization software for accurate context LLM h
allucinations:

1. Develop a text summarization software.
2. Install Wisecube and authenticate Pythia.
3. Integrate Pyth
ia into your workflow.
4. Detect hallucinations in AI-generated summaries.



[**Continuous online monitoring and compar
ison**](https://askpythia.ai/blog/why-continuous-monitoring-is-essential-for-maintaining-ai-integrity) of LLM claims and
 references identify when an LLM fails to generate appropriate responses for all LLM contexts. This includes examining t
he relevancy of responses against user queries, assessing the accuracy of claims, and giving insights into the model’s l
imitations.

Pythia UI displays model performance through visualizations and sends SMS alerts whenever an event occurs s
o you can track the LLM performance and your spending.

Start using [**Pythia**](https://askpythia.ai/) today to detect 
real-time hallucinations in your LLMs and improve their performance for reliable outcomes.



*The article was originall
y published on* [Pythia's website.](https://askpythia.ai/blog/practical-applications-of-pythia-in-llm-contexts-chatbots-
rag-systems-and-summarization)
```
---

     
 
all -  [ GenAI for automatic insights from data ](https://www.reddit.com/r/LangChain/comments/1e4xjhu/genai_for_automatic_insights_from_data/) , 2024-07-18-0911
```
Was wondering what tools exist for generating automatic insights from data. For example you feed in a large data set and
 based on the context of the data set a genAI tool is able to tell you insights positive or negative that are useful. Th
ings like 'Revenue has grown by 10% since last month' or 'Customer X usage has dropped since \_\_'. I've found some gene
rative BI tools online but my use case requires something that's more of a dev tool. Also, open to hearing about ideas o
f how to do something like this from scratch.
```
---

     
 
all -  [ creating SEO assistants using LLMs, RAG, GraphRAG/knowledge graph ](https://www.reddit.com/r/TechSEO/comments/1e4swxs/creating_seo_assistants_using_llms_rag/) , 2024-07-18-0911
```
I published yesterday an article on Search Engine Journal about a POC that we developed for creating an SEO assistant.


This assistant uses Retrieval-Augmented Generation (RAG) and GraphRAG to provide access to a SEO knowledge base and SaaS
 tools. More precisely, using external sources (litterature, but also access to SEO tools through APIs), we construct a 
knowledge graph using langchain, llamaindex and a nebula graph datastorage.

I strongly believe that implementing such s
ystems is game-changer for SEO tasks (more productivity, better strategies). I encourage everyone to replicate our POC, 
for which I’ve provided the source code in the article. While adapting it, particularly the knowledge graph aspect via N
ebula, requires effort, it is highly achievable for those that are a little bit familiar with python (and willing to lea
rn a little bit about LLM frameworks).

The SEJ article is here : [https://www.searchenginejournal.com/unlocking-the-pow
er-of-llm-knowledge-graph-introduction/518343/](https://www.searchenginejournal.com/unlocking-the-power-of-llm-knowledge
-graph-introduction/518343/)

And you, do you think - as I do - that this type of assistant is the future of SEO?
```
---

     
 
all -  [ Is There Any Reliable Agentic Tool? ](https://www.reddit.com/r/LangChain/comments/1e4s6xt/is_there_any_reliable_agentic_tool/) , 2024-07-18-0911
```
Hey everyone,

Is there a reliable agentic tool on the market that can operate independently and effectively? So far, I'
ve tried **CrewAI** and have explored **LangGraph**, though I haven't tested it yet. Despite adjusting the max iteration
s, these tools often take a lot of time and work best with OpenAI. However, I want to use them with AWS Bedrock models, 
specifically Mistral or Claude 3.

My primary use case is an internal application where the agent needs to automatically
 decide whether to use a specific agent, perform RAG, or search the web for information. This must be done without compr
omising our confidential company data by sending it to external Search APIs (like Google or DuckDuckGo) and without taki
ng an excessive amount of time to provide answers.

I'd really appreciate any recommendations or advice you can offer.
```
---

     
 
all -  [ GraphRAG+ LangChain  ](https://www.reddit.com/r/Langchaindev/comments/1e4rwpp/graphrag_langchain/) , 2024-07-18-0911
```
GraphRAG is an advanced RAG system that uses Knowledge Graphs instead of Vector DBs improving retrieval. Check out the i
mplementation using GraphQAChain in this video : https://youtu.be/wZHkeon42Aw
```
---

     
 
all -  [ Graph with a for loop ](https://www.reddit.com/r/LangChain/comments/1e4rcha/graph_with_a_for_loop/) , 2024-07-18-0911
```
Hi,

I need some clarifications. In my use case the first step requires an LLM to identify and split different segment o
f the input text / document. Then, for each of the segments I have a linear flow to follow (extract info, call agents, .
..). Finally I have to collect all the outputs.

I am unsure how to achieve the 'for loop' (if possible). Instead of an 
`add_edge`, I'd need an add edges

    workflow.add_node('split', split)
    workflow.add_node('extract', extract)
    w
orkflow.add_node('collect', collect)
    
    workflow.set_entry_point('split')  # after split I get an array of chunks

    
    workflow.add_edges('split', 'extract')  # for each chunk do some custom logic
    workflow.collect_edges('extra
ct', 'collect')  # collect everything
    
```
---

     
 
all -  [ Which vectorstore should I choose? ](https://www.reddit.com/r/LangChain/comments/1e4r8an/which_vectorstore_should_i_choose/) , 2024-07-18-0911
```
In my use case, the most important thing is accuracy, of retrieved documents from them

I'm going to create vectorstore 
of my codebase, so when codes get updated, I have to update those in my  vectorstore periodically (not all codes will ge
t updated)

Keeping these two things in mind, which one should I go with?
```
---

     
 
all -  [ Q&A RAG over tabular data ](https://www.reddit.com/r/LangChain/comments/1e4pqgn/qa_rag_over_tabular_data/) , 2024-07-18-0911
```
Hello dear community,

I am currently familiarising myself with LLM, especially RAG. I have an idea for a Q&A ChatBot an
d would like to learn how to build one.

I would like to use an Excel spreadsheet with three columns as a database. The 
first column is a typical question. The second column contains tags that describe the question. The third column contain
s an answer to the question.

When the user asks a question, a semantic search should first be performed using the first
 and second columns. This will find the top of the most appropriate questions in a cell. The answers to these questions 
in the third column are provided to the LLM as context.

It is important to me that the structured properties of the tab
le are fully exploited. Conventional RAGs return a fixed chunk size, even if it spans cells. However, I only want to ret
urn the cell that is relevant to the question.

My question is, what is the best way to implement this in LangChain? Doe
s it make sense to store the questions and tags as metadata? Can I do a semantic search on the metadata and give the cel
l with the corresponding answer as context to the LLM? With the ulterior motive of returning only the relevant context? 
I have also thought about a self-query retriever. However, this tends to use keywords for filtering, not quite what I am
 looking for. Or am I on the wrong track?

Kind regards
```
---

     
 
all -  [ 🔥 Apify is hiring Backend engineer for an AI/LLM team (Python / TypeScript) ](https://www.reddit.com/r/devjobspro/comments/1e4pnnk/apify_is_hiring_backend_engineer_for_an_aillm/) , 2024-07-18-0911
```
# 🔥 Apify is hiring Backend engineer for an AI/LLM team (Python / TypeScript)

🔖 Python 🔖 Typescript 🔖 AI 🔖 Node.js 🔖 LL
M 🔖 Langchain 🔖 Llamahub

**Details**

- 📥 **Category**: Backend
- 🧙 **Seniority**: Senior level
- 💻 **Working model**: 
Hybrid
- 🏝️ **Employment type**: Full time


- 📍 **Countries**: Czech Republic

**How to Apply:**

[🟡 Apply here](https:
//devjobspro.com/jobs/119-backend-engineer-for-an-ai-llm-team-python-typescript)
```
---

     
 
all -  [ New here - how do I surface and save historical threads of agent actions and conversations in langgr ](https://www.reddit.com/r/LangChain/comments/1e4masy/new_here_how_do_i_surface_and_save_historical/) , 2024-07-18-0911
```
I've set up a dict of main and sub questions(the answer for each feeds into the next) that build on an initial user requ
est. 

I set up a RAG agent workflow on langgraph and need to debug the overall conversational thread by reading through
 what is generated for each question.

I know I can extract the current state from agent_executor.stream()  but how do I
 get every iteration for every question asked? Is the only way to set up a for loop and print/ save the streamed outputs
 each time?  What does the llm get at each turn in the conversation? Shouldn't it be fed the full history?

Also any way
 to summarize and store a thread for downstream agents to absorb? If so any way to surface that summary for user inspect
ion?


Sorry if this is basic- still learning.
```
---

     
 
all -  [ How do I stream my output using ? ](https://www.reddit.com/r/LangChain/comments/1e4lnd5/how_do_i_stream_my_output_using/) , 2024-07-18-0911
```
     if prompt := st.chat_input('Hey, What's up?'):
        if len(pc.list_indexes()) == 0:
            st.error('Please
 upload some files first!')
        else:
            st.session_state.messages.append({'role': 'user', 'content': promp
t})
    
            contextualize_q_system_prompt = (
                'Given a chat history and the latest user questio
n '
                'which might reference context in the chat history, '
                'formulate a standalone questi
on which can be understood '
                'without the chat history. Do NOT answer the question, '
                'j
ust reformulate it if needed and otherwise return it as is.'
            )
            contextualize_q_prompt = ChatProm
ptTemplate.from_messages(
                [
                    ('system', contextualize_q_system_prompt),
             
       MessagesPlaceholder('chat_history'),
                    ('human', '{input}'),
                ]
            )
  
          # chunks ( 5 )
            compression_retriever = reRanker()
            history_aware_retriever = create_his
tory_aware_retriever(
                llm, compression_retriever, contextualize_q_prompt
            )
    
            
system_prompt = (
                'You are an assistant for question-answering tasks. '
                'Use the followi
ng pieces of retrieved context to answer '
                'the question. If you don't know the answer, say that you '
 
               'don't know.'
                '\n\n'
                '{context}'
            )
    
            chatPromp
t = ChatPromptTemplate.from_messages(
                [
                    ('system', system_prompt),
                 
   MessagesPlaceholder('chat_history'),
                    ('human', '{input}'),
                ]
            )
      
      question_answer_chain = create_stuff_documents_chain(llm, chatPrompt)
    
            rag_chain = create_retrieva
l_chain(history_aware_retriever, question_answer_chain)
    
            conversational_rag_chain = RunnableWithMessageH
istory(
                rag_chain,
                get_session_history,
                input_messages_key='input',
    
            history_messages_key='chat_history',
                output_messages_key='answer',
            )
    
      
      response = conversational_rag_chain.invoke(
                input={'input': prompt},
                config={'conf
igurable': {'session_id': 'hdf23me23edewDFSDMS'}}
            )
            print('response:', response['answer'])
     
       st.session_state.messages.append({'role': 'assistant', 'content': response['answer']})
    
            # Display
 updated messages
            for message in st.session_state.messages:
                with st.chat_message(message['ro
le']):
                    st.markdown(message['content'])



How do I output my response as a stream using Langchain's 
create\_retrieval\_chain ?  
Currently , I get my response when all of it is generated ( at once ) , but I want streamin
g feature instead .
```
---

     
 
all -  [ How to deal with multiple states? ](https://www.reddit.com/r/LangChain/comments/1e4l92y/how_to_deal_with_multiple_states/) , 2024-07-18-0911
```
I'm using supervisor graph and various agent graphs. How do pass state within nodes of child graph and parent graph? I c
ouldn't get what [documentation](https://langchain-ai.github.io/langgraph/how-tos/subgraph/) was trying to say.
```
---

     
 
all -  [ Langgraph: best practices for multiple steps graph ](https://www.reddit.com/r/LangChain/comments/1e4l74f/langgraph_best_practices_for_multiple_steps_graph/) , 2024-07-18-0911
```
Hi! As mentioned before, I have built a langgraph with a supervisor agent and two specialised agents. My question is: wh
at are the best practices for having some of these agents working in multiple steps? For example: one of the agents will
 receive the user input and first present to the user what the agent is about to do and after the user confirms it then 
the agent will finish the work.   
My question is: how do I get the same agent to do both of these steps? Should I add s
ystem prompt to the agent on each step? (For example: adding something like 'In this step now you must do X and display 
Y information to the user'). The problem here is that if there are multiple back and forth interactions between agent an
d user then the system prompt will become long and confusing.   
Other way could be saying to agent 'when you are on ste
p 1 you should focus on this, when you are on step 2 you should focus on that'.

Do any of you have experience with this
 kind of scenario?
```
---

     
 
all -  [ GPT-Instagram : Instagram Viral Posts with user own personality ](https://www.reddit.com/r/LangChain/comments/1e4k0is/gptinstagram_instagram_viral_posts_with_user_own/) , 2024-07-18-0911
```
As a weekend project created a Multi Agent AI app in Next.js, LangChain.js & LangGraph.js to simulate a Marketing depart
ment to recommend Instagram Viral Posts with user own personality.

If anyone interested to try or look at code: [https:
//github.com/MODSetter/gpt-instagram](https://github.com/MODSetter/gpt-instagram)

https://reddit.com/link/1e4k0is/video
/ig7wjanujucd1/player

  

```
---

     
 
all -  [ Developer looking for exciting opportunities ](https://www.reddit.com/r/Entrepreneur/comments/1e4jsp6/developer_looking_for_exciting_opportunities/) , 2024-07-18-0911
```
I'm basically a react native developer with 1 year of experience in app and web development. Altho I'm doing my average 
job right now, I'm dying to work on something real exciting that will help me learn quite alot of things and explore. I 
go around and thought what be better place to explore than that community of some highly ambious entrepreneurs.

Even on
 this normal job I try to explore various fields and takes up work around, but I'm looking for some real excieting probl
ems. I know things like nodejs, go, kotlin, react native, a bit of langchains, devops with docker, aws, etc. Like learni
ng new stuffs 😊

Majorly looking for some early stage startups where I can contribute and learn alot.  
Hope you guys ca
n help 😅
```
---

     
 
all -  [ An open source hub for top python functions that could be used as custom tools for AI projects. ](https://www.reddit.com/r/LocalLLaMA/comments/1e4jb76/an_open_source_hub_for_top_python_functions_that/) , 2024-07-18-0911
```
Hey LocalLLamas,

As I was working daily on my AI projects, I have collected few automation function in python that I fi
nd helpful. An idea came to mind, that if I could make an open source project that gather all of these python hacks into
 one, and crowdsource from others. I believe in the long term will be great for the whole  ecosystem.

So here it is, th
e very first foundation of the project. Current I gathered the top 15 functions, with all source code available to try.


https://reddit.com/link/1e4jb76/video/98n0hsut7vcd1/player

Hope it may be helpful for building your local langchain, l
anggraph app.

🔗 Features:

**Background Remover**: Automatically removes backgrounds from images.

* **QR Code Creator*
*: Easily generates QR codes from URLs.
* **Fake Data Generator**: Creates realistic dummy data for testing.
* **URL Sho
rtener**: Simplifies long URLs into concise ones.
* **YouTube Downloader**: Downloads YouTube videos or audio files.
* *
*Bulk Email Sender**: Sends emails in bulk with ease.
* **Image Scraper**: Fetches and displays images from the web.
* *
*Audiobook Maker**: Converts PDFs into audiobooks.
* **Code Analyzer**: Evaluates Python code using Pylint and Flake8.
*
 **Resource Monitor**: Keeps an eye on your system's resources.
* **Clipboard Tracker**: Logs all texts copied to your c
lipboard.
* **Spell Checker**: Corrects spelling and grammar errors.
* **Link Verifier**: Checks the connectivity of mul
tiple URLs.
* **News Reader**: Reads out loud trending news headlines.
* **Article Summarizer**: Condenses lengthy artic
les into summaries.
*  … and many more! 

💻 Try it out at: [Link](https://autopilot.streamlit.app/)

The Repo: [GitHub -
 Ai-Quill/automated: automated python scripts](https://github.com/Ai-Quill/automated.git)

🙏 C**ontribute: **I would lov
e community contributions! Fork the repo, suggest new scripts, or improve existing ones. 📚 More Info: Check out our GitH
ub repo for detailed instructions, features, and more!

**💬 Feedback: **would love to hear how you are using these pytho
n functions in your local llm tools.
```
---

     
 
all -  [ LangGraph  ](https://www.reddit.com/r/AIFromChina/comments/1e4ir2v/langgraph/) , 2024-07-18-0911
```
LangGraph aims to overcome the major limitation of traditional LangChain chains - that they lack looping at runtime. Thi
s problem can be easily addressed by introducing a graph structure, as graphs can easily introduce loops into chains, wh
ich are essentially directed acyclic graphs (DAGs).

Furthermore, graph tools have shown their power in organizing knowl
edge bases for retrieval-augmented generation (RAG) scenarios. Specifically, they can enhance the 'retrieval' stage to e
nable more meaningful context retrieval, ultimately improving the accuracy of generated responses. To achieve this, our 
strategy is to store the knowledge base in a graph-based database (e.g., Neo4j), leveraging the semantic capabilities of
 LLMs to correctly identify and map entities and relationships.

To realize this goal, LangChain has developed a powerfu
l library called LLMGraphTransformer, which aims to transform unstructured text data into a graph-based representation.


Welcome to follow: [https://aidisruption.substack.com/](https://aidisruption.substack.com/)
```
---

     
 
all -  [ Langgraph Human in the loop in Production ](https://www.reddit.com/r/LangChain/comments/1e4hays/langgraph_human_in_the_loop_in_production/) , 2024-07-18-0911
```
Are there anyone who has successfully done langgraph with human in the loop in production? How does that work? 
```
---

     
 
all -  [ How should I set up my multimodal chatbot? ](https://www.reddit.com/r/LangChain/comments/1e4gvl1/how_should_i_set_up_my_multimodal_chatbot/) , 2024-07-18-0911
```
As of now I have a chatbot (OpenAI embeddings & chat model) that can take in text/pdf files and answer questions about t
hem using embeddings and a vectorDB. I was wondering if it would be plausible to embed an image into the vectorDB, and u
se a multi modal LLM to be able to answer questions about said picture. I've been looking at other approaches (generatin
g text summaries of image and embedding that/sending the image straight to a multimodal LLM with the prompt) but I like 
the idea of embedding images into my vectorDB, and I don't really know the pros/cons between these methods. Any help is 
appreciated !
```
---

     
 
all -  [ How do Graph RAG search for relevant nodes? ](https://www.reddit.com/r/LangChain/comments/1e4c1j5/how_do_graph_rag_search_for_relevant_nodes/) , 2024-07-18-0911
```
Hi everyone, I have been reading around about Graph RAG lately. I don’t quite understand how the retriever searches for 
“relevant entities”? I have thought of exact full text search, but they would not be quite effective when the entities c
an be (and will be!) ambiguous ( e.g. two people with the same name, or same people with different names, etc.). Or mayb
e semantic search is utilized here? If so, I don’t think it would be efficient for a large graph with many entities.
Rea
lly appreciate your help! 
```
---

     
 
MachineLearning -  [ [D] Is Anyone Else Setting Up Real-Time Django Workers for their AI Application? What's the best way ](https://www.reddit.com/r/MachineLearning/comments/1e0qens/d_is_anyone_else_setting_up_realtime_django/) , 2024-07-18-0911
```
We completely underestimated this one tbh, thought it would be much more straight forward. But we've done it now and doc
umented how step by step [in this article series](https://medium.com/p/5828a1ea43a3).

A bit of context, we're building 
a mini free AI Agent that auto-generates manually customisable plots, so the user can basically style however they want.
 It needs to be cost effective and efficient, so we thought about how to do it and tested a couple other ways.

https://
preview.redd.it/cmly0a6bhwbd1.png?width=640&format=png&auto=webp&s=be1f5b2853e744adcaf8013e6d43b43f6be89617

We plan on 
releasing the project open source, so all feedback welcome! Is anyone else doing this and has any feedback? or do know o
f a better way to do it?
```
---

     
 
MachineLearning -  [ [P] Real Time AI Workers Web Application ](https://www.reddit.com/r/MachineLearning/comments/1dzryk9/p_real_time_ai_workers_web_application/) , 2024-07-18-0911
```
Hi everyone!

I've created a mini series on how to build a real time AI application using Django, LangChain and Celery.


Free knowledge - posting it in here for anyone working on something similar and had the same blockers I had when buildi
ng.

Let me know what you think on how I could potentially improve this architecture.

Part 1

[https://medium.com/towar
dsdev/how-to-set-up-django-from-scratch-with-celery-channels-redis-docker-real-time-django-601dff7ada79](https://medium.
com/towardsdev/how-to-set-up-django-from-scratch-with-celery-channels-redis-docker-real-time-django-601dff7ada79)

Part 
2

[https://medium.com/towardsdev/how-to-set-up-django-from-scratch-with-celery-channels-redis-docker-real-time-django-5
828a1ea43a3](https://medium.com/towardsdev/how-to-set-up-django-from-scratch-with-celery-channels-redis-docker-real-time
-django-5828a1ea43a3)

Part 3

[https://medium.com/towardsdev/how-to-set-up-django-from-scratch-with-celery-channels-red
is-docker-real-time-django-8e73c7b6b4c8](https://medium.com/towardsdev/how-to-set-up-django-from-scratch-with-celery-cha
nnels-redis-docker-real-time-django-8e73c7b6b4c8)

Part 4

[https://medium.com/towardsdev/how-to-set-up-django-from-scra
tch-with-celery-channels-redis-docker-real-time-django-c090c300517a](https://medium.com/towardsdev/how-to-set-up-django-
from-scratch-with-celery-channels-redis-docker-real-time-django-c090c300517a)

Part 5  
[https://medium.com/@cubode/how-
to-set-up-django-from-scratch-with-celery-channels-redis-docker-real-time-django-0845eb7e083c](https://medium.com/@cubod
e/how-to-set-up-django-from-scratch-with-celery-channels-redis-docker-real-time-django-0845eb7e083c)
```
---

     
 
deeplearning -  [ Llama 3 not running on GPU ](https://www.reddit.com/r/deeplearning/comments/1dptxsr/llama_3_not_running_on_gpu/) , 2024-07-18-0911
```
I dont know much theory about RAG but i need to implement it for a project.  
**I want to run llama3 on my GPU to get fa
ster results.**

`from langchain_community.llms import Ollama`  
`llm = Ollama(model='llama3',num_gpu=1)`  
`def generat
e_response(prompt, similar_jobs):`  
`descriptions = '\n\n'.join([job['Description'] for job in similar_jobs])`  
`augme
nted_prompt = f'{prompt}\n\nHere are some job recommendations based on your query:\n{descriptions}'`  
`for chunks in ll
m.stream(augmented_prompt):`  
`print(chunks, end='')`

I am giving llama3 my *'user prompt'* and top 5 nearest *'simila
r\_jobs'* using cosine similarity.  
This code goes not use my GPU but my CPU and RAM usage is high.

**My gpu usage is 
0%** , i have a Nvidia GeForce RTX 3050 Laptop GPU GDDR6 @ 4GB (128 bits)
```
---

     
 
deeplearning -  [ What is ReAct Prompting? the most important piece in agentic frameworks ](https://www.reddit.com/gallery/1djk4nk) , 2024-07-18-0911
```
“What is ReAct Prompting? the most important piece in agentic frameworks” - A quick read from Mastering LLM (Large Langu
age Model) 'Coffee Break Concepts' Vol.6

This document deeps dive into the ReAct Prompting method and why it's importan
t:
1. Limitations of LLM
2. Why ReAct prompting matters?
3. How ReAct Works?
4. LangChain Implementation
5. Why Prompt w
ithin agentic frameworks Matters?

Comment below on which topic you want to understand next in this 'Coffee Break Concep
ts' series and we will include those topics in upcoming weeks.
```
---

     
