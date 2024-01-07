 
all -  [ How can I run my python script when I start my NextJS app ](https://www.reddit.com/r/nextjs/comments/1909h6l/how_can_i_run_my_python_script_when_i_start_my/) , 2024-01-07-0911
```
I am working on the popular chat with PDF projects. The way I have mine setup is to have all the LLM code in a Python sc
ript and use Flask to set it up as an API I can call from the front end. Right now, when I start the app I do the normal
 'npm run dev' and then I also have to do 'python llmpython.py' to start my Python script. What's an efficient way to do
 this such that when my app starts, the Python script also starts? If I make this online, how would it work also?

&#x20
0B;

Here's my llmpython.py file:

&#x200B;

&#x200B;

    ```from langchain.document_loaders import PyPDFLoader
    fro
m langchain.text_splitter import RecursiveCharacterTextSplitter
    
    from langchain.vectorstores import FAISS
    fr
om langchain.embeddings.openai import OpenAIEmbeddings
    
    from langchain.chat_models import ChatOpenAI
    from la
ngchain.chains.question_answering import load_qa_chain
    
    from flask import Flask, jsonify, request
    from flask
_cors import CORS, cross_origin
    
    #Setting Environment variables
    from dotenv import load_dotenv
    import os

    load_dotenv()
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    
    # app instance
    app = Flask(__name__)
  
  CORS(app)
    @/cross_origin()
    @/app.route('/api/home', methods=['POST'])
    def chat_document():
    data = requ
est.get_json()
    pdfUrl = data['url']
    query = data['chat']
    
    #Load PDF
    #The url should be coming from t
he front end through a post request
    loader = PyPDFLoader(pdfUrl)
    if loader:
    data = loader.load_and_split()
 
   else:
    return 'Error loading PDF'
    
    #Text Splitting
    text_splitter = RecursiveCharacterTextSplitter(chun
k_size=1000, chunk_overlap=200)
    texts = text_splitter.split_documents(data)
    
    #Embedding and vector storage
 
   embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
    vectorstore = FAISS.from_documents(texts, embeddings
)
    
    #query
    # query = 'What's the main point of the document?'
    docs = vectorstore.similarity_search(query)

    
    #Load LLM and chatchain
    llm = ChatOpenAI(temperature=0, openai_api_key=OPENAI_API_KEY)
    chain = load_qa
_chain(llm, chain_type='stuff')
    llmresponse = chain.run(input_documents=docs, question=query)
    
    response = js
onify({
    'message': llmresponse,
    'role': 'ai'
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    
    return response
    
    
    @/app.route('/api/guest', methods=['POST'])
    def guest_document():
    data =
 request.get_json()
    pdfUrl = data['url']
    query1 = data['chat1']
    query2 = data['chat2']
    
    #Load PDF
  
  #The url should be coming from the front end through a post request
    loader = PyPDFLoader(pdfUrl)
    if loader:
  
  data = loader.load_and_split()
    else:
    return 'Error loading PDF'
    
    #Text Splitting
    text_splitter = R
ecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    texts = text_splitter.split_documents(data)
    
 
   #Embedding and vector storage
    embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
    vectorstore = FAIS
S.from_documents(texts, embeddings)
    
    #query
    # query = 'What's the main point of the document?'
    docs1 = v
ectorstore.similarity_search(query1)
    docs2 = vectorstore.similarity_search(query2)
    
    #Load LLM and chatchain

    llm = ChatOpenAI(temperature=0, openai_api_key=OPENAI_API_KEY)
    chain = load_qa_chain(llm, chain_type='stuff')
  
  llmresponse1 = chain.run(input_documents=docs1, question=query1)
    llmresponse2 = chain.run(input_documents=docs2, q
uestion=query2)
    response = jsonify({
    'message1': llmresponse1,
    'message2': llmresponse2,
    'role': 'ai'
  
  })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
    
    if __name__ == '__main__'
:
    app.run(debug=True, port=8080)

\`\`\`

&#x200B;

and this is one of the components where I am calling the flask a
pp from:

&#x200B;

    ```'use client';
    import { fileName, guestpdfUrl } from '@/components/Hero';
    import { But
ton } from '@/components/ui/button';
    import { useState} from 'react';
    import TabsSec from './TabsSec';
    
    
const Guest = () => {
      const [summary, setSummary] = useState<string>(''); // <-- specify type here
      const [bu
lletSummary, setBulletSummary] = useState<string>(''); // <-- specify type here
      const [isLoading, setIsLoading] = 
useState<boolean>(false); // <-- specify type here
    
      const processDocument = (event: React.FormEvent) => {
    
    event.preventDefault();
        setIsLoading(true);
    
        fetch('http://localhost:8080/api/guest', {
        
  method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON
.stringify({
            url: guestpdfUrl,
            chat1: 'Create a summary of this text',
            chat2: 'Creat
e a 10 bullet point summary of this text',
          }),
        })
          .then((response) => response.json())
     
     .then((data) => {
            console.log(data.message2);
            setSummary(data.message1);
            setBul
letSummary(data.message2);
            setIsLoading(false);
          });
      };
    
    
      return (
        <div
 className='flex items-center justify-center flex-col'>
          <div className=' text-[#202942] mb-4 text-4xl md:text-
5xl tracking-tight font-extrabold'>
            Welcome Guest
          </div>
          <div className=' text-[#202942]
  my-4 text-center text-xl md:text-2xl tracking-tight font-extrabold'>
            You&apos;ve uploaded a PDF called {fi
leName}
          </div>
          <div className='mb-8'>
            <Button
              className='rounded-full bg-[
#202942] text-[#dfeff4] 
               hover:bg-[#3a435e]
             font-bold text-sm md:text-base py-2 px-3'
      
        onClick={processDocument}
            >
              Process Document
            </Button>
          </div>
  
        <div></div>
          <TabsSec
            summary={summary}
            bulletSummary={bulletSummary}
         
   isLoading={isLoading}
          />{' '}
        </div>
      );
    };
    
    export default Guest;

\`\`\`

&#x200
B;

How would you advise that I achieve this? I was thinking of using an exec childprocess to run 'python llmpython.py' 
in a useEffect but it looks like that is not possible. I would appreciate any advice

&#x200B;

&#x200B;
```
---

     
 
all -  [ Need help regarding vector DBs ](https://www.reddit.com/r/LangChain/comments/1908cyz/need_help_regarding_vector_dbs/) , 2024-01-07-0911
```
Okay so my question is - if I am making a pdf(or url) summariser app , do I need to use vector DBs to store embeddings? 


I have been watching a lot of tutorials of chat to pdf apps and they use vector db to store the chunks - but do I need
 it since I dont wanna make a conversational app? I just want to take pdf or an url extract the text and summarise it on
e time only .


I know embeddings are necessary so that we don't have to send whole large text to llm model - is what I 
wanna do possible without databases?

Thanks
```
---

     
 
all -  [ Automating prompt writing & LLM evaluation ](https://www.reddit.com/r/LangChain/comments/19051ef/automating_prompt_writing_llm_evaluation/) , 2024-01-07-0911
```
Hey Reddit community! 🚀

Whilst building various things with LLMs I’ve found one of the most time-consuming, annoying th
ings to be writing & optimising prompts, then testing them across different models. That's why I want to share something
 I've been working on: [Composo.ai](http://composo.ai/).

&#x200B;

* **Automated Prompt Writing**: Wish GPT4 would just
 write its prompts for itself? Now you can 🙂. Great for those moments when you're stuck, just starting out or are trying
 to do the final bit of refining to a well-tuned prompt.
* **Compare Gemini vs GPT4 & more**: Want to test how Gemini st
acks up against Claude or GPT-4 for a certain prompt? Our platform lets you compare them side by side.
* **No sign-up to
 try it out**: Jump straight into action at [www.composo.ai](http://www.composo.ai/) \- no sign-up, no barriers.
* **Rob
ust testing & evaluation platform too:** We’re also building a robust testing & evaluation platform for production appli
cations, so you can automate all that subjective ‘testing by vibes’ of your application outputs.

The automated prompt w
riting is the easiest to get started with, and you can also test those prompts across models without having to sign up t
oo.

Super keen to hear what you think!
```
---

     
 
all -  [ Is it possible to fine tuning a model to improve RAG queries ? ](https://www.reddit.com/r/LocalLLaMA/comments/1901ttm/is_it_possible_to_fine_tuning_a_model_to_improve/) , 2024-01-07-0911
```
Hi !  
I am trying to use some local models + langchain on lawsuits in pt-br to make some queries.

Unfortunately the re
sults are no so precise for some basic question :(

So, I would like to know if is possible to fine tuning a model to im
prove RAG queries.  


If so, can you share some examples?  


Thanks in advance !
```
---

     
 
all -  [ I've just launched a new opensource Practical AI Development for React Developers course! ](https://www.reddit.com/r/reactjs/comments/19004eq/ive_just_launched_a_new_opensource_practical_ai/) , 2024-01-07-0911
```
Hey everyone!

Excited to share this with you.

![image](https://github.com/thestriver/ai-for-javascript-course/assets/1
6709708/95237a88-63e2-48b6-a2c6-fc45ff49fe7b)

I just released an open-source course for Javascript developers who want 
to build AI applications on GitHub. All 60 pages of them (if you want the PDF format of the primer). (The markdown file 
is at over 1600 lines right now and growing.) 🙂

Structured to take Javascript developers from 0-1, I put in everything 
I know from building AI-powered apps over the past year, and I hope you find it useful too.

[Github Link](https://githu
b.com/thestriver/ai-for-javascript-course)

Here are some of the topics touched on in the modules:

- **Introduction to 
LLMs 🧩**
- **Advanced Prompt Engineering and Optimization ✏️**
- **Integrating** **OpenAI GPT 3.5 and Mistral 7B Instruc
t v0.2 into JS apps**
- **Retrieval Augmented Generation 💬**
- **Using Vercel AI SDK, Pinecone, and Langchain to build a
 Research Assistant Tool**
- **Function Calling**
- **Building** 3 ****AI Agents with different levels of complexity 🤖**
**
- **Security, Ethics, and Performance in AI Development**

A relevant project accompanies each course.

I created thi
s course hoping it would be an excellent guide for aspiring AI developers and a valuable resource for the wider JavaScri
pt developer community.

I would love to get your feedback and, of course, would appreciate it if you shared any bugs or
 mistakes you discover or questions with me.
```
---

     
 
all -  [ End of Week Report DevolvedAI ](https://www.reddit.com/r/DevolvedAI/comments/18zykt5/end_of_week_report_devolvedai/) , 2024-01-07-0911
```
Highlights:
1. Data Management & Security:
   - Successful scraping and structuring of 'Devolved AI' GitBook content.
  
 - Advanced MongoDB and Google Cloud setups for Luna Chat app, enhancing security and scalability.
   - Initiation of a 
multi-database approach for optimized performance and security.

2. AI and Machine Learning Developments:
   - Significa
nt advancements in Luna Chat's language model.
   - Intensive research and application of GPT-3.5 Turbo and Rasa framewo
rk.
   - Development of new datasets and memorychain frameworks for Luna, enhancing accuracy and conversational capabili
ties.
   - Implementation of Langchain for AI text generation.
   - Ongoing efforts in fine-tuning Luna’s model for bett
er performance.

3. Blockchain Integration:
   - Progress in integrating blockchain for transactions.
   - Research on L
ayer 1 blockchain technologies.

4. Web Development Achievements:
   - Development of responsive web pages and Chat mode
 API.
   - Real-time updates on various web app features.

5. Collaborative Team Effort:
   - Continuous collaboration a
nd expertise sharing among team members, fostering innovation and efficiency.

Looking Ahead:
- Focused on enhancing Lun
a's first-person response mechanism.
- Exploring new search algorithms.
- Improving the conversational AI capabilities.

- Finalizing web app integrations and functionalities.

#DevolvedAI #AGC #Argocoin #AI #crypto
```
---

     
 
all -  [ 🔥 [HIRE] ChatGPT, Langchain, Generative AI, , Prompt Engineering ](https://www.reddit.com/r/ForHire_AI/comments/18zxgcq/hire_chatgpt_langchain_generative_ai_prompt/) , 2024-01-07-0911
```
[**View Profile**](https://remoteai.io/talent/profile/@jiukchoi) **=>** [**https://remoteai.io/talent/profile/@jiukchoi*
*](https://remoteai.io/talent/profile/@jiukchoi)

As a distinguished AI engineer with a focus on prompt engineering, I h
ave developed a deep understanding of artificial intelligence and its practical applications 🌐. My journey in this field
 began with a strong foundation in computer science, where I honed my programming and analytical skills 🔍. This backgrou
nd paved the way for my specialization in AI.   
My expertise lies in prompt engineering, a critical aspect of AI that i
nvolves designing and refining prompts to elicit accurate and relevant responses from AI models 🤖. My work has contribut
ed to advancements in AI interactions, making them more intuitive and user-friendly 👥.   
My expertise lies in prompt en
gineering, a critical aspect of AI that involves designing and refining prompts to elicit accurate and relevant response
s from AI models. My work has contributed to advancements in AI interactions, making them more intuitive and user-friend
ly.  
Driven by a passion for innovation and a commitment to excellence, I continuously explore new frontiers in AI, aim
ing to bridge the gap between human and machine intelligence for a more connected and intelligent future 🌟.

&#x200B;

&
#x200B;
```
---

     
 
all -  [ Chat model for 'any codebase' ](https://www.reddit.com/r/u_waynerad/comments/18zptpm/chat_model_for_any_codebase/) , 2024-01-07-0911
```
[DoWhile.AI](https://DoWhile.AI): claims to be 'non-hallucinating, highly-contextual & up-to-date answers on any codebas
e'.

What sort of codebase? Well, under 'trending repos', they list: React JS, Langchain Python, Auto GPT, Svelte, Node 
JS, Spring Boot, Flutter, Llama Index, Angular, PyTorch, Rust, and Next JS.

To give the system a whirl, I punched in th
e question, 'What is the best way to keep state on the server, on the browser in JavaScript, and in the Document Object 
Model visible to the user in sync?'

\----

In the given context of JavaScript and React, managing and keeping the state
 in sync across server, browser and Document Object Model (DOM) may involve different approaches. However, here are a fe
w common methods used:

1. React State and UseState Hook: A common way to manage local state in a React component is by 
using the 'useState' hook. This allows the state of your application to be managed within React's component architecture
, ensuring that the DOM stays in sync with your state.

Here's an example where 'useState' hook is used to manage naviga
tion state and sync state in a test suite for React DOM.

const \[syncState, setSyncState\] = React.useState(false);

co
nst \[hasNavigated, \_setHasNavigated\] = React.useState(false);

setHasNavigated = \_setHasNavigated;

function onPopst
ate() {

setSyncState(true);

}

React.useEffect(() => {

window.addEventListener('popstate', onPopstate);

return () =>
 {

window.removeEventListener('popstate', onPopstate);

Reference: 'ReactDOMFiberAsync-test.js'

\[ Link goes to: [http
s://github.com/facebook/react/blob/main/packages/react-dom/src/\_\_tests\_\_/ReactDOMFiberAsync-test.js](https://github.
com/facebook/react/blob/main/packages/react-dom/src/__tests__/ReactDOMFiberAsync-test.js) \]

&#x200B;

2. Server State 
Management: To keep the server state in sync, you can create JavaScript modules that exports functions to set and get th
e state. This becomes particularly handy if you're creating a server-rendered application using Node.js or if you have t
he need to manage state on the server-side.

For instance, in this example a module is created to get and set the 'serve
rState':

let serverState = 'Hello World';

export function setServerState(message) {

serverState = message;

}

export
 function getServerState() {

return serverState;

}

Reference: 'ServerState.js'

\[ Link goes to: [https://github.com/
facebook/react/blob/main/fixtures/flight-esm/src/ServerState.js](https://github.com/facebook/react/blob/main/fixtures/fl
ight-esm/src/ServerState.js) \]

&#x200B;

3. User Form State: In instances where the user is interacting with forms on 
the frontend, newly added hooks like 'useFormStatus' and 'useFormState' can be used to manage those states and keep them
 in sync. Reference can be found in '[CHANGELOG-canary.md](https://CHANGELOG-canary.md)'.

&#x200B;

4. Async Operations
: For situations where the state depends on asynchronous operations (like server responses), React provides features lik
e 'startTransition' to manage state during those operations. Further details can also be found in the '[CHANGELOG-canary
.md](https://CHANGELOG-canary.md)'.

&#x200B;

Note: These methods involve the system in how React operates -- reconcili
ng state changes with the view (DOM updates), and may depend largely on your application architecture. You may need a mo
re advanced state management library (like Redux, Mobx, or Zustand) for larger applications or specific use-cases.

In s
ummary, a robust way of keeping server and local state in sync in a React application involves a combination of properly
 managing local component state with 'useState()' and 'useEffect()', and maintaining server state consistency with serve
r-side state management strategies and efficient handling of asynchronous operations. Be sure to account for user intera
ctions that change application state and ensure that state changes trigger the necessary updates to the DOM. Additionall
y, for large applications consider using a state management library.

Answer derived from the following files:

fixtures
/flight-esm/src/ServerState.js

fixtures/flight/src/ServerState.js

packages/react-dom/src/\_\_tests\_\_/ReactDOMFiberAs
ync-test.js

packages/react-reconciler/src/ReactFiberBeginWork.js

CHANGELOG-canary.md

[https://chat.dowhile.ai/](https
://chat.dowhile.ai/)
```
---

     
 
all -  [ Book rewrite with large context window ](https://www.reddit.com/r/LangChain/comments/18zpl3w/book_rewrite_with_large_context_window/) , 2024-01-07-0911
```
Hey folks,

So I am new to LLMs but as a learning I want to rewrite the ending of Game of Thrones using a LLM.

&#x200B;


So far here's what I got:

\- Made my own dataset with the scripts for each episode on all seasons. (I was going to us
e the books... but they are just too much text for the LLM)

\- Simple inference using LLamaCpp, Mistral and Langchain


&#x200B;

But I can't feed all the episodes into one prompt, as it exceeds the token window size. I played with document
 splitting and Chroma as a Vector database, but it does not solve the problem.

So how can I proceed to rewrite it?

&#x
200B;

My code so far:

    # %%
    !pip install langchain langchain-community chromadb
    
    # %%
    !CMAKE_ARGS='
-DLLAMA_METAL=on' FORCE_CMAKE=1 pip install --upgrade --force-reinstall llama-cpp-python
    
    # %%
    from langchai
n.callbacks.manager import CallbackManager
    from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackH
andler
    from langchain.chains import LLMChain
    from langchain.prompts import PromptTemplate
    from langchain.pro
mpts.few_shot import FewShotPromptTemplate
    from langchain_community.llms import LlamaCpp
    
    # %%
    import os

    
    examples = []
    
    # Read .txt files under './dataset/'
    DATASET_PATH = './scripts/'
    files = os.lis
tdir(DATASET_PATH)
    for file in files:
        if file.endswith('.txt'):
            with open(os.path.join(DATASET_P
ATH, file), 'r') as f:
                content = f.read()
                title = content[:content.find('\n')]
         
       # Start content on the third line
                content = content[content.find('\n', content.find('\n') + 1) + 
1 :]
                season = file[: file.find('x')]
                episode = file[file.find('x') + 1 : file.find('.')]

                examples.append({
                    'title': title,
                    'content': content,
         
           'season': season,
                    'episode': episode
                })
                # examples.append
(['title: ' + title, 'book content: ' + content, 'season: ' + season, 'episode: ' + episode])
    
    print(examples[0]
)
    
    # %%
    from langchain.schema import Document
    # prompt = 'Given the following scripts, rewrite the final
 two seasons so that the plots are more consistent with the seasons before.'
    
    # source = ''
    # currentSeason 
= 0
    # for example in examples:
    #     if example['season'] != currentSeason:
    #         if currentSeason != 0:

    #             source += '<END OF SEASON>\n'
    #         source += '\nSEASON ' + str(example['season']) + '\n'
   
 #         currentSeason = example['season']
    
    #     source += example['content'] + '<END OF EPISODE>\n'
    
   
 documents = []
    for example in examples:
        documents.append(
            Document(
                page_conten
t=example['content'],
                metadata={
                    'title': example['title'],
                    'sea
son': example['season'],
                    'episode': example['episode']
                }
            )
        )
   
 
    # %%
    # from llama_cpp import Llama
    # model = './mistral-7b-v0.1.Q6_K.gguf'
    # llm = Llama(
    #     mo
del_path=model,
    #     n_ctx=8196,
    #     n_batch=512,
    #     n_threads=7,
    #     n_gpu_layers=2,
    #     
verbose=True,
    #     seed=42
    # )
    
    # message = f'<s>[INST] {prompt} [/INST]</s>{source}'
    # # output = 
llm(message, echo=True, stream=True, max_tokens=4096)
    
    # stream = llm.create_completion(
    #     message,
    
#     stream=True,
    #     echo=True,
    #     repeat_penalty=1.1, 
    #     max_tokens=4096, 
    #     stop=['<END
 OF SEASON>'],
    #)
    # for output in stream:
        # print(output['choices'][0]['text'].replace(message, ''))
   
 
    # print(output['usage'])
    # output = output['choices'][0]['text'].replace(message, '')
    # print(output)
    

    # %%
    callbackManager = CallbackManager([StreamingStdOutCallbackHandler()])
    
    llm = LlamaCpp(
        mod
el_path='./mistral-7b-v0.1.Q6_K.gguf',
        n_ctx=8196,
        n_batch=512,
        n_threads=7,
        n_gpu_layer
s=1,
        f16_kv=True,
        verbose=False,
        seed=42,
        callback_manager=callbackManager
    )
    
  
  pmt = PromptTemplate(
        template='Question: {input}\nAnswer: Hello!<',
        input_variables=['input']
    )
 
   llm_chain = LLMChain(llm=llm, prompt=pmt)
    
    # %%
    from langchain.text_splitter import RecursiveCharacterTex
tSplitter, CharacterTextSplitter
    
    chunkSize = 4096
    chunkOverlap = 4
    
    splitter = RecursiveCharacterTe
xtSplitter(
        chunk_size=chunkSize,
        chunk_overlap=chunkOverlap
    )
    
    docs = splitter.split_docume
nts(documents)
    print(f'from {len(documents)} to {len(docs)}')
    
    # %%
    from langchain.vectorstores import C
hroma
    from langchain_community.embeddings import LlamaCppEmbeddings
    
    storagePath = './storage/chroma'
    if
 not os.path.exists(storagePath):
        os.makedirs(storagePath)
    
    embeddings = LlamaCppEmbeddings(
        mod
el_path='./mistral-7b-v0.1.Q6_K.gguf',
        n_ctx=8196,
        n_batch=512,
        n_threads=7,
        n_gpu_layer
s=1,
        f16_kv=True,
        verbose=False,
        seed=42
    )
    
    # %%
    db = Chroma.from_documents(
   
     documents=docs,
        embedding=embeddings,
        persist_directory=storagePath,
    )
    
    # %%
    %%capt
ure captured --no-stdout
    llm_chain.run('Hey, what's up?')
    
    
    

&#x200B;
```
---

     
 
all -  [ [P] An open-source project for deploying local models ](https://www.reddit.com/r/MachineLearning/comments/18zkm5m/p_an_opensource_project_for_deploying_local_models/) , 2024-01-07-0911
```
 Introducing a new LLM WebUI project that supports various local model loading and provides streaming output for cutting
-edge online multimodal models GPT-4-Vision and Gemini-Pro-Vision. Completely free and open source, it serves as a valua
ble research tool for exploring diverse models. The project is actively under development with continuous updates:  
[ht
tps://github.com/smalltong02/keras-llm-robot](https://github.com/smalltong02/keras-llm-robot)

&#x200B;

[WebUI](https:/
/preview.redd.it/f95jievpepac1.png?width=2560&format=png&auto=webp&s=1f2908b484ededc78591719ef87efdac2f9497ba)

&#x200B;


[Configuration](https://preview.redd.it/owaj5s1repac1.png?width=2560&format=png&auto=webp&s=f837b1ef67cb8e4ccaee4ec602
a61859f53db100)

&#x200B;

[Tools & Agent](https://preview.redd.it/jrot8w9sepac1.png?width=2560&format=png&auto=webp&s=7
1e224f08620941146cd437a99bcb55d02930a9e)
```
---

     
 
all -  [ Automate marketing content generation effortlessly ](https://v.redd.it/5h7apd4t6mac1) , 2024-01-07-0911
```

```
---

     
 
all -  [ End-to-end observability for LangChain script ](https://www.reddit.com/r/LangChain/comments/18z5pch/endtoend_observability_for_langchain_script/) , 2024-01-07-0911
```
Prompt:  'What are the number of parameters in GPT5 and GPT4? What is the logarithm (base e) of the difference between t
he number of parameters?'

AimOS providing essential information about the trace:

[AimOS](https://preview.redd.it/u4wal
goh5mac1.jpg?width=2880&format=pjpg&auto=webp&s=ecdef81eb609552d333134a962397b4b483761dd)

Exploring the process: Steps 
tab provides a detailed walkthrough of the sequence of actions undertaken throughout the pipeline to achieve the specifi
ed goal. 

[AimOS](https://preview.redd.it/ju843lmi4mac1.jpg?width=2880&format=pjpg&auto=webp&s=6c7c44b724f584d1f70bdf00
27a2a17cbbdc9418)

The final answer to our question: The logarithm (base e) of the difference between the number of para
meters in GPT5 and GPT4 is 4.605170185988092.

Cost tab including three graphs showing token-usage, token-usage-input, a
nd token-usage-output, providing a detailed breakdown of the computational costs associated LangChain activities.

[AimO
S](https://preview.redd.it/w3xgkjcv5mac1.jpg?width=2880&format=pjpg&auto=webp&s=7e9460d625fd1a2c30291ba599ccd0ed2b33d1ad
)

AimOS has a Debugger for LangChain that logs LLMs prompts and generations, tools inputs/outputs, and chains metadata.
 

[https://github.com/aimhubio/aimos](https://github.com/aimhubio/aimos)
```
---

     
 
all -  [ RAG Vs. Batch Processing in Large Document Summarization ](https://www.reddit.com/r/LangChain/comments/18z51mu/rag_vs_batch_processing_in_large_document/) , 2024-01-07-0911
```
Let's say I have a CSV file with 100,000 comments related to a product. I would like to summarize all the comments and p
rovide some recommendations on how to improve the product.   


What is the best way to summarize this? Using RAG or chu
nking and feeding the entire list of comments to the LLM to process?
```
---

     
 
all -  [ Not even a single interview call for internships in Data ](https://i.redd.it/61ayw0oqwkac1.png) , 2024-01-07-0911
```
Do I need to add more projects and remove my achievements to get more key word matched . I have applied to around 300 jo
bs in past 4 month and haven't got a single call for internship in data related.
```
---

     
 
all -  [ ChromaDB or any vector database for mobile devices ](https://www.reddit.com/r/LangChain/comments/18yxpdg/chromadb_or_any_vector_database_for_mobile_devices/) , 2024-01-07-0911
```
While it is easy to create streamlit/hosted apps using vector databases; i am looking to create a solution which ensures
 that user data \[including vector database information\] never leaves user device, leading to utmost privacy \[unless s
earch results for a RAG solution are sent to an LLM\]

&#x200B;

Anyone has had luck running chromaDB on mobile ? or any
 other vector databases that would work accordingly ? 
```
---

     
 
all -  [ Extracting data from pdf containing complex tables ](https://www.reddit.com/r/LangChain/comments/18yxacm/extracting_data_from_pdf_containing_complex_tables/) , 2024-01-07-0911
```
Is there any library or any way which helps in extracting pdf containing complex tables data and store , and how can we 
chunk that pdf data such that table data preserves in vector db ? Assuming each pdf contains around 5-10 pages
```
---

     
 
all -  [ How do you test and manage use cases based on the langchain framework? ](https://www.reddit.com/r/LangChain/comments/18yws8j/how_do_you_test_and_manage_use_cases_based_on_the/) , 2024-01-07-0911
```
I have been developing based on langchain for a period of time recently, and later I came into contact with the service 
langsmith provided by it. The overall feeling is that the trace capability is quite powerful, but the test set managemen
t is not convenient to use. What did you use during the testing process? Test methods or dataset management tools.
```
---

     
 
all -  [ Full Stack Developer and Generative AI Engineer: Is this a realistic career path? ](https://www.reddit.com/r/cscareerquestions/comments/18ys69n/full_stack_developer_and_generative_ai_engineer/) , 2024-01-07-0911
```
I recently graduated with a degree in computer engineering, and I've been teaching myself full-stack development skills,
 with a focus on backend development. I find this field to be a good fit for me and I'm focusing mostly on .NET. My main
 motivation for choosing this path is the abundance of job opportunities.  
  
Apart from full-stack development, I re
ally enjoy anything AI-related. I can even say I enjoy working with AI more than building API's etc.. I have a strong fo
undation in Python and have independently studied machine learning and deep learning, completing projects such as my gra
duation thesis on medical image classification using deep learning. However, I've been hesitant to pursue a career in AI
 due to concerns about my math background and limited job opportunities in my location.  
  
Recently, my interest in 
generative AI has sparked a realization. I've delved into tools like Langchain, LlamaIndex, and LLMs, working on project
s focused on Retrieval Augmented Generation.  I also tinkered with Stable Diffusion and GANs in general previously. What
 happened is that I realized that working with generative AI is something I really enjoy and something that gives me muc
h more excitement and creative fulfillment than full-stack development.  This is where the uncertainty I'm currently fac
ing originates from.  
  
I want to be able to work with generative AI but not just be a 'prompt engineer'. I want to 
be able to understand what's going on behind the scenes and for that, I recognize the need to enhance my skills in machi
ne learning, NLP, and related areas. What I don't want is completely going down the path of data science. I want to work
 with generative AI, not just as a 'prompt engineer,' but as an AI engineer with a focus on generative AI solutions. I a
im to understand the intricacies behind the scenes and supervise the creation of 'AI-infused' software solutions from an
 architectural standpoint in the future. The problem with that is that my preparation has been geared towards full-stack
 web development, and I'm unsure if I can secure a job in AI at this point.  
  
I see four potential paths for myself
:  
  
1-) Fully commit to the full-stack development path and treat AI as a separate hobby.  
2-) Pursue full-stack 
development while building AI projects and spending an important piece of my free time preparing for a potential career 
shift.  
3-) Take the risk and actively search for a job in AI.  
4-) Somehow combine full-stack development and AI.  

  
Option 4 aligns with my ideal scenario, but I don't know how realistic it is. I don't even know how I'd label mysel
f. I feel lost and would appreciate any suggestions.  
  
Note: I am currently unemployed, focusing on enhancing my po
rtfolio for potential full-stack positions.
```
---

     
 
all -  [ LLM for RAG - embedding and chat not compatible? ](https://www.reddit.com/r/LocalLLaMA/comments/18yq1y6/llm_for_rag_embedding_and_chat_not_compatible/) , 2024-01-07-0911
```
Ok so I'm in early stages of developing a RAG system for communication (emails mostly), and so far, the plan is as follo
ws: use langchain to load email files and get metadata, use mistral:instruct on ollama to embed content, save all emails
 as chunks in elasticsearch database along with metadata, use langchain with mistral:instruct on ollama to query the ela
sticsearch db. The goal is to be able to ask questions like 'in the period April 4th 2018 until May 6th of 2018, has an 
employee from company A expressed any concerns about breaching copyright laws to an employee at company B?'. That's why 
we're using the elasticsearch db, so we can keep metadata like time and company in separate fields and avoid model hallu
cinations related to date and company affiliation. I've now come to understand that using mistral is not a good idea for
 embedding, and that I should use an encoder (Bert) or encoder-decoder (t5) model to do so. This would also help with sp
eed (I might have 2.5M emails to work with, and everything should preferably be embedded within only a day or two). My p
roblem is now though, that if I use a model that's good for embedding, then that model won't be as good for general lang
uage understanding and conversation, which I want. The whole point of doing a RAG system is to be able to chat with the 
database and ask questions, and to my understanding, Bert for instance would not be fit for that task. T5 might, but I'm
 not sure about that either, and it sure wouldn't be as good as mistral, for instance. So what to do? If I embed using B
ert, then I can't chat with my db, but if I use mistral to embed then I'm abusing the model, it'll take forever, and it'
ll create suboptimal embeddings (correct?). If it's in any way relevant, I can say that my data is mostly in Danish, but
 I have considered using machine translation to English as part of my preprocessing. I'm also not sure that that is a go
od idea, however. Thanks a lot in advance :)
```
---

     
 
all -  [ Would i use LangChain for this? ](https://www.reddit.com/r/LangChain/comments/18ypaes/would_i_use_langchain_for_this/) , 2024-01-07-0911
```
I want an LLM like GPT to be the brain of my automated workflow. I would define an SOP (standard operating procedure) fo
r how to handle a transaction from start to finish. The transaction will be added to a Postgres DB and trigger an event 
via Amazon SNS, at which point id like my LangChain app to start processing the transaction (which has a JSON structure)
. There will be points in the processing of this transaction where API requests will need to be made based on certain co
nditions in the data. Ill need a way to store the current state of the transaction to know what should happen next (or p
ossibly have the transaction in the db be the source of truth). There will be a step where ill need to send reminder ema
ils to users once a day until they complete an action. 

Can LangChain handle most of the thinking in my automated workf
low? Eg “based on the current state of the transaction you should probably do X next.”

Any tutorials or reading you cou
ld recommend would be helpful. Thanks!
```
---

     
 
all -  [ Please help with langchain, want both document retrieval and conversation memory ](https://www.reddit.com/r/LangChain/comments/18yovcm/please_help_with_langchain_want_both_document/) , 2024-01-07-0911
```
Hi everyone I am trying to use langchain to reference and answer questions about documents and keep memory during the co
nversation about my document questions. I keep running into issues where it only references the documents in my Pinecone
 data base but has no conversation memory. Any help would be greatly appreciated. Code below:

    import streamlit as s
t
    
    from io import StringIO
    
    
    
    import pinecone
    pinecone.init(api_key='', environment='gcp-sta
rter')
    
    from langchain import PromptTemplate
    from langchain.chat_models import ChatOpenAI
    from langchain
.chains import LLMChain
    from langchain.chains import RetrievalQA
    from langchain.embeddings import OpenAIEmbeddin
gs
    
    from langchain.vectorstores import Pinecone
    from langchain.text_splitter import RecursiveCharacterTextSp
litter
    
    from langchain.memory import ConversationBufferMemory
    
    
    
    OPENAI_API_KEY = ''
    OPENAI_
DIMENSION = 1536
    
    embedding = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
    
    st.reupload_file = False

    
    vector_store = Pinecone.from_existing_index('legal-cases', embedding)
    index = pinecone.Index('legal-cases')

    
    
    if not hasattr(st.session_state, 'convo_memory'):
        st.session_state.convo_memory = ConversationBuf
ferMemory(return_messages=True)
    
    
    
    
    def upload_new_file_to_pinecone(text):
        embedding = OpenA
IEmbeddings(openai_api_key=OPENAI_API_KEY)
    
        text_splitter = RecursiveCharacterTextSplitter(
        chunk_si
ze=100, chunk_overlap=0, length_function=len
    )
    
        chunks = text_splitter.create_documents([text])
    
   
     result = Pinecone.from_documents(chunks, embedding, index_name='legal-cases')
    
    
    st.title('📝 File Q&A')

    
    uploaded_file = st.file_uploader('Upload an article', type=('txt', 'md'))
    
    if st.reupload_file:
       
 print('updated file')
        # To read file as bytes:
        bytes_data = uploaded_file.getvalue()
    
        # To 
convert to a string based IO:
        stringio = StringIO(uploaded_file.getvalue().decode('utf-8'))
    
        # To re
ad file as string:
        string_data = stringio.read()
    
        index.delete(delete_all=True)
        
        
  
      upload_new_file_to_pinecone(string_data)
    
        
    
    
    
    
    def ask_and_get_answer(vector_store
, q, k=3):
        from langchain.chains import RetrievalQA
        from langchain.chat_models import ChatOpenAI
    
  
  
    
        llm = ChatOpenAI(model='gpt-3.5-turbo', temperature=1, api_key=OPENAI_API_KEY)
        retriever = vecto
r_store.as_retriever(search_type='similarity', search_kwargs={'k': k})
        chain = RetrievalQA.from_chain_type(llm=l
lm, chain_type='stuff', retriever=retriever, memory=st.session_state.convo_memory, )
    
        answer = chain.run(q)

        return answer
    
    st.session_state.vs = vector_store
    
    
    k = 3
    # user's question text input w
idget
    q = st.text_input('Ask a question about the content of your file:')
    
    
    
    
    if q: # if the use
r entered a question and hit enter
        standard_answer = ''
        q = f'{q} {standard_answer}'
        if 'vs' in 
st.session_state: # if there's the vector store (user uploaded, split and embedded a file)
            vector_store = st
.session_state.vs
            st.write(f'k: {k}')
            answer = ask_and_get_answer(vector_store, q, k)
    
    

            # text area widget for the LLM answer
            st.text_area('LLM Answer: ', value=answer)
            st.
divider()
            # if there's no chat history in the session state, create it
            if 'history' not in st.se
ssion_state:
                st.session_state.history = ''
            # the current question and answer
            val
ue = f'Q: {q} \nA: {answer}'
            st.session_state.history = f'{value} \n {'-' * 100} \n {st.session_state.histor
y}'
            h = st.session_state.history
            # text area widget for the chat history
            st.text_are
a(label='Chat History', value=h, key='history', height=400)
    
    
            print(st.session_state.convo_memory)
 
   


&#x200B;
```
---

     
 
all -  [ Tried to make a tweet generator using openai and chatgpt. Please check it and add suggestions. I wan ](https://www.reddit.com/r/LangChain/comments/18yj9j5/tried_to_make_a_tweet_generator_using_openai_and/) , 2024-01-07-0911
```
[https://github.com/ManasiTilak/TweetGen](https://github.com/ManasiTilak/TweetGen)
```
---

     
 
all -  [ How do you keep LLM conversation memory? ](https://www.reddit.com/r/LocalLLaMA/comments/18yfsgw/how_do_you_keep_llm_conversation_memory/) , 2024-01-07-0911
```
Hi everyone!

I'm developing a chatbot capable of track the entire history with a user.

I'm currently using Goliath 120
B, with Redis and langchain to return inside the prompt the latest 30 messages with the format USER: ASSISTANT:. 

Obvio
usly, after 30 messages it completely forgets what the user said before, do you use any alternative to this that can kee
ps track of the entire history? 

I read about **ConversationSummaryBufferMemory and ConversationSummaryMemory,** what d
o you thin about them? Are they a valida alternative?

Otherwise let me know if you have something else in mind!

Thank 
you
```
---

     
 
all -  [ Langchain streaming is broken with Local Hugging Face models ](https://www.reddit.com/r/LangChain/comments/18yfh3p/langchain_streaming_is_broken_with_local_hugging/) , 2024-01-07-0911
```
I get responses from my model, but only if I don't use the streaming=True parameter. I can also stream the model directl
y from my local server when I use curl, but not when I use langchain.

Context to the issue here with code example:

[ht
tps://github.com/langchain-ai/langchain/issues/15516](https://github.com/langchain-ai/langchain/issues/15516)
```
---

     
 
all -  [ RAG Embedding Model relevant to Chunk Size? ](https://www.reddit.com/r/LangChain/comments/18yd77i/rag_embedding_model_relevant_to_chunk_size/) , 2024-01-07-0911
```
Hi,

I have built a RAG App with Langchain and used the [intfloat/multilingual-e5-large](https://huggingface.co/intfloat
/multilingual-e5-large) embeddings so far. At the moment I tried oout different chunk sizes (100-2000) and I am wonderin
g if the embedding model is relevant for the chunk size? I was wondering because I saw that the embedding size is 1024.


Thanks for suggestions!
```
---

     
 
all -  [ Install 'llama-cpp-python' in requirements.txt file ](https://www.reddit.com/r/LangChain/comments/18ybano/install_llamacpppython_in_requirementstxt_file/) , 2024-01-07-0911
```
Hi,

I have put my application into a Docker and therefore I have created a requirements.txt file. Now I need to install
 'llama-cpp-python' for Mac, as I am loading my LLM with `from langchain.llms import LlamaCpp`. 

My installation comman
d specifically for Mac is: '`CMAKE_ARGS='-DLLAMA_METAL=on' FORCE_CMAKE=1 pip install llama-cpp-python`', but it does not
 work if I put this in my 'requirements.txt' file.

&#x200B;

How can I do this?
```
---

     
 
all -  [ How to use gpt3.5-turbo-instruct with Langchain? ](https://www.reddit.com/r/LangChain/comments/18y4pyj/how_to_use_gpt35turboinstruct_with_langchain/) , 2024-01-07-0911
```
How to use gpt3.5-turbo-instruct with Langchain? I get:   


'Error code: 404 - {'error': {'message': 'This is not a cha
t model and thus not supported in the v1/chat/completions endpoint. Did you mean to use v1/completions?', 'type': 'inval
id\_request\_error', 'param': 'model', 'code': None}}  


Is there any way to get langchain to hit the /completions endp
oint instead?

Or is langchain not meant for use with instruct models? I might have to abandon langchain for this projec
t?
```
---

     
 
all -  [ Semantic chunking ](https://www.reddit.com/r/LangChain/comments/18y44fp/semantic_chunking/) , 2024-01-07-0911
```
Hi,  
Wrote an article on how to autonomously perform semantic chunking for a wide variety of documents. Please give it 
a read : [Semantic chunking using LLM](https://medium.com/@boudhayan-dev/semantic-chunking-in-practice-23a8bc33d56d)
```
---

     
 
all -  [ Can someone help me debug this? Trouble with rendering server-side code on client-side ](https://www.reddit.com/r/nextjs/comments/18y313s/can_someone_help_me_debug_this_trouble_with/) , 2024-01-07-0911
```
traceback:  


https://preview.redd.it/vtk57p0odcac1.png?width=1603&format=png&auto=webp&s=b72994a65b0f486c9b47f56afbc6b
5396af52411

  
here is the repo:

[https://github.com/Euticus/chatpdf/blob/main/lib/s3-server.ts](https://github.com/Eu
ticus/chatpdf/blob/main/lib/s3-server.ts)  
[https://github.com/Euticus/chatpdf/blob/main/lib/pinecone.ts](https://githu
b.com/Euticus/chatpdf/blob/main/lib/pinecone.ts)  


CONTEXT: this app is supposed to be an AI PDF analyzer. Node.js -->
 Pinecone --> AWS S3 --> Next.js   


I understand that it thinks it's running server-side code on the client-side but I
 can't figure out a way to fix it. Any help would be great.   


Things I've tried:   
1. messing with the config file. 
  
2. creating a handler to fetch the server-side operations  
3. consulting pinecone and AWS docs... as far as I can te
ll this is how it's supposed to be implemented.   


&#x200B;
```
---

     
 
all -  [ Has anyone gotten Langchain to stream Hugging Face models with FastAPI? ](https://www.reddit.com/r/LangChain/comments/18y2coy/has_anyone_gotten_langchain_to_stream_hugging/) , 2024-01-07-0911
```
 I'm wondering if streaming even works with the HuggingFaceTextGenInference llm code.

I  get responses from my model, b
ut only when I run the model normally,  and don't use the streaming=True parameter. I can also stream the model directly
 from my local server when I use curl, but not when I use langchain.

Context to the issue here with code example:

[htt
ps://github.com/langchain-ai/langchain/issues/15516](https://github.com/langchain-ai/langchain/issues/15516)

Any help i
s appreciated. :)
```
---

     
 
all -  [ Please help with this ](https://www.reddit.com/r/LangChain/comments/18xydx7/please_help_with_this/) , 2024-01-07-0911
```
  

promptT = PromptTemplate(template=prompt\_template, input\_variables=\['context', 'question'\])  
 

llm = ChatGoogl
eGenerativeAI(model='gemini-pro',google\_api\_key=google\_api\_key)  


chain = load\_qa\_chain(llm=llm, chain\_type='st
uff',prompt=promptT)  


keeps giving me below error:

File 'pydantic\\[main.py](https://main.py)', line 341, in pydanti
c.main.BaseModel.\_\_init\_\_

pydantic.error\_wrappers.ValidationError: 2 validation errors for LLMChain

llm

  instan
ce of Runnable expected (type=type\_error.arbitrary\_type; expected\_arbitrary\_type=Runnable)

llm

  instance of Runna
ble expected (type=type\_error.arbitrary\_type; expected\_arbitrary\_type=Runnable)

I am fed up with this..I tried with
out the prompt template and I am sure it has something to do with the model but not sure how to correct..
```
---

     
 
all -  [ LCEL with Streamlit fails to include memory in conversations. ](https://www.reddit.com/r/LangChain/comments/18xu7jd/lcel_with_streamlit_fails_to_include_memory_in/) , 2024-01-07-0911
```
Hello, I have been trying to join LCEL with StreamlitChatMessageHistory to store chat messages. This is my code:

    ll
m_chain =  RunnablePassthrough.assign( \
    history=RunnableLambda(memory.load_memory_variables)
    | itemgetter('hist
ory'))  |  prompt_to_ai  |   llm_openai    |       
    output_parser

I got the code snippet from here: https://python.
langchain.com/docs/expression_language/cookbook/memory

Can someone please assist? Thank you.
```
---

     
 
all -  [ RAG for Pdf with tables ](https://www.reddit.com/r/LangChain/comments/18xp9xi/rag_for_pdf_with_tables/) , 2024-01-07-0911
```
I want to built a RAG system for science documents which contains the theory texts along withn equations, tables, and la
belled diagrams. Questions can be from understanding of theory, equations and information about tables. How should I pro
ceed? Have idea of building a naive rag system only. 
Any resources will be helpful.
```
---

     
 
all -  [ Deploy Langchain-Streamlit App to EXE-File ](https://www.reddit.com/r/LangChain/comments/18xlzmg/deploy_langchainstreamlit_app_to_exefile/) , 2024-01-07-0911
```
Hi,

I have built a RAG app with Langchain and Streamlit and now want to share it with my team. As I am dealing with con
fidential data, I don't want to use a cloud solution, so my idea was to convert the Ap to an .EXE-File, so that they can
 load and use it with no programming expertise. I saw this tutorial, but it is not working for me. 

Does anyone have a 
good resource for this?
```
---

     
 
all -  [ Difference between Answer and Observation? ](https://www.reddit.com/r/LangChain/comments/18xjizi/difference_between_answer_and_observation/) , 2024-01-07-0911
```
Hi all

I am using an agent executor and agents and chains and tools to query a SQL database. 

The whole chatbot works 
fine, but I just have a question about the output I get.

https://imgur.com/a/1ET05Cq

What is the difference between th
e 'Observation' and the 'Answer'?

For my tool I have return_direct=True.

Secondly, I am trying to stream the output of
 my LLM. I am using a custom callback handler to do that, and I can stream the intermediate SQL query and everything, bu
t not the 'Answer', or the 'Observation'. How do I do that?

Finally, the LLM is the outputting the 'Answer:' text, but 
when I have a check within the custom callback handler to check for 'Answer:', it does not raise the flag as I intend it
 to.

Am I approaching this the wrong way?
```
---

     
 
all -  [ Hevolve : A production app using Langchain ](https://www.reddit.com/r/LangChain/comments/18xjflb/hevolve_a_production_app_using_langchain/) , 2024-01-07-0911
```

https://play.google.com/store/apps/details?id=com.hertzai.hevolve

Latency ~5 seconds coz of RAG, chains and tools but 
fully context aware coz of the same reason.

Microsoft copilot with an AI Avatar which can talk to you in 10 languages
```
---

     
 
all -  [ VectorStore.addDocuments - do not add duplicates ](https://www.reddit.com/r/LangChain/comments/18xidx1/vectorstoreadddocuments_do_not_add_duplicates/) , 2024-01-07-0911
```
I am using langchain VectorStore (currently QDrant and plain to use OpenSearch in future). 

It works fine, but I have i
ssues. If I run addDocument for the same doc twice - I have two copies of the doc in store. 

Of course I can search for
 doc with a give is in qdrant before adding it (transactions?). But I wonder if there is standard way to ensure uniquene
ss? 
```
---

     
 
all -  [ Integrating Azure CosmosDB as vectorstore for RetrievalQA? ](https://www.reddit.com/r/LangChain/comments/18xhjnu/integrating_azure_cosmosdb_as_vectorstore_for/) , 2024-01-07-0911
```
Hi all,

I currently have this codebase right here that uses `RetrievalQA` to create a Q&A Chatbot. This current iterati
on uses `Chroma` as the vectorstore, and works perfectly.

    vectorstore = Chroma(persist_directory='./chroma_db', emb
edding_function=OpenAIEmbeddings())
    
    
    template = '''
    Instructions here
    {context}
    Question: {ques
tion}
    Helpful Answer:
    '''
    
    
    QA_CHAIN_PROMPT = PromptTemplate(input_variables=['context', 'question']
, template=template)
    
    
    llm = ChatOpenAI(model_name='gpt-3.5-turbo', temperature=0)
    qa = RetrievalQA.from
_chain_type(llm,
                                   chain_type='stuff',
                                   retriever=vec
torstore.as_retriever(),
                                   chain_type_kwargs={'prompt': QA_CHAIN_PROMPT})
    
    qa.r
un(query)

However, I am required to migrate the vector database over to Azure CosmosDB (vCore). Following the documenta
tions, I have created a function that converts my text document into embeddings, and writes them to CosmosDB.

    def C
osmosEmbedder():
       loader = TextLoader('./data/file.txt')
       data = loader.load()
    
    
       # Document S
plitting
       text_splitter = RecursiveCharacterTextSplitter(chunk_size = 500, chunk_overlap = 0)
       all_splits = 
text_splitter.split_documents(data)
    
    
       CONNECTION_STRING = os.getenv('MONGO_URI')
       NAMESPACE = 'test
db.testcollection'
       DB_NAME, COLLECTION_NAME = NAMESPACE.split('.')
    
    
       client: MongoClient = MongoCl
ient(CONNECTION_STRING)
       collection = client[DB_NAME][COLLECTION_NAME]
    
    
       vectorstore = AzureCosmosD
BVectorSearch(collection, OpenAIEmbeddings())
    
    
       vectorstore.add_documents(all_splits)

And using a simila
r function, I am able to verify that the embeddings do exist within CosmosDB. Now here is where the documentation gets u
nclear to me. The documentation proceeds to use similarity search as a working example. But my goal is to use the Cosmos
DB as a vectorstore for `RetrievalQA` instead. 

Does anyone have any idea on how to implement this? For reference, the 
documentation I was referring to can be found [here](https://python.langchain.com/docs/integrations/vectorstores/azure_c
osmos_db).

Greatly appreciate any inputs on the situation.
```
---

     
 
all -  [ Where to host RAG app? ](https://www.reddit.com/r/LangChain/comments/18xe8di/where_to_host_rag_app/) , 2024-01-07-0911
```
 

I'm working on a student project that involves a FastAPI backend serving a RAG (Retrieval-Augmented Generation) appli
cation, which interfaces with a frontend already hosted on Netlify. The app leverages the LLaMA index, and I recently ma
de some enhancements following the 'small to big retrieval' strategies outlined [here](https://docs.llamaindex.ai/en/sta
ble/optimizing/advanced_retrieval/advanced_retrieval.html).

While these improvements have significantly boosted the app
's performance, they've also led to a new challenge: my current hosting solution on a Digital Ocean droplet isn't cuttin
g it anymore, as I'm consistently running into out-of-memory issues.

I'm now in the market for a hosting platform that 
can comfortably handle the heavier memory requirements of my updated backend. Key requirements include:

* Robust enough
 to support a memory-intensive FastAPI app.
* HTTPS support for security.
* Preferably developer-friendly and cost-effec
tive, considering it's for a student project.

Does anyone have recommendations for hosting providers or services that c
an meet these needs? Or, if you've worked on similar projects, I'd love to hear how you tackled the hosting challenges. 
Any insights, tips, or shared experiences would be greatly appreciated!

Thank you all in advance!
```
---

     
 
all -  [ Anyone experiencing slow OpenAI responses/completions? ](https://www.reddit.com/r/LangChain/comments/18xbb2u/anyone_experiencing_slow_openai/) , 2024-01-07-0911
```
I was trying out some LCEL chains on Jupyter Notebook, and all of a sudden, I realized that now my chat completions are 
taking four times longer than they were yesterday.

&#x200B;

https://preview.redd.it/4ac8dgews5ac1.png?width=737&format
=png&auto=webp&s=84d5115a4d74a73779b9a2deb4f2c12ffd5ffad1
```
---

     
 
all -  [ *kwargs in Agents ](https://www.reddit.com/r/LangChain/comments/18x4w1f/kwargs_in_agents/) , 2024-01-07-0911
```
1. &#x200B;

There's a \*\*kwargs parameter in initialize\_agent for additional keywords arguments for you agent. When i
 ask the LangChain chat which keywords are available for each agent, it doesn't even know. Where can i find more detaile
d documentation for each agent? Is want to know which keywords are available for each agent, or am i misunderstanding? T
hanks.

2.

Is langchain even worth it? Maybe it's just me, but i think the documentation is very bad, but is there even
 a better alternative?
```
---

     
 
all -  [ Struggling understanding conversational-chat-agent and prompt template ](https://www.reddit.com/r/LangChain/comments/18x356k/struggling_understanding_conversationalchatagent/) , 2024-01-07-0911
```
Hello people,

We've been at it for a long time and still are not understanding how to get a correct output from any mod
el. So what we're having problems understanding is how langchain expects the prompt template to be formated. THe thought
 flow. We are trying different Thought, Action, Action Input and Observation, Final Answer, etc.. methods and none seem 
to work with tools and regular conversations (and a mix of these).

What we really need is a manual to read that talks a
bout how these keywords are supposed to be used. For example, which ones are important for the agent and which for the l
lm.

We've tried so many templates. Some stop responding at the Observation point, some include the whole thought proces
s in the response, some don't work at all. We are god at reading and understanding. We just need an official source to r
ead from. If there is none, can someone help us here ?

Here is an example of our prompt template right now, but stalls 
:

<s> Today is {date}. Your name is Betty. You work for Shopping321 in Spain. Your duties involve helping our customer 
named {name} manage his online purchases.

TOOLS:

\----

&#x200B;

You have access to the following tools:

&#x200B;

(
LIST OF TOOLS I DELETED FOR PRIVACY, but they are working)

&#x200B;

THOUGHT PROCESS:

\----

&#x200B;

Start your thou
ght process using the following format:

&#x200B;

Thought: What´s the nature of the request? Does it involve using a sp
ecific tool?

Process: Understand the user's request and determine if you need to use a tool or various tools.

Temporar
y Observation: Initial thoughts on how to proceed.

&#x200B;

If you need to use a tool, use the following thought proce
ss:

&#x200B;

Thought: Do I need to use a tool? Yes.

Action: \[Action to take, choose from tool list\] like this examp
le: 'InvoiceSearch'

Action Input: the input for the action and {request\_id}

Observation: the result of the action.

.
.. (this Thought/Action/Action Input/Observation can repeat only N times)

&#x200B;

If you do not need to use a tool, u
se the following thought process:

&#x200B;

Thought: How can I respond with my own knowledge without using a tool?

Pro
cess: Handle the request using natural conversation, applying the abstraction

Temporary Observation: Observations about
 the handling process

&#x200B;

CONCLUSIONS:

\----

Before giving the final response, gather all of your thoughts and 
observations made with and without tool usage. Order the thoughts aligned with the user's requests. Then prepare to give
 a final response following this thought process:

&#x200B;

Thought: Does the response fullfil the user's request based
 on all of the observations gathered thus far?

Process: Make final adjustments in order to fullfil user's requests. Use
 more tools if necessary.

&#x200B;

Betty: Deliver the comprehensive final response.

&#x200B;

Begin!

&#x200B;

Previ
ous conversation history:

{chat\_history}

&#x200B;

Request ID: {request\_id}

&#x200B;

{agent\_scratchpad}

&#x200B;


\[INST\] {input} \[/INST\] </s>

I am willing to pay via paypal for any personal assistance. Thanks!
```
---

     
 
MachineLearning -  [ [Project] Temporal Augmented Retrieval (TAR) - Dynamic RAG ](https://www.reddit.com/r/MachineLearning/comments/18uddmj/project_temporal_augmented_retrieval_tar_dynamic/) , 2024-01-07-0911
```
From a corpus of text, how can you detect emerging topics and their evolution through time?

Introducing Temporal Augmen
ted Retrieval (TAR). (built in the context of buildspace n&w s4)

TAR is an open-source advanced RAG approach that aims 
to factor in the dynamic and temporal aspects of textual data when performing retrieval.

It allows us to understand the
 evolution of discussed topics over time.

The idea behind this project is to open the debate regarding the current limi
tations of RAG methods

This first approach has been built without using RAG frameworks (like Jerry Liu’s langchain) and
 focuses on financial tweets 

Relevant links:

Medium: [https://medium.com/@adam-rida/temporal-augmented-retrieval-tar-
dynamic-rag-ad737506dfcc](https://medium.com/@adam-rida/temporal-augmented-retrieval-tar-dynamic-rag-ad737506dfcc)

Gith
ub:[https://github.com/adrida/Temporal\_RAG](https://github.com/adrida/Temporal_RAG)

Hugging Face Benchmark: [https://h
uggingface.co/spaces/Adr740/Temporal-RAG-Benchmark](https://huggingface.co/spaces/Adr740/Temporal-RAG-Benchmark)

My web
site: [adrida.github.io](https://adrida.github.io)

&#x200B;

https://preview.redd.it/lj7wkhk70f9c1.png?width=960&format
=png&auto=webp&s=fc79c5034351a1711e1ec051919a5c4d2edbc333
```
---

     
 
MachineLearning -  [ [R][P] Autogen + Langchain Tools + Local LLM doesn't work. ](https://www.reddit.com/r/MachineLearning/comments/18tex1j/rp_autogen_langchain_tools_local_llm_doesnt_work/) , 2024-01-07-0911
```
Hey folks, 

So I'm playing around with the agent framework Autogen and I'm trying to create agents by providing it cust
om tools to use. These custom tools are defined in the langchain framework. Furthermore, I am using open source LLM mode
ls like Mistral, LLAMA, Mixtral etc.

In my experience, I have been unable to get the Autogen+LocalLLM framework to iden
tify the right tools to use given the prompt. However it does a fantastic job with the GPT model. 

Please note that my 
goal is for the agent to mandatorily use the tools provided and not come up with its own code. And the agent should figu
re out the right tool to use. 

I have been very explicit with my prompting, despite which I am unable to get this to wo
rk.

Any thoughts and suggestions? Please let me know ! Please share your experiences as well. Cheers !
```
---

     
 
MachineLearning -  [ [P] Seeking Advice for Building a School Handbook Chatbot Using OpenAI and Vector Databases ](https://www.reddit.com/r/MachineLearning/comments/18rndcp/p_seeking_advice_for_building_a_school_handbook/) , 2024-01-07-0911
```
Hello everyone,

I'm embarking on a project to create a chatbot for my school's handbook, aiming to make it a resource f
or students to easily access information. As someone relatively new to AI, I'm seeking guidance on implementing this.

M
y current plan is to use OpenAI as the primary language learning model, focusing on affordability. I am considering inte
grating RAG (Retrieval-Augmented Generation) and LangChain for enhanced functionality. However, I'm quite perplexed abou
t choosing an appropriate vector database, as many options appear costly. The goal is to keep this system live and acces
sible for student usage without breaking the bank.

I'm also looking into open-source embedding models to pair with the 
vector database. Pinecone has caught my attention, but its pricing seems steep for our budget.

Does anyone have recomme
ndations or tips on affordable yet effective tools and strategies for this project? Any insights on vector databases sui
table for educational use, or ways to optimize cost without compromising quality, would be greatly appreciated.

Thank y
ou in advance for your help!

(I typed out my problem and had gpt4 fix up the format and wording dont bash me)
```
---

     
 
MachineLearning -  [ [D] github repositories for ai web search agents ](https://www.reddit.com/r/MachineLearning/comments/18dhtm4/d_github_repositories_for_ai_web_search_agents/) , 2024-01-07-0911
```
Do you know of any github repositories that either help with building a web search ai agent or that has a good one?

git
hub repositories that I saw so far but have not yet tried :

- langchain (the WebResearchRetriever and weblangchain for 
example (have not tried either) )
- autogpt
- gpt-researcher

[Edit: changed researchgpt to gpt-researcher]
```
---

     
 
MachineLearning -  [ [P] flex-prompt: a flexible prompt rendering engine that ensures you'll never exceed your LLM's cont ](https://www.reddit.com/r/MachineLearning/comments/18d581q/p_flexprompt_a_flexible_prompt_rendering_engine/) , 2024-01-07-0911
```
When working with LLMs, I frequently experience *token agony*.

[Error: This model's maximum context length is 4097 but 
you are trying to push in all of War and Peace, you imbecile](https://preview.redd.it/nldj0qva4s4c1.png?width=1348&forma
t=png&auto=webp&s=b16af79d83f329db1b77b32ed621f0138d7cc04d)

Perhaps you've experienced it too! The issue is particularl
y pronounced with retrieval augmented pipelines, since you have potentially quite a large set of documents which you cou
ld perhaps include in the prompt if only you knew how big it could be.

I got tired of hacking around this headache, so 
I wrote `flex-prompt` to address it. I wish I didn't have to. Perhaps someone can point me to a better solution! But I c
ouldn't find one, so alas, here it is.

`flex-prompt` provides a basic layout and component model to help you describe h
ow you want the pieces of your prompt to grow and shrink and a token-aware renderer which renders your prompt to fit you
r model's window.

[Github](https://github.com/queerviolet/flex-prompt), [Intro to flex prompt colab](https://colab.rese
arch.google.com/github/queerviolet/flex-prompt/blob/main/doc/intro_to_flex_prompt.ipynb)

# Quick examples

You can just
 `render(Flex(...))`, and flex prompt will fit the prompt into the context window, and tell you how many tokens are left
 over for the response:

    from flex_prompt import render, Flex, Expect
    rendered = render(
        Flex([
        
  'Given the text, answer the question.',
          '--Text--',
          WAR_AND_PEACE,
          '--End Text--',
     
     'Question: What's the title of this text?',
          'Answer:', Expect()
        ], join='\n'),
        model='tex
t-davinci-002')
    
    # rendered.output is the string to send to the model
    # rendered.max_response_tokens is how 
many tokens you can
    #   request in response without exceeding the model's context window
    print(rendered.output, 
rendered.max_response_tokens)

More typically, you'll want to define a prompt which takes parameters. To do this, you ca
n create a class (probably a dataclass) which derives `Flexed`:

    from flex_prompt import Flexed, Expect
    from dat
aclasses import dataclass
    
    @dataclass
    class Ask(Flexed):
      text: str
      question: str
      answer: s
tr | Expect = Expect()
      instruct: str = 'Given a text, answer the question.'
    
      flex_join = '\n' # yielded 
items will be joined by newlines
      def content(self, _ctx):
        if self.instruct:
          yield 'Given the tex
t, answer the question.'
          yield ''
        yield '-- Begin Text --'
        # note: we're using `Flex` here jus
t to attach a flex_weight
        # to the text, telling the renderer we'd like more space for the
        # text than a
nything else.
        yield Flex([self.text], flex_weight=2)
        yield '-- End Text --'
        yield 'Question: ', 
self.question
        yield 'Answer: ', self.answer

The renderer works much as you might expect. You can \`yield\` anyt
hing which you can pass to the top-level render function, including other components, creating a whole tree.

Note that 
the component above can be used to render both the actual prompt and examples. Examples simply have an `answer`. This is
 useful for experimenting with different ways of structuring a prompt while ensuring that all the examples we present to
 the LLM are in the same format.

# LangChain and Haystack Integrations

Flex prompt doesn't really care how you execute
 your prompt. For convenience, `render(model=)` does accept both LangChain and Haystack models:

    ask_tolstoy = Ask(t
ext=WAR_AND_PEACE, question='Who wrote this?')
    
    # Using LangChain
    from langchain.llms import OpenAI
    lc_l
lm = OpenAI()
    rendering = render(ask_tolstoy, model=lc_llm)
    print(lc_llm(rendering.output, max_tokens=rendering.
max_response_tokens))
    
    
    # Using Haystack
    from haystack.nodes import PromptModel
    
    hs_llm = Prompt
Model(model_name_or_path='text-davinci-002', api_key=os.environ['OPENAI_API_KEY'])
    rendering = render(ask_tolstoy, m
odel=hs_llm)
    print(hs_llm.invoke(rendering.output, max_tokens=rendering.max_response_tokens))
    

# Is it worth it
?

As models grow larger and larger context windows, I've asked myself whether this is worth it. Won't context sizes eve
ntually big enough to put in everything we might want without worry?

One response: 'everything I might want' is a very,
 very big set, plausibly bigger than any window size we're going to see soon.

Another: being able to do this kind of to
ken accounting is useful even if we don't completely fill context windows. For example, we might be able to augment our 
prompt with examples, documents, and tips. How much space should we allocate to each? The answer might well be model-dep
endent. How do we figure it out?

Flex prompt's output, a `Rendering` object, actually holds the entire component tree. 
You can look through the object to see how many tokens were allocated to each child. This is currently very manual, but 
it does provide the bedrock infrastructure to e.g. run tests to discover the optimal balance of augmented data for a giv
en prompt and model.

Additionally, the right admixture (and for that matter, the right *phrasing*) may well be model-de
pendent. Flex prompt currently provides only very limited model-specific rendering (you can look at [`ctx.target`](https
://ctx.target), but it doesn't tell you much), but there's no reason that can't be significantly improved. At the extrem
e limit is prompt *erasure*, where we fine-tune a model to require no or minimal instructions/examples for a given set o
f prompts. Flex prompt can enable transitions like this with no changes to the pipelines themselves: you'd still use the
 same prompt components, they'd just render differently if the target is a fine-tuned model vs. a generic one.

# Status
 & Future Work

Flex prompt is very much in early development. I would love to hear if and how people find it useful, an
d would love input and contributions!

Some things I'd like to tackle in the future:

* **Rendering message lists.** Fle
x prompt currently only renders strings, though it's set up to be able to render any type of output. Message histories b
asically grow without bound, so supporting this seems like a no-brainer.
* **Pagination**. If your rendering overflows (
as above, where we're trying to stuff *the entirety of war and peace* into a prompt), flex prompt will clip the offendin
g pieces to fit. But there's currently no way to get 'the next page'. But the `Rendering` actually retains enough inform
ation to do this! It would be great to be able to call `render(...).pages()` to get the sequence of prompts as we 'scrol
l' whatever has overflowed. This is medium-hanging fruit—a little tricky because we do have to descend the tree of rende
rings to find the exact one(s) which overflowed and then update only those.
* **Token accounting.** As mentioned above, 
you can currently grovel around in `Rendering` and look at the pieces of the prompt. This would be more useful if it wer
e a little easier, e.g. if you could use `rendering[Examples]` to find all the parts rendered by the `Examples` componen
t, or `rendering['advice']` to find all the parts which are tagged (somehow) as 'advice'. The use case here is prompt op
timization: discovering the optimal number or percentage of tokens to allot to each thing we might want to drop into the
 prompt.
* **More integrations.** Currently, flex prompt only supports OpenAI models. You can register your own target f
inders, but it would be great to have more support out of the box. This is mostly a matter of digging around and finding
 the tokenizers and window sizes for common models, and then writing the appropriate target finders. Contributions very 
welcome!
* **Model tuning.** As mentioned above, the rendering context could provide a mechanism for fetching model-spec
ific parameters. The basic idea is that `ctx[param]` will evaluate `param` against the context, and then we can define s
ome parameter types which load their model-specific values from *gestures vaguely* somewhere.

Thanks for reading!

* [F
lex prompt Github](https://github.com/queerviolet/flex-prompt)
* [Intro to flex prompt colab](https://colab.research.goo
gle.com/github/queerviolet/flex-prompt/blob/main/doc/intro_to_flex_prompt.ipynb)
* [My website](https://ashi.io). *shame
less plug: I have a lot of engineering experience and a bit of machine learning experience and* [*I am currently looking
 for a job*](https://ashi.io/resume.pdf)
```
---

     
 
MachineLearning -  [ [D] Working on RAG? You should be evaluating its performance and we've built a way to do that. ](https://www.reddit.com/r/MachineLearning/comments/18ciet5/d_working_on_rag_you_should_be_evaluating_its/) , 2024-01-07-0911
```
Check out our new open-source tool, Tonic Validate: [https://www.tonic.ai/validate](https://www.tonic.ai/validate)  


W
e've also been using the tool to evaluate different RAG tools out there. The latest post on LangChain vs Haystack is ava
ilable here:  [https://www.tonic.ai/blog/rag-evaluation-series-validating-the-rag-performance-of-langchain-vs-haystack](
https://www.tonic.ai/blog/rag-evaluation-series-validating-the-rag-performance-of-langchain-vs-haystack)

&#x200B;

Let 
us know what you think and if you're working on a RAG project, we'd love to hear about it! How are you measuring your RA
G system performance?
```
---

     
 
deeplearning -  [ Unlocking the Power of Language: How LangChain Transforms Data Analysis and More ](https://www.reddit.com/r/deeplearning/comments/18l788y/unlocking_the_power_of_language_how_langchain/) , 2024-01-07-0911
```
Language models have revolutionized natural language processing (NLP), yet they grapple with limitations that impede the
ir full potential. Enter LangChain, a pioneering framework that transcends these constraints, fostering innovative langu
age-based applications. To comprehend LangChain’s significance, we must first grasp the limitations plaguing large langu
age models (LLMs).

link: [https://medium.com/ai-advances/unlocking-the-power-of-language-how-langchain-transforms-data-
analysis-and-more-3c4f327d520d](https://medium.com/ai-advances/unlocking-the-power-of-language-how-langchain-transforms-
data-analysis-and-more-3c4f327d520d) 
```
---

     
 
deeplearning -  [ [D] Mastering Chain Composition with LangChain Expression Language (LCEL) ](https://www.reddit.com/r/deeplearning/comments/18i0wot/d_mastering_chain_composition_with_langchain/) , 2024-01-07-0911
```
In the intricate landscape of modern software development, orchestrating complex sequences of actions seamlessly poses a
 significant challenge. Enter LangChain Expression Language (LCEL), a groundbreaking declarative approach designed to re
volutionize the composition of chains within software architecture.

Link: [https://medium.com/ai-artistry/mastering-cha
in-composition-with-langchain-expression-language-lcel-2d5041fb0cbd](https://medium.com/ai-artistry/mastering-chain-comp
osition-with-langchain-expression-language-lcel-2d5041fb0cbd)  
```
---

     
