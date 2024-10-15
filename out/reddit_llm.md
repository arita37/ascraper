 
all -  [  Project Alice - v0.2 => open source platform for agentic workflows  ](https://www.reddit.com/r/LangChain/comments/1g3r1ol/project_alice_v02_open_source_platform_for/) , 2024-10-15-0913
```
Hello everyone! A few months ago I launch a project I'd been working on called Project Alice. And today I'm happy to sha
re an incredible amount of progress, and excited to get people to try it out.

To that effect, I've created a few videos
 that show you how to install the platform and an overview of it:

* [Part 1](https://www.youtube.com/watch?v=ojhcb9ADJq
U) (11:38)
* [Part 2](https://studio.youtube.com/video/oXGk6g_gPtU/edit) (8:38)

Repository: [Link](https://github.com/M
arianoMolina/project_alice)

# What is it though?

A free open source framework and platform for agentic workflows. It i
ncludes a frontend, backend and a python logic module. It takes 5 minutes to install, no coding needed, and you get a fr
ontend where you can create your own agents, chats, task/workflows, etc, run your tasks and/or chat with your agents. Yo
u can use local models, or most of the most used API providers for AI generation.

You don't need to know how to code at
 all, but if you do, you have full flexibility to improve any aspect of it since its all open source. The platform has b
een purposefully created so that it's code is comprehensible, easy to upgrade and improve. Frontend and backend are in T
S, python module uses Pydantic almost to a pedantic level.

It has a total of 22 apis at the moment:

        OPENAI
   
     OPENAI_VISION
        OPENAI_IMG_GENERATION
        OPENAI_EMBEDDINGS
        OPENAI_TTS
        OPENAI_STT
       
 OPENAI_ASTT
        AZURE
        GEMINI
        GEMINI_VISION
        GEMINI_IMG_GEN => Google's sdk is broken atm
   
     MISTRAL
        MISTRAL_VISION
        MISTRAL_EMBEDDINGS
        GEMINI_STT
        GEMINI_EMBEDDINGS
        COHE
RE
        GROQ
        GROQ_VISION
        GROQ_TTS
        META
        META_VISION
        ANTHROPIC
        ANTHROPI
C_VISION
        LM_STUDIO
        LM_STUDIO_VISION
        GOOGLE_SEARCH
        REDDIT_SEARCH
        WIKIPEDIA_SEARCH

        EXA_SEARCH
        ARXIV_SEARCH
        GOOGLE_KNOWLEDGE_GRAPH

And an uncountable number of models that you ca
n deploy with it.

It is going to keep getting better. If you think this is nice, wait until the next update drops. And 
if you feel like helping out, I'd be super grateful. I'm about to tackle RAG and ReACT capabilities in my agents, and I'
m sure a lot of people here have some experience with that. Maybe the idea of trying to come up with a (maybe industry?)
 standard sounds interesting?

Check out the videos if you want some help installing and understanding the frontend. Ask
 me any questions otherwise!
```
---

     
 
all -  [ NaturalAgents - notion-style editor to easily create AI Agents ](https://www.reddit.com/r/OpenSourceAI/comments/1g3qsir/naturalagents_notionstyle_editor_to_easily_create/) , 2024-10-15-0913
```
[NaturalAgents](https://github.com/NaturalAgents/NaturalAgents) is the easiest way to create AI Agents in a notion-style
 editor without code - using plain english and simple macros. It's fully open-source and will be actively maintained.

H
ow this is different from other agent builders -

1. No boilerplate code (imagine langchain for multiple agents)
2. No c
ode experience
3. Can easily share and build with others
4. Readable/organized agent outputs
5. Abstracts agent communic
ations without visual complexity (image large drag and drop flowcharts)

Would love to hear thoughts and feel free to re
ach out if you're interested in contributing!
```
---

     
 
all -  [ Vector Store Usage for RAG ](https://www.reddit.com/r/LangChain/comments/1g3puzu/vector_store_usage_for_rag/) , 2024-10-15-0913
```
I'm a newbie building an RAG application for a simple documentation Q&A where the user enters the URL for a documentatio
n and can ask questions on it. I understand I need a vector store for storing the embeddings. My question is would I nee
d separate collections for every documentation. And if a user enters a documentation that already exists, should it be o
verwritten with new embeddings?
```
---

     
 
all -  [ Does RAG Have a Scaling Problem? ](https://www.reddit.com/r/LlamaIndex/comments/1g3put2/does_rag_have_a_scaling_problem/) , 2024-10-15-0913
```
My team has been digging into the scalability of vector databases for RAG (Retrieval-Augmented Generation) systems, and 
we feel we might be hitting some limits that aren’t being widely discussed.

We tested Pinecone (using both LangChain an
d LlamaIndex) out to 100K pages. We found those solutions started to lose search accuracy in as few as 10K pages. At 100
K pages in the RAG, search accuracy dropped 10-12%.

To be clear, we think this is a vector issue not an orchestrator is
sue. Though we did find particular problems trying to scale LangChain ingestion because of Unstructured (more on the end
 of the piece about that). 

We also tested our approach at [EyeLevel.ai](http://eyelevel.ai/), which does not use vecto
rs at all (I know it sounds crazy), and found only a 2% drop in search accuracy at 100K pages. And showed better accurac
y by significant margins from the outset.

I'm posting our research here to start a conversation on non-vector based app
roaches to RAG. We think there's a big opportunity to do things differently that's still very compatible with orchestrat
ors like LangChain.  We'd love to build a community around it. 

**Here's our research below. I would love to know if an
yone else is exploring non-vector approaches to RAG and of course your thoughts on the research.**

**We explain the res
earch and results on YT as well.**  
[https://youtu.be/qV1Ab0qWyT8?si=dgPL21xAHeI2jXJo](https://youtu.be/qV1Ab0qWyT8?si=
dgPL21xAHeI2jXJo)

[Image: The chart shows accuracy loss at just 10,000 pages of content using a Pinecone vector databas
e with both LangChain and Llamaindex-based RAG applications.  Conversely, EyeLevel's GroundX APIs for RAG show almost no
 loss.](https://preview.redd.it/74oi00ko1sud1.png?width=1600&format=png&auto=webp&s=5f86d97d682631215832ab3f92b34c9641f8
d3e9)

# What’s Inside

In this report, we will review how the test was constructed, the detailed findings, our theories
 on why vector similarity search experienced challenges and suggested approaches to scale RAG without the performance hi
t. We also encourage you to read our [prior research](https://www.eyelevel.ai/post/most-accurate-rag) in which EyeLevel’
s GroundX APIs bested LangChain, Pinecone and Llamaindex based RAG systems by 50-120% on accuracy over 1,000 pages of co
ntent.  

The work was performed by Daniel Warfield, a data scientist and RAG engineer and Dr. Benjamin Fletcher, PhD, a
 computer scientist and former senior engineer at IBM Watson. Both men work for EyeLevel.ai. The data, code and methods 
of this test will be open sourced and available shortly. Others are invited to run the data and corroborate or challenge
 these findings. 

# Defining RAG 

**Feel free to skip this section if you’re familiar with RAG.**  

RAG stands for “R
etrieval Augmented Generation”. When you ask a RAG system a query, RAG does the following steps: 

1. Retrieval: Based o
n the query from the user, the RAG system retrieves relevant knowledge from a set of documents. 
2. Augmentation: The RA
G system combines the retrieved information with the user query to construct a prompt. 
3. Generation: The augmented pro
mpt is passed to a large language model, generating the final output. 

The implementation of these three steps can vary
 wildly between RAG approaches. However, the objective is the same: to make a language model more useful by feeding it i
nformation from real-world, relevant documents. 

RAG allows a language model to reference application specific informat
ion from human documents, allowing developers to build tailored and specific products 

# Beyond The Tech Demo 

When mo
st developers begin experimenting with RAG they might grab a few documents, stick them into a RAG document store and be 
blown away by the results. Like magic, many RAG systems can allow a language model to understand books, company document
s, emails, and more. 

However, as one continues experimenting with RAG, some difficulties begin to emerge. 

1. Many do
cuments are not purely textual. They might have images, tables, or complex formatting. While many RAG systems can parse 
complex documents, the quality of parsing varies widely between RAG approaches. We explore the realities of parsing in[ 
another article](https://www.eyelevel.ai/post/most-accurate-rag). 
2. As a RAG system is exposed to more documents, it h
as more opportunities to retrieve the wrong document, potentially causing a degradation in performance   
3. Because of 
technical complexity, the underlying non-determinism of language models, and the difficulty of profiling the performance
 of LLM applications in real world settings, it can be difficult to predict the cost and level of effort of developing R
AG applications. 

In this article we’ll focus on the second and third problems listed above; performance degradation of
 RAG at scale and difficulties of implementation 

# The Test 

To test how much larger document sets degrade the perfor
mance of RAG systems, we first defined a set of 92 questions based on real-world documents.  

[A few examples of the re
al-world documents used in this test, which contain answers to our 92 questions. ](https://preview.redd.it/ojr3ab7s1sud1
.png?width=1429&format=png&auto=webp&s=6ee3ce03d23a9ca0a35b181869c71a213d0da362)

A few examples of the real-world docum
ents used in this test, which contain answers to our 92 questions. 

We then constructed four document sets to apply RAG
 to. All four of these document sets contain the same 310 pages of documents which answer our 92 test questions. However
, each document set also contains a different number of irrelevant pages from miscellaneous documents. We started with 1
,000 pages and scaled up to 100,000 in our largest test. 

[We asked the same questions based on the same set of documen
ts \(blue\), but exposed the RAG system to varying amounts of unrelated documents \(red\). This diagram shows the number
 of relevant pages in each document set, compared to the total size of each document set.](https://preview.redd.it/r9nhj
ahv1sud1.png?width=1431&format=png&auto=webp&s=c09a05becc851cd1199fe39c92ee1753bc9f8950)

We asked the same questions ba
sed on the same set of documents (blue), but exposed the RAG system to varying amounts of unrelated documents (red). Thi
s diagram shows the number of relevant pages in each document set, compared to the total size of each document set.

An 
ideal RAG system would, in theory, behave identically across all document sets, as all document sets contain the same an
swers to the same questions. In practice, however, added information in a docstore can trick a RAG system into retrievin
g the wrong context for a given query. The more documents there are, the more likely this is to happen. Therefore, RAG p
erformance tends to degrade as the number of documents increases. 

In this test we applied each of these three popular 
RAG approaches to the four document sets mentioned above:

* LangChain: a popular python library designed to abstract ce
rtain LLM workflows. 
* LlamaIndex: a popular python library which has advanced vector embedding capability, and advance
d RAG functionality. 
* EyeLevel’s GroundX: a feature complete retrieval engine built for RAG. 

By applying each of the
se RAG approaches to the four document sets, we can study the relative performance of each RAG approach at scale. 

For 
both LangChain and LlamaIndex we employed Pinecone as our vector store and OpenAI’s text-embedding-ada-002 for embedding
. GroundX, being an all-in-one solution, was used in isolation up to the point of generation. All approaches used OpenAI
's gpt-4-1106-preview for the final generation of results. Results for each approach were evaluated as being true or fal
se via human evaluation. 

# The Effect of Scale on RAG 

We ran the test as defined in the previous section and got the
 following results. 

[The performance of different RAG approaches varies greatly, both in base performance and the rate
 of performance degradation at scale. We explore differences in base performance thoroughly in another article ](https:/
/preview.redd.it/o0x2y1dx1sud1.png?width=1600&format=png&auto=webp&s=fe6ce89f4b7657de3221b0e5b93110ecca20c546)

The perf
ormance of different RAG approaches varies greatly, both in base performance and the rate of performance degradation at 
scale. We explore differences in base performance thoroughly in another article 

As can be seen in the figure above, th
e rate at which RAG degrades in performance varies widely between RAG approaches. Based on these results one might expec
t GroundX to degrade in performance by 2% per 100,000 documents, while LCPC and LI might degrade 10-12% per 100,000 docu
ments. The reason for this difference in robustness to larger document sets, likely, has to do with the realities of usi
ng vector search as the bedrock of a RAG system.  

In theory a high dimensional vector space can hold a vast amount of 
information. 100,000 in binary is 17 values long (11000011010100000). So, if we *only* use binary vectors with unit comp
onents in a high dimensional vector space, we could store each page in our 100,000 page set with only a 17 dimensional s
pace. Text-embedding-ada-002, which is the encoder used in this experiment, outputs a 1536-dimension vector. If one calc
ulates 2\^1536 (effectively calculating how many things one could describe using only binary vectors in this space) the 
result would be a number that’s significantly greater than the number of atoms in the known universe. Of course, actual 
embeddings are not restricted to binary numbers; they can be expressed in decimal numbers of very high precision. Even r
elatively small vector spaces can hold a vast amount of information. 

The trick is, how do you get information into a v
ector space *meaningfully*? RAG needs content to be placed in a vector space such that similar things can be searched, t
hus the encoder has to practically organize information into useful regions. It’s our theory that modern encoders don’t 
have what it takes to organize large sets of documents in these vector spaces, even if the vector spaces can theoretical
ly fit a near infinite amount of information. The encoder can only put so much information into a vector space before th
e vector space gets so cluttered that distance-based search is rendered non-performant. 

[There is a big difference bet
ween a space being able to fit information, and that information being meaningfully organized. ](https://preview.redd.it
/inp40j1f2sud1.png?width=948&format=png&auto=webp&s=f7b0c838224196d7d0f24cb6db7abae3dbd8431d)

There is a big difference
 between a space being able to fit information, and that information being meaningfully organized. 

EyeLevel’s GroundX 
doesn’t use vector similarity as its core search strategy, but rather a tuned comparison based on the similarity of sema
ntic objects. There are no vectors used in this approach. This is likely why GroundX exhibits superior performance in la
rger document sets. 

In this test we employed what is commonly referred to as “naive” RAG. LlamaIndex and LangChain all
ow for many advanced RAG approaches, but they had little impact on performance and were harder to employ at larger scale
s. We cover that in another article which will be released shortly.

# The Surprising Technical Difficulty of Scale 

Wh
ile 100,000 pages seems like a lot, it’s actually a fairly small amount of information for industries like engineering, 
law, and healthcare. Initially we imagined testing on much larger document sets, but while conducting this test we were 
surprised by the practical difficulty of getting LangChain to work at scale; forcing us to reduce the scope of our test.
 

To get RAG up and running for a set of PDF documents, the first step is to parse the content of those PDFs into some 
sort of textual representation. LangChain uses libraries from [Unstructured.io](http://unstructured.io/) to perform pars
ing on complex PDFs, which works seamlessly for small document sets. 

Surprisingly, though, the speed of LangChain pars
ing is incredibly slow. Based on our analysis it appears that Unstructured uses a variety of models to detect and parse 
out key elements within a PDF. These models should employ GPU acceleration, but they don’t. That results in LangChain ta
king days to parse a modestly sized set of documents, even on very large (and expensive) compute instances. To get LangC
hain working we needed to reverse engineer portions of Unstructured and inject code to enable GPU utilization of these m
odels. 

It appears that this is a known issue in Unstructured, as seen in the notes below. As it stands, it presents si
gnificant difficulty in scaling LangChain to larger document sets, given LangChain abstracts away fine grain control of 
Unstructured. 

https://preview.redd.it/zebe6lqg2sud1.png?width=1346&format=png&auto=webp&s=393cefee81ed7de8f8b936c0087b
aa0c326fa1d0

[**Source: Github**](https://github.com/Unstructured-IO/unstructured-inference/blob/64cd41c37fe4535702b3be
9c6b58f380ca4c7edd/unstructured_inference/inference/layout.py#L175)

We only made improvements to LangChain parsing up t
o the point where this test became feasible. If you want to modify LangChain for faster parsing, here are some resources
: 

* The default directory loader of LangChain is Unstructured ([source1](https://python.langchain.com/v0.1/docs/module
s/data_connection/document_loaders/file_directory/),[ source2](https://github.com/langchain-ai/langchain/blob/410e9add44
43607618a75827afe1a676fcd7c0a7/libs/community/langchain_community/document_loaders/directory.py#L38)). 
* Unstructured u
ses “hi res” for the PDFs by default if text extraction cannot be performed on the document ([source1](https://github.co
m/langchain-ai/langchain/blob/410e9add4443607618a75827afe1a676fcd7c0a7/libs/community/langchain_community/document_loade
rs/directory.py#L38) ,[ source2](https://github.com/Unstructured-IO/unstructured/blob/23e570fc8ac71c5d1a5788dcb5b3a7a7a5
7bf078/unstructured/partition/strategies.py#L103) ). Other options are available like “fast” and “OCR only”, which have 
different processing intensities 
* “Hi Res” involves: 
   * Converting the pdf into images ([source](https://github.com
/Unstructured-IO/unstructured/blob/23e570fc8ac71c5d1a5788dcb5b3a7a7a57bf078/unstructured/partition/pdf_image/pdfminer_pr
ocessing.py#L36)) 
   * Running a layout detection model to understand the layout of the documents ([source](https://git
hub.com/Unstructured-IO/unstructured-inference/blob/76619ca66f47d013f6656fce775f6fddde5d36ae/unstructured_inference/mode
ls/yolox.py#L3)). This model benefits greatly from GPU utilization, but does not leverage the GPU unless ONNX is install
ed ([source](https://onnxruntime.ai/docs/get-started/with-python.html)) 
   * OCR extraction using tesseract (by default
) ([source](https://github.com/Unstructured-IO/unstructured/blob/23e570fc8ac71c5d1a5788dcb5b3a7a7a57bf078/unstructured/p
artition/utils/config.py#L103)) which is a very compute intensive process ([source](https://github.com/tesseract-ocr/tes
seract/issues/263)) 
   * Running the page through a table layout model ([source](https://github.com/Unstructured-IO/uns
tructured-inference/blob/76619ca66f47d013f6656fce775f6fddde5d36ae/unstructured_inference/models/tables.py#L140)) 

While
 our configuration efforts resulted in faster processing times, it was still too slow to be feasible for larger document
 sets. To reduce time, we did “hi res” parsing on the relevant documents and “fast” parsing on documents which were irre
levant to our questions. With this configuration, parsing 100,000 pages of documents took 8 hours. If we had applied “hi
 res” to all documents, we imagine that parsing would have taken 31 days (at around 30 seconds per page). 

At the end o
f the day, this test took two senior engineers (one who’s worked at a directorial level at several AI companies, and a m
ulti company CTO with decades of applied experience of AI at scale) several weeks to do the development necessary to wri
te this article, largely because of the difficulty of applying LangChain to a modestly sized document set.  To get LangC
hain working in a production setting, we estimate that the following efforts would be required: 

* Tesseract would need
 to be interfaced with in a way that is more compute and time efficient. This would likely require a high-performance CP
U instance, and modifications to the LangChain source code. 
* The layout and table models would need to be made to run 
on a GPU instance 
* To do both tasks in a cost-efficient manner, these tasks should probably be decoupled. However, thi
s is not possible with the current abstraction of LangChain. 

On top of using a unique technology which is highly perfo
rmant, GroundX also abstracts virtually all of these technical difficulties behind an API. You upload your documents, th
en search the results. That’s it. 

If you want RAG to be even easier, one of the things that makes Eyelevel so compelli
ng is the service aspect they provide to GroundX. You can work with Eyelevel as a partner to get GroundX working quickly
 and performantly for large scale applications. 

# Conclusion 

When choosing a platform to build RAG applications, eng
ineers must balance a variety of key metrics. The robustness of a system to maintain performance at scale is one of thos
e critical metrics. In this head-to-head test on real-world documents, EyeLevel’s GroundX exhibited a heightened level o
f performance at scale, beating LangChain and LlamaIndex. 

Another key metric is efficiency at scale. As it turns out, 
LangChain has significant implementation difficulties which can make the large-scale distribution of LangChain powered R
AG difficult and costly. 

Is this the last word? Certainly not. In future research, we will test various advanced RAG t
echniques, additional RAG frameworks such as Amazon Q and GPTs and increasingly complex and multimodal data types. So st
ay tuned. 

If you’re curious about running these results yourself, please reach out to us at [info@eyelevel.ai.Vector](
mailto:info@eyelevel.ai.Vector) databases, a key technology in building retrieval augmented generation or RAG applicatio
ns, has a scaling problem that few are talking about. 

According to new research by [EyeLevel.ai](https://www.eyelevel.
ai/), an AI tools company, the precision of vector similarity search degrades in as few as 10,000 pages, reaching a 12% 
performance hit by the 100,000-page mark.

The research also tested [EyeLevel’s enterprise-grade RAG platform](https://w
ww.eyelevel.ai/product/apis) which does not use vectors. EyeLevel lost only 2% accuracy at scale.

The findings suggest 
that while vector databases have become highly popular tools to build RAG and LLM-based applications, developers may fac
e unexpected challenges as they shift from testing to production and attempt to scale their applications.  

The work wa
s performed by Daniel Warfield, a data scientist and RAG engineer and Dr. Benjamin Fletcher, PhD, a computer scientist a
nd former senior engineer at IBM Watson. Both men work for EyeLevel.ai. The data, code and methods of this test will be 
open sourced and available shortly. Others are invited to run the data and corroborate or challenge these findings. 

My
 team has been digging into the scalability of vector databases for RAG (Retrieval-Augmented Generation) systems, and we
 feel we might be hitting some limits that aren’t being widely discussed.

We tested Pinecone (using both LangChain and 
LlamaIndex) out to 100K pages. We found those solutions started to lose search accuracy in as few as 10K pages. At 100K 
pages in the RAG, search accuracy dropped 10-12%.

We also tested our approach at [EyeLevel.ai](http://eyelevel.ai/), wh
ich does not use vectors at all (I know it sounds crazy), and found only a 2% drop in search accuracy at 100K pages. And
 showed better accuracy by significant margins from the outset.

**Here's our research below. I would love to know if an
yone else is exploring non-vector approaches to RAG and of course your thoughts on the research.**

**We explain the res
earch and results on YT as well.**  
[https://youtu.be/qV1Ab0qWyT8?si=dgPL21xAHeI2jXJo](https://youtu.be/qV1Ab0qWyT8?si=
dgPL21xAHeI2jXJo) 
```
---

     
 
all -  [ Gradio 5 - Building a Quick Chatbot UI for LangChain in python tutorial on Youtube ](https://www.reddit.com/r/Python/comments/1g3pac0/gradio_5_building_a_quick_chatbot_ui_for/) , 2024-10-15-0913
```
tutorial: [https://www.youtube.com/watch?v=u\_Xm3vgBQ9Y](https://www.youtube.com/watch?v=u_Xm3vgBQ9Y)



colab: [https:/
/colab.research.google.com/drive/1tq6h7yPmdX463xwA4hz31hen6Xh55MB-?usp=sharing#scrollTo=GQth439KJGG\_](https://colab.res
earch.google.com/drive/1tq6h7yPmdX463xwA4hz31hen6Xh55MB-?usp=sharing#scrollTo=GQth439KJGG_)



gradio 5 blog: [https://h
uggingface.co/blog/gradio-5](https://huggingface.co/blog/gradio-5)



gradio github: [https://github.com/gradio-app/grad
io](https://github.com/gradio-app/gradio)
```
---

     
 
all -  [ Is it just me or the dependency resolution in Langchain is a nightmare. Everytime I integrate any LL ](https://www.reddit.com/r/LangChain/comments/1g3mriz/is_it_just_me_or_the_dependency_resolution_in/) , 2024-10-15-0913
```

```
---

     
 
all -  [ I have a python codebase that uses streamlit, want to move to react for easier integration. ](https://www.reddit.com/r/LangChain/comments/1g3milz/i_have_a_python_codebase_that_uses_streamlit_want/) , 2024-10-15-0913
```
As the title states I've been working on a predominately python codebase with a lot of langchian concepts that have been
 written in python and I want to migrate away from streamlit to some sort of react library, please do let me know if the
re are any solutions availabel thank you.
```
---

     
 
all -  [ Python or Typescript for RAG? ](https://www.reddit.com/r/Rag/comments/1g3lgzy/python_or_typescript_for_rag/) , 2024-10-15-0913
```
I am working on a project for my Bachelor's thesis and want to build a Retrieval-Augmented Generation (RAG) system. For 
Langchain and LlamaIndex, there are both Python and TypeScript versions available. I am new to this topic but would like
 to set up a web application in the medium term, which will be programmed in Next.js later on. Since the project will ru
n on a server, does the backend language really matter? Or should I stick to one language, since TypeScript can be used 
in Next.js? The problem I see is that the documentation for Langchain and LlamaIndex in TypeScript is tiny compared to P
ython. As a beginner in this field, will I still be able to manage with TypeScript? I would prefer not to get stuck, but
 I would also like to cover my future projects. Another advantage would be that I could use the code for Obsidian plugin
 development, which can also be done in TypeScript. What do you think? Thanks in advance!
```
---

     
 
all -  [ Has anyone seen AI agents working in production at scale? ](https://www.reddit.com/r/LocalLLaMA/comments/1g3jkct/has_anyone_seen_ai_agents_working_in_production/) , 2024-10-15-0913
```
Has anyone seen AI agents working in production at scale? 

It doesn't matter if you're using the Swarm, langchain, or a
ny other AI agent orchestration framework if the underlying issue is that AI agents too slow, too expensive, and too unr
eliable. I wrote about [AI agent hype vs. reality](https://www.kadoa.com/blog/ai-agents-hype-vs-reality) a while ago, an
d I don't think it has changed yet.

>By combining tightly constrained LLMs, good evaluation data, human-in-the-loop ove
rsight, and traditional engineering methods, we can achieve reliably good results for automating medium-complex tasks.


>Will AI agents automate tedious repetitive work, such as web scraping, form filling, and data entry? Yes, absolutely.


>Will AI agents autonomously book your vacation without your intervention? Unlikely, at least in the near future.

What 
are your real-world use cases and experiences?
```
---

     
 
all -  [ LangGraph 101 - Tutorial with Practical Example ](https://www.reddit.com/r/LangChain/comments/1g3i734/langgraph_101_tutorial_with_practical_example/) , 2024-10-15-0913
```
Hi folks!

It's been a while but I just finished uploading my latest tutorial. I built a super simple, but extremely pow
erful two-node LangGraph app that can retrieve data from my resume and a job description and then use the information to
 respond to any question. It could for example:

* Re-write parts or all of my resume to match the job description.
* Ge
nerate relevant interview questions and provide feedback.
* Write job-specific cover letters.
* etc.

# [>>> Watch here 
<<<](https://youtu.be/7KIrBjQTGLA)

You get the idea! I know the official docs are somewhat complicated, and sometimes b
roken, and a lot of people have a hard time starting out using LangGraph. If you're one of those people or just getting 
started and want to learn more about the library, [check out the tutorial](https://youtu.be/7KIrBjQTGLA)!

Cheers! :)
```
---

     
 
all -  [ Does RAG Have a Scaling Problem? ](https://www.reddit.com/r/Rag/comments/1g3h9w2/does_rag_have_a_scaling_problem/) , 2024-10-15-0913
```
My team has been digging into the scalability of vector databases for RAG (Retrieval-Augmented Generation) systems, and 
we feel we might be hitting some limits that aren’t being widely discussed. 

We tested Pinecone (using both LangChain a
nd LlamaIndex) out to 100K pages. We found those solutions started to lose search accuracy in as few as 10K pages. At 10
0K pages in the RAG, search accuracy dropped 10-12%.

We also tested our approach at [EyeLevel.ai](http://EyeLevel.ai), 
which does not use vectors at all (I know it sounds crazy), and found only a 2% drop in search accuracy at 100K pages. A
nd showed better accuracy by significant margins from the outset. 

**Here's our research below. I would love to know if
 anyone else is exploring non-vector approaches to RAG and of course your thoughts on the research.** 

**We explain the
 research and results on YT as well.**   
[**https://www.youtube.com/watch?v=qV1Ab0qWyT8**](https://www.youtube.com/watc
h?v=qV1Ab0qWyT8)

[Image: The chart shows accuracy loss at just 10,000 pages of content using a Pinecone vector database
 with both LangChain and Llamaindex-based RAG applications.  Conversely, EyeLevel's GroundX APIs for RAG show almost no 
loss.](https://preview.redd.it/3okwujg7fqud1.png?width=1600&format=png&auto=webp&s=dfe1b2bb38f6d4a0fc5e7798ebd60fa23df13
c80)

# What’s Inside

In this report, we will review how the test was constructed, the detailed findings, our theories 
on why vector similarity search experienced challenges and suggested approaches to scale RAG without the performance hit
. We also encourage you to read our [prior research](https://www.eyelevel.ai/post/most-accurate-rag) in which EyeLevel’s
 GroundX APIs bested LangChain, Pinecone and Llamaindex based RAG systems by 50-120% on accuracy over 1,000 pages of con
tent.  

The work was performed by Daniel Warfield, a data scientist and RAG engineer and Dr. Benjamin Fletcher, PhD, a 
computer scientist and former senior engineer at IBM Watson. Both men work for EyeLevel.ai. The data, code and methods o
f this test will beopen sourced and available shortly. Others are invited to run the data and corroborate or challenge t
hese findings. 

# Defining RAG 

**Feel free to skip this section if you’re familiar with RAG.**  

RAG stands for “Ret
rieval Augmented Generation”. When you ask a RAG system a query, RAG does the following steps: 

1. Retrieval: Based on 
the query from the user, the RAG system retrieves relevant knowledge from a set of documents. 

1. Augmentation: The RAG
 system combines the retrieved information with the user query to construct a prompt. 

1. Generation: The augmented pro
mpt is passed to a large language model, generating the final output. 

The implementation of these three steps can vary
 wildly between RAG approaches. However, the objective is the same: to make a language model more useful by feeding it i
nformation from real-world, relevant documents. 

[RAG allows a language model to reference application specific informa
tion from human documents, allowing developers to build tailored and specific products ](https://preview.redd.it/z5t4h8a
cfqud1.png?width=1158&format=png&auto=webp&s=ce9d6e5ce5acb057243db14193f90f0a2072ccf2)

# Beyond The Tech Demo 

When mo
st developers begin experimenting with RAG they might grab a few documents, stick them into a RAG document store and be 
blown away by the results. Like magic, many RAG systems can allow a language model to understand books, company document
s, emails, and more. 

However, as one continues experimenting with RAG, some difficulties begin to emerge. 

1. Many do
cuments are not purely textual. They might have images, tables, or complex formatting. While many RAG systems can parse 
complex documents, the quality of parsing varies widely between RAG approaches. We explore the realities of parsing in[ 
another article](https://www.eyelevel.ai/post/most-accurate-rag). 

1. As a RAG system is exposed to more documents, it 
has more opportunities to retrieve the wrong document, potentially causing a degradation in performance   

1. Because o
f technical complexity, the underlying non-determinism of language models, and the difficulty of profiling the performan
ce of LLM applications in real world settings, it can be difficult to predict the cost and level of effort of developing
 RAG applications. 

In this article we’ll focus on the second and third problems listed above; performance degradation 
of RAG at scale and difficulties of implementation 

# The Test 

To test how much larger document sets degrade the perf
ormance of RAG systems, we first defined a set of 92 questions based on real-world documents.  

[A few examples of the 
real-world documents used in this test, which contain answers to our 92 questions. ](https://preview.redd.it/vbm3jcxffqu
d1.png?width=1429&format=png&auto=webp&s=9eed23eb6d7e0c6d8816063e7d3a9d86ad1848e8)

We then constructed four document se
ts to apply RAG to. All four of these document sets contain the same 310 pages of documents which answer our 92 test que
stions. However, each document set also contains a different number of irrelevant pages from miscellaneous documents. We
 started with 1,000 pages and scaled up to 100,000 in our largest test.   
 

[We asked the same questions based on the 
same set of documents \(blue\), but exposed the RAG system to varying amounts of unrelated documents \(red\). This diagr
am shows the number of relevant pages in each document set, compared to the total size of each document set.](https://pr
eview.redd.it/u4d6keqpfqud1.png?width=1431&format=png&auto=webp&s=b0161c312eca9b0633b5df58713f1ed92893cb30)

An ideal RA
G system would, in theory, behave identically across all document sets, as all document sets contain the same answers to
 the same questions. In practice, however, added information in a docstore can trick a RAG system into retrieving the wr
ong context for a given query. The more documents there are, the more likely this is to happen. Therefore, RAG performan
ce tends to degrade as the number of documents increases. 

In this test we applied each of these three popular RAG appr
oaches to the four document sets mentioned above:

* LangChain: a popular python library designed to abstract certain LL
M workflows. 
* LlamaIndex: a popular python library which has advanced vector embedding capability, and advanced RAG fu
nctionality. 
* EyeLevel’s GroundX: a feature complete retrieval engine built for RAG. 

By applying each of these RAG a
pproaches to the four document sets, we can study the relative performance of each RAG approach at scale. 

For both Lan
gChain and LlamaIndex we employed Pinecone as our vector store and OpenAI’s text-embedding-ada-002 for embedding. Ground
X, being an all-in-one solution, was used in isolation up to the point of generation. All approaches used OpenAI's gpt-4
-1106-preview for the final generation of results. Results for each approach were evaluated as being true or false via h
uman evaluation. 

# The Effect of Scale on RAG 

We ran the test as defined in the previous section and got the followi
ng results. 

[The performance of different RAG approaches varies greatly, both in base performance and the rate of perf
ormance degradation at scale. We explore differences in base performance thoroughly in another article ](https://preview
.redd.it/f3uqn8vsfqud1.png?width=1600&format=png&auto=webp&s=69abb4cf7d224a523457ac0b769a6dc2ae0148c7)

As can be seen i
n the figure above, the rate at which RAG degrades in performance varies widely between RAG approaches. Based on these r
esults one might expect GroundX to degrade in performance by 2% per 100,000 documents, while LCPC and LI might degrade 1
0-12% per 100,000 documents. The reason for this difference in robustness to larger document sets, likely, has to do wit
h the realities of using vector search as the bedrock of a RAG system.  

In theory a high dimensional vector space can 
hold a vast amount of information. 100,000 in binary is 17 values long (11000011010100000). So, if we *only* use binary 
vectors with unit components in a high dimensional vector space, we could store each page in our 100,000 page set with o
nly a 17 dimensional space. Text-embedding-ada-002, which is the encoder used in this experiment, outputs a 1536-dimensi
on vector. If one calculates 2\^1536 (effectively calculating how many things one could describe using only binary vecto
rs in this space) the result would be a number that’s significantly greater than the number of atoms in the known univer
se. Of course, actual embeddings are not restricted to binary numbers; they can be expressed in decimal numbers of very 
high precision. Even relatively small vector spaces can hold a vast amount of information. 

The trick is, how do you ge
t information into a vector space *meaningfully*? RAG needs content to be placed in a vector space such that similar thi
ngs can be searched, thus the encoder has to practically organize information into useful regions. It’s our theory that 
modern encoders don’t have what it takes to organize large sets of documents in these vector spaces, even if the vector 
spaces can theoretically fit a near infinite amount of information. The encoder can only put so much information into a 
vector space before the vector space gets so cluttered that distance-based search is rendered non-performant. 

[There i
s a big difference between a space being able to fit information, and that information being meaningfully organized. ](h
ttps://preview.redd.it/uzbfvsyufqud1.png?width=948&format=png&auto=webp&s=5dc7fad4f9e976a595281bac95e34f64e472613a)

Eye
Level’s GroundX doesn’t use vector similarity as its core search strategy, but rather a tuned comparison based on the si
milarity of semantic objects. There are no vectors used in this approach. This is likely why GroundX exhibits superior p
erformance in larger document sets. 

In this test we employed what is commonly referred to as “naive” RAG. LlamaIndex a
nd LangChain allow for many advanced RAG approaches, but they had little impact on performance and were harder to employ
 at larger scales. We cover that in another article which will be released shortly.

# The Surprising Technical Difficul
ty of Scale 

While 100,000 pages seems like a lot, it’s actually a fairly small amount of information for industries li
ke engineering, law, and healthcare. Initially we imagined testing on much larger document sets, but while conducting th
is test we were surprised by the practical difficulty of getting LangChain to work at scale; forcing us to reduce the sc
ope of our test. 

To get RAG up and running for a set of PDF documents, the first step is to parse the content of those
 PDFs into some sort of textual representation. LangChain uses libraries from [Unstructured.io](http://Unstructured.io) 
to perform parsing on complex PDFs, which works seamlessly for small document sets. 

Surprisingly, though, the speed of
 LangChain parsing is incredibly slow. Based on our analysis it appears that Unstructured uses a variety of models to de
tect and parse out key elements within a PDF. These models should employ GPU acceleration, but they don’t. That results 
in LangChain taking days to parse a modestly sized set of documents, even on very large (and expensive) compute instance
s. To get LangChain working we needed to reverse engineer portions of Unstructured and inject code to enable GPU utiliza
tion of these models. 

It appears that this is a known issue in Unstructured, as seen in the notes below. As it stands,
 it presents significant difficulty in scaling LangChain to larger document sets, given LangChain abstracts away fine gr
ain control of Unstructured. 

https://preview.redd.it/dhchak3xfqud1.png?width=1346&format=png&auto=webp&s=2e1e6b84f79d8
89c901f05140771f68bb0f00150

[**Source: Github**](https://github.com/Unstructured-IO/unstructured-inference/blob/64cd41c
37fe4535702b3be9c6b58f380ca4c7edd/unstructured_inference/inference/layout.py#L175)

We only made improvements to LangCha
in parsing up to the point where this test became feasible. If you want to modify LangChain for faster parsing, here are
 some resources: 

* The default directory loader of LangChain is Unstructured ([source1](https://python.langchain.com/v
0.1/docs/modules/data_connection/document_loaders/file_directory/),[ source2](https://github.com/langchain-ai/langchain/
blob/410e9add4443607618a75827afe1a676fcd7c0a7/libs/community/langchain_community/document_loaders/directory.py#L38)). 
*
 Unstructured uses “hi res” for the PDFs by default if text extraction cannot be performed on the document ([source1](ht
tps://github.com/langchain-ai/langchain/blob/410e9add4443607618a75827afe1a676fcd7c0a7/libs/community/langchain_community
/document_loaders/directory.py#L38) ,[ source2](https://github.com/Unstructured-IO/unstructured/blob/23e570fc8ac71c5d1a5
788dcb5b3a7a7a57bf078/unstructured/partition/strategies.py#L103) ). Other options are available like “fast” and “OCR onl
y”, which have different processing intensities 
* “Hi Res” involves: 
   * Converting the pdf into images ([source](htt
ps://github.com/Unstructured-IO/unstructured/blob/23e570fc8ac71c5d1a5788dcb5b3a7a7a57bf078/unstructured/partition/pdf_im
age/pdfminer_processing.py#L36)) 
   * Running a layout detection model to understand the layout of the documents ([sour
ce](https://github.com/Unstructured-IO/unstructured-inference/blob/76619ca66f47d013f6656fce775f6fddde5d36ae/unstructured
_inference/models/yolox.py#L3)). This model benefits greatly from GPU utilization, but does not leverage the GPU unless 
ONNX is installed ([source](https://onnxruntime.ai/docs/get-started/with-python.html)) 
   * OCR extraction using tesser
act (by default) ([source](https://github.com/Unstructured-IO/unstructured/blob/23e570fc8ac71c5d1a5788dcb5b3a7a7a57bf078
/unstructured/partition/utils/config.py#L103)) which is a very compute intensive process ([source](https://github.com/te
sseract-ocr/tesseract/issues/263)) 
   * Running the page through a table layout model ([source](https://github.com/Unst
ructured-IO/unstructured-inference/blob/76619ca66f47d013f6656fce775f6fddde5d36ae/unstructured_inference/models/tables.py
#L140)) 

While our configuration efforts resulted in faster processing times, it was still too slow to be feasible for 
larger document sets. To reduce time, we did “hi res” parsing on the relevant documents and “fast” parsing on documents 
which were irrelevant to our questions. With this configuration, parsing 100,000 pages of documents took 8 hours. If we 
had applied “hi res” to all documents, we imagine that parsing would have taken 31 days (at around 30 seconds per page).
 

At the end of the day, this test took two senior engineers (one who’s worked at a directorial level at several AI com
panies, and a multi company CTO with decades of applied experience of AI at scale) several weeks to do the development n
ecessary to write this article, largely because of the difficulty of applying LangChain to a modestly sized document set
.  To get LangChain working in a production setting, we estimate that the following efforts would be required: 

* Tesse
ract would need to be interfaced with in a way that is more compute and time efficient. This would likely require a high
-performance CPU instance, and modifications to the LangChain source code. 
* The layout and table models would need to 
be made to run on a GPU instance 
* To do both tasks in a cost-efficient manner, these tasks should probably be decouple
d. However, this is not possible with the current abstraction of LangChain. 

On top of using a unique technology which 
is highly performant, GroundX also abstracts virtually all of these technical difficulties behind an API. You upload you
r documents, then search the results. That’s it. 

If you want RAG to be even easier, one of the things that makes Eyele
vel so compelling is the service aspect they provide to GroundX. You can work with Eyelevel as a partner to get GroundX 
working quickly and performantly for large scale applications. 

# Conclusion 

When choosing a platform to build RAG ap
plications, engineers must balance a variety of key metrics. The robustness of a system to maintain performance at scale
 is one of those critical metrics. In this head-to-head test on real-world documents, EyeLevel’s GroundX exhibited a hei
ghtened level of performance at scale, beating LangChain and LlamaIndex. 

Another key metric is efficiency at scale. As
 it turns out, LangChain has significant implementation difficulties which can make the large-scale distribution of Lang
Chain powered RAG difficult and costly. 

Is this the last word? Certainly not. In future research, we will test various
 advanced RAG techniques, additional RAG frameworks such as Amazon Q and GPTs and increasingly complex and multimodal da
ta types. So stay tuned. 

If you’re curious about running these results yourself, please reach out to us at info@eyelev
el.ai.Vector databases, a key technology in building retrieval augmented generation or RAG applications, has a scaling p
roblem that few are talking about. 

According to new research by [EyeLevel.ai](https://www.eyelevel.ai/), an AI tools c
ompany, the precision of vector similarity search degrades in as few as 10,000 pages, reaching a 12% performance hit by 
the 100,000-page mark.

The research also tested [EyeLevel’s enterprise-grade RAG platform](https://www.eyelevel.ai/prod
uct/apis) which does not use vectors. EyeLevel lost only 2% accuracy at scale.

The findings suggest that while vector d
atabases have become highly popular tools to build RAG and LLM-based applications, developers may face unexpected challe
nges as they shift from testing to production and attempt to scale their applications.  

The work was performed by Dani
el Warfield, a data scientist and RAG engineer and Dr. Benjamin Fletcher, PhD, a computer scientist and former senior en
gineer at IBM Watson. Both men work for EyeLevel.ai. The data, code and methods of this test will be open sourced and av
ailable shortly. Others are invited to run the data and corroborate or challenge these findings. 
```
---

     
 
all -  [ Help scaling LLM classifications and validations ](https://www.reddit.com/r/LangChain/comments/1g3h1hd/help_scaling_llm_classifications_and_validations/) , 2024-10-15-0913
```
I'm working on an application that will classify 10 million records according to pretty well-defined standards. Ideally,
 I'd classify them with a LLM and LangChain, then run validation on it to double check the classifications. Here's the i
ssue: I'm a little lost. I've built smaller-scale RAG systems, but I have no idea how to do this at scale. Any help woul
d be greatly appreciated.

Big apologies if I shouldn't be posting the question here.
```
---

     
 
all -  [ Framework recommendation for a RAG project with LaTeX source files ](https://www.reddit.com/r/LangChain/comments/1g3gza0/framework_recommendation_for_a_rag_project_with/) , 2024-10-15-0913
```
Hi, I want to build a custom RAG application for question-answering on PDF files where I already have the LaTeX source.


  
The files have been parsed into LaTeX fragments and I have extracted metadata such as equation labels + LaTeX source
, what LaTeX source corresponds to which pages, and so on. All of this data is stored in a database. Different user will
 have access to different subsets of the LaTeX files.

The AI component will be build into an existing website (django),
 i.e. I would ideally like to answer questions such as:

-  Can you explain concept Y (it should be answered by any part
 of the material that has been made available)

-  Can you tell me what this file is about (the request will contain the
 file id)

- Can you explain what this page is about? (the request will contain the file id and page number,; but the ap
plication needs to understand that 'this page'  corresponds to the context associated with the file id and page number)




My current approach uses django vectordb plus custom queries/chunking but this is not very good. Ideally I would like
 an application where I can 'handfeed' it the LaTeX sources and metadata and use the library to do the RAG part. It is i
mportant that it replies with references to relevant text (if any) and it should also function in conversational mode.


I would like it to work with different endpoints and it is important that I can stream the response to the end-user (i.e
. it should respond with an iterator or similar).

Any guides or library recommendations would be highly appreciated!
```
---

     
 
all -  [ Similar tool like LangChain in GO ](https://www.reddit.com/r/golang/comments/1g3gqli/similar_tool_like_langchain_in_go/) , 2024-10-15-0913
```
Hey, I found this langChan tool from twitter. I'm more familiar to Golang, Does anyone know if there is alternative to t
his in Golang  
[https://python.langchain.com/docs/integrations/tools/](https://python.langchain.com/docs/integrations/t
ools/)
```
---

     
 
all -  [ Multi-Hop Agent with Langchain, Llama3, and Human-in-the-Loop for the Google Frames Benchmark ](https://www.reddit.com/r/LocalLLaMA/comments/1g3g365/multihop_agent_with_langchain_llama3_and/) , 2024-10-15-0913
```
In this notebook, I walk through how to create an agent using Langchain to solve the complex **Google Frames Benchmark**
 dataset. This agent leverages Wikipedia as a knowledge base to handle multi-hop reasoning tasks, with human reviewers p
roviding feedback via **Argilla** to improve its performance.

The **Frames-Benchmark** dataset is useful for building a
nd testing multi-hop retrieval and reasoning models. It consists of 824 challenging questions that require information r
etrieval from multiple Wikipedia articles (anywhere from 2 to 15 articles). These questions span diverse topics such as 
history, science, and health and are labeled based on reasoning types—numerical, tabular, multiple constraints, temporal
, and post-processing.

The human-in-the-loop feedback through **Argilla** helps make the agent’s thought process more t
ransparent and easier to refine with prompts.

Baseline results for the dataset show an accuracy range from **41% with b
asic prompting** to **66% for multi-step retrieval and reasoning**, indicating a lot of room for further improvements.


[LINK TO THE NOTEBOOK](https://github.com/argilla-io/argilla-cookbook/blob/main/multihop_langchain_frames_benchmark.ipyn
b)
```
---

     
 
all -  [ Build Your Own ChatGPT Clone with LangChain, Streamlit, and Ollama ](https://www.reddit.com/r/u_bluebashllc/comments/1g3ffq1/build_your_own_chatgpt_clone_with_langchain/) , 2024-10-15-0913
```
[Build Your Own ChatGPT Clone with LangChain, Streamlit, and Ollama](https://preview.redd.it/7dx6thfk1qud1.png?width=192
0&format=png&auto=webp&s=423a0defa28fb16eb889b261d42c7864750d613e)

Building your own [ChatGPT clone](https://www.blueba
sh.co/blog/build-chatgpt-clone-ollama-langchain-streamlit-rag/) is now easier with tools like Ollama, LangChain, and Str
eamlit RAG! Ollama provides an efficient way to run language models locally, while LangChain handles the integration and
 orchestration of various AI components. Use **RAG with LangChain** to provide context to the bot—allowing the chatbot t
o use information grabbed in real-time from uploaded files, offering far more accurate answers. Deploy the app by runnin
g your Streamlit interface, and voilà—you’ve created your own personal ChatGPT-like chatbot for real-world use!

**Impor
tant Tools**

**Ollama:** the central language model doing the talking.

**Streamlit:** Easy framework for writing web a
pplications. Could be helpful in building a front end for the chatbot.

**LangChain:** It integrates RAG, whereby you al
low your bot to retrieve information from other documents you have loaded.

**How to Build:**

**Set up environment**

I
nstall LangChain, Streamlit, and Ollama packages in your system.

**Create an Interface on Streamlit:** This is where th
e users will interact with the bot. There would be an uploading file feature where the users can upload files that will 
be used to provide context to the bot.

**Use RAG with LangChain:** The chatbot will use information grabbed in real-tim
e from uploaded files through LangChain and give far more accurate answers.

**Deploy the App:** Finally, you would just
 run your Streamlit app, and voilà. You've created your own personal ChatGPT-like chatbot for use.
```
---

     
 
all -  [ create_csv_agent fails to work on llama 3.1 70b through ollama. Which open-source model is compatibl ](https://www.reddit.com/r/LangChain/comments/1g3ex5n/create_csv_agent_fails_to_work_on_llama_31_70b/) , 2024-10-15-0913
```
I need a private model that works well on create_csv_agent. Gpt-4o was doing wonders but I don't want to entrust my comp
any's data to openai. I need a private in house model that can achieve this. What should I do? Which model worked for yo
u guys?
```
---

     
 
all -  [ How do you currently handle tasks that your AI agents cannot complete? ](https://www.reddit.com/r/LangChain/comments/1g3en5x/how_do_you_currently_handle_tasks_that_your_ai/) , 2024-10-15-0913
```
What challenges or inefficiencies do you face when integrating human intervention?
```
---

     
 
all -  [ RAG metadata ](https://www.reddit.com/r/LangChain/comments/1g3d0vg/rag_metadata/) , 2024-10-15-0913
```
Hello everyone! 

  
I'm building a RAG agent in LangGraph for production scale. On a small text files I used to send th
e whole content to the LLM so it generates some metadata about it, but for production level that won't be efficient beca
use the PDF size could be large. On the other hand if I created the metadata from the PDF's chunks they will be meaning 
less!! so how do you achieve that?

Thanks in advance, great community. <3

Co-founder, Shaareable Apps


```
---

     
 
all -  [  Major updates to XeroFlow node-based LLM tool ](https://www.reddit.com/r/ollama/comments/1g39vzo/major_updates_to_xeroflow_nodebased_llm_tool/) , 2024-10-15-0913
```
I just finished up a bunch of updates fixing issues dealing with the installer and a couple other minor issues in the pr
ogram. If you're not familiar with this tool it is a node-based llm tool that allows you to set up workflows to interact
 with and process data utilizing multiple llms. One of the updates it has now is it is able to utilize custom Vector dat
abases utilizing RAG and Langchain.    
For those of you who don't use Windows, just make sure you have python and pip i
nstalled and install using the requirements.txt file, once this is done then you can just run the [main.py](http://main.
py) file directly.

check it out here: [https://github.com/Xerophayze/XeroFlow](https://github.com/Xerophayze/XeroFlow)


https://preview.redd.it/3n41uzsx3oud1.png?width=752&format=png&auto=webp&s=b51db5d1e695a470f717bcbee12ac2c727424497

ht
tps://preview.redd.it/vh99khhq3oud1.png?width=1130&format=png&auto=webp&s=fe7d2b8216d295ce0fe6323f2d0623edd0c10acc

http
s://preview.redd.it/qshhx1iq3oud1.png?width=752&format=png&auto=webp&s=05bfb8aee6f3bd913ef68193947cd12e889d52bc

https:/
/preview.redd.it/pkxh0ghq3oud1.png?width=752&format=png&auto=webp&s=bb3ad0debd767995f625eafcb7e6023e35ba6e6a

https://pr
eview.redd.it/qe6m3ghq3oud1.png?width=857&format=png&auto=webp&s=5f6981fea7e4f314faed32ae4e451ad5fbcd1975


```
---

     
 
all -  [ Latest version of XeroFlow Node based LLM tool ](https://www.reddit.com/r/StableDiffusion/comments/1g39t3b/latest_version_of_xeroflow_node_based_llm_tool/) , 2024-10-15-0913
```
Hey everyone! Just fixed the issues with the installer for our tool. Make sure you have Python 3.10.9 installed; it shou
ld come with pip, but if not, you may need to install it separately. Once that's set, run the `setup.bat` file to instal
l all required dependencies—this may take a few minutes. When it’s done, you can launch the program by running `run.bat`
.

Also, I've left the API endpoints set up; just add your own API keys for OpenAI or Groq, and if you’re running a loca
l install or have Ollama on your system, simply adjust the IP address or hostname in the URL for those APIs.

This tool 
includes a vector database utilizing RAG and Langchain, with a sample document (an 80-90k word sci-fi novel that was wri
tten by the long form content node!) included in the database folder for you to check out. I'll be putting together a tu
torial video soon, so stay tuned!  
[https://github.com/Xerophayze/XeroFlow](https://github.com/Xerophayze/XeroFlow)

ht
tps://preview.redd.it/ccyzt0wp2oud1.png?width=1069&format=png&auto=webp&s=c6e27de025751899e508849e0fb1b9297921e7c2

http
s://preview.redd.it/c8xvguvp2oud1.png?width=1130&format=png&auto=webp&s=a7126f20e8c9844e0bf329ff6c7085ed8407a875

https:
//preview.redd.it/rft6bvvp2oud1.png?width=752&format=png&auto=webp&s=8cc31d58f5534c49c0ccc2e7a9709793cae2a919

https://p
review.redd.it/cv7p9gwp2oud1.png?width=752&format=png&auto=webp&s=5190ad7a57036e2fd037e248437d3ff8bf8f3ef5

https://prev
iew.redd.it/494kpuvp2oud1.png?width=857&format=png&auto=webp&s=a1e234ec05dc62b1820147e4f053d4a5a8ff3bd3


```
---

     
 
all -  [ Need help to create template for RAG app ](https://www.reddit.com/r/LangChain/comments/1g39p3h/need_help_to_create_template_for_rag_app/) , 2024-10-15-0913
```
I am creating a RAG application where I will be giving LLM a large set of responses array of objects where there will be
 multiple questions and it's answer provided by the user.  
For example :

    { 'responses': [ 
    { 'answers': [ 
   
   { 
        'question': 'WHAT IS YOUR NAME',
         'response': 'ABCD'
       }, {
       'question': 'What is your 
AGE',
       'response': '30' 
      } 
    ] },
     { 'answers': [ 
      { 'question': 'WHAT IS YOUR NAME',
       'r
esponse': 'ABCD'
       },
         { 'question': 'What is your AGE',
           'response': '30'
         } 
      ] },

      ...
     ]
    }

This is my current template :-

    Use the following pieces of context to answer the question.

      If you don't know the answer, just say that you don't know, don't try to make up an answer.
      Always say 'tha
nks for asking!' at the end of the answer.
      Don't provide any code for doing just provide the output.
      Conside
r the given context as document don't provide answer as a json data consider it as document.
      which contain informa
tion about all the responses for a particular form.
      The answer to a particular question is inside the response fie
ld, always provide the question along with response and make sure not to repeat the question.
      The given context is
 a array of user responses and each object is a response responded by a particular user.
      Consider all the users re
sponse before answering.
      {context}
    
      Question: {question}
      Helpful Answer:

Also whenever I ask it q
uestions it provides the answer on the basis of top 2 matches, if the number of questions are like 10, and If I ask it t
o 'give me all the questions present in the form' it gives only 2.
```
---

     
 
all -  [ Do I need to pay for unit test with langsmith library? ](https://www.reddit.com/r/LangChain/comments/1g33fsy/do_i_need_to_pay_for_unit_test_with_langsmith/) , 2024-10-15-0913
```
Pretty simple question I think?

I was reading the following:

[https://docs.smith.langchain.com/how\_to\_guides/evaluat
ion/unit\_testing](https://docs.smith.langchain.com/how_to_guides/evaluation/unit_testing)

But I don't get if I need to
 use the LangSmith web app to see the results or I can simply use the langsmith library to run my unit tests and get the
 results without the tracing.. Is this doable?

Is the use of the web app mandatory? Or langsmith can be used solely as 
a library without the tracing?

Thank you in advance!
```
---

     
 
all -  [ Which framework between haystack, langchain and llamaindex, or others? ](https://www.reddit.com/r/Rag/comments/1g31urm/which_framework_between_haystack_langchain_and/) , 2024-10-15-0913
```
The use case is the following.
Database: vector database with 10k scientific articles.
User needs: the user will need th
e chatbot both for advanced research on the dataset and chat with those results. 

Please let me know your advices!! 
```
---

     
 
all -  [ [Hiring][Remote] Software Engineer ](https://www.reddit.com/r/jobbit/comments/1g31h8x/hiringremote_software_engineer/) , 2024-10-15-0913
```
* Full-time opportunity
* Remote
* Compensation - $125k - $190k
* 4+ years of experience
* Experience with one or more o
f the following areas (or related technologies): 
   * Modern web/backend technologies: React, Typescript, Node, Next, P
ython
   * AI techniques and workflows: LLMs, RAG, Langchain, CoreML
   * Mobile development: Flutter (Dart), iOS (Swift
), Android (Kotlin)
   * Cloud platforms/infrastructure: GCP, AWS, Azure, Docker
   * Databases: Relational (PostgreSQL,
 MySQL) or Non-relational (MongoDB, Firestore)

Apply - [https://peerlist.io/company/squint/careers/software-engineer/jo
bhkknpn86qnjqbk2jaqlrngdperq](https://peerlist.io/company/squint/careers/software-engineer/jobhkknpn86qnjqbk2jaqlrngdper
q)
```
---

     
 
all -  [ [Hiring][Remote] Software Engineer ](https://www.reddit.com/r/RemoteJobHunters/comments/1g31erw/hiringremote_software_engineer/) , 2024-10-15-0913
```
* Full-time opportunity
* Remote 
* Compensation - $125k - $190k
* 4+ years of experience
* Experience with one or more 
of the following areas (or related technologies): 
   * Modern web/backend technologies: React, Typescript, Node, Next, 
Python
   * AI techniques and workflows: LLMs, RAG, Langchain, CoreML
   * Mobile development: Flutter (Dart), iOS (Swif
t), Android (Kotlin)
   * Cloud platforms/infrastructure: GCP, AWS, Azure, Docker
   * Databases: Relational (PostgreSQL
, MySQL) or Non-relational (MongoDB, Firestore)

Apply - [https://peerlist.io/company/squint/careers/software-engineer/j
obhkknpn86qnjqbk2jaqlrngdperq](https://peerlist.io/company/squint/careers/software-engineer/jobhkknpn86qnjqbk2jaqlrngdpe
rq)
```
---

     
 
all -  [ Idea: Interest in a competition model to build agents for businesses ](https://www.reddit.com/r/LangChain/comments/1g2zpr3/idea_interest_in_a_competition_model_to_build/) , 2024-10-15-0913
```
Imagine there was a platform whereby a business spec for a workflow (e.g. creating facebook ads) was understood.

Now le
ts assume the business who was interested in creating an agent for this commonly repeated workflow didn't have the resou
rces to do it and there wasn't a reasonable substitute already on the market.

The super simple spec might look somethin
g like:

* **Objective**: from a list of 100 ideas, create five 10s video variants from supplied Napkin Pitches for each
.
* **Constraints:**
   * At least 5 videos from the 500 created videos must pass a qualitative review and be selected
 
  * The total cost to me, the business, must be X or less
   * The total time to generate must be Y or less

Let's assum
e this business offers a $2000 prize for the winning submission (as judged by performance against the constraints) under
 a fixed contest length duration (e.g. 2 weeks). If you won, you'd secure the prize and your source code would be made a
vailable to the business + potentially made open for others to consume.

Without knowing more, if a platform and paradig
m like this existed, would you be interested in participating?
```
---

     
 
all -  [ All-In-One Tool for LLM Evaluation ](https://www.reddit.com/r/LangChain/comments/1g2z2q1/allinone_tool_for_llm_evaluation/) , 2024-10-15-0913
```
I was recently trying to build an app using LLMs but was having a lot of difficulty engineering my prompt to make sure i
t worked in every case. 

So I built this tool that automatically generates a test set and evaluates my model against it
 every time I change the prompt. The tool also creates an api for the model which logs and evaluates all calls made once
 deployed.

https://reddit.com/link/1g2z2q1/video/a5nzxvqw2lud1/player

Please let me know if this is something you'd fi
nd useful and if you want to try it and give feedback! Hope I could help in building your LLM apps!
```
---

     
 
all -  [ Extracting Regex Patterns from Strings - Trying to Think of Techniques to Improve ](https://www.reddit.com/r/LangChain/comments/1g2y6o4/extracting_regex_patterns_from_strings_trying_to/) , 2024-10-15-0913
```
Recently I've been working on a project that requires me to generate a ton of regex patterns from a large amount of stri
ngs. These strings can be in any form and may or may not have a pattern in them. An example of my use case would be tryi
ng to extract all of the names of people from a sentence. I need to generate both the name and the reusable regex patter
n required to extract the name in future strings. For example, in the string 'John Doe went to the store', the goal of t
he system would be to extract 'John Doe' with a regex pattern of '\^\\s\*John\\s+Doe'. The regex pattern just needs to b
e able to match to another sentence like 'I went to dinner with John Doe'. Both of those sentences would be able to be m
atched from the regex pattern generated from the first pattern.

There is a hidden complexity in that the sentence could
 be something like 'George walked his dog Max'. In this case, 'George' would be the desired extraction, rather than 'Max
'.

Right now, I am using two different LangChain functions to extract these patterns. One of them extracts the name wit
h some simple prompt engineering as well as a couple few-shot examples of names and sentences. The other generates the r
egex pattern with a similar approach of using some prompt engineering and few-shot examples.

The problem that I am havi
ng right now is that my accuracy has hit a ceiling. I am currently sitting at around 60% accuracy on the strings. Most o
f the strings are incredibly complex and either have a ton of noise, or they have multiple names and determining which o
ne is correct is non-trivial. Are there any techniques that could be used to help my use case?

Thanks for any help!
```
---

     
 
all -  [ Open-Source Embodied Agents from NASA/JPL ](https://youtu.be/mZTrSg7tEsA?si=r6_56O0O38lxQSaM) , 2024-10-15-0913
```
Hey r/robotics 👋

We recently shared a preprint of an upcoming IEEE article about ROSA: the Robot Operating System Agent
 (https://arxiv.org/abs/2410.06472).

ROSA works with ROS/ROS2 and popular language models like GPT-4o and Llama3.1 to m
ake it easy for humans to interact with robots using natural language. Check out the demo video to see what this new way
 of building and operating robots can do.

The project is open-source and can be easily added to existing ROS/ROS2 proje
cts. Just type ‘pip install jpl-rosa’ and you’ll be able to create an agent in a few lines of code. You can also customi
ze the agent with Robot System Prompts and your own custom tools using the LangChain standard for tool creation. There a
re lots of examples on the repository (https://github.com/nasa-jpl/rosa) and Wiki (https://github.com/nasa-jpl/rosa/wiki
).

We’d love to hear from you and are open to collaboration with the community. Let us know what you think!
```
---

     
 
all -  [ From Beginner to Problem-Solving Pro: The Ultimate Guide to Mastering Python ](https://www.reddit.com/r/BMSCE/comments/1g2qopn/from_beginner_to_problemsolving_pro_the_ultimate/) , 2024-10-15-0913
```


> If you want to become exceptional at something, you need the right guidance and a relentless focus on practice. Prob
lem-solving with Python is no different. Whether you're a beginner or already have some Python experience, here’s a dist
illed guide to the best resources that will take you from zero to hero.

---

**Interactive Platforms: Learn by Doing**

   - **LeetCode**: The go-to platform for sharpening your algorithmic skills. Problems range from easy to hard, perfect 
for anyone targeting tech interviews or leveling up their problem-solving skills. 
     - [Start Here](https://leetcode.
com/problemset/all/?difficulty=EASY&page=1&tag=python)
   
   - **HackerRank**: Solid for beginners, offering a well-str
uctured Python track. Good to build confidence before diving into harder challenges.
     - [Explore Python Track](https
://www.hackerrank.com/domains/tutorials/10-days-of-python)
   
   - **CodeSignal**: Ideal for those who want to challeng
e themselves with real-world coding tests and company-specific problems.
     - [Check it out](https://codesignal.com/)

   
   - **Codewars**: Solve community-created 'kata' and see how others think. A great way to learn different problem-s
olving techniques.
     - [Start solving](https://www.codewars.com/)

**The Best Courses: From Concept to Code**
   - **
'Python for Everybody' by University of Michigan on Coursera**: More than just Python basics, this course teaches you ho
w to think like a programmer.
     - [Enroll for Free](https://www.coursera.org/specializations/python)
   
   - **'Mast
ering Data Structures & Algorithms using Python' on Udemy**: Deep dive into solving complex problems with Python. Great 
if you want to understand the 'why' behind each solution.
     - [Course Link](https://www.udemy.com/course/python-for-d
ata-structures-algorithms-and-interviews/)
   
   - **MIT's 'Computational Thinking using Python' on EdX**: Not just cod
ing, but thinking like a computer scientist. Highly recommended for those who want to develop a strong foundation.
     
- [Learn More](https://www.edx.org/course/introduction-to-computer-science-and-programming-using-python)

**Essential Re
ads: From Beginner to Pro**
   - **'Python Programming: An Introduction to Computer Science' by John Zelle**: A clear an
d practical introduction to Python and problem-solving.
   - **'Automate the Boring Stuff with Python' by Al Sweigart**:
 Real-world examples make it easy to apply Python to everyday tasks.
   - **'Elements of Programming Interviews in Pytho
n'**: A no-nonsense guide to mastering interview-style problems.
   - **'Python Crash Course' by Eric Matthes**: Packed 
with hands-on exercises to quickly improve your coding and problem-solving.

**Tutorials & Blogs: Sharpen Your Edge**
  
 - **Real Python**: Clean, insightful tutorials on Python and algorithms. Great if you like to learn through reading.
  
   - [Visit Real Python](https://realpython.com/)
   
   - **GeeksforGeeks**: An extensive repository of problems, expla
nations, and Python solutions.
     - [Explore GeeksforGeeks](https://www.geeksforgeeks.org/python-programming-language/
)
   
   - **LeetCode Discuss**: Community-driven solutions and problem-solving discussions, especially valuable for int
erview prep.
     - [Join the Community](https://leetcode.com/discuss/)

**YouTube: Bite-sized Mastery**
   - **Tech Wit
h Tim**: Problem-solving tutorials, coding challenges, and practical examples.
     - [Tech With Tim](https://www.youtub
e.com/c/TechWithTim)
   
   - **CS Dojo**: Easy-to-follow explanations of algorithms with Python.
     - [CS Dojo](https
://youtube.com/@csdojo?si=lMjat_rv-c9FPqHM) 
   
   - **Kite**: Quick tutorials focusing on coding challenges.
     - [K
ite on YouTube](https://youtube.com/@kitehq?si=YuqpJYwBGpUDi3pt) 

**Competitive Programming: Level Up Your Skills**
   
- **TopCoder**: For those who thrive on solving complex challenges against the clock.
     - [TopCoder Python Track](htt
ps://www.topcoder.com/)
   
   - **Codeforces**: Real-time contests that test your coding speed and efficiency.
     - [
Start Competing](https://codeforces.com/)
   
   - **Exercism.io**: Solve problems and get feedback from mentors—perfect
 if you value personal growth.
     - [Join Exercism](https://exercism.io/tracks/python)

**DSA Resources: Become Unstop
pable**
   - **NeetCode**: Curated problem sets and videos that make DSA simpler to understand.
     - [NeetCode Resourc
es](https://neetcode.io/)
   
   - **AlgoExpert**: If you can invest, this is gold. Get high-quality explanations and ch
allenges.
     - [Check out AlgoExpert](https://www.algoexpert.io/)
   
   - **'Introduction to Algorithms' (CLRS)**: A 
classic. Pair it with Python and tackle the hardest problems.

---

**The Truth About Mastery**: 
> 'Learning to solve p
roblems with Python is not just about syntax, it’s about developing a mind that can break down complexity into simplicit
y. The key is practice, consistency, and a hunger for real understanding.' 

You don’t need a hundred resources; you nee
d focus. Pick a few from this list and dive deep. You'll be amazed at what you can achieve.

---

This guide should be a
 helpful launchpad, whether you're aiming for coding interviews, leveling up for competitive programming, or just love s
olving problems. What’s your favorite resource? Drop your go-to recommendations below!


**Additional 🔗 to some of the l
atest Python libraries :**

- [Polars](https://www.pola.rs/)
- [DuckDB](https://duckdb.org/)
- [PyCaret](https://pycaret
.gitbook.io/docs/)
- [JAX](https://jax.readthedocs.io/en/latest/)
- [LangChain](https://github.com/hwchase17/langchain)

- [LightGBM](https://lightgbm.readthedocs.io/en/latest/)
- [Caffe2](https://caffe2.ai/)
- [Transformers (Hugging Face)](
https://github.com/huggingface/transformers)
- [PyOD](https://pyod.readthedocs.io/en/latest/)
- [Plotly](https://plotly.
com/python/)
- [Bokeh](https://docs.bokeh.org/en/latest/)
- [Pydot](https://github.com/pydot/pydot) 

These links provid
e documentation and details for each library, making it easier to explore and integrate them into your projects.
```
---

     
 
all -  [ Mastering Problem-Solving with Python: A Curated Path for the Driven ](https://www.reddit.com/r/DTU__Delhi/comments/1g2qebd/mastering_problemsolving_with_python_a_curated/) , 2024-10-15-0913
```


> If you want to become exceptional at something, you need the right guidance and a relentless focus on practice. Prob
lem-solving with Python is no different. Whether you're a beginner or already have some Python experience, here’s a dist
illed guide to the best resources that will take you from zero to hero.

---

**Interactive Platforms: Learn by Doing**

   - **LeetCode**: The go-to platform for sharpening your algorithmic skills. Problems range from easy to hard, perfect 
for anyone targeting tech interviews or leveling up their problem-solving skills. 
     - [Start Here](https://leetcode.
com/problemset/all/?difficulty=EASY&page=1&tag=python)
   
   - **HackerRank**: Solid for beginners, offering a well-str
uctured Python track. Good to build confidence before diving into harder challenges.
     - [Explore Python Track](https
://www.hackerrank.com/domains/tutorials/10-days-of-python)
   
   - **CodeSignal**: Ideal for those who want to challeng
e themselves with real-world coding tests and company-specific problems.
     - [Check it out](https://codesignal.com/)

   
   - **Codewars**: Solve community-created 'kata' and see how others think. A great way to learn different problem-s
olving techniques.
     - [Start solving](https://www.codewars.com/)

**The Best Courses: From Concept to Code**
   - **
'Python for Everybody' by University of Michigan on Coursera**: More than just Python basics, this course teaches you ho
w to think like a programmer.
     - [Enroll for Free](https://www.coursera.org/specializations/python)
   
   - **'Mast
ering Data Structures & Algorithms using Python' on Udemy**: Deep dive into solving complex problems with Python. Great 
if you want to understand the 'why' behind each solution.
     - [Course Link](https://www.udemy.com/course/python-for-d
ata-structures-algorithms-and-interviews/)
   
   - **MIT's 'Computational Thinking using Python' on EdX**: Not just cod
ing, but thinking like a computer scientist. Highly recommended for those who want to develop a strong foundation.
     
- [Learn More](https://www.edx.org/course/introduction-to-computer-science-and-programming-using-python)

**Essential Re
ads: From Beginner to Pro**
   - **'Python Programming: An Introduction to Computer Science' by John Zelle**: A clear an
d practical introduction to Python and problem-solving.
   - **'Automate the Boring Stuff with Python' by Al Sweigart**:
 Real-world examples make it easy to apply Python to everyday tasks.
   - **'Elements of Programming Interviews in Pytho
n'**: A no-nonsense guide to mastering interview-style problems.
   - **'Python Crash Course' by Eric Matthes**: Packed 
with hands-on exercises to quickly improve your coding and problem-solving.

**Tutorials & Blogs: Sharpen Your Edge**
  
 - **Real Python**: Clean, insightful tutorials on Python and algorithms. Great if you like to learn through reading.
  
   - [Visit Real Python](https://realpython.com/)
   
   - **GeeksforGeeks**: An extensive repository of problems, expla
nations, and Python solutions.
     - [Explore GeeksforGeeks](https://www.geeksforgeeks.org/python-programming-language/
)
   
   - **LeetCode Discuss**: Community-driven solutions and problem-solving discussions, especially valuable for int
erview prep.
     - [Join the Community](https://leetcode.com/discuss/)

**YouTube: Bite-sized Mastery**
   - **Tech Wit
h Tim**: Problem-solving tutorials, coding challenges, and practical examples.
     - [Tech With Tim](https://www.youtub
e.com/c/TechWithTim)
   
   - **CS Dojo**: Easy-to-follow explanations of algorithms with Python.
     - [CS Dojo]( http
s://youtube.com/@csdojo?si=lMjat_rv-c9FPqHM) 
   
   - **Kite**: Quick tutorials focusing on coding challenges.
     - [
Kite on YouTube](https://youtube.com/@kitehq?si=YuqpJYwBGpUDi3pt) 

**Competitive Programming: Level Up Your Skills**
  
 - **TopCoder**: For those who thrive on solving complex challenges against the clock.
     - [TopCoder Python Track](ht
tps://www.topcoder.com/)
   
   - **Codeforces**: Real-time contests that test your coding speed and efficiency.
     - 
[Start Competing](https://codeforces.com/)
   
   - **Exercism.io**: Solve problems and get feedback from mentors—perfec
t if you value personal growth.
     - [Join Exercism](https://exercism.io/tracks/python)

**DSA Resources: Become Unsto
ppable**
   - **NeetCode**: Curated problem sets and videos that make DSA simpler to understand.
     - [NeetCode Resour
ces](https://neetcode.io/)
   
   - **AlgoExpert**: If you can invest, this is gold. Get high-quality explanations and c
hallenges.
     - [Check out AlgoExpert](https://www.algoexpert.io/)
   
   - **'Introduction to Algorithms' (CLRS)**: A
 classic. Pair it with Python and tackle the hardest problems.

---

**The Truth About Mastery**: 
> 'Learning to solve 
problems with Python is not just about syntax, it’s about developing a mind that can break down complexity into simplici
ty. The key is practice, consistency, and a hunger for real understanding.' 

You don’t need a hundred resources; you ne
ed focus. Pick a few from this list and dive deep. You'll be amazed at what you can achieve.

---

This guide should be 
a helpful launchpad, whether you're aiming for coding interviews, leveling up for competitive programming, or just love 
solving problems. What’s your favorite resource? Drop your go-to recommendations below!


 **Latest Python libraries bel
ow:**

- [Polars](https://www.pola.rs/)
- [DuckDB](https://duckdb.org/)
- [PyCaret](https://pycaret.gitbook.io/docs/)
- 
[JAX](https://jax.readthedocs.io/en/latest/)
- [LangChain](https://github.com/hwchase17/langchain)
- [LightGBM](https://
lightgbm.readthedocs.io/en/latest/)
- [Caffe2](https://caffe2.ai/)
- [Transformers (Hugging Face)](https://github.com/hu
ggingface/transformers)
- [PyOD](https://pyod.readthedocs.io/en/latest/)
- [Plotly](https://plotly.com/python/)
- [Bokeh
](https://docs.bokeh.org/en/latest/)
- [Pydot](https://github.com/pydot/pydot) 

These links provide documentation and d
etails for each library, making it easier to explore and integrate them into your projects.
```
---

     
 
all -  [ Generate <-> Validation for chat ](https://www.reddit.com/r/LangChain/comments/1g2n6tj/generate_validation_for_chat/) , 2024-10-15-0913
```
I'm building a chatbot with langgraph. To reduce errors, I've created a validation node which works like 

- Generator n
ode generates the response based on customer input

- Then the generation is sent to a validator. If the validation is s
uccessful, send the response to customers

- Else, send the response back to generator with feedback to regenerate. 

  

Facing trouble implementing this w.r.t storing history and getting the proper response from validation. Has anyone done
 anything similar to this? 
```
---

     
 
all -  [ 401 Unauthorized Error with Jina AI Embeddings API in Flask App – Need Help Troubleshooting ](https://www.reddit.com/r/LangChain/comments/1g2mlon/401_unauthorized_error_with_jina_ai_embeddings/) , 2024-10-15-0913
```
Hey Redditors!

I’m working on a Flask app that uses the Jina AI Embeddings API to process and embed document text. The 
app runs fine locally, but when I try to query the Jina API for embeddings, I keep getting the following error in the lo
gs:

(did this in my env itself)

https://preview.redd.it/3yt5h0052iud1.png?width=926&format=png&auto=webp&s=79eac415c74
3aa93730b847317030ede9fab1be0

It seems like the API request is being rejected due to an authorization issue, but I’m no
t sure why, since I’m including the API key in the headers as a Bearer token. Here's the relevant part of my \`app.py\` 
code where I make the request to Jina:

https://preview.redd.it/vnb5w0a62iud1.png?width=812&format=png&auto=webp&s=64c25
fa32f350c6807ee01766372d99ef0562342

and hence this at the end

https://preview.redd.it/kjkwrdx72iud1.png?width=1023&for
mat=png&auto=webp&s=3a21d3b521520cb5e48c18b7c1d8622cb5135bdc

Here’s what I’ve checked so far:

1. API Key: I’ve confirm
ed that my \`JINAAI\_API\_KEY\` is correct and stored in my environment variables.
2. Flask App Setup: My Flask app runs
 successfully on \`localhost:5000\`, and I'm using ngrok to tunnel traffic externally.
3. ngrok: The external URL works 
fine for other routes, but the API request to Jina still fails with a 401 error.

Any ideas on why this could be happeni
ng? Could it be something with the API key, headers, or maybe an issue with the way I’m handling the request?

Any advic
e would be greatly appreciated!

Thanks in advance!


```
---

     
 
all -  [ Text to SQL Public Chatbot ](https://www.reddit.com/r/LangChain/comments/1g2j6ro/text_to_sql_public_chatbot/) , 2024-10-15-0913
```
Hello all,

have you ever implemented a public chatbot that is able to query the DB ? What are the guardrails you put in
 place to avoid data leaking and breachs? 

I am thinking in a project where the chatbot will be available in a website 
where not logged people can use it and looking for the security piece on it besides row leves securities in the db
```
---

     
 
all -  [ What's the most efficient way to handle references like figures, tables or other sections in a RAG p ](https://i.redd.it/dsojnplzrgud1.png) , 2024-10-15-0913
```
 I could think of two ways and I'm currently implementing both. In my usecase, I'm converting all pages in a document ar
e into image format and using a multimodal llm for querying. Once I retrieve a relevant image, if there are external ref
erences,

A. Do RAG once more to retrieve the reference.

B. Identify all the references initially using the index page 
and parse and store them separately in a folder as images

With A, there are chances of RAG identifying just plain refer
ences elsewhere and not the actual definition

With B, there is a chance that some references might not be extracted cor
rectly
```
---

     
 
MachineLearning -  [ [D] How are folks building conversational Retrieval Augmented Generation apps ](https://www.reddit.com/r/MachineLearning/comments/1ftdby7/d_how_are_folks_building_conversational_retrieval/) , 2024-10-15-0913
```
I've read through various resources such as:  
- [https://vectorize.io/how-i-finally-got-agentic-rag-to-work-right/](htt
ps://vectorize.io/how-i-finally-got-agentic-rag-to-work-right/)  
- [https://python.langchain.com/docs/tutorials/qa\_cha
t\_history/](https://python.langchain.com/docs/tutorials/qa_chat_history/)  
- [https://langchain-ai.github.io/langgraph
/tutorials/rag/langgraph\_agentic\_rag/](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_agentic_rag/) 
 
- [https://docs.llamaindex.ai/en/stable/module\_guides/deploying/chat\_engines/](https://docs.llamaindex.ai/en/stable/
module_guides/deploying/chat_engines/)  
- [https://huggingface.co/datasets/nvidia/ChatRAG-Bench](https://huggingface.co
/datasets/nvidia/ChatRAG-Bench) 

But these feel overly reductive, since they don't address complexities like:  
1) when
 to retrieve vs. just respond immediately to reduce latency  
2) rely on existing context previously retrieved in the co
nversation instead of retrieving again at the current turn  
3) partition LLM context between retrieved information and 
past conversation history.

I'm sure some teams already have good systems for this, would appreciate pointers!
```
---

     
 
MachineLearning -  [ Built a web agent which call fill Google forms based on the user details [P] ](https://www.reddit.com/r/MachineLearning/comments/1fozud5/built_a_web_agent_which_call_fill_google_forms/) , 2024-10-15-0913
```
GitHub repo : [https://github.com/shaRk-033/web-agent](https://github.com/shaRk-033/web-agent)

Tried to solve it using 
two approaches:

# 1: Basic Scraping and Filling

This is the straightforward approach. The agent scrapes the form’s HTM
L and uses fixed XPaths to find and fill in the required fields.

* It pulls the form’s HTML, locates the fields with se
t XPaths, and inputs the answers. It’s a direct and simple method.
* If the form changes or an element isn’t where it’s 
expected, the process can fail and may need manual adjustments.

[basic approach](https://preview.redd.it/5e8g4a1k4xqd1.
png?width=1055&format=png&auto=webp&s=d8e984e4feaee2f0453b08c8696768c40a2a5c20)

2. Using LangChain Agents and tool call
ing

* LangChain Agent**:** The agent handles everything by using the LLM’s reasoning to decide what to do next, includi
ng generating those tricky XPaths.
* Error Handling**:** If something goes wrong (like an element not found), the agent 
tries again with better XPaths until it gets the job done.

[using langchain agents](https://preview.redd.it/948i88pl4xq
d1.png?width=782&format=png&auto=webp&s=ed1e6c19efec9f4cbbbd6ab5a22558f221cf745f)

Any recommendations to improve this w
ould be welcome. Also, if anyone has ideas on building similar web agents to automate other tasks, it would be great to 
hear them. :)
```
---

     
 
MachineLearning -  [ [P] Swapping Embedding Models for an LLM ](https://www.reddit.com/r/MachineLearning/comments/1fktvbj/p_swapping_embedding_models_for_an_llm/) , 2024-10-15-0913
```
How tightly coupled is an embedding model to a language model?

Taking an example from Langchain's tutorials, they use O
llama's _nomic-embed-text_ for embedding and _Llama3.1_ for the understanding and Q/A. I don't see any documentation abo
ut Llama being built on embeddings from this embedding model. 

Intuition suggests that a different embedding model may 
produce outputs of other sizes or produce a different tensor for a character/word, which would have an impact on the res
ults of the LLM. So would changing an embedding model require retraining/fine-tuning the LLM as well?

I need to use a e
mbedding model for code snippets and text. Do I need to find a specialized embedding model for that? If yes, how will ll
ama3.1 ingest the embeddings?
```
---

     
 
deeplearning -  [ What is the best approach for Parsing and Retrieving Code Context Across Multiple Files in a Hierarc ](https://www.reddit.com/r/deeplearning/comments/1fh58oz/what_is_the_best_approach_for_parsing_and/) , 2024-10-15-0913
```
I want to implement a Code-RAG system on a code directory where I need to:

* Parse and load all the files from folders 
and subfolders while excluding specific file extensions.
* Embed and store the parsed content into a vector store.
* Ret
rieve relevant information based on user queries.

However, I’m facing two major challenges:

**File Parsing and Loading
:** What’s the most efficient method to parse and load files in a hierarchical manner (reflecting their folder structure
)? Should I use Langchain’s directory loader, or is there a better way? I came across the Tree-sitter tool in Claude-dev
’s repo, which is used to build syntax trees for source files—would this be useful for hierarchical parsing?

**Cross-Fi
le Context Retrieval:** If the relevant context for a user’s query is spread across multiple files located in different 
subfolders, how can I fine-tune my retrieval system to identify the correct context across these files? Would reranking 
resolve this, or is there a better approach?

**Query Translation:** Do I need to use Something like Multi-Query or RAG-
Fusion to achieve better retrieval for hierarchical data?

\[I want to understand how tools like [continue.dev](http://c
ontinue.dev/) and [claude-dev](https://github.com/saoudrizwan/claude-dev) work\]
```
---

     
