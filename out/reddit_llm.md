 
all -  [ Langchain vs LlamaIndex ](https://www.reddit.com/gallery/1b1qzxt) , 2024-02-28-0909
```
now, fight!

also if anyone knows how to get a streaming loop working in langchain

I get all sorts of abstracted type e
rrors when I try and the documentation makes me want to cry

I just started learning llama index yesterday
```
---

     
 
all -  [ How To Use LangChain With ChatGPT ](https://www.successtechservices.com/how-to-use-langchain-with-chatgpt/) , 2024-02-28-0909
```

```
---

     
 
all -  [ How to Use LangChain with ChatGPT ](https://www.reddit.com/r/ArtificialInteligence/comments/1b1ntdk/how_to_use_langchain_with_chatgpt/) , 2024-02-28-0909
```
Did you know that integrating LangChain with ChatGPT can significantly enhance natural language processing capabilities 
and enable smarter text processing in your projects? LangChain, a powerful framework for building custom ChatGPT AI, com
bined with the AI language model, ChatGPT, can revolutionize the way you work with language data. 

In this article, I w
ill guide you through the process of integrating LangChain and ChatGPT step-by-step, allowing you to leverage their comb
ined power and unlock their full potential for efficient text processing.

https://www.successtechservices.com/how-to-us
e-langchain-with-chatgpt/
```
---

     
 
all -  [ Example unit test for Langchain chat models ](https://www.reddit.com/r/LangChain/comments/1b1kkkq/example_unit_test_for_langchain_chat_models/) , 2024-02-28-0909
```
Something I think that's missing from Langchain documentation is good examples for how to reliably test your chains/chat
s/whatever without actually using a real LLM (costly/slow/unreliable).

I created an example (with Dockerfile included) 
on how to test an LLMChain with a brief conversation including a ConversationBufferWindowMemory.

Please let me know wha
t you think! If you have other requests, let me know.

[https://github.com/ThreeRiversAINexus/sample-langchain-agents/bl
ob/main/fake\_llm\_examples/test\_chat\_convo.py](https://github.com/ThreeRiversAINexus/sample-langchain-agents/blob/mai
n/fake_llm_examples/test_chat_convo.py)

The example in the langchain documentation that this is based on: [https://pyth
on.langchain.com/docs/modules/model\_io/chat/quick\_start](https://python.langchain.com/docs/modules/model_io/chat/quick
_start)
```
---

     
 
all -  [ RAG model where the user may mention documents in their messages ](https://www.reddit.com/r/LangChain/comments/1b1k6ed/rag_model_where_the_user_may_mention_documents_in/) , 2024-02-28-0909
```
I have a pretty good LangChain RAG model up and running, and some users asked if it's possible to include the names and 
URLs of the documents they would like the LLM to search for in the query. 

Something like:

Human query: 'Using only th
e data sheet of product X, can you confirm that ....'

Programmatically speaking, I know that I can define the search fi
lters in the retriever, but I am not sure what is the best way to have the LLM detect the document the user is referring
 to first. 

A naive approach here would be to do this outside of the chain, and preprocess the query before sending it 
to the RAG model (alongside any search filter metadata, if applicable). Is that the recommended approach? What about age
nts, would that be too much for this use case?
```
---

     
 
all -  [ How to include metadata of retrieved content in the Output of retriever ](https://www.reddit.com/r/LangChain/comments/1b1k4p7/how_to_include_metadata_of_retrieved_content_in/) , 2024-02-28-0909
```
Hi, 

I have a noob question and hope that someone here can help. 

This is how I set up the agent for my blog.   
embed
dings = OpenAIEmbeddings()  
db = FAISS.load\_local('faiss\_index', embeddings)  
retriever = db.as\_retriever(search\_t
ype='mmr')  
tool = create\_retriever\_tool(  
 retriever,  
 'search\_chandler\_nguyen\_blog',  
 'Searches and returns
 content from Chandler Nguyen's blog. For any questions about what Chandler Nguyen wrote before, you must use this tool!
'  
)  
tools = \[tool\]  
prompt = ChatPromptTemplate.from\_messages(\[  
('system', 'You are a chatbot named Sydney. \
\  
You help people to answer questions about Chandler Nguyen Blog in a thoughtful way. \\  
Respond in a friendly and h
elpful tone, with concise answers if possible. \\  
Use HTML-compatible bullet point format and line breaks (\`<br>\`) f
or long answers where necessary. \\  
Use the following pieces of retrieved context to answer the question. \\  
If you 
do not know the answer, just say that you do not know. \\  
Include the blog post URL or published date as references in
 your answer. \\  
Please try your best as this is very important to me and the user.'),  
 MessagesPlaceholder(variable
\_name='chat\_history'),  
('user', '{input}'),  
 MessagesPlaceholder(variable\_name='agent\_scratchpad'),  
\])  
llm 
= ChatOpenAI(model\_name='gpt-3.5-turbo-0125', temperature=0, streaming=True)  
llm\_with\_tools = llm.bind\_tools(tools
)  
agent = (  
{  
 'input': lambda x: x\['input'\],  
 'agent\_scratchpad': lambda x: format\_to\_openai\_tool\_messag
es(x\['intermediate\_steps'\]),  
 'chat\_history': lambda x: x\['chat\_history'\],  
}  
 | prompt  
 | llm\_with\_tool
s  
 | OpenAIToolsAgentOutputParser()  
)  
agent\_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)  



The issue here is that the retriever output doesn't include metadata like 'URL' or 'published\_date'. I don't know how t
o incorporate that using RunnablePassthrough or RunnableParallel and/or 'lambda' ?  
I know that I can have the metadata
 this way:  
docs = retriever.invoke(query)  
for doc in docs:  
 print(doc.metadata)

&#x200B;
```
---

     
 
all -  [ Improve speed over my LLM App ](https://www.reddit.com/r/LocalLLaMA/comments/1b1jtvw/improve_speed_over_my_llm_app/) , 2024-02-28-0909
```
Hey guys,  
I was wondering I built a Langchain app connecting to a local LLM using Ollama (Mistral 8x7b) I make thousan
ds of requests a day, I have an RTX 4090 but it takes 15 - 25 seconds to get a response with 100% of my GPU used (checki
ng using nvtop). I was wondering if I build a rack and over time, adding more and more GPU Cards will I be able to incre
ase the speed of request processing?
```
---

     
 
all -  [ Langchain / OpenAI to Mistral conversion to query mysql ](https://www.reddit.com/r/LangChain/comments/1b1jfc2/langchain_openai_to_mistral_conversion_to_query/) , 2024-02-28-0909
```
I have the following LangChain/OpenAI that queries a mysql database for data, I have spun up a Mistral LLM thats running
 on my localhost - I have tried to adapt my code to solely use the Mistral LLM, however I get the following error:

Conn
ection could not be made due to the following error: Connection error.

&#x200B;

    def query_maker(user_input):
     
   #OpenAI LLM (working)
        #openaiLLM = ChatOpenAI(model='gpt-3.5-turbo', temperature=0.7, openai_api_key=api_key,
 cache=False)
        #Mistral LLM
        LLM = ChatOpenAI(model='mistral', temperature=0.7, base_url='http://localhost
:1234/v1/chat/completions', cache=False)
        prompt_template = PromptTemplate.from_template(
        '{system_prompt
} + '\n' +  {user_input}.')
        chain = LLMChain(llm=LLM, prompt=prompt_template)
        query=chain.run({'system_p
rompt': query_maker_gpt_system_prompt, 'user_input': user_input})
        return query

&#x200B;
```
---

     
 
all -  [ Few-Shot Classification using LangChain  ](https://www.reddit.com/r/LangChain/comments/1b1e1pp/fewshot_classification_using_langchain/) , 2024-02-28-0909
```
Hey everyone, check out this tutorial to understand how Few-Shot Classification (classification with very few labelled s
amples) can be achieved using LangChain's FewShotPromptTemplate https://youtu.be/iWqke_cbapU?si=oyXs7Ex5PctvITra
```
---

     
 
all -  [ Proper Storage Format for Local Retrieval of a ConversationalRetrievalChain QA Object ](https://www.reddit.com/r/LangChain/comments/1b1c85m/proper_storage_format_for_local_retrieval_of_a/) , 2024-02-28-0909
```
I want to store a QA object of type 

    <class 'langchain.chains.conversational_retrieval.base.ConversationalRetrieval
Chain'>

locally. What format should I use to ensure correct retrieval for question answering across different projects?

```
---

     
 
all -  [ What should I learn to get an internship in ML/AI? ](https://www.reddit.com/r/learnmachinelearning/comments/1b1ba2z/what_should_i_learn_to_get_an_internship_in_mlai/) , 2024-02-28-0909
```
I am a 1st year undergrad student. Backstory, I just learnt pandas and have been learning langchain for a while now. I a
m planning of taking CS229 after learning numpy and matplotlib. But my question is what should I learn or what projects 
I should built to get a summer internship? Should I build RAG application or learn something else? Any advice will be he
lpful. Thank you.
```
---

     
 
all -  [ How to load LLMs ](https://www.reddit.com/r/LargeLanguageModels/comments/1b1b96d/how_to_load_llms/) , 2024-02-28-0909
```
Hey there, I am relatively new to working with LLM. So far in order to work with LLMs I've been using libs like langchai
n and ollama that let you load LLM models and use them.

But I wonder how does this libs do that, I've been looking on t
heir repos to understand how does it works, but I wonder if there are some other sources I can take a look on how to do 
that.

I´d like to understand the process it takes to pick the llm file, open it with my code and serve it. Do I go and 
open also the inferences, do I have to tokenize or build my tokenizer first?

thanks a lot!!
```
---

     
 
all -  [ Production ready? ](https://www.reddit.com/r/LangChain/comments/1b194ot/production_ready/) , 2024-02-28-0909
```
Hey guys.  


Some Youtuber criticised LangChain saying it's not production ready. He said the the following: 'It abstra
cts away too many details from you, which makes it super hard to customize for a specific real world use case. Besides, 
it was released before function calling models, so there is no type validation, which is essential in production to prev
ent hallucinations.'  

Do you guys agree here?  


Do you think LangChain can be used in production already or are ther
e crucial steps making LangChain and possibly any other framework a hobby project for now?  


I like the idea of LangGr
aph a lot for example but not sure how much time I should invest here. 
```
---

     
 
all -  [ Deploy Mistral Large to Azure and create a conversation with Python and LangChain ](https://www.reddit.com/r/MistralAI/comments/1b180mk/deploy_mistral_large_to_azure_and_create_a/) , 2024-02-28-0909
```
&#x200B;

https://preview.redd.it/ozoz75uhm3lc1.jpg?width=2400&format=pjpg&auto=webp&s=6a6dc63ed2c78e5e697229cf8616435a8
2f40d9a

[Mistral AI ](https://mistral.ai/)has recently unveiled its most advanced open-source large language model (LLM
) yet, [Mistral Large](https://mistral.ai/news/mistral-large/), alongside its ChatGPT competitor, [Le Chat (beta)](https
://chat.mistral.ai/chat). Le Chat includes other models such as Next, and Small, to let you explore Mistral AI’s capabil
ities. 

This step-by-step guide will show you how to deploy Mistral Large on Azure and start using it immediately with 
LangChain.

[https://neon.tech/blog/deploy-mistral-large-to-azure-and-chat-with-langchain](https://neon.tech/blog/deploy
-mistral-large-to-azure-and-chat-with-langchain)
```
---

     
 
all -  [ Deploy Mistral Large to Azure and create a conversation with Python and LangChain ](https://www.reddit.com/r/LocalLLaMA/comments/1b17xg7/deploy_mistral_large_to_azure_and_create_a/) , 2024-02-28-0909
```
[](https://preview.redd.it/deploy-mistral-large-to-azure-and-create-a-conversation-v0-ozoz75uhm3lc1.jpg?width=2400&forma
t=pjpg&auto=webp&s=12769531183ee8ce311a8a78533b4fbc0491c154)
[Mistral AI ](https://mistral.ai/)has recently unveiled its
 most advanced open-source large language model (LLM) yet, [Mistral Large](https://mistral.ai/news/mistral-large/), alon
gside its ChatGPT competitor, [Le Chat (beta)](https://chat.mistral.ai/chat). Le Chat includes other models such as Next
, and Small, to let you explore Mistral AI’s capabilities. 

This step-by-step guide will show you how to deploy Mistral
 Large on Azure and start using it immediately with LangChain.

[https://neon.tech/blog/deploy-mistral-large-to-azure-an
d-chat-with-langchain](https://neon.tech/blog/deploy-mistral-large-to-azure-and-chat-with-langchain)
```
---

     
 
all -  [ Chat doesn`t provide right url, using SiteLoader ](https://www.reddit.com/r/LangChain/comments/1b0w8su/chat_doesnt_provide_right_url_using_siteloader/) , 2024-02-28-0909
```
Hello,

i\`m using siteloader to read data from sitemap.

The whole chat works great but it doesn\`t provide a right lin
k for the product.

How to get it working?  
this is my code: [https://pastebin.com/wxtutj6c](https://pastebin.com/wxtut
j6c)
```
---

     
 
all -  [ I want a reformatted table as output from a PDF file ](https://www.reddit.com/r/LangChain/comments/1b0nhga/i_want_a_reformatted_table_as_output_from_a_pdf/) , 2024-02-28-0909
```
So I have some PDF files with tables not structured properly. Basically some exported pivot tables from excel so they ar
e spaces in between categories which make it impossible to load this data.

I want to use langchain to solve this. 

So 
far this has mixed results. I tried giving the PDFs directly to ChatGPT 4 but it sometimes misses some columns and some 
times for gets a few rows. 

I am looking for how I can use vectorDB to enhance retrieval? Any suggestions? 
```
---

     
 
all -  [ Creating RAG Evaluation dataset manually: What to consider? ](https://www.reddit.com/r/LangChain/comments/1b0n1c9/creating_rag_evaluation_dataset_manually_what_to/) , 2024-02-28-0909
```
Hi,

I want to manually create a Evaluation dataset for RAG with complex Pdfs. I already tried synthetic dataset creatio
n but think you get more reliable evaluation results with human labeled data (e.g. experts on a specific topic, so they 
knlw which questions they would ask and which answers they would expect).

As human annotation is costly I want to discu
ss important Things to consider when starting.

My plan would be: 
- go through Pdf and Ask 10 questions per document
- 
Answer every question based on the informations from the doc

But how would you evaluate the retriever? You somehow woul
d need to also extract the context (for RAGAS it would be 'ground_truths'). For manual annotation, should the annotator 
just copy the page where the relevant context is inside?

Another interesting thing would be how to answer more complex 
questions, e.g. where the true answer is stored on muliple different pages of the document.

Thanks for all suggestions!

```
---

     
 
all -  [ Sql Agents in Langgraph  ](https://www.reddit.com/r/LangChain/comments/1b0mts2/sql_agents_in_langgraph/) , 2024-02-28-0909
```
Has anyone able to implement sql agent in langgraph,? If so can you please share rhe approach
```
---

     
 
all -  [ using private data with openai + account? ](https://www.reddit.com/r/OpenAI/comments/1b0mgo9/using_private_data_with_openai_account/) , 2024-02-28-0909
```
unfortunately i can't code. I'm looking for a tool that will allow me to use private data and query it with openai + (gp
t 4, LLama, etc.)  


I've looked into langchain but my brain is not smart enough, at the moment to utilize it.   I'm go
ing to try to learn some basic programming skills to at least be able to understand how things work but i'm not there ye
t.  Until then, are there any easy to use programs that are open source, can run on my hardware, and have idiot friendly
 user interfaces available?    


what are some open source options that can help me use my data with LLM's?  


thanks 
for any guidance
```
---

     
 
all -  [ Lang chain alternatives? ](https://www.reddit.com/r/LangChain/comments/1b0mcuk/lang_chain_alternatives/) , 2024-02-28-0909
```

So I’m looking to learn how to build ai systems and bots, mostly self taught for projects and research and not for jobs
 as such, I find Langchain to be exactly what I need but most people I’ve seen say it’s terrible and really pointless fo
r even slightly applications and alternatives should be used 

Any ideas or feedback on what to do?

```
---

     
 
all -  [ Unable to split text received via POST request in django ](https://www.reddit.com/r/django/comments/1b0kxtx/unable_to_split_text_received_via_post_request_in/) , 2024-02-28-0909
```
i am facing a weird error. I am trying to split text sent via form in django.

Here is my code in django

    from trans
formers import AutoTokenizer
    from langchain.text_splitter import CharacterTextSplitter
    tokenizer = AutoTokenizer
.from_pretrained('distilbert-base-uncased-finetuned-sst-2-english' )
    text_splitter = CharacterTextSplitter.from_hugg
ingface_tokenizer(
    tokenizer, chunk_size=256, chunk_overlap=0
    )
    def home(request):
      if request.method =
= 'POST':
         input_text = request.POST['input']  
         print('input_text',type(input_text))
         splitted_
text = text_splitter.split_text(str(input_text))
         print('splitted_text_length_outside',len(splitted_text))

The 
length is always 1, which mean text is not split. I have checked that i am receiving text from html form and the type of
 text is str.

&#x200B;

But when i use the same code outside of django such as in jupyter notebook, it work well and sp
lit the text.

&#x200B;

In django I tried \`input\_text.split()\` and that worked. But i am clueless why the langchain 
text splitter is not working.

&#x200B;

    def home(input_text):
      splitted_text = text_splitter.split_text(input_
text)
      print('splitted_text_length_outside',len(splitted_text))
    

&#x200B;

Here is my html form

    <form act
ion='{% url 'home' %}' method='post' id='myForm'>
{% csrf_token %}
    <textarea name='input' id='input' rows='4' cols='
50'></textarea>
    <br>
<button type='submit'>Submit</button>
    </form>


Here is my ajax code

&#x200B;

    $('#myF
orm').submit(function(event) {
    event.preventDefault();
    let formData = $(this).serialize();
    $.ajax({
    'url
': '/',
    'type': 'POST',
    'data': formData,
    'success': function(response) {
    console.log('success');
    },

    'error': function(error) {
    console.log('error',error);
    }});});
    
```
---

     
 
all -  [ RAG Framework playlist ](https://www.reddit.com/r/LangChain/comments/1b0kwvk/rag_framework_playlist/) , 2024-02-28-0909
```
Check out this playlist that covers
1. What is RAG? RAG framework explained with diagram
2. Multi-Document RAG
3. RAG us
ing persisted Vector DB
4. RAG vs Fine-Tuning
5. Saving & Loading Vector DBs
6. RAG FAQs
7. Analyze PDF, CSV, Youtube vi
deo, json, text and GitHub code using RAG

https://youtube.com/playlist?list=PLnH2pfPCPZsJ1qBbf0Fb7onButMjqYa-Z&si=_NgYV
sZ9QaEdaidC

```
---

     
 
all -  [ Returning source documents ](https://www.reddit.com/r/LangChain/comments/1b0hqkz/returning_source_documents/) , 2024-02-28-0909
```
My current implementation returns source documents for every answer, but it can be very slow (numerous users have also c
ommented on slow response times).  Vercel has an [integration](https://sdk.vercel.ai/docs/guides/providers/langchain) wi
th Langchain that seems to work a little faster, but it doesn't return sources, which is a deal-breaker for me.

My impl
ementation is based partly off of Langchain's [Conversational Retrieval Chain](https://js.langchain.com/docs/get_started
/quickstart#conversational-retrieval-chain), but I'm streaming the response back to the client.  This is the only soluti
on that has worked for me, despite being slow.

I'm also using a Pinecone vector db since my data is custom.  Is there a
 way to improve any part of this architecture to improve response times?
```
---

     
 
all -  [ Lang chain alternatives? ](https://www.reddit.com/r/CodingHelp/comments/1b0h5gl/lang_chain_alternatives/) , 2024-02-28-0909
```
So I’m looking to learn how to build ai systems and bots, mostly self taught for projects and research and not for jobs 
as such, I find Langchain to be exactly what I need but most people I’ve seen say it’s terrible and really pointless for
 even slightly applications and alternatives should be used 

Any ideas or feedback on what to do?

```
---

     
 
all -  [ Scrape any website to markdown for RAG ](https://www.reddit.com/r/LangChain/comments/1b0gw81/scrape_any_website_to_markdown_for_rag/) , 2024-02-28-0909
```
I've just launched [UseScraper.com](https://UseScraper.com) which crawls all the pages from any website to markdown or j
son. I made a short post on using it with langchan [https://usescraper.com/blog/langchain-chatgpt-rag-with-your-website-
content](https://usescraper.com/blog/langchain-chatgpt-rag-with-your-website-content)  

```
---

     
 
all -  [ Processing of PDFs ](https://www.reddit.com/r/LangChain/comments/1b0ezm6/processing_of_pdfs/) , 2024-02-28-0909
```
Hi,

We are doing RAG on ecological reports. Most of them are in PDF format. Much of the data is in tables, often with j
oined cells. I have had a lot of difficulty converting these to a text format that ChatGPT would understand. After tryin
g out all available python libraries for PDF to text, I ended up with pymupdf. I use a lot of tricks to extract the tabl
es (because there are often more than one per page) and then convert them to markdown format. The text snippets are then
 uploaded to Azure Search together with a bunch of metadata. It works ok, but processing takes a little time and Azure S
earch is crazy expensive. 

I just got a GPT4 license and tried uploading a report together with a question related to a
 complicated table in the document. The answer was spot on and processing was very fast. 

We cannot use OpenAI privacy 
reasons, otherwise it would be the best solution for my clients.  Azure's OpenAI API does not allow documents to be uplo
aded and MS copilot studio / graph fails in its answers. 

Is there a solution to this problem that I don't know about? 
Has anyone any idea on how OpenAI manages to process PDFs when all other libraries fail? 

&#x200B;
```
---

     
 
all -  [ Chat History implementation in langGraph ](https://www.reddit.com/r/LangChain/comments/1b0ey9g/chat_history_implementation_in_langgraph/) , 2024-02-28-0909
```
Hello,  
I have been using the chat history class of langchain to manage and save persistently the chat\_history of a ch
atbot application. Now I am exploring the langGraph, and I could only find tutorials about the rag application. Do you t
hink that langGraph is suitable also for creating a RAG chatbot with memory integration? And how can it be done??
```
---

     
 
all -  [ Agents: Large document information spread -- need help ](https://www.reddit.com/r/LangChain/comments/1b0e08l/agents_large_document_information_spread_need_help/) , 2024-02-28-0909
```
I am trying to understand, if its possible to take a large unstructured document and use langchain agents (with Retrieve
r Tool) to collect all the information required from the document. I have not been able to successfully do any end to en
d retrieval from the document, and so much so that the agent is throwing output like this 

'Unfortunately, the metadata
 provided does not include specific account details such as the account number or the provider name. This information mi
ght be available in a different section of the document or on a different document related to the account' 

Its part of
 the same document. Shouldnt this directly be handled by the agent, isnt that why we should use agent to solve such 'ite
rative' problems.Hope I am not over complicating this! Thanks  


    //Standard Agent Code of Langchain -- tools is jus
t a retriever
    
           agent = create_openai_tools_agent(llm=llm,tools=tools,prompt=agent_prompt)
            
  
          message_history = ChatMessageHistory()
            agent_executor = AgentExecutor(agent=agent,tools=tools, ver
bose=True,return_intermediate_steps=True,max_iterations=100)
            agent_with_chat_history = RunnableWithMessageHi
story(agent_executor, lambda session_id: message_history, input_messages_key='input', history_messages_key='chat_history
')

&#x200B;
```
---

     
 
all -  [ How do I improve my codebase reading skills in Python? ](https://www.reddit.com/r/learnpython/comments/1b08wr9/how_do_i_improve_my_codebase_reading_skills_in/) , 2024-02-28-0909
```
**How do I improve my codebase reading skills in Python?** 

For the last 6 months or so I've been learning Python and c
an write decent code using OOP but find it extremely hard to understand somebody else's code. Specifically, I was using 
the Langchain python library to build an MVP tool and since only basic tutorials are available for it, I thought of goin
g through the codebase to understand how more specialized implementation can be done but I got completely lost in the co
de. Couldn't understand a thing. 

This isn't true for just Langchain, I'm unable to understand other codebases in gener
al (I've tried reading python code for other packages but to no avail).

Guidance on this would be really helpful!
```
---

     
 
all -  [ Evaluate different LLMs or flows ](https://www.reddit.com/r/LangChain/comments/1b064fb/evaluate_different_llms_or_flows/) , 2024-02-28-0909
```
Question is self explanatory! Im looking for a workbench or way to evaluate different LLMs. For example giving score to 
answers, comparing prompts, giving good answer samples, etc etc

If it can show me the runs, the better so i can compare
.

Tried mlflow but only works for openai… that is too bad

Thanks is advance!
```
---

     
 
all -  [ [Hiring] Looking for a senior software engineer (25$/hr) ](https://www.reddit.com/r/forhire/comments/1b03uhj/hiring_looking_for_a_senior_software_engineer_25hr/) , 2024-02-28-0909
```
Senior Software Engineer - AI and Cloud Services

Key Responsibilities:

	•	Implement LangChain for advanced language mo
del integration and application development.
	•	Develop and manage databases using PostgreSQL, ensuring optimal performa
nce and reliability.
	•	Utilize Docker for containerization, facilitating consistent development, testing, and deploymen
t environments.
	•	Apply fuzzy matching techniques to enhance data matching and retrieval accuracy.
	•	Design and deploy
 agent-based models for complex simulations and problem-solving.
	•	Integrate semantic search capabilities to improve in
formation discovery and relevance.
	•	Manage and optimize cloud-based infrastructure and services on AWS, leveraging the
 Cloud Development Kit (CDK) for infrastructure as code practices.
	•	Develop applications and services using Python and
 FastAPI, focusing on high performance and scalability.
	•	Work with OpenAI technologies to incorporate cutting-edge AI 
and machine learning features into our products.

Application Process:

To apply, please send your resume and a cover le
tter highlighting your experience with the technologies.

Looking for long-term employees. 
```
---

     
 
all -  [ 🎉Langchain Rust🎉 ](https://www.reddit.com/r/LLMDevs/comments/1b01bee/langchain_rust/) , 2024-02-28-0909
```
I’m thrilled to share a personal project of mine: a Rust port of Langchain. As a core contributor to the official Go Lan
g port of Langchain (langchaingo), I’ve embarked on a new challenge to further my skills by diving into Rust programming
. This project is a standalone effort to reimagine Langchain’s capabilities within the Rust ecosystem, which is renowned
 for prioritizing safety and performance.

Take a look here: https://github.com/Abraxas-365/langchain-rust 

This is a p
ersonal initiative, not an official port, reflecting my ongoing quest to enhance my technical know-how and engage with i
nnovative language model applications. I’m eager to discover what possibilities this project might unlock and I warmly i
nvite you to check out the repository, share your insights, or consider contributing. Your feedback and contributions ar
e not only welcome but also highly valued as they contribute to the enrichment of both the project and the broader commu
nity. Let’s delve into the potential that lies at the crossroads of Rust and AI together!
```
---

     
 
all -  [ Which vectorstore for prosuction?  ](https://www.reddit.com/r/LangChain/comments/1azrzkc/which_vectorstore_for_prosuction/) , 2024-02-28-0909
```
Hi,

Which vectorstore do you like most for production usecases?
At the moment I am using Faiss, is this suitable for pr
oduction? I also heard that PgVector should be nice, what are advantages of it?

Thanks!
```
---

     
 
all -  [ We all hate LangChain, so what do we actually want? ](https://www.reddit.com/r/LocalLLaMA/comments/1azrk8b/we_all_hate_langchain_so_what_do_we_actually_want/) , 2024-02-28-0909
```
I appreciate the anti-langchain post as much as anyone, but in the spirit of optimism, I'd like to talk about what every
one wants to build and improve instead :)

I often hear 'Oh LLMs can do <x> easily, just ...' But once you start buildin
g, the complexities pile up quickly!

So for a fun Sunday discussion, what is your dream framework for working with lang
uage models?

For me, I'm mostly anti-framework these days, and prefer a more building blocks that you can pick and choo
se from. Here's some pain points off the top of my head:

* Context Management: I built a small LLM context manager tool
 to handle chat history, RAG, and other data. It worked well until I built a full app, and now I feel the pain from not 
being able to tweak it for each instance (influence scores easily, order, etc) and determine what was included in the li
mited context.
* Chains/Loops: I built a small-ish chain library so I could write custom prompts and loop them. It's kin
d of useful, but I found that many of the chain 'entries' need to be custom functions to control the flow. Seems nearly 
impossible for someone else to work with haha
* File Import: I used pymupdf since it seemed to give lower-level access t
o PDFs, enough that I could generate markdown w/ headings from files. Extracting images and tables in-line seems difficu
lt, and multi-column pages are a disaster. I'd love a library to convert any document to markdown.
* Chunking: I made a 
custom markdown chunking function so I could break it up by headings and include headings/doc title metadata in the chun
ks. It's still messy and I feel the limitations every time I use RAG.

There are also some higher level problems I'm int
erested in:

Handling chat/rag/agents smoothly - so the LLM will respond quickly when it can, use rag when necessary, an
d use assistant/agent loops otherwise.

Understanding multi-turn RAG/agents. For example, how do you handle a RAG questi
on and then a generic follow up with less context? The first message returns a bunch of results, and the second message 
returns none ('Ok, what's the second part mean?'). Do you keep including the original RAG data in the context, and keep 
filling it with more data as the chat continues? My RAG and assistant chats feel like one-shot instead of smooth convers
ations.

How about everyone else? What do you currently use, what are your pain points, and do you have a dream tool?

I
n the end, do we just have to roll our own custom libraries for each use case?
```
---

     
 
all -  [ OpenAi embedding v3 weird scores ](https://www.reddit.com/r/LangChain/comments/1azr70c/openai_embedding_v3_weird_scores/) , 2024-02-28-0909
```
I have been using ada for a while now with a Faiss store and it has been doing well. 

Today I tried text-embedding-3-la
rge today and the scores are weird. 

The correct match with ada gets a score of ~0.2 (0 being the best match and 1 bein
g the worst match) 
The correct match with text-embedding-3-large gets a score of ~0.5 

The full ordering from score 0-
1 seems to be better than ada. But the there is a shift towards a score of 1. 

Has anyone experienced that? Or has any 
explanation? 
```
---

     
 
all -  [ Best utility library? ](https://www.reddit.com/r/LocalLLaMA/comments/1azoqnl/best_utility_library/) , 2024-02-28-0909
```
There's been a few posts banging on Langchain a bit lately, but I find I do use their utility functions for doc loading,
 text splitting, etc.

What library is the best for these types of helper functions in your opinion?
```
---

     
 
all -  [ Langchain use cases ](https://www.reddit.com/r/LangChain/comments/1azoinv/langchain_use_cases/) , 2024-02-28-0909
```
I’m a software quality engineer and I’ve been tasked with exploring ai use cases for my team. The only thing I could thi
nk was test plan generation by storing our existing test plans in a db and information about products(PRD, public docs e
tc.) and somehow getting the llm to return a test plan draft based on this. Would this even be feasible and worth explor
ing? What other use cases you think could be beneficial to a quality engineering team? I’m an AI noob btw with interest 
in building on top of llm
```
---

     
 
all -  [ Langchain library - the worst 'common functionality' abstraction package out there? ](https://www.reddit.com/r/LocalLLaMA/comments/1azkbnl/langchain_library_the_worst_common_functionality/) , 2024-02-28-0909
```
I've recently had time to dive into the Langchain library for creating a simple chatbot with memory (previously I've jus
t used GPT4 APIs with my own abstractions).

I don't understand, really... Am I stupid or Langchain is completely unusab
le due to the incredible overengineering efforts? Also - wow, documentation and practical examples are soooo terrible!


There's just too much abstraction depth. I don't wanna blame the Langchain devs or anything, it's just my general feelin
g. Also - did I mention how confusing, hard-to-read and unclear the documentation is?

If shooting your foot with a C++ 
gun blows your whole leg off...

I feel that - shooting your foot with Langchain blows your both legs off and, additiona
lly, tears you apart in half.
```
---

     
 
MachineLearning -  [ [D] Graphs + vectordbs? Need your input: Cognee.ai . AI Data Pipelines for Real-World Production (Pa ](https://www.reddit.com/r/MachineLearning/comments/1aweo71/d_graphs_vectordbs_need_your_input_cogneeai_ai/) , 2024-02-28-0909
```
Hey there, Redditors!

I'm back with the latest installment on creating dependable AI data pipelines for real-world prod
uction.

If you've been following along, you know I'm on a mission to move beyond the '[thin OpenAI wrapper](https://top
oteretes.notion.site/Going-beyond-Langchain-Weaviate-and-towards-a-production-ready-modern-data-platform-7351d77a1eba40a
ab4394c24bef3a278?pvs=4)' trend and tackle the challenges of building robust data pipelines.

After a few months of work
, we integrated cognitive architecture with [keepi.ai](https://www.keepi.ai) 

We aim to explore with our demo:

**1. Co
ntext sanitization**  
The world of AI is fast-moving, and we've realized that the context is becoming a building block 
we refer to as a crucial part of future cognitive architecture.  
**2. Best Practices for AI Memory**  
In this rapidly 
evolving landscape, there are no established best practices. You'll need to make educated bets on tools and processes, k
nowing that things will change. We assume that having traditional data engineering practices + frameworks + classifiers 
and other AI solutions can solve a lot of standard hurdles  
**3. AI Frameworks**  
They are trying to do too much, too 
fast, too broad. We want to find a pattern and a correct layer of abstraction for the AI memory to fit new industry.  



&#x200B;

How does it work? 

The Github repo is l:

  


[How cognee works](https://preview.redd.it/yuiabmyihyjc1.png?
width=1633&format=png&auto=webp&s=4384c4441b615f72caf1e0591c5ab23aee735fab)

Github repo is [here](https://github.com/to
poteretes/cognee)

Next steps:  
I have questions for you:

1. Is context sanitization relevant for you?
2. How do you m
anage metadata? 
3. How do you prepare data for LLMs?
4. Are there any data enrichment steps you perform?

Check out the
 blog post:

[Link to part 4](https://topoteretes.notion.site/Going-beyond-Langchain-Weaviate-Level-4-towards-production
-fe90ff40e56e44c4a49f1492d360173c?pvs=4)

*Remember to give this post an upvote if you found it insightful!*  
*And also
 star our* [Github repo](https://github.com/topoteretes/cognee)
```
---

     
 
MachineLearning -  [ [D] AI projects Suggestions ](https://www.reddit.com/r/MachineLearning/comments/1aunkmw/d_ai_projects_suggestions/) , 2024-02-28-0909
```
Hi Everyone, I need a suggestion to create AI courses for students ( Hands-on AI projects). I am thinking about the late
st AI trends such as Langchain, RAG, and vector databases. In each project, there can be multiple tasks, and the main th
ing is each task should have an automated system in which we can verify whether students have done it correctly or not.


For example: Project with visualization cannot be automatically tested. 

For example: A project with visualization can
not be automatically tested. . em can verify if the length of the text is smaller we can verify that it is correct.
```
---

     
 
MachineLearning -  [ Whats in your RAG setup? [D] ](https://www.reddit.com/r/MachineLearning/comments/1apcp2w/whats_in_your_rag_setup_d/) , 2024-02-28-0909
```
What frameworks and libraries are you using in your RAG? 

I'm most curious if  LangChain is as popular as it was?

Here
's mine at a high-level: 

*  langchain to use OpenAI for creating embeddings
* Pinecone for storing embedding
* langcha
in to load document splitters and characters splitters for chunking
* Mongo for conversations memory

&#x200B;
```
---

     
 
MachineLearning -  [ [D] What's the best current RAG setup that would work with a local LLM? ](https://www.reddit.com/r/MachineLearning/comments/1ag6bo7/d_whats_the_best_current_rag_setup_that_would/) , 2024-02-28-0909
```
I've tried things like langchain in the past (6-8 months ago) but they were cumbersome and didn't work as expected.

I  
need RAG to get data from various pdfs (long one, 150+ pages) - and i  need a setup that will allow me to add more and m
ore data sources.

I wanna run this locally, can get a 24gb video card (or 2x16gb ones) - so i can run using 33b or smal
ler models.

I  know things in the industry change every 2 weeks, so i'm hoping there's  an easy and efficient way of do
ing RAG (compared to 6 months ago)
```
---

     
 
MachineLearning -  [ [P]: Anukool: My job hunting assistant ](https://www.reddit.com/r/MachineLearning/comments/1adu3tw/p_anukool_my_job_hunting_assistant/) , 2024-02-28-0909
```
Hey Reddit, I've been applying for jobs and found that writing a cover letter for each position was tedious. I also delv
ed into LLM and Langchain, hoping to leverage them for a project to aid in my job hunting. So, I developed Anukool under
 the GPL license. While it's far from perfect, it has proven very useful to me, and I hope it benefits you as well. All 
I have to do is provide it with a pdf containing information about me such as my experience, skills, projects, etc and i
t will use this information along with job description to generate cover letter for me. Since I'm new to ML and LLM, any
 advice or feedback is greatly appreciated, and contributions are also welcome. I plan to utilize Llama-2 soon to furthe
r open-source the project.

Check out the GitHub link, and please star it if you find the project interesting: https://g
ithub.com/dakshesh14/anukool
```
---

     
 
deeplearning -  [ [D] WebVoyager: Navigating Digital Cosmos with LangGraph & Multimodal Models ](https://www.reddit.com/r/deeplearning/comments/1altlca/d_webvoyager_navigating_digital_cosmos_with/) , 2024-02-28-0909
```
Embark on a journey through the digital cosmos with WebVoyager, a groundbreaking Large Multimodal Model (LMM) web agent 
designed to navigate the vastness of the online universe. In collaboration with Langchain, WebVoyager represents a parad
igm shift in autonomous web agents, seamlessly integrating visual and textual information to complete user instructions 
end-to-end by interacting with real-world websites.

Link: [https://medium.com/@andysingal/webvoyager-navigating-digital
-cosmos-with-langgraph-multimodal-models-dace64196c2f](https://medium.com/@andysingal/webvoyager-navigating-digital-cosm
os-with-langgraph-multimodal-models-dace64196c2f)
```
---

     
 
deeplearning -  [ [D] Langchain Elevates with Step-Back Prompting using RAGatouille ](https://www.reddit.com/r/deeplearning/comments/1agtyeh/d_langchain_elevates_with_stepback_prompting/) , 2024-02-28-0909
```
In the dynamic realm of natural language processing, a revolutionary synergy has emerged between Langchain and Step-Back
 Prompting. This article delves into the transformative collaboration, exploring how Langchain’s cutting-edge platform i
ncorporates Step-Back Prompting to redefine language processing capabilities. Join us on a journey of innovation and dis
covery as we unravel the intricacies of this powerful integration. As we explore the uncharted territories of language m
odels, Step-Back Prompting stands as a beacon of progress, promising a journey of nuanced understanding and elevated per
formance in the world of Large Language Models. Welcome to the future of language processing, where inspiration and inno
vation converge in a symphony of words and ideas.

Link: https://medium.com/ai-advances/langchain-elevates-with-step-bac
k-prompting-using-ragatouille-b433e6f200ea
```
---

     
 
deeplearning -  [ Become an AI Developer (Free 9 Part Series) ](https://www.reddit.com/r/deeplearning/comments/1afgp2r/become_an_ai_developer_free_9_part_series/) , 2024-02-28-0909
```
Just sharing a free series I stumbled across on Linkedin - DataCamp's 9-part AI code-along series.

This specific sessio
n linked below is 'Building Chatbots with OpenAI API and Pinecone' but there are 8 others to have a look at and code alo
ng to.

*Start from basics to build on skills with GPT, Pinecone and LangChain to create a chatbot that answers question
s about research papers. Make use of retrieval augmented generation, and learn how to combine this with conversational m
emory to hold a conversation with the chatbot. Code Along on DataCamp Workspace:* [*https://www.datacamp.com/code-along/
building-chatbots-openai-api-pinecone*](https://www.datacamp.com/code-along/building-chatbots-openai-api-pinecone)

Find
 all of the sessions at: [https://www.datacamp.com/ai-code-alongs](https://www.datacamp.com/ai-code-alongs)
```
---

     
 
deeplearning -  [ DSPy Explained! ](https://www.reddit.com/r/deeplearning/comments/1adypks/dspy_explained/) , 2024-02-28-0909
```
DSPy is the next big advancement for AI and building applications with LLMs!

Pioneered by frameworks such as LangChain 
and LlamaIndex, we can build much more powerful systems by chaining together LLM calls! This means that the output of on
e call to an LLM is the input to the next, and so on. We can think of chains as programs, with each LLM call analogous t
o a function that takes text as input and produces text as output.

DSPy offers a new programming model, inspired by PyT
orch, that gives you a massive amount of control over these LLM programs. Further the Signature abstraction wraps prompt
s and structured input / outputs to clean up LLM program codebases.

DSPy then pairs the syntax with a super novel compi
ler that jointly optimizes the instructions for each component of an LLM program, as well as sourcing examples of the ta
sk.

Here is my review of the ideas in DSPy, covering the core concepts and walking through the introduction notebooks s
howing how to compile a simple retrieve-then-read RAG program, as well as a more advanced Multi-Hop RAG program where yo
u have 2 LLM components to be optimized with the DSPy compiler! I hope you find it useful!

https://www.youtube.com/watc
h?v=41EfOY0Ldkc
```
---

     
