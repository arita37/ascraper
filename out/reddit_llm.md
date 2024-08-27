 
all -  [ [RAG Project] Help Needed ](https://www.reddit.com/r/Rag/comments/1f20usq/rag_project_help_needed/) , 2024-08-27-0912
```
Hi, I am doing this small mini project where I am making a RAG model based on a JSON file. I need to use Langchain, Open
 AI and Pinecone. Can someone interested help me please. If you can dm, I can share my progress
```
---

     
 
all -  [ Langchain tool to avoid cloudflare detection ](https://github.com/thevgergroup/undetected-browser-tool) , 2024-08-27-0912
```

```
---

     
 
all -  [ Building crowdsource Genrative AI Builder Community.(Alpha Invite)  ](https://www.reddit.com/r/LangChain/comments/1f1zbvz/building_crowdsource_genrative_ai_builder/) , 2024-08-27-0912
```
#Day1 - Document Building crowdsource Genrative AI Builder Community.

Together on a mission to Upskill, secure the futu
re of employee's and mitigate unemployment.

#Day2 - Resources to understand required hardware for AI
- Resources on Set
ups and what to choose PC, Server, Mini PC, egpu, cloud, so on. 

#Day3  - Starting a Weekly Newsletter to staying upto 
date. 
- Resources for Research papers, blogs, AI video, juypternote, models, finetuneting, reports etc.

#Day4 - Struct
uring the Weekly newsletter format for Community. 
- Social media
- GitHub Trends
- Huggingface trends 
- Reseach Papers

- Others : AI news, hardware, software so on.

#Day5 - Setting up discord server for Community Members :
- Get started 

- Discussion (Threads) 
- Discuss & Chill (Voice) 
- Community Share 
- AI resources 

Who can join? 

- Building GenAI
 And vision model mini Projects or MVP. 
- Maintain projects on GitHub, hugging face son on. 
- Testing github Projects,
 goggle collab, Kaggle, huggingface models, etc. 
- Testing ComfiUI Workflow,
- Testing LLMs, SLM, VLLM so on. 
- Want t
o create resources around GenAI and Vision models such as Reseacher Interview, Github Project or ComfiUI workflow discus
s, Live project showcase, Finetuneting models, training dreambooth, lora, so on. 
- Want to contribute to croudsource Ge
nAI Newsletter.
- If you want to grow, build or contribute to the community. 

Everything will be documented on GitHub. 


FREE Access to 1st 100 Member. 
https://discord.com/invite/dKskAgbhYH

Note : I'm looking for advisors, Volenteers, co
mmunity feedback to improvise,  Community suggestions to scale and monetize. 

Thank you
```
---

     
 
all -  [ Best way to make LLM response context aware with spreadsheet data ](https://www.reddit.com/r/LangChain/comments/1f1xsx5/best_way_to_make_llm_response_context_aware_with/) , 2024-08-27-0912
```
I'm having question marks on my approach and would love your expert opinion here: I'm developing a tool for electronics 
engineers where users input the name of a custom device and its components (Bill of Materials) into the system.
The tool
 then needs to generate a list of all manufacturing and assembly activities required to produce the device, intelligentl
y matching components to these activities. Additionally, it should generate a comprehensive list of any remaining inputs
 and outputs based on a predefined dataset of electronics manufacturing activities and components ('Electronics_Manufact
uring_Data.csv'). So the LLM response need to be context aware of the dataset and conform to the items in this dataset.

I'm wondering whether to implement this using Retrieval-Augmented Generation (RAG)/Fine tune/ or if transforming the dat
a into SQL for querying would be a better approach, or if there's another technique that might be more effective?
```
---

     
 
all -  [ RAG with PDF ](https://www.reddit.com/r/LangChain/comments/1f1vxc0/rag_with_pdf/) , 2024-08-27-0912
```
Im new to GenAI. I’m building a real estate chatbot. I have found some relevant pdf files but I am having trouble indexi
ng them. Any ideas how I can implement this?
```
---

     
 
all -  [ Which models can bu used in LangGraph? ](https://www.reddit.com/r/LangChain/comments/1f1s6u0/which_models_can_bu_used_in_langgraph/) , 2024-08-27-0912
```
Hi everyone, I have been working in a Adaptive RAG project and using LangGraph. For now I'm using OpenAI for LLM and Emb
eeding. But I wonder in LangGraph's Agent can I use any model from HuggingFace.
```
---

     
 
all -  [ How does the query work when using a vectordatabase ](https://www.reddit.com/r/LangChain/comments/1f1s43m/how_does_the_query_work_when_using_a/) , 2024-08-27-0912
```
  
Hey Everyone, I have been using this chain for a while, but it just comes up to me how this actually works internally
. As you can see I am passing a retriever from a vectorstore but the query is in plain text. Now I was wondering since I
 am using a sentence transformer for the embedding of my text but the query is in plain text (not embedded) how this sea
rch works here.  
Any help would be appreciated  
  
  
`retriever = vectorstore.as_retriever()`  
`new_chain = (`  
`{'
text': retriever, 'query': RunnablePassthrough()}`  
`| prompt_template`  
`| llm`               
`| JsonOutputParser()`
  
`)`


```
---

     
 
all -  [ Struggling with SQL Agent in Langchain and Ollama LLM – Need Help! ](https://www.reddit.com/r/LangChain/comments/1f1ptmh/struggling_with_sql_agent_in_langchain_and_ollama/) , 2024-08-27-0912
```
I've been working on creating an SQL agent in Langchain using OpenAI, and everything was running smoothly. However, when
 I switched to using a local Ollama LLM, things started to fall apart.

I tried using `AgentType.ZERO_SHOT_REACT_DESCRIP
TION`, but I kept running into an error: **'Invalid Format: Missing 'Action Input:' after 'Action:''**. The agent would 
generate thoughts and actions, but it always failed with this error and never returned any results. I also attempted to 
use `AgentType='tool_calling'`, but that didn’t work either.

At first, I thought it might be an issue with the model si
ze, so I upgraded to a larger 70B model, but still no luck. Interestingly, when I tested the same SQL agent with the ReA
ctAgent in LlamaIndex, it worked for simple queries. However, it struggles with more complex queries, often going into a
 loop and eventually failing.

Has anyone else experienced similar issues? I’m looking for guidance on how to create an 
SQL agent that works without relying on LlamaIndex or Langchain. Any help or pointers would be greatly appreciated!
```
---

     
 
all -  [ What's the modern stack for customer support AI chatbots? ](https://www.reddit.com/r/LangChain/comments/1f1pl7i/whats_the_modern_stack_for_customer_support_ai/) , 2024-08-27-0912
```
I'm looking to implement a WhatsApp customer support chatbot for a medium-ish online business. 

Previously I've built a
gents like these from scratch with a Node backend, putting all the product information straight into the context window 
(with GPT-4-32k) and building all the API integrations manually. 

Is there a better, less manual and potentially less c
ompute-cost-heavy way to create a client-facing AI agent these days?
```
---

     
 
all -  [ Deploy LLM app ](https://www.reddit.com/r/LangChain/comments/1f1p2dt/deploy_llm_app/) , 2024-08-27-0912
```
I have a streamlit based LLM app that can be used to query pdfs. It is being run locally now. How I can possibly product
ionise it? Is streamlit used for production?
```
---

     
 
all -  [ Displaying Graphs in Output ](https://www.reddit.com/r/LangChain/comments/1f1ou7y/displaying_graphs_in_output/) , 2024-08-27-0912
```
I'm using `create_csv_agent` and `create_python_agent` to analyze CSV files. While the agent can generate graphs, they a
ren't appearing in the output.

Is there a way to include the generated plots directly in the output?
```
---

     
 
all -  [ Is it possible to use Langgraph in Azure Promtpflow? ](https://www.reddit.com/r/LangChain/comments/1f1op94/is_it_possible_to_use_langgraph_in_azure/) , 2024-08-27-0912
```
Hey, not sure if this is a stupid question or not, but my team has been building RAG applications using Azure Promptflow
 for a while now and I recently started learning about langgraph and its potential. The question they have and I have no
 idea about is this: can Azure promptflow handle Langgraph and can we develop RAG or multi agent systems like that? I ha
ve tried running one of the multi-agent examples and it crashes when the StateGraph and more specifically its schema is 
initiated, then i get an error that says key error: __pf_main__
```
---

     
 
all -  [ Parallel loop over input array, combine results into output array ](https://www.reddit.com/r/LangChain/comments/1f1ol87/parallel_loop_over_input_array_combine_results/) , 2024-08-27-0912
```
I have a simple 'prompt | model | parser' chain. I'm passing a dict (created in separate chain) into invoke with the res
ult being added as a new property to the original input dict. This is set up like this:

    chain = (
       RunnablePa
ssthrough.assign(input_array=lambda x: input_array)
       | prompt
       | model
       | parser
    )
    
    passth
rough_chain = RunnablePassthrough.assign(new_output=chain)
    result = passthrough_chain.invoke({ 'input_array': my_arr
ay })
    print(result) ## { 'input_array': my_array, 'new_output': result_from_chain }

This is working as expected, bu
t now I would like to instead use 'chain' for each item in 'input\_array' with the result of each added to the 'new\_out
put'. I suspect this can be achieved using RunnableParallel in some way? I understand I don't need to use langchain LCEL
 to achieve this, but I would like to see how this can be achieved. Anyone have an ideas?
```
---

     
 
all -  [ Which is Better for My Issues Table: LangChain's SQL Chain or a Simple Text File? ](https://www.reddit.com/r/LangChain/comments/1f1mq73/which_is_better_for_my_issues_table_langchains/) , 2024-08-27-0912
```
Hey everyone!

I'm currently working on a Q&A project where I have a table called 'Issues' to store all the FAQs. I want
 to allow the admin to insert and update entries in this table easily. Now, I’m looking to integrate a retrieval-augment
ed generation (RAG) setup so that when someone asks a question, the LLM can fetch the relevant response from this table.


I'm trying to decide the best way to implement this. Should I use the SQL Chain feature from LangChain to interact dir
ectly with the table, or would it be better to store these issues in a text file and update my indexes each time there's
 a change?

I'd appreciate any insights or suggestions on which approach might be more efficient or easier to manage. Th
anks!
```
---

     
 
all -  [ How can I store the 'Short Term Memory' (or the State in Langgraph) for a ChatBot in Whatsapp for ea ](https://www.reddit.com/r/LangChain/comments/1f1morn/how_can_i_store_the_short_term_memory_or_the/) , 2024-08-27-0912
```
I have a Langgraph multi-agent workflow that already works in a JupyterNotebook, and in our company we want to implement
 it in Whatsapp to interact with users. But, i don't know how can i manage the memory for each user, since in my underst
anding (i have never really deployed code, im a Jr.) the whole script runs entirely each time an user interacts, so the 
whole state would be wiped off and the 'short term memory' would be erased, even when working with thread IDs. Any guide
/help would be very much appreciated. Thanks!
```
---

     
 
all -  [ Anyone help me setting the Settings of Chroma DB ](https://www.reddit.com/r/LangChain/comments/1f1m4js/anyone_help_me_setting_the_settings_of_chroma_db/) , 2024-08-27-0912
```
I am using new versions of langchain and use langchain_chroma to create my persistent client. Inorder to create a vector
store in duckdb+parquet format, it is required to pass client_settings to chroma, but I am able to pass only empty setti
ngs. If I pass with params, I am getting errors (traceable but no meaning) (it's there, says not there)(says cannot find
 key persist_dirrctory even if I pass). Any help on how to rectify would be appreciated... Thanks in advance
```
---

     
 
all -  [ Langchain OpenAi conversation chat Id support ](https://www.reddit.com/r/LangChain/comments/1f1l4ul/langchain_openai_conversation_chat_id_support/) , 2024-08-27-0912
```
Hi everyone, do you know how can i use openai chat id (or conversationId) using langchain framework? Now I am sending th
e whole prompt which contains old memory chats  in langchain instead of sending just prompt and chatId. I think langchai
n does not support openai chat id feature. Do you know any custom implementation or useful source which uses langchain a
nd chatid of openai chat for it?
```
---

     
 
all -  [ BIG difference in relevancy scores for same query, same chunks ](https://www.reddit.com/r/LLMDevs/comments/1f1k5fu/big_difference_in_relevancy_scores_for_same_query/) , 2024-08-27-0912
```
Hi

I have used same chunks and tested against 2 embedding models: Voyage 2 in Pinecone DB and then S3 buckets and Titan
 Embeddings. I see a big difference between the relevancy scores of Voyage2/Pinecone and S3/Titan with the Titan having 
lower scores. 

For example, the first chunk retrieved from Pinecone/Voyage had a 0.82 and S3/Titan had a 0.5 and it was
 the same chunk,same query. i'm using langchain's AmazonKnowledgeBasesRetriever for S3/Titan and for pinecone: docsearch
.similarity\_search\_with\_score. Ideally I could increase the score from the AWS setup.

Did anybody have similar issue
s and can explain why such a big difference and where to look to improve?

  

```
---

     
 
all -  [ BIG difference in relevancy scores for same query, same chunks ](https://www.reddit.com/r/LangChain/comments/1f1k5ez/big_difference_in_relevancy_scores_for_same_query/) , 2024-08-27-0912
```
Hi

I have used same chunks and tested against 2 embedding models: Voyage 2 in Pinecone DB and then S3 buckets and Titan
 Embeddings. I see a big difference between the relevancy scores of Voyage2/Pinecone and S3/Titan with the Titan having 
lower scores. 

For example, the first chunk retrieved from Pinecone/Voyage had a 0.82 and S3/Titan had a 0.5 and it was
 the same chunk,same query. i'm using langchain's AmazonKnowledgeBasesRetriever for S3/Titan and for pinecone: docsearch
.similarity\_search\_with\_score. Ideally I could increase the score from the AWS setup.

Did anybody have similar issue
s and can explain why such a big difference and where to look to improve?


```
---

     
 
all -  [ What’s the best way to serve a chat bot when using langchain? ](https://www.reddit.com/r/LangChain/comments/1f1fmvu/whats_the_best_way_to_serve_a_chat_bot_when_using/) , 2024-08-27-0912
```
Is running a rest API the best strategy or are there other methods? 

I’m planning on creating a rest api but curious if
 anyone has any actually useful architecture diagrams or documentation that could lead me in the right direction.

Cheer
s.
```
---

     
 
all -  [ Project 3 | Buddy - AI Chatbot | Level 4 ](https://www.reddit.com/r/myHeadstarter/comments/1f1famk/project_3_buddy_ai_chatbot_level_4/) , 2024-08-27-0912
```
Built an AI-powered chatbot focused on AI knowledge. We used Next.js, Material UI, and MongoDB, integrating OpenAI and A
WS Bedrock APIs with RAG via LangChain and Pinecone. Added prompt engineering and user feedback for refinement.

Try it 
here - [https://ai-chatbot-brown-two.vercel.app/](https://ai-chatbot-brown-two.vercel.app/)
```
---

     
 
all -  [ [Student] Computer Science New-Grad in Spring 2025: Looking for feedback on resume! ](https://www.reddit.com/r/EngineeringResumes/comments/1f12beo/student_computer_science_newgrad_in_spring_2025/) , 2024-08-27-0912
```
I am a US Computer Science student looking to graduate in Spring 2025. I am currently applying for new-grad/entry-level 
positions, primarily in software engineering but also other related roles. Just looking for some general feedback on res
ume to help improve my interview chances as much as possible, thank you! :)

https://preview.redd.it/m1lf6pullukd1.png?w
idth=5100&format=png&auto=webp&s=1f3b983d23cb5dada7e4200cf368ebdd3d842b69


```
---

     
 
all -  [ I am confused as hell (RAG alternative) ](https://www.reddit.com/r/LangChain/comments/1f11ylp/i_am_confused_as_hell_rag_alternative/) , 2024-08-27-0912
```
I am building an e-commerce comparison bot. I am scraping data from leading e-commerce stores. But I am confused how to 
proceed?
My best idea is turning all data into vector embeddings and implementing RAG on it.
But i think it would be rea
lly costly and I might not be able to add changes immediately. Any other way to do this? Without using vector db or any 
other pipeline I could use?
```
---

     
 
all -  [ Need opinion on this approach. How can I improve it? ](https://www.reddit.com/r/LangChain/comments/1f0zfm2/need_opinion_on_this_approach_how_can_i_improve_it/) , 2024-08-27-0912
```
I'm trying to extract the attributes of product from their descriptions like color, volume etc. Normal BERT QA models we
ren't performing well due to bad descriptions. So, I did a small experiment using search tools and agent executor from l
angchain. The results were much better.

Now, I want to implement this on a large scale (a few million datapoints). My c
oncerns are:

1. Latency : Each request takes a few secs and doing this for a million records is a long process. Not to 
mention, I have to give a few shot prompting and the prompt is kinda huge.

2. Robustness: Sending so many api (both ope
nai and search api)  request can crash my code

Is there anything that I can do to make this work in a fast andstable ma
nner? Will LangGraph help? Am I even on the right track?

Thanks!
```
---

     
 
all -  [ Tutor-rific Your RateMyProfessor Ai Assistant | Project 5 | Difficulty 3 ](https://www.reddit.com/r/myHeadstarter/comments/1f0x07n/tutorrific_your_ratemyprofessor_ai_assistant/) , 2024-08-27-0912
```
**🎓 Introducing Tutor-rific: The AI Rate My Professor Assistant Built with Next.js, OpenAI, and Pinecone!**

Hey everyon
e! 🚀

We’re thrilled to introduce our latest project, **Tutor-rific**—an AI-powered assistant designed to enhance the Ra
te My Professor experience like never before. Whether you're a student looking for the best professor or a faculty membe
r interested in feedback, Tutor-rific has got you covered!

# 🛠️ Tech Stack & Tools:

* **Next.js**: Our foundation for 
building a fast and scalable web application.
* **Pinecone**: For lightning-fast vector searches that make querying larg
e datasets a breeze.
* **shadcn/ui**: A sleek and customizable UI framework that gives Tutor-rific a modern and intuitiv
e interface.
* **LangChain**: We used LangChain for seamless integration of language models into our app.
* **TogetherAI
 Embeddings**: To ensure high-quality and context-aware embeddings.
* **Gemma-9b-it Model**: Our go-to model for natural
 language processing, making Tutor-rific smarter and more responsive.
* **React Loading Skeleton**: For a smooth and vis
ually appealing loading experience.
* **Firebase**: Handling all our backend needs, from authentication to real-time dat
abase management.

# 🌟 Features:

* **Instant Professor Insights**: Get detailed information about professors, including
 ratings, feedback, and more.
* **AI-Powered Search**: Quickly find professors that match your criteria using advanced A
I algorithms.
* **Personalized Recommendations**: Tutor-rific can suggest professors based on your past searches and pre
ferences.
* **Real-Time Updates**: Thanks to Firebase, the data is always fresh and up-to-date.

https://preview.redd.it
/xly9yle5gtkd1.png?width=1919&format=png&auto=webp&s=3ada0162f41a4d87a2bc4c3863df24c36e7a3e30

https://preview.redd.it/r
ntkcknxftkd1.png?width=1919&format=png&auto=webp&s=58334f2c9b5175543fb238b53851f53ee80d996b

[Visit The App](http://rate
yourprofessor.vercel.app/)
```
---

     
 
all -  [ How do you like AWS Textract for document parsing? ](https://www.reddit.com/r/LangChain/comments/1f0wd3u/how_do_you_like_aws_textract_for_document_parsing/) , 2024-08-27-0912
```
Document parsing is one of the bigger problems in the RAG domain. There are some great services out there like unstructu
red, LlamaParse and LLMWhisperer. 

One service that does not get mentioned a lot but seems quite powerful, too, is AWS 
Textract. Our first tests look quite promising, we have lots of tabular data to extract which it does quite well.

What 
is your experience with it? Is it a worthy competitor to the aforementioned tools?
```
---

     
 
all -  [ RAG with spreadsheet ](https://www.reddit.com/r/LangChain/comments/1f0uy6f/rag_with_spreadsheet/) , 2024-08-27-0912
```
RAG newbie requesting help from all you pros here🙌 Trying to implement RAG based on an excel spreadsheet (30k x 6). Usin
g llamaparse from llamaindex. My question is that after the indexing step (which takes a sweet while) - where does all t
he data get saved for me to have a lookie? I am used to working with Pinecone where I can log in to my account and see a
ll the indexed items but not sure how llamaindex stores all the indexed info for me to review. 

The implementation code
 (for indexing) is: 
from llama_index.core import VectorStoreIndex
index = VectorStoreIndex.from_documents(documents)
qu
ery_engine = index.as_query_engine()

```
---

     
 
all -  [ 'Unlock Your Potential with Udemy's Free Courses for 25 August 2024! . Don't miss out on this opport ](https://www.reddit.com/r/udemyfreeebies/comments/1f0uadc/unlock_your_potential_with_udemys_free_courses/) , 2024-08-27-0912
```
# Udemy Free Courses for 25 August 2024

Note : Coupons might expire anytime, so enroll as soon as possible to get the c
ourses for FREE.

* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/9432/)Executive Assistant Professional Certificati
on (EAPC)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/4405/)CISA Exam Questions for 2023 – 06 FULL HARD TEST
* [
REDEEM OFFER ](https://idownloadcoupon.com/udemy/13645/)Learn how to create Variables in Modern JavaScript
* [REDEEM OFF
ER ](https://idownloadcoupon.com/udemy/13644/)Marketing Professional Certification
* [REDEEM OFFER ](https://idownloadco
upon.com/udemy/6486/)The Complete ChatGPT Guide From Zero to Hero – 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/u
demy/13598/)JavaScript Soru Bankası: 110 Projeyle Derinlemesine Eğitim
* [REDEEM OFFER ](https://idownloadcoupon.com/ude
my/143/)Most Effective Tips to get your Dream Data Science Job
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/9821/
)CSS, JavaScript And PHP Complete Course For Beginners
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/13643/)JavaSc
ript, jQuery
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/13641/)React CRUD Operation with API Integration
* [RED
EEM OFFER ](https://idownloadcoupon.com/udemy/13642/)Microsoft Excel: Formulas
* [REDEEM OFFER ](https://idownloadcoupon
.com/udemy/8090/)Freelancing Professional Certification
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/5472/)Master
ing Python, Pandas, Numpy for Absolute Beginners
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/10553/)Adobe Illust
rator Essentials: Design Like a Pro in Days
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/7512/)Oracle Java Certif
ication Exam OCA 1Z0-808 Preparation Part2
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/7003/)NumPy, SciPy, Matpl
otlib & Pandas A-Z: Machine Learning
* Sphere Surface Area Unveiled: Basics and Formulas
* [REDEEM OFFER](https://idownl
oadcoupon.com/udemy/10452/)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/9472/)Branding & Brand Marketing Profess
ional Certification (BMPC)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/8332/)Adobe After Effects: From Beginner 
to Motion Master
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/7527/)Python Programming Beyond The Basics & Interm
ediate Training
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/6631/)Probability Beyond the Basics: Part 3
* [REDEE
M OFFER ](https://idownloadcoupon.com/udemy/10633/)CSS – The Complete Guide to CSS for Beginners
* [REDEEM OFFER ](https
://idownloadcoupon.com/udemy/12195/)PCEP (30-02): Entry-Level Python Practice Test – 2024
* [REDEEM OFFER ](https://idow
nloadcoupon.com/udemy/12448/)Python: From Zero to Hero – Code Your Way to the Top
* [REDEEM OFFER ](https://idownloadcou
pon.com/udemy/9467/)Board Member Executive Certification (BMEC)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/9291
/)Mastering One-Variable Equations
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/13638/)Beginner-Friendly LangChai
n Course: Build an AI PDF Document
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/13639/)Spherical Geometry Explore
d: Hemispheres and Their Measures
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/13640/)Insurance Essentials: Under
standing Fire, Marine, and More
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/10620/)Letter Writing Fundamentals
*
 [REDEEM OFFER ](https://idownloadcoupon.com/udemy/10077/)Note Making Demystified: Enhancing Your Study Skills
* [REDEEM
 OFFER ](https://idownloadcoupon.com/udemy/10094/)Crafting Invitations with Elegance and Precision
* Frequency Distribut
ion Mastery: Part 2
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/5777/)
* [REDEEM OFFER ](https://idownloadcoupon.
com/udemy/10621/)Demystifying Computer Viruses: Types, Spread, and Protection
* [REDEEM OFFER ](https://idownloadcoupon.
com/udemy/5918/)Adobe Illustrator Essentials: Zero to Hero for Beginners
* [REDEEM OFFER ](https://idownloadcoupon.com/u
demy/10987/)Executive Diploma in Corporate Entrepreneurship
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/4861/)Ch
oosing Your Career Path: Finding Your True Calling
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/5760/)Presentatio
n Excellence: Navigating the Complete Process
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/13515/)Beyond Basics: 
Calculating Cone Volume with Precision
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/10619/)Cybersecurity Unveiled
: Recognizing Its Vital Importance
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/10070/)Grammar Perfection: Master
ing the Most Common Errors
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/10074/)Diary Writing Benefits: Unlocking 
the Magic of Reflection
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/13632/)Data Center Electrical Design
* [REDE
EM OFFER ](https://idownloadcoupon.com/udemy/13633/)Comprehensive ASP .NET Core MVC Practice Test: Skill Mastery
* [REDE
EM OFFER ](https://idownloadcoupon.com/udemy/13631/)Navigating the Future: A Guide to Thrive in AI-Driven World
* [REDEE
M OFFER ](https://idownloadcoupon.com/udemy/13636/)Secure Networking – A Company Network Project on Open-Source
* [REDEE
M OFFER ](https://idownloadcoupon.com/udemy/13635/)Complete Technical Analysis for Stock Market ( In Hindi )
* [REDEEM O
FFER ](https://idownloadcoupon.com/udemy/13637/)Reverse Engineering and Memory Hacking with Cheat Engine
* Python Quiz C
hallenge for Beginner Job Interview Preparation
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/13629/)
* [REDEEM OFF
ER ](https://idownloadcoupon.com/udemy/13630/)C# Programming Quiz for Beginners Job Interview Preparation
* [REDEEM OFFE
R ](https://idownloadcoupon.com/udemy/13627/)Options Trading Master Class: 2024
* [REDEEM OFFER ](https://idownloadcoupo
n.com/udemy/13628/)Arduino Programming and Circuit Designs using Proteus IDE
* [REDEEM OFFER ](https://idownloadcoupon.c
om/udemy/13625/)Java Quiz Challenge for Beginners Job Interview Preparations
* [REDEEM OFFER ](https://idownloadcoupon.c
om/udemy/13626/)C Programming Quiz for Beginners Job Interview Preparation
* [REDEEM OFFER ](https://idownloadcoupon.com
/udemy/13623/)A Beginners Guide to Landing Guest Spots on Podcasts
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/1
3624/)C Programming Quiz for Beginners Job Interview Preparation
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/136
22/)70-689: Configuring Windows 8.1 Practice Test 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/8931/)GetResp
onse email marketing for beginners
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/6237/)AI Job Seeker: Artificial I
ntelligence Exam Preparation Test
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/12683/)Python Mastery with Tabnine
: AI-Enhanced Coding Efficiency
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/6288/)LATEST | Learn Advanced Python
 Programming | SOURCE CODE
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/11197/)Nodejs: All You Need to Know with 
Practical Project
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/10880/)MERN Stack: All You Need to Know with Pract
ical Project
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/10482/)Data Visualization | Python Matplotlib: Exam Pra
ctice Tests
* Canva Rockstar: Design Like a Pro for Social Media Success
* [REDEEM OFFER](https://idownloadcoupon.com/ud
emy/10655/)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/6238/)Unsupervised Machine Learning Challenge: Exam Prac
tice Test
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/10945/)Google Sheets – The Complete Google Sheets Course
*
 [REDEEM OFFER ](https://idownloadcoupon.com/udemy/7570/)Advanced Adobe Premiere Pro Add Hollywood-level Effects
* [REDE
EM OFFER ](https://idownloadcoupon.com/udemy/12077/)Google Sheets Masterclass: The Power of Excel and Analysis
* [REDEEM
 OFFER ](https://idownloadcoupon.com/udemy/6610/)07 Days of Code | Python Programming BootCamp
* [REDEEM OFFER ](https:/
/idownloadcoupon.com/udemy/6148/)Essential Microsoft PowerPoint Course for Everyone
* [REDEEM OFFER ](https://idownloadc
oupon.com/udemy/3338/)Complete JS Bootcamp | JavaScript Programming in 7 DAYS
* [REDEEM OFFER ](https://idownloadcoupon.
com/udemy/2707/)Easy Guitar for Beginners
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/10030/)Complete Windows Pa
ssword Cracking Course | Practical Guide
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/9448/)Corporate Governance 
Professional Certification (CGPC)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/13621/)How to Get Promoted and Suc
ceed at Work

GET MORE FREE ONLINE COURSES WITH CERTIFICATE – [CLICK HERE](https://idownloadcoupon.com/)
```
---

     
 
all -  [ 'Unlock Your Potential with Udemy's Free Courses for 25 August 2024! . Don't miss out on this opport ](https://www.reddit.com/r/udemyfreebies/comments/1f0ua9u/unlock_your_potential_with_udemys_free_courses/) , 2024-08-27-0912
```
# Udemy Free Courses for 25 August 2024

Note : Coupons might expire anytime, so enroll as soon as possible to get the c
ourses for FREE.

* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/9432/)Executive Assistant Professional Certificati
on (EAPC)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/4405/)CISA Exam Questions for 2023 – 06 FULL HARD TEST
* [
REDEEM OFFER ](https://idownloadcoupon.com/udemy/13645/)Learn how to create Variables in Modern JavaScript
* [REDEEM OFF
ER ](https://idownloadcoupon.com/udemy/13644/)Marketing Professional Certification
* [REDEEM OFFER ](https://idownloadco
upon.com/udemy/6486/)The Complete ChatGPT Guide From Zero to Hero – 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/u
demy/13598/)JavaScript Soru Bankası: 110 Projeyle Derinlemesine Eğitim
* [REDEEM OFFER ](https://idownloadcoupon.com/ude
my/143/)Most Effective Tips to get your Dream Data Science Job
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/9821/
)CSS, JavaScript And PHP Complete Course For Beginners
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/13643/)JavaSc
ript, jQuery
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/13641/)React CRUD Operation with API Integration
* [RED
EEM OFFER ](https://idownloadcoupon.com/udemy/13642/)Microsoft Excel: Formulas
* [REDEEM OFFER ](https://idownloadcoupon
.com/udemy/8090/)Freelancing Professional Certification
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/5472/)Master
ing Python, Pandas, Numpy for Absolute Beginners
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/10553/)Adobe Illust
rator Essentials: Design Like a Pro in Days
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/7512/)Oracle Java Certif
ication Exam OCA 1Z0-808 Preparation Part2
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/7003/)NumPy, SciPy, Matpl
otlib & Pandas A-Z: Machine Learning
* Sphere Surface Area Unveiled: Basics and Formulas
* [REDEEM OFFER](https://idownl
oadcoupon.com/udemy/10452/)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/9472/)Branding & Brand Marketing Profess
ional Certification (BMPC)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/8332/)Adobe After Effects: From Beginner 
to Motion Master
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/7527/)Python Programming Beyond The Basics & Interm
ediate Training
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/6631/)Probability Beyond the Basics: Part 3
* [REDEE
M OFFER ](https://idownloadcoupon.com/udemy/10633/)CSS – The Complete Guide to CSS for Beginners
* [REDEEM OFFER ](https
://idownloadcoupon.com/udemy/12195/)PCEP (30-02): Entry-Level Python Practice Test – 2024
* [REDEEM OFFER ](https://idow
nloadcoupon.com/udemy/12448/)Python: From Zero to Hero – Code Your Way to the Top
* [REDEEM OFFER ](https://idownloadcou
pon.com/udemy/9467/)Board Member Executive Certification (BMEC)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/9291
/)Mastering One-Variable Equations
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/13638/)Beginner-Friendly LangChai
n Course: Build an AI PDF Document
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/13639/)Spherical Geometry Explore
d: Hemispheres and Their Measures
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/13640/)Insurance Essentials: Under
standing Fire, Marine, and More
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/10620/)Letter Writing Fundamentals
*
 [REDEEM OFFER ](https://idownloadcoupon.com/udemy/10077/)Note Making Demystified: Enhancing Your Study Skills
* [REDEEM
 OFFER ](https://idownloadcoupon.com/udemy/10094/)Crafting Invitations with Elegance and Precision
* Frequency Distribut
ion Mastery: Part 2
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/5777/)
* [REDEEM OFFER ](https://idownloadcoupon.
com/udemy/10621/)Demystifying Computer Viruses: Types, Spread, and Protection
* [REDEEM OFFER ](https://idownloadcoupon.
com/udemy/5918/)Adobe Illustrator Essentials: Zero to Hero for Beginners
* [REDEEM OFFER ](https://idownloadcoupon.com/u
demy/10987/)Executive Diploma in Corporate Entrepreneurship
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/4861/)Ch
oosing Your Career Path: Finding Your True Calling
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/5760/)Presentatio
n Excellence: Navigating the Complete Process
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/13515/)Beyond Basics: 
Calculating Cone Volume with Precision
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/10619/)Cybersecurity Unveiled
: Recognizing Its Vital Importance
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/10070/)Grammar Perfection: Master
ing the Most Common Errors
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/10074/)Diary Writing Benefits: Unlocking 
the Magic of Reflection
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/13632/)Data Center Electrical Design
* [REDE
EM OFFER ](https://idownloadcoupon.com/udemy/13633/)Comprehensive ASP .NET Core MVC Practice Test: Skill Mastery
* [REDE
EM OFFER ](https://idownloadcoupon.com/udemy/13631/)Navigating the Future: A Guide to Thrive in AI-Driven World
* [REDEE
M OFFER ](https://idownloadcoupon.com/udemy/13636/)Secure Networking – A Company Network Project on Open-Source
* [REDEE
M OFFER ](https://idownloadcoupon.com/udemy/13635/)Complete Technical Analysis for Stock Market ( In Hindi )
* [REDEEM O
FFER ](https://idownloadcoupon.com/udemy/13637/)Reverse Engineering and Memory Hacking with Cheat Engine
* Python Quiz C
hallenge for Beginner Job Interview Preparation
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/13629/)
* [REDEEM OFF
ER ](https://idownloadcoupon.com/udemy/13630/)C# Programming Quiz for Beginners Job Interview Preparation
* [REDEEM OFFE
R ](https://idownloadcoupon.com/udemy/13627/)Options Trading Master Class: 2024
* [REDEEM OFFER ](https://idownloadcoupo
n.com/udemy/13628/)Arduino Programming and Circuit Designs using Proteus IDE
* [REDEEM OFFER ](https://idownloadcoupon.c
om/udemy/13625/)Java Quiz Challenge for Beginners Job Interview Preparations
* [REDEEM OFFER ](https://idownloadcoupon.c
om/udemy/13626/)C Programming Quiz for Beginners Job Interview Preparation
* [REDEEM OFFER ](https://idownloadcoupon.com
/udemy/13623/)A Beginners Guide to Landing Guest Spots on Podcasts
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/1
3624/)C Programming Quiz for Beginners Job Interview Preparation
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/136
22/)70-689: Configuring Windows 8.1 Practice Test 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/8931/)GetResp
onse email marketing for beginners
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/6237/)AI Job Seeker: Artificial I
ntelligence Exam Preparation Test
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/12683/)Python Mastery with Tabnine
: AI-Enhanced Coding Efficiency
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/6288/)LATEST | Learn Advanced Python
 Programming | SOURCE CODE
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/11197/)Nodejs: All You Need to Know with 
Practical Project
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/10880/)MERN Stack: All You Need to Know with Pract
ical Project
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/10482/)Data Visualization | Python Matplotlib: Exam Pra
ctice Tests
* Canva Rockstar: Design Like a Pro for Social Media Success
* [REDEEM OFFER](https://idownloadcoupon.com/ud
emy/10655/)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/6238/)Unsupervised Machine Learning Challenge: Exam Prac
tice Test
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/10945/)Google Sheets – The Complete Google Sheets Course
*
 [REDEEM OFFER ](https://idownloadcoupon.com/udemy/7570/)Advanced Adobe Premiere Pro Add Hollywood-level Effects
* [REDE
EM OFFER ](https://idownloadcoupon.com/udemy/12077/)Google Sheets Masterclass: The Power of Excel and Analysis
* [REDEEM
 OFFER ](https://idownloadcoupon.com/udemy/6610/)07 Days of Code | Python Programming BootCamp
* [REDEEM OFFER ](https:/
/idownloadcoupon.com/udemy/6148/)Essential Microsoft PowerPoint Course for Everyone
* [REDEEM OFFER ](https://idownloadc
oupon.com/udemy/3338/)Complete JS Bootcamp | JavaScript Programming in 7 DAYS
* [REDEEM OFFER ](https://idownloadcoupon.
com/udemy/2707/)Easy Guitar for Beginners
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/10030/)Complete Windows Pa
ssword Cracking Course | Practical Guide
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/9448/)Corporate Governance 
Professional Certification (CGPC)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/13621/)How to Get Promoted and Suc
ceed at Work

GET MORE FREE ONLINE COURSES WITH CERTIFICATE – [CLICK HERE](https://www.reddit.com/r/udemyfreeebies)
```
---

     
 
all -  [ PDF > Chunks > Markdown? ](https://www.reddit.com/r/LangChain/comments/1f0r0dt/pdf_chunks_markdown/) , 2024-08-27-0912
```
I’m building a legal research tool and need to show the end user a bounding box (rectangle) around citations.

Using Uns
tructured I can chunk PDF files and also get the bounding boxes, but the content is raw text.

Any suggestions for a bet
ter content pipeline?
```
---

     
 
all -  [ Agent communications in prompt text style instead of following a standard ](https://www.reddit.com/r/LangChain/comments/1f0qmgf/agent_communications_in_prompt_text_style_instead/) , 2024-08-27-0912
```
I have been running several langchain agent examples. They bomb time to time as one agent doesn't get the style of messa
ge or action it needs

Isn't a better approach to have strict communications between agents this is driven by llm not th
rough prompts as llm is able to ignore or hallucinate on prompts now

Are there any llm that are designed for a communic
ation protocol like static type function arguments
```
---

     
 
all -  [ Deployment to fireworks.ai  ](https://www.reddit.com/r/LangChain/comments/1f0qdon/deployment_to_fireworksai/) , 2024-08-27-0912
```
Is there some guide on how to deploy model to [fireworks.ai](http://fireworks.ai) ? Their docs are very unclear to me
```
---

     
 
all -  [ Rethinking Markdown Splitting for RAG: Context Preservation ](https://www.reddit.com/r/Rag/comments/1f0q2b7/rethinking_markdown_splitting_for_rag_context/) , 2024-08-27-0912
```
Hey everyone,

Recently I've been working on improving our RAG platform (filebrain.pro), and I wanted to share some insi
ghts and get your thoughts on a problem I've been tackling: markdown splitting.

**The Problem**

I started by using Lan
gChain's MarkdownHeaderSplitter, which is a solid tool.  
However, I noticed that the reference between text blocks was 
only at the metadata level. This led to some issues:

1. Loss of hierarchical context when chunks were processed indepen
dently
2. Increased complexity in pre- and post-processing of context
3. Challenges for LLMs in understanding the relati
onships between blocks and headers

**The Solution Attempt**

To address these issues, I've implemented a custom splitte
r that embeds references at the text/context level. Here's how it works:

1. Instead of just splitting on headers, we pr
eserve the full path of headers for each chunk.
2. Each chunk now looks something like this:

&#8203;

    Copy[H1] Main
 Topic > [H2] Subtopic > [H3] Specific Point
    Actual content of the chunk...

1. This approach maintains the hierarch
ical context within each section.
2. It ensures every chunk retains its full contextual integrity, even when processed i
ndependently.

**The Benefits**

1. Improved context retention: Each chunk now 'knows' where it belongs in the overall d
ocument structure.
2. Better retrieval accuracy: The embedded context allows for more precise matching during retrieval.

3. Reduced processing overhead: Less need for complex pre- and post-processing (using metadata) to maintain context.
4.
 Enhanced LLM understanding: The explicit hierarchy makes it easier for LLMs to grasp the relationships between differen
t parts of the document.

**Technical Implementation**

Here's a high-level overview of how I implemented this:

1. Pars
e the markdown to create a tree structure of headers and content.
2. Traverse the tree, building the header path as we g
o.
3. For each content block, prepend the current header path.
4. Split the content into chunks of appropriate size, ens
uring we don't split in the middle of sentences.
5. Each chunk retains the prepended header path.

**Questions for the C
ommunity**

1. Has anyone else experimented with similar context-preserving techniques for other document types splittin
g?
2. What potential drawbacks or edge cases should I be aware of with this approach?
3. How do you handle very deeply n
ested structures where the header path might become quite long?

I'm really excited about the potential of this approach
, but I'm also aware that there might be aspects I'm overlooking. I'd love to hear your thoughts, experiences, or critiq
ues.

Thanks
```
---

     
 
all -  [ [4 YoE] International Student in US looking for a new job. Not getting interview calls. Any feedback ](https://www.reddit.com/r/EngineeringResumes/comments/1f0nbth/4_yoe_international_student_in_us_looking_for_a/) , 2024-08-27-0912
```
As mentioned in my resume I am an international student with 4.2 years of hands-on experience in software development. C
urrently, I am working with a startup to gain additional experience, though this role is unpaid. Over the past 8 months,
 I have been actively searching for a full-time position but, unfortunately, have not received many responses. I am look
ing for advices or suggestions to improve my resume. Any feedback is much appreciated!!

https://preview.redd.it/s42isjh
9dqkd1.jpg?width=4967&format=pjpg&auto=webp&s=0231263d69e8b43cfa3f1790bae1b57df0a1e9af


```
---

     
 
all -  [ Problems Getting Hermes 3 405B's API Key ](https://www.reddit.com/r/LangChain/comments/1f0arfb/problems_getting_hermes_3_405bs_api_key/) , 2024-08-27-0912
```
i've been trying to get the API of Hermes 3 405B Instruct since it is completely free but i don't understand what i am s
upposed to do with this code. i asked ChatGPT but its guide was not clear and very general

[https://openrouter.ai/model
s/nousresearch/hermes-3-llama-3.1-405b/api](https://openrouter.ai/models/nousresearch/hermes-3-llama-3.1-405b/api)

You 
can also use OpenRouter with OpenAI's client API:

    import OpenAI from 'openai'
    
    const openai = new OpenAI({

      baseURL: 'https://openrouter.ai/api/v1',
      apiKey: $OPENROUTER_API_KEY,
      defaultHeaders: {
        'HTTP-
Referer': $YOUR_SITE_URL, // Optional, for including your app on openrouter.ai rankings.
        'X-Title': $YOUR_SITE_N
AME, // Optional. Shows in rankings on openrouter.ai.
      }
    })
    async function main() {
      const completion 
= await openai.chat.completions.create({
        model: 'nousresearch/hermes-3-llama-3.1-405b',
        messages: [
    
      { role: 'user', content: 'Say this is a test' }
        ],
      })
    
      console.log(completion.choices[0].m
essage)
    }
    main()
```
---

     
 
all -  [ 2025 graduate, not much luck in internships or placements ](https://i.redd.it/unfpislgumkd1.png) , 2024-08-27-0912
```
is there anything i should update in my resume? i did modify it according to some points on resumeworded
```
---

     
 
all -  [ Suggestions for implementing RAG with cobra ](https://www.reddit.com/r/golang/comments/1f06pnv/suggestions_for_implementing_rag_with_cobra/) , 2024-08-27-0912
```
Hello everyone!
I recently started learning go and made some simple CLI tools using cobra. Recently I got a project idea
 where I would want to have a RAG implementation for users directories and allow users to query them. 

Now I want to im
plement this directly using the CLI, as a start I was thinking to save the vector database directly on the local machine
 of the user but will probably move it to the cloud later. 

But considering the complexity of this and also given that 
files and the content of those files may change often, I have a few questions:

1) First and foremost, how can I even im
plement this? I am also new to RAG and have only implemented it using libraries like langchain.

2) Is it really feasibl
e to do this? And should I even give it a try?

3) Is there anything like this which already exists?

Thankyou!
```
---

     
 
all -  [ Real Estate Dataset Required  ](https://www.reddit.com/r/LangChain/comments/1f04t36/real_estate_dataset_required/) , 2024-08-27-0912
```

Hey Everyone 


I'm working on a real estate chatbot focused on providing general knowledge about property ownership la
ws, mortgage laws, interest rates, and taxes, specifically for the UK. The bot is intended to help users with verbal inf
ormation on how to buy a house, understand mortgage rates, and navigate related legal aspects.

However, I'm finding it 
challenging to locate a dataset that covers these legal and financial topics, as most available datasets are geared towa
rds price predictions. 

Does anyone know where I might find a dataset related to property laws, mortgage regulations, t
ax information, or similar topics? Any leads would be greatly appreciated!

Thanks in advance for your help.


```
---

     
 
all -  [ How to integrate a personalised prompt with LangChain and a vector database like Pinecone for a chat ](https://www.reddit.com/r/LangChain/comments/1f02d8b/how_to_integrate_a_personalised_prompt_with/) , 2024-08-27-0912
```
Hello everyone,

I am working on a chatbot project for an e-commerce site specialising in the sale of gourds. My goal is
 to create a virtual assistant named Max, which helps users find products and answer their questions by using data store
d in a vector database, Pinecone.

Problem:

Setting up the Chatbot Instructions: I have defined a personalised prompt w
ith a system message for the chatbot to follow specific instructions (for example, 'You are Max, an assistant in an e-co
mmerce store that sells gourds...'). However, I have difficulty formatting this prompt correctly so that the chatbot und
erstands the questions asked by the user and responds contextually.

What I have already tried:

•	 Using LangChain's Ch
atPromptTemplate: I formatted the prompt using ChatPromptTemplate.from_messages to structure the roles of messages ('sys
tem', 'human', 'ai'). The chatbot follows the system's instructions well, but it does not seem to integrate user data in
to its responses.

•	 Conversation History Management: I have put in place a mechanism to keep a conversation history, b
ut this does not seem to improve the chatbot's responses that remain generic.

Questions:

1.	 How can I better integrat
e a personalised prompt so that the chatbot correctly answers users' questions while tracking the stored data?

2.	 What
 is the best practice to ensure that the chatbot effectively uses the recovered data from Pinecone and the prompt provid
ed to generate a good response?

Any feedback, advice or code examples would be greatly appreciated!

Thank you very muc
h!
```
---

     
 
all -  [ How do you visualize agentic communications ](https://www.reddit.com/r/LangChain/comments/1ezzcdj/how_do_you_visualize_agentic_communications/) , 2024-08-27-0912
```
I am using Langgraph to do agent setup with several agents. What is the best way to visualize the steps done by differen
t agents, 
```
---

     
 
MachineLearning -  [ [P] using GPT4o with langchain/chroma for sports analysis  ](https://www.reddit.com/r/MachineLearning/comments/1enuzlp/p_using_gpt4o_with_langchainchroma_for_sports/) , 2024-08-27-0912
```
Hi all, I'm working on a side project that helps with sports analysis for historical games, which in turn will help with
 sports betting. Currently I've been only focused on MLB because I wanted to see how the use case would pan out.

My fir
st attempt at this was to use the openai endpoint and load all the relevant JSON objects and send a prompt along with th
em to GPT and see what I get back. Eventually, the context size was getting way too big and the problem I was running in
to was that it was expensive. Although, the prompts back were actually pretty decent and relevant to the data.

My secon
d attempt was to setup a RAG using Chroma/LangChain/GPT4o. I got it to work but the answers all seem very off and super 
vague. None of the data I have was shown in any of the prompts i asked, or any of the players that were playing in a gam
e were mentioned at all in the prompt back, plus it kept mentioning wrong games/teams whe asking it specific games. I’m 
assuming I might need to adjust the vector store a bit but not sure how I can do that with chroma.

My question is what 
might be the best way to setup some sort of process? My end result, I would like a response back using the historical da
ta I've provided to make assumptions on what a game could be like based off all the stats given, with some room for GPT 
to also make some inference as well.

I am a super new at this so it's been a learning process so far; please bear with 
me.
```
---

     
 
MachineLearning -  [ [R] [D] Langchain Evaluation with BeyondLLM
 ](https://www.reddit.com/r/MachineLearning/comments/1eki1fv/r_d_langchain_evaluation_with_beyondllm/) , 2024-08-27-0912
```
Hey everyone! Just came across a new feature of Beyond LLM that can evaluate Langchain RAG pipelines! It provides contex
t relevancy, answer relevancy, and groundedness. Check out the code snippet I’m sharing—perfect for testing your RAG pip
elines! For more info, be sure to check it out on GitHub [here](https://github.com/aiplanethub/beyondllm/blob/main/cookb
ook/evaluate_langchain_rag_pipeline_beyondllm.ipynb).

https://preview.redd.it/172m1y3dvsgd1.png?width=3972&format=png&a
uto=webp&s=63d5b0f41f0e46a58e7a2d5fb0d2bbc4384b3b1d


```
---

     
 
deeplearning -  [ Creating a project on NLP ](https://www.reddit.com/r/deeplearning/comments/1ey2e85/creating_a_project_on_nlp/) , 2024-08-27-0912
```
So me and my friend completed the ML and DL specialization by AndrewNg, and were just gonna get started on a project. We
 decided to make a academic assistant. So basically what this does is a user can upload a PDF,text file or any other sup
ported media and the can ask questions related to it's contents. The main objective being making learning quick given la
rger documents.

The pipeline we decided is pretty standard for such a project.

1. Split the text into chunks
2. Genera
te embeddings of the chunks
3. Store the chunks in a vector DB
4. Find the top K similar chunks to the query 
5. Retriev
e context and feed it into a LLM for an answer.

So I looked up for a library and framework to use and decided on langch
ain. We haven't decided on an LLM yet but want to run it locally so no OpenAI please. 

Since this is gonna be out first
 AI project confidence is low. I would really appreciate any heads up on the issues we may face, any suggestions on libr
aries,frameworks or models will be really helpful as well. 

Appreciate any resourceful comment 😊
```
---

     
 
deeplearning -  [ How To Build Your Retrieval Augmented Generation (RAG) Using Open-source Tools: LangChain, LLAMA 3,  ](https://www.reddit.com/r/deeplearning/comments/1emdotx/how_to_build_your_retrieval_augmented_generation/) , 2024-08-27-0912
```


TL;DR: RAG overcomes the limitations of LLMs by bringing in external sources of information as relevant context.  
  

At the end of the step-by-step tutorial, you will be able to give your favorite LLM (ChatGPT, LLAMA 3, Mixtral, Gemini, 
Claude, etc.) some documents, ask it a question and see it respond based on relevant context.  
  
This will be running 
locally, using open-source libraries. Zero API and tooling costs.

[Step-by-step Notebook with zero-cost RAG](https://co
decompass00.substack.com/p/build-open-source-rag-langchain-llm-llama-chroma)

![img](69v6kjfj3wgd1)


```
---

     
 
deeplearning -  [ Need help with creating CLI for 'non-programmers' (LLMs) ](https://www.reddit.com/r/deeplearning/comments/1elrfgm/need_help_with_creating_cli_for_nonprogrammers/) , 2024-08-27-0912
```
***TL;DR*** What is the best way to convert user input into sequence of commands and their corresponding parameters? Lik
e, imagine you are not a programmer and there is a console app with a CLI, but, well, you don't know the structure and t
he syntax of commands. And you don't want to know. YBut! You have a locally running instance of llama3.1 -- or whatever 
open LLM is out there now -- and you can ask it to create a CLI command for you. What would you do to accomplish that?


**Intro**

A little bit of context. I'm working on a project that targets scientists as end users. It has some UI using 
which it's possible to do all sort of things the lab workers would like to do. But recently the projects product owner d
ecided that it would be cool to have a small chat window that is accessable basically everywhere throughout the applicat
ion UI in which 'lives' a bot that can accept some input from a user and do what is requested. The pool of commands is f
inite and predefined.

**The issue**

So, putting details aside, the main issue to be solved is parsing user input (unst
ructured and possible incomplete data) to some structured form. In general, each and every user input should be transfor
med into a data structure that represents a sequence of commands with their parameters, for example:

User input: Please
, create X with param1 set to value1 and param2 equal to value2

Desired output:

    create_x --param1 value1 --param2 
value2

In this example, there is only one command, but in real life the request can represent a sequence of N commands,
 and they may depend on each other (sequence of execution does matter)

**What I've tried so far**

I have an 'experimen
t' environment: a python project with `ollama` and `langchain` installed. The main model I test is llama3.1-instruct wit
h 5bit quantization. (I'm sort of limited with hardware resourses, so XXB parameter models do not fit).

Up until now, I
've tried to achieve what I want with prompting in different forms, but in general I do the following:

1. As the very f
irst message in the chat, I create a 'system' one which explain what commands are there. The format is the following (I 
replaced original data not to expose the context more, so it's very generic): 

```xml
<scope>
    <models>
        <mod
el name='entityA'>
            <field name='uniqueId' type='string' description='unique identifier for entityA'/>
      
      <field name='label' type='string' description='label for entityA'/>
            <field name='category' type='enum'
 possible-value='alpha, beta, gamma, delta'/>
        </model>
        <model name='entityB'>
            <field name='u
niqueId' description='unique identifier for entityB'/>
            <field name='entityAIds' type='array' description='id
entifiers of entityAs associated with this entityB'/>
        </model>
    </models>
    <commands>
        <command nam
e='create_entityA' description='creates an instance of entityA'>
            <param name='uniqueId' type='string' descri
ption='unique identifier for entityA'/>
            <param name='label' type='string' description='label for entityA' re
quired='true'/>
            <param name='category' type='enum' possible-values='alpha, beta, gamma, delta'
             
      description='category of entityA (one value from the possible values list)' required='true'/>
        </command>
 
       <command name='remove_entityA' description='removes an instance of entityA by its unique identifier'>
           
 <param name='uniqueId' description='unique identifier of the entityA to be removed'
                   required='true'/
>
        </command>
        <command name='create_entityB'>
            <param name='label' description='label for enti
tyB'/>
        </command>
        <command name='link_entityAs_to_entityB'
                 description='associates inst
ances of entityA with a specific entityB based on the provided unique identifier of entityB'>
            <param name='u
niqueId' description='unique identifier of the entityB to which entityAs should be associated'
                   requir
ed='true'/>
            <param name='entityAIds'
                   description='an array of unique identifiers of entit
yAs to associate with the entityB'
                   type='array'
                   required='true'/>
        </comman
d>
        <command name='navigate' description='indicates that a user wants to go to a specific section of the platform
'>
            <param name='section' possible-values='entitiesA, entitiesB, configuration' required='true'/>
        </c
ommand>
        <command name='support' description='should be executed when a user seeks assistance on available functi
ons'/>
    </commands>
</scope>
```

So, now the model is provided with some context. Then, also in the 'system' message
 I:

* 'tell' the model that user input should be converted into a sequence of commands along with the corresponding par
ameters, all of this is described in the XML above
* describe the desired output format
* try to enforce some restrictio
n and cover edge cases

**The question part**

*Is this approach* ***viable***\*?\*

If yes, maybe there are some ***way
s to improve it***?

If not, *what would be* ***the alternative***?

So far I don't see how to apply fine tuning here

T
hank you in advance!
```
---

     
