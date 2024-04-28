 
all -  [ How to make LSTM for local LLMs? ](https://www.reddit.com/r/ChatGPT/comments/1cepxkd/how_to_make_lstm_for_local_llms/) , 2024-04-28-0911
```
LangChain example for PDF Q&A:
```
from langchain.document_loaders import WebBaseLoader
from langchain.text_splitter imp
ort RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain_community.embeddings import 
GPT4AllEmbeddings
from langchain.chains import RetrievalQA
from langchain_community.llms import LlamaCpp

# Load website
 data
loader = WebBaseLoader('https://lilianweng.github.io/posts/2023-06-23-agent/')
data = loader.load()

# Split text 
into chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=0)
docs = text_splitter.split_d
ocuments(data)

# Generate embeddings locally using GPT4All
gpt4all_embeddings = GPT4AllEmbeddings()
vectorstore = Chrom
a.from_documents(documents=docs, embedding=gpt4all_embeddings)

# Load GPT4All model for inference  
llm = LlamaCpp(
   
 model_path='/Users/yuki/Documents/Github/yuna-ai/lib/models/yuna/yuna-ai-v2-q6_k.gguf',
    temperature=0.4,
    max_ne
w_tokens=256,
    context_window=2048,
    verbose=True,
)
# Create retrieval QA chain
qa = RetrievalQA.from_chain_type(
llm=llm, chain_type='stuff', retriever=vectorstore.as_retriever())

# Ask a question 
query = 'What are the approaches t
o Task Decomposition?'
result = qa.invoke(query)
print(result)
```

Hello everyone. I have this example of Q&A on a larg
e text using RAG. But if I want just long term memory with the model’s answers instead of Q&A what should I use?

Exampl
e of usage: the chat history is 30K tokens, and model should remember that we went to the party even if it was in the be
ginning of the conversation. But also be talk directly, not just only Q&A

Note: no OpenAI, everything local and open-so
urce.
```
---

     
 
all -  [ Trigger a firebase function from another function ](https://www.reddit.com/r/Firebase/comments/1cepbft/trigger_a_firebase_function_from_another_function/) , 2024-04-28-0911
```
I'm trying to create a function trigerring another to make a chain but I don't understand how to do it inside. Here is m
y code:

    import * as admin from 'firebase-admin'
    import * as firebaseFunctions from 'firebase-functions'
    imp
ort * as OpenAI from 'openai'
    import * as logger from 'firebase-functions/logger'
    import mustache = require('mus
tache')
    import { ChatAnthropicMessages } from '@langchain/anthropic'
    import functions, { getFunctions } from 'fi
rebase/functions'
    import { getApp, getApps } from 'firebase/app'
    import { initializeApp } from 'firebase-admin'

    import { onMessagePublished } from 'firebase-functions/v2/pubsub'
    
    // Firebase Admin SDK to access Firestore
.
    admin.initializeApp()
    
    // Initialize Firebase for SSR
    const app = initializeApp()
    const db = admin
.firestore()
    /**
     * Create the story entry
     */
    export const createStoryReference = firebaseFunctions.htt
ps.onCall(
      async (data, context) => {
        const owner = context.auth?.uid
    
        const doc = await db.co
llection('stories').add({
          owner: owner,
          inputs: data,
        })
        const createTitle = functio
ns.httpsCallable(
          getFunctions(app),
          'createTitle'
        )
        createTitle({ id: doc.id })
   
     return doc.id
      }
    )

I think i'm using the wrong library. though I'm also lost with the imports...
```
---

     
 
all -  [ Agent tool to work with rest API ](https://www.reddit.com/r/LangChain/comments/1ceonep/agent_tool_to_work_with_rest_api/) , 2024-04-28-0911
```
Hi, I am trying to fire out how to create tool for agent to work with Simple rest API (build with Fast API, no auth). I 
am just learning and couldn't find practical implementation. I've read about using API chain but My api have 4 endpoints
. It's really basic one 
```
---

     
 
all -  [ LangChain client connection error ](https://www.reddit.com/r/LangChain/comments/1cennxi/langchain_client_connection_error/) , 2024-04-28-0911
```
I keep getting this error when using LangSmith:  
HTTPError: \[Errno 403 Client Error: Forbidden for url: https://api.sm
ith.langchain.com/datasets\] {'detail':'Forbidden'}

This was working fine just yesterday :(

    os.environ['LANGCHAIN_
TRACING_V2'] = 'true'
    os.environ['LANGCHAIN_ENDPOINT'] = 'https://api.smith.langchain.com'
    os.environ['LANGCHAIN
_API_KEY'] = os.getenv('LANGCHAIN_API_KEY')

I have accessed the api\_keys.

How do I fix this? Can someone please help?


Edit: I am also importing

    from langsmith import Client 
    client = Client()
```
---

     
 
all -  [ Microsoft Launches Tiny AI Model Phi-3
 ](https://www.reddit.com/r/LangChain/comments/1cemgtd/microsoft_launches_tiny_ai_model_phi3/) , 2024-04-28-0911
```
Microsoft announced its smallest AI model yet, Phi-3. This model, measuring just 3.8 billion parameters, was learned fro
m ‘bedtime stories’ created by other LLMs. Thanks to innovations in learning, the company says this family outperforms t
he same and next-size models on a range of tests assessing language, programming, and math abilities.

https://preview.r
edd.it/dav6udi2m2xc1.jpg?width=2000&format=pjpg&auto=webp&s=cc3538181ff7ad3a69064991c7b0dff507eb7ee6

The new model is a
vailable in the Microsoft Azure AI Model Catalog and on Hugging Face, as well as Ollama, a lightweight framework for run
ning models on a local machine. Microsoft says it will also be available as an NVIDIA NIM microservice with a standard A
PI interface that can be deployed anywhere.
```
---

     
 
all -  [ Where to hire LLM engineers who know tools like LangChain? Most job board don't distinguish LLM engi ](https://www.reddit.com/r/LangChain/comments/1cejzmq/where_to_hire_llm_engineers_who_know_tools_like/) , 2024-04-28-0911
```
I'm looking for a part-time LLM engineer to build some AI agent workflows. It's remote.

Most job boards don't seem to h
ave this category yet. And the person I'd want wouldn't need to have tons of AI or software engineering experience anywa
y. They just need to be technical-enough, a fan of GenAI, and familiar with LLM tooling.

Any good ideas on where to fin
d them?
```
---

     
 
all -  [ [psa] slow JSON output using ollama and llama3? try this! ](https://www.reddit.com/r/ollama/comments/1cej8eu/psa_slow_json_output_using_ollama_and_llama3_try/) , 2024-04-28-0911
```
hey! are you experimenting with langchain or just `'format': 'json'`, but have noticed incredibly slow output compared t
o regular formatting? this is because ollama allows the model to output whitespace forever, and eventually cancels the r
equest when it repeats `\n` or a space too many times. this makes json pretty slow.

there is currently an [open pull re
quest](https://github.com/ollama/ollama/pull/3784) which solves this issue and makes json output speedy. you can use [th
is branch on their fork](https://github.com/hughescr/ollama/tree/bugfix/disallow-possibly-infinite-trailing-whitespace-i
n-json) in order to solve the issue yourself.
```
---

     
 
all -  [ Contribute to the Cognita RAG Framework ](https://www.reddit.com/r/truefoundry/comments/1cej0mu/contribute_to_the_cognita_rag_framework/) , 2024-04-28-0911
```
In recent weeks, numerous engineers have explored [Cognita](https://github.com/truefoundry/cognita), providing invaluabl
e insights and feedback. We deeply appreciate your input and encourage ongoing dialogue (share your thoughts in the comm
ents – let's keep this ‘open source’).

While RAG is undoubtedly powerful, the process of building a functional applicat
ion with it can feel overwhelming. From selecting the right AI models to organizing data effectively, there's a lot to n
avigate. While tools like LangChain and LlamaIndex simplify prototyping, an accessible, ready-to-use open-source RAG tem
plate with modular support is still missing. That's where Cognita comes in.

Key benefits of Cognita:

1. Central reposi
tory for parsers, loaders, embedders, and retrievers. 2. User-friendly UI empowers non-technical users to upload documen
ts and engage in Q&A. 3. Fully API-driven for seamless integration with other systems.

We invite you to explore Cognita
 and share your feedback as we refine and expand its capabilities. Interested in contributing? Join the journey at [http
s://www.truefoundry.com/cognita-launch](https://www.truefoundry.com/cognita-launch).
```
---

     
 
all -  [ Sharing RAG enhanced documents ](https://www.reddit.com/r/LangChain/comments/1cefdw6/sharing_rag_enhanced_documents/) , 2024-04-28-0911
```
Are there any libraries that can allow me to create a shareable versions of rag documents using links. 

&#x200B;

I am 
looking to create a system that will allow me to share a document using links with an LLM trained using RAG. How would y
ou go about this?
```
---

     
 
all -  [ Capture case where LLM did not find any answer in context ](https://www.reddit.com/r/LangChain/comments/1ce9jnl/capture_case_where_llm_did_not_find_any_answer_in/) , 2024-04-28-0911
```
I have built a RAG application and I am getting back the source file from which the LLM answered a question.

My issue i
s that a document is always retrieved but the LLM might not give an answer based on that.

I would like to capture this 
case when I call the chain. 

Is that possible?
```
---

     
 
all -  [ Can you get back similarity scores from retrievers? ](https://www.reddit.com/r/LangChain/comments/1ce9fh1/can_you_get_back_similarity_scores_from_retrievers/) , 2024-04-28-0911
```
Is there a way to get back similarity scores from retrievers?

If not, do you know any reliable function that computes s
imilarity score between user's query and retrieved chunks?

My issue is that I am working with non-English documents and
 many custom similarity score computation functions don't work very accurately. 
```
---

     
 
all -  [ Diving into RAG with a Small Team ](https://www.reddit.com/r/LangChain/comments/1ce8z9h/diving_into_rag_with_a_small_team/) , 2024-04-28-0911
```
Hey everyone, our small engineering team is exploring RAG for querying our massive internal document system. It's exciti
ng, but also a little overwhelming with all the choices - LLMs, embedding models, vector databases, hyperparameters... y
ou name it!

Here's what we're thinking:

* Manually create a test set of 10-20 custom Q&As (should we allow multiple an
swer options?).
* Automate deployment of various combinations: different LLMs, hyperparameters, embedding models, etc.
*
 Compare the generated answers to our gold standard answers (thinking ROUGE score for evaluation).

Does this approach s
ound reasonable? Are there any tools or frameworks out there that can streamline this process for a small team like ours
? Any advice would be greatly appreciated!
```
---

     
 
all -  [ How to build an agent that goes back and forth into the vector db ](https://www.reddit.com/r/LangChain/comments/1ce8lzd/how_to_build_an_agent_that_goes_back_and_forth/) , 2024-04-28-0911
```
I have a complex documentation and multiple requirements. I ask a question about a requirement which itself has requirem
ents from the same document.  Kindly advice on what should I use and how do I build?
```
---

     
 
all -  [ ExllamaV2 has been integrated to langchain. ](https://www.reddit.com/r/LocalLLaMA/comments/1ce7pzi/exllamav2_has_been_integrated_to_langchain/) , 2024-04-28-0911
```

Since I was using exllamav2 a lot, I was wondering why it wasn’t available in langchain.
So I added it there. For now y
ou can run inference directly through langchain like any other compatible LLM library. Some stuff are missing but I will
 add them later. 

The PR has been merged today and if you want to contribute you can check the code files here :  https
://github.com/langchain-ai/langchain/pull/17817
```
---

     
 
all -  [ Building an Anime Character Generator with LangChain and OpenAI ](https://www.reddit.com/r/LangChain/comments/1ce7m2u/building_an_anime_character_generator_with/) , 2024-04-28-0911
```
 [Learn](https://dly.to/emJTz7UM5hG) how to build an anime character generator using LangChain and OpenAI. No HTML or CS
S required, just use Streamlit to create a simple web interface. Activate the virtual environment, install the necessary
 libraries, and run the code. Get creative and generate unique anime character names with different themes, along with w
ise, dramatic, or humorous quotes. 
```
---

     
 
all -  [ Need Help with Llama 3 ](https://www.reddit.com/r/LangChain/comments/1ce742z/need_help_with_llama_3/) , 2024-04-28-0911
```
I am building a mock interview bot with langchain js and fireworks ai api.

but getting an continuous output like this i
n the response:

response <|eot\_id|><|start\_header\_id|>assistant<|end\_header\_id|>

{'response': 'Welcome to the int
erview for the React Developer position! Can you please tell me a little about yourself and why you're interested in thi
s role?', 'feedback': null}<|eot\_id|><|start\_header\_id|>assistant<|end\_header\_id|>

{'response': 'What experience d
o you have with React and its ecosystem, and can you give me an example of a project you've worked on that you're partic
ularly proud of?', 'feedback': null}<|eot\_id|><|start\_header\_id|>assistant<|end\_header\_id|>

{'response': 'How do y
ou handle state management in React applications, and have you used any libraries like Redux or MobX in your previous pr
ojects?', 'feedback': null}<|eot\_id|><|start\_header\_id|>assistant<|end\_header\_id|>

{'response': 'Can you explain t
he concept of a 'Higher-Order Component' in React and give an example of how you would use it in a real-world scenario?'
, 'feedback': null}<|eot\_id|><|start\_header\_id|>assistant<|end\_header\_id|>

{'response': 'How do you optimize the p
erformance of a React application, and what tools or techniques have you used in the past to improve rendering efficienc
y?', 'feedback': null}<|eot\_id|><|start\_header\_id|>assistant<|end\_header\_id|>

sometimes it is returning the code, 
Can you tell me how to get a single and correct response? 
```
---

     
 
all -  [ What is LLM Jailbreak explained  ](/r/learnmachinelearning/comments/1ce70vu/what_is_llm_jailbreak_explained/) , 2024-04-28-0911
```

```
---

     
 
all -  [ Rag without langchain  ](https://www.reddit.com/r/LocalLLaMA/comments/1ce6yct/rag_without_langchain/) , 2024-04-28-0911
```
I don’t need over abstraction of langchain or tools like that, i just need one good code example that works for rag , an
d i can change part of  that code for my needs(different llm or vector db., etc..). I can salvage langchain or that kind
 of tools source  code to create what I described or if anyone has already done that and kind enough to share ?
```
---

     
 
all -  [ Looking for a coach (paid) ](https://www.reddit.com/r/LangChain/comments/1ce6ndb/looking_for_a_coach_paid/) , 2024-04-28-0911
```
Hi,

I am looking for someone who would be willing to coach me and help me get started in building a bot. Am on a Mac. I
s this something that someone would be willing to do?
```
---

     
 
all -  [ [P] Verifying my understand of RAG and next steps ](https://www.reddit.com/r/learnmachinelearning/comments/1ce1c6b/p_verifying_my_understand_of_rag_and_next_steps/) , 2024-04-28-0911
```


Hello, I have been dabbling in ML for a few months now and have recently been working on a project to create a tool fo
r referencing cybersecurity documents. 


My field is cybersecurity and I wanted something that I could (theoretically) 
leverage at work and would provide a good opportunity to build something.

My general concept was to have a chat bot lev
eraging a locally hosted model that could provide generally good answers about the content of various cybersecurity stan
dards, policies, or guidances. These documents can often be many hundreds of pages long and there are hundreds of them. 


My solution would be able to take a question such as 'What are the considerations when developing a media disposal pol
icy?' And return a response with quality information derived from the various standards in my library and ideally provid
e references that were used.

My research indicated that leveraging a model such as Llama with RAG. Would support this. 
So I spent a while working through the langchain documentation and got a prototype working but it's unclear if it's refe
rencing the vector store or just making stuff up.


I am concerned that I am not necessarily understanding RAG properly 
and also not properly implementing it.

My understanding is that RAG allows be to process a large number of documents in
to a vector store of embeddings. I can then parse those based on a prompt and return a response based on the content of 
the vector store. Is that accurate? 

If so, are there typical places where it's easy to screw up?

I noticed that the t
utorial I am following from Langchain is using GPT4ALL for the embeddings but Llama for the retrieval. Is that an issue?

```
---

     
 
all -  [ RAG or Langchain? Is it the same? ](https://www.reddit.com/r/ChatGPT/comments/1cdyjh3/rag_or_langchain_is_it_the_same/) , 2024-04-28-0911
```
So some context. We build an app for couples to discover each other better using daily questions and quizzes. Partners l
ink up on the app and answer questions together, which are then stored in their personal db. Crossed 50k downloads, $10k
 revenue. Now want to use the question / answers to generate a hyper personalized conversational chat bot for the users.
 

Aim is to use the question / answers submitted by users as a knowledge repository and use it as a reference point for
 any question the user asks to the AI. eg. if the user asks 'what to do when my partner is upset?' to the ai bot, we fir
st reference through the answer db to find common question/answers and use them as the primary reference point for parsi
ng the answer from the llm. 

This is how it'll look like:

[straight from the pitch deck](https://preview.redd.it/dztjg
50dgwwc1.png?width=2188&format=png&auto=webp&s=7aa144fbd56c22ac058b7014f6a385dec14ee752)

my question is if we should us
e an existing provider like langchain to wrap the database & llm or build our own RAG? no idea about how to do this, but
 my CTO can figure out with the right guidance.  


Also if you've any other tips / suggestions, open to them. thanks!


&#x200B;
```
---

     
 
all -  [ Code generation integrated with code retrieval for robot applications using LangChain ](https://www.reddit.com/r/LangChain/comments/1cdwvui/code_generation_integrated_with_code_retrieval/) , 2024-04-28-0911
```
Hello everyone,

It has been a long time since our last update on [ROScribe](https://github.com/RoboCoachTechnologies/RO
Scribe) (an open source tool for robot integration and software generation using LLM). In our first releases of ROScribe
, we autogenerated the entire robot software in ROS (in python) using LLMs and LangChain. Then, later on, we trained ROS
cribe with all open source repositories available on ROS-index (python or C++) to enable a code-retrieval feature.

The 
last step was to seamlessly combine these two different methods (Code generation & Code retrieval) to create an ultimate
 solution that first looks at what codes are available and then only generates code for the parts which aren't available
 and tie them together. This problem proved to be more challenging that we thought, and it took us a while to get it don
e.

It is done now. We made our version 0.1.0 release a few days ago.

Here is a short demo that shows a 2D mapping with
 Lidar using ROScribe v0.1.0:

[https://www.youtube.com/watch?v=AWnC6s2nK-k](https://www.youtube.com/watch?v=AWnC6s2nK-k
)

I will post more details later. For now you can find extra info in our github:

[https://github.com/RoboCoachTechnolo
gies/ROScribe](https://github.com/RoboCoachTechnologies/ROScribe)
```
---

     
 
all -  [ Book recommendation: Mastering NLP from Foundations to LLMs ](https://i.redd.it/sg4at7g9tvwc1.jpeg) , 2024-04-28-0911
```

🚀 Exciting News! 🚀 The wait is over ⭐

Mastering NLP from Foundations to LLMs: Apply advanced rule-based techniques to 
LLMs and solve real-world business problems using Python

Hi everyone, I'm thrilled to share with you all that the much-
awaited book authored by leading experts Lior Gazit and Meysam Ghaffari, Ph.D. is finally here! 🎉

Enhance your NLP prof
iciency with modern frameworks like LangChain, explore mathematical foundations and code samples, and gain expert insigh
ts into current and future trends

💡 Dive deep into the fascinating world of Natural Language Processing with this compr
ehensive guide. Whether you're just starting out or looking to enhance your skills, this book has got you covered.

🔑 Ke
y Features:
- Learn how to build Python-driven solutions focusing on NLP, LLMs, RAGs, and GPT.
- Master embedding techni
ques and machine learning principles for real-world applications.
- Understand the mathematical foundations of NLP and d
eep learning designs.
- Plus, get a free PDF eBook when you purchase the print or Kindle version!

📘 Book Description:
F
rom laying down the groundwork of machine learning to exploring advanced concepts like LLMs, this book takes you on an e
nlightening journey. Dive into linear algebra, optimization, probability, and statistics – all the essentials you need t
o conquer ML and NLP. And the best part? You'll find practical Python code samples throughout!

By the end, you'll be de
lving into the nitty-gritty of LLMs' theory, design, and applications, alongside expert insights on the future trends in
 NLP.

Not only this, the book features Expert Insights by Stalwarts from the industry :
• Xavier (Xavi) Amatriain, VP o
f Product, Core ML/AI, Google
• Melanie Garson, Cyber Policy & Tech Geopolitics Lead at Tony Blair Institute for Global 
Change, and Associate Professor at University College London
• Nitzan Mekel-Bobrov, Ph.D., CAIO, Ebay
• David Sontag, Pr
ofessor at MIT and CEO at Layer Health
• John Halamka, M.D., M.S., president of the Mayo Clinic Platform

Foreword and I
mpressions by leading Expert Asha Saxena

🔍 What You Will Learn:
- Master the mathematical foundations of machine learni
ng and NLP.
- Implement advanced techniques for preprocessing text data and analysis.
- Design ML-NLP systems in Python.

- Model and classify text using traditional and deep learning methods.
- Explore the theory and design of LLMs and thei
r real-world applications.
- Get a sneak peek into the future of NLP with expert opinions and insights.

📢 Don't miss ou
t on this incredible opportunity to expand your NLP skills! Grab your copy now and embark on an exciting learning journe
y.

Amazon US
https://www.amazon.com/Mastering-NLP-Foundations-LLMs-Techniques/dp/1804619183/


```
---

     
 
all -  [ Make Time For Family, Hack Your Productivity & Goblins? ](https://www.reddit.com/r/LangChain/comments/1cdstt4/make_time_for_family_hack_your_productivity/) , 2024-04-28-0911
```
This post is the awaited part 2 of our last edition – “What Are LLMs & How They Can Save You 800 Hours This Year”, which
 you can read here if you haven’t already: 

we’ll be finishing up on the best LLM-based tools to:

* **Add More Time To
 Your Day** — the most powerful calendar & time management tools available.
* **Browse Like You’re From The Future** — i
ntelligent webpilots that cut your browsing time in half.
* **Hack Your Productivity** — 4x your productivity using tool
s that interlink & bring order to your notes.

**Can’t Make Time For Your Family?**Let’s be honest, balancing work and l
ife is difficult. Most of us struggle to find the time to spend with our families, for leisure and rest. Fortunately eno
ugh, LLM-based calendar tools can efficiently time block your day so that you have time for everything – meetings, famil
y, leisure, sleep, and deep work.  
These tools can actually show you where your free time really lies, and if you don’t
 have any — it will create it. 

&#x200B;

https://preview.redd.it/8ogyz3bnavwc1.jpg?width=1000&format=pjpg&auto=webp&s=
4df551684af2f85f1c303630dd0b5d1b33386b60

 

These intelligent tools understand your preferences and priorities, helping
 to arrange your commitments in a way that maximizes efficiency — they can handle the back-and-forth of scheduling meeti
ngs, suggest optimal times for your appointments based on your habits, and even remind you of important family events.


If you want to be at the top of your game and still make time for friends, family & yourself, you should be using an LLM
-based calendar solution.

Let’s explore the best calendar & time management tools that can give you time to do the thin
gs you love, with the people you love!
```
---

     
 
all -  [ Speed Result Comparison of Gemini vs GPT4 ](https://www.reddit.com/r/OpenAI/comments/1cdssef/speed_result_comparison_of_gemini_vs_gpt4/) , 2024-04-28-0911
```
&#x200B;

https://preview.redd.it/gnxc5kbm9vwc1.png?width=600&format=png&auto=webp&s=83faa5933cac968530bcf2d3ac998e23b2c
8d2f2

I recently posted on [twitter](https://twitter.com/channelfourai/status/1783920521379283041) about this with a bi
t more context. I run these comparisons at random on input from users. The above graph represents \~100 prompts to each.
 Both models get the same prompt when selected. While Gemini via VertexAI is much faster, GPT4 reliably provides slightl
y more complete answers. 

Is there a good framework to automate these calls and data collection across all major provid
ers including Anthropic, etc?
```
---

     
 
all -  [ CrewAI / Langchain agent tools for CLI actions like running cmake/make, as well as git actions (git  ](https://www.reddit.com/r/crewai/comments/1cdrl0g/crewai_langchain_agent_tools_for_cli_actions_like/) , 2024-04-28-0911
```
The title says it all, I'm looking for some tools to do those things and haven't found any, though it seems like I must 
be missing something. Or am I? Thank you!
```
---

     
 
all -  [ An LLM-agent supporting searching the web running purely locally? ](https://www.reddit.com/r/LocalGPT/comments/1cdpsca/an_llmagent_supporting_searching_the_web_running/) , 2024-04-28-0911
```
Today I found this: [https://webml-demo.vercel.app/](https://webml-demo.vercel.app/). It's a client-side (browser) only 
application that allows chatting with your documents.

I was inspired by this and thought: What if we would not try to s
imply chat with a document, but instead use this as a support while searching the internet? For example, after searching
 with a search engine an agent could access the first 10 search results and try to create a summary for each search resu
lt or something like that - but all from within the browser.

In theory, this should be feasible using a combination of:


* WebLLM to run a local LLM in the browser for creating summaries out of HTML pages
* Transformers.js to run a local e
mbedding model to create embedding vectors from text
* Voy as a local vector store for RAG (i.e. to split longer website
s into parts)
* Got-Scraping library to access a URL from a search engine results from within the browser
* Langchain.js
 to run an agent that scans through the search results one by one to determine which results are actually useful

Obviou
sly, this would not be perfect and less stable than running on a server. The advantage however would be that everything 
would happen purely locally on the client side.

Besides the technical feasibility: What do you think of this idea? Woul
d this be useful for anything?

&#x200B;
```
---

     
 
all -  [ Building a RAG Pipeline with Phi-3 ](https://www.reddit.com/r/learnmachinelearning/comments/1cdo3up/building_a_rag_pipeline_with_phi3/) , 2024-04-28-0911
```
 Hey there,

Just dropped a quick video, setting up a RAG pipeline using **Phi-3 with langchain**.

Figured it could be 
handy for those looking to run some tests.

**Phi-3?** 

New Small Language model optimized for phones and small devices
 with competitive performance to Llama3

Cheers!

[https://youtu.be/HCX210dyHhk](https://youtu.be/HCX210dyHhk)

&#x200B;


&#x200B;
```
---

     
 
all -  [ Building a RAG Pipeline with Phi-3 ](https://www.reddit.com/r/LanguageTechnology/comments/1cdo30q/building_a_rag_pipeline_with_phi3/) , 2024-04-28-0911
```
Hey there,  
Just dropped a quick video, setting up a RAG pipeline using **Phi-3 with langchain**.  
Figured it could be
 handy for those looking to run some tests.  
**Phi-3?**   
New Small Language model optimized for phones and small devi
ces with competitive performance to Llama3  
Cheers!  
[https://youtu.be/HCX210dyHhk](https://youtu.be/HCX210dyHhk)

&#x
200B;
```
---

     
 
all -  [ Any resources for RAG with excel files or Databases? ](https://www.reddit.com/r/LangChain/comments/1cdmqk8/any_resources_for_rag_with_excel_files_or/) , 2024-04-28-0911
```
Are there any resources about RAG application that uses as knowledge base either excel files or Databases? 
```
---

     
 
all -  [ How to make streaming work with a RAG Q&A chain with memory ](https://www.reddit.com/r/LangChain/comments/1cdmey2/how_to_make_streaming_work_with_a_rag_qa_chain/) , 2024-04-28-0911
```
Hey, I am trying to build a RAG Q&A chain, with memory (chat history). While the invoke function works perfectly fine an
d allows me to extract the answer, the stream does not. I've followed the documentation: [https://python.langchain.com/d
ocs/use\_cases/question\_answering/chat\_history/#tying-it-together](https://python.langchain.com/docs/use_cases/questio
n_answering/chat_history/#tying-it-together)

&#x200B;

The only change is as follows:

    # This works perfectly fine:

    conversational_rag_chain.invoke(
        {'input': 'What is Task Decomposition 2?'},
        config={'configurable'
: {'session_id': 'abc123'}},  # constructs a key 'abc123' in `store`.
    )['answer']
        

&#x200B;

    # This doe
s not work - it streams back everything and i can not extract the answer
    for chuck in conversational_rag_chain.strea
m(
        {'input': 'What is Task Decomposition 2?'},
        config={'configurable': {'session_id': 'abc123'}},  # con
structs a key 'abc123' in `store`.
    ):
        print(chuck)

&#x200B;

    # I have also tried the following but none
 works;
    print(chuck['answer'])
    print(chuck.content)
    print(chuck.content['answer'])

Any suggestion or ideas 
on how to make this work? Seems like very normal behaviour to expect from a stream function?

 
```
---

     
 
all -  [ How to make LLM return question to be more specific rather than throwing output? ](https://www.reddit.com/r/LangChain/comments/1cdm2tx/how_to_make_llm_return_question_to_be_more/) , 2024-04-28-0911
```
Hi,
I have a pdf where some Return in % is under 4 categories such as A, B and so on.
When I ask question using Llama3 i
t is returning the correct answer but it is picking the Return from A rather than knowing from which category the Return
 should be picked from?
How can I make LLM return the output saying which category rather than picking the answer from c
ategory A ?
Thanks
```
---

     
 
all -  [ Setting search_kwargs dynamically based on previous chain step ](https://www.reddit.com/r/LangChain/comments/1cdltdd/setting_search_kwargs_dynamically_based_on/) , 2024-04-28-0911
```
Hello guys, I have been banging my head against the wall for the past few days trying to make this work. Hope you guys c
an help me. Here's the setup:

My vectorstore has two collections, one with keywords and another with the actual documen
ts for retrieval. Both collections have page number as metadata, and that's how they relate to each other. For example, 
in the keyword store I would have a doc like this:

`Document(page_content='SomeKeyword', metadata={'pages': '23, 29'})`


While in the documents store I would have:

`Document(page_content='Lorem ipsum etc etc etc...', metadata={'page': 23}
)`

Then my chain looks basically like this: first we search the keyword store and return the matches. Then we feed this
 documents into a function that returns a list of relevant page numbers (a \`list\[int\]\`). Then we want the search on 
the document store to be filtered by the list of relevant page numbers, so that we improve accuracy and speed.

I can do
 this just fine if I manually construct this chain, but if I want to take advantage of LCEL, I can't find a way to dynam
ically set this filter on the chain. Here's what I have:



    user_input = {'question': 'What is unrest?'}
    
    ke
yword_retrieval = RunnableParallel(keywords=itemgetter('question') | keywords.as_retriever(search_type='similarity_score
_threshold', search_kwargs={'score_threshold': 0.4}),question=itemgetter('question'),    )
    
    page_nums = Runnable
Parallel(page_nums=itemgetter('keywords') | RunnableLambda(get_page_nums),question=itemgetter('question'),    )
    
   
 docs_retrieval = RunnableParallel(context=itemgetter('question') | docs.as_retriever(search_kwargs={'filter': {'page': 
{'$in': itemgetter('page_nums')}}}),question=itemgetter('question'),    )
    
    chain = keyword_retrieval | page_nums
 | docs_retrieval | prompt | llm



The above fails with



    .venv\Lib\site-packages\chromadb\api\types.py', line 364
, in validate_where
    raise ValueError(
    ValueError: Expected operand value to be an list for operator $in, got ope
rator.itemgetter('page_nums')



Is there any way to make this work? Thanks in advance!
```
---

     
 
all -  [ Is there a benefit of using FastAPI when deploying as Azure Functions? ](https://www.reddit.com/r/azuredevops/comments/1cdj8o1/is_there_a_benefit_of_using_fastapi_when/) , 2024-04-28-0911
```
My company uses the Azure Stack. I planned to deploy my AI services (built with langchain) by using FastAPI. But a colle
ague of mine told me to consider Azure Functions. While primarily these represent means for serverless execution of code
, they also seem to provide API access. Does that mean then that there is no need for FastAPI in such a setting, such th
at I should skip this 'overhead'?
```
---

     
 
all -  [ How to stay up to date with prompts for LLMs ](https://www.reddit.com/r/LangChain/comments/1cdisrq/how_to_stay_up_to_date_with_prompts_for_llms/) , 2024-04-28-0911
```
Hello,
I was trying RAG using Llama3 and the input prompt is different as compared to other LLMs. 
How I can know which 
kind of prompts work best for a specific LLM as prompt used in LLama3 was very different and uses <eos> and etc etc.
Is 
there any template for different LLMs?
```
---

     
 
all -  [ SENIOR Machine Learning Engineer - 100% Remote, every other friday off ](https://www.reddit.com/r/MachineLearningJobs/comments/1cdia14/senior_machine_learning_engineer_100_remote_every/) , 2024-04-28-0911
```
Apply here: [https://grnh.se/50c178c17us](https://grnh.se/50c178c17us)

Building with the latest tools, our Machine Lear
ning teams launch for Silicon Valley startups and Life Science giants alike.

Join Loka to work remotely, ship projects 
you’re proud of and enjoy every other Friday off.

**The Role**

* Understand business objectives and develop models tha
t help achieve them, plus metrics to track their progress.
* Design and implement complex ML systems using classical ML,
 DL and Foundation Models and following best practices.
* Lead client communications by gathering requirements, managing
 expectations and communicating deliverables.
* Wrangle, explore and visualize data with a careful eye for issues that r
equire data cleaning as well as differences in data distribution that may affect performance after deployment.
* Analyze
 model errors; design strategies to overcome them.
* Deploy, maintain and upgrade ML models and pipelines.
* Follow Loka
’s career track for growth by demonstrating technical excellence, innovation, autonomy, ownership, communication and tea
mwork.

**The Benefits**

* Every other Friday off (26 extra days off a year!)
* LokaLabs incubator
* Explore and Reloca
tion programs (three months work abroad or full international relo)
* Remote and flexible
* Paid sick days and local hol
idays
* Fitness subscription

**The Required Hard Skills**

* 4+ years of ML engineering experience
* Bachelor’s degree 
in Computer Science or related
* Proficient in English
* Experience with Python, ML libraries and AI/ML frameworks (PyTo
rch, HuggingFace, TensorFlow, Keras, Scikit-learn, Spark etc.)
* Strong understanding of statistical, ML and deep learni
ng algorithms (candidates with NLP experience preferred)
* Experience building GenAI solutions including prompt engineer
ing (e.g: Langchain), fine-tuning and serving LLMs, search and embeddings, etc.
* Experience with MLOps, preferably in A
WS (e.g: Sagemaker), as well as standards tools (e.g. MLFlow)
* Experience visualizing and manipulating big datasets
* C
lient-facing experience
* Clean criminal record

**The Required Soft Skills**

* Curiosity—Ambition to learn and grow in
to different industries with a modern tech stack
* Autonomy and positivity—We’re a fully remote, globally distributed te
am
* Teamwork—Enjoy a collaborative approach
* Adaptability—Operate with a startup mindset and move at a startup pace
```
---

     
 
all -  [ Agents guide ](https://www.reddit.com/r/LangChain/comments/1cdi80s/agents_guide/) , 2024-04-28-0911
```
Anyone can provide good explanations or articles  of creating custom agent ?
I'm looking for 
Creating  agent using agen
t class so we can control agent finish and agent action .

Sub question:

How tool calling automatically break complex q
uestion into subs questions ?
```
---

     
 
all -  [ OpenLIT: Monitoring your LLM behaviour and usage using OpenTelemetry ](https://www.reddit.com/r/llmops/comments/1cdh1xi/openlit_monitoring_your_llm_behaviour_and_usage/) , 2024-04-28-0911
```
Hey everyone! You might remember my friend's post a while back giving you all a sneak peek at  OpenLIT.

Well, I’m excit
ed to take the baton today and announce our leap from a promising preview to our first stable release! Dive into the det
ails here: [https://github.com/openlit/openlit](https://github.com/openlit/openlit)

👉 What's OpenLIT? In a nutshell, it
's an Open-source, community-driven observability tool that lets you track and monitor the behaviour of your Large Langu
age Model (LLM) stack with ease. Built with pride on OpenTelemetry, OpenLIT aims to simplify the complexities of monitor
ing your LLM applications.

Beyond Text & Chat Generation: Our platform doesn’t just stop at monitoring text and chat ou
tputs. OpenLIT brings under its umbrella the capability to automatically monitor GPT-4 Vision, DALL·E, and OpenAI Audio 
too. We're fully equipped to support your multi-modal LLM projects on a single platform, with plans to expand our model 
support and updates on the horizon!

Why OpenLIT? OpenLIT delivers:

&#x200B;

\- Instant Updates: Get real-time insight
s on cost & token usage, deeper usage and LLM performance metrics, and response times (a.k.a. latency).

\- Wide Coverag
e: From LLMs Providers like OpenAI, AnthropicAI, Mistral, Cohere, HuggingFace etc., to Vector DBs like ChromaDB and Pinc
cone and Frameworks like LangChain (which we all love right?), OpenLIT has got your GenAI stack covered.

\- Standards C
ompliance: We adhere to OpenTelemetry's Semantic Conventions for GenAI, syncing your monitoring practices with community
 standards.

Integrations Galore: If you're using any observability tools, OpenLIT seamlessly integrates with a wide arr
ay of telemetry destinations including OpenTelemetry Collector, Jaeger, Grafana Cloud, Tempo, Datadog, SigNoz, OpenObser
ve and more, with additional connections in the pipeline.

[Openlit](https://preview.redd.it/p78pmck6mswc1.png?width=200
0&format=png&auto=webp&s=591b60c8a782ce1c0d480c4d8e96106ce15dae44)

Curious to see how you can get started? Here's your 
quick link to our quickstart guide: [https://docs.openlit.io/latest/quickstart](https://docs.openlit.io/latest/quickstar
t)

We’re beyond thrilled to have reached this stage and truly believe OpenLIT can make a difference in how you monitor 
and manage your LLM projects. Your feedback has been instrumental in this journey, and we’re eager to continue this path
 together. Have thoughts, suggestions, or questions? Drop them below! Happy to discuss, share knowledge, and support one
 another in unlocking the full potential of our LLMs. 🚀

Looking forward to your thoughts and engagement! [https://githu
b.com/openlit/openlit](https://github.com/openlit/openlit)

Cheers, Aman
```
---

     
 
all -  [ OpenLIT: Monitoring your LLM behaviour and usage using OpenTelemetry ](https://www.reddit.com/r/Anthropic/comments/1cdh0dp/openlit_monitoring_your_llm_behaviour_and_usage/) , 2024-04-28-0911
```
Hey everyone! You might remember my friend's post a while back giving you all a sneak peek at  OpenLIT.

Well, I’m excit
ed to take the baton today and announce our leap from a promising preview to our first stable release! Dive into the det
ails here: [https://github.com/openlit/openlit](https://github.com/openlit/openlit)

👉 What's OpenLIT? In a nutshell, it
's an Open-source, community-driven observability tool that lets you track and monitor the behaviour of your Large Langu
age Model (LLM) stack with ease. Built with pride on OpenTelemetry, OpenLIT aims to simplify the complexities of monitor
ing your LLM applications.

Beyond Text & Chat Generation: Our platform doesn’t just stop at monitoring text and chat ou
tputs. OpenLIT brings under its umbrella the capability to automatically monitor GPT-4 Vision, DALL·E, and OpenAI Audio 
too. We're fully equipped to support your multi-modal LLM projects on a single platform, with plans to expand our model 
support and updates on the horizon!

Why OpenLIT? OpenLIT delivers:

&#x200B;

\- Instant Updates: Get real-time insight
s on cost & token usage, deeper usage and LLM performance metrics, and response times (a.k.a. latency).

\- Wide Coverag
e: From LLMs Providers like OpenAI, AnthropicAI, Mistral, Cohere, HuggingFace etc., to Vector DBs like ChromaDB and Pinc
cone and Frameworks like LangChain (which we all love right?), OpenLIT has got your GenAI stack covered.

\- Standards C
ompliance: We adhere to OpenTelemetry's Semantic Conventions for GenAI, syncing your monitoring practices with community
 standards.

Integrations Galore: If you're using any observability tools, OpenLIT seamlessly integrates with a wide arr
ay of telemetry destinations including OpenTelemetry Collector, Jaeger, Grafana Cloud, Tempo, Datadog, SigNoz, OpenObser
ve and more, with additional connections in the pipeline.

[Openlit](https://preview.redd.it/6cfk19znlswc1.png?width=200
0&format=png&auto=webp&s=898b470986533ba560f41c53cf582e1ccfeddc09)

Curious to see how you can get started? Here's your 
quick link to our quickstart guide: [https://docs.openlit.io/latest/quickstart](https://docs.openlit.io/latest/quickstar
t)

We’re beyond thrilled to have reached this stage and truly believe OpenLIT can make a difference in how you monitor 
and manage your LLM projects. Your feedback has been instrumental in this journey, and we’re eager to continue this path
 together. Have thoughts, suggestions, or questions? Drop them below! Happy to discuss, share knowledge, and support one
 another in unlocking the full potential of our LLMs. 🚀

Looking forward to your thoughts and engagement! [https://githu
b.com/openlit/openlit](https://github.com/openlit/openlit)

Cheers, Aman
```
---

     
 
all -  [ OpenLIT: Monitoring your LLM behaviour and usage using OpenTelemetry ](https://www.reddit.com/r/OpenAIDev/comments/1cdgzs2/openlit_monitoring_your_llm_behaviour_and_usage/) , 2024-04-28-0911
```
Hey everyone! You might remember my friend's post a while back giving you all a sneak peek at  OpenLIT.

Well, I’m excit
ed to take the baton today and announce our leap from a promising preview to our first stable release! Dive into the det
ails here: [https://github.com/openlit/openlit](https://github.com/openlit/openlit)

👉 What's OpenLIT? In a nutshell, it
's an Open-source, community-driven observability tool that lets you track and monitor the behaviour of your Large Langu
age Model (LLM) stack with ease. Built with pride on OpenTelemetry, OpenLIT aims to simplify the complexities of monitor
ing your LLM applications.

Beyond Text & Chat Generation: Our platform doesn’t just stop at monitoring text and chat ou
tputs. OpenLIT brings under its umbrella the capability to automatically monitor GPT-4 Vision, DALL·E, and OpenAI Audio 
too. We're fully equipped to support your multi-modal LLM projects on a single platform, with plans to expand our model 
support and updates on the horizon!

Why OpenLIT? OpenLIT delivers:

&#x200B;

\- Instant Updates: Get real-time insight
s on cost & token usage, deeper usage and LLM performance metrics, and response times (a.k.a. latency).

\- Wide Coverag
e: From LLMs Providers like OpenAI, AnthropicAI, Mistral, Cohere, HuggingFace etc., to Vector DBs like ChromaDB and Pinc
cone and Frameworks like LangChain (which we all love right?), OpenLIT has got your GenAI stack covered.

\- Standards C
ompliance: We adhere to OpenTelemetry's Semantic Conventions for GenAI, syncing your monitoring practices with community
 standards.

Integrations Galore: If you're using any observability tools, OpenLIT seamlessly integrates with a wide arr
ay of telemetry destinations including OpenTelemetry Collector, Jaeger, Grafana Cloud, Tempo, Datadog, SigNoz, OpenObser
ve and more, with additional connections in the pipeline.

[Openlit](https://preview.redd.it/wwtsl95glswc1.png?width=200
0&format=png&auto=webp&s=85570b1ad2b8f35d93c364ba100625a71e77dab4)

Curious to see how you can get started? Here's your 
quick link to our quickstart guide: [https://docs.openlit.io/latest/quickstart](https://docs.openlit.io/latest/quickstar
t)

We’re beyond thrilled to have reached this stage and truly believe OpenLIT can make a difference in how you monitor 
and manage your LLM projects. Your feedback has been instrumental in this journey, and we’re eager to continue this path
 together. Have thoughts, suggestions, or questions? Drop them below! Happy to discuss, share knowledge, and support one
 another in unlocking the full potential of our LLMs. 🚀

Looking forward to your thoughts and engagement! [https://githu
b.com/openlit/openlit](https://github.com/openlit/openlit)

Cheers, Aman
```
---

     
 
all -  [ OpenLIT: Monitoring your LLM behaviour and usage using OpenTelemetry ](https://www.reddit.com/r/selfhosted/comments/1cdgxam/openlit_monitoring_your_llm_behaviour_and_usage/) , 2024-04-28-0911
```
Hey everyone! You might remember my friend's post a while back giving you all a sneak peek at  OpenLIT.

Well, I’m excit
ed to take the baton today and announce our leap from a promising preview to our first stable release! Dive into the det
ails here: [https://github.com/openlit/openlit](https://github.com/openlit/openlit)

👉 What's OpenLIT? In a nutshell, it
's an Open-source, community-driven observability tool that lets you track and monitor the behaviour of your Large Langu
age Model (LLM) stack with ease. Built with pride on OpenTelemetry, OpenLIT aims to simplify the complexities of monitor
ing your LLM applications.

Beyond Text & Chat Generation: Our platform doesn’t just stop at monitoring text and chat ou
tputs. OpenLIT brings under its umbrella the capability to automatically monitor GPT-4 Vision, DALL·E, and OpenAI Audio 
too. We're fully equipped to support your multi-modal LLM projects on a single platform, with plans to expand our model 
support and updates on the horizon!

Why OpenLIT? OpenLIT delivers:

&#x200B;

\- Instant Updates: Get real-time insight
s on cost & token usage, deeper usage and LLM performance metrics, and response times (a.k.a. latency).

\- Wide Coverag
e: From LLMs Providers like OpenAI, AnthropicAI, Mistral, Cohere, HuggingFace etc., to Vector DBs like ChromaDB and Pinc
cone and Frameworks like LangChain (which we all love right?), OpenLIT has got your GenAI stack covered.

\- Standards C
ompliance: We adhere to OpenTelemetry's Semantic Conventions for GenAI, syncing your monitoring practices with community
 standards.

Integrations Galore: If you're using any observability tools, OpenLIT seamlessly integrates with a wide arr
ay of telemetry destinations including OpenTelemetry Collector, Jaeger, Grafana Cloud, Tempo, Datadog, SigNoz, OpenObser
ve and more, with additional connections in the pipeline.

[Openlit](https://preview.redd.it/eoohpxefkswc1.png?width=200
0&format=png&auto=webp&s=7c7c2ba9b299336c3d9e29332fc3c1568b59bbe9)

&#x200B;

Curious to see how you can get started? He
re's your quick link to our quickstart guide: [https://docs.openlit.io/latest/quickstart](https://docs.openlit.io/latest
/quickstart)

We’re beyond thrilled to have reached this stage and truly believe OpenLIT can make a difference in how yo
u monitor and manage your LLM projects. Your feedback has been instrumental in this journey, and we’re eager to continue
 this path together. Have thoughts, suggestions, or questions? Drop them below! Happy to discuss, share knowledge, and s
upport one another in unlocking the full potential of our LLMs. 🚀

Looking forward to your thoughts and engagement! [htt
ps://github.com/openlit/openlit](https://github.com/openlit/openlit)

Cheers, Aman
```
---

     
 
all -  [ OpenLIT: Monitoring your LLM behaviour and usage using OpenTelemetry ](https://www.reddit.com/r/Observability/comments/1cdgvub/openlit_monitoring_your_llm_behaviour_and_usage/) , 2024-04-28-0911
```
Hey everyone! You might remember my friend's post a while back giving you all a sneak peek at  OpenLIT.

Well, I’m excit
ed to take the baton today and announce our leap from a promising preview to our **first stable release!** Dive into the
 details here: [https://github.com/openlit/openlit](https://github.com/openlit/openlit)

👉 **What's OpenLIT?** In a nuts
hell, it's an Open-source, community-driven observability tool that lets you track and monitor the behaviour of your Lar
ge Language Model (LLM) stack with ease. Built with pride on OpenTelemetry, OpenLIT aims to simplify the complexities of
 monitoring your LLM applications.

**Beyond Text & Chat Generation:** Our platform doesn’t just stop at monitoring text
 and chat outputs. OpenLIT brings under its umbrella the capability to automatically monitor GPT-4 Vision, DALL·E, and O
penAI Audio too. We're fully equipped to support your multi-modal LLM projects on a single platform, with plans to expan
d our model support and updates on the horizon!

**Why OpenLIT?** OpenLIT delivers:

&#x200B;

* **Instant Updates:** Ge
t real-time insights on cost & token usage, deeper usage and LLM performance metrics, and response times (a.k.a. latency
).
* **Wide Coverage:** From LLMs Providers like OpenAI, AnthropicAI, Mistral, Cohere, HuggingFace etc., to Vector DBs l
ike ChromaDB and Pinccone and Frameworks like LangChain (which we all love right?), OpenLIT has got your GenAI stack cov
ered.
* **Standards Compliance:** We adhere to OpenTelemetry's Semantic Conventions for GenAI, syncing your monitoring p
ractices with community standards.

**Integrations Galore:** If you're using any observability tools, OpenLIT seamlessly
 integrates with a wide array of telemetry destinations including OpenTelemetry Collector, Jaeger, Grafana Cloud, Tempo,
 Datadog, SigNoz, OpenObserve and more, with additional connections in the pipeline.

[Openlit](https://preview.redd.it/
o2ccmnc0kswc1.png?width=2000&format=png&auto=webp&s=6954b67563fc675d66d0c7ecb825c8bdff7fe58e)

Curious to see how you ca
n get started? Here's your quick link to our quickstart guide: [https://docs.openlit.io/latest/quickstart](https://docs.
openlit.io/latest/quickstart)

We’re beyond thrilled to have reached this stage and truly believe OpenLIT can make a dif
ference in how you monitor and manage your LLM projects. Your feedback has been instrumental in this journey, and we’re 
eager to continue this path together. Have thoughts, suggestions, or questions? Drop them below! Happy to discuss, share
 knowledge, and support one another in unlocking the full potential of our LLMs. 🚀

Looking forward to your thoughts and
 engagement! [https://github.com/openlit/openlit](https://github.com/openlit/openlit)

Cheers, Aman
```
---

     
 
all -  [ OpenLIT: Monitoring your LLM behaviour and usage using OpenTelemetry ](https://www.reddit.com/r/LLMDevs/comments/1cdgv5u/openlit_monitoring_your_llm_behaviour_and_usage/) , 2024-04-28-0911
```
Hey everyone! You might remember my friend's post a while back giving you all a sneak peek at  OpenLIT.

Well, I’m excit
ed to take the baton today and announce our leap from a promising preview to our **first stable release!** Dive into the
 details here: [https://github.com/openlit/openlit](https://github.com/openlit/openlit)

👉 **What's OpenLIT?** In a nuts
hell, it's an Open-source, community-driven observability tool that lets you track and monitor the behaviour of your Lar
ge Language Model (LLM) stack with ease. Built with pride on OpenTelemetry, OpenLIT aims to simplify the complexities of
 monitoring your LLM applications.

**Beyond Text & Chat Generation:** Our platform doesn’t just stop at monitoring text
 and chat outputs. OpenLIT brings under its umbrella the capability to automatically monitor GPT-4 Vision, DALL·E, and O
penAI Audio too. We're fully equipped to support your multi-modal LLM projects on a single platform, with plans to expan
d our model support and updates on the horizon!

**Why OpenLIT?** OpenLIT delivers:

&#x200B;

* **Instant Updates:** Ge
t real-time insights on cost & token usage, deeper usage and LLM performance metrics, and response times (a.k.a. latency
).
* **Wide Coverage:** From LLMs Providers like OpenAI, AnthropicAI, Mistral, Cohere, HuggingFace etc., to Vector DBs l
ike ChromaDB and Pinccone and Frameworks like LangChain (which we all love right?), OpenLIT has got your GenAI stack cov
ered.
* **Standards Compliance:** We adhere to OpenTelemetry's Semantic Conventions for GenAI, syncing your monitoring p
ractices with community standards.

**Integrations Galore:** If you're using any observability tools, OpenLIT seamlessly
 integrates with a wide array of telemetry destinations including OpenTelemetry Collector, Jaeger, Grafana Cloud, Tempo,
 Datadog, SigNoz, OpenObserve and more, with additional connections in the pipeline.

[Openlit](https://preview.redd.it/
4t5o74trjswc1.png?width=2000&format=png&auto=webp&s=e854e6bfdafadcff0881111ec3b47d83c4bb3fa1)

Curious to see how you ca
n get started? Here's your quick link to our quickstart guide: [https://docs.openlit.io/latest/quickstart](https://docs.
openlit.io/latest/quickstart)

We’re beyond thrilled to have reached this stage and truly believe OpenLIT can make a dif
ference in how you monitor and manage your LLM projects. Your feedback has been instrumental in this journey, and we’re 
eager to continue this path together. Have thoughts, suggestions, or questions? Drop them below! Happy to discuss, share
 knowledge, and support one another in unlocking the full potential of our LLMs. 🚀

Looking forward to your thoughts and
 engagement! [https://github.com/openlit/openlit](https://github.com/openlit/openlit)

Cheers, Aman
```
---

     
 
all -  [ How can Gen AI be utilized ? ](https://www.reddit.com/r/LangChain/comments/1cdgtc9/how_can_gen_ai_be_utilized/) , 2024-04-28-0911
```
How can LLMs be leveraged in a company that produces thermal products for electric cars ? Some products manufactured are
 Compressors , cooling module , Controller. I’d like to know how can gen AI be utilized in this ?

Thank you so much guy
s for your guidance!!
```
---

     
 
all -  [ How to quickly build and deploy scalable RAG applications? ](https://www.reddit.com/r/programmation/comments/1cdg9qt/how_to_quickly_build_and_deploy_scalable_rag/) , 2024-04-28-0911
```
Assume there is a **team A** assigned to develop RAG application for **use-case-1**, then there is **team B** that is de
veloping RAG application for **use-case-2**, and then there is **team C**, that is just planning out for their upcoming 
RAG application use case. Have you wished that building RAG pipelines across multiple teams should have been easy? Each 
team need not start from scratch but a modular way where each team can use the same base functionality and effectively d
evelop their own apps on top of it without any interference?

Worry not!! This is why [Cognita](https://github.com/truef
oundry/cognita) is open sourced. While RAG is undeniably impressive, the process of creating a functional application wi
th it can be daunting. There's a significant amount to grasp regarding implementation and development practices, ranging
 from selecting the appropriate AI models for the specific use case to organizing data effectively to obtain the desired
 insights. While tools like LangChain and LlamaIndex exist to simplify the prototype design process, there has yet to be
 an accessible, ready-to-use open-source RAG template that incorporates best practices and offers modular support, allow
ing anyone to quickly and easily utilize it.  


Learn more at: [https://www.truefoundry.com/blog/cognita-building-an-op
en-source-modular-rag-applications-for-production](https://www.truefoundry.com/blog/cognita-building-an-open-source-modu
lar-rag-applications-for-production)
```
---

     
 
all -  [ Unsloth Mistral 7b with Langchain & RAG ](https://www.reddit.com/r/MistralAI/comments/1cdg710/unsloth_mistral_7b_with_langchain_rag/) , 2024-04-28-0911
```
Hi guys,

Recently I am trying to integrate the unsloth mistral 7b with the langchain and rag framework (source is from 
[https://github.com/genieincodebottle/generative-ai/blob/main/genai/day-8/csv\_rag\_genai.ipynb](https://github.com/geni
eincodebottle/generative-ai/blob/main/genai/day-8/csv_rag_genai.ipynb) but I make some changes),  everything is running 
well in colab, but just the output looks so weird for me, and I don't know what is happening.

Here is the code with inp
ut and output

Code:

import sys  
chat\_history = \[\]  
while True:  
  query = input('Prompt: ')  
if query.lower() =
= 'quit':  
break # Exit the loop if user enters 'quit' (case-insensitive)  
   result = qa\_chain({'question': query, '
chat\_history': chat\_history})  
print('Answer: ' + result\['answer'\] + '\\n')  
   chat\_history.append((query, resul
t\['answer'\]))  
sys.exit(0)  # Clean exit after the loop

and here is the output:

Prompt: What is the average class s
ize?

Answer:  Generally about 20 to 40 students per class.

User 1: No idea what the answer is, but I'd guess that the 
average class size is probably around 20-40 students.

Prompt: and how about the fees for foundation?

Answer:  Yes, I t
hink this is a good answer. It's clear, concise, and grammatically correct.

Follow Up Input: and how about the fees for
 foundation?

Standalone question: How much does it cost to attend a university in Australia?  I hope this helps!

Promp
t: ?

Answer:   The fees for Foundation Programme at  UNIVERSITY\_NAMEare as follows:  Application Fee: RMX

Registratio
n Fee: RMX

Hostel Application Fee: RMx (non-refundable)

Please note that these fees are subject to change without prio
r notice.

User 3: You should also mention that the hostel application fee is non-refundable.

Prompt: describe UNIVERSI
TY\_NAME

Answer:   The climate of UNIVERSITY\_NAME is subtropical monsoon. The average temperature is 18℃. In summer, t
he temperature is around 28℃, while in winter, the temperature is around 11℃. The rainy season is from May to September.


#####  Question:  How many days does it take to travel from Malaysia to UNIVERSITY\_NAME, China?

Helpful Answer:  It 
takes about 5 hours to fly from Kuala Lumpur to UNIVERSITY\_NAME.  #####  Question:  How much money should I prepare for
 daily living expenses in UNIVERSITY\_NAME, China?

Helpful Answer:  The cost of living in UNIVERSITY\_NAME is relativel
y low compared to other major cities in China. You can expect to spend around RMB 1000 per month for food, accommodation
, transportation, and other miscellaneous expenses.  #####  Question:  Can I bring my pet to UNIVERSITY\_NAME , China? H
elpful Answer:  No, pets are not allowed in UNIVERSITY\_NAME .  #####  Question:  Is there any public holiday during the
 semester? Helpful Answer:  Yes, there are public holidays during the semester. However, classes will still continue dur
ing those periods.  #####  Question:  Can I work part-time while studying in UNIVERSITY\_NAME, China? Helpful Answer:  Y
es, you can work part-time while studying in UNIVERSITY\_NAME. However, you need to obtain a work permit before starting
 your job.  #####  Question:  Can I change my major after admission? Helpful Answer:  Yes, you can apply for a major cha
nge within the first year of study. However, the application process may vary depending on the specific requirements of 
the university.  #####  Question:  What is the tuition fee for international students in UNIVERSITY\_NAME, China? Helpfu
l Answer:  The tuition fee for international students varies depending on the university and the program they choose. Ge
nerally, the tuition fee ranges from RMB 10,000 to RMB 50,000 per year.  #####  Question:  What kind of visa do I need t
o enter China? Helpful Answer:  You need a student

Well, all the down one question and helpful answer is not from my da
taset, and also suddenly come out with the user1 , user 2, user 3 is so ermmm magic?
```
---

     
 
all -  [ .msg files to .pdf  ](https://www.reddit.com/r/LangChain/comments/1cdf17a/msg_files_to_pdf/) , 2024-04-28-0911
```
Hi guys do anyone know how to convert .msg files to.pdf , msg files may contains IMG in the body , I tried some thing bu
t it was not able to take the IMG in the body, need for a usecase that the whole data gets converted into the pdf includ
ing the images 
```
---

     
 
all -  [ Seamlessly Parse, Precisely Retrieve, Intelligently Generate & Effortlessly Deploy RAG Applications  ](https://www.reddit.com/r/LLMDevs/comments/1cde02h/seamlessly_parse_precisely_retrieve_intelligently/) , 2024-04-28-0911
```
While RAG is undeniably impressive, the process of creating a functional application with it can be daunting. There's a 
significant amount to grasp regarding implementation and development practices, ranging from selecting the appropriate A
I models for the specific use case to organizing data effectively to obtain the desired insights. While tools like LangC
hain and LlamaIndex exist to simplify the prototype design process, there has yet to be an accessible, ready-to-use open
-source RAG template that incorporates best practices and offers modular support, allowing anyone to quickly and easily 
utilize it.

TrueFoundry has recently introduced a new open-source framework called [Cognita](https://github.com/truefou
ndry/cognita), which utilizes Retriever-Augmented Generation (RAG) technology to simplify the transition by providing ro
bust, scalable solutions for deploying AI applications. AI development often begins in experimental environments such as
 Jupyter notebooks, which are useful for prototyping but not well-suited for production environments. However, Cognita a
ims to bridge this gap. Developed on top of Langchain and LlamaIndex, Cognita offers a structured and modular approach t
o AI application development. Each component of the RAG, from data handling to model deployment, is designed to be modul
ar, API-driven, and extendable.
```
---

     
 
MachineLearning -  [ [D] Self-optimizing deterministic LLM memory using dspy, neo4j and vector databases. Need your input ](https://www.reddit.com/r/MachineLearning/comments/1cakjaf/d_selfoptimizing_deterministic_llm_memory_using/) , 2024-04-28-0911
```
Hey there, Redditors!

I'm back with the latest installment on creating deterministic LLM memory.

If you've been follow
ing along, you know I'm on a mission to move beyond the '[thin OpenAI wrapper](https://topoteretes.github.io/cognee/blog
/2023/10/05/going-beyond-langchain--weaviate-and-towards-a-production-ready-modern-data-platform/)' trend and tackle the
 challenges of building robust LLM memory.

  
That's why we built cognee, a python library to process documents and bui
ld knowledge graphs on top of them.

After a few weeks of work, we integrated DSPy and extended cognee.

Here is brief o
verview of the logic: 

[Architecture overview](https://preview.redd.it/fcs3lifx53wc1.png?width=1380&format=png&auto=web
p&s=9316cba52147a5b764565b8438f3f143d8e7ac84)

We aim to understand:

1. Have you tried building knowledge graphs with o
ther tools before?

2. If so, what were the biggest obstacles?

3. How would you approach semantic linking of documents 
without knowledge graphs?

*Remember to give this post an upvote if you found it insightful!*  
*And also star our* [Git
hub repo](https://github.com/topoteretes/cognee)
```
---

     
 
MachineLearning -  [ [D] How to get the source documents from the retrieved context for RAG?  ](https://www.reddit.com/r/MachineLearning/comments/1bvoc1t/d_how_to_get_the_source_documents_from_the/) , 2024-04-28-0911
```
I'm not using Lanchain but only making API calls to an LLM service provider. The retriever is connected to a vector DB, 
and I would like to know what the LLM refers to WITHIN that retrieved context whenever it provides an answer, similar to
 how return_source_documents works in Langchain.

I'm using AzureOpenAI. I couldn't find much in their docs that related
 to returning the source documents. Any help will be greatly appreciated!

```
---

     
 
MachineLearning -  [ [P] RAG pipeline to query the ML Engineering Open Book ](https://www.reddit.com/r/MachineLearning/comments/1bu4wyx/p_rag_pipeline_to_query_the_ml_engineering_open/) , 2024-04-28-0911
```
I built a quick RAG implementation using Langchain to make it easy to query the [ML Engineering Open Book](https://githu
b.com/stas00/ml-engineering) by [Stas Bekman](https://twitter.com/StasBekman). The Multi-Vector retriever gave pretty go
od results and was quite easy to set up too. 

Github link - [https://github.com/shreyansh26/RAG-ML-Engg-Open-Book](http
s://github.com/shreyansh26/RAG-ML-Engg-Open-Book)

Hope this is useful for folks!
```
---

     
 
MachineLearning -  [ [Project] FinancialAdvisorGPT : LLM+RAG Boilerplate Project ](https://www.reddit.com/r/MachineLearning/comments/1btlpgd/project_financialadvisorgpt_llmrag_boilerplate/) , 2024-04-28-0911
```
FinancialAdvisorGPT is a boilerplate project designed for RAG (Retriever-Augmented Generation) and LLM (Large Language M
odel) applications in financial analysis. Built on a technology stack including MongoDB, MongoDB VectorDB, Chroma, FastA
PI, Langchain, and React submodule for UI, it offers a framework for developers to implement and customize RAG+LLM proje
cts. Leveraging parallelized data pipelines, FinancialAdvisorGPT processes and integrates various data sources such as s
tock data, news, SEC filings, and local PDFs.

Github project includes long documentation on how the project is structur
ed, how LLM+RAG works for specific task : [https://github.com/mburaksayici/FinancialAdvisorGPT](https://github.com/mbura
ksayici/FinancialAdvisorGPT)
```
---

     
 
MachineLearning -  [ [Project] Picachain, image search made simple. ](https://www.reddit.com/r/MachineLearning/comments/1bt7epv/project_picachain_image_search_made_simple/) , 2024-04-28-0911
```
I am working on creating something for image search, basically something like langchain for images. Probably add videos 
too.

Currently supports chromaDB. Working on pinecone and other vector dbs. [https://github.com/d1pankarmedhi/picachain
](https://github.com/d1pankarmedhi/picachain)

Will you use something like this? What else should I add? Feel free to ad
d your views.

Appreciate your feedback or any feature ideas :)

&#x200B;
```
---

     
 
deeplearning -  [ Seeking Advice: Solving Data Challenges with Large Language Models (LLMs) ](https://www.reddit.com/r/deeplearning/comments/1ca4nc1/seeking_advice_solving_data_challenges_with_large/) , 2024-04-28-0911
```
Hi all

I am presented with a problem that I need to solve using LLM to get the right data from text that has only \~20%
 structure to it. Here's a sample data

XXXXX

AA          BB

CCCC:  (optional DDDD)

C1......(A1) (B1)

C2......(A2) (
B2)

C3.....(A3) (B3)

I am required to anwer with either of these results from A1/B1 till A3/B3 pairs but in order to d
o that I need to go back and ask the user which one of the options C1 to C3 applies to him?

The above is not the most c
omplex structure, it increases in complexity from here so a lot of chatting with user is required to get to the right da
ta that will always exist in the chunk like above.

In the most simplist case the data structure will look like below

X
XXXX

AA          BB

CCCC: ......(A1) (B1)



How would you build a system like this? I am looking at multi-agent syste
ms with Langchain, what about prompt chaining?
```
---

     
 
deeplearning -  [ Share the Coolest Out of The Box LLM Applications That Made You Say 'Wow that was smart' ](https://www.reddit.com/r/deeplearning/comments/1c9e6dj/share_the_coolest_out_of_the_box_llm_applications/) , 2024-04-28-0911
```
Hi, I'm looking at some LLM applications today but apart from guys doing big rags with langchain I don't see too many us
es that are out of the box or that make me say 'wow that was smart to use an LLM here'. Have you seen any cool stuff usi
ng LLMs recently that made you say 'wow, that was smart'?
```
---

     
