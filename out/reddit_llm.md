 
all -  [ [0 YoE, Student, ML/AI/Software internship, Canada] ](https://i.redd.it/0g8hwhhnpnpd1.jpeg) , 2024-09-19-0912
```
Hello! l'm a second year CS student looking for an AI/ML or software dev internship for summer 2025. Looking for some fe
edback before I start applying.
```
---

     
 
all -  [ [Student] 0 YoE CS grad student looking for entry roles in Machine Learning/Data Science roles - loo ](https://www.reddit.com/r/EngineeringResumes/comments/1fk5ojt/student_0_yoe_cs_grad_student_looking_for_entry/) , 2024-09-19-0912
```
Hi all, I'm a CS grad looking to apply to entry-level Data Scientist or Machine Learning Engineer roles. I'm hoping to r
eceive some honest feedback so that I can make the necessary tweaks before I apply more. I have already applied to 100 j
obs over the past week and have been cold messaging employees on LinkedIn for referrals but received no response yet.

I
've tried to include projects that are business-focused and I have also incorporated metrics and keywords to showcase bu
siness impact. How else can I improve?

https://preview.redd.it/j53y8v3janpd1.png?width=4967&format=png&auto=webp&s=e446
63fb3d326e61bc06a5df53225b1731a3918f

  

```
---

     
 
all -  [ Emulate OpenAI API ](https://www.reddit.com/r/OpenWebUI/comments/1fk37bc/emulate_openai_api/) , 2024-09-19-0912
```
Is it possible?

I know Oobabooga does that. wonder if I can use langchain with OpenWebUI while using OpenAI api emulate
d on it.
```
---

     
 
all -  [ Build neo4j graph ](https://www.reddit.com/r/LangChain/comments/1fk2chx/build_neo4j_graph/) , 2024-09-19-0912
```
I want to build a neo4j graph from a batch of http requests.
I only want to have a relationship to know if a pair (reque
st, response) is connected with a other (request, response)
```
---

     
 
all -  [ The Agentic Patterns makes working auth agents so much better. ](https://www.reddit.com/r/AutoGenAI/comments/1fk0vnu/the_agentic_patterns_makes_working_auth_agents_so/) , 2024-09-19-0912
```
These Agentic Design Patterns helped me out a lot when building with AutoGen+Llama3!

I mostly use open source models (L
lama3 8B and Qwen1.5 32B Chat). Getting these open source models to work reliably has always been a challenge. That's wh
en my research led me to AutoGen and the concept of AI Agents.

Having used them for a while, there are some patterns wh
ich have been helping me out a lot. Wanted to share it with you guys,

# My Learnings

i. You solve the problem of indet
erminism with conversations and not via prompt engineering.

Prompt engineering is important. I'm not trying to dismiss 
it. But its hard to make the same prompt work for the different kinds of inputs your app needs to deal with.

A better a
pproach has been adopting the two agent pattern. Here, instead of taking an agent's response and forwarding it to the us
er (or the next agent) we let it talk to a companion agent first. We then let these agent talk with each other (1 to 3 t
urns depending on how complex the task was) to help 'align' the answer with the 'desired' answer.

Example: Lets say you
 are replacing a UI form with a chatbot. You may have an agent to handle the conversation with the user. But instead of 
it figuring out the JSON parameters to fill up the form, you can have a companion agent do that. The companion agent wou
ldn't really be following the entire conversation (just the deltas) and will keep a track of what fields are answered an
d what isn't. It can tell the chat agent what questions needs to be asked next.

This helps the chat agent focus on the 
'conversation' aspect (Dealing with prompt injection, politeness, preventing the chat from getting derailed) while the c
ompanion agent can take care of managing form data (JSON extraction, validation and so on).

Another example could be sp
litting a JSON formatter into 3 parts (An agent to spit out data in a semi structured format like markdown - Another one
 to convert that to JSON - The last one to validate the JSON). This is more of a sequential chat pattern but the last tw
o could and probably should be modelled as two-companion agents.

ii. LLMs are not awful judges. They are often good eno
ugh for things like RAG.

An extension of the two agent pattern is called 'Reflection.' Here we let the companion agent 
verify the primary agent's work and provide feedback for improvement.

Example: Let's say you got an agent that does RAG
. You can have the companion do a groundedness check to make sure that the text generation is in line with the retrieved
 chunks. If things are amiss, the companion can provide an additional prompt to the RAG agent to apply corrective measur
es and even mark certain chunks as irrelevant. You could also do a lot more checks like profanity check, relevance check
 (this can be hard) and so on. Not too bad if you ask me.

iii. Agents are just a function. They don't need to use LLMs.


I visualize agents as functions which take a conversational state (like an array of messages) as an input and return a
 message (or modified conversational state) as an output. Essentially they are just participants in a conversation.

Wha
t you do inside the function is upto you. Call an LLM, do RAG or whatever. But you could also just do basic clasificatio
n using a more traditional approach. But it doesn't need to be AI driven at all. If you know the previous agent will out
put JSON, you can have a simple JSON schema validator and call it a day. I think this is super powerful.

iv. Agents are
 composable.

Agents are meant to be composable. Like React's UI components.

So I end up using agents for simple prompt
 chaining solutions (which may be better done by raw dawging shit or using Langchain if you swing that way) as well. Thi
s lets me morph underperforming agents (or steps) with powerful patterns without having to rewire the entire chain. Pret
ty dope if you ask me.

## Conclusion

I hope I am able to communicate my learning wells. Do let me know if you have any
 questions or disagree with any of my points. I'm here to learn.

P.S. - Sharing a YouTube video I made on this topic wh
ere I dive a bit deeper into these examples! Would love for you to check that out as well. Feel free to roast me for my 
stupid jokes! Lol!

https://youtu.be/PKo761-MKM4
```
---

     
 
all -  [ What are you all building?  ](https://www.reddit.com/r/LangChain/comments/1fjzpej/what_are_you_all_building/) , 2024-09-19-0912
```
Just wanted to hear what you all are building and if you are using Langchain, how has your experience been so far. 
```
---

     
 
all -  [ Instructor output parser with LLM conversation memory chain ](https://www.reddit.com/r/LangChain/comments/1fjz4tg/instructor_output_parser_with_llm_conversation/) , 2024-09-19-0912
```
Can anyone help on how to integrate instructor parser with conversational chatbot, so it can collect the required field 
that I need from user queries ; ask relevant question if information is missing and stores and update the infos? And, la
stly shows the overallparsings result to user and ask for conformation?  Any guideline on how to implement it would be h
elpful! 
I am using openai model
```
---

     
 
all -  [ What do I build my agent's frontend on if i am using LangGraph? (Apart from streamlit) ](https://www.reddit.com/r/LangChain/comments/1fjyt7a/what_do_i_build_my_agents_frontend_on_if_i_am/) , 2024-09-19-0912
```
I am trying to make a production grade agent (planning on rolling it out as a web app) and I was wondering for my fronte
nd what should I use if I am using Langgraph to build my Ai agent? Should use React? or Next? or is there anything else 
more prod grade?  
Thanks.
```
---

     
 
all -  [ [0 YoE, Unemployed, Data Analyst/ Data Scientist, US] ](https://i.redd.it/nbn2qx8vplpd1.png) , 2024-09-19-0912
```

```
---

     
 
all -  [ Is there any good chat with Langchain documentation sites around? ](https://www.reddit.com/r/LangChain/comments/1fjx5b9/is_there_any_good_chat_with_langchain/) , 2024-09-19-0912
```
I used to use the chatgpt custom gpt features to chat with langchain documentation on an app I'm building, I feel like a
ll of them are slightly out of date as I'm prone to getting errors. 

The AI chat on the langchain site is really limite
d so I can't use that, so I'm wondering if there is anything else people are using for workloads


```
---

     
 
all -  [ These Agentic Design Patterns helped me out a lot when building with AutoGen+Llama3! ](https://www.reddit.com/r/LocalLLaMA/comments/1fjwtv2/these_agentic_design_patterns_helped_me_out_a_lot/) , 2024-09-19-0912
```
I mostly use open source models (Llama3 8B and Qwen1.5 32B Chat). Getting these open source models to work reliably has 
always been a challenge. That's when my research led me to AutoGen and the concept of AI Agents.

Having used them for a
 while, there are some patterns which have been helping me out a lot. Wanted to share it with you guys,

# My Learnings


i. You solve the problem of indeterminism with conversations and not via prompt engineering.

Prompt engineering is imp
ortant. I'm not trying to dismiss it. But its hard to make the same prompt work for the different kinds of inputs your a
pp needs to deal with.

A better approach has been adopting the two agent pattern. Here, instead of taking an agent's re
sponse and forwarding it to the user (or the next agent) we let it talk to a companion agent first. We then let these ag
ent talk with each other (1 to 3 turns depending on how complex the task was) to help 'align' the answer with the 'desir
ed' answer.

Example: Lets say you are replacing a UI form with a chatbot. You may have an agent to handle the conversat
ion with the user. But instead of it figuring out the JSON parameters to fill up the form, you can have a companion agen
t do that. The companion agent wouldn't really be following the entire conversation (just the deltas) and will keep a tr
ack of what fields are answered and what isn't. It can tell the chat agent what questions needs to be asked next.

This 
helps the chat agent focus on the 'conversation' aspect (Dealing with prompt injection, politeness, preventing the chat 
from getting derailed) while the companion agent can take care of managing form data (JSON extraction, validation and so
 on).

Another example could be splitting a JSON formatter into 3 parts (An agent to spit out data in a semi structured 
format like markdown - Another one to convert that to JSON - The last one to validate the JSON). This is more of a seque
ntial chat pattern but the last two could and probably should be modelled as two-companion agents.

ii. LLMs are not awf
ul judges. They are often good enough for things like RAG.

An extension of the two agent pattern is called 'Reflection.
' Here we let the companion agent verify the primary agent's work and provide feedback for improvement.

Example: Let's 
say you got an agent that does RAG. You can have the companion do a groundedness check to make sure that the text genera
tion is in line with the retrieved chunks. If things are amiss, the companion can provide an additional prompt to the RA
G agent to apply corrective measures and even mark certain chunks as irrelevant. You could also do a lot more checks lik
e profanity check, relevance check (this can be hard) and so on. Not too bad if you ask me.

iii. Agents are just a func
tion. They don't need to use LLMs.

I visualize agents as functions which take a conversational state (like an array of 
messages) as an input and return a message (or modified conversational state) as an output. Essentially they are just pa
rticipants in a conversation.

What you do inside the function is upto you. Call an LLM, do RAG or whatever. But you cou
ld also just do basic clasification using a more traditional approach. But it doesn't need to be AI driven at all. If yo
u know the previous agent will output JSON, you can have a simple JSON schema validator and call it a day. I think this 
is super powerful.

iv. Agents are composable.

Agents are meant to be composable. Like React's UI components.

So I end
 up using agents for simple prompt chaining solutions (which may be better done by raw dawging shit or using Langchain i
f you swing that way) as well. This lets me morph underperforming agents (or steps) with powerful patterns without havin
g to rewire the entire chain. Pretty dope if you ask me.

## Conclusion

I hope I am able to communicate my learning wel
ls. Do let me know if you have any questions or disagree with any of my points. I'm here to learn.

P.S. - Sharing a You
Tube video I made on this topic where I dive a bit deeper into these examples! Would love for you to check that out as w
ell. Feel free to roast me for my stupid jokes! Lol!
```
---

     
 
all -  [ Struggling to get interviews for ML engineer roles please let me know what the issue is with my resu ](https://www.reddit.com/r/Resume/comments/1fjvq7l/struggling_to_get_interviews_for_ml_engineer/) , 2024-09-19-0912
```
https://preview.redd.it/cjj6vh607lpd1.png?width=5100&format=png&auto=webp&s=8d9f2cc771a8f2a333cca4e70aeca960b617d1bf


```
---

     
 
all -  [ How would you marketing AI Agents Market Landscap Map ](https://www.reddit.com/r/marketing/comments/1fjut27/how_would_you_marketing_ai_agents_market_landscap/) , 2024-09-19-0912
```
Here is where imagination can go wild )) What kind of creazy marketing campaign might be done for interactive AI Agents 
Market Landscape map?

[Source AI Agents Directory](https://preview.redd.it/o14mbjx50lpd1.png?width=1319&format=png&auto
=webp&s=f92446c0f0c52d302b637312ffce2df1296dba64)
```
---

     
 
all -  [ Chat History vs Memory: what's the difference? ](https://www.reddit.com/r/LangChain/comments/1fju4sp/chat_history_vs_memory_whats_the_difference/) , 2024-09-19-0912
```
I'm wondering what's the difference between:

langchain.memory
langchain.core.memory
langchain.core.chat_history

What i
s the use case for each? Are any of those recommended over the others? Are any of those deprecated? Which integrates wit
h LCEL best?
```
---

     
 
all -  [ Self hosted personal assistant with function calling ](https://www.reddit.com/r/LocalLLaMA/comments/1fjtonw/self_hosted_personal_assistant_with_function/) , 2024-09-19-0912
```
Disclaimer: I'm software developer and I'm very bad at prompt engineering. I was trying to research this but found only 
infinite enterprise-first tools with 'book a demo' buttons on their websites without proper explanation of the product 


I want to make a personal chatbot with rag on personal notes and some function calling like to tell me the weather, use
 a calculator or make an event in the calendar, maybe give me a product reviews summary, etc. I have a feeling I'm not t
he first one to come up with this, so I guess there should be some chatbot framework with plugin system for these tools.


I tried openwebui but its rag just cuts first ~1000 tokens of the documents and it's function calling just never invok
ed (yes I enabled the tool I used). I tried making my own rag with vectorizing prompt and throwing results in a block wr
apped in <context><context />, but it never uses the context and prefers to hallucinate (prompt asked to use only inform
ation from the context, I even added 'don't be cringe' in the end as someone here said it reduces hallucinations). Llama
3 function calling works good enough but it always invokes a function instead of answering questions

If there is no cha
tbot application I dream about I would like to hear recommendations on how should I implement this and what are the best
 practices on implementing these types of bots. I have a feeling I would need some llm pipeline here with different mode
ls and prompts, is langchain good for this or I didn't understand what is it?

Thanks in advance!
```
---

     
 
all -  [ Best vectorstore for production in a RAG system. ](https://www.reddit.com/r/LangChain/comments/1fjoh9r/best_vectorstore_for_production_in_a_rag_system/) , 2024-09-19-0912
```
Hi, I am looking for a vectorstore for production for a RAG system. I created a POC with FAISS in AWS where each user ha
s its own vectorstore and these indexes are saved in a S3 bucket. I created a dynamodb table for storing metadata such a
s the start index and end index of each document, when it was uploaded etc.. Also, I found a way to delete the indexes o
f the FAISS system when the user wants to remove a pdf file to save memory. The problem is that I don't think that the F
AISS system is useful for a production application.  

Therefore, the RAG system would be hosted entirely in AWS where I
 will use Bedrock to host the LLM because I am dealing with sensitive data and this vectorstore needs to be hosted in AW
S too. So I am looking for a vectorstore for production and self-hosted. 

  
What alternatives could I use or approache
s.

  
Thanks
```
---

     
 
all -  [ Streamlit Data Analysis App ](https://www.reddit.com/r/Streamlit/comments/1fjo9es/streamlit_data_analysis_app/) , 2024-09-19-0912
```
Hi guys,

I have just been looking through the app gallery, I am looking for a data analysis AI template similar to the 
one on chainlit cookbook but for streamlit?

Here is the streamlit version [https://github.com/Chainlit/openai-assistant
](https://github.com/Chainlit/openai-assistant)

I have tried creating a data analyst AI from scratch with langchain but
 just can't get the ui right so if anyone knows a good repo please let me know!
```
---

     
 
all -  [ RAG Agents or LangGraph? ](https://www.reddit.com/r/LangChain/comments/1fjo3im/rag_agents_or_langgraph/) , 2024-09-19-0912
```
Hey everyone, 

I've been working with LangChain for around 6 months now and have a solid understanding of RAG, with a f
ew projects under my belt. I'm wondering what the next step should be—should I focus on RAG agents or dive into LangGrap
h?
```
---

     
 
all -  [ Langchain alternatives ](https://www.reddit.com/r/LangChain/comments/1fjmr4t/langchain_alternatives/) , 2024-09-19-0912
```
Hey,

I've been using LangChain for over 1.5 years, and I'm wondering if there are any better alternatives out there tha
t I might be missing out on. I've heard about DSPy—does it work with LangChain? What are the pros and cons (excluding co
mplexity)?
```
---

     
 
all -  [ OpenAI's Whisper AI Voice Psychologist Chatbot  ](https://www.reddit.com/r/LangChain/comments/1fjlwas/openais_whisper_ai_voice_psychologist_chatbot/) , 2024-09-19-0912
```
Hey everyone, 

In this video, I’m showing you something I’ve been working on — an **AI Voice Psychologist Chatbot**! Th
is bot uses AI and natural language processing to have conversations just like a psychologist would. You can literally t
alk to it, and it will respond in a thoughtful, meaningful way. 🎤💬

🔹 **What it does:**

* Listens to your voice
* Uses 
AI to understand and respond
* Easy to use with a clean Streamlit interface

If you're into AI or just curious how tech 
is helping mental health, check this out. I’ll be walking through how it works and showing a live demo!

💻 **Try it your
self** ▶ [Check out the live demo](https://tec-psychologists.streamlit.app/)  
🛠 **GitHub repo** ▶ [Explore the code](ht
tps://github.com/Rizwanali324)

Thanks a lot for watching! Your support means so much to me. Don’t forget to like 👍, com
ment 💬, and hit that subscribe button 🔔 if you enjoy my content.

💖 **Subscribe** ▶ [Join the community!](https://www.yo
utube.com/@Scoopsie-t2b)  
📌 **GitHub** ▶ [Check out my projects](https://github.com/Rizwanali324)  
📌 **LinkedIn** ▶ [C
onnect with me](https://www.linkedin.com/in/rizwan-ali123/)  
📌 **Facebook** ▶ [Follow me on Facebook](https://www.faceb
ook.com/rizwanali324)

Thanks for all your comments and support! ❤️

#AI #MentalHealth #Chatbot #VoiceAI #Streamlit #NLP

```
---

     
 
all -  [ Only text-oriented agent tools? ](https://www.reddit.com/r/crewai/comments/1fjkbbj/only_textoriented_agent_tools/) , 2024-09-19-0912
```
I’ve been digging into CrewAI lately and looking at all the tools they offer, and the ones from Composio. 

Almost all o
f them seem very text-oriented, ie accept some parameters, and output text. 

Since tools can output Pydantic objects (c
orrect me if I’m wrong), I’m somewhat surprised that not many tools take advantage of that.  

Anyone seen any object-ba
sed tools out there which aren’t just one-shot tools which spit out text?

Also I haven’t seen any RAG tools that handle
 a continuous conversation. They mostly are focused on one-shot RAG with no access to conversation history. 

Update: By
 tools, I had meant specifically for “tool calling”, like the LangChain compatible tools that CrewAI or LangGraph can ca
ll. 
```
---

     
 
all -  [ Only text-oriented agent tools? ](https://www.reddit.com/r/AI_Agents/comments/1fjkavt/only_textoriented_agent_tools/) , 2024-09-19-0912
```
I’ve been digging into CrewAI lately and looking at all the tools they offer, and the ones from Composio. 

Almost all o
f them seem very text-oriented, ie accept some parameters, and output text. 

Since tools can output Pydantic objects (c
orrect me if I’m wrong), I’m somewhat surprised that not many tools take advantage of that.  

Anyone seen any object-ba
sed tools out there which aren’t just one-shot tools which spit out text?

Also I haven’t seen any RAG tools that handle
 a continuous conversation. They mostly are focused on one-shot RAG with no access to conversation history. 

Update: Sa
w I wasn’t clear about tools, from some of the comments. By tools, I had meant specifically for “tool calling”, like the
 LangChain compatible tools that CrewAI or LangGraph can call. 
```
---

     
 
all -  [ Free RAG course using LangChain and LangServe by NVIDIA (limited time) ](https://www.reddit.com/r/LangChain/comments/1fjjymu/free_rag_course_using_langchain_and_langserve_by/) , 2024-09-19-0912
```
Hi everyone, just came to know NVIDIA is providing a free course on the RAG framework for a limited time, including **sh
ort videos, coding exercises and free NVIDIA LLM API.** I did it and the content is pretty good, especially the detailed
 jupyter notebooks. You can check it out here: [https://nvda.ws/3XpYrzo](https://nvda.ws/3XpYrzo)

To log in, you must r
egister (top-right) with your email id on the landing page as in the URL.
```
---

     
 
all -  [ Getting Chat History working  ](https://www.reddit.com/r/LangChain/comments/1fjb9lt/getting_chat_history_working/) , 2024-09-19-0912
```
Hey All, 

I'm a little new to Langchain, and having some difficulty getting my RAG bot to answer contextual questions b
ased on chat history, given that most of the information online suggests using some deprecated classes like Conversation
BufferMemory + StuffDocumentsChain.  I'm not nearly experienced enough to figure out exactly what I'm doing wrong, but c
urrently the chatbot won't pull on any previous answer as context - anyone have advice here?

    def ask_and_get_answer
(vector_store, q, k=3):
    
        llm = ChatOpenAI(model_name= 'gpt-4o', temperature = 1)
        retrieval_qa_chat_p
rompt = hub.pull('langchain-ai/retrieval-qa-chat')
        retriever = vector_store.as_retriever(search_type='similarity
') # Search kwargs retruns 3 closest chunks to query
    
        ## CHAIN TO ENABLE CONTEXTUAL CHAT HISTORY
    
      
  # Contextualize question
        contextualize_q_system_prompt = '''
            Given a chat history and the latest u
ser question
            which might reference context in the chat history, formulate a standalone
            question 
which can be understood without the chat history. '''
    
        contextualize_q_prompt = ChatPromptTemplate.from_mess
ages(
            [
                MessagesPlaceholder(variable_name=  'chat_history'),
                ('system', cont
extualize_q_system_prompt),
                ('human', '{input}')
            ]
        )
    
        history_aware_retr
iever = create_history_aware_retriever(llm=llm, retriever=retriever, prompt=contextualize_q_prompt)
    
        # Answe
r question
        qa_system_prompt = '''
            You are an assistant for question-answering tasks. Use the followi
ng pieces of
            retrieved context to answer the question. If you don't know the answer, just say 
            t
hat you don't know. Use three sentences maximum and keep the answer concise.
            {context}
            '''
    

        qa_prompt = ChatPromptTemplate.from_messages(
            [
                MessagesPlaceholder(variable_name='c
hat_history'),
                ('system', qa_system_prompt),
                ('human', '{input}')
            ]
        
)
        combine_docs_chain = create_stuff_documents_chain(llm=llm, prompt=qa_prompt)
        rag_chain = create_retrie
val_chain(history_aware_retriever, combine_docs_chain)
    
        ### Statefully manage chat history ###
        store
 = {}
    
        def get_session_history(session_id: str) -> BaseChatMessageHistory:
            if session_id not in 
store:
                store[session_id] = InMemoryChatMessageHistory()
            return store[session_id]
    
      
  conversational_rag_chain = RunnableWithMessageHistory(
            rag_chain,
            get_session_history,
       
     input_messages_key='input',
            output_messages_key='answer',
            history_messages_key='chat_histor
y'
        )
    
        answer = conversational_rag_chain.invoke({'input': q},
               config={'configurable': 
{'session_id': 'chat_history'}})
    
        return answer['answer']
```
---

     
 
all -  [ RAG application for generating SQL queries  ](https://www.reddit.com/r/LangChain/comments/1fj8jrb/rag_application_for_generating_sql_queries/) , 2024-09-19-0912
```
I want to build an RAG application that takes a  natural language prompt and generates a context aware SQL query based o
n it. I'm new to this and had a few questions:

1) My understanding of the workflow is to get my database's metadata (ta
bles, fields, types, relationships etc.) and vectorize it to store it in a vector store. The user prompt is also vectori
zed and with a similarly search, I get the similar vectors from the vector store to send it as context along with the us
er prompt to generate a SQL query as response. Is this the right flow?

2) I want to run the embedding model and llm mod
el locally. What are my options?

3) I understand vectorizing text data such as documents and page content but how would
 it work with the database metadata?
```
---

     
 
all -  [ Best way to set up a vector-store for structured data. ](https://www.reddit.com/r/LangChain/comments/1fj6cb7/best_way_to_set_up_a_vectorstore_for_structured/) , 2024-09-19-0912
```
Hi. Im relatively new to using langchain.

I'm working on a personal project where I vectorise some metadata of an e-com
merce site and set up a chat bot using a history aware retriever. 

I noticed that if I use csv data the bot doesn't do 
very well with bringing relevant data but as soon as it's in JSON format it performs far better. 

My question is 
1. wh
y is that the case?  
2. Can anyone point me to some tools that does a good job at storing structured data in a vector s
tore. 
3. How cab I deploy this in a production environment where the Metadata is updated on a weekly basis? Is there a 
way to routinely update the vector-store without splitting and chucking everything all over again (this'll cause a lot o
f downtime if done weekly)
```
---

     
 
all -  [ Langchain v0. 3 released ](https://www.reddit.com/r/LangChain/comments/1fj152a/langchain_v0_3_released/) , 2024-09-19-0912
```
Recently langchain v0.3 has released but what are some major changes or add-on in the latest version ? 
```
---

     
 
all -  [ Is Ollama really using my GPU for text generation ](https://www.reddit.com/r/ollama/comments/1fiyy64/is_ollama_really_using_my_gpu_for_text_generation/) , 2024-09-19-0912
```
Hello to the community!

I am relatively new to the field and am implementing RAG using Ollama. I have a question regard
ing Ollama and GPU usage. When I start the Ollama server and run my script, I can see with `nvidia-smi` that the Ollama 
server is loaded into GPU memory. However, shouldn’t I be able to see that Ollama is actively using the GPU with the `nv
top` command? It seems that during text generation, Ollama is only using the CPU, as all GPU utilization values show 0%.


Am I understanding this correctly, or could something else be happening? Any advice or help would be greatly appreciat
ed. Thanks in advance!



https://preview.redd.it/7fcxzdi8ddpd1.png?width=698&format=png&auto=webp&s=ecc4f6448db1b311c82
c993241a9fd6eef05a331

https://preview.redd.it/6cnzv959ddpd1.png?width=967&format=png&auto=webp&s=f98b28a185f935d1896f68
384ac5f207fe430e12

https://preview.redd.it/q5d0ff4addpd1.png?width=1017&format=png&auto=webp&s=f7c8e83c3af5938e27ccb3e2
03adfd9068c71e28


```
---

     
 
all -  [ How I created a RAG / ReAct flow using LangGraph (Studio) ](https://www.reddit.com/r/LangChain/comments/1fiyrpn/how_i_created_a_rag_react_flow_using_langgraph/) , 2024-09-19-0912
```
  
  
For my last project, I had to create a RAG / ReAct flow and used a combination of LangGraph and LangGraph Studio. 
The final flow looked like the graph shown below. It took me some time to figure out how to set everything up, so here i
s a summary of how I got started and why I chose LangGraph and LangGraph Studio.

https://preview.redd.it/pxq44jqu9dpd1.
png?width=1091&format=png&auto=webp&s=d3fffd7e2d857f6879e00f832fabde94251c204a

  
**Why ReAct Flows?**  
ReAct flows co
mbine an LLM's reasoning with action-taking capabilities, allowing diverse question-answering while minimizing hallucina
tions.

**Why LangGraph (Studio) ?**  
In the past, connecting several agents and chains quickly became confusing and ma
de it difficult for me to debug. So, I decided to use LangGraph. Since it integrates well with LangSmith, it also helped
 me efficiently trace my LLM calls without extra setup. The framework is still in the early stages, and many improvement
s are needed to make it easier to use and support a broader case of use cases.

LangGraph Studio's interactive environme
nt allows for real-time debugging and testing, making it easier to spot errors and optimize the flow. The biggest downsi
de I experienced using LangGraph Studio was that it runs on Docker containers. It's a really heavy application to run an
d it slows down my workstation.

I don't have a paid subscription to LangGraph Cloud, so I hosted the final app using a 
Docker container on Google Cloud run.

**Steps to Build a ReAct Flow:**

1. **Visualize the Flow:**
   * Start by drawin
g your flow to plan the structure.
2. **Create Flow Nodes:**
   * **Detect Intent:** Identify user intent to direct the 
flow appropriately.
   * **Split Questions:** Break down multi-part questions for targeted responses.
   * **LLM Answer:
** Handle simple queries directly with an LLM.
   * **Retrieve:** Fetch relevant documents for context.
   * **Transform
 Docs:** Clean and filter retrieved documents.
   * **RAG Answer:** Use context to generate a comprehensive response.
  
 * **Cite Sources:** Could you provide transparency by citing sources?
   * **SQL Agent:** Run database queries for data
-driven questions.
3. **Connect the Nodes:**
   * Use LangGraph's `StateGraph` to connect nodes and define flow logic.
4
. **Visualize with LangGraph Studio:**
   * This tool inspects and tests your flow, ensuring data moves correctly betwee
n nodes.

**Configuring the Graph:**  
Set up a `langgraph.json` file to point to your graph and manage dependencies.

F
or more details, check out the full tutorial on Medium: [How to Implement a ReAct Flow Using LangGraph Studio ](https://
medium.com/vectrix-ai/how-to-implement-a-react-flow-using-langgraph-studio-5e4b859b5506).
```
---

     
 
all -  [ Open-Source LLM Tools for Simplifying Paper Reading? ](https://www.reddit.com/r/LangChain/comments/1fiwdag/opensource_llm_tools_for_simplifying_paper_reading/) , 2024-09-19-0912
```
Programmer here. Any good open-source projects using LLMs to help read and understand academic papers?
```
---

     
 
all -  [ How are you all building human in the loop systems ](https://www.reddit.com/r/LangChain/comments/1fiqryc/how_are_you_all_building_human_in_the_loop_systems/) , 2024-09-19-0912
```
I'm currently working on a project where our application has tons of documents ingested and embedded in a vector store. 
It's honestly a big dumping ground so as is standard, I'm putting garbage in and getting garbage out

To combat this I a
m thinking about building a human enhanced system. I'm picturing the bot responding to the user query with an answer ret
rieved from the embeddings it found initially based on standard semantic search. A moderator then says 'No actually the 
answer you want is in documents A and B'. How would I go about teaching my bot to favor embeddings from those documents 
next time a similar query comes in?

I don't want the ranking to be part of the document embedding because the originall
y fetched documents are not bad necessarily. They may have some data that's just old and the moderator just happens to k
now about more up to date documents. I just want to nudge the system to rank the embeddings from the moderator specified
 documents higher next time a similar query comes in

Over time I'm thinking with enough input the application will natu
rally become more accurate as people mostly ask similarish questions and the bad embeddings just fall off from the conte
xt as more accurate documents get highly ranked
```
---

     
 
all -  [ Langchain ChatOllama().invoke() produced error: AttributeError: 'ModelPrivateAttr' object has no att ](https://www.reddit.com/r/LangChain/comments/1finnuj/langchain_chatollamainvoke_produced_error/) , 2024-09-19-0912
```
0

I used the following code to test if the ChatOllama() is working for me

    from langchain_ollama import ChatOllama

    
    chatmodel = ChatOllama(
        model='mistral:latest' # also tried model = 'mistral'
    )
    
    response_m
essage = chatmodel.invoke('Tell me a joke')

However, I received the following error message `AttributeError: 'ModelPriv
ateAttr' object has no attribute 'chat'`

Not sure what went wrong, any help is appreciated!

Before running the above p
ython code, I did verify the Ollama server is on and I was able to run the Ollama model in my terminal
```
---

     
 
all -  [ Text preprocessing before embeddings. ](https://www.reddit.com/r/LangChain/comments/1filu0o/text_preprocessing_before_embeddings/) , 2024-09-19-0912
```
I'm trying to make a recommendation chatbot based on the documents at the company I work for.  
The user can use this ch
atbot to list the documents that are relevant to their role, or just about a topic in specific.  
Each document is repre
sented by its summary, introduction, objectives, keyword, department, unit, etc...  
I'm using OpenAI text-embedding-3-s
mall and my question is, how can I preprocess this documents before feeding them into the embedding model so I can maxim
ize the retrieval process later?  

```
---

     
 
all -  [ List of FREE and Best Selling Discounted Courses ](https://www.reddit.com/r/udemyfreebies/comments/1fih9sq/list_of_free_and_best_selling_discounted_courses/) , 2024-09-19-0912
```
# Udemy Free Courses for 17 September 2024

Note : Coupons might expire anytime, so enroll as soon as possible to get th
e courses for FREE.

* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/14928/)Machine Learning using Python Programmin
g
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/14927/)Building Full Stack Python Web Apps Backed By Google Sheets

* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/14926/)Curso Completo de Linux Ubuntu
* [REDEEM OFFER ](https://ido
wnloadcoupon.com/udemy/14925/)Complete web development course
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/8974/)
Building Gen AI App 12+ Hands-on Projects with Gemini Pro
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/10198/)Jav
a Spring Boot: Professional eCommerce Project Masterclass
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/12239/)Com
plete Generative AI Course With Langchain and Huggingface
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/14529/)\[N
EW\] 2024: The Generative AI Lifecycle: A Primer
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/6709/)NLP – Buildin
g your own chatbots using AI
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/13966/)Mastering Power BI: Your Ultimat
e PL-300 Practice Tests 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/12759/)\[NEW\] 2024:Mastering Generativ
e AI-From LLMs to Applications
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/12369/)Build Instagram clone – React 
TailwindCSS Firebase
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/14530/)\[NEW\]Mastering Retrieval Augmented Gen
eration (RAG) IN LLMs
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/1606/)E-Commerce con ASP.NET Core | React | Cl
ean Architecture
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/8098/)Complete Machine Learning,NLP Bootcamp MLOPS 
& Deployment
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/14924/)ChatGPT for Business Analysts
* The Complete Gui
de to Instagram Marketing for Businesses
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/11483/)
* [REDEEM OFFER ](ht
tps://idownloadcoupon.com/udemy/9706/)Scrum Master Certification
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/111
41/)Advanced Scrum Master Certification
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/1724/)Outstanding | Python P
rogramming with Examples in One Day
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/10091/)Executive Diploma in Huma
n Resources Strategy
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/1719/)The Pandas Bootcamp | Data Analysis with 
Pandas Python3
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/4827/)Exam Test for Python OCR: Optical Character Rec
ognition OCR
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/2106/)Learn C# Programming with Examples in ONE DAY
* [
REDEEM OFFER ](https://idownloadcoupon.com/udemy/11983/)Research Methodologies in Strategy and Product Development
* [RE
DEEM OFFER ](https://idownloadcoupon.com/udemy/11942/)Adobe Premiere Pro CC Essential Video Editing Zero To Hero
* [REDE
EM OFFER ](https://idownloadcoupon.com/udemy/11840/)Blender Essential: From Beginner to 3D Masterclass
* [REDEEM OFFER ]
(https://idownloadcoupon.com/udemy/13077/)Complete Video Editing Mastery with Cyberlink PowerDirector
* [REDEEM OFFER ](
https://idownloadcoupon.com/udemy/1672/)Success Exam | Python NLTK : Natural Language ToolKit | NLP
* [REDEEM OFFER ](ht
tps://idownloadcoupon.com/udemy/7174/)Master Adobe Illustrator: Design Awesome Logos and Graphics
* [REDEEM OFFER ](http
s://idownloadcoupon.com/udemy/12315/)The Complete T-Shirt Design Toolkit: PS, AI
* [REDEEM OFFER ](https://idownloadcoup
on.com/udemy/9862/)Data Structures Algorithm DSA | Python+Javascript LEETCODE
* Advance MS Excel VBA for Beginner to Adv
anced
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/2643/)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/4834
/)Python Numpy Data Analysis for Data Scientist | AI | ML | DL
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/9668/
)Professional Diploma in Advertising and Public Relations
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/14922/)Pro
fessional Diploma in Administration Management
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/12683/)Python Mastery
 with Tabnine: AI-Enhanced Coding Efficiency
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/5752/)Complete Responsi
ve Web Development: 4 courses in 1
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/7903/)Cómo Crear un Blog con Inte
ligencia Artificial 2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/7512/)Oracle Java Certification Exam OCA 1Z
0-808 Preparation Part2
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/14569/)Professional Certificate in Marketing
 and Advertising
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/7812/)Máster en Comercio Electrónico con WordPress 
2024
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/9846/)Java 21 Programming Masterclass: Fundamentals for Beginne
rs
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/7902/)Crea una Página Web con Elementor Pro y el Tema Hello 2024

* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/11374/)The Complete Photo Editing Masterclass With Adobe and Canva
*
 [REDEEM OFFER ](https://idownloadcoupon.com/udemy/10280/)Essentials User Experience Design Adobe XD UI UX Design
* [RED
EEM OFFER ](https://idownloadcoupon.com/udemy/12274/)Mergers and Acquisitions: M
* [REDEEM OFFER ](https://idownloadcoup
on.com/udemy/6546/)Ultimate Character Design Course with Adobe Illustrator
* Cómo Crear un Blog con WordPress Para Princ
ipiantes 2024
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/7901/)
* [REDEEM OFFER ](https://idownloadcoupon.com/ud
emy/6292/)Yoga For a Healthy Back
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/11557/)Fast-track to Google Sheets
 Mastery Weekend Crash Course
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/8609/)PowerShell Regular Expressions: 
Regex Master Class
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/7698/)PowerShell Functions Master Class
* [REDEEM
 OFFER ](https://idownloadcoupon.com/udemy/14921/)Use ChatGPT And Ai To Make Money With Affiliate Marketing
* [REDEEM OF
FER ](https://idownloadcoupon.com/udemy/14920/)Wireless Wonders: Mastering ESP32 OTA (Over the Air) Updates
* [REDEEM OF
FER ](https://idownloadcoupon.com/udemy/14919/)Excel Intermedio
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/161/
)Ubuntu Network Server
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/11052/)Docker Basics Unleashed
* [REDEEM OFFE
R ](https://idownloadcoupon.com/udemy/2272/)TypeScript para principiantes desde 0
* [REDEEM OFFER ](https://idownloadcou
pon.com/udemy/11367/)Deep Learning Python Project: CNN based Image Classification
* [REDEEM OFFER ](https://idownloadcou
pon.com/udemy/8768/)أساسيات الذكاء الاصطناعي: مقدمة عن تقنيات الذكاء الاصطناعي
* [REDEEM OFFER ](https://idownloadcoupon
.com/udemy/14892/)Make a Web Template Responsive Using HTML5
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/8274/)G
oogle Analytics 4 (GA4) Certification. How to Pass the Exam
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/7904/)Có
mo Crear un Embudo de Ventas con WordPress Desde Cero 2024
* Upgrade Your Social Media Presence with ChatGPT
* [REDEEM O
FFER](https://idownloadcoupon.com/udemy/9689/)
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/7915/)Linux Security 
Checkup: Quick Audit Essentials
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/10953/)Ethical Hacking: Post-Exploit
ation
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/8729/)Chief Executive Officer (CEO) Program
* [REDEEM OFFER ](
https://idownloadcoupon.com/udemy/4754/)Linux Command Line Arsenal
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/7
922/)Build 20 JavaScript Projects in 20 Day with HTML, CSS & JS
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/9688
/)Reputation Management: Take Control of Your Company’s Image
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/10218/
)Augmented Reality Certification ( AR Foundation, Vuforia )
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/8763/)Wi
ndows Endpoint Security
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/14918/)Logo Design Essentials: Photoshop
* [
REDEEM OFFER ](https://idownloadcoupon.com/udemy/14916/)American English Consonants for Chinese Professionals
* [REDEEM 
OFFER ](https://idownloadcoupon.com/udemy/14915/)600 AEM Interview Questions Practice Test
* [REDEEM OFFER ](https://ido
wnloadcoupon.com/udemy/12204/)Python Project: Build a PDF File Handling Tool from Scratch
* [REDEEM OFFER ](https://idow
nloadcoupon.com/udemy/12392/)Word Stress of American English
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/12386/)
Construction Methodology of Steel
* [REDEEM OFFER ](https://idownloadcoupon.com/udemy/12677/)Advanced Program in Product
 Development and Management

GET MORE FREE ONLINE COURSES WITH CERTIFICATE – [CLICK HERE](https://idownloadcoupon.com/)
```
---

     
 
all -  [ Problem with OllamaEmbeddings and PGVector.from_documents ](https://www.reddit.com/r/LangChain/comments/1fih5yc/problem_with_ollamaembeddings_and_pgvectorfrom/) , 2024-09-19-0912
```
I started developing with LangChain and Vectorstores.

It is working for OpenAI but not for Ollama. Error is `404 page n
ot found`

Any Idea anyone?

Commandline output:

    $python script.py
    Uploading pdf started.
    docs loaded
    e
mbeddings_from_documents executed
    Error in embeddings_from_documents_ollama: 404 page not found
    embeddings_from_
documents_ollama executed
    Processing done

script.py:

    from langchain_ollama import OllamaEmbeddings
    from la
ngchain_openai.embeddings import OpenAIEmbeddings
    from langchain_community.document_loaders import PyPDFLoader
    f
rom langchain.text_splitter import CharacterTextSplitter
    from langchain_postgres.vectorstores import PGVector
    
 
   from secret_key import openai_key  # only for personal secret key
    
    import os
    
    os.environ['OPENAI_API_
KEY'] = openai_key
    
    # Postgress Database Connection details
    HOST = 'localhost'
    DATABASE = 'vectordb'
   
 USER = 'testuser'
    PWD = 'testpwd'
    PORT = 6432
    DRIVER = 'psycopg'
    
    CONNECTION_STRING = PGVector.conn
ection_string_from_db_params(DRIVER, HOST, PORT, DATABASE, USER, PWD, )
    
    FILE_NAME = 'data/budget_speech.pdf'
  
  COLLECTION_NAME = 'Book: Budget Speech'
    
    
    def pdf_content_into_documents():
        loader = PyPDFLoader(F
ILE_NAME)
        documents = loader.load_and_split()
        text_splitter = CharacterTextSplitter(chunk_size=2000, chu
nk_overlap=100)
        docs = text_splitter.split_documents(documents)
        return docs
    
    
    def embeddings
_from_documents(docs):
        embeddings = OpenAIEmbeddings()
        # # create the store
        PGVector.from_docume
nts(
            embedding=embeddings,
            documents=docs,
            collection_name=COLLECTION_NAME,
        
    connection=CONNECTION_STRING,
            pre_delete_collection=True,
        )
    
    
    def embeddings_from_do
cuments_ollama(docs):
        try:
            embeddings = OllamaEmbeddings(
                model='all-minilm',
      
          base_url='http://localhost:11434',
            )
            # # create the store
            PGVector.from_do
cuments(
                embedding=embeddings,
                documents=docs,
                collection_name=COLLECTIO
N_NAME,
                connection=CONNECTION_STRING,
                pre_delete_collection=True,
            )
        
except Exception as e:
            print(f'Error in embeddings_from_documents_ollama: {e}')
    
    
    def load_pdf_i
nto_db():
        docs = pdf_content_into_documents()
        print('docs loaded')
        embeddings_from_documents(doc
s)
        print('embeddings_from_documents executed')
        embeddings_from_documents_ollama(docs)
        print('emb
eddings_from_documents_ollama executed')
    
    
    def ask_question(query):
        embeddings = OpenAIEmbeddings()

    
        # load the store for searching
        pgvector_docsearch = PGVector(
            embeddings=embeddings,
  
          collection_name=COLLECTION_NAME,
            connection=CONNECTION_STRING,
            use_jsonb=True,
       
 )
    
        searched_docs = pgvector_docsearch.search(query, 'mmr', k=1)
        # searched_docs = pgvector_docsearc
h.similarity_search(query, k=4)
        result = searched_docs[0].page_content
        print(result)
    
    
    if __
name__ == '__main__':
        print('Uploading pdf started.')
        load_pdf_into_db()
    
     #   print('Searching 
based on query.')
     #   ask_question(query='What is the name of the Prime Minister ?')
    
        print('Processing
 done')

-----------------------------------------------------------------------------------

UPDATE 1:  
Doublecheck Ol
lama Embeddings:

    curl  -d '{'model': 'all-minilm', 'prompt': 'Hello, world!'}'http://localhost:11434/api/embeddings


Return:

    {'embedding':[0.2084004133939743,-0.0931989848613739,-0.3474540412425995,-0.2145247459411621,-0.116439498
96097183,-0.5225321054458618,0.3659696877002716,-0.3055870532989502,-0.3007390797138214,0.006659090518951416,0.072216771
54302597,-0.631626546382904,0.5624032616615295,0.20714163780212402,-0.03183358907699585,-0.23700833320617676,-0.27402549
982070923,-0.25414353609085083,-0.5537203550338745,-0.30361267924308777,0.19056284427642822,0.3730108141899109,0.0467369
9662089348,0.4185698330402374,-0.7141198515892029,0.32930928468704224,0.2059059888124466,0.17200733721256256,-0.20658761
262893677,-0.4961510896682739,-0.004195600748062134,0.4465978741645813,-0.19888943433761597,0.06801576167345047,0.106585
73359251022,0.16
    [...]

So this looks fine.

UPDATE 2:

Activate DEBUG logging in my Python script:

    import logg
ing
    logging.basicConfig(level=logging.DEBUG)

Output;

    [...]
    DEBUG:httpcore.http11:receive_response_headers.
started request=<Request [b'POST']>
    DEBUG:httpcore.http11:receive_response_headers.complete return_value=(b'HTTP/1.1
', 404, b'Not Found', [(b'Content-Type', b'text/plain'), (b'Date', b'Tue, 17 Sep 2024 21:43:33 GMT'), (b'Content-Length'
, b'18')])
    INFO:httpx:HTTP Request: POST  'HTTP/1.1 404 Not Found'
    DEBUG:httpcore.http11:receive_response_body.s
tarted request=<Request [b'POST']>
    DEBUG:httpcore.http11:receive_response_body.complete
    DEBUG:httpcore.http11:re
sponse_closed.started
    DEBUG:httpcore.http11:response_closed.complete
    Error in embeddings_from_documents_ollama: 
404 page not foundhttp://127.0.0.1:11434/api/embed

HTTP Request: POST [http://127.0.0.1:11434/api/embed](http://127.0.0
.1:11434/api/embed) and not HTTP Request: POST [http://127.0.0.1:11434/api/embeddings](http://127.0.0.1:11434/api/embedd
ings)

UPDATE 3:  
I changed in file \~/.local/lib/python3.10/site-packages/ollama/\_client.py Line 264:  
from '/api/em
bed' to '/api/embeddings':

      def embed(                 # this is line 251
        self,
        model: str = '',
 
       input: Union[str, Sequence[AnyStr]] = '',
        truncate: bool = True,
        options: Optional[Options] = Non
e,
        keep_alive: Optional[Union[float, str]] = None,
      ) -> Mapping[str, Any]:
        if not model:
         
 raise RequestError('must provide a model')
    
        return self._request(
          'POST',
          '/api/embeddi
ngs',     # this is changed
          json={
            'model': model,
            'input': input,
            'trunca
te': truncate,
            'options': options or {},
            'keep_alive': keep_alive,
          },
        ).json()


Output:

    DEBUG:httpcore.http11:receive_response_headers.started request=<Request [b'POST']>
    DEBUG:httpcore.htt
p11:receive_response_headers.complete return_value=(b'HTTP/1.1', 200, b'OK', [(b'Content-Type', b'application/json; char
set=utf-8'), (b'Date', b'Tue, 17 Sep 2024 21:54:55 GMT'), (b'Content-Length', b'16')])
    INFO:httpx:HTTP Request: POST
  'HTTP/1.1 200 OK'
    DEBUG:httpcore.http11:receive_response_body.started request=<Request [b'POST']>
    DEBUG:httpco
re.http11:receive_response_body.complete
    DEBUG:httpcore.http11:response_closed.started
    DEBUG:httpcore.http11:res
ponse_closed.complete
    Error in embeddings_from_documents_ollama: 'embeddings'

Error: 'embeddings' ..... very helpfu
l :( time to go to bed.
```
---

     
 
all -  [ İnput Guardrails ](https://www.reddit.com/r/LangChain/comments/1fieice/input_guardrails/) , 2024-09-19-0912
```
How do you use input guardrails in your project? I have no idea how to implement them in a project. Do you use an LLM or
 are there specific tools to hide sensitive data? How is the workflow?
```
---

     
 
all -  [ Confused between AI SDK and LangChain ](https://www.reddit.com/r/LangChain/comments/1fie8ul/confused_between_ai_sdk_and_langchain/) , 2024-09-19-0912
```
I'm new to building RAG applications. I came across the AI SDK from Vercel and LangChain. How are they different when th
ey both provide abstractions to make inferences from an LLM?

```
---

     
 
all -  [ Understanding the Power BI toolkit and agent ](https://www.reddit.com/r/LangChain/comments/1fidecq/understanding_the_power_bi_toolkit_and_agent/) , 2024-09-19-0912
```
I am trying to work with the Power BI toolkit and agent. I want to be able to allow users to ask questions to a selected
 Power BI dataset and extract relevant data out. After going through the documentation, it seems the only metadata about
 the dataset I have to input is the list of table names. How will the model know about the relationships between the tab
les, or about any existing measures within those table names?

  
Is it even worth using the Power BI toolkit for my use
 case, or is it too underdeveloped, and would I be better off trying to leverage an LLM differently?
```
---

     
 
all -  [ Issues Integrating create_pandas_dataframe_agent with Hugging Face Inference Endpoint ](https://www.reddit.com/r/LangChain/comments/1fic5b6/issues_integrating_create_pandas_dataframe_agent/) , 2024-09-19-0912
```
Hello,

I'm currently working on a project using LangChain. Specifically, I'm trying to connect the create\_pandas\_data
frame\_agent function to a Hugging Face Inference Endpoint, but I keep encountering errors. Is it impossible to use this
 combination? No matter what I try, the issue persists.

Has anyone successfully done this or have any insights on how t
o resolve it?

    from langchain_community.llms import HuggingFaceEndpoint
    from langchain_community.chat_models.hug
gingface import ChatHuggingFace
    
    llm = HuggingFaceEndpoint(
        endpoint_url=hf_endpoint_url,
        max_ne
w_tokens=4500,
        temperature=0.5,
    )
    
    # Create the pandas dataframe agent
    agent = create_pandas_dat
aframe_agent(
        llm=llm,
        df=df,
        agent_type='openai-tools',
        allow_dangerous_code=True,
    
    verbose=True
    )
    
    agent.run({'input': 'Q'})

https://preview.redd.it/vzip08dat7pd1.png?width=1304&format=p
ng&auto=webp&s=3702ce3aec7a27cee750dadf576a0fbdbbefafbb

error : 

    TypeError: InferenceClient.text_generation() got 
an unexpected keyword argument 'tools'
```
---

     
 
all -  [ Interactive AI Agents Market Landscape Map (Sep 2024) ](https://www.reddit.com/r/AI_Agents/comments/1fibklp/interactive_ai_agents_market_landscape_map_sep/) , 2024-09-19-0912
```
'Hey, AI Agents enthusiasts! Check out the interactive AI Agents Market Landscape Map (Sept 2024).'

you can play with i
t here: [https://aiagentsdirectory.com/landscape](https://aiagentsdirectory.com/landscape)

https://preview.redd.it/i5jr
o3too7pd1.png?width=1319&format=png&auto=webp&s=91ff194bff623a634d76259220b9d8c706b11448


```
---

     
 
all -  [ Has anyone used LangGraph to build agentic pipelines to assist writing? ](https://www.reddit.com/r/WritingWithAI/comments/1fiaqbk/has_anyone_used_langgraph_to_build_agentic/) , 2024-09-19-0912
```
I'm looking to experiment with augmenting my writing with a 'handmade' agentic workflow with lots of HiL. I've written s
ome short stories manually filtering and collating paragraphs from ChatGPT models I fine-tuned. 

Anyone here tried out 
LangGraph for this kind of thing?

  
[https://learn.deeplearning.ai/courses/ai-agents-in-langgraph/lesson/7/essay-write
r](https://learn.deeplearning.ai/courses/ai-agents-in-langgraph/lesson/7/essay-writer)

[https://langchain-ai.github.io/
langgraph/tutorials/multi\_agent/multi-agent-collaboration/](https://langchain-ai.github.io/langgraph/tutorials/multi_ag
ent/multi-agent-collaboration/)
```
---

     
 
MachineLearning -  [ [P] Review and suggest ideas for my chatbot ](https://www.reddit.com/r/MachineLearning/comments/1fb2mwl/p_review_and_suggest_ideas_for_my_chatbot/) , 2024-09-19-0912
```
Ok, so I am currently trying to build support chatbot with following technicalities 
1. FastAPI for web server(Need to m
ake it faster)
2. Qdrant as Vector Data Base(Found it to be the fastest amongst Chromadb, Elastic Search and Milvus)
3. 
MongoDB for storing all the data and feedback.
4. Semantic chunking with max token limit of 512.
5. granite-13b-chat-v2 
as the LLM(I know it's not good but I have limited options available)
6. The data is structured as well as unstructured.
 Thinking of having involving GraphRAG with current architecture.
7. Multiple data sources stored in multiple collection
s of vector database because I have implemented an access control.
8. Using mongoengine currently as a ORM. If you know 
something better please suggest.
9. Using all-miniLM-l6-v2 as vector embedding currently but planning to use stella_en_4
00M_v5.
10. Using cosine similarity to retrieve the documents.
11. Using BLEU, F1 and BERT score for automated evaluatio
n based on golden answer.
12. Using top_k as 3.
13. Currently using basic question answering prompt but want to improve 
it. Any tips? Also heard about Automatic Prompt Evaluation.
14. Currently using custom code for everything. Looking to u
se Llamaindex or Langchain for this. 
15. Right now I am not using any AI Agent, but I want to know your opinions. 
16. 
It's a simple RAG framework and I am working on improving it.
17. I haven't included reranker but I am planning to do so
 too.

I think I mentioned pretty much everything I am using for my project. So please share your suggestions, comments 
and reviews for the same. Thank you!!
```
---

     
 
MachineLearning -  [ [P] Lessons from Retrieval Augmented Generation ](https://www.reddit.com/r/MachineLearning/comments/1f9tvg7/p_lessons_from_retrieval_augmented_generation/) , 2024-09-19-0912
```
I implemented Rag in my organization and just wrote a blog about what we learned here:   
[https://www.b-yond.com/post/t
ransforming-telco-troubleshooting-our-journey-building-telcogpt-with-rag](https://www.b-yond.com/post/transforming-telco
-troubleshooting-our-journey-building-telcogpt-with-rag)

Hoping it would be helpful for those in this area. Covers rag 
evaluation (ragas), sql db, langchain agents vs chains, weaviate vector db, hybrid search, reranking, and more.

Some ad
ditional insights on ranking and hybrid search here:

[https://www.linkedin.com/posts/drzohaib\_transforming-telco-troub
leshooting-our-journey-activity-7232072089837486081--Le1?utm\_source=share&utm\_medium=member\_android](https://www.link
edin.com/posts/drzohaib_transforming-telco-troubleshooting-our-journey-activity-7232072089837486081--Le1?utm_source=shar
e&utm_medium=member_android)
```
---

     
 
deeplearning -  [ What is the best approach for Parsing and Retrieving Code Context Across Multiple Files in a Hierarc ](https://www.reddit.com/r/deeplearning/comments/1fh58oz/what_is_the_best_approach_for_parsing_and/) , 2024-09-19-0912
```
I want to implement a Code-RAG system on a code directory where I need to:

* Parse and load all the files from folders 
and subfolders while excluding specific file extensions.
* Embed and store the parsed content into a vector store.
* Ret
rieve relevant information based on user queries.

However, I’m facing two major challenges:

**File Parsing and Loading
:** What’s the most efficient method to parse and load files in a hierarchical manner (reflecting their folder structure
)? Should I use Langchain’s directory loader, or is there a better way? I came across the Tree-sitter tool in Claude-dev
’s repo, which is used to build syntax trees for source files—would this be useful for hierarchical parsing?

**Cross-Fi
le Context Retrieval:** If the relevant context for a user’s query is spread across multiple files located in different 
subfolders, how can I fine-tune my retrieval system to identify the correct context across these files? Would reranking 
resolve this, or is there a better approach?

**Query Translation:** Do I need to use Something like Multi-Query or RAG-
Fusion to achieve better retrieval for hierarchical data?

\[I want to understand how tools like [continue.dev](http://c
ontinue.dev/) and [claude-dev](https://github.com/saoudrizwan/claude-dev) work\]
```
---

     
 
deeplearning -  [ Month of August in AI ](https://www.reddit.com/r/deeplearning/comments/1f6zfz0/month_of_august_in_ai/) , 2024-09-19-0912
```
🔍 I**nside this Issue:**

* 🤖 La*test Breakthroughs: *This month it’s all about A*gents, LangChain RAG, and LLMs evaluat
ion challenges.*
* 🌐 AI Monthly News: Discover how these stories are revolutionizing industries and impacting everyday l
ife: E*U AI Act, California’s Controversial SB1047 AI regulation act, Drama at OpenAI, and possible funding at OpenAI by
 Nvidia and Apple.*
* 📚 Editor’s Special: This covers the interesting talks, lectures, and articles we came across recen
tly.

Follow me on Twitter and LinkedIn at [**RealAIGuys**](https://twitter.com/RealAIGuys) and [**AIGuysEditor**](https
://www.linkedin.com/in/vishal-rajput-999164122/) to get insight on new AI developments.

>**Please don't forget to subsc
ribe to our Newsletter:** [**https://medium.com/aiguys/newsletter**](https://medium.com/aiguys/newsletter)

# Latest Bre
akthroughs

Are Agents just simple rules? Are Agents just enhanced reasoning? The answer is yes and no. Yes, in the sens
e that agents have simple rules and can sometimes enhance reasoning capabilities compared to a single prompt. But No in 
the sense that agents can have a much more diverse functionality like using specific tools, summarizing, or even followi
ng a particular style. In this blog, we look into how to set up these agents in a hierarchal manner just like running a 
small team of Authors, researchers, and supervisors.

[**How To Build Hierarchical Multi-Agent Systems?**](https://mediu
m.com/aiguys/how-to-build-hierarchical-multi-agent-systems-dc26b19201d2?sk=90958e39e1a28f5030872a90f8e3f3da)

**TextGrad
**. It is a powerful framework performing automatic “differentiation” via text. **It backpropagates textual feedback pro
vided by LLMs to improve individual components of a compound AI system.** In this framework, LLMs provide rich, general,
 natural language suggestions to optimize variables in computation graphs, ranging from code snippets to molecular struc
tures. TextGrad showed effectiveness and generality across various applications, from question-answering and molecule op
timization to radiotherapy treatment planning.

[**TextGrad: Improving Prompting Using AutoGrad**](https://medium.com/ai
guys/textgrad-controlling-llm-behavior-via-text-2a82e2073d10?sk=3633a9aa63b884c97469bce659265921)

The addition of RAG t
o LLMs was an excellent idea. It helped the LLMs to become more specific and individualized. Adding new components to an
y system leads to more interactions and its own sets of problems. Adding RAG to LLMs leads to several problems such as h
ow to retrieve the best content, what type of prompt to write, and many more.

In this blog, we are going to combine the
 **LangChain RAG with DSPy**. We deep dive into how to evaluate the RAG pipeline quantitatively using **RAGAs** and how 
to create a system where instead of manually tweaking prompts, we let the system figure out the best prompt.

[**How To 
Build LangChain RAG With DSPy?**](https://medium.com/aiguys/how-to-build-langchain-rag-with-dspy-ce9154fbafaa?sk=b41d104
05f84c767cf9cd6a58d1ebac0)

As the field of natural language processing (NLP) advances, the evaluation of large language
 models (LLMs) like GPT-4 becomes increasingly important and complex. Traditional metrics such as accuracy are often ina
dequate for assessing these models’ performance because they fail to capture the nuances of human language. In this arti
cle, we will explore why evaluating LLMs is challenging and discuss effective methods like BLEU and ROUGE for a more com
prehensive evaluation.

[**The Challenges of Evaluating Large Language Models**](https://medium.com/aiguys/the-challenge
s-of-evaluating-large-language-models-ec2eb834a349)

# AI Monthly News

# AI Act enters into force

On 1 August 2024, th
e European Artificial Intelligence Act (AI Act) enters into force. The Act aims to foster responsible artificial intelli
gence development and deployment in the EU. The AI Act introduces a uniform framework across all EU countries, based on 
a forward-looking definition of AI and a risk-based approach:

* **Minimal risk:** most AI systems such as spam filters 
and AI-enabled video games face no obligation under the AI Act, but companies can voluntarily adopt additional codes of 
conduct.
* **Specific transparency risk:** systems like chatbots must clearly inform users that they are interacting wit
h a machine, while certain AI-generated content must be labelled as such.
* **High risk:** high-risk AI systems such as 
AI-based medical software or AI systems used for recruitment must comply with strict requirements, including risk-mitiga
tion systems, high-quality of data sets, clear user information, human oversight, etc.
* **Unacceptable risk:** for exam
ple, AI systems that allow “social scoring” by governments or companies are considered a clear threat to people’s fundam
ental rights and are therefore banned.

**EU announcement:** [**Click here**](https://commission.europa.eu/news/ai-act-e
nters-force-2024-08-01_en)

https://preview.redd.it/nwyzfzgm4cmd1.png?width=828&format=png&auto=webp&s=c873db37ca0dadd5b
510bea70ac9f633b96aaea4

# California AI bill SB-1047 sparks fierce debate, Senator likens it to ‘Jets vs. Sharks’ feud


**Key Aspects of SB-1047:**

* Regulation Scope: Targets “frontier” AI models, defined by their immense computational t
raining requirements (over 10²⁶ operations) or significant financial investment (>$100 million).
* Compliance Requiremen
ts: Developers must implement safety protocols, including the ability to immediately shut down, cybersecurity measures, 
and risk assessments, before model deployment.
* Whistleblower Protections: Encourages reporting of non-compliance or ri
sks by offering protection against retaliation.
* Safety Incident Reporting: Mandates reporting AI safety incidents with
in 72 hours to a newly established Frontier Model Division.
* Certification: Developers need to certify compliance, pote
ntially under penalty of perjury in earlier drafts, though amendments might have altered this.

**Pros:**

* Safety Firs
t: Prioritizes the prevention of catastrophic harms by enforcing rigorous safety standards, potentially safeguarding aga
inst AI misuse or malfunction.
* Incentivizes Responsible Development: By setting high standards for AI model training, 
the company encourages developers to think critically about the implications of their creations.
* Public Trust: Enhance
s public confidence in AI by ensuring transparency and accountability in the development process.

**Cons:**

* Innovati
on Stagnation: Critics argue it might stifle innovation, especially in open-source AI, due to the high costs and regulat
ory burdens of compliance.
* Ambiguity: Some definitions and requirements might be too specific or broad, leading to leg
al challenges or unintended consequences.
* Global Competitiveness: There’s concern that such regulations could push AI 
development outside California or the U.S., benefiting other nations without similar restrictions.
* Implementation Chal
lenges: The practicalities of enforcing such regulations, especially the “positive safety determination,” could be compl
ex and contentious.

**News Article:** [**Click here**](https://www.thenation.com/article/society/sb-1047-ai-big-tech-fi
ght/)

**Open Letter:** [**Click here**](https://safesecureai.org/open-letter)

https://preview.redd.it/ib96d7nk4cmd1.pn
g?width=828&format=png&auto=webp&s=0ed5913b5dae72e203c8592393e469d9130ed689

# MORE OpenAI drama

OpenAI co-founder John
 Schulman has left the company to join rival AI startup Anthropic, while OpenAI president and co-founder Greg Brockman i
s taking an extended leave until the end of the year. Schulman, who played a key role in creating the AI-powered chatbot
 platform ChatGPT and led OpenAI’s alignment science efforts, stated his move was driven by a desire to focus more on AI
 alignment and hands-on technical work. Peter Deng, a product manager who joined OpenAI last year, has also left the com
pany. With these departures, only three of OpenAI’s original 11 founders remain: CEO Sam Altman, Brockman, and Wojciech 
Zaremba, lead of language and code generation.

**News Article:** [**Click here**](https://techcrunch.com/2024/08/05/ope
nai-co-founder-leaves-for-anthropic/)

https://preview.redd.it/0vdjc18j4cmd1.png?width=828&format=png&auto=webp&s=e9de60
4c26aed3e47b50df3bdf114ef61f967080

# Apple and Nvidia may invest in OpenAI

Apple, which is planning to integrate ChatG
PT into iOS, is in talks to invest. Soon after, [*Bloomberg* also](https://www.bloomberg.com/news/articles/2024-08-29/nv
idia-has-held-discussions-about-joining-openai-s-funding-round?srnd=homepage-americas) reported that Apple is in talks b
ut added that Nvidia “has discussed” joining the funding round as well. The round is reportedly being led by Thrive Capi
tal and would value OpenAI at more than $100 billion.

**News Article:** [**Click here**](https://www.theverge.com/2024/
8/29/24231626/apple-nvidia-openai-invest-microsoft)

https://preview.redd.it/ude6jguh4cmd1.png?width=828&format=png&auto
=webp&s=3603cbca0dbb1be3e6d0efcf06c3a698428bbdd6

# Editor’s Special

* The AI Bubble: Will It Burst, and What Comes Aft
er?: [**Click here**](https://www.youtube.com/watch?v=91SK90SahHc&t=317s)
* Eric Schmidt Full Controversial Interview on
 AI Revolution (Former Google CEO): [**Click here**](https://www.youtube.com/watch?v=mKVFNg3DEng)
* AI isn’t gonna keep 
improving [**Click here**](https://www.youtube.com/watch?v=Y8Ym7hMR100)
* General Intelligence: Define it, measure it, b
uild it: [**Click here**](https://www.youtube.com/watch?v=nL9jEy99Nh0)
```
---

     
 
deeplearning -  [ Creating a project on NLP ](https://www.reddit.com/r/deeplearning/comments/1ey2e85/creating_a_project_on_nlp/) , 2024-09-19-0912
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

     
