 
all -  [ Practical Applications of Pythia in LLM Contexts: Chatbots, RAG Systems, and Summarization ](https://www.reddit.com/r/pythia/comments/1e52lyy/practical_applications_of_pythia_in_llm_contexts/) , 2024-07-17-0911
```
https://preview.redd.it/7pz9aa0teycd1.png?width=1920&format=png&auto=webp&s=701ca9ff431570cebcee5407258f16d19e97b136

*E
xplore the practical applications of Pythia and how it addresses LLM contexts to achieve reliable AI.*

[Pythia](https:/
/askpythia.ai/blog/introducing-pythia-the-ai-oracle-eradicating-llm-hallucinations) is a powerful hallucination detectio
n tool that detects [misinformation in large language model (LLM) outputs](https://www.weforum.org/agenda/2024/01/ai-dis
information-global-risks/) and ensures reliable interaction between AI and humans. It helps LLM developers and companies
 reduce error rates in LLM outputs, avoid spending millions on corrective procedures and legal liabilities, and maintain
 a good reputation among users.

Pythia’s unique [methodology](https://www.wisecube.ai/blog/the-wisecube-approach-to-enh
ancing-ai-reliability/) consists of claim extraction and categorization, real-time monitoring, and knowledge graph integ
ration to verify LLM response against legitimate sources of information. This enables Pythia to easily integrate with ch
atbots, RAG-based systems, and text summarization tools for real-time monitoring. It flags inappropriate outputs and gen
erates a detailed audit report highlighting the tool’s strengths and weaknesses. 

This feature allows developers and su
bject matter experts to work towards improving LLMs to mitigate hallucinations and serve their original purpose.

Let’s 
explore some of the Pythia use cases and how they address the LLM contexts in the real world.

# Pythia Use Cases

Here 
are the three common use cases of Pythia:

# Chatbots

Healthcare chatbots use natural language processing (NLP) to assi
st patients with medical support, such as assessing symptoms, appointment scheduling, or providing mental support. These
 chatbots are trained on medical databases to learn and improve their accuracy. Based on their learning, chatbots analyz
e user input and generate a relevant response for the user.

Pythia integrates within healthcare chatbots to monitor LLM
 responses against user queries. It measures the accuracy and alignment of the response with the user query by continuou
sly monitoring LLM activities. Whenever a user asks a question, and LLM generates a response, Pythia extracts knowledge 
triplets from the response and chatbot databases. It then compares knowledge triplets against each other to generate an 
LLM audit report.

# RAG (Retrieval-Augmented Generation) systems

[RAG systems](https://askpythia.ai/blog/a-guide-to-in
tegrating-pythia-api-with-rag-based-systems-using-wisecube-python-sdk) use an additional knowledge base beyond the train
ing data, adding an extra LLM claim verification layer. However, RAG systems can still generate nonsensical outputs due 
to the knowledge base's existing bias or limited relevant resources.

Like chatbots, Pythia integrates with RAG systems 
to detect [hallucinations in LLM responses](https://askpythia.ai/blog/understanding-ai-hallucinations-what-they-are-and-
why-they-matter). Once integrated, it continuously monitors the system performance in real-time using accuracy and task-
specific metrics and highlights the performance in Pythia UI. This enables LLM developers and stakeholders to make immed
iate corrective decisions and improve user experience. 

# Text Summarization

Healthcare text summarization involves co
ndensing large texts, such as medical reports or clinical documents, into shorter summaries while retaining the essentia
l information. Several machine learning and statistical methods assist LLMs in generating summaries of large, complex te
xts.

Accurately processing medical terminology, protecting sensitive information, and preserving information are common
 challenges text summarization systems face. These challenges result in generating inaccurate summaries or losing inform
ation and the meaning of the actual text.

Pythia effortlessly compares summarization tool outputs with its knowledge ba
se and ensures the generated summary doesn’t disregard essential information. It can also use a knowledge graph to ensur
e accurate, relevant, and up-to-date claims.

Pythia’s ability to integrate with LangChain makes it a go-to hallucinatio
n detection tool for LLM developers. This integration allows developers to leverage Pythia's full potential with effortl
ess interoperability. It also ensures RAG developers can access a comprehensive toolkit for developing reliable AI.

# P
ythia’s Ability to Address LLM Contexts

LLM context refers to the information an LLM uses to generate outputs. The cont
exts vary with LLM applications such as chatbots or RAG; understanding them is essential for effectively interpreting ou
tputs. 

# What are the three LLM contexts?

Below are the three LLM contexts and how they differ:

https://preview.redd
.it/m9avh7y6oycd1.png?width=2880&format=png&auto=webp&s=817b9adac13bd40beeb43be768d2b230d301e9aa

# Zero Context

Zero c
ontext refers to user prompts that ask for factual knowledge and don’t include any contextual information. LLM's respons
e to these prompts only relies on user queries and general knowledge of LLM based on its training.

For example, if a us
er asks, “***What is stevia used for?***”, the model answers, “***Stevia is a sweetener and sugar substitute derived fro
m the leaves of the Stevia rebaudiana plant. It is known for its intensely sweet taste without the calories of sugar.***
”

# Noisy Context

Noisy context refers to user prompts where the context includes irrelevant or misleading information
. This can confuse the model and potentially degrade the quality or accuracy of its responses. 

Here’s an example of a 
noisy context prompt, “***I've had a terrible headache for two weeks, and I'm really worried I have a brain tumor. I rea
d online that headaches are a major symptom.***”

# Accurate Context 

Accurate context means the user query is relevant
, clear, and directly related to the task or query. This helps the model generate precise and contextually appropriate r
esponses.

For example, “***I secured 3 As and 2 Bs in my A-level exams. However, I found that the admission requirement
 for University X is 4 As. What are some alternative options for me that are also in high demand and popular?***”

# How
 does Pythia address the three LLM contexts?

A robust LLM should be able to address the three contexts discussed above.
 An AI reliability solution should be able to assess an LLM’s response to accommodate the contexts.

https://preview.red
d.it/gekirvafoycd1.png?width=2544&format=png&auto=webp&s=5104db069d3380e6f69738ea6eb2e7432733574a

# Chatbots as Zero Co
ntext

Chatbots often encounter zero-context queries for quick medical assistance. These queries generally revolve aroun
d factual knowledge, and chatbots use their training databases to generate a response. However, if the user prompt is un
familiar to the chatbot, it can generate nonsensical outputs.

Pythia monitors chatbot responses to detect when the chat
bot fails to generate relevant outputs. Here’s how it works:

1. A user enters a query into the chatbot.
2. The chatbot 
generates an answer.
3. Pythia compares the answer to the chatbot’s knowledge base.
4. Pythia generates an audit report 
based on the comparison.



As a result, Pythia highlights when the chatbot deviates from its knowledge base and creates
 nonsensical outputs. For example, if a user asks, “***What is subrogation in insurance?***” when the chatbot is designe
d to assist insurance clients with customer support, it might generate an irrelevant output. When Pythia compares the ou
tput with the chatbot’s database, it identifies the irrelevant output and flags it. Finally, chatbot developers can debu
g the logic and improve its performance depending on their objectives. 

This allows chatbot developers and companies to
 provide a safe interaction between chatbots and end-users.

Here’s how to integrate Pythia in chatbots for zero-context
 LLM hallucination detection:

1. Develop a chatbot.
2. Install Wisecube and authenticate Pythia.
3. Integrate Pythia in
to your workflow.
4. Detect real-time hallucinations in chatbot responses.



# RAG Systems as Noisy Context

RAG system
s rely on external information sources to generate responses. Therefore, the accuracy of RAG systems is highly dependent
 on the accuracy of external sources. However, Pythia can compare RAG-based systems’ claims through an extensive knowled
ge graph, adding an extra verification layer. 

RAG systems often encounter noisy user prompts, and to ensure the reliab
ility of responses, they must be able to understand user context. Unlike traditional hallucination detection tools, Pyth
ia extracts claims from AI-generated output and knowledge bases as knowledge triplets. Knowledge triplets divide a sente
nce into **<subject, predicate, object>** format, revealing the relationship between subject and object to the RAG syste
m. 

For example, if a user asks, “***Leonard McCoy underwent a Prostate TRUS biopsy last week. He now feels a severe he
adache and a racing heartbeat. Please tell me risk-free solutions to ease his pain.***” to a RAG system, here’s how Pyth
ia dissects this prompt using knowledge triplets: **Subject:** *Leonard McCoy* **Predicate:** *underwent* **Object:** *P
rostate TRUS biopsy*

**Subject:** *Leonard McCoy* **Predicate:** *has* **Object:** *severe headache and raced heartbeat
*

This way, Pythia can interpret user concerns and detect the relevancy of the response through claim comparison. Since
 conventional methods don’t break sentences into this format, they only capture keywords like “***Prostate TRUS biopsy**
*” and generate a general result.

Based on the claim comparison, Pythia categorizes them into “*entailment*”, “*neutral
”*, “*contradiction*”, and “*missing facts*”. Finally, it generates an audit report, highlighting the performance of RAG
 systems so you can take necessary measures to improve its performance. Therefore, if your RAG system generates a genera
l output without understanding the user query, Pythia helps you identify that in real time and deliver a better experien
ce to end-users. 

Here’s [how to integrate Pythia in RAG systems](https://askpythia.ai/blog/a-guide-to-integrating-pyth
ia-api-with-rag-based-systems-using-wisecube-python-sdk) for noisy context LLM hallucination detection:

1. Develop a RA
G system.
2. Install Wisecube and authenticate Pythia.
3. Integrate Pythia into your workflow.
4. Detect hallucinations 
in RAG outputs.



Head over to Pythia docs for a detailed guide on [integrating Pythia in RAG systems](https://askpythi
a.ai/docs/integrate-pythia-with-rag-based-systems).

# Text Summarization as Accurate Context

Text summarization softwa
re usually processes queries providing clear information about the user's needs. This can include a summary of a detaile
d medical report, focusing on the key findings and recommendations. As a response, the software condenses large volumes 
of medical text, such as reports or clinical documents, into shorter summaries that retain the essential information. 


With the rise in AI content detectors, users sometimes demand summarization software to generate a human-like summary. T
his might confuse AI, resulting in missing information in the generated summary. Therefore, accurate processing of medic
al terminology, protecting sensitive information, and preserving the meaning of the original text are the challenges in 
this context.

Here’s how Pythia helps text summarization software to generate accurate summaries:

1. Knowledge triplet
s break down the relationship between phrases and sentences.
2. Claim comparison ensures the summary preserves the origi
nal message.
3. Optional knowledge graph check adds an extra verification layer.



For example, if a user enters a rese
arch paper for summarization, the software generates a summary, and Pythia detects this activity in real time. With the 
help of knowledge triplets, Pythia extracts the following key claims from the medical report: **Subject:** *Eigenvalues 
of the matrix and the stability of the system* **Predicate:** *are* **Object:** *significantly correlated*

**Subject:**
 *Theorem* **Predicate:** *shows* **Object:** *95% confidence interval*

However, the software overlooks the second clai
m in the summary. Pythia will immediately flag it as “*missing facts*”, guiding the developers to look into the underlyi
ng errors.

Similar to the other use cases, integrating Pythia in text summarization software for accurate context LLM h
allucinations:

1. Develop a text summarization software.
2. Install Wisecube and authenticate Pythia.
3. Integrate Pyth
ia into your workflow.
4. Detect hallucinations in AI-generated summaries.



[**Continuous online monitoring and compar
ison**](https://askpythia.ai/blog/why-continuous-monitoring-is-essential-for-maintaining-ai-integrity) of LLM claims and
 references identify when an LLM fails to generate appropriate responses for all LLM contexts. This includes examining t
he relevancy of responses against user queries, assessing the accuracy of claims, and giving insights into the model’s l
imitations.

Pythia UI displays model performance through visualizations and sends SMS alerts whenever an event occurs s
o you can track the LLM performance and your spending.

Start using [**Pythia**](https://askpythia.ai/) today to detect 
real-time hallucinations in your LLMs and improve their performance for reliable outcomes.



*The article was originall
y published on* [Pythia's website.](https://askpythia.ai/blog/practical-applications-of-pythia-in-llm-contexts-chatbots-
rag-systems-and-summarization)
```
---

     
 
all -  [ GenAI for automatic insights from data ](https://www.reddit.com/r/LangChain/comments/1e4xjhu/genai_for_automatic_insights_from_data/) , 2024-07-17-0911
```
Was wondering what tools exist for generating automatic insights from data. For example you feed in a large data set and
 based on the context of the data set a genAI tool is able to tell you insights positive or negative that are useful. Th
ings like 'Revenue has grown by 10% since last month' or 'Customer X usage has dropped since \_\_'. I've found some gene
rative BI tools online but my use case requires something that's more of a dev tool. Also, open to hearing about ideas o
f how to do something like this from scratch.
```
---

     
 
all -  [ creating SEO assistants using LLMs, RAG, GraphRAG/knowledge graph ](https://www.reddit.com/r/TechSEO/comments/1e4swxs/creating_seo_assistants_using_llms_rag/) , 2024-07-17-0911
```
I published yesterday an article on Search Engine Journal about a POC that we developed for creating an SEO assistant.


This assistant uses Retrieval-Augmented Generation (RAG) and GraphRAG to provide access to a SEO knowledge base and SaaS
 tools. More precisely, using external sources (litterature, but also access to SEO tools through APIs), we construct a 
knowledge graph using langchain, llamaindex and a nebula graph datastorage.

I strongly believe that implementing such s
ystems is game-changer for SEO tasks (more productivity, better strategies). I encourage everyone to replicate our POC, 
for which I’ve provided the source code in the article. While adapting it, particularly the knowledge graph aspect via N
ebula, requires effort, it is highly achievable for those that are a little bit familiar with python (and willing to lea
rn a little bit about LLM frameworks).

The SEJ article is here : [https://www.searchenginejournal.com/unlocking-the-pow
er-of-llm-knowledge-graph-introduction/518343/](https://www.searchenginejournal.com/unlocking-the-power-of-llm-knowledge
-graph-introduction/518343/)

And you, do you think - as I do - that this type of assistant is the future of SEO?
```
---

     
 
all -  [ Is There Any Reliable Agentic Tool? ](https://www.reddit.com/r/LangChain/comments/1e4s6xt/is_there_any_reliable_agentic_tool/) , 2024-07-17-0911
```
Hey everyone,

Is there a reliable agentic tool on the market that can operate independently and effectively? So far, I'
ve tried **CrewAI** and have explored **LangGraph**, though I haven't tested it yet. Despite adjusting the max iteration
s, these tools often take a lot of time and work best with OpenAI. However, I want to use them with AWS Bedrock models, 
specifically Mistral or Claude 3.

My primary use case is an internal application where the agent needs to automatically
 decide whether to use a specific agent, perform RAG, or search the web for information. This must be done without compr
omising our confidential company data by sending it to external Search APIs (like Google or DuckDuckGo) and without taki
ng an excessive amount of time to provide answers.

I'd really appreciate any recommendations or advice you can offer.
```
---

     
 
all -  [ Graph RAG + LangChain  ](/r/ArtificialInteligence/comments/1e4rsr6/graph_rag_codes_explained/) , 2024-07-17-0911
```

```
---

     
 
all -  [ GraphRAG+ LangChain  ](https://www.reddit.com/r/Langchaindev/comments/1e4rwpp/graphrag_langchain/) , 2024-07-17-0911
```
GraphRAG is an advanced RAG system that uses Knowledge Graphs instead of Vector DBs improving retrieval. Check out the i
mplementation using GraphQAChain in this video : https://youtu.be/wZHkeon42Aw
```
---

     
 
all -  [ Graph with a for loop ](https://www.reddit.com/r/LangChain/comments/1e4rcha/graph_with_a_for_loop/) , 2024-07-17-0911
```
Hi,

I need some clarifications. In my use case the first step requires an LLM to identify and split different segment o
f the input text / document. Then, for each of the segments I have a linear flow to follow (extract info, call agents, .
..). Finally I have to collect all the outputs.

I am unsure how to achieve the 'for loop' (if possible). Instead of an 
`add_edge`, I'd need an add edges

    workflow.add_node('split', split)
    workflow.add_node('extract', extract)
    w
orkflow.add_node('collect', collect)
    
    workflow.set_entry_point('split')  # after split I get an array of chunks

    
    workflow.add_edges('split', 'extract')  # for each chunk do some custom logic
    workflow.collect_edges('extra
ct', 'collect')  # collect everything
    
```
---

     
 
all -  [ Which vectorstore should I choose? ](https://www.reddit.com/r/LangChain/comments/1e4r8an/which_vectorstore_should_i_choose/) , 2024-07-17-0911
```
In my use case, the most important thing is accuracy, of retrieved documents from them

I'm going to create vectorstore 
of my codebase, so when codes get updated, I have to update those in my  vectorstore periodically (not all codes will ge
t updated)

Keeping these two things in mind, which one should I go with?
```
---

     
 
all -  [ Q&A RAG over tabular data ](https://www.reddit.com/r/LangChain/comments/1e4pqgn/qa_rag_over_tabular_data/) , 2024-07-17-0911
```
Hello dear community,

I am currently familiarising myself with LLM, especially RAG. I have an idea for a Q&A ChatBot an
d would like to learn how to build one.

I would like to use an Excel spreadsheet with three columns as a database. The 
first column is a typical question. The second column contains tags that describe the question. The third column contain
s an answer to the question.

When the user asks a question, a semantic search should first be performed using the first
 and second columns. This will find the top of the most appropriate questions in a cell. The answers to these questions 
in the third column are provided to the LLM as context.

It is important to me that the structured properties of the tab
le are fully exploited. Conventional RAGs return a fixed chunk size, even if it spans cells. However, I only want to ret
urn the cell that is relevant to the question.

My question is, what is the best way to implement this in LangChain? Doe
s it make sense to store the questions and tags as metadata? Can I do a semantic search on the metadata and give the cel
l with the corresponding answer as context to the LLM? With the ulterior motive of returning only the relevant context? 
I have also thought about a self-query retriever. However, this tends to use keywords for filtering, not quite what I am
 looking for. Or am I on the wrong track?

Kind regards
```
---

     
 
all -  [ 🔥 Apify is hiring Backend engineer for an AI/LLM team (Python / TypeScript) ](https://www.reddit.com/r/devjobspro/comments/1e4pnnk/apify_is_hiring_backend_engineer_for_an_aillm/) , 2024-07-17-0911
```
# 🔥 Apify is hiring Backend engineer for an AI/LLM team (Python / TypeScript)

🔖 Python 🔖 Typescript 🔖 AI 🔖 Node.js 🔖 LL
M 🔖 Langchain 🔖 Llamahub

**Details**

- 📥 **Category**: Backend
- 🧙 **Seniority**: Senior level
- 💻 **Working model**: 
Hybrid
- 🏝️ **Employment type**: Full time


- 📍 **Countries**: Czech Republic

**How to Apply:**

[🟡 Apply here](https:
//devjobspro.com/jobs/119-backend-engineer-for-an-ai-llm-team-python-typescript)
```
---

     
 
all -  [ New here - how do I surface and save historical threads of agent actions and conversations in langgr ](https://www.reddit.com/r/LangChain/comments/1e4masy/new_here_how_do_i_surface_and_save_historical/) , 2024-07-17-0911
```
I've set up a dict of main and sub questions(the answer for each feeds into the next) that build on an initial user requ
est. 

I set up a RAG agent workflow on langgraph and need to debug the overall conversational thread by reading through
 what is generated for each question.

I know I can extract the current state from agent_executor.stream()  but how do I
 get every iteration for every question asked? Is the only way to set up a for loop and print/ save the streamed outputs
 each time?  What does the llm get at each turn in the conversation? Shouldn't it be fed the full history?

Also any way
 to summarize and store a thread for downstream agents to absorb? If so any way to surface that summary for user inspect
ion?


Sorry if this is basic- still learning.
```
---

     
 
all -  [ How do I stream my output using ? ](https://www.reddit.com/r/LangChain/comments/1e4lnd5/how_do_i_stream_my_output_using/) , 2024-07-17-0911
```
     if prompt := st.chat_input('Hey, What's up?'):
        if len(pc.list_indexes()) == 0:
            st.error('Please
 upload some files first!')
        else:
            st.session_state.messages.append({'role': 'user', 'content': promp
t})
    
            contextualize_q_system_prompt = (
                'Given a chat history and the latest user questio
n '
                'which might reference context in the chat history, '
                'formulate a standalone questi
on which can be understood '
                'without the chat history. Do NOT answer the question, '
                'j
ust reformulate it if needed and otherwise return it as is.'
            )
            contextualize_q_prompt = ChatProm
ptTemplate.from_messages(
                [
                    ('system', contextualize_q_system_prompt),
             
       MessagesPlaceholder('chat_history'),
                    ('human', '{input}'),
                ]
            )
  
          # chunks ( 5 )
            compression_retriever = reRanker()
            history_aware_retriever = create_his
tory_aware_retriever(
                llm, compression_retriever, contextualize_q_prompt
            )
    
            
system_prompt = (
                'You are an assistant for question-answering tasks. '
                'Use the followi
ng pieces of retrieved context to answer '
                'the question. If you don't know the answer, say that you '
 
               'don't know.'
                '\n\n'
                '{context}'
            )
    
            chatPromp
t = ChatPromptTemplate.from_messages(
                [
                    ('system', system_prompt),
                 
   MessagesPlaceholder('chat_history'),
                    ('human', '{input}'),
                ]
            )
      
      question_answer_chain = create_stuff_documents_chain(llm, chatPrompt)
    
            rag_chain = create_retrieva
l_chain(history_aware_retriever, question_answer_chain)
    
            conversational_rag_chain = RunnableWithMessageH
istory(
                rag_chain,
                get_session_history,
                input_messages_key='input',
    
            history_messages_key='chat_history',
                output_messages_key='answer',
            )
    
      
      response = conversational_rag_chain.invoke(
                input={'input': prompt},
                config={'conf
igurable': {'session_id': 'hdf23me23edewDFSDMS'}}
            )
            print('response:', response['answer'])
     
       st.session_state.messages.append({'role': 'assistant', 'content': response['answer']})
    
            # Display
 updated messages
            for message in st.session_state.messages:
                with st.chat_message(message['ro
le']):
                    st.markdown(message['content'])



How do I output my response as a stream using Langchain's 
create\_retrieval\_chain ?  
Currently , I get my response when all of it is generated ( at once ) , but I want streamin
g feature instead .
```
---

     
 
all -  [ How to deal with multiple states? ](https://www.reddit.com/r/LangChain/comments/1e4l92y/how_to_deal_with_multiple_states/) , 2024-07-17-0911
```
I'm using supervisor graph and various agent graphs. How do pass state within nodes of child graph and parent graph? I c
ouldn't get what [documentation](https://langchain-ai.github.io/langgraph/how-tos/subgraph/) was trying to say.
```
---

     
 
all -  [ Langgraph: best practices for multiple steps graph ](https://www.reddit.com/r/LangChain/comments/1e4l74f/langgraph_best_practices_for_multiple_steps_graph/) , 2024-07-17-0911
```
Hi! As mentioned before, I have built a langgraph with a supervisor agent and two specialised agents. My question is: wh
at are the best practices for having some of these agents working in multiple steps? For example: one of the agents will
 receive the user input and first present to the user what the agent is about to do and after the user confirms it then 
the agent will finish the work.   
My question is: how do I get the same agent to do both of these steps? Should I add s
ystem prompt to the agent on each step? (For example: adding something like 'In this step now you must do X and display 
Y information to the user'). The problem here is that if there are multiple back and forth interactions between agent an
d user then the system prompt will become long and confusing.   
Other way could be saying to agent 'when you are on ste
p 1 you should focus on this, when you are on step 2 you should focus on that'.

Do any of you have experience with this
 kind of scenario?
```
---

     
 
all -  [ GPT-Instagram : Instagram Viral Posts with user own personality ](https://www.reddit.com/r/LangChain/comments/1e4k0is/gptinstagram_instagram_viral_posts_with_user_own/) , 2024-07-17-0911
```
As a weekend project created a Multi Agent AI app in Next.js, LangChain.js & LangGraph.js to simulate a Marketing depart
ment to recommend Instagram Viral Posts with user own personality.

If anyone interested to try or look at code: [https:
//github.com/MODSetter/gpt-instagram](https://github.com/MODSetter/gpt-instagram)

https://reddit.com/link/1e4k0is/video
/ig7wjanujucd1/player

  

```
---

     
 
all -  [ Developer looking for exciting opportunities ](https://www.reddit.com/r/Entrepreneur/comments/1e4jsp6/developer_looking_for_exciting_opportunities/) , 2024-07-17-0911
```
I'm basically a react native developer with 1 year of experience in app and web development. Altho I'm doing my average 
job right now, I'm dying to work on something real exciting that will help me learn quite alot of things and explore. I 
go around and thought what be better place to explore than that community of some highly ambious entrepreneurs.

Even on
 this normal job I try to explore various fields and takes up work around, but I'm looking for some real excieting probl
ems. I know things like nodejs, go, kotlin, react native, a bit of langchains, devops with docker, aws, etc. Like learni
ng new stuffs 😊

Majorly looking for some early stage startups where I can contribute and learn alot.  
Hope you guys ca
n help 😅
```
---

     
 
all -  [ An open source hub for top python functions that could be used as custom tools for AI projects. ](https://www.reddit.com/r/LocalLLaMA/comments/1e4jb76/an_open_source_hub_for_top_python_functions_that/) , 2024-07-17-0911
```
Hey LocalLLamas,

As I was working daily on my AI projects, I have collected few automation function in python that I fi
nd helpful. An idea came to mind, that if I could make an open source project that gather all of these python hacks into
 one, and crowdsource from others. I believe in the long term will be great for the whole  ecosystem.

So here it is, th
e very first foundation of the project. Current I gathered the top 15 functions, with all source code available to try.


https://reddit.com/link/1e4jb76/video/98n0hsut7vcd1/player

Hope it may be helpful for building your local langchain, l
anggraph app.

🔗 Features:

**Background Remover**: Automatically removes backgrounds from images.

* **QR Code Creator*
*: Easily generates QR codes from URLs.
* **Fake Data Generator**: Creates realistic dummy data for testing.
* **URL Sho
rtener**: Simplifies long URLs into concise ones.
* **YouTube Downloader**: Downloads YouTube videos or audio files.
* *
*Bulk Email Sender**: Sends emails in bulk with ease.
* **Image Scraper**: Fetches and displays images from the web.
* *
*Audiobook Maker**: Converts PDFs into audiobooks.
* **Code Analyzer**: Evaluates Python code using Pylint and Flake8.
*
 **Resource Monitor**: Keeps an eye on your system's resources.
* **Clipboard Tracker**: Logs all texts copied to your c
lipboard.
* **Spell Checker**: Corrects spelling and grammar errors.
* **Link Verifier**: Checks the connectivity of mul
tiple URLs.
* **News Reader**: Reads out loud trending news headlines.
* **Article Summarizer**: Condenses lengthy artic
les into summaries.
*  … and many more! 

💻 Try it out at: [Link](https://autopilot.streamlit.app/)

The Repo: [GitHub -
 Ai-Quill/automated: automated python scripts](https://github.com/Ai-Quill/automated.git)

🙏 C**ontribute: **I would lov
e community contributions! Fork the repo, suggest new scripts, or improve existing ones. 📚 More Info: Check out our GitH
ub repo for detailed instructions, features, and more!

**💬 Feedback: **would love to hear how you are using these pytho
n functions in your local llm tools.
```
---

     
 
all -  [ LangGraph  ](https://www.reddit.com/r/AIFromChina/comments/1e4ir2v/langgraph/) , 2024-07-17-0911
```
LangGraph aims to overcome the major limitation of traditional LangChain chains - that they lack looping at runtime. Thi
s problem can be easily addressed by introducing a graph structure, as graphs can easily introduce loops into chains, wh
ich are essentially directed acyclic graphs (DAGs).

Furthermore, graph tools have shown their power in organizing knowl
edge bases for retrieval-augmented generation (RAG) scenarios. Specifically, they can enhance the 'retrieval' stage to e
nable more meaningful context retrieval, ultimately improving the accuracy of generated responses. To achieve this, our 
strategy is to store the knowledge base in a graph-based database (e.g., Neo4j), leveraging the semantic capabilities of
 LLMs to correctly identify and map entities and relationships.

To realize this goal, LangChain has developed a powerfu
l library called LLMGraphTransformer, which aims to transform unstructured text data into a graph-based representation.


Welcome to follow: [https://aidisruption.substack.com/](https://aidisruption.substack.com/)
```
---

     
 
all -  [ Langgraph Human in the loop in Production ](https://www.reddit.com/r/LangChain/comments/1e4hays/langgraph_human_in_the_loop_in_production/) , 2024-07-17-0911
```
Are there anyone who has successfully done langgraph with human in the loop in production? How does that work? 
```
---

     
 
all -  [ How should I set up my multimodal chatbot? ](https://www.reddit.com/r/LangChain/comments/1e4gvl1/how_should_i_set_up_my_multimodal_chatbot/) , 2024-07-17-0911
```
As of now I have a chatbot (OpenAI embeddings & chat model) that can take in text/pdf files and answer questions about t
hem using embeddings and a vectorDB. I was wondering if it would be plausible to embed an image into the vectorDB, and u
se a multi modal LLM to be able to answer questions about said picture. I've been looking at other approaches (generatin
g text summaries of image and embedding that/sending the image straight to a multimodal LLM with the prompt) but I like 
the idea of embedding images into my vectorDB, and I don't really know the pros/cons between these methods. Any help is 
appreciated !
```
---

     
 
all -  [ How do Graph RAG search for relevant nodes? ](https://www.reddit.com/r/LangChain/comments/1e4c1j5/how_do_graph_rag_search_for_relevant_nodes/) , 2024-07-17-0911
```
Hi everyone, I have been reading around about Graph RAG lately. I don’t quite understand how the retriever searches for 
“relevant entities”? I have thought of exact full text search, but they would not be quite effective when the entities c
an be (and will be!) ambiguous ( e.g. two people with the same name, or same people with different names, etc.). Or mayb
e semantic search is utilized here? If so, I don’t think it would be efficient for a large graph with many entities.
Rea
lly appreciate your help! 
```
---

     
 
all -  [ MarkdownTextSplitter ](https://www.reddit.com/r/LangChain/comments/1e47vwu/markdowntextsplitter/) , 2024-07-17-0911
```
This LangChain tool is a little naive- it is just a text splitter with charLength and overlap size. Does anyone know of 
a compatible splitter that can breakdown a Markdown based on header sections and other elements (eg, lists, code, tables
)??
```
---

     
 
all -  [ Default search method in ChromDB while performing similarity_search() ](https://www.reddit.com/r/LangChain/comments/1e4059d/default_search_method_in_chromdb_while_performing/) , 2024-07-17-0911
```
What is the default search metric while using:

    similarity_search()

Also, can I explicitly give my own metrics, wha
t are the other metrics available for ChromaDB?
```
---

     
 
all -  [ [HELP/ IDEAS NEEDED] I have a llama 2 chat model working locally i want the model to take a CSV file ](https://www.reddit.com/r/LangChain/comments/1e3yv1o/help_ideas_needed_i_have_a_llama_2_chat_model/) , 2024-07-17-0911
```
So I have a llama 2 7b chat model on my machine running locally, what I want to do is that the model takes a CSV file as
 input the file can contain anything ranging from text, numbers, shareholder info, etc., process the file and gives out 
text in a particular paragraph form that makes sense, I tried asking multiple GPT's but I couldn't get anywhere 

So if 
any of you esteemed AI engineers could help a frustrated college student it would mean a lot 
```
---

     
 
all -  [ Biggest RAG Hurdles for Beginners? ](https://www.reddit.com/r/LangChain/comments/1e3ygh6/biggest_rag_hurdles_for_beginners/) , 2024-07-17-0911
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

     
 
all -  [ AzureChatOpenAI not working ](https://www.reddit.com/r/LangChain/comments/1e3w7l9/azurechatopenai_not_working/) , 2024-07-17-0911
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

     
 
all -  [ Cost Prediction of nvidia nim nv-embed-v1 ](https://www.reddit.com/r/LangChain/comments/1e3w5lq/cost_prediction_of_nvidia_nim_nvembedv1/) , 2024-07-17-0911
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

     
 
all -  [ Integration of RAGAS Evaluation with Langserve ](https://www.reddit.com/r/LangChain/comments/1e3u619/integration_of_ragas_evaluation_with_langserve/) , 2024-07-17-0911
```
Hey everyone, I am looking to integrate ragas scoring for every api call made to a langserve endpoint. Does anyone have 
any references or thoughts on how one can do this. I am planning to further log these metrics into langsmith to track th
e performance over time
```
---

     
 
all -  [ How to use LangChain with a custom endpoint? ](https://www.reddit.com/r/LangChain/comments/1e3rl5d/how_to_use_langchain_with_a_custom_endpoint/) , 2024-07-17-0911
```
Hello! So I have an endpoint on which my trained model is deployed. How can I use this with LangChain? endpoint\_url = '
---------/chat'

Can someone please give me the wrapper code, I am so confused because I already have this model and I d
ont know how to use this with LangChain. I want to utilize the ConversationBufferMemory method to retain context.

For b
ackground, I am using this endpoint for a Webex chatbot.
```
---

     
 
all -  [ [Experiment] Good chunking will lead you to the better RAG performance ](https://www.reddit.com/r/LangChain/comments/1e3q2lb/experiment_good_chunking_will_lead_you_to_the/) , 2024-07-17-0911
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

     
 
all -  [ Chroma db , results size ](https://www.reddit.com/r/LangChain/comments/1e3q18k/chroma_db_results_size/) , 2024-07-17-0911
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

     
 
all -  [ Finetuning ColBERT reranker ](https://www.reddit.com/r/LangChain/comments/1e3plel/finetuning_colbert_reranker/) , 2024-07-17-0911
```
Hello. Has anybody tried finetuning ColBERT models? Did it help you? How much data do you need to finetune it well? 
```
---

     
 
all -  [ ReAct issues ](https://www.reddit.com/r/LangChain/comments/1e3p6pf/react_issues/) , 2024-07-17-0911
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

     
 
all -  [ How important is CODING?? ](https://www.reddit.com/r/learnmachinelearning/comments/1e3oho2/how_important_is_coding/) , 2024-07-17-0911
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

     
 
MachineLearning -  [ [D] Is Anyone Else Setting Up Real-Time Django Workers for their AI Application? What's the best way ](https://www.reddit.com/r/MachineLearning/comments/1e0qens/d_is_anyone_else_setting_up_realtime_django/) , 2024-07-17-0911
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

     
 
MachineLearning -  [ [P] Real Time AI Workers Web Application ](https://www.reddit.com/r/MachineLearning/comments/1dzryk9/p_real_time_ai_workers_web_application/) , 2024-07-17-0911
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

     
 
deeplearning -  [ Llama 3 not running on GPU ](https://www.reddit.com/r/deeplearning/comments/1dptxsr/llama_3_not_running_on_gpu/) , 2024-07-17-0911
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

     
 
deeplearning -  [ What is ReAct Prompting? the most important piece in agentic frameworks ](https://www.reddit.com/gallery/1djk4nk) , 2024-07-17-0911
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

     
