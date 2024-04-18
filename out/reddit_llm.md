 
all -  [ Launched a LLM App Component Marketplace (Tools, Assistants) for use in Langchain (and no-code tools ](https://www.reddit.com/r/LangChain/comments/1c6m5gv/launched_a_llm_app_component_marketplace_tools/) , 2024-04-18-0910
```
Hi all, Worked with a friend to create a marketplace for Plugins/Tools and Assistants called theaiplugs.com. I was origi
nally a ChatGPT plugin developer (and I work in the AI/ML space fulltime). I thought there should be a place for people 
of different technical abilities to find quality, premade components that they can use in their own workflows (whether t
hey are using a Chat UI, Low-Code tools (n8n, langflow, flowise), or code (Langchain)). I also know how difficult fronte
nd/api credit management/billing/marketing is so the marketplace takes care of all of that. We launched this week and ar
e looking to onboard early sellers and would love feedback!  
Thanks, John Bralich Co-Founder @ [theaiplugs.com](http://
theaiplugs.com)
```
---

     
 
all -  [ Looking for sample PDF + sample queries + responses to test RAG ](https://www.reddit.com/r/LangChain/comments/1c6j83s/looking_for_sample_pdf_sample_queries_responses/) , 2024-04-18-0910
```
Hi, 

a quick google search didn't return me anything promising. Basically I would like to test my RAG system on a compl
ex PDF. I assume there are some sample PDFs out there or a batch of PDF documents and sample queries + matching response
s that I can run on my RAG to evaluate it quickly.

&#x200B;

Is anyone aware of something like that? I would definitely
 save me some time ;) 
```
---

     
 
all -  [ [HIRING] Seeking AI Development Expert - $15/hr ](https://www.reddit.com/r/forhire/comments/1c6j7z3/hiring_seeking_ai_development_expert_15hr/) , 2024-04-18-0910
```
We are on the lookout for an enthusiastic individual who possesses a solid understanding and expertise in AI development
, particularly with savvy AI tasks and AI tooling. The ideal candidate should have hands-on experience with LangChain an
d other contemporary AI frameworks. This opportunity is perfect for those who consider themselves somewhat of a full-sta
ck developer in the AI domain and are looking for a challenging role to apply their skills.  
Responsibilities:  
Work
 on advanced AI tasks and contribute to the development and optimization of AI tools.  
Engage with various AI framewor
ks, with a strong emphasis on LangChain, to build and maintain innovative solutions.  
Collaborate closely with our tea
m to design, develop, and refine AI-driven projects.  
Requirements:  
Proven experience in AI development, including 
a good understanding of different AI frameworks, especially LangChain.  
Strong proficiency in full-stack development a
s it pertains to AI projects.  
Ability to work independently and collaboratively in a fast-paced environment.  
A kee
n interest in staying abreast of the latest developments in AI technologies and frameworks.  
Details:  
Rate: $15 per
 hour  
Location: Remote  
Commitment: Part-time with the possibility of evolving into a full-time role based on perfo
rmance and project requirements.  
If you are passionate about AI and thrive in dynamic environments, we would love to 
hear from you. Please DM me your resume and a brief cover letter highlighting your experience with AI development and sp
ecific frameworks you have worked with.  
We look forward to embarking on this exciting journey together and achieving 
remarkable success with your expertise on our team.
```
---

     
 
all -  [ User-friendly RAG platform ](https://www.reddit.com/r/LangChain/comments/1c6hif8/userfriendly_rag_platform/) , 2024-04-18-0910
```
Hey folks

I've been exploring AI to help with the data analysis side of things and found that most of the tools require
 quite a bit of development and customization to be really useful or end-user-friendly.

Because of that, I started buil
ding something I call Raia, a user-friendly approach to using AI to perform RAG on databases and automate processes.

I'
m looking to connect with people who are open to providing feedback. My goal is to see if this is useful and help them s
olve a problem.

[I've made it available here](https://app.raia.live)

Any feedback is very much appreciated

https://pr
eview.redd.it/gw4t958f33vc1.png?width=1686&format=png&auto=webp&s=58017580d57b93ab878db3bfb0454d108d097614


```
---

     
 
all -  [ Suggestions for growth plan for a junior DS with one year experience ](https://www.reddit.com/r/datascience/comments/1c6hggs/suggestions_for_growth_plan_for_a_junior_ds_with/) , 2024-04-18-0910
```
Hi, I'm one year into my first DS job at a big German company. I want to decide in which direction I want to develop mys
elf careerwise and ask you for your opinion on that. Right now I do basic things like building ML models, big data analy
sis in pyspark, dashboards in powerbi and I also built small chatbots with streamlit, langchain and some Azure ressource
s. I know functional programming in Python but I never really learned object oriented programming, is this maybe somethi
ng I should go for?

I don't really have a senior colleague right now that could create a plan for me, it's a bit of a w
eird hierarchy there, so I'm super thankful for any input :)

Thank you!
```
---

     
 
all -  [ You know Gen AI != You know Deep Learning ](https://www.reddit.com/r/datascience/comments/1c6gdhi/you_know_gen_ai_you_know_deep_learning/) , 2024-04-18-0910
```
Hi,

I'm a student learning data science. 

I see few of my mates, making project with generative AI tools like langchai
n or open AI API etc

But this is what I think, and **I want to know if what I think is correct or not.**

Knowing how t
o use generative AI frameworks does not validate that you know deep learning or even basic machine learning.

I think bu
ilding projects with generative AI frameworks only validate that you know how to code by reading some docs.  I think any
one who knows basic programming can make an 'AI summarizer' or 'AI Chatbot' using langchain.

I don't feel that making s
uch projects can make me standout in any way for machine learning jobs.

I would rather make a basic data science projec
t which at least tries to solve some real business problem.
```
---

     
 
all -  [ Async function in Lang chain tools or agents ](https://www.reddit.com/r/LangChain/comments/1c6fnb8/async_function_in_lang_chain_tools_or_agents/) , 2024-04-18-0910
```
 

    async def summaries(query: str):
 print('query',query)
 result=support.find_most_similar_word(query,doc_names)
 i
f result['flag']==False:
 response='Sorry,no summarised content found check the document name once more'
 else:
 documen
t_name=result['documentName']
 print(document_name)
 url = 'http://localhost:8020/summary'

 jsonReq = {'name': document
_name}

 response = await requests.post(url, json=jsonReq)

 return response.text
 
 
    

 search = StructuredTool.fro
m_function(
 func=summaries,
 # coroutine= await summaries,
 name='summaries',
 description='always call this function f
or summary.useful for when you need to get summary of documents.If summary is found provide the summary else if not foun
d then say no summary found and stop.Don't bring up any ',
 coroutine=summaries,
 # coroutine= ... <- you can specify an
 async method if desired as well
            )
 

how can i call this async function in the right way . Can anone please
 help to correct this code
```
---

     
 
all -  [ Building ChatGPT from scratch, the right way ](https://blog.promptlayer.com/building-chatgpt-from-scratch-the-right-way-ef82e771886e) , 2024-04-18-0910
```

```
---

     
 
all -  [ Token sequence length ](https://www.reddit.com/r/LangChain/comments/1c6eh52/token_sequence_length/) , 2024-04-18-0910
```
I keep getting the error about token sequence length is 1024. I am not sure what it impacts! I am using Mistral-small wh
ich has 32k sequence length. Any guidance ?
```
---

     
 
all -  [ BM25 Retriever with Score Threshold ](https://www.reddit.com/r/LangChain/comments/1c6dlyu/bm25_retriever_with_score_threshold/) , 2024-04-18-0910
```
Hi,

as for my understanding with BM25 Retrieval, a score is computed. Therefore i would like to set a score threshold f
or my Langchain Ensemble Retriever with one Bm25 component. But I did not see a way to di this in Langchain.

I want to 
do this because otherwise the Bm25 is likely to find always something for generic questions and this might not be perfec
t.

Any thoughts on this?
```
---

     
 
all -  [ Self evaluating financial chatbot: Sharing code to download financial filings from SEC ](https://www.reddit.com/r/LangChain/comments/1c6cb1x/self_evaluating_financial_chatbot_sharing_code_to/) , 2024-04-18-0910
```
Hi, 

Like many in this sub, I have been using Langchain to learn and to build hobby projects, especially RAG agents wit
h self-evaluation. 

(Btw, the [RAG from scratch](https://www.youtube.com/watch?v=wd7TZ4w1mSw&list=PLfaIDFEXuae2LXbO1_PK
yVJiQ23ZztA0x&ab_channel=LangChain) Youtube series from Lance is extremely helpful!)

I am making **modest** progress to
wards a self-evaluating financial chatbot using the SEC data. Ideally, I want the chatbot to do the below but I am far f
rom completion:

* Allow you to ask questions about financial conditions, and trends across companies in the S&P 500 in 
the US.
* It uses data directly from the official financial filings of these companies with the SEC, to **avoid** **hall
ucination**
* It provides **detailed** **references** below each answer so that you can fact-check the answer if you wou
ld like
* The database has the last 5-10 years of financial filing data so you can ask the agent to reason about **trend
s** **over** **time**
* Before each answer is returned to you, there is another agent, whose job is to **critique** the 
**draft** answer by the LLM and propose how to improve it
* These suggestions and the entire context are then shared wit
h the original agent. The agent can then decide to **formulate** **different** **queries** to **retrieve** **better** **
information** from the database or simply incorporate the suggestions into the final answer
* This final answer is then,
 provided to the user.

One of the first hurdles is to get the data from the SEC. So in case this is helpful to anyone, 
[here](https://github.com/chandlernguyen/financial_agent) is my code to download different financial filings from each c
ompany from the SEC. I purposely want to download both the .txt file and the .zip file for each 10K and 10Q because I wa
nt the metadata and the actual report. Let me know what you think?

(And yes, I tried to use an already integrated finan
cial retriever with Langchain called [Kay.ai](https://Kay.ai) . It works but doesn't meet all of my needs.)

P.S: I wrot
e a much longer blog post to share my progress and challenges so far [here](https://www.chandlernguyen.com/blog/2024/04/
15/building-a-self-evaluating-financial-chatbot-a-journey-through-data-code-and-struggles/) in case you are at all inter
ested. 

&#x200B;
```
---

     
 
all -  [ Developers seem to inactive, at least in the JS repo ](https://www.reddit.com/r/LangChain/comments/1c6aquq/developers_seem_to_inactive_at_least_in_the_js/) , 2024-04-18-0910
```
Hi,

I am using langchain with typescript and I have reported a few bugs and feature requests already and none of them h
ave been answered so far.

There are even issues from January where only the useless bot answered has so far: [https://g
ithub.com/langchain-ai/langchainjs/issues/3978](https://github.com/langchain-ai/langchainjs/issues/3978)

Many people co
mplain about the documentation, but I am really worried about this problem.
```
---

     
 
all -  [ Creating a framework like langchain, but just for extraction. To later be integrated with langchain ](https://www.reddit.com/r/LangChain/comments/1c6afp1/creating_a_framework_like_langchain_but_just_for/) , 2024-04-18-0910
```
This post is a serious question that I have been contemplating for two months now, and I think it’s time to ask. Maybe t
his is not the best place to ask this question, but seems for me to be the best place, so here it is.

**Motivation:**


I have been working as a contractor for over a year in text extraction. My work involves extracting text from various so
urces, including legal documents and fintech platforms. I have observed that text extraction is just a small part of the
 bigger picture called LangChain. However, I don't think it's a major issue, just should be done in another place.

You 
can see my articles about the topic: 

[https://blog.gopenai.com/open-source-document-extraction-using-mistral-7b-llm-18
bf437ca1d2?source=your\_stories\_page-------------------------------------](https://blog.gopenai.com/open-source-documen
t-extraction-using-mistral-7b-llm-18bf437ca1d2?source=your_stories_page-------------------------------------)

[https://
medium.com/python-in-plain-english/claude-3-the-king-of-data-extraction-f06ad161aabf](https://medium.com/python-in-plain
-english/claude-3-the-king-of-data-extraction-f06ad161aabf)

This has been the repo for me to support the articles: [htt
ps://github.com/enoch3712/Open-DocLLM](https://github.com/enoch3712/Open-DocLLM)

So, i wanted to do something specific,
 maybe compared to [Parsr](https://github.com/axa-group/Parsr), that is an integration of several pieces like OCR+LLM, a
gents, and Databases, to extract data from sources. 

Here is a possible stack:Is this worth trying? Is anyone else doin
g this? Since I'm contributing daily, it could make sense.Use-cases: 

https://preview.redd.it/utwxo3whp1vc1.png?width=1
841&format=png&auto=webp&s=dd2341d76cde52b8522f9fe0e26cf2e13cca57de

1. Extract data according to a document. Classifies
 the document as “driver license”, gets the contract and extract the data. Returns a valid JSON.
2. Extract data with va
lidation. If field is null, calls a lambda/funcion
3. Give me a bunch of files, and extract“this content”. A bunch of fi
les like Excels, Read all of them, and extract the data with a specific format. Would use semantic routing, an agent to 
decide what to do. 
4. Easy loaders not only for AWS textExtract, Azure Form Recognizer, but also open source transforme
rs like docTR. 

Eventually evolving to provide open-source, fine-tuned models to help the extraction.

Thank you for yo
ur time. 
```
---

     
 
all -  [ Reader - LLM-Friendly websites ](https://www.reddit.com/r/LangChain/comments/1c691qg/reader_llmfriendly_websites/) , 2024-04-18-0910
```
I just stumbled upon this:  
[https://r.jina.ai](https://r.jina.ai)<website\_url here>

You can convert URLs to Markdown
. This format is then better understood by LLMs compared to HTML. I think it can be used for Agents or RAG with web sear
ches. I use it to generate synthetic data for a specific website.  
Example usage  
[https://r.jina.ai/https://en.wikipe
dia.org/wiki/Monkey\_Island](https://r.jina.ai/https://en.wikipedia.org/wiki/Monkey_Island)
```
---

     
 
all -  [ Include graph query into LCEL chain ](https://www.reddit.com/r/LangChain/comments/1c68ye8/include_graph_query_into_lcel_chain/) , 2024-04-18-0910
```
I am trying to build an LCEL chain. However, at the n-th step, a cypher graph query gets generated. The next step in the
 chain should be that the query gets executed and the result gets passed on to the next step. I have a Neo4jGraph object
, but I don't know how to integrate it into the chain. I thought about writing a function that gets the query, executes 
it and returns the result, but I don't know how to pass the graph to that function. Is there some element, for example a
 retriever, that I can use?
```
---

     
 
all -  [ Seeking assistance in combining two chains ](https://www.reddit.com/r/LangChain/comments/1c68juh/seeking_assistance_in_combining_two_chains/) , 2024-04-18-0910
```
Hey, guys!

I'm a newbie in LangChain and need help.

I'm working on a Next.js project for a chatbot where I'm using a R
etrievalQAChain. Now, I also want to make external API requests. For that, I'm implementing an APIChain. However, I'm st
ruggling to combine both chains to return the output as a single chain.
```
---

     
 
all -  [ Can an LLM application retrieve images(using RAG or some other technique)? ](https://www.reddit.com/r/LangChain/comments/1c66lrw/can_an_llm_application_retrieve_imagesusing_rag/) , 2024-04-18-0910
```
Im still new to Langchain and making use of it (though I am proficient enough with Python). I wanted to build a chatbot 
application where user inputs to the AI would make use of some provided image. As per my understanding, this is what RAG
 is for. However, I cant find an example where an LLM application is retreiving images passed to it. Here is the workflo
w I want to be able to implement:

\- User provides some prompt with an image. This image gets stored in the backend by 
the application. The LLM part of the application then uses this image or any previously provided images as contextual in
formation to reply to the prompt.

\- If the prompt requests for one of the images back for e.g. 'Can you go through the
 images and get back the one which is in black and white', then the application finds such an image and returns it or re
plies with a negative

Is the second part of this flow achievable using Langchain? Or would I have to do it some other w
ay?  
Note: i dont specifically want a model which can identify black and white images but basically perform some kind o
f semantic search through the images. The prompt may be 'Find all the images I provided and give back the ones with a tr
ee in it'
```
---

     
 
all -  [ Can an LLM application retrieve images? ](https://www.reddit.com/r/learnmachinelearning/comments/1c65tiw/can_an_llm_application_retrieve_images/) , 2024-04-18-0910
```
Im still new to Langchain and making use of it (though I am proficient enough with Python). I wanted to build a chatbot 
application where user inputs to the AI would make use of some provided image. As per my understanding, this is what RAG
 is for. However, I cant find an example where an LLM application is retreiving images passed to it. Here is the workflo
w I want to be able to implement:  


\- User provides some prompt with an image. This image gets stored in the backend 
by the application. The LLM part of the application then uses this image or any previously provided images as contextual
 information to reply to the prompt.

\- If the prompt requests for one of the images back for e.g. 'Can you go through 
the images and get back the one which is in black and white', then the application finds such an image and returns it or
 replies with a negative

&#x200B;

Is the second part of this flow achievable using Langchain? Or would I have to do it
 some other way?
```
---

     
 
all -  [ [SHARE COURSE] How to Build a GPT-4 Chatbot – Dan Shipper ](https://www.reddit.com/r/Skilldevelopt/comments/1c65eqq/share_course_how_to_build_a_gpt4_chatbot_dan/) , 2024-04-18-0910
```
**Source By:** [**How to Build a GPT-4 Chatbot – Dan Shipper**](https://www.creativecourse.net/how-to-build-a-gpt-4-chat
bot-dan-shipper/)

# What You’ll Learn In How to Build a GPT-4 Chatbot?

**WEEK 1** 

You will discover:

* The fundamen
tals of GPT model operation
* How to use Replit and ChatGPT for coding
* How to construct a simple chatbot

**WEEK 2**


You will discover:

* Why and how to repair basic chatbots
* How to create a chatbot enhanced with a knowledge base usin
g LllamaIndex
* The essential components of vector embeddings and databases

**WEEK 3**

You will discover:

* How to bu
ild a browser-based chatbot that can be interacted with
* How communications between clients and servers operate
* How t
o create a web-based chatbot using Flask and Pytho

**WEEK 4**

You will discover:

* How to create tool-using chatbots

* How function calling functions in OpenAI and Langchain
* Getting your bot into production

**WEEK 5**

* Demo Day: sho
w your classmates your chatbot.
* Commence on Each
```
---

     
 
all -  [ Streaming individual runnable component for LCEL ](https://www.reddit.com/r/LangChain/comments/1c64rf2/streaming_individual_runnable_component_for_lcel/) , 2024-04-18-0910
```
Hey guys,

Does anyone know how to stream the output from each of the runnable components for a LCEL implementation of a
 chain? Like what happens when you turn on verbose=true for an agent and it outputs all the steps it is taking. Or like 
how each runnables are traced in Langsmith.

I need to do this because the full chain takes 50 secs on average to run an
d this is a bad UX. Using streaming endpoint is not helpful because the final response from the chain is not alot, so I 
am not looking for the output streaming but streaming of the individual runnables in the LCEL.

Thanks

&#x200B;
```
---

     
 
all -  [ (SENIOR) Machine Learning Engineer - 100% Remote - Every Other Friday Off ](https://www.reddit.com/r/MachineLearningJobs/comments/1c64hzr/senior_machine_learning_engineer_100_remote_every/) , 2024-04-18-0910
```
Apply here: [https://grnh.se/cbc4e1997us](https://grnh.se/cbc4e1997us)

**The Role**

* Understanding of statistical, ML
 and deep learning algorithms
* Analyze errors of models and design strategies to overcome them
* Deploy, maintain, and 
upgrade ML models and pipelines
* Ambition to learn and grow into different industries with a modern tech stack
* Autono
my, adaptability and positivity (fully remote and globally distributed team)

**The Benefits**

* Every other Friday off
 (26 extra days off a year)
* LokaLabs™ incubator
* Relocation & Explore program (3 months or full relo)
* Remote and fl
exible
* Paid sick days and local holidays
* Fitness subscriptions and more

**The Required Hard Skills**

* Bachelor's 
Degree in Computer Science or related
* 2+ years of ML engineering experience
* Experience with Python, ML libraries and
 AI/ML frameworks (PyTorch, HuggingFace, TensorFlow, etc.)
* Proficient in English
* Clean criminal record

**Bonus Poin
ts for Experience with…**

* Building GenAI solutions, namely prompt engineering (e.g: Langchain), fine-tuning and servi
ng LLMs, search and embeddings, etc.
* MLOps, favorably in AWS (e.g: Sagemaker) as well as standards tools (e.g: MLFlow)

* Visualizing and manipulating big datasets
* NLP

**The Required Soft Skills**

* Curiosity—Ambition to learn and grow
 into different industries with a modern tech stack
* Autonomy and positivity—We’re a fully remote, globally distributed
 team
* Teamwork—Enjoy a collaborative approach
* Adaptability—Operate with a startup mindset and move at a startup pace


&#x200B;
```
---

     
 
all -  [ LLM book review ](https://www.reddit.com/r/learnmachinelearning/comments/1c62kzv/llm_book_review/) , 2024-04-18-0910
```
Has anyone gone through the 3 part book series on LLMs and Langchain:

  
**Mastering LangChain: Building Intelligent Ap
plications with Retrieval-Augmented Generation**  
**The SciPhi Advantage: Building High-Performance RAG Systems with Co
nfidence**   
**Building Next-Gen Conversational AI: A Python Implementation of RAG with LangChain for LLM Augmentation*
*  


There are no reviews, and I find it criminal for any publisher not to allow preview of the book before purchasing 
- it's like they encourage piracy. If anyone has any information about the quality of this series please share.
```
---

     
 
all -  [ SLM in AWS? ](https://www.reddit.com/r/LangChain/comments/1c62c2a/slm_in_aws/) , 2024-04-18-0910
```
Is there any small language models available in AWS? I was searching but mostly I found llms? We need some slm like flan
-t5 models that can be used for classification task.
```
---

     
 
all -  [ How can I make ollama build on what it just said when using it in langchain? ](https://www.reddit.com/r/ollama/comments/1c614ll/how_can_i_make_ollama_build_on_what_it_just_said/) , 2024-04-18-0910
```
I've been playing around with ollama and langchain in a python program and have it working pretty well however if I run 
multiple prompts in a row it doesn't 'remember' the previous results from the last prompt.   It's like I'm starting fres
h each time.  If I'm just running ollama directly from a prompt it remembers what I've already asked and can build it's 
responses off of that (up to a reason before it forgets)      I'm not sure what this is called or how to recreate it in 
my code.
```
---

     
 
all -  [ What are some agents which can be used in addition to the sql agent for rag on db. ](https://www.reddit.com/r/LangChain/comments/1c5vyfk/what_are_some_agents_which_can_be_used_in/) , 2024-04-18-0910
```
Hello

So I am able to connect a live postgres database and use the sql agent with open ai to a wide variety answer ques
tions about the database and generate sql queries as well. I wanted to know if there are any other useful agents for dat
abases maybe something to visualize, I used llamaindex in collab with a pandas dataframe and got very good results. Also
 would it be worthwhile to try and build your own agent. I would also want to know if anyone has tried open source model
s with tje langchain sql agent. 

Thanks
```
---

     
 
all -  [ An OSS tool for turning entire websites into LLM-ready markdown ](https://www.reddit.com/r/mlops/comments/1c5usna/an_oss_tool_for_turning_entire_websites_into/) , 2024-04-18-0910
```
While building [mendable.ai](https://mendable.ai) \- we found that feeding LLMs well-structured markdown improved accura
cy. We also found that it was hard.   


So, we released an open-source repo ([https://github.com/mendableai/firecrawl](
https://github.com/mendableai/firecrawl)) and API ([https://firecrawl.dev](https://firecrawl.dev)) that crawls and turns
 entire websites into a markdown with just a few lines of code. 

It handles

* Crawling without consistent sitemaps
* B
uilding the infra to handle running many scraping jobs
* Proxying, hosting headless browsers at scale
* Conversion to cl
ean markdown
* Caching
* Handling images, videos, and tables  


It is open source, and we also offer a free, easy-to-us
e API. It has built-in loaders for both r/llama_index and r/langchain.   


Hopefully, this is helpful. And if you've ex
perienced the problem, **consider contributing**! 🫡🔥 
```
---

     
 
all -  [ What's the most common way to do RAG these days? ](https://www.reddit.com/r/OpenAI/comments/1c5tc1n/whats_the_most_common_way_to_do_rag_these_days/) , 2024-04-18-0910
```
Hello friends!

I'm a coder. Very experienced with using GPT & Claude for LLM work, but have never dealt with more conte
nt that fits in a 128-200K context window until recently, so I have no experience with RAG.

**What're the most common &
 fastest to implement approaches?** I've used the new Assistants API and its the perfect level of easy to use, but its q
uite expensive in token use and not model-agnostic.

I see talk around LangChain and AutoGen for pipelines, Chroma and P
inecone for vector DBs...is there anything simpler? Something like the Assistants API, but more model agnostic. If not, 
what's the most common way to do this?

Thanks a ton r/OpenAI!
```
---

     
 
all -  [ what's the best way to pass dependencies into langchain tools? ](https://www.reddit.com/r/LangChain/comments/1c5slrj/whats_the_best_way_to_pass_dependencies_into/) , 2024-04-18-0910
```
Let's say I have a service I want to access inside a tool. Or I want to pass in a session ID or some session based state
 that I don't want to pass via the agent. 

I could obviously declare some things globally, but that isn't appropriate f
or everything. 

My first thought was wrapping tools in a class that contains their dependencies. I've tried different v
ariants of this, but seem to hit all kinds of issues. The documentation contains trivial use cases where we're passing b
asic types around, nothing more complex.

&#x200B;

What are people doing for tools which have more complex dependencies
? How are they injecting those into tools, in a langchain supported way, without making everything global?
```
---

     
 
all -  [ Langchain Interview. What things to prepare ](https://www.reddit.com/r/LangChain/comments/1c5r9qj/langchain_interview_what_things_to_prepare/) , 2024-04-18-0910
```
Hey Guys  
I have interview scheduled next week about Langchain. But I am not sure what will be asked? I wanted your inp
uts on what should I prepare.  


My background -  I have built multi-doc RAG. Technologies used - Langchain, Chroma, St
reamlit, [unstrctured.io](https://unstrctured.io)  


Please any help is appreciated  


Thanks

&#x200B;
```
---

     
 
all -  [ Knowledge Graph & RAG with Local LLM ](https://www.reddit.com/r/LocalLLaMA/comments/1c5o1z2/knowledge_graph_rag_with_local_llm/) , 2024-04-18-0910
```
Any insights on building a local LLM based RAG that uses a knowledge graph to query from? I read several examples from l
angchain & Llama\_index but it looks like they all need an open\_ai api call, and do not have provisions for a local llm

```
---

     
 
all -  [ Use 2 LLM, 1 for function calling and 1 for Contextual Response. ](https://www.reddit.com/r/LangChain/comments/1c5n0aw/use_2_llm_1_for_function_calling_and_1_for/) , 2024-04-18-0910
```
Hi, I am trying to develop an application that requires function calling and responding in everyday language based on th
e context of user input. I see in langchain we have [Ollama](https://js.langchain.com/docs/integrations/chat/ollama) and
 [Ollama functions](https://js.langchain.com/docs/integrations/chat/ollama_functions); I would like to use the Ollama Fu
nction first to check if the user needs to execute any function, then if not respond with regular Ollama, and if it does
, get the function data and pass it into Ollama and response usually.

How is this possible?
```
---

     
 
all -  [ Need architecture Help ](https://www.reddit.com/r/LangChain/comments/1c5mrr1/need_architecture_help/) , 2024-04-18-0910
```
Im trying building RAG LLM app for support analyst,my primary data is excel sheet with more than 6000 incidents(rows) wi
th columns [Descrietion, Pesolution, Work notes].
Description column explains Incident Description
Resolution column exp
lains resolution provided to that Incident
Work Notes column steps taken to solve incident.

User provides the new  inci
dent as prompt to the APP, expected functionality need to search similar incidents from data , then use that similar inc
ident to generate approx resolution.

Resources available uses
uses
Azure ai search (for vector search)
GPT 4

Should I 
clean data like,
1. Like  removing special characters 
2. Lowercase the all letters
letters
3.lemmatization 
4. Removing
 stop words like a , an 

My major doubt if I embed the description of each incident as one document , does similarity s
earch , take top k documents 

 What will K be? Will k be higher number or smaller number 

Or any idea other cluster si
milar incidents ?

```
---

     
 
all -  [ Early stopping method : generate ](https://www.reddit.com/r/LangChain/comments/1c5ljzo/early_stopping_method_generate/) , 2024-04-18-0910
```
Hi everyone, I must use old langchain method to generate an output:

    agent_executor = initialize_agent(
        tool
s,
        llm,
        agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
        max_execution_time=4,
        early_st
opping_method='generate',
        verbose=False,
        handle_parsing_errors=True,
        memory=memory,
    )

early
\_stopping\_method works well using 'generate' at the 4th iteration.  
  
If I use new method:

    agent = create_react
_agent(llm, tools, prompt)
    agent_executor = AgentExecutor(agent=agent,
                                   tools=tool
s,
                                   verbose=False,
                                   handle_parsing_errors=True,
    
                               early_stopping_method='generate',
                                   max_iterations=4)

I
t's like 'generate' is not implemented:

    '/python3.11/site-packages/langchain/agents/agent.py', line 127, in return_
stopped_response
        raise ValueError(
    ValueError: Got unsupported early_stopping_method `generate`

If I use 'f
orce' with and without max\_iterations:

    Agent stopped due to iteration limit or time limit.

The main issue is i'm 
using date\_time variable, so value change every second for others tools it works like a charm.

  
Has anyone solved th
is issue ? Or maybe myearly stopping method is outdated  
Thank you in advance
```
---

     
 
all -  [ Feedback wanted: LangChain documentation structure ](https://www.reddit.com/r/LangChain/comments/1c5l53d/feedback_wanted_langchain_documentation_structure/) , 2024-04-18-0910
```
Hey folks!

We're continuing to iterate on our documentation structure to make it easier to find relevant pages. We're w
ondering what people think of top-level 'tutorial', 'how to guides', 'conceptual guide' distinctions.

Page content is s
till WIP, but we were hoping to get feedback on **the structure** sooner rather than later.

I've linked the build we're
 iterating on below. Please let us know if you have any thoughts or reactions - do you think this would help you find th
e information you need more effectively?

[https://langchain-git-harrison-new-docs-langchain.vercel.app/docs/get\_starte
d/introduction](https://langchain-git-harrison-new-docs-langchain.vercel.app/docs/get_started/introduction)
```
---

     
 
all -  [ Retriever gives an error ](https://www.reddit.com/r/LangChain/comments/1c5hzvh/retriever_gives_an_error/) , 2024-04-18-0910
```
Edit: This was solved by updating the langchain python package


This is my first time using langchain for QA on a csv f
ile. My steps were CSVLoader --> RecursiveCharacterTextSplitter --> Chroma Vectorstore 
When I searched for a keyword on
 the vectorstore with vectorstore.search('keyword', search-type='similarity'), a few documents were found. However, then
 I tried using a retriever with 
retriever=vectorstore.as_retriever(search_type='similarity'). 
If I search for the same
 keyword I used before with 
retriever.invoke('keyword'), I get the error 
AttributeError: 'NoneType' object has no attr
ibute 'get'
But I don't understand why, as it worked directly on the vectorstore.
```
---

     
 
all -  [ How to replicate Command R like Citations ](https://www.reddit.com/r/LocalLLaMA/comments/1c5e97e/how_to_replicate_command_r_like_citations/) , 2024-04-18-0910
```
Hi all,

does anyone know what's the best way to replicate Cohere's Command R functionality of returning Citation snippe
ts from the context supplied? (See [Cohere docs](https://docs.cohere.com/docs/documents-and-citations)).

I would love t
o replicate the functionality when using local LLMs with a more permissive License than Command R (+). 

I know that lan
gchain has some functionality around citations and verbatim quotes. But trying it with 7B parameter models like Mistral,
 this didn't always work. The ideal scenario would be feeding the LLM context documents that are a couple of sentences l
ong, and getting the verbatim citation coupled with the answer from the LLM.

Does this require finetuning a model? Or w
hat's the best way to approach this problem?

&#x200B;
```
---

     
 
all -  [ Can you organize data into a csv with langchain? ](https://www.reddit.com/r/LangChain/comments/1c5e0ok/can_you_organize_data_into_a_csv_with_langchain/) , 2024-04-18-0910
```
Hello, im new to all of this but i have retreived contact info from paper with a OCR into a .txt file but due to the OCR
 being inaccurate its all unorganised and stuff. Is it possbile to use Langchain to organise this data and make it more 
accurate (the 'i' is often replaced with 'l') in a csv?
```
---

     
 
all -  [ Multi Agent Interview Panel using LangGraph and LangChain  ](https://www.reddit.com/r/ArtificialInteligence/comments/1c5ctv0/multi_agent_interview_panel_using_langgraph_and/) , 2024-04-18-0910
```
Check out this demo on how I developed a Multi-Agent system to first generate an Interview panel given job role and than
 these interviewers interview the candidate one by one (sequentially) , give feedback and eventually all the feedbacks a
re combined to select the candidate. Find the code explanations & demo for automated interview for Junior Product Manage
r here : https://youtu.be/or36qevjxGE?si=cM1LMhe5J_hnpyFO
```
---

     
 
MachineLearning -  [ [D] How to get the source documents from the retrieved context for RAG?  ](https://www.reddit.com/r/MachineLearning/comments/1bvoc1t/d_how_to_get_the_source_documents_from_the/) , 2024-04-18-0910
```
I'm not using Lanchain but only making API calls to an LLM service provider. The retriever is connected to a vector DB, 
and I would like to know what the LLM refers to WITHIN that retrieved context whenever it provides an answer, similar to
 how return_source_documents works in Langchain.

I'm using AzureOpenAI. I couldn't find much in their docs that related
 to returning the source documents. Any help will be greatly appreciated!

```
---

     
 
MachineLearning -  [ [P] RAG pipeline to query the ML Engineering Open Book ](https://www.reddit.com/r/MachineLearning/comments/1bu4wyx/p_rag_pipeline_to_query_the_ml_engineering_open/) , 2024-04-18-0910
```
I built a quick RAG implementation using Langchain to make it easy to query the [ML Engineering Open Book](https://githu
b.com/stas00/ml-engineering) by [Stas Bekman](https://twitter.com/StasBekman). The Multi-Vector retriever gave pretty go
od results and was quite easy to set up too. 

Github link - [https://github.com/shreyansh26/RAG-ML-Engg-Open-Book](http
s://github.com/shreyansh26/RAG-ML-Engg-Open-Book)

Hope this is useful for folks!
```
---

     
 
MachineLearning -  [ [Project] FinancialAdvisorGPT : LLM+RAG Boilerplate Project ](https://www.reddit.com/r/MachineLearning/comments/1btlpgd/project_financialadvisorgpt_llmrag_boilerplate/) , 2024-04-18-0910
```
FinancialAdvisorGPT is a boilerplate project designed for RAG (Retriever-Augmented Generation) and LLM (Large Language M
odel) applications in financial analysis. Built on a technology stack including MongoDB, MongoDB VectorDB, Chroma, FastA
PI, Langchain, and React submodule for UI, it offers a framework for developers to implement and customize RAG+LLM proje
cts. Leveraging parallelized data pipelines, FinancialAdvisorGPT processes and integrates various data sources such as s
tock data, news, SEC filings, and local PDFs.

Github project includes long documentation on how the project is structur
ed, how LLM+RAG works for specific task : [https://github.com/mburaksayici/FinancialAdvisorGPT](https://github.com/mbura
ksayici/FinancialAdvisorGPT)
```
---

     
 
MachineLearning -  [ [Project] Picachain, image search made simple. ](https://www.reddit.com/r/MachineLearning/comments/1bt7epv/project_picachain_image_search_made_simple/) , 2024-04-18-0910
```
I am working on creating something for image search, basically something like langchain for images. Probably add videos 
too.

Currently supports chromaDB. Working on pinecone and other vector dbs. [https://github.com/d1pankarmedhi/picachain
](https://github.com/d1pankarmedhi/picachain)

Will you use something like this? What else should I add? Feel free to ad
d your views.

Appreciate your feedback or any feature ideas :)

&#x200B;
```
---

     
 
deeplearning -  [ Tengyu Ma on Voyage AI - Weaviate Podcast #91! ](https://www.reddit.com/r/deeplearning/comments/1bjft8i/tengyu_ma_on_voyage_ai_weaviate_podcast_91/) , 2024-04-18-0910
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

     
