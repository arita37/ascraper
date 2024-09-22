 
all -  [ NL to SQL on a large DBs ](https://www.reddit.com/r/LangChain/comments/1fmed0k/nl_to_sql_on_a_large_dbs/) , 2024-09-22-0914
```
Hey everyone!

I’m fairly new to the world of open-source LLMs and I’m working on building an AI assistant that generate
s SQL queries based on user questions. I use LLaMA as my base model. It works well with smaller database schemas (2-3 ta
bles with simple relationships), but I’ve run into challenges when scaling up to larger databases (100+ tables and a sch
ema exceeding 20k tokens). The schema doesn’t fit into the model’s context size.

I’ve tried summarizing the key informa
tion about the tables and relationships into JSON and used LlamaIndex's `JsonQueryEngine`, but the results haven’t been 
great. It also makes sense that as the number of tables grows, the generated queries become more confusing and harder to
 manage.

Can LangChain help me with this issue?   
  
Could anyone point me in the right direction for handling this? I
f restructuring the database and creating view tables is the last what I want to do
```
---

     
 
all -  [ A simple guide on building RAG with Excel files ](https://www.reddit.com/r/LangChain/comments/1fmarsp/a_simple_guide_on_building_rag_with_excel_files/) , 2024-09-22-0914
```
A lot of people reach out to me asking how I'm building RAGs with excel files. It is a very common use case and the good
 news is that it can be very simple while also being extremely accurate and fast, much more so than with vector embeddin
gs or bm25.

So I decided to write a blog about how I am building and using SQL agents to create RAGs with excels. You c
an check it out here: [https://ajac-zero.com/posts/how-to-create-accurate-fast-rag-with-excel-files/](https://ajac-zero.
com/posts/how-to-create-accurate-fast-rag-with-excel-files/) .

The post is accompanied by a github repo where you can c
heck all the code used for this example RAG. If you find it useful you can give it a star!

Feel free to reach out in my
 social links if you'd like to chat about rag / agents, I'm always interested in hearing about the projects people are w
orking on :)
```
---

     
 
all -  [ Video narrator creating video narration out of uploaded videos. Upload video, take it frame by frame ](https://v.redd.it/3605lxazb7qd1) , 2024-09-22-0914
```

```
---

     
 
all -  [ What are good ways to get my vector search to return more recent results? ](https://www.reddit.com/r/LangChain/comments/1fm5tgc/what_are_good_ways_to_get_my_vector_search_to/) , 2024-09-22-0914
```
I'm experimenting with RAG stack. I'm hand rolling things but this seems like a smart community which is why I'm asking 
here. I'm using weaviate as my vector database.

I want to pull back relevant pieces of data using a vector search to fe
ed to the LLM. All the records I have vectorized have dates associated with them. I'm wondering if there are any good kn
own strategies for getting the vector search to prioritize more recent records? This includes querying strategies.

Than
ks.
```
---

     
 
all -  [ Not nable to get simple JSON formatted structured output from Llama 3.1 model and langchain Pydantic ](https://www.reddit.com/r/LangChain/comments/1fm3uor/not_nable_to_get_simple_json_formatted_structured/) , 2024-09-22-0914
```
Hey,

  
I am not sure why, if it is the model or due to the modules in langchain, but I dont get proper output and ever
y run I get different strange messages when using the PydanticOutputParser.

  
I try to reproduce this example (very ni
ce example!). I always get strange messages regarding the output. I am not able to get a list of activities like shown t
here:

[https://github.com/NachoCP/AIScraping/blob/main/article/article.md](https://github.com/NachoCP/AIScraping/blob/m
ain/article/article.md)

  
Does anyone experience similar things using PydanticOutputParser together with a Llama model
?
```
---

     
 
all -  [ Langchain/Langgraph Agents with o1-mini and o1-preview ](https://www.reddit.com/r/LangChain/comments/1fm36v0/langchainlanggraph_agents_with_o1mini_and/) , 2024-09-22-0914
```
I understand the current preview doesn't support system messages or function calling but it is possible to workaround an
d make a custom agent (like the early days of React Agents that parsed AI output for tool\_calls). Has anyone made a wor
king prototype of this that can be shared? It seems like all the latest pre-built agents only work with native tool\_cal
ling.

I tested out the API with tool\_calls and tool\_messages and the o1-mini and o1-preview do work fine with this fo
rmat. I just need the loop that manages the chat history like below but handles the tool calls etc manually by parsing t
he model response for json tool\_calls. Would be great if something is already out there so I don't have to reinvent it.


\`\`\`

    from langchain_openai import ChatOpenAI
    from langchain_core.messages import HumanMessage
    from lang
chain_core.messages import AIMessage, ToolMessage, ToolCall
    
    model = ChatOpenAI(model='o1-mini', temperature=1)

    
    
    response = model.invoke(
        [
            HumanMessage(content='Hi! I'm John'),
            AIMessage
(content='Hello John! How can I assist you today?'),
            HumanMessage(content='What is my last name?'),
        
    AIMessage(
                tool_calls=[
                    {
                        'name': 'searching_db',
      
                  'args': {'search': 'John's last name'},
                        'id': '123',
                    }
   
             ],
                content='',
            ),
            ToolMessage(content='Doe', tool_call_id='123'),
 
           AIMessage(content='Your last name is Doe.'),
            HumanMessage(content='When is my birthday?'),
      
      AIMessage(
                tool_calls=[
                    {
                        'name': 'searching_db',
    
                    'args': {'search': 'Hasan's birthday'},
                        'id': '123',
                    }
 
               ],
                content='',
            ),
            ToolMessage(content='October 22nd, 1987', tool_
call_id='123'),
        ]
    )
    
    print(response.content)
    
    
    ```
```
---

     
 
all -  [ Chain of thought question (not only for Local models) ](https://www.reddit.com/r/LocalLLM/comments/1fm0mi1/chain_of_thought_question_not_only_for_local/) , 2024-09-22-0914
```
Dear all,

I have been thinking about the Chain-Of-Thought approach.

My understanding si that you decompose a question 
in many steps and you walk through it to avoid misinterpretations. As the example below. But how is this practically imp
lemented?

Let's say I am using either Haystack or Langchain and I query my model, should I add 'let's solve this step b
y step'? but if you use the app of Chatgpt or Gemini, you do not write this, it is already in the application. What am I
 missing that they do in their application:



Input: 'If there are 3 apples and you take away 2, how many do you have?'




Traditional Approach Output: '1'



Chain of Thought Output:



Step 1: There are 3 apples in total.

Step 2: You ta
ke away 2 apples.

Step 3: You now have the 2 apples you took away.

Final Answer: 2
```
---

     
 
all -  [ Looking for Open-Source Apps for Best Practices ](https://www.reddit.com/r/LangChain/comments/1fm014s/looking_for_opensource_apps_for_best_practices/) , 2024-09-22-0914
```
Hey everyone! 👋

I’m learning LangChain and working on an open-source app using LangGraph and Next.js. I’m on the lookou
t for best practices, good patterns, and looking for some open-source apps that can help us overcome some challenges. 


**About my project:**

I've just launched **Aithelete** ([https://aithelete.vercel.app/](https://aithelete.vercel.app/))
, an AI Agent and fitness coach that creates personalized training programs. 🏋️‍♂️ It’s been a great learning experience
, and I’d love your feedback or suggestions to improve it! You can check out the code on GitHub here: [Aithelete on GitH
ub](https://github.com/mbarinov/aithelete). 🙌

**My current challenges:**

* **How to store prompts?** Best practices fo
r managing and updating prompts?
* **Any built-in retry tools?** Effective ways to handle retries in AI applications?
* 
**Should we use streaming in AI Agents?** When does it make sense?

Any insights, patterns, or feedback on Aithelete wou
ld be super helpful. Thanks—I’m excited to learn and keep growing! 😊
```
---

     
 
all -  [ Debugging Langgraph Cloud with breakpoints ](https://www.reddit.com/r/LangChain/comments/1flxq26/debugging_langgraph_cloud_with_breakpoints/) , 2024-09-22-0914
```
Hi guys, does any of you manage to debug langgraph cloud using VSCode breakpoints and if yes how did he do it?

My intui
tion is that since it runs on a container it should be possible by using vscode extension dev container, but maybe I am 
wrong.

Thanks
```
---

     
 
all -  [ RAG using JSON file with nested referencing or chained referencing ](https://www.reddit.com/r/LangChain/comments/1flmupc/rag_using_json_file_with_nested_referencing_or/) , 2024-09-22-0914
```
I am working with a JSON file where each object has a unique ID. The user queries using the unique ID of a particular ob
ject. Depending on the query, I may need to directly fetch certain field values from that object, or follow chained refe
rences to fetch data from related objects. The chain of references can sometimes go 2-3 levels deep.

How would I make m
y RAG agent aware of the structure of this JSON schema, so it knows which references to follow to answer the user's quer
y appropriately. For example, if an object references another object via a unique ID, the agent should understand how to
 resolve that reference and fetch the relevant data from the linked object.

**Current Setup:**

* I’ve parsed the JSON 
using LangChain's `JSONLoader`.
* I’m using `OpenAIEmbeddings` and storing the data in a Chroma VectorDatabase.
* I'm us
ing Gemini LLM for query responses.

I need some overview of the flow to implement
```
---

     
 
all -  [ RAG using JSON file with nested referencing or chained referencing ](https://www.reddit.com/r/Rag/comments/1flmtri/rag_using_json_file_with_nested_referencing_or/) , 2024-09-22-0914
```
I am working with a JSON file where each object has a unique ID. The user queries using the unique ID of a particular ob
ject. Depending on the query, I may need to directly fetch certain field values from that object, or follow chained refe
rences to fetch data from related objects. The chain of references can sometimes go 2-3 levels deep.

How would I make m
y RAG agent aware of the structure of this JSON schema, so it knows which references to follow to answer the user's quer
y appropriately. For example, if an object references another object via a unique ID, the agent should understand how to
 resolve that reference and fetch the relevant data from the linked object.

**Current Setup:**

* I’ve parsed the JSON 
using LangChain's `JSONLoader`.
* I’m using `OpenAIEmbeddings` and storing the data in a Chroma VectorDatabase.
* I'm us
ing Gemini LLM for query responses.

I need some overview of the flow to implement
```
---

     
 
all -  [ Resolution of Lanchain critical vulnerability ](https://www.reddit.com/r/LangChain/comments/1flkmok/resolution_of_lanchain_critical_vulnerability/) , 2024-09-22-0914
```
I'm using langchain in my job and a recent critical vulnerability [CVE-2024-46946](https://www.mend.io/vulnerability-dat
abase/CVE-2024-46946) is creating an issue in our deployments:

langchain\_experimental (aka LangChain Experimental) 0.1
.17 through 0.3.0 for LangChain allows attackers to execute arbitrary code through sympy.sympify (which uses eval) in LL
MSymbolicMathChain. LLMSymbolicMathChain was introduced in fcccde406dd9e9b05fc9babcbeb9ff527b0ec0c6 (2023-10-05).

  
It
 seems to be up to the latest version of langchain. Are there any updates on when this will be resolved?
```
---

     
 
all -  [ A new chunking algorithm proposal - Semantically chunking based on sliding token windows and similar ](https://www.reddit.com/r/LangChain/comments/1flhtxi/a_new_chunking_algorithm_proposal_semantically/) , 2024-09-22-0914
```
[Link to the chunking algorithm](https://github.com/nesbyte/ResearchChunkingStrategies/blob/main/main.ipynb) - there are
 samples of it's output at the bottom of the notebook, feedback/comments are welcome!

The new approach uses a sliding w
indow between token embeddings and does similarity comparisons between the sliding windows, once the similarities revers
e (local minima is found), that is where a chunk break is introduced. *This approach does not require any thresholds or 
manual tuning - it is inherently dynamic (and recursive if needed)*. [More detail provided in the notebook.](https://git
hub.com/nesbyte/ResearchChunkingStrategies/blob/main/main.ipynb)

This approach is designed for larger uniform bodies of
 text.

Depending on feedback variations can be made to be able to control chunk size and also benchmark it in a similar
 method as mentioned in [Chroma's chunking strategies for retrieval](https://research.trychroma.com/evaluating-chunking)
 paper.
```
---

     
 
all -  [ Filtering nested json response ](https://www.reddit.com/r/LangChain/comments/1flefus/filtering_nested_json_response/) , 2024-09-22-0914
```
Hey all,

What's the best way give an llm contest of a json object. The API I'm calling has multiple nested Json objects
 like this:

    {
      'General': {
        'Code': 'AAPL',
        'Type': 'Common Stock',
        'Name': 'Apple',
 
     },
      'Holders': {
        'Institutions': {},
        'Funds': {
          '0': {
            'name': 'Vanguard
 International Stock Index-Total Intl Stock Indx',
            'date': '2020-10-31',
            'totalShares': 1.52,
  
          'currentShares': 26895154
          },
          '1': {
            'name': 'Vanguard Tax Managed Fund-Vanguar
d Developed Markets Index Fund',
            'date': '2020-12-31',
            'totalShares': 0.64,
            'current
Shares': 11335622
          },
      }
      'Earnings': {
        'Trend': {
          '2024-06-30': {
            'dat
e': '2025-06-30',
            'growth': '-0.0220',
            'earningsEstimateAvg': '5.6700',
            'earningsEst
imateLow': '5.0100',
            'earningsEstimateHigh': '6.2200',
          },
          '2024-03-30': {
            'd
ate': '2024-06-30',
            'growth': '-0.0140',
            'earningsEstimateAvg': '5.8000',
            'earningsE
stimateLow': '5.5100',
            'earningsEstimateHigh': '5.9000',
          },
          '2023-12-31': {
            
'date': '2024-03-31',
            'growth': null,
            'earningsEstimateAvg': '5.8000',
            'earningsEsti
mateLow': '5.5100',
            'earningsEstimateHigh': '5.9000',
          },
    }

So for example if I want to ask th
e model to 'give me the latest 3 quarters of average earnings estimates', what is the best way to give the model context
 of the json schema so that it filters the data reliably get the Earnings\['Trent'\]\['date'\]\['earningsEstimateAvg'\] 
values?

I want the model to create the filter, not have the model process the json string and provide a response, becau
se the filtered data may be hundred objects.

So far all i can think of is adding the schema to the system prompt or the
 docstring of the langgraph toolcall, but the schema could be very large.

(p.s i'm using langgraph as well)
```
---

     
 
all -  [ LlamaIndex vs LangChain vs Pathway vs Others (2024 Guide to Top RAG Frameworks) ](https://www.reddit.com/r/LlamaIndex/comments/1fld7nw/llamaindex_vs_langchain_vs_pathway_vs_others_2024/) , 2024-09-22-0914
```
We’ve just released our **2024 guide** on the top RAG frameworks. Based on our RAG deployment experience, here are some 
key factors to consider when picking a framework:

**Key Factors for Selecting a RAG Framework:**

1. **Deployment Flexi
bility:** Does it support both local and cloud deployments? How easily can it scale across different environments?
2. **
Data Sources and Connectors:** What kind of data sources can it integrate with? Are there built-in connectors?
3. **RAG 
Features:** What retrieval methods and indexing capabilities does it offer? Does it support advanced querying techniques
?
4. **Advanced Prompting and Evaluation:** How does it handle prompt optimization and output evaluation?

**Comparison 
page:** [https://pathway.com/rag-frameworks](https://pathway.com/rag-frameworks)

It includes a detailed tabular compari
son of several frameworks, such as Pathway (our framework with 8k+ GitHub stars), Cohere, LlamaIndex, LangChain, Haystac
k, and the Assistants API.

Let me know what you think!
```
---

     
 
all -  [ Comparison between the Top RAG Frameworks (2024) ](https://www.reddit.com/r/LangChain/comments/1fld63q/comparison_between_the_top_rag_frameworks_2024/) , 2024-09-22-0914
```
We’ve just released our **2024 guide** on the top RAG frameworks. Based on our RAG deployment experience, here are some 
key factors to consider when picking a framework:

**Key Factors for Selecting a RAG Framework:**

1. **Deployment Flexi
bility:** Does it support both local and cloud deployments? How easily can it scale across different environments?
2. **
Data Sources and Connectors:** What kind of data sources can it integrate with? Are there built-in connectors?
3. **RAG 
Features:** What retrieval methods and indexing capabilities does it offer? Does it support advanced querying techniques
?
4. **Advanced Prompting and Evaluation:** How does it handle prompt optimization and output evaluation?

**Comparison 
page:** [https://pathway.com/rag-frameworks](https://pathway.com/rag-frameworks)

It includes a detailed tabular compari
son of several frameworks, such as Pathway (our framework with 8k+ GitHub stars), Cohere, LlamaIndex, LangChain, Haystac
k, and the Assistants API.
```
---

     
 
all -  [ Langgraph Studio does not capture code changes ](https://www.reddit.com/r/LangChain/comments/1fla0ac/langgraph_studio_does_not_capture_code_changes/) , 2024-09-22-0914
```
I like the idea of langgraph studio, but it looks like it does not capture code changes, which make it quite useless.

B
ecause a very good use would be to be able to fork a call and see how the output changes when changing prompt or tool lo
gics.

Am i missing something?
```
---

     
 
all -  [ Are ollama and gpt agents different in how they work? ](https://www.reddit.com/r/LangChain/comments/1fl9z2t/are_ollama_and_gpt_agents_different_in_how_they/) , 2024-09-22-0914
```
Hi. I am currently using ollama (llama3.1) to create an agent and do data visualization using retriever and csv query.


And here I have a problem.

I wanted to use gpt instead of ollama, so I set gpt to llm, but it seems that the agent work
s differently from llama3.1.

llama only uses the tools I set and does not generate multiple answers, but generates one 
answer per query.

However, when I set ChatOpenAI gpt to llm, it keeps generating multiple answers like ReAct and does n
ot seem to use the tools properly.

I will attach the code to create an agent using ollama and gpt below.

In this code,
 ollama works very well. But gpt does not.

**Please, I wish everything would work fine in gpt as well as in llama**

  
       llm = ChatOllama(model='llama3.1:70b')
        # llm = ChatOpenAI(model='gpt-4o-mini')
        
        tools = g
et_tools(state['df'], state['index'])
    
        agent = create_openai_functions_agent(llm, tools, prompt)
    
      
  agent_executor = AgentExecutor(
            agent=agent,
            tools=tools,
            verbose=True,
          
  handle_parsing_errors=False,
        )
```
---

     
 
all -  [ Hi does anyone have idea how can we consider accuracy of our chatbot? ](https://www.reddit.com/r/LangChain/comments/1fl8dir/hi_does_anyone_have_idea_how_can_we_consider/) , 2024-09-22-0914
```
I have searched some of the resource they mention many parameter out of which i found   
fallback rate interesting   
Ho
w to calculate the accuracy of a chatbot?

The easiest way is to check the total number of messages sent from the chatbo
t and check how many of them were Fallback messages. Deduct Fallback Messages from the total number of messages, then di
vide the number you got by the number of total messages and multiply it by 100.

Here’s an example:

You got 8,000 messa
ges. 750 out of those messages were fallback messages.

So, here’s what you do:

8,000 - 750 = 7,250  
7,250/8,000 = 0,9
06  
0,906\*100 = 90,6%

  
 but don't know how to calculate fallback message which message is fallback. Anyone have ide
a about this?  

```
---

     
 
all -  [ Is someone interested to join with me for learning #LLM #GenAI together??  ](https://www.reddit.com/r/LangChain/comments/1fl748j/is_someone_interested_to_join_with_me_for/) , 2024-09-22-0914
```

Is someone interested to join with me for learning #LLM #GenAI together?? 

I have basic idea of LLM and did some hands
 on too. But planning to understand the working behind in detail. So if anyone intrested then please DM me. Planning to 
start from tomorrow.

```
---

     
 
all -  [ SurfSense - Personal AI Assistant for World Wide Web Surfers. ](https://www.reddit.com/r/LangChain/comments/1fl5axm/surfsense_personal_ai_assistant_for_world_wide/) , 2024-09-22-0914
```
Hi Everyone,

For the past few months I have been trying to build a Personal AI Assistant for World Wide Web Surfers. It
 basically lets you form your own personal knowledge base from the webpages you visit. One of the feedback was to make i
t compatible with Local LLMs so just released a new version with Ollama support.

**What it is and why I am making it:**
  
Well when I’m browsing the internet, I tend to save a ton of content—but remembering when and what you saved? Total b
rain freeze! That’s where SurfSense comes in. SurfSense is a Personal AI Assistant for anything you see (Social Media Ch
ats, Calendar Invites, Important Mails, Tutorials, Recipes and anything ) on the World Wide Web. Now, you’ll never forge
t any browsing session. Easily capture your web browsing session and desired webpage content using an easy-to-use cross 
browser extension. Then, ask your personal knowledge base anything about your saved content, and voilà—instant recall!


# Key Features

* 💡 **Ide**a: Save any content you see on the internet in your own personal knowledge base.
* ⚙️ **Cross
 Browser Extension**: Save content from your favourite browser.
* 🔍 **Powerful Searc**h: Quickly find anything in your W
eb Browsing Sessions.
* 💬 **Chat with your Web Histor**y: Interact in Natural Language with your saved Web Browsing Sess
ions.
* 🔔 **Local LLM Suppor**t: Works Flawlessly with Ollama local LLMs.
* 🏠 **Self Hostabl**e: Open source and easy to
 deploy locally.
* 📊 **Advanced RAG Technique**s: Utilize the power of Advanced RAG Techniques.
* 🔟% **Cheap On Walle**t
: Works Flawlessly with OpenAI gpt-4o-mini model and Ollama local LLMs.
* 🕸️ **No Web Scrapin**g: Extension directly rea
ds the data from DOM to get accurate data.

Please test it out at [https://github.com/MODSetter/SurfSense](https://githu
b.com/MODSetter/SurfSense) and let me know your feedback.

https://reddit.com/link/1fl5axm/video/5u0m7o4pnwpd1/player


```
---

     
 
all -  [ Looking for recommendations to build a search application ](https://www.reddit.com/r/LangChain/comments/1fkzfu5/looking_for_recommendations_to_build_a_search/) , 2024-09-22-0914
```
Hi everyone, I believe this use-case/problem has been around for some time but since I am pretty new to the whole LLM wo
rld, I am still unsure what's the best way to develop such applications. 

What I'm trying to develop is an application 
that can take in a question (written in natural language) from the user, conduct a search over the internet (and perhaps
 internal local storages and databases), and come up with the list of top 5-10 results that are the most relevant to the
 user's query. 

With these results, the application summarises them and answers the original question in natural langua
ge, with citations from the search result (something like what Perplexity is doing). 

The 'special' thing about this ap
plication is that it is built for a small circle of network (a high net-worth group of users in a niche industry) so the
 answers have to be super relevant to the industry as well as their professions. 

Currently, the plan I have is Tavily,
 LangGraph, and MongoDB.

1. With the user's query, conduct a Tavily search to get at least 50 results.
2. Develop a con
text (just paragraphs of context) and do some rankings with the list of found results.
3. With the 5-10 top-ranked resul
ts, conduct some certain summarization with an agent and show the final answer on the app.

It sounds insanely simple an
d I am sure this is a popular topic/use-case and the community has come up with more successfuly/sophisticated solutions
. Can everyone advise?

Any ideas, knowledge sharing or advice is most welcome! Thank you!
```
---

     
 
all -  [ [P] Swapping Embedding Models for an LLM ](https://www.reddit.com/r/MachineLearning/comments/1fktvbj/p_swapping_embedding_models_for_an_llm/) , 2024-09-22-0914
```
How tightly coupled is an embedding model to a language model?

Taking an example from Langchain's tutorials, they use O
llama's _nomic-embed-text_ for embedding and _Llama3.1_ for the understanding and Q/A. I don't see any documentation abo
ut Llama being built on embeddings from this embedding model. 

Intuition suggests that a different embedding model may 
produce outputs of other sizes or produce a different tensor for a character/word, which would have an impact on the res
ults of the LLM. So would changing an embedding model require retraining/fine-tuning the LLM as well?

I need to use a e
mbedding model for code snippets and text. Do I need to find a specialized embedding model for that? If yes, how will ll
ama3.1 ingest the embeddings?
```
---

     
 
all -  [ Need Help with Langchain for Feeding Gemini LLM Direct PDFs in Base64 Format ](https://www.reddit.com/r/LangChain/comments/1fksrqc/need_help_with_langchain_for_feeding_gemini_llm/) , 2024-09-22-0914
```
Hey everyone,

I’m currently working with Langchain and Vertex AI’s Gemini model, and I need some help with feeding PDF 
files directly to Gemini. The files I have are encoded in Base64 format, and I’m looking for a way to process them corre
ctly.

I tried using a similar approach with an image example, but it’s not working for me. Here’s the code snippet I’ve
 been working with:

import base64

# Load PDF file in binary mode
with open('document_example.pdf', 'rb') as pdf_file:

    pdf_bytes = pdf_file.read()

# Create a base64-encoded message for the PDF
pdf_message = {
    'type': 'document_url
',
    'document_url': {
        'url': f'data:application/pdf;base64,{base64.b64encode(pdf_bytes).decode('utf-8')}'
   
 },
}
text_message = {
    'type': 'text',
    'text': 'What is the content of this PDF document?',
}

# Prepare input f
or model consumption
message = HumanMessage(content=[text_message, pdf_message])

# Invoke a model response
output = llm
.invoke([message])
print(output.content)

Llm responses are like “I am unsure how to process base64 encoded files”
Someh
ow this code is not working, and I’m not sure what I’m missing. Any ideas on how to handle PDFs encoded in Base64, or wh
at adjustments need to be made to this snippet to work with Langchain and Gemini?

Thanks in advance!

Let me know if yo
u’d like any more adjustments! 
```
---

     
 
all -  [ LangGraph allows you to make falsifiable, testable agents that are actually useful. ](https://www.reddit.com/r/datascience/comments/1fknbyi/langgraph_allows_you_to_make_falsifiable_testable/) , 2024-09-22-0914
```
I recently had a conversation with the founder of Arize, an AI testing and observability platform. he said something int
eresting which I'll paraphrase:

'ReAct agents aren't successful in production because they're too vague. More constrain
ed agents, like graph based agents, have been doing much better'. - [source](https://www.youtube.com/watch?v=N59Z7uJ8DDA
&list=PLPaLTf0W0L_P8p5GmJFBSwEIr0PinWPpH&index=2)

talking about agents with a company focused in AI observability and t
esting was a breath of fresh air, and had me thinking of agents in a new and radical way: Like they're software which ne
eds to be testable.

For those of you who don't know, LangGraph is a new set of tooling by LangChain which allows you to
 structure an agent as a directed graph. There are nodes which allow you to do operations, edges which allow you to chai
n operations together, and decision edges which allow you to make a decision based on some criteria. I think there are a
 few ways to actually make these graphs, but I'm only familiar with the 'state graph', which allows you to define some s
tate object (which is a dictionary with a bunch of default values) that gets passed around throughout the graph. This al
lows you to do things like:

* Keep track of the conversational flow
* Keep track of key parsed data
* Keep track of exp
licit application logic
* Work with stateless API setups, presumably, because the state is atomic and serializable
* Emp
loy explicit programmatic steps in the conversation/process seamlessly.

Here's an example of a conversation with a grap
h based agent I created. Notice how well it marries strict programatic rules and strange conversational edge cases: some
thing more loosely defined agents like ReAct struggle with.

    Hi there! I'm Rachael, and I'm excited to help you get 
set up with a new home. Could you please provide me with your full name so we can get started?
    dan w
    Hi Dan, it 
looks like your name might be incomplete. Could you please provide your full name or confirm if 'Dan W' is indeed your f
ull name? This will help me get started on finding the perfect home for you.
    yeah beleive it or not that's actually 
my full name. Weird parents.
    Nice to meet you, Dan W! Do you already have an account set up with us?
    yep
    Gre
at, Dan! Could you please provide the email address associated with your account?
    yeah it's 
    Great, Dan! A short
 code has been sent to your email. Could you please check your inbox and provide me with that code to confirm your email
?
    just got it. 1111
    Email verified. Done!
    output state:
    {'first_name': 'Dan', 'last_name': 'W', 'increme
ntor': 5, 'conversation':...}hire@danielwarfield.dev

[source, with code](https://iaee.substack.com/p/langgraph-intuitiv
ely-and-exhaustively)

The fact that this conversation is, under the hood, structured as a directed graph allows me to m
odify key points in the conversation explicitly, rather than contend with a single massive prompt which governs the whol
e conversation.

I’ve had a lot of conversations with some heavy hitters in the industry over the last few months, and I
’m seeing a regular theme: If AI can’t transcend the twitter demo and become actual useful products, then the industry i
s in a world of hurt. Luckily, I think graph based agents are the right balance of abstract and specific to solve a lot 
of conversational use cases. I expect we’ll see them grow as a fundamental component of modern LLM powered applications.

```
---

     
 
all -  [ all up-to-date knowledge + code on Agents and RAG in one place! ](https://diamantai.substack.com/) , 2024-09-22-0914
```
Hey everyone! You've probably seen me writing here frequently, sharing content about RAG and Agents. I'm leading the ope
n-source GitHub repo of RAG_Techniques, which has grown to 6.3K stars (as of the moment of writing this post), and I've 
launched a soaring new repo of GenAI agents.

I'm excited to announce a free initiative aimed at democratizing AI and co
de for everyone.

 I've just launched a **new newsletter** (600 subscribers in just a week!) that will provide you with 
all the insights and updates happening in the tutorial repos, as well as blog posts describing these techniques.

We als
o support academic researchers by sharing code tutorials of their cutting-edge new technologies.

Plus, we have a flouri
shing Discord community where people are discussing these technologies and contributing.

Feel free to join us and enjoy
 this journey together! 😊
```
---

     
 
all -  [ Do Podcast with Albert Einstein!! ](https://www.reddit.com/r/SideProject/comments/1fkkc4c/do_podcast_with_albert_einstein/) , 2024-09-22-0914
```
Okay!   
So on 15th September 2024, I got this idea of creating an webapp which lets you do podcast with great peoples l
ike Albert Einstein, Steve Jobs, Elon Musk and many more and I started creating it just 15 minute after I got the idea o
n 15th Sep. late evening. I created the landing page in just 55 minutes. (A record time for me, Haha)   
  
Check it her
e ([PodMeAI](http://podmeai.vercel.app)) - [podmeai.vercel.app](http://podmeai.vercel.app) (web, is done waitlist is ope
n and I will make it live with product hunt launch)  
  
After which I jumped on the biggest part, how can I get NLP to 
a place where it always talk like someone with as high accuracy as possible, So I added hugging face and removed it and 
tried pinecone and langchain but didn't worked well so removed it again and added hugging face again : ). Now you are th
inking how did do it in a single day?!! and the answer is **I like what I do**.

I completed the rest of things like UI 
etc. till 17 late night 2:00 AM and today on 18 I thought what if I also add chat with PDF option and just did it till l
ate night of 18 Sep. 3:00 AM or so.   
  
Now today I made the UI better and added the subscription with stripe and read
y to launch. 

I also made challenge to myself in build in public on X that I will complete this in 5 days and here I di
d it in just 4 days. [https://x.com/miteshmawar](https://x.com/miteshmawar)  
  
**If you have idea just got an do it!!!
!**
```
---

     
 
all -  [ Need help with using RAG, I need to know if this idea is plausible ](https://www.reddit.com/r/LangChain/comments/1fkkbsx/need_help_with_using_rag_i_need_to_know_if_this/) , 2024-09-22-0914
```
The goal is to create a document that contains condensed data from hundreds of documents. The system will first analyze 
hundreds of PDFs, extract the relevant data and create a document with only the relevant data from each document. It kin
d of functions as a spreadsheet, like:

For document 100, the author is a, the document was created on 1/1/2000, and it 
is about x.

For document 101, the author is b, the document was created on 1/2/2002, and it is about y.

For document 1
02, the author is c, the document was created on 3/1/2005, and it is about z.

So this is my question. This document, ev
en though it's condensed, will eventually be somewhat large just because of the amount of documents and information (mor
e than in my example).

So if I use a rag an LLM and ask 

'give me a list of documents that are about y'

or 

'give me
 a list of documents written by c in the  year 2002'

To get this information, and for it to be complete, it would neces
sarily have to read through \*every\* line of the document, not just a few chunks, to be accurate. So wouldn't this defe
at the purpose of using a RAG, which would limit how much of the document is read? 

Is there a better way to do what I'
m trying to accomplish? The results at the moment haven't been that great. Right now I'm using a chroma vector DB with h
uggingface embeddings.
```
---

     
 
all -  [ I made this whole SaaS in just 4 days! ](https://www.reddit.com/r/SaaS/comments/1fkk92u/i_made_this_whole_saas_in_just_4_days/) , 2024-09-22-0914
```
Okay!   
So on 15th September 2024, I got this idea of creating an webapp which lets you do podcast with great peoples l
ike Albert Einstein, Steve Jobs, Elon Musk and many more and I started creating it just 15 minute after I got the idea o
n 15th Sep. late evening. I created the landing page in just 55 minutes. (A record time for me, Haha)   
  
Check it her
e ([PodMeAI](http://podmeai.vercel.app)) - [podmeai.vercel.app](http://podmeai.vercel.app) (web, is done waitlist is ope
n and I will make it live with product hunt launch)  
  
After which I jumped on the biggest part, how can I get NLP to 
a place where it always talk like someone with as high accuracy as possible, So I added hugging face and removed it and 
tried pinecone and Langchain but didn't worked well so removed it again and added hugging face again : ). Now you are th
inking how did do it in a single day?!! and the answer is **I like what I do**.

I completed the rest of things like UI 
etc. till 17 late night 2:00 AM and today on 18 I thought what if I also add chat with PDF option and just did it till l
ate night of 18 Sep. 3:00 AM or so.   
  
Now today I made the UI better and added the subscription with stripe and read
y to launch. 

I also made challenge to myself in build in public on X that I will complete this in 5 days and here I di
d it in just 4 days. [https://x.com/miteshmawar](https://x.com/miteshmawar)  
  
**If you have idea just got an do it!!!
!**
```
---

     
 
all -  [ Seeking advice: AI-powered summaries for MS Teams and Email to feed our knowledge base ](https://www.reddit.com/r/LangChain/comments/1fkjr7e/seeking_advice_aipowered_summaries_for_ms_teams/) , 2024-09-22-0914
```
Hey there, fellow AI enthusiasts and productivity gurus! I'm working on a project that's got me proper chuffed, but I co
uld use some sage advice from the hive mind.

**The goal:** We're aiming to create AI-powered summaries of our MS Teams 
group chats, channels, meeting notes, and email messages. These summaries will then be fed into our complex knowledge ba
se on a continuous basis.

**The challenge:** While we're already working with AI agents, I'm wondering if there are exi
sting solutions or libraries that could streamline our process or complement what we're doing. I'm particularly interest
ed in:

1. Tools specifically designed for summarising MS Teams content
2. Email summarisation libraries or services
3. 
AI-powered summarisation libraries that excel at condensing conversational text

**Our current approach:** We're using c
ustom AI agents to handle the summarisation, but I can't help feeling like we might be reinventing the wheel in some are
as.

**Questions for you lovely lot:**

1. Have any of you tackled a similar challenge? What was your approach?
2. Are t
here any standout libraries or services for AI-powered summarisation that you'd recommend?
3. How are you handling the c
ontinuous feeding of summaries into your knowledge base? Any tips for keeping it all organised and easily searchable?
4.
 Any potential pitfalls or challenges we should be aware of when summarising sensitive business communications?

I'm dea
d keen to hear your thoughts, experiences, and recommendations. Cheers in advance for any help you can offer!

**TL;DR:*
* Looking for advice on AI-powered summarisation tools/libraries for MS Teams and email content to feed into a knowledge
 base. Any recommendations or experiences to share?
```
---

     
 
all -  [ LangChain Invoke Error ](https://www.reddit.com/r/LangChain/comments/1fkjirr/langchain_invoke_error/) , 2024-09-22-0914
```
Hi Everyone ,

Good day ,

Any idea whats wrong with my below code ? I am using LangChain + DeepSeek and I am getting th
e below error.

    UnprocessableEntityError: Failed to deserialize the JSON body into the target type: prompt: invalid 
type: sequence, expected a string at line 1 column 3

TIA

My code for this.

    import langchain
    from langchain_op
enai import OpenAI
    # from langchain_core.prompts import PromptTemplate
    import os
    
    # Ensure the API key i
s set
    api_key = os.getenv('DEEPSEEK_API_KEY')
    
    # Initialize the OpenAI model
    llm = OpenAI(model='deepsee
k-chat',   api_key=api_key, base_url='https://api.deepseek.com/beta')
    
    response = llm.invoke('Hi!')
    print(re
sponse.content)
```
---

     
 
all -  [ Improving RAG Application: Chunking, Reranking, and Lambda Cold-Start Issues ](https://www.reddit.com/r/aws/comments/1fkhbmv/improving_rag_application_chunking_reranking_and/) , 2024-09-22-0914
```
I'm developing a Retrieval-Augmented Generation (RAG) application using the following AWS services and tools:

- AWS Lam
bda

- Amazon Bedrock

- Amazon Aurora DB

- FAISS (Facebook AI Similarity Search)

- LangChain

I'm encountering model 
hallucination issues when asking questions. Despite adjusting hyperparameters, the problems persist. I believe implement
ing a reranking strategy and improving my chunking approach could help. Additionally, I'm facing Lambda cold-start issue
s that are increasing latency.

Current chunking constants:

    TOP_P = 0.4
    
    CHUNK_SIZE = 3000
    
    CHUNK_O
VERLAP = 100
    
    TEMPERATURE_VALUE = 0.5
    

Issues:

1. Hallucinations: The model is providing incomplete answer
s and showing confusion when choosing tools (LangChain).
2. Chunking strategy: I need help understanding and fixing issu
es with my current chunking approach.
3. Reranking: I'm looking for lightweight, open-source reranking tools and models 
compatible with the Llama 3 model on Amazon Bedrock.
4. Lambda cold-start: This is increasing the latency of my applicat
ion.

Questions:

1. How can I understand and improve my chunking strategy to reduce hallucinations?
2. What are some li
ghtweight, open-source reranking tools and models compatible with the Llama 3 model on Amazon Bedrock? (I prefer to stic
k with Bedrock.)
3. How can I address the Lambda cold-start issues to reduce latency?
```
---

     
 
all -  [ What's the Type / Shape of the data for Checkpointers / Custom MemorySaver in LangGraph JS? ](https://www.reddit.com/r/LangChain/comments/1fkhbbr/whats_the_type_shape_of_the_data_for/) , 2024-09-22-0914
```
I need to create a custom MemorySaver for the database I'm using and I'm wondering what the schema is of the Records to 
be stored in the Database. 

Is there an explanation of exactly this? Is it a Checkpoint? Is it a Thread? Is a Thread pa
rt of a Checkpoint? It'd be great to know what parts are put together to make up the 'stuff'. 

I've looked at the Metho
ds in MemorySaver so I think I can see some of it, but is there a clear definition of it somewhere??
```
---

     
 
all -  [ I have been trying to get Chatgroq to work for tool calling using the llama3-8b-8192 model. For some ](https://www.reddit.com/r/LangChain/comments/1fkf9fc/i_have_been_trying_to_get_chatgroq_to_work_for/) , 2024-09-22-0914
```
Here's a link to my script: [https://pastebin.com/p2qjz3k2](https://pastebin.com/p2qjz3k2)
```
---

     
 
all -  [ Guardrails on LangGraph ](https://www.reddit.com/r/LangChain/comments/1fkev19/guardrails_on_langgraph/) , 2024-09-22-0914
```
Hey everyone, I trying to develop a Customer Assistant Chatbot project using LangGraph. As a last step I wanna add a gua
rdrails layer to my flow. If the generated response contains competitor names we won't show the response to the user, to
 do this I want to use Competitor Check from Guardrails AI. But I can't understant how can I apply that to my project.


Guardrails: [https://hub.guardrailsai.com/validator/guardrails/competitor\_check](https://hub.guardrailsai.com/validator
/guardrails/competitor_check)

  
Should I get the last messages from the state and check it if response contains compet
itor names or not. If doesn't contain we can show the response but it does we will return a different messages? right?


And will it be the last node in agent flow right?

Thanks.
```
---

     
 
all -  [ Building RAG with Postgres ](https://www.reddit.com/r/Rag/comments/1fkdtmg/building_rag_with_postgres/) , 2024-09-22-0914
```
hey :) i've gotten a lot of requests to write this posts about using postgres for RAg as people seem to want  
- a simpl
er stack  
- move away from frameworks like LangChain

here's the post: [https://anyblockers.com/posts/building-rag-with
-postgres](https://anyblockers.com/posts/building-rag-with-postgres)

let me know what you think!
```
---

     
 
all -  [ Output based on the tool used ](https://www.reddit.com/r/LangChain/comments/1fkdq0v/output_based_on_the_tool_used/) , 2024-09-22-0914
```
So I am working with an agent who has access to N tools. Based on the user prompt the agent can access any tool and resp
ond back. 

Before sending the response back to the user I want to format it for a ui framework I am using based on whic
h tool is returning the final output. 
I don't want the tools directly to return this output as it might confuse the age
nt. 
```
---

     
 
all -  [ Multimodal_RAG ](https://www.reddit.com/r/Rag/comments/1fkdhhr/multimodal_rag/) , 2024-09-22-0914
```
Hello everyone, I am new to reddit and Gen AI field as well...While there are already some really awesome templates/Full
 stack solutions out there, its just too much information to follow for someone like me so i created one myself. Do chec
k it out [here](https://github.com/sallu-786/Multimodal_RAG) . Suggestions/contributions are more than welcome

[Made us
ing Streamlit+Langchain+OpenAI\/Ollama](https://reddit.com/link/1fkdhhr/video/47pggx3lbppd1/player)
```
---

     
 
all -  [ Help Needed with Calculating Pricing for Processing Documents with Langchain #26640
 ](https://www.reddit.com/r/LangChain/comments/1fk91la/help_needed_with_calculating_pricing_for/) , 2024-09-22-0914
```
Hi Langchain Team,

I’m working on a project where I load documents (PDF, DOCX, TXT), split them into smaller chunks usi
ng the RecursiveCharacterTextSplitter, and then convert them into graph nodes and relationships with LLMGraphTransformer
 to store in a graph database.  
I want to **calculate the number of tokens and/or the price when using the LLMGraphTran
sformer for one document.**

Here’s a simplified version of my process:

Load the document (different formats like PDF, 
DOCX, TXT).  
Split the document into chunks using RecursiveCharacterTextSplitter (chunk size: 1500, overlap: 30).  
Ext
ract nodes and relationships using LLMGraphTransformer.  
Store the nodes and relationships in a graph database (e.g., N
eo4j).  
I would like to calculate the cost for processing each document, considering the following:

Each chunk of text
 processed by the model contributes to the cost.  
I’m using OpenAI’s API for the LLM transformation.  
I need to unders
tand how to calculate or estimate the pricing for each document based on its size, the number of tokens, and the number 
of API calls.  
Questions:

Is there an existing Langchain function or utility that helps calculate costs based on the n
umber of tokens or API calls made during the document processing?  
What’s the best way to estimate or calculate costs f
or each document processed, especially when the document is split into multiple chunks?  
I appreciate any guidance or e
xamples on how to approach pricing for document conversion with Langchain.

Thank you in advance!

    class DocumentPro
cessor:
    def init(self, llm, allowed_nodes, allowed_relationships):
    self.llm = llm
    self.allowed_nodes = allow
ed_nodes
    self.allowed_relationships = allowed_relationships
    def load_document(self, doc_path):
        '''
     
   Load the document based on its format (PDF, DOCX, TXT)
        '''
        if doc_path.endswith('.pdf'):
            
loader = PyMuPDFLoader(doc_path)
        elif doc_path.endswith('.docx') or doc_path.endswith('.doc'):
            loade
r = Docx2txtLoader(doc_path)
        elif doc_path.endswith('.txt'):
            loader = TextLoader(doc_path)
        e
lse:
            raise ValueError('Unsupported file format')
    
        return loader.load()
    
    def process_docu
ment(self, doc_path, document_type='', topic='', user=None, case=None, process=None, num_splits=0):
        try:
       
     # Load the document
            print('Processing document: ', doc_path)
            doc = self.load_document(doc_p
ath)
    
            # Implementing the text splitter
            text_splitter = RecursiveCharacterTextSplitter(chunk_
size=1500, chunk_overlap=30)
            documents_split = text_splitter.split_documents(doc)
    
            # Initial
ize LLMGraphTransformer
            llm_transformer = LLMGraphTransformer(llm=self.llm, allowed_nodes=self.allowed_nodes
, allowed_relationships=self.allowed_relationships)
            
            # Convert document splits into graph docume
nts
            graph_documents = llm_transformer.convert_to_graph_documents(documents_split)
    
            # Here I 
would process the `graph_documents` to extract nodes/relationships
            # and store them in a graph database (e.g
., Neo4j)
            
            return graph_documents
    
        except Exception as e:
            print(f'Error 
processing document {doc_path}: {e}')
            return None
```
---

     
 
all -  [ System requirements for Bge-reranker-base  ](https://www.reddit.com/r/huggingface/comments/1fk8tvb/system_requirements_for_bgererankerbase/) , 2024-09-22-0914
```
Hi all. Just a junior dev. I wanted to use Bge-reranker-base as my reranking model. I wanted to know what's the system r
equirements. I searched the internet, but wasn't able to find. I wanted to know how much CPU and RAM will be used for CP
U only reranking, and GPU and RAM for GPU based reranking. The framework I use is langchain.
```
---

     
 
all -  [ Has anyone ever got `ChatHuggingFace` to work? ](https://www.reddit.com/r/huggingface/comments/1fk8er9/has_anyone_ever_got_chathuggingface_to_work/) , 2024-09-22-0914
```
This is more of a \*little\* bit of a frustration post than a question, but I've been at it for days trying to get stuff
 to work with the langchain x huggingface integration. The examples on both websites don't work (and just demonstrate op
enai examples), and the github issues where everyone is having the same problems seem unresolved? Any thoughts or contex
t? 😢
```
---

     
 
MachineLearning -  [ [P] Review and suggest ideas for my chatbot ](https://www.reddit.com/r/MachineLearning/comments/1fb2mwl/p_review_and_suggest_ideas_for_my_chatbot/) , 2024-09-22-0914
```
Ok, so I am currently trying to build support chatbot with following technicalities 
1. FastAPI for web server(Need to m
ake it faster)
2. Qdrant as Vector Data Base(Found it to be the fastest amongst Chromadb, Elastic Search and Milvus)
3. 
MongoDB for storing all the data and feedback.
4. Semantic chunking with max token limit of 512.
5. granite-13b-chat-v2 
as the LLM(I know it's not good but I have limited options available)
6. The data is structured as well as unstructured.
 Thinking of having involving GraphRAG with current architecture.
7. Multiple data sources stored in multiple collection
s of vector database because I have implemented an access control.
8. Using mongoengine currently as a ORM. If you know 
something better please suggest.
9. Using all-miniLM-l6-v2 as vector embedding currently but planning to use stella_en_4
00M_v5.
10. Using cosine similarity to retrieve the documents.
11. Using BLEU, F1 and BERT score for automated evaluatio
n based on golden answer.
12. Using top_k as 3.
13. Currently using basic question answering prompt but want to improve 
it. Any tips? Also heard about Automatic Prompt Evaluation.
14. Currently using custom code for everything. Looking to u
se Llamaindex or Langchain for this. 
15. Right now I am not using any AI Agent, but I want to know your opinions. 
16. 
It's a simple RAG framework and I am working on improving it.
17. I haven't included reranker but I am planning to do so
 too.

I think I mentioned pretty much everything I am using for my project. So please share your suggestions, comments 
and reviews for the same. Thank you!!
```
---

     
 
MachineLearning -  [ [P] Lessons from Retrieval Augmented Generation ](https://www.reddit.com/r/MachineLearning/comments/1f9tvg7/p_lessons_from_retrieval_augmented_generation/) , 2024-09-22-0914
```
I implemented Rag in my organization and just wrote a blog about what we learned here:   
[https://www.b-yond.com/post/t
ransforming-telco-troubleshooting-our-journey-building-telcogpt-with-rag](https://www.b-yond.com/post/transforming-telco
-troubleshooting-our-journey-building-telcogpt-with-rag)

Hoping it would be helpful for those in this area. Covers rag 
evaluation (ragas), sql db, langchain agents vs chains, weaviate vector db, hybrid search, reranking, and more.

Some ad
ditional insights on ranking and hybrid search here:

[https://www.linkedin.com/posts/drzohaib\_transforming-telco-troub
leshooting-our-journey-activity-7232072089837486081--Le1?utm\_source=share&utm\_medium=member\_android](https://www.link
edin.com/posts/drzohaib_transforming-telco-troubleshooting-our-journey-activity-7232072089837486081--Le1?utm_source=shar
e&utm_medium=member_android)
```
---

     
 
deeplearning -  [ What is the best approach for Parsing and Retrieving Code Context Across Multiple Files in a Hierarc ](https://www.reddit.com/r/deeplearning/comments/1fh58oz/what_is_the_best_approach_for_parsing_and/) , 2024-09-22-0914
```
I want to implement a Code-RAG system on a code directory where I need to:

* Parse and load all the files from folders 
and subfolders while excluding specific file extensions.
* Embed and store the parsed content into a vector store.
* Ret
rieve relevant information based on user queries.

However, I’m facing two major challenges:

**File Parsing and Loading
:** What’s the most efficient method to parse and load files in a hierarchical manner (reflecting their folder structure
)? Should I use Langchain’s directory loader, or is there a better way? I came across the Tree-sitter tool in Claude-dev
’s repo, which is used to build syntax trees for source files—would this be useful for hierarchical parsing?

**Cross-Fi
le Context Retrieval:** If the relevant context for a user’s query is spread across multiple files located in different 
subfolders, how can I fine-tune my retrieval system to identify the correct context across these files? Would reranking 
resolve this, or is there a better approach?

**Query Translation:** Do I need to use Something like Multi-Query or RAG-
Fusion to achieve better retrieval for hierarchical data?

\[I want to understand how tools like [continue.dev](http://c
ontinue.dev/) and [claude-dev](https://github.com/saoudrizwan/claude-dev) work\]
```
---

     
 
deeplearning -  [ Month of August in AI ](https://www.reddit.com/r/deeplearning/comments/1f6zfz0/month_of_august_in_ai/) , 2024-09-22-0914
```
🔍 I**nside this Issue:**

* 🤖 La*test Breakthroughs: *This month it’s all about A*gents, LangChain RAG, and LLMs evaluat
ion challenges.*
* 🌐 AI Monthly News: Discover how these stories are revolutionizing industries and impacting everyday l
ife: E*U AI Act, California’s Controversial SB1047 AI regulation act, Drama at OpenAI, and possible funding at OpenAI by
 Nvidia and Apple.*
* 📚 Editor’s Special: This covers the interesting talks, lectures, and articles we came across recen
tly.

Follow me on Twitter and LinkedIn at [**RealAIGuys**](https://twitter.com/RealAIGuys) and [**AIGuysEditor**](https
://www.linkedin.com/in/vishal-rajput-999164122/) to get insight on new AI developments.

>**Please don't forget to subsc
ribe to our Newsletter:** [**https://medium.com/aiguys/newsletter**](https://medium.com/aiguys/newsletter)

# Latest Bre
akthroughs

Are Agents just simple rules? Are Agents just enhanced reasoning? The answer is yes and no. Yes, in the sens
e that agents have simple rules and can sometimes enhance reasoning capabilities compared to a single prompt. But No in 
the sense that agents can have a much more diverse functionality like using specific tools, summarizing, or even followi
ng a particular style. In this blog, we look into how to set up these agents in a hierarchal manner just like running a 
small team of Authors, researchers, and supervisors.

[**How To Build Hierarchical Multi-Agent Systems?**](https://mediu
m.com/aiguys/how-to-build-hierarchical-multi-agent-systems-dc26b19201d2?sk=90958e39e1a28f5030872a90f8e3f3da)

**TextGrad
**. It is a powerful framework performing automatic “differentiation” via text. **It backpropagates textual feedback pro
vided by LLMs to improve individual components of a compound AI system.** In this framework, LLMs provide rich, general,
 natural language suggestions to optimize variables in computation graphs, ranging from code snippets to molecular struc
tures. TextGrad showed effectiveness and generality across various applications, from question-answering and molecule op
timization to radiotherapy treatment planning.

[**TextGrad: Improving Prompting Using AutoGrad**](https://medium.com/ai
guys/textgrad-controlling-llm-behavior-via-text-2a82e2073d10?sk=3633a9aa63b884c97469bce659265921)

The addition of RAG t
o LLMs was an excellent idea. It helped the LLMs to become more specific and individualized. Adding new components to an
y system leads to more interactions and its own sets of problems. Adding RAG to LLMs leads to several problems such as h
ow to retrieve the best content, what type of prompt to write, and many more.

In this blog, we are going to combine the
 **LangChain RAG with DSPy**. We deep dive into how to evaluate the RAG pipeline quantitatively using **RAGAs** and how 
to create a system where instead of manually tweaking prompts, we let the system figure out the best prompt.

[**How To 
Build LangChain RAG With DSPy?**](https://medium.com/aiguys/how-to-build-langchain-rag-with-dspy-ce9154fbafaa?sk=b41d104
05f84c767cf9cd6a58d1ebac0)

As the field of natural language processing (NLP) advances, the evaluation of large language
 models (LLMs) like GPT-4 becomes increasingly important and complex. Traditional metrics such as accuracy are often ina
dequate for assessing these models’ performance because they fail to capture the nuances of human language. In this arti
cle, we will explore why evaluating LLMs is challenging and discuss effective methods like BLEU and ROUGE for a more com
prehensive evaluation.

[**The Challenges of Evaluating Large Language Models**](https://medium.com/aiguys/the-challenge
s-of-evaluating-large-language-models-ec2eb834a349)

# AI Monthly News

# AI Act enters into force

On 1 August 2024, th
e European Artificial Intelligence Act (AI Act) enters into force. The Act aims to foster responsible artificial intelli
gence development and deployment in the EU. The AI Act introduces a uniform framework across all EU countries, based on 
a forward-looking definition of AI and a risk-based approach:

* **Minimal risk:** most AI systems such as spam filters 
and AI-enabled video games face no obligation under the AI Act, but companies can voluntarily adopt additional codes of 
conduct.
* **Specific transparency risk:** systems like chatbots must clearly inform users that they are interacting wit
h a machine, while certain AI-generated content must be labelled as such.
* **High risk:** high-risk AI systems such as 
AI-based medical software or AI systems used for recruitment must comply with strict requirements, including risk-mitiga
tion systems, high-quality of data sets, clear user information, human oversight, etc.
* **Unacceptable risk:** for exam
ple, AI systems that allow “social scoring” by governments or companies are considered a clear threat to people’s fundam
ental rights and are therefore banned.

**EU announcement:** [**Click here**](https://commission.europa.eu/news/ai-act-e
nters-force-2024-08-01_en)

https://preview.redd.it/nwyzfzgm4cmd1.png?width=828&format=png&auto=webp&s=c873db37ca0dadd5b
510bea70ac9f633b96aaea4

# California AI bill SB-1047 sparks fierce debate, Senator likens it to ‘Jets vs. Sharks’ feud


**Key Aspects of SB-1047:**

* Regulation Scope: Targets “frontier” AI models, defined by their immense computational t
raining requirements (over 10²⁶ operations) or significant financial investment (>$100 million).
* Compliance Requiremen
ts: Developers must implement safety protocols, including the ability to immediately shut down, cybersecurity measures, 
and risk assessments, before model deployment.
* Whistleblower Protections: Encourages reporting of non-compliance or ri
sks by offering protection against retaliation.
* Safety Incident Reporting: Mandates reporting AI safety incidents with
in 72 hours to a newly established Frontier Model Division.
* Certification: Developers need to certify compliance, pote
ntially under penalty of perjury in earlier drafts, though amendments might have altered this.

**Pros:**

* Safety Firs
t: Prioritizes the prevention of catastrophic harms by enforcing rigorous safety standards, potentially safeguarding aga
inst AI misuse or malfunction.
* Incentivizes Responsible Development: By setting high standards for AI model training, 
the company encourages developers to think critically about the implications of their creations.
* Public Trust: Enhance
s public confidence in AI by ensuring transparency and accountability in the development process.

**Cons:**

* Innovati
on Stagnation: Critics argue it might stifle innovation, especially in open-source AI, due to the high costs and regulat
ory burdens of compliance.
* Ambiguity: Some definitions and requirements might be too specific or broad, leading to leg
al challenges or unintended consequences.
* Global Competitiveness: There’s concern that such regulations could push AI 
development outside California or the U.S., benefiting other nations without similar restrictions.
* Implementation Chal
lenges: The practicalities of enforcing such regulations, especially the “positive safety determination,” could be compl
ex and contentious.

**News Article:** [**Click here**](https://www.thenation.com/article/society/sb-1047-ai-big-tech-fi
ght/)

**Open Letter:** [**Click here**](https://safesecureai.org/open-letter)

https://preview.redd.it/ib96d7nk4cmd1.pn
g?width=828&format=png&auto=webp&s=0ed5913b5dae72e203c8592393e469d9130ed689

# MORE OpenAI drama

OpenAI co-founder John
 Schulman has left the company to join rival AI startup Anthropic, while OpenAI president and co-founder Greg Brockman i
s taking an extended leave until the end of the year. Schulman, who played a key role in creating the AI-powered chatbot
 platform ChatGPT and led OpenAI’s alignment science efforts, stated his move was driven by a desire to focus more on AI
 alignment and hands-on technical work. Peter Deng, a product manager who joined OpenAI last year, has also left the com
pany. With these departures, only three of OpenAI’s original 11 founders remain: CEO Sam Altman, Brockman, and Wojciech 
Zaremba, lead of language and code generation.

**News Article:** [**Click here**](https://techcrunch.com/2024/08/05/ope
nai-co-founder-leaves-for-anthropic/)

https://preview.redd.it/0vdjc18j4cmd1.png?width=828&format=png&auto=webp&s=e9de60
4c26aed3e47b50df3bdf114ef61f967080

# Apple and Nvidia may invest in OpenAI

Apple, which is planning to integrate ChatG
PT into iOS, is in talks to invest. Soon after, [*Bloomberg* also](https://www.bloomberg.com/news/articles/2024-08-29/nv
idia-has-held-discussions-about-joining-openai-s-funding-round?srnd=homepage-americas) reported that Apple is in talks b
ut added that Nvidia “has discussed” joining the funding round as well. The round is reportedly being led by Thrive Capi
tal and would value OpenAI at more than $100 billion.

**News Article:** [**Click here**](https://www.theverge.com/2024/
8/29/24231626/apple-nvidia-openai-invest-microsoft)

https://preview.redd.it/ude6jguh4cmd1.png?width=828&format=png&auto
=webp&s=3603cbca0dbb1be3e6d0efcf06c3a698428bbdd6

# Editor’s Special

* The AI Bubble: Will It Burst, and What Comes Aft
er?: [**Click here**](https://www.youtube.com/watch?v=91SK90SahHc&t=317s)
* Eric Schmidt Full Controversial Interview on
 AI Revolution (Former Google CEO): [**Click here**](https://www.youtube.com/watch?v=mKVFNg3DEng)
* AI isn’t gonna keep 
improving [**Click here**](https://www.youtube.com/watch?v=Y8Ym7hMR100)
* General Intelligence: Define it, measure it, b
uild it: [**Click here**](https://www.youtube.com/watch?v=nL9jEy99Nh0)
```
---

     
