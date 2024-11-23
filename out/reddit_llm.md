 
all -  [ blog: ChatGPT is Eating Genius, or why being smart doesn't matter anymore ](https://www.reddit.com/r/LangChain/comments/1gxmbqo/blog_chatgpt_is_eating_genius_or_why_being_smart/) , 2024-11-23-0914
```
[https://glassbead-tc.medium.com/glassbeads-blog-how-chatgpt-is-eating-genius-and-they-shall-become-providence-pt-i-0fb7
f86240e4](https://glassbead-tc.medium.com/glassbeads-blog-how-chatgpt-is-eating-genius-and-they-shall-become-providence-
pt-i-0fb7f86240e4)

I'm going to expand on this some, but this is my dev blog's second entry. It'll mostly be a LangChai
n-oriented thing, but I thought the sub might find this interesting at least.
```
---

     
 
all -  [ AI Agent + pinecone 'source citations' ](https://www.reddit.com/r/LangChain/comments/1gxkk8s/ai_agent_pinecone_source_citations/) , 2024-11-23-0914
```
I need my agent to provide 'source citations' from the chunks at the end of each answer. It is already in the 'system me
ssage' as part of the prompt but it is just ignoring it. The rest of the prompt seems to be fine.

Any suggestions? I wo
uld like to understand why is not working and how to accomplish it.

Many thanks!
```
---

     
 
all -  [ How do you run evals ? ](https://www.reddit.com/r/LangChain/comments/1gxjztm/how_do_you_run_evals/) , 2024-11-23-0914
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

     
 
all -  [ How to setup db for LangGraph PostgresSaver with FastAPI ](https://www.reddit.com/r/LangChain/comments/1gxibz5/how_to_setup_db_for_langgraph_postgressaver_with/) , 2024-11-23-0914
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

     
 
all -  [ My quest for ultimate laziness...Automating everything! ](https://www.reddit.com/r/LangChain/comments/1gxgke1/my_quest_for_ultimate_lazinessautomating/) , 2024-11-23-0914
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

     
 
all -  [ How can I create a Chat with JSON application with Langchain to chat with 3 json files ](https://www.reddit.com/r/LangChain/comments/1gxd7w6/how_can_i_create_a_chat_with_json_application/) , 2024-11-23-0914
```

```
---

     
 
all -  [ Please review my resume and give feed back. I really appreciate your time :) ](https://www.reddit.com/r/CERN/comments/1gxaq1j/please_review_my_resume_and_give_feed_back_i/) , 2024-11-23-0914
```
https://preview.redd.it/f4b8j24b4h2e1.png?width=766&format=png&auto=webp&s=b0ba0c0e8c646de1a872593a14ebc0e55d418351




```
---

     
 
all -  [ Running LangGraph locally without Docker for desktop application integration ](https://www.reddit.com/r/LangChain/comments/1gx8g54/running_langgraph_locally_without_docker_for/) , 2024-11-23-0914
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

     
 
all -  [ HELP: Improve llm image processing with number “1” and “7” ](https://www.reddit.com/r/LangChain/comments/1gx7z2t/help_improve_llm_image_processing_with_number_1/) , 2024-11-23-0914
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

     
 
all -  [ Reasoning behind RAGAS' metric scores ](https://www.reddit.com/r/LangChain/comments/1gx7ie5/reasoning_behind_ragas_metric_scores/) , 2024-11-23-0914
```
Hey guys, I'm using RAGAS' metrics as part of an evaluation framework.

For example, I'm using the Context Recall metric
s which might output a scoe of 0.38, but I really want to know the **reasoning** behind this score.

Is it possible for 
RAGAS to output its reasoning or some kind of verbosity a long side its score?

Appreciate any hints or help!
```
---

     
 
all -  [ Multi Agent tech stack?  ](https://www.reddit.com/r/LangChain/comments/1gx76w0/multi_agent_tech_stack/) , 2024-11-23-0914
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

     
 
all -  [ Guys I made so many retro ui components in my free time, now i feel like i should put these into an  ](https://www.reddit.com/r/developersIndia/comments/1gx6h9f/guys_i_made_so_many_retro_ui_components_in_my/) , 2024-11-23-0914
```
title itself skills: MERN, langchain 
```
---

     
 
all -  [ Pointers on local LLM with Ollama/OpenWebUI and RAG ](https://www.reddit.com/r/selfhosted/comments/1gx6gx3/pointers_on_local_llm_with_ollamaopenwebui_and_rag/) , 2024-11-23-0914
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

     
 
all -  [ Guys I made so many retro ui components in my free time, now i feel like i should put these into an  ](https://www.reddit.com/r/SaaS/comments/1gx6g8z/guys_i_made_so_many_retro_ui_components_in_my/) , 2024-11-23-0914
```
title itself

skills: MERN, langchain 
```
---

     
 
all -  [ Help Needed Software engineer Resume Review ](https://www.reddit.com/r/arbeitsleben/comments/1gx6fy3/help_needed_software_engineer_resume_review/) , 2024-11-23-0914
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

     
 
all -  [ Need building app like perplexity ](https://www.reddit.com/r/Rag/comments/1gx44lr/need_building_app_like_perplexity/) , 2024-11-23-0914
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

     
 
all -  [ Guys Review my resume and suggest me changes required (this resume not getting through) ](https://i.redd.it/vc5gubdl4f2e1.jpeg) , 2024-11-23-0914
```
Guys pls review my resume any type of insight would be helpful!
```
---

     
 
all -  [ LangChain context switching chatbot ](https://www.reddit.com/r/LangChain/comments/1gx1o3v/langchain_context_switching_chatbot/) , 2024-11-23-0914
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

     
 
all -  [ Customer Support Evolution Tracker: AI-Powered Support Quality Analysis 🎯 ](https://www.reddit.com/r/ArtificialMoney/comments/1gx11k7/customer_support_evolution_tracker_aipowered/) , 2024-11-23-0914
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

     
 
all -  [ how does v0 work ](https://www.reddit.com/r/LangChain/comments/1gwt9i9/how_does_v0_work/) , 2024-11-23-0914
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

     
 
all -  [ How expensive are lambda layers? ](https://www.reddit.com/r/aws/comments/1gws5id/how_expensive_are_lambda_layers/) , 2024-11-23-0914
```
I am storing langchain module on lambda layers it is about 250mb.

Should i be worried about aws charging me?

It is a b
asic library for what i am doing
```
---

     
 
all -  [ Langchain for audiovisual experiences: Mediachain ](https://www.reddit.com/r/moviepy/comments/1gws02u/langchain_for_audiovisual_experiences_mediachain/) , 2024-11-23-0914
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

     
 
all -  [ Langchain for visual experiences: Mediachain ](https://www.reddit.com/r/LangChain/comments/1gwrxqx/langchain_for_visual_experiences_mediachain/) , 2024-11-23-0914
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

     
 
all -  [ In langgraph, is there a way to route to two different toolnodes 'simultaniously'? (given a single A ](https://www.reddit.com/r/LangChain/comments/1gwp9bu/in_langgraph_is_there_a_way_to_route_to_two/) , 2024-11-23-0914
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

     
 
all -  [ Best option using LoRA fine-tuning open-source LLMs for a corporate?  ](https://www.reddit.com/r/LLMDevs/comments/1gwoqro/best_option_using_lora_finetuning_opensource_llms/) , 2024-11-23-0914
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

     
 
all -  [ [New Feature Launch] Searching & Favoriting ](https://www.reddit.com/r/u_youdotcom_/comments/1gwncx3/new_feature_launch_searching_favoriting/) , 2024-11-23-0914
```
Ask and you shall receive . . . We’re thrilled to introduce the launch of our most requested features: Searching & Favor
iting. ⭐️Favorite your important threads with just a click and 🔍Search effortlessly across all your old conversations.


Productivity: Leveled up 🚀

https://preview.redd.it/zrno4eoh9b2e1.jpg?width=1700&format=pjpg&auto=webp&s=33a1ee17bfe5810
2ec99a55a107dc1ab4f999ea4


```
---

     
 
all -  [ LangGraph with DSPy ](https://www.reddit.com/r/LangGraph/comments/1gwl1he/langgraph_with_dspy/) , 2024-11-23-0914
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

     
 
all -  [ [Student] Final year student. Can't land a single interview. Will appreciate any feedback. ](https://www.reddit.com/r/EngineeringResumes/comments/1gwju3s/student_final_year_student_cant_land_a_single/) , 2024-11-23-0914
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

     
 
all -  [ If anyone from Langchain team is reading this: STOP EVERYTHING and JUST UPDATE AND ORGANISE THE DOCS ](https://www.reddit.com/r/LangChain/comments/1gwh09x/if_anyone_from_langchain_team_is_reading_this/) , 2024-11-23-0914
```
I know very many people who just give up on this framework. It's supposed to be easy for people with average or low codi
ng experience. You are building the product for experienced devs who could even build agents without using langgraph or 
langchain.

It should be so easy, you could pass well organised docs to Cursor for example and you could create agent wo
rkflows with simple logic and commands. But the docs are so confusing, 0 organisation and you need to do so much searchi
ng and finding your own way to use the framework.
```
---

     
 
all -  [ What If Automation Was Actually… Effortless? ](https://www.reddit.com/r/LangChain/comments/1gwegx9/what_if_automation_was_actually_effortless/) , 2024-11-23-0914
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

     
 
all -  [ best LLMs with balance of performance/size for a command-line agent? & is LangChain a good usecase f ](https://www.reddit.com/r/LangChain/comments/1gwe546/best_llms_with_balance_of_performancesize_for_a/) , 2024-11-23-0914
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

     
 
all -  [ OpenAI Privacy policy  ](https://www.reddit.com/r/LangChain/comments/1gwdhw5/openai_privacy_policy/) , 2024-11-23-0914
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

     
 
all -  [ A prompt management tool for teams that allows business people to create better AI prompts while dev ](https://www.reddit.com/r/LangChain/comments/1gwciqh/a_prompt_management_tool_for_teams_that_allows/) , 2024-11-23-0914
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

     
 
all -  [ LLM noob here, requesting help on embeddings, langchain ](https://www.reddit.com/r/ollama/comments/1gwbyen/llm_noob_here_requesting_help_on_embeddings/) , 2024-11-23-0914
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

     
 
all -  [ Langchain Async, how's it working behind the scenes? ](https://www.reddit.com/r/LangChain/comments/1gwakj2/langchain_async_hows_it_working_behind_the_scenes/) , 2024-11-23-0914
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

     
 
all -  [ Building an application with OpenAI api that analyses multiple PDFs with bank account statements. Wh ](https://www.reddit.com/r/LangChain/comments/1gwagn1/building_an_application_with_openai_api_that/) , 2024-11-23-0914
```
I have multiple bank accounts in a few different countries. I want  to be able to ask questions about it.

HOW I CURRENT
LY DO IT:
1. I download all of my bank account statements (PDFs, CSVs, images...) and my family's (~20 statements, some 
are as long as 70 pages, some are 2 pages).
2. I upload them to ChatGPT.
3. I ask questions about them.

THE APP I WANT 
TO BUILD:
1. I upload all of my bank account statements to the app .
2. The answers to a set of pre-defined question are
 retrieved automatically.

HOW DO I ACHIEVE THIS?
I'm new to using the OpenAI api. I don't know how to achieve this. Som
e questions:

1. Can I submit PDFs, CSVs and images all through the same api call?
2. Which model can do this?
3. For th
e specific case of PDFs: is it better to
....a) convert to image and have openai answer questions about images? or
....b
) extract text from the PDF and have openai find answers to questions on text?
4. Are there going to be problems with ve
ry long PDFs? What are some techniques to avoid such problems?
```
---

     
 
all -  [ What is your opinion on langraph for complex projects ](https://www.reddit.com/r/LangChain/comments/1gw9ct0/what_is_your_opinion_on_langraph_for_complex/) , 2024-11-23-0914
```
I’m working on LLM powered chatbots in my company and we are struggle in defining complex flows with langraph. We are st
ruggling because we can do the same thing in X different ways, but more importantly testing complex graph is a mess.
Wha
t is your opinion?
Langraph reminds me the first Tensorflow (Jeff  Dean was the main contributor) and we all know how is
 finished and why everyone uses Pytorch. 
Very curious to hear the point of view of this community
```
---

     
 
all -  [ Supply Chain Disruption Predictor: Anticipate and Mitigate Supply Chain Risks with AI 🔄 ](https://www.reddit.com/r/ArtificialMoney/comments/1gw94bq/supply_chain_disruption_predictor_anticipate_and/) , 2024-11-23-0914
```
Let's build an AI-powered system that predicts potential supply chain disruptions before they impact operations. By anal
yzing multiple data streams - from weather patterns and geopolitical events to supplier health metrics and transportatio
n data - we can help businesses proactively manage supply chain risks and maintain operational resilience.

## 😫 Problem

Supply chain disruptions have become increasingly common and costly. Traditional supply chain management relies heavily
 on historical data and reactive measures, leaving businesses vulnerable to:
* Unexpected supplier failures
* Transporta
tion bottlenecks
* Natural disasters
* Geopolitical events
* Market volatility
* Labor shortages
* Quality control issue
s

While companies have access to massive amounts of supply chain data, they lack the tools to effectively synthesize th
is information into actionable predictions and mitigation strategies.

## ✨ Solution
Our Supply Chain Disruption Predict
or will serve as an early warning system by combining diverse data sources with advanced AI models to forecast potential
 disruptions and suggest mitigation strategies.

Key capabilities include:
* Real-time monitoring of supplier health ind
icators
* Weather pattern analysis for logistics impact
* Geopolitical risk assessment
* Alternative supplier recommenda
tions
* Transportation route optimization
* Inventory level optimization
* Automated risk mitigation workflows

The syst
em will not only predict disruptions but also provide actionable recommendations like 'Increase safety stock of Componen
t X due to predicted weather disruption in supplier region' or 'Consider alternate shipping route through Port B due to 
emerging congestion at Port A.'

## 🎯 Target Users
Our platform will serve various stakeholders in the supply chain ecos
ystem:
* Supply Chain Managers
* Procurement Teams
* Logistics Coordinators
* Manufacturing Operations Leaders
* Risk Ma
nagement Teams
* C-Suite Executives
* Small to Medium Manufacturers
* Large Enterprise Organizations

## 🛠️ Implementati
on Approach
Let's break down the technical architecture into its core components:

* Infrastructure Stack:
  * AWS for p
rimary cloud infrastructure
  * Kubernetes for containerization
  * MongoDB for flexible data storage
  * Elasticsearch 
for real-time search and analytics
  * Redis for caching and real-time updates
  * Apache Kafka for event streaming

* B
ackend Services:
  * Python with FastAPI for main application
  * Node.js for real-time features
  * GraphQL for flexibl
e data querying
  * Apache Airflow for data pipeline orchestration

* Frontend Development:
  * Next.js for web applicat
ion
  * React for interactive dashboards
  * D3.js for data visualization
  * TailwindCSS for styling

* AI/ML Component
s:
  * TensorFlow for deep learning models
  * Prophet for time series forecasting
  * Scikit-learn for traditional ML m
odels
  * SpaCy for NLP tasks
  * LangChain for LLM integration

## 📊 Data Integration
The system will integrate data fr
om multiple sources:

* External Data:
  * Weather APIs
  * News feeds and social media
  * Economic indicators
  * Tran
sportation tracking systems
  * Satellite imagery
  * Currency exchange rates

* Internal Data:
  * ERP systems
  * Supp
lier performance metrics
  * Inventory levels
  * Production schedules
  * Historical disruption data
  * Quality contro
l metrics

## 🤖 AI Models and Analytics

### Prediction Engine
We'll implement several specialized models:
* Time series
 forecasting for demand prediction
* Classification models for risk assessment
* Natural language processing for news an
alysis
* Computer vision for satellite imagery analysis
* Anomaly detection for early warning signals

### Risk Assessme
nt Framework
The system will calculate risk scores based on:
* Historical performance data
* Current market conditions
*
 Geographic concentration
* Supplier financial health
* Transportation network stability
* Political stability metrics


## 💰 Monetization Strategy
We'll implement a tiered pricing model:

* Starter Tier:
  * Basic disruption predictions
  *
 Limited data sources
  * Standard reports
  * Email alerts

* Professional Tier:
  * Advanced predictions
  * Custom da
ta integration
  * API access
  * Priority alerts

* Enterprise Tier:
  * Custom model development
  * Dedicated support

  * Advanced analytics
  * Multi-user collaboration
  * White-label options

## 🔒 Security and Compliance
Supply chain 
data is sensitive and requires robust security measures:
* End-to-end encryption
* Role-based access control
* Audit log
ging
* Compliance with industry standards
* Regular security assessments
* Data residency options

## 🚀 Development Phas
es

### Phase 1: Foundation
* Core data integration framework
* Basic prediction models
* Essential dashboard features
*
 Initial alert system

### Phase 2: Enhancement
* Advanced AI models
* Additional data sources
* Custom integrations
* M
obile app development

### Phase 3: Scale
* Advanced analytics
* Multi-tenant architecture
* Global deployment options
*
 Marketplace for third-party integrations

## 🎯 Success Metrics
We'll track several KPIs to measure effectiveness:
* Pre
diction accuracy
* Time saved in risk mitigation
* Cost savings from avoided disruptions
* User engagement metrics
* Res
olution time improvements
* ROI for mitigation strategies

## 💭 Future Potential
The platform could evolve in several di
rections:
* Autonomous mitigation execution
* Blockchain integration for transparency
* AI-powered supplier discovery
* 
Carbon footprint optimization
* Digital twin integration
* Cross-industry collaboration networks

## 🤔 Discussion Points

Let's explore some critical considerations:

* How can we balance prediction accuracy with actionable insights?
* What'
s the right approach to handle conflicting data sources?
* How do we account for complex supplier relationships?
* What 
role should human judgment play in the system?

Share your thoughts and experiences in the comments! What supply chain c
hallenges would you like this system to address? 👇

## 🌟 Getting Started
Ready to contribute to this project? Here are s
ome first steps:
* Fork the repository
* Review the technical documentation
* Join our Discord community
* Check out the
 contribution guidelines

Let's work together to build a more resilient supply chain ecosystem! 🚀
```
---

     
 
all -  [ aim : to compare 2 documents: (guidelines, proposal) and check if proposal gets accepted/rejected ba ](https://www.reddit.com/r/developersIndia/comments/1gw64tr/aim_to_compare_2_documents_guidelines_proposal/) , 2024-11-23-0914
```


AIM : 
1. if an organization has created a proposal, a tool is to be made to cross check if proper guidelines are foll
owed in order for the proposal to get accepted. 

2. The tool should specify the anomalies and the points from the propo
sal that are not in line with the guidelines which might lead to a rejection. 


DATA : 
1. i have different structures 
of the guidelines and the proposal 

2. guidelines was originally in pdf format, i have it in json as well 


3. and for
 the proposal, it is a budget file which was in excel. i can pass it as pdf, csv or json. i have created a nested json f
or the excel file as well. 



METHOD (at present) : 
i used langchain's document comparison guide. 

1. used '.pdf' for
 both guidelines and the proposal

Note - the guidelines is text and a few tables 
Proposal has this excel file filled w
ith budget allocations for different purposes. I also have an empty template of the proposal with just headings. I haven
't used this yet.
 
2. Rag chain is created

Used pdf loader, chunked it, created docs, embeddings, agents, tools, retri
ever for both the pdf separately 

3. yet im not getting promising results. what should i look at? 

i want the llm to k
ind of give a decision whether the proposal will get accepted or not with proper accurate reasons 



what should i focu
s on? where am i going wrong? 


Note 2 - I read in another reddit post that RAG is just getting the documents, shreddin
g it, putting it into the toilet (vector store) and asking a toddler to get the required pieces and assembling it 😭

how
 shall i navigate this ? 
```
---

     
 
all -  [ aim : to compare 2 documents: (guidelines, proposal) and check if proposal gets accepted/rejected ba ](https://www.reddit.com/r/LangChain/comments/1gw5xxv/aim_to_compare_2_documents_guidelines_proposal/) , 2024-11-23-0914
```
AIM : 
1. if an organization has created a proposal, a tool is to be made to cross check if proper guidelines are follow
ed in order for the proposal to get accepted. 

2. The tool should specify the anomalies and the points from the proposa
l that are not in line with the guidelines which might lead to a rejection. 


DATA : 
1. i have different structures of
 the guidelines and the proposal 

2. guidelines was originally in pdf format, i have it in json as well 


3. and for t
he proposal, it is a budget file which was in excel. i can pass it as pdf, csv or json. i have created a nested json for
 the excel file as well. 



METHOD (at present) : 
i used langchain's document comparison guide. 

1. used '.pdf' for b
oth guidelines and the proposal

Note - the guidelines is text and a few tables 
Proposal has this excel file filled wit
h budget allocations for different purposes. I also have an empty template of the proposal with just headings. I haven't
 used this yet.
 
2. Rag chain is created

Used pdf loader, chunked it, created docs, embeddings, agents, tools, retriev
er for both the pdf separately 

3. yet im not getting promising results. what should i look at? 

i want it to kind of 
give a decision whether the proposal will get accepted or not with proper accurate reasons 



what should i focus on? w
here am i going wrong? 

Note 2 - I read in another reddit post that RAG is just getting the documents, shredding it, pu
tting it into the toilet (vector store) and asking a toddler to get the required pieces and assembling it 😭

how shall i
 navigate this ? 
```
---

     
 
all -  [ List of FREE and Best Selling Discounted Courses ](https://www.reddit.com/r/udemyfreeebies/comments/1gw0szl/list_of_free_and_best_selling_discounted_courses/) , 2024-11-23-0914
```
# Udemy Free Courses for 21 November 2024

Note : Coupons might expire anytime, so enroll as soon as possible to get the
 courses for FREE.

* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/25777/)Mastering Microsoft Azure: Advanced Servi
ces
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/25776/)Azure ChatGPT and OpenAI Service – The Complete Guide
* [
REDEEM OFFER ](https://idownloadcoupon.com/udemy/25775/)RAG, AI Agents and Generative AI with Python and OpenAI 2025
* [
REDEEM OFFER ](https://idownloadcoupon.com/udemy/25774/)Master Time Series Analysis and Forecasting with Python 2025
* [
REDEEM OFFER ](https://idownloadcoupon.com/udemy/25773/)Angular: De cero a experto
* [REDEEM OFFER ](https://idownloadco
upon.com/udemy/25772/)Complete Generative AI Course With Langchain and Huggingface
* [REDEEM OFFER ](https://idownloadco
upon.com/udemy/25771/)Complete MLOps Bootcamp With 10+ End To End ML Projects
* [REDEEM OFFER ](https://idownloadcoupon.
com/udemy/25770/)Complete Data Science,Machine Learning,DL,NLP Bootcamp
* [REDEEM OFFER ](https://idownloadcoupon.com/ud
emy/25769/)Mathematics-Basics to Advanced for Data Science And GenAI
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy
/25768/)Complete Python With DSA Bootcamp + LEETCODE Exercises
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/25767
/)Complete Arabic Course: Learn Arabic for Beginners
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/25766/)Dart & F
lutter | The Complete Flutter Development Course
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/25765/)Building Gen
 AI App 12+ Hands-on Projects with Gemini Pro
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/25764/)Complete Data A
nalyst Bootcamp From Basics To Advanced
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/25763/)Mastering Figma from 
0 to 100 (UI/UX Mastery Course)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/25762/)Spring Boot & Angular: Constr
uye aplicación reserva hotelera
* Crea sistemas de Reservas y Alquiler con PHP 7 y MercadoPago
* [REDEEM OFFER](https://
idownloadcoupon.com/udemy/25761/)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/25760/)Crea Sistemas Marketplace c
on Angular y Firebase Database
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/25759/)Crea sistemas Ecommerce con PH
P y MySQL V1.0
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/25758/)Observabilidad de Aplicaciones JAVA con OpenTe
lemetry
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/25757/)Introduction to Arab Culture
* [REDEEM OFFER ](https:
//idownloadcoupon.com/udemy/25756/)Advance MS Excel VBA for Beginner to Advanced
* [REDEEM OFFER ](https://idownloadcoup
on.com/udemy/25755/)Python Programming Language (Practice Projects)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/
25754/)700-905: Cisco DevNet Professional Exam
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/25753/)Developing suc
cessful Professional Relationships
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/25752/)PL-300: Microsoft Power BI
 Practice Test – 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/25751/)70-489: Developing Microsoft SharePoint
 Practice test 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/25750/)Python Development and Python Programming
 Fundamentals
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/25749/)Master Amazon EC2 Storage: Complete Guide for E
BS, EFS & AMI
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/25748/)Build a Simple Calculator in React + JavaScript
 Foundations
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/25747/)Professional Logo Production With Artificial Int
elligence
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/25746/)JavaScript, Bootstrap, & PHP – Certification for Be
ginners
* Cloud Computing Essentials: Linode, Linux, and LAMP Stack
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/2
5745/)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/25744/)Setup a Virtual Web Server using Linode or Digital Oce
an
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/25743/)JavaScript & jQuery – Certification Course for Beginners
*
 [REDEEM OFFER ](https://idownloadcoupon.com/udemy/25742/)How to be a programmer | Full guide to start (Arabic)
* [REDEE
M OFFER ](https://idownloadcoupon.com/udemy/25741/)Introduction to Domain Names and Web Hosting – Quick Guide
* [REDEEM 
OFFER ](https://idownloadcoupon.com/udemy/25740/)Learn Bootstrap – For Beginners
* [REDEEM OFFER ](https://idownloadcoup
on.com/udemy/25739/)Linode: Build and Deploy Responsive Websites on the Cloud
* [REDEEM OFFER ](https://idownloadcoupon.
com/udemy/25738/)AWS & React: Deploy an Auto-Scaling E-Commerce App with ELB
* [REDEEM OFFER ](https://idownloadcoupon.c
om/udemy/25737/)Elevate Your Leadership, Amplify Your Communication Skills
* [REDEEM OFFER ](https://idownloadcoupon.com
/udemy/25736/)Figma UI/UX Complete Bootcamp: Design 5 Job-Ready Projects
* [REDEEM OFFER ](https://idownloadcoupon.com/u
demy/25735/)Mastering Market Research for Effective Product Management
* [REDEEM OFFER ](https://idownloadcoupon.com/ude
my/25734/)Mastering the Foundations of Sales Operations
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/25733/)Trans
forming Business with AI: Organization and Society
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/25732/)Mastering 
Sales Negotiation for High-Value Deals
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/25731/)Financial Modeling wit
h Generative AI Certification
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/25730/)AI Market Analysis & Strategy C
ertification
* AI Powered Business Model Design | Certification
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/25729
/)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/25728/)Code Full-Stack GPS Project with Expert Guidance | 2024
* 
[REDEEM OFFER ](https://idownloadcoupon.com/udemy/25727/)Strategic Partnerships and Collaborations
* [REDEEM OFFER ](htt
ps://idownloadcoupon.com/udemy/25726/)Master Landscape Photo Editing From Scratch
* [REDEEM OFFER ](https://idownloadcou
pon.com/udemy/25725/)The Ultimate Guide for Beginners in Photo Editing
* [REDEEM OFFER ](https://idownloadcoupon.com/ude
my/25724/)Navigating Change: AI & Automation in Modern Workplaces
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/25
723/)Business Development with Generative AI | Certification
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/25722/)
Facebook Ads Improvement: Make Your Ads Breathtaking
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/25721/)15 Effec
tive Steps for Growing Business in Social Media
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/25720/)7 Days of Han
ds-On AI Development Bootcamp and Certification
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/25719/)Enhance Light
room Editing with the Luminar Neo Plugin
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/25718/)Professional Certifi
cate in SMM Social Media Marketing
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/25717/)Voice Cloning With Artific
ial Intelligence Audio Course
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/25716/)Python Fundamentals – A Compreh
ensive Beginner’s Guide
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/25715/)P2150-870: IBM Certified Specialist P
ractice test 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/25714/)YouTube Startrack For Beginners: Launch You
r Channel Today
* C# Basics: From Zero to First Applications
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/25713/)

* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/25712/)iOS Development Kickstart: Craft Your First App With SwiftUI

* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/25711/)Online Course Creation: 10 Key Steps from Idea to Launch
* [R
EDEEM OFFER ](https://idownloadcoupon.com/udemy/25710/)React Crash Course: From Zero to Hero
* [REDEEM OFFER ](https://i
downloadcoupon.com/udemy/25709/)Land Analyst Job in Web3 VC – Intensive Course
* [REDEEM OFFER ](https://idownloadcoupon
.com/udemy/25708/)Professional Certificate in Marketing & Marketing Management
* [REDEEM OFFER ](https://idownloadcoupon
.com/udemy/25707/)Web Design Course with HTML CSS and WordPress
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/2570
6/)C-level management: 100 models for business – 5 courses in 1
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/2570
5/)Exam 2V0-13.24:VMware Cloud Foundation 5.2 Architect VCP-VCF
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/2570
4/)Amazon FBA Guide: From Zero to Seller
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/25703/)70-414: Implementing
 Windows Server 2012 Practice Test 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/25702/)Canva & AI Mastery (B
ULK Content Creation with AI & ChatGPT)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/25701/)350-801: Implementing
 Operating Cisco Collaboration 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/25700/)350-701: Implementing and
 Operating Cisco Security Core 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/25699/)70-448: Microsoft SQL Ser
ver 2008 R2 Practice Test 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/25698/)70-417: Upgrade MCSA Windows S
erver 2012 Practice Test 2024
* 70-411: Administering Windows Server 2012 Practice Test 2024
* [REDEEM OFFER](https://id
ownloadcoupon.com/udemy/25697/)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/25696/)Presentation Skills: Give a G
reat Acceptance Speech
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/25695/)Theory of Constraints: Certification
*
 [REDEEM OFFER ](https://idownloadcoupon.com/udemy/25694/)CompTIA Project+ (PK0-005) Practice Tests – 2024 Updated
* [RE
DEEM OFFER ](https://idownloadcoupon.com/udemy/25693/)350-901: Developing Applications Using Cisco Core 2024
* [REDEEM O
FFER ](https://idownloadcoupon.com/udemy/25692/)350-601: Implementing and Operating Cisco Data Center 2024
* [REDEEM OFF
ER ](https://idownloadcoupon.com/udemy/25691/)350-501: Implementing Operating Cisco Service Provider 2024
* [REDEEM OFFE
R ](https://idownloadcoupon.com/udemy/25690/)Lean Waste Management: Strategies for Streamlining Processes
* [REDEEM OFFE
R ](https://idownloadcoupon.com/udemy/25689/)Basic Quality Management Fundamentals: Essential Principles.
* [REDEEM OFFE
R ](https://idownloadcoupon.com/udemy/25688/)Learn SQL in 3 Hours : A tutorial for fast learners
* [REDEEM OFFER ](https
://idownloadcoupon.com/udemy/25687/)Professional Certificate in Coaching
* [REDEEM OFFER ](https://idownloadcoupon.com/u
demy/25686/)Sales Skills Training: Give a Winning Sales Presentation
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy
/25685/)Online Course Creation: Teach an Online Course
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/25684/)Solvin
g LeetCode’s Top Interview Questions in Java \[2024\]
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/25683/)Ultimat
e Guide to Product Design: Design Thinking Approach
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/25682/)Car Repai
r and Electrician Training Certificated : CRETC+

GET MORE FREE ONLINE COURSES WITH CERTIFICATE – [CLICK HERE](https://i
downloadcoupon.com/)
```
---

     
 
all -  [ List of FREE and Best Selling Discounted Courses ](https://www.reddit.com/r/udemyfreebies/comments/1gw0sy4/list_of_free_and_best_selling_discounted_courses/) , 2024-11-23-0914
```
# Udemy Free Courses for 21 November 2024

Note : Coupons might expire anytime, so enroll as soon as possible to get the
 courses for FREE.

* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/25777/)Mastering Microsoft Azure: Advanced Servi
ces
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/25776/)Azure ChatGPT and OpenAI Service – The Complete Guide
* [
REDEEM OFFER ](https://idownloadcoupon.com/udemy/25775/)RAG, AI Agents and Generative AI with Python and OpenAI 2025
* [
REDEEM OFFER ](https://idownloadcoupon.com/udemy/25774/)Master Time Series Analysis and Forecasting with Python 2025
* [
REDEEM OFFER ](https://idownloadcoupon.com/udemy/25773/)Angular: De cero a experto
* [REDEEM OFFER ](https://idownloadco
upon.com/udemy/25772/)Complete Generative AI Course With Langchain and Huggingface
* [REDEEM OFFER ](https://idownloadco
upon.com/udemy/25771/)Complete MLOps Bootcamp With 10+ End To End ML Projects
* [REDEEM OFFER ](https://idownloadcoupon.
com/udemy/25770/)Complete Data Science,Machine Learning,DL,NLP Bootcamp
* [REDEEM OFFER ](https://idownloadcoupon.com/ud
emy/25769/)Mathematics-Basics to Advanced for Data Science And GenAI
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy
/25768/)Complete Python With DSA Bootcamp + LEETCODE Exercises
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/25767
/)Complete Arabic Course: Learn Arabic for Beginners
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/25766/)Dart & F
lutter | The Complete Flutter Development Course
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/25765/)Building Gen
 AI App 12+ Hands-on Projects with Gemini Pro
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/25764/)Complete Data A
nalyst Bootcamp From Basics To Advanced
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/25763/)Mastering Figma from 
0 to 100 (UI/UX Mastery Course)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/25762/)Spring Boot & Angular: Constr
uye aplicación reserva hotelera
* Crea sistemas de Reservas y Alquiler con PHP 7 y MercadoPago
* [REDEEM OFFER](https://
idownloadcoupon.com/udemy/25761/)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/25760/)Crea Sistemas Marketplace c
on Angular y Firebase Database
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/25759/)Crea sistemas Ecommerce con PH
P y MySQL V1.0
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/25758/)Observabilidad de Aplicaciones JAVA con OpenTe
lemetry
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/25757/)Introduction to Arab Culture
* [REDEEM OFFER ](https:
//idownloadcoupon.com/udemy/25756/)Advance MS Excel VBA for Beginner to Advanced
* [REDEEM OFFER ](https://idownloadcoup
on.com/udemy/25755/)Python Programming Language (Practice Projects)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/
25754/)700-905: Cisco DevNet Professional Exam
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/25753/)Developing suc
cessful Professional Relationships
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/25752/)PL-300: Microsoft Power BI
 Practice Test – 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/25751/)70-489: Developing Microsoft SharePoint
 Practice test 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/25750/)Python Development and Python Programming
 Fundamentals
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/25749/)Master Amazon EC2 Storage: Complete Guide for E
BS, EFS & AMI
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/25748/)Build a Simple Calculator in React + JavaScript
 Foundations
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/25747/)Professional Logo Production With Artificial Int
elligence
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/25746/)JavaScript, Bootstrap, & PHP – Certification for Be
ginners
* Cloud Computing Essentials: Linode, Linux, and LAMP Stack
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/2
5745/)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/25744/)Setup a Virtual Web Server using Linode or Digital Oce
an
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/25743/)JavaScript & jQuery – Certification Course for Beginners
*
 [REDEEM OFFER ](https://idownloadcoupon.com/udemy/25742/)How to be a programmer | Full guide to start (Arabic)
* [REDEE
M OFFER ](https://idownloadcoupon.com/udemy/25741/)Introduction to Domain Names and Web Hosting – Quick Guide
* [REDEEM 
OFFER ](https://idownloadcoupon.com/udemy/25740/)Learn Bootstrap – For Beginners
* [REDEEM OFFER ](https://idownloadcoup
on.com/udemy/25739/)Linode: Build and Deploy Responsive Websites on the Cloud
* [REDEEM OFFER ](https://idownloadcoupon.
com/udemy/25738/)AWS & React: Deploy an Auto-Scaling E-Commerce App with ELB
* [REDEEM OFFER ](https://idownloadcoupon.c
om/udemy/25737/)Elevate Your Leadership, Amplify Your Communication Skills
* [REDEEM OFFER ](https://idownloadcoupon.com
/udemy/25736/)Figma UI/UX Complete Bootcamp: Design 5 Job-Ready Projects
* [REDEEM OFFER ](https://idownloadcoupon.com/u
demy/25735/)Mastering Market Research for Effective Product Management
* [REDEEM OFFER ](https://idownloadcoupon.com/ude
my/25734/)Mastering the Foundations of Sales Operations
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/25733/)Trans
forming Business with AI: Organization and Society
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/25732/)Mastering 
Sales Negotiation for High-Value Deals
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/25731/)Financial Modeling wit
h Generative AI Certification
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/25730/)AI Market Analysis & Strategy C
ertification
* AI Powered Business Model Design | Certification
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/25729
/)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/25728/)Code Full-Stack GPS Project with Expert Guidance | 2024
* 
[REDEEM OFFER ](https://idownloadcoupon.com/udemy/25727/)Strategic Partnerships and Collaborations
* [REDEEM OFFER ](htt
ps://idownloadcoupon.com/udemy/25726/)Master Landscape Photo Editing From Scratch
* [REDEEM OFFER ](https://idownloadcou
pon.com/udemy/25725/)The Ultimate Guide for Beginners in Photo Editing
* [REDEEM OFFER ](https://idownloadcoupon.com/ude
my/25724/)Navigating Change: AI & Automation in Modern Workplaces
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/25
723/)Business Development with Generative AI | Certification
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/25722/)
Facebook Ads Improvement: Make Your Ads Breathtaking
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/25721/)15 Effec
tive Steps for Growing Business in Social Media
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/25720/)7 Days of Han
ds-On AI Development Bootcamp and Certification
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/25719/)Enhance Light
room Editing with the Luminar Neo Plugin
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/25718/)Professional Certifi
cate in SMM Social Media Marketing
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/25717/)Voice Cloning With Artific
ial Intelligence Audio Course
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/25716/)Python Fundamentals – A Compreh
ensive Beginner’s Guide
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/25715/)P2150-870: IBM Certified Specialist P
ractice test 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/25714/)YouTube Startrack For Beginners: Launch You
r Channel Today
* C# Basics: From Zero to First Applications
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/25713/)

* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/25712/)iOS Development Kickstart: Craft Your First App With SwiftUI

* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/25711/)Online Course Creation: 10 Key Steps from Idea to Launch
* [R
EDEEM OFFER ](https://idownloadcoupon.com/udemy/25710/)React Crash Course: From Zero to Hero
* [REDEEM OFFER ](https://i
downloadcoupon.com/udemy/25709/)Land Analyst Job in Web3 VC – Intensive Course
* [REDEEM OFFER ](https://idownloadcoupon
.com/udemy/25708/)Professional Certificate in Marketing & Marketing Management
* [REDEEM OFFER ](https://idownloadcoupon
.com/udemy/25707/)Web Design Course with HTML CSS and WordPress
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/2570
6/)C-level management: 100 models for business – 5 courses in 1
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/2570
5/)Exam 2V0-13.24:VMware Cloud Foundation 5.2 Architect VCP-VCF
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/2570
4/)Amazon FBA Guide: From Zero to Seller
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/25703/)70-414: Implementing
 Windows Server 2012 Practice Test 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/25702/)Canva & AI Mastery (B
ULK Content Creation with AI & ChatGPT)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/25701/)350-801: Implementing
 Operating Cisco Collaboration 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/25700/)350-701: Implementing and
 Operating Cisco Security Core 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/25699/)70-448: Microsoft SQL Ser
ver 2008 R2 Practice Test 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/25698/)70-417: Upgrade MCSA Windows S
erver 2012 Practice Test 2024
* 70-411: Administering Windows Server 2012 Practice Test 2024
* [REDEEM OFFER](https://id
ownloadcoupon.com/udemy/25697/)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/25696/)Presentation Skills: Give a G
reat Acceptance Speech
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/25695/)Theory of Constraints: Certification
*
 [REDEEM OFFER ](https://idownloadcoupon.com/udemy/25694/)CompTIA Project+ (PK0-005) Practice Tests – 2024 Updated
* [RE
DEEM OFFER ](https://idownloadcoupon.com/udemy/25693/)350-901: Developing Applications Using Cisco Core 2024
* [REDEEM O
FFER ](https://idownloadcoupon.com/udemy/25692/)350-601: Implementing and Operating Cisco Data Center 2024
* [REDEEM OFF
ER ](https://idownloadcoupon.com/udemy/25691/)350-501: Implementing Operating Cisco Service Provider 2024
* [REDEEM OFFE
R ](https://idownloadcoupon.com/udemy/25690/)Lean Waste Management: Strategies for Streamlining Processes
* [REDEEM OFFE
R ](https://idownloadcoupon.com/udemy/25689/)Basic Quality Management Fundamentals: Essential Principles.
* [REDEEM OFFE
R ](https://idownloadcoupon.com/udemy/25688/)Learn SQL in 3 Hours : A tutorial for fast learners
* [REDEEM OFFER ](https
://idownloadcoupon.com/udemy/25687/)Professional Certificate in Coaching
* [REDEEM OFFER ](https://idownloadcoupon.com/u
demy/25686/)Sales Skills Training: Give a Winning Sales Presentation
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy
/25685/)Online Course Creation: Teach an Online Course
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/25684/)Solvin
g LeetCode’s Top Interview Questions in Java \[2024\]
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/25683/)Ultimat
e Guide to Product Design: Design Thinking Approach
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/25682/)Car Repai
r and Electrician Training Certificated : CRETC+

GET MORE FREE ONLINE COURSES WITH CERTIFICATE – [CLICK HERE](https://w
ww.reddit.com/r/udemyfreeebies/)
```
---

     
 
all -  [ Please tell me where all i need improvements. Made it on word and i am not at all confident on this. ](https://i.redd.it/kpyi5069z32e1.jpeg) , 2024-11-23-0914
```
Some ATC checker website is giving 75+ while some are giving below 50. i am really sceptical about this. i feel this is 
the most important thing that would help me get interviews so i want to make it perfect. please tell me where all i need
 improvement. would really appreciate your help.

also, please do let me know if i should change the skills section and 
if i am missing any important skills as a 2yoe MERN developer. Thanks
```
---

     
 
all -  [ A Guide to Integrating Pythia API with RAG-based Systems Using Wisecube Python SDK ](https://www.reddit.com/r/pythia/comments/1gvvbcm/a_guide_to_integrating_pythia_api_with_ragbased/) , 2024-11-23-0914
```
Retrieval Augmented Generation (RAG) systems generate outputs from an external knowledge base to enhance the accuracy of
 generative AI. Despite their suitability in various applications, including customer service, risk management, and rese
arch, RAG systems are prone to AI hallucinations.

Wisecube's Pythia is a hallucination detection tool which detects hal
lucinations in real time and promises continuous improvement of RAG outputs, resulting in reliable outputs. Pythia easil
y integrates with RAG-based systems and generates hallucination reports for RAG outputs that guide developers in taking 
corrective measures on time.

In this blog post, we’ll explore the step-by-step process of integrating Pythia in RAG sys
tems. We’ll also have a look at the benefits of using Pythia for hallucination detection in RAG systems.

**What is RAG?
**

RAG systems improve the accuracy of LLMs by referencing an external knowledge base outside of their training data. T
he external knowledge base makes RAG systems context-aware and provides a source of factual information. RAG systems usu
ally use vector databases to store massive data and retrieve relevant information quickly.

Since RAG-based systems rely
 on external knowledge bases, the accuracy of knowledge base can significantly impact the quality of RAG outputs. Biased
 knowledge bases can lead to non-sensical outputs and perpetuate bias, which leads to unfair and misleading LLM response
s.

Let's have a look at the step-by-step process of integrating Pythia with RAG-based systems to detect hallucinations 
in RAG outputs.

**Getting an API Key**

You need a unique API key to authenticate Wisecube Pythia and integrate it into
 RAG systems. Fill out the API key request form to get your unique Wisecube API key.

**Installing Wisecube Python SDK**


Next, you need to install Wisecube Python SDK in your machine or cloud-based Python IDE, depending on what you’re usin
g. Copy the following command in your Python console and run the code to install Wisecube:

    pip install wisecube

**
Install Relevant Libraries from LangChain**

Developing an RAG system requires language processing libraries and a vecto
r database from LangChain. Run the following code to install the necessary libraries in your Python console:

    %pip i
nstall --upgrade --quiet  wisecube langchain langchain-community 
    langchainhub langchain-openai langchain-chroma bs4


**Authenticate API Key**

The API key needs to be authenticated before you begin using it. Since we’re using ChatGPT, 
we also need an OpenAI API key to implement an LLM in our RAG system. os and getpass Python modules help you save and au
thenticate the API keys securely:

    import os
    from getpass import getpass
      
    API_KEY = getpass('Wisecube 
API Key:')
    OPENAI_API_KEY = getpass('Open API Key:')
    os.environ['OPENAI_API_KEY'] = OPENAI_API_KEY

**Creating a
n OpenAI Instance**

Next, we create a ChatOpenAI instance and specify the model. In the following code, we set the Open
AI instance to llm variable and specify the gpt-3.5-turbo-0125 model for our system. You can use any [model](https://pla
tform.openai.com/docs/models/overview) from GPT-4 and GPT-4 Turbo, DALL-E, TTS, Whisper, Embeddings, Moderation, and dep
recated models.

    from langchain_openai import ChatOpenAI
      
    llm = ChatOpenAI(model='gpt-3.5-turbo-0125')

**
Creating a RAG-based System in Python**

Since this tutorial focuses on integrating Pythia with RAG systems, we’ll imple
ment a simple RAG using Langchain. However, using the same approach, you can use Pythia for hallucination detection in c
omplex RAG systems.

Below is the breakdown of the RAG system in the following code snippet:

1. Load a blog post as our
 knowledge base for the RAG system using WebBaseLoader.
2. Split the extracted text and save it into a vector database.

3. Retrieve information from the vector database based on user query. This information will serve as our reference in Py
thia.
4. hub.pull('rlm/rag-prompt') pulls a pre-defined RAG prompt from LangSmith prompt hub. This prompt guides LLM on 
how to use the retrieved information from the knowledge base. You can use other relevant prompts as well.
5. Create a La
ngChain pipeline to generate a response against user query. 

&#8203;

    # Load, chunk and index the contents of the b
log.
    loader = 
    WebBaseLoader('https://my.clevelandclinic.org/health/diseases/7104-diabetes')
    docs = loader.l
oad()
      
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, 
    chunk_overlap=200)
    splits = te
xt_splitter.split_documents(docs)
    vectorstore = Chroma.from_documents(documents=splits, 
    embedding=OpenAIEmbeddi
ngs())
      
    # Retrieve and generate using the relevant snippets of the blog.
    retriever = vectorstore.as_retrie
ver()
    prompt = hub.pull('rlm/rag-prompt')
    def format_docs(docs):    
           
            return '\n\n'.join(
doc.page_content for doc in docs)
              
    rag_chain = (    
            {'context': retriever | format_docs, 
'question': 
    RunnablePassthrough()}    
            | prompt   
            | llm   
            | StrOutputParser()

    )



**Using RAG to Generate Output**

You can query your RAG system to generate relevant output now. The following
 code defines a variable question that stores user queries and extracts references and responses from the retriever and 
rag\_chain function defined in the previous step:

    question = 'What is diabetes?'
    reference = retriever.invoke(q
uestion)
    response = rag_chain.invoke(question)

**Using Pythia to Detect Hallucinations**

Finally, you can use Pyth
ia to detect hallucinations in your RAG-generated outputs. You just need to provide ask\_pythia with a reference and res
ponse extracted in the previous step, along with the question. Pythia will detect and categorize hallucinations among en
tailment, contradiction, neutral, and missing facts:

    qa_client = WisecubeClient(API_KEY).client
    response_from_s
dk = qa_client.ask_pythia(reference[0].page_content, 
    response, question)

Pythia’s response after hallucination det
ection in RAG output is in the screenshot below. It extracts claims as knowledge triplets and flags claims into relevant
 classes, including entailment, contradiction, neutral, and missing facts.

Finally, it highlights the accuracy of the r
esponse and the percentage contribution of each class.

https://preview.redd.it/joqago0ng32e1.png?width=1896&format=png&
auto=webp&s=72696f631ce67063488917873d5b653b16fe84c4



**Benefits of Integrating Pythia with RAG-based Systems**

Pythi
a’s ability to seamlessly integrate with RAG-based systems ensures real-time hallucination detection in RAG outputs, enh
ancing user trust and speeding up the research. Integration of Pythia with RAG-based systems offers the following benefi
ts:

**Advanced Hallucination Detection**

Pythia divides user queries into knowledge triplets, making AI context-aware 
and accurate. Once Pythia detects hallucinations in RAG, it generates an audit report to guide developers towards its im
provement.

**Seamless Integration With Langchain**

Pythia easily integrates with the Langchain ecosystem. This empower
s developers to leverage Pythia's full potential with effortless interoperability.

**Customizable Detection**

Pythia c
an be configured to suit specific use cases using the LangChain ecosystem, allowing improved flexibility and increased a
ccuracy in tailored RAG systems.

**Real-time Analysis**

Pythia detects and flags hallucinations in real-time. Real-tim
e monitoring and analysis allow immediate corrective actions, ensuring the improvement of AI systems over time.

**Enhan
ced Trust in AI**

Pythia reduces the risk of misinformation in AI responses, ensuring accurate outputs and strengthened
 user trust in AI.

**Advanced Privacy**

Pythia protects user information so RAG developers can leverage its capabiliti
es without worrying about their data security.

Request your API key today and uncover the true potential of your RAG-ba
sed systems with continuous hallucination monitoring and analysis.

***The article was originally published*** **on** [*
*Pythia's website.**](https://askpythia.ai/blog/a-guide-to-integrating-pythia-api-with-rag-based-systems-using-wisecube-
python-sdk)
```
---

     
 
all -  [ How does a company optimize its document management system for RAG ](https://www.reddit.com/r/LangChain/comments/1gvv4x1/how_does_a_company_optimize_its_document/) , 2024-11-23-0914
```
RAG performance isn't just about the tech stack. We all know it's trash-in trash-out. How should an organisation manage 
it's documents in a way that's optimized for AI applications and RAG?
```
---

     
 
all -  [ Steamlit Callback Handler with LangGraph ReAct Agent? ](https://www.reddit.com/r/LangChain/comments/1gvqzm1/steamlit_callback_handler_with_langgraph_react/) , 2024-11-23-0914
```
I am attempting to use the Streamlit Callback Handler outlined in this documentation. [https://python.langchain.com/docs
/integrations/callbacks/streamlit/](https://python.langchain.com/docs/integrations/callbacks/streamlit/)

  
However, th
at callback handler was designed to work with a LangChain AgentExecutor. It is now recommended to use LangGraph ReAct Ag
ents instead of AgentExecutors.

Is there a way to get this callback handler to work with LangGraph ReAct agents? I want
 to visualize the agent's chain of thought when it responds to a query. If I can't use that callback handler, how can I 
achieve my goal?
```
---

     
 
MachineLearning -  [ [P] Open-source declarative framework to build LLM applications - looking for contributors ](https://www.reddit.com/r/MachineLearning/comments/1gkpazh/p_opensource_declarative_framework_to_build_llm/) , 2024-11-23-0914
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

     
 
deeplearning -  [ Fast AI's deep learning for coders by jeremy howard for begginer?  ](https://www.reddit.com/r/deeplearning/comments/1gb2k3p/fast_ais_deep_learning_for_coders_by_jeremy/) , 2024-11-23-0914
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

     
