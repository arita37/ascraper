 
all -  [ Aider + langchain: A match made in heaven? ](https://www.reddit.com/r/LocalLLaMA/comments/1hczbla/aider_langchain_a_match_made_in_heaven/) , 2024-12-13-0914
```
 🚀

Hey everyone! In the spirit of r/localllama, I wanted to share a little experiment I’ve been working on: [RA.Aid](ht
tps://github.com/ai-christianson/RA.Aid). This started after Windsurf announced their pricing changes, and I kept runnin
g into its limits—usage caps, unreliability, and cost. I thought, why not try building something together that combines 
the best parts of aider and LangChain to handle programming tasks more effectively?

RA.Aid is an experiment to make aid
er a tool for a LangChain agent. The agent explores your codebase, finds key facts, files, and snippets for your task, a
nd can even ask tough questions using o1-preview. It’s been exciting to see how well it works with tools like:  
- **Fil
e exploration tools** for navigating projects.  
- **Fuzzy find + ripgrep** for quickly locating key snippets.  
- An op
tional **cowboy 🤠 mode** that lets the agent automatically run shell commands (if you’re feeling adventurous).  

So far
, it has been performing better for the tasks I’ve tested it on, especially complex ones. Right now, it’s set up with so
me of the strongest models available (like Claude and o1-preview). However, it should work well with open models too, th
ough we’ll probably need to do more prompting work and add configurability to make it really effective.  

If we can get
 some PRs rolling in, we might be able to create a completely free and open tool that far surpasses even $500/month prop
rietary solutions like Devin. The code is up on GitHub under Apache 2.0: [RA.Aid](https://github.com/ai-christianson/RA.
Aid).

Happy to hear any thoughts or feedback from the community!
```
---

     
 
all -  [ Token limit challenge with large tool/function calling response ](https://www.reddit.com/r/LangChain/comments/1hcwrzk/token_limit_challenge_with_large_toolfunction/) , 2024-12-13-0914
```
Hi everyone, 

  
I'm currently building application with function calling using langchain/langgraph. Tool calling funct
ionality works well in general but some of my tools make call to 3rd party search API, which often return huge JSON resp
onse body. In the scenario when multiple search requests needs to be called, and all tool calling search responses need 
to pass to invoke AI model to generate AI response, I quickly run into token limit for AI model. Does anyone has any exp
erience with handling huge tool calling response and has some solution that can optimize? 

  
I have considered few way
s 

(1) In tool calling, after getting response from 3rd party search API, before returning back to my main agent, I cal
l AI model to summary my search API response. However, this results into loss of information from the original search re
sponse which eventually leads to poor final AI response

(2) In tool calling, after getting response from 3rd party sear
ch API, transform the response into documents, save it as embedding and search for the most relevant document, return to
 the main agent. However, this search within search sounds really inefficient consider search API might already return r
esults with high relevance? 
```
---

     
 
all -  [  CommanderAI / LLM-Driven Action Generation on Windows with Langchain (openai) ](https://www.reddit.com/r/OpenAIDev/comments/1hcwok1/commanderai_llmdriven_action_generation_on/) , 2024-12-13-0914
```
Hey everyone,

I’m sharing a project I worked on some time ago: a LLM-Driven Action Generation on Windows with Langchain
 (openai). An automation system powered by a Large Language Model (LLM) to understand and execute instructions. The idea
 is simple: you give a natural language command (e.g., “Open Notepad and type ‘Hello, world!’”), and the system attempts
 to translate it into actual actions on your Windows machine.

**Key Features:**

* **LLM-Driven Action Generation:** Th
e system interprets requests and dynamically generates Python code to interact with applications.
* **Automated Windows 
Interaction:** Opening and controlling applications using tools like pywinauto and pyautogui.
* **Screen Analysis & OCR:
** Capture and analyze the screen with Tesseract OCR to verify UI states and adapt accordingly.
* **Speech Recognition &
 Text-to-Speech:** Control the computer with voice commands and receive spoken feedback.

**Current State of the Project
:**  
This is a proof of concept developed a while ago and not maintained recently. There are many bugs, unfinished feat
ures, and plenty of optimizations to be done. Overall, it’s more a feasibility demo than a polished product.

**Why Shar
e It?**

* If you’re curious about integrating an LLM with Windows automation tools, this project might serve as inspira
tion.
* You’re welcome to contribute by fixing bugs, adding features, or suggesting improvements.
* Consider this a star
ting point rather than a finished solution. Any feedback or assistance is greatly appreciated!

**How to Contribute:**


* The source code is available on GitHub (link in the comments).
* Feel free to fork, open PRs, file issues, or simply u
se it as a reference for your own projects.

**In Summary:**  
This project showcases the potential of LLM-driven Window
s automation. Although it’s incomplete and imperfect, I’m sharing it to encourage discussion, experimentation, and hopef
ully the emergence of more refined solutions!

Thanks in advance to anyone who takes a look. Feel free to share your tho
ughts or contributions!  


[https://github.com/JacquesGariepy/CommanderAI](https://github.com/JacquesGariepy/CommanderA
I)


```
---

     
 
all -  [ multi RAG issue ](https://www.reddit.com/r/LangChain/comments/1hcvpmy/multi_rag_issue/) , 2024-12-13-0914
```
Hi everyone, I need your help. I'm working on a multi-profile RAG using RetrievalQA, FAISS, and Chainlit. Recently, whil
e testing, I encountered an issue with memory usage.

I have 5 chat profiles in Chainlit, each linked to a different vec
tor database. When I select a chat profile and load its corresponding vector database, memory usage increases as expecte
d. However, when I close that chat profile, the memory usage does not decrease.

Does anyone know how to solve this issu
e? Is there a function to properly close or unload vector databases in RetrievalQA? Or perhaps a way to terminate the Re
trievalQA process and free up memory?
```
---

     
 
all -  [ How to clone any Twitter personality into an AI (your move, Elon) 🤖 ](https://www.reddit.com/r/LangChain/comments/1hcrjfp/how_to_clone_any_twitter_personality_into_an_ai/) , 2024-12-13-0914
```
The LangChain team dropped this gem showing how to build AI personas from Twitter/X profiles using LangGraph and Arcade.
 It's basically like having a conversation with someone's Twitter alter ego, minus the blue checkmark drama.

Key featur
es:

* Uses long-term memory to store tweets (like that ex who remembers everything you said 3 years ago)
* RAG implemen
tation that's actually useful and not just buzzword bingo
* Works with any Twitter profile (ethics left as an exercise f
or the reader)
* Uses Arcade to integrate with Twitter/X
* Clean implementation that won't make your eyes bleed

Video t
utorial shows full implementation from scratch. Perfect for when you want to chat with tech Twitter without actually goi
ng on Twitter.

[https://www.youtube.com/watch?v=rMDu930oNYY](https://www.youtube.com/watch?v=rMDu930oNYY)

P.S. No GPTs
 were harmed in the making of this tutorial.
```
---

     
 
all -  [ [For Hire] Title [For Hire] Experienced AI/ML, Full Stack, and DevOps Developer – Ready to Tackle Yo ](https://www.reddit.com/r/forhire/comments/1hcpvx4/for_hire_title_for_hire_experienced_aiml_full/) , 2024-12-13-0914
```
🚀 **Your One-Stop Solution for AI/ML, Full Stack Development, and DevOps!**

Hey, I'm Sheryar! 👋 I'm an experienced **AI
/ML Engineer**, **Full Stack Developer**, and **DevOps Specialist**. If you're looking to bring your ideas to life with 
scalable, high-performance solutions, I can help!

💻 **Full Stack Development**

* Beautiful UIs: React | Angular
* Powe
rful APIs: Node.js | NestJS
* Easy Payment Integration: Stripe
* Cloud Infrastructure: AWS | GCP

🤖 **AI & Machine Learn
ing**

* Smart Chatbots with LangChain
* Custom AI Models for NLP, Automation, & More

⚙️ **DevOps Solutions**

* CI/CD 
Pipelines with GitHub Actions | Jenkins
* Containerization with Docker | Kubernetes
* Infrastructure as Code: Terraform 
| Ansible
* Monitoring Tools: Prometheus | Grafana

🌟 **Recent Projects**

* 🚗 Ride-Sharing: Real-time vehicle tracking 
& payments
* 📦 Logistics: Multi-stop delivery route optimization
* 🛒 E-Commerce: Scalable Kubernetes clusters for high-t
raffic apps

💰 **Rates**: $20–$25/hour (negotiable)  
📧 **Let's talk!** DM me to discuss your project!

🔗 **GitHub**: [s
torm1033](https://github.com/storm1033)

Let’s collaborate and build something amazing! 🌐✨
```
---

     
 
all -  [ What happened to Conversational Retrieval QA? ](https://www.reddit.com/r/LangChain/comments/1hcpf6v/what_happened_to_conversational_retrieval_qa/) , 2024-12-13-0914
```
Once upon a time in the v0.1 days there was this idea of \[Conversational Retrieval QA\](https://js.langchain.com/v0.1/d
ocs/modules/chains/popular/chat\_vector\_db\_legacy/).  You can see the docs on this webpage, but if you click the link 
to go to the current stable version it doesn't seem to exist anymore.

Does anyone know if this got absorbed into someth
ing else less obvious or did they just drop support for it?
```
---

     
 
all -  [ Not able to generate embeddings ](https://www.reddit.com/r/learnmachinelearning/comments/1hcp5ht/not_able_to_generate_embeddings/) , 2024-12-13-0914
```
I am using Langchain and google generative AI to generate embeddings of the document, however I am encountering Error 40
3 ->  
langchain\_google\_genai.\_common.GoogleGenerativeAIError: Error embedding content: 403 Request had insufficient 
authentication scopes. \[reason: 'ACCESS\_TOKEN\_SCOPE\_INSUFFICIENT'

    import os
    from dotenv import load_dotenv

    from langchain_google_genai import ChatGoogleGenerativeAI
    from langchain_community.vectorstores import Chroma
  
  from langchain_google_genai import GoogleGenerativeAIEmbeddings
    from langchain.text_splitter import CharacterTextS
plitter
    from langchain_community.document_loaders import TextLoader
    import google.generativeai as genai
    
   
 
    load_dotenv()
    api_key = os.getenv('GEMINI_API_KEY')
    
    
    model = ChatGoogleGenerativeAI(model = 'gemi
ni-1.5-pro',api_key=api_key)
    
    
    genai.configure(api_key=api_key)
    
    current_working_directory = os.getc
wd()
    file_path = os.path.join(current_working_directory,'books/odyssey.txt')
    
    storing_directory = os.path.jo
in(current_working_directory,'db','chroma_db')
    
    
    if not os.path.exists(storing_directory):
        print('St
oring directory does not exist..Initializing a vector store.......\n')
        if not os.path.exists(file_path):
       
     raise FileNotFoundError(f'The {file_path} could not be found.\n')
        # read the content from the file
        
loader = TextLoader(file_path)
        document = loader.load()
    
        # create chunks
        text_splitter = Cha
racterTextSplitter(chunk_size=1000,chunk_overlap=0)
        docs = text_splitter.split_documents(document)
    
        
# Display Info
        print('\n------------Document Chunk Info----------------\n')
        print(f'Number of document c
hunks----> {len(docs)}')
        print(f'Sample Chunk---->\n{docs[0].page_content}\n')
    
        # create embeddings

        print('\n------------creating embeddings----------------\n')
        embeddings = GoogleGenerativeAIEmbeddings(m
odel = 'models/embedding-001',api_key=api_key)
        print('\n--------------finished creating embeddings-------------\
n')
    
        # vector store
        print('\n--------------Creating vector store-------------\n')
        db = Chrom
a.from_documents(
            documents=docs,
            embedding=embeddings,
            persist_directory=storing_di
rectory
        )
        print('\n--------------finished creating vector store-------------\n')
    
    else:
        
print('-----------------vector store already exists')
    
    

Somebody please help I been stuck here for last 2 hours
  

```
---

     
 
all -  [ Not able to generate embeddings ](https://www.reddit.com/r/generativeAI/comments/1hcp3y0/not_able_to_generate_embeddings/) , 2024-12-13-0914
```
I am using Langchain and google generative AI to generate embeddings of the document, however I am encountering Error 40
3 ->  
langchain\_google\_genai.\_common.GoogleGenerativeAIError: Error embedding content: 403 Request had insufficient 
authentication scopes. \[reason: 'ACCESS\_TOKEN\_SCOPE\_INSUFFICIENT'

Somebody please help I been stuck here for last 2
 hours

    import os
    from dotenv import load_dotenv
    from langchain_google_genai import ChatGoogleGenerativeAI
 
   from langchain_community.vectorstores import Chroma
    from langchain_google_genai import GoogleGenerativeAIEmbeddin
gs
    from langchain.text_splitter import CharacterTextSplitter
    from langchain_community.document_loaders import Te
xtLoader
    import google.generativeai as genai
    
    
    load_dotenv()
    api_key = os.getenv('GEMINI_API_KEY')
 
   
    
    model = ChatGoogleGenerativeAI(model = 'gemini-1.5-pro',api_key=api_key)
    
    
    genai.configure(api_
key=api_key)
    
    current_working_directory = os.getcwd()
    file_path = os.path.join(current_working_directory,'bo
oks/odyssey.txt')
    
    storing_directory = os.path.join(current_working_directory,'db','chroma_db')
    
    
    if
 not os.path.exists(storing_directory):
        print('Storing directory does not exist..Initializing a vector store....
...\n')
        if not os.path.exists(file_path):
            raise FileNotFoundError(f'The {file_path} could not be fou
nd.\n')
        # read the content from the file
        loader = TextLoader(file_path)
        document = loader.load()

    
        # create chunks
        text_splitter = CharacterTextSplitter(chunk_size=1000,chunk_overlap=0)
        doc
s = text_splitter.split_documents(document)
    
        # Display Info
        print('\n------------Document Chunk Info
----------------\n')
        print(f'Number of document chunks----> {len(docs)}')
        print(f'Sample Chunk---->\n{do
cs[0].page_content}\n')
    
        # create embeddings
        print('\n------------creating embeddings---------------
-\n')
        embeddings = GoogleGenerativeAIEmbeddings(model = 'models/embedding-001',api_key=api_key)
        print('\
n--------------finished creating embeddings-------------\n')
    
        # vector store
        print('\n--------------
Creating vector store-------------\n')
        db = Chroma.from_documents(
            documents=docs,
            embed
ding=embeddings,
            persist_directory=storing_directory
        )
        print('\n--------------finished creat
ing vector store-------------\n')
    
    else:
        print('-----------------vector store already exists')
    

My 
code->  

```
---

     
 
all -  [ Any alternatives to LangChain for LLMs/GraphRAG on RDF graphs? ](https://www.reddit.com/r/KnowledgeGraph/comments/1hcozn1/any_alternatives_to_langchain_for_llmsgraphrag_on/) , 2024-12-13-0914
```
Hello. I am getting more into GraphRAG. This year a project I was involved with transformed a large RDF graph into Neo4j
 (via Neosemantics), and from there I used LangChain and our in-house AI models to do GraphRAG things, with great result
s. I proved that this approach gave much better answers (because of kg context) than traditional RAG. Shoutout to Jesus 
Barrasa, for both his Neo4j semantic expertise, and the 'Going Meta' YouTube series which I highly recommend.     
  
Ho
wever, I am at the end of the day an ontologist, and we have tons of RDF ontologies, with no interest in (or resources f
or) transforming all of those into Neo4j graphs. I've looked into how to do things directly with RDF and it's not an enc
ouraging landscape.  
  
LangChain can do things through RdfGraph, but it's mostly based on rdflib, whereas 'knowledge g
raph' support from tons of frameworks is super robust. The SparqlQAChain is neat, since you can directly see what SPARQL
 query the LLM is composing to try to answer the question. But I don't actually care about knowledge graph generation, w
hich is unfortunately what so much tooling is built around. I already have everything highly structured within a defined
 domain! Once it gets to actual RAG, the usual vector similarity search rears its ugly head, and isn't GraphRAG, and wou
ld actually be a terrible strategy for already-structured data.   
  
So, has anyone been in this same position of needi
ng to do GraphRAG things directly on RDF data (i.e., use vectorization but merely as a pre/post filtering mechanism, but
 ground all answers in the knowledge graph), but have used things OTHER than LangChain?  
```
---

     
 
all -  [ ChatPDF and PDF.ai are making millions using open source tech... here's the code ](https://www.reddit.com/r/Entrepreneur/comments/1hcm180/chatpdf_and_pdfai_are_making_millions_using_open/) , 2024-12-13-0914
```
# Why 'copy' an existing product?

The best SaaS products weren’t the first of their kind - think Slack, Shopify, Zoom, 
Dropbox, or HubSpot. They didn’t invent team communication, e-commerce, video conferencing, cloud storage, or marketing 
tools; they just made them better.

# What is a 'Chat with PDF' SaaS?

These are AI-powered PDF assistants that let you 
upload a PDF and ask questions about its content. You can summarize articles, extract key details from a contract, analy
ze a research paper, and more.

# Let's look at the market

Made possible by advances in AI like ChatGPT and Retrieval-A
ugmented Generation (RAG), PDF chat tools started gaining traction in early 2023 and have seen consistent growth in mark
et interest, which is currently at an all-time high (source: google trends)

Keywords like 'chat PDF' and 'PDF AI' get b
etween 1 to 10 million searches every month (source:keyword planner), with a broad target audience that includes researc
hers, students, and professionals across various industries.

Leaders like PDF.ai and ChatPDF have already gained millio
ns of users within a year of launch, driven by the growing market demand, with paid users subscribing at around $20/mont
h.

# Alright, so how do we build this with open source?

The core tech for most PDF AI tools are based on the same arch
itecture. You generate text embeddings (AI-friendly text representations; usually via OpenAI APIs) for the uploaded PDF’
s chapters/topics and store them in a vector database (like Pinecone/pgvector).

Now, every time the user asks a questio
n, a similarity search is performed to find the most similar PDF topics from the vector database. The selected topic con
tents are then sent to an LLM (like ChatGPT) along with the question, which generates a contextual answer!

Here are som
e of the best open source implementations for this process (source: GitHub):

* GPT4 & LangChain Chatbot for large PDF d
ocs by Mayo Oshin
* MultiPDF Chat App by Alejandro AO
* PDFToChat by Hassan El Mghari

Worried about building signups, u
ser management, payments, etc.? Here are my go-to open-source SaaS boilerplates that include everything you need out of 
the box (source: GitHub):

* SaaS Boilerplate by Remi Wg
* Open SaaS by wasp-lang

You can **check out the hyperlinks in
 the first comment, or look em up on google** (they're quite popular).

# A few ideas to stand out from the noise:

Here
 are a few strategies that could help you differentiate and achieve product market fit (based on the pivot principles fr
om The Lean Startup by Eric Ries):

1. **Narrow down your target audience for a personalized UX:** For instance, an exam
 prep assistant for students with study notes and quiz generator; or a document due diligence and analysis tool for lawy
ers.
2. **Add unique features to increase switching cost:** You could autogenerate APIs for the uploaded PDFs to enable 
remote integrations (eg. support chatbot knowledge base); or build in workflow automation features for bulk analyses of 
PDFs.
3. **Offer platform level advantages:** You could ship a native mobile/desktop apps for a more integrated UX; or (
non-trivial) offer private/offline support by replacing the APIs with local open source deployments (eg. llama for LLM, 
an embedding model from the MTEB list, and FAISS for vector search).

**TMI?** I’m an ex-AI engineer and product lead, s
o don’t hesitate to reach out with any questions!

Thanks for reading! this was the first post on my new weekly newslett
er (link in first comment) which covers open-source/turnkey resources behind popular products (like this one). Feel free
 to bring up other products you'd like me to analyze or any other aspects you'd like to learn about in future posts.
```
---

     
 
all -  [ ChatPDF and PDF.ai are making millions using open source tech... here's the code ](https://www.reddit.com/r/microsaas/comments/1hckxwo/chatpdf_and_pdfai_are_making_millions_using_open/) , 2024-12-13-0914
```
# Why 'copy' an existing product?

The best SaaS products weren’t the first of their kind - think Slack, Shopify, Zoom, 
Dropbox, or HubSpot. They didn’t invent team communication, e-commerce, video conferencing, cloud storage, or marketing 
tools; they just made them better.

# What is a 'Chat with PDF' SaaS?

These are AI-powered PDF assistants that let you 
upload a PDF and ask questions about its content. You can summarize articles, extract key details from a contract, analy
ze a research paper, and more. To see this in action or dive deeper into the tech behind it, check out this [YouTube vid
eo.](https://www.youtube.com/watch?v=ih9PBGVVOO4)

# Let's look at the market

Made possible by advances in AI like Chat
GPT and Retrieval-Augmented Generation (RAG), PDF chat tools started gaining traction in early 2023 and have seen consis
tent growth in market interest, which is currently at an all-time high (source:[google trends](https://trends.google.com
/trends/explore?date=today%205-y&q=pdf%20chat,pdf%20ai&hl=en-GB))

Keywords like 'chat PDF' and 'PDF AI' get between 1 t
o 10 million searches every month (source:keyword planner), with a broad target audience that includes researchers, stud
ents, and professionals across various industries.

Leaders like PDF.ai and ChatPDF have already gained millions of user
s within a year of launch, driven by the growing market demand, with paid users subscribing at around $20/month.

# Alri
ght, so how do we build this with open source?

The core tech for most PDF AI tools are based on the same architecture. 
You generate text embeddings (AI-friendly text representations; usually via OpenAI APIs) for the uploaded PDF’s chapters
/topics and store them in a vector database (like Pinecone).

Now, every time the user asks a question, a similarity sea
rch is performed to find the most similar PDF topics from the vector database. The selected topic contents are then sent
 to an LLM (like ChatGPT) along with the question, which generates a contextual answer!

Here are some of the best open 
source implementations for this process:

* [GPT4 & LangChain Chatbot for large PDF docs](https://github.com/mayooear/gp
t4-pdf-chatbot-langchain) by Mayo Oshin
* [MultiPDF Chat App](https://github.com/alejandro-ao/ask-multiple-pdfs) by Alej
andro AO
* [PDFToChat](https://github.com/Nutlope/pdftochat) by Hassan El Mghari

Worried about building signups, user m
anagement, payments, etc.? Here are my go-to open-source SaaS boilerplates that include everything you need out of the b
ox:

* [SaaS Boilerplate](https://github.com/ixartz/SaaS-Boilerplate) by Remi Wg
* [Open SaaS](https://github.com/wasp-l
ang/open-saas) by wasp-lang

# A few ideas to stand out from the noise:

Here are a few strategies that could help you d
ifferentiate and achieve product market fit (based on the pivot principles from The Lean Startup by Eric Ries):

1. **Na
rrow down your target audience for a personalized UX:** For instance, an exam prep assistant for students with study not
es and quiz generator; or a document due diligence and analysis tool for lawyers.
2. **Add unique features to increase s
witching cost:** You could autogenerate APIs for the uploaded PDFs to enable remote integrations (eg. support chatbot kn
owledge base); or build in workflow automation features for bulk analyses of PDFs.
3. **Offer platform level advantages:
** You could ship a native mobile/desktop apps for a more integrated UX; or (non-trivial) offer private/offline support 
by replacing the APIs with local open source deployments (eg. llama for LLM, an embedding model from the MTEB list, and 
FAISS for vector search).

**TMI?** I’m an ex-AI engineer and product lead, so don’t hesitate to reach out with any ques
tions!

**P.S.** I've started a free weekly [newsletter](https://saaswithcode.substack.com/p/issue-1-launch-a-saas-like-
chatpdf) to share open-source/turnkey resources behind popular products (like this one). If you’re a founder looking to 
launch your next product without reinventing the wheel, please subscribe :)
```
---

     
 
all -  [ I made a free directory of Agentic Tools ](https://www.reddit.com/r/LangChain/comments/1hckonl/i_made_a_free_directory_of_agentic_tools/) , 2024-12-13-0914
```
Hey everyone! 👋

With the rapid evolution of AI and the growing ecosystem of AI agents, finding the right tools that wor
k well with these agents has become increasingly important. That's why I created the [Agentic Tools Directory](https://d
irectory.composio.dev/) \- a comprehensive collection of agent-friendly tools across different categories.

**What is th
e Agentic Tools Directory?**

It's a curated repository where you can discover and explore tools specifically designed o
r optimized for AI agents. Whether you're a developer, researcher, or AI enthusiast, this directory aims to be your go-t
o resource for finding agent-compatible tools.

**What you'll find:**

* Tools categorized by functionality and use case

* Clear information about agent compatibility
* Regular updates as new tools emerge
* A community-driven approach to di
scovering and sharing resources

**Are you building an agentic tool?**

If you've developed a tool that works well with 
AI agents, we'd love to include it in the directory! This is a great opportunity to increase your tool's visibility with
in the AI agent ecosystem.

**How to get involved:**

1. Explore the directory
2. Submit your tool
3. Share your feedbac
k and suggestions

Let's build this resource together and make it easier for everyone to discover and utilize agent-frie
ndly tools!

Questions, suggestions, or feedback? Drop them in the comments below!
```
---

     
 
all -  [ as a fresher can i write this under my name in resume. ](https://www.reddit.com/r/IndiaTech/comments/1hcjnml/as_a_fresher_can_i_write_this_under_my_name_in/) , 2024-12-13-0914
```
also i have 3 months of work experience is it even countable as experience

https://preview.redd.it/yvdm7njsre6e1.png?wi
dth=1180&format=png&auto=webp&s=f585ecfc8b94952eecaf9c7efbaf787e0b101209


```
---

     
 
all -  [ A way in langgraph to find if the execution is completed ](https://www.reddit.com/r/LangChain/comments/1hcj99u/a_way_in_langgraph_to_find_if_the_execution_is/) , 2024-12-13-0914
```
Iam building a workflow which asks for human input for onboarding, I want to know in some way that the execution is comp
leted or ongoing so that i can use it to switch to next workflow. How can i achieve this by using interupts or by using 
a state variable
```
---

     
 
all -  [ My llm agent with tools is not converting the ToolMessage into an AI message ](https://www.reddit.com/r/LangChain/comments/1hci1do/my_llm_agent_with_tools_is_not_converting_the/) , 2024-12-13-0914
```
Hello and  a good day to you all!

I have been stuck on this issue for too long so I've decided to come and ask for your
 help. I made a graph which contains an llm agent that is connected to a tool (just one tool function for now). The tool
 loops back to the agent, but the agent never converts the ToolMessage into an AImessage to return to the user. After th
e state gets updated with the ToolMessage, the agent just calls the tool again, gets another ToolMessage, and it keeps o
n looping indefinitely.

For a clearer picture - the user wants to update his tickets in a project management database, 
and the tools return a string of user's tickets separated by a comma. The agent should reply with normal language delive
ring the tickets and asking the user to choose one to update. 

The agent is 

    ChatOpenAI(model='gpt-4o-mini', tempe
rature=0).bind_tools(self.tools)

 and get\_user\_tickets is the tool.



Any help is appreciated!

Here are my logs so 
that you can see the messages:



024-12-12 10:46:36.966 | INFO     | notion\_bot.agents.qa\_agent:run:86 - Starting QAA
gent.

2024-12-12 10:46:37.569 | INFO     | notion\_bot.agents.qa\_agent:run:105 - {'messages': \[HumanMessage(content='
update a ticket', additional\_kwargs={}, response\_metadata={}, id='be57ff2f-b79e-43d0-9ebc-eb71bd655597')\]}

2024-12-1
2 10:46:38.048 | INFO     | notion\_bot.agents.get\_user\_tickets:get\_user\_tickets:40 - \['Woohoo', 'Async', 'BlaBla'\
]

2024-12-12 10:46:38.052 | INFO     | notion\_bot.agents.qa\_agent:run:86 - Starting QAAgent.

2024-12-12 10:46:38.714
 | INFO     | notion\_bot.agents.qa\_agent:run:105 - {'messages': \[HumanMessage(content='update a ticket', additional\_
kwargs={}, response\_metadata={}, id='be57ff2f-b79e-43d0-9ebc-eb71bd655597'), AIMessage(content='', additional\_kwargs={
'tool\_calls': \[{'id': 'call\_sYlZhRQGDeUWBetTISfLP7KK', 'function': {'arguments': '{}', 'name': 'get\_user\_tickets'},
 'type': 'function'}\], 'refusal': None}, response\_metadata={'token\_usage': {'completion\_tokens': 12, 'prompt\_tokens
': 328, 'total\_tokens': 340, 'completion\_tokens\_details': {'audio\_tokens': 0, 'reasoning\_tokens': 0, 'accepted\_pre
diction\_tokens': 0, 'rejected\_prediction\_tokens': 0}, 'prompt\_tokens\_details': {'audio\_tokens': 0, 'cached\_tokens
': 0}}, 'model\_name': 'gpt-4o-mini-2024-07-18', 'system\_fingerprint': 'fp\_6fc10e10eb', 'finish\_reason': 'tool\_calls
', 'logprobs': None}, id='run-c0c944cd-bbe5-4262-ad53-7e0040069b6c-0', tool\_calls=\[{'name': 'get\_user\_tickets', 'arg
s': {}, 'id': 'call\_sYlZhRQGDeUWBetTISfLP7KK', 'type': 'tool\_call'}\], usage\_metadata={'input\_tokens': 328, 'output\
_tokens': 12, 'total\_tokens': 340, 'input\_token\_details': {'audio': 0, 'cache\_read': 0}, 'output\_token\_details': {
'audio': 0, 'reasoning': 0}}), ToolMessage(content='Woohoo, Async, BlaBla', name='get\_user\_tickets', id='58520eb1-a67b
-43b3-a030-8040e36e9027', tool\_call\_id='call\_sYlZhRQGDeUWBetTISfLP7KK')\]}

2024-12-12 10:46:39.166 | INFO     | noti
on\_bot.agents.get\_user\_tickets:get\_user\_tickets:40 - \['Woohoo', 'Async', 'BlaBla'\]

2024-12-12 10:46:39.172 | INF
O     | notion\_bot.agents.qa\_agent:run:86 - Starting QAAgent.

 
```
---

     
 
all -  [ Is it possible to update langgraph state using tool  ](https://www.reddit.com/r/LangChain/comments/1hcgxrk/is_it_possible_to_update_langgraph_state_using/) , 2024-12-13-0914
```

```
---

     
 
all -  [ Should I reuse a single LangChain ChatOpenAI instance or create a new one for each request in FastAP ](https://www.reddit.com/r/LangChain/comments/1hcf16g/should_i_reuse_a_single_langchain_chatopenai/) , 2024-12-13-0914
```
Hi everyone,

I’m currently working on a FastAPI server where I’m integrating LangChain with the OpenAI API. Right now, 
I’m initializing my `ChatOpenAI` LLM object once at the start of my Python file, something like this:

    llm = ChatOpe
nAI(
        model='gpt-4',
        temperature=0,
        max_tokens=None,
        api_key=os.environ.get('OPENAI_API_K
EY'),
    )
    prompt_manager = PromptManager('prompt_manager/second_opinion_prompts.yaml')
    

Then I use this `llm`
 object in multiple different functions/endpoints. My question is: is it a good practice to reuse this single `llm` inst
ance across multiple requests and endpoints, or should I create a separate `llm` instance for each function call?

I’m s
till a bit new to LangChain and FastAPI, so I’m not entirely sure about the performance and scalability implications. Fo
r example, if I have hundreds of users hitting the server concurrently, would reusing a single `llm` instance cause issu
es (such as rate-limiting, thread safety, or unexpected state sharing)? Or is this the recommended way to go, since crea
ting a new `llm` object each time might add unnecessary overhead?

Any guidance, tips, or best practices from your exper
ience would be really appreciated!

Thanks in advance!
```
---

     
 
all -  [ Chance me for RSI (Experienced Researcher at Ivy + Stanford)  ](https://www.reddit.com/r/summerprogramresults/comments/1hce5t6/chance_me_for_rsi_experienced_researcher_at_ivy/) , 2024-12-13-0914
```
Chance me for RSI:   
  
Essentially my ECS + Test scores: 

**Test Scores:** 

1510 PSAT

1550 SAT

**STEM ECS:**   
\-
 Global Finals Qualifier for VEX Robotics Competition. Programmer for the team 5327A. (2023)

\- Currently Captain of th
e MATE ROV Competition club at school

Academic Research

Researcher at Brown University (2024-Present)

• Developing Ka
lman filter algorithms for Pleistocene temperature reconstruction

• Publication and presentation forthcoming at America
n Geophysical Union 2025

Research Intern at Stanford University (2023)

• Created Retrieval Augmented Generation system
 for wildfire & air quality data analysis

• Implemented advanced NLP techniques using PyTorch and LangChain

• Publicat
ion

Research Intern at Australian Institute of Marine Science (2024)

• Developed Python scripts for 3D coral reef anal
ysis

• Implemented Möller-Trumbore algorithm for environmental modeling

• Used in paper for EcoRAPP (ecological intell
igence for reef restoration adaptation program)

about internal tools to diagnose Coral Bleaching and where to take acti
on

Underwater Ecosystem Drone Innovation

\- Developed novel underwater drone system for 3D coral reef mapping

\- Secu
red $11,000 venture capital investment

\- Obtained utility provisional patent for innovative marine mapping technology


\- Created scalable solution for reef ecosystem documentation and monitoring

\- System enables high-resolution 3D mode
ling of threatened marine environments  
  
**Non STEM:**   
  
REEFlect:

Founded and scaled global environmental monit
oring organization spanning 11 countries

Secured $2,500 municipal grant for the organization from City of Dublin

Estab
lished partnerships with East Bay Regional Park Districts, Big Sur Land Trust, Bear Yuba

Land Trust

Led international 
collaboration with Ocean Project Ghana for coastal cleanup initiatives in Ghana

Amassed over 200 members in over 7 diﬀe
rent countries
```
---

     
 
all -  [ Why Pydantic AI might be the future for building AI Agents? ](https://www.reddit.com/r/PydanticAI/comments/1hcc9qq/why_pydantic_ai_might_be_the_future_for_building/) , 2024-12-13-0914
```
Hi guys,

Pyndatic AI is a new framework comparing to heavy-weight such as Langchain and LlamaIndex. However, I found it
 very easy to use and powerful. It gives me a lot of flexibility to build versatile AI agents. 

Beside excellent data v
alidation (of course, it is from Pydantic, which is used by all big players such as OpenAI, Langchain...etc.), the bigge
st plus for me is: Pythonic and minimum of abstraction. We can easily go in the code and know how things are done under 
the hood. This siginificantly reduceds debugging time.

Check it out at [https://ai.pydantic.dev/](https://ai.pydantic.d
ev/)
```
---

     
 
all -  [ Problems installing langchain-python-rag-document from examples ](https://www.reddit.com/r/ollama/comments/1hcayho/problems_installing_langchainpythonragdocument/) , 2024-12-13-0914
```
i get this after installing from requirements.txt

    ERROR: Ignored the following versions that require a different py
thon version: 1.21.2 Requires-Python >=3.7,<3.11; 1.21.3 Requires-Python >=3.7,<3.11; 1.21.4 Requires-Python >=3.7,<3.11
; 1.21.5 Requires-Python >=3.7,<3.11; 1.21.6 Requires-Python >=3.7,<3.11
    
    ERROR: Could not find a version that s
atisfies the requirement tensorflow-macos==2.13.0 (from versions: 2.12.0)
    
    ERROR: No matching distribution found
 for tensorflow-macos==2.13.0
    
    $ pip --version
    pip 24.2 from xyz (python 3.11)
    $ python --version
    Py
thon 3.11.9

I have python 3.9.20 which i access with `python3.9` but how do i get the associated `pip` to install requi
rements?
```
---

     
 
all -  [ I automated my entire job with Python & AI - Ask me how to automate YOUR most hated task ](https://www.reddit.com/r/ArtificialInteligence/comments/1hc93pz/i_automated_my_entire_job_with_python_ai_ask_me/) , 2024-12-13-0914
```
Hey r/ArtificialInteligence  \- I'm the dev who automated an entire marketing agency's workflow. Ask me literally anythi
ng about automating your boring tasks. Some quick overview of what I've built:

• Turned 5-6 hours of daily research and
 posting into CrewAI+Langchain+DDG agency

• Built AI Bot that analyzes and answers 1000+ customer emails daily (For ver
y cheap - 0.5$ a day)

• Created Tweepy-Tiktok-bot+Instapy bots that manage entire social media presence, with CrewAI fo
r agents and Flux Dev for image generation

• Automated job applications on LinkedIn with Selenium+Gemini Flash 1.5

• A
utomated content generation with local AI models (for free)

• Automated entire YouTube channel (thumbnails, description
s, tags, posting) with custom FLUX Dev Lora, cheapest and most effective LLMs and hosted on cloud

• Built web scraper b
ot that monitors thousands of tokens prices and trader bots that makes the buy/sell on Binance

• Made a system that mon
itors and auto-responds to Reddit/Discord opportunities with [PRAW+discord.py](http://PRAW+discord.py)

Ask me about:

H
ow to automate your specific task Which tools actually work (and which are trash)

Real costs and time savings

Common a
utomation mistakes

Specific tech stacks for your automation needs

How to choose AI models to save costs

Custom soluti
ons vs existing tools

I've processed millions of tasks using these systems. Not theoretical - all tested and running.


I use Python, JS, and modern AI Stack (not just Zapier or [make.com](http://make.com) connections).

I'm building my por
tfolio and looking for interesting problems to solve. But first - ask me anything about your automation needs. I'll give
 you a free breakdown of how I'd solve it.

Some questions to get started: What's your most time-consuming daily task? W
hich part of your job do you wish was automated? How much time do you waste on repetitive tasks? Or ask whatever you wan
t to know...

Drop your questions below - I'll show you exactly how to automate it (with proof of similar projects I've 
done) :)
```
---

     
 
all -  [ I automated my entire job with Python & AI - Ask me how to automate YOUR most hated task ](https://www.reddit.com/r/Automate/comments/1hc8x5v/i_automated_my_entire_job_with_python_ai_ask_me/) , 2024-12-13-0914
```
Hey r/Automate  \- I'm the dev who automated an entire marketing agency's workflow. Ask me literally anything about auto
mating your boring tasks. Some quick overview of what I've built:

• Turned 5-6 hours of daily research and posting into
 CrewAI+Langchain+DDG agency 

• Built AI Bot that analyzes and answers 1000+ customer emails daily (For very cheap - 0.
5$ a day) 

• Created Tweepy-Tiktok-bot+Instapy bots that manage entire social media presence, with CrewAI for agents an
d Flux Dev for image generation 

• Automated job applications on LinkedIn with Selenium+Gemini Flash 1.5 

• Automated 
content generation with local AI models (for free) 

• Automated entire YouTube channel (thumbnails, descriptions, tags,
 posting) with custom FLUX Dev Lora, cheapest and most effective LLMs and hosted on cloud 

• Built web scraper bot that
 monitors thousands of tokens prices and trader bots that makes the buy/sell on Binance • Made a system that monitors an
d auto-responds to Reddit/Discord opportunities with [PRAW+discord.py](http://PRAW+discord.py)

Portfolio: [https://gith
ub.com/kakachia777/](https://github.com/kakachia777/) (I'm pushing projects gradually)

Ask me about: How to automate yo
ur specific task Which tools actually work (and which are trash) Real costs and time savings Common automation mistakes 
Specific tech stacks for your automation needs How to choose AI models to save costs Custom solutions vs existing tools


I've processed millions of tasks using these systems. Not theoretical - all tested and running. Quick flex: My automati
on tools have processed over 1M+ tasks for real clients. I use Python, JS, and modern AI (not just Zapier or [make.com](
http://make.com) connections).

I'm building my portfolio and looking for interesting problems to solve. But first - ask
 me anything about your automation needs. I'll give you a free breakdown of how I'd solve it.

Some questions to get sta
rted: What's your most time-consuming daily task? Which part of your job do you wish was automated? How much time do you
 waste on repetitive tasks? Or anything you want to know...

Drop your questions below - I'll show you exactly how to au
tomate it (with proof of similar projects I've done) :)
```
---

     
 
all -  [ [0 YOE, Unemployed , Machine Learning/Data Science, India] ](https://www.reddit.com/r/resumes/comments/1hc0c61/0_yoe_unemployed_machine_learningdata_science/) , 2024-12-13-0914
```
https://preview.redd.it/pbevskapi96e1.png?width=1170&format=png&auto=webp&s=6c61dfd3845cd82bc1ca6eeac19c00a2049231a8

ht
tps://preview.redd.it/wz65kahqi96e1.png?width=1070&format=png&auto=webp&s=b368ed92fd9cb957c2a0e1d6f4dee03f1bbbc58d

I am
 a 3rd year student pursuing BTech. I need feedback for applying to internships. As of now, I am not getting shortlisted
. What kind of projects do I need to add or showcase which will catch the attention. am i missing something here
```
---

     
 
all -  [ Conversational avatar  ](https://www.reddit.com/r/LangChain/comments/1hbxlfs/conversational_avatar/) , 2024-12-13-0914
```
Has anyone tried creating this kind of project? 
```
---

     
 
all -  [ Local tool calling agents using LangChain and Ollama are inexplicably poorly performing ](https://www.reddit.com/r/LocalLLaMA/comments/1hbx96u/local_tool_calling_agents_using_langchain_and/) , 2024-12-13-0914
```
Hi all,

Has anyone tried to create tool calling agents with LangChain and Ollama?  My attempts have been almost univers
ally unsuccessful.  Problems include:

1. Losing the ability to chat

2. Calling tools when it is not appropriate

3. Ca
lling tools on non-sensical inputs

The same agents work fine on, e.g., openai.

I have encountered this on a variety of
 models on Ollama.  Oddly enough, llama3-groq-tool-use:8b is the lone model that seems to work reasonably.

Has anyone e
ncountered this and determined the cause?

Here's a draft notebook/blog where I have some experiments: [https://colab.re
search.google.com/drive/1DngmKINhV95iKVVGF7YC5\_K7oiujMT6q?usp=sharing](https://colab.research.google.com/drive/1DngmKIN
hV95iKVVGF7YC5_K7oiujMT6q?usp=sharing)
```
---

     
 
all -  [ We built a frontend framework for LangGraph ](https://www.reddit.com/r/LangChain/comments/1hbw7yj/we_built_a_frontend_framework_for_langgraph/) , 2024-12-13-0914
```
At [CopilotKit](https://github.com/CopilotKit/CopilotKit), we build components & tools that help developers build in-app
 AI assistants (like Chatbots). Over the last few months we've been working to support deeper in-app Agent integrations.
  

  
So we collaborated with the LangChain team, to build a toolset that helps users integrate their LangGraph agents 
into full-stack apps with full support across the LangGraph ecosystem (Python, JS, Cloud, Studio, etc). 



Our new [Co-
Agents release](https://www.copilotkit.ai/blog/build-full-stack-apps-with-langgraph-and-copilotkit) contains tools that 
allow you to: 

\- Stream an agent's intermediate state (to the frontend) 

\- Share real-time state between the agent &
 the application 

\- Allow the Agent to take actions in your application 

\- Human-in-the-loop to steer and correct ag
ents (built with LangGraph breakpoints) 

\- Agentic Generative UI 

In our new release we support LangGraph JS, Python,
 LangGraph Platform (Cloud) and LangGraph Studio. 

  
You can build an Agentic Application in just a few minutes with L
angGraph & Co-Agents and we have great demos and [tutorials](https://go.copilotkit.ai/ai-travel-demo-video) to guide you
. 

  
We're fully open-source (MIT), get started here: 

[https://github.com/CopilotKit/CopilotKit](https://github.com/
CopilotKit/CopilotKit)

https://preview.redd.it/rwy3ec0ho86e1.png?width=993&format=png&auto=webp&s=e910313e67dfeecf90661
d36816d2298952e1b7a
```
---

     
 
all -  [ Stripe agent toolkit useful? ](https://www.reddit.com/r/LangChain/comments/1hbtz8f/stripe_agent_toolkit_useful/) , 2024-12-13-0914
```
Anyone using the Stripe agent toolkit https://github.com/stripe/agent-toolkit? 

I've been trying to automate payments (
with human in the loop confirmation) for customer support using the langchain part of their agent, but only 10 tools are
 so exposed.   
Anyone extended/using it?
```
---

     
 
all -  [ [For Hire] Programmer/Web Developer/IT Consultant (Python, PHP, AI, etc.) ](https://www.reddit.com/r/forhire/comments/1hbsdu1/for_hire_programmerweb_developerit_consultant/) , 2024-12-13-0914
```
To get in contact, please message me, I don't use the chat thing and might miss you or reply very late. Then we can swit
ch to email/discord/telegram or whatever else. Apologies for starting with this, but many missed it when it was lower.


I'm a programmer/web developer with 15 years of professional experience. I am available for all sorts of programming and
 web development tasks.

I also offer consulting services. If you need something done, but don't know how exactly, I can
 help. I'm an excellent researcher and I communicate well. I will work with you to find the best solution for your probl
em.

My services include, but are not limited to:

* websites

* desktop applications

* AI integration (chatGPT API, la
ngchain, whatever else turns up)

* integration with APIs and other webservices

* all kinds of scripts

* task automati
on

* website optimization

* debugging

* plugins for existing software

* bots (Reddit, Telegram, etc)

* code audits


If you're looking for someone to take care of a variety of different tasks, I can offer continuous support.

My preferr
ed environment is Python with Django, but I work with anything Python or PHP based. I have no problem with learning new 
technologies that are needed for the project.

Rate is $60/h.

Portfolio:

https://bdabkowski.yum.pl

Satisfied customer
s:

https://www.reddit.com/r/testimonials/comments/2e8gqy/pos_uqui_need_a_backend_web_dev_look_no_further/

https://www.
reddit.com/r/testimonials/comments/7fsdze/pos_hiring_uqui_was_an_example_of_how_it_should/

https://www.reddit.com/r/tes
timonials/comments/80pu9l/pos_uqui_great_work_detailed_and_fast/

https://www.reddit.com/r/testimonials/comments/b0nx68/
uqui_is_a_hardworking_intelligent_honest_apps/

https://www.reddit.com/r/testimonials/comments/j3mz3p/uqui_is_a_great_we
b_development_consultant_with/

https://www.reddit.com/r/testimonials/comments/v40ay3/pos_uqui_is_a_great_backend_dev_to
_work_with/

Please note: I am not a designer. To make it clear, it means zero aesthetic sense.
```
---

     
 
all -  [ Which tool are you using to build Ai Agents? ](https://i.redd.it/p2j1smaff76e1.jpeg) , 2024-12-13-0914
```
As mentioned in the title, Curious to know which tool is the most effective. 

I'm using Langchain and my own custom too
ls as of now for creatingagents in my currentprojects. Used flowise before and did not try N8N completely.
```
---

     
 
all -  [ Need advice on hosting LLM on GPU in production ! ](https://www.reddit.com/r/LangChain/comments/1hbqtss/need_advice_on_hosting_llm_on_gpu_in_production/) , 2024-12-13-0914
```
I currently have A40 single GPU of 48GB VRAM. I want to host Qwen2.5 14B Instruct AWQ model in it. I tried hosting it us
ing Nvidia Triton + VLLM backend. I want to use this model for RAG application. Due to some concerns, My prompt to the R
AG is so high (\~20 lines). The GPU Utilization is around 80-90% for a single hit and it is taking around 4-5 sec to res
pond. But, When there are concurrent requests to the same API, the latency is spiking up. Even if there two concurrent r
equests, time taken to respond is around 7-9 sec. I want to scale this application for 500 users. I need advice on below
 areas.   
1. How much GPU should I need to use? Should I use a single GPU or Multi GPU for this task?  
2. What serving
 platform should I have to use other than Nvidia-Triton + VLLM backend to achieve greater throughput?  
I'm new to this.
 Could you please help me out?
```
---

     
 
all -  [ Beyond table parsing in RAG: table data understanding ](https://www.reddit.com/r/LangChain/comments/1hbq78j/beyond_table_parsing_in_rag_table_data/) , 2024-12-13-0914
```
Proper parsing of tables in RAG is really important. As we looked at this problem we wanted to do something that provide
s true understanding of tables across the complete RAG flow - from parsing through retrieval. Excited to share this new 
functionality available with Vectara, and curious to hear what you all think, and how to further improve this.

[https:/
/www.vectara.com/blog/table-data-understanding](https://www.vectara.com/blog/table-data-understanding)
```
---

     
 
all -  [ Looking for Resources to Learn AI Agents and Build a Roadmap with LangChain ](https://www.reddit.com/r/LangChain/comments/1hbps28/looking_for_resources_to_learn_ai_agents_and/) , 2024-12-13-0914
```
Hi everyone,
I'm diving into the world of AI and looking to focus on building AI agents using LangChain. I'm interested 
in understanding the roadmap, best practices, and any recommended tutorials, courses, or documentation that could help m
e get started.

Are there any must-read resources, GitHub repositories, or online communities you'd recommend? If you've
 worked with LangChain, I'd love to hear about your learning journey and tips.

Thanks in advance for your help!
```
---

     
 
all -  [ Not getting shortlisted by resume off campus. Roast my resume. ](https://www.reddit.com/r/developersIndia/comments/1hboym6/not_getting_shortlisted_by_resume_off_campus/) , 2024-12-13-0914
```
I am a final-year undergraduate at a tier 1 engineering college. Despite securing an offer from a tier 1 software compan
y through an on-campus process (which required no resume shortlisting, only a competitive programming round followed by 
interviews), I am struggling to get my resume shortlisted off-campus. Even startups on platforms like Wellfound/LinkedIn
, offering unpaid or low-paying roles, are not considering my application. Any suggestion is highly appreciated.

https:
//preview.redd.it/wc8daf8ei66e1.png?width=1190&format=png&auto=webp&s=d8f8707af1031ae8e8dd4d814a8ccf6f427cb682


```
---

     
 
all -  [ What’s Your Biggest Challenge with Automation? ](https://www.reddit.com/r/LangChain/comments/1hbnird/whats_your_biggest_challenge_with_automation/) , 2024-12-13-0914
```
Hi guys, I’ve been working on a SaaS of mine called [Wellows.com](http://wellows.com/), designed to simplify workflow au
tomation using just natural language prompts. The idea came from my own frustration with how complex and time-consuming 
automation can be setting up workflows, syncing tools, and managing repetitive tasks shouldn’t take hours.

Here’s where
 we’re at:

* The platform is in its final development stages, and we’re focusing on building something that works for r
eal teams with real challenges.
* I’ve seen SaaS teams struggle to automate critical tasks like onboarding new users, sy
ncing data across tools, and generating usage reports. Our goal is to eliminate that pain.

Here’s what I’ve learned so 
far from this journey:

1. **Understanding pain points is key.** Every team’s struggles with automation are unique. I’ve
 been speaking with SaaS teams to learn where workflows break down and what’s stopped them from automating more.
2. **Si
mple wins.** The feedback I’ve received highlights that people don’t want another complex tool they want an intuitive so
lution that saves them time, not one that eats it up.
3. **Collaboration is everything.** Working closely with early tes
ters has shown me that user input is invaluable. Their insights have helped shape features that address real-world probl
ems, not just hypothetical ones.

**Here’s what’s next:**  
We’re gearing up to launch soon and are actively looking for
 feedback to refine the platform further. If you’re struggling with a task that’s tough to automate or if you’ve been he
sitant to dive into automation, let’s talk. I’d love to hear about your experiences and brainstorm solutions together.


So tell me, what’s the #1 task your team struggles to automate?
```
---

     
 
all -  [ Slick agent tracing via Pydantic Logfire with zero instrumentation for common scenarios… ](https://i.redd.it/rfb97v4wx46e1.jpeg) , 2024-12-13-0914
```

Disclaimer: I don’t work for Pydantic Logfire. But I do help with dev relations for Arch(Gateway)

If you are building 
agents and want rich agent (prompt + tools + LLM) observability, imho Pydantic logfire offers the most simple setup and 
visually appealing experience - especially when combined with https://github.com/katanemo/archgw

archgw is an intellige
nt gateway for agents that offers fast⚡️function calling, rich LLM tracing (source events) and guardrails 🧱 so that deve
lopers can focus on what matters most.

With zero lines of application code and rich out-of-the-box tracing for agents (
prompt, tools call, LLM) via Arch and Logfire. 

Checkout the demo here: https://github.com/katanemo/archgw/tree/main/de
mos/weather_forecast

```
---

     
 
all -  [ RAG Semi_structured data processing  ](https://www.reddit.com/r/LangChain/comments/1hbirst/rag_semi_structured_data_processing/) , 2024-12-13-0914
```
I'm creating a rag pipeline for semi and Unstructured pdf documents.For parsing the pdf I'm using Pymupdf4llm and the fi
nal format of text is markdown 

Main issues:
1.chunking: what is the best chucking strategy to split them by their head
ers and I have tables which I don't want to split them 


2. Tables handling: if my table is continuing in 3 pages then 
the header is not maintained in all pages and it is not able to answer it correctly 

If I'm maintaining the previous pa
ge context of 30% in this page then when answering it is considering that chunk and while returning it is giving that pa
ge as the answer page and confusing from which page the actual answer is really from

3.Complex tables analysis:While th
e questions are from a complex table whicj contains all numbers and very less text data in it ,so while retrievering it 
is considering the chunks where it find the same numbers but llm is every time answering differently and not able to sol
ve it.




Please help me out 

Using: Pymupdf4llm,Langchain,Langgraph,python,Groq,llama 3.1 70b model
```
---

     
 
all -  [ Best practices for rag ](https://www.reddit.com/r/LLMDevs/comments/1hbes3d/best_practices_for_rag/) , 2024-12-13-0914
```
Hi llmdevs! Any suggestions on best practices for rag? For a beginner? I have been playing around with rag for about a m
onth now, and what all knowledge i have so far is what is given by openai and Claude that helped me with my project. I a
m not getting desired results back so iam assuming there are issues with my setup.

I've tried llamaindex and langchain 
and their default chucking embedding tools (along with custom chucking with cosine similarity as suggested by openai). A
nd worked with faiss and qdrant so far as my vector stores along with llama various versions and openai.

My use case ha
s to do with public sec filings (and one day private financial data from my company, if my setup works).

If it were you
, how would go about setting up the stack? Any help is greatly appreciated. Will answer any missing pieces of informatio
n. 
```
---

     
 
all -  [ Need help: Infinite Loop on RNEventSource with Server-Sent Events (SSE) - Only Receiving “attempt: 1 ](https://www.reddit.com/r/reactnative/comments/1hbepuo/need_help_infinite_loop_on_rneventsource_with/) , 2024-12-13-0914
```
I am working on a React Native expo managed project using RNEventSource to handle Server-Sent Events (SSE) from a langch
ain endpoint. My backend is correctly streaming data (confirmed via Postman), but the frontend gets stuck in an infinite
 loop of the same response, only receiving:

    LOG  Open SSE connection.
    LOG  Stream Data: {'attempt': 1, 'run_id'
: '1efb7463-0ff8-60c3-bd10-17ccc210899f'}
    WARN  Unexpected Data: {'run_id':'1efb7463-0ff8-60c3-bd10-17ccc210899f','a
ttempt':1}
    LOG  Stream Data: {'attempt': 1, 'run_id': '1efb7463-0ff8-60c3-bd10-17ccc210899f'}
    WARN  Unexpected D
ata: {'run_id':'1efb7463-0ff8-60c3-bd10-17ccc210899f','attempt':1'}
    ...

Code:  


    const askDogy = async (reques
t) => {
      const url = `${assitantBaseUrl}/threads/${threadId}/runs/stream`
      const requestBody = JSON.stringify(
{
        assistant_id: assistantID,
        input: {
          messages: [{ role: 'user', content: request }],
        
},
        stream_mode: ['messages'],
      })
    
      const options = {
        body: requestBody,
        method: '
POST',
        headers: {
          'Content-Type': 'application/json',
          Accept: 'text/event-stream',
        }
,
      }
    
      eventSourceRef.current = new RNEventSource(url, options)
    
      eventSourceRef.current.addEvent
Listener('open', () => {
        console.log('Open SSE connection.')
      })
    
      eventSourceRef.current.addEvent
Listener('message', (event) => {
        console.log('Raw Event:', event)
        try {
          const data = JSON.pars
e(event.data)
          console.log('Parsed Data:', data)
    
          if (data.content) {
            console.log('AI
 Reply Content:', data.content)
            setChatResponse('Bot', data.content, true)
          } else {
            co
nsole.warn('Unexpected Data:', data)
          }
        } catch (error) {
          console.error('Error parsing event 
data:', error)
        }
      })
    
      eventSourceRef.current.addEventListener('error', (error) => {
        conso
le.error('Stream error:', error)
    
            if (error.status === 409) {
              console.log('Conflict detect
ed, creating a new thread...')
              // Create a new thread and retry
              tempThreadId = await createT
hread()
              if (!tempThreadId)
                throw new Error('Failed to create a new thread after conflict')

              setThreadId(tempThreadId)
    
              // Retry the stream with the new thread ID
              con
sole.log('Retrying with new thread ID:', tempThreadId)
              await askDogy(request) // Recursive call with the n
ew thread
            } else {
              handleStopStream()
            }
      })
    }

  
**Debugging Observation
s:**

* I receive the same attempt: 1 data repeatedly with no progress.
* The backend should send incremental updates, b
ut the frontend logs do not show progress.

**Questions:**

* Is there a known issue with RNEventSource or its compatibi
lity with React Native?
* Could there be something specific I need to handle in RNEventSource to parse incremental updat
es?
* Any other npm package/library I can use to handle server sent events in react native/expo?

**Things I've tried:**


* Verified backend compliance with the SSE spec.
* Ensured RNEventSource initialization includes proper headers and me
thod.
* Added maximum retries and timeout logic in case of backend failures (now removed).
* Tested backend with Postman
 and it streams correctly.

  
Thanks in advance. Link to [stackoverflow post](https://stackoverflow.com/questions/79270
017/infinite-loop-on-rneventsource-with-server-sent-events-sse-only-receiving-a)
```
---

     
 
all -  [ [For Hire] Experienced AI/Full Stack & DevOps Developer – Seeking Challenging, High-Impact Projects! ](https://www.reddit.com/r/forhire/comments/1hbbhib/for_hire_experienced_aifull_stack_devops/) , 2024-12-13-0914
```
🚀 **Your All-in-One Solution for AI/ML, Full Stack Development, and DevOps!**

👋 Hi, I’m Sheryar, an experienced AI/ML E
ngineer, Full Stack Developer, and DevOps Specialist. I’m here to help turn your ideas into scalable, high-performance s
olutions!

💻 **Full Stack Development Expertise**  
🔹 Stunning UIs: React/Angular  
🔹 Robust APIs: Node.js, NestJS  
🔹 S
eamless Payment Integration: Stripe  
🔹 Cloud Infrastructure: AWS, GCP

🤖 **AI & Machine Learning**  
🔹 Smart Chatbots: 
Built with LangChain  
🔹 Custom AI Models: NLP, Automation

⚙️ **DevOps Solutions**  
🔹 CI/CD Pipelines: GitHub Actions,
 Jenkins  
🔹 Containerization: Docker, Kubernetes  
🔹 Infrastructure as Code: Terraform, Ansible  
🔹 Monitoring Tools: P
rometheus, Grafana

🌟 **Recent Projects**  
🚗 **Ride-Sharing**: Real-time tracking & payments  
📦 **Logistics**: Multi-s
top delivery optimization  
🛒 **E-Commerce**: Scalable Kubernetes clusters

💰 **Rates**: $20–$25/hour (negotiable)  
📧 *
*Let’s talk!** DM me to discuss your project!  
GitHub: [storm1033](https://github.com/storm1033)

**Let’s build somethi
ng amazing together!** 🌐✨

# 🌟 Let's Build Something Amazing Together! 🌟

# 👋 Hi, I'm Sheryar!

An AI/ML Engineer, Full 
Stack Developer, and DevOps Specialist. I help transform ideas into scalable, high-performance solutions. Whether you're
 looking to build a robust app, deploy intelligent AI systems, or streamline your infrastructure, I’ve got you covered!


# 🚀 What I Do Best:

# Full Stack Development

From sleek, user-friendly interfaces to powerful backends, I create seam
less web applications:

* **Stunning UIs**: React | Angular
* **Robust APIs**: Node.js | NestJS
* **Seamless Payment Int
egrations**: Stripe
* **Cloud Infrastructure**: AWS | GCP

# AI & Machine Learning

Unlock the potential of AI to elevat
e your product with intelligent, data-driven features:

* **AI Chatbots**: Powered by LangChain
* **Tailored AI Models**
: NLP, Automation, and more

# DevOps Excellence

I automate, optimize, and ensure reliability at scale:

* **CI/CD Pipe
lines**: GitHub Actions | Jenkins
* **Containerization**: Docker | Kubernetes
* **Infrastructure as Code**: Terraform | 
Ansible
* **Monitoring**: Prometheus | Grafana

# 🌟 Featured Projects

Here’s a glimpse of what I’ve worked on recently:


* **Ride-Sharing App**: Real-time vehicle tracking, seamless payments
* **Logistics Platform**: Multi-stop delivery ro
ute optimization
* **E-Commerce Platform**: Scalable Kubernetes clusters handling high traffic

# 💡 Let’s Collaborate!


* 💰 **Rate**: $20–$25/hour (negotiable depending on the project)
* 📩 **Reach Out**: DM me to discuss your project!

📍 **
GitHub**: [storm1033](https://github.com/storm1033)

**Let's turn your ideas into scalable, impactful solutions!** 🌐✨
```
---

     
 
all -  [ What is your go-to way of calling LLMs ?  ](https://www.reddit.com/r/node/comments/1hba5qq/what_is_your_goto_way_of_calling_llms/) , 2024-12-13-0914
```
For once, nodejs is not the main area of experimentation, we are a bit behind python for tooling. Still, what do y'all u
se for interfacing with llms ? For validating structured data ?

I know people hate on langchain, but there has to be so
mething better than raw openai package?
```
---

     
 
MachineLearning -  [ [P] Minima: local conversational retrieval augmented generation project (Ollama, Langchain, FastAPI, ](https://www.reddit.com/r/MachineLearning/comments/1h1pudq/p_minima_local_conversational_retrieval_augmented/) , 2024-12-13-0914
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

     
