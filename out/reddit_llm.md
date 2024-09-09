 
all -  [ Detect relation between requests ](https://www.reddit.com/r/LangChain/comments/1fc547s/detect_relation_between_requests/) , 2024-09-09-0912
```
I have a batch of requests (100 for example) and i want to find which requests are related. I was wondering to know if i
t is viable to build an agent/chain to find a sequence of requests that are related and in a second step analyze if this
 sequence is a vulnerability.

Maybe only 3 three requests of this 100 can be connected to build a vulnerability.


Than
ks
```
---

     
 
all -  [ Evaluate FAISS Vector Database for RAG ](https://www.reddit.com/r/LangChain/comments/1fc4347/evaluate_faiss_vector_database_for_rag/) , 2024-09-09-0912
```
While creating an RAG FAQ chatbot using LangChain and FAISS, I made the vector database using FAISS and about 80 pairs F
AQs and their answers. Now, I want to check if the vector database performs well at retrieving proper context given a qu
ery. How should I proceed? Are there any frameworks that can help?
```
---

     
 
all -  [ How to Maintain Context in LLM Content Generation? ](https://www.reddit.com/r/LangChain/comments/1fc3emy/how_to_maintain_context_in_llm_content_generation/) , 2024-09-09-0912
```
Hi everyone,

I'm working on generating website content using an LLM, but as many of you may know, generating content in
 one go doesn’t always yield stable results. Instead, breaking the task into smaller chunks often works better. However,
 this approach tends to create semantic gaps between different parts of the content, which lowers its overall quality.


I was thinking of using Langchain and ChromaDB to store previously generated sections and remind the LLM of these parts 
when generating new sections. For example, I could start by asking the LLM to generate two introductory paragraphs. Then
, I would remind the LLM of these paragraphs when asking it to generate the development section. This way, it can produc
e more relevant and cohesive results that stay aligned with the introduction.

What would be the most efficient way to a
chieve this? Should I focus on prompt engineering (e.g., inserting previous sections directly into the prompt template)?
 Or would a solution like ChromaDB be better suited for this scenario?

Would love to hear your thoughts and suggestions
!
```
---

     
 
all -  [ Multi-Agent System (Chatbot) with LangGraph and External Tools ](https://www.reddit.com/r/LangChain/comments/1fc2fqp/multiagent_system_chatbot_with_langgraph_and/) , 2024-09-09-0912
```
Hey All,

I'm excited to share my project: a multi-agent chatbot leveraging LangGraph and external tools like Wikipedia,
 Arxiv, and more! The goal is to create a conversational AI that combines the strengths of LLMs and specialized knowledg
e sources.

**Here's the challenge:** 

When a user asks a question, the system generates multiple answers from differen
t sources (LLM and external tools). I want to display the most relevant answer, hiding unnecessary responses.

**Example
:**

User query: 'Hi, How are you?'  
Relevant answer: LLM's response (not Wikipedia's)

To achieve this, I'm considerin
g implementing semantic similarity between the user's query and the generated answers. But is this the most efficient ap
proach?

**Questions:**

1. Does LangChain or LangGraph provide built-in functionality for relevance ranking or filterin
g?
2. Are there alternative methods to semantic similarity for determining relevance?
3. What are some potential pitfall
s or considerations when integrating multiple knowledge sources?

**Technical Details:**

* LangGraph for graph-based co
nversational AI
* External tools: Wikipedia, Arxiv, and potentially more
* LLM: Any model via ChatGroq

If you're experi
enced with chatbot development, NLP, or knowledge graph architectures, I'd love your input!

Share your thoughts, sugges
tions, and expertise!
```
---

     
 
all -  [ [D] Help with RAG App with 100+ docs ](https://www.reddit.com/r/Rag/comments/1fc1n58/d_help_with_rag_app_with_100_docs/) , 2024-09-09-0912
```
I am working on retrieval augmented generation app. I have many documents inside directories and subdirectories. The doc
uments add up to something like 5GB. Types of documents I need to retrieve from are pdf, xlsx, docx and mpp...

I used l
angchain to create the normal flow, a vector store and an ensemble retriever. I have also heard of knowledge graphs and 
that they may be a better alternative to vector stores (gotta do some research). All of this experimenting was local. Th
e problem is when I tested it, even after around 4 hours the embedding process was not finished so I kind of gave up...


Some guidance/pointers would be amazing
```
---

     
 
all -  [ Stop trying to parse your documents and use ColPali (Open Source) ](https://www.reddit.com/r/LangChain/comments/1fc15wg/stop_trying_to_parse_your_documents_and_use/) , 2024-09-09-0912
```
I've been building RAGs for enterprises (banks, hospitals, lawyers) for the past \~2 years, and have been talking to som
e members of our community and it seems everybody has the same problem when building RAGs: **How the hell do we parse ou
r data correctly?**

I feel this paint everyday at my job. Reality is that real world data is super messy, real document
s are filled with graphs, tables, diagrams, and even ones that are pure text like legal documents have specific formatti
ng that makes it really hard to extract text correctly using OCR, Unstructured, etc. I have even tried most private data
 extraction solutions like Azure Document Intelligence, GCP Document AI, IBM WatsonX Discovery, and they weren't good en
ough.

Ironically a good example of this is the transformers paper, here are some images from it:

https://preview.redd.
it/j345liy5qlnd1.png?width=322&format=png&auto=webp&s=869e05cd23bb0e1ff15d16db0c8fd29044733501

https://preview.redd.it/
xnii8td6qlnd1.png?width=511&format=png&auto=webp&s=50d4bddbc87db11fc5e9f4bd5e1728cd2717f37a

https://preview.redd.it/g4m
l18h9qlnd1.png?width=503&format=png&auto=webp&s=592931b1858c26ff04a87fbf847dd40b30ca5e93

No tool I've tried I has been 
parse to parse this information into text correctly. And this is just one average document. I have clients with thousand
 of documents filled with tables and pictures like these. In the end a lot of these cases needed to involve manual label
ing or extraction which is just not scalable. But why are real documents so convoluted?

Because humans are visual. One 
picture is worth a thousand words. By trying to turn our documents into text we lose so much information it crazy, but t
here is an answer:

**Instead of trying to transform human documents into something LLMs understand, we should make LLMs
 understand documents the way humans do.**

All the new models (gpt4o, gemini, claude) are now multimodal, so they have 
the ability to see these pages like we do, and they are actually really great at interpreting them. The problem for RAG 
was that we need to search the right pages to show the model for a specific question, which was difficult... until ColPa
li was released.

**ColPali** is an embedding model trained on documents pages, so you give it an image of a page and it
 gives you an embedding you can store in a vector db related to that page. On top of that, it generates ColBERT embeddin
gs which contain much more detail that vector embeddings.

While it's still an *very* new idea I have been excited to tr
y it out with my projects. So I built [Midras](https://github.com/ajac-zero/midrasai), an Open Source python library tha
t let's you set up ColPali in your own applications, completely free locally or using cloud GPUs with my micro-saas API.
 Using Midras you are able to ingest a pdf file directly and query it, without any preprocessing! You can check out an e
xample notebook of RAG with ColPali and Gemini Flash [here](https://github.com/ajac-zero/midrasai/blob/main/examples/vec
tor_search/vector_search.ipynb).

It's still early days for this new way of visual RAG, so there will be many problems t
o solve along the way. However I think it's the right path for the future of RAG. I intend to use this method for my own
 enterprise projects, so my aim is to make Midras as production ready as possible, while still keeping it open source an
d flexible so you can adapt it to your specific needs.

If you're interested, please give it a star! If you want a speci
fic feature (like support for a specific vector database) please submit an issue!

I also want to learn about more real 
use cases for RAG, so if you have or are working on one, my DMs are open and I would love to talk. Let's push RAG forwar
d together!
```
---

     
 
all -  [ [Help] Tool Calling with Gemini 1.5 Flash - Issues with Complex Agent for Academic Profiles ](https://www.reddit.com/r/LangChain/comments/1fc0f10/help_tool_calling_with_gemini_15_flash_issues/) , 2024-09-09-0912
```
Hey everyone,

I'm working on building a complex agent using LangChain, aiming to fetch student data from a database and
 create their academic profiles. I was able to get this working using OpenAI’s GPT-4 (via the `create_openai_tools_agent
`), but I’ve been running into some issues when switching to Gemini 1.5 Flash and experimenting with tool calling agents
.

# What I’ve Done So Far:

* I successfully set up the agent with GPT-4, where it first retrieves the student data and
 then constructs an academic profile from it.
* Now, I’m trying to replicate this setup using the Gemini 1.5 Flash model
 with tool calling, but I'm encountering a couple of challenges.

# The Issues:

1. **Tool Order Not Respected:** Despit
e specifying in the tool description that the agent should first fetch the data and then create the profile, it skips di
rectly to the profile creation step. This seems to happen regardless of how I phrase the tool instructions.
2. **Errors 
with Complex Queries:** For more complex tasks, like fetching data for two students and comparing their profiles, the ag
ent throws a `400 error`. Here’s a snippet of the error I’m getting:google.api\_core.exceptions.InvalidArgument: 400 \* 
GenerateContentRequest.contents\[3\].parts\[0\].function\_response.name: Name cannot be empty.

This happens when I atte
mpt to retrieve the data for two students (e.g., `Ana` and `Bianca`) and compare their profiles.

# What’s Next?

After 
sorting this out, I’d like to test the agent with other models like LLaMA and Mistral, but first, I need to figure out t
he tool-calling order and the error with more complex queries.

Has anyone faced similar issues with Gemini 1.5 Flash or
 have any tips on how to resolve this? Any insights on how to better handle tool calling in LangChain or best practices 
for agent workflows would be super helpful!

Thanks in advance!This happens when I attempt to retrieve the data for two 
students (e.g., Ana and Bianca) and compare their profiles.What’s Next?After sorting this out, I’d like to test the agen
t with other models like LLaMA and Mistral, but first, I need to figure out the tool-calling order and the error with mo
re complex queries.Has anyone faced similar issues with Gemini 1.5 Flash or have any tips on how to resolve this? Any in
sights on how to better handle tool calling in LangChain or best practices for agent workflows would be super helpful!Th
anks in advance!
```
---

     
 
all -  [ New tutorials in our comprehensive RAG open-source educational repo! ](https://github.com/NirDiamant/RAG_Techniques) , 2024-09-09-0912
```
✨ Community exploded to 515 members within 2 weeks

🛠️ 6 game-changing features added:

* Reliable RAG - verify your RAG
 answers and visualize the sources of the answers
* Propositions Chunking
* CSV Integration
* Document Augmentation usin
g questions about them for better retrieval 
* Microsoft graph RAG implementation 
* Ready-to-Run Scripts

💡 All communi
ty-driven, all open source!
Join us in shaping the future of RAG. Link to Discord at the beginning of the repo! 🤝🔥
```
---

     
 
all -  [ Need Help Setting Up a Chatbot with LangChain: SelfRAG, GraphRAG, and LangGraph ](https://www.reddit.com/r/Langchaindev/comments/1fbwafg/need_help_setting_up_a_chatbot_with_langchain/) , 2024-09-09-0912
```
Hey everyone,



I'm working on building a chatbot using LangChain and could really use some help with configuring a few
 specific components. My goal is to enhance the chatbot's ability to retrieve relevant information and answer complex qu
estions more effectively. Here's what I'm trying to set up:



1. \*\*SelfRAG:\*\* To improve the system's autonomy in r
etrieving relevant information and generating responses.

   

2. \*\*GraphRAG:\*\* To integrate retrieval with knowledg
e graphs, enhancing the ability to answer complex questions.



3. \*\*LangGraph:\*\* To create and manage knowledge gra
phs that represent relationships between concepts in the loaded documents.



I'm relatively new to these components, an
d any guidance on how to set them up or best practices for using them would be greatly appreciated. Whether it's documen
tation, tutorials, code examples, or just some tips from your experience, I'd love to hear from you!



Thanks in advanc
e for your help!
```
---

     
 
all -  [ Flowise Multilingual - Answer in the same language than the user's {question} ](https://www.reddit.com/r/flowise/comments/1fbvicg/flowise_multilingual_answer_in_the_same_language/) , 2024-09-09-0912
```
https://preview.redd.it/xdnkao9gjknd1.png?width=881&format=png&auto=webp&s=876d10e286107ba7154373a4bf2602b2fde7baa3

Hey
, I'm trying to make a chain with the second output being the translated version of the first output.  
If I want to tra
nslate into one specific language, I have no problem - ex: Translate the {question} in spanish = it works.  
But I would
 like it to translate the first output in the same language than the {question} is formulated - ex: Translate the {llmCh
ain\_0.data.instance} in the same language the {question} is formulated = it fails.  
It would allow me to get second ou
tputs in any language, swedish, chinese, hindi, french,...  
I've tried several different prompts, it sometimes worked, 
but not on a regular basis.

Does someones has a possible solution for that?


```
---

     
 
all -  [ Where am I going wrong? ITS BEEN 2 WEEKS WITH THIS ERROR  ](https://www.reddit.com/r/LangChain/comments/1fbv4kj/where_am_i_going_wrong_its_been_2_weeks_with_this/) , 2024-09-09-0912
```
I have set up a **Flask web application** with two routes (`/upload` and `/query`).

1. I have integrated **Qdrant** for
 storing and searching document embeddings.
2. I have configured **PyPDFLoader** to extract text from uploaded PDF files
.
3. I have implemented a function to **chunk large documents** using LangChain’s `RecursiveCharacterTextSplitter`.
4. I
 have embedded document text using **Jina’s CLIP embedding API**.
5. I have **stored document embeddings** in Qdrant usi
ng the `upsert` method.
6. I have processed **user queries**, embedded them, and searched for similar document chunks in
 Qdrant.
7. I have used **ChatGroq LLM** to generate responses based on the queried documents.
8. I have tracked and ret
urned **response times** for LLM queries.

code:

from flask import Flask, request, jsonify, render\_template

from qdra
nt\_client import QdrantClient

from qdrant\_client.http.models import VectorParams, Distance, PointStruct

import os

i
mport requests

import uuid

import time

from pypdfloader import PyPDFLoader

from langchain.text\_splitter import Recu
rsiveCharacterTextSplitter

from langchain.chains.combine\_documents import create\_stuff\_documents\_chain

from langch
ain\_groq import ChatGroq

from config import Config

app = Flask(\_\_name\_\_)

app.config.from\_object(Config)

qdrant
\_client = QdrantClient(

url=app.config\['QDRANT\_URL'\],

api\_key=app.config\['QDRANT\_API\_KEY'\],

)

qdrant\_clien
t.recreate\_collection(

collection\_name=app.config\['COLLECTION\_NAME'\],

vectors\_config=VectorParams(size=768, dist
ance=Distance.COSINE)

)

os.environ\['groq\_api\_key'\] = 'gsk\_WBqHA6p2LZBEeK'

groq\_api\_key = os.environ\['groq\_ap
i\_key'\]

llm = ChatGroq(groq\_api\_key=groq\_api\_key, model\_name='llama-3.1-70b-versatile')

u/app.route('/')

def i
ndex():

return render\_template('index.html')

def extract\_text\_from\_pdf(file\_path):

loader = PyPDFLoader(file\_pa
th)

documents = loader.load()

plain\_text = '\\n'.join(\[doc.page\_content for doc in documents\])

return plain\_text


def chunk\_document(text):

text\_splitter = RecursiveCharacterTextSplitter(chunk\_size=1000, chunk\_overlap=200)

chu
nks = text\_splitter.split\_text(text)

return chunks

def embed\_document(content: str):

jina\_api\_url = 'https://api
.jina.ai/v1/embeddings'

payload = {

'model': 'jina-clip-v1',

'normalized': True,

'embedding\_type': 'float',

'input
': \[{'text': content}\]

}

headers = {

'Content-Type': 'application/json',

'Authorization': f'Bearer {os.getenv('JIN
AAI\_API\_KEY')}'

}

response = requests.post(jina\_api\_url, headers=headers, json=payload)

return response.json()\['
data'\]\[0\]\['embedding'\] if response.status\_code == 200 else None

u/app.route('/upload', methods=\['POST'\])

def u
pload\_document():

file = request.files\['file'\]

if not file:

return jsonify({'message': 'No file uploaded'}), 400


file\_path = f'./{file.filename}'

file.save(file\_path)

text = extract\_text\_from\_pdf(file\_path)

chunks = chunk\_d
ocument(text)

for chunk in chunks:

embedding = embed\_document(chunk)

if embedding:

point\_id = str(uuid.uuid4())

p
oint = PointStruct(id=point\_id, vector=embedding, payload={'text': chunk})

qdrant\_client.upsert(collection\_name=app.
config\['COLLECTION\_NAME'\], points=\[point\])

return jsonify({'message': 'Document uploaded and processed successfull
y'}), 200

u/app.route('/query', methods=\['POST'\])

def query\_document():

query\_text = request.json.get('query')

i
f not query\_text:

return jsonify({'message': 'Query text is required'}), 400

query\_embedding = embed\_document(query
\_text)

if query\_embedding:

search\_result = qdrant\_client.search(

collection\_name=app.config\['COLLECTION\_NAME'\
],

query\_vector=query\_embedding,

limit=3

)

documents = \[doc.payload\['text'\] for doc in search\_result\]

docume
nt\_chain = create\_stuff\_documents\_chain(llm, documents)

start = time.process\_time()

response = document\_chain.in
voke({'input': query\_text})

response\_time = time.process\_time() - start

return jsonify({

'response\_time': respons
e\_time,

'answer': response\['answer'\],

'documents': documents

}), 200

else:

return jsonify({'message': 'Failed to
 generate query embeddings'}), 500

if \_\_name\_\_ == '\_\_main\_\_':

app.run(host='0.0.0.0', port=5000, debug=True)




  
error: (base) C:\\Users\\meow\\OneDrive\\Desktop\\restx>pip install Flask qdrant-client requests pypdfloader langch
ain langchain\_groq

Requirement already satisfied: Flask in c:\\users\\ashraf\\anaconda3\\lib\\site-packages (3.0.3)

R
equirement already satisfied: qdrant-client in c:\\users\\ashraf\\anaconda3\\lib\\site-packages (1.11.0)

Requirement al
ready satisfied: requests in c:\\users\\ashraf\\anaconda3\\lib\\site-packages (2.31.0)

ERROR: Could not find a version 
that satisfies the requirement pypdfloader (from versions: none)

ERROR: No matching distribution found for pypdfloader



```
---

     
 
all -  [ Anthropic LangChain JSON support? ](https://www.reddit.com/r/ClaudeAI/comments/1fbuyb5/anthropic_langchain_json_support/) , 2024-09-09-0912
```
I’m a programmer developing a project with LangChain that needs to use its JSON support feature to get an JSON output. S
o far I’m getting that with GPT, Mistral and Gemini. I’ve try to work around that limitation but Anthropic models never 
give a constant JSON output. Their models add text either at the beginning or the end of the response, but the worst par
t is that they imagine new JSON formats. For programmers to have a not constant response is a deal breaker. I don’t get 
why other models are programmer friendly but not Anthropic. In the Anthropic LangChain api page the JSON support is not 
there and after a year waiting I think it will never be:

https://python.langchain.com/v0.2/docs/integrations/chat/anthr
opic/

I would like to ask programmers with experience out there who have been working with Anthropic these questions. D
oes any programmer out there faced this problem? What is your way to get a constant format response from it?
```
---

     
 
all -  [ SQLAgent with ER relationship ](https://www.reddit.com/r/LangChain/comments/1fbsizg/sqlagent_with_er_relationship/) , 2024-09-09-0912
```


https://preview.redd.it/g2ubpj91ijnd1.png?width=1208&format=png&auto=webp&s=5ddde33896f8813bea9e64b273009e27bbf73c84


MY ER relationship looks like this,   
I Want to Fetch data of 'only' the subspace which is being passed   
So I have 2-
3 options here ig:-  
1. Create seperate  db files for each subspace and pass it as  
db =SQLDatabase.from\_uri('sqlite:
///updated\_database.db') #example  
But while scaling I think it's hard and maybe not so good to do hard to execute as 
of now

  
2. The only current I mentioned and am using passing subspace\_id as a param in SQL\_PREFIX  
passing the who
le db file

    SQL_PREFIX = '''You are an agent designed to interact with a SQL database.
    Given an input question, 
create a syntactically correct SQLite query to run, then look at the results of the query and return the answer.
    Unl
ess the user specifies a specific number of examples they wish to obtain, always limit your query to at most 5 results.

    You can order the results by a relevant column to return the most interesting examples in the database.
    Never qu
ery for all the columns from a specific table, only ask for the relevant columns given the question.
    You have access
 to tools for interacting with the database.
    Only use the below tools. Only use the information returned by the belo
w tools to construct your final answer.
    You MUST double check your query before executing it. If you get an error wh
ile executing a query, rewrite the query and try again.
    
    DO NOT make any DML statements (INSERT, UPDATE, DELETE,
 DROP etc.) to the database.
    
    To start you should ALWAYS look at the tables in the database to see what you can 
query.
    Do NOT skip this step.
    Then you should query the schema of the most relevant tables.
    Note- Only Fetch
 data for subspace id <subspace_id> '''



What should I even do ?
```
---

     
 
all -  [ [10 YoE, Data Scientist, Senior Data Scientist, United States] ](https://www.reddit.com/r/resumes/comments/1fbqkqg/10_yoe_data_scientist_senior_data_scientist/) , 2024-09-09-0912
```
https://preview.redd.it/mznijhisuind1.jpg?width=2481&format=pjpg&auto=webp&s=a39cd4cc6c0b601c25da76c8cc3f73f3b04b9dd3

H
ello everyone, I have five years of experience as a data scientist in the logistics and automotive industries. I would a
ppreciate any help with resume reviews or referrals to secure senior data scientist interviews at top tech companies. I'
m also open to any feedback on improving my profile.  
  
I’d be grateful if you could spare a few minutes—it would mean
 a lot. Thank you!  
  

```
---

     
 
all -  [ How to build an AI coding agent? ](https://www.reddit.com/r/LocalLLaMA/comments/1fbqgov/how_to_build_an_ai_coding_agent/) , 2024-09-09-0912
```
Hi guys , Actually I was looking to build an AI coding agent that can write code on repository level and also It can be 
used to build entire applications from just text prompts. I know this can be done with langchain and langraph. But what 
are the other steps I meed to follow ? and can anyone give me a complete roadmap on how I can start building this?
```
---

     
 
all -  [ Make agent understand/convert the terms in natural language to the actual values in database ](https://www.reddit.com/r/LangChain/comments/1fboyjc/make_agent_understandconvert_the_terms_in_natural/) , 2024-09-09-0912
```
Hello everyone, I have been building a multi-agent system that takes in a natural language question and converts it into
 an SQL query to query again the database. 

It's been working quite well but whenever the question includes a term that
 isn't exactly the same and in the database, it's kind of messed up. 

For example, when the user asks the question 'Wha
t is the revenue in the States?'. The correct query should be 'select sum(revenue) from sales where country = 'US'. I do
n't know how to make the agent understand that 'the States' should mean 'US' in the context of the database. 
```
---

     
 
all -  [ best llm model for human chat ](https://www.reddit.com/r/LangChain/comments/1fbnxix/best_llm_model_for_human_chat/) , 2024-09-09-0912
```
what is the current best ai llm model for a human friend like chatting experience?? 
```
---

     
 
all -  [ [Student] Sent over 200+ SWE internships applications, but barley getting interviews ](https://www.reddit.com/r/EngineeringResumes/comments/1fbh3l4/student_sent_over_200_swe_internships/) , 2024-09-09-0912
```
https://preview.redd.it/zzo8ftb5bgnd1.png?width=5100&format=png&auto=webp&s=365d22e834c98eac1bafea5779a97b38c9227cdf

I'
m trying to figure out what is wrong with my resume because it looks fine to me. I am targeting entry-level software eng
ineering internships at small companies or big tech companies. I have a premium subscription to ResumeWord AI, and despi
te a score of over 95 in my resume, it didn't really have an impact. I have a niche in AI and RAG and try to sneak in so
ft skills in a technical way. I had previous internships due to connections and networking(I mass applied and got nothin
g last year) and never actually went through a full interview process. Also, a slightly smaller question is having a bro
ader skillset more important or specialization. And yes, I have following 90% of the guidelines mentioned on the Wiki of
 this subreddit. Any harsh criticism would be greatly appreciated.
```
---

     
 
all -  [ Langchain Structured Output vs OpenAI Structured Outputs ](https://www.reddit.com/r/LangChain/comments/1fbfrcn/langchain_structured_output_vs_openai_structured/) , 2024-09-09-0912
```
Hello. As you know, openai recently announced the 'Structured Outputs' feature. They used to support json response befor
e, but this new feature offers 100% guarantee and provides much more stable usage. I also need an LLM that can provide 1
00% guaranteed and high-performance JSON response. But I also need to use the langchain library for some of its features
 (such as prompt template, ai agent tools) and multiple llm support. At this point, I have 2 questions:



1) What is th
e difference between the langchain structured outputs feature and the new openai structured outputs feature? Can langcha
in provide 100% guaranteed and high-performance JSON response like openai?

2) If not, is there a way to use the new ope
nai feature via langchain?



I am new to langchain and llms in general. I would be very happy if you could help me, tha
nk you.
```
---

     
 
all -  [ LangChain's Repository ](https://github.com/langchain-ai/langchain) , 2024-09-09-0912
```

```
---

     
 
all -  [ I wrote my first Medium blog on Multi-Agent Systems Discussion ](https://www.reddit.com/r/LangChain/comments/1fb47oz/i_wrote_my_first_medium_blog_on_multiagent/) , 2024-09-09-0912
```
For a few months, I have been a part of this sub and working on multi-agent systems for several use-cases. 
I recently w
rote an article on Medium on the same and I would really appreciate your feedback. I wanted to mostly present my finding
s about what works and what doesn't in the industry along with giving an introduction to the topic. 

Here's the link: [
Medium](https://medium.com/@yashbhardwaj.1912/the-power-of-collaboration-llm-agents-in-multi-agent-systems-8c0441157f14)
! 
```
---

     
 
all -  [ Review and suggest ideas for my RAG chatbot ](https://www.reddit.com/r/LocalLLaMA/comments/1fb2osi/review_and_suggest_ideas_for_my_rag_chatbot/) , 2024-09-09-0912
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

     
 
all -  [ GraphRAG practical issues  ](https://www.reddit.com/r/learnmachinelearning/comments/1fb2ekl/graphrag_practical_issues/) , 2024-09-09-0912
```
I tried GraphRAG using LangChain and figured out some problems and issues it can't handle. Check out GraphRAG problems d
emonstrated here : https://youtu.be/z5ldGLU7NwU?si=o0KQ6riVkLKpyRHF
```
---

     
 
all -  [ Has anyone tried this tool? ](https://www.reddit.com/r/PromptEngineering/comments/1faurye/has_anyone_tried_this_tool/) , 2024-09-09-0912
```
Just wondering if this is worth a look vs just langchain, or what is special about it?

[https://venturebeat.com/ai/how-
few-shot-learning-with-googles-prompt-poet-can-supercharge-your-llms/](https://venturebeat.com/ai/how-few-shot-learning-
with-googles-prompt-poet-can-supercharge-your-llms/)


```
---

     
 
all -  [ What does your LLM stack look like these days? ](https://www.reddit.com/r/LangChain/comments/1fanhgm/what_does_your_llm_stack_look_like_these_days/) , 2024-09-09-0912
```
I am starting to use more of CrewAI, DSPy, Claude sonnet, chromadb and Langtrace. 
```
---

     
 
all -  [ has anyone checked this Decomposed Automation Correction for Text-to-SQL?  ](https://www.reddit.com/r/LangChain/comments/1fan5am/has_anyone_checked_this_decomposed_automation/) , 2024-09-09-0912
```
[https://github.com/zirui-HIT/DAC/tree/main](https://github.com/zirui-HIT/DAC/tree/main)

[https://arxiv.org/pdf/2408.08
779v2](https://arxiv.org/pdf/2408.08779v2)
```
---

     
 
all -  [ Does Microsoft Ever Make Anything Easy? Azure + Langchain help ](https://www.reddit.com/r/LangChain/comments/1faknzu/does_microsoft_ever_make_anything_easy_azure/) , 2024-09-09-0912
```
I am trying to setup, a working Langchain script to chat with AI to my Azure instance. Below is what I had before in def
ining the llm.

```javascript
import { ChatOpenAI } from 'langchain/chat_models/openai'

let llm = new ChatOpenAI({
  op
enAIApiKey,
  streaming: true,
  callbacks: [
    {
      handleLLMStart: async () => {
        id = setTimeout(() => {

          chat.setMessage(-1, md(`### Sorry, the AI is taking a long time to respond.`))
          setLoading(true)
    
    }, 3000)
        log(JSON.stringify({ event: 'handleLLMStart' }))
        currentMessage = ``
        chat.addMessag
e('')
      },
      handleLLMNewToken: async token => {
        clearTimeout(id)
        setLoading(false)
        if (
!token) return
        currentMessage += token
        let htmlMessage = md(currentMessage)
        chat.setMessage(-1, 
htmlMessage)
      },
      handleLLMError: async err => {
        warn(JSON.stringify({ event: 'handleLLMError', error:
 err }))
        running = false
        await appendToLogFile(JSON.stringify({ type: 'Error', message: err.message }) +
 ',\n')
      },
      handleLLMEnd: async () => {
        running = false
        log(JSON.stringify({ event: 'handleLL
MEnd' }))
        if (currentMessage) {
          await appendToLogFile(JSON.stringify({ type: 'AI', message: currentMes
sage }) + ',\n')
        }
        currentMessage = ``
      },
    },
  ],
})
```

I know that import above is deprecat
ed, I am trying to switch to using `AzureChatOpenAI` and this is the code I have, which aligns with the new 0.2 docs

``
`javascript
import { AzureChatOpenAI } from '@langchain/openai';

let llm = new AzureChatOpenAI({
  azureOpenAIApiKey: p
rocess.env.AZURE_OPENAI_API_KEY,
  azureOpenAIApiInstanceName: process.env.AZURE_OPENAI_API_INSTANCE_NAME,
  azureOpenAI
ApiDeploymentName: process.env.AZURE_OPENAI_API_DEPLOYMENT_NAME,
  azureOpenAIApiVersion: process.env.AZURE_OPENAI_API_V
ERSION,
  callbacks: [
    {
      handleLLMStart: async () => {
        id = setTimeout(() => {
          chat.setMessa
ge(-1, md(`### Sorry, the AI is taking a long time to respond.`))
          setLoading(true)
        }, 3000)
        lo
g(JSON.stringify({ event: 'handleLLMStart' }))
        currentMessage = ``
        chat.addMessage('')
      },
      ha
ndleLLMNewToken: async token => {
        clearTimeout(id)
        setLoading(false)
        if (!token) return
        
currentMessage += token
        let htmlMessage = md(currentMessage)
        chat.setMessage(-1, htmlMessage)
      },
 
     handleLLMError: async err => {
        warn(JSON.stringify({ event: 'handleLLMError', error: err }))
        runnin
g = false
        await appendToLogFile(JSON.stringify({ type: 'Error', message: err.message }) + ',\n')
      },
      
handleLLMEnd: async () => {
        running = false
        log(JSON.stringify({ event: 'handleLLMEnd' }))
        if (c
urrentMessage) {
          await appendToLogFile(JSON.stringify({ type: 'AI', message: currentMessage }) + ',\n')
      
  }
        currentMessage = ``
      },
    },
  ],
})
```

I get a 404 error, which is not very helpful. I know for a 
fact my values are correct becuase I have a non langchain script that uses `const { AzureOpenAI } = require('openai');` 
and it works fine.

Also, I have noticed there might be an API Version that is for a particular deployment on Azure, as 
well as an API version for the entire instance. 

If anyone can provide insight on setting up Azure with Langchain and N
odeJS, I would be very greatful.

Thanks and happy coding.
```
---

     
 
all -  [ Free Generative AI Web App Course: Learn LangChain, NLP & Streamlit ](https://www.reddit.com/r/myHeadstarter/comments/1fak4vf/free_generative_ai_web_app_course_learn_langchain/) , 2024-09-09-0912
```
Here’s the link: [Free Course](https://www.udemy.com/course/building-generative-ai-web-apps-with-streamlit-langchain/) 🚀


My team at **ViSTEM** just launched an **exciting, FREE** course to teach you how to build AI-powered web apps using *
*Streamlit** and **LangChain**! Perfect for anyone wanting to dive into generative AI and web development. Whether you'r
e a beginner with some Python knowledge or an experienced developer, this course is a game-changer. Plus, you can even e
arn a **certificate** from us at ViSTEM—just send proof of completion! 🏆

**Course Highlights:**

* **Streamlit:** Build
 dynamic web apps
* **LangChain:** Master state-of-the-art AI frameworks
* **Text Summarization with NLP**
* **arXiv API
 Setup** for research paper handling

Get hands-on experience with **real-world projects** and build your own AI-powered
 research app! 🌟
```
---

     
 
all -  [ What is optimal for Langflow: Loop or multi-api call? or Tasks? ](https://www.reddit.com/r/LangChain/comments/1faiz56/what_is_optimal_for_langflow_loop_or_multiapi/) , 2024-09-09-0912
```
I'm in the midst of a fun side project to get good MTG ruling. My stopping point is getting LangChain/LangFlow to iterat
e over a list of \[words in brackets\] in a prompt, and then take those \[words in brackets\] from the user and put each
 set into an API request. Is there an easy way to do that? 
```
---

     
 
all -  [ Claude, Projects and RAG ](https://www.reddit.com/r/LangChain/comments/1faenrt/claude_projects_and_rag/) , 2024-09-09-0912
```
My understanding is that the Projects feature of Claude Soinnet 3.5 works a little like a RAG feature.  
The documents i
n the knowledge are indexed and then the prompt is augmented by information located within the documents located in the 
knowledge.  
The difference with RAG is that the documents in knowledge are uploaded  and not retrieved as in A RAG syst
em. Is this understanding correct?
```
---

     
 
all -  [ LangGraph.js Fundamentals: Nodes, Edges, Conditional Edges, and Graphs ](https://www.reddit.com/r/LangChain/comments/1faeh4h/langgraphjs_fundamentals_nodes_edges_conditional/) , 2024-09-09-0912
```
Hey folks! I've made this intro tutorial for LangGraph.js. 

[https://www.js-craft.io/blog/langgraph-js-conditional-edge
s-graphs/](https://www.js-craft.io/blog/langgraph-js-conditional-edges-graphs/)

Any feedback is welcomed! 
```
---

     
 
all -  [ Text2SQL using HuggingFace Llama3 ](https://www.reddit.com/r/LangChain/comments/1fae122/text2sql_using_huggingface_llama3/) , 2024-09-09-0912
```
Has anyone used HuggingFace to access Llama3 for Text2SQL problems? I can get results with Gemma using HuggingFace but w
hen I load Llama3 it says it's 16GB so I can't load directly. I can't find resources for Text2SQL using HuggingFace, but
 it's available for OpenAI, Groq. Below is the code with the Gemma model. 

    load_dotenv()
    
    POSTGRESQL_HOST =
 os.getenv('POSTGRESQL_HOST')
    POSTGRESQL_USER = os.getenv('POSTGRESQL_USER')
    POSTGRESQL_PASS = os.getenv('POSTGR
ESQL_PASS')
    POSTGRESQL_DB = os.getenv('POSTGRESQL_DB')
    POSTGRESQL_URI = f'postgresql://{POSTGRESQL_USER}:{POSTGR
ESQL_PASS}@{POSTGRESQL_HOST}:5432/{POSTGRESQL_DB}'
    
    HUGGINGFACEHUB_API_TOKEN = os.getenv('HUGGINGFACEHUB_API_TOK
EN')
    
    hf = HuggingFaceEndpoint(repo_id = 'google/gemma-2b', temperature = 0.1, huggingfacehub_api_token = HUGGIN
GFACEHUB_API_TOKEN)
    
    def configure_db(db_uri):
        return SQLDatabase(create_engine(db_uri))
    
    db = c
onfigure_db(POSTGRESQL_URI)
    
    db_chain = SQLDatabaseChain.from_llm(hf, db, verbose=True)
    
    user_query = 'W
hich control governs incident response planning under NIS2?'
    response = db_chain.invoke(user_query)
    print(respon
se)
    
```
---

     
 
all -  [ LLM uses fake documents from examples as context ](https://www.reddit.com/r/LangChain/comments/1faatl2/llm_uses_fake_documents_from_examples_as_context/) , 2024-09-09-0912
```
Hello!

I have been working on an internal AI assistant for my company, and have set up a RAG pipeline.

Unfortunately, 
given the right query, the model uses the fake documents provided through examples to generate his answer, which is quit
e jarring. Is there any best practice here? A way to clearly indicate that information given as examples should not be c
onsidered?

If that makes a difference, my team has been toying with [Prompty ](https://prompty.ai/)for the prompt templ
ating, and its langchain integration, [langchain\_prompty](https://api.python.langchain.com/en/latest/prompty_api_refere
nce.html). I'll gladly switch to something else if needed.

As for why examples are needed here, I am using structured o
utput to generate the answer chunk by chunk, with each chunk associated to a list of IDs, linking to the documents used 
for this chunk. Examples have a substantial impact on how well the model follows guidelines (not naming the documents in
 the body of the answer for example).

Thanks!
```
---

     
 
all -  [ Dev partner for Medium com scraper ](https://www.reddit.com/r/LangChain/comments/1faa4dk/dev_partner_for_medium_com_scraper/) , 2024-09-09-0912
```
I'm working on developing a Medium.com scraper that collects article data (titles, subtitles, authors, dates, etc.), and
 I'm looking for someone to join me in building it quickly and efficiently. If you have experience with Python, Selenium
, BeautifulSoup, or any web scraping tools and want to collaborate on this, let's connect!I'm open to new ideas and appr
oaches to make the scraper more powerful. DM me if you're interested, and let's get this rolling!
```
---

     
 
all -  [ is Langchian production ready? ](https://www.reddit.com/r/LangChain/comments/1fa9y8l/is_langchian_production_ready/) , 2024-09-09-0912
```
I am working on a startup project and almost finished. I have used langchain. Seen somewhere on youtube that langchain a
nd llamaindex or not prod ready? is it true?
```
---

     
 
all -  [ Evaluate your RAG pipeline with Ragas, agnostic of LLM ](https://www.reddit.com/r/LangChain/comments/1fa9953/evaluate_your_rag_pipeline_with_ragas_agnostic_of/) , 2024-09-09-0912
```
Another update from RAG Me Up! We have added some rudimentary evaluation metrics using Ragas so you can now start tweaki
ng your RAG pipeline objectively. Best thing is that it doesn't matter if you use ChatGPT, Gemini, Claude, Ollama, LLaMa
 3.1 or any other LLM, they are all supported.

By the way - we also added Re2 to have the LLM re-read your question, im
proving performance.

  
[https://github.com/AI-Commandos/RAGMeUp](https://github.com/AI-Commandos/RAGMeUp)
```
---

     
 
MachineLearning -  [ [P] Lessons from Retrieval Augmented Generation ](https://www.reddit.com/r/MachineLearning/comments/1f9tvg7/p_lessons_from_retrieval_augmented_generation/) , 2024-09-09-0912
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

     
 
MachineLearning -  [ [P] using GPT4o with langchain/chroma for sports analysis  ](https://www.reddit.com/r/MachineLearning/comments/1enuzlp/p_using_gpt4o_with_langchainchroma_for_sports/) , 2024-09-09-0912
```
Hi all, I'm working on a side project that helps with sports analysis for historical games, which in turn will help with
 sports betting. Currently I've been only focused on MLB because I wanted to see how the use case would pan out.

My fir
st attempt at this was to use the openai endpoint and load all the relevant JSON objects and send a prompt along with th
em to GPT and see what I get back. Eventually, the context size was getting way too big and the problem I was running in
to was that it was expensive. Although, the prompts back were actually pretty decent and relevant to the data.

My secon
d attempt was to setup a RAG using Chroma/LangChain/GPT4o. I got it to work but the answers all seem very off and super 
vague. None of the data I have was shown in any of the prompts i asked, or any of the players that were playing in a gam
e were mentioned at all in the prompt back, plus it kept mentioning wrong games/teams whe asking it specific games. I’m 
assuming I might need to adjust the vector store a bit but not sure how I can do that with chroma.

My question is what 
might be the best way to setup some sort of process? My end result, I would like a response back using the historical da
ta I've provided to make assumptions on what a game could be like based off all the stats given, with some room for GPT 
to also make some inference as well.

I am a super new at this so it's been a learning process so far; please bear with 
me.
```
---

     
 
deeplearning -  [ Month of August in AI ](https://www.reddit.com/r/deeplearning/comments/1f6zfz0/month_of_august_in_ai/) , 2024-09-09-0912
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

     
 
deeplearning -  [ Creating a project on NLP ](https://www.reddit.com/r/deeplearning/comments/1ey2e85/creating_a_project_on_nlp/) , 2024-09-09-0912
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

     
