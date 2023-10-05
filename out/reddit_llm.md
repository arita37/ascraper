 
all -  [ looking to figure out how to get an agent to read text classifiers and then apply to descriptions ](https://www.reddit.com/r/LangChain/comments/17021gf/looking_to_figure_out_how_to_get_an_agent_to_read/) , 2023-10-05-0910
```
I'm trying to get LangChain to read two Excel files - one with classifier info and the other with company descriptions. 
The goal is to classify the companies based on the info in the first file. Got the files loaded up, but stumbling a bit 
with setting up the agent and executor in LangChain to process this data and get the results out. Anyone here tackled so
mething similar or got some tips? Thanks!
```
---

     
 
all -  [ Handle sessions with separate ID's without res-instantiating RedisChatMessageHistory ](https://www.reddit.com/r/LangChain/comments/16zyemd/handle_sessions_with_separate_ids_without/) , 2023-10-05-0910
```
I have an LangChain/Flask application where each request carries a session ID, and therefore I can separate their messag
e histories as follows (pseudo-code):  


    @app.post('chat')
    def chat(str):
        redis = RedisChatMessageHisto
ry(
            # Use the incoming session_id
            session_id=app.request.session_id
        )
    
        conve
rsation = ConversationChain(
            llm=llm, 
            memory=ConversationBufferMemory(
                # Use th
e Redis adaptor, which only has access to the given app.request.session_id history
                chat_memory=redis
   
         )
        )
    
        conversation({'input': app.request.body'}

The problem with this approach is that I ha
ve to instantiate the Chain and its components at every request, introducing some overhead.

Is there a (thread-safe) wa
y to change  \`RedisChatMessageHistory\` session\_id without instantiating the whole thing every time?
```
---

     
 
all -  [ Easy RAG Implementation for GenAI using Mongo: Langchain alternative ](https://www.reddit.com/r/mongodb/comments/16zx1gc/easy_rag_implementation_for_genai_using_mongo/) , 2023-10-05-0910
```
Hi all, we worked really hard to develop our open source library on Github for easy, straightforward RAG implementation 
for GenAI using Mongo (and Milvus, FAISS or PineCone for vector DB). We built in a lot of features for easy document ing
estion that is scalable as well as native parsing for PDFs and Office documents for a very fast ingestion. Please check 
out our LLMWare library and we would be extra grateful if you can leave a star!

[https://github.com/llmware-ai/llmware]
(https://github.com/llmware-ai/llmware)
```
---

     
 
all -  [ New Github Library for RAG: Langchain Alternative ](https://www.reddit.com/r/ArtificialNtelligence/comments/16zwrsa/new_github_library_for_rag_langchain_alternative/) , 2023-10-05-0910
```
HI all, we worked really hard and created an open source library that is an integrated RAG system for GenAI with a lot o
f great features on Github for LLMWare (straightforward, easy to use). It would be great if you can check it out (would 
be extra grateful if you can leave a star). Thank you!

[https://github.com/llmware-ai/llmware](https://github.com/llmwa
re-ai/llmware)
```
---

     
 
all -  [ Interesting hallucinations with a RAG-type chatbot ](https://www.reddit.com/r/LangChain/comments/16zqz0p/interesting_hallucinations_with_a_ragtype_chatbot/) , 2023-10-05-0910
```
I'm building a RAG chatbot for IT support. It ingests KB articles (chunked), retrieves them based on the query and then 
runs the 'classic' prompt that instructs the LLM to answer only using the source material from the retriever.  So far so
 good and the results were good in a pre-testing phase.  
Then I started testing with real-world questions and I stumble
d into an interesting case:  
\- the user types a message about not being to get into Microsoft Project.  
\- the retrie
ver retrieves an article about troubleshooting not being able to use Outlook.   
\- the LLM uses the chunk, copies the t
ext almost as is and substitutes the text 'Outlook' with 'Project' going as far as changing the name of the outlook exec
utable into the supposed project executable (winproj.exe) in a procedure. Of course the answer is wrong but I cannot get
 the LLM to simply say 'I do not know'.  
The LLM used is GPT-3.5 16k, latest version from Azure Open AI.  
I talked wit
h other people developing RAG chatbots and nobody saw something like that (but they are using other non-GPT models like 
Claude and llama).  


Any ideas? Did u see something like that happen? Did you find a solution?
```
---

     
 
all -  [ Memory is not working with ConversationalRetrievalQAChain. ](https://www.reddit.com/r/LangChain/comments/16zpv8l/memory_is_not_working_with/) , 2023-10-05-0910
```
Hey, so I am working with next JS 13, langchain and supabase. I have used  

ConversationalRetrievalQAChain like this:


     const qachain =  ConversationalRetrievalQAChain.fromLLM(
        model, 
        vectorstore.asRetriever(),
       
 { memory: memory,
          questionGeneratorChainOptions:{
          template: CONDENSE_QUESTION_TEMPLATE, 
          
llm:nonStreamingModel
        },
        qaChainOptions: {
          type: 'stuff', 
          prompt: PromptTemplate.fr
omTemplate(ANSWER_TEMPLATE)
        },
      });

I tried adding  ConversationSummaryMemory as memory but it isn't worki
ng. 

    const memory = new ConversationSummaryMemory({
          llm: model, 
          memoryKey: 'chat_history', 
  
        inputKey: 'question',   
          returnMessages: true,
        });

I tried printing what is being stored in t
he memory like this:  


    console.log('This is memory: ',memory.buffer);

But nothing is being print.

Here is how I 
call the chain:

    const callbacks = CallbackManager.fromHandlers(handlers);
    const latest = messages[messages.leng
th - 1].content;
    qachain.call({ 
          question: latest,
          chat_history:(messages as Message[]).map((m) 
=> `${m.role}: ${m.content}`).join('\n')}, 
          callbacks
          ).catch((e) => {
          console.error('____
___________ THIS IS THE ERROR ________', e);
      }); 

&#x200B;
```
---

     
 
all -  [ As a soloproneur, here is how I'm scaling with AI and GPT-based tools ](https://www.reddit.com/r/Entrepreneur/comments/16zp7pt/as_a_soloproneur_here_is_how_im_scaling_with_ai/) , 2023-10-05-0910
```
Being a solopreneur has its fair share of challenges. Currently I've got businesses in ecommerce, agency work, and affil
iate marketing, and one undeniable truth remains: to truly scale by yourself, you need more than just sheer will. That's
 where I feel technology, especially AI, steps in.

As such, I wanted some AI tools that have genuinely made a differenc
e in my own work as a solo business operator. No fluff, just tried-and-true tools and platforms that have worked for me.
 The ability for me to scale alone with AI tools that take advantage of GPT in one way, or another has been significant 
and really changed my game over the past year. They bring in an element of adaptability and intelligence and work right 
alongside “traditional automation”. Whether you're new to this or looking to optimize your current setup, I hope this po
st helps. FYI I used multiple prompts with GPT-4 to draft this using my personal notes.

# Plus AI (add-on for google sl
ides/docs)

I handle a lot of sales calls and demos for my AI automation agency. As I’m providing a custom service rathe
r than a product, every client has different pain points and as such I need to make a new slide deck each time. And maki
ng slides used to be a huge PITA and pretty much the bane of my existence until slide deck generators using GPT came out
. My favorite so far has been PlusAI, which works as a plugin for Google Slides. You pretty much give it a rough idea, o
r some key points and it creates some slides right within Google Slides. For me, I’ve been pasting the website copy or a
ny information on my client, then telling PlusAI the service I want to propose. After the slides are made, you have a lo
t of leeway to edit the slides again with AI, compared to other slide generators out there. With 'Remix', I can switch u
p layouts if something feels off, and 'Rewrite' is there to gently nudge the AI in a different direction if I ever need 
it to. It's definitely given me a bit of breathing space in a schedule that often feels suffocating.

## echo.win (web-b
ased app)

As a solopreneur, I'm constantly juggling roles. Managing incoming calls can be particularly challenging. Ech
o.win, a modern call management platform, has become a game-changer for my business. It's like having a 24/7 personal as
sistant. Its advanced AI understands and responds to queries in a remarkably human way, freeing up my time. A standout f
eature is the Scenario Builder, allowing me to create personalized conversation flows. Live transcripts and in-depth ana
lytics help me make data-driven decisions. The platform is scalable, handling multiple simultaneous calls and improving 
customer satisfaction. Automatic contact updates ensure I never miss an important call. Echo.win's pricing is reasonable
, offering a personalized business number, AI agents, unlimited scenarios, live transcripts, and 100 answered call minut
es per month. Extra minutes are available at a nominal cost. Echo.win has revolutionized my call management. It's a comp
rehensive, no-code platform that ensures my customers are always heard and never missed

# MindStudio by YouAi (web app/
GUI)

I work with numerous clients in my AI agency, and a recurring task is creating chatbots and demo apps tailored to 
their specific needs and connected to their knowledge base/data sources. Typically, I would make production builds from 
scratch with libraries such as LangChain/LlamaIndex, however it’s quite cumbersome to do this for free demos. As each cl
ient has unique requirements, it means I'm often creating something from scratch. For this, I’ve been using MindStudio (
by YouAi) to quickly come up with the first iteration of my app. It supports multiple AI models (GPT, Claude, Llama), le
t’s you upload custom data sources via multiple formats (PDF, CSV, Excel, TXT, Docx, and HTML), allows for custom flows 
and rules, and lets you to quickly publish your apps. If you are in their developer program, YouAi has built-in payment 
infrastructure to charge your users for using your app.

Unlike many of the other AI builders I’ve tried, MindStudio bas
ically lets me dictate every step of the AI interaction at a high level, while at the same time simplifying the behind-t
he-scenes work. Just like how you'd sketch an outline or jot down main points, you start with a scaffold or decide to 'r
emix' an existing AI, and it will open up the IDE. I often find myself importing client data or specific project details
, and then laying out the kind of app or chatbot I'm looking to prototype. And once you've got your prototype you can cu
stomize the app as much as you want.

## LLamaIndex (Python framework)

As mentioned before, in my AI agency, I frequent
ly create chatbots and apps for clients, tailored to their specific needs and connected to their data sources. LlamaInde
x, a data framework for LLM applications, has been a game-changer in this process. It allows me to ingest, structure, an
d access private or domain-specific data.

The major difference over LangChain is I feel like LlamaIndex does high level
 abstraction much better.. Where LangChain unnecessarily abstracts the simplest logic, LlamaIndex actually has clear ben
efits when it comes to integrating your data with LLMs- it comes with data connectors that ingest data from various sour
ces and formats, data indexes that structure data for easy consumption by LLMs, and engines that provide natural languag
e access to data. It also includes data agents, LLM-powered knowledge workers augmented by tools, and application integr
ations that tie LlamaIndex back into the rest of the ecosystem. LlamaIndex is user-friendly, allowing beginners to use i
t with just five lines of code, while advanced users can customize and extend any module to fit their needs. To be compl
etely honest, to me it’s more than a tool- at its heart it’s a framework that ensures seamless integration of LLMs with 
data sources while allowing for complete flexibility compared to no-code tools.

## GoCharlie (web app)

GoCharlie, the 
first AI Agent product for content creation, has been a game-changer for my business. Powered by a proprietary LLM calle
d Charlie, it's capable of handling multi-input/multi-output tasks. GoCharlie's capabilities are vast, including content
 repurposing, image generation in 4K and 8K for various aspect ratios, SEO-optimized blog creation, fact-checking, web r
esearch, and stock photo and GIF pull-ins. It also offers audio transcriptions for uploaded audio/video files and YouTub
e URLs, web scraping capabilities, and translation.

One standout feature is its multiple input capability, where I can 
attach a file (like a brand brief from a client) and instruct it to create a social media campaign using brand guideline
s. It considers the file, prompt, and website, and produces multiple outputs for each channel, each of which can be edit
ed separately. Its multi-output feature allows me to write a prompt and receive a response, which can then be edited fur
ther using AI. Overall, very satisfied with GoCharlie and in my opinion it really presents itself as an effective altern
ative to GPT based tools.

# ProfilePro (chrome extension)

As someone overseeing multiple Google Business Profiles (GBP
s) for my various businesses, I’ve been using ProfilePro by Merchynt. This tool stood out with its ability to auto-gener
ate SEO-optimized content like review responses and business updates based on minimal business input. It works as a Chro
me extension, and offers suggestions for responses automatically on your GBP, with multiple options for the tone it will
 write in. As a plus, it can generate AI images for Google posts, and offer suggestions for services and service/product
 descriptions. While it streamlines many GBP tasks, it still allows room for personal adjustments and refinements, offer
ing a balance between automation and individual touch. And if you are like me and don't have dedicated SEO experience, i
t can handle ongoing optimization tasks to help boost visibility and drive more customers to profiles through Google Map
s and Search
```
---

     
 
all -  [ Streaming Question HOW TO - streaming a subsequent chain while the parent chain is still streaming o ](/r/Langchaindev/comments/16z4bn9/streaming_question_how_to_streaming_a_subsequent/) , 2023-10-05-0910
```

```
---

     
 
all -  [ [P] Retrieval augmented generation with OpenSearch and reranking [Video tutorial] ](https://www.reddit.com/r/MachineLearning/comments/16zouad/p_retrieval_augmented_generation_with_opensearch/) , 2023-10-05-0910
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

     
 
all -  [ Multiple llm route ](https://www.reddit.com/r/LangChain/comments/16zhtfl/multiple_llm_route/) , 2023-10-05-0910
```
 I am working on a project that involves conversational interactions with both Word and Excel files. Specifically, for h
andling Word files, I utilized the Lama2 model, which relies on a vector database to provide responses. Meanwhile, for E
xcel-related tasks, I used the GPT-3.5 model. How to determine which model to use based on the user's input prompt.
```
---

     
 
all -  [ Custom LLM agent with custom tool not work due to lack func argument ](https://www.reddit.com/r/LangChain/comments/16zcfpa/custom_llm_agent_with_custom_tool_not_work_due_to/) , 2023-10-05-0910
```
while following [https://python.langchain.com/docs/modules/agents/how\_to/custom\_llm\_agent#set-up-tool](https://python
.langchain.com/docs/modules/agents/how_to/custom_llm_agent#set-up-tool), we also want to custom tool adding extra schema
 validation, from the example for the tool listed, we need name, description, and func field, for custom tool we only ha
ve name and description field, here's the custom tool code [https://gist.github.com/elvis-cai/203487d2bfd11d57625d84f812
2e875e](https://gist.github.com/elvis-cai/203487d2bfd11d57625d84f8122e875e),   

this is the custom tool we are referrin
g to [https://python.langchain.com/docs/modules/agents/tools/custom\_tools#subclassing-the-basetool-class](https://pytho
n.langchain.com/docs/modules/agents/tools/custom_tools#subclassing-the-basetool-class).

&#x200B;

not sure how to make 
it work with pydantic validation, thanks. 
```
---

     
 
all -  [ Is there anyway to get chat-gpt's response while its still generating via langchain and python api? ](https://www.reddit.com/r/OpenAI/comments/16za9uw/is_there_anyway_to_get_chatgpts_response_while/) , 2023-10-05-0910
```
I created a short script that allows for me to interact with chat-gpt over phone. It prompts chat-gpt, feeds its respons
e into elevenlabs and then plays the audio out loud. However, this takes a very long time because eleven labs only stars
 generating the audio after gpt is completely done generating its response, and then it only starts playing after the en
tire audio has finished generating. This is super slow especially for longer responses, and it ruins the entire flow of 
the conversation. Does anyone know if there's anything I can do about this?
```
---

     
 
all -  [ Data Privacy - Memory features of Langchain ](https://www.reddit.com/r/LangChain/comments/16z9pxs/data_privacy_memory_features_of_langchain/) , 2023-10-05-0910
```
Hi all,

As the title indicates, I want to ask about the memory features in Langchain. I was talking to someone at work 
who raised some concerns about data security/privacy when dealing with the memory classes in Langchain. The main concern
 they have is about chat history getting stored in an external database during runtime.

My personal understanding based
 on documentation and also looking at the langchain repo is that the data is stored locally and there doesn't seem to be
 any indication of any interaction with external databases. If any of y'all have dealt with these kind of questions befo
re, how did you approach it? What steps or methods would you recommend to definitively address and alleviate these data 
storage concerns?

Thanks!
```
---

     
 
all -  [ Strategy for PDF data extraction and Display ](https://www.reddit.com/r/LangChain/comments/16z7sfl/strategy_for_pdf_data_extraction_and_display/) , 2023-10-05-0910
```
I'm learning LangChain and working on a project where I need to:

1. Extract data from a \~50 page PDF.
2. Display this 
data in structured tables.

For context, think of the PDF as a product catalog, with item names, descriptions, and price
s.

My first program uses PyPDF2 for PDF parsing and FAISS coupled with OpenAIEmbeddings for similarity-based querying. 
For instance:

    query = 'What is the price of the television set'
    docs = document_search.similarity_search(query)

    chain.run(input_documents=docs, question=query

This works well, but the result is plain-text and lacks structure. 
I've now shifted to learning structured output, creating a schema to define data representation.  My basic structure cou
ld be the item name, the item description, and the item cost.

Now, onto my main question: What's the most efficient app
roach for feeding PDF data into my structured output chain? Currently, I'm using broad queries like 'list all items with
 a price,' which tap into my initial vector-based similarity search framework. Is this approach more complicated than ne
cessary? Given that I've moved towards structured outputs and am essentially using 'catch-all' queries, the need for vec
tor-based querying seems redundant.  


\*Update - I did try just submitted the entire contents of the PDF, but its far 
larger than the token limit for most models I'm using; What's the best way to split up the document and submit for my st
ructured input, if not the vector/similarity search method?

Any tips or best practices are welcome!
```
---

     
 
all -  [ Langchain Chatbot is not that great.. ](https://www.reddit.com/r/LangChain/comments/16z7nzk/langchain_chatbot_is_not_that_great/) , 2023-10-05-0910
```
I noticed that langchain chatbot is prone to hallucination easily and does not provide accurate data. What's your expere
ince with it?  
Below is an example of it importing a class that does not exist (I searched under langchain repo -> libs
 -> langchain -> langchain -> llms)   


Perhaps it's not meant to solve this kinda probelm? would like to know others' 
feedbacks. 

https://preview.redd.it/4jkg6dd5r2sb1.png?width=904&format=png&auto=webp&s=318a2bad3ff686e02385409f8679e695
2b0e51e2

second example:   
correct way to import chatOllama: \`from langchain.chat\_models import ChatOllama\`   


ht
tps://preview.redd.it/jij85uhar2sb1.png?width=2306&format=png&auto=webp&s=569ccd2d4758e3da7a4cdd22c238b3e5001f2c72

&#x2
00B;
```
---

     
 
all -  [ After a few hours of battleing to make it understand ](https://www.reddit.com/r/LangChain/comments/16z54mf/after_a_few_hours_of_battleing_to_make_it/) , 2023-10-05-0910
```
This is peak prompt engineering.

&#x200B;

&#x200B;

https://preview.redd.it/emhr6d2p92sb1.png?width=957&format=png&aut
o=webp&s=2b8e1aa1f37b31c1864b7a432a49239bb4086efa
```
---

     
 
all -  [ User Feedback for RAG ](https://www.reddit.com/r/LangChain/comments/16z4rn3/user_feedback_for_rag/) , 2023-10-05-0910
```
I’ve read about using AI to generate sample questions and answers, then having end-users provide feedback and using that
 data to fine-tune a model. Would this approach would with embeddings and RAG? If the vector embedding contained sample 
questions and answers, could I prompt the bot to answer in the style of the sample answers from the embedding?
```
---

     
 
all -  [ Here to try to solve your LLM problems ](https://www.reddit.com/r/LangChain/comments/16z4mha/here_to_try_to_solve_your_llm_problems/) , 2023-10-05-0910
```
I have been working with NLP using machine learning and deep learning for 6.5  years and with LLMs since the time it bec
ame a thing. Have been working with other transformers models before that as well. 

If anyone has any business problem 
and wants  some help, I will be trying my best to help them out. I will be doing this for a small fee. 

No charge if I 
hear the problem and I do not have adequate knowledge to solve the issue even if I have spent some time towards solving 
it. 

Will share credential via DM if required.
```
---

     
 
all -  [ can RAG models base their answers from outside the documents? ](https://www.reddit.com/r/LangChain/comments/16z4bd3/can_rag_models_base_their_answers_from_outside/) , 2023-10-05-0910
```
can RAG models base their answers from outside the documents used?
```
---

     
 
all -  [ [Announcement] Upcoming event – Reddit AMA with Harrison Chase, co-founder and CEO of LangChain: Tue ](https://www.reddit.com/r/LangChain/comments/16z1s1p/announcement_upcoming_event_reddit_ama_with/) , 2023-10-05-0910
```
Join us on Tuesday, October 24th from 9-11 AM Pacific (12-2 PM Eastern) for an **AMA hosted** by **Harrison Chase, co-fo
under and CEO of LangChain**. This is your opportunity to ask Harrison questions about utilizing LangChain in developing
 large language model (LLM) applications, and to *share your own ideas and suggestions*. Take advantage of this chance t
o learn more about how to leverage LangChain in your own projects and get insights into latest developments.
```
---

     
 
all -  [ Use multiple Chroma Databases in Langchain ](https://www.reddit.com/r/LangChain/comments/16z0nkh/use_multiple_chroma_databases_in_langchain/) , 2023-10-05-0910
```
I'm working on making a chatPDF-like program for a school professor but he requested to keep the subjects divided, so I 
was thinking about making different pages for my website, each for every subject and link to every page a specific chrom
aDB, I don't know if it's possible though and I haven't found anything on the documentation.

Has anyone tried this befo
re or knows if it's even possible?
```
---

     
 
all -  [ My Journey with Langchain on finishing my MA and reinventing Dropbox powered by GPT ](https://www.reddit.com/r/LangChain/comments/16yz1ej/my_journey_with_langchain_on_finishing_my_ma_and/) , 2023-10-05-0910
```
As an introvert who finds solace in books and coding, I wanted to share a personal story that began in November last yea
r, that’s when I discovered Langchain. I was in the process of writing my master's thesis at the time. The timing just h
appened to be so perfect that I was using Langchain to conduct research for my final thesis. 

It allowed me to create m
y own knowledge base, a place where I could access a treasure trove of resources, including YouTube videos, PDFs, docume
nts, and presentations, and get needed information quickly.

Today, finally, as also a proud tiny contributor to Langcha
in I’m excited to present to you Knowbase.ai, my small app  that enables you to harness the power of your accumulated kn
owledge.

https://reddit.com/link/16yz1ej/video/s7s283z021sb1/player

Knowbase.ai is a versatile platform that can host 
YouTube videos, PDFs, documents, and presentations, making it your one-stop hub for knowledge.
```
---

     
 
all -  [ New to langchain ](https://www.reddit.com/r/LangChain/comments/16yxoa2/new_to_langchain/) , 2023-10-05-0910
```
When building a QnA based bot on uploaded Pdfs (like the many examples online), when the bot is answering questions does
 it just look at the docs for answers or is it broader?

sorry for the basic question
```
---

     
 
all -  [ Looking for Co-Founder to join an early stage start-up ](https://www.reddit.com/r/LangChain/comments/16yx4xs/looking_for_cofounder_to_join_an_early_stage/) , 2023-10-05-0910
```
I'm on the lookout for two passionate co-founders: one with technical expertise and another with a flair for marketing a
nd sales, to embark on an exciting journey with me. Here's a bit about the venture and myself:

**About the Startup**:


* **Niche**: We aim to revolutionize how companies integrate Legal Lifecycle Management (LLM) systems into their existin
g applications, making the process seamless and efficient.
* **Stage**: We are at the inception stage. I recently took t
he leap of faith and quit my full-time job to make this dream a reality.

**About Me**:

* **Background**: Graduated fro
m high school 2 years ago.
* **Experience**: Jumped straight into the tech scene and served as a software developer at a
 startup for 2 years. Has built and shipped 6 products with live users. Led the development of 2 of them.

**What I'm Lo
oking for**:

1. **Technical Co-founder**:

* **Skillset**: We are building it out in Next.js, TypeScript, Tailwind, and
 Prisma. Needs to be proficient in using Langchain. 
* **Mindset**: Entrepreneurial, ready for challenges, and committed
 to the cause.

1. **Marketing/Sales Co-founder**:

* **Skillset**: Proven experience in startup marketing, B2B sales, o
r SaaS marketing would be a big plus. Ability to strategize, execute, and optimize marketing campaigns, while also under
standing the nuances of selling tech solutions.
* **Mindset**: Growth-focused, data-driven, and someone who understands 
the startup hustle.

If any of the above roles resonate with you and wants to learn more send me an email at [shanyuzhan
g123@gmail.com](mailto:shanyuzhang123@gmail.com) or DM me.
```
---

     
 
all -  [ Best LLM serving providers for cost, latency, quality, auto-tuning & fine-tuning. ](https://www.reddit.com/r/LangChain/comments/16yssmf/best_llm_serving_providers_for_cost_latency/) , 2023-10-05-0910
```
I've been using OpenAI's API directly primarily thus far. Hugging Face looks interesting - but I'm not really clear on t
heir pricing or what models to select.
```
---

     
 
all -  [ How to know the langchain BTS? ](https://www.reddit.com/r/LangChain/comments/16yscor/how_to_know_the_langchain_bts/) , 2023-10-05-0910
```
How can I understand the system prompts langchain gives when I insert the pdf?
```
---

     
 
all -  [ How can i merge 2 Models? ](https://www.reddit.com/r/LocalLLaMA/comments/16yrc6c/how_can_i_merge_2_models/) , 2023-10-05-0910
```
so i have 2 models that are very good the synthia-34b-v1.2.Q4\_K\_M is uncensored but not that good for langchain while 
the speechless-llama2-hermes-orca-platypus-wizardlm-13b.Q8\_0 is perfect for langchain but its censored so is there a wa
y to merge them together to make the synthia-34b better or the speechless-llama2-hermes-orca-platypus-wizardlm-13b uncen
sored i have a 3090 if that changes anything
```
---

     
 
all -  [ Automating comic creation using Langchain ](https://www.reddit.com/r/LangChain/comments/16yozpt/automating_comic_creation_using_langchain/) , 2023-10-05-0910
```
hello,
I am trying to learn programming as a hobby (I have some experience with visual scripting as level designer). 
I 
would like to learn python with a project that will motivate me, so here is a project I would love to achieve : generati
ng a comic book as automatically as possible.

I want to learn to use OpenAI api, to help me automate the creation of a 
comics. I would like to be able to chain prompts to brainstorm ideas, then develop the characters relations, the world, 
and the overall story arc, and finally generate the story page by page… and generate image with dale when it is possible
 (soon hopefully)

Unfortunately I am lacking some basic knowledge to help me get started. Is langchain a good framework
  for this kind of prompt chaining project, also parsing of a csv/xml file with my prompts.
Any recommended resources or
 tutorials that can help me get started?

If you know someone who is working on similar project or have brick of codes I
 would love to hear about.

I'm grateful for any advice or pointers you can offer!
Thanks
```
---

     
 
all -  [ Is it possibile to connect to the 'Browse with Bing' feature on Open AI? ](https://www.reddit.com/r/LangChain/comments/16yn5bp/is_it_possibile_to_connect_to_the_browse_with/) , 2023-10-05-0910
```
Just wondering if there is anyway to call upon it through langchain.
```
---

     
 
all -  [ How to stream AI responses from server actions? ](https://www.reddit.com/r/nextjs/comments/16yjgi2/how_to_stream_ai_responses_from_server_actions/) , 2023-10-05-0910
```
Does anyone know if and how I can stream ChatGPT responses from server actions? I have Vercel's `ai` library and Langcha
in installed.
```
---

     
 
all -  [ What are some of your gripes with Langchain? ](https://www.reddit.com/r/LangChain/comments/16yj4s2/what_are_some_of_your_gripes_with_langchain/) , 2023-10-05-0910
```
langchain has gotten too complicated, so i'm building [tinylang](https://github.com/astelmach01/tinylang), a simpler alt
ernative.

what are some things you'd like to see?  
what are some things in langchain that just seem super unecessary o
r annoying?
```
---

     
 
all -  [ Overview: AI Assembly Architectures ](https://www.reddit.com/r/AI_Agents/comments/16yc9zg/overview_ai_assembly_architectures/) , 2023-10-05-0910
```
I'm currently trying to make a list with all agent-systems, RAG systems, cognitive architectures, and similar. Then coll
ecting data on the features and limitations, as many points of distinction as possible, opinions, ... Input is welcome.


- Auto-GPT: [github.com/Significant-Gravitas/Auto-GPT](https://github.com/Significant-Gravitas/Auto-GPT)
- AutoGen: [gi
thub.com/microsoft/autogen](https://github.com/microsoft/autogen)
- BASI: [github.com/oliveirabruno01/babyagi-asi](https
://github.com/oliveirabruno01/babyagi-asi)
- BabyAGI: [github.com/yoheinakajima/babyagi](https://github.com/yoheinakajim
a/babyagi)
- GripTape: [griptape.ai](https://griptape.ai)
- Jarvis: [github.com/microsoft/JARVIS](https://github.com/mic
rosoft/JARVIS)
- LangChain [docs.langchain.com/docs](https://docs.langchain.com/docs)
- LlamaIndex: [github.com/run-llam
a/llama\_index](https://github.com/run-llama/llama_index)
- Open-Assistant [github.com/LAION-AI/Open-Assistant](https://
github.com/LAION-AI/Open-Assistant)
- Semantic Kernel [github.com/microsoft/semantic-kernel](https://github.com/microsof
t/semantic-kernel)
- SmartGPT: [github.com/Cormanz/smartgpt](https://github.com/Cormanz/smartgpt)
- TxAI: [github.com/ne
uml/txtai](https://github.com/neuml/txtai)
- tinyLLM: [github.com/zozoheir/tinyllm](https://github.com/zozoheir/tinyllm)


# Chatbots and Conversational AI:
- BondAI: [github.com/krohling/bondai](https://github.com/krohling/bondai)
- BeeBot:
 [github.com/AutoPackAI/beebot](https://github.com/AutoPackAI/beebot)

# Machine Learning and Data Processing:
- NeMo-Gu
ardrails: [github.com/NVIDIA/NeMo-Guardrails](https://github.com/NVIDIA/NeMo-Guardrails)
- Haystack: [github.com/deepset
-ai/haystack](https://github.com/deepset-ai/haystack)
- EdgeChains: [github.com/arakoodev/EdgeChains](https://github.com
/arakoodev/EdgeChains)

# Frameworks for Advanced AI, Reasoning and Cognitive Architectures:
- ACT-R (Adaptive Control o
f Thought - Rational)
- Soar
- CLARION
- OpenCog: [github.com/opencog](https://github.com/opencog)
- Dave Shapiro: [yout
ube.com/@4IR.David.Shapiro](https://youtube.com/@4IR.David.Shapiro)
- Some guys from IBM Watson worked on it (forgot the
 name)
- Cyc: [en.wikipedia.org/wiki/Cyc](https://en.wikipedia.org/wiki/Cyc)

# Agents in a Virtual Environment
- MineRL
: [minerl.io](https://minerl.io)
- Malmo: [github.com/malmo](https://github.com/microsoft/malmo)
- AgentVerse: [github.c
om/AgentVerse](https://github.com/OpenBMB/AgentVerse)

# Comments and Comparissons (probably outdated)
- /r/ChatGPT/comm
ents/12cql0c/autogpt_vs_babyagi/
- /r/AutoGPT/comments/15jrs4n/autogpt_is_failing_to_acomplish_its_goals/

# Curated Lis
ts
- [github.com/awesome-ai-agents](https://github.com/e2b-dev/awesome-ai-agents)
- [github.com/Awesome-AGI](https://git
hub.com/EmbraceAGI/Awesome-AGI)

# Recommended Tutorials
- RAG: gpt-index.readthedocs.io/en/latest/examples/low_level/os
s_ingestion_retrieval.html
- RAG: https://python.langchain.com/docs/expression_language/cookbook/retrieval

EDIT: Update
d from time to time.
```
---

     
 
all -  [ Building a Chatbot for Internal Document Retrieval Using Language Models ](https://www.reddit.com/r/LangChain/comments/16y76tm/building_a_chatbot_for_internal_document/) , 2023-10-05-0910
```
Hello everyone,

I am currently an intern at a company and am exploring a project idea to pave my way to a full-time pos
ition. I've noticed that employees often need to share and request information contained in various documents (Excel fil
es, emails, etc.). I am considering creating a chatbot to simplify this information retrieval process across different d
epartments.

I've begun by learning about language models and have managed to set up a system that loads documents from 
a directory, converts them to text, and utilizes OpenAI's embedding model to create and save embeddings to a Chroma data
base. I've tested this setup with some machine history data in CSV format provided by a coworker. The goal is to answer 
queries like, 'What's the average number for this column between these dates?' However, the system should also handle em
ails, PDFs, Excel, and Word files.

I used the Llama 7B model for embedding because  I was hitting a token limit per min
ute with the OpenAI model, especially with large files (\~10,000 lines of data). After setting up the VectorDB, I faced 
a token limit issue again while trying to answer questions due to the large amount of data being processed.

Considering
 the privacy and performance requirements, I am also contemplating the use of a local AI model on a powerful machine ins
tead of relying on cloud-based solutions like OpenAI. This could potentially address the performance issues and ensure b
etter data privacy and maybe help me to overcome token limitations.

I initially tried using OpenAI's embedding model to
 process the documents, but I ran into a limitation on the number of tokens that could be processed per minute. Due to t
his restriction, I decided to switch to a local model for embedding, specifically the [**Mistral-7B-v0.1 model**](https:
//huggingface.co/mistralai/Mistral-7B-v0.1) from Hugging Face. This switch allowed me to process the documents and build
 the database without hitting any token limitations. Now that the database is complete, I've switched back to using Open
AI for other parts of the process. However, I am not entirely sure if everything is set up correctly as this code has be
en pieced together over the past three days, and I'm eager to ensure it's on the right track.  


My code:  [here](https
://textbin.net/wibm5znigu)

**Here are my requirements:**

1. Ensure high privacy.
2. Handle a large amount of data effi
ciently.
3. Provide quick responses.
4. Achieve 99% accuracy based solely on document information.

**I have several que
stions and would appreciate any insights:**

1. Am I on the right track with my current approach?
2. Is ChromaDB the rig
ht choice, or is there a better database for my needs?
3. Would a local AI model be more suitable, or is OpenAI preferab
le in this scenario?
4. Are there other models better suited for embedding or chatting, especially with Excel and CSV fi
les? If yes, is it advisable to use different models for different file types?

**Ideally, I'd like to:**

* Specify dat
a (e.g., by department or file name) to make easy for AI.
* Retain a memory of chats for follow-up queries based on prev
ious responses.
* Update the database with new files and data seamlessly.

*Please note that I am not seeking help due t
o laziness; I am on a time limit for this project. While I would continue searching for solutions, any assistance that c
ould help expedite my progress would be greatly appreciated.*

Thank you for your time and suggestions!
```
---

     
 
all -  [ Not split PDF's ](https://www.reddit.com/r/LangChain/comments/16y6ist/not_split_pdfs/) , 2023-10-05-0910
```
I'm trying to process PDF's without splitting them by pages. I essentially want to consider the entire PDF as a single d
ocument. Should I convert the PDF to a single TXT file and then process it or is there anything within the documentation
. I was not able to find anything in the documentation.
```
---

     
 
all -  [ Limiting BabyAGI tasks list... ](https://www.reddit.com/r/LangChain/comments/16y41tc/limiting_babyagi_tasks_list/) , 2023-10-05-0910
```
I have been looking into BabyAGI capabilities and have a small setup done where I have :

*  research reports (PDF) inge
sted in my vector store(azure search)
* ToDo and  ConversationalRetrievalChain  provided as tools to agent\_executor

No
w when i run babyagi with an objective it starts creating tasks using todo tool, which uses openai as llm. But the tasks
 are way out of context from what I have in my search vectordb. Thus, the agent keep creating tasks which cannot be acco
mplished based on data I have in my search index.  


This results in agent going in loops and tasks keep growing until 
max\_iteration count i reached and ends with no answer.  


So, Is there a way to constrict tasks to what can be accompl
ished from knowledge base? Or skip the ones that failed to complete and generate answer out of what was accomplished?
```
---

     
 
all -  [ Chatbot for website? ](https://www.reddit.com/r/LangChain/comments/16y2u4o/chatbot_for_website/) , 2023-10-05-0910
```
How to build a Chatbot that can be integrated with existing websites?
```
---

     
 
all -  [ Langchain tool ](https://www.reddit.com/r/LangChain/comments/16y2p94/langchain_tool/) , 2023-10-05-0910
```
I am looking for a tool easy to setup and fully managed where langchain vector database and API to retrieve information 
can be included. What is your favorite tool? Thanks
```
---

     
 
all -  [ github web scraping? ](https://www.reddit.com/r/ChatGPT/comments/16xy8s9/github_web_scraping/) , 2023-10-05-0910
```
does anyone know the best way to get a whole documentation in a suitable format to integrate with an llm?

I'm thinking 
about using pinecone/langchain to teach an llm my codebase. but the first step is to get the data from the repo.

I trie
d using 'apify' directly on the main github repo page but it seems inefficient and like it ends up with a bunch of usele
ss data.

apologies if any of this is absurd, im new to it. (also is all of this kosher with github's terms and conditio
ns and stuff?)
```
---

     
 
all -  [ github repo scraping? ](https://www.reddit.com/r/LargeLanguageModels/comments/16xy7rz/github_repo_scraping/) , 2023-10-05-0910
```
does anyone know the best way to get a whole documentation in a suitable format to integrate with an llm?

I'm thinking 
about using pinecone/langchain to teach an llm my codebase. but the first step is to get the data from the repo. 

I tri
ed using 'apify' directly on the main github repo page but it seems inefficient and like it ends up with a bunch of usel
ess data. 

apologies if any of this is absurd, im new to it.  (also is all of this kosher with github's terms and condi
tions and stuff?)
```
---

     
 
all -  [ Running OpenAI on top of Function Calls / Agents? ](https://www.reddit.com/r/LangChain/comments/16xvdp6/running_openai_on_top_of_function_calls_agents/) , 2023-10-05-0910
```
We have created a custom agent on top of the built-in CSV and SQL agent - it works great.

Behind the scenes, its runnin
g python code, and I cannot figure out how to run OpenAI Functions on top of that code.

For example, if i upload a CSV 
file, i would like to run OpenAI sentiment on top of the dataset - instead, all the code can run is the built-in python 
libraries, like NLTK, which is weirdly limiting.

Am I missing something?
```
---

     
 
all -  [ Doubt about embeddings with vector stores ](https://www.reddit.com/r/LangChain/comments/16xub91/doubt_about_embeddings_with_vector_stores/) , 2023-10-05-0910
```
Hi guys!

I have adoubt about embedding prices, so here it's the code I'm currently using, which worked (I modified it f
or private information)  


    loader = ConfluenceLoader(url='https://confluenceweb.com', token='tokenConfluence')
    

    documents = loader.load(
        space_key='spaceKey', include_attachments=False, limit=50, max_pages=20
    )
    

    text_splitter = RecursiveCharacterTextSplitter(chunk_size = 500, chunk_overlap = 0)
    
    all_splits = text_spli
tter.split_documents(documents)
    
    vectorstore = Chroma.from_documents(documents=all_splits, embedding=OpenAIEmbed
dings(openai_api_key='openApiKey'))
    
    query = 'Question for the model'
    docs = vectorstore.similarity_search(q
uery)
    
    llm = ChatOpenAI(model_name='gpt-3.5-turbo', temperature=0, openai_api_key='openAiApiKey', max_tokens=100
)
    qa_chain = RetrievalQA.from_chain_type(llm,retriever=vectorstore.as_retriever())
    result = qa_chain({'query': q
uery})
    

The goal of this code is the following: We want to make QA for the information in our Confluence. We want t
o train the model to answer as an assistant for a customer portal.  


**My doubt is the following one:** Do I always ha
ve to pay the price for OpenAiEmbeddings? I've just tried using Chroma, one of the vectorstores recomended in the docume
ntation. In case I execute this code several times, will I always have to pay it?   


Is there any way to have this  se
parated in **two scripts? One for the 'ingestion'** of information from our documents into the vector store and a s**eco
nd script that just asks the model without having to pay the embedding again**. I know that I will always have to pay fo
r passing the question with the prompt and for generating the answer... But is there a way to load everything from my Co
nfluence, embed it and then just make different questions over it? Or will I always need to pay the embedding price?

Sh
ould I just use an open-source free embedding solution like  all-MiniLM-L6-v2? **This project is going to be hosted in A
mazon Web Services**, so I dont know if there would be any kind of problem with that because we dont want to have any lo
cal machine running this code.

&#x200B;

I'm really confused about vector stores, if you could guide me, it would mean 
a lot.

&#x200B;
```
---

     
 
all -  [ Best way to distill information from a long HTML document? ](https://www.reddit.com/r/LocalLLaMA/comments/16xtjq0/best_way_to_distill_information_from_a_long_html/) , 2023-10-05-0910
```
Hi, I am looking for some pointers to distill information from a single, large but quite structural (to human) **HTML** 
document containing some event schedules\*. 

I am using langchain's WebBaseLoader to perform the data ingestion, Recurs
iveCharacterTextSplitter for chunking and Chroma DB as the vector store. Retrieval is done using ConversationalRetrieval
Chain.

The problems I am facing are the title of the event and the schedule information do not sit next to each other, 
and the html2text essentially messed up all the event-schedule relationship (it ended up with all the events jammed toge
ther in one long paragraph and the schedules scattered everywhere). The chunking of text also led to further separation 
of the events and schedule information, and that the answers produced, if any, were only limited to what the maximum con
text the LLM could handle.

My questions are, do you have a better experience dealing with this kind of problem involvin
g many large HTML tables in a single long HTML document? What is the best way to have the LLM to parse and understand su
ch document in order to extract information, not from part of it, but through the whole thing in order to compose the an
swer?

\* A very typical example is [https://www.royalalberthall.com/tickets/](https://www.royalalberthall.com/tickets/)
 . with the exception that the title and the schedule are farther apart (many tables each with many rows). I would like 
to make a query to the LLM such as:

'List all classical music concerts in Oct 2023 in a tabular form containing only th
e titles and the date-time of the concert. For examples:

Title | Date

Easy listening classical | 28 Oct 18:30

Four se
asons- Winter | 30 Oct 19:00'
```
---

     
 
all -  [ llama-cpp on T4 google colab, Unable to use GPU ](https://www.reddit.com/r/LocalLLaMA/comments/16xswej/llamacpp_on_t4_google_colab_unable_to_use_gpu/) , 2023-10-05-0910
```
 In Google Colab, though have access to both CPU and GPU T4 GPU resources for running following code. However, what is t
he reason I am encounter limitations, the GPU is not being used?  I selected T4 from runtime options  

`!CMAKE_ARGS='-D
LLAMA_BLAS=ON -DLLAMA_BLAS_VENDOR=OpenBLAS' pip install llama-cpp-python`

&#x200B;

`!pip install langchain`

`!wget` [
`https://huggingface.co/TheBloke/Llama-2-7b-Chat-GGUF/resolve/main/llama-2-7b-chat.Q5_0.gguf`](https://huggingface.co/Th
eBloke/Llama-2-7b-Chat-GGUF/resolve/main/llama-2-7b-chat.Q5_0.gguf)

&#x200B;

`from langchain.llms import LlamaCpp`

`f
rom langchain.prompts import PromptTemplate`

`from langchain.chains import LLMChain`

`from langchain.callbacks.manager
 import CallbackManager`

`from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler`

&#x200B;

`
prompt = PromptTemplate(template=template, input_variables=['question'])`

&#x200B;

`callback_manager = CallbackManager
([StreamingStdOutCallbackHandler()])`

&#x200B;

`llm = LlamaCpp(`

`model_path='/content/llama-2-7b-chat.Q5_0.gguf',`


`temperature=0.75,`

`max_tokens=500,`

`top_p=1,`

`callback_manager=callback_manager,`

`verbose=True,`

`)`

`llm_cha
in = LLMChain(prompt=prompt, llm=llm)`

&#x200B;

`llm_chain.run(question)`

&#x200B;
```
---

     
 
all -  [ How to download Spotify podcast transcripts? ](https://www.reddit.com/r/LangChain/comments/16xqnid/how_to_download_spotify_podcast_transcripts/) , 2023-10-05-0910
```
Has anyone figured out the best way to process and summarize Spotify podcast?
```
---

     
 
all -  [ About to buy Hardware for 7k ](https://www.reddit.com/r/LocalLLaMA/comments/16xq65o/about_to_buy_hardware_for_7k/) , 2023-10-05-0910
```
 Hey,

At the end of the month, I'll be receiving a profit share of 7k, which I intend to use to purchase hardware for a
n LLM.

I was thinking of:

2x 3090(Used) Intel Core i9-13900K 256GB DDR5 RAM A suitable motherboard, of course (500-1k$
) Is a 1000W PSU enough, or would a 1500W PSU be better?

Using the cloud is not an option for me because I want to trai
n my LLM on my own data, and I generally prefer it to be uncensored, as I'm tired of hearing phrases like, 'As an LLM, I
'd like to remind you that blablabla.'

The goal is to learn how to create a self-operating AI Assistant with Langchain,
 etc., and an RAG where I can store ALL my knowledge about everything that interests me. I just want to dive in and lear
n by working on various projects and expanding my knowledge.

I'm thinking of using 2x 3090 so that I can experiment wit
h combining different models and see how they interact with each other, among other things.

I'm just asking here for an
y potential pitfalls to watch out for. Any hardware suggestions? Are there any good beginner projects?

I'm not particul
arly skilled in Python, but that doesn't mean I can't learn it.
```
---

     
 
MachineLearning -  [ [D] Perplexity.ai Search Feasibility ](https://www.reddit.com/r/MachineLearning/comments/16x63ce/d_perplexityai_search_feasibility/) , 2023-10-05-0910
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

     
 
MachineLearning -  [ [P] vLLM, Langchain, Embedchain ? ](https://www.reddit.com/r/MachineLearning/comments/16ndyxc/p_vllm_langchain_embedchain/) , 2023-10-05-0910
```
Which libraries do you think would be the most important to learn between these, and to use in my next personal project 
? This will be a conversational chatbot trained on podcast transcripts
```
---

     
 
MachineLearning -  [ [R] Agents: An Open-source Framework for Autonomous Language Agents - AIWaves Inc 2023 ](https://www.reddit.com/r/MachineLearning/comments/16jl4pe/r_agents_an_opensource_framework_for_autonomous/) , 2023-10-05-0910
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

     
 
MachineLearning -  [ [P] Ways to speed up llama-2 summarization on sagemaker? ](https://www.reddit.com/r/MachineLearning/comments/16iutyp/p_ways_to_speed_up_llama2_summarization_on/) , 2023-10-05-0910
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

     
 
MachineLearning -  [ [P][R] Kani: A Lightweight Highly Hackable Open-Source Framework for Building Chat Applications with ](https://www.reddit.com/r/MachineLearning/comments/16gxp51/pr_kani_a_lightweight_highly_hackable_opensource/) , 2023-10-05-0910
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

     
 
MachineLearning -  [ [D] Data Extraction using fine-tuned LLM? ](https://www.reddit.com/r/MachineLearning/comments/16fenlb/d_data_extraction_using_finetuned_llm/) , 2023-10-05-0910
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

     
 
MachineLearning -  [ [D] Chains and Agents ](https://www.reddit.com/r/MachineLearning/comments/16d7ee6/d_chains_and_agents/) , 2023-10-05-0910
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

     
 
MachineLearning -  [ [P] FalkorDB - a fast Graph Database - Knowledge Graph as RAG ](https://www.reddit.com/r/MachineLearning/comments/16cg6k7/p_falkordb_a_fast_graph_database_knowledge_graph/) , 2023-10-05-0910
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

     
 
deeplearning -  [ TheBloke/Llama-2-7b does not appear to have a file named pytorch_model.bin, tf_model.h5, model.ckpt  ](https://www.reddit.com/r/deeplearning/comments/16ihzn8/theblokellama27b_does_not_appear_to_have_a_file/) , 2023-10-05-0910
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

     
 
deeplearning -  [ How to find 'custom' datasets for LLM ](https://www.reddit.com/r/deeplearning/comments/16bj3hg/how_to_find_custom_datasets_for_llm/) , 2023-10-05-0910
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

     
