 
all -  [ LangChain in Under 5 Min | A Quick Guide for Beginners ](https://youtu.be/bV5wI0DB7YM?si=jYph0twu4ZJPKYKo) , 2024-08-25-0912
```

```
---

     
 
all -  [ Problems Getting Hermes 3 405B's API Key ](https://www.reddit.com/r/LangChain/comments/1f0arfb/problems_getting_hermes_3_405bs_api_key/) , 2024-08-25-0912
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

     
 
all -  [ 2025 graduate, not much luck in internships or placements ](https://i.redd.it/unfpislgumkd1.png) , 2024-08-25-0912
```
is there anything i should update in my resume? i did modify it according to some points on resumeworded
```
---

     
 
all -  [ Suggestions for implementing RAG with cobra ](https://www.reddit.com/r/golang/comments/1f06pnv/suggestions_for_implementing_rag_with_cobra/) , 2024-08-25-0912
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

     
 
all -  [ Real Estate Dataset Required  ](https://www.reddit.com/r/LangChain/comments/1f04t36/real_estate_dataset_required/) , 2024-08-25-0912
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

     
 
all -  [ How to integrate a personalised prompt with LangChain and a vector database like Pinecone for a chat ](https://www.reddit.com/r/LangChain/comments/1f02d8b/how_to_integrate_a_personalised_prompt_with/) , 2024-08-25-0912
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

     
 
all -  [ How do you visualize agentic communications ](https://www.reddit.com/r/LangChain/comments/1ezzcdj/how_do_you_visualize_agentic_communications/) , 2024-08-25-0912
```
I am using Langgraph to do agent setup with several agents. What is the best way to visualize the steps done by differen
t agents, 
```
---

     
 
all -  [ Unable to Implement RAG For CSV Files ](https://www.reddit.com/r/LangChain/comments/1ezx03c/unable_to_implement_rag_for_csv_files/) , 2024-08-25-0912
```
I’m working on implementing a RAG workflow for CSV files that contain Arabic text, which requires UTF-8 encoding. The wo
rkflow includes:



1. Loading CSV Files (Partition\_CSV)

2. Chunking

3. Defining Embeddings

4. Converting to Vector 
Embeddings, in Vector DB (Postgres-PG Vector)

5. Defining Prompt

6.  then defining LLM

I tested this successfully wit
h an Small English CSV file, but encountered issues when loading the Arabic CSV file. The problem seems to be with the \
`Partition\_CSV\` function, which lacks an option for encoding. Without encoding, Arabic fields convert to question mark
s, leading to LLM not recognizing the content and responding with 'I don't know.'

I attempted to use \`CSVLoader\`, whi
ch offers an encoding option, but it still doesn’t handle the Arabic text correctly. As a result output remains same, an
swer to any question I don't Know.

Is there any  alternatives to resolve this issue.   
Thanks.
```
---

     
 
all -  [ How to work with API Data  ](https://www.reddit.com/r/Rag/comments/1ezpkyy/how_to_work_with_api_data/) , 2024-08-25-0912
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

     
 
all -  [ How to pass multiple inputs during invoke  to a MessageGraph(langraph) ](https://www.reddit.com/r/LangChain/comments/1ezn36b/how_to_pass_multiple_inputs_during_invoke_to_a/) , 2024-08-25-0912
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

     
 
all -  [ [1 YoE] DS Student Searching for over a Year with over 500 Applications only 3 Interviews With No Of ](https://www.reddit.com/r/EngineeringResumes/comments/1ezmwfb/1_yoe_ds_student_searching_for_over_a_year_with/) , 2024-08-25-0912
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

     
 
all -  [ How can we ensure that only humans are interacting with the chatbot?  ](https://www.reddit.com/r/LangChain/comments/1ezm79b/how_can_we_ensure_that_only_humans_are/) , 2024-08-25-0912
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

     
 
all -  [ Looking for researchers and members of AI development teams to take part in an IRB approved user stu ](https://www.reddit.com/r/LangChain/comments/1ezm4pb/looking_for_researchers_and_members_of_ai/) , 2024-08-25-0912
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

     
 
all -  [ Building Reliable GenAI Agents using Knowledge Graphs ](https://www.reddit.com/r/LangChain/comments/1ezhaji/building_reliable_genai_agents_using_knowledge/) , 2024-08-25-0912
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

     
 
all -  [ LLMs to query databases from natural language ](https://www.reddit.com/r/LangChain/comments/1ezg5xd/llms_to_query_databases_from_natural_language/) , 2024-08-25-0912
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

     
 
all -  [ Multi-Agent Supervision (OpenAI Assistants: Directly) ](https://www.reddit.com/r/LangChain/comments/1ezfuzz/multiagent_supervision_openai_assistants_directly/) , 2024-08-25-0912
```
I've been trying to use OpenAI Assistants as agents in langchain but I'm having trouble connecting to a specific existin
g Assistant, with a pre-existing assistant ID. Do we know if there is a solution to make this setup work? Thank you in a
dvance.
```
---

     
 
all -  [ Has anyone used RAPTOR for RAG? ](https://www.reddit.com/r/LangChain/comments/1ezdd5t/has_anyone_used_raptor_for_rag/) , 2024-08-25-0912
```
The official implementation on Github: [https://github.com/parthsarthi03/raptor](https://github.com/parthsarthi03/raptor
) is not complete, and I am not really sure how to work around with multiple documents (I have over 100+). 

If anyone h
as a full implementation of RAPTOR that uses local or open source hugging face models please do share it.
```
---

     
 
all -  [ Help me learn Python , Langchain , RAG the correct way  ](https://www.reddit.com/r/Rag/comments/1ezciy1/help_me_learn_python_langchain_rag_the_correct_way/) , 2024-08-25-0912
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

     
 
all -  [ How to improve the accuracy and working of sql agent?  ](https://www.reddit.com/r/LangChain/comments/1eza5m4/how_to_improve_the_accuracy_and_working_of_sql/) , 2024-08-25-0912
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

     
 
all -  [ Long, expensive, awesome ](https://www.reddit.com/r/LangChain/comments/1ez9onz/long_expensive_awesome/) , 2024-08-25-0912
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

     
 
all -  [ Seeking guidance to learn LLMs ](https://www.reddit.com/r/LangChain/comments/1ez7e7h/seeking_guidance_to_learn_llms/) , 2024-08-25-0912
```
Hi everyone. I am new to field of LLMs. I am seeking some guidance on how and where to start from. I hear a lot of termi
nology like RAG, agents etc but have no idea of where to start. Kindly guide me with some starting points/repos.
```
---

     
 
all -  [ Is there currently a way to smoothly handle tool calling while using a vLLM?  ](https://www.reddit.com/r/LangChain/comments/1ez7cb6/is_there_currently_a_way_to_smoothly_handle_tool/) , 2024-08-25-0912
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

     
 
all -  [ Agency - Reliable, safe, & compliant AI Agents ](https://www.reddit.com/r/u_Wesubmit/comments/1ez5f6a/agency_reliable_safe_compliant_ai_agents/) , 2024-08-25-0912
```
Agency helps enterprises build, evaluate, and monitor AI agents. From the team at [AgentOps.ai](http://agentops.ai/).

[
Agen.cy](http://agen.cy/) (Agency AI) develops cutting edge AI agents using CrewAI, AutoGen, CamelAI, LLamaIndex, Langch
ain, Cohere, MultiOn + many more. 
```
---

     
 
all -  [ How do I get a custom attributes preserved in the HumanMessage object passed to the BaseChatMessageH ](https://www.reddit.com/r/LangChain/comments/1ez24hc/how_do_i_get_a_custom_attributes_preserved_in_the/) , 2024-08-25-0912
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

     
 
all -  [ How can I parse Unstructured document? ](https://www.reddit.com/r/LangChain/comments/1eyyv3d/how_can_i_parse_unstructured_document/) , 2024-08-25-0912
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
 ](https://www.reddit.com/r/LangChain/comments/1eyy9h2/can_smythos_rag_handle_enterprise_level_rag/) , 2024-08-25-0912
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

     
 
all -  [ JSONLoader, search for key but return content ](https://www.reddit.com/r/LangChain/comments/1eyxj6n/jsonloader_search_for_key_but_return_content/) , 2024-08-25-0912
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

     
 
all -  [ Where to start langchain and generative ai as a begineer? ](https://www.reddit.com/r/generativeAI/comments/1eype0m/where_to_start_langchain_and_generative_ai_as_a/) , 2024-08-25-0912
```
Do i really need the knowledge of machine learning and deep learning to learn this?
```
---

     
 
all -  [ Token streaming + structured response parsing ](https://www.reddit.com/r/LangChain/comments/1eynruh/token_streaming_structured_response_parsing/) , 2024-08-25-0912
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

     
 
all -  [ Question about PDF Parsing. Please Help Me! ](https://www.reddit.com/r/LangChain/comments/1eylm73/question_about_pdf_parsing_please_help_me/) , 2024-08-25-0912
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

     
 
all -  [ Fine-tuning in another language ](https://www.reddit.com/r/LangChain/comments/1eylgcz/finetuning_in_another_language/) , 2024-08-25-0912
```
I need to 'feed' a model custom data, but it is in Bulgarian. Is there a way to do this?

```
---

     
 
all -  [ How can I create my own version of NotebookLM? How can I evaluate it against a csv of questions and  ](https://www.reddit.com/r/LocalLLaMA/comments/1eyla7p/how_can_i_create_my_own_version_of_notebooklm_how/) , 2024-08-25-0912
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

     
 
MachineLearning -  [ [P] using GPT4o with langchain/chroma for sports analysis  ](https://www.reddit.com/r/MachineLearning/comments/1enuzlp/p_using_gpt4o_with_langchainchroma_for_sports/) , 2024-08-25-0912
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
 ](https://www.reddit.com/r/MachineLearning/comments/1eki1fv/r_d_langchain_evaluation_with_beyondllm/) , 2024-08-25-0912
```
Hey everyone! Just came across a new feature of Beyond LLM that can evaluate Langchain RAG pipelines! It provides contex
t relevancy, answer relevancy, and groundedness. Check out the code snippet I’m sharing—perfect for testing your RAG pip
elines! For more info, be sure to check it out on GitHub [here](https://github.com/aiplanethub/beyondllm/blob/main/cookb
ook/evaluate_langchain_rag_pipeline_beyondllm.ipynb).

https://preview.redd.it/172m1y3dvsgd1.png?width=3972&format=png&a
uto=webp&s=63d5b0f41f0e46a58e7a2d5fb0d2bbc4384b3b1d


```
---

     
 
deeplearning -  [ Creating a project on NLP ](https://www.reddit.com/r/deeplearning/comments/1ey2e85/creating_a_project_on_nlp/) , 2024-08-25-0912
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

     
 
deeplearning -  [ How To Build Your Retrieval Augmented Generation (RAG) Using Open-source Tools: LangChain, LLAMA 3,  ](https://www.reddit.com/r/deeplearning/comments/1emdotx/how_to_build_your_retrieval_augmented_generation/) , 2024-08-25-0912
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

     
 
deeplearning -  [ Need help with creating CLI for 'non-programmers' (LLMs) ](https://www.reddit.com/r/deeplearning/comments/1elrfgm/need_help_with_creating_cli_for_nonprogrammers/) , 2024-08-25-0912
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

     
