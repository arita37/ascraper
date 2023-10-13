 
all -  [ llama2 13b hallucination on a retrival based bot ](https://www.reddit.com/r/LocalLLaMA/comments/176a0gv/llama2_13b_hallucination_on_a_retrival_based_bot/) , 2023-10-13-0910
```
looking for some suggestions on how to manage llama2 hallucination. I have a retrieval based bot where the model gets th
e data from vectors which contains data from multiple pdf. Now the challenge is if vector contains two set of totally di
fferent data for example one talks about container orchestration and another about a order processing system of online s
tore, i notice that model gets completely hallucinated . here is an example:-  
User:- what is contrainer orchestration 
 
Bot :- container orchestration refers to a process of .....  
USer:- so can i order pizza using it?  
Bot:- Yes you ca
n order pizza as the Order processing takes the new order and looks for the inventory to allocate .....  


I have used 
RAG via langchains RetrievalQA . This was suppose to solve this problem but i don;t have any luck.  Any suggestion would
 be of great help.
```
---

     
 
all -  [ Personality Chatbot using Langchain and LangSmith. [Looking for oppinions] ](https://www.reddit.com/r/SideProject/comments/1768tvn/personality_chatbot_using_langchain_and_langsmith/) , 2023-10-13-0910
```
Hey guys,

We are developing a chatbot using Langchain framework. My idea is that Bot can talk with user based on their 
info, hobbies and personalities. These info will be collected by LLM and each turn it will be ingested to the prompt. Th
ank to it, maybe it can talk more friendly.

We use MongoDB as memory and LangSmith to tracing bot's LLM calls. It still
 be developed and updating more features.

If you find it useful or see anything that needs improvement, please let our 
know.

Here is the link to it : [Chatbot with Langchain](https://github.com/btrcm00/chatbot-with-langchain)
```
---

     
 
all -  [ Building a Retrieval Augmented Generation application using Langchain (video) ](https://www.youtube.com/watch?v=ygZO21A8WaA) , 2023-10-13-0910
```

```
---

     
 
all -  [ [Langchain] Mistralai LLM avec Langchin ](https://www.reddit.com/r/redditenfrancais/comments/1762y5q/langchain_mistralai_llm_avec_langchin/) , 2023-10-13-0910
```
Langchain soutient-il le modèle AI LLM Mistral?

Traduit et reposté à partir de la publication https://www.reddit.com/16
vwilm
```
---

     
 
all -  [ A Chatbot using Langchain to integrate LLM with MongoDB memory and LangSmith to tracing LLM calls. ](https://www.reddit.com/r/Langchaindev/comments/1762w8e/a_chatbot_using_langchain_to_integrate_llm_with/) , 2023-10-13-0910
```
 We are developing a chatbot using Langchain framework. We use MongoDB as memory and LangSmith to tracing bot's LLM call
s.

If you find it useful or see anything that needs improvement, please let our know.

Here is the link to it : [https:
//github.com/btrcm00/chatbot-with-langchain](https://github.com/btrcm00/chatbot-with-langchain)
```
---

     
 
all -  [ A Chatbot using Langchain to integrate LLM with MongoDB memory and LangSmith to tracing LLM calls. ](https://www.reddit.com/r/LangChain/comments/1762tkr/a_chatbot_using_langchain_to_integrate_llm_with/) , 2023-10-13-0910
```
We are developing a chatbot using Langchain framework. We use MongoDB as memory and LangSmith to tracing bot's LLM calls
.

If you find it useful or see anything that needs improvement, please let our know.

 Here is the link to it : [https:
//github.com/btrcm00/chatbot-with-langchain](https://github.com/btrcm00/chatbot-with-langchain)
```
---

     
 
all -  [ Existing relational database to new vector database? ](https://www.reddit.com/r/datascience/comments/1761n34/existing_relational_database_to_new_vector/) , 2023-10-13-0910
```
I'm in the very early stages of an investigatory project at my job (senior software engineer with a moderate amount of d
ata mining and snowflake/star pattern ETL OLAP warehousing experience in SSAS from years ago, long before modern tools a
nd platforms, who has somehow now been deemed the SME for all things 'AI').

Basically, I have a relational SQL Server d
atabase containing tens of millions of products, each with up to 20 categories of detail. I also now have usage data fro
m our website that tracks customer interaction with these products, logging things like their account details and demogr
aphics as well as their IP, location, searches, where they clicked, how long they interacted, what they interacted with 
previously, what they interacted with next, etc.

If they wanted to run this in an old-school schema, I could work somet
hing up. I could probably even make some great reports in Power BI. But my bosses, of course, want to load this into a C
hatGPT-type interface to ask natural language questions about the data.

My cursory research tells me I need to massage 
my data into a vector database first and foremost before I start worrying about Langchain, Llama, and OpenAI, and any sp
ecific platform or toolset. But I'm not sure where to start, and I'm getting hung up on that there doesn't seem to be an
y good examples of migrating existing data - everything is either too much hype and promise-selling language that is spa
rse on detail or is a very in-the-weeds, poorly documented, mostly-incoherent mess with no examples at all or uses examp
les that are so simplistic to be not relevant to anyone.

I found some (albeit again very simplistic) examples from Milv
us that show importing semi-structured JSON-formatted objects that roughly align with what I'd equate to, in my world, d
enormalized key/value pairs for various product properties. Cool, that makes sense. That's half of it. But I'm not sure 
about the other half - how much, if any, pre-aggregation do I need to do with the analytics data? Do I import essentiall
y one object for every single piece of tracked data, or do I roll it up beforehand? I'm most interested in having this v
ector data be used to identify period-based trends, forecasts, and recommendations like 'Based on his individual product
 engagement tracking as well as the aggregate tracking of his demographically similar cohorts over the past week, what p
roducts should we surface for Bob Smith next?'

Basically, all this is a very long-winded, rambling way to get to three 
questions:

1. Are there any examples of converting a remotely complex RDMS into a vector database?

2. How much massagi
ng beyond basic denormalization and pre-aggregation do I need to do?

3. Is it sufficient to load data as lists of a but
tload of key-value pairs, or would I do better to zhuzh it into wordy natural language descriptions of the data?
```
---

     
 
all -  [ Positional metadata from PDFloaders? ](https://www.reddit.com/r/LangChain/comments/175qj2b/positional_metadata_from_pdfloaders/) , 2023-10-13-0910
```
The headline kind of says it all. Is it possible to get the positional metadata of the pieces of text you create from th
e text splitter? Would greatly enhance the user experience. Right now I'm just showing the pieces of text when mouse is 
hovering over a link
```
---

     
 
all -  [ [Langchain] Comment déployer le script Langchain Python à la production ](https://www.reddit.com/r/redditenfrancais/comments/175hqpo/langchain_comment_déployer_le_script_langchain/) , 2023-10-13-0910
```
Hé les gens! Je veux donc créer une application Web pour les entreprises de mon pays en tirant parti de la puissance de 
Langchain.

Mon problème est que je n'ai jamais déployé un seul script python dans un environnement de production, donc 
je ne sais pas par où commencer.

Je préférerais éviter les outils tels que rationaliser et gradio car les interfaces ut
ilisateur qu'ils ont ne sont pas idéales.

Au lieu de cela, je voudrais un frontend à faible code (Framer, Wix, WordPres
s, Bubble, etc.) avec lequel je peux facilement intégrer mon script Python. Cela ne me dérange pas non plus d'apprendre 
un peu de HTML, CSS, JS etc. si nécessaire, mais la situation idéale serait le frontage à faible code.

Connaissez-vous 
des ressources ou avez-vous déployé une application Web AI avec Langchain à l'aide d'un outil de code bas? J'adorerais e
ntendre des conseils et être pointé dans une certaine direction

Traduit et reposté à partir de la publication https://w
ww.reddit.com/145o0h5
```
---

     
 
all -  [ How does the pipe '|' symbol work in Python from this LangChain example? ](https://www.reddit.com/r/LangChain/comments/175edd4/how_does_the_pipe_symbol_work_in_python_from_this/) , 2023-10-13-0910
```
I'm not that experienced in Python and this is my first time trying LangChain.

In the example provided by the doc [http
s://python.langchain.com/docs/modules/agents/](https://python.langchain.com/docs/modules/agents/) , there is this one sn
ippet:

    from langchain.agents.format_scratchpad import format_to_openai_functions
    from langchain.agents.output_p
arsers import OpenAIFunctionsAgentOutputParser
    agent = {
        'input': lambda x: x['input'],
        'agent_scrat
chpad': lambda x: format_to_openai_functions(x['intermediate_steps'])
    } | prompt | llm_with_tools | OpenAIFunctionsA
gentOutputParser()

Then the \`agent\` variable is passed into \`AgentExecutor\`:

    agent_executor = AgentExecutor(ag
ent=agent, tools=tools, verbose=True)
    agent_executor.invoke({'input': 'how many letters in the word educa?'})

I und
erstand how \`prompt\` can be piped with \`llm\_with\_tools\`, because the type of \`prompt\` overrides the function \`\
_\_or\_\_\`, but how does piping dictionary and \`prompt\` work?
```
---

     
 
all -  [ Help with ideas for a project? ](https://www.reddit.com/r/AskRobotics/comments/175c4x6/help_with_ideas_for_a_project/) , 2023-10-13-0910
```
Help with an idea?

So I want to make what I’ve dubbed the everythingbot2023 because I want to try and combine every som
ewhat reasonably feasible diy robotics/ai/electronics project up until 2023 into one robot. I’m looking for more ideas t
o add.

Here is what I have so far:

•Stair climbing tracks •computer vision robotic arm •internal 3d printer- arm can g
rab 3d printed objects •offline chatbot voice response LLm-speaker/microphone- langchain+streamlit+llama 
•LiDAR- ledge/
object detection •top mount image recognition camera •face tracking mini airsoft turret •floor projector •sense of touch
 strips  •fingerprint scan top storage container •solar panel.
 
   Of course I want to interconnect all of those parts 
with the LLm as much as possible. Also I want it to have a little plant on top that it monitors and waters.
     
I am n
ot looking for advice. I fully understand how ridiculously over-ambitious this is, and I probably won’t be able to do mo
re than a few features, but hopefully someone else, or a group of people will steal the idea. But what I’m looking for i
s more “technically” feasible ideas to throw into this conglomeration. Just to have it all on the list, I know there has
 to be way more. Anything from other robotics projects to just electronics projects to add. Thank you.
```
---

     
 
all -  [ Getting Started with GenAI Stack powered with Docker, LangChain, Neo4j and Ollama ](https://www.reddit.com/r/u_ajeetsraina/comments/175ay08/getting_started_with_genai_stack_powered_with/) , 2023-10-13-0910
```
[https://collabnix.com/getting-started-with-genai-stack-powered-with-docker-langchain-neo4j-and-ollama/](https://collabn
ix.com/getting-started-with-genai-stack-powered-with-docker-langchain-neo4j-and-ollama/) 
```
---

     
 
all -  [ test effectiveness embeddings retrievalQA chatbot ](https://www.reddit.com/r/LangChain/comments/1758n1i/test_effectiveness_embeddings_retrievalqa_chatbot/) , 2023-10-13-0910
```
I have developed a chatbot that uses mistral7B instruct as LLM connected to a DB of embeddings to generate answers basin
g on context. 

The documents I am trying to embed are \~800 pdfs and the the embedding process entails splitting these 
documents (after a preprocessing) using HuggingFaceTokenizer ([https://python.langchain.com/docs/modules/data\_connectio
n/document\_transformers/text\_splitters/split\_by\_token#hugging-face-tokenizer](https://python.langchain.com/docs/modu
les/data_connection/document_transformers/text_splitters/split_by_token#hugging-face-tokenizer)) with the tokeniser of m
istral. The chunks length that I tried are \[50,200,300,400,500,750\] with the overlap of 1/3, this is the my embedding 
function: [https://huggingface.co/BAAI/bge-large-en-v1.5](https://huggingface.co/BAAI/bge-large-en-v1.5), chain type stu
ff and 6 docs retrieved. 

All sounds good until I read through the documents, make some test questions and realise the 
documents retrieved are very rarely the ones I was hoping to get. 

Anyone has faced a similar problem?
```
---

     
 
all -  [ Extending Workshop Learnings: A Dive into Supabase, PGvector, and LangChain ](https://www.reddit.com/r/Supabase/comments/1755wzh/extending_workshop_learnings_a_dive_into_supabase/) , 2023-10-13-0910
```
&#x200B;

https://preview.redd.it/4sgc6gps7itb1.png?width=1224&format=png&auto=webp&s=374c6d0c1bfcf16f590c9b4a698067d467
b8c873

I had the privilege of attending the 'Pgvector to Prod in 2 hours' workshop led by Greg Richardson at the recent
 AI Engineer Summit. The workshop was a deep dive into Supabase and PGvector, teaching us how to rapidly build a secure,
 production-ready web app.

Being someone who has been working with LangChain, I found this workshop as an opportunity t
o compare, learn, and enhance my understanding of these tools. I've articulated my journey, findings, and the contrastin
g insights between Supabase, PGvector, and LangChain in my latest blog post titled **'Extending Workshop Learnings: From
 Supabase and PGvector to LangChain'**.

In the post, I also share how this experience has inspired me to venture into a
 new project with LangChain, focusing on the rapid development and scalability of AI applications.

I've included code s
nippets, insights on text embedding generation, and a comparative analysis that could be a good read for anyone keen on 
AI application development. I’d love to hear your thoughts, feedback, or any questions you might have. Feel free to shar
e your comments here or on the blog post!

Thank you and happy reading! 📖

&#x200B;

Twitter: [https://twitter.com/arpag
on/status/1711965601797656962](https://twitter.com/arpagon/status/1711965601797656962)   
Blog Post: [https://blog.artis
anlabs.io/posts/supabase-pgvector](https://blog.artisanlabs.io/posts/supabase-pgvector)   
Jupyter Notebook Version: [ht
tps://github.com/ArtisanLabs/chatgpt-your-files/blob/main/tools/langchain/main.ipynb](https://github.com/ArtisanLabs/cha
tgpt-your-files/blob/main/tools/langchain/main.ipynb)
```
---

     
 
all -  [ Does metadata improve semantic search by default? ](https://www.reddit.com/r/LangChain/comments/174xcgf/does_metadata_improve_semantic_search_by_default/) , 2023-10-13-0910
```
Does merely including metadata (source, keyword, summary) improve the performance of a semantic search?

I am using Pine
cone to store my vectors and I am looking to improve accuracy of the search.

Additionally, what improvements can be mad
e to further enhance the accuracy? I have heard about hybrid search, but could never find a resource that evaluates its 
accuracy.
```
---

     
 
all -  [ Embedding JSON documents for categorical attributes, tags, etc ](https://www.reddit.com/r/LangChain/comments/174sw8f/embedding_json_documents_for_categorical/) , 2023-10-13-0910
```
If I have a JSON document resembling curriculum containing attributes such as:

Title

Description

Difficulty Level

Ta
gs

It's easy to understand how you would embed the textual information such as title and description, but can the categ
orical information be embedded for purposes of semantic search?

Example: 'Intro to X'

(Prioritizes Beginner level cour
ses)

Also, Tags above should be prioritized in search results. Can I instruct the embedding approach to increase weight
ing to categorical and tag based metadata?

&#x200B;

Hopefully this makes sense.
```
---

     
 
all -  [ Image inputs in chatgpt api? ](https://www.reddit.com/r/LangChain/comments/174rn9b/image_inputs_in_chatgpt_api/) , 2023-10-13-0910
```
Hi there, I know there are image inputs possible with chatgpt plus, is there an api endpoint for that too? I looked thro
ugh the documentation and wasn't able to find anything 
```
---

     
 
all -  [ I need to know how local vector databases work ](https://www.reddit.com/r/ChatGPTCoding/comments/174r6xj/i_need_to_know_how_local_vector_databases_work/) , 2023-10-13-0910
```
Im not a strong developer so excuse my beginner questions, that’s why i always try to find the visual tools. I recently 
started using flowise and noticed there is a kind of local vector db component that can replace pinecone and i tried it 
and it works as its replacement without any api keys or anything.

Can i do this in any application I build with langcha
in. Can i do a local vector db that indexes a certain folder so i can chat with its contents. How can i do it or where c
an i start. What is the difference between this, pinecone and chroma?
```
---

     
 
all -  [ Advancements in extracting tabular data from PDFs? ](https://www.reddit.com/r/datascience/comments/174pkt1/advancements_in_extracting_tabular_data_from_pdfs/) , 2023-10-13-0910
```
Hi everyone!

Is there a simple and robust method for extracting highly tabular data from a PDF without resorting to rul
e based regex parsing?  I'm currently using PDFminer, PDFplumber and regex to build templates to extract PDFs based on t
he type of PDF but it's very time-consuming and tedious.  Is there a better way?

I've used Langchain and OpenAI to buil
d 'Chat with your document' apps which works great for uploading a PDF of a whitepaper and asking it to summarize the pa
per, but when it comes to extracting table data - I don't think this solution will work.

&#x200B;

Thank you for your i
nput,

Data Scallion
```
---

     
 
all -  [ LangChain Lab ](https://www.reddit.com/r/LangChain/comments/174osbm/langchain_lab/) , 2023-10-13-0910
```
This experiment will verify different use cases of LLM using LangChain, which include chat, role-playing, and document-b
ased QA.

[https://github.com/coolbeevip/langchain-lab](https://github.com/coolbeevip/langchain-lab)
```
---

     
 
all -  [ Does StackAI have any big advantages over Flowise? ](https://www.reddit.com/r/ChatGPTCoding/comments/174ools/does_stackai_have_any_big_advantages_over_flowise/) , 2023-10-13-0910
```
Hey.

I am slightly overwhelmed by all the options when it comes to LLM applications.

Does stackAI (or other services) 
have any advantages over the free open-source langchain UI 'Flowise' ?

And can someone maybe list the different usecase
s for all the major/relevant applications of these sorts? (Flowise, Botpress, StackAI, VoiceFlow \*insert any other rele
vant thing of this nature.

And perhaps general tips.

Thanks in advance.
```
---

     
 
all -  [ Does StackAI have any big advantages over Flowise? ](https://www.reddit.com/r/Chatbots/comments/174om21/does_stackai_have_any_big_advantages_over_flowise/) , 2023-10-13-0910
```
Hey.

I am slightly overwhelmed by all the options when it comes to LLM applications. 

Does stackAI have any advantages
 over the free open-source langchain UI 'Flowise' ? 

And can someone maybe list the different usecases for all the majo
r/relevant applications of these sorts? (Flowise, Botpress, StackAI, VoiceFlow \*insert any other relevant thing of this
 nature.

And perhaps general tips.

Thanks in advance.
```
---

     
 
all -  [ I run an AI automation agency (AAA). My honest overview and review of this new business model ](https://www.reddit.com/r/Entrepreneur/comments/174o7vd/i_run_an_ai_automation_agency_aaa_my_honest/) , 2023-10-13-0910
```
I started an AI tools directory in February, and then branched off that to start an AI automation agency (AAA) in June. 
So far I've come across a lot of unsustainable 'ideas' to make money with AI, but at the same time a few diamonds in the
 rough that aren't fully tapped into yet- especially the AAA model. Thought I'd share this post to shine light into this
 new business model and share some ways you could potentially start your own agency, or at the very least know who you a
re dealing with and how to pick and choose when you (inevitably) get bombarded with cold emails from them down the line.


# Foreword

Running an AAA does NOT involve using AI tools directly to generate and sell content directly. That ship h
as sailed, and unless you are happy with $5 from Fiverr every month or so, it is not a real business model. Cry me a riv
er but generating generic art with AI and slapping it onto a T-shirt to sell on Etsy won't make you a dime.

At the same
 time, **the AAA model will NOT require you to have a deep theoretical knowledge of AI, or any academic degree**, as we 
are more so dealing with the practical applications of generative AI and how we can implement these into different workf
lows and tech-stacks, rather than building AI models from the ground up. Regardless of all that, common sense and a will
ingness to learn will help (a shit ton), as with anything.

Keep in mind - **this WILL involve work and motivation as we
ll**. The mindset that AI somehow means everything can be done for you on autopilot is not the right way to approach thi
ngs. The common theme of businesses I've seen who have successfully implemented AI into their operations is the willinge
ss to work with AI in a way that augments their existing operations, rather than flat out replace a worker or team. And 
this is exactly the train of thought you need when working with AI as a business model.

However, as the field is relati
vely unsaturated and hype surrounding AI is still fresh for enterprises, right now is the prime time to start something 
new if generative AI interests you at all. With that being said, I'll be going over three of the most successful AI-adja
cent businesses I've seen over this past year, in addition to some tips and resources to point you in the right directio
n.

# so.. WTF is an AI Automation Agency?

The AI automation agency (or as some YouTubers have coined it, the AAA model
) at its core involves creating custom AI solutions for businesses. I have over 1500 AI tools listed in my directory, ho
wever the feedback I've received from some enterprise users is that ready-made SaaS tools are too generic to meet their 
specific needs. Combine this with the fact **virtually no smaller companies have the time or skills required to develop 
custom solutions** right off the bat, and you have yourself real demand. I would say in practice, the AAA model is quite
 similar to Wordpress and even web dev agencies, with the major difference being all solutions you develop will incorpor
ate key aspects of AI AND automation.

Which brings me to my second point- JUST AI IS NOT ENOUGH. Rather than reducing t
he amount of time required to complete certain tasks, I've seen many AI agencies make the mistake of recommending and (t
rying to) sell solutions that more likely than not increase the workload of their clients. For example, if you were to m
ake an internal tool that has AI answer questions based on their knowledge base, but this knowledge base has to be updat
ed manually, this is creating unnecessary work. As such I think one of the key components of building successful AI solu
tions is incorporating the new (Generative AI/LLMs) with the old (programmtic automation- think Zapier, APIs, etc.).

Fi
nally, for this business model to be successful, ideally you should **target a niche in which you have already worked an
d understand pain points and needs**. Not only does this make it much easier to get calls booked with prospects, the sol
utions you build will have much greater value to your clients (meaning you get paid more). A mistake I've seen many AAA 
operators make (and I blame this on the 'Get Rich Quick' YouTubers) is focusing too much on a specific productized servi
ce, rather than really understanding the needs of businesses. The former is much done via a SaaS model, but when going t
he agency route the only thing that makes sense is building custom solutions. This is why **I always take a consultant-f
irst approach**. You can only build once you understand what they actually need and how certain solutions may impact the
ir operations, workflows, and bottom-line.

# Basics of How to Get Started

1. **Pick a niche.** As I mentioned previous
ly, preferably one that you've worked in before. Niches I know of that are actively being bombarded with cold emails inc
lude real estate, e-commerce, auto-dealerships, lawyers, and medical offices. There is a reason for this, but I will tel
l you straight up this business model works well if you target any white-collar service business (internal tools approac
h) or high volume businesses (customer facing tools approach).
2. **Setup your toolbox.** If you wanted to start a press
ure washing business, you would need a pressure-washer. This is no different. For those without programming knowledge, I
've seen two common ways AAA get setup to build- one is having a network of on-call web developers, whether its personal
 contacts or simply going to Upwork or any talent sourcing agency. The second is having an arsenal of no-code tools. I'l
l get to this more in a second, but this works beecause at its core, when we are dealing with the practical applications
 of AI, the code is quite simple, simply put.
3. **Start cold sales.** Unless you have a network already, this is not a 
step you can skip. You've already picked a niche, so all you have to do is find the right message. Keep cold emails shor
t, sweet, but enticing- and it will help a lot if you did step 1 correctly and intimately understand who your audience i
s. I'll be touching base later about how you can leverage AI yourself to help you with outreach and closing.

# The beau
ty of gen AI and the AAA model

You don't need to be a seasoned web developer to make this business model work. The larg
e majority of solutions that SME clients want is best done using an API for an LLM for the actual AI aspect. **The value
 we create with the solutions we build comes with the conceptual framework and design that not only does what they need 
it to but integrates smoothly with their existing tech-stack and workflow.** The actual implementation is quite straight
forward once you understand the high level design and know which tools you are going to use.

To give you a sense, even 
if you plan to build out these apps yourself (say in Python) the large majority of the nitty gritty technical work has a
lready been done for you, especially if you leverage Python libraries and packages that offer high level abstraction for
 LLM-related functions. For instance, calling GPT can be as little as a single line of code. (And there are no-code tool
s where these functions are simply an icon on a GUI). Aside from understanding the capabilities and limitations of these
 tools and frameworks, the only thing that matters is being able to put them in a way that makes sense for what you want
 to build. Which is why outsourcing and no-code tools both work in our case.

# Okay... but how TF am I suppposed to act
ually build out these solutions?

Now the fun part. I highly recommend getting familiar with Langchain and LlamaIndex. B
oth are Python libraires that help a lot with the high-level LLM abstraction I mentioned previously. The two most import
ant aspects include being able to integrate internal data sources/knowledge bases with LLMs, and have LLMs perform auton
omous actions. The two most common methods respectively are RAG and output parsing.

**RAG (retrieval augmented Generati
on)**

If you've ever seen a tool that seemingly 'trains' GPT on your own data, and wonder how it all works- well I have
 an answer from you. At a high level, the user query is first being fed to what's called a vector database to run vector
 search. Vector search basically lets you do semantic search where you are searching data based on meaning. The vector d
atabases then retrieves the most relevant sections of text as it relates to the user query, and this text gets APPENDED 
to your GPT prompt to provide extra context to the AI. Further, with prompt engineering, you can limit GPT to only gener
ate an answer if it can be found within this extra context, greatly limiting the chance of hallucination (this is where 
AI makes random shit up). Aside from vector databases, we can also implement RAG with other data sources and retrieval m
ethods, for example SQL databses (via parsing the outputs of LLM's- more on this later).

**Autonomous Agents via Output
 Parsing**

A common need of clients has been having AI actually perform tasks, rather than simply spitting out text. Fo
r example, with autonomous agents, we can have an e-commerce chatbot do the work of a basic customer service rep (i.e. l
ook into orders, refunds, shipping). At a high level, what's going on is that the response of the LLM is being used prog
rammtically to determine which API to call. Keeping on with the e-commerce example, if I wanted a chatbot to check shipp
ing status, I could have a LLM response within my app (not shown to the user) with a prompt that outputs a random hash o
r string, and programmatically I can determine which API call to make based on this hash/string. And using the same fund
amental concept as with RAG, I can append the the API response to a final prompt that would spit out the answer for the 
user.

**How No Code Tools Can Fit In (With some example solutions you can build)**

With that being said, you don't nec
essarily need to do all of the above by coding yourself, with Python libraries or otherwise. **However, I will say that 
having that high level overview will help IMMENSELY when it comes to using no-code tools to do the actual work for you.*
* Regardless, here are a few common solutions you might build for clients as well as some no-code tools you can use to b
uild them out.

* **Ex. Solution 1: AI Chatbots for SMEs (Small and Medium Enterprises)**
   * This involves creating **
chatbots that handle user queries, lead gen, and so forth with AI**, and will use the principles of RAG at heart. After 
getting the required data from your client (i.e. product catalogues, previous support tickets, FAQ, internal documentati
on), you upload this into your knowledge base and write a prompt that makes sense for your use case. One no-code tool th
at does this well is **MyAskAI**. The beauty of it especially for building external chatbots is the ability to quickly i
ngest entire websites into your knowledge base via a sitemap, and bulk uploading files. Essentially, they've covered the
 entire grunt work required to do this manually. Finally, you can create a inline or chat widget on your client's websit
e with a few lines of HTML, or altneratively integrate it with a Slack/Teams chatbot (if you are going for an internal Q
&A chatbot approach). Other tools you could use include **Botpress and Voiceflow**, however these are less for RAG and m
ore for building out complete chatbot flows that may or may not incorporate LLMs. Both apps are essentially GUIs that el
iminate the pain and tears and trying to implement complex flows manually, and both natively incoporate AI intents and a
 knowledge base feature.
* **Ex. Solution 2: Internal Apps**
   * Similar to the first example, except we go beyond maki
ng just chatbots but tools such as report generation and really **any sort of internal tool or automations that may inco
rporate LLM's**. For instance, you can have a tool that automatically generates replies to inbound emails based on your 
client's knowledge base. Or an automation that does the same thing but for replies to Instagram comments. Another exampl
e could be a tool that generates a description and screeenshot based on a URL (useful for directory sites, made one for 
my own :P). Getting into more advanced implementations of LLMs, we can have tools that can generate entire drafts of rep
orts (think 80+ pages), based not only on data from a knowledge base but also the writing style, format, and author voic
e of previous reports.
   * One good tool to create content generation panels for your clients would be **MindStudio**. 
You can train LLM's via prompt engineering in a structured way with your own data to essentially fine tune them for what
ever text you need it to generate. Furthermore, it has a GUI where you can dictate the entire AI flow. You can also uplo
ad data sources via multiple formats, including PDF, CSV, and Docx.
   * For automations that require interactions betwe
en multiple apps, I recommend the OG **zapier/make.com** if you want a no-code solution. For instance, for the automatic
 email reply generator, I can have a trigger such that when an email is received, a custom AI reply is generated by **My
AskAI**, and finally a draft is created in my email client. Or, for an automation where I can create a social media post
s on multiple platforms based on a RSS feed (news feed), I can implement this directly in Zapier with their native GPT a
ction ([see screenshot](https://imgur.com/9rwpaz4))
   * As for more complex LLM flows that may require multiple layers 
of LLMs, data sources, and APIs working together to generate a single response i.e. a long form 100 page report, I would
 recommend tools such as Stack AI or Flowise (open-source alternative) to build these solutions out. Essentially, you ge
t most of the functions and features of Python packages such as Langchain and LlamaIndex in a GUI. [See screenshot](http
s://imgur.com/o5trxuC) for an example of a flow

# How the hell are you supposed to find clients?

With all that being s
aid, none of this matters if you can't find anyone to sell to. You will have to do cold sales, one way or the other, esp
ecially if you are brand new to the game. And what better way to sell your AI services than with AI itself? If we want t
o integrate AI into the cold outreach process, first we must identify what it's good at doing, and that's obviously writ
ing a bunch of text, in a short amount of time. Similar to the solutions that an AAA can build for its clients, we can t
ake advantage of the same principles in our own sales processes.

**How to do outreach**

Once you've identified your ni
che and their pain points/opportunities for automation, you want to craft a compelling message in which you can send via
 cold email and cold calls to get prospects booked on demos/consultations. I won't get into too much detail in terms of 
exactly how to write emails or calling scripts, as there are millions of resources to help with this, but I will tell yo
u a few key points you want to keep in mind when doing outreach for your AAA.

First, you want to keep in mind that many
 businesses are still hesitant about AI and may not understand what it really is or how it can benefit their operations.
 However, we can take advantage of how mass media has been reporting on AI this past year- at the very least people are 
AWARE that sooner or later they may have to implement AI into their businesses to stay competitive. We want to frame our
 message in a way that introduces generative AI as a technology that can have a direct, tangible, and positive impact on
 their business. Although it may be hard to quantify, I like to include estimates of man-hours saved or costs saved at l
east in my final proposals to prospects. Times are TOUGH right now, and money is expensive, so you need to have a compel
ling reason for businesses to get on board.

Once you've gotten your messaging down, you will want to create a list of p
rospects to contact. Tools you can use to find prospects include **Apollo.io, reply.io, zoominfo (expensive af), and Lin
kedin Sales Navigator**. What specific job titles, etc. to target will depend on your niche but for smaller companies th
is will tend to be the owner. For white collar niches, i.e. law, the professional that will be directly benefiting from 
the tool (i.e. partners) may be better to contact. And for larger organizations you may want to target business improvem
ent and digital transformation leads/directors- these are the people directly in charge of projects like what you may be
 proposing.

Okay- so you have your message, and your list, and now all it comes down to is getting the good word out. I
 won't be going into the details of how to send these out, a quick Google search will give you hundreds of resources for
 cold outreach methods. However, personalization is key and beyond simple dynamic variables you want to make sure you ca
n either personalize your email campaigns directly with AI (SmartWriter.ai is an example of a tool that can do this), or
 at the very least have the ability to import email messages programmatically. Alternatively, ask ChatGPT to make you a 
Python Script that can take in a list of emails, scrape info based on their linkedin URL or website, and all pass this o
nto a GPT prompt that specifies your messaging to generate an email. From there, send away.

**How tf do I close?**

Onc
e you've got some prospects booked in on your meetings, you will need to close deals with them to turn them into clients
.

* Call #1: Consultation
   * Tying back to when I mentioned you want to take a consultant-first appraoch, you will wa
nt to listen closely to their goals and needs and understand their pain points. This would be the first call, and typica
lly I would provide a high level overview of different solutions we could build to tacke these. It really helps to have 
a presentation available, so you can graphically demonstrate key points and key technologies. I like to use **Plus AI** 
for this, it's basically a Google Slides add-on that can generate slide decks for you. I copy and paste my default compa
ny messaging, add some key points for the presentation, and it comes out with pretty decent slides.
* Call #2: Demo
   *
 The second call would involve a demo of one of these solutions, and typically I'll quickly prototype it with boilerplat
e code I already have, otherwise I'll cook something up in a no-code tool. If you have a niche where one type of solutio
n is commonly demanded, it helps to have a general demo set up to be able to handle a larger volume of calls, so you are
n't burning yourself out. I'll also elaborate on how the final product would look like in comparison to the demo.
* Call
 #3 and Beyond:
   * Once the initial consultation and demo is complete, you will want to alleviate any remaining concer
ns from your prospects and work with them to reach a final work proposal. It's crucial you lay out exactly what you will
 be building (in writing) and ensure the prospect understands this. Furthermore, be clear and transparent with timelines
 and communication methods for the project. In terms of pricing, you want to take this from a value-based approach. The 
same solution may be worth a lot more to client A than client B. Furthermore, you can create 'add-ons' such as monthly m
aintenance/upgrade packages, training sessions for employeees, and so forth, separate from the initial setup fee you wou
ld charge.

**How you can incorporate AI into marketing your businesses**

Beyond cold sales, I highly recommend creatin
g a funnel to capture warm leads. For instance, I do this currently with my AI tools directory, which links directly to 
my AI agency and has consistent branding throughout. Warm leads are much more likely to close (and honestly, much nicer 
to deal with).

However, even without an AI-related website, at the very least you will want to create a presence on soc
ial media and the web in general. As with any agency, you will want basic a professional presence. A professional virtua
l address helps, in addition to a Google Business Profile (GBP) and TrustPilot. a GBP (especially for local SEO) and Tru
stpilot page also helps improve the looks of your search results immensely.

For GBP, I recommend using **ProfilePro**, 
which is a chrome extension you can use to automate SEO work for your GBP. Aside from SEO optimzied business description
s based on your business, it can handle Q/A answers, responses, updates, and service descriptions based on local keyword
s.

**Privacy and Legal Concerns of the AAA Model**

Aside from typical concerns for agencies relating to service contra
cts, there are a few issues (especially when using no-code tools) that will need to be addressed to run a successful AAA
. Most of these surround privacy concerns when working with proprietary data. In your terms with your client, you will w
ant to clearly define hosting providers and any third party tools you will be using to build their solution, and a DPA w
ith these third parties listed as subprocessors if necessary. In addition, you will want to implement best practices lik
e redacting private information from data being used for building solutions. In terms of addressing concerns directly fr
om clients, it helps if you host your solutions on their own servers (not possible with AI tools), and address the fact 
only ChatGPT queries in the web app, not OpenAI API calls, will be used to train OpenAI's models (as reported by mainstr
eam media). The key here is to be open and transparent with your clients about ALL the tools you are using, where there 
data will be going, and make sure to get this all in writing.

# have fun, and keep an open mind

Before I finish this p
ost, I just want to reiterate the fact that this is NOT an easy way to make money. Running an AI agency will require hou
rs and hours of dedication and work, and constantly rearranging your schedule to meet prospect and client needs. However
, if you are looking for a new business to run, and have a knack for understanding business operations and are **genuine
ly interested in the pracitcal applications of generative AI**, then I say go for it. The time is ticking before AAA bec
omes the new dropshipping or SMMA, and I've a firm believer that those who set foot first and establish themselves in th
is field will come out top. And remember, while 100 thousand people may read this post, only 2 may actually take initiat
ive and start.
```
---

     
 
all -  [ Snowflake as vector db? ](https://www.reddit.com/r/LangChain/comments/174npws/snowflake_as_vector_db/) , 2023-10-13-0910
```
Hi, just a couple of words before I explain what I'm asking, I know that Snowflake or any traditional database is not me
ant to perform as well as Pinecone does.

But the company I work at has a long process to start working with new vendors
, like Pinecone.

Is it possible to use Snowflake as a vector store? And if so, do you have examples? I didn't find anyt
hing on the internet.

&#x200B;
```
---

     
 
all -  [ What's the best LLM for handling multi-step tasks/data, which isn't insanely expensive? ](https://www.reddit.com/r/ChatGPTCoding/comments/174mm17/whats_the_best_llm_for_handling_multistep/) , 2023-10-13-0910
```
Hello!

I've spent the last few days trying to build a multi-step chatbot, using the GPT3.5 Turbo 16K model, which can b
oth converse with the user in a fun way (basically, standard function), but can also collect several pieces of info from
 a user in natural-language, before returning that entire thing as one object. My first run, a single prompt, was a bit 
of a failure, I just couldn't put enough into the prompts to make it understand all the context, rules, and what it can 
and can't do. After much research, I began to work on building multiple agents, which hand tasks around based on the con
text (I also looked into langchain, but found the JS docs, which is what I'm working in, a little lacking & confusing!)


After much tweaking, and much prompt engineering, I've gotten much closer. I have one handler that essentially decides 
if the user wants to 'run' the task, currently running the task, or just wants a general convo. For each call, I also pa
ss in a 'context' object, which contains information on the things the user has already specified in chat. This is built
 and updated by the initial agent too, and seems to work for the most part. It nearly always successfully parses most of
 the data and hands it off to a relevant agent. 

The first issue however arises when the sub-agent is in charge of work
ing out which data has been provided, which hasn't, and which needs clarifying/improving, and then prompting the user ba
sed on that. I'd like it to be able to use a few simple tools to enhance data - for example, if a user has specified a g
eneral location, such as 'New York Library', I have a tool that allows it to generate a search term to hand over to the 
google places API to access the proper location data including the address for this. The issue is though, it just doesn'
t seem to be able to fully manage and understand the context of all the data. It also is a challenge making sure all of 
the agents know the rules and what they can and can't do, and catching any mistruths they say in prompt engineering.

Th
e second issue is that while this approach seems to be working - and maybe with more refining and agents might work full
y - it's also really slow. Because I'm asking GPT to really read and consider all the context, and am having to make 2 o
r 3 different calls to GPT for each single user message, it takes close to 10 seconds per response. The cost is also beg
inning to rise, of course, which is making it slowly more unviable too.

I did one single run on GPT4 with my original V
1 prompt, and it got much closer, making me feel it'd be much more viable using GPT4... but it GPT4 is just way too expe
nsive for me at the moment to be able to use.

My next idea is to break it down and put it a bit more on rails, so once 
the user enters the collection flow, I have one agent per piece of data and always go in the same order, but I'm a littl
e weary about this as I still want a free-entry text field, and I'm worried if a user begins the chat with one or more o
f the pieces of info in the initial message, I may end up in a very similar position to my V2 attempt.

Therefore, I'm i
nterested to know if anyone else has achieved this sort of multi-step context etc using a different model (IE Llama 2 or
 Claude), or if anyone has any tips that might improve reliability or reduce the need for so many agents?
```
---

     
 
all -  [ Create professional photos for folks who can't afford them? ](https://www.reddit.com/r/StableDiffusion/comments/174ml71/create_professional_photos_for_folks_who_cant/) , 2023-10-13-0910
```
Hi all (posted originally on r/singularity and they said to post here) - I work for an ed-tech company that specializes 
in giving access to skills and training to those who aren't served by traditional education channels. We are providing s
kills to get your first job, how money works, food safety, hygiene, and things like this.

We are focused mainly on Sout
hern Africa right now and one thing we've noticed our learners struggle with is that they aren't able to have profession
al-looking headshots taken. This is something that is often used in hiring situations in these markets. They all have ac
cess to low-end smartphones though.

Can anyone recommend a way for us to add the capability to take a photo (or multipl
e?) and turn it into something you'd likely see on LinkedIn or similar? I'm the CTO and pretty deep into Langchain and o
ther LLM technologies. I've used Midjourney and Dall-E for original creations, but need some help finding a technique fo
r this use case. Thanks!
```
---

     
 
all -  [ Running prompts on custom data ](https://www.reddit.com/r/learnmachinelearning/comments/174fg5w/running_prompts_on_custom_data/) , 2023-10-13-0910
```
Hey everyone. I am noob trying to learn LLMs. 

I have a text file with some unstructured data. There are no any column 
or rows, just strings.

I want gpt to use this information and answer my prompts by only using that data.

And answer sh
ould not be in like 1 or 2 lines. I want very long format structured answer as instructed in my prompt. 

I researched a
nd understood that langchain can help with it. But is there any other alternative because I was not satisfied with the o
utput or maybe I am doing something wrong. 

Can someone tell me which is the best LLM for this and how to achieve this?


Thanks
```
---

     
 
all -  [ Purpose of Pipeline/Chain Abstractions? ](https://www.reddit.com/r/LocalLLaMA/comments/174eckz/purpose_of_pipelinechain_abstractions/) , 2023-10-13-0910
```
I've worked with more than a few streaming, distributed processing, and orchestration frameworks in the past, and am fam
iliar with their designs and, more importantly, the reasoning behind their designs. It's common for frameworks like thes
e to have you treat your functions as some flavor of an abstract computation node, assemble them into pipelines, use con
ditional/'routing' primitives that they provide, limit the library functions you can call from within a computation node
 to a set of functions their API provides, etc.

This is done so the frameworks can more easily accomplish their core pu
rpose, i.e. distribute and parallelize computation while routing data/messages, control the input/output flow themselves
 for distributed execution, feed streaming events from an external source to a function by invoking it per msg or in bat
ches, support streaming computation using stream processing functions the framework has built-in support for, etc. The r
eason for these frameworks to not use vanilla Python/etc is partly because applications using the framework can not be e
xecuted as a normal Python script, executed by the Python interpreter, because the framework is essentially providing a 
different execution model (i.e. streaming, distributed, event-based + distributed, whatever) and will need to itself per
form certain functions that the interpreter normally would perform.

Handling all of these things is significantly easie
r for a framework if it provides a set of standard abstractions (in code) that define how applications must be structure
d, control how clients can define functions, inputs, execution and data flow, limit what methods can be called from with
in functions, limit how clients can define and access stateful variables, etc - think Flink & similar as examples. The d
esign of these constructs/API enforces the restrictions inherent to the framework, and using them versus vanilla Python/
etc removes the need for things like Python/etc AST parsing and validation. These abstractions are restrictive, as they 
limit how you can write your application, and they require the framework to reimplement and handle things the actual lan
guage runtime normally would - but it's all for the sake of enabling the frameworks' core functionality.

I'm seeing the
 same concepts used in frameworks like Haystack, Griptape, LangChain, but with none of the benefits and no similar under
lying reasons. Can somebody explain why things like [https://docs.haystack.deepset.ai/docs/nodes\_overview#decision-node
s](https://docs.haystack.deepset.ai/docs/nodes_overview#decision-nodes) and Haystack/Griptape's various types of nodes, 
plus pipelines, workflows, agents, etc etc... are better than \`if\` statements (in the case of decision nodes) and norm
al Python function definitions and general execution?

Let's take this snippet from Langchain's docs as another example:
[​](https://python.langchain.com/docs/modules/chains/#why-do-we-need-chains)

>Why do we need chains?  
>  
>Chains allo
w us to combine multiple components together to create a single, coherent application. For example, we can create a chai
n that takes user input, formats it with a PromptTemplate, and then passes the formatted response to an LLM. We can buil
d more complex chains by combining multiple chains together, or by combining chains with other components.

Am I crazy, 
or are they are literally just describing the concept of abstracting code into function blocks and allowing function blo
cks to call other function blocks... you know, the most fundamental and basic of programming primitives. It would be one
 thing if Chains were then used as a building block by the framework to enable some type of functionality/processing, or
 provide some kind of guarantee, that normal Python function definitions and invocations do not already provide... but n
o, instead they're just invoked and executed like any other function/callable, with the 'chain' becoming nothing more th
an the call stack at runtime. What is a single benefit of having to structure everything using a hierarchy of 'Chains' v
ersus normal Python/Typescript function calls?

One could argue that useless/contrived abstractions still have actual va
lue for framework authors because they increase the coupling between your codebase and their framework, increasing the f
riction of moving to a different framework... but to paraphrase Hanlon, 'prob not.' Am I just missing something?
```
---

     
 
all -  [ S3DirectoryLoader Unstructured docx not working ](https://www.reddit.com/r/LangChain/comments/174dd0b/s3directoryloader_unstructured_docx_not_working/) , 2023-10-13-0910
```
Hi all.  I'm trying to develop a RAG prototype in an AWS Sagemaker environment.  I have a load of MS Word documents in a
 bucket and have pip installed the unstructured package.  However when I try and load the documents using LangChain's S3
 Directory loader it throws an exception and tells me I need to install unstructured(docx).   

I'm going to try the Fil
eLoadee to see if that works but I have more than 100 files to load.   Has anyone come across this issue?
```
---

     
 
all -  [ LangChain + Streamlit + Llama: Bringing Conversational AI to Your Local Machine ](https://www.reddit.com/r/ArtificialInteligence/comments/174922q/langchain_streamlit_llama_bringing_conversational/) , 2023-10-13-0910
```
Integrating open-source LLMs and LangChain for free generative question answering (no API key required). Learn more: htt
ps://plainenglish.io/blog/langchain-streamlit-llama-bringing-conversational-ai-to-your-local-machine  
  

```
---

     
 
all -  [ HI, I need some Insights on RAG, possibly a solution or suggestion ](https://www.reddit.com/r/LangChain/comments/17411qu/hi_i_need_some_insights_on_rag_possibly_a/) , 2023-10-13-0910
```
I was given a task to create a Q and A bot on some company files (user manuals and lot of catalogs with technical datash
eets)  
So I started building a RAG system. Results of the system is not good , it often say that the context dose not m
entioned what I'm asking.  
There are few things I identified that might cause a problem:  
1. Documents are in Dutch la
nguage , (might mitigate the problem because the Questions are mostly Dutch).  
2. Amount of the Document \~ 200 PDFs , 
Average Pages 15\~20.  
3. All of the documents contain lot of images (catalogs and stuff) so the text is only the half 
of the actual information.  
4. PDFs contain lot of tabular data too, which I cant see the tabular format from the extra
cted data (I used an pdf parser to extract the text data from the pdf).  
So to get a better output I changed these para
meters :  
1.Using Regex I preprocessed the extracted text data (remove the whitespaces and replace the special characte
rs)  
2. Since I need specific answers from the bot I set the chunk size to 250\~450, and chunk overlap 75\~175 (Recursi
veCharacterTextSplitter)  
3. Set temperature to 0 (Which I don't think have an impact on the output accuracy)  


I'm u
sing ,  
LLM : GPT-4.  
Embeddings : text-embeddings-ada-002 .  
Supportive Library : Langchain. (Silly me, but thought 
to mention it just in case)  
Test Env. VDB : FAISS . (For testing varied chunk sizes and other parameters)  
Production
 Env. VDB : Pinecone (Standard) .  


No Prompt engineering used so far (tree of thought , ReAct or etc.) , intend to us
e parent document retrieval from Langchain.  


What am I doing wrong here ? What can I do better ? I'm open to any sugg
estions  
```
---

     
 
all -  [ What Memory Type Do You Recommend? ](https://www.reddit.com/r/LangChain/comments/173t400/what_memory_type_do_you_recommend/) , 2023-10-13-0910
```
I'm building a RAG app and I'm at the point where I need to install robust long-term memory. The langchain memory types 
I'm currently considering are,

1. [Conversation Summary Buffer](https://python.langchain.com/docs/modules/memory/types/
summary_buffer),
2. [Entity](https://python.langchain.com/docs/modules/memory/types/entity_summary_memory),
3. [Conversa
tion Knowledge Graph](https://python.langchain.com/docs/modules/memory/types/kg)

However, I'm curious if any of you hav
e hands on experience and can make a recommendation. 

Have you tried different Langchain memory types? How did they wor
k for you? 
```
---

     
 
all -  [ How to make an agent decide and call multiple functions if needed? ](https://www.reddit.com/r/LangChain/comments/173rv7y/how_to_make_an_agent_decide_and_call_multiple/) , 2023-10-13-0910
```
I am new to langchain. I am try to build something.
User message: 'Create a object with name obj and delete obj b'

I ha
ve two functions: create object and delete object,

Initially, it was executing only the first command. But then I chang
ed the changed the agent type to this. It started executing both commands

`initialize_agent( agent=AgentType.STRUCTURED
_CHAT_ZERO_SHOT_REACT_DESCRIPTION`

But when I changed the function and message to accept two params, it started throwin
g this error: 

User message: 'Create a object with name hello and size 10 and delete obj b'

`ToolException: Too many a
rguments to single-input tool Create Bot. Args: ['hello', 10]`

This is my function def:

`def create_obj(name, size):`



Also, for my use case should I continue with  `AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION `or` Multi Action
 Agent`? I am very confused!

Thank you in advance!
```
---

     
 
all -  [ Let’s see everyone’s LangChain Projects! ](https://www.reddit.com/r/homeassistant/comments/173rsy7/lets_see_everyones_langchain_projects/) , 2023-10-13-0910
```
Having played around with OpenAI's function calling features and the LangChains agents, it's been a surprise to see that
 not many have integrated GPT-3.5 into their Home Assistant (Hass) setups. My hands-on experience with LangChain over th
e last few weeks has me believing that setting up an agent to perform semantic searches against a vector store, especial
ly with all Hass entities at its disposal, could be a game changer.

I’m feeling the itch to get my hands dirty and bind
 my own setup, but I'm curious to see if anyone else has dived into this yet. It's exciting to think about the different
 ways we could optimize our Hass assistants with this kind of setup. Would love to hear what the community is up to befo
re I take the plunge!
```
---

     
 
all -  [ Is there any way to load online PDFs using UnstructuredURLLoader? ](https://www.reddit.com/r/LangChain/comments/173qx3d/is_there_any_way_to_load_online_pdfs_using/) , 2023-10-13-0910
```
I am trying to do question answering using UnstructuredURLLoader   
How can I achieve this?  
Pls help me out !!!  
**An
y help would be greatly appreciated**   


online PDFs like '[https://qwertyui/UG\_2023-24.pdf](https://mnit.ac.in/cms/u
ploads/2023/06/UG_2023-24.pdf)'
```
---

     
 
all -  [ Best techniques for optimizing LLM agent speed ](https://www.reddit.com/r/LangChain/comments/173pdpz/best_techniques_for_optimizing_llm_agent_speed/) , 2023-10-13-0910
```
Hey folks-

Looking for a summary of techniques for minimizing latency. Even with simple agent architectures (e.g. 1 GPT
 3.5 agent or 2-5 talking to each other), latency feels quite high (>30s).

Thinking of trying out fine-tuned Mistral & 
optimizing prompt lengths, relying on Vector DBs more, etc. Curious what others have done successfully.
```
---

     
 
all -  [ Summary of latest language-AI techniques with example LangChain code? ](https://www.reddit.com/r/LangChain/comments/173p3ys/summary_of_latest_languageai_techniques_with/) , 2023-10-13-0910
```
Hey folks-

I'm looking for a small collection / cheatsheet of common patterns & example code demonstrating how to imple
ment with LangChain - e.g. Retrieval-Augmented Generation, ReAct agents, Tree of Thought, Plan & Execute agents, etc.

I
deally, would be <10 pages with code + succinct explainers.

Cheers
```
---

     
 
all -  [ Best solution for serving & fine-tuning Mistral 7B & other OSS models ](https://www.reddit.com/r/LangChain/comments/173p2h3/best_solution_for_serving_finetuning_mistral_7b/) , 2023-10-13-0910
```
Hey folks!

I'm looking for a platform where I can query the Instruct version of Mistral 7B & easily fine-tune it to my 
use-case cheaply & easily via LangChain.

What's the current best option(s)?
```
---

     
 
all -  [ Best way to expand the Next-Langchain starter? ](https://www.reddit.com/r/LangChain/comments/173ovyr/best_way_to_expand_the_nextlangchain_starter/) , 2023-10-13-0910
```
I recently set up the [Next-Langchain-starter from Vercel](https://github.com/vercel/ai/tree/main/examples/next-langchai
n), and it is phenomenal: Easy to setup, easy to modify. So far I've only done a few modifications:

* Added auth0
* Add
ed a custom template
* Added knowledge about todays date and time.

Have any of you experimented with it? Do you have su
ggestions for what functionality that is easy and useful to add, to quickly show the benefits of LangChain? I am conside
ring adding a YouTube document-loader next, but very open to suggestions on where to start.
```
---

     
 
all -  [ add metadata to document without openai ](https://www.reddit.com/r/LangChain/comments/173l5x4/add_metadata_to_document_without_openai/) , 2023-10-13-0910
```
How to add metadata to my document (i.e a contract between buyer and seller). Now while storing documents in vector stor
e (FAISS). I want to add meta data to each contract but without the use of openai. Kindly suggest any way to do this.

M
eta data: buyer name, vendor name, duration of the contract, pricing condition etc

&#x200B;
```
---

     
 
MachineLearning -  [ [P] Retrieval augmented generation with OpenSearch and reranking [Video tutorial] ](https://www.reddit.com/r/MachineLearning/comments/16zouad/p_retrieval_augmented_generation_with_opensearch/) , 2023-10-13-0910
```
I created a video tutorial that tries to demonstrate that semantic search (using embeddings) is not always necessary for
 RAG (retrieval augmented generation). It was inspired by the following Cohere blog post: [https://txt.cohere.com/rerank
/](https://txt.cohere.com/rerank/)


I code up a minimal RAG pipeline: `OpenSearch -> Rerank -> Chat completion` (withou
t using Langchain or similar libraries) and then see how it performs on various queries.


Hope some of you find it help
ful. Feel free to share any feedback@

Video link: https://youtu.be/OsE7YcDcPz0
```
---

     
 
MachineLearning -  [ [D] Perplexity.ai Search Feasibility ](https://www.reddit.com/r/MachineLearning/comments/16x63ce/d_perplexityai_search_feasibility/) , 2023-10-13-0910
```
I've been using [Perplexity.ai](https://perplexity.ai/) for a bit now when it hit me that I don't understand how they ca
n sustain their business model with search. Stuff like Bing search and Google search cost around $5 or more per 1000 sea
rches, so how can they even afford to do this kind of search. Do they have their own search index.

Also, I don't know h
ow they pull in the data from these sources so fast? I've played around with some things like this with Langchain with r
etrieval, but the speed of splitting and tokenizing website html is not very fast. Have they already pre-scrapped the we
bsites from the search results and tokenized them for LLM retrieval?
```
---

     
 
MachineLearning -  [ [P] vLLM, Langchain, Embedchain ? ](https://www.reddit.com/r/MachineLearning/comments/16ndyxc/p_vllm_langchain_embedchain/) , 2023-10-13-0910
```
Which libraries do you think would be the most important to learn between these, and to use in my next personal project 
? This will be a conversational chatbot trained on podcast transcripts
```
---

     
 
MachineLearning -  [ [R] Agents: An Open-source Framework for Autonomous Language Agents - AIWaves Inc 2023 ](https://www.reddit.com/r/MachineLearning/comments/16jl4pe/r_agents_an_opensource_framework_for_autonomous/) , 2023-10-13-0910
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

     
 
MachineLearning -  [ [P] Ways to speed up llama-2 summarization on sagemaker? ](https://www.reddit.com/r/MachineLearning/comments/16iutyp/p_ways_to_speed_up_llama2_summarization_on/) , 2023-10-13-0910
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

     
 
MachineLearning -  [ [P][R] Kani: A Lightweight Highly Hackable Open-Source Framework for Building Chat Applications with ](https://www.reddit.com/r/MachineLearning/comments/16gxp51/pr_kani_a_lightweight_highly_hackable_opensource/) , 2023-10-13-0910
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

     
 
deeplearning -  [ AutoGen from Microsoft ](https://www.reddit.com/r/deeplearning/comments/170hke6/autogen_from_microsoft/) , 2023-10-13-0910
```
AI agents are AI systems that can exhibit capabilities such as conducting conversations, completing tasks, reasoning, an
d seamlessly interacting with humans. 

As frameworks like LangChain build Agents as a module in their framework, Micros
oft is thinking way ahead. It has built **AutoGen**, a framework to enable seamless MULTI-agent conversation and collabo
ration to accomplish complex tasks by reasoning and working autonomously. 

Here is a video explaining the latest AutoGe
n framework from Microsoft: https://youtu.be/daigxHA2aYw?si=86alxsVZkRpz5Quv

Do you think multi-agents are the future o
f AI? Or will AI emerge in other ways? Let me know your thoughts.
```
---

     
 
deeplearning -  [ TheBloke/Llama-2-7b does not appear to have a file named pytorch_model.bin, tf_model.h5, model.ckpt  ](https://www.reddit.com/r/deeplearning/comments/16ihzn8/theblokellama27b_does_not_appear_to_have_a_file/) , 2023-10-13-0910
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

     
