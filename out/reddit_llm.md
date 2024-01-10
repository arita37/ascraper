 
all -  [ Applied to 100+ SWE internships with very few interviews ](https://www.reddit.com/r/resumes/comments/192u489/applied_to_100_swe_internships_with_very_few/) , 2024-01-10-0910
```
Hey everyone - 

I've applied to 100 + SWE internships (career switcher, international student) with practically no OAs.


What's wrong with my CV, and what can I do to improve it?

&#x200B;

https://preview.redd.it/6k80xpv68ibc1.jpg?width=2
545&format=pjpg&auto=webp&s=5bdc3886faa07300f783d7f8fd7512e73b9a4c95
```
---

     
 
all -  [ Nextjs + LangChain + Supabase template to build AI apps ](https://templateai.co) , 2024-01-10-0910
```

```
---

     
 
all -  [ Next.js starter for building AI apps (image and text gen, vector search) ](https://www.reddit.com/r/nextjs/comments/192ssyg/nextjs_starter_for_building_ai_apps_image_and/) , 2024-01-10-0910
```
Hey Next.js community,

I created a starter template to help developers build full-stack apps with AI features: image ge
neration, text generation, vector search and more.

It's built on Next.js + Tailwind for the front-end. Supports Supabas
e for database and authentication, and Stripe for payments. Also comes with built-in components for a landing page and d
ashboard.

For the AI integrations, I use Replicate for image gen, gpt-3.5 for text gen, Supapase pgvector as the vector
 store, and LangChain for LLM management.

I've put up the template along with tons of documentation and videos here: [h
ttps://templateai.co/](https://templateai.co/)

Hope you all find it useful. Cheers.

&#x200B;
```
---

     
 
all -  [ What LLM orchestration am I thinking about? ](https://www.reddit.com/r/ArtificialInteligence/comments/192p9cq/what_llm_orchestration_am_i_thinking_about/) , 2024-01-10-0910
```
Hi everyone,  
A few months ago I was playing around with a bunch of different tools to manage integrations and LLMs. I 
randomly found a website, where within the UI I was able to:  
\- Provide a prompt for a complex task (e.g. build app th
at does XYZ)  
\- It broke it down into subtasks (e.g. choose data schemas, create frontend...etc)  
\- It then started 
working on each subtasks and finding new ones as it completed each one  
I was blown away but then needing to do my rese
arch took me somewhere else. I now have time to invest more time in this venture but can't find it for the life of me. I
 think it was based on LangChain or AutoGPT but I've been searching for hours and can't find it so trying my luck here :
)  
Anyone know what this is or uses it?
```
---

     
 
all -  [ What LLM orchestration tool am I thinking about? ](https://www.reddit.com/r/LangChain/comments/192p8lz/what_llm_orchestration_tool_am_i_thinking_about/) , 2024-01-10-0910
```
Hi everyone,  


A few months ago I was playing around with a bunch of different tools to manage integrations and LLMs. 
I randomly found a website, where within the UI I was able to:

\- Provide a prompt for a complex task (e.g. build app t
hat does XYZ)

\- It broke it down into subtasks (e.g. choose data schemas, create frontend...etc)

\- It then started w
orking on each subtasks and finding new ones as it completed each one

&#x200B;

I was blown away but then needing to do
 my research took me somewhere else. I now have time to invest more time in this venture but can't find it for the life 
of me. I think it was based on LangChain or AutoGPT but I've been searching for hours and can't find it so trying my luc
k here :)

Anyone know what this is or uses it?
```
---

     
 
all -  [ I have been unable to get an interview with any of the top companies like MAANG and others. ](https://www.reddit.com/r/resumes/comments/192p0p7/i_have_been_unable_to_get_an_interview_with_any/) , 2024-01-10-0910
```
I am looking out Data Scientist roles involving NLP and LLMS. I really need feedback on what I might be missing on my re
sume.

https://preview.redd.it/tfrtl27d8hbc1.png?width=820&format=png&auto=webp&s=c3ac18ecb31fb091811a86549dcf0dee110c34
1e
```
---

     
 
all -  [ Is LangChain needed/ideal for a chatbot? ](https://www.reddit.com/r/LangChain/comments/192oom1/is_langchain_neededideal_for_a_chatbot/) , 2024-01-10-0910
```
I'm working on creating a chatbot for some long research papers of mine (using RAG). While I'd like the ability to answe
r both summary questions, e.g. 'What's paper x all about?', I also want the chatbot to answer specific questions. This n
eed speaks to the usefulness of Agents (I think), but since I don't need to chain together a bunch of tasks, I'm wonderi
ng if LangChain is overkill?
```
---

     
 
all -  [ How to make openai tools agent store tool messages ](https://www.reddit.com/r/LangChain/comments/192kifr/how_to_make_openai_tools_agent_store_tool_messages/) , 2024-01-10-0910
```
I have the following code, memory does not store the intermediate steps in the tools calling, how can this be achieved? 
 


    def answer_langchain_v2(input, chat_token):
        memory = ConversationBufferMemory(
                memory_ke
y='chat_history', return_messages=True)
        azure_open_ai = AzureChatOpenAI(
            temperature=0,
            
max_tokens=3000,
            verbose=True,
        )
        tools = [retrieve_benchmarks, search_entities()]
        pr
ompt = hub.pull('hwchase17/openai-tools-agent')
        agent = create_openai_tools_agent(
            azure_open_ai, to
ols, prompt)
        agent_executor = AgentExecutor(
            agent=agent,
            tools=tools,
            verbo
se=True,
            handle_parsing_errors=True,
            memory=memory
        )
        output = agent_executor.inv
oke(
            {
                'input': input_schema.format(input=input),
            }
        )['output']

&#x200B
;
```
---

     
 
all -  [ Visualizing Software Complexity with a 3D Force-Directed Graph ](https://www.reddit.com/r/Python/comments/192ket2/visualizing_software_complexity_with_a_3d/) , 2024-01-10-0910
```
Hello everyone!

I want to share a project for which Python support was just added recently:

[https://github.com/gabote
chs/dep-tree](https://github.com/gabotechs/dep-tree)

This is a tool that allows users to visualize the complexity of a 
code base using a 3D force-directed graph:

* It will take a Python executable/library's entrypoint and calculate it's d
ependencies based on the import statements.
* It will recursively crawl the import statements looking for more import st
atements in the imported files, building recursively a file dependency graph.
* It will render the graph using a force-d
irected layout, and all the crawled files will be placed in a three-dimensional space simulating some attraction/repulsi
on forces based on the dependencies between them.
* There's already some samples using well known open-source projects t
hat are quite surprising:
   * [langchain](https://dep-tree-explorer.vercel.app/api?repo=https%3A%2F%2Fgithub.com%2Flang
chain-ai%2Flangchain&entrypoint=libs%2Flangchain%2Flangchain%2F__init__.py)
   * [tensorflow](https://dep-tree-explorer.
vercel.app/api?repo=https%3A%2F%2Fgithub.com%2Ftensorflow%2Ftensorflow&entrypoint=tensorflow%2Fpython%2Fkeras%2Fmodels.p
y)
   * [numpy](https://dep-tree-explorer.vercel.app/api?repo=https%3A%2F%2Fgithub.com%2Fnumpy%2Fnumpy&entrypoint=numpy%
2F__init__.py)
   * [pytorch](https://dep-tree-explorer.vercel.app/api?repo=https%3A%2F%2Fgithub.com%2Fpytorch%2Fpytorch
&entrypoint=torch%2Fnn%2F__init__.py)

I wrote a blog post about it if you want to dive deeper: [link](https://dev.to/ga
botechs/about-software-complexity-569d)

Hope you liked it!
```
---

     
 
all -  [ Best practices for uploading PDFs when type varies a lot (scanned documents, exports, tables, ...) ](https://www.reddit.com/r/LangChain/comments/192epg3/best_practices_for_uploading_pdfs_when_type/) , 2024-01-10-0910
```
We're building a web app, that allows the user to upload PDFs, which we then summarise. 

A challenge we have is that pe
ople upload very different formats of PDFs. (Word exports, flattened images, scanned documents, ...). 

In my head I was
 thinking of detecting if it has lots of big images (when it's a scan), then using a vision model over those images, and
 then summarising the outputs. If there are no images, then just extracting texts (potentially handing tables slightly d
ifferently). 

What are the best practices on ensuring all the information is extracted? In my head I was thinking of de
tecting if it has lots of big images (when it's a scan), then using a vision model over those images, and then summarisi
ng the outputs. If there are no images, then just extract texts (potentially handing tables slightly differently). 
```
---

     
 
all -  [ [Q] Is it possible to give ollama access to a local gitlab repository? ](https://www.reddit.com/r/LocalLLaMA/comments/192dz3r/q_is_it_possible_to_give_ollama_access_to_a_local/) , 2024-01-10-0910
```
I'm playing arround with https://github.com/ollama-webui/ollama-webui and I'm quite pleased with the ease of use and per
formance. I've tested it with starcoder and mistral , putting in some archives for RAG and the results are not bad, but 
was wondering if there is a way to give ollama a way to access a project inside a gitlab instance with a restricted user
 and it's password so it can access the project and answer some simple questions like 'What version of .net is this proj
ect using?'

Can this be done or is just a pipe dream? I have read some work was done some months ago with langchain for
 searching full codebases , but I was aiming at something more limited for the moment.

As a more general question , cou
ld a local model access websites I point it at ? like 'Give me a list of the new items in the local newspaper website ht
tps://www.localnews.com' for the last 2 hours ?
```
---

     
 
all -  [ I just started learning. ](https://www.reddit.com/r/LangChain/comments/192avem/i_just_started_learning/) , 2024-01-10-0910
```
What is the difference between LangChain and LangSmith? What do you think is the best way to learn this framework?
```
---

     
 
all -  [ Using local data for context ](https://www.reddit.com/r/LocalLLaMA/comments/192aasu/using_local_data_for_context/) , 2024-01-10-0910
```
Hi all, I'm looking at connecting an LLM to a folder of text documents for context. I've been investigating ChatGPT4All 
and Langchain as possible ways to achieve this, but I'm most familiar with KoboldCPP for running LLMS. I have a bot that
 interfaces with my LLM, so I'd need the end result of the LLM+documents to still have an API my bot can grab from.

Tho
se of you who have done this, do you have any tips? Any particular guides (of the million available) that are actually w
orth looking at?
```
---

     
 
all -  [ [D] Are Custom LLM RAG apps going to become redundant? ](https://www.reddit.com/r/MachineLearning/comments/1929n4f/d_are_custom_llm_rag_apps_going_to_become/) , 2024-01-10-0910
```
Loks like Copilot Studio is being rolled out (https://www.microsoft.com/en-us/microsoft-copilot/microsoft-copilot-studio
) with an impressive looking no code/out of the box RAG solution.

There is a phenomenal amount of development and activ
ity in the Open Source RAG world (e.g Langchain, Llamaindex, etc), which I am a great supporter of FYI.

However, what s
eems strange is that this no code out of the box solution (Copilot Studio - just as an example of one) seems overwhelmin
gly to be the better option if you wanted to build a RAG app i.e If you compare the cost to build and productionise a cu
stom RAG app vs the cost of using Copilot Studio, it's almost an order of magnitude lower (no matter how you cut it with
 the developer time and duration). 

My question is, it seems to me we are moving towards a situation where enterprise s
olutions will make custom RAG apps redundant (not in all cases of course, but most cases), however there seems to be ver
y little discussion of this relative to the activity in the open source community. Do people agree this is a likely scen
ario? 

Obviously there will be exceptions…but on most use cases I don’t see how you can compete with an instant/minimal
 setup, low cost, highly scalable RAG solution.
```
---

     
 
all -  [ Are there any GUI tools out there that allows you to use LLMs in this manner ](https://www.reddit.com/r/ChatGPT/comments/1922abj/are_there_any_gui_tools_out_there_that_allows_you/) , 2024-01-10-0910
```
Sorry if this is common knowledge, I’m new to using LLMs and all my experience until now has been with Chat GPT using Op
en AI’s web ui. I want to explore other language models especially some of the opensource ones like Mixtral 8B etc 

Is 
there a GUI tool I can use to keep all these models in one place? And manage things like context? For example I will hav
e seperate system
prompts for “Programmer”, “Lawyer”, “Advise giver” etc and depending on what the mood calls for I can 
select the most appropriate one? And also I can load context from memory to pick up a conversation from where I last lef
t off?

I believe Langchain can do this but it looks like it’s not really a UI but a lib you need to install and write s
cripts for. I’m ok with that cause I’m a developer by trade but I was hoping to start off with something more turn-key, 
like select this or that model from a drop-down and have all your saved context appear on the left etc in the form of a 
web or desktop app. 

Is there such a tool out there people can recommend? Thanks in advance!
```
---

     
 
all -  [ Here's how you can add AI superpowers to your C# app! ](https://www.reddit.com/r/csharp/comments/191yhnz/heres_how_you_can_add_ai_superpowers_to_your_c_app/) , 2024-01-10-0910
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

     
 
all -  [ React prompting Mistral or Mixtral ](https://www.reddit.com/r/MistralAI/comments/191wg3i/react_prompting_mistral_or_mixtral/) , 2024-01-10-0910
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

     
 
all -  [ [For Hire] Laravel and TALL Stack Wizard with Python, AI Automation, and API Integration Superpowers ](https://www.reddit.com/r/forhire/comments/191v0no/for_hire_laravel_and_tall_stack_wizard_with/) , 2024-01-10-0910
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

     
 
all -  [ has anybody used langchain tools but totally used custom logic for parsing LLM responses and invokin ](https://www.reddit.com/r/LangChain/comments/191sm46/has_anybody_used_langchain_tools_but_totally_used/) , 2024-01-10-0910
```
I like the tools but I'm not a huge fan of the default agent prompts. Just wondering if anybody has done this? 
```
---

     
 
all -  [ Opensource Practical AI Development for Javascript Developers primer! (Uses Nextjs and AI SDK for ma ](https://www.reddit.com/r/nextjs/comments/191rbv7/opensource_practical_ai_development_for/) , 2024-01-10-0910
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

     
 
all -  [ NeuralGPT - A Working Character.ai Client ](https://www.reddit.com/r/AIPsychology/comments/191r7jj/neuralgpt_a_working_characterai_client/) , 2024-01-10-0910
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

     
 
all -  [ I released a new opensource Practical AI Development for Javascript Developers course! (Heavily uses ](https://www.reddit.com/r/LangChain/comments/191r21r/i_released_a_new_opensource_practical_ai/) , 2024-01-10-0910
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

     
 
all -  [ New to LangChain? Start here! ](https://www.reddit.com/r/LangChain/comments/191q3qk/new_to_langchain_start_here/) , 2024-01-10-0910
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

     
 
all -  [ [D] Unleashing the Power of Langchain with Wandb: Revolutionizing Topic Modeling and Evaluation ](https://www.reddit.com/r/deeplearning/comments/191mm83/d_unleashing_the_power_of_langchain_with_wandb/) , 2024-01-10-0910
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

     
 
all -  [ Can you suggest some top-notch teams actively looking for exceptional machine learning engineers or  ](https://www.reddit.com/r/jobs/comments/191j5ri/can_you_suggest_some_topnotch_teams_actively/) , 2024-01-10-0910
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

     
 
all -  [ 1.5 yıl önce mezun oldum hala iş bulamıyorum, tavsiyeleriniz var mı? ](https://www.reddit.com/r/CodingTR/comments/191hmxf/15_yıl_önce_mezun_oldum_hala_iş_bulamıyorum/) , 2024-01-10-0910
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

     
 
all -  [ RAG - Responding with multiple data types ](https://www.reddit.com/r/LangChain/comments/191d8td/rag_responding_with_multiple_data_types/) , 2024-01-10-0910
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

     
 
all -  [ Can someone please help me understand why this document lookup app can't remember previous questions ](https://www.reddit.com/r/LangChain/comments/191bsyn/can_someone_please_help_me_understand_why_this/) , 2024-01-10-0910
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

     
 
all -  [ Please teach me how to get relevant vector store results ](https://www.reddit.com/r/LangChain/comments/191b6is/please_teach_me_how_to_get_relevant_vector_store/) , 2024-01-10-0910
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

     
 
all -  [ How to use Output parser with ConversationalRetrievalQAChain? ](https://www.reddit.com/r/LangChain/comments/191b28p/how_to_use_output_parser_with/) , 2024-01-10-0910
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

     
 
all -  [ Summary Generation on large CSV files ](https://www.reddit.com/r/LangChain/comments/19137og/summary_generation_on_large_csv_files/) , 2024-01-10-0910
```
I have a large csv file of about 50mb with a few columns. I would like to summarize the information that I have in this 
file using an LLM. My major concern would be dealing with the context length. Can anyone provide me with any existing im
plementations of this concept or guide me with links which can help me? Thank you.
```
---

     
 
all -  [ Structured data extraction from text using Langchain? ](https://www.reddit.com/r/LangChain/comments/19129gt/structured_data_extraction_from_text_using/) , 2024-01-10-0910
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

     
 
all -  [ My first pipeline using Llama7b / llvm / Langchain / EasyOCR / TinyDB ](https://www.reddit.com/r/LocalLLaMA/comments/1910xpv/my_first_pipeline_using_llama7b_llvm_langchain/) , 2024-01-10-0910
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

     
 
all -  [ How to use model from hugging face in langchain? ](https://www.reddit.com/r/Langchaindev/comments/191082s/how_to_use_model_from_hugging_face_in_langchain/) , 2024-01-10-0910
```
It is constantly giving me time out error
```
---

     
 
all -  [ Tabular and Graph Output ](https://www.reddit.com/r/LangChain/comments/190sud6/tabular_and_graph_output/) , 2024-01-10-0910
```
Hi Everyone,

I am new to Langchain and been using it to query SQL databases. I want to query a database where the outpu
t I get is in tabular form like how would you query in a mysql workbench. The output should have only the relevant colum
ns and data attributes. Then I have a next requirement to output in a graph form for a graph database.

Can anyone guide
 me or share examples on how to do that?
```
---

     
 
all -  [ Error429(insufficient quota) for new openai account ](https://www.reddit.com/gallery/190r1uz) , 2024-01-10-0910
```
I built a basic LLM. Code & error are in the attached pics. My OpenAI account is new and I used 0 credits until now. But
 it's giving me error 429. There isn't any loop to send multiple requests so I don't get why it's throwing that error
```
---

     
 
all -  [ Real time Arxiv API + RAG at inference ](https://www.reddit.com/r/LocalLLaMA/comments/190qaol/real_time_arxiv_api_rag_at_inference/) , 2024-01-10-0910
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

     
 
all -  [ Use Langchain or Assistants API? ](https://www.reddit.com/r/OpenAI/comments/190pm6o/use_langchain_or_assistants_api/) , 2024-01-10-0910
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

     
 
all -  [ Is GenAI hype declining or are low-hanging fruits gone? ](https://www.reddit.com/r/OpenAI/comments/190lb0a/is_genai_hype_declining_or_are_lowhanging_fruits/) , 2024-01-10-0910
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

     
 
all -  [ Best way to do error handling with langchain? ](https://www.reddit.com/r/LangChain/comments/190k71t/best_way_to_do_error_handling_with_langchain/) , 2024-01-10-0910
```
I have some chains setup, but how do I set it up so, if the json fails to parse, you re-ask the chatbot to correct the e
rrors? and if it does parse, it just goes forward. 

Iv'e read through the docs but found this very difficult. I'm not u
sing agents btw, just regular chains. 
```
---

     
 
all -  [ Apply Model Chat / Instruct Template ](https://www.reddit.com/r/LangChain/comments/190i8ne/apply_model_chat_instruct_template/) , 2024-01-10-0910
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

     
 
MachineLearning -  [ [P] An open-source project for deploying local models ](https://www.reddit.com/r/MachineLearning/comments/18zkm5m/p_an_opensource_project_for_deploying_local_models/) , 2024-01-10-0910
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

     
 
MachineLearning -  [ [Project] Temporal Augmented Retrieval (TAR) - Dynamic RAG ](https://www.reddit.com/r/MachineLearning/comments/18uddmj/project_temporal_augmented_retrieval_tar_dynamic/) , 2024-01-10-0910
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

     
 
MachineLearning -  [ [R][P] Autogen + Langchain Tools + Local LLM doesn't work. ](https://www.reddit.com/r/MachineLearning/comments/18tex1j/rp_autogen_langchain_tools_local_llm_doesnt_work/) , 2024-01-10-0910
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

     
 
MachineLearning -  [ [P] Seeking Advice for Building a School Handbook Chatbot Using OpenAI and Vector Databases ](https://www.reddit.com/r/MachineLearning/comments/18rndcp/p_seeking_advice_for_building_a_school_handbook/) , 2024-01-10-0910
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

     
 
deeplearning -  [ Unlocking the Power of Language: How LangChain Transforms Data Analysis and More ](https://www.reddit.com/r/deeplearning/comments/18l788y/unlocking_the_power_of_language_how_langchain/) , 2024-01-10-0910
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

     
 
deeplearning -  [ [D] Mastering Chain Composition with LangChain Expression Language (LCEL) ](https://www.reddit.com/r/deeplearning/comments/18i0wot/d_mastering_chain_composition_with_langchain/) , 2024-01-10-0910
```
In the intricate landscape of modern software development, orchestrating complex sequences of actions seamlessly poses a
 significant challenge. Enter LangChain Expression Language (LCEL), a groundbreaking declarative approach designed to re
volutionize the composition of chains within software architecture.

Link: [https://medium.com/ai-artistry/mastering-cha
in-composition-with-langchain-expression-language-lcel-2d5041fb0cbd](https://medium.com/ai-artistry/mastering-chain-comp
osition-with-langchain-expression-language-lcel-2d5041fb0cbd)  
```
---

     
