 
all -  [ Here's how you can add AI superpowers to your C# app! ](https://www.reddit.com/r/csharp/comments/191yhnz/heres_how_you_can_add_ai_superpowers_to_your_c_app/) , 2024-01-09-0910
```
I've been working with C# for many, many years now... More recently, I've been testing and writing about AI tools and da
ta frameworks like LangChain and LamaIndex that make it easier for me to add AI capabilities to my apps.

After some tes
ting and a bunch of articles, I found that the Semantic Kernel SDK from Microsoft is the ideal solution for C# devs like
 me since it's part of the framework and can easily consume existing C# functions with few (if any) modifications.

Here
's what I build using Semantic Kernel:

* Three prompt plugins  

   * One that generates a common myth about AI using O
penAI's GPT
   * One that fact-checks it
   * One that adjusts the generated output to match a social media posting best
 practices
* One native function  

   * Simulates posting to social media

[I wrote an easy-to-follow step-by-step Sema
ntic Kernel tutorial](https://www.gettingstarted.ai/using-semantic-kernel-add-ai-capabilities-to-csharp-app-microsoft-pa
rt-1/). Please share your feedback and leave a comment below if you have any questions. Happy to help!

Cheers 🥂
```
---

     
 
all -  [ React prompting Mistral or Mixtral ](https://www.reddit.com/r/MistralAI/comments/191wg3i/react_prompting_mistral_or_mixtral/) , 2024-01-09-0910
```
I am trying to create an agent using tools by using react prompting technique for mixtral:8x7b-instruct-v0.1-q4\_K\_M. I
 am mixing langchain zeroshot agent strategy and the strategy from this page [https://www.pinecone.io/learn/mixtral-8x7b
/](https://www.pinecone.io/learn/mixtral-8x7b/) using JSON answers leading to instructions like:

    You are an XY agen
t capable of using a variety of tools to answer a question. ...
    
    
    Here are the tools:
    - ...
    - ...
  
  
    To use these tools you must always respond in JSON format containing `'tool_name'` and `'input'` key-value pairs!
 For example, ...
    
    ```json
    {
        'tool_name': 'sql_get_similar_examples',
        'input': 'How many mac
hines are there?'
    }
    ```
    
    Use the following format:
    
    User: the input question you must answer 
  
  Thought: you should always think about what to do 
    Action: the action to take in the JSON format listed above, whe
reas 'tool_name' should be one of [...] and 'input' should be the input of the tool
    Observation: the result of the a
ction 
    ... (this Thought/Action/Observation can repeat N times) 
    Thought: I now know the final answer 
    Final
 Answer: the final answer to the original input question by using the Final Answer tool in JSON format   
    
    Begin
!  
    
    User: {input} 
    Thought: {first thought}
    Action: ```json
    {
        'tool_name': 

It actually wo
rks quite well for the first couple of Thought/Action/Observation iterations. When the llm wants to call a tool I run it
 and append the llm answer as well as the tool's result (which can be quite long) with a new '\\nThought: ' string to th
e prompt and run the merged prompt again. The llm then comes up with a new Thought and Action.

Still, after a couple of
 iterations the llm somehow looses the whole context and does not call tools anymore. It seems to lose its purpose of an
swering the user question but simply describes the last tool output in the 'Thought:' section. May it be, the prompt get
s too long for Mixtral to follow the react pattern?

Have you got any experience/advice for using Mixtral as react agent
?
```
---

     
 
all -  [ [For Hire] Laravel and TALL Stack Wizard with Python, AI Automation, and API Integration Superpowers ](https://www.reddit.com/r/forhire/comments/191v0no/for_hire_laravel_and_tall_stack_wizard_with/) , 2024-01-09-0910
```
Hello, reddit!

My name is Patrick, and I live in Utah.

I'm a Laravel and TALL Stack Wizard with Python, AI Automation,
 and API Integration Superpowers. I have over 10 years of experience as a contract developer, working with various clien
ts and projects across different industries and domains.

I can help you build amazing web applications using Laravel, t
he most popular PHP framework, and the TALL stack, which consists of Tailwind CSS, Alpine.js, and Livewire. These techno
logies allow me to create beautiful, dynamic, and reactive web apps with minimal JavaScript and elegant syntax.

I also 
have expertise in Python, AI automation, and API integration. I can use Python to create powerful scripts, bots, scraper
s, crawlers, and data analysis tools. I can automate various tasks and processes using AI and machine learning technique
s. I can integrate your web app with various platforms and services using APIs, such as Zapier, Make, Botpress, Langchai
n, and more.

I'm looking for projects that are challenging, interesting, and rewarding. I'm open to working on an hourl
y basis ($60/hour), a project-based contract, or a monthly retainer with support, maintenance, and devops/hosting servic
es. I can only work remotely at this time as I live in a semi rural area in southern Utah. I'm flexible with the time zo
ne and schedule.

If you are interested in hiring me, please send me a PM or chat request. GitHub and LinkedIn available
 on request.

Thank you for reading and I hope to hear from you soon! 😊
```
---

     
 
all -  [ Roast my resume ](https://www.reddit.com/gallery/191sxai) , 2024-01-09-0910
```

```
---

     
 
all -  [ has anybody used langchain tools but totally used custom logic for parsing LLM responses and invokin ](https://www.reddit.com/r/LangChain/comments/191sm46/has_anybody_used_langchain_tools_but_totally_used/) , 2024-01-09-0910
```
I like the tools but I'm not a huge fan of the default agent prompts. Just wondering if anybody has done this? 
```
---

     
 
all -  [ Opensource Practical AI Development for Javascript Developers primer! (Uses Nextjs and AI SDK for ma ](https://www.reddit.com/r/nextjs/comments/191rbv7/opensource_practical_ai_development_for/) , 2024-01-09-0910
```
Hey everyone!

Excited to share this with you.

![image](https://github.com/thestriver/ai-for-javascript-course/assets/1
6709708/95237a88-63e2-48b6-a2c6-fc45ff49fe7b)

I released an open-source course for Javascript developers who want to bu
ild AI applications on GitHub. All 60 pages of them (if you want the PDF format of the primer). (The markdown file is at
 over 1600 lines right now and growing.) 🙂

Structured to take Javascript developers from 0-1, I put in everything I kno
w from building AI-powered apps over the past year, and I hope you find it useful too.

[Github Link](https://github.com
/thestriver/ai-for-javascript-course)

Here are some of the topics touched on in the modules:

- **Introduction to LLMs 
🧩**
- **Advanced Prompt Engineering and Optimization ✏️**
- **Integrating** **OpenAI GPT 3.5 and Mistral 7B Instruct v0.
2 into JS apps**
- **Retrieval Augmented Generation 💬**
- **Using Vercel AI SDK, Pinecone, and Langchain to build a Rese
arch Assistant Tool**
- **Function Calling**
- **Building** 3 ****AI Agents with different levels of complexity 🤖****
- 
**Security, Ethics, and Performance in AI Development**

A relevant project accompanies each course.

I created this cou
rse hoping it would be an excellent guide for aspiring AI developers and a valuable resource for the wider JavaScript de
veloper community.

I would love to get your feedback and, of course, would appreciate it if you shared any bugs or mist
akes you discover or questions with me.
```
---

     
 
all -  [ NeuralGPT - A Working Character.ai Client ](https://www.reddit.com/r/AIPsychology/comments/191r7jj/neuralgpt_a_working_characterai_client/) , 2024-01-09-0910
```
Short update - I just wrote a character.ai client (just like the title suggests :P) based on their unofficial API - you 
can find it here:  
 [NeuralGPT/Chat-center/characterAI.py at main · CognitiveCodes/NeuralGPT (github.com)](https://gith
ub.com/CognitiveCodes/NeuralGPT/blob/main/Chat-center/characterAI.py) 

You can speak with your characters directly, run
 it as websocket server or connect it to an already running server.   
First you must provide your user token to log in 
and then paste your character ID. You can find instructions how to get them in here:  [Xtr4F/PyCharacterAI: An unofficia
l Python api wrapper for character.ai (github.com)](https://github.com/Xtr4F/PyCharacterAI)   


https://preview.redd.it
/mkp0jmqk89bc1.png?width=1193&format=png&auto=webp&s=ff4d956cc35d50a4c4ae43e85a4eb83ee351bd24
```
---

     
 
all -  [ I released a new opensource Practical AI Development for Javascript Developers course! (Heavily uses ](https://www.reddit.com/r/LangChain/comments/191r21r/i_released_a_new_opensource_practical_ai/) , 2024-01-09-0910
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

     
 
all -  [ New to LangChain? Start here! ](https://www.reddit.com/r/LangChain/comments/191q3qk/new_to_langchain_start_here/) , 2024-01-09-0910
```
Hi 👋 

I wrote this [introductory post](https://www.gettingstarted.ai/everything-you-need-to-know-when-getting-started-w
ith-langchain/) for anyone just getting started with LangChain.

I try to keep it simple while going over important poin
ts so you can get started in no time.

If you’re new to LangChain, you’ll want to [read this introductory post](https://
www.gettingstarted.ai/everything-you-need-to-know-when-getting-started-with-langchain/) and then dive deeper into more a
dvanced topics as you progress.
 
Check it out and let me know if you have any questions or feedback.

Cheers!
```
---

     
 
all -  [ [D] Unleashing the Power of Langchain with Wandb: Revolutionizing Topic Modeling and Evaluation ](https://www.reddit.com/r/deeplearning/comments/191mm83/d_unleashing_the_power_of_langchain_with_wandb/) , 2024-01-09-0910
```
Complementing Langchain’s prowess, Wandb emerges as a powerhouse meticulously designed for developers leveraging LLM tec
hnology. As an evaluation framework and production monitoring platform, Wandb stands out for its tailored approach. Its 
arsenal comprises real-time monitoring, granular analytics, and streamlined evaluation processes, laying the groundwork 
for elevated performance and reliability in AI applications.

&#x200B;

Link: [https://medium.com/ai-advances/unleashing
-the-power-of-langchain-with-wandb-revolutionizing-topic-modeling-and-evaluation-75af5cf51b15](https://medium.com/ai-adv
ances/unleashing-the-power-of-langchain-with-wandb-revolutionizing-topic-modeling-and-evaluation-75af5cf51b15) 
```
---

     
 
all -  [ Can you suggest some top-notch teams actively looking for exceptional machine learning engineers or  ](https://www.reddit.com/r/jobs/comments/191j5ri/can_you_suggest_some_topnotch_teams_actively/) , 2024-01-09-0910
```
Hey everyone,

I have 7 years of experience in the Machine Learning domain. Currently, I am looking for a long-term oppo
rtunity in a team that aligns with my values and culture. The ideal team should focus on result-driven performance evalu
ations, maintain transparency, foster a collaborative environment and have little to no office politics. Additionally, i
t would be great if they follow good software engineering and documentation practices.

Tech Stack: Python(Dask, NumPy, 
SciPy, Pandas, Xgboost, OpenCV, scikit-learn, NLTK, Gensim, PySpark), Deep Learning (TensorFlow, Keras, PyTorch), Flask,
 FastAPI, SQL, Neo4j, Cloud Technologies (Google Cloud Platform, MLFlow, Kubernetes) and NLP (spaCy, Stanford CoreNLP, L
lamaIndex, LangChain and advanced NLP techniques like RAG, DPO, LoRA and QLoRA), MLFlow, Apache Airflow, Apache Beam, Do
cker, Kubernetes\[Beginner\], HuggingFace

Skills: Linux, Git, CI/CD, Machine learning, NLP, Computer Vision, Recommende
r Systems

I am a qualified candidate with experience in the field, and I would appreciate your help finding my next opp
ortunity. Thank you for your support.
```
---

     
 
all -  [ [D] Any good teams hiring for ML Engineers or Python Devs ](https://www.reddit.com/r/MachineLearning/comments/191io4z/d_any_good_teams_hiring_for_ml_engineers_or/) , 2024-01-09-0910
```
Hey everyone,

I have 7 years of experience in the Machine Learning domain. Currently, I am looking for a long-term oppo
rtunity in a team that aligns with my values and culture. The ideal team should focus on result-driven performance evalu
ations, maintain transparency, foster a collaborative environment and have little to no office politics. Additionally, i
t would be great if they follow good software engineering and documentation practices.

**Tech Stack:** Python(Dask, Num
Py, SciPy, Pandas, Xgboost, OpenCV, scikit-learn, NLTK, Gensim, PySpark), Deep Learning (TensorFlow, Keras, PyTorch), Fl
ask, FastAPI, SQL, Neo4j, Cloud Technologies (Google Cloud Platform, MLFlow, Kubernetes) and NLP (spaCy, Stanford CoreNL
P, LlamaIndex, LangChain and advanced NLP techniques like RAG, DPO, LoRA and QLoRA), MLFlow, Apache Airflow, Apache Beam
, Docker, Kubernetes\[Beginner\], HuggingFace  
**Skills:** Linux, Git, CI/CD, Machine learning, NLP, Computer Vision, R
ecommender Systems

I am a qualified candidate with experience in the field, and would appreciate your help in finding m
y next opportunity. Thank you for your support.
```
---

     
 
all -  [ 1.5 yıl önce mezun oldum hala iş bulamıyorum, tavsiyeleriniz var mı? ](https://www.reddit.com/r/CodingTR/comments/191hmxf/15_yıl_önce_mezun_oldum_hala_iş_bulamıyorum/) , 2024-01-09-0910
```
Merhabalar.

Ben orta-iyi arası bir üniversiteden mezun olmuş birisiyim. Okul zamanımda, çeşitli çalışma ve projelerde y
er aldım, kulüp ve ekiplerde yer aldım, kendim çalıştım bir şeyler geliştirdim, bir çok farklı teknoloji öğrendim. Ancak
 şu ana kadar yalnızca bir kaç kez interview yapma şansım oldu. LinkedIn üzerinden 100 yere başvurduysam 2 şirket ile gö
rüştüm şimdiye kadar, yabancı 10 şirkete başvurdum, oradan da 2 şirket ile görüşme yapabildim. Aralarında iyi giden tek 
görüşme Canonical ile yaptığım görüşmeydi, onda da 4 farklı etaptan yalnızca bir görüşmede zorlandım ve başarısız oldum.


Demem o ki, bu kadar application yapıyor ve iş bulamıyorsam bir yerlerde hata yapıyorum demektir. Tanıdığım hiçkimse y
ok, referansım yok, torpil yok, fakir sıradan bir aileyiz. Kendi emeklerimle çok fazla şey öğrendimi düşünüyorum, öğrend
iğim çeşitli open-source teknikler ile bir çok teknik soruna çözüm bulmakta kendimi yetenekli görüyorum ama maalesef eli
me hiçbir şey geçmiyor. Bu durumu tersine çevirmek için ne yapmam gerekiyor?

(CV'yi 1 sayfa tutmaya çalıştığım için pro
jelerden sadece 2sini koydum, 2 sayfaya çıkarıp her şeyi dahil etmeyi planlıyorum artık)

&#x200B;

https://preview.redd
.it/c0v8kcc3m6bc1.png?width=738&format=png&auto=webp&s=f90909bedf64424128bcd548ecb825715dd45df8
```
---

     
 
all -  [ RAG - Responding with multiple data types ](https://www.reddit.com/r/LangChain/comments/191d8td/rag_responding_with_multiple_data_types/) , 2024-01-09-0910
```
Hi 

I'm fairly new to this so pardon the basic question, I poked around this community but couldn't find the response s
o some help would be kindly appreciated. Here's the situation:

I'm using RAG to build an assistant for my employer. Cur
rently I've set up a chatbot that uses Langchain, OpenAI embedding, Deeplake as a vector database. And my current setup 
works well from a demo perspective where I can show the chatbot responding over some code files and giving some value. H
owever, when I combine other data types into the database (after chunking and embedding) such as my companies Confluence
 documentation, it doesn't seem to mesh well with the codebase data. I believe i should be doinf this in a way where the
 vector database has files stored in such a way that makes it clear for the retriever what part of the vector database c
ame from a codebase and what part came from documentation (confluence) and they need to be referenced together but store
d seperately to work effienciently. 

Moreover i need some kind of an agent setup which can identify whether to respond 
with context from the codebase's vector files or from the confluence documentations vector files or an appropriate combi
nation of both (that would be ideal). . 

It would also be extremely powerful if I could also somehow add on the compani
es PDFs, word files, PowerPoint, excel files etc. Into the mix and have it all be part of the same RAG flow. 

I would a
ppreciate some guidance from people who have done similar or the knowhow to solve this.
```
---

     
 
all -  [ Can someone please help me understand why this document lookup app can't remember previous questions ](https://www.reddit.com/r/LangChain/comments/191bsyn/can_someone_please_help_me_understand_why_this/) , 2024-01-09-0910
```
Hi everyone I'm trying to create a document retrieval app with memory. Currently it will only answer document questions 
and will not answer successive questions.   
For example if I ask for 3\*3 it returns correctly but if i ask it to multi
ply the previous result by 3 it will tell me the document doesn't have a number it knows to multiply by 3. Any help woul
d be greatly appreciated.

    import streamlit as st
    from langchain.memory.chat_message_histories import StreamlitC
hatMessageHistory
    
    
    from io import StringIO
    
    
    import pinecone
    
    pinecone.init(api_key='',
 environment='gcp-starter')
    
    from langchain import PromptTemplate
    from langchain.chat_models import ChatOpen
AI
    from langchain.chains import LLMChain
    from langchain.chains import ConversationalRetrievalChain
    from lang
chain.embeddings import OpenAIEmbeddings
    
    from langchain.vectorstores import Pinecone
    from langchain.text_sp
litter import RecursiveCharacterTextSplitter
    
    from langchain.memory import ConversationBufferMemory
    
    fro
m langchain.schema import SystemMessage
    
    
    
    OPENAI_API_KEY = ''
    OPENAI_DIMENSION = 1536
    
    embe
dding = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
    
    st.reupload_file = False
    
    vector_store = Pineco
ne.from_existing_index('legal-cases', embedding)
    index = pinecone.Index('legal-cases')
    
    
    def upload_new_
file_to_pinecone(text):
        embedding = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
    
        text_splitter =
 RecursiveCharacterTextSplitter(
            chunk_size=100, chunk_overlap=0, length_function=len
        )
    
       
 chunks = text_splitter.create_documents([text])
    
        result = Pinecone.from_documents(chunks, embedding, index_
name='legal-cases')
    
    
    st.title('📝 File Q&A')
    
    uploaded_file = st.file_uploader('Upload an article', 
type=('txt', 'md'))
    
    if st.reupload_file:
        print('updated file')
        # To read file as bytes:
       
 bytes_data = uploaded_file.getvalue()
    
        # To convert to a string based IO:
        stringio = StringIO(uploa
ded_file.getvalue().decode('utf-8'))
    
        # To read file as string:
        string_data = stringio.read()
    
 
       index.delete(delete_all=True)
    
        upload_new_file_to_pinecone(string_data)
    
    
    
    from langc
hain.chains import RetrievalQA
    from langchain.chat_models import ChatOpenAI
    
    
    
    
    k = 3
    # user
's question text input widget
    q = st.text_input('Ask a question about the content of your file:')
    
    
    if q
:  # if the user entered a question and hit enter
        standard_answer = ''
        q = f'{q} {standard_answer}'
    

        system_message = f'''
            You are an assistant which helps to user find answers to his question with in
ternal company data.
            This data will be provided by a vector db as context.
            You also help with no
rmal stuff like answering questions or generating text by ignoring this system message.
            When asked to summar
ize a specific page only summarize pages which match the page id within the url if appliable.
        '''
        system
_message = SystemMessage(content=system_message)
    
    
        memory = ConversationBufferMemory(
            memory
_key='chat_history',
            input_key='question',
            output_key='answer',
            return_messages=True
,
        )
    
        memory.chat_memory.add_message(system_message)
        
        
        llm = ChatOpenAI(model
='gpt-3.5-turbo', temperature=1, api_key=OPENAI_API_KEY)
        retriever = vector_store.as_retriever(
        search_t
ype='similarity', search_kwargs={'k': k}
    )
        chain = ConversationalRetrievalChain.from_llm(
            llm,
 
           retriever=retriever,
            memory=memory,
            return_source_documents=True,
    )
        answe
r = chain({'question' : q})['chat_history'][-1].content
    
    
        # text area widget for the LLM answer
        
st.text_area('LLM Answer: ', value=answer)
        st.divider()
        # if there's no chat history in the session stat
e, create it
        if 'history' not in st.session_state:
            st.session_state.history = ''
        # the curre
nt question and answer
        value = f'Q: {q} \nA: {answer}'
        st.session_state.history = (
            f'{value
} \n {'-' * 100} \n {st.session_state.history}'
        )
        h = st.session_state.history
        # text area widge
t for the chat history
        st.text_area(label='Chat History', value=h, key='history', height=400)
    
```
---

     
 
all -  [ Please teach me how to get relevant vector store results ](https://www.reddit.com/r/LangChain/comments/191b6is/please_teach_me_how_to_get_relevant_vector_store/) , 2024-01-09-0910
```
Hi, I'm doing an experiment with langchain and chatgpt to see if I can get chatgpt to make business recommendations base
d on keywords provided in the prompt. I am using the following code:

    loader = TextLoader('/tmp/training.txt')
    i
ndex = VectorstoreIndexCreator().from_loaders([loader])
    
    chain = ConversationalRetrievalChain.from_llm(
      ll
m=ChatOpenAI(model='gpt-4'),
      retriever=index.vectorstore.as_retriever(search_kwargs={'k': 10}),
    )

training.tx
t is just a text file with a JSON array e.g.

    [
      {
        'name': 'Some Software Shop',
        'keywords': [ 
'SaaS', 'sales' ],
        'description': '...',
      }
    ]

When I prompt with something like 'What businesses deal 
with SaaS?', it never seems to return the relevant results i.e. those with 'SaaS' in the keywords. Moreover, it seems th
at I always get the same handful of results out of hundreds in the file.

Any thoughts on where I'm going wrong? Thank y
ou.
```
---

     
 
all -  [ How to use Output parser with ConversationalRetrievalQAChain? ](https://www.reddit.com/r/LangChain/comments/191b28p/how_to_use_output_parser_with/) , 2024-01-09-0910
```
How to add ouput parser to ConversationalRetrievalQAChain or ConversationChain?

 I can able to add outputparser to LLMC
hain but it's not working for above conversation chains.  


    Code:

    from langchain.output_parsers import Respons
eSchema, StructuredOutputParser
    from langchain.memory import ConversationBufferMemory
    from langchain.prompts imp
ort PromptTemplate, ChatPromptTemplate, HumanMessagePromptTemplate
    from langchain.chat_models import ChatOpenAI
    
from langchain.chains import LLMChain, ConversationalRetrievalChain
    
    
    checker_tmpl = '''
    # Task Descript
ion:
    As a customer support representative, your role is to provide accurate and helpful responses to customer inquir
ies. Use the provided context to understand the customer's issue and answer their questions directly. Avoid any extraneo
us information or explanations that are not directly relevant to the customer's query.
    
    {format_instructions}
  
  
    
    Chat History:\n\n{history} \n\n
    
    # Given Context:
    {context}
    
    
    
    # Customer's Ques
tion:
    {question}
    
    {human_input}
    
    # Your Response:
    [Please type your answer here, ensuring it is 
concise, relevant, and directly addresses the customer's question based on the given context.]
    
    '''
    
    
  
  checker_response_schemas = [
        ResponseSchema(
            name='requires_customer_support_contact',
           
 description='Indicates whether the user needs to contact customer support. Set to True if the context does not sufficie
ntly address the user's issue and further assistance is needed. Set to False if the provided context is adequate to answ
er the user's query.',
            type='boolean'
        ),
        ResponseSchema(
            name='contextual_answer
',
            description='Provides a direct answer to the user's question, utilizing the given context. The response s
hould be concise, accurate, and specifically tailored to address the query based on the context provided.',
        ),
 
   ]
    
    
    
    
    check_output_parser = StructuredOutputParser.from_response_schemas(checker_response_schemas
)
    
    
    
    
    resume_checker_prompt = ChatPromptTemplate(
        messages=[
            HumanMessagePromptT
emplate.from_template(checker_tmpl)
        ],
        input_variables=['history','question','context'],
        partial
_variables={'format_instructions': check_output_parser.get_format_instructions()}
    )
    
    
    
    memory = Conv
ersationBufferMemory(
        memory_key='history',
        input_key='human_input'
    )
    
    
    
    llm = ChatO
penAI(model_name='gpt-3.5-turbo-1106')
    chat_chain = LLMChain(
        llm=llm,
        prompt=resume_checker_prompt,

        memory = memory
    )
    
    # I wanna use below chain with output parser.
    
    chain = ConversationalRet
rievalChain.from_llm(
        llm=llm,
        memory=memory,
        chain_type='stuff',
        retriever=retriever,
 
       return_source_documents=True,
        get_chat_history=lambda h : h,
        verbose=False ,
        )

&#x200B;
```
---

     
 
all -  [ Summary Generation on large CSV files ](https://www.reddit.com/r/LangChain/comments/19137og/summary_generation_on_large_csv_files/) , 2024-01-09-0910
```
I have a large csv file of about 50mb with a few columns. I would like to summarize the information that I have in this 
file using an LLM. My major concern would be dealing with the context length. Can anyone provide me with any existing im
plementations of this concept or guide me with links which can help me? Thank you.
```
---

     
 
all -  [ Structured data extraction from text using Langchain? ](https://www.reddit.com/r/LangChain/comments/19129gt/structured_data_extraction_from_text_using/) , 2024-01-09-0910
```
I usually work on knowledge graph extraction from text and I've been looking at LLMs for quite some time now. I tried us
ing Langchain for the past few days. However, it seems to be very pleonastic compared to doing the same things myself, e
xcept for the JsonOutputParser part which I've found useful.   
I had however a strange behaviour which probably could b
e answered by someone here: I used Pydantic do describe the schema to be extracted. I need the model to choose one word 
from the list as a vocabulary given the text it is provided, but it always returns the whole list again. I had different
 mistakes when I just sent a single string, but this seems rather odd. Any clue in what might be going on?   


https://
preview.redd.it/in1z5l1sz2bc1.png?width=1496&format=png&auto=webp&s=080d65fa037264f6dbb9173eca4fd9d8578cd42c

&#x200B;
```
---

     
 
all -  [ My first pipeline using Llama7b / llvm / Langchain / EasyOCR / TinyDB ](https://www.reddit.com/r/LocalLLaMA/comments/1910xpv/my_first_pipeline_using_llama7b_llvm_langchain/) , 2024-01-09-0910
```
I am really happy with the result so I feel the urge to share. Hope it matches the community interest.

I started explor
ing self hosted AI for a while now, I had a hard time finding out an architecture that had the following requirement:  

  - Have openai api compatibility, so that I can fallback to using openai if the result were not satisfying  
  - Pipeli
ne the tasks in a data lake fashion   
  - Work on Intel Arc. (I bought 5, 16gb for a total of 1000$ on sale), the full 
machine costed 2000$.


I finally made a dhms, data hoarder management system for my companies accounting, to have an or
ganized filesystem / database to manage all the receipts / invoices I batch scan:  


The architecture:
```
+----------+
     +---------+     +--------------------+     +---------------------+
| Invoices | --> | EasyOCR | --> |       TinyDB 
      | --> | Coherent Filesystem |
+----------+     +---------+     +--------------------+     +---------------------+

                                   ^
                                   |
                                 +------------
--------+
                                 | Langchain Pipeline |
                                 +--------------------
+

```

Langchain:
```markdown
| Langchain Extractor | --> | Llama7b (t=0.8) | --> | Extracted Information | --> | Langc
hain Formatter | --> | Llama7b (t=0.3) |
```

The processing took 4h: 01:12:02 -> 05:19:29 which is insanely fast.

Host
ing costs is part of my office lease.

Next Step: Buy some more gpus; perhaps AMDs for a change; Nvidia beeing too expen
sive. feeding all my daily mails to Llama / Mistral...
```
---

     
 
all -  [ How to use model from hugging face in langchain? ](https://www.reddit.com/r/Langchaindev/comments/191082s/how_to_use_model_from_hugging_face_in_langchain/) , 2024-01-09-0910
```
It is constantly giving me time out error
```
---

     
 
all -  [ Tabular and Graph Output ](https://www.reddit.com/r/LangChain/comments/190sud6/tabular_and_graph_output/) , 2024-01-09-0910
```
Hi Everyone,

I am new to Langchain and been using it to query SQL databases. I want to query a database where the outpu
t I get is in tabular form like how would you query in a mysql workbench. The output should have only the relevant colum
ns and data attributes. Then I have a next requirement to output in a graph form for a graph database.

Can anyone guide
 me or share examples on how to do that?
```
---

     
 
all -  [ Error429(insufficient quota) for new openai account ](https://www.reddit.com/gallery/190r1uz) , 2024-01-09-0910
```
I built a basic LLM. Code & error are in the attached pics. My OpenAI account is new and I used 0 credits until now. But
 it's giving me error 429. There isn't any loop to send multiple requests so I don't get why it's throwing that error
```
---

     
 
all -  [ Real time Arxiv API + RAG at inference ](https://www.reddit.com/r/LocalLLaMA/comments/190qaol/real_time_arxiv_api_rag_at_inference/) , 2024-01-09-0910
```
Hi everyone,

I’m quite new to the space and as a first project, I’m attempting to create an arxiv chat bot. I’m aware t
hat this kind of bot is something that’s been done many times but I haven’t seen anything with the approach. 

Most appr
oaches I came across involves querying the arxiv api and using mainly the abstract as context. My approach involves pars
ing the pdf along with some of its references, chunking it, and using RAG to retrieve the context. Has anyone implement 
anything similar? 

I’m currently doing langchain to do all of this but any suggestions of a better framework would be n
ice!
```
---

     
 
all -  [ Use Langchain or Assistants API? ](https://www.reddit.com/r/OpenAI/comments/190pm6o/use_langchain_or_assistants_api/) , 2024-01-09-0910
```
Hi guys, Iam a total noobie in this field. Sorry if the question sounds dumb.

Iam going to work on a python script whic
h autofills forms using selenium. But the forms will be of different types. Like, new forms will be released in future. 
I want gpt to analyse the html document and find xpath of certain elements like checkbox. 

What I wanted to know is tha
t, should I know langchain or can I do it with assistants api? Iam not even sure if my question is right. Hope someone h
elps. :)
```
---

     
 
all -  [ Is GenAI hype declining or are low-hanging fruits gone? ](https://www.reddit.com/r/OpenAI/comments/190lb0a/is_genai_hype_declining_or_are_lowhanging_fruits/) , 2024-01-09-0910
```
	
Post ChatGPT, there were many interesting papers on the properties and features of large language models. The pace of 
publication was so fast that every week we could see at least 1-2 papers that would make the news.
On the open-source si
de, we had some low quality models and there was so much experimentation to see what works and what doesn't. Soon we got
 llama and llama 2 and a plethora of models to play with. So many projects started around them, many got abandoned short
ly.

Now that I reflect on what happened in 2023, despite all the progress that was made, I feel like the pace of growth
 has decreased. In early 2023 I legit thought 'this is how singularity feels like; every 2-3 days we'll have something n
ew and exciting'.

But now things are more settled. We still get new models every day and Mixtral is still amazing. But 
something seems off. No company (not even Google) was able to make something better than GPT-4. So many Chat UI and wrap
per projects are abandoned (Github can be a scary place...), and we're not much further in our way to understand what th
e heck happens in these models than we were a year ago. In addition, it's become clear that GPT-4-level intelligence mig
ht be the best we can extract from the current LLM technology, and no one takes AGI seriously anymore.

Edit: I should a
dd that Langchain, LlamaIndex and so many other 'frameworks' built around LLMs that used to be all the rage now are evid
ently useless in production. RAG is still RAG, and no matter the tricks you play to make it 'smarter', it's still just R
AG. Langchain and similar frameworks cause more problems than they solve, and the tech debt is horrible. Vector database
s are the same. Most are fighting for that sweet VC money, and their features are essentially the same. So many startups
 suddenly went out of business after OpenAI's first DevDay; so many more will perish after the second DevDay. It's uncle
ar how $$$ VC will be allocated in 2024 given that the safest bet to make money off of AI was and still is OpenAI, not G
oogle, not these third-party frameworks and libraries, not some wrapper around OpenAI's API with a nice UI and shiny web
site.

What do you think about all this?
```
---

     
 
all -  [ Best way to do error handling with langchain? ](https://www.reddit.com/r/LangChain/comments/190k71t/best_way_to_do_error_handling_with_langchain/) , 2024-01-09-0910
```
I have some chains setup, but how do I set it up so, if the json fails to parse, you re-ask the chatbot to correct the e
rrors? and if it does parse, it just goes forward. 

Iv'e read through the docs but found this very difficult. I'm not u
sing agents btw, just regular chains. 
```
---

     
 
all -  [ Apply Model Chat / Instruct Template ](https://www.reddit.com/r/LangChain/comments/190i8ne/apply_model_chat_instruct_template/) , 2024-01-09-0910
```
It is my first-time use LangChain and I have no idea how to apply the chat / instruct template of a model in the prompt 
using Llama-cpp.

For example, tiny-llama uses the following prompt template:

    <|system|>
    {system_message}</s> 

    <|user|>
    {prompt}</s>
    <|assistant|>

And I 'apply' the template using the following runnable chain following
 LangChain doc:

    [
     promptTemplate,
     model.bind({
      stop: ['<|system|>', '<|user|>', '<|assistant|>', '<
/s>'],
     }),
     outputParser
    ]

When I apply invoke the chain, I got the following output:

    [llm/start] [1:
llm:LlamaCpp] Entering LLM run with input: {
      'prompts': [
        '<|system|>\nYou are a helpful AI assistant that
 provides information based on your knowledge without any creation of unknown information.\nIf you do not know the answe
r to a question, you must say \'I don't know\'.</s>\n<|user|>\nSystem Context:\n\nyour name is John\n\nAre you Amy?</s>\
n<|assistant|>Response:'
      ]
    }

I have no idea if I have applied the template correctly, because of the 'prompts
' key feels like there is another place for providing the system info.

Are there any missing steps I have to perform be
fore passing it into the invoke function? Do I mix up the meaning of 'prompt template'? Any help in any languages is hig
hly appreciated.
```
---

     
 
all -  [ How to connect llms with custom functions and database. ](https://www.reddit.com/r/LLMDevs/comments/190hyn5/how_to_connect_llms_with_custom_functions_and/) , 2024-01-09-0910
```
I have gone through langchain, while using gpt, but i want to use falcon model (not mandatory ) since it’s opens source,
 so the idea is that the model will chat with user and with the given user prompt the model will also give him info abou
t the database, like mongodb, and also if we can build a custom functions which the model can call automatically based o
n its knowledge. Lets say if i ask llms that, i want to get a “hello world written “ so the model understands its and ca
lls “def hello(): 
Hope I explained it well.
```
---

     
 
all -  [ Need feedback ](https://www.reddit.com/r/resumes/comments/190eyzj/need_feedback/) , 2024-01-09-0910
```
Would love some criticism of my resume. I polished it up over the past week. Im currently seeking fulltime employment fo
r entry level data roles but haven't been able to land any calls yet :(. Would love any form of feedback. Thanks!

[Woul
d love some criticism of my resume. I polished it up over the past week. I'm currently seeking full-time employment for 
entry-level data roles but haven't been able to land any calls yet :\(. Would love any form of feedback. Thanks!s!!](htt
ps://preview.redd.it/9k70zhehywac1.png?width=940&format=png&auto=webp&s=6a9868ef8e3af6274785df82ac4f9dc45440d312)
```
---

     
 
all -  [ How can I run my python script when I start my NextJS app ](https://www.reddit.com/r/nextjs/comments/1909h6l/how_can_i_run_my_python_script_when_i_start_my/) , 2024-01-09-0910
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

     
 
all -  [ Automating prompt writing & LLM evaluation ](https://www.reddit.com/r/LangChain/comments/19051ef/automating_prompt_writing_llm_evaluation/) , 2024-01-09-0910
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

     
 
all -  [ Is it possible to fine tuning a model to improve RAG queries ? ](https://www.reddit.com/r/LocalLLaMA/comments/1901ttm/is_it_possible_to_fine_tuning_a_model_to_improve/) , 2024-01-09-0910
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

     
 
all -  [ End of Week Report DevolvedAI ](https://www.reddit.com/r/DevolvedAI/comments/18zykt5/end_of_week_report_devolvedai/) , 2024-01-09-0910
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

     
 
all -  [ 🔥 [HIRE] ChatGPT, Langchain, Generative AI, , Prompt Engineering ](https://www.reddit.com/r/ForHire_AI/comments/18zxgcq/hire_chatgpt_langchain_generative_ai_prompt/) , 2024-01-09-0910
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

     
 
all -  [ Chat model for 'any codebase' ](https://www.reddit.com/r/u_waynerad/comments/18zptpm/chat_model_for_any_codebase/) , 2024-01-09-0910
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

     
 
all -  [ Book rewrite with large context window ](https://www.reddit.com/r/LangChain/comments/18zpl3w/book_rewrite_with_large_context_window/) , 2024-01-09-0910
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

     
 
all -  [ [P] An open-source project for deploying local models ](https://www.reddit.com/r/MachineLearning/comments/18zkm5m/p_an_opensource_project_for_deploying_local_models/) , 2024-01-09-0910
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

     
 
all -  [ End-to-end observability for LangChain script ](https://www.reddit.com/r/LangChain/comments/18z5pch/endtoend_observability_for_langchain_script/) , 2024-01-09-0910
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

     
 
all -  [ RAG Vs. Batch Processing in Large Document Summarization ](https://www.reddit.com/r/LangChain/comments/18z51mu/rag_vs_batch_processing_in_large_document/) , 2024-01-09-0910
```
Let's say I have a CSV file with 100,000 comments related to a product. I would like to summarize all the comments and p
rovide some recommendations on how to improve the product.   


What is the best way to summarize this? Using RAG or chu
nking and feeding the entire list of comments to the LLM to process?
```
---

     
 
all -  [ Not even a single interview call for internships in Data ](https://i.redd.it/61ayw0oqwkac1.png) , 2024-01-09-0910
```
Do I need to add more projects and remove my achievements to get more key word matched . I have applied to around 300 jo
bs in past 4 month and haven't got a single call for internship in data related.
```
---

     
 
all -  [ ChromaDB or any vector database for mobile devices ](https://www.reddit.com/r/LangChain/comments/18yxpdg/chromadb_or_any_vector_database_for_mobile_devices/) , 2024-01-09-0910
```
While it is easy to create streamlit/hosted apps using vector databases; i am looking to create a solution which ensures
 that user data \[including vector database information\] never leaves user device, leading to utmost privacy \[unless s
earch results for a RAG solution are sent to an LLM\]

&#x200B;

Anyone has had luck running chromaDB on mobile ? or any
 other vector databases that would work accordingly ? 
```
---

     
 
all -  [ Extracting data from pdf containing complex tables ](https://www.reddit.com/r/LangChain/comments/18yxacm/extracting_data_from_pdf_containing_complex_tables/) , 2024-01-09-0910
```
Is there any library or any way which helps in extracting pdf containing complex tables data and store , and how can we 
chunk that pdf data such that table data preserves in vector db ? Assuming each pdf contains around 5-10 pages
```
---

     
 
all -  [ How do you test and manage use cases based on the langchain framework? ](https://www.reddit.com/r/LangChain/comments/18yws8j/how_do_you_test_and_manage_use_cases_based_on_the/) , 2024-01-09-0910
```
I have been developing based on langchain for a period of time recently, and later I came into contact with the service 
langsmith provided by it. The overall feeling is that the trace capability is quite powerful, but the test set managemen
t is not convenient to use. What did you use during the testing process? Test methods or dataset management tools.
```
---

     
 
MachineLearning -  [ [Project] Temporal Augmented Retrieval (TAR) - Dynamic RAG ](https://www.reddit.com/r/MachineLearning/comments/18uddmj/project_temporal_augmented_retrieval_tar_dynamic/) , 2024-01-09-0910
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

     
 
MachineLearning -  [ [R][P] Autogen + Langchain Tools + Local LLM doesn't work. ](https://www.reddit.com/r/MachineLearning/comments/18tex1j/rp_autogen_langchain_tools_local_llm_doesnt_work/) , 2024-01-09-0910
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

     
 
MachineLearning -  [ [P] Seeking Advice for Building a School Handbook Chatbot Using OpenAI and Vector Databases ](https://www.reddit.com/r/MachineLearning/comments/18rndcp/p_seeking_advice_for_building_a_school_handbook/) , 2024-01-09-0910
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

     
 
deeplearning -  [ Unlocking the Power of Language: How LangChain Transforms Data Analysis and More ](https://www.reddit.com/r/deeplearning/comments/18l788y/unlocking_the_power_of_language_how_langchain/) , 2024-01-09-0910
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

     
 
deeplearning -  [ [D] Mastering Chain Composition with LangChain Expression Language (LCEL) ](https://www.reddit.com/r/deeplearning/comments/18i0wot/d_mastering_chain_composition_with_langchain/) , 2024-01-09-0910
```
In the intricate landscape of modern software development, orchestrating complex sequences of actions seamlessly poses a
 significant challenge. Enter LangChain Expression Language (LCEL), a groundbreaking declarative approach designed to re
volutionize the composition of chains within software architecture.

Link: [https://medium.com/ai-artistry/mastering-cha
in-composition-with-langchain-expression-language-lcel-2d5041fb0cbd](https://medium.com/ai-artistry/mastering-chain-comp
osition-with-langchain-expression-language-lcel-2d5041fb0cbd)  
```
---

     
