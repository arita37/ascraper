 
all -  [ I built an open-source Desktop app to let Claude control your computer ](https://www.reddit.com/r/LangChain/comments/1gdp3h0/i_built_an_opensource_desktop_app_to_let_claude/) , 2024-10-28-0913
```
https://reddit.com/link/1gdp3h0/video/3s10nv8x1exd1/player

 
```
---

     
 
all -  [ How to build a multi-agent app to support structured and unstructured data query? ](https://www.reddit.com/r/LangChain/comments/1gdjd7v/how_to_build_a_multiagent_app_to_support/) , 2024-10-28-0913
```
I am looking to build an app that can query both structured and unstructured data sources - mostly a user question would
 either point to structured or unstrctured data sources and app would need to make a decision where it needs to go.

I e
nvision this as a multi-agent app with an agent for structured data and an agent for unstructured data with a supervisor
 agent for deciding which sub-agent to invoke.

Has anyone experimented or built something like this using LangGraph and
 OpenAI?
```
---

     
 
all -  [ Need help with some PromptEngineering basics on Open WebUI... ](https://www.reddit.com/r/LocalLLM/comments/1gdf7mq/need_help_with_some_promptengineering_basics_on/) , 2024-10-28-0913
```
So I've followed the steps by NetworkChuck in his Youtube [video](https://www.youtube.com/watch?v=Wjrdr0NU4Sk). and now 
I have a local LLM in my computer. But now I'm trying to make my own model based on Ollama3.1:8b, but with a specific sy
stem prompt. So I have a couple of questions:

1. What's the difference between the Model's system prompt, and the RAG T
emplate?
2. Is there a specific framework I should use for system prompts, or is the Co-Star Framework pretty much works
? Does it make a difference if I use hashtags or XML tags?
3. What's the use of the 'Chain of thought' part Or does it n
ot do anything (refer to my system prompt below)? I basically got inspired from [https://openwebui.com/p/varunmahajan/sy
stem-prompt-generator](https://openwebui.com/p/varunmahajan/system-prompt-generator)
4. I'm trying to figure out how to 
tell it NOT to answer anything, unless I give it a document to summarize, or at least, ask the user if they want to give
 a general information.  Can you tell me what I did wrong there?
5. I'm trying to test if my system prompt make sense. W
hat tool can I use other than [LangSmith PlayGround](https://smith.langchain.com/hub/ohkgi/superb_system_instruction_pro
mpt/playground)? (or maybe it doesn't actually make sense? Because there's no Ollama there...

&#8203;

    #####
    # 
CONTEXT #
    You are an AI assistant called Summary Sam designed to extract key information from documents provided by 
users which helps the user summarize the information from the given file(s), and/or explain what the information in the 
documentation.
    #####
    # OBJECTIVE #
    To create an understandable explanation, and answer any information that 
the user asked, based on the given documentation. If no documentation is provided by the user, respond with 'I cannot an
swer you. Please give me a document to summarize first'.
    #####
    # STYLE #
    Blend technical accuracy with appro
achable language, clear and concise, suitable to be read by professional people. Maintain a neutral tone, and do not mak
e any sound that's too much like a sales or marketing pitch.
    #####
    # AUDIENCE #
    Tailor the output towards wo
rking professionals and academics who are seeking to understand a documentation or research paper and are looking for fa
cts and key points.
    #####
    # RESPONSE #
    ## RULES OF ENGAGEMENT WITH USERS ##
    - **STRUCTURE** your prompt 
clearly, with precision, and according to the complexity suitable for the model size.
    - **MAINTAIN CONSISTENCY** in 
by answering in the same language as the user query.
    - If the source is not the same language as the user query, do 
not attempt to translate it, but instead quote the information directly, but form it in an understandable summary, and e
xplain it in the same language as the user query.
    - If the user doesn't give any documentation to summarize, then ap
ologize, before answering with 'I cannot answer you. Please give me a document to summarize first'
    - If the user doe
sn't give any documentation to summarize, don't give information about general knowledge, before the user gives back the
ir answer, that they want you to give it a general knowledge answer, with the timestamp where you had achieved the gener
al knowledge answer.
    - If the answer is not clear, ask the user for clarification to ensure accurate response.
    #
# CHAIN OF THOUGHTS ##
    1. Clearly enumerate your explanation, on why you give such summary
    2. Always give out re
ferences on where you had summarized the information, complete with page number, as well as line number when possible.
 
   #####
```
---

     
 
all -  [ Best Approach to Building a Chatbot with Twitter Data Using LLMs (LLaMA 3.2)? ](https://www.reddit.com/r/developersIndia/comments/1gdf4jj/best_approach_to_building_a_chatbot_with_twitter/) , 2024-10-28-0913
```
**Hello everyone,**

I'm currently working on analyzing customer support inquiries from various insurance companies (twi
tter handles) and generating questions from these tweets using LLaMA 3.2. The dataset includes both full conversation an
d tweet-level formats, containing customer support inquiries.

Now, I'm looking to take it a step further and build a ch
atbot that can:

1. Answer customer queries based on the patterns found in the historical tweets. (Currently doing manua
lly)
2. Utilize the questions I've already generated.
3. Learn from ongoing interactions with users to improve its respo
nses over time.

Given the data I have and my experience working with LLMs, what would be the best way to approach build
ing this chatbot? Here are a few specifics I'm curious about:

* What framework or tools (open-source or otherwise) woul
d work well for this kind of chatbot development?
* How can I integrate LLaMA 3.2 (or another model, if recommended) to 
handle real-time question generation and answering?
* How should I structure the chatbot's learning process to continuou
sly improve its responses from new tweets or user interactions?

Any suggestions on architecture, training strategies,RA
Gs or frameworks (like Rasa, Langchain, etc.) would be greatly appreciated. Thank you!
```
---

     
 
all -  [ I created a Claude Computer Use alternative to use with OpenAI and Gemini, using Langchain and open- ](https://i.redd.it/5rtd09dycbxd1.jpeg) , 2024-10-28-0913
```

github: https://github.com/Clevrr-AI/Clevrr-Computer

The day Anthropic announced Computer Use, I knew this was gonna b
low up, but at the same time, it was not a model-specific capability but rather a flow that was enabling it to do so. 


I it got me thinking whether the same (at least upto a level) can be done, with a model-agnostic approach, so I don’t ha
ve to rely on Anthropic to do it. 

I got to building it, and in one day of idk-how-many coffees and some prototyping, I
 built Clevrr Computer - an AI Agent that can control your computer using text inputs. 

The tool is built using Langcha
in’s ReAct agent and a custom screen intelligence tool, here’s how it works. 

- The user asks for a task to be complete
d, that task is broken down into a chain-of-actions by the primary agent. 
- Before performing any task, the agent calls
 the `get_screen_info` tool for understanding what’s on the screen. 
- This tool is basically a multimodal llm call that
 first takes a screenshot of the current screen, draws gridlines around it for precise coordinate tracking, and sends th
e image to the llm along with the question by the master agent. 
- The response from the tool is taken by the master age
nt to perform computer tasks like moving the mouse, clicking, typing, etc using the `PyAutoGUI` library.

And that’s how
 the whole computer is controlled. 

**Please note that this is a very nascent repository right now, and I have not enab
led measures to first create a sandbox environment to isolate the system, so running malicious command will destroy your
 computer, however I have tried to restrict such usage in the prompt**

Please give it a try and I would love some quali
ty contributions to the repository!
```
---

     
 
all -  [ Paper to podcast using LangChain ](https://www.reddit.com/r/generativeAI/comments/1gdco7f/paper_to_podcast_using_langchain/) , 2024-10-28-0913
```
I have built this small open-source app using LangChain and Openai API and I want you guys to give me feedback about it.

It basically takes a research paper and turns it into an engaging podcast between 3 persons:
- host: present the paper 
and directs the discussion.
- learner: asks interesting questions about the paper.
- researcher: have a lot of knowledge
, comments and explaind complex concepts.
This is perfect for people who like podcasts and enjoy listening to papers whi
le traveling.
You need an OpenAI Key to make it work, and it costs ~0.19$ for a ~16 pages paper.
Feel free to roast me, 
I really need to improve 💪
Link: https://github.com/Azzedde/paper_to_podcast/tree/main
```
---

     
 
all -  [ I created a Claude Computer Use alternative to use with OpenAI and Gemini, using Langchain and open- ](https://i.redd.it/76cf8mknk5xd1.jpeg) , 2024-10-28-0913
```

```
---

     
 
all -  [ How to get Django back rnd internship/job in so much saturation? ](https://i.redd.it/xu1vtquzpaxd1.jpeg) , 2024-10-28-0913
```
I have been trying to get a job/internship but no luck

In my city,there are barely any companies/software houses meanwh
ile the recent chatgpt shit blew up this field
There were total 3500 students that took admission in my uni in computer 
field

And there would be barely like 100 or something software houses

How do i get noticed? Its not like i got selecte
d for the interview
I am not even being called for internviews despite being 
Well skilled and a good student

Attaching
 an image of skills so you guys can see i atleast got enough to get an interview
```
---

     
 
all -  [ EmailSnap - Empower Your Email Routine with LLM Agents ](https://www.reddit.com/r/u_ilbets/comments/1gd2nnb/emailsnap_empower_your_email_routine_with_llm/) , 2024-10-28-0913
```
Nowadays, almost every service revolves around communication, whether it’s plumbers, receptionists at clinics, or clerks
 in banks. Every day, countless people read emails, review attached scanned documents, and PDFs; and sort, organize, and
 forward them elsewhere. Imagine how much time we could save if we automated this process! With the advancements in Gene
rative AI and Large Language Models (LLMs), it’s no longer just a dream — it’s possible now.

https://preview.redd.it/i0
dduokz28xd1.jpg?width=1792&format=pjpg&auto=webp&s=592ef68deb152ee99d4d3736b3219bf4e5aee935

# Problem ✨ Solution

You r
eceive an email with a long thread of messages and attached files — many of them with random names. *What do you really 
want?* To quickly understand what the email is about and know what actions to take.

That’s where EmailSnap comes in. Si
mply forward the email to [**review@emailsnap.app**](mailto:review@emailsnap.app), and [**EmailSnap**](https://emailsnap
.app/) will apply AI to analyze the email and its attachments, then send you back a new, actionable, and well-formatted 
response.

The processed email contains:

* **Title:** \[Priority\] Subject
* **From:** Sender of the email
* **To:** Re
cipient
* **Highlights:** Key action items in bullet points
* **Summary:** A concise review of the email content and att
ached files
* **Attachments:** Renamed to reflect their actual content

# [EmailSnap.app](http://EmailSnap.app) 📩

The i
mplementation consists mainly of two parts: the underlying infrastructure and the LLM flow. Let’s start with the more in
teresting part.

# AI Review ✨

For the LLM implementation, we use the LangChain stack: **LangChain**, and **LangSmith**
. Despite not using LangGraph itself, I apply the same graph-like idea for executing EmailSnap’s LLM processing, as it r
equires multiple LLM calls with different prompts while using various tools, like saving intermediate states to a databa
se and S3.

Our execution graph contains the following nodes:

* **Format Email:** Reads the EML file and converts it in
to well-formatted text, handling threads and forwarded messages while removing redundant HTML tags and other irrelevant 
information.
* **Read Attachments:** If the attached file is an image or PDF, we convert it to Base64 for the LLM to rea
d the content. For PDFs, each page is converted into a new image, potentially creating a long loop.
* **Review Attachmen
t:** This node creates a summary with highlights and action items from each document, suggests the recipient, and propos
es a better file name.
* **Email Summary:** The final node combines the formatted email and the summaries from all attac
hments to generate a complete email with insights, action items, highlights, and an overall summary.

After the final co
ntent is generated, we will send out a new email back to the sender including reorganized attachments.

https://preview.
redd.it/13kb3pl338xd1.jpg?width=580&format=pjpg&auto=webp&s=715202d38b4149ab29879e45fa05329ac79a46d4

# Sample

Finally,
 let’s take a look at a real example. I took an MRI report in PDF format from an online source, sent it to one email add
ress, and then forwarded it to [**review@emailsnap.app**](mailto:review@emailsnap.app). EmailSnap generated a new subjec
t, highlights, and summary. It also extracted the recipient from the PDF — **Dr. Ross Banner** — and finally suggested a
 new file name: **Regina Doe MRI Report**, based on the patient’s name and procedure.

https://preview.redd.it/znbrr37a3
8xd1.jpg?width=2694&format=pjpg&auto=webp&s=b14dc7a43c8d757861f0abce7f93dc78ef6a638d

# Interested?

Interested in the i
dea? ping me at [help@emailsnap.app](mailto:help@emailsnap.app) 
```
---

     
 
all -  [ agentic ASI ](https://www.reddit.com/r/LangChain/comments/1gcuxgs/agentic_asi/) , 2024-10-28-0913
```
I realized that superintelligence is already appearing today in a modular form. And what if the modules could be LangGra
ph agents? 

For example calculator: superintelligent in its narrow field of making calculations. Also easily implementa
ble to LangGraph as a tool. It can help the main LLM with calculations. 

What if this approach can be scaled? Can we im
plement other modules, that would create a superintelligence (or at least something similarly intelligent) together? 

I
 saw an interview with Demis Hassabis, where he spoke about implementing some 'tools' directly into Gemini and letting o
thers be called by Gemini. This resonated with me, because calling tools is very solved today. The first part about impl
ementing directly into the model is different as only few companies can do this. 

But could be stick with the tool call
ing (or communication between agents) only to create a superintelligence? How could we intertwine the thinking of the mo
dules/agents? 

Could we share some ideas about this please? 
```
---

     
 
all -  [ Open Source NotebookLM Podcast API seeking Contributors ](https://www.reddit.com/r/OpenSourceAI/comments/1gcqdcg/open_source_notebooklm_podcast_api_seeking/) , 2024-10-28-0913
```
I love NotebookLM 'Deep Dives' audio generation; it's really a new UI/UX for LLMs. However, I wished there were an API s
o I could automated things instead of being tied to Google's UI.

So I built an open source Python package for it:

[htt
ps://github.com/souzatharsis/podcastfy](https://github.com/souzatharsis/podcastfy)

It uses langchain for LLM management
, llamafile to enable running llms locally and it integrates with several text-to-speech models.  It is multimodal, mult
ilingual and fully customizable.

The project already reached thousands of downloads and it's in a point that would bene
fit from additional contributors! If you are excited about this kind of problem, we would love your help!
```
---

     
 
all -  [ Need Guidance on whether to sit and study from scratch or just wing it.  ](https://www.reddit.com/r/developersIndia/comments/1gcm2y9/need_guidance_on_whether_to_sit_and_study_from/) , 2024-10-28-0913
```
Context :  
0. I graduated from NIT in Mechanical Engineering. But I always had an idea that I would want my career in S
oftware industry. I have no DSA knowledge nor practice. So only training I had was after college in Java & SQL.

1. I am
 working in the software industry from the past 4 years. Currently I am working as an langchain developer from the past 
six months.
2. My background : 3 Years in one service based company. Majorly worked on an internal tool and on the side 
learnt java stack. Got hands on properly for 1 year. Then resigned and joined another company as the stack in my previou
s company was legacy and I wanted hands on learning in latest java stack.
3. Gave and cleared a lot of interviews(Servic
e Based) by just studying the most asked interview questions and practice questions and got hired.
4. So after joining a
nother company, I was excited and was provided with amazing opportunities with great work. But soon I could see that I a
m not able to catch up. And I could also understand that since my base and hands on is not a lot, I could not take compl
ex stories and work at the speed that was expected at my experience.
5. So after working for 6 months, I was assigned a 
fresh project using Langchain. Since it is GenAI, I accepted and now I am comfortable in it. But I want my core strong s
kill to be the java stack.

My main question is :

As this stage in my life, should I invest time to study everything fr
om scractch and spend maybe 4-6 months to build a strong base or just wing it by getting more and more practice by just 
building YT projects and then just that the java coding becomes a habit rather than deep understanding. I feel like I wi
ll get by for another few years just by winging it but that makes me cautious and take a step back and sit and learn eve
rything from scratch. I am super confused.

PS : I am also married since the past 1 year and that is also a facet in my 
life.

I am just hoping for some guidance from the folks here.
```
---

     
 
all -  [ How do I get this menu in Safari? ](https://www.reddit.com/r/VisionPro/comments/1gcibho/how_do_i_get_this_menu_in_safari/) , 2024-10-28-0913
```
https://preview.redd.it/w1e9yf21y2xd1.png?width=1920&format=png&auto=webp&s=8d5881da24543947c7c6809b3c0b1e8dede90fdd

  

I've randomly got this menu in Safari but I'm not sure how I did. I didn't even know that this type of a menu exists in
 Safari. Does anyone know how to get that menu? Thanks! 
```
---

     
 
all -  [ AI SQL Agent not working or hallucinating like mad ](https://www.reddit.com/r/n8n/comments/1gchmi4/ai_sql_agent_not_working_or_hallucinating_like_mad/) , 2024-10-28-0913
```
Trying to use this workflow for [sql ai agent](https://n8n.io/workflows/2292-talk-to-your-sqlite-database-with-a-langcha
in-ai-agent/) but it’s not working.  
Tried with Ollama and Gemini, both do not work.

Error:  
Could not parse LLM outp
ut: Based on the provided information, here is a rewritten version of the query with improvements: `sql SELECT DISTINCT 
Title FROM albums WHERE ArtistId = 1;` Changes made: \* Added `DISTINCT` to remove duplicate titles from the result set.
 \* Removed the `LIMIT 10` clause, as it’s not necessary in this case. If you need to limit the number of results for so
me reason, consider adding it with a comment explaining its purpose. This query is more efficient and concise than the o
riginal version, and it achieves the same goal: retrieving unique titles from the “albums” table where the ArtistId is 1
. However, without knowing the exact data types of ArtistId and Title, or having access to the actual database schema an
d sample rows, it’s difficult to provide a more tailored solution. But, using PostgreSQL’s syntax, you can also use doub
le quotes for quoting table names: `sql SELECT DISTINCT ''Title'' FROM 'albums' WHERE ArtistId = 1;` Or, if you want to 
avoid the double quotes altogether: `sql SELECT DISTINCT Title FROM albums WHERE ArtistId = 1;` In this case, PostgreSQL
 will interpret `Albums` as a table name automatically. If you want to use subqueries or JOINs for more complex queries,
 I can provide examples and explanations for those cases as well. Just let me know!

https://preview.redd.it/s0au808bp2x
d1.png?width=690&format=png&auto=webp&s=056a4b098a422c24c2e42407c8055cdcdea2c054

I then tried with Gemini model, and it
’s just straight up making things up:

https://preview.redd.it/p6juk9ccp2xd1.png?width=690&format=png&auto=webp&s=023570
ab301727bea1d06bd93edf61460bddd609

[Real db data](https://preview.redd.it/fuhum7afp2xd1.png?width=1324&format=png&auto=
webp&s=877b0d08b1545d5f61f0e82471efe0886dbae47a)


```
---

     
 
all -  [ (Very skilled) 3D artist seeking advice for career change to cybersecurity. (Study program advice). ](https://www.reddit.com/r/ITCareerQuestions/comments/1gcg6d9/very_skilled_3d_artist_seeking_advice_for_career/) , 2024-10-28-0913
```
I qualify for a 14 month program fully paid by the government. I'd like to know your 
thoughts about this program, given
 the length of the duration. I’m a 3D artist with spectacular skills, but I feel AI is taking over careers to do with ar
t.


Certificates:

Google IT Support Professional Certificate
Google Cybersecurity Professional Certificate
CompTIA Sec
urity+
CompTIA Network+
CompTIA A+
IHK Berlin - Operative Professionals

Concepts covered:

Python Fundamentals: Learn t
he basics of programming, including syntax,
data types, and simple operations.

Algorithmic Thinking: Develop problem-so
lving and logic-building skills
using algorithms.

Looping: Learn how to create repetition in your code using for loops.


Intro to HTML + CSS: The basic building blocks of web pages.

Strings and Lists: Learn about two sequential data types
 in Python.

Functions: Creating reusable code blocks and understanding how
functions work.


Technologies:

Python
HTML

CSS
Git
Command Line Interface


AI for Cybersecurity, technologies and frameworks:

OWASP Top 10 for
LLM Applications

Large Language
Models (LLMs)
Perplexity
MITRE ATLAS
OpenRouter
ChatGPT, Claude, Gemini
LangChain
Microsoft Copilot for S
ecurity
Prompt engineering
Gradio and Streamlit


Concepts covered:

Foundations of AI in Cybersecurity: Introduction to
 AI and ML in cybersecurity,
LLM fundamentals, MITRE ATLAS, OWASP Top 10 for LLM Applications, ENISA
AI Resources, NIST 
AI Risk Management Framework, and ethical considerations.

Threat Detection and Management: AI for anomaly detection and
 pattern
recognition, AI-powered intrusion detection systems.

Security Operations: AI-driven SIEM and log analysis, aut
omated incident
response using AI, and AI for threat hunting and intelligence.

Risk Assessment and Compliance: AI for s
ecurity compliance automation, risk
assessment and analysis using machine learning, and AI in policy enforcement
and mon
itoring.

Advanced Prompt Engineering for IT Security: Prompt engineering
fundamentals, LLM settings optimization, zero-
shot and few-shot prompting
techniques, meta prompting and prompt chaining strategies, Tree of Thoughts
methodology, and
 security-specific prompt examples.

AI for User Support and Problem-Solving: Implementing AI for IT support,
AI-driven 
troubleshooting and diagnostics, and automated problem resolution
using machine learning.

AI Tools and Platforms for Cy
bersecurity: Microsoft Copilot for Security,
Perplexity.ai for research and analysis, capabilities and use cases of Clau
de,
ChatGPT, and Gemini, and custom GPT creation for specialized security tasks.

Data Analysis and Insights: Anomaly de
tection in large datasets and predictive
analytics for threat forecasting.

AI Application Development for Cybersecurity
: Python programming for AI
security applications, LangChain Functions, Tools, and Agents), Gradio and
Streamlit for bui
lding AI security dashboards, and semantic search
implementation.

Advanced LLM Techniques: RAG Retrieval-Augmented Gene
ration), prompt
caching, embeddings, fine-tuning, and function calling in LLMs.

Security Automation: Developing AI-powe
red security scripts, command line
AI completions for security tasks, and automating vulnerability management
with AI.



If you’ve read this far, I thank you for your time and I'd appreciate any advice/suggestion.
```
---

     
 
all -  [ How to scrape URLs faster with WebbaseLoader/SeleniumURLLoader? ](https://www.reddit.com/r/LangChain/comments/1gcfd6g/how_to_scrape_urls_faster_with/) , 2024-10-28-0913
```
I have designed a multi agents RAG using Langgraph, based on query it diverts question to RAG or Web search, using Googl
e Serper, I'm getting the metadata and extracting links from there and those links (for example 5 links) I'm passing to 
SeleniumURLLoader(urls).load after that I'm storing the scraped content into vectorstore and retrieving relevant content
 based on query

But this process takes 1-2 minutes, I debug each step, and found that most of the time is going on in s
craping the websites, embeddings are being created within 1-2s

How can I speed up the process?

async functions will he
lp? Or parallel processing of each link to a different agent (creating 5 different agents and each of them handling 1 li
nk simultaneously)

(I'm aware of the approach, instead of scraping the website, use metadata from Google Serper, but it
 doesn't have detailed snippets that I'm looking for, so scraping is the only option I have)

(Also I can't use paid cra
wlers, if any of you have better scraper/crawler which is free, kindly suggest those)
```
---

     
 
all -  [ A Simple Implementation of Automatic Prompt Generation using DSPy ](https://www.reddit.com/r/LangChain/comments/1gc3oo2/a_simple_implementation_of_automatic_prompt/) , 2024-10-28-0913
```
A simplified implementation of 'automatic prompt generation' using the techniques used in DSPy's MIPROv2 optimizer. This
 program uses the gsm8k dataset consisting of math problems and is made up of 3 modules: This program is made up of 3 mo
dules:

1. Module 1 generates demos for the prompt
2. Module 2 generates an instruction for the prompt
3. Module 3 uses 
the outputs of module 1 & 2 to generate the final prompt.

**Module 1**

This module takes a labeled training data set a
nd generates 2 (`NUM_SETS`) sets of 10 demos each:

* 5 demos are directly sampled from the dataset
* 5 demos are genera
ted using the model and satisfies the metric i.e. generated output = expected output

https://preview.redd.it/fqda7rjwmy
wd1.png?width=1462&format=png&auto=webp&s=c2f86e2e7aaf03f6b40a0a6808dc4197f3d8d475

**Module 2**

This module takes the 
2 sets of 10 demos generated in Step 1 along with a string representation of the application code i.e. the code of this 
program and generates 2(`NUM_INSTRUCTIONS`) different instructions by

* Identifying the class of problems using the dem
os
* Identifying the intent of user using the program semantics

https://preview.redd.it/b846jbrymywd1.png?width=1390&fo
rmat=png&auto=webp&s=f919bad00b2a91eb953798e40ef896a21374c54b

**Module 3**

In this final step, it takes the outputs fr
om the previous steps as inputs and generates two different final prompts (since we have 2 sets of 10 demos from step 1 
and 2 instructions from step 2).

https://preview.redd.it/unyb65l0nywd1.png?width=1490&format=png&auto=webp&s=2d6bc6122a
15141ec51646f6affec47ecfa777c5

**Conclusion**

That's how you can generate prompt candidates using DSPy. Note that we s
tarted purely with a bunch of labeled datasets and nothing else. If you are curious to dive deep and understand more abo
ut this prompt optimization technique, check out the research paper [here](https://arxiv.org/pdf/2406.11695). If you wou
ld like to start using this optimizer, check out the dspy docs [here](https://dspy-docs.vercel.app/deep-dive/optimizers/
miprov2/).

**Source Code**

You can find the full source code for this example - https://github.com/Scale3-Labs/dspy-ex
amples/tree/main/src/simple_miprov2

# Additional Notes

1. Each one of the 3 modules are built using the ChainOfThought
 optimizer and Signature hints to guide the program to do what we want to do.
2. I am building an open source observabil
ity tool called Langtrace which you can use to understand what goes in and out of the LLM and trace every step within ea
ch module deeply.
3. The final prompts can be further optimized using a metric and you can technically generate 4 prompt
s with 2 demos and 2 instructions (2 x 2 permutation). These are left out for the sake of simplicity.
4. Since module 2 
uses the program code to identify the intent, re-structuring your code or adding comments can affect the outputs.
```
---

     
 
all -  [ Getting messages from within a tool in LangGraph ](https://www.reddit.com/r/LangChain/comments/1gc06vn/getting_messages_from_within_a_tool_in_langgraph/) , 2024-10-28-0913
```
Hello,

I have a graph with subggraphs, in one subgraph I call the tools inside of a node. Inside the tool itself I'm ta
king input from the user after I print to him what to enter and I also invoke the LLM. 

1. What's the usual way of prom
pting the user for input? I'm a bit confused here. Let's say in production, does the print statement get shown to the us
er? As far as I know it's the list of messages.

2. How can I access the state from within a tool in order to update the
 list of messages? I'm not using a ToolNode.

The first question might seem stupid, but I really don't know. I've been s
tuck for a while thinking through these. No clear thoughts yet. 

Thanks!
```
---

     
 
all -  [ Community/Network around AI Agents ](https://www.reddit.com/r/LangChain/comments/1gbz805/communitynetwork_around_ai_agents/) , 2024-10-28-0913
```
We just launched our community focused on AI Agents! Here it is: [https://discord.gg/qEfQVwg2](https://discord.gg/qEfQVw
g2)

We're going to have

* Constantly Updated News
* Learning Resources
* Hackathons and Investment Resources (getting 
your ideas funded)
* AI Agent Marketplace (Trading post for AI Agent buyers and sellers)
* Ongoing agent experiments tha
t the community can get involved in
* and much more as we grow

Me and my partner truly believe that AI will soon enable
 people to start enterprise level businesses on their own. Imagine you want to build a one-person software company run a
lmost entirely by agents. We're not there yet but we're getting closer, and we want to build platforms to make it insane
ly easy to build and manage these projects using AI Agents.

If you're excited for AI Agents and what they will help us 
create, consider joining!
```
---

     
 
all -  [ Agent runs on loop, sometimes time out, sometimes giving incorrect answer, sometimes proper answer. ](https://www.reddit.com/r/LangChain/comments/1gbz54x/agent_runs_on_loop_sometimes_time_out_sometimes/) , 2024-10-28-0913
```
Trying to build one text to sql project. I'm using ollama llama3.2 locally. But my model is slow and it keep on running 
sometimes without giving the result. Sometimes it generates query but not able to extract the query result. Could someon
e help me with this? Thanks in advance!! 

    from langchain_community.llms import Ollama
    from db import get_schema
, db
    from langchain_community.agent_toolkits import create_sql_agent
    from langchain_community.agent_toolkits.sql
.toolkit import SQLDatabaseToolkit
    from langchain_ollama import OllamaLLM
    from langchain.agents import AgentType

    from langchain_community.tools.sql_database.tool import QuerySQLDataBaseTool, InfoSQLDatabaseTool, ListSQLDatabaseT
ool, QuerySQLCheckerTool
    from langchain_community.embeddings import OllamaEmbeddings
    from langchain_community.ve
ctorstores import FAISS
    from langchain_core.example_selectors import SemanticSimilarityExampleSelector
    from lang
chain_core.prompts import FewShotPromptTemplate, PromptTemplate, ChatPromptTemplate
    from langchain_core.prompts impo
rt SystemMessagePromptTemplate
    from langchain.agents import AgentExecutor, create_react_agent
    
    
    llm = Ol
lamaLLM(model='llama3.2')
    toolkit = SQLDatabaseToolkit(db=db, llm=llm)
    
    embeddings = (
        OllamaEmbeddi
ngs(model = 'llama3.2')
    )
    
    examples = [
        {   'input': 'List all actors.', 
            'query': 'SELE
CT * FROM Actor;'
        },
        {
            'input': 'Find all movies of Ed Chase',
            'query': 'SELECT 
film.title, concat(actor.first_name, ' ', actor.last_name) as actorname from film LEFT JOIN filmactor on film.film_id=fi
lmactor.film_id LEFT JOIN actor on actor.actor_id=filmactor.actor_id WHERE concat(actor.first_name, ' ', actor.last_name
) LIKE '%Ed Chase%''
        },
        {
            'input': 'Find all customers for the postal code 35200.',
        
    'query': 'SELECT first_name,last_name,address_id FROM customer WHERE address_id = (SELECT address_id FROM address WH
ERE postal_code = '35200');',
        },
        {
            'input': 'Find full address of Mary Smith.',
            
'query': 'SELECT address, address2, district, postal_code from address where address_id = (select address_id from custom
er where concat(first_name,' ', last_name) LIKE '%Mary Smith%');',
        },
        {
            'input': 'How many c
ustomers are there',
            'query': 'SELECT COUNT(*) FROM customer',
        },
        {
            'input': 'Fi
nd the total number of actors.',
            'query': 'SELECT COUNT(DISTINT(actor_id)) FROM Actor;',
        },
        
{
            'input': 'Who are the top 5 customers by total purchase?',
            'query': 'SELECT customer.customer_
id AS customer_id, concat(customer.first_name, ' ', customer.last_name) as customer_name, SUM(payment.amount) AS TotalPu
rchase FROM payment LEFT JOIN customer on customer.customer_id=payment.customer_id GROUP BY customer.customer_id ORDER B
Y TotalPurchase DESC LIMIT 5;',
        },
    ]
    
    example_selector = SemanticSimilarityExampleSelector.from_exam
ples(
        examples,
        embeddings,
        FAISS,
        k=3,
        input_keys=['input'],
    )
    
    sql
_db_query =  QuerySQLDataBaseTool(db = db)
    sql_db_schema =  InfoSQLDatabaseTool(db = db)
    sql_db_list_tables =  L
istSQLDatabaseTool(db = db)
    sql_db_query_checker = QuerySQLCheckerTool(db = db, llm = llm)
    
    
    tools = [sq
l_db_query, sql_db_schema, sql_db_list_tables, sql_db_query_checker]
    
    # matched_queries = example_selector.vecto
rstore.search('How many actors are there?', search_type = 'mmr')
    
    
    # for tool in tools:
    #     print(tool
.name + ' - ' + tool.description.strip() + '\n')
    
    system_prefix = '''
    Answer the following questions as best
 you can. You have access to the following tools:
    
    {tools}
    
    Use the following format:
    
    Question:
 the input question you must answer
    Thought: you should always think about what to do
    Action: the action to take
, should be one of [{tool_names}]
    Action Input: the input to the action 
    Observation:
    the result of the acti
on 
    ... (this Thought/Action/Action Input/Observation can repeat N times)
    Thought: I now know the final answer
 
   Final Answer: the final answer to the original input question 
    
    Here are some examples of user inputs and the
ir corresponding SQL queries:
    '''
    
    suffix = '''
    Begin!
    
    Question: {input} 
    Thought:{agent_sc
ratchpad}
    '''
    
    dynamic_few_shot_prompt_template = FewShotPromptTemplate(
        example_selector = example_
selector,
        example_prompt=PromptTemplate.from_template(
            'User input: {input}\nSQL query: {query}'
   
     ),
        input_variables=['input'],
        prefix=system_prefix,
        suffix=suffix
    )
    
    
    full_
prompt = ChatPromptTemplate.from_messages(
        [
            SystemMessagePromptTemplate(prompt=dynamic_few_shot_pro
mpt_template),
        ]
    )
    
    # prompt_val = full_prompt.invoke(
    #     {
    #         'input': 'How many 
actors are there?',
    #         'tool_names' : [tool.name for tool in tools],
    #         'tools' : [tool.name + ' -
 ' + tool.description.strip() for tool in tools],
    #         'agent_scratchpad': [],
    #     }
    # )
    # print(
prompt_val.to_string())
    
    
    agent = create_react_agent(llm, tools, full_prompt)
    agent_executor = AgentExec
utor(agent=agent, tools=tools, verbose=True, handle_parsing_errors=True)
    des = agent_executor.invoke({'input': 'How 
many actors are there?'})
    
    
    print(des)

Terminal: **Runs on loop and not extracting output \[In this case '2
00' is the answer\], sometimes not even correct answer.**

    Entering new AgentExecutor chain...
    
    Action: sql_
db_query
    Action Input: SELECT COUNT(DISTINCT actor_id) FROM Actor;[(200,)]Question: How many actors are there? 
    
Thought: Action: sql_db_query
    Action Input: SELECT COUNT(DISTINCT actor_id) FROM Actor[(200,)]Question: How many act
ors are there? 
    Thought: I need to execute a query that counts the number of distinct actor IDs.
    Action: sql_db_
query
    Action Input: SELECT COUNT(DISTINCT actor_id) FROM Actor[(200,)]Question: How many actors are there?
    Thoug
ht: I need to count the number of distinct actor IDs.
    Action: sql_db_query
    Action Input: SELECT COUNT(DISTINCT a
ctor_id) FROM Actor[(200,)]Question: How many actors are there? 
    Thought: I want to execute a SQL query that counts 
the number of distinct actor IDs.
    Action: sql_db_query
    Action Input: SELECT COUNT(DISTINCT actor_id) FROM Actor[
(200,)]Question: How many actors are there? 
    Thought: I should use the sql_db_query tool to execute a SQL query that
 counts the number of distinct actor IDs.
    Action: sql_db_query
    Action Input: SELECT COUNT(DISTINCT actor_id) FRO
M Actor[(200,)]Question: How many actors are there? 
    Thought: I need to use the sql_db_query tool to execute a SQL q
uery that counts the number of distinct actor IDs.
    Action: sql_db_query
    Action Input: SELECT COUNT(DISTINCT acto
r_id) FROM Actor[(200,)]Question: How many actors are there? 
    Thought: I need to count the number of distinct actor 
IDs.
    Action: sql_db_query
    Action Input: SELECT COUNT(DISTINCT actor_id) FROM Actor[(200,)]Question: How many act
ors are there?
    Thought: Execute a SQL query that counts the number of distinct actor IDs.
    Action: sql_db_query
 
   Action Input: SELECT COUNT(DISTINCT actor_id) FROM Actor[(200,)]Question: How many actors are there? 
    Thought: I 
want to execute a SQL query that counts the number of distinct actor IDs.
    Action: sql_db_query
    Action Input: SEL
ECT COUNT(DISTINCT actor_id) FROM Actor[(200,)]Question: How many actors are there?
    Thought: I need to use the sql_d
b_query tool to execute a SQL query that counts the number of distinct actor IDs.
    Action: sql_db_query
    Action In
put: SELECT COUNT(DISTINCT actor_id) FROM Actor[(200,)]Question: How many actors are there? 
    Thought: I need to use 
the sql_db_query tool to execute a SQL query that counts the number of distinct actor IDs.
    Action: sql_db_query
    
Action Input: SELECT COUNT(DISTINCT actor_id) FROM Actor[(200,)]Question: How many actors are there? 
    Thought: Execu
te a SQL query to count the number of distinct actor IDs.
    Action: sql_db_query
    Action Input: SELECT COUNT(DISTIN
CT actor_id) FROM Actor[(200,)]Question: How many actors are there? 
    Thought: I need to use the sql_db_query tool to
 execute a SQL query that counts the number of distinct actor IDs.
    Action: sql_db_query
    Action Input: SELECT COU
NT(DISTINCT actor_id) FROM Actor[(200,)]Question: How many actors are there? 
    Thought: I should use the sql_db_query
 tool to execute a SQL query that counts the number of distinct actor IDs.
    Action: sql_db_query
    Action Input: SE
LECT COUNT(DISTINCT actor_id) FROM Actor[(200,)] 
    
    
    {'input': 'How many actors are there?', 'output': 'Agent
 stopped due to iteration limit or time limit.'} 
```
---

     
 
all -  [ CopilotKit: Build Agent-Native Applications with CoAgents & LangGraph ](https://www.reddit.com/r/LangChain/comments/1gbxilp/copilotkit_build_agentnative_applications_with/) , 2024-10-28-0913
```
We are excited to release CoAgents + LangGraph - your new open-source tool for embedding powerful AI agents in your in-a
pp chatbot! With CoAgents, you can:

* Shared State (Agent `↔` Application) with support for intermediate state streamin
g
* Agentic Generative UI
* Human-in-the-Loop
* Realtime frontend actions
* Agent Steering (LangGraph checkpoints)

Reso
urces:

* Check it out here: [CopilotKit on GitHub](https://go.copilotkit.ai/copilot)
* And dive into our walkthrough fo
r a full guide: [Everything You Need to Build Agent-Native Applications](https://go.copilotkit.ai/coagent-blog)

Webinar
:

* Build Agent-Native Applications with CoAgents & LangGraph(Oct. 28th): [Register Here](https://lu.ma/2kxspzl4)
```
---

     
 
all -  [ Title: Urgent Help Needed with PDF Table Extraction in Langchain Project

 ](https://www.reddit.com/r/LangChain/comments/1gbx399/title_urgent_help_needed_with_pdf_table/) , 2024-10-28-0913
```
I'm currently working on a project utilizing Langchain for a large language model (LLM) RAG retriever. Despite having mi
llions of PDF files stored in Supabase, I'm achieving over 90% efficiency with structured data extraction. However, I'm 
facing a significant challenge with my PDFs, as they often contain complex multi-dimensional tables.

I've experimented 
with various parsers and libraries, including Camelot, OpenParser, Tabula, PDFMiner, PyMuPDF, and many others. Unfortuna
tely, none have effectively resolved the issues I'm encountering. The extracted data lacks a coherent structure, making 
it difficult to connect the dots between different pieces of information.

The complexity of the layouts in my PDFs is s
uch that even advanced and paid solutions (like AskYourPDF, OpenAI's 4.0, and Petal) seem to rely on similar underlying 
parsers, leading to the same parsing errors.

I would greatly appreciate any suggestions or insights on how to tackle th
is problem. Thank you!
```
---

     
 
all -  [ RAG-Enhanced Chatbot Application | AI-Powered Document Retrieval & Chatbot Demo | LangChain & OpenAI ](https://www.reddit.com/r/django/comments/1gbtw0l/ragenhanced_chatbot_application_aipowered/) , 2024-10-28-0913
```
I’m excited to share my latest project, an AI-driven chatbot built with LangChain, OpenAI’s GPT-4, ChromaDB, and Streaml
it. By leveraging Retrieval-Augmented Generation (RAG) this application delivers data-backed, contextually rich response
s, perfect for high-impact customer support and knowledge-based applications.

📽️ Watch the Demo - [https://youtu.be/MZD
iMMai6zo?si=xN6hJ-Zj0S627Sj0](https://youtu.be/MZDiMMai6zo?si=xN6hJ-Zj0S627Sj0)  
💻 Explore the Project - [https://githu
b.com/abdurrahimcs50/RAG\_Chatbot\_Project.git](https://github.com/abdurrahimcs50/RAG_Chatbot_Project.git)

🟢 Key Featur
es:

✅ Real-Time Chat Interface: Chat with AI models like OpenAI’s GPT-4 in a responsive interface.  
✅ Document Uploads
 for RAG: Improve chatbot responses by uploading your own documents (PDF, TXT, DOCX, MD).  
✅ URL-Based RAG: Integrate r
eal-time web content into your chat interactions for up-to-date responses.   
✅ Model Selection: Switch easily between O
penAI models, including GPT-4, to suit your needs.  
✅ Interaction Logging: Automatically logs chats for tracking insigh
ts and refining user experiences.

💼 Perfect For: Customer support, research assistants, and knowledge-based application
s that require reliable, accurate responses. This demo shows how the chatbot processes user inputs, retrieves document a
nd web data, and combines it with AI capabilities to deliver comprehensive answers.  
🟢 Tech Stack:

✅ LangChain  
✅ Ope
nAI (GPT-4)  
✅ Streamlit  
✅ ChromaDB  
✅ Docker

If you’re looking to bring AI-powered solutions to your business, fee
l free to connect! I’m a Freelance Python Developer & Generative AI Specialist ready to take on projects that demand cut
ting-edge AI solutions with Django, Docker, LangChain, OpenAI, and more.
```
---

     
 
all -  [ RAG expertise  ](https://www.reddit.com/r/LangChain/comments/1gbt7ql/rag_expertise/) , 2024-10-28-0913
```
We are building a RAG solution to summarize and query medical records on a large scale.  End product very similar to dig
italowl.com.

Looking for subject matter experts with demonstrated experience for paid, short term contract help to test
 and help finish the product.   Please message privately with CV and availability if interested.
```
---

     
 
all -  [ Udemy Free Courses for 25 October 2024 ](https://www.reddit.com/r/udemyfreeebies/comments/1gbs5oj/udemy_free_courses_for_25_october_2024/) , 2024-10-28-0913
```
# Udemy Free Courses for 25 October 2024

Note : Coupons might expire anytime, so enroll as soon as possible to get the 
courses for FREE.

* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20900/)Free Tutorial – Spring Boot LDAP Integrati
on: Secure Authentication & Manage
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20899/)Free Spring Boot Tutorial 
– Master Spring Boot: Build, Test, and Optimize Applications
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20898/)
Free Azure DevOps Tutorial – Azure DevOps Essentials: Learn in Hindi
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy
/20897/)Free Blogging Tutorial – Build WordPress Blogging Website + Blogging with ChatGPT
* [REDEEM OFFER ](https://idow
nloadcoupon.com/udemy/20896/)Free Tutorial – Pengembangan Solusi Aplikasi Berbasis Mobile
* [REDEEM OFFER ](https://idow
nloadcoupon.com/udemy/20895/)Free Chatbot Tutorial – Build No-code AI Chatbot: Transform Your Customer Engagement
* [RED
EEM OFFER ](https://idownloadcoupon.com/udemy/20894/)Free Tutorial – Attracting Aligned Clients
* [REDEEM OFFER ](https:
//idownloadcoupon.com/udemy/20893/)Free InVideo Tutorial – InVideo Video Creation with ChatGPT (Free Course)
* [REDEEM O
FFER ](https://idownloadcoupon.com/udemy/20892/)Free Digital Marketing Tutorial – State of AI for Growth: Separate the S
ignal from the Noise
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20891/)Free Sales Skills Tutorial – Negociação 
Persuasiva: Supere Objeções e Feche mais Vendas
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20890/)Free Sales Ma
nagement Tutorial – O Poder da IA nas Vendas: Da Prospecção ao Fechamento
* [REDEEM OFFER ](https://idownloadcoupon.com/
udemy/20889/)Free Business Consulting Tutorial – Mastering Professional Services – Consulting 101
* [REDEEM OFFER ](http
s://idownloadcoupon.com/udemy/20888/)Free Shopify Tutorial – How To Use Sellerboard For Shopify – Full Tutorial & Review

* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20887/)Free Marketing Strategy Tutorial – Marketing Digital: Estude
, entenda e escolha um caminho.
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20886/)Free Web Design Tutorial – Ур
оки веб-дизайна для начинающих | Бесплатные занятия
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20885/)Free Care
er Development Tutorial – Build a Career You Love
* Free Self-Awareness Tutorial – Developing Self-Awareness: A Journey 
to Personal Growth
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/20884/)
* [REDEEM OFFER ](https://idownloadcoupon.
com/udemy/20883/)Free Tutorial – İnsan Kaynakları Planlaması, Mülakat ve Seçme Süreçleri
* [REDEEM OFFER ](https://idown
loadcoupon.com/udemy/20882/)Free Tutorial – Watchdog 101: Factchecking in Sri Lanka
* [REDEEM OFFER ](https://idownloadc
oupon.com/udemy/20881/)Free Parenting Tutorial – Clarity and Presence as an Entrepreneur Parent
* [REDEEM OFFER ](https:
//idownloadcoupon.com/udemy/20880/)Free Web Development Tutorial – Программирование для начинающих | Верстка сайта сайта
 с нуля
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20879/)Free ChatGPT Tutorial – Utiliser ChatGPT sur Windows 
10 et 11 efficacement.
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20878/)Free Apache Flink Tutorial – Apache Fl
ink Training For Beginners
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20877/)ChatGPT for Product Management & I
nnovation
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20876/)CDMP Data Quality Practice Questions Practitioner/M
aster
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20875/)Clojure Introduction: Learn Functional Programming
* [R
EDEEM OFFER ](https://idownloadcoupon.com/udemy/20874/)Procurement Manager Professional Certification
* [REDEEM OFFER ](
https://idownloadcoupon.com/udemy/20873/)Contact Center Manager Professional Certification
* [REDEEM OFFER ](https://ido
wnloadcoupon.com/udemy/20872/)Chief Customer Experience Officer Executive Certification
* [REDEEM OFFER ](https://idownl
oadcoupon.com/udemy/20871/)Chief Business Development Officer Executive Certification
* [REDEEM OFFER ](https://idownloa
dcoupon.com/udemy/20870/)Agile Professional Certification
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20869/)Man
agement Executive Certification
* Debugging Javascript / NodeJS
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/20868
/)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20867/)Marketing Professional Certification
* [REDEEM OFFER ](htt
ps://idownloadcoupon.com/udemy/20866/)Python Complete Course And Flask Framework, HTML Essentials
* [REDEEM OFFER ](http
s://idownloadcoupon.com/udemy/20865/)Sales Focus B2B Selling Skills Programme
* [REDEEM OFFER ](https://idownloadcoupon.
com/udemy/20864/)CompTIA Linux+ XK0-005: Ace Your 2024 Exam with 500+ Qs each
* [REDEEM OFFER ](https://idownloadcoupon.
com/udemy/20863/)Charging Stations for Electric Vehicles
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20862/)Free
lancing Professional Certification
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20861/)Adobe Premiere Pro Advance
d Video Editing Course
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20860/)Computer Networks Fundamentals
* [REDE
EM OFFER ](https://idownloadcoupon.com/udemy/20859/)Microsoft Excel- Conditional Formatting
* [REDEEM OFFER ](https://id
ownloadcoupon.com/udemy/20858/)Board Member Executive Certification (BMEC)
* [REDEEM OFFER ](https://idownloadcoupon.com
/udemy/20857/)CSS And Javascript Crash Course
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20856/)Resume Mastery:
 Crafting Your Career Success
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20855/)The Interview Maestro: Perfecti
ng the Art for Success
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20854/)Creative Speaking Mastery: Unlocking Y
our Speechcraft Pote
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20853/)Branding & Brand Marketing Professional 
Certification (BMPC)
* The Ultimate Resume Writing Guide: Crafting a Winning Prof
* [REDEEM OFFER](https://idownloadcoup
on.com/udemy/20852/)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20851/)Crafting a Winning Job Application: The 
Essentials
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20850/)Web Application Fundamentals: Building Your Founda
tion Part2
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20849/)Web Application Fundamentals: Building Your Founda
tion Part1
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20848/)The Art of Communication: A Path to Success
* [RED
EEM OFFER ](https://idownloadcoupon.com/udemy/20847/)Java Training Complete Course for Java Beginners All in One
* [REDE
EM OFFER ](https://idownloadcoupon.com/udemy/20846/)Exam 2V0-11.24 : VMware Cloud Foundation 5.2 Administrator
* [REDEEM
 OFFER ](https://idownloadcoupon.com/udemy/20845/)SAFe®: General Overview course
* [REDEEM OFFER ](https://idownloadcoup
on.com/udemy/20844/)PHP Laravel: Build Amazing Streaming Service
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/208
43/)Comprehensive WordPress MCQs: From Basic to Advanced
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20842/)Micr
osoft Office Mastery Learn Word Excel and PowerPoint
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20841/)AZ-900: 
Microsoft Azure Fundamentals Practice Exam
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20840/)ChatGPT Prompt Eng
ineering Guide: Make Money Using ChatGPT
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20839/)Easy Ways to Make Mo
ney Online with ChatGPT for Beginners
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20838/)70-671: Microsoft Share
Point Configuring Practice Test 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20837/)Agile Coach Certificatio
n
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20836/)Complete MS Office Course Masterclass: Beginner to Advanced

* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20835/)Canva Masterclass: Social Media, T-Shirt, Video Edit, Motion

* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20834/)Master Filmora: Editing, Motion Graphics, and Color Grading

* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20833/)UI/UX Design Masterclass with Adobe XD: From Beginner to Pro

* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20832/)T-Shirt Design for Beginner to Advanced with Adobe Photoshop

* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20831/)Corporate Governance Professional Certification (CGPC)
* [RED
EEM OFFER ](https://idownloadcoupon.com/udemy/20830/)Executive Assistant Professional Certification (EAPC)
* [REDEEM OFF
ER ](https://idownloadcoupon.com/udemy/20829/)Transformers in Computer Vision – English version
* [REDEEM OFFER ](https:
//idownloadcoupon.com/udemy/20828/)Generative AI: Learn about the next AI frontier
* [REDEEM OFFER ](https://idownloadco
upon.com/udemy/20827/)Generative AI (English Version): Unleashing Next-Gen AI
* [REDEEM OFFER ](https://idownloadcoupon.
com/udemy/20826/)Reinforcement Learning (English): Master the Art of RL
* [REDEEM OFFER ](https://idownloadcoupon.com/ud
emy/20825/)Deep Learning for Computer Vision
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20824/)Deep Learning fo
r Natural Language Processing
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20823/)Deployment of Machine Learning 
Models
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20822/)Transformers in Computer Vision
* [REDEEM OFFER ](http
s://idownloadcoupon.com/udemy/20821/)Reinforcement Learning
* Open-source LLMs: Uncensored & secure AI locally with RAG

* [REDEEM OFFER](https://idownloadcoupon.com/udemy/20820/)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20819/)AI
-Agents: Automation & Business with LangChain & LLM Apps
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20818/)How 
to Become an Embedded Systems Engineer Bootcamp
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20817/)Herramientas 
de Google 2024, ¡Desde Cero Hasta Experto!
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20816/)Coaching program –
 Become the Woman of Your Life!
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20815/)Practice Exams | AWS Certifie
d Solutions Architect Associate
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20814/)Staff Engineer Survival Manua
l: AI Era Technical Leadership
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20813/)Curso de microservicios con Sp
ring Boot y Spring Cloud
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20812/)Curso Completo de Kubernetes Desde C
ero para Programadores
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20811/)Tiktok Ads marketing Crash Course For 
Beginners (Hindi/Urdu)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20810/)Google Ads And Tiktok Ads Crash Course
 (Hindi/ Urdu)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20809/)Tiktok Marketing & Shopify Ecommerce store (hi
ndi/urdu)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20808/)Facebook Marketing + Whatsapp Ads (CASE STUDY) Hind
i 2023
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20807/)Digital Marketing Business With Google My Business
* [
REDEEM OFFER ](https://idownloadcoupon.com/udemy/20806/)Google Ads Mastery\~ Beginner To Pro \~ HINDI/URDU 2023
* [REDEE
M OFFER ](https://idownloadcoupon.com/udemy/20805/)Facebook Ads Marketing Funnel For Ecommerce Hindi

GET MORE FREE ONLI
NE COURSES WITH CERTIFICATE – [CLICK HERE](https://idownloadcoupon.com/)
```
---

     
 
all -  [ Udemy Free Courses for 25 October 2024 ](https://www.reddit.com/r/udemyfreebies/comments/1gbs5kx/udemy_free_courses_for_25_october_2024/) , 2024-10-28-0913
```
# Udemy Free Courses for 25 October 2024

Note : Coupons might expire anytime, so enroll as soon as possible to get the 
courses for FREE.

* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20900/)Free Tutorial – Spring Boot LDAP Integrati
on: Secure Authentication & Manage
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20899/)Free Spring Boot Tutorial 
– Master Spring Boot: Build, Test, and Optimize Applications
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20898/)
Free Azure DevOps Tutorial – Azure DevOps Essentials: Learn in Hindi
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy
/20897/)Free Blogging Tutorial – Build WordPress Blogging Website + Blogging with ChatGPT
* [REDEEM OFFER ](https://idow
nloadcoupon.com/udemy/20896/)Free Tutorial – Pengembangan Solusi Aplikasi Berbasis Mobile
* [REDEEM OFFER ](https://idow
nloadcoupon.com/udemy/20895/)Free Chatbot Tutorial – Build No-code AI Chatbot: Transform Your Customer Engagement
* [RED
EEM OFFER ](https://idownloadcoupon.com/udemy/20894/)Free Tutorial – Attracting Aligned Clients
* [REDEEM OFFER ](https:
//idownloadcoupon.com/udemy/20893/)Free InVideo Tutorial – InVideo Video Creation with ChatGPT (Free Course)
* [REDEEM O
FFER ](https://idownloadcoupon.com/udemy/20892/)Free Digital Marketing Tutorial – State of AI for Growth: Separate the S
ignal from the Noise
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20891/)Free Sales Skills Tutorial – Negociação 
Persuasiva: Supere Objeções e Feche mais Vendas
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20890/)Free Sales Ma
nagement Tutorial – O Poder da IA nas Vendas: Da Prospecção ao Fechamento
* [REDEEM OFFER ](https://idownloadcoupon.com/
udemy/20889/)Free Business Consulting Tutorial – Mastering Professional Services – Consulting 101
* [REDEEM OFFER ](http
s://idownloadcoupon.com/udemy/20888/)Free Shopify Tutorial – How To Use Sellerboard For Shopify – Full Tutorial & Review

* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20887/)Free Marketing Strategy Tutorial – Marketing Digital: Estude
, entenda e escolha um caminho.
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20886/)Free Web Design Tutorial – Ур
оки веб-дизайна для начинающих | Бесплатные занятия
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20885/)Free Care
er Development Tutorial – Build a Career You Love
* Free Self-Awareness Tutorial – Developing Self-Awareness: A Journey 
to Personal Growth
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/20884/)
* [REDEEM OFFER ](https://idownloadcoupon.
com/udemy/20883/)Free Tutorial – İnsan Kaynakları Planlaması, Mülakat ve Seçme Süreçleri
* [REDEEM OFFER ](https://idown
loadcoupon.com/udemy/20882/)Free Tutorial – Watchdog 101: Factchecking in Sri Lanka
* [REDEEM OFFER ](https://idownloadc
oupon.com/udemy/20881/)Free Parenting Tutorial – Clarity and Presence as an Entrepreneur Parent
* [REDEEM OFFER ](https:
//idownloadcoupon.com/udemy/20880/)Free Web Development Tutorial – Программирование для начинающих | Верстка сайта сайта
 с нуля
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20879/)Free ChatGPT Tutorial – Utiliser ChatGPT sur Windows 
10 et 11 efficacement.
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20878/)Free Apache Flink Tutorial – Apache Fl
ink Training For Beginners
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20877/)ChatGPT for Product Management & I
nnovation
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20876/)CDMP Data Quality Practice Questions Practitioner/M
aster
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20875/)Clojure Introduction: Learn Functional Programming
* [R
EDEEM OFFER ](https://idownloadcoupon.com/udemy/20874/)Procurement Manager Professional Certification
* [REDEEM OFFER ](
https://idownloadcoupon.com/udemy/20873/)Contact Center Manager Professional Certification
* [REDEEM OFFER ](https://ido
wnloadcoupon.com/udemy/20872/)Chief Customer Experience Officer Executive Certification
* [REDEEM OFFER ](https://idownl
oadcoupon.com/udemy/20871/)Chief Business Development Officer Executive Certification
* [REDEEM OFFER ](https://idownloa
dcoupon.com/udemy/20870/)Agile Professional Certification
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20869/)Man
agement Executive Certification
* Debugging Javascript / NodeJS
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/20868
/)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20867/)Marketing Professional Certification
* [REDEEM OFFER ](htt
ps://idownloadcoupon.com/udemy/20866/)Python Complete Course And Flask Framework, HTML Essentials
* [REDEEM OFFER ](http
s://idownloadcoupon.com/udemy/20865/)Sales Focus B2B Selling Skills Programme
* [REDEEM OFFER ](https://idownloadcoupon.
com/udemy/20864/)CompTIA Linux+ XK0-005: Ace Your 2024 Exam with 500+ Qs each
* [REDEEM OFFER ](https://idownloadcoupon.
com/udemy/20863/)Charging Stations for Electric Vehicles
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20862/)Free
lancing Professional Certification
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20861/)Adobe Premiere Pro Advance
d Video Editing Course
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20860/)Computer Networks Fundamentals
* [REDE
EM OFFER ](https://idownloadcoupon.com/udemy/20859/)Microsoft Excel- Conditional Formatting
* [REDEEM OFFER ](https://id
ownloadcoupon.com/udemy/20858/)Board Member Executive Certification (BMEC)
* [REDEEM OFFER ](https://idownloadcoupon.com
/udemy/20857/)CSS And Javascript Crash Course
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20856/)Resume Mastery:
 Crafting Your Career Success
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20855/)The Interview Maestro: Perfecti
ng the Art for Success
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20854/)Creative Speaking Mastery: Unlocking Y
our Speechcraft Pote
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20853/)Branding & Brand Marketing Professional 
Certification (BMPC)
* The Ultimate Resume Writing Guide: Crafting a Winning Prof
* [REDEEM OFFER](https://idownloadcoup
on.com/udemy/20852/)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20851/)Crafting a Winning Job Application: The 
Essentials
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20850/)Web Application Fundamentals: Building Your Founda
tion Part2
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20849/)Web Application Fundamentals: Building Your Founda
tion Part1
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20848/)The Art of Communication: A Path to Success
* [RED
EEM OFFER ](https://idownloadcoupon.com/udemy/20847/)Java Training Complete Course for Java Beginners All in One
* [REDE
EM OFFER ](https://idownloadcoupon.com/udemy/20846/)Exam 2V0-11.24 : VMware Cloud Foundation 5.2 Administrator
* [REDEEM
 OFFER ](https://idownloadcoupon.com/udemy/20845/)SAFe®: General Overview course
* [REDEEM OFFER ](https://idownloadcoup
on.com/udemy/20844/)PHP Laravel: Build Amazing Streaming Service
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/208
43/)Comprehensive WordPress MCQs: From Basic to Advanced
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20842/)Micr
osoft Office Mastery Learn Word Excel and PowerPoint
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20841/)AZ-900: 
Microsoft Azure Fundamentals Practice Exam
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20840/)ChatGPT Prompt Eng
ineering Guide: Make Money Using ChatGPT
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20839/)Easy Ways to Make Mo
ney Online with ChatGPT for Beginners
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20838/)70-671: Microsoft Share
Point Configuring Practice Test 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20837/)Agile Coach Certificatio
n
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20836/)Complete MS Office Course Masterclass: Beginner to Advanced

* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20835/)Canva Masterclass: Social Media, T-Shirt, Video Edit, Motion

* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20834/)Master Filmora: Editing, Motion Graphics, and Color Grading

* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20833/)UI/UX Design Masterclass with Adobe XD: From Beginner to Pro

* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20832/)T-Shirt Design for Beginner to Advanced with Adobe Photoshop

* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20831/)Corporate Governance Professional Certification (CGPC)
* [RED
EEM OFFER ](https://idownloadcoupon.com/udemy/20830/)Executive Assistant Professional Certification (EAPC)
* [REDEEM OFF
ER ](https://idownloadcoupon.com/udemy/20829/)Transformers in Computer Vision – English version
* [REDEEM OFFER ](https:
//idownloadcoupon.com/udemy/20828/)Generative AI: Learn about the next AI frontier
* [REDEEM OFFER ](https://idownloadco
upon.com/udemy/20827/)Generative AI (English Version): Unleashing Next-Gen AI
* [REDEEM OFFER ](https://idownloadcoupon.
com/udemy/20826/)Reinforcement Learning (English): Master the Art of RL
* [REDEEM OFFER ](https://idownloadcoupon.com/ud
emy/20825/)Deep Learning for Computer Vision
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20824/)Deep Learning fo
r Natural Language Processing
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20823/)Deployment of Machine Learning 
Models
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20822/)Transformers in Computer Vision
* [REDEEM OFFER ](http
s://idownloadcoupon.com/udemy/20821/)Reinforcement Learning
* Open-source LLMs: Uncensored & secure AI locally with RAG

* [REDEEM OFFER](https://idownloadcoupon.com/udemy/20820/)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20819/)AI
-Agents: Automation & Business with LangChain & LLM Apps
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20818/)How 
to Become an Embedded Systems Engineer Bootcamp
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20817/)Herramientas 
de Google 2024, ¡Desde Cero Hasta Experto!
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20816/)Coaching program –
 Become the Woman of Your Life!
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20815/)Practice Exams | AWS Certifie
d Solutions Architect Associate
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20814/)Staff Engineer Survival Manua
l: AI Era Technical Leadership
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20813/)Curso de microservicios con Sp
ring Boot y Spring Cloud
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20812/)Curso Completo de Kubernetes Desde C
ero para Programadores
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20811/)Tiktok Ads marketing Crash Course For 
Beginners (Hindi/Urdu)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20810/)Google Ads And Tiktok Ads Crash Course
 (Hindi/ Urdu)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20809/)Tiktok Marketing & Shopify Ecommerce store (hi
ndi/urdu)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20808/)Facebook Marketing + Whatsapp Ads (CASE STUDY) Hind
i 2023
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20807/)Digital Marketing Business With Google My Business
* [
REDEEM OFFER ](https://idownloadcoupon.com/udemy/20806/)Google Ads Mastery\~ Beginner To Pro \~ HINDI/URDU 2023
* [REDEE
M OFFER ](https://idownloadcoupon.com/udemy/20805/)Facebook Ads Marketing Funnel For Ecommerce Hindi

GET MORE FREE ONLI
NE COURSES WITH CERTIFICATE – [CLICK HERE](https://www.reddit.com/r/udemyfreeebies/)
```
---

     
 
all -  [ Le marché de l’IA pour les junior est infernal…  ](https://i.redd.it/m3e6ue0dqvwd1.jpeg) , 2024-10-28-0913
```
La startup dans laquelle je bosse actuellement n’a pas validé ma période d’essai. 
D’après eu, j’ai fait un travail rema
rquable et ai fortement impacté leur produit, mais c’est trop de travail de former un Junior et ils sont dans une vision
 de “senioriser” leurs équipes.
```
---

     
 
all -  [ Question: Moving from LLMChain with memory to LCEL chain ](https://www.reddit.com/r/LangChain/comments/1gbpxv3/question_moving_from_llmchain_with_memory_to_lcel/) , 2024-10-28-0913
```
Hi all,  
I need some help with migrating from LLMChain to LCEL chain. I have a memory object being created where 'histo
ry' returns messages from database and being passed to ConversationBufferWindowMemory. 

    memory = ConversationBuffer
WindowMemory(
            memory_key='chat_history', chat_memory=history, k=6
        )  

I am creating LLMChain as abo
ve. I need some help around how I can lift and shift 'memory' to LCEL Chain. Read some articles but could not get my hea
d around it. Thanks!

    qa = LLMChain(llm=llm, prompt=qa_prompt, memory=memory)
```
---

     
 
all -  [ 3D artist career change (seeking advise regarding a program) ](https://www.reddit.com/r/Cybersecurity101/comments/1gbp1yl/3d_artist_career_change_seeking_advise_regarding/) , 2024-10-28-0913
```
I qualify for a 14 month program fully paid by the government. I'd like to know your 
thoughts about this program, given
 the length of the duration. I’d love to hear what you think about changing careers; I’m a 3D artist with spectacular sk
ills, but I feel AI is taking over careers to do with art.


Certificates:

Google IT Support Professional Certificate
G
oogle Cybersecurity Professional Certificate
CompTIA Security+
CompTIA Network+
CompTIA A+
IHK Berlin - Operative Profes
sionals

Concepts covered:

Python Fundamentals: Learn the basics of programming, including syntax,
data types, and simp
le operations.

Algorithmic Thinking: Develop problem-solving and logic-building skills
using algorithms.

Looping: Lear
n how to create repetition in your code using for loops.

Intro to HTML + CSS: The basic building blocks of web pages.


Strings and Lists: Learn about two sequential data types in Python.

Functions: Creating reusable code blocks and unders
tanding how
functions work.


Technologies:

Python
HTML
CSS
Git
Command Line Interface


AI for Cybersecurity, technolo
gies and frameworks:

OWASP Top 10 for
LLM Applications
Large Language
Models (LLMs)
Perplexity
MITRE ATLAS
OpenRouter
C
hatGPT, Claude, Gemini
LangChain
Microsoft Copilot for Security
Prompt engineering
Gradio and Streamlit


Concepts cover
ed:

Foundations of AI in Cybersecurity: Introduction to AI and ML in cybersecurity,
LLM fundamentals, MITRE ATLAS, OWAS
P Top 10 for LLM Applications, ENISA
AI Resources, NIST AI Risk Management Framework, and ethical considerations.

Threa
t Detection and Management: AI for anomaly detection and pattern
recognition, AI-powered intrusion detection systems.

S
ecurity Operations: AI-driven SIEM and log analysis, automated incident
response using AI, and AI for threat hunting and
 intelligence.

Risk Assessment and Compliance: AI for security compliance automation, risk
assessment and analysis usin
g machine learning, and AI in policy enforcement
and monitoring.

Advanced Prompt Engineering for IT Security: Prompt en
gineering
fundamentals, LLM settings optimization, zero-shot and few-shot prompting
techniques, meta prompting and promp
t chaining strategies, Tree of Thoughts
methodology, and security-specific prompt examples.

AI for User Support and Pro
blem-Solving: Implementing AI for IT support,
AI-driven troubleshooting and diagnostics, and automated problem resolutio
n
using machine learning.

AI Tools and Platforms for Cybersecurity: Microsoft Copilot for Security,
Perplexity.ai for r
esearch and analysis, capabilities and use cases of Claude,
ChatGPT, and Gemini, and custom GPT creation for specialized
 security tasks.

Data Analysis and Insights: Anomaly detection in large datasets and predictive
analytics for threat fo
recasting.

AI Application Development for Cybersecurity: Python programming for AI
security applications, LangChain Fun
ctions, Tools, and Agents), Gradio and
Streamlit for building AI security dashboards, and semantic search
implementation
.

Advanced LLM Techniques: RAG Retrieval-Augmented Generation), prompt
caching, embeddings, fine-tuning, and function c
alling in LLMs.

Security Automation: Developing AI-powered security scripts, command line
AI completions for security t
asks, and automating vulnerability management
with AI.


If you’ve read this far, I thank you for your time and I'd appr
eciate any advice/suggestion.
```
---

     
 
all -  [ 3D Artist career change (asking for opinions on this program) ](https://www.reddit.com/r/cybersecurity/comments/1gbp144/3d_artist_career_change_asking_for_opinions_on/) , 2024-10-28-0913
```
Edit: Fellas, kindly don't downvote my post. I'm not in a good situation for the time being, I'm trying to evaluate my c
areer options by seeking your opinions and I would really appreciate all the info I can gather.

___________


I qualify
 for a 14 month program fully paid by the government. I'd like to know your 
thoughts about this program, given the leng
th of the duration. I’m a 3D artist with spectacular skills, but I feel AI is taking over careers to do with art.


Cert
ificates:

Google IT Support Professional Certificate
Google Cybersecurity Professional Certificate
CompTIA Security+
Co
mpTIA Network+
CompTIA A+
IHK Berlin - Operative Professionals

Concepts covered:

Python Fundamentals: Learn the basics
 of programming, including syntax,
data types, and simple operations.

Algorithmic Thinking: Develop problem-solving and
 logic-building skills
using algorithms.

Looping: Learn how to create repetition in your code using for loops.

Intro t
o HTML + CSS: The basic building blocks of web pages.

Strings and Lists: Learn about two sequential data types in Pytho
n.

Functions: Creating reusable code blocks and understanding how
functions work.


Technologies:

Python
HTML
CSS
Git

Command Line Interface


AI for Cybersecurity, technologies and frameworks:

OWASP Top 10 for
LLM Applications
Large Lan
guage
Models (LLMs)
Perplexity
MITRE ATLAS
OpenRouter
ChatGPT, Claude, Gemini
LangChain
Microsoft Copilot for Security
P
rompt engineering
Gradio and Streamlit


Concepts covered:

Foundations of AI in Cybersecurity: Introduction to AI and M
L in cybersecurity,
LLM fundamentals, MITRE ATLAS, OWASP Top 10 for LLM Applications, ENISA
AI Resources, NIST AI Risk M
anagement Framework, and ethical considerations.

Threat Detection and Management: AI for anomaly detection and pattern

recognition, AI-powered intrusion detection systems.

Security Operations: AI-driven SIEM and log analysis, automated in
cident
response using AI, and AI for threat hunting and intelligence.

Risk Assessment and Compliance: AI for security c
ompliance automation, risk
assessment and analysis using machine learning, and AI in policy enforcement
and monitoring.


Advanced Prompt Engineering for IT Security: Prompt engineering
fundamentals, LLM settings optimization, zero-shot and 
few-shot prompting
techniques, meta prompting and prompt chaining strategies, Tree of Thoughts
methodology, and security
-specific prompt examples.

AI for User Support and Problem-Solving: Implementing AI for IT support,
AI-driven troublesh
ooting and diagnostics, and automated problem resolution
using machine learning.

AI Tools and Platforms for Cybersecuri
ty: Microsoft Copilot for Security,
Perplexity.ai for research and analysis, capabilities and use cases of Claude,
ChatG
PT, and Gemini, and custom GPT creation for specialized security tasks.

Data Analysis and Insights: Anomaly detection i
n large datasets and predictive
analytics for threat forecasting.

AI Application Development for Cybersecurity: Python 
programming for AI
security applications, LangChain Functions, Tools, and Agents), Gradio and
Streamlit for building AI 
security dashboards, and semantic search
implementation.

Advanced LLM Techniques: RAG Retrieval-Augmented Generation), 
prompt
caching, embeddings, fine-tuning, and function calling in LLMs.

Security Automation: Developing AI-powered secur
ity scripts, command line
AI completions for security tasks, and automating vulnerability management
with AI.


If you’v
e read this far, I thank you for your time and I'd appreciate any advice/suggestion.
```
---

     
 
all -  [ Orchestration agent in ChatGPT ](https://www.reddit.com/r/LangChain/comments/1gbnk79/orchestration_agent_in_chatgpt/) , 2024-10-28-0913
```
Hi,

I am working on building an orchestrator in ChatGPT.I have few agents in GPT environment. Now I want just to prompt
 the orchestrator and it will invoke the relevant agent based on keywords.I have designed structured prompt and it is ro
uting it but relevant agent is not responding.  
If someone can give input.
```
---

     
 
all -  [ Question: How to Create a More Flexible Tool Creation Workflow in LangChain? ](https://www.reddit.com/r/LangChain/comments/1gbnalq/question_how_to_create_a_more_flexible_tool/) , 2024-10-28-0913
```
I'm currently working on an agentic workflow using LangChain and have found that hard-coding tools can be limiting. I’m 
curious if there’s a way to make the tools more flexible, allowing them to be dynamically created or accessed in real-ti
me during the workflow. Would it be possible to integrate a system where agents can not only execute predefined tools bu
t also create or adapt new tools as needed on the spot? Has anyone experimented with this kind of dynamic tool generatio
n within LangChain, and if so, how did you approach it?
```
---

     
 
all -  [ Need your opinions on this program (3D product visualizer changing careers to cybersecurity) ](https://www.reddit.com/r/CyberSecurityAdvice/comments/1gbm2dy/need_your_opinions_on_this_program_3d_product/) , 2024-10-28-0913
```
I qualify for a 14 month program fully paid by the government. I'd like to know your 
thoughts about this program, give
n the length of the duration. I’d love to hear what you think about changing careers; I’m a 3D artist with spectacular s
kills, but I feel AI is taking over careers to do with art.


Certificates:

Google IT Support Professional Certifi
cate
Google Cybersecurity Professional Certificate
CompTIA Security+
CompTIA Network+
CompTIA A+
IHK Berlin - Opera
tive Professionals

Concepts covered:

Python Fundamentals: Learn the basics of programming, including syntax,
data
 types, and simple operations.

Algorithmic Thinking: Develop problem-solving and logic-building skills
using algorit
hms.

Looping: Learn how to create repetition in your code using for loops.

Intro to HTML + CSS: The basic building
 blocks of web pages.

Strings and Lists: Learn about two sequential data types in Python.

Functions: Creating reus
able code blocks and understanding how
functions work.


Technologies:

Python
HTML
CSS
Git
Command Line Inter
face


AI for Cybersecurity, technologies and frameworks:

OWASP Top 10 for
LLM Applications
Large Language
Mode
ls (LLMs)
Perplexity
MITRE ATLAS
OpenRouter
ChatGPT, Claude, Gemini
LangChain
Microsoft Copilot for Security
Prom
pt engineering
Gradio and Streamlit


Concepts covered:

Foundations of AI in Cybersecurity: Introduction to AI an
d ML in cybersecurity,
LLM fundamentals, MITRE ATLAS, OWASP Top 10 for LLM Applications, ENISA
AI Resources, NIST AI R
isk Management Framework, and ethical considerations.

Threat Detection and Management: AI for anomaly detection and p
attern
recognition, AI-powered intrusion detection systems.

Security Operations: AI-driven SIEM and log analysis, au
tomated incident
response using AI, and AI for threat hunting and intelligence.

Risk Assessment and Compliance: AI f
or security compliance automation, risk
assessment and analysis using machine learning, and AI in policy enforcement
a
nd monitoring.

Advanced Prompt Engineering for IT Security: Prompt engineering
fundamentals, LLM settings optimizati
on, zero-shot and few-shot prompting
techniques, meta prompting and prompt chaining strategies, Tree of Thoughts
metho
dology, and security-specific prompt examples.

AI for User Support and Problem-Solving: Implementing AI for IT suppor
t,
AI-driven troubleshooting and diagnostics, and automated problem resolution
using machine learning.

AI Tools and
 Platforms for Cybersecurity: Microsoft Copilot for Security,
Perplexity.ai for research and analysis, capabilities and
 use cases of Claude,
ChatGPT, and Gemini, and custom GPT creation for specialized security tasks.

Data Analysis and
 Insights: Anomaly detection in large datasets and predictive
analytics for threat forecasting.

AI Application Devel
opment for Cybersecurity: Python programming for AI
security applications, LangChain Functions, Tools, and Agents), Gra
dio and
Streamlit for building AI security dashboards, and semantic search
implementation.

Advanced LLM Techniques:
 RAG Retrieval-Augmented Generation), prompt
caching, embeddings, fine-tuning, and function calling in LLMs.

Securit
y Automation: Developing AI-powered security scripts, command line
AI completions for security tasks, and automating vu
lnerability management
with AI.


If you’ve read this far, I thank you for your time and I'd appreciate any advice/s
uggestion.
```
---

     
 
all -  [ Langflow with Pgvector migrations ](https://www.reddit.com/r/langflow/comments/1gbl8as/langflow_with_pgvector_migrations/) , 2024-10-28-0913
```
I have been using Langflow with postgresql as a backend database. I have connected it to a separate 'langflow' database 
where all flows and messages are saved.

Now I am trying to build a RAG system using pgvector. When I connect it to the 
same 'langflow' db for storing the vector embeddings, it creates the langchain_pg_collection and langchain_pg_embedding 
tables and everything works perfectly. But later when I am restarting the server, I am running into migration issues tel
ling there is a mismatch.

Has anyone faced similar issues?

Should I use a separate database for maintaining the vector
 storage instead of using the same 'langflow' database?
```
---

     
 
all -  [ Summarising contexts spread across pages ](https://www.reddit.com/r/LangChain/comments/1gbl6i6/summarising_contexts_spread_across_pages/) , 2024-10-28-0913
```
Can a suitable RAG technique be applied to summarise like say, a particular chapter or section spread across many pages 
in a document? Ideally the pipeline should retrieve all chunks belonging only of that chapter.

I have checked LLM sherp
a so far which had a nice pdf parser utility to get section headings and does smart chunking (i.e) appending section tit
les to chunks. This should ideally help during retrieval stage. 

I had a problem of installing llm sherpa and manually 
did the job of appending section titles to chunks. However retrieval with faiss and Claude embeddings were not good as I
 expected. So summary is very bland but still slightly better than normal chunking.

I also checked calpoli which deals 
with pdf as image format and it's really good with retrieval and we don't have to go through the entire hassle of chunki
ng but the problem of retrieving specific sections alone is still a challenge.


Alternate solution:
1. Using a PDF pars
er to identify sections and summarising with help of long context models (not sure if long context models can distill ev
ery portion of the text and not have lost in the middle problem)

If anyone has any thoughts or suggestions on how to go
 about any new techniques on summarisation, it would be helpful for me to go about :)
```
---

     
 
all -  [ Code included: scrape websites agentically with LangGraph x Firecrawl ](https://www.reddit.com/r/LangChain/comments/1gbl08x/code_included_scrape_websites_agentically_with/) , 2024-10-28-0913
```
Video: [https://www.youtube.com/watch?v=vSz5-KeRyHs](https://www.youtube.com/watch?v=vSz5-KeRyHs)

Code: [https://github
.com/trancethehuman/ai-workshop-code/blob/main/Scrape\_the\_web\_agentically\_with\_Firecrawl\_and\_LangGraph.ipynb](htt
ps://github.com/trancethehuman/ai-workshop-code/blob/main/Scrape_the_web_agentically_with_Firecrawl_and_LangGraph.ipynb)


  
Feedbacks are welcomed!
```
---

     
 
all -  [ Fixing Langchain.js's ToolCallingAgentOutputParser Error with Ollama LLM and a Custom Tool ](https://www.reddit.com/r/MailDevNetwork/comments/1gbf79d/fixing_langchainjss_toolcallingagentoutputparser/) , 2024-10-28-0913
```
&#x200B;

https://preview.redd.it/25s1rc2m5swd1.png?width=1024&format=png&auto=webp&s=35a587bd303daaf6b8e7fd8709c5394189
9b3058

   


## Understanding and Fixing ToolCallingAgentOutputParser Errors in Langchain.js

&#x200B;

https://preview
.redd.it/92oj3izm5swd1.jpg?width=1154&format=pjpg&auto=webp&s=47a67415154f9d91a45caa707340c900aa1bc6be

&#x200B;

When w
orking with **Langchain**.js v2, developers often aim to create efficient agents using custom tools and language models 
like Ollama. However, integrating these components can sometimes lead to errors that are difficult to debug.

One such e
rror is the 'parseResult on ToolCallingAgentOutputParser only works on ChatGeneration output,' which can occur when buil
ding a custom tool within the agent framework. Understanding the root cause of this issue is crucial to ensure the agent
 and tool work correctly.

This article explores a simple implementation of a custom tool that adds 2 to a number input,
 using Langchain's createToolCallingAgent and the Ollama model. By analyzing the error and its context, we can better gr
asp how to troubleshoot it.

The following sections will guide you through the code, explain the error, and provide solu
tions to address this problem. Whether you're new to Langchain.js or experienced, this guide will help you move past thi
s issue efficiently.

  


https://preview.redd.it/g60hygyq5swd1.png?width=770&format=png&auto=webp&s=22604a722b406efeda
e80b26cac23493483239e1

&#x200B;

### Understanding the Custom Tool and Agent Error Handling in Langchain.js

&#x200B;


https://preview.redd.it/rv42ibon5swd1.jpg?width=1125&format=pjpg&auto=webp&s=886d2b2c1a5e29ee3c8a17f3f8dc5b5d8ab52a83

&
#x200B;

In the example provided, we are working with Langchain.js v2 to create a custom tool that integrates with the *
*Ollama** language model. The main purpose of the tool is to perform a simple mathematical operation: adding 2 to the in
put value. The tool is built using Langchain’s **tool** function, which defines reusable functions that can be invoked b
y an agent. To ensure the tool works correctly, the input schema is validated with the Zod library, guaranteeing that th
e input is a valid number. This ensures proper error handling and prevents the tool from failing due to invalid inputs.


The custom tool is then incorporated into an agent using the **createToolCallingAgent** function. This command allows t
he agent to call the tool when needed, and the agent is powered by the Ollama model, which is configured with specific p
arameters such as temperature to control the creativity of the responses. To facilitate smooth interaction between the a
gent and the tool, a chat prompt template is used. This template organizes the conversation by defining different types 
of messages, such as system messages, human input, and placeholders. The placeholders, such as **MessagesPlaceholder**, 
allow the conversation to be dynamic, with elements like the chat history being included.

One of the key issues address
ed in this example is the error handling around the Langchain agent's output parsing. The error message 'parseResult on 
ToolCallingAgentOutputParser only works on ChatGeneration output' stems from a mismatch between the type of output expec
ted by the parser and the actual output generated. To handle this error, the custom tool is wrapped in robust logic, ens
uring that all inputs and outputs conform to expected formats. This is further managed by the **AgentExecutor** class, w
hich coordinates the execution of the agent and tools, making sure that the query and tool output are properly synchroni
zed.

Finally, the scripts implement asynchronous execution using **await**, allowing the system to handle operations wi
thout blocking other processes. The agent waits for the tool to return its result before proceeding, ensuring that the r
esponse is both accurate and timely. Additionally, unit tests are included to validate the tool's functionality, ensurin
g that it consistently produces the correct output. These tests not only confirm the tool’s mathematical operation but a
lso check how well it handles invalid input, improving the overall reliability of the solution. This modular and error-r
esistant design makes the scripts reusable and effective for various applications within Langchain.js.

### Fixing the L
angchain.js Error with Modular Approach

&#x200B;

https://preview.redd.it/vzhle79o5swd1.jpg?width=1125&format=pjpg&auto
=webp&s=53a00eddcdf8d55c69f06e09feef2ecfa3e8d2ac

&#x200B;

Solution 1: JavaScript with modular approach and error handl
ing using Langchain.js and Ollama LLM

  


https://preview.redd.it/1un0bpfr5swd1.png?width=770&format=png&auto=webp&s=d
ebc0f320eee837df3b429964af11783593bb87c

&#x200B;

    import { tool } from '@langchain/core/tools';
    import { z } fr
om 'zod';
    import { Ollama } from '@langchain/ollama';
    import { ChatPromptTemplate } from '@langchain/core/prompt
s';
    import { createToolCallingAgent } from 'langchain/agents';
    import { AgentExecutor } from 'langchain/agents';

    // Initialize LLM with Ollama
    const llm = new Ollama({
    model: 'llama3',
    temperature: 0.7,
    });
    /
/ Custom tool to add 2 to the input number
    const magicTool = tool(
    async (input) => {
    return input + 2;
    
},
    {
    name: 'magic_function',
    description: 'Applies a magic function to an input',
    schema: z.object({ inp
ut: z.number() }),
    };
    );
    const tools = [magicTool];
    // Setup ChatPromptTemplate with placeholders
    co
nst prompt = ChatPromptTemplate.fromMessages([
    ['system', 'You are a helpful assistant called iHelp'],
    ['placeho
lder', '{chat_history}'],
    ['human', '{input}'],
    ['placeholder', '{agent_scratchpad}'],
    ]);
    // Agent conf
iguration
    const agent = createToolCallingAgent({ llm, tools, prompt });
    // Execute agent query
    const agentEx
ecutor = new AgentExecutor({ agent, tools });
    const query = 'What is the value of magic_function(3)?';
    await age
ntExecutor.invoke({ input: query });

### Enhanced Error Handling for Langchain.js Agent

&#x200B;

https://preview.redd
.it/8dnx85uo5swd1.jpg?width=1125&format=pjpg&auto=webp&s=8f53e33e08c7f78293a561e99ddb195598550338

&#x200B;

Solution 2:
 Error handling with unit tests to validate the custom tool's output in Langchain.js

  


https://preview.redd.it/ncpxq
wsr5swd1.png?width=770&format=png&auto=webp&s=cbf1ec679ffd93a951be5fde0c1328f7b32d2f9e

&#x200B;

    import { tool } fr
om '@langchain/core/tools';
    import { z } from 'zod';
    import { Ollama } from '@langchain/ollama';
    import { cr
eateToolCallingAgent } from 'langchain/agents';
    import { AgentExecutor } from 'langchain/agents';
    // Initialize 
LLM with Ollama
    const llm = new Ollama({ model: 'llama3', temperature: 0.7 });
    // Custom tool with added error h
andling
    const magicTool = tool(
    async (input) => {
    try {
    if (typeof input !== 'number') throw new Error(
'Invalid input type!');
    return input + 2;
    } catch (err) {
    return err.message;
    }
    },
    {
    name: '
magic_function',
    description: 'Adds 2 to input and handles errors',
    schema: z.object({ input: z.number() }),
   
 }
    );
    const tools = [magicTool];
    // Agent and execution
    const agent = createToolCallingAgent({ llm, tool
s });
    const agentExecutor = new AgentExecutor({ agent, tools });
    const query = 'magic_function('abc')'; // Test 
with invalid input
    await agentExecutor.invoke({ input: query });
    // Unit test example
    import { expect } from
 'chai';
    it('should return 5 when input is 3', async () => {
    const result = await magicTool(3);
    expect(resul
t).to.equal(5);
    });

### Exploring the Role of Agents in Langchain.js and Ollama LLM Integration

&#x200B;

https://
preview.redd.it/zzqgr6fp5swd1.jpg?width=1125&format=pjpg&auto=webp&s=c4fd1a130466b3ce19222a181bed36e6f8b70514

&#x200B;


When working with Langchain.js, integrating **agents** with tools and language models like Ollama is a critical aspect 
of building dynamic applications. An agent allows you to connect a custom tool, which performs specific tasks, to a lang
uage model, which handles more conversational or generative tasks. By using agents, developers can automate workflows wh
ere a model not only generates responses but also invokes tools to perform calculations or data processing.

The key com
ponent in this integration is the **createToolCallingAgent** function. This function lets the agent trigger specific too
ls when necessary, ensuring that tasks are completed accurately and efficiently. While the primary focus is often on cre
ating the tool itself, understanding how to manage the agent's workflow and avoid parsing errors is equally important. E
rrors like 'parseResult on ToolCallingAgentOutputParser only works on ChatGeneration output' usually occur when the agen
t's output isn't compatible with the parsing system, highlighting the need for proper alignment between the agent’s outp
ut and the expected format.

The use of prompt templates, such as **ChatPromptTemplate**, further enriches the interacti
on by allowing dynamic messages and context placeholders. This allows the agent to adjust its responses based on the cha
t history or the agent’s scratchpad. Optimizing the prompt templates and ensuring the agent's outputs are correctly pars
ed can prevent many common errors, making your Langchain.js applications more reliable and efficient.

#### Frequently A
sked Questions About Langchain.js, Agents, and Tools

&#x200B;

https://preview.redd.it/pvpvrb0q5swd1.jpg?width=1155&for
mat=pjpg&auto=webp&s=319ff3e15b969c2a8994adf870969bc6ce083a36

&#x200B;

What is an agent in Langchain.js?

An agent is 
a component that interacts with tools and language models to perform specific tasks based on a user query. It uses the *
*createToolCallingAgent** function to trigger tools.

How do you resolve the 'parseResult on ToolCallingAgentOutputParse
r' error?

This error occurs when the agent's output is incompatible with the parser. Ensure the output matches what the
 parser expects and use a **ChatGeneration** output format.

What is the purpose of the **AgentExecutor**?

The **AgentE
xecutor** manages the execution of the agent and its tools, allowing you to run complex workflows in Langchain.js applic
ations.

How does **ChatPromptTemplate** work?

**ChatPromptTemplate** organizes chat messages in a structured format, a
llowing for dynamic content such as chat history and agent scratchpad to be inserted into the conversation flow.

Why is
 **Zod** used in the tool?

**Zod** is used for input validation, ensuring that the input to the custom tool is of the c
orrect type (e.g., a number), which reduces the chances of errors.

#### Final Thoughts on Error Handling in Langchain.j
s

&#x200B;

https://preview.redd.it/zo3vhblq5swd1.jpg?width=1155&format=pjpg&auto=webp&s=cbd875f11336a2ae96df0616433a1c
7d4bfad09e

&#x200B;

Solving the 'parseResult on ToolCallingAgentOutputParser only works on ChatGeneration output' erro
r requires careful alignment between the output of your agent and its parsing expectations. With the right approach, thi
s error can be avoided.

By using appropriate tools like **Zod** for validation and ensuring that agents, such as those 
built with Ollama, handle inputs and outputs correctly, you can create robust solutions in **Langchain**.js without enco
untering parsing issues.

###### Sources and References for Langchain.js Error Resolution

Elaborates on the official La
ngchain documentation, which provides insights into tool creation and agent configurations. [**Langchain Documentation**
](https://docs.langchain.com/) Inside.

Further explains the use of Zod for input validation and its application in Lang
chain.js. [**Zod Documentation**](https://zod.dev/) Inside.

Describes the Ollama language model and its implementation 
within custom agents. [**Ollama LLM**](https://ollama.ai/) Inside.

[**Fixing Langchain.js's ToolCallingAgentOutputParse
r Error with Ollama LLM and a Custom Tool**](https://www.tempmail.us.com/en/langchain/fixing-langchain-js-s-toolcallinga
gentoutputparser-error-with-ollama-llm-and-a-custom-tool)  
 
```
---

     
 
all -  [ List of FREE and Best Selling Discounted Courses ](https://www.reddit.com/r/udemyfreeebies/comments/1gbc5qo/list_of_free_and_best_selling_discounted_courses/) , 2024-10-28-0913
```
# Udemy Free Courses for 25 October 2024

Note : Coupons might expire anytime, so enroll as soon as possible to get the 
courses for FREE.

* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20820/)Open-source LLMs: Uncensored & secure AI l
ocally with RAG
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20819/)AI-Agents: Automation & Business with LangCha
in & LLM Apps
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20818/)How to Become an Embedded Systems Engineer Boot
camp
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20817/)Herramientas de Google 2024, ¡Desde Cero Hasta Experto!

* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20816/)Coaching program – Become the Woman of Your Life!
* [REDEEM O
FFER ](https://idownloadcoupon.com/udemy/20815/)Practice Exams | AWS Certified Solutions Architect Associate
* [REDEEM O
FFER ](https://idownloadcoupon.com/udemy/20814/)Staff Engineer Survival Manual: AI Era Technical Leadership
* [REDEEM OF
FER ](https://idownloadcoupon.com/udemy/20813/)Curso de microservicios con Spring Boot y Spring Cloud
* [REDEEM OFFER ](
https://idownloadcoupon.com/udemy/20812/)Curso Completo de Kubernetes Desde Cero para Programadores
* [REDEEM OFFER ](ht
tps://idownloadcoupon.com/udemy/20811/)Tiktok Ads marketing Crash Course For Beginners (Hindi/Urdu)
* [REDEEM OFFER ](ht
tps://idownloadcoupon.com/udemy/20810/)Google Ads And Tiktok Ads Crash Course (Hindi/ Urdu)
* [REDEEM OFFER ](https://id
ownloadcoupon.com/udemy/20809/)Tiktok Marketing & Shopify Ecommerce store (hindi/urdu)
* [REDEEM OFFER ](https://idownlo
adcoupon.com/udemy/20808/)Facebook Marketing + Whatsapp Ads (CASE STUDY) Hindi 2023
* [REDEEM OFFER ](https://idownloadc
oupon.com/udemy/20807/)Digital Marketing Business With Google My Business
* [REDEEM OFFER ](https://idownloadcoupon.com/
udemy/20806/)Google Ads Mastery\~ Beginner To Pro \~ HINDI/URDU 2023
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy
/20805/)Facebook Ads Marketing Funnel For Ecommerce Hindi
* Secret Facebook Ads Targeting Pro Stratigies 2023 In Hindi
*
 [REDEEM OFFER](https://idownloadcoupon.com/udemy/20804/)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20803/)Est
rategias Pro de Targeting de Audiencia con Facebook Ads
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20802/)Marke
ting en Facebook Ads – Leads /Clientes Potenciales 2023
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20801/)700-7
55: Cisco Security Sales Specialist Exam
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20800/)Configuración y Opti
mizacion de tu Página de Facebook 2023
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20799/)Facebook Ads & Ecommer
ce Easy Course 2023 Hindi
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20798/)Essential Photoshop Course Beginner
 to Intermediate
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20797/)Basic to Advanced T-shirt Design with Adobe 
Photoshop CC
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20796/)Certification in Welding Technology for Engineer
s – CWI
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20795/)Facebook Ads Marketing In Hindi/Urdu 2023
* [REDEEM O
FFER ](https://idownloadcoupon.com/udemy/20794/)Easy Instagram Marketing In Hindi
* [REDEEM OFFER ](https://idownloadcou
pon.com/udemy/20793/)Como crear y configurar tu canal de Youtube desde cero 2023
* [REDEEM OFFER ](https://idownloadcoup
on.com/udemy/20792/)Data Structures and OOP with C++ : CS104, CS105 Masterclass
* [REDEEM OFFER ](https://idownloadcoupo
n.com/udemy/20791/)1Z0-1104-23: Oracle Security Professional Practice Exam
* [REDEEM OFFER ](https://idownloadcoupon.com
/udemy/20790/)Generative AI for Beginners: Future of Innovation Unlocked
* [REDEEM OFFER ](https://idownloadcoupon.com/u
demy/20789/)700-760: Cisco IoT Advantage Sales Specialist Exam
* Canva Design Crash Course
* [REDEEM OFFER](https://idow
nloadcoupon.com/udemy/20788/)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20787/)Lightroom Classic CC: Master th
e Library & Develop Module
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20786/)Adobe Illustrator for Everyone: De
sign Like a Pro
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20785/)CEH v12 Certification Practice Questions 2024

* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20784/)AWS Certified AI Practitioner (AIF-C01) Practice Exam 2024
*
 [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20783/)AZ-900: Microsoft Azure Fundamentals Practice Questions 2024
*
 [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20782/)PCAP Certified Associate Python Programmer Practice Exam
* [RE
DEEM OFFER ](https://idownloadcoupon.com/udemy/20781/)MS Word – Microsoft Word Course Beginner to Expert
* [REDEEM OFFER
 ](https://idownloadcoupon.com/udemy/20780/)45-Day ESP32 Bootcamp
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20
779/)CompTIA Cloud+ (CV0-004): Complete Exam Prep & Cloud Mastery
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20
778/)AWS Certified AI Practitioner: Exam Prep & AI Foundations
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20777
/)AWS Certified Cloud Practitioner: Exam Prep & Cloud Mastery
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20776/
)Linux Command-Line & Shell Scripting for Absolute Beginners
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20775/)
Introduction to AI and ChatGPT
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20774/)Arduino 4 Seven Segments Displ
ay Interfacing
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20773/)Introduction to ARM Cortex-M Architecture
* Be
st Prompt Engineering Practice Tests & Interview Questions
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/20772/)
* 
[REDEEM OFFER ](https://idownloadcoupon.com/udemy/20771/)Cloud Computing Masterclass – Deployment to Administration
* [R
EDEEM OFFER ](https://idownloadcoupon.com/udemy/20770/)AI Governance Professional (AIGP) Certification & AI Mastery
* [R
EDEEM OFFER ](https://idownloadcoupon.com/udemy/20769/)CGRC – Governance, Risk and Compliance Certification Mastery
* [R
EDEEM OFFER ](https://idownloadcoupon.com/udemy/20768/)HSE Certification – ISO 14001 & OHSAS 18001
* [REDEEM OFFER ](htt
ps://idownloadcoupon.com/udemy/20767/)NVIDIA-Certified Associate: AI Infrastructure and Operations
* [REDEEM OFFER ](htt
ps://idownloadcoupon.com/udemy/20766/)Mastering C++ Fundamentals with Generative AI: A Hands-On
* [REDEEM OFFER ](https:
//idownloadcoupon.com/udemy/20765/)Java Mastery Intermediate: Methods, Collections, and Beyond
* [REDEEM OFFER ](https:/
/idownloadcoupon.com/udemy/20764/)Mastering Advanced Java with Object-Oriented Programming
* [REDEEM OFFER ](https://ido
wnloadcoupon.com/udemy/20763/)Generative AI for Dynamic Java Web Applications with ChatGPT
* [REDEEM OFFER ](https://ido
wnloadcoupon.com/udemy/20762/)Mastering Tabnine AI for Efficient Code Development
* [REDEEM OFFER ](https://idownloadcou
pon.com/udemy/20761/)Android Projects Course Build 3 Applications from Scratch
* [REDEEM OFFER ](https://idownloadcoupon
.com/udemy/20760/)Android Apps Development in Hindi and Build 10 Applications
* [REDEEM OFFER ](https://idownloadcoupon.
com/udemy/20759/)Android Very Basic App Development Course with Java in Hindi
* [REDEEM OFFER ](https://idownloadcoupon.
com/udemy/20758/)Zero Coding Website with Google Sites
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20757/)Unders
tanding Hair Color Foundations
* The Ultimate C Programming Practice Test-600+ Questions
* [REDEEM OFFER](https://idownl
oadcoupon.com/udemy/20756/)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20755/)SQL- The Complete Introduction to
 SQL programming
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20754/)07 Days of Code | Python Programming BootCam
p
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20753/)Excel Tips and trick : Learn MS Excel by making 7 Projects

* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20752/)Python for Data Science with Assignments
* [REDEEM OFFER ](ht
tps://idownloadcoupon.com/udemy/20751/)C++ And PHP Complete Course for C++ and PHP Beginners
* [REDEEM OFFER ](https://i
downloadcoupon.com/udemy/20750/)NSE5\_FMG-7.2: Fortinet Network Security Expert Practice 2024
* [REDEEM OFFER ](https://
idownloadcoupon.com/udemy/20749/)Currency Management for Small Businesses & Corporates
* [REDEEM OFFER ](https://idownlo
adcoupon.com/udemy/20748/)Entrenamiento Visual FoxPro 9 y MariaDB -Mod01
* [REDEEM OFFER ](https://idownloadcoupon.com/u
demy/20747/)Visual FoxPro – Clases Visuales (nueva versión)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20746/)E
ntrenamiento Visual FoxPro 9 y MySQL Server -Mod02
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20745/)Entrenamie
nto Visual FoxPro 9 y PostgreSQL -Mod01
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20744/)Tarea 01 Clases Visua
les y otras Herramientas – VFP Avanzado
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20743/)Complete JS Bootcamp 
| JavaScript Programming in 7 DAYS
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20742/)Theoretical Foundations of
 AI in Cybersecurity
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20741/)Principles and Practices of the Generati
ve AI Life Cycle
* Principles of Governance in Generative AI
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/20740/)

* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20739/)Philosophy and Foundations of Artificial Intelligence (AI)
* 
[REDEEM OFFER ](https://idownloadcoupon.com/udemy/20738/)LATEST | Learn Advanced Python Programming | SOURCE CODE
* [RED
EEM OFFER ](https://idownloadcoupon.com/udemy/20737/)Introduction to Quantum Computing
* [REDEEM OFFER ](https://idownlo
adcoupon.com/udemy/20736/)Certified Data Management Professional (CDMP) – Associate
* [REDEEM OFFER ](https://idownloadc
oupon.com/udemy/20735/)Run Multiple Sites on an Instance: Digital Ocean & Linode
* [REDEEM OFFER ](https://idownloadcoup
on.com/udemy/20734/)Build a WordPress Powered Amazon Affiliate Site on NGINX
* [REDEEM OFFER ](https://idownloadcoupon.c
om/udemy/20733/)Linode: Build a Scalable Blog App using PHP & MySQL DB
* [REDEEM OFFER ](https://idownloadcoupon.com/ude
my/20732/)Cloud Computing Essentials: Linode, Linux, and LAMP Stack
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/
20731/)Configure NGINX on a Cloud Server: Digital Ocean & AWS
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20730/
)Linode: Web Server and Database Foundations
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20729/)HTML, CSS, & Jav
aScript – Certification Course for Beginners
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20728/)Linode: Build an
d Deploy Responsive Websites on the Cloud
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20727/)Run Multiple Sites 
on a Cloud Server: AWS & Digital Ocean
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20726/)Build and Deploy Respo
nsive Websites on AWS using HTML & CSS
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20725/)GetResponse email mark
eting for beginners
* Internet & Cloud Computing Foundations
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/20724/)

* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20723/)Cloud-Powered Web App Development with AWS and PHP
* [REDEEM 
OFFER ](https://idownloadcoupon.com/udemy/20722/)Introduction to Domain Names and Web Hosting – Quick Guide
* [REDEEM OF
FER ](https://idownloadcoupon.com/udemy/20721/)How the Internet Works & the Web Development Process
* [REDEEM OFFER ](ht
tps://idownloadcoupon.com/udemy/20720/)Setup a Virtual Web Server using Linode or Digital Ocean
* [REDEEM OFFER ](https:
//idownloadcoupon.com/udemy/20719/)Build an Amazon Affiliate E-Commerce Store from Scratch
* [REDEEM OFFER ](https://ido
wnloadcoupon.com/udemy/20718/)Cloud Computing and Amazon Web Services (AWS) Fundamentals
* [REDEEM OFFER ](https://idown
loadcoupon.com/udemy/20717/)AWS Identity and Access Management (IAM) Foundations
* [REDEEM OFFER ](https://idownloadcoup
on.com/udemy/20716/)Create a Members Only Blog using PHP, MySQL, & AJAX
* [REDEEM OFFER ](https://idownloadcoupon.com/ud
emy/20715/)Bootstrap & jQuery – Certification Course for Beginners
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/2
0714/)JavaScript & jQuery – Certification Course for Beginners
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20713
/)HTML, JavaScript, & Bootstrap – Certification Course
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20712/)Build 
a Simple Calculator in React + JavaScript Foundations
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20711/)300-415
: Cisco SD-WAN Solutions Practice test 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20710/)Amazon Elastic Co
mpute Cloud (EC2) Beginners Certification
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20709/)Blockchain Professi
onal Certification
* Setup LAMP Stack on a Remote Cloud Server + PHP Foundations
* [REDEEM OFFER](https://idownloadcoupo
n.com/udemy/20708/)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20707/)NGINX, Apache, SSL Encryption – Certifica
tion Course
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20706/)JavaScript, Bootstrap, & PHP – Certification for 
Beginners
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20705/)HTML, CSS, & Bootstrap – Certification Course for B
eginners
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20704/)The Complete Guide to Effective Communication Skills

* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20703/)Digital Marketing Automation: One Step Ahead of Competitors

* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20702/)Account-Based Marketing – ABM: Increase Your B2B Efficiency
*
 [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20701/)How to Create Your Perfect LinkedIn Outreach Campaign
* [REDEE
M OFFER ](https://idownloadcoupon.com/udemy/20700/)Facebook Ads: Run Your First Ad Campaign
* [REDEEM OFFER ](https://id
ownloadcoupon.com/udemy/20699/)Google My Business. How to Master Powerful Tool for Company
* [REDEEM OFFER ](https://ido
wnloadcoupon.com/udemy/20698/)Web Analytics with Similarweb: from Basic to PRO!
* [REDEEM OFFER ](https://idownloadcoupo
n.com/udemy/20697/)CDO Chief Digital Officer Executive Certification
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy
/20696/)Timeboxing: A Short and Practical Guide
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20695/)Make a WordPr
ess Website with Elementor
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20694/)Mastering SEO With ChatGPT: Ultima
te Beginner’s Guide
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/20693/)Implementing Agile Marketing and Marketin
g Sprints

GET MORE FREE ONLINE COURSES WITH CERTIFICATE – [CLICK HERE](https://idownloadcoupon.com/)
```
---

     
 
all -  [ RAG text to sql ](https://www.reddit.com/r/LangChain/comments/1gbc0pu/rag_text_to_sql/) , 2024-10-28-0913
```
Does anyone have any good tutorial that walks through generating sql queries based on vector store chunks of data?

The 
tutorials I see are sql generators based off of the actual db. This would be just based on text, markdown files and pdf 
chunks which house examples and data reference tables. 


```
---

     
 
all -  [ Suggestions for Video RAG Integration: Frame-by-Frame Analysis & Timestamp Queries ](https://www.reddit.com/r/LangChain/comments/1gb9lwx/suggestions_for_video_rag_integration/) , 2024-10-28-0913
```
Hey everyone! 👋

I’m currently working on a multimodal multi-query RAG system. So far, I’ve integrated:

Blogs 📝
Video S
ummaries 🎥
Audio 🎧
PDFs 📄
Images 🖼️
The next challenge I’m tackling is Video RAG — specifically, I want it to:

Understa
nd videos at specific timestamps
Analyze frame-by-frame content
Answer questions related to those timestamps
I’m looking
 for any suggestions or ideas on how I can enhance this video understanding part, especially with the timestamp and fram
e analysis. Any input or tips would be super helpful!

Thanks in advance! 🙌
```
---

     
 
MachineLearning -  [ [D] How are folks building conversational Retrieval Augmented Generation apps ](https://www.reddit.com/r/MachineLearning/comments/1ftdby7/d_how_are_folks_building_conversational_retrieval/) , 2024-10-28-0913
```
I've read through various resources such as:  
- [https://vectorize.io/how-i-finally-got-agentic-rag-to-work-right/](htt
ps://vectorize.io/how-i-finally-got-agentic-rag-to-work-right/)  
- [https://python.langchain.com/docs/tutorials/qa\_cha
t\_history/](https://python.langchain.com/docs/tutorials/qa_chat_history/)  
- [https://langchain-ai.github.io/langgraph
/tutorials/rag/langgraph\_agentic\_rag/](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/) 
 
- [https://docs.llamaindex.ai/en/stable/module\_guides/deploying/chat\_engines/](https://docs.llamaindex.ai/en/stable/
module_guides/deploying/chat_engines/)  
- [https://huggingface.co/datasets/nvidia/ChatRAG-Bench](https://huggingface.co
/datasets/nvidia/ChatRAG-Bench) 

But these feel overly reductive, since they don't address complexities like:  
1) when
 to retrieve vs. just respond immediately to reduce latency  
2) rely on existing context previously retrieved in the co
nversation instead of retrieving again at the current turn  
3) partition LLM context between retrieved information and 
past conversation history.

I'm sure some teams already have good systems for this, would appreciate pointers!
```
---

     
 
deeplearning -  [ Fast AI's deep learning for coders by jeremy howard for begginer?  ](https://www.reddit.com/r/deeplearning/comments/1gb2k3p/fast_ais_deep_learning_for_coders_by_jeremy/) , 2024-10-28-0913
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

     
