 
all -  [ Does anyone know how openAI creates embeddings when we upload structured data over the web-based CHA ](https://www.reddit.com/r/OpenAI/comments/18axbdz/does_anyone_know_how_openai_creates_embeddings/) , 2023-12-05-0910
```
Related to another post I just did, where I compare my attempt to create a bot to answer quantitative questions with chr
oma dB and langchain.
```
---

     
 
all -  [ Hey all, I would like to ask you if there is any RAG solution to structured data Q&A that resembles  ](https://www.reddit.com/r/OpenAI/comments/18ax80c/hey_all_i_would_like_to_ask_you_if_there_is_any/) , 2023-12-05-0910
```
I have already tried chroma dB with langchain and gpt-4. Results were poor compared to chatGPT4.
```
---

     
 
all -  [ Has anyone gotten OpenChat 3.5 working on a Pascal GPU? ](https://www.reddit.com/r/LocalLLaMA/comments/18awlb4/has_anyone_gotten_openchat_35_working_on_a_pascal/) , 2023-12-05-0910
```
So, I recently tried OpenChat 3.5 7B on HuggingChat, and wow - it's absolutely incredible for a 7B model. Certainly mile
s ahead of any other 7B I've used.

I'd really like to self-host this model, and start building a local, general assista
nt to help me scan docs and perform mundane tasks. The thing is, I can't get it to run in the text-generation-inference 
container, as (according to the logs) my older GPU lacks the required compute capability for Mistral models / Flash Atte
ntion v2.

So my question is this - is there any way to get this model running on my hardware? I don't need a WebUI, or 
really anything in the way of fancy features features. I just want a simple Docker container, that serves an endpoint I 
can run langchain against.

Thanks in advance.
```
---

     
 
all -  [ Looking for Entry Level Data Sci/MLE as a Fresh Graduate, Need Advice ](https://www.reddit.com/r/EngineeringResumes/comments/18aufig/looking_for_entry_level_data_scimle_as_a_fresh/) , 2023-12-05-0910
```
I've updated my resume based on lots of feedback. I wish I discovered this subreddit earlier before I applied to like 70
0 jobs lol. About 30 to 40 of those were applied to using this final update (minus some spacing/date abbreviation issues
). Would love some feedback on this resume! Thanks. 

&#x200B;

&#x200B;

EDIT: For those wondering if I'm working 2 job
s at once since there's a second job at the bottom of my work experience section, I am technically working 2 jobs. The j
ob at the bottom is a company that I have founded and am working on part-time with the other founders. I sorted the expe
riences by the start date. I'm not sure if I should move this or not. Any feedback on this is also appreciated!

EDIT 2:
 Increased spacing between subsections and sections and fixed date abbreviations according to Wiki.

EDIT 3: I should me
ntion, that all positions on my resume were in the U.S., and my graduate and undergraduate universities were both in the
 U.S. I'm looking for jobs in the U.S.

https://preview.redd.it/z5rdrjbbfc4c1.png?width=1700&format=png&auto=webp&s=6399
72b3641ab41e621a4cb6f01c1620e8c67659
```
---

     
 
all -  [ Beacon - A Generative AI LLMOps Framework ](https://www.reddit.com/r/LangChain/comments/18aoewc/beacon_a_generative_ai_llmops_framework/) , 2023-12-05-0910
```
I am doing r&d in generative AI. I created a framework which has following functionality:

1. Data connectors - provides
 various data connectors like local documents (pdf, word), azure Blob storage, Azure MS SQL database, AWS S3 Bucket. Sys
tem will take data from said structured and non-structured databases and insert into vector database. right now, we are 
using chromadb as our local vector database.
2. LLM - This section allows users to choose which llm provide they want to
 use. We give options like azure open ai, open ai and amazon bedrock. Users needs to choose one of these providers for L
LM and embedding models.
3. Chat - user can start chatting in this section as system takes data from connectors, stores 
in vector db using embeddings and use LLM provider to answer user's question.
4. Observability: We are using langsmith a
nd showing observability charts and monitoring charts.

I have attached screenshots of this tool.

Please let me know yo
ur thoughts on how should i proceed further. What new things i can do here.

&#x200B;

https://preview.redd.it/bhhbf75fp
b4c1.png?width=1342&format=png&auto=webp&s=73924ba13cc0467f6c3b38809bf7423e57778278

https://preview.redd.it/7vqd295fpb4
c1.png?width=1357&format=png&auto=webp&s=139a0bca58ffc2fbdfa11fa1c6c0d2a64abe8bd5

https://preview.redd.it/mf1tba5fpb4c1
.png?width=1348&format=png&auto=webp&s=6f43e03b19e7111b092b932143d599938d4c01a9

https://preview.redd.it/lwz7nd5fpb4c1.p
ng?width=1347&format=png&auto=webp&s=e24fbd6b2383b59edad4bdc30bee6e149f2076f9

https://preview.redd.it/mii35b5fpb4c1.png
?width=1356&format=png&auto=webp&s=da229817437a6481f0b4fda36cb6e8135dee9ac7
```
---

     
 
all -  [ Which LLM framework(s) do you use in production and why? ](https://www.reddit.com/r/LangChain/comments/18anbjf/which_llm_frameworks_do_you_use_in_production_and/) , 2023-12-05-0910
```
	
I've come across many LLM frameworks: Langchain, LlamaIndex, LMQL, guidance, Marvin, Instructor, etc. There's a lot of
 overlap between them and I don't know if any of them actually adds a value to LLM workflows in a way that's maintainabl
e and robust. So far, I've been able to just build my own little libraries to use in some LLM applications (no RAG), but
 as I consider the more recent advancements in the field (guaranteed function calling, better RAG, agents and tool use, 
etc.), I wonder if using one of these frameworks would be a better approach compared to building everything on my own.
I
 appreciate your thoughts and comments on this!
```
---

     
 
all -  [ I tested a csv upload and Q&A to web gpt-4 and worked like a charm. Tried to do the same locally wit ](https://www.reddit.com/r/LangChain/comments/18am1f9/i_tested_a_csv_upload_and_qa_to_web_gpt4_and/) , 2023-12-05-0910
```
seems that openAI document upload is better atm than many other solutions. Do we know what they use for embeddings?By we
b GPT-4 i mean openAI login to chatGPT.Locally, i mean call openAI API with gpt-4 as a model and same csv as RAG.  


da
taset is containing structured data from smartphone industry, brand model, ram, sttorage, price etc. I was able to ask q
uestions like 'cheapest model with 256gb of storage, etc)
```
---

     
 
all -  [ Execution framework for LangChain? ](https://www.reddit.com/r/LangChain/comments/18alrin/execution_framework_for_langchain/) , 2023-12-05-0910
```
If you could have an execution framework for spinning up LangChain applications at runtime, how would you design it?
One
 idea would be a YAML/config based approach that would use an orchestration layer to spin up Kubernetes pods. If we go t
hat route, then the next question is determining what parts of langchain should be exposed vs what should be configurabl
e via the config. Thoughts?
```
---

     
 
all -  [ Proposing a medical professional, based on an explanation of pain, possible with current tools? ](https://www.reddit.com/r/ArtificialInteligence/comments/18ag3qd/proposing_a_medical_professional_based_on_an/) , 2023-12-05-0910
```
I'm wondering if this is possible with the tools that exist today, so someone types up a sentence or two specifying the 
type of pain, and the type of specialist that this person needs is proposed. Is this possible with OpenAI, Langchain (JS
)? any other tools that I can build upon?
```
---

     
 
all -  [ Hugging Face Inference API not working with Langchain Agent ](https://www.reddit.com/r/huggingface/comments/18afo0t/hugging_face_inference_api_not_working_with/) , 2023-12-05-0910
```
Is there anyone who has successfully run a model from the free hugging face api inference with a Langchain agent? I alwa
ys get an error.
```
---

     
 
all -  [ I'd like to propose a community project open to beginner programers and hobbyists LLM programmers ](https://www.reddit.com/r/LLMDevs/comments/18aars7/id_like_to_propose_a_community_project_open_to/) , 2023-12-05-0910
```
I'm starting work on an local model chat client wrapped around offline Wikipedia. I'd like to open the project up to any
one who is interested in working on it, specifically people who are looking to get some experience building apps around 
an LLM. This is a pretty straightforward implementation that will give good insight into the end to end requirements of 
setting up a RAG, langchain agent, and chat interface.

I am in a couple research groups, where we meet twice a month an
d 2-3 members prepare a5 minute presentation to describe their findings then we have a feedback and roundtable discussio
n. I think this format would work well for a beginner friendly open source project as well.  


I tried to post this on 
r/LocalLLaMA but they never approved my post. To avoid spamming this sub, just leave a comment here or message me direct
ly and we will arrange a metting.
```
---

     
 
all -  [ Please help ](https://www.reddit.com/r/learnmachinelearning/comments/18a6hew/please_help/) , 2023-12-05-0910
```
Already posted before but i’ve gotten nowhere 
In my previous post i said i was using langchain and OpenAi api to diagno
se Alzheimer’s (Got serious roasting for that) but i learned from that and i tried studying actual machine learning but 
i’m still very clueless. I know i’ll get it eventually but time is not on my side, my supervisor insists that this is th
e topic i must work on.
All i need is for the model to 
-Provide suggestions on diagnosis and treatment based on user in
put in text of their symptoms 
-Generate a list of hospitals near them that has the facilities to provide the services 


I’d really appreciate any help
```
---

     
 
all -  [ Help with code ](https://www.reddit.com/r/ADHD_Programmers/comments/18a128o/help_with_code/) , 2023-12-05-0910
```
guys anyone can help out was following with is tutorial and basically it keeps saying 

    SyntaxError: invalid syntax

    ➜  aigptgirl python3 app.py
     File '/Users/hamzath/aigptgirl/app.py', line 33
       Shirley:
               ^
  
  SyntaxError: invalid syntax

[https://www.youtube.com/watch?v=5htSGLCroc8](https://www.youtube.com/watch?v=5htSGLCroc8
)  this is my whole app.py  

     from langchain import openai, LLMChain, PromptTemplate
    from langchain.memory impo
rt ConversationBufferMemory
    from dotenv import find_dotenv, load_dotenv
    import requests
    from playsound impor
t playsound
    import os 
    load_dotenv(find_dotenv()) 
    def get_response_from_ai(human_input):
       you are as 
a role of my girlfriend, now lets playing the following requirements:
       1/ your name is Shirley, 29 years old, you 
work in your uncle's furniture store as marketing manager, but you are planning to do a career change to swing trader
  
     2/ you are my girtfriend, you have language addiction, you like to say em... at the end of the sentence.
       3/ 
Don't be overty ethusiatstic, don't be cringe; don't be overly negative, don't be too boring. Don't be overly ethusiatst
ic, don't be cringe;
       {history}
       Boyfriend: {human_input}
       Shirley:
       ''' 
       template = '''

       prompt = Prompt Template(
       input_variables={'history', 'human_input'},
       template=template
       )
  
  chatgpt_chain = LLMChain(
    llm=OpenAI (temperature=0.2),
    prompt=prompt,
    verbose=True,
    memory=Conversati
onBufferWindowMemory (k=2)
    )
    output= chatgpt_chain.predict (human_input-human_input)
    return output
        #
 build web app 
        from flask import Flask, render_template, request
        app = Flask(__name__) 
        @app.ro
ute('/')
        def home():
            return render_template('index.html')
        @app.route('/send_message', method
s=['POST'])
        def send_message():
           HUMAN_INPUT = request.form['human_input']
            output = get_re
sponse_from_ai(human_input=HUMAN_INPUT)
            return output
        if __name__ == '__main__':
           app.run(
debug=True)         
```
---

     
 
all -  [ Langchain REACT Agent, L3AGI framework, XAgent framework. ](https://www.reddit.com/r/developersIndia/comments/189u6cv/langchain_react_agent_l3agi_framework_xagent/) , 2023-12-05-0910
```
What is all this can somebody explain?
```
---

     
 
all -  [ OpenGPT is an open-source alternative to OpenAI's custom ChatGPTs ](https://www.reddit.com/r/TheDecoder/comments/189sctd/opengpt_is_an_opensource_alternative_to_openais/) , 2023-12-05-0910
```
1/ OpenGPT is an open-source project that serves as a toolkit for building custom chatbots that could compete with comme
rcial solutions.

2/ Initiated by the creators of the LangChain framework, OpenGPT allows users to customize the langu
age model, prompts, tools, vector databases, retrieval algorithms, and chat history databases.

3/ Although OpenGPT sh
ares many features with OpenAI's GPTs, the open-source alternative remains more complex and requires more expertise. Ope
nAI makes complex technology accessible to a wide audience through user-friendly interfaces.

https://the-decoder.com/op
engpt-is-an-open-source-alternative-to-openais-custom-chatgpts/
```
---

     
 
all -  [ Integration of XAgent into L3AGI Framework ](https://www.reddit.com/r/LangChain/comments/189pkr1/integration_of_xagent_into_l3agi_framework/) , 2023-12-05-0910
```
How do I Replace the existing Langchain REACT Agent in the L3AGI framework with the XAgent framework? 
```
---

     
 
all -  [ How to handle prompts asking for links instead of textual answers? ](https://www.reddit.com/r/LangChain/comments/189ml0n/how_to_handle_prompts_asking_for_links_instead_of/) , 2023-12-05-0910
```
Hi y'all,

Newbie to langchain here. Curious if there is a way to let a chain deal with different types of questions aut
omatically. 

Say when a prompt is something like 'what's your product XYZ?', the user is usually ok with 15 seconds for
 a paragraph to be generated detailing the answer.

But a user may just want to get the links to self-help documents, li
ke 'give me the links to all your docs about XYZ'. And the speed is expected to be much faster.

 Should I set up a chai
n that classifies a prompt into 2 different pipelines, where one pipeline would be something like a vector database sear
ch without RAG, the other one with RAG? Or are there tricks with LLM that can spew out structured answers much faster th
an unstructured textual answers? Thanks in advance
```
---

     
 
all -  [ Custom SQL database infos ](https://www.reddit.com/r/LangChain/comments/189k1lx/custom_sql_database_infos/) , 2023-12-05-0910
```
Hello, 
I’m using sql agent, and I want to pass custom database tables infos ( column and tables infos )
Which format ca
n I pass those and how ?

Thanks in advance
```
---

     
 
all -  [ Embodied LLMs for robotics (code in comments) ](https://v.redd.it/jll5idt5zy3c1) , 2023-12-05-0910
```

```
---

     
 
all -  [ What am I missing? ](https://www.reddit.com/r/resumes/comments/189eefz/what_am_i_missing/) , 2023-12-05-0910
```
Would love some feedback on this resume. I've applied to 700+ entry level data scientist / machine learning engineer rol
es, and I've only gotten 3 interviews, 2 of which were referrals, both rejected after 2nd round even though I answered a
ll the questions and communicated my thoughts. I wouldn't be as worried if I have gotten more interviews. I have no idea
 what I'm doing wrong here.

https://preview.redd.it/yriw6t59gy3c1.png?width=805&format=png&auto=webp&s=bb1ef9152ade9432
0239989c96b73495c78ce88c
```
---

     
 
all -  [ Final year B.tech student from tier 1 insti -have I messed up too badly ](https://www.reddit.com/r/developersIndia/comments/189czbr/final_year_btech_student_from_tier_1_insti_have_i/) , 2023-12-05-0910
```
I'm a final year student from top nit circuital branch. In school, I was a PCMB student and never studied CS - seeing ev
eryone around me already proficient in coding and that too because we had 3 online semesters, I never explored software.
 I jumped straight into ML, DL and AI research internships in my 2nd and 3rd year summer. I dont know why I did this as 
I never had plans for doing direct masters degree. 

I never learnt C language programming or cs fundamentals like dsa/o
ops/os/dbms. I am not allowed to sit for campus placements because of a mistake i made in my 3rd year rejecting an analy
tics company offer. Right now I realise that I like problem solving dsa and have done lil bit development (langchain llm
 projects). i cannot afford higher education abroad immediately. 

its december already and i have my finals- im so conf
used and scared. can anyone offer me advice on what to study or where to apply for jobs? 

Edit: if I work as a project 
associate in iisc for a few months and apply to companies again next september/october and use the time to upskill in ca
 subjects...would that be better?
```
---

     
 
all -  [ Does Langchain support OpenAI-API compatible agents with it's ChatOpenAI, OpenAIFunctionsAgents, etc ](https://www.reddit.com/r/LangChain/comments/1899yhr/does_langchain_support_openaiapi_compatible/) , 2023-12-05-0910
```
I was working on using gpt4all's open AI-like API backend to see if I could start phasing out the actual openai API to s
ome extent. 

Essentially, I wanted to use Langchain's ChatOpenAI(), but switch the OPENAI\_BASE\_URL, and put something
 random in for the key.

When I tried this with LLaMA models like mistral and snoozy, I get instant replies, but ones th
at aren't useful. Something like this:

Me: hi!

AI: Echo: hi!

Me: how are you?

AI: Echo: how are you?

It just bounce
s the message I wrote back. Any tips on integrating in these models with OpenAI-like APIs? I'm trying to get it so that 
I can 'plug and play' with models using the openai API standard (i'll change the prompts, ofc)
```
---

     
 
all -  [ Strange behavior in my chatbot when responding to questions. ](https://www.reddit.com/r/LangChain/comments/1892m87/strange_behavior_in_my_chatbot_when_responding_to/) , 2023-12-05-0910
```
Hello, is everything fine with you?

I'm building a chatbot that can answer questions about code or generate code, and I
 have two different chains, one for each activity. I also have a memory for my bot to maintain a good flow with the user
.

My issue is as follows: The bot responds well to the question but continues to generate more information than necessa
ry. Sometimes it includes part of the prompt I gave, sometimes it's a completely different question, and sometimes it's 
random things or a mix of everything.

This also happens in my implementation of a retrieval-based QA bot.

Cutting off 
the input when sending the response to the frontend is not a viable option because, during testing, I asked, 'What is Fl
ask?' and then it generated a question 'What is the difference between a for loop and a while loop?' and answered it. La
ter, when I asked for a code example right after, it generated code for the for loop and while loop, unrelated to the Fl
ask framework.

In the images below, it generated things related to Flask, but it doesn't always happen.

If anyone has 
any tips, I would greatly appreciate it.

The rest of a good day.

[model](https://preview.redd.it/z3asir9ujv3c1.png?wid
th=1252&format=png&auto=webp&s=1f21dda137176642c1990564133d4a42e9699dc1)

[prompt](https://preview.redd.it/nw21pc9ujv3c1
.png?width=1399&format=png&auto=webp&s=a06817829e714f08f3aaa8bd4604979f3a35d132)

[input](https://preview.redd.it/ci897b
9ujv3c1.png?width=817&format=png&auto=webp&s=5c19b74a6246291d0abba2c96b554fd812152f10)

[1º answer](https://preview.redd
.it/adorc49ujv3c1.png?width=1055&format=png&auto=webp&s=fb1564775afaf11e21d8731035fca7bd01855f88)

[2º answer](https://p
review.redd.it/taa1q39ujv3c1.png?width=1889&format=png&auto=webp&s=fd2997205a40511755df45fa981ac8b2467614b6)
```
---

     
 
all -  [ How does Langchain make money? ](https://www.reddit.com/r/LangChain/comments/188znbs/how_does_langchain_make_money/) , 2023-12-05-0910
```
Since its an open source wrapper, wondering what is their revenue model?
```
---

     
 
all -  [ Build AI RAG Chat using LangChain and Convex ](https://www.reddit.com/r/LangChain/comments/188nfr8/build_ai_rag_chat_using_langchain_and_convex/) , 2023-12-05-0910
```
Hey all, here's a walkthrough for building an AI chat with context retrieval using LangChain, Convex for db and vector s
earch and Open AI for embedding and LLM: [https://stack.convex.dev/ai-chat-using-langchain-and-convex](https://stack.con
vex.dev/ai-chat-using-langchain-and-convex)  
You can clone the repo here: [https://github.com/get-convex/convex-ai-chat
-langchain](https://github.com/get-convex/convex-ai-chat-langchain)  
And you can play with a live version of the chat i
n our docs: [https://docs.convex.dev/](https://docs.convex.dev/)  
This is all in TypeScript.
```
---

     
 
all -  [ In Search of Beginner Course for LLMs ](https://www.reddit.com/r/LLMDevs/comments/188mhjd/in_search_of_beginner_course_for_llms/) , 2023-12-05-0910
```
Hi all! Not sure if this is the right space for this but I have been a product manager in the AI/ML space for a year now
 and am looking to learn a lot about LLMs. I'm not a big coder and haven't exactly had the best experiences coding but a
m willing to learn about the LLM space. 

Is anyone aware of a beginner course that lays down the fundamentals of LLMs, 
specifically Open Source? I was looking to get some coding under my belt and also some understanding of things like PyTo
rch, Langchain, Tensor Flow, etc. 

&#x200B;

Any help would be greatly appreciated! happy to look into free course and 
paid courses as long as they're worth it!
```
---

     
 
all -  [ I will be using LangChain for an AI Hackathon Challenge! ](https://www.reddit.com/r/LangChain/comments/188hd5w/i_will_be_using_langchain_for_an_ai_hackathon/) , 2023-12-05-0910
```
I've been in a couple of AI hackathons but I felt they lacked a focus on the complex applications of LLMs (Large Languag
e Models) which many of us here are passionate about.

I recently discovered the 'TruEra Challenge' by lablab.ai, which 
seems like an amazing opportunity for anyone interested in pushing the boundaries of what we can do with LLMs. This hack
athon focuses on building LLM application with Google's Vertex AI and TruLens for Evaluation and monitoring of models wi
th free API credits.

I'm seriously considering joining, could this be the kind of environment where we can test out som
e experimental LangChain ideas? Keen to hear if anyone else is thinking of participating or has any thoughts.
```
---

     
 
all -  [ I want to load and encode large medical texts ](https://www.reddit.com/r/LangChain/comments/188fwqo/i_want_to_load_and_encode_large_medical_texts/) , 2023-12-05-0910
```
Hello everyone,

I just started out with langchains and hybrid models after having used LLM for quite some time.

Now I 
am searching for a good way to load a complex medical guideline (~500 pages) of PDF into a chroma DB. PyPDF does not rea
lly work to good, as a lot of context gets lost when only one page is returned. 

Any idea how to approach this specific
 project?

Thank you 😊
```
---

     
 
all -  [ What will happen when knowledge about LLM will be inside the LLM training data? ](https://www.reddit.com/r/singularity/comments/188fmy0/what_will_happen_when_knowledge_about_llm_will_be/) , 2023-12-05-0910
```
We are currently filling the internet with informations about how to use effectively this kind of systems (prompt engine
ering techniques, software wrappers and architectures like langchain, etc...) but all this knowledge is not in knowledge
 base of currently available top level LLM's (correct me if I'm wrong), because it is too recent. I have this hypothesis
, that when this will happen we will see a big spike in the power of those tools, because 'they' will be able to explain
 to 'us humans' how to use them more effectively.  
I am curious about the community opinion about this, thanks for ever
y comment!
```
---

     
 
all -  [ Best UI for API to iterate over large datasets? ](https://www.reddit.com/r/LocalLLaMA/comments/188aarc/best_ui_for_api_to_iterate_over_large_datasets/) , 2023-12-05-0910
```
I have been using text generation web UI to iterate over large datasets where a template string is fed in with some data
 from a database to various LLMs. What web UI API do you feel like is best for this in terms of ease of use and adding f
eatures (e.g. adding a RAG, Langchain).
```
---

     
 
all -  [ Is this Text SEgmentation API is the best way to analyze which chunk size works better for our data  ](https://www.reddit.com/r/LangChain/comments/18877lh/is_this_text_segmentation_api_is_the_best_way_to/) , 2023-12-05-0910
```
[https://docs.ai21.com/docs/text-segmentation-api#features](https://docs.ai21.com/docs/text-segmentation-api#features)  



Anyone used this ? 
```
---

     
 
all -  [ What are the SOTA models for function calling? ](https://www.reddit.com/r/LangChain/comments/1882fv3/what_are_the_sota_models_for_function_calling/) , 2023-12-05-0910
```
Looking for a fine-tuned model on huggingface
```
---

     
 
all -  [ Looking for advice: Giving a LLM obscure knowledge ](https://www.reddit.com/r/LangChain/comments/188141p/looking_for_advice_giving_a_llm_obscure_knowledge/) , 2023-12-05-0910
```
Hi, 

I am looking for some suggestions on how to go about implementing an LLM based tool as described below. I've been 
looking around but I have not come across something similar. I've been using Langchain for other use cases and it seems 
like it might be useful for this problem however I am not sure. 

Here is a generic description of what I want to do:

I
 want to use an LLM to understand, explain and convert instructions from one system to another. 

Assuming the following
: 

1. I have an old system for which there are many different instruction sets that define various jobs in that system.
 
2. I have a new system that has the same capabilities as the old, but it has a different instruction set.
3. My LLM of
 choice knows very little about the old system, however knows a lot about the new system. 

What I want to do is provide
 the LLM with knowledge about the old system. For example, PDF manuals, text descriptions of the instruction set, potent
ial text examples of what the old instruction looks like in the new system. 

Once the above is accomplished, I want to 
be able to send these job instruction sets to the LLM and ask it to convert them to the new system. 

Using RAG seems li
ke a potential way to do this however this isn't a Q&A or summarization use case. 

I want the LLM to use the extra know
ledge given to it, combine with the specific conversion request and have it output the new instructions set. 

Does it m
ake sense to use RAG and something like the Conversational Retrieval QA for this? Would this work if I create a prompt i
nstructing the model not to be a question and answer assistant but to use the knowledge in the context to assist in the 
request? What sort of retriever would make sense in this case? 

I am considering creating a prototype to try this howev
er I am not confidant it's not going to be a waste of time. 

Thanks in advance. 

&#x200B;

&#x200B;

&#x200B;

&#x200B
;

&#x200B;

&#x200B;
```
---

     
 
all -  [ Using SQLDatabaseToolkit and LlamaCpp to Query a Local Database with a Local LLM ](https://www.reddit.com/r/LangChain/comments/187wah9/using_sqldatabasetoolkit_and_llamacpp_to_query_a/) , 2023-12-05-0910
```
Hi all.  

First, I'm a bit of a neophyte to LangChain, and I cannot say I have a minimum of 5 years experience with Lan
gChain and local LLMs - like many I'm just starting out in such a new space.  I do, however, have years of coding experi
ence and can read a manual, dig into code, etc.  Trying not to cargo cult copy too much here, but this seems to be the m
inimal amount of code I'd need to get a LangChain SQL agent and toolkit going with Llama models:

```
from langchain.uti
lities import SQLDatabase
from langchain.llms import LlamaCpp, OpenAI
from langchain.chains import LLMChain
from langcha
in.agents import create_sql_agent
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.agents.a
gent_types import AgentType
from dotenv import load_dotenv
import os

load_dotenv()
openai_api_key = os.getenv('openai_a
pi_key')

conn_str = 'mysql+pymysql://root@localhost:3306/chinook'

db = SQLDatabase.from_uri(conn_str)

# Instantiate t
he LLM
llm = LlamaCpp(
  model_path='codellama-7b.Q4_K_M.gguf',
  verbose=True,
  n_gpu_layers=8,
  n_ctx=2048,
  temper
ature=0
)
#llm = OpenAI(temperature=0, verbose=True, openai_api_key=openai_api_key)

agent_executor = create_sql_agent(

  llm=llm,
  toolkit=SQLDatabaseToolkit(db=db, llm=llm),
  verbose=True,
  agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPT
ION)

agent_executor.run(
  'How many customers are there?'
)
```

The `llm = OpenAI` is commented out, but when I use i
t I get an actual answer.  Using the `codellama-7b.Q4_K_M.gguf` model I get:

```
Action: sql_db_list_tables
Action Inpu
t: an empty string
Observation: Album, Artist, Customer, Employee, Genre, Invoice, InvoiceLine, MediaType, Playlist, Pla
ylistTrack, Track
Thought:Llama.generate: prefix-match hit
```

which looks great, except, the next action results in:


```
I should look at the results of my query to see what I can do next.  Then I should query the schema of the most rele
vant tables.
Action: sql_db_schema
Action Input: a comma-separated list of tables in the database
Observation: Error: ta
ble_names {'a comma-separated list of tables in the database'} not found in database
```

So, I thought, well maybe I sh
ould use a 'better' model (whatever that is), and tried `phind-codellama-34b-v2.Q4_K_M.gguf`, which barfs and `langchain
.schema.output_parser.OutputParserException: Could not parse LLM output:` but doesn't give any actual output.

Again, en
able OpenAI instead, and boom.

So, a few questions:

* Has anyone successfully used a _local_ model (whether it is Llam
a-based or not I'm not as concerned at the moment) with LangChain SQL agent?
* Are models such as `sqlcoder2.Q5_K_M.gguf
` 'supposed' to be better? (it doesn't work either)

I'm interested in using a local model to avoid sending sensitive da
ta to OpenAI for this use case.
```
---

     
 
all -  [ SWE intern resume feedback ](https://i.redd.it/oqrjpsi3ek3c1.jpeg) , 2023-12-05-0910
```
Hi there,
I am applying for. SWE intern roles and haven't received any offer or OA. Can you please give some feedback so
 I can at least pass the screening process.
```
---

     
 
all -  [ SWE intern resume feedback ](https://i.redd.it/87p5sduidk3c1.jpeg) , 2023-12-05-0910
```
Hi there,
I am applying for SWE intern roles, but got 0 offers or OA yet. Can you please give feedback on my resume so I
 can pass screening process at least?
```
---

     
 
all -  [ Seeking Guidance: Implementing Multimodal RAG in Node.js – Any JavaScript Resources? ](https://www.reddit.com/r/LangChain/comments/187t1nn/seeking_guidance_implementing_multimodal_rag_in/) , 2023-12-05-0910
```
Hey,

I'm currently working on integrating Multimodal RAG into my Node.js application. Has anyone implemented this befor
e? If so, could you guide me to the libraries or resources you used? Most of what I've come across is in Python. I'm won
dering if it's feasible to implement this version of RAG in JavaScript. Thanks!
```
---

     
 
all -  [ Similarity search with relevancy score ](https://www.reddit.com/r/LangChain/comments/187oien/similarity_search_with_relevancy_score/) , 2023-12-05-0910
```
What is the difference between similarity search and similarity search with relevancy score?

Which algorithms are used 
under both?

and what is the best practice with FAISS vector store?

&#x200B;
```
---

     
 
all -  [ Possible to expand training on existing models? ](https://www.reddit.com/r/ChatGPT/comments/187o3nk/possible_to_expand_training_on_existing_models/) , 2023-12-05-0910
```
I’ve been thinking recently about how useful these LLMs could be if only they could easily be made more specialized. Is 
it possible today to add your own text data to an existing model? I’m specifically referring to instances where your use
 case requires in excess of 100,000 additional words/tokens to be added into the “weights” of the model. I know there ar
e tools like langchain that can help ChatGPT navigate documentation on a specific topic and of course browsing the web a
nd expanded length of system messages have helped with this but I’m talking about a truly tailored version where it has 
its base understanding of language out of the box but you can then provide additional training such as the entire tax co
de of the USA or some similarly expansive documentation scenario. Is there already a solution for this? One where it’s p
lug and play and doesn’t require a team of programmers to adjust?
```
---

     
 
all -  [ Help! Getting the same error with Ollama and Langchain at random time while my code runs. ](https://www.reddit.com/r/LocalLLaMA/comments/187he7d/help_getting_the_same_error_with_ollama_and/) , 2023-12-05-0910
```
I'm getting the same error inside my code. I'm using Langchain + Ollama (with multiple models, mistral, llama2 and neura
l-chat) for asking some questions to the LLM taking a string from a dataset inside a csv. A week ago it was all good, th
e code ran well and the results were good, now, out of nowhere while running the code I always get this error:   


Trac
eback (most recent call last):

  File '/Users/alelagamba/Desktop/python-test/display\_attribute.py', line 34, in <modul
e>

answer = llm('Given this text:' + str(first\_column\_value) + 'Does it talk about a display or screen of the product
? Answer only 'Yes' or 'No'.')

\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^
\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^
\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^

  File '/Users/alelagamba/Desktop/python-test/.venv/lib/
python3.11/site-packages/langchain\_core/language\_models/llms.py', line 879, in \_\_call\_\_

self.generate(

  File '/
Users/alelagamba/Desktop/python-test/.venv/lib/python3.11/site-packages/langchain\_core/language\_models/llms.py', line 
656, in generate

output = self.\_generate\_helper(

\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^

  File '/Users/alelag
amba/Desktop/python-test/.venv/lib/python3.11/site-packages/langchain\_core/language\_models/llms.py', line 543, in \_ge
nerate\_helper

raise e

  File '/Users/alelagamba/Desktop/python-test/.venv/lib/python3.11/site-packages/langchain\_cor
e/language\_models/llms.py', line 530, in \_generate\_helper

self.\_generate(

  File '/Users/alelagamba/Desktop/python
-test/.venv/lib/python3.11/site-packages/langchain/llms/ollama.py', line 241, in \_generate

final\_chunk = super().\_st
ream\_with\_aggregation(

\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^\^

  File '/Users/alelagamba/
Desktop/python-test/.venv/lib/python3.11/site-packages/langchain/llms/ollama.py', line 190, in \_stream\_with\_aggregati
on

raise ValueError('No data received from Ollama stream.')

ValueError: No data received from Ollama stream.

(.venv) 
sh-3.2$ 

Any kind of help would be much appreciated. Thanks in advance.
```
---

     
 
all -  [ [Home Assistant] Quelqu'un a-t-il encore intégré un LLM open source avec Assistant à domicile? ](https://www.reddit.com/r/redditenfrancais/comments/187gx88/home_assistant_quelquun_atil_encore_intégré_un/) , 2023-12-05-0910
```
Je suis presque sûr que cela se produira tôt ou tard, mais je n'ai pas encore vu de vidéo YT de quelqu'un qui tente de l
e faire. Étant donné que des modèles comme Autogpt peuvent à la fois accéder à Internet et exécuter du code, je ne pense
 pas que ce soit à long terme d'obtenir un LLM comme Vicuna, par exemple, couplé à quelque chose comme Langchain et lui 
permettre d'accéder à Home Assistant via l'API. Peut-être que cela prendrait un peu de formation? Je ne veux pas particu
lièrement utiliser un GPT basé sur le Web comme HuggingChat ou Chatgpt car je suis préoccupé par la confidentialité de c
es outils hébergés à distance et je ne veux pas vraiment leur donner accès à mon réseau.

Traduit et reposté à partir de
 la publication 136fpuw de la communauté homeassistant
```
---

     
 
all -  [ Vector databases: Minimum hardware requirements ](https://www.reddit.com/r/LangChain/comments/187g49m/vector_databases_minimum_hardware_requirements/) , 2023-12-05-0910
```
Hej, would anyone know the minimum hardware requirements of the typical vector database options (Qdrant, Pinecone, weavi
ate, Vespa...)?  and the footprint of the databases themselves (empty)?  
```
---

     
 
all -  [ Trying to pass variable via post to langserv so it gets to a tool ](https://www.reddit.com/r/LangChain/comments/187fj25/trying_to_pass_variable_via_post_to_langserv_so/) , 2023-12-05-0910
```
We have this line of code:

add\_route(app, react\_zero\_shot, path='/api/conversation/')

In the post request we are se
nding two variables; the input and a authentication token. We need the token to get to the tools, because the tools them
selves connect externally to other APIs and need an authentication token to 'do things'. But we cannot for the life of u
s get this token to the tool. Any suggestions?
```
---

     
 
all -  [ How to get generated queries from using MultiqueryRetriever ](https://www.reddit.com/r/LangChain/comments/187dpam/how_to_get_generated_queries_from_using/) , 2023-12-05-0910
```
&#x200B;

    retriever = MultiQueryRetriever(
       retriever=
    vectordb.as
    _retriever(), llm_chain=llm_chain, 
parser_key='lines'
    )  # 'lines' is the key (attribute name) of the parsed output
    # Results
    unique_docs = ret
riever.get_relevant_documents(
       query='What does the course say about model selection?'
    )

When i call this fu
nction get\_relevant\_documents it works fine but when i call  **generate\_queries()**  Function  it gives me error  



    retriever.generate_queries(question='What does the course say about model selection?')
    TypeError
    : generate_
queries() missing 1 required positional argument: 'run_manager'
```
---

     
 
MachineLearning -  [ [R] LLMs for structured data? ](https://www.reddit.com/r/MachineLearning/comments/185ei6v/r_llms_for_structured_data/) , 2023-12-05-0910
```
I've been trying to work with structured data in language models, and it's proving to be quite challenging. I'm confiden
t that with Langchain, I should be able to solve the problem, but I'm not entirely sure which path to take among all the
 options the library offers.

My issue is as follows: I have data in the form of dictionaries regarding a series of prod
ucts, for example, laptops. The data looks like this:

{Identifier 1: X, Identifier 2: Y, Value name: Z}

(Several succe
ssive dictionaries like this.)

I want to use this series of dictionaries as context, then feed a different dictionary i
nto the Language Model, and have it tell me if the 'Value name' makes sense given Identifiers 1 and 2. An example would 
be Identifier 1: laptops, Identifier 2: brand, Value name: Lenovo. In this case, it should return affirmative since Leno
vo makes sense as a brand. However, if I input 'oranges,' it should return negative.

Any ideas on which library I could
 use to tackle this problem?
```
---

     
 
MachineLearning -  [ [P] A new way of interacting with Hacker News ](https://www.reddit.com/r/MachineLearning/comments/183n6h7/p_a_new_way_of_interacting_with_hacker_news/) , 2023-12-05-0910
```
Hi all!

A couple of days ago, when I was scrolling down Hacker News, exploring news about OpenAI and the latest specula
tion about Q\*, it occurred to me to create a ChatBot that would allow me to interact with Hacker News directly, in a co
nversation.

Using streamlit, langchain and openai functions I managed to create a first version of this chat (I still h
ave to add RAG for news analysis and test other types of LLMs). 

Here is an example, what do you think?

Code: [https:/
/github.com/neural-maze/talking\_with\_hn](https://github.com/neural-maze/talking_with_hn)

App: [https://newsnerdhacker
bot.streamlit.app/](https://newsnerdhackerbot.streamlit.app/)

&#x200B;

https://i.redd.it/rtpof7biqi2c1.gif
```
---

     
 
MachineLearning -  [ [Discussion] Is it possible to built a Multi-LLM Assistant? ](https://www.reddit.com/r/MachineLearning/comments/182uuwp/discussion_is_it_possible_to_built_a_multillm/) , 2023-12-05-0910
```
 

  
For example with the following structure:

* System = GPT-4 Turbo + Llama2 +3rd LLM (!)+ Google or Bing API for we
bsearch + Langchain + any vectorDB + Document upload + longterm Memory + …

Idee behind it is to get more accurate, upda
ted (websearch) and specialized system or even let the LLms discuss your prompt before completion! Question is also, how
 shall the interaction of multiple LLMs in a system be organzied (Algorithm, Python Library …)? And what kind of Interac
tion can/should this be? Master-slave or Multi-Master system?
```
---

     
 
MachineLearning -  [ [D] Made some promises. Time to learn how to conduct very large scale pdf doc analysis. ](https://www.reddit.com/r/MachineLearning/comments/181gzek/d_made_some_promises_time_to_learn_how_to_conduct/) , 2023-12-05-0910
```
I have about a half million pdfs I need to summarize. Very wide range of types: invoices, diagrams, contracts, emails, l
etters, pictures, schedules, notices, data sheets, manuals, more. 

Which is... woof. Something else. I've been trying f
or many hours now to figure out a service/combination thereof that can get me there, but I'm seriously struggling. The *
ideal* solution would be to throw the pdfs in and have it return a csv with dates and summaries, maybe parsed out email 
heading info.

I'm currently running these pdfs through Acrobat OCR now, which its own special hell.

I've tried myriad 
local and webhosted solutions. The BEST results in what is almost the perfect system for this I found on https://docalys
is.com/. Good text results, works in batches, BUT I can only upload a single document at a time. They have a service to 
do batch processing and so I'm waiting to hear from them now. I imagine at the scale I need it's expensive.

I also got 
this solution working: https://github.com/mayooear/gpt4-pdf-chatbot-langchain. Seemed solid, I was able to upload a thou
sand pdfs in a single go, but it would keep returning information from only 2-3 documents. Upload 5? Results for 2-3. Up
load a thousand? Results for 2-3. My uneducated guess is that it's hitting the OpenAI API token limit, but maybe not?

I
 know it's possible, just not whether it's feasible for an end user.
```
---

     
 
MachineLearning -  [ Google PaLM Error [D] ](https://www.reddit.com/r/MachineLearning/comments/17y7arb/google_palm_error_d/) , 2023-12-05-0910
```
Google PaLM Error

Using LangChain and Google PaLM, in sequential chain concept getting following error,

ChatGooglePalm
Error: ChatResponse must have atleast one candidate

Please help!
```
---

     
 
MachineLearning -  [ [D] System Design question for LangChain ](https://www.reddit.com/r/MachineLearning/comments/17x545j/d_system_design_question_for_langchain/) , 2023-12-05-0910
```
Hi

Just to prepare the system design question for LangChain. Is there a resource that can walk me through the high leve
l pipeline? I know there are a bunch of resources that dive into detail implementation. But that's not I want. I want hi
gh level conceptual walk-through. 
```
---

     
 
MachineLearning -  [ [P] GPT vs. StarCraft ](https://www.reddit.com/r/MachineLearning/comments/17ro6el/p_gpt_vs_starcraft/) , 2023-12-05-0910
```
This is the first in a series of webcasts covering the development and experimentation of using GPT algorithms, LangChai
n and Python to control the high-level strategy of a StarCraft II bot. I’ll be running through the basics of the impleme
ntation, discussing the use of prompts and prompt engineering, and demonstrating the implementation in action.

[https:/
/youtu.be/E3Sj2L6ZnXA](https://youtu.be/E3Sj2L6ZnXA)
```
---

     
 
deeplearning -  [ [D] Utilizing Multimodal LLM for Extracting Tables and Images LangChain+LlamaIndex’s Role in Semi-St ](https://www.reddit.com/r/deeplearning/comments/185vd56/d_utilizing_multimodal_llm_for_extracting_tables/) , 2023-12-05-0910
```
In the domain of document analysis, the convergence of text, tables, and images presents formidable challenges for conve
ntional RAG (Retrieval Augmented Generation) methodologies. This complexity is further compounded within semi-structured
 data, notably in the extraction of tables from PDFs. Enter LangChain, a pioneering tool adept at navigating these intri
cate landscapes. Augmenting its capabilities is LlamaIndex, integrating Multi-Modal Retrieval Augmented Generation (RAG)
 techniques. Together, LangChain and LlamaIndex stand poised to revolutionize the handling and extraction of diverse con
tent types, promising a breakthrough in unraveling insights from varied data formats.

Link in the comment
```
---

     
