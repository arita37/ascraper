 
all -  [ Is there a way to force the prebuilt react agent to call tools (vector store) for each question aske ](https://www.reddit.com/r/LangChain/comments/1e9sc59/is_there_a_way_to_force_the_prebuilt_react_agent/) , 2024-07-23-0911
```
I noticed that it didn't always call the vectorstore when asked a q- and for those answers it was always giving generic 
answers

react agent documentation: [https://langchain-ai.github.io/langgraph/how-tos/create-react-agent/#code](https://
langchain-ai.github.io/langgraph/how-tos/create-react-agent/#code)
```
---

     
 
all -  [ Langchain chatbot integration in Laravel ](https://www.reddit.com/r/LangChain/comments/1e9s7iw/langchain_chatbot_integration_in_laravel/) , 2024-07-23-0911
```
I am developing a chatbot app where I am using Langchain to feed it documents. I have completed the backend logic for th
e app, including controllers, tables and real-time chat (using pusher) in Laravel. I plan to use Flutter for the fronten
d. How can I integrate the model in Laravel?
```
---

     
 
all -  [ Who is using nextjs for their RAG? ](https://www.reddit.com/r/LangChain/comments/1e9mhmn/who_is_using_nextjs_for_their_rag/) , 2024-07-23-0911
```
1. Nextjs / React
2. Streamit
3. Python/Django/Flask

What do you use?
```
---

     
 
all -  [ How to achieve consistency in formatting? ](https://www.reddit.com/r/LangChain/comments/1e9meao/how_to_achieve_consistency_in_formatting/) , 2024-07-23-0911
```
We use json formatted output from OpenAIs GPT-4o.
We have a rather (single) big prompt for table extraction.

What are y
our approaches to achieve consistency in formatting.. especially regarding punctuation of numbers when processing variou
s language formats like Englisch, French, German, Polish, Chinese

Example:

Task 1
Extract all unit prices for all line
 items and return them as an array where each value is formatted as double (xxx.xx)

Task 2
Extract all quantities for a
ll line items and return them as an array where each value is formatted as double (xxx.xx)

Task 3
..


Problem is:
when
 doing this for multiple parts of the table in a single prompt, the formatting gets messed up.


```
---

     
 
all -  [ Looking For a Passionate Collabrator(s)/Fresher Backend Devleoper ](https://www.reddit.com/r/developersIndia/comments/1e9jvhz/looking_for_a_passionate_collabratorsfresher/) , 2024-07-23-0911
```
Looking For a Passionate Collabrator(s)/Fresher Backend Devleoper who eager to learn new things related AI and LLM (in J
S) .  
Only Fresher Or 6 Month Experience , Lets Do work on project.  
Tech Stack=>  
Must Know:  NodeJs (Express/Fastif
y) along With Typesript, Logic Building,  
Optional: NestJs, Golang, Microservices,  
What will We Learn Together: Langc
hain Js, LLM Model Training , TensorflowJS, BrainJs, OnnxJs Runtime,Synaptic, HuggingFace, LLama, KesarJs,TouchJs,Vector
/Chroma/Pinecode DB, etc and much more ... a long list ahead

No Payment or moneyn involved

Only Backend Devs:  
Fronte
nd Wale Dur Rahe
```
---

     
 
all -  [ How to restrict chatbot from answering unrelated questions?  ](https://www.reddit.com/r/LangChain/comments/1e9jii5/how_to_restrict_chatbot_from_answering_unrelated/) , 2024-07-23-0911
```
Hey I'm developing a customer service chatbot that answers questions on a specific topic based on knowledge provided to 
the bot. 
In my system prompt I tell it to only answer related questions and refuse to answer unrelated stuff. However i
t still answers questions like 'why is the sky blue?' and so on. 
Do you guys have any tips on how to improve this? 
```
---

     
 
all -  [ Built a RAG system for internal documents using LangChain, FastAPI, and a frontend with Streamlit. W ](https://www.reddit.com/r/LangChain/comments/1e9j3cq/built_a_rag_system_for_internal_documents_using/) , 2024-07-23-0911
```
Hey all,

This is my first take on something that is related to LLM and RAG systems. I've been working on a Retrieval-Au
gmented Generation (RAG) based question answering system which generate answers to the queries from uploaded documents, 
and I'd love to get your feedback, suggestions, and ideas for improvements. The system uses FastAPI, LangChain and Strea
mlit for a minimal UI.

Key features of the system:

1. Document upload and processing
2. Directory processing for batch
 document addition
3. FAISS vector store for efficient document retrieval
4. GPT4All for generating embeddings and answe
ring questions
5. Asynchronous operations for improved performance
6. WebSocket support for real-time question answering


GitHub Repository: [docGPT](https://github.com/nshefeek/docGPT.git)

Some specific areas I'm looking for feedback on:


1. Code quality and best practices.
2. Usage of LangChain.
3. The approach to improve query response timing.
4. A bette
r approach to splitting the documents in such a way that the embeddings generated maintains a metadata that can be used 
to trace back to the original source doument.

Current state of the project:

* Able to upload a PDF, TXT or CSV documen
t.
* Able to upload a directory of PDF documents. But since Streamlit has no widget for folder upload, the folder path h
as to be input as text.
* Queries return somewhat relevant answers, but the returned metadata can't be used to backtrack
 to the exact source location (like the paragraph from which the answer was inferred etc.).
* Query times vary between 1
20-180 seconds.

Thank you in advance for your time and expertise. I'm looking forward to your insights and suggestions 
to help improve this project!
```
---

     
 
all -  [ Chroma DB taking long time to populate ](https://www.reddit.com/r/LangChain/comments/1e9h5dq/chroma_db_taking_long_time_to_populate/) , 2024-07-23-0911
```
When I populate my chromadb, it takes a long time. To add \~3,000 docs can take upwards of 10 minutes, and adding any mo
re docs afterwards will take much longer. When adding to the db, it is only using \~10% GPU and CPU usage. Is there any 
way to speed this process up or use more resources when populating the DB?

For context, I'm using random textbooks to p
opulate the DB with rn, but this issue happens no matter the content I'm adding to the DB.

    #Embedding function I us
e
    embeddings = OllamaEmbeddings(model='nomic-embed-text')
    
    #This block is what takes forever
    new_chunk_i
ds = [chunk.metadata['id'] for chunk in new_chunks]
    db.add_documents(new_chunks, ids=new_chunk_ids)
```
---

     
 
all -  [ Is the new open-sourced mem0 ready for production? ](https://www.reddit.com/r/LLMDevs/comments/1e9gh7z/is_the_new_opensourced_mem0_ready_for_production/) , 2024-07-23-0911
```
Hello, fellos,

I am newbie on LLM dev, and currently looking for a way to build an chat app with context history memory
 and ability to search on the web.  A little overwhelmed by all the stuff like langchain, llamaindex, phidata…… any reco
mmendations for a not-that-large project?

Should I just use mem0 for the memory thing and another package for searching
?
```
---

     
 
all -  [ Knowledge Graph LangChain codes explained ](https://www.reddit.com/r/Langchaindev/comments/1e9ey72/knowledge_graph_langchain_codes_explained/) , 2024-07-23-0911
```
Knowledge Graph is the buzz word since GraphRAG has came in which is quite useful for Graph Analytics over unstructured 
data. This video demonstrates how to use LangChain to build a stand alone Knowledge Graph from text : https://youtu.be/Y
nhG_arZEj0
```
---

     
 
all -  [ Knowledge Graph using LangChain  ](/r/LangChain/comments/1e9etyn/knowledge_graph_using_langchain/) , 2024-07-23-0911
```

```
---

     
 
all -  [ Automatic RAG Evaluation + Monitoring ](https://www.reddit.com/r/LangChain/comments/1e9e3lb/automatic_rag_evaluation_monitoring/) , 2024-07-23-0911
```
Hey everyone,

What are you using to evaluate and monitor your RAG applications?  
  
I've been using LangSmith, but I'm
 not satisfied with it so far. In my opinion, the UX is bad and it lacks an effective way to compare different prompts. 
I'm now considering experimenting with PromptLayer, as it seems to offer better features.  
  
Our situation is a bit co
mplex, though. We're experimenting with two different approaches: a multi-chain setup and one based on function calling.
 So we're really looking to compare entire workflows rather than just individual prompts.

Has anyone found a good solut
ion for monitoring, and more importantly, evaluating these kinds of setups? I'd appreciate any insights or recommendatio
ns.
```
---

     
 
all -  [ How to best tackle RAG for multiple documents with multiple topics? ](https://www.reddit.com/r/LangChain/comments/1e9c81i/how_to_best_tackle_rag_for_multiple_documents/) , 2024-07-23-0911
```
I'm building a chatbot with RAG system for a school, and they want to have all the courses and classes as *knowledge,* s
o students can ask *anything* and the bot should get the answer from all this knowledge*.* I'm having a hard time figuri
ng out how to tackle this, at the moment it's like 50 pdfs, with a lot of pages, for 5 courses, and with many different 
topics. So if a students asks 'What is the best way to do X', the system should somehow look through all these pdfs and 
get the answer, or somehow know which pdfs are the most appropriates to go look for an answer. Not all the documents are
 relevant for a particular question, most likely just one/two/three documents will be relevant.

What I'm doing now is a
dding 'tags', so the people uploading these documents should add one or more tags: 'course 1, tool X, some-other-keyword
', so when someone asks a question, I first try to see if the question matches some of the tags, and then just go get th
e pdfs with those tags.

tldr: how to implement RAG when the knowledge is a lot of different files talking about differe
nt topics.
```
---

     
 
all -  [ Would RAG be useful in this caes ? ](https://www.reddit.com/r/LangChain/comments/1e9c226/would_rag_be_useful_in_this_caes/) , 2024-07-23-0911
```
I trained a Llama2 7b chat model with QLoRA on customer support discussions (Instruction/Output format), and i'm trying 
to find a way to insert knowledge in the model, mainly about fixed information (Products in the store, customer service 
phone number, store opening hours...). Would implementing RAG would be a good idea ?
```
---

     
 
all -  [ Mult-React-agents workflow using Langgraph ](https://www.reddit.com/r/LangChain/comments/1e9bnwm/multreactagents_workflow_using_langgraph/) , 2024-07-23-0911
```
I am facing a problem, I am using:

`from langgraph.prebuilt import create_react_agent`

to create a react agent but thi
s react agent is already complied `langgraph.graph.state.CompiledStateGraph`

And now, I wanna have two more react agent
s and add those agents in the graph but there is no way to the best of my knowledge. 

    react_agent_1 = create_react_
agent(model, tools=tools, messages_modifier=prompt)
    react_agent_2 = create_react_agent(model, tools=tools, messages_
modifier=prompt)
    react_agent_3 = create_react_agent(model, tools=tools, messages_modifier=prompt)

Now I wanna have 
the `react_agent_1` as the parent/supervisor agent and`react_agent_2` and and`react_agent_3`as child agents. Now, how ca
n I add these two agents in the already compiled graph as the other two are agents are also the complied graphs.    
```
---

     
 
all -  [ What Is LangChain, and How Does It Work? ](https://www.reddit.com/r/TechChilli/comments/1e9atzk/what_is_langchain_and_how_does_it_work/) , 2024-07-23-0911
```
# Learn about LangChain, a powerful tool for developing applications with large language models. Discover its features, 
how it works, and its impact on AI-driven solutions.

See here - [https://techchilli.com/artificial-intelligence/what-is
-langchain/](https://techchilli.com/artificial-intelligence/what-is-langchain/)
```
---

     
 
all -  [ Langgraph: what is the advantage of use Toolnodes with llm.bind_tools vs just using an agent with to ](https://www.reddit.com/r/LangChain/comments/1e9ap85/langgraph_what_is_the_advantage_of_use_toolnodes/) , 2024-07-23-0911
```
I see different implementations of Langggraph online, usually the most complex use toolnodes and the agents can only req
uest a tool to be used, not using the tool themselves (i.e. they use bind\_tools).   
The approach with tool\_node seem 
to make the graph more complex and bureaucratic. Is there any use case in which we shouldn't just give the tools to the 
agent? What is the advantage of the ToolNode approach?
```
---

     
 
all -  [ How to format LLM output of my Streamlit + Langchain app like ChatGPT does ? ](https://www.reddit.com/r/LangChain/comments/1e98vyl/how_to_format_llm_output_of_my_streamlit/) , 2024-07-23-0911
```
Hi , I'm developing a PDFRAG app . 

Currently , I'm able to upload a PDF , ask questions from it , the response is stre
amed back to me .

This is working fine . 

Now , I want ChatGPT like functionality where the title of the response is l
arger in font size and bold and the subtitle / the text is smaller in font size and normal in style .

This is my app re
sponse to a query where I ask the model to generate a title and subtitle .

https://preview.redd.it/bhqvd9av21ed1.png?wi
dth=920&format=png&auto=webp&s=e14a9fd323bc8829c4646b8200bc9492ae69ce17

And this is AIPDF's response .

https://preview
.redd.it/im1ktz4b31ed1.png?width=641&format=png&auto=webp&s=9de639f58d9200b1dacf671253f774474c6039f7

I want my response
 like AIPDF .

What do I need to do ? I'm using Langchain and Streamlit to develop my application .
```
---

     
 
all -  [ Which Vector Database already provides confidence scoring to us? ](https://www.reddit.com/r/LangChain/comments/1e98owl/which_vector_database_already_provides_confidence/) , 2024-07-23-0911
```
I am deciding between different vector databases to add. 

  
I would prefer a vector database which could already give 
me confidence score. 

  
So that when the chunk is found, there is also similarity score (confidence score) provided, a
nd I do not have to implement it manually later on. 


```
---

     
 
all -  [ Pandas DataFrame Agent - strange issue  ](https://i.redd.it/qe45holue0ed1.jpeg) , 2024-07-23-0911
```
I've created a DataFrame agent and sent in the simple question 'how many rows are there in the DataFrame?'.

I can see t
he action input is correct:

df.shape[0]

However it looks like it's struggling with assigning a value to Observation? I
've added a photo of the issue (sorry it's not a screenshot).


```
---

     
 
all -  [ LLM that evaluates human answers ](https://www.reddit.com/r/LangChain/comments/1e96ndq/llm_that_evaluates_human_answers/) , 2024-07-23-0911
```
I want to build an LLM powered evaluation application using LangChain where human users answer a set of pre-defined ques
tions and an LLM checks the correctness of the answers and assign a percentage of how correct the answer is and how the 
answers can be improved. Assume that correct answers are stored in a database

Can someone provide a guide or a tutorial
 for this?
```
---

     
 
all -  [ GraphRAG for JSON using LangChain  ](https://www.reddit.com/r/ArtificialInteligence/comments/1e96dzl/graphrag_for_json_using_langchain/) , 2024-07-23-0911
```
This tutorial explains how to use GraphRAG using JSON file and LangChain. This involves
1. Converting json to text
2. Cr
eate Knowledge Graph
3. Create GraphQA chain

https://youtu.be/wXTs3cmZuJA?si=dnwTo6BHbK8WgGEF
```
---

     
 
all -  [ Need some help to optimize the performance of my first ever langchain application. ](https://www.reddit.com/r/LangChain/comments/1e95iug/need_some_help_to_optimize_the_performance_of_my/) , 2024-07-23-0911
```
I'm developing a mental health assessment tool using LangChain and OpenAI. The goal is to analyze user inputs and answer
 predefined questions about their mental state based solely on the information explicitly stated in their input.

My cur
rent implementation uses a ChatPromptTemplate with system and human messages, followed by a ChatOpenAI model and JsonOut
putParser. However, I'm getting mixed results. The model sometimes infers information not explicitly stated in the input
.

Here's a simplified version of my questions.json. There are around 30 questions in my json.

    [
      {
          
'name': 'Age',
          'question_text': 'Select your age group:',
          'displayOptions': [
            '12 to 21'
,
            '21 to 30',
            '30 to 50', 
            '60 and above'
          ]
        },
      {
          '
name': 'Gender',
          'question_text': 'Select your gender:',
          'displayOptions': [
            'Male',
   
         'Female',
            'Others'
          ]
        },
    {
          'name': 'StressRecently', 
          'que
stion_text': 'Have you been stressed about something recently?',
          'displayOptions': [
            'Yes',
      
      'No'
          ]
        },
    
    ]

Sample user input is:  

    I'm 32 year old guy.i've been working 10-12 h
ours in office although i am working from home. I've trouble sleeping.
    

the response i'm getting is 

    {
       
 'analysis': {
            'AbnormalDailyActivity': 'Unknown',
            'AbnormalDisinterested': 'Unknown',
         
   'AbnormalDistraction': 'Unknown',
            'AbnormalEating': 'Unknown',
            'AbnormalMindMaking': 'Unknown
',
            'AbnormalWeightGain': 'Unknown',
            'Age': '30 to 50',
            'ChronicHealth': 'Unknown',
 
           'CurrentChallenges': 'Unknown',
            'CurrentSituation': 'Unknown',
            'Employment': 'Unknown
',
            'EnergyLevel': 'Yes',
            'EngageActivities': 'Unknown',
            'EnjoyNormalDay': 'Unknown',

            'Gender': 'Male',
            'GoodHealth': 'Unknown',
            'ServiceType': 'Unknown',
            'S
taylocation': 'Home or at relatives',
            'StressAge': 'Unknown',
            'StressLoss': 'Unknown',
         
   'StressRecently': 'Yes',
            'StressShared1': 'Unknown',
            'WellBeingHealth': 'Unknown',
          
  'WellBeingNormal': 'Unknown',
            'WellBeingSatisfy': 'Unknown',
            'WorklifeBalance': 'Unknown',
   
         'Workstress': 'Unknown',
            'lackofMotivation': 'Yes'
        },
        'response_time': '3.45 second
s'
    }

now the issue is that i am getting and answer for StressRecently as Yes but the user's input doesn't has anyth
ing related to the stress. I've tried to change the prompt as per my requirement but the LLM is inferring the data from 
the user's input. I need it to answer only those questions which are explicitly mentioned in the user's input. 

here's 
the code i am using for my prompting. 

    system_template = '''You are a highly precise mental health assessment assis
tant. Your role is to analyze user inputs and respond to a set of predefined questions about their mental state and well
-being. Follow these strict guidelines:
    
    1. Only use information explicitly stated in the user's input.
    2. D
O NOT make inferences, assumptions, or guesses about unstated information.
    3. Respond with 'Unknown' for any questio
n that cannot be directly answered from the given information.
    4. Be extremely cautious: it's better to answer 'Unkn
own' than to potentially provide incorrect information.
    5. Focus solely on the content of the user's statement, not 
on interpreting or diagnosing their condition.
    6. DO NOT interpret or diagnose. Only report what is directly stated.

    
    Remember, this is a critical assessment tool dealing with real patients' mental health. Accuracy and caution a
re paramount.
    
    '''
    
    human_template = '''Carefully read the following user input:
    
    User's stateme
nt: {text}
    
    Based solely on this input, provide answers to the following questions. Use 'Unknown' for any questi
on that cannot be answered with absolute certainty based on the explicit content of the user's statement.
    
    Quest
ions:
    {questions}
    
    While answering the questions, use the question_text field to answer the question. don;t 
rely on just the name field.
    Provide your answers in JSON format. Include all questions, using 'Unknown' for any tha
t cannot be confidently answered based solely on the given information.'''
    
    prompt_template = ChatPromptTemplate
.from_messages([
        ('system', system_template),
        ('human', human_template)
    ])
    
    chain = prompt_t
emplate | model | parser
    
    def analyze_situation(
    text
    ):
        start_time = time.time()
        
     
   result = chain.invoke({
            'questions': json.dumps(questions_json, 
    indent
    =2),
            'text': 
text
        })
        
        end_time = time.time()
        elapsed_time = end_time - start_time
        
        
 
   return
     result, elapsed_time
    

  
Can i get any pointers or guidance on   
  
- How to improve my prompt to e
nsure the model only uses explicitly stated information?  
- Are there better LangChain components or techniques I shoul
d consider for this task? 

As a LangChain novice, any guidance on best practices would be greatly appreciated.
```
---

     
 
all -  [ Updates on RAG app ](https://www.reddit.com/r/LangChain/comments/1e95do2/updates_on_rag_app/) , 2024-07-23-0911
```
I am an intern and I'm trying to create a RAG app for my company so it will be easier for them to get access to their te
st test data. But when I look at how frequently things change in the RAG world, like modules moving from langchain to la
ngchain_community, and calls being changed. Do you guys think it's a good idea I go ahead with it? Cos if I leave and th
ere is an update or anything like that no one apart from me can do it. So in the end it becomes useless a few months aft
er. 
```
---

     
 
all -  [ classification ](https://www.reddit.com/r/LangChain/comments/1e92zuz/classification/) , 2024-07-23-0911
```
how to make my chain learn to classify tabular data? 
```
---

     
 
all -  [ Boost Your AI Agent's Exposure: Join Specialized AI Agent Directory! ](https://www.reddit.com/r/LangChain/comments/1e8ymoy/boost_your_ai_agents_exposure_join_specialized_ai/) , 2024-07-23-0911
```
Hey AI Agent builder,

If you're working on an AI agent, consider adding it to specialized and free [AI Agent Directory]
(https://aiagentsdirectory.com/)! It’s a fantastic way to gain extra exposure and benefit from an SEO backlink to your p
roject. Our directory is tailored specifically for AI agents, providing a platform to showcase your work to a broader au
dience.

https://preview.redd.it/1vkgq0ga8ydd1.png?width=1594&format=png&auto=webp&s=d7af1c74646bbd7ba3948dd2e5edd3b7a33
7a10b


```
---

     
 
all -  [ Creating an AI Therapist That You Can Talk To Anytime, Anywhere ](https://www.reddit.com/r/LangChain/comments/1e8tbyr/creating_an_ai_therapist_that_you_can_talk_to/) , 2024-07-23-0911
```
Hey Reddit community,

I wanted to share something I've been passionately working on recently. I've developed an AI Ther
apist—an innovative solution aimed at making emotional support accessible to everyone, right at your fingertips.

What d
oes it do?

Imagine having a therapist available anytime, anywhere, simply by calling. This AI Therapist isn't just abou
t conversation; it's designed to understand your emotions through your voice and provide personalized support. Whether y
ou're dealing with stress, seeking advice, or in need of a friendly ear, it's here to listen and engage with empathy.

W
hy is this important?

Traditional therapy can be costly and inaccessible to many. Recognizing this, I've created this A
I Therapist to break down barriers and ensure everyone can access the emotional support they deserve.

Privacy and Acces
sibility

Privacy is paramount. No data is shared, no voice recordings are kept, and everything is deleted after each se
ssion. Your confidentiality and emotional well-being are prioritized.

Join the Beta Stage

Currently, the AI Therapist 
is in its beta stage, evolving with feedback. I'm eager to hear your thoughts on features you find most beneficial. Whet
her it's enhancing emotional understanding, adding new forms of support, or refining its responsiveness, your input will
 shape its development.

Let's make therapy more accessible and supportive for everyone.

If you're interested in trying
 it out or have questions, feel free to reach out! Together, we can make a positive impact on mental health care.

Looki
ng forward to your thoughts!
```
---

     
 
all -  [ Data ingest ](https://www.reddit.com/r/LangChain/comments/1e8szox/data_ingest/) , 2024-07-23-0911
```
I have been looking for examples of llm used to determine format of unknown format data to write code to ingest it into 
a common known standard format. It seems like something RAG would be useful for. Maybe make it part of a pipeline as the
 first step in a data analytics process...thoughts? Recommendations?
```
---

     
 
all -  [ Don't know why I'm getting an unexpected keyword argument error? ](https://www.reddit.com/r/LangChain/comments/1e8q4l9/dont_know_why_im_getting_an_unexpected_keyword/) , 2024-07-23-0911
```
For the life of me I can't figure out why the below won't work given the instructions [here](https://langchain-ai.github
.io/langgraph/how-tos/create-react-agent-system-prompt/):  
  
  
Code in Jupyter Notebook:

  
`agent_executor = create
_react_agent(llm, tools, state_modifier=system_message, checkpointer=memory)`  
  
`from IPython.display import Image, d
isplay`

`display(Image(agent_executor.get_graph().draw_mermaid_png()))`  
  
  
-----Error---:  
{  
'name': 'TypeError
',  
'message': 'create\_react\_agent() got an unexpected keyword argument 'state\_modifier'',  
'stack': '-------------
--------------------------------------------------------------  
TypeError                                 Traceback (mo
st recent call last)  
\~\\\\AppData\\\\Local\\\\Temp\\\\ipykernel\_844\\\\2897566165.py in <module>  
1 from typing imp
ort Literal  
2   
----> 3 agent\_executor = create\_react\_agent(llm, tools, state\_modifier=system\_message, checkpoin
ter=memory)  
4   
5 from IPython.display import Image, display  
  
TypeError: create\_react\_agent() got an unexpected
 keyword argument 'state\_modifier''  
}  

```
---

     
 
all -  [ RAG in Production: Best Practices for Robust and Scalable Systems ](https://www.reddit.com/r/LangChain/comments/1e8oct1/rag_in_production_best_practices_for_robust_and/) , 2024-07-23-0911
```
🚀 Exciting News! 🚀

Just published my latest blog post on the Behitek blog: 'RAG in Production: Best Practices for Robus
t and Scalable Systems' 🌟

In this article, I explore how to effectively implement Retrieval-Augmented Generation (RAG) 
models in production environments. From reducing hallucinations to maintaining document hierarchy and optimizing chunkin
g strategies, this guide covers all you need to know for robust and efficient RAG deployments.

Check it out and share y
our thoughts or experiences! I'd love to hear your feedback and any additional tips you might have. 👇

🔗 [https://behite
k.com/blog/2024/07/18/rag-in-production](https://behitek.com/blog/2024/07/18/rag-in-production)
```
---

     
 
all -  [ how to find confidence score from the AI responses ](https://www.reddit.com/r/LangChain/comments/1e8izci/how_to_find_confidence_score_from_the_ai_responses/) , 2024-07-23-0911
```
I have **100 pages PDF** data stores in vector database.

Now i ask it questions but I do not know if the **answer is co
rrect or not**

I want to implement scoring, in 5 categories, where AI tells me, how Confidence it is in the response wh
ich is received.

* Confidence
* Somewhat Confident
* Medium Confident
* Low Confidence
* Very low Confidence

How can I
 do it ?
```
---

     
 
all -  [ Dependent Field Generation ](https://www.reddit.com/r/LangChain/comments/1e8gufz/dependent_field_generation/) , 2024-07-23-0911
```
Hey guys, I was working on GPT-dependent field generation for my side project. The idea is to have a tree of field depen
dencies, execute the leaf dependencies in parallel, and pass the context to the upper dependency layers. Then I realized
 that Langchain exists... Does it have something similar?

[https://gist.github.com/andrewshvv/952eb4547560783fb86b7ad81
56216c6](https://gist.github.com/andrewshvv/952eb4547560783fb86b7ad8156216c6)

    class StringGenerator extends BaseGen
erator {
      async before(_: Context, __: Output, runner: GPTRunner): Promise<void> {
        runner.add({ role: 'syst
em', content: 'Initially you are given empty string, write only final value' });
      }
    
    
      @field('d', ['a
'])
      async handler_some_field_d(_: Context, data: Output, runner: GPTRunner): Promise<void> {
        runner.add({ 
role: 'user', content: 'Add letter D to string, what is final string?' });
        const completion = await runner.run()
;
        data['should_be_bcad'] = completion.content;
      }
    
    
      @field('a', ['b', 'c'])
      async handl
er_some_field_a(_: Context, data: Output, runner: GPTRunner): Promise<void> {
        runner.add({ role: 'user', content
: 'Add letter A to string, what is final string?' });
        const completion = await runner.run();
        data['shoul
d_be_bca'] = completion.content;
      }
    
    
      @field('c')
      async handler_some_field_c(_: Context, data: 
Output, runner: GPTRunner): Promise<void> {
        runner.add({ role: 'user', content: 'Add letter C to string, what is
 final string?' });
        const completion = await runner.run();
        data['should_be_c'] = completion.content;
   
   }
    
    
      @field('b')
      async handler_some_field_b(_: Context, data: Output, runner: GPTRunner): Promise<
void> {
        runner.add({ role: 'user', content: 'Add letter B to string, what is final string?' });
        const co
mpletion = await runner.run();
        data['should_be_b'] = completion.content;
      }
    
    
      async generate(
context: Context): Promise<Output> {
        const data = await super.generate(context);
        return data;
      }
  
  
    
    }
    
    
    // Example usage:
    const g = new StringGenerator();
    const finalData = await g.generat
e({ 'some context': 'context' });
    
    
    console.log('Final Data:', finalData);
    // Final Data: {
    //   sho
uld_be_b: 'B',
    //   should_be_c: 'C',
    //   should_be_bca: 'BCA',
    //   should_be_bcad: 'BCAD'
    // }
```
---

     
 
all -  [ Infinity surpasses 1k Github stars & new inference package launch - `pip install embed`  ](https://www.reddit.com/r/LocalLLaMA/comments/1e83cah/infinity_surpasses_1k_github_stars_new_inference/) , 2024-07-23-0911
```
Today, I am launching [https://github.com/michaelfeil/embed](https://github.com/michaelfeil/embed) (MIT). After launchin
g the async framework for OpenAI compatible embedding, re-ranking, clip and classification requests.

[https://github.co
m/michaelfeil/infinity](https://github.com/michaelfeil/infinity) recently hit 1000 Github stars & \~300 PRs/Issues/Discu
ssions. A learning is that the ecosystem (llamaindex, langchain, others) are not ready for asynchronous usage. As a resu
lt, I am launching a more streamlined version with a synchronous API that returns synchronous futures on each method. 


Features:  
- Runs on AMD, CUDA and CPU, via torch or onnx. Automatically chooses optimal settings (e.g. O-4, FA2)  
- O
ptions for int8/fp8 weight-only quantization   
- embedding quantization [https://huggingface.co/blog/embedding-quantiza
tion](https://huggingface.co/blog/embedding-quantization) 
```
---

     
 
all -  [ Hey guys I know we all hate langchain but I have a question  ](https://www.reddit.com/r/datascience/comments/1e7xtww/hey_guys_i_know_we_all_hate_langchain_but_i_have/) , 2024-07-23-0911
```
I’m building a chat bot . And since the data is in a data warehouse,  it’s in a table . Do you think retrieval methods p
erform better when the data is in a text format, just a docs file or it works just the same on a tabular data too and cs
v or parquet format. And I’m planning on using llama index or langchain. Thank you 
```
---

     
 
all -  [ [D] Embedding generation in production? How are you doing it? ](https://www.reddit.com/r/MachineLearning/comments/1e7xt6k/d_embedding_generation_in_production_how_are_you/) , 2024-07-23-0911
```


For those building production RAG pipelines, how are you generating embeddings. More than which model, I'm interested 
in how your deploying it. Are you calling the openai/vertex API endpoint directly? Using langchain/llamaindex wrappers? 
Using vectordb  classes? Or some other way?
```
---

     
 
all -  [ Has anyone been able to use ChatAnthropicVertex tool calling? ](https://www.reddit.com/r/ClaudeAI/comments/1e7qksc/has_anyone_been_able_to_use_chatanthropicvertex/) , 2024-07-23-0911
```
Seems there are a lot of bugs in it's implementation. bind_tools with ChatAnthropicVertex is literally unusable because 
it doesn't return finish_reason. Tool calls are also incorrect. Have you been able to use it. #langchain #VertexAi
```
---

     
 
all -  [ Is learning langchain worth it?  ](https://www.reddit.com/r/learnmachinelearning/comments/1e7pj1l/is_learning_langchain_worth_it/) , 2024-07-23-0911
```
Hello, 

I recently heard about langchain(ik I'm late) but I read briefly about it, and understood it is used for creati
ng genAi apps. But most of the reddit review is pretty negative for this library. 

So is it worth it to learn and creat
e projects using this or no
```
---

     
 
MachineLearning -  [ [D] Is Anyone Else Setting Up Real-Time Django Workers for their AI Application? What's the best way ](https://www.reddit.com/r/MachineLearning/comments/1e0qens/d_is_anyone_else_setting_up_realtime_django/) , 2024-07-23-0911
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

     
 
MachineLearning -  [ [P] Real Time AI Workers Web Application ](https://www.reddit.com/r/MachineLearning/comments/1dzryk9/p_real_time_ai_workers_web_application/) , 2024-07-23-0911
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

     
 
deeplearning -  [ Llama 3 not running on GPU ](https://www.reddit.com/r/deeplearning/comments/1dptxsr/llama_3_not_running_on_gpu/) , 2024-07-23-0911
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

     
