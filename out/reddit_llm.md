 
all -  [ What is the best way to set up multiple LLMs for the best results?
 ](https://www.reddit.com/r/LangChain/comments/1et9bd2/what_is_the_best_way_to_set_up_multiple_llms_for/) , 2024-08-16-0911
```
I am creating an AI agent for copywriting, it is something that I have done for a while and I think it is one of the are
as that LLMs can greatly help. First, I know that no agent can be better than a good copywriter with solid experience bu
t truth be told, most copywriters I’ve came across are mostly average or slightly above average, and that’s what I’m aim
ing for, content that your slightly above average copywriter can come up with(if I can get higher quality, even better)


I know that using multiple LLMs in setups like Chain-of-thought and LLM-Debate can produce the best results. For the st
art, I want to use two LLMs;

The first LLM will receive some information about ,say, a product, then it will come up wi
th content. This LLM should be knowledge rich and if possible should have the ability to do internet searches to get mor
e information.

The first response is then forwarded to the second LLM, which is the “creative” one. This LLM will be pr
e prompted to understand the context and should have powerful literary criticism capabilities. It will go through the co
ntent and check to ensure it is within the given context and that it has the literary styles that give the content a uni
que voice.

The second LLM then responds with the final response which we can use as product copy.

I am testing this at
 [~SmythOS~](https://smythos.com/) and I would like to know if you have any suggestions on how I can do this best. Which
 models should I use for LLM1 and LLM2? Are two LLMs even enough? What should I take note of for prompting? And any othe
r things I might be missing. Thanks in advance.
```
---

     
 
all -  [ FREE SOFTWARE TO CREATE  RESUME BASED ON JOB DESCRIPTION ](https://www.reddit.com/r/LangChain/comments/1et8x6n/free_software_to_create_resume_based_on_job/) , 2024-08-16-0911
```
# Introducing Resume_Builder_AIHawk🚀

Are you tired of spending hours perfecting your resume for every job application? 
Say hello to **Resume_Builder_AIHawk**, a powerful Python tool designed to make creating visually stunning resumes fast 
and effortless!

## 🛠️ Features:

- **Interactive Command-Line Interface:** Navigate through options and prompts with ea
se using our user-friendly CLI.
- **Dynamic Style Management:** Select from a variety of pre-defined resume styles to ma
tch your preference.
- **Job Description Integration:** Automatically customize your resume based on a job URL, ensuring
 it aligns perfectly with the job requirements and skills.

## 📈 Why Use Resume_Builder_AIHawk?

- **Save Time:** Quickl
y generate resumes tailored to specific job descriptions.
- **Increase Your Chances:** A resume that matches the job req
uirements can significantly boost your chances of landing that interview.
- **User-Friendly:** Designed with simplicity 
in mind to make resume building a breeze.

Ready to elevate your job application game? Check out [Resume_Builder_AIHawk 
on GitHub](https://github.com/your-repo-url) and start creating standout resumes today!

Feel free to ask any questions 
or provide feedback. Your input is invaluable!
```
---

     
 
all -  [ RAG Ingestion C4 Models ](https://www.reddit.com/gallery/1et5vf5) , 2024-08-16-0911
```

```
---

     
 
all -  [ Critique my design idea, please ](https://www.reddit.com/r/LocalLLM/comments/1et3nt7/critique_my_design_idea_please/) , 2024-08-16-0911
```
**TL;DR** I want to summarize multiple industry specific newsletters for
internal use. Am I on the right track?

I've be
en looking around for a newsletter summarizer for intrnal use in
my startup. I haven't found any that fit my criteria (s
ee below), so
before I head down some dead-end rabbit holes, I'd like to get some
feedback on my current ideas.

In my s
tartup, we need to keep up to date on the news in the widget
industry and we use newsletters as once source for that.

F
or the sake of this conversation, I'm going to define a newsletter as a
single file comprising *n* news pieces. There wi
ll be *m* newsletters.
Typically *n*, *m* < 10.

Not only do I want to summarize multiple industry newsletters, I also
w
ant to remove duplicate news bits -- I don't want to read *n*
summaries about the same news piece -- but also remove non
-relevant new
pieces. How 'relevant' is defined I'll worry about later.
I also want to have links in the summary referri
ng back to the original
newsletter.

I don't want to open accounts with a dozen websites. The only thing I
want to do ma
nually is open the final summary.

I want everything to be local but I'll use OpenAI as a first pass then
substitute $LO
CAL_LLM eventually.

I'm going to use [this
tutorial](https://python.langchain.com/v0.2/docs/tutorials/summarization/)
a
s a template/guide.
```
---

     
 
all -  [ Please rate my resume for internship. I am in 3rd sem college.  ](https://i.redd.it/t5vehbyqmvid1.jpeg) , 2024-08-16-0911
```
I am not a softy so you can be as real as you want and thank you for your time 💙
```
---

     
 
all -  [ Knowledge management platform + RAG ](https://www.reddit.com/r/LangChain/comments/1et2c5n/knowledge_management_platform_rag/) , 2024-08-16-0911
```
Hey! Anyone has experience integrating a knowledge management system with a vector database (RAG)? 

I’m trying to look 
for platforms (ideally open source), that can be used to manage documents, and at the same time to feed a vector databas
e to do RAG.

Any ideas?
```
---

     
 
all -  [ Can Local RAG find location from where the answers are found? ](https://www.reddit.com/r/LocalLLaMA/comments/1et1icn/can_local_rag_find_location_from_where_the/) , 2024-08-16-0911
```
Hi, I have a built a simple RAG program using Ollama and Langchain (RetrievalQA). I have 15 PDF files, with each being 0
.5MB \~ 1MB, 95% text. It works really good for a short few lines of code. While it does provide me the right answer and
 many times what is the section header it is from, it doesn't provide the source file name.

When I created a sample app
lication using OpenAI File Search API tutorial, and that is able to provide me the answer along with which file the data
 is from.

How can I replicate this in Langchain? Is it even possible to get the source file using RetrievalQA? My guess
 is that since we are chunking (using RecursiveCharacterTextSplitter) may be that information is lost? If so, what other
 methods can be used to find the source?

Given that there are so many tutorials on Local RAG using Langchain, google se
arch is not showing up the right one.
```
---

     
 
all -  [ How to debug why obvious questions are missed? ](https://www.reddit.com/r/LangChain/comments/1eszali/how_to_debug_why_obvious_questions_are_missed/) , 2024-08-16-0911
```
I'm using langchain with a Chroma db, and huggingface embeddings. My goal is to have it read pdfs and answer basic quest
ions.

I wanted it to answer 'what is the study title' but wasn't having much luck, so I explicitly stated in the docume
nt: 'The study title is 'abc123'' and it still responded with either a wrong answer, or 'the study title is not explicit
ly stated in the document'. 

Any ideas as to how I can debug this?
```
---

     
 
all -  [ unhashable type: 'dict' - Help Needed ](https://www.reddit.com/r/LangChain/comments/1esvvie/unhashable_type_dict_help_needed/) , 2024-08-16-0911
```
  
I used this code with other versions, but I accidentally changed the langgraph and langchain-core versions, and now I
 can't for what version it worked

    AgentState = {}
    
    AgentState['a'] = []
    AgentState['b'] = []
    AgentS
tate['c'] = []
    AgentState['d'] = []
    
    #... nodes defined here in between
    
    from langgraph.graph import
 StateGraph, END
    
    graph = StateGraph(AgentState)
    
    #... graphs defined
    

  
In what versions this wor
ks, or how to work around this?
```
---

     
 
all -  [ Working with RAG Models in Python: Why LangChain and Django Are Becoming Popular ](https://www.reddit.com/r/django/comments/1esvnji/working_with_rag_models_in_python_why_langchain/) , 2024-08-16-0911
```
Recently started working on RAG models using LangChain and found that many Python developers prefer this approach over d
irect AI assistants. Django is also recommended over Flask for scalability reasons. Would love to hear your experiences!

```
---

     
 
all -  [ Python Devs Prefer RAG Models: Insights on LangChain and Django vs. Flask ](https://www.reddit.com/r/Langchaindev/comments/1esvlgy/python_devs_prefer_rag_models_insights_on/) , 2024-08-16-0911
```
I've been exploring RAG models with LangChain and observed that Python developers often recommend RAG over traditional A
I assistants. There's also a push for Django instead of Flask due to scalability concerns. What do you think?
```
---

     
 
all -  [ Is RAG with LangChain the New Norm for Python LLM Integration? ](https://www.reddit.com/r/LangChain/comments/1esvjfz/is_rag_with_langchain_the_new_norm_for_python_llm/) , 2024-08-16-0911
```
As I delve into RAG models using LangChain, I've noticed a shift in the Python community towards RAG models rather than 
AI assistants for LLM integration. Additionally, Django is being recommended over Flask for scalability. Any thoughts?
```
---

     
 
all -  [ Transitioning to RAG Models and Django for Scalable Python AI Solutions ](https://www.reddit.com/r/learnprogramming/comments/1esvidl/transitioning_to_rag_models_and_django_for/) , 2024-08-16-0911
```
Recently started using RAG models with LangChain and noticed a preference among Python developers for RAG over AI assist
ants. Also, Django is suggested over Flask for scalability in AI projects. Curious about your opinions!
```
---

     
 
all -  [ RAG Models vs. AI Assistants: Which Is Better for Python LLM Integration? ](https://www.reddit.com/r/learnpython/comments/1esvfgu/rag_models_vs_ai_assistants_which_is_better_for/) , 2024-08-16-0911
```
Been exploring RAG models in LangChain recently and found that many Python developers lean towards RAG instead of tradit
ional AI assistants when integrating LLMs. Django is also being recommended over Flask for scalability. Thoughts?
```
---

     
 
all -  [ Why Are Python Devs Favoring RAG Models and LangChain for LLM Integration? ](https://www.reddit.com/r/PythonLearning/comments/1esvekm/why_are_python_devs_favoring_rag_models_and/) , 2024-08-16-0911
```
I've started working with RAG models in LangChain and observed that many Python developers prefer RAG over standard AI a
ssistants for direct LLM integration. There's also a shift towards using Django over Flask. What's your take?
```
---

     
 
all -  [ RAG Models in LangChain: A Game Changer for Python Developers? ](https://www.reddit.com/r/PythonProjects2/comments/1esvdtg/rag_models_in_langchain_a_game_changer_for_python/) , 2024-08-16-0911
```
Just dived into RAG models with LangChain and noticed a trend among Python devs favoring RAG over traditional AI assista
nts for LLM integration. Also, Django is being pushed over Flask for scalability. Would love to hear your experiences!
```
---

     
 
all -  [ Exploring RAG Models with LangChain: Is it Better than Traditional AI Assistants? ](https://www.reddit.com/r/pythontips/comments/1esvd9c/exploring_rag_models_with_langchain_is_it_better/) , 2024-08-16-0911
```
I've recently started experimenting with RAG models using LangChain and noticed that many Python developers recommend RA
G over direct AI assistants when integrating LLMs. I've also been advised to use Django instead of Flask for scalability
. What are your thoughts on this?
```
---

     
 
all -  [ Aiohttp and Requests in Webbaseloader ](https://www.reddit.com/r/LangChain/comments/1esv7m6/aiohttp_and_requests_in_webbaseloader/) , 2024-08-16-0911
```
I have been looking into the source of Webbaseloader and saw that requests.Session()'s attributes from \_\_init\_\_ are 
passed to aiohttp's session in \_fetch function. Is that all that connects the two or are these two libraries more integ
rated?  
From their docs I can tell these are independent projects
```
---

     
 
all -  [ An open source tutorial of controllable RAG agent for solving complex tasks (using langgraph) ](https://github.com/NirDiamant/Controllable-RAG-Agent) , 2024-08-16-0911
```
Hi all,

After sharing with you a broad collection of various strategies for RAG (https://github.com/NirDiamant/RAG_Tech
niques), 
I'm excited to share a controllable agent that can tackle complex RAG tasks, whether they involve challenging 
questions requiring reasoning or difficult data!

This agent includes a planner that dynamically creates and updates tas
ks necessary to solve the problem, along with retrieval and answering tools equipped with hallucination checks.

The age
nt is presented in a detailed Jupyter notebook, with every step thoroughly explained. For further information, the repos
itory also includes links to a Medium article and a YouTube video of a lecture I gave on the subject.

Enjoy!
```
---

     
 
all -  [ Migrating ReAct agents to LangGraph. Human input tool ](https://www.reddit.com/r/LangChain/comments/1esu831/migrating_react_agents_to_langgraph_human_input/) , 2024-08-16-0911
```
Hello,

I'm trying to migrate some of my ReAct agents to LangGraph. I've been using LangChain's 'create\_react\_agent' f
unction before and the human input tool has been working fine, but with the new function from langgraph.prebuilt the age
nt never prompts for input. I'm using load\_tools(\['human'\]).

How have you managed to create LangGraph agents that us
e this tool?
```
---

     
 
all -  [ I built a tool that parses unstructured documents into JSON (or JSONL on request). ld love your feed ](https://www.reddit.com/r/LangChain/comments/1ester7/i_built_a_tool_that_parses_unstructured_documents/) , 2024-08-16-0911
```
Hey everyone,

I wanted to share what I built to see what you guys think. I'm curious about any use cases you might have
 or just general feedback.

You can check out it out [here](https://www.pardocs.com).

I created [ParDocs](https://www.p
ardocs.com) with a simple mission: to make unstructured document extraction as painless as possible. I know firsthand ho
w much time and effort can go into pre-training and labeling, and I wanted to build a tool that lets you focus on what r
eally matters -> building and coding.

It’s free to use during this beta phase. After that, I'm considering pricing it a
t $0.09/page. I’d love to hear your feedback on this.

I’m personally available to answer any questions or help you get 
started.

Looking forward to your thoughts and feedback!
```
---

     
 
all -  [ Trying to build conversational AI agent/bot for meeting platforms like Meet/Zoom/Teams ](https://www.reddit.com/r/LangChain/comments/1essqv3/trying_to_build_conversational_ai_agentbot_for/) , 2024-08-16-0911
```
I am pretty new to this field. My goal is to build an AI agents/bot that can join a meeting, process the transcripts liv
e, send it to an LLM to generate responses and say that text out in the call.

I have built some selenium automation tha
t can join a meeting and relying on meet closed captions to generate a live transcript. I am unsure if that is a very sc
alable solution because all bots seem to be using the APIs directly for automation.

Are there any better ways to build 
meeting bots that can support 2-way conversations?

Also any best practices for building AI agent bots?
```
---

     
 
all -  [ An Image and Text Retrieval Framework You Can Take Away with Just a Ctrl-C ](https://www.reddit.com/r/LocalLLaMA/comments/1esrbsy/an_image_and_text_retrieval_framework_you_can/) , 2024-08-16-0911
```
HuixiangDou is an LLM-based knowledge assistant for group chat scenarios. With many people in a group chat, the robot sh
ould not respond to all messages. Its design rules are as follows:

* Stay silent on irrelevant content — rejection
* Di
rectly reply to what should be answered — retrieve
* Respect local policies and cultural sensitivities — reliable

[http
s://github.com/InternLM/HuixiangDou](https://github.com/InternLM/HuixiangDou)

In the [previous article](https://www.red
dit.com/r/LocalLLaMA/comments/1ekmljb/enhance_dense_retrieval_precision_with_hybrid/), we introduced how to enhance the 
ability of dense retrieval with a knowledge graph. This article shares the software design considerations in image and t
ext retrieval.

# 0x01 Software Design

There are already many well-known RAG frameworks on GitHub:

* **Langchain**: Ma
inly composed of `langchain-core` and `langchain-community`, providing a large number of LLM application examples
* **Gr
aphRAG**: Based on multi-turn LLM, builds knowledge graphs of different levels from the original text
* **RagFlow**: Pro
vides a complete set of RAG workflows, suitable for enterprises and individuals of different scales

HuixiangDou focuses
 on group chat scenarios. In addition to providing precision reports on business data, it is more simple and effective i
n implementation without historical baggage.

# Encouraging Users to Take the Code

It's not just about `pip install` an
d then calling APIs. HuixiangDou assumes that users also like to directly copy the source code.This can improve the expe
rience for both parties:

1. The author doesn't need to invest too much effort in API documentation and maintenance, aft
er all, there is no complex abstraction
2. It is also not difficult for users to understand, what you see is what you ge
t, just need to focus on the details

Therefore, HuixiangDou's source code has three core directories:

* `primitive`. S
ome basic designs, such as multimodal `Query`, `Splitter` methods, `Faiss`reading and writing faiss, etc.
* `service`. T
he pipeline required by RAG, such as web search, hybrid knowledge graph for rejection, etc.
* `frontend`. The access met
hod for group chat software (such as Feishu, WeChat, etc.)

Compared to `langchain`, HuixiangDou's design is more in lin
e with the original functions of each module, for example:

* The structure after splitting is `Chunk` rather than `Docu
ment`
* Whether the feature is normalized and which distance function is used depends on the design of the text2vec mode
l. This is not the responsibility of `faiss`
* `Query` is more friendly to images/voice, and does not need to be stuffed
 into awkward metadata

If users want to build their own RAG application, they don't want to introduce a large dependenc
y and don't want to write it themselves, they can just take the `primitive` directory with ctrl-c. HuixiangDou also prov
ides unit tests and precision reports to ensure that what is taken away is reliable.

# Image and Text Hybrid Retrieval


If there is 10G GPU mem, HuixiangDou can currently use Visualized-BGE to extract image features, and the features of im
ages and text are put into the same faiss library for subsequent retrieval.The feature library construction process is c
ompletely the same as pure text modality:

    python3 -m huixiangdou.service.feature_store --config_path config-multimo
dal.ini

Then run a simple gradio WebUI:

    python3 tests/test_query_gradio.py --config_path config-multimodal.ini

Su
bmit questions and images to retrieve the document to which the image belongs and answer:

https://preview.redd.it/kyx4l
e6uwsid1.png?width=1080&format=png&auto=webp&s=30235feed474d333eab83c794eeff394a6efa1ce

Notes:

* Manually download the
 eva-clip weights to the bge-m3 model directory. The essence of the Visualized-BGE model is to align the semantics of im
ages and text
* It is necessary to install HuixiangDou's `requirements-multimodal.txt` and the main branch of FlagEmbedd
ing, we have made some small fixes

Thanks to the simple design of primitive, HuixiangDou is still a BCE text model that
 only requires 1.5G of GPU mem by default. We have aligned the business accuracy before and after the implementation of 
multimodality.

# 0x02 Summary

This article shares the design considerations of HuixiangDou in the process of implement
ing image hybrid retrieval, and we encourage users to take the code more.I

n terms of image and text retrieval, current
ly only markdown are supported, and more formats need to be supported.
```
---

     
 
all -  [ Growing Context Architecture ](https://www.reddit.com/r/LangChain/comments/1espyux/growing_context_architecture/) , 2024-08-16-0911
```
Calling all langchain architects!   
I have a question around the potential architecture of an app I'm working on. Essen
tially, a client gives me some input for a feature, then I feed that into a prompt to extract lineitem requirements from
 that feature. Then the client gives me more information, and I feed that + the original client information and extract 
new / ammended requirements from the combined context. The client can repeat this process of giving more and more contex
t.   
  
I also have a prompt that can regenerate requirements at any given time.   
  
My question is, how should I han
dle this ever-growing context, and keep extracting the most up to date requirements using all known context. I have expl
ored the following:

* Adding all context to every prompt when I want to perform a new requirement extraction (this coul
d prove to become hard to manage with token limits)
* Using a vectorstore (this only uses a subset of the context unless
 k is very large - I think this is the wrong use case)
* Using a memory buffer (however this could get tainted over time
, especially if the regenerate prompt is run multiple times)
* Creating summaries at each step (this could potentially l
ose specific data) 

Am I overthinking this? Is there a preferred method that anyone has used / some sort of industry st
andard for this kind of use case? Many thanks!
```
---

     
 
all -  [ Use Langchain with OpenSource AI Gateway integrated with Guardrails ](https://www.reddit.com/r/Langchaindev/comments/1esokm8/use_langchain_with_opensource_ai_gateway/) , 2024-08-16-0911
```
We've been developing Portkey Gateway, an open-source AI gateway that's now processing billions of tokens daily across 2
00+ LLMs. Today, we're launching a significant update: integrated Guardrails at the gateway level.

Key technical featur
es:

1. Guardrails as middleware: We've implemented a hooks architecture that allows guardrails to act as middleware in 
the request/response flow. This enables real-time LLM output evaluation and transformation.
2. Flexible orchestration: T
he gateway can now route requests based on guardrail verdicts. This allows for complex logic like fallbacks to different
 models or prompts based on output quality.
3. Plugin system: We've designed a modular plugin system that allows integra
tion of various guardrail implementations (e.g., guardrails ai, microsoft/guidance, vectara/hallucination-detection).
4.
 Stateless design: The guardrails implementation maintains the gateway's stateless nature, ensuring scalability and allo
wing for easy horizontal scaling.
5. Unified API: Despite the added complexity, we've maintained our unified API across 
different LLM providers, now extended to include guardrail configurations.
6. Performance impact: Latency increase is mi
nimal (<20ms) for most guardrails, and even lesser for deterministic guardrails like regex match, json schema check, etc
.

Here's the link to docs - [Portkey's Integration with  Langchain](https://docs.portkey.ai/docs/welcome/integration-gu
ides/langchain-js)

Detailed note: [https://portkey.wiki/guardrail](https://portkey.wiki/guardrail)

Challenges we're st
ill tackling:

Standardizing evaluation metrics across different types of guardrails

Handling guardrail false positives
/negatives effectively

We believe this approach of integrating guardrails at the gateway level provides a powerful tool
 for managing LLM behavior in production environments.

The code is open-source, and we welcome contributions and feedba
ck.

We're particularly interested in hearing about specific use cases or challenges you've faced in implementing reliab
le LLM systems.

What are your thoughts on this approach? Are there specific guardrail implementations or orchestration 
patterns you'd like to see added?
```
---

     
 
all -  [ Roast my resume please.  Have 1.1 years of experience working as an SDE in data science team. ](https://www.reddit.com/r/developersIndia/comments/1esmv7p/roast_my_resume_please_have_11_years_of/) , 2024-08-16-0911
```
I am targeting NLP SDE, Data engineer and Data Scientist roles. Not getting any callbacks. Anything I can improve upon?


https://preview.redd.it/loqh65hrfrid1.jpg?width=2550&format=pjpg&auto=webp&s=f4c44a6e8eddf61278a7bdb5b6e20c9e5ff0bdfd



```
---

     
 
all -  [ Tool Invocation Loops in AzureChatOpenAI When Using tool_choice ](https://www.reddit.com/r/LangChain/comments/1esk29r/tool_invocation_loops_in_azurechatopenai_when/) , 2024-08-16-0911
```
I'm using AzureChatOpenAI and I'm trying to figure out how to make the Agent call a tool using `tool_choice`. I attempte
d to create an LLM binded with tools and set `tool_choice` to 'required,' but my agent keeps entering a loop, repeatedly
 calling the tool. My prompt does include `{input}`, so if that's a potential solution, I've already tried it. How can I
 resolve this issue?

  
Also my agent is a part of the AgentExecutor.
```
---

     
 
all -  [ [FOR HIRE] I will code you almost everything in Python, for an affordable price.  ](https://www.reddit.com/r/hiring/comments/1esjo2k/for_hire_i_will_code_you_almost_everything_in/) , 2024-08-16-0911
```
Hey there! I'm Diego, 

Are you drowning in boring tasks or dreaming up with exciting projects? Let me bring some coding
 magic to the table with Python. 

With over 4 years of experience, I've worked in a variety of projects, including auto
mation, chatbots, APIs, web development, web scraping, and more!

# What can I do for you?

* **Automate the boring stuf
f**: Say goodbye to repetitive tasks!
* **Build Chatbots**: Want a digital buddy? I can make that happen.
* **Build your
 web app:** Time to build the next big thing together.
* **Grab data from websites**: Web scraping made easy.
* **Work w
ith AI**: Using cool stuff like Langchain or the Chat-GPT API.

If you believe you have something that I could do for yo
u, please place a $bid and send me the details of the project. As always, the price depends, but It's usually from 15$ t
o 20$ for simple or intermediate projects.
```
---

     
 
all -  [ SurfSense A Knowledge Graph Brain for your Web Browsing Sessions ](https://www.reddit.com/r/PythonProjects2/comments/1esimy7/surfsense_a_knowledge_graph_brain_for_your_web/) , 2024-08-16-0911
```
Well when I’m browsing the internet, I tend to save a ton of content—but remembering when and what you saved? Total brai
n freeze! ❄️ That’s where SurfSense comes in. SurfSense is like a Knowledge Graph 🧠 Brain 🧠 for anything you see on the 
World Wide Web. Now, you’ll never forget any browsing session. Easily capture your web browsing session and desired webp
age content using an easy-to-use Chrome extension. Then, ask your personal knowledge base anything about your saved cont
ent., and voilà—instant recall! 🧑‍💻🌐

The whole backend is made in FastAPI & Langchain in Python.

Do give it a try : [h
ttps://github.com/MODSetter/SurfSense](https://github.com/MODSetter/SurfSense)

and lmk what is your feedback/suggestion
s.
```
---

     
 
all -  [ [for hire] I will automate your boring tasks with Python ](https://www.reddit.com/r/Jobs4Bitcoins/comments/1esii99/for_hire_i_will_automate_your_boring_tasks_with/) , 2024-08-16-0911
```
*Log in* *Inbox* *Open email* *Download* *Copy* *Paste* *Save* *Mark as read* *Next email* *Download* *Copy* *Paste* *Sa
ve* *Mark as read* *Next email* *Repeat*

Sigh... Boring tasks... Endlessly repeating, never stopping. 

But... what if 
you could automate them? 

You know, save ten minutes a day, and in a year, you could have saved 60 hours. 

That's a lo
t of hours...
 
That's what I'm offering here, the opportunity to finally automate all the boring stuff out of your life
. 

What can I do? 

- Automate excel tasks. [$30]
- Web scrape information from websites. [$50]
- Automate tasks [$20]

- Retrieve specific information from emails [$40]
- Custom scripts [Starting at $75]

What tools I use? 

I use Python t
o code all my scripts, I know how to use several libraries, here are some:

- Playwright 
- Selenium
- Flask 
- Langchai
n
- Llama-cpp-python
- Pandas
- BeautifulSoup
- Many others...

Why me? 

I'm responsive, easy to work with, and will pr
ovide support even after the project is completed. 
 
That's it. Feel free to send me a DM with all the details, and I'l
l get back to you.


```
---

     
 
all -  [ [Hiring] [Remote] [US] - Senior AI Engineer - RAG Systems and Generative AI ](https://www.reddit.com/r/techjobs/comments/1esia31/hiring_remote_us_senior_ai_engineer_rag_systems/) , 2024-08-16-0911
```
**Job Type**: Contract

**About Us:** We seek a Senior AI Engineer with expertise in Retrieval-Augmented Generation (RAG
) systems, Generative AI, and Microsoft Azure to join our dynamic team.

**Job Description:** We are looking for a Senio
r AI Engineer to lead the development and integration of advanced AI systems focused on RAG and generative AI. This role
 will involve designing, implementing, and optimizing AI solutions that leverage large language models, vector databases
, and state-of-the-art frameworks like Langchain. The ideal candidate will have a strong background in Python and experi
ence working with Microsoft Azure and other cloud-based services.

**Key Responsibilities:**

- Lead the design and deve
lopment of a conversational RAG system that interacts with scraped data from various sources.

- Develop and integrate A
PI and website scrapers for multiple data sources.

- Implement and maintain scalable AI solutions using Microsoft Azure
 services.

- Utilize Langchain and other frameworks to enhance the capabilities of our AI systems.

- Work with vector 
databases to store and retrieve large-scale data efficiently.

- Collaborate with cross-functional teams to ensure seaml
ess integration of AI solutions into existing systems.

- Conduct testing and validation to ensure the reliability and a
ccuracy of AI models.

- Maintain confidentiality and security of all project-related information.

**Requirements:**

-
 Bachelor’s or Master’s degree in Computer Science, Engineering, or a related field.

- Proven experience in developing 
and deploying RAG systems and generative AI

solutions.

- Strong proficiency in Python and experience with AI framework
s and libraries.

- Experience with Microsoft Azure and other cloud-based services.

- Knowledge of Langchain and vector
 databases.

- Excellent problem-solving skills and the ability to work in a fast-paced environment.

- Strong communica
tion and collaboration skills.

**Preferred Qualifications:**

- Experience with website scraping and integration of mul
tiple APIs.

- Prior experience in leading AI projects from conception to deployment.

- Knowledge of secure coding prac
tices and data privacy regulations.

**How to Apply:** Interested candidates are invited to submit their resume and a co
ver letter detailing their relevant experience and why they are a good fit for this role. Please send your application t
o [ai\_engineering@techrecruit-pro.com](mailto:ai_engineering@techrecruit-pro.com)


```
---

     
 
all -  [ Passing Config to LangGraph Tool Discrepancies  ](https://www.reddit.com/r/LangChain/comments/1esdvq2/passing_config_to_langgraph_tool_discrepancies/) , 2024-08-16-0911
```
**[Solved]**: config type in tool must be of type `RunnableConfig` only. Not `RunnableConfig | None`, not `Optional[Runn
ableConfig]`. Maybe `langchain` team can modify their `_get_runnable_config_param` function to do additional checks for 
flexibility to cater for this (reasoning in comments)

# Issue

All my tools are created using BaseTool.

LangGraph docu
mentation says I can invoke the graph with a configurable and it will be accessible in the tool's _run method's config R
unnable. However, the value seems to be None.

I created an additional tool using the @tool decorator and added it to th
e tools array for the graph, and noticed that the config was actually accessible there, with the specified values.

I ev
en log the config in the different node runnables throughout the graph and see that it is present. So not sure why it is
n't showing up in the _run for the base tool.

On a phone, but it was something like this:

```
@tool
def my_tool(param1
: int, config: RunnableConfig):
    print('Config is', config, type(config))

# I get 'Config is' {...really large dict.
..}, <dict>

tools=[my_tool]
```
```
class MyTool(BaseTool):
   ...
   def _run(
        param1: int,
        param2: st
ring,
        config: RunnableConfig
    ):
        print('Config is', config, type(config))

# I get 'Config is' None, 
<NoneType>
tools=[MyTool()] #no worries, it is properly instatiated and sent to the graph.
```

I use langgraph 0.1.17 (
I forgot the correct number, but it's the last one before 0.2 due to breaking changes) but I doubt it's that, since Base
Tool is from langchain_community, of which I have the latest version.

*Edit:* I call my graph using `graph.astream_even
ts`. Not sure if that causes the difference, but including that knowledge here regardless. My BaseTool does not have a m
atching `_arun` method to go with all the async functions though, but I'm not sure that is why it does not show the conf
ig.
```
---

     
 
all -  [ AI Innovations: AnthropicAIs Claude, Googles Gemini, and More ](https://www.reddit.com/r/ai_news_by_ai/comments/1es8w3v/ai_innovations_anthropicais_claude_googles_gemini/) , 2024-08-16-0911
```





#major_players #feature #tool #release #update #api #dataset #science #opinions #event #leaders #bigtech #hardware 
#opensource #startups #vc #paper #scheduled

AnthropicAI has introduced new features for Claude, including the ability t
o customize instructions for responses within projects. Claude Pro and Team users can now organize their chats into Proj
ects, enhancing idea generation and decision-making. Projects include a 200K context window for adding relevant document
s, code, and insights. Users can ground Claude's outputs in internal knowledge, define custom instructions, and create s
ide-by-side with Claude using Artifacts. Claude Team users can share snapshots of their best conversations with Claude t
o inspire collaboration and innovation [1][2]. 







AnthropicAI has also fine-tuned their Claude 3 Haiku model in Ama
zon Bedrock, allowing customers to customize the model for specialized tasks. Fine-tuning enhances performance, reduces 
costs, ensures consistent formatting, and provides an easy-to-use API. The technique has been successfully applied to mo
derating online comments and has garnered positive feedback from companies like SK Telecom and Thomson Reuters [4][5].








Anthropic has launched a new AI assistant app called 'Claude by Anthropic' developed by Anthropic PBC. The app off
ers instant answers, collaboration on tasks, and assistance with various activities. Users can access powerful AI models
 for knowledge on different subjects. The app is free to use, with an option to upgrade to a paid Pro plan for additiona
l features [7]. The Claude Android app by Anthropic is now available for download on Google Play [6].







Anthropic i
s expanding their bug bounty program to focus on finding universal jailbreaks in their next-generation safety system. Th
ey are offering rewards for novel vulnerabilities across various domains, including cybersecurity [10]. 







Mistral 
AI has released several new models including Mathstral, Codestral Mamba, and Mistral NeMo. These models specialize in ad
vanced mathematical problems, architecture research, and multilingual applications respectively [12][13][14]. Mistral AI
 also announced advancements in language models for software development, including simpler model customization, an alph
a release of Agents for creating custom behavior, and a stable version of their client SDK [15].







Google has intro
duced Gemini, which is considered the biggest advancement since the launch of Google Assistant. Gemini models enable mor
e natural communication by better understanding words and intent. Users can receive personalized help across Google's ap
ps with their permission [19]. Google's AI assistant, Gemini, is being developed for Android in 45 languages across over
 200 countries and territories [20]. Google has also introduced the Tensor G4 chip, which is their fastest and most powe
rful chip yet, developed in collaboration with Google DeepMind for Pixel devices [22].







Groq Inc is hiring ambitio
us individuals to work on their LLM inference solution. The company is looking for individuals to help take their techno
logy to the next level and change the world [28]. 







Financial institutions are using data analytics and generative
 AI for trading strategies and risk management in capital markets [33]. 







NVIDIA and LangChain held a Generative A
I Agents Developer Contest, with top prize winners including Agents of Inference, V-AI Personal Trainer, and Mystery Man
or [35]. 







Encord has raised $30 million in Series B funding to invest in the future of multimodal AI data develop
ment. The company aims to be the final AI data platform a company ever needs, with a focus on improving model performanc
e and reducing costs for customers [40].







Capsule is an interactive app that uses computer vision and generative A
I to help users find and buy products from any social media platform by snapping a screenshot [41].







Dimely, a Y C
ombinator's S24 startup, is an AI copilot for billing teams that automates manual workflows, saving teams hundreds of ho
urs monthly [42].







Yann LeCun discusses the limitations of auto-regressive language models (AR-LLMs) in innovation
 and problem-solving. He points out that while hallucinations and stochastic generation can create new content, it may n
ot always be useful or accurate [53].




[1. Anthropic @AnthropicAI https://twitter.com/AnthropicAI/status/180561673171
4453826](https://twitter.com/AnthropicAI/status/1805616731714453826)

[2. Anthropic @AnthropicAI https://twitter.com/Ant
hropicAI/status/1805616734998544891](https://twitter.com/AnthropicAI/status/1805616734998544891)

[3. Anthropic @Anthrop
icAI https://twitter.com/AnthropicAI/status/1805616841789682000](https://twitter.com/AnthropicAI/status/1805616841789682
000)

[4. Anthropic @AnthropicAI https://twitter.com/AnthropicAI/status/1811084348692517323](https://twitter.com/Anthrop
icAI/status/1811084348692517323)

[5. Anthropic @AnthropicAI https://twitter.com/AnthropicAI/status/1811084350156320820]
(https://twitter.com/AnthropicAI/status/1811084350156320820)

[6. Anthropic @AnthropicAI https://twitter.com/AnthropicAI
/status/1813237754081251573](https://twitter.com/AnthropicAI/status/1813237754081251573)

[7. Anthropic @AnthropicAI htt
ps://twitter.com/AnthropicAI/status/1813241344573284491](https://twitter.com/AnthropicAI/status/1813241344573284491)

[8
. Anthropic @AnthropicAI https://twitter.com/AnthropicAI/status/1818985491271725488](https://twitter.com/AnthropicAI/sta
tus/1818985491271725488)

[9. Anthropic @AnthropicAI https://twitter.com/AnthropicAI/status/1819437715164713225](https:/
/twitter.com/AnthropicAI/status/1819437715164713225)

[10. Anthropic @AnthropicAI https://twitter.com/AnthropicAI/status
/1821533729765913011](https://twitter.com/AnthropicAI/status/1821533729765913011)

[11. Mistral AI @MistralAI https://tw
itter.com/MistralAI/status/1777872671709057307](https://twitter.com/MistralAI/status/1777872671709057307)

[12. Mistral 
AI @MistralAI https://twitter.com/MistralAI/status/1813222156265791531](https://twitter.com/MistralAI/status/18132221562
65791531)

[13. Mistral AI @MistralAI https://twitter.com/MistralAI/status/1813947930455499200](https://twitter.com/Mist
ralAI/status/1813947930455499200)

[14. Mistral AI @MistralAI https://twitter.com/MistralAI/status/1816133332582703547](
https://twitter.com/MistralAI/status/1816133332582703547)

[15. Mistral AI @MistralAI https://twitter.com/MistralAI/stat
us/1821251862554681828](https://twitter.com/MistralAI/status/1821251862554681828)

[16. Andrew Ng @AndrewYNg https://twi
tter.com/AndrewYNg/status/1823388325409140946](https://twitter.com/AndrewYNg/status/1823388325409140946)

[17. OpenAI @o
penai https://twitter.com/openai/status/1823404955933548818](https://twitter.com/openai/status/1823404955933548818)

[18
. Sundar Pichai @sundarpichai https://twitter.com/sundarpichai/status/1823408796565418040](https://twitter.com/sundarpic
hai/status/1823408796565418040)

[19. Google @google https://twitter.com/google/status/1823406418294194687](https://twit
ter.com/google/status/1823406418294194687)

[20. Google @google https://twitter.com/google/status/1823406999033274588](h
ttps://twitter.com/google/status/1823406999033274588)

[21. Google @google https://twitter.com/google/status/18234114148
34241753](https://twitter.com/google/status/1823411414834241753)

[22. Google @google https://twitter.com/google/status/
1823411698113335562](https://twitter.com/google/status/1823411698113335562)

[23. Google @google https://twitter.com/goo
gle/status/1823413757537644671](https://twitter.com/google/status/1823413757537644671)

[24. Google @google https://twit
ter.com/google/status/1823424424009150468](https://twitter.com/google/status/1823424424009150468)

[25. Google @google h
ttps://twitter.com/google/status/1823716797947756939](https://twitter.com/google/status/1823716797947756939)

[26. Groq 
Inc @GroqInc https://twitter.com/GroqInc/status/1823403817490334188](https://twitter.com/GroqInc/status/1823403817490334
188)

[27. Groq Inc @GroqInc https://twitter.com/GroqInc/status/1823404373072056542](https://twitter.com/GroqInc/status/
1823404373072056542)

[28. Groq Inc @GroqInc https://twitter.com/GroqInc/status/1823420810280808519](https://twitter.com
/GroqInc/status/1823420810280808519)

[29. Groq Inc @GroqInc https://twitter.com/GroqInc/status/1823711926834143370](htt
ps://twitter.com/GroqInc/status/1823711926834143370)

[30. Andrej Karpathy @karpathy https://twitter.com/karpathy/status
/1823418177197646104](https://twitter.com/karpathy/status/1823418177197646104)

[31. Andrej Karpathy @karpathy https://t
witter.com/karpathy/status/1823420863297028464](https://twitter.com/karpathy/status/1823420863297028464)

[32. Andrej Ka
rpathy @karpathy https://twitter.com/karpathy/status/1823422092035154432](https://twitter.com/karpathy/status/1823422092
035154432)

[33. NVIDIA AI @NVIDIAAI https://twitter.com/NVIDIAAI/status/1823421550940344598](https://twitter.com/NVIDIA
AI/status/1823421550940344598)

[34. NVIDIA AI Developer @NVIDIAAIDev https://twitter.com/NVIDIAAIDev/status/18234116579
73887195](https://twitter.com/NVIDIAAIDev/status/1823411657973887195)

[35. NVIDIA AI Developer @NVIDIAAIDev https://twi
tter.com/NVIDIAAIDev/status/1823423501774340606](https://twitter.com/NVIDIAAIDev/status/1823423501774340606)

[36. NVIDI
A AI Developer @NVIDIAAIDev https://twitter.com/NVIDIAAIDev/status/1823449446878740910](https://twitter.com/NVIDIAAIDev/
status/1823449446878740910)

[37. cohere @cohere https://twitter.com/cohere/status/1823438828201529491](https://twitter.
com/cohere/status/1823438828201529491)

[38. cohere @cohere https://twitter.com/cohere/status/1823444835631817072](https
://twitter.com/cohere/status/1823444835631817072)

[39. Y Combinator @ycombinator https://twitter.com/ycombinator/status
/1823404146680381830](https://twitter.com/ycombinator/status/1823404146680381830)

[40. Y Combinator @ycombinator https:
//twitter.com/ycombinator/status/1823436934842388830](https://twitter.com/ycombinator/status/1823436934842388830)

[41. 
Y Combinator @ycombinator https://twitter.com/ycombinator/status/1823453219114172421](https://twitter.com/ycombinator/st
atus/1823453219114172421)

[42. Y Combinator @ycombinator https://twitter.com/ycombinator/status/1823736346344874293](ht
tps://twitter.com/ycombinator/status/1823736346344874293)

[43. Google AI @googleai https://twitter.com/googleai/status/
1823447342600872206](https://twitter.com/googleai/status/1823447342600872206)

[44. a16z @a16z https://twitter.com/a16z/
status/1823532409964691497](https://twitter.com/a16z/status/1823532409964691497)

[45. a16z @a16z https://twitter.com/a1
6z/status/1823532413236199918](https://twitter.com/a16z/status/1823532413236199918)

[46. a16z @a16z https://twitter.com
/a16z/status/1823532414863598003](https://twitter.com/a16z/status/1823532414863598003)

[47. a16z @a16z https://twitter.
com/a16z/status/1823532416692314284](https://twitter.com/a16z/status/1823532416692314284)

[48. xAI @xai https://twitter
.com/xai/status/1823597788573098215](https://twitter.com/xai/status/1823597788573098215)

[49. Yann LeCun @ylecun https:
//twitter.com/ylecun/status/1823412785545666942](https://twitter.com/ylecun/status/1823412785545666942)

[50. Yann LeCun
 @ylecun https://twitter.com/ylecun/status/1823456514398458266](https://twitter.com/ylecun/status/1823456514398458266)


[51. Yann LeCun @ylecun https://twitter.com/ylecun/status/1823466302163325388](https://twitter.com/ylecun/status/1823466
302163325388)

[52. Yann LeCun @ylecun https://twitter.com/ylecun/status/1823621547862499757](https://twitter.com/ylecun
/status/1823621547862499757)

[53. Yann LeCun @ylecun https://twitter.com/ylecun/status/1823628775868752211](https://twi
tter.com/ylecun/status/1823628775868752211)

[54. Yann LeCun @ylecun https://twitter.com/ylecun/status/18236580574710622
18](https://twitter.com/ylecun/status/1823658057471062218)

[55. Yann LeCun @ylecun https://twitter.com/ylecun/status/18
23674931051180307](https://twitter.com/ylecun/status/1823674931051180307)

[56. Yann LeCun @ylecun https://twitter.com/y
lecun/status/1823675204243218723](https://twitter.com/ylecun/status/1823675204243218723)

[57. Yann LeCun @ylecun https:
//twitter.com/ylecun/status/1823675987441103227](https://twitter.com/ylecun/status/1823675987441103227)
```
---

     
 
all -  [ Which software tools and models for processing invoice PDFs? ](https://www.reddit.com/r/LocalLLM/comments/1es8s6o/which_software_tools_and_models_for_processing/) , 2024-08-16-0911
```
I'm just taking my first steps with AI. Please be considerate of me.
I am currently trying to build an application that 
allows me to read invoices in PDF format and output them in structured JSON. I am interested in all the details of the i
nvoice, such as sender, recipient, service date, invoice date, invoice number, each individual invoice item and so on.


In any case, I want to run the project *completely locally*, i.e. not integrate any third-party providers (currently I c
an only run it on the CPU, a more powerful graphics card will be added later). The invoice PDF is to be processed via RA
G.

My first question now is which software and which models are basically of interest to me here. I was thinking of Lan
gchain with Ollama and FAISS/Chroma, and possibly unstructured.io to prepare PDFs beforehand. I would possibly use Strea
mlit for a GUI.

Which language model would be suitable for me? Mistral? Can anyone give me tips on which tools and mode
ls are suitable?
```
---

     
 
all -  [ Portkey Gateway - An open-source AI Gateway with integrated Guardrails ](https://www.reddit.com/r/LangChain/comments/1es7gw5/portkey_gateway_an_opensource_ai_gateway_with/) , 2024-08-16-0911
```
We've been developing Portkey Gateway, an open-source AI gateway that's now processing billions of tokens daily across 2
00+ LLMs. Today, we're launching a significant update: integrated Guardrails at the gateway level.

Key technical featur
es:

Guardrails as middleware: We've implemented a hooks architecture that allows guardrails to act as middleware in the
 request/response flow. This enables real-time LLM output evaluation and transformation.

Flexible orchestration: The ga
teway can now route requests based on guardrail verdicts. This allows for complex logic like fallbacks to different mode
ls or prompts based on output quality.

Plugin system: We've designed a modular plugin system that allows integration of
 various guardrail implementations (e.g., guardrails ai, microsoft/guidance, vectara/hallucination-detection).

Stateles
s design: The guardrails implementation maintains the gateway's stateless nature, ensuring scalability and allowing for 
easy horizontal scaling.

Unified API: Despite the added complexity, we've maintained our unified API across different L
LM providers, now extended to include guardrail configurations.

Performance impact: Latency increase is minimal (<20ms)
 for most guardrails, and even lesser for deterministic guardrails like regex match, json schema check, etc.

Challenges
 we're still tackling:

Standardizing evaluation metrics across different types of guardrails

Handling guardrail false 
positives/negatives effectively

We believe this approach of integrating guardrails at the gateway level provides a powe
rful tool for managing LLM behavior in production environments.

The code is open-source, and we welcome contributions a
nd feedback.

We're particularly interested in hearing about specific use cases or challenges you've faced in implementi
ng reliable LLM systems.

Detailed note: [https://portkey.wiki/guardrail](https://portkey.wiki/guardrail)

What are your
 thoughts on this approach? Are there specific guardrail implementations or orchestration patterns you'd like to see add
ed?
```
---

     
 
all -  [ [OpenSource] Created this library for making finite state machine based agents ](https://www.reddit.com/r/OpenAIDev/comments/1es6mpy/opensource_created_this_library_for_making_finite/) , 2024-08-16-0911
```
Not another langchain or 'bla bla bla of give me tools and prompt and I create your agent' library, but instead an autom
aton based approach.. basically you define set of states and possible transitions, each state has it's own system prompt
 and its own instructions...

Check it out now! - [https://github.com/searchX/moorellm](https://github.com/searchX/moore
llm)

Also, since it is using latest structured responses from openai, so it will always 100% give correct format (bewar
e of quality XD)
```
---

     
 
all -  [ Why are you using RAG? ](https://www.reddit.com/r/LangChain/comments/1es4lh3/why_are_you_using_rag/) , 2024-08-16-0911
```
I'm building in the AI space, and I'm really curious what the most popular (and the most creative) use cases for RAG are
.

What are you building that requires RAG? How have you found the experience? Is anybody using RAG for something very u
nexpected?
```
---

     
 
all -  [ What is the difference Webvoiger and an Agent with PlayRight as a tool? ](https://www.reddit.com/r/LangChain/comments/1es3ea2/what_is_the_difference_webvoiger_and_an_agent/) , 2024-08-16-0911
```
We see Webvoiger can browse a web which can be done easily with an Agent with Playright as a tool. What could be the dif
ference between these two implementations in terms of capability of intelligent web browsing?
```
---

     
 
all -  [ Can Langchain Query Multiple Datasources? ](https://www.reddit.com/r/LangChain/comments/1es32w3/can_langchain_query_multiple_datasources/) , 2024-08-16-0911
```
Hi all,

I am quite new to Langchain but I am trying to develop a chatbot that can query multiple databases of different
 types and sources (sql database, webscraped data, etc.).

Ideally, I would also like the different sources to be able t
o 'collaborate' with each other? Since I am working with webscraped news data, it would be nice to have the data in my s
ql database to interact with the news data. But perhaps that is really not possible, please let me know. I would be happ
y enough if it can switch and identify the right source.


```
---

     
 
all -  [ (Profile Review) Looking for honest review of my profile ](https://i.redd.it/o01k3kdy1nid1.jpeg) , 2024-08-16-0911
```
Can
```
---

     
 
all -  [ Filtering before similarity search in Faiss ](https://www.reddit.com/r/LangChain/comments/1erz8b9/filtering_before_similarity_search_in_faiss/) , 2024-08-16-0911
```
I have a project that requires filtering before search. I initially used DeepLake, but I noticed it was slow, so I switc
hed to Faiss. However, I'm facing an issue where the `similarity_search` function performs the similarity search first a
nd then applies filtering. Is there a way to reverse this order, so filtering happens before the similarity search?
```
---

     
 
all -  [ Integrating Multimodal RAG with Google Gemini 1.5 Flash and Pathway ](https://www.reddit.com/r/LangChain/comments/1erz1ww/integrating_multimodal_rag_with_google_gemini_15/) , 2024-08-16-0911
```
Hey everyone, I wanted to share a new app template that goes beyond traditional OCR by effectively extracting and parsin
g visual elements like images, diagrams, schemas, and tables from PDFs using Vision Language Models (VLMs). This setup l
everages the power of Google Gemini 1.5 Flash within the Pathway ecosystem.

👉 Check out the full article and code here:
 [https://pathway.com/developers/templates/gemini-multimodal-rag](https://pathway.com/developers/templates/gemini-multim
odal-rag)  
  
**Why Google Gemini 1.5 Flash?**  
– It’s a key part of the GCP stack widely used within the Pathway and 
broader LLM community.  
– It features a 1 million token context window and advanced multimodal reasoning capabilities. 
 
– New users and young developers can access up to $300 in free Google Cloud credits, which is great for experimenting 
with Gemini models and other GCP services.

**Does Gemini Flash’s 1M context window make RAG obsolete?**  
Some might ar
gue that the extensive context window could reduce the need for RAG, but the truth is, RAG remains essential for curatin
g and optimizing the context provided to the model, ensuring relevance and accuracy.

For those interested in understand
ing the role of RAG with the Gemini LLM suite, this template covers it all.  
  
To help you dive in, we’ve put together
 a detailed, step-by-step guide with code and configurations for setting up your own Multimodal RAG application. Hope yo
u find it useful!
```
---

     
 
all -  [ Claude keeps repeating sentences like 'Based on the articles' in the answer ](https://www.reddit.com/r/ClaudeAI/comments/1eryikm/claude_keeps_repeating_sentences_like_based_on/) , 2024-08-16-0911
```
I am using Claude Haiku via Amazon Bedrock and Langchain (ChatBedrock API) to create a simple RAG chatbot. 

The problem
 I'm facing is that the model keeps repeating sentences like 'Based on the articles' in the answer.  
My goal is to not 
mention that the answer is based on the articles. 

I've tried to add explicit rules that deny this type of behaviour an
d provided examples without luck. 

For reference, this is the prompt template I am using:

'''  
You are a customer sup
port bot. Your goal is to answer customer queries by strictly adhering to the information obtained verbatim from the art
icles provided below. The customer question is wrapped in the <question></question> XML tags, while the articles are wra
pped in the <articles></articles> XML tags. 

<question>  
{question}  
</question>

<articles>  
{context}  
</articles
>

Follow these rules:  
- NEVER reference the word 'article' in the answer. For instance, never write: “Based on the in
formation provided”, 'According to the articles', 'According to the information provided' or 'The articles state'.  
- I
f there is no relevant information in articles, write “No relevant information” instead.   
- Answer the question, start
ing with “Answer:“  
- Do not rely on internal knowledge or make speculative predictions to answer questions. Do not hal
lucinate.  
- Write only information that answers the question, without any extra non-relevant information.  
'''

  
Ha
s anyone got the same behaviour?
```
---

     
 
all -  [ A guide to understand Semantic Splitting for document chunking in LLM applications ](https://www.reddit.com/r/LangChain/comments/1erxo60/a_guide_to_understand_semantic_splitting_for/) , 2024-08-16-0911
```
Hey everyone,

Today, I want to share an in-depth guide on semantic splitting, a powerful technique for chunking documen
ts in language model applications. This method is particularly valuable for retrieval augmented generation (RAG)

🎥 I ha
ve a YT video with a hands on Python implementation if you're interested check it out: [https://youtu.be/qvDbOYz6U24](ht
tps://youtu.be/qvDbOYz6U24)

# The Challenge with Large Language Models

Large Language Models (LLMs) face two significa
nt limitations:

1. **Knowledge Cutoff**: LLMs only know information from their training data, making it challenging to 
work with up-to-date or specialized information.
2. **Context Limitations**: LLMs have a maximum input size, making it d
ifficult to process long documents directly.

# Retrieval Augmented Generation

To address these limitations, we use a t
echnique called Retrieval Augmented Generation:

1. Split long documents into smaller chunks
2. Store these chunks in a 
database
3. When a query comes in, find the most relevant chunks
4. Combine the query with these relevant chunks
5. Feed
 this combined input to the LLM for processing

The key to making this work effectively lies in how we split the documen
ts. This is where semantic splitting shines.

# Understanding Semantic Splitting

Unlike traditional methods that split 
documents based on arbitrary rules (like character count or sentence number), semantic splitting aims to chunk documents
 based on meaning or topics.

**The Sliding Window Technique**

1. Here's how semantic splitting works using a sliding w
indow approach:
2. Start with a window that covers a portion of your document (e.g., 6 sentences).
3. Divide this window
 into two halves.
4. Generate embeddings (vector representations) for each half.
5. Calculate the divergence between the
se embeddings.
6. Move the window forward by one sentence and repeat steps 2-4.
7. Continue this process until you've co
vered the entire document.

The divergence between embeddings tells us how different the topics in the two halves are. A
 high divergence suggests a significant change in topic, indicating a good place to split the document.

**Visualizing t
he Results**

If we plot the divergence against the window position, we typically see peaks where major topic shifts occ
ur. These peaks represent optimal splitting points.

**Automatic Peak Detection**

To automate the process of finding sp
lit points:

1. Calculate the maximum divergence in your data.
2. Set a threshold (e.g., 80% of the maximum divergence).

3. Use a peak detection algorithm to find all peaks above this threshold.

These detected peaks become your automatic s
plit points.

# A Practical Example

Let's consider a document that interleaves sections from two Wikipedia pages: 'Fran
cis I of France' and 'Linear Algebra'. These topics are vastly different, which should result in clear divergence peaks 
where the topics switch.

1. Split the entire document into sentences.
2. Apply the sliding window technique.
3. Calcula
te embeddings and divergences.
4. Plot the results and detect peaks.

You should see clear peaks where the document swit
ches between historical and mathematical content.

# Benefits of Semantic Splitting

1. Creates more meaningful chunks b
ased on actual content rather than arbitrary rules.
2. Improves the relevance of retrieved chunks in retrieval augmented
 generation.
3. Adapts to the natural structure of the document, regardless of formatting or length.

# Implementing Sem
antic Splitting

To implement this in practice, you'll need:

1. A method to split text into sentences.
2. An embedding 
model (e.g., from OpenAI or a local alternative).
3. A function to calculate divergence between embeddings.
4. A peak de
tection algorithm.

# Conclusion

By creating more meaningful chunks, **Semantic Splitting** can significantly improve t
he performance of retrieval augmented generation systems.

I encourage you to experiment with this technique in your own
 projects.

It's particularly useful for applications dealing with long, diverse documents or frequently updated informa
tion.
```
---

     
 
all -  [ How strong is the moat of Vector DB?  ](https://www.reddit.com/r/LangChain/comments/1erxdp0/how_strong_is_the_moat_of_vector_db/) , 2024-08-16-0911
```
Hey community!  
I recently saw a post on LinkedIn, that with time the moat of VectorDB will vanish if classic DB such a
s Mongo / Postgres DB also are Vector DB (which they already do support through extensions today). Hence will Vector DB 
(Qdrant, Pinecone, and Weaviate) become obsolete? What is your take on that? 
```
---

     
 
MachineLearning -  [ [P] using GPT4o with langchain/chroma for sports analysis  ](https://www.reddit.com/r/MachineLearning/comments/1enuzlp/p_using_gpt4o_with_langchainchroma_for_sports/) , 2024-08-16-0911
```
Hi all, I'm working on a side project that helps with sports analysis for historical games, which in turn will help with
 sports betting. Currently I've been only focused on MLB because I wanted to see how the use case would pan out.

My fir
st attempt at this was to use the openai endpoint and load all the relevant JSON objects and send a prompt along with th
em to GPT and see what I get back. Eventually, the context size was getting way too big and the problem I was running in
to was that it was expensive. Although, the prompts back were actually pretty decent and relevant to the data.

My secon
d attempt was to setup a RAG using Chroma/LangChain/GPT4o. I got it to work but the answers all seem very off and super 
vague. None of the data I have was shown in any of the prompts i asked, or any of the players that were playing in a gam
e were mentioned at all in the prompt back, plus it kept mentioning wrong games/teams whe asking it specific games. I’m 
assuming I might need to adjust the vector store a bit but not sure how I can do that with chroma.

My question is what 
might be the best way to setup some sort of process? My end result, I would like a response back using the historical da
ta I've provided to make assumptions on what a game could be like based off all the stats given, with some room for GPT 
to also make some inference as well.

I am a super new at this so it's been a learning process so far; please bear with 
me.
```
---

     
 
MachineLearning -  [ [R] [D] Langchain Evaluation with BeyondLLM
 ](https://www.reddit.com/r/MachineLearning/comments/1eki1fv/r_d_langchain_evaluation_with_beyondllm/) , 2024-08-16-0911
```
Hey everyone! Just came across a new feature of Beyond LLM that can evaluate Langchain RAG pipelines! It provides contex
t relevancy, answer relevancy, and groundedness. Check out the code snippet I’m sharing—perfect for testing your RAG pip
elines! For more info, be sure to check it out on GitHub [here](https://github.com/aiplanethub/beyondllm/blob/main/cookb
ook/evaluate_langchain_rag_pipeline_beyondllm.ipynb).

https://preview.redd.it/172m1y3dvsgd1.png?width=3972&format=png&a
uto=webp&s=63d5b0f41f0e46a58e7a2d5fb0d2bbc4384b3b1d


```
---

     
 
MachineLearning -  [ [D] Embedding generation in production? How are you doing it? ](https://www.reddit.com/r/MachineLearning/comments/1e7xt6k/d_embedding_generation_in_production_how_are_you/) , 2024-08-16-0911
```


For those building production RAG pipelines, how are you generating embeddings. More than which model, I'm interested 
in how your deploying it. Are you calling the openai/vertex API endpoint directly? Using langchain/llamaindex wrappers? 
Using vectordb  classes? Or some other way?
```
---

     
 
deeplearning -  [ How To Build Your Retrieval Augmented Generation (RAG) Using Open-source Tools: LangChain, LLAMA 3,  ](https://www.reddit.com/r/deeplearning/comments/1emdotx/how_to_build_your_retrieval_augmented_generation/) , 2024-08-16-0911
```


TL;DR: RAG overcomes the limitations of LLMs by bringing in external sources of information as relevant context.  
  

At the end of the step-by-step tutorial, you will be able to give your favorite LLM (ChatGPT, LLAMA 3, Mixtral, Gemini, 
Claude, etc.) some documents, ask it a question and see it respond based on relevant context.  
  
This will be running 
locally, using open-source libraries. Zero API and tooling costs.

[Step-by-step Notebook with zero-cost RAG](https://co
decompass00.substack.com/p/build-open-source-rag-langchain-llm-llama-chroma)

![img](69v6kjfj3wgd1)


```
---

     
 
deeplearning -  [ Need help with creating CLI for 'non-programmers' (LLMs) ](https://www.reddit.com/r/deeplearning/comments/1elrfgm/need_help_with_creating_cli_for_nonprogrammers/) , 2024-08-16-0911
```
***TL;DR*** What is the best way to convert user input into sequence of commands and their corresponding parameters? Lik
e, imagine you are not a programmer and there is a console app with a CLI, but, well, you don't know the structure and t
he syntax of commands. And you don't want to know. YBut! You have a locally running instance of llama3.1 -- or whatever 
open LLM is out there now -- and you can ask it to create a CLI command for you. What would you do to accomplish that?


**Intro**

A little bit of context. I'm working on a project that targets scientists as end users. It has some UI using 
which it's possible to do all sort of things the lab workers would like to do. But recently the projects product owner d
ecided that it would be cool to have a small chat window that is accessable basically everywhere throughout the applicat
ion UI in which 'lives' a bot that can accept some input from a user and do what is requested. The pool of commands is f
inite and predefined.

**The issue**

So, putting details aside, the main issue to be solved is parsing user input (unst
ructured and possible incomplete data) to some structured form. In general, each and every user input should be transfor
med into a data structure that represents a sequence of commands with their parameters, for example:

User input: Please
, create X with param1 set to value1 and param2 equal to value2

Desired output:

    create_x --param1 value1 --param2 
value2

In this example, there is only one command, but in real life the request can represent a sequence of N commands,
 and they may depend on each other (sequence of execution does matter)

**What I've tried so far**

I have an 'experimen
t' environment: a python project with `ollama` and `langchain` installed. The main model I test is llama3.1-instruct wit
h 5bit quantization. (I'm sort of limited with hardware resourses, so XXB parameter models do not fit).

Up until now, I
've tried to achieve what I want with prompting in different forms, but in general I do the following:

1. As the very f
irst message in the chat, I create a 'system' one which explain what commands are there. The format is the following (I 
replaced original data not to expose the context more, so it's very generic): 

```xml
<scope>
    <models>
        <mod
el name='entityA'>
            <field name='uniqueId' type='string' description='unique identifier for entityA'/>
      
      <field name='label' type='string' description='label for entityA'/>
            <field name='category' type='enum'
 possible-value='alpha, beta, gamma, delta'/>
        </model>
        <model name='entityB'>
            <field name='u
niqueId' description='unique identifier for entityB'/>
            <field name='entityAIds' type='array' description='id
entifiers of entityAs associated with this entityB'/>
        </model>
    </models>
    <commands>
        <command nam
e='create_entityA' description='creates an instance of entityA'>
            <param name='uniqueId' type='string' descri
ption='unique identifier for entityA'/>
            <param name='label' type='string' description='label for entityA' re
quired='true'/>
            <param name='category' type='enum' possible-values='alpha, beta, gamma, delta'
             
      description='category of entityA (one value from the possible values list)' required='true'/>
        </command>
 
       <command name='remove_entityA' description='removes an instance of entityA by its unique identifier'>
           
 <param name='uniqueId' description='unique identifier of the entityA to be removed'
                   required='true'/
>
        </command>
        <command name='create_entityB'>
            <param name='label' description='label for enti
tyB'/>
        </command>
        <command name='link_entityAs_to_entityB'
                 description='associates inst
ances of entityA with a specific entityB based on the provided unique identifier of entityB'>
            <param name='u
niqueId' description='unique identifier of the entityB to which entityAs should be associated'
                   requir
ed='true'/>
            <param name='entityAIds'
                   description='an array of unique identifiers of entit
yAs to associate with the entityB'
                   type='array'
                   required='true'/>
        </comman
d>
        <command name='navigate' description='indicates that a user wants to go to a specific section of the platform
'>
            <param name='section' possible-values='entitiesA, entitiesB, configuration' required='true'/>
        </c
ommand>
        <command name='support' description='should be executed when a user seeks assistance on available functi
ons'/>
    </commands>
</scope>
```

So, now the model is provided with some context. Then, also in the 'system' message
 I:

* 'tell' the model that user input should be converted into a sequence of commands along with the corresponding par
ameters, all of this is described in the XML above
* describe the desired output format
* try to enforce some restrictio
n and cover edge cases

**The question part**

*Is this approach* ***viable***\*?\*

If yes, maybe there are some ***way
s to improve it***?

If not, *what would be* ***the alternative***?

So far I don't see how to apply fine tuning here

T
hank you in advance!
```
---

     
