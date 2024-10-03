 
all -  [ Question related to Graphs ](https://www.reddit.com/r/LangChain/comments/1fuhocb/question_related_to_graphs/) , 2024-10-03-0912
```
Hi Guys,

I'm dabbling around in Langgraph and running into an issue at this point.

I am trying to make a first node in
 my graph that should decide if someone is just small talking or actually asking a RAG specific question. It should make
 that decision based on the question and memory. I've try to implement this and it works if do this only on the question
, but id like to do it also based on memory.

Here is my implementation:

`from typing import TypedDict`  
`from langgra
ph.graph import StateGraph`  
`from langgraph.graph import Graph`

`class AgentState(TypedDict):`  
`messages: list[str]
`  
`workflow = StateGraph(AgentState)`

`def agent(question, memory):`  
`res = llm.invoke(f'''You are given an interac
tion with a user so far and the final  question. Use these to decide if the user is interested in small talk or that it 
want to know something specifically pension related.`  
`If it's related to small talk, return 'Small Talk'`  
`If it's 
related to pensions, return 'Pension'`  
`Only return either of these values and nothing else`

`Here is the question:` 
 
`{question}`  

`Here is the full conversation:`  
`{memory}`  
`''')`  
`return res.content`

`from langgraph.graph i
mport StateGraph, START, END`  
`from langgraph.graph.message import add_messages`  
`workflow = Graph()`  
`workflow.ad
d_node('agent', agent)`  
`workflow.add_edge(START, 'agent')`  
`workflow.add_edge('agent', END)`  
`graph = workflow.co
mpile()`  
`graph.invoke('How are you?', 'Nothing')`

  
this returns:  
AttributeError: 'str' object has no attribute '
items'

is there an issue with what i defined in my class?

Any help would be sweet! Thanks in advance
```
---

     
 
all -  [ Please help me find learning materials from the curriculum of this AI cohert ](https://www.reddit.com/r/learnprogramming/comments/1fuhlly/please_help_me_find_learning_materials_from_the/) , 2024-10-03-0912
```
Hello guys,

I have very basic coding knowledge; just for hobby but I'm interested in learning more about technical AI s
tuff. I really want to join this cohert but it's quite expensive for me ($1600).

They have their course plan [over](htt
ps://www.100xengineers.com/#curriculum) here. It would be really awesome if you could help me find a good source for any
 of the topics that you know.

Thanks!

# Course plan:

**Week 1:** Proprietary Models & Diffusion

* Live Lesson: Histo
ry of GenAI, How to Research, and Intro to Playground AI
* Live Lesson: How Diffusion Models Work and Playground AI
* Li
ve Lesson: Prompt Engineering for Various Outputs

**Week 2:** Intro to Stable Diffusion

**Week 3: Advanced Stable Diff
usion** (Img2Img, Extension & Inpainting)

* Live Lesson: Checkpoints, ControlNet, and More
* Live Lesson: img2img, Inpa
inting, and Extensions
* Assignment: Make a Diffusion Engine
* Lesson 1: How to Install Extensions
* Lesson 2: ControlNe
t
* Lesson 3: Inpainting

**Week 4: Dreambooth, ControlNet & IP Adapters**

* Live Lesson: Intro to Dreambooth and Contr
olNet IP Adapters
* Live Lesson: Parameters & Training with Dreambooth
* Lesson 1: IP Adapters
* Lesson 2: Preparing Dat
aset for Dreambooth Training
* Lesson 3: Dreambooth Training Parameters

**Week 5: Advanced Finetuning**

* Live Lesson:
 Intro to LoRA
* Live Lesson: Mastering LoRA Parameters
* Lesson 1: How to Install Kohya SS
* Lesson 2: Dataset for Trai
ning LoRA
* Lesson 3: Parameters for LoRA

**Week 6: ComfyUI**

* Live Lesson: Basics of ComfyUI
* Assignment: Advanced 
ComfyUI Workflows
* Live Lesson: Assignment 2 - Dreambooth Training

**Week 7: Advanced ComfyUI**

* Live Lesson: Breakd
own of ComfyUI Workflows
* Live Lesson: Project Breakdown & Revisions
* Capstone: Mid Cohort Capstone Project

**Week 8:
 Get Ready to Code**

* Live Lesson: Design Thinking and Problem Solving
* Video Lesson: Why Code?
* Exercise: Practice 
Set - BigBinary Exercises
* Live Lesson: Intro to Python
* Assignment: Product Breakdown

**Week 9: Get Ready to Code**


* Live Lesson: Building an API with FastAPI
* Live Lesson: Intro to UI Building
* Assignment: Build Your AI Toolkit
* A
ssignment: Developing a Chatbot

**Week 11: Topic: Building Full Stack AI Apps**

**Week 12: Intro to LLMs**

**Week 13*
*: **AI Agents (Autogen, crewAI, AssistantAPIs)**

**Week 14**: RAG with Langchain & Llamaindex

**Week 14:** Topic: Vec
tor Database (LLM Memory)

**Week 16**: Fine-tuning LLMs

**Week 17:** Model Deployment (MLOps)
```
---

     
 
all -  [ Please help me find learning materials from the curriculum of this AI cohert ](https://www.reddit.com/r/developersIndia/comments/1fuh6ex/please_help_me_find_learning_materials_from_the/) , 2024-10-03-0912
```
Hello guys,

I have very basic coding knowledge; just for hobby but I'm interested in learning more about technical AI s
tuff. I really want to join this cohert but it's quite expensive for me (₹1.35L).

They have their course plan [over](ht
tps://www.100xengineers.com/#curriculum) here. If you can help me find a good source for any of the topics you know, it 
will be real nice!

Thanks

# Course plan:

**Week 1:** Proprietary Models & Diffusion

* Live Lesson: History of GenAI,
 How to Research, and Intro to Playground AI
* Live Lesson: How Diffusion Models Work and Playground AI
* Live Lesson: P
rompt Engineering for Various Outputs

**Week 2:** Intro to Stable Diffusion

**Week 3: Advanced Stable Diffusion** (Img
2Img, Extension & Inpainting)

* Live Lesson: Checkpoints, ControlNet, and More
* Live Lesson: img2img, Inpainting, and 
Extensions
* Assignment: Make a Diffusion Engine
* Lesson 1: How to Install Extensions
* Lesson 2: ControlNet
* Lesson 3
: Inpainting

**Week 4: Dreambooth, ControlNet & IP Adapters**

* Live Lesson: Intro to Dreambooth and ControlNet IP Ada
pters
* Live Lesson: Parameters & Training with Dreambooth
* Lesson 1: IP Adapters
* Lesson 2: Preparing Dataset for Dre
ambooth Training
* Lesson 3: Dreambooth Training Parameters

**Week 5: Advanced Finetuning**

* Live Lesson: Intro to Lo
RA
* Live Lesson: Mastering LoRA Parameters
* Lesson 1: How to Install Kohya SS
* Lesson 2: Dataset for Training LoRA
* 
Lesson 3: Parameters for LoRA

**Week 6: ComfyUI**

* Live Lesson: Basics of ComfyUI
* Assignment: Advanced ComfyUI Work
flows
* Live Lesson: Assignment 2 - Dreambooth Training

**Week 7: Advanced ComfyUI**

* Live Lesson: Breakdown of Comfy
UI Workflows
* Live Lesson: Project Breakdown & Revisions
* Capstone: Mid Cohort Capstone Project

**Week 8: Get Ready t
o Code**

*  Live Lesson: Design Thinking and Problem Solving
* Video Lesson: Why Code?
* Exercise: Practice Set - BigBi
nary Exercises
* Live Lesson: Intro to Python
* Assignment: Product Breakdown

**Week 9: Get Ready to Code**

* Live Les
son: Building an API with FastAPI
* Live Lesson: Intro to UI Building
* Assignment: Build Your AI Toolkit
* Assignment: 
Developing a Chatbot

**Week 11: Topic: Building Full Stack AI Apps**

**Week 12: Intro to LLMs**

**Week 13**: **AI Age
nts (Autogen, crewAI, AssistantAPIs)**

**Week 14**: RAG with Langchain & Llamaindex

**Week 14:** Topic: Vector Databas
e (LLM Memory)

**Week 16**: Fine-tuning LLMs

**Week 17:** Model Deployment (MLOps)
```
---

     
 
all -  [ 🚀 Join our Global AI Agents Hackathon with LangChain 🦜🔗 and Llama Index 🦙! ](https://tensorops.ai/aiagentsonlinehackathon) , 2024-10-03-0912
```
I'm organizing a global online hackathon focused on creating AI Agents, partnering with LangChain!!! and Llama Index. 🎉


Key Details:
🏆 Challenge: Build an AI Agent + create usage guide
🌐 Format: Online, with live webinars and expert lectur
es
🧠 Perks: Top-tier mentors and judges
📚 Submission: PR to the GitHub GenAI_Agents repo

We got over 100 registrations 
in the first 24 hours 😲 

❓ Questions? Ask below!

Registration in the link attached.
```
---

     
 
all -  [ Issues with Running LLMs Locally for PDF Data Extraction (OLLAMA and Langchain vs HuggingFaceChat) ](https://www.reddit.com/r/LocalLLaMA/comments/1fufo1g/issues_with_running_llms_locally_for_pdf_data/) , 2024-10-03-0912
```
Hey everyone,

I’ve been experimenting with running LLMs locally using tools like OLLAMA and Langchain, and I’ve encount
ered an issue when trying to extract basic information from PDFs (like title, author, etc.).

When I use the `command-r`
 model on HuggingFaceChat, paired with their document parser, it works perfectly, returning clean and accurate metadata.
 However, when I try to replicate this locally in Langchain, using either the `PyPDFLoader` or `UnstructuredLoader`, and
 the same model, the performance drops significantly. Instead of giving me the metadata I ask for, the model starts ramb
ling, generating random details from the text without providing the specific data requested.

Has anyone else faced a si
milar issue when running models locally for PDF parsing? How different is the data extraction approach between Langchain
 and HuggingFaceChat? If you’ve managed to resolve this or have any insights, I’d love to hear them.

Thanks in advance!

```
---

     
 
all -  [ Experiment Tracking Tools & Lbirary Suggestion For Using Alonside Langchain ](https://www.reddit.com/r/LangChain/comments/1fufh22/experiment_tracking_tools_lbirary_suggestion_for/) , 2024-10-03-0912
```
Hey everyone,

  
I'm at the beggining of developing a LLM application. My plan is preparing a MLOps arhictecture along 
with Langchain to track Chain, RAG utils (vector db name, search params etc.), input-output and evaluation metrics etc. 
In order to do this, I've planned to use MLFlow, however, compabilities between those libraries are not set (or maintene
d after langchain version 0.1 I do not know) so I'm not able to finish a full tracking pipeline for now (langchain versi
on == 0.3.1, mlflow version == 2.16.2). In addition, in mlflow website, they said this notebook was made with langchain 
version 0.1, but downgrading langchain library from 0.3 to 0.1 to use mlflow only might seems not a good idea at all.  


  
Is there any suggestion to use tracking library, tool etc. to use with Langchain ?   
  
Cheers     
```
---

     
 
all -  [ AgentLite By Salesforce ](https://www.reddit.com/r/LangChain/comments/1fub1mp/agentlite_by_salesforce/) , 2024-10-03-0912
```
in the AgentLite study there are some pretty bold statements in terms of how AgentLite compares to other dev environment
s, like LangChain...

  
Does anyone have practical experience in building solutions with AgentLite?

https://preview.re
dd.it/6xuhk3jtvasd1.png?width=2066&format=png&auto=webp&s=7b1f4a7bfe13311ff4fb16d1a6aa895f909e1699

  

```
---

     
 
all -  [ RAG - Hybrid Document Search and Knowledge Graph with Contextual Chunking, OpenAI, Anthropic, FAISS, ](https://www.reddit.com/r/Rag/comments/1fu9u5r/rag_hybrid_document_search_and_knowledge_graph/) , 2024-10-03-0912
```
Hey folks!

Previously, I released [Contextual-Doc-Retrieval-OpenAI-Reranker](https://github.com/lesteroliver911/context
ual-doc-retrieval-opneai-reranker), and now I've enhanced it by integrating a graph-based approach to further boost accu
racy. The project leverages OpenAI’s API, contextual chunking, and retrieval augmentation, making it a powerful tool for
 precise document retrieval. I’ve also used strategies like embedding-based reranking to ensure the results are as accur
ate as possible.

**the git-repo** [**here**](https://github.com/lesteroliver911/contextual-chunking-graphpowered-rag)


The runnable Python code is available on GitHub for you to fork, experiment with, or use for educational purposes. As so
meone new to Python and learning to code with AI, this project represents my journey to grow and improve, and I’d love y
our feedback and support. Your encouragement will motivate me to keep learning and evolving in the Python community! 🙌




[architecture diagram based on the code. correction - we are using the gpt-4o model](https://preview.redd.it/spinhmf6f
asd1.png?width=1920&format=png&auto=webp&s=8967b1026d99d7fc25d0dc12b66f54953c9c2794)

# Table of Contents

* [Features](
#features)
* [Key Strategies for Accuracy and Robustness](#key-strategies-for-accuracy-and-robustness)
* [Installation](
#installation)
* [Environment Variables](#environment-variables)
* [Usage](#usage)
* [Example](#example)
* [Results](#re
sults)
* [Evaluation](#evaluation)
* [Visualization](#visualization)
* [Contributing](#contributing)
* [License](#licens
e)

# Features

* **Hybrid Search**: Combines vector search with FAISS and BM25 token-based search for enhanced retrieva
l accuracy and robustness.
* **Contextual Chunking**: Splits documents into chunks while maintaining context across boun
daries to improve embedding quality.
* **Knowledge Graph**: Builds a graph from document chunks, linking them based on s
emantic similarity and shared concepts, which helps in accurate context expansion.
* **Context Expansion**: Automaticall
y expands context using graph traversal to ensure that queries receive complete answers.
* **Answer Checking**: Uses an 
LLM to verify whether the retrieved context fully answers the query and expands context if necessary.
* **Re-Ranking**: 
Improves retrieval results by re-ranking documents using Cohere's re-ranking model.
* **Graph Visualization**: Visualize
s the retrieval path and relationships between document chunks, aiding in understanding how answers are derived.

# Key 
Strategies for Accuracy and Robustness

1. **Contextual Chunking**:
   * Documents are split into manageable, overlappin
g chunks using the `RecursiveCharacterTextSplitter`. This ensures that the integrity of ideas across boundaries is prese
rved, leading to better embedding quality and improved retrieval accuracy.
   * Each chunk is augmented with contextual 
information from surrounding chunks, creating semantically richer and more context-aware embeddings. This approach ensur
es that the system retrieves documents with a deeper understanding of the overall context.
2. **Hybrid Retrieval (FAISS 
and BM25)**:
   * **FAISS** is used for semantic vector search, capturing the underlying meaning of queries and document
s. It provides highly relevant results based on deep embeddings of the text.
   * **BM25**, a token-based search, ensure
s that exact keyword matches are retrieved efficiently. Combining FAISS and BM25 in a hybrid approach enhances precision
, recall, and overall robustness.
3. **Knowledge Graph**:
   * The knowledge graph connects chunks of documents based on
 both semantic similarity and shared concepts. By traversing the graph during query expansion, the system ensures that r
esponses are not only accurate but also contextually enriched.
   * Key concepts are extracted using an LLM and stored i
n nodes, providing a deeper understanding of relationships between document chunks.
4. **Answer Verification**:
   * Onc
e documents are retrieved, the system checks if the context is sufficient to answer the query completely. If not, it aut
omatically expands the context using the knowledge graph, ensuring robustness in the quality of responses.
5. **Re-Ranki
ng**:
   * Using Cohere's re-ranking model, the system reorders search results to ensure that the most relevant document
s appear at the top, further improving retrieval accuracy.

# Usage

1. **Load a PDF Document**: The system uses `LlamaP
arse` to load and process PDF documents. Simply run the [`main.py`](http://main.py) script, and provide the path to your
 PDF file:python [main.py](http://main.py)
2. **Query the Document**: After processing the document, you can enter queri
es in the terminal, and the system will retrieve and display the relevant information:Enter your query: What are the key
 points in the document?
3. **Exit**: Type `exit` to stop the query loop.

# Example

    Enter the path to your PDF fil
e: /path/to/your/document.pdf
    
    Enter your query (or 'exit' to quit): What is the main concept?
    Response: The
 main concept revolves around...
    
    Total Tokens: 1234
    Prompt Tokens: 567
    Completion Tokens: 456
    Total
 Cost (USD): $0.023

# Results

The system provides **highly accurate** retrieval results due to the combination of FAIS
S, BM25, and graph-based context expansion. Here's an example result from querying a technical document:

**Query**: 'Wh
at are the key benefits discussed?'

**Result**:

* **FAISS/BM25 hybrid search**: Retrieved the relevant sections based 
on both semantic meaning and keyword relevance.
* **Answer**: 'The key benefits include increased performance, scalabili
ty, and enhanced security.'
* **Tokens used**: 765
* **Accuracy**: 95% (cross-verified with manual review of the documen
t).

# Evaluation

The system supports evaluating the retrieval performance using test queries and documents. Metrics su
ch as **hit rate**, **precision**, **recall**, and **nDCG (Normalized Discounted Cumulative Gain)** are computed to meas
ure accuracy and robustness.

    test_queries = [
        {'query': 'What are the key findings?', 'golden_chunk_uuids':
 ['uuid1', 'uuid2']},
        ...
    ]
    
    evaluation_results = graph_rag.evaluate(test_queries)
    print('Evalua
tion Results:', evaluation_results)

**Evaluation Result (Example)**:

* **Hit Rate**: 98%
* **Precision**: 90%
* **Reca
ll**: 85%
* **nDCG**: 92%

These metrics highlight the system's robustness in retrieving and ranking relevant content.


# Visualization

The system can visualize the knowledge graph traversal process, highlighting the nodes visited during c
ontext expansion. This provides a clear representation of how the system derives its answers:

1. **Traversal Visualizat
ion**: The graph traversal path is displayed using `matplotlib` and `networkx`, with key concepts and relationships high
lighted.
2. **Filtered Content**: The system will also print the filtered content of the nodes in the order of traversal
.Filtered content of visited nodes in order of traversal: Step 1 - Node 0: Filtered Content: This chunk discusses... Ste
p 2 - Node 1: Filtered Content: This chunk adds details on...

# License

This project is licensed under the MIT License
. See the LICENSE file for details.
```
---

     
 
all -  [ Received Cool Swag 😎 ](https://i.redd.it/5jr7pq85l9sd1.jpeg) , 2024-10-03-0912
```

```
---

     
 
all -  [ Making my AI assistant understand complex product configurations – Any advice? ](https://www.reddit.com/r/LangChain/comments/1fu2ec7/making_my_ai_assistant_understand_complex_product/) , 2024-10-03-0912
```
I'm trying to build a chat assistant that is an expert in a company's refrigeration products, such as refrigerators, fre
ezers, and wine coolers. Each product type has different categories (e.g., French door refrigerators, side-by-side freez
ers, etc.) and multiple models under each category. Every model offers features like different temperature controls, ene
rgy ratings, and storage capacities.

The data about these features is stored in a very complex SQL database, and we als
o have detailed product descriptions in a text format.

**What I've tried so far:**

I created an agent using LangChain 
with two tools:

1. A vector database containing product descriptions
2. Another tool to query the SQL database based on
 user input.

The challenge is that the SQL database structure is quite intricate, leading to incorrect predictions from
 the LLM, and the chat experience lacks interactivity. For instance, if a user asks, 'What’s the temperature range of mo
del X?' the assistant doesn't prompt the user further by saying, 'This depends on the cooling zones. We offer single, du
al, and triple cooling zones. Which one are you interested in?'

**My goal:**

I want to make the interaction more user-
friendly, like:

**User:** 'I'm looking for a refrigerator.'  
**AI:** 'We offer the following types: French door, side-
by-side, and top freezer. Which one are you interested in?'  
**User:** 'Tell me about French door refrigerators.'  
**A
I:** 'Our French door refrigerators come in various sizes and offer features like adjustable temperature zones, humidity
-controlled crispers, and energy-saving modes. Would you like more details on a specific feature?'

**User:** 'What abou
t the adjustable temperature zones?'  
**AI:** 'The adjustable temperature zones vary based on the model. Would you like
 to know about the temperature range, available sizes, or energy ratings?'

**User:** 'Tell me the temperature range.'  

**AI:** 'Our French door refrigerators offer temperature ranges from -2°C to 8°C. Some models have separate compartment
s with independent temperature settings. Are you looking for more information on a specific model?'

I believe using Lan
gGraph could help solve this problem and make the chat more interactive, but I'm not entirely sure how to implement it e
ffectively for this use case. Is LangGraph the right solution, or should I be approaching this differently? Any guidance
 or advice would be incredibly helpful!
```
---

     
 
all -  [ How would you create a PowerPoint to text agent?
 ](https://www.reddit.com/r/SmythOS_/comments/1fu0dp8/how_would_you_create_a_powerpoint_to_text_agent/) , 2024-10-03-0912
```
I'm looking to build an AI agent that can convert PowerPoint presentations into text summaries. I'm curious about the mo
st cost-effective way to approach this, preferably using open-source tools. Here's what I'm thinking:

1. PowerPoint par
sing: Any recommendations for libraries that can extract content from .pptx files?
2. Text extraction: Once we have the 
slide content, what's a good way to pull out the relevant text?
3. Summarization: Are there any lightweight, open-source
 NLP models that could help condense the extracted text?
4. Would LangChain and AutoGPT be an overkill for this task? An
y other frameworks I should consider?
```
---

     
 
all -  [ HTML to markdown ](https://www.reddit.com/r/LangChain/comments/1ftz07p/html_to_markdown/) , 2024-10-03-0912
```
I want to build an RAG application for documentation Q&A. I'm new to this but I understand I've to do some preprocessing
 to first convert the webpage of the documentation and all the sublinks into markup to then split into chunks and store 
in a vector store. What's the best and preferred way to do the conversion?
```
---

     
 
all -  [ List of FREE and Best Selling Discounted Courses ](https://www.reddit.com/r/udemyfreebies/comments/1ftyb6j/list_of_free_and_best_selling_discounted_courses/) , 2024-10-03-0912
```
# Udemy Free Courses for 02 October 2024

Note : Coupons might expire anytime, so enroll as soon as possible to get the 
courses for FREE.

* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/16909/)Complete FastAPI masterclass from scratch

* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/16908/)\[NEW\] 2024:Mastering Generative AI-From LLMs to Application
s
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/16907/)\[NEW\]Mastering Retrieval Augmented Generation (RAG) IN LL
Ms
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/16906/)Crea un Sistema de Compra y Venta con PHP, JS y SQL SERVER

* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/16905/)Reinforcement Learning beginner to master – AI in Python
* [
REDEEM OFFER ](https://idownloadcoupon.com/udemy/16904/)Time Series Analysis, Forecasting, and Machine Learning
* [REDEE
M OFFER ](https://idownloadcoupon.com/udemy/16903/)The Complete Ethical Hacking Coding Course
* [REDEEM OFFER ](https://
idownloadcoupon.com/udemy/16902/)SOC(Cybersecurity):Build Powerful SOC with Open Source Tools
* [REDEEM OFFER ](https://
idownloadcoupon.com/udemy/16901/)Cyber Security-SOC and SIEM (SPLUNK&ELK) for Beginners -2024
* [REDEEM OFFER ](https://
idownloadcoupon.com/udemy/16900/)Cyber Security (SOC) Interview Questions and Answers-2024
* [REDEEM OFFER ](https://ido
wnloadcoupon.com/udemy/16899/)Azure Data Factory Training–Continuous Integration/Delivery
* [REDEEM OFFER ](https://idow
nloadcoupon.com/udemy/16898/)Master Angular 7 (formerly Angular 2): The Complete Course
* [REDEEM OFFER ](https://idownl
oadcoupon.com/udemy/16897/)Mastering Figma from 0 to 100 (UI/UX Mastery Course)
* [REDEEM OFFER ](https://idownloadcoupo
n.com/udemy/16896/)Mathematics-Basics to Advanced for Data Science And GenAI
* [REDEEM OFFER ](https://idownloadcoupon.c
om/udemy/16895/)Complete Generative AI Course With Langchain and Huggingface
* [REDEEM OFFER ](https://idownloadcoupon.c
om/udemy/16894/)Building Gen AI App 12+ Hands-on Projects with Gemini Pro
* \[New\] 1300+ DevOps Interview Questions – P
ractice Tests Pack
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/16893/)
* [REDEEM OFFER ](https://idownloadcoupon.
com/udemy/16892/)React 16: The Complete Course (incl. React Router 4 & Redux)
* [REDEEM OFFER ](https://idownloadcoupon.
com/udemy/16891/)Complete Machine Learning,NLP Bootcamp MLOPS & Deployment
* [REDEEM OFFER ](https://idownloadcoupon.com
/udemy/16890/)Complete Data Analyst Bootcamp From Basics To Advanced
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy
/16889/)6 FULL Certified in Cybersecurity (CC) tests #1-6 ISC2 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/
16888/)Free System Design Interview Tutorial – System Design Masterclass (2024)
* [REDEEM OFFER ](https://idownloadcoupo
n.com/udemy/16887/)Python Web Development: Building Interactive Websites
* [REDEEM OFFER ](https://idownloadcoupon.com/u
demy/16886/)Practical IoT Security and Penetration testing for Beginners
* [REDEEM OFFER ](https://idownloadcoupon.com/u
demy/16885/)AWS Certified Data Engineer – Associate – Hands On + Exams
* [REDEEM OFFER ](https://idownloadcoupon.com/ude
my/16884/)Certified Kubernetes Administrator Ultimate Masterclass
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/16
883/)Certified Kubernetes Application Developer Masterclass
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/16882/)A
WS Certified Cloud Practitioner
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/16881/)Ethically Hack the Planet Par
t 2
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/16880/)Ethically Hack the Planet Part 4
* [REDEEM OFFER ](https:
//idownloadcoupon.com/udemy/16879/)Robotics and ROS 2 – Learn by Doing! Manipulators
* [REDEEM OFFER ](https://idownload
coupon.com/udemy/16878/)The Complete JavaScript Course: From Zero to Expert
* Certified Kubernetes Security Specialist M
asterclass
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/16877/)
* [REDEEM OFFER ](https://idownloadcoupon.com/udem
y/16876/)Learn Basics of Robotics
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/16875/)Complete Beginners Trading 
Strategy For Passive Income
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/16874/)ChatGPT Masterclass: The Ultimate
 Beginner’s Guide!
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/16873/)Google Cloud Network Engineer (PCNE) Full 
Practice Exams
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/16872/)Presentations with ChatGPT
* [REDEEM OFFER ](h
ttps://idownloadcoupon.com/udemy/16871/)Professional Diploma in Omnichannel Sales&Service Management
* [REDEEM OFFER ](h
ttps://idownloadcoupon.com/udemy/16870/)File & Folder Management Using PowerShell
* [REDEEM OFFER ](https://idownloadcou
pon.com/udemy/16869/)ChatGPT Prompt Engineering Mastery
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/16868/)Pytho
n & Gen AI Basics: Transition from Java in Just 15 days
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/16867/)Agile
 Fundamentals Certification
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/16866/)Supercharging your business with 
AI tools
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/16865/)7 steps to entrepreneurship: A complete business pla
n (PRO)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/16864/)Financial Modeling on Excel Complete finance course o
n Excel
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/16863/)ChatGPT & Generative AI: The ultimate AI course
* [RE
DEEM OFFER ](https://idownloadcoupon.com/udemy/16862/)ChatGPT e IA Generativa: guía de IA y prompt engineering
* Trends 
in Ethical Teaching
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/16861/)
* [REDEEM OFFER ](https://idownloadcoupon
.com/udemy/16860/)Scrum Master Certification
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/16859/)Master Agile & S
crum Basics
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/16858/)Executive Diploma in Consumer Lending Business
* 
[REDEEM OFFER ](https://idownloadcoupon.com/udemy/16857/)The Complete Java Course: From Basics to Advanced
* [REDEEM OFF
ER ](https://idownloadcoupon.com/udemy/16855/)Free FinOps Tutorial – FinOps for GenAI
* [REDEEM OFFER ](https://idownloa
dcoupon.com/udemy/16854/)Free ChatGPT Tutorial – What is ChatGPT and how does it work?
* [REDEEM OFFER ](https://idownlo
adcoupon.com/udemy/16853/)Free Natural Language Processing (NLP) Tutorial – A Beginner’s guide to the spaCy NLP library

* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/16852/)Free Business Branding Tutorial – Brand Management Essentials
 for Start-ups
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/16851/)Free LinkedIn Tutorial – LinkedIn Ads Free Cou
rse: Step by Step Beginners Guide
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/16850/)Free Tutorial – Beyond Heal
ing with NLS DIagnostics
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/16849/)Free Tutorial – Creating Videos with
 AI: invideo AI Video Creation Course
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/16848/)Free Tutorial – Beginne
rs Course of UX/UI Design on Adobe XD – Part 2
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/16847/)Master Content
 Creation : Become a paid Content Creator
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/16846/)Metaverse Professio
nal Certification
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/16845/)Interface Windows User Commands From The Be
ginner To Admin
* Web3 Professional Certification
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/16844/)
* [REDEEM O
FFER ](https://idownloadcoupon.com/udemy/16843/)ChatGPT e IA Generativa: guía de IA y prompt engineering
* [REDEEM OFFER
 ](https://idownloadcoupon.com/udemy/16842/)User Interface Design Professional Certification
* [REDEEM OFFER ](https://i
downloadcoupon.com/udemy/16841/)B2B Sales Director Executive Certification
* [REDEEM OFFER ](https://idownloadcoupon.com
/udemy/16840/)Agile Trainer Certification
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/16839/)Scrum Master Certif
ication
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/16838/)Learn how to create Variables in Modern JavaScript
* 
[REDEEM OFFER ](https://idownloadcoupon.com/udemy/16837/)Modelización financiera: curso completo de finanzas en Excel
* 
[REDEEM OFFER ](https://idownloadcoupon.com/udemy/16836/)Product Owner Professional Certification
* [REDEEM OFFER ](http
s://idownloadcoupon.com/udemy/16835/)Sales Professional Certification
* [REDEEM OFFER ](https://idownloadcoupon.com/udem
y/16834/)CSO Chief Security Officer Executive Certification
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/16833/)C
CO Chief Compliance Officer Executive Certification
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/16832/)Python Pr
o Bootcamp Zero to Hero
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/16831/)Prompt & AI Engineering Safety Profes
sional Certification
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/16830/)Comment ne plus échouer ? Le système de 
la réussite
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/16829/)Aprende WPF y MAUI desde CERO usando C#

GET MORE
 FREE ONLINE COURSES WITH CERTIFICATE – [CLICK HERE](https://idownloadcoupon.com/)
```
---

     
 
all -  [ Help with Streaming LLM Output Between Nodes in LangGraph ](https://www.reddit.com/r/LangChain/comments/1ftxfqw/help_with_streaming_llm_output_between_nodes_in/) , 2024-10-03-0912
```
Hi, I want to implement a graph in which one node calls an LLM with structured output, similar to [this](https://python.
langchain.com/docs/how_to/structured_output/#streaming)

`from typing_extensions import Annotated, TypedDict`

`class Jo
ke(TypedDict):`

`'''Joke to tell user.'''`

`setup: Annotated[str, ..., 'The setup of the joke']`

`punchline: Annotate
d[str, ..., 'The punchline of the joke']`

`rating: Annotated[Optional[int], None, 'How funny the joke is, from 1 to 10'
]`

`structured_llm = llm.with_structured_output(Joke)`

`for chunk in structured_llm.stream('Tell me a joke about cats'
):`

`print(chunk)`

In this example, every chunk is a piece of JSON. I want to implement this in a node that sends ever
y chunk to another node. For example, the next node will filter some information from the chunks it receives. Finally, i
t will write its output to `messages.` Basically, my use case is that I don't want to stream output directly from the LL
M node but to stream it from the formatting node. Can anyone please provide a code sample to help me do this?
```
---

     
 
all -  [ LLM Applications to Production  ](https://www.reddit.com/r/LangChain/comments/1fturqx/llm_applications_to_production/) , 2024-10-03-0912
```
Hey guys , we’ve been developing PoCs till now , and in order to move this to production line , what all steps are requi
red? What workflow is needed .. I’m new to this , so please guide me . Thanks ! 
```
---

     
 
all -  [ Debunking myths about pgvector ](https://www.reddit.com/r/LangChain/comments/1fttx7s/debunking_myths_about_pgvector/) , 2024-10-03-0912
```
I noticed a lot of recurring confusion around pgvector (the highly popular vector embedding extension for Postgres). One
 source of confusion is that pgvector is a meeting point of two communities: 

* People who understand vectors and vecto
r storage, but don't understand Postgres. 
* People who understand Postgres, SQL and relational DBs, but don't know much
 about vectors.

I wrote a blog about some of these misunderstandings that keep coming up again and again - especially a
round vector indexes and their limitations. Lots of folks believe that: 

1. You have to use vector indexes
2. Vector in
dexes are pretty much like other indexes in RDBMS
3. Pgvector is limited to 2000 dimension vectors
4. Pgvector misses da
ta for queries with WHERE conditions.
5. You only use vector embeddings for RAG
6. Pgvector can't work with BM25 (or oth
er sparse text-search vectors) 

I hope it helps someone or at least that you learn something interesting.

[https://www
.thenile.dev/blog/pgvector\_myth\_debunking](https://www.thenile.dev/blog/pgvector_myth_debunking)
```
---

     
 
all -  [ Benchmarking Hallucination Detection Methods in RAG ](https://www.reddit.com/r/LangChain/comments/1ftru5d/benchmarking_hallucination_detection_methods_in/) , 2024-10-03-0912
```
I came across this helpful Towards Data Science article for folks building RAG systems and concerned about hallucination
s.

If you're like me, keeping user trust intact is a top priority, and unchecked hallucinations undermine that. The [ar
ticle](https://towardsdatascience.com/benchmarking-hallucination-detection-methods-in-rag-6a03c555f063) benchmarks many 
hallucination detection methods across 4 RAG datasets (RAGAS, G-eval, DeepEval, TLM, and LLM self-evaluation).

Check it
 out if you're curious how well these tools can automatically catch incorrect RAG responses in practice. Would love to h
ear your thoughts if you've tried any of these methods, or have other suggestions for effective hallucination detection!

```
---

     
 
all -  [ Making a UUID Output Parser in Langchain ](https://www.reddit.com/r/LangChain/comments/1ftpdjn/making_a_uuid_output_parser_in_langchain/) , 2024-10-03-0912
```
Was trying to think of a good introductory feature to work on (as this is the first time I would be contributing to Lang
chain) and thought that this could be a good starting PR (the uuid output parser) in order to get used to the codebase. 
Is this a good idea? In terms of the output parser itself, was thinking it would help in terms of session management and
 data tracking.
```
---

     
 
all -  [ AWS DynamoDB backed checkpoint saver for Langgraph JS ](https://www.reddit.com/r/LangChain/comments/1ftpazv/aws_dynamodb_backed_checkpoint_saver_for/) , 2024-10-03-0912
```
In case anyone is looking to use DynamoDB as the persistence for Langgraph JS, I have created a package.

Link: [https:/
/www.npmjs.com/package/@rwai/langgraphjs-checkpoint-dynamodb](https://www.npmjs.com/package/@rwai/langgraphjs-checkpoint
-dynamodb)

It borrows heavily from the existing two persistence packages released by the Langchain team.
```
---

     
 
all -  [ How does ELL compare to langchain? ](https://www.reddit.com/r/datascience/comments/1ftp0oh/how_does_ell_compare_to_langchain/) , 2024-10-03-0912
```
Hey hey, just stumbled upon this [ELL](https://docs.ell.so/index.html) thing and curious if anyone tried it. How does it
 compare to langchain? Are they complementary?
```
---

     
 
all -  [ GIT Code - Exploring Contextual Retrieval with OpenAI GPT-4o, Cohere, and LangChain /no UI ](https://www.reddit.com/r/Rag/comments/1ftmfc7/git_code_exploring_contextual_retrieval_with/) , 2024-10-03-0912
```
I recently saw Claude’s post on using contextual retrievers to improve Retrieval-Augmented Generation (RAG) systems, whi
ch got me thinking about my own experiment. While Claude’s example used their Sonnet 3.5 model, I decided to go a differ
ent route and built something similar using the more budget-friendly **GPT-4o** from OpenAI.

I also integrated **Cohere
’s re-ranking** and **query expansion** to enhance accuracy. The system combines **BM25 for keyword-based search** with 
**contextual embeddings** to bring in more relevant results.

I’ve tested it on a 42-page document, parsing it with **Ll
amaParse** in multimodal mode. It only took a minute or two to get everything processed, and I’m now able to retrieve in
fo from anywhere in the document without the dreaded 'lost in the middle' issue. Next up: testing it on a 500-page docum
ent (will update you on that soon!).

here is the code: [Code Git Repo](https://github.com/lesteroliver911/contextual-do
c-retrieval-opneai-reranker)

**Features**

* **PDF Parsing**: Extracts content from PDFs using LlamaParse.
* **Contextu
al Chunking**: Splits documents into manageable chunks and provides contextual summaries using OpenAI's GPT-4.
* **BM25 
Search**: Implements a BM25 search index for efficient keyword-based retrieval.
* **Cohere Re-ranking**: Enhances search
 results by re-ranking them using Cohere's reranking model.
* **Query Expansion**: Expands search queries using AI to im
prove retrieval performance.
* **Error Handling**: Robust exception handling ensures reliable document processing.

If y
ou’re into RAG systems or AI in general, you can check out the code here: [Code Git Repo](https://github.com/lesterolive
r911/contextual-doc-retrieval-opneai-reranker) . I also explain the practical steps, how it works.

Would love to hear y
our thoughts or ideas on how I can improve it. Feel free to fork, contribute, or just drop feedback!
```
---

     
 
all -  [ How do I enhance LLM capabilities to carry out calculations on financial statement documents using R ](https://www.reddit.com/r/LangChain/comments/1fth9sb/how_do_i_enhance_llm_capabilities_to_carry_out/) , 2024-10-03-0912
```
I am currently working on RAG on financial statements. I am using gemini as my LLM and openAI with llamaindex for my age
nts. I want my RAG to be able to calculate any ratios or profits based on user query.  
I tried creating separate functi
ons and used tools to manage the functions like gross\_margin, revenue turn out etc. Yet the results are not as expected
.  
Is there any other way of going about with this.

Also I have another thought, is it possible for us to extract tabl
es from the documents in CSV format so that I can query the CSV for calculations.

  
Edit:  
I created separate functio
ns for mathematical calculations and assigned tools to call that particular function and created agents to handle those 
tools, so based on the query the respective tool is to be called in turn which calls the respective functions for carryi
ng out the calculations.  
The responses weren't as expected. As in didn't obtain any.
```
---

     
 
all -  [ [D] How are folks building conversational Retrieval Augmented Generation apps ](https://www.reddit.com/r/MachineLearning/comments/1ftdby7/d_how_are_folks_building_conversational_retrieval/) , 2024-10-03-0912
```
I've read through various resources such as:  
- [https://vectorize.io/how-i-finally-got-agentic-rag-to-work-right/](htt
ps://vectorize.io/how-i-finally-got-agentic-rag-to-work-right/)  
- [https://python.langchain.com/docs/tutorials/qa\_cha
t\_history/](https://python.langchain.com/docs/tutorials/qa_chat_history/)  
- [https://langchain-ai.github.io/langgraph
/tutorials/rag/langgraph\_agentic\_rag/](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/) 
 
- [https://docs.llamaindex.ai/en/stable/module\_guides/deploying/chat\_engines/](https://docs.llamaindex.ai/en/stable/
module_guides/deploying/chat_engines/)  
- [https://huggingface.co/datasets/nvidia/ChatRAG-Bench](https://huggingface.co
/datasets/nvidia/ChatRAG-Bench) 

But these feel overly reductive, since they don't address complexities like:  
1) when
 to retrieve vs. just respond immediately to reduce latency  
2) rely on existing context previously retrieved in the co
nversation instead of retrieving again at the current turn  
3) partition LLM context between retrieved information and 
past conversation history.

I'm sure some teams already have good systems for this, would appreciate pointers!
```
---

     
 
all -  [ How to know what agent architectures to use in Langgraph? ](https://www.reddit.com/r/LangChain/comments/1ftazvm/how_to_know_what_agent_architectures_to_use_in/) , 2024-10-03-0912
```
I have been using Langgraph for quite some time now and was wondering how you should think/choose between what architect
ures to use.

I believe this is an issue, mainly because when there are different ways of doing things, most people (inc
luding myself) tend to over-optimise their use case. For example, using hierarchical agent teams instead of using a simp
ler plan and solve architecture, that uses less tokens than you require for your use case. 

Would love to hear how othe
rs may go about this!
```
---

     
 
all -  [ Does anyone know when Langgraph Cloud will be out of beta? ](https://www.reddit.com/r/LangChain/comments/1ft520j/does_anyone_know_when_langgraph_cloud_will_be_out/) , 2024-10-03-0912
```
Hey, I think Langgraph is amazing and would like to use it alongside Langgraph Studio and Langgraph Cloud. Langgraph Clo
ud is currently in beta and not available to free users. 

Does anyone know when they will get Langgraph Cloud out of be
ta and whether or not they will be available to free users?
```
---

     
 
all -  [ Some help with UnstructuredLoader ](https://www.reddit.com/r/LangChain/comments/1ft1noj/some_help_with_unstructuredloader/) , 2024-10-03-0912
```
I am working with UnstructuredLoader, for loading PDFs, but I am having this error, and I have run out of ideas.

Here i
s my code and the error: 

https://preview.redd.it/6uhbpaz9hzrd1.png?width=885&format=png&auto=webp&s=49cd650fe2805d40b4
d73c887749ca700c89b366

    from langchain_unstructured import UnstructuredLoader
    
    
    file_path = './reports/c
otswold2-512313_207882.pdf'
    
    loader = UnstructuredLoader(
        file_path=file_path,
        strategy='hi_res'
,
        partition_via_api=False,
        coordinates=False,
    )
    
    docs = []
    for doc in loader.lazy_load()
:
        docs.append(doc)
```
---

     
 
all -  [ About using tools in langgraph  ](https://www.reddit.com/r/LangChain/comments/1fsx8at/about_using_tools_in_langgraph/) , 2024-10-03-0912
```
I have a question regarding using tools in agents that how would a LLM decide if it has to go to which the tool is conne
ct with it for example if I ask questions about something happened in 2024 and i had already connected to search tool li
ke tavily then how would LLM decide if he has to give answer which might be wrong or has to go with tools and then respo
nse it back.
```
---

     
 
all -  [ Any Langchain discord server?  ](https://www.reddit.com/r/LangChain/comments/1fstyus/any_langchain_discord_server/) , 2024-10-03-0912
```
Is there official Langchain discord server where people can ask questions or solve there code queries ? 
```
---

     
 
all -  [ LangGraph: interactive sequential tool calling ](https://www.reddit.com/r/LangChain/comments/1fst8i4/langgraph_interactive_sequential_tool_calling/) , 2024-10-03-0912
```
Hello everyone,

I'm building an AI assistant for our app, trying to instruct the LLM in a conversation, I ask it to cre
ate a project and a task for example in the database using the tools I defined. Assuming the process has several steps. 
I want the LLM to walk me through it and ask me for the required inputs to the tools. 

sample conversation I want:

- U
ser: Create a project  
- tool calling step  
- AI: what's the name of the project

- User: the project name is X

- AI:
 what are the names of the tasks that this project require in order to complete  
- User: one task named Y

  
Will prov
iding a ChatPrompt be sufficient to achieve this behavior or something else? 
```
---

     
 
all -  [ Streaming chatbot ](https://www.reddit.com/r/LangChain/comments/1fsr2g3/streaming_chatbot/) , 2024-10-03-0912
```
Hi everyone.

I made a chatbot to chat with my SQL data following this tutorial: https://python.langchain.com/docs/tutor
ials/sql_qa/

I used create_react_agent from langgraph. I am using React as my frontend and FastAPI as my backend. It wo
rks fine, but I want to stream the responses (aka the final answer) from the agent on my frontend. Is there any way to d
o that? I tried streaming on the backend following the various how-tos on langgraph, but I want to be able to stream on 
my frontend. 

Thanks a lot. 
```
---

     
 
all -  [ Ragflow vs kotaemon ](https://www.reddit.com/r/LangChain/comments/1fsql3a/ragflow_vs_kotaemon/) , 2024-10-03-0912
```
For those that have tried both, which of these worked better when training on your documents, which had a better experie
nce setting up locally?
```
---

     
 
all -  [ I made MVP just 15 days as a side project ](https://www.reddit.com/r/SideProject/comments/1fsppnz/i_made_mvp_just_15_days_as_a_side_project/) , 2024-10-03-0912
```
Hello everyone,

I am thrilled to announce that I will be undertaking the creation of my first project, [SubGPT.ai](http
s://SubGPT.ai), which involves building a chatbot for websites. Despite the challenges, I am determined to complete this
 project within a short timeframe of just 15 days.

Project Name: AI No Chatbot Builder with Your Own Data

Project Link
: [https://subgpt.ai](https://subgpt.ai/)

* Project Stack: Backend: Python Django, Django Rest Framework. 
* Frontend: 
HTML, CSS, JavaScript, Bootstrap 5. 
* Version Control: Git, GitHub.
* Auto Deployment: GitHub Actions.
* AI Model: Open
AI, Langchain Models, Google Gemini
* Payment Gateway (Lemon squeezy)

Features:

↳ Easy-to-build GPTs for multiple appl
ications

↳ Upload Your PDF to train your Chatbot

↳ Seamless integrations (WordPress, WhatsApp, WebFlow, Bubble, Weebly
)

↳ Advanced capabilities: multi-language support, personalized responses, and more

↳ API Integration

↳ Lead Generati
ons

↳ Make Real-Time Virtual Customer Supported Chatbot and more

  

```
---

     
 
all -  [ Has prompt chaining been proven to work better than just one larger stepwise prompt? ](https://www.reddit.com/r/LocalLLaMA/comments/1fsj4ww/has_prompt_chaining_been_proven_to_work_better/) , 2024-10-03-0912
```
I know prompt chaining is basically the standard at this point and there are popular libraries such as LangChain that pr
omote this approach. However, especially with the larger context windows nowadays, is it necessary or does it lead to be
tter results to break a prompt up into multiple requests and chain them together? Found this [study](https://arxiv.org/h
tml/2406.00507v1#:~:text=This%20paper%20is%20dedicated%20to,produce%20a%20more%20favorable%20outcome) on prompt chaining
 vs a stepwise prompt. They seem to have concluded prompt chaining can produce a more favorable outcome, but they only e
xperimented on a text summarization task. Do you guys have any insights on this or if I am missing something?
```
---

     
 
all -  [ Arg `k` in `BufferWindowMemory`? ](https://www.reddit.com/r/LangChain/comments/1fshldy/arg_k_in_bufferwindowmemory/) , 2024-10-03-0912
```
Hi,

It looks like they removed this argument from 0.2 to 0.3 of Langchain JS. But I am curious, the API docs have no re
al description. But what is the `k` arg used for in the `BufferWindowMemory` class which is only in 0.2 

[BufferWindowM
emory 0.2 Docs](https://v02.api.js.langchain.com/classes/langchain.memory.BufferWindowMemory.html)

It looks like they h
ave a new class called `BufferMemory` for 0.3 without the `k` arg.

Any insight would be much appreciated.

Thanks!
```
---

     
 
all -  [ Amazon Bedrock Knowledge Bases as Agent Tool ](https://www.reddit.com/r/aws/comments/1fshbxj/amazon_bedrock_knowledge_bases_as_agent_tool/) , 2024-10-03-0912
```
Hello all, 

  
I am wondering if you had implemented Amazon KB as tool using Langchain, and also how do you manage the 
conversation history with it ?

  
I have a use case where I need a RAG to talk with documents and also the AI to query 
a SQL database, I was thinking in use KB as one tool and sql as other tool, but I am not sure if make sense to use KB or
 not, the main benefit that it will bring are the default connectors with web scrapper, sharepoint, etc.

Also, it seems
 that the conversation history are saved in memory and not persistent storage, I have build other AI apps where I use Dy
namodb to store the conversation history, but since KB manages internally the context of the conversation not sure how I
 would persist the conversation and send it to have the conversation across sessions.
```
---

     
 
all -  [ Attempting to build a knowledge base for storing LLM outputs. Feedback welcome! ](https://www.reddit.com/r/LLMDevs/comments/1fsfozx/attempting_to_build_a_knowledge_base_for_storing/) , 2024-10-03-0912
```
Hi everyone,

I would never have put myself into the category of 'developer' as it's not my job.

'Open source enthusias
t' for sure. But this sub keeps cropping up in my searches so I thought it would be worth sharing what I'm working on.


I began getting really into using various LLMs earlier this year for both professional and personal reasons.

While I th
ink that the advance of LLMs is exhilarating and amazing, my thoughts began turning to the rather mundane problem of sto
rage and data sovereignty. 

Namely ... I'm getting increasingly more useful outputs from the web UIs... what am I going
 to do with them? Can I back up all my outputs incrementally? How independent is this chunk of data from the platform I'
m using (Also: can I add tags? Seemingly not! Can I search through them? Nope!)

I had a couple of weeks in semi-vacatio
n mode so just before I left I set up a Postgres database with the idea of kickstarting a project to build some kind of 
organisation system. 

Over the course of the summer I built up a decent relational database. I gravitated around the id
ea of the system having four core modules: prompts, outputs, agents, and contexts (agent = custom LLM configs rather tha
n fine-tuning whole models). The contextual module is my latest addition:  it's a store of morsels of information that c
an be dropped into new LLMs whenever you need to quickly bring them up to 'speed' on a project or provide a set of found
ational facts. I'm sure more will come to mind.

There are a bunch of M2Ms and O2Ms relating everything together: prompt
s are associated with outputs (a conversation module is inevitably but right now multiple outputs are simply associated 
with the initial prompt); outputs and prompts with agents; and there are a few custom taxonomies like 'tags' and 'accura
cy ratings'.

My objective was (and is) to build out something like a 'workbench' . The collected outputs are 'raw mater
ial'. They get annotated, tagged with metadata, and in some cases edited carefully by a human. After that, they're store
d and managed just like any other piece of reference knowledge. I use LLMs intensively and routinely for stack research 
and this is one of the use-cases I have in mind. But there are countless. 

For want of a proper UI, my initial system d
esign was simply using NocoDB over the database and manually inputting prompts and outputs. Latterly, I've begun using L
LMs via their APIs. My offline prototype handles this perfectly: a prompt is collected, saved to that table. The API ret
urns its output output, and it gets saved to the output table. Finally, the relationship between the two is set down in 
the conventional method (ie, by writing foreign key values to a join table). (This also works in Obsidian but as much as
 I like the tool I don't think it's the right architecture for this)

Oddly enough, the part of this project I thought w
e be easiest (building a frontend) is proving the hardest. It bugs me to do this, but I'm 'dumbing down' the database ba
ck to its essential elements in order to make defining the schema into an ORM a lot easier.

Other things I've been chec
king out? MongoDB seemed interesting but ultimately I stuck with Postgres. Vector databases and graph databases .. intri
guing possibilities. LangChain ... I'm almost certain this could make developing this easier and it's on my radar to loo
k into it. 

Ultimately, it's a CRUD app that is honed in on working with LLMs and specifically trying to address the ve
ry neglected topic of output management: how to manage and refine the outputs so that they can be as valuable as possibl
e. 

The essential task for me is making sure that the database and storage buckets (for files etc) can be set by the us
er. The philosophy underpinning this is that LLMs are amazing. But prompt engineering and context-refinement aren't the 
only things we need to do to leverage them; we also need to figure out workflows and best practices for owning and then 
managing their outputs. 

It's a personal project that I'm using as an excuse to dive into the fascinating world of LLMs
. My note are open source and if I can ever get something robust enough that can be shared, I will absolutely put them o
ut there. For now, I'm enjoying plodding along. 

Critiques and thoughts welcome!
```
---

     
 
all -  [ Best open source RAG for 100s of PDFs ? ](https://www.reddit.com/r/LangChain/comments/1fsd1yw/best_open_source_rag_for_100s_of_pdfs/) , 2024-10-03-0912
```
I have 100-200 PDFs that I want to be able to ask and answer questions about. Most of the solutions I see are about Llam
aparse or 1000 other tools that are all closed source. If I wanted to do this without my data going anywhere, what appro
ach or guide/resource would you recommend? I’ve already converted all my documents to markdown using marker, just not su
re how to proceed from there effectively.


```
---

     
 
MachineLearning -  [ Built a web agent which call fill Google forms based on the user details [P] ](https://www.reddit.com/r/MachineLearning/comments/1fozud5/built_a_web_agent_which_call_fill_google_forms/) , 2024-10-03-0912
```
GitHub repo : [https://github.com/shaRk-033/web-agent](https://github.com/shaRk-033/web-agent)

Tried to solve it using 
two approaches:

# 1: Basic Scraping and Filling

This is the straightforward approach. The agent scrapes the form’s HTM
L and uses fixed XPaths to find and fill in the required fields.

* It pulls the form’s HTML, locates the fields with se
t XPaths, and inputs the answers. It’s a direct and simple method.
* If the form changes or an element isn’t where it’s 
expected, the process can fail and may need manual adjustments.

[basic approach](https://preview.redd.it/5e8g4a1k4xqd1.
png?width=1055&format=png&auto=webp&s=d8e984e4feaee2f0453b08c8696768c40a2a5c20)

2. Using LangChain Agents and tool call
ing

* LangChain Agent**:** The agent handles everything by using the LLM’s reasoning to decide what to do next, includi
ng generating those tricky XPaths.
* Error Handling**:** If something goes wrong (like an element not found), the agent 
tries again with better XPaths until it gets the job done.

[using langchain agents](https://preview.redd.it/948i88pl4xq
d1.png?width=782&format=png&auto=webp&s=ed1e6c19efec9f4cbbbd6ab5a22558f221cf745f)

Any recommendations to improve this w
ould be welcome. Also, if anyone has ideas on building similar web agents to automate other tasks, it would be great to 
hear them. :)
```
---

     
 
MachineLearning -  [ [P] Swapping Embedding Models for an LLM ](https://www.reddit.com/r/MachineLearning/comments/1fktvbj/p_swapping_embedding_models_for_an_llm/) , 2024-10-03-0912
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

     
 
MachineLearning -  [ [P] Review and suggest ideas for my chatbot ](https://www.reddit.com/r/MachineLearning/comments/1fb2mwl/p_review_and_suggest_ideas_for_my_chatbot/) , 2024-10-03-0912
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

     
 
MachineLearning -  [ [P] Lessons from Retrieval Augmented Generation ](https://www.reddit.com/r/MachineLearning/comments/1f9tvg7/p_lessons_from_retrieval_augmented_generation/) , 2024-10-03-0912
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

     
 
deeplearning -  [ What is the best approach for Parsing and Retrieving Code Context Across Multiple Files in a Hierarc ](https://www.reddit.com/r/deeplearning/comments/1fh58oz/what_is_the_best_approach_for_parsing_and/) , 2024-10-03-0912
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

     
 
deeplearning -  [ Month of August in AI ](https://www.reddit.com/r/deeplearning/comments/1f6zfz0/month_of_august_in_ai/) , 2024-10-03-0912
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

     
