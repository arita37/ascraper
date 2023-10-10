 
all -  [ Make LLM to answer based on my postresql table QA ](https://www.reddit.com/r/LangChain/comments/1745pp4/make_llm_to_answer_based_on_my_postresql_table_qa/) , 2023-10-10-0909
```
I want to make Chatgpt answer some question based on my table which has a column question and another column which is an
swers and it has a list of answers in it. Is there a way to do this ?
```
---

     
 
all -  [ HI, I need some Insights on RAG, possibly a solution or suggestion ](https://www.reddit.com/r/LangChain/comments/17411qu/hi_i_need_some_insights_on_rag_possibly_a/) , 2023-10-10-0909
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

     
 
all -  [ Building RAG-based LLM Applications for Production (Part 1) ](https://www.anyscale.com/blog/a-comprehensive-guide-for-building-rag-based-llm-applications-part-1) , 2023-10-10-0909
```

```
---

     
 
all -  [ AI to create professional photos for folks who can't afford them ](https://www.reddit.com/r/singularity/comments/173xo3f/ai_to_create_professional_photos_for_folks_who/) , 2023-10-10-0909
```
Hi all - I work for an ed-tech company that specializes in giving access to skills and training to those who aren't serv
ed by traditional education channels. We are providing skills to get your first job, how money works, food safety, hygin
e, things like this.

We are focused mainly on Southern Africa right now and one thing we've noticed our learners strugg
le with is that they aren't able to have professional-looking headshots taken. This is something that is often used in h
iring situations in these markets.  They all have access to low-end smartphones though. 

Can anyone recommend a way for
 us to add the capability to take a photo (or multiple?) and turn it into something you'd likely see on LinkedIn or simi
lar? I'm the CTO and pretty deep into Langchain and other LLM technologies. I've used Midjourney for original creations,
 but need some help finding a technique for this use case. Thanks!
```
---

     
 
all -  [ What Memory Type Do You Recommend? ](https://www.reddit.com/r/LangChain/comments/173t400/what_memory_type_do_you_recommend/) , 2023-10-10-0909
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

     
 
all -  [ How to make an agent decide and call multiple functions if needed? ](https://www.reddit.com/r/LangChain/comments/173rv7y/how_to_make_an_agent_decide_and_call_multiple/) , 2023-10-10-0909
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

     
 
all -  [ Let’s see everyone’s LangChain Projects! ](https://www.reddit.com/r/homeassistant/comments/173rsy7/lets_see_everyones_langchain_projects/) , 2023-10-10-0909
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

     
 
all -  [ Is there any way to load online PDFs using UnstructuredURLLoader? ](https://www.reddit.com/r/LangChain/comments/173qx3d/is_there_any_way_to_load_online_pdfs_using/) , 2023-10-10-0909
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

     
 
all -  [ Best techniques for optimizing LLM agent speed ](https://www.reddit.com/r/LangChain/comments/173pdpz/best_techniques_for_optimizing_llm_agent_speed/) , 2023-10-10-0909
```
Hey folks-

Looking for a summary of techniques for minimizing latency. Even with simple agent architectures (e.g. 1 GPT
 3.5 agent or 2-5 talking to each other), latency feels quite high (>30s).

Thinking of trying out fine-tuned Mistral & 
optimizing prompt lengths, relying on Vector DBs more, etc. Curious what others have done successfully.
```
---

     
 
all -  [ Summary of latest language-AI techniques with example LangChain code? ](https://www.reddit.com/r/LangChain/comments/173p3ys/summary_of_latest_languageai_techniques_with/) , 2023-10-10-0909
```
Hey folks-

I'm looking for a small collection / cheatsheet of common patterns & example code demonstrating how to imple
ment with LangChain - e.g. Retrieval-Augmented Generation, ReAct agents, Tree of Thought, Plan & Execute agents, etc.

I
deally, would be <10 pages with code + succinct explainers.

Cheers
```
---

     
 
all -  [ Best solution for serving & fine-tuning Mistral 7B & other OSS models ](https://www.reddit.com/r/LangChain/comments/173p2h3/best_solution_for_serving_finetuning_mistral_7b/) , 2023-10-10-0909
```
Hey folks!

I'm looking for a platform where I can query the Instruct version of Mistral 7B & easily fine-tune it to my 
use-case cheaply & easily via LangChain.

What's the current best option(s)?
```
---

     
 
all -  [ Best way to expand the Next-Langchain starter? ](https://www.reddit.com/r/LangChain/comments/173ovyr/best_way_to_expand_the_nextlangchain_starter/) , 2023-10-10-0909
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

     
 
all -  [ add metadata to document without openai ](https://www.reddit.com/r/LangChain/comments/173l5x4/add_metadata_to_document_without_openai/) , 2023-10-10-0909
```
How to add metadata to my document (i.e a contract between buyer and seller). Now while storing documents in vector stor
e (FAISS). I want to add meta data to each contract but without the use of openai. Kindly suggest any way to do this.

M
eta data: buyer name, vendor name, duration of the contract, pricing condition etc

&#x200B;
```
---

     
 
all -  [ Best solutions for Chainlit-like experience w/real-time audio conversations? ](https://www.reddit.com/r/LangChain/comments/1737v04/best_solutions_for_chainlitlike_experience/) , 2023-10-10-0909
```
I want to create an experience similar to the real-time audio-based conversational experience OpenAI released in ChatGPT
 recently:  
[https://openai.com/blog/chatgpt-can-now-see-hear-and-speak](https://openai.com/blog/chatgpt-can-now-see-he
ar-and-speak)  


I've started using ChainLit recently and love how easy it makes it to build a text-based frontend for 
a LLM - I'm wondering if something similar exists for making audio-chat like experiences yet?
```
---

     
 
all -  [ SQLDatabaseChain and ConversationalRetrievalChain ](https://www.reddit.com/r/LangChain/comments/1735yvo/sqldatabasechain_and_conversationalretrievalchain/) , 2023-10-10-0909
```
I have these two chains in Python that work nicely each on their own but I encountered 2 problems that I would apreciate
 if anybody wants to brainstorm with me.  


1. The sql chain has problems with questions that require context from chat
 history. Should I make a cusotm chain just to condense the question with chat history and then feed this question to bo
th chains? Is there a better option or an already implemented condensation chain?
2. How should I put the two together? 
SQLDatabaseChain is great since it fetches real time data while ConversationalRetrievalChain is great since it fetches m
y vector store data. How should I combine the two?

Thank you for any ideas
```
---

     
 
all -  [ Easiest JS Chatbot Template - SvelteKit + Langchain + Vercel AI SDK ](https://www.reddit.com/r/aiengineer/comments/1730k7d/easiest_js_chatbot_template_sveltekit_langchain/) , 2023-10-10-0909
```
Looking to chat with ChatGPT about YOUR documents?📷    


Let me show you the easiest way I found to make a fully functi
onal QA Chatbot with: 

* u/sveltejs SvelteKit
* u/LangChainAI JavaScript
* u/vercel AI SDK

The chat endpoint is less t
han 100 lines of code!   


Follow me on twitter for more SvelteKit + AI Engineer content: [https://twitter.com/SimonNom
1/status/1710286285733294209](https://twitter.com/SimonNom1/status/1710286285733294209)    


Check out the repo here:  
 
[https://github.com/SimonPrammer/svelte-chat-langchain](https://github.com/SimonPrammer/svelte-chat-langchain) 
```
---

     
 
all -  [ Issues using chromadb with splade model ](https://www.reddit.com/r/LangChain/comments/172xq82/issues_using_chromadb_with_splade_model/) , 2023-10-10-0909
```
I’m using splade model to create sparse embeddings which have a dimension size over 30000. I’m wanting to know if anyone
 here has used sparse embeddings and a vector database before and if I could get some help.
```
---

     
 
all -  [ As of 2023, it is possible to scrape a site that wasn't in the training set for a model to query it  ](https://www.reddit.com/r/ArtificialInteligence/comments/172xjdb/as_of_2023_it_is_possible_to_scrape_a_site_that/) , 2023-10-10-0909
```
Hi! I'm working with people with disabilities. It's a very specific field and the content was no used to train GPT. So, 
when you query GPT (or the competition for that matter), the information is not returned.  Example: very specific inform
ation on correlation between behaviours and certain disabilities.

I understand I could use langchain or similar to 'scr
ape' the content and feed it back to the user as part of an chat agent. But it seems to only spit out the information ve
rbatim, rather than 'comprehend' what it was presented with in order to rehash it in a simple manner.  
So my question i
s: it it possible to do this in 2023, using either cloud based solutions or local environments ?  


Thank you.
```
---

     
 
all -  [ I’m looking for this prompt engineering game, but I forgot what it is called ](https://www.reddit.com/r/LangChain/comments/172x1ti/im_looking_for_this_prompt_engineering_game_but_i/) , 2023-10-10-0909
```
This game has a nodal interface, and lets you design a prompt using these boxes which you connect with wires. Different 
boxes do different things, logic, sliders, or a box that represents a person. 

Then you press the run button, and it ge
nerates the output. 

Does anyone know what game this is?

It’s also dark mode, and has a really cool looking design.

I
f you know what it is, you will seriously make my year, it was so much fun!
```
---

     
 
all -  [ Rag with ChatGPT and ChromaDB for BG3 using Langchain ](https://www.reddit.com/r/kungfudev/comments/172j1hu/rag_with_chatgpt_and_chromadb_for_bg3_using/) , 2023-10-10-0909
```
In recent weeks, I've been delving into GenAI while also enjoying the fantastic game Baldur's Gate 3 (BG3).

&#x200B;

[
https://www.kungfudev.com/blog/2023/10/07/poc-langchain-chromadb](https://www.kungfudev.com/blog/2023/10/07/poc-langchai
n-chromadb)

&#x200B;
```
---

     
 
all -  [ How to implement filters in MongoDB Atlas Vector Search? (Using langchain.js) ](https://www.reddit.com/r/LangChain/comments/172evas/how_to_implement_filters_in_mongodb_atlas_vector/) , 2023-10-10-0909
```
Hello, 

For context, here's the structure of the documents in my collection: 

    {
         _id: ObjectId(),
        
text: 'Bye bye',
        embedding: Array,
        id: 1,
        site: 'check'
    }

Now I am trying to call the vecto
rStore.asRetriever() method with the goal of only retrieving documents where site = 'check' but I am unable to do so usi
ng the following code:

    const retriever = await vectorStore.asRetriever({
      searchType: 'mmr',
      searchKwarg
s: {
        fetchK: 2,
        lambda: 0.1
      },
      filter: {
          'compound': {
              'must': [
   
               {
                      'text': {
                          'path': 'site',
                          'qu
ery': 'check'
                      }
                  }
              ]
          }
      }
    });

Any idea how to a
chieve the above? A similar question was asked for the Python version and I've already tried the suggested approach but 
to no avail: [https://www.mongodb.com/community/forums/t/filtering-the-results-of-vector-search-with-langchain/240608](h
ttps://www.mongodb.com/community/forums/t/filtering-the-results-of-vector-search-with-langchain/240608)
```
---

     
 
all -  [ Use Case for langchain (or not)? ](https://www.reddit.com/r/LangChain/comments/1722804/use_case_for_langchain_or_not/) , 2023-10-10-0909
```
Hello, sorry for the title could not find anything better.

I'm a 'traditional' software engineer that has been asked fr
om the boss if I can develop the following application:

'we have A LOT (around half millinon) of PDF documents that are
 reports about the performance of a company. Each report is very long (around 100 pages of text) and is terminated by a 
couple of tables that summarize the same information for quick lookup. The reports are 'printed' from word documents, an
d the word document itself come from a dozen of templates (because the template changed with the passing of time) and th
ose coming from the same period differ between only for the few information (for example, the name of the company, the a
ddress, the number of employers etc.). Also most of the information would be easy accessible, if only the tables could b
e easy to read from a pdf. Lastly, the boss would like to chat with the document asking informations about it. But also 
wants to chat wit the dabase as a whole'

Some examples of queries:

'Who is the medic that works for the company X?' (e
ach company has one and only one medic associated with them)

'What are the companies served by a particular medic?'

'W
hat company has the property X?' (the properties are  described in the table with a checkbox

&#x200B;

Here it is the i
ntuition of the usefulness of a LLM chain: the request to 'chat' with the knoledge database

Here are my worries, though
:

* first question is the more easy in my opinion to go right because I could find the relative embedding and make chat
gpt or someone else reply just for that information on that single document. However, a question: should the chunk conta
in both the medic name and the company name (for the context), or just the medic? Because, as I said, The document is 10
0 pages long and the company name is cited ONLY in the first page. Easy to solve, but a question since I'm beginner
* Se
cond question: as I have understood, LLM can reply only to something they has Just seen, I mean that you have to present
 them with an embedding and they can answer only on that. Suppose that a medic is associated to 10000 companies (I doubt
, but it is just an example) as far as I know it cannot reply since most LLM can take up to 4k token as an input. Am I r
ight?
* 3rd question, as far as I have seen through experimentation, LLM have trouble reading on tables, whatever the fo
rmatting is. Am i right?

&#x200B;

All this concerns make me wonder if this problem should be approached from an algori
thmic perspective and a traditional (sql o nosql) database. Is that correct, or there is a margin of hybridations? May b
e should I try looking towards chain agents (just found them, might be the case)?I'm not looking about code, just some h
ints on what to do or not to do

thanks to everyone

&#x200B;
```
---

     
 
all -  [ Summary/QA from 5-10 page text without vectorizing it ](https://www.reddit.com/r/LangChain/comments/171zzst/summaryqa_from_510_page_text_without_vectorizing/) , 2023-10-10-0909
```
Hey,

I'm wokring in a market intelligence function and I have a weekly need of providing 5-10 bullet point summaries of
 competitors news which they publish.

Idelly, I would be able to load a PDF to langchain and and the results which the 
LLM  gives would be following structure which I can define.

Issue in vectorstore approach is that it only selects x chu
nks which will be assessed/summarized, but I would like to take everything in scope (although it's costly but so is my t
ime 😄). For example in financial reports the relevant numbers might be very scattered within the document.

Any suggesti
on whether tejre would be better options than:
1) extract pdf to test eg pypdf
2) input text string as prompt input to t
he LLM and use a conversationalchain

Thanks a alot for your help!
```
---

     
 
all -  [ AI Conference in SF with CEO of LangChain ](https://www.reddit.com/r/conferences/comments/171vv1p/ai_conference_in_sf_with_ceo_of_langchain/) , 2023-10-10-0909
```
 

[**SingleStore**](https://www.linkedin.com/feed/#) is hosting, ‘SingleStore Now: The Real-Time AI Conference’ on Oct 
17th at the Chase Center in San Francisco!

Highlights include:

\- Keynotes from industry stalwarts like [**Harrison Ch
ase**](https://www.linkedin.com/feed/#), CEO of [**LangChain**](https://www.linkedin.com/feed/#).

\- Opportunities for 
invaluable networking within the industry.

\- Engaging, hands-on sessions covering a gamut of topics from LLMs to vecto
r databases.

\- A chance to participate in an AI hackathon (and win prizes!).

\- Live demonstrations and tutorials on 
building applications with ChatGPT, semantic search, image recognition, and more!

Although the regular ticket price is 
$199, I'm thrilled to share a special code with you. Register here: https://singlestorenowtherealtimeaicon.splashthat.co
m/ using “Vinija-25” and attend the event for only $25!

Whether you're just beginning your journey into AI and semantic
 search, or keen on mastering the craft of creating comprehensive generative AI applications, this conference promises i
mmense value!
```
---

     
 
all -  [ repo for digestion and logical chunking of pdfs? ](https://www.reddit.com/r/LangChain/comments/171k6gm/repo_for_digestion_and_logical_chunking_of_pdfs/) , 2023-10-10-0909
```
are there repos or methods out there for effectively digesting, analyzing the layout, charts graphs etc that may be with
in a pdf, and creating a chunking schema for upload to a vector db, that would work on most layouts found in pdfs?
```
---

     
 
all -  [ Telling the LLM where to look before retrieval ](https://www.reddit.com/r/LangChain/comments/171idqq/telling_the_llm_where_to_look_before_retrieval/) , 2023-10-10-0909
```
I built a custom chatbot that can answer questions based on content from either youtube or a specific website.   


Both
 youtube and website content are stored in my local vectorstore via FAISS.

  
When a user asks a chatbot a question tha
t can be answered by the website, we want it to look there instead of youtube. And vice-versa. Right now, it's retrievin
g mostly from youtube because queries generally semantically match youtube content, even though a simple response can be
 found from the website.  


I was thinking I need to build an LLM-based classifier system or a Langchain function. This
 first step would have the LLM determine where to look. I haven't played around with functions - can a function be an LL
M call?

&#x200B;

Any other tips or pointers would be appreciated! Happy to report back on what we try and how it perfo
rms.

&#x200B;
```
---

     
 
all -  [ 'How to finetune LLM Using RLHF ?' - Postive Review Chatbot 404 - YouTube ](https://www.reddit.com/r/LangChain/comments/171ecew/how_to_finetune_llm_using_rlhf_postive_review/) , 2023-10-10-0909
```
 ['How to finetune LLM Using RLHF ?' - Postive Review Chatbot 404 - YouTube](https://www.youtube.com/watch?v=B5dhaZPJQx0
) 
```
---

     
 
all -  [ Open-source alternative to Chatbase, SiteGPT and Dante AI built with Langchain ](https://www.reddit.com/r/LangChain/comments/171dx1h/opensource_alternative_to_chatbase_sitegpt_and/) , 2023-10-10-0909
```
Chatbase, SiteGPT and Dante AI allow you to chat with your data. I have made an open-source solution so that you can run
 something like that yourselves

Here is the link to it :- [https://github.com/Anil-matcha/Chatbase](https://github.com/
Anil-matcha/Chatbase)
```
---

     
 
all -  [ How to improve the quality of RAG answers? ](https://www.reddit.com/r/LangChain/comments/171bevs/how_to_improve_the_quality_of_rag_answers/) , 2023-10-10-0909
```
All those 'Chat with PDF' apps out there show particularly good results compared to standard Langchain QnA based on RAG.
 I wonder how do they improve the quality of answers. 

This becomes even more evident when you deal with questions like
 'summarize this doc'. I don't see how one could use RAG to answer questions related to summarization. I have been doing
 some research but haven't found any effective solution yet.
```
---

     
 
all -  [ Task Specific Alternative to GPT-4 ](https://www.reddit.com/r/LocalLLaMA/comments/1719t4m/task_specific_alternative_to_gpt4/) , 2023-10-10-0909
```
I'm creating different agents to complete various tasks, and one of which is to crawl through a website to find specific
 information. It was easiest to prove out the concept with GPT-4 since a lot of libraries (like Langchain) already creat
e zero shot agent implementations for that model. Now that I have proved out the concept, I want to find a model I can d
eploy locally. Right now, I can test with a 3090 locally, but I will soon have some A100s at my disposal. Does anyone ha
ve recommendations for models that would do well with this task? I know I will have to do some prompt engineering to tes
t this out more thoroughly for anything else. It would be great if there was a very task-specific leaderboard of models
```
---

     
 
all -  [ Size scaling for vector databases (Chroma DB specifically) ](https://www.reddit.com/r/LangChain/comments/170qmjp/size_scaling_for_vector_databases_chroma_db/) , 2023-10-10-0909
```
Has anyone run across or conducted their own study of how the size of the files and datastorage increase with the number
 of document chunks that are loaded into the database? Is it quadratic, sub-linear, etc?

Also how sensitive is the size
 the choice of embeddings? If you use the \`text-embedding-ada-002\` with 1500 dimensions compared with another model wi
th only 300, will the database size go up linearly (approximately 5x larger)?

We've started exploring this idea, but I 
wanted to if anyone has dug into it already.
```
---

     
 
all -  [ AI assistant integration beyond the native integration? ](https://www.reddit.com/r/todoist/comments/170ptp5/ai_assistant_integration_beyond_the_native/) , 2023-10-10-0909
```
Hi all - 

Long time Todoist user here, new to the subreddit.. 

I have tried the 'AI Assistant' that Todoist put out an
d this is useful in some ways, but what I'm looking for is to have AI assist me with trying to prioritize against my goa
ls, remind me of what is important, be able to add new tasks based on our conversations, etc. 

I have some experience d
eveloping Langchain based solutions using AI and I'm tempted to do this myself, but before I go down that road, I wanted
 to see if there were existing solutions. 

Does this exist already? Has anyone built their own version of this?
```
---

     
 
all -  [ Finetuned models for function calling? ](https://www.reddit.com/r/LocalLLaMA/comments/170pej3/finetuned_models_for_function_calling/) , 2023-10-10-0909
```
Hello. Are there finetuned LLaMa2 models that can reliably work for function calling yet? (Setting up agents in Langchai
n and such). Previous discussion is around 2 months old so I wonder if there has been some advances on this.

I have bee
n trying to build a chatbot that can search on the internet and can be locally hosted but the models I've tried are terr
ible at this.
```
---

     
 
all -  [ Give our customers an LLM to talk to about their data ](https://www.reddit.com/r/LocalLLaMA/comments/170npuw/give_our_customers_an_llm_to_talk_to_about_their/) , 2023-10-10-0909
```
Hello guys, we are a small web design company, and we are testing langchain and llama2 llm locally. We want to be able t
o create a chatbot for our customers so the llm can check out their hosting stats and our customers can ask questions su
ch as 'how much more space do I need if I want to add a new email account, create a database, when will I need to upgrad
e my account,  etc,,  So our main question is, where can we read up on how many concurrent users we can have if we use l
angchain and how can we setup ques or buffering so when the GPU is bogged down, it will still process the queries from o
ur customers but keep them in a waiting list until their request is up. Is this a crazy project or doable? Thanks!
```
---

     
 
all -  [ RecursiveCharacterTextSplitter: create_documents vs split_documents ](https://www.reddit.com/r/LangChain/comments/170mfkc/recursivecharactertextsplitter_create_documents/) , 2023-10-10-0909
```
Greetings to the community,

My first post here. Apologies in advance for any possible violation of community's establis
hed principles and practices 🙏

In the RecursiveCharacterTextSplitter class, I'm not clear about the difference between 
the two methods: **create\_documents** vs **split\_documents**.

Suppose I've a given text, in any form, whether split/u
n-split in NLP sentences. It could be from multiple documents (PDF/text).

Which method I should choose to split the tex
t, and why?

For example, in Section 3 of *Ingest chat embedding* given here [https://python.langchain.com/docs/use\_cas
es/question\_answering/integrations/semantic-search-over-chat](https://python.langchain.com/docs/use_cases/question_answ
ering/integrations/semantic-search-over-chat), first split\_text is used (with CharacterTextSplitter), and then create\_
documents (with RecursiveCharacterTextSplitter). Why not directly use **split\_documents** on the initial text?
```
---

     
 
all -  [ My strategy for picking a vector database: a side-by-side comparison ](https://www.reddit.com/r/LangChain/comments/170jigz/my_strategy_for_picking_a_vector_database_a/) , 2023-10-10-0909
```
I made this table to compare vector databases in order to help me choose the best one for a new project. I spent quite a
 few hours on it, so I wanted to share it here too in hopes it might help others as well. My main criteria when choosing
 vector DB were the speed, scalability, developer experinece, community and price.

https://preview.redd.it/dw181oiz8esb
1.png?width=1870&format=png&auto=webp&s=cf26639b12a1b6e5662198f11fe31f71c9ba8123

You'll find all of the comparison para
meters in the article and more details here: [https://benchmark.vectorview.ai/vectordbs.html](https://benchmark.vectorvi
ew.ai/vectordbs.html)  


Edit: For transparency, I am the co-fouder of Vectorview.ai which is an analytics tool for sem
antic search that let's developers understand how their embedded documents are used. 
```
---

     
 
all -  [ Interested in using LangChain and llama.cpp, to create industry specific search / chat bot, for data ](https://www.reddit.com/r/LangChain/comments/170ij5e/interested_in_using_langchain_and_llamacpp_to/) , 2023-10-10-0909
```
Hi,

I'm a software / solution architect, in eCommerce. I'm a competent developer and system architect, but new to LLMs,
 or even training a chatbot. I've built a very basic chatbot on node/react, using the OpenAI API. However, from this I l
earned two things, because of the size and complexity of the data I want to train the LLM on, I will need something more
 structured like LangChain. And, because of the nature of the tool I'd like to build, I'm not sure the OpenAI fee struct
ure will be financially viable.

This utility / search tool will be useful to the service departments of auto dealership
s, and just general service shops.

I expect they will value its utility at somewhere between $499, and $999 per year. T
hey won't want to pay an extreme amount for this, but they will pay for it. And there are 1000s of shops for whom it wou
ld save time for their employees, and be of use.

There might be 100 searches per day on it, from each paid user, and wi
th OpenAIs model, based on really limited experience, and sort of a gut feeling from my testing.... I think that would m
ean low, or negative margins, if relying on OpenAI / ChatGPT.

My expectation, and hope, is instead to build an applicat
ion that runs entirely locally, using llama.cpp, and run this utility on a single server.

I am looking for someone with
 technical understanding of using llama.cpp with LangChain, who has trained a LLM against a large and complex database, 
who might be interested in working on this project with me as a consultant.

&#x200B;

Thanks
```
---

     
 
all -  [ I'm wondering if it's possible to patent the LangChain Process that I developed. ](https://www.reddit.com/r/legaladvice/comments/170i0ph/im_wondering_if_its_possible_to_patent_the/) , 2023-10-10-0909
```
Our team created a proprietary approach utilizing LLMs and LangChain derivative. Is it patentable?
```
---

     
 
all -  [ AutoGen from Microsoft ](https://www.reddit.com/r/learnmachinelearning/comments/170hl7w/autogen_from_microsoft/) , 2023-10-10-0909
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

     
 
MachineLearning -  [ [P] Retrieval augmented generation with OpenSearch and reranking [Video tutorial] ](https://www.reddit.com/r/MachineLearning/comments/16zouad/p_retrieval_augmented_generation_with_opensearch/) , 2023-10-10-0909
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

     
 
MachineLearning -  [ [D] Perplexity.ai Search Feasibility ](https://www.reddit.com/r/MachineLearning/comments/16x63ce/d_perplexityai_search_feasibility/) , 2023-10-10-0909
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

     
 
MachineLearning -  [ [P] vLLM, Langchain, Embedchain ? ](https://www.reddit.com/r/MachineLearning/comments/16ndyxc/p_vllm_langchain_embedchain/) , 2023-10-10-0909
```
Which libraries do you think would be the most important to learn between these, and to use in my next personal project 
? This will be a conversational chatbot trained on podcast transcripts
```
---

     
 
MachineLearning -  [ [R] Agents: An Open-source Framework for Autonomous Language Agents - AIWaves Inc 2023 ](https://www.reddit.com/r/MachineLearning/comments/16jl4pe/r_agents_an_opensource_framework_for_autonomous/) , 2023-10-10-0909
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

     
 
MachineLearning -  [ [P] Ways to speed up llama-2 summarization on sagemaker? ](https://www.reddit.com/r/MachineLearning/comments/16iutyp/p_ways_to_speed_up_llama2_summarization_on/) , 2023-10-10-0909
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

     
 
MachineLearning -  [ [P][R] Kani: A Lightweight Highly Hackable Open-Source Framework for Building Chat Applications with ](https://www.reddit.com/r/MachineLearning/comments/16gxp51/pr_kani_a_lightweight_highly_hackable_opensource/) , 2023-10-10-0909
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

     
 
MachineLearning -  [ [D] Data Extraction using fine-tuned LLM? ](https://www.reddit.com/r/MachineLearning/comments/16fenlb/d_data_extraction_using_finetuned_llm/) , 2023-10-10-0909
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

     
 
deeplearning -  [ TheBloke/Llama-2-7b does not appear to have a file named pytorch_model.bin, tf_model.h5, model.ckpt  ](https://www.reddit.com/r/deeplearning/comments/16ihzn8/theblokellama27b_does_not_appear_to_have_a_file/) , 2023-10-10-0909
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

     
