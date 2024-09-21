 
all -  [ RAG using JSON file with nested referencing or chained referencing ](https://www.reddit.com/r/LangChain/comments/1flmupc/rag_using_json_file_with_nested_referencing_or/) , 2024-09-21-0912
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

     
 
all -  [ RAG using JSON file with nested referencing or chained referencing ](https://www.reddit.com/r/Rag/comments/1flmtri/rag_using_json_file_with_nested_referencing_or/) , 2024-09-21-0912
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

     
 
all -  [ Resolution of Lanchain critical vulnerability ](https://www.reddit.com/r/LangChain/comments/1flkmok/resolution_of_lanchain_critical_vulnerability/) , 2024-09-21-0912
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

     
 
all -  [ A new chunking algorithm proposal - Semantically chunking based on sliding token windows and similar ](https://www.reddit.com/r/LangChain/comments/1flhtxi/a_new_chunking_algorithm_proposal_semantically/) , 2024-09-21-0912
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

     
 
all -  [ Filtering nested json response ](https://www.reddit.com/r/LangChain/comments/1flefus/filtering_nested_json_response/) , 2024-09-21-0912
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

     
 
all -  [ Please give feedback, been looking for summer 2025 internships ](https://i.redd.it/0g8hwhhnpnpd1.jpeg) , 2024-09-21-0912
```

```
---

     
 
all -  [ LlamaIndex vs LangChain vs Pathway vs Others (2024 Guide to Top RAG Frameworks) ](https://www.reddit.com/r/LlamaIndex/comments/1fld7nw/llamaindex_vs_langchain_vs_pathway_vs_others_2024/) , 2024-09-21-0912
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

     
 
all -  [ Comparison between the Top RAG Frameworks (2024) ](https://www.reddit.com/r/LangChain/comments/1fld63q/comparison_between_the_top_rag_frameworks_2024/) , 2024-09-21-0912
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

     
 
all -  [ Langgraph Studio does not capture code changes ](https://www.reddit.com/r/LangChain/comments/1fla0ac/langgraph_studio_does_not_capture_code_changes/) , 2024-09-21-0912
```
I like the idea of langgraph studio, but it looks like it does not capture code changes, which make it quite useless.

B
ecause a very good use would be to be able to fork a call and see how the output changes when changing prompt or tool lo
gics.

Am i missing something?
```
---

     
 
all -  [ Are ollama and gpt agents different in how they work? ](https://www.reddit.com/r/LangChain/comments/1fl9z2t/are_ollama_and_gpt_agents_different_in_how_they/) , 2024-09-21-0912
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

     
 
all -  [ Hi does anyone have idea how can we consider accuracy of our chatbot? ](https://www.reddit.com/r/LangChain/comments/1fl8dir/hi_does_anyone_have_idea_how_can_we_consider/) , 2024-09-21-0912
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

     
 
all -  [ Is someone interested to join with me for learning #LLM #GenAI together??  ](https://www.reddit.com/r/LangChain/comments/1fl748j/is_someone_interested_to_join_with_me_for/) , 2024-09-21-0912
```

Is someone interested to join with me for learning #LLM #GenAI together?? 

I have basic idea of LLM and did some hands
 on too. But planning to understand the working behind in detail. So if anyone intrested then please DM me. Planning to 
start from tomorrow.

```
---

     
 
all -  [ SurfSense - Personal AI Assistant for World Wide Web Surfers. ](https://www.reddit.com/r/LangChain/comments/1fl5axm/surfsense_personal_ai_assistant_for_world_wide/) , 2024-09-21-0912
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

     
 
all -  [ Looking for recommendations to build a search application ](https://www.reddit.com/r/LangChain/comments/1fkzfu5/looking_for_recommendations_to_build_a_search/) , 2024-09-21-0912
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

     
 
all -  [ [P] Swapping Embedding Models for an LLM ](https://www.reddit.com/r/MachineLearning/comments/1fktvbj/p_swapping_embedding_models_for_an_llm/) , 2024-09-21-0912
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

     
 
all -  [ Need Help with Langchain for Feeding Gemini LLM Direct PDFs in Base64 Format ](https://www.reddit.com/r/LangChain/comments/1fksrqc/need_help_with_langchain_for_feeding_gemini_llm/) , 2024-09-21-0912
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

     
 
all -  [ LangGraph allows you to make falsifiable, testable agents that are actually useful. ](https://www.reddit.com/r/datascience/comments/1fknbyi/langgraph_allows_you_to_make_falsifiable_testable/) , 2024-09-21-0912
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

     
 
all -  [ all up-to-date knowledge + code on Agents and RAG in one place! ](https://diamantai.substack.com/) , 2024-09-21-0912
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

     
 
all -  [ Do Podcast with Albert Einstein!! ](https://www.reddit.com/r/SideProject/comments/1fkkc4c/do_podcast_with_albert_einstein/) , 2024-09-21-0912
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

     
 
all -  [ Need help with using RAG, I need to know if this idea is plausible ](https://www.reddit.com/r/LangChain/comments/1fkkbsx/need_help_with_using_rag_i_need_to_know_if_this/) , 2024-09-21-0912
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

     
 
all -  [ I made this whole SaaS in just 4 days! ](https://www.reddit.com/r/SaaS/comments/1fkk92u/i_made_this_whole_saas_in_just_4_days/) , 2024-09-21-0912
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

     
 
all -  [ Seeking advice: AI-powered summaries for MS Teams and Email to feed our knowledge base ](https://www.reddit.com/r/LangChain/comments/1fkjr7e/seeking_advice_aipowered_summaries_for_ms_teams/) , 2024-09-21-0912
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

     
 
all -  [ LangChain Invoke Error ](https://www.reddit.com/r/LangChain/comments/1fkjirr/langchain_invoke_error/) , 2024-09-21-0912
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

     
 
all -  [ Improving RAG Application: Chunking, Reranking, and Lambda Cold-Start Issues ](https://www.reddit.com/r/aws/comments/1fkhbmv/improving_rag_application_chunking_reranking_and/) , 2024-09-21-0912
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

     
 
all -  [ What's the Type / Shape of the data for Checkpointers / Custom MemorySaver in LangGraph JS? ](https://www.reddit.com/r/LangChain/comments/1fkhbbr/whats_the_type_shape_of_the_data_for/) , 2024-09-21-0912
```
I need to create a custom MemorySaver for the database I'm using and I'm wondering what the schema is of the Records to 
be stored in the Database. 

Is there an explanation of exactly this? Is it a Checkpoint? Is it a Thread? Is a Thread pa
rt of a Checkpoint? It'd be great to know what parts are put together to make up the 'stuff'. 

I've looked at the Metho
ds in MemorySaver so I think I can see some of it, but is there a clear definition of it somewhere??
```
---

     
 
all -  [ I have been trying to get Chatgroq to work for tool calling using the llama3-8b-8192 model. For some ](https://www.reddit.com/r/LangChain/comments/1fkf9fc/i_have_been_trying_to_get_chatgroq_to_work_for/) , 2024-09-21-0912
```
Here's a link to my script: [https://pastebin.com/p2qjz3k2](https://pastebin.com/p2qjz3k2)
```
---

     
 
all -  [ Guardrails on LangGraph ](https://www.reddit.com/r/LangChain/comments/1fkev19/guardrails_on_langgraph/) , 2024-09-21-0912
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

     
 
all -  [ Building RAG with Postgres ](https://www.reddit.com/r/Rag/comments/1fkdtmg/building_rag_with_postgres/) , 2024-09-21-0912
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

     
 
all -  [ Output based on the tool used ](https://www.reddit.com/r/LangChain/comments/1fkdq0v/output_based_on_the_tool_used/) , 2024-09-21-0912
```
So I am working with an agent who has access to N tools. Based on the user prompt the agent can access any tool and resp
ond back. 

Before sending the response back to the user I want to format it for a ui framework I am using based on whic
h tool is returning the final output. 
I don't want the tools directly to return this output as it might confuse the age
nt. 
```
---

     
 
all -  [ Multimodal_RAG ](https://www.reddit.com/r/Rag/comments/1fkdhhr/multimodal_rag/) , 2024-09-21-0912
```
Hello everyone, I am new to reddit and Gen AI field as well...While there are already some really awesome templates/Full
 stack solutions out there, its just too much information to follow for someone like me so i created one myself. Do chec
k it out [here](https://github.com/sallu-786/Multimodal_RAG) . Suggestions/contributions are more than welcome

[Made us
ing Streamlit+Langchain+OpenAI\/Ollama](https://reddit.com/link/1fkdhhr/video/47pggx3lbppd1/player)
```
---

     
 
all -  [ Help Needed with Calculating Pricing for Processing Documents with Langchain #26640
 ](https://www.reddit.com/r/LangChain/comments/1fk91la/help_needed_with_calculating_pricing_for/) , 2024-09-21-0912
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

     
 
all -  [ System requirements for Bge-reranker-base  ](https://www.reddit.com/r/huggingface/comments/1fk8tvb/system_requirements_for_bgererankerbase/) , 2024-09-21-0912
```
Hi all. Just a junior dev. I wanted to use Bge-reranker-base as my reranking model. I wanted to know what's the system r
equirements. I searched the internet, but wasn't able to find. I wanted to know how much CPU and RAM will be used for CP
U only reranking, and GPU and RAM for GPU based reranking. The framework I use is langchain.
```
---

     
 
all -  [ Has anyone ever got `ChatHuggingFace` to work? ](https://www.reddit.com/r/huggingface/comments/1fk8er9/has_anyone_ever_got_chathuggingface_to_work/) , 2024-09-21-0912
```
This is more of a \*little\* bit of a frustration post than a question, but I've been at it for days trying to get stuff
 to work with the langchain x huggingface integration. The examples on both websites don't work (and just demonstrate op
enai examples), and the github issues where everyone is having the same problems seem unresolved? Any thoughts or contex
t? 😢
```
---

     
 
all -  [ [Student] 0 YoE CS grad student looking for entry roles in Machine Learning/Data Science roles - loo ](https://www.reddit.com/r/EngineeringResumes/comments/1fk5ojt/student_0_yoe_cs_grad_student_looking_for_entry/) , 2024-09-21-0912
```
Hi all, I'm a CS grad looking to apply to entry-level Data Scientist or Machine Learning Engineer roles. I'm hoping to r
eceive some honest feedback so that I can make the necessary tweaks before I apply more. I have already applied to 100 j
obs over the past week and have been cold messaging employees on LinkedIn for referrals but received no response yet.

I
've tried to include projects that are business-focused and I have also incorporated metrics and keywords to showcase bu
siness impact. How else can I improve?

https://preview.redd.it/j53y8v3janpd1.png?width=4967&format=png&auto=webp&s=e446
63fb3d326e61bc06a5df53225b1731a3918f

  

```
---

     
 
all -  [ Emulate OpenAI API ](https://www.reddit.com/r/OpenWebUI/comments/1fk37bc/emulate_openai_api/) , 2024-09-21-0912
```
Is it possible?

I know Oobabooga does that. wonder if I can use langchain with OpenWebUI while using OpenAI api emulate
d on it.
```
---

     
 
all -  [ Build neo4j graph ](https://www.reddit.com/r/LangChain/comments/1fk2chx/build_neo4j_graph/) , 2024-09-21-0912
```
I want to build a neo4j graph from a batch of http requests.
I only want to have a relationship to know if a pair (reque
st, response) is connected with a other (request, response)
```
---

     
 
all -  [ The Agentic Patterns makes working auth agents so much better. ](https://www.reddit.com/r/AutoGenAI/comments/1fk0vnu/the_agentic_patterns_makes_working_auth_agents_so/) , 2024-09-21-0912
```
These Agentic Design Patterns helped me out a lot when building with AutoGen+Llama3!

I mostly use open source models (L
lama3 8B and Qwen1.5 32B Chat). Getting these open source models to work reliably has always been a challenge. That's wh
en my research led me to AutoGen and the concept of AI Agents.

Having used them for a while, there are some patterns wh
ich have been helping me out a lot. Wanted to share it with you guys,

# My Learnings

i. You solve the problem of indet
erminism with conversations and not via prompt engineering.

Prompt engineering is important. I'm not trying to dismiss 
it. But its hard to make the same prompt work for the different kinds of inputs your app needs to deal with.

A better a
pproach has been adopting the two agent pattern. Here, instead of taking an agent's response and forwarding it to the us
er (or the next agent) we let it talk to a companion agent first. We then let these agent talk with each other (1 to 3 t
urns depending on how complex the task was) to help 'align' the answer with the 'desired' answer.

Example: Lets say you
 are replacing a UI form with a chatbot. You may have an agent to handle the conversation with the user. But instead of 
it figuring out the JSON parameters to fill up the form, you can have a companion agent do that. The companion agent wou
ldn't really be following the entire conversation (just the deltas) and will keep a track of what fields are answered an
d what isn't. It can tell the chat agent what questions needs to be asked next.

This helps the chat agent focus on the 
'conversation' aspect (Dealing with prompt injection, politeness, preventing the chat from getting derailed) while the c
ompanion agent can take care of managing form data (JSON extraction, validation and so on).

Another example could be sp
litting a JSON formatter into 3 parts (An agent to spit out data in a semi structured format like markdown - Another one
 to convert that to JSON - The last one to validate the JSON). This is more of a sequential chat pattern but the last tw
o could and probably should be modelled as two-companion agents.

ii. LLMs are not awful judges. They are often good eno
ugh for things like RAG.

An extension of the two agent pattern is called 'Reflection.' Here we let the companion agent 
verify the primary agent's work and provide feedback for improvement.

Example: Let's say you got an agent that does RAG
. You can have the companion do a groundedness check to make sure that the text generation is in line with the retrieved
 chunks. If things are amiss, the companion can provide an additional prompt to the RAG agent to apply corrective measur
es and even mark certain chunks as irrelevant. You could also do a lot more checks like profanity check, relevance check
 (this can be hard) and so on. Not too bad if you ask me.

iii. Agents are just a function. They don't need to use LLMs.


I visualize agents as functions which take a conversational state (like an array of messages) as an input and return a
 message (or modified conversational state) as an output. Essentially they are just participants in a conversation.

Wha
t you do inside the function is upto you. Call an LLM, do RAG or whatever. But you could also just do basic clasificatio
n using a more traditional approach. But it doesn't need to be AI driven at all. If you know the previous agent will out
put JSON, you can have a simple JSON schema validator and call it a day. I think this is super powerful.

iv. Agents are
 composable.

Agents are meant to be composable. Like React's UI components.

So I end up using agents for simple prompt
 chaining solutions (which may be better done by raw dawging shit or using Langchain if you swing that way) as well. Thi
s lets me morph underperforming agents (or steps) with powerful patterns without having to rewire the entire chain. Pret
ty dope if you ask me.

## Conclusion

I hope I am able to communicate my learning wells. Do let me know if you have any
 questions or disagree with any of my points. I'm here to learn.

P.S. - Sharing a YouTube video I made on this topic wh
ere I dive a bit deeper into these examples! Would love for you to check that out as well. Feel free to roast me for my 
stupid jokes! Lol!

https://youtu.be/PKo761-MKM4
```
---

     
 
all -  [ What are you all building?  ](https://www.reddit.com/r/LangChain/comments/1fjzpej/what_are_you_all_building/) , 2024-09-21-0912
```
Just wanted to hear what you all are building and if you are using Langchain, how has your experience been so far. 
```
---

     
 
all -  [ Instructor output parser with LLM conversation memory chain ](https://www.reddit.com/r/LangChain/comments/1fjz4tg/instructor_output_parser_with_llm_conversation/) , 2024-09-21-0912
```
Can anyone help on how to integrate instructor parser with conversational chatbot, so it can collect the required field 
that I need from user queries ; ask relevant question if information is missing and stores and update the infos? And, la
stly shows the overallparsings result to user and ask for conformation?  Any guideline on how to implement it would be h
elpful! 
I am using openai model
```
---

     
 
all -  [ What do I build my agent's frontend on if i am using LangGraph? (Apart from streamlit) ](https://www.reddit.com/r/LangChain/comments/1fjyt7a/what_do_i_build_my_agents_frontend_on_if_i_am/) , 2024-09-21-0912
```
I am trying to make a production grade agent (planning on rolling it out as a web app) and I was wondering for my fronte
nd what should I use if I am using Langgraph to build my Ai agent? Should use React? or Next? or is there anything else 
more prod grade?  
Thanks.
```
---

     
 
all -  [ Is there any good chat with Langchain documentation sites around? ](https://www.reddit.com/r/LangChain/comments/1fjx5b9/is_there_any_good_chat_with_langchain/) , 2024-09-21-0912
```
I used to use the chatgpt custom gpt features to chat with langchain documentation on an app I'm building, I feel like a
ll of them are slightly out of date as I'm prone to getting errors. 

The AI chat on the langchain site is really limite
d so I can't use that, so I'm wondering if there is anything else people are using for workloads


```
---

     
 
all -  [ These Agentic Design Patterns helped me out a lot when building with AutoGen+Llama3! ](https://www.reddit.com/r/LocalLLaMA/comments/1fjwtv2/these_agentic_design_patterns_helped_me_out_a_lot/) , 2024-09-21-0912
```
I mostly use open source models (Llama3 8B and Qwen1.5 32B Chat). Getting these open source models to work reliably has 
always been a challenge. That's when my research led me to AutoGen and the concept of AI Agents.

Having used them for a
 while, there are some patterns which have been helping me out a lot. Wanted to share it with you guys,

# My Learnings


i. You solve the problem of indeterminism with conversations and not via prompt engineering.

Prompt engineering is imp
ortant. I'm not trying to dismiss it. But its hard to make the same prompt work for the different kinds of inputs your a
pp needs to deal with.

A better approach has been adopting the two agent pattern. Here, instead of taking an agent's re
sponse and forwarding it to the user (or the next agent) we let it talk to a companion agent first. We then let these ag
ent talk with each other (1 to 3 turns depending on how complex the task was) to help 'align' the answer with the 'desir
ed' answer.

Example: Lets say you are replacing a UI form with a chatbot. You may have an agent to handle the conversat
ion with the user. But instead of it figuring out the JSON parameters to fill up the form, you can have a companion agen
t do that. The companion agent wouldn't really be following the entire conversation (just the deltas) and will keep a tr
ack of what fields are answered and what isn't. It can tell the chat agent what questions needs to be asked next.

This 
helps the chat agent focus on the 'conversation' aspect (Dealing with prompt injection, politeness, preventing the chat 
from getting derailed) while the companion agent can take care of managing form data (JSON extraction, validation and so
 on).

Another example could be splitting a JSON formatter into 3 parts (An agent to spit out data in a semi structured 
format like markdown - Another one to convert that to JSON - The last one to validate the JSON). This is more of a seque
ntial chat pattern but the last two could and probably should be modelled as two-companion agents.

ii. LLMs are not awf
ul judges. They are often good enough for things like RAG.

An extension of the two agent pattern is called 'Reflection.
' Here we let the companion agent verify the primary agent's work and provide feedback for improvement.

Example: Let's 
say you got an agent that does RAG. You can have the companion do a groundedness check to make sure that the text genera
tion is in line with the retrieved chunks. If things are amiss, the companion can provide an additional prompt to the RA
G agent to apply corrective measures and even mark certain chunks as irrelevant. You could also do a lot more checks lik
e profanity check, relevance check (this can be hard) and so on. Not too bad if you ask me.

iii. Agents are just a func
tion. They don't need to use LLMs.

I visualize agents as functions which take a conversational state (like an array of 
messages) as an input and return a message (or modified conversational state) as an output. Essentially they are just pa
rticipants in a conversation.

What you do inside the function is upto you. Call an LLM, do RAG or whatever. But you cou
ld also just do basic clasification using a more traditional approach. But it doesn't need to be AI driven at all. If yo
u know the previous agent will output JSON, you can have a simple JSON schema validator and call it a day. I think this 
is super powerful.

iv. Agents are composable.

Agents are meant to be composable. Like React's UI components.

So I end
 up using agents for simple prompt chaining solutions (which may be better done by raw dawging shit or using Langchain i
f you swing that way) as well. This lets me morph underperforming agents (or steps) with powerful patterns without havin
g to rewire the entire chain. Pretty dope if you ask me.

## Conclusion

I hope I am able to communicate my learning wel
ls. Do let me know if you have any questions or disagree with any of my points. I'm here to learn.

P.S. - Sharing a You
Tube video I made on this topic where I dive a bit deeper into these examples! Would love for you to check that out as w
ell. Feel free to roast me for my stupid jokes! Lol!
```
---

     
 
all -  [ Struggling to get interviews for ML engineer roles please let me know what the issue is with my resu ](https://www.reddit.com/r/Resume/comments/1fjvq7l/struggling_to_get_interviews_for_ml_engineer/) , 2024-09-21-0912
```
https://preview.redd.it/cjj6vh607lpd1.png?width=5100&format=png&auto=webp&s=8d9f2cc771a8f2a333cca4e70aeca960b617d1bf


```
---

     
 
MachineLearning -  [ [P] Review and suggest ideas for my chatbot ](https://www.reddit.com/r/MachineLearning/comments/1fb2mwl/p_review_and_suggest_ideas_for_my_chatbot/) , 2024-09-21-0912
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

     
 
MachineLearning -  [ [P] Lessons from Retrieval Augmented Generation ](https://www.reddit.com/r/MachineLearning/comments/1f9tvg7/p_lessons_from_retrieval_augmented_generation/) , 2024-09-21-0912
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

     
 
deeplearning -  [ What is the best approach for Parsing and Retrieving Code Context Across Multiple Files in a Hierarc ](https://www.reddit.com/r/deeplearning/comments/1fh58oz/what_is_the_best_approach_for_parsing_and/) , 2024-09-21-0912
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

     
 
deeplearning -  [ Month of August in AI ](https://www.reddit.com/r/deeplearning/comments/1f6zfz0/month_of_august_in_ai/) , 2024-09-21-0912
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

     
 
deeplearning -  [ Creating a project on NLP ](https://www.reddit.com/r/deeplearning/comments/1ey2e85/creating_a_project_on_nlp/) , 2024-09-21-0912
```
So me and my friend completed the ML and DL specialization by AndrewNg, and were just gonna get started on a project. We
 decided to make a academic assistant. So basically what this does is a user can upload a PDF,text file or any other sup
ported media and the can ask questions related to it's contents. The main objective being making learning quick given la
rger documents.

The pipeline we decided is pretty standard for such a project.

1. Split the text into chunks
2. Genera
te embeddings of the chunks
3. Store the chunks in a vector DB
4. Find the top K similar chunks to the query 
5. Retriev
e context and feed it into a LLM for an answer.

So I looked up for a library and framework to use and decided on langch
ain. We haven't decided on an LLM yet but want to run it locally so no OpenAI please. 

Since this is gonna be out first
 AI project confidence is low. I would really appreciate any heads up on the issues we may face, any suggestions on libr
aries,frameworks or models will be really helpful as well. 

Appreciate any resourceful comment 😊
```
---

     
