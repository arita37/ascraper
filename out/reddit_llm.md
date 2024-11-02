 
all -  [ Mistral Large Model and streaming ](https://www.reddit.com/r/MistralAI/comments/1ghjt4o/mistral_large_model_and_streaming/) , 2024-11-02-0912
```
Hi,

I am using [ChatMistralAI](https://python.langchain.com/docs/integrations/chat/mistralai/) and [FastAPI](https://fa
stapi.tiangolo.com/) with the Python client and I am scratching my head on how to enable streaming successfully with Mis
tral Large. I am battling a lot of 422 and trying to find out what the issue is in the request I am sending. Since ChatM
istralAI should act as a wrapper and it abstracts away the details of constructing requests directly to the API, making 
it easier to use without needing to build raw HTTP requests. Therefore, my first attempt was this:

\`\`\`  
from fastap
i import FastAPI, HTTPException

from fastapi.responses import StreamingResponse

from langchain.chat\_models import Cha
tMistral

from pydantic import BaseModel



app = FastAPI()



class Question(BaseModel):

text: str

temperature: float
 = 0.7

max\_new\_tokens: int = 100



@app.post('/code-generation')  # corrected @ symbol

async def code\_generation(q
uestion: Question):

mistral\_api\_key = 'YOUR\_MISTRAL\_API\_KEY'



\# Initialize ChatMistral with streaming enabled


chat\_mistral = ChatMistral(

api\_key=mistral\_api\_key,

model='mistral-large',  # specify the model variant

temperat
ure=question.temperature,

max\_tokens=question.max\_new\_tokens,

stream=True

)



async def stream\_response():

try:


async for token in chat\_mistral.chat\_stream(messages=question.text):

yield token\['choices'\]\[0\]\['delta'\]\['con
tent'\]

except Exception as e:

raise HTTPException(status\_code=500, detail=str(e))



return StreamingResponse(stream
\_response(), media\_type='text/plain')

\`\`\`

However, I don't seem to get it right as I am banging my head with 422 
errors that I cannot clearly debug. I took a different approach, but still with no joy and using directly the `'https://
api.mistral.ai/v1/chat/completions' endpoint, as follows:`

`from fastapi import FastAPI, HTTPException`

`from fastapi.
responses import StreamingResponse`

`import requests`

`import json`

`app = FastAPI()`

`mistral_api_key = 'YOUR_MISTR
AL_API_KEY'`

u/app`.post('/code-generation')`

`async def code_generation(question: Question):`

`headers = {`

`'Autho
rization': f'Bearer {mistral_api_key}',`

`'Content-Type': 'application/json',`

`'Accept': 'application/json',`

`}`

`
payload = {`

`'model': 'mistral-large', # whatever model ID`

`'temperature': question.temperature,`

`'max_tokens': qu
estion.max_new_tokens,`

`'stream': True,`

`'messages': question.text`

`}`

`def mistral_endpoint(headers, payload):`


`try:`

`response = requests.post(`

`'https://api.mistral.ai/v1/chat/completions',`

`headers=headers,`

`json=payload
,`

`stream=True`

`)`

`response.raise_for_status() # Raises an error for non-200 responses`

`for line in response.ite
r_lines():`

`if line and line != b'data: [DONE]':`

`json_data = json.loads(line.decode('utf-8').replace('data: ', ''))
`

`yield json_data['choices'][0]['delta']['content']`

`except requests.exceptions.RequestException as e:`

`raise HTTP
Exception(status_code=500, detail=f'Error communicating with Mistral API: {e}')`

`return StreamingResponse(mistral_endp
oint(headers, payload), media_type='text/plain')`

What is the correct way to enable streaming for a Mistral Large model
? Do you directly use the `chat/completions` endpoint? What is exactly the payload I need to construct? What am I missin
g?

Thanks
```
---

     
 
all -  [ I was super frustated with langchain's pile of unnecessary abstractions, so I created something new ](https://www.reddit.com/r/LangChain/comments/1ghglbs/i_was_super_frustated_with_langchains_pile_of/) , 2024-11-02-0912
```
**Has anyone else been frustated writing and debugging langchain code?** There are so many classes and abstractions that
 don't seem to add much value. As a result, what really happens behind the curtains feel quite opaque. For me having low
-level control is very important. 

So I just published this open-source framework [**GenSphere**](https://github.com/oc
topus2023-inc/gensphere)**.** You build LLM applications with yaml files, that define an execution graph. Nodes can be e
ither LLM API calls, regular function executions or other graphs themselves. Because you can nest graphs easily, buildin
g complex applications is not an issue, but at the same time you don't lose control. 

There is also this Hub that you c
an push and pull projects from, so it becomes easy to share what you build and leverage from the community.

Its all ope
n-source. Would love to get your thoughts. Pls reach out or join the [discord server](https://discord.gg/DZFWMXJv) if yo
u want to contribute.
```
---

     
 
all -  [ Autonomous Dynamic Graph Creation ](https://www.reddit.com/r/LangChain/comments/1ghf7df/autonomous_dynamic_graph_creation/) , 2024-11-02-0912
```
Has anyone experimented with creating a planner agent that dynamically creates graphs to carry out complex tasks?  
I've
 built an agentic framework from scratch where each agents each hold specific personas and sets of tools and collaborate
 in a centralized conversation with the user.  
Each message received by an agent triggers an sort of 'internal monologu
e' which implements the ReAct framework.

But I've noticed that without clear directions, planning, and tasks assignment
s, the agent team really struggles to carry out complex tasks.

So I was thinking: it'd be great to implement a sort of 
plan-execute pattern with a planning agent. Ideally it would even create a LangGraph Graph.  
Models would even be train
ed on planning, kind of like how o1-preview has been trained on chain of thoughts.

Any thoughts? Anyone has experimente
d with this?  
Cheers!
```
---

     
 
all -  [ List of FREE and Best Selling Discounted Courses ](https://www.reddit.com/r/udemyfreebies/comments/1ghedzm/list_of_free_and_best_selling_discounted_courses/) , 2024-11-02-0912
```
# Udemy Free Courses for 02 November 2024

Note : Coupons might expire anytime, so enroll as soon as possible to get the
 courses for FREE.

* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/22077/)[ASP.NET](http://ASP.NET) MVC Complete Gu
ide using .NET Core \[.NET8 Updated\]
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/22076/)Become a professional i
nterior designer using sketch up pro
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/22075/)How To Make Money Everyd
ay Using AI ChatGPT /Fiverr.
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/22074/)Grow your Facebook page organica
lly 5000 follower in a week
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/22073/)AutoCAD 2D Floor Plan From Beginn
er To Advanced Level.
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/22072/)Complete Data Analyst Bootcamp From Bas
ics To Advanced
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/22071/)Mastering Figma from 0 to 100 (UI/UX Mastery 
Course)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/22070/)Elearning 2024: Create & Sell Online Courses
* [REDEE
M OFFER ](https://idownloadcoupon.com/udemy/22069/)All in One Pure Practical Social Media Marketing Course
* [REDEEM OFF
ER ](https://idownloadcoupon.com/udemy/22068/)Mathematics-Basics to Advanced for Data Science And GenAI
* [REDEEM OFFER 
](https://idownloadcoupon.com/udemy/22067/)Complete Data Science,Machine Learning,DL,NLP Bootcamp
* [REDEEM OFFER ](http
s://idownloadcoupon.com/udemy/22066/)Complete MLOps Bootcamp With 10+ End To End ML Projects
* [REDEEM OFFER ](https://i
downloadcoupon.com/udemy/22065/)Complete Generative AI Course With Langchain and Huggingface
* [REDEEM OFFER ](https://i
downloadcoupon.com/udemy/22064/)Building Gen AI App 12+ Hands-on Projects with Gemini Pro
* [REDEEM OFFER ](https://idow
nloadcoupon.com/udemy/22063/)Beginner Affiliate Marketing To Start In 1 Day – 2024
* [REDEEM OFFER ](https://idownloadco
upon.com/udemy/22062/)Fiverr Freelancing 2024: Sell Like The Top 1%
* Create (Artificial Intelligence) AI VIDEOS WITH ZE
RO FILMING
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/22061/)
* [REDEEM OFFER ](https://idownloadcoupon.com/udem
y/22060/)Linux A to Z 2025: Secure Your Dream IT Job with Confidence
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy
/22059/)\[NEW\] Ultimate AWS Certified AI Practitioner AIF-C01
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/22058
/)Red Teaming | Exploit Development with Assembly and C |MSAC+
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/22057
/)Practical Cisco Networking Labs in Cisco Packet Tracer
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/22056/)Comp
uter Networks Fundamentals
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/22055/)IP Addressing and Subnetting – Zer
o to Hero
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/22054/)Information Security Fundamentals
* [REDEEM OFFER ]
(https://idownloadcoupon.com/udemy/22053/)JN0-664: Juniper Network Professional Security Practice 2024
* [REDEEM OFFER ]
(https://idownloadcoupon.com/udemy/22052/)Professional Diploma in CRM Platforms Management
* [REDEEM OFFER ](https://ido
wnloadcoupon.com/udemy/22051/)JavaScript Coding Interview Questions \[with SOLUTIONS\]
* [REDEEM OFFER ](https://idownlo
adcoupon.com/udemy/22050/)Essential Microsoft Excel from Beginner to Advance level
* [REDEEM OFFER ](https://idownloadco
upon.com/udemy/22049/)Android Training & Certification – 49 Projects
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy
/22048/)iOS 11 Mobile Development and Certification – iPhone & iPad
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/
22047/)Wireshark Ninja | Mastering Real Wireshark PROALL|2023WSHRK+
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/
22046/)Mastering Network Security: Defending Against Cyber Threats
* Facebook Ads Marketing – Start Lead Generation Busi
ness 2023
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/22045/)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy
/22044/)6 Practice Tests – AWS Certified Architect Professional
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/2204
3/)Capcut Ninja: Mastering Video Editing Basics to Advanced
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/22042/)J
ava Network Programming – Mastering TCP/IP : CJNP+ JAVA+
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/22041/)Crim
inology and Criminal Psychology | Certified CSI+ Course
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/22040/)The C
omplete Photoshop Masterclass: From 0 to Hero
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/22039/)Passive Income 
By Making Udmy Courses 2023
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/22038/)Build Shopify store & Run Faceboo
k Page Likes Ad In 2023
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/22037/)Configuración y Optimizacion de tu Pá
gina de Facebook 2023
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/22036/)Register Company in UK Get paypal & Str
ipe Business Hindi
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/22035/)Facebook Conversions Ads Marketing For Sel
ling Products 2023
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/22034/)Facebook Ads And Marketing – Lead Generati
on Pro
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/22033/)Google Adwords Crash Course 2023
* [REDEEM OFFER ](htt
ps://idownloadcoupon.com/udemy/22032/)Run Search Ad In Google Ads & Easy SEO For Beginners-2023
* [REDEEM OFFER ](https:
//idownloadcoupon.com/udemy/22031/)Facebook Ads Marketing For Events Organic & Paid Strategy
* [REDEEM OFFER ](https://i
downloadcoupon.com/udemy/22030/)Facebook Ads Lead Generation Marketing for business
* Digital Marketing Business With Go
ogle My Business
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/22029/)
* [REDEEM OFFER ](https://idownloadcoupon.co
m/udemy/22028/)Facebook Ads & Facebook Marketing Funnel Crash Course- 2023
* [REDEEM OFFER ](https://idownloadcoupon.com
/udemy/22027/)Run Digital Marketing Ad Using Google Adwords Express
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/
22026/)Facebook Ads Google My Business & Google Ads (Adwords) 2023
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/2
2025/)Facebook Marketing & Facebook Ads Course For Beginners 2023
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/22
024/)Facebook Ads Marketing Crash Course Traffic & leads – 2023
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/2202
3/)Google Ads And Tiktok Ads Crash Course (Hindi/ Urdu)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/22022/)How T
o Edit Viral Shorts In CapCut
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/22021/)Tiktok Marketing & Shopify Ecom
merce store (hindi/urdu)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/22020/)Color Theory: Learn The Art and Scie
nce of Colors
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/22019/)Ultimate Photoshop Mock-Up Creation Course
* [R
EDEEM OFFER ](https://idownloadcoupon.com/udemy/22018/)Digital Marketing Business Online For Free Social Media
* [REDEEM
 OFFER ](https://idownloadcoupon.com/udemy/22017/)Canva Design Crash Course
* [REDEEM OFFER ](https://idownloadcoupon.co
m/udemy/22016/)Secret Facebook Ads Targeting Pro Stratigies 2023 In Hindi
* [REDEEM OFFER ](https://idownloadcoupon.com/
udemy/22015/)Design Principles, Typography & Color Theory in 1 MegaCourse
* [REDEEM OFFER ](https://idownloadcoupon.com/
udemy/22014/)Facebook Marketing + Whatsapp Ads (CASE STUDY) Hindi 2023
* Google Ads Mastery\~ Beginner To Pro \~ HINDI/U
RDU 2023
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/22013/)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/
22012/)Tiktok Ads marketing Crash Course For Beginners (Hindi/Urdu)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/
22011/)Facebook Pixel Tracking Shopify \~ Apple iOS14 \~ Ecommerce
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/2
2010/)Como crear y configurar tu canal de Youtube desde cero 2023
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/22
009/)Product Hunting for Dropshipping stores
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/22008/)Get 10,000 faceb
ook page followers at cheap Hindi
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/22007/)Learn Camtasia Video Editin
g Masterclass Professional
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/22006/)Facebook Ads & Ecommerce Easy Cour
se 2023 Hindi
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/22005/)Easy Instagram Marketing In Hindi
* [REDEEM OFF
ER ](https://idownloadcoupon.com/udemy/22004/)Facebook Ads Marketing In Hindi/Urdu 2023
* [REDEEM OFFER ](https://idownl
oadcoupon.com/udemy/22003/)The Complete Illustrator Masterclass: From 0 to Hero
* [REDEEM OFFER ](https://idownloadcoupo
n.com/udemy/22002/)Building a shopify store and CJ dropshipping
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/2200
1/)Marketing en Facebook Ads – Leads /Clientes Potenciales 2023
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/2200
0/)Facebook Ads Marketing Targeting Strategies \~Hindi 2023
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/21999/)F
acebook Ads Targeting Strategies For Success Fast 2023
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/21998/)Get Fo
llowers And engagement with Facebook Ads (easy mode)
* Estrategias Pro de Targeting de Audiencia con Facebook Ads
* [RED
EEM OFFER](https://idownloadcoupon.com/udemy/21997/)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/21996/)CSS Fund
amentals: Comprehensive Training for Web Developers
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/21995/)GRE Maste
ry: 5 Comprehensive Practice Tests
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/21994/)DEA-1TT4: Dell EMC Associa
te Practice test 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/21993/)Seo Training Masterclass 2024 : Beginne
r to Advance Startegy
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/21992/)Professional Diploma in Office Administ
ration Management
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/21991/)DES-1423: Dell EMC Specialist Isilon Soluti
on Practice test
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/21990/)DES-1D12: Dell EMC Specialist – Midrange Sto
rage Solutions
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/21989/)DES-6322: Dell EMC Specialist VxRail Appliance
 Practice test
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/21988/)C1000-010: IBM Cloud Pak for Data v4.x Practic
e test 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/21987/)E20-555: Dell EMC Isilon Solution and Design Spec
ialist Exam
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/21986/)E20-393: Dell EMC Unity Solution Specialist Pract
ice test 24
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/21985/)DEA-41T1: Dell EMC PowerEdge Associate Practice t
est 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/21984/)5V0-22.23: VMware Certified Professional – VMware vS
AN 8.x
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/21983/)Professional Diploma in Digital Products Management
* 
[REDEEM OFFER ](https://idownloadcoupon.com/udemy/21982/)Hands-On Python Machine Learning with Real World Projects
* How
 neuromarketing can influence buying behavior
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/21981/)
* [REDEEM OFFER
 ](https://idownloadcoupon.com/udemy/21980/)The Complete Growth Mindset Course – The Mindset for Success
* [REDEEM OFFER
 ](https://idownloadcoupon.com/udemy/21979/)Home Workout Habits in 10 Min – Fitness for Busy-Lazy People
* [REDEEM OFFER
 ](https://idownloadcoupon.com/udemy/21978/)The Complete Talking Head Video Production Masterclass
* [REDEEM OFFER ](htt
ps://idownloadcoupon.com/udemy/21977/)Unlocking the Power of Relative Clauses in English language
* [REDEEM OFFER ](http
s://idownloadcoupon.com/udemy/21976/)Body Language in the Workplace
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/
21975/)Persuasion in Business Communications
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/21974/)Laravel 10 Essen
tials: User Roles & Permissions with Spatie
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/21973/)HTML5 Certificati
on Prep: Comprehensive Practice Tests
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/21972/)Bootstrap Mastery: Buil
d Responsive Websites Like a Pro
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/21971/)Complete jQuery Masterclass:
 From Beginner to Expert
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/21970/)JavaScript Mastery From Basics to Ad
vanced
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/21969/)ChatGPT Mastery: From Creative Writing to Coding Solut
ions
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/21968/)CSS3 Certification Prep: Comprehensive Practice Tests
* 
[REDEEM OFFER ](https://idownloadcoupon.com/udemy/21967/)Dart Mastery – Become a Dart Master From Zero to Hero
* [REDEEM
 OFFER ](https://idownloadcoupon.com/udemy/21966/)HTML5 CSS3 and JavaScript for Beginners: From Zero to Hero
* Mastering
 Postman: A Comprehensive API Testing Course
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/21965/)
* [REDEEM OFFER 
](https://idownloadcoupon.com/udemy/21964/)Laravel and Postman Rest API Development: Beginner to Pro
* [REDEEM OFFER ](h
ttps://idownloadcoupon.com/udemy/21963/)Wealth Creation Blueprint: From 9 to 5 to Financial Freedom
* [REDEEM OFFER ](ht
tps://idownloadcoupon.com/udemy/21962/)Frontend Web Development HTML5 CSS3 JavaScript and Bootstrap
* [REDEEM OFFER ](ht
tps://idownloadcoupon.com/udemy/21961/)cPanel Essentials: Mastering Web Hosting Management
* [REDEEM OFFER ](https://ido
wnloadcoupon.com/udemy/21960/)HTML5 CSS3 JavaScript Bootstrap and Jquery Masterclass
* [REDEEM OFFER ](https://idownload
coupon.com/udemy/21959/)Public Speaking Skills: Give a Great Informational Speech
* [REDEEM OFFER ](https://idownloadcou
pon.com/udemy/21958/)Dart and Flutter: The Ultimate Mobile App Development Course
* [REDEEM OFFER ](https://idownloadcou
pon.com/udemy/21957/)HTML and CSS for Web Designers: From Basics to Beautiful
* [REDEEM OFFER ](https://idownloadcoupon.
com/udemy/21956/)Sales Skills Training: Free Sales Generation Seminars
* [REDEEM OFFER ](https://idownloadcoupon.com/ude
my/21955/)Presentation Skills -Deliver an Excellent Ceremonial Speech
* [REDEEM OFFER ](https://idownloadcoupon.com/udem
y/21954/)Public Speaking: Speak Like a High-Powered Executive
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/21953/
)Complete Good Sleep Habits Course – Sleep Better Tonight!
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/21952/)Co
mplete Willpower Course – Build Self Control & Good Habits
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/21951/)Pe
rsuasion: Give a Persuasive Presentation
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/21950/)The Complete Virtual
 Sales Presentation Course Sales Skills

GET MORE FREE ONLINE COURSES WITH CERTIFICATE – [CLICK HERE](https://idownloadc
oupon.com/)
```
---

     
 
all -  [ Autogen needs improvement. How no one felt the need for call back function ](https://www.reddit.com/r/LangChain/comments/1ghcvi5/autogen_needs_improvement_how_no_one_felt_the/) , 2024-11-02-0912
```
I know this is langchain subreddit but thought to discuss here as most agent developers are there..

I have been playing
 with autogen for few hours to understand.
I immediately felt two needs,
Suppose there are two agents, writer and review
er. 
The termination condition is when reviewer gives it rating of 8 or more.
My need is execution of certain functions 
when this terminal condition is met, currently what i found is only way is custom implementation.
Second, 
For human in 
the loop, I don't want my user to enter prompt via terminal, I need it to be through WhatsApp message or some slack inte
gration. How do I do this?

Suggestions are welcomed. Or any other framework with these features.. 
```
---

     
 
all -  [ Integrating External REST API LLM Calls with LangGraph ](https://www.reddit.com/r/LangChain/comments/1ghc5pg/integrating_external_rest_api_llm_calls_with/) , 2024-11-02-0912
```

I'm working on implementing an agent system using LangGraph, but with a twist - my LLM calls need to go through a REST 
API service instead of using direct LLM integrations.

- Using LangGraph for agent orchestration
- Need to make LLM call
s via REST API endpoints
- Looking to build a custom agent that works with this architecture

1. Is it possible to integ
rate external REST API calls for LLM interactions within the LangGraph framework?
2. Are there any examples or best prac
tices for creating custom agents that use HTTP requests instead of direct LLM integrations?
3. What would be the recomme
nded approach to handle asynchronous REST API calls in this context?

## Technical Details Needed
- Best way to wrap RES
T API calls within LangGraph's expected interfaces
- How to handle authentication and session management
- Proper error 
handling and retry mechanisms
- State management considerations

Any guidance, examples, or pointers to relevant documen
tation would be greatly appreciated. Thank you!
```
---

     
 
all -  [ Fuzzy matching medical terminology using AI ](https://www.reddit.com/r/learnprogramming/comments/1ghb3ei/fuzzy_matching_medical_terminology_using_ai/) , 2024-11-02-0912
```
Have a txt file with 2 columns, description and corresponding code. Need help intelligently matching user inputted free-
form text to the description, and returning the corresponding code.



Background:

I am building a medical pricing webs
ite. The user inputs free form text (à la Google) describing the condition and receives pricing at local hospitals.

Med
ical billing is a labyrinth, separated into inpatient and outpatient services and diagnosis codes. A diagnosis code (ICD
10) will usually translate into an inpatient code (DRG), but not always. Other times, ICD10 codes will translate to the 
wrong DRG code. 

I have been using a forward searching approach, searching first for the ICD10 code and translating it 
to a DRG. As an example, a search for 'heart transplant' yields the ICD10 code Z94.1 which corresponds to DRGs 314-316 (
'Other Circulatory System Diagnoses'). In fact, DRGs 001 and 002 ('Heart Transplant') are more correct, but do not have 
a corresponding ICD10 code. 

[CMS.gov](http://CMS.gov) has appendices that list exactly which ICD10 corresponds with wh
ich DRG as well as DRG numbers and descriptions. Not all DRGs have a corresponding ICD10 code, so **I will have to match
 the user-inputted free form text to DRGs directly.**



Things I have explored:

String matching using Jaccard Distance
/ Levenshtein Distance/ Jaro-Winkler: not the best since most laypeople will not know the exact medical terminology ('sn
oring' symptom vs 'sleep apnea' medical term)

Zero-shot approach with Gemini and OpenAI. Both AIs will hallucinate and 
return the wrong DRGs. 

* Fine tuning: OpenAI, Gemini, and Llama3.2 both require a question and answer dataset, best if
 50 examples per classification (DRG code). This is... not easy and probably not going to be very accurate. Hard to gues
s what a user might input in free form text.
* Corpus of documents for Retrieval Augmented Generation (RAG): LangChain V
ectara, Gemini, Vertex AI for RAG: This is a promising option but examples on the [Vectara](https://python.langchain.com
/v0.1/docs/integrations/providers/vectara/vectara_summary/) site show that this approach is better for summarizing, or r
etrieving relevant 'chunks', than strict regurgitation.
* Vertex AI for tabular data: similar challenges with providing 
examples for fine tuning
* QLoRA/ LoRA: probably much more technically oriented and more than I need, also increased har
dware requirements.

Giving OpenAI/ Gemini a complete list of all the DRG descriptions with each prompt, asking the AI t
o match with the appropriate entry. This would use a large number of tokens ($) for every prompt. Is there a way to keep
 this in memory? Is that what the Corpus is? If I provide a text file as a document in the Corpus, is the AI smart enoug
h to match the user input to the DRG description in the file and return the corresponding DRG code in the file in a diff
erent column?
```
---

     
 
all -  [ Tools / guidance  ](https://www.reddit.com/r/LocalLLM/comments/1gha8gy/tools_guidance/) , 2024-11-02-0912
```
I want to create a model that analyzes specific books I've selected about coding and other related topics. My goal is fo
r this model to help integrate new features into the app, acting as a consultant by leveraging the knowledge from these 
books as well as the app's source code that I provide. I've already developed a basic model using LangChain and LLaMA th
at retrieves answers from the books, but I’m unsure how to proceed from this point. What steps should I take next to enh
ance this model? 
```
---

     
 
all -  [ Started with one node. Now, look at it!  ](https://i.redd.it/shf35e2jabyd1.png) , 2024-11-02-0912
```

```
---

     
 
all -  [ Langchain SelfQueryRetriever unable to read Structured Query ](https://www.reddit.com/r/LangChain/comments/1gh8exz/langchain_selfqueryretriever_unable_to_read/) , 2024-11-02-0912
```
Anyone using SelfQueryRetriever? I am trying to implement this retriever to create a RAG Chatbot. However, the retriever
 seems to have trouble reading my Structured Query. I have already tried both SelfQueryRetriever() and SelfQueryRetrieve
r.from\_llm(), and they both give different errors. 

Appreciate if anyone has any experience in this, thanks!
```
---

     
 
all -  [ CCD ETL via LangGraph ](https://youtu.be/gZYu45aw3Hw?si=r5QWuGELvSE9rh-p) , 2024-11-02-0912
```
Built a tool for extracting healthcare CCD data into custom schemas. This can speed up building of interfaces for connec
ting hospitals, providers and independent practices to each other and to HIE’s.
```
---

     
 
all -  [ When using `with_structured_output` with pydantic BaseModel, does the Field description do anything? ](https://www.reddit.com/r/LangChain/comments/1ggvkf7/when_using_with_structured_output_with_pydantic/) , 2024-11-02-0912
```
Basically the title. I am experimenting the \`with\_structured\_output\` and I find that the llm uses the variable name 
to know what to populate. 

`phrases_with_dumb: list[str]`

I thought the pydantic's Field description would affect the 
behavior too, but seems like it's not affecting how the model generates the data. 

`phrases: list[str] = Field(descript
ion='list of phrases with the word dumb')`

So should I assume that Field description is not used when the model generat
es the data? 
```
---

     
 
all -  [ Get responses longer than the llm context window ](https://www.reddit.com/r/LangChain/comments/1ggv50c/get_responses_longer_than_the_llm_context_window/) , 2024-11-02-0912
```
Hi, is there a way to get a response longer than the allowed context window e.g by using loops or threads. In gpt ui for
 instance, I'd instruct it to let me know if there's more and continue when I respond with continue. Thanks for the help

```
---

     
 
all -  [ VERY slow Document creation ](https://www.reddit.com/r/LangChain/comments/1ggt5r7/very_slow_document_creation/) , 2024-11-02-0912
```
Hey! Im trying to create Langchain [Document](https://python.langchain.com/v0.2/api_reference/core/documents/langchain_c
ore.documents.base.Document.html#langchain_core.documents.base.Document) objects from JSON objects, but Document creatio
n is taking *VERY* long. using tqdm, im seeing 30-40i/s, then a pause for 10 seconds, dip to 3i/s for 20 seconds, then b
ack up to 20i/s, ect. ect.

`tqdm import tqdm`  
`from langchain_core.documents import Document`  
`from langchain_commu
nity.graph_vectorstores.links import METADATA_LINKS_KEY, Link`  
`import jsondef create_documents(json_file):`  
`docume
nts = {}`  
  
`with tqdm(desc='Creating documents', mininterval=1) as pbar:`  
`for line in json_file:`  
`if not line.
strip():`  
`continue`  
  
`line_data = json.loads(line)`  
`source, targets = next(iter(line_data.items()))`  
  
`# C
reate set of links more efficiently`  
`links = {`  
`Link.outgoing(kind='href', tag=target)`  
`for target in targets` 
 
`}`  
`links.add(Link.incoming(kind='href', tag=source))`  
  
`documents[source] = Document(`  
`id=source,`  
`page_
content='',`  
`metadata={`  
`'content_id': source,`  
`METADATA_LINKS_KEY: list(links)`  
`}`  
`)`  
  
`print(f'Samp
le of documents:')`  
`for i, (title, doc) in enumerate(list(documents.items())[:5]):`  
`print(f'Document {i+1}:')`  
`
print(f'  Title: {title}')`  
`print(f'  ID: {doc.id}')`  
`print(f'  Content ID: {doc.metadata['content_id']}')`  
`pri
nt(f'  Number of links: {len(doc.metadata[METADATA_LINKS_KEY])}')`  
`print(f'  Sample links: {doc.metadata[METADATA_LIN
KS_KEY][:5]}')`  
`print()`  
  
`return documentswith open('test.json', 'r', encoding='utf-8') as json_file:`  
  `prin
t(f'Data loaded from 'links.json'')`  
  `print('Creating documents...')`  
  `documents = create_documents(json_file)` 
 
  `print(f'Created {len(documents)} documents')`



Anyone know whats going on?
```
---

     
 
all -  [ What is the other best alternative to LangGraph? ](https://www.reddit.com/r/LangChain/comments/1ggrqis/what_is_the_other_best_alternative_to_langgraph/) , 2024-11-02-0912
```
I am a software engineer with 5+ years of experience and decent experience with LangChain. Over the past week, I am buil
ding a stock analyst agent on LangGraph, and the experience has been terrible.

The documentation and tutorials make me 
feel dumb, even simple tasks seem unnecessarily difficult, which has left me frustrated. I’ve decided not to proceed wit
h LangGraph for the time being,I just can’t imagine using it to build 10-20 more nodes.

Is there an alternative on the 
market today that any of you are using? Ideally, something in async Python.
```
---

     
 
all -  [ Is this possible? ](https://www.reddit.com/r/LangChain/comments/1ggqtad/is_this_possible/) , 2024-11-02-0912
```
I have a JSON dataset of the format:
[
{
key1: val1,
key2: val2,
key3: val3,
...
}
{
key1: val1,
key2: val2,
key3: val3

...
}
...
]

There is data in one key which relates to another one.

Is it possible to build a RAG chatbot, in such a wa
y that it accepts dynamic inputs and gives answers based on the key.

[1] For instance, let's say key1 is dog and key2 i
s cat, the rag chatbot should detect from the chat input if it contains cat or dog and should return  the value based on
 the key. If the chat message contains anything related to dog in it, it should return the answer from the dog key else 
if the message has anything related to catch in it, it should return from the cat key.

[2] The RAG model should also ge
nerate outcome based on the following scenario: let's say if the value4 and value5 depends on what is given in value3.


[3]Another case is, value5 and value6 are numbers. The chatbot RAG should make sure it provides information in such a wa
y that if the user mentions any number and the number is in between value5 and value6, it should return the output from 
value4 or value5 based on the logic in point [1]


Could you guys please let me know if this is possible, cause i couldn
't find any example over the internet. 
```
---

     
 
all -  [ AWS certification for GenAI after AI practitioner? ](https://www.reddit.com/r/AWSCertifications/comments/1ggpbv2/aws_certification_for_genai_after_ai_practitioner/) , 2024-11-02-0912
```
Is there a good certification to do specifically for GenAI on AWS? I'm more interested in leveraging GenAI tools and not
 on the usual route of ML sagemaker models etc.

If not, what other certifications do you recommend tailored for GenAI? 
I'm right now working with OpenAI and want to go deeper into aspects of finetuning, perhaps may langchain etc. 

Sorry, 
just posting a long question, but my intent is to get a certification while also working on my startup idea. Right now, 
I'm mostly doing prompt engineering and some AWS plumbing and hence finding ways of expanding my horizons.
```
---

     
 
all -  [ Jupyter not honoring Conda environments? ](https://www.reddit.com/r/JupyterNotebooks/comments/1ggmaty/jupyter_not_honoring_conda_environments/) , 2024-11-02-0912
```
Hi all!

I've been using jupyter on an off for a while, but I need to start using it a lot more regularly, and I need to
 integrate with conda virtual environments.

Working on a new ubuntu 24.04 install, I installed Anaconda, then created a
 new virtual environment and installed jupyter:

    conda create -n jupyter python=3.12
    conda activate jupyter
    
pip install jupyterlab
    jupyter lab
    ... 

So far so good, everything running as expected. So I then create anothe
r conda environment for a new project and register it with jupyter via ipykernel.

    conda create -n rag-llama3.2 pyth
on=3.11
    conda activate rag-llama3.2
    python -m ipykernel install --user --name=rag-llama3.2

The ipykernel part w
as completely new to me, I was following a medium post: [https://medium.com/@nrk25693/how-to-add-your-conda-environment-
to-your-jupyter-notebook-in-just-4-steps-abeab8b8d084](https://medium.com/@nrk25693/how-to-add-your-conda-environment-to
-your-jupyter-notebook-in-just-4-steps-abeab8b8d084)

So I now have jupyter running in its own conda env, and a new env 
to use for my project. This is where things get very strange. I jump in to the jupyter console, create a new notebook, a
nd select the newly registered kernel from the dropdown, all seems fine. I start installing a few packages and writing a
 little code:

    ! pip install langchain-nomic
    ! pip install -qU langchain-ollama
    ! pip list | grep langchain

    langchain-core            0.3.14
    langchain-nomic           0.1.3
    langchain-ollama          0.2.0

Packages i
nstalled, so I begin with an import:

    # LLM using local Ollama
    
    ### LLM
    from langchain_ollama import Cha
tOllama
    
    local_llm = 'llama3.2:3b-instruct-fp16'
    docker_host = 'http://127.0.0.1:11434'
    
    llm = ChatO
llama(model=local_llm, temperature=0, api_base_url=docker_host)
    llm_json_mode = ChatOllama(model=local_llm, temperat
ure=0, format='json', api_base_url=docker_host)

Computer says no!

    ------------------------------------------------
---------------------------
    ModuleNotFoundError                       Traceback (most recent call last)
    Cell In[
4], line 4
          1 # LLM using local Ollama
          2 
          3 ### LLM
    ----> 4 from langchain_ollama impor
t ChatOllama
          6 local_llm = 'llama3.2:3b-instruct-fp16'
          7 docker_host = 'http://127.0.0.1:11434'
    

    ModuleNotFoundError: No module named 'langchain_ollama'------------------------------------------------------------
---------------
    ModuleNotFoundError                       Traceback (most recent call last)
    Cell In[4], line 4
 
         1 # LLM using local Ollama
          2 
          3 ### LLM
    ----> 4 from langchain_ollama import ChatOllama

          6 local_llm = 'llama3.2:3b-instruct-fp16'
          7 docker_host = 'http://127.0.0.1:11434'
    
    ModuleN
otFoundError: No module named 'langchain_ollama'

So the modules are installed, but I can't import them. At this point I
 started hunting around and found a few commands to help identify the problem:

    !jupyter kernelspec list --json
    

    {
      'kernelspecs': {
        'python3': {
          'resource_dir': '/home/gjws/anaconda3/envs/jupyter/share/ju
pyter/kernels/python3',
          'spec': {
            'argv': [
              'python',
              '-m',
          
    'ipykernel_launcher',
              '-f',
              '{connection_file}'
            ],
            'env': {},
  
          'display_name': 'Python 3 (ipykernel)',
            'language': 'python',
            'interrupt_mode': 'signa
l',
            'metadata': {
              'debugger': true
            }
          }
        },
        'rag-llama3.2'
: {
          'resource_dir': '/home/gjws/.local/share/jupyter/kernels/rag-llama3.2',
          'spec': {
            'a
rgv': [
              '/home/gjws/anaconda3/envs/rag-llama3.2/bin/python',
              '-Xfrozen_modules=off',
       
       '-m',
              'ipykernel_launcher',
              '-f',
              '{connection_file}'
            ],
  
          'env': {},
            'display_name': 'rag-llama3.2',
            'language': 'python',
            'interrup
t_mode': 'signal',
            'metadata': {
              'debugger': true
            }
          }
        }
      }

    }
    /home/gjws/anaconda3/envs/jupyter/bin/python{
      'kernelspecs': {
        'python3': {
          'resource_
dir': '/home/gjws/anaconda3/envs/jupyter/share/jupyter/kernels/python3',
          'spec': {
            'argv': [
     
         'python',
              '-m',
              'ipykernel_launcher',
              '-f',
              '{connectio
n_file}'
            ],
            'env': {},
            'display_name': 'Python 3 (ipykernel)',
            'language
': 'python',
            'interrupt_mode': 'signal',
            'metadata': {
              'debugger': true
          
  }
          }
        },
        'rag-llama3.2': {
          'resource_dir': '/home/gjws/.local/share/jupyter/kernels/
rag-llama3.2',
          'spec': {
            'argv': [
              '/home/gjws/anaconda3/envs/rag-llama3.2/bin/pytho
n',
              '-Xfrozen_modules=off',
              '-m',
              'ipykernel_launcher',
              '-f',
  
            '{connection_file}'
            ],
            'env': {},
            'display_name': 'rag-llama3.2',
      
      'language': 'python',
            'interrupt_mode': 'signal',
            'metadata': {
              'debugger': 
true
            }
          }
        }
      }
    }
    
    !which -a python
    /home/gjws/anaconda3/envs/jupyter/b
in/python

So to my untrained eyes, jupyter is seeing both the jupyter conda environment and the rag-llama3.2 environmen
t and getting confused.

Now I don't know where to go.

Have I done something fundamentally wrong?

Should I NOT be runn
ing jupyter in its own venv and just install it globally?

Have I screwed up the ipykernel steps somewhere?

Any help wo
uld be much appreciated. I've been at this for hours and have hit a brick wall :(

Thanks for taking the time to read al
l this!!!
```
---

     
 
all -  [ Which version is better, the shorter or longer one? I've changed my carrer. ](https://www.reddit.com/r/resumes/comments/1ggm0mc/which_version_is_better_the_shorter_or_longer_one/) , 2024-11-02-0912
```
[Long Version](https://preview.redd.it/2ytulhse05yd1.png?width=1172&format=png&auto=webp&s=203467d1c9fb5b63f4b973c348b91
eca6d7399bc)

  


[Short Version](https://preview.redd.it/8mff2rhk05yd1.png?width=1171&format=png&auto=webp&s=35bfbc3a5
9e965629d49b174519825b4c3f3d94f)

  
The short version deletes my former experience and moves a 'Collaborative Project' 
from 'Experience' to the 'Projects Highlights' section, where I leave only 3 projects. The long version has more info: m
ore projects and more experience, with the collaborative project as an experience.

I prefer the short one, because I pu
t all the most important info on the first page, but I want to make sure that the info I don't show on this version is n
ot THAT important.

Any opinions?

Thanks in advance.
```
---

     
 
all -  [ ChatGPT Prompting Method ](https://www.reddit.com/r/PromptEngineering/comments/1ggfoax/chatgpt_prompting_method/) , 2024-11-02-0912
```
Not too long ago, people were posting ChatGPT prompts that made the chat window turned into an interactive q&a. It may h
ave been connected with Langchain, but I can't seem to find any of those types of posts. Those types of prompts also oft
en had emojis as part of its design and user interface. Does anyone remember what I'm talking about?
```
---

     
 
all -  [ 🌟 [Open Source] FlutterVoiceFriend – Open Source Voice Chatbot Framework for Flutter Devs! 🚀 ](https://www.reddit.com/r/FlutterDev/comments/1ggf4hw/open_source_fluttervoicefriend_open_source_voice/) , 2024-11-02-0912
```
Hey devs!

A few months ago, I was searching everywhere for a voice chatbot framework to use with Flutter, especially af
ter discovering that Langchain had been ported to Flutter. My goal was to create a **mindful self-compassion assistant f
or kids**, but I couldn’t find any ready-made solution for the setup I had in mind. So, I decided to build my own and th
en to open source it, this is a story behind **FlutterVoiceFriend**!

**FlutterVoiceFriend is far from perfect, but I be
lieve it can help others get started on their voice chatbot journey.**

👉 [GitHub Repo: FlutterVoiceFriend](https://gith
ub.com/jbpassot/flutter_voice_friend/)

# What is FlutterVoiceFriend?

It’s an open-source Flutter app framework that co
mbines **Langchain, OpenAI for TTS/NLP**, and multiple Speech-to-Text (STT) options (including Deepgram for online and o
ffline STT) to create **interactive, voice-driven chatbots**.

# Why it Might Be Helpful 🚀:

Whether you’re working on a
 virtual assistant, educational companion, or a voice-driven game, FlutterVoiceFriend gives you a flexible starting poin
t to create voice-based applications that are **fully customizable** and cross-platform.

# Key Features:

* **Voice-to-
Voice Conversations**: Speak with the bot and get natural voice responses!
* **Multiple Speech Recognition Options**: Bo
th on-device and cloud STT, making it versatile for different environments and device capabilities.
* **Natural Language
 Processing**: Langchain + OpenAI models for creating more natural, nuanced dialogues.
* **Customizable TTS**: Set up di
fferent voices and languages to give your chatbot a unique “personality.”
* **Built with Flutter**: Compatible across iO
S, Android, and Web platforms from a single codebase.

# The App That Started It All:

Here’s the app I originally built
 using this framework – [The Friend In Me](https://apps.apple.com/us/app/the-friend-in-me/id6605936938), a mindfulness c
ompanion for kids.

# Looking for Contributors!

If you’re interested in building out features, writing tests, optimizin
g for different use cases, or just want to contribute ideas, I’d love for you to get involved. Whether you’re a Flutter 
guru or just excited to work with voice/chatbot tech, let’s make this better together!

# Happy coding! 😊
```
---

     
 
all -  [ Production-ready and fast RAG Solution for Generating JSONs Based on PDF Documents my quick research ](https://www.reddit.com/r/LocalLLaMA/comments/1gge5bh/productionready_and_fast_rag_solution_for/) , 2024-11-02-0912
```
Hey everyone!

I’m exploring options for a production-grade Retrieval-Augmented Generation (RAG) setup to generate JSON 
data from documents. My goal is to get **accurate, commercial-ready outputs** as quickly as possible. I’m open to models
, as long as the results are reliable and production-suited. After some research and help from GPT, I’ve narrowed down t
o a few options and would appreciate insights or any advice based on experience.

# Current Options Considered GPT table
:

https://preview.redd.it/azd7m59yg3yd1.png?width=899&format=png&auto=webp&s=0dd00c476aceeef1ddd56aa7ba0a3709c9bcf54a


https://preview.redd.it/qtzbduuzg3yd1.png?width=795&format=png&auto=webp&s=31dded5c8a05fde171552ff9b6b4b8fff4e108f8

Key
 Priorities:

* **Accuracy and production-readiness** for JSON outputs.
* **Commercial use** licensing and support.
* **
Ease of scaling and deployment** for enterprise production (though I’m flexible on initial setup time if results are sol
id).
* I could pay

AWS Bedrock seem like the best path for this, or would something else better fit my needs? Does anyo
ne have experience with Bedrock in a production RAG workflow, or should I be looking deeper into SageMaker or an open-so
urce alternative?

It seems that Haystack would be nice for production, customization and then putting it on the cloud b
ut with a bit more time investment.
```
---

     
 
all -  [ Are there any Local LLMs with COT capabilities? ](https://www.reddit.com/r/LangChain/comments/1ggcalv/are_there_any_local_llms_with_cot_capabilities/) , 2024-11-02-0912
```
Hi All,

Been dabbing at Ollama to create a custom RAG hosted in local server (for security reasons). Now the client wan
ts a Chain of Thought (COT) capability as well. Basically the client wants basic numerical functionality. For e.g. 'I am
 doing 80 mph on I 80. What is the average speed here and how much slower or faster I am'.

The data has details about a
vg speed of I80. example 90 mph. So the RAG application should say 'I am 10mph slower than average speed.'

Are there an
y COT capable Local LLMs? If not any idea how to solve the above problem?
```
---

     
 
all -  [ Prod Level RAG Applications ](https://www.reddit.com/r/Rag/comments/1ggc76e/prod_level_rag_applications/) , 2024-11-02-0912
```
Hi everyone, I have been learning Rag for months and I have created some question-answering applications using LangChain
 to add to my resume. But I am wondering in real life, in production level rag applications, what is the difference from
 my local simple rag project? Which vectorstore do you use for your project, or embedding model? open source or api?

  

What are the biggest differences between production-level RAG applications and simple RAG projects on github? Are your 
documents usually pdf or csv?

Thank you.
```
---

     
 
all -  [ Using conda environments with Jupyter best practices? ](https://www.reddit.com/r/JupyterLab/comments/1gg9y4b/using_conda_environments_with_jupyter_best/) , 2024-11-02-0912
```
Hi all!

I've been using jupyter on an off for a while, but I need to start using it a lot more regularly, and I need to
 integrate with conda virtual environments. 

Working on a new ubuntu 24.04 install, I installed Anaconda, then created 
a new virtual environment and installed jupyter:

    conda create -n jupyter python=3.12
    conda activate jupyter
   
 pip install jupyterlab
    jupyter lab
    ... 
    

  
So far so good, everything running as expected. So I then crea
te another conda environment for a new project and register it with jupyter via ipykernel. 

    conda create -n rag-lla
ma3.2 python=3.11
    conda activate rag-llama3.2
    python -m ipykernel install --user --name=rag-llama3.2

The ipyker
nel part was completely new to me, I was following a medium post: [https://medium.com/@nrk25693/how-to-add-your-conda-en
vironment-to-your-jupyter-notebook-in-just-4-steps-abeab8b8d084](https://medium.com/@nrk25693/how-to-add-your-conda-envi
ronment-to-your-jupyter-notebook-in-just-4-steps-abeab8b8d084)

So I now have jupyter running in its own conda env, and 
a new env to use for my project. This is where things get very strange. I jump in to the jupyter console, create a new n
otebook, and select the newly registered kernel from the dropdown, all seems fine. I start installing a few packages and
 writing a little code:

    ! pip install langchain-nomic
    ! pip install -qU langchain-ollama
    ! pip list | grep 
langchain
    langchain-core            0.3.14
    langchain-nomic           0.1.3
    langchain-ollama          0.2.0


  
Packages installed, so I begin with an import:

    # LLM using local Ollama
    
    ### LLM
    from langchain_olla
ma import ChatOllama
    
    local_llm = 'llama3.2:3b-instruct-fp16'
    docker_host = 'http://127.0.0.1:11434'
    
  
  llm = ChatOllama(model=local_llm, temperature=0, api_base_url=docker_host)
    llm_json_mode = ChatOllama(model=local_
llm, temperature=0, format='json', api_base_url=docker_host)

Computer says no!

    -----------------------------------
----------------------------------------
    ModuleNotFoundError                       Traceback (most recent call last)

    Cell In[4], line 4
          1 # LLM using local Ollama
          2 
          3 ### LLM
    ----> 4 from langchain
_ollama import ChatOllama
          6 local_llm = 'llama3.2:3b-instruct-fp16'
          7 docker_host = 'http://127.0.0.
1:11434'
    
    ModuleNotFoundError: No module named 'langchain_ollama'-----------------------------------------------
----------------------------
    ModuleNotFoundError                       Traceback (most recent call last)
    Cell In
[4], line 4
          1 # LLM using local Ollama
          2 
          3 ### LLM
    ----> 4 from langchain_ollama impo
rt ChatOllama
          6 local_llm = 'llama3.2:3b-instruct-fp16'
          7 docker_host = 'http://127.0.0.1:11434'
   
 
    ModuleNotFoundError: No module named 'langchain_ollama'

So the modules are installed, but I can't import them. At
 this point I started hunting around and found a few commands to help identify the problem:

    !jupyter kernelspec lis
t --json
    
    {
      'kernelspecs': {
        'python3': {
          'resource_dir': '/home/gjws/anaconda3/envs/jup
yter/share/jupyter/kernels/python3',
          'spec': {
            'argv': [
              'python',
              '-m
',
              'ipykernel_launcher',
              '-f',
              '{connection_file}'
            ],
            
'env': {},
            'display_name': 'Python 3 (ipykernel)',
            'language': 'python',
            'interrupt_
mode': 'signal',
            'metadata': {
              'debugger': true
            }
          }
        },
        '
rag-llama3.2': {
          'resource_dir': '/home/gjws/.local/share/jupyter/kernels/rag-llama3.2',
          'spec': {
 
           'argv': [
              '/home/gjws/anaconda3/envs/rag-llama3.2/bin/python',
              '-Xfrozen_modules=
off',
              '-m',
              'ipykernel_launcher',
              '-f',
              '{connection_file}'
    
        ],
            'env': {},
            'display_name': 'rag-llama3.2',
            'language': 'python',
        
    'interrupt_mode': 'signal',
            'metadata': {
              'debugger': true
            }
          }
     
   }
      }
    }
    /home/gjws/anaconda3/envs/jupyter/bin/python{
      'kernelspecs': {
        'python3': {
       
   'resource_dir': '/home/gjws/anaconda3/envs/jupyter/share/jupyter/kernels/python3',
          'spec': {
            'a
rgv': [
              'python',
              '-m',
              'ipykernel_launcher',
              '-f',
            
  '{connection_file}'
            ],
            'env': {},
            'display_name': 'Python 3 (ipykernel)',
        
    'language': 'python',
            'interrupt_mode': 'signal',
            'metadata': {
              'debugger': tr
ue
            }
          }
        },
        'rag-llama3.2': {
          'resource_dir': '/home/gjws/.local/share/jup
yter/kernels/rag-llama3.2',
          'spec': {
            'argv': [
              '/home/gjws/anaconda3/envs/rag-llama
3.2/bin/python',
              '-Xfrozen_modules=off',
              '-m',
              'ipykernel_launcher',
         
     '-f',
              '{connection_file}'
            ],
            'env': {},
            'display_name': 'rag-llam
a3.2',
            'language': 'python',
            'interrupt_mode': 'signal',
            'metadata': {
             
 'debugger': true
            }
          }
        }
      }
    }
    
    !which -a python
    /home/gjws/anaconda3/e
nvs/jupyter/bin/python

  
So to my untrained eyes, jupyter is seeing both the jupyter conda environment and the rag-lla
ma3.2 environment and getting confused.

Now I don't know where to go. 

Have I done something fundamentally wrong?

Sho
uld I NOT be running jupyter in its own venv and just install it globally?

Have I screwed up the ipykernel steps somewh
ere?

  
Any help would be much appreciated. I've been at this for hours and have hit a brick wall :(

  
Thanks for tak
ing the time to read all this!!!
```
---

     
 
all -  [ Not able to connect to MS SQL Server Database using the tools of Crewai & Langchain. ](https://www.reddit.com/r/crewai/comments/1gg54xa/not_able_to_connect_to_ms_sql_server_database/) , 2024-11-02-0912
```
I've tried using NL2SQL tool of Crewai and even the SQLDatabaseToolkit of Langchain, but nothing worked. All of these an
d the examples on the internet are either on SQLLite, Postgres or using MySQL which someone barely uses in their Product
ion environment. No working example of someone using these tools with MS SQL. I'm able to connect directly using pyodbc 
library, but I want the LLM powered agents to be able to connect and query the DB. Is there a better way of achieveing t
his? Should I create a tool of my own using pyodbc? Has anyone tried connecting their LLM powered agents to their MS SQL
 Database? I'd like to know how you did it?
```
---

     
 
all -  [ Which open-source stack to use for WhatsApp AI customer service? (Concerned about relying solely on  ](https://www.reddit.com/r/LangChain/comments/1gfx4cz/which_opensource_stack_to_use_for_whatsapp_ai/) , 2024-11-02-0912
```
Hey fellow DS folks! 👋

I'm a freelancer based in Brazil getting into AI development. Here's my situation: WhatsApp is H
UGE here for business-customer communication, and I'm getting lots of requests to build AI customer service solutions us
ing GPT/LLMs.

I've studied LangChain and while it's powerful, I'm hesitant to build production systems solely based on 
it. My main concerns are:

1. Many clients want the full power of ChatGPT-like interaction, but I need to ensure the AI 
stays within customer service boundaries
2. Looking for a balance between modern LLM capabilities and traditional custom
er service guardrails (like human oversight when needed)
3. Need something robust enough for production use

**What I'm 
looking for:**

* Battle-tested open-source tools/frameworks for WhatsApp + LLM integration
* Solutions that are widely 
adopted in the industry
* Something that allows proper boundaries/constraints on the AI's scope

Has anyone here impleme
nted something similar? Is there an established stack I should look into? Would really appreciate insights from those wh
o've tackled similar projects!

Edit: For context, I'm specifically looking at building this for small/medium businesses
 that want to automate basic customer support while maintaining quality and control.
```
---

     
 
all -  [ [Student] Current Computer Engineering (ML Focus) Masters Student Applying to AI/ML internships, nee ](https://www.reddit.com/r/EngineeringResumes/comments/1gfu3k7/student_current_computer_engineering_ml_focus/) , 2024-11-02-0912
```
I'm doing my Masters in Computer Engineering with a heavy focus on machine learning, I was able to get an AI/ML internsh
ip this summer, but I am trying to apply more places for 2025 and have been having very bad luck so far (no interviews).


I posted the original resume that I've used for 2025 applications so far in other subreddits and got a lot of feedback
, many said the resume was likely why I wasn't getting any type of interviews and quick rejections. So I decided to just
 let someone on fiver make it instead, because I have no idea what I'm doing and I'm very desperate.

I'm wondering if t
his new resume is decent, because if so, at least now I know if I don't get interviews it's just because I'm not qualifi
ed. If it's not good, any advice on what to change would be very helpful. Because there are still some places left to ap
ply to (not many though).

Also, I'm wondering what I can do to improve my qualifications if they aren't enough for an A
I/ML internship at a larger company (I'm not talking about FAANG, I haven't even bothered with that lol).

https://previ
ew.redd.it/paez60z6wxxd1.png?width=5100&format=png&auto=webp&s=ef2760d98ff8d0d7ebe2055c97404f5eb6942de9

https://preview
.redd.it/s89fsyy6wxxd1.png?width=5100&format=png&auto=webp&s=5303b6d02055d337f12b304e782b357518d3e6f2

  

```
---

     
 
all -  [ Getting Started with LangchainJS: Build a Flexible AI Prompt Service ](https://passarella.dev/p/getting-started-with-langchainjs-build-a-flexible-ai-prompt-service) , 2024-11-02-0912
```
Hey everyone, I wrote an article for those wanting to start with AI and LangchainJS. It's useful for personal projects o
r new generative AI features at your work. In the article I quickly go through some basic Langchain concepts and build a
 reusable and easily extendable class.
```
---

     
 
all -  [ Vectorstore with advanced/versatile filtering ](https://www.reddit.com/r/LangChain/comments/1gfqghi/vectorstore_with_advancedversatile_filtering/) , 2024-11-02-0912
```
Hi all

I am looking for vectorstore options that have versatile filtering capabilities. So far the most complete is qdr
ant but its free cloud offer is a bit more restrictive. I am looking for alternatives.

For example, chroma, pinecone an
d mongodb atlas have similar where operators similar to SQL like equal, not equal, other numerical ones, in array and no
t in array.

I am more interested in operators like 'like' for substring pattern matching.

Any experience?
```
---

     
 
all -  [ RAG web app with local vector DB ](https://www.reddit.com/r/LangChain/comments/1gfolho/rag_web_app_with_local_vector_db/) , 2024-11-02-0912
```
Use case: users of the web app will chat with their localhost vector DB which contains their own private data. 

Questio
n: are there alternatives to have a user interact with their own private data securely?
```
---

     
 
all -  [ Doubt and worry for job security due to high hike switch and domain switch. Please give advice to a  ](https://www.reddit.com/r/developersIndia/comments/1gfn03m/doubt_and_worry_for_job_security_due_to_high_hike/) , 2024-11-02-0912
```
Hello fellow developers, a youngling here with 1+ YOE in a Big4 company where i am not getting much work except some sql
 and vba macro tasks here and there. 
Most of my colleagues who joined here agreed that in this place, our careers are g
etting stagnated at the start itself under promises of security.

Due to financial issues, i have been applying a lot to
 many companies and i finally got shortlisted for the final stage in a US based remote company (50 to 200 employees)
wit
h only about 20 developers in india as per linkedin

The new role is AI NLP ops engineer. They are dealing with AI Agent
s as per their jd. 

I already worked on AI Agents a bit(CrewAI, langchain,etc) during my previous parttime (with some l
ights from the moon) in another US based remote company as part time


I am a bit worried here as once i switch into thi
s role, Will it be too hard to switch back to a normal developer role(MERN, backend, etc)?(note: i always keep myself bu
sy in weekends with some fullstack projects or so to keep myself fluent).


Another issue is the hike. My current CTC is
 approx 8LPA and the one they are offering will be 18 - 22 LPA. If in case i got a layoff, will it be hard to get even a
 job in indian based companies with <2 YOE since they look at previous package a lot here.


I am really worried since d
ue to financial conditions, i really need to get a new job but also cant at all afford to be jobless due to layoffs.




P.S. To GenAI/ML engineers who are experienced, due to my previous internship which dealt in AI agents, i already know a
bout RAG architecture, finetuning, CrewAI and other stuff at an intermediate level. But could you please guide me on wha
t to learn more on this field so that i can keep my job secure?



Thanks a lot in advance for the advices.




TLDR:
1.
 switching to an AI NLP engineer (python, AWS). Can i make it back to a normal SDE role after this?
2. hike from 8LPA to
 18LPA at <2YOE. will this cause issue in finding a new job incase of layoffs?
3. Doubts on Guidance from AI/ML engineer
s



```
---

     
 
all -  [ English Text to Sql to Data ](https://www.reddit.com/r/ChatGPTPro/comments/1gfkudf/english_text_to_sql_to_data/) , 2024-11-02-0912
```
I need to accept as input english text and return data from a DB. I’m trying to understand the distinct advantages of th
e different tools available.

Hearing langchain is a mess, whats the consensus here? What are the different tools availa
ble to add context and knowledge to the prompt?
```
---

     
 
all -  [ What are best in class datasets to conduct Chain of Thought Fine-tuning? ](https://www.reddit.com/r/LangChain/comments/1gfk6tb/what_are_best_in_class_datasets_to_conduct_chain/) , 2024-11-02-0912
```
As the title says, I’d like to do some finetuning tasks with the goal of improving the chain of thought capability. For 
this, what are commonly accepted or best-in-class datasets? 

Thanks for all your comments.
```
---

     
 
all -  [ Where to find example of Llama2 code (no langchain) ](https://www.reddit.com/r/learnmachinelearning/comments/1gfijbe/where_to_find_example_of_llama2_code_no_langchain/) , 2024-11-02-0912
```
Hi all, 

  
I want to learn how to write an LLM class (like LLama 2 using HuggingFace pretrained checkpoints). I don't 
want to use langchain since I want to have free access to all component. 

  
I was searching something like: an initial
ization part, a generate function etc. 

Do you have some autors or github repo of person who write good quality code an
 learn from those?
```
---

     
 
all -  [ How can I enable pagination like support for my SQL agent? ](https://www.reddit.com/r/LangChain/comments/1gfftuy/how_can_i_enable_pagination_like_support_for_my/) , 2024-11-02-0912
```
Hello everyone, I'm working on a Langgraph project i.e. an SQL agent. 

Reference: [https://docs.smith.langchain.com/eva
luation/tutorials/agents](https://docs.smith.langchain.com/evaluation/tutorials/agents) ( core logic is this only with f
ew modifications )

Now, suppose I have a table of 10k users , I ask a question , SQL Agent generates the query and the 
query returns 8k users . 

We know that LLM can't take care of these 8k users in 1 call and will return some users (  fi
rst few ) only. 

I want to have support for something like pagination that we normally have in applications. I hope I'm
 able to explain my problem.

How can I enable pagination for my agent ?
```
---

     
 
all -  [ Customer Support Template Generator: Create Response Templates from Past Tickets 📝 ](https://www.reddit.com/r/ArtificialMoney/comments/1gffgp6/customer_support_template_generator_create/) , 2024-11-02-0912
```
# 💡 The Idea

Let's build an AI system that analyzes your historical support tickets to automatically generate response 
templates. By learning from your team's best responses, we can create a dynamic template library that evolves with your 
support operations, saving time while maintaining consistency and quality.

# 😫 Problem

After speaking with customer su
pport teams, these pain points consistently emerge:

* Support agents spend too much time rewriting similar responses
* 
Knowledge sharing between team members is inefficient
* Template libraries become outdated and require manual maintenanc
e
* New hires struggle to maintain consistent tone and quality
* Teams lack insights into which responses work best

The
 fundamental challenge is scaling quality support without sacrificing personalization or increasing response times.

# ✨
 Solution

We'll build an intelligent system that:

1. Processes Historical Data:

* Analyzes past support conversations

* Identifies common question patterns
* Learns from your best-performing responses

1. Generates Dynamic Templates:

* 
Creates categorized response templates
* Includes variable placeholders for personalization
* Maintains your team's voic
e and style

1. Provides Smart Suggestions:

* Recommends relevant templates in real-time
* Offers personalization sugge
stions
* Tracks template performance

# 🎯 Target Users

Our primary users fall into several categories:

Support Teams:


* Customer Service Representatives
* Technical Support Engineers
* Community Managers
* Support Team Leads

Organizatio
ns:

* SaaS companies
* E-commerce businesses
* Technical support departments
* Customer success teams

# 💰 Monetization


We can implement a tiered pricing strategy:

Free Tier:

* Basic template generation
* Limited historical analysis
* S
tandard categories

Professional Tier:

* Advanced analytics
* Custom categories
* API access
* Team collaboration featu
res

Enterprise Tier:

* Custom model training
* Multi-language support
* Advanced integrations
* Dedicated support

# 🛠
️ Technical Architecture

Core Components:

    Historical Data -> Analysis Engine -> Template Generation -> Template Ma
nagement -> Integration Layer

Key Technologies:

* OpenAI API for template generation and analysis
* LangChain for conv
ersation processing
* Pinecone for semantic search
* PostgreSQL for template storage
* Redis for caching

Infrastructure
:

* Next.js for the web interface
* Docker for containerization
* Vercel for deployment
* Supabase for user management


# 📈 Development Phases

# Phase 1: Core Template Generation

* Historical data analysis
* Basic template creation
* Sim
ple categorization
* Web interface MVP

# Phase 2: Intelligence Layer

* Response effectiveness scoring
* Smart categori
zation
* Personalization suggestions
* Performance analytics

# Phase 3: Integration & Scale

* Help desk integrations
*
 API development
* Multi-language support
* Advanced analytics

# 🚀 MVP Features

Essential Features:

* Ticket analysis
 engine
* Template generation system
* Basic categorization
* Simple search/filter
* Template editor
* Performance track
ing

User Interface:

* Template dashboard
* Category management
* Search functionality
* Basic analytics

# 💡 Technical
 Challenges

Data Processing:

* Handling different ticket formats
* Identifying high-quality responses
* Managing perso
nally identifiable information (PII)
* Maintaining context accuracy

Template Generation:

* Preserving brand voice
* Cr
eating flexible variable systems
* Handling edge cases
* Maintaining template freshness

# 🔒 Security & Compliance

Key 
Considerations:

* Data encryption (at rest and in transit)
* PII detection and redaction
* Access control and audit log
s
* GDPR/CCPA compliance
* Data retention policies

# 🔄 Integration Strategy

Help Desk Platforms:

* Zendesk
* Intercom

* Freshdesk
* Custom API integrations

Communication Channels:

* Email
* Chat
* Social media
* Knowledge base

# 💭 Fut
ure Enhancements

Advanced Features:

* AI-powered response customization
* Sentiment analysis
* Multi-language template
 generation
* Response effectiveness prediction
* A/B testing system
* Automated template updates

# 🎯 Success Metrics


Track These KPIs:

* Response time improvement
* Template usage rates
* Customer satisfaction scores
* Agent productivit
y
* Template effectiveness
* Learning curve reduction

# 💭 Discussion Points

Technical Considerations:

* How do we bal
ance automation with maintaining a human touch?
* What's the best approach for template versioning?
* How can we effecti
vely measure template success?
* What level of customization should we allow?

Share your experiences with similar syste
ms - what worked and what didn't? What challenges did you face in maintaining template quality? 👇
```
---

     
 
deeplearning -  [ Fast AI's deep learning for coders by jeremy howard for begginer?  ](https://www.reddit.com/r/deeplearning/comments/1gb2k3p/fast_ais_deep_learning_for_coders_by_jeremy/) , 2024-11-02-0912
```
I am a full stack python developer who do web dev in django

I am now starting deep learning,i am a compelete begginer


(Have worked with pandas,numpy,matplotlib,langchain only)

I wanna ask,should i do this course,will i understand what he
 is coding and code myslef

I just dont want to do blind coding,i wanna learn what is the purpose,how it works and how t
o do it

Will this course teach me that or not?

Thanks in advance
```
---

     
