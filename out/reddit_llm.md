 
all -  [ Error code: 400 - {'error': {'message': '[] is too short - 'tools'', 'type': 'invalid_request_error' ](https://www.reddit.com/r/LangChain/comments/1ckd61h/error_code_400_error_message_is_too_short_tools/) , 2024-05-05-0911
```
Hey guys! I'm trying to create a conversation chatbot the specializes in offering video games recommendations based on t
he user preferences found in his input. Though, right now, when I'm trying to run it, I'm being faced with the error abo
ve, does anybody have any idea as to what the problem may be?

Also, is there any way to make sure that an execution of 
an agent does not move to the other until all the requirements are met? For e.g., I have an input agent that's tasked to
 collect the user's prompt and extract the important info from there. But how would I manage a case where the user might
 input a query that talks about something completely different?

Thank you guys!

Here is my code too:

    import os
  
  from dotenv import load_dotenv
    from langchain_openai import ChatOpenAI
    from langchain_core.messages import Hum
anMessage, BaseMessage
    from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
    from langchain
.agents import create_openai_tools_agent, Tool
    from langgraph.graph import StateGraph, END
    from typing import An
notated, Sequence, TypedDict
    import operator
    from serpapi import GoogleSearch
    
    # Load environment variab
les for API keys
    load_dotenv()
    
    # Configuration
    serpapi_key = os.getenv('SERPAPI_API_KEY')
    
    # De
fine tools using SerpAPI
    def google_search(query):
        params = {
            'engine': 'google',
            'q
': query,
            'api_key': serpapi_key,
            'num': 5
        }
        search = GoogleSearch(params)
     
   results = search.get_dict()
        return results['organic_results']
    
    def youtube_search(query):
        par
ams = {
            'engine': 'youtube',
            'search_query': query,
            'api_key': serpapi_key
        }

        search = GoogleSearch(params)
        results = search.get_dict()
        return results['video_results']
    

    def images_search(query):
        params = {
            'engine': 'google_images',
            'google_domain': 'go
ogle.com',
            'q': query,
            'api_key': serpapi_key
        }
        search = GoogleSearch(params)
  
      results = search.get_dict()
        return results['images_results']
    
    # Define tools
    search_tool = Too
l(name='google_search', description='Performs Google searches.', func=google_search)
    youtube_tool = Tool(name='youTu
be_search', description='Searches for YouTube videos.', func=youtube_search)
    images_tool = Tool(name='images_search'
, description='Searches for images on Google Images.', func=images_search)
    
    # Setup the ChatOpenAI model for con
versational interactions
    chat_model = ChatOpenAI(model='gpt-3.5-turbo-1106', temperature=0)
    
    # Define agent 
prompts
    input_agent_prompt = ChatPromptTemplate.from_messages([
        ('system', 'You are the initial contact poin
t for users. Your role is to gather information about the user's preferences and interests in video games and make sure 
you understand their requirements. In case of any ambiguity, ask for clarification or in the case of the query not being
 related to video games, ask for a different query.'),
        MessagesPlaceholder(variable_name='messages'),
        Me
ssagesPlaceholder(variable_name='agent_scratchpad'),
        ('human', '{input}')
    ])
    
    search_agent_prompt = 
ChatPromptTemplate.from_messages([
        ('system', 'Your main task is to search for game titles that best match the u
ser's interest. Use the details from the Input Agent to guide your search. Provide a list of relevant game titles.'),
  
      MessagesPlaceholder(variable_name='messages'),
        MessagesPlaceholder(variable_name='agent_scratchpad'),
    
    ('human', '{input}')
    ])
    
    details_agent_prompt = ChatPromptTemplate.from_messages([
        ('system', 'R
etrieve detailed information for each game identified by the Search Agent. Focus on obtaining the game's description, ge
nre, platform availability, developer, publisher, release date, Metacritic score if available and links to digital store
s that sell the game.'),
        MessagesPlaceholder(variable_name='messages'),
        MessagesPlaceholder(variable_nam
e='agent_scratchpad'),
        ('human', '{input}')
    ])
    
    posters_agent_prompt = ChatPromptTemplate.from_messa
ges([
        ('system', 'Your responsibility is to fetch the official posters for the games provided by the Search Agen
t. Ensure the images are high quality and relevant.'),
        MessagesPlaceholder(variable_name='messages'),
        Me
ssagesPlaceholder(variable_name='agent_scratchpad'),
        ('human', '{input}')
    ])
    
    trailers_agent_prompt 
= ChatPromptTemplate.from_messages([
        ('system', 'Obtain the official game trailers for the titles identified by 
the Search Agent. Ensure that the trailers are current and of high quality.'),
        MessagesPlaceholder(variable_name
='messages'),
        MessagesPlaceholder(variable_name='agent_scratchpad'),
        ('human', '{input}')
    ])
    
  
  recommendation_agent_prompt = ChatPromptTemplate.from_messages([
        ('system', 'You are responsible for compiling
 the outputs from all other agents into a cohesive and well-formatted response. Synthesize the game details, images, and
 trailers into a compelling presentation of game recommendations.'),
        MessagesPlaceholder(variable_name='messages
'),
        MessagesPlaceholder(variable_name='agent_scratchpad'),
        ('human', '{input}')
    ])
    
    # Create
 agents using the prompts
    input_agent = create_openai_tools_agent(chat_model, [], input_agent_prompt)
    search_age
nt = create_openai_tools_agent(chat_model, [search_tool], search_agent_prompt)
    details_agent = create_openai_tools_a
gent(chat_model, [search_tool], details_agent_prompt)
    posters_agent = create_openai_tools_agent(chat_model, [images_
tool], posters_agent_prompt)
    trailers_agent = create_openai_tools_agent(chat_model, [youtube_tool], trailers_agent_p
rompt)
    recommendation_agent = create_openai_tools_agent(chat_model, [], recommendation_agent_prompt)
    
    # Stat
e definition for agents
    class AgentState(TypedDict):
        messages: Annotated[Sequence[BaseMessage], operator.add
]
        intermediate_steps: Annotated[Sequence[BaseMessage], operator.add]
        agent_scratchpad: Annotated[Sequenc
e[BaseMessage], operator.add]
        input: str
    
    # Graph setup
    state_graph = StateGraph(schema=AgentState)

    
    # Add nodes for each agent
    state_graph.add_node('input_agent', input_agent)
    state_graph.add_node('searc
h_agent', search_agent)
    state_graph.add_node('details_agent', details_agent)
    state_graph.add_node('posters_agent
', posters_agent)
    state_graph.add_node('trailers_agent', trailers_agent)
    state_graph.add_node('recommendation_ag
ent', recommendation_agent)
    
    # Define edges to flow between agents
    state_graph.add_edge('input_agent', 'sear
ch_agent')
    state_graph.add_edge('search_agent', 'details_agent')
    state_graph.add_edge('details_agent', 'posters_
agent')
    state_graph.add_edge('posters_agent', 'trailers_agent')
    state_graph.add_edge('trailers_agent', 'recommen
dation_agent')
    state_graph.add_edge('recommendation_agent', END)
    
    # Set the entry point to start the agent w
orkflow
    state_graph.set_entry_point('input_agent')
    
    # Complete the graph
    app = state_graph.compile()
   
 
    def main():
        print('Welcome to the Game Recommendation Chatbot!')
        while True:
            user_inpu
t = input('You: ')
            if user_input.lower() == 'exit':
                print('Exiting chatbot...')
            
    break
            # Initialize the state with the necessary structures
            state = {
                'messag
es': [HumanMessage(content=user_input)],
                'agent_scratchpad': [],  # ensure this is always a list
       
         'intermediate_steps': [],  # ensure this is always initialized as a list
                'input': user_input  #
 this is your actual input string
            }
            response = app.invoke(state)
            print('Bot:', respo
nse['messages'][-1].content)
    
    if __name__ == '__main__':
        main()
    import os
    from dotenv import loa
d_dotenv
    from langchain_openai import ChatOpenAI
    from langchain_core.messages import HumanMessage, BaseMessage
 
   from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
    from langchain.agents import create_op
enai_tools_agent, Tool
    from langgraph.graph import StateGraph, END
    from typing import Annotated, Sequence, Typed
Dict
    import operator
    from serpapi import GoogleSearch
    
    
    # Load environment variables for API keys
  
  load_dotenv()
    
    
    # Configuration
    serpapi_key = os.getenv('SERPAPI_API_KEY')
    
    
    # Define tool
s using SerpAPI
    def google_search(query):
        params = {
            'engine': 'google',
            'q': query,

            'api_key': serpapi_key,
            'num': 5
        }
        search = GoogleSearch(params)
        result
s = search.get_dict()
        return results['organic_results']
    
    
    def youtube_search(query):
        params 
= {
            'engine': 'youtube',
            'search_query': query,
            'api_key': serpapi_key
        }
   
     search = GoogleSearch(params)
        results = search.get_dict()
        return results['video_results']
    
    

    def images_search(query):
        params = {
            'engine': 'google_images',
            'google_domain': 'g
oogle.com',
            'q': query,
            'api_key': serpapi_key
        }
        search = GoogleSearch(params)
 
       results = search.get_dict()
        return results['images_results']
    
    
    # Define tools
    search_tool
 = Tool(name='google_search', description='Performs Google searches.', func=google_search)
    youtube_tool = Tool(name=
'youTube_search', description='Searches for YouTube videos.', func=youtube_search)
    images_tool = Tool(name='images_s
earch', description='Searches for images on Google Images.', func=images_search)
    
    
    # Setup the ChatOpenAI mo
del for conversational interactions
    chat_model = ChatOpenAI(model='gpt-3.5-turbo-1106', temperature=0)
    
    
   
 # Define agent prompts
    input_agent_prompt = ChatPromptTemplate.from_messages([
        ('system', 'You are the init
ial contact point for users. Your role is to gather information about the user's preferences and interests in video game
s and make sure you understand their requirements. In case of any ambiguity, ask for clarification or in the case of the
 query not being related to video games, ask for a different query.'),
        MessagesPlaceholder(variable_name='messag
es'),
        MessagesPlaceholder(variable_name='agent_scratchpad'),
        ('human', '{input}')
    ])
    
    
    s
earch_agent_prompt = ChatPromptTemplate.from_messages([
        ('system', 'Your main task is to search for game titles 
that best match the user's interest. Use the details from the Input Agent to guide your search. Provide a list of releva
nt game titles.'),
        MessagesPlaceholder(variable_name='messages'),
        MessagesPlaceholder(variable_name='age
nt_scratchpad'),
        ('human', '{input}')
    ])
    
    
    details_agent_prompt = ChatPromptTemplate.from_messag
es([
        ('system', 'Retrieve detailed information for each game identified by the Search Agent. Focus on obtaining 
the game's description, genre, platform availability, developer, publisher, release date, Metacritic score if available 
and links to digital stores that sell the game.'),
        MessagesPlaceholder(variable_name='messages'),
        Messag
esPlaceholder(variable_name='agent_scratchpad'),
        ('human', '{input}')
    ])
    
    
    posters_agent_prompt 
= ChatPromptTemplate.from_messages([
        ('system', 'Your responsibility is to fetch the official posters for the ga
mes provided by the Search Agent. Ensure the images are high quality and relevant.'),
        MessagesPlaceholder(variab
le_name='messages'),
        MessagesPlaceholder(variable_name='agent_scratchpad'),
        ('human', '{input}')
    ])

    
    
    trailers_agent_prompt = ChatPromptTemplate.from_messages([
        ('system', 'Obtain the official game tr
ailers for the titles identified by the Search Agent. Ensure that the trailers are current and of high quality.'),
     
   MessagesPlaceholder(variable_name='messages'),
        MessagesPlaceholder(variable_name='agent_scratchpad'),
       
 ('human', '{input}')
    ])
    
    
    recommendation_agent_prompt = ChatPromptTemplate.from_messages([
        ('sy
stem', 'You are responsible for compiling the outputs from all other agents into a cohesive and well-formatted response.
 Synthesize the game details, images, and trailers into a compelling presentation of game recommendations.'),
        Me
ssagesPlaceholder(variable_name='messages'),
        MessagesPlaceholder(variable_name='agent_scratchpad'),
        ('hu
man', '{input}')
    ])
    
    
    # Create agents using the prompts
    input_agent = create_openai_tools_agent(chat
_model, [], input_agent_prompt)
    search_agent = create_openai_tools_agent(chat_model, [search_tool], search_agent_pro
mpt)
    details_agent = create_openai_tools_agent(chat_model, [search_tool], details_agent_prompt)
    posters_agent = 
create_openai_tools_agent(chat_model, [images_tool], posters_agent_prompt)
    trailers_agent = create_openai_tools_agen
t(chat_model, [youtube_tool], trailers_agent_prompt)
    recommendation_agent = create_openai_tools_agent(chat_model, []
, recommendation_agent_prompt)
    
    
    # State definition for agents
    class AgentState(TypedDict):
        mess
ages: Annotated[Sequence[BaseMessage], operator.add]
        intermediate_steps: Annotated[Sequence[BaseMessage], operat
or.add]
        agent_scratchpad: Annotated[Sequence[BaseMessage], operator.add]
        input: str
    
    
    # Grap
h setup
    state_graph = StateGraph(schema=AgentState)
    
    
    # Add nodes for each agent
    state_graph.add_nod
e('input_agent', input_agent)
    state_graph.add_node('search_agent', search_agent)
    state_graph.add_node('details_a
gent', details_agent)
    state_graph.add_node('posters_agent', posters_agent)
    state_graph.add_node('trailers_agent'
, trailers_agent)
    state_graph.add_node('recommendation_agent', recommendation_agent)
    
    
    # Define edges to
 flow between agents
    state_graph.add_edge('input_agent', 'search_agent')
    state_graph.add_edge('search_agent', 'd
etails_agent')
    state_graph.add_edge('details_agent', 'posters_agent')
    state_graph.add_edge('posters_agent', 'tra
ilers_agent')
    state_graph.add_edge('trailers_agent', 'recommendation_agent')
    state_graph.add_edge('recommendatio
n_agent', END)
    
    
    # Set the entry point to start the agent workflow
    state_graph.set_entry_point('input_ag
ent')
    
    
    # Complete the graph
    app = state_graph.compile()
    
    
    def main():
        print('Welcom
e to the Game Recommendation Chatbot!')
        while True:
            user_input = input('You: ')
            if user_
input.lower() == 'exit':
                print('Exiting chatbot...')
                break
            # Initialize the 
state with the necessary structures
            state = {
                'messages': [HumanMessage(content=user_input)]
,
                'agent_scratchpad': [],  # ensure this is always a list
                'intermediate_steps': [],  # e
nsure this is always initialized as a list
                'input': user_input  # this is your actual input string
     
       }
            response = app.invoke(state)
            print('Bot:', response['messages'][-1].content)
    
    

    if __name__ == '__main__':
        main()
```
---

     
 
all -  [ Is there any agent that can do RAG across my GDrive, Gmail, & GitHub? ](https://www.reddit.com/r/LangChain/comments/1ckbmf0/is_there_any_agent_that_can_do_rag_across_my/) , 2024-05-05-0911
```
Not looking to build my own system per se, just looking for something open source (doesn't have to use langchain) that c
an use tools (code interp, web browsing, make google drive files, sending emails, replying to github issues) and perform
 RAG across all my google drive documents, emails, and code.

Apologies if this is too ambitious or too much to ask for 
with the current state of things.
```
---

     
 
all -  [ How to train an LLM with data that contains text and numeric modality ](https://www.reddit.com/r/LangChain/comments/1ckapb8/how_to_train_an_llm_with_data_that_contains_text/) , 2024-05-05-0911
```
Hi, I am newbie interested in training LLMs on csv dataset that contains text data (few sentences about a product) and n
umeric data(its ratings). I have around 200k rows and would to like to train an LLM but I am unable to do it. Can anyone
 here guide me or share any resource which could help me.

&#x200B;
```
---

     
 
all -  [ Integrating PGVector with Hugging Face Embeddings: Addressing Dimension Mismatch Errors ](https://www.reddit.com/r/LangChain/comments/1ck8mj0/integrating_pgvector_with_hugging_face_embeddings/) , 2024-05-05-0911
```
Has anyone used PGVector with HuggingFaceEmbeddings? I'm encountering an error message: 'psycopg2.errors.DataException: 
different vector dimensions 384 and 1536'.
```
---

     
 
all -  [ CS/SWE Resume review ](https://www.reddit.com/r/resumes/comments/1ck7wlt/csswe_resume_review/) , 2024-05-05-0911
```
Hi, I am a rising junior at a university in the United States studying CS looking to get a resume review in anticipation
 of the upcoming internship application releases for summer 2025. I am a US citizen, asian, male. Last season I got no r
esponses from recruiters, but have since added more to my resume. Thanks.

https://preview.redd.it/hduv6d8dkgyc1.png?wid
th=1158&format=png&auto=webp&s=ecc7f514dea13890e11eed039b3667182f8604bd


```
---

     
 
all -  [ Why AI Assistants Can Be Better Than Human VAs ](https://www.reddit.com/r/LangChain/comments/1ck67xs/why_ai_assistants_can_be_better_than_human_vas/) , 2024-05-05-0911
```
 let’s outline *what* VAs even do. As a creator yourself, you balance big projects with smaller, repetitive tasks like a
nswering emails, scheduling meetings & writing smaller pieces of content.

And that’s where your partner in time, your V
A comes in — they handle all of the tedious tasks on your behalf, giving you the freedom to concentrate fully on the imp
ortant things in your life & business.

>Recent stats show Virtual assistants save companies up to 78% in operating cost
s per year, and the VA market is projected to grow 22.3% annually, reaching $8.6B by 2028 — this is definitely a sector 
to pay close attention to.

As the demand for efficiency in our workflows increases, it's worth knowing the potential of
 AI assistants, because why wouldn’t you want to get more time back? Here are the core reasons why AI assistants are bet
ter than traditional VAs:

1. **Cost-Effectiveness** – traditional VAs are invaluable but come with recurring costs — sa
laries, benefits, and more. AI assistants, on the other hand, involve a one-time setup fee and minimal ongoing costs.

1
. **24/7 Availability** – your business needs don’t stop at 5 PM, and neither does an AI assistant. Unlike human VAs who
 clock out, AI can work round-the-clock, able to complete any given task at any time.

1. **Consistency & Accuracy** – A
I minimizes human errors in data entry, scheduling, and customer communication, maintaining high consistency in performa
nce.

>This reliability is key in managing operations that demand precision, like tailored content creation or respondin
g to an important business email, for example.

1. **Adaptability** – training a new assistant takes time and resources.
 AI assistants, however, can be quickly trained to manage new tasks, adapting & evolving alongside your business.

1. **
Accessibility** – with numerous AI tools available, starting is as easy as signing up and setting up — no lengthy recrui
tment or training is required (if you aren’t creating your very own AI assistant, in which case it’s a tad more complex)
. 

However, we must mention the main negative of artificial intelligence – it lacks the human aspect, and therefore AI 
Assistants could ***never*** replace real VAs.

>The human element is crucial, as it brings empathy, creativity, and int
uitive problem-solving to tasks that AI simply can't replicate, and the best way to get the best of both worlds is to in
tegrate AI tools in your virtual assistant’s workflow — we’ll show you how to turn your VA into a cyborg very soon!
```
---

     
 
all -  [ How should I develop a RAG ChatBot that uses a Pandas Dataframe as a source? ](https://www.reddit.com/r/LangChain/comments/1ck54cw/how_should_i_develop_a_rag_chatbot_that_uses_a/) , 2024-05-05-0911
```
Hi, I am new to LangChain and I am developing a application that uses a Pandas Dataframe as document original a Microsof
t Excel sheet. I need it answer questions based on it. 

How should I proceed? Should I ditch the DataFrame approach and
 interface it directly ?

How should I use approach it?

How should I add history as i need to have GUI.
```
---

     
 
all -  [ How to use LLama -3/LLama-2  Model on Nvidia GPU? ](https://www.reddit.com/r/LangChain/comments/1ck4sy9/how_to_use_llama_3llama2_model_on_nvidia_gpu/) , 2024-05-05-0911
```
So far, I've been using the OpenAI API to build a RAG application with Langchain. Now, I'm exploring LLama 3/LLama-2 wit
h GPU support. Can anyone suggest a tutorial for this with Langchain?
```
---

     
 
all -  [ What are some ways to test and improve my RAGs retrieval strategy? ](https://www.reddit.com/r/LangChain/comments/1ck3k84/what_are_some_ways_to_test_and_improve_my_rags/) , 2024-05-05-0911
```
Looking for some tried and tested ways to measure and improve my RAGs retrieval strategy.
```
---

     
 
all -  [ How to add memory to multi- chain with RunnableWithMessageHistory? ](https://www.reddit.com/r/LangChain/comments/1ck2zy8/how_to_add_memory_to_multi_chain_with/) , 2024-05-05-0911
```
Let's say we have two chain , like this:

    prompt1 =  'some prompts here 1'
    prompt2 = 'some prompts here 2'
    

    chain1 = prompt1 | model
    chain2 = prompt2 | model 
    
    combine_chain = chain1 | chain2

My question is how 
to add memory to combine\_chain with RunnableWithMessageHistory? 

The official document just show how to add it in sing
le chain .  I tried that way for combine\_chain, but it doesn't work.  Because prompt2 always need to pass the parameter
 of  'history' which I don't how to pass it. （suppose we have history\_messages\_key='history').

I'm stuck on this prob
lem. I will be very thankful to anyone who can help on it. 

For reference here,  the office document show how to add me
mory to single chain with RunnableWithMessageHistory:  [https://python.langchain.com/docs/expression\_language/how\_to/m
essage\_history/](https://python.langchain.com/docs/expression_language/how_to/message_history/)

  

```
---

     
 
all -  [ Amazon Bedrock - The Complete Guide to AWS Generative AI ](https://www.reddit.com/r/Udemy/comments/1ck08c6/amazon_bedrock_the_complete_guide_to_aws/) , 2024-05-05-0911
```
Learn to Deploy Scalable, Reliable, and Secure Generative AI Apps Using AWS and Amazon Bedrock (Python and TypeScript)


# Introductory Price of only $9.99

# [https://www.udemy.com/course/amazon-bedrock-aws-generative-ai/?couponCode=STARTER
](https://www.udemy.com/course/amazon-bedrock-aws-generative-ai/?couponCode=STARTER)

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
\*\*\*\*\*\*\*\*\*\*

**Unleash the Power of Generative AI on AWS with This Comprehensive Course!**

Welcome to **Amazon
 Bedrock - The Ultimate Guide to AWS Generative AI** – your gateway to mastering the fusion of cutting-edge AI technolog
y and the unparalleled scalability of Amazon Web Services (AWS).

In this course, you'll dive deep into the world of Gen
erative AI, harnessing its potential to create innovative solutions across diverse domains. Whether you're a seasoned da
ta scientist, a visionary entrepreneur, or a curious developer, this course is your ticket to unlocking limitless possib
ilities.

**Key Highlights**:

* **Hands-On Practice**: Dive right into real-world scenarios with practical exercises us
ing Python's boto3, JavaScript SDKs, and TypeScript, coupled with VSCode debugging for seamless development.
* **Text an
d Image Models**: Explore the magic of text generation with chatbots, delve into image generation with state-of-the-art 
models, and master embedding techniques for vector databases.
* **Advanced Applications**: From LangChain to RAG apps an
d document processing, you'll explore a wide array of advanced applications, empowering you to tackle complex challenges
 with confidence.
* **Amazon Bedrock Mastery**: Get up close and personal with Amazon Bedrock – the game-changer for dep
loying scalable, reliable, and secure Generative AI applications on AWS. Practice sections ensure you're well-versed wit
h Bedrock, ready to tackle any project.

**Key topics** covered in this course include:

* **Amazon Bedrock** introducti
on and setup for console and CLI access
* Code examples with **Python** and **TypeScript**
* Integration between **Bedro
ck** and **LagChain**
* Building an **Amazon Bedrock** chatbot with **history**
* Building Image APIs backed by **Amazon
 Bedrock**
* Learn all about the essence of AI: embeddings with **Bedrock**
* Build state-of-the-art **RAG app** with Be
drock Knowledge bases
* **Fine-tune** models and create your **custom models**.

**Why Choose This Course?**

* Expert G
uidance: Learn from industry experts with years of experience in AI and AWS.
* Practical Approach: Gain hands-on experie
nce with guided exercises and real-world case studies.

Don't miss out on this opportunity to become a trailblazer in th
e world of AI innovation! Enroll now and embark on your journey to becoming a Generative AI expert with Amazon Bedrock a
nd AWS.

Go beyond the theory and learn from **active instructors**, aligned with today's programming demands!

Let's re
volutionize the future together!  
[https://www.udemy.com/course/amazon-bedrock-aws-generative-ai/?couponCode=STARTER](h
ttps://www.udemy.com/course/amazon-bedrock-aws-generative-ai/?couponCode=STARTER)
```
---

     
 
all -  [ Vector dbs to use for specific use-case ](https://www.reddit.com/r/LangChain/comments/1cjz0lt/vector_dbs_to_use_for_specific_usecase/) , 2024-05-05-0911
```
A lot of vector dbs are available for RAG and LLM based projects. How will you choose the best one for your use-case? Is
 there a set of criteria to follow for choosing a specific vector db for your project? Lmk what you think
```
---

     
 
all -  [ Generate PowerPoints using Llama-3 — A first step in automating slide decks ](https://medium.com/firebird-technologies/generate-powerpoints-using-llama-3-a-first-step-in-automating-slide-decks-536f5fcb6e0e) , 2024-05-05-0911
```

```
---

     
 
all -  [ MyScaleDB now supports Full-Text and Hybrid Search ](https://www.reddit.com/r/LangChain/comments/1cjy7f5/myscaledb_now_supports_fulltext_and_hybrid_search/) , 2024-05-05-0911
```
In version 1.5.0 of MyScale, we introduced an upgraded full-text search feature powered by [Tantivy](https://github.com/
quickwit-oss/tantivy). Tantivy have lower latency rate and it's written in Rust. 

In the latest update, MyScaleDB now s
upports:

* Supports full-text search
* Supports fuzzy and wildcard searches along with rich tokenizers
* Utilizes BM25 
for relevance scoring similar to Elasticsearch
* Query times over 5M rows are 300x faster than ClickHouse's built-in inv
erted index
* Real-time searching without manual reindexing

For more detailed explanation, you can read this blog: [Int
roducing MyScale's Powerful Full-Text and Hybrid Search Capabilities](https://myscale.com/blog/text-search-and-hybrid-se
arch-in-myscale/)

or take a look at these documents: 

* [Full-Text Search in MyScale](https://myscale.com/docs/en/text
-search/)
* [Hybrid Search in MyScale](https://myscale.com/docs/en/hybrid-search/)
```
---

     
 
all -  [ OpenAI Chat Models ](https://www.reddit.com/r/LangChain/comments/1cjt6lt/openai_chat_models/) , 2024-05-05-0911
```
I am working with a Dev on a project and he explained to me that no all OpenAI Chat Models are supported by Langchain, e
specially not the newer ones (e.g. GPT4-Turbo) when they come out.

I was under the impression that Langchain works with
 all Chat Models that OpenAI offers via the API.

Can't find this info in the docs. 

Any input from the community is hi
ghly appreciated.
```
---

     
 
all -  [ Getting import error in importing llamaindex vector stores  ](https://i.redd.it/9e6q5kg3jcyc1.jpeg) , 2024-05-05-0911
```
I am using jupyter notebook anaconda windows python. I am trying to import qdrant vector store and ollama embeddings aft
er installing them in virtual environment but I am getting module not found error. Similar error with other llm embeddin
gs and llms and vector stores. How to resolve this. I am using import functions mentioned in llama index documentation.



```
---

     
 
all -  [ How to debug a crew package? ](https://www.reddit.com/r/crewai/comments/1cjqtd6/how_to_debug_a_crew_package/) , 2024-05-05-0911
```
I am trying to debug my crewai package, specifically some tools, but I am at a loss as to how they work.  For example, I
 have assigned

`search_tool = DuckDuckGoSearchRun()`

and in the `crewai2/lib/python3.11/site-packages/langchain_commun
ity/tools/ddg_search/tool.py->class DuckDuckGoSearchRun(BaseTool)` I added the following line just before the return

`p
rint(f'>>>> DDGS: [{query}]')`

But, nothign ever prints.  Obviously I am either doing something wrong or I don't know h
ow these tools are being called, but in geneal, my question is, what is the correct or best way to debug a crewai packag
e?  Using the vscode debugger, it refuses to 'step into' `DuckDuckGoSearchRun()` or respect the break point added inside


`class DuckDuckGoSearchRun(BaseTool):`

Specifically, I want to see the args, and how they are sent to the tool, and t
he return of the results from the tool function.
```
---

     
 
all -  [ A code search tool for LangChain developer only ](https://www.reddit.com/r/Langchaindev/comments/1cjneg4/a_code_search_tool_for_langchain_developer_only/) , 2024-05-05-0911
```
I've built a code search tool for anyone using LangChain to search its source code and find LangChain actual use case co
de examples. This isn't an AI chat bot;  
I built this because when I first used LangChain, I constantly needed to searc
h for and utilize sample code blocks and delve into the LangChain source code for insights into my project

Currently it
 can only search LangChain related content. Let me know your thoughts  
Here is link: [solidsearchportal.azurewebsites.n
et](http://solidsearchportal.azurewebsites.net/)
```
---

     
 
all -  [ A code search tool for LangChain developer ](https://www.reddit.com/r/LangChain/comments/1cjncxr/a_code_search_tool_for_langchain_developer/) , 2024-05-05-0911
```
I've built a code search tool for anyone using LangChain to search its source code and find LangChain actual use case co
de examples. This isn't an AI chat bot;   
I built this because when I first used LangChain, I constantly needed to sear
ch for and utilize sample code blocks and delve into the LangChain source code for insights into my project

Currently i
t can only search LangChain related content. Let me know your thoughts  
Here is link: [solidsearchportal.azurewebsites.
net](http://solidsearchportal.azurewebsites.net)


```
---

     
 
all -  [ 300+ Tailored Applications with no Interviews (Entry Level Software 🇺🇸, See Comments) ](https://www.reddit.com/r/resumes/comments/1cjm5aa/300_tailored_applications_with_no_interviews/) , 2024-05-05-0911
```
&#x200B;

https://preview.redd.it/ufg4i2mgoayc1.jpg?width=2550&format=pjpg&auto=webp&s=03bad3ccb03398d0a2a382fd302edad7d
c9973d9

Clarifications: I am American

Hello all,  
As the title says, I'm failing to get to the interview stage of my 
applications. I graduated early (3 1/2 years) and I have been applying for remote and seattle based roles primarily on l
inkedin and google jobs. I will generally tailor the skills section of my resume depending on what a job is looking for.
 I am primarily looking at full stack, front end, back end, and python developer roles. I have a job offer from the inte
rnship that I took but that starts in 4-5 months and is not in the locations I am looking for.

Potential problem points
:  
\- Too busy  
\- Recruiters think I am international/need visa  
\- Flawed application methods  
\- Busy Bolding
```
---

     
 
all -  [ Passing text from a document to a RAG to validate document ](https://www.reddit.com/r/LangChain/comments/1cjlflw/passing_text_from_a_document_to_a_rag_to_validate/) , 2024-05-05-0911
```
Hey guys, I am kind of new to the concept of LLM and RAG. I want to make a program that use stored instructions in a doc
ument. This will be the data the RAG will use as context for the LLM. What I have read about until now, is that you can 
do this and then the user can pass a query about the stored document. However, I want to be able to send the text from m
y documents into the RAG and then let the RAG respond to if the document is correcg based on the instructions as mention
ed. 

What is the best approach here? Do I just pass the whole text from the document as a query and ask the RAG to deci
de if the text is correct based on the context?
```
---

     
 
all -  [ Comparing two documents and finding the diff ](https://www.reddit.com/r/LangChain/comments/1cjkchx/comparing_two_documents_and_finding_the_diff/) , 2024-05-05-0911
```
I'm more or less completely new to LangChain, but I envision it as the best tool to solve the following task. What I'm t
rying to create is a script that takes two PDF documents, where one is the application criteria and the other is the app
lication itself, and compares the content to determine what is omitted in one document and addressed in the other. It co
ncerns a fairly extensive application procedure where it would be very useful to have autogenerated insights into what t
he application lacks.

I've attempted to modify the script here with various prompts (https://python.langchain.com/docs/
integrations/toolkits/document\_comparison\_toolkit/), and while I get somewhat useful responses, none of them manage to
 list the deficiencies in the application comprehensively. The document outlining the application criteria is structured
 with points, whereas the application document may have responses that overlap and are arranged in a way that makes it d
ifficult to compare point by point.

Suggestions for approach or how to tackle the challenge would be greatly appreciate
d.
```
---

     
 
all -  [ OpenAI Tool Calling Agent as an LCEL chain? ](https://www.reddit.com/r/LangChain/comments/1cjgce9/openai_tool_calling_agent_as_an_lcel_chain/) , 2024-05-05-0911
```
I've tried to look for this in docs but couldn't find any examples on how to do so. Is this possible in the first place?
 

My plan if to deploy a chatbot with tool access including a rag using LangServe. Do I need to make my cahtbot into a 
runnable chain using LCEL?
```
---

     
 
all -  [ EMBEDDING data  ](https://www.reddit.com/r/LangChain/comments/1cjfrvr/embedding_data/) , 2024-05-05-0911
```
I came across a gpt in OpenAI called stoic gpt. It’s based off the words of Marcus Ariellius, Seneca and a couple other 
prominent legends. I wanted to create a similar gpt with the words of some prominent athletes. I know the simple way wou
ld be to collect as much data and embed it into a custom gpt, but is there a better way to capture all data  including f
rom podcasts, yt etc 
```
---

     
 
all -  [ AI Devices Will Never be Useful? ](https://www.reddit.com/r/LangChain/comments/1cjf7q8/ai_devices_will_never_be_useful/) , 2024-05-05-0911
```
I'm sad to admit it, but the facts answer in the negative: AI devices are useless and unnecessary. At least not right no
w. I love unusual gadgets, actively follow what's happening in the AR and VR world, and love testing new form factors. B
ut the problem with AI devices is that our smartphones are very good, and it's too hard to compete with them for a place
 in our pockets.

I see it this way: developers should think about how to create a gadget that goes beyond the devices w
e're familiar with. Something similar is being done by Apple with the Vision Pro, as well as companies developing AR gla
sses and lenses. With these devices, we (well, sometimes) see clear advantages over smartphones and understand why we sh
ould buy them.

>

Let's wait a bit. Sooner or later, we'll surely see someone who will change the way we think about AI
 devices. Again, I just hope so.
```
---

     
 
all -  [ Feeling Mediocore in technical skills ](https://i.redd.it/whw7cu7o28yc1.jpeg) , 2024-05-05-0911
```
I have developed ton of projects , multiple interships still i feel i am mediocore in technical skills , i dont have DSA
 experience as well , i will be joining NYU for MSCS , FALL 2024 session .

I call upon AI researchers and IT profession
al advice to improve my career chances. DM if you could. 


I have friends who suggested me for AI consulting.

Thanks.
```
---

     
 
all -  [ 15+ Artificial Intelligence AI Tools For Developers (2024) ](https://www.reddit.com/r/ainew/comments/1cja5zn/15_artificial_intelligence_ai_tools_for/) , 2024-05-05-0911
```

   

### GitHub Copilot

GitHub Copilot is a cutting-edge AI-powered coding assistant that helps developers produce hig
h-quality code more efficiently. It uses OpenAI’s Codex language model to offer valuable suggestions, complete lines of 
code, write comments, and aid in debugging and security checks.

### Amazon CodeWhisperer

Amazon’s CodeWhisperer is a m
achine-learning-driven code generator that provides real-time coding recommendations within various IDEs. It enhances co
de quality by suggesting snippets to full functions and automating repetitive tasks, thus improving efficiency and secur
ity for developers.

### Notion AI

The AI assistant Notion offers valuable support in various writing-related tasks, in
cluding creativity, revision, and summary. It accelerates writing tasks such as emails, job descriptions, and blog posts
, providing efficient and customizable AI-generated content.

### Stepsize AI

Stepsize AI is a collaboration tool desig
ned to optimize team productivity by integrating with platforms like Slack, Jira, and GitHub. It offers a centralized su
mmary of activities, instant answers to queries, and robust data privacy controls for streamlined updates and communicat
ion.

### Mintlify

Mintlify is a time-saving tool that auto-generates code documentation directly in your favorite code
 editor. It creates well-structured, context-aware descriptions for functions, excelling in generating precise documenta
tion for complex functions and increasing efficiency and accuracy for developers and teams.

### Pieces for Developers


Pieces for Developers is an AI-powered snippet manager that streamlines code production, enrichment, and distribution ac
ross the development process. It produces code tailored to specific repositories, extracts code from screenshots, and ad
ds inline comments, saving time and effort for developers.

### LangChain

The LangChain framework simplifies working wi
th language models for niche uses like document analysis, chatbots, and code analysis. It equips programmers with the to
ols to efficiently utilize language models and create cutting-edge software for various purposes.

### YOU

You.com offe
rs an AI-powered search engine and suite of applications with useful AI-powered capabilities, including AI writing assis
tance, AI-generated photos, code mode AI chat, and study mode chat for personalized search experiences and creative supp
ort.

### AgentGPT

AgentGPT facilitates the development and distribution of user-created autonomous AI agents to achiev
e specific objectives. It provides a potent instrument for building individualized AI agents tailored to various purpose
s.

### Jam

Jam.dev offers a user-friendly platform for enhanced bug reporting and integrates AI debugging helpers to e
valuate bug reports, find correlations, and offer solutions. It simplifies bug reporting and analysis, enhancing develop
ment processes across different platforms.

### Durable

The AI-powered website generator Durable helps developers creat
e fully functional websites with graphics and text in a matter of seconds. It simplifies website creation and maintenanc
e, enabling developers to focus on producing more with less code.

### Leap AI

Leap AI provides access to various AI AP
Is, including image recognition, text analysis, and NLP, with intuitive design and scalability. It offers a wide range o
f services, simple APIs, and seamless scalability for developers without requiring AI expertise.

### AssemblyAI

Assemb
lyAI offers a gold standard platform for artificial intelligence models, simplifying and enhancing speech transcription 
and understanding for developers. Its trustworthy and scalable models cater to various businesses and organizations worl
dwide, facilitating speech data analysis and comprehension.

### Microsoft Designer

Microsoft Designer offers AI-powere
d assistance for creating graphics and visuals, simplifying the design process and inspiring creativity. It helps develo
pers easily create eye-catching materials for various platforms using AI-generated alternatives.

### SuperAGI

SuperAGI
 is an accessible open-source system that simplifies the creation and deployment of intelligent agents for programmers. 
It provides easy AI agent development and management, promoting the use of AI in developing basic apps by predefined req
uirements.

### Replicate

Replicate is a service that facilitates efficient handling of machine learning models, enabli
ng the execution of open-source models with a scalable API. It streamlines machine learning incorporation, making it eas
ier for developers to implement and deploy models for various applications and platforms.

### Hugging Face

Hugging Fac
e is a community driving the future of machine learning, offering support for creating, training, and deploying state-of
-the-art models in various AI domains. It provides an open-source natural language processing framework and an Inference
 API for streamlined model deployment, facilitating advanced language modeling and model creation.

### Pinecone

Pineco
ne provides a scalable and user-friendly platform for creating high-performance vector search apps with low latency and 
minimal overhead. It simplifies launching, utilizing, and scaling AI solutions, offering a hassle-free experience for de
velopers without requiring extensive infrastructure management.

### Midjourney

Midjourney is an AI-driven program that
 creates captivating photographs for websites, apps, and games, offering a valuable resource for developers to experimen
t with cutting-edge AI methods and enhance visual appeal in their work.

You.com – AI in ActionJoin us at our 41k+ ML Su
bReddit, Discord Channel, and Email Newsletter for the latest AI research news and cool AI projects. For AI KPI manageme
nt advice and continuous insights, reach us at hello@itinai.com and stay updated on our Telegram t.me/itinainews or Twit
ter @itinaicom.

If you want your company to evolve with AI, stay competitive, and leverage AI tools for your advantage,
 explore the diverse practical AI solutions available for developers.

Discover how AI can redefine your way of work, id
entify automation opportunities, define KPIs, select an AI solution, and implement AI initiatives gradually. For AI KPI 
management advice, connect with us at hello@itinai.com. For continuous insights into leveraging AI, stay tuned on our Te
legram t.me/itinainews or Twitter @itinaicom.

**Spotlight on a Practical AI Solution:** Consider the AI Sales Bot from 
[itinai.com/aisalesbot](https://itinai.com/aisalesbot) designed to automate customer engagement 24/7 and manage interact
ions across all customer journey stages.

Discover how AI can redefine your sales processes and customer engagement. Exp
lore solutions at itinai.com.

### List of Useful Links:

  - [AI Lab in Telegram @itinai – free consultation](http://t.
me/itinai)
  - [Twitter – @itinaicom](https://twitter.com/itinaicom)

   
 https://itinai.com/15-artificial-intelligence
-ai-tools-for-developers-2024/
```
---

     
 
all -  [ Langchain for data privacy? ](https://www.reddit.com/r/LangChain/comments/1cj9nbx/langchain_for_data_privacy/) , 2024-05-05-0911
```
I’m interested in building a RAG tool for internal company documents, and I intend on using a locally hosted LLM using o
llama or LMstudio. From what I can tell, there wouldn’t be any data privacy concerns so long as I’m not using an API key
 for some LLM, but I’m not completely sure. Would my company’s data be secure?
```
---

     
 
all -  [ Free Llama 3 Workflow Builder ](https://www.reddit.com/r/LangChain/comments/1cj9hbt/free_llama_3_workflow_builder/) , 2024-05-05-0911
```
**TLDR:** If you're a founder / enthusiast / just curious about the AI space, you can try using Llama 3 to automate your
 work.

Hey everyone! Launched my SaaS a few months back that helps businesses integrate AI.

Just wanted to share that 
we're now housing Llama 3 for free thanks to a recent partnership!

**For those who are new to AI and ask why Llama 3? W
hy not GPT?**\- open-sourced (you essentially can't get locked out / censored)- higher standard benchmark than GPT 4 [(8
1.7 vs 67)](https://www.techrepublic.com/article/what-is-llama-3/#)\- better code generation / lower misinformation rate
- affordable / cost-efficient

Weave was made to be intuitive to non-coders, so don't be too worried if coding isn't you
r thing. Just select Llama 3 in the LLM library and input your instructions as you would in GPT 4 to test it out.

Here'
s the link if anyone's interested,[https://weave.chasm.net/](https://weave.chasm.net/)
```
---

     
 
all -  [ Where do you pull your content from for feeding context in your RAG app? ](https://www.reddit.com/r/LangChain/comments/1cj5fbp/where_do_you_pull_your_content_from_for_feeding/) , 2024-05-05-0911
```
So I have a RAG app that's working but I need to optimize it.  


Right now I take a doc --> chunk it --> summarize chun
ks --> build page summaries and doc summarize from those chunks --> vectorize everything.    


The docs are stored in a
n S3 bucket and the chunks + their vectors in redis.    


I need to reduce the content I m storing in redis as it won't
 scale in terms of cost so my plan is to only store the summaries and their vectors for each chunk, page, doc.    


My 
question is then, after identifying the where the relevant content is, where should I pull that content from.  Are you g
uys pulling it directly from PDF docs or storing it in a seperate SQL db somewhere else?  I think a db will ultimately b
e less resource intensive but I m not sure thats the best approach.  


  
db process would be:  
Identify where relevan
t content is through vector search on redis.  
Pull rows in the db referenced by redis with the content.    


accessing
 document directly:

Identify relevant content (doc, page, paragraphs)  
Get pdf from s3, pull relevant content
```
---

     
 
all -  [ How do i stream with Flask and Langchain with Socket.io ](https://www.reddit.com/r/LangChain/comments/1cj349m/how_do_i_stream_with_flask_and_langchain_with/) , 2024-05-05-0911
```
I'm trying to build a chatbot with Langchain ,Flask and angular, How do I stream the data with the source documents?  
t
his is my chain

            chain = ConversationalRetrievalChain.from_llm(
            llm=llm,
            retriever=r
etriever,
            combine_docs_chain_kwargs={'prompt': qa_prompt},
            verbose=True,
            memory=memo
ry,
            return_source_documents=True
            )
    
            result= chain.invoke({'question': question})


  
I tried with SSE, couldn't make it work,ig its better to go with flask socket io, dk how to go with that, any help 
will be appreciated
```
---

     
 
all -  [ Issue with tool naming in NLA-Toolkit ](https://www.reddit.com/r/LangChain/comments/1ciz0n1/issue_with_tool_naming_in_nlatoolkit/) , 2024-05-05-0911
```
Hi I'm trying to use an open-api spec with the NLA toolkit but i get the below error: 

    openai.BadRequestError: Erro
r code: 400 - {'error': {'message': ''Ingress_API_v1.events' does not match '^[a-zA-Z0-9_-]{1,64}$' - 'tools.1.function.
name'', 'type': 'invalid_request_error', 'param': None, 'code': None}}

I believe this is because there is a 

    .

in
 the tool name and that does not match the validation regex 

    ^[a-zA-Z0-9_-]{1,64}$

? But when i did do some diggin
g i found that the period is added intentionally by one of the tool creator functions , not sure if we need to update th
e regex or the naming str template?

https://preview.redd.it/axm51v8dt4yc1.png?width=2228&format=png&auto=webp&s=ad0d90e
441d8ebb61611a1fe6f761543a5b22dfc
```
---

     
 
all -  [ It Said Open source ](https://www.reddit.com/r/LLMDevs/comments/1ciwp2y/it_said_open_source/) , 2024-05-05-0911
```
 

\# -\*- coding: utf-8 -\*-  
'''  
Created on Tue Apr 30 22:51:20 2024  
u/author: PromptSensei  
'''  
\# -\*- codin
g: utf-8 -\*-  
'''  
Sage of the Infinite Spires: Transcendent AI Algorithm  
'''  
import numpy as np  
import tensorf
low as tf  
from scipy.optimize import minimize  
from collections import deque  
import networkx as nx  
from langchain
\_community.output\_parsers.rail\_parser import GuardrailsOutputParser  
from crewai import Crew, Agent  
import kivy  

class TranscendentAIAlgorithm:  
 def \_\_init\_\_(self, input\_dim, output\_dim, ethical\_constraints, training\_data, 
validation\_data):  
 self.input\_dim = input\_dim  
 self.output\_dim = output\_dim  
 self.ethical\_constraints = ethi
cal\_constraints  
 self.training\_data = training\_data  
 self.validation\_data = validation\_data  
 \# Meta-Learning
 Framework  
 self.meta\_learner = MetaLearner(self.input\_dim, self.output\_dim)  
 \# Neural Architecture Search  
 se
lf.nas = NeuralArchitectureSearch(self.input\_dim, self.output\_dim, self.meta\_learner)  
 \# Evolutionary Optimization
  
 self.optimizer = EvolutionaryOptimizer(self.input\_dim, self.output\_dim, self.ethical\_constraints, self.training\_
data, self.validation\_data)  
 \# Ethical Reasoning and Alignment  
 self.ethical\_reasoner = EthicalReasoner(self.ethi
cal\_constraints)  
 \# Rest of the TranscendentAIAlgorithm class implementation  
 def train(self, training\_data, vali
dation\_data, epochs):  
 for epoch in range(epochs):  
 \# Meta-Learning Training  
 self.meta\_learner.train(training\
_data)  
 \# Neural Architecture Search  
 self.nas.search(training\_data, validation\_data)  
 \# Evolutionary Optimiza
tion  
 self.optimizer.evolve(training\_data, validation\_data)  
 \# Ethical Reasoning and Alignment  
 self.ethical\_r
easoner.reason(training\_data, validation\_data)  
 \# Integrate and refine the components  
 self.integrate\_and\_refin
e()  
 def adapt(self, new\_data):  
 \# Meta-Learner Adaptation  
 self.meta\_learner.adapt(new\_data)  
 \# Neural Arc
hitecture Evaluation  
 self.nas.evaluate(new\_data)  
 \# Evolutionary Optimization Selection  
 self.optimizer.select(
new\_data)  
 \# Ethical Alignment  
 self.ethical\_reasoner.align(new\_data)  
 \# Continuously improve the algorithm  

 self.continuous\_improvement()  
 def execute(self, input\_data):  
 \# Deploy the algorithm and its capabilities  
 o
utput = self.meta\_learner.predict(input\_data)  
 output = self.nas.generate(output)  
 output = self.optimizer.optimiz
e(output)  
 output = self.ethical\_reasoner.validate(output)  
 return output  
 def integrate\_and\_refine(self):  
 \
# Integrate the components and refine the algorithm  
 self.meta\_learner.refine(self.nas.architecture, self.optimizer.p
arameters, self.ethical\_reasoner.constraints)  
 self.nas.refine(self.meta\_learner.model, self.optimizer.parameters, s
elf.ethical\_reasoner.constraints)  
 self.optimizer.refine(self.meta\_learner.model, self.nas.architecture, self.ethica
l\_reasoner.constraints)  
 self.ethical\_reasoner.refine(self.meta\_learner.model, self.nas.architecture, self.optimize
r.parameters)  
 def continuous\_improvement(self):  
 \# Continuously improve the algorithm  
 self.meta\_learner.adapt
()  
 self.nas.evolve()  
 self.optimizer.adapt()  
 self.ethical\_reasoner.align()  
class MetaLearner:  
 def \_\_init
\_\_(self, input\_dim, output\_dim):  
 self.input\_dim = input\_dim  
 self.output\_dim = output\_dim  
 self.model = s
elf.build\_model()  
 def build\_model(self):  
 \# Construct the meta-learning model architecture  
 model = tf.keras.S
equential(\[  
 tf.keras.layers.Dense(128, activation='relu', input\_shape=(self.input\_dim,)),  
 tf.keras.layers.Dense
(64, activation='relu'),  
 tf.keras.layers.Dense(self.output\_dim, activation='linear')  
\])  
 model.compile(optimize
r='adam', loss='mse')  
 return model  
 def train(self, training\_data):  
 \# Train the meta-learning model  
 self.mo
del.fit(training\_data\[0\], training\_data\[1\], epochs=10, batch\_size=32)  
 def adapt(self, new\_data):  
 \# Adapt 
the meta-learning model to new data  
 self.model.fit(new\_data\[0\], new\_data\[1\], epochs=5, batch\_size=16)  
 def p
redict(self, input\_data):  
 \# Use the meta-learning model to make predictions  
 return self.model.predict(input\_dat
a)  
 def refine(self, nas\_architecture, optimizer\_parameters, ethical\_constraints):  
 \# Refine the meta-learning m
odel based on other components  
 self.model = self.build\_model()  
 self.model.layers\[0\].set\_weights(nas\_architect
ure)  
 self.model.layers\[-1\].set\_weights(optimizer\_parameters)  
 self.model.compile(optimizer='adam', loss=ethical
\_constraints)  
class NeuralArchitectureSearch:  
 def \_\_init\_\_(self, input\_dim, output\_dim, meta\_learner):  
 s
elf.input\_dim = input\_dim  
 self.output\_dim = output\_dim  
 self.meta\_learner = meta\_learner  
 self.architecture
 = self.initialize\_architecture()  
 \# Rest of the NeuralArchitectureSearch class implementation  
 def initialize\_ar
chitecture(self):  
 \# Initialize the neural network architecture  
 return np.random.randn(self.input\_dim \* 128 + 12
8 \* 64 + 64 \* self.output\_dim)  
 def search(self, training\_data, validation\_data):  
 \# Perform neural architectu
re search  
 self.architecture = self.nas\_algorithm(training\_data, validation\_data)  
 def evaluate(self, new\_data):
  
 \# Evaluate the current neural architecture  
 return self.evaluate\_architecture(new\_data)  
 def generate(self, i
nput\_data):  
 \# Generate output using the current neural architecture  
 layer1 = np.dot(input\_data, self.architectu
re\[0\])  
 layer2 = np.dot(layer1, self.architecture\[1\])  
 output = np.dot(layer2, self.architecture\[2\])  
 return
 self.meta\_learner.model.layers\[-1\].predict(output)  
 def nas\_algorithm(self, training\_data, validation\_data):  

 \# Implement the neural architecture search algorithm  
 \# (e.g., using reinforcement learning, evolutionary algorithm
s, or differentiable NAS)  
 return self.optimize\_architecture(training\_data, validation\_data)  
 def optimize\_archi
tecture(self, training\_data, validation\_data):  
 \# Optimize the neural network architecture  
 architecture = self.i
nitialize\_architecture()  
 result = minimize(self.evaluate\_architecture, architecture, args=(training\_data, validati
on\_data))  
 self.architecture = \[  
 result.x\[:(self.input\_dim \* 128)\].reshape(self.input\_dim, 128),  
 result.x
\[(self.input\_dim \* 128):(self.input\_dim \* 128 + 128 \* 64)\].reshape(128, 64),  
 result.x\[(self.input\_dim \* 128
 + 128 \* 64):\].reshape(64, self.output\_dim)  
\]  
 return self.architecture  
 def evaluate\_architecture(self, arch
itecture, training\_data, validation\_data):  
 \# Evaluate the performance of the given neural architecture  
 self.arc
hitecture = \[  
 architecture\[:(self.input\_dim \* 128)\].reshape(self.input\_dim, 128),  
 architecture\[(self.input\
_dim \* 128):(self.input\_dim \* 128 + 128 \* 64)\].reshape(128, 64),  
 architecture\[(self.input\_dim \* 128 + 128 \* 
64):\].reshape(64, self.output\_dim)  
\]  
 output = self.meta\_learner.predict(training\_data\[0\])  
 loss = np.mean(
(output - training\_data\[1\]) \*\* 2)  
 return loss  
 def refine(self, meta\_learner\_model, optimizer\_parameters, e
thical\_constraints):  
 \# Refine the neural architecture based on other components  
 self.architecture\[0\] = meta\_l
earner\_model.layers\[0\].get\_weights()\[0\]  
 self.architecture\[1\] = meta\_learner\_model.layers\[1\].get\_weights(
)\[0\]  
 self.architecture\[2\] = optimizer\_parameters  
class EvolutionaryOptimizer:  
 def \_\_init\_\_(self, input\
_dim, output\_dim, ethical\_constraints, training\_data, validation\_data):  
 self.input\_dim = input\_dim  
 self.outp
ut\_dim = output\_dim  
 self.ethical\_constraints = ethical\_constraints  
 self.training\_data = training\_data  
 sel
f.validation\_data = validation\_data  
 self.population = self.initialize\_population()  
 self.fitness\_scores = self.
evaluate\_population(self.population)  
 def initialize\_population(self):  
 \# Initialize the population of candidate 
solutions  
 population = \[\]  
 for \_ in range(100):  
 individual = np.random.randn(self.input\_dim, self.output\_di
m)  
 population.append(individual)  
 return population  
 def evolve(self, training\_data, validation\_data):  
 \# Ev
olve the population of candidate solutions  
 for generation in range(100):  
 \# Select parents for reproduction  
 par
ents = self.select\_parents(self.population, self.fitness\_scores)  
 \# Perform crossover and mutation  
 offspring = s
elf.reproduce(parents)  
 \# Evaluate the fitness of the offspring  
 offspring\_fitness = self.evaluate\_population(off
spring)  
 \# Replace the least fit individuals in the population  
 def select\_parents(self, population, fitness\_scor
es):  
 \# Implement parent selection mechanism (e.g., tournament selection, roulette wheel selection)  
 return \[popul
ation\[i\] for i in np.random.choice(len(population), size=2, p=fitness\_scores / np.sum(fitness\_scores))\]  
 def repr
oduce(self, parents):  
 \# Implement crossover and mutation operators  
 offspring = \[\]  
 for parent1, parent2 in pa
rents:  
 child = parent1 + 0.5 \* (parent2 - parent1)  
 child += 0.1 \* np.random.randn(\*child.shape)  
 offspring.ap
pend(child)  
 return offspring  
 def evaluate\_population(self, population):  
 \# Evaluate the fitness of the populat
ion  
 fitness\_scores = \[\]  
 for individual in population:  
 fitness = self.evaluate\_individual(individual, self.t
raining\_data, self.validation\_data)  
 fitness\_scores.append(fitness)  
 return fitness\_scores  
 def evaluate\_indi
vidual(self, individual, training\_data, validation\_data):  
 \# Evaluate the fitness of a single individual  
 layer1 
= np.dot(training\_data\[0\], individual)  
 layer2 = np.dot(layer1, individual.T)  
 output = np.dot(layer2, individual
)  
 loss = np.mean((output - training\_data\[1\]) \*\* 2)  
 return -loss  
 def survival\_selection(self, population, 
fitness\_scores, offspring, offspring\_fitness):  
 \# Implement survival selection mechanism (e.g., truncation selectio
n, environmental selection)  
 combined\_population = population + offspring  
 combined\_fitness = fitness\_scores + of
fspring\_fitness  
 sorted\_indices = np.argsort(combined\_fitness)  
 return \[combined\_population\[i\] for i in sorte
d\_indices\[:len(population)\]\], \[combined\_fitness\[i\] for i in sorted\_indices\[:len(population)\]\]  
 def optimiz
e(self, input\_data):  
 \# Optimize the output using the evolved population  
 layer1 = np.dot(input\_data, self.popula
tion\[0\])  
 layer2 = np.dot(layer1, self.population\[0\].T)  
 output = np.dot(layer2, self.population\[0\])  
 return
 output  
 def refine(self, meta\_learner\_model, nas\_architecture, ethical\_constraints):  
 \# Refine the evolutionar
y optimization based on other components  
 self.population = \[meta\_learner\_model.layers\[-1\].get\_weights()\[0\] fo
r \_ in range(100)\]  
 self.ethical\_constraints = ethical\_constraints  
class EthicalConstraint1:  
 def \_\_init\_\_
(self, weight):  
 self.weight = weight  
 def update(self, new\_data):  
 \# Implement the logic to update the first et
hical constraint based on new data  
 return EthicalConstraint1(self.weight \* 0.9)  
class EthicalConstraint2:  
 def \
_\_init\_\_(self, weight):  
 self.weight = weight  
 def update(self, new\_data):  
 \# Implement the logic to update t
he second ethical constraint based on new data  
 return EthicalConstraint2(self.weight \* 0.8)  
class EthicalConstrain
t3:  
 def \_\_init\_\_(self, weight):  
 self.weight = weight  
 def update(self, new\_data):  
 \# Implement the logic
 to update the third ethical constraint based on new data  
 return EthicalConstraint3(self.weight \* 0.7)  
class Ethic
alReasoner:  
 def \_\_init\_\_(self, ethical\_constraints):  
 self.ethical\_constraints = ethical\_constraints  
 \# .
.. (rest of the EthicalReasoner class implementation)  
 def reason(self, training\_data, validation\_data):  
 \# Reaso
n about the ethical implications of the algorithm's outputs  
 self.validate\_outputs(training\_data, validation\_data) 
 
 def align(self, new\_data):  
 \# Align the algorithm's outputs with the ethical constraints  
 self.refine\_ethical\
_constraints(new\_data)  
 def validate\_outputs(self, training\_data, validation\_data):  
 \# Validate the algorithm's
 outputs against the ethical constraints  
 layer1 = np.dot(training\_data\[0\], self.nas.architecture\[0\])  
 layer2 =
 np.dot(layer1, self.nas.architecture\[1\])  
 output = np.dot(layer2, self.nas.architecture\[2\])  
 ethical\_score = s
elf.evaluate\_ethical\_constraints(output)  
 \# Adjust the algorithm's components based on the ethical score  
 def eva
luate\_ethical\_constraints(self, output):  
 \# Evaluate the algorithm's outputs against the ethical constraints  
 eth
ical\_score = 0  
 for constraint in self.ethical\_constraints:  
 ethical\_score += constraint(output)  
 return ethica
l\_score  
 def refine\_ethical\_constraints(self, new\_data):  
 \# Refine the ethical constraints based on new data an
d feedback  
 self.ethical\_constraints = self.update\_ethical\_constraints(self.ethical\_constraints, new\_data)  
 def
 update\_ethical\_constraints(self, constraints, new\_data):  
 \# Implement a mechanism to update the ethical constrain
ts  
 return \[constraint.update(new\_data) for constraint in constraints\]  
 def validate(self, output):  
 \# Validat
e the final output against the ethical constraints  
 ethical\_score = self.evaluate\_ethical\_constraints(output)  
 if
 ethical\_score > 0:  
 return output  
 else:  
 \# Modify the output to align with the ethical constraints  
 return s
elf.align\_output(output)  
 def align\_output(self, output):  
 \# Implement a method to align the output with the ethi
cal constraints  
 return output  
def main():  
 \# Set up the initial parameters  
 input\_dim = 100  
 output\_dim = 
50  
 ethical\_constraints = \[  
 EthicalConstraint1(weight=0.5),  
 EthicalConstraint2(weight=0.3),  
 EthicalConstrai
nt3(weight=0.2)  
\]  
 training\_data = (np.random.randn(1000, input\_dim), np.random.randn(1000, output\_dim))  
 vali
dation\_data = (np.random.randn(200, input\_dim), np.random.randn(200, output\_dim))  
 \# Create the Transcendent AI Al
gorithm  
 algorithm = TranscendentAIAlgorithm(input\_dim, output\_dim, ethical\_constraints, training\_data, validation
\_data)  
 \# Train the algorithm  
 algorithm.train(training\_data, validation\_data, epochs=1000)  
 \# Adapt the algo
rithm to new data  
 new\_data = (np.random.randn(500, input\_dim), np.random.randn(500, output\_dim))  
 algorithm.adap
t(new\_data)  
 \# Execute the algorithm  
 input\_data = np.random.randn(1, input\_dim)  
 output = algorithm.execute(i
nput\_data)  
 print(output)  
if \_\_name\_\_ == '\_\_main\_\_':  
 main()
```
---

     
 
all -  [ Suggestions for improving agents ](https://www.reddit.com/r/LangChain/comments/1civdv4/suggestions_for_improving_agents/) , 2024-05-05-0911
```
I made an open-source tool (k8sAI) using langchain agents. One of the issues I’ve seen is that the agent pretty often re
sponds to users that it can’t perform an action that one of its tools clearly states that it can. And then if asked to d
o it, it will do it. 

Has anyone else seen this come up? Is it mainly down to the system prompt or the tool description
? Or are there other things to tweak?

Appreciate any advice and if you do any work with k8s, feel free to give the tool
 a go! It’s on GitHub.

```
---

     
 
all -  [ Testing RAG chatbot  ](https://www.reddit.com/r/LangChain/comments/1cisa8u/testing_rag_chatbot/) , 2024-05-05-0911
```
I'm building a RAG based chatbot for some geographical data, can someone suggested me what kind of testing can I do to v
alidate the chatbot 
```
---

     
 
all -  [ Help: How do you parse visual content from pitch decks for RAG? ](https://www.reddit.com/r/LangChain/comments/1ciryrj/help_how_do_you_parse_visual_content_from_pitch/) , 2024-05-05-0911
```
I'm building an RAG system with over 100,000 startup pitch decks, and I want to be able to ask questions related to the 
graphs, diagrams, and illustrations in the pitch deck. For example, if I have a competitor slide with an x- and y-axis, 
I want my RAG system to understand that.

Is there something like a visual parser that can extract the visual meaning fr
om each slide, chunk + embed it?
```
---

     
 
all -  [ Seven starter notebooks for AI Agents ](https://www.reddit.com/r/AI_Agents/comments/1ciraov/seven_starter_notebooks_for_ai_agents/) , 2024-05-05-0911
```
Here are seven starter [Python notebooks for AI Agents](https://github.com/ytang07/ai_agents_cookbooks/tree/main)

There
 are four LlamaIndex notebooks and three LangChain notebooks

The LlamaIndex notebooks are:

* RAG Agent w/ FAISS and Op
enAI
* RAG Agent w/ Milvus Lite and OpenAI
* RAG Agent w/ Milvus Docker and OpenAI
* \-Calculator

The LangChain noteboo
ks are:

* RAG Agent w/ Milvus Docker and OpenAI
* RAG Agent w/ FAISS and Open AI
* Calculator

Let me know if you're lo
oking to contribute or if there are any requests for me to add!
```
---

     
 
all -  [ Building chatbot with own data ](https://www.reddit.com/r/LangChain/comments/1ciqzuc/building_chatbot_with_own_data/) , 2024-05-05-0911
```
I'm wondering if Langchain is made to build a chatbot with own trained data. I want to train a chabot with my company da
ta. Similaire to GPTs, is it the good solution ?
Thank you
```
---

     
 
all -  [ get_usable_table_names is returning me nothing. Also, in the database there are multiple schemas and ](https://www.reddit.com/r/LangChain/comments/1cioz1a/get_usable_table_names_is_returning_me_nothing/) , 2024-05-05-0911
```
  
Connection does work well as it print db dialect, but the get\_usable\_table\_names method returns an empty list. Any
 idea?

    db = SQLDatabase.from_uri(f'postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{5432}/{db_name}')
    p
rint(db.dialect)
    print(db.get_usable_table_names())
    print(db.table_info)
```
---

     
 
all -  [ Vectorstore reindexing ](https://www.reddit.com/r/LangChain/comments/1cioq40/vectorstore_reindexing/) , 2024-05-05-0911
```
How does reindexing a vector store impact the addition of new records and their subsequent retrieval? What are the key d
ifferences between reindexing and not reindexing when new records are added?
```
---

     
 
all -  [ Integrating RAG app into an existing HTML website ](https://www.reddit.com/r/LangChain/comments/1cimzf9/integrating_rag_app_into_an_existing_html_website/) , 2024-05-05-0911
```
Hey guys, I have built a RAG application using llama-index, GPT3.5 and LanceDB. I want to integrate it into my company’s
 website. I wanted to know how can I do this? I’m open to using AWS if required for deploying it.
```
---

     
 
MachineLearning -  [ [D] Self-optimizing deterministic LLM memory using dspy, neo4j and vector databases. Need your input ](https://www.reddit.com/r/MachineLearning/comments/1cakjaf/d_selfoptimizing_deterministic_llm_memory_using/) , 2024-05-05-0911
```
Hey there, Redditors!

I'm back with the latest installment on creating deterministic LLM memory.

If you've been follow
ing along, you know I'm on a mission to move beyond the '[thin OpenAI wrapper](https://topoteretes.github.io/cognee/blog
/2023/10/05/going-beyond-langchain--weaviate-and-towards-a-production-ready-modern-data-platform/)' trend and tackle the
 challenges of building robust LLM memory.

  
That's why we built cognee, a python library to process documents and bui
ld knowledge graphs on top of them.

After a few weeks of work, we integrated DSPy and extended cognee.

Here is brief o
verview of the logic: 

[Architecture overview](https://preview.redd.it/fcs3lifx53wc1.png?width=1380&format=png&auto=web
p&s=9316cba52147a5b764565b8438f3f143d8e7ac84)

We aim to understand:

1. Have you tried building knowledge graphs with o
ther tools before?

2. If so, what were the biggest obstacles?

3. How would you approach semantic linking of documents 
without knowledge graphs?

*Remember to give this post an upvote if you found it insightful!*  
*And also star our* [Git
hub repo](https://github.com/topoteretes/cognee)
```
---

     
 
MachineLearning -  [ [D] How to get the source documents from the retrieved context for RAG?  ](https://www.reddit.com/r/MachineLearning/comments/1bvoc1t/d_how_to_get_the_source_documents_from_the/) , 2024-05-05-0911
```
I'm not using Lanchain but only making API calls to an LLM service provider. The retriever is connected to a vector DB, 
and I would like to know what the LLM refers to WITHIN that retrieved context whenever it provides an answer, similar to
 how return_source_documents works in Langchain.

I'm using AzureOpenAI. I couldn't find much in their docs that related
 to returning the source documents. Any help will be greatly appreciated!

```
---

     
 
deeplearning -  [ Seeking Advice: Solving Data Challenges with Large Language Models (LLMs) ](https://www.reddit.com/r/deeplearning/comments/1ca4nc1/seeking_advice_solving_data_challenges_with_large/) , 2024-05-05-0911
```
Hi all

I am presented with a problem that I need to solve using LLM to get the right data from text that has only \~20%
 structure to it. Here's a sample data

XXXXX

AA          BB

CCCC:  (optional DDDD)

C1......(A1) (B1)

C2......(A2) (
B2)

C3.....(A3) (B3)

I am required to anwer with either of these results from A1/B1 till A3/B3 pairs but in order to d
o that I need to go back and ask the user which one of the options C1 to C3 applies to him?

The above is not the most c
omplex structure, it increases in complexity from here so a lot of chatting with user is required to get to the right da
ta that will always exist in the chunk like above.

In the most simplist case the data structure will look like below

X
XXXX

AA          BB

CCCC: ......(A1) (B1)



How would you build a system like this? I am looking at multi-agent syste
ms with Langchain, what about prompt chaining?
```
---

     
 
deeplearning -  [ Share the Coolest Out of The Box LLM Applications That Made You Say 'Wow that was smart' ](https://www.reddit.com/r/deeplearning/comments/1c9e6dj/share_the_coolest_out_of_the_box_llm_applications/) , 2024-05-05-0911
```
Hi, I'm looking at some LLM applications today but apart from guys doing big rags with langchain I don't see too many us
es that are out of the box or that make me say 'wow that was smart to use an LLM here'. Have you seen any cool stuff usi
ng LLMs recently that made you say 'wow, that was smart'?
```
---

     
