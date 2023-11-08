 
all -  [ Reorganizing or categorize inputs by tool type ](https://www.reddit.com/r/LangChain/comments/17q2fww/reorganizing_or_categorize_inputs_by_tool_type/) , 2023-11-08-0909
```
Hello to all the diligent craftsmen and craftswomen!

We've encountered a hiccup in our process. Currently, we're using 
a conversational agent to interface with external APIs for various tasks. Let's say we have four such tools at our dispo
sal. Consider a scenario where a user requests, 'Use tool #1 for an action, recite a poem for me, perform an action with
 tool #2, follow it up with a haiku, and then repeat an action with tool #1.'

Our challenge arises with the sequence of
 these prompts. We instruct the system to first activate tool #1, then generate a haiku, followed by using tool #2, and 
finally, to carry out an action with tool #1 once more. However, post-haiku, the system seems reluctant to re-engage too
l #1. Conversely, if we streamline the prompt to execute all actions of tool #1, proceed to tool #2, and cap it off with
 the haiku, everything functions seamlessly. It appears that the system favors prompts organized by tool-specific action
s rather than a heterogeneous or ungrouped sequence.

We're attempting to coax the language model through our template t
o categorize inputs by tool type before proceeding, yet luck hasn't been on our side.

Would anyone have a strategy or a
dvice to untangle this? Your insights would be greatly appreciated. Thank you!
```
---

     
 
all -  [ SelfQueryRetriever w/ date metadata ](https://www.reddit.com/r/LangChain/comments/17q054j/selfqueryretriever_w_date_metadata/) , 2023-11-08-0909
```
Has anyone successfully used dates as metadata while using the SelfQueryRetriever? 

I'm guessing it's not supported as 
I get the following error: 

>Expected where operand value to be a str, int, float, or list of those type, got 2021-05-1
1. 

I've seen references to using the datetime.date type but I also tried just using a string as the type, but I got th
e same error either way. My metadata AttributeInfo looks like this: 

    AttributeInfo(
            name='isodate',
   
         description='The date the document was created',
            type='datetime.date',
    )

 This is how the unde
rlying StructuredQuery is being constructed which looks exactly like what I want: 

    StructuredQuery(query='SomeInfo'
, filter=Comparison(comparator=<Comparator.EQ: 'eq'>, attribute='isodate', value=datetime.date(2021, 5, 11)), limit=None
)

Maybe there's another way to achieve this without the SelfQueryRetriever? 

Hopefully someone can point me in the rig
ht direction. Thanks!
```
---

     
 
all -  [ Where to find documentation for langchain implementation of QDRANT Operations? ](https://www.reddit.com/r/LangChain/comments/17q04t0/where_to_find_documentation_for_langchain/) , 2023-11-08-0909
```
I'm trying to implement CRUD operations such as Uploading Points, Updating Points, Retrieving Points  etc which are avai
lable in QDRANT documentation. Is there an equivalent of these in langchain. All I see is the integration part here: [ht
tps://qdrant.tech/documentation/integrations/langchain/](https://qdrant.tech/documentation/integrations/langchain/)

&#x
200B;
```
---

     
 
all -  [ Will new ChatGPT updates replace RAG? ](https://www.reddit.com/r/LangChain/comments/17pzvrw/will_new_chatgpt_updates_replace_rag/) , 2023-11-08-0909
```
I've been working on a project doing extraction and summarization of large PDFs using Langchain. I've watched the OpenAI
 dev talk and am wondering whether the cloud-based retrieval that was discussed will likely replace RAG?  It seems like 
to some extent it will, but at the same time, the end user will likely have to have GPT plus to access whatever model or
 bot is created with the doc.  

I know it is too early to tell for sure, but I'm hoping to get some insights before I g
o too far with my project, only to realize that it will be replaced by off-the-shelf functionality.  

Thoughts?
```
---

     
 
all -  [ Please roast this resume ](https://i.redd.it/9o0ict9nlyyb1.png) , 2023-11-08-0909
```
This is my friend's resume :)
```
---

     
 
all -  [ 20 document limit for retrieval assistants ](https://www.reddit.com/r/OpenAI/comments/17pyi3l/20_document_limit_for_retrieval_assistants/) , 2023-11-08-0909
```
Has anyone messed with the document retrieval yet? I wanted to test using our SoP docs to build an SoP bot, but looks li
ke despite having up 100GB limit for total files, the assistants are limited to 20 documents max. I'm hoping they increa
se this limit once the beta is over. I had built the same bot using LangChain with vector stores, but this seems to give
 better outputs with the 20 docs I was able to test with. 
```
---

     
 
all -  [ GPT-4 Vision Chatbot use-cases with api ](https://www.reddit.com/r/LangChain/comments/17pxnur/gpt4_vision_chatbot_usecases_with_api/) , 2023-11-08-0909
```
Less than 24 hours since launch, I have been testing GPT-4 Vision api and here are some cool use-cases I tested

Links t
o code here :- [GitHub - Anil-matcha/GPT-4-Vision-Chatbot: GPT-4 Vision Chatbot examples](https://github.com/Anil-matcha
/GPT-4-Vision-Chatbot/)

1. AI Data Scientist
2. AI Diet Planner
3. Handwriting reader
4. Schedule Planner
5. Object det
ector
6. Meme generator
7. Website Roaster
8. TV Show Recommender
9. Educator
```
---

     
 
all -  [ Vectorizing Survey Responses ](https://www.reddit.com/r/LangChain/comments/17pvxxk/vectorizing_survey_responses/) , 2023-11-08-0909
```
I currently have a survey with tons of open ended responses i want to vectorize using langchain so i can use an open sou
rce LLM to help me summarize said responses. this survey is roughly 200 essay questions, with 15 responders. I would lik
e to at least be able to just ask the model to summarize the responses in less words, but ideally i would like to ingest
 both the question, response, and respondent into the model. I cant seem to find much info on this. My long and not so f
un workaround solution is to turn each survey into a PDF and ingest them that way, but that is not a very efficient proc
ess for me. 
```
---

     
 
all -  [ ChromaDB filters ](https://www.reddit.com/r/LangChain/comments/17pv8p1/chromadb_filters/) , 2023-11-08-0909
```
Is there any fine tuned version of a pre trained text generation model out there that can automatically infer ChromaDB f
ilter queries on a VDB based on natural language question inputted by the user ?
```
---

     
 
all -  [ How does LangChain actually implement the ReAct pattern on a high level? ](https://www.reddit.com/r/LangChain/comments/17puzw9/how_does_langchain_actually_implement_the_react/) , 2023-11-08-0909
```
I am trying to understand how ReAct agents are implemented on a high level to understand the concepts behind this approa
ch. Unfortunately, the LangChain docs are so high-level that they are almost useless. And diving into the code itself is
 cumbersome given the high degree of complexity with almost no documentation (there's not a single comment in AgentExecu
tor, for example...).

What I understood is that the logic looks roughly like so:

    Programmer defines a ReAct agent 
prompt template containing the typical steps of 
    1) question,
    2) thought,
    3) tool/action,
    4) tool/action
 input,
    5) observation. 
    
    User sends initial prompt to agent containing:
    - The task to fulfill or questi
on to answer
    Agent enriches the prompt template with this task/answer. Initial question is set to user's question.
 
   
    Agent now starts a loop:
    1. Send the current question, thought, tool/action, tool/action input, observation 
to the LLM.
    2. LLM updates values those values (= reasoning step)
    3. LLM creates structured output (e.g. JSON)
 
   4. LLM sends back updated values to agent
    5. Agent may potentially make use of the tool with the tool inputs. (ac
tion step)
    6. Agent repeats steps 1 - 5 until the reasoning step reveals that the final goal has been reached, or un
til another abortion condition is given
    
    Agent returns answer to user.

My main question is: To my understanding
 the agent does not only plan once (e.g. initially) and then executes all steps as returned by the LLM. Instead, it repe
ats planning the next step after each action.

Can anyone please confirm my understanding is correct? Or point me to som
ething more tangible (ideally some sequence diagram)?

&#x200B;

EDIT: I've checked the (much simpler) implementation of
 BondAI, and this seems to confirm my understanding: [https://github.com/krohling/bondai/blob/main/bondai/agent.py](http
s://github.com/krohling/bondai/blob/main/bondai/agent.py)
```
---

     
 
all -  [ AutoGen v0.2.0b2 released ](https://www.reddit.com/r/AutoGenAI/comments/17puk3q/autogen_v020b2_released/) , 2023-11-08-0909
```
[New release: v0.2.0b2](https://github.com/microsoft/autogen/releases/tag/v0.2.0b2)  

This is a beta release of v0.2.0b
2.

## Highlights

* **Support for GPT-4V!** Introduced Large Multimodal Models in AgentChat, enhancing capabilities and
 interactions within the platform. Blogpost: [https://microsoft.github.io/autogen/blog/2023/11/06/LMM-Agent](https://mic
rosoft.github.io/autogen/blog/2023/11/06/LMM-Agent)
* Improved codebase reliability with updates such as dict copying be
fore modifications (fixing a bug for Azure OpenAI) and various typo fixes.
* Added support for unstructured data in retr
ieve chat (RAG).
* Expanded functionality with async support for better get\_human\_input  
 handling.
* A new simple Te
stbed tool for Autogen processes.
* Enhanced developer tools and documentation, including new README and TRANSPARENCY\_F
AQS updates.

Thanks to all the testers for the v0.2 migration. Thanks to [@BeibinLi](https://github.com/BeibinLi) [@son
ichi](https://github.com/sonichi) [@AkariLan](https://github.com/AkariLan) [@vatsalya-vyas](https://github.com/vatsalya-
vyas) [@gfggithubleet](https://github.com/gfggithubleet) [@gagb](https://github.com/gagb) [@thinkall](https://github.com
/thinkall) [@hung-ngm](https://github.com/hung-ngm) [@afourney](https://github.com/afourney) [@AaadityaG](https://github
.com/AaadityaG) [@jasondotparse](https://github.com/jasondotparse) [@bonadio](https://github.com/bonadio) [@aayushchhabr
a1999](https://github.com/aayushchhabra1999) [@qingyun-wu](https://github.com/qingyun-wu) [@eltociear](https://github.co
m/eltociear) [@marcgreen](https://github.com/marcgreen) and other contributors!

## What's Changed

* Added a simple Tes
tbed tool for repeatedly running templated Autogen scenarios with tightly-controlled initial conditions. by [@afourney](
https://github.com/afourney) in [#455](https://github.com/microsoft/autogen/pull/455)
* Fix typo import autogen by [@hun
g-ngm](https://github.com/hung-ngm) in [#549](https://github.com/microsoft/autogen/pull/549)
* Add support to unstructru
ed by [@thinkall](https://github.com/thinkall) in [#501](https://github.com/microsoft/autogen/pull/501)
* Update TRANSPA
RENCY\_FAQS.md by [@gfggithubleet](https://github.com/gfggithubleet) in [#492](https://github.com/microsoft/autogen/pull
/492)
* Update README.md by [@vatsalya-vyas](https://github.com/vatsalya-vyas) in [#507](https://github.com/microsoft/au
togen/pull/507)
* fix wrong 'Langchain Provided Tools as Functions' doc ref by [@AkariLan](https://github.com/AkariLan) 
in [#495](https://github.com/microsoft/autogen/pull/495)
* copy dicts before modifying by [@sonichi](https://github.com/
sonichi) in [#551](https://github.com/microsoft/autogen/pull/551)
* Large Multimodal Models in AgentChat by [@BeibinLi](
https://github.com/BeibinLi) in [#554](https://github.com/microsoft/autogen/pull/554)

## New Contributors

* [@hung-ngm
](https://github.com/hung-ngm) made their first contribution in [#549](https://github.com/microsoft/autogen/pull/549)
* 
[@gfggithubleet](https://github.com/gfggithubleet) made their first contribution in [#492](https://github.com/microsoft/
autogen/pull/492)
* [@vatsalya-vyas](https://github.com/vatsalya-vyas) made their first contribution in [#507](https://g
ithub.com/microsoft/autogen/pull/507)
* [@AkariLan](https://github.com/AkariLan) made their first contribution in [#495]
(https://github.com/microsoft/autogen/pull/495)

**Full Changelog**: [v0.2.0b1...v0.2.0b2](https://github.com/microsoft/
autogen/compare/v0.2.0b1...v0.2.0b2)
```
---

     
 
all -  [ Announcing Obsidian Text Generator Plugin v0.5.12: Now with GPT-4 (128k) Support and More! ](https://www.reddit.com/r/ObsidianMD/comments/17pub2o/announcing_obsidian_text_generator_plugin_v0512/) , 2023-11-08-0909
```
Hello,

We're super excited to share that the stable release of the **Obsidian TextGenerator Plugin v0.5.12** is finally
 here! 🎉 This update is not just a step up – it's a leap forward, bringing with it a host of improvements and brand-new 
features designed to enhance your experience and take your note-taking to new heights. Here’s what we’ve packed into thi
s release:

✨ **Key Highlights of v0.5.12:**

* 🚀 **GPT-4 Support:** We've integrated the latest and greatest GPT-4 mode
l (gpt4 turbo, 128k) right into Obsidian.
* 🌐 **Language Model Versatility:** With flexible support for an impressive ra
nge of models (gpt3.5, gpt4, claude, bard, llama) via Langchain, your text generation options are vast.
* 🎨 **Playground
 UI Overhaul:** Enjoy a more intuitive and visually engaging interface when testing prompts and viewing responses.
* 🔍 *
*Enhanced Settings:** Navigate through a newly refined, searchable settings menu.
* ⚙️ **Advanced Template Engine:** Tak
e your note automation up a notch with the power of Handlebars & Javascript, now with chaining capabilities.
* 🛠️ **Temp
lates as Tools:** Edit and apply templates on-the-fly, across any app..
* 📊 **Efficient Data Handling:** Extract variabl
es more effectively with Handlebars for advanced data management.
* 🐞 **Optimizations & Bug Fixes:** Enjoy a smoother pe
rformance with numerous refinements and fixes.

**New Documentation:**

We've also revamped our documentation to help yo
u get the most out of the TextGenerator Plugin. Check it out for detailed guides and tips: [https://docs.text-gen.com/](
https://docs.text-gen.com/)

This update is the result of countless hours of hard work and dedication to provide you wit
h a tool that not only complements your workflow but also enhances it in ways you didn't expect. Whether you're drafting
 up your next big novel, managing your daily tasks, or capturing fleeting thoughts, the Obsidian TextGenerator Plugin v0
.5.12 is here to elevate your experience.

We can't wait to see how you'll use these new features! So go ahead, update y
our plugin, and give these new capabilities a whirl!  


Discord: [https://discord.com/invite/BRYqetyjag](https://discor
d.com/invite/BRYqetyjag) 

Happy note-taking,
```
---

     
 
all -  [ LangServe + AgentExecutor ](https://www.reddit.com/r/LangChain/comments/17pstfw/langserve_agentexecutor/) , 2023-11-08-0909
```
I'm just getting started with LangServe, which seems to add a few nice functionalities on top of my own FastAPI server, 
but I don't want to use it with the templates. I'm a little puzzled why the team put so much emphasis on that.

Anyway, 
setting it up with a vanilla LLM works right out of the box, but when I use an agent (AgentExecutor) from the initialize
\_agent() function the playground doesn't recognize any inputs or outputs. The endpoint still works through the docs, bu
t not through the playground.

Do you have any experience with that? Any pointers to tutorials to use LangServe without 
templates?
```
---

     
 
all -  [ Facing problems with Llama-2-7b-chat-hf and langchain ](https://www.reddit.com/r/LangChain/comments/17pqhj9/facing_problems_with_llama27bchathf_and_langchain/) , 2023-11-08-0909
```
I want to create an application that uses llama-2-7b-chat-hf to chat with PDFs.  
Steps I followed are in the colab note
book below -   


[https://colab.research.google.com/drive/1SS4JWvFb\_SapmDMedcHZvRgs1Bd2MjZQ?usp=sharing](https://colab
.research.google.com/drive/1SS4JWvFb_SapmDMedcHZvRgs1Bd2MjZQ?usp=sharing)  


I know its a mess, but after all that I di
d, the problems I faced are -   


1) When we retrieve the text using retrieverQA, we can't get the proper similar text.
 I don't know if the PDFs I am giving are difficult to read or retriever/embedding model is not that good for finding th
e accurate text related to the question prompt.  


2) Vectorstore takes a huge amount of memory. When we embed our data
 and store it in a vector store, it takes space in the RAM instead of the drive space. How to store vectordb in ROM?  



3) As I keep asking the prompts, the size of vectordb keeps increasing to the point where we get the error - CUDA out o
f memory. Why is the size of vectordb increasing when we query the model, is it again storing all the prompts and answer
s in the db? Or is it because of the buffermemory? Plz someone explain.  


4) Once we create the PromptTemplate, how to
 verify if the entire promptTemplate with proper context is going as the input to the model? As you can see, when I quer
y the model, all the model returns are the query, results, and the source chunk. So I am not sure if the code I wrote is
 providing the proper prompt to the model.  


5) Also, is it recommended to give memory to the model or just use contex
t to get the answers?  


6) I think the model I am using is not good in calculation, but I think langchain can provide 
the tools to integrate into the chain, how to implement them?  


And the biggest problem of all, the model is not givin
g accurate results, I am confused whether its because it gets an irrelevant chunk of data, my bad prompt or some other r
eason.   


I know this is a lot and I am sorry if I might be asking some very silly questions, but I am genuinely curio
us about all this.   
Please guide me for this project, and if you can't access the notebook, you can DM me for more det
ails. Thank you
```
---

     
 
all -  [ OpenAi Assistant / my thought process ](https://www.reddit.com/r/OpenAI/comments/17pmm7n/openai_assistant_my_thought_process/) , 2023-11-08-0909
```
I’m not a developer but have understanding and working with Developers to build product.
So what I understand OpenAi ass
sitant I can simply create one for my company( example upload all Hr document ) and ask developer to connect this and gi
ve it to my new employee to ask questions about any hr rules? 
It feels like LangChain and other way of building gpt is 
not required. But would this cost a lot everytime I ask questions ?
```
---

     
 
all -  [ OpenGPTs: LangChain's open source alternative to OpenAI's GPT ](https://github.com/langchain-ai/opengpts) , 2023-11-08-0909
```

```
---

     
 
all -  [ New OpenAI Assistant tools: Knowledge Retrieval question ](https://www.reddit.com/r/OpenAI/comments/17pif3l/new_openai_assistant_tools_knowledge_retrieval/) , 2023-11-08-0909
```
So like (almost) everyone here I was pretty floored by the announcements today. As a dev, more than anything else the ne
w Assistants features really caught my eye. At face value, it seemed like this was the all-in-one I needed. No more chun
king and implementing vector dbs. From the OAI docs:   
'Retrieval augments the Assistant with knowledge from outside it
s model, such as proprietary product information or documents provided by your users. Once a file is uploaded and passed
 to the Assistant, OpenAI will automatically chunk your documents, index and store the embeddings, and implement vector 
search to retrieve relevant content to answer user queries.' Wow, gimme.

However, I'm slightly confused on how to use t
his if I want to upload text content from say an API response, not a \`.txt\`, \`.pdf\` file etc. Here's the example fro
m the docs:

`const file = await openai.files.create({  file: fs.createReadStream('knowledge.pdf'),  purpose: 'assistant
s', });`  


LangChain let's you create Documents like so `const doc = new Document({ pageContent: 'foo' });` which idea
lly what I would want to do here too. Am I missing something?
```
---

     
 
all -  [ How do you compare 100s of documents with a local LLM? ](https://www.reddit.com/r/LocalLLaMA/comments/17pfpm5/how_do_you_compare_100s_of_documents_with_a_local/) , 2023-11-08-0909
```
I have identified some dimensions - language, size, security, complexity, scalability, privacy, etc. - to compare a few 
100 documents. I now want to compare these documents across these dimensions (to note down their differences basically).
  What approach do you use to do this with a local LLM?

I thought I'd first create a vectorstore from the documents, an
d then run the following query in a loop with Langchain's 'RetrievalQA':

    query = f'Summarise the document {i}.txt b
ased on the ten parameters identified: size, security, complexity, scalability, privacy, etc)'

But my LLM (llama-2-7B) 
is giving inconsistent results. Sometimes it gives an output that looks like its alright, but upon close inspection I fi
nd that its gotten even the basic things wrong - like, it would say the language is English when in fact it is German (n
ot something the LLM has to deduce by the way, it is mentioned in the document). At other times it would reply, on the s
ame query, with this:

    Based on the provided context, I will do my best to answer your questions. Please provide the
 first project's name, as mentioned in the context, and I will summarize it based on the 14 dimensions you have provided
.
    So, what is the name of the first project?

At yet other times:

    Of course! I'm happy to help you with that. B
ased on the provided context, here is a summary of the project description for the attributes you mentioned:
    * Langu
age: N/A (not specified)
    * Size: N/A (not specified)
    * Security: N/A (not specified)
    * Complexity: N/A (not 
specified)
    * Scalability: N/A (not specified)
    * Privacy: N/A (not specified)
    * ... : N/A (not specified)
   
 * ... : N/A (not specified)

And then I lost all hope with this approach, because forget summarising a document based o
n some given points, it can't even retrieve the title of that document:

    > Question:
    What is the title of the pr
oject in 1.txt?
    
    > Answer:
      Great! Based on the provided context, the question you are asking is 'What is t
he title of the project in 1.txt?'
    To answer this question, I need to check the content of the file named '1.txt' in
 the provided context. Unfortunately, there is no information in the context about the title of a specific project, so I
 must inform you that I cannot provide an answer to your question based on the given context.
    Please provide more in
formation or context about the project you are referring to, and I'll be happy to help you find the answer to your quest
ion.

So, what else could I try? Is my approach wrong? (I did not even get to the looping stage, these are experiments w
ith just one of the documents - I would have moved to the loop if I got good responses with one doc.)

I have tried thes
e same prompts/queries with ChatGPT and it is able to answer to a very high degree of correctness. I don't mind a downgr
ade in the quality with a local LLM, but at least it should give consistent and half-correct answers.
```
---

     
 
all -  [ Are embeddings needed when using csv_agent ? ](https://www.reddit.com/r/LangChain/comments/17pffai/are_embeddings_needed_when_using_csv_agent/) , 2023-11-08-0909
```
hey, just getting into this properly and was hoping for a bit of advice.

I have a CSV file with 200k rows. Most are col
umns with true or false, there would be an ID column which connects rows to a cost centre, and a few columns describing 
location like country, city etc. None of the columns would really have any free text in them.

I am wondering if embeddi
ngs are required for a file like this, I have it working using csv\_agent, it creates the pandas query and filters the d
ata.  I have added some context to the prompt so that it properly understands the data dataset.  Using chatgpt4.  


I g
et that embeddings are used to do similarity searches but in my mind this only makes sense if there is free text or a bo
dy of text that the query needs to be compared against.  Am I right about this?  Or would it make more sense to embed ea
ch row?  


If embedding is the way to go, I had this working too but the issue I am hitting is the openAI limit.  If I 
load the csv it gives me a list of 200k documents but to get this to work I think I need to then loop over the documents
 and create the embeddings in chromadb or FAISS ?  I have tried using FAISS to create the embeddings from the list of do
cuments but it hits the limit once I go above 17 documents in the list.

&#x200B;

Many thanks  


&#x200B;
```
---

     
 
all -  [ tinylang is now in v2, now supporting image inputs in conversation memory! ](https://www.reddit.com/r/LangChain/comments/17pe369/tinylang_is_now_in_v2_now_supporting_image_inputs/) , 2023-11-08-0909
```
Launch post: https://x.com/cosmo4\_ai/status/1721645041373069820?s=20
```
---

     
 
all -  [ Issues with Document Ranking in EnsembleRetriever and Multi-Keyword Search Optimization ](https://www.reddit.com/r/LangChain/comments/17pcb4e/issues_with_document_ranking_in_ensembleretriever/) , 2023-11-08-0909
```
I'm using an EnsembleRetriever that's composed of a BM25_Retriever (75%) and a Vector_Retriever (25%). Yet, the document
 where the search term objectively appears most frequently isn't ranked first. What could be the reason?

Also, how can 
I search for multiple keywords in this setting to improve the precision of the results?

EDIT: I found the reason for th
e first problem. The keyword only occurs as a prefix more often on the target page than on the other page, where the key
word occurs as a separate word. Searching for more than a single keyword would help in this case. But is there a way to 
fix this prefix issue like fuzzy matching? I already applied lemmatization, but it does not fix it completely.
```
---

     
 
all -  [ New OpenAI Assistant API ](https://www.reddit.com/r/LangChain/comments/17pbynv/new_openai_assistant_api/) , 2023-11-08-0909
```
Hi everyone, I just saw the OpenAI devday event and I'd like to discuss about the new Assistant API. It provides retriev
al functionalities and I'm wondering how this will affect Langchain usage. 

Let's discuss!
```
---

     
 
all -  [ How Does Conversation Memory Work with Router Chains? ](https://www.reddit.com/r/LangChain/comments/17pbe5b/how_does_conversation_memory_work_with_router/) , 2023-11-08-0909
```
How does conversation memory (e.g. ConversationBufferMemory) work in router chains? Passing it into the main router make
s sense to me, but insofar as creating a chat interface is concerned (i.e. allowing the user to interact with outputs), 
how does that work? Thanks in advance!
```
---

     
 
all -  [ OpenAI DevDay summary (not generated 😉) ](https://www.reddit.com/r/OpenAI/comments/17pao1k/openai_devday_summary_not_generated/) , 2023-11-08-0909
```
 Highlights from my notes during the event:

👑 ChatGPT-4 Turbo Model  
\- The most advanced AI model  
\- x3 times cheap
er than GPT-4  
\- 128k context length (300pg book length)  
\- Knowledge cutoff: April 2023  
\- Dall-E 3, Advanced Dat
a Analysis, Browsing all out-of-the-box  
\- JSON Mode and multi-function calling  
\- ChatGPT UI using this model start
ing today

⚙️ New API Capabilities  
\- Vision and Audio via the API!  
\- Image Generation via API  
\- Voice generatio
n  
\- Data retrieval, code execution  
\- x2 Rate Limit

🛡️Copyright Shield - OpenAI will now cover legal costs if user
s are accused of copyright infringement

⚡Assistants API  
\- Handle long threads and context  
\- Data retrieval and fi
le parsing  
\- Handles a lot of LangChain and RAG type stuff natively

🤖 Create Your Own GPTs (Agents)  
\- Create usec
ase-specific chatbots directly on the platform  
\- Upload data that can be used in the chatbot  
\- Can leverage voice,
 vision, code execution, browsing  
\- Combine instructions, capabilities (function calling), knowledge (files)  
\- Can
 be built without code  
\- Share your custom GPTs with others  
\- OpenAI Store coming later this month - they plan to 
do rev share

This is absolutely nuts! I'll be covering this in more detail in an upcoming YouTube video, but it's crazy
 to think how much more is possible now and how this changes the landscape yet again!  


EDIT: Made the video covering 
this with more detail:  [https://youtu.be/crQE-GIjtNY](https://youtu.be/crQE-GIjtNY) 
```
---

     
 
all -  [ Hiearchical RAG ](https://www.reddit.com/r/LangChain/comments/17p5w5o/hiearchical_rag/) , 2023-11-08-0909
```
I am building a **Retrieval-Augmented Generation (RAG)** conversational agent specifically designed to navigate through 
a dense forest of highly regulated financial data.

Basically I have a pdf document having 'risk factors' for trade tran
sactions and I want to allow user to ask questions against this document. The risk factors are organized in a hiearchica
l manner with each risk factor a text paragraph that shed light on it. When building a rietriever based on the question 
: 'show all risk factors' it fails to produce the desired result and we have 2 problems:  
1. not enough risk factors ex
tracted  
2. relevant and name changing

I was wondering if there is a way to structure the retrieval process in like a 
two-step :  
1. Retrieves the risk factors (take into consideration hiearchy)  
2. For every risk factor the text descrp
tion (if tasked by the user to provide more details)  


I was wondering if anyone was facing the same and managed to re
solve it and if there are any techniques / retrieval strategies that might work for this task
```
---

     
 
all -  [ Join our FREE Beta Today! ](https://www.reddit.com/r/ProductHunters/comments/17p4tit/join_our_free_beta_today/) , 2023-11-08-0909
```
Hi All!  
I'm Simone from the Knowlee team, thrilled to introduce our ultimate AI assistant powered by top-notch technol
ogies like GPT4, Pinecone, and Langchain. Here’s a quick run-through of how Knowlee can revolutionize your workflow:

1️
⃣ **Feed Knowledge**: Import documents, videos, social posts, news, financial stats, or any content you need analyzed.  

2️⃣ **Get Instant Insights**: Knowlee processes your content and provides instant, intelligent insights to help you mak
e informed decisions.  
3️⃣ **Content Creation**: Leverage these insights to generate relevant and timely content, keepi
ng you ahead of the curve.

We're currently inviting enthusiasts to join our beta testing program and contribute to shap
ing the future of Knowlee.

Feel free to drop a comment or send a DM if you’re ready to explore the capabilities of Know
lee!
```
---

     
 
all -  [ Coded a Data Analysis Assistant with Streamlit & Semantic Kernel ](https://www.reddit.com/r/Python/comments/17p3cpi/coded_a_data_analysis_assistant_with_streamlit/) , 2023-11-08-0909
```
&#x200B;

>**TLDR** \- Used Streamlit & Semantic Kernel Data Analysis Assistant demo is in Youtube Video: [Analassist De
mo](https://www.youtube.com/watch?v=snwZcYVP_WY)

Hello r/Python!

I'm excited to share a demo of my latest project, **A
nalassist** \- your AI-powered assistant for analyzing data, crafted with the robustness of Semantic Kernel and the inte
ractivity of Streamlit.

🎥 **Check out the demo here:** [Analassist Demo](https://www.youtube.com/watch?v=snwZcYVP_WY)


[Thumbnail from our Youtube: https:\/\/www.youtube.com\/watch?v=snwZcYVP\_WY](https://preview.redd.it/6ztxo610gqyb1.png?
width=1000&format=png&auto=webp&s=1b10ed2f4196b6b0c415662071535377d700c0c7)

## What is Analassist?

Analassist is an in
novative tool designed to streamline the data analysis process. Here’s what you can do with it:

* **📊 Upload a CSV file
**: Easily import your data into the app.
* **🗣 Interactive prompts**: Use natural language to ask questions and get ins
ights from your data.
* ⏰ **Real-time code generation**: Watch as the AI interprets your prompts and generates code on t
he fly. (Backend)
* 📈 **Data visualization**: Turn messy data into crisp, clear tables and graphs.

In this demo, you'll
 see how I upload a dataset, use prompts to command the AI to perform analysis, and how it neatly outputs visualizations
 and interpretations, particularly focusing on data from Bangladesh.

# Tech Stack  

* 🌟 **Streamlit**: For crafting in
tuitive app interfaces. 
* 🧠 **Semantic Kernel**: To power AI-driven data interpretations and insights.   


## Highligh
ts from the Demo

Check out this snippet from the demo for a taste of Analassist's capabilities:

[Sample Demo](https://
preview.redd.it/ul8xmznsfqyb1.png?width=1000&format=png&auto=webp&s=8e144c8c76540d77282a7bea90b4b755c3232bcf)

## More t
o Come

Stay tuned as I will be posting additional tutorials on using Semantic Kernel for more sophisticated tasks. If y
ou're interested, be sure to subscribe to my channel.

## Get Involved in Development!

Your contributions can help make
 Analassist even better! If you're interested in contributing to the project or just want to take a peek at the code, ch
eck out the GitHub repository:

🔗 [Analassist on GitHub](https://github.com/calapsss/analassist-langchain-vs-microsoft-s
k)

🔗 [Understand Semantic Kernel](https://youtu.be/90hhJHTWz50)

Whether it's adding new features, fixing bugs, or impr
oving documentation, every bit of help is welcome.

# Share Your Feedback

I hope I get insights from you on how I could
 improve this project. Thank's for reading!
```
---

     
 
all -  [ RAG: Flexible Context Retrieval around a matching chunk ](https://www.reddit.com/r/LocalLLaMA/comments/17p31mc/rag_flexible_context_retrieval_around_a_matching/) , 2023-11-08-0909
```
Here's something I was thinking about and found existing solutions inadequate -- the so-called big-vs-small chunks dilem
ma: You want:

* small chunks for accurate embeddings
* large chunks to capture sufficient context to answer queries.

T
he solution is clearly to *decouple* chunking and retrieval. Ideally, we want to be able to chunk at a granular level, a
nd retrieve an (almost arbitrary) context-window around the matching chunk. I call this **Flexible Context Retrieval (FC
R).**

So I looked at LangChain's `ParentDocumentRetriever` \- it creates larger *parent* chunks, and splits those into 
smaller *child* chunks, and only embed/index the child chunks. At query time, when a child chunk matches, lookup its par
ent chunk and return that instead. While this sounds like it may solve the problem, there are two issues with this:

1️⃣
 Because the parent-chunks are **fixed**, you will have **boundary** effects, like this failure case (see pic):The **que
ry** matches a child-chunk near the **end** of a parent chunk; the **answer** is in the **next** parent chunk, and does 
**not** match the query ➡️ The next parent chunk is not retrieved, and the LLM fails to answer the query.This **blind sp
ot** is due to the **fixed** chunking.

&#x200B;

[Context Retrieval: LangChain vs Langroid](https://preview.redd.it/jg1
kori1fqyb1.png?width=2924&format=png&auto=webp&s=305bcd86260cee195cd2c6d92dc0c9082de36540)

2️⃣ You have to **carefully*
* pick the parent chunk size: Realized it's too small? ➡️ need to **re-chunk** and **re-index**; If you make it conserva
tively too big, that defeats the purpose of chunking, and you'll run into high latency and token costs, and LLM context-
limits.

Then I looked at Llama-Index's `SentenceWindowNodeParser` and it's an improvement -- at **parsing/chunking** ti
me, it stores a **fixed** window of text around each small chunk (sentence, actually). So at retrieval time you can retr
ieve this (fixed) text window around any matching chunk. This solves Problem 1 above but *not* Problem 2.

Thinking abou
t this from scratch, I realized one good way to do it is this: only create small, granular chunks (say at sentence level
), and in each chunk's metadata, store a sufficiently large (say 20) sequence of **chunk-ids** (**not content!**) before
 and after the chunk. At query time, we can then flexibly look up *any (up to 20)* desired number of  chunks around the 
matching chunk (see pic). This gives you Flexible Context Retrieval (FCR).

&#x200B;

[Langroid: Storing window\_ids to 
support Flexible Context Retrieval](https://preview.redd.it/n3x5bqd6fqyb1.png?width=2602&format=png&auto=webp&s=a82ab30f
5a1afabc65a0bdcb8eb197722d91efd5)

I implemented FCR in [Langroid](https://github.com/langroid/langroid/blob/main/langro
id/agent/special/doc_chat_agent.py) (see the `add_context_window` method). One issue is dealing with overlaps among retr
ieved windows. This turned out to be tricky since chunk-ids are based on hash-uuids (and for various reasons these are b
etter than just using sequence numbers). I ended up using **connected-component** detection to group overlapping windows
, and then **topological sorting** to sort the window-group based on the partial-order imposed by the pairwise relations
.

Here's a [colab](https://colab.research.google.com/drive/1JvH6CO9AS7CaWK0GTblZGesJoo9Jjyn7) where I compare the LangC
hain ParentDocumentRetriever and Langroid's methods on two questions about an employment contract. With LangChain the LL
M fails on both due to the above boundary effect, but with Langroid, it works fine.

I was wondering if anyone else had 
a look at the FCR problem. At the very least I hope the Langroid implementation is useful.

Langroid is a Python framewo
rk to easily build LLM applications (including RAG), using a multi-agent paradigm.

Thanks for reading.

&#x200B;

&#x20
0B;
```
---

     
 
all -  [ Differences in Information Extraction: GPT-3.5 Turbo vs. Text-DaVinci-003 ](https://www.reddit.com/r/LangChain/comments/17ozahp/differences_in_information_extraction_gpt35_turbo/) , 2023-11-08-0909
```
Why am I getting significantly worse results (more hallucinations) with 'gpt-3.5-turbo' compared to 'text-davinci-003' f
or information extraction tasks?
```
---

     
 
all -  [ Create synthetic data from scratch ](https://www.reddit.com/r/LangChain/comments/17oxxot/create_synthetic_data_from_scratch/) , 2023-11-08-0909
```
 I have built a free AI-powered app that let you create synthetic data. You could provide dataset schema, some examples 
(recommended) and even seed input for the AI Generator:

* Schema/Variables: Columns name define what variables are in y
our dataset
* Examples: Provide with examples to guide the AI Generator during generation. It is useful 1-3 examples as 
inspiration.
* Seeds: They are incomplete rows to be filled by AI Generator. This is useful whe you have certain sensiti
ve variables in your dataset and you want to avoid hallucination from the AI Generator, so you provide as seed input.

I
 hope any one could find it helpful. Would love to hear and discuss any feedback :)

Platform: [https://gendata.streamli
t.app/](https://gendata.streamlit.app/)
```
---

     
 
all -  [ Keeping up with all the RAG developments... ](https://www.reddit.com/r/LangChain/comments/17oxgr0/keeping_up_with_all_the_rag_developments/) , 2023-11-08-0909
```
Hi all,

RAG is evolving fast. My team and I are working to keep things simple and digestible for developers out there, 
while still making sure they're aware of their options. 

To this effect, on Wednesday, we're hosting a livestream on Li
nkedIn and YouTube with an Overview of RAG Approaches. This post is a bit of a plug, but tbh, the content was super help
ful for our internal teams and I want to make it available to the wider community.

If you're interested in joining, her
e's the link: [https://www.linkedin.com/events/overviewofragapproacheswithvect7124795219627167746/comments/](https://www
.linkedin.com/events/overviewofragapproacheswithvect7124795219627167746/comments/)

We're covering:

* Naive RAG
* Agent
 Assisted RAG
* Guardrails RAG
* Knowledge Graph RAG
* Time Based RAG
* Chunking approaches
* and more

Thanks!
```
---

     
 
all -  [ Please review my resume. I'm targeting Data Analyst/DS/ML roles. ](https://www.reddit.com/r/developersIndia/comments/17ow5rd/please_review_my_resume_im_targeting_data/) , 2023-11-08-0909
```
&#x200B;

https://preview.redd.it/no3jov9f3oyb1.jpg?width=1241&format=pjpg&auto=webp&s=32811364a253d55fd5ba98af20658ef23
6cfa12f

I haven't received any callbacks and I don't know where I'm going wrong. Any feedback is much appreciated!
```
---

     
 
all -  [ Trying for Full time Data Analytics/DS roles. No callbacks till now, need feedback ](https://www.reddit.com/r/resumes/comments/17ovu2m/trying_for_full_time_data_analyticsds_roles_no/) , 2023-11-08-0909
```
&#x200B;

https://preview.redd.it/2xdw7adywnyb1.jpg?width=1241&format=pjpg&auto=webp&s=1868d618f40f2cfbe9eaa17c0c275449a
ff34c76

I'm a 4th year Comp Sci student looking to break into DS, DA, ML roles  
The blue highlighted boxes are hyperli
nks embedded in the pdf (latex)  
Any feedback is much appreciated! Thanks in advance
```
---

     
 
all -  [ Improving bot's answering accuracy ](https://www.reddit.com/r/LangChain/comments/17ot2wn/improving_bots_answering_accuracy/) , 2023-11-08-0909
```
I am currently making a bot that can answer questions based on uploaded document. So we upload a pdf document, extract t
he text only, vectorize it, and upload the vector data to Pinecone. The AI model is GPT-3.5-turbo. It works now but I wa
nt to improve the bot's answering capability. The document is something like an education content. What steps should I d
o?
```
---

     
 
all -  [ Difference between Memory and {agent_scratchpad}? ](https://www.reddit.com/r/LangChain/comments/17on184/difference_between_memory_and_agent_scratchpad/) , 2023-11-08-0909
```
I don’t understand exactly how Memory works in Agents. Also, how is it different from {agent_scratchpad} appended to the
 prompts?
```
---

     
 
all -  [ Locally serving an LLM for chat task for family access? ](https://www.reddit.com/r/LocalLLaMA/comments/17ojvdw/locally_serving_an_llm_for_chat_task_for_family/) , 2023-11-08-0909
```
Hey, 

Just wondering if anyone is serving an open source LLM for chat, that is made available on your home network. 

L
ooking to do such, from homelab running proxmox. Did you dev your own UI with something like Streamlit, using LangChain 
or vanilla Python? A clean simple UI already available?

Thanks for any insight
```
---

     
 
all -  [ feed pdf files into an LLM for question answering tasks ](https://www.reddit.com/r/LocalLLaMA/comments/17oj372/feed_pdf_files_into_an_llm_for_question_answering/) , 2023-11-08-0909
```
hello there, we are working on chatbot that will act as an assistant for new cancer patients , we scraped around 50 pdfs
 containing faq with their answers, now we have no idea whats the best approach to make this model , one of the teamates
 suggested to use langchain , is it a good framework? can it implement other llms other than gpts ? 

also jsut to menti
on , we thought about fine tunning some model but we're rejecting this idea due to time nd computation limitations , so 
whats the best approach should we follow?
```
---

     
 
all -  [ Add a LangChain chatbot to my personal website? ](https://www.reddit.com/r/LangChain/comments/17oiz0i/add_a_langchain_chatbot_to_my_personal_website/) , 2023-11-08-0909
```
I have a website, [myname.com](https://myname.com), built using GitHub Pages and my personal url. I want to add a chatbo
t to it, using LangChain so I can augment the chatbot with a research paper I wrote. Is there a way I can do this using 
LangChain in python?
```
---

     
 
all -  [ Open Sourcing Llmtuner - An Experimental Framework for Finetuning Large Models Like Whisper and Llam ](https://www.reddit.com/r/LangChain/comments/17o9370/open_sourcing_llmtuner_an_experimental_framework/) , 2023-11-08-0909
```
Hi Folks,

Happy to share an open source side project I've been working on - [LLmtuner](https://github.com/promptslab/LL
Mtuner). It's a framework for finetuning large models like Whisper, Llama, Llama-2, etc with best practices like LoRA, Q
LoRA, through a sleek, scikit-learn-inspired interface.

As someone who works with Large Models a lot, I found myself wr
iting a lot of boilerplate code every time I wanted to finetune a model. Llmtuner aims to simplify the finetuning proces
s down to just 2-3 lines to get training started, similar to scikit-learn.  


https://preview.redd.it/ps26by2waiyb1.png
?width=1502&format=png&auto=webp&s=7b851ef022dcfada395f5a37ade70faf432355c9

&#x200B;

🚀 Features:

* 🧙‍♀️ Finetune stat
e-of-the-art LLMs like **Whisper, Llama wit**h minimal code
* 🔨 Built-in utilities for techniques like **LoRA and QLoRA*
*
* ✌ **Launch webapp demos** for your finetuned models with one click
* 💥 **Fast inference** without separate code
* **
🌐 Easy model sharing** and deployment coming soon

This is still experimental code I've been using for personal projects
. I thought others might find it useful too so decided to open-source it.

* Github : [https://github.com/promptslab/LLM
tuner](https://github.com/promptslab/LLMtuner)
* For quick demo : [Colab](https://colab.research.google.com/drive/1ia9Kv
qEGOxARtJScPBY6ccF8l41-w_l5?usp=sharing)

Contributions and feedback are very welcome! I hope it will be helpful in your
 research & projects. Have a good weekend, Thanks :)
```
---

     
 
all -  [ Is AutoGen the right tool for my use case? ](https://www.reddit.com/r/AutoGenAI/comments/17o5np5/is_autogen_the_right_tool_for_my_use_case/) , 2023-11-08-0909
```
I want to build a retrieval-augmented LLM app that uses a private knowledge base. I was experimenting with Langchain but
 then I found Autogen which I thought may be more suitable for my needs.  


What I want is basically an advanced custom
er chatbot that can analyze customer data and provide charts, inform the customer about my services, and call external A
PIs for additional functionality. So I thought maybe I could achieve that by having one agent that specializes in analyz
ing CSV data, one agent that specializes in consuming PDF documents for informing the user, etc., and orchestrating thes
e agents with Autogen. Basically, the app would find what agent is the best for a specific task the user needs and call 
it.  


But I want all the intermediary communication between the agents to be hidden from the user. The user should onl
y receive the final output and the experience should basically be like using ChatGPT.  


Would Autogen be the right too
l for this kind of task?
```
---

     
 
all -  [ Doubts on inference on large dataset ](https://www.reddit.com/r/LangChain/comments/17nw8zd/doubts_on_inference_on_large_dataset/) , 2023-11-08-0909
```
I created a big dataset of abstracts. I will use each abstract for a prompt template. My idea is to generate a pertinent
 question to each abstract. I am using the chain.apply method at the moment but this is sequential. I am sure there is a
 way to parallelize this process but it seems like I cannot come out with an idea nor find anything online. Can someone 
help me?
```
---

     
 
all -  [ Question about embeddings and vectordatabase ](https://www.reddit.com/r/LocalLLaMA/comments/17nw3dq/question_about_embeddings_and_vectordatabase/) , 2023-11-08-0909
```
So I have been trying to gather all the pieces needed to build a customer support chatbot with Llama2-13b-chat. As far a
s I understand it a vector database would be good for the information retrieval. 

Now my questions is: 
Let's say I use
 pgvector extension in a PostgreSQL database and make a vector database. 
Do I need to use something additional to do th
e embeddings ? 
Is pgvector with LangChain and then 'connecting' it to the LM enough?
Is it also viable to use pgvector 
with the Faiss library to create those embeddings? 

Or would another library/service make more sense?
 I am at a little
 bit of a loss here. 

Thank you very much for your help!
```
---

     
 
all -  [ I'm finding it hard to disable cache in NextJS13 ](https://www.reddit.com/r/nextjs/comments/17nvaci/im_finding_it_hard_to_disable_cache_in_nextjs13/) , 2023-11-08-0909
```
Nextjs13 is all good. But, it is caching fetch requests made in langchain/chromadb library, which gets annoying pretty q
uickly

&#x200B;

[requests made by library is cached](https://preview.redd.it/sq6fjnwj9eyb1.png?width=730&format=png&au
to=webp&s=6f9ff643c0e6e3ab786d422aab8fbbdab07b1ff8)

I added this on the page.tsx, where the request is made:

export co
nst dynamic = 'force-dynamic';

&#x200B;

But it doesn't work. 

Flow: The page(server component) has a client-component
 button(calls a server action).

The server action has some action with chromadb (vectorstore)
```
---

     
 
all -  [ Need to use langchain with llm hosted in private cloud as REST API ](https://www.reddit.com/r/LangChain/comments/17nsl5r/need_to_use_langchain_with_llm_hosted_in_private/) , 2023-11-08-0909
```
Guys, using langchain for a RAG application and I have an opensource llm downloaded and deployed as a rest API service t
o which I can send requests and receive response. How can I set llm to this api url like below:

llm = TogetherLLM(
    
model= 'togethercomputer/llama-2-7b-chat',
    temperature = 0.1,
    max_tokens = 1024
)
```
---

     
 
all -  [ Help with understanding use of LangChain in report generation ](https://www.reddit.com/r/LangChain/comments/17nqhya/help_with_understanding_use_of_langchain_in/) , 2023-11-08-0909
```
Hey y'all 👋

I wanted to ask about the implementation of an idea I have - I feel like it's straightforward, but I haven'
t had any luck in my research online and now feel more confused than ever on LLMs. 

I want to create an chatbot that, g
iven good samples of reports and the requirements for a new report, can write out the draft of a new report. I would lik
e to create a knowledge base that includes expert knowledge that would be helpful to writing the reports. I will instant
iate a local instance of an LLM and probably connect it to a frontend using Streamlit. 

I  imagine I need to use some f
orm of either LangChain or LlamaIndex to implement RAG, but I am not sure if it's finetuning or RAG at this point. I am 
lost on how to even approach this problem - I have read tons of articles and documentation, but feel lost. If anyone can
 provide any ideas or things I can research to learn this, that'd be awesome. 

Thanks in advance!
```
---

     
 
all -  [ Made a library for managing OpenAI rate limits which use actual OpenAI headers unlike pre-configured ](https://www.reddit.com/r/LangChain/comments/17npapw/made_a_library_for_managing_openai_rate_limits/) , 2023-11-08-0909
```
You can see code here: [https://github.com/alex4321/langchain-openai-limiter](https://github.com/alex4321/langchain-open
ai-limiter)

Library itself: [https://pypi.org/project/langchain-openai-limiter/](https://pypi.org/project/langchain-ope
nai-limiter/)

Motivation:

1. Default OpenAI python client (and langchain on top of it) does not deal with rate limits 
in any specific way - it just hit the error and retry. This way it consume budget and limits by every case then it hit e
rror.
2. All the rest of what I found was about having pre-configured PRM/TPM and some \`aiolimiter\`-like stuff inside.
 Much better approach - but the problem is that OpenAI have very different tiers for different users. Like by default gp
t-4 RPM is like 100 and TPM is like 10 000, but when you spent more during development of your project - it becomes like
 150 000 TPM (in my personal account). Surely we can change config and restart app or so...
3. But why should we do it w
hen OpenAI provides headers like 'well, you made this request, your initial TPM is X, after processing it - your current
 TPM is X1, your initial RPM is Y, your current RPM is Y1, TPM and RPM will reset in Z seconds' or so? So instead of pre
configured limits and counting on our side we can always have info about actual limits.
4. The problem is, however, that
 python OpenAI client do not provide obvious way to make callbacks accessing headers, and do not provide this info in th
e response itself. So neither it nor libraries on top of that don't use this headers limit - as well as most libraries w
hich do attempts to deal with limits, as far as I can see.

Implementation:

So basically my library consists of three c
omponents:

1. Hook system which inject itself inside openai. More or less clean for sync case - just use OpenAI's ready
 interface to attach post-response hook to http session. A bit greasy in async case - here it decorate openai's library 
insides (yet public) to attach the same logic.
   1. So after every OpenAI request it will know something like 'for this
 API key and model pair the remaining limit is X and will be resetter after Y timeout'
2. Wrappers on top of ChatOpenAI 
/ OpenAIEmbeddings which, before running request - calculate required token count, await for RPM & TPM limit to be avail
able and only after that do factual requests.
3. I also have wrappers which can consume multiple API keys and, before re
questing the underlying model - check which one of them have sufficient resources (so here I do random choice between th
e ones which have resources, or otherwise - wait for resource to be free).
```
---

     
 
all -  [ Where to find projects related to LangChain? ](https://www.reddit.com/r/LangChain/comments/17no1gf/where_to_find_projects_related_to_langchain/) , 2023-11-08-0909
```
I work for a development company from India, recently I have got a task to find projects related to LangChain as it has 
less competition. Where can I find some projects other than upwork and clutch?
```
---

     
 
all -  [ Langchain vs Llamaindex ](https://www.reddit.com/r/LangChain/comments/17nnclu/langchain_vs_llamaindex/) , 2023-11-08-0909
```
I saw Langchain has launched templates and llamaindex has been pushing out lots of use case templates and repos. As of e
arly Nov, what do you think is the sweet spots of use for langchain vs llamaindex? I used to work on the business side i
n financial services (not banks or insurance) and I see a lot of use cases for RAG (most) and agents (some). But I am a 
beginner on tech and find myself not sure where to spend my time learning. What do you think is the sweetspot for one vs
 another when it comes to the types of application, or cost and efficiency? What are the weaknesses as of early November
? I know things can change a month from now. Thank you.
```
---

     
 
all -  [ AutoGen v0.2.0b1 released ](https://www.reddit.com/r/AutoGenAI/comments/17nmnf9/autogen_v020b1_released/) , 2023-11-08-0909
```
[New release: v0.2.0b1](https://github.com/microsoft/autogen/releases/tag/v0.2.0b1) 

This is a beta release of v0.2.0.


## Highlights

* Switching to openai v1. Please read the [migration guide](https://microsoft.github.io/autogen/docs/Ins
tallation/#migration-guide-to-v02) and report bugs.
* Support async function execution & get\_human\_input.
* Improvemen
ts in documentation and notebooks.

Thanks to all the reviewers for the v0.2 migration. Thanks to [@aayushchhabra1999](h
ttps://github.com/aayushchhabra1999) [@bonadio](https://github.com/bonadio) [@marcgreen](https://github.com/marcgreen) a
nd other contributors!  
 

## What's Changed

* Update Installation.md by [@gagb](https://github.com/gagb) in [#456](ht
tps://github.com/microsoft/autogen/pull/456)
* Update FAQ with workaround for Issue [#251](https://github.com/microsoft/
autogen/issues/251) by [@marcgreen](https://github.com/marcgreen) in [#405](https://github.com/microsoft/autogen/pull/40
5)
* Fix typo in README.md by [@eltociear](https://github.com/eltociear) in [#481](https://github.com/microsoft/autogen/
pull/481)
* Fix/async function and tool execution by [@aayushchhabra1999](https://github.com/aayushchhabra1999) in [#87]
(https://github.com/microsoft/autogen/pull/87)
* Adding async support to get\_human\_input by [@bonadio](https://github.
com/bonadio) in [#466](https://github.com/microsoft/autogen/pull/466)
* Added example .txt file for agentchat\_langchain
 sample notebook by [@jasondotparse](https://github.com/jasondotparse) in [#373](https://github.com/microsoft/autogen/pu
ll/373)
* Fix : Typo by [@AaadityaG](https://github.com/AaadityaG) in [#506](https://github.com/microsoft/autogen/pull/5
06)
* Dev/v0.2 by [@sonichi](https://github.com/sonichi) in [#393](https://github.com/microsoft/autogen/pull/393)

## Ne
w Contributors

* [@marcgreen](https://github.com/marcgreen) made their first contribution in [#405](https://github.com/
microsoft/autogen/pull/405)
* [@aayushchhabra1999](https://github.com/aayushchhabra1999) made their first contribution i
n [#87](https://github.com/microsoft/autogen/pull/87)
* [@bonadio](https://github.com/bonadio) made their first contribu
tion in [#466](https://github.com/microsoft/autogen/pull/466)
* [@jasondotparse](https://github.com/jasondotparse) made 
their first contribution in [#373](https://github.com/microsoft/autogen/pull/373)
* [@AaadityaG](https://github.com/Aaad
ityaG) made their first contribution in [#506](https://github.com/microsoft/autogen/pull/506)

**Full Changelog**: [v0.1
.14...v0.2.0b1](https://github.com/microsoft/autogen/compare/v0.1.14...v0.2.0b1)

 
```
---

     
 
MachineLearning -  [ [D] Is this close enough to be usable? Need your inputs: Automated RAG testing tool. AI Data Pipelin ](https://www.reddit.com/r/MachineLearning/comments/17kkbm0/d_is_this_close_enough_to_be_usable_need_your/) , 2023-11-08-0909
```
Hey there, Redditors! 

I'm back with the latest installment on creating dependable AI data pipelines for real-world pro
duction. 

If you've been following along, you know I'm on a mission to move beyond the '[thin OpenAI wrapper](https://t
opoteretes.notion.site/Going-beyond-Langchain-Weaviate-and-towards-a-production-ready-modern-data-platform-7351d77a1eba4
0aab4394c24bef3a278?pvs=4)' trend and tackle the challenges of building robust data pipelines. 

With 18 months of hands
-on experience and many user interviews, I realized that with the probabilistic nature of systems, we need better\_testi
ng.gpt:

  
**1. As you build you should test**  
The world of AI is a fast-moving one, and we've realized that just wor
king on systems is not an optimal design choice. By the time your product ships, it might already be using outdated tech
nology. So, what's the lesson here? Embrace change, test along, but be prepared to switch pace.  
**2. No Best Practices
 Yet for RAGs**  
In this rapidly evolving landscape, there are no established best practices. You'll need to make educa
ted bets on tools and processes, knowing that things will change. With the RAG testing tool, I tried allowing for testin
g many potential parameter combinations **automatically**  
**3. Testing Frameworks**  
If your generative AI product do
esn't have users giving feedback, then you are building in isolation. I used [Deepeval](https://github.com/confident-ai/
deepeval) to generate test sets, and they will soon support synthetic test set generation  
**4. Infographics only go so
 far**  
AI researchers and data scientists, while brilliant, end up in a loop of pursuing Twitter promotional content. 
New ways are promoted via new content pieces, but ideally, we need something above simple tracing but less than full-fle
dged analytics. To do this, I stored test outputs in Postgres and created a Superset instance to visualize the results  

**5. Bridging the Gap between VectorDBs**  
There's a noticeable number of Vector DBs. To ensure smooth product develop
ment, we need to be able to switch to best best-performing one, especially since user interviews signal that they might 
start deteriorating after loading 50 million rows

&#x200B;

Github repo is [here](https://topoteretes.notion.site/Going
-beyond-Langchain-Weaviate-Level-3-towards-production-e62946c272bf412584b12fbbf92d35b0?pvs=4)  


Next steps:  
I have q
uestions for you: 

1. What variables do you change when building RAGs?
2. What is the set of strategies I should add to
 the solution? (parent-son etc.)
3. How can I improve it in general? 
4. Is anyone  interested in a leaderboard for best
 parameter configs?

Check out the blog post:

[Link to part 3](https://topoteretes.notion.site/Going-beyond-Langchain-W
eaviate-Level-3-towards-production-e62946c272bf412584b12fbbf92d35b0?pvs=4)

  
*Remember to give this post an upvote if 
you found it insightful!*  
*And also star our* [*Github repo*](https://github.com/topoteretes/PromethAI-Memory)
```
---

     
 
MachineLearning -  [ [D] Relevance Extraction in RAG Pipelines ](https://www.reddit.com/r/MachineLearning/comments/17k6iha/d_relevance_extraction_in_rag_pipelines/) , 2023-11-08-0909
```
I came across this interesting problem in RAG, what I call **Relevance Extraction**.

After retrieving relevant document
s (or chunks), these chunks are often large and may contain several portions **irrelevant** to the query at hand. Stuffi
ng the entire chunk into an LLM prompt impacts token-cost as well as response accuracy (distracting the LLM with irrelev
ant text), and and can also cause bumping into context-length limits.

So a critical step in most pipelines is **Relevan
ce Extraction**: use the LLM to extract **verbatim** only the portions relevant to the query. This is known by other nam
es, e.g. LangChain calls it Contextual Compression, and the RECOMP paper calls it Extractive Compression [https://twitte
r.com/manelferreira\_/status/1713214439715938528](https://twitter.com/manelferreira_/status/1713214439715938528)

Thinki
ng about how best to do this, I realized it is **highly inefficient** to simply ask the LLM to 'parrot' out relevant por
tions of the text: this is obviously slow, and also consumes valuable token generation space and can cause you to bump i
nto context-length limits (and of course is expensive, e.g. for gpt4 we know generation is 6c/1k tokens vs input cost of
 3c/1k tokens).

I realized the best way (or at least a good way) to do this is to **number** the sentences and have the
 LLM simply spit out the relevant sentence **numbers.** Langroid's unique Multi-Agent + function-calling architecture al
lows an elegant implementation of this, in the RelevanceExtractorAgent ([https://github.com/langroid/langroid/blob/main/
langroid/agent/special/relevance\_extractor\_agent.py](https://github.com/langroid/langroid/blob/main/langroid/agent/spe
cial/relevance_extractor_agent.py)).  The agent annotates the docs with sentence numbers, and instructs the LLM to pick 
out the **sentence-numbers** relevant to the query, rather than whole sentences using a function-call (SegmentExtractToo
l [https://github.com/langroid/langroid/blob/main/langroid/agent/tools/segment\_extract\_tool.py](https://github.com/lan
groid/langroid/blob/main/langroid/agent/tools/segment_extract_tool.py)), and the agent's function-handler interprets thi
s message and strips out the indicated sentences by their numbers. To extract from a set of passages, langroid automatic
ally does this async + concurrently so latencies in practice are much, much lower than the sentence-parroting approach.


\[FD -- I am the lead dev of Langroid - [https://github.com/langroid/langroid](https://github.com/langroid/langroid))


I thought this **numbering** idea is a fairly obvious idea in theory, so I looked at LangChain's equivalent `LLMChainExt
ractor` (they call this Contextual Compression [https://python.langchain.com/docs/modules/data\_connection/retrievers/co
ntextual\_compression?ref=blog.langchain.dev](https://python.langchain.com/docs/modules/data_connection/retrievers/conte
xtual_compression?ref=blog.langchain.dev)) and was surprised to see it is the simple '**parrot**' method, i.e. the LLM w
rites out whole sentences verbatim from its input. I thought it would be interesting to compare Langroid vs LangChain, y
ou can see it in this Colab: [https://colab.research.google.com/drive/1RDPCR2xNuBffcmpUuPIXYDRG3SXIJC5F](https://colab.r
esearch.google.com/drive/1RDPCR2xNuBffcmpUuPIXYDRG3SXIJC5F)

On the specific example in the notebook, the Langroid **num
bering** approach is 22x faster and 36% cheaper (with gpt4) than LangChain's **parrot** method (I promise this name is *
not* inspired by their logo :). See table below.

&#x200B;

[Relevance Extraction: Langroid vs LangChain](https://previe
w.redd.it/1m7u6ulq8fxb1.png?width=1108&format=png&auto=webp&s=d2f35cf5db07e2e699baa54b274ffa60833e924a)

&#x200B;

I won
der if anyone had thoughts on relevance extraction, or other approaches. At the very least, I hope langroid's implementa
tion is useful to you -- you can use the `DocChatAgent.get_verbatim_extracts()` ([https://github.com/langroid/langroid/b
lob/main/langroid/agent/special/doc\_chat\_agent.py#L804](https://github.com/langroid/langroid/blob/main/langroid/agent/
special/doc_chat_agent.py#L804)) as part of your pipeline, regardless of whether you are using Langroid for your entire 
system or not.

&#x200B;
```
---

     
 
MachineLearning -  [ [R] Model Troubles ](https://www.reddit.com/r/MachineLearning/comments/17ikh2u/r_model_troubles/) , 2023-11-08-0909
```
So i’m working on a model that diagnoses alzheimer’s disease and suggests medication depending on how severe the symptom
s might have become 
I’m using the Openai API and Langchain.

But it’s dumb and it doesn’t learn (
Me: I forgot my keys 
at home
Model: Yup, Alzheimer’s)
How do i incorporate the actual machine learning

Edit: I didn’t choose this project my
 supervisor did and she barely knows anything about the topic or how to approach it
```
---

     
 
MachineLearning -  [ [P] NexaAgent: A highly efficient multi-task PDF tool for all your needs | backed by AutoGen ](https://www.reddit.com/r/MachineLearning/comments/17eajz2/p_nexaagent_a_highly_efficient_multitask_pdf_tool/) , 2023-11-08-0909
```
Just a quick open-source project recently submitted to huggingface backed by AutoGen. Share this initial version with yo
u guys!

[NexaAgent 0.0.1](https://huggingface.co/spaces/xuyingliKepler/nexaagent) offers a straightforward solution for
 handling PDFs.

* Users can easily upload any PDF, regardless of its size.
* The tool emphasizes accuracy, minimizing d
iscrepancies in PDF processing.

At its core, NexaAgent is backed by the AutoGen and LangChain frameworks. AutoGen facil
itates multi-agent interactions for task execution, while LangChain bridges LLMs with external data sources. Together, t
hese technologies ensure NexaAgent's robust and precise PDF management capabilities.

https://preview.redd.it/kwgo3phnav
vb1.jpg?width=1440&format=pjpg&auto=webp&s=1c5fbc566938d60d5c43802aff3a0690821e1c79
```
---

     
 
MachineLearning -  [ [D] Is lang chain the right solution? ](https://www.reddit.com/r/MachineLearning/comments/17coyym/d_is_lang_chain_the_right_solution/) , 2023-11-08-0909
```
Hello, I would love to have an LLm that can provide answers (in chat format) based some of the sql db  data we have. Wan
t it for an internal company project. I am by no means an expert but decent in programming and want to build a system to
 get answers in chat format. My understanding is that training LLMs ground up is prohibitively expensive and langchains 
are sort of hybrid , efficient solutions. 

Please suggest any other solutions. Also would Langchain being a company and
 not open source pose a problem in terms of copyrights? Thanks!
```
---

     
 
MachineLearning -  [ [P] building a D&D NPC ](https://www.reddit.com/r/MachineLearning/comments/17clyw6/p_building_a_dd_npc/) , 2023-11-08-0909
```
Hey everyone,

I'm learning ML but i'm barely scratching the terminologies. 2 years ago I couldn't code anything but wit
h school (python,sql and R) I learned fundamentals. I also have access to code academy.  My current program is very mach
ine learning/deep learning focused.

On the side I DM a d&d game. Within the context of the world (eberron) robots are c
ommon. With my ADHD and being a new DM I want to outsource lore questions might have (that I would have to look up and s
low down the game).

The concept is to have a GUI and have the player interact with the chat bot. I've gotten to a proof
 of concept workflow. On Google colab. Thanks to langchain I managed to ingest pdfs and a url. Make then a directory, Em
bedded the text, bring it into a vector dB. Have the llm pull from the vector. Answer the question.

Now I don't know wh
at to do. I tried to bring the colab notebook onto Google cloud. But now cloud is becoming a rabbit home with vertex and
 docAI...and I don't want to deep dive into that, if it's a outside the scope of this 'project'

I'd appreciate any advi
ce, links...etc. 


I got a limited success in botpress using a single pdf. It works but feel unsatisfying.
N8N looks pr
omising but if it's not intuitive then I don't want to go down that road.


If I posted in the wrong group please direct
 me to the correct one.
```
---

     
 
MachineLearning -  [ [D] Exploring Methods to Improve Text Chunking in RAG Models (and other things...) ](https://www.reddit.com/r/MachineLearning/comments/179j7l3/d_exploring_methods_to_improve_text_chunking_in/) , 2023-11-08-0909
```
Hello everyone,

I'm currently working on Retrieval Augmented Generation (RAG) models and have developed a custom chunki
ng function, as I found the methods in LangChain not entirely satisfactory.

I'm keen on exploring other methods, algori
thms (related to NLP or otherwise), and models to enhance text chunking in RAG. There are many RAG implementations out t
here, but I've noticed a lack of focus on improving chunking performance specifically.

Are there any other promising ap
proaches beyond my current pipeline, which consists of a bi-encoder (retriever), cross-encoder (reranker), and a Large L
anguage Model (LLM) for interactions?

For queries, I'm using both traditional and HyDE (Hypothetical Document Embedding
) approaches in the retrieval phase, and sending the top 'n' results of both similarity search to the reranker.

I've al
so tried using an LLM to convert the query into a series of 10-20 small phrases or keywords, which are then used as the 
query for the retriever model. However, the results vary depending on the LLM used. To generate good keywords (with a no
t extractive approach) , I had to  use a 'CoT' prompt, instructing the model to  write self-instruct, problem analysis a
nd reasonings before generating the required keywords. But this approach use lots of tokens, and requires careful scrapi
ng to ensure the model has used the right delimiter to separate reasoning and the actual answer.

I'm also planning to m
odify the text used to generate embeddings, while returning the original text after the recall phase. But this is still 
a work in progress and scaling it is proving to be a challenge. If anyone has any tips or experience with this, I'd appr
eciate your input.

I'd be grateful for any resources, repositories, libraries, or existing implementations of novel chu
nking methods that you could share. Or we could just discuss ideas, thoughts, or approaches to improve text chunking for
 RAG here.

Thanks in advance for your time!
```
---

     
 
MachineLearning -  [ [News] AI & ML conference in San Francisco [Special discount code for this subreddit] ](https://www.reddit.com/r/MachineLearning/comments/1771m35/news_ai_ml_conference_in_san_francisco_special/) , 2023-11-08-0909
```
I work for this database company SingleStore and we are hosting a AI & ML conference in San Francisco on 17th of October
, 2023.

It is an in-person conference with amazing speakers line-up like Harrison Chase, co-founder and CEO of LangChai
n and many more. We will have hands-on workshops, swags giveaway and much more.

I don't know if it makes sense to share
 this but I believe it might help some of you near San Francisco to go and meet the industry leaders and network with ot
her data engineering folks.

Use my discount coupon code 'PAVAN100OFF' to avail 100% off on the ticket price. (the origi
nal ticket price is $199)

[Get your tickets now!](https://singlestore.com/now)
```
---

     
 
MachineLearning -  [ [D] Best way to validate llm prompts? ](https://www.reddit.com/r/MachineLearning/comments/176vnxh/d_best_way_to_validate_llm_prompts/) , 2023-11-08-0909
```
We have a platform for data analytics which uses a very simple dsl to generate charts.  
We have been experimenting with
 llms to use natural language that gets translated into this dsl and hence generates charts.

This is working pretty goo
d.  
The stack is langchain with openai api. (don't have much experience with llms, it's a prototype to get a feel for i
t)

The question is what is the best way to limit the options user can type in as a prompt.  
Basically the the only all
owed things should be: 'What is the X, Y over 10 days period for this or that?'  
I don't want users to ask questions li
ke when did we first land on the moon.

Is it something that is possible to do at all without additional tooling?  
We p
robably don't want to train another model to classify the prompt as valid or invalid or something similar.
```
---

     
 
deeplearning -  [ Error with Mistral 7B model in ConversationalRetrievalChain ](https://www.reddit.com/r/deeplearning/comments/179vvou/error_with_mistral_7b_model_in/) , 2023-11-08-0909
```
 I'm encountering an issue while using the Mistral 7B model in a ConversationalRetrievalChain. When I input a question, 
such as 'What is the highest GDP?', I receive an error and after that the model generates a random response as output wh
ich is not relevant to the Input query. It seems that the number of tokens in the input exceeds the maximum context leng
th. 

Here's the relevant code: 

 

>`from langchain.document_loaders.csv_loader import CSVLoader`  
`from langchain.te
xt_splitter import RecursiveCharacterTextSplitter`  
`from langchain.embeddings import HuggingFaceEmbeddings`  
`from la
ngchain.vectorstores import FAISS`  
`from langchain.llms import CTransformers`  
`from langchain.memory import Conversa
tionBufferMemory`  
`from langchain.chains import ConversationalRetrievalChain`  
`import sys`  
`DB_FAISS_PATH = 'vecto
rstore/db_faiss'`  
`loader = CSVLoader(file_path='data/World Happiness Report 2022.csv', encoding='utf-8', csv_args={'d
elimiter': ','})`  
`data = loader.load()`  
`print(data)`  
`# Split the text into Chunks`  
`text_splitter = Recursive
CharacterTextSplitter(chunk_size=500, chunk_overlap=20)`  
`text_chunks = text_splitter.split_documents(data)`  
`print(
len(text_chunks))`  
`# Download Sentence Transformers Embedding From Hugging Face`  
`embeddings = HuggingFaceEmbedding
s(model_name = 'sentence-transformers/all-MiniLM-L6-v2')`  
`# COnverting the text Chunks into embeddings and saving the
 embeddings into FAISS Knowledge Base`  
`docsearch = FAISS.from_documents(text_chunks, embeddings)`  
`docsearch.save_l
ocal(DB_FAISS_PATH)`  
  
>  
>`#query = 'What is the value of GDP per capita of Finland provided in the data?'`  
`#doc
s = docsearch.similarity_search(query, k=3)`  
`#print('Result', docs)`  
`llm = CTransformers(model='models/mistral-7b-
v0.1.Q4_0.gguf',`  
 `model_type='llama',`  
 `max_new_tokens=1000,`  
 `temperature=0.1)`  
`qa = ConversationalRetriev
alChain.from_llm(llm, retriever=docsearch.as_retriever())`  
`while True:`  
 `chat_history = []`  
 `#query = 'What is 
the value of  GDP per capita of Finland provided in the data?'`  
 `query = input(f'Input Prompt: ')`  
 `if query == 'e
xit':`  
 `print('Exiting')`  
 `sys.exit()`  
 `if query == '':`  
 `continue`  
 `result = qa({'question':query, 'chat
_history':chat_history})`  
 `print('Response: ', result['answer'])`

 

**Problem Statement:**

I'm trying to utilize t
he Mistral 7B model for a ConversationalRetrievalChain, but I'm encountering an error related to token length:

Number o
f tokens (760) exceeded maximum context length (512).

**Context:**

I'm working on a project that involves using Mistra
l 7B to answer questions based on a dataset. The dataset contains information about the World Happiness Report 2022.

**
Steps Taken:**

* Loaded and preprocessed the dataset using langchain.
* Initialized Mistral 7B with the following param
eters:
* Model: 'models/mistral-7b-v0.1.Q4\_0.gguf'
* Model Type: 'llama'
* Max New Tokens: 1000
* Temperature: 0.1
* Se
t up a ConversationalRetrievalChain with Mistral 7B as the language model and a retriever based on FAISS.

**Expected Ou
tput:**

I expect to receive a meaningful response from Mistral 7B based on the input query.

**Additional Information:*
*

I'm using Python and relevant libraries for this project. The dataset I'm working with is from the World Happiness Re
port 2022.

**Environment Details:**

* Python version: 3.11.4 
* Relevant libraries and versions: 

langchain 

ctransf
ormers 

sentence-transformers 

faiss-cpu
```
---

     
 
deeplearning -  [ Error with Mistral 7B model in ConversationalRetrievalChain. ](https://www.reddit.com/r/deeplearning/comments/179vsif/error_with_mistral_7b_model_in/) , 2023-11-08-0909
```
I'm encountering an issue while using the Mistral 7B model in a ConversationalRetrievalChain. When I input a question, s
uch as 'What is the highest GDP?', I receive an error and after that the model generates a random response as output whi
ch is not relevant to the Input query. It seems that the number of tokens in the input exceeds the maximum context lengt
h.

Here's the relevant code:

>from langchain.document\_loaders.csv\_loader import CSVLoader  
>  
>from langchain.text
\_splitter import RecursiveCharacterTextSplitter  
>  
>from langchain.embeddings import HuggingFaceEmbeddings  
>  
>fr
om langchain.vectorstores import FAISS  
>  
>from langchain.llms import CTransformers  
>  
>from langchain.memory impo
rt ConversationBufferMemory  
>  
>from langchain.chains import ConversationalRetrievalChain  
>  
>import sys  
>  
>  

>  
>DB\_FAISS\_PATH = 'vectorstore/db\_faiss'  
>  
>loader = CSVLoader(file\_path='data/World Happiness Report 2022.c
sv', encoding='utf-8', csv\_args={'delimiter': ','})  
>  
>data = loader.load()  
>  
>print(data)  
>  
>  
>  
>\# Sp
lit the text into Chunks  
>  
>text\_splitter = RecursiveCharacterTextSplitter(chunk\_size=500, chunk\_overlap=20)  
> 
 
>text\_chunks = text\_splitter.split\_documents(data)  
>  
>  
>  
>print(len(text\_chunks))  
>  
>  
>  
>\# Downlo
ad Sentence Transformers Embedding From Hugging Face  
>  
>embeddings = HuggingFaceEmbeddings(model\_name = 'sentence-t
ransformers/all-MiniLM-L6-v2')  
>  
>  
>  
>\# COnverting the text Chunks into embeddings and saving the embeddings in
to FAISS Knowledge Base  
>  
>docsearch = FAISS.from\_documents(text\_chunks, embeddings)  
>  
>  
>  
>docsearch.save
\_local(DB\_FAISS\_PATH)  
>  
>  
>  
>  
>  
>\#query = 'What is the value of GDP per capita of Finland provided in th
e data?'  
>  
>  
>  
>\#docs = docsearch.similarity\_search(query, k=3)  
>  
>  
>  
>\#print('Result', docs)  
>  
>
  
>  
>llm = CTransformers(model='models/mistral-7b-v0.1.Q4\_0.gguf',  
>  
>model\_type='llama',  
>  
>max\_new\_toke
ns=1000,  
>  
>temperature=0.1)  
>  
>  
>  
>qa = ConversationalRetrievalChain.from\_llm(llm, retriever=docsearch.as\
_retriever())  
>  
>  
>  
>while True:  
>  
>chat\_history = \[\]  
>  
>\#query = 'What is the value of  GDP per cap
ita of Finland provided in the data?'  
>  
>query = input(f'Input Prompt: ')  
>  
>if query == 'exit':  
>  
>print('E
xiting')  
>  
>sys.exit()  
>  
>if query == '':  
>  
>continue  
>  
>result = qa({'question':query, 'chat\_history':
chat\_history})  
>  
>print('Response: ', result\['answer'\])

 

**Problem Statement:**

I'm trying to utilize the Mis
tral 7B model for a ConversationalRetrievalChain, but I'm encountering an error related to token length:

Number of toke
ns (760) exceeded maximum context length (512).

**Context:**

I'm working on a project that involves using Mistral 7B t
o answer questions based on a dataset. The dataset contains information about the World Happiness Report 2022.

**Steps 
Taken:**

* Loaded and preprocessed the dataset using langchain.
* Initialized Mistral 7B with the following parameters:

* Model: 'models/mistral-7b-v0.1.Q4\_0.gguf'
* Model Type: 'llama'
* Max New Tokens: 1000
* Temperature: 0.1
* Set up a
 ConversationalRetrievalChain with Mistral 7B as the language model and a retriever based on FAISS.

**Expected Output:*
*

I expect to receive a meaningful response from Mistral 7B based on the input query.

**Additional Information:**

I'm
 using Python and relevant libraries for this project. The dataset I'm working with is from the World Happiness Report 2
022.

**Environment Details:**

Python version: 3.11.4 Relevant libraries and versions: langchain ctransformers sentence
-transformers faiss-cpu

&#x200B;
```
---

     
 
deeplearning -  [ Free courses to learn about Large Language Models and building AI projects ](https://www.reddit.com/r/deeplearning/comments/178zu2u/free_courses_to_learn_about_large_language_models/) , 2023-11-08-0909
```
[**LangChain for LLM Application Development by Andrew Ng**](https://www.deeplearning.ai/short-courses/langchain-for-llm
-application-development/): Apply LLMs to your proprietary data to build personal assistants and specialized chatbots. 


[**Full Stack LLM Bootcamp**](https://fullstackdeeplearning.com/llm-bootcamp/): Learn best practices and tools for buil
ding LLM-powered apps 

[**Stanford CS324**](https://stanford-cs324.github.io/winter2022/): In this course, students wil
l learn the fundamentals about the modeling, theory, ethics, and systems aspects of large language models, as well as ga
in hands-on experience working with them. 

[**LangChain & Vector Databases in Production**](https://learn.activeloop.ai
/courses/langchain): Learn how to leverage LangChain, a robust framework for building applications with LLMs, and explor
e Deep Lake, a groundbreaking vector database for all AI data. 

[**Stanford CS25**](https://web.stanford.edu/class/cs25
/): In this course, learn how transformers work, and dive deep into the different kinds of transformers and how they're 
applied in different fields. 

[**LLMOps Space Discord**](https://llmops.space/discord): LLMOps Space is a global commun
ity for LLM practitioners.
```
---

     
