 
all -  [ OS plugin framework for AI actions, available as LangChain Toolkit and on OpenGPTs ](https://www.reddit.com/r/LangChain/comments/1ars2t0/os_plugin_framework_for_ai_actions_available_as/) , 2024-02-16-0909
```
We have created an open source framework to create and run AI actions to connect LLM-apps with the real world. Infrastru
cture, control and AI safety.

See use case and more [details here on the LangChain blog](https://blog.langchain.dev/mee
t-connery-an-open-source-plugin-infrastructure-for-opengpts-and-llm-apps/).

[GitHub repo and links to docs here](https:
//github.com/connery-io/connery)

Would love to get your feedback.
```
---

     
 
all -  [ Logically separated Semantic Example Selectors ](https://www.reddit.com/r/LangChain/comments/1arrqt5/logically_separated_semantic_example_selectors/) , 2024-02-16-0909
```
In a personal project I defined various chains, where each chain is responsible for a particular topic. To improve the c
ompletions quality, I perform few-shot for each topic. I do so using one SemanticSimilarityExampleSelector per topic and
 Chroma as vector database.

However, Chroma saves all the examples together and each SemanticSimilarityExampleSelector 
instance shares and selects the same examples, regardless of the chain’s topic

How can avoid this behaviour?
```
---

     
 
all -  [ iA chatbot for Trello ? ](https://www.reddit.com/r/trello/comments/1arrn4j/ia_chatbot_for_trello/) , 2024-02-16-0909
```
Hi,
Is there someone who managed to create a functionnal IA chatbot for trello ?
I mean, a chatbot that will be capable 
of searching info in a board (title, description, comments, labels, custom fields...) ?
I saw Langchain framework has a 
Trello agent, but i struggle using it... And did not find a real tutorial.
I also tried uploading json and csv in ChatGP
T, but the answers were not great (maybe a bad embedding/indexation).
Thanks for your feedbacks 👍
```
---

     
 
all -  [ Defining LLM Project architecture ](https://www.reddit.com/r/LangChain/comments/1arrmts/defining_llm_project_architecture/) , 2024-02-16-0909
```
I’m developing a project based on LLMs: ideally a chat that can interact with different APIs. To interact with such APIs
, a JSON request must be formalized. Indeed, being a chat, memory is needed.

What is the best way to do so?

Currently,
 I have two approaches in mind

- A LLMRouter identifies one route per API + a default route. This works, but introducin
g memory is quite difficult as I’m using LangChain and I have to integrate multiple different LLMChains, Few-shot-templa
tes, memory, and routing
- An agent with memory that has one tool per API plus a default chat. The tools, having to tran
slate the prompt to a JSON, would be simply LLMs in few shot settings
```
---

     
 
all -  [ Suggest Most optimal RAG pipeline for insurance support chatbot. ](https://www.reddit.com/r/LangChain/comments/1arraqh/suggest_most_optimal_rag_pipeline_for_insurance/) , 2024-02-16-0909
```
I am tasked to build AI RAG chatbot for health insurance company.

Please suggest optimal RAG pipeline,  
better tools a
nd tech stack for low latency and accuracy of the answers?

Thanks in advance.
```
---

     
 
all -  [ Retrieving output that exceeds context length after parsing? ](https://www.reddit.com/r/LangChain/comments/1arqpqp/retrieving_output_that_exceeds_context_length/) , 2024-02-16-0909
```
Basically the scenario is I load up a large pdf file which gets processed with the document parser and text splitter whi
ch then is passed through to my prompt for processing - How would I retrieve the entire pdf’s content after it has gone 
through the LLM? Or am I not using/thinking about this properly because my use case isn’t to use it as a chatbot but rat
her a processing layer for the entire pdf
```
---

     
 
all -  [ Chat with PDF, YouTube Videos, Websites & Audio Files - Langchain Project Demo ](https://youtu.be/E8VmiNK_uS4) , 2024-02-16-0909
```

```
---

     
 
all -  [ AI Agents using LangChain ](https://www.reddit.com/r/Langchaindev/comments/1arfbyw/ai_agents_using_langchain/) , 2024-02-16-0909
```
Hey everyone, check out this tutorial on how to run different AI-Agents using LangChain https://youtu.be/3pdcvSnCbf0?si=
RmUqW5GjlEDkhyYT
```
---

     
 
all -  [ Fanchat, a character.ai website powered by Mistral Ai ](https://www.reddit.com/r/MistralAI/comments/1arf6rx/fanchat_a_characterai_website_powered_by_mistral/) , 2024-02-16-0909
```
Hello Mistral Fans ! Just a quick message to say that i've created a [character.ai](https://character.ai) like website w
ith Langchain , Next.js and Mistral Api.   
Don't hesitate to try it and tell me what do you think ! 

[https://www.wear
efanchat.com](https://www.wearefanchat.com/dashboard)  
[https://youtu.be/0tbyMuBrFU8?si=kJ2z5Z1A2M9Zg8ro](https://youtu
.be/0tbyMuBrFU8?si=kJ2z5Z1A2M9Zg8ro)
```
---

     
 
all -  [ Conditional bypassing chain stages ](https://www.reddit.com/r/LangChain/comments/1areohp/conditional_bypassing_chain_stages/) , 2024-02-16-0909
```
Hello everyone! Is there a way to make, in idiomatic way, a conditional RunningSequence and bypass llm stage if retrieve
r returns empty list?
```
---

     
 
all -  [ Langchain is overhyped, you don't need it ](https://www.reddit.com/r/ChatGPTCoding/comments/1arbtc1/langchain_is_overhyped_you_dont_need_it/) , 2024-02-16-0909
```
I see nobody is talking about the downsides of langchain, I would have not wasted my time if we had. Let's do it now.

I
 have multiple projects using gpt, mistral, etc. Some of them use langchainjs and some of them use official sdk (e.g. op
enai node ackage,) and some directly make http request to the api. 


* All projects that don't use langchain are workin
g fine
* It is debatable which was most productive among sdk vs direct http call but I'd lean towards direct http call.

* On the other hand wherever I used langchain, it took me significantly more time to get started and fix bugs, langchain
 is a complex project. And even after using its features such as function calling, caching, etc. I don't see any real va
lue addition.

The initial thought process to choose langchain was that it would be easier to switch gpt with other mode
ls (in future). I was trying to solve a problem which I didn't have but the hype made me believe otherwise. To even make
 things worse, now I see that it will be harder to switch the models than using those models without langchain. 

With a
ll due respect to authors, I believe the project has lost its direction and trying to do more than it should be doing. F
irst you need to focus on basic stuff, make it simple to use and debug, and then focus on adding more value. If the prom
ise of portability between models is not delivered and complexity is added which makes doing even basic stuff harder, wh
y would I choose to use langchain and explore other features? My learning is simple, choose the direct api integration o
ver langchain. Until you see some specific usage of langchain, don't use it. I have multiple llm based projects doing al
l sorts of different stuff and even after 1+ yrs of development, none of them would need langchain, and I can't imagine 
why would someone need langchain ever.

How was your experience with langchain vs without it?
```
---

     
 
all -  [ In langchain/llama-index how to connect to multiple databases at once? [SQL Server] ](https://www.reddit.com/r/LangChain/comments/1ar8v7o/in_langchainllamaindex_how_to_connect_to_multiple/) , 2024-02-16-0909
```
What I want to do is - 

    connection_string = (
'DRIVER={ODBC Driver 17 for SQL Server};\
                      SERVE
R='+server+';\
                      DATABASE='+database+';\
                      UID='+username+';\
                  
    PWD='+password+';\
                      readonly=True'
)
connection_url = URL.create(
 'mssql+pyodbc', 
 query={'od
bc_connect': connection_string}
)
    sql_database = SQLDatabase(engine, sample_rows_in_table_info=3, include_tables=lis
t(table_details.keys()), view_support=True)

As you can see, here tables of only one database can be specified. What if 
I want to query multiple databases and also I require joining tables of multiples databases. how can I specify that?
```
---

     
 
all -  [ Langchain User Group Meeting Today Feb 15 2024 ](https://www.reddit.com/r/LangChain/comments/1ar8h9d/langchain_user_group_meeting_today_feb_15_2024/) , 2024-02-16-0909
```
Hello!

I've been organizing a langchain user group meeting every other Thursday at 7pm eastern US time.

We  get people
 just interested in langchain, people using langchain at   work, people using langchain as a hobby. We like to discuss t
he   langchain blog posts, interesting projects using langchain, and as a   general networking event among people tuned 
into the AI boom. It's a  great opportunity to share the latest developments, what works, what   doesn't work, and so on
.

[https://www.meetup.com/langchain-user-group/events/298419249/](https://www.meetup.com/langchain-user-group/events/29
8419249/)
```
---

     
 
all -  [ Should I use next.js if I don't utilize the built in api functionality? ](https://www.reddit.com/r/nextjs/comments/1ar7w31/should_i_use_nextjs_if_i_dont_utilize_the_built/) , 2024-02-16-0909
```
Let's take for instance the [vercel AI chatbot](https://vercel.com/templates/next.js/nextjs-ai-chatbot) \- it uses the a
pi folder to expose the CRUD requests for langchain and openai calls.

&#x200B;

I get that \`useChat\` from the \`ai\` 
package relies on \`route.ts\` file as an endpoint but I don't exactly see why I should use this functionality vs a trad
itional http call to a backend like django/rails/node etc.

&#x200B;

If I don't use the built in api from next.js, is t
here a point to using this framework?  
What is the benefit of using the built in api vs a traditional http client?
```
---

     
 
all -  [ How to implement LLM AI chatbot using vLLM in AWS with EKS ](https://www.reddit.com/r/LangChain/comments/1ar7hk9/how_to_implement_llm_ai_chatbot_using_vllm_in_aws/) , 2024-02-16-0909
```
 Hi guys,

I need some help and was wondering if anyone have some steps or a guide for me to implement the Mixtral-8x7B-
Instruct-v0.1 model (the LLM for my AI chatbot) using this GPU optimized library called vLLM ([https://github.com/vllm-p
roject/vllm](https://github.com/vllm-project/vllm)) in AWS using EKS (Elastic Kubernetes Service).

This is urgent. Woul
d really really appreciate any help with this. Many thanks!

Ps: if you have some sort of rough guidelines without the v
LLM part or instead of EKS use EC2, that would work too.
```
---

     
 
all -  [ How to set up RAG with Dolphin-mixtral-8x7b on text-generation-webui? ](https://www.reddit.com/r/Oobabooga/comments/1ar6i5i/how_to_set_up_rag_with_dolphinmixtral8x7b_on/) , 2024-02-16-0909
```
Hey I am new to all this AI stuff and I'm trying to do my first  setup on linux. I've decided to run Dolphin-mixtral-8x7
b on my machine but I would like if it could retrieve information from the internet or my documents but I have no Idea o
n how to achieve this. I've heard of LangChain but I can't find a n00b friendly tutorial for 0 knowledge people.   

Can
 you help me with this?   
```
---

     
 
all -  [ CrewAI vs AutoGen? ](https://www.reddit.com/r/AI_Agents/comments/1ar0sr8/crewai_vs_autogen/) , 2024-02-16-0909
```
Hello, I wanted to ask about your opinion for comparison between different multi-agent frameworks. I have been playing w
ith both Autogen and CrewAI (I haven't tested ChatDev or others) and I am curious which you find better for your use cas
e and why.

&#x200B;

From my experience:  
\- Crew AI is more accessible and easily gets you something cool, cuz it's b
uilt on the the top of Langchain  
\- Autogen has better default code execution capabilities, maybe is more difficult to
 set up? Not sure.  


Happy to discuss!

  

```
---

     
 
all -  [ [3.5 YoE] Software Engineer trying to land interviews ](https://www.reddit.com/r/EngineeringResumes/comments/1ar0a5s/35_yoe_software_engineer_trying_to_land_interviews/) , 2024-02-16-0909
```
Hi all, looking to see how I can optimize this resume to land Software Engineering interviews. Haven't had much luck wit
h hearing back from the companies I've applied to (50+), either templated rejections or no response. Just recently updat
ed this using the wiki, but it's largely the same as versions I've been recently submitting.

https://preview.redd.it/fd
uu5gg6qmic1.png?width=5100&format=png&auto=webp&s=fb513ef1e5f5a26b798f4102f4e0d09194eee715

\- Currently located in the 
northeast but open to positions across the US and potentially abroad if it's a good fit

\- My experience is at small-me
dium sized startups and am looking to get experience at a larger pre-IPO company, also plan to eventually apply to FAANG
 but don't want my resume tossed out from the get go

\- Recently laid off from most recent position due to reorg

\- US
 citizen

Wondering if there are specific bullets I can reword to sound more impactful. Open to stylistic feedback also 
regarding formatting, spacing etc. Also curious about my Skills/Education/Honors section and if any of that doesn't seem
 useful or necessary. 
```
---

     
 
all -  [ How to set up RAG with Dolphin-mixtral-8x7b on ollama? ](https://www.reddit.com/r/ollama/comments/1aqt9v6/how_to_set_up_rag_with_dolphinmixtral8x7b_on/) , 2024-02-16-0909
```
Hey I am new to all this AI stuff and I'm trying to do my first setup on linux. I've decided to run Dolphin-mixtral-8x7b
 on my machine but I would like if it could retrieve information from the internet or my documents but I have no Idea on
 how to achieve this. I've heard of LangChain but I can't find a n00b friendly tutorial for 0 knowledge people.   


Can
 someone help me with this?
```
---

     
 
all -  [ Vector similarity check ](https://www.reddit.com/r/LangChain/comments/1aqt4w4/vector_similarity_check/) , 2024-02-16-0909
```
So I need to compare the similarity between 2 sentences contextually. I used tfIdVectorizer from sklearn to vectorize bo
th sentences and then calculate the cosine distance between them. This works good until any of the sentence is not in En
glish. Then I changed the embedding model to text-embedding-ada-002 which I believe is multilingual. Somehow the cosine 
distance is always too near around 0.7 even though both sentences are whole different contextually. Any advice for this?

```
---

     
 
all -  [ How to persistently save a Parent Document Retriever? ](https://www.reddit.com/r/LangChain/comments/1aqijs9/how_to_persistently_save_a_parent_document/) , 2024-02-16-0909
```
Hi,

i want to try out storing smaller embeddings for search with larger chunks for context. It seems that the Parent Do
cument Retriever serves this purpose. However the LangChain Documentation as well as numerous tutorials on YouTube do no
t mention any way of a persistent implementation. They just use an In Memory approach for the docstore. I have lots of d
ocuments i want to embed, so i basically want to have a persistent data structure with my embeddings and the correspondi
ng text chunks for context.

I first tried out using LangChains LocalStorage instead of InMemory, however this throws an
 error. 

Is there an easy way to store my Parent document retriever for later use?

&#x200B;

Thank you for your help
```
---

     
 
all -  [ How to retrieve document custom_id using source file name? ](https://www.reddit.com/r/LangChain/comments/1aqhlwg/how_to_retrieve_document_custom_id_using_source/) , 2024-02-16-0909
```
Is there any method to retrieve a document's custom_id using other attributes like the file name in Pgvector
```
---

     
 
all -  [ Best German Embedding Model? ](https://www.reddit.com/r/LangChain/comments/1aqh168/best_german_embedding_model/) , 2024-02-16-0909
```
Hi,

I wanted to discuss which german open-source embedding models worked best for your use case? My use case would be a
 RAG app where more or less complex german docs are retrieved. 

I played around with several multilingual/german embedd
ings but I am not sure which one to use. The results between the differnt embedding models are quite big I tried:

\- ji
naai/jina-embeddings-v2-base-de (recently published)

\- intfloat/multilingual-e5-large

\- T-Systems-onsite/cross-en-de
-roberta-sentence-transformer

\- sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2

\- aari1995/German\_Seman
tic\_STS\_V2

These are the results:

`sentence1 = 'Ich liebe Cola'`

`sentence2 = 'Ich hasse Pepsi'`

`from numpy.linal
g import normcos_sim = lambda a,b: (a @ b.T) / (norm(a)*norm(b))embeddings = model.encode([sentence1,sentence2])embeddin
gs1 = model1.encode([sentence1,sentence2])embeddings2 = model2.encode([sentence1,sentence2])embeddings3 = model3.encode(
[sentence1,sentence2])embeddings4 = model4.encode([sentence1,sentence2])print(f'Jina: {cos_sim(embeddings[0], embeddings
[1])}')print(f'Intfloat: {cos_sim(embeddings1[0], embeddings1[1])}')print(f'RoBERTa: {cos_sim(embeddings2[0], embeddings
2[1])}')print(f'Paraphrase: {cos_sim(embeddings3[0], embeddings3[1])}')print(f'German Semantic: {cos_sim(embeddings4[0],
 embeddings4[1])}')`

&#x200B;

https://preview.redd.it/dcziehfp3iic1.png?width=282&format=png&auto=webp&s=858aa47781726
a3e543beba43001b9017bd4e2df
```
---

     
 
all -  [ My debut book on Generative AI is out !! ](https://www.reddit.com/r/GPT/comments/1aqewqs/my_debut_book_on_generative_ai_is_out/) , 2024-02-16-0909
```
I am thrilled to announce the launch of my debut technical book, “***LangChain in your Pocket: Beginner’s Guide to Build
ing Generative AI Applications using LLMs***” which is available on Amazon in Kindle, PDF and Paperback formats (bestsel
ler on Amazon in)

https://preview.redd.it/3wgfk1vwghic1.png?width=785&format=png&auto=webp&s=c7e4b15abf8572d88a10f5d0cc
5b033eec9d142f

In this comprehensive guide, the readers will explore LangChain, a powerful Python/JavaScript framework 
designed for harnessing Generative AI. Through ***practical examples and hands-on*** exercises, you’ll gain the skills n
ecessary to develop a diverse range of AI applications, including Few-Shot Classification, Auto-SQL generators, Internet
-enabled GPT, Multi-Document RAG and more.

***Key Features:***\- Step-by-step code explanations with expected outputs f
or each solution.- No prerequisites: If you know Python, you’re ready to dive in.- Practical, hands-on guide with minima
l mathematical explanations.

***Amazon*** : [https://www.amazon.com/LangChain-your-Pocket-Generative-Applications-ebook
/dp/B0CTHQHT25](https://www.amazon.com/LangChain-your-Pocket-Generative-Applications-ebook/dp/B0CTHQHT25)

***About me:*
**

I'm a Senior Data Scientist at DBS Bank with about 5 years of experience in Data Science & AI. Additionally, I manag
e 'Data Science in your Pocket', a [Medium Publication](https://medium.com/@mehulgupta_7991) & [YouTube channel](https:/
/www.youtube.com/@datascienceinyourpocket/videos) with \~600 Data Science & AI tutorials and a cumulative million views 
till date. To know more, you can check [here](https://www.linkedin.com/in/mehulgupta7991/)
```
---

     
 
all -  [ My debut book on Generative AI is out ! ](https://www.reddit.com/r/Chatbots/comments/1aqepbm/my_debut_book_on_generative_ai_is_out/) , 2024-02-16-0909
```
I am thrilled to announce the launch of my debut technical book, “***LangChain in your Pocket: Beginner’s Guide to Build
ing Generative AI Applications using LLMs***” which is available on Amazon in Kindle, PDF and Paperback formats (bestsel
ler on [Amazon.in](https://Amazon.in))

&#x200B;

https://preview.redd.it/l3cebhfyehic1.png?width=785&format=png&auto=we
bp&s=deefed64ac7e8ec9d6e47f86c59d9c4fdaf0c8f6

In this comprehensive guide, the readers will explore LangChain, a powerf
ul Python/JavaScript framework designed for harnessing Generative AI. Through ***practical examples and hands-on*** exer
cises, you’ll gain the skills necessary to develop a diverse range of AI applications, including Few-Shot Classification
, Auto-SQL generators, Internet-enabled GPT, Multi-Document RAG and more.

***Key Features:***\- Step-by-step code expla
nations with expected outputs for each solution.- No prerequisites: If you know Python, you’re ready to dive in.- Practi
cal, hands-on guide with minimal mathematical explanations.

***Amazon*** : [https://www.amazon.com/LangChain-your-Pocke
t-Generative-Applications-ebook/dp/B0CTHQHT25](https://www.amazon.com/LangChain-your-Pocket-Generative-Applications-eboo
k/dp/B0CTHQHT25)

***About me:***

I'm a Senior Data Scientist at DBS Bank with about 5 years of experience in Data Scie
nce & AI. Additionally, I manage 'Data Science in your Pocket', a [Medium Publication](https://medium.com/@mehulgupta_79
91) & [YouTube channel](https://www.youtube.com/@datascienceinyourpocket/videos) with \~600 Data Science & AI tutorials 
and a cumulative million views till date. To know more, you can check [here](https://www.linkedin.com/in/mehulgupta7991/
)
```
---

     
 
all -  [ The agent doesn't know how to process custom tools with multiple parameters. ](https://www.reddit.com/r/LangChain/comments/1aqdo35/the_agent_doesnt_know_how_to_process_custom_tools/) , 2024-02-16-0909
```
I'm trying to use Cohere API to run an agent, but even though it was able to correctly fetch the necessary parameters fr
om the query, it can't be properly passed into the custom tool with multiple parameter. I see it is not formatting the p
arameters as required, what can I do to help it do as the formatting want?

The link goes to the colab notebook with an 
example.

[https://colab.research.google.com/drive/1lShUML0qKM59Ds7Wr8eo4Z\_Nx8dxJ8f9?usp=sharing](https://colab.researc
h.google.com/drive/1lShUML0qKM59Ds7Wr8eo4Z_Nx8dxJ8f9?usp=sharing)
```
---

     
 
all -  [ Not sure why langsmith hub doesn't work ](https://www.reddit.com/r/LangChain/comments/1aqaejb/not_sure_why_langsmith_hub_doesnt_work/) , 2024-02-16-0909
```
So I'm trying to use Langsmith Hub for my prompts. I've tested using:  
prompt = hub.pull('hwchase17/openai-tools-agent'
)  


My script work fine. Now I want to add my own system prompt, so I've forked the above, and edited the system promp
t.  


But when I run the script now, I get this error:  
KeyError: 'Input to ChatPromptTemplate is missing variables {'
chat\_history'}.  Expected: \['agent\_scratchpad', 'chat\_history', 'input'\] Received: \['input', 'intermediate\_steps'
, 'agent\_scratchpad'\]'  


On langsmith hub, I've added the 'chat\_history'. But when i pull, for some reason it doesn
't pull through.  


Any thoughts?
```
---

     
 
all -  [ What's the standard practice for setting initialization prompts and maintaining context when switchi ](https://www.reddit.com/r/OpenAIDev/comments/1aq79ab/whats_the_standard_practice_for_setting/) , 2024-02-16-0909
```
Hi I am trying to build a modularized LLM application using Langchain where within any individual conversation, the app 
can seamless switch between multiple LLMs to respond to the query, for example:

1. User: What's 1+ 1?
2. App (GPT-3.5):
 1+1 is 2
3. User: Concatenate the last name of the current president of the US with the answer from your last response

4. App (Gemini Ultra): Biden2

I have two technical questions that I hope this subreddit can help answer:

1. What's the
 standard practice for setting the initialization prompts or background prompts? For example I want to tell this App tha
t 'your name is Bob', and I want this App to continuously remember it's Bob regardless how long the conversation has got
ten or any switching between LLMs. Do I set this at the beginning of the conversation or before every single response?
2
. What's the standard practice for conversation memory management when there's switching of LLM involved within one conv
ersation? Do I store all the conversation history within a vector database and do a index search prior to any individual
 response?
```
---

     
 
all -  [ [D] What's the standard practice for setting initialization prompts and maintaining context when swi ](https://www.reddit.com/r/MachineLearning/comments/1aq78ao/d_whats_the_standard_practice_for_setting/) , 2024-02-16-0909
```
Hi I am trying to build a modularized LLM application using Langchain where within any individual conversation the app c
an seamless switch between multiple LLMs to respond to the query, for example:

1. User: What's 1+ 1?
2. App (GPT-3.5): 
1+1 is 2
3. User: Concatenate the last name of the current president of the US with the answer from your last response
4
. App (Gemini Ultra): Biden2

I have two technical questions that I hope this subreddit can help answer:

1. What's the 
standard practice for setting the initialization prompts or background prompts? For example I want to tell this App that
 'your name is Bob', and I want this App to continuously remember it's Bob regardless how long the conversation has gott
en or any switching between LLMs. Do I set this at the beginning of the conversation or before every single response?
2.
 What's the standard practice for conversation memory management when there's switching of LLM involved within one conve
rsation? Do I store all the conversation history within a vector database and do a index search prior to any individual 
response?
```
---

     
 
all -  [ What is AI Observability ](https://www.reddit.com/r/AIObservability/comments/1aq6hxm/what_is_ai_observability/) , 2024-02-16-0909
```
Let's say there was an example Q&A bot powered by a large language model created by a coffee company to enage their cust
omers more effectively. A user's question such as 'what's a latte?' kicks off a workflow that identifies relevant conten
t from a knowledgebase about coffee using an embedding model and passes this context to a large language which then summ
arizes the content in a brief natural response.

In an sample deployment, the workflow could be implemented as a python 
program coded using LangChain framework and the embedding & language models are obtained from Huggingface. Workflow is s
erved up using Azure ML and the models are served using Nvidia Triton inference server hosted on kubernetes service in A
zure.

AI observability would require capturing and correlating metrics from across the LLM app components and the AI in
fra services used to run these components to understand what impacts performance and how to best optimize it.
```
---

     
 
all -  [ What can we do about user spam? ](https://www.reddit.com/r/LangChain/comments/1aq5n46/what_can_we_do_about_user_spam/) , 2024-02-16-0909
```
I’m implementing an agent to hopefully trial with some of our current users via WhatsApp and realized that users could e
asily spam messages to get a response, thus unnecessarily increasing our costs by calling some api to return a model’s r
esponse.

What strategies could someone implement to to tackle this issue?
```
---

     
 
all -  [ Introductory courses that aren't video based? ](https://www.reddit.com/r/LangChain/comments/1aq2xzl/introductory_courses_that_arent_video_based/) , 2024-02-16-0909
```
Management at my customer service job has given the green light to work on continuing education classes when it's slow. 
I'm looking for some introductory classes I can take that are text based as I cannot watch videos during my shift. Does 
anyone know of some course options that are read along only with no video component?
```
---

     
 
all -  [ Is there a way to store Vectorstores? ](https://www.reddit.com/r/LangChain/comments/1aq2nvr/is_there_a_way_to_store_vectorstores/) , 2024-02-16-0909
```
Hi, I am building a vectorstore using `Chroma.from_documents` of textual data. Because my dataset is large, the number o
f chunks is high and hence it takes a long time to create the vector store. What is the best way to - a) parallelize it.
 and b) store it so I don't have to do it every time I run my notebook?
```
---

     
 
all -  [ Deployment template for running LangServe on AWS Fargate ](https://www.reddit.com/r/LangChain/comments/1aq19oe/deployment_template_for_running_langserve_on_aws/) , 2024-02-16-0909
```
A template to deploy your LangChain app running locally to the cloud. This architecture specifically packages LangServe 
into a Docker image, stores the image in ECR, and runs the container in AWS Fargate with an ALB in front.

[langserve\_r
eference\_architecture](https://preview.redd.it/flzjgv5wfeic1.png?width=6079&format=png&auto=webp&s=b5a5d4ab4330d435cdf1
4d43f1a3f5487a8577ff)

The template comes in Python, Typescript, Golang, C#, YAML. It uses OpenAI for the LLM.

Read the
 [blog post](https://www.pulumi.com/blog/easy-ai-apps-with-langserve-and-pulumi) to follow along with the two examples: 
a Gandalf chatbot and a Pinecone RAG app. Let me know if you have any questions or if you would like to see any other ki
nd of template.
```
---

     
 
all -  [ Is this possible? ](https://www.reddit.com/r/generativeAI/comments/1apz09f/is_this_possible/) , 2024-02-16-0909
```
Hi, newbie to GenAI here. 

I wanted to know if we can download open source GenAI models and use them in an isolated env
ironment by fine tuning them to retrieve needed data and answer the questions asked based on it. 

I've started to learn
 LangChain and ig we can do that using it. If the whole system needs to be on cloud, how do we  basically host this whol
e thing?

Will there be any security issues like some leakage points in the downloaded model itself such that it steals 
data from us?

I need to make a POC for clients like media or law firms. 

Any input or suggestions will be helpful and 
appreciated. Thanks.
```
---

     
 
all -  [ Using Vertex AI Model Garden with Langchain ](https://www.reddit.com/r/LangChain/comments/1apwigv/using_vertex_ai_model_garden_with_langchain/) , 2024-02-16-0909
```
I am trying to use Vertex AI Model Garden for inference with Langchain. I have successfully deployed Mistral to an endpo
int in Google Cloud and want to get inference with the class VertexAIModelGarden which is already implemented. However, 
it seems the output returned by the endpoint is not correctly parsed as it only contains a single character (see image).


I found a pull request on the langchain github repo that mentions this issue and there is a link to another repo where
 someone has implemented a temporary fix ( [https://github.com/shikanime/langchain-vertexai-extended](https://github.com
/shikanime/langchain-vertexai-extended) ). I tried using this code and it seems to work but I was wondering if anyone el
se had this issue and if this 'fix' will eventually be included in Langchain. Furthermore, the stream method is not yet 
supported in this fix so we can just use the invoke. 

&#x200B;

https://preview.redd.it/lekh5bkvgdic1.png?width=1290&fo
rmat=png&auto=webp&s=cc51b00326ae91a98b3b5f6ee958129d61f3192f
```
---

     
 
all -  [ GPT4ALL function calling ](https://www.reddit.com/r/LangChain/comments/1aputis/gpt4all_function_calling/) , 2024-02-16-0909
```
I know there is this support for function calling for models like [OpenAI](https://python.langchain.com/docs/modules/mod
el_io/chat/function_calling) but is this also supported in the GPTAALL?
```
---

     
 
all -  [ Preparing model for production ](https://www.reddit.com/r/LangChain/comments/1apu4ml/preparing_model_for_production/) , 2024-02-16-0909
```
Hi, I have wrote a chat model based on huggingface inference through langchain, and I would like to prepare it for produ
ction. 

My scope is kinda small as I am aiming to host it locally in WAMP/XAMP or AWS server to be used as demonstratio
n of the app.  

I was able to find few API explanations out there but it is quite unclear hence it is my very first imp
lementation in such context.

I tried Writing a Flash app and prepare few files one that has Flash api calla, the second
 one has the code structure for the app (starting with package importing and ending with response), and the last file ha
s all the functions that I am using in my second file that preprocess and handle data.

I'm left wondering on one questi
on is that the model and memory initialization and construction is in the second file, which leave me wondering how the 
memory of the chat model is going to persist when the user query it multiple queries within the same interaction.
```
---

     
 
all -  [ Please give tips can't get any internship ,sophomore at tier 3 ](https://i.redd.it/qnje7e0h1cic1.jpeg) , 2024-02-16-0909
```
Suggestions or any advice on resume are appreciated 🙂
```
---

     
 
all -  [ Ollama sequential behaviour ](https://www.reddit.com/r/LangChain/comments/1apq6ql/ollama_sequential_behaviour/) , 2024-02-16-0909
```
Hey,   
I was exploring the Ollama library to serve the mistral model, I came into a case where the model was serving a 
single request at a time. 

i.e. Scenario: Simultaneous requests from two or more machines were served by the model on a
 first come first serve basis. Expected behavior: Serve multiple requests simultaneously.  


If the expected behavior i
s possible, guide me through the process.
```
---

     
 
all -  [ How can I use LangChain to filter through files in a directory given some filters ](https://www.reddit.com/r/LangChain/comments/1apq229/how_can_i_use_langchain_to_filter_through_files/) , 2024-02-16-0909
```
Im trying to mass filter through a windows directory given filters such as date, file type, and other important keywords
, is there any python library or langchain system that can filter using some basic filters like these? I have tried indi
vidually going file by file and running a loader but it takes forever and is quite cost intensive.
```
---

     
 
MachineLearning -  [ Whats in your RAG setup? [D] ](https://www.reddit.com/r/MachineLearning/comments/1apcp2w/whats_in_your_rag_setup_d/) , 2024-02-16-0909
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

     
 
MachineLearning -  [ [D] What's the best current RAG setup that would work with a local LLM? ](https://www.reddit.com/r/MachineLearning/comments/1ag6bo7/d_whats_the_best_current_rag_setup_that_would/) , 2024-02-16-0909
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

     
 
MachineLearning -  [ [P]: Anukool: My job hunting assistant ](https://www.reddit.com/r/MachineLearning/comments/1adu3tw/p_anukool_my_job_hunting_assistant/) , 2024-02-16-0909
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

     
 
MachineLearning -  [ New Data API for Astra [N] ](https://www.reddit.com/r/MachineLearning/comments/199uobn/new_data_api_for_astra_n/) , 2024-02-16-0909
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

     
 
MachineLearning -  [ [D] While using function calling or tools on openai or langchain, does openai have access to the dat ](https://www.reddit.com/r/MachineLearning/comments/199t8be/d_while_using_function_calling_or_tools_on_openai/) , 2024-02-16-0909
```
I am working on a client project and I am using langchain's tools and agents. I want to know if the data is getting pass
ed to openai or is it just like that - Output of one function is being directly passed to the second function with the k
nowledge of openai.
```
---

     
 
deeplearning -  [ [D] WebVoyager: Navigating Digital Cosmos with LangGraph & Multimodal Models ](https://www.reddit.com/r/deeplearning/comments/1altlca/d_webvoyager_navigating_digital_cosmos_with/) , 2024-02-16-0909
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

     
 
deeplearning -  [ [D] Langchain Elevates with Step-Back Prompting using RAGatouille ](https://www.reddit.com/r/deeplearning/comments/1agtyeh/d_langchain_elevates_with_stepback_prompting/) , 2024-02-16-0909
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

     
 
deeplearning -  [ Become an AI Developer (Free 9 Part Series) ](https://www.reddit.com/r/deeplearning/comments/1afgp2r/become_an_ai_developer_free_9_part_series/) , 2024-02-16-0909
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

     
 
deeplearning -  [ DSPy Explained! ](https://www.reddit.com/r/deeplearning/comments/1adypks/dspy_explained/) , 2024-02-16-0909
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

     
