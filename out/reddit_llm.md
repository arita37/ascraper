 
all -  [ Comparing autogen and crewai for a marketing automation project ](https://www.reddit.com/r/LangChain/comments/1frrf52/comparing_autogen_and_crewai_for_a_marketing/) , 2024-09-29-0914
```
I've been thinking for a while to compare different agents frameworks. As I'm currently working on a marketing automatio
n project so decided to do it comparing autogen and crewai. Here is my first attempt at both [https://youtu.be/gTXODqVI7
kQ](https://youtu.be/gTXODqVI7kQ)

The code is available here: [https://github.com/alinaqi/CampaignGPT](https://github.c
om/alinaqi/CampaignGPT)

Here is the summary:  
CrewAI while interesting has strange abstractions and for anything serio
us, it quickly becomes a bit difficult to work with.   
AutoGen seems to be a lot easier and worked quite well. I will b
e using it to continue with the project. 

WDYT? 
```
---

     
 
all -  [ Methods to implement web search, I'll share mine and would love to read yours ](https://www.reddit.com/r/ChatGPTCoding/comments/1frpsem/methods_to_implement_web_search_ill_share_mine/) , 2024-09-29-0914
```
I opted to write my own because I prefer to have full control over the actions taken. In my experience using LangChain i
n the past just made debugging quite cumbersome due to most of the action occurring 'under the hood' so to speak (this c
ould also be due to lack of experience).

1. The AI generates the search query via function calling from the conversatio
n request from the user. I'm using gpt-4o for this part. This query is the only input to the function. The system prompt
 for the AI provides it with the current date, so it often uses this in the query when searching for time sensitive info
 such as news.
2. Using [googleapis.com](http://googleapis.com) with the aiohttp library to pull the top 10 results for 
the query.
3. For each URL returned, text is scraped using beautiful soup library and passing it through gpt-4o-mini to 
have it summarized against the query. I found that I had to add this step due to exceeding the context window on some se
arch queries.
4. All summaries are aggregated, along with the website title and URLs (so the AI can cite sources) and pa
ssed back to the AI model that made the function call.  This usually ends up being between 1200-2000 tokens of informati
on.

It's been working quite well so far, although occasionally I get 403 errors from certain sites. I've implemented he
aders to help with that but can't seem to find a combo that works 100% of the time. I'm running steps 3 & 4 asynchronous
ly so it doesn't take much time, especially when combined with 4o mini.

A couple neat things I found while playing arou
nd with this:

* I found if I ask it to search a specific site, it appends 'site: reddit.com' for example to the end of 
the search query and pulls results only from that site.  I thought that was cool of it to use its native knowledge on ho
w search queries work.
* I asked it to give me a parts list with pricing for the most top end gaming PC currently and it
 did searches to find out the best parts, then searched for pricing on each, and finally created a pretty slick breakdow
n of compatible parts and their prices with URLs.  It just looped through calling the search function until it had all o
f the info needed.

I'd love to hear how you may have implemented internet search as well as use cases you may have foun
d for it.  My business use case will be to assist techs and engineers with finding solutions to problems online after th
e chatbot parses their service ticket symptoms, issues, troubleshooting performed, etc.
```
---

     
 
all -  [ List of FREE and Best Selling Discounted Courses ](https://www.reddit.com/r/udemyfreeebies/comments/1frotr3/list_of_free_and_best_selling_discounted_courses/) , 2024-09-29-0914
```
# Udemy Free Courses for 29 September 2024

Note : Coupons might expire anytime, so enroll as soon as possible to get th
e courses for FREE.

* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/16503/)Core Java and Coding for Automation Test
ers – For Beginners
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/16502/)Desarrollo Web: HTML, CSS Y JS : Front En
d Web Development
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/16501/)Software Career Bootcamp: Recession, Layoff
 and AI Challenge
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/16500/)Microservicios Spring Boot, Spring Cloud Ne
tflix Eureka 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/16499/)Blueprint For Successful Microservices & AP
I Implementation
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/16498/)React & Spring Boot: Creando Webapp Full Sta
ck 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/16497/)Prevención Lavado de Dinero ALD y Programa de Cumplim
iento
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/16496/)Mindful Stress Management: Master Emotional Control Tod
ay
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/16495/)Master 20 Practical Leadership Skills for Corporate Succes
s
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/16494/)Master Public Speaking: 23 Tips for Workplace Presentations

* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/16493/)Gain 8 Essential Skills For Complete Personal Transformation

* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/16492/)Criptomonedas : Delitos Financieros y Cumplimiento ALD / CFT

* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/16491/)Assertiveness 101: Become More Assertive in Just 90 Minutes

* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/16490/)Virtual Meetings with Confidence: 90-minute Confidence Guide

* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/16489/)Body Language in Business: Gain Confidence & Read Others
* [R
EDEEM OFFER ](https://idownloadcoupon.com/udemy/16488/)Presentation Skills & Public Speaking: Complete Masterclass
* Tim
e Management & Productivity: Stress Less, Accomplish More
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/16487/)
* [
REDEEM OFFER ](https://idownloadcoupon.com/udemy/16486/)Gain Practical Communication Skills with this Complete Guide
* [
REDEEM OFFER ](https://idownloadcoupon.com/udemy/16485/)Diseño de Sistemas de Alarma contra Incendio basado NFPA 72
* [R
EDEEM OFFER ](https://idownloadcoupon.com/udemy/16484/)Learn Fundamentals and Basics of Spring boot
* [REDEEM OFFER ](ht
tps://idownloadcoupon.com/udemy/16483/)System Design (LLD + HLD) from Basics to Advanced
* [REDEEM OFFER ](https://idown
loadcoupon.com/udemy/16482/)CCSP Cloud Security Professional Complete Training – 2024
* [REDEEM OFFER ](https://idownloa
dcoupon.com/udemy/16481/)Diffusion Mastery: Flux, Stable Diffusion, Midjourney & more
* [REDEEM OFFER ](https://idownloa
dcoupon.com/udemy/16480/)Learn Shop drawing: from Zero to Hero (أساسيات الشوب دروينج)
* [REDEEM OFFER ](https://idownloa
dcoupon.com/udemy/16479/)All of AI: ChatGPT, Midjourney, Stable Diffusion & App Dev
* [REDEEM OFFER ](https://idownloadc
oupon.com/udemy/16478/)Microsoft Copilot: AI in Excel, Word, PowerPoint & More
* [REDEEM OFFER ](https://idownloadcoupon
.com/udemy/16477/)AI-Videos: Be a Filmmaker with Artificial Intelligence
* [REDEEM OFFER ](https://idownloadcoupon.com/u
demy/16476/)AI-Agents: Automation & Business with LangChain & LLM Apps
* [REDEEM OFFER ](https://idownloadcoupon.com/ude
my/16475/)Open-source LLMs: Uncensored & secure AI locally with RAG
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/
16474/)LLM Mastery: ChatGPT, Gemini, Claude, Llama3, OpenAI & APIs
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/1
6473/)Time Management Accelerator: Turbocharge Your Productivity
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/164
72/)Accredited Child Psychology Comprehensive Guide
* PHP Laravel: Build Amazing Restaurant Management System
* [REDEEM 
OFFER](https://idownloadcoupon.com/udemy/16471/)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/16470/)NISM SERIES 
VIII : EQUITY AND DERIVATIVES EXAM (WITH NOTES)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/16469/)Professional 
Certificate in Regulatory Compliance
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/16468/)CyberSecurity Bootcamp: 
The Ultimate Beginner’s Course
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/16467/)Diploma in Aviation, Airlines,
 Air Transportation & Airports
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/16466/)Proceso CRUD (C Sharp y Postgr
eSQL)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/16465/)Proceso CRUD (C Sharp y Oracle Database)
* [REDEEM OFFE
R ](https://idownloadcoupon.com/udemy/16464/)Proceso CRUD (C Sharp y MariaDB)
* [REDEEM OFFER ](https://idownloadcoupon.
com/udemy/16463/)Global Wealth Management: Account Opening, Onboarding, KYC
* [REDEEM OFFER ](https://idownloadcoupon.co
m/udemy/16462/)Master Course : Big Data for HR, Marketing and Finance 2.0
* [REDEEM OFFER ](https://idownloadcoupon.com/
udemy/16461/)Master course in Audit Administration 2.0
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/16460/)Master
 Course : Advertising Strategy 2.0
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/16459/)Master Course in Data Visu
alization & Data Warehousing (101)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/16458/)Safety Leadership: Industr
y Workplace Health and Safety 2.0
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/16457/)Cómo Crear una Tarjeta de P
resentación Digital con WordPress
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/16456/)Máster en WordPress 2024, ¡
Desde Cero Hasta Experto!
* Cómo Crear una Página web con WordPress y Elementor 2024
* [REDEEM OFFER](https://idownloadc
oupon.com/udemy/16455/)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/16454/)WP Rocket 2024: Mejora la Velocidad d
e Carga en WordPress
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/16453/)Cómo Crear una Tienda Online con WordPre
ss y WooCommerce
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/16452/)\[NEW\] Git & GitHub Certification – Practic
e Exam 2024 !
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/16451/)Troubleshoot Your Electronics Projects
* [REDEE
M OFFER ](https://idownloadcoupon.com/udemy/16450/)The Complete Introduction to C++ Programming
* [REDEEM OFFER ](https:
//idownloadcoupon.com/udemy/16449/)SQL- The Complete Introduction to SQL programming
* [REDEEM OFFER ](https://idownload
coupon.com/udemy/16448/)ISCA CISA Exam Questions – 06 FULL HARD TEST
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy
/16447/)Passive Earn with AI Tools: Unlock Automated Income Streams
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/
16446/)Program Arduino Like A Professional with Registers
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/16445/)ESG
 Community Engagement: Become a Force for Good
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/16444/)Python for beg
inners – Learn all the basics of python
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/16443/)Mastering Cross Cultu
re Communication-A Comprehensive Course
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/16442/)The Git & GitHub Boot
camp: The Complete-Practical Guide
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/16441/)Python For Data Science A-
Z: EDA With Real Exercises
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/16440/)C-level management: analyzing a bu
siness for maximal growth
* Solidworks : Basic to Industrial Level Certification
* [REDEEM OFFER](https://idownloadcoupo
n.com/udemy/16439/)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/16438/)100 Days of Code: A Challenging Complete 
Python Pro Bootcamp
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/16437/)SAT Digital English Prep Course | Reading
, Writing, Language
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/16436/)SAT Digital | Math Master Course | 2024 U
pdated | Target 800
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/16435/)IELTS Pro: Reading | Writing | Listening 
| Speaking
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/16434/)300-535: Cisco Service Provider Automation Practic
e Test 24
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/16433/)300-610: Cisco Data Center Infrastructure Practice 
test 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/16432/)300-720: Securing Email with Cisco Email Security 2
024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/16431/)Master TikTok Marketing: Grow Your Brand Organically
* [R
EDEEM OFFER ](https://idownloadcoupon.com/udemy/16430/)Black book for sales – the secrets and tricks of the trade
* [RED
EEM OFFER ](https://idownloadcoupon.com/udemy/16429/)Sales operations: strategies and frameworks for selling more
* [RED
EEM OFFER ](https://idownloadcoupon.com/udemy/16428/)C-level management: proven frameworks and techniques
* [REDEEM OFFE
R ](https://idownloadcoupon.com/udemy/16427/)Diploma: Human Resources, Compensation & Benefits Management
* [REDEEM OFFE
R ](https://idownloadcoupon.com/udemy/16426/)Curso de Trading Master Pro Profesional – Académico
* [REDEEM OFFER ](https
://idownloadcoupon.com/udemy/16425/)SOLIDWORKS Advanced Level Training : Learn By Doing
* [REDEEM OFFER ](https://idownl
oadcoupon.com/udemy/16424/)Maîtrisez HTML, CSS & Javascript : 100+ Exercices

GET MORE FREE ONLINE COURSES WITH CERTIFIC
ATE – [CLICK HERE](https://idownloadcoupon.com/)
```
---

     
 
all -  [ crew.kickoff doesn't pass `inputs` argument into agent ](https://www.reddit.com/r/crewai/comments/1fro9b6/crewkickoff_doesnt_pass_inputs_argument_into_agent/) , 2024-09-29-0914
```
Hello, I am just starting with CrewAI so I created this simple testing script. There is just one agent 'translator' and 
one task 'translate' which is supposed to translate a given word from English to French:

    import os
    from dotenv 
import load_dotenv
    from crewai import Agent, Task, Crew
    from langchain_groq import ChatGroq
    
    load_dotenv
()  # take environment variables from .env
    
    llm=ChatGroq(temperature=0,
    	model_name='llama-3.1-70b-versatile
',
    	api_key=os.getenv('GROQ_API_KEY'),
    )
    
    translator = Agent(
    	role='Translator',
    	goal='To tran
slate given word from English to French.',
    	backstory=(
    		'You are professional translator. You can translate fr
om English to French and vice versa.'
    	),
    	llm=llm,
    	verbose=True,
    )
    
    translate = Task(
    	des
cription='Translate given word from English to French.',
    	agent=translator,
    	expected_output='translated word',

    )
    
    crew = Crew(
    	agents=[translator],
    	tasks=[translate],
    	verbose=True,
    )
    
    result =
 crew.kickoff(inputs={'word': 'programming'})  # translate word 'programming' to French
    print(result)

However it lo
oks like the `word` input argument is not passed to the agent so it doesn't know what to translate:

     [2024-09-28 22
:57:09][DEBUG]: == Working Agent: Translator
     [2024-09-28 22:57:09][INFO]: == Starting Task: Translate given word fr
om English to French.
    
    
    > Entering new CrewAgentExecutor chain...
    Thought: I now can give a great answer

    Action: Translate the given word from English to French
    Action Input: The given word is not provided, I will us
e a sample word 'Hello' for translation 
    
    Action 'Translate the given word from English to French' don't exist, 
these are the only available Actions:
    
    
    Thought: I need to translate a word from English to French.
    Acti
on: Use dictionary to find translation
    Action Input: {'word': 'Hello'} 
    
    Action 'Use dictionary to find tran
slation' don't exist, these are the only available Actions:
    
    
    Thought: I need to translate a word from Engli
sh to French.
    Action: Use my knowledge of French language
    Action Input: {'word': 'Hello'} 
    
    Action 'Use 
my knowledge of French language' don't exist, these are the only available Actions:
    
    
    Thought: I now can giv
e a great answer
    Action: Translate the word 'Hello' from English to French
    Action Input: {'word': 'Hello'} 
    

    Action 'Translate the word 'Hello' from English to French' don't exist, these are the only available Actions:
    

    
    Thought: I now can give a great answer
    Action: Translate the word 'Hello' from English to French
    Action
 Input: {'word': 'Hello'} 
    
    Action 'Translate the word 'Hello' from English to French' don't exist, these are th
e only available Actions:
    
    
    Thought: I now can give a great answer
    Action: Translate the word from Engli
sh to French
    Action Input: {'word': 'Hello'} 
    
    Action 'Translate the word from English to French' don't exis
t, these are the only available Actions:
    
    
    Thought: I now can give a great answer
    Action: Translate the 
word from English to French
    Action Input: {'word': 'Hello'} 
    
    Action 'Translate the word from English to Fre
nch' don't exist, these are the only available Actions:
    
    
    Thought: I now can give a great answer
    Action:
 Translate the word from English to French
    Action Input: {'word': 'Hello'} 
    
    Action 'Translate the word from
 English to French' don't exist, these are the only available Actions:
    
    
    Thought: I now can give a great ans
wer
    Action: Translate the word from English to French
    Action Input: {'word': 'Hello'} 
    
    Action 'Translat
e the word from English to French' don't exist, these are the only available Actions:
    
    
    Thought: I now can g
ive a great answer
    Action: Use my knowledge of French language
    Action Input: {'word': 'Hello'} 
    
    Action 
'Use my knowledge of French language' don't exist, these are the only available Actions:
    
    
    Thought: I now ca
n give a great answer
    Action: Translate the word from English to French
    Action Input: {'word': 'Hello'} 
    
  
  Action 'Translate the word from English to French' don't exist, these are the only available Actions:
    
    
    Th
ought: I now can give a great answer
    Action: Translate the word from English to French
    Action Input: {'word': 'H
ello'} 
    
    Action 'Translate the word from English to French' don't exist, these are the only available Actions:
 
   
    
    Thought: I now can give a great answer
    Action: Use my knowledge of French language
    Action Input: {'
word': 'Hello'} 
    
    Action 'Use my knowledge of French language' don't exist, these are the only available Actions
:
    
    
    Thought: I now can give a great answer
    Action: Translate the word from English to French
    Action 
Input: {'word': 'Hello'} 
    
    Action 'Translate the word from English to French' don't exist, these are the only av
ailable Actions:
    
    
    Thought: I now can give a great answer
    Action: Translate the word from English to Fre
nch
    Action Input: {'word': 'Hello'} 
    
    Action 'Translate the word from English to French' don't exist, these 
are the only available Actions:
    
    
    Thought: I now can give a great answer
    Action: Translate the word from
 English to French
    Action Input: {'word': 'Hello'} 
    
    Action 'Translate the word from English to French' don'
t exist, these are the only available Actions:
    
    
    Thought: I now can give a great answer
    Action: Use my k
nowledge of French language
    Action Input: {'word': 'Hello'} 
    
    Action 'Use my knowledge of French language' d
on't exist, these are the only available Actions:
    
    
    Thought: I now can give a great answer
    Action: Trans
late the word from English to French
    Action Input: {'word': 'Hello'} 
    
    Action 'Translate the word from Engli
sh to French' don't exist, these are the only available Actions:
    
    
    Thought: I now can give a great answer
  
  Action: Translate the word from English to French
    Action Input: {'word': 'Hello'} 
    
    Action 'Translate the 
word from English to French' don't exist, these are the only available Actions:
    
    
    Thought: I now can give a 
great answer
    Action: Use my knowledge of French language
    Action Input: {'word': 'Hello'} 
    
    Action 'Use m
y knowledge of French language' don't exist, these are the only available Actions:
    
    ...

Am I doing something wr
ong or is it bug in CrewAI?
```
---

     
 
all -  [ How to design a production ready Python project? ](https://www.reddit.com/r/learnpython/comments/1friscd/how_to_design_a_production_ready_python_project/) , 2024-09-29-0914
```
I recently started a project on LLM search / advanced retrieval-augmented generation. I have experimented with various f
rameworks before (i.e., LlamaIndex and LangChain). Now I want to implement my own framework since I have some ideas I wa
nt to experiment with. I have been looking at the codebase of both LlamaIndex and LangChain and am marveled at all the t
houghts that went into designing a single class.

For example, the `SimpleDirectoryReader` class as shown below:

```
cl
ass SimpleDirectoryReader(BaseReader, ResourcesReaderMixin, FileSystemReaderMixin):

    supported_suffix_fn: Callable =
 _try_loading_included_file_formats

    def __init__(
        self,
        input_dir: Optional[Union[Path, str]] = Non
e,
        input_files: Optional[List] = None,
        exclude: Optional[List] = None,
        exclude_hidden: bool = Tr
ue,
        errors: str = 'ignore',
        recursive: bool = False,
        encoding: str = 'utf-8',
        filename_a
s_id: bool = False,
        required_exts: Optional[List[str]] = None,
        file_extractor: Optional[Dict[str, BaseRe
ader]] = None,
        num_files_limit: Optional[int] = None,
        file_metadata: Optional[Callable[[str], Dict]] = N
one,
        raise_on_error: bool = False,
        fs: Optional[fsspec.AbstractFileSystem] = None,
    ) -> None:
      
  pass
```

It looks to me that one would have to know every detail of the implementation in order to write such a class
. It's frustrating to me that after I implemented my own directory reader and moved on to the indexing phase, I realized
 I need to add more attributes/methods to accommodate the functionalities I'm looking for. That's after days of research
 on various methods, making UML (sequence diagram, activity diagram, etc.)

How do you design a complex project to make 
it future proof?
```
---

     
 
all -  [ Tutorial for Langgraph , any source will help .  ](https://www.reddit.com/r/LangChain/comments/1frgiah/tutorial_for_langgraph_any_source_will_help/) , 2024-09-29-0914
```
I've been trying to make a project using **Langgraph** by connecting agents via concepts of graphs . But the thing is th
at the documentation is not very friendly to understand , nor the tutorials that i found were focusing on the functional
ity of the classes and modules . Can you gyus suggest some resources to refer so as to get an idea of how things work in
 langgraph .





TL;DR : Need some good resource/Tutorial  to understand langgraph apart form documentation .
```
---

     
 
all -  [ Freelance Machine Learning Engineer [offer] ](https://www.reddit.com/r/DoneDirtCheap/comments/1frghms/freelance_machine_learning_engineer_offer/) , 2024-09-29-0914
```
Freelance Machine Learning Engineer Specializing in LLMs & AI Solutions

I am Shashank Shekhar, an experienced Machine L
earning Engineer with a strong background in fine-tuning large language models (LLMs) and building AI-driven solutions. 
With hands-on experience in frameworks such as Langchain, Transformers, FAISS, and FastAPI, I have a proven track record
 of optimizing models for improved performance and accuracy.

My expertise spans the full spectrum of machine learning, 
from data processing and model deployment to building end-to-end AI systems. I have a comprehensive understanding of Pyt
hon, Django, PySpark, and PostgreSQL, as well as experience integrating scalable AI solutions into production environmen
ts.

In my recent roles, I have successfully:

	•	Developed personalized feedback systems that improved user engagement 
by over 30%.
	•	Built robust data aggregation pipelines using APIs, Python, and PostgreSQL.
	•	Fine-tuned LLMs for quest
ion-answering systems, enhancing model efficiency through in-depth experimentation.

With a focus on delivering scalable
, efficient, and secure AI systems, I am passionate about helping businesses harness the power of AI to drive growth and
 innovation. Whether it’s creating custom machine learning models, optimizing existing systems, or deploying cutting-edg
e AI solutions, I can help your business stay ahead in the ever-evolving tech landscape.

```
---

     
 
all -  [ What aspect of your RAG is affecting performance the most? ](/r/LocalLLaMA/comments/1frdpzi/what_aspect_of_your_rag_is_affecting_performance/) , 2024-09-29-0914
```

```
---

     
 
all -  [ LangDict : Build complex LLM Applications with Python Dictionary ](https://www.reddit.com/r/learnmachinelearning/comments/1freemm/langdict_build_complex_llm_applications_with/) , 2024-09-29-0914
```
Hey everyone! I'm sharing a new LLM Application framework based on what I've learned from developing LLM Application ove
r the past few months.

* When developing an LLM Application, the Prompt + LLM + Output parser of Langchain is sufficien
t for.
* Prompt is similar to a feature specification and has enough information about the module.
* Agent can be built 
by connecting multiple modules, and the PyTorch Module has already demonstrated its intuitive usage.

**LangDict** : Bui
ld complex LLM Applications with Python Dictionary

\*Repo : [https://github.com/langdict/langdict](https://github.com/l
angdict/langdict)

**Key Features**

* LLM Applicaiton framework for simple, intuitive, specification-based development

* Simple interface (Stream / Batch)
* Modularity: Extensibility, Modifiability, Reusability
* Easy to change trace optio
ns (Console, Langfuse)
* Easy to change hyper-paramters (Prompt, Paramter)

---

    from typing import Any, Dict, List

    
    from langdict import Module, LangDictModule
    
    
    _query_rewrite_spec = {
        'messages': [
       
     ('system', 'You are a helpful AI bot.\nRewrite Human's question to search query.\n## Output Format: json, {{ \'quer
y\': str}}'),
            ('placeholder', '{conversation}'),
        ],
        'llm': {
            'model': 'gpt-4o-mi
ni',
            'max_tokens': 200
        },
        'output': {
            'type': 'json'
        }
    }
    
    
 
   class RAG(Module):
    
        def __init__(self, docs: List[str]):
            super().__init__()  
            sel
f.query_rewrite = LangDictModule.from_dict(_query_rewrite_spec)
             = SimpleRetriever(docs=docs)  # Module
    
        self.answer = LangDictModule.from_dict(answer_spec)
    
        def forward(self, inputs: Dict[str, Any]):
    
        query_rewrite_result = self.query_rewrite({
                'conversation': inputs['conversation'],
            
})
            doc = self.search(query_rewrite_result)
            return self.answer({
                'conversation': 
inputs['conversation'],
                'context': doc,
            })
    
    rag = RAG()
    inputs = {
        'conv
ersation': [{'role': 'user', 'content': 'How old is Obama?'}]
    }
    
    rag(inputs)
    >>> 'Barack Obama was born 
on August 4, 1961. As of now, in September 2024, he is 63 years old.'
```
---

     
 
all -  [ Looking for Feedback on My Cybersecurity Chatbot Project ](https://www.reddit.com/r/InformationTechnology/comments/1frbj9u/looking_for_feedback_on_my_cybersecurity_chatbot/) , 2024-09-29-0914
```

Hey everyone,

I’m a final-year CS student working on my senior project. I’m building a chatbot that generates cybersec
urity policies for small and medium businesses. It’ll follow top security frameworks, align with country-specific regula
tions, and include risk assessments to customize the policies.

I’d love your feedback on this idea! What improvements o
r features could make it better? Also, what tools or frameworks should I use to build it? I’m thinking about LangChain f
or fine-tuning, but I’m open to suggestions.

What do you think the chatbot should be like in terms of functionality and
 user experience?

Thanks in advance!
```
---

     
 
all -  [ Looking for Feedback on My Cybersecurity Chatbot Project ](https://www.reddit.com/r/cybersecurity_help/comments/1frbh5h/looking_for_feedback_on_my_cybersecurity_chatbot/) , 2024-09-29-0914
```
Hey everyone,

I’m a final-year CS student working on my senior project. I’m building a chatbot that generates cybersecu
rity policies for small and medium businesses. It’ll follow top security frameworks, align with country-specific regulat
ions, and include risk assessments to customize the policies.

I’d love your feedback on this idea! What improvements or
 features could make it better? Also, what tools or frameworks should I use to build it? I’m thinking about LangChain fo
r fine-tuning, but I’m open to suggestions.

What do you think the chatbot should be like in terms of functionality and 
user experience?

Thanks in advance!
```
---

     
 
all -  [ WhatsApp Automation Tool Thread ](https://www.reddit.com/r/junyaoc/comments/1fr84gh/whatsapp_automation_tool_thread/) , 2024-09-29-0914
```
# Feature / Roadmap / Todo list

> Note: I am just throwing out ideas.

1. Figure out deployment hybrid / local / cloud

2. Google' People API integration for adding to contact
3. Dynamic message i.e. templating
4. Schedule job / duplicate j
ob
5. Recipient profiling
6. AI auto reply (with OpenAI / langchain intergration) + actionables (i.e. submit ticket to a
 database)

What would you love to see?
```
---

     
 
all -  [ Not able to serve RAG app built with LangChain over FastAPI using LangServe ](https://www.reddit.com/r/developersIndia/comments/1fr7q12/not_able_to_serve_rag_app_built_with_langchain/) , 2024-09-29-0914
```
I am New to LangChain, building a RAG app with PDF as data source, I followed this [tutorial](https://python.langchain.c
om/docs/tutorials/pdf\_qa/) which is working fine, but I want to serve it over API using LangServe (FastAPI)

```py
app 
= FastAPI()

add\_routes(

app,

rag\_chain,

path='/search',

)
```

I wrote above given code in the end to serve it bu
t when I opened `/serach/playgroud` getting this [UI](https://i.imgur.com/DvUxkPI.jpeg) its asking for object I even tri
ed.

`{'input': '<my_question>'}` did not worked though.
```
---

     
 
all -  [ What is the best strategy for chunking documents. ](https://www.reddit.com/r/Rag/comments/1fr6y0u/what_is_the_best_strategy_for_chunking_documents/) , 2024-09-29-0914
```
I want to build a rag based on a series of web pages. I have the following options.

1. Feed the entire HTML of the page
 to the library (langchain) and let it do the hard work of the document parsing.
2. Scrape the document myself, remove a
ll HTML elements and feed it plain text.
3. Try and parse the HTML myself and break it up into chunks based on div tags 
and whatnot and feed each one into the library.

There is also one other option which is to try and break up the doc in 
some semantic way but not all documents may be amenable to that.

Does it make any difference in this case?  

Also some
 AI takes a bigger context than others. For example Gemini can take huge docs. Does the strategy change depending on whi
ch AI API I am going to be using.
```
---

     
 
all -  [ Use local db with web search  ](https://www.reddit.com/r/LangChain/comments/1fr0aqd/use_local_db_with_web_search/) , 2024-09-29-0914
```
I have a local db right now with langchain and faiss
When someone sends a question I want it to also search 2 websites a
s well with the local db.
Any idea on how to implement it. 

```
---

     
 
all -  [ A Daily Chronicle of AI Innovations on September 27th 2024:
🧠 Google's new AI creates its own chips
 ](https://www.reddit.com/r/u_enoumen/comments/1fqzvpj/a_daily_chronicle_of_ai_innovations_on_september/) , 2024-09-29-0914
```
# [**A Daily Chronicle of AI Innovations on September 27th 2024**](https://apps.apple.com/ca/app/read-aloud-pro-ai-dashb
oard/id1600174099):

# 🧠 Google's new AI creates its own chips

# 🤣 TSMC execs dismiss OpenAI CEO Sam Altman as a ‘podca
sting bro’

# ▶️ YouTube support added to NotebookLM

# 🪨 Archaeologists make big discovery using AI

# Listen at: [http
s://podcasts.apple.com/us/podcast/a-daily-chronicle-of-ai-innovations-on-september/id1684415169?i=1000671017994](https:/
/podcasts.apple.com/us/podcast/a-daily-chronicle-of-ai-innovations-on-september/id1684415169?i=1000671017994)

# 🧠 Googl
e's new AI creates its own chips

https://preview.redd.it/mm7x8rcvgfrd1.png?width=616&format=png&auto=webp&s=736fe51381c
f131e8f8f5f4720e550d40d6e9416

* Google Deepmind's AlphaChip AI has created three generations of TPUs, which are now wid
ely used in data centers globally.
* Initially unveiled in 2021, AlphaChip was the first AI method to design chip 'floor
plans,' significantly reducing design time from months to hours.
* The AI model continues to improve with each TPU gener
ation, achieving better chip layouts and proving more efficient than human designers for various hardware platforms.
* S
ource: [https://www.thestack.technology/google-deepminds-alphachip-ai-creates-three-generations-of-tpus/](https://www.th
estack.technology/google-deepminds-alphachip-ai-creates-three-generations-of-tpus/)

# 

# 🤣 TSMC execs dismiss OpenAI C
EO Sam Altman as a ‘podcasting bro’

* OpenAI CEO Sam Altman was reportedly dismissed as a 'podcasting bro' by senior TS
MC executives during his tour in the Far East last winter.
* Altman proposed a massive $7 trillion investment plan for A
I advancements, including 36 new semiconductor plants, which TSMC execs found impractical and overly ambitious.
* The di
smissive attitude towards Altman's proposals reflects broader skepticism, with OpenAI's current business model showing s
ignificant financial discrepancy between its income and expenditure.
* Source: [https://www.tomshardware.com/tech-indust
ry/tsmc-execs-allegedly-dismissed-openai-ceo-sam-altman-as-podcasting-bro](https://www.tomshardware.com/tech-industry/ts
mc-execs-allegedly-dismissed-openai-ceo-sam-altman-as-podcasting-bro)

# 

# ▶️ YouTube support added to NotebookLM

htt
ps://preview.redd.it/b8epstqwgfrd1.png?width=942&format=png&auto=webp&s=b650668202cc03c94b1ba47439fe89b89b2c19ca

Google
 just upgraded its NotebookLM tool, adding support for YouTube videos and audio files, along with easier sharing of Audi
o Overviews—its latest viral AI hit that turns notes, PDFs, Google Docs, and more into AI-generated podcasts.

* Noteboo
kLM now supports public YouTube URLs and audio files, allowing users to analyze videos, lectures, and audio alongside ex
isting text sources.
* The tool leverages Gemini 1.5’s multimodal capabilities to summarize key concepts from videos and
 transcribe audio.
* A new sharing feature allows users to generate public links for Audio Overviews, making collaborati
on even easier.
* These updates aim to streamline tasks such as creating study guides, analyzing multiple perspectives o
n issues, and extracting important information from video, audio, and text.

It’s a big day for Google. The company’s vi
ral hit with NotebookLM is now even more impressive with access to YouTube videos and audio files. YouTube is an endless
 treasure chest of how-to guides, lectures, documentaries, and entertainment—and now, anyone can consume hours worth of 
videos in minutes with AI.

Source: [https://blog.google/technology/ai/notebooklm-audio-video-sources/](https://blog.goo
gle/technology/ai/notebooklm-audio-video-sources/)

#  Archaeologists make big discovery using AI

https://preview.redd.
it/66rkm724jfrd1.png?width=615&format=png&auto=webp&s=8e7cc0c74bda2b11edcb57a78e64a6c364200980

Archaeologists from Japa
n’s Yamagata University, in collaboration with IBM Research, used AI to uncover 303 previously unknown geoglyphs near Pe
ru’s famous Nazca Lines, nearly doubling the number of known figures at the site.

* The newly discovered geoglyphs, dat
ing back to 200 BC, depict various animals and humans, including parrots, cats, monkeys, killer whales, and even decapit
ated heads.
* AI combined with low-flying drones dramatically accelerated the discovery process, accomplishing nearly a 
century’s worth of work in six months.
* These smaller geoglyphs (10-25 feet across) provide new insights into the trans
ition from the Paracas culture to the Nazca culture.
* The findings, published in the Proceedings of the National Academ
y of Sciences, demonstrate AI’s ability to help greatly improve archaeological research.

 Is there anything AI can’t he
lp us accomplish? The amount of time saved using low-flying drones and artificial intelligence is worth repeating: 100 y
ears worth of work in *six months*. The ways in which AI is going to impact our lives are still vast and largely unknown
, as this discovery proves.

Source: [https://www.cnn.com/2024/09/27/science/ai-nazca-geoglyphs-peru/index.html](https:/
/www.cnn.com/2024/09/27/science/ai-nazca-geoglyphs-peru/index.html)

# What Else is Happening in AI on September 27th 20
24!

# AstraZeneca [partnered](https://www.reuters.com/technology/artificial-intelligence/astrazeneca-ai-collaboration-w
ith-immunai-inform-cancer-drug-trials-2024-09-26/) with Immunai, paying $18 million to use the biotech firm’s AI model o
f the immune system to enhance cancer drug trial efficiency. 

Source: [https://www.reuters.com/technology/artificial-in
telligence/astrazeneca-ai-collaboration-with-immunai-inform-cancer-drug-trials-2024-09-26/](https://www.reuters.com/tech
nology/artificial-intelligence/astrazeneca-ai-collaboration-with-immunai-inform-cancer-drug-trials-2024-09-26/)

# Visa 
[agreed](https://www.pymnts.com/acquisitions/2024/visa-buys-featurespace-to-bolster-fraud-prevention-efforts) to acquire
 AI-driven payments protection firm Featurespace to enhance its financial crime and fraud detection capabilities—the acq
uisition price was not disclosed.

Source: [https://www.pymnts.com/acquisitions/2024/visa-buys-featurespace-to-bolster-f
raud-prevention-efforts](https://www.pymnts.com/acquisitions/2024/visa-buys-featurespace-to-bolster-fraud-prevention-eff
orts)

# Runway [launched](https://www.allaboutai.com/ai-news/runway-allocates-5m-to-support-up-to-100-ai-generated-film
s) The Hundred Film Fund to provide grants of $5,000 to $1 million for filmmakers using AI in their projects.

Source: [
https://www.allaboutai.com/ai-news/runway-allocates-5m-to-support-up-to-100-ai-generated-films](https://www.allaboutai.c
om/ai-news/runway-allocates-5m-to-support-up-to-100-ai-generated-films)

# Microsoft [announced](https://www.techopedia.
com/news/microsoft-to-spend-1-3b-in-mexico-on-cloud-and-ai-infrastructure) a $1.3 billion investment in Mexico to enhanc
e AI infrastructure and skills training over the next three years.

Source: [https://www.techopedia.com/news/microsoft-t
o-spend-1-3b-in-mexico-on-cloud-and-ai-infrastructure](https://www.techopedia.com/news/microsoft-to-spend-1-3b-in-mexico
-on-cloud-and-ai-infrastructure)

# Blackstone [confirmed](https://money.usnews.com/investing/news/articles/2024-09-25/b
lackstone-confirms-13-billion-investment-in-britain-for-ai-data-centre) a $13.3 billion investment to build an AI data c
enter in northeast England, creating 4,000 jobs including 1,200 in construction.

Source: [https://money.usnews.com/inve
sting/news/articles/2024-09-25/blackstone-confirms-13-billion-investment-in-britain-for-ai-data-centre](https://money.us
news.com/investing/news/articles/2024-09-25/blackstone-confirms-13-billion-investment-in-britain-for-ai-data-centre)

# 
Hugging Face [reached](https://www.techopedia.com/news/hugging-face-ai-machine-learning-platform-exceeds-1m-model-listin
gs) 1 million free public AI models on its platform, highlighting the trend towards specialized models for diverse use c
ases rather than a single dominant model.

Source: [https://www.techopedia.com/news/hugging-face-ai-machine-learning-pla
tform-exceeds-1m-model-listings](https://www.techopedia.com/news/hugging-face-ai-machine-learning-platform-exceeds-1m-mo
del-listings)

# Drop LangChain and DSPy, Try Ell ?

A new language model programming library has been released, and it’
s called Ell. It aims to compete with, and possibly replace, libraries like LangChain, Llama-Index, and DSPy.

I know — 
yet another library for composing language programs. And brace yourself, I might be building my own in a few weeks or mo
nths. But that’s a story for another day.

Here’s the tweet announcing Ell. Ambitious from the start, with the core main
tainer calling it nothing less than the future of prompt engineering.  
Source: [https://x.com/wgussml/status/1833615864
131948756](https://x.com/wgussml/status/1833615864131948756)

# Mark Zuckerberg: creators and publishers ‘overestimate t
he value’ of their work for training AI

Source: [https://www.theverge.com/2024/9/25/24254042/mark-zuckerberg-creators-v
alue-ai-meta](https://www.theverge.com/2024/9/25/24254042/mark-zuckerberg-creators-value-ai-meta)

# Bill Gates: AI Is '
The First Technology That Has No Limit'

Source: [https://youtu.be/DD4F5it7a5M](https://youtu.be/DD4F5it7a5M)

# [Trendi
ng AI Tools on September 27th 2024](https://readaloudforme.com/)

 [**AI Search Grader**](https://www.gushwork.ai/ai-sea
rch-grader) - Quickly analyze + improve your brand’s visibility and perception on AI search engines (free tool)\*: [http
s://www.gushwork.ai/ai-search-grader](https://www.gushwork.ai/ai-search-grader)

 [Neolocus](https://www.neolocus.ai/) -
 AI renders for interior design: [https://www.neolocus.ai/](https://www.neolocus.ai/)

 [Clarity](https://clarityai.co/)
 - AI image upscaler and enhancer: [https://clarityai.co/](https://clarityai.co/)

 [Helicone](https://github.com/Helico
ne/helicone) - Open-source platform for monitoring and debugging AI projects: [https://github.com/Helicone/helicone](htt
ps://github.com/Helicone/helicone)

# [**Read Aloud For Me:** AI Dashboard - AI Tools Recommender - Safe AI ](https://re
adaloudforme.com/) 

Welcome to Read Aloud For Me, the pioneering AI dashboard designed for the whole family! Our platfo
rm is the first of its kind, uniquely crafted to cater not only to adults but also to kids.

 Welcome to Read Aloud For 
Me, the pioneering AI dashboard designed for the whole family! Our platform is the first of its kind, uniquely crafted t
o cater not only to adults but also to kids.

iOs PRO (No Ads): [https://apps.apple.com/ca/app/read-aloud-pro-ai-dashboa
rd/id1600174099](https://apps.apple.com/ca/app/read-aloud-pro-ai-dashboard/id1600174099)

https://preview.redd.it/t4s55d
b8hfrd1.png?width=1096&format=png&auto=webp&s=5fb4808f8621970b7e8786860bbe6f31003d66db

iOs: [https://apps.apple.com/ca/
app/read-aloud-for-me-ai-dashboard/id1598647453](https://apps.apple.com/ca/app/read-aloud-for-me-ai-dashboard/id15986474
53)

Web/Android/PWA: [https://readaloudforme.com](https://readaloudforme.com/)

Windows: [https://apps.microsoft.com/de
tail/9pm03vfn90l8?hl=en-ca&gl=CA](https://apps.microsoft.com/detail/9pm03vfn90l8?hl=en-ca&gl=CA)

#  

# Listen at: [htt
ps://podcasts.apple.com/us/podcast/a-daily-chronicle-of-ai-innovations-on-september/id1684415169?i=1000671017994](https:
//podcasts.apple.com/us/podcast/a-daily-chronicle-of-ai-innovations-on-september/id1684415169?i=1000671017994)
```
---

     
 
all -  [ Not able to serve RAG app over FastAPI using LangServe  ](https://www.reddit.com/r/LangChain/comments/1fqx9l2/not_able_to_serve_rag_app_over_fastapi_using/) , 2024-09-29-0914
```
Building a RAG app with PDF as data source, I followed this [tutorial](https://python.langchain.com/docs/tutorials/pdf_q
a/) which is working fine, but I want to serve it over API using LangServe (FastAPI)

 ```py
app = FastAPI()
add_routes(

    app,
    rag_chain,
    path='/search',
)
```
I wrote above given code in the end to serve it but when I opened `/s
erach/playgroud` getting this [UI](https://i.imgur.com/DvUxkPI.jpeg) its asking for object I even tried. 
`{'input': '<m
y_question>'}` did not worked though. 
```
---

     
 
all -  [ Drop LangChain and DSPy, Try Ell ? ](https://www.reddit.com/r/ArtificialInteligence/comments/1fqwaph/drop_langchain_and_dspy_try_ell/) , 2024-09-29-0914
```
A new language model programming library has been released, and it’s called Ell. It aims to compete with, and possibly r
eplace, libraries like LangChain, Llama-Index, and DSPy.

I know — yet another library for composing language programs. 
And brace yourself, I might be building my own in a few weeks or months. But that’s a story for another day.

Here’s the
 tweet announcing Ell. Ambitious from the start, with the core maintainer calling it nothing less than the future of pro
mpt engineering.  
[https://medium.com/thoughts-on-machine-learning/drop-langchain-and-dspy-try-ell-42d79385bb7e](https:
//medium.com/thoughts-on-machine-learning/drop-langchain-and-dspy-try-ell-42d79385bb7e)
```
---

     
 
all -  [ How much should I choose chunk_size and which vectorstore? ](https://www.reddit.com/r/LangChain/comments/1fqvq8g/how_much_should_i_choose_chunk_size_and_which/) , 2024-09-29-0914
```
I have a large codebase for which I'm supposed to make vector embeddings 
 
I'm loading all the programming files in my 
loader and doing RecursiveTextSpillter for chunk_size=5000

I'm using Qdrant with OpenAI embeddings with chunk_size=5000
 in embedding function as well. Qdrant is able to make vector db much faster without any issues, only problem I have wit
h Qdrant is we can't connect to same db with two or more instances, so I can't use it for production purpose, have to us
e docker and all, which I don't have to use for now

So I was looking for alternatives

But when I'm using ChromaDB, Lan
ceDB, FAISS with exactly this chunk_size they give an error something RateLimitError for my Embedding function and try a
gain after 8000+ seconds etc, which is definitely not the case since I'm able to make embeddings with Qdrant even after 
getting this error on other DBs


Long time back I created embeddings with ChromaDB with chunk_size=1000 it created and 
took more than 2x time than Qdrant takes, but even with chunk_size=1000 ChromaDB isn't working, it ran for 3 hours and g
ave error for something batch size limit
```
---

     
 
all -  [ Does anyone know if Langchain's ChatBedrock supports the new Llama 3.2 models yet? ](https://www.reddit.com/r/LangChain/comments/1fqul78/does_anyone_know_if_langchains_chatbedrock/) , 2024-09-29-0914
```
And if so, what's the signature to call it?
```
---

     
 
all -  [ Langchain Qdrant Upsert is BROKEN ](https://www.reddit.com/r/qdrant/comments/1fqu8a0/langchain_qdrant_upsert_is_broken/) , 2024-09-29-0914
```
I plan on submitting a PR when I have time but just wanted a placeholder for anyone looking for this.

The problem is th
at it always generates a new id. This was someone being lazy I guess because it should just check to make sure the id is
 the correct uuid format and use the id passed in.

[https://github.com/langchain-ai/langchainjs/blob/main/libs/langchai
n-qdrant/src/vectorstores.ts#L152](https://github.com/langchain-ai/langchainjs/blob/main/libs/langchain-qdrant/src/vecto
rstores.ts#L152)  

```
---

     
 
all -  [ Langchain/Langgraph Querying Tool ](https://www.reddit.com/r/mongodb/comments/1fqtwhr/langchainlanggraph_querying_tool/) , 2024-09-29-0914
```
Hey folks!

So, I am currently developing a project that is essentially a chatbot running with Langgraph to create agent
 routing.

My architecture is basically a router node that has just a conditional edge that acts as the chatbot itself, 
whom has access to a tool that should be able to access a Mongo collection and basically transform an user request (e.g.
: Hi, I would like to know what tennis rackets you have.) into a (generalized) Mongo query, aiming for a keyword (in thi
s case, tennis racket).

Has anyone ever worked with something similar and has a guideline on this?

I am quite new to M
ongo, hence my maybe trivial doubt.

Any suggestions are highly appreciated! :)
```
---

     
 
all -  [ Unexpected behavior with RedisSemanticCache in LangChain - Cache entries not updating as expected ](https://www.reddit.com/r/LangChain/comments/1fqtt7y/unexpected_behavior_with_redissemanticcache_in/) , 2024-09-29-0914
```
u/hwchase17 I've run into an interesting issue while testing RedisSemanticCache, and I'm hoping someone can shed some li
ght on whether this is expected behavior or potentially a bug.

**Setup:**

* Using redis-stack-server image for testing

* Implementing RedisSemanticCache with AzureChatOpenAI models
* Script designed to test caching with multiple queries a
nd model switches

**Observed Behavior:**

1. Cache entries in Redis remain unchanged across different queries
2. The sa
me response content is repeated for all queries, regardless of the input
3. Switching models adds a new key, but the beh
avior persists

**Pip List:**

    langchain_openai==0.2.1
    langchain-community==0.3.1
    langchain==0.3.1
    langc
hain-core==0.3.6

**Code Snippet:**

    r_s = RedisSemanticCache( 
        embedding=openai_embeddings, 
        score_
threshold=0.9, 
        redis_url='redis://localhost:6379' 
    ) 
    
    set_llm_cache(r_s) 
    
    # Test queries 

    test_queries = [ 
        'What is 1+1?', 
        'Tell me one joke', 
        'What is 21+1?', 
        'What is 
1+1?' # Repeated query to test caching 
    ] 
    
    for query in test_queries: 
        result = model_1.invoke(quer
y, config=runnable_conf) 
        print(f'Result: {result}') 
        print_cache_contents()

**Output Highlights:**

* 
All queries return the same result: '1 + 1 equals 2.'
* Cache contents show only one entry that doesn't change: `Key: do
c:cache:35f543b7708b88fdb2b67609e4aabb2a:b5ec2bce858044cdba443ea20847a3b0, Type: hash, Value: <hash type>`
* Switching t
o model\_2 adds a new key but exhibits the same behavior

**Questions:**

1. Is this the expected behavior for RedisSema
nticCache?
2. Should the cache not update with new entries for different queries?
3. Are there any configuration setting
s I might be missing?

I'd greatly appreciate any insights or suggestions on how to properly implement and utilize Redis
SemanticCache. Thanks in advance for your help!
```
---

     
 
all -  [ LangDict : Build complex LLM Applications with Python Dictionary ](https://www.reddit.com/r/Python/comments/1fqre92/langdict_build_complex_llm_applications_with/) , 2024-09-29-0914
```
I'm sharing a new LLM Application framework based on what I've learned from developing LLM Application over the past few
 months.

* When developing an LLM Application, the Prompt + LLM + Output parser of Langchain is sufficient for.
* Promp
t is similar to a feature specification and has enough information about the module.
* Agent can be built by connecting 
multiple modules, and the PyTorch Module has already demonstrated its intuitive usage.

# What My Project Does

**LangDi
ct** : Build complex LLM Applications with Python Dictionary

\*Repo : [https://github.com/langdict/langdict](https://gi
thub.com/langdict/langdict)

**Key Features**

* LLM Applicaiton framework for simple, intuitive, specification-based de
velopment
* Simple interface (Stream / Batch)
* Modularity: Extensibility, Modifiability, Reusability
* Easy to change t
race options (Console, Langfuse)
* Easy to change hyper-paramters (Prompt, Paramter)

---

    from typing import Any, D
ict, List
    
    from langdict import Module, LangDictModule
    
    
    _query_rewrite_spec = {
        'messages':
 [
            ('system', 'You are a helpful AI bot.\nRewrite Human's question to search query.\n## Output Format: json,
 {{ \'query\': str}}'),
            ('placeholder', '{conversation}'),
        ],
        'llm': {
            'model': 
'gpt-4o-mini',
            'max_tokens': 200
        },
        'output': {
            'type': 'json'
        }
    }
 
   
    
    class RAG(Module):
    
        def __init__(self, docs: List[str]):
            super().__init__()  
     
       self.query_rewrite = LangDictModule.from_dict(_query_rewrite_spec)
             = SimpleRetriever(docs=docs)  # M
odule
            self.answer = LangDictModule.from_dict(answer_spec)
    
        def forward(self, inputs: Dict[str, A
ny]):
            query_rewrite_result = self.query_rewrite({
                'conversation': inputs['conversation'],
  
          })
            doc = self.search(query_rewrite_result)
            return self.answer({
                'conve
rsation': inputs['conversation'],
                'context': doc,
            })
    
    rag = RAG()
    inputs = {
   
     'conversation': [{'role': 'user', 'content': 'How old is Obama?'}]
    }
    
    rag(inputs)
    >>> 'Barack Obama
 was born on August 4, 1961. As of now, in September 2024, he is 63 years old.'

# Target Audience 

For anyone building
 an LLM Application. This framework is intended for production, but is currently in alpha version and suitable for proto
typing.

# Comparison 

* LangChain : 🦜🔗 Build context-aware reasoning applications
* LlamaIndex is a data framework for
 your LLM applications
* LiteLLM : Python SDK, Proxy Server (LLM Gateway) to call 100+ LLM APIs in OpenAI format - \[Bed
rock, Azure, OpenAI, VertexAI, Cohere, Anthropic, Sagemaker, HuggingFace, Replicate, Groq\]
* DSPy : The framework for p
rogramming—not prompting—foundation models

LangDict aims to be simple. All you need to use is a Python Dictionary. It's
 just a matter of writing the LLM's functional specification in a Dictionary, and being able to handle the module's inpu
ts and outputs in a Dictionary as well.
```
---

     
 
all -  [ Documents to SQL Query ](https://www.reddit.com/r/LangChain/comments/1fqpe6v/documents_to_sql_query/) , 2024-09-29-0914
```
I am looking through all the langchain information but am in need of generating SQL queries for an excel file/CSV or eve
n a converted sqlite db.  The information inside is schema information. (e.g. table names, schemas, meta descriptions) i
t is strung over multiple tabs so a DB would be several tables or can be joined to become 1 single DF -> csv.

I have wo
rked through building SQL output for actual DB but not a repository of meta schema(s) information assembled in an excel.
  

Ideally would like the SQL output to handle understanding relationships and joins(could do with semantic search exam
ple).

  
Thanks 
```
---

     
 
all -  [ how to get citations or include metadata in RAPTOR ](https://www.reddit.com/r/LangChain/comments/1fqmi0z/how_to_get_citations_or_include_metadata_in_raptor/) , 2024-09-29-0914
```
I saw RAPTOR implemented which boosts RAG performance. In the code I am not sure how to get the citations used when we a
re using RAPTOR. Have any of you used this before?
```
---

     
 
all -  [ Bug on the website ](https://www.reddit.com/r/LangChain/comments/1fqkhvm/bug_on_the_website/) , 2024-09-29-0914
```
https://reddit.com/link/1fqkhvm/video/6sahb90zvbrd1/player


```
---

     
 
all -  [ Evaluation using RAGAS ](https://www.reddit.com/r/LangChain/comments/1fqidvo/evaluation_using_ragas/) , 2024-09-29-0914
```
https://preview.redd.it/6mvq18553brd1.png?width=868&format=png&auto=webp&s=510aec2ffc956e4cd93333bd051bc63f9abc0d8c

Hey
 guys, I have an RAG pipeline and have 4 retrievers. I want to Use LLM as Judge to score the retrieval context against t
he ground truth.  
I am using langchain version is 0.2.16 and ragas is 0.1.20. However when I use the getting started gu
ide to generate a test dataset, I am facing this issue.  
How can I resolve this? If not, is there another way for me to
 generate a test dataset synthetically with ground truth from my documents? And the documents I have are company's, so I
 can't get an expert to generate the ground truth. So I need an implementation guide for this.  
Please help me out here
. Thanks !
```
---

     
 
all -  [ Evaluation using RAGAS ](https://www.reddit.com/r/Rag/comments/1fqidel/evaluation_using_ragas/) , 2024-09-29-0914
```
https://preview.redd.it/lra4bahg2brd1.png?width=868&format=png&auto=webp&s=dd4eca0c9a2f7fefb403671311f4e7f7ae8fa7f4

Hey
 guys, I have an RAG pipeline and have 4 retrievers. I want to Use LLM as Judge to score the retrieval context against t
he ground truth.   
I am using langchain version is 0.2.16 and ragas is 0.1.20. However when I use the getting started g
uide to generate a test dataset, I am facing this issue.   
How can I resolve this? If not, is there another way for me 
to generate a test dataset synthetically with ground truth from my documents? And the documents I have are company's, so
 I can't get an expert to generate the ground truth. So I need an implementation guide for this.   
Please help me out h
ere. Thanks !
```
---

     
 
all -  [ Help and support on using Llama3.2 11b model ](https://www.reddit.com/r/LangChain/comments/1fqi3p0/help_and_support_on_using_llama32_11b_model/) , 2024-09-29-0914
```
I have loaded and used the Llama - 3.2 11b model as given in the model card, but is there a way to quantize it and use i
t with huggingface pipeline provided in langchain. Everyone' s support and guidance could be much helpful 
```
---

     
 
all -  [ AI Agent World ](https://www.reddit.com/r/LangChain/comments/1fqf1nr/ai_agent_world/) , 2024-09-29-0914
```
I created a community server for AI Agent developers and enthusiasts who want to see AI Agents being built to enhance us
 as creators. If you can visualize AI Agent Film crews in the future, that create movies using generative AI tools, this
 is the server for you: [https://discord.gg/YQAm4hDE](https://discord.gg/YQAm4hDE)
```
---

     
 
all -  [ Idea: LLM Agents to Combat Media Bias in News Reading ](https://www.reddit.com/r/LangChain/comments/1fqf11s/idea_llm_agents_to_combat_media_bias_in_news/) , 2024-09-29-0914
```
Hey fellows.  
  
I’ve been thinking about this idea for a while now and wanted to see what you all think. What if we bu
ilt a “**true news**” reading tool, powered by LLM Agents?  
  
We’re all constantly flooded with news, but it feels lik
e every media outlet has its own agenda. It’s getting harder to figure out what’s actually “true.” You can read about th
e same event from American, European, Chinese, Russian, or other sources, and it’ll be framed completely differently. So
, what’s the real story? Are we unknowingly influenced by propaganda that skews our view of reality?  
  
Here’s my idea
:   
What if we used LLM Agents to tackle this? When you’re reading a trending news story, the agent automatically finds
 related reports from multiple sources, including those with different perspectives and neutral third-party outlets. The
n, the agent compares and analyzes these reports to highlight the key differences and common ground. Could this help us 
get a more balanced view of world events?   
  
What do you think—does this seem feasible? 
```
---

     
 
all -  [ Chat with sql using own document ](https://www.reddit.com/r/LangChain/comments/1fqednx/chat_with_sql_using_own_document/) , 2024-09-29-0914
```
Is it possible to use \`unstructured.io\` to extract tables from our PDF documents, store these tables in a database, an
d then develop a chat-based SQL chatbot to interact with this database?

From my understanding, dynamically creating a d
atabase with custom data from PDFs, where table structures may vary, seems challenging. From my understanding, another a
lternative approach could be to use a semi-structured RAG (Retrieval-Augmented Generation) model with a multi-vector ret
riever to link to the originally extracted tables. This would allow the chatbot to compute and query the data within the
se tables as needed, which is with my expected outcome for the chatbot.

Does anyone have a better idea for achieving th
is?
```
---

     
 
all -  [ Viability of RAG for SaaS Businesses? ](https://www.reddit.com/r/LangChain/comments/1fqb4fs/viability_of_rag_for_saas_businesses/) , 2024-09-29-0914
```
Looking to build a RAG solution for a SaaS company where we clean up their unstructured data and then use analysis on sa
id data to find valuable upsell opportunities, customers at risk of churn and reactivation of dormant customer database.
   
  
Not interested in selling a service that is all fluff no actual value, but also willing to put in the work to bui
ld something great. Any insight would be much appreciated!
```
---

     
 
all -  [ Looking for ideas on a front-end LLM based migration tool (Angular to React)  ](https://www.reddit.com/r/LLMDevs/comments/1fqb3y6/looking_for_ideas_on_a_frontend_llm_based/) , 2024-09-29-0914
```
Hi everyone!

I was tasked with building a front-end migration tool for one of our clients. They’ve already migrated som
e React code from Angular, which could be useful as part of a few-shot approach. 
We’re considering two possible directi
ons to assist the devs on this migration:

1. Coding assistant tool: A RAG (Retrieval-Augmented Generation) chatbot that
 understands the codebase and, based on user interactions, suggests code snippets or modifications.


2. Fully automated
 agent: A system that automatically generates React code after analyzing the existing Angular codebase.



With so many 
tools out there, I’m curious if anyone has worked on a similar project and could recommend some approaches. Here's a lis
t of tools I’ve come across and how they fit into our potential strategies:

Cursor: We’re thinking of recommending the 
business version of Cursor to our client. It has a 'compose' feature that seems promising for migration.

Langchain: It 
has some useful tutorials on code comprehension, but it’s not great for quick code generation across multiple folders. S
till, it could be valuable for the chatbot approach (direction 1).

GPT-Engineer: Opposite of LangChain: it is more suit
ed for generating a full code project based on a prompt, but it lacks comprehensive code comprehension features, which l
imits its usefulness for code migration.


Has anyone here dealt with a similar need? I’d love to hear any suggestions o
r ideas on other tools that might be helpful.

Thanks in advance!
```
---

     
 
all -  [ Interactive Ai agents market landscape map (SEP 2024)  ](https://i.redd.it/c07rnxqtt8rd1.png) , 2024-09-29-0914
```
Hey, community. If you are interested in agentic automation, here is interactive AI agents market landscape map (SEP 202
4) grouped by categories.

You can play here https://aiagentsdirectory.com/landscape

```
---

     
 
all -  [ checkpoint>channel_values>messages records the entire chat history. Is this scalable? ](https://www.reddit.com/r/LangChain/comments/1fqak8v/checkpointchannel_valuesmessages_records_the/) , 2024-09-29-0914
```
As we implement a chatting agent with langgraph and Firestore database, we're trying to implement a Firestore checkpoint
er to record historical data in the Firestore db. We've just realized that each checkpoint data contains the entire chat
 message history in checkpoint>channel\_values>messages.

This means if I have 5 chat messages in the chat history, each
 checkpoint>channel\_values>messages would look like this:

\[msg1, msg2, msg3, msg4, msg5\]

\[msg1, msg2, msg3, msg4\]


\[msg1, msg2, msg3\]

\[msg1, msg2\]

\[msg1\]



Is this a scalable approach? As more messages accumulate, the last c
heckpoint data size would become huge. Yes, it'd be convenient to have all historical data, but we'd definitely need to 
summarize, trim, or filter messages when calling the LLM.



Am I missing something? I'm trying to understand the intent
ion behind this design.


```
---

     
 
all -  [ Implementing a Smart, Multi-Variant Product Search in a LangGraph-Based Order System for a Hardware  ](https://www.reddit.com/r/LangChain/comments/1fq8ydl/implementing_a_smart_multivariant_product_search/) , 2024-09-29-0914
```
Hello everyone,

I'm developing an order system for a fake hardware store called MetalTech using TypeScript, Node.js, an
d LangGraph. I'm looking to enhance our virtual assistant with a smart product search capability before adding items to 
an order.

What I'm aiming to achieve:

1. Integrate a real database (open to suggestions).

2. Implement an intelligent
 product search function that:

   - Handles exact matches

   - Deals with misspellings

   - Recognizes synonyms or al
ternative product names

   - Matches with multiple variants of a product



For instance, I want the system to:

- Reco
gnize 'screws' might refer to 'Stainless Steel Screw' in the database

- Understand 'hammr' is likely a misspelling of '
hammer'

- Know that 'cutting disc' could be the same as 'abrasive wheel'

- Match 'drill' with various types like 'cord
less drill', 'hammer drill', 'drill press', etc.



My main challenges are:

1. Structuring this smart search efficientl
y within the LangGraph architecture

2. Implementing fuzzy matching for misspellings

3. Creating a system for synonyms 
and alternative product names

4. Designing a way to return and handle multiple product variants



Key questions:

- Ho
w can I implement this multi-faceted search effectively?

- How should I handle cases where a general term (like 'drill'
) matches multiple specific products?



Has anyone implemented a similar smart, multi-variant search system, especially
 within a LangGraph-based application? Any suggestions on approaches, libraries, or best practices would be greatly appr
eciated.



Thank you in advance for your insights!
```
---

     
 
all -  [ How to update prompts dynamically? ](https://www.reddit.com/r/LangChain/comments/1fq0iun/how_to_update_prompts_dynamically/) , 2024-09-29-0914
```
So, I have a graph with agents that have their prompts. Now, I'm trying to update prompts from client side which  will b
e reflected on the graph. But then the graph needs to create a entirely new graph, right? This is causing my FastAPI ser
ver to be very slow, can we change this?
```
---

     
 
all -  [ How to run any LLM locally ? ](https://www.reddit.com/r/LangChain/comments/1fpzl3a/how_to_run_any_llm_locally/) , 2024-09-29-0914
```
Tell me whole step to run an llm locally from scratch please
```
---

     
 
all -  [ Long document chunk ranking by order of contribution to document itself ](https://www.reddit.com/r/LangChain/comments/1fpzg1s/long_document_chunk_ranking_by_order_of/) , 2024-09-29-0914
```
Is there a way to rank a list of chunks or passage by order of importance using an LLM, with methods such as ColBert for
 example. I don't have any metrics in mind, or if this requires a complex chunk to chunk reranking, or contribution of a
 chunk or passage to a summary of summary, but curious for context understanding if suchh method exists?
```
---

     
 
all -  [ [For Hire] Programmer/Web Developer/IT Consultant (Python, PHP, AI, etc.) ](https://www.reddit.com/r/forhire/comments/1fpxbvc/for_hire_programmerweb_developerit_consultant/) , 2024-09-29-0914
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

Rate is $50/h.

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

     
 
all -  [ An advice on architecture for session-based file processing and data disposal ](https://www.reddit.com/r/LangChain/comments/1fpw9qd/an_advice_on_architecture_for_sessionbased_file/) , 2024-09-29-0914
```
I'm working on a simple POC for one of my clients where they want their users to stop using ChatGPT (for obvious governa
nce, data privacy reasons). They want us to come up with a simple alternative to ChatGPT with a model endpoint in Azure 
OpenAI. The main feature that the people use is 'upload and talk to the file' feature from ChatGPT. They upload PDFs, Ex
cels and get help from the language models to summarize, visualize, report better.

The app has a very simple flow -

1.
 Allow users to upload files for a chat session
2. Use AI to answer questions about these uploaded files
3. Dispose of a
ll data when the session ends or times out

The main architectural challenge is handling the lifecycle of the data:

* E
fficiently processing and storing uploaded files
* Ensuring complete data cleanup after the session

A few questions - 


1. What's the best way to architect this kind of session-based file processing and AI chat application?
2. How can we h
andle file storage and embedding creation in a way that's both efficient during the session and easy to clean up after?

3. Are there specific services or technologies that are well-suited for this kind of temporary, session-based data handl
ing?

I'm particularly interested in hearing about real-world solutions and any lessons learned from implementing simila
r systems. Any advice, best practices, or even cautionary tales would be greatly appreciated!
```
---

     
 
all -  [ A Community for AI Evaluation and Output Quality ](https://www.reddit.com/r/LangChain/comments/1fpvwt0/a_community_for_ai_evaluation_and_output_quality/) , 2024-09-29-0914
```
If you're focused on output quality and evaluation in LLMs, I’ve created r/AIQuality —a community dedicated to those of 
us working to build reliable, hallucination-free systems.

Personally, I’ve faced constant challenges with evaluating my
 RAG pipeline. Should I use DSPy to build it? Which retriever technique works best? Should I switch to a different gener
ator model? And most importantly, how do I truly know if my model is improving or regressing? These are the questions th
at make evaluation tough, but crucial.

With RAG and LLMs evolving rapidly, there wasn't a space to dive deep into these
 evaluation struggles—until now. That’s why I created this community: to share insights, explore cutting-edge research, 
and tackle the real challenges of evaluating LLM/RAG systems.

If you’re navigating similar issues and want to improve y
our evaluation process, join us. [https://www.reddit.com/r/AIQuality/](https://www.reddit.com/r/AIQuality/)
```
---

     
 
all -  [ LLamaParse vs LLMWhisperer? ](https://www.reddit.com/r/LangChain/comments/1fpvkdm/llamaparse_vs_llmwhisperer/) , 2024-09-29-0914
```
Looking for a solution to parse fairly complex PDFs (graphs, images, tables across multiple pages) into text to use for 
RAG and indexing - accuracy is pretty key. These two seem to come up the most often when searching online - with LlamaPa
rse recently coming out with their new premium version.

Which do folks normally use and why? Or is unstructured io norm
ally good enough

Are there any pdf2text benchmarks out there to run them against each other? This seems like a fairly c
ommon task
```
---

     
 
MachineLearning -  [ Built a web agent which call fill Google forms based on the user details [P] ](https://www.reddit.com/r/MachineLearning/comments/1fozud5/built_a_web_agent_which_call_fill_google_forms/) , 2024-09-29-0914
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

     
 
MachineLearning -  [ [P] Swapping Embedding Models for an LLM ](https://www.reddit.com/r/MachineLearning/comments/1fktvbj/p_swapping_embedding_models_for_an_llm/) , 2024-09-29-0914
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

     
 
MachineLearning -  [ [P] Review and suggest ideas for my chatbot ](https://www.reddit.com/r/MachineLearning/comments/1fb2mwl/p_review_and_suggest_ideas_for_my_chatbot/) , 2024-09-29-0914
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

     
 
MachineLearning -  [ [P] Lessons from Retrieval Augmented Generation ](https://www.reddit.com/r/MachineLearning/comments/1f9tvg7/p_lessons_from_retrieval_augmented_generation/) , 2024-09-29-0914
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

     
 
deeplearning -  [ What is the best approach for Parsing and Retrieving Code Context Across Multiple Files in a Hierarc ](https://www.reddit.com/r/deeplearning/comments/1fh58oz/what_is_the_best_approach_for_parsing_and/) , 2024-09-29-0914
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

     
 
deeplearning -  [ Month of August in AI ](https://www.reddit.com/r/deeplearning/comments/1f6zfz0/month_of_august_in_ai/) , 2024-09-29-0914
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

     
