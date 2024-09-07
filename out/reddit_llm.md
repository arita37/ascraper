 
all -  [ Can you tell us what you built with Langchain? A SaaS? A startup? ](https://www.reddit.com/r/LangChain/comments/1farnur/can_you_tell_us_what_you_built_with_langchain_a/) , 2024-09-07-0911
```

```
---

     
 
all -  [ What does your LLM stack look like these days? ](https://www.reddit.com/r/LangChain/comments/1fanhgm/what_does_your_llm_stack_look_like_these_days/) , 2024-09-07-0911
```
I am starting to use more of CrewAI, DSPy, Claude sonnet, chromadb and Langtrace. 
```
---

     
 
all -  [ has anyone checked this Decomposed Automation Correction for Text-to-SQL?  ](https://www.reddit.com/r/LangChain/comments/1fan5am/has_anyone_checked_this_decomposed_automation/) , 2024-09-07-0911
```
[https://github.com/zirui-HIT/DAC/tree/main](https://github.com/zirui-HIT/DAC/tree/main)

[https://arxiv.org/pdf/2408.08
779v2](https://arxiv.org/pdf/2408.08779v2)
```
---

     
 
all -  [ Does Microsoft Ever Make Anything Easy? Azure + Langchain help ](https://www.reddit.com/r/LangChain/comments/1faknzu/does_microsoft_ever_make_anything_easy_azure/) , 2024-09-07-0911
```
I am trying to setup, a working Langchain script to chat with AI to my Azure instance. Below is what I had before in def
ining the llm.

```javascript
import { ChatOpenAI } from 'langchain/chat_models/openai'

let llm = new ChatOpenAI({
  op
enAIApiKey,
  streaming: true,
  callbacks: [
    {
      handleLLMStart: async () => {
        id = setTimeout(() => {

          chat.setMessage(-1, md(`### Sorry, the AI is taking a long time to respond.`))
          setLoading(true)
    
    }, 3000)
        log(JSON.stringify({ event: 'handleLLMStart' }))
        currentMessage = ``
        chat.addMessag
e('')
      },
      handleLLMNewToken: async token => {
        clearTimeout(id)
        setLoading(false)
        if (
!token) return
        currentMessage += token
        let htmlMessage = md(currentMessage)
        chat.setMessage(-1, 
htmlMessage)
      },
      handleLLMError: async err => {
        warn(JSON.stringify({ event: 'handleLLMError', error:
 err }))
        running = false
        await appendToLogFile(JSON.stringify({ type: 'Error', message: err.message }) +
 ',\n')
      },
      handleLLMEnd: async () => {
        running = false
        log(JSON.stringify({ event: 'handleLL
MEnd' }))
        if (currentMessage) {
          await appendToLogFile(JSON.stringify({ type: 'AI', message: currentMes
sage }) + ',\n')
        }
        currentMessage = ``
      },
    },
  ],
})
```

I know that import above is deprecat
ed, I am trying to switch to using `AzureChatOpenAI` and this is the code I have, which aligns with the new 0.2 docs

``
`javascript
import { AzureChatOpenAI } from '@langchain/openai';

let llm = new AzureChatOpenAI({
  azureOpenAIApiKey: p
rocess.env.AZURE_OPENAI_API_KEY,
  azureOpenAIApiInstanceName: process.env.AZURE_OPENAI_API_INSTANCE_NAME,
  azureOpenAI
ApiDeploymentName: process.env.AZURE_OPENAI_API_DEPLOYMENT_NAME,
  azureOpenAIApiVersion: process.env.AZURE_OPENAI_API_V
ERSION,
  callbacks: [
    {
      handleLLMStart: async () => {
        id = setTimeout(() => {
          chat.setMessa
ge(-1, md(`### Sorry, the AI is taking a long time to respond.`))
          setLoading(true)
        }, 3000)
        lo
g(JSON.stringify({ event: 'handleLLMStart' }))
        currentMessage = ``
        chat.addMessage('')
      },
      ha
ndleLLMNewToken: async token => {
        clearTimeout(id)
        setLoading(false)
        if (!token) return
        
currentMessage += token
        let htmlMessage = md(currentMessage)
        chat.setMessage(-1, htmlMessage)
      },
 
     handleLLMError: async err => {
        warn(JSON.stringify({ event: 'handleLLMError', error: err }))
        runnin
g = false
        await appendToLogFile(JSON.stringify({ type: 'Error', message: err.message }) + ',\n')
      },
      
handleLLMEnd: async () => {
        running = false
        log(JSON.stringify({ event: 'handleLLMEnd' }))
        if (c
urrentMessage) {
          await appendToLogFile(JSON.stringify({ type: 'AI', message: currentMessage }) + ',\n')
      
  }
        currentMessage = ``
      },
    },
  ],
})
```

I get a 404 error, which is not very helpful. I know for a 
fact my values are correct becuase I have a non langchain script that uses `const { AzureOpenAI } = require('openai');` 
and it works fine.

Also, I have noticed there might be an API Version that is for a particular deployment on Azure, as 
well as an API version for the entire instance. 

If anyone can provide insight on setting up Azure with Langchain and N
odeJS, I would be very greatful.

Thanks and happy coding.
```
---

     
 
all -  [ Free Generative AI Web App Course: Learn LangChain, NLP & Streamlit ](https://www.reddit.com/r/myHeadstarter/comments/1fak4vf/free_generative_ai_web_app_course_learn_langchain/) , 2024-09-07-0911
```
Here’s the link: [Free Course](https://www.udemy.com/course/building-generative-ai-web-apps-with-streamlit-langchain/) 🚀


My team at **ViSTEM** just launched an **exciting, FREE** course to teach you how to build AI-powered web apps using *
*Streamlit** and **LangChain**! Perfect for anyone wanting to dive into generative AI and web development. Whether you'r
e a beginner with some Python knowledge or an experienced developer, this course is a game-changer. Plus, you can even e
arn a **certificate** from us at ViSTEM—just send proof of completion! 🏆

**Course Highlights:**

* **Streamlit:** Build
 dynamic web apps
* **LangChain:** Master state-of-the-art AI frameworks
* **Text Summarization with NLP**
* **arXiv API
 Setup** for research paper handling

Get hands-on experience with **real-world projects** and build your own AI-powered
 research app! 🌟
```
---

     
 
all -  [ What is optimal for Langflow: Loop or multi-api call? or Tasks? ](https://www.reddit.com/r/LangChain/comments/1faiz56/what_is_optimal_for_langflow_loop_or_multiapi/) , 2024-09-07-0911
```
I'm in the midst of a fun side project to get good MTG ruling. My stopping point is getting LangChain/LangFlow to iterat
e over a list of \[words in brackets\] in a prompt, and then take those \[words in brackets\] from the user and put each
 set into an API request. Is there an easy way to do that? 
```
---

     
 
all -  [ Claude, Projects and RAG ](https://www.reddit.com/r/LangChain/comments/1faenrt/claude_projects_and_rag/) , 2024-09-07-0911
```
My understanding is that the Projects feature of Claude Soinnet 3.5 works a little like a RAG feature.  
The documents i
n the knowledge are indexed and then the prompt is augmented by information located within the documents located in the 
knowledge.  
The difference with RAG is that the documents in knowledge are uploaded  and not retrieved as in A RAG syst
em. Is this understanding correct?
```
---

     
 
all -  [ LangGraph.js Fundamentals: Nodes, Edges, Conditional Edges, and Graphs ](https://www.reddit.com/r/LangChain/comments/1faeh4h/langgraphjs_fundamentals_nodes_edges_conditional/) , 2024-09-07-0911
```
Hey folks! I've made this intro tutorial for LangGraph.js. 

[https://www.js-craft.io/blog/langgraph-js-conditional-edge
s-graphs/](https://www.js-craft.io/blog/langgraph-js-conditional-edges-graphs/)

Any feedback is welcomed! 
```
---

     
 
all -  [ Text2SQL using HuggingFace Llama3 ](https://www.reddit.com/r/LangChain/comments/1fae122/text2sql_using_huggingface_llama3/) , 2024-09-07-0911
```
Has anyone used HuggingFace to access Llama3 for Text2SQL problems? I can get results with Gemma using HuggingFace but w
hen I load Llama3 it says it's 16GB so I can't load directly. I can't find resources for Text2SQL using HuggingFace, but
 it's available for OpenAI, Groq. Below is the code with the Gemma model. 

    load_dotenv()
    
    POSTGRESQL_HOST =
 os.getenv('POSTGRESQL_HOST')
    POSTGRESQL_USER = os.getenv('POSTGRESQL_USER')
    POSTGRESQL_PASS = os.getenv('POSTGR
ESQL_PASS')
    POSTGRESQL_DB = os.getenv('POSTGRESQL_DB')
    POSTGRESQL_URI = f'postgresql://{POSTGRESQL_USER}:{POSTGR
ESQL_PASS}@{POSTGRESQL_HOST}:5432/{POSTGRESQL_DB}'
    
    HUGGINGFACEHUB_API_TOKEN = os.getenv('HUGGINGFACEHUB_API_TOK
EN')
    
    hf = HuggingFaceEndpoint(repo_id = 'google/gemma-2b', temperature = 0.1, huggingfacehub_api_token = HUGGIN
GFACEHUB_API_TOKEN)
    
    def configure_db(db_uri):
        return SQLDatabase(create_engine(db_uri))
    
    db = c
onfigure_db(POSTGRESQL_URI)
    
    db_chain = SQLDatabaseChain.from_llm(hf, db, verbose=True)
    
    user_query = 'W
hich control governs incident response planning under NIS2?'
    response = db_chain.invoke(user_query)
    print(respon
se)
    
```
---

     
 
all -  [ LLM uses fake documents from examples as context ](https://www.reddit.com/r/LangChain/comments/1faatl2/llm_uses_fake_documents_from_examples_as_context/) , 2024-09-07-0911
```
Hello!

I have been working on an internal AI assistant for my company, and have set up a RAG pipeline.

Unfortunately, 
given the right query, the model uses the fake documents provided through examples to generate his answer, which is quit
e jarring. Is there any best practice here? A way to clearly indicate that information given as examples should not be c
onsidered?

If that makes a difference, my team has been toying with [Prompty ](https://prompty.ai/)for the prompt templ
ating, and its langchain integration, [langchain\_prompty](https://api.python.langchain.com/en/latest/prompty_api_refere
nce.html). I'll gladly switch to something else if needed.

As for why examples are needed here, I am using structured o
utput to generate the answer chunk by chunk, with each chunk associated to a list of IDs, linking to the documents used 
for this chunk. Examples have a substantial impact on how well the model follows guidelines (not naming the documents in
 the body of the answer for example).

Thanks!
```
---

     
 
all -  [ Dev partner for Medium com scraper ](https://www.reddit.com/r/LangChain/comments/1faa4dk/dev_partner_for_medium_com_scraper/) , 2024-09-07-0911
```
I'm working on developing a Medium.com scraper that collects article data (titles, subtitles, authors, dates, etc.), and
 I'm looking for someone to join me in building it quickly and efficiently. If you have experience with Python, Selenium
, BeautifulSoup, or any web scraping tools and want to collaborate on this, let's connect!I'm open to new ideas and appr
oaches to make the scraper more powerful. DM me if you're interested, and let's get this rolling!
```
---

     
 
all -  [ is Langchian production ready? ](https://www.reddit.com/r/LangChain/comments/1fa9y8l/is_langchian_production_ready/) , 2024-09-07-0911
```
I am working on a startup project and almost finished. I have used langchain. Seen somewhere on youtube that langchain a
nd llamaindex or not prod ready? is it true?
```
---

     
 
all -  [ Evaluate your RAG pipeline with Ragas, agnostic of LLM ](https://www.reddit.com/r/LangChain/comments/1fa9953/evaluate_your_rag_pipeline_with_ragas_agnostic_of/) , 2024-09-07-0911
```
Another update from RAG Me Up! We have added some rudimentary evaluation metrics using Ragas so you can now start tweaki
ng your RAG pipeline objectively. Best thing is that it doesn't matter if you use ChatGPT, Gemini, Claude, Ollama, LLaMa
 3.1 or any other LLM, they are all supported.

By the way - we also added Re2 to have the LLM re-read your question, im
proving performance.

  
[https://github.com/AI-Commandos/RAGMeUp](https://github.com/AI-Commandos/RAGMeUp)
```
---

     
 
all -  [ Live context and fact checks using RAG and whisper  ](https://www.reddit.com/r/LangChain/comments/1fa8ov2/live_context_and_fact_checks_using_rag_and_whisper/) , 2024-09-07-0911
```
I have a need for a tool that could be connected to a zoom call or similar and could in realtime pull up and summarise r
elevant information and perhaps also fact check.

E.g on a call person X says “the total cost of the project will be £65
 and take 2 years”

In realtime, something could pop up that says
 “
- the initial proposal stated the total cost would 
be £55
- in an email on 6th September Bob told Mary that the project was still within budget” etc.

And ideally it would
 be linked to the sources.

I remember seeing someone’s project for doing job interviews and I’ve seen some fact check p
rojects but can’t find these again.

Are there any repos or libraries that would get me a good chunk of the way there?


I’m assuming it will use OpenAI GPT, whisper, langchain but perhaps there is something that brings it all together?
```
---

     
 
all -  [ Do I need finetuning or a better RAG? ](https://www.reddit.com/r/LangChain/comments/1fa8ilr/do_i_need_finetuning_or_a_better_rag/) , 2024-09-07-0911
```
Hi everyone,  
I created a RAG model for question answering. My document is having too much details and many subheadings
 too. I have set my chunk size as 1024. I noticed RAG is not retrieving related context, as subheadings not having the t
opic name most of the times.

Currently thinking about finetuning by creating question answer pairs from my dataset. But
 I believe it can lead to more hallucination. I read articles saying finetuning can not be used to provide model with ne
w knowledge. Correct me if I am wrong. Else I think I need to pre process my docs better. Have anyone tried finetuning f
or question answering with custom data? Please share your experiences.
```
---

     
 
all -  [ Tavily vs. Exa for RAG with LangChain - Any Recommendations? ](https://www.reddit.com/r/Rag/comments/1fa73cn/tavily_vs_exa_for_rag_with_langchain_any/) , 2024-09-07-0911
```
I'm starting to build a RAG workflow using LangChain, and I'm at the stage where I need to pick a search tool. I'm looki
ng at Tavily and Exa, but I'm not sure which one would be the better choice.   
What are the key difference between them
?
```
---

     
 
all -  [ Langrunner Simplifies Remote Execution in Generative AI Workflows ](https://www.reddit.com/r/Langchaindev/comments/1fa6tk5/langrunner_simplifies_remote_execution_in/) , 2024-09-07-0911
```
When using Langchain and LlamaIndex to develop Generative AI applications, dealing with compute-intensive tasks (like fi
ne-tuning with GPUs) can be a hassle. To solve this, we created the **Langrunner** tool which offers an inline API that 
lets you execute specific blocks of code remotely without wrapping the entire codebase. It integrates directly into your
 existing workflow, scheduling tasks on clusters optimized with the necessary resources (AWS, GCP, Azure, or Kubernetes)
 and pulling results back into your local environment.

No more manual containerization or artifact transfers—just strea
mlined development from within your notebook!

Check it out here: [https://github.com/dkubeai/langrunner](https://github
.com/dkubeai/langrunner)
```
---

     
 
all -  [ Langrunner: Simplifying Remote Execution in Generative AI Workflows ](https://www.reddit.com/r/LLMDevs/comments/1fa6bf1/langrunner_simplifying_remote_execution_in/) , 2024-09-07-0911
```
When using LlamaIndex and Langchain to develop Generative AI applications, dealing with compute-intensive tasks (like fi
ne-tuning with GPUs) can be a hassle. Langrunner lets you easily execute code blocks remotely (on AWS, GCP, Azure, or Ku
bernetes) without the hassle of wrapping your entire codebase. Results flow right back into your local environment—no ma
nual containerization needed.

Level up your AI dev experience and check it out here: [https://github.com/dkubeai/langru
nner](https://github.com/dkubeai/langrunner)
```
---

     
 
all -  [ What is the best way to minimalize html code for llm.  ](https://www.reddit.com/r/LangChain/comments/1fa156y/what_is_the_best_way_to_minimalize_html_code_for/) , 2024-09-07-0911
```
I want to minimalize token count of a html file. I just want to make the llm see the web page with that html or any thin
g with lower token size. 
```
---

     
 
all -  [ Trabalhar com front tendo experiência apenas com back ](https://www.reddit.com/r/brdev/comments/1f9zjvc/trabalhar_com_front_tendo_experiência_apenas_com/) , 2024-09-07-0911
```
Contexto: trabalhava como dev backend jr em uma consultoria pequena da minha cidade, mas troquei de emprego como fullsta
ck jr e agora trabalho remoto pra uma empresa grande de SP que vende ERP pro Brasil todo. Esse trampo eu consegui por in
dicação, e apesar do foco da vaga ser backend com uso de IA (GenAI na AWS com Python e Langchain, mais especificamente) 
também querem que eu toque algumas coisas de Vue.js.

Acontece que eu não sei quase NADA de frontend, fiz uma coisa aqui
 ou ali na faculdade, mas não tenho nenhuma experiência profissional com HTML, CSS e Javascript. A sorte é que meu super
ior disse que não cobraria que eu soubesse essas coisas logo de cara. 

Mas queria saber de vocês se já aconteceram de t
er que tocar front sendo backend, ou vice-versa? Como foi isso? 


```
---

     
 
all -  [ LangChain's ConversationBufferMemory vs OpenAI API's message history ](https://www.reddit.com/r/LangChain/comments/1f9x1g0/langchains_conversationbuffermemory_vs_openai/) , 2024-09-07-0911
```
This is a question particularly relevant to using LangChain with OpenAI APIs. From my understanding, which might be wron
g, LangChain's ConversationBufferMemory injects the entire conversation history into each prompt being passed to the LLM
. While this doesn't lead to much of a problem with the context window, it seems needlessly expensive to call the API wi
th the entire conversation history when it already has a message history that it stores. The API charges for the number 
of tokens for each input.

Wouldn't the ConversationBufferMemory method be inefficient and expensive, or am I missing so
mething here?
```
---

     
 
all -  [ [P] Lessons from Retrieval Augmented Generation ](https://www.reddit.com/r/MachineLearning/comments/1f9tvg7/p_lessons_from_retrieval_augmented_generation/) , 2024-09-07-0911
```
I implemented Rag in my organization and just wrote a blog about what we learned here:   
[https://www.b-yond.com/post/t
ransforming-telco-troubleshooting-our-journey-building-telcogpt-with-rag](https://www.b-yond.com/post/transforming-telco
-troubleshooting-our-journey-building-telcogpt-with-rag)

Hoping it would be helpful for those in this area. Covers rag 
evaluation (ragas), sql db, langchain agents vs chains, weaviate vector db, hybrid search, reranking, and more.

Some ad
ditional insights on ranking and hybrid search here:

[https://www.linkedin.com/posts/drzohaib\_transforming-telco-troub
leshooting-our-journey-activity-7232072089837486081--Le1?utm\_source=share&utm\_medium=member\_android](https://www.link
edin.com/posts/drzohaib_transforming-telco-troubleshooting-our-journey-activity-7232072089837486081--Le1?utm_source=shar
e&utm_medium=member_android)
```
---

     
 
all -  [ How to incorporate Agents into a RAG model ](https://www.reddit.com/r/LangChain/comments/1f9t31s/how_to_incorporate_agents_into_a_rag_model/) , 2024-09-07-0911
```
I'm new to langchain, and I'm currently creating an LLM application to answer questions from custom data (here, data scr
aped from websites). When I prompt a query, the answer sometimes turns out to be, 'I could not find an answer to that fr
om the provided data.' 

I was thinking of employing agents to retrieve extra information from external websites. Basica
lly, is there any way that I can create a hybrid model that combines the strength of both my internal vector database an
d external web search through agents? If so, please guide me on how to do so. I would appreciate it if you share require
d resources as well!
```
---

     
 
all -  [ Best way to add Rewoo (Planner arch) to a chat flow in Langgraph? ](https://www.reddit.com/r/LangChain/comments/1f9rqp8/best_way_to_add_rewoo_planner_arch_to_a_chat_flow/) , 2024-09-07-0911
```
Hey everyone,

I started using a graph based on *supervisor architecture* to build a conversational agent. I had better 
results using a graph based on *Router Agent*, but when dealing with more complex tasks that require multiple steps, thi
ngs haven’t worked as well as I'd hoped. So, I’m thinking about adding the Rewoo-based planner architecture (from the do
cs) into the flow.

The challenge is that in the example, the graph receives a 'Task' as input, but in a conversational 
agent, the user doesn’t always send a clear task—they just keep chatting.

Here are a couple of approaches I’m thinking 
of testing:

1. **Generate a Task from the conversation**: Take the list of messages between the user and the final AI r
esponse, and use that to write a Task that the graph can process.
2. **Feed the message history directly to the Planning
 Agent**: Instead of passing a Task, just pass the message history, and let the agent figure out the planning from that.


**Another option**: Send the message history to the planning node, but then in a parallel execution, pass a Task writt
en based on the messages directly to the solver node.

Any other ideas or suggestions?
```
---

     
 
all -  [ How perplexity handles web scraping ](https://www.reddit.com/r/LangChain/comments/1f9rpq1/how_perplexity_handles_web_scraping/) , 2024-09-07-0911
```
Hi folks,   
We recently have tried to implement some search function for open web results but one thing we found very f
rustrating is scraping time. Does any of you know or can guess how service like Perplexity or  GPT search can have such 
fast response? May I know if the speed is driven by 1) cached parsed website result or 2) underlying architecture(unlike
 current common web loader connector) or 3) simply more dedicated compute resources?   
And if possible, may I know if a
nyone can share how you improve the web searching + parsing speed in your project?  Our current speed with scraping prov
ider is just unacceptably slow... 

Thanks so much for help!
```
---

     
 
all -  [ Help! I got the hint of firing in my current job. Seeking for guidance ](https://www.reddit.com/r/LangChain/comments/1f9pxgk/help_i_got_the_hint_of_firing_in_my_current_job/) , 2024-09-07-0911
```
Help! I got the hint of firing in my current job. Seeking for guidance

Currently working in nontechnical work as a proj
ect architect junior. Finished Mtech in Data Science & due to a bad marker I ended up here. I just want to get into AI f
ield. Please share tips please. I don't know-how much time I have in this company.
```
---

     
 
all -  [ Langrunner Simplifies Remote Execution in Generative AI Workflows ](https://www.reddit.com/r/LocalLLaMA/comments/1f9pitr/langrunner_simplifies_remote_execution_in/) , 2024-09-07-0911
```
When using LlamaIndex and Langchain to develop Generative AI applications, dealing with compute-intensive tasks (like fi
ne-tuning with GPUs) can be a hassle. To solve this, we created the **Langrunner** tool which offers an inline API that 
lets you execute specific blocks of code remotely without wrapping the entire codebase. It integrates directly into your
 existing workflow, scheduling tasks on clusters optimized with the necessary resources (AWS, GCP, Azure, or Kubernetes)
 and pulling results back into your local environment.

No more manual containerization or artifact transfers—just strea
mlined development from within your notebook!

Check it out here: [https://github.com/dkubeai/langrunner](https://github
.com/dkubeai/langrunner)
```
---

     
 
all -  [ I Built an App with Lyzr Agent API That Auto-Writes & Posts Tweets! 🧠✨ Check It Out! ](https://www.reddit.com/r/LangChain/comments/1f9oep3/i_built_an_app_with_lyzr_agent_api_that/) , 2024-09-07-0911
```
[Auto Write and Post Tweets](https://reddit.com/link/1f9oep3/video/ii5kymv880nd1/player)

**Hey Reddit!**

I'm thrilled 
to share something I've been working on – an app that uses the Lyzr Agent API to automatically write and post tweets for
 you! Whether you're a social media manager, a content creator, or just someone who struggles with writer's block, this 
app takes care of everything.

**What does it do?**

* Generates AI-powered tweets based on your prompts
* Posts them di
rectly to your Twitter account
* Saves time and helps boost engagement with fresh ideas

If you're tired of coming up wi
th tweets or want to automate your posting, give it a try. Would love to hear your feedback or any features you'd like t
o see added!

#AI #Automation #Twitter #Productivity
```
---

     
 
all -  [ The propositions method for RAG - new way of data ingestion ](https://medium.com/@nirdiamant21/the-propositions-method-enhancing-information-retrieval-for-ai-systems-c5ed6e5a4d2e) , 2024-09-07-0911
```
I've just published a detailed article on Medium about the Propositions Method for AI Information Retrieval. If you're i
nterested in Natural Language Processing, information retrieval, or AI in general, I think you'll find this pretty fasci
nating.

What's the Propositions Method?
In short, it's a technique for breaking down complex information into simple, a
tomic facts. This allows AI systems to understand and retrieve information more accurately and efficiently.
In the artic
le, I cover:

- What exactly the Propositions Method is
- Why it's becoming increasingly important in AI
- How it works 
(with examples)
- The potential benefits and applications
- Some challenges and future directions

We'll soon be adding 
an implementation of the Propositions Method to our extensive collection of RAG (Retrieval-Augmented Generation) tutoria
ls. Our GitHub repository (5.5K ⭐) currently covers 25 different RAG techniques, and this will be a valuable addition. C
heck it out here: https://github.com/NirDiamant/RAG_Techniques
```
---

     
 
all -  [ Episode 0: Open Interpreter Obsidian & Convert Anything ](https://www.reddit.com/r/ToolUse/comments/1f9mr14/episode_0_open_interpreter_obsidian_convert/) , 2024-09-07-0911
```
We pay homage to Open Interpreter, where we met working together, by building a couple of very cool tools that have Open
 Interpreter at the core.

[https://www.youtube.com/watch?v=HjcPRoPfri](https://www.youtube.com/watch?v=HjcPRoPfri)

Ope
n Interpreter Obsidian Plugin - Use Open Interpreter to control your Obsidian vault!

CV - Convert anything to anything 
using the power of Open Interpreter

Friend and Open Glass merge forces

LangChain ambient AI agents UX

Next week, web 
scraping

Code  
[https://github.com/MikeBirdTech/obsidian-open-interpreter](https://github.com/MikeBirdTech/obsidian-op
en-interpreter)  
[https://github.com/tyfiero](https://www.youtube.com/redirect?event=video_description&redir_token=QUFF
LUhqbTl0WHBRUnUxcU1vMUpEZ3VKdUpsRGlvOHJvUXxBQ3Jtc0ttNF9QdGx5VHZxRmlsVjd4TUFjXy0ydS1OWXJNdlMwc3ZRR29yN2g0dUU2Z0NFU0xDNVB0
aHp5VzJMWk95NFVuNHE3U25pVnZRRmxZVUkyc2p5YlJlX0VTQzNiOFEtbG9yLV9xUUFvbzM3T3VDd09wOA&q=https%3A%2F%2Fgithub.com%2Ftyfiero&
v=HjcPRoPfri0)

[https://x.com/tooluseai](https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqb
Hh2azBHbjNhdjh2bHNHaW1YVXdSVVhQai1MZ3xBQ3Jtc0tsM0lKMmdYeXB6NUxKR0dHUlJKUmY3UFFteVBLeDZnUkdyOUpqa3BjWFhXdGFyNER6dl9IWUFEU
GlWNnMyak4yWFBXdEs1dGg3RmowNXF5RVd1dzdtUHpkUkVHQVR1RGdrYnVfTTB6bTc3V1BnTGhuaw&q=https%3A%2F%2Fx.com%2Ftooluseai&v=HjcPRo
Pfri0)  
[https://x.com/MikeBirdTech](https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbDFTT
1Jta3d1NHcwamZBSW9fRjZKMHZoSTM0UXxBQ3Jtc0tsc0E2YmlXR0xYa0FmQVFuMXJSNGg0eEF1QTNTVERiVHR6bW8za3N3UWJRcTE2RlJPS01ta285MjV0W
GZUWUpOazQ2WmpxNVNfMGpxVXN1c21aRnpESHA5ZVJfX1c1UFhDc0RDSzZHRkZmTU5GcC00OA&q=https%3A%2F%2Fx.com%2FMikeBirdTech&v=HjcPRoP
fri0)  
[https://x.com/FieroTy](https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbjdyd0Z2VFZ
TTmZ5NzE5V05WZW8xYUc0dlUyUXxBQ3Jtc0tsM2RWeWZOeEFTQzZsWTIzQkVIVHE0Yl9QNkgwVUxPSDBOYmlHOVZsQlZQV3d2VVZjM2hiZTFfZG0wdzcydFZ
ISDFNcFBTbGFzT0xTLU43ZEItQ2J4RUp6TTRGaURyaGZhTEZJbjlld0xzbnlsZlIxNA&q=https%3A%2F%2Fx.com%2FFieroTy&v=HjcPRoPfri0)

# 
```
---

     
 
all -  [ Trouble chunking mixed text documents  ](https://www.reddit.com/r/LangChain/comments/1f9mdt4/trouble_chunking_mixed_text_documents/) , 2024-09-07-0911
```
I'm working on a project where I need to translate (using llm api) long documents stored as text in a PostgreSQL databas
e. These documents contain a mix of regular text and large tables. My main challenge is to preserve the table structure 
during translation and processing, but I'm running into issues with chunking the text, as it often ruins the format of t
he tables. The tables aren’t in a standard format (markdown latex etc) but are just text which an llm can tell is struct
ured from the spacing. However I’m struggling to automate it via spacing as the rest of the doc has lots of formatting t
oo! And I can’t use an llm to chunk it as it’s too long. 

Unsure of this makes any sense!
```
---

     
 
all -  [ How do I build a Langgraph tool to create query parameters for Github user search ? ](https://www.reddit.com/r/LangChain/comments/1f9lshh/how_do_i_build_a_langgraph_tool_to_create_query/) , 2024-09-07-0911
```
Hello everyone , I'm currently learning Langgraph.   
I want to build a Github agent . This agent will take a query like
 ' I need frontend developer proficient in ReactJS , based in Bangalore and who also knows Python ' and convert it to qu
ery parameter format so that I can call Github user search api with it and get the results.   
  
You can see what I wan
t from my agent by referring to the below conversation. 

Can someone guide me about how can I build this agent ?

[http
s://chatgpt.com/share/2fd44861-3417-4fea-998f-bad18369d6f5](https://chatgpt.com/share/2fd44861-3417-4fea-998f-bad18369d6
f5)  

```
---

     
 
all -  [ I made a RAG library that helps with the boring stuff related to RAG. ](https://www.reddit.com/r/LocalLLaMA/comments/1f9ls7r/i_made_a_rag_library_that_helps_with_the_boring/) , 2024-09-07-0911
```
People who have worked on RAG-like systems know that RAG is primarily a data problem. It largely depends on your vector 
database—how you load your data, preprocess it, and chunk it. This doesn’t mean that other aspects are less important, b
ut it does make them boring, repetitive, and difficult to log. The main reason for this is that RAG involves many hyperp
arameters to choose from, including which models to use, the hyperparameters of the models themselves, and whether to ad
d different techniques such as a reranker or query reformulation.



To address this, [I created a library ](https://git
hub.com/khalilbenkhaled/yaraa)that automates the 'boring' stuff. You can create your own vector database however you lik
e, but when it comes to testing and playing with the pipeline, the library helps you get up and running as quickly as po
ssible. You can either use a YAML file and execute a Python script or use the components of the library as you wish.




For example, with the YAML approach, you edit the YAML file as shown, run a script, and voila—a user interface is at you
r fingertips, allowing you to chat with your system. Alternatively, you can modify the YAML file to specify evaluation m
etrics, and the library will perform the evaluation and return the results to you.



Under the hood, the library does n
ot use any wrapper libraries or LLM orchestration frameworks such as LangChain or LlamaIndex. During installation, you o
nly install the packages you intend to use.



[Here’s the link: YARAA. ](https://github.com/khalilbenkhaled/yaraa) Plea
se make sure to star it if you like what you see. 

Note: It is still in early development, so there aren’t many interfa
ces and evaluation metrics available yet. If you have any suggestions, please leave them in the comments or feel free to
 open an issue. 

If you want to contribute, pull requests are highly appreciated.
```
---

     
 
all -  [ Learnings from RAG ](https://www.reddit.com/r/Rag/comments/1f9j5b1/learnings_from_rag/) , 2024-09-07-0911
```
I implemented Rag in my organization and just wrote a blog about what we learned here:
https://www.b-yond.com/post/trans
forming-telco-troubleshooting-our-journey-building-telcogpt-with-rag

Hoping it would be helpful for those in this area.
 
Covers rag evaluation (ragas), sql db, langchain agents vs chains, weaviate vector db, hybrid search, reranking, and m
ore. 

Some additional insights on Hybrid search here:

https://www.linkedin.com/posts/drzohaib_transforming-telco-troub
leshooting-our-journey-activity-7232072089837486081--Le1?utm_source=share&utm_medium=member_android
```
---

     
 
all -  [ Building AI Customer Support with PII data Protection using Langchain ](https://www.reddit.com/r/agi/comments/1f9iyaf/building_ai_customer_support_with_pii_data/) , 2024-09-07-0911
```
I recently tackled a challenge that I think a lot of us face: building a chatbot that can handle customer support querie
s without compromising user privacy.

Creating a chatbot that can understand and respond to user queries while also prot
ecting Personally Identifiable Information (PII). It's a trickier balance than you might expect!

My Solution: I built a
 chatbot using LangChain with some extra security features. Here's what it can do:

* Detect PII in user input (emails, 
phone numbers, etc.)
* Block processing of sensitive data
* Provide helpful responses without exposing private info

I'v
e created a full tutorial with code examples in this Collab notebook: [https://git.new/langhchainPII](https://git.new/la
nghchainPII)

Here's a snippet of how I set it up:

`portkey_config = {`

`'after_request_hooks': [`

`{`

`'id': 'your-
config-id-here'`

`}`

`]`

`}`

`llm = ChatOpenAI(`

`base_url=PORTKEY_GATEWAY_URL,`

`model='gpt-3.5-turbo',`

`defaul
t_headers=createHeaders(`

`provider='openai',`

`api_key='Your_API_Key',`

`config=portkey_config,`

`)`

`)`

\`\`\`


1. The bot successfully blocks PII from being processed or repeated back
2. It maintains natural conversation flow while
 prioritizing data security
3. Performance impact is minimal - you can have security without sacrificing speed

You can 
run it locally or in Colab to see the PII protection in action. I would love to know your feedback
```
---

     
 
all -  [ How I Built a GPT-4 Customer Support Langchain Chatbot That Protects against PII ](https://www.reddit.com/r/OpenAIDev/comments/1f9ixfl/how_i_built_a_gpt4_customer_support_langchain/) , 2024-09-07-0911
```
Creating a chatbot that can understand and respond to user queries while also protecting Personally Identifiable Informa
tion (PII). It's a trickier balance than you might expect!

I built a chatbot using LangChain with some extra security f
eatures. Here's what it can do:

* Detect PII in user input (emails, phone numbers, etc.)
* Block processing of sensitiv
e data
* Provide helpful responses without exposing private info

I've created a full tutorial with code examples in thi
s Collab notebook: [https://git.new/langhchainPII](https://git.new/langhchainPII)

Here's a snippet of how I set it up:


`portkey_config = {`

`'after_request_hooks': [`

`{`

`'id': 'your-config-id-here'`

`}`

`]`

`}`

`llm = ChatOpenAI(
`

`base_url=PORTKEY_GATEWAY_URL,`

`model='gpt-3.5-turbo',`

`default_headers=createHeaders(`

`provider='openai',`

`a
pi_key='Your_API_Key',`

`config=portkey_config,`

`)`

`)`

\`\`\`

1. The bot successfully blocks PII from being proce
ssed or repeated back
2. It maintains natural conversation flow while prioritizing data security
3. Performance impact i
s minimal - you can have security without sacrificing speed

You can run it locally or in Colab to see the PII protectio
n in action. I would love to know your feedback

Upvote1Downvote0comments  

```
---

     
 
all -  [ Langgraph workflow and memory ](https://www.reddit.com/r/LangChain/comments/1f9ib6p/langgraph_workflow_and_memory/) , 2024-09-07-0911
```
Hi there, 

I been trying to build a multi agent system with langgraph and I have a few questions. I got my workflow wor
king with an agent supervisor hierarchy architecture. The only thing I am missing is the workflow memory design. For our
 use case we are using supabase. 

We want to create a ui interface with conversations and chat messages. 

Would you ha
ve a single workflow executing everytime a new message comes in? 

Or would you have a single workflow in a cycle. 

For
 the memory do you store and load the graph state everytime or do you save messages separate from the graph state. 

And
 finally , how do you save the schema in supabase, I don't want to use the postgres client in the docs. Is there an easy
 way to copy paste the schema for the graph state. 

what's the easiest way besides manually creating my own schema?. 
```
---

     
 
all -  [ Any good LLM libraries? ](https://www.reddit.com/r/LocalLLaMA/comments/1f9i1xc/any_good_llm_libraries/) , 2024-09-07-0911
```
I'm just wondering if there are actually any well written python packages for LLM use cases. My requirements are basical
ly:

- no spaghetti code (i.e langchain, llama index)
- no package with 1000s dependency

Please let me know if you know
 some, I mostly write everything on my own for now but if I can automate some of it, would be nice. 

```
---

     
 
all -  [ can i use a langchain Agent in a crew? ](https://www.reddit.com/r/crewai/comments/1f9hyj1/can_i_use_a_langchain_agent_in_a_crew/) , 2024-09-07-0911
```
is there a way to use this agent langchain\_experimental.agents.agent\_toolkits.python.base.create\_python\_agent

in a 
crewAI crew with other crewai Agents?
```
---

     
 
all -  [ ❓What version of LangChain do you use? ](https://www.reddit.com/r/LangChain/comments/1f9hoc0/what_version_of_langchain_do_you_use/) , 2024-09-07-0911
```


[View Poll](https://www.reddit.com/poll/1f9hoc0)
```
---

     
 
MachineLearning -  [ [P] using GPT4o with langchain/chroma for sports analysis  ](https://www.reddit.com/r/MachineLearning/comments/1enuzlp/p_using_gpt4o_with_langchainchroma_for_sports/) , 2024-09-07-0911
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

     
 
deeplearning -  [ Month of August in AI ](https://www.reddit.com/r/deeplearning/comments/1f6zfz0/month_of_august_in_ai/) , 2024-09-07-0911
```
🔍 I**nside this Issue:**

* 🤖 La*test Breakthroughs: *This month it’s all about A*gents, LangChain RAG, and LLMs evaluat
ion challenges.*
* 🌐 AI Monthly News: Discover how these stories are revolutionizing industries and impacting everyday l
ife: E*U AI Act, California’s Controversial SB1047 AI regulation act, Drama at OpenAI, and possible funding at OpenAI by
 Nvidia and Apple.*
* 📚 Editor’s Special: This covers the interesting talks, lectures, and articles we came across recen
tly.

Follow me on Twitter and LinkedIn at [**RealAIGuys**](https://twitter.com/RealAIGuys) and [**AIGuysEditor**](https
://www.linkedin.com/in/vishal-rajput-999164122/) to get insight on new AI developments.

>**Please don't forget to subsc
ribe to our Newsletter:** [**https://medium.com/aiguys/newsletter**](https://medium.com/aiguys/newsletter)

# Latest Bre
akthroughs

Are Agents just simple rules? Are Agents just enhanced reasoning? The answer is yes and no. Yes, in the sens
e that agents have simple rules and can sometimes enhance reasoning capabilities compared to a single prompt. But No in 
the sense that agents can have a much more diverse functionality like using specific tools, summarizing, or even followi
ng a particular style. In this blog, we look into how to set up these agents in a hierarchal manner just like running a 
small team of Authors, researchers, and supervisors.

[**How To Build Hierarchical Multi-Agent Systems?**](https://mediu
m.com/aiguys/how-to-build-hierarchical-multi-agent-systems-dc26b19201d2?sk=90958e39e1a28f5030872a90f8e3f3da)

**TextGrad
**. It is a powerful framework performing automatic “differentiation” via text. **It backpropagates textual feedback pro
vided by LLMs to improve individual components of a compound AI system.** In this framework, LLMs provide rich, general,
 natural language suggestions to optimize variables in computation graphs, ranging from code snippets to molecular struc
tures. TextGrad showed effectiveness and generality across various applications, from question-answering and molecule op
timization to radiotherapy treatment planning.

[**TextGrad: Improving Prompting Using AutoGrad**](https://medium.com/ai
guys/textgrad-controlling-llm-behavior-via-text-2a82e2073d10?sk=3633a9aa63b884c97469bce659265921)

The addition of RAG t
o LLMs was an excellent idea. It helped the LLMs to become more specific and individualized. Adding new components to an
y system leads to more interactions and its own sets of problems. Adding RAG to LLMs leads to several problems such as h
ow to retrieve the best content, what type of prompt to write, and many more.

In this blog, we are going to combine the
 **LangChain RAG with DSPy**. We deep dive into how to evaluate the RAG pipeline quantitatively using **RAGAs** and how 
to create a system where instead of manually tweaking prompts, we let the system figure out the best prompt.

[**How To 
Build LangChain RAG With DSPy?**](https://medium.com/aiguys/how-to-build-langchain-rag-with-dspy-ce9154fbafaa?sk=b41d104
05f84c767cf9cd6a58d1ebac0)

As the field of natural language processing (NLP) advances, the evaluation of large language
 models (LLMs) like GPT-4 becomes increasingly important and complex. Traditional metrics such as accuracy are often ina
dequate for assessing these models’ performance because they fail to capture the nuances of human language. In this arti
cle, we will explore why evaluating LLMs is challenging and discuss effective methods like BLEU and ROUGE for a more com
prehensive evaluation.

[**The Challenges of Evaluating Large Language Models**](https://medium.com/aiguys/the-challenge
s-of-evaluating-large-language-models-ec2eb834a349)

# AI Monthly News

# AI Act enters into force

On 1 August 2024, th
e European Artificial Intelligence Act (AI Act) enters into force. The Act aims to foster responsible artificial intelli
gence development and deployment in the EU. The AI Act introduces a uniform framework across all EU countries, based on 
a forward-looking definition of AI and a risk-based approach:

* **Minimal risk:** most AI systems such as spam filters 
and AI-enabled video games face no obligation under the AI Act, but companies can voluntarily adopt additional codes of 
conduct.
* **Specific transparency risk:** systems like chatbots must clearly inform users that they are interacting wit
h a machine, while certain AI-generated content must be labelled as such.
* **High risk:** high-risk AI systems such as 
AI-based medical software or AI systems used for recruitment must comply with strict requirements, including risk-mitiga
tion systems, high-quality of data sets, clear user information, human oversight, etc.
* **Unacceptable risk:** for exam
ple, AI systems that allow “social scoring” by governments or companies are considered a clear threat to people’s fundam
ental rights and are therefore banned.

**EU announcement:** [**Click here**](https://commission.europa.eu/news/ai-act-e
nters-force-2024-08-01_en)

https://preview.redd.it/nwyzfzgm4cmd1.png?width=828&format=png&auto=webp&s=c873db37ca0dadd5b
510bea70ac9f633b96aaea4

# California AI bill SB-1047 sparks fierce debate, Senator likens it to ‘Jets vs. Sharks’ feud


**Key Aspects of SB-1047:**

* Regulation Scope: Targets “frontier” AI models, defined by their immense computational t
raining requirements (over 10²⁶ operations) or significant financial investment (>$100 million).
* Compliance Requiremen
ts: Developers must implement safety protocols, including the ability to immediately shut down, cybersecurity measures, 
and risk assessments, before model deployment.
* Whistleblower Protections: Encourages reporting of non-compliance or ri
sks by offering protection against retaliation.
* Safety Incident Reporting: Mandates reporting AI safety incidents with
in 72 hours to a newly established Frontier Model Division.
* Certification: Developers need to certify compliance, pote
ntially under penalty of perjury in earlier drafts, though amendments might have altered this.

**Pros:**

* Safety Firs
t: Prioritizes the prevention of catastrophic harms by enforcing rigorous safety standards, potentially safeguarding aga
inst AI misuse or malfunction.
* Incentivizes Responsible Development: By setting high standards for AI model training, 
the company encourages developers to think critically about the implications of their creations.
* Public Trust: Enhance
s public confidence in AI by ensuring transparency and accountability in the development process.

**Cons:**

* Innovati
on Stagnation: Critics argue it might stifle innovation, especially in open-source AI, due to the high costs and regulat
ory burdens of compliance.
* Ambiguity: Some definitions and requirements might be too specific or broad, leading to leg
al challenges or unintended consequences.
* Global Competitiveness: There’s concern that such regulations could push AI 
development outside California or the U.S., benefiting other nations without similar restrictions.
* Implementation Chal
lenges: The practicalities of enforcing such regulations, especially the “positive safety determination,” could be compl
ex and contentious.

**News Article:** [**Click here**](https://www.thenation.com/article/society/sb-1047-ai-big-tech-fi
ght/)

**Open Letter:** [**Click here**](https://safesecureai.org/open-letter)

https://preview.redd.it/ib96d7nk4cmd1.pn
g?width=828&format=png&auto=webp&s=0ed5913b5dae72e203c8592393e469d9130ed689

# MORE OpenAI drama

OpenAI co-founder John
 Schulman has left the company to join rival AI startup Anthropic, while OpenAI president and co-founder Greg Brockman i
s taking an extended leave until the end of the year. Schulman, who played a key role in creating the AI-powered chatbot
 platform ChatGPT and led OpenAI’s alignment science efforts, stated his move was driven by a desire to focus more on AI
 alignment and hands-on technical work. Peter Deng, a product manager who joined OpenAI last year, has also left the com
pany. With these departures, only three of OpenAI’s original 11 founders remain: CEO Sam Altman, Brockman, and Wojciech 
Zaremba, lead of language and code generation.

**News Article:** [**Click here**](https://techcrunch.com/2024/08/05/ope
nai-co-founder-leaves-for-anthropic/)

https://preview.redd.it/0vdjc18j4cmd1.png?width=828&format=png&auto=webp&s=e9de60
4c26aed3e47b50df3bdf114ef61f967080

# Apple and Nvidia may invest in OpenAI

Apple, which is planning to integrate ChatG
PT into iOS, is in talks to invest. Soon after, [*Bloomberg* also](https://www.bloomberg.com/news/articles/2024-08-29/nv
idia-has-held-discussions-about-joining-openai-s-funding-round?srnd=homepage-americas) reported that Apple is in talks b
ut added that Nvidia “has discussed” joining the funding round as well. The round is reportedly being led by Thrive Capi
tal and would value OpenAI at more than $100 billion.

**News Article:** [**Click here**](https://www.theverge.com/2024/
8/29/24231626/apple-nvidia-openai-invest-microsoft)

https://preview.redd.it/ude6jguh4cmd1.png?width=828&format=png&auto
=webp&s=3603cbca0dbb1be3e6d0efcf06c3a698428bbdd6

# Editor’s Special

* The AI Bubble: Will It Burst, and What Comes Aft
er?: [**Click here**](https://www.youtube.com/watch?v=91SK90SahHc&t=317s)
* Eric Schmidt Full Controversial Interview on
 AI Revolution (Former Google CEO): [**Click here**](https://www.youtube.com/watch?v=mKVFNg3DEng)
* AI isn’t gonna keep 
improving [**Click here**](https://www.youtube.com/watch?v=Y8Ym7hMR100)
* General Intelligence: Define it, measure it, b
uild it: [**Click here**](https://www.youtube.com/watch?v=nL9jEy99Nh0)
```
---

     
 
deeplearning -  [ Creating a project on NLP ](https://www.reddit.com/r/deeplearning/comments/1ey2e85/creating_a_project_on_nlp/) , 2024-09-07-0911
```
So me and my friend completed the ML and DL specialization by AndrewNg, and were just gonna get started on a project. We
 decided to make a academic assistant. So basically what this does is a user can upload a PDF,text file or any other sup
ported media and the can ask questions related to it's contents. The main objective being making learning quick given la
rger documents.

The pipeline we decided is pretty standard for such a project.

1. Split the text into chunks
2. Genera
te embeddings of the chunks
3. Store the chunks in a vector DB
4. Find the top K similar chunks to the query 
5. Retriev
e context and feed it into a LLM for an answer.

So I looked up for a library and framework to use and decided on langch
ain. We haven't decided on an LLM yet but want to run it locally so no OpenAI please. 

Since this is gonna be out first
 AI project confidence is low. I would really appreciate any heads up on the issues we may face, any suggestions on libr
aries,frameworks or models will be really helpful as well. 

Appreciate any resourceful comment 😊
```
---

     
 
deeplearning -  [ How To Build Your Retrieval Augmented Generation (RAG) Using Open-source Tools: LangChain, LLAMA 3,  ](https://www.reddit.com/r/deeplearning/comments/1emdotx/how_to_build_your_retrieval_augmented_generation/) , 2024-09-07-0911
```


TL;DR: RAG overcomes the limitations of LLMs by bringing in external sources of information as relevant context.  
  

At the end of the step-by-step tutorial, you will be able to give your favorite LLM (ChatGPT, LLAMA 3, Mixtral, Gemini, 
Claude, etc.) some documents, ask it a question and see it respond based on relevant context.  
  
This will be running 
locally, using open-source libraries. Zero API and tooling costs.

[Step-by-step Notebook with zero-cost RAG](https://co
decompass00.substack.com/p/build-open-source-rag-langchain-llm-llama-chroma)

*Processing img 69v6kjfj3wgd1...*


```
---

     
