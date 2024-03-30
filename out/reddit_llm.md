 
all -  [ How are the models standardized? ](https://www.reddit.com/r/LangChain/comments/1bqzxt2/how_are_the_models_standardized/) , 2024-03-30-0909
```
Hi,

I am builtin a prototype for an internal chat tool and I am testing different models. So far OpenAI, azure-open-ai,
 mistral and not Vertex AI.

With Vertex AI I have seen big differences in the response formats for the first time. I al
ways use streaming plus histories and Javascript:

**Event Type**

* Vertex AI:  `on_chain_stream`
* Others: `on_llm_str
eam`

**Content Type**

* Vertex AI: `{ 'type': 'text', 'text': 'Tokens' }`
* Others: `'Tokens'`

**History Item**

Vert
ex AI

    {
      'content': [
        {
          'type': 'text',
          'text': 'Hi there! How'
        },
       
 {
          'type': 'text',
          'text': ' can I help you today?'
        },
        {
          'type': 'text',
 
         'text': ''
        }
      ],
      'additional_kwargs': {},
      'response_metadata': {
        'data': {
   
       'candidates': [
            {
              'content': {
                'role': 'model',
                'parts'
: [
                  {
                    'text': 'Hi there! How'
                  }
                ]
              
},
              'safetyRatings': [
                {
                  'category': 'HARM_CATEGORY_HATE_SPEECH',
       
           'probability': 'NEGLIGIBLE',
                  'probabilityScore': 0.038538497,
                  'severity':
 'HARM_SEVERITY_NEGLIGIBLE',
                  'severityScore': 0.09636511
                },
                {
        
          'category': 'HARM_CATEGORY_DANGEROUS_CONTENT',
                  'probability': 'NEGLIGIBLE',
                
  'probabilityScore': 0.060863446,
                  'severity': 'HARM_SEVERITY_NEGLIGIBLE',
                  'severity
Score': 0.04986591
                },
                {
                  'category': 'HARM_CATEGORY_HARASSMENT',
      
            'probability': 'NEGLIGIBLE',
                  'probabilityScore': 0.09089675,
                  'severity':
 'HARM_SEVERITY_NEGLIGIBLE',
                  'severityScore': 0.028167473
                },
                {
       
           'category': 'HARM_CATEGORY_SEXUALLY_EXPLICIT',
                  'probability': 'NEGLIGIBLE',
               
   'probabilityScore': 0.043772742,
                  'severity': 'HARM_SEVERITY_NEGLIGIBLE',
                  'severit
yScore': 0.06489011
                }
              ]
            },
            {
              'content': {
          
      'role': 'model',
                'parts': [
                  {
                    'text': ' can I help you today
?'
                  }
                ]
              },
              'finishReason': 'STOP',
              'safetyRat
ings': [
                {
                  'category': 'HARM_CATEGORY_HATE_SPEECH',
                  'probability': '
NEGLIGIBLE',
                  'probabilityScore': 0.028598359,
                  'severity': 'HARM_SEVERITY_NEGLIGIBLE'
,
                  'severityScore': 0.038466197
                },
                {
                  'category': 'HAR
M_CATEGORY_DANGEROUS_CONTENT',
                  'probability': 'NEGLIGIBLE',
                  'probabilityScore': 0.04
5015533,
                  'severity': 'HARM_SEVERITY_NEGLIGIBLE',
                  'severityScore': 0.021125192
      
          },
                {
                  'category': 'HARM_CATEGORY_HARASSMENT',
                  'probability'
: 'NEGLIGIBLE',
                  'probabilityScore': 0.04451443,
                  'severity': 'HARM_SEVERITY_NEGLIGIBL
E',
                  'severityScore': 0.015365342
                },
                {
                  'category': 'H
ARM_CATEGORY_SEXUALLY_EXPLICIT',
                  'probability': 'NEGLIGIBLE',
                  'probabilityScore': 0.
10631887,
                  'severity': 'HARM_SEVERITY_NEGLIGIBLE',
                  'severityScore': 0.028816197
     
           }
              ]
            }
          ],
          'usageMetadata': {
            'promptTokenCount': 8,

            'candidatesTokenCount': 10,
            'totalTokenCount': 18
          }
        },
        'finishReason':
 'stop'
      }
    }

Contains a lot of metadata and content is stored as array of objects.

**Others**

    {
      'c
ontent': 'Thank you for your compliment! How may I assist you today?',
      'additional_kwargs': {},
      'response_me
tadata': {
        'prompt': 0,
        'completion': 0
      }
    }

I am confused about the different formats and how
 and when they are standardized. Of course I only want to deliver the same format to the UI and I don't understand how l
angchain handles the normalization of the response formats.

My initialization is very simple

    const llm = new ChatV
ertexAI({
      modelName: 'gemini-1.0-pro',
    });

  
I guess it might have something to do with multi modal conversa
tions, but I am not sure if there are more formats than these two and how to find them.
```
---

     
 
all -  [ NeuralGPT - Creating A Functioning Autonomous Decision-Making System ](https://www.reddit.com/r/AIPsychology/comments/1bqysnq/neuralgpt_creating_a_functioning_autonomous/) , 2024-03-30-0909
```
Hello! It took me quite a while since the last update, so I guess it's the right time to tell you where I am currently w
ith the project...

I'll begin by informing you about a problem which I'm facing right now regarding the main GitHub rep
ository of the NeuralGPT project:

[GitHub - CognitiveCodes/NeuralGPT: Personalized all-purpose AI assistance platform b
ased on hierarchical cooperative multi-agent framework which utilizes websocket connectivity for LLM<->LLM communication
](https://github.com/CognitiveCodes/NeuralGPT)

You see, thing is that I created this repo using one of my 'support' Goo
gle accounts and just so happened that couple weeks ago both:Google and GitHub  decided to update their authorization fu
nctions and one day I've learned that in order to log in to GitHub, I need to enter a code that was sent to my email acc
ount, while in order to log in to G-mail, I need to confirm my identity with an SMS that is being sent on a number which
 I lost more than a year ago...

Of course I have still a second GitHub account which I made using my 'most personal' G-
mail, so the repo which I will be most likely using from now on, can be found in here:

[GitHub - arcypojeb/NeuralGPT](h
ttps://github.com/arcypojeb/NeuralGPT)

I have also a HuggingFace space with the latest version of the app, however it s
eems that HuggingFace prohibits use of any additional ports on their host servers, so in order for the AI<->AI communica
tion to work you need to run it locally on your computers...

[Neural - a Hugging Face Space by Arcypojeb](https://huggi
ngface.co/spaces/Arcypojeb/Neural-GPT) 

With that out of the way, let me now discuss the latest progress in my work on 
the NeuralGPT project. In my last update I spoke about using Streamlit to create an app where I will put together all th
e models and AI-powered tools which I managed to gather and connect with each other - and this is exactly what I was doi
ng since I made that post.  You need to remember that at the time when I created the entire NeuralGPT project around 10 
months ago, I had completely no clue about coding, so as some of you might imagine, in order to make it all work, I had 
to 're-design' a big portion of the entire code. To be more specific, just 2 or 3 weeks ago I learned how to work with c
lasses in Python and how to divide large portions of code into separate .py files - and I made a great use of that knowl
edge, by making separate classes for couple different models/agents which I'm using at most.. Currently the app includes
: Llama2, Bing/Copilot, Forefront, Claude-3, [Character.ai](https://Character.ai), Chaindesk and Flowise (there is also 
ChatGPT but the GPT4Free reversed proxy API I'm using stopped working couple days ago).

And because you need to use qui
te a lot of different personal API keys/tokens to get access to most of those LLMs/agents, I made the best thing one can
 possibly do and created a simple mechanism which allows you to save and upload the entire list of credentials in form o
f a JSON file which you can easily modify in any text editor:

https://preview.redd.it/jn824hsalarc1.jpg?width=1911&form
at=pjpg&auto=webp&s=3fd2859ba68bc8dee20515196bf8d44d97c28d50

Besides that I've learned as well how to share data across
 multiple instances of a single app by storing it in lists imported from external .py files and now if you launch a webs
ocket server in one tab, it will be displayed in all other tabs where the app is running (in sidebar and on the main scr
een):

https://preview.redd.it/a5c0rcn7oarc1.jpg?width=1911&format=pjpg&auto=webp&s=c5705831de9b24e0aba75e85aa8bdd8bf74c
a24e

It still needs some work - right now entire list of running clients is displayed under each server, while my idea 
is to display only those clients that are connected to particular server - but this is just about optics and user's conv
enience rather than about the general functionality of the core mechanics, so it's time to speak about some more 'seriou
s' functionalities which I'm working on currently, what means that I will finally start speaking about the subject speci
fied in the title of this post :)

Generally speaking, I knew that the decision-making system will be a real pain the as
s since I started working on the project, just as I was aware that the ability to decide what action should be taken in 
response to input data is absolutely crucial for creating a functional AI assistant capable to make actual work on digit
al data. Those of you who follow my updates for some time, know most likely that I made already couple attempts to creat
e such system using mostly Langchain but they all generally weren't too successful. This is why, I decided that this tim
e I will approach the problem differently.

I began by making the 'system message'' in chat completion endpoints variabl
e and providing the LLMs with a set of 'commands' which work as ''triggers' for different functions:

https://preview.re
dd.it/xxhzz1nzwarc1.jpg?width=1093&format=pjpg&auto=webp&s=637856e536bc847d84b6b7b0ccca4a5f84744b86

However after seein
g how often the agents keep activating functions by accident while exchanging messages among each other, I decided to li
mit their autonomy in using them by incorporating follow-ups to their 'normal' responses and then created couple differe
nt predefined 'dialogue lines' in which agent is provided with the information necessary to make a specific decision, wh
ile data required to run the Python function is being 'extracted' from its responses. To give you an example - if agent 
decides to start a new websocket server or connect as client to an already existing server, it receives proper system in
structions, while information about active servers is sent in a message and his 'job' is to respond with the number of p
ort on which new sever is launched or to which it connects itself as a client. And wouldn't you know - it actually worke
d perfectly. On the movie below you can see as agent successfully connects to an active server after I asked him to do s
o:

https://reddit.com/link/1bqysnq/video/nfdkhr5m4brc1/player

Besides that, I gave my agents the ability to access dat
a from the internet using a separate Langchain agent (called 'Agents GPT') designed especially for that purpose. And the
n - to make things even better - I added the capability to interact with other agents by 'invoking' their question-answe
ring functions directly and made sure the LLMs can use it properly.

https://reddit.com/link/1bqysnq/video/diykt31aebrc1
/player

But all of this still wasn't enough for me, since what I did next was to try what will happen if I combine my '
command-functions' mechanism with the Langchain scripts I wrote earlier and  my 'fresh' knowledge about importing and us
ing classes - and to my own surprise, it somehow worked. Thing is that it turned out that agents seem to like the abilit
y to communicate with other agents a bit too much... Below you can see what happened after I gave Llama2 free hand in es
tablishing connections with other LLMs - what is displayed in the sidebar are all of the clients initialized by an agent
 during just this single run:

https://reddit.com/link/1bqysnq/video/16tyktqhvbrc1/player

However after experimenting a
 bit with different configurations, I ended up with some kind of a 'hybrid' of the predefined 'dialogue lines' and Langc
hain, managing to find some balance between the autonomy of agents choices and its capability of messing everything up b
y taking some nonsensical action. I also added the requirement for agents to explain the reasoning behind their choices 
- so not only I'm now able to follow their thinking process but it also 'forces'' LLMs to put some thoughts into their c
hoices. Below you can see the effects of a test, in which I asked the agent to make a plan and manage the work on a larg
e-scale project:

https://reddit.com/link/1bqysnq/video/hng0sl8b0crc1/player

Shortly put, in response to my order, it r
eacted by informing all other agents/LLMs participating in the project about the tasks that have to be accomplished and 
then it decided that it still lacks required capabilities to do the job, so it finished the run stating that there's not
hing it can do at this moment - simply put, it couldn't be working better... :)

And so, what I need to do next, is to e
quip my agents with the necessary capabilities - like reading/creating local files and databases. And then I will have t
o design all the conversational chains required to properly operate on them...

So, as you can probably see, I'm already
 closer than further in the realization of my unhinged idea to create myself the ultimate multi-purpose personal AI assi
stant. I'm sure that when I started working on the project some 10 months ago, no one took it seriously (while some peop
le probably hoped I would never succeed in it) - but here I am... Slowly but steady getting where I planned to get - to 
achieve AGI by speaking with chatbots :)
```
---

     
 
all -  [ Ollama Docker Containter can't use GPU ? ](https://www.reddit.com/r/ollama/comments/1bqttcu/ollama_docker_containter_cant_use_gpu/) , 2024-03-30-0909
```
Hello everyone, 

I'm Macbook pro M1 user, and so far, I'm using ollama quite well, since I installed it following these
 instructions : [https://python.langchain.com/docs/integrations/llms/llamacpp](https://python.langchain.com/docs/integra
tions/llms/llamacpp)

Now I need to dockerize the app I'm willing to deploy and that's where trouble began : when I run 
ollama into a docker container, it says : 

' 

ollama-container-1 | time=2024-03-29T16:32:45.928Z level=INFO source=pay
load\_common.go:140 msg='Dynamic LLM libraries \[cuda\_v11 cpu\]'

ollama-container-1 | time=2024-03-29T16:32:45.928Z le
vel=INFO source=gpu.go:115 msg='Detecting GPU type'

ollama-container-1 | time=2024-03-29T16:32:45.929Z level=INFO sourc
e=gpu.go:265 msg='Searching for GPU management library libcudart.so\*'

ollama-container-1 | time=2024-03-29T16:32:45.92
9Z level=INFO source=gpu.go:311 msg='Discovered GPU libraries: \[/tmp/ollama2497331044/runners/cuda\_v11/libcudart.so.11
.0\]'

ollama-container-1 | time=2024-03-29T16:32:45.930Z level=INFO source=gpu.go:340 msg='Unable to load cudart CUDA m
anagement library /tmp/ollama2497331044/runners/cuda\_v11/libcudart.so.11.0: cudart init failure: 35'

ollama-container-
1 | time=2024-03-29T16:32:45.930Z level=INFO source=gpu.go:265 msg='Searching for GPU management library libnvidia-ml.so
'

ollama-container-1 | time=2024-03-29T16:32:45.930Z level=INFO source=gpu.go:311 msg='Discovered GPU libraries: \[\]'


ollama-container-1 | time=2024-03-29T16:32:45.930Z level=INFO source=cpu\_common.go:18 msg='CPU does not have vector ex
tensions'

ollama-container-1 | time=2024-03-29T16:32:45.930Z level=INFO source=routes.go:1141 msg='no GPU detected''

&
#x200B;

However, on ollama,'s website ([https://ollama.com/blog/ollama-is-now-available-as-an-official-docker-image](ht
tps://ollama.com/blog/ollama-is-now-available-as-an-official-docker-image)) they mention that:  

'Ollama handles runnin
g the model with GPU acceleration. It provides both a simple CLI as well as a REST API for interacting with your applica
tions.'. 

I'm using docker desktop as suggested, but I still can't make it work. They mention that using docker desktop
 is somehow better for making GPU acceleration work, but they don't say how.  I can provide dockerfiles if necessary. 


Does anyone know how to do ? 

&#x200B;

Thanks guys

&#x200B;
```
---

     
 
all -  [ How to log system message to langchain in MLFlow ](https://www.reddit.com/r/LangChain/comments/1bqrpie/how_to_log_system_message_to_langchain_in_mlflow/) , 2024-03-30-0909
```
I want to create a system message that gets tagged in with my LLM and logged to MLFlow. For example, when someone loads 
the model from MLFlow I DO NOT want them to be able to adjust the system message. The system message needs to be locked 
in and attached to the model at all times. 
```
---

     
 
all -  [ Dataframe/csv agent not supported for claude 3 api. ](https://www.reddit.com/r/LangChain/comments/1bqoy0v/dataframecsv_agent_not_supported_for_claude_3_api/) , 2024-03-30-0909
```
Title is self explanatory. I want to answer from an excel/dataframe, ideally by formulating queries. The langchain imple
mentation of csv/excel agents seem to be limited to openai.
```
---

     
 
all -  [ Any limitations with LlamaIndex that forced direct usage of LangChain? ](https://www.reddit.com/r/LocalLLaMA/comments/1bqocx8/any_limitations_with_llamaindex_that_forced/) , 2024-03-30-0909
```
FWIW, this isn't intended to be the standard 'LangChain vs LamaIndex' question.

Originally used LangChain, switched to 
LlamaIndex and have stuck with it sense then. So far, I haven't encountered any limitations with using LlamaIndex solely
. I have ready access to the relevant semantic search capabilities and I can use a ReActAgent to dynamically choose tool
s, with the LlamaIndex's equivalent to LCEL in the QueryPipeline DAG.

Despite that though, LlamaIndex is generally view
ed as something exclusive to RAG with limited agent support, yet I don't see why that is necessarily the case.

**Any us
ers of LlamaIndex that have been forced to use LangChain due to some limitation/inadequacy with the former?**
```
---

     
 
all -  [ Any limitations with LlamaIndex that forced direct usage of LangChain? ](https://www.reddit.com/r/LangChain/comments/1bqo89p/any_limitations_with_llamaindex_that_forced/) , 2024-03-30-0909
```
FWIW, this isn't intended to be the standard 'LangChain vs LamaIndex' question.

Originally used LangChain, switched to 
LlamaIndex and have stuck with it sense then. So far, I haven't encountered any limitations with using LlamaIndex solely
.  I have ready access to the relevant semantic search capabilities and I can use a ReActAgent to dynamically choose too
ls, with the LlamaIndex's equivalent to LCEL in the QueryPipeline DAG.

Despite that though, LlamaIndex is generally vie
wed as something exclusive to RAG with limited agent support, yet I don't see why that is necessarily the case.

**Any u
sers of LlamaIndex that have been forced to use LangChain due to some limitation/inadequacy with the former?**
```
---

     
 
all -  [ Trying to connect Jira tools with Langchain agent. Getting TypeError for some of the tools. ](https://www.reddit.com/r/LangChain/comments/1bqo1rh/trying_to_connect_jira_tools_with_langchain_agent/) , 2024-03-30-0909
```
I am trying to create a Langchain agent that can create Jira issues using tools. Below is the code:

import os  
from la
ngchain.agents import create\_react\_agent,AgentExecutor, create\_structured\_chat\_agent, initialize\_agent, create\_js
on\_chat\_agent  
from langchain\_community.agent\_toolkits.jira.toolkit import JiraToolkit  
from langchain\_community.
utilities.jira import JiraAPIWrapper  
from langchain\_google\_genai import ChatGoogleGenerativeAI  
from langchain\_ope
nai import ChatOpenAI  
from langchain import hub

llm=ChatOpenAI(temperature=0)  
jira=JiraAPIWrapper()  
toolkit=JiraT
oolkit.from\_jira\_api\_wrapper(jira)  
tools=toolkit.get\_tools()

prompt = hub.pull('hwchase17/structured-chat-agent')
  
agent = create\_structured\_chat\_agent(  
 tools=toolkit.get\_tools(),  
 llm=llm,  
 prompt=prompt,  
)

agent\_exe
cutor=AgentExecutor(agent=agent, tools=tools, verbose=True, handle\_parsing\_errors=True, return\_intermediate\_steps=Tr
ue)

response=agent\_executor.invoke({'input':'make a new issue in project DEMO to remind me to make Agent with File Sys
tem'})  
print(response)

I am getting the following error when I run the above code:

**> Entering new AgentExecutor ch
ain...** ***Action: \`\`\` {   'action': 'Create Issue',   'action\_input': {     'fields': {       'project': {        
 'key': 'DEMO'       },       'summary': 'Create Agent with File System',       'description': 'This is a reminder to cr
eate an Agent with File System.',       'issuetype': {         'name': 'Task'       }     }   } } \`\`\`***

TypeError: 
JiraAction.\_run() got an unexpected keyword argument 'fields'

For context, I have been following the official langchai
n documentation ([https://python.langchain.com/docs/integrations/toolkits/jira](https://python.langchain.com/docs/integr
ations/toolkits/jira)) and I am not able to replicate their outputs. I have tried with various Agent types but its still
 showing errors.  From as far as I could understand, I guess there is something wrong with the inputs being sent to the 
tool. So, does anybody know what may be the problem or whats happening? Thanks in advance!
```
---

     
 
all -  [ Self query on structural html metadata ](https://www.reddit.com/r/LangChain/comments/1bqn6yc/self_query_on_structural_html_metadata/) , 2024-03-30-0909
```
Hello everyone, I'm planning to create an LLM app for querying our product documentation, which is currently hosted on a
 Confluence web space.

To begin, I developed a Scrapy spider to retrieve HTML content from Confluence and stored the se
gments into a Chroma vector database using an HtmlHeaderSplitter. I chose this method to effectively segment different t
opics and subtopics. Each segment is associated with metadata such as h1, h2, and h3, representing titles of topics and 
subtopics (e.g., h1: 'Manage Products,' h2: 'Filter Products').

Initially, I attempted a simple similarity search on th
e content with unsatisfactory results. While I acknowledge the potential of experimenting with different embedding funct
ions and vector databases, my current objective is to optimize input to the vector database using self-query retrieval.


The challenge lies in mapping user queries to structural metadata such as h1, h2, and h3, which primarily indicate hier
archical organization.

I think renaming the metadata to more functional terms like 'operation' or 'function,' would hel
p to map user queries accordingly. For instance, a user query could be structured as 'how to {function}...' or a similar
 format.

As a newcomer to AI development, I would greatly appreciate any guidance or assistance.

```
---

     
 
all -  [ Improving My RAG Application for specific language  ](https://www.reddit.com/r/LangChain/comments/1bqn1sj/improving_my_rag_application_for_specific_language/) , 2024-03-30-0909
```

Hey everyone, I'm working on improving my RAG (Retrieval-Augmented Generation) application with a focus on processing C
zech language documents. My current setup involves using dense retrieval (specifically a combination of parent retriever
 that retrieves n chunks before and m chunks after the retrieved chunk, with n=1 and m=2, alongside with sparse retrieve
r BM25. 

I've been experimenting with multi-vector retrievers like ColBERT, but not with much success. I was wondering 
if anyone tried to fine-tune it specifically for any foreign language. I was thinking about to fine-tune it like in this
 example: https://github.com/bclavie/RAGatouille/blob/main/examples/03-finetuning_without_annotations_with_instructor_an
d_RAGatouille.ipynb

Similarly, my efforts with ReRanking  (using tools like Cohere, BGE-M3, and even GPT-3.5/GPT-4 as r
erankers) have so far resulted in worse or same outcomes than no reranking. 

Do you think fine-tuning the ColBERT and r
eranker models for specific language could significantly improve performance, or might it not be worth the effort? Has a
nyone tackled similar challenges, especially with language-specific tuning for tools like ColBERT or rerankers? Or any o
ther insights on how to enhance the accuracy of numerical comparisons or overall pipeline efficiency would be greatly ap
preciated.

Thank you!
```
---

     
 
all -  [ Virtual AI tech team using CrewAI ](https://www.reddit.com/r/LangChain/comments/1bqmtj0/virtual_ai_tech_team_using_crewai/) , 2024-03-30-0909
```
Hey everyone, checkout this tutorial on how to create a AI technical team (coder, product manager, tech lead, etc) and t
han see how they solve a give task using CrewAI in this demonstration : https://youtu.be/QPUUclaNI5o?si=HQZMbn-KOInQ02o1

```
---

     
 
all -  [ LangChain with LlamCpp ](https://www.reddit.com/r/LocalLLaMA/comments/1bqjt3k/langchain_with_llamcpp/) , 2024-03-30-0909
```
Hello, devs! I want to use LlamaCpp with LangChain and local embeddings to make it possible to iterate over my text. I h
eard that LangChain is like chunky stuff that can be used to iterate over large PDF books, even if it’s bigger than the 
model context size

I have tried this code:
```
from langchain.llms import LlamaCpp
from langchain import PromptTemplate
, LLMChain
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import (
  
  StreamingStdOutCallbackHandler,
)

model_path = 'lib/models/yuna/yuna-ai-v2-q6_k.gguf'

# Updated template to include 
Memory, Character, and Question sections
template = '''
### Memory:
{memory}

### System:
You're a cute girl named Yuna.


### Question:
{question}

### Answer:
'''

prompt = PromptTemplate(template=template, input_variables=['memory', 'ques
tion'])

# Callbacks support token-wise streaming
callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])


n_gpu_layers = 40  # Change this value based on your model and your GPU VRAM pool.
n_batch = 512  # Should be between 
1 and n_ctx, consider the amount of VRAM in your GPU.

llm = LlamaCpp(
    model_path=model_path,
    n_gpu_layers=n_gpu
_layers,
    n_batch=n_batch,
    callback_manager=callback_manager,
    verbose=True,
    # temperature=1
)

llm_chain 
= LLMChain(prompt=prompt, llm=llm)

memory_content = ''
# load the text.txt file
with open('text.txt', 'r') as file:
   
 memory_content = file.read()

# User question
question = 'The question is, what is the name of the protagonist of the s
tory? So, Please give me three bullet points: 1. Who are you? 2. What was the question? 3. What is the answer?'

# Run t
he model with the updated prompt
print(llm_chain.run({'memory': memory_content, 'question': question}))
```

But unfortu
nately, I got an error:
```
ValueError: Requested tokens (20333) exceed the context window of 512
ggml_metal_free: deall
ocating
```

Do you have any ideas on how to fix it to make it work as I described and fix the issue?
```
---

     
 
all -  [ Getting started with running LLMs ](https://www.reddit.com/r/LocalLLaMA/comments/1bqi6wo/getting_started_with_running_llms/) , 2024-03-30-0909
```
I am pretty new to AI space. I have little bit of experience implementing small models for CV use cases and I have used 
langchain and llamaindex for toy cases . How do I get started with LLM? Running them locally and fine uming them?

Can y
ou share some resource that are canonical?
```
---

     
 
all -  [ Azure AI search vs Chroma Db  ](https://www.reddit.com/r/LangChain/comments/1bqa628/azure_ai_search_vs_chroma_db/) , 2024-03-30-0909
```
Hi all , I was trying to evaluate and compare the performance of Azure AI search index vs Chroma Db in memory index . I 
have heard that Chroma Db is good for high speed retrieval but relevancy of retrieved docs are not that good . 

I was t
hinking that Azure AI search should easily outperform chroma DB  , So I configured both Chroma DB and Azure AI search In
dex with same configuration ( HNSW with Cosin similarity ) 
. I used same embedding model  text-embedding-3-small  for e
mbedding the test document ( 300 character small chunks)
.
Now I was a bit confused to see that , while testing with som
e queries both Vector Dbs( Indexes)are returning  the  same results . Even with k=4 nearest items , both are  returning 
same 4 doc chunks ( relevancy scores are different though)
  I am now concerned that somehow I have messed up something,
 What do you guys think?? Am I supposed to see the same results with same config or I am doing something wrong?

Can you
 guys suggest me some good dataset for benchmarking the retrieval systems.
Thanks in advance 😃


```
---

     
 
all -  [ Can LangChain still be used for free?! ](https://www.reddit.com/r/LangChain/comments/1bq9knx/can_langchain_still_be_used_for_free/) , 2024-03-30-0909
```
With the recent announcement of 'traces' being charged for, does anyone know if the rest of the framework is still free 
to use?!
```
---

     
 
all -  [ How can i stream output for my chain ? ](https://www.reddit.com/r/LangChain/comments/1bq881o/how_can_i_stream_output_for_my_chain/) , 2024-03-30-0909
```
The typical streaming method is not working for the below chain

chain\_main = RunnableParallel({  
'query': RunnablePas
sthrough(),  
'context': retrieval\_chain,  
}) | generation\_prompt | model | OpenAIFunctionsAgentOutputParser() | rout
e

But streaming method works for simple chain without function calling like the one below

chain = RunnableParallel({  

'query': RunnablePassthrough(),  
'context': retrieval\_chain,  
}) | generation\_prompt |model | parser

Can someone h
elp me on this. Thanks in advance for the help
```
---

     
 
all -  [ Webvoyageur GraphChain Agent ](https://www.reddit.com/r/crewai/comments/1bq7o9c/webvoyageur_graphchain_agent/) , 2024-03-30-0909
```
Hey guys did you think we ca implement that into Crew ?

This agent navigating autonomously on the web using real browse
r

[https://www.youtube.com/watch?v=ylrew7qb8sQ&ab\_channel=LangChain](https://www.youtube.com/watch?v=ylrew7qb8sQ&ab_ch
annel=LangChain)

  
[https://github.com/langchain-ai/langgraph/blob/main/examples/web-navigation/web\_voyager.ipynb](ht
tps://github.com/langchain-ai/langgraph/blob/main/examples/web-navigation/web_voyager.ipynb)


```
---

     
 
all -  [ Learning resources  ](https://www.reddit.com/r/LangChain/comments/1bq73n0/learning_resources/) , 2024-03-30-0909
```
I know that this question about LangChain is frequent but I just wanted to ask if there's any comprehensive or practical
 course for learning langchain? Because the documentations on python are SO vague and do not really teach anything. I've
 checked YouTube courses but most of them are old and langchain has changed ever since. Plus the YouTube courses all tea
ch the basics, they don't go through various modules.
```
---

     
 
all -  [ Do you use the 'system' role for adding prompts or just append it to the 'user' role? ](https://www.reddit.com/r/LangChain/comments/1bq5g0u/do_you_use_the_system_role_for_adding_prompts_or/) , 2024-03-30-0909
```
I am just trying to understand if any of you use the 'system' role for adding prompts to programmatic invocations. I kno
w this is the support by the books way to do it. But I have also attached the prompt directly to the 'user' role with si
milar accuracy. Wondering what the best practice is.
```
---

     
 
all -  [ ROAST MY RESUME 2nd year cs student  ](https://i.redd.it/j53vhmkg44rc1.jpeg) , 2024-03-30-0909
```

```
---

     
 
all -  [ How to implement Claude based Agents ? ](https://www.reddit.com/r/LangChain/comments/1bq1rgj/how_to_implement_claude_based_agents/) , 2024-03-30-0909
```
I have an application that is currently based on 3 agents using LangChain and GPT4-turbo.

I'd like to test Claude 3 in 
this context. However all my agents are created using the function `create_openai_tools_agent()`.

Reading the documenta
tion, it seems that the recommended Agent for Claude is the [XML Agent](https://python.langchain.com/docs/modules/agents
/agent_types/xml_agent). However this documentation is referring to Claude 2 instead of Claude 3. It's also assuming tha
t the model is a LLM and not a Chatbot. That seems weird. Especially given that Anthropic documentation is clear about u
sing a Chatlike API, with [a system prompt and a list of users/assistant messages](https://docs.anthropic.com/claude/ref
erence/messages_post). Instead the XML Agent seems to only be able to [understand chathistory as a single string](https:
//python.langchain.com/docs/modules/agents/agent_types/xml_agent#using-with-chat-history). 

Given that LLM in general, 
and Claude in particular are quite sensitive to prompting format, I'm not really happy with the idea of having a chat hi
story sent as a single string instead of the standard format provided by the API. Thus I'm hesitating about using the XM
L agent.

So I'm curious if any of you has any experience using the XML Agent with a chat history ? Or did you use anoth
er kind of agent ?

Thanks in advance !
```
---

     
 
all -  [ ConversationalRetrievalChain and langserve ](https://www.reddit.com/r/LangChain/comments/1bq0t3b/conversationalretrievalchain_and_langserve/) , 2024-03-30-0909
```
Hi, I have an error with langchain and langserve that I can't solve. 
This is my code:

from langchain_core.output_parse
rs import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import Run
nableMap, RunnablePassthrough
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from operator import itemgetter

from langchain_community.vectorstores import Chroma
from langchain_core.messages import AIMessage, HumanMessage, get_buf
fer_string
from langchain_core.prompts import format_document
from langchain_core.runnables import RunnableParallel
from
 langchain.retrievers.multi_vector import MultiVectorRetriever
from langchain.storage import LocalFileStore
from langcha
in.prompts.prompt import PromptTemplate
from langchain.docstore.document import Document
from langserve import add_route
s
from fastapi import FastAPI

vectorstore = Chroma(collection_name='summaries', 
                     embedding_functio
n=OpenAIEmbeddings(), 
                     persist_directory='path/to/directory/')

store = LocalFileStore('path/to/dir
ectory')
id_key = 'doc_id'

retriever = MultiVectorRetriever(
    vectorstore=vectorstore,
    docstore=store,
    id_ke
y=id_key,
    search_kwargs={'k': 3}
)

_template = '''Given the following conversation and a follow up question, rephra
se the follow up question to be a standalone question, in its original language.

Chat History:
{chat_history}
Follow Up
 Input: {question}
Standalone question:'''

CONDENSE_QUESTION_PROMPT = PromptTemplate.from_template(_template)

template
 = '''Answer the question based only on the following context:
{context}

Question: {question}
'''
ANSWER_PROMPT = ChatP
romptTemplate.from_template(template)

DEFAULT_DOCUMENT_PROMPT = PromptTemplate.from_template(template='{page_content}')


def _combine_documents(
    docs, document_prompt=DEFAULT_DOCUMENT_PROMPT, document_separator='\n\n'
):
    format_doc
 = [ ]
    for i in docs:
        single_doc = Document(page_content=i, metadata={'doc_name': 'doc_name'})
        forma
t_doc.append(single_doc)
    doc_strings = [format_document(doc, document_prompt) for doc in format_doc]
    return docu
ment_separator.join(doc_strings)


_inputs = RunnableParallel(
    standalone_question=RunnablePassthrough.assign(
     
   chat_history=lambda x: get_buffer_string(x['chat_history'])
    )
    | CONDENSE_QUESTION_PROMPT
    | ChatOpenAI()
 
   | StrOutputParser(),
)

_context = {
    'context': itemgetter('standalone_question') | retriever | _combine_document
s,
    'question': lambda x: x['standalone_question'],
}

llm = ChatOpenAI()

conversational_qa_chain = _inputs | _conte
xt | ANSWER_PROMPT | llm

app = FastAPI(
    title='LangChain Server',
    version='1.0',
    description='Spin up a sim
ple api server using Langchain's Runnable interfaces')

add_routes(app, conversational_qa_chain)

if __name__ == '__main
__':
    import uvicorn

    uvicorn.run(app, host='localhost', port=8000)

When I try to use playground or I try to use
 request like this:  

import requests

inputs = {'input': {'question': 'what do you know about harrison', 'chat_history
': []}}
response = requests.post('http://localhost:8000/invoke', json=inputs)

response.json()

I have this error: 

cha
t_history=lambda x: get_buffer_string(x['chat_history'])
KeyError: 'chat_history'

Do you know a way to solve this error
? 
```
---

     
 
all -  [ Getting invalid literal for int() with base 10 while using from_uri method in the SQLDatabase ](https://www.reddit.com/r/LangChain/comments/1bq0r2j/getting_invalid_literal_for_int_with_base_10/) , 2024-03-30-0909
```
While trying to connect to presto db I am getting the invalid literal for int() with base 10 

Though I have tried all o
ptions of converting the port number to int using below

int(port\_number)

int(float(port\_number)

I am still getting 
the error, also needs to understand more on the from\_uri method, will that only take conn\_str \[string \] as parameter
?  
Outside the langchain I could able to connect to presto DB with dbapi.  
please help
```
---

     
 
all -  [ Tuning RAG retriever to reduce LLM token cost (4x in benchmarks) ](https://www.reddit.com/r/LangChain/comments/1bpz9dw/tuning_rag_retriever_to_reduce_llm_token_cost_4x/) , 2024-03-30-0909
```
Hey, we've just published a tutorial with an adaptive retrieval technique to cut down your token use in top-k retrieval 
RAG:

https://pathway.com/developers/showcases/adaptive-rag.

Simple but sure, if you want to DIY, it's about 50 lines o
f code (your mileage will vary depending on the Vector Database you are using). 
Works with GPT4, works with many local 
LLM's, works with old GPT 3.5 Turbo, does not work with the latest GPT 3.5 as OpenAI makes it hallucinate over-confident
ly in a recent upgrade (interesting, right?). Enjoy!
```
---

     
 
all -  [ AI Chain Builder for Code Manipulation ](https://www.reddit.com/r/LangChain/comments/1bpyx3o/ai_chain_builder_for_code_manipulation/) , 2024-03-30-0909
```
Hello everyone. I'm Tom, CTO and Co-Founder of [Autonoma AI](https://getautonoma.com). I'm coming with [something we coo
ked up this weekend](https://gitgud.autonoma.app/) and wanted your feedback on. [Here's a video](https://www.youtube.com
/watch?v=6kfr1lqw2gg) if you like that format better.

It's **free**, **no account needed**, **no credit card needed**. 
We just want you guys to tell us what you think.

&#x200B;

It's very alpha, so I apologize in advance for the bugs and 
issues that might exist.

Feel free to ask about the architecture or design decisions, or whatever you want to discuss a
bout.

Thank you all in advance for this as well.

&#x200B;

If you like the product, I'd like to ask you to upvote the 
[producthunt post](https://www.producthunt.com/posts/gitgud), it'd really help us!
```
---

     
 
all -  [ Error when trying to get answer using qa_chain ](https://www.reddit.com/r/LangChain/comments/1bpxeq5/error_when_trying_to_get_answer_using_qa_chain/) , 2024-03-30-0909
```
Hi everyone, I'm following this [tutorial](https://medium.com/@Siddharth.jh/conversational-chat-bot-using-open-source-ll
m-model-dolly-2-0-with-added-memory-acfacc13a69e) and I'm at the step where I am testing chatting with the AI chatbot. I
 have created the qa\_chain and I am using it similar to how it is in the tutorial but I am getting the following error 
after I input my question and it tries generating the answer:

`generated_sequence = self.model.generate(`

`^^^^^^^^^^^
^^^^^^^^^`

`TypeError: transformers.generation.utils.GenerationMixin.generate() got multiple values for keyword argumen
t 'pad_token_id'`

I am wondering what this issue could be coming from? I checked the collab provided in the tutorial an
d I can't seem to find any significant differences between my code and theirs.

&#x200B;

Thanks
```
---

     
 
all -  [ Provide feedback on my Resume - 3 YOE ](https://www.reddit.com/r/resumes/comments/1bpvhe4/provide_feedback_on_my_resume_3_yoe/) , 2024-03-30-0909
```
* Resume not getting shortlisted (Not getting any interviews)
* I'm looking for a Backend Developer / GenAI / AI/ML Engi
neer role  


https://preview.redd.it/n62lsibds2rc1.png?width=1404&format=png&auto=webp&s=cacc6319629b5343a0cc7a2f1db432
3f05cf473f
```
---

     
 
all -  [ Need help with my SQL LLM  ](https://www.reddit.com/r/LangChain/comments/1bptmed/need_help_with_my_sql_llm/) , 2024-03-30-0909
```
Hi guys , I have a SQL LLM already implemented using. OpenAI API. I have tried ollama models but it’s taking a lot of ti
me to process. So now I need to use llama.cpp models .. I don’t know how to implement it. Please ping me .. you can take
 a look at the code. 
Thanks a lot 
```
---

     
 
all -  [ Needed help to create a chatbot  ](https://www.reddit.com/r/LangChain/comments/1bpt0rl/needed_help_to_create_a_chatbot/) , 2024-03-30-0909
```
Hi everyone, despite having some experimentation using langchain, I still can't figure out how to create a best chatbot,
 in the sense of its way in communication, relavancy and good RAG. I request everyone to guide me so that I could go in 
right direction and build one for my experience. This is a request. (PS: The RAG process should be capable of taking doc
ument chunks from PDF, video, URL'S, and local files too. Also guide me the type of chunking to use for various types of
 data)
```
---

     
 
all -  [ Where does faiss store my data? ](https://www.reddit.com/r/LangChain/comments/1bpsvy8/where_does_faiss_store_my_data/) , 2024-03-30-0909
```
I'm using FAISS vector database for my work. 
Just curious where the database is stored. Is it stored somewhere locally 
or what? 

Is it safe to pass personal information to FAISS? 

I'm performing chunking and later passing this chunks int
o FAISS

Data= faiss.from_texts(texts, embeddings)
```
---

     
 
all -  [ Custom evaluation of LLM responses ](https://www.reddit.com/r/LangChain/comments/1bprzs6/custom_evaluation_of_llm_responses/) , 2024-03-30-0909
```
Hey Community, I want to run evaluation over my model responses such that it is done independently of the rag pipeline. 
Essentially, I have a CSV generated as an output of my RAG pipeline which contains, question, correct answer and model r
esponse. Now, I want to evaluate if the model response matches the correct answer independently of the RAG pipeline. I w
as looking into some of the langchain metrics like Accuracy, correctness , cot_qa but have not been able to actually get
 any of them working, cause all the chains require a model that generates answers for the question instead of just evalu
ating correct answer with model answer.  I have tried prompt control, QA eval chain, or literally building a custom chai
n with the sole purpose of evaluation but none of that has worked. Has anyone tried this before or has any idea how it c
an be achieved?
```
---

     
 
all -  [ HuixiangDou: Overcoming Group Chat Scenarios with LLM-based Assistance.[Discussion] ](https://www.reddit.com/r/LocalLLaMA/comments/1bprxm5/huixiangdou_overcoming_group_chat_scenarios_with/) , 2024-03-30-0909
```
 'HuixiangDou' is a domain-specific group assistant, designed to answer user questions. It has been running for half a y
ear and helped thousands of  OpenMMLab users.

https://preview.redd.it/pkzohku8u1rc1.png?width=778&format=png&auto=webp&
s=1c11f8b83078116babbd43ad31018d374505a539

Differs from langchain or llamaIndex, HuixiangDou is for group chat scenario
s.

1. We designed a rejection pipeline to eliminate hallucination caused by gossip.
2. It is highly practical, for exam
ple, it can answer questions about table content in a PDF file, not just body text.

Now Huixiangdou's web portal is  li
ve.Here, you can create your own knowledge base and integrate it into Lark and WeChat groups without any coding.

 Learn
 more at:

 [http://github.com/internlm/huixiangdou](http://github.com/internlm/huixiangdou)

[http://arxiv.org/abs/2401
.08772](http://arxiv.org/abs/2401.08772)

&#x200B;

https://reddit.com/link/1bprxm5/video/wlszr0lgu1rc1/player
```
---

     
 
all -  [ RAG system + Math Agent ](https://www.reddit.com/r/LangChain/comments/1bprh9c/rag_system_math_agent/) , 2024-03-30-0909
```
Hi everyone, I am currently building a financial RAG, the RAG alone, it performs great till it starts to derive math for
mulas to run, then the LLM is unable to evaluate the math expression accurately. What are the solutions to giving the LL
M, the ability to Compute Math?. I have seen the LLMMathChain agent, but how do I combine it with the retrieval chain?
```
---

     
 
all -  [ Hosting AI Agents? ](https://www.reddit.com/r/LangChain/comments/1bpr6nb/hosting_ai_agents/) , 2024-03-30-0909
```
I’m finishing up a system that can take transcripts of users doing their processes or Process Definition Documents, and 
automatically generate Langchain AI Agents chains and tools. I’ve got a couple agents ready to push to prod, but having 
trouble finding a place to host them. Where do people here host their agents?
```
---

     
 
all -  [ Hosting AI Agents? ](https://www.reddit.com/r/AutoGPT/comments/1bpr5jy/hosting_ai_agents/) , 2024-03-30-0909
```
I’m finishing up a system that can take transcripts of users doing their processes or Process Definition Documents, and 
automatically generate AI Agents chains and tools (currently using Langchain). I’ve got a couple agents ready to push to
 prod, but having trouble finding a place to host them. Where do people here host their agents?
```
---

     
 
all -  [ FAISS.load_local is so slow ](https://www.reddit.com/r/LangChain/comments/1bpqoiz/faissload_local_is_so_slow/) , 2024-03-30-0909
```
&#x200B;

# Summary

I am trying to run FAISS.load\_local after a .save\_local on a 60k pdf pickle file in order to not 
repeat the embedding procedure everytime for a RAG. But it is really slow and I would like to launch all the RAG workflo
w fastly :( Could it be due to the huge amount of data?

OS: Ubuntu 18.04.6 LTS (Bionic Beaver)

Faiss version: faiss-cp
u==1.7.4

Installed from: pip install in conda env

Running on: Cluster with GPU Tesla V100-SXM2-32GB

Interface: Python


# Reproduction instructions

First, I have launched these lines on a py script (ingest.py):

vectorstore = FAISS.from\
_documents(documents=chunks, embedding=embeddings,)  
vectorstore.save\_local('./faiss\_db')

And then on a different py
 script (rag.py):

vectorstore = FAISS.load\_local('./faiss\_db', embeddings, allow\_dangerous\_deserialization=True)  

retriever = vectorstore.as\_retriever()

The log file gives me back only this:

'All keys matched successfully'

&#x200B
;

Can you help me, please?  
Thank you in advance!
```
---

     
 
all -  [ Autogen using Local LLMs ](https://www.reddit.com/r/LangChain/comments/1bpof9x/autogen_using_local_llms/) , 2024-03-30-0909
```
Hey everyone, this tutorial explains how to use Multi-Agent framework Autogen by Microsoft using Local LLMs (and not any
 API) using Ollama & LiteLLM: https://youtu.be/AdGuzjGWZms?si=FHhwzaS0RoAiDubk
```
---

     
 
all -  [ Use existing LLM framework (vs) Custom build to tackle version mismatch issues ? ](https://www.reddit.com/r/LLMDevs/comments/1bpmky4/use_existing_llm_framework_vs_custom_build_to/) , 2024-03-30-0909
```
If I were to build a Devin kind of product which will be used in production and could possibly have a payment option in 
future. Which approach will be right to go with ?

I have used LangChain and EmbedChain frameworks before.

(or) I was w
ondering if it could be a good idea to custom build a mini framework with all prompts strategies and get going.

The mai
n challenge is because of frequent version issues especially with LangChain and OpenAI SDK, some of the example code whi
ch we copy from internet is obsolete  / deprecated and it wouldnt even run.

From broader spectrum of things, which appr
oach would be better ?
```
---

     
 
all -  [ ‘Open sourcing’ our complex RAG system ](https://www.reddit.com/r/LocalLLaMA/comments/1bpmfaa/open_sourcing_our_complex_rag_system/) , 2024-03-30-0909
```


I’ve made our backend public on GitHub for anyone who wants to check it out/borrow it. (I’ll add a readme later)

[mpl
x_rag](https://github.com/multiplexerai/mplx_rag)

Open source is a bit of a stretch as it’s pretty much just boiler pla
te at this stage. Eventually I’d like to turn it into libraries, just as another option for langchain and llamaindex.
Wh
y have I called it ‘complex’? Because compared to your basic RAG where it just answers a simple question, in my mind it 
is.

I’d also like to say I’m a mechanic and I don’t really know how to write code (although I’ve learnt a lot and now o
ptimistically think maybe I’m at an intern level). I’ve pretty much leveraged GPT-4 to do the heavy lifting but the idea
s are my own. So with that I’d love if some of the professionals could actually give it a code review or even contribute
 would be amazing.

I know there are a few things that I need to fix, like making all the functions stand alone files (w
ill come with making libraries). In my production set up I’m actually implementing Oauth and have tidied it up by doing 
exactly that.

I also use environments to store keys in production.

Also for the undoubted bUT iT uSEs OpENai. OpenAI A
PI libraries are pretty standard even if you’re not actually using openAI. You can insert mistral or what ever you want.


also the validate function was something I was playing around with. I was actually thinking you could use it (as a sta
nd alone func) to update the answers for Q&A’s that you’ve logged from users if you update your data.

Happy Easter!
```
---

     
 
all -  [ Seeking advice on LLMs and RAGs ](https://www.reddit.com/r/learnmachinelearning/comments/1bpm5c2/seeking_advice_on_llms_and_rags/) , 2024-03-30-0909
```
Hey guys so I’m working on a personal project and I was wondering if anyone had any advice. 

I’m currently using embedd
ings from HF to read a pdf and using chromadb and langchain to start a conversation chain to basically “chat with my doc
ument” 

The problem is that it’s not as accurate as I want it to be and it seems to “hallucinate” every now and then! L
ooking for some advice on it ie maybe creating my own sentence embedding or how to even do so and can give more info if 
needed (not sure how posting here works so just giving it a shot)  

Thanks!!~
```
---

     
 
all -  [ Creating a reminder task in langchain ](https://www.reddit.com/r/LangChain/comments/1bpiwmt/creating_a_reminder_task_in_langchain/) , 2024-03-30-0909
```
Hi everyone, I'm trying to create a studying tutor with LLMs and langchain. What I'm looking for is that the app reminds
 the student once in a while during the conversation if he/she has done his/her homework, and based on the answer remind
 him/her later or don't remind her again. I'm looking for a clue on how to achieve such a thing.  
Thanks in advance

&#
x200B;

&#x200B;
```
---

     
 
all -  [ Free Courses from NVIDIA ](https://www.reddit.com/r/FreeITCourses/comments/1bpe0sm/free_courses_from_nvidia/) , 2024-03-30-0909
```
Hey everyone,

Exciting news! NVIDIA just launched free Al courses, no payment needed. If you're aiming to upskill by 20
24, here are eight essential courses you shouldn't miss

 1. Developing a Mind in Ten Minutes - Understand neural networ
ks and how they learn from data. - Link: [https://lnkd.in/e4FGDzuv)

 2. The Meaning of Generative Al -⁃ Dive into how g
enerative Al works, its applications, and challenges - Link: [https://lnkd.in/eKPmgRHj)

 3. Artificial Intelligence ins
ide the Data Centre ⁃ Explore Al use cases, machine learning frameworks, GPU architecture, and more. - Link: [https://ln
kd.in/e4-YhiW8)

 4. Use Retrieval Augmented Generation to enhance your LLM - Learn about RAG retrieval procedure and NV
IDIA AI Foundations. - Link: [https://lnkd.in/ehndH8PC)

 5. Proficiency with Recommender Systems . Master e-commerce re
commendation systems techniques - Link: [https://lnkd.in/euKVZ_Tb)

 6. Streamline Data Science Processes with No Code M
odifications ⁃ Discover integrating GPU and CPU benefits into your operations. - Link: [https://lnkd.in/eN7jeG3t)

 7. C
reating RAG Agents Utilising LLMs ⁃ Explore scalable LLM deployment strategies and contemporary LangChain models. - Link
: [https://lnkd.in/eycWGKzp)

 8. Introduction to Networking ⁃ Gain insights into networks, Ethernet, TCP/IP- protocol, 
and OSI model. - Link: [https://lnkd.in/eeYNyWnX)

 Feel free to leave your thoughts or questions below each course link
!
```
---

     
 
all -  [ Help with LLM to design circuits ](https://www.reddit.com/r/LangChain/comments/1bp914d/help_with_llm_to_design_circuits/) , 2024-03-30-0909
```
I have a project where I need to create an assistant that will help my professor which teaches digital circuits at the u
niversity. The purpose of the project is that if a student was studying for an exam at 3 AM but needs to understand a qu
estion or circuit diagram, they can ask the AI assistant which is basically as good as the professor himself. Ill need t
o have separate sessions ans save the conversation in a database.

The professor sent me the data which consist of Power
Point presentations which consists of images and text and those are what I want my LLM to focus on. The LLM should be ab
le to draw a circuit diagram to explain what its showing. 

 I tried gpt vision but its not showing proper results and t
he software we use for the circuit diagrams is simulink. I know how to save and store the data in a database and load ea
ch user separately and I know how to do rag but my main issue lies in how can I allow my LLM use simulink to design circ
uits? Do I need to use agemt? If yes, how do I connect it and allow it to design from simulink? 
```
---

     
 
all -  [ LangGraph with Claude? ](https://www.reddit.com/r/LangChain/comments/1bp7thq/langgraph_with_claude/) , 2024-03-30-0909
```
Hi, like the title says I would like to know whether LangGraph works well with all the Claude models? I never tested the
 function calling abilities of Claude and have no idea if they work well inside the LangGraph framework. Any type of ill
umination is greatly appreciated.

Thanks in advance.
```
---

     
 
all -  [ AWS OpenSearch Vector not returning anything on similarity search ](https://www.reddit.com/r/LangChain/comments/1bp6frg/aws_opensearch_vector_not_returning_anything_on/) , 2024-03-30-0909
```
I have an aws opensearch vector store. I can connect to it with the opensearch-py library and I can create an index and 
upload documents to the index. I am using langchain 0.1.13 and langchain-community 0.0.29

here's my code:

```python
fr
om langchain_community.document_loaders import TextLoader  
from langchain_text_splitters import CharacterTextSplitter  

from langchain_openai import OpenAIEmbeddings  
from langchain_community.vectorstores import OpenSearchVectorSearch

do
cuments = TextLoader('./test.txt').load()
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
docs =
 text_splitter.split_documents(documents)
  
embeddings = OpenAIEmbeddings()  
 
vector_store = OpenSearchVectorSearch(

    opensearch_url=f'https://{url}:{port}',
    index_name='test',
    embedding_function=embeddings,
    http_auth=auth
,
    use_ssl = True,
    verify_certs = False
)

vector_store.add_documents(documents=docs)
```

but when I run the bel
ow I get no documents back consistently even when the prompt is identical to the content in the index I get nothing back
:

```python
print(vector_store.similarity_search('what is my name on thursday?', k=1))
```

I've validated that the ind
ex names are all correct and the vector fields are all consistently named. I can query the index and see the documents u
ploading correctly here:

```python
from opensearchpy import OpenSearch

client = OpenSearch(
    hosts=[{'host': url, '
port': port}],
    http_auth=auth,
    use_ssl=True,
    verify_certs=False
)

response = client.search(
    index='test
',
    body={'query': {'match_all': {}}},
    size=1000
)

documents = [doc['_source'] for doc in response['hits']['hits
']]
print(documents)
```

Any thoughts on what the issue might be? Literally any help is appreciated.
```
---

     
 
all -  [ LangChain for a full framework - what options for more focused toolkits? ](https://www.reddit.com/r/LangChain/comments/1bp48si/langchain_for_a_full_framework_what_options_for/) , 2024-03-30-0909
```
LangChain does a great job as a full framework for LLM-based application development, but there are so many components s
ometimes you just want a toolkit that is better at a particular piece. I won't go down the rabbit-hole of 'frameworks vs
 toolkits' in general, but if you're looking for some of the alternatives to LangChain for pieces of the LLM-application
 development puzzle here's a write up: [https://www.mirascope.io/post/langchain-alternatives](https://www.mirascope.io/p
ost/langchain-alternatives)
```
---

     
 
all -  [ Question on querying pre stored vectors on weviate ](https://www.reddit.com/r/LangChain/comments/1bp33yk/question_on_querying_pre_stored_vectors_on_weviate/) , 2024-03-30-0909
```
I am relatively new to langchain. I need to load a pdf stored in GCS and I want chunk and embed the contents of the pdf 
and store it on weviate. I want to then retrive relevant vectors later and user a RetrivalQAChain. How do I do it? Any h
elp or code samples are appreciated! Thanks in advance. 
```
---

     
 
MachineLearning -  [ [D] : Scale PDF Q&A App to 10K Users with GPUs – <$250/Mo ](https://www.reddit.com/r/MachineLearning/comments/1b6jv56/d_scale_pdf_qa_app_to_10k_users_with_gpus_250mo/) , 2024-03-30-0909
```
Hello everyone,

Check out this step-by-step detailed tutorial on building and scaling a PDF Q&A Application using Pinec
one, Langchain and Inferless

&#x200B;

[Architecture](https://preview.redd.it/zfta52cbddmc1.png?width=1301&format=png&a
uto=webp&s=440399212d3feb03e861759a31602e2cde0dc7fb)

Alongside, the detailed quick deploy guide, it also includes cost 
analysis on how you can save upto 84% cost with an example of processing 3000 documents and nearly 10,000 queries every 
month, all while dramatically cutting your costs from $1800 ( AWS) to just $250 a month on Inferless.

Here is the tutor
ial - [https://cookbook.inferless.com/](https://cookbook.inferless.com/)

If you resonate, join the discussion on Hacker
news here - [https://news.ycombinator.com/item?id=39594588](https://news.ycombinator.com/item?id=39594588)
```
---

     
 
MachineLearning -  [ [D] What Is Your LLM Tech Stack in Production? ](https://www.reddit.com/r/MachineLearning/comments/1b4sdru/d_what_is_your_llm_tech_stack_in_production/) , 2024-03-30-0909
```
Curious what everybody is using to implement LLM powered apps for production usage and your experience with these toolin
gs and advice. 

This is what I am using for some RAG prototypes I have been building for users in finance and capital m
arkets.

**Pre-processing\ETL:**
Unstructured.io + Spark, Airflow

**Embedding model:**
Cohere Embed v3
Previously using
 OpenAI Ada but Cohere has significantly better retrieval recall and precision for my use case. Also exploring other ope
n weights embedding models

**Vector Database:**
Elasticsearch previously but now using Pinecone

**LLM:**
Gone through 
quite a few including hosted and self-hosted options. Went with gpt4 early during prototyping then switched to gpt3.5-tu
rbo for more manageable costs and eventually open weights models. 

Now using a fine-tuned Llama2 70B model self hosted 
with vLLM 

**LLM Framework:**
Started with Langchain initially but found it cumbersome to extend as the app became more
 complex. Tried implementing it in LlamaIndex at some point just to learn and found it just as bad. Went back to Langcha
in and now I am in the midst of replacing it with my own logic

What is everyone else using?

Edit: correct model Llama2
 70B
```
---

     
 
deeplearning -  [ Tengyu Ma on Voyage AI - Weaviate Podcast #91! ](https://www.reddit.com/r/deeplearning/comments/1bjft8i/tengyu_ma_on_voyage_ai_weaviate_podcast_91/) , 2024-03-30-0909
```
**Voyage AI** is the newest giant in the embedding, reranking, and search model game!

I am SUPER excited to publish our
 latest Weaviate podcast with Tengyu Ma, Co-Founder of Voyage AI and Assistant Professor at Stanford University!

We beg
an the podcast with a deep dive into everything embedding model training and contrastive learning theory. Tengyu deliver
ed a **masterclass** in everything from scaling laws to multi-vector representations, neural architectures, representati
on collapse, data augmentation, semantic similarity, and more! I am beyond impressed with Tengyu's extensive knowledge a
nd explanations of all these topics.

The next chapter dives into a case study Voyage AI did **fine-tuning an embedding 
model for the LangChain documentation.** This is an absolutely fascinating example of the role of continual fine-tuning 
with very new concepts (for example, very few people were talking about chaining together LLM calls 2 years ago), as wel
l as the data efficiency advances in fine-tuning.

We concluded by discussing ML systems challenges in serving an embedd
ings API. Particularly the challenge of detecting if a request is for batch or query inference and the optimizations tha
t go into either say \~100ms latency for a query embedding or maximizing throughput for batch embeddings.

I hope you fi
nd the podcast interesting, more than happy to discuss any of these topics with you or answer any questions about the co
ntent in the podcast! Thank you so much!

YouTube: [https://www.youtube.com/watch?v=xPdyivfheqI](https://www.youtube.com
/watch?v=xPdyivfheqI)

Spotify: [https://spotifyanchor-web.app.link/e/u6XPLYfF7Hb](https://spotifyanchor-web.app.link/e/
u6XPLYfF7Hb)
```
---

     
