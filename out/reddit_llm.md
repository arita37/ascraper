 
all -  [ A demonstration video of RAG feature ](https://www.reddit.com/r/huggingface/comments/19bpbjo/a_demonstration_video_of_rag_feature/) , 2024-01-21-0911
```
 

Currently, this project supports RAG functionality, allowing the creation of knowledge bases, uploading various types
 of documents for vectorization, and enabling the base model to answer questions based on the knowledge base. Achieving 
high precision with RAG functionality requires significant work and research. While the implementation of this project i
s still in its early stages, it serves as a sufficient entry-level research tool. Here is a demonstration video showcasi
ng its capabilities:  
[https://youtu.be/dyIFLISlskI](https://youtu.be/dyIFLISlskI)

&#x200B;

[ Knowledge Base Interfac
e ](https://preview.redd.it/09j18n8pkodc1.png?width=2560&format=png&auto=webp&s=3b40a0b9b9837fa52b67de938e69a3305a69bf7e
)

&#x200B;

[ Upload Docs to Knowledge Base ](https://preview.redd.it/s2he4upqkodc1.png?width=2560&format=png&auto=webp
&s=4ae3d496c89944f82e13f5c812f2cc243e6e7326)

&#x200B;

[ Docs Content View ](https://preview.redd.it/3ojg8oiukodc1.png?
width=2560&format=png&auto=webp&s=a640337695cfedb53849ce448a859dd25f5dec22)

&#x200B;

[ Foundation Model Chat Base on K
B ](https://preview.redd.it/niqcinewkodc1.png?width=2560&format=png&auto=webp&s=4756a32b0efd15966ca64fb399197a387243c3f1
)
```
---

     
 
all -  [ Langchain vs Llama Index ](https://www.reddit.com/r/LangChain/comments/19bnjnz/langchain_vs_llama_index/) , 2024-01-21-0911
```
Hey guys,

I am deciding to implement RAG pipeline into my code

between Langchain and Llama Index, what RAG capability 
yield better performance and what's the main different?

Thanks a lot guys!
```
---

     
 
all -  [ Integrating Azure AI search ](https://www.reddit.com/r/LangChain/comments/19bn28q/integrating_azure_ai_search/) , 2024-01-21-0911
```
Howdy. I have a project which initially made use of LlamaIndex and GithubRepositoryReader to locally persist a vector st
ore containing the contents of a github code repository that I will now be looking to instead integrate into Azure AI se
arch service.

Does anyone know of any resources they can point me to which demonstrates such a project (generating embe
ddings for a code repo, uploading the docs to azure ai search, q&a against said search service)

Thanks!
```
---

     
 
all -  [ Ensemble Retriever with ParentDoc ](https://www.reddit.com/r/LangChain/comments/19bjuov/ensemble_retriever_with_parentdoc/) , 2024-01-21-0911
```
I have tested two retriever methods, 1) Pinecone Hybrid Search and 2) ParentDocument Retriever.

Generally, the ParentDo
cument Retriever performs a lot better but there are instances where the Hybrid search finds interesting nuggets.

I wan
ted to know, if using the ensemble retriever, I can do a combination of BM25 and ParentDocument? Has anyone tried this?


Thanks
```
---

     
 
all -  [ GPT4AllEmbeddings modify model path ](https://www.reddit.com/r/LangChain/comments/19biswa/gpt4allembeddings_modify_model_path/) , 2024-01-21-0911
```
I'd like to modify the model path using GPT4AllEmbeddings and use a model I already downloading from the browser (the al
l-MiniLM-L6-v2-f16.gguf model, the same that GPT4AllEmbeddings downloads by default).

I need it to create RAG chatbot c
ompletely offline.

The langchain documentation chatbot suggests me to use:

>from langchain\_community.embeddings **imp
ort** GPT4AllEmbeddings  
model\_path = '/path/to/your/model.bin'  
gpt4all\_embd = GPT4AllEmbeddings(model=model\_path)


I tried it but it does not work. It completely ignore the model path.

Is there something I'm missing?
```
---

     
 
all -  [ How to Run LangChain Benchmarks to Evaluate Local LLMs from Hugging Face ](https://deci.ai/blog/how-to-run-langchain-benchmarks-with-local-llms-from-hugging-face/) , 2024-01-21-0911
```

```
---

     
 
all -  [ LangChain Questions - Advanced Use Cases ](https://www.reddit.com/r/LangChain/comments/19bfisz/langchain_questions_advanced_use_cases/) , 2024-01-21-0911
```
first time long time. love the platform.

we have build custom tools and agents.

i am trying to extend our implementati
on with the following

\- custom meta-prompts - that are stored on the firm or individual level and could be used as par
t of a workflow

\- Custom meta-data storage - like a list of URLs. this would allow the user to edit this list, and the
n a custom agent (web scraper, etc) could reference it

\- multi-agents? our function calls can only do one thing at a t
ime (one scrape, etc). is there a way to run multiple, in parallel, and return together?

&#x200B;

thanks
```
---

     
 
all -  [ Question about hardware requirements for LangChain and vector DBs ](https://www.reddit.com/r/LangChain/comments/19bcztd/question_about_hardware_requirements_for/) , 2024-01-21-0911
```
Howdy. I am an experienced software engineer working on my first ever project using an LLM. My goal is to use it to repl
ace a rules engine for transaction categorization in an application I have. I will feed in the new transactions, list of
 categories, plus data on past categorized transactions, to produce the new output. All results will go through manual r
eview prior to being accepted, which is the current behavior with the existing rules engine anyway.

This will be deploy
ed to my home server which has a powerful CPU, lots of RAM, but a shit GPU. Because of this, my plan is to use a cloud L
LM like ChatGPT. However I want to run the Vector database (Cassandra, chroma, etc. haven't picked yet) on the server. I
 know the embeddings will be generated by the LLM and just stored in the Vector DB, so I don't need to worry about the h
ardware needs for that.

My question is around querying the Vector DB. Are there special hardware requirements (ie, GPU-
preferred operations) for running those queries? I'm not worried about operations that a CPU can handle well, only stuff
 that requires a beefier GPU.

Thanks in advance
```
---

     
 
all -  [ Resume Feedback and Career Advice Needed! ](https://www.reddit.com/r/developersIndia/comments/19ba933/resume_feedback_and_career_advice_needed/) , 2024-01-21-0911
```
Here is my  resume, looking for feedback and career advice. Any suggestions on how to improve or opportunities I should 
explore? Thanks in advance!    


 I want to switch my job; until now, I was applying at random places and did some cold
 emails with no response. Other than that, I received two offers from UK who saw one of my project on GitHub, emailed me
, and offered an interview. However, the interview is still pending, and they are taking time to respond. I also have an
other interview opportunity for a frontend role in a crypto startup; the interview is on Wednesday next week. Let's hope
 for the best!  


A bit about me: I come from a non-tech background, previously involved in sports (Played cricket at t
he national level). However, my love for computers and software led me to choose a career in tech. While I don't have a 
strong DSA & LeetCode profile, I am currently learning and improving in that area as well.

My Github: [https://github.c
om/ChetanXpro](https://github.com/ChetanXpro)  


Resume:

[Resume](https://preview.redd.it/ulxm6jrl2ldc1.png?width=1058
&format=png&auto=webp&s=60655279b2fd8c67f4f7332ea847a23835dddd72)
```
---

     
 
all -  [ Relation between LiteLLM and LangChain ](https://www.reddit.com/r/LangChain/comments/19b9fzw/relation_between_litellm_and_langchain/) , 2024-01-21-0911
```
Hello,

I am currently looking into using LLMs for a project and figured LiteLLM might be a good start to test out diffe
rent models. With a bit of research I saw that langchain is basically the number one library for doing this kind of thin
gs, becauso of RAG support etc.

What I do not quite understand is, what is the relation between these tools? Does LangC
hain use LiteLLM or vice versa? Is there even a link or are these just completely seperate tools? There is also autogen,
 which is basically LangChain with mutiple agents developed by microsoft if I understand it correctly.

What I found was
 the mention of LangChain in LiteLLMs docs: [https://docs.litellm.ai/docs/langchain/](https://docs.litellm.ai/docs/langc
hain/) where ChatLiteLLM is imported from LangChain, does that mean there is LiteLLM integrated into LangChain?

&#x200B
;

 I am quite confused here, would appreciate any input on this topic. Thanks!
```
---

     
 
all -  [ Özgeçmişime bakabilir misiniz? (Eleştirileriniz üzerine sıfırdan yaptım.) ](https://www.reddit.com/r/CodingTR/comments/19b8fbm/özgeçmişime_bakabilir_misiniz_eleştirileriniz/) , 2024-01-21-0911
```
Merhaba, ben daha önce de özgeçmişimi sizinle paylaşmıştım. Yararlı eleştirileriniz üzerine tamamen sıfırdan yeniden yap
tım. Bir çok eksiği bana göstermiş oldunuz. Şimdiki hali nasıl olmuş bakabilir misiniz? Ağustos ayında mezun oldum, yeni
 mezun sayılırım. Veri bilimi alanında kariyer hedefliyorum.

https://preview.redd.it/ysbhtfkdikdc1.jpg?width=1653&forma
t=pjpg&auto=webp&s=8ac110d126fb7930b0ef6284de05efabb947e7fd

https://preview.redd.it/w0y3sfkdikdc1.jpg?width=1653&format
=pjpg&auto=webp&s=28f0a21179543b9b4c46fda35ea1f4a9964dcc7d
```
---

     
 
all -  [ Multiple PDF's vs single large file? ](https://www.reddit.com/r/LangChain/comments/19b40f8/multiple_pdfs_vs_single_large_file/) , 2024-01-21-0911
```
Hi, I build a chat bot with langchain.js and one of the tools of the bot is using a  VectorDBQAChain connecred to a vect
or store that is basicaly one big txt file. The model I use is  gpt-3.5-turbo-0613 and the chunck size of the text split
ter is 1000. There are just a hundred rows of information. It works ok, but it takes too much time and sends a lot of em
bedings until it can answer a question correctly.

Now I am asked to create similar chat bot but working with a few thou
sand PDF's and I wonder if this is even possible? I saw there is DocumentLoader, but is it needs to send embedings of al
l the content until it can formulate an answer it is useless. The cost will be too high and the time it takes will be en
ourmous. Maybe I am missing something here?
```
---

     
 
all -  [ Is there any common loaders in langchain to load all types of documents?? ](https://www.reddit.com/r/LangChain/comments/19b2ivj/is_there_any_common_loaders_in_langchain_to_load/) , 2024-01-21-0911
```
I am into creating an interactive chatbot that can take inputs from multiple data sources like pdf, word file, text file
, excel files etc. I am using Pinecone retriever with Langchain wrapper on top of it. When I go for DirectoryLoader usin
g glob function, I’m unable to load other file types except PDF and convert it to vector embeddings. Need a way to load 
rest of the documents and process it further for embeddings.
```
---

     
 
all -  [ Introducing Langfuse - Open Source Observability, Analytics and AI Engineering for LLM apps ](https://www.reddit.com/r/LLMDevs/comments/19apbed/introducing_langfuse_open_source_observability/) , 2024-01-21-0911
```
Max, Marc and Clemens here, founders of **Langfuse** ([https://langfuse.com](https://langfuse.com)). We’re building OSS 
tooling to help developers iterate on LLMs in production.   
We came onto the scene with a **Show HN** back in August ([
https://news.ycombinator.com/item?id=37310070](https://news.ycombinator.com/item?id=37310070)). Back then we were still 
a rather simple solution for logging out traces. We had just started adding scrappy analytics through Looker Studio. 

*
*I wanted to take this opportunity to introduce us to the Reddit community.**

Since our first launch we’ve shipped: 

*
 Dashboards: custom charts on top of tremor.so which replaced looker
* SDKs 2.0: performance upgrades, fewer dependencie
s, more stable
* Sessions: group traces into sessions & replay user interactions
* Integrations: added integrations for 
OpenAI, Langchain, Flowise, Langflow, LiteLLM
* Easier self-hosting: automatic db migrations by pulling latest container

* Evals: model-based evals through e.g. Ragas \[1\] framework
* Exports: rich source data as .csv, JSON/L & access to y
our data via GET API
* Datasets: run tests on sets of inputs and expected outputs
* UI: improvements including hotkeys, 
tables, filtering, search

**Latest**

* Prompt Management: Host your prompts in Langfuse, get automatic versioning and 
keep your code tidy. Edit in UI/SDK and invoke in your code through `langfuse.get_prompt('prompt-slug')`

The repo is av
ailable under **MIT license** and we’re proud to support a vibrant community of self-hosting users (**one docker contain
er**) through GitHub and Discord. 

We’ll be around in the comments and look forward to hearing what you think. We take 
it to heart!

GitHub: [https://github.com/langfuse/langfuse/](https://github.com/langfuse/langfuse/)

Try a demo: [https
://langfuse.com/docs/demo](https://langfuse.com/docs/demo) -- **+ there is a generous free tier and the option to self-h
ost Langfuse.**

\[1\] [https://github.com/explodinggradients/ragas](https://github.com/explodinggradients/ragas) 
```
---

     
 
all -  [ How to achieve relevance question leading ](https://www.reddit.com/r/LangChain/comments/19an810/how_to_achieve_relevance_question_leading/) , 2024-01-21-0911
```
When a user asks a question, in what way can I achieve the display of similar questions. For example: the user asks for 
Bob's age? I will give 4 related questions: who is Bob, Bob's gender,.... But these questions are not random, they are g
iven based on my profile
```
---

     
 
all -  [ How to dockerise a Langchain app ](https://www.reddit.com/r/LangChain/comments/19amgmz/how_to_dockerise_a_langchain_app/) , 2024-01-21-0911
```
Hi everybody I was wondering how would it be like a typical Dockerfile for running a langchain pipeline. 
```
---

     
 
all -  [ Using Agent in langChain I want to abort in specific situations, how should I design it ](https://www.reddit.com/r/LangChain/comments/19ambyh/using_agent_in_langchain_i_want_to_abort_in/) , 2024-01-21-0911
```
I want to realize such a scenario:
Let's say I have a `name` field stored in my db, and when the user asks for bob, I ma
y have Bob, Boe... in the db. If there is no exact match for bob, I want the bot to guide the user: do you want to query
 Bob or boe?

What I understand is that it's actually how to make the bot stop to continue the query and output the resu
lt under certain circumstances during the execution, how should I implement this using langChain? Can I do it by `bind(s
top='xx')`?
```
---

     
 
all -  [ [For Hire] Programmer/Web Developer/IT Consultant (Python, PHP, AI, etc.) ](https://www.reddit.com/r/forhire/comments/19alzyp/for_hire_programmerweb_developerit_consultant/) , 2024-01-21-0911
```
To get in contact, please message me, I don't use the chat thing and might miss you or reply very late. Then we can swit
ch to email/discord/telegram or whatever else. Apologies for starting with this, but many missed it when it was lower.


I'm a programmer/web developer with 13 years of professional experience. I am available for all sorts of programming and
 web development tasks.

I also offer consulting services. If you need something done, but don't know how exactly, I can
 help. I'm an excellent researcher and I communicate well. I will work with you to find the best solution for your probl
em.

My services include, but are not limited to:

* websites

* desktop applications

* AI integration (chatGPT API, la
ngchain, whatever else turns up)

* integration with APIs and other webservices

* all kinds of scripts

* task automati
on

* website optimization

* debugging

* plugins for existing software

* bots (Reddit, Telegram, etc)

* code audits


If you're looking for someone to take care of a variety of different tasks, I can offer continuous support.

My preferr
ed environment is Python with Django, but I work with anything Python or PHP based. I have no problem with learning new 
technologies that are needed for the project.

Rate is $50/h. Can also do fixed price by project, but only if the projec
t/milestone is well-defined.

Satisfied customers:

https://www.reddit.com/r/testimonials/comments/2e8gqy/pos_uqui_need_
a_backend_web_dev_look_no_further/

https://www.reddit.com/r/testimonials/comments/7fsdze/pos_hiring_uqui_was_an_example
_of_how_it_should/

https://www.reddit.com/r/testimonials/comments/80pu9l/pos_uqui_great_work_detailed_and_fast/

https:
//www.reddit.com/r/testimonials/comments/b0nx68/uqui_is_a_hardworking_intelligent_honest_apps/

https://www.reddit.com/r
/testimonials/comments/j3mz3p/uqui_is_a_great_web_development_consultant_with/

https://www.reddit.com/r/testimonials/co
mments/v40ay3/pos_uqui_is_a_great_backend_dev_to_work_with/

Please note: I am not a designer. To make it clear, it mean
s zero aesthetic sense.
```
---

     
 
all -  [ Message Repetition ](https://www.reddit.com/r/StreamlitOfficial/comments/19akk9i/message_repetition/) , 2024-01-21-0911
```
 

Hello! I need some help with my code. The expected output of the code below is:  
user : Solar Energy of “one of the 
specified cities”, the bot shows the form to prompt the user of the data then user clicks on submit then the bot display
s solar energy is “certain number”. However, when the user clicks on submit the bot repeats the first message that is So
lar Energy of “certain city”, then shows the solar energy value.

&#x200B;

    
    import os
    import streamlit as s
t
    from displayer import bot_template, user_template
    from dotenv import load_dotenv
    from langchain_openai imp
ort ChatOpenAI
    from langchain.schema import SystemMessage, HumanMessage, AIMessage
    from ML.Ml import CityWeather
Data
    
    def init():
        load_dotenv()
    
        # Loading OpenAI API key
        if os.getenv('OPENAI_API_K
EY') is None or os.getenv('OPENAI_API_KEY') == '':
            print('OPENAI_API_KEY is not set yet')
            exit(1
)
        else:
            print('OPENAI_API_KEY is set')
        
    
    def main():
        init()
    
        # I
nitialize LangChain Chat
        chat = ChatOpenAI(temperature=0)
    
        if 'messages' not in st.session_state:
  
          st.session_state.messages = [
                SystemMessage(content='You are a helpful assistant.')
          
  ]
            
        form_submission = False  #Boolean variable to track whether the form is submitted
        
    
    st.header('Green Optimizer 🤖')
    
        with st.sidebar:
            # CHATTING CODE
            user_input = st
.text_input('Enter your message:')
            
            if user_input:
            #if user_input:
                s
t.session_state.messages.append(HumanMessage(content=user_input))
                with st.spinner('Thinking..'):
       
             if any(city in user_input.lower() for city in ['jeddah', 'skaka', 'riyadh', 'dammam']):
                   
     user_city = None
                        for city in ['jeddah', 'skaka', 'riyadh', 'dammam']:
                     
       if city in user_input.lower():
                                user_city = city
                                b
reak
    
                        # If city name is found, proceed with solar energy analysis
                        if
 user_city:
                            # Display the form for user input
                            st.write(f'Welcome
! Please enter the following information for {user_city.capitalize()}:')
                            with st.form(key='w
eather_form'):
                                ALLSKY = st.number_input('Enter ALLSKY:')
                               
 CLRSKY = st.number_input('Enter CLRSKY:')
                                pressure = st.number_input('Enter pressure:')

                                temperature = st.number_input('Enter temperature:')
                                moi
sture = st.number_input('Enter moisture:')
    
                                submit_button = st.form_submit_button(la
bel='Submit')
    
                            # If the form is submitted, calculate and display the result
            
                if submit_button:
                                form_submission = True
                               
 # Create CityWeatherData instance
                                weather_data = CityWeatherData(city=user_city)
    
 
                               # Analyze weather for the selected city
                                solar_energy = we
ather_data.analyze_weather(
                                    ALLSKY=ALLSKY, CLRSKY=CLRSKY, temperature=temperature, p
ressure=pressure, moisture=moisture
                                )
                                # Append the user 
and AI messages to the conversation
                                st.session_state.messages.append(AIMessage(content=f
'The Solar Energy in {user_city.capitalize()} is: {solar_energy}'))
    
                        else:
                 
           # If no valid city name is found, proceed with regular chat
                            response = chat(st.se
ssion_state.messages)
                            st.session_state.messages.append(AIMessage(content=response.content))

                    else:
                        # If no city name is mentioned, proceed with regular chat
            
            response = chat(st.session_state.messages)
                        st.session_state.messages.append(AIMessag
e(content=response.content))
    
        # Displaying all the messages the user had by fetching them
        messages =
 st.session_state.get('messages', [])
    
        # Looping through all the messages, if 1 user(odd number) display it 
from the human position.
        # If two users(even number) display it from the bot position.
        for i, msgs in en
umerate(messages[1:]):
            if i % 2 == 0:
                st.markdown(user_template.replace('{{MSG}}', msgs.cont
ent), unsafe_allow_html=True)
            else:
                st.markdown(bot_template.replace('{{MSG}}', msgs.content
), unsafe_allow_html=True)
    
    if __name__ == '__main__':
        main()

Many Thanks in Advance!
```
---

     
 
all -  [ Describe your local LLM Setup ](https://www.reddit.com/r/LocalLLaMA/comments/19ak9x1/describe_your_local_llm_setup/) , 2024-01-21-0911
```
I'd like to understand what you guys use as your local setup. What models (eg llama/mistral/qwen) do you use in conjucti
on with what tools ( eg memGPT, autoGPT, langchain, crewAI and whatnot).   
Do you have different models/tools for diffe
rent use cases? How much of your workflow is automated with LLMs.  
And how often (if at all) do you finetune models to 
suit your needs better?   
I feel that there is so much potential in local LLMs that I'm missing out on and would love t
o learn from you guys...  

```
---

     
 
all -  [ Streaming with Llamacpp, Langchain and FastAPI ](https://www.reddit.com/r/LangChain/comments/19aevbz/streaming_with_llamacpp_langchain_and_fastapi/) , 2024-01-21-0911
```
Hi,

I am using Llamacpp to load my models and streaming in the terminal works with the `StreamingStdOutCallbackHandler(
)` and the parameter `streaming=True`.

Now I want to enable Streaming in FastAPI responses, but didn't find a solution 
that satisfies my requirements. Many tutorials wait until the response from the LLM is ready and then streaming it. But 
I want to see a 'live' streaming of the tokens, otherwise it will take too long until the user gets a response (especial
ly for longer texts).

So does anyone know to do this with Llamacpp and FastAPI?

&#x200B;

(I am NOT using any OpenAI m
odel, I am using GGUF models locally)
```
---

     
 
all -  [ What should I do to get a job? ](https://www.reddit.com/r/developersIndia/comments/19ae43n/what_should_i_do_to_get_a_job/) , 2024-01-21-0911
```
This is my resume (not everything mentioned in this are the things i am an expert at...some are just on the very basic l
evel like i used them for a project that is it):
Skills
Programming Languages
* Python * R Programming
* C * Bash
To
ols
* Github & HuggingFace * FastAPI
* SQL & VectorDB * Locust
* Docker * AWS & Render
Technologies
* AI/ ML/ DL /N
N * Computer Vision
* NLP (L.L.M's & Generative AI) * Linux
* API Testing * Technical Blogs & S.E.O.
Libraries/ Frame
works
Langchain, Llama-Index, Pinecone ,TensorFlow/ Keras, Dlib, Sci-Kit Learn, Openai, Chainlit,
Streamlit, Goose, , 
Gradio, OpenCV, FaceRecognition, Pandas, Pillow, etc.

Also i have done about 7-8 internships(mostly in the ai field)...
. currently doing one as an AI/ML developer intern and freelancing at gfg.


In my final sem of Btech AI.....what are th
e scopes for me....unable to land a job....and i need a good job to show ROI for my btech ai (it is highly expensive)...
. hoping for 12-14 lpa🥲....dont kill me for this hope (earlier it used to be 16-20 but then i started understanding the 
system and conditions)

My scopes??
```
---

     
 
all -  [ Deployment of RAG Based QNA Model ](https://www.reddit.com/r/LangChain/comments/19adx5s/deployment_of_rag_based_qna_model/) , 2024-01-21-0911
```
Hello People
I've joined this community very recently,
I'm working on a project, where I'm creating a QnA model on exist
ing magazines of my college.
I'm experimenting between different embeddings (openai, bge, gte..), vector stores (FAISS, 
Chroma db,...), document chunking ...
Finally I have to deploy all of this into a webpage 
Can you suggest a way forward
?
```
---

     
 
all -  [ Template population ](https://www.reddit.com/r/AiAutomations/comments/19a9rup/template_population/) , 2024-01-21-0911
```
In the domain I work in there are a lot of templates used that often for specific reasons need to be printed out and fil
led in by hand still.

I want to be able to generate populated versions of these templates using an AI that I train(?) o
r fine tune(?) on a lot of specific domain based information. I would prefer to be able to make that domain hyper specif
ic as well and it's ok if the model doesn't know almost anything beyond that. Is this something that is possible? If so 
how?

I have a setup using langchain, openAI and some python libraries where I can upload PDFs on the specific domain to
 build knowledge and have a chat with an AI about specifically those PDFs. What I want to do it take it to the next step
 so I can write 'create template A.pdf populated with the information for hyperspecific domain X'
```
---

     
 
all -  [ Advice on LLM based inventory search ](https://www.reddit.com/r/LLMDevs/comments/19a67lp/advice_on_llm_based_inventory_search/) , 2024-01-21-0911
```
I am a noob in the LLM space, and am looking for some advice towards system design for LLM based inventory search. Basic
ally I envision using a chat based interface to search a proprietary inventory (database), to users. The way I see it is
 that there is a two fold problem:  


1. Understanding or extracting user input/paramaters to be able to do backend cal
ls/api calls/ database queries etc. in order to get real-time/cached data.
2. (Optional) Understanding the response from
 the api, and having follow up conversation with the user, based on the model's understanding of the response. 

What wo
uld be the right tools to explore to get started on either of the two? Furthermore in which scenario/how can I ensure da
ta privacy, as well as ownership of the tuned model?  


Apologies if this is too vague, while I know titbits here and t
here about langchain, LLMs etc. I have no idea what's the right approach to take, and the current tool exploration path 
is pretty much of whatever I hear in blogs/random google search discovery.
```
---

     
 
all -  [ Langchain appears to be a library with unnecessary complexities. ](https://www.reddit.com/r/LangChain/comments/19a5flh/langchain_appears_to_be_a_library_with/) , 2024-01-21-0911
```
I found langchain to be overly complex for my needs, leading me to opt for coding from scratch. It seemed like langchain
 created vectordb per table, rather than consolidating them within one table, which wasn't efficient according to my pre
ferences.

Despite the complexities, I required a tool like langchain for splitting my documents into chunks. This quest
 took up more of my time, and I couldn't fully comprehend the hype surrounding langchain as the epitome of freedom.

Non
etheless, I took matters into my own hands and devised my splitting technique. While it may not be the most optimal solu
tion, it suits my requirements perfectly. I leveraged the spaCy Library and its NLP capabilities to separate my document
s into sentences, providing me with the desired outcome and a sense of freedom.
```
---

     
 
all -  [ Apichain ](https://i.redd.it/f576w3wcdadc1.jpeg) , 2024-01-21-0911
```
 when streaming apichain, it prepends the api url to a streaming text response. Any ideas why it would do this ?
```
---

     
 
all -  [ Cost x Prompt too high using GPT 4 ](https://www.reddit.com/r/LangChain/comments/19a4pxq/cost_x_prompt_too_high_using_gpt_4/) , 2024-01-21-0911
```
Hey guys! I am developing a expense chatbot on WhatsApp but the cost per customer is very high. Each request is about 0.
0884 and we are expecting each customer to do at least 100 request per month. Which would mean $8 per customer.

&#x200B
;

We have a set of tools that is elevating the cost because it is passed as context, so my idea was to store the tools 
in a db, use GPT-3.5 to decide which tool to use. Pass just one tool to GPT 4 in the prompt and reduce the cost. But the
 costs would still be high at $0.025 per request.   


I have two questions:  


1. What do you think about my solution?

2. Do you think using Llama2 would be a good idea to create a chatbot? And if so do you have any docs on how to do so.


THanks!
```
---

     
 
all -  [ More than 500 jobs applied for entry level ML engineer none even game me a single interview. Please  ](https://www.reddit.com/r/resumes/comments/199zp4r/more_than_500_jobs_applied_for_entry_level_ml/) , 2024-01-21-0911
```
&#x200B;

https://preview.redd.it/4f4jl3srb9dc1.png?width=1428&format=png&auto=webp&s=98f3b971f3e315ebbe688b72faef7829a8
1601c0
```
---

     
 
all -  [ I love writing tutorials. What are you most interested in? ](https://www.reddit.com/r/LocalLLaMA/comments/199ut0n/i_love_writing_tutorials_what_are_you_most/) , 2024-01-21-0911
```
I've got a cool job where I get to go out and learn about stuff so that I can write about it.

There's a gap in my sched
ule, enough for a decently in-depth blog. I wanted to see what the community was most interested in so that help out.

H
ope this doesn't come off as selfish promo, but here's a few examples of stuff I've done in the past:

• [Generating Tex
t with GGUF](https://colab.research.google.com/drive/1y4RCTIfTTb53b_S95xl4IZaW8am6sBxz)

•[Evaluating Advanced Retrieval
 Methods Using LangChain + ragas](https://colab.research.google.com/drive/1SNgF0MudcIAIBibmi-YkWFwn8Nptt4r5)

• [Evaluat
ing the Impact of Decoding Strategies on Instruction Following](https://colab.research.google.com/drive/1UFBWOUbUUAHTf7i
lCGhPtGDMDeYXrJzt)

• [DeciLM-7B Head to Head Against Mistral-7B on Chain of Thought Tasks](https://colab.research.googl
e.com/drive/11VmmWiY_K76WHepVNp2OU6w3VGuMjBVm)

• [How to Run LangChain Benchmarks with Local LLM from Hugging Face](htt
ps://colab.research.google.com/drive/1ehBzDjUQrioa4abvTIWtABU1ENI2l_2g)

Cheers!
```
---

     
 
all -  [ New Data API for Astra [N] ](https://www.reddit.com/r/MachineLearning/comments/199uobn/new_data_api_for_astra_n/) , 2024-01-21-0911
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

     
 
all -  [ [D] While using function calling or tools on openai or langchain, does openai have access to the dat ](https://www.reddit.com/r/MachineLearning/comments/199t8be/d_while_using_function_calling_or_tools_on_openai/) , 2024-01-21-0911
```
I am working on a client project and I am using langchain's tools and agents. I want to know if the data is getting pass
ed to openai or is it just like that - Output of one function is being directly passed to the second function with the k
nowledge of openai.
```
---

     
 
all -  [ Getting 'value is not a valid dict (type=type_error.dict)' ](https://www.reddit.com/r/LangChain/comments/199rxcn/getting_value_is_not_a_valid_dict_typetype/) , 2024-01-21-0911
```
    docsearch_in_os = OpenSearchVectorSearch(
 opensearch_url=os.environ.get('OPENSEARCH_URL'),
 index_name=index_name,

 embedding_function=bedrock_embeddings,
 http_auth=auth,
 timeout=30,
 use_ssl=True,
 verify_certs=True,
 connection_cla
ss=RequestsHttpConnection,
 is_aoss=True,
    )
 print(user_input)
 print(docsearch_in_os)
 chain = RetrievalQA.from_cha
in_type(
 llm=llm,
 chain_type='stuff',
 retriever=docsearch_in_os.as_retriever(),
 return_source_documents=False,
 chai
n_type_kwargs={'prompt': PROMPT},
    )
 result = chain({'query': user_input})
 print(result)
 answer = result['result']


The above block of code is working fine with the opensearch vector store I created manually via Sagemaker. But somehow
, the same piece of code isn't working when the Opensearch vector store is created via The AWS Bedrock Console. I am get
ting error:  
'value is not a valid dict (type=type\_error.dict)'

https://preview.redd.it/qd5en8unp7dc1.png?width=2880&
format=png&auto=webp&s=af4809165591a12514aa05ade0a8eef29de23e1d
```
---

     
 
all -  [ Project: QA on any PDF document using RAG and VectorDB ](https://i.redd.it/c0cfiqr0o7dc1.jpeg) , 2024-01-21-0911
```
The Smart PDF Reader is a comprehensive project that harnesses the power of the Retrieval-Augmented Generation (RAG) mod
el over a Large Language Model (LLM) powered by Langchain. Additionally, it utilizes the Pinecone vector database to eff
iciently store and retrieve vectors associated with PDF documents. This approach enables the extraction of essential inf
ormation from PDF files without the need for training the model on question-answering datasets.

Find the GitHub repo: [
here](https://github.com/Arshad221b/RAG-on-PDF)
```
---

     
 
all -  [ Which are the best tools to create a Chat App that can use multiple models? ](https://www.reddit.com/r/LocalLLaMA/comments/199opgz/which_are_the_best_tools_to_create_a_chat_app/) , 2024-01-21-0911
```
Hello,

I want to make a chat app that can run multiple models but I am not sure if I should start with LangChain + Olla
ma, based on what I understand LangChain can make some complex tasks and Ollama can answer api calls that can load diffe
rent models.

Unfortunately this combo is not perfect because the visualization of the chat must be custom - due to that
 I came across ChainLit but it didn't provide in-house Chat History that can work with self-hosted models.

Maybe I am d
oing something wrong or my research is not enough but if anyone can help me out in finding a good stack that can run a s
imple chat that can be made into a mini-custom project with chat history/context it would be great.

Thanks,
```
---

     
 
all -  [ Streaming JSON values? ](https://www.reddit.com/r/OpenAI/comments/199o4u2/streaming_json_values/) , 2024-01-21-0911
```
I'm building a chatbot and have requirements to stream the values of returned JSON, but not the keys. For example in too
l calling one of the variables is 'Reasoning' where GPT4 explains the reason it picked this tool that we want to display
.  


Parsing the JSON once completed is trivial, but I need to stream the values for this key.


Example:  
[{'Thought'
: 'Prompt is for internal data so using the get_internal_data tool'}]


I want to ignore everything and only return the 
tokens making up 'Prompt is for internal data so using the get_internal_data tool'.


Oddly I cannot find much on this o
nline. How can this be achieved?

I'm using Azure OpenAI GTP4 and tool calling (no langchain).
```
---

     
 
all -  [ Struggling with LangChain and ChromaDB - Help Needed! ](https://www.reddit.com/r/LangChain/comments/199ne8a/struggling_with_langchain_and_chromadb_help_needed/) , 2024-01-21-0911
```
 

I'm reaching out because I'm having a frustrating issue with LangChain and ChromaDB, and I could really use some help
 from those more experienced than myself. Here's my situation:

I have thousands of text documents that contain detailed
 information, and I'm trying to utilize LangChain and ChromaDB (BAAI/bge-large-en-v1.5) to extract meaningful insights f
rom them. The problem I'm encountering is that when I run the pipeline, it keeps fetching the wrong details for certain 
cases.

For example, let's say I have a case number 'P L D 1949 Dacca 13'. Instead of retrieving the relevant informatio
n for that specific case, the model returns the details for 'P L D 1949 Dacca 30' instead. This is happening consistentl
y across many documents, and I'm at a loss as to why this is occurrcing.

Here are some additional details about my setu
p and process:

\* I'm relatively new to LangChain, so please bear with me if my mistake is obvious.

\* I've followed t
he instructions provided by the LangChain team for setting up the environment and running the pipeline.

\* My dataset c
onsists of plain text files containing various types of legal documents.

\* I'm using the BAAI/bge-large-en-v1.5 model 
for text embedding

Thank you in advance for taking the time to read through my post and offer assistance. Your expertis
e means a lot to me, and I look forward to hearing your thoughts and suggestions.
```
---

     
 
all -  [ Langsmith ](https://www.reddit.com/r/LangChain/comments/199nbwa/langsmith/) , 2024-01-21-0911
```
Hey I was using langhchain before the 0.1.0 update and I'm using it in a project that will go live soon, however I want 
to move to 0.1.0 but my custom agent completely breaks and I feel like LangSmith is my only option. Is there a way to ge
t an invite code as I have been on the wait list for a bit.
```
---

     
 
all -  [ Struggling with LangChain and ChromaDB - Help Needed! ](https://www.reddit.com/r/LanguageTechnology/comments/199n6dl/struggling_with_langchain_and_chromadb_help_needed/) , 2024-01-21-0911
```
  
I'm reaching out because I'm having a frustrating issue with LangChain and ChromaDB, and I could really use some h
elp from those more experienced than myself. Here's my situation:  
  
I have thousands of text documents that contain
 detailed information, and I'm trying to utilize LangChain and ChromaDB (BAAI/bge-large-en-v1.5) to extract meaningful i
nsights from them. The problem I'm encountering is that when I run the pipeline, it keeps fetching the wrong details for
 certain cases.  
  
For example, let's say I have a case number 'P L D 1949 Dacca 13'. Instead of retrieving the rele
vant information for that specific case, the model returns the details for 'P L D 1949 Dacca 30' instead. This is happen
ing consistently across many documents, and I'm at a loss as to why this is occurrcing.  
  
Here are some additional 
details about my setup and process:  
  
\* I'm relatively new to LangChain, so please bear with me if my mistake is o
bvious.  
\* I've followed the instructions provided by the LangChain team for setting up the environment and running t
he pipeline.  
\* My dataset consists of plain text files containing various types of legal documents.  
\* I'm using
 the BAAI/bge-large-en-v1.5 model for text embedding   
  
Thank you in advance for taking the time to read through 
my post and offer assistance. Your expertise means a lot to me, and I look forward to hearing your thoughts and suggesti
ons.
```
---

     
 
all -  [ Langchain 0.1.1 is not working with pinecone-client 3.0.0 ](https://www.reddit.com/r/LangChain/comments/199mklo/langchain_011_is_not_working_with_pineconeclient/) , 2024-01-21-0911
```
    from langchain_community.vectorstores import Pinecone
    from langchain_openai import OpenAIEmbeddings
    from pin
econe import Pinecone as PineconeClient
    pinecone=PineconeClient(
                api_key= {API KEY}
                
)
    embeddings = OpenAIEmbeddings(
        model='text-embedding-ada-002',
        openai_api_key={open_ai_api_key}
  
  )
    vectorstore = Pinecone.from_existing_index(index_name, embeddings)

This gives the following error:  


raise Pi
neconeConfigurationError('You haven't specified an Api-Key.')

pinecone.exceptions.PineconeConfigurationError: You haven
't specified an Api-Key.  


  
Although I provided all the required api keys in line #5 and line #9
```
---

     
 
all -  [ mistral & agents ](https://www.reddit.com/r/MistralAI/comments/199lrht/mistral_agents/) , 2024-01-21-0911
```
is anybody tried mistral with agents using langchain?  its good with function calling?
```
---

     
 
all -  [ Talk with your Data! ](https://www.reddit.com/r/MediumApp/comments/199iv6z/talk_with_your_data/) , 2024-01-21-0911
```
Read this article to learn how to build a GenAI bot, with LangChain and Streamlit in Python. 

Give it data and get answ
ers!
```
---

     
 
all -  [ How do I improve RAG extracted document list ](https://www.reddit.com/r/LangChain/comments/199ejhc/how_do_i_improve_rag_extracted_document_list/) , 2024-01-21-0911
```
I am building a RAG app with langhain, how do you ensure you get the optimal results from your vector store so that the 
extracted documents and prompt sent to the LLM contain all the relevant information? I had to increase topK to as high a
s 50 before getting a good result.
```
---

     
 
all -  [ Example Structured Chat Agent with Complete History ](https://www.reddit.com/r/LangChain/comments/199edvi/example_structured_chat_agent_with_complete/) , 2024-01-21-0911
```
I noticed that in the langchain documentation there was no happy medium where it's explained how to add a memory to both
 the AgentExecutor and the chat itself. If you don't have it in the AgentExecutor, it doesn't see previous steps. In the
 custom agent example, it has you managing the chat history manually.

I've created an example based on the langchain do
cs that does this here: [https://github.com/ThreeRiversAINexus/sample-langchain-agents/blob/main/structured\_chat.py](ht
tps://github.com/ThreeRiversAINexus/sample-langchain-agents/blob/main/structured_chat.py)

Please let me know what you t
hink and if there are any other agents you need help with.

Edit: I've added a string splitting tool and gave an example
 using it to prove that it has memory of the chats as well as the agent executor steps.
```
---

     
 
all -  [ How do I use Lang Chain for AI Recommendations on my app? ](https://www.reddit.com/r/LangChain/comments/1995ips/how_do_i_use_lang_chain_for_ai_recommendations_on/) , 2024-01-21-0911
```
Hello. 

I'm creating a social media app and I intend to use AI for post recommendations. How do I use Lang Chain to ach
ieve that? Any suggestions?
```
---

     
 
MachineLearning -  [ [D] Code vs JSON output for LLM agents? Frameworks like LangChain rely on LLMs responding with JSON  ](https://www.reddit.com/r/MachineLearning/comments/197f416/d_code_vs_json_output_for_llm_agents_frameworks/) , 2024-01-21-0911
```
[CaP](https://arxiv.org/pdf/2209.07753.pdf), [Voyager](https://arxiv.org/pdf/2305.16291.pdf), [Octopus](https://arxiv.or
g/abs/2310.08588)

I work primarily with JSON based agents but code-as-policy agents seem to be extremely powerful. Here
 are some of the benefits and weaknesses I've seen

Pros of code

1. Less tool creation needed - The prebuilt math/file/
string/list manipulation abilities that come with code are enormous. In a JSON based agent, you would have to formally d
eclare each of these as a tool which you expose to the LLM and explain in your prompting, which is a lot of work and eat
s up a ton of the context window. 
2. Reduced number of transactions - The LLM can write scripts that invoke multiple to
ols and manipulate their results in ways that are difficult to do in a single transaction via JSON. For example, in one 
script, the model could search a DB 3 times, perform regex on the query results, convert them to integers, and add them 
up. Doing this in one step via JSON tool invocations is basically impossible. 
3. Less syntax errors - this might be tot
ally just vibe-based reasoning, but it really seems like LLMs have an easier time writing valid python than valid JSON, 
especially when you have lots of nested arguments in your methods.

Cons

1. Crazy risky - This is the obvious one. You 
have a machine executing random code. There are ways to mitigate this but still. I mean seriously we all learned not to 
use eval, so it is crazy to basically see research tending towards just running eval on the outputs of these models. 
2.
 Scripts with errors - Sometimes the model tries to get too fancy and writes complex programs that have bugs, resulting 
in many needed retries. 

Do any of you have thoughts or experience with these approaches in the wild? 

Is anybody awar
e of any experiments that compare these two approaches against each other? 

&#x200B;
```
---

     
 
MachineLearning -  [ [D] Are Custom LLM RAG apps going to become redundant? ](https://www.reddit.com/r/MachineLearning/comments/1929n4f/d_are_custom_llm_rag_apps_going_to_become/) , 2024-01-21-0911
```
Loks like Copilot Studio is being rolled out (https://www.microsoft.com/en-us/microsoft-copilot/microsoft-copilot-studio
) with an impressive looking no code/out of the box RAG solution.

There is a phenomenal amount of development and activ
ity in the Open Source RAG world (e.g Langchain, Llamaindex, etc), which I am a great supporter of FYI.

However, what s
eems strange is that this no code out of the box solution (Copilot Studio - just as an example of one) seems overwhelmin
gly to be the better option if you wanted to build a RAG app i.e If you compare the cost to build and productionise a cu
stom RAG app vs the cost of using Copilot Studio, it's almost an order of magnitude lower (no matter how you cut it with
 the developer time and duration). 

My question is, it seems to me we are moving towards a situation where enterprise s
olutions will make custom RAG apps redundant (not in all cases of course, but most cases), however there seems to be ver
y little discussion of this relative to the activity in the open source community. Do people agree this is a likely scen
ario? 

Obviously there will be exceptions…but on most use cases I don’t see how you can compete with an instant/minimal
 setup, low cost, highly scalable RAG solution.
```
---

     
 
MachineLearning -  [ [P] An open-source project for deploying local models ](https://www.reddit.com/r/MachineLearning/comments/18zkm5m/p_an_opensource_project_for_deploying_local_models/) , 2024-01-21-0911
```
 Introducing a new LLM WebUI project that supports various local model loading and provides streaming output for cutting
-edge online multimodal models GPT-4-Vision and Gemini-Pro-Vision. Completely free and open source, it serves as a valua
ble research tool for exploring diverse models. The project is actively under development with continuous updates:  
[ht
tps://github.com/smalltong02/keras-llm-robot](https://github.com/smalltong02/keras-llm-robot)

&#x200B;

[WebUI](https:/
/preview.redd.it/f95jievpepac1.png?width=2560&format=png&auto=webp&s=1f2908b484ededc78591719ef87efdac2f9497ba)

&#x200B;


[Configuration](https://preview.redd.it/owaj5s1repac1.png?width=2560&format=png&auto=webp&s=f837b1ef67cb8e4ccaee4ec602
a61859f53db100)

&#x200B;

[Tools & Agent](https://preview.redd.it/jrot8w9sepac1.png?width=2560&format=png&auto=webp&s=7
1e224f08620941146cd437a99bcb55d02930a9e)
```
---

     
 
MachineLearning -  [ [Project] Temporal Augmented Retrieval (TAR) - Dynamic RAG ](https://www.reddit.com/r/MachineLearning/comments/18uddmj/project_temporal_augmented_retrieval_tar_dynamic/) , 2024-01-21-0911
```
From a corpus of text, how can you detect emerging topics and their evolution through time?

Introducing Temporal Augmen
ted Retrieval (TAR). (built in the context of buildspace n&w s4)

TAR is an open-source advanced RAG approach that aims 
to factor in the dynamic and temporal aspects of textual data when performing retrieval.

It allows us to understand the
 evolution of discussed topics over time.

The idea behind this project is to open the debate regarding the current limi
tations of RAG methods

This first approach has been built without using RAG frameworks (like Jerry Liu’s langchain) and
 focuses on financial tweets 

Relevant links:

Medium: [https://medium.com/@adam-rida/temporal-augmented-retrieval-tar-
dynamic-rag-ad737506dfcc](https://medium.com/@adam-rida/temporal-augmented-retrieval-tar-dynamic-rag-ad737506dfcc)

Gith
ub:[https://github.com/adrida/Temporal\_RAG](https://github.com/adrida/Temporal_RAG)

Hugging Face Benchmark: [https://h
uggingface.co/spaces/Adr740/Temporal-RAG-Benchmark](https://huggingface.co/spaces/Adr740/Temporal-RAG-Benchmark)

My web
site: [adrida.github.io](https://adrida.github.io)

&#x200B;

https://preview.redd.it/lj7wkhk70f9c1.png?width=960&format
=png&auto=webp&s=fc79c5034351a1711e1ec051919a5c4d2edbc333
```
---

     
 
MachineLearning -  [ [R][P] Autogen + Langchain Tools + Local LLM doesn't work. ](https://www.reddit.com/r/MachineLearning/comments/18tex1j/rp_autogen_langchain_tools_local_llm_doesnt_work/) , 2024-01-21-0911
```
Hey folks, 

So I'm playing around with the agent framework Autogen and I'm trying to create agents by providing it cust
om tools to use. These custom tools are defined in the langchain framework. Furthermore, I am using open source LLM mode
ls like Mistral, LLAMA, Mixtral etc.

In my experience, I have been unable to get the Autogen+LocalLLM framework to iden
tify the right tools to use given the prompt. However it does a fantastic job with the GPT model. 

Please note that my 
goal is for the agent to mandatorily use the tools provided and not come up with its own code. And the agent should figu
re out the right tool to use. 

I have been very explicit with my prompting, despite which I am unable to get this to wo
rk.

Any thoughts and suggestions? Please let me know ! Please share your experiences as well. Cheers !
```
---

     
 
MachineLearning -  [ [P] Seeking Advice for Building a School Handbook Chatbot Using OpenAI and Vector Databases ](https://www.reddit.com/r/MachineLearning/comments/18rndcp/p_seeking_advice_for_building_a_school_handbook/) , 2024-01-21-0911
```
Hello everyone,

I'm embarking on a project to create a chatbot for my school's handbook, aiming to make it a resource f
or students to easily access information. As someone relatively new to AI, I'm seeking guidance on implementing this.

M
y current plan is to use OpenAI as the primary language learning model, focusing on affordability. I am considering inte
grating RAG (Retrieval-Augmented Generation) and LangChain for enhanced functionality. However, I'm quite perplexed abou
t choosing an appropriate vector database, as many options appear costly. The goal is to keep this system live and acces
sible for student usage without breaking the bank.

I'm also looking into open-source embedding models to pair with the 
vector database. Pinecone has caught my attention, but its pricing seems steep for our budget.

Does anyone have recomme
ndations or tips on affordable yet effective tools and strategies for this project? Any insights on vector databases sui
table for educational use, or ways to optimize cost without compromising quality, would be greatly appreciated.

Thank y
ou in advance for your help!

(I typed out my problem and had gpt4 fix up the format and wording dont bash me)
```
---

     
 
deeplearning -  [ [D] Unleashing the Power of Langchain with Wandb: Revolutionizing Topic Modeling and Evaluation ](https://www.reddit.com/r/deeplearning/comments/191mm83/d_unleashing_the_power_of_langchain_with_wandb/) , 2024-01-21-0911
```
Complementing Langchain’s prowess, Wandb emerges as a powerhouse meticulously designed for developers leveraging LLM tec
hnology. As an evaluation framework and production monitoring platform, Wandb stands out for its tailored approach. Its 
arsenal comprises real-time monitoring, granular analytics, and streamlined evaluation processes, laying the groundwork 
for elevated performance and reliability in AI applications.

&#x200B;

Link: [https://medium.com/ai-advances/unleashing
-the-power-of-langchain-with-wandb-revolutionizing-topic-modeling-and-evaluation-75af5cf51b15](https://medium.com/ai-adv
ances/unleashing-the-power-of-langchain-with-wandb-revolutionizing-topic-modeling-and-evaluation-75af5cf51b15) 
```
---

     
