 
all -  [ Question about manual testing on LangSmith hub ](https://www.reddit.com/r/LangChain/comments/1d4d5mp/question_about_manual_testing_on_langsmith_hub/) , 2024-05-31-0910
```
Hi folks, I was just wondering if there is a feature on the langSmith where we can manually evaluate the inputs/outputs 
of our LLM. On the documentation they talk about how there can be manual evaluators that can be set up but I can't seem 
to find it.

any help would be appreciated.

thanks in advance 
```
---

     
 
all -  [ How to resolve ModuleNotFoundError ](https://www.reddit.com/r/learnpython/comments/1d4c5q2/how_to_resolve_modulenotfounderror/) , 2024-05-31-0910
```
Hi guys, I need help resolving the ModelNotFoundError after installing the library from the command line. I can see the 
library on the pip list, but if I run my code, I get the error below. 

  
---------------------------------------------
------------------------------  
ModuleNotFoundError                       Traceback (most recent call last)  
Cell In\[
30\], [line 3](vscode-notebook-cell:?execution_count=30&line=3)  
[1](vscode-notebook-cell:?execution_count=30&line=1) #
 import libraries   
----> [3](vscode-notebook-cell:?execution_count=30&line=3) from langchain.llms import OpenAI  
  
F
ile c:\\Users\\LENOVO\\Desktop\\All-folder\\personal\\LLM\\venv\\lib\\site-packages\\langchain\\llms\\\_\_init\_\_.py:54
4, in \_\_getattr\_\_(name)  
[543](file:///C:/Users/LENOVO/Desktop/All-folder/personal/LLM/venv/lib/site-packages/langc
hain/llms/__init__.py:543) def \_\_getattr\_\_(name: str) -> Any:  
--> [544](file:///C:/Users/LENOVO/Desktop/All-folder
/personal/LLM/venv/lib/site-packages/langchain/llms/__init__.py:544)from langchain\_community import llms  
[546](file:/
//C:/Users/LENOVO/Desktop/All-folder/personal/LLM/venv/lib/site-packages/langchain/llms/__init__.py:546)# If not in inte
ractive env, raise warning.  
[547](file:///C:/Users/LENOVO/Desktop/All-folder/personal/LLM/venv/lib/site-packages/langc
hain/llms/__init__.py:547)if not is\_interactive\_env():  
  
ModuleNotFoundError: No module named 'langchain\_community
'


```
---

     
 
all -  [ Build a QA Bot with TypeScript for your documentation with Langchain ](https://www.reddit.com/r/typescript/comments/1d4bvd3/build_a_qa_bot_with_typescript_for_your/) , 2024-05-31-0910
```
**TL;DR**

Are you interested in building a QA bot for your docs?

In this tutorial, it walks through:

* How to build a
n AI-powered Q&A bot for your websites and documentation
* Fetch your website's content via sitemaps, accept user's quer
ies, and provide answers based on the data provided.

Stack:

* TypeScript
* Next.js for the frontend,
* Wing for the ba
ckend
* Langchain processes users' queries with LLMs (GPT-4)

Read the full article [here](https://wingla.ng/qa-bot).
```
---

     
 
all -  [ Is there a tool or website for showing the best stack to do a particular thing and examples. ](https://www.reddit.com/r/webdev/comments/1d4babf/is_there_a_tool_or_website_for_showing_the_best/) , 2024-05-31-0910
```
Is there a website or repo list that shows off the best stack to do a particular thing?

  
Like search:

How to make a 
chatbot app,

Here's a list of tools to help you make x with this stack:

1. Langchain 

2. Python

3. OpenAI

etc
```
---

     
 
all -  [ Help on creating a ChatBot for in-app private data ](https://www.reddit.com/r/LangChain/comments/1d4a55w/help_on_creating_a_chatbot_for_inapp_private_data/) , 2024-05-31-0910
```
Hello, I'm very new to LLMs and I got confused on how to proceed. At the moment I want to use LanChain and ChatGPT.

I h
ave this task:

* in the backend of my app I have a few functions that query SQL database and return a JSON
* the ChatBo
t should take the user question as an input
* the ChatBot should choose which functions to call
* based on the JSON obje
ct/s returned the ChatBot should be able to answer the user\`s question

I'm not sure what would be the best approach he
re - RAG, Agent, OpenAI Function calling. 
```
---

     
 
all -  [ RAG relation between documents ](https://www.reddit.com/r/LangChain/comments/1d49off/rag_relation_between_documents/) , 2024-05-31-0910
```
I have a list of json objects that have a module name and a link to a file. I have this files downloaded. However when I
 query something about a module name, it only retrieves that json object and does not retrieve the file associated with 
that json object. I am assuming a solution would be to add module names to all the files so it relates them, however is 
there a better way?
```
---

     
 
all -  [ RAG Me Up - easy RAG ](https://www.reddit.com/r/LocalLLaMA/comments/1d48l95/rag_me_up_easy_rag/) , 2024-05-31-0910
```
After doing RAG for quite a while, we figured we'd open source our generic framework with some lessons learned so far, c
heck it out: [https://github.com/UnderstandLingBV/RAGMeUp](https://github.com/UnderstandLingBV/RAGMeUp)

The idea is to 
make RAG simple as possible so we aim to add a lot more support for different file types, chunkers and vector stores. Th
e goal is to not write code but instead configure the whole thing.

It uses Langchain and can be run as a server to writ
e your own UI against or more importantly, you can use one of ours. For now we have a Scala UI written and committed but
 there's plans on doing a NodeJS and Python one too so everyone can just stick with their own programming language.

Thi
ngs like deciding if new documents should be fetched or not are added natively and adding/reloading documents on the fly
 as well. In the future we will most likely also add automatic summarization to make sure that the full chat history wil
l always fit within context sizes (wink, LLaMa3).

There's probably stuff like this out there already, or maybe not, but
 either way: have a go and let us know if you enjoy it.

Heavily under development right now, so a bit feature-poor but 
there's lots more to come.
```
---

     
 
all -  [ CopilotKit v0.9.0 (MIT) - open source framework for in-app AI Copilots & agents ](https://www.reddit.com/r/OpenAI/comments/1d48jqp/copilotkit_v090_mit_open_source_framework_for/) , 2024-05-31-0910
```
Hi everyone,

I'm a contributor to an awesome open-source library that I think the developers here will love.

[CopilotK
it](https://github.com/CopilotKit/CopilotKit) is an open-source framework for building in-app AI copilots, in-app AI age
nts (powered by LangChain & AI text editing. The framework makes building these easy and it manages the connection betwe
en your application context & your copilot.

We have a really strong emphasis in our community of staying on top of ever
y new development in the field.

**Here are some of the new features in the latest release:**

1. GPT-4o & native voice 
support (build a voice-powered in-app copilot)
2. LangChain adapter for bringing specialized agents into your app
3. Gem
ini support
4. Generative UI: chatbot can stream generated UI components as specified by the developer & the LLM.
5. Cop
ilot suggestions: auto suggestions of new questions for the end-user to ask with generative UI. These can be manually co
ntrolled by the programmer, and also informed by GPT intelligence for the given context

The library is fully open-sourc
ed under MIT license and self hosted. We're still looking for more things to add, happy to hear your thoughts :)

[https
://github.com/CopilotKit/CopilotKit](https://github.com/CopilotKit/CopilotKit)
```
---

     
 
all -  [ Crewai x Langchain ](https://www.reddit.com/r/crewai/comments/1d447tj/crewai_x_langchain/) , 2024-05-31-0910
```
Hi everyone!

  
Does anyone know any documentation/reference on how to best integrate langchain tools with crewai? 
```
---

     
 
all -  [ Langchain lemonai tool ](https://www.reddit.com/r/LangChain/comments/1d44719/langchain_lemonai_tool/) , 2024-05-31-0910
```
Hi everyone! I'm trying to wrap my head around how I could integrate lemonai agents into my workflow. It says that it in
tegrates with `Airtable`, `Hubspot`, `Discord`, `Notion`, `Slack` and `Github`. It sounds super powerful and i was wonde
ring if you had any feedback ?
```
---

     
 
all -  [ Rag with AWS Neptune ](https://www.reddit.com/r/LangChain/comments/1d42rsd/rag_with_aws_neptune/) , 2024-05-31-0910
```
I am looking for tutorial/repo on RAG with Neptune for graph data
```
---

     
 
all -  [ CrewAI on open webui ](https://www.reddit.com/r/crewai/comments/1d42p41/crewai_on_open_webui/) , 2024-05-31-0910
```
Created a crew with 4 local lammas and been trying to use open webui without succes. 

    import openai
    from langch
ain_community.llms import Ollama
    from crewai import Agent, Task, Crew, Process
    from flask import Flask, request,
 jsonify
    import threading
    
    # Define the models
    model1 = Ollama(model='starcoder2:latest')
    model2 = O
llama(model='deepseek-coder:latest')
    model3 = Ollama(model='codegemma:2b')
    model4 = Ollama(model='codellama')
  
  
    # Define the agents with their respective goals and backstories
    classifier1 = Agent(
        role='Code Perfo
rmance Optimizer',
        goal='Optimize the provided code for performance, fixing efficiency issues such as unnecessar
y nested loops, high-cost operations, and opportunities for parallelization or optimization.',
        backstory='Prof. 
OptiCode is an expert in high-performance computing, specializing in squeezing out every bit of performance from complex
 code.',
        verbose=True,
        allow_delegation=False,
        llm=model1
    )
    
    classifier2 = Agent(
  
      role='Code Readability Enhancer',
        goal='Enhance the readability of the provided code, making changes to va
riable names, function structures, and comments.',
        backstory='Dr. CleanCode excels in making complex code more h
uman-readable, bridging the gap between human language and programming languages.',
        verbose=True,
        allow_
delegation=False,
        llm=model2
    )
    
    classifier3 = Agent(
        role='SOLID Principles Verifier',
     
   goal='Ensure the provided code adheres to SOLID principles, making necessary adjustments and improvements.',
        
backstory='Solidus helps developers ensure their code adheres to high standards of software engineering, making it robus
t and maintainable.',
        verbose=True,
        allow_delegation=False,
        llm=model3
    )
    
    classifier
4 = Agent(
        role='Code Correctness Verifier',
        goal='Verify the correctness of the provided code, ensuring
 it meets requirements, identifying logical errors, and finalizing the code.',
        backstory='DebugMaster has an ext
ensive database of coding errors and a keen understanding of code logic, ensuring every piece of code it reviews is flaw
less.',
        verbose=True,
        allow_delegation=False,
        llm=model4
    )
    
    # Define the tasks for e
ach agent
    agent1_task = Task(
        description='Analyze and optimize the code for performance, identifying and fi
xing efficiency issues, and apply improvements.',
        agent=classifier1,
        expected_output='Enhanced code with
 performance improvements.'
    )
    
    agent2_task = Task(
        description='Enhance the readability of the code,
 making changes to variable names, function structures, and comments.',
        agent=classifier2,
        expected_outp
ut='Enhanced code with improved readability.'
    )
    
    agent3_task = Task(
        description='Ensure the code ad
heres to SOLID principles, making necessary adjustments and improvements.',
        agent=classifier3,
        expected_
output='Enhanced code adhering to SOLID principles.'
    )
    
    agent4_task = Task(
        description='Verify the 
correctness of the code, ensuring it meets requirements, identifying logical errors, and finalizing the code.',
        
agent=classifier4,
        expected_output='Fully corrected and verified code.'
    )
    
    # Create the crew with ag
ents and tasks in sequence
    crew = Crew(
        agents=[classifier1, classifier2, classifier3, classifier4],
       
 tasks=[agent1_task, agent2_task, agent3_task, agent4_task],
        process=Process.sequential
    )
    
    # Initial
ize Flask app
    app = Flask(__name__)
    
    @app.route('/api/models', methods=['GET'])
    def list_models():
     
   return jsonify({
            'models': [
                {'name': 'crewai_code_optimizer', 'description': 'A model th
at optimizes code through various stages.'}
            ]
        })
    
    @app.route('/api/models/crewai_code_optimi
zer', methods=['POST'])
    def handle_models():
        data = request.json
        initial_code = data.get('code', '')

        
        if not initial_code:
            return jsonify({'error': 'No code provided'}), 400
    
        initi
al_task = Task(
            description='This is the initial task to provide the code to be analyzed.',
            agen
t=classifier1,
            expected_output=initial_code,
        )
    
        # Add the initial task to the crew
     
   crew.tasks.insert(0, initial_task)
    
        # Kick off the process
        output = crew.kickoff()
    
        #
 Remove the initial task after processing
        crew.tasks.pop(0)
    
        return jsonify({'enhanced_code': output
})
    
    def run_flask():
        app.run(host='0.0.0.0', port=5003)
    
    def run_chat():
        while True:
   
         initial_code = input('Please input the code to be analyzed (or type 'exit' to quit):\n')
            if initial
_code.lower() == 'exit':
                break
    
            initial_task = Task(
                description='This i
s the initial task to provide the code to be analyzed.',
                agent=classifier1,
                expected_out
put=initial_code,
            )
    
            # Add the initial task to the crew
            crew.tasks.insert(0, ini
tial_task)
    
            # Kick off the process
            output = crew.kickoff()
            print(output)
    
  
          # Remove the initial task after processing
            crew.tasks.pop(0)
    
    if __name__ == '__main__':
 
       # Run Flask in a separate thread
        flask_thread = threading.Thread(target=run_flask)
        flask_thread.s
tart()
    
        # Run the chat interface
        run_chat()
    
    
    

Can anyone give me a hint on where I'm m
aking a mistake?  

```
---

     
 
all -  [ How to deploy a finetuned model on a private server? ](https://www.reddit.com/r/LocalLLaMA/comments/1d405va/how_to_deploy_a_finetuned_model_on_a_private/) , 2024-05-31-0910
```
I have a project where I need to fine-tune a Large Language Model (LLM) such as LLAMA3 for a specific task and then depl
oy it on the company's server as a chatbot to recommend 'questionnaires / surveys' based on studies described by the use
rs.

As I am new to working with LLMs, I need some guidance. Here is my planned approach:

1. Obtain a base model and tr
ain it on my dataset using a fine-tuning method like QLoRa.
2. Save the trained model and convert it into a GGFU file us
ing LLAMA.cpp, allowing for local testing. (I'm planning to using langchain at this step)
3. Once the model is tested an
d verified, create an API that enables users to interact with the model.
4. Develop a Docker image of the application, w
hich will consist of the API at this stage.
5. Deploy the API on the company’s private server using the Docker image and
 connect it to our website.

Is this the correct approach to achieve my goal? Thank you for your help.
```
---

     
 
all -  [ Leveraging LangChain and Streamlit for Interactive CSV Analysis ](https://dly.to/Im4DJK9gQzv) , 2024-05-31-0910
```

```
---

     
 
all -  [ AI agent for identifying longest running queries and optimizing them on Snowflake ](https://www.reddit.com/r/snowflake/comments/1d3yhea/ai_agent_for_identifying_longest_running_queries/) , 2024-05-31-0910
```
Hello everyone! My team has created a Snowflake query optimization agent, and we wanted to share it with you all to get 
ideas/feedback on how to improve it and identify other use cases for it. Meet Snow-Wise!

**What it does:**

* Identifie
s the longest running tasks
* Offers immediate optimization suggestions
* Shares query logs to verify improvements

We u
sed Snowflake Arctic, Cortex, Langchain, Python, OpenAI, and Streamlit to build it. So far, we've seen a 50% reduction i
n latency for some of our warehouse queries with the help of Snow-Wise.

Here is the [demo video](https://www.loom.com/s
hare/119282ca006d4792873d38d86dc23f69) put together by u/imshubham31. The [GitHub repo](https://github.com/HousewareHQ/s
now-wise) has more details if you want to check it out.

Would love to hear your thoughts and feedback!
```
---

     
 
all -  [ Is Elastic search better than ChromaDB? ](https://www.reddit.com/r/LangChain/comments/1d3xtlq/is_elastic_search_better_than_chromadb/) , 2024-05-31-0910
```
So, I am working on a RAG framework and for that I am currently using ChromaDB with all-MiniLM-L6-v2 embedding function.
 But one of my colleague suggested using Elastic Search for they mentioned it is much faster and accurate. So I did my o
wn testing and found that for top_k=5, ES is 100% faster than ChromaDB. For all top_k values, ES is performing much fast
er. Also for top_k = 5, ES retrieved current document link 37% times accurately than ChromaDB. 

However, when I read th
ings online, it is mentioned that ChromaDB is faster and is used by many companies as their go to vectordb. What do you 
think could be the possible reason for this? Is there anything that I can use to improve ChromaDB's performance and accu
racy?
```
---

     
 
all -  [ Would you use this instead of Perplexity? ](https://www.reddit.com/r/perplexity_ai/comments/1d3upmf/would_you_use_this_instead_of_perplexity/) , 2024-05-31-0910
```
I'm building a General purpose AI Copilot (Bind AI) with ability to switch between GPT-4o, Claude 3 Opus, Command R and 
a few other models. We just added 'Web Search', similar to Perplexity it can research the web and provide a summarized a
nswer. You can generate code and execute the code (simple stuff which does not require multiple files to execute)

I wan
ted get feedback from this community, as you guys use multiple tools along with Perplexity:

1. Would you find this usef
ul, in addition *or* as a replacement to Perplexity, Phind, MS Copilot or similar?
2. If not, why not, what could make t
his more useful?

If you're interested to know the inner workings, we're using a prompt template + Langchain Agents/Tool
s which interacts with the web. We experimented with quite a few APIs for search retrieval (Bing search, Brave, Google s
earch via SERPapi, Tavily). It is fairly easy to get something working, however, it does require implementing agentic wo
rkflows and tool routing to get better responses, esp. for cases where you don't actually need to search the web (recent
 models such as GPT-4o do fairly well without internet search). We also noticed that, better models do better job synthe
sizing the information from search results, we compared 4o, Command R, Haiku, Mixtral, GPT 3.5. (I might write a blog po
st on this, I had posted a comment on a sub-reddit recently). We're not yet integrated with Mistral Codestral which just
 came out today.

**Edit**: Removed the links, since I got the feedback I was looking for.

  
If you're curious, you ca
n google for 'Bind AI' and find the link.
```
---

     
 
all -  [ GCP Vector Search as Vector Database? ](https://www.reddit.com/r/LangChain/comments/1d3tx3f/gcp_vector_search_as_vector_database/) , 2024-05-31-0910
```
I'm looking for a vector database that can scale - around 500m+ embeddings. I want to know how GCP Vector Search compare
s to other solutions such as QDrant and Milvus. Seems like GCP Vector Search is super easy to get started and has high p
erformance. I'm not sure why more people aren't talking about it.
```
---

     
 
all -  [ Question about chatbot and chat message history with vector db ](https://www.reddit.com/r/LangChain/comments/1d3ok4l/question_about_chatbot_and_chat_message_history/) , 2024-05-31-0910
```
Basically I am creating an app in which you are able to chat with the openai and I want to store the last 7 times or 7 d
ays worth of message history from user. Now the problem is if i plainly save the chat messages then it takes up a lot of
 token size. I tried using the conversation summary buffer and all kinds of memory but either they were also resulting i
n a lot of tokens or did not give as expected output.

My question is that is there a way that once the user is done wit
h the chat I can store the chat in a vector db and then whenever a user chats with the AI again it first checks the vect
or db for a reference of that object and returns related data and then my open ai llm with a specified prompt and the da
ta collected give a response whereas if there is no data found speific to the object then my llm plainly uses the prompt
 I have given it?

Kindly give me if there are any other ways to do it 

My tech stack is  
Frontend Flutter, Backend Py
thon therefore it would be easy for me to attach langchain to python and just push requests from my app to my hosted api
 using python. 

Thanks
```
---

     
 
all -  [ Generative AI Agents Developer Contest with NVIDIA and LangChain ](https://www.reddit.com/r/nvidia/comments/1d3ng79/generative_ai_agents_developer_contest_with/) , 2024-05-31-0910
```
As part of the NVIDIA developer team, I wanted to share details about our current [Generative AI Agents Developer Contes
t with LangChain](https://nvda.ws/4dXWDE3), running now through June 17.

This is your chance to start developing your n
ext Generative AI application for a chance to win an NVIDIA 4090 GPU and LangSmith credits.

To get started, check out o
ur step-by-step developer resources on our [contest page](https://nvda.ws/4dXWDE3) and our [ contest tips and tricks](ht
tps://nvda.ws/44ZJUN3) technical blog. Connect with NVIDIA and LangChain technical experts on our [Discord channel](http
s://discord.com/invite/nvidiadeveloper) to help with troubleshooting and to answer your questions.

Participants will ha
ve the chance to win GPUs and hundreds of dollars worth of rewards from LangChain:

* Two winners will each receive an [
NVIDIA GeForce RTX 4090 GPU](https://www.nvidia.com/en-us/geforce/graphics-cards/40-series/rtx-4090/).
* One special men
tion will receive an NVIDIA GeForce RTX 4080 SUPER.
* The top 10 projects will each receive $200 in LangSmith credits an
d LangChain merchandise
* The top 100 projects will each receive an[ NVIDIA Deep Learning Institute LLM course](https://
www.nvidia.com/en-us/training/).
* All valid participants will receive a digital participation certificate signed by NVI
DIA CEO Jensen Huang.

See the contest [Terms & Conditions](https://www.nvidia.com/en-us/ai-data-science/generative-ai/d
eveloper-contest-with-langchain/terms-and-conditions/)

Good luck with your projects!

https://preview.redd.it/hj81jz30q
f3d1.jpg?width=1920&format=pjpg&auto=webp&s=e04e566f7268f021c430f6c93f30957a621554b5
```
---

     
 
all -  [ Visual Agents Flow Engineering Tool Early-Access ](https://www.reddit.com/r/LangChain/comments/1d3iv90/visual_agents_flow_engineering_tool_earlyaccess/) , 2024-05-31-0910
```
Hi,  
   I'm working on a visual agents tool built on langchain and looking for people to try it out and maybe give some
 feedback or thoughts on it. It's a completely serverless tool so there is no backend or API and all the execution and d
ata resides local and private to you.

What do you think? I'm just one guy building this, so I'm hoping to get some comm
unity input! Thank you

Here is a quick demo of building a SQL Agent  and then answering a question about your data. All
 within YOUR browser environment.  
[https://youtu.be/\_3crxBzVg3A?si=-qCtoBv21NrIcFws](https://youtu.be/_3crxBzVg3A?si=
-qCtoBv21NrIcFws)  


And the app

[https://app.visualagents.ai/#/](https://app.visualagents.ai/#/)  

```
---

     
 
all -  [ Need a Help on creating RAG-based SQL Bot ](https://www.reddit.com/r/LangChain/comments/1d3hhkj/need_a_help_on_creating_ragbased_sql_bot/) , 2024-05-31-0910
```
I have a requirement to build a Chatbot Application over a SQL DB , Here the SQL DB will be very huge consists of many F
act and Dimensional tables,  Here are my below queries and please try to help me answer or provide better references.

1
. Chatbot must be able to pick table names dynamically based on the user input and form queries and execute

2. How a Ve
ctore DB can be leveraged here, can we  embed all the tables and store in the vectoreDB, will be easier to query on simi
larity search?- am I missing any basics here please guide

  
3. is it a viable option to build an RAG system on the SQL
 DB and have it embedded into Vector DB ?  
and use memory management to retrieve the previously asked Queries to pop up
 automatically ?

  
can you please help!
```
---

     
 
all -  [ gpt-4o App for Windows and Linux and macos =) MIT licenced ](https://www.reddit.com/r/aiagents/comments/1d3h3oc/gpt4o_app_for_windows_and_linux_and_macos_mit/) , 2024-05-31-0910
```
# Explanation and Reason

Hi i am python developer and after OpenAI GPT-4o launch, i just i little bit angry because the
 app that they talked about just work in MacOS and a joke, it will come to windows november lol. Come on bro, if there i
s API, developers like us can make this app and release in just few days with langchain agent and tool infrastructure.


So i just release our GPT-4o clone and its totaly usable. You can use to take meeting notes, writing code and copying to
 your clipboard, or read and remember your calendar. There is unlimited possibilities.

# Current Features

* \*\*Screen
 Read\*\*
* Microphone
* \*\*System Audio\*\*
* Memory

--

* Open and close app
* Open a URL
* \*\*Clipboard\*\*
* Sear
ch Engines
* \*\*Python and SH Interpreters\*\*
* Writing and Running Scripts
* Using your Telegram Account
* Knowledge 
Management

# Open Call to devs

If there is some people to interest and develop this and adding some features just like
 auto take screen shot each 5 second and say somethings if something wrong. We can open a **GitHub Organization** and de
velop together. Just for open-source, just for competition.

https://preview.redd.it/mipkh0pgbe3d1.png?width=656&format=
png&auto=webp&s=988cb7a9653c1860d854d13fd3f415de7192ff13

[onuratakan/gpt-computer-assistant: gpt-4o Desktop Personel As
isstant (github.com)](https://github.com/onuratakan/gpt-computer-assistant)
```
---

     
 
all -  [ gpt-4o App for Windows and Linux and macos =) MIT licenced ](https://www.reddit.com/r/gpt_4o/comments/1d3h060/gpt4o_app_for_windows_and_linux_and_macos_mit/) , 2024-05-31-0910
```
# Explanation and Reason

Hi i am python developer and after OpenAI GPT-4o launch, i just i little bit angry because the
 app that they talked about just work in MacOS and a joke, it will come to windows november lol. Come on bro, if there i
s API, developers like us can make this app and release in just few days with langchain agent and tool infrastructure.


So i just release our GPT-4o clone and its totaly usable. You can use to take meeting notes, writing code and copying to
 your clipboard, or read and remember your calendar. There is unlimited possibilities.

# Current Features

* \*\*Screen
 Read\*\*
* Microphone
* \*\*System Audio\*\*
* Memory

--

* Open and close app
* Open a URL

* \*\*Clipboard\*\*
* Sea
rch Engines
* \*\*Python and SH Interpreters\*\*
* Writing and Running Scripts
* Using your Telegram Account
* Knowledge
 Management

# Open Call to devs

If there is some people to interest and develop this and adding some features just lik
e auto take screen shot each 5 second and say somethings if something wrong. We can open a **GitHub Organization** and d
evelop together. Just for open-source, just for competition.

https://preview.redd.it/mipkh0pgbe3d1.png?width=656&format
=png&auto=webp&s=988cb7a9653c1860d854d13fd3f415de7192ff13

  


[onuratakan/gpt-computer-assistant: gpt-4o Desktop Perso
nel Asisstant (github.com)](https://github.com/onuratakan/gpt-computer-assistant)
```
---

     
 
all -  [ Attempting to Parse PDF's with Financial Data (Balance Sheets, P&Ls, 10Ks) ](https://www.reddit.com/r/LangChain/comments/1d3fz8x/attempting_to_parse_pdfs_with_financial_data/) , 2024-05-31-0910
```
Has anyone had any luck using LangChain to parse these kind of documents?

I built a chatbot before to answer questions 
about a code base and about research papers. Those were pretty straight forward. But reading financial pdfs has turned o
ut to be a real challenge.

I'm able to get good answers for pdfs that are more structured (like some of the P&L's) but 
with others it's constantly providing wrong answers or no answer and consistently referencing wrong documents.

I'm feel
 like it probably has to do with how I'm vectorizing the data but I'm at a loss. 

Here's the code:

    import os
    o
s.environ['PINECONE_API_KEY'] = PINECONE_API_KEY
    
    from langchain.retrievers.self_query.base import SelfQueryRetr
iever
    from langchain.chains.query_constructor.base import AttributeInfo
    from langchain.prompts import ChatPrompt
Template
    from langchain.schema.output_parser import StrOutputParser
    from langchain.memory import ConversationTok
enBufferMemory
    from langchain_core.prompts import MessagesPlaceholder
    from langchain_openai.embeddings import Op
enAIEmbeddings
    from langchain_openai.chat_models import ChatOpenAI
    from langchain_community.document_loaders imp
ort DirectoryLoader
    from langchain_community.vectorstores import Pinecone as PC
    from pinecone import Pinecone, S
erverlessSpec
    import nltk
    
    class RAG():
        def __init__(self,
                     docs_dir: str,
     
                n_retrievals: int = 4,
                     chat_max_tokens: int = 3097,
                     model_name
 = 'gpt-4',
                     creativeness: float = 0.7):
            self.__model = self.__set_llm_model(model_name,
 creativeness)
            self.__docs_list = self.__get_docs_list(docs_dir)
            self.__retriever = self.__set_r
etriever(k=n_retrievals)
    
        def __set_llm_model(self, model_name = 'gpt-4', temperature: float = 0.7):
       
     return ChatOpenAI(
                       model_name=model_name, 
                       temperature=temperature, 

                       openai_api_key=os.environ['OPENAI_API_KEY'])
        
        def __get_docs_list(self, docs_dir:
 str) -> list:
            print('Loading documents...')
            loader = DirectoryLoader(docs_dir,
                
                     recursive=True,
                                     show_progress=True,
                          
           use_multithreading=True,
                                     max_concurrency=4)
            docs_list = load
er.load_and_split()
           
            return docs_list
        
        def __set_retriever(self, k: int = 4):
   
         # Initialize Pinecone
            pinecone = Pinecone(
                api_key=PINECONE_API_KEY
            )
 
           index_name = 'fin-docs'
    
            embeddings = OpenAIEmbeddings(model='text-embedding-3-small')
      
      
            # Create Pinecone index if it doesn't exist
            if index_name not in pinecone.list_indexes().
names():
                pinecone.create_index(
                    name=index_name, 
                    dimension=3072
, 
                    metric='cosine', 
                    spec=ServerlessSpec(cloud='aws', region='us-east-1')
      
          )
            
            vector_store = PC.from_documents(
                self.__docs_list,
               
 embedding=embeddings,
                index_name=index_name
            )
    
            _retriever = SelfQueryRetrie
ver.from_llm(
                self.__model,
                vector_store,
                document_content_description,

                metadata_field_info,
                search_kwargs={'k': k}
            )
    
            return _retri
ever
        
        def __set_chat_history(self, max_token_limit: int = 3097):
            return ConversationTokenBuf
ferMemory(
                       llm=self.__model,         
                       max_token_limit=max_token_limit,
   
                    return_messages=True)
        
        def ask(self, question: str) -> str:
            prompt = Cha
tPromptTemplate.from_messages([
                ('system', 'You are an assistant responsible for answering questions 
  
                      about documents. Answer the user's question with a 
                        reasonable level of de
tail and based on the following 
                        context document(s):\n\n{context}'),
                ('user', '
{input}'),
            ])
           
            output_parser = StrOutputParser()
            chain = prompt | self.__
model | output_parser
            answer = chain.invoke({
                'input': question,
                'context': 
self.__retriever.get_relevant_documents(question)
            })
           
            return answer

I can try and pr
ovide example docs if that would help as well. Would appreciate any help from ppl who've done something similar to this 
before.

&#x200B;
```
---

     
 
all -  [ Scaling RAG for Large Datasets: Need Your Insights! ](https://www.reddit.com/r/LangChain/comments/1d3fy9h/scaling_rag_for_large_datasets_need_your_insights/) , 2024-05-31-0910
```
I am currently working on implementing RAG for a specific use case, and I have made good progress with a working example
. So far, I have created embeddings for about 10-15 PDF/HTML files and I am using Qdrant locally (via Docker) to manage 
them.

Now, I am looking to scale up to around 30-40k files and I am unsure if this will work seamlessly. I have already
 implemented metadata filtering, so narrowing down relevant chunks isn't a problem.

My main concern is the memory usage
 of the Docker container. When I check the container, it shows a memory cap of 3.5GB. I am new to Docker, so I am wonder
ing if my vector embeddings size shouldn't exceed this limit. If that's the case, how should I address this problem?

Ha
s anyone here tried using RAG with such a large dataset? If so, did you encounter any issues, particularly with handling
 and storing vector embeddings? Any best practices or tips you could share would be greatly appreciated!
```
---

     
 
all -  [ Extracting Tables in PDFs ](https://www.reddit.com/r/LangChain/comments/1d3fi3d/extracting_tables_in_pdfs/) , 2024-05-31-0910
```
Hi everyone. I am having troubles with extracting Tables in PDFs. I have PDFs of pricing options for different types of 
bricks. Theyre meant for marketing purposes actually, but I want to extract this value into JSON objects using Langchain
.

Take a look:

[Pricing options for bricks inside a PDF](https://preview.redd.it/z05xvep2zd3d1.png?width=1910&format=p
ng&auto=webp&s=1cefd038628e6921ad1a610a6237838ddc892ff7)

I have already tried using [Unstructured.io](http://Unstructur
ed.io) however the JSON it returned wasnt good and it didnt even detect the Tables.

This is the workflow im trying to a
chieve:

1. User loads in PDF of pricing list
2. Document is split per table (I only need the info of the data, nothing 
else. Some documents extend 100 pages)
3. For each Table, an LLM takes the information and creates a meaningful JSON out
 of it
4. I save the JSON inside a db

How would I do this splitting?

Thank you all in advance for your help :)

  
UPD
ATE: I managed to get great results! Thanks to everyone who helped. Really nice to have recieved and tried out your sugg
estion. The one that worked for me best was from @[Classic\_essays](https://www.reddit.com/user/Classic_essays/) . 

Her
es a sneak peek:

https://preview.redd.it/l3cvw4jeem3d1.png?width=1326&format=png&auto=webp&s=19f7aa646102fc562657ee1ff5
1b70b28ec631b2

For those interested in the sollution I did:

Very simple: I splitted the PDF by page and encoded each p
age with base64 and stored it in an array. Then I sent the single page to GPT with a prompt.

    response = client.chat
.completions.create(
      model='gpt-4o',
      messages=[
          {'role': 'system', 'content': instructions_propmt}
,
        {
          'role': 'user',
          'content': [
            {
              'type': 'image_url',
          
    'image_url': {
                'url': f'data:image/jpeg;base64,{base64_image}',
              },
            },
    
      ],
        }
      ],
      max_tokens=300,
    )

NOTE: This is definitely NOT the cheapest option (for me, aroun
d €0.02 per page for gpt-4o) however it is the one that game me the highest accuracy which was important for this projec
t. 

Again thank you to everyone!
```
---

     
 
all -  [ Bedrock support in structured_output isnt implemented  ](https://www.reddit.com/r/LangChain/comments/1d3dloo/bedrock_support_in_structured_output_isnt/) , 2024-05-31-0910
```
Hi guys i m trying to use  where my llm point on foundation model hosted in bedrock but getting error :notimplemented ye
t 

      File 'C:\code\dev\rmsology\venv\Lib\site-packages\langchain_core\language_models\base.py', line 210, in with_s
tructured_output
        raise NotImplementedError()
    NotImplementedError
    
    
```
---

     
 
all -  [ Chunking a service ticket ](https://www.reddit.com/r/LangChain/comments/1d3bvxq/chunking_a_service_ticket/) , 2024-05-31-0910
```
Hi,
I need to build a RAG using service ticket data.
One service ticket is a ticket opened by the customer about specifi
ed issue for one product, is composed about:
1) one status
2) related product
3) one list of messages write by who has o
pen the ticket and the service team

This ticket can has from 2 to 20/30 messages.

How chunk strategy we can use? I thi
nk that we use a semantic chunk or fixed chunk we could lose the context.

```
---

     
 
all -  [ Parsing Unstructured Text ](https://www.reddit.com/r/LangChain/comments/1d3a3ee/parsing_unstructured_text/) , 2024-05-31-0910
```
Not sure if this the right place but here goes anyway. I have an excel spreadsheet that provides a weekly report. Each r
ow contains 7 columns. 6 of these are standard fare for a spreadsheet. The last one though is a challenge. The cell cont
ains up to 10,000 characters of free form text that represents shift notes from a range of different employees. Typicall
y, these notes take the form of the example below.

<At 7:10 I inspected the widget file. The widget file was complete a
nd had no errors. After that I called the office to report my findings. Then I had a coffee break. I reviewed the log fi
le for the office server and completed that task by nine AM. There were no other events for the remainder of my shift. 9
:30 a.m. arrived on site. 9:45 a.m. inspected the widget file no anomalies noted. 10:05 a.m. received a status update vi
a phone call with Joe Bloggs. 11:15 a.m. morning coffee break. 11:30 a.m. commenced handover with the afternoon shift. N
ew shift on the job from 12:00 p.m. first half of the shift was uneventful. Aroundabout 145 I received a text message to
 advise that the bearing on the widget machine was due to be replaced on Friday. I put a note into the log for the Frida
y crew. At 3:00 p.m. my shift was over. 3:00 p.m. arrived on site. 3:15 p.m. completed review of bog entry for the day. 
345pm phone call the head office requesting additional post-it notes to be supplied. Nothing much happen for the rest of
 the shift. 6:00 p.m. arrived on site. 9 p.m. arrived on site and  inspected the logs. No further action required.>

I'm
 trying to figure out how to 'read' all these notes and pull out what looks like to be a complete event note or summaris
e, in dot points, the events of the day. As I said, this is a sheet for a week and there are at least 5 of these huge te
xt entries, one for each day. 

I've played around a little with chunking but quickly convinced myself that a chunking s
trategy could lead to events being missed because there is no single fit that I can see.

Anyone got any insight on how 
to handle such problems?
```
---

     
 
all -  [ Intercepting Function Calling and showing the data in UI ](https://www.reddit.com/r/LangChain/comments/1d3852u/intercepting_function_calling_and_showing_the/) , 2024-05-31-0910
```
I'm currently working on a project where I need to integrate GPT-3.5 or GPT-4 into a product carousel, instead of the ty
pical markdown text display. Specifically, I'm looking to intercept the model's function calls and then present the resu
lts in a carousel format on my site.

Has anyone here tackled a similar challenge? I'm interested in any insights or app
roaches you might have used to modify the output format of these models.

  
I'd still want the gpt model to have contex
t of what was fetched from the API i.e. what products, specially their names and product Ids?


```
---

     
 
all -  [ How to Make DataFrame Accessible to LangChain Agent ](https://www.reddit.com/r/LangChain/comments/1d368lr/how_to_make_dataframe_accessible_to_langchain/) , 2024-05-31-0910
```
Hi everyone,

I'm currently working on a LangChain agent and need some help with making a DataFrame (df) accessible to t
he agent. Here’s a quick overview of what I’m trying to achieve:

* The agent has access to several function tools.
* Th
ese tools require a DataFrame (df) as a parameter.
* The agent’s task is to call these tools, passing the data stored in
 a df variable.

**My Question:** Is there a way to ensure that the df variable is accessible to the agent so it can suc
cessfully pass the data to the function tools?

Any guidance or examples would be greatly appreciated!

Thanks in advanc
e!
```
---

     
 
all -  [ The best investment after Nvidia GPUs profit is… ](https://www.reddit.com/r/ChatGPT/comments/1d35f6n/the_best_investment_after_nvidia_gpus_profit_is/) , 2024-05-31-0910
```
I’m a investor of NVIDIA and TSMC since 2024/January (STOP reading here if you don't know what their correlation is with
 OpenAI), when I’ve made a research about which business will make a partnership or support to the OpenAI growth (coz no
 business grow up standalone).

Of course some classical AI programming skills background of mine helped me on that view
.

Now after around 50% profit, I’m searching for the next big support for that increasing demand for LLM... something t
hat only few people can predict.

Recently:  
The xAI (Elon) announced will buy 100k units of Nvidia H100 GPU (this is f
ucking awesome... 5x better than the best GPU your addicted gamer friend ever had)...

Apple stopped the production of i
ts own LLM to start a partnership with OpenAI…

Reddit is making a partnership with OpenAI…

We all know the GPT 4.0 isn
't that dumb 3.0 anymore (that 3 version was merely an word predictor, even for simple math operations... not even close
 to the 4.0 reasoning)

And the GPT-5 will make 4.0 look like a dumb (wtf???)

And I’m wondering where is it all going t
o help my investment profit for next 3 years.  
Any ideas to share?

* Maybe some effort on the Reinforcement Learning A
I?
* Better computer vision hardware components?
* Build Custom AI Agents for individuals and businesses?
* Better RAG v
ector databases indexing?
* Realistic voice cloning?
* Neuralink-LLM integration?
* No/Low-code LangChain tool?

DM for 
thoughts partnership about profit on that field.   
Just curious? get out.
```
---

     
 
all -  [ How to show what agent is currently doing to user in streamlit? ](https://www.reddit.com/r/LangChain/comments/1d34xfq/how_to_show_what_agent_is_currently_doing_to_user/) , 2024-05-31-0910
```
Like I want to show, executing agent chain, executing sql genery, generating response like it prints in termial. Is ther
 any way to do this?
```
---

     
 
all -  [ Chat RTX not working
 ](https://www.reddit.com/r/techsupport/comments/1d34tvm/chat_rtx_not_working/) , 2024-05-31-0910
```
i downloaded chat RTX successfully , but it wont run , I get the error of

httpx.ConnectError: \[SSL: CERTIFICATE\_VERIF
Y\_FAILED\] certificate verify failed: unable to get local issuer certificate (\_ssl.c:1007)

and here what does it look
 like in the web:







and here what look like in app cmd







# This site can’t be reached

[**127.0.0.1**](http://
127.0.0.1) refused to connect.

Try:

* Checking the connection
* [Checking the proxy and the firewall](chrome-error://c
hromewebdata/#buttons)

ERR\_CONNECTION\_REFUSEDReloadHide detailsCheck your Internet connectionCheck any cables and reb
oot any routers, modems, or other network devices you may be using.Allow Chrome to access the network in your firewall o
r antivirus settings.If it is already listed as a program allowed to access the network, try removing it from the list a
nd adding it again.If you use a proxy server…Check your proxy settings or contact your network administrator to make sur
e the proxy server is working. If you don't believe you should be using a proxy server: Go to the Chrome menu > Settings
 > Show advanced settings… > Change proxy settings… > LAN Settings and deselect 'Use a proxy server for your LAN'.This s
ite can’t be reached

[**127.0.0.1**](http://127.0.0.1) refused to connect.

Try:

* Checking the connection
* [Checking
 the proxy and the firewall](chrome-error://chromewebdata/#buttons)







hope someone can help, Thanks





Environmen
t path found: C:\\Users\\User\\AppData\\Local\\NVIDIA\\ChatRTX\\env\_nvd\_rag

Privileges of original process: \['SeShut
downPrivilege', 'SeChangeNotifyPrivilege', 'SeUndockPrivilege', 'SeIncreaseWorkingSetPrivilege', 'SeTimeZonePrivilege'\]


Privileges of restricted app token: \['SeChangeNotifyPrivilege'\]

Process Id =  17940

Environment path found: C:\\Us
ers\\User\\AppData\\Local\\NVIDIA\\ChatRTX\\env\_nvd\_rag

App running with config

 {

'models': {

'supported': \[

{


'name': 'Mistral 7B int4',

'id': 'mistral\_model',

'ngc\_model\_name': 'nvidia/llama/mistral-7b-int4-chat:1.2',

'is\
_downloaded\_required': true,

'downloaded': true,

'is\_installation\_required': true,

'setup\_finished': true,

'min\
_gpu\_memory': 8,

'should\_show\_in\_UI': true,

'prerequisite': {

'checkpoints\_files': \[

'config.json',

'rank0.sa
fetensors',

'license.txt'

\],

'tokenizer\_ngc\_dir': 'mistral7b\_hf\_tokenizer',

'tokenizer\_files': {

'config': 'c
onfig.json',

'tokenizer': 'tokenizer.json',

'model': 'tokenizer.model',

'tokenizer\_config': 'tokenizer\_config.json'


},

'checkpoints\_local\_dir': 'model\_checkpoints',

'tokenizer\_local\_dir': 'tokenizer',

'engine\_build\_command':
 'trtllm-build --checkpoint\_dir %checkpoints\_local\_dir% --output\_dir %engine\_dir% --gpt\_attention\_plugin float16 
--gemm\_plugin float16 --max\_batch\_size 1 --max\_input\_len 7168 --max\_output\_len 1024 --context\_fmha=enable --page
d\_kv\_cache=disable --remove\_input\_padding=disable',

'engine\_dir': 'engine'

},

'metadata': {

'engine': 'rank0.en
gine',

'max\_new\_tokens': 1024,

'max\_input\_token': 7168,

'temperature': 0.1,

'prompt\_template': 'Default'

},

'
model\_info': 'The Mistral-7B is a instruct fine-tuned text generation model | <a href='https ://github.c om/mistralai/m
istral-src/blob/main/LICENSE'> License </a>',

'model\_license': '<a href='https ://github. com/mistralai/mistral-src/bl
ob/main/LICENSE'> License </a>',

'model\_size': '4GB'

},

{

'name': 'Llama2 13B int4',

'id': 'llaam2\_model',

'ngc\
_model\_name': 'nvidia/llama/llama2-13b:1.5',

'is\_downloaded\_required': true,

'downloaded': false,

'is\_installatio
n\_required': true,

'setup\_finished': false,

'min\_gpu\_memory': 16,

'should\_show\_in\_UI': false,

'prerequisite':
 {

'checkpoints\_files': \[

'config.json',

'rank0.safetensors',

'README.txt',

'license.txt'

\],

'tokenizer\_ngc\_
dir': 'llama13\_hf\_tokenizer',

'tokenizer\_files': {

'config': 'config.json',

'tokenizer': 'tokenizer.json',

'model
': 'tokenizer.model',

'tokenizer\_config': 'tokenizer\_config.json'

},

'checkpoints\_local\_dir': 'model\_checkpoints
',

'tokenizer\_local\_dir': 'tokenizer',

'engine\_build\_command': 'trtllm-build --checkpoint\_dir %checkpoints\_local
\_dir% --output\_dir %engine\_dir% --gpt\_attention\_plugin float16 --gemm\_plugin float16 --max\_batch\_size 1 --max\_i
nput\_len 3072 --max\_output\_len 1024 --context\_fmha=enable --paged\_kv\_cache=disable --remove\_input\_padding=disabl
e',

'engine\_dir': 'engine'

},

'metadata': {

'engine': 'rank0.engine',

'max\_new\_tokens': 1024,

'max\_input\_toke
n': 7168,

'temperature': 0.1,

'prompt\_template': 'Default'

},

'model\_info': 'LlaMa 2 is a large language AI model 
capable of generating text and code in response to prompts | <a href='https ://ai.meta.c om/llama/license/'> License </a
>',

'model\_license': '<a href='https ://ai.meta.com /llama/license/'> License </a>',

'model\_size': '6.8GB' 

},

{


'name': 'ChatGLM 3 6B int4 (Supports Chinese)',

'id': 'chatglm3\_model',

'ngc\_model\_name': 'nvidia/chatglm3-6b-chat-
int4:1.0',

'is\_downloaded\_required': true,

'downloaded': false,

'is\_installation\_required': true,

'setup\_finish
ed': false,

'min\_gpu\_memory': 8,

'should\_show\_in\_UI': true,

'prerequisite': {

'checkpoints\_files': \[

'config
.json',

'rank0.safetensors',

'license.txt'

\],

'tokenizer\_ngc\_dir': 'Tokenizer',

'tokenizer\_files': {

'config':
 'config.json',

'model': 'tokenizer.model',

'tokenizer\_config': 'tokenizer\_config.json'

},

'checkpoints\_local\_di
r': 'model\_checkpoints',

'tokenizer\_local\_dir': 'tokenizer',

'engine\_build\_command': 'trtllm-build --checkpoint\_
dir %checkpoints\_local\_dir% --output\_dir %engine\_dir% --gemm\_plugin float16 --max\_batch\_size 1 --max\_input\_len 
7168 --max\_output\_len 1024',

'engine\_dir': 'engine'

},

'metadata': {

'engine': 'rank0.engine',

'max\_new\_tokens
': 1024,

'max\_input\_token': 7168,

'temperature': 0.1

},

'model\_info': 'ChatGLM-6B is an open bilingual language m
odel based on General Language Model framework, with 6.2 billion parameters | <a href= 'https ://huggingface.co/THUDM/ch
atglm3-6b/blob/main/MODEL\_LICENSE'> License </a>',

'model\_license': '<a href= 'https ://huggingface.co/THUDM/chatglm3
-6b/blob/main/MODEL\_LICENSE'> License </a>',

'model\_size': '3.8GB'

},

{

'name': 'Gemma 7B int4',

'id': 'Gemma\_mo
del',

'ngc\_model\_name': 'nvidia/llama/gemma-7b-int4-rtx:1.1',

'is\_downloaded\_required': true,

'downloaded': false
,

'is\_installation\_required': true,

'setup\_finished': false,

'min\_gpu\_memory': 16,

'should\_show\_in\_UI': fals
e,

'prerequisite': {

'checkpoints\_files': \[

'config.json',

'rank0.safetensors',

'Prohibited\_use\_policy.txt',

'
license.txt',

'Notice.txt'

\],

'tokenizer\_ngc\_dir': 'Gemma7b\_hf\_tokenizer',

'tokenizer\_files': {

'vocab\_file'
: 'tmp\_vocab.model'

},

'checkpoints\_local\_dir': 'model\_checkpoints',

'vocab\_local\_dir': 'tokenizer',

'engine\_
build\_command': 'trtllm-build --checkpoint\_dir %checkpoints\_local\_dir% --gemm\_plugin float16 --gpt\_attention\_plug
in float16 --max\_batch\_size 1 --max\_input\_len 4096 --max\_output\_len 1024 --output\_dir %engine\_dir%',

'engine\_d
ir': 'engine'

},

'metadata': {

'engine': 'rank0.engine',

'max\_new\_tokens': 1024,

'max\_input\_token': 7168,

'tem
perature': 0.1

},

'model\_info': 'Gemma-7B is a 7B parameter model from Gemma family of models from Google | <a href= 
'https ://ai.google.dev/gemma/terms'> License </a>',

'model\_license': '<a href= 'https: //ai.google.dev/gemma/terms'> 
License </a>',

'model\_size': '6.6GB'

},

{

'name': 'CLIP',

'id': 'clip\_model',

'hf\_model\_name': 'openai/clip-vi
t-large-patch14-336',

'is\_downloaded\_required': true,

'downloaded': false,

'download\_link': 'https ://huggingface.
co/openai/clip-vit-large-patch14-336/resolve/main',

'is\_installation\_required': false,

'setup\_finished': false,

'm
in\_gpu\_memory': 8,

'should\_show\_in\_UI': true,

'prerequisite': {

'checkpoints\_files': \[

'README.md',

'config.
json',

'merges.txt',

'preprocessor\_config.json',

'pytorch\_model.bin',

'special\_tokens\_map.json',

'tokenizer.jso
n',

'tokenizer\_config.json',

'vocab.json'

\],

'checkpoints\_local\_dir': 'clip\_model'

},

'metadata': {},

'model
\_info': 'CLIP is a multi-modal vision and language model used for image-text similarity and for zero-shot image classif
ication | <a href='https ://github.c om/openai/CLIP/blob/main/LICENSE'> License </a>',

'model\_license': '<a href='http
s ://github.co m/openai/CLIP/blob/main/LICENSE'> License </a>',

'model\_size': '1.5GB'

}

\],

'selected': 'Mistral 7B
 int4',

'enable\_asr': true,

'supported\_asr': \[

{

'name': 'Whisper Medium Int8',

'installed': true,

'metadata': 
{

'encoder\_engine': 'whisper\_encoder\_float16\_tp1\_rank0.engine',

'decoder\_engine': 'whisper\_decoder\_float16\_tp
1\_rank0.engine',

'model\_path': 'model\\\\whisper\\\\whisper\_medium\_int8\_engine',

'assets\_path': 'model\\\\whispe
r\\\\whisper\_assets'

}

}

\]

},

'sample\_questions': \[

{

'query': 'How does NVIDIA ACE generate emotional respon
ses?'

},

{

'query': 'What is Portal prelude RTX?'

},

{

'query': 'What is important about Half Life 2 RTX?'

},

{


'query': 'When is the launch date for Ratchet & Clank: Rift Apart on PC?'

}

\],

'sample\_questions\_chinese': \[

{


'query': 'NVIDIA ACE是如何生成富有情感的回复的？'

},

{

'query': '传送门：序曲是什么？'

},

{

'query': '半条命 2 RTX版有什么重要意义？'

},

{

'query'
: '瑞奇与叮当：时空跳转何时会在PC平台发布？'

}

\],

'sample\_questions\_clip': \[

{

'query': 'Pictures of bicycles'

},

{

'query': 'P
ictures of toys'

},

{

'query': 'Pictures of dinosaurs'

},

{

'query': 'Pictures of computer'

}

\],

'dataset': {


'sources': \[

'directory',

'nodataset'

\],

'selected': 'directory',

'path': 'dataset',

'path\_chinese': 'chinese\
_dataset',

'path\_clip': 'images\_dataset',

'isRelative': true

},

'strings': {

'directory': 'Folder Path',

'nodata
set': 'AI model default'

}

}

\[TensorRT-LLM\] TensorRT-LLM version: 0.9.0

Privileges of app process: \['SeChangeNoti
fyPrivilege'\]

C:\\Users\\User\\AppData\\Local\\NVIDIA\\ChatRTX\\env\_nvd\_rag\\lib\\site-packages\\langchain\\chat\_mo
dels\\\_\_init\_\_.py:31: LangChainDeprecationWarning: Importing chat models from langchain is deprecated. Importing fro
m langchain will no longer be supported as of langchain==0.2.0. Please import from langchain-community instead:



\`fro
m langchain\_community.chat\_models import ChatAnyscale\`.



To install langchain-community run \`pip install -U langch
ain-community\`.

  warnings.warn(

C:\\Users\\User\\AppData\\Local\\NVIDIA\\ChatRTX\\env\_nvd\_rag\\lib\\site-packages\
\langchain\\chat\_models\\\_\_init\_\_.py:31: LangChainDeprecationWarning: Importing chat models from langchain is depre
cated. Importing from langchain will no longer be supported as of langchain==0.2.0. Please import from langchain-communi
ty instead:



\`from langchain\_community.chat\_models import ChatOpenAI\`.



To install langchain-community run \`pip
 install -U langchain-community\`.

  warnings.warn(

C:\\Users\\User\\AppData\\Local\\NVIDIA\\ChatRTX\\env\_nvd\_rag\\l
ib\\site-packages\\langchain\\embeddings\\\_\_init\_\_.py:29: LangChainDeprecationWarning: Importing embeddings from lan
gchain is deprecated. Importing from langchain will no longer be supported as of langchain==0.2.0. Please import from la
ngchain-community instead:



\`from langchain\_community.embeddings import HuggingFaceBgeEmbeddings\`.



To install la
ngchain-community run \`pip install -U langchain-community\`.

  warnings.warn(

C:\\Users\\User\\AppData\\Local\\NVIDIA
\\ChatRTX\\env\_nvd\_rag\\lib\\site-packages\\langchain\\embeddings\\\_\_init\_\_.py:29: LangChainDeprecationWarning: Im
porting embeddings from langchain is deprecated. Importing from langchain will no longer be supported as of langchain==0
.2.0. Please import from langchain-community instead:



\`from langchain\_community.embeddings import HuggingFaceEmbedd
ings\`.



To install langchain-community run \`pip install -U langchain-community\`.

  warnings.warn(

C:\\Users\\User
\\AppData\\Local\\NVIDIA\\ChatRTX\\env\_nvd\_rag\\lib\\site-packages\\langchain\\llms\\\_\_init\_\_.py:548: LangChainDep
recationWarning: Importing LLMs from langchain is deprecated. Importing from langchain will no longer be supported as of
 langchain==0.2.0. Please import from langchain-community instead:



\`from langchain\_community.llms import AI21\`.




To install langchain-community run \`pip install -U langchain-community\`.

  warnings.warn(

C:\\Users\\User\\AppData\
\Local\\NVIDIA\\ChatRTX\\env\_nvd\_rag\\lib\\site-packages\\langchain\\llms\\\_\_init\_\_.py:548: LangChainDeprecationWa
rning: Importing LLMs from langchain is deprecated. Importing from langchain will no longer be supported as of langchain
==0.2.0. Please import from langchain-community instead:



\`from langchain\_community.llms import Cohere\`.



To inst
all langchain-community run \`pip install -U langchain-community\`.

  warnings.warn(

C:\\Users\\User\\AppData\\Local\\
NVIDIA\\ChatRTX\\env\_nvd\_rag\\lib\\site-packages\\langchain\\llms\\\_\_init\_\_.py:548: LangChainDeprecationWarning: I
mporting LLMs from langchain is deprecated. Importing from langchain will no longer be supported as of langchain==0.2.0.
 Please import from langchain-community instead:



\`from langchain\_community.llms import FakeListLLM\`.



To install
 langchain-community run \`pip install -U langchain-community\`.

  warnings.warn(

C:\\Users\\User\\AppData\\Local\\NVI
DIA\\ChatRTX\\env\_nvd\_rag\\lib\\site-packages\\langchain\\llms\\\_\_init\_\_.py:548: LangChainDeprecationWarning: Impo
rting LLMs from langchain is deprecated. Importing from langchain will no longer be supported as of langchain==0.2.0. Pl
ease import from langchain-community instead:



\`from langchain\_community.llms import OpenAI\`.



To install langcha
in-community run \`pip install -U langchain-community\`.

  warnings.warn(

Using the persisted value form dataset\_vect
or\_embedding

Open HTTP s://127.0.0.1:48710?cookie=48e206cf-1b47-40a3-a517-ff7f0223f1ed&\_\_theme=dark in browser to st
art ChatRTX

Running on local URL:  HTTP s://127.0.0.1:48710

Traceback (most recent call last):

  File 'C:\\Users\\Use
r\\AppData\\Local\\NVIDIA\\ChatRTX\\env\_nvd\_rag\\lib\\site-packages\\httpx\\\_transports\\default.py', line 69, in map
\_httpcore\_exceptions

yield

  File 'C:\\Users\\User\\AppData\\Local\\NVIDIA\\ChatRTX\\env\_nvd\_rag\\lib\\site-packag
es\\httpx\\\_transports\\default.py', line 233, in handle\_request

resp = self.\_pool.handle\_request(req)

  File 'C:\
\Users\\User\\AppData\\Local\\NVIDIA\\ChatRTX\\env\_nvd\_rag\\lib\\site-packages\\httpcore\\\_sync\\connection\_pool.py'
, line 216, in handle\_request

raise exc from None

  File 'C:\\Users\\User\\AppData\\Local\\NVIDIA\\ChatRTX\\env\_nvd\
_rag\\lib\\site-packages\\httpcore\\\_sync\\connection\_pool.py', line 196, in handle\_request

response = connection.ha
ndle\_request(

  File 'C:\\Users\\User\\AppData\\Local\\NVIDIA\\ChatRTX\\env\_nvd\_rag\\lib\\site-packages\\httpcore\\\
_sync\\connection.py', line 99, in handle\_request

raise exc

  File 'C:\\Users\\User\\AppData\\Local\\NVIDIA\\ChatRTX\
\env\_nvd\_rag\\lib\\site-packages\\httpcore\\\_sync\\connection.py', line 76, in handle\_request

stream = self.\_conne
ct(request)

  File 'C:\\Users\\User\\AppData\\Local\\NVIDIA\\ChatRTX\\env\_nvd\_rag\\lib\\site-packages\\httpcore\\\_sy
nc\\connection.py', line 154, in \_connect

stream = stream.start\_tls(\*\*kwargs)

  File 'C:\\Users\\User\\AppData\\Lo
cal\\NVIDIA\\ChatRTX\\env\_nvd\_rag\\lib\\site-packages\\httpcore\\\_backends\\sync.py', line 152, in start\_tls

with m
ap\_exceptions(exc\_map):

  File 'C:\\Users\\User\\AppData\\Local\\NVIDIA\\ChatRTX\\env\_nvd\_rag\\lib\\contextlib.py',
 line 153, in \_\_exit\_\_

self.gen.throw(typ, value, traceback)

  File 'C:\\Users\\User\\AppData\\Local\\NVIDIA\\Chat
RTX\\env\_nvd\_rag\\lib\\site-packages\\httpcore\\\_exceptions.py', line 14, in map\_exceptions

raise to\_exc(exc) from
 exc

httpcore.ConnectError: \[SSL: CERTIFICATE\_VERIFY\_FAILED\] certificate verify failed: unable to get local issuer 
certificate (\_ssl.c:1007)



The above exception was the direct cause of the following exception:



Traceback (most re
cent call last):

  File 'D:\\chatrtx\\CRTX\\RAG\\trt-llm-rag-windows-ChatRTX\_0.3\\app.py', line 706, in <module>

inte
rface.render()

  File 'D:\\chatrtx\\CRTX\\RAG\\trt-llm-rag-windows-ChatRTX\_0.3\\ui\\user\_interface.py', line 426, in 
render

interface.launch(

  File 'C:\\Users\\User\\AppData\\Local\\NVIDIA\\ChatRTX\\env\_nvd\_rag\\lib\\site-packages\\
gradio\\blocks.py', line 2209, in launch

httpx.get(

  File 'C:\\Users\\User\\AppData\\Local\\NVIDIA\\ChatRTX\\env\_nvd
\_rag\\lib\\site-packages\\httpx\\\_api.py', line 198, in get

return request(

  File 'C:\\Users\\User\\AppData\\Local\
\NVIDIA\\ChatRTX\\env\_nvd\_rag\\lib\\site-packages\\httpx\\\_api.py', line 106, in request

return client.request(

  F
ile 'C:\\Users\\User\\AppData\\Local\\NVIDIA\\ChatRTX\\env\_nvd\_rag\\lib\\site-packages\\httpx\\\_client.py', line 827,
 in request

return self.send(request, auth=auth, follow\_redirects=follow\_redirects)

  File 'C:\\Users\\User\\AppData
\\Local\\NVIDIA\\ChatRTX\\env\_nvd\_rag\\lib\\site-packages\\httpx\\\_client.py', line 914, in send

response = self.\_s
end\_handling\_auth(

  File 'C:\\Users\\User\\AppData\\Local\\NVIDIA\\ChatRTX\\env\_nvd\_rag\\lib\\site-packages\\httpx
\\\_client.py', line 942, in \_send\_handling\_auth

response = self.\_send\_handling\_redirects(

  File 'C:\\Users\\Us
er\\AppData\\Local\\NVIDIA\\ChatRTX\\env\_nvd\_rag\\lib\\site-packages\\httpx\\\_client.py', line 979, in \_send\_handli
ng\_redirects

response = self.\_send\_single\_request(request)

  File 'C:\\Users\\User\\AppData\\Local\\NVIDIA\\ChatRT
X\\env\_nvd\_rag\\lib\\site-packages\\httpx\\\_client.py', line 1015, in \_send\_single\_request

response = transport.h
andle\_request(request)

  File 'C:\\Users\\User\\AppData\\Local\\NVIDIA\\ChatRTX\\env\_nvd\_rag\\lib\\site-packages\\ht
tpx\\\_transports\\default.py', line 232, in handle\_request

with map\_httpcore\_exceptions():

  File 'C:\\Users\\User
\\AppData\\Local\\NVIDIA\\ChatRTX\\env\_nvd\_rag\\lib\\contextlib.py', line 153, in \_\_exit\_\_

self.gen.throw(typ, va
lue, traceback)

  File 'C:\\Users\\User\\AppData\\Local\\NVIDIA\\ChatRTX\\env\_nvd\_rag\\lib\\site-packages\\httpx\\\_t
ransports\\default.py', line 86, in map\_httpcore\_exceptions

raise mapped\_exc(message) from exc

httpx.ConnectError: 
\[SSL: CERTIFICATE\_VERIFY\_FAILED\] certificate verify failed: unable to get local issuer certificate (\_ssl.c:1007)

P
ress any key to continue . . .


```
---

     
 
all -  [ 10k Story to 60k Novel? ](https://www.reddit.com/r/LangChain/comments/1d34r3h/10k_story_to_60k_novel/) , 2024-05-31-0910
```
I want to use AI to expand my 10,000 word story into a 60k word novel. Obviously Chat GPT doesn't offer enough tokens to
 do this, so I'm wondering, can Lang Chain combine with Chat GPT to accomplish this? I haven't used Lang Chain yet to un
derstand its capabilities yet. 

If it is possible for this to work, how complicated would it be to do?
```
---

     
 
all -  [ Kernel Memory | Deploy with a cheap infrastructure ](https://www.reddit.com/r/LangChain/comments/1d32vkw/kernel_memory_deploy_with_a_cheap_infrastructure/) , 2024-05-31-0910
```
Hello, how are you?

I am deploying a Kernel Memory service in production and wanted to get your opinion on my decision.
 Is it more cost-effective? The idea is to make it an async REST API.

- Service host: EC2 - AWS.
* Queue service: Rabbi
tMQ on the EC2 machine hosting the Kernel Memory web service.
* Storage & Vector Search: MongoDB Atlas.
* The embedding 
and LLM models used will be from OpenAI.
```
---

     
 
MachineLearning -  [ [R] Building an Observable arXiv RAG Chatbot with LangChain, Chainlit, and Literal AI ](https://www.reddit.com/r/MachineLearning/comments/1crwh0q/r_building_an_observable_arxiv_rag_chatbot_with/) , 2024-05-31-0910
```
Hey r/MachineLearning, I published a new article where I built an observable semantic research paper application.

This 
is an extensive tutorial where I go in detail about:

1. Developing a RAG pipeline to process and retrieve the most rele
vant PDF documents from the arXiv API.
2. Developing a Chainlit driven web app with a Copilot for online paper retrieval
.
3. Enhancing the app with LLM observability features from Literal AI.

You can read the article here: [https://medium.
com/towards-data-science/building-an-observable-arxiv-rag-chatbot-with-langchain-chainlit-and-literal-ai-9c345fcd1cd8](h
ttps://medium.com/towards-data-science/building-an-observable-arxiv-rag-chatbot-with-langchain-chainlit-and-literal-ai-9
c345fcd1cd8)

Code for the tutorial: [https://github.com/tahreemrasul/semantic\_research\_engine](https://github.com/tah
reemrasul/semantic_research_engine)


```
---

     
 
MachineLearning -  [ [P] LLMinator: A Llama.cpp + Gradio based opensource Chatbot to run llms locally(cpu/cuda) directly  ](https://www.reddit.com/r/MachineLearning/comments/1cpbgd1/p_llminator_a_llamacpp_gradio_based_opensource/) , 2024-05-31-0910
```
Hi I am currently working on a context-aware streaming chatbot based on Llama.cpp, Gradio, Langchain, Transformers. LLMi
nator can pull LLMs directly from HF & run them locally on cuda or cpu.

I am looking for recommendations & help from op
ensource community to grow this further.

**Github Repo:** [https://github.com/Aesthisia/LLMinator](https://github.com/A
esthisia/LLMinator)

**Goal:** To help developers with kickstarter code/tool to run LLMs.

https://preview.redd.it/fnzja
7rjwqzc1.png?width=1846&format=png&auto=webp&s=a62c43614d63e82156fef8722b986b051cc1795b

**Features:**

* Context-aware 
Chatbot.
* Inbuilt code syntax highlighting.
* Load any LLM repo directly from HuggingFace.
* Supports both CPU & Cuda m
odes.
* Load & Offload saved models.
* Command Line Args
* API Access(Soon to be available)

Any review or feedback is a
ppreciated.
```
---

     
