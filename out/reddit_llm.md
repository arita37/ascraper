 
all -  [ OpenGPT is an open-source alternative to OpenAI's custom ChatGPTs ](https://www.reddit.com/r/TheDecoder/comments/189sctd/opengpt_is_an_opensource_alternative_to_openais/) , 2023-12-04-0910
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

     
 
all -  [ Integration of XAgent into L3AGI Framework ](https://www.reddit.com/r/LangChain/comments/189pkr1/integration_of_xagent_into_l3agi_framework/) , 2023-12-04-0910
```
How do I Replace the existing Langchain REACT Agent in the L3AGI framework with the XAgent framework? 
```
---

     
 
all -  [ How to handle prompts asking for links instead of textual answers? ](https://www.reddit.com/r/LangChain/comments/189ml0n/how_to_handle_prompts_asking_for_links_instead_of/) , 2023-12-04-0910
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

     
 
all -  [ Custom SQL database infos ](https://www.reddit.com/r/LangChain/comments/189k1lx/custom_sql_database_infos/) , 2023-12-04-0910
```
Hello, 
I’m using sql agent, and I want to pass custom database tables infos ( column and tables infos )
Which format ca
n I pass those and how ?

Thanks in advance
```
---

     
 
all -  [ Embodied LLMs for robotics (code in comments) ](https://v.redd.it/jll5idt5zy3c1) , 2023-12-04-0910
```

```
---

     
 
all -  [ What am I missing? ](https://www.reddit.com/r/resumes/comments/189eefz/what_am_i_missing/) , 2023-12-04-0910
```
Would love some feedback on this resume. I've applied to 700+ entry level data scientist / machine learning engineer rol
es, and I've only gotten 3 interviews, 2 of which were referrals, both rejected after 2nd round even though I answered a
ll the questions and communicated my thoughts. I wouldn't be as worried if I have gotten more interviews. I have no idea
 what I'm doing wrong here.

https://preview.redd.it/yriw6t59gy3c1.png?width=805&format=png&auto=webp&s=bb1ef9152ade9432
0239989c96b73495c78ce88c
```
---

     
 
all -  [ Final year B.tech student from tier 1 insti -have I messed up too badly ](https://www.reddit.com/r/developersIndia/comments/189czbr/final_year_btech_student_from_tier_1_insti_have_i/) , 2023-12-04-0910
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

     
 
all -  [ Does Langchain support OpenAI-API compatible agents with it's ChatOpenAI, OpenAIFunctionsAgents, etc ](https://www.reddit.com/r/LangChain/comments/1899yhr/does_langchain_support_openaiapi_compatible/) , 2023-12-04-0910
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

     
 
all -  [ Strange behavior in my chatbot when responding to questions. ](https://www.reddit.com/r/LangChain/comments/1892m87/strange_behavior_in_my_chatbot_when_responding_to/) , 2023-12-04-0910
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

     
 
all -  [ How does Langchain make money? ](https://www.reddit.com/r/LangChain/comments/188znbs/how_does_langchain_make_money/) , 2023-12-04-0910
```
Since its an open source wrapper, wondering what is their revenue model?
```
---

     
 
all -  [ Build AI RAG Chat using LangChain and Convex ](https://www.reddit.com/r/LangChain/comments/188nfr8/build_ai_rag_chat_using_langchain_and_convex/) , 2023-12-04-0910
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

     
 
all -  [ In Search of Beginner Course for LLMs ](https://www.reddit.com/r/LLMDevs/comments/188mhjd/in_search_of_beginner_course_for_llms/) , 2023-12-04-0910
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

     
 
all -  [ I will be using LangChain for an AI Hackathon Challenge! ](https://www.reddit.com/r/LangChain/comments/188hd5w/i_will_be_using_langchain_for_an_ai_hackathon/) , 2023-12-04-0910
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

     
 
all -  [ I want to load and encode large medical texts ](https://www.reddit.com/r/LangChain/comments/188fwqo/i_want_to_load_and_encode_large_medical_texts/) , 2023-12-04-0910
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

     
 
all -  [ What will happen when knowledge about LLM will be inside the LLM training data? ](https://www.reddit.com/r/singularity/comments/188fmy0/what_will_happen_when_knowledge_about_llm_will_be/) , 2023-12-04-0910
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

     
 
all -  [ Best UI for API to iterate over large datasets? ](https://www.reddit.com/r/LocalLLaMA/comments/188aarc/best_ui_for_api_to_iterate_over_large_datasets/) , 2023-12-04-0910
```
I have been using text generation web UI to iterate over large datasets where a template string is fed in with some data
 from a database to various LLMs. What web UI API do you feel like is best for this in terms of ease of use and adding f
eatures (e.g. adding a RAG, Langchain).
```
---

     
 
all -  [ Is this Text SEgmentation API is the best way to analyze which chunk size works better for our data  ](https://www.reddit.com/r/LangChain/comments/18877lh/is_this_text_segmentation_api_is_the_best_way_to/) , 2023-12-04-0910
```
[https://docs.ai21.com/docs/text-segmentation-api#features](https://docs.ai21.com/docs/text-segmentation-api#features)  



Anyone used this ? 
```
---

     
 
all -  [ What are the SOTA models for function calling? ](https://www.reddit.com/r/LangChain/comments/1882fv3/what_are_the_sota_models_for_function_calling/) , 2023-12-04-0910
```
Looking for a fine-tuned model on huggingface
```
---

     
 
all -  [ Looking for advice: Giving a LLM obscure knowledge ](https://www.reddit.com/r/LangChain/comments/188141p/looking_for_advice_giving_a_llm_obscure_knowledge/) , 2023-12-04-0910
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

     
 
all -  [ Using SQLDatabaseToolkit and LlamaCpp to Query a Local Database with a Local LLM ](https://www.reddit.com/r/LangChain/comments/187wah9/using_sqldatabasetoolkit_and_llamacpp_to_query_a/) , 2023-12-04-0910
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

     
 
all -  [ SWE intern resume feedback ](https://i.redd.it/oqrjpsi3ek3c1.jpeg) , 2023-12-04-0910
```
Hi there,
I am applying for. SWE intern roles and haven't received any offer or OA. Can you please give some feedback so
 I can at least pass the screening process.
```
---

     
 
all -  [ SWE intern resume feedback ](https://i.redd.it/87p5sduidk3c1.jpeg) , 2023-12-04-0910
```
Hi there,
I am applying for SWE intern roles, but got 0 offers or OA yet. Can you please give feedback on my resume so I
 can pass screening process at least?
```
---

     
 
all -  [ Seeking Guidance: Implementing Multimodal RAG in Node.js – Any JavaScript Resources? ](https://www.reddit.com/r/LangChain/comments/187t1nn/seeking_guidance_implementing_multimodal_rag_in/) , 2023-12-04-0910
```
Hey,

I'm currently working on integrating Multimodal RAG into my Node.js application. Has anyone implemented this befor
e? If so, could you guide me to the libraries or resources you used? Most of what I've come across is in Python. I'm won
dering if it's feasible to implement this version of RAG in JavaScript. Thanks!
```
---

     
 
all -  [ Similarity search with relevancy score ](https://www.reddit.com/r/LangChain/comments/187oien/similarity_search_with_relevancy_score/) , 2023-12-04-0910
```
What is the difference between similarity search and similarity search with relevancy score?

Which algorithms are used 
under both?

and what is the best practice with FAISS vector store?

&#x200B;
```
---

     
 
all -  [ Possible to expand training on existing models? ](https://www.reddit.com/r/ChatGPT/comments/187o3nk/possible_to_expand_training_on_existing_models/) , 2023-12-04-0910
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

     
 
all -  [ Help! Getting the same error with Ollama and Langchain at random time while my code runs. ](https://www.reddit.com/r/LocalLLaMA/comments/187he7d/help_getting_the_same_error_with_ollama_and/) , 2023-12-04-0910
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

     
 
all -  [ [Home Assistant] Quelqu'un a-t-il encore intégré un LLM open source avec Assistant à domicile? ](https://www.reddit.com/r/redditenfrancais/comments/187gx88/home_assistant_quelquun_atil_encore_intégré_un/) , 2023-12-04-0910
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

     
 
all -  [ Vector databases: Minimum hardware requirements ](https://www.reddit.com/r/LangChain/comments/187g49m/vector_databases_minimum_hardware_requirements/) , 2023-12-04-0910
```
Hej, would anyone know the minimum hardware requirements of the typical vector database options (Qdrant, Pinecone, weavi
ate, Vespa...)?  and the footprint of the databases themselves (empty)?  
```
---

     
 
all -  [ Trying to pass variable via post to langserv so it gets to a tool ](https://www.reddit.com/r/LangChain/comments/187fj25/trying_to_pass_variable_via_post_to_langserv_so/) , 2023-12-04-0910
```
We have this line of code:

add\_route(app, react\_zero\_shot, path='/api/conversation/')

In the post request we are se
nding two variables; the input and a authentication token. We need the token to get to the tools, because the tools them
selves connect externally to other APIs and need an authentication token to 'do things'. But we cannot for the life of u
s get this token to the tool. Any suggestions?
```
---

     
 
all -  [ How to get generated queries from using MultiqueryRetriever ](https://www.reddit.com/r/LangChain/comments/187dpam/how_to_get_generated_queries_from_using/) , 2023-12-04-0910
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

     
 
all -  [ YiVal for prompt auto-tuning ](https://www.reddit.com/r/u_YiVal/comments/1877dsp/yival_for_prompt_autotuning/) , 2023-12-04-0910
```
Developing language model prompts can be biased , time-consuming , and subject to data limitations. By prompt auto-tunin
g through the YiVal framework, this process can be greatly simplified, reducing the burden on developers and improving w
ork efficiency.

&#x200B;

https://preview.redd.it/07elrp9cce3c1.png?width=1100&format=png&auto=webp&s=9ce5602cd2202f222
b8737cdaada9a37c5eb68e2

\#Yival #GenAI #PromptEngineering #langchain #openai #automl #mlops #chatgpt
```
---

     
 
all -  [ Cant import langchain OpenAI ](https://www.reddit.com/r/LangChain/comments/1870pdw/cant_import_langchain_openai/) , 2023-12-04-0910
```
I am trying to use the OpenAI and create\_csv\_agent import from langchain however it seems to be greyed out and not ava
ilable. I have tried reinstalling on a virtual environment and I am still getting the same issue. Does anyone know a fix
 to this?

https://preview.redd.it/0qlr6eeruc3c1.png?width=818&format=png&auto=webp&s=221a237b31bb0ea8b7a9abaa9a9a9bfa17
e7ac8a

Other imports seem to work such as the create\_json\_agent so I do not know why it wont let me import the create
\_csv\_agent and OpenAI. I have tried re-installing langchain and openai many times and there still is an issue. Any sup
port is much appreciated.

EDIT: I have managed to get the OpenAI import working however when I try to instal csv\_agent
s I get this message - ERROR: Could not find a version that satisfies the requirement csv\_agent (from versions: none)


ERROR: No matching distribution found for csv\_agent
```
---

     
 
all -  [ Looking for overlapping information between the documents of two different companies ](https://www.reddit.com/r/LangChain/comments/186yx0y/looking_for_overlapping_information_between_the/) , 2023-12-04-0910
```
I have documentation from different companies, particularly regarding business process, roles, and organizational depart
ments (\*). The information doesn't necessarily appears under those subtitles inside the documentation. What i need is, 
given two companies, find if those companies have overlapping business process, roles, or organizational departments bet
ween them.

I was thinking in two approaches.

The first one (brute force): find per each company the information regard
ing (\*), (probably) chunk it, and vectorize it. Then given the chunks from one company i will look for the most similar
 chunks belonging to the other company (above certain threshold), and if found any compare then with a llm call. 

The s
econd one: according to this article [https://mlops.community/combine-and-query-multiple-documents-with-llm/](https://ml
ops.community/combine-and-query-multiple-documents-with-llm/), it is possible to query multiple documents (i would like 
to know what happens if the documents are bigger than the proposed in the example) looking for (\*) over certain indices
 (companies).

Do you think that my understand is correct? do you have some experience with that?

Thanks!
```
---

     
 
all -  [ How do improve results of vector embeddings in the following scenario ? ](https://www.reddit.com/r/LangChain/comments/186xvts/how_do_improve_results_of_vector_embeddings_in/) , 2023-12-04-0910
```
I'm currently working on a document selection problem and needed some inputs on how to proceed further in solving thisTh
e input I have is user data and I've to return a set of documents which match the user is talking about in the descripti
on.

The list of documents is very huge around 2-3 Million records and they are very unstructured and user input necessa
rily might not be present in the document.

Currently I've tried the following

1. Create summary of all the documents u
sing llm
2. Create embedding of this and store it in vector db.
3. Create summary of user input on the fly
4. create emb
edding of the summarised user input and search in vector db and return top x documents with probability >=y

This does g
et me documents very quickly but there are a lot of false positives and I'm not sure how to reduce these false positives
.

One of the thing I found is user query might not be present in the documents directly so in this case there are a lot
 of false positives.

Is any any other way to solve this selection problem or reduce the number of false positives that 
come up in vector search ?

I also tried re ranking with BM25 algorithm but it did not help a lot
```
---

     
 
all -  [ What's your preferred development language? ](https://www.reddit.com/r/LangChain/comments/186x2er/whats_your_preferred_development_language/) , 2023-12-04-0910
```
Curious why the python package for LangChain is much more popular than the Javascript package. Is this because the major
ity of people trying LangChain this early are coming from ML eng or data science, where python is the most common langua
ge, or something else.   


What's your preferred development language and background?

[View Poll](https://www.reddit.c
om/poll/186x2er)
```
---

     
 
all -  [ RAG filtering docs to only send relevant data to llm ](https://www.reddit.com/r/LangChain/comments/186sgyf/rag_filtering_docs_to_only_send_relevant_data_to/) , 2023-12-04-0910
```
Hey all,

I need some help with understanding how to filter or do similarity scores I think..

My goal is to chunk a tex
t file, embed it, have a user ask one question about the text. However I want to ensure the data being sent to llm (text
 file chunks / documents) are only the ones relevant to the original user question.

For example: text file contains a b
unch of info about processes in the company. I chunk/split and embed with memory vectorStore.

User asks question about 
one specific process, llm is sent chunks which seem related to the relevant process and other chunks are ignored. 

This
 is attempt to only have context which is useful for answering the question and hoping for a more reliable result.

Is m
y logic correct or is there some simple way to achieve this?

Thank you
```
---

     
 
all -  [ I have created a free online ChatGPT, welcome everyone to give it a try. ](https://www.reddit.com/r/LangChain/comments/186iv2u/i_have_created_a_free_online_chatgpt_welcome/) , 2023-12-04-0910
```
Deploy based on Cloudflare AI Workers.

&#x200B;

[https://freechat.mggg.cloud/](https://freechat.mggg.cloud/)
```
---

     
 
all -  [ AI agent that acts as an expert in robotics (a LangChain application) ](https://www.reddit.com/r/LangChain/comments/186acth/ai_agent_that_acts_as_an_expert_in_robotics_a/) , 2023-12-04-0910
```
I would like to introduce you to  [ROScribe](https://github.com/RoboCoachTechnologies/ROScribe): an AI-native robot inte
gration solution that generates the entire robot software based on the description provided through natural language. RO
Scribe uses GPT and LangChain under the hood.

I am pleased to announce that we made a new release that supports a major
 feature which comes very helpful in robot integration.

**Training ROScribe on ROS index**

We trained [ROScribe](https
://github.com/RoboCoachTechnologies/ROScribe) on all open source repositories and ROS packages listed on ROS index. Unde
r the hood, we load all documents and metadata associated with all repositories listed on ROS index into a vector databa
se and use RAG (retrieval augmented generation) technique to access them. Using this method, we essentially teach the LL
M (gpt3.5 in our default setting) everything on ROS Index to make it an AI agent expert in robotics.  
ROScribe is train
ed on all ROS versions (ROS & ROS 2) and all distributions.

**Use ROScribe as a robotics expert**

With this release yo
u can use [ROScribe](https://github.com/RoboCoachTechnologies/ROScribe) as your personal robotics consultant. You can as
k him any technical question within robotics domain and have him show you the options you have within ROS index to build
 your robot. You can ask him to show you examples and demos of a particular solution, or help you install and run any of
 the ROS packages available in ROS index.  
Here is a [demo](https://www.youtube.com/watch?v=3b5FyZvlkxI) that shows ROS
cribe helping a robotics engineer to find a multilayer grid mapping solution and shows him how to install it.

To run RO
Scribe for this specific feature use: roscribe-rag in your command line.

You can find more info on our [github](https:/
/github.com/RoboCoachTechnologies/ROScribe) and its wiki page.

**New in this release**

Here are what’s new in release 
v0.0.4:

Knowledge extraction:

* Scripts for automatic extraction of ROS package documentation given your choice of ROS
 version
* Build a vector database over ROS Index

Retrieval augmented generation (RAG) capabilities for ROScribe:

* No
w ROScribe has access to the most recent open-source ROS repositories that can be found on ROS Index
* ROScribe can be c
alled as an AI agent that assists you with finding the relevant ROS packages for your project
* Use roscribe-rag to run 
the RAG agent

Creating a wiki page for documentation to keep the readme file short.

**Future roadmap**  
As of now, th
e entire code is generated by the LLM, meaning that the RAG feature (explained above) is currently a stand-alone feature
 and isn’t fully integrated into the main solution. We are working on a fully-integrated solution that retrieves the hum
an-written (open source) ROS packages whenever possible (from ROS index or elsewhere), and only generates code when ther
e is no better code available. This feature will be part of our next release.  
We also plan to give ROScribe a web-base
d GUI.

Please checkout our [github](https://github.com/RoboCoachTechnologies/ROScribe) and let us know what you think.
```
---

     
 
all -  [ Zapier NLA help ](https://www.reddit.com/r/LangChain/comments/1867cb2/zapier_nla_help/) , 2023-12-04-0910
```
I'm trying to use zapier natural language actions with langchain agents. However, it says that it's deprecaated on the l
angchain website [https://python.langchain.com/docs/integrations/tools/zapier](https://python.langchain.com/docs/integra
tions/tools/zapier)  How do I connect my agent to zapier now? There's no updates on either side regarding this deprecati
on.
```
---

     
 
all -  [ Can't run Falcon 7b locally ](https://www.reddit.com/r/Langchaindev/comments/1866nmp/cant_run_falcon_7b_locally/) , 2023-12-04-0910
```
Hello, I'm about 2 minutes from an aneurysm trying to get this running locally.

Here's my code:

    from langchain.pro
mpts import PromptTemplate
    from langchain.chains import LLMChain
    from langchain.llms.huggingface_pipeline import
 HuggingFacePipeline
    from transformers import AutoTokenizer, pipeline
    
    import torch
    
    model = 'tiiuae
/falcon-7b-instruct'
    
    tokenizer = AutoTokenizer.from_pretrained(model, offload_folder='./offload_dir')
    
    
pipeline = pipeline(
        'text-generation',
        model=model,
        tokenizer=tokenizer,
        torch_dtype=to
rch.bfloat16,
        device_map='auto',
        max_length=200,
        do_sample=True,
        top_k=10,
        num_r
eturn_sequences=1,
        eos_token_id=tokenizer.eos_token_id
    )

And the error output:

    Traceback (most recent 
call last): File '/home/friend/Documents/falcon7bLangChain/main.py', line 12, in <module> pipeline = pipeline( File '/ho
me/friend/Documents/falcon7bLangChain/venv/lib/python3.10/site-packages/transformers/pipelines/init.py', line 870, in pi
peline framework, model = infer_framework_load_model( File '/home/friend/Documents/falcon7bLangChain/venv/lib/python3.10
/site-packages/transformers/pipelines/base.py', line 282, in infer_framework_load_model raise ValueError( ValueError: Co
uld not load model tiiuae/falcon-7b-instruct with any of the following classes: (<class 'transformers.models.auto.modeli
ng_auto.AutoModelForCausalLM'>, <class 'transformers.models.falcon.modeling_falcon.FalconForCausalLM'>). See the origina
l errors:
    while loading with AutoModelForCausalLM, an error is thrown:
    Traceback (most recent call last):
      
File '/home/friend/Documents/falcon7bLangChain/venv/lib/python3.10/site-packages/transformers/pipelines/base.py', line 2
69, in infer_framework_load_model
        model = model_class.from_pretrained(model, **kwargs)
      File '/home/friend/
Documents/falcon7bLangChain/venv/lib/python3.10/site-packages/transformers/models/auto/auto_factory.py', line 566, in fr
om_pretrained
        return model_class.from_pretrained(
      File '/home/friend/Documents/falcon7bLangChain/venv/lib/
python3.10/site-packages/transformers/modeling_utils.py', line 3480, in from_pretrained
        ) = cls._load_pretrained
_model(
      File '/home/friend/Documents/falcon7bLangChain/venv/lib/python3.10/site-packages/transformers/modeling_uti
ls.py', line 3601, in _load_pretrained_model
        raise ValueError(
    ValueError: The current `device_map` had weig
hts offloaded to the disk. Please provide an `offload_folder` for them. Alternatively, make sure you have `safetensors` 
installed if the model you are using offers the weights in this format.
    
    while loading with FalconForCausalLM, a
n error is thrown:
    Traceback (most recent call last):
      File '/home/friend/Documents/falcon7bLangChain/venv/lib/
python3.10/site-packages/transformers/pipelines/base.py', line 269, in infer_framework_load_model
        model = model_
class.from_pretrained(model, **kwargs)
      File '/home/friend/Documents/falcon7bLangChain/venv/lib/python3.10/site-pac
kages/transformers/modeling_utils.py', line 3480, in from_pretrained
        ) = cls._load_pretrained_model(
      File 
'/home/friend/Documents/falcon7bLangChain/venv/lib/python3.10/site-packages/transformers/modeling_utils.py', line 3601, 
in _load_pretrained_model
        raise ValueError(
    ValueError: The current `device_map` had weights offloaded to th
e disk. Please provide an `offload_folder` for them. Alternatively, make sure you have `safetensors` installed if the mo
del you are using offers the weights in this format.

I have specified an `offload_folder`, called `offload_dir` in the 
same directory as the script. `safetensors` is installed, and the `transformers` package is the newest available version
. I'm completely lost on what the issue could be, any ideas?
```
---

     
 
MachineLearning -  [ [R] LLMs for structured data? ](https://www.reddit.com/r/MachineLearning/comments/185ei6v/r_llms_for_structured_data/) , 2023-12-04-0910
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

     
 
MachineLearning -  [ [P] A new way of interacting with Hacker News ](https://www.reddit.com/r/MachineLearning/comments/183n6h7/p_a_new_way_of_interacting_with_hacker_news/) , 2023-12-04-0910
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

     
 
MachineLearning -  [ [Discussion] Is it possible to built a Multi-LLM Assistant? ](https://www.reddit.com/r/MachineLearning/comments/182uuwp/discussion_is_it_possible_to_built_a_multillm/) , 2023-12-04-0910
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

     
 
MachineLearning -  [ [D] Made some promises. Time to learn how to conduct very large scale pdf doc analysis. ](https://www.reddit.com/r/MachineLearning/comments/181gzek/d_made_some_promises_time_to_learn_how_to_conduct/) , 2023-12-04-0910
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

     
 
MachineLearning -  [ Google PaLM Error [D] ](https://www.reddit.com/r/MachineLearning/comments/17y7arb/google_palm_error_d/) , 2023-12-04-0910
```
Google PaLM Error

Using LangChain and Google PaLM, in sequential chain concept getting following error,

ChatGooglePalm
Error: ChatResponse must have atleast one candidate

Please help!
```
---

     
 
MachineLearning -  [ [D] System Design question for LangChain ](https://www.reddit.com/r/MachineLearning/comments/17x545j/d_system_design_question_for_langchain/) , 2023-12-04-0910
```
Hi

Just to prepare the system design question for LangChain. Is there a resource that can walk me through the high leve
l pipeline? I know there are a bunch of resources that dive into detail implementation. But that's not I want. I want hi
gh level conceptual walk-through. 
```
---

     
 
MachineLearning -  [ [P] GPT vs. StarCraft ](https://www.reddit.com/r/MachineLearning/comments/17ro6el/p_gpt_vs_starcraft/) , 2023-12-04-0910
```
This is the first in a series of webcasts covering the development and experimentation of using GPT algorithms, LangChai
n and Python to control the high-level strategy of a StarCraft II bot. I’ll be running through the basics of the impleme
ntation, discussing the use of prompts and prompt engineering, and demonstrating the implementation in action.

[https:/
/youtu.be/E3Sj2L6ZnXA](https://youtu.be/E3Sj2L6ZnXA)
```
---

     
 
deeplearning -  [ [D] Utilizing Multimodal LLM for Extracting Tables and Images LangChain+LlamaIndex’s Role in Semi-St ](https://www.reddit.com/r/deeplearning/comments/185vd56/d_utilizing_multimodal_llm_for_extracting_tables/) , 2023-12-04-0910
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

     
