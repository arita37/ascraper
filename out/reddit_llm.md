 
all -  [ Ways to summarize with RAG ](https://www.reddit.com/r/LangChain/comments/1hm9cvv/ways_to_summarize_with_rag/) , 2024-12-26-0913
```
“RAG is not designed to summarize entire book” - you may wanted to write this comment which is quite ok, I dove into ful
l internet resources, trying to find most sophisticated method to summarize user uploaded file using rag, imagine simple
 scenario, user uploads pdf book, and later asks question: “who are main characters in this book?”, what is approaches y
ou have used to get near good results? 
```
---

     
 
all -  [ What do you think of Groq? ](https://www.reddit.com/r/LangChain/comments/1hm7i83/what_do_you_think_of_groq/) , 2024-12-26-0913
```
What are your experiences with Groq? What are its pros, cons, and limitations? Thanks.
```
---

     
 
all -  [ prompt format question ](https://www.reddit.com/r/LangChain/comments/1hm7how/prompt_format_question/) , 2024-12-26-0913
```
I found the following code from a YouTube tutorial video. My question is regarding the structure of the prompt. In parti
cular, how does one know that he/she has to specify two MessagePlaceHolders()'s? This is a tutorial about getting data f
rom yfinance.

    from langchain.agents import AgentExecutor, create_tool_calling_agent
    from langchain_groq import 
ChatGroq
    from langchain.prompts import ChatPromptTemplate
    from langchain_core.prompts import MessagesPlaceholder

    
    tools = [
             company_information,
             last_dividend_and_earnings_date,
             stock_s
plits_history,
             summary_of_mutual_fund_holders,
             summary_of_institutional_holders, 
            
 stock_grade_updrages_downgrades,
             stock_news
    ]
    
    prompt = ChatPromptTemplate.from_messages(
    
    [
            (
                'system',
                'You are a helpful assistant. Try to answer user query usi
ng available tools.',
            ),
            MessagesPlaceholder(variable_name='messages'),
            MessagesPlac
eholder(variable_name='agent_scratchpad'),
        ]
    )
    
    llama3 = ChatGroq(api_key=groq_api_key, model='llama
3-8b-8192', temperature=0)
    
    finance_agent = create_tool_calling_agent(llama3, tools, prompt)
    
    finance_ag
ent_executor = AgentExecutor(agent=finance_agent, tools=tools, verbose=True)
    

  

```
---

     
 
all -  [ Open AI Realtime with langchain powered RAG POC ](/r/LangChain/comments/1hm1e1m/open_ai_realtime_with_langchain_powered_rag_poc/) , 2024-12-26-0913
```

```
---

     
 
all -  [ Does anyone know of any github projects that use ChatHuggingFace with tool-use? ](https://www.reddit.com/r/huggingface/comments/1hm2k7v/does_anyone_know_of_any_github_projects_that_use/) , 2024-12-26-0913
```
It'd be a load of help. I've tried everything on the Langchain documentation (for a Langgraph project i've been trying t
o build), but it simply does not work. Tool-use creates the strangest of issues. If there's anything that's built alread
y, it'd be a lot easier to work.
```
---

     
 
all -  [ Open AI Realtime with langchain powered RAG POC ](https://www.reddit.com/r/LangChain/comments/1hm1e1m/open_ai_realtime_with_langchain_powered_rag_poc/) , 2024-12-26-0913
```
Hi Everyone, we are proud to share the release of our open source voice-to-voice Proof of concept where you can upload y
our documents and ask questions related to them.

You can upload your documents and interact with them through our dashb
oard.📊.

Based on OpenAI Realtime AND langchain

Powered by [Supabase](https://www.linkedin.com/company/supabase/)  \+ [
Qdrant](https://www.linkedin.com/company/qdrant/)  \+ [NextJs](https://www.linkedin.com/company/nextjs/) 

Github repo: 
[https://github.com/actualize-ae/voice-chat-pdf](https://github.com/actualize-ae/voice-chat-pdf)

If you like the concep
t or have feedback please feel free to contribute a star and share feedback :) 

[Demo Video](https://reddit.com/link/1h
m1e1m/video/xlg0qhc45g6e1/player)

Architecture Diagram:

https://preview.redd.it/g29cnxdk5g6e1.png?width=2050&format=pn
g&auto=webp&s=3abdc714f810565c163d7aba3d5c4cebcf666b55


```
---

     
 
all -  [ Parsing Error and no green lines highlight ](https://www.reddit.com/r/n8n/comments/1hm0pdr/parsing_error_and_no_green_lines_highlight/) , 2024-12-26-0913
```
Hello everyone, I'm reaching out for some help with two issues I'm experiencing with my AI models. As a novice user, ple
ase bear with me if my questions seem silly!

**Issue 1: Parsing Error with Llama 3.2**

I've noticed that when I use th
e Llama 3.2 model, I'm getting parsing errors. However, this issue doesn't seem to occur with the QWEN 2.5 coder. Can an
yone help me understand why this is happening?

**Issue 2: Colored Lines not Displaying**

I've noticed that the dotted 
lines connecting these models are not displaying in green color even after execution. Is there a setting or configuratio
n issue here? Any guidance on how to resolve this would be greatly appreciated.

Thank you in advance for your help and 
patience!

https://preview.redd.it/83vykiyqxz8e1.png?width=1738&format=png&auto=webp&s=2d034e3ee8bb6b2cdbc2bac787b7398e1
a2a86fe


```
---

     
 
all -  [ Is it possible to create a multi agent system without any framework? ](https://www.reddit.com/r/LangChain/comments/1hlz3rb/is_it_possible_to_create_a_multi_agent_system/) , 2024-12-26-0913
```
The question is self explanatory.
```
---

     
 
all -  [ Preventing Assistant from Sending Messages Before Tool Calls in LangGraph ](https://www.reddit.com/r/LangChain/comments/1hly6u7/preventing_assistant_from_sending_messages_before/) , 2024-12-26-0913
```
Hey everyone,

I'm building a chatbot using LangGraph with the gpt-4o model and integrating it with several tools to int
eract with our internal APIs. The chatbot is designed to respond with a defined structured format to be rendered in fron
t end later.

I'm encountering an issue where the model sometimes streams a preliminary/opening message to the user *bef
ore* executing a tool call. This leads to multiple messages being sent for a single user query, which our current front-
end cannot handle.

For example:

* User: Detail for product A
* AI: let me search for you ... *<- this is the prelimina
ry/opening message I wanted to prevent*
* (AI executing tool)
* AI: Here is the detail for product A

**What I've Tried:
**

* I've tried adding instructions to the assistant prompt to refrain from sending any preliminary messages before too
l execution.
* I also added instruction to emphasize direct tool execution in the tool descriptions.

However, both of t
hese approaches not working as expected.

I want to ask are there any method in langgraph to prevent this? Thanks
```
---

     
 
all -  [ What's not working? ](https://www.reddit.com/r/LangChain/comments/1hlwx2a/whats_not_working/) , 2024-12-26-0913
```
Why is RAG not working well for you currently?
```
---

     
 
all -  [ Resume analysis for MLE roles (0-2 year experience) ](https://www.reddit.com/r/learnmachinelearning/comments/1hlv9bw/resume_analysis_for_mle_roles_02_year_experience/) , 2024-12-26-0913
```
Hello everyone, I am a student at university in the US about to graduate. I have a decent offer for SWE and I trying to 
interview for MLE roles. Would really appreciate advice/suggestions on resume. Please be as unfiltered and honest as pos
sible. I want to understand what my resume is lacking. TIA.

https://preview.redd.it/pkma7dlsux8e1.png?width=1238&format
=png&auto=webp&s=0062df3c4a7e2532a976bfe6f02bab47b2a42ee7


```
---

     
 
all -  [ LangChain In Your Pocket (Generative AI Book, Packt published) : Free Audiobook ](https://www.reddit.com/r/datascience/comments/1hlup8w/langchain_in_your_pocket_generative_ai_book_packt/) , 2024-12-26-0913
```
Hi everyone,

It's been almost a year now since I published my debut book

>“LangChain In Your Pocket : Beginner’s Guide
 to Building Generative AI Applications using LLMs”

https://preview.redd.it/lgtj9570ix8e1.png?width=934&format=png&auto
=webp&s=8b2a0e87914072d5125551adf830b731afcb293e

And what a journey it has been. The book saw major milestones becoming
 a **National and even International Bestseller in the AI category**. So to celebrate its success, I’ve released the Fre
e Audiobook version of “LangChain In Your Pocket” making it accessible to all users free of cost. I hope this is useful.
 The book is currently rated at 4.6 on amazon India and 4.2 on amazon com, making it amongst the top-rated books on Lang
Chain and is published by Packt as well

More details : [https://medium.com/data-science-in-your-pocket/langchain-in-you
r-pocket-free-audiobook-dad1d1704775](https://medium.com/data-science-in-your-pocket/langchain-in-your-pocket-free-audio
book-dad1d1704775)

# Table of Contents

* Introduction
* Hello World
* Different LangChain Modules
* Models & Prompts
*
 Chains
* Agents
* OutputParsers & Memory
* Callbacks
* RAG Framework & Vector Databases
* LangChain for NLP problems
* 
Handling LLM Hallucinations
* Evaluating LLMs
* Advanced Prompt Engineering
* Autonomous AI agents
* LangSmith & LangSer
ve
* Additional Features

**Edit :** Unable to post direct link (maybe Reddit Guidelines), hence posted medium post with
 the link.
```
---

     
 
all -  [ Free Audiobook : LangChain In Your Pocket (Packt published) ](https://www.reddit.com/r/OpenAI/comments/1hluk3m/free_audiobook_langchain_in_your_pocket_packt/) , 2024-12-26-0913
```
Hi everyone,

It's been almost a year now since I published my debut book

>“LangChain In Your Pocket : Beginner’s Guide
 to Building Generative AI Applications using LLMs”

https://preview.redd.it/lgtj9570ix8e1.png?width=934&format=png&auto
=webp&s=8b2a0e87914072d5125551adf830b731afcb293e

And what a journey it has been. The book saw major milestones becoming
 a **National and even International Bestseller in the AI category**. So to celebrate its success, I’ve released the Fre
e Audiobook version of “LangChain In Your Pocket” making it accessible to all users free of cost. I hope this is useful.
 The book is currently rated at 4.6 on amazon India and 4.2 on amazon com, making it amongst the top-rated books on Lang
Chain and is published by Packt.

More details : [https://medium.com/data-science-in-your-pocket/langchain-in-your-pocke
t-free-audiobook-dad1d1704775](https://medium.com/data-science-in-your-pocket/langchain-in-your-pocket-free-audiobook-da
d1d1704775)

# Table of Contents

* Introduction
* Hello World
* Different LangChain Modules
* Models & Prompts
* Chains

* Agents
* OutputParsers & Memory
* Callbacks
* RAG Framework & Vector Databases
* LangChain for NLP problems
* Handlin
g LLM Hallucinations
* Evaluating LLMs
* Advanced Prompt Engineering
* Autonomous AI agents
* LangSmith & LangServe
* Ad
ditional Features

**Edit :** Unable to post direct link (maybe Reddit Guidelines), hence posted medium post with the li
nk.
```
---

     
 
all -  [ LangChain In Your Pocket : Free Audiobook ](https://www.reddit.com/r/learnmachinelearning/comments/1hlui47/langchain_in_your_pocket_free_audiobook/) , 2024-12-26-0913
```
Hi everyone,

It's been almost a year now since I published my debut book

>“LangChain In Your Pocket : Beginner’s Guide
 to Building Generative AI Applications using LLMs” (Packt Published)

https://preview.redd.it/lgtj9570ix8e1.png?width=9
34&format=png&auto=webp&s=8b2a0e87914072d5125551adf830b731afcb293e

And what a journey it has been. The book saw major m
ilestones becoming a **National and even International Bestseller in the AI category**. So to celebrate its success, I’v
e released the Free Audiobook version of “LangChain In Your Pocket” making it accessible to all users free of cost. I ho
pe this is useful. The book is currently rated at 4.6 on amazon India and 4.2 on amazon com, making it amongst the top-r
ated books on LangChain.

More details : [https://medium.com/data-science-in-your-pocket/langchain-in-your-pocket-free-a
udiobook-dad1d1704775](https://medium.com/data-science-in-your-pocket/langchain-in-your-pocket-free-audiobook-dad1d17047
75)

# Table of Contents

* Introduction
* Hello World
* Different LangChain Modules
* Models & Prompts
* Chains
* Agent
s
* OutputParsers & Memory
* Callbacks
* RAG Framework & Vector Databases
* LangChain for NLP problems
* Handling LLM Ha
llucinations
* Evaluating LLMs
* Advanced Prompt Engineering
* Autonomous AI agents
* LangSmith & LangServe
* Additional
 Features

**Edit :** Unable to post direct link (maybe Reddit Guidelines), hence posted medium post with the link.
```
---

     
 
all -  [ Free Audiobook : LangChain in your Pocket ](https://www.reddit.com/r/Rag/comments/1hluhi8/free_audiobook_langchain_in_your_pocket/) , 2024-12-26-0913
```
Hi everyone,

It's been almost a year now since I published my debut book

>“LangChain In Your Pocket : Beginner’s Guide
 to Building Generative AI Applications using LLMs”

https://preview.redd.it/lgtj9570ix8e1.png?width=934&format=png&auto
=webp&s=8b2a0e87914072d5125551adf830b731afcb293e

And what a journey it has been. The book saw major milestones becoming
 a **National and even International Bestseller in the AI category**. So to celebrate its success, I’ve released the Fre
e Audiobook version of “LangChain In Your Pocket” making it accessible to all users free of cost. I hope this is useful.
 The book is currently rated at 4.6 on amazon India and 4.2 on amazon com, making it amongst the top-rated books on Lang
Chain.

More details : [https://medium.com/data-science-in-your-pocket/langchain-in-your-pocket-free-audiobook-dad1d1704
775](https://medium.com/data-science-in-your-pocket/langchain-in-your-pocket-free-audiobook-dad1d1704775)

# Table of Co
ntents

* Introduction
* Hello World
* Different LangChain Modules
* Models & Prompts
* Chains
* Agents
* OutputParsers 
& Memory
* Callbacks
* RAG Framework & Vector Databases
* LangChain for NLP problems
* Handling LLM Hallucinations
* Eva
luating LLMs
* Advanced Prompt Engineering
* Autonomous AI agents
* LangSmith & LangServe
* Additional Features

**Edit 
:** Unable to post direct link (maybe Reddit Guidelines), hence posted medium post with the link.
```
---

     
 
all -  [ LangChain In Your Pocket free Audiobook ](https://www.reddit.com/r/LangChain/comments/1hlug9s/langchain_in_your_pocket_free_audiobook/) , 2024-12-26-0913
```
Hi everyone,

It's been almost a year now since I published my debut book

>“LangChain In Your Pocket : Beginner’s Guide
 to Building Generative AI Applications using LLMs” (Packt published)

https://preview.redd.it/lgtj9570ix8e1.png?width=9
34&format=png&auto=webp&s=8b2a0e87914072d5125551adf830b731afcb293e

And what a journey it has been. The book saw major m
ilestones becoming a **National and even International Bestseller in the AI category**. So to celebrate its success, I’v
e released the Free Audiobook version of “LangChain In Your Pocket” making it accessible to all users free of cost. I ho
pe this is useful. The book is currently rated at 4.6 on amazon India and 4.2 on amazon com, making it amongst the top-r
ated books on LangChain.

More details : [https://medium.com/data-science-in-your-pocket/langchain-in-your-pocket-free-a
udiobook-dad1d1704775](https://medium.com/data-science-in-your-pocket/langchain-in-your-pocket-free-audiobook-dad1d17047
75)

# Table of Contents

* Introduction
* Hello World
* Different LangChain Modules
* Models & Prompts
* Chains
* Agent
s
* OutputParsers & Memory
* Callbacks
* RAG Framework & Vector Databases
* LangChain for NLP problems
* Handling LLM Ha
llucinations
* Evaluating LLMs
* Advanced Prompt Engineering
* Autonomous AI agents
* LangSmith & LangServe
* Additional
 Features

**Edit :** Unable to post direct link (maybe Reddit Guidelines), hence posted medium post with the link.
```
---

     
 
all -  [ Langachain Agent & Tool ](https://www.reddit.com/r/LangChain/comments/1hlt3c1/langachain_agent_tool/) , 2024-12-26-0913
```
I have a context like

```

issuer is  somebank. Rate is 1.0% year 1; 2.0% year 2 onwards. Maturity date is 20/01/2023. 
Coupon frequency is semi-annual long first coupon. Trade date is 20/11/2015. calendar is London, Newyork. Counterparty i
s some bank. Etc…

```

From here i need to get Rate; Maturity Date; Trade date and construct a table. So in langchain w
hich agent and tool will be helpful to construct the table. Or if i have descriptions correctly which langchain agent an
d tool will do correctly?
```
---

     
 
all -  [ Build AI Agents with SwarmEx (GitHub) ](https://www.reddit.com/r/elixir/comments/1hlhu1n/build_ai_agents_with_swarmex_github/) , 2024-12-26-0913
```
[https://github.com/nrrso/swarm\_ex](https://github.com/nrrso/swarm_ex)  
Found this really cool library while searching
 for alternatives to Langchain Elixir. While Langchain (Elixir) is cool, I felt like an abstraction layer of doing thing
s in parallel would be nice and found this.

The thing about Elixir is the actor model/message passing lends itself quit
e naturally to agents. I have also worked with Langraph on Python land and it is not as elegant, especially having to re
ason about your code 6 months from now.
```
---

     
 
all -  [ How to add a prompt with instructions to my code ?  ](https://www.reddit.com/r/LangChain/comments/1hlhqxv/how_to_add_a_prompt_with_instructions_to_my_code/) , 2024-12-26-0913
```
    how to enable the ai here to follow instructions from the prompt : 
    here is my code : 
    # Helper Functions
  
  def load_documents(directory: str):
        '''
        Load documents from the specified directory.
        '''
     
   loader = DirectoryLoader(directory, glob='./*.pdf')
        documents = loader.load()
        return documents
    
 
   
    def split_documents(documents, chunk_size=2000, chunk_overlap=500):
        '''
        Split documents into sma
ller chunks for vectorization.
        '''
        text_splitter = CharacterTextSplitter(
            chunk_size=chunk_s
ize,
            chunk_overlap=chunk_overlap
        )
        return text_splitter.split_documents(documents)
    
    

    def setup_vectorstore(documents, embeddings, persist_directory: str):
        '''
        Create or load a FAISS ve
ctorstore.
        '''
        if not os.path.exists(persist_directory):
            os.makedirs(persist_directory)
    
    vectorstore = FAISS.from_documents(
            documents=documents,
            embedding=embeddings
        )
    
    return vectorstore
    
    
    def create_chat_chain(vectorstore):
        '''
        Create a conversational ret
rieval chain using Ollama with Llama 3.2.
        '''
        llm = Ollama(model='llama3.2:latest')
        retriever = 
vectorstore.as_retriever()
        memory = ConversationBufferMemory(
            #llm=llm,
            memory_key='chat
_history',
            return_messages=True,
            output_key='answer'  # Explicitly specify the output key
      
  )
        chain = ConversationalRetrievalChain.from_llm(
            llm=llm,
            retriever=retriever,
       
     chain_type='stuff',
            memory=memory,
            verbose=True,
            return_source_documents=True  
# Allows retrieving source documents
        )
        return chain
    
    
    # Main Streamlit Application
    def m
ain():
        # Page Configuration
        st.set_page_config(
            page_title='Multi Doc Chat',
            pag
e_icon='📚',
            layout='centered'
        )
    
        st.title('📚 Multi Documents Chatbot')
    
        # In
itialize embeddings and vectorstore
        embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-Min
iLM-L6-v2')
        persist_directory = 'vector_db_dir'
    
        if 'vectorstore' not in st.session_state:
         
   # Specify your directory path here
            documents = load_documents(path of file)
            text_chunks = spl
it_documents(documents)
            st.session_state.vectorstore = setup_vectorstore(text_chunks, embeddings, persist_di
rectory)
    
        if 'chat_chain' not in st.session_state:
            st.session_state.chat_chain = create_chat_cha
in(st.session_state.vectorstore)
    
        if 'chat_history' not in st.session_state:
            st.session_state.ch
at_history = []
    
        # Display chat history
        for message in st.session_state.chat_history:
            wi
th st.chat_message(message['role']):
                st.markdown(message['content'])
    
        # Input and response h
andling
        user_input = st.chat_input('Ask AI...')
        if user_input:
            st.session_state.chat_history
.append({'role': 'user', 'content': user_input})
    
            with st.chat_message('user'):
                st.markd
own(user_input)
    
            with st.chat_message('assistant'):
                response = st.session_state.chat_cha
in({'question': user_input})
                assistant_response = response['answer']
                st.markdown(assista
nt_response)
                st.session_state.chat_history.append({'role': 'assistant', 'content': assistant_response})

    
    
    # Run the application
    if __name__ == '__main__':
        main()
```
---

     
 
all -  [ Seeking Guidance for Building a RAG-Powered Chatbot with LangChain and Llama ](https://www.reddit.com/r/Rag/comments/1hlg5jp/seeking_guidance_for_building_a_ragpowered/) , 2024-12-26-0913
```
I’m developing a RAG system for the company where I’m doing my internship. The goal is to use it as a chatbot for the us
ers of the enterprise platform, answering questions based on manuals and documentation. This will help save the IT depar
tment’s time by avoiding repetitive queries.

Although I’ve read a lot about RAG, I feel like I’ve fallen into an endles
s pit of documentation, so I’m seeking some guidance.

So far, I’m considering using LangChain, PostgreSQL with Pgvector
 as the vector database, and Llama as the language model. Do you think this setup is viable?

I’d really appreciate any 
advice or recommendations you could share.
```
---

     
 
all -  [ Arch (0.1.7) 🚀 - accurate multi-turn intent detection especially for follow-up questions in RAG. Plu ](https://i.redd.it/se5dhprlet8e1.jpeg) , 2024-12-26-0913
```
https://github.com/katanemo/archgw - an intelligent gateway for agents. Engineered with (fast) LLMs for the secure handl
ing, rich observability, and seamless integration of prompts with functions/APIs - all outside business logic.

Disclaim
er: I am work here and this was a big release that simplifies a lot for developers. Ask me anything
```
---

     
 
all -  [ Multi AI Agent framework for Time series, Text and visual data ](https://www.reddit.com/r/LangChain/comments/1hlfq0k/multi_ai_agent_framework_for_time_series_text_and/) , 2024-12-26-0913
```
I am trying to create a multi-AI agent which retrieves time series, text and visual data what are the frameworks that an
yone can suggest me to build this one, I have seen langgraph, crewAI and autogen being the most popular out there. But a
re they really good for multi model multi-AI agent systems?
```
---

     
 
all -  [ 'Fetching 30 files' during start - why? ](https://www.reddit.com/r/OpenWebUI/comments/1hlfidk/fetching_30_files_during_start_why/) , 2024-12-26-0913
```
Whenever I start Open WebUI (in a docker container), it fetches some files from somewhere. Here's a piece of log:

`open
-webui  | WARNI [langchain_community.utils.user_agent] USER_AGENT environment variable not set, consider setting it to i
dentify your requests.`

`Fetching 30 files: 100%|██████████| 30/30 [00:00<00:00, 385978.90it/s]`

`open-webui  | INFO: 
    Started server process [1]`

What are those files and how to disable that?

I'd like to run OpenWebUI with Ollama wi
th no internet connection, but it gets stuck when it cannot fetch that stuff (tested by disabling network).
```
---

     
 
all -  [ Diving into the Hype and Reality of AI Agent Frameworks - What Are People Saying? ](https://i.redd.it/35jmcq7f9t8e1.jpeg) , 2024-12-26-0913
```


I've been doing a deep dive into the burgeoning world of AI agent frameworks like Langchain, AutoGPT, and others, and 
wanted to share a summary of the user sentiment I've been picking up across the web, particularly here on Reddit and oth
er tech forums. It's a fascinating space, and the conversations are buzzing!

The Overall Vibe: A Mix of Excitement and 
Cautious Optimism

Generally, there's a strong sense of excitement and anticipation surrounding these frameworks. People
 are clearly intrigued by the potential of building truly autonomous AI agents that can reason, plan, and act in the rea
l world. The idea of AI handling complex tasks with minimal human intervention is definitely captivating.

The Good (Wha
t People Are Hyped About):

Automation Potential: This is the biggest draw. Users are excited about the possibilities of
 automating repetitive tasks, complex workflows, and even creative processes. Think coding assistants that go beyond sim
ple completions, personal research assistants, or even automated business processes.

Democratization of AI: Frameworks 
like Langchain, with their relatively accessible APIs and abstractions, are seen as tools that can empower developers (a
nd even technically savvy non-developers) to build sophisticated AI applications without needing a PhD in machine learni
ng.

Rapid Prototyping and Experimentation: These frameworks make it easier to quickly build and test out different agen
t architectures and workflows. The modular nature and pre-built components are a big plus for rapid iteration.

Novel Ap
plication Ideas: Discussions are brimming with creative ideas for how these agents could be used. From building personal
ized learning platforms to creating intelligent smart home ecosystems, the possibilities seem endless.

Integration with
 Powerful Models: The ability to easily integrate with powerful language models like GPT-3/4 and other specialized AI mo
dels is a major selling point. Users appreciate the ability to leverage state-of-the-art AI without having to train ever
ything from scratch.

Active Development and Community: Many frameworks have active and growing communities, which is a 
huge plus for troubleshooting, sharing ideas, and contributing to the development of the tools.

The Not-So-Good (Concer
ns and Skepticism):

Complexity and Learning Curve: While aiming for accessibility, many users find the frameworks compl
ex to get started with. Understanding the different components, chains, agents, and memory management can be challenging
, especially for beginners.

Debugging and Troubleshooting: When things go wrong, debugging these complex agent systems 
can be difficult. Understanding the flow of information and identifying the root cause of errors can be time-consuming.


Reliability and Consistency: A common concern is the reliability and consistency of these agents. Sometimes they work b
rilliantly, and other times they produce unexpected or nonsensical results. This unpredictability is a barrier for deplo
ying them in critical applications.

'Hallucinations' and Factuality: Because many of these frameworks rely on large lan
guage models, the issue of 'hallucinations' (generating incorrect or fabricated information) is a significant concern. U
sers are wary of relying on agents for tasks where factual accuracy is paramount.

Security Concerns: As these agents ga
in more autonomy and potentially access sensitive data or external tools, security becomes a major worry. Discussions ar
ound access control, sandboxing, and preventing malicious use are frequent.

Resource Intensive: Running complex agents 
can be computationally expensive, especially when interacting with powerful language models. Users are mindful of the co
st implications for development and deployment.

Ethical Considerations: The potential for misuse, bias, and unintended 
consequences with autonomous agents is a recurring theme in discussions. Users are grappling with the ethical implicatio
ns of deploying these powerful technologies.

The 'Demo vs. Reality' Gap: There's a feeling that some of the impressive 
demos don't always translate directly into real-world, robust applications. Bridging this gap is a key challenge.

The F
uture (Where People See This Going):

Despite the challenges, the overall sentiment is optimistic about the future of AI
 agent frameworks. Users believe that as the technology matures, these frameworks will become more reliable, easier to u
se, and capable of tackling increasingly complex problems. There's a sense of being on the cusp of a significant shift i
n how we interact with and leverage AI.

Key Takeaways from User Sentiment:

High potential, early stage: Everyone agree
s there's something powerful here, but it's still relatively early days.

Usability is key: Making these frameworks more
 accessible and easier to debug is crucial for wider adoption.

Focus on reliability and safety: Addressing the concerns
 around hallucinations, security, and ethical implications is paramount for building trust.

Practical applications are 
the goal: While the theoretical possibilities are exciting, users are eager to see more concrete examples of real-world 
value.

What are your thoughts? Have you been experimenting with AI agent frameworks? What are your biggest excitements 
and concerns? Share your experiences in the comments below!



```
---

     
 
all -  [ RA.Aid v0.10.0 - Web research, interactive chat, and more ](https://www.reddit.com/r/LocalLLaMA/comments/1hlf7tz/raaid_v0100_web_research_interactive_chat_and_more/) , 2024-12-26-0913
```
Hey all,

Following up on: [https://www.reddit.com/r/LocalLLaMA/comments/1hczbla/aider\_langchain\_a\_match\_made\_in\_h
eaven/](https://www.reddit.com/r/LocalLLaMA/comments/1hczbla/aider_langchain_a_match_made_in_heaven/)

Just wanted to sh
are an update on RA.Aid v0.10.0. If you haven't come across RA.Aid before, it's our community's open-source autonomous A
I dev agent. It works by placing AI into a ReAct loop, much like windsurf, cursor, devin, or [aide.dev](http://aide.dev)
, but it's completely free and under the Apache License 2.0.

What's New?

* Web Research: RA.Aid can now pull informati
on from the web, making it smarter and more relevant to your coding needs.
* Interactive Chat Mode: With the --chat flag
, you can now guide RA.Aid directly, asking questions or redirecting tasks.
* Ctrl-C Interrupt: You can interrupt its pr
ocess anytime to give feedback or change direction, or just exit.

Why RA.Aid?

* Community Built: This project thrives 
on our collective efforts. Let's make this our dev agent.
* Open Source: No paywalls here, just open collaboration for a
ll.
* Versatile: From refactoring to feature implementation, RA.Aid is there for you.

Contribute or Check it Out:

* Ex
plore RA.Aid: [https://github.com/ai-christianson/RA.Aid](https://github.com/ai-christianson/RA.Aid)
* Contribute: Wheth
er it's code, ideas, or bug reports, your input shapes RA.Aid.
* Feedback: Got thoughts? Let's discuss them in the issue
s.

Let's keep building RA.Aid together into something truly useful for the developer community.

Happy coding! 💻✨🎉
```
---

     
 
all -  [ Roast my resume for Gen AI/ ML based roles. Genuinely needed ](https://www.reddit.com/r/developersIndia/comments/1hlecai/roast_my_resume_for_gen_ai_ml_based_roles/) , 2024-12-26-0913
```
https://preview.redd.it/6qeiz7d11t8e1.png?width=674&format=png&auto=webp&s=161278aa43310409a13f382c4354a9846efe5231

Ple
ase review my resume and roast the fuck out of it but be genuine
```
---

     
 
all -  [ How to handle complexe rag locally ? ](https://www.reddit.com/r/Rag/comments/1hlcdy6/how_to_handle_complexe_rag_locally/) , 2024-12-26-0913
```
Complex multiple files rag
Hello, I'm working on a project related to build a streamlit chat application that allows use
rs ( project holders ) to boost their projects across different stages and help them prepare for presenting their projec
ts within a startup programm,  I have for this rag app , 40 pdfs ( 40 projects ) and a guide.pdf ( cookbook) , this guid
e shows the different stages and phases the project passes by and how to get financement and support from different enti
ties and banks, I used langchain + faiss + ollama + llama 3.2 + hugging face embedding for this project ( data is very p
rivate ) ! The app dosent work well since I want the assistant to follow the rules provided in the guide and consider th
e details of each project to guide the user since the user is a project owner while Leveraging the llama 3.2 capabilitie
s to suggest solution that matches the guide and stages and also to zoom on the corresponding project.
Thank you
```
---

     
 
all -  [ Complex multiple files rag ](https://www.reddit.com/r/LangChain/comments/1hlc16g/complex_multiple_files_rag/) , 2024-12-26-0913
```
Hello, I'm working on a project related to build a streamlit chat application that allows users ( project holders ) to b
oost their projects across different stages and help them prepare for presenting their projects within a startup program
m,  I have for this rag app , 40 pdfs ( 40 projects ) and a guide.pdf ( cookbook) , this guide shows the different stage
s and phases the project passes by and how to get financement and support from different entities and banks, I used lang
chain + faiss + ollama + llama 3.2 + hugging face embedding for this project ( data is very private ) ! The app dosent w
ork well since I want the assistant to follow the rules provided in the guide and consider the details of each project t
o guide the user since the user is a project owner while Leveraging the llama 3.2 capabilities to suggest solution that 
matches the guide and stages and also to zoom on the corresponding project.
Thank you
```
---

     
 
all -  [ How AI Really Learns ](https://open.substack.com/pub/diamantai/p/how-ai-really-learns-the-journey?r=336pe4&utm_campaign=post&utm_medium=web&showWelcomeOnShare=true) , 2024-12-26-0913
```
I’ve heard that many people really want to understand what it means for an AI model to learn, so I’ve written an intuiti
ve and well-explained blog post about it. Enjoy! :)
```
---

     
 
all -  [ how to host langchain on huggingface space? ](https://www.reddit.com/r/LangChain/comments/1hlaytl/how_to_host_langchain_on_huggingface_space/) , 2024-12-26-0913
```
previously i have hosted flowise which is based on langchain but now i am actually using langchain with coding and all i
sing Python and i wanna host it to test, how can i? any guide doc tutorial or anything?
```
---

     
 
all -  [ Agent Marketplace + multi tenant integration ](https://www.reddit.com/r/LangChain/comments/1hl9mo6/agent_marketplace_multi_tenant_integration/) , 2024-12-26-0913
```
I’ve developed a multitenant integration platform that allows users to connect various data sources, integrate with GPT,
 and receive responses. Initially, I saw a market need for such a solution. However, I’m noticing an increasing number o
f RAG agents so I thought I'd go extra mile.

To differentiate, I’m exploring the idea of enabling users to bring their 
own agents, integrate them with our platform, and showcase them in our marketplace. Our platform simplifies the process 
by managing all integrations, offering over 100+ connectors for these agents.

Additionally, I’m considering building a 
workflow feature where users can selectively connect different agents from the marketplace, create inter-agent collabora
tions, and even design their own agents to add value. The ultimate goal is to create a highly customizable and collabora
tive environment for agent-based solutions.

Does this approach sound valuable? I’d appreciate your feedback!  
[Chainwi
de.io](http://Chainwide.io) if anyone's interested.
```
---

     
 
all -  [ Did anyone compare googles embedding model with open ai and others ](https://www.reddit.com/r/LangChain/comments/1hl9agu/did_anyone_compare_googles_embedding_model_with/) , 2024-12-26-0913
```
Hi, I am building a rag application, and I started using Google's embedding model and LLM model. I feel Google's embeddi
ng model is not doing great. I am not getting good search results even when the store contains only a few files. I could
n't find any article comparing the Gemini embedding model with open ai or mistral so I thought I ask here.   
  
[Gemini
 models  |  Gemini API  |  Google AI for Developers](https://ai.google.dev/gemini-api/docs/models/gemini)
```
---

     
 
all -  [ best way for Image Chunking in RAG-Based PDF Answering System?
 ](https://www.reddit.com/r/LangChain/comments/1hl94lj/best_way_for_image_chunking_in_ragbased_pdf/) , 2024-12-26-0913
```
Hi,

I am building a rag based PDF answering system specifically for complex PDFs which contains lots of multi-column ta
bles, images, bulleted points etc. The parsing process is complete and text, tables are genereted properly.

I am stuck 
on image chunking. I found a google colab code for image chunking. Its flow was somewhat like this:

1. make summary of 
text and images, create their embeddings and store it into vector store.
2. And the original text and images were stored
 into docstore, linked with embeddings of summary in vectorstore using doc id.

**Problem**: Lack of enough context for 
the model to generate better summaries of images

I tested it with my PDF but the answer on queries related to image was
n't too accurate and reliable. Wrong images were returned for many queries.

The summaries for images generated by the L
LM (gpt-4o-mini) were not good enough therefore the responses were also not accurate.

I was thinking to pass the text, 
points and paragraph around the images inside the pdf as context to the LLM to generate proper descriptions. But i am no
t very sure of this approach and i need some insights. Did anyone else face similar problem here? How did you tackle it?
 Any help would be greatly appreciated.
```
---

     
 
all -  [ Hiring - Data Science Engr - Bangalore Startup ](https://www.reddit.com/r/StartUpIndia/comments/1hl73ps/hiring_data_science_engr_bangalore_startup/) , 2024-12-26-0913
```
**Data Science Engr**  
**Bangalore based startup**

7+ Yrs

Requirements 

1- GenAI deployment experience

2-Familiar w
ith LLM frameworks like Langchain & Multi GPU training methods, fastAPI async

3- Experience in Tensorflow, Pytorch & Da
ta manipulation - pandas, NumPy

4-Tools experience of AWS / Azure to deploy ML models & Data visualisation experience i
n Tableau / PowerBI

Max fixed comp on offer - INR 45 L

Apply - [https://www.linkedin.com/jobs/view/4108453652/](https:
//www.linkedin.com/jobs/view/4108453652/) 
```
---

     
 
all -  [ Hiring for a Data Science Engr - Bangalore Startup ](https://www.reddit.com/r/IndiaJobsOpenings/comments/1hl7152/hiring_for_a_data_science_engr_bangalore_startup/) , 2024-12-26-0913
```
Dat Science Engr  
Bangalore based startup  
IC role - Full time WFO, NO HYBRID, NO WFH

Requirements 

7+ yrs exp

Requ
irements 

1- GenAI model deployment real time

2-Familiar with LLM frameworks like Langchain,  Multi GPU training metho
ds, fastAPI async

3- Experience with Machine Learning experience in Tensorflow, Pytorch & Data manipulation - pandas, N
umPy

4-Tools experience of AWS / Azure to deploy ML models & Data visualisation experience in Tableau / PowerBI  
  
Ma
x fixed comp on offer - INR 45 L

Share CV - [sandeep@corpsourceone.com](mailto:sandeep@corpsourceone.com) 
```
---

     
 
all -  [ Role of Ruby in AI trends ](https://www.reddit.com/r/ruby/comments/1hl4ri5/role_of_ruby_in_ai_trends/) , 2024-12-26-0913
```
What’s the role of Ruby in AI trends? Should we stick with it or switch to Python?

As we dive deeper into 2024, AI is c
learly dominating the tech landscape, and Python seems to have an undeniable lead. From AI agents to cutting-edge model 
development and seamless integrations, Python is the go-to language for the latest advancements.

Ruby, on the other han
d, doesn’t seem to share the same momentum in AI. While the ecosystem has seen some contributions (e.g., gems like Langc
hain.rb), it’s still far behind Python’s robust libraries, frameworks, and community support in this space.

For those o
f us who love Ruby and use it extensively in web development, how do you see its future in AI?

- Do you think Ruby has 
potential in this space, or is it destined to remain a niche choice for AI work?

- Are you sticking with Ruby for AI pr
ojects, even if it means using a lesser-equipped ecosystem?

- Or would you switch to Python for AI development, conside
ring its vast tools and community support?


I’d love to hear your thoughts on where Ruby fits into the AI conversation 
and how you approach this dilemma.


---

What do you think?


```
---

     
 
all -  [ Problems installing pyarrow in a virtual environment ](https://www.reddit.com/r/learnpython/comments/1hl32jr/problems_installing_pyarrow_in_a_virtual/) , 2024-12-26-0913
```
**Context:** I’m a data analyst and I usually work in only one environment that’s mainly Jupyter Notebooks. I don’t know
 anything about software best practices or development, github, and I have a tenuous grasp on coding in general. 

**My 
Goal:** I recently built a simple AI Agent in python that connects my companies’ BigQuery database to an LLM and then ou
tputs that AI response back into BigQuery. 

I need to find a way to deploy this to google cloud so that my co-workers c
an interact with it. I decided I am going to use  Streamlit, which is supposedly the easiest way to stand up a front end
 for a little Python app. 

**The Problem:** I got a simple 'hello world' streamlit page up, but when I try to recreate 
the environment to build my AI Agent in the new environment, the installation of key packages doesn't work. Pyarrow is t
he main one I'm having trouble with right now.   
  
I read online that I should create a virtual environment for deploy
ing my app to the cloud.  I'm not sure if this is strictly necessary, but that's what I've been trying to do because I'm
 just following the steps. Plus, I couldn't run streamlit from my jupyter notebooks.   


**What i've done:** I created 
the virtual environment using `python3 -m venv .venv`, which works fine, but when I try to install the packages I need (
like `pyarrow, langchain, pandas`, etc.), I keep running into errors. I expected that I would just create the environmen
t, activate it, and then run `pip install pyarrow, pip install langchain`, and `pip install pandas.` However, instead of
 it installing smoothly, I started getting errors with pyarrow and ended up having to install things like cmake, apache-
arrow, and more. But, it’s frustrating because none of these installations of cmake or apache-arrow are solving the prob
lem with pyarrow. 



**Snippet of the Errors:**

>Collecting pyarrow

>  Using cached pyarrow-18.1.0.tar.gz (1.1 MB)

>
  Installing build dependencies ... done

>  Getting requirements to build wheel ... done

>  Preparing metadata (pyproj
ect.toml) ... done

>Building wheels for collected packages: pyarrow

>  Building wheel for pyarrow (pyproject.toml) ...
 error

>  error: subprocess-exited-with-error

>  × Building wheel for pyarrow (pyproject.toml) did not run successfull
y.

>  │ exit code: 1

>  ╰─> \[832 lines of output\]

>\-- Configuring incomplete, errors occurred!

>error: command '/
usr/local/bin/cmake' failed with exit code 1

>\[end of output\]  

>  note: This error originates from a subprocess, an
d is likely not a problem with pip.

>  ERROR: Failed building wheel for pyarrow

>Failed to build pyarrow

>ERROR: ERRO
R: Failed to build installable wheels for some pyproject.toml based projects (pyarrow)

>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\
_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_



I’ve been trying to troubleshoot online, but noth
ing is really working. 

Any help would be greatly appreciated. If you could point me toward the key concepts I need to 
understand in order to diagnose the issue, that would be really helpful. If you have any specific advice, I would love t
hat. 


```
---

     
 
all -  [ World's largest AI Agent directory. ](https://i.redd.it/dtg2z1u3tn8e1.png) , 2024-12-26-0913
```
Hey all!

I've made the world's largest ai agent directory. 

The agent market is so scrappy at the moment and very diff
icult to find the right agent for the job. 

Agent Locker makes it as easy as possible to filter agents by category, use
 case, integration method and price and you can also specify agentic, ai tools and agent platforms. 

There's over 1000 
ai listings already and we're growing everyday. 

https://www.agentlocker.ai 

Hope you find it useful.
```
---

     
 
all -  [ [Student] I'm only getting interviews for ML/AI internships if I have a referral. What's wrong with  ](https://www.reddit.com/r/EngineeringResumes/comments/1hkwp6s/student_im_only_getting_interviews_for_mlai/) , 2024-12-26-0913
```
I am a computer engineering Master's student focusing on ML/AI (it's all I've done for around 3 years). I've been applyi
ng to a lot of ML/AI internships (not FAANG), but I haven't been able to get an interview unless I have a referral. 

Th
e only reason I got my previous AI internship at Lennox, and my interview with Salesforce this time around, is because s
omeone had to make a recruiter actually look at my resume. The only one I got on my own was JP Morgan last year, but I h
ave been rejected without an interview or OA by hundreds of companies since then.

I'm wondering what I'm doing wrong an
d how to fix it. I'm not sure if I can't get an interview on my own because I don't have enough experience or if it's be
cause my resume is bad. The weird thing is that whenever I have an interview the managers seem really interested in my e
xperience and projects, but most of the time I'm not sure if the recruiters are even reading my resume.

Any help would 
be greatly appreciated, because this process has been very demoralizing, and even though my Salesforce interview went we
ll I'm not sure if I'll get the position (and I don't have any backup because I can't get an interview).

PS: The only o
ther experience I can add to my resume for now is the Amazon AI safety challenge I'm working on with some professors in 
my department, there should be a paper written about our work on this too. Not sure if adding that and taking out one of
 my older projects would help.

https://preview.redd.it/y2gsxnivrn8e1.jpg?width=5100&format=pjpg&auto=webp&s=457e415681e
6673aece7af38b4a829769aa56384


```
---

     
 
all -  [ I'm only getting interviews if I have a referral. What's wrong with my resume/experience?  ](https://www.reddit.com/r/MLQuestions/comments/1hkwh7a/im_only_getting_interviews_if_i_have_a_referral/) , 2024-12-26-0913
```
I am a computer engineering Master's student focusing on ML/AI (it's all I've done for around 3 years). I've been applyi
ng to a lot of ML/AI internships (not FAANG), but I haven't been able to get an interview unless I have a referral. The 
only reason I got my previous AI internship at Lennox, and my interview with Salesforce this time around, is because som
eone had to make a recruiter actually look at my resume. The only one I got on my own was JP Morgan last year, but I hav
e been rejected without an interview or OA by hundreds of companies since then.

I'm wondering what I'm doing wrong and 
how to fix it. I'm not sure if I can't get an interview on my own because I don't have enough experience or if it's beca
use my resume is bad.  The weird thing is that whenever I have an interview the managers seem really interested in my ex
perience and projects, but most of the time I'm not sure if the recruiters are even reading my resume. 

  
Any help wou
ld be greatly appreciated, because this process has been very demoralizing, and even though my Salesforce interview went
 well I'm not sure if I'll get the position (and I don't have any backup because I can't get an interview). 



PS: The 
only other experience I can add to my resume for now is the Amazon AI safety challenge I'm working on with some professo
rs in my department, there should be a paper written about our work on this too. Not sure if adding that and taking out 
one of my older projects would help.

https://preview.redd.it/fzbh56slpn8e1.png?width=1252&format=png&auto=webp&s=2161b4
8716d798426ba78bf8a8c7c4e40e7d8ef5


```
---

     
 
all -  [ How to pick agents from LangChain Hub? ](https://www.reddit.com/r/LangChain/comments/1hkwb39/how_to_pick_agents_from_langchain_hub/) , 2024-12-26-0913
```
There are so many agents on LangChain Hub. How do I pick ones that would meet my needs? 

I have tried this one,  hwchas
e17/openai-functions-agent. But it seems  to support openai models better. I want to use an agent to work with tools and
 then use LLM to yield answers. These tools will retrieve data from yfinance. Thanks.  

```
---

     
 
all -  [ Langgraph + Cursor ](https://www.reddit.com/r/LangChain/comments/1hkt13b/langgraph_cursor/) , 2024-12-26-0913
```
Has anyone a good workflow to create LG apps with cursor ai?

```
---

     
 
all -  [ Help me understand the potential career options for an SE in the wake of AI development ](https://www.reddit.com/r/learnmachinelearning/comments/1hkqvmn/help_me_understand_the_potential_career_options/) , 2024-12-26-0913
```
I'm an SE with 10 years of experience and no degree, and I'm acutely aware of the need to be adaptable with the given di
rection of AI, but I'm struggling to understand the different possible paths to take.

Assuming we don't hit a level of 
AI which replaces *ALL* jobs yet, I figure the most useful path I can take is to strengthen high level SE skills, e.g. s
ystem architecture and design, as well as being au fait with AI integrations, e.g. using libraries like Langchain to bui
ld RAG systems, being able to use vector DBs etc.

Once I've got those basics down, I want to transition diagonally into
 a field that's at least somewhat robust to changes, e.g. ML engineer, MLops, etc. Other options I have wondered about a
re things like robotics or cyber security, which are both fields I assume will become more necessary given the presumed 
trajectory of AI. 

I think ideally I'd go into an ML engineer/MLops role, assuming the day to day looks roughly like de
veloping, finetuning, evaluating and deploying models, or just creating novels things.

The issue I'm having is understa
nding what's actually expected of those roles, as AI engineer / ML engineer seems to mean 100 different things, with som
e companies are expecting PhDs and others are expecting SEs who can use OpenAI APIs. And in general I'd just quite like 
to hear people's thoughts on what career paths people think are useful to aim for, have the best chance of sticking arou
nd for a few years, think are feasible, what skills to aim for which will generally be useful, etc.

Any and all thought
s welcome
```
---

     
 
all -  [ A rant about LangChain, and a minimalist alternative ](https://www.reddit.com/r/LangChain/comments/1hknn5a/a_rant_about_langchain_and_a_minimalist/) , 2024-12-26-0913
```
So, one of the questions I had on [my GitHub project](https://github.com/BrainBlend-AI/atomic-agents) was:

>Why we need
 this framework ?

>I’m trying to get a better understanding of this framework and was hoping you could help because the
 openai API also offer structured outputs?

>Since LangChain also supports input/output schemas with validation, what ma
kes this tool different or more valuable?

>I am asking because all trainings they are teaching langchain library to new
 developers . I’d really appreciate your insights—thanks so much for your time!

And, I figured the answer to this might
 be useful to some of you other fine folk here, it did turn into a bit of a rant, but here we go (beware, strong opinion
s follow):

Let me start by saying that I think it is wrong to start with learning or teaching *any* framework if you do
n't know how to do things without the framework. In this case, you should learn how to use the API on its own first—lear
n what different techniques are on their own and how to implement them, like RAG, ReACT, Chain-of-Thought, etc.—so you c
an actually understand what value a framework or library does (or doesn’t) bring to the table.

Now, as a developer with
 15 years of experience, knowing people are being taught to use LangChain straight out of the gate *really* makes me sad
, because—let’s be honest—it’s objectively not a good choice, and I’ve met a lot of folks who can corroborate this.

Per
sonally, I took a year off between clients to figure out what I could use to deliver AI projects in the fastest way poss
ible, while still sticking to my principle of *only* delivering high-quality and maintainable code.

And the sad truth i
s that out of everything I tried, LangChain might be the *worst* possible choice—while somehow also being the most popul
ar. Common complaints on reddit and from my personal convos with devs & teamleads/CTOs are:

* Unnecessary abstractions

* The same feature being done in three different ways
* Hard to customize
* Hard to maintain (things break often between
 updates)

Personally, I took more than one deep-dive into its code-base and from the perspective of someone who has bee
n coding for 15+ years, it is pretty horrendous in terms of programming patterns, best practices, etc... All things that
 should be **AT THE ABSOLUTE FOREFRONT of anything that is made for other developers!**

**So, why is LangChain so popul
ar?** Because it’s not just an open-source library, it’s a company with a CEO, investors, venture capital, etc. They too
k something that was never really built for the long-term and blew it up. Then they integrated every single prompt-engin
eering paper (ReACT, CoT, and so on) rather than just providing the tools to let you build your own approach. In reality
, each method can be tweaked in hundreds of ways that the library just doesn’t allow you to do (easily).

Their core bus
iness is not providing you with the best developer experience or the most maintainable code; it’s about partnerships wit
h every vector DB and search company (and hooking up with educators, too). That’s the only real reason people keep getti
ng into LangChain: it’s just really popular.

**The Minimalist Alternative: Atomic Agents**  
You don’t *need* to use At
omic Agents (heck, it might not even be the right fit for your use case), but here’s *why* I built it and made it open-s
ource:

1. I started out using the OpenAI API directly.
2. I wanted structured output and not have to parse JSON manuall
y, so I found “Guidance.” But after its API changed, I discovered “Instructor,” and I liked it more.
3. With Instructor,
 I could easily switch to other language models or providers (Claude, Groq, etc.) without heavy rewrites, and it has a b
uilt-in retry mechanism.
4. The missing piece was a consistent way to build AI applications—something minimalistic, lett
ing me experiment quickly but still have maintainable, production-quality code.

After trying out LangChain, crewai, aut
ogen, langgraph, flowise, and so forth, I just kept coming back to a simpler approach. Eventually, after several rewrite
s, I ended up with what I now call Atomic Agents. Multiple companies have approached me about it as an alternative to La
ngChain, and I’m currently helping a client rewrite their codebase from LangChain to Atomic Agents because their CTO has
 the same maintainability concerns I did.

**So why do you need Atomic Agents?** If you want the benefits of Instructor,
 coupled with a minimalist organizational layer that lets you experiment freely and still deliver production-grade code,
 then try it out. If you’re happy building from scratch, do that. The point is you *understand* the techniques first, an
d then pick your tools.

[Here’s the repo if you want to take a look.](https://github.com/BrainBlend-AI/atomic-agents)


Hope this clarifies some things! Feel free to share your thoughts below.
```
---

     
 
all -  [ RAG LLM Generating the Prompt also at the response ](https://www.reddit.com/r/LangChain/comments/1hkn089/rag_llm_generating_the_prompt_also_at_the_response/) , 2024-12-26-0913
```
hi , im trying to build simple RAG system , everything good but the output contain everything (retrieval docs+promt+answ
er+halluciation) even with print(result\['result'\]) , im using llama 3.2 3b . any solution?
```
---

     
 
all -  [ BuildFast Masterclass - Peter (Download) ](https://www.reddit.com/r/EvangelineStudying/comments/1hki5oq/buildfast_masterclass_peter_download/) , 2024-12-26-0913
```
Can you get 'BuildFast Masterclass - Peter' as a free download? Nope, but you can get it through a group-buy for a small
 fee. It's 100% legit. Just check it out.

👉 [BuildFast Masterclass - Peter (Download)](https://lunacourse.com/product/p
eter-build-fast-masterclass/)

* Only $18
* Proof of Product included

https://preview.redd.it/amyv6urxoj8e1.png?width=2
212&format=png&auto=webp&s=335b0c8806f2e1a63cfa2f1c934aebc6dab3954b

https://preview.redd.it/cd9qcdpzoj8e1.png?width=110
8&format=png&auto=webp&s=8f0003a61943771da7b2f4b4c72bd1ba2b3a0494

# What is BuildFast Masterclass?

'BuildFast Mastercl
ass - Peter' is your one-stop-shop for diving headfirst into the AI-building universe. Created by Peter, a seasoned soft
ware engineer turned AI enthusiast, this course promises to take you from “where do I even begin?” to confidently launch
ing your own AI-powered apps. It's for developers, career professionals, and small business owners looking to move past 
the overwhelm and actually start creating with AI.

Peter’s mission? To help you save time, cut through the noise of end
less AI tutorials, and focus on building real, functional projects.

# Who is BuildFast Masterclass for?

If you’ve ever
 felt lost in the vast sea of AI tools, libraries, and jargon, then this course is for you. Whether you’re a developer, 
a small business owner, or someone curious about AI but unsure where to start, BuildFast Masterclass caters to all skill
 levels.

The course is especially great for people who:

* Have ideas but struggle to turn them into reality.
* Are tir
ed of consuming tutorial after tutorial without taking action.
* Want to learn by doing, not just watching or reading.


# Why should you consider BuildFast Masterclass?

The biggest draw of this course is its hands-on approach. Peter emphas
izes *'just-in-time learning'*—a method where you learn a concept and immediately put it into practice by building somet
hing. This is a game-changer because it keeps you motivated and ensures the knowledge sticks.

Plus, the course isn’t ju
st about learning AI; it’s about creating tangible products. Whether it’s an AI chatbot, a voice app, or fine-tuning an 
LLM, every project is designed to teach you real-world applications.

# What makes BuildFast Masterclass different?

Her
e’s where 'BuildFast Masterclass - Peter' really stands out:

* **Step-by-step Roadmap**: No more piecing together rando
m tutorials. This course organizes everything into a logical flow.
* **Community**: With 357+ members, you’ll join a vib
rant group of like-minded builders from around the globe. Collaboration and support are a big part of the experience.
* 
**Expert Guidance**: Peter’s background as a FAANG software engineer and his passion for teaching means you’re in good h
ands.

# When can you start?

Right now! The moment you join, you get instant access to a library of videos covering fun
damentals like LLMs, prompts, memory types, and vector databases. The course is entirely self-paced, so you can fit it i
nto your schedule.

# How does BuildFast Masterclass work?

It’s simple:

1. **Learn the Fundamentals**: Bite-sized vide
os that break down core concepts.
2. **Build Projects**: Apply what you’ve learned to create actual AI products.
3. **Jo
in the Community**: Share your progress, ask for help, and get inspired by others.

# Where does the magic happen?

The 
course is hosted online, so you can learn from anywhere. Whether you’re in your living room or a coffee shop halfway acr
oss the world, all you need is an internet connection and the drive to start building.

# Final Thoughts on BuildFast Ma
sterclass

'BuildFast Masterclass - Peter' is perfect if you’re ready to stop learning and start building. The hands-on 
projects, supportive community, and clear roadmap make it an ideal choice for anyone looking to break into AI developmen
t.

With Peter as your guide, you’ll go from feeling overwhelmed to shipping your first AI product faster than you think
. So why wait? Dive in and start building the future today!
```
---

     
 
MachineLearning -  [ [P] Minima: local conversational retrieval augmented generation project (Ollama, Langchain, FastAPI, ](https://www.reddit.com/r/MachineLearning/comments/1h1pudq/p_minima_local_conversational_retrieval_augmented/) , 2024-12-26-0913
```
  
[https://github.com/dmayboroda/minima](https://github.com/dmayboroda/minima)  
  
Hey everyone, I would like to intro
duce you my latest repo, that is a local conversational rag on your files, Be honest, you can use this as a rag on-premi
ses, cause it is build with docker, langchain, ollama, fastapi, hf All models download automatically, soon I'll add an a
bility to choose a model For now solution contains:

* Locally running Ollama (currently qwen-0.5b model hardcoded, soon
 you'll be able to choose a model from ollama registry)
* Local indexing (using sentence-transformer embedding model, yo
u can switch to other model, but only sentence-transformers applied, also will be changed soon)
* Qdrant container runni
ng on your machine
* Reranker running locally (BAAI/bge-reranker-base currently hardcoded, but i will also add an abilit
y to choose a reranker)
* Websocket based chat with saving history
* Simple chat UI written with React
* As a plus, you 
can use local rag with ChatGPT as a custom GPT, so you able to query your local data through official chatgpt web and ma
c os/ios app.
* You can deploy it as a RAG on-premises, all containers can work on CPU machines

Couple of ideas/problem
s:

* Model Context Protocol support
* Right now there is no incremental indexing or reindexing
* No selection for the m
odels (will be added soon)
* Different environment support (cuda, mps, custom npu's)

Welcome to contribute (watch, fork
, star) Thank you so much!
```
---

     
