 
all -  [ Create_sql_agent not able to access db when being used as a tool in a multi-tool agent ](https://www.reddit.com/r/LangChain/comments/16a6fxq/create_sql_agent_not_able_to_access_db_when_being/) , 2023-09-05-0909
```
I have created a SQL bot using Langchain that was performing great, utilizing the create\_sql\_agent toolkit, however no
w as I am trying to add more tools that play off of the queries it was performing, the bot is now unable to make any inf
erences about the names of the columns, or seem to connect to the db at all. I am basing my work off of the docs here: [
https://python.langchain.com/docs/modules/agents/agent\_types/openai\_functions\_agent](https://python.langchain.com/doc
s/modules/agents/agent_types/openai_functions_agent)  
Let me know if there are any mistakes in approach on my part, or 
if anyone has experienced anything similar.  
Thanks in advance!
```
---

     
 
all -  [ Structured data and LLMs: Should I embed? ](/r/vectordatabase/comments/16a3x33/structured_data_and_llms_should_i_embed/) , 2023-09-05-0909
```

```
---

     
 
all -  [ LLM for big contextual questions ](https://www.reddit.com/r/LangChain/comments/169zbmo/llm_for_big_contextual_questions/) , 2023-09-05-0909
```
Hi all,

i need an LLM that can run on my avarage GPU for now (GeForce 3060) and can take an input of a big context (say
 7000 tokens) and return an answer for it.

llama2 seems not to fit and mpt7 needs a stronger GPU.

any suggestions?
```
---

     
 
all -  [ Saving AIMessages to a file ](https://www.reddit.com/r/LangChain/comments/169yjw8/saving_aimessages_to_a_file/) , 2023-09-05-0909
```
I have code that looks like this:

    chat = ChatOpenAI(openai_api_key=api_key)
    system_tempalte = 'some text'
    s
ystem_message = SystemMessagePromptTemplate.from_template(system_template)
    human_template = '{variable_one} {variabl
e_two}'
    human_message = HumanMessagePromptTemplate.from_template(human_template)
    chat_prompt = ChatPromptTemplat
e.from_messages([system_message, human_message])
    for i in range (len(variable_one)):
        prompt = chat_prompt.fo
rmat_messages(variable_one = variable_one[i], variable_two = variable_two[i])
        results = chat(prompt)

what I wan
t to do is return the AIMessage as a string that I can write to a file that has Variable One: Variable Two: and then the
 AIMessage based on what variables its iterated. I haven't been able to make sense of how to do that from the documentat
ion. Anyone got any ideas?
```
---

     
 
all -  [ GPT-4 enhanced GPT-3.5 prompting ](https://www.reddit.com/r/LangChain/comments/169xjsl/gpt4_enhanced_gpt35_prompting/) , 2023-09-05-0909
```
I've recently read a post on Twitter where someone claimed that he has great success with crafting and refining prompts 
for GPT-3.5 with the help of GPT-4. Unfortunately he gave no further hints on how he's doing that. He claimed that his m
ethod lifts GPT-3.5 almost on GPT-4 level. 

1. Anybody heard of this approach?
2. Wouldn't LangChain be the perfect too
l to automate that?
```
---

     
 
all -  [ Ways to Inject Metadata into Text Chunks? ](https://www.reddit.com/r/LangChain/comments/169uxea/ways_to_inject_metadata_into_text_chunks/) , 2023-09-05-0909
```
Hi, would anybody know what the best way to inject metadata into text chunks using LangChain or maybe even Llama Index w
ould be?

For my use-case, I want to load in a PDF, and split the PDF into chunks, I want to be able to inject additiona
l metadata. Is there a class in LangChain that helps with that? If not, what would be a good way to do this? I thought o
f a somewhat hacky way of doing it by converting to JSON, appending the metadata fields, and then using the jsonloader t
o load it back in.

Any ideas or suggestions would be most welcomed and appreciated. Thanks in advanced!
```
---

     
 
all -  [ Running llama 2(any model) in nodejs? ](https://i.redd.it/lbsexelh69mb1.jpg) , 2023-09-05-0909
```
I'm trying to run llama2 model by using node js but am constantly running into errors. The langchain documentation recom
mends some other npm package and there are some tutorials out there which are using a totally different npm package. I'v
e tried everything(even moved the file to D) in order to make the path simple, but yet the same error pops up. 

Can any
body tell me how to correctly set up local llm with nodejs? Fed up of errors and I've been trying since yesterday!
Pleas
e help!!
```
---

     
 
all -  [ StructuredOutputParser with OpenAI chat model in JS ](https://www.reddit.com/r/LangChain/comments/169u1c2/structuredoutputparser_with_openai_chat_model_in/) , 2023-09-05-0909
```
Did anyone manage to use StructuredOutputParser with a SequentialChain or RunnableSequence in Javascript?

My code looks
 like this and I'm getting a parsing error:

    import 'dotenv/config';
    
    import { PromptTemplate } from 'langch
ain/prompts';
    import { ChatOpenAI } from 'langchain/chat_models/openai';
    import { RunnableSequence } from 'langc
hain/schema/runnable';
    import { StructuredOutputParser } from 'langchain/output_parsers';
    
    // OPEN AI CONFIG

    const model = new ChatOpenAI({
      openAIApiKey: process.env.OPENAI_API_KEY,
      modelName: 'gpt-3.5-turbo',
  
    max_tokens: 1800,
      frequency_penalty: 0.1,
      temperature: 0.4,
    });
    
    const promptTemplate = Prom
ptTemplate.fromTemplate(
      `Please provided me a detailed meaning for each the following expression in German: {expr
ession}
      `
    );
    
    //OUTPUT PARSERS
    // const outputParser = new StringOutputParser();
    
    // With 
a `StructuredOutputParser` we can define a schema for the output.
    const parser = StructuredOutputParser.fromNamesAnd
Descriptions({
      expression: 'expression provided',
      meaning: 'detailed meaning of the expression',
    });
   
 const formatInstructions = parser.getFormatInstructions();
    
    const chain = RunnableSequence.from([promptTemplate
, model, parser]);
    
    const result = await chain.invoke({ expression: 'Abendkleid' });
    
    console.log(result
);
```
---

     
 
all -  [ I built a Chrome extension that adds a chatbot to every GitHub repository ](https://www.reddit.com/r/Python/comments/169trj1/i_built_a_chrome_extension_that_adds_a_chatbot_to/) , 2023-09-05-0909
```
Try it here: [https://chrome.google.com/webstore/detail/adrenaline/noafjjeodnjmdbmcmckafcbnnfclkfbl?hl=en&authuser=2](ht
tps://chrome.google.com/webstore/detail/adrenaline/noafjjeodnjmdbmcmckafcbnnfclkfbl?hl=en&authuser=2)

**Why did I build
 this?**

I spend a lot of time browsing code on GitHub. I'm usually searching for code that solves a problem I'm runnin
g into, or just trying to understand how to use an open-source library with bad documentation. But either way, GitHub's 
native code search system can only do so much and I always end up combing through sometimes thousands of lines of code t
o get what I want.

I built this extension to solve that problem. It uses a combination of vector search + static analys
is + GPT-4 to insert an AI expert into every codebase. You can ask it anything and it'll not only try its best to answer
 the question, but cite specific files, functions, and code snippets in the repository to back up its answer.

**How did
 I build this?**

I'm using *langchain* (a Python library for working with LLMs) for the question-answering pipeline, an
d I used the Python bindings for *tree-sitter* (a library for parsing ASTs for various languages) to intelligently split
 code into chunks. All of this logic (indexing repositories + answering questions) is implemented in a Python websocket 
server. 
```
---

     
 
all -  [ Doubts on making an agent curated to a particular domain ](https://www.reddit.com/r/LangChain/comments/169qkvo/doubts_on_making_an_agent_curated_to_a_particular/) , 2023-09-05-0909
```
I want to create an agent using langchain and as a beginner I don't know where to start. I want my agent to answer only 
for technical questions.
```
---

     
 
all -  [ Few Shot Prompt with Load_qa_chain stuff ](https://www.reddit.com/r/LangChain/comments/169oseq/few_shot_prompt_with_load_qa_chain_stuff/) , 2023-09-05-0909
```
Can we incorporate few shot prompt into load_qa_chain of type 'stuff'? My few shot prompt template worked fine for LLMCh
ain but there is a variable type error when I insert the same few shot prompt template into load_qa_chain. Thanks!
```
---

     
 
all -  [ Building and debugging LLMs with Aim: LangChain + AimStack ](https://www.reddit.com/r/LangChain/comments/169k5yt/building_and_debugging_llms_with_aim_langchain/) , 2023-09-05-0909
```
Hi r/LangChain community!

With the introduction of ChatGPT and large language models (LLMs) such as GPT3.5-turbo and GP
T4, AI progress has skyrocketed.

As AI systems get increasingly complex, the ability to effectively debug and monitor t
hem becomes crucial. Without comprehensive tracing and debugging, the improvement, monitoring and understanding of these
 systems become extremely challenging.

**⛓🦜It's now possible to trace LangChain agents and chains with Aim, using just 
a few lines of code! All you need to do is configure the Aim callback and run your executions as usual.**

Below are a f
ew highlights from the integration. Check out the full article [here](https://aimstack.io/blog/integrations/langchain-ai
m-building-and-debugging-ai-systems-made-easy).

On the home page, you'll find an organized view of all your tracked exe
cutions, making it easy to keep track of your progress and recent runs.

[Home page](https://preview.redd.it/9qlg67oxl6m
b1.jpg?width=1500&format=pjpg&auto=webp&s=aa0c4d4376c837d36464acae0ca5a2a8010c3a3a)

When navigating to an individual ex
ecution page, you'll find an overview of system information and execution details. Here you can access:

* CLI command a
nd arguments,
* Environment variables,
* Packages,
* Git information,
* System resource usage,
* and other relevant info
rmation about an individual execution.

[Overview](https://preview.redd.it/fi66yma1m6mb1.jpg?width=1500&format=pjpg&auto
=webp&s=5be6a212a4010f854fe01bb5804222ddba352c42)

Aim automatically captures terminal outputs during execution. Access 
these logs in the “Logs” tab to easily keep track of the progress of your AI system and identify issues.

[Logs tab](htt
ps://preview.redd.it/5iq1q1w3m6mb1.jpg?width=1500&format=pjpg&auto=webp&s=de1441edcabbe3feee9fc329d15fd59becd51eee)

In 
the 'Text' tab, you can explore the inner workings of a chain, including agent actions, tools and LLMs inputs and output
s. This in-depth view allows you to review the metadata collected at every step of execution.

[Texts tab](https://previ
ew.redd.it/ojwkhtw6m6mb1.jpg?width=1500&format=pjpg&auto=webp&s=cc23f4c42e6acc2b20be9b16dcc34c20c056d47f)

With Text Exp
lorer, you can effortlessly compare multiple executions, examining their actions, inputs, and outputs side by side. It h
elps to identify patterns or spot discrepancies.

[Text explorer](https://preview.redd.it/l8s5ct39m6mb1.jpg?width=1500&f
ormat=pjpg&auto=webp&s=a1a12da2f0024efe3a254452c7f465199917d199)

To read the full article click [here](https://aimstack
.io/blog/integrations/langchain-aim-building-and-debugging-ai-systems-made-easy), we prompt the agent to discover who Le
onardo DiCaprio’s girlfriend is and calculate her current age raised to the power of 0.43. 

If you haven't yet, drop a 
star to support open-source project! ⭐️  
[https://github.com/aimhubio/aim](https://github.com/aimhubio/aim)

Feel free 
to join the community [Aim Discord Community](https://discord.com/invite/zXq2NfVdtF). 🙌
```
---

     
 
all -  [ Langchain with Openrouter ](https://www.reddit.com/r/LangChain/comments/169j8cg/langchain_with_openrouter/) , 2023-09-05-0909
```
Is anyone using Langchain with [Openrouter.ai](https://Openrouter.ai)? I'm trying to use the gpt-4 model on openrouter b
ut it's giving me drastically different results than using gpt-4 on the openai website.

Anyone else using gpt-4 with op
enrouter and langchain? Can you get it to give you good results?
```
---

     
 
all -  [ Running several Lora models ](https://www.reddit.com/r/LangChain/comments/169cgv6/running_several_lora_models/) , 2023-09-05-0909
```
I am using LLAMA2 13B and I have several (ie 4) different LORA finetunes. I want to run all of them on the same GPU. Wha
t’s the best library for doing this?
```
---

     
 
all -  [ Branching out from OpenAI question ](https://www.reddit.com/r/LLMDevs/comments/1690hyk/branching_out_from_openai_question/) , 2023-09-05-0909
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

     
 
all -  [ I want to make an LLM on my YouTube transcripts, and I am not sure how to get it done. ](https://www.reddit.com/r/LangChain/comments/168xubo/i_want_to_make_an_llm_on_my_youtube_transcripts/) , 2023-09-05-0909
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

     
 
all -  [ 3rd Year CS Student - Resume Review please ](https://www.reddit.com/r/resumes/comments/168x4pf/3rd_year_cs_student_resume_review_please/) , 2023-09-05-0909
```
&#x200B;

https://preview.redd.it/nsvmpqi3m1mb1.jpg?width=1239&format=pjpg&auto=webp&s=9cdddc7733cf5bc54242b11a55fa3beaf
6124815
```
---

     
 
all -  [ Error with agent syntax. ](https://www.reddit.com/r/LangChain/comments/168szss/error_with_agent_syntax/) , 2023-09-05-0909
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

     
 
all -  [ Crawl websites and use them with Langchain ](https://www.reddit.com/r/LangChain/comments/168sgfi/crawl_websites_and_use_them_with_langchain/) , 2023-09-05-0909
```
What is the best way to crawl websites and answer questions from them using Langchain framework? Are there any prebuilt 
options available? Or doing something like automatically download and convert the page to PDF, index it and then run cha
ins/prompts for Q&A? Looking for something scalable as the requirement is to answer from quiet a bit of links. Thanks.
```
---

     
 
all -  [ Merging GPT-4 and PDF-based Retrieval System ](https://www.reddit.com/r/ChatGPTPro/comments/168sgbf/merging_gpt4_and_pdfbased_retrieval_system/) , 2023-09-05-0909
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

     
 
all -  [ Merging GPT-4 and PDF-based Retrieval System ](https://www.reddit.com/r/OpenAI/comments/168sft4/merging_gpt4_and_pdfbased_retrieval_system/) , 2023-09-05-0909
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

     
 
all -  [ ChatGPT Plugins - How to find URL? ](https://www.reddit.com/r/LangChain/comments/168s47r/chatgpt_plugins_how_to_find_url/) , 2023-09-05-0909
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

     
 
all -  [ Langchain+local LLM+Javascript? ](https://www.reddit.com/r/LangChain/comments/168qcvq/langchainlocal_llmjavascript/) , 2023-09-05-0909
```
Hi. Can I hook langchain up to my local LLM? I´ve seen some videos of people doing it with python and something called p
ipelines, but no info on Javascript. Can it be done with javascript? 
```
---

     
 
all -  [ Accessing high-quality curated vector embedding knowledgebases ](https://www.reddit.com/r/LangChain/comments/168pkqs/accessing_highquality_curated_vector_embedding/) , 2023-09-05-0909
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

     
 
all -  [ To query specific document from chromadb with llama2 ](https://www.reddit.com/r/LangChain/comments/168mqwm/to_query_specific_document_from_chromadb_with/) , 2023-09-05-0909
```
I am planning to index multiple document and later if a question comes against a specific document i want llama2 to answ
er from that specific document only. Also i wanted avoid indexing again if the document is already there. How can I do t
his with chroma client and langchain.
```
---

     
 
all -  [ Chatbot help ](https://www.reddit.com/r/Python/comments/168l850/chatbot_help/) , 2023-09-05-0909
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

     
 
all -  [ I built a Discord bot that takes files, websites, to teach GPT, or chat, or DALL E 2 ](https://www.reddit.com/r/ChatGPTCoding/comments/168iavi/i_built_a_discord_bot_that_takes_files_websites/) , 2023-09-05-0909
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

     
 
all -  [ Call for participation in an open source langchain application project ](https://www.reddit.com/r/LangChain/comments/168gd02/call_for_participation_in_an_open_source/) , 2023-09-05-0909
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

     
 
all -  [ Journey to Build the Ultimate ChatGPT Has Hit a Roadblock – Could Use Your Expertise! ](https://www.reddit.com/r/ChatGPT/comments/168fhgg/journey_to_build_the_ultimate_chatgpt_has_hit_a/) , 2023-09-05-0909
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

     
 
all -  [ AI Tools ](https://www.reddit.com/r/u_Best_Ai_Tools_Finder/comments/168dcan/ai_tools/) , 2023-09-05-0909
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

     
 
all -  [ How to deploy/host custom LLM app for production? ](https://www.reddit.com/r/LocalLLaMA/comments/1689jfx/how_to_deployhost_custom_llm_app_for_production/) , 2023-09-05-0909
```
So let's say we have created app using Langchain and Pinecone (for embeddings). App uses AutoTokenizer, AutoModelForCaus
alLM, ConversationalRetrievalChain for basic QA on documents and X model from HuggingFace.   


For now I ran this in Go
ogle Colab, but what if I want to make this accessable to public? How do I host this and where? I know there is Azure th
ing, but that's for using OpenAi stuff. I couldn't find any good guide or anything like that for hosting this LLM apps f
or public, so not locally.
```
---

     
 
all -  [ I am having trouble with large dataset. ](https://www.reddit.com/r/LangChain/comments/1688bek/i_am_having_trouble_with_large_dataset/) , 2023-09-05-0909
```
I am using langchain framework 'load_qa_chain' to ask questions from a huge dataset. But it is unable to answer some que
stion which require checking on the whole dataset (for eg: If the dataset is the conversation between two people for yea
rs, query: List all the critical problems faced by the person in his lifetime? , It is able to give some of it but missi
ng some important data). How can I resolve this?
```
---

     
 
all -  [ How should I go about getting my AI to use tools correctly (and consistently)? ](https://www.reddit.com/r/LocalLLaMA/comments/1687l5p/how_should_i_go_about_getting_my_ai_to_use_tools/) , 2023-09-05-0909
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

     
 
all -  [ help ](https://www.reddit.com/r/LangChain/comments/1687dxt/help/) , 2023-09-05-0909
```
 how do we handle larger context length while finetuning the model ?  
suppose i have the dataset with question, answer 
pair.  
My problem here is question exceed the context length so that answer doesnot fit. which has lead the model doesn
't generate the answer. How do we actually solve this issue? 
```
---

     
 
all -  [ How Code Interpreter Orchestration is Designed? ](https://www.reddit.com/r/ChatGPT/comments/1684itm/how_code_interpreter_orchestration_is_designed/) , 2023-09-05-0909
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

     
 
all -  [ How to deal with missing question mark? ](https://www.reddit.com/r/LangChain/comments/167vauj/how_to_deal_with_missing_question_mark/) , 2023-09-05-0909
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

     
 
all -  [ I have some defined classes and a design system. What is the best approach to build a chat bot that  ](https://www.reddit.com/r/LangChain/comments/167sfdx/i_have_some_defined_classes_and_a_design_system/) , 2023-09-05-0909
```
 How can I create a chatbot that generates HTML components using predefined classes from a design system, and what is th
e best approach to manage this without utilizing a vector store? 
```
---

     
 
all -  [ Conversationalretrievalchains pigeon holes on chat history + history overwhelms context window ](https://www.reddit.com/r/LangChain/comments/167ndda/conversationalretrievalchains_pigeon_holes_on/) , 2023-09-05-0909
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

     
 
all -  [ The talks from SeattleJS Conf 2023 have been posted online (free) ](https://www.reddit.com/r/webdev/comments/167kfyv/the_talks_from_seattlejs_conf_2023_have_been/) , 2023-09-05-0909
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

     
 
all -  [ Langchain in Javascript in a .NET project ](https://www.reddit.com/r/LangChain/comments/167g2mi/langchain_in_javascript_in_a_net_project/) , 2023-09-05-0909
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

     
 
all -  [ Stanford DSPy - Better than LangChain? ](https://www.reddit.com/r/LangChain/comments/167dzcb/stanford_dspy_better_than_langchain/) , 2023-09-05-0909
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

     
 
all -  [ I'm trying to stream recorded audio from the browser to my LLM powered backend. ](https://www.reddit.com/r/LangChain/comments/167bjky/im_trying_to_stream_recorded_audio_from_the/) , 2023-09-05-0909
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

     
 
MachineLearning -  [ [D] Is there anything LangChain can do better than using LLMs directly (either through a website or  ](https://www.reddit.com/r/MachineLearning/comments/165airj/d_is_there_anything_langchain_can_do_better_than/) , 2023-09-05-0909
```
I haven't used ChatGPT a lot or any other LLMs, I've been reading about  Langchain and its use cases, and I'm having tro
uble wrapping my head  around exactly what it does. From what I understand, its an alternative  interface for LLMs, allo
wing for easy switching between them, and makes  some work for specific use cases easier. If I wanted to write an app or
  script to interact with LLMs and do other tasks, how would LangChain be  better than just making API call(s) to an LLM
, getting back the result  as a string, and doing whatever with it?
```
---

     
 
MachineLearning -  [ Apache Airflow vs. LangChain and LlamaHub for LLM data pipeline [D] ](https://www.reddit.com/r/MachineLearning/comments/160lexg/apache_airflow_vs_langchain_and_llamahub_for_llm/) , 2023-09-05-0909
```
I’m looking for recommendations, suggestions, and/or good documentation that outlines which data pipeline would be best 
to ingest my private data (which will then be split into chunks/nodes for vector embeddings and so forth). Thank you in 
advance!
```
---

     
 
MachineLearning -  [ [P] LLM Apps Are Mostly Data Pipelines ](https://www.reddit.com/r/MachineLearning/comments/15z0muk/p_llm_apps_are_mostly_data_pipelines/) , 2023-09-05-0909
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

     
 
MachineLearning -  [ [P] pgml-chat: A command-line tool for deploying low-latency knowledge-based chatbots ](https://www.reddit.com/r/MachineLearning/comments/15t5nzl/p_pgmlchat_a_commandline_tool_for_deploying/) , 2023-09-05-0909
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

     
 
MachineLearning -  [ [P] My apprehension about LangChain and why you don’t need LangChain for building a RAG bot. ](https://www.reddit.com/r/MachineLearning/comments/15ry3z4/p_my_apprehension_about_langchain_and_why_you/) , 2023-09-05-0909
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

     
 
MachineLearning -  [ [D] Approach to creating an 'AI tutor' chatbot for a fantasy language? ](https://www.reddit.com/r/MachineLearning/comments/15o4jy9/d_approach_to_creating_an_ai_tutor_chatbot_for_a/) , 2023-09-05-0909
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

     
 
MachineLearning -  [ LLMs Challenges and Approaches Panel [N] ](https://www.reddit.com/r/MachineLearning/comments/15noqwr/llms_challenges_and_approaches_panel_n/) , 2023-09-05-0909
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

     
 
MachineLearning -  [ [D] training a model for function calls ](https://www.reddit.com/r/MachineLearning/comments/15n1j52/d_training_a_model_for_function_calls/) , 2023-09-05-0909
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

     
 
MachineLearning -  [ [D]Embedding model and vector store on LangChain ](https://www.reddit.com/r/MachineLearning/comments/15lllm0/dembedding_model_and_vector_store_on_langchain/) , 2023-09-05-0909
```
For Langchain users, what are the best text embedding models and vector stores (with similarity search) among the many i
ntegrations for connecting a AI model to text data? 

And does performance vary drastically from one model/database to a
nother? 
```
---

     
 
MachineLearning -  [ [P] Rust meets Llama2: OpenAI compatible API written in Rust ](https://www.reddit.com/r/MachineLearning/comments/15k254o/p_rust_meets_llama2_openai_compatible_api_written/) , 2023-09-05-0909
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

     
 
MachineLearning -  [ [D] Document-based QnA without OpenAI? ](https://www.reddit.com/r/MachineLearning/comments/15imv19/d_documentbased_qna_without_openai/) , 2023-09-05-0909
```
I am working on a project that is very popular with the inception of Langchain + GPT applications. However, I want to ma
ke it open source and hence don't want to use GPT. So something like Langchain + LLama2, etc. I know currently Langchain
 only supports GPT but any other ideas are highly appreciated!
```
---

     
