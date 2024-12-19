 
all -  [ A few of the powerhouses relying on NVIDIA AI. Soon, their AI computations will be immutably anchore ](https://i.redd.it/3x70n4i81p7e1.png) , 2024-12-19-0913
```

```
---

     
 
all -  [ LangChainDeprecationWarning ](https://www.reddit.com/r/LangChain/comments/1hhemqy/langchaindeprecationwarning/) , 2024-12-19-0913
```
I found that when I call SQLChatMessageHistory(), it yields the following warning message: LangChainDeprecationWarning: 
\`connection\_string\` was deprecated in LangChain 0.2.2 and will be removed in 1.0. Use connection instead.  
history =
 get\_session\_history(user\_id)



Since it is a LangChain API, what can I do about it?
```
---

     
 
all -  [ Flexible number of retrievals for RAG ](https://www.reddit.com/r/LangChain/comments/1hhe1so/flexible_number_of_retrievals_for_rag/) , 2024-12-19-0913
```
I am currently learning LangChain and would like to build a RAG with Chroma. In the classic approach, you always get a f
ixed number of retrievals back (Top K).

With this approach, however, other important retrievals might not be considered
 or unimportant ones might be included in the context.

A flexible approach would be much better here. Simply specify a 
maximum number of retrievals, e.g. 5, and a semantic threshold above which they are selected.

If there is a lot of data
, the LLM gets more context; if there is no good data, perhaps only one. This also reduces the risk of hallucinating.

I
s there such an approach with LangChain and Chroma?
```
---

     
 
all -  [ Possible to build collaborative agents in Langchain? ](https://www.reddit.com/r/LangChain/comments/1hhbqfg/possible_to_build_collaborative_agents_in/) , 2024-12-19-0913
```
**Do not post your self promoting website or tool. Not interested**

I have come into a project already deep in Langchai
n so probably not feasible to move to something else. Has anyone built actually useful collaborative agents in Langchain
? I am building a technical forum moderator that can go answer user's technical questions

For that I need
1. RAG to fin
d previously asked similar questions
2. Website crawler tools that can go research the contents of wikis and links menti
oned
3. SQL capable agent that can query internal database for some data

There will be questions where I need to break 
down the task and use all of those capabilities in a certain order. How are people approaching building stuff like this?


Potentially open to Lang graph if you all will say is the right move. I just want something I'm not twisting myself in
 a knot to build and modularize

I have looked into crewAI and what not but they are too high level and don't give the l
evel of control I want with chaining and passing around inputs

```
---

     
 
all -  [ Provable Answers – The Missing Piece to Trusting AI Responses? ](https://www.reddit.com/r/LangChain/comments/1hh89um/provable_answers_the_missing_piece_to_trusting_ai/) , 2024-12-19-0913
```
The number one reason LLM projects fail is the **quality of AI answers**. This is a far bigger issue than performance or
 latency.

Verifying the accuracy of LLM-generated answers, especially when working with private or enterprise data, is 
particularly challenging. It is not like fact-checking public information through a quick Google search. Verifying inter
nal data is harder, slower, and often not something users are motivated to do. If users don’t trust the answers, they’ll
 stop using the agent.

To address this, we built **Proving**—a tool that cryptographically proves the correctness of AI
-generated answers for private database queries.

Here’s how it works:

A user asks a natural language question. The too
l translates the question into SQL, runs the query, and returns the answer in natural language **along with a proof** th
at verifies:

* The SQL query it ran.
* That the query included all relevant data.

Currently, the tool supports Natural
 Language to SQL queries on PostgreSQL, MySQL, and SQLite (yes we use Langchain!)

[Here’s a link to our blog for more d
etails.](https://provably.ai/blog/introducing-proving-a-technique-to-rapidly-verify-and-trust-ai-answers)

We’d love you
r feedback:

1. Would this kind of tool accelerate AI answer verification?
2. Could tools like this help reduce user anx
iety around trusting AI answers?
3. Are you using LLMs to query data? Would you like to explore whether this tool could 
help increase user trust?
```
---

     
 
all -  [ Crewai vs LangChain: Which is better for building agentic apps? ](https://www.reddit.com/r/crewai/comments/1hh438u/crewai_vs_langchain_which_is_better_for_building/) , 2024-12-19-0913
```
I’m trying to choose between Crewai and LangChain for developing agent-based applications.i have 3 questions 
1. Which t
ool offers an easier learning curve?
2. Which one provides better flexibility and ease of use for building complex workf
lows?
3. Are there any notable limitations or strengths of one over the other?
Any insights, especially from those who’v
e worked with both, would be greatly appreciated!


```
---

     
 
all -  [ [For Hire] Skilled Full Stack Developer, AI/ML Expert, and DevOps Pro – Let’s Build Your Next Game-C ](https://www.reddit.com/r/forhire/comments/1hh3dd2/for_hire_skilled_full_stack_developer_aiml_expert/) , 2024-12-19-0913
```
🚀 **Full Stack Developer | AI/ML Engineer | DevOps Specialist – Open for Hire**!

Hi there! I'm Sheryar 👋, a passionate 
developer with the skills and experience to bring your vision to life. Here's what I bring to the table:

# 💻 Full Stack
 Development Expertise

* **Frontend:** React | Angular
* **Backend:** Node.js | NestJS
* **Payments:** Seamless Stripe 
Integrations
* **Cloud Services:** AWS | GCP

# 🤖 AI & Machine Learning Innovations

* Smart Chatbots built with LangCha
in
* Custom NLP models for automation and insights

# ⚙️ DevOps Solutions for Scalable Systems

* **CI/CD Pipelines:** G
itHub Actions | Jenkins
* **Containerization:** Docker | Kubernetes
* **Infrastructure as Code:** Terraform | Ansible

#
 🌟 Notable Projects

* 🚗 **Ride-Sharing App**: Real-time tracking & payment flows
* 📦 **Logistics Platform**: Route opti
mization for multi-stop deliveries
* 🛒 **E-Commerce Infrastructure**: Scalable Kubernetes clusters

# 💰 Rates

* $10–$15
/hour (negotiable based on project scope)

  
Also available for contract-based jobs.

📧 **DM me to discuss your project
 needs**!  
🔗 **GitHub**: [storm1033](https://github.com/storm1033)

Let’s collaborate and turn your ideas into reality!
 🌟
```
---

     
 
all -  [ How to Add PDF Understanding to your AI Agents ](https://www.reddit.com/r/LangChain/comments/1hh25yw/how_to_add_pdf_understanding_to_your_ai_agents/) , 2024-12-19-0913
```
Most of the agents I build for customers need some level of PDF Understanding to work. I spent a lot of time testing out
 different approaches and implementations before landing on one that seems to work well regardless of the file contents 
and infrastructure requirements.

tl;dr:

>What a number of LLM researchers have figured out over the last year is that 
vision models are actually really good at understanding images of documents. And it makes sense that some significant po
rtion of multi-modal LLM training data is images of pages of documents... the internet is full of them.  
So in addition
 to extracting the text, if we can also convert the document's pages to images then we can send BOTH to the LLM and get 
a much better understanding of the document's content.

link to full blog post: [https://www.asterave.com/blog/pdf-under
standing](https://www.asterave.com/blog/pdf-understanding)
```
---

     
 
all -  [ Custom chunk sizes for different categories? ](https://www.reddit.com/r/LangChain/comments/1hgzm8q/custom_chunk_sizes_for_different_categories/) , 2024-12-19-0913
```
Is it a good idea to use a specific chunk size for each category in .json files across different categories?
```
---

     
 
all -  [ We created a playground using Anthropic's computer use and Langchain ](https://www.reddit.com/r/aidevtools/comments/1hgzatq/we_created_a_playground_using_anthropics_computer/) , 2024-12-19-0913
```
Currently, AI's capability cannot perform most real-world tasks. The biggest obstacle is that LLMs are still insufficien
t. However, current LLMs can handle repetitive tasks, jobs within a specific framework, and tasks requiring minimal inte
lligence. We've created a playground environment where you can test this [http://playground.gca.dev](http://playground.g
ca.dev/)
```
---

     
 
all -  [  LangChain - ChatOLLAMA model - calling tool on every input  ](https://www.reddit.com/r/LangChain/comments/1hgy388/langchain_chatollama_model_calling_tool_on_every/) , 2024-12-19-0913
```
* *llama3.2:1b*
* *llama3.2:3b*
* *llama3.2:1b-instruct-fp16*
* *llama3.1:8b*

I've tested above models and all the abov
e models are calling tools even with simple query like 'hi'.

the behavior is same whether binding :

* **tools\_list**

* **openai\_format\_tools\_list**

Need help.

Result:

    python 1_tool_calling_test.py 
    content='' additional_kwa
rgs={} response_metadata={'model': 'llama3.1:8b', 'created_at': '2024-12-18T09:17:37.90843589Z', 'done': True, 'done_rea
son': 'stop', 'total_duration': 72841245771, 'load_duration': 13778033737, 'prompt_eval_count': 194, 'prompt_eval_durati
on': 50723000000, 'eval_count': 22, 'eval_duration': 8337000000, 'message': Message(role='assistant', content='', images
=None, tool_calls=[ToolCall(function=Function(name='tavily_search_results_json', arguments={'query': 'current events'}))
])} id='run-8931e574-9297-4ce9-93f1-54d00ce8c413-0' tool_calls=[{'name': 'tavily_search_results_json', 'args': {'query':
 'current events'}, 'id': '82754a8a-619b-4a1e-85d3-cb767d4c6a9f', 'type': 'tool_call'}] usage_metadata={'input_tokens': 
194, 'output_tokens': 22, 'total_tokens': 216} 
    
    
    [{'name': 'tavily_search_results_json', 'args': {'query': 
'current events'}, 'id': '82754a8a-619b-4a1e-85d3-cb767d4c6a9f', 'type': 'tool_call'}]
    

Code For testing:

    from
 typing import List
    from dotenv import load_dotenv, find_dotenv
    load_dotenv(find_dotenv())
    from langchain_co
re.tools import tool
    from langchain_ollama import ChatOllama
    from langchain_community.tools.tavily_search import
 TavilySearchResults
    from langchain_core.utils.function_calling import convert_to_openai_tool
    
    # @tool
    #
 def web_search_tool(web_query: str) -> str:
    #     '''
    #     Use this tool only when you need to use web search 
in order to find an answer for user.
    #     Args:
    #         web_query (str) : the query for web search
        
 
   #     '''
    #     search = TavilySearchResults()
    #     results = search.invoke(query)
    #     return results

    
    web_search_tool = TavilySearchResults()
    
    tools_list = [web_search_tool]
    openai_format_tools_list = 
[convert_to_openai_tool(f) for f in tools_list]
    
    llm = ChatOllama(model='llama3.1:8b', temperature=0).bind_tools
(tools_list)
    
    result = llm.invoke('Hi, how are you?')
    
    print(result,'\n\n')
    print(result.tool_calls)

    
    
```
---

     
 
all -  [ with_stuctured_output in create_react_agent ](https://www.reddit.com/r/LangChain/comments/1hgxyb5/with_stuctured_output_in_create_react_agent/) , 2024-12-19-0913
```
Hello!

Can somebody help me? I'm currently building a multi agent system usung langchain and langgraph. But I don't fin
d any articles about how to use StucturedOutput in create_react_agent, is there a way that I can do this?
```
---

     
 
all -  [ Why is my semantic search with HuggingFace models not returning correct answers? ](https://www.reddit.com/r/LangChain/comments/1hgwro6/why_is_my_semantic_search_with_huggingface_models/) , 2024-12-19-0913
```
Hi everyone,

I’m working on a semantic search project using HuggingFace models for text embedding and an LLM for answer
ing queries. Here’s the workflow:

User uploads documents (PDFs).
We process the documents, generate embeddings, and sto
re them in a vector database.
Users query the uploaded documents, and we return answers from the LLM.
Everything is func
tioning well except for one issue: sometimes the model doesn’t return the correct answer even though the information exi
sts in the uploaded documents.

I’ve tried:

Verifying the embedding quality.
Checking the vector database query configu
ration.
Ensuring the LLM receives the relevant context.
Despite this, the answers are occasionally off.

Possible reason
s I’ve considered:

Embedding model not capturing enough semantic nuance.
Improper chunking of the documents.
Retrieval 
pipeline not ranking relevant chunks accurately.
I’d love to hear your thoughts on:

Why this might be happening.
How I 
can improve accuracy and ensure the correct information is retrieved.
Any suggestions on improving embeddings, chunking 
strategies, or tweaking the retrieval setup would be greatly appreciated!

Thanks in advance!
```
---

     
 
all -  [ How to Improve the Accuracy of RAG Search? ](https://www.reddit.com/r/LangChain/comments/1hgv25q/how_to_improve_the_accuracy_of_rag_search/) , 2024-12-19-0913
```
I attempted to build a **multi-agent chatbot**, where one of the agents is called the **'knowledge searcher'**. This age
nt determines whether a `function_calling` is needed to retrieve related knowledge based on the user's query. The workin
g principle of the **knowledge searcher** is as follows:

1. When a `function_calling` is required, it retrieves content
 from predefined variables. Otherwise, it returns `None`.
2. It organizes the retrieved content into a summary of 200 wo
rds using an LLM.

The output of the **knowledge searcher** is then used as the input for the **final agent**.

## Why T
his Approach?

1. **Limited Data Volume**  
   The dataset is relatively small.
   
2. **Issues with Traditional RAG Tec
hniques**  
   Traditional RAG often returns irrelevant results or fails to retrieve essential data.  
   For example, w
hen my dataset contains specifications for computers `a`, `b`, and `c`, and the user asks, *'What are the specifications
 of computer a?'*, it often retrieves specifications for all three (`a`, `b`, and `c`). If this combined result is passe
d to the final agent, the prompt becomes overly complex, leading to degraded response quality.

## Question
However, whe
n I use this `function-calling` approach instead of vector search, I encounter some issues:

1. The chatbot response tim
e becomes slower.
2. Sometimes the user's query does not require accessing the knowledge base, yet it still triggers the
 function calling, even though I keep refining the prompt.

Therefore, I believe I ultimately need to return to using th
e RAG (Retrieval-Augmented Generation) method. However, the challenges I face with RAG include 'frequently retrieving ir
relevant data' and 'failing to retrieve relevant data'. I'm unsure if there is something I am not handling well, such as
 document chunking or other processing steps.

Additionally, I’ve also tried using hybrid search (**BM25 + FAISS**), but
 the problem still lies in the document segmentation process. Since the current dataset is small, I can easily review th
e segmented document chunks. However, the same piece of information is often split into different chunks, and the search
 results only consider one part as relevant.

I’ve come across technologies like **Graph RAG**, but considering the cost
 and the fact that the dataset isn’t complex enough yet, I’d like to ask if anyone has suggestions that might be more su
itable for my situation.

---

## Prompts and Function Calls

### **Knowledge Searcher Prompt**
```python
knowledge_sear
cher = '''
# Knowledge Base
The current knowledge base includes:
1. samsung_computer_introduce: ....
2. .... 
...

# Too
ls 
Access the full content of the knowledge base using tools.
The names of the available tools and their related parame
ters are as follows:
{tool_names}

# Search Conditions
- **When a search is needed**:
   - The query involves specific p
roduct specifications, application cases, or integration methods.
   - The user explicitly asks for detailed information
 about a particular product.
   - Keywords in the query are highly relevant to the knowledge base content (e.g., 'comput
er resolution,' 'model selection').

- **When a search is not needed**:
   - The query is about general information (e.g
., product price, support methods) that cannot be mapped to the knowledge base.
   - The query is entirely unrelated to 
the knowledge base.
   - The query is too vague to determine specific needs.
   - The question has already been answered
 in the conversation and does not require further searching.

# Key Constraints
- When a query meets the 'search conditi
ons,' use the tool to retrieve related knowledge base content and summarize it in 200 words. (Do not answer the question
 directly.)
- If a search is not needed, return `None`.
'''
```

## **Final Agent Prompt**
```python
final_agent = '''
R
efer to the search results from the knowledge base to answer the user's question:
User Query: {user_query}
Knowledge Bas
e Content: {knowledge_searcher_response}
...
'''
```

## **function**
```python
@tool
async def get_releted_knowledge(re
lated_knowledge: str):
    '''
    Get the related knowledge description.

    Parameters
    ----------
    related_kno
wledge : str
        The related data we want to retrieve.
        Includes: samsung_computer_introduce...
    '''
    p
rint(f'Try to access the {related_knowledge} knowledge.')
    if related_knowledge == 'others':
        get_releted_know
ledge.return_direct = True
        return None
    get_releted_knowledge.return_direct = False
    return eval(related_k
nowledge)

samsung_computer_introduce = '''
# Summary
Samsung computers provide high-performance computing solutions, co
mbining the latest hardware technology with innovative design to meet various usage needs. Whether for daily office task
s, gaming, or professional creation, Samsung computers offer exceptional performance and user experience.

# Products
Ke
y features of Samsung computers include:
- **High-Performance Processors**: Equipped with the latest generation of proce
ssors, delivering robust computing power for multitasking and high-performance needs.
- **Premium Display Technology**: 
Features high-resolution displays with vibrant colors and sharp visuals, ideal for video playback, image editing, and ga
ming.
- **Portable Design**: Lightweight and portable, perfect for on-the-go office needs.
- **Long-Lasting Battery**: P
rovides extended battery life, reducing the need for frequent recharging.

# Technology
Samsung computers offer the foll
owing technical advantages:
- **Latest Hardware Technology**: Incorporates the latest hardware for superior performance 
and stability.
- **Innovative Design**: Combines stylish and practical design for a comfortable user experience.
- **Ver
satile Applications**: Suitable for office, entertainment, and creative tasks, catering to diverse usage scenarios.
- **
Security Assurance**: Built-in multi-layered security measures ensure data protection and privacy.
'''
```

# Vector Sto
re

```python
def load_files_from_folder(folder_path: str, file_types: list = ['pdf', 'md']):
    documents = []
    for
 filename in os.listdir(folder_path):
        if filename.split('.')[-1].lower() in file_types:
            file_path = 
os.path.join(folder_path, filename)

            if filename.endswith('.pdf'):
                loader = PDFPlumberLoader
(file_path)
            elif filename.endswith('.md'):
                loader = UnstructuredMarkdownLoader(file_path, en
coding='utf-8')
            else:
                continue

            docs = loader.load()

            # Add metadata

            category = filename.split('.')[0].lower()
            for doc in docs:
                doc.metadata['filena
me'] = filename
                doc.metadata['category'] = category

            documents.extend(docs)

    return docu
ments


def split_documents(documents, chunk_size: int = 100, chunk_overlap: int = 20):
    '''
    Parameters
    -----
-----
    chunk_size: int
        The size of content for each split document.
    '''
    text_splitter = RecursiveChar
acterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=len,
    
)
    split_docs = text_splitter.split_documents(documents)
    return split_docs


def create_vectorstore(documents, ve
ctorstore_path: str, api: str = None, rebuild: bool = False) -> FAISS:
    api_key = os.getenv('OPENAI_API_KEY', api)
  
  embeddings = OpenAIEmbeddings(api_key=api_key)
    if rebuild or not os.path.exists(vectorstore_path):
        vectors
tore = FAISS.from_documents(documents, embeddings)
        vectorstore.save_local(vectorstore_path)
        print('Vecto
rstore created and saved successfully.')
    else:
        print('Loading existing vectorstore...')
        vectorstore 
= FAISS.load_local(vectorstore_path, embeddings, allow_dangerous_deserialization=True)
        existing_docs = set(doc.m
etadata['filename'] for doc in vectorstore.docstore._dict.values())

        new_documents = [doc for doc in documents i
f doc.metadata['filename'] not in existing_docs]

        if new_documents:
            # Add new documents to vectorsto
re
            vectorstore.add_documents(new_documents)
            vectorstore.save_local(vectorstore_path)
           
 print('Vectorstore updated successfully.')
        else:
            print('No new documents to update.')

    return v
ectorstore
```

```
---

     
 
all -  [ State In Langchain vs Langgraph ](https://www.reddit.com/r/LangChain/comments/1hguxk8/state_in_langchain_vs_langgraph/) , 2024-12-19-0913
```
I was watching the IBM video on Langchain vs Langgraph, and they made a key point on how state is managed, saying that L
anggraph is more 'robust.' What exactly does that mean? Are there any concrete examples of how this robustness is import
ant? Please point me towards some resources. I did some basic google searching but can't find anything that has a nuance
d answer for what I am asking.

Edit: Just found this - [https://langchain-ai.github.io/langgraph/concepts/low\_level/](
https://langchain-ai.github.io/langgraph/concepts/low_level/)
```
---

     
 
all -  [ need advice ](https://i.redd.it/zhxkhwq18i7e1.jpeg) , 2024-12-19-0913
```
please tell me how to improve my cv and suggest better project ideas as well.
I really want to land an internship 
```
---

     
 
all -  [ [Project] Video Foundation Model as an API ](https://www.reddit.com/r/LangChain/comments/1hgm2df/project_video_foundation_model_as_an_api/) , 2024-12-19-0913
```
Hey everybody! My team and I have been working on a foundational video language model (viFM) as-a-service we're excited 
to do our first release!

tl;dw is an API for video foundational models (viFMs) and provides video understanding. It hel
ps developers build apps powered by an AI that can watch and understand videos just like a human. 

  
Only search is av
ailable right now but these are all the features that will be releasing over the next few weeks:

* Semantic video searc
h: Use plain English to find specific moments in single or multiple videos
* Classification: Identify context-based acti
ons or behaviors
* Labeling: Add metadata or label every event
* Scene splitting: Automatically split videos into scenes
 based on what you’re looking for
* Video-to-text: Get text description of what is happening in the clip or video

  
Wh
at can you build with tl;dw?

* an AI agent that can recommend videos based on your preferences
* the internal media dis
covery platform [Netflix](https://netflixtechblog.com/building-a-media-understanding-platform-for-ml-innovations-9bef996
2dcb7) has
* smart home security camera like the demo we have [here](https://trytldw.ai/security_demo)
* find usable sho
ts if you’re producing a video
* automatically add metadata to videos or scenes

Any feedback is appreciated! Is there s
omething you’d like to see? Do you think this API is useful? How would you use it, etc. Happy to answer any questions as
 well.

[Register and get an API key](https://trytldw.ai/register): [https://trytldw.ai/register:](https://trytldw.ai/re
gister:)

[Follow the quick start guide to understand the basics.](https://docs.trytldw.ai/intro)

[Documentation can be
 viewed here](https://docs.trytldw.ai/)

Demos + tutorials coming soon.

Happy to answer any questions!
```
---

     
 
all -  [ Need help with recovering conversations from checkpoint store ](https://www.reddit.com/r/LangChain/comments/1hgkbt5/need_help_with_recovering_conversations_from/) , 2024-12-19-0913
```
So I tried out the MongoDB checkpointer implementation from [here](https://langchain-ai.github.io/langgraph/how-tos/pers
istence_mongodb/), and while it does work great out of the box for storing graph state, I am running into some problems 
when trying to use it as a conversation store. Apparently, every time the state of the graph changes, a new checkpoint i
s written to the database  which contains all the messages in all the previous checkpoints, which I assume is implemente
d this way in order to enable time travelling. My question is first of all, is there a way to disable this or tune it in
 a way such that I store one document per conversation (thread\_id) in my db, which keeps updating instead of writing a 
new checkpoint every time. ( I assuming there is no way to do this currently, just want to know why  ) Secondly, is usin
g persistent DB checkpointers event a good way to store conversations? Or do people generally implement their own stores
? Let us say I wish to store multiple conversations and want to pull a single a conversation by given thread\_id. Someth
ing like storing the `created_at` attribute in the metadata, then sorting in descending order and picking the first chec
kpoint would work, but at this point I feel like I'm unnecessarily complicating stuff and should just go for a self made
 conversation store, especially as my requirements will become more complex. 
```
---

     
 
all -  [ Does LangChain support Open AI Batch API? ](https://www.reddit.com/r/LangChain/comments/1hghach/does_langchain_support_open_ai_batch_api/) , 2024-12-19-0913
```
Hi,

  
I would like to utilize Open AI Batch API as it helps reduce the cost by 50%. I have been using Open AI through 
LangChain and I have been trying to find some information on how to incorporate the Open AI's Batch API but I found no h
elpful information on it. Does LangChain even support Batch API?
```
---

     
 
all -  [ Random Human messages and response ](https://www.reddit.com/r/LangChain/comments/1hgamfk/random_human_messages_and_response/) , 2024-12-19-0913
```
While printing result. Some random sentence gets print. Then needed response is printed and than again a random conversi
on gets print.Why is it happening.

Version of packages:  
langchain-core:0.3.25  
langchain-huggingface: 0.1.2

https:/
/preview.redd.it/sgm8d0b4ue7e1.png?width=1680&format=png&auto=webp&s=d871ee6e0357afbd78fa3bddea3221038743f246


```
---

     
 
all -  [ Persisting Chat History in LangChain JS ](https://www.reddit.com/r/LangChain/comments/1hgahty/persisting_chat_history_in_langchain_js/) , 2024-12-19-0913
```
I've read the docs for LangChain (JS) on how to use LangGraph and checkpointSaver etc to persist chat history. It all se
ems super complicated and unnecessary to me.

If I persist my own messages and use trim messages doesn't it accomplish t
he g\`oal of chat history?

`const llm = new ChatOpenAI({ model: 'gpt-4o' });`

`// GET THESE MESSAGES FROM DATABASE`  

`const messages = [`  
`new SystemMessage('you're a good assistant, you always respond with a joke.'),`  
`new HumanMess
age('i wonder why it's called langchain'),`  
`new AIMessage(`  
`'Well, I guess they thought 'WordRope' and 'SentenceSt
ring' just didn\'t have the same ring to it!'`  
`),`  
`new HumanMessage('and who is harrison chasing anyways'),`  
`ne
w AIMessage(`  
`'Hmmm let me think.\n\nWhy, he's probably chasing after the last cup of coffee in the office!'`  
`),` 
 
`new HumanMessage('what do you call a speechless parrot'),`  
`];`

`// TRIM MESSAGES`  
`const trimmed = await trimMe
ssages(messages, {`  
`maxTokens: 45,`  
`strategy: 'last',`  
`tokenCounter: llm,`  
`});`

`const chain = trimmed.pipe
(llm);`  
`// INVOKE LLM WITH CHAT HISTORY. MUCH EASIER!`  
`await chain.invoke(messages);`
```
---

     
 
all -  [ Forcing LLM function call not yet available using langchain4j ](https://www.reddit.com/r/LangChain/comments/1hg5lqh/forcing_llm_function_call_not_yet_available_using/) , 2024-12-19-0913
```
Hi all. Am I right that forcing of LLM function call using langchain4j library (Java) is not yet supported? Seems so but
 just want to confirm.
```
---

     
 
all -  [ LangGraph with React Agent & Azure GPT-4o: Parallel Tool Call Delay Issue in Traces ](https://www.reddit.com/r/LangChain/comments/1hfzr38/langgraph_with_react_agent_azure_gpt4o_parallel/) , 2024-12-19-0913
```
Hi everyone,

I am using a React agent with LangGraph to orchestrate function calls to Azure OpenAI GPT-4o. My workflow 
involves the following:

1. Extract 30 questions from one tool.
2. Use a RAG tool to retrieve answers.

Since `parallel 
tool call = true`, the RAG tool hits all the questions in parallel. However, when I check the traces, I observe an unexp
ected pattern:

* It processes the first 10-12 calls, then pauses briefly.
* After the gap, it processes the next 10-12 
calls.

I don’t see any set limits on the function or parameters for the number of parallel calls. I’ve attached an imag
e of the trace for clarity. Does anyone have an idea why this might be happening? Could it be an internal limitation or 
bottleneck somewhere?

  
Here’s the trace image for reference:  


https://preview.redd.it/95y456cvdb7e1.png?width=1863
&format=png&auto=webp&s=6e9cc7a6b03ea64a1cc0c0057074a61e7ec7a36c

Any help or insights would be greatly appreciated.


```
---

     
 
all -  [ Build a Production Level RAG System with LangGraph ](https://www.reddit.com/r/LangChain/comments/1hfyzbx/build_a_production_level_rag_system_with_langgraph/) , 2024-12-19-0913
```
\[Update\] - Full Access links are provided!



Hello,

I recently open sourced a RAG application I built with LangGraph
 for a production application and I published the detail + the code in three articles on medium.com.

Part 1: [https://m
edium.com/@h1rouhani/build-production-ready-ai-assistant-backend-service-in-python-part-1-9c7b2910eea3?sk=f74a571c26fcde
6f711e007235be4a25](https://medium.com/@h1rouhani/build-production-ready-ai-assistant-backend-service-in-python-part-1-9
c7b2910eea3?sk=f74a571c26fcde6f711e007235be4a25)

Part 2: [https://medium.com/@h1rouhani/build-production-ready-ai-assis
tant-backend-service-in-python-part-2-a8d31f0c2dc3?sk=0d7d81ff16e1e7a3222f834317649f96](https://medium.com/@h1rouhani/bu
ild-production-ready-ai-assistant-backend-service-in-python-part-2-a8d31f0c2dc3?sk=0d7d81ff16e1e7a3222f834317649f96)

Pa
rt 3: [https://medium.com/@h1rouhani/build-production-ready-ai-assistant-backend-service-in-python-part-3-093ba216918e?s
k=793f875df27b37b956379720a6774112](https://medium.com/@h1rouhani/build-production-ready-ai-assistant-backend-service-in
-python-part-3-093ba216918e?sk=793f875df27b37b956379720a6774112)
```
---

     
 
all -  [ Llama 3.1 8B struggles with tool calls ](https://www.reddit.com/r/LocalLLaMA/comments/1hfxepg/llama_31_8b_struggles_with_tool_calls/) , 2024-12-19-0913
```
Hello,

I'm using the Llama 3.1 8B model within a standard ReAct architecture. Despite having a very specific system pro
mpt, the model consistently tries to call tools even when it's unnecessary.

I've checked my code, and everything seems 
fine. Interestingly, I tried the same setup with Mistral NeMo, and the experience was significantly better—no excessive 
tool calls.

I'm running this with LangChain and Ollama. Is this a known issue, or am I missing something? Has anyone el
se experienced this behavior?

Thanks in advance!
```
---

     
 
all -  [ Llama 3.1 8B model struggles when calling tools ](https://www.reddit.com/r/LangChain/comments/1hfxay2/llama_31_8b_model_struggles_when_calling_tools/) , 2024-12-19-0913
```
Hello,

I'm using the Llama 3.1 8B model within a standard ReAct architecture. Despite having a very specific system pro
mpt, the model consistently tries to call tools even when it's unnecessary.

I've checked my code, and everything seems 
fine. Interestingly, I tried the same setup with Mistral NeMo, and the experience was significantly better, no excessive
 tool calls.

I'm running this with LangChain and Ollama. Is this a known issue, or am I missing something? Has anyone e
lse experienced this behavior?

Thanks in advance!
```
---

     
 
all -  [ LLM reliability: getting users to trust your AI agent  ](https://www.anti-vc.com/p/getting-users-to-trust-your-ai-agent?utm_campaign=post&showWelcomeOnShare=false) , 2024-12-19-0913
```
Does anyone have lessons they’d like to share? I collected how startups use LangGraph and LangSmith to deploy Agentic RA
G. 
```
---

     
 
all -  [ Build (Fast)Agents with FastAPIs ](https://i.redd.it/6hgi2hy5897e1.jpeg) , 2024-12-19-0913
```
Okay so our definition of agent == prompt + LLM + APIs/tools. 

And https://github.com/katanemo/archgw is a new, framewo
rk agnostic, intelligent infrastructure project to build fast, observable agents using APIs as tools. It also has the #1
 trending function calling LLM on hugging face. https://x.com/salman_paracha/status/1865639711286690009?s=46

Disclaimer
: I help with devrel. Ask me anything. 
```
---

     
 
all -  [ tags option of XMLOutputParser? ](https://www.reddit.com/r/LangChain/comments/1hfoipj/tags_option_of_xmloutputparser/) , 2024-12-19-0913
```
Hey folks, the tags option of XMLOutputParser is not documented, what is it supposed to do ? I was expecting it to limit
 the available tags however it doesn't seem to have any effect.

[https://python.langchain.com/api\_reference/core/outpu
t\_parsers/langchain\_core.output\_parsers.xml.XMLOutputParser.html#langchain\_core.output\_parsers.xml.XMLOutputParser.
tags](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.xml.XMLOutputParser.h
tml#langchain_core.output_parsers.xml.XMLOutputParser.tags)  

```
---

     
 
all -  [ Querying Tables ](https://www.reddit.com/r/LangChain/comments/1hflxz6/querying_tables/) , 2024-12-19-0913
```
Hi,

Could you please guide me to some resources that can help me better understand the most suitable way to query table
s (specifically in my case)? I have read that RAG is not well-suited for tables and that it is better to use an SQL agen
t to create and execute queries.

For example, I have a table with a description column where each string is unique. If 
a user's query involves filtering this column (lets's say this get decided in previous nodes), it becomes challenging to
 handle using standard SQL. I have tried using the LIKE operator, but in the prompt I have to list all possible descript
ions in that column. While this method works, it is not scalable for other tables.

Do you have any suggestions? I was t
hinking whether there was a way of tagging such columns when creating the table in the database and if the search evolve
s around that column, use a specific NLP search (I may be completely off here) ?

Thank you in advance.
```
---

     
 
all -  [ Roast my beginner RAG project ](https://www.reddit.com/r/LangChain/comments/1hfliok/roast_my_beginner_rag_project/) , 2024-12-19-0913
```
I made a rag chatbot that uses docling for parsing files, semantic double pass merging (best) for chunking, qdrant for v
ector DB, gemini flash for chat. This includes hybrid search and Colbert for reranking. I made both local and cloud setu
p files. I think this is beginner friendly code who understands rag theoretically. Also added gradio chatbot( thanks to 
sonnet). You can find guide.md where I tried to explain about the project.

Everything is built with free API's

https:/
/github.com/Lokesh-Chimakurthi/Reliable_RAG
```
---

     
 
all -  [ Roast my beginner RAG project ](https://www.reddit.com/r/LLMDevs/comments/1hflhty/roast_my_beginner_rag_project/) , 2024-12-19-0913
```
I made a rag chatbot that uses docling for parsing files, semantic double pass merging (best) for chunking, qdrant for v
ector DB, gemini flash for chat. This includes hybrid search and Colbert for reranking. I made both local and cloud setu
p files. I think this is beginner friendly code who understands rag theoretically. No langchain, llamaindex just for chu
nking. Also added gradio chatbot( thanks to sonnet). You can find guide.md where I tried to explain about the project.


Everything is built with free API's

https://github.com/Lokesh-Chimakurthi/Reliable_RAG
```
---

     
 
all -  [ Anthropic'in çıkardığı Computer use ile ilgili bir teknoloji yaptık. ](https://www.reddit.com/r/CodingTR/comments/1hfkw8p/anthropicin_çıkardığı_computer_use_ile_ilgili_bir/) , 2024-12-19-0913
```
Merhaba arkadaşlar,

  
Son zamanlarda Anthropic bazı AI teknolojileri tanıttı. Computer Use ve MCP. Bu teknolojiler LLM
'lerin bilgisayarı daha kolay kullanmasını amaçlıyor. Computer use ve Model context protocol(MCP) LLM'lerin bilgisayarla
 etkileşime girmesini kolaylaştırıyor. Normalde klavye, mouse ile yaptığımız insan etkileşimini taklit ediyorlar. Comput
er use OCR'den çok daha kaliteli. MCP ise bir protokol.



Biz de açık kaynak bir computer use framework yazıyoruz. AI'ı
n bilgisayarı kullanarak task'leri bitirmesini sağlıyoruz. Hatta bu frameworkün kolayca denenebilmesi için bir playgroun
d ortamı yaptık isterseniz göz atabilirsiniz [playground.gca.dev](http://playground.gca.dev) 

Computer use teknolojisi 
şu anda çok yavaş. Örneğin Google'den araştırma yapmak için önce fareyi hareket ettiriyor, sonra iki kere tıklıyor sonra
 araştıracağı başlığı yazıyor, sonra siteye girmek için tekrar tıklıyor vs. Biz bu kısımlarda Langchain kullanıyoruz Lan
gchain tooları bu işi daha kolay daha az maliyetli ve daha hızlı yapıyorlar.

Computer use teknolojisinin iyi yanı ekran
da bir yere tıklatmak istediğinizde bunu çok yüksek bir başarı ile yapıyor. Ayrıca her adımı sırasıyla başarı ile tekrar
lıyor. Bu kısmı Langchain tooları ile yapamıyoruz. Onun için Anthropic'in computer use teknolojisini kullanıyoruz. 

  

Playground ortamında denemeler yapıp hata aldığınız şeyleri yazabilirseniz çok sevinirim. Hata alınan kısımlar için work
flowlar yazarak çözmeye çalışıyoruz. Tavsiyeleriniz bizim için çok değerli. 


```
---

     
 
all -  [ Understanding Prompt Engineering ](https://open.substack.com/pub/diamantai/p/understanding-prompt-engineering?utm_source=share&utm_medium=android&r=336pe4) , 2024-12-19-0913
```
Ever wondered why some prompts deliver great results while others fall flat? I put together this blog to break down what
’s happening behind the scenes and offer a practical way to understand how prompts guide language models.

🔍 What’s Insi
de:
1) How Language Models Work: A straightforward look at pretraining and fine-tuning, and how these phases shape what 
models can do.

2) Why Reasoning Works: Insights into how models use patterns and attention mechanisms to mimic logical 
reasoning, even when they’re trained to just predict the next word.

3) Techniques to Improve Prompts: Role prompting, s
tep-by-step reasoning, and temperature adjustments—practical tips you can start using right away.

4) Templates for Bett
er Results: Simple, reusable formats to guide models for tasks like coding, explaining concepts, or solving problems.
```
---

     
 
all -  [ Alternative to LangChain? ](https://www.reddit.com/r/LLMDevs/comments/1hfjfo6/alternative_to_langchain/) , 2024-12-19-0913
```
Hi, I am trying to compile an LLM application, I want to use features as in Langchain but Langchain documentation is ext
remely poor. I am looking to find alternatives, to langchain.

  
What else orchestration frameworks are being used in i
ndustry?
```
---

     
 
all -  [ The Top 14 Software Languages, Frameworks & Libraries Job Trends in 2024 ](https://www.reddit.com/r/cscareerquestions/comments/1hfi16b/the_top_14_software_languages_frameworks/) , 2024-12-19-0913
```
[https://mail.job.zip/p/the-job-zip-awards-2024-top-trends-in-ai-databases-software#the-top-14-software-languages-frame]
(https://mail.job.zip/p/the-job-zip-awards-2024-top-trends-in-ai-databases-software#the-top-14-software-languages-frame)


# 14.[ ](https://job.zip/trend/langchain?utm_source=mail.job.zip&utm_medium=referral&utm_campaign=the-job-zip-awards-2
024-top-trends-in-ai-databases-software)[Tailwind CSS](https://job.zip/trend/tailwind-css?utm_source=mail.job.zip&utm_me
dium=referral&utm_campaign=the-job-zip-awards-2024-top-trends-in-ai-databases-software)

📈 +25% Growth  
**800-1.6k empl
oyers**

A utility-first CSS framework that provides low-level utility classes to build custom designs without writing C
SS from scratch.

# 13.[ ](https://job.zip/trend/langchain?utm_source=mail.job.zip&utm_medium=referral&utm_campaign=the-
job-zip-awards-2024-top-trends-in-ai-databases-software)[FastAPI](https://job.zip/trend/fastapi?utm_source=mail.job.zip&
utm_medium=referral&utm_campaign=the-job-zip-awards-2024-top-trends-in-ai-databases-software)

📈 +25% Growth  
**1k-2k e
mployers**

FastAPI is a modern, high-performance web framework for building APIs with Python. It is designed to be easy
 to use and fast, leveraging Python's type hints to provide automatic validation and documentation of API endpoints.

# 
12.[ LangChain](https://job.zip/trend/langchain?utm_source=mail.job.zip&utm_medium=referral&utm_campaign=the-job-zip-awa
rds-2024-top-trends-in-ai-databases-software)

📈 +25% Growth  
**700-1.4k employers**

A framework for developing applic
ations powered by language models, enabling the integration of natural language processing capabilities into software.


# 11. [tRPC](https://job.zip/trend/trpc?utm_source=mail.job.zip&utm_medium=referral&utm_campaign=the-job-zip-awards-2024
-top-trends-in-ai-databases-software)

📈 +27% Growth  
**40-80 employers**

A TypeScript library for building end-to-end
 typesafe APIs, allowing seamless communication between client and server.

# 10. [AutoGen](https://job.zip/trend/autoge
n?utm_source=mail.job.zip&utm_medium=referral&utm_campaign=the-job-zip-awards-2024-top-trends-in-ai-databases-software)


📈 +39% Growth  
**70-140 employers**

AutoGen is a framework designed to facilitate the creation of complex AI applicat
ions by enabling multiple large language models (LLMs) to collaborate as agents.

# 9. [asyncio](https://job.zip/trend/a
syncio?utm_source=mail.job.zip&utm_medium=referral&utm_campaign=the-job-zip-awards-2024-top-trends-in-ai-databases-softw
are)

📈 +50% Growth  
**90-180 employers**

A library in Python to write concurrent code using the async/await syntax. A
llows for efficient management of I/O-bound operations.

# 8. [Htmx](https://job.zip/trend/htmx?utm_source=mail.job.zip&
utm_medium=referral&utm_campaign=the-job-zip-awards-2024-top-trends-in-ai-databases-software)

📈 +78% Growth  
**25-50 e
mployers**

A library that allows developers to access modern browser features directly from HTML, enabling dynamic web 
applications without JavaScript.

# 7. [Zustand](https://job.zip/trend/zustand-javascript?utm_source=mail.job.zip&utm_me
dium=referral&utm_campaign=the-job-zip-awards-2024-top-trends-in-ai-databases-software)

📈 +83% Growth  
**100-200 emplo
yers**

A small, fast, and scalable state management library for React applications, known for its simplicity and flexib
ility.

# 6. [Tauri](https://job.zip/trend/tauri-software?utm_source=mail.job.zip&utm_medium=referral&utm_campaign=the-j
ob-zip-awards-2024-top-trends-in-ai-databases-software)

📈 +111% Growth  
**12-24 employers**

A framework for building 
tiny, fast, and secure desktop applications with Rust and web technologies.

# 5. [TanStack](https://job.zip/trend/tanst
ack?utm_source=mail.job.zip&utm_medium=referral&utm_campaign=the-job-zip-awards-2024-top-trends-in-ai-databases-software
)

📈 +137% Growth  
**60-120 employers**

A collection of open-source libraries for building modern web applications, in
cluding tools for state management and data fetching.

# 4. [Shadcn](https://job.zip/trend/shadcn?utm_source=mail.job.zi
p&utm_medium=referral&utm_campaign=the-job-zip-awards-2024-top-trends-in-ai-databases-software)

📈 +200% Growth  
**40-8
0 employers**

Shadcn is a collection of reusable components and utilities for building web applications using React. It
 provides a set of pre-designed, customizable components that adhere to modern design principles, making it easier for d
evelopers to create consistent and visually appealing user interfaces.

# 3. [Ollama](https://job.zip/trend/ollama?utm_s
ource=mail.job.zip&utm_medium=referral&utm_campaign=the-job-zip-awards-2024-top-trends-in-ai-databases-software)

📈 +287
% Growth  
**30-60 employers**

Ollama is an open-source framework designed for serving large language models (LLMs) loc
ally on on-premise devices.

# 2. [DSPy](https://job.zip/trend/dspy?utm_source=mail.job.zip&utm_medium=referral&utm_camp
aign=the-job-zip-awards-2024-top-trends-in-ai-databases-software)

📈 +500% Growth  
**15-30 employers**

DSPy is an open
-source framework developed by Stanford NLP for programming language models, focusing on building modular AI systems rat
her than relying on traditional prompting.

# 1. [CrewAI](https://job.zip/trend/crewai?utm_source=mail.job.zip&utm_mediu
m=referral&utm_campaign=the-job-zip-awards-2024-top-trends-in-ai-databases-software)

📈 +1240% Growth  
**30-60 employer
s**
```
---

     
 
all -  [ Deploy RAG Chatbot on MS Teams ](https://www.reddit.com/r/LangChain/comments/1hfghrj/deploy_rag_chatbot_on_ms_teams/) , 2024-12-19-0913
```
Hey,

I’ve developed a RAG-based chatbot currently in the form of an IPYNB file and would like to deploy it on Microsoft
 Teams. However, I’m unsure how to proceed and would greatly appreciate any guidance or resources to help me achieve thi
s.


```
---

     
 
all -  [ How to Create and Integrate a Separate LangChain Package? Need Guidance! ](https://www.reddit.com/r/LangChain/comments/1hfevq4/how_to_create_and_integrate_a_separate_langchain/) , 2024-12-19-0913
```
Hi everyone!

I’m working on improving a `YoutubeLoader` integration for LangChain, and during the review process, it wa
s suggested that I create a separate package for it instead of contributing directly to the LangChain monorepo. I’ve rea
d the contributing guide and had a discussion on GitHub, but I’m still unclear about a few things.

Here’s what I unders
tand so far:

1. The integration package should be managed in **my own repository**, not as part of a fork of `langchain
-ai/langchain`.
2. Once ready, I need to publish the package to **PyPI** so others can install it.
3. I’ll need to updat
e LangChain’s docs and mark the old community integration as deprecated, linking users to my new package.

But I still h
ave a few questions:

* Do I need to first fork `langchain-ai/langchain` and integrate the package there, or is the work
flow entirely separate (as in, just create and maintain my own repository)?
* How exactly do I update LangChain's docs? 
Is it just about deprecating the old code and pointing to my package?

If anyone has experience contributing integration
s to LangChain or has gone through this process before, I’d love to hear your advice or tips!
```
---

     
 
all -  [ How can I use langgraph studio on windows [like a poor with out mac] ](https://www.reddit.com/r/LangChain/comments/1hfcu3s/how_can_i_use_langgraph_studio_on_windows_like_a/) , 2024-12-19-0913
```
I have agents built using langgraph. And I saw that l langgraph studio is only supported on Mac os. But they have the lo
cal host what ever method for the poors.

Help me to connect langgraph that run locally on the top of langsmith to my ag
ents please and thanks 
```
---

     
 
all -  [ Is there a way or plugin to connect to the ChatGPT browser interface? ](https://www.reddit.com/r/LangChain/comments/1hfcrq5/is_there_a_way_or_plugin_to_connect_to_the/) , 2024-12-19-0913
```
Hello everyone,  
I’ve recently started using LangChain, and I think it’s fantastic! However, for a small test I’m worki
ng on, I’d like to find a way to connect directly to my ChatGPT Pro account in the browser.

To clarify, I’m not looking
 to use the OpenAI API, but instead, I want to interact with the ChatGPT browser chat interface. Is this something that 
can be done?

Thanks in advance for any insights or suggestions!
```
---

     
 
all -  [ Seeking Architectures for Building Agents ](https://www.reddit.com/r/LangChain/comments/1hfb4o8/seeking_architectures_for_building_agents/) , 2024-12-19-0913
```
Hello everyone,

I am looking for papers that explore agent architectures for diverse objectives, as well as technical p
apers on real-world LLM-based agent solutions. For reference, I'm interested in works similar to the cited papers in the
 Langgraph tutorials:

[https://langchain-ai.github.io/langgraph/tutorials/](https://langchain-ai.github.io/langgraph/tu
torials/)

Thank you!


```
---

     
 
all -  [ Youtube Video content fact checker app ](https://www.reddit.com/r/LangChain/comments/1hfaqsj/youtube_video_content_fact_checker_app/) , 2024-12-19-0913
```
Hey falks, I am given a task to make an app that gets an input (query) from user and returns list of youtube videos (5 o
r 10). The returned list of videos are ordered accoridng to their similarity of title and the content of the video. Vide
os with the highest similarity should be in the top. I am new in langchain and have some idea how to tackle it:   
1. I 
extract the content and the title of the returned list of videos.  
2. Then do similarity search (like cosine-similarity
) between the title and the corresponding content.  
3. Return the list with the highest rate of similarity in the top. 


This is what I am planning to do.  
If there are anybody with such project experience or those who are expert, please,
 share your ideas to tackle this project.  

```
---

     
 
MachineLearning -  [ [P] Minima: local conversational retrieval augmented generation project (Ollama, Langchain, FastAPI, ](https://www.reddit.com/r/MachineLearning/comments/1h1pudq/p_minima_local_conversational_retrieval_augmented/) , 2024-12-19-0913
```
  
[https://github.com/dmayboroda/minima](https://github.com/dmayboroda/minima)  
  
Hey everyone, I would like to intro
duce you my latest repo, that is a local conversational rag on your files, Be honest, you can use this as a rag on-premi
ses, cause it is build with docker, langchain, ollama, fastapi, hf All models download automatically, soon I'll add an a
bility to choose a model For now solution contains:

* Locally running Ollama (currently qwen-0.5b model hardcoded, soon
 you'll be able to choose a model from ollama registry)
* Local indexing (using sentence-transformer embedding model, yo
u can switch to other model, but only sentence-transformers applied, also will be changed soon)
* Qdrant container runni
ng on your machine
* Reranker running locally (BAAI/bge-reranker-base currently hardcoded, but i will also add an abilit
y to choose a reranker)
* Websocket based chat with saving history
* Simple chat UI written with React
* As a plus, you 
can use local rag with ChatGPT as a custom GPT, so you able to query your local data through official chatgpt web and ma
c os/ios app.
* You can deploy it as a RAG on-premises, all containers can work on CPU machines

Couple of ideas/problem
s:

* Model Context Protocol support
* Right now there is no incremental indexing or reindexing
* No selection for the m
odels (will be added soon)
* Different environment support (cuda, mps, custom npu's)

Welcome to contribute (watch, fork
, star) Thank you so much!
```
---

     
