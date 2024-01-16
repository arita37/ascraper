 
all -  [ Anyone trained and hosted their own knowledge base chatbot? ](https://www.reddit.com/r/AIBizOps/comments/197mu0h/anyone_trained_and_hosted_their_own_knowledge/) , 2024-01-16-0910
```
I’ve been playing around with this a little.  I’m trying to come up with some chatbot solutions to help my company.

Lik
e a lot of companies, we have tons of internal data/practices.  I’d love to create something a user could query and find
 an answer.

I built something last night using LangChain and FAISS with FastText, and it worked, but it just basically 
functioned as an inaccurate text search.

I was hoping to implement something that could read and summarize for the user
.  Obviously, I could create something like a wrapper around ChatGPT, but we have a few limitations.

1. It has to be co
mpletely private, so it has to be hosted locally and we can’t send sensitive data to some external vendor.

2. It has to
 be free.

3. We don’t want it having access to external data (e.g., no questions about politics, etc.).

Has anyone bui
lt anything like this?  I’m extremely new, so please don’t hurt me if I’m asking for something stupid or impossible.

Th
anks in advance!
```
---

     
 
all -  [ How to add web search to ollama model ](https://www.reddit.com/r/ollama/comments/197meew/how_to_add_web_search_to_ollama_model/) , 2024-01-16-0910
```
Hello guys, does anyone know how to add an internet search option to ollama? I was thinking of using LangChain with a se
arch tool like DuckDuckGo, what do you think? 
```
---

     
 
all -  [ Mistral 7B QAGeneration Chain Langchain - JSONDecode Error ](https://www.reddit.com/r/LangChain/comments/197j354/mistral_7b_qageneration_chain_langchain/) , 2024-01-16-0910
```
hello   
I'm trying to use the Mistral 7B model for question-answer generation using the QAGeneration Chain  
 

`def ll
m_question_generation_pipeline(chunks):`  
`documents = [Document(page_content=chunk) for chunk in chunks]`  
`repo_id =
 'mistralai/Mistral-7B-v0.1'`  
`llm = HuggingFaceHub(repo_id=repo_id, model_kwargs={'temperature': 0.5, 'max_length': 5
12})`  
`qa_chain = QAGenerationChain.from_llm(llm = llm, verbose = True)`  
`raw_output = qa_chain.run(documents[0].pag
e_content)`  
`print('Raw Output:', raw_output)`

&#x200B;

this is my code, but I'm getting this error frequently  
`ra
ise JSONDecodeError('Expecting value', s, err.value) from None`

`json.decoder.JSONDecodeError: Expecting value: line 1 
column 2 (char 1)`  


this is the prompt created by QAGeneration chain  
`Prompt after formatting:`

`You are a smart a
ssistant designed to help high school teachers come up with reading comprehension questions.`

`Given a piece of text, y
ou must come up with a question and answer pair that can be used to test a student's reading comprehension abilities.`


`When coming up with this question/answer pair, you must respond in the following format:`

`\`\`\``

`{`

`'question': 
'$YOUR_QUESTION_HERE',`

`'answer': '$THE_ANSWER_HERE'`

`}`

`\`\`\``

&#x200B;

`Everything between the \`\`\` must be
 valid json.`

&#x200B;

`Please come up with a question/answer pair, in the specified JSON format, for the following te
xt:`  


I searched for this error, it is saying that it could be possible if the LLM is not giving proper JSON formated
 output  
Would anyone be able to help me solve this error?
```
---

     
 
all -  [ [D] Code vs JSON output for LLM agents? Frameworks like LangChain rely on LLMs responding with JSON  ](https://www.reddit.com/r/MachineLearning/comments/197f416/d_code_vs_json_output_for_llm_agents_frameworks/) , 2024-01-16-0910
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

     
 
all -  [ I am a technical blogger and want to train an LLM on my blogs. ](https://www.reddit.com/r/LangChain/comments/197eq8d/i_am_a_technical_blogger_and_want_to_train_an_llm/) , 2024-01-16-0910
```
Learning LangChain so figured I would love to see how llms learn my writing and as a bonus would write about how i built
 this?

So need help with a few questions from the community

1) Which LLM would be best other than OpenAi models as I w
ant to experiment with opensource models

2) list of tools, agents  and chains which would help me do this? 

3) Bonus m
y content has code embedded in it and visualizations, anyway I could tell the LLM to do it for me?
```
---

     
 
all -  [ Need suggestions on code understanding by llm and output. ](https://www.reddit.com/r/LangChain/comments/197b58d/need_suggestions_on_code_understanding_by_llm_and/) , 2024-01-16-0910
```
What I want to achieve?
User can improve code quality and refactoring for give source code repository.

Input - code rep
ository (python, java, dotnet, etc.)
Db - chromadb or pinecone
Embeddeding - sentence transformer model
Top k results - 
MMR search
Key - Azureopnai key n endpoint 

Kindly suggest LLM and retrieval in best way if possible. Any link or refer
ences from Microsoft is also fine.
```
---

     
 
all -  [ Building AI chatbot ](https://www.reddit.com/r/aws/comments/197aas5/building_ai_chatbot/) , 2024-01-16-0910
```
Hi all

I'd like to build an AI chatbot. I'm literally fresh in the subject and don't know much about AWS tools in that 
matter, so please help me clarify.  

More details:  

The model is yet to be chosen and to be trained with specific FAQ
 & answers. It should answer user's question, finding most sutiable answer from the FAQ.  

If anyone has ever tried to 
built similar thing please suggest the tools and possible issues with what I have found out so far.  

  

My findings: 
 

1. AWS Bedrock (seems more friendly than Sagemaker)  
2. Will have to create FAQ Embeddings, so probably need a vecto
r store? Is OpenSearch good?   
3. Are there also things like agents in here? For prompt engineering for example?   
4. 
With having Bedrock and it's tools, would I still need to use Langchain for example?  

 
```
---

     
 
all -  [ Custom GPT to assist with langchain development ](https://www.reddit.com/r/LangChain/comments/1979xgt/custom_gpt_to_assist_with_langchain_development/) , 2024-01-16-0910
```
Hi Guys,

&#x200B;

I did a little side project to help me on my project, I'm doing a database parser agent using Clause
 2.1 on bedrock that uses Python to query Druid with a LOT of contexts.

Been struggling quite a lot with documentation 
with anything that is not open ai.

So I created a Custom GPT to help me where it can.

&#x200B;

It's not perfect, but 
it's been helping me a little so I wanted to share it with you all.

&#x200B;

[Langchain Specialist](https://chat.opena
i.com/g/g-yqSII6PUj-langchain-specialist)
```
---

     
 
all -  [ What is similarity search with relevancy score ](https://www.reddit.com/r/LangChain/comments/19795k7/what_is_similarity_search_with_relevancy_score/) , 2024-01-16-0910
```
What is the difference between a similarty search and similarty search with relevancy score?
```
---

     
 
all -  [ Why Reranking exists in the first place? ](https://www.reddit.com/r/LangChain/comments/1978ywu/why_reranking_exists_in_the_first_place/) , 2024-01-16-0910
```
I'm trying to understand why Reranking is often needed in RAG technique and why it can't be just skipped completely.

Wo
uld Reranking still exist if LLM models were bigger and better at creating embeddings(converting prompts into vectors in
 space)? 
```
---

     
 
all -  [ Getting error on chat history langchain. ValueError: variable chat_history should be a list of base  ](https://www.reddit.com/r/LangChain/comments/19777hm/getting_error_on_chat_history_langchain/) , 2024-01-16-0910
```
[https://python.langchain.com/docs/use\_cases/question\_answering/chat\_history](https://python.langchain.com/docs/use_c
ases/question_answering/chat_history)  
I am referring to these docs for chat history  
 I\]this code is giving me error
 on this 'chat\_history.extend(\[HumanMessage(content=question), ai\_msg\])  
line'

chat\_history = \[\]  
question = '
What is function of form nec?'  
ai\_msg = rag\_chain.invoke({'question': question, 'chat\_history': chat\_history})  
c
hat\_history.extend(\[HumanMessage(content=question), ai\_msg\])  
second\_question = 'is there anything else about it?'
  
rag\_chain.invoke({'question': second\_question, 'chat\_history': chat\_history})
```
---

     
 
all -  [ Best way to validate llm prompts? ](https://www.reddit.com/r/OpenAI/comments/1974nfo/best_way_to_validate_llm_prompts/) , 2024-01-16-0910
```
We have a platform for data analytics which uses a very simple dsl to generate charts.  
We have been experimenting with
 llms to use natural language that gets translated into this dsl and hence generates charts.

This is working pretty goo
d.  
The stack is langchain with openai api. (don't have much experience with llms, it's a prototype to get a feel for i
t)

The question is what is the best way to limit the options user can type in as a prompt.  
Basically the the only all
owed things should be: 'What is the X, Y over 10 days period for this or that?'  
I don't want users to ask questions li
ke when did we first land on the moon.

Is it something that is possible to do at all without additional tooling?  
We p
robably don't want to train another model to classify the prompt as valid or invalid or something similar.
```
---

     
 
all -  [ Finetune Mixtral on Enterprise data - How does the training data should look like? ](https://www.reddit.com/r/LangChain/comments/1973jxk/finetune_mixtral_on_enterprise_data_how_does_the/) , 2024-01-16-0910
```
Hi,

I want to fine-tune a Mistral or Mixtral model on my companies data. Specifically the model should write bullet-poi
nts to full texts. I was wondering how the training data has to look like for this task?

Is it a valid way to let a LLM
 create bullet points out of a text and use these bullet-points-full-text-examples for training? 
```
---

     
 
all -  [ Anyone have Yi-34B (running with Ollama) with LangChain working ](https://www.reddit.com/r/LangChain/comments/196vqu3/anyone_have_yi34b_running_with_ollama_with/) , 2024-01-16-0910
```
I've been able to get all other local models, running with Ollama, working with LangChain. However, Yi-34B never returns
 a response.

I'm running an RTX 3090 and it is fitting in VRAM according to nvtop (20GB used).

Something simple like t
his never finishes (the last line is the one that never finishes):

    from langchain_community.llms import Ollama
    

    ollama_model_name = 'yi:34b-chat-q4_K_M'
    llm = Ollama(model=ollama_model_name, temperature=0.1)
    
    llm.in
voke('why is the sky blue?') # This line never finishes...

I run it directly with Ollama and it responds instantly:

  
  $ ollama run yi:34b-chat-q4_K_M
    >>> why is the sky blue?
    The sky appears blue to us because of a phenomenon ca
lled Rayleigh scattering. This occurs when light from the sun 
    interacts with the molecules of the Earth's atmospher
e, which are composed primarily of nitrogen and oxygen. These 
    molecules are much smaller than the wavelength of vis
ible light, so they can scatter light very efficiently.
    
    When sunlight enters the atmosphere, it strikes these a
tmospheric particles and is scattered in different directions.
    The shorter wavelengths of blue light are scattered m
ore than longer wavelengths of red light because they have 
    higher energy and thus a greater probability to interact
 with the molecules. This means that more blue light gets 
    scattered relative to other colors, which is why we see a
 blue sky most of the time.
    
    The intensity of Rayleigh scattering also depends on the angle at which light hits 
an atmospheric molecule. 
    Scattering is most effective when light hits molecules nearly head-on, which preferentiall
y scatters light in all 
    directions away from the sun. This scattered blue light then reaches our eyes after being s
cattered multiple times by
    different air molecules, giving us the perception of a blue sky.
    
    The color we se
e also depends on the observer's line of sight relative to the sun. When the sun is high in the sky, 
    more blue ligh
t scatters directly into our eyes, making the sky appear very blue. As the sun approaches the horizon, 
    the light ha
s to pass through more air and is scattered less efficiently, which means that more red light reaches our
    eyes, resu
lting in a reddish sky at sunset and sunrise.
    
    Additionally, other factors can influence the color of the sky, s
uch as pollution or dust particles in the 
    atmosphere, which can scatter light differently and change the appearance
 of the sky.
    

Any ideas?
```
---

     
 
all -  [ Chatbot for potential customers ](https://www.reddit.com/r/LangChain/comments/196uo2k/chatbot_for_potential_customers/) , 2024-01-16-0910
```
I have some experience in programming, mostly in nodeJS. Basically I want to create a chatbot that 
1. qualifies leads b
y asking questions
2. answers questions from my knowledge base using RAG. 
3. If the user wants to set up an appointment
, it extracts the information and stores it in a table. 

I want the bot to handle multiple conversations concurrently. 


Read through langchain documentation but still confused how to approach this. If you've made anything similar, please 
share some insight!
```
---

     
 
all -  [ A python package I created for llms application including my own implementation of long short term m ](https://www.reddit.com/r/LocalLLaMA/comments/196qqoy/a_python_package_i_created_for_llms_application/) , 2024-01-16-0910
```
[https://github.com/nath1295/LLMPlus](https://github.com/nath1295/LLMPlus)

I find Langchain annoying for not letting yo
u set different llms with different generation configurations, so I tried to build my own custom llms to avoid loading l
ocal models multiple times when I want to build an agent or tool that uses the same underlying model. Also, some of the 
streaming and stop words for llms are not that great in langchain, so I have my own implementation in this package I cre
ated.   
I am still using an Intel MacBook (too poor to get Nvidia cards or even a new Macbook :( ) to work on this proj
ect, so I cannot guarantee the installation will be seamless, but hopefully the pip install works. The code should be wo
rking with Cuda or apple silicon (used Colab and my friend's flashy new macbook to briefly test it).  


Stuff I have in
 the package:

* An LLM factory class to generate Langchain-compatible llms while only loading the model once.
* Embeddi
ng toolkits that have text splitters bundled with the embedding model.
* A Vector database class built on top of FAISS f
or local storage.
* Memory classes: (base one and one with both long-term and short-term memory, powered by a vector dat
abase)
* Prompt template class that helps you to format your prompt with different prompt formats (have some presets lik
e llama2, chatml, vicuna etc.)
* A base tool class and a web search tool with duckduckgo as an example (please have a lo
ok, wonder if there are better ways to do that)
* A Gradio chatbot web app that lets you store different conversations, 
also you can set your own system prompt and configure the long-term and short-term memory settings, and you can set gene
ration configurations like temperature, max new tokens, top k etc. (This is just for fun, my front-end skills are not be
tter than a monkey to be very honest.)
* And of course, the docs in the repo as well.

&#x200B;

I know I'm no expert, t
here are plenty of people in this sub who are extremely knowledgeable in this LLM field, so treat this as an amateur pro
ject looking for advice if you can bear with me for my spaghetti code. Would really appreciate any comments :')) Forgive
 me if I can't do much testing on fancy GPUs like you guys have, trying not to spend any money to work on this project..
.
```
---

     
 
all -  [ Resume review for data scientist position ](https://www.reddit.com/r/resumes/comments/196omyb/resume_review_for_data_scientist_position/) , 2024-01-16-0910
```
Hi Everyone,

I would love to get some feedback about my resume.

Target positions: data scientist / Senior data scienti
st positions

Location: USA

Thanks!

&#x200B;

https://preview.redd.it/jvdpeev7qgcc1.jpg?width=2550&format=pjpg&auto=we
bp&s=5f1dc9e2740df855bf44262def4f87c39561d189
```
---

     
 
all -  [ can i get an invite code for langsmith please , been waiting forever ](https://www.reddit.com/r/LangChain/comments/196nq3r/can_i_get_an_invite_code_for_langsmith_please/) , 2024-01-16-0910
```
can i get an invite code for langsmith please , been waiting forever
```
---

     
 
all -  [ Using LLMs to draw simple insight from tabular data: a discussion ](https://www.reddit.com/r/dataengineering/comments/196nl41/using_llms_to_draw_simple_insight_from_tabular/) , 2024-01-16-0910
```
Hey hey all, data/analytics engineer here,

I got a lenghty topic, hopefully worthy of a lenghty discussion. I'm looking
 into LLM-s and how they could be used for assisting in understanding reports.

I would like your opinion on the followi
ng idea I am exploring.

**Business Problem**

Our company got loads of reports generated, more than humanely possible t
o read (that's another discussion to have, but many of these are legally required, etc.). It would be really cool that f
or a given report, there would be a few sentences highlighting things.

A Report's (Reader's) Digest if you will. Things
 like

* 'It seems that compared to 2023 Q1, in 2023 Q2 our sales in department x has increased by 6.4% percent which is
 unusually high.'
* 'Our social network reach has been constantly falling on Facebook since 2023 February.'
* 'The avera
ge customer rating has been dropping for 5 consecutive days.'

**Understanding limits**

I get that LLM-s work with stri
ng data, so i'm guessing this isn't a straightforward thing to do. I'm also thinking that currently LLM-s won't figure o
ut insights on their own without guidance, thus questions should be agreed upon with business. (Altough self-propelled i
nsight finding would be a holy grail.) So with this in mind:

* probably business questions should be agreed upon
* prob
ably business shouldn't ask their questions directly from an LLM agent
* LLMs are not great at understanding tabular dat
a so this is not an obvious path ahead

**Brainstorming ideas**

Architecture-wise, I would be using Databricks (somethi
ng we actively work with), loading a report in as a delta table, then use a [LLM serving endpoint](https://learn.microso
ft.com/en-us/azure/databricks/machine-learning/model-serving/llm-optimized-model-serving). This is fairly new stuff comi
ng from them, it's still in public preview, but it can leverage LLama-2, keeps the data on databricks side so it seems s
ecure. (GDPR says hello.)

I found of course Pandas AI, that could be useful in combination with databricks somehow? I a
lso found this [fairly recent paper](https://arxiv.org/pdf/2401.04398v1.pdf), which talks about 'Evolving chain for tabl
e reasoning' on L[LamaIndex linkedin page](https://www.linkedin.com/posts/llamaindex_chain-of-table-use-llms-to-understa
nd-activity-7151983658596229120-fOo3?utm_source=share&utm_medium=member_desktop) that proposes a chain-of-table querying
 that looks interesting. It seems something closer to what LangChain is doing. Some [medium.com](https://medium.com) art
icles i found: [1](https://medium.com/@murtuza753/using-llama-2-0-faiss-and-langchain-for-question-answering-on-your-own
-data-682241488476) (this is about documents), [2](https://ameer-hakme.medium.com/unlocking-context-aware-insights-in-ta
bular-data-with-llms-and-langchain-fac1d33b5c6d) (this is about tabular data)

**A maybe functioning idea**

Okay so let
's see if the following makes sense, it is very highlever and very brainstormy:

1. Agree on with business what are the 
core questions they want to know from a report.
2. A LLama-2 model is setup in Databricks with serving endpoint
   1. ED
IT: so probably not Llama-2, but something along this line: [https://ameer-hakme.medium.com/unlocking-context-aware-insi
ghts-in-tabular-data-with-llms-and-langchain-fac1d33b5c6d](https://ameer-hakme.medium.com/unlocking-context-aware-insigh
ts-in-tabular-data-with-llms-and-langchain-fac1d33b5c6d) or PandasAI working with a databricks-stored llama2 (afaik that
 is supported)
3. A job runs daily:
   1. A report is ingested some magical data engineering-y way (my fellow data engin
eers know the pain)
   2. Prompt engineering: do some setup with the LLM agent (no clue yet what could be needed, but it
's a good guess that this is required - to prevent hallucations, etc).
   3. Prompts from business are loaded from some 
config file
   4. Results are stored in a separate delta table with following schema:
      1. Some primary key
      2.
 Some report identifier
      3. Business unit or stakeholder identifier
      4. Prompt
      5. Answer
      6. Timest
amp
   5. A SQL Warehouse endpoint is available and can be queried (by PowerBI for example that gets the latest answers.
)

**Problems and limitations**

How do we check if the answers are correct? Monitoring results is very blackbox-y at be
st. Ideally endusers needs to be trained on the purpose of the Report's Digest is to highlight stuff, but they have to v
erify it themselves. Getting feedback from endusers can be also complicated

**Conclusion in an ideal world**

Business 
managers like to look at PowerBI reports, and with this new feature they get an immediate highlight of the day, the top 
3 questions they always wanna know about comes with immedaite answers. 'We have an increased count of customer service t
ickets compared to previous week'. The manager looks at the graph and it seems to verify this statement.

Engineer team 
walks into the sunset with cool music in background

&#x200B;
```
---

     
 
all -  [ Langchain developers community For Free. ](https://www.reddit.com/r/Langchain_developers/comments/196m52z/langchain_developers_community_for_free/) , 2024-01-16-0910
```
The main point of this community rather than Langchain which already exists but have to create a separate for developers
 , who need help to learn and need assistance.

  
Feel Free to join and grow this community 

LangChain is an open-sour
ce framework and developer toolkit that helps developers get LLM applications from prototype to production. It is availa
ble for Python and Javascript at https://www.langchain.com/. 
```
---

     
 
all -  [ Seeking advice for developing a text-to-sql application ](https://www.reddit.com/r/OpenAI/comments/196lvge/seeking_advice_for_developing_a_texttosql/) , 2024-01-16-0910
```
Hi everyone,

I'm currently working on an internal project at my company. My goal is to develop a chat-based solution th
at allows business users to query the data warehouse (we're using BigQuery) through conversation. I’m trying to make thi
s project more production-ready, rather than being an experiment. I’m using LangChain with OpenAI currently and I could 
really use some inputs:

1. **Data Privacy and Access Control**: One of our top priorities is to ensure data privacy and
 appropriate access controls. Tagging a column like “revenue” to be private might work for simple scenarios, but real-li
fe scenarios are more complex, for example, how do you let users from the marketing department see the “email” column of
 customers, while others see redacted email? What about row-level security?
2. **Reviewing Generated SQL Queries**: Our 
data analysts have raised concerns about the difficulty in reviewing SQL statements generated by LLMs. These queries can
 be complex and hard to interpret. Any suggestions for making this process more manageable and transparent? Perhaps a SQ
L lineage tool to show the visibility of the SQL ?
3. **Semantic Integration with Database Tables and Columns**: Lastly,
 I'm wondering about the best way to integrate semantics into our database tables and columns. Seems that feeding dbt mo
dels (including description) directly to the LLM can work at first, but is there any solution that I can let business us
ers define these metadata themselves ? Does it mean I need to build an internal tool that allows users to update the met
adata ?

Any feedback, insights, or experiences you can share regarding these challenges are appreciated.

Thanks!
```
---

     
 
all -  [ Seeking advice for developing a text-to-sql application ](https://www.reddit.com/r/LangChain/comments/196lhv9/seeking_advice_for_developing_a_texttosql/) , 2024-01-16-0910
```
Hi everyone,

I'm currently working on an internal project at my company. My goal is to develop a chat-based solution th
at allows business users to query the data warehouse (we're using BigQuery) through conversation. I’m trying to make thi
s project more production-ready, rather than being an experiment. I’m using LangChain and followed guides in documentati
on & blogs (ex: [https://python.langchain.com/docs/use\_cases/qa\_structured/sql](https://python.langchain.com/docs/use_
cases/qa_structured/sql)) to achieve the first version and I could really use some inputs:

1. **Data Privacy and Access
 Control**: One of our top priorities is to ensure data privacy and appropriate access controls. Tagging a column like “
revenue” to be private might work for simple scenarios, but real-life scenarios are more complex, for example, how do yo
u let users from the marketing department see the “email” column of customers, while others see redacted email? What abo
ut row-level security?
2. **Reviewing Generated SQL Queries**: Our data analysts have raised concerns about the difficul
ty in reviewing SQL statements generated by LLMs. These queries can be complex and hard to interpret. Any suggestions fo
r making this process more manageable and transparent? Perhaps a SQL lineage tool to show the visibility of the SQL ?
3.
 **Semantic Integration with Database Tables and Columns**: Lastly, I'm wondering about the best way to integrate semant
ics into our database tables and columns. Seems that feeding dbt models (including description) directly to the LLM can 
work at first, but is there any solution that I can let business users define these metadata themselves ? Does it mean I
 need to build an internal tool that allows users to update the metadata ?

Any feedback, insights, or experiences you c
an share regarding these challenges are appreciated.

Thanks!
```
---

     
 
all -  [ Seeking advice for developing a text-to-sql application ](https://www.reddit.com/r/LLMDevs/comments/196ldg3/seeking_advice_for_developing_a_texttosql/) , 2024-01-16-0910
```
Hi everyone,

I'm currently working on an internal project at my company. My goal is to develop a chat-based solution th
at allows business users to query the data warehouse (we're using BigQuery) through conversation. I’m trying to make thi
s project more production-ready, rather than being an experiment. I’m using LangChain (also trying out LlamaIndex), and 
I could really use some inputs:

1. **Data Privacy and Access Control**: One of our top priorities is to ensure data pri
vacy and appropriate access controls. Tagging a column like “revenue” to be private might work for simple scenarios, but
 real-life scenarios are more complex, for example, how do you let users from the marketing department see the “email” c
olumn of customers, while others see redacted email? What about row-level security?
2. **Reviewing Generated SQL Queries
**: Our data analysts have raised concerns about the difficulty in reviewing SQL statements generated by LLMs. These que
ries can be complex and hard to interpret. Any suggestions for making this process more manageable and transparent? Perh
aps a SQL lineage tool to show the visibility of the SQL ?
3. **Semantic Integration with Database Tables and Columns**:
 Lastly, I'm wondering about the best way to integrate semantics into our database tables and columns. Seems that feedin
g dbt models (including description) directly to the LLM can work at first, but is there any solution that I can let bus
iness users define these metadata themselves ? Does it mean I need to build an internal tool that allows users to update
 the metadata ?

Any feedback, insights, or experiences you can share regarding these challenges are appreciated.

Thank
s!
```
---

     
 
all -  [ A Vision ](https://www.reddit.com/r/LangChain/comments/196lcjp/a_vision/) , 2024-01-16-0910
```
My employer is doing a Hackathon soon and the focus is on GenAI. Like most orgs, they’ve created a spin off LLM for empl
oyee use running on GPT-4 that we can use in our daily tasks (and hackathon practice). There’s a document upload feature
 where I’ve been providing context about the platform we support (microservices in FinTech) along with a small dataset o
f information related to successful processing of requests, time taken data, and application error log data for maybe a 
15 minute sample and would them prompt it with a question like “Customer XYZ reported some issues at 11:30am, was anythi
ng going on?”  I’d get a pretty decent response back where it would point out an increase in failed requests and some er
rors logged around that same time. 

My question is how do I expand upon this?

I’m still working on the DataBricks note
book that will pull this data in a consistent format based on the requested time and eventually stream this of some sort
. 

More so though, it’s the context needed to accurately answer needs applied each time I test a new snippet of data. T
hat lead me to vector databases, HuggingFace models, LangChain, and Faiss. It all feels very overwhelming to logically c
onnect these dots. 

Is there an ELI5 of how this would conceptually work regarding the data generated, the context, and
 answering the prompt?
```
---

     
 
all -  [ [Student], 5 year BS MS program 4th year student. Looking for Software eng/dev internships. ](https://www.reddit.com/r/EngineeringResumes/comments/1968k64/student_5_year_bs_ms_program_4th_year_student/) , 2024-01-16-0910
```
Hello, I am a 4th year student in a 5 year MS BS program, and I am looking for an software engineering/developer interns
hip in FAANG or any higher level tech company anywhere in the US and I am willing to relocate. I would like some advice 
as to what my resume is lacking, or needs to do better, any help is greatly appreciated. Thank you!

https://preview.red
d.it/0p7ge06xeccc1.jpg?width=850&format=pjpg&auto=webp&s=8ff44d3376bf0a3c13443a5442847b7c16193b06

 
```
---

     
 
all -  [ Why langchain focuses on OpenAI rather than local llm? ](https://www.reddit.com/r/LangChain/comments/1966yxv/why_langchain_focuses_on_openai_rather_than_local/) , 2024-01-16-0910
```
Sorry I am new to langchain. And I found all the examples are OpenAI. But I think the value of langchain is mainly on lo
cal llm. Otherwise, why not using GPTs? I’m very curious about it.
```
---

     
 
all -  [ Optimizing Text Embedding for Cohere AI ](https://www.reddit.com/r/LangChain/comments/195yneb/optimizing_text_embedding_for_cohere_ai/) , 2024-01-16-0910
```
I'm utilizing Cohere AI for a project, and I have a text file that I want to embed. While I'm aware that Langchain has c
hunking functions, I believe Tiktoken might be more effective. However, I'm unsure about how Tiktoken works or if it wou
ld be suitable for Cohere.
```
---

     
 
all -  [ Me pueden dar retro para mi CV, me gustaria aplicar a internships en la region al norte de México y  ](https://i.redd.it/ynci98h6k9cc1.jpeg) , 2024-01-16-0910
```

```
---

     
 
all -  [ LLM Assistant with function calling - Just a small test project I made ](https://www.reddit.com/r/LocalLLaMA/comments/195t9qi/llm_assistant_with_function_calling_just_a_small/) , 2024-01-16-0910
```
[https://github.com/Rivridis/LLM-Assistant](https://github.com/Rivridis/LLM-Assistant)

This is an attempt to make a LLM
 application that can call functions and search the internet, all without langchain or any complex setups. This is based
 purely on llama-cpp-python and can be run using any gguf models which uses the ChatML prompting format.

I used RAG for
 searching the internet, using DuckDuckGo search engine, and appending the search result to the system prompt. All other
 functions are called based on the example given in system prompt.

I even added a Gradio chat UI, and I shall find a wa
y to add stuff like uploading documents and searching from them (Maybe by using some vector database).

If anyone has an
y feature ideas or improvement to the code, feel free to let me know, as I plan to make this project even more feature r
ich, once I find a way to make the LLM choose multiple functions instead of the current one function at a time.
```
---

     
 
all -  [ How to implement RAG? ](https://www.reddit.com/r/LocalLLaMA/comments/195snd0/how_to_implement_rag/) , 2024-01-16-0910
```
I am making my own frontend, is there an easy way to add RAG functionality? I'm using Ooba for the backend, it's relativ
ely easy to use the API, but I can't seem to find anything similar for a RAG system. Possibly no langchain or docker.
```
---

     
 
all -  [ Mastering RAG App Embedding with Custom Models ](https://www.reddit.com/r/LangChain/comments/195rest/mastering_rag_app_embedding_with_custom_models/) , 2024-01-16-0910
```
Hey folks, 

I've been pondering the process of embedding in a RAG app using various models. When examining examples, I 
noticed that some models (the most popular ones) include their embeddings. However, if I want to perform embedding with 
a different foundation model or an instructive one, what's the procedure? Do I need to extract the truncated version of 
the LLM to create the embedding model, or is there a process I'm not familiar with? 
```
---

     
 
all -  [ Looking for resources to learn LLM Development ](https://www.reddit.com/r/LLMDevs/comments/195r8pg/looking_for_resources_to_learn_llm_development/) , 2024-01-16-0910
```
I'm an experienced senior software engineer who just hasn't touched LLMs before. My goal is to learn how to integrate an
 LLM into an application to do tasks like data analysis, leveraging data in the application alongside new inputs to maxi
mize the accuracy of the results. So far my research has led me to the following:

1. Store my data, or a limited replic
a of the important parts, in a vector database as embeddings. This makes it easier and more efficient to query for relev
ant data and feed to the LLM.

2. Everything needs to go into the prompt. Embeddings can help, but I need to feed everyt
hing to the LLM with detailed instructions.

3. The tooling around this is pretty mixed. For example, LangChain keeps co
ming up in my searches but there are so many conflicting opinions around it I'm hesitant to adopt it.

So anyway, I'm lo
oking for learning resources. I'm fine with it being lower level, Ie avoiding abstractions like LangChain and hand rolli
ng things. Long term higher abstractions are better, but for learning I can benefit from understanding the fundamental m
echanics.

Ideally I need to understand more about vector databases and embeddings so I can understand their true value 
beyond mere buzzwords. I'm sure there are plenty of pros and cons, which I need to understand to know when to leverage t
his tool.

Then of course how to feed embeddings to the LLM in an optimal way along with my prompts. I'm finding lots of
 good articles on prompt engineering, so that is good.

Lastly, the best free/super cheap LLMs to test with. For prod ap
ps you want the best, Ie GPT4 or the like. But for this, I'm learning. I care less about top-notch results and more abou
t saving my wallet while educating myself.

Thanks for reading this wall of text. Looking forward to any feedback and di
rection on educational resources. Thanks.
```
---

     
 
all -  [ Me podrian dar consejos sobre que deberia ponerle/cambiarle a mi CV quiero ver si se arman las inter ](https://www.reddit.com/r/taquerosprogramadores/comments/195hp64/me_podrian_dar_consejos_sobre_que_deberia/) , 2024-01-16-0910
```
&#x200B;

https://preview.redd.it/iuzi7vjuj5cc1.jpg?width=757&format=pjpg&auto=webp&s=8eb186844badcbd7194a10324af0ca6f52
36dbad
```
---

     
 
all -  [ Please critique my CV. About 200 apps and still no call. ](https://i.redd.it/atci47ypz4cc1.jpeg) , 2024-01-16-0910
```
Graduating in May and desperately looking for a gig as an international student. Kindda getting anxious now lol. Any fee
dback would be greatly appreciated!
```
---

     
 
all -  [ Show and Tell: What have you built with LLMs? ](https://www.reddit.com/r/LangChain/comments/1958znq/show_and_tell_what_have_you_built_with_llms/) , 2024-01-16-0910
```
Hello LLM enthusiasts! I'm eager to hear about the creative and innovative ways you've been using Large Language Models 
(LLMs) in your projects. Lang Chain, has been a game-changer in bringing these applications from the drawing board to re
al-world use. Have you developed something unique, solved a complex problem, or simply experimented with something fun? 
Let's inspire each other by sharing our experiences and discussing how Lang Chain has facilitated our journey with LLMs!

```
---

     
 
all -  [ Trying to solve for bad data ](https://www.reddit.com/r/LangChain/comments/1957t7r/trying_to_solve_for_bad_data/) , 2024-01-16-0910
```
Hi. I'm tasked with building a chatbot for work. We are an HR tech company. 

I'm using Retrieval QA, trying different c
hunking sizes, testing both Pinecone and Supabase for vector Retrieval. 

However, I'm of the opinion that our data suck
s. Our API docs have like 50 words per page at most, and there are maybe 30 pages. We have a lot of support tickets, lik
e 500, but only 20% have actual answers written out to the ticket reason. So I get maybe 20-50 words per useable ticket.
 Lastly, our community sourced internal documentation is fragmentation and inconsistently designed. 

I've engineered al
l the text into consistent structures. The purpose is Q/A, like 'If a user is complaining X isn't working in their dashb
oard, what might be the cause?'

But is there anything realistic I can do with this situation when the data is so low vo
lume and poor quality? Any technical approaches that don't require a manual documentation overhaul, that is. 

Thanks.
```
---

     
 
all -  [ Langchain with Hugging face models ](https://www.reddit.com/r/LangChain/comments/1954q8y/langchain_with_hugging_face_models/) , 2024-01-16-0910
```
I am new to langchain. Can someone please explain to me how to use hugging face models like Microsoft phi-2 with langcha
in? The official documentation talks about openAI and other inference API based LLMs but how about locally running model
s?
```
---

     
 
all -  [ Intro to LangChain - Full Documentation Overview ](https://youtu.be/dXP841pBcJw?si=V03bfGxR0E2DVOA8) , 2024-01-16-0910
```
Comprehensive LangChain Overview
```
---

     
 
MachineLearning -  [ [D] Are Custom LLM RAG apps going to become redundant? ](https://www.reddit.com/r/MachineLearning/comments/1929n4f/d_are_custom_llm_rag_apps_going_to_become/) , 2024-01-16-0910
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

     
 
MachineLearning -  [ [P] An open-source project for deploying local models ](https://www.reddit.com/r/MachineLearning/comments/18zkm5m/p_an_opensource_project_for_deploying_local_models/) , 2024-01-16-0910
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

     
 
MachineLearning -  [ [Project] Temporal Augmented Retrieval (TAR) - Dynamic RAG ](https://www.reddit.com/r/MachineLearning/comments/18uddmj/project_temporal_augmented_retrieval_tar_dynamic/) , 2024-01-16-0910
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

     
 
MachineLearning -  [ [R][P] Autogen + Langchain Tools + Local LLM doesn't work. ](https://www.reddit.com/r/MachineLearning/comments/18tex1j/rp_autogen_langchain_tools_local_llm_doesnt_work/) , 2024-01-16-0910
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

     
 
MachineLearning -  [ [P] Seeking Advice for Building a School Handbook Chatbot Using OpenAI and Vector Databases ](https://www.reddit.com/r/MachineLearning/comments/18rndcp/p_seeking_advice_for_building_a_school_handbook/) , 2024-01-16-0910
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

     
 
deeplearning -  [ [D] Unleashing the Power of Langchain with Wandb: Revolutionizing Topic Modeling and Evaluation ](https://www.reddit.com/r/deeplearning/comments/191mm83/d_unleashing_the_power_of_langchain_with_wandb/) , 2024-01-16-0910
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

     
 
deeplearning -  [ Unlocking the Power of Language: How LangChain Transforms Data Analysis and More ](https://www.reddit.com/r/deeplearning/comments/18l788y/unlocking_the_power_of_language_how_langchain/) , 2024-01-16-0910
```
Language models have revolutionized natural language processing (NLP), yet they grapple with limitations that impede the
ir full potential. Enter LangChain, a pioneering framework that transcends these constraints, fostering innovative langu
age-based applications. To comprehend LangChain’s significance, we must first grasp the limitations plaguing large langu
age models (LLMs).

link: [https://medium.com/ai-advances/unlocking-the-power-of-language-how-langchain-transforms-data-
analysis-and-more-3c4f327d520d](https://medium.com/ai-advances/unlocking-the-power-of-language-how-langchain-transforms-
data-analysis-and-more-3c4f327d520d) 
```
---

     
