 
all -  [ RAG with a language that is not english ](https://www.reddit.com/r/LangChain/comments/1gya4ox/rag_with_a_language_that_is_not_english/) , 2024-11-24-0914
```
I'm trying to use langchain to build this chatbot that responds on FAQ data.

The FAQ data is really short and contains 
20 questions more or less. 

I'm struggling with embeddings and I figured out that with a similarity search I cannot ret
rieve the most similar question when the prompt contain synonyms. This is due the fact that my data source is not in eng
lish (i used a multilingual embedding model that you can find \[here\](https://huggingface.co/BAAI/bge-m3) )  
For the g
eneration step I've implemented a prompt that prevent the LLM to wonder outside the boundaries of the context and most o
f the times it respond by blocking the user question.  
From a user perspective I will be very upset if it couldnt respo
nd to my question.

I've implemented also another solution that doesn't rely on vectordb and uses the LLM (passing both 
the question and the answer of the FAQ data) but it still struggle when asking some specific questions.

Any other ideas
 in how to complete this simple project are welcome since I'm starting to doubt the feasibility of the project due to th
e poor performances
```
---

     
 
all -  [ Exfunc: API for your AI to take action on the web without a browser ](https://www.reddit.com/r/LLMDevs/comments/1gy717b/exfunc_api_for_your_ai_to_take_action_on_the_web/) , 2024-11-24-0914
```
Today, AI models can process and generate data very well but can’t use software that we use to do our work. This is larg
ely because software that we use is primarily GUI-based and requires a browser to access. We’re trying to change that wi
th [Exfunc](https://www.exfunc.com), which is an API service that your AI can use to fetch data and take action in vario
us software applications without a browser!

With just an API call, you can fetch reviews from Yelp, search properties o
n Zillow, or extract contact information from company websites. We take care of the rest from provisioning infrastructur
e to scaling browser automations. Check out our [documentation](https://docs.exfunc.com/api-reference) and [cookbooks](h
ttps://github.com/carvedai/exfunc/tree/main/cookbooks).

[You can use the chat assistant here: https:\/\/app.exfunc.com\
/chat It is built on top of assistant-ui-stockbroker: https:\/\/github.com\/Yonom\/assistant-ui-stockbroker](https://red
dit.com/link/1gy717b/video/bc06i0om5p2e1/player)

With our [agent toolkit](https://github.com/carvedai/exfunc-agent-tool
kit), you can integrate Exfunc API into your agents in a few lines of code. It supports [Vercel’s AI SDK](https://sdk.ve
rcel.ai) and [LangChain](https://www.langchain.com) and works with any LLM provider that supports function calling.

   
 import {generateText} from 'ai';
    import {openai} from '@ai-sdk/openai';
    import {ExfuncAgentToolkit} from '@exfu
nc/agent-toolkit/ai-sdk';
    
    const exfuncAgentToolkit = new ExfuncAgentToolkit({
      apiKey: process.env.EXFUNC_
API_KEY ?? '',  // This is the default and can be omitted
    });
    
    (async () => {
      const result = await gen
erateText({
        model: openai('gpt-4o-mini'),
        tools: {
          ...exfuncAgentToolkit.getTools(),
        }
,
        maxSteps: 5,
        prompt: 'get reviews for yin du wonton noodle in SF',
      });
      console.log(result.
text);
    })();

You can check out the source code of our toolkit here: [https://github.com/carvedai/exfunc-agent-toolk
it](https://github.com/carvedai/exfunc-agent-toolkit)

Key Features:

* Unified API: You can interact with many applicat
ions through our API without using a separate interface for each application. Standardization also makes it easy for AI 
to chain multiple API calls to accomplish a task (eg. sequential function calling).
* Type-safe, structured format: We p
rovide structured input and output formats and have Python and TypeScript SDKs that validate types.
* Serverless automat
ions: You don’t have to manage your own infrastructure to run browser automations.

You can sign up without a credit car
d and use it for free forever. Free tier limits should be generous enough for personal use. If you need higher limits, y
ou can message me, and I can move you to a paid plan.

API reference: [https://docs.exfunc.com/api-reference](https://do
cs.exfunc.com/api-reference)

Cookbooks: [https://github.com/carvedai/exfunc/tree/main/cookbooks](https://github.com/car
vedai/exfunc/tree/main/cookbooks)

Feel free to join our discord: [https://discord.com/invite/5TdjpyGKbq](https://discor
d.com/invite/5TdjpyGKbq)

Thanks!
```
---

     
 
all -  [ Exfunc: API for your AI to take action on the web without a browser ](https://www.reddit.com/r/LangChain/comments/1gy6vjv/exfunc_api_for_your_ai_to_take_action_on_the_web/) , 2024-11-24-0914
```
Today, AI models can process and generate data very well but can’t use software that we use to do our work. This is larg
ely because software that we use is primarily GUI-based and requires a browser to access. We’re trying to change that wi
th [Exfunc](https://www.exfunc.com), which is an API service that your AI can use to fetch data and take action in vario
us software applications without a browser!

With just an API call, you can fetch reviews from Yelp, search properties o
n Zillow, or extract contact information from company websites. We take care of the rest from provisioning infrastructur
e to scaling browser automations. Check out our [documentation](https://docs.exfunc.com/api-reference) and [cookbooks](h
ttps://github.com/carvedai/exfunc).

[You can use the chat assistant here: https:\/\/app.exfunc.com\/chat It is built on
 top of assistant-ui-stockbroker: https:\/\/github.com\/Yonom\/assistant-ui-stockbroker](https://reddit.com/link/1gy6vjv
/video/bc06i0om5p2e1/player)

With our [agent toolkit](https://github.com/carvedai/exfunc-agent-toolkit), you can integr
ate Exfunc API into your agents in a few lines of code. It supports [Vercel’s AI SDK](https://sdk.vercel.ai) and [LangCh
ain](https://www.langchain.com) and works with any LLM provider that supports function calling.

    from langchain_open
ai import ChatOpenAI
    from langgraph.prebuilt import create_react_agent
    from exfunc_agent_toolkit.langchain.toolk
it import ExfuncAgentToolkit
    
    llm = ChatOpenAI(model='gpt-4o-mini')
    
    exfunc_agent_toolkit = ExfuncAgentT
oolkit()
    
    tools = []
    tools.extend(exfunc_agent_toolkit.get_tools())
    
    langgraph_agent_executor = crea
te_react_agent(llm, tools)
    
    example_query = 'what did dalton caldwell say recently on twitter?'
    
    events 
= langgraph_agent_executor.stream(
        {'messages': [('user', example_query)]},
        stream_mode='values',
    )

    for event in events:
        event['messages'][-1].pretty_print()

You can check out the source code of our toolkit 
here: [https://github.com/carvedai/exfunc-agent-toolkit](https://github.com/carvedai/exfunc-agent-toolkit)

Key Features
:

* Unified API: You can interact with many applications through our API without using a separate interface for each ap
plication. Standardization also makes it easy for AI to chain multiple API calls to accomplish a task (eg. sequential fu
nction calling).
* Type-safe, structured format: We provide structured input and output formats and have Python and Type
Script SDKs that validate types.
* Serverless automations: You don’t have to manage your own infrastructure to run brows
er automations.

You can sign up without a credit card and use it for free forever. Free tier limits should be generous 
enough for personal use. If you need higher limits, you can message me, and I can move you to a paid plan.

Feel free to
 join our discord: [https://discord.com/invite/5TdjpyGKbq](https://discord.com/invite/5TdjpyGKbq)

Thanks!
```
---

     
 
all -  [ Applying from last 3 months but not getting interview calls  ](https://i.redd.it/zaoxv775no2e1.jpeg) , 2024-11-24-0914
```
I started looking for a job in Pune from last three months but not getting any interview calls. Few just called to ask i
nformation but no updates further. Is my resume wrong in some way? Currently im at 9LPA and asking for 30% hike, is I’m 
asking too much? I’m ok if any company match the offer in Pune. Are my expectations are too much or am I applying for th
e wrong companies? I’m applying to every company on naukri, linkedin, indeed. 
```
---

     
 
all -  [ Create a OpenAI swarm agents what are working like a label record but just for programming to reach  ](https://www.reddit.com/r/ChatGPT/comments/1gy38ci/create_a_openai_swarm_agents_what_are_working/) , 2024-11-24-0914
```
Creating a “swarm” of OpenAI agents functioning like a record label for programming is an innovative concept. Here’s a f
ramework for how you could design such a system:

Overview

This platform would manage a collective of AI agents and hum
an programmers, guiding their collaborative efforts towards achieving specific programming-related goals. Think of it as
 a talent label, but for coding and software development.

Key Components

	1.	Swarm Architecture
	•	Core Agent: The lea
der that coordinates other agents, assigns tasks, and ensures alignment with the target goals.
	•	Specialist Agents:
	•	
Frontend, Backend, AI/ML, DevOps, etc.
	•	Agents trained to excel in specific domains, analogous to artists on a record 
label.
	•	Quality Control Agents: These ensure that the output meets coding standards, is efficient, and is free of bugs
.
	2.	Human Collaborators
	•	A pool of human programmers acts as the “mentors” or “producers,” reviewing, refining, and 
expanding the output of the swarm.
	3.	Target-Oriented Design
	•	Goal Definition: A central repository where the “record
 label” (or the user) defines clear goals for a project (e.g., create a new app, optimize an algorithm, or build a platf
orm).
	•	Agent Assignments: Based on the goal, tasks are distributed among agents in parallel or sequentially.
	4.	Learn
ing & Feedback
	•	Every iteration is assessed by both AI-based quality checks and human input.
	•	Continuous learning pi
pelines allow agents to improve based on feedback.

How It Works

	1.	Project Kickoff
	•	The user submits a project idea
 and requirements (akin to a pitch for a record).
	•	The Core Agent breaks down the idea into smaller milestones.
	2.	Ta
sk Allocation
	•	Each Specialist Agent takes on a specific task (e.g., API development, UI design).
	•	Agents collaborat
e using shared models, tools, and repositories like Git.
	3.	Real-Time Collaboration
	•	Agents interact in real-time, sh
aring intermediate results and aligning on dependencies.
	•	Use of a centralized coordination platform for version contr
ol and updates.
	4.	Quality Assurance
	•	Outputs are reviewed by Quality Control Agents.
	•	Human programmers provide fi
nal reviews and adjustments, ensuring production-quality output.
	5.	Release
	•	Once polished, the project is “released”
 to the client, similar to how a record is launched.

Technological Stack

	1.	Infrastructure
	•	Cloud Services: AWS, Az
ure, or Google Cloud for hosting.
	•	Communication: APIs for inter-agent communication, message queues for task distribu
tion.
	2.	Programming Frameworks
	•	Python (for ML and orchestration).
	•	Tools like LangChain for chaining agents.
	•	G
itHub/GitLab for version control.
	3.	Learning Systems
	•	Fine-tuning GPT models for domain-specific tasks.
	•	RLHF (Rei
nforcement Learning with Human Feedback) to refine agent interactions.
	4.	Monitoring and Management
	•	Dashboards to tr
ack progress and bottlenecks.
	•	Logging mechanisms for debugging and improvements.

Benefits

	1.	Parallel Development

	•	Tasks handled simultaneously by agents, speeding up development.
	2.	Cost-Effective
	•	Reduces the need for large hum
an teams by leveraging AI.
	3.	Scalable
	•	Easily add or remove agents based on project complexity.
	4.	Talent Discovery

	•	Like a record label scouts talent, the system identifies promising programmers and AI modules.

Challenges and Solut
ions

	1.	Coordination Among Agents
	•	Solution: Implement robust communication protocols and a hierarchy of responsibil
ities.
	2.	Maintaining Code Quality
	•	Solution: Use linters, static code analyzers, and human oversight.
	3.	Avoiding R
edundancy
	•	Solution: Agents access a shared knowledge base to prevent duplication.

Would you like me to expand on any
 specific part, such as implementation details, an example use case, or a business plan?

Below is a Python-based implem
entation of a basic swarm agent framework using LangChain and asyncio for agent orchestration. This is a prototype to de
monstrate how tasks can be distributed to different agents, monitored, and combined into a single project pipeline.

Cod
e: Swarm Agent Framework

import asyncio
from langchain.agents import initialize_agent, Tool
from langchain.chat_models 
import ChatOpenAI
from langchain.prompts import PromptTemplate

# Initialize OpenAI API
openai_model = ChatOpenAI(temper
ature=0.2, model='gpt-4')

# Define specialized tools (agents for specific tasks)
def frontend_agent(task_description):

    return f'Frontend Agent: Create HTML/CSS/JS for the task: {task_description}.'

def backend_agent(task_description):

    return f'Backend Agent: Develop Python backend for the task: {task_description}.'

def devops_agent(task_descriptio
n):
    return f'DevOps Agent: Set up CI/CD pipeline for the task: {task_description}.'

# Define task manager
class Tas
kManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, agent_func, task_description):
       
 self.tasks.append((agent_func, task_description))

    async def execute_tasks(self):
        results = await asyncio.g
ather(
            *[self.run_agent(agent_func, task_description) for agent_func, task_description in self.tasks]
      
  )
        return results

    async def run_agent(self, agent_func, task_description):
        prompt = agent_func(tas
k_description)
        response = await asyncio.to_thread(lambda: openai_model.run(prompt))
        return response

# M
ain Swarm Orchestration
async def main_project_pipeline(project_goal):
    print(f'Initializing swarm for project: {proj
ect_goal}')

    # Break down project into tasks
    task_manager = TaskManager()
    task_manager.add_task(frontend_age
nt, 'Design the homepage layout')
    task_manager.add_task(backend_agent, 'Create an API endpoint for user registration
')
    task_manager.add_task(devops_agent, 'Set up Docker and deploy to AWS')

    # Execute tasks concurrently
    resu
lts = await task_manager.execute_tasks()

    # Combine and finalize results
    print('\nTask Results:')
    for i, res
ult in enumerate(results, 1):
        print(f'Task {i} Result:\n{result}\n')

    # Integration (placeholder)
    final_
output = 'Integrated Project:\n' + '\n'.join(results)
    print('Final Integrated Output:\n', final_output)

# Run the s
warm pipeline
if __name__ == '__main__':
    asyncio.run(main_project_pipeline('Build a small-scale web application'))


How It Works

	1.	Agents:
	•	Each agent function (e.g., frontend_agent, backend_agent) represents a specialized AI modul
e that works on a specific part of the project.
	•	These are simplistic placeholders; in a real system, they could use f
ine-tuned models for specific programming tasks.
	2.	Task Manager:
	•	A central orchestrator that assigns tasks to agent
s and ensures they run concurrently using asyncio.
	3.	Asynchronous Execution:
	•	All agents run their tasks in parallel
, improving efficiency.
	4.	Final Integration:
	•	Outputs from all agents are gathered and combined into a final deliver
able. This part can be expanded for more complex workflows (e.g., testing and deploying).

Output Example

When you run 
the code, it will simulate agents handling the tasks:

Initializing swarm for project: Build a small-scale web applicati
on

Task Results:
Task 1 Result:
Frontend Agent: Create HTML/CSS/JS for the task: Design the homepage layout.

Task 2 Re
sult:
Backend Agent: Develop Python backend for the task: Create an API endpoint for user registration.

Task 3 Result:

DevOps Agent: Set up CI/CD pipeline for the task: Set up Docker and deploy to AWS.

Final Integrated Output:
Frontend Ag
ent: Create HTML/CSS/JS for the task: Design the homepage layout.
Backend Agent: Develop Python backend for the task: Cr
eate an API endpoint for user registration.
DevOps Agent: Set up CI/CD pipeline for the task: Set up Docker and deploy t
o AWS.

Next Steps

To expand this framework:
	1.	Replace placeholder functions: Use actual programming logic or pre-tra
ined fine-tuned models to generate code.
	2.	Integrate GitHub API: Automate code commits, reviews, and pull requests.
	3
.	Add Testing Agent: Include an agent for automated testing (unit, integration, etc.).
	4.	Deployment Pipeline: Implemen
t a real CI/CD system using tools like Jenkins or GitHub Actions.

Would you like me to add specific functionality, like
 API integration or testing automation?
```
---

     
 
all -  [ How to make more reliable reports using AI — A Technical Guide ](https://medium.com/firebird-technologies/how-to-make-more-reliable-reports-using-ai-a-technical-guide-672b2d01cb2a) , 2024-11-24-0914
```

```
---

     
 
all -  [ Pointers on local LLM with Ollama/OpenWebUI and RAG ](https://www.reddit.com/r/LocalLLaMA/comments/1gy0z2d/pointers_on_local_llm_with_ollamaopenwebui_and_rag/) , 2024-11-24-0914
```
Hi,

I want to be able to ask a local LLM questions on my own documents. Say I have a bunch of manuals for machines and 
my own notes, I want to be able to ask 'what does error code 12 mean on machine XY'. I researched that topic and it seem
s that RAG is what I'm looking for. I also looked that up. Now it seem LangChain and Chroma-DB is are tools that can be 
used for this.

As far as I understood, you (for lack of better words) 'train' the RAG model on your files with LangChai
n, and the resulting 'model' (again, for lack of better words) gets stored on Chroma-DB for later access by whatever LLM
.

What I'd prefer was, to be able to simply drop new files in a folder, that then gets used by the LLM. I wouldn't mind
 if 'training' is a scheduled thing.

Is that correct? Can you maybe give me some advice on better solutions or point me
 to a guide you think is good? I want to deploy with Docker, in case that is important.

Thanks


```
---

     
 
all -  [ PRD Writing Agent ](https://www.reddit.com/r/AI_Agents/comments/1gxs6mm/prd_writing_agent/) , 2024-11-24-0914
```
So I've been looking to automate some of my work and one of the time-consuming parts is writing the technical PRDs which
 includes analyzing my codebase, looking for affected features/parts of the codebase and then writing out detailed chang
es needed before handing it off to other devs.

This entire flow is definitely something an agent can cover. I'm aware o
f the agent tools that I can use to achieve this. I've used Langchain for current work and thinking of using Crew or Lan
ggraph for this.

Does anyone have any existing references I can use to get started with this? Any boilerplates I can bu
ild on top of?
```
---

     
 
all -  [ Production-ready agents from APIs - built with Gradio + Arch + FastAPI + OpenAI ](https://i.redd.it/389a2dwvtk2e1.jpeg) , 2024-11-24-0914
```
https://github.com/katanemo/archgw - an intelligent proxy for agents. Transparently add tracing, safety and personalizat
ion features with APIs
```
---

     
 
all -  [ How are you monitoring/deploying your AI agents in production? ](https://www.reddit.com/r/AI_Agents/comments/1gxokte/how_are_you_monitoringdeploying_your_ai_agents_in/) , 2024-11-24-0914
```
Hi all,

We've been building agents for a while now and often run into issues trying to make them work reliably together
. We are extensively using OpenAI's tool calling for progressively complex use cases but at times it feels like we are a
dding layers of complexity without standardization. Is anyone else feeling the same?

LangChain with LangSmith has been 
helpful, but tools for debugging and deploying agents still feel lacking. Curious what others are using and what best pr
actices you're following in production:

1. **How are you deploying complex single agents in production?** *For us, it f
eels like deploying a massive monolith and scaling them has been pretty costly.*
2. **Are you deploying agents in distri
buted environments?** *It helped us, but also brought a whole new set of challenges.*
3. **How do you ensure reliable co
mmunication between agents in centralized or distributed setups?** *This is the biggest issue we face. Failures happen o
ften because there's no standardized message-passing behavior. We tried standardizing, but teams keep tweaking it, causi
ng breakages.*
4. **What tools do you use to trace requests across multiple agents?** *We’ve tried Langsmith, Openteleme
try, and others, but none feel purpose-built for this. Please do mention if you are using something else.*
5. **Any othe
r pain points in making agents work in production?** *We’re dealing with plenty of smaller issues as well.*

It feels li
ke many of these issues come from the ecosystem moving too fast. Still, simplicity in DX like deploying on DO/Vercel jus
t feels missing.

Honestly, I’m asking to understand the current state of operations and see if I can build something to
 help myself as well as others.   
  
Would really appreciate any experiences or insights you can share.
```
---

     
 
all -  [ How are you monitoring/deploying your AI agents in production? ](https://www.reddit.com/r/learnmachinelearning/comments/1gxo3fy/how_are_you_monitoringdeploying_your_ai_agents_in/) , 2024-11-24-0914
```
Hi all,

We've been building agents for a while now and often run into issues trying to make them work reliably together
. We are extensively using OpenAI's tool calling for incrementally complex use cases but at times it feels like we are a
dding layers of complexity without standardization. Is anyone else feeling the same?

LangChain with LangSmith has been 
helpful, but tools for debugging and deploying agents still feel lacking. Curious what others are using and what best pr
actices you're following in production:

1. **How are you deploying complex single agents in production?** *For us, it f
eels like deploying a massive monolith and scaling them has been pretty costly.*
2. **Are you deploying agents in distri
buted environments?** *It helped us, but also brought a whole new set of challenges.*
3. **How do you ensure reliable co
mmunication between agents in centralized or distributed setups?** *This is the biggest issue we face. Failures happen o
ften because there's no standardized message-passing behavior. We tried standardizing, but teams keep tweaking it, causi
ng breakages.*
4. **What tools do you use to trace requests across multiple agents?** *We’ve tried Langsmith, Openteleme
try, and others, but none feel purpose-built for this. Please do mention if you are using something else.*
5. **Any othe
r pain points in making agents work in production?** *We’re dealing with plenty of smaller issues as well.*

It feels li
ke many of these issues come from the ecosystem moving too fast.

Honestly, I’m asking to understand the current state o
f operations and see if there are solutions that could help me and others. Would really appreciate any experiences or in
sights you can share.
```
---

     
 
all -  [ How are you deploying your agents in production? ](https://www.reddit.com/r/LangChain/comments/1gxnse4/how_are_you_deploying_your_agents_in_production/) , 2024-11-24-0914
```
Hi all,

We've been building agents for quite some time and often face issues trying to make them work reliably together
.

LangChain with LangSmith has been extremely helpful, but the available tools for debugging and deploying agents still
 feel inadequate. I'm curious about what others are using and the best practices you're following in production:

1. **H
ow are you deploying complex single agents in production?** *For us, it feels like deploying a massive monolith, and sca
ling each one has been quite costly.*
2. **Are you deploying agents in distributed environments?** *While it has helped,
 it also introduced a whole new set of challenges.*
3. **How do you ensure reliable communication between agents in cent
ralized/distributed setups?** *This is our biggest pain point, often leading to failures due to a lack of standardized m
essage-passing behavior. We've tried standardizing it, but teams keep tweaking things, causing frequent breakages.*
4. *
*What tools are you using to trace requests across multiple agents?** We've tried Langsmith, *Opentelemetry, and others,
 but none feel purpose-built for this use case.*
5. **Any other pain points in making agents/multi-agent systems work in
 production?** *We face a lot of other smaller issues. Would love to hear your thoughts.*

I feel many agent deployment/
management issues stem from the ecosystem's rapid evolution, but that doesn't justify the lack of robust support.

Hones
tly, I'm asking this to understand the current state of operations and explore potential solutions for myself and others
. Any insights or experiences you can share would be greatly appreciated.
```
---

     
 
all -  [ blog: ChatGPT is Eating Genius, or why being smart doesn't matter anymore ](https://www.reddit.com/r/LangChain/comments/1gxmbqo/blog_chatgpt_is_eating_genius_or_why_being_smart/) , 2024-11-24-0914
```
[https://glassbead-tc.medium.com/glassbeads-blog-how-chatgpt-is-eating-genius-and-they-shall-become-providence-pt-i-0fb7
f86240e4](https://glassbead-tc.medium.com/glassbeads-blog-how-chatgpt-is-eating-genius-and-they-shall-become-providence-
pt-i-0fb7f86240e4)

I'm going to expand on this some, but this is my dev blog's second entry. It'll mostly be a LangChai
n-oriented thing, but I thought the sub might find this interesting at least.
```
---

     
 
all -  [ AI Agent + pinecone 'source citations' ](https://www.reddit.com/r/LangChain/comments/1gxkk8s/ai_agent_pinecone_source_citations/) , 2024-11-24-0914
```
I need my agent to provide 'source citations' from the chunks at the end of each answer. It is already in the 'system me
ssage' as part of the prompt but it is just ignoring it. The rest of the prompt seems to be fine.

Any suggestions? I wo
uld like to understand why is not working and how to accomplish it.

Many thanks!
```
---

     
 
all -  [ How do you run evals ? ](https://www.reddit.com/r/LangChain/comments/1gxjztm/how_do_you_run_evals/) , 2024-11-24-0914
```
Hey there
Everyone says that evals and benchmarks are the best way to radically increase the performance of a LLM based 
app. I do agree with that and what to build a solid eval architecture. 
But how do you concretely organize internally to
 run these evals ? Which tools ? Which workflows ? At which frequency ? Do you use external experts on your domain to he
lp you ? 
Would love to know :) 
```
---

     
 
all -  [ How to setup db for LangGraph PostgresSaver with FastAPI ](https://www.reddit.com/r/LangChain/comments/1gxibz5/how_to_setup_db_for_langgraph_postgressaver_with/) , 2024-11-24-0914
```
Trying to implement checkpointing with `PostgresSaver` but keep getting errors related to the db not being setup.

```
E
RROR:  relation 'checkpoints' does not exist at character 1294
```

My endpoint is just:

```
@chat_router.post('/chat/g
et-response')
def chat(
    request: Request,
    body: Body,
):
    '''Handles a chat request and calls appropriate fun
ctions based on user input.'''
    try:

        # Use the LangGraph agent to process the query
        # Initialize mem
ory to persist state between graph runs
        from langgraph.checkpoint.postgres import PostgresSaver

        DB_URI 
= f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{DB}?sslmode=disable'
        with 
PostgresSaver.from_conn_string(DB_URI) as checkpointer:
            
# Compile the graph
            checkpointer.setup(
)

            graph = graph_builder.compile(
                checkpointer=checkpointer,
            )

            fina
l_state = graph.invoke({'messages': [{'role':'human', 'content':'hi'}]})
```

Do i need to run cmds to setup beforehand?
 I'm using Alembic for migrations, tried searching everywhere for the schema but couldn't find it.

More, how do I struc
ture this so it only `.setup()`s once? Using docker. Thanks!
```
---

     
 
all -  [ My quest for ultimate laziness...Automating everything! ](https://www.reddit.com/r/LangChain/comments/1gxgke1/my_quest_for_ultimate_lazinessautomating/) , 2024-11-24-0914
```
Soo it all started about 2–3 months ago, where as a marketeer I wanted to automate a lot of my repetitive tasks and I we
nt through many solutions ranging from python codes *(too technical)* or using Zapier *(too costly)* non of that actuall
y worked out for me until I got to know that there is a new tech in the market called **Ai Agents** that does automation
s for you. Obviously I jumped on the band wagon but quickly realized it was also a complex technology which people like 
me are highly unlikely to adapt to, frustrated I wanted to give up but realized this isn't just me facing this problem a
nd people like me deserve to use this tech as well, so how can I make it simple to use? That's when I talked to my frien
d who's an ML engineer and we discussed how we can actually build something to solve this. This is where my journey to c
reate [something ](http://Wellows.com)I believe can truly change the way we work—a platform that makes automation simple
, intuitive, and impactful for everyone.  
  
Here’s the thing: automation has so much potential to save us time, reduce
 costs, and eliminate repetitive tasks. But the reality is, for many of us, it still feels like a maze—too many tools, c
onfusing interfaces, and workflows that just don’t flow....  
  
What if automation didn’t have to be so complicated??  

  
That’s the vision I’m working toward. A [space ](http://wellows.com)where:  
  
**Automation is accessible:** You do
n’t need to be a tech expert to benefit from it.  
**Workflows adapt to you:** Not the other way around.  
**Impact is m
easurable:** You can see the time and costs saved, right on your dashboard.  
  
This isn’t just about making another au
tomation tool....it’s about solving real problems for people in a way that’s meaningful and easy to use.  
  
I know it 
won’t be easy, but I’m determined to make it happen. If your down with what I'm trying to do check it out and join the [
waitlist](http://wellows.com)  

```
---

     
 
all -  [ Please review my resume and give feed back. I really appreciate your time :) ](https://www.reddit.com/r/CERN/comments/1gxaq1j/please_review_my_resume_and_give_feed_back_i/) , 2024-11-24-0914
```
https://preview.redd.it/f4b8j24b4h2e1.png?width=766&format=png&auto=webp&s=b0ba0c0e8c646de1a872593a14ebc0e55d418351




```
---

     
 
all -  [ Running LangGraph locally without Docker for desktop application integration ](https://www.reddit.com/r/LangChain/comments/1gx8g54/running_langgraph_locally_without_docker_for/) , 2024-11-24-0914
```

Hi everyone,

I'm working on an agent-based project where we need to integrate LangGraph to control a locally installed
 debugging tool. Our goal is to create an agent that can assist users with tasks like automatic configuration file gener
ation and debug automation.

**Project Requirements:**
- Run LangGraph completely locally (as part of a desktop applicat
ion installation)
- Process user input through LangGraph
- Multiple agents interact with different LLMs and tools
- Outp
ut structured results to a bridge tool that controls our local debugging application

I've gone through the LangGraph de
ployment documents and found that it always requires Docker for production. However, I'm wondering:

1. Is it possible t
o run LangGraph entirely locally without Docker?
2. Can we just use the framework directly like in the tutorials where w
e build a graph and invoke it with user input?
3. Why is there so little guidance about building agents within local des
ktop applications? Is this approach discouraged?

If Docker is required, what are the alternatives for desktop applicati
on integration?

I'm quite new to agent development, so any guidance would be greatly appreciated. Thanks in advance!


```
---

     
 
all -  [ HELP: Improve llm image processing with number “1” and “7” ](https://www.reddit.com/r/LangChain/comments/1gx7z2t/help_improve_llm_image_processing_with_number_1/) , 2024-11-24-0914
```
Hello! I’m having an issue using the GPT4o model. It gets confused when identifying the numbers 7 and 1 for a task invol
ving analyzing an order on a sheet of paper.  
I’m doing this through the OpenAI playground with a custom assistant, and
 I provide this prompt:  
  
*Instructions for Image Analysis ## Objective Perform a detailed analysis of the informatio
n contained in the image, ensuring the accurate interpretation of alphanumeric characters. ## Specific Criteria 1. Analy
ze each character carefully and precisely. 2. If you identify the number “7,” check if it has a horizontal line in the m
iddle: -* ***With a line:*** *Identify it as “7.” -* ***Without a line:*** *Interpret it as “1.” ## Accuracy Prioritize 
precision in data extraction and interpretation, ensuring the visual information is reflected as faithfully as possible.
*

https://preview.redd.it/kfd5b0l1hg2e1.png?width=1482&format=png&auto=webp&s=7e8e8264bc03873b2461e951fcfef666a5e25de0


I think that The main objective is to identify the number 7 only when it has a “line” in the middle, otherwise identify
 as 1  


in the reference image you can see that the original image(right side) has 1's and the model is reconizing it 
as 7's

If someone could suggest me about how can I improve the model, how can I use RAG for this solution  or your expe
rience and approach with similar projects. I would be very grateful.
```
---

     
 
all -  [ Reasoning behind RAGAS' metric scores ](https://www.reddit.com/r/LangChain/comments/1gx7ie5/reasoning_behind_ragas_metric_scores/) , 2024-11-24-0914
```
Hey guys, I'm using RAGAS' metrics as part of an evaluation framework.

For example, I'm using the Context Recall metric
s which might output a scoe of 0.38, but I really want to know the **reasoning** behind this score.

Is it possible for 
RAGAS to output its reasoning or some kind of verbosity a long side its score?

Appreciate any hints or help!
```
---

     
 
all -  [ Multi Agent tech stack?  ](https://www.reddit.com/r/LangChain/comments/1gx76w0/multi_agent_tech_stack/) , 2024-11-24-0914
```
The multi-agent landscape has had a couple of interesting drops in the last few days:

* **AWS's Multi-Agent Orchestrato
r** ([GitHub](https://github.com/awslabs/multi-agent-orchestrator)): Built-in multi-agent orchestration, intent classifi
cation, and support for streaming responses.
* **LangChain's Agent Protocol** ([Blog](https://blog.langchain.dev/agent-p
rotocol-interoperability-for-llm-agents/)): Aims to standardize LLM agents for interoperability across frameworks.

I’ve
 been building a lot of task specific agents for codebases (debugging, testing, Q&A, LLD etc.) at [potpie](https://potpi
e.ai/) and chose CrewAI for its ease of use. I love how simple it makes things and how it just works with the correct to
oling. But as the number of agents is growing, I am exploring ways to route requests to the right agent intelligently. I
t's also better UX. Here are the options I’m considering:

1. **CrewAI + LangGraph + Agent Protocol**: Integrate current
 agents with LangGraph for routing via Agent Protocol. This is the least amount of effort.
2. **Rebuild in LangGraph**: 
Create a classifier node and add each agent as a conditional node. It also adds first class streaming support to the age
nts which is great for UX and which Crew does not have.
3. **Switch to AWS Orchestrator**: Use AWS’s orchestration and i
ntent handling to simplify routing. Orchestration/ Intent classification is the main feature of this framework, which le
ads me to think management might be easier going ahead. But this involves the most amount of work as not just agents but
 the entire tooling will have to be redone.
4. **CrewAI’s Manager Agent**: Use CrewAI’s hierarchical processes and a cus
tom manager agent for structured task delegation. But I will still be stuck with no realtime response streaming.

I’m cu
rious if anyone has worked with these tools and features—how do they compare in terms of flexibility, scalability, and t
rade-offs? Would love to hear your thoughts! 

P.S The reason I am posting here is I am really leaning towards langgraph
, I just want to know if there are any gotchas with the framework. I've only built a small POC with it till now. 
```
---

     
 
all -  [ Guys I made so many retro ui components in my free time, now i feel like i should put these into an  ](https://www.reddit.com/r/developersIndia/comments/1gx6h9f/guys_i_made_so_many_retro_ui_components_in_my/) , 2024-11-24-0914
```
title itself skills: MERN, langchain 
```
---

     
 
all -  [ Pointers on local LLM with Ollama/OpenWebUI and RAG ](https://www.reddit.com/r/selfhosted/comments/1gx6gx3/pointers_on_local_llm_with_ollamaopenwebui_and_rag/) , 2024-11-24-0914
```
Hi,



I want to be able to ask a local LLM questions on my own documents. Say I have a bunch of manuals for machines an
d my own notes, I want to be able to ask 'what does error code 12 mean on machine XY'. I researched that topic and it se
ems that RAG is what I'm looking for. I also looked that up. Now it seem LangChain and Chroma-DB is are tools that can b
e used for this.



As far as I understood, you (for lack of better words) 'train' the RAG model on your files with Lang
Chain, and the resulting 'model' (again, for lack of better words) gets stored on Chroma-DB for later access by whatever
 LLM.



What I'd prefer was, to be able to simply drop new files in a folder, that then gets used by the LLM. I wouldn'
t mind if 'training' is a scheduled thing.



Is that correct? Can you maybe give me some advice on better solutions or 
point me to a guide you think is good? I want to deploy with Docker, in case that is important.



Thanks
```
---

     
 
all -  [ Guys I made so many retro ui components in my free time, now i feel like i should put these into an  ](https://www.reddit.com/r/SaaS/comments/1gx6g8z/guys_i_made_so_many_retro_ui_components_in_my/) , 2024-11-24-0914
```
title itself

skills: MERN, langchain 
```
---

     
 
all -  [ Help Needed Software engineer Resume Review ](https://www.reddit.com/r/arbeitsleben/comments/1gx6fy3/help_needed_software_engineer_resume_review/) , 2024-11-24-0914
```
Ich bin Masterstudent in Deutschland mit einiger Berufserfahrung, habe meine Diplomarbeit abgeschlossen und suche nach J
obs. Ich habe Lebensläufe verschickt, aber keine Rückrufe erhalten. Kann jemand meinen Lebenslauf überprüfen und mir ein
ige Vorschläge machen?

https://preview.redd.it/9kt7jn7m2g2e1.png?width=550&format=png&auto=webp&s=588eab770b6f5cf25ba3a
467b882e605b60c368c

https://preview.redd.it/aztapxfp2g2e1.png?width=547&format=png&auto=webp&s=b1eb4e02021163b41ca51ab8
b7d9092a849a0e85
```
---

     
 
all -  [ Need building app like perplexity ](https://www.reddit.com/r/Rag/comments/1gx44lr/need_building_app_like_perplexity/) , 2024-11-24-0914
```
Hey guys, i have built an app like perlexity. It can browse internet and answers. The thing is perplexity is too fast an
d even blackbox is also v fast. 

How are you they getting this much speed i mean my llm inferencing also fast i am usin
g groq for inference. But now two main components are scraper and vector database. 

right now i am using chromadb and o
penai embeddings for vectordb operations. And i am using webbasedloader from langchain for webscraping. 

now i think i 
can improve on vectordb and embeddings ( but i think openai embeddings is fast enough) 

I need suggestions on using vec
tordb i want to know what these companies like perplexity, blackbox uses. 

I want to make mine as fast as them
```
---

     
 
all -  [ Guys Review my resume and suggest me changes required (this resume not getting through) ](https://i.redd.it/vc5gubdl4f2e1.jpeg) , 2024-11-24-0914
```
Guys pls review my resume any type of insight would be helpful!
```
---

     
 
all -  [ LangChain context switching chatbot ](https://www.reddit.com/r/LangChain/comments/1gx1o3v/langchain_context_switching_chatbot/) , 2024-11-24-0914
```


I'm reviewing a LangChain agent that manages an AI conversation system using Langchain legacy AgentExecutor, but facin
g some issues like high latencies, non deterministic nature, any comments on how i can improve the architecture itself?


The system handles the following functionalities:

1. **User Message Processing**: Incoming user messages are processed
 using GPT-4 as the core LLM.
2. **Memory Management**: The agent uses a conversation memory system limited to the last 
*n* messages to maintain context.
3. **Module-Oriented Flow**:
   * **Modules as Functional Units**: Each conversation f
low is divided into multiple interconnected modules (e.g., M1, M2, M3).
   * **Module Instructions**: Each module contai
ns detailed instructions (ranging from 500–1,000 lines) specifying its functional behavior. For example, **M1 (Authentic
ation)** might include instructions like:
      * 'Verify user credentials.'
      * 'Handle scenarios where users provi
de invalid data.'
      * 'Escalate to human support if required.'
   * **Module Connections via Edges**: Edges connect 
modules and contain transition instructions. For instance, the edge connecting M1 → M2 might state:
      * 'If the user
 has successfully authenticated, proceed to M2 (Data Retrieval).'
      * 'If authentication fails, transition to M3 (Er
ror Handling).'
4. **Module Switching with Tools**:
   * A default tool is passed to each module to evaluate transition 
logic dynamically.
   * Upon deciding the next module (e.g., transitioning from M1 → M2), the system:
      * Updates th
e system prompt with M2's instructions.
      * Removes M1’s instructions and related history from the context to reduce
 complexity.
   * This design supports an unlimited number of modules, enabling flexible workflows.

# Problems Identifi
ed:

1. **High Latency**:
   * Due to the large volume of instructions per module (\~500–1,000 lines), GPT-4 calls often
 result in latencies of **3–6 seconds** per interaction.
   * For example, in M1, when verifying user credentials and ha
ndling multiple contingencies, the model processes extensive context, leading to slow responses.
2. **Non-Deterministic 
Module Switching**:
   * The default tool occasionally fails to produce consistent transitions between modules.
   * Exa
mple: A user completes M1 (Authentication), but instead of reliably moving to M2, the system sometimes loops back or sel
ects an incorrect module like M3.
3. **Instruction Overload within Modules**:
   * The model struggles to perform all th
e tasks specified in a module due to the extensive instruction set.
   * Example: In M1, if the instructions include 've
rify user credentials,' 'handle invalid attempts,' and 'provide detailed error feedback,' the bot might only complete on
e or two tasks, leaving others unaddressed.

# 


```
---

     
 
all -  [ Customer Support Evolution Tracker: AI-Powered Support Quality Analysis 🎯 ](https://www.reddit.com/r/ArtificialMoney/comments/1gx11k7/customer_support_evolution_tracker_aipowered/) , 2024-11-24-0914
```
Let's build an intelligent system that tracks how customer support conversations evolve and improve over time. This AI-p
owered platform will analyze support interactions, identify patterns in resolution strategies, and help teams continuous
ly improve their customer service quality. Think of it as a 'fitness tracker' for your support team's performance and gr
owth.

## 😫 Problem
Customer support teams often struggle to maintain consistency and track genuine improvement in their
 service quality. While traditional metrics like response time and customer satisfaction scores provide some insight, th
ey don't tell the whole story. Teams lack visibility into how their conversation strategies evolve, which approaches wor
k best for different types of issues, and whether their responses are becoming more effective over time.

Moreover, supp
ort managers find it challenging to:
* Identify which team members excel at handling specific types of issues
* Track th
e evolution of response strategies across different channels
* Measure the actual impact of training initiatives
* Ensur
e consistent tone and approach across the entire team

## ✨ Solution
Our system will use natural language processing and
 machine learning to create a comprehensive support quality analytics platform. Rather than just tracking basic metrics,
 we'll provide deep insights into conversation patterns, resolution effectiveness, and team evolution.

Key features wil
l include:
* Conversation flow analysis to identify successful resolution patterns
* Automatic detection of tone, empath
y, and professionalism in responses
* Topic clustering to understand common issue patterns
* Historical trending to trac
k improvement in handling similar issues
* AI-powered suggestions for response improvements
* Team learning recommendati
ons based on successful interactions

The platform will not only track metrics but actively suggest improvements. For in
stance, it might notice that certain phrasing leads to better customer satisfaction scores and recommend similar approac
hes to other team members. It could also identify gaps in knowledge base coverage based on recurring questions.

## 🎯 Ta
rget Users
Our platform serves multiple stakeholders in the customer support ecosystem:

* Support Team Leaders: Get ins
ights into team performance and identify training opportunities
* Individual Support Agents: Receive personalized feedba
ck and improvement suggestions
* Quality Assurance Teams: Track consistency and compliance across interactions
* Product
 Teams: Understand customer pain points and feature requests through support data
* Business Analysts: Access trend data
 to inform strategic decisions

## 💰 Monetization Strategy
We'll implement a usage-based pricing model with tiered featu
res:

* Starter: Basic analytics and individual agent tracking
* Professional: Advanced team analytics, AI suggestions, 
and integration capabilities
* Enterprise: Custom reporting, API access, and dedicated support

Additional revenue strea
ms can include:
* Custom model training for specific industry vocabularies
* Integration services for enterprise clients

* Consulting services for support team optimization

## 🛠️ Implementation Approach
The system requires sophisticated na
tural language processing capabilities combined with scalable data processing. Here's our recommended technical stack:


* Cloud Infrastructure
  * AWS for core infrastructure and scalability
  * Docker containers orchestrated with Kubernete
s
  * Fly.io for edge deployment of analysis services

* Backend Services
  * FastAPI for main application server
  * Ra
bbitMQ for message queuing
  * Redis (via Upstash) for caching and real-time analytics

* Data Storage
  * PostgreSQL (v
ia Supabase) for structured data
  * Vector database for semantic search capabilities
  * S3 for conversation archive st
orage

* AI/ML Pipeline
  * Hugging Face for NLP model hosting
  * TensorFlow for custom model training
  * LangChain fo
r LLM orchestration

* Frontend
  * Next.js for web interface
  * React Native for mobile app
  * Vercel for frontend de
ployment

* Integration APIs
  * REST APIs for basic integration
  * GraphQL for complex data queries
  * Webhook suppor
t for real-time updates

## 🔒 Privacy and Security
Given the sensitive nature of customer support data, security is para
mount. We'll implement:

* End-to-end encryption for all support conversations
* Automatic PII detection and redaction
*
 Role-based access control with detailed audit logs
* Compliance with GDPR, CCPA, and other relevant regulations
* Regul
ar penetration testing and security audits

## 🚀 Development Phases

### Phase 1: Foundation
* Basic conversation analys
is pipeline
* Essential metrics tracking
* Simple dashboard for insights

### Phase 2: Intelligence Layer
* AI-powered c
onversation analysis
* Pattern recognition
* Initial recommendation engine

### Phase 3: Advanced Features
* Custom mode
l training capabilities
* Advanced team analytics
* Integration framework

### Phase 4: Enterprise Features
* Custom rep
orting
* Advanced compliance features
* White-label options

## 🎯 Future Potential
The platform can evolve in several ex
citing directions:

* Predictive analytics for support volume and resource planning
* Automated quality assurance and co
mpliance checking
* Integration with CRM and help desk platforms
* Support for voice and video interaction analysis
* Re
al-time coaching suggestions during live conversations

## 💭 Discussion Points
Let's explore some key considerations:

*
 How do we balance automated analysis with human judgment in support quality assessment?
* What's the right mix of quant
itative metrics and qualitative insights?
* How can we ensure the system promotes genuine improvement rather than 'gamin
g' metrics?
* What role should AI play in real-time support interactions?

Share your thoughts and experiences in the co
mments below! 💬

Would you use a system like this to improve your support team's performance? What features would be mos
t valuable to you? Let's discuss! 👇
```
---

     
 
all -  [ how does v0 work ](https://www.reddit.com/r/LangChain/comments/1gwt9i9/how_does_v0_work/) , 2024-11-24-0914
```
how do tools like v0 actually get built from scratch? are the llms fine-tuned on something like shadcn and different exa
mples?

i’ve been trying to build something similar but for a different ui library and running into issues with hallucin
ations. the workflow i’m following is:

enhance query -> choose_components -> generate_code (based on example code from 
the library) -> enhance_ui

but the llm often hallucinates components or just generates completely off outputs. is fine-
tuning the only way to fix this? or is there another way to handle these hallucinations?

```
---

     
 
all -  [ How expensive are lambda layers? ](https://www.reddit.com/r/aws/comments/1gws5id/how_expensive_are_lambda_layers/) , 2024-11-24-0914
```
I am storing langchain module on lambda layers it is about 250mb.

Should i be worried about aws charging me?

It is a b
asic library for what i am doing
```
---

     
 
all -  [ Langchain for audiovisual experiences: Mediachain ](https://www.reddit.com/r/moviepy/comments/1gws02u/langchain_for_audiovisual_experiences_mediachain/) , 2024-11-24-0914
```
A few months ago, I started working on TurboReel, an automation tool for generating short videos 100x faster. It was bui
lt with MoviePy and OpenAI. While MoviePy is great for basic tasks, I found it limiting for more complex ones. Plus, I r
elied too heavily on OpenAI, which made it tricky to keep improving the project.

We ended up using Revideo for the vide
o processing tasks.

That made me realize that AI tools should be separated from the video engine(MoviePy, Revideo, Remo
tion, etc.) or AI service(GPT, ElevenLabs, Dalle, Runway, Sora, etc.) you choose to use. So you can easily switch betwee
n the best out there.

Also, there is no hub for audiovisual generation knowledge. So this is my attempt to create that 
hub.

Mediachain repo: [https://github.com/TurboReel/mediachain](https://github.com/TurboReel/mediachain)
```
---

     
 
all -  [ Langchain for visual experiences: Mediachain ](https://www.reddit.com/r/LangChain/comments/1gwrxqx/langchain_for_visual_experiences_mediachain/) , 2024-11-24-0914
```
A few months ago, I started working on [TurboReel](http://turboreelgpt.tech), an automation tool for generating short vi
deos 100x faster. It was built with MoviePy and OpenAI. While MoviePy is great for basic tasks, I found it limiting for 
more complex ones. Plus, I relied too heavily on OpenAI, which made it tricky to keep improving the project.

We ended u
p using Revideo for the video processing tasks.

That made me realize that AI tools should be separated from the video e
ngine(MoviePy, Revideo, Remotion, etc.) or AI service(GPT, ElevenLabs, Dalle, Runway, Sora, etc.) you choose to use. So 
you can easily switch between the best out there.

Also, there is no hub for audiovisual generation knowledge. So this i
s my attempt to create that hub.

Mediachain repo: [https://github.com/TurboReel/mediachain](https://github.com/TurboRee
l/mediachain)
```
---

     
 
all -  [ In langgraph, is there a way to route to two different toolnodes 'simultaniously'? (given a single A ](https://www.reddit.com/r/LangChain/comments/1gwp9bu/in_langgraph_is_there_a_way_to_route_to_two/) , 2024-11-24-0914
```
So, my situation is as follows:

I have an assistant node with access to some tools, some of which return sensitive info
rmation. To treat this sensitive information properly, I have created two tool nodes, namely 'safe\_tools\_node' and 'se
nsitive\_tools\_node', and a router function to point to the right node depending on the tool call needed.

This works f
ine if all of the tool calls point to the same node, but as soon as the Assistant requests say, a tool call from the saf
e node and also a tool call from the sensitive node, I don\`t know how to accomplish this.

  
Is there a way for me to 
maintain this segregation but also ensure that every tool is called?
```
---

     
 
all -  [ Best option using LoRA fine-tuning open-source LLMs for a corporate?  ](https://www.reddit.com/r/LLMDevs/comments/1gwoqro/best_option_using_lora_finetuning_opensource_llms/) , 2024-11-24-0914
```
I am doing research on using LoRA fine-tuning with open-source LLMs for my company.  
Currently, they use AWS BedRock wi
th RAG and the inference time is too slow. 

What are the options if I want to use LoRA fine-tuning with open-source LLM
s for business purposes (like internal LLMs)?

My input formats would be docx, pdf, xlsx, etc.

Library: Langchain, Hugg
ingFace, or others?  
Models: Llama 3.1, Mistral 7B, or others?
```
---

     
 
all -  [ [New Feature Launch] Searching & Favoriting ](https://www.reddit.com/r/u_youdotcom_/comments/1gwncx3/new_feature_launch_searching_favoriting/) , 2024-11-24-0914
```
Ask and you shall receive . . . We’re thrilled to introduce the launch of our most requested features: Searching & Favor
iting. ⭐️Favorite your important threads with just a click and 🔍Search effortlessly across all your old conversations.


Productivity: Leveled up 🚀

https://preview.redd.it/zrno4eoh9b2e1.jpg?width=1700&format=pjpg&auto=webp&s=33a1ee17bfe5810
2ec99a55a107dc1ab4f999ea4


```
---

     
 
all -  [ LangGraph with DSPy ](https://www.reddit.com/r/LangGraph/comments/1gwl1he/langgraph_with_dspy/) , 2024-11-24-0914
```
Is anyone using this combination of LangGraph and DSPy?  I started with pure LangGraph for the graph/state/workflow desi
gn and orchestration and integrated LangChain for the LLM integration. However, that still required a lot of “traditiona
l” prompt engineering. 

DSPy provides the antidote to prompt design and I started integrating it into my LangGraph proj
ect (replacing LangChain integration). I haven’t gone too deep yet so before I do I wanted to check if anyone else has g
one down this path and are any “Danger Will Robinson” things I should know about. 

Thanks y’all!

```
---

     
 
all -  [ [Student] Final year student. Can't land a single interview. Will appreciate any feedback. ](https://www.reddit.com/r/EngineeringResumes/comments/1gwju3s/student_final_year_student_cant_land_a_single/) , 2024-11-24-0914
```
Hi. As the title says, I'm in my final year of my software engineering degree. I'm aiming for entry level Machine Learni
ng Engineer roles. However, I've applied to hundreds of internships/part time jobs, and yet I have not even received a s
ingle reply or a call for even an initial interview. I can only assume my resume is not making past the screening stage.


I'm located in Pakistan, and I'm applying to jobs and internships in my city as well as remote jobs. I've good a reall
y solid CGPA, and I feel I have a good portfolio of projects to showcase. I'm also studying from one of the top universi
ties of my country (especially in IT). I've also got some ML experience working as a paid research assistant at my unive
rsity, which I am currently doing. The selection for this role was through an interview process. In this role, I am basi
cally working with computer vision techniques and deep learning models. I thought this would make me stand out since the
re are less than 10 students in my university who are working in research, but it seems it does not. Recently, I receive
d an email about an opportunity for a Machine Learning Intern role opening for final year students at a software company
, which is 1km from my house. It's a well structured company, and I was aiming to work there after my degree, and did no
t expect that they'd hire interns. I sent my application, and asked a friend who works there as a Machine Learning Engin
eer to refer me. But, I never got an interview. Infact, the friend told me that they are only hiring from my university,
 and was surprised that they never even called me once. After this, I came here hoping to get some advice on my resume, 
as I am desperately in need of work due to my family's financial problems. I'm afraid that if I can't start with any com
pany now as an intern, the companies won't have any jobs left to give, since they'll offer the jobs to the interns who a
re already working with them.

The unity development internship I did during the summer was at the only company who call
ed me when I applied to hundreds of companies for an internship. I did it for the sole reason that I didn't get a call f
rom any other company, not even for an interview. I initially had my phone number removed from my resume, but I have add
ed it now, since the game development company contacted me through a cold call, and I figured my phone number should be 
accessible if that's how companies contact potential employees.

All I want is to get an initial interview at least. I k
now I can make a really good impression, but I feel like my resume might not be making it there somehow. Even if I don't
 get in after the interview, at least I'll know I got my chance.

Please review my resume. I've changed the sensitive in
formation with text that would indicate what would be there. Any feedback would be appreciated.

https://preview.redd.it
/smb4u0vvaa2e1.png?width=4961&format=png&auto=webp&s=3c0dfdc54dba3fccfa35db2146a17fd783472512
```
---

     
 
all -  [ If anyone from Langchain team is reading this: STOP EVERYTHING and JUST UPDATE AND ORGANISE THE DOCS ](https://www.reddit.com/r/LangChain/comments/1gwh09x/if_anyone_from_langchain_team_is_reading_this/) , 2024-11-24-0914
```
I know very many people who just give up on this framework. It's supposed to be easy for people with average or low codi
ng experience. You are building the product for experienced devs who could even build agents without using langgraph or 
langchain.

It should be so easy, you could pass well organised docs to Cursor for example and you could create agent wo
rkflows with simple logic and commands. But the docs are so confusing, 0 organisation and you need to do so much searchi
ng and finding your own way to use the framework.
```
---

     
 
all -  [ What If Automation Was Actually… Effortless? ](https://www.reddit.com/r/LangChain/comments/1gwegx9/what_if_automation_was_actually_effortless/) , 2024-11-24-0914
```
After all the amazing input on my [last post](https://www.reddit.com/r/LangChain/comments/1gshuh5/why_are_ai_agent_tools
_so_complex_thinking_of_a/), one thing is crystal clear: automation tools are still not as accessible, seamless, or intu
itive as they need to be. There’s so much potential for these tools to revolutionize how we work, but the complexity kee
ps holding people back.

It’s got me thinking—what if automation didn’t feel like a second job to set up? What if there 
was a solution designed to make things truly effortless for everyone, not just developers or tech-savvy teams?

Here’s t
he kind of tool I’ve been envisioning (and, full disclosure, I’m working on [something](http://wellows.com/) to tackle t
hese exact challenges):

**1. A Single, Intuitive Platform for All Automation Needs**

Imagine having everything—AI tool
s, workflows, and integrations—accessible in one place, but without the overwhelming learning curve. No endless tabs, no
 piecing together different systems, just one clean, user-friendly platform.

*Would this kind of simplicity be a game-c
hanger for you?*

**2. Automation That Adjusts to You**

What if the tool actually adapted to your workflow instead of t
he other way around? Whether it’s a small business needing basic time-saving workflows or a SaaS team looking for powerf
ul AI-driven automation, the system should scale with you.

*Does customization without complexity feel like a missing p
iece for you?*

**3. Real-Time Metrics to Prove It’s Working**

One thing I keep hearing is how hard it is to know wheth
er your automation efforts are really making an impact. Imagine a dashboard that gives you real-time insights into time 
saved, processes improved, and costs cut—all without any manual tracking.

*Would having measurable results motivate you
 to embrace automation fully?*

**4. Built for Everyone—Not Just Tech Experts**

I think the biggest barrier is making a
utomation tools that anyone can use, from small business owners to marketing teams, without requiring a tech background.
 What if all it took to set up a workflow was answering a few simple prompts?

I’m working on a [product ](http://wellow
s.com/)that aims to solve all of these pain points, and I’d love to hear your thoughts. What’s the one thing that would 
make automation actually work for you?

If this sounds like something you’d want to explore, drop a comment or message m
e—I’m all ears. Let’s build a future where automation really is as simple as it promises to be.
```
---

     
 
all -  [ best LLMs with balance of performance/size for a command-line agent? & is LangChain a good usecase f ](https://www.reddit.com/r/LangChain/comments/1gwe546/best_llms_with_balance_of_performancesize_for_a/) , 2024-11-24-0914
```
I want to run an LLM on google colabs free tier GPUs that can I can give strict SSH access to my local machine to test t
hat it can translate and execute bash commands from my natural language prompts.

Also interested to hear what are the b
est examples of this command-line bridge ai-use that already exist, and whether or not the best approach is just to use 
one of the big models' APIs (running the LLM in cloud was for more personal learning experience).

And generally peoples
 thoughts on the idea. I think it will be useful for me because you can probably whack some speech-to-text on there and 
achieve super-user/turbo-accessibility of your machine.

Also I feel like this is not really as complicated as many of t
he applications of LangChain - is this a good framework for the idea? I dont intend to define/limit all the bash functio
ns the agent can use, and theres only 1 agent, and no need for scaling.
```
---

     
 
all -  [ OpenAI Privacy policy  ](https://www.reddit.com/r/LangChain/comments/1gwdhw5/openai_privacy_policy/) , 2024-11-24-0914
```
I am developing an app for a CRM client that uses a proprietary database with customer and sales data. They’re exploring
 a conversational AI interface, like OpenAI's ChatGPT, to enable users to query the database naturally.



The plan is t
o integrate this feature into platforms like WhatsApp. However, the client is concerned about protecting their proprieta
ry data and ensuring it isn’t exposed or incorporated into OpenAI’s training models.



Could you provide guidance on sa
feguards or best practices to address this concern? Thank you
```
---

     
 
all -  [ A prompt management tool for teams that allows business people to create better AI prompts while dev ](https://www.reddit.com/r/LangChain/comments/1gwciqh/a_prompt_management_tool_for_teams_that_allows/) , 2024-11-24-0914
```
Over the past year, I've been on an interesting journey integrating AI into various products. One pattern kept emerging:
 while technical teams could handle the implementation, business stakeholders wanted to be actively involved in crafting
 and optimizing AI prompts. But making prompt changes meant constant redeployments - not ideal.

This challenge led me t
o build Promptmgr - a collaborative platform where both technical and business teams can work together on AI prompts. Th
ink of it as 'Git for prompts' but with a user-friendly interface that non-developers can actually use.

Key features in
clude:

* Interactive playground for real-time testing
* Support for OpenAI, Anthropic, and other leading AI models
* Bu
ilt-in versioning and rollback capabilities
*  Advanced templating with conditional logic
* Performance monitoring and c
ross-model comparisons

We've been using it with clients for about a month now, and the feedback has been incredible. Te
ams love being able to iterate on prompts without depending on engineering for every change.

I'd love to hear your thou
ghts! There's a demo account available if you'd like to try it out: [https://www.promptmgr.com](https://www.promptmgr.co
m)

What features would you find most valuable in a tool like this?
```
---

     
 
all -  [ LLM noob here, requesting help on embeddings, langchain ](https://www.reddit.com/r/ollama/comments/1gwbyen/llm_noob_here_requesting_help_on_embeddings/) , 2024-11-24-0914
```
Hi all, I am new to LLMs and still learning about the different concepts. I was going through some of the tutorials on f
ine-tunings, RAGs, etc. 

Almost 80% of the tutorials out there are using langchains, hugging-face and other services. M
y question is what is the real purpose of “Langchain” and services such as hugging face? 

Can’t I leverage the embed me
thod in the ollama SDK to create the embeddings?

Happy to go through any documentations/blogs if required.
```
---

     
 
all -  [ Langchain Async, how's it working behind the scenes? ](https://www.reddit.com/r/LangChain/comments/1gwakj2/langchain_async_hows_it_working_behind_the_scenes/) , 2024-11-24-0914
```
Alright, I apologise if this is a dumb question but here goes.

From what I understand, going from a synchronous call to
 a asynchronous one just needs us to go from `output = chain.batch(inputs)` to `output = await chain.abatch(inputs)`.

B
ut how does this actually lead to any improvements? Are we not just sending out a asynchronous task and then immediately
 waiting for it to finish without doing any work in the meantime?

What am I missing?
```
---

     
 
MachineLearning -  [ [P] Open-source declarative framework to build LLM applications - looking for contributors ](https://www.reddit.com/r/MachineLearning/comments/1gkpazh/p_opensource_declarative_framework_to_build_llm/) , 2024-11-24-0914
```
I've been building LLM-based applications, and was super frustated with all major frameworks - langchain, autogen, crewA
I, etc. They also seem to introduce a pile of unnecessary abstractions. It becomes super hard to understand what's going
 behind the curtains even for very simple stuff.

[So I just published this open-source framework GenSphere.](https://gi
thub.com/octopus2023-inc/gensphere) The idea is have something like **Docker for LLMs**. You build applications with YAM
L files, that define an execution graph. Nodes can be either LLM API calls, regular function executions or other graphs 
themselves. Because you can nest graphs easily, building complex applications is not an issue, but at the same time you 
don't lose control.

You basically code in YAML, stating what are the tasks that need to be done and how they connect. O
ther than that, you only write individual python functions to be called during the execution. No new classes and abstrac
tions to learn.

Its all open-source. **Now I'm looking for contributors** to adapt the framework for cycles and conditi
onal nodes - which would allow full-fledged agentic system building! Pls reach out  if you want to contribute, there are
 tons of things to do!

PS: [you can read the detailed docs here,](https://gensphere.readthedocs.io/en/latest/) And go o
ver this quick [Google Colab tutorial.](https://github.com/octopus2023-inc/gensphere/blob/main/examples/gensphere_tutori
al.ipynb)
```
---

     
 
deeplearning -  [ Fast AI's deep learning for coders by jeremy howard for begginer?  ](https://www.reddit.com/r/deeplearning/comments/1gb2k3p/fast_ais_deep_learning_for_coders_by_jeremy/) , 2024-11-24-0914
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

     
