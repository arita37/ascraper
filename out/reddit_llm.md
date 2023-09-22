 
all -  [ [Personal AI/ML Project] Chatbot which can answer your document ](https://www.reddit.com/r/ChatGPT/comments/16ovqyy/personal_aiml_project_chatbot_which_can_answer/) , 2023-09-22-0909
```
Hi Folks,

During my free time, I was doing personal project basically created a chatbot which can answer your question 
from document. I used Langchain(framework), ChromaDB(vector database), Streamlit(ui) and used both local llm(Llama2 base
d model) or OpenAI api for llm. You can use PDF, TXT, CSV, and DOCX files for question answering. Any contributions to t
his project will be highly welcome. Thanks!

Github link: [https://github.com/himanshu662000/InfoGPT](https://github.com
/himanshu662000/InfoGPT)
```
---

     
 
all -  [ [Personal AI/ML Project] Chatbot which can answer your document ](https://www.reddit.com/r/LangChain/comments/16ouikv/personal_aiml_project_chatbot_which_can_answer/) , 2023-09-22-0909
```
Hi Folks,

During my free time doing personal project basically created a chatbot which can answer your question from do
cument. I used Langchain(framework), ChromaDB(vector database), Streamlit(ui) and used both local llm(Llama2 based model
) or OpenAI api for llm. You can use PDF, TXT, CSV, and DOCX files for question answering. Any contributions to this pro
ject will be highly welcome. Thanks!

Github link: [https://github.com/himanshu662000/InfoGPT](https://github.com/himans
hu662000/InfoGPT)

&#x200B;

&#x200B;
```
---

     
 
all -  [ Real-time ChatGPT ](https://www.reddit.com/r/LangChain/comments/16orpax/realtime_chatgpt/) , 2023-09-22-0909
```
Do anyone of you guys have experience of Using the Search functionality in Agents. Actually, I'm trying to create an Con
versation model that will answer current scenario questions as well using ChainLit and Langchain. I'm just doing it for 
practice. What are your thoughts on this?
```
---

     
 
all -  [ Meet BondAI, an AI Agent that works better than AutoGPT and has a friendly API for building your own ](https://www.reddit.com/r/OpenSourceAI/comments/16oo2fe/meet_bondai_an_ai_agent_that_works_better_than/) , 2023-09-22-0909
```
📢 I'm excited to introduce **BondAI**, an AI Agent framework and CLI, with a lightweight yet robust API making integrati
on into your own applications straightforward and easy.

**Repository**: [https://github.com/krohling/bondai](https://gi
thub.com/krohling/bondai)

# ⚡️Examples

Here's an example of buying/selling Stocks with [Alpaca Markets](https://alpaca
.markets/). I strongly recommend using Paper Trading btw!

    from bondai import Agent 
    from bondai.tools.alpaca_ma
rkets import (
        CreateOrderTool, 
        GetAccountTool, 
        ListPositionsTool
    )
    
    task = (
    
    'I want you to sell off all of my existing positions.'
        Then I want you to buy 10 shares of NVIDIA with a lim
it price of $456.'
    )
    
    Agent(tools=[
       CreateOrderTool(),
       GetAccountTool(),
       ListPositionsT
ool()
     ]).run(task) 

&#x200B;

[Here's an example](https://github.com/krohling/bondai/tree/main/examples/online-res
earch) of BondAI doing online research and [here's a home automation example](https://github.com/krohling/bondai/tree/ma
in/examples/home-automation).

# 🔍 What is BondAI?

BondAI is a framework crafted for the smooth integration and customi
zation of Conversational AI Agents. Leveraging the power of OpenAI's [function calling support](https://openai.com/blog/
function-calling-and-other-api-updates), it sidesteps the hurdles often encountered in building a Conversational Agent, 
offering solutions such as:

* Integration with Azure OpenAI Services
* Memory management
* Error handling
* Integrated 
semantic search
* A rich array of pre-existing tools
* Straightforward API for crafting custom tools

Moreover, it offer
s a CLI interface that promises an impressive command line agent experience, available to anyone with an OpenAI API Key!


# 🏗️ Why build BondAI?

I am convinced that AI agents are going to be an important architecture for the future of AI. 
Despite their phenomenal problem-solving abilities, the existing tooling often fell short in performing simple tasks, an
d the frameworks appeared unnecessarily complicated. This spurred the birth of BondAI, aiming to address these shortcomi
ngs and offer a more optimized environment for agent implementations.

I am keen on hearing your feedback on BondAI's fu
nctionality and any suggestions for improvements!

# 🛠️ Installation & Usage

Getting started is super simple with the B
ondAI CLI

    pip install bondai
    export OPENAI_API_KEY=xxxxxx
    bondai # Start the CLI

The CLI tool offers a rea
dy-to-use agent experience packed with several default tools. You can also integrate it with various tools such as Googl
e Search, Alpaca Markets, and LangChain Tools to execute a myriad of tasks effectively. Detailed guides and examples for
 usage are available in the README.

# 🔧 APIs and Custom Tools

The BondAI framework offers flexible APIs to build your 
agent and create custom tools. It follows a straightforward implementation approach, making the tool creation process ha
ssle-free for developers.

Examples of included Tools:

* Google and Duck Duck Go Search
* Semantic Search for Files and
 Websites
* Alpaca Markets
* Gmail Integration
* Easily import tools from LangChain!

# 🐋 Docker Container

For a secure
 environment, especially while using tools with file system access, running BondAI within a docker container is highly r
ecommended. Follow the steps in the REAME to easily build and run the BondAI container.

🚀 Join the mission; contribute 
to BondAI! And please share feedback/ideas in the comments!
```
---

     
 
all -  [ Random/Wrong Answer - URL ](https://www.reddit.com/r/LangChain/comments/16omfio/randomwrong_answer_url/) , 2023-09-22-0909
```
I posted this in the llama2 subreddit but thought i'd try here as well, apologies if not allowed.  
I'm trying out the L
lama2 via llama cpp and langchain in a QA setup, very basic. I loaded only one document, txt that had something like the
 following below with nothing else,

ABC Order #1111
Status: Open

ABC Order #2222
Status: Shipped

ABC Order #3333
Stat
us: Cancelled

However when i asked, 'tell me about ABC Order #2222', it answered with:

'It has been shipped and you ca
n track it here https://tracking.abcorder.com/orders/2222'

My question on any thoughts where it even came up with that 
URL, is there something i can do with the prompts to avoid unnecessary info that wasn't asked, especially since it has n
o basis.

Thank you
```
---

     
 
all -  [ Random/Wrong answers ](https://www.reddit.com/r/LLaMA2/comments/16om6li/randomwrong_answers/) , 2023-09-22-0909
```
I'm trying out the Llama2 via llama cpp and langchain in a QA setup, very basic.  I loaded only one document, txt that h
ad something like the following below with nothing else,  


ABC Order #1111  
Status:  Open

ABC Order #2222  
Status: 
 Shipped

ABC Order #3333  
Status:  Cancelled

However when i asked, 'tell me about ABC Order #2222', it answered with:


 'It has been shipped and you can track it here [https://tracking.abcorder.com/orders/2222](https://tracking.abcrder.c
om/orders/2222)'

My question on any thoughts where it even came up with that URL, is there something i can do with the 
prompts to avoid unnecessary info that wasn't asked, especially since it has no basis.

Thank you
```
---

     
 
all -  [ looking for LangChain example_selector guide. Have you seen a good one? ](https://www.reddit.com/r/LangChain/comments/16olm9c/looking_for_langchain_example_selector_guide_have/) , 2023-09-22-0909
```
Hi

Im trying to find some more complex implementations guides for example\_selector.

[One from the docs](https://pytho
n.langchain.com/docs/modules/model_io/prompts/example_selectors/similarity) doesn't cover cases when your examples have 
nested json structure.

Will appreciate if you share some good  implementation  examples
```
---

     
 
all -  [ Getting completely random stuff with LlamaCpp when using the llama-2-7b.Q4_K_M.gguf model ](https://www.reddit.com/r/LocalLLaMA/comments/16oldrp/getting_completely_random_stuff_with_llamacpp/) , 2023-09-22-0909
```
Hello first I must say: I'm completely new to this. Today I tried the llama 7b model and this code

    from langchain.l
lms import LlamaCpp
    
    model = LlamaCpp(
        verbose=False,
        model_path='./model/llama-2-7b.Q4_K_M.gguf
',
    )
    
    o = model('Hi how are you?')
    print(o)

Returns a completely large random message that basically ju
st extends what I typed in.

The return is:

>I was asked by a friend to take over as leader of the local youth club. ev
erybody else has moved away or is busy, so who's going to run it?  
>  
>A: That's a difficult task.  
>  
>B: It was a 
really successful club, but nobody wants to do it any more. We need someone with experience and commitment.  
>  
>A: Ye
s, I can understand that.  
>  
>B: But what I don't know is whether you have the necessary experience or commitment.

&
#x200B;

I tried using a better prompt but it basically always happend that my model would just talk with itself and aut
ocomplete what I just typed and fantasizing.

Maybe someone could explain to me why that happens and how I prevent this 
from happening. 

&#x200B;
```
---

     
 
all -  [ LangChain in MOJO for speedup? 🔥 ](https://www.reddit.com/r/LangChain/comments/16ol9b0/langchain_in_mojo_for_speedup/) , 2023-09-22-0909
```
As far as I understand, you can run Python code in the newly released Mojo language for speedup, right? I haven't tried 
this out yet but was wondering:

Would using LangChain in Mojo (if possible) lead to any significant performance increas
e? E.g. Things like building a vector database from files can take some time with the DataLoader. 

Would love to hear w
hether this makes sense to try out or not. Thanks!
```
---

     
 
all -  [ DevOps AI Assistant Open Leaderboard ](https://www.reddit.com/r/devops/comments/16ol4d6/devops_ai_assistant_open_leaderboard/) , 2023-09-22-0909
```
Over the past year, a flurry of AI Assistants for DevOps engineers have been released. However, it's difficult to unders
tand their capabilities without benchmarking their performance. I recently built a [DevOps AI Assistant Open Leaderboard
](https://github.com/opstower-ai/devops-ai-open-leaderboard), a tool to benchmark a number of AI Assistants across a var
iety of DevOps tasks. The raw results, question datasets, and prompts used for evaluation [are available on GitHub](http
s://github.com/opstower-ai/devops-ai-open-leaderboard).

To start, I spent hours searching GitHub and other sources for 
DevOps-focused AI Assistants that can be invoked from the command line or a REST API, are functional, and and are not in
 private BETA. I found 12 AI assistants that met this criteria. Of these 12, 8 are able to directly interact with extern
al systems (versus just generating code or config file snippets). I was able to benchmark 5 of these AI Assistants with 
benchmarks for two more to come.

The current benchmarks are focused on the following tasks:

1. AWS Services
2. AWS Clo
udWatch Metrics
3. AWS Billing
4. kubectl

The following AI Assistants were benchmarked:

1. [OpsTower.ai](https://githu
b.com/opstower-ai/llm-opstower) (AWS Services, AWS CloudWatch Metrics, AWS Billing)
2. [ReleaseAI](https://release.ai/) 
(AWS Services, AWS CloudWatch Metrics, AWS Billing)
3. [mico](https://github.com/tahtaciburak/mico)  (kubectl)
4. [devin
jeon/kubectl-gpt](https://github.com/devinjeon/kubectl-gpt)  (kubectl)
5. [abhishek-ch/kubectl-GPT](https://github.com/a
bhishek-ch/Kubectl-GPT) (kubectl)

My biggest evaluation hurdle was generating ground truth data. These agents interact 
with external services in realtime and the data they return is constantly changing. Inspired by Langsmith's [dynamic eva
luation](https://github.com/langchain-ai/langsmith-cookbook/blob/main/testing-examples/dynamic-data/testing_dynamic_data
.ipynb), I created reference methods to return the data needed to generate correct answers. When evaluating an agent's a
ccuracy on a question/answer, the agent's response is compared to the response from the invoked reference method. I then
 rely on an GPT-4 to [generate a confidence score](https://github.com/opstower-ai/devops-ai-open-leaderboard/blob/main/p
rompts/dynamic_eval.rb) for each answer.

In short, GPT-4 is acting as a human evaluator. This is an approach I'm curren
tly comfortable with: in the early stages of evaluating OpsTower.ai, I started with static ground truth results and need
ed to evaluate the accuracy by hand. This became very tedious, so I implemented the dynamic evaluation mentioned above a
nd saw almost identical accuracy scores between the two approaches. Also, as mentioned in Eugene Yan's excellent [blog p
ost on LLM patterns](https://eugeneyan.com/writing/llm-patterns/#evals-to-measure-performance), using GPT-4 as an evalua
tor has a high correlation with human judgement.

## The results

First, hats off to the DevOps AI Assistants that I was
 able to get running! Many do not work, or the accuracy was so poor I assumed they were not functional.

Below is a summ
ary of answer accuracy. Full details [on GitHub](https://github.com/opstower-ai/devops-ai-open-leaderboard).

**AWS Serv
ices**

* [OpsTower.ai](https://OpsTower.ai) \- 92%
* [Release](https://Release.ai) AI - 72%

**AWS Cloudwatch Metrics**


* [OpsTower.ai](https://OpsTower.ai) \- 89%
* Release AI - 56%

**AWS Billing**

* [OpsTower.ai](https://OpsTower.ai) 
\- 91%
* Release AI - 73%

**Kubectl**

* abhishek-ch/kubectl-GPT - 83%
* devinjeon/kubectl-gpt - 50%
* mico - 17%

## O
bservations

**OpsTower.ai and Release AI appear to have the strongest foundation**. I believe they'd both likely handle
 the kubectl dataset questions well if each agent was trained on kubectl. The AWS dataset is more challenging as both th
e AWS REST API and the AWS CLI is more complex than kubectl.

**I think in the next six months, DevOps AI Assistants wil
l begin to perform more complex reasoning.** These agents first need to build up accuracy for the basic tasks, then they
 can can invoke those tasks when needed on advanced questions. I do not believe any capable of reliable complex reasonin
g today.

## Future work

I plan on adding additional benchmarks for Azure, Kubernetes cluster analysis, more AWS servic
es (ex: Cloudwatch Logs), and advanced reasoning.

## Comments and feedback

I'd love to get suggestions for DevOps AI A
ssistants I missed or other evaluation benchmarks you'd like to see! See [GitHub for for details](https://github.com/ops
tower-ai/devops-ai-open-leaderboard).
```
---

     
 
all -  [ How might I create a 'cast' of 'actors' that I can 'direct'? ](https://www.reddit.com/r/LangChain/comments/16ohy3q/how_might_i_create_a_cast_of_actors_that_i_can/) , 2023-09-22-0909
```
I’d like to create a “cast” that I can “direct.”

Something like this: ———->

**ACTOR 1**: An LLM agent who is a classic
ally trained actor and a member of the Royal Shakespeare Company.

**ACTOR 2**: An LLM agent who is a method actor known
 for being experimental.

**ME**: The Human

**SCENE:**

**Me**: “Ok Actor 1 and Actor 2, I want you to do the balcony s
cene from Romeo and Juliet.”

**\[Actors do the scene\]**

**Me**: “No, that was all wrong! Do it again but this time wi
th passion!”

**\[Actors do scene again, incorporating the director’s notes\]**

Any ideas about how to go about somethi
ng like that? Are there any frameworks/tools/repositories that could help me get there?
```
---

     
 
all -  [ Need Help with Adding Custom Instructions in Chainlit x Langchain with StorageContext ](https://www.reddit.com/r/datascience/comments/16ogkfd/need_help_with_adding_custom_instructions_in/) , 2023-09-22-0909
```
Hello everyone!

&#x200B;

I am a beginner working with Chainlit x Langchain and I am in need of some assistance. I am t
rying to figure out how to add custom instructions for generating answers, such as 'Answer like a pirate would'. I have 
some text files in the 'data' folder, and I'm curious about how to integrate such instructions within the existing setup
.

&#x200B;

Here's a snippet of the current code:

&#x200B;

`try:`

`# rebuild storage context`

`storage_context = St
orageContext.from_defaults(persist_dir='./storage')`

`# load index`

`index = load_index_from_storage(storage_context)`


 `except:`

`from llama_index import GPTVectorStoreIndex, SimpleDirectoryReader`

`documents = SimpleDirectoryReader('
./data').load_data()`

`index = GPTVectorStoreIndex.from_documents(documents)`

`index.storage_context.persist()`

  `u/
cl.on_chat_start async def factory():`

`llm_predictor = LLMPredictor(`

`llm=ChatOpenAI(`

`temperature=0,`

`model_nam
e='gpt-3.5-turbo',`

`streaming=True,`

`# openai_api_key=API_KEY`

`),`

`)`

`service_context = ServiceContext.from_de
faults(`

`llm_predictor=llm_predictor,`

`chunk_size=512,`

`callback_manager=CallbackManager([cl.LlamaIndexCallbackHan
dler()]),`

`)`

`query_engine = index.as_query_engine(`

`service_context=service_context,`

`streaming=True,`

`)`

`c
l.user_session.set('query_engine', query_engine)`

   `u/cl.on_message async def main(message):`

`query_engine = cl.use
r_session.get('query_engine')`

  `# type: RetrieverQueryEngine`

`response = await cl.make_async(query_engine.query)(me
ssage)`

`response_message = cl.Message(content='')`

`for token in response.response_gen:`

`await response_message.str
eam_token(token=token)`

`if response.response_txt:`

`response_message.content = response.response_txt`

`await respons
e_message.send()`  


I think I am stepping into the wrong direction, but I feel that this thing should not be that hard
.

I am looking for guidance on how to integrate custom instructions for answer generation in Chainlit x Langchain and w
ould appreciate any advice or suggestions on learning resources or paths.

 Looking forward to hearing your thoughts and
 suggestions!

&#x200B;

&#x200B;
```
---

     
 
all -  [ I created BoilerCode after shipping more than 40 products ](https://www.reddit.com/r/SideProject/comments/16ocna8/i_created_boilercode_after_shipping_more_than_40/) , 2023-09-22-0909
```
Hey 👋

I am Manoj, have been building products for a long time. Till now launched more than 40 products (some mobile app
s, some web apps, some chrome extensions)

Some of them failed quite early but some of them got more than 5k users. Earl
ier I used to do only B2C products and was offering everything for free. 

Then I shifted my focus on products on B2B an
d started shipping like crazy. Recently I took a challenge to ship a product in 24 hours and did that. Shared complete j
ourney on Twitter.

Anyway, I reuse my code as much as I can and that is the only reason how I can ship products fast 


And last week decided to combine all my reusable code and turned them into https://BoilerCode.co 

For now I have added 
NextJs Boilerplates and also included Langchain integration. 

All boilerplates comes with bunch of Integratione out of 
the box and also created a detailed documentation. 

(Btw you also get that documentation code in the boilerplates so yo
u can also create your custom blogs)

Let me know in case you have any questions/suggestion/feedback.

Always trying to 
improve the offerings. 

Cheers!!
```
---

     
 
all -  [ Final Year Project help. ](https://www.reddit.com/r/learnprogramming/comments/16oaczj/final_year_project_help/) , 2023-09-22-0909
```
I am a CS student in my final year. I want to create a project that would look good on my resume, and is feasible to be 
completed in one year.  
  
What I know so far:  


* C# and unity. Switching to Godot right now due to unity contro
versy, I don't want to continue with unity. But game dev was my passion. I have made basic games so far, like flappy bir
d clone, top down shooter, and a tetris clone.
* Flutter/Dart : Made a few basic mobile apps.
* Python : I have been l
earning to make apps on flask and langchain. With the new AI hype, I want to jump on the bandwagon and learn more about 
it.

  
My current plans:

1. Game dev AI Assistant : I will call it DevBuddy, or GameBro. The AI is a chatbot Plug-in 
in Godot engine. The AI will be trained on the documentation, and can assist the user. It will have 2 modes - Do (Instru
ction) and tell. In tell, you can ask it question on how to do a certain task in the version on Godot the user is on. Ex
 - It can tell step by step on how to change some settings, what the error means, etc. In do mode, you can give it instr
uctions like - Create a 2D character with a basic movement script. Create a script for a 2D shotgun prefab, which will f
ire 4 bullets at a 15 degree angle, with 'x' ammo, 'y' reload time. It will be very good for new users who have not made
 a game before.
2. AI simulates how the pyramids might have been built in ancient Egypt.
3. Mobile RPG or Puzzle Game,
 kinda like shattered pixel dungeon on the Play store.  

4. Mobile music app - First the app will search the music yo
u want to listen on Youtube, then download/stream the video you select in mp3 format. You can then create playlists usin
g downloaded songs.  
Or you can ask an AI to create you a playlist with the existing songs you have, or create a compl
etely new playlist based on what songs you like. It will then stream it for you. You can download the playlist if you wa
nt to.  


I would like to receive feedback, or any new ideas that you have. I will discuss it with a professor tomorr
ow, but I feel like I needed to be be in the right headspace or something. I feel like he will be disappointed in my pro
posals.
```
---

     
 
all -  [ What is the best way to use GPT4 to query multiple csvs/dataframes? ](https://www.reddit.com/r/LangChain/comments/16oa87p/what_is_the_best_way_to_use_gpt4_to_query/) , 2023-09-22-0909
```
Langchain is not serving the purpose. Do you guys have any suggestion or would you suggest I need to build my own thing?

```
---

     
 
all -  [ Questions regarding how to proceed with my AI journey ](https://www.reddit.com/r/ArtificialInteligence/comments/16o5n00/questions_regarding_how_to_proceed_with_my_ai/) , 2023-09-22-0909
```
Hey there!  


I'm not new to ML/AI since I'm studying a bachelor in astronomy (So I do have all the linear algebra/calc
ulus/stats knowledge), but I do have a really weak knowledge in AI in general. I work for a big tech company, but my rol
e is very specific. We could say I'm a Data engineer (more kind of an SQL Developer in GCP). I was diagnosed with ADHD a
 couple months ago, and I'm treting it. The results are amazing, and now I can really focus on learning new things, and 
I'm really doing it and taking advantage of it. I'm really really motivated. I'm trying to switch to this area since las
t year, but because of a couple things (including ADHD) I could not advance too much, more than the 'basics' (Data clean
ing, EDA, Modelling, basic metrics, etc). I do have an Udemy business account given by the company, a Workera account, a
nd I'm slowly going for the Professional machine learning engineer certfication by Google Cloud. My questions are the fo
llowing:  


1) I'm tired of doing courses. Do you know any practical guide with exercises and/or things to gain general
 knowledge doing more than watching courses and copying what their 'exercises' say? I know that the best way is to do id
eas that I do have (e.g. I wanna make a model for recognizing guitar brands from an image), but to get stronger in the b
asics, I'd really appreciate some recommendations.

&#x200B;

2) Since I'm more into the end-to-end solutions (a.k.a cre
ating a full ML/AI product), what tools/stacks do you recommend for 'general' MLOps/AIOps purposes (such as model monito
ring, model serving, pipelines, CI/CD, feature store, AutoML, etc) that does not belong to any cloud provider? I'm talki
ng about tools like Kubeflow, MLFlow, Tensorflow extended, Flask, Gradio, etc.

&#x200B;

3) What are the tools/stacks a
re companies asking for on this kind of job positions?

&#x200B;

4) My company is making a very big focus on LLMs (as e
veryone is doing right now). What courses/exercises do you recommend doing for gaining experience/knowledge? What tools/
frameworks? I only know about LangChain and Huggingface.

&#x200B;

As I mentioned, I'd really appreciate your help sinc
e I'm very motivated and I have a lot of opportunities to get certifications/courses done, and I just want to develop my
 AI/ML career the best and most optimal way.

&#x200B;

Thanks!

&#x200B;

P.S: I've been reading the 'Education/Learnin
g' section, and it's really interesting, including demos/exercises/courses more tailored to practical learning, but I re
ally want to get more opinions than just going straight to this without any other options.
```
---

     
 
all -  [ Is it just me or is Langchain is too complicated to understand and work with? (r/DataScience) ](https://www.reddit.com/r/datascience/comments/16ni0h7/is_it_just_me_or_is_langchain_is_too_complicated/) , 2023-09-22-0909
```

```
---

     
 
all -  [ Semantic document search ](https://www.reddit.com/r/LangChain/comments/16nvy5b/semantic_document_search/) , 2023-09-22-0909
```
Suggest me some resources for semantic document search

It's not searching semantically in a document but searching a do
cument from a group of documents.
```
---

     
 
all -  [ How to manage ReAct agent prompt size as iterations increase? ](https://www.reddit.com/r/LangChain/comments/16nuytk/how_to_manage_react_agent_prompt_size_as/) , 2023-09-22-0909
```
As the number of iterations increase for an agent, the prompt for the LLM planning step quickly becomes larger and large
r until it exceeds the prompt limit. What strategies are y'all using to manage the prompt size during the planning phase
? This has been especially a problem when the output of a tool is sizable. 
```
---

     
 
all -  [ Zep's New Web UI: Easily Manage Your LLM App's Users, Memory, and Vector Indexes ](https://www.reddit.com/r/LangChain/comments/16nufn5/zeps_new_web_ui_easily_manage_your_llm_apps_users/) , 2023-09-22-0909
```
Hey all, Zep now has a Web UI! 🔥🎉  You can manage users, memories, vector indexes, and more via Zep’s web admin interfac
e.

**What's Zep?** 

With Zep, you can take your LLM app prototype to production in minutes with fast, scalable buildin
g blocks for memory, search, and enrichment. No recoding required as Zep’s components are drop-in replacements for exist
ing LangChain or LlamaIndex classes.  


🎥 A quick demo of Zep in action: [https://vimeo.com/865785086?share=copy](https
://vimeo.com/865785086?share=copy)  
🏠 Zep website: [https://www.getzep.com/](https://www.getzep.com/)  
⭐️ Zep on GitHu
b [https://github.com/getzep/zep](https://github.com/getzep/zep)

&#x200B;

https://preview.redd.it/kpcrt8t6rgpb1.png?wi
dth=2184&format=png&auto=webp&s=69c4b1693e2a0556c90f482ee269b48f626cff99
```
---

     
 
all -  [ Urgent question: uploading docs to llama ](https://www.reddit.com/r/LocalLLaMA/comments/16ns4hk/urgent_question_uploading_docs_to_llama/) , 2023-09-22-0909
```
So I wanna know if I build a chat bot with llama2, is there a feature that would allow users to upload their local docum
ents onto the platform and help them with queries related to that ?

I saw langchain approach where you cut the file int
o smaller chunks and then use vector db. But is that something which can be done with an actual product used in a large 
company?
```
---

     
 
all -  [ How to decide when call a tool or not ](https://www.reddit.com/r/LangChain/comments/16ni6us/how_to_decide_when_call_a_tool_or_not/) , 2023-09-22-0909
```
Hi all, someone knows how can i set if i want to call one tool or no, my specific case is as following: I want to ask by
 default to chatgpt but if chatgpt is not able to answer because the question involve context posterior to 2021 I want t
o call the Serpapi tool to search in internet for the information, I do not want to call the tool every time because it 
would have extra cost. I'm not able to find any tutorial or documentation that show how to achieve this.  
Thanks in adv
ance for the help.
```
---

     
 
all -  [ group by or unique in search result using similaritySearch ](https://www.reddit.com/r/Supabase/comments/16ng8hs/group_by_or_unique_in_search_result_using/) , 2023-09-22-0909
```
 i embed text documents and chose supabase as my vector store. documents can have multiple embeddings. but i want to gro
up it with only one result per document.  also if there is a way to paginate this result  i use langchain, supabase pgve
ctor and supabase gte-small hugging face 
```
---

     
 
all -  [ FineTuning vs LangChain .. or a Mix ? ](https://www.reddit.com/r/LocalLLaMA/comments/16nfwhx/finetuning_vs_langchain_or_a_mix/) , 2023-09-22-0909
```
Hey everyone ,

excuse me if I sound like a noob in these topics . but recently I discovered the world of huggingface an
d local LLMs . I work at a company that provides software services to a lot of clients , and one of our products is supp
osed to be a chatbot that aids the customers by guiding them or answering any question about that client . in addition t
o that , each customer has some personal data in the client's database , let's say stuff like name , date joined , activ
ity .. and other analytics regarding his membership with that specific client . which all of them can be easily retrieve
d by using our companies API requests that returns user info in a json format .

I came across this post [https://www.re
ddit.com/r/LocalLLaMA/comments/14vnfh2/my\_experience\_on\_starting\_with\_fine\_tuning\_llms/](https://www.reddit.com/r
/LocalLLaMA/comments/14vnfh2/my_experience_on_starting_with_fine_tuning_llms/)that further made me realize that fine-tun
ing a model on that client's specific data might be a good idea .

collect data , structure it like (preferably in  #ins
truction,#input,#output format as I saw this is good format based on alpaca-cleaned data-set) , and fine-tune one of the
 hugging face models on it . that way , any question about that client , the model would be able to answer it in a speci
fic way rather than a generic way like a generic LLM would do .

ok great , let's say we fine-tuned the model on that cl
ient's data , and now it can answer any question about that client for the user like any FAQ , any info about the client
 , how to register , how to cancel etc...  but it got me thinking , how would I also train the model to be able to answe
r queries where the user asks about some specific info about himself and not just some generic info question about the c
lient ? , imagine if the client is a gym , how can I train the model to be also able to answer a question similar to 'wh
en does my membership end ?' . should I provide also in the training data examples for these types of questions with som
e fake data about a fake user ? or is there no need to train the model on these types of questions and just do it using 
LangChain by specifying type of chains that get user info as input and a query from the user , while also providing some
 examples in the prompt to further help the LLM understand how the questions is supposed to be answered ?but also , how 
would I do that in Langchain for a lot of different types of queries ? should I just think of a lot of possible queries 
from that user that asks for specific user info ?

or is there a dynamic way in langchain to firstly get the query , fig
ure out what sort of info needed to answer the question , use one of our API calls to retrieve the info , and then answe
r using that Info ?

sorry if I rambled some nonsense , I would be happy for some advice from you guys
```
---

     
 
all -  [ dialoqbase – open source chatbot creation platform ](https://www.reddit.com/r/ChatGPT/comments/16nerpm/dialoqbase_open_source_chatbot_creation_platform/) , 2023-09-22-0909
```
I have been working on a side project for the last 3 months, built around LangchainJS and pgvector. It now supports *Cha
tGPT*, *Llama*, *Claude*, and *Bison* models, and the bot can integrate with WhatsApp, Telegram, and Discord for now. I 
would really appreciate some feedback. Thanks!

repo: [https://github.com/n4ze3m/dialoqbase](https://github.com/n4ze3m/d
ialoqbase)
```
---

     
 
all -  [ [P] vLLM, Langchain, Embedchain ? ](https://www.reddit.com/r/MachineLearning/comments/16ndyxc/p_vllm_langchain_embedchain/) , 2023-09-22-0909
```
Which libraries do you think would be the most important to learn between these, and to use in my next personal project 
? This will be a conversational chatbot trained on podcast transcripts
```
---

     
 
all -  [ History is troublesome. Answers with knowledge of subject but not with context information. ](https://www.reddit.com/r/LangChain/comments/16n6qsv/history_is_troublesome_answers_with_knowledge_of/) , 2023-09-22-0909
```
So here is my problem. I use the  ConversationalRetrievalQAChain and provide those history messages: 

      const pastM
essages = [
        new SystemMessage('Always provide helpful information. Sometimes you can infer it from previous mess
ages. You always know an answer.'),
        new HumanMessage('Who is he?'),
        new AIMessage('Barack Obama is an Am
erican politician who served as the 44th President of the United States. He was born on August 4, 1961, in Honolulu, Haw
aii. Barack Obama is a member of the Democratic Party and made history by becoming the first African American president 
of the United States.'),
      ];

When I then ask e.g. ' Please make the text shorter' it always answers with ' I'm sor
ry, but I don't have any information on Barack Obama in the provided context. ' or something similar. The same when I wa
nt to know the age or something. It is really weird. GPT-4 appears to always know the subject of the past messages but n
ot the rest of the content.   


Does anyone know how to fix this?
```
---

     
 
all -  [ Using language models to create a robotic ecosystem ](https://www.reddit.com/r/computervision/comments/16n5s0g/using_language_models_to_create_a_robotic/) , 2023-09-22-0909
```
Hello everyone,

Me and my friends at RoboCoach Inc (a san diego based startup) recently created this open source projec
t to use GPT and Langchain to capture the details of a robotic design through human language interface, and to automatic
ally create the ROS (Robot Operating System) packages:

[https://github.com/RoboCoachTechnologies/ROScribe](https://gith
ub.com/RoboCoachTechnologies/ROScribe)

Demo: [https://www.youtube.com/watch?v=H2QaeelkReU](https://www.youtube.com/watc
h?v=H2QaeelkReU) 

Please check it out and let me know what you think. It works for ROS1 for now, but we will add ROS2 v
ery soon. We plan to add a lot of features into this software, so stay tuned for future releases.

We appreciate if you 
drop us a star on our repo, if you download the code, run it, and file issues, and if you contribute to this robotic pro
ject. We plan to make a robotic ecosystem based on LLMs and ROS. This is just the first step toward that goal.

I hope t
his tool helps your next robotics project.

&#x200B;
```
---

     
 
all -  [ How to leverage user feedback into my LLM application? ](https://www.reddit.com/r/LangChain/comments/16n4fug/how_to_leverage_user_feedback_into_my_llm/) , 2023-09-22-0909
```
As a context, we have a multiuser chatbot based on LangChain + OpenAI, it does RAG with conversational memory. 

The use
r can rate every response of the LLM with 👍👎buttons.

Concersations are stores as is feedback. So we know the questions 
and answers that where down voted. 

Right now we are not leveraging that anyhow.

I'm looking for inspiration on how to
 leverage the user feedback.

Do you guys have implemented such user feedback thing and how do you use it?
(of course i 
could review it manually, or fo reporting on it... And later make decisions base on the reports/analytics.)

 I'm more l
ooking for ways to get the LLM (or LLM based application) to use that information to give better answer or not give agai
n the same answer if it was down voted...
```
---

     
 
all -  [ Why is langchain not using 'messages' from OpenAI's chat completion endpoint? ](https://www.reddit.com/r/LangChain/comments/16n3eka/why_is_langchain_not_using_messages_from_openais/) , 2023-09-22-0909
```
I was exploring the prompts in Langchain's agents and the calls to OpenAI's endpoints, and I found it doesn't use the ['
messages' param when calling ChatCompletion](https://platform.openai.com/docs/api-reference/chat/streaming), but instead
 puts everything in the prompt such as:

    Instruction.
    
    Chat History:
    {conversation between Human and Ass
istant}
    
    New question:
    {new message}
    
    Assistant:

Why is this? I can think of some advantages, such 
as:

1. Conceptually, it makes more sense as an LLM receives a string to predict a string
2. It is LLM agnostic
3. It al
lows you to have more control of what's going on
4. It makes everything more transparent

But, am I missing something?
```
---

     
 
all -  [ Enhancement idea and feedback ](https://www.reddit.com/r/LangChain/comments/16n1njd/enhancement_idea_and_feedback/) , 2023-09-22-0909
```
We have developed a unified AI-driven platform that lets you engage with all your favorite businesses right from a singl
e WhatsApp chat. No need to give away you contact number or sift through spammy messages. Llms are integrated to make in
teractions more personalized and context-rich. The platform also features 'Consolidated Communications,' where we bundle
 similar offers or messages from various providers into one easy-to-digest update. For businesses, we offer valuable ana
lytics and targeted marketing opportunities. How do you think Langchain could fit into enhancing this experience? We're 
eager to hear your input!
```
---

     
 
all -  [ How to approach using langchain to train OpenAI with Network Traffic Logs ](https://www.reddit.com/r/LangChain/comments/16n05w1/how_to_approach_using_langchain_to_train_openai/) , 2023-09-22-0909
```
Hello! I am currently doing an independent study at my university on using OpenAI's API to help in areas like data analy
tics and cybersecurity. My professor gave me a massive dataset of about 1,500,000 lines of network traffic logs to use i
n training for OpenAI to be able to detect a cyberattack. I will paste some example lines below. Does anyone have some i
nsight in how I can use langchain in this project? To be honest I am not even sure where to start, but I think I'd like 
to start with an example only using like 1000 lines with 70% training and 30% test. Any help and insight is GREATLY appr
eciated!

0,tcp,private,S0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,292,8,1.00,1.00,0.00,0.00,0.03,0.06,0.00,255,8,0.03,0.06,
0.00,0.00,1.00,1.00,0.00,0.00,neptune.  0,tcp,private,S0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,293,9,1.00,1.00,0.00,0.00,0
.03,0.06,0.00,255,9,0.04,0.06,0.00,0.00,1.00,1.00,0.00,0.00,neptune.  0,tcp,private,S0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
,0,294,4,1.00,1.00,0.00,0.00,0.01,0.06,0.00,255,4,0.02,0.06,0.00,0.00,1.00,1.00,0.00,0.00,neptune.  0,icmp,eco\_i,SF,8,0
,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,44,0.00,0.00,0.00,0.00,1.00,0.00,1.00,1,255,1.00,0.00,1.00,0.50,0.00,0.00,0.00,0.00,i
psweep.  0,icmp,eco\_i,SF,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,43,0.00,0.00,0.00,0.00,1.00,0.00,1.00,2,255,1.00,0.00,1.
00,0.50,0.00,0.00,0.00,0.00,ipsweep.  1,tcp,smtp,SF,1466,330,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,1,0.00,0.00,0.00,0.00,1.0
0,0.00,0.00,1,1,1.00,0.00,1.00,0.00,0.00,0.00,0.00,0.00,normal.  1,tcp,smtp,SF,1646,328,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,
1,2,0.00,0.00,0.00,0.00,1.00,0.00,1.00,72,53,0.74,0.04,0.01,0.00,0.00,0.00,0.00,0.00,normal. 1154,tcp,telnet,SF,360,1078
36,0,0,1,0,0,1,9,0,0,1,0,0,0,0,0,0,1,1,0.00,0.00,0.00,0.00,1.00,0.00,0.00,73,1,0.01,0.05,0.01,0.00,0.00,0.00,0.00,0.00,n
ormal.
```
---

     
 
all -  [ Semantic text splitting using LLMs ](https://www.reddit.com/r/LangChain/comments/16mz4e7/semantic_text_splitting_using_llms/) , 2023-09-22-0909
```
Hey,   


At Neum AI, we have been playing around with several iterations of doing semantic text splitting using LLMs. T
oday, we released an open-source package with our latest for people to try out. At a high level, these capabilities enab
le you to provide a sample piece of text and let the tool come up with a strategy to split that text. That strategy gets
 converted to code which you can then leverage across a document set. We have found this to be especially useful when we
 have large number of documents that follow patterns / templates, as well as when we have customers give us one offs tha
t are hard to split using more traditional methods. 

The tool is by no means perfect, but at least gives a good idea of
 the right direction to take when chunking the document. You can try out the tools either on our playground or directly 
using our python module. Links to both below:  


Learn more: [Contextually splitting documents (neum.ai)](https://www.n
eum.ai/post/contextually-splitting-documents) 

Playground: [Streamlit (neumai-playground.streamlit.app)](https://neumai
-playground.streamlit.app/) 

Module: [neumai-tools · PyPI](https://pypi.org/project/neumai-tools/) 
```
---

     
 
all -  [ Fundamental Q on Langchain from a newbie ](https://www.reddit.com/r/LangChain/comments/16my8sa/fundamental_q_on_langchain_from_a_newbie/) , 2023-09-22-0909
```
Hey, I'm just getting started with langchains and I have a fundamental question. 

How does a person who wants to build 
a langchain know whether or not the information they plan on building a langchain with is already in the LLM they want t
o connect with? 

Consequently, how does one know their efforts won't be a waste of time and energy being redundant?
```
---

     
 
all -  [ [INSTANT DOWLOAD] Peter – Buildfast Masterclass – Learn to build your own AI chatbot ](https://www.reddit.com/r/DailyNewsEco/comments/16mv0ch/instant_dowload_peter_buildfast_masterclass_learn/) , 2023-09-22-0909
```
**Download this course here:** [**Peter – Buildfast Masterclass – Learn to build your own AI chatbot**](https://shoppy.g
g/product/gTTVpAo)

[**Sale Page**](https://buildfast.academy/) 

**Here are all of the videos inside Fundamentals**  
*
*That you get instant access to upon joining BuildFast**

1. **LLMs: Overview, using LLMs in Langchain, open-sourced LLM
s, chat model, embedding text.**
2. **Chains: Chains 101, LLM Chain, Sequential Chain, and four other important Langchai
n chains.**
3. **Prompt: Prompts 101, Example Prompts, Output Parser.**
4. **Memory: 4 Memory Types Explained, How to us
e Memory in a Chain, How to add Memory to an Agent**
5. **Document Loaders: Document Loaders 101, When to use Document L
oader, Import data from Text & CSV, and Loading data from Discord, Notion, Telegram**
6. **Indexes: Indexes 101, Retriev
ers and Text Splitters.**
7. **Vector Database & Embeddings: Vector databases 101, when to use vector databases, Embeddi
ngs and vector database use-cases.**
```
---

     
 
MachineLearning -  [ [R] Agents: An Open-source Framework for Autonomous Language Agents - AIWaves Inc 2023 ](https://www.reddit.com/r/MachineLearning/comments/16jl4pe/r_agents_an_opensource_framework_for_autonomous/) , 2023-09-22-0909
```
Paper: [https://arxiv.org/abs/2309.07870](https://arxiv.org/abs/2309.07870) 

Github: [https://github.com/aiwaves-cn/age
nts](https://github.com/aiwaves-cn/agents) 

Abstract:

>Recent advances on large language models (LLMs) enable research
ers and developers to build autonomous language agents that can automatically solve various tasks and **interact with en
vironments, humans, and other agents** using natural language interfaces. **We consider language agents as a promising d
irection towards artificial general intelligence** and release Agents, an **open-source library** with the goal of openi
ng up these advances to a wider non-specialist audience. Agents is carefully engineered to support important **features 
including planning, memory,  tool usage, multi-agent communication, and fine-grained symbolic  control.** Agents is **us
er-friendly** as it **enables non-specialists** to build, customize, test, tune, and deploy state-of-the-art **autonomou
s language agents without much coding**. The **library** is also **research-friendly as its modularized design** makes i
t **easily extensible for researchers.** 

https://preview.redd.it/3bdi71r5rgob1.jpg?width=1131&format=pjpg&auto=webp&s=
760942c19be6ecda791414c812a77e72751c526d

https://preview.redd.it/howf64r5rgob1.jpg?width=1656&format=pjpg&auto=webp&s=6
36744fccab7a1c2bafb902bad5dbb647440fff5

&#x200B;
```
---

     
 
MachineLearning -  [ [P] Ways to speed up llama-2 summarization on sagemaker? ](https://www.reddit.com/r/MachineLearning/comments/16iutyp/p_ways_to_speed_up_llama2_summarization_on/) , 2023-09-22-0909
```
I'm currently working on a project to give a quick summary of long articles/conversations.

I'm running llama-2-7b-chat-
hf with 4bit quantization on a g5.2xlarge instance on sagemaker.

The method I'm using is map\_reduce (option 2)from thi
s webpage [https://python.langchain.com/docs/use\_cases/summarization](https://python.langchain.com/docs/use_cases/summa
rization))

Of everything I've tried this is the only one that's been able to do decent summaries in a reasonable amount
 of time. However with really long articles (10,000+ words) it takes \~6 minutes before giving an output.

I tried runni
ng this same thing on a g5.12xlarge instance which has 4 A10G gpus but it hasn't reduced the time by any noticeable amou
nt.

Is there anything else I could be doing to speed this up?

&#x200B;

For reference here is the code I'm running in 
Sagemaker notebook

[https://gist.github.com/phwang4/1ab4d772228b6fff8616c28ac054c229](https://gist.github.com/phwang4/1
ab4d772228b6fff8616c28ac054c229)
```
---

     
 
MachineLearning -  [ [P][R] Kani: A Lightweight Highly Hackable Open-Source Framework for Building Chat Applications with ](https://www.reddit.com/r/MachineLearning/comments/16gxp51/pr_kani_a_lightweight_highly_hackable_opensource/) , 2023-09-22-0909
```
Hey all, we just released our new project/paper and we thought you all might find it useful!

Our project (Kani) is a su
per lightweight and hackable alternative to frameworks like LangChain or simpleAIchat meant to help developers hook in c
allable functions or tools to chat models easily. With Kani, devs can write functions in pure python and just add one li
ne (the `@ai_function()` decorator) to turn any function into an AI-callable function!

Kani works with any model and ha
s built-in tools for OpenAI, HuggingFace, LLaMAv2, Vicuna, and GGML with more to come. Kani also never does any prompt e
ngineering under the hood and doesn't require learning complex library tools---all defaults are minimal and highly custo
mizable.

Check out our Colab for mini-examples of things like retrieval, web-search, model routing, etc. [https://colab
.research.google.com/github/zhudotexe/kani/blob/main/examples/colab\_examples.ipynb](https://colab.research.google.com/g
ithub/zhudotexe/kani/blob/main/examples/colab_examples.ipynb)  

If you're interested in learning more check out our lin
ks below!  
Paper: [https://arxiv.org/abs/2309.05542](https://arxiv.org/abs/2309.05542)  
GitHub: [https://github.com/zh
udotexe/kani](https://github.com/zhudotexe/kani)  
Docs: [https://kani.readthedocs.io/](https://kani.readthedocs.io/)
```
---

     
 
MachineLearning -  [ [D] Data Extraction using fine-tuned LLM? ](https://www.reddit.com/r/MachineLearning/comments/16fenlb/d_data_extraction_using_finetuned_llm/) , 2023-09-22-0909
```
Hey Reddit,

I'm working on a tool to pull data from highly irregular Excel files. I've gotten reasonable results which 
is extremely fast with standard Python coding, but it's far from perfect due to the lack of standardized templates. 

In
terestingly, when I tested ChatGPT-4 on a sample table, it did a decent job at data extraction. However, relying solely 
on GPT-4 has its downsides like token limits and slow processing speed (and data privacy issues). Plus, splitting the Ex
cel sheet to fit within these limits results in loss of context and data.

I'm considering fine-tuning a language model 
to post-process data that was in a Pandas DataFrame (perhaps converted to JSON). Has anyone had success with this approa
ch or have alternative recommendations? I've tried Langchain, but it wasn't helpful.

I have figured out to extract the 
relevant columns, but the post-processing part is where I am considering using an LLM which understands the domain and w
hat needs to be extracted based on the examples I feed it.

Looking forward to your thoughts! And would be happy to answ
er any additional questions.
```
---

     
 
MachineLearning -  [ [D] Chains and Agents ](https://www.reddit.com/r/MachineLearning/comments/16d7ee6/d_chains_and_agents/) , 2023-09-22-0909
```
I think there's a lot of confusion around AI agents today and it's mainly because of lack of definition and using the wr
ong terminology.

We've been talking to many companies who are claiming they're working on agents but when you look unde
r the hood, they are really just chains.

I just listened to the Latent Space pod with Harrison Chase (Founder of Langch
ain) and I really liked how he thinks about chains vs agents.

Chains: sequence of tasks in a more rigid order, where yo
u have more control, more predictability.  
Agents: handling the edge-cases, the long-tail of things that can happen.

A
nd the most important thing is that it's not an OR question but an AND one: you can use them in the same application by 
starting with chains -> figuring our the edge-cases -> using agents to deal with them.

https://preview.redd.it/l59sc4sr
i0nb1.png?width=3127&format=png&auto=webp&s=1f3f8730c48687eaabf1f554deb181cf35b96036
```
---

     
 
MachineLearning -  [ [P] FalkorDB - a fast Graph Database - Knowledge Graph as RAG ](https://www.reddit.com/r/MachineLearning/comments/16cg6k7/p_falkordb_a_fast_graph_database_knowledge_graph/) , 2023-09-22-0909
```
We're building a fast low latency Graph Database called FalkorDB that will also support Vector search.  
It's based on R
edis and can be used both as a stand alone database or a module for existing Redis.  
It feels like that is going to be 
the most optimized way to serve Knowledge as RAG, would love to get your feedback.  
[https://github.com/FalkorDB/falkor
db](https://github.com/FalkorDB/falkordb)  


It already supports LlamIndex and Langchain:  
[https://python.langchain.c
om/docs/use\_cases/more/graph/graph\_falkordb\_qa](https://python.langchain.com/docs/use_cases/more/graph/graph_falkordb
_qa)  
[https://gpt-index.readthedocs.io/en/latest/examples/index\_structs/knowledge\_graph/FalkorDBGraphDemo.html](http
s://gpt-index.readthedocs.io/en/latest/examples/index_structs/knowledge_graph/FalkorDBGraphDemo.html)

&#x200B;
```
---

     
 
MachineLearning -  [ [D] Is there anything LangChain can do better than using LLMs directly (either through a website or  ](https://www.reddit.com/r/MachineLearning/comments/165airj/d_is_there_anything_langchain_can_do_better_than/) , 2023-09-22-0909
```
I haven't used ChatGPT a lot or any other LLMs, I've been reading about  Langchain and its use cases, and I'm having tro
uble wrapping my head  around exactly what it does. From what I understand, its an alternative  interface for LLMs, allo
wing for easy switching between them, and makes  some work for specific use cases easier. If I wanted to write an app or
  script to interact with LLMs and do other tasks, how would LangChain be  better than just making API call(s) to an LLM
, getting back the result  as a string, and doing whatever with it?
```
---

     
 
MachineLearning -  [ Apache Airflow vs. LangChain and LlamaHub for LLM data pipeline [D] ](https://www.reddit.com/r/MachineLearning/comments/160lexg/apache_airflow_vs_langchain_and_llamahub_for_llm/) , 2023-09-22-0909
```
I’m looking for recommendations, suggestions, and/or good documentation that outlines which data pipeline would be best 
to ingest my private data (which will then be split into chunks/nodes for vector embeddings and so forth). Thank you in 
advance!
```
---

     
 
MachineLearning -  [ [P] LLM Apps Are Mostly Data Pipelines ](https://www.reddit.com/r/MachineLearning/comments/15z0muk/p_llm_apps_are_mostly_data_pipelines/) , 2023-09-22-0909
```
My colleague just wrote up an article on [LLM-based apps and how to use data engineering tools to help build them faster
](https://meltano.com/blog/llm-apps-are-mostly-data-pipelines/) that I found really insightful.

It contains a complete 
implementation

* with scraping context data from a docs website
* chunking it, getting embeddings via the openAI API
* 
loading it into pinecone
* and finally a simple Q&A interface with streamlit on top of it

**Here's a quick summary:**


* LangChain and LlamaIndex are great tools for quick exploration
* But aren't perfect for production-grade use
* I think
 we all know the 'LangChain is pointless' debate, but there's a lot of real meat to it, and Pat describes a few of them 
(a lot of LangChains extractors are super basic, 2-3 liners without retries etc.)
* LLM applications are all about movin
g data, extracting and enriching data (creating embeddings!) are the most expensive ones of those steps
* A bunch of dat
a engineering tools are out there that make these two steps much easier, versionable, robust, and reproducible.
* Meltan
o is one such tool and Pat implemented the above described pipeline with it

**FWIW**: The GitHub project that comes wit
h the post is super easy to run and super modular. I just tested it and was able to modify everything for my own applica
tion within 30 mins.
```
---

     
 
deeplearning -  [ TheBloke/Llama-2-7b does not appear to have a file named pytorch_model.bin, tf_model.h5, model.ckpt  ](https://www.reddit.com/r/deeplearning/comments/16ihzn8/theblokellama27b_does_not_appear_to_have_a_file/) , 2023-09-22-0909
```
Hey everyone!

As you can guess from the title, this is the error I get. I only changed the model in AutoModelForCausalL
M, Older version was 

&#x200B;

&#x200B;

`'''`

`model = AutoModelForCausalLM.from_pretrained('meta-llama/Llama-2-7b-c
hat-hf',`

`device_map ='auto',`

`torch_dtype = torch.float16,`

`use_auth_token = True)`

`'''`

&#x200B;

However, si
nce my GPU is NVIDIA GeForce RTX 2080 TI, it answers a simple question in 20 mins. Then I changed it to: 

`model = Auto
ModelForCausalLM.from_pretrained('TheBloke/Llama-2-7b-Chat-GGUF',`

`model_file = 'llama-2-7b-chat.q4_K_M.gguf',`

`devi
ce_map ='auto',`

`torch_dtype = torch.float16,`

`use_auth_token = True)`

&#x200B;

However, this is not working, and 
giving the error. Below is the full code, if it is needed to solve.

&#x200B;

&#x200B;

from langchain.document\_loader
s import JSONLoader

from langchain.text\_splitter import CharacterTextSplitter, TokenTextSplitter, RecursiveCharacterTe
xtSplitter

from langchain.embeddings import HuggingFaceEmbeddings

from langchain.vectorstores import Chroma

from lang
chain import HuggingFacePipeline

from langchain.chains import ConversationalRetrievalChain

from langchain.memory impor
t ConversationBufferMemory

from langchain.embeddings.openai import OpenAIEmbeddings

from langchain.embeddings.huggingf
ace import HuggingFaceEmbeddings

from langchain.chat\_models import ChatOpenAI

import os

import sys

import huggingfa
ce\_hub

from huggingface\_hub import notebook\_login

import torch

import transformers

from transformers import AutoT
okenizer, AutoModelForCausalLM, pipeline

from torch import cuda, bfloat16

import chromadb

from pathlib import Path

f
rom pprint import pprint

import json

from loader import JSONLoader

from [langchain.prompts.chat](https://langchain.pr
ompts.chat) import PromptTemplate, HumanMessagePromptTemplate, SystemMessagePromptTemplate, ChatPromptTemplate

import j
son

from langchain.docstore.document import Document

&#x200B;

def parse\_json(json\_data):

'''Parse JSON data into a
 Python dictionary.'''

return json.loads(json\_data)

&#x200B;

def create\_doc(json\_data):

'''Create a Document obje
ct from JSON data.'''

data = parse\_json(json\_data)

content\_value = ''

&#x200B;

\# Collect values of keys that con
tain 'item' in their name

for key, value in data.items():

if 'item' in key.lower():

content\_value += value + '\\n' 




&#x200B;

return Document(page\_content=content\_value, metadata={'company': data\['company'\]})

&#x200B;

&#x200B;


\##embed\_model\_id = 'BAAI/bge-base-en' ## CHANGE

&#x200B;

embed\_model\_id = 'sentence-transformers/all-mpnet-base-
v2'

&#x200B;

&#x200B;

&#x200B;

device = f'cuda:{cuda.current\_device()}' if cuda.is\_available() else 'cpu' ## NVIDI
A GeForce RTX 2080 TI

&#x200B;

embed\_model = HuggingFaceEmbeddings(

model\_name=embed\_model\_id,

model\_kwargs={'d
evice': device},

encode\_kwargs={'device': device, 'batch\_size': 32}

)

&#x200B;

docs = \[\]

&#x200B;

&#x200B;

fo
r file in os.listdir('lessdata'):

if file.endswith('.json'):

file\_path = './lessdata/'+file

with open(file\_path) as
 file:

json\_data = [file.read](https://file.read)()

document = create\_doc(json\_data)

docs.append(document)

&#x200
B;

&#x200B;

document\_splitter = RecursiveCharacterTextSplitter(separators=\['\\n'\], chunk\_size = 500, chunk\_overla
p = 100)

document\_chunks = document\_splitter.split\_documents(docs)

&#x200B;

&#x200B;

vectordb = Chroma.from\_docu
ments(document\_chunks,embedding=embed\_model, persist\_directory='./database')

&#x200B;

\##vectordb.persist()

'''

v
ectordb = Chroma.from\_documents(document\_chunks,embedding=embed\_model, persist\_directory='./database')

vectordb.per
sist('./database')

&#x200B;

&#x200B;

'''

&#x200B;

&#x200B;

&#x200B;

\### PLEASE DO NOT TOUCH THE VSCODE

&#x200B;


&#x200B;

tokenizer = AutoTokenizer.from\_pretrained('meta-llama/Llama-2-7b-chat-hf', use\_auth\_token = True,)

&#x20
0B;

&#x200B;

model = AutoModelForCausalLM.from\_pretrained('TheBloke/Llama-2-7b-Chat-GGUF',

model\_file = 'llama-2-7b
-chat.q4\_K\_M.gguf',

device\_map ='auto',

torch\_dtype = torch.float16,

use\_auth\_token = True)

&#x200B;

&#x200B;


&#x200B;

&#x200B;

'''

model = AutoModelForCausalLM.from\_pretrained('meta-llama/Llama-2-7b-chat-hf',

device\_map =
'auto',

torch\_dtype = torch.float16,

use\_auth\_token = True)

&#x200B;

&#x200B;

'''

&#x200B;

&#x200B;

&#x200B;


pipe = pipeline('text-generation',

model = model,

tokenizer = tokenizer,

device\_map='auto',

max\_new\_tokens = 512
,

min\_new\_tokens = 1,

top\_k = 5) ##see it 

&#x200B;

\## In vectorstore, take top 5 closest vectors-inputs-context
s, whatever you wanna call.

&#x200B;

llm = HuggingFacePipeline(pipeline=pipe, model\_kwargs= {'temperature':0.7})

&#x
200B;

memory = ConversationBufferMemory(memory\_key='chat\_history', input\_key='question', output\_key='answer', retur
n\_messages=True)

&#x200B;

system\_template = r''' 

Given a context, use your knowledge and answer the question. Be f
lexible, and try everything to answer in the format asked by query.

 \----

{context}

\----

'''

&#x200B;

&#x200B;


user\_template = 'Question:\`\`\`{question}\`\`\`'

&#x200B;

messages = \[

SystemMessagePromptTemplate.from\_template(
system\_template),

HumanMessagePromptTemplate.from\_template(user\_template)

\]

&#x200B;

&#x200B;

qa\_prompt = Chat
PromptTemplate.from\_messages(messages)

&#x200B;

&#x200B;

&#x200B;

jsonExpert = ConversationalRetrievalChain.from\_l
lm(llm = llm, 

retriever=vectordb.as\_retriever(search\_kwargs = {'k': 1}), ## whats it

verbose = True, memory = memor
y, combine\_docs\_chain\_kwargs={'prompt': qa\_prompt},

return\_source\_documents = True

)

&#x200B;

\##retriever ret
urns 1 output object.

&#x200B;

chat\_history = \[\]

query = 'Consider the financials and progress of companies who is
 in the tech business.'

result = jsonExpert({'question': query}, {'chat\_history': chat\_history})

\#result = jsonExpe
rt({'question': query})

&#x200B;

&#x200B;

sources = result\['source\_documents'\]\[0\]

print(result\['answer'\])

pp
rint(sources)

pprint(memory)
```
---

     
 
deeplearning -  [ How to find 'custom' datasets for LLM ](https://www.reddit.com/r/deeplearning/comments/16bj3hg/how_to_find_custom_datasets_for_llm/) , 2023-09-22-0909
```
Hey folks,

I've been digging everywhere, including here, for LLMs and custom applications. So, I read many things, lear
ned from ppl here. Its time to try something. I will try implement Llama v2 - Langchain - Chroma combination. But also I
 want to upload a dataset so that I can try my model on that. 

I find some datasets big enough (for now, 2-5 gb is ok) 
however they are table-style. I want something more texty, I mean I could use 'American Stories' or 'Arxiv' however I be
lieve that they are already used by Llama to train. 

&#x200B;

Is there any suggestions or sources that you can provide
 ? Thanks!
```
---

     
