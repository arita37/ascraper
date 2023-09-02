 
all -  [ How Code Interpreter Orchestration is Designed? ](https://www.reddit.com/r/ChatGPT/comments/1684itm/how_code_interpreter_orchestration_is_designed/) , 1693666398.0
```
The user experience when interacting with ChatGPT’s code interpreter is impressively seamless. I am wondering how is the
 prompt and orchestration designed to support the features outlined below? Is there a “langchain” agent that can offer c
omparable functionality?

“it is evident that the code interpreter is capable of utilizing external files, executing scr
ipts, planning, creating multiple scripts to address a single query, and incorporating answers directly into the respons
e. Moreover, it has additional functionalities such as debugging/self-correction, the ability to seek modifications or c
larifications post script generation” 
[https://levelup.gitconnected.com/the-magical-chatgpt-code-interpreter-plugin-you
r-personal-programmer-and-data-analyst-f8cd69e8323b](https://levelup.gitconnected.com/the-magical-chatgpt-code-interpret
er-plugin-your-personal-programmer-and-data-analyst-f8cd69e8323b)
```
---

     
 
all -  [ How to deal with missing question mark? ](https://www.reddit.com/r/LangChain/comments/167vauj/how_to_deal_with_missing_question_mark/) , 1693637101.0
```
I've noticed that there is a different answer if you put question mark or not in the question. I have trained a llm that
 behaves very nicely, trained on a company FAQ. But the answers differ if a question mark is present or not, the latter 
being a pain since the reply becomes a generic one and not the one that it should based on the training document.

Train
ed with openAI functions, ver 3.5

Amy way to get pass this? Prompt engineering? How to understand if it's a question or
 not and apply the question mark?

Thanks!
```
---

     
 
all -  [ I have some defined classes and a design system. What is the best approach to build a chat bot that  ](https://www.reddit.com/r/LangChain/comments/167sfdx/i_have_some_defined_classes_and_a_design_system/) , 1693627485.0
```
 How can I create a chatbot that generates HTML components using predefined classes from a design system, and what is th
e best approach to manage this without utilizing a vector store? 
```
---

     
 
all -  [ Conversationalretrievalchains pigeon holes on chat history + history overwhelms context window ](https://www.reddit.com/r/LangChain/comments/167ndda/conversationalretrievalchains_pigeon_holes_on/) , 1693612938.0
```
Hey y’all, I build an app using conversationalretrievalchains (CRCs). But I am having two problems. I have solved both, 
but I am curious if there is a better way to handle them. 

The two problems

* The chat pigeonholes itself once you sta
rt to include chat history. 
* Long chat histories completely overwhelm the context window making it such that the quest
ion isn’t even included in the inference request anymore. 

For completeness, I am using Quadrant and MPT-30B (not that 
I think that matters a lot. I believe all CRCs with chat history will suffer from these issues). 

Let me explain in mor
e detail. 

Problem 1. When you create a CRC with chat memory, you add the conversation history to each request. At firs
t, the chat history is empty, and so the chat works as you expect. But once you add the history to the request, it start
s to include it in the similarity search with the vector store. As a result, the vector store will only return the same 
document repeatedly as it is the best match based on the chat history. But as a result, you can never get out of this pi
geonhole of information. 

My current solution is to include an additional call to the LLM to determine if the question 
is a follow-up question to the previous question. If it answers yes, I’ll include the history if it answers no, I won’t 


This works ok but does introduce quite a bit of latency as I have to do yet another LLM call. If you are familiar with
 the CRC, you know that it already does two calls. One to condense the chat history and one to answer the question. 

No
w for the second problem. If your chat history gets long enough, it will eventually get too long for the context window,
 and as a result, it will cut off the actual question. The resulting answers are random ramblings about the chat history
 that makes no sense and have no relation to the question. I solved this by only including the last five messages. This 
works fine but does introduce long-term memory loss. 

I guess you could get creative and add another inference call or 
similarity search between the question and the chat history to decide which bits to include, but to be honest, I don’t c
are that much about the long-term memory loss. 

Overall, it just feels like nobody actually used langchain to build any
thing but cool local demos on your laptop. There are a lot of issues that start to pop up the moment you build an actual
 chatbot. 

I am debating dropping it entirely and just doing the similarity search myself. After all, all langchain doe
s is wrap some vector store and LLM call in a nice wrapper. 

Anyway, I hope that made sense, and I am curious if people
 have encountered the same problem and what solution they came up with. 
```
---

     
 
all -  [ The talks from SeattleJS Conf 2023 have been posted online (free) ](https://www.reddit.com/r/webdev/comments/167kfyv/the_talks_from_seattlejs_conf_2023_have_been/) , 1693605570.0
```
The talks from [SeattleJS Conf 2023](https://seattlejs.com/conf) have been posted online, for free! 

[https://www.youtu
be.com/playlist?list=PLLiioAbFTbKMJMlJnhkiKy7IfsnsCVAb5](https://www.youtube.com/playlist?list=PLLiioAbFTbKMJMlJnhkiKy7I
fsnsCVAb5)

Talk rundown:

* What to Know About Deno 2.0 by Kevin Whinnery
* Rebuilding in Rust for Good Reason by Eve P
orcello
* 50 shades of React rendering with Next.js by Ben Ilegbodu
* FLIP no more; Viva View Transitions by Adam Argyle

* Creating a Design System using Design Tokens With Amplify by Erik Hanchett
* Move over passwords, passkeys are my new
 best friend! by Daphne Liu
* Understanding LangChain Agents and Tools with Twilio (or with SMS) by Lizzie Siegle
* Buil
ding a Real-Time Multiplayer Reactions Component by John Pham
* Every Process, Everywhere, All at Once by Luis Montes
* 
ES13 and Beyond: The Future of JavaScript by Christina Zhu
* Static Analysis: Don't Fear the Linter! by Josh Goldberg
* 
A Plea for Boring Tech by Jason Lengstorf

&#x200B;
```
---

     
 
all -  [ Langchain in Javascript in a .NET project ](https://www.reddit.com/r/LangChain/comments/167g2mi/langchain_in_javascript_in_a_net_project/) , 1693595383.0
```
Sorry for being an absolute beginner but I have a co-worker that supplied me some JS Langchain code and I am trying to i
ntegrate it into my .NET project. Is this possible?

&#x200B;

I have installed what I believe are the correct Nuget pac
kages but they appear to be targeting the .NET Framework. I also tried running the 'npm install -S langchain' command in
 the package manager console with no luck.

These are the lines I am getting an exception on:

**import { PromptTemplate
 } from 'langchain/prompts';**

**import { LLMChain } from 'langchain/chains';**

**import { OpenAI } from 'langchain/ll
ms/openai';**

&#x200B;

Here is the error:

**Failed to resolve module specifier 'langchain/chains'. Relative reference
s must start with either '/', './', or '../'.**

The install of the packages did not add a Langchain folder into the pro
ject, so I don't know how to reference what it's looking for with a relative path. Any help or knowledge would be apprec
iated. I have been banging my head against a wall for two days.
```
---

     
 
all -  [ Stanford DSPy - Better than LangChain? ](https://www.reddit.com/r/LangChain/comments/167dzcb/stanford_dspy_better_than_langchain/) , 1693590576.0
```
Stanford recently launched [DSPy](https://github.com/stanfordnlp/dspy), a really cool python language model framework th
at includes automatic prompt generation for tasks.   


I'm interested to hear what you guys think about this because it
 sounds like a potential LangChain replacement. It looks like a great alternative to manual prompt engineering, but I do
n't completely understand how they are able to optimize prompts.  


Here's how they compare DSPy to LangChain:  
 

>La
ngChain and LlamaIndex are popular libraries that target high-level application development with LMs. They offer many *b
atteries-included*, pre-built application modules that plug in with your data or configuration. In practice, many usecas
es genuinely *don't need* any special components indeed. If you'd be happy to use someone's generic, off-the-shelf promp
t for question answering over PDFs or standard text-to-SQL as long as it's easy to set up on your data, then you will pr
obably find a very rich ecosystem in these libraries.  
>  
>Unlike these libraries, **DSPy** doesn't internally contain
 hand-crafted prompts that target specific applications you can build. Instead, **DSPy** introduces a very small set of 
much more powerful and general-purpose modules *that can learn to prompt (or finetune) your LM within your pipeline on y
our data*.  
>  
>**DSPy** offers a whole different degree of modularity: when you change your data, make tweaks to your
 program's control flow, or change your target LM, the **DSPy compiler** can map your program into a new set of prompts 
(or finetunes) that are optimized specifically for this pipeline. Because of this, you may find that **DSPy** obtains th
e highest quality for your task, with the least effort, provided you're willing to implement (or extend) your own short 
program.  
>  
>If you're familiar with neural networks:  
>  
>This is like the difference between PyTorch (i.e., repre
senting **DSPy**) and HuggingFace Transformers (i.e., representing the higher-level libraries). If you simply want to us
e off-the-shelf BERT-base-uncased or GPT2-large or apply minimal finetuning to them, HF Transformers makes it very strai
ghtforward. If, however, you're looking to build your own architecture (or extend an existing one significantly), you ha
ve to quickly drop down into something much more modular like PyTorch. Luckily, HF Transformers *is* implemented in back
ends like PyTorch. We are similarly excited about high-level wrapper around **DSPy** for common applications. If this is
 implemented using **DSPy**, your high-level application can also adapt significantly to your data in a way that static 
prompt chains won't. Please [open an issue](https://github.com/stanfordnlp/dspy/issues/new) if this is something you wan
t to help with.

&#x200B;
```
---

     
 
all -  [ I'm trying to stream recorded audio from the browser to my LLM powered backend. ](https://www.reddit.com/r/LangChain/comments/167bjky/im_trying_to_stream_recorded_audio_from_the/) , 1693585042.0
```
I've been stuck on this for a few days. Before I added my client app, I could record audio with Python's sounddevice lib
rary and pass every 1 second of audio to webrtcvad for voice activity detection. 

The VAD requires 16bit PCM audio, whi
ch python can produce no problem. JS by contrast has been more difficult. MediaRecorder is out because it only produces 
compressed audio formats that I can't put through VAD, so I've been building with Web Audio API. My front end is sending
 audio chunks but everything was turning up 'voiced' by my VAD so I took a listen and it's full of very loud static. Cha
tGPT and I put together some code that would grab a small sample of each audio chunk as 16bit PCM, and the full audio ch
unk as 32bit PCM. 

I'm considering using some standard audio format instead of 32pcm, because I don't really need to pr
ocess it in my server other than for VAD, but now that I think of it, my logic for stitching together audio chunks requi
res the audio to be a numpy array.

 I'm not really familiar with Web Audio API, or worklet nodes for that matter, so I'
ve been leaning heavy on ChatGPT for this portion, but it hasn't been able to solve this issue. 

Has anyone else handle
d streams in this way? Is the solution in Web Audio API?
```
---

     
 
all -  [ How do I choose an embeddings model? ](https://www.reddit.com/r/LangChain/comments/1678qrt/how_do_i_choose_an_embeddings_model/) , 1693578651.0
```
Can I use OpenAI embeddings in Chroma with a HuggingFace or GPT4ALL model and vice versa?

Is one type of embedding bett
er than another for similarity search accuracy?

Thanks in advance for you reply!
```
---

     
 
all -  [ Why does MarkdownHeaderTextSplitter remove the headers and put them into the metadata if vector stor ](https://www.reddit.com/r/LangChain/comments/16785z2/why_does_markdownheadertextsplitter_remove_the/) , 1693577302.0
```
I'm a bit confused by why [MarkdownHeaderTextSplitter](https://python.langchain.com/docs/modules/data_connection/documen
t_transformers/text_splitters/markdown_header_metadata) removes the markdown headers and puts them into metadata instead
. If we can only filter on metadata in vector stores and not search on metadata, wouldn't this make the markdown heading
 essentially useless for similarity searching?

Any insight/help would be greatly appreciated. Thanks in advance!
```
---

     
 
all -  [ How to save DocArrayInMemorySearch object ](https://www.reddit.com/r/LangChain/comments/1673lji/how_to_save_docarrayinmemorysearch_object/) , 1693564829.0
```
Does anyone know how I can persist or save the database object created using DocArrayInMemorySearch.from\_documents(text
s, embedding)? I can't find anything in the documentation and it would really help my project to be able to quickly uplo
ad this. If anyone has any leads I'd really appreciate it. I'm working in Colab.
```
---

     
 
all -  [ Combining LLMs with vector DBs ](https://www.reddit.com/r/LangChain/comments/1672tpn/combining_llms_with_vector_dbs/) , 1693562209.0
```
I'm building a product categorizer that takes in the name of a product and assigns a category to it. My categories are s
tored in a FAISS database.

What I want to do is the following:  
Input the name and description for the product, and fe
tch, say the top 5 relevant categories from the DB, and then pass these along with the product information to the LLM to
 choose the most fitting one. I want the categories to be exclusively from this DB.

I tried using the RetrievalQAChain,
 it worked fine, until I introduced a PydanticOutputParser, upon which it started to give me weird results.

Am I doing 
this right?

Also more broadly, does the RetrievalQAChain perform the similarity search against the whole query? I'm not
 sure why introducing the parser would cause the results to change.

Thanks!
```
---

     
 
all -  [ Creating an Embeddings REST API ](https://www.reddit.com/r/LangChain/comments/1672pca/creating_an_embeddings_rest_api/) , 1693561784.0
```
I wish to create a REST API (Django) that allows users to upload documents and then search on them. 

My thought was to 
have two endpoints:

* `/embeddings` \- used to ingest the document, upload embeddings to Pinecone
* `/chat` \- chat wit
h the document

Here is the code I wrote for this (found off a guide):

    @router.post('/embeddings', response=Embeddi
ngsOut)
    def create_embeddings(request, file: UploadedFile = File(...)):
        # set the openai key
        openai.
api_key = settings.OPENAI_KEY
    
        # Save the file to media storage
        fs = FileSystemStorage(location='med
ia/')  # specify the location
        filename = fs.save(file, file)
        file_url = fs.url(filename)
    
        # 
load the file
        loader = PyPDFLoader(f'{BASE_DIR}{file_url}')
        data = loader.load()
    
        # split in
to chunks
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=0)
        texts = text_
splitter.split_documents(data)
    
        # set up the embeddings object
        OPENAI_API_KEY = settings.OPENAI_KEY

        embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
    
        # initialize and upload embeddings to 
Pinecone
        pinecone.init(
            api_key=settings.PINECONE_API_KEY,
            environment=settings.PINECONE
_API_ENV
        )
        index_name = 'index'
        docsearch = Pinecone.from_texts([t.page_content for t in texts],
 embeddings, index_name=index_name)
    
        return {
            'message': 'File uploaded'
        }
    
    
   
 @router.post('/chat', response=AiOut)
    def create_chat(request):    
    
        # ... all the code from the other 
API
    
        llm = OpenAI(temperature=0, openai_api_key=settings.OPENAI_KEY)
        chain = load_qa_chain(llm, chai
n_type='stuff')
    
        query = 'what is this document about?'
        docs = docsearch.similarity_search(query)
  
      response = chain.run(input_documents=docs, question=query)
    
        return {
            'message': str,
     
       'session_id': str
        }

&#x200B;

The `/embeddings` endpoint works great. 

But, the `/chat` endpoint is whe
re I'm struggling. From the code I have, it looks like I'd needed to load the document every time a query is made.

Feel
s like I'm missing something :)

Would appreciate any nudge in the right direction!
```
---

     
 
all -  [ Build an LLM-powered application using LangChain ](https://www.leewayhertz.com/build-llm-powered-apps-with-langchain/) , 1693556088.0
```

```
---

     
 
all -  [ RefineDocumentsChain ](https://www.reddit.com/r/LangChain/comments/1670dl4/refinedocumentschain/) , 1693553418.0
```
hey guys, I can't for the life of me unserstand how to use this for a question insted of summary. i want it to get multi
ple contexts and imporve on the answer it gives.

&#x200B;

any leads?

&#x200B;

thanks!!
```
---

     
 
all -  [ LangChain Library Adds Full Support for Neo4j Vector Index ](https://www.reddit.com/r/Neo4j/comments/166z06j/langchain_library_adds_full_support_for_neo4j/) , 1693548504.0
```
My latest blog post demonstrates how to use the recently added Neo4j Vector index in LangChain Library to both load and 
read data.

&#x200B;

[https://medium.com/neo4j/langchain-library-adds-full-support-for-neo4j-vector-index-fa94b8eab334]
(https://medium.com/neo4j/langchain-library-adds-full-support-for-neo4j-vector-index-fa94b8eab334)
```
---

     
 
all -  [ Would you pay for high-quality vector embeddings? ](https://www.reddit.com/r/LangChain/comments/166yug1/would_you_pay_for_highquality_vector_embeddings/) , 1693547972.0
```
I'm thinking to curate high quality vector embedding 'libraries' and enable developers to call them via an API. This way
 they can embed knowledge from across domains easily into their apps.

Would this be useful to you as a developer?

edit
 1: the vector embedding libraries would be curated textual content by subject-matter-experts on topics like also tradin
g, molecular biology, etc. that developers can't curate on their own.
```
---

     
 
all -  [ What do the GPU-poor use to host models? ](https://www.reddit.com/r/LangChain/comments/166wnjm/what_do_the_gpupoor_use_to_host_models/) , 1693540868.0
```
I have an M2 mac but with no video card. Last I recall, it caps out at the 13b-models, 8-bit versions. So the performanc
e isn't that great (15s responses and not very accurate answers)

I also have access to Google collab, which I've been u
sing for experimentation. However, while I'm storing large models on Google drive, you frequently have to re-install pyt
hon dependencies...which can be just as expensive as re-downloading a large model. 

So what are others using? 

Maybe s
elf-hosting on AWS? Other ideas?
```
---

     
 
all -  [ ICYMI August: Zep Vector DB, User Store, LangChain collabs & more! ](https://www.reddit.com/r/LangChain/comments/166tqw2/icymi_august_zep_vector_db_user_store_langchain/) , 1693532379.0
```
It's been a while since I posted here, but I thought I'd update you on [Zep's](https://docs.getzep.com/) August activiti
es, including several collaborations with LangChain + additional LangChain integrations.

I've read that many of you hav
e started to look beyond LangChain for more advanced functionality and enhanced performance. Zep recently integrated wit
h LlamaIndex and improved our [Python and TypeScript SDKs](https://docs.getzep.com/) to make it easier and faster to bui
ld apps without utilizing frameworks.

DM me if you have any questions or feedback!

&#x200B;

* We shipped the [Zep Vec
tor Store](https://blog.getzep.com/introducing-the-zep-document-vector-store/). 🔎 Zep is now a single, batteries-include
d platform for grounding LLM apps with long-term memory.
* We partnered with LangChain to demonstrate building [three fo
undational LLM apps using TypeScript](https://blog.getzep.com/foundations-of-llm-app-development-langchainjs/) 🧱🛠️ (and 
on the [LangChain blog](https://blog.langchain.dev/zep-x-langsmith-foundations-of-llm-app-development-with-langchain-js-
and-zep/?ref=blog.getzep.com)). The article also offers a great introduction to LangChain's LangSmith observability plat
form.
* We introduced the [Zep User Store](https://blog.getzep.com/introducing-users/). 🧑🏻‍🚀🧔🏿‍♂️👷‍♀️🦸🏽‍♀️ The new User 
object and its associated Sessions provide a powerful way to manage and understand the behavior of individuals using you
r application.
* We released [support for LlamaIndex](https://gpt-index.readthedocs.io/en/latest/examples/vector_stores/
ZepIndexDemo.html?ref=blog.getzep.com) 🦙❤️ and [collaborated with the LlamaIndex team on a post for their blog](https://
twitter.com/jerryjliu0/status/1690018390059225088?ref=blog.getzep.com).
* FlowiseAI [launched support](https://twitter.c
om/FlowiseAI/status/1694372350748172682?ref=blog.getzep.com) for Zep's new Vector Store! And LangChain[ released support
](https://twitter.com/LangChainAI/status/1691868585885626790?ref=blog.getzep.com) for both LangChain Python and LangChai
n.js!
* And finally, we released support for [Anthropic's Claude family](https://blog.getzep.com/announcing-anthropic-ll
m-support/) of LLM models.
```
---

     
 
all -  [ Using LangChain to build a working tic-tac-toe game with GUI without writing a line of code ](https://www.youtube.com/watch?v=_JdmzpXLyE0) , 1693526289.0
```

```
---

     
 
all -  [ I Built an All-In-One Discord Bot for OpenAI's GPT 3.5 Turbo ](https://www.reddit.com/r/OpenAI/comments/166qrg9/i_built_an_allinone_discord_bot_for_openais_gpt/) , 1693524723.0
```
This project has been on going for most of the year, I just released the bot as public recently. It is 4,500 lines of py
thon code that utilizes python modules like LLM Predictor, SimpleGPTVectorIndex, OpenChatAI, Langchain, etc. 

The bot o
perates on a secure Google Cloud compute instance. The bot is also built with robust class management, threading, and th
read locking, along with complete isolation of users sessions or files. It also has three tiers of file validation, key 
validation, and a data sanitization process that makes it possible for users to upload data not properly prepared for in
dexing or tabulation.

The bot has three primary functions - learn, chat, and image. In learn mode it can receive, in di
rect message, filetypes: .doc, .docx, .pdf, .odt, .rtf, .txt, and can also fetch data from web links. In chat mode, user
s in Discord can chat with their GPT model with on the fly options like setting the temperature, token limit, amount of 
context to fetch from previous messages, set user roles, and using prompts. In image mode, the bot uses DALL E 2 with ge
neration, regeneration, and variation modules. 

Session authors can give users roles in the chat mode, with options: sy
stem, user (function is in the works). When a user has a role, they can set a prompt for themselves. Only session author
s can give roles, and individuals can only set prompts for themselves. Session authors can also remove a users role. 

I
've also built in utilities, in the learning mode, for generating conversation logs from the interaction, including upvo
te messages, downvote messages, and bookmarking messages. Note, in the screenshot below, these are done by react and can
 only be done by the session author. On session exit, if the session author chooses, the log files are sent to them in d
irect message before being discarded from the actual cloud server. 

Easily, entire groups of people can collaboratively
 work with ChatGPT using custom data, and the session author can set roles for system and user.  Roles are applied (assi
stant, system, user) and function is in the works.

Due to the nature of file and key exchange risks, the bot only handl
es file or keys in direct messages with user. This reduces risk of key exposure or copyright issues in a Discord server 
setting. Users who supply keys, save keys, upload files, or receive log files, all these actions take place in direct me
ssage with the bot. 

Saving keys is completely optional, and the bot will only display partial keys - just like OpenAI 
does, if a user is managing their saved keys. Key files are also automatically deleted from the cloud server if not used
 within 5 days.

The bot only retains user data long enough to index and embed it into the session, then the files are p
romptly discarded. When a user exits a session, any remaining files and the session directory are also discarded. 

The 
bot treats each server instance, each user instance, and each session instance as isolated objects and events. This is n
ot only necessary to keep users experiences and data truly separate, but also to mitigate multi and concurrent processin
g issues. 

The primary goal of this build was to compile many other smaller builds that I, and a community of others, u
sed to work together and build an esoteric variation of ChatGPT. This bot is beta, just made public after months of test
ing. 

Currently, there are a few limitations - limited time, limited data upload sizes, and 1 session per user, 1 sessi
on per channel.

There is even more to this bot, but I am not sure I should overwhelm this post with all of the details.
 

To try the bot, invite the bot, see the terms, see the privacy statements or further info on its usage and options, v
isit the bot's home server EtherCereal: [https://top.gg/servers/907301373387898950](https://top.gg/servers/9073013733878
98950)

The Developer (me): [https://www.linkedin.com/in/nicholas-dustin-065560108/](https://www.linkedin.com/in/nichola
s-dustin-065560108/)

\*an example after uploading a .docx book, sent to me to use by the book's author\*

https://previ
ew.redd.it/d5pxg8vm4jlb1.png?width=1253&format=png&auto=webp&s=f79bd558c753b2dad2878be2f1e2dd8d35609ff1

&#x200B;
```
---

     
 
all -  [ Output parser for openai chat models ](https://www.reddit.com/r/LangChain/comments/166jxzi/output_parser_for_openai_chat_models/) , 1693508882.0
```
I can’t seem to get this output parser from langchain to work for the chatopenai models: 

https://python.langchain.com/
docs/modules/model_io/output_parsers/pydantic

It works when I just use openai but not the chatopenai. Let me know if an
yone has any ideas or examples. I’m trying to output json object that has two list items.
```
---

     
 
all -  [ Have any LLMs been optimized or fine tuned to be effective langchain agents? ](https://www.reddit.com/r/LangChain/comments/166hoq8/have_any_llms_been_optimized_or_fine_tuned_to_be/) , 1693503776.0
```
Now that GPT 3.5 has fine tuning, and 4 is supposedly soon to follow, has anybody made datasets to make the best possibl
e agent?

Same question for open source LLMs.

&#x200B;

I've seen this dataset which looks great [https://huggingface.c
o/datasets/jamescalam/agent-conversations-retrieval-tool](https://huggingface.co/datasets/jamescalam/agent-conversations
-retrieval-tool) but I'm not sure what the license on it is. Also definitely curious to hear about any others.
```
---

     
 
all -  [ 🤖 Agenta: Open-Source Platform for LLM Prompt Engineering, Evaluation, and Deployment ](https://www.reddit.com/r/opensource/comments/166gb8a/agenta_opensource_platform_for_llm_prompt/) , 1693500536.0
```
👋 Hey everyone,

🛠️ If you're building with LLMs, you'll want to take a look at agenta. We've open-sourced this platform
 to turbocharge your LLM app development. Here’s what’s in it for you:

- 📝 **Prompt Engineering**: Experiment with diff
erent prompts, models, embeddings, and RAG strategies.
- 🔄 **Versioning & Evaluation**: Track and test changes in your L
LM app
- 🚀 **One-Click Deployment**: Get an API live with just one click.
- 💻 **Integrate with Your Code**: Integrate ag
enta with your existing code base, whether written with langchain, llama_index or any other framework/library

👥 Agenta 
makes it easier for both product people and developers to collaborate. You can create apps using both UI and from code.


🎥 **Youtube Demo (2mn)**: [Watch it out here](https://youtu.be/XTlEvcvXjLk?si=Yipxt4TSn6lqTEU5)

▶️ **Live Demo**: [Che
ck it out here](https://demo.agenta.ai/)

⭐ **Support Us**: If you find this useful, please star us on GitHub: [Agenta o
n GitHub](https://github.com/agenta-ai/agenta)

👩‍💻 **Get Involved**: We're looking for contributors and have a range of
 open issues. Join our community on Slack: [Agenta Slack Channel](https://join.slack.com/t/agenta-hq/shared_invite/zt-1z
safop5i-Y7~ZySbhRZvKVPV5DO_7IA)
```
---

     
 
all -  [ 🤖 Agenta: Open-Source Platform for LLM Prompt Engineering, Evaluation, and Deployment ](https://www.reddit.com/r/PromptEngineering/comments/166fxyq/agenta_opensource_platform_for_llm_prompt/) , 1693499644.0
```
👋 Hey everyone,

🛠️ If you're building with LLMs, you'll want to take a look at agenta ([2min demo](https://youtu.be/XTl
EvcvXjLk?si=Yipxt4TSn6lqTEU5)). We've open-sourced this platform to turbocharge LLM app development. Here’s what’s in it
 for you:

- 📝 **Prompt Engineering**: Experiment with different prompts, models, embeddings, and RAG strategies.
- 🔄 **
Versioning & Evaluation**: Track and test changes in your LLM app
- 🚀 **One-Click Deployment**: Get an API live with jus
t one click.
- 💻 **Integrate with Your Code**: Integrate agenta with your existing code base, whether written with langc
hain, llama_index or any other framework/library

👥 Agenta makes it easier for both product people and developers to col
laborate. You can create apps using both UI and from code.

🎥 **Youtube Demo (2mn)**: [Watch it out here](https://youtu.
be/XTlEvcvXjLk?si=Yipxt4TSn6lqTEU5)

▶️ **Live Demo**: [Check it out here](https://demo.agenta.ai/)

⭐ **Support Us**: I
f you find this useful, please star us on GitHub: [Agenta on GitHub](https://github.com/agenta-ai/agenta)

👩‍💻 **Get Inv
olved**: We're looking for contributors and have a range of open issues. Join our community on Slack: [Agenta Slack Chan
nel](https://join.slack.com/t/agenta-hq/shared_invite/zt-1zsafop5i-Y7~ZySbhRZvKVPV5DO_7IA)
```
---

     
 
all -  [ langchain generating similar questions with question_generator parameter ](https://www.reddit.com/r/LangChain/comments/166fc4g/langchain_generating_similar_questions_with/) , 1693498207.0
```
Hello,

I am utilizing LangChain as a query documentation tool for a collection of policies contained within a specific 
directory. During my interactions with the Weaviate vector store, I've encountered instances where I need to fine-tune m
y queries in order to obtain meaningful responses. Therefore, I've decided to create a list of 'similar questions' that 
is displayed when the model gives no response, providing the user the option to choose from 5 similar questions that are
 likely to generate an accurate response. I've come across the 'question\_generator' parameter within the Conversational
RetrievalChain class, and I'm seeking clarification on its functionality. I'm aware it takes in the current question and
 chat history, however, I'm interested in understanding whether the 'question\_generator' parameter can be employed to s
can the entire vector store and generate questions that are apt to yield informative responses.

Thanks.
```
---

     
 
all -  [ What are the best tutorials/resources for building agents with LangChain? ](/r/AI_Agents/comments/166aqlm/what_are_the_best_tutorialsresources_for_building/) , 1693493043.0
```

```
---

     
 
all -  [ I've been exploring the best way to summarize documents with LLMs. LangChain's MapReduce is good, bu ](/r/LangChain/comments/165xmzx/ive_been_exploring_the_best_way_to_summarize/) , 1693490258.0
```

```
---

     
 
all -  [ What are the best tutorials/resources for building agents with LangChain? ](https://www.reddit.com/r/AI_Agents/comments/166aqlm/what_are_the_best_tutorialsresources_for_building/) , 1693487358.0
```
I am new to coding and I only made a very simple agent for text completion so far. Now I want to try out Langchain, sinc
e everyone is talking about it.

But I need external resources, videos, tutorials to help. Do you have experience with a
gents in Langchain? How easy do you find it, and can you recommend learning sources?

Thanks!
```
---

     
 
all -  [ What SDKs, tools, and frameworks are you using for building AI agents? ](https://www.reddit.com/r/AI_Agents/comments/166a16e/what_sdks_tools_and_frameworks_are_you_using_for/) , 1693485510.0
```
I still dont see a clear consensus about what tools work best for agents debugging, monitoring, deployment etc. Of cours
e there are popular frameworks for building agents, such as Langchain, but I am looking also for more techstack-agnostic
 software, for people who build agents without a pre-defined framework.
```
---

     
 
all -  [ I'm testing openAI function calling and I'm not really getting what I wanted. Is there any alternati ](https://www.reddit.com/r/LangChain/comments/1669ica/im_testing_openai_function_calling_and_im_not/) , 1693484063.0
```
I'm basically trying to extract relevant info from chunks of text but it is very inconsistent. I know it's not determini
stic, but still I expected to perform better and do what has been told at least 50% of the times.

I wonder if there are
 other models with similar functionality through API.
```
---

     
 
all -  [ General guidance on my project please. ](https://www.reddit.com/r/LocalLLaMA/comments/16674h6/general_guidance_on_my_project_please/) , 1693476901.0
```
Could someone please help with fleshing out the steps that I need to take to get my project underway?

Here is the info:
 I have a rented ubuntu server(ryzen 5900x, 64gb ram) that I can access remotely. No graphics card and no graphical inte
rface on the server. I want to run a uncensored LLM on this rig. I tried downloading koboldcpp+some llama model, but kob
old has a graphical interface and it was suuper slow through X11 and xming server. 

1. How would i run an llm on ubuntu
 with only command line. 
2. How would I give it a persistent character?
3. Is Langchain what i need?
4. Do i need to se
t up a code interpreter on the server to run it all? 

I think I just need 'big picture' steps to understand how it all 
sits together. Thanks.
```
---

     
 
all -  [ Building a Q&A system Using LangChain with FalkorDB ](https://www.falkordb.com/blog/building-a-qa-system-using-kg) , 1693475933.0
```

```
---

     
 
all -  [ Make langchain recognize a pydantic subclass ](https://www.reddit.com/r/LangChain/comments/16661mt/make_langchain_recognize_a_pydantic_subclass/) , 1693473292.0
```
I use the OpenAIMultiFunctions Agent to let the user create groups by text.

For example:

>'Create a group in Berlin wi
th Kate and John'

There are 2 tools, **one for the creation of the group** the other will call the API with the name an
d **return the contact data of the user**.

I have 2 classes  
**Guest**

    class Guest(BaseModel):
     '''Informatio
n about a group Guest of a group'''
 id: int = Field(..., description='The id of the user')
 first_name: str = Field(...
, description='The first name of the user')
 last_name: str = Field(description='The last name of the user')
 code: str 
= Field(description='The phone code of the user')
 phoneNumber: str = Field(description='The phone number of the user')


 **Group**

    class Group(BaseModel):
 '''Information about a group'''
 title: str = Field(..., description='The titl
e of the cast')
 description: str = Field(..., description='The description of the cast')
 location: str = Field(descrip
tion='The location of the cast')
 guestList: Optional[List[Guest]] = Field(description='The list of guests of the cast')


In general everything is working, the agent first gets the contact from the api but then creates the group with empty 
guest or with wrong data like \[{'name': 'Kate', 'phone': '1234567890'}\].  


I also tried to use the ReAct agent, but 
there its the same, the format of the pydantic does not take the subclass of guest.

Someone has an idea about that?  



&#x200B;
```
---

     
 
all -  [ LangChain Summary with Gitlab AI Bot ](https://www.reddit.com/r/LangChain/comments/1661ds4/langchain_summary_with_gitlab_ai_bot/) , 1693457431.0
```
#### Generates a summary for GitLab merge requests by OpenAI.

&#x200B;

https://preview.redd.it/cb4j9xnamdlb1.png?width
=1730&format=png&auto=webp&s=262b9397b42a977c4db7345e64525f8c56169ecd

Check out the repository and give it some love! [
https://github.com/coolbeevip/gitlab-bot](https://github.com/coolbeevip/gitlab-bot)
```
---

     
 
all -  [ I've been exploring the best way to summarize documents with LLMs. LangChain's MapReduce is good, bu ](https://www.reddit.com/r/LangChain/comments/165xmzx/ive_been_exploring_the_best_way_to_summarize/) , 1693446783.0
```
Obviously, short documents are easy – just pass in the entire contents of the document into an LLM and out comes a nicel
y assembled summary. But what do you do when the document is longer than even the most generous LLMs? I ran into this pr
oblem while building my new mini-app, [**summarize.wtf**](https://summarize.wtf/)

Langchain offers [Map Reduce](https:/
/python.langchain.com/docs/modules/chains/document/map_reduce), which basically breaks down the document into shorter pi
eces and summarizes each one recursively to patch together a final summary that fits within a specified token limit. Alt
hough Map Reduce does generate a fairly inclusive summary, it is **extremely** expensive, and the cost and processing ti
me associated with it grows super-linearly with the length of the document. Also, it may potentially emphasize less impo
rtant topics while underemphasizing more salient topics in the document due to its equal application of summarization ac
ross the entire document.

So this led me to explore other techniques. I wrote a [pretty detailed article on this topic 
of document summarization with AI](https://pashpashpash.substack.com/p/tackling-the-challenge-of-document), but the TL;D
R is that breaking down a document into key topics with the help of **K-Means vector clustering** is by far the most eff
ective and cost-efficient way to do this. In a nutshell, you chunk the document and vectorize each chunk.

Chunks talkin
g about similar things/topics will fall into distinct 'meaning clusters', and you can sample either the center-point or 
collection of points within each cluster to gather '**representative chunks**' for each distinct meaning cluster a.k.a. 
average meaning of each topic. Then you can stuff these representative chunks into a long context window and generate a 
detailed, comprehensive summary that touches the most important and distinct topics the document covers. I wrote more de
tails on this approach and how it works in my Substack article here: [https://pashpashpash.substack.com/p/tackling-the-c
hallenge-of-document](https://pashpashpash.substack.com/p/tackling-the-challenge-of-document)

Basically, the key is to 
strike a balance between comprehensiveness, accuracy, cost, and computational efficiency. I found that Vector clustering
 combined with this K-means clustering approach offers this balance, making it the go-to choice for [**summarize.wtf**](
https://summarize.wtf/).

What do you guys think about this? Have you found other ways to accomplish this? I'd love to g
et your input and potentially brainstorm other ways of doing this.
```
---

     
 
all -  [ Error when using Weaviate.add_documents() ](https://www.reddit.com/r/LangChain/comments/165x6mt/error_when_using_weaviateadd_documents/) , 1693445591.0
```
So the thing is, whenever I am trying to add a new document to my vector database it prompts the following error:

`'tup
le' object has no attribute 'page_content'`

and the following are the pieces of code that I am running:

    if file.fi
lename.lower().endswith('.pdf'):                         
    pdf = ep.PDFLoad(file_path)  # this is the loader from lan
gchain                         
    doc = pdf.load()                         
    archivo = crear_archivo(doc, file)

In
side the function crear\_archivo I am splitting the document and then adding it to the `Weaviate.add_documents()` functi
on:

     cliente = db.NewVect()  # This one creates the weaviate.client
     text_splitter = CharacterTextSplitter(chun
k_size=1000, chunk_overlap=0)
     docs = text_splitter.split_documents(document)
    
     embeddings = OpenAIEmbedding
s()
     return Weaviate.add_documents(docs, embeddings, client=client, 
     weaviate_url=EnvVect.Host, by_text=False, 
index_name='LangChain') 
    # using this instead of from_documents since I don't want to initialize a new vectorstore
 
   # Some more logic to save the doc to another non-vectorial database

&#x200B;

Whenever I try to run the code it brea
ks during the `Weaviate.add_documents()` function prompting the following error:

`'tuple' object has no attribute 'page
_content'`. I tried to check the type of `docs`, but that doesn't seem wrong since it returns a `List[Document]` which i
s the same type the function accepts.

I also kind of followed this approach:

[https://github.com/langchain-ai/chat-lan
gchain/blob/master/ingest.py](https://github.com/langchain-ai/chat-langchain/blob/master/ingest.py)

which is where I go
t the idea of using add\_documents, since from\_documents is not intended for the thing I'm trying to do.
```
---

     
 
all -  [ Langchain agent returns the name of the tool in the final response ](https://www.reddit.com/r/LangChain/comments/165t8bt/langchain_agent_returns_the_name_of_the_tool_in/) , 1693435442.0
```
Hey all

I am using langchain to create a chatbot, using multiple tools which query different databases to give me the f
inal answer.

Everything works fine, but the problem is that the agent returns the name of the tool in the final answer.


So if I have two tools SQLtool and Texttool, then the answer might be:

'According to SQLtool ....'.

I have mentioned
 in the prompt which goes to the LLM not to mention the name of the tool, but it still mentions it.

Any leads?

Followi
ng are the classes I use:

* from langchain import SQLDatabase, SQLDatabaseChain
* from langchain.prompts.prompt import 
PromptTemplate
* from langchain.chat_models import ChatOpenAI
* from langchain.memory import ConversationBufferWindowMem
ory
* from langchain.chains import ConversationChain, LLMChain
* from langchain.embeddings import OpenAIEmbeddings
* fro
m langchain.chains import RetrievalQAWithSourcesChain
* from langchain.vectorstores import Pinecone
* from langchain.age
nts import Agent, Tool, AgentType, AgentOutputParser, AgentExecutor, initialize_agent
* from langchain.agents.conversati
onal.output_parser import ConvoOutputParser
* from langchain.agents.conversational.prompt import SUFFIX
```
---

     
 
all -  [ New release and new demo for GPT-Synthesizer, an open source tool using LangChain for software desig ](/r/LangChain/comments/165sxqz/new_release_and_new_demo_for_gptsynthesizer_an/) , 1693435117.0
```

```
---

     
 
all -  [ New release and new demo for GPT-Synthesizer, an open source tool using LangChain for software desig ](https://www.reddit.com/r/LangChain/comments/165sxqz/new_release_and_new_demo_for_gptsynthesizer_an/) , 1693434734.0
```
The open source repo: [https://github.com/RoboCoachTechnologies/GPT-Synthesizer](https://github.com/RoboCoachTechnologie
s/GPT-Synthesizer)

The new demo (tic-tac-toe game with GUI): [https://www.youtube.com/watch?v=\_JdmzpXLyE0&list=PLN8Hz7
F2GjIksKtU1gdRIxrCbccpVE4Jy](https://www.youtube.com/watch?v=_JdmzpXLyE0&list=PLN8Hz7F2GjIksKtU1gdRIxrCbccpVE4Jy)

Watch
 to the end of the demo video. You can see that the tic-tac-toe game, that is completely auto-generated by GPT-Synthesiz
er, works without any user's modification. 
```
---

     
 
all -  [ Input wanted on measuring and improving the performance of a RAG system ](https://www.reddit.com/r/OpenAI/comments/165k5mq/input_wanted_on_measuring_and_improving_the/) , 1693414587.0
```
Hi all. I’m looking input on how to measure and improve the performance of a RAG/
Q&A with document retrieval system (ht
tps://python.langchain.com/docs/use_cases/question_answering/).

I work for a company that makes software and I’ve imple
mented this RAG system over our customer-facing product documentation. It’s currently in proof of concept phase (proving
 that RAG-based access is more useful than traditional search engines).

Other than tweaking the prompt that generates t
he answer based on the question and retrieved texts, I'm kind of stuck now in terms of measuring improving the performan
ce of this system. I'm hoping that I can get some pointers from this community.

I know my way around software, but good
 to note that I have not spent the majority of my career as a software engineer. I've taught mysf programming in my past
, and I've been dabbling since (I have a medium-sized Rails application in production). 

Any input is appreciated.
```
---

     
 
all -  [ Should I move to Python? ](https://www.reddit.com/r/rprogramming/comments/165ij20/should_i_move_to_python/) , 1693410887.0
```
I love R. I have used R for statistics, used RQDA to analyze text, learnt some ML on R and so many other things. But, no
w it seems I might need to change. RQDA is deprecated. I am not sure if there are tools in R to configure AI tools - and
 videos suggest installing python tools in R for them (eg Langchain). Is it time to move?
```
---

     
 
all -  [ (Good Discussion) Is there anything LangChain can do better than using LLMs directly (either through ](/r/MachineLearning/comments/165airj/d_is_there_anything_langchain_can_do_better_than/) , 1693408637.0
```

```
---

     
 
all -  [ Looking for best practices when it comes to retrieval for summarization ](https://www.reddit.com/r/LangChain/comments/165cclv/looking_for_best_practices_when_it_comes_to/) , 1693395760.0
```
I have pdf's of various structures from which I want to summarize different types of factors. There is no unified struct
ure and it will keep changing. What is the best I can do in terms of chunking and retrieval for these documents? There s
eems to be essential parts missing from the reterieval. 

I've tried using small chunks with 500 tokens each and feeding
 it to chatgpt app for retrieval but the results are disappointing.

I've seen a few approaches but can't find the refer
ence anymore where people would feed chunks to the retriever in a sequential manner. Then there seem to be prompt engine
ering approaches where we give examples of what should be retrieved from an example. Should I use one Example per Factor
 I want to retrieve ajd structure the prompt in a way that communicates to chatgpt the structure I want to get out?

Exa
mple:{}
Result:{}
Chunk:{}

Etc?

Same for the summarization task with regards to peompt engineering?
```
---

     
 
all -  [ How to use Langchain Agents with DocumentLoader? Is it even possible? ](https://www.reddit.com/r/LangChain/comments/165av9y/how_to_use_langchain_agents_with_documentloader/) , 1693391109.0
```
I'm currently working on a DynamicTool project and I would like to use Langchain Agents with DocumentLoader to load web 
pages. I have already familiarized myself with the PuppeteerLoader, which is documented here ([**https://js.langchain.co
m/docs/modules/data\_connection/document\_loaders/integrations/web\_loaders/web\_puppeteer/**](https://js.langchain.com/
docs/modules/data_connection/document_loaders/integrations/web_loaders/web_puppeteer/)).

However, I'm not sure how to c
ombine Langchain Agents and DocumentLoader. Does anyone have experience with this or can provide any guidance? Is there 
a way to integrate these two tools?

I would greatly appreciate your help and any tips you can provide!
```
---

     
 
all -  [ Is GPT able to categorize large amount of documents according to their description? ](https://www.reddit.com/r/LangChain/comments/165ajpm/is_gpt_able_to_categorize_large_amount_of/) , 1693390010.0
```
I'm looking for the right way to categorize (by topic or sentiment) a list of documents (\~1000). Each document is struc
tured (JSON response); one of the field is the description which contains a free text that could indicate the category.


Would you advice to run a qa on each document or to first embed them and save in Vector DB?
```
---

     
 
MachineLearning -  [ [D] Is there anything LangChain can do better than using LLMs directly (either through a website or  ](https://www.reddit.com/r/MachineLearning/comments/165airj/d_is_there_anything_langchain_can_do_better_than/) , 1693389926.0
```
I haven't used ChatGPT a lot or any other LLMs, I've been reading about  Langchain and its use cases, and I'm having tro
uble wrapping my head  around exactly what it does. From what I understand, its an alternative  interface for LLMs, allo
wing for easy switching between them, and makes  some work for specific use cases easier. If I wanted to write an app or
  script to interact with LLMs and do other tasks, how would LangChain be  better than just making API call(s) to an LLM
, getting back the result  as a string, and doing whatever with it?
```
---

     
 
MachineLearning -  [ Apache Airflow vs. LangChain and LlamaHub for LLM data pipeline [D] ](https://www.reddit.com/r/MachineLearning/comments/160lexg/apache_airflow_vs_langchain_and_llamahub_for_llm/) , 1692928014.0
```
I’m looking for recommendations, suggestions, and/or good documentation that outlines which data pipeline would be best 
to ingest my private data (which will then be split into chunks/nodes for vector embeddings and so forth). Thank you in 
advance!
```
---

     
 
MachineLearning -  [ [P] LLM Apps Are Mostly Data Pipelines ](https://www.reddit.com/r/MachineLearning/comments/15z0muk/p_llm_apps_are_mostly_data_pipelines/) , 1692788725.0
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

     
 
MachineLearning -  [ [P] pgml-chat: A command-line tool for deploying low-latency knowledge-based chatbots ](https://www.reddit.com/r/MachineLearning/comments/15t5nzl/p_pgmlchat_a_commandline_tool_for_deploying/) , 1692228120.0
```
We've created an open source chat bot builder, on top of PostgresML. This tool makes it easy to ingest documents and set
 a system prompt for a chatbot with knowledge of your content. The innovation is in the simplicity and efficiency, rathe
r than the functionality.

PostgresML runs open source embedding models alongside pgvector in Postgres to implement chat
 bot prompt creation without any network calls, which makes it \~4x faster than competing architectures. It can also do 
text generation with that prompt (and no additional network hops) using any open source model from HuggingFace, but it a
lso integrates with the GPT-4 API if you'd like to use that instead. 

The full writeup including some benchmarks for co
mpeting architectures is here:  [https://postgresml.org/blog/pgml-chat-a-command-line-tool-for-deploying-low-latency-kno
wledge-based-chatbots-part-I](https://postgresml.org/blog/pgml-chat-a-command-line-tool-for-deploying-low-latency-knowle
dge-based-chatbots-part-I)

You can chat with a deployment that has access to our blogs and documentation content it in 
\[our Discord\]([https://discord.com/channels/1013868243036930099/1013868243536072868](https://discord.com/channels/1013
868243036930099/1013868243536072868)), where it answers questions addressed to @PgBot.

&#x200B;

* The source code for 
the bot builder and server is only a few hundred lines of Python [https://github.com/postgresml/postgresml/tree/master/p
gml-apps/pgml-chat#readme](https://github.com/postgresml/postgresml/tree/master/pgml-apps/pgml-chat#readme)
* The chat a
pp is so small, because it's delegates all the vector db and embedding generation options to our Python client SDK, whic
h is available for anyone to build other apps with: [https://pypi.org/project/pgml/](https://pypi.org/project/pgml/)
* T
he Python client SDK is so small, because it's just a wrapper around the Rust client SDK: [https://github.com/postgresml
/postgresml/tree/master/pgml-sdks/rust/pgml](https://github.com/postgresml/postgresml/tree/master/pgml-sdks/rust/pgml). 
Currently we also support JS/Typescript SDKs as well, all generated from the same safe and efficient underlying Rust imp
lementation, using some fancy Rust macros.
* The Rust client SDK is also pretty simple though, because it just delegates
 everything to the Postgres database extension, which is where everything is computed in a single GPU accelerated proces
s, without having to load any ML models, data, or dependencies on client apps, effectively eliminating all the typical M
L data<->model network hops. Which makes it faster, simpler and safer.

This lays out what we think a is a better approa
ch to AI application architecture compared to libraries like LangChain or LlamaIndex, that focus on glueing together dis
parate data stores, algorithms, models over the network.  

```
---

     
 
MachineLearning -  [ [P] My apprehension about LangChain and why you don’t need LangChain for building a RAG bot. ](https://www.reddit.com/r/MachineLearning/comments/15ry3z4/p_my_apprehension_about_langchain_and_why_you/) , 1692118520.0
```
A lot of you might be giving me a mouthful just by reading the title of this blog. But to each their own, and probably y
ou might be just riding the hype train. Initially, I was quite fascinated by the work being done on LangChain and using 
it. And so I thought I would give it a try, but when I was installing it, I saw it downloading loads and loads of other 
libraries and most of which were not useful for what I was trying to build.

Checkout the entire blog post at [https://t
hevatsalsaglani.medium.com/why-you-dont-need-langchain-for-building-a-rag-bot-a1dfbc74b64f](https://thevatsalsaglani.med
ium.com/why-you-dont-need-langchain-for-building-a-rag-bot-a1dfbc74b64f)
```
---

     
 
MachineLearning -  [ [D] Approach to creating an 'AI tutor' chatbot for a fantasy language? ](https://www.reddit.com/r/MachineLearning/comments/15o4jy9/d_approach_to_creating_an_ai_tutor_chatbot_for_a/) , 1691747830.0
```
What are the possible practical approaches to creating an 'AI tutor' for a custom fantasy language, i.e. a language whic
h is definitely not covered in any large, mainstream LLM?

Assume in the fantasy language (like Game of Throne's Dothrak
i, but completely custom, so it's guaranteed not to be covered at all by an existing LLM), we have a dictionary of terms
, and a simple description of a grammar. What can I do with that?

Initially I was thinking of using 'Retrieval-Augmente
d Generation' (RAG), where I would pass it my dictionary of terms and their definitions and the grammar doc (i.e. the so
urce documents), and using OpenAI's LLM and LangChain's API wrapper and Pinecone long-term memory vector database, store
 the dictionary/grammar in Pinecone's vector database. Then a query comes in to translate an English word to a fantasy w
ord, and it looks in the Pinecone DB for similar English words, then passes the results with the fantasy word to the LLM
, along with the query, and generates a nice English response, with the fantasy word somewhere in there.

But that doesn
't seem like it would work the more I think about it. Then if I want to add the ability for it to translate English to t
he fantasy language, that seems impossible without first having a huge corpus of translation material (which is complete
ly impractical for a fantasy language). So can an existing generic LLM take a grammar as input, and learn to speak a fan
tasy language? If so, how would you make that happen?

Or what are other approaches to accomplishing this sort of thing?

```
---

     
 
MachineLearning -  [ LLMs Challenges and Approaches Panel [N] ](https://www.reddit.com/r/MachineLearning/comments/15noqwr/llms_challenges_and_approaches_panel_n/) , 1691702326.0
```
&#x200B;

https://preview.redd.it/wl1gtcngnchb1.jpg?width=1500&format=pjpg&auto=webp&s=24e35d852603c6139fd67f79457ec593f
bad99f7

If you're someone who's curious about or working with LLMs there's a cool panel discussion coming up: 

* Compa
ring the pros and cons of using existing LLMs, prompt engineering, and fine-tuning on custom datasets for different ente
rprise use cases.
* Fine-Tuning LLMs: Exploring the advantages and challenges of fine-tuning LLMs on custom datasets to 
align with specific business objectives.
* Tools and platforms: Discussing the various tools and platforms to facilitate
 LLM implementation 
* Overcoming Challenges: Addressing the challenges associated with adopting LLMs, including data pr
ivacy, creating high quality datasets, computational resources, ethical considerations, and the need for specialized exp
ertise.
* Future Directions: Exploring emerging trends, advancements, and potential future applications of LLMs in the e
nterprise context.

Here's the event info: [https://www.eventbrite.com/e/large-language-models-for-enterprise-success-ch
allenges-and-approaches-tickets-695089811337?aff=oddtdtcreator](https://www.eventbrite.com/e/large-language-models-for-e
nterprise-success-challenges-and-approaches-tickets-695089811337?aff=oddtdtcreator)
```
---

     
 
MachineLearning -  [ [D] training a model for function calls ](https://www.reddit.com/r/MachineLearning/comments/15n1j52/d_training_a_model_for_function_calls/) , 1691640324.0
```
would it be possible to train or fine-tune a small (1-3B) model who's sole purpose is to perform function calls? similar
 to how we have tiny models like replit-v2-3B that are super capable at specific things like code auto-complete .  


i 
know that's how openAI implemented function call was by fine-tuning gpt-3.5/4 but I'm thinking just a straight up base m
odel trained to understand and excel at function calls (similar to Gorilla for apis)

i'm thinking it would be a perfect
 'glue' for bigger LLM apps-- avoiding the need for external tools like langchain/quidance/etc...
```
---

     
 
MachineLearning -  [ [D]Embedding model and vector store on LangChain ](https://www.reddit.com/r/MachineLearning/comments/15lllm0/dembedding_model_and_vector_store_on_langchain/) , 1691508979.0
```
For Langchain users, what are the best text embedding models and vector stores (with similarity search) among the many i
ntegrations for connecting a AI model to text data? 

And does performance vary drastically from one model/database to a
nother? 
```
---

     
 
MachineLearning -  [ [P] Rust meets Llama2: OpenAI compatible API written in Rust ](https://www.reddit.com/r/MachineLearning/comments/15k254o/p_rust_meets_llama2_openai_compatible_api_written/) , 1691359615.0
```
Hello,

I have been working on an OpenAI-compatible API for serving LLAMA-2 models written entirely in Rust. It supports
 offloading computation to  Nvidia GPU and Metal acceleration for GGML models !

Here is the project  link: [Cria- Local
 LLAMA2 API](https://github.com/AmineDiro/cria)

You can use it as an OpenAI replacement (check out the included \`Langc
hain\` example in the project).

This is an ongoing project, I have implemented the \`embeddings\` and \`completions\` r
outes. The \`chat-completion\` route will be here very soon!

Really interested in your feedback and I would welcome any
 help :) !

&#x200B;

&#x200B;
```
---

     
 
MachineLearning -  [ [D] Document-based QnA without OpenAI? ](https://www.reddit.com/r/MachineLearning/comments/15imv19/d_documentbased_qna_without_openai/) , 1691212978.0
```
I am working on a project that is very popular with the inception of Langchain + GPT applications. However, I want to ma
ke it open source and hence don't want to use GPT. So something like Langchain + LLama2, etc. I know currently Langchain
 only supports GPT but any other ideas are highly appreciated!
```
---

     
 
MachineLearning -  [ [D] Roadmap for AI engineer (implementation of language models on premise) ](https://www.reddit.com/r/MachineLearning/comments/15gzsfv/d_roadmap_for_ai_engineer_implementation_of/) , 1691056710.0
```
 I worked for less than a year as a Data Engineer. I decided to look for other challenges and got a job as an AI enginee
r developing language models.

The product of the company that hired me is related to data and metadata management. My t
asks will be to introduce features to the product, including a chat function that will allow for asking questions about 
data. Other tasks will include research and proposing additional AI-related functionalities to the product (on premise).
 I have a two weeks left to start work and I need to prepare a bit. My job will involve implementing ready-made solution
s and conducting research (high level - I need to implement valuable features and no one cares how).

**What are the mos
t important things I should learn before starting work?**

First of all, I replicated a few applications from this blog:
 [https://blog.streamlit.io/tag/llms/](https://blog.streamlit.io/tag/llms/)

Then I have focused on Langchain. I'm also 
in the middle of a course on Udemy about Next-Gen AI projects - Beginner friendly - Langchain, Pinecone - OpenAI, Huggin
gFace & LLAMA 2 models

I need a roadmap that will guide me a bit. I'm looking for blogs/materials/courses that will giv
e me practical knowledge in this matter.
```
---

     
 
deeplearning -  [ VectorDB Operations with Faiss (View, Add, Delete, Save, QnA and Similarity Search) via Langchain ](/r/LangChain/comments/15qm2ie/vectordb_operations_with_faiss_view_add_delete/) , 1691993028.0
```

```
---

     
 
deeplearning -  [ QnA system that supports multiple file types[PDF, CSV, DOCX, TXT, PPT, URLs] with LangChain on Colab ](/r/LangChain/comments/15mld5x/qna_system_that_supports_multiple_file_typespdf/) , 1691601693.0
```

```
---

     
 
deeplearning -  [ Using PDFs with GPT Models ](https://www.reddit.com/r/deeplearning/comments/15g6i4x/using_pdfs_with_gpt_models/) , 1690976012.0
```
Found a blog talking about how we can interact with PDFs in Python by using GPT API & Langchain. It talks about some pre
tty cool automations you can build involving PDFs - [https://nanonets.com/blog/chat-with-pdfs-using-chatgpt-and-openai-g
pt-api/](https://nanonets.com/blog/chat-with-pdfs-using-chatgpt-and-openai-gpt-api/)
```
---

     
 
deeplearning -  [ List of all MLOps & LLMOps companies -- LLMOps.Space ](https://i.redd.it/d26rgf9fmnfb1.png) , 1690963455.0
```

```
---

     
