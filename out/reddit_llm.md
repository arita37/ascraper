 
all -  [ [1 YoE, Data Science Co-op, Data Scientist, United States] ](https://www.reddit.com/r/resumes/comments/1ey4bpi/1_yoe_data_science_coop_data_scientist_united/) , 2024-08-22-0911
```
I've been applying to entry-level data science positions but haven't received any callbacks. My only professional experi
ence in the field is from a co-op, and I’m unsure if my resume highlights the right projects. Some job postings ask for 
GenAI, LLM, or deep learning experience, while others emphasize data engineering skills. I'm confused about what to incl
ude on my resume to get noticed by hiring managers. Any advice on improving my resume or strategy would be greatly appre
ciated! Please tell me everything wrong with my resume

https://preview.redd.it/jugj7bstp3kd1.png?width=977&format=png&a
uto=webp&s=384a381edbb0562c485b61d5c6bd7d1a3ea5f0c6


```
---

     
 
all -  [ Advice Needed: Struggling with Entry-Level Data Science Resume and Job Applications ](https://www.reddit.com/r/learnmachinelearning/comments/1ey3yp0/advice_needed_struggling_with_entrylevel_data/) , 2024-08-22-0911
```
've been applying to entry-level data science positions but haven't received any callbacks. My only professional experie
nce in the field is from a co-op, and I’m unsure if my resume highlights the right projects. Some job postings ask for G
enAI, LLM, or deep learning experience, while others emphasize data engineering skills. I'm confused about what to inclu
de on my resume to get noticed by hiring managers. Any advice on improving my resume or strategy would be greatly apprec
iated!

https://preview.redd.it/vttp9f1vm3kd1.png?width=977&format=png&auto=webp&s=69e4f610f1a4f14e20668ee65025b9c59a31a
42c


```
---

     
 
all -  [ Creating a project on NLP ](https://www.reddit.com/r/deeplearning/comments/1ey2e85/creating_a_project_on_nlp/) , 2024-08-22-0911
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

     
 
all -  [ Human in the Loop for Autonomous Agents ](https://www.reddit.com/r/LangChain/comments/1ey1qia/human_in_the_loop_for_autonomous_agents/) , 2024-08-22-0911
```


I found myself building a bunch of LLM-backed features that needed to use tool calling, and some of those tools involv
ed doing things that were somewhat high stakes - communicating on my behalf or modifying shared / production data. one e
xample - I wanted to replace a marketing website with a chatbot + vector DB loaded with the previous content, docs, and 
blog posts.

Between hallucinations, missing knowledge base info, and the LLM generally writing like an psuedo-intellect
ual high schooler, I realized I couldn't trust it to communicate unsupervised with my website visitors. I needed a way t
o improve the percent of high-quality responses, and do it this at scale.

I wired up a prototype that would

1. consult
 me in slack before sending any response down to a website visitor
2. incorporate my feedback into the knowledge base, a
nd
3. reformulate answers until I approved the message
4. send it to the visitor

That prototype evolved into what is no
w HumanLayer [https://github.com/humanlayer/humanlayer#why-humanlayer](https://github.com/humanlayer/humanlayer#why-huma
nlayer)

  
Update - want to acknowledge this is similar to some of the stuff u/tisi3000 has posted as well!
```
---

     
 
all -  [ * Possibly noob post, I need help or a reference to some article to write the appropriate data for a ](https://www.reddit.com/r/LangChain/comments/1exyxkf/possibly_noob_post_i_need_help_or_a_reference_to/) , 2024-08-22-0911
```
Am attempting to use the langchain/StructuredOutputParser to generate json from the openai response, this is the output 
i am looking for...  


    // example
    {
        'ratings': [
            {
                'num': 1,
              
  'title': 'Customer Engagement',
                'score': 8,
                'total': 10,
                'comment': 'G
ood customer engagement'
            },
            {
                'num': 2,
                'title': 'Product Knowle
dge',
                'score': 9,
                'total': 10,
                'comment': 'Excellent product knowledge'

            },
            {
                'num': 3,
                'title': 'Problem Solving',
                'scor
e': 7,
                'total': 10,
                'comment': 'Needs improvement in problem solving'
            }
    
    ],
        'total_obtained': 24,
        'total_score_available': 30
    }

I can't find a proper explanation of the
 docs to help me. Do you have any ideas?  this is my current schema that does not produce the result...😔

response\_sche
mas = \[  
ResponseSchema(  
name='rating',  
description='Individual rating item',  
fields=\[  
{'name': 'num', 'type'
: 'int'},  
{'name': 'title', 'type': 'str'},  
{'name': 'score', 'type': 'int'},  
{'name': 'total', 'type': 'int'},  

{'name': 'comment', 'type': 'str'},  
\]  
), ResponseSchema(  
name='ratings\_response',  
description='Ratings respons
e',  
fields=\[  
{'name': 'ratings', 'type': 'Dict\[str, Rating\]'},  
{'name': 'total\_obtained', 'type': 'int'},  
{'
name': 'total\_score\_available', 'type': 'int'},  
\]  
)\]
```
---

     
 
all -  [ Getting a structured tavily response ](https://www.reddit.com/r/LangChain/comments/1exwujh/getting_a_structured_tavily_response/) , 2024-08-22-0911
```
I've tried different things such as binding TavilySearchResults and my own Pydantic Model as llm tools but I never seem 
to get reliable results. Does anyone have an idea on how to achieve a structured output from using Tavily as a tool? 

F
or example: I'm using Tavily to find the best restaurant in Boston. I'd like to get certain information about that resta
urant as a structured response (e.g. 'location': 'example street', 'opening hours:' 'mo-fr'...).

I also tried using the
 TavilySearchAPIRetriever but without success.
```
---

     
 
all -  [ Suggestions needed in building AI part of a SAAS platform  ](https://www.reddit.com/r/developersIndia/comments/1exvhjr/suggestions_needed_in_building_ai_part_of_a_saas/) , 2024-08-22-0911
```
Hey, I’m working on a platform where users can connect their Ads accounts, allowing us to retrieve and store their ad da
ta. Users can then interact with a chatbot to ask questions like 'How did my ads perform last week?' or 'What can I do t
o improve performance?' The chatbot provides answers based on the available data context.

Currently, I’m using a RAG ap
proach, where I chunk the data, store it in a vector database, and use LangChain to create the pipeline with a prompt te
mplate. However, I’m running into issues where the chatbot sometimes generates incorrect responses, and I’m also encount
ering token limit errors.

I’m looking for alternative methods to address these problems and would really appreciate you
r insights and feedback on this.
```
---

     
 
all -  [ Developed a New Project for Extracting structured data from unstructured text Using Azure AI and Ope ](https://www.reddit.com/r/LangChain/comments/1exuop7/developed_a_new_project_for_extracting_structured/) , 2024-08-22-0911
```
Hey everyone!

I've developed a new project that uses Azure AI Document Intelligence and Azure OpenAI to extract structu
red data from all kinds of documents—PDFs, Word files, images, and more. For example, let’s say you want to extract some
 pre-defined information from a utility bill in a structured format.

Here's how it works:

1. Your documents get ingest
ed by the service.
2. Azure AI Document Intelligence converts them into structured Markdown.
3. I then use Azure AI's fu
nction calling capabilities to send the Markdown to Azure OpenAI, which parses it and outputs the data in clean JSON for
mat.

The best part is, this is highly customizable to fit your specific needs. You can define your own data schemas and
 prompts, and the system will handle the rest.

This is a paid service, so if you're interested in a demo or want to lea
rn more about how I can help with your document processing needs, feel free to shoot me a DM. I'm offering this as a fre
elance service, and I'd be happy to show you how it all comes together!

```
---

     
 
all -  [ Suggestion on fresher salary for SDE mostly working in LLM/RAG fullstack application ](https://www.reddit.com/r/developersIndia/comments/1exu0i5/suggestion_on_fresher_salary_for_sde_mostly/) , 2024-08-22-0911
```
from the last one month i was working in the 8 year old company as a trainee there they newly open an ai labs where i wa
s soley responsbile to work on various project that revolves around LLM/RAG fullstack application based on LLM/RAG mostl
y work with open ai langchain, llamaindex
so today my training period is completed and they are going to offer me full t
ime role there so on the upcoming days i had a salary discussion with my company director as i am directly working with 
him 

Wanted to know about what was the salary i should expect from them for this role

and what was the starting salary
 for this role 


```
---

     
 
all -  [ Headless IDE for Coding Agents ](https://www.reddit.com/r/LocalLLaMA/comments/1extoy6/headless_ide_for_coding_agents/) , 2024-08-22-0911
```
Hi all! This post is less about models and more about tooling. But it's 100% LLM-related and can be run locally. 

After
 making several attempts to make coding agents work I noticed the same pattern: the better the tools you give to agents,
 the better outcomes they produce. So I thought what if I gave them a proper IDE except it would be headless since agent
s don’t need a UI? That’s how I came to build Hide, a headless IDE for coding agents.

Hide is built on top of existing 
tools and standards for coding like devcontainers and LSP. When given a code repo, Hide spins up a devcontainer, install
s the dependencies, and provides APIs for codebase interaction. Developers can craft custom toolkits using Hide APIs or 
use Hide's pre-built toolkits for popular frameworks like Langchain.

The project is still a work in progress but it can
 already be tried. I’m curious to hear what you think.

Documentation: [https://hide.sh/](https://hide.sh/)

GitHub: [ht
tps://github.com/artmoskvin/hide](https://github.com/artmoskvin/hide)
```
---

     
 
all -  [ Learning Path for LangChain as a Full Stack Dev with 10+ Years Experience? ](https://www.reddit.com/r/LangChain/comments/1extkyw/learning_path_for_langchain_as_a_full_stack_dev/) , 2024-08-22-0911
```
Hey folks ✌️

I’m a full stack dev with 10+ years in the game, mostly working with JavaScript/TypeScript, React, and Nod
e.js. I’m diving into LangChain and would love some guidance on the best way to learn it.

What’s the best learning path
 or resources for someone with my background? And just to be clear, a 1-hour online course or just reading the docs does
n’t count—I’m looking for something meatier! 😅

Thanks!
```
---

     
 
all -  [ llmio: A Lightweight Library for LLM I/O ](https://www.reddit.com/r/Python/comments/1exsm6z/llmio_a_lightweight_library_for_llm_io/) , 2024-08-22-0911
```
Hey everyone,

&nbsp;

I'm excited to share [llmio](https://github.com/badgeir/llmio), a lightweight Python library for 
LLM I/O. llmio makes it easy to define and use tools with large language model (LLM) APIs that are compatible with OpenA
I's API format.

&nbsp;

**What My Project Does**:

- **Easy tool definition**: Uses type annotations to parse function 
signatures and automatically adds them to the agent's capabilities.
- **Focus on what matters**: Abstracts away the API 
details so you can concentrate on your core project.
- **Lightweight**: The core library itself is less than 500 lines o
f code.
&nbsp;

**Target Audience**:
llmio is designed for developers who are working with LLM agents / applications wit
h tool capabilities,
and for people who want a quick way to set up and experiment with tools.
It is designed for product
ion use.

&nbsp;

**Comparison**:

Allthough alternatives like Langchain exists, these libraries attempt to do much more
. **llmio** is meant as a lightweight library with a clear and simple interface for adding tool capabilities to LLM agen
ts and applications.

&nbsp;

Check it out on [Github](https://github.com/badgeir/llmio), I'd love to hear your feedback
 and see what you build with it!

```
---

     
 
all -  [ How do I add chat memory to RetrievalQA chain in langchain? ](https://www.reddit.com/r/Rag/comments/1exq8lb/how_do_i_add_chat_memory_to_retrievalqa_chain_in/) , 2024-08-22-0911
```
I have tried the memory classes in langchain but they don't seem to do the job well. I know there is an option of using 
Conversational chain but my task involved a lot of vector search so that wouldn't be the best solution. I believe the in
dustry standard is use another chain to store context and rephrase the user input to include context in the question bef
ore passing it to the RetrievalQA. However, my manager wants me to store just the questions and answers of first 10 conv
ersations. I'm not sure how to do it. I was thinking - store them in a list and update it in prompt template 'history' p
laceholder as a str. Either way idk how to do it. Pls help!
```
---

     
 
all -  [ How are you doing Agent Workflows? ](https://www.reddit.com/r/LangChain/comments/1expshp/how_are_you_doing_agent_workflows/) , 2024-08-22-0911
```
Hey Friends!

I'm wondering - how are you orchestrating agent workflows? I've seen some cool tools like [hatchet.run](ht
tp://hatchet.run), but there are more AI specific ones too (+LangGraph). I'm curious what the community is up to.

What 
makes a good workflow orchestration tool?
```
---

     
 
all -  [ World's Most Comprehensive RAG Tutorials Repo (Open Source) Now Open to Contributions + Community Di ](https://github.com/NirDiamant/RAG_Techniques) , 2024-08-22-0911
```
Our open-source RAG repository is exploding! Here's why:

- 20+ cutting-edge techniques
- Detailed explanations & visual
izations
- Real-world use cases
- Active community

🌟 Contribute & Get Recognized!
Add techniques, improve docs, create 
visuals - every contributor gets credited!

 📚 Here to Learn?
Dive into our guides and notebooks. All levels welcome!

 
🔗 Get Involved:
1. Star & fork the repo
2. Contribute your expertise
3. Join our Discord (link in repo)
```
---

     
 
all -  [ Pause/Terminate Streaming Messages (LangGraph) ](https://www.reddit.com/r/LangChain/comments/1expes5/pauseterminate_streaming_messages_langgraph/) , 2024-08-22-0911
```
In ChatGPT one can press the stop button while the interface is streaming a response, to halt the remaining responses, a
nd the incomplete response is stored in history.

I have no idea if the LLM itself is actually halted, or if it just sto
ps accepting new messages from the backend.

Is there a way to do this canceling in the graph?

I use the graphs `astrea
m_events` and yield responses to the front-end via FastAPI's StreamingResponse. I imagine that to halt streaming, I can 
listen for a flag in the endpoint method, and instead of yield, I could just break or return, which would stop sending r
esponses.

However, the LLM will still be being executed. Is it possible halt execution as well?
Even more, rather than 
stop the graph altogether, is it possible to just stop that LLM node? That way, it could proceed to the other nodes I ha
ve that work on saving conversation messages, etc.
```
---

     
 
all -  [ Multi-Agent  Supervision  (OpenAI Assistants: Directly) ](https://www.reddit.com/r/LangChain/comments/1exp8nl/multiagent_supervision_openai_assistants_directly/) , 2024-08-22-0911
```
I’ve been diving into multi-agent architecture Supervision  using OpenAI Assistants, and I’ve hit a snag. While tutorial
s on supervision work great, I’m having trouble directly connecting with a specific Assistant ID  (OpenaAI ) that I want
 modify through the OpenAI dashboard.





Is anyone else facing this issue? Have you found any solutions or workarounds
? I’d love to hear your thoughts or experiences. I’m eager to get this working smoothly, so any advice would be greatly 
appreciated!



I’m looking forward to your responses!
```
---

     
 
all -  [ Elastic Expedites SecOps Tasks with LangChain ](https://quantisnow.com/i/elastic-expedites-secops-tasks-with-langchain-5667438?utm_source=reddit) , 2024-08-22-0911
```

```
---

     
 
all -  [ Using Fallbacks in LangChain.js ](https://www.reddit.com/r/LangChain/comments/1exooz7/using_fallbacks_in_langchainjs/) , 2024-08-22-0911
```
Hi folks! I've made this short article on how to use Fallbacks in LangChain.js   
[https://www.js-craft.io/blog/fallback
s-langchain-javascript/](https://www.js-craft.io/blog/fallbacks-langchain-javascript/)

I think fallbacks are a useful f
eature and can be used in many creative ways. What do you think? 
```
---

     
 
all -  [ How to develop a structured Streamlit + Langchain app ? ](https://www.reddit.com/r/LangChain/comments/1exoi03/how_to_develop_a_structured_streamlit_langchain/) , 2024-08-22-0911
```
Hello everyone , I'm a web dev currently learning AI , a beginner in Python and AI in general .

If anyone of you is fam
iliar with ReactJS or other web frameworks , you know that when building a project we structure our app into different c
omponents ( src/pages , src/modules , src/utils etc ) .

Is there any standard way of developing streamlit apps in a mod
ular way similar to how we do in ReactJS and other frameworks ?

Asking this because I'm currently developing a PDF RAG 
app . It is \~500 lines of code in a single file ( app . py file ) ... One function after another ... and the code doesn
't look good at all

I hope I'm able to convey my problem , I've asked this question in Streamlit reddit as well , repea
ting here as I use Langchain in my app extensively . Thanks in advance !
```
---

     
 
all -  [ Build up Dict throughout a chain ](https://www.reddit.com/r/LangChain/comments/1exo4gy/build_up_dict_throughout_a_chain/) , 2024-08-22-0911
```
I'm sure this is a very simple question, but I'm having more trouble than expected to get this to work. In the first ste
p of my chain I am using a document loader. I want to keep the raw results of loader.load() in a Dict like { 'docs': \[D
ocument()\] }. The results of the remaining steps of my chain would be stored in another property of the Dict. How can I
 achieve this? I gather that RunnablePassthrough is required I'm not getting anywhere with it.
```
---

     
 
all -  [ Transform Langchain toolkit into Openai Tools format ](https://www.reddit.com/r/LangChain/comments/1exnmmn/transform_langchain_toolkit_into_openai_tools/) , 2024-08-22-0911
```
I want to use SQLdatabaseToolkit with openai assistant but I am unable to turn functions into json format, How can I do 
that?
```
---

     
 
all -  [ Question Answering system over SQL database ](https://www.reddit.com/r/Langchaindev/comments/1exkq9j/question_answering_system_over_sql_database/) , 2024-08-22-0911
```
I'm doing a mini project using langchain. It is a conversational chatbot for my university library. Right now, i have us
ed streamlit, and retrieval over pdf document. I'm encountering a few errors, and unable to make llm retrieve accurately
 over SQL. If anyone have expertise in this, please help. 
```
---

     
 
all -  [ Finetuning model response with system prompt ](https://www.reddit.com/r/LocalLLaMA/comments/1exiyss/finetuning_model_response_with_system_prompt/) , 2024-08-22-0911
```
I recently finetuned a T5-SMALL model for my usecase. It is simple and working based on my provided dataset. But, i want
 to response to be dynamic somehow similar to my dataset. 

For, that i tried to implement langchain with system prompt.
 But whenever i use system prompt with my model, the response focuses more on the system prompt rather than my own datas
et. 

Eg:

System\_prompt : prompt\_template = PromptTemplate(  
input\_variables=\['input\_text'\],  
template='{input\
_text} | You are an AI assistant. Provide generalized responses.'  
)

Input : Monthly sales growth

Model output : Anal
yzing monthly sales growth

System prompt integrated output : Calculating your AI skills for monthly sales growth
```
---

     
 
all -  [ Finetuning response with system prompt ](https://www.reddit.com/r/LangChain/comments/1exiy4a/finetuning_response_with_system_prompt/) , 2024-08-22-0911
```
I recently finetuned a T5-SMALL model for my usecase. It is simple and working based on my provided dataset. But, i want
 to response to be dynamic somehow similar to my dataset. 

For, that i tried to implement langchain with system prompt.
 But whenever i use system prompt with my model, the response focuses more on the system prompt rather than my own datas
et. 

Eg:

System\_prompt : prompt\_template = PromptTemplate(input\_variables=\['input\_text'\],    template='{input\
_text} | You are an AI assistant. Provide generalized responses.')

Input : Monthly sales growth

Model output : Analyz
ing monthly sales growth

System prompt integrated output : Calculating your AI skills for monthly sales growth
```
---

     
 
all -  [ Can function calling in llms can be used with all models? ](https://www.reddit.com/r/LangChain/comments/1exiow2/can_function_calling_in_llms_can_be_used_with_all/) , 2024-08-22-0911
```
I already created a RAG pipeline using ollama model. I want my model to generate csv file if asked by user on data it re
trieved. So, thought of using function calling. Currently I am using phi. Should I use specific model for function calli
ng? I saw there is a mistral 7B finetuned for function calling available in ollama. Should I use such finetuned models? 
If anyone have some idea or worked on similar feature please let me know.
```
---

     
 
all -  [ is this any method/way to add an additional key and value in existing metadatas generated by pgvecto ](https://www.reddit.com/r/LangChain/comments/1exifwn/is_this_any_methodway_to_add_an_additional_key/) , 2024-08-22-0911
```
How to add additional field in metadata in pgvector while processing/storing embedding in vector database and filter doc
ument using metadata,  
currently I am getting metadata as :  
{  
'page': 2,  
'Title': 'Code of Conduct Policy',  
'so
urce': '/home/temp/CustomBot/media/[dkgagavza@gmail.comknnjjnnnnnnnnnnn](mailto:dkgagavza@gmail.comknnjjnnnnnnnnnnn)/Cod
e of Conduct Policy.pdf',  
'Creator': 'Pages',  
'ModDate': 'D:20230119063429Z00'00'',  
'Producer': 'macOS Version 11.
6 (Build 20G165) Quartz PDFContext',  
'file\_path': '/home/temp/CustomBot/media/[dkagvagzaz@gmail.comknnjjnnnnnnnnnnn](
mailto:dkagvagzaz@gmail.comknnjjnnnnnnnnnnn)/Code of Conduct Policy.pdf',  
'total\_pages': 16,  
'CreationDate': 'D:202
30119063429Z00'00''  
}
```
---

     
 
all -  [ In Small-to-Big chunking, what are the optimal sizes of the small and big chunks? What are some best ](https://www.reddit.com/r/LangChain/comments/1exgj12/in_smalltobig_chunking_what_are_the_optimal_sizes/) , 2024-08-22-0911
```
[This](https://arxiv.org/pdf/2407.01219) best practices survey mentions that small-to-big chunking is the best strategy.


It mentions the general best chunk size is around 256-512.

What in this case, what should be the small and big chunk 
size? How to break in the best way? 

  
Also, if I use HyDE for hypothetical document to retrieve from, what size shoul
d that be? Similar to the small chunk, or the big chunk? Or even larger?
```
---

     
 
all -  [ Code generative ai ](https://www.reddit.com/r/LangChain/comments/1exg4gu/code_generative_ai/) , 2024-08-22-0911
```
How are LLMs trained to generate codes based on users input?
```
---

     
 
all -  [ Project Summary: Exploring the Power of Generative AI in Healthcare ](https://www.reddit.com/r/LangChain/comments/1ex8my8/project_summary_exploring_the_power_of_generative/) , 2024-08-22-0911
```
Hey all 🤖

I wanted to share this project I've been working on with the LangChain community. It was very exploratory and
 I got a change to work from figuring out system prompts and how to use the AgentExecutor to being able to utilize LangG
raph to take my project to the next level.

Here's a summary of the tech used:

* LangChain **:** At the time, OpenAI’s 
Python package was in early development. LangChain, with its large and active developer community, was a natural choice.

* **LangGraph:** Already embedded in the LangChain ecosystem, LangGraph was a logical extension.
* **AzureOpenAI:** Whi
le I started with OpenAI, I found Azure to be more cost-effective, though it required more manual setup.
* **Spoonacular
 API:** A free, albeit limited, recipe API.
* Streamlit **UI:** Chosen for its speed and ease in creating a user interfa
ce.

  
  
I'm too lazy to rewrite the article for reddit, but here's a link to the post on LinkedIn. I think its still 
readable even if you don't have LinkedIn but let me know if its not.

 Also welcome all feedback I'm learning and growin
g, as we all are! 

[https://www.linkedin.com/pulse/exploring-power-generative-ai-healthcare-lyn-scott-jr--8ms6c/](https
://www.linkedin.com/pulse/exploring-power-generative-ai-healthcare-lyn-scott-jr--8ms6c/)
```
---

     
 
all -  [ Many chunks with small content Vs contextualCompressionRetriever ](https://www.reddit.com/r/LangChain/comments/1ex7zaq/many_chunks_with_small_content_vs/) , 2024-08-22-0911
```

I've been thinking about the use of context compression in retrieval systems. Why would anyone prefer compressing conte
xt (potentially losing information) instead of just using smaller, more granular chunks of data? In theory, breaking inf
ormation into smaller pieces should help maintain fidelity and accuracy, right?

```
---

     
 
all -  [ Simple Agentic RAG for multi vector store application ](https://www.reddit.com/r/LangChain/comments/1ex1o0b/simple_agentic_rag_for_multi_vector_store/) , 2024-08-22-0911
```
Hello everyone,

Just finished a post on how to create a simple Agentic RAG that choose which vector stores to use. This
 is actually a good introduction to LangGraph.

Here's the link:  [link](https://www.metadocs.co/2024/08/20/simple-agent
ic-rag-for-multi-vector-stores-with-langchain-and-langgraph/).

Have a nice read!
```
---

     
 
all -  [ Check result of structured data with a tool calling to create the output (any insights?) ](https://www.reddit.com/r/LangChain/comments/1ex0kde/check_result_of_structured_data_with_a_tool/) , 2024-08-22-0911
```
I'd like to gather some data from the user input, let's say, height, weight and age.

I'm able to do that using:  
Where
 UserData is a pydantic class



    runnable = prompt | llm.with_structured_output(schema=UserData)
    result_data = r
unnable.invoke('I am 165 cm tall')



From there I can get: `height=165`

How can I add a function/tool call to the mix 
to check if I have 3 props? (height, weight and age)

The idea is for the user to chat with the bot in a 'normal' conver
sation, and whenever it flags the 3 props are gathered, it can return a calculation. On each interaction, it checks if a
ny prop is in the message; if so, adds it to the Class until it has all 3.
```
---

     
 
all -  [ Citations with Langchain RAG Agent ](https://www.reddit.com/r/LangChain/comments/1ewyfxi/citations_with_langchain_rag_agent/) , 2024-08-22-0911
```
Greetings,

I am attempting to follow this guide on creating a conversational Langchain agent.  
[https://python.langcha
in.com/v0.2/docs/tutorials/qa\_chat\_history/](https://python.langchain.com/v0.2/docs/tutorials/qa_chat_history/)

Previ
ously, my app was using the chains outlined in that guide.

  
I want to create an agent executor with the retriever as 
a tool. However, I want the agent to cite its sources from the retrieved documents.

I am struggling to implement the fu
nction-calling code to create citations with the langchain agent. This is because my program uses the llm.with\_structur
ed\_output() tool calling model. outlined in the documentation below.  
[https://python.langchain.com/v0.2/docs/how\_to/
qa\_citations/](https://python.langchain.com/v0.2/docs/how_to/qa_citations/)

I am also using the following chains.

`de
f format_docs_with_id(docs: List[Document]) -> str:`  
`formatted = [`  
`f'Source ID: {i}\nArticle Title: {doc.metadata
['title']}\nArticle Snippet: {doc.page_content}'`  
`for i, doc in enumerate(docs)`  
`]`  
`return '\n\n' + '\n\n'.join
(formatted)`

`rag_chain_from_docs = (`  
`RunnablePassthrough.assign(context=(lambda x: format_docs_with_id(x['context'
])))`  
`| prompt`  
`| structured_llm`  
`)`

`retrieve_docs = (lambda x: x['input']) | retriever`

`chain = RunnablePa
ssthrough.assign(context=retrieve_docs).assign(`  
`answer=rag_chain_from_docs`  
`)`

As far as I understand it, it is 
not possible to use the with structured output and the above LLM chains with langchain agents.

Does anyone know how to 
integrate citations with a retriver-tool-wielding langchain agent?
```
---

     
 
all -  [ create_tool_calling_agent only return tool result in json instead of a straightfoward answer ](https://www.reddit.com/r/LangChain/comments/1ewxmw5/create_tool_calling_agent_only_return_tool_result/) , 2024-08-22-0911
```
    from langchain.agents import AgentExecutor, create_tool_calling_agent
    prompt = ChatPromptTemplate.from_messages(

        [('system', 'You are a helpful Finance/Investment AI assistant.'),
            ('placeholder', '{chat_history}'
),
            ('human', '{input}'),
            ('placeholder', '{agent_scratchpad}'),]
    )
    tools = [get_income_s
tatement_tool]
    agent = create_tool_calling_agent(llm, tools, prompt)
    
    agent_executor = AgentExecutor(agent=a
gent, tools=tools, verbose=True)
    agent_executor.invoke({'input': 'what is apple's revenue on 2022? give me a short a
nswer'})from 



I built a create\_tool\_calling\_agent that has the get\_income\_statement tool, which takes in company
 ticker,start\_date, end\_date and returns corresponding income statement data. when I asked 'What is apple's revenue in
 2022? ', the agent only returned me the data from the tools in JSON format instead of a text like' Apple's revenue in 2
022 is xxxx'.( see picture) what went wrong, why can't the agent observer the tool result and return me a text with the 
answer of my question in it. Seems like the observation->rethink part of an agent is missing here

 

https://preview.re
dd.it/atshf6s61ujd1.png?width=1850&format=png&auto=webp&s=693ace0ce68cc477806beb394fca71f936bf095b

[https://smith.langc
hain.com/public/a6c6054f-47da-409e-9fdb-d30884d6b310/r](https://smith.langchain.com/public/a6c6054f-47da-409e-9fdb-d3088
4d6b310/r)

https://preview.redd.it/4egupcbb1ujd1.png?width=1097&format=png&auto=webp&s=60d49942551f76ce850452e758e13f0b
46fe4ba1


```
---

     
 
all -  [ Langsmith offline evaluators? ](https://www.reddit.com/r/LangChain/comments/1ewx37w/langsmith_offline_evaluators/) , 2024-08-22-0911
```
Hey all :)
I am wondering whether it’s possible to use offline evaluators when testing with langsmith aka models that do
 not function via API?
My concern is that i am using company data which i would rather not send over to OpenAI or any ot
her company outside of the country
Thanks 🙏🏼 
```
---

     
 
all -  [ Is this good enough to land a Django developer (remote) job ](https://i.redd.it/a8nn9d26otjd1.png) , 2024-08-22-0911
```
Hey guys I am looking for a junior Django developer role is this resume good enough to land a job ? 
```
---

     
 
all -  [ Udemy Free Courses for 20 August 2024 ](https://www.reddit.com/r/udemyfreeebies/comments/1ewu3d0/udemy_free_courses_for_20_august_2024/) , 2024-08-22-0911
```
# Udemy Free Courses for 20 August 2024

Note : Coupons might expire anytime, so enroll as soon as possible to get the c
ourses for FREE.

* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/13333/)Strategic Business Development
* [REDEEM OF
FER ](https://idownloadcoupon.com/udemy/13332/)Disruptive Thinking: Innovate and Transform Ideas
* [REDEEM OFFER ](https
://idownloadcoupon.com/udemy/13331/)Professional Relationship Building for Success
* [REDEEM OFFER ](https://idownloadco
upon.com/udemy/2534/)Linode: Web Server and Database Foundations
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/108
95/)Run Multiple Sites on an Instance: Digital Ocean & Linode
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/10065/
)Philosophy and Foundations of Artificial Intelligence (AI)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/685/)Con
figure NGINX on a Cloud Server: Digital Ocean & AWS
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/9868/)Linode: Fo
undations of Web Server Security
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/10891/)Optimizing Operations with A
I: Strategies and Applications
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/9874/)Linode: Build a Scalable Blog A
pp using PHP & MySQL DB
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/2418/)Cloud Computing Essentials: Linode, Li
nux, and LAMP Stack
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/11456/)Mastering Sales Negotiation for High-Valu
e Deals
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/11560/)HTML, CSS, React – Certification Course for Beginners

* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/11457/)Theoretical Foundations of AI in Cybersecurity
* [REDEEM OFF
ER ](https://idownloadcoupon.com/udemy/10066/)AI & Cognitive Science: Bridging Minds and Machines
* [REDEEM OFFER ](http
s://idownloadcoupon.com/udemy/10062/)Building a Sustainable Supply Chain for the Future
* Linode: Deploy Scalable React 
Web Apps on the Cloud
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/3351/)
* [REDEEM OFFER ](https://idownloadcoupo
n.com/udemy/8223/)AWS and Linode: The Ultimate Guide to Cloud Computing \[IaaS\]
* [REDEEM OFFER ](https://idownloadcoup
on.com/udemy/6215/)Linode: Build and Deploy Responsive Websites on the Cloud
* [REDEEM OFFER ](https://idownloadcoupon.c
om/udemy/11952/)Transforming Business with AI: Organization and Society
* [REDEEM OFFER ](https://idownloadcoupon.com/ud
emy/13330/)Bootstrap & jQuery – Certification Course for Beginners
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/1
3327/)Complete Bootstrap
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/13326/)Master in Business Analysis
* [REDEE
M OFFER ](https://idownloadcoupon.com/udemy/13325/)Master in Data Science, Data Analytics and Data Analysis
* [REDEEM OF
FER ](https://idownloadcoupon.com/udemy/12950/)React – Complete Developer Course with Hands-On Projects
* [REDEEM OFFER 
](https://idownloadcoupon.com/udemy/4626/)Build a Custom E-Commerce Site in React + JavaScript Basics
* [REDEEM OFFER ](
https://idownloadcoupon.com/udemy/7708/)Complete JavaScript, jQuery and React Bootcamp – Hands-On
* [REDEEM OFFER ](http
s://idownloadcoupon.com/udemy/2540/)Complete JavaScript, XML, AJAX and React Bootcamp – Hands-On
* [REDEEM OFFER ](https
://idownloadcoupon.com/udemy/10705/)Master in Systems Thinking
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/6164/
)How to make right career choices & choosing one for success
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/10741/)
Master in Talent Acquisition by Skilled Interview Taking
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/12579/)دليل
 شامل لكشف سر النجاح في البزنس؟
* Learn to Host Multiple Domains on one Virtual Server
* [REDEEM OFFER](https://idownloa
dcoupon.com/udemy/4634/)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/10726/)Master in Business Development and B
2B Sales & Marketing
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/10712/)Excellence in Interpersonal Skills (Peop
le & Social Skills)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/11246/)NGINX, Apache, SSL Encryption – Certifica
tion Course
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/12645/)Master in Product Management (IT)
* [REDEEM OFFER
 ](https://idownloadcoupon.com/udemy/10723/)How to become a Successful Software Programming Developer
* [REDEEM OFFER ](
https://idownloadcoupon.com/udemy/12609/)Master in Solution Architecture
* [REDEEM OFFER ](https://idownloadcoupon.com/u
demy/7707/)Build a Connect-4 Clone in React + JavaScript Foundations
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy
/7507/)Install NGINX, PHP, MySQL, SSL & WordPress on Ubuntu
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/10737/)M
aster in Software Architecture, Engineering and Development
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/11114/)B
uild a Simple Calculator in React JavaScript Foundations
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/10275/)Navi
gating the Crypto Universe
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/10843/)Python & Django | The Complete Dja
ngo Web Development Course
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/12643/)Master in Game Theory
* [REDEEM OF
FER ](https://idownloadcoupon.com/udemy/8625/)Ultimate Front-End Bootcamp: CSS, Bootstrap, JQ, JS, React
* [REDEEM OFFER
 ](https://idownloadcoupon.com/udemy/13324/)Master in Sales Management
* Master in Product Design
* [REDEEM OFFER](https
://idownloadcoupon.com/udemy/13323/)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/13322/)Scrum Master PSM 2 – Moc
k Tests
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/10722/)Master in Business Administration (MBA)
* [REDEEM OFF
ER ](https://idownloadcoupon.com/udemy/7224/)Essential Photoshop Course for Beginner to Advanced
* [REDEEM OFFER ](https
://idownloadcoupon.com/udemy/11158/)Master in Brand Strategy and Brand Management
* [REDEEM OFFER ](https://idownloadcou
pon.com/udemy/12152/)Graphics Design and Video Editing Course for Beginner
* [REDEEM OFFER ](https://idownloadcoupon.com
/udemy/7250/)Java Complete Course Using Visual Studio Code
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/7829/)Qui
ckBooks Online Bank Reconciliation
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/11565/)Design & Develop Unique Cu
stomer Value / Selling Proposition
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/5234/)The Beginner’s Guide to Bas
h Scripting and Automation
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/10113/)Campus Placements & Corporate Rela
tions Excellence
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/10717/)Master in Digital, Internet and Social Media
 Marketing
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/10213/)QuickBooks Desktop Bank Reconciliation
* [REDEEM O
FFER ](https://idownloadcoupon.com/udemy/11170/)Practical Fundamental Equity, Shares & Stock Analysis
* [REDEEM OFFER ](
https://idownloadcoupon.com/udemy/10721/)Master in Human Resources (HR) Management ( HRM)
* [REDEEM OFFER ](https://idow
nloadcoupon.com/udemy/7831/)Mastering QuickBooks Online 2024: A Comprehensive Guide
* Mind Power – Change Your Thought P
rocess To Change Your Life
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/7486/)
* [REDEEM OFFER ](https://idownload
coupon.com/udemy/10708/)Master Time Management for Higher Personal Productivity
* [REDEEM OFFER ](https://idownloadcoupo
n.com/udemy/7639/)Financial Accounting – Inventory Costs
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/13319/)Snow
flake Snowpark API for Python: Master Class with Project
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/13320/)\[DE
A-C01 | ARA-C01\] Snowflake Advanced Certification Prep
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/13318/)Ultim
ate Guide to Creating Presentations with PowerPoint
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/13316/)Trading e
n Gbp/Nzd – estrategia intradiaria efectiva
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/13317/)Essential Skills 
of Microsoft PowerPoint and Google Slide
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/13314/)Global Economics Pla
ybook: International Business Strategies
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/13315/)Artificial Intellige
nce Auditing, AI Tools
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/13313/)Boost Focus: Ayurvedic Concentration I
mprovement Certificate
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/13312/)Closing with confidence: techniques to
 develop your business
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/13311/)Real Estate License Exam Math
* [REDEE
M OFFER ](https://idownloadcoupon.com/udemy/13309/)Advanced Certification in Ayurveda: Master Core Principles
* [REDEEM 
OFFER ](https://idownloadcoupon.com/udemy/13306/)BMS – Building Management System Crash Course ( 2 in 1 )
* [REDEEM OFFE
R ](https://idownloadcoupon.com/udemy/13305/)IELTS Writing MASTERCLASS ( Unlock the Secrets to Band 8 )
* C, C and PHP: 
Comprehensive Programming Bootcamp
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/13307/)
* [REDEEM OFFER ](https://
idownloadcoupon.com/udemy/13308/)Advanced Ayurvedic Nutrition Certification Program – Level 1
* [REDEEM OFFER ](https://
idownloadcoupon.com/udemy/13304/)HVAC Engineering MASTER CLASS: HVAC AIR DISTRIBUTION DESIGN
* [REDEEM OFFER ](https://i
downloadcoupon.com/udemy/10276/)The Meditation Blueprint: Building Your Inner Sanctuary
* [REDEEM OFFER ](https://idownl
oadcoupon.com/udemy/12733/)Ayurvedic Daily Routine: Dinacharya Certification Course
* [REDEEM OFFER ](https://idownloadc
oupon.com/udemy/6650/)Adobe Premiere Pro CC Video Editing Course For Beginners
* [REDEEM OFFER ](https://idownloadcoupon
.com/udemy/11278/)The Beginner’s Guide to Adobe Premiere Pro: Edit Like a Pro
* [REDEEM OFFER ](https://idownloadcoupon.
com/udemy/8828/)Learn Chess in Hindi : Zero to Master Level
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/13262/)C
omplete IT Bootcamp 2025 (Part 2)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/8639/)Learn DaVinci Resolve: The C
omplete Video Editing Bootcamp
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/9923/)Natural Language Processing Cha
llenges : Exam Practice Tests
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/8726/)Learn Figma: UI/UX Design Master
class From Beginner to Pro
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/8659/)YouTube Thumbnail Design (Stunning 
Thumbnails Masterclass)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/6332/)Universidad Excel – Básico, Intermedio
 y Avanzado!
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/12355/)Find Your Ayurvedic Body Type: Diet
* [REDEEM OF
FER ](https://idownloadcoupon.com/udemy/8324/)Learn AutoCAD 2D
* Storytelling Masterclass – Business Storytelling for Le
aders
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/13084/)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/112
16/)Executive Certificate in Business Leadership
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/3596/)La fuerza int
erior para continuar: resiliencia
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/13301/)The Complete Mailchimp Emai
l Marketing Course for 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/13300/)Amazon Marketing PPC 2024 – The C
omplete Amazon Ads Course
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/13299/)Amazon FBA Course – How to Sell on 
Amazon MASTERY 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/13302/)Facebook Ads & Facebook Marketing MASTERY
 2024 | Coursenvy
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/13297/)Building a Strong Opening Repertoire
* [RED
EEM OFFER ](https://idownloadcoupon.com/udemy/13296/)Python. Estructuras de datos y algoritmos en Python
* [REDEEM OFFER
 ](https://idownloadcoupon.com/udemy/13298/)Social Media Marketing MASTERY 2024 | Ads on 10 Platforms
* [REDEEM OFFER ](
https://idownloadcoupon.com/udemy/13294/)Project Management Professional – PMP “PMBOK 6th edition”
* [REDEEM OFFER ](htt
ps://idownloadcoupon.com/udemy/13295/)Master 100 New AI Tools: The Ultimate Productivity Course
* [REDEEM OFFER ](https:
//idownloadcoupon.com/udemy/13292/)Azure Solutions Architect Certification: The Ultimate Bundle
* [REDEEM OFFER ](https:
//idownloadcoupon.com/udemy/13291/)Morning Meditation | Best Guided Meditation Under 10 Minutes
* [REDEEM OFFER ](https:
//idownloadcoupon.com/udemy/13293/)Django Masterclass : Build 9 Real World Django Projects
* [REDEEM OFFER ](https://ido
wnloadcoupon.com/udemy/12239/)Complete Generative AI Course With Langchain and Huggingface

GET MORE FREE ONLINE COURSES
 WITH CERTIFICATE – [CLICK HERE](https://idownloadcoupon.com/)
```
---

     
 
all -  [ Udemy Free Courses for 20 August 2024 ](https://www.reddit.com/r/udemyfreebies/comments/1ewu39t/udemy_free_courses_for_20_august_2024/) , 2024-08-22-0911
```
# Udemy Free Courses for 20 August 2024

Note : Coupons might expire anytime, so enroll as soon as possible to get the c
ourses for FREE.

* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/13333/)Strategic Business Development
* [REDEEM OF
FER ](https://idownloadcoupon.com/udemy/13332/)Disruptive Thinking: Innovate and Transform Ideas
* [REDEEM OFFER ](https
://idownloadcoupon.com/udemy/13331/)Professional Relationship Building for Success
* [REDEEM OFFER ](https://idownloadco
upon.com/udemy/2534/)Linode: Web Server and Database Foundations
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/108
95/)Run Multiple Sites on an Instance: Digital Ocean & Linode
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/10065/
)Philosophy and Foundations of Artificial Intelligence (AI)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/685/)Con
figure NGINX on a Cloud Server: Digital Ocean & AWS
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/9868/)Linode: Fo
undations of Web Server Security
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/10891/)Optimizing Operations with A
I: Strategies and Applications
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/9874/)Linode: Build a Scalable Blog A
pp using PHP & MySQL DB
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/2418/)Cloud Computing Essentials: Linode, Li
nux, and LAMP Stack
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/11456/)Mastering Sales Negotiation for High-Valu
e Deals
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/11560/)HTML, CSS, React – Certification Course for Beginners

* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/11457/)Theoretical Foundations of AI in Cybersecurity
* [REDEEM OFF
ER ](https://idownloadcoupon.com/udemy/10066/)AI & Cognitive Science: Bridging Minds and Machines
* [REDEEM OFFER ](http
s://idownloadcoupon.com/udemy/10062/)Building a Sustainable Supply Chain for the Future
* Linode: Deploy Scalable React 
Web Apps on the Cloud
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/3351/)
* [REDEEM OFFER ](https://idownloadcoupo
n.com/udemy/8223/)AWS and Linode: The Ultimate Guide to Cloud Computing \[IaaS\]
* [REDEEM OFFER ](https://idownloadcoup
on.com/udemy/6215/)Linode: Build and Deploy Responsive Websites on the Cloud
* [REDEEM OFFER ](https://idownloadcoupon.c
om/udemy/11952/)Transforming Business with AI: Organization and Society
* [REDEEM OFFER ](https://idownloadcoupon.com/ud
emy/13330/)Bootstrap & jQuery – Certification Course for Beginners
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/1
3327/)Complete Bootstrap
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/13326/)Master in Business Analysis
* [REDEE
M OFFER ](https://idownloadcoupon.com/udemy/13325/)Master in Data Science, Data Analytics and Data Analysis
* [REDEEM OF
FER ](https://idownloadcoupon.com/udemy/12950/)React – Complete Developer Course with Hands-On Projects
* [REDEEM OFFER 
](https://idownloadcoupon.com/udemy/4626/)Build a Custom E-Commerce Site in React + JavaScript Basics
* [REDEEM OFFER ](
https://idownloadcoupon.com/udemy/7708/)Complete JavaScript, jQuery and React Bootcamp – Hands-On
* [REDEEM OFFER ](http
s://idownloadcoupon.com/udemy/2540/)Complete JavaScript, XML, AJAX and React Bootcamp – Hands-On
* [REDEEM OFFER ](https
://idownloadcoupon.com/udemy/10705/)Master in Systems Thinking
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/6164/
)How to make right career choices & choosing one for success
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/10741/)
Master in Talent Acquisition by Skilled Interview Taking
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/12579/)دليل
 شامل لكشف سر النجاح في البزنس؟
* Learn to Host Multiple Domains on one Virtual Server
* [REDEEM OFFER](https://idownloa
dcoupon.com/udemy/4634/)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/10726/)Master in Business Development and B
2B Sales & Marketing
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/10712/)Excellence in Interpersonal Skills (Peop
le & Social Skills)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/11246/)NGINX, Apache, SSL Encryption – Certifica
tion Course
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/12645/)Master in Product Management (IT)
* [REDEEM OFFER
 ](https://idownloadcoupon.com/udemy/10723/)How to become a Successful Software Programming Developer
* [REDEEM OFFER ](
https://idownloadcoupon.com/udemy/12609/)Master in Solution Architecture
* [REDEEM OFFER ](https://idownloadcoupon.com/u
demy/7707/)Build a Connect-4 Clone in React + JavaScript Foundations
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy
/7507/)Install NGINX, PHP, MySQL, SSL & WordPress on Ubuntu
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/10737/)M
aster in Software Architecture, Engineering and Development
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/11114/)B
uild a Simple Calculator in React JavaScript Foundations
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/10275/)Navi
gating the Crypto Universe
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/10843/)Python & Django | The Complete Dja
ngo Web Development Course
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/12643/)Master in Game Theory
* [REDEEM OF
FER ](https://idownloadcoupon.com/udemy/8625/)Ultimate Front-End Bootcamp: CSS, Bootstrap, JQ, JS, React
* [REDEEM OFFER
 ](https://idownloadcoupon.com/udemy/13324/)Master in Sales Management
* Master in Product Design
* [REDEEM OFFER](https
://idownloadcoupon.com/udemy/13323/)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/13322/)Scrum Master PSM 2 – Moc
k Tests
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/10722/)Master in Business Administration (MBA)
* [REDEEM OFF
ER ](https://idownloadcoupon.com/udemy/7224/)Essential Photoshop Course for Beginner to Advanced
* [REDEEM OFFER ](https
://idownloadcoupon.com/udemy/11158/)Master in Brand Strategy and Brand Management
* [REDEEM OFFER ](https://idownloadcou
pon.com/udemy/12152/)Graphics Design and Video Editing Course for Beginner
* [REDEEM OFFER ](https://idownloadcoupon.com
/udemy/7250/)Java Complete Course Using Visual Studio Code
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/7829/)Qui
ckBooks Online Bank Reconciliation
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/11565/)Design & Develop Unique Cu
stomer Value / Selling Proposition
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/5234/)The Beginner’s Guide to Bas
h Scripting and Automation
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/10113/)Campus Placements & Corporate Rela
tions Excellence
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/10717/)Master in Digital, Internet and Social Media
 Marketing
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/10213/)QuickBooks Desktop Bank Reconciliation
* [REDEEM O
FFER ](https://idownloadcoupon.com/udemy/11170/)Practical Fundamental Equity, Shares & Stock Analysis
* [REDEEM OFFER ](
https://idownloadcoupon.com/udemy/10721/)Master in Human Resources (HR) Management ( HRM)
* [REDEEM OFFER ](https://idow
nloadcoupon.com/udemy/7831/)Mastering QuickBooks Online 2024: A Comprehensive Guide
* Mind Power – Change Your Thought P
rocess To Change Your Life
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/7486/)
* [REDEEM OFFER ](https://idownload
coupon.com/udemy/10708/)Master Time Management for Higher Personal Productivity
* [REDEEM OFFER ](https://idownloadcoupo
n.com/udemy/7639/)Financial Accounting – Inventory Costs
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/13319/)Snow
flake Snowpark API for Python: Master Class with Project
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/13320/)\[DE
A-C01 | ARA-C01\] Snowflake Advanced Certification Prep
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/13318/)Ultim
ate Guide to Creating Presentations with PowerPoint
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/13316/)Trading e
n Gbp/Nzd – estrategia intradiaria efectiva
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/13317/)Essential Skills 
of Microsoft PowerPoint and Google Slide
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/13314/)Global Economics Pla
ybook: International Business Strategies
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/13315/)Artificial Intellige
nce Auditing, AI Tools
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/13313/)Boost Focus: Ayurvedic Concentration I
mprovement Certificate
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/13312/)Closing with confidence: techniques to
 develop your business
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/13311/)Real Estate License Exam Math
* [REDEE
M OFFER ](https://idownloadcoupon.com/udemy/13309/)Advanced Certification in Ayurveda: Master Core Principles
* [REDEEM 
OFFER ](https://idownloadcoupon.com/udemy/13306/)BMS – Building Management System Crash Course ( 2 in 1 )
* [REDEEM OFFE
R ](https://idownloadcoupon.com/udemy/13305/)IELTS Writing MASTERCLASS ( Unlock the Secrets to Band 8 )
* C, C and PHP: 
Comprehensive Programming Bootcamp
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/13307/)
* [REDEEM OFFER ](https://
idownloadcoupon.com/udemy/13308/)Advanced Ayurvedic Nutrition Certification Program – Level 1
* [REDEEM OFFER ](https://
idownloadcoupon.com/udemy/13304/)HVAC Engineering MASTER CLASS: HVAC AIR DISTRIBUTION DESIGN
* [REDEEM OFFER ](https://i
downloadcoupon.com/udemy/10276/)The Meditation Blueprint: Building Your Inner Sanctuary
* [REDEEM OFFER ](https://idownl
oadcoupon.com/udemy/12733/)Ayurvedic Daily Routine: Dinacharya Certification Course
* [REDEEM OFFER ](https://idownloadc
oupon.com/udemy/6650/)Adobe Premiere Pro CC Video Editing Course For Beginners
* [REDEEM OFFER ](https://idownloadcoupon
.com/udemy/11278/)The Beginner’s Guide to Adobe Premiere Pro: Edit Like a Pro
* [REDEEM OFFER ](https://idownloadcoupon.
com/udemy/8828/)Learn Chess in Hindi : Zero to Master Level
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/13262/)C
omplete IT Bootcamp 2025 (Part 2)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/8639/)Learn DaVinci Resolve: The C
omplete Video Editing Bootcamp
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/9923/)Natural Language Processing Cha
llenges : Exam Practice Tests
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/8726/)Learn Figma: UI/UX Design Master
class From Beginner to Pro
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/8659/)YouTube Thumbnail Design (Stunning 
Thumbnails Masterclass)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/6332/)Universidad Excel – Básico, Intermedio
 y Avanzado!
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/12355/)Find Your Ayurvedic Body Type: Diet
* [REDEEM OF
FER ](https://idownloadcoupon.com/udemy/8324/)Learn AutoCAD 2D
* Storytelling Masterclass – Business Storytelling for Le
aders
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/13084/)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/112
16/)Executive Certificate in Business Leadership
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/3596/)La fuerza int
erior para continuar: resiliencia
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/13301/)The Complete Mailchimp Emai
l Marketing Course for 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/13300/)Amazon Marketing PPC 2024 – The C
omplete Amazon Ads Course
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/13299/)Amazon FBA Course – How to Sell on 
Amazon MASTERY 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/13302/)Facebook Ads & Facebook Marketing MASTERY
 2024 | Coursenvy
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/13297/)Building a Strong Opening Repertoire
* [RED
EEM OFFER ](https://idownloadcoupon.com/udemy/13296/)Python. Estructuras de datos y algoritmos en Python
* [REDEEM OFFER
 ](https://idownloadcoupon.com/udemy/13298/)Social Media Marketing MASTERY 2024 | Ads on 10 Platforms
* [REDEEM OFFER ](
https://idownloadcoupon.com/udemy/13294/)Project Management Professional – PMP “PMBOK 6th edition”
* [REDEEM OFFER ](htt
ps://idownloadcoupon.com/udemy/13295/)Master 100 New AI Tools: The Ultimate Productivity Course
* [REDEEM OFFER ](https:
//idownloadcoupon.com/udemy/13292/)Azure Solutions Architect Certification: The Ultimate Bundle
* [REDEEM OFFER ](https:
//idownloadcoupon.com/udemy/13291/)Morning Meditation | Best Guided Meditation Under 10 Minutes
* [REDEEM OFFER ](https:
//idownloadcoupon.com/udemy/13293/)Django Masterclass : Build 9 Real World Django Projects
* [REDEEM OFFER ](https://ido
wnloadcoupon.com/udemy/12239/)Complete Generative AI Course With Langchain and Huggingface

GET MORE FREE ONLINE COURSES
 WITH CERTIFICATE – [CLICK HERE](https://www.reddit.com/r/udemyfreeebies/)
```
---

     
 
all -  [ Query  ](https://www.reddit.com/r/LangChain/comments/1ewqbct/query/) , 2024-08-22-0911
```
I am working on creating embedings based on files user upload. I want to know what will be good way if I saved the files
 uploaded by user or after saving vector db should delete it? 
```
---

     
 
all -  [ RAG vs Fine-tuning? ](https://www.reddit.com/r/LangChain/comments/1ewppvh/rag_vs_finetuning/) , 2024-08-22-0911
```
My context is an excel sheet with 30k x 8 cells. I want the model to read a user entry and return a matched row from the
 context (it won't be a perfect match, I want the LLM to understand the user input and use its expertise to link the inp
ut to the most suitable match from the database). I'm more inclined towards RAG, but wanted to get some opinions. I've n
ever implemented RAG before - can I use the spreadsheet for embeddings? Or convert to JSON?
Any best practices when deal
ing with spreadsheets as context - including chunk size, overlap length, etc?🙏
```
---

     
 
all -  [ Roast my resume | Hardly getting any callbacks ~ suggestions are appreciated!! ](https://i.redd.it/isz6454rcrjd1.jpeg) , 2024-08-22-0911
```
Heyy Devs, I relocated back to India post my masters from US and I am actively looking for SDE 2 roles in India.
I haven
’t been able to get more interviews or offers. Guide me if my resume needs any changes? And what kind of roles should I 
target ? SDE 2 or .. ?

Tech stack id like to work - Python / Backend dev

PS : there is a gap visible on my resume betw
een my Bachelors and work exp, thats coz of Civil services aspirations.

Thank you !!
```
---

     
 
all -  [ Improve GraphRAG using LangGraph ](https://www.reddit.com/r/LangChain/comments/1ewmkey/improve_graphrag_using_langgraph/) , 2024-08-22-0911
```
GraphRAG is an advanced version of RAG retrieval system which uses Knowledge Graphs for retrieval. LangGraph is an exten
sion of LangChain supporting multi-agent orchestration alongside cyclic behaviour in GenAI apps. Check this tutorial on 
how to improve GraphRAG using LangGraph: https://youtu.be/DaSjS98WCWk
```
---

     
 
MachineLearning -  [ [P] using GPT4o with langchain/chroma for sports analysis  ](https://www.reddit.com/r/MachineLearning/comments/1enuzlp/p_using_gpt4o_with_langchainchroma_for_sports/) , 2024-08-22-0911
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
 ](https://www.reddit.com/r/MachineLearning/comments/1eki1fv/r_d_langchain_evaluation_with_beyondllm/) , 2024-08-22-0911
```
Hey everyone! Just came across a new feature of Beyond LLM that can evaluate Langchain RAG pipelines! It provides contex
t relevancy, answer relevancy, and groundedness. Check out the code snippet I’m sharing—perfect for testing your RAG pip
elines! For more info, be sure to check it out on GitHub [here](https://github.com/aiplanethub/beyondllm/blob/main/cookb
ook/evaluate_langchain_rag_pipeline_beyondllm.ipynb).

https://preview.redd.it/172m1y3dvsgd1.png?width=3972&format=png&a
uto=webp&s=63d5b0f41f0e46a58e7a2d5fb0d2bbc4384b3b1d


```
---

     
 
deeplearning -  [ How To Build Your Retrieval Augmented Generation (RAG) Using Open-source Tools: LangChain, LLAMA 3,  ](https://www.reddit.com/r/deeplearning/comments/1emdotx/how_to_build_your_retrieval_augmented_generation/) , 2024-08-22-0911
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

     
 
deeplearning -  [ Need help with creating CLI for 'non-programmers' (LLMs) ](https://www.reddit.com/r/deeplearning/comments/1elrfgm/need_help_with_creating_cli_for_nonprogrammers/) , 2024-08-22-0911
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

     
