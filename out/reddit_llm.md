 
all -  [ MarkdownTextSplitter ](https://www.reddit.com/r/LangChain/comments/1e47vwu/markdowntextsplitter/) , 2024-07-16-0911
```
This LangChain tool is a little naive- it is just a text splitter with charLength and overlap size. Does anyone know of 
a compatible splitter that can breakdown a Markdown based on header sections and other elements (eg, lists, code, tables
)??
```
---

     
 
all -  [ Default search method in ChromDB while performing similarity_search() ](https://www.reddit.com/r/LocalLLaMA/comments/1e407tg/default_search_method_in_chromdb_while_performing/) , 2024-07-16-0911
```
What is the default search metric while using:

    similarity_search()

Also, can I explicitly give my own metrics, wha
t are the other metrics available for ChromaDB?

Link to the method: [https://api.python.langchain.com/en/latest/vectors
tores/langchain\_community.vectorstores.chroma.Chroma.html#langchain\_community.vectorstores.chroma.Chroma.similarity\_s
earch](https://api.python.langchain.com/en/latest/vectorstores/langchain_community.vectorstores.chroma.Chroma.html#langc
hain_community.vectorstores.chroma.Chroma.similarity_search)
```
---

     
 
all -  [ Default search method in ChromDB while performing similarity_search() ](https://www.reddit.com/r/LangChain/comments/1e4059d/default_search_method_in_chromdb_while_performing/) , 2024-07-16-0911
```
What is the default search metric while using:

    similarity_search()

Also, can I explicitly give my own metrics, wha
t are the other metrics available for ChromaDB?
```
---

     
 
all -  [ [HELP/ IDEAS NEEDED] I have a llama 2 chat model working locally i want the model to take a CSV file ](https://www.reddit.com/r/LangChain/comments/1e3yv1o/help_ideas_needed_i_have_a_llama_2_chat_model/) , 2024-07-16-0911
```
So I have a llama 2 7b chat model on my machine running locally, what I want to do is that the model takes a CSV file as
 input the file can contain anything ranging from text, numbers, shareholder info, etc., process the file and gives out 
text in a particular paragraph form that makes sense, I tried asking multiple GPT's but I couldn't get anywhere 

So if 
any of you esteemed AI engineers could help a frustrated college student it would mean a lot 
```
---

     
 
all -  [ Biggest RAG Hurdles for Beginners? ](https://www.reddit.com/r/LangChain/comments/1e3ygh6/biggest_rag_hurdles_for_beginners/) , 2024-07-16-0911
```
Hey Everyone,

I'm curious what the group thinks are the biggest pain points for devs getting started with RAG? My list 
would be:  

* **hallucination**: especially with complex docs
* **eval**: there are tools to score completions vs retri
evals, but what about the rest of the RAG pipeline where the problems actually occur. 
* **complexity:** many pieces of 
the pipeline to master (parse, extract, convert to LLM friendly data, chunk, embed, create metadata for context, search,
 rerank, etc) and lots of theories on best approach to each one. 

What's everyone else dealing with?


```
---

     
 
all -  [ Hola, les comparto este webinar que se ve interesante sobre LLMs con Langchain y Python ](https://www.uniandinos.org.co/eventos/-uso-practico-de-llms-large-language-models-langchain-y-python-5161) , 2024-07-16-0911
```

```
---

     
 
all -  [ AzureChatOpenAI not working ](https://www.reddit.com/r/LangChain/comments/1e3w7l9/azurechatopenai_not_working/) , 2024-07-16-0911
```
I am trying to get \`AzureChatOpenAI\` to work, but keep getting \`openai.NotFoundError: Error code: 404 - {'error': {'c
ode': '404', 'message': 'Resource not found'}}

\` 

It works if I use \`AzureOpenAI\`. However, the issue with this is 
I got the following error

\`\`\`  
raise ValueError(

ValueError: OpenAIChat currently only supports single prompt, got
  
\`\`\`

I am trying a simple tutorial to use \`load\_summarize\_chain\`

  
Does anyone have any idea?
```
---

     
 
all -  [ Cost Prediction of nvidia nim nv-embed-v1 ](https://www.reddit.com/r/LangChain/comments/1e3w5lq/cost_prediction_of_nvidia_nim_nvembedv1/) , 2024-07-16-0911
```
I am creating a RAG application based on legal texts. I have documents approx. 80 million tokens long. As you know for R
AG application I need to embed documents first.

Formerly I was using openai embeddings *text-embedding-3-large* model b
ut it will cost 10k$. For better outputs and lower cost I want to switch *Nvidia nim nv-embed-v1* but I have never hoste
d an AI model before so I cannot predict approx. cost.

I will be glad if you guys can share any source for hosting AI m
odels, calculating Host Cost and maybe tell me which one is cheaper *text-embedding-3-large* or *Nvidia nim nv-embed-v1*
?

Thank you.
```
---

     
 
all -  [ Integration of RAGAS Evaluation with Langserve ](https://www.reddit.com/r/LangChain/comments/1e3u619/integration_of_ragas_evaluation_with_langserve/) , 2024-07-16-0911
```
Hey everyone, I am looking to integrate ragas scoring for every api call made to a langserve endpoint. Does anyone have 
any references or thoughts on how one can do this. I am planning to further log these metrics into langsmith to track th
e performance over time
```
---

     
 
all -  [ How to use LangChain with a custom endpoint? ](https://www.reddit.com/r/LangChain/comments/1e3rl5d/how_to_use_langchain_with_a_custom_endpoint/) , 2024-07-16-0911
```
Hello! So I have an endpoint on which my trained model is deployed. How can I use this with LangChain? endpoint\_url = '
---------/chat'

Can someone please give me the wrapper code, I am so confused because I already have this model and I d
ont know how to use this with LangChain. I want to utilize the ConversationBufferMemory method to retain context.

For b
ackground, I am using this endpoint for a Webex chatbot.
```
---

     
 
all -  [ [Experiment] Good chunking will lead you to the better RAG performance ](https://www.reddit.com/r/LangChain/comments/1e3q2lb/experiment_good_chunking_will_lead_you_to_the/) , 2024-07-16-0911
```
Yes, chunking document in RAG is important. But, how much? I got curious and ran a experiment to see how chunking method
 will effect to the RAG performance.

[The diagram of the experiment](https://preview.redd.it/krnc1j0fancd1.png?width=28
94&format=png&auto=webp&s=a045b1d5ed51e6d721adc1112805e2bea5968dae)

I selected total five chunking method. I ran exact 
same RAG pipeline with different chunking method and measure the answer quality. It was Korean document with 40 question
s.

# The five chunking method

- No Chunk : PDF page itself is the chunk.  
- Token Splitter  
- Recursive Splitter  
-
 Window Splitter : comes from [LlamaIndex](https://docs.llamaindex.ai/en/stable/examples/node_postprocessor/MetadataRepl
acementDemo/) : passage merge after retrieval  
- Semantic Splitter : used openai embedding

I used G-eval as a LLM-eval
 metric. And I used [AutoRAG](https://github.com/Marker-Inc-Korea/AutoRAG) to quickly run the RAG experiment. (The G-eva
l range is 1 to 5)

Plus, since the G-eval is not perfect metric, I checked all question and answers manually and measur
e the factualness of the RAG answers. 

If the answer was perfect, I gave 1. If the RAG system said 'don't know', I gave
 0. If there was hallucination, I gave -1. And the answer might be vague, then I gave 0.5.

# Result

|Metric Result|No 
Chunk|Token Splitter|Recursive Splitter|Window Splitter|Semantic Splitter|
|:-|:-|:-|:-|:-|:-|
|G-eval|2.4706 |3.3529 |3
.1176 |3.3529 |**3.7647**|
|Human Eval|0.3529   |0.6471|0.4706|0.5882 |**0.7941**|

Both G-eval and human eval, the sema
ntic splitter performs best. The score is quite different, and its impact is quite big. Find the right chunking is essen
tial to build great RAG system.

# Limitation

Since I used only 40 questions, and human eval was performed only on the 
17 questions, the statistic needs to be larger for more precise result. 

---

This experiment took only a few hours, th
anks to the [AutoRAG](https://github.com/Marker-Inc-Korea/AutoRAG/). You can optimize and run the experiment easily usin
g it. It is open-source project so feel free to use it on your RAG project.
```
---

     
 
all -  [ Chroma db , results size ](https://www.reddit.com/r/LangChain/comments/1e3q18k/chroma_db_results_size/) , 2024-07-16-0911
```
Hello everyone, so I have this problem puzzling, i have a simple rag app to chat with my pdf files, and i use crhoma as 
the vector db, i am using cosine for saving the documents and threshold for retrieving the most relevant ones, my proble
m is i have to provide a n\_results for chroma, otherwise the default is returning 4 documents,  my problem is if i prov
ide 500 results, it will always provide 500 results, no matter how relevant they are, i wonder is there a smart way to a
djust the search results each time? cause sometimes 500 results might be too big , sometimes it might be low, so i might
 lose information, also returning 500 results has some other drawbacks as well, as the app is becoming very slow, not to
 mention the token size limit.

Thank you in advance!
```
---

     
 
all -  [ Finetuning ColBERT reranker ](https://www.reddit.com/r/LangChain/comments/1e3plel/finetuning_colbert_reranker/) , 2024-07-16-0911
```
Hello. Has anybody tried finetuning ColBERT models? Did it help you? How much data do you need to finetune it well? 
```
---

     
 
all -  [ ReAct issues ](https://www.reddit.com/r/LangChain/comments/1e3p6pf/react_issues/) , 2024-07-16-0911
```
Hi everyone!

I'm working with langchain to create a RAG-ReAct agent with job candidates CVs. Right now I'm having two m
ain issues: some degree of hallucination (even though I have my llm temperature set to 0; I guess you can't elude it com
pletely with llms) and tool management. My question is about this one.

I've created my tools with the Tool class, and t
ried with different queries explicitely designed to use several of them in the same process, but I keep getting my agent
 to stop its output after using the first tool. 

For example, if I ask it to first look for people with experience in H
adoop and then calculate for each of them how many years of experience they have in the field (I have a tool designed fo
r basic info search and one designed for calculating periods of time), it will output a list with an answer to the first
 question, but will forget the second one.

I've tried with prompting: nothing. I've also tried with setting return_dire
ct to False, but it gets an excesive tokens error.

I'm using create_react_agent function and AgentExecutor class with a
n OpenAI call.

My prompt is based on [this one](https://smith.langchain.com/hub/hwchase17/react) from langchain hub. 


Any help would be appreciated, since I keep getting stucked and I've run out of ideas. Thanks a lot!
```
---

     
 
all -  [ How important is CODING?? ](https://www.reddit.com/r/learnmachinelearning/comments/1e3oho2/how_important_is_coding/) , 2024-07-16-0911
```
I know all basic fundamentals of Python(variables, function, list, set, tuples, class etc..)  
But I just don't know how
 much emphasis should be given to coding.

Because I think what's more important is what we're doing with the code. Beca
use just to make a Neural network, using Tensorflow we do this in one way, using Pytorch in another way(different syntax
), while Maths behind this is same...
All the things that we used in Langchain to make a GenAI app, now within a year co
ding syntax is changed a lot.

I just don' t know
```
---

     
 
all -  [ ChatGPT Vision API with LangChain and JavaScript ](https://www.reddit.com/r/LangChain/comments/1e3oap0/chatgpt_vision_api_with_langchain_and_javascript/) , 2024-07-16-0911
```
Hi folks!  
  
Made this short example with ChatGPT Vision API, LangChain and Node: [https://www.js-craft.io/blog/vision
-api-langchain-javascript/](https://www.js-craft.io/blog/vision-api-langchain-javascript/)

https://preview.redd.it/wxpx
g0erqmcd1.jpg?width=1582&format=pjpg&auto=webp&s=82969758c98e21ef28bd13caccdcc04fc9aa651e

Hope it's helpful for someone
 as a getting started example  🙂


```
---

     
 
all -  [ Is multi threading possible for llms integrated from the vllm framework? ](https://www.reddit.com/r/LangChain/comments/1e3mqf3/is_multi_threading_possible_for_llms_integrated/) , 2024-07-16-0911
```
I'm currently exploring options to reduce the response time/ inference time through multithreading the prompts, so is it
 possible and what are some other ways to execute multiple prompts at a same time.  
Currently I'm working with the phi-
3 models in google colab free, i'm always encountering a error related to a parameter 'num\_new\_tokens' and the prompts
 are not executing.

If anyone has already implemented multithreading or multiprocessing of LLMs can you explain or prov
ide a link to the resource
```
---

     
 
all -  [ Deploy Api with LLM backend ](https://www.reddit.com/r/LangChain/comments/1e3lu2v/deploy_api_with_llm_backend/) , 2024-07-16-0911
```
Hey guys so I had a question. Have a simple api that in an input, calls an LLM for processing (I use llama3 with grok at
 the moment) and returns an output. When I run it on my computer it runs fine. Takes a few seconds but runs. Most of thi
s is fancy prompting so I haven’t fine tuned the model or anything at the moment. It’s just chained prompts and LLMs

I 
tried to deploy it on render to test out but I keep getting a memory error given it’s taken more than 512MB given that i
s renders free tier. 

Does anybody know where else I can try this out? Another server or even a real cheap one? 

As fo
r long term I need to move passed grok and deploy my own LLM using olama or just move to open AI. I haven’t moved yet be
cause I find the output to be better with llama3 vs OpenAI 3.5….4o is too cost prohibitive at the moment 

Any advice? 
```
---

     
 
all -  [ Memory Preservation using AI (Beta testing iOS App) ](https://www.reddit.com/r/LangChain/comments/1e37ksf/memory_preservation_using_ai_beta_testing_ios_app/) , 2024-07-16-0911
```
Super excited to share that our iOS app is live for beta testers. In case you want to join please visit us at: [https://
myreflection.ai/](https://myreflection.ai/)

MyReflection is a memory preservation agent on steroids, encompassing image
s, audios, and journals. Imagine interacting with these memories, reminiscing, and exploring them. It's like a mirror al
lowing you to further reflect on your thoughts, ideas, or experiences. Through these memories, we enable our users to cr
eate a digital interactive twin of themselves later on.

This was built keeping user security and privacy on top of our 
list. Please give it a test drive would love to hear your feedback. 
```
---

     
 
all -  [ llamaindex query responses are short ](https://www.reddit.com/r/LlamaIndex/comments/1e33h84/llamaindex_query_responses_are_short/) , 2024-07-16-0911
```
I find llamaindex query responses much shorter than the answer I get from langchain. Especially compared to directly ask
ing questions to chatgpt4o on OpenAI website. What is the reason for this?

        query_engine = vsindex.as_query_engi
ne(
            similarity_top_k=top_k, response_mode=llama_response_mode)  
        answer = query_engine.query(query)

    

  
I played with top\_k to 10 also different response models like refine or tree\_summarize
```
---

     
 
all -  [ Langchain Agent with self query retrieval. ](https://www.reddit.com/r/LangChain/comments/1e32ffw/langchain_agent_with_self_query_retrieval/) , 2024-07-16-0911
```
Has anyone worked on or have any resources regarding using the self query retrieval mechanism with langchain agent and g
ot exact response from agent without any hallucinations or not able get required documents from vectordb like problems.
```
---

     
 
all -  [ Beginner using langchain having some doubts ](https://www.reddit.com/r/LangChain/comments/1e2zh63/beginner_using_langchain_having_some_doubts/) , 2024-07-16-0911
```
I recently started with Python and the project I built first was a simple project based on the rag model. High level is 
I used a book and parsed it , created chunks and stored the embeddings in the chromadb (which is a vector db). 

Based o
n user query finds the most relevant first matching chunk and passes it to llm with this info as context and user query.
 The llm(gemini-pro) generates the response 

Doubt:

Are these type of projects are even good projects as I've just com
pleted my graduation 2 weeks ago in computer science. Does this type of projects are even good for fresher?
What more in
teresting things I should do and how do I measure that the my rag model produces better results compared to directly ask
ing the llm same query. What are the parameters the length,  Grammer or etc of the generated response 

I've just starte
d this and there might be some very basic or dumb doubts from my side. I'm looking for some direction I could go on with
 Gen-ai 
```
---

     
 
all -  [ stupid question : which tool LangChain team use to draw their schema ? ](https://www.reddit.com/r/LangChain/comments/1e2xzbu/stupid_question_which_tool_langchain_team_use_to/) , 2024-07-16-0911
```
Love LangChain schematic, which tool they use ? Do you have any recommandation to draw easily agentic/LLM app architectu
re ?

https://preview.redd.it/905gadmjbgcd1.png?width=2893&format=png&auto=webp&s=dbc2601a5ad8917901a4ab23c88a6095968141
1f


```
---

     
 
all -  [ Do GoogleAPI a requirement for the web research class ? ](https://www.reddit.com/r/LangChain/comments/1e2w4zx/do_googleapi_a_requirement_for_the_web_research/) , 2024-07-16-0911
```
I wrote a custom search tool class which does not use Google, but I am still unable to get the web research functionalit
y to work since it keeps demanding a google api key?

```
---

     
 
all -  [ Why should i keep using langchain? ](https://www.reddit.com/r/LangChain/comments/1e2vx5m/why_should_i_keep_using_langchain/) , 2024-07-16-0911
```
I made a RAG system with Langchain just becasuse a coworker did a POC with it, and i've structured it much better. At th
e moment i use pgvector as vectorstore adding some filter to it based on metadata, pass the document to the stuff chain 
and get a streaming answer.

Now the business requires some new features, like parent document retriever, calculating co
sts, hybrid search/reranking, etc.. that i find very tough using Langchain instead of making all vanilla.

At the moment
 i just place a postgres query, call openAI to rephrase my question and history, and call openAI again to get the answer
. Is nothing that fancy, isn't it?
```
---

     
 
all -  [ Roast my resume,not getting calls for even oa for internships ](https://i.redd.it/3spnw6x35fcd1.jpeg) , 2024-07-16-0911
```
I am looking for ml/data science/data analytics internship since my pre final year has begin. For ml I have doing resear
ch projects in healthcare for quite some time.
I have also qualified Amazon ml summer school and in top 50 out of 1400 i
n amex product track(result is yet to come for last round).I have applied a lot for above mentioned  domains but to no s
ucess till date how can I improve this resume to cater to what is actually needed to atleast receive a call?
```
---

     
 
all -  [ Are vector embeddings / similarity search non-deterministic? ](https://www.reddit.com/r/LangChain/comments/1e2hnoq/are_vector_embeddings_similarity_search/) , 2024-07-16-0911
```
I created some documents to test out the performance of the vector store and embedding, and when using LangChain batch m
ethod to process multiple queries at the same time I get different results even for pretty straightforward queries. I ha
ve two documents each contains info about golf and tennis. The query to the retriever is simply retriever.batch([Tennis,
 Golf]).

The response changes from one call to the next. Sometimes the batch returns content related to only golf or so
metimes only tennis. I thought maybe it’s because the similarity closeness of the sports in vector space so I added a th
ird document with “cats,dogs” etc and randomly the batch method sometimes returns this document as the most relevant. 


Extremely confused. Could it be an issue with the embeddings?

UPDATE: I tried another vector db (Chromadb) instead of W
eaviate and the issue was resolved. 
```
---

     
 
all -  [ Non-relevant questions to the context in chatbot ](https://www.reddit.com/r/LangChain/comments/1e2grkh/nonrelevant_questions_to_the_context_in_chatbot/) , 2024-07-16-0911
```
Hi everyone,

While implementing RAG in a chatbot pipeline, what are the common strategies for dealing with questions th
at are not relevant to the context?  
When asking questions about the context stored in my local DB the retriever gets t
he relevant data and the LLM generates the right answer. However, if I ask questions like 'Who are you', or 'How are you
?' I get hallucinations because the prompt contains under the hood also retrieved context.

I tried specifying in the sy
stem prompt that if the question is not relevant to the context, say I don't know but it didn't help.

Thank you all for
 your help
```
---

     
 
all -  [ What should someone with a MSc Data science degree do? ](https://www.reddit.com/r/developersIndia/comments/1e2cghw/what_should_someone_with_a_msc_data_science/) , 2024-07-16-0911
```
Well, I hold a master's in data science. No BTech. But I've built fullstack projects with django + react, flask, built f
lutter a basic flutter app with dart, used hyped llms for a complete chat bot with RAG using neo4j and langchain. I've a
lso done a lot of analytics as a learner and a freelancer. Did a shitty software job for 4 months and quit because it wa
s pointless. 

What should I do now? Been jobless since Feb end. Upskilled a lot, did a lot, contributing to open-source
 whenever I can. I've started losing hair, can't sleep, distanced myself from everyone because of the stress and anxiety
. Should I focus on something else? I've got 2 offers in the last 4 months (1 for an longterm internship where they make
 you work real projects on yourself with the client with no pay or PPO and 2nd one was similar with no pay and pay is on
ly when the product gets costumers). 

Some people have said I don't have the marketing skills to market my skills. I've
 tried everything and I don't know what I'm missing. My resume is updated every month with the latest project, details a
nd stuff and checked with ATS (always above 70). I send cold mails to every recruiter I can find. Many have said they wo
n't offer a job because of my degree. Only the ones who gave me take-home assessments did interviews with me. Out of tho
se 4 interviews, I got 2 offers and those were basically useless. 


I want to work as a data engineer and I've been hon
ing my skills for that. 


Maybe I'm being desperate. Idk, it's just disappointing. 
```
---

     
 
all -  [ Need help with using Langchain runnables .. ](https://www.reddit.com/r/LangChain/comments/1e2acs1/need_help_with_using_langchain_runnables/) , 2024-07-16-0911
```
Hey everyone,

I am currently working on a project where I need to process nested queries using Langchain. Specifically,
 I have a requirement where an LLM evaluates a rule for example address should contain company name, street name, pin co
de, city name, and state. The outer chain should wait for all the internal chains to process, and then the outer chain s
hould be evaluated.

I have been trying to implement this using Land Chain runnables, but I am facing some challenges in
 getting it to work as expected. Could anyone provide some guidance or examples on how to properly structure the Land Ch
ain runnables to achieve this nested query processing behavior?

Any help, code snippets, or resources would be greatly 
appreciated. Thank you in advance!
```
---

     
 
all -  [ Langgraph: what implementation strategy would you recommend for this case?  ](https://www.reddit.com/r/LangChain/comments/1e276vp/langgraph_what_implementation_strategy_would_you/) , 2024-07-16-0911
```
Hi! I would like to get suggestions on how to implement the following using langgraph:
What i have today: i have a langg
raph workflow containing one 'supervisor' agent and I 2 specialised agents. When the user inputs a request the superviso
r decides what agent to send the work to until it decides the work is finished.
What i want to do now is:
-for one of th
ese agents I want to make it a two step operation. So the agent receives the request and then displays to the user infor
mation about what he is about to do. The user can then give an ok of ask for some tweak. Then the agent finishes the job
. 
Another possibility here is that the agent decides it doesn't has all the info and reaches to the user to ask for add
itional info (in that case he will also reach the user to confirm the operation). 
I imagine I can achieve this with bre
akpoints and collecting human input, but since I've never did it before i am a bit confusing on how the states and workf
low should look like. 
```
---

     
 
all -  [ Full stack Python developers needed ](https://www.reddit.com/r/PythonJobs/comments/1e25xv4/full_stack_python_developers_needed/) , 2024-07-16-0911
```
Howdy,

Recently established startup in Romania, VC backed, we need 3 full stack developers available immediately to acc
elerate the development of a SaaS platform, Azure hosted, powered by AI. Everything in Azure DevOps.

Ideally, someone w
ith good experience in Python, FastAPI, next.js, langchain, llama-index, knowledge of LLMs, Graphrag, Azure app services
/container apps, IaC, RAG pipelines, with great attention to non functional reqs.

Very important, b2b only, preferably 
EU timezone, remote all the time if the day looks approximately like this, 3-5 pushes in production per day, constant im
provements:

11:00. Standup.

11:30. You are participating in a call with a new client who recently started using our pl
atform. It asks about possible additional integrations with other systems. After the call, you draw up a plan for the ne
w functionality — depending on the priority, you might aim for completion on the same day.

14:30. While working, we not
ice that we are encountering an issue that is causing performance issues for some tenants. The whole team mobilizes to i
dentify and solve the problem.

16:00. The new functionality is complete. Push the new code and inform the customer abou
t the new capability.

17:00. Conduct an onboarding call for a new customer, taking notes on the user's reaction to the 
product.
```
---

     
 
all -  [ AI phone calling agent ](https://www.reddit.com/r/LangChain/comments/1e25aed/ai_phone_calling_agent/) , 2024-07-16-0911
```
We are an ai chatbot company,  I am to add a phone calling layer over the chatbot , I am looking for techstack for such 
usecase. I am using python for that. Want everything to be customised, Speech to Text , text to speech.

Currently I am 
to use Twillio. But I want to have full control over speech . To transcribe &etc  i aim to use in house model 


Suggest
 resources.
```
---

     
 
all -  [ SQL Agent to automate querying (LangChain, LlamaIndex, CrewAI) ](https://www.reddit.com/r/Automate/comments/1e23u1r/sql_agent_to_automate_querying_langchain/) , 2024-07-16-0911
```
Hey everyone! 🚀 I’m thrilled to share another exciting project: an SQL Agent to execute SQL queries and document them.


**Objectives**

This project aims to create an intelligent agent capable of interacting with SQL databases to perform qu
eries, log them, and manage data efficiently.

**Implementation Details**

Tools & Frameworks:  
Composio, Langchain, Ll
amaIndex, CrewAI, ChatGPT, Python

Setup:

1. Clone the repo: git clone
2. Navigate to the example: cd composio/python/e
xamples/sql\_agent
3. Install dependencies: pip install -r requirements.txt

**Key Features**

1. SQL Query Execution: A
utomatically run and log SQL commands.
2. Database Management: Seamlessly interact with and manage data in various datab
ases.
3. Agentic Integration: Leverage multiple frameworks for enhanced data processing and query management.
4. Dynamic
 Query Handling: Generate and execute SQL queries based on real-time inputs.
5. Data Analysis: Use built-in functions to
 analyze query results and visualize data.

**Results**

The agent automates database interactions, making data manageme
nt more efficient and less error-prone. It can be integrated into various applications where database interaction is req
uired.

[GitHub Repo](https://git.new/SQLAgent)

Feel free to explore the project, give it a star if you find it useful,
 and let me know your thoughts or suggestions for improvements! 🌟
```
---

     
 
all -  [ Tool calling with Claude 3.5 not working ](https://www.reddit.com/r/LangChain/comments/1e1r8rk/tool_calling_with_claude_35_not_working/) , 2024-07-16-0911
```
Hi, I am building an AI agent with Claude 3.5. My functions are not being invoked by the agent. My understanding was tha
t Langchain automatically calls the agent, but it is not being called. I do, however, am receiving as a model response t
hat function needs to be called. Here's the model response and my code:

    > Entering new AgentExecutor chain...
    c
ontent: Certainly
    content: ,
    content:  ****. I
    content: 'll create
    content:  a new I
    content: **** f
or you
    content:  using
    content:  the available
    content:  function
    content: .
    content: toolu_01G44ahC
crqSaXgiUWrvX85L
    content: None
    [{'text': 'Certainly, *****. I'll create ******* for you using the available func
tion.', 'type': 'text', 'index': 0}, {'id': 'toolu_01G44ahCcrqSaXgiUWrvX85L', 'input': {}, 'name': '*******', 'type': 't
ool_use', 'index': 1, 'partial_json': ''}]
    
    > Finished chain.
    
    
    
    llm_with_tools = llm.bind_tools
(tools)
    agent = (
        {
            'input': lambda x: x['input'],
            'agent_scratchpad': lambda x: for
mat_to_openai_tool_messages(
                x['intermediate_steps']
            ),
            'chat_history': lambda x
: x['chat_history'],
        }
        | prompt
        | llm_with_tools
        | OpenAIToolsAgentOutputParser()
    )

    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
```
---

     
 
all -  [ Want to use langchain or llamaindex of structured data pdf parsing ](https://www.reddit.com/r/LLMDevs/comments/1e1qosr/want_to_use_langchain_or_llamaindex_of_structured/) , 2024-07-16-0911
```
Can any one tell me what would be the cost for parsing semi structured data from PDF table, images and store them in pin
econe .

Both the platforms are openbsource so would this cost me if I use their platform in production.
```
---

     
 
all -  [ Full stack python developer ](https://www.reddit.com/r/programare/comments/1e1qip6/full_stack_python_developer/) , 2024-07-16-0911
```
Salutare,

Startup recent infiintat, VC backed, avem nevoie de 3 full stack developers disponibili imediat pentru a acce
lera dezvoltarea unei platforme SaaS, Azure hosted, powered by AI. Totul in Azure DevOps.

Ideal ar fi cineva cu experie
nta buna pe Python, FastAPI, next.js, langchain, llama-index, cunostiinte despre LLMs, Azure app services/container apps
, IaC, cu atentie mare pe non functional reqs.

Foarte important, b2b only, remote all time daca ziua arata in felul urm
ator, 3-5 push-uri in productie pe zi, imbunatiri constante:

11:00. Standup.

11:30. Participi la un apel cu un client 
nou care a inceput recent sa utilizeze platforma noastra. Te intreaba despre posibile integrari suplimentare cu alte sis
teme. Dupa apel, redactezi un plan pentru noua functionalitate — in functie de prioritate, s-ar putea sa vizezi finaliza
rea in aceeasi zi.

14:30. In timp ce lucram, observam ca intampinam o problema de performanta care cauzeaza probleme de
 performanta pentru unii tenanti. Toata echipa se mobilizeaza pentru a identifica si rezolva problema.

16:00. Noua func
tionalitate este completa. Push la noul cod si informezi clientul despre noua capabilitate.

17:00. Conduci un apel de o
nboarding pentru un nou client, luand notite despre reactia utilizatorului la produs.

17:45. Standup/cina cu echipa. Di
scutam despre viata, stiri, munca etc.

18:30. Seara buna, pe urmatoarea zi!






```
---

     
 
all -  [ Learn till transformers, what is next (towards llm) ? ](https://www.reddit.com/r/learnmachinelearning/comments/1e1mx46/learn_till_transformers_what_is_next_towards_llm/) , 2024-07-16-0911
```
Just finished learning transformers,  ofcourse will code gpt from scratch (Andrej karpaty's). I am going towards llm's a
nd Gen AI applications.


What should I do next ? Read about each llm & architecture ? Learn langchain ? I am very confu
sed different rodmaps say different approach. 

Help me in guiding from your experience and mistakes. 

A flow will help
.


Thanks in advance.
```
---

     
 
all -  [ Please Suggest me better open source model for getting json output (Rag operation).  ](https://www.reddit.com/r/LangChain/comments/1e1jutc/please_suggest_me_better_open_source_model_for/) , 2024-07-16-0911
```
The model is about to extract the data from the pdf based bunch of questions. I tried different quantized model. But eve
ry time I tried i failed to make an output. The model giving me schema it self (jsonoutputparser)  
```
---

     
 
MachineLearning -  [ [D] Is Anyone Else Setting Up Real-Time Django Workers for their AI Application? What's the best way ](https://www.reddit.com/r/MachineLearning/comments/1e0qens/d_is_anyone_else_setting_up_realtime_django/) , 2024-07-16-0911
```
We completely underestimated this one tbh, thought it would be much more straight forward. But we've done it now and doc
umented how step by step [in this article series](https://medium.com/p/5828a1ea43a3).

A bit of context, we're building 
a mini free AI Agent that auto-generates manually customisable plots, so the user can basically style however they want.
 It needs to be cost effective and efficient, so we thought about how to do it and tested a couple other ways.

https://
preview.redd.it/cmly0a6bhwbd1.png?width=640&format=png&auto=webp&s=be1f5b2853e744adcaf8013e6d43b43f6be89617

We plan on 
releasing the project open source, so all feedback welcome! Is anyone else doing this and has any feedback? or do know o
f a better way to do it?
```
---

     
 
MachineLearning -  [ [P] Real Time AI Workers Web Application ](https://www.reddit.com/r/MachineLearning/comments/1dzryk9/p_real_time_ai_workers_web_application/) , 2024-07-16-0911
```
Hi everyone!

I've created a mini series on how to build a real time AI application using Django, LangChain and Celery.


Free knowledge - posting it in here for anyone working on something similar and had the same blockers I had when buildi
ng.

Let me know what you think on how I could potentially improve this architecture.

Part 1

[https://medium.com/towar
dsdev/how-to-set-up-django-from-scratch-with-celery-channels-redis-docker-real-time-django-601dff7ada79](https://medium.
com/towardsdev/how-to-set-up-django-from-scratch-with-celery-channels-redis-docker-real-time-django-601dff7ada79)

Part 
2

[https://medium.com/towardsdev/how-to-set-up-django-from-scratch-with-celery-channels-redis-docker-real-time-django-5
828a1ea43a3](https://medium.com/towardsdev/how-to-set-up-django-from-scratch-with-celery-channels-redis-docker-real-time
-django-5828a1ea43a3)

Part 3

[https://medium.com/towardsdev/how-to-set-up-django-from-scratch-with-celery-channels-red
is-docker-real-time-django-8e73c7b6b4c8](https://medium.com/towardsdev/how-to-set-up-django-from-scratch-with-celery-cha
nnels-redis-docker-real-time-django-8e73c7b6b4c8)

Part 4

[https://medium.com/towardsdev/how-to-set-up-django-from-scra
tch-with-celery-channels-redis-docker-real-time-django-c090c300517a](https://medium.com/towardsdev/how-to-set-up-django-
from-scratch-with-celery-channels-redis-docker-real-time-django-c090c300517a)

Part 5  
[https://medium.com/@cubode/how-
to-set-up-django-from-scratch-with-celery-channels-redis-docker-real-time-django-0845eb7e083c](https://medium.com/@cubod
e/how-to-set-up-django-from-scratch-with-celery-channels-redis-docker-real-time-django-0845eb7e083c)
```
---

     
 
MachineLearning -  [ [P] Seeking Feedback on My GenAI Job Fit Project - New to LangChain/LangGraph ](https://www.reddit.com/r/MachineLearning/comments/1dgns9p/p_seeking_feedback_on_my_genai_job_fit_project/) , 2024-07-16-0911
```
Hi all,

Soo, i have been working on a a projectcalled [GenAI Job Fit](https://github.com/DAVEinside/GenAI_Job_Fit). It'
s an AI-driven system designed to enhance job applications by providing tailored recommendations based on individual pro
files.

I'm relatively new to LangChain and LangGraph, and I've incorporated them into this project. I would greatly app
reciate it if you could check out the repository and provide any feedback or suggestions for improvement.

Your insights
 on how I can better implement LangChain/LangGraph, or any other aspect of the project, would be incredibly valuable. I'
m eager to learn and make this project as robust as possible.

Thank you in advance for your time and feedback!

Repo Li
nk : [https://github.com/DAVEinside/GenAI\_Job\_Fit](https://github.com/DAVEinside/GenAI_Job_Fit)
```
---

     
 
deeplearning -  [ Llama 3 not running on GPU ](https://www.reddit.com/r/deeplearning/comments/1dptxsr/llama_3_not_running_on_gpu/) , 2024-07-16-0911
```
I dont know much theory about RAG but i need to implement it for a project.  
**I want to run llama3 on my GPU to get fa
ster results.**

`from langchain_community.llms import Ollama`  
`llm = Ollama(model='llama3',num_gpu=1)`  
`def generat
e_response(prompt, similar_jobs):`  
`descriptions = '\n\n'.join([job['Description'] for job in similar_jobs])`  
`augme
nted_prompt = f'{prompt}\n\nHere are some job recommendations based on your query:\n{descriptions}'`  
`for chunks in ll
m.stream(augmented_prompt):`  
`print(chunks, end='')`

I am giving llama3 my *'user prompt'* and top 5 nearest *'simila
r\_jobs'* using cosine similarity.  
This code goes not use my GPU but my CPU and RAM usage is high.

**My gpu usage is 
0%** , i have a Nvidia GeForce RTX 3050 Laptop GPU GDDR6 @ 4GB (128 bits)
```
---

     
 
deeplearning -  [ What is ReAct Prompting? the most important piece in agentic frameworks ](https://www.reddit.com/gallery/1djk4nk) , 2024-07-16-0911
```
“What is ReAct Prompting? the most important piece in agentic frameworks” - A quick read from Mastering LLM (Large Langu
age Model) 'Coffee Break Concepts' Vol.6

This document deeps dive into the ReAct Prompting method and why it's importan
t:
1. Limitations of LLM
2. Why ReAct prompting matters?
3. How ReAct Works?
4. LangChain Implementation
5. Why Prompt w
ithin agentic frameworks Matters?

Comment below on which topic you want to understand next in this 'Coffee Break Concep
ts' series and we will include those topics in upcoming weeks.
```
---

     
