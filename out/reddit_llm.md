 
all -  [ Please help with this ](https://www.reddit.com/r/LangChain/comments/18xydx7/please_help_with_this/) , 2024-01-04-0910
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

     
 
all -  [ LCEL with Streamlit fails to include memory in conversations. ](https://www.reddit.com/r/LangChain/comments/18xu7jd/lcel_with_streamlit_fails_to_include_memory_in/) , 2024-01-04-0910
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

     
 
all -  [ LangChain's 1st Module: Model I/O 🤖 ](https://dev.to/jaydeepb21/1st-module-model-io-4b6a) , 2024-01-04-0910
```

```
---

     
 
all -  [ RAG for Pdf with tables ](https://www.reddit.com/r/LangChain/comments/18xp9xi/rag_for_pdf_with_tables/) , 2024-01-04-0910
```
I want to built a RAG system for science documents which contains the theory texts along withn equations, tables, and la
belled diagrams. Questions can be from understanding of theory, equations and information about tables. How should I pro
ceed? Have idea of building a naive rag system only. 
Any resources will be helpful.
```
---

     
 
all -  [ Deploy Langchain-Streamlit App to EXE-File ](https://www.reddit.com/r/LangChain/comments/18xlzmg/deploy_langchainstreamlit_app_to_exefile/) , 2024-01-04-0910
```
Hi,

I have built a RAG app with Langchain and Streamlit and now want to share it with my team. As I am dealing with con
fidential data, I don't want to use a cloud solution, so my idea was to convert the Ap to an .EXE-File, so that they can
 load and use it with no programming expertise. I saw this tutorial, but it is not working for me. 

Does anyone have a 
good resource for this?
```
---

     
 
all -  [ Difference between Answer and Observation? ](https://www.reddit.com/r/LangChain/comments/18xjizi/difference_between_answer_and_observation/) , 2024-01-04-0910
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

     
 
all -  [ Hevolve : A production app using Langchain ](https://www.reddit.com/r/LangChain/comments/18xjflb/hevolve_a_production_app_using_langchain/) , 2024-01-04-0910
```

https://play.google.com/store/apps/details?id=com.hertzai.hevolve

Latency ~5 seconds coz of RAG, chains and tools but 
fully context aware coz of the same reason.

Microsoft copilot with an AI Avatar which can talk to you in 10 languages
```
---

     
 
all -  [ VectorStore.addDocuments - do not add duplicates ](https://www.reddit.com/r/LangChain/comments/18xidx1/vectorstoreadddocuments_do_not_add_duplicates/) , 2024-01-04-0910
```
I am using langchain VectorStore (currently QDrant and plain to use OpenSearch in future). 

It works fine, but I have i
ssues. If I run addDocument for the same doc twice - I have two copies of the doc in store. 

Of course I can search for
 doc with a give is in qdrant before adding it (transactions?). But I wonder if there is standard way to ensure uniquene
ss? 
```
---

     
 
all -  [ Integrating Azure CosmosDB as vectorstore for RetrievalQA? ](https://www.reddit.com/r/LangChain/comments/18xhjnu/integrating_azure_cosmosdb_as_vectorstore_for/) , 2024-01-04-0910
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

     
 
all -  [ Where to host RAG app? ](https://www.reddit.com/r/LangChain/comments/18xe8di/where_to_host_rag_app/) , 2024-01-04-0910
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

     
 
all -  [ Anyone experiencing slow OpenAI responses/completions? ](https://www.reddit.com/r/LangChain/comments/18xbb2u/anyone_experiencing_slow_openai/) , 2024-01-04-0910
```
I was trying out some LCEL chains on Jupyter Notebook, and all of a sudden, I realized that now my chat completions are 
taking four times longer than they were yesterday.

&#x200B;

https://preview.redd.it/4ac8dgews5ac1.png?width=737&format
=png&auto=webp&s=84d5115a4d74a73779b9a2deb4f2c12ffd5ffad1
```
---

     
 
all -  [ *kwargs in Agents ](https://www.reddit.com/r/LangChain/comments/18x4w1f/kwargs_in_agents/) , 2024-01-04-0910
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

     
 
all -  [ Struggling understanding conversational-chat-agent and prompt template ](https://www.reddit.com/r/LangChain/comments/18x356k/struggling_understanding_conversationalchatagent/) , 2024-01-04-0910
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

     
 
all -  [ Rag Demo - Cheapest way to host ](https://www.reddit.com/r/LangChain/comments/18wzh73/rag_demo_cheapest_way_to_host/) , 2024-01-04-0910
```
Hi,

i have built a RAG app with Langchain locally. Now I want to host it in the cloud for a little demo showcase (less 
than 5 users), so that others can try out how well it is working. 

What would be a cheap and efficient way to host a La
ngchain App in the cloud?

Fyi: I have used a quantized Mixtral 8x7b model (less rhan 30GB RAM required). Alternatively 
I can switch to smaller models like a quantized Mistral 7B model.
```
---

     
 
all -  [ If you want to add AI superpowers to your C# app... ](https://www.reddit.com/r/dotnet/comments/18wygc5/if_you_want_to_add_ai_superpowers_to_your_c_app/) , 2024-01-04-0910
```
I've been working with C# for many, many years now... More recently, I've been testing and writing about AI tools and da
ta frameworks like LangChain and LamaIndex that make it easier for me to add AI capabilities to my apps.

After some tes
ting and a bunch of articles, I found that the Semantic Kernel SDK from Microsoft is the ideal solution for C# devs like
 me since it's part of the framework and can easily consume existing C# functions with few (if any) modifications.

Here
's what I build using Semantic Kernel:

* Three prompt plugins
   * One that generates a common myth about AI using Open
AI's GPT
   * One that fact-checks it
   * One that adjusts the generated output to match a social media posting best pr
actices
* One native function
   * Simulates posting to social media

[I wrote an easy-to-follow step-by-step Semantic K
ernel tutorial](https://www.gettingstarted.ai/using-semantic-kernel-add-ai-capabilities-to-csharp-app-microsoft-part-1/)
. Please share your feedback and leave a comment below if you have any questions. Happy to help!

Cheers 🥂
```
---

     
 
all -  [ Calling API doesn't work when using Langchain ](https://www.reddit.com/r/LangChain/comments/18wxfd2/calling_api_doesnt_work_when_using_langchain/) , 2024-01-04-0910
```
When I use Postman to query the Hubspot endpoint: [https://api.hubapi.com/crm/v3/properties/contacts](https://api.hubapi
.com/crm/v3/properties/contacts) using the authorisation below (where X is of course the censored token):

     headers 
= {
      'Authorization': 'Bearer X'
    }

I get a working API response.

However, when I try to pass the above as par
t of natural language instructions to Langchain's API Chain (see code below), authentication fails.

    HubSpotDocs =  
'''
    
    The below is Hubspot API documentation showing how to create a contact. 
    
    The endpoint is: 
    
  
  'https://api.hubapi.com/crm/v3/properties/contacts'. 
    
    ///Example request body to create a new contact
    {
 
     'properties': {
        'email': 'example@hubspot.com',
        'firstname': 'Jane',
        'lastname': 'Doe',
   
     'phone': '(555) 555-5555',
        'company': 'HubSpot',
        'website': 'hubspot.com',
        'lifecyclestage'
: 'marketingqualifiedlead'
      }
    }
    
    Use the below authorisation:
    
    headers = {
      'Authorization
': 'Bearer X'
    }
    
    '''
    
    
    llm = ChatOpenAI(temperature=0, model= 'gpt-3.5-turbo-1106', openai_api_k
ey='Y')
    
    Test = APIChain.from_llm_and_api_docs(llm, HubSpotDocs,limit_to_domains=None, verbose=True)
    
    Te
st.run('Create a new contact named Sara with email sara@google.com. She resides in Toronto.')

The LLM responds with:

 
   > Entering new APIChain chain...
    https://api.hubapi.com/crm/v3/properties/contacts?properties={'email':'sara@goog
le.com','firstname':'Sara','city':'Toronto'}
    {'status':'error','message':'Authentication credentials not found. This
 API supports OAuth 2.0 authentication and you can find more details at https://developers.hubspot.com/docs/methods/auth
/oauth-overview','correlationId':'3a41a5c5-dbe9-4b19-8cc6-d6293290a52b','category':'INVALID_AUTHENTICATION'}
    
    > 
Finished chain.

Clearly, the LLM is understanding the ask correctly as it maps e.g. 'Toronto' to city. However, the aut
horisation is failing (even though it works in Postman). This means that the issue isn't the authentication but more so 
the way Langchain/the LLM interprets (then passes to Hubspot) authorisation. How can I fix this? I am facing a similar i
ssue with attempting to call the Google Calendar API using APIChain method/natural language.
```
---

     
 
all -  [ Advice for MBA after engineering and a trashy job ](https://www.reddit.com/r/Indian_Academia/comments/18wvt3h/advice_for_mba_after_engineering_and_a_trashy_job/) , 2024-01-04-0910
```
Hi, I am a 23yo female SDE. My qualifications, Bachelors in CSE graduated in 2022. 
In 2021 joined a decent company as a
n intern in AI/ML department. In the name of AI we were made to annotate data but because we had a few data scientists i
n the team and I thought we would get to learn from them in the future I continued there. Also there were not many compa
nies for AIML roles during our placement drive and I didn’t care to look out for internships off campus ( big mistake ig
), I was quite laid back because of covid. 

So after my internship I got PPO and stayed in the company, worked on Named
 Entity Recognition, fixing bugs of existing product, making APIs, document parsing, using OpenAI API in our existing pr
oduct, Langchain, prompt writing. 

But I feel like my tech stack sucks, feel kya that is true. Most profiles for Python
 related roles require AWS, Azure, Frontend and what not. I have no experience in this plus I don’t like backend develop
ement. So I thought of learning new skills and finding new roles. 

*dramatic music*
Thanks to OpenAi our company decide
d to dissolve AIML team in October23, all the senior roles were sacked and juniors (like me) were moved to other teams. 
My current team works with Django, and I am supposed to do core backend dev work now,I’m struggling for life fr. 

And t
here’s more, so the annual review got messed up by my current manager because she didn’t get my previous manager’s  inpu
t and gave me an extremely bad review which has made me feel worthless and depressed because all the work I had done til
l October was not considered. I had led a project that was internally used by many other teams of our company and it was
 praised a lot. 

So now I’m anxious and depressed, working for a company that I hate, with an awful team manager who di
dn’t even provide KTs. I’m looking for new roles but the market sucks. I want to get into business analytics, I have som
e experience with data science during college but I have zero business knowledge. Thinking of doing MBA in Business Anal
ytics from a private university in Punjab (under 10 lakh fee). But yaar yeh top b schools vagerah na jaane ka fomo hogya
 toh? 
Bhai, zindagi jhand hogayi soch soch ke, ho kuch nahi raha merese.

Also I don’t want to spend 20-30 lakh on mba,
 I think it’s not worth it, especially in my case. Loan kaun lega yaar and I don’t want to add financial burden on my fa
mily. Also waiting another year to prepare for CAT, appear for it, results, interviews. And I don’t think I can sustain 
my current job for long with how I’ve been feeling, I have no motivation and all I do is overthink and get anxious. 
```
---

     
 
all -  [ Trening tools ](https://www.reddit.com/r/LangChain/comments/18wtxcy/trening_tools/) , 2024-01-04-0910
```
What are some of the trending tools that companies are looking for in the interns in the field of AI?
```
---

     
 
all -  [ In your experience for which usecases is LangChain better and for which LlamaIndex ](https://www.reddit.com/r/LangChain/comments/18wooh1/in_your_experience_for_which_usecases_is/) , 2024-01-04-0910
```
Learning about this quite extensively for over a month. Have always known that Llamaindex also exist and has the same pu
rpose. 

In which usecases or tools has Llamaindex been better or and vice versa for LangChain
```
---

     
 
all -  [ How to attain a NL -> SQL to extract data. ](https://www.reddit.com/r/developersIndia/comments/18wmhv5/how_to_attain_a_nl_sql_to_extract_data/) , 2024-01-04-0910
```
 An interface where the user puts up a query for the database. The AI will then ask some questions (if needed) to ensure
 that the user is on the same page. Afterward, it will convert the natural language into an SQL query, which can be appl
ied to the database to extract the desired result. 

I'm not in touch with the AI field, and I have no idea how to do th
is. Please guide me through the process. I've researched llama index and langchain, but I didn't get a clear idea about 
this. 
```
---

     
 
all -  [ ChatGoogleGenerativeAI not considering history, when asked to predict unlike openAI using langchain  ](https://www.reddit.com/r/LangChain/comments/18wgxvt/chatgooglegenerativeai_not_considering_history/) , 2024-01-04-0910
```
I'm using langchains conversation for creating a chatbot and this is the prompt its generated after few convos

    The 
following is a friendly conversation between a human and an AI. The AI is talkative and provides lots of specific detail
s from its context. If the AI does not know the answer to a question, it truthfully says it does not know.
    
    Curr
ent conversation:
    Human: Hi, my name is Andrew
    AI: Hello Andrew, it's nice to meet you. My name is Bard, and I'm
 an AI chatbot. I'm still under development, but I'm learning more every day. I'm happy to chat with you about anything 
you like. What would you like to talk about?
    Human: What is 1+1?
    AI: 1 + 1 is 2.
    Human: What is my name?
   
 AI: I do not have access to your personal information, so I cannot answer that question.
    Human: What is my name?
  
  AI: I do not have access to your personal information, so I cannot answer that question.
    Human: Hi, i need to go g
rocery shopping tomorrow
    AI: That's great! Grocery shopping can be a fun and rewarding experience. What kind of groc
eries do you need to buy?
    Human: What is 1+1?
    AI: 1 + 1 is 2.
    Human: when do i need to go grocery shopping?

    AI: 'You did not specify when you need to go grocery shopping.'

OpenAI answers the question correctly, but gemini i
sin't using the history. Do langchain prompts works for openai only and I need to change it or is something else worng.


    llm = ChatGoogleGenerativeAI(model='gemini-pro', temperature=0)
    memory = ConversationBufferMemory()
    convers
ation = ConversationChain(
        llm=llm, 
        memory = memory,
        verbose=True
    )

&#x200B;
```
---

     
 
all -  [ Revolucionando el Web Scraping con IA ](https://www.reddit.com/r/LangChain/comments/18w2ms9/revolucionando_el_web_scraping_con_ia/) , 2024-01-04-0910
```
Todos sabemos lo '**tedioso**' que es hacer web scrapping, entender la estructura de un sitio web para que nuestro códig
o pueda obtener resultados, estar en constante mantenimiento por si el sitio web cambia su estructura o si agregan funci
onalidad con java script para cargar dinámicamente la información. Pero **¿Que pasaría si hubiera una manera de converti
r este 'tedioso' proceso en uno muy sencillo, adaptable a cualquier estructura?**

por ejemplo:

&#x200B;

https://previ
ew.redd.it/mmfiq0b8dv9c1.png?width=2232&format=png&auto=webp&s=377d8ff89ed3c0b16713a0c2f2dd742e27f5f9fa

&#x200B;

https
://preview.redd.it/g8rvpedadv9c1.png?width=1488&format=png&auto=webp&s=232b1858d1a70ffdff9d470dbfe279cc84e9bd86

Le asig
namos la tarea a la IA que se adapte a cualquier estructura de cualquier sitio web y obtenga resultados orgánicos de cal
idad.

&#x200B;

https://preview.redd.it/s0jp125hdv9c1.png?width=1189&format=png&auto=webp&s=2b59846330b114b9cf1b3aa0763
024999a7d6dc9

Pueden leer el artículo completo en el siguiente enlace:Link: [https://es.linkedin.com/pulse/revolucionan
do-el-web-scraping-con-ia-jean-pierre-alvarez-8gmge?trk=public\_post\_feed-article-content](https://es.linkedin.com/puls
e/revolucionando-el-web-scraping-con-ia-jean-pierre-alvarez-8gmge?trk=public_post_feed-article-content)

&#x200B;
```
---

     
 
all -  [ What are must have developer tools to build generative ai apps? ](https://www.reddit.com/r/ChatGPTCoding/comments/18vvqo2/what_are_must_have_developer_tools_to_build/) , 2024-01-04-0910
```
I have built multiple automations using gpt, midjourney, etc. Now looking to create a more organized version of these to
ols, what tools should I explore?

Edit: I see the question was quite open ended, let me add the tools that I have used 
and then you can add your recommendations

* Langchain (I use it only for few projects)
* OpenAI API
* 11labs api
* Redi
s (I use it for caching)
* node.js and express.js (all my projects are built as npm library with a cli that spins up exp
ress server to create http service on top of library)
* mocha and chai for testing, I run those tests on each PR with Gi
tHub actions, I use an spare openai account just for testing
* FluxNinja Aperture for rate limiting
* Your recommemdatio
ns (any small/big addition that can save time and headache in the future)
```
---

     
 
all -  [ Extremely fast response LLM interface and architect. ](https://www.reddit.com/r/LLMDevs/comments/18vrxx3/extremely_fast_response_llm_interface_and/) , 2024-01-04-0910
```

Hi all, I’m new to the technology and I’m looking to build a LLm api. Would like to seek advice to improve on the respo
nse speed. 

Problem statement:

I am working to build a chat feature for a manufacturing repair line to guide workers o
n how to fix various issue. The product changes hourly and so does the solution to fix it. The boss is very good coming 
out with solution but is way too busy to explain or teach his 38 repair man. His goal is to create a ML chat bot to do t
he reply where he will update the database with all sort of solution and when his repair man query the chat bot to searc
h for the best answer. He knows he will need the ML chat bot because:

1. Everyone ask a question differently. 
2. He ca
n add more solutions and does not need to repeat himself.

The chat bot must achieve a few critical requirement from my 
crazy boss. 

1. Each response must be below 1 sec. (Includes multiple prompt)
2. No simulating of a quick reply. He wan
ts the entire sentences to be out under 1sec. 
3.Must have a database query where he can upload a list of his solution. 

4. Must have memory but does not need to saved to a database
5. Answers should be short and easy. 
6. Don’t ask him to 
just let his employee search the database. He wants to move forward in the llm space. Not backwards. 
7. On-premise or o
n cloud doesn’t matter. (Prototype first before and funds)

The solution is usually short.
 
Example, “use a size 8 wenc
h with a bottom power up approach. Control the strength applied”

However the below 1 sec requirement is just crazy! Her
e is my build:

Langchain interface (quantization)
Llama-2-7b-chat-hf
Bitsnbytes: 4bit, nf4, double quant, torch.bfloat1
6

FAISS for memory caching
Sentence-transformers/all-mpney-base-v2
Langchain.memory conversationBufferMemory

vector da
tabase for storage of solution
Langchain vector store qdrant

Running on 3080 gpu

Prompt template.  


Total response t
ime taken per query: 1min

Can anyone provide any better solution to improve the speed?
I’m thinking of using vllm inste
ad to improve on the response speed. But I don’t think I can achieve 1sec. 

 Please help before I get fired.
```
---

     
 
all -  [ Finetuning code generation model on our own repositories ](https://www.reddit.com/r/LocalLLaMA/comments/18v80cn/finetuning_code_generation_model_on_our_own/) , 2024-01-04-0910
```
Hello,

I'm working on a code generation system for my personal usage. I've had some success with a RAG system using lan
gchain to add similar snippets as context, concatenate them and pass as prompt to a code Llama endpoint. My next step wo
uld be to finetune the model on my own code base.

I've seen several tutorials with axolotl on a text-to-SQL generation 
dataset, or on some prompt answering dataset, but I haven't seen anything like finetuning the model on multiple user-own
ed repos.

This surprises as I would have thought this was the next logical step to improve accuracy. Am I mistaken ? Is
 the knowledge added by finetuning already present in the context ? Is the performance gain not worth the hassle ?

Did 
somebody already tried this and has some feedback ?

Thanks a lot

&#x200B;

 
```
---

     
 
all -  [ Anyone done some webscraping using LangChain can guide me? ](https://www.reddit.com/r/LangChain/comments/18v6lqb/anyone_done_some_webscraping_using_langchain_can/) , 2024-01-04-0910
```
Hi so here is what I want langchain to do. 

Go to a website, submit some text in the text\_search bar

wait for the sea
rch result to load, fetch some of the contents of the search back
```
---

     
 
all -  [ CrewAI agent framework with local models ](https://github.com/joaomdmoura/crewAI) , 2024-01-04-0910
```
This is great news for everyone who wants to develop agentic software. After a lot of failure and disappointments with r
unning Autogen with local models, I tried the rising star of agent frameworks, CrewAI. It is a multi-agent framework bas
ed on LangChain and utilities LangChain's recently added support for Ollama's JSON mode for reliable function calling. T
he developer treats local models as first class citizens.

I tried the [stock analysis](https://github.com/joaomdmoura/c
rewAI-examples/tree/main/stock_analysis) example code where the agents use a wide range of tools including google search
es and subsequently summarizing the top results, storing them in a vector database and generating analysis based on the 
findings. I tried it with Mistral 7B instruct 0.2 via Ollama on my MacBook Pro M1 16 GB laptop. It took the three agents
 15-20 min to perform all the research, RAG, and analysis to come up with a reasonable report. Very cool.
```
---

     
 
all -  [ Is anyone actually using Langchain in production? ](https://www.reddit.com/r/LocalLLaMA/comments/18v0sxq/is_anyone_actually_using_langchain_in_production/) , 2024-01-04-0910
```
Langchain seems pretty messed up.

\- The documentation is subpar compared to what one can expect from a tool that can b
e used in production. I tried searching for what's the difference between chain and agent without getting a clear answer
 to it.

\- The dis-cord community is pretty inactive honestly so many unclosed queries still in the chat.

\- There are
 so many ways of creating, for instance, an agent. and the document fails to provide a structured approach to incrementa
lly introducing these different methods.

So are people/companies actually using langchain in their products?
```
---

     
 
all -  [ Is anyone actually using Langchain in production? ](https://www.reddit.com/r/LangChain/comments/18v0s3k/is_anyone_actually_using_langchain_in_production/) , 2024-01-04-0910
```
Langchain seems pretty messed up. 

\- The documentation is subpar compared to what one can expect from a tool that can 
be used in production. I tried searching for what's the difference between chain and agent without getting a clear answe
r to it. 

\- The discord community is pretty inactive honestly so many unclosed queries still in the chat.

\- There ar
e so many ways of creating, for instance, an agent. and the document fails to provide a structured approach to increment
ally introducing these different methods.

&#x200B;

So are people/companies actually using langchain in their products?

```
---

     
 
all -  [ Any alternatives to Langchain's webpdfloader? ](https://www.reddit.com/r/LangChain/comments/18uwc21/any_alternatives_to_langchains_webpdfloader/) , 2024-01-04-0910
```
I'm trying to just load a pdf from a URL. I'm confused how to do so using the [webPDFLoader](https://js.langchain.com/do
cs/integrations/document_loaders/web_loaders/pdf). If anyone has a bit of time, please help explain how to implement thi
s? I would appreciate any help pls.

I'm doing this in nextjs. Where in the webPDFloader section do I put the pdfUrl var
iable?

    'use client';
    import React, { useEffect } from 'react';
    import { WebPDFLoader } from 'langchain/docu
ment_loaders/web/pdf';
    import { guestPdfId } from '@/components/Hero';
    import { Document } from 'react-pdf';
   
 
    
    
    const bucketId = process.env.NEXT_PUBLIC_APPWRITE_BUCKET_ID!;
    const fileId = guestPdfId;
    const p
rojectId = process.env.NEXT_PUBLIC_APPWRITE_PROJECT_ID!;
    
    const pdfUrl = `https://cloud.appwrite.io/v1/storage/b
uckets/${bucketId}/files/${fileId}/view?project=${projectId}&mode=admin`;
    
    // webPDFLoader
    const blob = new 
Blob(); // e.g. from a file input
    
    const loader = new WebPDFLoader(blob, {
      // you may need to add `.then(m
 => m.default)` to the end of the import
      pdfjs: () => import('pdfjs-dist/legacy/build/pdf.js'),
    });
    
    d
ocs = loader.load()
    
    const docLen = docs.length()
    
    const ProcessPdf = () => {
    
      return <div>
  
      <button onClick={doclen}>Show PDF</button>
    </div>;
    };
    
    export default ProcessPdf;
    

&#x200B;
```
---

     
 
all -  [ How Langchain or Llama Index stack against “native” RAG solutions? ](https://www.reddit.com/r/LangChain/comments/18uojpr/how_langchain_or_llama_index_stack_against_native/) , 2024-01-04-0910
```
I am new to the topic, and I want to build an assistant chatbot that can reference data from websites and docs. This can
 be achieved with OpenAI plugins and Cohere RAG connectors, just like using a framework like langchain. How do they comp
are?
```
---

     
 
all -  [ How can I keep my outputs consistent ](https://www.reddit.com/r/LangChain/comments/18unseb/how_can_i_keep_my_outputs_consistent/) , 2024-01-04-0910
```
I am working on one of my clients project where the user will pass the drug name and url of a pdf , from that pdf we nee
d to extract some fields , though chunk size kept is 2200 model is gpt-4-32k I see inconsistent results , how can I make
 results more consistent
```
---

     
 
all -  [ Wrote a small article on what I'll be learning in 2024. What are you guys planning to learn? ](https://www.reddit.com/r/developersIndia/comments/18ul6fa/wrote_a_small_article_on_what_ill_be_learning_in/) , 2024-01-04-0910
```
[Link to the article](https://dev.to/wannabee/discovering-new-tech-in-2024-what-ill-learn-3o0o)

&#x200B;

https://previ
ew.redd.it/ends614ezg9c1.png?width=2358&format=png&auto=webp&s=d711d072761a6b065ab2791d7cc5cc5fba8dab10
```
---

     
 
all -  [ Some help with feelings? ](https://www.reddit.com/r/LocalLLaMA/comments/18uiypc/some_help_with_feelings/) , 2024-01-04-0910
```
Hey, I'm kind of stuck here. Maybe you could help me out.
Still time for the one promised good deed this year ;) 
I'm tr
ying to make a voiced chatbot with a frontend, that reveals a smile or sorrow etc. based on the sentence it speaks.
I tr
ied different models, but none seem to obey my instruction for a complete chat session. 
The first idea was to return JS
ON in the following structure:

{
'feeling':'Joy',
'answer':'Hey!',
'code':'In case there is code to display. The bot sh
ouldn't read it'
}

But I got rid of that. Even though I told the llm to not explain the JSON or not to continue the con
versation it did sometimes.

Then I just moved on to something more simple. I told the llm to start every sentence with 
the feeling enclosed in 3 asterix like (which reddit turns into cursive words..):

***Joy*** Hey there! ***Neutral*** Ho
w can I help you? 

But still the same problems. After a while the instruction is simply ommited, it continues the conve
rstation without the user, or even worse it adds the history to the response.

The instruction to write with those feeli
ngs was included in the system prompt every time and some dummy conversation messages were included in the history. 

Mo
st tries were made with lmstudio and Mistral7bInstruct0.2. I also tried openchat, phi2 and dolphin-mixtral but i can't g
et the output to stay consistent. 

At this point I'd really appreciate any input. :)

Should I include some kind of fai
lsafe, that checks the response and remind the llm to respond correctly like langchain does it?
```
---

     
 
all -  [ [For Hire] Programmer/Web Developer/IT Consultant (Python, PHP, AI, etc.) ](https://www.reddit.com/r/forhire/comments/18ugr69/for_hire_programmerweb_developerit_consultant/) , 2024-01-04-0910
```
To get in contact, please **message** me, I **don't** use the chat thing and might miss you or reply very late. Then we 
can switch to email/discord/telegram or whatever else. Apologies for starting with this, but many missed it when it was 
lower.

I'm a programmer/web developer with 13 years of professional experience. I am available for all sorts of program
ming and web development tasks.

I also offer consulting services. If you need something done, but don't know how exactl
y, I can help. I'm an excellent researcher and I communicate well. I will work with you to find the best solution for yo
ur problem.

My services include, but are not limited to:

* websites

* desktop applications

* AI integration (chatGPT
 API, langchain, whatever else turns up)

* integration with APIs and other webservices

* all kinds of scripts

* task 
automation

* website optimization

* debugging

* plugins for existing software

* bots (Reddit, Telegram, etc)

If you
're looking for someone to take care of a variety of different tasks, I can offer continuous support.

My preferred envi
ronment is Python with Django, but I work with anything Python or PHP based. I have no problem with learning new technol
ogies that are needed for the project.

Rate is $50/h. Can also do fixed price by project, but only if the project/miles
tone is well-defined.

Satisfied customers:

https://www.reddit.com/r/testimonials/comments/2e8gqy/pos_uqui_need_a_backe
nd_web_dev_look_no_further/

https://www.reddit.com/r/testimonials/comments/7fsdze/pos_hiring_uqui_was_an_example_of_how
_it_should/

https://www.reddit.com/r/testimonials/comments/80pu9l/pos_uqui_great_work_detailed_and_fast/

https://www.r
eddit.com/r/testimonials/comments/b0nx68/uqui_is_a_hardworking_intelligent_honest_apps/

https://www.reddit.com/r/testim
onials/comments/j3mz3p/uqui_is_a_great_web_development_consultant_with/

https://www.reddit.com/r/testimonials/comments/
v40ay3/pos_uqui_is_a_great_backend_dev_to_work_with/

Some examples of sites I worked on: http://bdabkowski.yum.pl/

Ple
ase note: I am **not** a designer. To make it clear, it means zero aesthetic sense.
```
---

     
 
all -  [ [Project] Temporal Augmented Retrieval (TAR) - Dynamic RAG ](https://www.reddit.com/r/MachineLearning/comments/18uddmj/project_temporal_augmented_retrieval_tar_dynamic/) , 2024-01-04-0910
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

     
 
all -  [ Help needed in understanding hosting with vLLM and Torchserve ](https://www.reddit.com/r/LocalLLaMA/comments/18uci4k/help_needed_in_understanding_hosting_with_vllm/) , 2024-01-04-0910
```
Hi all, I am fairly new to NLP and LLM hosting. I was planning to host Llama2-7B on an A10 GPU. On google searching I fo
und out that vLLM is quite famous and robust for hosting LLM's with 'Paged Attention' (Need to read this yet). 

I am fa
irly comfortably with torchserve, so I was planning to host vLLM (llama2-7b) in combination with Pytorch Serve. I am pla
nning to do the following:   
\- Load the model on model server with:  **llm = LLM(model='facebook/opt-125m')**   
\- Wi
thin the torchserve inference function, I will infer like: **single\_output = llm.generate(1\_PROMPT, sampling\_params)*
* 

\-------------------

My Questions: 

\- There could  be multiple requests at a time. The queue and async operations
 will be handled by torchserve. **So in this case, will vLLM internally perform continuous batching ?** 

\- Is this the
 right way to use vLLM on any model-server other than the setup already provided by vLLM repo ? (triton, openai, langcha
in, etc) (when I say any model server, I mean flask, django, or any other python based server application). 

\-------  

Thanks a lot for your suggestions and guidance in advance. I am also not against Triton or anything which I provided ou
t of box, I am just exploring this combination as all other models I use are currently hosted using torchserve (all the 
models are CNN based though).   
 
```
---

     
 
all -  [ Would it be smarter to use chunks of just embeddings in this situation? ](https://www.reddit.com/r/LangChain/comments/18u77h9/would_it_be_smarter_to_use_chunks_of_just/) , 2024-01-04-0910
```
I work for a company that develops software to manage company operations, including freight management, interest, profit
s, inventory, and more. We used to provide each customer with a massive user's manual as a reference for any questions t
hey might have. However, this proved to be incredibly inefficient, so we decided to leverage the power of LLMs (Large La
nguage Models) to create a personalized chat interface. This would allow clients to get answers directly from the manual
 in a more dynamic and user-friendly way.

Unfortunately, simply feeding the entire manual to the LLM resulted in chaoti
c and inaccurate outputs. Answers were often incoherent and meaningless. Thankfully, I discovered the techniques of chun
king and embeddings.

Now, my question is: given that our company's manual is already divided into smaller PDFs for each
 topic, should I further break down these sections into smaller chunks for LLM training, or would it be sufficient to ju
st create embeddings from the existing PDFs? Additionally, can the LLM formulate answers by drawing information from mul
tiple vectors (embeddings) at once? Or it only uses the info from the embedding it's mostly similar to the user's query?

```
---

     
 
all -  [ what should use to bulid Saas for chating with static 50K document's , Chatgpt Api ? or Langchain ?  ](https://www.reddit.com/r/OpenAI/comments/18tvty6/what_should_use_to_bulid_saas_for_chating_with/) , 2024-01-04-0910
```
hello folks 

&#x200B;

i hav an idea and i want start to build it but before i have question based on the nature of the
 project and data 

&#x200B;

what should use to bulid it ? 

when the data is static and its contains 50K document's  ,


should i use Chatgpt Api ? 

or Langchain ? 

or lamaindex ? 
```
---

     
 
all -  [ what should use to bulid Saas for chating with static 50K document's , Chatgpt Api ? or Langchain ?  ](https://www.reddit.com/r/PromptEngineering/comments/18tvtrh/what_should_use_to_bulid_saas_for_chating_with/) , 2024-01-04-0910
```
hello folks   
i hav an idea and i want start to build it but before i have question based on the nature of the project 
and data   
what should use to bulid it ?   
when the data is static and its contains 50K document's  ,  
should i use C
hatgpt Api ?   
or Langchain ?   
or lamaindex ? 
```
---

     
 
MachineLearning -  [ [R][P] Autogen + Langchain Tools + Local LLM doesn't work. ](https://www.reddit.com/r/MachineLearning/comments/18tex1j/rp_autogen_langchain_tools_local_llm_doesnt_work/) , 2024-01-04-0910
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

     
 
MachineLearning -  [ [P] Seeking Advice for Building a School Handbook Chatbot Using OpenAI and Vector Databases ](https://www.reddit.com/r/MachineLearning/comments/18rndcp/p_seeking_advice_for_building_a_school_handbook/) , 2024-01-04-0910
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

     
 
MachineLearning -  [ [D] github repositories for ai web search agents ](https://www.reddit.com/r/MachineLearning/comments/18dhtm4/d_github_repositories_for_ai_web_search_agents/) , 2024-01-04-0910
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

     
 
MachineLearning -  [ [P] flex-prompt: a flexible prompt rendering engine that ensures you'll never exceed your LLM's cont ](https://www.reddit.com/r/MachineLearning/comments/18d581q/p_flexprompt_a_flexible_prompt_rendering_engine/) , 2024-01-04-0910
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

     
 
MachineLearning -  [ [D] Working on RAG? You should be evaluating its performance and we've built a way to do that. ](https://www.reddit.com/r/MachineLearning/comments/18ciet5/d_working_on_rag_you_should_be_evaluating_its/) , 2024-01-04-0910
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

     
 
deeplearning -  [ Unlocking the Power of Language: How LangChain Transforms Data Analysis and More ](https://www.reddit.com/r/deeplearning/comments/18l788y/unlocking_the_power_of_language_how_langchain/) , 2024-01-04-0910
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

     
 
deeplearning -  [ [D] Mastering Chain Composition with LangChain Expression Language (LCEL) ](https://www.reddit.com/r/deeplearning/comments/18i0wot/d_mastering_chain_composition_with_langchain/) , 2024-01-04-0910
```
In the intricate landscape of modern software development, orchestrating complex sequences of actions seamlessly poses a
 significant challenge. Enter LangChain Expression Language (LCEL), a groundbreaking declarative approach designed to re
volutionize the composition of chains within software architecture.

Link: [https://medium.com/ai-artistry/mastering-cha
in-composition-with-langchain-expression-language-lcel-2d5041fb0cbd](https://medium.com/ai-artistry/mastering-chain-comp
osition-with-langchain-expression-language-lcel-2d5041fb0cbd)  
```
---

     
