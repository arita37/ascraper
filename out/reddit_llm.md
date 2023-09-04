 
all -  [ Running several Lora models ](https://www.reddit.com/r/LangChain/comments/169cgv6/running_several_lora_models/) , 2023-09-04-0909
```
I am using LLAMA2 13B and I have several (ie 4) different LORA finetunes. I want to run all of them on the same GPU. Wha
t’s the best library for doing this?
```
---

     
 
all -  [ Branching out from OpenAI question ](https://www.reddit.com/r/LLMDevs/comments/1690hyk/branching_out_from_openai_question/) , 2023-09-04-0909
```
Hi all, so I built a little Linux command line-based chatbot that also has a number of features such as the ability to p
ipe text into it and then inject a prompt, things like that - I haven't open sourced it yet but I intend to...

The only
 problem I have is that, though the tool allows for on the fly switching of OpenAI models, It doesn't use other LLMs.

T
he question I have for you guys is, rather than building custom connectors for different models, is there a maintained l
ibrary or component I can leverage to be able to easily integrate other LLMs?

Or, am I overly concerned about the varia
tion of different models interfaces?

I considered langchain but it's a little heavy.. unless I didn't consider it thoro
ughly enough.

Streaming is exceedingly important to me as well.
```
---

     
 
all -  [ I want to make an LLM on my YouTube transcripts, and I am not sure how to get it done. ](https://www.reddit.com/r/LangChain/comments/168xubo/i_want_to_make_an_llm_on_my_youtube_transcripts/) , 2023-09-04-0909
```
Hi folks, I am new to this, so I am still learning.

However, I want to create an LLM trained on the transcripts of my p
ast YouTube videos. When I want to create a new video, I want to be able to pass in documents ( using Langchain) and tex
t for chatgpt to help me generate videos. I also want to be able to use the LLM of my YouTube transcript so that it gene
rates a script in my writing size.   


I am not sure if Langchain would be the best way to execute this. How would I ar
chitect this?
```
---

     
 
all -  [ 3rd Year CS Student - Resume Review please ](https://www.reddit.com/r/resumes/comments/168x4pf/3rd_year_cs_student_resume_review_please/) , 2023-09-04-0909
```
&#x200B;

https://preview.redd.it/nsvmpqi3m1mb1.jpg?width=1239&format=pjpg&auto=webp&s=9cdddc7733cf5bc54242b11a55fa3beaf
6124815
```
---

     
 
all -  [ Free Tutorial - LangChain 101 pour les Débutants (OpenAI / ChatGPT / LLMOps) ](https://idownloadcoupon.com/udemy/870/) , 2023-09-04-0909
```

```
---

     
 
all -  [ Error with agent syntax. ](https://www.reddit.com/r/LangChain/comments/168szss/error_with_agent_syntax/) , 2023-09-04-0909
```
My agent works fine when I declare the tools like this:

&#x200B;

`def get_current_tasks() -> str:`

`'''Useful when lo
oking up a client's current tasks'''`

`with SessionLocal() as db:`

`mss = MindStateService(user_id=1, db=db)`

`return
 mss.get_current_tasks()`

`tools=['get_current_tasks]`

&#x200B;

But if I create a single of MindStateService and try 
to do it this way:

`Tool(`

`name='get_current_tasks',`

   `func=m_s_s.get_current_tasks,`

`description='useful for w
hen you need to look up a client's current tasks.',`

`)`

It will run the function, but give me an error:  Too many arg
uments to single-input tool get_grateful_for. Args: [] 

This must be because it doesn't have access to my object. I've 
seen other people do something similar with this syntax, and I would prefer to use it since I'm making my agent part of 
a class. But I cannot get it to work. Is there any way I can get a list of functions belonging to a custom object to wor
k as agent functions?
```
---

     
 
all -  [ Crawl websites and use them with Langchain ](https://www.reddit.com/r/LangChain/comments/168sgfi/crawl_websites_and_use_them_with_langchain/) , 2023-09-04-0909
```
What is the best way to crawl websites and answer questions from them using Langchain framework? Are there any prebuilt 
options available? Or doing something like automatically download and convert the page to PDF, index it and then run cha
ins/prompts for Q&A? Looking for something scalable as the requirement is to answer from quiet a bit of links. Thanks.
```
---

     
 
all -  [ Merging GPT-4 and PDF-based Retrieval System ](https://www.reddit.com/r/ChatGPTPro/comments/168sgbf/merging_gpt4_and_pdfbased_retrieval_system/) , 2023-09-04-0909
```
Hey Reddit fam,

I'm knee-deep in a research project that's focused on the capabilities of ChatGPT (GPT-4.0, to be speci
fic) in passing the CISA exam. My initial plan was to run a side-by-side analysis comparing the stock GPT-4.0 model with
 a version specially trained on additional data.

I've cobbled together a Python script using various code snippets I fo
und online, which lets me train the model using PDF documents. The idea was to end up with a supercharged ChatGPT that c
ombines its original abilities with the insights from my training material.

However, what I've inadvertently ended up w
ith seems to be a retrieval-based system. It utilizes GPT-4 for natural language generation and a collection of document
s as a database for information retrieval. The catch is, it seems to only answer queries that are directly related to th
e training documents.

I've hit a roadblock and can't seem to find a solid solution to make it work as intended. Anyone 
out there who's ventured into something similar or has any tips on how to pull this off?

Appreciate your help in advanc
e!

    import os
    from langchain.document_loaders import PyMuPDFLoader
    from langchain.text_splitter import Recur
siveCharacterTextSplitter
    from langchain.vectorstores import Chroma
    from langchain.embeddings import OpenAIEmbed
dings
    from langchain.chat_models import ChatOpenAI
    from langchain.chains import RetrievalQA
    
    os.environ[
'OPENAI_API_KEY'] = 'KEY'
    
    persist_directory = '.\storage'
    pdf_path =  '.\docs\CISA _Review_Manual_27th_edit
ion.pdf'
    
    loader = PyMuPDFLoader(pdf_path)
    documents = loader.load()
    
    text_splitter = RecursiveChara
cterTextSplitter(chunk_size=512, chunk_overlap=10)
    texts = text_splitter.split_documents(documents)
    
    embeddi
ngs = OpenAIEmbeddings()
    vectordb = Chroma.from_documents(documents=texts, embedding=embeddings, persist_directory=p
ersist_directory)
    
    vectordb.persist()
    
    retriever = vectordb.as_retriever(search_kwargs={'k': 3})
    llm
 = ChatOpenAI(model_name='gpt-4')
    
    qa = RetrievalQA.from_chain_type(llm=llm, chain_type='stuff', retriever=retri
ever)
    
    while True:
        user_input = input('Entere a query: ')
        if user_input == 'exit':
            b
reak
        
        query = f'###Prompt {user_input}'
        try:
            llm_reponse = qa(query)
            pri
nt(llm_reponse['result'])
        except Exception as err:
            print('Exception occurred. Please try again.', st
r(err))

&#x200B;
```
---

     
 
all -  [ Merging GPT-4 and PDF-based Retrieval System ](https://www.reddit.com/r/OpenAI/comments/168sft4/merging_gpt4_and_pdfbased_retrieval_system/) , 2023-09-04-0909
```
Hey Reddit fam,

I'm knee-deep in a research project that's focused on the capabilities of ChatGPT (GPT-4.0, to be speci
fic) in passing the CISA exam. My initial plan was to run a side-by-side analysis comparing the stock GPT-4.0 model with
 a version specially trained on additional data.

I've cobbled together a Python script using various code snippets I fo
und online, which lets me train the model using PDF documents. The idea was to end up with a supercharged ChatGPT that c
ombines its original abilities with the insights from my training material.

However, what I've inadvertently ended up w
ith seems to be a retrieval-based system. It utilizes GPT-4 for natural language generation and a collection of document
s as a database for information retrieval. The catch is, it seems to only answer queries that are directly related to th
e training documents.

I've hit a roadblock and can't seem to find a solid solution to make it work as intended. Anyone 
out there who's ventured into something similar or has any tips on how to pull this off?

Appreciate your help in advanc
e!

&#x200B;

    import os
    from langchain.document_loaders import PyMuPDFLoader
    from langchain.text_splitter im
port RecursiveCharacterTextSplitter
    from langchain.vectorstores import Chroma
    from langchain.embeddings import O
penAIEmbeddings
    from langchain.chat_models import ChatOpenAI
    from langchain.chains import RetrievalQA
    
    o
s.environ['OPENAI_API_KEY'] = 'Key'
    
    persist_directory = '.\storage'
    pdf_path =  '.\docs\CISA _Review_Manual
_27th_edition.pdf'
    
    loader = PyMuPDFLoader(pdf_path)
    documents = loader.load()
    
    text_splitter = Recu
rsiveCharacterTextSplitter(chunk_size=512, chunk_overlap=10)
    texts = text_splitter.split_documents(documents)
    
 
   embeddings = OpenAIEmbeddings()
    vectordb = Chroma.from_documents(documents=texts, embedding=embeddings, persist_d
irectory=persist_directory)
    
    vectordb.persist()
    
    retriever = vectordb.as_retriever(search_kwargs={'k': 3
})
    llm = ChatOpenAI(model_name='gpt-4')
    
    qa = RetrievalQA.from_chain_type(llm=llm, chain_type='stuff', retri
ever=retriever)
    
    while True:
        user_input = input('Entere a query: ')
        if user_input == 'exit':
   
         break
        
        query = f'###Prompt {user_input}'
        try:
            llm_reponse = qa(query)
     
       print(llm_reponse['result'])
        except Exception as err:
            print('Exception occurred. Please try a
gain.', str(err))
```
---

     
 
all -  [ ChatGPT Plugins - How to find URL? ](https://www.reddit.com/r/LangChain/comments/168s47r/chatgpt_plugins_how_to_find_url/) , 2023-09-04-0909
```
According to the Documentation:

[https://python.langchain.com/docs/integrations/tools/chatgpt\_plugins](https://python.
langchain.com/docs/integrations/tools/chatgpt_plugins)

You can simply add existing (non-authorized) Plugins like Klarna
 as a tool to the LLM:

&#x200B;

 `tool = AIPluginTool.from_plugin_url('https://www.klarna.com/.well-known/ai-plugin.js
on')` 

I want to try this out with 'web\_requests', but I struggle to find the URL for it.

Is there some way to quickl
y find out the URL needed to use Plugins as tools in langchain?
```
---

     
 
all -  [ Langchain+local LLM+Javascript? ](https://www.reddit.com/r/LangChain/comments/168qcvq/langchainlocal_llmjavascript/) , 2023-09-04-0909
```
Hi. Can I hook langchain up to my local LLM? I´ve seen some videos of people doing it with python and something called p
ipelines, but no info on Javascript. Can it be done with javascript? 
```
---

     
 
all -  [ Accessing high-quality curated vector embedding knowledgebases ](https://www.reddit.com/r/LangChain/comments/168pkqs/accessing_highquality_curated_vector_embedding/) , 2023-09-04-0909
```
I recently asked a question here about the usefulness for developers to access a repository of curated high-quality know
ledge bases from experts across domains, to be able to plug in to any LLM (via vector embeddings) with an API call.

Got
 some good responses and decided to build it out! Thanks to those shared their feedback. A bunch of things to think thro
ugh, but I think it's a good problem to solve.

&#x200B;

* Currently, developers need to play the role of a subject-mat
ter-expert to learn, curate & test the right content to create a knowledgebase.
* There is no destination for developers
 to access production-ready, high-quality knowledgebases from experts across a variety of topics in the form of vector e
mbeddings.

https://preview.redd.it/quq5wyuoizlb1.jpg?width=2134&format=pjpg&auto=webp&s=83fbd301ea8ce2eefe46bf5816a49eb
d9ee5c547

* Lore brings in experts across various domains to host knowledgebases.
* We take care of converting knowledg
ebases into vector embeddings and optimizing retrieval so that experts & developers don’t need to maintain pipelines for
 cleaning, embedding, hosting, maintaining & retrieving data.

https://preview.redd.it/uf4fejxuizlb1.jpg?width=1926&form
at=pjpg&auto=webp&s=16d45a79976db95d702f2cccc780c2d4b6f27509

Check out [https://lore.market](https://lore.market), join
 the waitlist and stay connected :)
```
---

     
 
all -  [ To query specific document from chromadb with llama2 ](https://www.reddit.com/r/LangChain/comments/168mqwm/to_query_specific_document_from_chromadb_with/) , 2023-09-04-0909
```
I am planning to index multiple document and later if a question comes against a specific document i want llama2 to answ
er from that specific document only. Also i wanted avoid indexing again if the document is already there. How can I do t
his with chroma client and langchain.
```
---

     
 
all -  [ Chatbot help ](https://www.reddit.com/r/Python/comments/168l850/chatbot_help/) , 2023-09-04-0909
```
Hi guys, My intent is to build a chatbot for an existing Sustainability dashboard. The data behind the dashboard resides
 on a snowflake sql server.

No I want to use to build a flowbased chatbot so that user can ask natural language questio
ns and the bot can understand the backend tabular data and respond accordingly. The data is tabular with text and number
s. So I guess Embedding will not make much sense here right?

I thought may we can use langchain and llm to go ve sql qu
eries and then spit out the result for the user. 

Question cam be like what  is the ESG score of company Mastercard? 
S
o the chatbot should search for this company  in the database and them give the scores.

How can it be done? I tried goo
gle dialog flow but it’s hard to connect with my sql data. Also, I can pull the data in csv form as well.
```
---

     
 
all -  [ I built a Discord bot that takes files, websites, to teach GPT, or chat, or DALL E 2 ](https://www.reddit.com/r/ChatGPTCoding/comments/168iavi/i_built_a_discord_bot_that_takes_files_websites/) , 2023-09-04-0909
```
Its pretty great! I worked on it most of this year. 4,500 lines of python code. And it really uses LLM Predictor, Simple
GPTVectorIndex, Langchain, OpenChatAI - etc, to embed custom data into AI instance.

It operates on secure Google Cloud 
compute instance. Very powerful, have used the core of this bot for a very long time, and tried to make it something pub
lic and user friendly.

Currently it is Beta, so only free edition with some limitations... But it allows for group cola
b with custom data or group training AI. We tested this for many months on a model to make it esoteric, it has been grea
t success.

This is a toolkit for users to train their own ChatGPT models, so you need to have OpenAI API to use this bo
t. 

It has three primary modes: !learn, !chat, !image. !learn is shown in the video below. !chat sets it as a chatbot, 
and you can set max tokens, temperature, roles for users, allow users to set prompts, or set the amount of context to se
nd etc. !image uses DALL E 2 with regenerate and variate functions.

In our use case, we used multiple bots to test the 
features that currently developed into this bot. We would set all server members to have system role in the AI chat, and
 set prompts to be esoteric, and we also custom trained it on open source data regarding numerology, totems, earth medic
ine, astrology, etc. Over time it became so great we did not need prompting anymore, and the model is impeccable with pe
rforming divination, astrology, or numerology readings.

To see info on terms, privacy, security, to try the bot or invi
te the bot, see this server:

[https://top.gg/servers/907301373387898950](https://top.gg/servers/907301373387898950)

&#
x200B;

https://reddit.com/link/168iavi/video/n2j4gsxtmxlb1/player
```
---

     
 
all -  [ Call for participation in an open source langchain application project ](https://www.reddit.com/r/LangChain/comments/168gd02/call_for_participation_in_an_open_source/) , 2023-09-04-0909
```
Fellow LangChain enthusiasts. We are looking forward to see some of you beautiful folks participate in our open source p
roject. It's called GPT-Synthesizer and it uses LangChain and GPT3.5 for software design and code generation. We would l
ove to have more people contribute to this project:

[https://github.com/RoboCoachTechnologies/GPT-Synthesizer](https://
github.com/RoboCoachTechnologies/GPT-Synthesizer)

Another way that you can help us, is to create a video of you using t
his project to create your software. If you send us such videos we will gladly put it on our github and credit your cont
ribution on our page. 
```
---

     
 
all -  [ Journey to Build the Ultimate ChatGPT Has Hit a Roadblock – Could Use Your Expertise! ](https://www.reddit.com/r/ChatGPT/comments/168fhgg/journey_to_build_the_ultimate_chatgpt_has_hit_a/) , 2023-09-04-0909
```
Hey Reddit fam,

I'm knee-deep in a research project that's focused on the capabilities of ChatGPT (GPT-4.0, to be speci
fic) in passing the CISA exam. My initial plan was to run a side-by-side analysis comparing the stock GPT-4.0 model with
 a version specially trained on additional data.

I've cobbled together a Python script using various code snippets I fo
und online, which lets me train the model using PDF documents. The idea was to end up with a supercharged ChatGPT that c
ombines its original abilities with the insights from my training material.

However, what I've inadvertently ended up w
ith seems to be a retrieval-based system. It utilizes GPT-4 for natural language generation and a collection of document
s as a database for information retrieval. The catch is, it seems to only answer queries that are directly related to th
e training documents.

I've hit a roadblock and can't seem to find a solid solution to make it work as intended. Anyone 
out there who's ventured into something similar or has any tips on how to pull this off?

Appreciate your help in advanc
e!

&#x200B;

    import os
    from langchain.document_loaders import PyMuPDFLoader
    from langchain.text_splitter im
port RecursiveCharacterTextSplitter
    from langchain.vectorstores import Chroma
    from langchain.embeddings import O
penAIEmbeddings
    from langchain.chat_models import ChatOpenAI
    from langchain.chains import RetrievalQA
    
    o
s.environ['OPENAI_API_KEY'] = 'APIKEY'
    
    persist_directory = '.\storage'
    pdf_path =  '.\docs\CISA _Review_Man
ual_27th_edition.pdf'
    
    loader = PyMuPDFLoader(pdf_path)
    documents = loader.load()
    
    text_splitter = R
ecursiveCharacterTextSplitter(chunk_size=512, chunk_overlap=10)
    texts = text_splitter.split_documents(documents)
   
 
    embeddings = OpenAIEmbeddings()
    vectordb = Chroma.from_documents(documents=texts, embedding=embeddings, persis
t_directory=persist_directory)
    
    vectordb.persist()
    
    retriever = vectordb.as_retriever(search_kwargs={'k'
: 3})
    llm = ChatOpenAI(model_name='gpt-4')
    
    qa = RetrievalQA.from_chain_type(llm=llm, chain_type='stuff', re
triever=retriever)
    
    while True:
        user_input = input('Entere a query: ')
        if user_input == 'exit':

            break
        
        query = f'###Prompt {user_input}'
        try:
            llm_reponse = qa(query)
  
          print(llm_reponse['result'])
        except Exception as err:
            print('Exception occurred. Please tr
y again.', str(err))

&#x200B;
```
---

     
 
all -  [ AI Tools ](https://www.reddit.com/r/u_Best_Ai_Tools_Finder/comments/168dcan/ai_tools/) , 2023-09-04-0909
```
Here are 25 ChatGPT Plugins that'll skyrocket your efficiency in minutes:

1. Slack: Querying Slack

2. Zapier: Interact
 with 5000+ apps like Google Sheets, and Docs.

3. Best AI Tools Finder: Find any AI tool for anything imaginable.

4. K
larna Shopping: Search and compare prices from 1000s of online shops.

5. Vogue: Search through vogue articles.

6. TODO
 plugin: Manage a TO-DO list in ChatGPT.

7. Lowes: Find the right tools for all of your home building needs.

8. Speech
ki: Just simply ask ChatGPT to turn your text into audio.

9. FigGPT: Design using Figma in ChatGPT.

10. Noteable: Crea
te notebooks in Python, SQL, and Markdown to explore and visualize data.

11. KAYAK: Plan & book your next trip in ChatG
PT.

12. LangChain Docs: Up to date info for the LangChain Python library.

13. Expedia: Bring your trip plans to life i
n one place.

14. Crypto Prices: Get the price on any crypto.

15. NBA: Up-to-date NBA standings & Stats.

16. Qdrant: P
lugin to search through Qdrants documentation.

17. Open Table: Search and get booking at restaurants anywhere, anytime.


18. Zilliz Plugin: Search through your documentation and talk to it.

19. Wolfram: Access computation, math, curated k
nowledge and real time data

20. Pricerunner: Get the perfect shopping suggestions.

21. Instacart: Order groceries from
 your near by store.

22. Send Email: Send the perfect emails through ChatGPT.

23. FiscalNote: Access real time data se
ts for legal and political purpose.

24. DAN: Change ChatGPT’s personality.

25. DesignerGPT: Generate a website within 
ChatGPT.
```
---

     
 
all -  [ How to deploy/host custom LLM app for production? ](https://www.reddit.com/r/LocalLLaMA/comments/1689jfx/how_to_deployhost_custom_llm_app_for_production/) , 2023-09-04-0909
```
So let's say we have created app using Langchain and Pinecone (for embeddings). App uses AutoTokenizer, AutoModelForCaus
alLM, ConversationalRetrievalChain for basic QA on documents and X model from HuggingFace.   


For now I ran this in Go
ogle Colab, but what if I want to make this accessable to public? How do I host this and where? I know there is Azure th
ing, but that's for using OpenAi stuff. I couldn't find any good guide or anything like that for hosting this LLM apps f
or public, so not locally.
```
---

     
 
all -  [ I am having trouble with large dataset. ](https://www.reddit.com/r/LangChain/comments/1688bek/i_am_having_trouble_with_large_dataset/) , 2023-09-04-0909
```
I am using langchain framework 'load_qa_chain' to ask questions from a huge dataset. But it is unable to answer some que
stion which require checking on the whole dataset (for eg: If the dataset is the conversation between two people for yea
rs, query: List all the critical problems faced by the person in his lifetime? , It is able to give some of it but missi
ng some important data). How can I resolve this?
```
---

     
 
all -  [ How should I go about getting my AI to use tools correctly (and consistently)? ](https://www.reddit.com/r/LocalLLaMA/comments/1687l5p/how_should_i_go_about_getting_my_ai_to_use_tools/) , 2023-09-04-0909
```
My goal is to get an open source AI to use tools, for example searching for information online.

Currently what I'm doin
g is giving it a list of tool names in its prompt, that looks something like this '<SEARCH(Input)>' along with explanati
ons of what they do and examples of how they work, then asking it to append it to its message with 'Input' replaced, the
n I have a script match those and perform actions. This works about half the time, the other half it just fails miserabl
y (making up tool names, using incorrect formats, etc).

I've been looking for ways to improve this for awhile, so far t
he only other implementation of this I've seen is langchain's tools system. After looking through its code, it seems lik
e it works similarly to my own code, except instead of just asking the AI to append something to its regular message, th
e AI has to always use a specific message format that includes a section for tools, like this:

>Thought: Do I need to u
se a tool? Yes  
>  
>Action: the action to take, should be one of \[{tool\_names}\]  
>  
>Action Input: the input to t
he action  
>  
>Observation: the result of the action

...Of course, I have no idea how langchain gets an AI to follow 
that format, because mine absolutely would not no matter what kind of prompt I gave it.

Should I try to use something l
ike LMQL or Guidance to force it to use a langchain-style output format, or is there another way to make it 'understand'
 how to use tools better? I've found [this article](https://www.promptingguide.ai/techniques/art) which seems to be exac
tly what I'm trying to do, but I have no idea how to implement it...

I've also considered that my particular model coul
d just not be that good, but I'd like to give it a shot using prompt/output formatting anyway. I've considered trying to
 make a lora of some kind to teach it my particular tools setup, would that be a good idea? Though I'd have to research 
it more since I have no idea how those really work, and I'm not even sure if I have the hardware to do that anyway...

H
as anyone else gotten an open source model to use tools, if so, how?
```
---

     
 
all -  [ help ](https://www.reddit.com/r/LangChain/comments/1687dxt/help/) , 2023-09-04-0909
```
 how do we handle larger context length while finetuning the model ?  
suppose i have the dataset with question, answer 
pair.  
My problem here is question exceed the context length so that answer doesnot fit. which has lead the model doesn
't generate the answer. How do we actually solve this issue? 
```
---

     
 
all -  [ How Code Interpreter Orchestration is Designed? ](https://www.reddit.com/r/ChatGPT/comments/1684itm/how_code_interpreter_orchestration_is_designed/) , 2023-09-04-0909
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

     
 
all -  [ How to deal with missing question mark? ](https://www.reddit.com/r/LangChain/comments/167vauj/how_to_deal_with_missing_question_mark/) , 2023-09-04-0909
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

     
 
all -  [ I have some defined classes and a design system. What is the best approach to build a chat bot that  ](https://www.reddit.com/r/LangChain/comments/167sfdx/i_have_some_defined_classes_and_a_design_system/) , 2023-09-04-0909
```
 How can I create a chatbot that generates HTML components using predefined classes from a design system, and what is th
e best approach to manage this without utilizing a vector store? 
```
---

     
 
all -  [ Conversationalretrievalchains pigeon holes on chat history + history overwhelms context window ](https://www.reddit.com/r/LangChain/comments/167ndda/conversationalretrievalchains_pigeon_holes_on/) , 2023-09-04-0909
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

     
 
all -  [ The talks from SeattleJS Conf 2023 have been posted online (free) ](https://www.reddit.com/r/webdev/comments/167kfyv/the_talks_from_seattlejs_conf_2023_have_been/) , 2023-09-04-0909
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

     
 
all -  [ Langchain in Javascript in a .NET project ](https://www.reddit.com/r/LangChain/comments/167g2mi/langchain_in_javascript_in_a_net_project/) , 2023-09-04-0909
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

     
 
all -  [ Stanford DSPy - Better than LangChain? ](https://www.reddit.com/r/LangChain/comments/167dzcb/stanford_dspy_better_than_langchain/) , 2023-09-04-0909
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

     
 
all -  [ I'm trying to stream recorded audio from the browser to my LLM powered backend. ](https://www.reddit.com/r/LangChain/comments/167bjky/im_trying_to_stream_recorded_audio_from_the/) , 2023-09-04-0909
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

     
 
all -  [ How do I choose an embeddings model? ](https://www.reddit.com/r/LangChain/comments/1678qrt/how_do_i_choose_an_embeddings_model/) , 2023-09-04-0909
```
Can I use OpenAI embeddings in Chroma with a HuggingFace or GPT4ALL model and vice versa?

Is one type of embedding bett
er than another for similarity search accuracy?

Thanks in advance for you reply!
```
---

     
 
all -  [ Why does MarkdownHeaderTextSplitter remove the headers and put them into the metadata if vector stor ](https://www.reddit.com/r/LangChain/comments/16785z2/why_does_markdownheadertextsplitter_remove_the/) , 2023-09-04-0909
```
I'm a bit confused by why [MarkdownHeaderTextSplitter](https://python.langchain.com/docs/modules/data_connection/documen
t_transformers/text_splitters/markdown_header_metadata) removes the markdown headers and puts them into metadata instead
. If we can only filter on metadata in vector stores and not search on metadata, wouldn't this make the markdown heading
 essentially useless for similarity searching?

Any insight/help would be greatly appreciated. Thanks in advance!
```
---

     
 
all -  [ How to save DocArrayInMemorySearch object ](https://www.reddit.com/r/LangChain/comments/1673lji/how_to_save_docarrayinmemorysearch_object/) , 2023-09-04-0909
```
Does anyone know how I can persist or save the database object created using DocArrayInMemorySearch.from\_documents(text
s, embedding)? I can't find anything in the documentation and it would really help my project to be able to quickly uplo
ad this. If anyone has any leads I'd really appreciate it. I'm working in Colab.
```
---

     
 
all -  [ Combining LLMs with vector DBs ](https://www.reddit.com/r/LangChain/comments/1672tpn/combining_llms_with_vector_dbs/) , 2023-09-04-0909
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

     
 
all -  [ Creating an Embeddings REST API ](https://www.reddit.com/r/LangChain/comments/1672pca/creating_an_embeddings_rest_api/) , 2023-09-04-0909
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

     
 
all -  [ RefineDocumentsChain ](https://www.reddit.com/r/LangChain/comments/1670dl4/refinedocumentschain/) , 2023-09-04-0909
```
hey guys, I can't for the life of me unserstand how to use this for a question insted of summary. i want it to get multi
ple contexts and imporve on the answer it gives.

&#x200B;

any leads?

&#x200B;

thanks!!
```
---

     
 
all -  [ LangChain Library Adds Full Support for Neo4j Vector Index ](https://www.reddit.com/r/Neo4j/comments/166z06j/langchain_library_adds_full_support_for_neo4j/) , 2023-09-04-0909
```
My latest blog post demonstrates how to use the recently added Neo4j Vector index in LangChain Library to both load and 
read data.

&#x200B;

[https://medium.com/neo4j/langchain-library-adds-full-support-for-neo4j-vector-index-fa94b8eab334]
(https://medium.com/neo4j/langchain-library-adds-full-support-for-neo4j-vector-index-fa94b8eab334)
```
---

     
 
all -  [ Would you pay for high-quality vector embeddings? ](https://www.reddit.com/r/LangChain/comments/166yug1/would_you_pay_for_highquality_vector_embeddings/) , 2023-09-04-0909
```
I'm thinking to curate high quality vector embedding 'libraries' and enable developers to call them via an API. This way
 they can embed knowledge from across domains easily into their apps.

Would this be useful to you as a developer?

edit
 1: the vector embedding libraries would be curated textual content by subject-matter-experts on topics like also tradin
g, molecular biology, etc. that developers can't curate on their own.
```
---

     
 
all -  [ What do the GPU-poor use to host models? ](https://www.reddit.com/r/LangChain/comments/166wnjm/what_do_the_gpupoor_use_to_host_models/) , 2023-09-04-0909
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

     
 
all -  [ ICYMI August: Zep Vector DB, User Store, LangChain collabs & more! ](https://www.reddit.com/r/LangChain/comments/166tqw2/icymi_august_zep_vector_db_user_store_langchain/) , 2023-09-04-0909
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

     
 
all -  [ I Built an All-In-One Discord Bot for OpenAI's GPT 3.5 Turbo ](https://www.reddit.com/r/OpenAI/comments/166qrg9/i_built_an_allinone_discord_bot_for_openais_gpt/) , 2023-09-04-0909
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

     
 
all -  [ Output parser for openai chat models ](https://www.reddit.com/r/LangChain/comments/166jxzi/output_parser_for_openai_chat_models/) , 2023-09-04-0909
```
I can’t seem to get this output parser from langchain to work for the chatopenai models: 

https://python.langchain.com/
docs/modules/model_io/output_parsers/pydantic

It works when I just use openai but not the chatopenai. Let me know if an
yone has any ideas or examples. I’m trying to output json object that has two list items.
```
---

     
 
all -  [ Have any LLMs been optimized or fine tuned to be effective langchain agents? ](https://www.reddit.com/r/LangChain/comments/166hoq8/have_any_llms_been_optimized_or_fine_tuned_to_be/) , 2023-09-04-0909
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

     
 
all -  [ 🤖 Agenta: Open-Source Platform for LLM Prompt Engineering, Evaluation, and Deployment ](https://www.reddit.com/r/opensource/comments/166gb8a/agenta_opensource_platform_for_llm_prompt/) , 2023-09-04-0909
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

     
 
all -  [ 🤖 Agenta: Open-Source Platform for LLM Prompt Engineering, Evaluation, and Deployment ](https://www.reddit.com/r/PromptEngineering/comments/166fxyq/agenta_opensource_platform_for_llm_prompt/) , 2023-09-04-0909
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

     
 
all -  [ langchain generating similar questions with question_generator parameter ](https://www.reddit.com/r/LangChain/comments/166fc4g/langchain_generating_similar_questions_with/) , 2023-09-04-0909
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

     
 
MachineLearning -  [ [D] Is there anything LangChain can do better than using LLMs directly (either through a website or  ](https://www.reddit.com/r/MachineLearning/comments/165airj/d_is_there_anything_langchain_can_do_better_than/) , 2023-09-04-0909
```
I haven't used ChatGPT a lot or any other LLMs, I've been reading about  Langchain and its use cases, and I'm having tro
uble wrapping my head  around exactly what it does. From what I understand, its an alternative  interface for LLMs, allo
wing for easy switching between them, and makes  some work for specific use cases easier. If I wanted to write an app or
  script to interact with LLMs and do other tasks, how would LangChain be  better than just making API call(s) to an LLM
, getting back the result  as a string, and doing whatever with it?
```
---

     
 
MachineLearning -  [ Apache Airflow vs. LangChain and LlamaHub for LLM data pipeline [D] ](https://www.reddit.com/r/MachineLearning/comments/160lexg/apache_airflow_vs_langchain_and_llamahub_for_llm/) , 2023-09-04-0909
```
I’m looking for recommendations, suggestions, and/or good documentation that outlines which data pipeline would be best 
to ingest my private data (which will then be split into chunks/nodes for vector embeddings and so forth). Thank you in 
advance!
```
---

     
 
MachineLearning -  [ [P] LLM Apps Are Mostly Data Pipelines ](https://www.reddit.com/r/MachineLearning/comments/15z0muk/p_llm_apps_are_mostly_data_pipelines/) , 2023-09-04-0909
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

     
 
MachineLearning -  [ [P] pgml-chat: A command-line tool for deploying low-latency knowledge-based chatbots ](https://www.reddit.com/r/MachineLearning/comments/15t5nzl/p_pgmlchat_a_commandline_tool_for_deploying/) , 2023-09-04-0909
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

     
 
MachineLearning -  [ [P] My apprehension about LangChain and why you don’t need LangChain for building a RAG bot. ](https://www.reddit.com/r/MachineLearning/comments/15ry3z4/p_my_apprehension_about_langchain_and_why_you/) , 2023-09-04-0909
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

     
 
MachineLearning -  [ [D] Approach to creating an 'AI tutor' chatbot for a fantasy language? ](https://www.reddit.com/r/MachineLearning/comments/15o4jy9/d_approach_to_creating_an_ai_tutor_chatbot_for_a/) , 2023-09-04-0909
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

     
 
MachineLearning -  [ LLMs Challenges and Approaches Panel [N] ](https://www.reddit.com/r/MachineLearning/comments/15noqwr/llms_challenges_and_approaches_panel_n/) , 2023-09-04-0909
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

     
 
MachineLearning -  [ [D] training a model for function calls ](https://www.reddit.com/r/MachineLearning/comments/15n1j52/d_training_a_model_for_function_calls/) , 2023-09-04-0909
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

     
 
MachineLearning -  [ [D]Embedding model and vector store on LangChain ](https://www.reddit.com/r/MachineLearning/comments/15lllm0/dembedding_model_and_vector_store_on_langchain/) , 2023-09-04-0909
```
For Langchain users, what are the best text embedding models and vector stores (with similarity search) among the many i
ntegrations for connecting a AI model to text data? 

And does performance vary drastically from one model/database to a
nother? 
```
---

     
 
MachineLearning -  [ [P] Rust meets Llama2: OpenAI compatible API written in Rust ](https://www.reddit.com/r/MachineLearning/comments/15k254o/p_rust_meets_llama2_openai_compatible_api_written/) , 2023-09-04-0909
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

     
 
MachineLearning -  [ [D] Document-based QnA without OpenAI? ](https://www.reddit.com/r/MachineLearning/comments/15imv19/d_documentbased_qna_without_openai/) , 2023-09-04-0909
```
I am working on a project that is very popular with the inception of Langchain + GPT applications. However, I want to ma
ke it open source and hence don't want to use GPT. So something like Langchain + LLama2, etc. I know currently Langchain
 only supports GPT but any other ideas are highly appreciated!
```
---

     
