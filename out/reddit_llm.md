 
all -  [ How to Stop Document Retrieval in a RAG chatbot for Greeting input from user Like Hi, Hello, Good Mo ](https://www.reddit.com/r/LangChain/comments/19d9d6t/how_to_stop_document_retrieval_in_a_rag_chatbot/) , 2024-01-23-0910
```
I have built RAG chatbot entirely from scratch NO langchain involved. The docs are retrieved for every query, I want to 
Stop docs Retrieval for Greeting messenges.

I have tried conditional check by storing all Greeting messages in a list w
hich worked fine
But what if user enters different greeting message that's not in list,  what if he enters with spelling
 mistakes. This will definitely fail.

How to handle this?
```
---

     
 
all -  [ LLM based ChatBots with Memory ](https://www.reddit.com/r/LangChain/comments/19d72dg/llm_based_chatbots_with_memory/) , 2024-01-23-0910
```
I am building a chatbot using Azure OpenAI API. Is there a way I can integrate the memory module of the Langchain framew
ork into my chat application? Currently, I am using summarization to implement the short-term memory but I would like to
 expand the memory implications to a long-term memory and also manage the summarization using the buffer memory methods 
in Langchain. My conversations are currently stored in a Redis cache.
```
---

     
 
all -  [ Developing an app using open source LLMs ](https://www.reddit.com/r/LangChain/comments/19d64ek/developing_an_app_using_open_source_llms/) , 2024-01-23-0910
```
Hi folks

I'm currently trying to build an app (python) using local llms 
I tried Mistral 7b instruct. 
I have tried few
 prompts asking the model to generate code snippets and functions. But now i have to test the model if it can give sourc
e code to build an app (let's say a chatbot for instance). 
Basically the input would be a use case in natural language


For example: Build an end to end chatbot that can answer customer's queries and help with the issues.

What should be m
y approach ? How to get this done ? Please provide suggestions since I'm really new to LLMs. If possible provide any tut
orials or guides.
```
---

     
 
all -  [ vec2word ](https://www.reddit.com/r/LangChain/comments/19d3z4g/vec2word/) , 2024-01-23-0910
```
I want to embed a prompt, invert the sign of each embedding, then turn that new embedding back into text.

I am getting 
stuck on getting the embedding transformed back into words...

how do you do that?
```
---

     
 
all -  [ Mistral 7B from Mistral.AI - FULL WHITEPAPER OVERVIEW ](https://youtu.be/rSUqg5X4SAU?si=xoXyfmrDUu7idHI3) , 2024-01-23-0910
```

```
---

     
 
all -  [ Create full RAG solution tutorial ](https://www.reddit.com/r/LangChain/comments/19d11xt/create_full_rag_solution_tutorial/) , 2024-01-23-0910
```
I am trying to build rag solution for a user guide
I have worked with chromadb and OpenAI but I want to build something 
robust step by step 
Can you suggest something for me 
Thanks
```
---

     
 
all -  [ wht chat_histrory ](https://www.reddit.com/r/LangChain/comments/19cus3v/wht_chat_histrory/) , 2024-01-23-0910
```
I know this is not related langchain. somehow i am unable to post in python group. why the hell this is showing error. c
hat\_history I declared at  99. why its showingerror at 106 but not at 108

&#x200B;

&#x200B;

https://preview.redd.it/
4e8lqlgolzdc1.png?width=1324&format=png&auto=webp&s=277c36af1e06d189b047d50ada64a7b07001ed8c
```
---

     
 
all -  [ FAISS as Retriever: Score Treshold not working ](https://www.reddit.com/r/LangChain/comments/19ctf42/faiss_as_retriever_score_treshold_not_working/) , 2024-01-23-0910
```
Hi,

in a RAG application, I am using FAISS as retriever:

`retriever = vectorstore.as_retriever(search_kwargs={'k': 3, 
'score_treshold': 0.9}, search_type='similarity')`

`retriever.get_relevant_documents('- I am Karl and I play soccer')`


However when changing the Score-Treshold I am still getting back the same documents. So there is no difference if I set
 it to 0.1 or 0.9.

In my understanding it should work as follows:

\- Search the top 3 docs that have a similarity scor
e of 0.9 or higher.

\- If for example only one doc has a higher similarity than 0.9, only retrieve one doc.

\- But: it
 is always retrieving 3 Docs, even if they are not similar

&#x200B;

Is this assumption correct or how can I make it wo
rk?
```
---

     
 
all -  [ Developing an AI-Powered Gym chat app ](https://www.reddit.com/r/LangChain/comments/19csujt/developing_an_aipowered_gym_chat_app/) , 2024-01-23-0910
```
I'm working on an innovative gym app that incorporates AI for personalized workout plans and diet charts, sourced from a
 gym owner's knowledge base.

Here's the scoop: 

Users can input their daily attendance, receive workout plans(from tra
iners), track meals, and chat with an AI bot. 

The Ai  bot should consider knowledge based and user's previous history 
texts and their database(their workout and meal history and plan(weightloss) and their Medical condition(optional) ) and
 provide optimal answers according to the users queries


My tech arsenal I like to use includes 

Rag, LangChain, Supab
ase, supabase - VectorDB, and Next.js. I'm eager to hear your thoughts and insights on how to make this ambitious projec
t a reality. Any advice, suggestions, or experiences you can share would be immensely helpful! Thanks a ton! 💪🤖
```
---

     
 
all -  [ Survey about Retrieval Augmented Generation (RAG) in Real Production ](https://www.reddit.com/r/LangChain/comments/19crogm/survey_about_retrieval_augmented_generation_rag/) , 2024-01-23-0910
```
I'm now working in an AI company, and we're developing infra products to enhance RAG. As the product marketing, it's imp
ortant to hear from the community. I want to know:

* How necessary do you think the RAG project can be for your current
 business?
* What are the primary challenges you face with the current implementation of RAG?
* Which embedding model yo
u are using now？
* Have you considered finding a better Embedding model to get better results from RAG?

I'm looking for
ward to seeing your reply from anyone who is exploring RAG for real production. You are also welcome to share your insig
hts via the [survey](https://forms.gle/xkyBpruTC7twZxSz7), and I‘ll then contact you to discuss future collaboration opp
ortunities. You may find more information about our product, the Jina Embeddings model in the survey form. And our Embed
dings have been integrated into Langchain already. 
```
---

     
 
all -  [ function calling with mistral or agent langchain with mistral - help wanted ](https://www.reddit.com/r/MistralAI/comments/19cq269/function_calling_with_mistral_or_agent_langchain/) , 2024-01-23-0910
```
can someone please provide a reference for this? I wanted to call different tools .& for that need some support of funct
ion calling in mistral .help is really appreciated
```
---

     
 
all -  [ RAG vs. full context ](https://www.reddit.com/r/LangChain/comments/19cpvw6/rag_vs_full_context/) , 2024-01-23-0910
```
I found that using RAG to search for documents through a vector store definitely loses some of the information, such as 
context, because it has no way to look at your problem based on the whole document. langchain There is a concept propose
d in that, which is `Parent Document Retriever`. But even so, I think he may not be as effective as passing all the data
 as context to LLM,then this also derives a maximum token problem, then does it mean: the model that supports the most t
okens is better at searching, something like `CLAUDE2` vs `ChatGPT`. It feels like the simplest and crudest is instead t
he most effective

Edit：
Or maybe this is the way to go.
[advanced-rag](https://medium.com/@akriti.upadhyay/building-adv
anced-rag-applications-using-falkordb-langchain-diffbot-api-and-openai-083fa1b6a96c)
```
---

     
 
all -  [ Create AI Chatbots for Websites in Python - EmbedChain Dash ](https://www.reddit.com/r/LangChain/comments/19coe4m/create_ai_chatbots_for_websites_in_python/) , 2024-01-23-0910
```
Hey Everyone,I just created a free video tutorial showing how to build an AI Chatbots for Beginners in Python. We'll use
 the EmbedChain (built on top of LangChain) and Dash libraries, and we'll learn the core principles of training and inte
racting with your bot. I hope you learn a lot.

[https://youtu.be/tmOmTBEdNrE](https://youtu.be/tmOmTBEdNrE)

&#x200B;


https://preview.redd.it/tq1ovgfihxdc1.png?width=1280&format=png&auto=webp&s=b4e1593532e2f396d0397ec80161020a30d14b69
```
---

     
 
all -  [ New Grad seeking Data Science/ML/Computer Vision/NLP roles. 200+ apps, 0 interviews. Any suggestions ](https://www.reddit.com/r/resumes/comments/19ckqfk/new_grad_seeking_data_sciencemlcomputer_visionnlp/) , 2024-01-23-0910
```
Can you please evaluate my resume and tell me what am I doing wrong/can improve upon? Is my resume unable to parse ATS?


https://preview.redd.it/yeztutkmiwdc1.jpg?width=2481&format=pjpg&auto=webp&s=0a94d4b08a03a9057e2b49b7ea6aee6e9112054f
```
---

     
 
all -  [ Chatbot RAG and tool about crypto ](https://www.reddit.com/r/LangChain/comments/19cgrpd/chatbot_rag_and_tool_about_crypto/) , 2024-01-23-0910
```
I already have some basic knowledge about langchain and LLM. Now I want to apply it to a production environment, but I r
ealize that basic knowledge is not enough. I want to make a news Q&A chatbot application using RAG and use API access to
ols to get real-time information about cryptocurrencies. Does anyone have a sample repo that I can refer to? Thank you v
ery much
```
---

     
 
all -  [ I haven’t seen anyone do it yet, so I built an agent that can talk to my car via the Ford API ](https://www.reddit.com/gallery/19cei8t) , 2024-01-23-0910
```
Step one is done. I build an agent that’s using the gpt-3.5-turbo api, and langchain to house the Ford API as a callable
 tool.
```
---

     
 
all -  [ Request to improve integration with openai assistant api to add custom functions registered inside p ](https://www.reddit.com/r/LangChain/comments/19c9969/request_to_improve_integration_with_openai/) , 2024-01-23-0910
```

Not sure where to ask this question

Why: I am seeing mild success with openai assistant api on their portal platform.o
penai.com. However it's impossible to test custom functions on their portal. DevX of that api is not straightforward. I 
seem to like Langchain attempts to wrap this capability. However it's missing this ability to register custom functions.
 

Please guide me if there's a work around?

----
Feature Request created by chat.langchain.com after I couldn't get my
 answer on this help portal
---
Subject: Feature Request: Custom Function Registration in Langchain
Dear Langchain Team,

I hope this message finds you well. I am a user of the Langchain platform and have been exploring the capabilities of t
he OpenAI Assistant integration. While working with the platform, I noticed that there is no explicit documentation or m
ention of a register_function method for registering custom functions with the OpenAI Assistant.
I believe that having t
he ability to register custom functions would greatly enhance the flexibility and extensibility of the OpenAI Assistant.
 This feature would allow users to define their own functions and seamlessly integrate them into the assistant's convers
ational flow.
Specifically, I envision a method similar to register_function that would enable users to define custom fu
nctions in Python and register them with the OpenAI Assistant. These registered functions could then be invoked during t
he conversation, allowing for more dynamic and interactive interactions with the assistant.
I kindly request that the La
ngchain team consider adding this feature to the platform. It would empower users to create more tailored and specialize
d conversational experiences with the OpenAI Assistant.
Thank you for your attention to this feature request. I apprecia
te your dedication to continuously improving the Langchain platform and look forward to any updates or feedback regardin
g this request.
Best regards,
[Your Name]
```
---

     
 
all -  [ RAG, langchain app ](https://www.reddit.com/r/RagAI/comments/19c97bl/rag_langchain_app/) , 2024-01-23-0910
```
Can anybody suggest ai tools that can build a langchain & rag app?
```
---

     
 
all -  [ What framework to use to build a LLM chatbot which is enterprise scalable to multiple users ](https://www.reddit.com/r/ChatGPT_GoogleBard/comments/19bzk8f/what_framework_to_use_to_build_a_llm_chatbot/) , 2024-01-23-0910
```
Hey guys, what framework or tools do I use if I wanted to build a LLM chatbot which is enterprise scalable to multiple u
sers?

A framework/tool I am thinking of is Langchain. There won’t be any fine-tuning for my chatbot so I am not sure if
 I need to use Langchain.

Would there be a different suitable framework to use if I wanted to build for a small to mid 
sized enterprise compared to a large enterprise?

I am thinking of using AWS to host the LLM model. 

Any help would rea
lly be appreciated. Many thanks!
```
---

     
 
all -  [ What framework to use to build an open-sourced LLM chatbot which is enterprise scalable to multiple  ](https://www.reddit.com/r/MLQuestions/comments/19bzim1/what_framework_to_use_to_build_an_opensourced_llm/) , 2024-01-23-0910
```
Hey guys, what framework or tools do I use if I wanted to build an open-sourced LLM chatbot which is enterprise scalable
 to multiple users?

A framework/tool I am thinking of is Langchain. There won’t be any fine-tuning for my chatbot so I 
am not sure if I need to use Langchain.

Would there be a different suitable framework to use if I wanted to build for a
 small to mid sized enterprise compared to a large enterprise?

I am thinking of using AWS to host the LLM model. 

Any 
help would really be appreciated. Many thanks!
```
---

     
 
all -  [ Advice on Getting Started RAG and LLM using Langchain and TinyLlama ](https://www.reddit.com/r/ArtificialInteligence/comments/19bz6bo/advice_on_getting_started_rag_and_llm_using/) , 2024-01-23-0910
```
I am currently learning RAG and LLM and how RAG can help reduce hallucinations on LLM when generating responses.

I foll
owed this article [https://thebeep.substack.com/p/data-prepare-of-basic-retrieval-augmented](https://thebeep.substack.co
m/p/data-prepare-of-basic-retrieval-augmented) and found that useful. However, I would need some suggestions on how to m
ake an application on top of it. So that end users can use this application. 
```
---

     
 
all -  [ Is LLM 'temperature' setting similar to 'Guidance scale' from Stable Diffusion? ](https://www.reddit.com/r/LangChain/comments/19bz3o1/is_llm_temperature_setting_similar_to_guidance/) , 2024-01-23-0910
```
\*Guidance Scale\* Stable diffusion setting,  “prompt strength”

\> Guidance Scale: controls how similar the generated i
mage will be to the prompt. A higher guidance scale means the model will try to generate an image that follows the promp
t more strictly. A lower guidance scale means the model will have more creativity.

&#x200B;

&#x200B;
```
---

     
 
all -  [ Resume Feedback and Career Advice Needed! ](https://www.reddit.com/r/resumes/comments/19bx74j/resume_feedback_and_career_advice_needed/) , 2024-01-23-0910
```
Here is my resume, looking for feedback and career advice. Any suggestions on how to improve or opportunities I should e
xplore? Thanks in advance!

I want to switch my job; until now, I was applying at random places and did some cold emails
 with no response. Other than that, I received two offers from UK who saw one of my project on GitHub, emailed me, and o
ffered an interview. However, the interview is still pending, and they are taking time to respond. I also have another i
nterview opportunity for a frontend role in a crypto startup; the interview is on Wednesday next week. Let's hope for th
e best!

A bit about me: I come from a non-tech background, previously involved in sports (Played cricket at the nationa
l level). However, my love for computers and software led me to choose a career in tech. While I don't have a strong DSA
 & LeetCode profile, I am currently learning and improving in that area as well.

My Github: [https://github.com/ChetanX
pro](https://github.com/ChetanXpro)

Resume:  


[Resume](https://preview.redd.it/csza6nr2oqdc1.png?width=1058&format=pn
g&auto=webp&s=3c01c36634cdb1543754d86d159d7a9d0e395405)
```
---

     
 
all -  [ Is there a chat to help with the langchain API? ](https://www.reddit.com/r/LangChain/comments/19bqj57/is_there_a_chat_to_help_with_the_langchain_api/) , 2024-01-23-0910
```
Title, is chatGPT the best llm to help with the python API?

🙏
```
---

     
 
all -  [ A demonstration video of RAG feature ](https://www.reddit.com/r/huggingface/comments/19bpbjo/a_demonstration_video_of_rag_feature/) , 2024-01-23-0910
```
 

Currently, this project supports RAG functionality, allowing the creation of knowledge bases, uploading various types
 of documents for vectorization, and enabling the base model to answer questions based on the knowledge base. Achieving 
high precision with RAG functionality requires significant work and research. While the implementation of this project i
s still in its early stages, it serves as a sufficient entry-level research tool. Here is a demonstration video showcasi
ng its capabilities:  
[https://youtu.be/dyIFLISlskI](https://youtu.be/dyIFLISlskI)

&#x200B;

[ Knowledge Base Interfac
e ](https://preview.redd.it/09j18n8pkodc1.png?width=2560&format=png&auto=webp&s=3b40a0b9b9837fa52b67de938e69a3305a69bf7e
)

&#x200B;

[ Upload Docs to Knowledge Base ](https://preview.redd.it/s2he4upqkodc1.png?width=2560&format=png&auto=webp
&s=4ae3d496c89944f82e13f5c812f2cc243e6e7326)

&#x200B;

[ Docs Content View ](https://preview.redd.it/3ojg8oiukodc1.png?
width=2560&format=png&auto=webp&s=a640337695cfedb53849ce448a859dd25f5dec22)

&#x200B;

[ Foundation Model Chat Base on K
B ](https://preview.redd.it/niqcinewkodc1.png?width=2560&format=png&auto=webp&s=4756a32b0efd15966ca64fb399197a387243c3f1
)
```
---

     
 
all -  [ Langchain vs Llama Index ](https://www.reddit.com/r/LangChain/comments/19bnjnz/langchain_vs_llama_index/) , 2024-01-23-0910
```
Hey guys,

I am deciding to implement RAG pipeline into my code

between Langchain and Llama Index, what RAG capability 
yield better performance and what's the main different?

Thanks a lot guys!
```
---

     
 
all -  [ Integrating Azure AI search ](https://www.reddit.com/r/LangChain/comments/19bn28q/integrating_azure_ai_search/) , 2024-01-23-0910
```
Howdy. I have a project which initially made use of LlamaIndex and GithubRepositoryReader to locally persist a vector st
ore containing the contents of a github code repository that I will now be looking to instead integrate into Azure AI se
arch service.

Does anyone know of any resources they can point me to which demonstrates such a project (generating embe
ddings for a code repo, uploading the docs to azure ai search, q&a against said search service)

Thanks!
```
---

     
 
all -  [ Ensemble Retriever with ParentDoc ](https://www.reddit.com/r/LangChain/comments/19bjuov/ensemble_retriever_with_parentdoc/) , 2024-01-23-0910
```
I have tested two retriever methods, 1) Pinecone Hybrid Search and 2) ParentDocument Retriever.

Generally, the ParentDo
cument Retriever performs a lot better but there are instances where the Hybrid search finds interesting nuggets.

I wan
ted to know, if using the ensemble retriever, I can do a combination of BM25 and ParentDocument? Has anyone tried this?


Thanks
```
---

     
 
all -  [ GPT4AllEmbeddings modify model path ](https://www.reddit.com/r/LangChain/comments/19biswa/gpt4allembeddings_modify_model_path/) , 2024-01-23-0910
```
I'd like to modify the model path using GPT4AllEmbeddings and use a model I already downloading from the browser (the al
l-MiniLM-L6-v2-f16.gguf model, the same that GPT4AllEmbeddings downloads by default).

I need it to create RAG chatbot c
ompletely offline.

The langchain documentation chatbot suggests me to use:

>from langchain\_community.embeddings **imp
ort** GPT4AllEmbeddings  
model\_path = '/path/to/your/model.bin'  
gpt4all\_embd = GPT4AllEmbeddings(model=model\_path)


I tried it but it does not work. It completely ignore the model path.

Is there something I'm missing?
```
---

     
 
all -  [ LangChain Questions - Advanced Use Cases ](https://www.reddit.com/r/LangChain/comments/19bfisz/langchain_questions_advanced_use_cases/) , 2024-01-23-0910
```
first time long time. love the platform.

we have build custom tools and agents.

i am trying to extend our implementati
on with the following

\- custom meta-prompts - that are stored on the firm or individual level and could be used as par
t of a workflow

\- Custom meta-data storage - like a list of URLs. this would allow the user to edit this list, and the
n a custom agent (web scraper, etc) could reference it

\- multi-agents? our function calls can only do one thing at a t
ime (one scrape, etc). is there a way to run multiple, in parallel, and return together?

&#x200B;

thanks
```
---

     
 
all -  [ Question about hardware requirements for LangChain and vector DBs ](https://www.reddit.com/r/LangChain/comments/19bcztd/question_about_hardware_requirements_for/) , 2024-01-23-0910
```
Howdy. I am an experienced software engineer working on my first ever project using an LLM. My goal is to use it to repl
ace a rules engine for transaction categorization in an application I have. I will feed in the new transactions, list of
 categories, plus data on past categorized transactions, to produce the new output. All results will go through manual r
eview prior to being accepted, which is the current behavior with the existing rules engine anyway.

This will be deploy
ed to my home server which has a powerful CPU, lots of RAM, but a shit GPU. Because of this, my plan is to use a cloud L
LM like ChatGPT. However I want to run the Vector database (Cassandra, chroma, etc. haven't picked yet) on the server. I
 know the embeddings will be generated by the LLM and just stored in the Vector DB, so I don't need to worry about the h
ardware needs for that.

My question is around querying the Vector DB. Are there special hardware requirements (ie, GPU-
preferred operations) for running those queries? I'm not worried about operations that a CPU can handle well, only stuff
 that requires a beefier GPU.

Thanks in advance
```
---

     
 
all -  [ Resume Feedback and Career Advice Needed! ](https://www.reddit.com/r/developersIndia/comments/19ba933/resume_feedback_and_career_advice_needed/) , 2024-01-23-0910
```
Here is my  resume, looking for feedback and career advice. Any suggestions on how to improve or opportunities I should 
explore? Thanks in advance!    


 I want to switch my job; until now, I was applying at random places and did some cold
 emails with no response. Other than that, I received two offers from UK who saw one of my project on GitHub, emailed me
, and offered an interview. However, the interview is still pending, and they are taking time to respond. I also have an
other interview opportunity for a frontend role in a crypto startup; the interview is on Wednesday next week. Let's hope
 for the best!  


A bit about me: I come from a non-tech background, previously involved in sports (Played cricket at t
he national level). However, my love for computers and software led me to choose a career in tech. While I don't have a 
strong DSA & LeetCode profile, I am currently learning and improving in that area as well.

My Github: [https://github.c
om/ChetanXpro](https://github.com/ChetanXpro)  


Resume:

[Resume](https://preview.redd.it/ulxm6jrl2ldc1.png?width=1058
&format=png&auto=webp&s=60655279b2fd8c67f4f7332ea847a23835dddd72)
```
---

     
 
all -  [ Relation between LiteLLM and LangChain ](https://www.reddit.com/r/LangChain/comments/19b9fzw/relation_between_litellm_and_langchain/) , 2024-01-23-0910
```
Hello,

I am currently looking into using LLMs for a project and figured LiteLLM might be a good start to test out diffe
rent models. With a bit of research I saw that langchain is basically the number one library for doing this kind of thin
gs, becauso of RAG support etc.

What I do not quite understand is, what is the relation between these tools? Does LangC
hain use LiteLLM or vice versa? Is there even a link or are these just completely seperate tools? There is also autogen,
 which is basically LangChain with mutiple agents developed by microsoft if I understand it correctly.

What I found was
 the mention of LangChain in LiteLLMs docs: [https://docs.litellm.ai/docs/langchain/](https://docs.litellm.ai/docs/langc
hain/) where ChatLiteLLM is imported from LangChain, does that mean there is LiteLLM integrated into LangChain?

&#x200B
;

 I am quite confused here, would appreciate any input on this topic. Thanks!
```
---

     
 
all -  [ Özgeçmişime bakabilir misiniz? (Eleştirileriniz üzerine sıfırdan yaptım.) ](https://www.reddit.com/r/CodingTR/comments/19b8fbm/özgeçmişime_bakabilir_misiniz_eleştirileriniz/) , 2024-01-23-0910
```
Merhaba, ben daha önce de özgeçmişimi sizinle paylaşmıştım. Yararlı eleştirileriniz üzerine tamamen sıfırdan yeniden yap
tım. Bir çok eksiği bana göstermiş oldunuz. Şimdiki hali nasıl olmuş bakabilir misiniz? Ağustos ayında mezun oldum, yeni
 mezun sayılırım. Veri bilimi alanında kariyer hedefliyorum.

https://preview.redd.it/ysbhtfkdikdc1.jpg?width=1653&forma
t=pjpg&auto=webp&s=8ac110d126fb7930b0ef6284de05efabb947e7fd

https://preview.redd.it/w0y3sfkdikdc1.jpg?width=1653&format
=pjpg&auto=webp&s=28f0a21179543b9b4c46fda35ea1f4a9964dcc7d
```
---

     
 
all -  [ Multiple PDF's vs single large file? ](https://www.reddit.com/r/LangChain/comments/19b40f8/multiple_pdfs_vs_single_large_file/) , 2024-01-23-0910
```
Hi, I build a chat bot with langchain.js and one of the tools of the bot is using a  VectorDBQAChain connecred to a vect
or store that is basicaly one big txt file. The model I use is  gpt-3.5-turbo-0613 and the chunck size of the text split
ter is 1000. There are just a hundred rows of information. It works ok, but it takes too much time and sends a lot of em
bedings until it can answer a question correctly.

Now I am asked to create similar chat bot but working with a few thou
sand PDF's and I wonder if this is even possible? I saw there is DocumentLoader, but is it needs to send embedings of al
l the content until it can formulate an answer it is useless. The cost will be too high and the time it takes will be en
ourmous. Maybe I am missing something here?
```
---

     
 
all -  [ Is there any common loaders in langchain to load all types of documents?? ](https://www.reddit.com/r/LangChain/comments/19b2ivj/is_there_any_common_loaders_in_langchain_to_load/) , 2024-01-23-0910
```
I am into creating an interactive chatbot that can take inputs from multiple data sources like pdf, word file, text file
, excel files etc. I am using Pinecone retriever with Langchain wrapper on top of it. When I go for DirectoryLoader usin
g glob function, I’m unable to load other file types except PDF and convert it to vector embeddings. Need a way to load 
rest of the documents and process it further for embeddings.
```
---

     
 
all -  [ Introducing Langfuse - Open Source Observability, Analytics and AI Engineering for LLM apps ](https://www.reddit.com/r/LLMDevs/comments/19apbed/introducing_langfuse_open_source_observability/) , 2024-01-23-0910
```
Max, Marc and Clemens here, founders of **Langfuse** ([https://langfuse.com](https://langfuse.com)). We’re building OSS 
tooling to help developers iterate on LLMs in production.   
We came onto the scene with a **Show HN** back in August ([
https://news.ycombinator.com/item?id=37310070](https://news.ycombinator.com/item?id=37310070)). Back then we were still 
a rather simple solution for logging out traces. We had just started adding scrappy analytics through Looker Studio. 

*
*I wanted to take this opportunity to introduce us to the Reddit community.**

Since our first launch we’ve shipped: 

*
 Dashboards: custom charts on top of tremor.so which replaced looker
* SDKs 2.0: performance upgrades, fewer dependencie
s, more stable
* Sessions: group traces into sessions & replay user interactions
* Integrations: added integrations for 
OpenAI, Langchain, Flowise, Langflow, LiteLLM
* Easier self-hosting: automatic db migrations by pulling latest container

* Evals: model-based evals through e.g. Ragas \[1\] framework
* Exports: rich source data as .csv, JSON/L & access to y
our data via GET API
* Datasets: run tests on sets of inputs and expected outputs
* UI: improvements including hotkeys, 
tables, filtering, search

**Latest**

* Prompt Management: Host your prompts in Langfuse, get automatic versioning and 
keep your code tidy. Edit in UI/SDK and invoke in your code through `langfuse.get_prompt('prompt-slug')`

The repo is av
ailable under **MIT license** and we’re proud to support a vibrant community of self-hosting users (**one docker contain
er**) through GitHub and Discord. 

We’ll be around in the comments and look forward to hearing what you think. We take 
it to heart!

GitHub: [https://github.com/langfuse/langfuse/](https://github.com/langfuse/langfuse/)

Try a demo: [https
://langfuse.com/docs/demo](https://langfuse.com/docs/demo) -- **+ there is a generous free tier and the option to self-h
ost Langfuse.**

\[1\] [https://github.com/explodinggradients/ragas](https://github.com/explodinggradients/ragas) 
```
---

     
 
all -  [ How to achieve relevance question leading ](https://www.reddit.com/r/LangChain/comments/19an810/how_to_achieve_relevance_question_leading/) , 2024-01-23-0910
```
When a user asks a question, in what way can I achieve the display of similar questions. For example: the user asks for 
Bob's age? I will give 4 related questions: who is Bob, Bob's gender,.... But these questions are not random, they are g
iven based on my profile
```
---

     
 
all -  [ How to dockerise a Langchain app ](https://www.reddit.com/r/LangChain/comments/19amgmz/how_to_dockerise_a_langchain_app/) , 2024-01-23-0910
```
Hi everybody I was wondering how would it be like a typical Dockerfile for running a langchain pipeline. 
```
---

     
 
all -  [ Using Agent in langChain I want to abort in specific situations, how should I design it ](https://www.reddit.com/r/LangChain/comments/19ambyh/using_agent_in_langchain_i_want_to_abort_in/) , 2024-01-23-0910
```
I want to realize such a scenario:
Let's say I have a `name` field stored in my db, and when the user asks for bob, I ma
y have Bob, Boe... in the db. If there is no exact match for bob, I want the bot to guide the user: do you want to query
 Bob or boe?

What I understand is that it's actually how to make the bot stop to continue the query and output the resu
lt under certain circumstances during the execution, how should I implement this using langChain? Can I do it by `bind(s
top='xx')`?
```
---

     
 
MachineLearning -  [ New Data API for Astra [N] ](https://www.reddit.com/r/MachineLearning/comments/199uobn/new_data_api_for_astra_n/) , 2024-01-23-0910
```
I saw that DataStax/Astra DB [just released a new Data API to help with building production GenAI and RAG applications](
https://www.datastax.com/blog/general-availability-data-api-for-enhanced-developer-experience). This API makes the prove
n petabyte-scale of Apache Cassandra easy to use and available to any JavaScript, Python, or full-stack application deve
loper.

There will also be a joint webinar with LangChain available for registration here: [https://www.datastax.com/eve
nts/wikichat-build-a-real-time-rag-app-on-wikipedia-with-langchain-and-vercel](https://www.datastax.com/events/wikichat-
build-a-real-time-rag-app-on-wikipedia-with-langchain-and-vercel)
```
---

     
 
MachineLearning -  [ [D] While using function calling or tools on openai or langchain, does openai have access to the dat ](https://www.reddit.com/r/MachineLearning/comments/199t8be/d_while_using_function_calling_or_tools_on_openai/) , 2024-01-23-0910
```
I am working on a client project and I am using langchain's tools and agents. I want to know if the data is getting pass
ed to openai or is it just like that - Output of one function is being directly passed to the second function with the k
nowledge of openai.
```
---

     
 
MachineLearning -  [ [D] Code vs JSON output for LLM agents? Frameworks like LangChain rely on LLMs responding with JSON  ](https://www.reddit.com/r/MachineLearning/comments/197f416/d_code_vs_json_output_for_llm_agents_frameworks/) , 2024-01-23-0910
```
[CaP](https://arxiv.org/pdf/2209.07753.pdf), [Voyager](https://arxiv.org/pdf/2305.16291.pdf), [Octopus](https://arxiv.or
g/abs/2310.08588)

I work primarily with JSON based agents but code-as-policy agents seem to be extremely powerful. Here
 are some of the benefits and weaknesses I've seen

Pros of code

1. Less tool creation needed - The prebuilt math/file/
string/list manipulation abilities that come with code are enormous. In a JSON based agent, you would have to formally d
eclare each of these as a tool which you expose to the LLM and explain in your prompting, which is a lot of work and eat
s up a ton of the context window. 
2. Reduced number of transactions - The LLM can write scripts that invoke multiple to
ols and manipulate their results in ways that are difficult to do in a single transaction via JSON. For example, in one 
script, the model could search a DB 3 times, perform regex on the query results, convert them to integers, and add them 
up. Doing this in one step via JSON tool invocations is basically impossible. 
3. Less syntax errors - this might be tot
ally just vibe-based reasoning, but it really seems like LLMs have an easier time writing valid python than valid JSON, 
especially when you have lots of nested arguments in your methods.

Cons

1. Crazy risky - This is the obvious one. You 
have a machine executing random code. There are ways to mitigate this but still. I mean seriously we all learned not to 
use eval, so it is crazy to basically see research tending towards just running eval on the outputs of these models. 
2.
 Scripts with errors - Sometimes the model tries to get too fancy and writes complex programs that have bugs, resulting 
in many needed retries. 

Do any of you have thoughts or experience with these approaches in the wild? 

Is anybody awar
e of any experiments that compare these two approaches against each other? 

&#x200B;
```
---

     
 
MachineLearning -  [ [D] Are Custom LLM RAG apps going to become redundant? ](https://www.reddit.com/r/MachineLearning/comments/1929n4f/d_are_custom_llm_rag_apps_going_to_become/) , 2024-01-23-0910
```
Loks like Copilot Studio is being rolled out (https://www.microsoft.com/en-us/microsoft-copilot/microsoft-copilot-studio
) with an impressive looking no code/out of the box RAG solution.

There is a phenomenal amount of development and activ
ity in the Open Source RAG world (e.g Langchain, Llamaindex, etc), which I am a great supporter of FYI.

However, what s
eems strange is that this no code out of the box solution (Copilot Studio - just as an example of one) seems overwhelmin
gly to be the better option if you wanted to build a RAG app i.e If you compare the cost to build and productionise a cu
stom RAG app vs the cost of using Copilot Studio, it's almost an order of magnitude lower (no matter how you cut it with
 the developer time and duration). 

My question is, it seems to me we are moving towards a situation where enterprise s
olutions will make custom RAG apps redundant (not in all cases of course, but most cases), however there seems to be ver
y little discussion of this relative to the activity in the open source community. Do people agree this is a likely scen
ario? 

Obviously there will be exceptions…but on most use cases I don’t see how you can compete with an instant/minimal
 setup, low cost, highly scalable RAG solution.
```
---

     
 
MachineLearning -  [ [P] An open-source project for deploying local models ](https://www.reddit.com/r/MachineLearning/comments/18zkm5m/p_an_opensource_project_for_deploying_local_models/) , 2024-01-23-0910
```
 Introducing a new LLM WebUI project that supports various local model loading and provides streaming output for cutting
-edge online multimodal models GPT-4-Vision and Gemini-Pro-Vision. Completely free and open source, it serves as a valua
ble research tool for exploring diverse models. The project is actively under development with continuous updates:  
[ht
tps://github.com/smalltong02/keras-llm-robot](https://github.com/smalltong02/keras-llm-robot)

&#x200B;

[WebUI](https:/
/preview.redd.it/f95jievpepac1.png?width=2560&format=png&auto=webp&s=1f2908b484ededc78591719ef87efdac2f9497ba)

&#x200B;


[Configuration](https://preview.redd.it/owaj5s1repac1.png?width=2560&format=png&auto=webp&s=f837b1ef67cb8e4ccaee4ec602
a61859f53db100)

&#x200B;

[Tools & Agent](https://preview.redd.it/jrot8w9sepac1.png?width=2560&format=png&auto=webp&s=7
1e224f08620941146cd437a99bcb55d02930a9e)
```
---

     
 
MachineLearning -  [ [Project] Temporal Augmented Retrieval (TAR) - Dynamic RAG ](https://www.reddit.com/r/MachineLearning/comments/18uddmj/project_temporal_augmented_retrieval_tar_dynamic/) , 2024-01-23-0910
```
From a corpus of text, how can you detect emerging topics and their evolution through time?

Introducing Temporal Augmen
ted Retrieval (TAR). (built in the context of buildspace n&w s4)

TAR is an open-source advanced RAG approach that aims 
to factor in the dynamic and temporal aspects of textual data when performing retrieval.

It allows us to understand the
 evolution of discussed topics over time.

The idea behind this project is to open the debate regarding the current limi
tations of RAG methods

This first approach has been built without using RAG frameworks (like Jerry Liu’s langchain) and
 focuses on financial tweets 

Relevant links:

Medium: [https://medium.com/@adam-rida/temporal-augmented-retrieval-tar-
dynamic-rag-ad737506dfcc](https://medium.com/@adam-rida/temporal-augmented-retrieval-tar-dynamic-rag-ad737506dfcc)

Gith
ub:[https://github.com/adrida/Temporal\_RAG](https://github.com/adrida/Temporal_RAG)

Hugging Face Benchmark: [https://h
uggingface.co/spaces/Adr740/Temporal-RAG-Benchmark](https://huggingface.co/spaces/Adr740/Temporal-RAG-Benchmark)

My web
site: [adrida.github.io](https://adrida.github.io)

&#x200B;

https://preview.redd.it/lj7wkhk70f9c1.png?width=960&format
=png&auto=webp&s=fc79c5034351a1711e1ec051919a5c4d2edbc333
```
---

     
 
MachineLearning -  [ [R][P] Autogen + Langchain Tools + Local LLM doesn't work. ](https://www.reddit.com/r/MachineLearning/comments/18tex1j/rp_autogen_langchain_tools_local_llm_doesnt_work/) , 2024-01-23-0910
```
Hey folks, 

So I'm playing around with the agent framework Autogen and I'm trying to create agents by providing it cust
om tools to use. These custom tools are defined in the langchain framework. Furthermore, I am using open source LLM mode
ls like Mistral, LLAMA, Mixtral etc.

In my experience, I have been unable to get the Autogen+LocalLLM framework to iden
tify the right tools to use given the prompt. However it does a fantastic job with the GPT model. 

Please note that my 
goal is for the agent to mandatorily use the tools provided and not come up with its own code. And the agent should figu
re out the right tool to use. 

I have been very explicit with my prompting, despite which I am unable to get this to wo
rk.

Any thoughts and suggestions? Please let me know ! Please share your experiences as well. Cheers !
```
---

     
 
MachineLearning -  [ [P] Seeking Advice for Building a School Handbook Chatbot Using OpenAI and Vector Databases ](https://www.reddit.com/r/MachineLearning/comments/18rndcp/p_seeking_advice_for_building_a_school_handbook/) , 2024-01-23-0910
```
Hello everyone,

I'm embarking on a project to create a chatbot for my school's handbook, aiming to make it a resource f
or students to easily access information. As someone relatively new to AI, I'm seeking guidance on implementing this.

M
y current plan is to use OpenAI as the primary language learning model, focusing on affordability. I am considering inte
grating RAG (Retrieval-Augmented Generation) and LangChain for enhanced functionality. However, I'm quite perplexed abou
t choosing an appropriate vector database, as many options appear costly. The goal is to keep this system live and acces
sible for student usage without breaking the bank.

I'm also looking into open-source embedding models to pair with the 
vector database. Pinecone has caught my attention, but its pricing seems steep for our budget.

Does anyone have recomme
ndations or tips on affordable yet effective tools and strategies for this project? Any insights on vector databases sui
table for educational use, or ways to optimize cost without compromising quality, would be greatly appreciated.

Thank y
ou in advance for your help!

(I typed out my problem and had gpt4 fix up the format and wording dont bash me)
```
---

     
 
deeplearning -  [ [D] Unleashing the Power of Langchain with Wandb: Revolutionizing Topic Modeling and Evaluation ](https://www.reddit.com/r/deeplearning/comments/191mm83/d_unleashing_the_power_of_langchain_with_wandb/) , 2024-01-23-0910
```
Complementing Langchain’s prowess, Wandb emerges as a powerhouse meticulously designed for developers leveraging LLM tec
hnology. As an evaluation framework and production monitoring platform, Wandb stands out for its tailored approach. Its 
arsenal comprises real-time monitoring, granular analytics, and streamlined evaluation processes, laying the groundwork 
for elevated performance and reliability in AI applications.

&#x200B;

Link: [https://medium.com/ai-advances/unleashing
-the-power-of-langchain-with-wandb-revolutionizing-topic-modeling-and-evaluation-75af5cf51b15](https://medium.com/ai-adv
ances/unleashing-the-power-of-langchain-with-wandb-revolutionizing-topic-modeling-and-evaluation-75af5cf51b15) 
```
---

     
