 
all -  [ Nice try, dude! Nice try :) ](https://i.redd.it/8kx7bm86p37e1.png) , 2024-12-16-0914
```

```
---

     
 
all -  [ Is LangChain the leading agentic framework? Should the begginer developers use LangChain or somethin ](https://www.reddit.com/r/AI_Agents/comments/1hf5dmq/is_langchain_the_leading_agentic_framework_should/) , 2024-12-16-0914
```
I want to learn to agentic frameworks but not sure where to start. Any tips?
```
---

     
 
all -  [ Test your AI apps with MockAI (Open-Source) ](https://www.reddit.com/r/LangChain/comments/1hf41kv/test_your_ai_apps_with_mockai_opensource/) , 2024-12-16-0914
```
As I began productionizing applications as an AI engineer, I needed a tool that would allow me to run tests, CI/CD pipel
ines, and benchmarks on my code that relied on LLMs. As you know once leaving demo-land these become EXTREMELY important
, especially with the fast nature of AI app development.

I needed a tool that would allow me to easily evaluate my LLM 
code without incurring cost and without blowing up waiting periods with generation times, while still allowing me to sim
ulate the 'real thing' as closely as possible, so I made [MockAI](https://github.com/ajac-zero/mock-ai).

I then realize
d that what I was building could be useful to other AI engineers, and so I turned it into an open-source library!

# How
 it works

MockAI works by mimicking servers from LLM providers locally, in a way that their API expects. As such, we ca
n use the normal `openai` library with MockAI along with any derivatives such as `langchain`. The only change we have to
 do is to set the `base_url` parameter to our local MockAI server.

# How to use

Start the server.

    # with pip inst
all
    $ pip install ai-mock 
    $ ai-mock server
    
    # or in one step with uv
    $ uvx ai-mock server

Change t
he base URL

    from openai import OpenAI
    
    # This client will call the real API
    client = OpenAI(api_key='..
.')
    
    # This client will call the mock API
    mock = OpenAI(api_key='...', base_url='http://localhost:8100/opena
i') 

The rest of the code is the exact same!

    # Real - Incur cost and generation time
    completion = client.chat.
completions.create(
        model='gpt-4o',
        messages=[ {'role': 'user', 'content': 'hello'} ]
      ).choices[0]
.message
    
    print(completion.content)
    # 'Hello! How may I assist you today?'
    
    # Mock - Instant and fre
e with no code changes
    completion = mock.chat.completions.create(
        model='gpt-4o',
        messages=[ {'role'
: 'user', 'content': 'hello'} ]
      ).choices[0].message
    
    print(completion.content)
    # 'hello'
    
    # B
ONUS - Set a custom mock response
    completion = mock.chat.completions.create(
        model='gpt-4o',
        message
s=[ {'role': 'user', 'content': 'Who created MockAI?'} ],
        extra_headers={'mock-response': 'MockAI was made by aj
ac-zero'},
      ).choices[0].message
    
    print(completion.content)
    # 'MockAI was made by ajac-zero'

Of course
, real use cases usually require tools, streaming, async, frameworks, etc. And I'm glad to say they are all supported by
 MockAI! You can check out more details [in the repo here](https://github.com/ajac-zero/mock-ai).

# Free Public API

I 
have set up a MockAI server as a public API, I intend for it to be a public service for our community, so you don't need
 to pay anything or create an account to make use of it.

If you decide to use it you don't have to install anything at 
all! Just change the 'base\_url' parameter to `mockai.ajac-zero.com`. Let's use `langchain` as an example:

    from lan
gchain_openai import ChatOpenAI
    from langchain_core.messages import HumanMessage, SystemMessage
    
    model = Cha
tOpenAI(
        model='gpt-4o-mini',
        api_key='...',
        base_url='https://mockai.ajac-zero.com/openai'
    
)
    
    messages = [
        SystemMessage('Translate the following from English into Italian'),
        HumanMessage
('hi!'),
    ]
    
    response = model.invoke(messages)
    print(response.content)
    # 'hi!'

It's a simple spell b
ut quite ~~unbreakable~~ useful. Hopefully, other AI engineers can make use of this library. I personally am using it fo
r testing, CI/CD pipelines, and recently to benchmark code without inference variations.

If you like the project or thi
nk it's useful, please leave a star on the [repo](https://github.com/ajac-zero/mock-ai)!
```
---

     
 
all -  [ Test your AI apps with MockAI (Open-Source) ](https://www.reddit.com/r/LLMDevs/comments/1hf3xga/test_your_ai_apps_with_mockai_opensource/) , 2024-12-16-0914
```
As I began productionizing applications as an AI engineer, I needed a tool that would allow me to run tests, CI/CD pipel
ines, and benchmarks on my code that relied on LLMs. As you know once leaving demo-land these become EXTREMELY important
, especially with the fast nature of AI app development.

I needed a tool that would allow me to easily evaluate my LLM 
code without incurring cost and without blowing up waiting periods with generation times, while still allowing me to sim
ulate the 'real thing' as closely as possible, so I made [MockAI](https://github.com/ajac-zero/mock-ai).

I then realize
d that what I was building could be useful to other AI engineers, and so I turned it into an open-source library!

# How
 it works

MockAI works by mimicking servers from LLM providers locally, in a way that their API expects. As such, we ca
n use the normal `openai` library with MockAI along with any derivatives such as `langchain`. The only change we have to
 do is to set the `base_url` parameter to our local MockAI server.

# How to use

Start the server.

    # with pip inst
all
    $ pip install ai-mock 
    $ ai-mock server
    
    # or in one step with uv
    $ uvx ai-mock server

Change t
he base URL

    from openai import OpenAI
    
    # This client will call the real API
    client = OpenAI(api_key='..
.')
    
    # This client will call the mock API
    mock = OpenAI(api_key='...', base_url='http://localhost:8100/opena
i') 

The rest of the code is the exact same!

    # Real - Incur cost and generation time
    completion = client.chat.
completions.create(
        model='gpt-4o',
        messages=[ {'role': 'user', 'content': 'hello'} ]
      ).choices[0]
.message
    
    print(completion.content)
    # 'Hello! How may I assist you today?'
    
    # Mock - Instant and fre
e with no code changes
    completion = mock.chat.completions.create(
        model='gpt-4o',
        messages=[ {'role'
: 'user', 'content': 'hello'} ]
      ).choices[0].message
    
    print(completion.content)
    # 'hello'
    
    # B
ONUS - Set a custom mock response
    completion = mock.chat.completions.create(
        model='gpt-4o',
        message
s=[ {'role': 'user', 'content': 'Who created MockAI?'} ],
        extra_headers={'mock-response': 'MockAI was made by aj
ac-zero'},
      ).choices[0].message
    
    print(completion.content)
    # 'MockAI was made by ajac-zero'

Of course
, real use cases usually require tools, streaming, async, frameworks, etc. And I'm glad to say they are all supported by
 MockAI! You can check out more details [in the repo here](https://github.com/ajac-zero/mock-ai).

# Free Public API

I 
have set up a MockAI server as a public API, I intend for it to be a public service for our community, so you don't need
 to pay anything or create an account to make use of it.

If you decide to use it you don't have to install anything at 
all! Just change the 'base\_url' parameter to `mockai.ajac-zero.com`. Let's use `langchain` as an example:

    from lan
gchain_openai import ChatOpenAI
    from langchain_core.messages import HumanMessage, SystemMessage
    
    model = Cha
tOpenAI(
        model='gpt-4o-mini',
        api_key='...',
        base_url='https://mockai.ajac-zero.com/openai'
    
)
    
    messages = [
        SystemMessage('Translate the following from English into Italian'),
        HumanMessage
('hi!'),
    ]
    
    response = model.invoke(messages)
    print(response.content)
    # 'hi!'

It's a simple spell b
ut quite ~~unbreakable~~ useful. Hopefully, other AI engineers can make use of this library. I personally am using it fo
r testing, CI/CD pipelines, and recently to benchmark code without inference variations.

If you like the project or thi
nk it's useful, please leave a star on the [repo](https://github.com/ajac-zero/mock-ai)!
```
---

     
 
all -  [ Why is nobody talking about recursive task decomposition. ](https://www.reddit.com/r/LangChain/comments/1hf1ang/why_is_nobody_talking_about_recursive_task/) , 2024-12-16-0914
```
Im researching the possibilities of integrating LLMs for pentesting. I researched many architecture and the one that con
viced me the most is recursive task decomposition. It is the most convincing architecture to me, yet nobody is talking a
bout it. Pentesting for me is just a way to test the agents capabilities, but for me if we can correctly decompose a tas
k recursively into subtaskks esay enough, every task would be doable. From pentesting, to playing games, to solving prob
lems,....
Every body is focusing on making niche agents  to execute specifics kind of task but nobody is thinking about 
something more generic. Look at LLMs , they weren't made for juste one specific topic, , they do all sort of things. I w
onder why nobody is doing this. 
Does anybody have an opinion on this?

```
---

     
 
all -  [ New to Coding Help - LangChain chat bot - stuck for 3 days ](https://www.reddit.com/r/LangChain/comments/1hey2bo/new_to_coding_help_langchain_chat_bot_stuck_for_3/) , 2024-12-16-0914
```
Hi guys, i thought of something I wanted to build a couple weeks ago so ive been learning to code and heavily relying on
 cursor. everything has been going fine until now. I have the code for a functional langchain chat bot. i know its funct
ional becuase it works in emulator. but when I deploy it it doesn't work. it throws a cors error but nothing ive tried f
or 3 days has resolved it. Ive had to hard reset from git twice now. i cant imagine its a complex issue. i just assume t
hat my lack of foundational coding knowledge is blocking me from fixing it. would any one have any idea whats going on? 
or have questions I can answer that would help get to a solution?   
im using firebase as my backend so its firebase emu
lator im working with and firebase deployment. 

to anyone that ends up trying to help, thank you 🙏
```
---

     
 
all -  [ Which vision model do you use for embeddings for vision rag? ](https://www.reddit.com/r/LangChain/comments/1hethzo/which_vision_model_do_you_use_for_embeddings_for/) , 2024-12-16-0914
```
Which model do you all use for vision embeddings other than colpali based or is it the best? Would like to know both fre
e and paid ways
```
---

     
 
all -  [ [For Hire] Skilled Full Stack Developer, AI/ML Expert, and DevOps Pro – Let’s Build Your Next Game-C ](https://www.reddit.com/r/forhire/comments/1hesz9z/for_hire_skilled_full_stack_developer_aiml_expert/) , 2024-12-16-0914
```
🚀 **Full Stack Developer | AI/ML Engineer | DevOps Specialist – Open for Hire!**

Hi there! I'm Sheryar 👋, a passionate 
developer with the skills and experience to bring your vision to life. Here's what I bring to the table:

# 💻 Full Stack
 Development Expertise

* **Frontend:** React | Angular
* **Backend:** Node.js | NestJS
* **Payments:** Seamless Stripe 
Integrations
* **Cloud Services:** AWS | GCP

# 🤖 AI & Machine Learning Innovations

* Smart Chatbots built with LangCha
in
* Custom NLP models for automation and insights

# ⚙️ DevOps Solutions for Scalable Systems

* **CI/CD Pipelines:** G
itHub Actions | Jenkins
* **Containerization:** Docker | Kubernetes
* **Infrastructure as Code:** Terraform | Ansible

#
 🌟 Notable Projects

* 🚗 **Ride-Sharing App:** Real-time tracking & payment flows
* 📦 **Logistics Platform:** Route opti
mization for multi-stop deliveries
* 🛒 **E-Commerce Infrastructure:** Scalable Kubernetes clusters

# 💰 Rates

* $10–$15
/hour (negotiable based on project scope)

📧 **DM me to discuss your project needs!**  
🔗 **GitHub:** [storm1033](https:
//github.com/storm1033)

Let’s collaborate and turn your ideas into reality! 🌟
```
---

     
 
all -  [ What is your python stack? ](https://www.reddit.com/r/ExperiencedDevs/comments/1hes05o/what_is_your_python_stack/) , 2024-12-16-0914
```
Many of the libraries, concepts and design patterns have been understood by me in practice. when entering a new project,
 or when I am faced with a problem for my existing stack, I tend to search the web for 'how do I do X' or ask colleagues
 for pointers. I figured I'd make a post where people denote the stack they use for different workflows and what problem
s that stack solves. I'll start!

APIs:

- FastAPI as the base
- Strict Pydantic validation across the entire app helps 
me work more structured and catch errors easier
- SQLAlchemy as the sql adapter if needed. I make a base CRUD class in s
qlalchemy then make CRUD pydantic classes for required inputs and output schemas, then make individual classes for each 
db model along with unique methods for querying
- Tenacity for retries
- Celery for task orchestration and execution alt
hough there's a new player in town called Prefect. For pure workflow orchestration you could also use DAG based tools li
ke Dagster, Argo and Airflow although I haven't used these outside the context of a kube cluster and i don't enjoy worki
ng with those. You can also use fastapi background tasks in place of celery but I'm not familiar with it and it's limita
tions 
- Webhooks for managing events and routing. I use hookdeck personally
- Firestore for when im not feeling like us
ing sql or the data is primarily JSON based. You can create listeners on cloud functions but be careful of race conditio
ns.
- Cloud run for hosting the api
- gitlab for the repo cause it let's me have an integrated cicd platform without nee
ding to use extensions plus the UI is nicer for me
- Redis to handle queues, I don't like working with rabbitmq for this

- Celery and cloud run don't work together, so the Celery workers need to be on a VM while the API can be on cloud run.
 People also use cloud tasks for celery but haven't looked into that


Specific services for different tasks:

LLMs:
- P
ortkey as the entry point for all LLM calls. I use a long config to define fallback behavior and retries and guardrails 
for prompt injection 
- Deepinfra and Fireworks as the AI providers
- Actively avoid all langchain implementations inclu
ding langsmith and langgraph and build this out myself if needed.

Scraping:
- Scrapingbee because these guys were the m
ost reliable for web scraping
- Proxycurl for linkedin Scraping
- Data Ocean on rapid api for crunchbase Scraping
- To g
et the news I use newspaper, which is an unofficial google news package. it works decently 
- SerperAPI for google searc
hes

This stack has allowed me to make apps that people pay money for, which is neat. I'm sure I'll think of other stuff
 in the future so will be editing this post

```
---

     
 
all -  [ Need help with selecting a good LLM ](https://www.reddit.com/r/LLMDevs/comments/1hepy6n/need_help_with_selecting_a_good_llm/) , 2024-12-16-0914
```
Hello, I'm making a project where every user has 10k input tokens and 400 output tokens worth of interaction at least 20
0 times a month. The project is for general use(Like general knowledge question,  or generating mathematical questions).
 Basically, it won't be much related to programming so IK claude isn't the best option.

I'm super new to all these LLM 
API's, so can someone guide me on the best cost-efficient api I can buy and integrate into my project? It'd also be real
ly helpful if it supports Langchain
```
---

     
 
all -  [ RAG on excel files ](https://www.reddit.com/r/LangChain/comments/1hen4ds/rag_on_excel_files/) , 2024-12-16-0914
```
Hey guys I’m currently tasked with working on rag for several excel files and I was wondering if someone has done someth
ing similar in production already. I’ve seen PandasAI but not sure if I should go for it or if theres a better alternati
ve. I have about 50 excel files.

Also if you have pushed to production, what were the issues you faced? Thanks in advan
ce
```
---

     
 
all -  [ struggling to understand the langgraph tutorial (build a basic chatbot) ](https://www.reddit.com/r/LangChain/comments/1heg7pi/struggling_to_understand_the_langgraph_tutorial/) , 2024-12-16-0914
```
link: [https://langchain-ai.github.io/langgraph/tutorials/introduction/#part-1-build-a-basic-chatbot](https://langchain-
ai.github.io/langgraph/tutorials/introduction/#part-1-build-a-basic-chatbot)

So far I am able to follow this tutorial f
or the 'build chatbot section' - what I don't understand is the logic in the 'while True' statement below - specifically
 on how the excelption logic is invoked:

  
`while True:`  
`try:`  
`user_input = input('User: ')`  
`if user_input.lo
wer() in ['quit', 'exit', 'q']:`  
`print('Goodbye!')`  
`break`  
  
`stream_graph_updates(user_input)`  
`except:`  
`
# fallback if input() is not available`  
`user_input = 'What do you know about LangGraph?'`  
`print('User: ' + user_in
put)`  
`stream_graph_updates(user_input)`  
`break`

  


Question :    exception logic trigger - how does it get trigg
ered? 

If you look at the tutorial, it is showing the results of executing the exception logic -  

`Assistant: LangGra
ph is a library designed to help build stateful multi-agent applications using language models. It provides tools for cr
eating workflows and state machines to coordinate multiple AI agents or language model interactions. LangGraph is built 
on top of LangChain, leveraging its components while adding graph-based coordination capabilities. It's particularly use
ful for developing more complex, stateful AI applications that go beyond simple query-response interactions.`  
Goodbye!




How does the execution logic  get triggered?  




```
---

     
 
all -  [ Do we have anything to replicate livekit agents voice capabilities with langgraph? ](https://www.reddit.com/r/LangChain/comments/1heed8a/do_we_have_anything_to_replicate_livekit_agents/) , 2024-12-16-0914
```
I am working on a voice agent that needs to have as low latency as possible with the speech-text-speech pipeline. (I am 
not going for multimodal realtime apis like the one of openai and recently released gemini 2.0 flash because they are co
stly and in beta as well as closed source). 

I want to make as many things on opensource as possible.

I first looked i
nto livekit which is opensource webrtc framework . which also has agents , these agents are pretty fast with a lot of op
timizations in the streaming pipeline. Now the issue with this is that agent framework of livekit is pretty basic with f
unction calling, i was looking for something more like langgraph and in best case scenario a langraph integration with l
ivekit.

On a similar note i looked at pipecat as well which also has pipecat flow to simulate decent flows somewhat lik
e langgraph while also being optimized for voice capabilites. The issue wth pipecat is that although it is opensource it
self, it only fully supports daily as a transport layer (something like livekit transport integration is in progress but
 even then i would prefer if instead of pipecat flows i could use something like langraph with good voice capabilities)


I wanted to ask for any suggestions on how to go about this problem. Thanks.
```
---

     
 
all -  [ Is this Langgraph chatbot worth it? ROAST ME ](https://www.reddit.com/r/LangChain/comments/1hee7f1/is_this_langgraph_chatbot_worth_it_roast_me/) , 2024-12-16-0914
```
Hi everybody,

I'm the founder of [**Chetty.ai**](http://Chetty.ai), an AI chatbot for websites.

Recently, I developed 
the first version of an agent in **Langgraph** to handle web searches in a more complex way. I already have ten major cu
stomers using this engine, so everything is fully operational and in production.

Could you please try it out and share 
your honest feedback? It's simple—just insert any website and ask about their services.

[https://chetty.ai/advanced-sea
rch-demo](https://chetty.ai/advanced-search-demo)

Thanks!
```
---

     
 
all -  [ I've built an MVP to level up your LangChain and AI skills - looking for feedback 🚀 ](https://www.reddit.com/r/LangChain/comments/1he8wiv/ive_built_an_mvp_to_level_up_your_langchain_and/) , 2024-12-16-0914
```
Hello LangChain and AI experts,

I'm building a free app to help users enhance their AI skills, including prompt enginee
ring, LangChain, Haystack, etc, and would like to see if it is useful for you.

What I've built:

* **Skill Trees:** Vis
ual guides to discover essential skills and concepts, specifically for Python developers working in advanced AI areas.
*
 **Quizzes:** Test your knowledge and identify gaps to improve your expertise in your focus areas.

I've built an MVP an
d would love your feedback to make this more useful, if you:

* Work with tools like LangChain,
* Dive into prompt engin
eering or Python AI/ML development,
* Or just want to see how this could help you grow.

**You’re welcome to try it out 
— It’s free:**

👉 [skill-up.io](https://www.skill-up.io/)

I hope it can be useful for you. If you like it, feel free to
 sign up to track your progress.

[AI and ML skill tree](https://preview.redd.it/nlovzr0q827e1.jpg?width=1080&format=pjp
g&auto=webp&s=55f7c0cdf1ed2915f0ce9a3f329cdac2780e3be9)

I appreciate your feedback:

* Is the skill tree structure help
ful for navigating complex topics?
* Are the quizzes relevant and engaging?
* What features would you me to add to solve
 your pain points when learning Python and related techs?

I’d love to help you more! Let me know what you need and I’ll
 build it. You can reach out by filling out [this form](https://www.notion.so/140ac95ae0208076972ef715f74c4429?pvs=21) o
r messaging me.
```
---

     
 
all -  [ Langchain Integration ](https://www.reddit.com/r/AIlice/comments/1he4oby/langchain_integration/) , 2024-12-16-0914
```
Love the project, separately have been exploring RAG set ups through langchain and wondering if people know any approach
es that can be used to integrate Allice with that efficiently? 
```
---

     
 
all -  [ How to make SqlAgent to query NoSQL for answers? ](https://www.reddit.com/r/learnmachinelearning/comments/1he3ebg/how_to_make_sqlagent_to_query_nosql_for_answers/) , 2024-12-16-0914
```
I am new to ML.

LangChain has that with relational databases. How to make it work with NoSQL databases?
```
---

     
 
all -  [ I am sharing ChatGPT & AI courses and projects on YouTube
 ](https://www.reddit.com/r/ChatGPT/comments/1hdyje8/i_am_sharing_chatgpt_ai_courses_and_projects_on/) , 2024-12-16-0914
```
Hello, I wanted to share that I am sharing free courses and projects on my YouTube Channel. I have more than 200 videos 
and I created playlists for learning Data Science. I am leaving the playlist link below, have a great day!

AI Tutorials
 (ChatGPT, LangChain & LLMs) -> [https://youtube.com/playlist?list=PLTsu3dft3CWhAAPowINZa5cMZ5elpfrxW&si=DvsefwOEJd3k-Sh
N](https://youtube.com/playlist?list=PLTsu3dft3CWhAAPowINZa5cMZ5elpfrxW&si=DvsefwOEJd3k-ShN)
```
---

     
 
all -  [ Frustrated. Should I change my career? ](https://www.reddit.com/r/technepal/comments/1hdwai2/frustrated_should_i_change_my_career/) , 2024-12-16-0914
```
Few years ago I started with Python. Until now I have learned almost eveything I felt required SQL, Pandas, Numpy, Matpl
otlib, Langchain, AWS, Fastapi, Tensorflow and many more. Still I am not even getting  glimpse of finding a job. Thought
 I could get into AI, ML, Data Science of not at least Data Analytics. I have contacted every person. Most of them tell 
that it's difficult to find internship in these fields. Without internship, how could I even start my professional life.
 Companies open vacancies for seniors. 

  At current, I am studying CSIT sixth sem. Most of you may think that it's too
 early. But what if I don't get job even after graduation. My college is useless. I don't even rely on it. Just thinking
 if it is better to go in web development with python or some other areas. If not, the last option that resorts is quick
ly head off to abroad. I see nothing to stay here.
```
---

     
 
all -  [ Made a simple processor for building systems like Anthropic's artifacts/v0.dev ](https://www.reddit.com/r/LangChain/comments/1hdufsv/made_a_simple_processor_for_building_systems_like/) , 2024-12-16-0914
```
Built this small tag processor after wanting to quickly prototype systems similar to Anthropic's artifacts or v0.dev. No
t trying to recreate them, just wanted something lightweight that lets you quickly build and experiment with similar ide
as.

Basic example:

    typescriptCopyconst processor = new FluffyTagProcessor();
    
    // Handle regular conversati
on
    processor.setUntaggedContentHandler(content => {
        console.log(content); 
    // Normal conversation flows

    });
    
    // Handle artifacts/special blocks
    processor.registerHandler('artifact', {
        handler: (attrs,
 content) => {
            createArtifact(attrs.type, content);
        }
    });

Works with streaming APIs out of the 
box, so you can build interactive systems that update in real-time. About 4KB, no dependencies.

Mainly sharing in case 
others want to experiment with similar systems. TypeScript and Python versions: [github repo](https://github.com/m-ahmed
-elbeskeri/FluffyTagProcessor/tree/main?tab=readme-ov-file)
```
---

     
 
all -  [ [Student] Non-Target CS Student looking for Summer 2025 Internships ](https://www.reddit.com/r/EngineeringResumes/comments/1hdpaec/student_nontarget_cs_student_looking_for_summer/) , 2024-12-16-0914
```
[I am having little luck with applying to Summer 2025 internships related to software engineering, and I've currently ap
plied to around 400 places. I know the market is pretty bad right now, but just wanted to make sure my resume was optima
l for getting me interviews, cause right now I have gotten mostly nothing from online applications \(Had an interview fr
om my school's career fair\). Any advice would be greatly appreciated.](https://preview.redd.it/qnc9d2sc7p6e1.png?width=
5100&format=png&auto=webp&s=68f0c23f6576eb216c1f4c5fdc6190e2aa9dba60)


```
---

     
 
all -  [ Modularizing AI workflows in production ](https://www.reddit.com/r/LangChain/comments/1hdm37i/modularizing_ai_workflows_in_production/) , 2024-12-16-0914
```
Wanted to share some challenges and solutions we discovered while working with complex prompt chains in production. We s
tarted hitting some pain points as our prompt chains grew more sophisticated:

* Keeping track of prompt versions across
 different chain configurations became a nightmare
* Testing different prompt variations meant lots of manual copying an
d pasting. Especially when tracking the performances.
* Deploying updated chains to production was tedious and error-pro
ne. Environment variables was fine at first until the list of prompts start to grow.
* Collaborating on prompt engineeri
ng with the team led to version conflicts.
   * We started with code verisoning it, but it was hard to loop in other sta
keholders (ex: product managers, domain experts) to do code reviews on GitHub. Notion doesn’t have a good versioning sys
tem built-in so everyone was kind of afraid to overwrite the other person’s work and ended up putting a lot of comments 
all over the place.

We ended up building a simple UI-based solution that helps us:

1. Visualize the entire prompt chai
n flow
2. Track different versions of the workflow and make them replayable.
3. Deploy the workflows as separate service
 endpoints in order to manage them programmatically in code

The biggest learning was that treating chained prompts like
 we treat workflows (with proper versioning and replayability) made a huge difference in our development speed.

Here’s 
a high-level diagram of how we modularize AI workflows from the rest of the services

https://preview.redd.it/4cwpce4uio
6e1.png?width=1612&format=png&auto=webp&s=a290f010d8605bec3e1825603e87665366e802c2

We’ve made our tool available at [ww
w.bighummingbird.com](http://www.bighummingbird.com/) if anyone wants to try it, but I’m also curious to hear how others
 are handling these challenges? :)
```
---

     
 
all -  [ Avoid sending messages at the same time ](https://www.reddit.com/r/LangChain/comments/1hdlx5e/avoid_sending_messages_at_the_same_time/) , 2024-12-16-0914
```
Hi,  
I have a graph on langgraph wrapped around a FastAPI project.  
I want to avoid sending two messages at the same t
ime to the same chat\_id through the API.  
Is there any way I can know when a thread is processing a message before sen
ding a new one?  
Thanks in advance!
```
---

     
 
all -  [ why my agent is not calling the tools  help me to fix this .. ](https://www.reddit.com/r/node/comments/1hdllox/why_my_agent_is_not_calling_the_tools_help_me_to/) , 2024-12-16-0914
```
mport dotenv from 'dotenv';  
dotenv.config();  
import { tool } from '@langchain/core/tools';  
import { z } from 'zod'
;  
import { ChatGoogleGenerativeAI } from '@langchain/google-genai';  
import { ChatPromptTemplate } from '@langchain/c
ore/prompts';  
import { AgentExecutor, createToolCallingAgent } from 'langchain/agents';  
import { TavilySearchResults
 } from '@langchain/community/tools/tavily\_search';

const llm = new ChatGoogleGenerativeAI({  
apiKey: process.env.GEM
INI,  
model: 'gemini-1.5-flash',  
});

const search = new TavilySearchResults({  
apiKey: process.env.TAVILY,  
maxRes
ults: 2,  
});

*// Improved magicTool: Now actually uses the input*  
const magicTool = tool(  
async (input) => {  
*/
/Simulate fetching company name - replace this with actual API call if needed.*

return 'The company name is Acme Corpor
ation.';  
},  
{  
name: 'business\_info',  
description:  
'This tool provides business information like name, locatio
n, etc. Ask specific questions.',  
}  
);

const tools = \[magicTool\];

const prompt = ChatPromptTemplate.fromMessages
(\[  
\[  
'system',  
'You are a helpful assistant that answers the following questions as best you can. You have acces
s to the following tools:',  
\],  
\['placeholder', '{chat\_history}'\],  
\['human', '{input}'\],  
\['placeholder', '
{agent\_scratchpad}'\],  
\]);

const agent = createToolCallingAgent({  
llm,  
tools,  
prompt,  
});

const agentexe =
 new AgentExecutor({  
agent,  
tools,  
verbose: true,  
});

const res = await agentexe.invoke({ input: 'what is the c
ompany name?' });  
console.log(res);
```
---

     
 
all -  [ why my agent is not calling the tools please help me to fix this  .. ](https://www.reddit.com/r/LangChain/comments/1hdksj8/why_my_agent_is_not_calling_the_tools_please_help/) , 2024-12-16-0914
```
import dotenv from 'dotenv';  
dotenv.config();  
import { tool } from '@langchain/core/tools';  
import { z } from 'zod
';  
import { ChatGoogleGenerativeAI } from '@langchain/google-genai';  
import { ChatPromptTemplate } from '@langchain/
core/prompts';  
import { AgentExecutor, createToolCallingAgent } from 'langchain/agents';  
import { TavilySearchResult
s } from '@langchain/community/tools/tavily\_search';  
  
const llm = new ChatGoogleGenerativeAI({  
  apiKey: process.
env.GEMINI,  
  model: 'gemini-1.5-flash',  
});  
  
const search = new TavilySearchResults({  
  apiKey: process.env.T
AVILY,  
  maxResults: 2,  
});  
  
*// Improved magicTool:  Now actually uses the input*  
const magicTool = tool(  
 
 async (input) => {  
*//Simulate fetching company name - replace this with actual API call if needed.*  
  
return 'The
 company name is Acme Corporation.';  
  },  
  {  
name: 'business\_info',  
description:  
'This tool provides busines
s information like name, location, etc.  Ask specific questions.',  
  }  
);  
  
const tools = \[magicTool\];  
  
con
st prompt = ChatPromptTemplate.fromMessages(\[  
  \[  
'system',  
'You are a helpful assistant that answers the follow
ing questions as best you can. You have access to the following tools:',  
  \],  
  \['placeholder', '{chat\_history}'\
],  
  \['human', '{input}'\],  
  \['placeholder', '{agent\_scratchpad}'\],  
\]);  
  
const agent = createToolCalling
Agent({  
  llm,  
  tools,  
  prompt,  
});  
  
const agentexe = new AgentExecutor({  
  agent,  
  tools,  
  verbos
e: true,  
});  
  
const res = await agentexe.invoke({ input: 'what is the company name?' });  
console.log(res);  
  

import dotenv from 'dotenv';  
dotenv.config();  
import { tool } from '@langchain/core/tools';  
import { z } from 'zod
';  
import { ChatGoogleGenerativeAI } from '@langchain/google-genai';  
import { ChatPromptTemplate } from '@langchain/
core/prompts';  
import { AgentExecutor, createToolCallingAgent } from 'langchain/agents';  
import { TavilySearchResult
s } from '@langchain/community/tools/tavily\_search';  
  
  
const llm = new ChatGoogleGenerativeAI({  
  apiKey: proce
ss.env.GEMINI,  
  model: 'gemini-1.5-flash',  
});  
  
  
const search = new TavilySearchResults({  
  apiKey: process
.env.TAVILY,  
  maxResults: 2,  
});  
  
  
// Improved magicTool:  Now actually uses the input  
const magicTool = to
ol(  
  async (input) => {  
//Simulate fetching company name - replace this with actual API call if needed.  
  
  
ret
urn 'The company name is Acme Corporation.';  
  },  
  {  
name: 'business\_info',  
description:  
'This tool provides
 business information like name, location, etc.  Ask specific questions.',  
  }  
);  
  
  
const tools = \[magicTool\
];  
  
  
const prompt = ChatPromptTemplate.fromMessages(\[  
  \[  
'system',  
'You are a helpful assistant that answ
ers the following questions as best you can. You have access to the following tools:',  
  \],  
  \['placeholder', '{ch
at\_history}'\],  
  \['human', '{input}'\],  
  \['placeholder', '{agent\_scratchpad}'\],  
\]);  
  
  
const agent = 
createToolCallingAgent({  
  llm,  
  tools,  
  prompt,  
});  
  
{  
  input: 'what is the company name?',  
  output
: 'I need more information to answer your question.  The available tools don't contain any information about a specific 
company.  Can you provide more context or details?\\n'  
}  
const agentexe = new AgentExecutor({  
  agent,  
  tools, 
 
  verbose: true,  
});  
  
  
const res = await agentexe.invoke({ input: 'what is the company name?' });  
console.lo
g(res);  
  
the output is  ::   
 {  
  input: 'what is the company name?',  
  output: 'I need more information to ans
wer your question.  The available tools don't contain any information about a specific company.  Can you provide more co
ntext or details?\\n'  
}
```
---

     
 
all -  [ why my agent is not calling the tools please help me to fix this  ,  ](https://www.reddit.com/r/Bard/comments/1hdkqi8/why_my_agent_is_not_calling_the_tools_please_help/) , 2024-12-16-0914
```
    import dotenv from 'dotenv';
    dotenv.config();
    import { tool } from '@langchain/core/tools';
    import { z }
 from 'zod';
    import { ChatGoogleGenerativeAI } from '@langchain/google-genai';
    import { ChatPromptTemplate } fro
m '@langchain/core/prompts';
    import { AgentExecutor, createToolCallingAgent } from 'langchain/agents';
    import { 
TavilySearchResults } from '@langchain/community/tools/tavily_search';
    
    const llm = new ChatGoogleGenerativeAI({

      apiKey: process.env.GEMINI,
      model: 'gemini-1.5-flash',
    });
    
    const search = new TavilySearchResu
lts({
      apiKey: process.env.TAVILY,
      maxResults: 2,
    });
    
    // Improved magicTool:  Now actually uses 
the input
    const magicTool = tool(
      async (input) => {
        
    //Simulate fetching company name - replace t
his with actual API call if needed.
    
        return 'The company name is Acme Corporation.';
      },
      {
      
  name: 'business_info',
        description:
          'This tool provides business information like name, location, et
c.  Ask specific questions.',
      }
    );
    
    const tools = [magicTool];
    
    const prompt = ChatPromptTempl
ate.fromMessages([
      [
        'system',
        'You are a helpful assistant that answers the following questions a
s best you can. You have access to the following tools:',
      ],
      ['placeholder', '{chat_history}'],
      ['huma
n', '{input}'],
      ['placeholder', '{agent_scratchpad}'],
    ]);
    
    const agent = createToolCallingAgent({
   
   llm,
      tools,
      prompt,
    });
    
    const agentexe = new AgentExecutor({
      agent,
      tools,
     
 verbose: true,
    });
    
    const res = await agentexe.invoke({ input: 'what is the company name?' });
    console.
log(res);
    
    import dotenv from 'dotenv';
    dotenv.config();
    import { tool } from '@langchain/core/tools';
 
   import { z } from 'zod';
    import { ChatGoogleGenerativeAI } from '@langchain/google-genai';
    import { ChatPromp
tTemplate } from '@langchain/core/prompts';
    import { AgentExecutor, createToolCallingAgent } from 'langchain/agents'
;
    import { TavilySearchResults } from '@langchain/community/tools/tavily_search';
    
    
    const llm = new Chat
GoogleGenerativeAI({
      apiKey: process.env.GEMINI,
      model: 'gemini-1.5-flash',
    });
    
    
    const sear
ch = new TavilySearchResults({
      apiKey: process.env.TAVILY,
      maxResults: 2,
    });
    
    
    // Improved 
magicTool:  Now actually uses the input
    const magicTool = tool(
      async (input) => {
        //Simulate fetching
 company name - replace this with actual API call if needed.
    
    
        return 'The company name is Acme Corporat
ion.';
      },
      {
        name: 'business_info',
        description:
          'This tool provides business infor
mation like name, location, etc.  Ask specific questions.',
      }
    );
    
    
    const tools = [magicTool];
    

    
    const prompt = ChatPromptTemplate.fromMessages([
      [
        'system',
        'You are a helpful assistan
t that answers the following questions as best you can. You have access to the following tools:',
      ],
      ['place
holder', '{chat_history}'],
      ['human', '{input}'],
      ['placeholder', '{agent_scratchpad}'],
    ]);
    
    
 
   const agent = createToolCallingAgent({
      llm,
      tools,
      prompt,
    });
    
    {
      input: 'what is
 the company name?',
      output: 'I need more information to answer your question.  The available tools don't contain 
any information about a specific company.  Can you provide more context or details?\n'
    }
    const agentexe = new Ag
entExecutor({
      agent,
      tools,
      verbose: true,
    });
    
    
    const res = await agentexe.invoke({ i
nput: 'what is the company name?' });
    console.log(res);
    
    the output is  :: 
     {
      input: 'what is the
 company name?',
      output: 'I need more information to answer your question.  The available tools don't contain any 
information about a specific company.  Can you provide more context or details?\n'
    }
```
---

     
 
all -  [ Advance Your Career: 100 Free Certified Courses on Udemy ](https://www.reddit.com/r/Udemy/comments/1hdjv70/advance_your_career_100_free_certified_courses_on/) , 2024-12-16-0914
```
Visualization techniques for Decision Makers and Leaders

https://courze.org/visualization-techniques-for-decision-maker
s-and-leaders/



300+ JavaScript Interview Questions – Practice Tests

https://courze.org/300-javascript-interview-ques
tions-practice-tests/



300+ Python Interview Questions – Practice Tests

https://courze.org/300-python-interview-quest
ions-practice-tests/



Scrum Master Certification

https://courze.org/scrum-master-certification-4/



Business Analysi
s

https://courze.org/business-analysis/



C Corporation Income Tax (Form 1120)

https://courze.org/c-corporation-incom
e-tax-form-1120/



Zero to Hero in LangChain: Build GenAI apps using LangChain

https://courze.org/zero-to-hero-in-lang
chain-build-genai-apps-using-langchain/



Blogger: Make A Professional Website For Free With No Coding

https://courze.
org/blogger-make-a-professional-website-for-free-with-no-coding/



Solving LeetCode’s Top Interview Questions in Java \
[2024\]

https://courze.org/solving-leetcodes-top-interview-questions-in-java/



4 Comprehensive Practice Tests for any
 Python Certification

https://courze.org/4-comprehensive-practice-tests-for-any-python-certification/



Excel Certific
ation Exam Preparation: 4 Practice Tests 2024

https://courze.org/excel-certification-exam-preparation-4-practice-tests-
2024-3/



4 MS Excel Certification Practice Test & Interview Question

https://courze.org/4-ms-excel-certification-prac
tice-test-interview-question/



CHRO Chief Human Resources Officer Executive Certification

https://courze.org/chro-chi
ef-human-resources-officer-executive-certification/



Prioritization Techniques for Decision Makers and Leaders

https:
//courze.org/prioritization-techniques-for-decision-makers-and-leaders/



The Complete Matlab Course for Wireless Comm.
 Engineering

https://courze.org/the-complete-matlab-course-for-wireless-comm-engineering/



Currency Management for Sm
all Businesses & Corporates

https://courze.org/currency-management-for-small-businesses-corporates/



Statistics & Exc
el

https://courze.org/statistics-excel/



Prompt & AI Engineering Safety Professional Certification

https://courze.or
g/prompt-engineering-safety-ai-engineering-safety-expert/



ChatGPT Prompt Engineering Guide: Make Money Using ChatGPT


https://courze.org/chatgpt-prompt-engineering-guide-make-money-using-chatgpt/



AI Course Creation Guide: Creating an 
Online Course Using AI

https://courze.org/ai-course-creation-guide-creating-an-online-course-using-ai/



Advanced Skil
l Test: Python Professional Level 1 (PCPP1™)

https://courze.org/advanced-skill-test-python-professional-level-1-pcpp1-2
/



Advanced Skill Test: Python Professional Level 1 (PCPP1™)

https://courze.org/advanced-skill-test-python-profession
al-level-1-pcpp1-7/



Advanced Skill Test: Python Professional Level 1 (PCPP1™)

https://courze.org/advanced-skill-test
-python-professional-level-1-pcpp1-9/



Advanced Skill Test: Python Professional Level 1 (PCPP1™)

https://courze.org/a
dvanced-skill-test-python-professional-level-1-pcpp1-10/



Advanced Skill Test: Python Professional Level 1 (PCPP1™)

h
ttps://courze.org/advanced-skill-test-python-professional-level-1-pcpp1-12/



Advanced Skill Test: Python Professional 
Level 1 (PCPP1™)

https://courze.org/advanced-skill-test-python-professional-level-1-pcpp1-15/



7 steps to entrepreneu
rship: A complete business plan (PRO)

https://courze.org/7-steps-to-entrepreneurship-a-complete-business-plan-pro/



A
utoCAD 2D & Isometric | AutoCAD Civil & Architectural

https://courze.org/autocad-2d-isometric-autocad-civil-architectur
al/



Microsoft Power BI for Beginners & Excel Users

https://courze.org/microsoft-power-bi-for-beginners-excel-users/




CMO Chief Marketing Officer Executive Certification

https://courze.org/cmo-chief-marketing-officer-executive-certifi
cation/



Transform Your Life in 5 Days: I Challenge You to Fail

https://courze.org/transform-your-life-in-5-days-i-ch
allenge-you-to-fail/



Mastering Power BI Report Design – Beginner to Advanced

https://courze.org/mastering-power-bi-r
eport-design-beginner-to-advanced/



Practical Machine Learning for Data Scientists

https://courze.org/practical-machi
ne-learning-for-data-scientists/



Generative AI: Learn about the next AI frontier

https://courze.org/generative-ai-le
arn-about-the-next-ai-frontier/



Master LCD Interfacing with Arduino: From Basics to Projects

https://courze.org/mast
er-lcd-interfacing-with-arduino-from-basics-to-projects/



Deployment of Machine Learning Models

https://courze.org/de
ployment-of-machine-learning-models/



Reinforcement Learning

https://courze.org/reinforcement-learning/



Deep Learn
ing for Computer Vision

https://courze.org/deep-learning-for-computer-vision/



Deep Learning for Natural Language Pro
cessing

https://courze.org/deep-learning-for-natural-language-processing/



Oracle Java Certification Exam OCA 1Z0-808
 Preparation Part1

https://courze.org/oracle-java-certification-exam-oca-1z0-808-preparation-part1/




```
---

     
 
all -  [ Direct OpenAI API vs. LangChain: A Performance and Workflow Comparison
 ](https://www.reddit.com/r/OpenSourceeAI/comments/1hdgunu/direct_openai_api_vs_langchain_a_performance_and/) , 2024-12-16-0914
```
Choosing between OpenAI’s API and LangChain can be tricky. In my latest blog, we explore:

* Why the Direct API is faste
r (hint: fewer layers).
* How LangChain handles complex workflows with ease.
* The trade-offs between speed, simplicity,
 and flexibility

Blog Link: [https://blogs.adityabh.is-a.dev/posts/langchain-vs-openai-simplicity-vs-scalability/](http
s://blogs.adityabh.is-a.dev/posts/langchain-vs-openai-simplicity-vs-scalability/)

If you’ve ever wondered when to stick
 with the Direct API and when LangChain’s extra features make sense, this is for you! Check it out for a deep dive into 
performance, bottlenecks, and use cases.

Let’s discuss: Which tool do you prefer, and why? 🤔
```
---

     
 
all -  [ Langgraph Persistence memory: InvalidSqlStatementName ](https://www.reddit.com/r/LangChain/comments/1hdbvre/langgraph_persistence_memory/) , 2024-12-16-0914
```
    async def run_graph(user_input: str, thread_id: str):
        with AsyncConnection.connect(os.getenv('DB_URI'), **co
nnection_kwargs) as conn:
            checkpointer = AsyncPostgresSaver(conn)
            await checkpointer.setup()
   
         graph = workflow.compile(checkpointer=checkpointer)
            config = {'configurable': {'thread_id': thread_
id}}
            async for event in graph.astream_events(
                {'messages': [HumanMessage(content=user_input)
]},
                version = 'v2', stream_mode='values', config=config
            ):
                if 'on_chat_model
_stream' == event['event']:
                    if len(event['data']['chunk'].content) > 0:
                        prin
t(event['data']['chunk'].content, end='', flush=True)
    
    if __name__ == '__main__':
        print('Running model')

        asyncio.run(run_graph(user_input='How are you?', thread_id='testing5'))

`DB_URI= postgresql://USER:PASSWORD@aw
s-0-eu-central-1.pooler.supabase.com:6543/postgres?sslmode=disable`

I am using above code for `react-agent` with `memor
y`. Without `memory`, agent is working fine but when I add memory to it then sometime it gives me this error and sometim
e it works fine. I am not sure what could be wrong.

`psycopg.errors.InvalidSqlStatementName: prepared statement '_pg3_1
4' does not exist`
```
---

     
 
all -  [ A Personalized Academic Companion - AI Agent ](https://open.substack.com/pub/diamantai/p/atlas-when-artificial-intelligence?r=336pe4&utm_campaign=post&utm_medium=web&showWelcomeOnShare=false) , 2024-12-16-0914
```
During the hackathon I ran with LangChain, a team of developers created ATLAS—a system of AI agents designed to help stu
dents tackle the overwhelming challenges of modern education. From optimizing study schedules to tailoring learning reso
urces, ATLAS provides personalized support to make studying more effective and less stressful.

I shared the full story,
 along with insights into how it works, in the blog attached (including also a link to the full code tutorial + YouTube 
pitch video)

Curious to hear your thoughts :)
```
---

     
 
all -  [ How to extract Title/Heading/Chapter Name from the PDF ](https://www.reddit.com/r/LangChain/comments/1hdbeeo/how_to_extract_titleheadingchapter_name_from_the/) , 2024-12-16-0914
```
I am working on a RAG Pipeline, in which I am extracting PDF and store in the mongo. When I perform a query, it responds
 with a specific answer. Now I want to add Page Number and Title OR Chapter name OR heading of the title in the response
.

I am trying to fetch but it is not that much accurate. Anyone having a good approach ?
```
---

     
 
all -  [ What is best practice for follow-up questions? ](https://www.reddit.com/r/Rag/comments/1hdaf2y/what_is_best_practice_for_followup_questions/) , 2024-12-16-0914
```
I am implementing Ai agent, and feeding it with some scraped data, i am using Langchain alongside with express.js, from 
your experience what is low cost and effective solution to handle follow up questions in rag? I read langchain docs but 
they are suggesting to make another LLM call which may be costly, is there any appropriate practice for it which really 
works, please share your experience, any material or web resource will be appreciated 
```
---

     
 
all -  [ Qdrant DB Retriever issue ](https://www.reddit.com/r/LangChain/comments/1hd9oz8/qdrant_db_retriever_issue/) , 2024-12-16-0914
```
Previously I have used Chroma DB now I wold like to use Qdrant db

I have uploaded my docs to qdrant db using qdrant cli
ent through langchain framework, created a collection name and assigned hugging face embedding model now now I’m not abl
e to retrieve the query using .query method which was previously used in chroma DB I would like to know different modes 
of search’s supported by qdrantvectorstore

can any one guide me or share any links 
```
---

     
 
all -  [ How to return tool output directly without sending it to LLM again from a Langgraph Agent ? ](https://www.reddit.com/r/LangChain/comments/1hd9cc4/how_to_return_tool_output_directly_without/) , 2024-12-16-0914
```
A typical ReAct loop follows user -> assistant -> tool -> assistant ..., -> user. In some cases, you don't need to call 
the LLM after the tool completes, the user can view the results directly themselves.

I am currently developing a Langgr
aph Agent ( this [https://langchain-ai.github.io/langgraph/#example](https://langchain-ai.github.io/langgraph/#example) 
is the base ) .

For my agent , I have 2 tools for calling 2 apis.  
  
Results from these 2 tool calls can be large...v
ery large some times depending on the user query.

I want that the tool outputs ( i.e. the api response ) instead of goi
ng back to the agent , it should be returned directly to the user.

I found a Langchain JS reference for this ( [https:/
/langchain-ai.github.io/langgraphjs/how-tos/dynamically-returning-directly/](https://langchain-ai.github.io/langgraphjs/
how-tos/dynamically-returning-directly/) ) but I'm developing using Python. Can anyone guide me how to directly return t
he tool outputs to the user ?

My app is a streamlit app. Thanks!
```
---

     
 
all -  [ Direct OpenAI API vs. LangChain: A Performance and Workflow Comparison
 ](https://www.reddit.com/r/OpenAI/comments/1hd6x21/direct_openai_api_vs_langchain_a_performance_and/) , 2024-12-16-0914
```
Choosing between OpenAI’s API and LangChain can be tricky. In my latest blog, we explore:

* Why the Direct API is faste
r (hint: fewer layers).
* How LangChain handles complex workflows with ease.
* The trade-offs between speed, simplicity,
 and flexibility.

Blog link: [https://blogs.adityabh.is-a.dev/posts/langchain-vs-openai-simplicity-vs-scalability/](htt
ps://blogs.adityabh.is-a.dev/posts/langchain-vs-openai-simplicity-vs-scalability/)

If you’ve ever wondered when to stic
k with the Direct API and when LangChain’s extra features make sense, this is for you! Check it out for a deep dive into
 performance, bottlenecks, and use cases.

Let’s discuss: Which tool do you prefer, and why? 🤔
```
---

     
 
all -  [ Direct OpenAI API vs. LangChain: A Performance and Workflow Comparison ](https://www.reddit.com/r/LangChain/comments/1hd6w5x/direct_openai_api_vs_langchain_a_performance_and/) , 2024-12-16-0914
```
Choosing between OpenAI’s API and LangChain can be tricky. In my latest blog, we explore:

* Why the Direct API is faste
r (hint: fewer layers).
* How LangChain handles complex workflows with ease.
* The trade-offs between speed, simplicity,
 and flexibility

Blog Link: [https://blogs.adityabh.is-a.dev/posts/langchain-vs-openai-simplicity-vs-scalability/](http
s://blogs.adityabh.is-a.dev/posts/langchain-vs-openai-simplicity-vs-scalability/)

If you’ve ever wondered when to stick
 with the Direct API and when LangChain’s extra features make sense, this is for you! Check it out for a deep dive into 
performance, bottlenecks, and use cases.

Let’s discuss: Which tool do you prefer, and why? 🤔
```
---

     
 
all -  [ AI Companion ](https://www.reddit.com/r/LangChain/comments/1hd6fo6/ai_companion/) , 2024-12-16-0914
```
We trying to develop a bot for people to talk when feeling lonely. I came by such a bot which is already very popular na
med Replica. Is there any other such bots which are already in use? Anyone knows which latest LLM Replica is using in th
e backend?
```
---

     
 
all -  [ My ideal development wishlist for building AI apps ](https://www.reddit.com/r/LangChain/comments/1hd62k6/my_ideal_development_wishlist_for_building_ai_apps/) , 2024-12-16-0914
```
As I reflect on what I’m building now and what I have built over the last 2 years I often go back to this list I made a 
few months ago.  

Wondering if anyone else relates 


It’s straight copy/paste from my notion page but felt worth shari
ng 


- I want an easier way to integrate AI into my app from what everyone is putting out on jupyter notebooks
    - no
tebooks are great but there is so much overhead in trying out all these new techniques. I wish there was better tooling 
to integrate it into an app at some point. 
- I want some pre-bundled options and kits to get me going
- I want SOME con
trol over the AI server I’m running with hooks into other custom systems.
- I don’t want a Low/no Code solution, I want 
to have control of the code
- I want an Open Source tool that works with other open source software. No vendor lock in
-
 I want to share my AI code easily so that other application devs can test out my changes. 
- I want to be able to run e
valuations and other LLMOps features directly
    - evaluations
    - lifecycle
    - traces
- I want to deploy this eas
ily and work with my deployment strategies
- I want to switch out AI techniques easily so as new ones come out, I can se
e the benefit right away
- I want to have an ecosystem of easy AI plugins I can use and can hook onto my existing server
. Can be quality of life, features, stand-alone applications 
- I want a runtime that can handle most of the boilerplate
 of running a server. 
```
---

     
 
all -  [ Aider + langchain: A match made in heaven? ](https://www.reddit.com/r/LocalLLaMA/comments/1hczbla/aider_langchain_a_match_made_in_heaven/) , 2024-12-16-0914
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

     
 
all -  [ Token limit challenge with large tool/function calling response ](https://www.reddit.com/r/LangChain/comments/1hcwrzk/token_limit_challenge_with_large_toolfunction/) , 2024-12-16-0914
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

     
 
all -  [  CommanderAI / LLM-Driven Action Generation on Windows with Langchain (openai) ](https://www.reddit.com/r/OpenAIDev/comments/1hcwok1/commanderai_llmdriven_action_generation_on/) , 2024-12-16-0914
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

     
 
all -  [ multi RAG issue ](https://www.reddit.com/r/LangChain/comments/1hcvpmy/multi_rag_issue/) , 2024-12-16-0914
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

     
 
MachineLearning -  [ [P] Minima: local conversational retrieval augmented generation project (Ollama, Langchain, FastAPI, ](https://www.reddit.com/r/MachineLearning/comments/1h1pudq/p_minima_local_conversational_retrieval_augmented/) , 2024-12-16-0914
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

     
