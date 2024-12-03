 
all -  [ Evaluation metrics for llm summary  ](https://www.reddit.com/r/LangChain/comments/1h5a1sj/evaluation_metrics_for_llm_summary/) , 2024-12-03-0915
```
I am working on long document summarization model using gpt-4o-mini and mistralAI.

I want compare my llm output with hu
man output. 

Initially,i compared with Abstract as reference with llm output. The results such as blue,rouge are varyin
g at broad range. 

I absorbed that length of a llm output is double the abstract.

So, I am looking for suggestions to 
evaluate llm summary output only, for eg: before and after improving context of llm with external information.
```
---

     
 
all -  [ what is difference between bind_tools to a LLM or creating an agent with vanilla LLM and the tool ?  ](https://www.reddit.com/r/LangChain/comments/1h58de1/what_is_difference_between_bind_tools_to_a_llm_or/) , 2024-12-03-0915
```
i am confused between the two so any help?


```
---

     
 
all -  [ Building a Personalized AI Assistant with LangChain ](https://www.reddit.com/r/u_KonradFreeman/comments/1h56mgk/building_a_personalized_ai_assistant_with/) , 2024-12-03-0915
```
In this blog post, we'll explore a Python script that serves as a foundation for building such an AI assistant. We'll de
lve into how you can use this code as a starting point and discuss several exciting applications, complete with follow-u
p prompts to inspire your next project.

  
Read about some of the possible applications of this starting point on my no
n-monetized blog or just check out the repo.

[https://danielkliewer.com/2024/12/02/persona-chat](https://danielkliewer.
com/2024/12/02/persona-chat)

`git clone` [`https://github.com/kliewerdaniel/PersonaChat.git`](https://github.com/kliewe
rdaniel/PersonaChat.git)

The provided Python script leverages the power of LangChain, OpenAI's GPT models, and vector d
atabases to create an AI assistant that imitates the writing style of a specific persona based on provided writing sampl
es. Here's what the script does:

1. **Loads Writing Samples**: Reads text and PDF files from a specified folder to gath
er writing samples.
2. **Processes and Embeds Text**: Splits the text into manageable chunks and creates embeddings usin
g OpenAI's API.
3. **Creates a Vector Store**: Stores the embeddings in a Chroma vector store for efficient retrieval.
4
. **Sets Up a Retrieval QA Chain**: Uses LangChain's RetrievalQA to build an interactive question-answering system.
5. *
*Interacts with the User**: Provides a conversational interface where the AI assistant responds in the persona's writing
 style.
6. **Saves Conversations**: Logs the conversation history into a Markdown file for future reference.

# It is ju
st a basic one file app, the requirements are:

    openai
    python-dotenv
    langchain 
    chromadb 
    pinecone-c
lient 
    tiktoken
    sentence-transformers
    PyPDF2
    langchain-community
    langchain-openai 
    langchain-chr
oma
    pypdf

Here is the file:

    import os
    import sys
    import glob
    from langchain_community.document_loa
ders import TextLoader, PyPDFLoader
    from langchain.text_splitter import RecursiveCharacterTextSplitter
    from lang
chain_community.embeddings import OpenAIEmbeddings
    from langchain_community.vectorstores import Chroma
    from lang
chain_community.chat_models import ChatOpenAI
    from langchain.chains import RetrievalQA
    from langchain.prompts im
port PromptTemplate
    import openai
    from langchain_openai import OpenAIEmbeddings  # Updated import
    from doten
v import load_dotenv
    from langchain.memory import ConversationBufferMemory
    
    load_dotenv()  # Load variables 
from .env
    openai_api_key = os.getenv('OPENAI_API_KEY')
    if not openai_api_key:
        print('Error: OPENAI_API_K
EY not found in environment variables.')
        exit(1)
    
    def main():
    
        
        # Initialize memory

        memory = ConversationBufferMemory(memory_key='history', return_messages=True)
    
    
        # Step 1: Load a
nd process writing samples
        folder_path = './writing_samples'
        documents = []
        for filepath in glob
.glob(os.path.join(folder_path, '**/*.*'), recursive=True):
            if os.path.isfile(filepath):
                ext
 = os.path.splitext(filepath)[1].lower()
                try:
                    if ext == '.txt':
                    
    loader = TextLoader(filepath, encoding='utf-8')
                        documents.extend(loader.load())
            
        elif ext == '.pdf':
                        loader = PyPDFLoader(filepath)
                        documents.ext
end(loader.load())
                    else:
                        print(f'Unsupported file format: {filepath}')
     
           except Exception as e:
                    print(f'Error reading '{filepath}': {e}')
    
        if not docu
ments:
            print('No documents found in the folder.')
            exit(1)
    
        text_splitter = Recursive
CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        texts = text_splitter.split_documents(documents)
    

        # Step 2: Create embeddings and vector store
        embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key
)  # Pass API key directly
        vector_store = Chroma.from_documents(texts, embeddings, persist_directory='./persona_
vectorstore')
        vector_store.persist()
    
        # Step 3: Set up the retriever and agent
        retriever = v
ector_store.as_retriever(search_kwargs={'k': 3})
        llm = ChatOpenAI(temperature=0.7, openai_api_key=openai_api_key
)
    
    
        persona_prompt = PromptTemplate(
            input_variables=['context', 'question'],
            te
mplate='''
    Based on the context answer to the best of your ability
    
    Context:
    {context}
    
    Question
:
    {question}
    
    Answer in the writing style of the context.
    '''
        )
    
        qa_chain = Retrieva
lQA.from_chain_type(
            llm=llm,
            chain_type='stuff',
            retriever=retriever,
            m
emory=memory,
            return_source_documents=False,
            chain_type_kwargs={'prompt': persona_prompt}
      
  )
    
        def save_to_markdown(conversation, filename='conversation.md'): 
            with open(filename, 'a', e
ncoding='utf-8') as f:
                f.write(conversation + '\n\n---\n\n')
    
    
        # Step 4: Interact with t
he user and save to markdown
        print('You can now interact with the persona. Type 'exit' to quit.\n')
        conv
ersation_history = ''
        while True:
            user_input = input('You: ')
            if user_input.lower() in (
'exit', 'quit'):
                break
    
            # Generate response
            response = qa_chain.run(user_inp
ut)
    
            # Display and save the conversation
            print(f'Persona: {response}\n')
            convers
ation = f'### You:\n{user_input}\n\n### Persona:\n{response}'
            save_to_markdown(conversation)
    
    
    i
f __name__ == '__main__':
        main()

  
Let me know what you think. 
```
---

     
 
all -  [ Questioning the value of langchain ](https://www.reddit.com/r/LangChain/comments/1h56klp/questioning_the_value_of_langchain/) , 2024-12-03-0915
```
I deployed a simple app using LangGraph served by a react FE.

Everything worked fine… until it didn’t. It’s a nightmare
 to debug. And I’m questioning what value the langchain ecosystem really offers.

Any viewpoints would be appreciated be
fore I commit coupling my code with langchain. 

I’m looking at ell, getliteralai. Majority of the value comes from the 
LLM server, including streaming.

I’m terms of parallelisation and managing the state of the graph, does langgraph rally
 do a lot of heavy lifting? I mean I can build interesting agents from scratch. So…

I’m feeling it’s a bait and switch 
tbh, but I could just be frustrated… 
```
---

     
 
all -  [ [For Hire] Unlock Your Business's Potential with Expert Full-Stack Development for a Powerful Digita ](https://www.reddit.com/r/forhire/comments/1h54cyt/for_hire_unlock_your_businesss_potential_with/) , 2024-12-03-0915
```
Hi Reddit! 👋

In today’s digital-first world, having a powerful and seamless online presence is no longer optional—it’s 
essential. Whether it’s creating user-friendly web platforms, scaling backend systems, or integrating smart automation, 
a robust tech foundation ensures your business stays ahead of the curve. From startups to established enterprises, I’m h
ere to help you build the tools you need to succeed.

I’m Sheryar, a Full Stack Developer skilled in React, Next.js, Nes
tJS, Node.js, AWS, and LangChain. I specialize in:

✅ **Frontend**: Responsive, pixel-perfect UIs with React/Angular  
✅
 **Backend**: Scalable APIs & microservices (Node.js, NestJS)  
✅ **Databases**: Advanced PostgreSQL with JSON handling 
 
✅ **Payments**: Stripe integration for secure transactions  
✅ **Cloud**: AWS deployments  
✅ **Chatbots & Voicebots**
: Development with LangChain for intelligent automation

**Recent Work:**  
🚗 **Ride-sharing app** with Stripe payments 
& live tracking  
📦 **Urban logistics platform** with multi-stop deliveries  
📊 **Custom CRM** with Twilio API integrati
on  
🤖 **Chatbot & Voicebot solutions** for automation and customer support

💰 **Rate**: $15–$20/hour (negotiable)  
📧 D
M me to discuss your project or view my portfolio!  
**GitHub**: storm1033

Let’s create impactful digital solutions and
 take your business to the next level! 🚀
```
---

     
 
all -  [ Help with Vector Databases ](https://www.reddit.com/r/LLMDevs/comments/1h53bdl/help_with_vector_databases/) , 2024-12-03-0915
```
Hey folks, I was tasked with making a Question Answering Chatbot for my firm -
I ended up with a Question Answering chai
n via Langchain
I'm using the following models -
For Inference: Mistral 7B (from Ollama)
For Embeddings: Llama 2 7B (Oll
ama aswell)
For Vector DB: FAISS Local DB

I like this system because I get to produce a chat-bot like answer via the In
ference Model - Mistral, however, due to my lack of experience, I decided to simply go with Llama 2 for Embedding model.


Each of my org's documents are anywhere from 5000-25000 characters in length. There's about 13 so far and more to be a
dded as time passes (current count at about 180,000) [I convert these docs into one long text file which is auto-formatt
ed and cleaned].
I'm using the following chunking system:
Chunk Size: 3000
Chunk Overlap: 200

I'm using FAISS' similari
ty search to retrieve the relevant chunks from the user prompt - however the accuracy massively degrades as I go beyond 
say 30,000 characters in length. I'm a complete newbie when it comes to using Vector-DB's - I'm not sure if I'm supposed
 to fine-tune the Vector DB, or if I should opt for a new Embedding Model. But I'd like some help, tutorial and other he
lpful resources will be a lifesaver! I'd like a Retrieval System that has good accuracy with fast Retrieval speeds - how
ever the accuracy is a priority. 

Thanks for the long read!

```
---

     
 
all -  [  I replaced my voicemail with ChatGPT. ](https://www.reddit.com/r/EntrepreneurRideAlong/comments/1h539l9/i_replaced_my_voicemail_with_chatgpt/) , 2024-12-03-0915
```
Weekend Build: I replaced my voicemail with ChatGPT.

Features:
- Books meeting on Calendly
- Spam filter
- Knows me (RA
G)

Why?: It sucks to call doctors, lawyers etc to schedule a meeting or get simple information. I know this will become
 standard.

Story: When I worked at the Pentagon, we had a really sweet elderly secretary Barbara. If I released this I'
d call this CallBarbara AI.

Tech: Twilio (phone), Deepgram (TTS), OpenAI (LLM), LangChain RAG (for my information), Cal
endly (availability), Google (calendar int). Unfortunately Calendly API blows so I had to use google's api. 

Learnings:
 I could make this significantly faster and more expensive with OpenAI's realtime voice (Speech-to-speech), or an open s
ource version. 

Next/ Maybe: 
- Build front end (for anyone to use)
- Clone any voice
- Figure out use-cases (SMB brick
 and mortar?)
```
---

     
 
all -  [ Need Advice on Implementing Reranking Models for an AI-Based Document-Specific Copilot feature ](https://www.reddit.com/r/LLMDevs/comments/1h50nwl/need_advice_on_implementing_reranking_models_for/) , 2024-12-03-0915
```
Hey everyone! I'm currently working on an AI-based grant writing system that includes two main features:

Main  AI: Uses
 LLMs to generate grant-specific suggestions based on user-uploaded documents.

Copilot Feature: Allows document-specifi
c Q&A by utilizing a query format like /{filename} {query} to fetch information from the specified document.

Currently,
 we use FAISS for vector storage and retrieval, with metadata managed through .pkl files. This setup works for similarit
y-based retrieval of relevant content. However, I’m considering introducing a reranking model to further enhance retriev
al accuracy, especially for our Copilot feature.

Challenges with Current Setup:

Document-Specific Retrieval: We're sto
ring document-specific embeddings and metadata in .pkl files, and retrieval works by first querying FAISS.

Objective: I
mprove the precision of the results retrieved by Copilot when the user requests data from a specific document (e.g., /ex
ample.pdf summarize content).

Questions for the Community:

Is using a reranking model (e.g., BERT-based reranker, Mini
LM) a good idea to add another layer of precision for document retrieval, especially when handling specific document req
uests?

If I implement a reranking model, do I still need the structured .pkl files, or can I rely solely on the embeddi
ngs and reranking for retrieval?

How can I effectively integrate a reranking model into my current FAISS + Langchain se
tup?

I’d love to hear your thoughts, and if you have experience in using reranking models with FAISS or similar, any ad
vice would be highly appreciated. Thank you!


```
---

     
 
all -  [ Need Advice on Implementing Reranking Models for an AI-Based Document-Specific Copilot feature ](https://www.reddit.com/r/learnmachinelearning/comments/1h50l6c/need_advice_on_implementing_reranking_models_for/) , 2024-12-03-0915
```
Hey everyone! I'm currently working on an AI-based grant writing system that includes two main features:

1. **Main  AI*
*: Uses LLMs to generate grant-specific suggestions based on user-uploaded documents.
2. **Copilot Feature**: Allows doc
ument-specific Q&A by utilizing a query format like `/{filename} {query}` to fetch information from the specified docume
nt.

Currently, we use **FAISS** for vector storage and retrieval, with metadata managed through `.pkl` files. This setu
p works for similarity-based retrieval of relevant content. However, I’m considering introducing a **reranking model** t
o further enhance retrieval accuracy, especially for our Copilot feature.

**Challenges with Current Setup:**

* **Docum
ent-Specific Retrieval**: We're storing document-specific embeddings and metadata in `.pkl` files, and retrieval works b
y first querying FAISS.
* **Objective**: Improve the precision of the results retrieved by Copilot when the user request
s data from a specific document (e.g., `/example.pdf summarize content`).

**Questions for the Community:**

1. Is using
 a reranking model (e.g., **BERT-based reranker, MiniLM**) a good idea to add another layer of precision for document re
trieval, especially when handling specific document requests?
2. If I implement a reranking model, do I still need the s
tructured `.pkl` files, or can I rely solely on the embeddings and reranking for retrieval?
3. How can I effectively int
egrate a reranking model into my current FAISS + Langchain setup?

I’d love to hear your thoughts, and if you have exper
ience in using reranking models with FAISS or similar, any advice would be highly appreciated. Thank you!

# 
```
---

     
 
all -  [ Build a Multi-Agent AI System with LangChain, AutoGen, Azure OpenAI GPT-4, and Azure PostgreSQL ](https://www.reddit.com/r/PostgreSQL/comments/1h4z6rl/build_a_multiagent_ai_system_with_langchain/) , 2024-12-03-0915
```
Hello, I have started a Github Repo to work on simple scenarios with Multi AI Agents and Databases. There are 3 scenario
s there: Chat with Your Data, Develop on Your Data and Act on Your Data.I am using Autogen, Langchain, Azure PostgreSQL,
 and Azure Open AI. 

I welcome feedback and improvements from the community: [https://github.com/Azure-Samples/azure-po
stgresql-openai-langchain-autogen-demo](https://github.com/Azure-Samples/azure-postgresql-openai-langchain-autogen-demo)
 

I am planning to use other LLM models but I am hitting issues with using other GPT models as they keep adding \`\` sq
l \`\`\`

  

```
---

     
 
all -  [ error with HuggingFaceEmbeddings ](https://www.reddit.com/r/LangChain/comments/1h4ynos/error_with_huggingfaceembeddings/) , 2024-12-03-0915
```
hello guys, i have been trying to fix this issue for a while i cant really figure it out, so what happens is when i run


    from langchain_huggingface import HuggingFaceEmbeddings
    embeddings_model = HuggingFaceEmbeddings()

i get the e
rror:

    RuntimeError: Failed to import transformers.integrations.integration_utils because of the following error (lo
ok up to see its traceback):
    Failed to import transformers.modeling_utils because of the following error (look up to
 see its traceback):
    cannot import name 'quantize_' from 'torchao.quantization' (C:\Users\kashy\AppData\Local\Progra
ms\Python\Python310\lib\site-packages\torchao\quantization\__init__.py)

can someone please help me with it. thanks in a
dvance
```
---

     
 
all -  [ Claude Doesn't Follow My Few Shot Prompts ](https://www.reddit.com/r/LangChain/comments/1h4w0ac/claude_doesnt_follow_my_few_shot_prompts/) , 2024-12-03-0915
```
    claude_sentiment_clf = ChatAnthropic(
        model='claude-3-5-sonnet-20240620',
        temperature=0,
        max
_tokens=3,
        timeout=None,
        max_retries=2,
    claude_sentiment_clf = ChatAnthropic(
        model='claude-
3-5-sonnet-20240620',
        temperature=0,
        max_tokens=3,
        timeout=None,
        max_retries=2,
    )

H
ere I create an instance of the Claude 3.5 Sonnet and later on using LangChain I pass it on a prompt to make a simple cl
assification and within this prompt I have few shot examples.

Initially it was working well and i had it restricted to 
3 labels. Now it is trying to generate non-sense argumentation of why it thinks the classification is..

I run the same 
chains with OpenAI API and I don't have any issues what so ever.

What is causing this to happen?

Again to clarify, it 
outputs 3 tokens, but not the ones I want.

I want it to output \[Bullish, Bearish, Neutral\], instead it gives me somet
hing like 'The article suggests'

Is there some type of memory reset that might be causing the issue?

I am using the pa
id API version.

The outputs are given here:

('Bullish', 'Here are the')

first output is OPEN AI, which is working as 
intented. The second output is Claude.

And here are the Few Shots:

)

Here I create an instance of the Claude 3.5 Sonn
et and later on using LangChain I pass it on a prompt to make a simple classification and within this prompt I have few 
shot examples.

Initially it was working well and i had it restricted to 3 labels. Now it is trying to generate non-sens
e argumentation of why it thinks the classification is..

I run the same chains with OpenAI API and I don't have any iss
ues what so ever.

What is causing this to happen?

Again to clarify, it outputs 3 tokens, but not the ones I want.

I w
ant it to output \[Bullish, Bearish, Neutral\], instead it gives me something like 'The article suggests'

Is there some
 type of memory reset that might be causing the issue?

I am using the paid API version.

The outputs are given here:

(
'Bullish', 'Here are the')

first output is OPEN AI, which is working as intented. The second output is Claude.

https:/
/preview.redd.it/3p6cacef2g4e1.png?width=1080&format=png&auto=webp&s=c6e629c5d0aa419d0db9ffff216760362f538381

https://p
review.redd.it/jw35b7hg2g4e1.png?width=1051&format=png&auto=webp&s=13e60b1da444f6916446221db6824742e87ab915

And here ar
e the Few Shots:

https://preview.redd.it/iolm8jkd2g4e1.png?width=302&format=png&auto=webp&s=89ddd2cf480b351d71201e65870
da59937f84e7d


```
---

     
 
all -  [ Claude Doesn't Follow My Few Shot Prompts ](https://www.reddit.com/r/ClaudeAI/comments/1h4vtjl/claude_doesnt_follow_my_few_shot_prompts/) , 2024-12-03-0915
```
    claude_sentiment_clf = ChatAnthropic(
        model='claude-3-5-sonnet-20240620',
        temperature=0,
        max
_tokens=3,
        timeout=None,
        max_retries=2,
    )

Here I create an instance of the Claude 3.5 Sonnet and la
ter on using LangChain I pass it on a prompt to make a simple classification and within this prompt I have few shot exam
ples.

Initially it was working well and i had it restricted to 3 labels. Now it is trying to generate non-sense argumen
tation of why it thinks the classification is..

I run the same chains with OpenAI API and I don't have any issues what 
so ever.

What is causing this to happen?

Again to clarify, it outputs 3 tokens, but not the ones I want.

I want it to
 output \[Bullish, Bearish, Neutral\], instead it gives me something like 'The article suggests'

Is there some type of 
memory reset that might be causing the issue?

  
I am using the paid API version.

The outputs are given here:

('Bulli
sh', 'Here are the')

first output is OPEN AI, which is working as intented. The second output is Claude.

https://previ
ew.redd.it/pl8b73lc1g4e1.png?width=1225&format=png&auto=webp&s=b704b8911a3299e2f449fe94bb1512c5f830cda4

https://preview
.redd.it/rm4akq091g4e1.png?width=1051&format=png&auto=webp&s=19dd82885d1586c95fdd2db5c531cc8fafd50bd6

And here are the 
Few Shots:



https://preview.redd.it/3uwz6rth1g4e1.png?width=302&format=png&auto=webp&s=05815208ac2be654cc2599524f544cb
820735937


```
---

     
 
all -  [ Master Generative AI: LangChain & Hugging Face - 4\ Projects ](https://freewebcart.com/master-generative-ai-langchain-hugging-face-4projects/) , 2024-12-03-0915
```

```
---

     
 
all -  [ What is the process of extracting keywords from multiple pdfs. ](https://www.reddit.com/r/LangChain/comments/1h4r1xd/what_is_the_process_of_extracting_keywords_from/) , 2024-12-03-0915
```
https://preview.redd.it/2uucr4f3ke4e1.png?width=1316&format=png&auto=webp&s=1a9671e2d2b1160c18193b6b961f520a0aa96869

I 
am trying to implement a feature that can extract all the topics and its subtopics from pdfs or docs uploaded by the use
r. The issue is i can't figure out how do I do a vector search on the pdfs vector storage. I want this kind of structure
 attached in the image. I get it i can structurer the data using LLM, but how do I get all the topics from the pdfs uplo
aded. Either I can extract keywords from each chunk by giving it to llm but that will use soo manny tokens. I am new to 
langchain as well. Also show up a screenshot or something how do you guys setup your agents in js.  

```
---

     
 
all -  [ Chunking strategy for diverse sets of documents  ](https://www.reddit.com/r/LangChain/comments/1h4qm3l/chunking_strategy_for_diverse_sets_of_documents/) , 2024-12-03-0915
```
I am working on a RAG system for analysing and pulling information out of documents. These documents come from various c
lients and thus the structure and layout of the documents is very different from one document to the next, also the file
 types (can be pdf, docx). I am thus struggling to find a good method for chunking which I can apply to all documents th
at come in. At the moment I am simply pulling all of the text out of the document and then using semantic splitting. Ive
 also dabbled in using an agent to help me split but that has also not been super reliable.

Any tips on how I can handl
e diverse document sets?
```
---

     
 
all -  [ Advance Your Career: 100 Free Certified Courses on Udemy  ](https://www.reddit.com/r/Udemy/comments/1h4q2id/advance_your_career_100_free_certified_courses_on/) , 2024-12-03-0915
```
Selenium Webdriver with Java & TestNG Testing Framework

https://courze.org/selenium-webdriver-with-java-testng-testing-
framework/



Digital Marketing Professional Certification

https://courze.org/digital-marketing-professional-certificat
ion/



C\_SAC\_2415 SAP Analytics Cloud Practice Test

https://courze.org/c\_sac\_2415-sap-analytics-cloud-practice-tes
t/



Non-Engineers’ Guide to Tech Study Abroad: MS, Tech MBA, PhD

https://courze.org/non-engineers-guide-to-tech-study
-abroad-ms-tech-mba-phd/



PowerShell Regular Expressions: Regex Master Class

https://courze.org/powershell-regular-ex
pressions-regex-master-class/



AZ-900: Azure Fundamentals Complete Training \[6 Hrs.\]

https://courze.org/az-900-exam
-prep-mastering-azure-fundamentals/



The Complete C & C++ Programming Course – Mastering  C & C++

https://courze.org/
the-complete-c-c-programming-course-mastering-c-c/



Machine Learning – Fundamental of Python Machine Learning

https:/
/courze.org/machine-learning-fundamental-of-python-machine-learning/



Python for Data Science Pro: The Complete Master
y Course

https://courze.org/python-for-data-science-pro-the-complete-mastery-course/



PowerShell Functions Master Cla
ss

https://courze.org/powershell-functions-master-class/



C-level management: 20 models for business operations (4/5)


https://courze.org/c-level-management-100-models-for-business-success-part-4/



File & Folder Management Using PowerS
hell: For Beginners

https://courze.org/file-folder-management-using-powershell/



Accelerate Your Learning: Master Ang
ular 18 and ASP.NET 8.0

https://courze.org/accelerate-your-learning-master-angular-18-and-asp-net-8-0/



AWS Certified
 Cloud Practitioner (CLF-C02) Practice Exams

https://courze.org/aws-certified-cloud-practitioner-clf-c02-practice-exams
/



Master Microservices : From Learner to Lead Architect

https://courze.org/master-microservices-from-learner-to-lead
-architect/



Data-driven decisions: mastering market research strategies

https://courze.org/data-driven-decisions-mas
tering-market-research-strategies/



CSS, JavaScript And PHP Complete Course For Beginners

https://courze.org/css-java
script-and-php-complete-course-for-beginners/



Metasploit from Scratch: Beginner to Professional

https://courze.org/m
etasploit-from-scratch-beginner-to-professional/



Become a Hydra Expert: Advanced Brute Forcing Techniques

https://co
urze.org/become-a-hydra-expert-advanced-brute-forcing-techniques/



NMAP Mastery: Ultimate Guide to Network Scanning

h
ttps://courze.org/nmap-mastery-ultimate-guide-to-network-scanning/



SmartPhone Graphic Design

https://courze.org/smar
tphone-graphic-design/



Web Development Professional Certification

https://courze.org/web-development-professional-ce
rtification/



Master Generative AI: LangChain & Hugging Face – 4 Projects

https://courze.org/master-generative-ai-lan
gchain-hugging-face-4-projects/



SmartPhone 3D Logo and Mockup Design

https://courze.org/smartphone-3d-logo-and-mocku
p-design/



Entrepreneurship: 60 Day Startup Launch Blueprint

https://courze.org/entrepreneurship-60-day-startup-launc
h-blueprint/



NSE7\_OTS-7.2: Fortinet Network Security Expert Practice 2024

https://courze.org/nse7\_ots-7-2-fortinet
-network-security-expert-practice-2024/



NSE7\_PBC-6.4: Fortinet Network Security Expert Practice 2024

https://courze
.org/nse7\_pbc-6-4-fortinet-network-security-expert-practice-2024/



NSE7\_PBC-7.2: Fortinet Network Security Expert Pr
actice 2024

https://courze.org/nse7\_pbc-7-2-fortinet-network-security-expert-practice-2024/



NSE7\_SDW-6.4: Fortinet
 Network Security Expert Practice 2024

https://courze.org/nse7\_sdw-6-4-fortinet-network-security-expert-practice-2024/




25 Projects in 25 days of AI Development Bootcamp

https://courze.org/25-projects-in-25-days-of-ai-development-bootc
amp/



Comprehensive TypeScript Practice Exam: Basics to Advanced

https://courze.org/comprehensive-typescript-practice
-exam-basics-to-advanced/



Lean Six Sigma Green Belt Professional Certification

https://courze.org/lean-six-sigma-gre
en-belt-professional-certification/



Mastering HTML5 and CSS3 (Part 1 – Beginner Level)

https://courze.org/mastering-
html5-and-css3-part-1-beginner-level/



AZ-900: Microsoft Azure Fundamentals Practice Exam

https://courze.org/az-900-m
icrosoft-azure-fundamentals-practice-exam/



CLF-C02 AWS Certified Cloud Practitioner | Practice Exams

https://courze.
org/clf-c02-aws-certified-cloud-practitioner-exam-tests-oct-2024/



SAA-C03 AWS Certified Solutions Architect Associate
 Practice

https://courze.org/saa-c03-aws-certified-solutions-architect-associate-practice/



AZ-204: Microsoft Azure D
eveloper Associate | Practice Exam

https://courze.org/az-204-microsoft-azure-developer-associate-practice-exam/



DOP-
C02 AWS Certified DevOps Engineer-Professional Exam

https://courze.org/dop-c02-aws-certified-devops-engineer-profession
al-exam/



C++ And Java Training Crash Course for Beginners

https://courze.org/c-and-java-training-crash-course-2022/




The Complete C++ Programming Course from Basic to Expert

https://courze.org/the-complete-c-programming-course-from-b
asic-to-expert/




```
---

     
 
all -  [ PREVENTING FINE-TUNED LLM TO ANSWER OUTSIDE OF CONTEXT
 ](https://www.reddit.com/r/LangChain/comments/1h4po9o/preventing_finetuned_llm_to_answer_outside_of/) , 2024-12-03-0915
```
Hello. I have fine-tuned a model that is performing well and I added RAG as well.

The flow of my llm-rag goes like this
:

  
I ask it questions, and it first goes to vector db and extracts the top 5 hits. I then pass these top 5 hits to my
 **LLM prompt** as context and then my LLM answers.

The problem I'm facing is if the user asks anything outside of the 
domain, the vector db still returns the top 5 hits. I can't limit the hits based on score, as it returns 80 above for co
ntextual and non-contextual similarity. I am using [gte-large](https://huggingface.co/thenlper/gte-large) embedding mode
l ( i tried all-MiniLM-L6-v2 but it was not picking up good context hence i went with gte-large).

  
So even when I ask
 outside domain questions it returns hits and the hits go into LLM Prompt and it answers.

  
So is there any workaround
?

  
Thanks
```
---

     
 
all -  [ Web scraping package in Python ](https://www.reddit.com/r/LangChain/comments/1h4pkbw/web_scraping_package_in_python/) , 2024-12-03-0915
```
Currently , I'm trying to get content from the urls. Could you recommend some libraries to scrap websites?
```
---

     
 
all -  [ Best chunking method for PDFs with complex layout?
 ](https://www.reddit.com/r/LangChain/comments/1h4p54t/best_chunking_method_for_pdfs_with_complex_layout/) , 2024-12-03-0915
```
I am working on a RAG based PDF Query system , specifically for complex PDFs that contains multi column tables, images, 
tables that span across multiple pages, tables that have images inside them.

I want to find the best chunking strategy 
for such pdfs.

Currently i am using RecursiveCharacterTextSplitter. What worked best for you all for complex PDF?


```
---

     
 
all -  [ ChatBot In structured and Unstructured Data ](https://www.reddit.com/r/LangChain/comments/1h4omfr/chatbot_in_structured_and_unstructured_data/) , 2024-12-03-0915
```
I am developing a ChatBot based on Structured Data of MongoDB. I am generating Mongodb queries from LLM and searching th
e database based on that query. So, users can converse the Mongodb data in Natural language and I am converting the Mong
odb results into Natural language using LLM. 

Also,I am using Azure AI search with Azure OpenAI for the ChatBot based o
n PDFs and PPTs .

How can I combine both these cases? If user asks any question it can generate the queries based on th
e relevant data from PDFs of other Unstructured data or vice versa.

Any suggested approach with Langchain and Azure Ope
n AI where it can generate the response in natural language based on Structured data and unstructured data automatically
?

Please share your thoughts..
```
---

     
 
all -  [ Abstract: Automated Design of Agentic Tools ](https://www.reddit.com/r/LangChain/comments/1h4l6jz/abstract_automated_design_of_agentic_tools/) , 2024-12-03-0915
```
I had an idea earlier today that I'm opening up to some of the Reddit AI subs to crowdsource a verdict on its feasibilit
y, at either a theoretical or pragmatic level.

Some of you have probably heard about Shengran Hu's paper 'Automated Des
ign of Agentic Systems', which started from the premise that a machine built with a Turing-complete language can do anyt
hing if resources are no object, and humans can do some set of productive tasks that's narrower in scope than 'anything.
' Hu and his team reason that, considered over time, this means AI agents designed by AI agents will inevitably surpass 
hand-crafted, human-designed agents. The paper demonstrates that by using a 'meta search agent' to iteratively construct
 agents or assemble them from derived building blocks, the resulting agents will often see substantial performance impro
vements over their designer agent predecessors. It's a technique that's unlikely to be widely deployed in production app
lications, at least until commercially available quantum computers get here, but I and a lot of others found Hu's demons
tration of his basic premise remarkable.

Now, my idea. Consider the following situation: we have an agent, and this age
nt is operating is an unusually chaotic environment. The agent must handle a tremendous number of potential situations o
r conditions, a number so large that writing out the entire possible set of scenarios in the workflow is either impossib
le or prohibitively inconvenient. Suppose that the entire set of possible situations the agent might encounter was divid
ed into two groups: those that are predictable and can be handled with standard agentic techniques, and those that are n
ot predictable and cannot be anticipated ahead of the graph starting to run. In the latter case, we might want to add a 
special node to one or more graphs in our agentic system: a node that would design, instantiate, and invoke a custom too
l \*dynamically, on the spot\* according to its assessment of the situation at hand.

Following Hu's logic, if an intell
igence written in Python or TypeScript can in theory do anything, and a human developer is capable of something short of
 'anything', the artificial intelligence has a fundamentally stronger capacity to build *tools* *it can use* than a huma
n intelligence could.

Here's the gist: using this reasoning, the ADAS approach could be revised or augmented into a 'AD
AT' (Automated Design of Agentic Tools) approach, and on the surface, I think this could be implemented successfully in 
production here and now. Here are my assumptions, and I'd like input whether you think they are flawed, or if you think 
they're well-defined.

P1: A tool has much less freedom in its workflow, and is generally made of fewer steps, than a fu
ll agent.  
P2: A tool has less agency to alter the path of the workflow that follows its use than a complete agent does
.  
P3: ADAT, while less powerful/transformative to a workflow than ADAS, incurs fewer penalties in the form of compound
ing uncertainty than ADAS does, and contributes less complexity to the agentic process as well.  
**Q.E.D: An 'improvise
d tool generation' node would be a novel, effective measure when dealing with chaos or uncertainty in an agentic workflo
w, and perhaps in other contexts as well.**

I'm not an AI or ML scientist, just an ordinary GenAI dev, but if my reason
ing appears sound, I'll want to partner with a mathematician or ML engineer and attempt to demonstrate or disprove this.
 If you see any major or critical flaws in this idea, please let me know: I want to pursue this idea if it has the poten
tial I suspect it could, but not if it's ineffective in a way that my lack of mathematics or research training might be 
hiding from me.

Thanks, everyone!
```
---

     
 
all -  [ [0 YOE] New Grad seeking entry-level opportunities  in Data  analyst across Canada ](https://www.reddit.com/r/EngineeringResumes/comments/1h4ibi2/0_yoe_new_grad_seeking_entrylevel_opportunities/) , 2024-12-03-0915
```
Hey Guys, Need help in improving the resume, about to graduate soon . I am targeting any new grad / entry level role. Ap
plying to all over canada. i need all the criticism i can get . And Thank you in advance

Looking to optimize projects s
ection as well as work experience section

https://preview.redd.it/wcasdxjxzb4e1.jpg?width=5100&format=pjpg&auto=webp&s=
ec92d7026bcb4134cc4ba4112abe63b3050f4cec


```
---

     
 
all -  [ Resume Review - [0 YOE, New Grad, Data Related roles, Canada) ](https://www.reddit.com/r/resumesupport/comments/1h4i8iu/resume_review_0_yoe_new_grad_data_related_roles/) , 2024-12-03-0915
```
Hey Guys, Need help in improving the resume, about to graduate soon . I am targeting any new grad / entry level role. Ap
plying to all over canada.  i need all the criticism i can get . And Thank you in advance

  
Looking to optimize projec
ts section as well as work experience section

.

https://preview.redd.it/r6isutm8zb4e1.jpg?width=5100&format=pjpg&auto=
webp&s=95b4ba0308f4314f23ac53a77533ca74219cd1e0


```
---

     
 
all -  [ [0 YOE, Unemployed, Data Analyst, Canada]-  New grad Looking to land a full time data related role ](https://www.reddit.com/r/resumes/comments/1h4i62o/0_yoe_unemployed_data_analyst_canada_new_grad/) , 2024-12-03-0915
```
Need help in improving the resume, about to graduate soon . I am targeting any new grad / entry level role. Applying to 
all over canada.  i need all the criticism i can get . And Thank you in advance

https://preview.redd.it/n35ej3dnyb4e1.j
pg?width=5100&format=pjpg&auto=webp&s=d53c5e77821ab49cf9219fd29bd8c18deae00887


```
---

     
 
all -  [ What is the process of extracting keywords from multiple pdfs. ](https://www.reddit.com/r/Langchaindev/comments/1h4dyoi/what_is_the_process_of_extracting_keywords_from/) , 2024-12-03-0915
```
I am trying to implement a feature that can extract all the topics and its subtopics from pdfs or docs uploaded by the u
ser. The issue is i can't figure out how do I do a vector search on the pdfs vector storage. I want this kind of structu
re attached in the image. I get it i can structurer the data using LLM, but how do I get all the topics from the pdfs up
loaded. Either I can extract keywords from each chunk by giving it to llm but that will use soo manny tokens. I am new t
o langchain as well. Also show up a screenshot or something how do you guys setup your agents in js.

https://preview.re
dd.it/pn7apmyp0b4e1.png?width=1316&format=png&auto=webp&s=51cf4a5e0c82603f21f81258ae8284b0db1c5363


```
---

     
 
all -  [ [For Hire] Frontend and Backend Developer with the top and latest development technologies for a gre ](https://www.reddit.com/r/freelance_forhire/comments/1h4c8dm/for_hire_frontend_and_backend_developer_with_the/) , 2024-12-03-0915
```
Hi Redditors,

I'm Emad a Full-stack Web developer/engineer with 8 years of experience, and I'm looking for new projects
 to start working on, please take a look at my portfolio here [https://www.sx-portfolio.com](https://www.sx-portfolio.co
m) (let me know if you need more examples or direct links to live websites in the PM)

**Here is my skill set:**

**For 
Frontend:**

* HTML / CSS
* JS / ESNext
* Webpack / Gulp / Grunt / Gatsby
* React (With Redux, Zustand, or MobX)
* Next.
js
* Vuejs (With VueX)
* Angular
* TypeScript

**For Backend:**

* Node.js
* Python
* Express.js
* MongoDB
* Mongoose
* 
Nest.js
* GraphQL
* Meteor (with Apollo and React)
* TypeScript

**For AI-based projects:**

* Python
* Langchain
* Fast
API
* Uvicorn
* Pydantic

**For Desktop Apps:**

* Electron

**For Mobile Apps (iOS and Android):**

* React Native
* Ex
po

**For Design:**

* Photoshop
* Illustrator

**Here is my Resume:**  [My resume link!](http://www.sx-portfolio.com/we
bsite-resources/My%20resume.pdf)

**And here are some testimonials from my clients :)**

* [Slips](https://www.reddit.co
m/r/testimonials/comments/agfmwf/pos_swordx10_is_a_brilliant_developer_and_a/)
* [VidSync](https://www.reddit.com/r/test
imonials/comments/5gvz3d/pos_uswordx10_excellent_frontend_dev/)
* [Las Cruces Directory](https://www.reddit.com/r/testim
onials/comments/5hyks4/uswordx10_is_awesome/)
* [SigurenZalog](https://www.reddit.com/r/testimonials/comments/5jsfqf/pos
_quality_web_design_from_uswordx10/)
* [Bitlounge](https://www.reddit.com/r/testimonials/comments/5lh2pz/pos_uswordx10_t
op_fontend_devdesigner/)
* [Foxul](https://www.reddit.com/r/testimonials/comments/5l3p8j/pos_quality_web_coding_from_usw
ordx10/)
* [LootTicket](https://www.reddit.com/r/testimonials/comments/5nfh1j/pos_uswordx10_is_an_amazing_front_end_dev/
)

**My Pricing:**

I work hourly for $35/hr and my fixed prices depend on your project's complexity.

Don't worry about
 the price, just PM me with your project and I'm sure we can figure out something that goes with your budget. :)

If you
 have any questions don't hesitate to PM me and I will be more than happy to answer you :) and here is my portfolio agai
n if you need my contact details [www.sx-portfolio.com](https://www.sx-portfolio.com) (Click the red handle in the top-r
ight or pm me for it)
```
---

     
 
all -  [ Best approach for automating WhatsApp communication between field teams and management. ](https://www.reddit.com/r/LangChain/comments/1h4atay/best_approach_for_automating_whatsapp/) , 2024-12-03-0915
```

Looking for advice on automating our WhatsApp communication:

Current setup:
- Field team reports hourly data in Group 
A
- Staff reviews data
- Staff forwards to Group B (management)

Need to:
- Automate this while maintaining data review 
capability
- Store structured data from WhatsApp responses for reporting
- Generate automated reports from collected dat
a

Considering WhatsApp Business API with chatbot or third-party solutions.

Anyone implemented similar automation? Look
ing for platform recommendations and rough cost estimates.

Thanks!
```
---

     
 
all -  [ [For Hire] React, NEXT, Nest, Express, Langchain and Full Stack Developer. ](https://www.reddit.com/r/forhire/comments/1h4ai5f/for_hire_react_next_nest_express_langchain_and/) , 2024-12-03-0915
```
Hi Reddit! 👋  
I'm Sheryar, a Full Stack Developer skilled in **React, Next.js, NestJS, Node.js, AWS**, and **LangChain*
*. I specialize in:

✅ **Frontend**: Responsive, pixel-perfect UIs with React/Angular  
✅ **Backend**: Scalable APIs & m
icroservices (Node.js, NestJS)  
✅ **Databases**: Advanced PostgreSQL with JSON handling  
✅ **Payments**: Stripe integr
ation for secure transactions  
✅ **Cloud**: AWS deployments  
✅ **Chatbots & Voicebots**: Development with LangChain fo
r intelligent automation

**Recent Work**:  
🚗 Ride-sharing app with Stripe payments & live tracking  
📦 Urban logistics
 platform with multi-stop deliveries  
📊 Custom CRM with Twilio API integration  
🤖 Chatbot & Voicebot solutions for aut
omation and customer support

💰 **Rat**e: $15–$20/hour (negotiable)  
📧 DM me to discuss your project or view my portfol
io!  
**GitHub**: [storm1033](https://github.com/storm1033)

Let’s build something amazing together! 🚀
```
---

     
 
all -  [ Create your own basic RAG ](https://www.reddit.com/r/ArtificialInteligence/comments/1h48jdg/create_your_own_basic_rag/) , 2024-12-03-0915
```
[https://danielkliewer.com/2024/12/01/basic-rag](https://danielkliewer.com/2024/12/01/basic-rag)

In this guide I go thr
ough how to set up basic Retrieval Augmented Generation.

You can adapt it to your own projects.

I am really excited ab
out learning this. I knew what it was in concept but now I can use it for my own projects.

To save you a click the main
 juxt of the guide is the following code:

    import os
    import sys
    import glob
    from dotenv import load_dote
nv
    
    # Load environment variables from .env file
    load_dotenv()
    
    # Updated imports
    from langchain_
openai.embeddings import OpenAIEmbeddings
    from langchain_chroma.vectorstores import Chroma
    from langchain_openai
.llms import OpenAI
    from langchain.chains import RetrievalQA
    
    # Updated document loaders
    from langchain_
community.document_loaders import TextLoader, PyPDFLoader
    from langchain.text_splitter import RecursiveCharacterText
Splitter
    
    def main():
       # Load OpenAI API key
       openai_api_key = os.getenv('OPENAI_API_KEY')
       if
 not openai_api_key:
           print('Please set your OPENAI_API_KEY in the .env file.')
           sys.exit(1)
      

       # Define the folder path (change 'data' to your folder name)
       folder_path = './data'
       if not os.path.
exists(folder_path):
           print(f'Folder '{folder_path}' does not exist.')
           sys.exit(1)
      
       # 
Read all files in the folder
       documents = []
       for filepath in glob.glob(os.path.join(folder_path, '**/*.*'),
 recursive=True):
           if os.path.isfile(filepath):
               ext = os.path.splitext(filepath)[1].lower()
   
            try:
                   if ext == '.txt':
                       loader = TextLoader(filepath, encoding='utf
-8')
                       documents.extend(loader.load_and_split())
                   elif ext == '.pdf':
           
            loader = PyPDFLoader(filepath)
                       documents.extend(loader.load_and_split())
            
       else:
                       print(f'Unsupported file format: {filepath}')
               except Exception as e:

                   print(f'Error reading '{filepath}': {e}')
      
       if not documents:
           print('No docume
nts found in the folder.')
           sys.exit(1)
      
       # Split documents into chunks
       text_splitter = Rec
ursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
       texts = text_splitter.split_documents(documents)

      
       # Initialize embeddings and vector store
       embeddings = OpenAIEmbeddings()
       vector_store = Chro
ma(embedding_function=embeddings, persist_directory='./chroma_store')
      
       # Add texts to vector store in batch
es
       batch_size = 500  # Adjust this number as needed
       for i in range(0, len(texts), batch_size):
           
batch_texts = texts[i:i+batch_size]
           vector_store.add_documents(batch_texts)
      
       # Set up retriever

       retriever = vector_store.as_retriever(search_kwargs={'k': 3})
      
       # Set up the language model
       ll
m = OpenAI(temperature=0.7)
      
       # Create the RetrievalQA chain
       qa_chain = RetrievalQA.from_chain_type(

           llm=llm,
           chain_type='stuff',  # Options: 'stuff', 'map_reduce', 'refine', 'map_rerank'
           
retriever=retriever
       )
      
       # Interactive prompt for user queries
       print('The system is ready. You 
can now ask questions about the content.')
       while True:
           query = input('Enter your question (or type 'ex
it' to quit): ')
           if query.lower() in ('exit', 'quit'):
               break
           try:
               re
sponse = qa_chain.run(query)
               print(f'\nAnswer: {response}\n')
           except Exception as e:
         
      print(f'An error occurred: {e}\n')
              
    if __name__ == '__main__':
       main()

I hope you find th
is helpful. I am excited to explore the possibilities so if you have already used a RAG for your use case I would love t
o here what you use it for.

I think I will use it with the new AI agents set up I created which I described in a previo
us post.

I keep my blog free from monetization of any kind. I am just sharing this because I am excited about learning.
 Hope you enjoy.
```
---

     
 
all -  [ How I Built a Multi-Modal Search Pipeline with Voyager-3 ](https://www.reddit.com/r/LangChain/comments/1h47x6j/how_i_built_a_multimodal_search_pipeline_with/) , 2024-12-03-0915
```
Hey all,

I recently dove deep into multi-modal embeddings and built a pipeline that combines text and image data into a
 unified vector space. It’s a pretty cool way to connect and retrieve content across multiple modalities, so I thought I
’d share my experience and steps in case anyone’s interested in exploring something similar.



Here’s a breakdown of wh
at I did:

**Why Multi-Modal Embeddings?**

The main idea is to embed text and images into the same vector space, allowi
ng for seamless searches across modalities. For example, if you search for “cat,” the pipeline can retrieve related imag
es of cats *and* the text describing them—even if the text doesn’t explicitly mention the word “cat.”



**The Tools I U
sed**

1. **Voyager-3**: A state-of-the-art multi-modal embedding model.

2. **Weaviate**: A vector database for storing
 and querying embeddings.

3. **Unstructured**: A Python library for extracting content (text and images) from PDFs and 
other documents.

4. **LangGraph**: For building an end-to-end retrieval pipeline.



**How It Works**

1. **Extracting 
Text and Images**:

Using Unstructured, I pulled text and images from a sample PDF, chunked the content by title, and gr
ouped it into meaningful sections.

2. **Creating Multi-Modal Embeddings**:

I used Voyager-3 to embed both text and ima
ges into a shared vector space. This ensures the embeddings are contextually linked, even if the connection isn’t explic
itly clear in the data.

3. **Storing in Weaviate**:

The embeddings, along with metadata, were stored in Weaviate, whic
h makes querying incredibly efficient.

4. **Querying the Data**:

To test it out, I queried something like, “What does 
this magazine say about waterfalls?” The pipeline retrieved both text and images relevant to waterfalls—even if the text
 didn’t mention “waterfall” directly but was associated with a photo of one.

5. **End-to-End Pipeline**:

Finally, I bu
ilt a retrieval pipeline using LangGraph, where users can ask questions, and the pipeline retrieves and combines relevan
t text and images to answer.



**Why This Is Exciting**

This kind of multi-modal search pipeline has so many practical
 applications:

• Retrieving information from documents, books, or magazines that mix text and images.

• Making sense o
f visually rich content like brochures or presentations.

• Cross-modal retrieval—searching for text with images and vic
e versa.

I detailed the entire process in a [blog post here](https://medium.com/vectrix-ai/how-to-build-a-powerful-mult
i-modal-search-pipeline-with-voyager-3-6024ff98d9ca), where I also shared some code snippets and examples.

If you’re in
terested in trying this out, I’ve also uploaded the code to [GitHub](https://github.com/vectrix-ai/vectrix-graphs/blob/m
ain/examples/multi-model-embeddings.ipynb). Would love to hear your thoughts, ideas, or similar projects you’ve worked o
n!

Happy to answer any questions or go into more detail if you’re curious. 😊
```
---

     
 
all -  [ Virtual try on API  ](https://www.reddit.com/r/LangChain/comments/1h4119c/virtual_try_on_api/) , 2024-12-03-0915
```
Hey  im trying to build a platform for virtual try on, does anyone know a free api which I can use for building this 
```
---

     
 
all -  [ Need Opinions on a Unique PII and CCI Redaction Use Case with LLMs ](https://www.reddit.com/r/LangChain/comments/1h40ifi/need_opinions_on_a_unique_pii_and_cci_redaction/) , 2024-12-03-0915
```
I’m working on a **unique** Personally identifiable information **(PII) redaction use case**, and I’d love to hear your 
thoughts on it. Here’s the situation:

Imagine you have PDF documents of HR letters, official emails, and documents of t
hese sorts. Unlike typical PII redaction tasks, **we don’t want to redact information identifying the data subject.** Fo
r context, a 'data subject' refers to the individual whose data is being processed (e.g., the main requestor, or the per
son who the document is addressing). Instead, we aim to redact **information identifying other specific individuals (not
 the data subject)** in documents.

Additionally, we don’t want to redact **organization-related information**—just the 
personal details of individuals other than the data subject. Later on, we’ll expand the redaction scope to include **Com
mercially Confidential Information (CCI)**, which adds another layer of complexity.

**Example:** in an HR Letter, the d
ata subject might be 'John Smith,' whose employment details are being confirmed. Information about John (e.g., name, pos
ition, start date) would not be redacted. However, details about 'Sarah Johnson,' the HR manager, who is mentioned in th
e letter, should be redacted if they identify her personally (e.g., her name, her email address). Meanwhile, the company
's email (e.g., [hr@xyzCorporation.com](mailto:hr@xyzCorporation.com)) would be kept since it's organizational, not pers
onal.

# Why an LLM Seems Useful?

I think an LLM could play a key role in:

1. **Identifying the Data Subject**: The LL
M could help analyze the document context and pinpoint who the data subject is. This would allow us to create a clear li
st of **what to redact and what to exclude**.
2. **Detecting CCI**: Since CCI often requires understanding nuanced busin
ess context, an LLM would likely outperform traditional keyword-based or rule-based methods.

# The Proposed Solution:


* Start by using an LLM to **identify the data subject** and generate a list of entities to redact or exclude.
* Then, u
se **Presidio** (or a similar tool) for the actual redaction, ensuring scalability and control over the redaction proces
s.

# My Questions:

1. **Do you think this approach makes sense?**
2. **Would you suggest a different way to tackle thi
s problem?**
3. How well do you think an LLM will handle CCI redaction, given its need for contextual understanding?

I’
m trying to balance accuracy with efficiency and avoid overcomplicating things unnecessarily. Any advice, alternative to
ols, or insights would be greatly appreciated!

Thanks in advance!
```
---

     
 
all -  [ Please suggest resources for learning GenAI, Langchain, for other AI skills for web development ](https://www.reddit.com/r/developersIndia/comments/1h3z077/please_suggest_resources_for_learning_genai/) , 2024-12-03-0915
```
I am a MERN Stack Developer having good amount of experience of developing full stack application. I want to learn GenAI
 skills which I can integrate along with my applications. Can you please suggest me some good resources for learning Gen
AI, Langchain, RAG, etc ?
```
---

     
 
all -  [ Just Built an Agentic RAG Chatbot From Scratch—No Libraries, Just Code! ](https://www.reddit.com/r/LangChain/comments/1h3y86k/just_built_an_agentic_rag_chatbot_from_scratchno/) , 2024-12-03-0915
```
Hey everyone!

I’ve been working on building an Agentic RAG chatbot completely from scratch—no libraries, no frameworks,
 just clean, simple code. It’s pure HTML, CSS, and JavaScript on the frontend with FastAPI on the backend. Handles embed
dings, cosine similarity, and reasoning all directly in the codebase.

I wanted to share it in case anyone’s curious or 
thinking about implementing something similar. It’s lightweight, transparent, and a great way to learn the inner working
s of RAG systems.

If you find it helpful, giving it a ⭐ on GitHub would mean a lot to me: \[Agentic RAG Chat\](https://
github.com/AndrewNgo-ini/agentic\_rag). Thanks, and I’d love to hear your feedback! 😊
```
---

     
 
all -  [ Issues when prompting for credentials using Chainlit UI + Langgraph ](https://www.reddit.com/r/LangChain/comments/1h3u7ei/issues_when_prompting_for_credentials_using/) , 2024-12-03-0915
```
Hello,

I’m building a basic ReAct (Reasoning and Acting) AI agent using Langgraph and Chainlit. The LLM has access to a
 tool that requires the user to provide a username and a password before it can execute any actions.

The workflow is as
 follows:

1. User input  
2. Tool call  
3. Request for credentials  
4. Tool execution  
5. End

I am experiencing iss
ues with properly asking the user for their credentials. I am using Chainlit version 1.3.0.

Do you have any examples I 
can refer to?
```
---

     
 
all -  [ Is there any free embeddings model API? ](https://www.reddit.com/r/LangChain/comments/1h3irug/is_there_any_free_embeddings_model_api/) , 2024-12-03-0915
```
I am searching for an free embeddings model with API, not self hosted ones. I am building a personal project on Android 
application that does RAG. Now the catch is, Android studio doesn't support pytorch version >1.4. Though there are free 
versions that have very limited tokens, that isn't enough for me.
```
---

     
 
all -  [ Frontend for solopreneur project ](https://www.reddit.com/r/LangChain/comments/1h3i3u6/frontend_for_solopreneur_project/) , 2024-12-03-0915
```
Hi there :)   
I'm running a quick Agents-RAG prototype with n8n (on top of langchain) and Streamlit on GC for the front
 end.

Now I'm taking a look at some Streamlit alternatives. I was taking a look at openWebUI but I have no time to lear
n that stack. So I'm wondering if I should consider G Mesop or even Django.

I'm out of cognitive energy to learn much m
ore and would love to keep it simple. SO my questions are:  
\- Do you think it makes sense to move from Streamlit to Me
sop?   
\- What about the learning curve for Django?  
\- For simple GUI customizations (navigation, popups, etc), Does 
it make any sens to work on openwebui?

Don't even know if any of my questions makes any sense.... just need some input-
feedback-guidance
```
---

     
 
all -  [ Why is using a small model considered ineffective? I want to build a system that answers users' ques ](https://www.reddit.com/r/LangChain/comments/1h3esmm/why_is_using_a_small_model_considered_ineffective/) , 2024-12-03-0915
```
Why didn’t I train a small model on this data (questions and answers) and then using RAG to improve the accuracy of answ
ering the questions?

The advantages of a small model are that I can guarantee the confidentiality of the information, w
ithout sending it to an American company. It's fast and doesn’t require high infrastructure.

Why does a model with 67 m
illion parameters end up taking more than 20 MB when uploaded to Hugging Face?

However, most people criticize small mod
els. Some studies and trends from large companies are focused on creating small models specialized in specific tasks (ag
ent models), and some research papers suggest that this is the future!
```
---

     
 
all -  [ Output format adjustments  ](https://www.reddit.com/gallery/1h3c23c) , 2024-12-03-0915
```
I’m currently working on an app that helps visualise problem breakdowns in mind maps. As you can see I have problem gett
ing the text from the agents back in a way that’s nice to visualise, anyone got tricks ?
```
---

     
 
all -  [ Choosing an AI model for My knowledge management app  ](https://www.reddit.com/r/LangChain/comments/1h3b0kt/choosing_an_ai_model_for_my_knowledge_management/) , 2024-12-03-0915
```
Hi , I'm working on My internship project  that's a knowledge Management  system using fastapi  and I have to make a cha
tbot that generate answers based on the documents inserted in the database I used langchian and an open source model to 
generate the embeddings using  the pgvector extension in postgreSQL, the problem still in generating the answers from th
eses embeddeds I want a performing  free AI model and in the same time I can't install it locally . what you suggest ???
 
```
---

     
 
all -  [ (Resume review) Roast my Resume, 2024 grad. Career advice needed.  ](https://i.redd.it/67pjrd0jwz3e1.jpeg) , 2024-12-03-0915
```
Current role: Junior DevOps Engineer (started recently) 
Target role: Backend Developer

Basically I feel underpaid and 
undervalued in current job and want to switch. 

```
---

     
 
MachineLearning -  [ [P] Minima: local conversational retrieval augmented generation project (Ollama, Langchain, FastAPI, ](https://www.reddit.com/r/MachineLearning/comments/1h1pudq/p_minima_local_conversational_retrieval_augmented/) , 2024-12-03-0915
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

     
 
MachineLearning -  [ [P] Open-source declarative framework to build LLM applications - looking for contributors ](https://www.reddit.com/r/MachineLearning/comments/1gkpazh/p_opensource_declarative_framework_to_build_llm/) , 2024-12-03-0915
```
I've been building LLM-based applications, and was super frustated with all major frameworks - langchain, autogen, crewA
I, etc. They also seem to introduce a pile of unnecessary abstractions. It becomes super hard to understand what's going
 behind the curtains even for very simple stuff.

[So I just published this open-source framework GenSphere.](https://gi
thub.com/octopus2023-inc/gensphere) The idea is have something like **Docker for LLMs**. You build applications with YAM
L files, that define an execution graph. Nodes can be either LLM API calls, regular function executions or other graphs 
themselves. Because you can nest graphs easily, building complex applications is not an issue, but at the same time you 
don't lose control.

You basically code in YAML, stating what are the tasks that need to be done and how they connect. O
ther than that, you only write individual python functions to be called during the execution. No new classes and abstrac
tions to learn.

Its all open-source. **Now I'm looking for contributors** to adapt the framework for cycles and conditi
onal nodes - which would allow full-fledged agentic system building! Pls reach out  if you want to contribute, there are
 tons of things to do!

PS: [you can read the detailed docs here,](https://gensphere.readthedocs.io/en/latest/) And go o
ver this quick [Google Colab tutorial.](https://github.com/octopus2023-inc/gensphere/blob/main/examples/gensphere_tutori
al.ipynb)
```
---

     
