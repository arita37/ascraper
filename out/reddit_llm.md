 
all -  [ AI Infrastructure needs more open-source engagement ](https://www.reddit.com/r/opensource/comments/17qzrfa/ai_infrastructure_needs_more_opensource_engagement/) , 2023-11-09-0909
```
The open-source community has always been at the forefront of innovation, but it feels like we are lagging when it comes
 to AI. 

  
AI is a generational shift for dev and tech and there's a serious risk of the big guys are running away wit
h the space and monopolizing it.   

  
I maintain CopilotKit, an open-source AI library, and while we're good interest,
 95% of it is coming from enterprise and people already in AI, and not the typical open-source community.    


What hap
pens in these early days will be pivotal to what the space looks like in years to come. Don't sleep on AI-infra! 

  
**
Some great OS AI libraries you can support & contribute to:**   
1. [CopilotKit](https://github.com/RecursivelyAI/Copilo
tKit) (My library):  Infra for embedding an AI Copilot into any app (react).   
2. [Pezzo.ai](https://github.com/pezzola
bs/pezzo): Prompt management & observability.   
3. [SwirlSearch](https://github.com/swirlai/swirl-search): LLM-powered 
search & synthesis.  
4. [LangChain](https://github.com/langchain-ai/langchain): build apps with LLMs. String together L
LM chains + other programs.   

```
---

     
 
all -  [ I'm currently looking for full-time jobs or summer internships, any advice? On a greencard so cant w ](https://i.redd.it/sc11s8qxp6zb1.png) , 2023-11-09-0909
```

```
---

     
 
all -  [ Full Document Understanding with RAG—Need Insights ](https://www.reddit.com/r/LangChain/comments/17qsmhs/full_document_understanding_with_ragneed_insights/) , 2023-11-09-0909
```
Hey everyone,

I'm working on a RAG project and hitting a snag. RAG only dissects text chunk by chunk, missing the 'big 
picture' of the entire document or diving deep into the text. Essentially, I'm looking to create a recursive RAG that gr
asps the full meaning and structure of the whole document, not just isolated snippets.

Any ideas on how to approach thi
s or resources you could point me toward?

Thanks!
```
---

     
 
all -  [ my Knowledge based chatbot is answering sometimes from the pdfs and other times from the gpt itself. ](https://www.reddit.com/r/LangChain/comments/17qs4le/my_knowledge_based_chatbot_is_answering_sometimes/) , 2023-11-09-0909
```
Hello everyone, I have a problem with my project. Actually i am working on chatbot knowledge base using langchain and pi
necone to answer questions only from the pdf imported . but it doesnt answer specifically from the document and sometime
s if something is not in the doc and i ask it it answers like it is chatgpt.  
```
---

     
 
all -  [ Chunking and storing structured data and vectors for RAG ](https://www.reddit.com/r/LocalLLaMA/comments/17qqokv/chunking_and_storing_structured_data_and_vectors/) , 2023-11-09-0909
```
TL:DR is there an example someone can point me to for RAG with highly structured documents where the agent returns conve
rsation along with cross references to document paragraphs or sections? Input= long text document (~500-1000 page), outp
ut is Q/A with references to document paragraph, page, or other simple cross reference.

I've been looking into RAG in m
y (extremely limited) spare time for a few months now but I'm getting hung up on vector databases. It may be due to the 
fact that my use case revolves around highly structured specification documents where I desire to be able to recover sec
tion and paragraph references in a QA session with a rag assistant. 

Most off-the-shelf solutions seem to not care what
 your data looks like and just provides a black box solution for data chunking and vectoring, like having a single HTML 
link for a website for the source information and magically it works. This confuses me because langchain has a great lea
rning path that includes quite a bit of focus on proper data chunking and vector database structuring, then literally ev
ery example treats the chunking and vector store step as an afterthought. I don't like to do something I don't understan
d so I've been focused more on creating a database for my data that makes sense in my brain. 

I have successfully creat
ed a local vector database (sqlite) with SBERT that returns paragraph numbers with a similarity search but I haven't bri
dged that to feeding those results into an LLM.

Am I thinking too hard about this? Are the off the shelf rag solutions 
able to handle the paragraph numbers without me explicitly trying to cram them into a database structure? Or am I on the
 right path, and I should continue with the database that makes sense to me and keep figuring out how to implement the L
LM step after the vector search?

I started looking at llamaindex, then Langchain, now autogen. But my spare time is lim
ited enough that I haven't implemented anything with any of these, only a (successful) sbert similarity search which did
n't use any of these. If someone has an example for structured documents where the q/a provides cross-references, I'd re
ally appreciate it.
```
---

     
 
all -  [ New Updates Made Vector Databases Redundant ](https://www.reddit.com/r/LangChain/comments/17qq7q6/new_updates_made_vector_databases_redundant/) , 2023-11-09-0909
```
The new retrieval function allows you to train the AI on your documents. 

Will this impact vector databases?
```
---

     
 
all -  [ Is there anyway to collect and process user feedback from AI chat locally? ](https://www.reddit.com/r/LangChain/comments/17qluy1/is_there_anyway_to_collect_and_process_user/) , 2023-11-09-0909
```
I have built a chatbot using  llama2, langchain and chainlit. I am trying to collect user feedback on the answers and an
alyze them. 

Is there is a way I can implement this feedback structure locally, without using hosted systems like langs
mith or trurbricks?

&#x200B;
```
---

     
 
all -  [ Ignore broken PDFs in DirectoryLoader ](https://i.redd.it/w0mpa9ia34zb1.jpg) , 2023-11-09-0909
```
I’m working on a large scale RAG pipeline (1000 pdf files). The program will interrupted because of the errors in PDFloa
der. I tried to load PDFs individually by a For loop using PyPDFLoader but the latency is too much. Is there any reliabl
e way to do this ?
```
---

     
 
all -  [ Hugging Face Hub LLMs keep timing out ](https://www.reddit.com/r/LangChain/comments/17qj9a0/hugging_face_hub_llms_keep_timing_out/) , 2023-11-09-0909
```
None of the 'Hugging Face Hub' LLMs works from LangChain. I get a timeout error after waiting for a very long time. I'm 
not the only one, as it has been reported [here](https://stackoverflow.com/questions/76265748/indefinite-wait-while-usin
g-langchain-and-huggingfacehub-in-python) and [here](https://github.com/langchain-ai/langchain/issues/3275), and a few m
onths since those reports, the problem persists. 

The only LLMs that work reliably without timing out are the ones from
 OpenAI. Considering that, I'm failing to see the point of LangChain instead of using the OpenAI Python library directly
. 

Has anyone else faced this problem, and did you figure out how to make other LLMs work?
```
---

     
 
all -  [ Trying new jina-embeddings-v2-base-en model ](https://www.reddit.com/r/LangChain/comments/17qj92b/trying_new_jinaembeddingsv2baseen_model/) , 2023-11-09-0909
```
was trying to use jina embeddings to create a vector database in chroma, but got errors. This is the detailed implementa
tion -  
\## loaded the jina model -

from langchain.embeddings import HuggingFaceEmbeddings

model\_name = 'jinaai/jina
-embeddings-v2-base-en'  
model\_kwargs = {'device': 'cuda'}  
encode\_kwargs = {'normalize\_embeddings': True}  
model 
= HuggingFaceEmbeddings(  
model\_name=model\_name,  
model\_kwargs=model\_kwargs,  
encode\_kwargs=encode\_kwargs  
)


chroma settings -

from chromadb.config import Settings

error in the above step -tings(  
anonymized\_telemetry=False, 
 
is\_persistent=True,  
)

Creating the persist directory -

persist\_directory = 'db'  
embedding = model

vectordb = 
Chroma.from\_documents(documents=texts,  
embedding=embedding,  
persist\_directory=persist\_directory,  
client\_settin
gs=CHROMA\_SETTINGS)

error in above step -

Expected EmbeddingFunction.call to have the following signature: odict\_key
s(\['self', 'input'\]), got odict\_keys(\['self', 'args', 'kwargs'\])

Can anyone help to solve it?
```
---

     
 
all -  [ How to turn a promising software library into a business model? ](https://www.reddit.com/r/startups/comments/17qixxq/how_to_turn_a_promising_software_library_into_a/) , 2023-11-09-0909
```
Hi all, I have had an interesting idea that potentially could change the way we interact with LLMs. I am currently writi
ng a prototype. While I believe the idea has a similar potential like Langchain or Haystack, what I am missing is an ide
a how to monetize it. Sure, I can create a library and open source it. But then what? I may gain some kudos, but that's 
not a business model, it's just a library. Selling the library for money will not work. I could try to get a patent arou
nd it, but I think that's quite useless and also takes way too long. I expect that in few months someone will come up wi
th a similar idea like mine independently.  
Does anyone have any blueprints how to turn a software library (comparable 
to Langchain) into a business model?
```
---

     
 
all -  [ Vertexaisearch retrieval with retrieval qa with sources chain ](https://www.reddit.com/r/LangChain/comments/17qidql/vertexaisearch_retrieval_with_retrieval_qa_with/) , 2023-11-09-0909
```
I've uploaded a CSV file into vector ai portal in search and conversation app. Then I'm using retriever to initiall quer
y the list of documents and using qachain with prompt template.

But, I'm getting an error which says 
' Valueerror: doc
ument prompt requires documents to have metadata variables  : [source] Received doc with missing metadata: [source] '

H
ow to add source as metadata to the CSV and what values to populate this with ?
```
---

     
 
all -  [ Image generation with langchain ](https://www.reddit.com/r/LangChain/comments/17qhrhs/image_generation_with_langchain/) , 2023-11-09-0909
```
Hi,

I'm trying to make kids stories generator with text and image on langchain. No issue with text, it's pretty straigh
t forward. But things gets harder when I want to generate no dommesques images. The only way I find is the dall-e image 
generator but it's really messy. I wasn't able to understand how this works even when looking in the code: https://githu
b.com/langchain-ai/langchain/blob/master/libs/langchain/langchain/utilities/dalle_image_generator.py

It doesn't seem to
 use a dedicated endpoint and it's not clear how to select the model...

What would be the alternative to generates imag
es with langchain ?
```
---

     
 
all -  [ very confused with langchain ](https://www.reddit.com/r/LangChain/comments/17qd4ok/very_confused_with_langchain/) , 2023-11-09-0909
```
Is it just me, or langchain is very confusing?

First I get totally confused between typescript and python documentation
. Which is kind of stupid, but there are no distinction visually between two set of documentation.  I google something, 
and it gives me a link, and it is not immediately obvious that it is the other language, until you reach the code. And t
he implementation is not quite parallel. It seems there are differences between two implementations.

&#x200B;

Then the
re are competing concepts like chains vs agents. Which I have read the difference, but still very close in practice.

&#
x200B;

Or I thought  `prompt | llm` is the same as `LLMChain(llm=llm, prompt=prompt)` but apparently not.

&#x200B;

Ho
w do you really learn this thing for good?
```
---

     
 
all -  [ Collection and pg_vector in Supabase ](https://www.reddit.com/r/Supabase/comments/17qcnim/collection_and_pg_vector_in_supabase/) , 2023-11-09-0909
```
Hi all --

Are collections a part of pgvector in supabase at all? I know you reference one when using the Pgvector vecto
r vector store in langchain, and I assume a collection is the same as an index in pinecone. So I'm curious of an analogo
us solution with Supabase. 

Please correct me on any of this!
```
---

     
 
all -  [ New OpenAI Canva action via API ](https://www.reddit.com/r/LangChain/comments/17q9grw/new_openai_canva_action_via_api/) , 2023-11-09-0909
```
Is it possible to access the new Canva AI actions via the OpenAI API? If not, do you think that OpenAI will add this fea
ture in the future?
```
---

     
 
all -  [ Reorganizing or categorize inputs by tool type ](https://www.reddit.com/r/LangChain/comments/17q2fww/reorganizing_or_categorize_inputs_by_tool_type/) , 2023-11-09-0909
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

     
 
all -  [ SelfQueryRetriever w/ date metadata ](https://www.reddit.com/r/LangChain/comments/17q054j/selfqueryretriever_w_date_metadata/) , 2023-11-09-0909
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

     
 
all -  [ Where to find documentation for langchain implementation of QDRANT Operations? ](https://www.reddit.com/r/LangChain/comments/17q04t0/where_to_find_documentation_for_langchain/) , 2023-11-09-0909
```
I'm trying to implement CRUD operations such as Uploading Points, Updating Points, Retrieving Points  etc which are avai
lable in QDRANT documentation. Is there an equivalent of these in langchain. All I see is the integration part here: [ht
tps://qdrant.tech/documentation/integrations/langchain/](https://qdrant.tech/documentation/integrations/langchain/)

&#x
200B;
```
---

     
 
all -  [ Will new ChatGPT updates replace RAG? ](https://www.reddit.com/r/LangChain/comments/17pzvrw/will_new_chatgpt_updates_replace_rag/) , 2023-11-09-0909
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

     
 
all -  [ Please roast this resume ](https://i.redd.it/9o0ict9nlyyb1.png) , 2023-11-09-0909
```
This is my friend's resume :)
```
---

     
 
all -  [ 20 document limit for retrieval assistants ](https://www.reddit.com/r/OpenAI/comments/17pyi3l/20_document_limit_for_retrieval_assistants/) , 2023-11-09-0909
```
Has anyone messed with the document retrieval yet? I wanted to test using our SoP docs to build an SoP bot, but looks li
ke despite having up 100GB limit for total files, the assistants are limited to 20 documents max. I'm hoping they increa
se this limit once the beta is over. I had built the same bot using LangChain with vector stores, but this seems to give
 better outputs with the 20 docs I was able to test with. 
```
---

     
 
all -  [ GPT-4 Vision Chatbot use-cases with api ](https://www.reddit.com/r/LangChain/comments/17pxnur/gpt4_vision_chatbot_usecases_with_api/) , 2023-11-09-0909
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

     
 
all -  [ Vectorizing Survey Responses ](https://www.reddit.com/r/LangChain/comments/17pvxxk/vectorizing_survey_responses/) , 2023-11-09-0909
```
I currently have a survey with tons of open ended responses i want to vectorize using langchain so i can use an open sou
rce LLM to help me summarize said responses. this survey is roughly 200 essay questions, with 15 responders. I would lik
e to at least be able to just ask the model to summarize the responses in less words, but ideally i would like to ingest
 both the question, response, and respondent into the model. I cant seem to find much info on this. My long and not so f
un workaround solution is to turn each survey into a PDF and ingest them that way, but that is not a very efficient proc
ess for me. 
```
---

     
 
all -  [ ChromaDB filters ](https://www.reddit.com/r/LangChain/comments/17pv8p1/chromadb_filters/) , 2023-11-09-0909
```
Is there any fine tuned version of a pre trained text generation model out there that can automatically infer ChromaDB f
ilter queries on a VDB based on natural language question inputted by the user ?
```
---

     
 
all -  [ How does LangChain actually implement the ReAct pattern on a high level? ](https://www.reddit.com/r/LangChain/comments/17puzw9/how_does_langchain_actually_implement_the_react/) , 2023-11-09-0909
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

     
 
all -  [ AutoGen v0.2.0b2 released ](https://www.reddit.com/r/AutoGenAI/comments/17puk3q/autogen_v020b2_released/) , 2023-11-09-0909
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

     
 
all -  [ Announcing Obsidian Text Generator Plugin v0.5.12: Now with GPT-4 (128k) Support and More! ](https://www.reddit.com/r/ObsidianMD/comments/17pub2o/announcing_obsidian_text_generator_plugin_v0512/) , 2023-11-09-0909
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

     
 
all -  [ LangServe + AgentExecutor ](https://www.reddit.com/r/LangChain/comments/17pstfw/langserve_agentexecutor/) , 2023-11-09-0909
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

     
 
all -  [ Facing problems with Llama-2-7b-chat-hf and langchain ](https://www.reddit.com/r/LangChain/comments/17pqhj9/facing_problems_with_llama27bchathf_and_langchain/) , 2023-11-09-0909
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

     
 
all -  [ Host Python script in SageMaker? Building a RAG-application ](https://www.reddit.com/r/aws/comments/17ppsjx/host_python_script_in_sagemaker_building_a/) , 2023-11-09-0909
```
Hello, i'm fairly new to AWS and deploying software in the cloud generally.

I'm trying to build a RAG application as a 
student project. 

Basicially im running a local embedding model within my SageMaker notebook instance that gets the con
text from a vector database (just uploaded as a directory). With LangChain i make the call to another deployed SageMaker
 Jumpstart LLM Endpoint.

Running the program within Sagemaker works without problems. However i now need to deploy my a
pplication in a way that it gets accessible. So i want to build a frontend and connect it to my Sagemaker notebook. I re
ad that Sagemaker is mostly used for deploying machine learning models however in my case its more like a small python p
rogram that does a little bit of work and then calls another endpoint. Can i simply build another endpoint out of my Sag
emaker notebook instance and make it accessible via a Lambda function and API Gateway? I read a lot of the documentation
 but didn't really understand what the easiest way to deploy is.

Thanks for your help.
```
---

     
 
all -  [ OpenAi Assistant / my thought process ](https://www.reddit.com/r/OpenAI/comments/17pmm7n/openai_assistant_my_thought_process/) , 2023-11-09-0909
```
I’m not a developer but have understanding and working with Developers to build product.
So what I understand OpenAi ass
sitant I can simply create one for my company( example upload all Hr document ) and ask developer to connect this and gi
ve it to my new employee to ask questions about any hr rules? 
It feels like LangChain and other way of building gpt is 
not required. But would this cost a lot everytime I ask questions ?
```
---

     
 
all -  [ New OpenAI Assistant tools: Knowledge Retrieval question ](https://www.reddit.com/r/OpenAI/comments/17pif3l/new_openai_assistant_tools_knowledge_retrieval/) , 2023-11-09-0909
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

     
 
all -  [ How do you compare 100s of documents with a local LLM? ](https://www.reddit.com/r/LocalLLaMA/comments/17pfpm5/how_do_you_compare_100s_of_documents_with_a_local/) , 2023-11-09-0909
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

     
 
all -  [ Are embeddings needed when using csv_agent ? ](https://www.reddit.com/r/LangChain/comments/17pffai/are_embeddings_needed_when_using_csv_agent/) , 2023-11-09-0909
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

     
 
all -  [ tinylang is now in v2, now supporting image inputs in conversation memory! ](https://www.reddit.com/r/LangChain/comments/17pe369/tinylang_is_now_in_v2_now_supporting_image_inputs/) , 2023-11-09-0909
```
Launch post: https://x.com/cosmo4\_ai/status/1721645041373069820?s=20
```
---

     
 
all -  [ Issues with Document Ranking in EnsembleRetriever and Multi-Keyword Search Optimization ](https://www.reddit.com/r/LangChain/comments/17pcb4e/issues_with_document_ranking_in_ensembleretriever/) , 2023-11-09-0909
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

     
 
all -  [ New OpenAI Assistant API ](https://www.reddit.com/r/LangChain/comments/17pbynv/new_openai_assistant_api/) , 2023-11-09-0909
```
Hi everyone, I just saw the OpenAI devday event and I'd like to discuss about the new Assistant API. It provides retriev
al functionalities and I'm wondering how this will affect Langchain usage. 

Let's discuss!
```
---

     
 
all -  [ How Does Conversation Memory Work with Router Chains? ](https://www.reddit.com/r/LangChain/comments/17pbe5b/how_does_conversation_memory_work_with_router/) , 2023-11-09-0909
```
How does conversation memory (e.g. ConversationBufferMemory) work in router chains? Passing it into the main router make
s sense to me, but insofar as creating a chat interface is concerned (i.e. allowing the user to interact with outputs), 
how does that work? Thanks in advance!
```
---

     
 
all -  [ OpenAI DevDay summary (not generated 😉) ](https://www.reddit.com/r/OpenAI/comments/17pao1k/openai_devday_summary_not_generated/) , 2023-11-09-0909
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

     
 
all -  [ Hiearchical RAG ](https://www.reddit.com/r/LangChain/comments/17p5w5o/hiearchical_rag/) , 2023-11-09-0909
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

     
 
all -  [ Join our FREE Beta Today! ](https://www.reddit.com/r/ProductHunters/comments/17p4tit/join_our_free_beta_today/) , 2023-11-09-0909
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

     
 
all -  [ Coded a Data Analysis Assistant with Streamlit & Semantic Kernel ](https://www.reddit.com/r/Python/comments/17p3cpi/coded_a_data_analysis_assistant_with_streamlit/) , 2023-11-09-0909
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

     
 
MachineLearning -  [ [D] Is this close enough to be usable? Need your inputs: Automated RAG testing tool. AI Data Pipelin ](https://www.reddit.com/r/MachineLearning/comments/17kkbm0/d_is_this_close_enough_to_be_usable_need_your/) , 2023-11-09-0909
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

     
 
MachineLearning -  [ [D] Relevance Extraction in RAG Pipelines ](https://www.reddit.com/r/MachineLearning/comments/17k6iha/d_relevance_extraction_in_rag_pipelines/) , 2023-11-09-0909
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

     
 
MachineLearning -  [ [R] Model Troubles ](https://www.reddit.com/r/MachineLearning/comments/17ikh2u/r_model_troubles/) , 2023-11-09-0909
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

     
 
MachineLearning -  [ [P] NexaAgent: A highly efficient multi-task PDF tool for all your needs | backed by AutoGen ](https://www.reddit.com/r/MachineLearning/comments/17eajz2/p_nexaagent_a_highly_efficient_multitask_pdf_tool/) , 2023-11-09-0909
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

     
 
MachineLearning -  [ [D] Is lang chain the right solution? ](https://www.reddit.com/r/MachineLearning/comments/17coyym/d_is_lang_chain_the_right_solution/) , 2023-11-09-0909
```
Hello, I would love to have an LLm that can provide answers (in chat format) based some of the sql db  data we have. Wan
t it for an internal company project. I am by no means an expert but decent in programming and want to build a system to
 get answers in chat format. My understanding is that training LLMs ground up is prohibitively expensive and langchains 
are sort of hybrid , efficient solutions. 

Please suggest any other solutions. Also would Langchain being a company and
 not open source pose a problem in terms of copyrights? Thanks!
```
---

     
 
MachineLearning -  [ [P] building a D&D NPC ](https://www.reddit.com/r/MachineLearning/comments/17clyw6/p_building_a_dd_npc/) , 2023-11-09-0909
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

     
 
MachineLearning -  [ [D] Exploring Methods to Improve Text Chunking in RAG Models (and other things...) ](https://www.reddit.com/r/MachineLearning/comments/179j7l3/d_exploring_methods_to_improve_text_chunking_in/) , 2023-11-09-0909
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

     
 
MachineLearning -  [ [News] AI & ML conference in San Francisco [Special discount code for this subreddit] ](https://www.reddit.com/r/MachineLearning/comments/1771m35/news_ai_ml_conference_in_san_francisco_special/) , 2023-11-09-0909
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

     
 
MachineLearning -  [ [D] Best way to validate llm prompts? ](https://www.reddit.com/r/MachineLearning/comments/176vnxh/d_best_way_to_validate_llm_prompts/) , 2023-11-09-0909
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

     
 
deeplearning -  [ Error with Mistral 7B model in ConversationalRetrievalChain ](https://www.reddit.com/r/deeplearning/comments/179vvou/error_with_mistral_7b_model_in/) , 2023-11-09-0909
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

     
 
deeplearning -  [ Error with Mistral 7B model in ConversationalRetrievalChain. ](https://www.reddit.com/r/deeplearning/comments/179vsif/error_with_mistral_7b_model_in/) , 2023-11-09-0909
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

     
 
deeplearning -  [ Free courses to learn about Large Language Models and building AI projects ](https://www.reddit.com/r/deeplearning/comments/178zu2u/free_courses_to_learn_about_large_language_models/) , 2023-11-09-0909
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

     
