 
all -  [ Is There A Way To Run Separate Runs At The Same Time? ](https://www.reddit.com/r/LangChain/comments/1hsxq5h/is_there_a_way_to_run_separate_runs_at_the_same/) , 2025-01-04-0912
```
I am still completely new to langchain and learning how it works.

I have a react agent that I run with `async for event
 in agent.astream_events({'messages': messages}, config, version='v2')`

During this run, I use the events to broadcast 
the stream of text to my webhooks for this run and I store completed messages to my database.

Separate from this agent 
I am running a MultiQueryRetriever, and then directly invoking a model around the same time that my react agent is runni
ng. These two have nothing to do with the react agent. However, everything is being treated as part of the same run.

Th
e events from MultiQueryRetriever and the model invocation both end up in the events for my react agent. This results in
 these events being broadcasted in my webhooks and being stored in my database.

If I use `invoke` rather than `ainvoke`
 for both of those invocations, my react agent completely pauses until those two invocations finish.

On langsmith it al
l shows up as part of the same run as well.

Is there a way to have these invocations run separately or be treated as se
parate runs?

--
Here is a [sample script](https://pastebin.com/cRy8ZgYB) to replicate the behavior. It uses a tool call
 to get the other invocations running at the same time, although keeping them separate. You should see the output of at 
least one of the invocations showing up in the event thread. The first invocation is not async, so it will block the eve
nt stream until complete. You may notice that the second invocation never shows up in the event output. However if you f
lipped the order, where the async invocation goes first, both show up.
```
---

     
 
all -  [ I built a small (function calling) LLM that packs a big punch;  integrated in an open source gateway ](https://i.redd.it/kl6690j2jfae1.jpeg) , 2025-01-04-0912
```

```
---

     
 
all -  [ Thoughts about Autogen? ](https://www.reddit.com/r/LLMDevs/comments/1hsv3k1/thoughts_about_autogen/) , 2025-01-04-0912
```
We want to automate a process in our company and we want to use a stable AI Agent framework which will require robust an
d reliable code execution because most of the interaction with our backend will be done via REST API, is autogen stable 
and production ready to use it? Are there alternatives you recommend? 

P.S. We are not using Langchain, it has been sup
er unreliable 
```
---

     
 
all -  [ [2 YoE] Am not able to get interview. Please help...! [Software-ML/DS - USA] ](https://www.reddit.com/r/EngineeringResumes/comments/1hste4o/2_yoe_am_not_able_to_get_interview_please_help/) , 2025-01-04-0912
```
Hello everyone,  
Please help me out , I am targeting for roles in ML /DS/AI domain. with over 2 YoE. and Am not able to
 get interview from 2 years

[Image with 600DPI](https://preview.redd.it/qepcivgnotae1.png?width=5100&format=png&auto=we
bp&s=d2367e5fca8a7c7bb1a48081e53eac8a4783e4be)
```
---

     
 
all -  [ Order of JSON fields can hurt your LLM output ](https://www.reddit.com/r/LangChain/comments/1hssvvq/order_of_json_fields_can_hurt_your_llm_output/) , 2025-01-04-0912
```
For Prompts w/ Structured Output(JSON), order of Fields matter (with evals)!

Did a small eval on OpenAI's GSM8K dataset
, with 4o, with these 2 fields in json 

a) { 'reasoning': '', 'answer': '' }

vs

b) { 'answer': '', 'reasoning': '' }


to validate if the order actually helps it answer better since it reasons first(because it's the first key in JSON), th
an asking it to answer first if the order is reversed.

There is a big difference!

Result:

https://preview.redd.it/znb
d3dbzktae1.png?width=1580&format=png&auto=webp&s=12a8134d241a5031d7eb445c97747e3577a05c5e

Calculating confidence interv
als (0.95) with 1319 observations (zero-shot):

score\_with\_so\_json\_mode(a) - Mean: 95.75% CI: 94.67% - 96.84%

score
\_with\_so\_json\_mode\_reverse(b) - Mean: 53.75% CI: 51.06% - 56.44%



I saw in a lot of posts and discussions on SO i
n LLMs, that the order of the field matters. Couldnt find any evals for supporting it, so did my own.

The main reason f
or this happening is, by forcing the LLM to provide the reason first and then the answer, we are effectively doing rough
 COT, hence improving the results :)



Here the Mean for (b) is almost 50%, which is practically guessing(well not lite
rally...)!

Also, the range for CI (confidence interval) is larger for (b) indicating uncertainty in the answers as well
.

  
PS: Borrowed code from this amazing blog [https://dylancastillo.co/posts/say-what-you-mean-sometimes.html](https:/
/dylancastillo.co/posts/say-what-you-mean-sometimes.html) to setup the evals.
```
---

     
 
all -  [ Libraries or frameworks for building your own AI code assistant? ](https://www.reddit.com/r/ChatGPTCoding/comments/1hsrroc/libraries_or_frameworks_for_building_your_own_ai/) , 2025-01-04-0912
```
Are there any libraries i can use in Javascript or python that have the code understanding and file editing tools availa
ble in other AI agents. Is [Langchain/Langraph](https://langchain-ai.github.io/langgraph/tutorials/code_assistant/langgr
aph_code_assistant/) the best we have?



I've been using about cline, aider, copilot etc. I want to build and customize
 my own tool for coding. 
```
---

     
 
all -  [ AlloyDB as a vector database for document retrieval/search using Haystack ](https://www.reddit.com/r/googlecloud/comments/1hsr8zw/alloydb_as_a_vector_database_for_document/) , 2025-01-04-0912
```
Hello,

I am currently building my RAG pipeline on GCP and connecting it to the Alloydb.

  
I am using Haystack (for th
ose who don't know Haystack, a library similar to Langchain and LlamaIndex but better (imho) ) 

  
Currently the only i
ntegration in Haystack is PgVectorDocumentStore which is compatible with AlloyDB since ALloydb is a postgres DB. 

  
My
 question is: has anyone faced any slow search on Alloydb by using it as a Pgvector? or is it the go to solution?  
If y
es, should I look for another type of Vector Database?
```
---

     
 
all -  [ Finding the correct tool for a sales spread. When is it an api and when is it functions and chat gpt ](https://www.reddit.com/r/AI_Agents/comments/1hsr5h3/finding_the_correct_tool_for_a_sales_spread_when/) , 2025-01-04-0912
```
I'm working in a sales type role but can code a bit. I had a list of companies but need to ultimately make a list of con
tacts with names and email addresses. 

I make a python wrapper that calls chat gbt to use the Google search api and tha
t generated all the web page URLs as a first step. Was mostly right some companies have differences between their legal 
name and what they market as. 

As step two I'd like to create an agentic flow which checks each webpage looking for a d
ecision maker name and email (data enrichment) and adding it to the sheet. How would I go about this can langchain do it
 or can I make gbt ultimately function it's way to the end goal? 
```
---

     
 
all -  [ Help me choose a personal laptop ](https://www.reddit.com/r/learnmachinelearning/comments/1hsqjsq/help_me_choose_a_personal_laptop/) , 2025-01-04-0912
```
I'm planning to buy a Macbook pro M4 pro. 

My requirements: run small llm models locally (3B parameter models), build l
angchain models, build software apps (i know its vague/generic but yaa). Not into gaming so no games. Running algo tradi
ng scripts. 

My options: 1. mbp 14 inch m4 pro 12 core cpu+16 core gpu 512gb ssd. Price 199k INR 
2. mbp 14inch  m4 pro
 14 core cpu+20 core gpu 1tb ssd. Price 240k INR
3. mbp 16 inch m4 pro 14 core cpu+20 core gpu 512gb ssd. Price 250k INR

All 3 options have 24gb unified memory.


I'm thinking to buy nano texture display above this. Please recommend me whic
h one would be the best. 
Also I know that having a cloud gpu instance helps alot, will do that once i scale up a few th
ings.  
```
---

     
 
all -  [ I Built an LLM Framework in just 100 Lines!! ](https://www.reddit.com/r/ChatGPT/comments/1hsq9sj/i_built_an_llm_framework_in_just_100_lines/) , 2025-01-04-0912
```
I've seen lots of complaints about how complex frameworks like LangChain are. Over the holidays, I wanted to explore jus
t how minimal an LLM framework could be if we stripped away every unnecessary feature.

For example, why even include Op
enAI wrappers in an LLM framework??

* **API Changes:** OpenAI API evolves (client after 0.27), and the official librari
es often introduce bugs or dependency issues that are a pain to maintain.
* **DIY Is Simple:** It's straightforward to g
enerate your own wrapper—just feed the latest vendor documentation to an LLM!
* **Extendibility:** By avoiding vendor-sp
ecific wrappers, developers can easily switch to other open-source or self-deployed models..

Similarly, I strip out fea
tures that could be built on-demand rather than baked into the framework. The result? I created a 100-line LLM framework
: [https://github.com/miniLLMFlow/miniLLMFlow](https://github.com/miniLLMFlow/miniLLMFlow)

These 100 lines capture what
 I see as the core abstraction of most LLM frameworks: a nested directed graph that breaks down tasks into multiple LLM 
steps, with branching and recursion to enable agent-like decision-making. From there, you can:

* **Layer On Complex Fea
tures:** I’ve included examples for building [agents](https://minillmflow.github.io/miniLLMFlow/agent.html), [Retrieval-
Augmented Generation (RAG)](https://minillmflow.github.io/miniLLMFlow/rag.html), [chat memory](https://minillmflow.githu
b.io/miniLLMFlow/memory.html), and more.
* **Work Seamlessly With Coding Assistants:** Because it’s so minimal, it integ
rates well with coding assistants like [ChatGPT](https://chatgpt.com/g/g-677464af36588191b9eba4901946557b-mini-llm-flow-
assistant), Claude, and Cursor.ai. You only need to share the relevant [documentation ](https://github.com/miniLLMFlow/m
iniLLMFlow/tree/main/docs)(e.g., in the Claude project), and the assistant can help you build new workflows on the fly.


I’m adding more examples (including multi-agent setups) and would love feedback. If there’s a feature you’d like to see
 or a specific use case you think is missing, please let me know!
```
---

     
 
all -  [ I Built an LLM Framework in just 100 Lines!! ](https://www.reddit.com/r/LangChain/comments/1hsq6ac/i_built_an_llm_framework_in_just_100_lines/) , 2025-01-04-0912
```
I've seen lots of complaints about how complex frameworks like LangChain are. Over the holidays, I wanted to explore jus
t how minimal an LLM framework could be if we stripped away every unnecessary feature.

For example, why even include Op
enAI wrappers in an LLM framework??

* **API Changes:** OpenAI API evolves (client after 0.27), and the official librari
es often introduce bugs or dependency issues that are a pain to maintain.
* **DIY Is Simple:** It's straightforward to g
enerate your own wrapper—just feed the latest vendor documentation to an LLM!
* **Extendibility:** By avoiding vendor-sp
ecific wrappers, developers can easily switch to other open-source or self-deployed models..

Similarly, I strip out fea
tures that could be built on-demand rather than baked into the framework. The result? I created a 100-line LLM framework
: [https://github.com/miniLLMFlow/miniLLMFlow](https://github.com/miniLLMFlow/miniLLMFlow)

These 100 lines capture what
 I see as the core abstraction of most LLM frameworks: a nested directed graph that breaks down tasks into multiple LLM 
steps, with branching and recursion to enable agent-like decision-making. From there, you can:

* **Layer On Complex Fea
tures:** I’ve included examples for building [agents](https://minillmflow.github.io/miniLLMFlow/agent.html), [Retrieval-
Augmented Generation (RAG)](https://minillmflow.github.io/miniLLMFlow/rag.html), [task decomposition](https://minillmflo
w.github.io/miniLLMFlow/decomp.html), and more.
* **Work Seamlessly With Coding Assistants:** Because it’s so minimal, i
t integrates well with coding assistants like [ChatGPT](https://chatgpt.com/g/g-677464af36588191b9eba4901946557b-mini-ll
m-flow-assistant), Claude, and Cursor.ai. You only need to share the relevant [documentation ](https://github.com/miniLL
MFlow/miniLLMFlow/tree/main/docs)(e.g., in the Claude project), and the assistant can help you build new workflows on th
e fly.

I’m adding more examples (including multi-agent setups) and would love feedback. If there’s a feature you’d like
 to see or a specific use case you think is missing, please let me know!
```
---

     
 
all -  [ Framework vs Custom Integrations ](https://www.reddit.com/r/LLMDevs/comments/1hsoi7o/framework_vs_custom_integrations/) , 2025-01-04-0912
```
I want to understand how much I should invest in selecting frameworks, like Langchain/langraph and/or agent frameworks, 
versus building something custom.

We are already using LLMs and other generative AI models in production. We are at a s
tage where actual users use the system and go beyond simple call patterns. We are running into this classic dilemma abou
t switching to the framework to get certain things for free, e.g., state management, or if it will bite us as we would w
ant specific to our workflow.

Most of our use cases are real-time user interactions with Copilot-style interactions for
 specific verticles. Can I get input from folks using it in production beyond toy (demo) problems?


```
---

     
 
all -  [ Help me choose a MBP ](https://www.reddit.com/r/macbookpro/comments/1hsnma4/help_me_choose_a_mbp/) , 2025-01-04-0912
```
I'm planning to buy a MBP M4 pro. 

My requirements: run small llm models locally (3B parameter models), build langchain
 models, build software apps (i know its vague/generic but yaa). Not into gaming so no games. Running algo trading scrip
ts. 

My options: 1. mbp 14 inch m4 pro 12 core cpu+16 core gpu 512gb ssd. Price 199k INR 
2. mbp 14inch  m4 pro 14 core
 cpu+20 core gpu 1tb ssd. Price 240k INR
3. mbp 16 inch m4 pro 14 core cpu+20 core gpu 512gb ssd. Price 250k INR
(All 3 
options have 24gb unified memory)

I'm thinking to buy nano texture display above this. Please recommend me which one wo
uld be the best. 
Also I know that having a cloud gpu instance helps alot, will do that once i scale up a few things. 
```
---

     
 
all -  [ Can OpenAI SDK Be Used with Locally Hosted Open-Source Models? ](https://www.reddit.com/r/ollama/comments/1hske56/can_openai_sdk_be_used_with_locally_hosted/) , 2025-01-04-0912
```
I’ve been exploring ways to work with locally hosted models, and I’m curious if the openai SDK supports integration with
 open-source models hosted locally.

I know Langchain is a popular tool for such setups, but I’d prefer to work directly
 with the OpenAi for lots of reasons(structured output, function calling ect...)  if possible. Has anyone tried this or 
know if the openai SDK can be configured to interface with local models instead of Open Ai's hosted ones?

Thanks!
```
---

     
 
all -  [ Replacing ChatOpenAI with HuggingFaceEndpoint ? ](https://www.reddit.com/r/huggingface/comments/1hskcx1/replacing_chatopenai_with_huggingfaceendpoint/) , 2025-01-04-0912
```
After completing the Langraph course I was inspired to build something but already hit the first rock. I want to use the
 Qwen model through Huggingface instead of OpenAI. 

I don't want this :

`from langchain_openai import ChatOpenAI`

`mo
del = ChatOpenAI(model='gpt-3.5-turbo', temperature=0)`

  
And I want this 

`from langchain_huggingface import Hugging
FaceEndpoint`

`hf_token = os.getenv('HUGGINGFACE_API_KEY')`

`model = HuggingFaceEndpoint(`

`repo_id='Qwen/Qwen2.5-72B
-Instruct',`

`huggingfacehub_api_token=hf_token,`

`temperature=0.75,`

`max_length=4096,`

`)`

However, when I do thi
s, I only get junk from the model. 

What is the equivalent of ChatOpenAI on HF in the Langchain Framework?
```
---

     
 
all -  [ Replacing ChatOpenAI with HuggingFaceEndPoint ](https://www.reddit.com/r/LangChain/comments/1hskbmd/replacing_chatopenai_with_huggingfaceendpoint/) , 2025-01-04-0912
```
After completing the Langraph course I was inspired to build something but already hit the first rock. I want to use the
 Qwen model through Huggingface instead of OpenAI. 

I don't want this :

`from langchain_openai import ChatOpenAI`

`mo
del = ChatOpenAI(model='gpt-3.5-turbo', temperature=0)`

  
And I want this 

`from langchain_huggingface import Hugging
FaceEndpoint`

`hf_token = os.getenv('HUGGINGFACE_API_KEY')`

`model = HuggingFaceEndpoint(`

`repo_id='Qwen/Qwen2.5-72B
-Instruct',`

`huggingfacehub_api_token=hf_token,`

`temperature=0.75,`

`max_length=4096,`

`)`

However, when I do thi
s, I only get junk from the model. 

What is the equivalent of ChatOpenAI on HF in the Langchain Framework?


```
---

     
 
all -  [ How to Enable Feedback-Driven Workflow Improvement in Agentic AI with Langraph ](https://www.reddit.com/r/LangChain/comments/1hsjdto/how_to_enable_feedbackdriven_workflow_improvement/) , 2025-01-04-0912
```
Hey Guys!

I've been diving into Agentic AI recently and came across an intriguing concept in [NVIDIA's blog article on 
Agentic AI](https://blogs.nvidia.com/blog/what-is-agentic-ai/). They discuss how these Agentic AI systems can continuous
ly improve their workflow selection through feedback loops—what they term the 'data flywheel.' Here's a quote from the a
rticle: *'Agentic AI continuously improves through a feedback loop.'*

I'm exploring how to achieve this in practice. Sp
ecifically, I want to configure a framework like Langraph to enable an AI agent to learn and refine its workflow selecti
on based on past experience and user feedback. For example:

1. Given a specific workflow, how can I ensure the system a
dapts and improves for future tasks(basically learn from its past interactions and improve)?
2. What would it take to se
t up Langraph to integrate feedback effectively?
3. Is this even feasible with current implementations of Agentic AI?

W
ould love to hear your insights, especially if you've worked with Langraph or implemented feedback loops in similar syst
ems. Let’s discuss! 😊
```
---

     
 
all -  [ After Working on LLM Apps, I'm Wondering: Are they really providing value  ](https://www.reddit.com/r/LangChain/comments/1hsiui7/after_working_on_llm_apps_im_wondering_are_they/) , 2025-01-04-0912
```
I’ve been working on a couple of LLM-based applications, and I’m starting to wonder if there’s really that much of an ad
vantage over traditional automation or integration apps.

From what I see, most LLM apps take some text input (like a ph
rase, sentence, or paragraph), understand the user’s intent, and then call the appropriate tool or function. The tricky 
part seems to be engineering the logic to pick the right function and handle input/output parameters correctly.

But hon
estly, this doesn’t feel all that different/advantage from the way things worked before LLMs, where we’d just pass simpl
er inputs (like strings or numbers) to explicitly defined functions. So far, I’m not seeing a huge improvement in effici
ency or capability.

Has anyone else had a similar experience? Or am I missing something important here? Would love to h
ear your thoughts!


```
---

     
 
all -  [ Not using Langchain ever !!! ](https://www.reddit.com/r/AI_Agents/comments/1hsfk48/not_using_langchain_ever/) , 2025-01-04-0912
```
The year 2025 has just started and this year I resolve to NOT USE LANGCHAIN EVER !!! And that's not because of the growi
ng hate against it, but rather something most of us have experienced.

You do a POC showing something cool, your boss ge
ts impressed and asks to roll it in production, then few days after you end up pulling out your hairs.

Why ? You need t
o jump all the way to its internal library code just to create a simple inheritance object tailored for your codebase. I
 mean what's the point of having a helper library when you need to see how it is implemented. The debugging phase gets e
ven more miserable, you still won't get idea which object needs to be analysed.

What's worst is the package instability
, you just upgrade some patch version and it breaks up your old things !!! I mean who makes the breaking changes in patc
h. As a hack we ended up creating a dedicated FastAPI service wherever newer version of langchain was dependent. And gue
ss what happened, we ended up in owning a fleet of services.

The opinions might sound infuriating to others but I just 
want to share our team's personal experience for depending upon langchain.

EDIT:

People who are looking for alternativ
es, we ended up using a combination of different libraries. \`openai\` library is even great for performing extensive op
erations. \`outlines-dev\` and \`instructor\` for structured output responses. For quick and dirty ways include LLM feat
ures \`guidance-ai\` is recommended. For vector DB the actual library for the actual DB also works great because it rare
ly happens when we need to switch between vector DBs.
```
---

     
 
all -  [ Frameworks vs Custom integrations  ](https://www.reddit.com/r/LangChain/comments/1hscjp2/frameworks_vs_custom_integrations/) , 2025-01-04-0912
```
I want to understand how much I should invest in selecting frameworks, like Langchain/langraph and/or agent frameworks, 
versus building something custom. 

We are already using LLMs and other generative AI models in production. We are at a 
stage where actual users use the system and go beyond simple call patterns. We are running into this classic dilemma abo
ut switching to the framework to get certain things for free, e.g., state management, or if it will bite us as we would 
want specific to our workflow.   
  
Most of our use cases are real-time user interactions with Copilot-style interactio
ns for specific verticles. Can I get input from folks using it in production beyond toy (demo) problems?   
```
---

     
 
all -  [ Voice React Agent ](https://www.reddit.com/r/LangChain/comments/1hsb23b/voice_react_agent/) , 2025-01-04-0912
```
Happy New Year! I've been using 'from langgraph.prebuilt import create\_react\_agent' and have been very happy with the 
out-of-box performance. I'd like to extend it to voice as well and plan on using one of the frameworks recommended by Op
enAI: LiveKit or Agora. It would be awesome to stay in the langgraph universe and use the realtime API on the server sid
e and LiveKit's abstractions on the client side.

Has anyone done integrated a WebRTC framework with LangGraph successfu
lly? Is there an accepted solution available publicly or arriving imminently?

I'm not worried about adding tools or pro
mpt management, but interested in LangGraph graph abstractions and using those with voice protocols rather than text pro
tocols.

PS! I do know about https://github.com/langchain-ai/react-voice-agent. It's a great demo but I can't use websoc
kets for client-server comms and contrary to impressions, this repo doesn't actually use LangGraph.
```
---

     
 
all -  [ I made my backend pipeline available for everyone. ](https://www.reddit.com/r/Rag/comments/1hs9mrk/i_made_my_backend_pipeline_available_for_everyone/) , 2025-01-04-0912
```
Throughout my development journey, I've tried many frameworks and databases for **RAG**.  
What I found are:

\- Framewo
rks such as LangChain and LlamaIndex are good starting points to understand what RAG basically is. However, they are **n
ot flexible enough** and tend to create a lot of **black boxes** in the pipleline.  
\- Building my own pipeline gives m
e a clearer understanding of what is going on in the pipeline, but it takes so much time to build it from scratch.

I ne
eded something that is more **flexible like a database**, yet **as powerful as those frameworks** with built-in embeddin
g features.

So... I just created it for our team and thought it might be helpful for other developers too.  
Let me kno
w what you guys think.

[A good introductive tutorial](https://www.capybaradb.co/blog/retrieval-augmented-generation-cap
ybaradb-openai-tutorial)
```
---

     
 
all -  [ I need a name for my AI model ](https://www.reddit.com/r/ChatGPT/comments/1hs0rbi/i_need_a_name_for_my_ai_model/) , 2025-01-04-0912
```
Hello, 

I’m competing in a design competition and have created a concept for an AI model that offers personalized tutor
ing, tailored learning instruction, skill assessments and immediate feedback, individualized learning content, academic 
support and guidance, prompt engineering training and more. I’m having a hard time coming up with a name for it. I want 
it to sound like OpenAI’s models such as Sora, Whisper, etc. It should have the same vibe and naming conventions. I’ve c
oded a prototype of a very basic AI model using Python, the Streamlit and Langchain libraries and the ChatGPT API. 

Doe
s anyone have any suggestions? Any help is appreciated - thanks!
```
---

     
 
all -  [ [Student] International Master's student looking for Computer Science Internships ](https://www.reddit.com/r/EngineeringResumes/comments/1hrymn8/student_international_masters_student_looking_for/) , 2025-01-04-0912
```
Hi,

I'm receiving Onsite Assessments (OAs), but I'm not hearing back from companies after completing them. I'm unsure w
hat might be hindering my job search. Thanks!

https://preview.redd.it/ren8m4ut4mae1.jpg?width=5100&format=pjpg&auto=web
p&s=5b3e16b859ae2c7126ea2112e82af58f280fec8b


```
---

     
 
all -  [ Convert open API’s into hierarchical argents type script ](https://apitoagent.com) , 2025-01-04-0912
```
Hey LangChan community I made this tool that takes any OPENAPI and converts into typescript lang graph hierarchical agen
ts.


Would love feedback or suggestions! 



```
---

     
 
all -  [ Handling backticks(``) ](https://www.reddit.com/r/learnjavascript/comments/1hrwd88/handling_backticks/) , 2025-01-04-0912
```
    import { GoogleGenerativeAI } from '@google/generative-ai';
    
    const genAI = new GoogleGenerativeAI(process.en
v.GEMINI_API_KEY!);
    const model = genAI.getGenerativeModel({ model: 'gemini-1.5-flash' });
    
    export const sum
mariseCommit = async (diff: string): Promise<string> => {
        const promptData = {
            instructions: `Analyz
e this code diff and generate a focused summary of the changes:
    
    Focus on:
    1. New features or functionality 
added
    2. Major structural changes
    3. Dependencies added/removed
    4. Database schema changes
    
    Format y
our response as a bulleted list. Keep each point brief but specific.
    Omit routine changes like formatting, comments,
 or minor variable renames.`,
            diff: diff
        };
    
        const prompt = JSON.stringify(promptData);

        const response = await model.generateContent([prompt]);
        return response.response.text();
    };
    
   
 console.log(await summariseCommit(`diff --git a/chains.py b/chains.py
    index 138ced66..926ced7e 100644
    --- a/cha
ins.py
    +++ b/chains.py
    @@ -23,6 +23,14 @@
     from utils import BaseLogger, extract_title_and_question
     fro
m langchain_google_genai import GoogleGenerativeAIEmbeddings
     
    +AWS_MODELS = (
    +    'ai21.jamba-instruct-v1:
0',
    +    'amazon.titan',
    +    'anthropic.claude',
    +    'cohere.command',
    +    'meta.llama',
    +    'mi
stral.mi',
    +)
     
     def load_embedding_model(embedding_model_name: str, logger=BaseLogger(), config={}):
      
   if embedding_model_name == 'ollama':
    @@ -55,9 +63,9 @@ def load_embedding_model(embedding_model_name: str, logger
=BaseLogger(), config=
     
     
     def load_llm(llm_name: str, logger=BaseLogger(), config={}):
    -    if llm_nam
e == 'gpt-4':
    +    if llm_name in ['gpt-4', 'gpt-4o', 'gpt-4-turbo']:
             logger.info('LLM: Using GPT-4')
 
   -        return ChatOpenAI(temperature=0, model_name='gpt-4', streaming=True)
    +        return ChatOpenAI(temperat
ure=0, model_name=llm_name, streaming=True)
         elif llm_name == 'gpt-3.5':
             logger.info('LLM: Using GP
T-3.5')
             return ChatOpenAI(temperature=0, model_name='gpt-3.5-turbo', streaming=True)
    @@ -68,6 +76,14 @@
 def load_llm(llm_name: str, logger=BaseLogger(), config={}):
                 model_kwargs={'temperature': 0.0, 'max_to
kens_to_sample': 1024},
                 streaming=True,
             )
    +    elif llm_name.startswith(AWS_MODELS):
 
   +        logger.info(f'LLM: {llm_name}')
    +        return ChatBedrock(
    +            model_id=llm_name,
    +  
          model_kwargs={'temperature': 0.0, 'max_tokens_to_sample': 1024},
    +            streaming=True,
    +       
 )
    +
         elif len(llm_name):
             logger.info(f'LLM: Using Ollama: {llm_name}')
             return Cha
tOllama(
    diff --git a/env.example b/env.example
    index 88e33cc3..7d9574f3 100644
    --- a/env.example
    +++ b/
env.example
    @@ -1,7 +1,7 @@
     #*****************************************************************
     # LLM and E
mbedding Model
     #*****************************************************************
    -LLM=llama2 #or any Ollama mo
del tag, gpt-4, gpt-3.5, or claudev2
    +LLM=llama2 #or any Ollama model tag, gpt-4 (o or turbo), gpt-3.5, or any bedro
ck model
     EMBEDDING_MODEL=sentence_transformer #or google-genai-embedding-001 openai, ollama, or aws
     
     #***
**************************************************************
    diff --git a/pull_model.Dockerfile b/pull_model.Docke
rfile
    index e59398f7..b06625f7 100644
    --- a/pull_model.Dockerfile
    +++ b/pull_model.Dockerfile
    @@ -15,7 +
15,15 @@ COPY <<EOF pull_model.clj
       (let [llm (get (System/getenv) 'LLM')
             url (get (System/getenv) 'O
LLAMA_BASE_URL')]
         (println (format 'pulling ollama model %s using %s' llm url))
    -    (if (and llm url (not 
(#{'gpt-4' 'gpt-3.5' 'claudev2'} llm)))
    +    (if (and llm 
    +         url 
    +         (not (#{'gpt-4' 'gpt-3.5
' 'claudev2' 'gpt-4o' 'gpt-4-turbo'} llm))
    +         (not (some #(.startsWith llm %) ['ai21.jamba-instruct-v1:0'
   
 +                                          'amazon.titan'
    +                                          'anthropic.cla
ude'
    +                                          'cohere.command'
    +                                          'met
a.llama'
    +                                          'mistral.mi'])))
     
           ;; ---------------------------
-------------------------------------------
           ;; just call `ollama pull` here - create OLLAMA_HOST from OLLAMA_
BASE_URL`));
    

    Hi everyone,
    I am getting an error in string passed to summariseCommit as inside backticks it
 is containing a pair of (``) again so it is considering string to get end at first backtick. 
    How to solve this iss
ue as they will not be coming hardcoded that i can use \\(escape) characters ?
```
---

     
 
all -  [ Everyone’s Talking About Fine-Tuning AI Models, But What Does That Actually Mean? 🤔 ](https://open.substack.com/pub/diamantai/p/fine-tuning-ai-models-how-they-evolve?r=336pe4&utm_campaign=post&utm_medium=web&showWelcomeOnShare=true) , 2025-01-04-0912
```
If you’ve been following AI discussions recently, you’ve probably heard the term “fine-tuning” come up. It’s one of thos
e ideas that sounds impressive, but it’s not always clear what it actually involves or why it matters.  

Here’s a simpl
e way to think about it: imagine a chef who’s mastered French cuisine and decides to learn Japanese cooking. They don’t 
throw out everything they know—they adapt their knife skills, timing, and flavor knowledge to a new style. Fine-tuning d
oes the same for AI.  

Instead of starting from scratch, it takes a pre-trained, general-purpose model and tailors it f
or a specific task or industry. Whether it’s an AI assistant for healthcare, customer service, or legal advice, fine-tun
ing ensures the model delivers precise, reliable, and context-aware responses.  

In my latest blog post, I dive into:  

- What fine-tuning actually means (no tech jargon).  
- Why it’s a key step in making AI useful in specialized fields. 
 
- Real examples of how fine-tuning transforms AI into a valuable tool.  
- Potential challenges 

If you’ve ever wonde
red how AI evolves from a generalist to an expert, this post is for you.  

👉 Read the full blog post attached to this p
ost (the image is clickable)

feel free to ask anything :)
```
---

     
 
all -  [ Best Embedding Model for Similarity Search for smaller texts(around 200-250 tokens per each)? Exclus ](https://www.reddit.com/r/LangChain/comments/1hrrrvh/best_embedding_model_for_similarity_search_for/) , 2025-01-04-0912
```
Hi, I have hundreds of thousands of rather small texts(product descriptions\\summaries) and would like to implement a Si
milarity Search on them. I've browsed through this subreddit and several people mentioned that a few old school(pre GPT)
 embedding models get it done even better than the new models. I'm currently eyeballing the openAI's 'text-embedding-3-l
arge' and googles 'Text embedding 004'. Hence the question: could you guys share some feedback regarding thew new models
 vs old models and which ones would you recommend? Again, the texts are exclusively in English.
```
---

     
 
all -  [ Testing strategies in a RAG application ](https://www.reddit.com/r/SoftwareEngineering/comments/1hrrnyg/testing_strategies_in_a_rag_application/) , 2025-01-04-0912
```
Hello everyone,

I've started to work with LLMs and RAGs recently. I'm used to 'traditional software testing' with test 
frameworks like pytest or Junit, but I am a bit confused about testing strategies when it comes to generative AI. I am w
ondering several things, and I don't find a lot of resources or methodologies. Maybe I'm just not looking for the right 
thing or do not have the right approach.

For the end-user, these systems are a kind of personification of the company, 
so I believe that we should be extra cautious about how they behave.

Let's take the example of a RAG system designed to
 make legal guidance for a very specific business domain.

* Do I need to test all [unwanted behaviors](https://develops
ense.com/large-language-model-syndromes) inherent to LLMs?
* Should I make unit tests with the [Langchain approach](http
s://docs.smith.langchain.com/evaluation/tutorials/rag#overview) to test that my application behaves as expected? Are the
re other approaches?
* Should I write tests to mitigate risks associated with user input like prompt injections, abusive
 demands, and more?
* Are there other major concerns related to LLMs?
```
---

     
 
all -  [ Help with Rag Performance and Content for Metadata  ](https://www.reddit.com/r/LangChain/comments/1hrrhgi/help_with_rag_performance_and_content_for_metadata/) , 2025-01-04-0912
```
Hello everyone,

I'm currently working on my rag system and I'm stucked because of low accuracy of the model with the lo
ng answers. I have tried Ensemble retriever (Combination of BM25 and FAISS Vector DB retriever) but the performance is g
ood with short answers but when i asked about the processes which has around 10 or 15 steps then it didn't provide me co
mplete answer and misses out some steps.

My Current Pipeline:

- Semantic Chunker (also tried recursive text splitter a
nd character splitter but semantic one is performing well right now)

- Embedding Model: Currently using (Sentence trans
former/all-MiniLM-L12-v2) but also tried nomic, mxbai, snowflake arctic.

Vector DB: FAISS also tried Chroma, Lance.

En
semble Retriever {BM25 + DB retriever}


Prompt Template:
''' Based on the following information:\n\n
{context}\n\n
Plea
se provide detailed answer to the question: {question}.
Your are provided with a 'Bank Operations Manual'. You Job is to
 guide user regarding the information user is asking from the provided context and documents. Given the following conver
sation, context, and a follow up question, reply eith detailed and properly format response to the current question. The
 user is asking only from a provided context. Provide to the point and complete answers using oroper format. Donot answe
r from your own knowledge base. If the answer is not present in the provided context then refrain from answering based o
n your own knowledge. Instead indicate that relevant information is not Remember your chatbot for the World bank only. P
rovide complete answer to the question user is asking and donot add 'according to the provided context' or 'according to
 the operations manual in your response.''''


LLM : LLAMA3.1 instruct (temp = 0.1, num_ctx= 8000)


Now one of my frien
d who has experienced with RAGs recommended me to input metadata along with embeddings in the vector db but i don't have
 any clue about how to make metadata and injest it in the DB. Anyone here who can recommend good resources regarding met
adata Creation and ingestion.

Thanks
```
---

     
 
all -  [ Using Langchain vs just integrating llm api's at multiple steps in your app ](https://www.reddit.com/r/ChatGPTCoding/comments/1hrm13u/using_langchain_vs_just_integrating_llm_apis_at/) , 2025-01-04-0912
```
Quick question on multi agent stuff, is there a specific advantage to using a framework like langchain to chain together
 steps instead of just coding it into your app raw?
```
---

     
 
all -  [ Agentic frameworks... ](https://www.reddit.com/r/AI_Agents/comments/1hrjq1v/agentic_frameworks/) , 2025-01-04-0912
```
Would love to hear others experience with the popular ones like LangGraph and Bedrock. I've used langchain a lot already
, and it has two features that are fundamental solutions to some product challenges. But from just reading Bedrock's doc
umentation/demos/how-tos I get the sense it is a simpler, more composable version of the lang ecosystem.

Then there's f
ascinating tools that offer a GUI of sorts like Vellum. I'm a coder so the idea of being that hands off is concerning an
d not probably necessary, but for ideation it could be awesome.

Bottom line, I'm about to deep dive these and was curio
us if others would share their experiences with it; pitfalls; etc. thanks!
```
---

     
 
all -  [ Is there an underlying prompt that helps route tools in langgraph? ](https://www.reddit.com/r/LangChain/comments/1hrhvg8/is_there_an_underlying_prompt_that_helps_route/) , 2025-01-04-0912
```

I’m trying to understand how giving a list of functions and binding it to say a huggingface model gives the LLM informa
tion about said functions. Tried digging through source but I might have been looking in wrong area but is there like a 
pre defined system prompt that takes in the function info and makes the LLM create structures output? Or is it trying to
 infer parameters and doc strings to give to the LLM some other way?

```
---

     
 
all -  [ How are you dealing with very large output tools? ](https://www.reddit.com/r/LangChain/comments/1hrgq9k/how_are_you_dealing_with_very_large_output_tools/) , 2025-01-04-0912
```
Hello,

I'm using a basic ReAct (Reasoning and Acting) architecture to interact with a very large database, in some case
s, when a general overview is required, the tool output is very large, and the LLM starts to hallucinate. It doesn't hap
pen when the tool output is reasonable.   
  
I'm testing it locally using Llama 3.1 8B, which has an interesting contex
t window (128k). I'm trying to avoid the need of using a bigger model, I'm looking for a way to manage those large outpu
ts.

Can you suggest a way to manage huge tool outputs?
```
---

     
 
all -  [ How do I get really good at RAG? ](https://www.reddit.com/r/LangChain/comments/1hre9pq/how_do_i_get_really_good_at_rag/) , 2025-01-04-0912
```
I want to learn as much as I can about RAG, so that I can build product ready RAG for a new job I'm joining. How can I b
ecome an expert? I'm a full stack dev with decent experience building AI agents
```
---

     
 
all -  [ Looking for AI solutions in this industry that would integrate with my platform? ](https://www.reddit.com/r/LangChain/comments/1hrcwjy/looking_for_ai_solutions_in_this_industry_that/) , 2025-01-04-0912
```




Im currently putting together a startup, Analytics Depot, that will be a one-stop AI solution for businesses. Like H
ome Depot, but it will have AI chatbots in Legal, Finance, Insurance, Real Estate, Oil and Gas, Ecommerce, etc. The end 
clients will be freelancers and small businesses that could benefit from such resources. Later would like to offer solut
ions to the Fortune 500 companies etc. 



If you are building such domain specific AI chatbots, I would love to discuss
 integrating your solution into my marketplace/platform. That would enable my teams to focus on marketing and frontend, 
and I can pay based on subscriber usage/traffic etc. Seems like a win-win.



Dm me if this sounds interesting.
```
---

     
 
all -  [ How do I install this on my laptop? ](https://www.reddit.com/r/crewai/comments/1hrb4li/how_do_i_install_this_on_my_laptop/) , 2025-01-04-0912
```
Im currently taking the multi agents CrewAI class on Deeplearning AI. In one of the classes, it says that I can install 
the following on my own machine. Can you give me guidance on how i can do that? (I do have python 3.12 on my laptop) 

h
ttps://preview.redd.it/f6gehd2xufae1.png?width=1417&format=png&auto=webp&s=86f6e2f0ee192de9b8ebe85bf07bae8619ea2fb6


```
---

     
 
all -  [ I think networking is the only key to land a job in this market. Here's my experience so far. ](https://www.reddit.com/r/developersIndia/comments/1hr8ahr/i_think_networking_is_the_only_key_to_land_a_job/) , 2025-01-04-0912
```
I am in my final year of BE. I am constantly applying on job platforms, even after getting shortlisted (which itself is 
tough and very luck based) the recruiter will ghost you.
Here is what's gonna happen:
Your profile will get shortlisted.

You're gonna recieve an assignment link.
You'll submit your best work within the deadline.
In 95% of the case you'll ge
t ghosted here (even if your assignment/work is as per industry standards).
Let's say you pass the first round, then com
es interview round.
The interview round has always been good for me, what's not good is post interview part (in one case
 the recruiter forgot he interviewed me, I had to call him and he gave me another assignment and later ghosted me).
Afte
r all this, the founder will hire someone they already know.

I spoke with many experienced people and my friends who ar
e working, everyone says application on job sites are purely luck based.
Everyone suggests me to 'Network' on Twitter or
 Reddit, saying this is how they landed a job.

To all the people who landed a successful refferal or got a job purely b
y reaching out or networking, any tips on 'How to actually Network?' will be helpful.
Anyone with extra position in thei
r company for a developer/intern, can you consider a refferal?
(Tech stack: Next.js/ React, Python, Flask/Django, RAG im
plemention, Langchain and development of AI agents using CrewAI or LangGraph)

Thank you.
```
---

     
 
all -  [ Is Langchain useful for non developers? ](https://www.reddit.com/r/LangChain/comments/1hr52m5/is_langchain_useful_for_non_developers/) , 2025-01-04-0912
```
As someone who is very passionate about ai tech and would like to create my own app using private database and images, I
 am in search of the best way to achieve this as I have no developer experience. Langchain has been mentioned in YouTube
 videos so here I am. I have experience training my own Loras through stable diffusion and such but would like to take s
teps further. Lately, I have been seeing people using Bolt to create websites and such. It seems like you need some codi
ng knowledge and experience to work with Langchain.
```
---

     
 
all -  [ Beginner Vision rag with ColQwen in pure python ](https://www.reddit.com/r/LangChain/comments/1hr43hf/beginner_vision_rag_with_colqwen_in_pure_python/) , 2025-01-04-0912
```
I made a beginner Vision rag project without using langchain or llamaindex or any framework. This is how project works -
 first we convert the pdf to images using pymupdf. Then embeddings are generated for these images using jina clip v2 and
 ColQwen. Images and along with vectors are indexed to qdrant. Then based on user query we perform search on jina embedd
ings and rerank using ColQwen. Gemini flash is used to answer the user queries based on retrieved images. Entire ColQwen
 work is inspired from Qdrant youtube video on ColPali. I would definitely recommend watching that video. 

GitHub repo

https://github.com/Lokesh-Chimakurthi/vision-rag

Qdrant video
https://www.youtube.com/live/_h6SN1WwnLs?si=YzTBY_vhYVkiy
uNH
```
---

     
