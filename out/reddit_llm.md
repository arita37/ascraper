 
all -  [ Build an AI-powered blogging platform (Next.js, Langchain & CopilotKit) ](https://thegreatbonnie.hashnode.dev/how-to-build-an-ai-powered-blogging-platform-nextjs-langchain-copilotkit) , 2024-04-20-0910
```

```
---

     
 
all -  [ Curated list of open source tools to test and improve the accuracy of your RAG/LLM based app ](https://www.reddit.com/r/LangChain/comments/1c87gn2/curated_list_of_open_source_tools_to_test_and/) , 2024-04-20-0910
```
Hey everyone,

  
What are some of the tools you are using for testing and improving your applications? I have been cura
ting/following a few of these. But, wanted to learn what your general experience has been? and what challenges you all a
re facing.

- [https://github.com/explodinggradients/ragas](https://github.com/explodinggradients/ragas)  
- [https://gi
thub.com/promptfoo/promptfoo](https://github.com/promptfoo/promptfoo)  
- [https://github.com/braintrustdata/autoevals](
https://github.com/braintrustdata/autoevals)  
- [https://github.com/stanfordnlp/dspy](https://github.com/stanfordnlp/ds
py)  
- [https://github.com/jxnl/instructor/](https://github.com/jxnl/instructor/)  
- [https://github.com/guidance-ai/g
uidance](https://github.com/guidance-ai/guidance)

Separately, I am also building one which is more focused towards trac
ing and evaluations  
- [https://github.com/Scale3-Labs/langtrace](https://github.com/Scale3-Labs/langtrace)
```
---

     
 
all -  [ I need some guidance on my approach ](https://www.reddit.com/r/Langchaindev/comments/1c85g5f/i_need_some_guidance_on_my_approach/) , 2024-04-20-0910
```
I'm working on a tool that has a giant data entry that consist in a json describing a structure for a file and this is m
y first attemp of using Langchain. This is what I'm doing:

First, I fetch the json file and get the value I need. It st
ill consists in a few thousand lines.

    data = requests.get(...)
    raw_data = str(data)
    splitter = CharacterTex
tSplitter(chunk_size=500, chunk_overlap=0)
    documentation = splitter.split_text(text=raw_data)
    vector = Chroma.fr
om_texts(documentation, embeddings)
    return vectorraw_data = str(data)
    splitter = CharacterTextSplitter(chunk_siz
e=500, chunk_overlap=0)
    documentation = splitter.split_text(text=raw_data)
    vector = Chroma.from_texts(documentat
ion, embeddings)
    return vector

  
Then, I build my prompt:

    vector = <the returned vector>
    llm = ChatOpenAI
(api_key='...')
    template = '''You are a system that generates UI components following the sctructure described in th
is context {context}, from an user request. Answer using a json object
                Use texts in spanish for the requ
ired components. 
                '''
    user_request = '{input}'
    prompt = ChatPromptTemplate.from_messages([
     
   ('system', template),
        ('human', user_request)
    ])
    
    document_chain = create_stuff_documents_chain(l
lm, prompt)
    
    retrival = vector.as_retriever()
    
    retrival_chain = create_retrieval_chain(retrival, documen
t_chain)
    
    result = retrival_chain.invoke(
        {
            'input': 'I need to create three buttons for my 
app'
        }
    )
    
    return str(result)

What would be the best approach for archiving my purpouse of giving th
e required context to the llm without exceding the token limit? Maybe I should not put the context in the prompt templat
e, but I don't have other alternative in mind.
```
---

     
 
all -  [ Allowed comparators for different vector stores? ](https://www.reddit.com/r/LangChain/comments/1c84lph/allowed_comparators_for_different_vector_stores/) , 2024-04-20-0910
```
I am looking for a good vector store for self-querying in LangChain. I want to be able to query, “find me a movie with D
iCaprio in it” and it should be able to find Leonardo DiCaprio in the metadata.

Chroma doesn’t support “contain”, what 
would be other DB options that can support this while also do the vector similarity search? LangChain documentation does
n’t describe the “allowed_comparators” attribute in their self-querying vector stores info.
```
---

     
 
all -  [ Question about you guys ](https://www.reddit.com/r/LangChain/comments/1c8370g/question_about_you_guys/) , 2024-04-20-0910
```
Hey everybody. Without going too much into detail I would be super interested what you guys are using this technology fo
r. We hear a lot about technicalities here but I'm really wondering how much you are using these technologies in your li
fe and in your work. Would be super interesting to know
```
---

     
 
all -  [ AgentExecutor VS model.bind_tools() in langgraph ](https://www.reddit.com/r/LangChain/comments/1c82vk3/agentexecutor_vs_modelbind_tools_in_langgraph/) , 2024-04-20-0910
```
Guys, with the latest updates, can someone please explain to me the difference between invoking AgentExecutor having use
d 'create\_tool\_calling\_agent' method as opposed to binding tools to the model and invoking it? Especially in the cont
ext of langgraph. I see so many tutorials on langgraph and it is always 'model.bind\_tools()', only a few tutorials use 
AgentExecutor within langgrpah. Do I even need to use it within a langgraph? What would be the benefit/difference?
```
---

     
 
all -  [ Is it true that it's slower to use Langchain than to call the model API's directly? ](https://www.reddit.com/r/LangChain/comments/1c82clj/is_it_true_that_its_slower_to_use_langchain_than/) , 2024-04-20-0910
```
I have heard from many people that Langchain is good for prototyping but not for production, is it because it's slower t
han using each LLM's APIs directly? I did some testing comparing the response speed from calling OpenAI directly versus 
calling it via Langchain, and Langchain consistently generates output 10% - 30% slower, not sure if it's my local proble
m or if it's a universal observation. 
```
---

     
 
all -  [ Burr: an OS framework for building and debugging agentic AI apps faster ](https://www.reddit.com/r/AI_Agents/comments/1c81b63/burr_an_os_framework_for_building_and_debugging/) , 2024-04-20-0910
```
[https://github.com/dagworks-inc/burr](https://github.com/dagworks-inc/burr)

**TL;DR** We created Burr to make it easie
r to build and debug AI applications that carry state/make complex decisions. AI agents are a very natural application. 
It is similar in concept to Langgraph, and works with any framework you want (Langchain, etc...). It comes with OS telem
etry. We're looking for users, contributors, and feedback.

**The problem(s):** A lot of tools in the LLM space (DSPY, s
uperagents, etc...) end up burying what you actually want to see behind a layer of complexity and prompt manipulation. W
hile making applications that make decisions naturally requires complexity, we wanted to make it easier to logically mod
el, view telemetry, manage state, etc... while not imposing any restrictions on what you can do or how to interact with 
LLM APIs.

**We built Burr** to solve these problems. With Burr, you represent your application as a state machine of py
thon functions/objects and specify transitions/state manipulation between them. We designed it with the following capabi
lities in mind:

1. Manage application memory: Burr's state abstraction allows you to prune memory/feed it to your LLM (
in whatever way you want)
2. Persist/reload state: Burr allows you to load from any point in an application's run so you
 can debug/restart from failure
3. Monitor application decisions: Burr comes with a telemetry UI that you can use to deb
ug your app in real-time
4. Integrate with your favorite tooling: Burr is just stitching together python primitives -- c
lasses + functions, so you can write whatever you want. Use langchain and dive into the OpenAI/other APIs when you need.

5. Gather eval data: Burr has logging capabilities to ensure you capture data for fine-tuning/eval

It is meant to be a
 lightweight python library (zero dependencies), with a host of plugins. You can get started by running: pip install 'bu
rr\[start\]' && burr  
 \-- this will start the telemetry server with a few demos (click on *demos* to play with a chatb
ot + watch telemetry at the same time).

Then, check out the following resources:

1. [Burr's documentation/getting star
ted](https://burr.dagworks.io/getting_started/)
2. [Multi-agent-collaboration example using LCEL](https://github.com/DAG
Works-Inc/burr/tree/main/examples/multi-agent-collaboration/lcel)
3. [Fairly complex control-flow example that uses AI +
 human feedback to draft an email](https://github.com/DAGWorks-Inc/burr/tree/main/examples/web-server)

**We're really e
xcited** about the initial reception and are hoping to get more feedback/OS users/contributors -- feel free to DM me or 
comment here if you have any questions, and happy developing!

PS -- the name *Burr* is a play on the project we OSed ca
lled [Hamilton](https://github.com/dagworks-inc/hamilton) that you may be familiar with. They actually work nicely toget
her!
```
---

     
 
all -  [ PGVector duplicate embedding ](https://www.reddit.com/r/LangChain/comments/1c80n7e/pgvector_duplicate_embedding/) , 2024-04-20-0910
```
how prevent duplicate embedding instance in pgvector without delete collection.

update existing once and want new one  


```
---

     
 
all -  [ Langtrace Evaluations - Breeze through with hotkeys ](https://www.reddit.com/r/LangChain/comments/1c7zp7y/langtrace_evaluations_breeze_through_with_hotkeys/) , 2024-04-20-0910
```


https://reddit.com/link/1c7zp7y/video/v8ord1suegvc1/player

We have been busy shipping updates to **Langtrace**, an **
Open Source LLM observability tool** and I am excited to show our new and improved Evaluations Dashboard. We learned fro
m our early users that improving the RAG/model accuracy and gaining confidence with deploying their LLM based apps to pr
oduction has been the number 1 priority.

To solve for this, we have built a couple of things:

**1. Create tests with d
ifferent scoring scales and automatically capture LLM requests to these tests using Langtrace's SDK.**

**2. Evaluate th
e the requests by scoring against the response provided by the LLM to measure the overall average of each test.**

Effec
tively, teams can come up with a release criteria like - 'Factual Accuracy > 99%, Response Quality > 95%, Response Bias 
> 85%, Context Recall > 90%' and measure their product's performance against this release metric with Langtrace.

Additi
onally, we also realized that the user experience is extremely important for effective and fast evaluations. As a result
, the evaluations flow is fully optimized for hot keys and as an evaluator, you can breeze through a series of evaluatio
ns with just the arrow keys, enter and backspace without having to click through a bunch of times for each request.

Fin
ally, all of this can be setup with just 2 lines of code and Langtrace's Evaluation's dashboard will start capturing the
 requests in the appropriate test automatically

Don't forget to check out Langtrace and star the repository on Github.


Github - [https://github.com/Scale3-Labs/langtrace](https://github.com/Scale3-Labs/langtrace)
```
---

     
 
all -  [ AI Automatic Agency Business Explained (a practical guide) ](https://www.reddit.com/r/EntrepreneurRideAlong/comments/1c7ttiz/ai_automatic_agency_business_explained_a/) , 2024-04-20-0910
```
The rise of artificial intelligence (AI) has opened doors for businesses to streamline their operations and gain a compe
titive edge. I have been working in the field of AI for almost 2 years now. I am building an advanced AI directory calle
d seekme. While working for Seekme, I got the chance to meet AI founders and overall explore the AI landscape. AI have r
aised some highly potential busines opportunities. One of the new AI business potential is AI Automation Agency also kno
wn as AAA. The idea is quite new and low competitive. But it is definitely something that can attract eyes of small to m
id tier businesses. Here are the basic concept of the AI Automation Agency (AAA) model, an approach to implementing cust
om AI solutions for businesses. (I am assuming you already know what LLM, OCR, RAG etc means)

**What is an AI Automatio
n Agency (AAA)?**
Unlike traditional AI tools that offer generic functionalities, AAAs cater to specific business needs 
by creating custom AI solutions. These solutions integrate seamlessly with existing workflows and tech stacks, leveragin
g the power of generative AI and automation.
Lemme give you an example to make the idea clear. Imagine a high-volume leg
al firm drowning in paperwork. An AAA could design an AI-powered solution that automates tasks like document review and 
contract summarization. The AAA would integrate Optical Character Recognition (OCR) to convert scanned documents into te
xt and then utilize LLMs to analyze the content. Based on pre-defined rules and legal knowledge bases, the LLM could ide
ntify key clauses, flag potential risks, and even generate draft summaries  of lengthy contracts. This not only frees up
 valuable time for lawyers to focus on complex legal matters but also improves accuracy and consistency in document proc
essing as well as better reporting.

**Why AAA?**
Here are some compelling reasons to consider the AAA model:
**Fills th
e Gap for Smaller Businesses:** Many smaller companies lack the resources or expertise to develop in-house AI solutions.
 AAAs bridge this gap by providing readily available, customized solutions.
**Focus on Value, Not Just AI:** Effective A
I solutions go beyond simply incorporating AI. AAAs understand the importance of integrating AI with automation (think Z
apier) to create solutions that deliver real value.
**Niche Targeting is Key:** Focusing on a specific niche allows AAAs
 to gain a deeper understanding of client pain points and develop solutions that directly address them. This approach al
so helps with targeted outreach and establishing credibility.

**Roadmap to guide you through launching your AAA:**
 Cho
ose Your Niche: Select a niche you're familiar with, such as real estate, e-commerce, or legal services. Understanding t
he industry's needs allows you to develop solutions that resonate with clients.
 Build Your Toolkit: There are two main 
approaches to building custom solutions:
 Developer Network: If you lack programming expertise, consider building a netw
ork of on-demand web developers.
 No-Code Tools: Utilize no-code tools that offer drag-and-drop interfaces for building 
AI-powered solutions without coding.
 Cold Sales are Essential: Unless you have a pre-existing network, cold sales are c
rucial for acquiring clients. Craft compelling messages that highlight the value proposition of your AAA services.
The b
eauty of the AAA model lies in its accessibility. You don't  need to be a seasoned programmer to get started. Although y
ou must know basic coding and understand it’s principals. Most client needs can be addressed using APIs for Large Langua
ge Models (LLMs) along with automation tools. The true value lies in your ability to design and implement solutions that
  integrate seamlessly  with existing systems and workflows.

**Glimpse into the technical aspects of building custom AI
 solutions:**
**Leveraging LLMs:** Tools like Langchain and LlamaIndex simplify working with LLMs. They enable functiona
lities like integrating internal data sources and prompting LLMs to perform actions.
**Understanding RAG (Retrieval-Augm
ented Generation)**: RAG allows you to 'train' LLMs on a client's specific data, enhancing response accuracy and reducin
g the risk of irrelevant outputs.
**Enabling Autonomous Agents:** By analyzing LLM outputs, you can programmatically tri
gger actions like API calls. This allows chatbots to perform tasks beyond simply providing information.

**How No-Code T
ools Can Help**
No-code tools empower you to build solutions even without extensive coding knowledge. Here are some exam
ples:
**Solution 1:** AI Chatbots for SMEs: Tools like MyAskAI can be used to create chatbots that handle user queries, 
lead generation, and more. They simplify data ingestion and chatbot integration.
**Solution 2:** Internal Apps: Create i
nternal tools like report generation or draft generation based on user data and preferences. Tools like MindStudio can b
e used for content generation, and Zapier/Make.com can automate workflows involving multiple apps.

**Here's how to leve
rage AI for effective outreach:**
**Craft Compelling Messages:** Identify client pain points and frame your message to s
howcase how AI-powered solutions can address them. Quantify the potential benefits, such as cost savings or increased pr
oductivity.
**Targeted Prospecting:** Utilize tools like Apollo.io or ZoomInfo to find relevant prospects within your ch
osen niche. Tailor your outreach based on the target audience (e.g., company owners for smaller businesses, specific pro
fessionals in white-collar niches).

**Closing the Deal**
Once you've secured meetings with potential clients, focus on 
effectively closing the deal:
**Consultation Call:** Actively listen to client needs and pain points. Present a high-lev
el overview of potential solutions using tools like Plus AI for creating presentations.
**Demo Call:** Showcase a functi
onal prototype of a solution built with boilerplate code or no-code tools. Explain how the final product will look and f
unctionalities.

+++
PS: I am building [seekme.ai](https://seekme.ai). It acts as a comprehensive library of over 12000 
AI tools, categorized for various use cases, category, tasks and professions. The directory is updated daily, and even h
as a handy AI-powered search to help you filter and find the perfect AI tools. We send weekly AI updates in our newslett
er [subscribe here](https://seekme.ai/subscribe/newsletter)
```
---

     
 
all -  [ Unable to send request to containerized flask app ](https://www.reddit.com/r/flask/comments/1c7tk65/unable_to_send_request_to_containerized_flask_app/) , 2024-04-20-0910
```
Code for app.py - 

from flask import Flask, redirect, url_for, render_template, request, jsonify
import random
import o
s
import time
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from langchain_google_genai import C
hatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage


app = Flask(__name__)
app.config
['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

db = SQLAlchemy(app)

os.environ['GOOGLE_API_KEY'] = ''

class Data(d
b.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    request = db.Column(db.Text, nullable
=False)
    response = db.Column(db.Text)
    date_time = db.Column(db.DateTime, default=datetime.utcnow) 
    # action 
= db.Column(db.String(80))

    def __repr__(self):
        return '<UserData %r - %r>' % (self.request, self.date_time)


@app.route('/', methods = ['POST', 'GET'])
def home():

    if request.method == 'POST':
        json = request.get_js
on()

        if json and 'query'in json:
            question = json['query']

            model = ChatGoogleGenerative
AI(model='gemini-pro', convert_system_message_to_human=True)
            resp = model(
                [
               
     SystemMessage(content='Answer the given question in short - '),
                    HumanMessage(content = question
)
                ]
            )
        

            new_data = Data(request = question, response = resp.content)
   
         try:
                db.session.add(new_data)
                db.session.commit()
                return jsonif
y({'answer': resp.content})
            except Exception as e:
                print('##################################
#########')
                print(e)
                print('####################################################')
     
           return 'There was an issue in adding the data in database'
        else:
            return 'Unsupported quer
y format'
    else:
        # data = Data.query.order_by(Data.date_created).all()
        return 'Problem with request t
ype.'
        # return render_template('index.html', user_data = user_data)
    
    # return render_template('index.htm
l', content = 123)

def initialize_database():
    with app.app_context():
        db.create_all()

@app.route('/admin')
 ## This was unaccessible, so redirect user to home.
def admin():
    time.sleep(3)
    return '<h1>This is a header</h1
>'

if __name__ == '__main__':
    initialize_database()
    # db.create_all()
    app.run(debug=True)

Some things are 
removed from the code.

Code for dockerfile -

FROM python:3.10.13-bookworm

WORKDIR /app

COPY ./requirements.txt /app

COPY ./Dockerfile /app
COPY ./app.py /app

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

EXPOS
E 5000

CMD python -u app.py

Code for test.py to send request to app -

test.py to send request to the app - 

import r
equests
import json

url = 'http://localhost:5000/'

question = 'What is a star?'
myobj = {'query': question}

data = js
on.dumps(myobj)

headers = {'Content-Type': 'application/json'}

response = requests.post(url, json = myobj, headers= he
aders)

print(response)
print(response.text)

Command for docker container - docker run -p 5000:5000 --name flask-app-co
ntainer flask-app:1.0
```
---

     
 
all -  [ Llama2 generating empty response ](https://i.redd.it/85fat4n5nevc1.jpeg) , 2024-04-20-0910
```
Hey everyone! I'm working on building a simple email replier, which uses the llama2-7b-chat-gguf model from Huggingface.
 I'm using the CTransformers function to create a llm instance and then using a custom prompt template to generate reply
 to an email body. I'm using the get_response() function from the image above.

However, for certain mails which are hav
ing a longer body, the response is just coming out blank. My streamlit app showing the output, just runs and stops witho
ut showing any error, just a blank response. Same in the terminal. However, it does generate okay replies for some other
 mails. Cant understand if this is random or some mails are causing some bug here.

Note: Previously, i had gotten an er
ror of token limit exceeded, when i tried to generate response for a spam email having a body much longer than any of my
 ham emails, but here no such error is coming.

Can anyone give any hint/guidance/help? The project is to be submitted u
rgently.


```
---

     
 
all -  [ Challenges with AI Agents Tools and Open Source Models Guidance Needed ](https://www.reddit.com/r/AI_Agents/comments/1c7s980/challenges_with_ai_agents_tools_and_open_source/) , 2024-04-20-0910
```
 Is there a standard approach to building an agentic framework that yields good results? I'm currently using open-source
 tools like CrewAI for agents and Langchain for tool creation, but I'm running into issues due to their reliance on Open
AI's structure. Specifically, I'm trying to keep as much of the tech stack open-source as possible, including LLM models
 and embeddings. Any guidance on how to overcome these challenges and create effective tools would be greatly appreciate
d! 
```
---

     
 
all -  [ I need help i want create user input chat ](https://www.reddit.com/r/LangChain/comments/1c7s200/i_need_help_i_want_create_user_input_chat/) , 2024-04-20-0910
```
let's understand what scenario i want implement

1. i already have some information about user in database.
2. now if us
er ask question and if that question's answer is not available in database then chatbot should ask user to provide me th
at information and it should store in database now if user ask same question in future then my chatbot should to ans tha
t que

ex: lets user 'A' whose first name and last name i have already in my database but i don't have his birth date an
d if user A ask query 'when is my birthday ' then my chat bot is unable to ans that que as my db has no information.  
s
o my chatbot should reply 'i don't have that information can you please provide me your birth date'

now if user A provi
de his birth date then it should be store in Database . now whenever user A ask in future when is my birthday then now m
y chatbot is able to ans that que.

i want implement this feature using langchain

guy's please help and thanks in advan
ce
```
---

     
 
all -  [ What's the best framework to create a domain expert chatbot with search capabilities? ](https://www.reddit.com/r/Chatbots/comments/1c7rpe2/whats_the_best_framework_to_create_a_domain/) , 2024-04-20-0910
```
I want to create a chatbot with additional capability to search and retrieve the necessary information. I have no experi
ence in this.

I did some research and the recommended frameworks for chatbots are:
1. Dailogflow (No idea which option 
I would need: ES or CX)
2. RASA
3. Langchain
4. Botpress
5. Anything better that I might have missed


The alternatives 
for search feature are:
1. Google search API
2. Elastic Search

Hosting:
1. GCP
2. VPS


My constraints are
1. I want to
 complete this project as early as possible. I'd like to avoid anything 'from scratch' at this point. I'll prefer 'batte
ries included' kinda approach like django. A smaller learning curve would be better though I don't have any problem to g
o through steeper learning curve if it's absolutely necessary and worth it.

2. I'll be bearing the expense out of my ow
n pocket. I can't afford anything expensive. I've a bad experience with AWS during my learning phase. I had left one ECS
 instance ON and I got huge bill. I don't want to repeat the same mistake. I don't want to shoot the expenses out of roo
f during development and the testing phase itself. Hidden costs shouldn't be even a possibility. 

3. I understand that 
LLMs aren't really perfect and hallucinations are a constant issue. So, anything near to satisfactory conversation is ac
ceptable in terms of bot quality. 

4. Data privacy. Eventually, I would be testing this tool on actual users. I'd like 
their data to be safe and protected. 

5. This bot will be limited to specific industry. So, ability to train or fine tu
ne it for specialized knowledge is important.


Google ecosystem (dialogflow + search api + GCP) looks good but I've som
e reservations when it comes to google. I worry about the costs. I don't want to repeat my AWS like experience again. I 
don't trust google with user data. 

But barring above concerns, it seems better alternative from development speed and 
conversation accuracy point of view.


2. I don't have any idea about RASA. The only thing I know is that it'll take mor
e development time than dialogflow or botpress.

3. Langchain: Same as RASA. Not much idea about it. I saw some posts on
 reddit complaining that it makes the code messy.

4. Botpress: I believe it's similar to dialogflow and will be easier 
to develop a chatbot with it. I don't know about quality of the conversations or costs associated with it.  


What fram
ework would you recommend? What framework is in demand in the industry? Any other tips are welcome. If you are running s
imilar thing, please share your experiences. 


TLDR: I'm looking for a framework to create chatbot with search capabili
ties. I need to keep the expenses, development time, and learning curve as little as possible. Data privacy is important
. What tech stack would you recommend?
  
```
---

     
 
all -  [ how to make conversationalretrievalchain to include metadata in the prompt using langchain with chro ](https://www.reddit.com/r/LangChain/comments/1c7ra1w/how_to_make_conversationalretrievalchain_to/) , 2024-04-20-0910
```
 im trying to do a bot that answer questions from a chromadb , i have stored multiple pdf files with metadata like the f
ilename and candidate name , my problem is when i use conversational retrieval chain the LLM model just receive page\_co
ntent without the metadata , i want the LLM model to be aware of the page\_content with its metadata like filename and c
andidate name here is my code   
 

    conversation_chain=ConversationalRetrievalChain.from_llm(         llm=llm,      
   retriever=SelfQueryRetriever.from_llm(llm,vectorstore,document_content_description,metadata_field_info),             
    memory=memory,         verbose=True,                      )

 

and here is my attribute info

    metadata_field_in
fo = [     AttributeInfo(         name='filename',         description='The name of the resumee',         type='string',
               ),     AttributeInfo(         name='candidatename',         description='the name of the candidate',     
    type='string'     )  ]

and here is how i use the chain  

 

conversation\_chain({'query':user\_question})

&#x200B
;

&#x200B;
```
---

     
 
all -  [ Need help in understanding RunnablePassthrough ](https://www.reddit.com/r/LangChain/comments/1c7qwsw/need_help_in_understanding_runnablepassthrough/) , 2024-04-20-0910
```
I have a doubt in the RAG quickstart example provided in Langchain docs.  


    rag_chain = (
        {
            'co
ntext': retriever | format_docs, 
            'question': RunnablePassthrough(),
        }
        | prompt
        | ll
m
        | StrOutputParser()
    )

Here, how does the retriever in the 'context' get access to the 'question'?
```
---

     
 
all -  [ Create chatbot with user input ](https://www.reddit.com/r/LangChain/comments/1c7q8ke/create_chatbot_with_user_input/) , 2024-04-20-0910
```
Hello i am creating chatbot where i have store my data in database and create embedding for vector search but now i want
 add feature if anybody ask query to my chatbot and chatbot does not have specific information then chatbot should ask u
ser provide me additional information and if user provide information that it should be stored in my db so if again that
 query asked then my chatbot able provide to response of same query ( using langchain ) . Thanks in advance 
```
---

     
 
all -  [ Need help in understanding chunking strategy for RAG application in production  ](https://www.reddit.com/r/LangChain/comments/1c7pnzg/need_help_in_understanding_chunking_strategy_for/) , 2024-04-20-0910
```
Hey guys! Anyone here running RAG pipelines in production with user uploaded documents (semantic chunking, summaries, kn
owledge graphs etc)? I am working on a RAG application for PPC and want to chunks SOPs into chunks for vector DB. But I 
am confused on which chunking strategy is better to get the most optimal results from the LLM.
```
---

     
 
all -  [ Is there an API that generates text and cites the text with sources from the internet? ](https://www.reddit.com/r/LangChain/comments/1c7pgho/is_there_an_api_that_generates_text_and_cites_the/) , 2024-04-20-0910
```
I'm trying to build something like [Perplexity.AI](http://Perplexity.AI) and looking for an API that does the retrieval 
from the net, parses the topk links, passes this through an LLM and produces text along with citations? 

LangChain has 
some functionality to cite sources from a text file but looking for an end-to-end solution here.
```
---

     
 
all -  [ cant get map_rerank to work ](https://www.reddit.com/r/LangChain/comments/1c7kw5k/cant_get_map_rerank_to_work/) , 2024-04-20-0910
```
  

This is my code, It needs improvement. The objective of the app is to retrieve simillar costumer support tickets fro
m a .csv, have the llm rerank the best one, and try tô respond the query, while showing the source. I figured the map\_r
erank chain would be perfect for the case, but It lacks good examples in documentation.

&#x200B;

from langchain.prompt
s import ChatPromptTemplate

from langchain.prompts.prompt import PromptTemplate

from operator import itemgetter

from 
typing import List, Tuple

from langchain.schema.runnable import RunnableMap, RunnablePassthrough

from langchain.schema
 import format\_document

from langchain.chains import RetrievalQA

from langchain.callbacks.manager import CallbackMana
ger

from langchain\_community.callbacks import StreamlitCallbackHandler

from langchain.callbacks.streaming\_stdout\_fi
nal\_only import FinalStreamingStdOutCallbackHandler

   
 

\# %%

callback\_manager=CallbackManager(\[FinalStreamingSt
dOutCallbackHandler()\])

llm = Ollama(model='Mistral', callback\_manager=CallbackManager(\[FinalStreamingStdOutCallback
Handler()\])) # 👈 stef default

\# %%

\# load document

loader = DirectoryLoader('../buscaRAG/source\_documents/', glob
='./\*.csv', loader\_cls=CSVLoader, 

loader\_kwargs={'encoding': 'utf-8', 'csv\_args': {'delimiter': ';','fieldnames': 
\['Id', 'Título', 'Descrição do chamado', 'Última ação de acompanhamento'\]}})

documents = loader.load()

\# split the 
documents into chunks

text\_splitter = CharacterTextSplitter(        

separator = ',',

chunk\_size = 1000,

chunk\_ov
erlap = 0,

length\_function = len,

)

texts = text\_splitter.split\_documents(documents)   

\# iniciar modelo de embe
dd

model\_name = 'intfloat/multilingual-e5-large'

encode\_kwargs = {'normalize\_embeddings': True} # set True to compu
te cosine similarity

model\_norm = HuggingFaceEmbeddings(model\_name=model\_name, model\_kwargs={'device': 'cuda'}, enc
ode\_kwargs=encode\_kwargs)

embeddings = model\_norm

\# expose this index in a retriever interface

db = Chroma(persis
t\_directory='../buscaRAG/chroma\_db', embedding\_function=embeddings)

retriever = db.as\_retriever(search\_type='simil
arity\_score\_threshold', search\_kwargs={'score\_threshold': 0.5, 'k': 6})

\#TFIDF retriever

TFIDF\_retriever = TFIDF
Retriever.from\_documents(documents)

\#ensemble retriever

ensemble\_retriever = EnsembleRetriever( retrievers=\[TFIDF\
_retriever, retriever\], weights=\[0.5, 0.5\], c= 80)

\# %%

\# create a chain to answer questions

qa = RetrievalQA.fr
om\_chain\_type(

llm=llm,

chain\_type='map\_rerank',

retriever=ensemble\_retriever,

return\_source\_documents=True,


verbose=True,

)

\# %%

def embedd():

db = Chroma.from\_documents(texts, embeddings, persist\_directory='../buscaRAG/
chroma\_db')

return db

\# %%

   
 

colA, colB = st.columns(\[.90, .10\])

with colA:

prompt = st.text\_input('promp
t', value='', key='prompt')

response = ''

with colB:

st.markdown('')

st.markdown('')

if st.button('🙋‍♀️', key='butt
on'):

response = qa.invoke(prompt, callbacks=\[StreamlitCallbackHandler(st.container())\])

st.markdown(response)

&#x2
00B;

The problems:

Mistral 7b Works Fine in ollama, but when a call It through langchain It slows down and hallucinate
s. Is It something with the system prompt?

g3r2ld0: Langchain complains that the chain doesnt have an output parser, I 
dont know How to put a simple string one in the chain. The warn in question?

AppData\\Roaming\\Python\\Python311\\site-
packages\\langchain\\chains\\llm.py:344: UserWarning: The apply\_and\_parse method is deprecated, instead pass an output
 parser directly to LLMChain

g3r2ld0: In streamlit, the widget showing the callbacks is too thin
```
---

     
 
all -  [ I studied 5,000+ Series A and Series B stage companies in the USA to identify the next unicorns ](https://www.reddit.com/r/private_equity/comments/1c7jyrd/i_studied_5000_series_a_and_series_b_stage/) , 2024-04-20-0910
```
I researched over 5000 Series A and Series B stage companies in the USA to identify the next unicorns.

I identified 10 
companies that I feel could become unicorns very soon based on several factors including growth rates, hiring trends, an
d leadership. I then ranked them on a few metrics and presented the data to you below.

I used Crustdata's database for 
this research.

# Top 10 Fastest Growing Soonicorn Companies in the USA

1. LangChain is a language model application de
velopment library that develops a language model framework to power applications.

2. Vilya is a biotechnology company d
eveloping a novel class of drugs that precisely target the biology of disease.

3. Duckbill is an execution engine for d
aily tasks that functions as a personal assistant copilot using AI-powered technology.

4. Gutsy is a data-driven securi
ty governance platform that applies process mining to secure enterprises.

5. rabbit inc. is a tech company specializing
 in creating a customized operating system using a natural language interface. They most recently launched the rabbit r1
 that got a lot of attention worldwide.

6. Babylon is building a new public Cosmos-based PoS blockchain called Babylon 
with a native token as the bridge between Bitcoin and the PoS world.

7. Saronic builds scalable, fully integrated unman
ned surface vehicles and vessels for naval and maritime forces.

8. Unstructured transforms natural language data from r
aw to machine learning-ready through its open-source libraries and APIs.

9. Yurts is a secure, deployable, full-stack g
enerative AI platform for Large Language Models.

10. Luminopia is developing a new class of treatments through digital 
therapeutics for significant neuro-visual disorders.

You can read the full research (with some cool pictures & graphs) 
[here](https://goldenpineapple.substack.com/p/the-usas-next-unicorns)
```
---

     
 
all -  [ 2 LLMs within Langchain Agent ](https://www.reddit.com/r/LangChain/comments/1c7ilq3/2_llms_within_langchain_agent/) , 2024-04-20-0910
```
I’m building an agent with custom tools with Langchain and wanna know how to use different llms within it.

The issue I 
ran into with assistant API from OpenAI is that it’s super slow. So I thought since Groq is ultra fast and rolled out th
e new tool calling feature, I’d give it a shot. But the thing is Groq’s tool calling isn’t really working, meaning it do
esn’t recognize when to call a tool. So I thought maybe I could use GPT-turbo to decide whether it needs to call a tool 
and run the tool, and have Groq to output the final result. However, I don’t seem to find the way to do it. Does anyone 
know how to work it out? Or do I just need to use Router Chain or something for this?
```
---

     
 
all -  [ I studied 5,000+ Series A and Series B stage companies in the USA to identify the next unicorns ](https://www.reddit.com/r/SaaS/comments/1c7ic61/i_studied_5000_series_a_and_series_b_stage/) , 2024-04-20-0910
```
I researched over 5000 Series A and Series B stage companies in the USA to identify the next unicorns.  

I identified 1
0 companies that I feel could become unicorns very soon based on several factors including growth rates, hiring trends, 
and leadership. I then ranked them on a few metrics and presented the data to you below.

I used Crustdata's database fo
r this research.

### Top 10 Fastest Growing Soonicorn Companies in the USA

1. LangChain is a language model applicatio
n development library that develops a language model framework to power applications. 

2. Vilya is a biotechnology comp
any developing a novel class of drugs that precisely target the biology of disease. 

3. Duckbill is an execution engine
 for daily tasks that functions as a personal assistant copilot using AI-powered technology.

4. Gutsy is a data-driven 
security governance platform that applies process mining to secure enterprises.

5. rabbit inc. is a tech company specia
lizing in creating a customized operating system using a natural language interface. They most recently launched the rab
bit r1 that got a lot of attention worldwide. 

6. Babylon is building a new public Cosmos-based PoS blockchain called B
abylon with a native token as the bridge between Bitcoin and the PoS world.

7. Saronic builds scalable, fully integrate
d unmanned surface vehicles and vessels for naval and maritime forces. 

8. Unstructured transforms natural language dat
a from raw to machine learning-ready through its open-source libraries and APIs.

9. Yurts is a secure, deployable, full
-stack generative AI platform for Large Language Models.

10. Luminopia is developing a new class of treatments through 
digital therapeutics for significant neuro-visual disorders.


You can read the full research (with some cool pictures &
 graphs) [here](https://goldenpineapple.substack.com/p/the-usas-next-unicorns)
```
---

     
 
all -  [ Best way of using context from different files? ](https://www.reddit.com/r/LangChain/comments/1c7fcad/best_way_of_using_context_from_different_files/) , 2024-04-20-0910
```
I'm struggling trying to use a .txt and a .csv file to give more context to my Chatbot.

This is partly what I have at t
he moment:

    # For text files
    text_loader = DirectoryLoader('', glob='./test.txt', loader_cls=TextLoader)
    tex
t_docs = text_loader.load()
    # For CSV files
    csv_loader = DirectoryLoader('', glob='./stock.csv', loader_cls=CSVL
oader)
    csv_docs = csv_loader.load()
    # Combine the documents
    loader_all = MergedDataLoader(loaders=[text_load
er, csv_loader])
    docs = loader_all.load()
    db = Chroma.from_documents(docs, embedding_function)
    retriever = d
b.as_retriever()
    chain = (
    {'context': retriever, 'question': RunnablePassthrough()}
    | prompt
    | model
  
  | StrOutputParser()
    )

When I ask something related to the data within the .csv (related to some products' stock) 
it answers well. But, if it's a question of something within the .txt file, it doesn't know what to answer.

Have someon
e already dealt with this?
```
---

     
 
all -  [ Streaming Pandas Dataframe ](https://www.reddit.com/r/LangChain/comments/1c7cp2r/streaming_pandas_dataframe/) , 2024-04-20-0910
```
Does the Pandas Dataframe Agent allow for streaming, or rather - is it even beneficial to attempt to stream it or does i
t output all at once? 
```
---

     
 
all -  [ LangChain + gpt-4-vision-preview? ](https://www.reddit.com/r/LangChain/comments/1c7a141/langchain_gpt4visionpreview/) , 2024-04-20-0910
```
I have a fairly simple idea, which surprisingly difficult to execute. I am using LangChain in Python and I am trying to 
do the following:  


1. Sent gpt-4-vision an image
2. Make it extract some items in the image
3. Parse the response usi
ng the Pydantic parser (as I have a set structure in which i want the items) 

However, the uploading of an image seems 
to only be possible with the 'HumanMessage' object, which does not work together with the PromptTemplate. Has anyone man
aged to get this to work?  


Below is a very simplified version of my code:

    model = ChatOpenAI(model='gpt-4-vision
-preview', max_tokens=1024)
    parser = PydanticOutputParser(pydantic_object=ImageDetails)
    
    prompt = PromptTemp
late(
        template='''
          You are an expert on OCR.
        ''',
        input_variables=['query'],
        p
artial_variables={'format_instructions': parser.get_format_instructions()},
        validate_template=True,
    )
    
 
   chain = prompt | model | parser
    
    chain.invoke({'query': 'Identify all items, quantities and amounts on this p
icture.'})

Uploading an image with this code works, but ideally I'd like to combine them both into 1.

    image = enco
de_image('./image.jpeg')
    
    msg = model.invoke(
        [   AIMessage(
            content='You are a useful bot t
hat is especially good at OCR from images'
        ),
            HumanMessage(
                content=[
              
      {'type': 'text', 'text': 'Identify all items, quantities and amounts on this picture'},
                    {
    
                    'type': 'image_url',
                        'image_url': {
                            'url': f'dat
a:image/jpeg;base64,{image}'
                        },
                    },
                ]
            )
        ]

    )

&#x200B;
```
---

     
 
all -  [ I need some help in understanding the difference in utility between Langchain and AutoGPT ](https://www.reddit.com/r/LangChain/comments/1c731tr/i_need_some_help_in_understanding_the_difference/) , 2024-04-20-0910
```
First off - sorry if this is a question borne of ignorance, I've only been researching Langchain and RAG for about 2 wee
ks now and have mostly been working on toy projects with it in that time.

I am interested in making a modular agent bot
 that could help me with a few tasks.

The goal would be for the bot to be on 24/7ish, able to respond to user requests,
 my own admin requests, and to interact with APIs. Basically a chat and email bot with memory, that stays persistently u
p. The bot **must** be RAG enabled - I need it to have memory and 'learn' new things.

I originally started building all
 of this with Langchain and more or less had the event loop created, RAG enabled, etc. However from what I can tell Auto
GPT seems to do very similar stuff, which is great, but also doesn't allow the granularity of bot creation that Langchai
n does, and there's no real way to integrate them (and from what I can tell, doesn't really allow for any advanced form 
of RAG implementation?)

Are there ways to build bots like AutoGPT in Langchain? Would I essentially be re-inventing the
 wheel? Are there projects that are Langchain-based that work similarly, or allow greater modularity? I want a bot that 
can do a multi-step thinking progress and essentially work autonomously, but teams of people are obviously going to be b
etter at developing a framework like that than just me alone, which is why I'm so concerned about trying to build a bot 
like that.
```
---

     
 
all -  [ Use a local vector store in the browser? ](https://www.reddit.com/r/LangChain/comments/1c72f3s/use_a_local_vector_store_in_the_browser/) , 2024-04-20-0910
```
I'm working on a web chat to interact with LLMs, and I'm trying to add the possibility for the user to upload a PDF and 
use RAG to interact with it via a LLM (pretty standard so far). However, I was wondering if I can achieve that without m
anaging a cloud vector database (e.g. such as Pinecone). Currently, the user's data is stored locally in their browser w
ith indexedDB (i.e. almost same as localstorage), so I would have liked to **run a retriever in the browser as well** (i
n order to extract the relevant chunks to pass to the LLM). Is it possible? Basically I would need a vector database tha
t can run in the browser where I load the embeddings (from indexedDB) and run the retriever.

Is there a better way? (My
 only preference would be not having to manage a cloud vector db, which would involve a server and authentication.)

Tha
nks in advance! (Please let me know if I'm not making sense - I'm quite new to RAG and Langchain.)
```
---

     
 
all -  [ With or without vectorization ](https://www.reddit.com/r/LangChain/comments/1c70t2h/with_or_without_vectorization/) , 2024-04-20-0910
```
Hey, can we create a question answer over documents System without the vectorization using langchain? If yes plis, diffe
rentiate between the system created using vectorization and without vectorization.
```
---

     
 
all -  [ How to use Chain-of-Thoughts methods in your project? ](https://www.reddit.com/r/LangChain/comments/1c700pk/how_to_use_chainofthoughts_methods_in_your_project/) , 2024-04-20-0910
```
The introduction of CoT prompting improved large language models’ results in performing reasoning tasks.

I compiled the
 useful resources that could help you utilize CoT methods in your projects:

Methods that require you to write your prom
pt in a specific way:

* Basic: zero-shot prompting, few-shot prompting
* Chain-of-thought: Original method, self-consis
tency, zero-shot chain-of-thought -> Read our [article](https://www.turingpost.com/p/cot) and use these [7 resources to 
master prompt engineering](https://www.turingpost.com/p/prompttomaster)

Other variations of Chain-of-Thought methods:


* Automatic-Chain-of-Thought (Auto-CoT) proposes replacing the entire CoT framework with a single phrase: 'Let's think s
tep by step.' → [Original code from AWS](https://github.com/amazon-science/auto-cot)
* Program-of-Thoughts Prompting (Po
T) suggested expressing the reasoning steps as Python programs by the LLM and delegating the computation to a Python int
erpreter instead of computing the result by the LLM itself → [Original code](https://github.com/wenhuchen/Program-of-Tho
ughts)
* Multimodal Chain-of-Thought Reasoning (Multimodal-CoT) suggested incorporating language (text) and vision (imag
es) modalities instead of working with just text → [Original code from AWS](https://github.com/amazon-science/mm-cot)
* 
Tree-of-Thoughts (ToT) adopts a more human-like approach to problem-solving by framing each task as a search across a tr
ee of possibilities where each node in this tree represents a partial solution. → [Original code from the Princeton NLP 
team](https://github.com/princeton-nlp/tree-of-thought-llm)
* Graph-of-Thoughts (GoT) leverages graph theory to represen
t the reasoning process → [Original code](https://github.com/spcl/graph-of-thoughts)
* Algorithm-of-Thoughts (AoT) embed
s algorithmic processes within prompts, enabling efficient problem-solving with fewer queries → [Code for implementing A
oT from Agora AI lab](https://github.com/kyegomez/Algorithm-Of-Thoughts)
* Skeleton-of-Thought (SoT) is based on the ide
a of guiding the LLM itself to give a skeleton of the answer first and then write the overall answer parallelly instead 
of sequentially. → [Original code](https://github.com/imagination-research/sot)

Do you use any of these methods? Which 
one is your favorite?
```
---

     
 
all -  [ How to output specific intermediary results at the end of the chain ](https://www.reddit.com/r/LangChain/comments/1c6zl4g/how_to_output_specific_intermediary_results_at/) , 2024-04-20-0910
```
Edit: I found out how to do this with (lambda x: intermediate_results.update({'resultA':x}) or x)

I have a chain in lan
gchain that calls on LLMs several times and then processes the output. It looks something like prompt1 | llm | OutputPar
ser | prompt2 | llm | OutlutParser etc. I would like to capture the results that come out of the Output Parser and have 
the chain return those together with the actual result of the chain. 
```
---

     
 
all -  [ Persistent directory storage for docstore in MultiVectorRetriever ](https://www.reddit.com/r/LangChain/comments/1c6y7oo/persistent_directory_storage_for_docstore_in/) , 2024-04-20-0910
```
i have been using the multi vector retriever from langchain for storing images and their description to my embeddings db
. i am embedding the descriptions and storing the images as it is for retrieval. the documents are labelled by doc\_id w
hich i am storing in a InMemoryStore but i would want this to be in a persistent directory or variable (which i can stor
e in a directory).   
i have tried using the LocalFileStore but it stores byte-like object and the docstore needs to be 
in str format ([documentation](https://api.python.langchain.com/en/latest/retrievers/langchain.retrievers.multi_vector.M
ultiVectorRetriever.html#langchain-retrievers-multi-vector-multivectorretriever)) so this approach threw TypeError. 

is
 there anyway to implement this functionality? please help me, i am just a beginner with langchain and llms.

this is my
 code for the retriever and the llm chain- 

    import uuid
    
    from langchain.retrievers.multi_vector import Mult
iVectorRetriever
    from langchain.storage import InMemoryStore, LocalFileStore
    from langchain_community.vectorstor
es import Chroma
    from langchain_core.documents import Document
    
    def create_multi_vector_retriever(store, vec
torstore, id_key, text_summaries=None, texts=None):
      '''
      Create a multi-vector retriever that indexes summari
es and stores embeddings in a folder.
    
      Args:
          folder_path: Path to the folder for storing embeddings.

          text_summaries: List of text summaries for new documents (optional).
          texts: List of corresponding t
exts/images/etc. for new documents ek(optional).
    
      Returns:
          The multi-vector retriever instance.
    
  '''
    
      # Create the multi-vector retriever
      retriever = MultiVectorRetriever(
          vectorstore=vecto
rstore,
          docstore=store,
          id_key=id_key,
          search_kwargs={'k': 5},
      )
    
      def add_
documents(retriever, doc_summaries, doc_contents):
          doc_ids = [str(uuid.uuid4()) for _ in doc_contents]
       
   summary_docs = [
              Document(page_content=s, metadata={id_key: doc_ids[i]})
              for i,s, in enum
erate(doc_summaries)
          ]
          retriever.vectorstore.add_documents(summary_docs)
          retriever.docstor
e.mset(list(zip(doc_ids, doc_contents)))
          print('added')
    
      # Filter out empty text_summaries
      non
_empty_text_summaries = [summary for summary in text_summaries if summary.strip()]
    
      # Add texts, tables, and i
mages if summaries are not empty
      if non_empty_text_summaries:
          add_documents(retriever, non_empty_text_su
mmaries, texts)
    
      return retriever
    
    
    vectorstore = Chroma(
        collection_name = 'second',
    
    persist_directory = '/content/embeddings12',
        embedding_function=VertexAIEmbeddings(model_name='textembedding
-gecko@latest'),
    )
    
    docstore = InMemoryStore()
    id_key='doc_id'
    
    # Create Retriever
    retriever
_multi_vector_img = create_multi_vector_retriever(
        docstore,
        vectorstore,
        id_key,
        doc_su
mmaries, #description of the images
        doc_img_base64_list #the actual images
    )
    
    def multi_modal_rag_ch
ain(retriever):
      '''
      Multi-modal RAG chain
      '''
    
      # Multi-modal LLM
      model = ChatVertexAI(

          temperature = 0, model_name = 'gemini-pro-vision', max_output_tokens=2048, safety_settings = safety_settings

      )
    
    
      # RAG Pipeline
      chain = (
          {
              'context': retriever | RunnableLambda(s
plit_image_text_types),
              'question': RunnablePassthrough()
          }
          | RunnableLambda(img_promp
t_func)
          | model
          | StrOutputParser()
      )
      return chain
    
    
    # Create RAG chain
    
chain_multimodal_rag = multi_modal_rag_chain(retriever_multi_vector_img)

thanks a lot!!
```
---

     
 
all -  [ What are the most promising ways you guys have done RAG evaluation during dev and monitoring? ](https://www.reddit.com/r/LangChain/comments/1c6wkza/what_are_the_most_promising_ways_you_guys_have/) , 2024-04-20-0910
```
See post title
```
---

     
 
MachineLearning -  [ [D] How to get the source documents from the retrieved context for RAG?  ](https://www.reddit.com/r/MachineLearning/comments/1bvoc1t/d_how_to_get_the_source_documents_from_the/) , 2024-04-20-0910
```
I'm not using Lanchain but only making API calls to an LLM service provider. The retriever is connected to a vector DB, 
and I would like to know what the LLM refers to WITHIN that retrieved context whenever it provides an answer, similar to
 how return_source_documents works in Langchain.

I'm using AzureOpenAI. I couldn't find much in their docs that related
 to returning the source documents. Any help will be greatly appreciated!

```
---

     
 
MachineLearning -  [ [P] RAG pipeline to query the ML Engineering Open Book ](https://www.reddit.com/r/MachineLearning/comments/1bu4wyx/p_rag_pipeline_to_query_the_ml_engineering_open/) , 2024-04-20-0910
```
I built a quick RAG implementation using Langchain to make it easy to query the [ML Engineering Open Book](https://githu
b.com/stas00/ml-engineering) by [Stas Bekman](https://twitter.com/StasBekman). The Multi-Vector retriever gave pretty go
od results and was quite easy to set up too. 

Github link - [https://github.com/shreyansh26/RAG-ML-Engg-Open-Book](http
s://github.com/shreyansh26/RAG-ML-Engg-Open-Book)

Hope this is useful for folks!
```
---

     
 
MachineLearning -  [ [Project] FinancialAdvisorGPT : LLM+RAG Boilerplate Project ](https://www.reddit.com/r/MachineLearning/comments/1btlpgd/project_financialadvisorgpt_llmrag_boilerplate/) , 2024-04-20-0910
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

     
 
MachineLearning -  [ [Project] Picachain, image search made simple. ](https://www.reddit.com/r/MachineLearning/comments/1bt7epv/project_picachain_image_search_made_simple/) , 2024-04-20-0910
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

     
 
deeplearning -  [ Tengyu Ma on Voyage AI - Weaviate Podcast #91! ](https://www.reddit.com/r/deeplearning/comments/1bjft8i/tengyu_ma_on_voyage_ai_weaviate_podcast_91/) , 2024-04-20-0910
```
**Voyage AI** is the newest giant in the embedding, reranking, and search model game!

I am SUPER excited to publish our
 latest Weaviate podcast with Tengyu Ma, Co-Founder of Voyage AI and Assistant Professor at Stanford University!

We beg
an the podcast with a deep dive into everything embedding model training and contrastive learning theory. Tengyu deliver
ed a **masterclass** in everything from scaling laws to multi-vector representations, neural architectures, representati
on collapse, data augmentation, semantic similarity, and more! I am beyond impressed with Tengyu's extensive knowledge a
nd explanations of all these topics.

The next chapter dives into a case study Voyage AI did **fine-tuning an embedding 
model for the LangChain documentation.** This is an absolutely fascinating example of the role of continual fine-tuning 
with very new concepts (for example, very few people were talking about chaining together LLM calls 2 years ago), as wel
l as the data efficiency advances in fine-tuning.

We concluded by discussing ML systems challenges in serving an embedd
ings API. Particularly the challenge of detecting if a request is for batch or query inference and the optimizations tha
t go into either say \~100ms latency for a query embedding or maximizing throughput for batch embeddings.

I hope you fi
nd the podcast interesting, more than happy to discuss any of these topics with you or answer any questions about the co
ntent in the podcast! Thank you so much!

YouTube: [https://www.youtube.com/watch?v=xPdyivfheqI](https://www.youtube.com
/watch?v=xPdyivfheqI)

Spotify: [https://spotifyanchor-web.app.link/e/u6XPLYfF7Hb](https://spotifyanchor-web.app.link/e/
u6XPLYfF7Hb)
```
---

     
