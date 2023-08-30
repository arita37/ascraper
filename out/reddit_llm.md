 
all -  [ Logistical tips for testing a fine-tuned model ](https://www.reddit.com/r/GPT3/comments/164xyqk/logistical_tips_for_testing_a_finetuned_model/) , 2023-08-30-0909
```
Hello all! I am relatively new to all of this so please forgive any questions asked in complete ignorance.

I am current
ly using LangChain to fine-tune a gpt-3.5 model. I am doing this by separating my data into training and testing sets. T
he data I am using is in a CSV, and both the training and testing sets are very large in their own rights.

My concern i
s that when I test how well the model predicts for each instance in the testing set, I am going to burn through my usage
 cap for the month. And if the test doesn't yield the results I need, I am going to have to do this all over again after
 making the needed adjustments. 

This is especially a problem because the product my company sells uses the same OpenAI
 account that I am using to test my data. If I burn through our available usage, clients will be unable to make API call
s for the rest of the month via our product.

I have a strong feeling that I am doing this completely wrong. Any advice 
that anyone can provide would be greatly appreciated. Thank you!
```
---

     
 
all -  [ This 'Self Aware' Github Repo Taught Me More About Code in 5 Minutes Than Months Of Online Tutorials ](https://v.redd.it/pod8wflxp4lb1) , 2023-08-30-0909
```

```
---

     
 
all -  [ Advice for writing prompt that might return nothing (help pls 🙏) ](https://www.reddit.com/r/ChatGPTPromptGenius/comments/164u21l/advice_for_writing_prompt_that_might_return/) , 2023-08-30-0909
```
Using gpt3.5turbo api via langchain for a class project to find a specific mailing address that might be in a short docu
ment. The reason I am using gpt is that the input documents are differently formatted each time and may contain abbrevia
tions or typos. I have a list of potential mailing addresses that can be contained in the document and if none of them m
atch/correlate, I want to return a blank array \[\]. I want to achieve very low false positive rate, how can I tailor a 
prompt given the input document and list of mailing addresses to return an empty array when nothing is found to be corre
lating?
```
---

     
 
all -  [ ConversationalRetrievalChain [got multiple argument for question_generator] ](https://www.reddit.com/r/LangChain/comments/164smjc/conversationalretrievalchain_got_multiple/) , 2023-08-30-0909
```
Getting error: got multiple values for keyword argument- question\_generator .

&#x200B;

**return cls(\\nTypeError: lan
gchain.chains.conversational\_retrieval.base.ConversationalRetrievalChain() got multiple values for keyword argument \\'
question\_generator\\'', 'SystemError'**

&#x200B;

Qtemplate = (  
'Combine the chat history and follow up question int
o '  
'a standalone question. Chat History: {chat\_history}'  
'Follow up question: {question} withoud changing the real
 meaning of the question itself.'  
)  
 CONDENSE\_QUESTION\_PROMPT = PromptTemplate.from\_template(Qtemplate)  
 questi
on\_generator\_chain = LLMChain(llm=OpenAI(openai\_api\_key=openai.api\_key), prompt=CONDENSE\_QUESTION\_PROMPT)  
 chai
n = ConversationalRetrievalChain.from\_llm(  
llm=llm,  
retriever=self.vector\_store.as\_retriever(),  
combine\_docs\_
chain\_kwargs=chain\_type\_kwargs,  
verbose=True,  
return\_source\_documents=True,  
get\_chat\_history=lambda h: h,  

memory=window\_memory,  
question\_generator=question\_generator\_chain

)
```
---

     
 
all -  [ How would you solve for this use-case? ](https://www.reddit.com/r/LangChain/comments/164qfyo/how_would_you_solve_for_this_usecase/) , 2023-08-30-0909
```
Hi all. I have a scoring system against a set of environmental criteria and I apply this to a company, by looking at the
ir annual report/sustainability disclosure. Normally, this is a manual effort which involves a lot of ctrl + f and going
 through PDFs to source information. So, I have implemented RAG against GPT-4 and using Retrieval QA to ask basic questi
ons which works and definitely helps speed up the process of finding information, but I'd love to be able to make the wh
ole end-to-end process automated so an LLM can score a client.

I outline an example of the scoring criteria below:

Cat
egory: Green spending

Score 1 - The client has quantified plans to spend money on reducing their emissions in the next 
two years.

Score 2 - The client has plans to spend money on reducing emissions but has not quantified this.

Score 3 - 
The client has no plans to spend money to reduce emissions.

So how would I put this in an Instruct Tune format I use fo
r a Llama model?

Instruction:

Score the client from 1-3 based on the following criteria.

Score 1 - The client has qua
ntified plans to spend money on reducing their emissions in the next two years.

Score 2 - The client has plans to spend
 money on reducing emissions but has not quantified this.

Score 3 - The client has no plans to spend money to reduce em
issions.

Output:

Insert model answer here for one of the scores.

Repeat this so each score has a model answer across 
the categories.

There are about 15 categories, and I could generate 1,000-2,000 examples across the various combination
s of score and category.

My plan would then be to use this fine-tuned model in RAG, and ask it to score British Petrole
um on Green Spending by accessing the documents.

1. Does this sound like a sound strategy?
2. Is there a limit to the t
okens that can be in an instruction?

Thanks!
```
---

     
 
all -  [ Block answer if no source documents retrieved. ](https://www.reddit.com/r/LangChain/comments/164pdn2/block_answer_if_no_source_documents_retrieved/) , 2023-08-30-0909
```
I am currently using the RetrievalQA chain with similarity search and a score threshold. However, there are instances wh
ere no documents are retrieved. In such cases, I would like the LLM to respond with 'answer not available' or not respon
d at all. I don't want to use prompt engineering but instead am looking for a deterministic solution. Although one way t
o handle this would be to capture the response, check for source\_documents, and then handle it appropriately, this is n
ot feasible for me as I am streaming the answers and cannot check for source\_documents in real-time.

I am curious to k
now if others have encountered this issue and found a solution. I have already checked the documentation and the source 
code for any relevant arguments but found nothing.
```
---

     
 
all -  [ Looking for a ChromaDB Client Similar to pgAdmin or MongoDB Studio ](https://www.reddit.com/r/LangChain/comments/164ofnm/looking_for_a_chromadb_client_similar_to_pgadmin/) , 2023-08-30-0909
```
I am currently working with ChromaDB for a project and I'm in need of a user-friendly client tool that can provide a gra
phical interface for managing and interacting with my ChromaDB instance. Much like pgAdmin for PostgreSQL and MongoDB St
udio for MongoDB, I'm hoping to find a dedicated client that offers features like browsing, querying, and modifying data
, as well as managing database configurations.

If anyone is aware of a ChromaDB client that fits this description, I wo
uld greatly appreciate your recommendations. Open-source options are preferred, but any suggestions for reliable client 
tools that streamline ChromaDB administration would be incredibly valuable. Thank you in advance for your assistance!
```
---

     
 
all -  [ 📢 Check out this exclusive free webinar on building a powerful app to interact with your Salesforce  ](https://www.reddit.com/r/machinelearningnews/comments/164nia0/check_out_this_exclusive_free_webinar_on_building/) , 2023-08-30-0909
```
🔥 Highlights:

✅ Dive deep into PLG & understand campaign efficiency.

✅ Hands-on session powered by Langchain & a vecto
r database.

✅ Ensure privacy & security for your internal data.

✅ Handle multi-model data from varied sources seamless
ly.

[🔗 Register now and stay ahead of the curve!](https://www.singlestore.com/resources/webinar-chatgpt-for-plg-talk-wi
th-your-salesforce-or-segment-data-08-2023/?utm_source=asif-razzaq&utm_medium=influencer&utm_campaign=ChatGPT-for-PLG-Ta
lk-With-Your-Salesforce-or-Segment-Data&campaignid=7014X000002ep0hQAA)
```
---

     
 
all -  [ Deep Evals - Open Source Python Package for Unit Testing LLMs ](https://www.reddit.com/r/opensource/comments/164n7uj/deep_evals_open_source_python_package_for_unit/) , 2023-08-30-0909
```
[https://github.com/confident-ai/deepeval](https://github.com/confident-ai/deepeval)

Hey everyone 😊,I created an open s
ource python package called Deep Evals that helps developers unit test their LLM implementations (for example, a custome
r support chatbot built using LangChain vs lLamaIndex). This helps you quickly iterate and improve on your LLM implement
ation as you can now more easily identify areas that aren't performing as expected.

Unlike a lot of current approaches,
 we don't use LLMs to evaluate itself ✅. Instead, our package compares expected outputs (which are derived from your kno
wledge bases, such as your company's internal documents), against the actual output of your LLM implementation based on 
metrics you care about. This comparison is done using off the shelf models based on research, and the type of metrics in
clude things like factual consistency, answer relevancy, bias-ness, toxicity, and more. (you can find more information h
ere: [https://docs.confident-ai.com/docs/framework](https://docs.confident-ai.com/docs/framework))

&#x200B;

Here are s
ome features we currently offer:

* integration with Pytest (perfect for an ML engineer's workflow)
* out-of-the-box eva
luation metrics (see above for more detail)
* integration with lLamaIndex (in progress)
* integration with LangChain (in
 progress)
* CLI
* A web platform for anyone to view log and view test results ([app.confident-ai.com](https://app.confi
dent-ai.com))

&#x200B;

We currently also have a lot on the roadmap, which includes:

* adding more out-of-the-box metr
ics
* synthetic data generation (this helps developers save time as they don't have to prepare evaluation datasets)
* ou
tput clustering and classification (this helps developers identify what use cases need more attention)
* integration wit
h LangChain
* integration with lLamaIndex

&#x200B;

We built Deep Evals because I realized I was wasting a lot of time 
eyeballing LLM outputs and I wasn't confident in the chatbot I was building at the time (it was kinda flaky).I wanted to
 put this here because I feel this is a great project to contribute to if you enjoy ML, even if you're just getting star
ted in ML and/or contributing to OS. The project is still fresh so relatively easy to get started, and bits related to M
L is relatively isolated, especially if you're looking to add a new metric!

Thanks for reading this long post, comment 
below for any questions and feel free to comment / DM if you're interested in helping out! 😊
```
---

     
 
all -  [ Is my way of use a MapReduceDocumentsChain correct please? ](https://www.reddit.com/r/LangChain/comments/164lt2h/is_my_way_of_use_a_mapreducedocumentschain/) , 2023-08-30-0909
```
Hi!

I have a list of small markdown chunks in a folder, about 30, that I load in a list using the \`\`\`UnstructuredMar
kdownLoader\`\`\`. Some of these chunks contain information about some tools, and some don't. So this gives me a list of
 Documents. I want to use a Map Reduce chain on them to answer some questions. So my Map Reduce chain is similar to the 
[MapReduceDocumentsChain API documentation](https://api.python.langchain.com/en/latest/chains/langchain.chains.combine_d
ocuments.map_reduce.MapReduceDocumentsChain.html#langchain.chains.combine_documents.map_reduce.MapReduceDocumentsChain):


\`\`\`

query = 'Give me the name of the presented manufacturing tool in this text as well as its usage and number of 
cycles before fatigue breaks it.'

llm = ChatOpenAI(model\_name = 'gpt-3.5-turbo-16k', openai\_api\_key = openai\_api\_k
ey)

\# This prompt defines the answer that we ask about each chunk

prompt = PromptTemplate.from\_template(

'''{questi
on}. Use the following text to answer the question:

{context}  
If the text isn't enough to answer the question, return
 nothing, an empty string.

''',

partial\_variables = {'question': question})

\# The map chain that will apply the pro
mpt to each one of the chunks

map\_chain = LLMChain(llm = llm, prompt = prompt)

\# This is the variable that is used i
n the reduce prompt to indicate where will be the results of the         # formating  
document\_variable\_name = 'conte
xt'  
\# This prompt defines how we combine the documents  
reduce\_prompt = PromptTemplate.from\_template(  
'''We have
 the following question: {question}. We have extracted the following texts to help answer it:  
{context}''',

partial\_
variables = {'question': question})

  
reduce\_llm\_chain = LLMChain(llm = llm, prompt = reduce\_prompt)  
\# How we fo
rmat each document before reducing  
document\_prompt = PromptTemplate.from\_template(  
'''From this following text ret
urn a JSON that satisfies this question: '{question}'.  
If there is no data just return an empty string.  
{page\_conte
nt}''',  
partial\_variables = {'question': question})  
\# This is chain formats the results of the map chain, and comb
ines them using the reduce\_llm\_chain  
combine\_documents\_chain = StuffDocumentsChain(  
llm\_chain = reduce\_llm\_ch
ain,  
document\_prompt = document\_prompt,  
document\_variable\_name = document\_variable\_name  
)  
\# This chain is
 an abstraction over the concept of Reduce Chains  
reduce\_chain = ReduceDocumentsChain(  
combine\_documents\_chain = 
combine\_documents\_chain,  
token\_max = 15000  
)  


\# The final Map Reduce chain

chain = MapReduceDocumentsChain( 
 
llm\_chain = map\_chain,  
reduce\_documents\_chain = reduce\_chain,  
)

[chain.run](https://chain.run)(chunks) # Her
e chunks in a list of Document that have page\_content and metadata

\`\`\`

I don't know if I am doing something wrong,
 but my results seem to vary a lot from one run to another. Sometimes I get a JSON about almost all the tools in my chun
ks that have an understandable structure. Some other times I get a JSON about just two or three tools. Often I get 'I co
uldn't find what you're asking for' or something in the lines. Sometimes I get an empty JSON with an unfinished structur
e.

I'd be really grateful if someone can confirm if what I'm doing is correct and fitting for what I want to do (extrac
t data from a bunch of chunks without using a retriever).  

```
---

     
 
all -  [ Free Development and Usage of Document GPT (This can be asked, unlike ChatGPT!) ](https://www.reddit.com/r/LangChain/comments/164ihsk/free_development_and_usage_of_document_gpt_this/) , 2023-08-30-0909
```
## Creating a Document GPT with OpenAI API for Free

Some time ago, I shared how to build a document GPT application usi
ng `Langchain` and `Streamlit`, which you can refer to in the [previous article](https://www.reddit.com/r/LangChain/comm
ents/14vwv63/chatpdf_what_chatgpt_cant_do_this_can/).

As we all know, using the OpenAI API requires an API key, especia
lly when implementing a document GPT with Langchain, which can lead to substantial API usage. This has deterred many peo
ple and prevented most users from experiencing the application.

There is an open-source project on GitHub called [`gpt4
free`](https://github.com/xtekky/gpt4free) that allows you to utilize the OpenAI GPT model without needing an OpenAI API
 key.

This enables us to create a completely free document GPT. We simply need to modify the LLM calls in Langchain to 
use `gpt4free`.

* Source code and setup: [GitHub Repository](https://github.com/Lin-jun-xiang/docGPT-streamlit)
* Appli
cation: [DocGPT App](https://docgpt-app.streamlit.app/)

Comparison between using OpenAI API (paid) and `gpt4free` (free
):

https://preview.redd.it/fgrbcefww1lb1.png?width=957&format=png&auto=webp&s=8c99ee4d10cb9240b806de9007ba0788b13712d7


About `gpt4free`:

* When using `gpt4free`, it has several [different Providers](https://github.com/xtekky/gpt4free#mod
els), each with varying statuses. Sometimes you may not be able to use it properly, so remember to switch!
* It's recomm
ended to use Python version 3.9 or above (3.8 won't work).
* Additionally, `gpt4free` includes a disclaimer, suggesting 
not to use this technology for corporate projects to avoid potential issues.
```
---

     
 
all -  [ How are you guys generating massive vector bases? ](https://www.reddit.com/r/LangChain/comments/164f508/how_are_you_guys_generating_massive_vector_bases/) , 2023-08-30-0909
```
I apologize if this seems like a rookie question; 

But the state of ingestion just takes forever. I haven’t the patienc
e to wait hours for massive amounts of data to be embedded and then ingested. I am familiar with chunking the documents 
before loading, preprocessing text, then nlp chain/ split/ chunk/ token / embed. I’ve used activeloops compute engine, a
nd colabs high-ram and/or a100 gpu. It takes forever. 

So, aside from slowly ingesting documents over time. How the hel
l do people get such large databases? 

secondary question; does performance improve with the size of the db/ quantity o
f vectors? Ie; should I stuff everything into a single vectorstore and that’s better at finding the specific  informatio
n, or separate vector stores for individual topics/categories? 

my answer is yes to the vectorstore size based on my kn
owledge to date.
```
---

     
 
all -  [ Prompt Engineering Seems Like Guesswork - How To Evaluate LLM application properly? ](https://www.reddit.com/r/LangChain/comments/164ey51/prompt_engineering_seems_like_guesswork_how_to/) , 2023-08-30-0909
```
How are folks evaluating the quality of your LLM applications? I'm running a mental health chatbot in production (small 
scale - 10's of active users) and I've spent a lot of time finetuning prompts but it's all just guesswork. 

I'll make a
 tweak to the prompt and run a few test conversations and just kinda get the vibes of whether it's better or worse than 
before the tweak. Is this what y'all are doing too or am  I missing something???
```
---

     
 
all -  [ What tools or frameworks do you use to make AI-based products or features? ](https://www.reddit.com/r/Startup_Ideas/comments/164esrw/what_tools_or_frameworks_do_you_use_to_make/) , 2023-08-30-0909
```
Hi, I built [TreeScale.com](https://TreeScale.com).  
I wanted to discuss what tools or frameworks you use to make an AI
 or LLM-based feature for your product, like text generators or chatbots.  
Based on my research and client conversation
s, most developers use LangChain to make their Large Language Model-based product features. Still, as a developer, I und
erstand that writing text-based prompts into the text is not sustainable in the long term.  
What are your preferences t
here?
```
---

     
 
all -  [ What do you use for building AI/LLM Product features? ](https://www.reddit.com/r/webdev/comments/164embi/what_do_you_use_for_building_aillm_product/) , 2023-08-30-0909
```
Hi, I built [TreeScale.com](https://TreeScale.com). 

I wanted to discuss what tools or frameworks you use to make an AI
 or LLM-based feature for your product, like text generators or chatbots.

Based on my research and client conversations
, most developers use LangChain to make their Large Language Model-based product features. Still, as a developer, I unde
rstand that writing text-based prompts into the text is not sustainable in the long term.

What are your preferences the
re?
```
---

     
 
all -  [ Incoming EE/CE Freshman looking for CS Summer Internships ](https://www.reddit.com/r/resumes/comments/164bz13/incoming_eece_freshman_looking_for_cs_summer/) , 2023-08-30-0909
```
My grad date is 2026 b/c I've seen most employers don't like freshman and I technically have sophmore standing b/c AP cr
edits.  

https://preview.redd.it/zp9f217s70lb1.png?width=1700&format=png&auto=webp&s=d9eb94b18b53f57fe9bbd589362f242820
b76596

Other Questions:  
 I have like 4 other unmentioned projects on my website, what types of projects should I be i
ncluding on my resume?  (Ones I put the most effort into vs. maximizing buzz words / paragraph lmao).  

I'm going into 
college this year so I don't have any college clubs / classes.  Should I try to include a HS cybersecurity club I was pa
rt of, or are projects more important.

Are certs worth anything in this field, or are projects still prioritized? 
```
---

     
 
all -  [ Have the VCs decided not to fund newer search related startups ? ](https://www.reddit.com/r/ycombinator/comments/1649fis/have_the_vcs_decided_not_to_fund_newer_search/) , 2023-08-30-0909
```
Preamble- Not building a langchain wrapper.

We bootstrapped a startup, building AI SAAS product for Enterprise customer
s. It is a combination of multiple LLM capabilities under one roof, including enterprise chatgpt like product (numerous 
LLMs added to it, including open source ones) and complex search Webagent.  Our revenue went from 0 to 300k in less than
 two months without any marketing spend. Up until two weeks ago we had a very strong VC interest and had five commitment
s for funding. However, since last week - 4 of the VCs have pulled out.

This space has been hot for a while .Is there s
omething happening that we I might not be aware of, I know the recent update from open AI but is there a specific insigh
t or discussion that is causing the VCs to be more cautious?
```
---

     
 
all -  [ Is there a way to print out the full prompt that the chain is sending to OpenAI API? ](https://www.reddit.com/r/LangChain/comments/1643z8k/is_there_a_way_to_print_out_the_full_prompt_that/) , 2023-08-30-0909
```
I have to go to the source code to look for the prompt langchain uses, such as [https://github.com/langchain-ai/langchai
n/blob/master/libs/langchain/langchain/agents/agent\_toolkits/pandas/prompt.py](https://github.com/langchain-ai/langchai
n/blob/master/libs/langchain/langchain/agents/agent_toolkits/pandas/prompt.py) here for the pandas agent. Does anyone kn
ow how to print out the full prompt? 

When I create the agent using verbose=True, it does not print the full prompt. 


\`\`\`

agent = create\_pandas\_dataframe\_agent(  
ChatOpenAI(temperature=0, model='gpt-3.5-turbo-0613'),  
df,  
verbo
se=True,  
agent\_type=AgentType.OPENAI\_FUNCTIONS,  
)

\`\`\`

Thanks for the help.
```
---

     
 
all -  [ Is LangChain the right tool to interact with a LLM for large number of private data? ](https://www.reddit.com/r/LangChain/comments/1641ou4/is_langchain_the_right_tool_to_interact_with_a/) , 2023-08-30-0909
```
classical fine-tuning a 70b LLM is very compute expensive. Can the community suggest how a can train a LLM with a very l
arge private dataset? Would LangChain be the solution if I have say 100,000 product specs that I want the LLM to referen
ce? I image with LangChain it would not work as a typical Llama2 context window is 4k tokens.

Thank you in advance, ple
ase correct me if my understanding of how langchain works is incorrect.
```
---

     
 
all -  [ Best agent type for “Master” slack agent? ](https://www.reddit.com/r/LangChain/comments/163x9nk/best_agent_type_for_master_slack_agent/) , 2023-08-30-0909
```
Hey, I’m trying to make a “master” agent that users will interact with via slack. It will have access to tools, plus oth
er agents and chains as tools (like little assistants it can call on). It also needs to be conversational with shared me
mory across agents and tools. 

Which agent type is best to accomplish this?
```
---

     
 
all -  [ Chat with your database: GraphQL API + Langchain ](https://www.reddit.com/r/graphql/comments/163nkwn/chat_with_your_database_graphql_api_langchain/) , 2023-08-30-0909
```
Has anyone worked with Langchain to apply LLM on top of a database? 

Im currently building an application with ChatGPT 
on top of a MongoDB with GraphQL in LangChain.

[https://python.langchain.com/docs/integrations/tools/graphql](https://p
ython.langchain.com/docs/integrations/tools/graphql)
```
---

     
 
all -  [ Create a lesson from a chapter of a book or pdf? ](https://www.reddit.com/r/LangChain/comments/163my1m/create_a_lesson_from_a_chapter_of_a_book_or_pdf/) , 2023-08-30-0909
```
Hello everyone, 

I'd trying to generate 'lessons' from a text doc (or pdf). 

Basically to create a content to help peo
ple learn a topic. 

Let's say it's Accounting. And I want to create a lesson on chapter 2. 

I though that I could use 
LC for this. I.E. ingest chapter into vector DB embeddings. / GPT-4

I used RetrievalQAChain then with a prompt such as 
'You are a helpful teacher on Accounting. Summarise the important parts of the chapter 2 ‘Introduction to Financial Stat
ements'. Include information, important examples and key concepts'.

But what I get back is not a lesson. It's more a fe
w short sentences of text or very high level summary of the chapter'. 

Does anyone know of a better way of achieving th
is? 

many thanks 

&#x200B;

&#x200B;
```
---

     
 
all -  [ Conversation Bot on CSV ](https://www.reddit.com/r/LangChain/comments/163gl7t/conversation_bot_on_csv/) , 2023-08-30-0909
```
Hello All, I am trying to create a conversation chatbot that can converse on csv/excel file. I have used embedding techn
iques just like the normal docs but I don't think this work well for structured data. I have used pandas agent as well c
sv agent which performed for most of the csv. But when the csv structure is different it seems to fail. Sometimes starts
 hallucinating.   
What I meant by different structure is that the csv/excel might be containing multiple columns header
 after few rows. I know this is kind of contrary on how to save a csv but the users might upload file like these(edge ca
ses). Need some ideas on how to handle this situation. Also for maintaining the conversation I am storing the chat have 
created a prompt which takes all the conversations and curate a question which can be run by csvAgent.  
Please help or 
share some suggestion on this problem. Thanks
```
---

     
 
all -  [ Js langchain for documents ](https://www.reddit.com/r/LangChain/comments/163do7e/js_langchain_for_documents/) , 2023-08-30-0909
```
Do you know any opensource project in js or node that can chat with documents ?
I am really interested to learn the fram
ework and a good idea is to start with an open source project.
Thanks in advance
```
---

     
 
all -  [ Unexpected behavior: get_relevant_documents() ](https://www.reddit.com/r/LangChain/comments/163d80b/unexpected_behavior_get_relevant_documents/) , 2023-08-30-0909
```
Is anyone else facing issues with case-sensitive queries? I've set all my metadata to lowercase and used the lower() met
hod to transform the query to lowercase as well. Although the modified query AND metadata prints as lowercase, when I pa
ss the modified query to the get_relevant_documents function, the value extracted from the query to search through metad
ata reverts back to its original case, with the initial letter capitalized. As a result, the function returns no matches
 because it's looking for 'Dog' while my metadata is stored as 'dog'. Does anyone have a workaround for this problem?
```
---

     
 
all -  [ AgentExecutor Chain running multiple times ](https://www.reddit.com/r/learnpython/comments/163cqb6/agentexecutor_chain_running_multiple_times/) , 2023-08-30-0909
```
I have created a chatbot using Langchain that uses RetrievalQAwithSourcesChain to answer questions, however if I ask the
 chatbot a question (refer 1 in image), it runs the AgentExecutor, gives the answer and automatically creates another Ag
entExecutor chain with the same query (refer 2 in image), this happens even when I have asked the question just once
```
---

     
 
all -  [ AgentExecutor running multiple times ](https://www.reddit.com/r/LangChain/comments/163cob5/agentexecutor_running_multiple_times/) , 2023-08-30-0909
```
I have created a chatbot that uses RetrievalQAwithSourcesChain to answer questions, however if I ask the chatbot a quest
ion (refer 1 in image), it runs the AgentExecutor, gives the answer and automatically creates another AgentExecutor chai
n with the same query (refer 2 in image), this happens even when I have asked the question just once.

https://preview.r
edd.it/3n0nlzhehskb1.jpg?width=934&format=pjpg&auto=webp&s=d3cc46d69fa311761c6dadd619104108c3148369

https://preview.red
d.it/gv93jw7e8skb1.jpg?width=1919&format=pjpg&auto=webp&s=acaff6c740447aecc2974aab328ca82f74cab83f
```
---

     
 
all -  [ GPT-Synthesizer version 0.0.3 is out ](https://www.reddit.com/r/LangChain/comments/163a2qz/gptsynthesizer_version_003_is_out/) , 2023-08-30-0909
```
Hello fellow programmers. We made a new release on our open source software. 

[https://github.com/RoboCoachTechnologies
/GPT-Synthesizer](https://github.com/RoboCoachTechnologies/GPT-Synthesizer)

GPT-Synthesizer is a free tool written on t
op of LangChain to facilitate he process of software design and codebase generation. The new release provides some impro
vements (creating the top/main function for python, creating a log file) as well as a bug fix (regarding the location of
 the workspace folder). Please feel free to take a look. I hope this helps whatever langchain project you are doing. 
```
---

     
 
all -  [ Token Limit Exceeded Error in SQL Database Agent ](https://www.reddit.com/r/LangChain/comments/16361w0/token_limit_exceeded_error_in_sql_database_agent/) , 2023-08-30-0909
```
I am using Langchain / SQLDatabaseChain - when I query small database , everything works fine - however using a decent s
ized database, I get the error below.

Does this mean we can forget about using this for real world situations right now
 (even using  

gpt-3.5-turbo-16k) does not help?

&#x200B;

 This model's maximum context length is 4097 tokens, howeve
r you requested 7944 tokens (6944 in your prompt; 1000 for the completion). Please reduce your prompt; or completion len
gth.' 
```
---

     
 
all -  [ Chat with technical document ](https://www.reddit.com/r/LangChain/comments/163420k/chat_with_technical_document/) , 2023-08-30-0909
```
I am trying to setup an openAI document Q&A. The documents are about technical specifications of a communication protoco
l. chatgpt (3.5-turbo or 4) has already some knowledge about this protocol but does not have the latest updated specific
ations. I wanted to use chatGPT knowledge along with the technical documents provided to get accurate Q&A.

Each PDF doc
ument is divided into sections, subsection, etc… and has a header in every page mentioning the document name and version
.  The document contains also mathematical expressions, tables, and figures. 

So far I used chromadb and openAI embeddi
ng + chatogpt-3.5-turbo for Q&A. Results are good overall but the referencing is usually wrong (sometimes it gives corre
ct information but the document/section referenced is wrong). And sometimes it does not answer the right way. But for mo
re simple questions it’s usually accurate enough. 

- Any idea how to improve the model?
- Does anyone know the best way
 to load/embed a PDF with math equations, tables, and figures?
```
---

     
 
all -  [ Back and forth conversations before a vector search? ](https://www.reddit.com/r/LangChain/comments/1633xw6/back_and_forth_conversations_before_a_vector/) , 2023-08-30-0909
```
I am playing around with [this](https://github.com/mayooear/gpt4-pdf-chatbot-langchain) github project, which takes a us
er question as input and immediately runs a vector search on it to find relevant storied information before delivering a
n answer. 

Say I want the chatbot to allow for some back and forth before it runs the search and retrieval, what is the
 best way to do that? I want to allow for the agent to ask clarifying questions towards the user, and most importantly, 
ask the user if it got the question right before it tries to answer it.

Is there an open source project out there that 
does this? Any difficulties in building something like it? 
```
---

     
 
all -  [ What do people use for production? ](https://www.reddit.com/r/LangChain/comments/16330n0/what_do_people_use_for_production/) , 2023-08-30-0909
```
I've seen various comments on here that langchain is great for prototyping but not production.

What are people using in
stead? Just the raw python libraries like torch & transformers?
```
---

     
 
all -  [ elastic search hybrid search in langchain ](https://www.reddit.com/r/elasticsearch/comments/16324rp/elastic_search_hybrid_search_in_langchain/) , 2023-08-30-0909
```
Hi,

I'm following langchain's tutorial ([https://python.langchain.com/docs/integrations/vectorstores/elasticsearch](htt
ps://python.langchain.com/docs/integrations/vectorstores/elasticsearch)) on using elastic search to do hybrid search for
 both embedding based search and keyword based search. as shown in the following, it seems it issues two queries: one fo
r embedding based search and another for keyword based search and combine them using rank function rrp. Unfortunately, t
he rrp function is not free, right now, I'm still in the stage of prototype and wanted to use free version of elastic se
arch. Is there a way i can use other rank functions or using my own custom script to implement my own ranker ? Or is the
re a way to return all document found and I can rank them externally ? 

Thanks, 

&#x200B;

\`\`\`

db = ElasticsearchS
tore.from\_documents(  
docs,   
embeddings,   
es\_url='http://localhost:9200',   
index\_name='test',  
strategy=Elast
icsearchStore.ApproxRetrievalStrategy(  
hybrid=True,  
 )  
)

\###the search strategy configed as follows: 

{  
 'knn
': {  
 'field': 'vector',  
 'filter': \[\],  
 'k': 1,  
 'num\_candidates': 50,  
 'query\_vector': \[1.0, ..., 0.0\]
,  
 },  
 'query': {  
 'bool': {  
 'filter': \[\],  
 'must': \[{'match': {'text': {'query': 'foo'}}}\],  
 }  
 },  

 'rank': {'rrf': {}},  
}

\`\`\`

&#x200B;
```
---

     
 
all -  [ Reflections after 1 month of LangChain and a question ](https://www.reddit.com/r/LangChain/comments/16312a7/reflections_after_1_month_of_langchain_and_a/) , 2023-08-30-0909
```
Hi!

I've been playing around with LangChain for around a month now. At first, I thought that my first project idea woul
d be simple. I set out to use a PDF document loader with a RetrievalQA chain.  


I've made a lot of progress, but I am 
finding that I can rarely use LangChain. I wonder whether this is a common experience. 

For instance, when naively usin
g the RetrievalQA chain, I noticed that the text chunks it identified as relevant to my query were often missing importa
nt context. I then decided to use Pinecone and create my index using their API, so that I could include metadata along w
ith the embeddings.   


I can now do a similarity search on my Pinecone Index and see that the correct document chunks 
are identified. The metadata contains additional context that's needed to address the query. As a test, I naively pasted
 the search response (text + metadata for each chunk) into a chat.openai prompt window. Now my questions are answered co
rrectly! 

I thought that I would be ready to use LangChain now. I thought that I'd be able to wrap my vectorstore as a 
retriever and then use the RetrievalQA chain. Wrong again. And I'm having trouble figuring out my next steps.   


Here'
s my question:

It'd be great if I could make this work by simply defining a custom prompt template that references Pine
cone metadata along with each document chunk. Is there a way to do this using the RetrievalQA chain? Again, I think I ma
y need to move away from LangChain and do this manually. Maybe I'm missing something....

&#x200B;
```
---

     
 
all -  [ Need help with AI framework. ](https://www.reddit.com/r/OpenAI/comments/162uh97/need_help_with_ai_framework/) , 2023-08-30-0909
```
Hi everyone.
I am trying to create a mental well-being product with GPT's openAI. 
Trying to use Langchain for vectors s
ince the product requires user's medical data. 
Can someone help me with a tutorial or anything similar for managing vec
tors and embeddings. I used to code in c++ 15 years back for 3 years or so. Thanks to GPT I have gone back to coding in 
python and handling API requests with flask. 

Currently I succeeded in creating a simple vector but the conversation fl
ow for my product is based upon clinical conversational model. 
Also I am planning to use whisper for NLP in Hindi(India
n language) so speech to text conversion is also in my plans. 
Some help would be deeply appreciated. 
Thanks in advance
. :)
```
---

     
 
all -  [ Looking to go deeper beyond courses with own project - what might a complex project look like? ](https://www.reddit.com/r/LangChain/comments/162qnfd/looking_to_go_deeper_beyond_courses_with_own/) , 2023-08-30-0909
```
Hey, 

Done a few LangChain courses, and now I think the best way to learn possibilities and limitations is to take on a
n own project as a portfolio piece. Want to do something with complexity. 

Grateful for ideas on what a complex LangCha
in solution might look like, in terms of components and services used, any idea use case problems to solve etc.

Been br
owsing through the LangChain blog for ideas, anywhere else I could look for inspiration?

Thanks!
```
---

     
 
all -  [ What are the best courses on langchain? ](https://www.reddit.com/r/LangChain/comments/162q6rz/what_are_the_best_courses_on_langchain/) , 2023-08-30-0909
```
I am not necessarily looking for a free course.
```
---

     
 
all -  [ Is there a way I can update or delete document from HNSWlib index or FAISS index using javascript. ](https://www.reddit.com/r/LangChain/comments/162hrc5/is_there_a_way_i_can_update_or_delete_document/) , 2023-08-30-0909
```
I have vector store in my computer, i index my documents in vector store and use it for Q&A chatbot. Now few documents g
et updated and few documents get deleted, so I have to do the same in vector store. How can I achieve that, any help? I 
use javascript.
```
---

     
 
all -  [ Inspired in AutoGPT I had released ExpertGPTs ](https://www.reddit.com/r/AutoGPT/comments/16228lh/inspired_in_autogpt_i_had_released_expertgpts/) , 2023-08-30-0909
```
[https://www.reddit.com/r/LangChain/comments/16224v2/experts\_gpts\_using\_langchain/](https://www.reddit.com/r/LangChai
n/comments/16224v2/experts_gpts_using_langchain/)
```
---

     
 
all -  [ Experts GPTs using langchain ](https://www.reddit.com/r/LangChain/comments/16224v2/experts_gpts_using_langchain/) , 2023-08-30-0909
```
I have created this project that is an implementation of langchain to provide an easy way to create chatbots and bot cha
ins using memory - vector db using redis stack -, chat history and some extra tools I believe are usefull, at least for 
me. Happy to get feedback and colaborators.

[https://github.com/andrescevp/expert\_gpts](https://github.com/andrescevp/
expert_gpts)
```
---

     
 
all -  [ What are Langchains biggest issues? ](https://www.reddit.com/r/LangChain/comments/1620zic/what_are_langchains_biggest_issues/) , 2023-08-30-0909
```
I see the framework gaining popularity. But what are the biggest issues that Langchain has?

 What should we be concerne
d with if we adopted this framework?
```
---

     
 
all -  [ Using persistent Chromadb as llm vectorstore for langchain in Python ](https://www.reddit.com/r/LangChain/comments/161zz7x/using_persistent_chromadb_as_llm_vectorstore_for/) , 2023-08-30-0909
```
I have no issues getting a ChromaDB and vectorstore created and using it in Langchain to build out QA logic.  However I 
have moved on to persisting the ChromaDB instance and querying it successfully to simply retrieve most relevant doc\[0\]
.  However going through the examples of trying to re-construct this:  
`# store in Chroma index`  
`vectorstore = Chrom
a.from_documents(documents, embeddings)`

`#implement a Conversational Chain from your Chroma vectorbd above`  
`Convers
ationalRetrievalChain.from_llm(ChatOpenAI(temperature=0, model='gpt-4'), vectorstore.as_retriever())`  


incorporating 
a persistent ChromaDb I'm getting lost; the below works fine for simply  retrieving relevant docs..  
`db = Chroma(persi
st_directory='./chroma_db', embedding_function=OpenAIEmbeddings())`  
`query = 'Where can I get a copy of the training d
ocument xyz?'`  
`matching_docs = db.similarity_search(query)`  
`print(matching_docs[0])`

But I'm not having any luck 
finding examples where a persistent Chromadb is queried like this and incorporated into a call like this with vectorstor
e argument setup (or if that is even needed here)  
`ConversationalRetrievalChain.from_llm(ChatOpenAI(temperature=0, mod
el='gpt-4'),???)`

&#x200B;

thanks for any pointers! 
```
---

     
 
all -  [ Resources for memory for RAG systems ](https://www.reddit.com/r/learnmachinelearning/comments/161udzs/resources_for_memory_for_rag_systems/) , 2023-08-30-0909
```
I'm building a retrieval augmented generation system and for single queries it is working well. However, I can't get my 
head around memory for it. I've built several conversational chatbots using a queue type memory just fine, but a RAG sys
tem has two issues:

1. If query 1 is fundamentally different from query 2, the previous query context shouldn't be fed 
back in

2. If query 1 and query 2 are similar, or 2 is a follow up to 1, the retrieval step shouldn't happen, or at lea
st should be modified to seek only new information

Does anyone have resources I can look at to see how this works? I'm 
not talking about like, langchain documentation or something, the tools don't matter. More like, conceptually how is thi
s supposed to work?
```
---

     
 
MachineLearning -  [ Apache Airflow vs. LangChain and LlamaHub for LLM data pipeline [D] ](https://www.reddit.com/r/MachineLearning/comments/160lexg/apache_airflow_vs_langchain_and_llamahub_for_llm/) , 2023-08-30-0909
```
I’m looking for recommendations, suggestions, and/or good documentation that outlines which data pipeline would be best 
to ingest my private data (which will then be split into chunks/nodes for vector embeddings and so forth). Thank you in 
advance!
```
---

     
 
MachineLearning -  [ [P] LLM Apps Are Mostly Data Pipelines ](https://www.reddit.com/r/MachineLearning/comments/15z0muk/p_llm_apps_are_mostly_data_pipelines/) , 2023-08-30-0909
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

     
 
MachineLearning -  [ [P] pgml-chat: A command-line tool for deploying low-latency knowledge-based chatbots ](https://www.reddit.com/r/MachineLearning/comments/15t5nzl/p_pgmlchat_a_commandline_tool_for_deploying/) , 2023-08-30-0909
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

     
 
MachineLearning -  [ [P] My apprehension about LangChain and why you don’t need LangChain for building a RAG bot. ](https://www.reddit.com/r/MachineLearning/comments/15ry3z4/p_my_apprehension_about_langchain_and_why_you/) , 2023-08-30-0909
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

     
 
MachineLearning -  [ [D] Approach to creating an 'AI tutor' chatbot for a fantasy language? ](https://www.reddit.com/r/MachineLearning/comments/15o4jy9/d_approach_to_creating_an_ai_tutor_chatbot_for_a/) , 2023-08-30-0909
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

     
 
MachineLearning -  [ LLMs Challenges and Approaches Panel [N] ](https://www.reddit.com/r/MachineLearning/comments/15noqwr/llms_challenges_and_approaches_panel_n/) , 2023-08-30-0909
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

     
 
MachineLearning -  [ [D] training a model for function calls ](https://www.reddit.com/r/MachineLearning/comments/15n1j52/d_training_a_model_for_function_calls/) , 2023-08-30-0909
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

     
 
MachineLearning -  [ [D]Embedding model and vector store on LangChain ](https://www.reddit.com/r/MachineLearning/comments/15lllm0/dembedding_model_and_vector_store_on_langchain/) , 2023-08-30-0909
```
For Langchain users, what are the best text embedding models and vector stores (with similarity search) among the many i
ntegrations for connecting a AI model to text data? 

And does performance vary drastically from one model/database to a
nother? 
```
---

     
 
MachineLearning -  [ [P] Rust meets Llama2: OpenAI compatible API written in Rust ](https://www.reddit.com/r/MachineLearning/comments/15k254o/p_rust_meets_llama2_openai_compatible_api_written/) , 2023-08-30-0909
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

     
 
MachineLearning -  [ [D] Document-based QnA without OpenAI? ](https://www.reddit.com/r/MachineLearning/comments/15imv19/d_documentbased_qna_without_openai/) , 2023-08-30-0909
```
I am working on a project that is very popular with the inception of Langchain + GPT applications. However, I want to ma
ke it open source and hence don't want to use GPT. So something like Langchain + LLama2, etc. I know currently Langchain
 only supports GPT but any other ideas are highly appreciated!
```
---

     
 
MachineLearning -  [ [D] Roadmap for AI engineer (implementation of language models on premise) ](https://www.reddit.com/r/MachineLearning/comments/15gzsfv/d_roadmap_for_ai_engineer_implementation_of/) , 2023-08-30-0909
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

     
 
deeplearning -  [ Using PDFs with GPT Models ](https://www.reddit.com/r/deeplearning/comments/15g6i4x/using_pdfs_with_gpt_models/) , 2023-08-30-0909
```
Found a blog talking about how we can interact with PDFs in Python by using GPT API & Langchain. It talks about some pre
tty cool automations you can build involving PDFs - [https://nanonets.com/blog/chat-with-pdfs-using-chatgpt-and-openai-g
pt-api/](https://nanonets.com/blog/chat-with-pdfs-using-chatgpt-and-openai-gpt-api/)
```
---

     
