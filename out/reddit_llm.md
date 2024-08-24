 
all -  [ How to work with API Data  ](https://www.reddit.com/r/Rag/comments/1ezpkyy/how_to_work_with_api_data/) , 2024-08-24-0911
```
Hey, I’m working on a platform where users can connect their Ads accounts, allowing us to retrieve and store their ad da
ta. Users can then interact with a chatbot to ask questions like 'How did my ads perform last week?' or 'What can I do t
o improve performance?' The chatbot provides answers based on the available data context.

Currently, I’m using a RAG ap
proach, where I chunk the data, store it in a vector database, and use LangChain to create the pipeline with a prompt te
mplate. However, I’m running into issues where the chatbot sometimes generates incorrect responses, and I’m also encount
ering token limit errors.

I’m looking for alternative methods to address these problems and would really appreciate you
r insights and feedback on this.
```
---

     
 
all -  [ Is it worth dedicating time to learn Langchain with the constant influx of new AI frameworks? ](/r/LangChain/comments/1brew3a/is_it_worth_dedicating_time_to_learn_langchain/) , 2024-08-24-0911
```

```
---

     
 
all -  [ How to pass multiple inputs during invoke  to a MessageGraph(langraph) ](https://www.reddit.com/r/LangChain/comments/1ezn36b/how_to_pass_multiple_inputs_during_invoke_to_a/) , 2024-08-24-0911
```
We have a MessageGraph for an LLMCompiler implementation and as expected we pass a users's question when running invoke 
as a list of HumanMessage objects(which are mapped to a default 'messages' key and passed to prompt templates), this wor
ks fine for simple use cases but now we need to pass an additional piece of information/context at invoke time(not at gr
aph  building time), we did something similar with a react agent and it was very easy passing a dictionary similar to `i
nvoke({'messages':input, 'context':context})`. But for MessageGraph this did not work, it looks as the list of messages 
passed when you run `invoke(messages)` is automatically mapped in the prompt to the 'messages' key and no other inputs c
an be added, I tried passing a dicionary  `invoke({'messages':messages, 'context':context})` and it did not work, failed
 with error:

     Message dict must contain 'role' and 'content' keys, got {'messages':messages,'context':context}

Any
 ideas on how to pass multiple inputs(that are mapped to prompts) in a MessageGraph at invoke time?  

```
---

     
 
all -  [ [1 YoE] DS Student Searching for over a Year with over 500 Applications only 3 Interviews With No Of ](https://www.reddit.com/r/EngineeringResumes/comments/1ezmwfb/1_yoe_ds_student_searching_for_over_a_year_with/) , 2024-08-24-0911
```
Reading the wiki definitely helped me out but I'm still at a loss, my friends who are good engineers say my resume looks
 pretty nice, and they have given me recs for their companies, those were the 3 interviews I had. So idk what to do next
 besides post here because I have yet to get an interview from applications.

Willing to do basically anything data scie
nce, analytics or engineering related since I have experience doing basically all of it, would prefer SWE role but I'll 
take anything, even internships, that can help me pay off debt. Should I have multiple copies of my resume for different
 types of applications?

I put software engineer for my top experience role even though I founded the company (venture b
acked, so a mild accomplishment) because I figured it would perform better in ATS, is this correct line of thinking?

Fi
nally, Is there anything that I'm overtly missing here? This is the second time I overhauled my resume, I think it looks
 pretty good now! but I wanted to check here before I send more applications out. Any advice is helpful- I am grateful t
o hear anything. thank you if you read this far!!!!

https://preview.redd.it/yepwpfb04hkd1.png?width=5100&format=png&aut
o=webp&s=0295e6f76a4302332cda3a0209b6aeae7d77766c


```
---

     
 
all -  [ How can we ensure that only humans are interacting with the chatbot?  ](https://www.reddit.com/r/LangChain/comments/1ezm79b/how_can_we_ensure_that_only_humans_are/) , 2024-08-24-0911
```
Hi all,

A bit of a novice when it comes to building fully developed applications, but in talking to a potential client 
I had this question come up. When implementing a chatbot on a clients site, How can we ensure that only humans are inter
acting with the chatbot and only traffic from their website?

They are worried about usage costs, and want to avoid any 
sort of brute force attack that would blow their budget out of the water. Could we put a limit on queries per user sessi
on? Is there a plug and play captcha service we could add to the page?

Any advice would be useful, and if there are oth
er good subs I’d love to hear about them!
```
---

     
 
all -  [ Looking for researchers and members of AI development teams to take part in an IRB approved user stu ](https://www.reddit.com/r/LangChain/comments/1ezm4pb/looking_for_researchers_and_members_of_ai/) , 2024-08-24-0911
```
We are looking for researchers and members of AI development teams who are at least 18 years old with 2+ years in the so
ftware development field to take an anonymous survey in support of my research at the University of Maine. This may take
 20-30 minutes and will survey your viewpoints on the challenges posed by the future development of AI systems in your i
ndustry. If you would like to participate, please read the following recruitment page before continuing to the survey. U
pon completion of the survey, you can be entered in a raffle for a $25 amazon gift card.

[https://docs.google.com/docum
ent/d/1Jsry\_aQXIkz5ImF-Xq\_QZtYRKX3YsY1\_AJwVTSA9fsA/edit](https://docs.google.com/document/d/1Jsry_aQXIkz5ImF-Xq_QZtYR
KX3YsY1_AJwVTSA9fsA/edit)
```
---

     
 
all -  [ Building Reliable GenAI Agents using Knowledge Graphs ](https://www.reddit.com/r/LangChain/comments/1ezhaji/building_reliable_genai_agents_using_knowledge/) , 2024-08-24-0911
```
Hey folks, here from [cogniswitch.ai](http://cogniswitch.ai) we help automate the Genai pipeline completely from Ingesti
on to retrieval. We've got our tool listed on LangChain, if you'd like to check it out here's a link: [https://python.la
ngchain.com/v0.2/docs/integrations/tools/cogniswitch/](https://python.langchain.com/v0.2/docs/integrations/tools/cognisw
itch/)

We'll be hosting an interactive session that helps developers build out reliable genAI agents. It will be a comp
lete hands-on session so you can ask questions and work in a sandbox environment to try it yourself. If anyone is intere
sted or wants to learn we'd be happy to help, There will be no sales pitch or gimmicks, just a hands-on developer event:
 [https://nuvepro.com/register-for-our-genai-e-workshop-building-genai-chatbots-using-knowledge-graphs/](https://nuvepro
.com/register-for-our-genai-e-workshop-building-genai-chatbots-using-knowledge-graphs/)
```
---

     
 
all -  [ LLMs to query databases from natural language ](https://www.reddit.com/r/LangChain/comments/1ezg5xd/llms_to_query_databases_from_natural_language/) , 2024-08-24-0911
```
Hi everyone,

I'm looking to build an application where a natural language question from a non-technical user (with no b
ackground in databases or programming) is converted by a LLM into a query that retrieves the correct information from a 
database. I understand this concept isn't entirely new, and I'm sure many of you have already developed something simila
r. That's why I'd love to hear your recommendations on how to implement it and how you handle common challenges in this 
area.

For example, how do you ensure the generated query is secure? How do you improve query accuracy when dealing with
 complex databases? Also, would an approach using RAG or Knowledge RAG be effective for this use case?

Thanks in advanc
e for your insights!
```
---

     
 
all -  [ Multi-Agent Supervision (OpenAI Assistants: Directly) ](https://www.reddit.com/r/LangChain/comments/1ezfuzz/multiagent_supervision_openai_assistants_directly/) , 2024-08-24-0911
```
I've been trying to use OpenAI Assistants as agents in langchain but I'm having trouble connecting to a specific existin
g Assistant, with a pre-existing assistant ID. Do we know if there is a solution to make this setup work? Thank you in a
dvance.
```
---

     
 
all -  [ Has anyone used RAPTOR for RAG? ](https://www.reddit.com/r/LangChain/comments/1ezdd5t/has_anyone_used_raptor_for_rag/) , 2024-08-24-0911
```
The official implementation on Github: [https://github.com/parthsarthi03/raptor](https://github.com/parthsarthi03/raptor
) is not complete, and I am not really sure how to work around with multiple documents (I have over 100+). 

If anyone h
as a full implementation of RAPTOR that uses local or open source hugging face models please do share it.
```
---

     
 
all -  [ Help me learn Python , Langchain , RAG the correct way  ](https://www.reddit.com/r/Rag/comments/1ezciy1/help_me_learn_python_langchain_rag_the_correct_way/) , 2024-08-24-0911
```
Hi , I'm a web dev coming from a JS background currently learning GenAI ( mainly RAG ) .

As of today , its been around 
2 months of me learning Langchain , Streamlit and RAG concepts . I skipped Python as I thought I would learn it on the g
o .

Now , even after 2 months , I feel like I'm confident enough and maybe there is problem in my learning approach . h
elp me fix it .  
  
How much should I know and be able to do after 2 months of learning GenAI ?   
  
I've developed so
me RAG related apps learning from the tutorials available on YT , but I'm not able to build something on my own . the RA
G apps that I wrote ...some of them with \~500 LOC ... aren't modular ... fun fact is that I don't even know how to make
 it modular :> 

I need help with 2 things for now

First ... how much python do I need to learn to get comfortable ...c
an anyone tell me the best tutorial for learning Python ( GenAI specific )   
  
Second ... can anyone guide me on how t
o write modular code 

Thanks in advance !
```
---

     
 
all -  [ How to improve the accuracy and working of sql agent?  ](https://www.reddit.com/r/LangChain/comments/1eza5m4/how_to_improve_the_accuracy_and_working_of_sql/) , 2024-08-24-0911
```
Please share your experience how to make sql agent deal with user queries related to around 4 5 tables accurately. 

Wha
t steps or tips are important for me to consider. 

How to prompt sql agent. 
How to make the sql agent work faster as i
t is much slower, it first lists tables etc.

How to make sql agent handle errors when executing sql queries. 

How to m
ake sql agent have greater understanding of all of our tables.

Sql agent uses a step where it fetches some few rows of 
all our tables and unfortunately these few rows do not represent all of the data in our tables. And these rows sometimes
 negativity affect the sql agent accuracy. 

And what about few shots of user queries along with correct SQL queries pro
vided to SQL agent for better understanding. 

Please experts guide. 
```
---

     
 
all -  [ Long, expensive, awesome ](https://www.reddit.com/r/LangChain/comments/1ez9onz/long_expensive_awesome/) , 2024-08-24-0911
```
I know exactly how to build an awesome RAG. It’s as easy as a pie.

First, prepare your data. Let’s say you’re using smt
h like [unstructured.io](http://unstructured.io), hi\_res option. Your, oh, about 400 pdf files will be processed in jus
t a week or so, maybe a bit more… No biggie.

Make sure to use some smart chunking. Smth semantic, with embedings from O
penAI. I mean, come on, even a kid knows that.

But! Data prep doesn't stop there! You want it awesome,right? Every chun
k needs to go through some LLM magic. Analyze it, enrich it so that every chunk is like Scrooge McDuck diving into his m
oney bin. Keywords, summarization, all that jazz. Pick a pricey LLM, don’t be stingy. You want awesome, don’t you?

Ok, 
now for search. Simple stuff. Every query needs to be rephrased by LLM, like, 5-7 times, maybe 10. Less is pointless. So
 - each query will give you 10 new ones,but what a bunch!

Then, take them all into vector search. And the results? You 
guessed it! Straight into Cohere reranker! We’re going for awesome, remember? Don’t forget to merge the results.

And no
w, for the final touch - LLM on the output. Here is my suggestion: pick a few models, let each one do its job. Then, use
 yet another model to pick the best one. Or, you know, whichever…

And the most important rule - no open source, only pr
oprietary, only hardcore!

P.S. Under every Reddit post, there’s always a comment saying, “Clearly, this post was writte
n by ChatGPT.” Don’t bother. This post was entirely crafted by ChatGPT, no humans involved.

P.P.S. For those who made i
t through all these words - here’s a confession. I never do it that way. It's too long, costly, and complicated for me. 
I prefer the easy way. In fact, right now some friends of mine have invited me to test their RAG API. I load data in the
re and get a ready Search API - query as input, ready-made RAG context as output. That's what I realy like. I'm trying i
t for free now, and I look forward to the community edition in the future. Everything works pretty quickly. I'm testing 
the quality of the search now. If the quality is OK, I can tell about it here.
```
---

     
 
all -  [ Seeking guidance to learn LLMs ](https://www.reddit.com/r/LangChain/comments/1ez7e7h/seeking_guidance_to_learn_llms/) , 2024-08-24-0911
```
Hi everyone. I am new to field of LLMs. I am seeking some guidance on how and where to start from. I hear a lot of termi
nology like RAG, agents etc but have no idea of where to start. Kindly guide me with some starting points/repos.
```
---

     
 
all -  [ Is there currently a way to smoothly handle tool calling while using a vLLM?  ](https://www.reddit.com/r/LangChain/comments/1ez7cb6/is_there_currently_a_way_to_smoothly_handle_tool/) , 2024-08-24-0911
```
Or is it just not possible at the moment? I know it has been on the vLLM roadmap for a while now, so is it just not poss
ible yet to integrate vLLMs while working with langchain components such as react\_agents that automatically handle tool
s and functions calling?   
Specifically, I'm trying to make the application I built using OpenAI API to work also when 
using a vLLM serving Llama-3.1-8B-Instruct, but it clearly cannot handle function calls in the same way the API does. Is
 the only solution at the moment to build workarounds like this? [https://python.langchain.com/v0.2/docs/how\_to/tools\_
prompting/](https://python.langchain.com/v0.2/docs/how_to/tools_prompting/)
```
---

     
 
all -  [ Agency - Reliable, safe, & compliant AI Agents ](https://www.reddit.com/r/u_Wesubmit/comments/1ez5f6a/agency_reliable_safe_compliant_ai_agents/) , 2024-08-24-0911
```
Agency helps enterprises build, evaluate, and monitor AI agents. From the team at [AgentOps.ai](http://agentops.ai/).

[
Agen.cy](http://agen.cy/) (Agency AI) develops cutting edge AI agents using CrewAI, AutoGen, CamelAI, LLamaIndex, Langch
ain, Cohere, MultiOn + many more. 
```
---

     
 
all -  [ How do I get a custom attributes preserved in the HumanMessage object passed to the BaseChatMessageH ](https://www.reddit.com/r/LangChain/comments/1ez24hc/how_do_i_get_a_custom_attributes_preserved_in_the/) , 2024-08-24-0911
```
Hello, I am a newbie just started to use python LangChain. I am trying to pass a custom attribute (e.g. the timestamp wh
en the human prompt was received) through a chain with history enabled, so when LangChain calls add\_messages() on our B
aseChatMessageHistory implementation the HumanMessage object in the \[messages\] would have that attribute in its additi
onal\_kwargs.

I thought I could pass in the custom attribute when I make the template: 


HumanMessagePromptTemplate.fr
om\_template('{temp}', additional\_kwargs={'myattr': 'myval'})


but the HumanMessage object received by add\_messages()
 had an empty additional\_kwargs.

I must be on the wrong track. Is there a way to achieve this? Thanks!

```
---

     
 
all -  [ How can I parse Unstructured document? ](https://www.reddit.com/r/LangChain/comments/1eyyv3d/how_can_i_parse_unstructured_document/) , 2024-08-24-0911
```
I've been studying RAG (Retrieval-Augmented Generation) for just under a month now. I've recently completed the Langchai
n tutorial and created a simple toy project using Streamlit. I understand that to improve RAG performance, adjustments a
re needed in various areas: query tuning, document parsing, vector store optimization, retriever fine-tuning, and genera
tor improvements.



Currently, I'm focusing on learning how to effectively parse documents. During the Langchain tutori
al, I thought it was as simple as loading documents with PDFLoader and then using RecursiveTextSplitter or SemanticChunk
er on each Document object. However, I've come to realize that parsing PDFs in a way that mirrors human understanding an
d storing them in a vector store is much more challenging due to the unstructured nature of PDFs.



I've been researchi
ng three main issues through YouTube, Reddit, and Google:



1. How to process multi-column documents

2. How to handle 
tables within documents

3. How to perform chunking when images or tables are interspersed within the text



For issue 
#1, I've found that various PDF loaders like LlamaParse and PDFPlumber can address this. For issue #2, I've learned that
 LlamaParse can convert tables to markdown format. (I'm also curious about other methods people use for this.)



Howeve
r, I'm completely stuck on issue #3. Despite days of searching, I haven't found any guides or clear solutions for chunki
ng text with embedded images or tables. I've been at a standstill for days, spending entire days trying to figure this o
ut.



Could you please tell me how experts typically solve issue #3? I'm desperate for any insights or guidance on this
 matter. Your help would be immensely appreciated!
```
---

     
 
all -  [ Can SmythOS RAG handle enterprise level RAG systems?
 ](https://www.reddit.com/r/LangChain/comments/1eyy9h2/can_smythos_rag_handle_enterprise_level_rag/) , 2024-08-24-0911
```
I have read a good number of posts on this sub of inquiries and discussion into the right approach when it comes to RAG.
 The sentiment around it, as far as I can tell, is that it might not be the hero that it was hoisted to be from the begi
nning and to get the best results from it, you gotta put in the work, a lot of work.

I found out that SmythOS has a num
ber of data related components,

* Data Lookup
* Data Source Indexer
* Data Source Cleaner

The platform is no code but 
I would assume that under the hood these data components use RAG for storage, indexing, search etc

I created a simple w
orkflow that I had to add a couple of documents, around 10, and with the data components and an LLM, I tried retrieving 
information from the docs through chat and it worked fairly well. 

I know 10 documents aren’t much and I know I might n
ot be knowledgeable enough about RAG to know what to test for and that’s why I’m asking here for your opinions, what’s y
our take on how SmythOS handles data retrieval, search and indexing? Would it be sufficient for an enterprise level RAG 
solution?
```
---

     
 
all -  [ JSONLoader, search for key but return content ](https://www.reddit.com/r/LangChain/comments/1eyxj6n/jsonloader_search_for_key_but_return_content/) , 2024-08-24-0911
```
`llm = ChatOpenAI(model='gpt-4o')`

`loader = JSONLoader(`

`file_path='./extracted_data.jsonl',`

`jq_schema='.title',`


`text_content=False,`

`json_lines=True,`

`)`

I have a JSON format like this:

{

'title': 'X Title',

'content': 'X
 content'

}

Is it possible to search based on the title but return the content to the LLM?


```
---

     
 
all -  [ Where to start langchain and generative ai as a begineer? ](https://www.reddit.com/r/generativeAI/comments/1eype0m/where_to_start_langchain_and_generative_ai_as_a/) , 2024-08-24-0911
```
Do i really need the knowledge of machine learning and deep learning to learn this?
```
---

     
 
all -  [ Token streaming + structured response parsing ](https://www.reddit.com/r/LangChain/comments/1eynruh/token_streaming_structured_response_parsing/) , 2024-08-24-0911
```
I'm trying to build a POC of re-work of my AI chat app that I've built using LangChain and gpt-4 using full streaming ca
pabilities. My goal is to make visual/audio latency as minimal as possible. What I want is to use *astream\_events* per 
LangChain docs to get token streaming. My system prompt has some places where I request structured responses along with 
text. Here is an example:

    Here is a form you need to fill-in: { 'content':'user-form', 'form-id':'form-1a2b3c4d'}


My understanding that *JsonOutputParser* supports streaming I can attach it to my LCEL, but it doesn't work this way - I
 still receive raw tokens in *astream\_events*, but I can get the parsed result when streaming is over (not what I need)
.

Is there any way to parse a stream of tokens and extract structured content out of it? I believe there are some ways,
 but wasn't able to google them, unfortunately. What do you use for that?
```
---

     
 
all -  [ Question about PDF Parsing. Please Help Me! ](https://www.reddit.com/r/LangChain/comments/1eylm73/question_about_pdf_parsing_please_help_me/) , 2024-08-24-0911
```
Hello. Everyone. I recently started studying RAG. So I need your advice.



When working with PDF documents, we often ne
ed to load them using a PDFLoader and then divide the content into chunks, ideally grouping related content together. Ho
wever, PDF documents frequently have a highly unstructured format, with images interspersed within the text. Current PDF
Loaders like Marker, while advanced, cannot automatically concatenate text sections and separately identify images in th
e same way a human would perceive the document structure. This limitation presents a significant challenge.

Given these
 constraints, how should developers approach the task of effectively processing such complex PDF structures? What strate
gies can be employed to:



Accurately identify and group related textual content?

Properly handle embedded images and 
other non-textual elements?

Maintain the logical flow and context of the document during the chunking process?



Can y
ou provide some best practices or methodologies that address these challenges in PDF processing and chunking, particular
ly for documents with mixed content types and complex layouts?

https://preview.redd.it/114apizad8kd1.png?width=1316&for
mat=png&auto=webp&s=5e60ea3c32f46ad3b374f6b650f7250472c4033d

  

```
---

     
 
all -  [ Fine-tuning in another language ](https://www.reddit.com/r/LangChain/comments/1eylgcz/finetuning_in_another_language/) , 2024-08-24-0911
```
I need to 'feed' a model custom data, but it is in Bulgarian. Is there a way to do this?

```
---

     
 
all -  [ How can I create my own version of NotebookLM? How can I evaluate it against a csv of questions and  ](https://www.reddit.com/r/LocalLLaMA/comments/1eyla7p/how_can_i_create_my_own_version_of_notebooklm_how/) , 2024-08-24-0911
```
I tried notebookLM today, and was very underwhelmed.

  
I want to make my own version of it, or use an open source vers
ion that someone else has made. As far as I can see, notebookLM is just a RAG application using Google's models. I've re
ad about how LangChain, LlamaIndex, and Haystack are used to create RAG applications, but i'm getting a bit overwhelmed 
reading about them on the internet. So many differing opinions. I've only used MilvusDB for my vector database before, a
nd the quickstart guide they gave used LlamaIndex and OpenAI. I need to learn Langchain and Haystack.

  
For the LLMs a
ctually answering queries, i'm hoping to evaluate Claude, Gemini, GPT, and LLaMA against eachother.

  
I have a created
 a csv file of 20 questions and answers so far, and plan to get more. I wonder if this will be helpful in evaluating the
 rag applications against eachother.

  
I looked at [RagBuilder](https://www.reddit.com/r/LocalLLaMA/comments/1eujz24/r
agbuilder_now_supports_azureopenai_googlevertex/) but did not really like it. If I could speak to the dev maybe I could 
figure it out, but I don't think I need to use something so complicated.

  
How do I start on this project?
```
---

     
 
all -  [ What’s your preferred approach to RAG search? ](https://www.reddit.com/r/LangChain/comments/1eyl7c3/whats_your_preferred_approach_to_rag_search/) , 2024-08-24-0911
```
I wrote the same post in the r/RAG community, but I haven't got a response there yet because that community is still qui
te small. So I'll ask here. I'm new to Reddit, and this is my very first post, so please be gentle!

I've been working o
n building RAG systems and have noticed that search tends to be the current bottleneck, particularly in specialized doma
ins. Existing methods often struggle to accurately select the most relevant context chunks.

How do you handle this? Wha
t’s your preferred approach to RAG search — vector-based, full-text, or hybrid? Do you rely on custom formulas, reranker
s, query expansion/reformulation, or specialized dictionaries?

Have you worked with knowledge bases containing hundreds
 of thousands or even millions of documents? How has that experience shaped your approach? Thanks to everyone who respon
ds! This is important to me!
```
---

     
 
all -  [ 2025 graduate, doubting whether i will get a good job or not ](https://www.reddit.com/r/developersIndia/comments/1eyl15n/2025_graduate_doubting_whether_i_will_get_a_good/) , 2024-08-24-0911
```
https://preview.redd.it/6qs6fc5y88kd1.png?width=759&format=png&auto=webp&s=2289ba1699333a088181ac6c364a9f18654f01a6


```
---

     
 
all -  [ High-Precision RAG for Table Heavy Documents… (Using LangChain, Unstructured.io, & KDB.AI) ](https://www.reddit.com/r/kdbai/comments/1eykuqz/highprecision_rag_for_table_heavy_documents_using/) , 2024-08-24-0911
```
One aspect of RAG that’s been bugging me is the decline in accuracy when retrieving specific values from embedded tables
 within a document. It’s even worse when the document is packed with multiple similar complex tables (especially nested 
columns), like in an earnings report. So I set out on a mission to improve RAG on table heavy documents using [LangChain
](https://www.linkedin.com/company/langchain/), [unstructured.io](https://www.linkedin.com/company/unstructuredio/), and
 [KDB.AI](https://www.linkedin.com/company/kdb-ai/), and wrote this article to tell the tale: [https://lnkd.in/gBDNYx68]
(https://lnkd.in/gBDNYx68)  
Key highlights:  
✔ Precise table extraction techniques  
✔ Contextual enrichment using LLM
s  
✔ Clever format standardization tricks  
✔ A unified embedding approach for optimal retrieval  
Enjoy the article an
d share your thoughts in the comments below!
```
---

     
 
all -  [ Support for open source library flow-prompt for Gemini-Claude-OpenAI ](https://www.reddit.com/r/ClaudeAI/comments/1eykriw/support_for_open_source_library_flowprompt_for/) , 2024-08-24-0911
```
Hey, we're (3 developers) developing library flow-prompt based on our experience as Director of AI and other AI startups
. The problem we faced:

* langchain is good for prototyping; hard to customize with constant exceptions;
* distribute t
he load, avoid rate limits in production. Ideally to distribute the laod across multiple Azure models,  Claude, and prob
ably to use OpenAI as fallback strategy, because there are no free credits on OpenAi models;
* pro-prompting, you need a
 smarter way to define what should go in prompt and in what order, and budget automatically is calculated;
* model agnos
tic, btw Gemini, OpenAI, Claude. Despite they need to have their own rules, with format of adding in the prompt;

So we 
all included in that library, and

We added the first CI/CD pipeline there. Which defines statements from the human writ
ten response for specific test context. And we compare statements from human response and real LLM response.

We're usin
g that library in the some companies. I'm sure more can benefit. And we would be blissed if you will provide feedback an
d share what you want from next prompt library you wanna try, and happy to see any contributions.  
[https://www.flow-pr
ompt.com/](https://www.flow-prompt.com/)

discord:  
[https://discord.gg/rrgpnspAQa](https://discord.gg/rrgpnspAQa)
```
---

     
 
all -  [ Tips for Reducing LangChain Package Size in AWS Lambda? ](https://www.reddit.com/r/LangChain/comments/1eykko9/tips_for_reducing_langchain_package_size_in_aws/) , 2024-08-24-0911
```
Hi everyone,

I'm currently working on a project where we're using LangChain in an AWS Lambda function. However, we're f
acing some challenges with the 'langchain' package size due to the dependencies it pulls in, specifically 'numpy' and 's
qlalchemy,' which are significantly bloating our Lambda layer.

At this stage, we only need 'langchain' for the legacy `
AgentExecutor`, and we're trying to keep our deployment as lightweight as possible. Has anyone encountered a similar iss
ue? If so, do you have any tips or workarounds for minimizing the package size or selectively excluding certain dependen
cies?

Any advice would be greatly appreciated!

[](https://www.reddit.com/user/hwchase17/) 
```
---

     
 
all -  [ How to make llm more robust in looking and filtering data for the responses. ](https://www.reddit.com/r/LangChain/comments/1eyjq2f/how_to_make_llm_more_robust_in_looking_and/) , 2024-08-24-0911
```
I was working on a agent where the task was to just using prompt and function calling, I need to make a chabot. 

Bot wo
rks fine with openai gpt4o-mini until I increased one more function. After that I noticed that llm is not using the func
tions properly. So I changed llm to gpt-4o . It start calling appropriately but still lacks in filtering data. It doesn'
t give right answer even the return datatype from the function is structured.

What methods one can suggest to improve t
his thing ?

I have tried improve the prompting , but it doesn't work in enhancing the data looking part.

I added a fil
ter function also to get the accuracy but it doesn't work. The parameter length is too long.
```
---

     
 
all -  [ My Resume Needs Debugging! Help Fix This Mess Before It Crashes My Job Hunt! ](https://i.redd.it/a87ugq2vp7kd1.jpeg) , 2024-08-24-0911
```
Hey folks,I’m looking for some feedback on my resume. I want to make sure it's polished and error-free before sending it
 out. 

Thanks in advance for your help!
```
---

     
 
all -  [ Gemini 1.5 Pro Exp not available  ](https://www.reddit.com/r/LangChain/comments/1eyglwx/gemini_15_pro_exp_not_available/) , 2024-08-24-0911
```
Hi!

I’m trying to use gemini-1.5-pro-exp-0801 with Langchain but get a 404 saying the model is not available. I am able
 to use it with GenAI SDK though. Any thoughts? Has anybody else faced this issue?
```
---

     
 
all -  [ [0 YoE, Student, SDE, India] ](https://www.reddit.com/r/resumes/comments/1eygc8j/0_yoe_student_sde_india/) , 2024-08-24-0911
```
Hey everyone, I am going to apply for SWE FTE roles this year, I need a review on my CV, I had my Internship last summer
 at a firm in Data Analytics role( it is at a Big4 but I admit that I haven't been allotted even a decent amount of work
), and I attached my projects and skills too, I have few academic achievements and extra curricular section in my full r
esume, which I don't want to reveal, please give your review and suggestions on these sections, how do I improvise it, I
 feel this doesn't look good, any suggestions would be appreciated, thanks a lot in advance.

https://preview.redd.it/ss
lg8n0157kd1.png?width=1350&format=png&auto=webp&s=41e3b6f2d1f8bfba46326dc1931bde28c7b73199


```
---

     
 
all -  [ So many people were talking about RAG so I created r/Rag ](https://www.reddit.com/r/LangChain/comments/1eyf4vw/so_many_people_were_talking_about_rag_so_i/) , 2024-08-24-0911
```
In the fast-moving world of AI, I see posts about RAG multiple times every hour in hundreds of different subreddits. It 
definitely is a technology that won't go away soon. For those who don't know what RAG is , it's basically combining LLMs
 with external knowledge sources. This approach lets AI not just generate coherent responses but also tap into a deep we
ll of information, pushing the boundaries of what machines can do.

But you know what? As amazing as RAG is, I noticed s
omething missing. Despite all the buzz and potential, there isn’t really a go-to place for those of us who are excited a
bout RAG, eager to dive into its possibilities, share ideas, and collaborate on cool projects. I wanted to create a spac
e where we can come together - a hub for innovation, discussion, and support.
```
---

     
 
all -  [ Deploying Model to Fireworks ](https://www.reddit.com/r/LangChain/comments/1eyeheu/deploying_model_to_fireworks/) , 2024-08-24-0911
```
I am building on LangGraph and I want to used finetuned Llama 3.1 8b

So I finetuned lama-3.1-8b-instruct-bnb-4bit with 
unsloth and have necessary files in a folder, but how to deploy it to [fireworks.ai](http://fireworks.ai/) is confusing,
 tried to follow the docs  
  
I have windows, but I have ubuntu installed in which I installed firecracker



Really wo
uld appreciate guidance:)
```
---

     
 
all -  [ Is My Approach Considered RAG, and How Can I Improve It? ](https://www.reddit.com/r/LangChain/comments/1eye7bj/is_my_approach_considered_rag_and_how_can_i/) , 2024-08-24-0911
```
Hi everyone,

I'm working with LLMs (like GPT-4) and I want to understand if my current approach is considered a Retriev
al-Augmented Generation (RAG) method and how I might improve it.

Here’s what I’m doing: I’ve set up various tools with 
descriptions that the LLM can use. For example, if a user requests information about 'X,' the LLM calls a specific tool 
that returns data related to 'X.' The LLM then processes this data as part of its response.

For instance, I might have 
a single tool that accepts an input of resource_type. Depending on this input, the LLM fetches different data to work wi
th.

Is this method in line with the RAG framework? If so, are there any best practices or improvements I could implemen
t to enhance the effectiveness of this setup?

Thanks for your insights!
```
---

     
 
all -  [ How to Prevent LLM from Overwriting Parameters Passed to a LangChain Tool in a Custom Agent? ](https://www.reddit.com/r/LangChain/comments/1eyd29z/how_to_prevent_llm_from_overwriting_parameters/) , 2024-08-24-0911
```
I'm working on a custom LangChain agent that uses a tool to make API calls based on parameters passed in the code. Howev
er, I'm encountering an issue where the LLM is generating its own parameters instead of using the ones I pass. Here’s th
e relevant code:

    import requests
    from langchain_core.pydantic_v1 import BaseModel, Field
    from typing import
 Optional
    from langchain.agents import Tool, AgentExecutor, create_tool_calling_agent
    from langchain.chat_models
 import ChatOpenAI
    from langchain_core.tools import StructuredTool
    
    def get_swagger_file(api_name):
        
api_list = requests.get('https://api.apis.guru/v2/list.json').json()
        preferred_version = api_list[api_name]['pre
ferred']
        swagger_url = api_list[api_name]['versions'][preferred_version]['swaggerUrl']
        return requests.g
et(swagger_url).json()
    
    class APIToolInput(BaseModel):
        api_name: str
        method: str
        endpoin
t: str
        params: Optional[dict] = Field(default=None)
        data: Optional[dict] = Field(default=None)
    
    
def call_api(api_name: str, method: str, endpoint, params: dict = None, data: dict = None) -> str:
        swagger_spec 
= get_swagger_file(api_name)
        paths = swagger_spec.get('paths', {})
        if endpoint not in paths:
           
 return {'error': 'Path not found'}
        
        if method not in paths[endpoint]:
            return {'error': 'Met
hod not found'}
    
        server = swagger_spec['servers'][0]['url']
        url = f'{server}{endpoint}'
    
       
 # Make the API call
        response = requests.request(method, url, params=params)
        json_response = response.js
on()
        
        return json_response
    
    def api_tool(input_data: APIToolInput) -> str:
        api_name = in
put_data.api_name
        method = input_data.method
        endpoint = input_data.endpoint
        params = input_data.
params
        data = input_data.data
        
        # Call the API with the parameters
        return call_api(api_na
me, method, endpoint, params, data)
    
    tool = StructuredTool(
        name='APITool',
        func=api_tool,
     
   description='Calls the specified API endpoint with the given method and parameters.',
        args_schema=APIToolInpu
t
    )
    
    llm = ChatOpenAI(temperature=0.7, model_name='gpt-4')
    
    from langchain_core.prompts import ChatP
romptTemplate
    
    prompt = ChatPromptTemplate.from_messages(
        [
            ('system', 'You are a helpful as
sistant'),
            ('human', '{input}'),
            ('placeholder', '{agent_scratchpad}'),
        ]
    )
    
   
 agent = create_tool_calling_agent(
        tools=[tool],
        llm=llm,
        prompt=prompt
    )
    
    agent_ex
ecutor = AgentExecutor(agent=agent, tools=[tool], verbose=True)
    
    api_name = 'trakt.tv'
    method = 'get'
    en
dpoint = '/movies/anticipated'
    
    response = agent_executor.invoke({
        'input': 'What are the most anticipat
ed movies?',
        'api_name': api_name,
        'method': method,
        'endpoint': endpoint
    })

The problem is
 that the tool is not using the parameters I provide, but instead, the LLM seems to be generating them. Here’s the outpu
t:

    Entering new AgentExecutor chain...
    
    Invoking: APITool with {'api_name': 'movieDatabase', 'method': 'GET
', 'endpoint': '/movies/anticipated'}

As you can see, the `api_name` has changed to `movieDatabase`, even though I pass
ed `trakt.tv`. I want the tool to use the parameters I define in the code, not those generated by the LLM.

There a way 
to ensure that the parameters I pass are respected?

Any advice or suggestions would be greatly appreciated.
```
---

     
 
MachineLearning -  [ [P] using GPT4o with langchain/chroma for sports analysis  ](https://www.reddit.com/r/MachineLearning/comments/1enuzlp/p_using_gpt4o_with_langchainchroma_for_sports/) , 2024-08-24-0911
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
 ](https://www.reddit.com/r/MachineLearning/comments/1eki1fv/r_d_langchain_evaluation_with_beyondllm/) , 2024-08-24-0911
```
Hey everyone! Just came across a new feature of Beyond LLM that can evaluate Langchain RAG pipelines! It provides contex
t relevancy, answer relevancy, and groundedness. Check out the code snippet I’m sharing—perfect for testing your RAG pip
elines! For more info, be sure to check it out on GitHub [here](https://github.com/aiplanethub/beyondllm/blob/main/cookb
ook/evaluate_langchain_rag_pipeline_beyondllm.ipynb).

https://preview.redd.it/172m1y3dvsgd1.png?width=3972&format=png&a
uto=webp&s=63d5b0f41f0e46a58e7a2d5fb0d2bbc4384b3b1d


```
---

     
 
deeplearning -  [ Creating a project on NLP ](https://www.reddit.com/r/deeplearning/comments/1ey2e85/creating_a_project_on_nlp/) , 2024-08-24-0911
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

     
 
deeplearning -  [ How To Build Your Retrieval Augmented Generation (RAG) Using Open-source Tools: LangChain, LLAMA 3,  ](https://www.reddit.com/r/deeplearning/comments/1emdotx/how_to_build_your_retrieval_augmented_generation/) , 2024-08-24-0911
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

     
 
deeplearning -  [ Need help with creating CLI for 'non-programmers' (LLMs) ](https://www.reddit.com/r/deeplearning/comments/1elrfgm/need_help_with_creating_cli_for_nonprogrammers/) , 2024-08-24-0911
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

     
