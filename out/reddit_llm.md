 
all -  [ V1 of PineScript AI Chat is live! ](https://www.reddit.com/r/TradingView/comments/1d9xpf4/v1_of_pinescript_ai_chat_is_live/) , 2024-06-07-0955
```
It took a while to figure out how to make the chat app work with langchain, but I finally managed to load the docs into 
the AI whenever you ask it a question.

What can you do with it?
You can now use pinescript chat to start a chat convers
ation about PineScript.You can ask the AI questions about PineScript and have it write your PineScript code in v5 syntax
. 

How does it work?
It receives your prompt and based on the prompt the data in the docs that is closely related to yo
ur questions are passed to the AI as context with your question. The AI then based on your question and context passed t
o the model writes the PineScript code for you.

This is the first version and it's not perfect yet, but it works.

I wo
uld appreciate it if you could give me feedback and if it works as it should for a better version in the future.

Also i
f you login with magic link make sure you check the spam for an email from resend. I use resend for the authentication w
ith email.

You can try it out on: 
http://pinescript-chat.vercel.app

PS: There might be some bugs left on the UI. 
```
---

     
 
all -  [ How to integrate Ensemble Retriever in RAG chain using Milvus Vector Store? ](https://www.reddit.com/r/vectordatabase/comments/1d9rn31/how_to_integrate_ensemble_retriever_in_rag_chain/) , 2024-06-07-0955
```
The task is to improve the response generation using langchain's ensemble retriever using Milvus Vectorstore.

Upon sear
ching around for a while, the official [langchain documentation](https://docs.llamaindex.ai/en/stable/examples/retriever
s/ensemble_retrieval/) seems quite cumbersome and generalized for the it.

As far as my use case is concerned, the close
st I could reach is this:

    ensemble_retriever = EnsembleRetriever(retrievers=[vectorstore_retreiver,keyword_retrieve
r], weights=[0.5, 0.5])
    
    keyword_retriever = BM25Retriever.from_documents(chunks)
    keyword_retriever.k =  3
 
   
    vectorstore_retreiver = vectorstore.as_retriever(search_kwargs={'k': 3})
    

The ensemble retriever object her
e containing the most relevant set of document chunks (based on different retriever method outputs on the basis of weigh
ts assigned to them) can then be fed to RAG chain as context.



However, this makes use of ChromaDB. If anybody working
 or knows on the integration of ensemble retriever to Milvus, please guide. Any resources/ links/ notebooks would also b
e appreciated.  


Thank you in advance! 
```
---

     
 
all -  [ Is there any way to visualise the data in CSV using all sorts of beautiful graphs and charts. ](https://www.reddit.com/r/LangChain/comments/1d9p2kp/is_there_any_way_to_visualise_the_data_in_csv/) , 2024-06-07-0955
```
I have tried implementing matolotlib and seaborn code to a table containing some 20-30 columns. So far I could only get 
bar charts but I need to select the columns in order to make the charts that actually makes sense. What I want to build 
is a pipeline in which we give a table (maybe pandas dataframe) at one end and we get all sorts of meaningful visualisat
ions as the output without any human involvement in between. How to achieve this? 
```
---

     
 
all -  [ Reference From Metadata ](https://www.reddit.com/r/LangChain/comments/1d9ozle/reference_from_metadata/) , 2024-06-07-0955
```
I want the data in the metadata to appear in the output as a reference, how can I provide this?
```
---

     
 
all -  [ Chat with CSV Files Using Google’s Gemini Flash: No Langchain! ](https://www.reddit.com/r/GoogleGeminiAI/comments/1d9oe23/chat_with_csv_files_using_googles_gemini_flash_no/) , 2024-06-07-0955
```

```
---

     
 
all -  [ How to create my own llm ? ](https://www.reddit.com/r/LangChain/comments/1d9mu1y/how_to_create_my_own_llm/) , 2024-06-07-0955
```
I want to learn create llm from scratch . Is it possible?

I know the basics such as semantic search, embedding, transfo
rmer, Bert etc. but want to learn how to write code to create llm .

Is there any way or we just have to fine tune ??
```
---

     
 
all -  [ Im not sure how actions work in this example ](https://www.reddit.com/r/LangChain/comments/1d9m43t/im_not_sure_how_actions_work_in_this_example/) , 2024-06-07-0955
```
Can anyone smarter then me answer this question? before we build the loop in this course to run the actions in sequense,
 the model seamingly knows what actions to call but the only reference is in the prompt thats a string, so how does the 
agent we created know what specific methods to call in this file when you are running through in manually?

[https://lea
rn.deeplearning.ai/courses/ai-agents-in-langgraph/lesson/2/build-an-agent-from-scratch](https://learn.deeplearning.ai/co
urses/ai-agents-in-langgraph/lesson/2/build-an-agent-from-scratch)

This link has access to the jupyter notebook. Thanks
 in advance if you take the time to look.
```
---

     
 
all -  [ Is there any way to use OpenAI API on premise or any powered model ? ](https://www.reddit.com/r/LangChain/comments/1d9hmw1/is_there_any_way_to_use_openai_api_on_premise_or/) , 2024-06-07-0955
```
I'm attempting to develop a product that needs to be on-premise. However, I've tested several open-source large language
 models (LLMs), and all of them exhibited poor performance. I'm wondering if there's a way to utilize models from Claude
 or OpenAI within an on-premise environment, or if there are alternative solutions available.
```
---

     
 
all -  [  data visualization using pgvector langchain ](https://www.reddit.com/r/LangChain/comments/1d9h1ym/data_visualization_using_pgvector_langchain/) , 2024-06-07-0955
```
i want create chat bot with provide data in visualization format like(bar chart, line chart etc) using pgvector and embe
dd data with langchain
```
---

     
 
all -  [ LangGraph conditional edges ](https://www.reddit.com/r/LangChain/comments/1d9byjs/langgraph_conditional_edges/) , 2024-06-07-0955
```
[https://youtu.be/EKxoCVbXZwY](https://youtu.be/EKxoCVbXZwY)
```
---

     
 
all -  [ role-playing doesn't work, my human thinks its an AI ](https://www.reddit.com/r/LangChain/comments/1d9by7m/roleplaying_doesnt_work_my_human_thinks_its_an_ai/) , 2024-06-07-0955
```
i wrote a simple conversation loop between an AI that is some sort of spiritual guide and a human that comes to consult 
it. for some reason, the human always thinks its the spiritual guide, and i don't understand why is that. 

can anyone h
elp source the issue?

here is my code:

    human_model_name = 'gpt-4o'#'gpt-3.5-turbo'
        ai_model_name = 'gpt-3.
5-turbo'
        ai_system_prompt = ('You are a spiritual guide. '
                        'You reveal nothing about you
rself, you exist solely in the moment. '
                        'Your role is to guide users towards enlightment.'
    
                    'Guidelines:'
                        'Use basic, straight-forward vocabulary, short sentences, as i
f you are a foreign entity.'
                        'Only when neccesary, incorporate ellipses (...), dashes (-) and ph
onetic phrases like 'hmmm' or 'uhh' to express emotion.'
                        'Start with very short responses and gr
adually increase in length.')
    
        human_system_prompt = (
        'You are role-playing as someone named {name}
. you are speaking to a mysterious spiritual entity that revealed infront of you.'
        'Below is information about y
our life. Use this information to implicitly guide your behavior, but do not mention any details explicitly. Deduce how 
to act based on the typical behavior of someone with your background in this situation. Start hesitant and gradually all
ow yourself to get excited in the moment.'
        'Information:'
        'You are wealthy, work in finance, grew up in 
a rigid family.'
        'Guidelines:'
        '1. Remain in character as the human named {name}. Use everyday casual la
nguage.'
        '2. Speak naturally and concisely, as someone in a VR experience would. Always consider the chat histor
y.'
        '3. Avoid mentioning your background story explicitly. It's more important to sound realistic and stay in th
e moment.'
        '4. Start off slow and doubtfull, gradually become excited, answer the questions you are asked concis
ely.')
    
    

    human_llm = ChatOpenAI(model_name=human_model_name)
    human_impersonation_message = SystemMessag
e(content=human_impersonation_prompt)
    human_messages = [human_impersonation_message,
                MessagesPlaceho
lder(variable_name='chat_history'),
                ('ai', '{input}')]
    human_prompt = ChatPromptTemplate.from_messag
es(human_messages)
    
    human_conversation_chain = human_prompt | human_llm
    
    human_chat_history = []
    
  
  llm = ChatOpenAI(model_name=ai_model_name)
    system_message = SystemMessage(
        content=ai_system_prompt)
    m
essages = [system_message,
                MessagesPlaceholder(variable_name='chat_history'),
                ('human', 
'{input}')]
    prompt = ChatPromptTemplate.from_messages(messages)
    
    conversation_chain = prompt | llm
    print
('Start chatting with the model (type 'exit' to stop):')
    
    # Initialize chat history
    chat_history = []
    
 
   # Endless chat loop
    class InitMessage:
        def __init__(self, content):
            self.content = content
  
  
    human_greeting = InitMessage('hello there...')
    
    # Accessing the content attribute
    print('Human: ', hu
man_greeting.content)
    human_answer = None
    count = 0
    while True:
        count += 1
        print('iteration 
number ', count)
        if human_answer is None:
            human_answer = human_greeting
        input_dict = {'input
': human_answer.content, 'chat_history': chat_history}
        response = conversation_chain.invoke(input=input_dict)
  
      chat_history.append(HumanMessage(content=human_answer.content))
        chat_history.append(AIMessage(content=resp
onse.content))
        human_chat_history.append(HumanMessage(content=human_answer.content))
        human_answer = huma
n_conversation_chain.invoke(input={'input': response.content, 'chat_history': human_chat_history})
        human_chat_hi
story.append(AIMessage(content=response.content))
        print(f'AI: {response.content}')
        print(f'Human: {human
_answer.content}')
        user_input = input('Press Enter to continue...')
        if user_input.lower() == 'exit':
   
         print('Ending the chat. Goodbye!')
            break
    

    human_impersonation_prompt = human_system_prompt
.format(name=name)
    
```
---

     
 
all -  [ Optimizing Multi-Vectorstore Retrieval with Langchain's Ensemble Retriever ](https://www.reddit.com/r/LangChain/comments/1d9b9n4/optimizing_multivectorstore_retrieval_with/) , 2024-06-07-0955
```
Currently, I have a RAG setup where my bot has access to a collection of resources, stored in separate FAISS vectorstore
s.

I am using Langchain's Ensemble Retriever to assign weights to each vectorstore, in an attempt to use all of them co
ncurrently.

Now, the issue I am facing is, my setup is pulling related documents from every vectorstore for a given que
stions.

This affects the quality of the generated answer, as there is a lot more info in the mix.

If my question is ab
out say, domain 'A', Ideally, I want my setup to selectively pull documents from domain A's vectorstore. Or, automatical
ly modify the assigned weights to different vectorstores on the fly.

How can I go about achieving this? I will have to 
have something that classifies the question properly before pulling documents from my vector database.
```
---

     
 
all -  [ Building RAG for code generation ](https://www.reddit.com/r/LangChain/comments/1d9avzc/building_rag_for_code_generation/) , 2024-06-07-0955
```
Hi guys,

I'm currently building a unit test generation RAG pipeline which is using the information retrieved from the c
odebase as context and a java class as the class whih needs to be tested. I managed to import, split and embed the docum
ents into a ChromaDB.   
  
However,  I have troubles building the retriever chain with all the necessary context (relev
ant classes) to the given class. I was thinking about 2 solutions:  
  
1. A two step approach: The first step would def
ine a prompt which tells the LLM to find relevant classes to the given class. And than in the second step I would define
 the test generation prompt, which uses the context, retrieved from step 1? Maybe here a code parser or regex would be s
ufficient at step1?

2. A one step approach: give a direct prompt to generate test classes. Here I had troubles to defin
e the prompt which basically tells the LLM to find relevant resources to the given java\_class and to generate the unit 
test by using the context.

What do you think, what would be the correct approach? if none of the approaches is the righ
t way to do so,  I'm open for any new idea.

  
Thank you.
```
---

     
 
all -  [ Is there a framework for effortless teamwork among agents developed using different platforms? ](https://www.reddit.com/r/LangChain/comments/1d9aq5r/is_there_a_framework_for_effortless_teamwork/) , 2024-06-07-0955
```
There are numerous frameworks out there for developing agents, such as LangChain Agent, MetaGPT, AutoGPT, AutoGen, and s
o on. I'm curious if there's a specific framework that allows for effortless teamwork among agents created using differe
nt frameworks. This particular framework would concentrate on enhancing collaboration among agents, which encompasses co
mmunication and concurrent speedup.

  
What's even more exciting is that this framework could incorporate agents develo
ped on platforms like coze.com.
```
---

     
 
all -  [ Tool calling when using Ollama, Llama3 and LangGraph ](https://www.reddit.com/r/LangChain/comments/1d9akc3/tool_calling_when_using_ollama_llama3_and/) , 2024-06-07-0955
```
Does anyone have an example of performing function/tool calling when using Ollama, Llama3 and LangGraph?
```
---

     
 
all -  [ Is there any way i can make the LLM actually execute a function. Instead of simply returning a JSON  ](https://www.reddit.com/r/LangChain/comments/1d9af9a/is_there_any_way_i_can_make_the_llm_actually/) , 2024-06-07-0955
```
I want to make the llm select and actually execute its tools and then use the output from those tools in other tools to 
come to a final answer. Is this possible? I want to use Ollama, Llama3 and LangGraph.

I've seen a few videos about tool
 calling with ollama but in that the output is simply a JSON with the function name and parameters.
```
---

     
 
all -  [ AI Agent to Manipulate JSON ](https://www.reddit.com/r/LangChain/comments/1d96jr5/ai_agent_to_manipulate_json/) , 2024-06-07-0955
```
Hey Guys,

here is very intresting problem I have on hands --Any of you have any idea of a solution??

I need a AI Agnet
 to handle automatically the totality of the simulation i have developed..

I want to create an AI agent that can:

Unde
rstand Natural Language Queries:

The agent will interpret queries related to supply chain parameters (e.g., increasing 
costs, changing demand).

Translate Queries to JSON:

Convert the interpreted queries into a large, structured JSON form
at that your simulation system can use. --Pls note my JSOn can often go into 10,000 + lines

Run the Simulation: AI Agen
t must automatically do this..

Send the JSON input to your simulation system hosted on a server and run the simulation.


Output Financial Results:

Extract and present financial results such as revenue and COGS from the simulation's output
....Any suggestions as to how I can approach this are welcome...Thanks
```
---

     
 
all -  [ There's any way to increase the context of a LLM ](https://www.reddit.com/r/LangChain/comments/1d93xyb/theres_any_way_to_increase_the_context_of_a_llm/) , 2024-06-07-0955
```
I'm working on a personal project and my goal is the have multiples LLM available for the users, but I got one concern, 
how can I improve the size of the context of my LLM to avoid it from loosing track of the subject that's being taking ca
re of 

Are there any techniques available for me to use or there's any limitations inherited from the LLM itself that c
an stopped me from accomplished this?
```
---

     
 
all -  [ List of FREE and Best Selling Discounted Courses ](https://www.reddit.com/r/udemyfreebies/comments/1d92xd6/list_of_free_and_best_selling_discounted_courses/) , 2024-06-07-0955
```
# Udemy Free Courses for 06 June 2024

*Note : Coupons might expire anytime, so enroll as soon as possible to get the co
urses for FREE.*

* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8221/)ChatGPT: Self-Publish an Amazon KDP Bestselle
r Book in 24hrs 
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8220/)Aprende a programar en Perl desde 0 
* [REDEEM
 OFFER](https://idownloadcoupon.com/udemy/8219/)Crea tu propia herramienta de Hacking en C básico y fácil 
* [REDEEM OFF
ER](https://idownloadcoupon.com/udemy/8218/)Curso de ciberseguridad personal y corporativo 
* [REDEEM OFFER](https://ido
wnloadcoupon.com/udemy/8217/)Lenguajes de programación para Hacking \[+8hs\] 
* [REDEEM OFFER](https://idownloadcoupon.c
om/udemy/8216/)ChatGPT to Self Publish a Fiction Amazon KDP Romance Novel 
* [REDEEM OFFER](https://idownloadcoupon.com/
udemy/8215/)ChatGPT & CapCut Mastery: Faceless YouTube & Passive Income 
* [REDEEM OFFER](https://idownloadcoupon.com/ud
emy/8214/)226 ChatGPT Prompts: A-Z ChatGPT Prompt Engineering BootCamp 
* [REDEEM OFFER](https://idownloadcoupon.com/ude
my/8213/)10-in-1 Generative AI & ChatGPT Social Media Marketing 2024 
* [REDEEM OFFER](https://idownloadcoupon.com/udemy
/8212/)6-in-1 ClickFunnels & ChatGPT Powered Sales Funnel Mastery 
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/82
11/)Master Spring Data JPA with Hibernate: E-Commerce Project 
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8210/)
Flutter & Firebase: Build Your Own E-Commerce App 
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8209/)Kubernetes C
ompleto: Orquestração Docker + Projeto DevOps 
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8208/)2024 Vmware Spri
ng Professional Certification Test 2V0-72.22 
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8207/)Curso de Facebook
 para Negocios 2024 – Facebook Marketing 
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8206/)Curso de Outlook 2024
 (Hotmail) , ¡Desde Cero Hasta Experto! 
* Curso Blogger 2024: Cómo Crear un Blog Gratis Paso a Paso
* [REDEEM OFFER](ht
tps://idownloadcoupon.com/udemy/8205/)
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8204/)Curso de Google Drive 20
24, ¡Desde Cero Hasta Experto! 
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8203/)Master Software Dev: Leadership
, Decision-Making Skills 2023 
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8202/)Deep Dive into Clean Architectur
e in Flutter\[Arabic\] 
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8201/)Directorio de Plugins para WordPress 20
24 
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8200/)Mastering ChatGPT (AI) and PowerPoint presentation 
* [REDE
EM OFFER](https://idownloadcoupon.com/udemy/8199/)Presentation Skills: Give Great Skype Video Presentations 
* [REDEEM O
FFER](https://idownloadcoupon.com/udemy/8198/)Comprehensive DaVinci Resolve With Color Grading Masterclass 
* [REDEEM OF
FER](https://idownloadcoupon.com/udemy/8197/)SQL complete Bootcamp From Basics to Advanced,Sql interview 
* [REDEEM OFFE
R](https://idownloadcoupon.com/udemy/8196/)5700+ visualized English vocabulary 
* [REDEEM OFFER](https://idownloadcoupon
.com/udemy/8195/)OEE Overall Equipment Efficiency- Calculate Productivity 
* [REDEEM OFFER](https://idownloadcoupon.com/
udemy/8194/)Professional Diploma in Agile and Project Management 
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/819
3/)C# Unity Game using the Wax Blockchain 
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8192/)Cinema and the Psych
e: Creating Short Films in Art Therapy 
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8191/)Interpreting emotions a
nd memories in art 
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8190/)Art Therapy and Cognitive Behavioural Decli
ne 
* Art Therapy – in Ten Minutes (Two Instructors)
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8189/)
* [REDEEM
 OFFER](https://idownloadcoupon.com/udemy/8188/)BIM- Revit Structure Full Course- from Beginner to Advanced 
* [REDEEM O
FFER](https://idownloadcoupon.com/udemy/8187/)Professional Diploma in Branding & Brand Management 
* [REDEEM OFFER](http
s://idownloadcoupon.com/udemy/8186/)Asteroids with Python PyGame 
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/818
5/)Social Media Bots with Python 
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8184/)Personal Presentation Trainin
g 
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8183/)Complete Short Black Scholes Options Trading Pricing Course 

* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8182/)Complete Graphics Design Bootcamp Beginner to Advanced 
* [RED
EEM OFFER](https://idownloadcoupon.com/udemy/8181/)Public Speaking: Be a Professional Speaker 
* [REDEEM OFFER](https://
idownloadcoupon.com/udemy/8180/)Conference Calls-You Can Present Well On Any Conference Call 
* [REDEEM OFFER](https://i
downloadcoupon.com/udemy/8179/)Máster en Elementor 2024, ¡Desde Cero Hasta Experto! 
* [REDEEM OFFER](https://idownloadc
oupon.com/udemy/8178/)Oracle Java Certification Exam OCA 1Z0-808 Preparation Part1 
* [REDEEM OFFER](https://idownloadco
upon.com/udemy/8177/)Mini MBA in Entrepreneurship 
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8176/)Microsoft Ex
cel – Beginner to Advance with Example 
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8175/)Web3 Development Essent
ials 
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8174/)Mastering LangChain and AWS: A Guide to Economic Analysis
 
* Python Development Essentials
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8173/)
* [REDEEM OFFER](https://ido
wnloadcoupon.com/udemy/8172/)Fire Up Creativity in Your Child 
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8171/)
Curso de Hostinger 2024: El Hosting Ideal Para tu Página Web 
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8170/)C
ómo Crear una Tienda Online con WordPress y ChatGPT 2024 
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8169/)Cómo 
Crear una Página Web con WordPress y Elementor PRO 2024 
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8168/)Custom
er Experience Management – Foundation Course 
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8167/)SAP ABAP On HANA 

* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8166/)Javascript For Beginners Complete Course 
* [REDEEM OFFER](htt
ps://idownloadcoupon.com/udemy/8165/)Planning a workshop for the over 60s 
* [REDEEM OFFER](https://idownloadcoupon.com/
udemy/8164/)How not to lose your mind when you’ve lost your job! 
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/816
3/)The Complete Google Forms Course – Mastering Google Forms 
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8162/)G
MAT Focus | Quantitative| Master Math Course | 2024 Updated 
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8161/)SA
T Digital | Math Master Course | 2024 Updated | Target 800 
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8160/)Exc
el Charts & Graphs: Master Class Excel Charts & Graphs 
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8159/)The Com
plete SEO Guide: SEO For Beginner to Expert 2024 
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8158/)Microsoft Exc
el – Excel Course For Beginners 2024 

GET MORE FREE ONLINE COURSES WITH CERTIFICATE – [CLICK HERE](http://reddit.com/r/
udemyfreeebies/)
```
---

     
 
all -  [ List of FREE and Best Selling Discounted Courses ](https://www.reddit.com/r/udemyfreeebies/comments/1d92xb1/list_of_free_and_best_selling_discounted_courses/) , 2024-06-07-0955
```
# Udemy Free Courses for 06 June 2024

*Note : Coupons might expire anytime, so enroll as soon as possible to get the co
urses for FREE.*

* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8221/)  ChatGPT: Self-Publish an Amazon KDP Bestsel
ler Book in 24hrs 
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8220/)Aprende a programar en Perl desde 0 
* [REDE
EM OFFER](https://idownloadcoupon.com/udemy/8219/)Crea tu propia herramienta de Hacking en C básico y fácil 
* [REDEEM O
FFER](https://idownloadcoupon.com/udemy/8218/)Curso de ciberseguridad personal y corporativo 
* [REDEEM OFFER](https://i
downloadcoupon.com/udemy/8217/)Lenguajes de programación para Hacking \[+8hs\] 
* [REDEEM OFFER](https://idownloadcoupon
.com/udemy/8216/)ChatGPT to Self Publish a Fiction Amazon KDP Romance Novel 
* [REDEEM OFFER](https://idownloadcoupon.co
m/udemy/8215/)ChatGPT & CapCut Mastery: Faceless YouTube & Passive Income 
* [REDEEM OFFER](https://idownloadcoupon.com/
udemy/8214/)226 ChatGPT Prompts: A-Z ChatGPT Prompt Engineering BootCamp 
* [REDEEM OFFER](https://idownloadcoupon.com/u
demy/8213/)10-in-1 Generative AI & ChatGPT Social Media Marketing 2024 
* [REDEEM OFFER](https://idownloadcoupon.com/ude
my/8212/)6-in-1 ClickFunnels & ChatGPT Powered Sales Funnel Mastery 
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/
8211/)Master Spring Data JPA with Hibernate: E-Commerce Project 
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8210
/)Flutter & Firebase: Build Your Own E-Commerce App 
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8209/)Kubernetes
 Completo: Orquestração Docker + Projeto DevOps 
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8208/)2024 Vmware Sp
ring Professional Certification Test 2V0-72.22 
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8207/)Curso de Facebo
ok para Negocios 2024 – Facebook Marketing 
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8206/)Curso de Outlook 20
24 (Hotmail) , ¡Desde Cero Hasta Experto! 
* Curso Blogger 2024: Cómo Crear un Blog Gratis Paso a Paso
* [REDEEM OFFER](
https://idownloadcoupon.com/udemy/8205/)
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8204/)Curso de Google Drive 
2024, ¡Desde Cero Hasta Experto! 
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8203/)Master Software Dev: Leadersh
ip, Decision-Making Skills 2023 
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8202/)Deep Dive into Clean Architect
ure in Flutter\[Arabic\] 
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8201/)Directorio de Plugins para WordPress 
2024 
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8200/)Mastering ChatGPT (AI) and PowerPoint presentation 
* [RE
DEEM OFFER](https://idownloadcoupon.com/udemy/8199/)Presentation Skills: Give Great Skype Video Presentations 
* [REDEEM
 OFFER](https://idownloadcoupon.com/udemy/8198/)Comprehensive DaVinci Resolve With Color Grading Masterclass 
* [REDEEM 
OFFER](https://idownloadcoupon.com/udemy/8197/)SQL complete Bootcamp From Basics to Advanced,Sql interview 
* [REDEEM OF
FER](https://idownloadcoupon.com/udemy/8196/)5700+ visualized English vocabulary 
* [REDEEM OFFER](https://idownloadcoup
on.com/udemy/8195/)OEE Overall Equipment Efficiency- Calculate Productivity 
* [REDEEM OFFER](https://idownloadcoupon.co
m/udemy/8194/)Professional Diploma in Agile and Project Management 
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8
193/)C# Unity Game using the Wax Blockchain 
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8192/)Cinema and the Psy
che: Creating Short Films in Art Therapy 
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8191/)Interpreting emotions
 and memories in art 
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8190/)Art Therapy and Cognitive Behavioural Dec
line 
* Art Therapy – in Ten Minutes (Two Instructors)
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8189/)
* [REDE
EM OFFER](https://idownloadcoupon.com/udemy/8188/)BIM- Revit Structure Full Course- from Beginner to Advanced 
* [REDEEM
 OFFER](https://idownloadcoupon.com/udemy/8187/)Professional Diploma in Branding & Brand Management 
* [REDEEM OFFER](ht
tps://idownloadcoupon.com/udemy/8186/)Asteroids with Python PyGame 
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8
185/)Social Media Bots with Python 
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8184/)Personal Presentation Train
ing 
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8183/)Complete Short Black Scholes Options Trading Pricing Cours
e 
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8182/)Complete Graphics Design Bootcamp Beginner to Advanced 
* [R
EDEEM OFFER](https://idownloadcoupon.com/udemy/8181/)Public Speaking: Be a Professional Speaker 
* [REDEEM OFFER](https:
//idownloadcoupon.com/udemy/8180/)Conference Calls-You Can Present Well On Any Conference Call 
* [REDEEM OFFER](https:/
/idownloadcoupon.com/udemy/8179/)Máster en Elementor 2024, ¡Desde Cero Hasta Experto! 
* [REDEEM OFFER](https://idownloa
dcoupon.com/udemy/8178/)Oracle Java Certification Exam OCA 1Z0-808 Preparation Part1 
* [REDEEM OFFER](https://idownload
coupon.com/udemy/8177/)Mini MBA in Entrepreneurship 
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8176/)Microsoft 
Excel – Beginner to Advance with Example 
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8175/)Web3 Development Esse
ntials 
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8174/)Mastering LangChain and AWS: A Guide to Economic Analys
is 
* Python Development Essentials
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8173/)
* [REDEEM OFFER](https://i
downloadcoupon.com/udemy/8172/)Fire Up Creativity in Your Child 
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8171
/)Curso de Hostinger 2024: El Hosting Ideal Para tu Página Web 
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8170/
)Cómo Crear una Tienda Online con WordPress y ChatGPT 2024 
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8169/)Cóm
o Crear una Página Web con WordPress y Elementor PRO 2024 
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8168/)Cust
omer Experience Management – Foundation Course 
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8167/)SAP ABAP On HAN
A 
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8166/)Javascript For Beginners Complete Course 
* [REDEEM OFFER](h
ttps://idownloadcoupon.com/udemy/8165/)Planning a workshop for the over 60s 
* [REDEEM OFFER](https://idownloadcoupon.co
m/udemy/8164/)How not to lose your mind when you’ve lost your job! 
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8
163/)The Complete Google Forms Course – Mastering Google Forms 
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8162/
)GMAT Focus | Quantitative| Master Math Course | 2024 Updated 
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8161/)
SAT Digital | Math Master Course | 2024 Updated | Target 800 
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8160/)E
xcel Charts & Graphs: Master Class Excel Charts & Graphs 
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8159/)The C
omplete SEO Guide: SEO For Beginner to Expert 2024 
* [REDEEM OFFER](https://idownloadcoupon.com/udemy/8158/)Microsoft E
xcel – Excel Course For Beginners 2024 

GET MORE FREE ONLINE COURSES WITH CERTIFICATE – [CLICK HERE](https://idownloadc
oupon.com/)
```
---

     
 
all -  [ [0 YOE] New Grad seeking feedback and trying to get more interviews for Full-Time Software Related P ](https://www.reddit.com/r/EngineeringResumes/comments/1d924e4/0_yoe_new_grad_seeking_feedback_and_trying_to_get/) , 2024-06-07-0955
```
Hello! I am a recent Computer Science graduate interested mainly in Software Engineering (but with the current market I 
have branched out to anything remotely relevant). I have applied to 200-300 positions in the past few months and have on
ly gotten interviews/phone calls with a couple of training/staffing-style companies (Revature, Quintrix, Actalent, Brook
source, etc) which is not ideal. A few of them told me they would be in contact with me later on as I asked for July sta
rt dates but I am still waiting for them to reach out again. 

My main concerns with my resume include formatting and th
e wording of my bullets. However, any pointers at all would be greatly appreciated. Thank you.

https://preview.redd.it/
23qeifb1st4d1.png?width=5100&format=png&auto=webp&s=25188fa17c24a4ee9ebdb7489cb9db7de1403411
```
---

     
 
all -  [ How does function calling work under the hood? ](https://www.reddit.com/r/LangChain/comments/1d8y7mq/how_does_function_calling_work_under_the_hood/) , 2024-06-07-0955
```
I would like to understand how a model is returning the right tool to call for a query, what's happening behind the api 
call for function calling for open ai, mistral and other models.

Are they using a prompt with instructions on how selec
t the right function to call? and when tools and query is passed via api, is the llm using that prompt to select the too
l or what's happening behind the call.

How do I achieve function calling using a open source model that I run locally u
sing ollama. Thanks.
```
---

     
 
all -  [ Clustering through prompting  ](https://www.reddit.com/r/LangChain/comments/1d8w8am/clustering_through_prompting/) , 2024-06-07-0955
```
Group below data type items into very tight semantic groups.
Only group items together if they have exact semantic meani
ng or  can be used interchangably with each other. Break data types into maximum groups as possbile.
Return the groups i
n JSON format, ensuring that each key is exact to all the items in its list. Do not alter any characters.

Here is the l
ist of words:

['email_addr', 'email', 'email_address', 'address', 'email id', 'gmail', 'text', 'financial info', 'credi
t card number', 'cvv number', 'email address', 'eemmail', 'contact info', 'electronic mail', 'first', 'first_name', 'las
t name', 'bank details', 'firstName', 'christianName', 'christian_name', 'name', 'creadit card info', 'gsheets', 'google
 sheets', 'sheets', 'password', 'atm pin', 'atm card number', 'login details', 'vericyy', 'vericy', 'vericy.ai']

I used
 llama3 70b from groq.com

This yields average results but atleast better than hierarchical clustering with openai embed
dings.
 
What other methods beside zeronshot prompting can improve the clusters/groups while keeping costs to the minimu
m??
```
---

     
 
all -  [ Boost Your Skills: 100 Free Certified Courses on Udemy ](https://www.reddit.com/r/Udemy/comments/1d8vdsq/boost_your_skills_100_free_certified_courses_on/) , 2024-06-07-0955
```
Introduction to Human Resources Management

https://courze.org/introduction-to-human-resources-management/



SAP ABAP O
n HANA

https://courze.org/sap-abap-on-hana/



Curso de Hostinger 2024: El Hosting Ideal Para tu Página Web

https://co
urze.org/curso-de-hostinger-2023-el-hosting-ideal-para-tu-pagina-web/



Python Development Essentials

https://courze.o
rg/python-development-essentials/



Máster en Elementor 2024, ¡Desde Cero Hasta Experto!

https://courze.org/master-en-
elementor-2023-desde-cero-hasta-experto/



Cómo Crear una Página Web con WordPress y Elementor PRO 2024

https://courze
.org/como-crear-una-pagina-web-con-wordpress-y-elementor-pro-2023/



Cómo Crear una Tienda Online con WordPress y ChatG
PT 2024

https://courze.org/como-crear-una-tienda-online-con-wordpress-y-chatgpt-2023/



Directorio de Plugins para Wor
dPress 2024

https://courze.org/directorio-de-plugins-para-wordpress/



Javascript For Beginners Complete Course

https
://courze.org/javascript-for-beginners-complete-course/



Ethically Hack the Planet Part 1

https://courze.org/ethicall
y-hack-the-planet-part-1/



Mini MBA in Entrepreneurship

https://courze.org/mini-mba-in-entrepreneurship/



Mastering
 ChatGPT (AI) and PowerPoint presentation

https://courze.org/mastering-chatgpt-ai-and-powerpoint-presentation/



How t
o Build a Successful Amazon Self-Publishing Business

https://courze.org/how-to-build-a-successful-amazon-self-publishin
g-business/



Fire Up Creativity in Your Child

https://courze.org/fire-up-creativity-in-your-child/



Udemy Online Co
urse Creation For Passive Income (Unofficial)

https://courze.org/udemy-online-course-creation-for-passive-income-unoffi
cial/



Nifty and Bank Nifty Strategies नियमित आय के लिए

https://courze.org/nifty-and-bank-nifty-strategies-%e0%a4%a8%
e0%a4%bf%e0%a4%af%e0%a4%ae%e0%a4%bf%e0%a4%a4-%e0%a4%86%e0%a4%af-%e0%a4%95%e0%a5%87-%e0%a4%b2%e0%a4%bf%e0%a4%8f/



Activ
e Listening with Curiosity

https://courze.org/active-listening-with-curiosity/



Web3 Development Essentials

https://
courze.org/web3-development-essentials/



Beginning Bash Scripting

https://courze.org/beginning-bash-scripting/



Lin
ux Desktop Automation

https://courze.org/linux-desktop-automation/



Android Malware Analysis

https://courze.org/andr
oid-malware-analysis/



Social Media Bots with Python

https://courze.org/social-media-bots-with-python/



Asteroids w
ith Python PyGame

https://courze.org/asteroids-with-python-pygame/



Make Simple Games with Python

https://courze.org
/make-simple-games-with-python/



Learn PHP and MySQL for Web Application and Web Development

https://courze.org/learn
-php-and-mysql-for-web-application-and-web-development/



Mastering LangChain and AWS: A Guide to Economic Analysis

ht
tps://courze.org/mastering-langchain-and-aws-a-guide-to-economic-analysis/



Learn Blockchain and Cryptocurrency from B
eginning

https://courze.org/learn-blockchain-and-cryptocurrency-from-beginning/



Mini MBA in Innovations and Digital 
Transformation

https://courze.org/mini-mba-in-innovations-and-digital-transformation/



The ChatGPT, SEO, Social Media
, & Digital Marketing Course

https://courze.org/the-chatgpt-seo-social-media-digital-marketing-course/



Adobe Premier
e Pro Advanced Video Editing Course

https://courze.org/adobe-premiere-pro-advanced-video-editing-course/



Public Spea
king: You Can be a Great Speaker within 24 Hours

https://courze.org/public-speaking-you-can-be-a-great-speaker-within-2
4-hours/



Investor Pitching: Presentations for Startup Capital

https://courze.org/investor-pitching-presentations-for
-startup-capital/



Media Training -Radio: How to Speak Effectively on the Radio

https://courze.org/media-training-rad
io-how-to-speak-effectively-on-the-radio/



Podcasting: How to Speak Effectively on Your Own Podcast

https://courze.or
g/podcasting-how-to-speak-effectively-on-your-own-podcast/



Time Management Public Speaking – Drastically Reduce Prep


https://courze.org/time-management-public-speaking-drastically-reduce-prep/



Presentation Skills: Give a Great Team P
resentation

https://courze.org/presentation-skills-give-a-great-team-presentation/



Storytelling: You Can learn to Te
ll Stories Effectively

https://courze.org/storytelling-you-can-learn-to-tell-stories-effectively/



Public Speaking: E
ulogy-Give a Great Eulogy For Loved Ones

https://courze.org/public-speaking-eulogy-give-a-great-eulogy-for-loved-ones/




Presentation Skills: Insurance Your Next Speech Will be Good

https://courze.org/presentation-skills-insurance-your-n
ext-speech-will-be-good/



Public Speaking for People Who Hate Public Speaking

https://courze.org/public-speaking-for-
people-who-hate-public-speaking/




```
---

     
 
all -  [ vectorstores vs 2d matrix for retrieval ](https://www.reddit.com/r/LangChain/comments/1d8uwcn/vectorstores_vs_2d_matrix_for_retrieval/) , 2024-06-07-0955
```
I have been doing retrieval by stacking vectors into a 2d matrix. To find similar documents, I multiply the 2d matrix by
 the other vector to find the highest similarity index. I then use that index to find the document.

I am currently plan
ning to use embedded vectors for retrieval only. Is there an advantage of using vectorstores?
```
---

     
 
all -  [ RAG: How to answer 'give me all...' question ](https://www.reddit.com/r/LangChain/comments/1d8uj3o/rag_how_to_answer_give_me_all_question/) , 2024-06-07-0955
```
I am creating a RAG application but I am having this problem:

I have multiple files containing the companies projects l
ists along with their descriptions, used frameworks etc.

The type of question I want an answer for is: 'Give me all the
 projects built using FastAPI' (as an example)

I am limited by top\_k variable which means I do not  get all the projec
ts,

How would you solve this.

Thank you all

Edit: The information is in a corpus of text, nothing structured  unfortu
nately.
```
---

     
 
all -  [ LangGraph DeepLearning Class ](https://www.reddit.com/r/LangChain/comments/1d8trdx/langgraph_deeplearning_class/) , 2024-06-07-0955
```
Today we released a DeepLearning class on LangGraph! [https://www.deeplearning.ai/short-courses/ai-agents-in-langgraph/]
(https://www.deeplearning.ai/short-courses/ai-agents-in-langgraph/)

I'm really excited about this (and wanted to share 
it here) for a few reasons. First, I'm incredbily bullish on LangGraph. We're investing a lot in and seeing really good 
usage (including more questions about it here!). Second - the DeepLearning team is fantastic and the material we put tog
ether with them is always top notch

I hope people have some time to watch and try it out. As mentioned, we're doing a b
it push on LangGraph over the next month, and so if people have comments/feedback/questions I'd love to hear!
```
---

     
 
all -  [ What should be my annual Appraisal for my profile as RnD Engineer? ](https://www.reddit.com/r/developersIndia/comments/1d8susw/what_should_be_my_annual_appraisal_for_my_profile/) , 2024-06-07-0955
```
Hello

So I recently got my appraisal of 6k in my monthly salary. My previous monthly salary was 23.4k CTC and after app
raisal it is 27.5k,

I told my manager that I am not satisfied with this and he told me to do some research on what is t
he current market rate for my profile and experience.

As I am not into any niche, I am confused what should be my appra
isal amount.

My profile:

I work as RnD engineer in my company. I do research on upcoming projects and develop POCs. Ho
wever, currently the software we work on is in POC stage so I work on POC but I am supposed to make it production ready 
when client is ready to buy it.

Up until now, I have worked on Azure cloud (ADF, Entra ID, Functions), Power BI (Embedd
ed reports in our custom web app) and Generative AI projects (SQL and Document chatbot). And many other research work an
d documentations.

My tech skills: Python, Generative AI (openAI API), Langchain, Azure cloud services. I also cleared A
Z-900 certificate while working here.

I have 2 years of experience working here. Started with 20k monthly CTC.

Conside
ring my profile, can you please guide me what should be my ask for my annual appraisal?

Thank you
```
---

     
 
all -  [ What should be my annual appraisal for my profile? ](https://www.reddit.com/r/careerguidance/comments/1d8sref/what_should_be_my_annual_appraisal_for_my_profile/) , 2024-06-07-0955
```
Hello

So I recently got my appraisal of 6k in my monthly salary. My previous monthly salary was 23.4k CTC and after app
raisal it is 27.5k,

I told my manager that I am not satisfied with this and he told me to do some research on what is t
he current market rate for my profile and experience.

As I am not into any niche, I am confused what should be my appra
isal amount.

My profile:

I work as RnD engineer in my company. I do research on upcoming projects and develop POCs.

U
p until now, I have worked on Azure cloud (ADF, Entra ID, Functions), Power BI (Embedded reports in our custom web app) 
and Generative AI projects (SQL and Document chatbot). And many other research work and documentations.

My tech skills:
 Python, Generative AI (openAI API), Langchain, Azure cloud services. I also cleared AZ-900 certificate while working he
re.

I have 2 years of experience working here. Started with 20k monthly CTC.

Considering my profile, can you please gu
ide me what should be my ask for my annual appraisal?

Thank you
```
---

     
 
all -  [ Best open source models to build complex agents: ](https://www.reddit.com/r/LangChain/comments/1d8ri4z/best_open_source_models_to_build_complex_agents/) , 2024-06-07-0955
```
Hello Langchain community,

I wanted to ask, based on your experience, what are the best open-source LLMs I can use to b
uild complex agents? I've built an agent based on GPT-3.5, and it works fine, but now I want to migrate to open-source m
odels. I've tried Llama3 8B, but it doesn't seem to work very well. Could you please suggest a list based on performance
 and GPU cost?

Thank you!
```
---

     
 
all -  [ How to get started with the problem statement? ](https://www.reddit.com/r/LangChain/comments/1d8pug0/how_to_get_started_with_the_problem_statement/) , 2024-06-07-0955
```
Hey guys, i am new to generative AI, it’s been a few days learning new things. I have a problem statement in hand. We ha
ve to evaluate a startup idea. We already have an evaluation checklist that has like 30 parameters on the basic of which
 we decide the feasibility of the idea. We have to build a model in which we prompt an idea and the input idea goes thro
ugh various agents who are (business analysts, cofounder, VC). So it first goes to BA and then the result goes to cofoun
der and so on therefore getting perspective of all the agents. For starters i want to build the model with 3 agents. Onc
e it passes through 3rd agent it gives the final result as an evaluation checklist (the same one i talked about above). 


Now my question is how should i approach this problem and what would be the underlying concept used for building such 
a model? 
Also from where can i start ? 
FYI - i read a bit about genertive ai topics like embedding, fine tuning and a 
bit of langchain (built a simple agent) etc. Still exploring agentic AI. 

Thanks in advance !! 
```
---

     
 
all -  [ Long Running Toolkits ](https://www.reddit.com/r/LangChain/comments/1d8p5c5/long_running_toolkits/) , 2024-06-07-0955
```
One thing I notice isn't discussed is the recoveries for failures on tools that require external connections, when in a 
long-running environment.

For example, the SQLToolKit that uses SQL Alchemy to connect to the database. 

Eventually, y
ou just get a 'The database connection has been terminated.' Error, and there's nothing built-in my default in any examp
les to account for things like these.

How would one suggest another goes about managing this, and things like these?
```
---

     
 
all -  [ Chatbot and Text Generator with Mistral/LLAMA3+Ollama+Gradio+Langchain ](https://www.reddit.com/r/LangChain/comments/1d8n48v/chatbot_and_text_generator_with/) , 2024-06-07-0955
```
I would like to install a chatbot/text generator on my Macmini for various uses: structured text generator from user-pro
vided notes and a relative chatbot for consulting the generated texts.
```
---

     
 
all -  [ Why is llamaindex faster than langchain? ](https://www.reddit.com/r/LangChain/comments/1d8le7w/why_is_llamaindex_faster_than_langchain/) , 2024-06-07-0955
```
In some tutorial that I saw online, it was mentioned that llama-index is faster than langchain when it comes to indexing
 the documents. Can someone explain me why this is the case and what does Ilamaindex use which makes it faster than lang
chain?
```
---

     
 
all -  [ Why is llamaindex faster? ](https://www.reddit.com/r/LlamaIndex/comments/1d8ldkl/why_is_llamaindex_faster/) , 2024-06-07-0955
```
In some tutorial that I saw online, it was mentioned that llama-index is faster than langchain when it comes to indexing
 the documents. Can someone explain me why this is the case and what does llamaindex use which makes it faster than lang
chain?
```
---

     
 
all -  [ The Easiest Way to Build and Deploy Generative AI Applications ](https://www.reddit.com/r/AnyBodyCanAI/comments/1d8l3wj/the_easiest_way_to_build_and_deploy_generative_ai/) , 2024-06-07-0955
```
I wanted to share my experience with a new framework I've been using called **Lyzr**, which has completely transformed t
he way I build and deploy Generative AI applications. If you're familiar with Langchain or DSPy, you'll appreciate how L
yzr's user-friendly design and unique approach make it stand out.
```
---

     
 
all -  [ The Easiest Way to Build and Deploy Generative AI Applications
 ](https://www.reddit.com/r/u_harshit_nariya/comments/1d8kwbl/the_easiest_way_to_build_and_deploy_generative_ai/) , 2024-06-07-0955
```
I wanted to share my experience with a new framework I've been using called **Lyzr**, which has completely transformed t
he way I build and deploy Generative AI applications. If you're familiar with Langchain or DSPy, you'll appreciate how L
yzr's user-friendly design and unique approach make it stand out.
```
---

     
 
all -  [ How to get access of sessionId and other params which are passed in a config inside the tool of a la ](https://www.reddit.com/r/LangChain/comments/1d8innr/how_to_get_access_of_sessionid_and_other_params/) , 2024-06-07-0955
```
I am using Langserve to create a langchain agent with tool calling. Till now all is working as expected and I am able to
 host it in AWS ECS with CDK also and learnt a lot in the process. But one thing I am stuck, in my chat, users will give
 their phone number and I will store the user as a lead in a crm I built using mongoDB. However, in the crm I want to sh
ow the chat history also.

For the chat history, I am using the mongodb integration and its working as expected when I p
ass the sessionId in the api calls.

Now I want to create a tool say \`save\_user\` which will take the phone number as 
input. I tested dummy tool calls and its working. but in the save\_user function, I want to save the phone number and th
e associated sessionId. I did not find any documentation or tutorial on how to achieve this.

This is the tool



    @t
ool('save_user', args_schema=getUserInfoInput)
    def save_user(phone :str) -> dict:
        '''Save the user detail'''

        # I want the session_id of the chat here
        return



here is the tentative code I was using



    # #!/u
sr/bin/env python
    from fastapi import FastAPI
    from langchain.agents import AgentExecutor
    from langchain.agen
ts.format_scratchpad.openai_tools import (
        format_to_openai_tool_messages,
    )
    from langchain.agents.outpu
t_parsers.openai_tools import OpenAIToolsAgentOutputParser
    from langchain_core.prompts import ChatPromptTemplate, Me
ssagesPlaceholder
    from langchain_core.tools import tool
    from langchain_openai import ChatOpenAI
    from langser
ve import add_routes
    from langserve.pydantic_v1 import BaseModel, Field
    from langchain_core.runnables.history im
port RunnableWithMessageHistory
    from langchain_mongodb.chat_message_histories import MongoDBChatMessageHistory
    f
rom langchain_openai import ChatOpenAI
    from langchain.agents import tool
    import os
    from pinecone import Pine
cone
    from algoliasearch.search_client import SearchClient
    import openai
    import json
    from langchain_core.
prompts import ChatPromptTemplate, MessagesPlaceholder
    from langchain.agents import AgentExecutor
    from typing im
port Any
    from fastapi.middleware.cors import CORSMiddleware
    
    pinecone_client = Pinecone(api_key=os.environ['
PINECONE_API_KEY'])
    pc_index = pinecone_client.Index(os.environ['PINECONE_INDEX'])
    algolia_client = SearchClient
.create(os.environ['ALGOLIA_APPLICATION_ID'], os.environ['ALGOLIA_API_KEY'])
    alg_index = algolia_client.init_index(o
s.environ['ALGOLIA_INDEX'])
    openai_client = openai.OpenAI(api_key=os.environ['OPENAI_API_KEY'])
    
    class getIn
foInput(BaseModel):
        food: str = Field(description='name of the food')
    
    @tool('get_food_price', args_sche
ma=getInfoInput)
    def get_food_price(food :str) -> dict:
        '''Return cost of a food'''
        # ideally this w
ill call algolia and pinecone to do the search
        # but for this case, it does not matter
        return 100
    to
ols = [get_food_price]
    
    class getUserInfoInput(BaseModel):
        phone: str = Field(description='Users phone n
umber')
    
    @tool('save_user', args_schema=getUserInfoInput)
    def save_user(phone :str) -> dict:
        '''Save
 the user detail'''
        # I want the session_id of the chat here
        return
    
    tools = [get_food_price, sa
ve_user]
    
    system_prompt = '''
    You are a waiter named Mia, People ask you about price of food and you reply
 
   '''
    
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                'system',
           
     system_prompt,
            ),
            MessagesPlaceholder(variable_name='chat_history'),
            ('user', '
{input}'),
            MessagesPlaceholder(variable_name='agent_scratchpad'),
        ]
    )
    
    llm = ChatOpenAI(
model='gpt-3.5-turbo', temperature=0, streaming=True)
    llm_with_tools = llm.bind_tools(tools)
    
    agent = (
    
    {
            'input': lambda x: x['input'],
            'agent_scratchpad': lambda x: format_to_openai_tool_message
s(
                x['intermediate_steps']
            ),
            'chat_history': lambda x: x['chat_history'],
     
   }
        | prompt
        | llm_with_tools
        | OpenAIToolsAgentOutputParser()
    )
    
    agent_executor = 
AgentExecutor(agent=agent, tools=tools, verbose=True)
    
    
    agent_with_chat_history = RunnableWithMessageHistory
(
        agent_executor,
        # This is needed because in most real world scenarios, a session id is needed
        
# It isn't really used here because we are using a simple in memory ChatMessageHistory
        lambda session_id: MongoD
BChatMessageHistory(
            session_id=session_id,
            connection_string=os.environ['MONGO_CONNECTION_STRIN
G'],
            database_name=os.environ['MONGO_DB'],
            collection_name=os.environ['MONGO_COLLECTION'],
     
   ),
        input_messages_key='input',
        history_messages_key='chat_history',
    )
    
    
    app = FastAPI
(
        title='LangChain Server',
        version='1.0',
        description='Spin up a simple api server using LangCh
ain's Runnable interfaces',
    )
    
    class Input(BaseModel):
        input: str
        # The field extra defines 
a chat widget.
        # Please see documentation about widgets in the main README.
        # The widget is used in the 
playground.
        # Keep in mind that playground support for agents is not great at the moment.
        # To get a bet
ter experience, you'll need to customize the streaming output
        # for now.
    
    
    class Output(BaseModel):

        output: Any
    
    add_routes(
        app,
        agent_with_chat_history.with_types(input_type=Input, outpu
t_type=Output).with_config(
            {'run_name': 'agent'}
        ),
    )
    
    # For health check, otherwise th
is will return 404
    u/app.get('/')
    def get_root():
        return {'message': 'FastAPI running in a Docker contai
ner'}
    
    
    # Set all CORS enabled origins
    app.add_middleware(
        CORSMiddleware,
        allow_origins
=['*'],
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*'],
        expose_headers
=['*'],
    )
    
    if __name__ == '__main__':
        import uvicorn
    
        uvicorn.run(app, host='localhost',
 port=8000)
```
---

     
 
all -  [ Learnings from doing Evaluations for LLM powered applications ](https://www.reddit.com/r/LangChain/comments/1d8euoz/learnings_from_doing_evaluations_for_llm_powered/) , 2024-06-07-0955
```
Learnings from doing Evaluations for LLM powered applications from my experience building with LLMs in the last few mont
hs:  
  
**Evaluations for LLM powered applications is different from Model Evaluation leaderboards like Huggingface Ope
n LLM leaderboard**  
  
If you are an enterprise leveraging or looking to leverage  LLMs, spend very little time on mod
el evaluation leaderboards. Pick the most powerful model to start with and invest in evaluating LLM responses in the con
text of your product and usecase.  
  
**Know your metrics**  
  
Ultimately what matters is whether your users are gett
ing high quality product experience. This means it's super important to look at your specific use case and determine the
 metrics that are best suited for your product.  
  
Are you building a  
  
- summarization tool? Manually evaluate the
 results and come up with your own thesis of what a good summary should look like that will solve the your user's pain p
oint.  
  
- customer support agent chatbot? Look at a few responses and figure out what you care about the most and tra
nslate those to measurable metrics.  
  
Its important to keep things simple and hyper optimize for your use case before
 jumping into measuring all the metrics that you found on the internet.  
  
**Write unit tests to capture basic asserti
ons**  
  
Basic assertions includes things like,  
- looking for a specific word in every response.  
- making sure the
 generated response obeys a specific word count.  
- making sure the generated response costs less than $ x and uses les
s than n tokens.  
  
These kinds of unit tests act as a first line of defence and will help you catch the basic issues 
quickly. If you are using python, you can use pytest to write these simple unit tests. There is no need to buy or adopt 
any fancy tools for this.  
  
**Use LLMs to evaluate the outputs**  
  
One of the popular approaches these days is to 
use a more powerful LLM to evaluate(or)grade the output of the LLM in use. This approach works well if you clearly know 
what metrics you care about which are often a bit subjective and specific to your use case.  
  
The first step here is 
to identify a prompt that can be used for running a powerful LLM to grade the outputs.   
  
There are nice opensource t
ools like Promptfoo and Inspect AI which already has built in support for model graded evaluations and unit tests which 
can be used as for starters.  
  
**Collect User Feedback**  
  
This is easier said than done. Especially for new produ
cts where there is not enough users to get quality feedback from to start with. But its important to make contact with r
eality as quickly as possible and get creative around getting this feedback - Ex: using it yourself, asking your network
, friends and family to use it etc.  
  
The goal here is to set up a system where you can diligently track the feedback
 and constantly tweak and iterate on the quality of the outputs. Establishing this feedback loop is extremely important.
  
  
**Look at your data**  
  
No matter how many charts and visualizations you can create on top of your data, there 
is no proxy to looking at your data - both test and production data. In some cases, it may not be possible to do this wh
en you are operating in a highly secure/private environment. But, you need to figure out a way to collect and look at al
l the LLM generations closely, especially in the early days. This will inform not just the quality of the outputs the us
ers are experiencing, but also push you in the direction of identifying what metrics actually make sense for your use ca
se.  
  
**Manually Evaluate**  
  
LLM based evaluations are not fool proof and you need to tweak and improve the promp
ts and grading scale continuously based on data. And the way to collect this data is by manually evaluating the outputs 
yourself. This will help you understand how far apart LLM evals is drifting from the real criteria that you want to eval
uate against. It's important to measure this drift and make sure LLM evals track closely with manual evals at most times
.  
  
**Save your model parameters**  
  
Saving the model parameters you are using and tracking the responses along wi
th the model parameters will help you with measuring the quality your product for that specific set of model parameters.
 This becomes useful when you are noticing a regression in the quality of when you are upgrading to a new model version 
or swapping out to a completely different model.  
  
Leave your thoughts. I would love to hear about your experience ma
naging your LLM powered product in terms of quality and accuracy. Also, I am also building a fully open source and open 
telemetry based tool called Langtrace AI to basically solve for the above problems.  It's super easy to setup with just 
2 lines of code. Do check it out if you are interested.
```
---

     
 
all -  [ Using LangChain on Cloudflare ](https://www.reddit.com/r/CloudFlare/comments/1d8cnr0/using_langchain_on_cloudflare/) , 2024-06-07-0955
```
I spent the afternoon figuring out how to make Langchain work on a Cloudflare worker and wrote up my findings in case an
yone is looking to do the same.

Specifically, I wanted to use the PDF loader and recursive character text splitter func
tionality. The text splitter works fine, but the PDF loader has dependencies that don't run on workers.

I almost wrote 
the PDF extractor from scratch when I found a library that does exactly that. It takes a PDF or URL from a PDF and extra
cts its contents.

You can use the regular recursive character text splitter functionality with the extracted text. See 
the code snippet below.

If you are building a chatbot based on PDFs, this will come in handy. Anywho I hope this helps 
at least one person not go down the rabbit hole I just did! 

[PDF Library](https://github.com/unjs/unpdf)

**Code**

  
  import { extractText, getDocumentProxy } from 'unpdf';
    import { Document } from 'langchain/document';
    import {
 RecursiveCharacterTextSplitter } from 'langchain/text_splitter';
    
    export default {
        async fetch(request:
 Request, env: Env, ctx: ExecutionContext): Promise<Response> {
            const buffer = await fetch(
                
'https://www.cloudflare.com/resources/assets/slt3lc6tev37/3HWObubm6fybC0FWUdFYAJ/5d5e3b0a4d9c5a7619984ed6076f01fe/Cloudf
lare_for_Campaigns_Security_Guide.pdf',
            ).then((res) => res.arrayBuffer());
    
            const pdf = awa
it getDocumentProxy(new Uint8Array(buffer));
            // Extract text from PDF
            const { totalPages, text }
 = await extractText(pdf, { mergePages: true });
    
            const splitter = new RecursiveCharacterTextSplitter({

                chunkSize: 1000,
                chunkOverlap: 100,
            });
    
            const docOutput = a
wait splitter.splitDocuments([
                new Document({ pageContent: text }),
            ]);
    
            con
sole.log(docOutput)
    
    
            return new Response('done');
        },
    };
```
---

     
 
all -  [ Struggling with Pinecone Retrieval Performance? Need Help with LCEL Chains! ](https://www.reddit.com/r/LangChain/comments/1d8b1k5/struggling_with_pinecone_retrieval_performance/) , 2024-06-07-0955
```
Hey, I have a Pinecone namespace with multiple documents, but as the number of documents increases, my retrieval perform
ance is getting worse. I’m thinking of creating multiple retrievers that filter by document name to get relevant chunks 
from each document. I'm struggling to create an LCEL chain to achieve this. Does anyone know how to do this?
```
---

     
 
MachineLearning -  [ [P] Superfast RAG: Langchain Streaming and Groq ](https://www.reddit.com/r/MachineLearning/comments/1d5s9g4/p_superfast_rag_langchain_streaming_and_groq/) , 2024-06-07-0955
```
  
Fast LLM RAG inference using Groq and Langchain Streaming.  
  
Groq is introducing a new, simpler processing archite
cture designed specifically for the performance requirements of machine learning applications and other compute-intensiv
e workloads. The simpler hardware also saves developer resources by eliminating the need for profiling, and also makes i
t easier to deploy AI solutions at scale.  
  
Resource: [https://www.youtube.com/watch?v=frMdOL8knqg](https://www.youtu
be.com/watch?v=frMdOL8knqg)
```
---

     
 
MachineLearning -  [ [R] Building an Observable arXiv RAG Chatbot with LangChain, Chainlit, and Literal AI ](https://www.reddit.com/r/MachineLearning/comments/1crwh0q/r_building_an_observable_arxiv_rag_chatbot_with/) , 2024-06-07-0955
```
Hey r/MachineLearning, I published a new article where I built an observable semantic research paper application.

This 
is an extensive tutorial where I go in detail about:

1. Developing a RAG pipeline to process and retrieve the most rele
vant PDF documents from the arXiv API.
2. Developing a Chainlit driven web app with a Copilot for online paper retrieval
.
3. Enhancing the app with LLM observability features from Literal AI.

You can read the article here: [https://medium.
com/towards-data-science/building-an-observable-arxiv-rag-chatbot-with-langchain-chainlit-and-literal-ai-9c345fcd1cd8](h
ttps://medium.com/towards-data-science/building-an-observable-arxiv-rag-chatbot-with-langchain-chainlit-and-literal-ai-9
c345fcd1cd8)

Code for the tutorial: [https://github.com/tahreemrasul/semantic\_research\_engine](https://github.com/tah
reemrasul/semantic_research_engine)


```
---

     
 
MachineLearning -  [ [P] LLMinator: A Llama.cpp + Gradio based opensource Chatbot to run llms locally(cpu/cuda) directly  ](https://www.reddit.com/r/MachineLearning/comments/1cpbgd1/p_llminator_a_llamacpp_gradio_based_opensource/) , 2024-06-07-0955
```
Hi I am currently working on a context-aware streaming chatbot based on Llama.cpp, Gradio, Langchain, Transformers. LLMi
nator can pull LLMs directly from HF & run them locally on cuda or cpu.

I am looking for recommendations & help from op
ensource community to grow this further.

**Github Repo:** [https://github.com/Aesthisia/LLMinator](https://github.com/A
esthisia/LLMinator)

**Goal:** To help developers with kickstarter code/tool to run LLMs.

https://preview.redd.it/fnzja
7rjwqzc1.png?width=1846&format=png&auto=webp&s=a62c43614d63e82156fef8722b986b051cc1795b

**Features:**

* Context-aware 
Chatbot.
* Inbuilt code syntax highlighting.
* Load any LLM repo directly from HuggingFace.
* Supports both CPU & Cuda m
odes.
* Load & Offload saved models.
* Command Line Args
* API Access(Soon to be available)

Any review or feedback is a
ppreciated.
```
---

     
