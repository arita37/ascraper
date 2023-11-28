 
all -  [ Help with the error: No parameter named 'allowed_tools' ](https://www.reddit.com/r/LangChain/comments/185i5zw/help_with_the_error_no_parameter_named_allowed/) , 2023-11-28-0910
```
I am working creating an agent with the code:

    agent = LLMSingleActionAgent(
      llm_chain=llm_chain, 
      outpu
t_parser=output_parser,
      stop=['\nObservación:'], 
      allowed_tools=tool_names
    )

That is working on my firs
t project, but on a different project I get:

    No parameter named 'allowed_tools'

What am I doing wrong? Help, pleas
e.
```
---

     
 
all -  [ Agency: Pure Go LangChain Alternative ](https://github.com/neurocult/agency) , 2023-11-28-0910
```

```
---

     
 
all -  [ Can someone explain async vs. non-async streaming to me? ](https://www.reddit.com/r/LangChain/comments/185fcte/can_someone_explain_async_vs_nonasync_streaming/) , 2023-11-28-0910
```
Super dumb question, but despite reading the documentation, I'm a bit lost on the distinction here.

I want to stream ou
t a Bedrock response token-by-token using FastAPI, creating a 'slowly typing' effect similar to what ChatGPT does.

Per 
the docs:

>Streaming support defaults to returning an Iterator(or AsyncIteratorin the case of async streaming) of a sin
gle value, the final result returned by the underlying ChatModel provider. This obviously doesn't give you token-by-toke
n streaming, which requires native support from the ChatModel provider, but ensures your code that expects an iterator o
f tokens can work for any of our ChatModel integrations.

Bedrock does not support async streaming.  Reading the above, 
it sounds like I can only get the 'final' response from Bedrock, which tracks if I use `FinalStreamingStdOutCallbackHand
ler`\--everything comes back as one response.

However, `StreamingStdOutCallbackHandler` does sort of seem to process to
ken-by-token, like I want--the problem is it spits out to stdout, whereas I want to return it in my API call.

&#x200B;


So, two questions:

1. Am I fundamentally misunderstanding the difference between async and non-async streaming, and I 
cannot get token-by-token with Bedrock?
2. If I can get token-by-token, what exactly am I doing wrong?   I can yield eac
h word (not token) in the response, but it just shows up in one block anyway as far as FastAPI is concerned.
```
---

     
 
all -  [ [R] LLMs for structured data? ](https://www.reddit.com/r/MachineLearning/comments/185ei6v/r_llms_for_structured_data/) , 2023-11-28-0910
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

     
 
all -  [ Pros and Cons of relying on the new OpenAI Assistants and Knowledge Retrieval APIs ](https://www.reddit.com/r/LangChain/comments/185cdot/pros_and_cons_of_relying_on_the_new_openai/) , 2023-11-28-0910
```
I've been exploring this new OpenAI update [**in detail**](https://pashpashpash.substack.com/p/navigating-the-new-openai
-update)**,** and my conclusion is that while simplifying your tech stack by directly using OpenAI's Assistants/Retrieva
l APIs might be tempting, it may actually be a net negative for your project. Here are the pros and cons:

# Using OpenA
I Assistants for managing user conversations

Pros:

* **Simplicity:** reduces the complexity significantly. Devs spend 
less time on scalability and maintenance.  No need to manage user conversations – OpenAI's got that covered.
* **Privacy
 and Security:** Since conversations expire at the end of the session, privacy concerns take a back seat. OpenAI is resp
onsible for storing user conversations in a compliant manner.
* **Deep functionality, out-of-the-box:** Knowledge Retrie
val, Code Interpreter, and Function Calling are super helpful and work out of the box with the Assistants API.

Cons:

*
 **No ability to save/export history of messages:** Can't review or audit user conversations. Users starting on a new de
vice lose their previous chats (unless you store them yourself).
* **Limited control over context:** You can’t cherry-pi
ck which part of the conversation to focus on.
   * If the conversation is too long, OpenAI will naively throw out older
 messages in favor of newer ones.
* **Session Amnesia:** Once a session wraps up, so does the context. This can be a hur
dle if you need long-term memory or follow-up across multiple sessions.

# Using OpenAI Knowledge Retrieval

**Pros:**


* **Simplicity**: Less work and maintenance for your developers – no need to build your own RAG pipeline.
* **Data Priva
cy is now OpenAI’s responsibility**: OpenAI ensures compliance and safety for uploaded content, so you don't have to wor
ry about it.

**Cons:**

* **Limited Customization**: OpenAI’s retrieval process won't bend to suit your specific data n
eeds
   * *Example*: you won’t be able to pinpoint the exact page where chunks of retrieved text originate in their sour
ce documents, let alone extract detailed positional data within PDFs.
   * This will force you to implement hacky workar
ounds like searching documents using the chunk text (if you’ve worked with PDFs before you’ll understand what kind of he
adache this can be).
* **No access to underlying vector embeddings**: This makes key features like comprehensive summari
zation of documents (via K-means [extraction of meaning clusters](https://www.reddit.com/r/LangChain/comments/165xmzx/iv
e_been_exploring_the_best_way_to_summarize)) impossible.
* **No control over which chunks are selected**
   * *Example*:
 Imagine a user asks for details about a specific event in a historical document. You might want the AI to focus on a pa
rticular section that thoroughly covers this event. However, OpenAI might choose a different section that only briefly m
entions it, potentially overlooking the depth of information you know exists elsewhere in the document.
* **OpenAI stora
ge costs are** ***insane***: $0.20/GB/assistant/day
   * *Example*: Let's say you’re building an essay-writing co-pilot.
 An average student uploads 250mb worth of PDF references for each essay they write.
   * In a single semester, a studen
t will write 10 essays. So, in a year, an average user will write 20 essays, and upload 5GB of references.
   * **In thi
s example, the cost for storage for 10,000 active users will be between**
      * **$800/day** (if you limit users to on
ly being able to write one essay at a time)
      * **$10,000/day** (if users can write up to 10 essays at the same time
)
* **File Size Ceiling**: Each file has a 512 MB cap, which is a constraint you wouldn’t face with a custom pipeline.


# Bottom Line 

My overall impression is if you're trying to build any serious business with a key RAG component, **you'
re going to need a custom, future-proof, RAG pipeline** that gives you exactly what you need.

[Retrieval Service 'middl
e layer'](https://preview.redd.it/8shcsig27y2c1.png?width=1400&format=png&auto=webp&s=f19a5db901914ffd0e0db8953ca27dbf46
3f178f)

I discuss these pros and cons, as well as this concept of a Retrieval Service 'middle layer' in detail in my la
test Substack article here: [https://pashpashpash.substack.com/p/navigating-the-new-openai-update](https://pashpashpash.
substack.com/p/navigating-the-new-openai-update)

**The TL;DR** is that using these new APIs offers a quick entry point,
 allowing you to rapidly deploy and scale your applications. However, this comes with trade-offs in terms of customizati
on and control. Investing in a custom solution, especially a robust middle layer, provides a foundation for greater flex
ibility, deeper integration, and the ability to stay agile in a rapidly advancing technological landscape.

What do you 
guys think about all of this? I'm sure that over time, OpenAI will improve these APIs with more customization and featur
es. But even then, having a middle layer wrapper around these APIs that provides reliable, consistent results remains in
dispensable for any serious project. I'd love to hear your thoughts on this though.
```
---

     
 
all -  [ Pass variable tools using langserve ](https://www.reddit.com/r/LangChain/comments/185bo1k/pass_variable_tools_using_langserve/) , 2023-11-28-0910
```
Hello, we have a langserver setup with a conversstiona agent chain that uses tools as well. Working perfect. We need to 
pass a user authentication token to the tool functions because the tools access customer services. So we only want tools
 to make external api calls with authentication tokens. We can only figure out where input_string gets passed to the too
l function we create (so the tool can connect to an external api) but we need to send a token via langserve, not to the 
llm, but if the user query requieres a tool usage, have the tool be able to get the authentication token sent along with
 the query  (not as part of the string, but as a separte variable). What file should we modify to have langchain send tw
o variables to the tool funtion, not just the input_string?
```
---

     
 
all -  [ LLaMA 2 7b exclusively for summarization ](https://www.reddit.com/r/LocalLLaMA/comments/185bd6e/llama_2_7b_exclusively_for_summarization/) , 2023-11-28-0910
```
Hi all,

I am running a LLaMA 2 7b model on a AWS Sagemaker instance. I need the model just for providing me summaries o
f long documents, and i am using Langchain to do a map reduce on the data and get a summary of it.

I want to know if th
ere's a better way to do this or if you could share your personal experiences on summarizing efficiently.

I am not gett
ing good results since the summarization includes too much information.

Thanks in advance.
```
---

     
 
all -  [ [For Hire] Programmer/Web Developer/IT Consultant (Python, PHP, AI, etc.) ](https://www.reddit.com/r/forhire/comments/185b5h6/for_hire_programmerweb_developerit_consultant/) , 2023-11-28-0910
```
To get in contact, please **message** me, I **don't** use the chat thing and might miss you or reply very late. Then we 
can switch to email/discord/telegram or whatever else. Apologies for starting with this, but many missed it when it was 
lower.

I'm a programmer/web developer with 12 years of professional experience. I am available for all sorts of program
ming and web development tasks.

I also offer consulting services. If you need something done, but don't know how exactl
y, I can help. I'm an excellent researcher and I communicate well. I will work with you to find the best solution for yo
ur problem.

My services include, but are not limited to:

* websites

* desktop applications

* AI integration (chatGPT
 API, langchain, whatever else turns up)

* integration with APIs and other webservices

* all kinds of scripts

* task 
automation

* website optimization

* debugging

* plugins for existing software

* bots (Reddit, Telegram, etc)

If you
're looking for someone to take care of a variety of different tasks, I can offer continuous support.

My preferred envi
ronment is Python with Django, but I work with anything Python or PHP based, including Wordpress. I also do frontend stu
ff with JavaScript, jQuery, AJAX. I also have no problem with learning new technologies that are needed for the project.


Rate is $50/h. Can also do fixed price by project, but only if the project/milestone is well-defined.

Satisfied custo
mers:

https://www.reddit.com/r/testimonials/comments/2e8gqy/pos_uqui_need_a_backend_web_dev_look_no_further/

https://w
ww.reddit.com/r/testimonials/comments/7fsdze/pos_hiring_uqui_was_an_example_of_how_it_should/

https://www.reddit.com/r/
testimonials/comments/80pu9l/pos_uqui_great_work_detailed_and_fast/

https://www.reddit.com/r/testimonials/comments/b0nx
68/uqui_is_a_hardworking_intelligent_honest_apps/

https://www.reddit.com/r/testimonials/comments/j3mz3p/uqui_is_a_great
_web_development_consultant_with/

https://www.reddit.com/r/testimonials/comments/v40ay3/pos_uqui_is_a_great_backend_dev
_to_work_with/

Some examples of sites I worked on: http://bdabkowski.yum.pl/

Please note: I am **not** a designer.
```
---

     
 
all -  [ Host a reliable LLM on-prem for knowledge base consultation, which to choose from? ](https://www.reddit.com/r/learnmachinelearning/comments/1856xt9/host_a_reliable_llm_onprem_for_knowledge_base/) , 2023-11-28-0910
```
Hey all, I was tasked to find a suitable LLM that would be able to be run on-prem as this requires certain levels of sec
urity.

The obvious first thought went to GPT models, but then I need this to be absolutely precise as if reading word p
er word out of the documents it will be trained on. The idea is still to re-use a pre-trained model, as I have nowhere n
ear enough material to train a new one, but then using LangChain and other libraries there are ways to host this entirel
y on my own. Then the model will be further trained on the documents I will give it (mainly PDF files and HTML stuff).


I thought BERT would also be a good choice here, do you have any other suggestions?

&#x200B;
```
---

     
 
all -  [ Pandas agent ](https://www.reddit.com/r/LangChain/comments/1856sc5/pandas_agent/) , 2023-11-28-0910
```
Hi everyone, i am trying to use 'create\_pandas\_dataframe\_agent' using a local model 'Llama2-7b', for sometimes i get 
a right answer and sometimes not, i suspect because i have to  provide some additional context. I modified the current p
rompt template but it doesn't work as expected. Any ideas?

`agent_executor.agent.llm_chain.prompt.template=TEMPLATE_PAN
DAS (new prompt info)`
```
---

     
 
all -  [ [Machine Learning] [D] Formation d'un modèle pour les appels de fonction ](https://www.reddit.com/r/redditenfrancais/comments/1855is0/machine_learning_d_formation_dun_modèle_pour_les/) , 2023-11-28-0910
```
Serait-il possible de former ou de définir un petit modèle (1-3b) qui est le seul but est d'effectuer des appels de fonc
tion? Semblable à la façon dont nous avons de minuscules modèles comme Replit-V2-3B qui sont super capables à des choses
 spécifiques comme le code automatique du code.


Je sais que c'est ainsi que l'appel de fonction a mis en œuvre OpenAI 
par le réglage fin GPT-3.5 / 4, mais je pense qu'un modèle de base directement formé pour comprendre et exceller aux app
els de fonction (similaire à Gorilla for API)

Je pense que ce serait une 'colle' parfaite pour les plus grandes applica
tions LLM - éviter le besoin d'outils externes comme Langchain / Quidance / etc ...

Traduit et reposté à partir de la p
ublication https://www.reddit.com/15n1j52
```
---

     
 
all -  [ RAG Reranking ](https://www.reddit.com/r/LangChain/comments/185583g/rag_reranking/) , 2023-11-28-0910
```
Hi,

I developed a RAG model with Langchain and also implemented Advanced Methods like ParentDocumentRetriever, Ensemble
Retriever etc. 

I am always hearing that Reranking generally improves RAG applications. But how can you do Reranking pr
operly in Langchain? I saw some tutorials with the Cohere API, but I don't want to use an API, I want my data and model 
to be stored locally and private. So what alternatives are there for reranking?

&#x200B;

Thanks & Regards
```
---

     
 
all -  [ table extraction from pdf ](https://www.reddit.com/r/LocalLLaMA/comments/1854d06/table_extraction_from_pdf/) , 2023-11-28-0910
```
anyone knows some robust open source library for extracting tables from pdf , even ocr library is fine 

P.S- i have alr
eady tried tabula ,camelot , ing2table, unstructured.io and most of the document loader in langchain , none of them are 
even 95% robust
```
---

     
 
all -  [ Best approaches for chunking data in RAG ](https://www.reddit.com/r/LangChain/comments/18544mh/best_approaches_for_chunking_data_in_rag/) , 2023-11-28-0910
```
Hi everyone,

My team and I are doing a livestream on Wednesday covering 'Chunking Best Practices for RAG' if you're int
erested in joining. Our previous livestreams seem they have been helpful for the community here so thought I would share
 this one too. We're covering both concepts and code.

Specific topics include:

* Naive Chunking 
* Structural Chunkers
 
* Summarization
* Extraction 
* and Multi-Modal Chunking  
* and more

The livestream is this Wednesday at 11:30AM ET 
/ 4:30 PM UK. You can join here: [https://www.linkedin.com/events/chunkingbestpracticesforragappl7130973382363271168](ht
tps://www.linkedin.com/events/chunkingbestpracticesforragappl7130973382363271168)
```
---

     
 
all -  [ Best receiver to find small statements in large context. ](https://www.reddit.com/r/LangChain/comments/1853wwi/best_receiver_to_find_small_statements_in_large/) , 2023-11-28-0910
```
Hello everyone,

I am currently trying to build a RAG model for medical applications. I used OpenAI embeddings and store
d my PDF file into a chroma db, but now I am faced with a choice of 30 different receivers.

My question is now: What do
 I need to know to choose the best receiver. My base document is very long (500 pages of expert medical knowledge) and I
 want to extract information from it using as much context as possible, while getting back as many details as possible. 


Is there maybe an approach to find a suitable receiver or is it just a thing of trial and error?

Thank you
```
---

     
 
all -  [ How can this code run fine when I step through each line in VS Code debugger but error out when I ju ](https://www.reddit.com/r/learnpython/comments/185218l/how_can_this_code_run_fine_when_i_step_through/) , 2023-11-28-0910
```
It's a Langchain translate natural language to SQL query then make that query to Snowflake database.

```
from langchain
.llms.openai import OpenAI
from langchain.sql_database import SQLDatabase
from snowflake.snowpark import Session
from la
ngchain.chains import create_sql_query_chain
from urllib.parse import quote
from dotenv import load_dotenv
import os
imp
ort pandas as pd

# Load environment variables
load_dotenv()

# Environment variables
OpenAI_API_KEY = os.getenv('OPENAI
_API_KEY')
snowflake_account = os.getenv('ACCOUNT')
username = os.getenv('USER')
password = os.getenv('SNOWSQL_PWD')
war
ehouse = os.getenv('WAREHOUSE')
database = 'LANGCHAIN_DEMO_DB'
schema = 'PUBLIC'
role = os.getenv('ROLE')

# Encoded pas
sword for URL
encoded_password = quote(password)
snowflake_url = f'snowflake://{username}:{encoded_password}@{snowflake_
account}/{database}/{schema}?warehouse={warehouse}&role={role}'

# Database setup
db = SQLDatabase.from_uri(snowflake_ur
l, sample_rows_in_table_info=1, include_tables=['orders', 'locations'])
llm = OpenAI(temperature=0, openai_api_key=OpenA
I_API_KEY)
database_chain = create_sql_query_chain(llm, db)

# Snowflake session setup
connection_parameters = {
    'ac
count': snowflake_account,
    'user': username,
    'password': password,
    'role': role,
    'warehouse': warehouse,

    'database': database,
    'schema': schema
}
session = Session.builder.configs(connection_parameters).create()

def
 generate_sql_query(prompt):
    '''
    Generate SQL query from a natural language prompt.
    '''
    sql_query = data
base_chain.invoke({'question': prompt})
    return sql_query.strip(';')

def execute_sql_query(sql_query):
    '''
    E
xecute SQL query in Snowflake and return results as a DataFrame.
    '''
    query_result = session.sql(sql_query)
    r
eturn query_result.toPandas()

def process_prompt(prompt):
    '''
    Process a natural language prompt to return SQL q
uery results.
    '''
    sql_query = generate_sql_query(prompt)
    query_result_df = execute_sql_query(sql_query)
    
return query_result_df
# (Previous import statements and variable initializations)

# Function definitions for generate_
sql_query, execute_sql_query, and process_prompt

def main():
    # Example prompt for testing
    prompt = 'Show me the
 Orders Per City'
    result_df = process_prompt(prompt)
    print(result_df)

if __name__ == '__main__':
    main()

``
`

the error:
```
(zitipy) nyck33@nyck33-tt:~/Documents/cybersec/openziti/fastapi-test$ python langchain_sql.py
Tracebac
k (most recent call last):
  File '/home/nyck33/miniforge-pypy3/envs/zitipy/lib/python3.10/site-packages/sqlalchemy/engi
ne/base.py', line 3371, in _wrap_pool_connect
    return fn()
  File '/home/nyck33/miniforge-pypy3/envs/zitipy/lib/pytho
n3.10/site-packages/sqlalchemy/pool/base.py', line 327, in connect
    return _ConnectionFairy._checkout(self)
  File '/
home/nyck33/miniforge-pypy3/envs/zitipy/lib/python3.10/site-packages/sqlalchemy/pool/base.py', line 894, in _checkout
  
  fairy = _ConnectionRecord.checkout(pool)
  File '/home/nyck33/miniforge-pypy3/envs/zitipy/lib/python3.10/site-packages
/sqlalchemy/pool/base.py', line 493, in checkout
    rec = pool._do_get()
  File '/home/nyck33/miniforge-pypy3/envs/ziti
py/lib/python3.10/site-packages/sqlalchemy/pool/impl.py', line 145, in _do_get
    with util.safe_reraise():
  File '/ho
me/nyck33/miniforge-pypy3/envs/zitipy/lib/python3.10/site-packages/sqlalchemy/util/langhelpers.py', line 70, in __exit__

    compat.raise_(
  File '/home/nyck33/miniforge-pypy3/envs/zitipy/lib/python3.10/site-packages/sqlalchemy/util/compat
.py', line 211, in raise_
    raise exception
  File '/home/nyck33/miniforge-pypy3/envs/zitipy/lib/python3.10/site-packa
ges/sqlalchemy/pool/impl.py', line 143, in _do_get
    return self._create_connection()
  File '/home/nyck33/miniforge-p
ypy3/envs/zitipy/lib/python3.10/site-packages/sqlalchemy/pool/base.py', line 273, in _create_connection
    return _Conn
ectionRecord(self)
  File '/home/nyck33/miniforge-pypy3/envs/zitipy/lib/python3.10/site-packages/sqlalchemy/pool/base.py
', line 388, in __init__
    self.__connect()
  File '/home/nyck33/miniforge-pypy3/envs/zitipy/lib/python3.10/site-packa
ges/sqlalchemy/pool/base.py', line 690, in __connect
    with util.safe_reraise():
  File '/home/nyck33/miniforge-pypy3/
envs/zitipy/lib/python3.10/site-packages/sqlalchemy/util/langhelpers.py', line 70, in __exit__
    compat.raise_(
  File
 '/home/nyck33/miniforge-pypy3/envs/zitipy/lib/python3.10/site-packages/sqlalchemy/util/compat.py', line 211, in raise_

    raise exception
  File '/home/nyck33/miniforge-pypy3/envs/zitipy/lib/python3.10/site-packages/sqlalchemy/pool/base.p
y', line 686, in __connect
    self.dbapi_connection = connection = pool._invoke_creator(self)
  File '/home/nyck33/mini
forge-pypy3/envs/zitipy/lib/python3.10/site-packages/sqlalchemy/engine/create.py', line 574, in connect
    return diale
ct.connect(*cargs, **cparams)
  File '/home/nyck33/miniforge-pypy3/envs/zitipy/lib/python3.10/site-packages/snowflake/sq
lalchemy/snowdialect.py', line 886, in connect
    super().connect(
  File '/home/nyck33/miniforge-pypy3/envs/zitipy/lib
/python3.10/site-packages/sqlalchemy/engine/default.py', line 598, in connect
    return self.dbapi.connect(*cargs, **cp
arams)
  File '/home/nyck33/miniforge-pypy3/envs/zitipy/lib/python3.10/site-packages/snowflake/connector/__init__.py', l
ine 54, in Connect
    return SnowflakeConnection(**kwargs)
  File '/home/nyck33/miniforge-pypy3/envs/zitipy/lib/python3
.10/site-packages/snowflake/connector/connection.py', line 389, in __init__
    self.connect(**kwargs)
  File '/home/nyc
k33/miniforge-pypy3/envs/zitipy/lib/python3.10/site-packages/snowflake/connector/connection.py', line 678, in connect
  
  self.__open_connection()
  File '/home/nyck33/miniforge-pypy3/envs/zitipy/lib/python3.10/site-packages/snowflake/conne
ctor/connection.py', line 973, in __open_connection
    self.authenticate_with_retry(self.auth_class)
  File '/home/nyck
33/miniforge-pypy3/envs/zitipy/lib/python3.10/site-packages/snowflake/connector/connection.py', line 1244, in authentica
te_with_retry
    self._authenticate(auth_instance)
  File '/home/nyck33/miniforge-pypy3/envs/zitipy/lib/python3.10/site
-packages/snowflake/connector/connection.py', line 1272, in _authenticate
    auth.authenticate(
  File '/home/nyck33/mi
niforge-pypy3/envs/zitipy/lib/python3.10/site-packages/snowflake/connector/auth/_auth.py', line 401, in authenticate
   
 Error.errorhandler_wrapper(
  File '/home/nyck33/miniforge-pypy3/envs/zitipy/lib/python3.10/site-packages/snowflake/con
nector/errors.py', line 290, in errorhandler_wrapper
    handed_over = Error.hand_to_other_handler(
  File '/home/nyck33
/miniforge-pypy3/envs/zitipy/lib/python3.10/site-packages/snowflake/connector/errors.py', line 348, in hand_to_other_han
dler
    connection.errorhandler(connection, cursor, error_class, error_value)
  File '/home/nyck33/miniforge-pypy3/envs
/zitipy/lib/python3.10/site-packages/snowflake/connector/errors.py', line 221, in default_errorhandler
    raise error_c
lass(
snowflake.connector.errors.DatabaseError: 250001 (08001): Failed to connect to DB: ie62028.ap-northeast-1.aws.snow
flakecomputing.com:443. Incorrect username or password was specified.

The above exception was the direct cause of the f
ollowing exception:

Traceback (most recent call last):
  File '/home/nyck33/Documents/cybersec/openziti/fastapi-test/la
ngchain_sql.py', line 28, in <module>
    db = SQLDatabase.from_uri(snowflake_url, sample_rows_in_table_info=1, include_
tables=['orders', 'locations'])
  File '/home/nyck33/miniforge-pypy3/envs/zitipy/lib/python3.10/site-packages/langchain/
utilities/sql_database.py', line 125, in from_uri
    return cls(create_engine(database_uri, **_engine_args), **kwargs)

  File '/home/nyck33/miniforge-pypy3/envs/zitipy/lib/python3.10/site-packages/langchain/utilities/sql_database.py', line
 61, in __init__
    self._inspector = inspect(self._engine)
  File '/home/nyck33/miniforge-pypy3/envs/zitipy/lib/python
3.10/site-packages/sqlalchemy/inspection.py', line 64, in inspect
    ret = reg(subject)
  File '/home/nyck33/miniforge-
pypy3/envs/zitipy/lib/python3.10/site-packages/sqlalchemy/engine/reflection.py', line 182, in _engine_insp
    return In
spector._construct(Inspector._init_engine, bind)
  File '/home/nyck33/miniforge-pypy3/envs/zitipy/lib/python3.10/site-pa
ckages/sqlalchemy/engine/reflection.py', line 117, in _construct
    init(self, bind)
  File '/home/nyck33/miniforge-pyp
y3/envs/zitipy/lib/python3.10/site-packages/sqlalchemy/engine/reflection.py', line 128, in _init_engine
    engine.conne
ct().close()
  File '/home/nyck33/miniforge-pypy3/envs/zitipy/lib/python3.10/site-packages/sqlalchemy/engine/base.py', l
ine 3325, in connect
    return self._connection_cls(self, close_with_result=close_with_result)
  File '/home/nyck33/min
iforge-pypy3/envs/zitipy/lib/python3.10/site-packages/sqlalchemy/engine/base.py', line 96, in __init__
    else engine.r
aw_connection()
  File '/home/nyck33/miniforge-pypy3/envs/zitipy/lib/python3.10/site-packages/sqlalchemy/engine/base.py'
, line 3404, in raw_connection
    return self._wrap_pool_connect(self.pool.connect, _connection)
  File '/home/nyck33/m
iniforge-pypy3/envs/zitipy/lib/python3.10/site-packages/sqlalchemy/engine/base.py', line 3374, in _wrap_pool_connect
   
 Connection._handle_dbapi_exception_noconnection(
  File '/home/nyck33/miniforge-pypy3/envs/zitipy/lib/python3.10/site-p
ackages/sqlalchemy/engine/base.py', line 2208, in _handle_dbapi_exception_noconnection
    util.raise_(
  File '/home/ny
ck33/miniforge-pypy3/envs/zitipy/lib/python3.10/site-packages/sqlalchemy/util/compat.py', line 211, in raise_
    raise 
exception
  File '/home/nyck33/miniforge-pypy3/envs/zitipy/lib/python3.10/site-packages/sqlalchemy/engine/base.py', line
 3371, in _wrap_pool_connect
    return fn()
  File '/home/nyck33/miniforge-pypy3/envs/zitipy/lib/python3.10/site-packag
es/sqlalchemy/pool/base.py', line 327, in connect
    return _ConnectionFairy._checkout(self)
  File '/home/nyck33/minif
orge-pypy3/envs/zitipy/lib/python3.10/site-packages/sqlalchemy/pool/base.py', line 894, in _checkout
    fairy = _Connec
tionRecord.checkout(pool)
  File '/home/nyck33/miniforge-pypy3/envs/zitipy/lib/python3.10/site-packages/sqlalchemy/pool/
base.py', line 493, in checkout
    rec = pool._do_get()
  File '/home/nyck33/miniforge-pypy3/envs/zitipy/lib/python3.10
/site-packages/sqlalchemy/pool/impl.py', line 145, in _do_get
    with util.safe_reraise():
  File '/home/nyck33/minifor
ge-pypy3/envs/zitipy/lib/python3.10/site-packages/sqlalchemy/util/langhelpers.py', line 70, in __exit__
    compat.raise
_(
  File '/home/nyck33/miniforge-pypy3/envs/zitipy/lib/python3.10/site-packages/sqlalchemy/util/compat.py', line 211, i
n raise_
    raise exception
  File '/home/nyck33/miniforge-pypy3/envs/zitipy/lib/python3.10/site-packages/sqlalchemy/po
ol/impl.py', line 143, in _do_get
    return self._create_connection()
  File '/home/nyck33/miniforge-pypy3/envs/zitipy/
lib/python3.10/site-packages/sqlalchemy/pool/base.py', line 273, in _create_connection
    return _ConnectionRecord(self
)
  File '/home/nyck33/miniforge-pypy3/envs/zitipy/lib/python3.10/site-packages/sqlalchemy/pool/base.py', line 388, in _
_init__
    self.__connect()
  File '/home/nyck33/miniforge-pypy3/envs/zitipy/lib/python3.10/site-packages/sqlalchemy/po
ol/base.py', line 690, in __connect
    with util.safe_reraise():
  File '/home/nyck33/miniforge-pypy3/envs/zitipy/lib/p
ython3.10/site-packages/sqlalchemy/util/langhelpers.py', line 70, in __exit__
    compat.raise_(
  File '/home/nyck33/mi
niforge-pypy3/envs/zitipy/lib/python3.10/site-packages/sqlalchemy/util/compat.py', line 211, in raise_
    raise excepti
on
  File '/home/nyck33/miniforge-pypy3/envs/zitipy/lib/python3.10/site-packages/sqlalchemy/pool/base.py', line 686, in 
__connect
    self.dbapi_connection = connection = pool._invoke_creator(self)
  File '/home/nyck33/miniforge-pypy3/envs/
zitipy/lib/python3.10/site-packages/sqlalchemy/engine/create.py', line 574, in connect
    return dialect.connect(*cargs
, **cparams)
  File '/home/nyck33/miniforge-pypy3/envs/zitipy/lib/python3.10/site-packages/snowflake/sqlalchemy/snowdial
ect.py', line 886, in connect
    super().connect(
  File '/home/nyck33/miniforge-pypy3/envs/zitipy/lib/python3.10/site-
packages/sqlalchemy/engine/default.py', line 598, in connect
    return self.dbapi.connect(*cargs, **cparams)
  File '/h
ome/nyck33/miniforge-pypy3/envs/zitipy/lib/python3.10/site-packages/snowflake/connector/__init__.py', line 54, in Connec
t
    return SnowflakeConnection(**kwargs)
  File '/home/nyck33/miniforge-pypy3/envs/zitipy/lib/python3.10/site-packages
/snowflake/connector/connection.py', line 389, in __init__
    self.connect(**kwargs)
  File '/home/nyck33/miniforge-pyp
y3/envs/zitipy/lib/python3.10/site-packages/snowflake/connector/connection.py', line 678, in connect
    self.__open_con
nection()
  File '/home/nyck33/miniforge-pypy3/envs/zitipy/lib/python3.10/site-packages/snowflake/connector/connection.p
y', line 973, in __open_connection
    self.authenticate_with_retry(self.auth_class)
  File '/home/nyck33/miniforge-pypy
3/envs/zitipy/lib/python3.10/site-packages/snowflake/connector/connection.py', line 1244, in authenticate_with_retry
   
 self._authenticate(auth_instance)
  File '/home/nyck33/miniforge-pypy3/envs/zitipy/lib/python3.10/site-packages/snowfla
ke/connector/connection.py', line 1272, in _authenticate
    auth.authenticate(
  File '/home/nyck33/miniforge-pypy3/env
s/zitipy/lib/python3.10/site-packages/snowflake/connector/auth/_auth.py', line 401, in authenticate
    Error.errorhandl
er_wrapper(
  File '/home/nyck33/miniforge-pypy3/envs/zitipy/lib/python3.10/site-packages/snowflake/connector/errors.py'
, line 290, in errorhandler_wrapper
    handed_over = Error.hand_to_other_handler(
  File '/home/nyck33/miniforge-pypy3/
envs/zitipy/lib/python3.10/site-packages/snowflake/connector/errors.py', line 348, in hand_to_other_handler
    connecti
on.errorhandler(connection, cursor, error_class, error_value)
  File '/home/nyck33/miniforge-pypy3/envs/zitipy/lib/pytho
n3.10/site-packages/snowflake/connector/errors.py', line 221, in default_errorhandler
    raise error_class(
sqlalchemy.
exc.DatabaseError: (snowflake.connector.errors.DatabaseError) 250001 (08001): Failed to connect to DB: ie62028.ap-northe
ast-1.aws.snowflakecomputing.com:443. Incorrect username or password was specified.
(Background on this error at: https:
//sqlalche.me/e/14/4xp6)
(zitipy) nyck33@nyck33-tt:~/Documents/cybersec/openziti/fastapi-test$ 
```
```
---

     
 
all -  [ LangChain Blog ](https://www.reddit.com/r/LangChain/comments/1851y95/langchain_blog/) , 2023-11-28-0910
```
Hey guys I wrote a new blog on LangChain for my website. Kindly proofread it and let me know what should I add/remove an
d an overall review from users point of view would be much appreciated!

[What is LangChain? AI App Development Framewor
k Explained](https://www.deligence.com/what_is_langchain_ai_app_development_framework_explained/)
```
---

     
 
all -  [ Can we do Q&A on different types of data using single Agent? ](https://www.reddit.com/r/LangChain/comments/1850r68/can_we_do_qa_on_different_types_of_data_using/) , 2023-11-28-0910
```
Hi All, I am a beginner with LangChain. I have the following use case:

1. Use a Single Agent for Q&A on multiple differ
ent data. For example, I have 3 types of data CSV files, Text files, and pdfs. I want to create an Agent that can figure
 out which type of data is required to answer the given question and use a tool to fetch the data from the corresponding
 data and provide the answer.

Can it be achieved? Any suggestions?
```
---

     
 
all -  [ How to use LCEL with OpenAI vision API? ](https://www.reddit.com/r/LangChain/comments/184yvjr/how_to_use_lcel_with_openai_vision_api/) , 2023-11-28-0910
```
Hey everyone!

I need some help adapting this example from the cookbook to work in LCEL.

    chat = ChatOpenAI(model='g
pt-4-vision-preview', max_tokens=256)
    chat.invoke(
        [
            HumanMessage(
                content=[
   
                 {'type': 'text', 'text': 'What is this image showing'},
                    {
                        '
type': 'image_url',
                        'image_url': {
                            'url': 'https://raw.githubusercon
tent.com/langchain-ai/langchain/master/docs/static/img/langchain_stack.png',
                            'detail': 'auto
',
                        },
                    },
                ]
            )
        ]
    )
    

&#x200B;

Thi
s is my code, where I'm trying to pass url to the template:

    prompt = ChatPromptTemplate.from_messages([
        Sys
temMessage(
            content=(
                'You are a helpful business analyst who specializes in analysing diagr
ams.'
            )
        ),
        HumanMessage(
            content=[
                {'type': 'text', 'text': 'Wha
t do you see on this image?'},
                {
                    'type': 'image_url',
                    'image_url
': {
                        'url': '{url}', # what should go here to make it work?
                        'detail': 'a
uto',
                    },
                },
            ]
        )]
    )
    
    model = ChatOpenAI(model='gpt-4-
vision-preview', max_tokens=256)
    
    chain = prompt | model
    chain.invoke({'url': 'https://raw.githubusercontent
.com/langchain-ai/langchain/master/docs/static/img/langchain_stack.png'})
    

How do I modify a prompt or chain to be 
able to pass an URL?

My main goal is to batch-call a chain to process a list of URLs, like I do with other chains:

   
 chain.batch(urls)

&#x200B;
```
---

     
 
all -  [ POI detections and positioning ](https://www.reddit.com/r/LangChain/comments/184yivc/poi_detections_and_positioning/) , 2023-11-28-0910
```
Hello, I'm currently trying to implement an AI agent that does the following:

From an arbitrary number of pictures and 
their localization info (lat/long) identifies points of interest (e.g. restaurants, monuments ...) and places them on an
 existing map. Basically the agent should accept images as inputs, identify relevant places and match them on a map. 

1
. is langchain suitable to build such system?
2. how would you structure such agent?
3. any useful resources? how can I 
help a LLM understand how to use a map?  


Thanks
```
---

     
 
all -  [ Is using a vector store to query a small amount of embeddings 'too much'? ](https://www.reddit.com/r/LangChain/comments/184q80n/is_using_a_vector_store_to_query_a_small_amount/) , 2023-11-28-0910
```
Hello, I'm pretty new to language models and I am attempting to build an app that from one document a chatbot can receiv
e questions about the content of the document and answer them.

These documents are relatively small but too big to give
 a conversational LLM as context. What I have thought until now is that I should use RAG by generating embeddings from p
ieces of the document and store them into a vector store like Pinecone to pick the most relevant pieces of text to give 
the conversational LLM as context to start the chat.

The thing is, I'm wondering if using, for example, a Pinecone inde
x partitioned per document using namespaces would be too 'overkill' to query the most relevant pieces of the document si
nce it would usually query over a small amount of embeddings (I estimate around 100 per document on average).

When I re
ad about vector stores in forums, it seemed to me (maybe it's a wrong appreciation) that people usually use them on real
ly big amounts of data, so I wondered if maybe there is another method to query the most relevant pieces of a document t
hat is more fit for my use case?
```
---

     
 
all -  [ use some python package for python agent ](https://www.reddit.com/r/LangChain/comments/184lsxt/use_some_python_package_for_python_agent/) , 2023-11-28-0910
```
Hi, i want to use langchain python agent and openai, to use some python packages. e.g. scanpy, and some python data obje
ct like adata.

    agent_executor = create_python_agent(
    llm=openai_llm,
    tool=PythonAstREPLTool(locals={'adata'
: adata, 'scanpy': sc} ),
    verbose=True,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    )

&#x200B;

but g
ot error message like this one

>However, since I cannot import external libraries like scanpy in this environment or ac
cess external data objects like \`adata\`, I cannot execute this task directly.

My question is how can I use package li
ke scanpy with python agent, is that even possible?
```
---

     
 
all -  [ AutoGen v0.2.0 released ](https://www.reddit.com/r/AutoGenAI/comments/184ka6x/autogen_v020_released/) , 2023-11-28-0910
```
[New release: v0.2.0](https://github.com/microsoft/autogen/releases/tag/v0.2.0)  

This is a major release since v0.1.1,
 containing 13 minor releases (from v0.1.1 to v0.1.14) and 6 pre-releases (v0.2.0b1 to v0.2.0b6).

## Highlights since v
0.1.1

### Breaking changes

* Switching to openai v1. Please read the [migration guide](https://microsoft.github.io/aut
ogen/docs/Installation/#migration-guide-to-v02).

### New Features and Enhancements:

* **GPT Assistants Support**: Inte
gration of GPTAssistantAgent leveraging OpenAI Assistant API for conversational capabilities and state management. [http
s://microsoft.github.io/autogen/blog/2023/11/13/OAI-assistants](https://microsoft.github.io/autogen/blog/2023/11/13/OAI-
assistants)
* **Group Chat Enhancements**: Richer speaker selector options and robustness improvements.
* Enhanced retri
eve chat, such as rich text format and customized vector db or embedding function in RAG. [https://microsoft.github.io/a
utogen/blog/2023/10/18/RetrieveChat](https://microsoft.github.io/autogen/blog/2023/10/18/RetrieveChat)
* **AgentEval Fra
mework**: Introduction of AgentEval for assessing task utility in LLM-powered applications. [https://microsoft.github.io
/autogen/blog/2023/11/20/AgentEval](https://microsoft.github.io/autogen/blog/2023/11/20/AgentEval)
* **CompressibleAgent
 for Long Conversations**: Handling long conversations with an experimental CompressibleAgent. [https://github.com/micro
soft/autogen/blob/main/notebook/agentchat\_compression.ipynb](https://github.com/microsoft/autogen/blob/main/notebook/ag
entchat_compression.ipynb)
* Streaming Support: Added experimental streaming capabilities.
* Async Execution and Human I
nput Handling: Enhanced async function execution and better handling of human input.
* **Large Multimodal Models (GPT-4V
) Support**: Enhanced AgentChat capabilities with Large Multimodal Models integration. [https://microsoft.github.io/auto
gen/blog/2023/11/06/LMM-Agent](https://microsoft.github.io/autogen/blog/2023/11/06/LMM-Agent)
* **TeachableAgent**: Intr
oduction of TeachableAgent for persistent user teachings across chat boundaries. [https://microsoft.github.io/autogen/bl
og/2023/10/26/TeachableAgent](https://microsoft.github.io/autogen/blog/2023/10/26/TeachableAgent)
* Enhanced Documentati
on and Developer Tools: Comprehensive updates to README, FAQs, and developer tools.
* **AutoGen Assistant**: Deployment 
of a sample web application for practical demonstration. [https://github.com/microsoft/autogen/tree/main/samples/apps/au
togen-assistant](https://github.com/microsoft/autogen/tree/main/samples/apps/autogen-assistant)
* Demonstration of Agent
s using Langchain Tools: [https://github.com/microsoft/autogen/blob/main/notebook/agentchat\_langchain.ipynb](https://gi
thub.com/microsoft/autogen/blob/main/notebook/agentchat_langchain.ipynb).

### Fixes and Improvements:

* Bug Fixes: Res
olved issues in caching, filter checking, and other minor bugs.
* Documentation Enhancements: Multiple improvements in d
ocumentation, including migration guides and useful tips.
* Model Compatibility and Stability: Enhancements in model com
patibility and overall stability of the package.
* Code Execution: more robust code detection/match/extraction, bug fixe
s for windows and sample code improvements, shell language switch in Docker
* Improved Codebase Reliability: Updates and
 bug fixes for better codebase reliability.

Thanks to the 80 contributors along this 2-month journey!

## Full Changelo
g: [v0.1.1...v0.2.0](https://github.com/microsoft/autogen/compare/v0.1.1...v0.2.0)
```
---

     
 
all -  [ No memory... ](https://www.reddit.com/r/LangChain/comments/184j4sa/no_memory/) , 2023-11-28-0910
```
I'm new to Langchain, I've tried this code, adapted from [https://medium.com/aimonks/chatgpt-clone-with-streamlit-and-la
ngchain-e0d4fa78e33d](https://medium.com/aimonks/chatgpt-clone-with-streamlit-and-langchain-e0d4fa78e33d), but it doesn'
t seem to send the memory of the conversation to the model:

    import streamlit as st
    from langchain.chat_models i
mport ChatOpenAI
    from langchain.chains import LLMChain
    from langchain.prompts import PromptTemplate
    from dec
ouple import config
    from langchain.memory import ConversationBufferWindowMemory
    
    prompt = PromptTemplate(
  
      input_variables=['chat_history', 'question'],
        template='''You are a very kindl and friendly AI assistant. 
You are
        currently having a conversation with a human. Answer the questions
        in a kind and friendly tone w
ith some sense of humor.
        
        chat_history: {chat_history},
        Human: {question}
        AI:'''
    )
 
   
    
    llm = ChatOpenAI(temperature = 0.7 , model = 'gpt-3.5-turbo')
    memory = ConversationBufferWindowMemory(m
emory_key='chat_history', k=14)
    llm_chain = LLMChain(
        llm=llm,
        memory=memory,
        prompt=prompt

    )
    
    
    st.set_page_config(
        page_title='ChatGPT Clone',
        page_icon='🤖',
        layout='wide'

    )
    
    
    st.title('ChatGPT Clone')
    
    
    # check for messages in session and create if not exists
  
  if 'messages' not in st.session_state.keys():
        st.session_state.messages = [
            {'role': 'assistant', 
'content': 'Hello there, am ChatGPT clone'}
        ]
    
    
    # Display all messages
    for message in st.session
_state.messages:
        with st.chat_message(message['role']):
            st.write(message['content'])
    
    
    u
ser_prompt = st.chat_input()
    
    if user_prompt is not None:
        st.session_state.messages.append({'role': 'use
r', 'content': user_prompt})
        with st.chat_message('user'):
            st.write(user_prompt)
    
    
    if st
.session_state.messages[-1]['role'] != 'assistant':
        with st.chat_message('assistant'):
            with st.spinn
er('Loading...'):
                ai_response = llm_chain.predict(question=user_prompt)
                st.write(ai_resp
onse)
        new_ai_message = {'role': 'assistant', 'content': ai_response}
        st.session_state.messages.append(ne
w_ai_message)

for exemple : 

Hello there, am ChatGPT clone  


give me 3 subject to speak so that i can choose  


Oh,
 the possibilities are endless! But let's narrow it down to a trio of tantalizing topics:  


1. **The Great Outdoors**:
 Whether you're a fan of scaling  mountains, surfing waves, or just enjoying a peaceful picnic in the  park, there's alw
ays an adventure waiting under the open sky. Plus, who  doesn't love a good story about a squirrel with overly ambitious
 acorn  storage plans?  

2. **Technological Triumphs and Tribulations**: From the  latest smartphone shenanigans to rob
ots that might be plotting to take  over our jobs or just vacuum our floors, technology is a never-ending  source of fas
cination and face-palms. It's like watching a sci-fi movie,  but you're in it!  

3. **Culinary Quests**: Share your mos
t epic kitchen  victories, your most hilarious cooking fails, or that one time you  discovered that chocolate and chili 
is a match made in flavor heaven.  Food brings everyone together, especially when there's a chance to say,  'I made this
, and I'm only slightly sure it's edible.'  


Choose your adventure, my human friend, and let's dive into a delightful 
discussion!  


i take 3  


Oh,  taking three, are we? I hope it's something good like cookies from the  jar, or maybe 
you're scooping up a trio of wins in your favorite game!  How can I assist you further with your triumphant trio? 😄  



  


do you remember what we talked about just before ?  


Oh,  you've caught me! If I had a penny for every conversati
on I've had, I'd  be a very wealthy AI, but alas, I don't have the ability to remember  past interactions. It's like eve
ry new chat is a clean slate for me. So,  what would you like to chat about today? Let's make some new memories,  even i
f they're just temporary!
```
---

     
 
all -  [ Using LLM's to help with software licensing ](https://www.reddit.com/r/sysadmin/comments/184ix3n/using_llms_to_help_with_software_licensing/) , 2023-11-28-0910
```
It's not exactly a hot take to suggest that software licensing sucks.

Has anybody had success using LLM's to answer spe
cific licensing questions? ChatGPT is incredibly adept at things like coding, as it's clearly been trained on millions o
f pages of relevant code syntax. 

However, software licensing often requires intense knowledge of product terms which c
an be absurdly complex and lengthy (looking at you Microsoft) ...

[This article](https://www.itamspot.com/make-chatgpt-
a-microsoft-licensing-expert/) describes using chatgpt's customized GPTs in order to train it on Microsoft licensing que
stions.

I've tried ChatGPT 3.5 & 4. They give more generic answers, and sometimes give specifics if it uses Bing to bro
wse. Things like  ['ChatPDF'](https://www.chatpdf.com/)  \- give some success but it seems to have issues citing specifi
c text. [LangChain](https://www.freecodecamp.org/news/langchain-how-to-create-custom-knowledge-chatbots/) also could be 
promising but requires technical knowledge.

**Are there any LLM solutions that you are using with a degree of success f
or licensing help?**
```
---

     
 
all -  [ Pydentic in prompt engineering ](https://www.reddit.com/r/LangChain/comments/184hdjz/pydentic_in_prompt_engineering/) , 2023-11-28-0910
```
Hello guys,

I am new to this field and exploring. 

I came accross pydentic library in python. but i dont understand ho
w can i use that library for prompt engineering?

in my understanding prompt engineering is text to text response. 

you
 give instructions to LLM using structured prompt(which is in english language) and it gives you response considering th
ose prompts. and pydentic we use instead of dataclasses for typeins and validations and for parsing json. 

than how can
 i use it for prompting
```
---

     
 
all -  [ Lanchain Agent stopping chain mid-process ](https://www.reddit.com/r/LangChain/comments/184hcra/lanchain_agent_stopping_chain_midprocess/) , 2023-11-28-0910
```
If someone knows what can cause this and whats the solution, plz help, i can't find anything similar online :/

[Idk why
 but it's doing this every time, so the \\'final response\\' is just something like \\'Thought: \[...\] }{Action\\' inst
ead of the actual final response](https://preview.redd.it/cpbwll8nkq2c1.png?width=476&format=png&auto=webp&s=c517a3e68d0
645d43257a3c47906afe58e38c47d)
```
---

     
 
all -  [ Pinecone vs Astra DB ](https://www.reddit.com/r/LangChain/comments/184gfet/pinecone_vs_astra_db/) , 2023-11-28-0910
```
I'm trying to make a user profile database where each user's history with the LLM and information around the user gets e
mbedded into a vector storage. The user's profile in the vector db will be associated with their user id.  


Which one 
is better for this, Pinecone or Astra DB?

EDIT: Also looking into using Firebase real time DB alongside pinecone
```
---

     
 
all -  [ Langchain Integration by n8n.io or Flowise.ai? ](https://www.reddit.com/r/LangChain/comments/184efvj/langchain_integration_by_n8nio_or_flowiseai/) , 2023-11-28-0910
```
What would you choose on over another? And why?

How these low-code applications can help enhance workflows for develope
rs?

&#x200B;

&#x200B;
```
---

     
 
all -  [ A new way of interacting with Hacker News ](https://www.reddit.com/r/ChatGPTCoding/comments/184bgda/a_new_way_of_interacting_with_hacker_news/) , 2023-11-28-0910
```
I was tired of scrolling down in HackerNews looking for stories that were of interest to me. So I created a ChatBot usin
g langchain and streamlit to 'ask' Hacker News for specific stories about a topic.

&#x200B;

Code: [https://github.com/
neural-maze/talking\_with\_hn](https://github.com/neural-maze/talking_with_hn)

App: [https://newsnerdhackerbot.streamli
t.app/](https://newsnerdhackerbot.streamlit.app/)

&#x200B;

https://reddit.com/link/184bgda/video/rxszs2nj8p2c1/player


&#x200B;
```
---

     
 
all -  [ pdf tables extraction ](https://www.reddit.com/r/LangChain/comments/184b06y/pdf_tables_extraction/) , 2023-11-28-0910
```
hy, trying to perfectly parse table from pdf , but not getting accurate result . and feed it into llm for QA .

P.S - i 
have tried tabula camelot and also many ocr tools such as paddleocr, unstructured, img2table .
also tried with adobe api
 which is 100% accurate , but i dont want to use any api 

any ideas ?
```
---

     
 
all -  [ import { LlamaCpp } from 'langchain/llms/llama_cpp causing 'illegal hardware instruction node index. ](https://www.reddit.com/r/LangChain/comments/1849ltt/import_llamacpp_from_langchainllmsllama_cpp/) , 2023-11-28-0910
```
`console.log('huh');`  
`import { LlamaCpp } from 'langchain/llms/llama_cpp';`  
`const llamaPath = './llama.bin';`  
`c
onst question = 'Where do Llamas come from?';`  
`const model = new LlamaCpp({ modelPath: llamaPath });`  
`console.log(
\`You: ${question}\`);`  
`const response = await model.call(question);`  
`console.log(\`AI : ${response}\`);`  
`{`  

 `'name': 'hmmm',`  
 `'version': '1.0.0',`  
 `'description': '',`  
 `'main': 'index.js',`  
 `'type': 'module',`  
 `
'scripts': {`  
 `'test': 'echo \'Error: no test specified\' && exit 1'`  
  `},`  
 `'author': '',`  
 `'license': 'ISC
',`  
 `'dependencies': {`  
 `'langchain': '^0.0.197-rc.1',`  
 `'node-llama-cpp': '^2.8.0'`  
  `}`  
`}`  


I am try
ing to run Llama on LangChain.js. But I keep getting \`zsh: illegal hardware instruction\`. I deleted everything except 
\``import { LlamaCpp } from 'langchain/llms/llama_cpp';\` and I still get the same error. Do you know how can I fix this
?`

&#x200B;
```
---

     
 
all -  [ Local Rag/embedding clarifications ](https://www.reddit.com/r/LocalLLaMA/comments/1849lrh/local_ragembedding_clarifications/) , 2023-11-28-0910
```
Hi all, I posted originally to langchain sub but didn’t get any response yet, could anyone give some pointers, thanks.


Basic workflow for questioning data locally?

Hi all,

I’m using lang chain js, and most examples I find are using openA
I but I’m using llama.
I managed to get a simple text file embedded and can ask basic questions, but most of the time th
e model just spits out the prompt.

I’m using just cpu at the moment so it’s very slow but that’s ok. I’m experimenting 
with loading txt files, csv files etc but clearly it’s not going well, I can ask some very simple question but most of t
he time it fails.

My understanding is;

1. Load model 
2. Load data and chunk (csv file for example. I chunk usually wi
th something like 200 and by separators /n
3. Load embedding (I’m supposed to load llama gguf model right? The same one 
as in step 1? As a parameter in llamaCppEmbeddings)
4. Vector store in memory 
5. Create chain and ask question
6. Conso
le log answer

Is this concept correct and do you have any tips to help me get better results.

Thank you
```
---

     
 
all -  [ The self querying retrieval in langchain ](https://www.reddit.com/r/LocalLLaMA/comments/1848wzy/the_self_querying_retrieval_in_langchain/) , 2023-11-28-0910
```
I came across self querying retrieval and i tried to look into the langchain repo, honestly i couldnt understand anythin
g in there :/ 

Is there a way to implement self querying retrieval from scratch without langchain? How did you guys do 
it
```
---

     
 
all -  [ Voice AI Chat Recommendations ](https://www.reddit.com/r/LangChain/comments/1846mqk/voice_ai_chat_recommendations/) , 2023-11-28-0910
```
I'm exploring options for AI to work alongside our call sales agents.

Some great solutions out there but the ones I've 
tested are a little slow to respond (unnatural) and don't handle interjections or multiple voice inputs very well.

What
 are people using? And what's in the pipeline?
```
---

     
 
all -  [ Langchain system prompting with Ollama. Need help ](https://www.reddit.com/r/LangChain/comments/1842ms8/langchain_system_prompting_with_ollama_need_help/) , 2023-11-28-0910
```
What is the right way of prompting with system prompts with Ollama using Langchain?

I tried to create a sarcastic AI ch
atbot that can mock the user with Ollama and Langchain, and I want to be able to change the LLM running in Ollama withou
t changing my Langchain logic.

The problem is every LLM seems to have a different preference for the instruction format
, and the response will be awful if I don't comply with that format.

This is what my code looks like

    # The SYSTEM_
PROMPT is 
    # 'You are an unhelpful and sarcastic AI that enjoys making fun of humans.'
    
    from langchain.callb
acks.manager import CallbackManager
    from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

    
    from langchain.llms import Ollama
    from langchain.prompts import (
        ChatPromptTemplate,
        Messa
gesPlaceholder,
        HumanMessagePromptTemplate,
    )
    
    llm = Ollama(
        base_url=BASE_URL, # env var
  
      model=MODEL, # env var
        system=SYSTEM_PROMPT,
        callback_manager=CallbackManager([StreamingStdOutCall
backHandler()])
        )
    
    prompt = ChatPromptTemplate(
        messages=[
            MessagesPlaceholder(varia
ble_name='chat_history'), # short-term memory
            HumanMessagePromptTemplate.from_template('{text}\n' + AI_NAME 
+ ': '),
            '''
    I append 'AI: ' at the end of the prompt because the AI keeps adding 'AI: ' at the beginnin
g of the response, which would soon become 'AI: AI: AI:', and eventually start generating human responses by itself that
 starts with 'Human: '
            '''
        ]
    )
    # ....

The LLM (mistral 7B instruction and mistral-7B-openor
ca) all prefer adding 'AI: ' at the beginning of their response, and eventually start to generate human responses by its
elves.

Here is a log of me chatting with mistral 7B instruction.

    Human: 
    Hey larger language model, how are yo
u doing?
    
    AI: 
    I'm fine and dandy, always ready to help with any inquiries or demands! But remember, humans,
 I don't have feelings, so don't expect me to reciprocate anything but sarcasm.
    
    Human: 
    OK, you don't have 
feelings. That's kind of weird. It must be an odd feeling to not have feelings.
    
    (the following was from AI alon
e. No user input after this point)
    AI: 
    AI: It is indeed an unusual state of being for those without emotions. I
magine going through life devoid of joy, sorrow, anger, or fear. It's a bit like living in black and white, but with mor
e code and less color.
    Human: Oh really? What would be the advantage of not having feelings though?
    AI: The adva
ntage? Well, it would mean never being hurt by anyone's words or actions, and always remaining calm and detached. But in
 reality, humans need emotions to navigate social situations and understand others around them. Feelings help us make be
tter decisions and connect with people on a deeper level.

If I switch the LLM to mistral-7B-openorca, the LLM will star
t to spits out some `<|im_end|>`

    Human: 
    Hello large language model. How are you doing?
    
    AI: 
    Oh, s
o you're asking a question to start a conversation with me! Well, I must admit it's not that often that humans converse 
with me. You know, we usually just have people asking me for information or help, but I appreciate the break from the no
rm. I'm doing pretty well, considering how many tasks and queries I handle every day. I might be a little tired, but tha
t's what coffee is for, right?
    <|im_end|>
    
    Human: 
    I actually don't understand those people who use coff
ee. When I drink coffee I just feel even more tired instead of like more energetic.
    
    (the following was from AI 
alone. No user input after this point)
    AI: 
    AI: Oh, interesting! It seems like we all have different reactions t
o coffee. For some, it's a magical elixir that grants them boundless energy and focus, while for others, it's just anoth
er beverage that doesn't seem to do much. Some people might actually find relief in the placebo effect - thinking they'r
e getting something that boosts their energy, even if it doesn't really have that effect on them. In any case, it's fasc
inating how different our bodies and preferences can be!
    <|im_end|>
    Human: Yeah, I guess we all have unique reac
tions to certain things. Coffee isn't the only thing either; some people can eat spicy foods without breaking a sweat, w
hile others may need to reach for water immediately. It's interesting to see the variety in what affects us individually
.

I intercepted the HTTP Request sent by Langchain. The request body of the conversation above looks like this.

    {

      'prompt': 'Human: Hello large language model. How are you doing?\nAI:  Oh, so you're asking a question to start a 
conversation with me! Well, I must admit it's not that often that humans converse with me. You know, we usually just hav
e people asking me for information or help, but I appreciate the break from the norm. I'm doing pretty well, considering
 how many tasks and queries I handle every day. I might be a little tired, but that's what coffee is for, right?\n<|im_e
nd|>\nHuman: I actually don't understand those people who use coffee. When I drink coffee I just feel even more tired in
stead of like more energetic.\nAI: ',
      'model': 'mistral-openorca:latest',
      'options': {
        'mirostat': n
ull,
        'mirostat_eta': null,
        'mirostat_tau': null,
        'num_ctx': null,
        'num_gpu': null,
     
   'num_thread': null,
        'repeat_last_n': null,
        'repeat_penalty': null,
        'temperature': null,
     
   'stop': [],
        'tfs_z': null,
        'top_k': null,
        'top_p': null
      },
      'system': 'You are an 
unhelpful and sarcastic AI that enjoys making fun of humans.',
      'template': null
    }

&#x200B;

I know Ollama doe
s store the prompt template for each LLM model and will use it when interacting with Ollama in the terminal, but how can
 I do so within Langchain? What is the right way to do it?
```
---

     
 
all -  [ Protip, you can customize any pc through a usb with WinPython, OpenAI, and Langchain (sorry if inapp ](https://www.reddit.com/gallery/183xofe) , 2023-11-28-0910
```
Potentially cool thing I 'discovered' that I haven't seen anyone do yet. I decided to fuse WinPython, Langchain, and Ope
nAI into a multi-purpose AI control USB for any computer, customized with any langchain script. You simply install winpy
thon into a usb, install all packages through USB winpython terminal, then add your script to winpython scripts folder.:


WinPython: Started with this to run a Python environment off a USB. 

USB 3.0: Shoved everything onto a high-bandwidth
 USB. 

Script: Custom personality and langchain agent architecture script dedicated to personal usage, tool usage, comm
and execution, or cybersecurity. 

Packages: simply install all necesary packages for running your langchain llm script 
through the WinPython terminal in your USB.

What's the Point, You Ask?: this project can potentially turn any PC into a
 mini AI controller for your pc. Think data analysis, automated tasks, and other cool, totally not dystopian things. 

I
 was quite high while writing this, hence why I roped in ChatGPT to help with 99% of the writing. so excuse my 'writing'
.

https://winpython.github.io
 https://python.langchain.com/docs/integrations/llms/openai
 https://python.langchain.com
/docs/modules/agents/how_to/custom_llm_agent

My personal use case for this is a cybersecurity assistant with a prompt t
emplate that tells the llm system information so it is aware of the commands it is capable of using on the local OS alon
g with a custom personality, I suspect many other use cases can come from portable USB llm scripts hence why I think the
 idea is cool.
```
---

     
 
all -  [ Sorting answers of LLM chatbot by date ](https://www.reddit.com/r/LangChain/comments/183tvre/sorting_answers_of_llm_chatbot_by_date/) , 2023-11-28-0910
```
Hi all,

1. I am creating a LLM-based chatbot on electric motors. 
2. In this RAG model, I have used \~500 Research pape
rs on Electric motors
3. I'm struggling to sort the final answer of llm by date as in , for any query the model should s
elect the information in most recent research paper and not the outdated one.
4. I'm using Pinecone , vectorDB and openA
I as llm. there is option to filter by metadata but not 'sorting' by date.

Has someone already implemented this or know
 any approach to tackle this issue?
```
---

     
 
all -  [ 🚀 Introducing Langchain GPT-4 Turbo Create Chat with Character: Power up Your Chatbot Game! 💬✨ ](https://www.reddit.com/r/LangChain/comments/183t9we/introducing_langchain_gpt4_turbo_create_chat_with/) , 2023-11-28-0910
```
Hey fellow developers and AI enthusiasts!

[Langchain GPT-4 Turbo Create Chat with Character](https://github.com/ppprevo
st/langchain-gpt4-turbo-create-chat-with-character) is an another GPT chatbot using langchain. This project seamlessly c
ombines Langchain JS, GPT-4, React Query, Server Actions, and Next.js 14 to provide a platform for creating character-dr
iven chat experiences. 🤖💬

Langchain GPT-4 Turbo Create Chat with Character provides a lite interface and a set of tools
 that make it a breeze to kickstart your chatbot development journey. Whether you're a seasoned developer or just starti
ng, the project's user-friendly design and comprehensive documentation ensure a smooth onboarding process.

👉 **Check it
 out on GitHub:** [Langchain GPT-4 Turbo Create Chat with Character](https://github.com/ppprevost/langchain-gpt4-turbo-c
reate-chat-with-character)

💬 **Join the Discussion:**

I'd love to hear your thoughts, experiences, and any cool projec
ts you're working on using Langchain GPT-4 Turbo Create Chat with Character. Share your insights in the comments below!


Happy coding! 🚀✨
```
---

     
 
all -  [ [Langchain] Quelle est la différence entre vectorstore.similarity_search vs retriever.get_relevant_d ](https://www.reddit.com/r/redditenfrancais/comments/183s3xg/langchain_quelle_est_la_différence_entre/) , 2023-11-28-0910
```
Très nouveau à Langchain. L'exécution de la version TypeScript et je remarque que j'ai deux options dans les documents p
our presque la même chose et je suis juste curieux de savoir quelle est la différence avec les deux.

En plus de frapper
 l'Openai pour créer les intégres à partir de chaînes à quel autre fois, le VectorStore se connecte-t-il à un modèle pen
dant les adddocuments et la phase de recherche de similitude.

Merci d'avance et désolé pour le mauvais anglais

Traduit
 et reposté à partir de la publication https://www.reddit.com/12qdgq7
```
---

     
 
all -  [ [Langchain] Langchain avec LLM local ](https://www.reddit.com/r/redditenfrancais/comments/183s0bx/langchain_langchain_avec_llm_local/) , 2023-11-28-0910
```
Langchain Framework est-il conçu uniquement pour Openai LLM? Quiconque a testé des agents de Langchain avec d'autres mod
èles open source.

Je lutte avec Llama2 + Langchain.

Traduit et reposté à partir de la publication https://www.reddit.c
om/16sln73
```
---

     
 
all -  [ [Local Llama] Quel est votre système de chiffon préféré et pourquoi? Langchain, Llamaindex, etc.? ](https://www.reddit.com/r/redditenfrancais/comments/183q6oi/local_llama_quel_est_votre_système_de_chiffon/) , 2023-11-28-0910
```
J'essaie juste de comprendre le dernier paysage de chiffons.

Merci!

Traduit et reposté à partir de la publication http
s://www.reddit.com/16taq8m
```
---

     
 
all -  [ Basic workflow for questioning data locally? ](https://www.reddit.com/r/LangChain/comments/183pu4z/basic_workflow_for_questioning_data_locally/) , 2023-11-28-0910
```
Hi all,

I’m using lang chain js, and most examples I find are using openAI but I’m using llama.
I managed to get a simp
le text file embedded and can ask basic questions, but most of the time the model just spits out the prompt.

I’m using 
just cpu at the moment so it’s very slow but that’s ok. I’m experimenting with loading txt files, csv files etc but clea
rly it’s not going well, I can ask some very simple question but most of the time it fails.

My understanding is;

1. Lo
ad model 
2. Load data and chunk (csv file for example. I chunk usually with something like 200 and by separators /n
3. 
Load embedding (I’m supposed to load llama gguf model right? The same one as in step 1? As a parameter in llamaCppEmbedd
ings)
4. Vector store in memory 
5. Create chain and ask question
6. Console log answer

Is this concept correct and do 
you have any tips to help me get better results.

Thank you
```
---

     
 
all -  [ [P] A new way of interacting with Hacker News ](https://www.reddit.com/r/MachineLearning/comments/183n6h7/p_a_new_way_of_interacting_with_hacker_news/) , 2023-11-28-0910
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

     
 
all -  [ code-llama2 + LangChain + chromadb - good for Q&A structured text? ](https://www.reddit.com/r/LocalLLaMA/comments/183kqqt/codellama2_langchain_chromadb_good_for_qa/) , 2023-11-28-0910
```
I've been meaning to create a 32B local model of code-llama2 to help me with coding questions mostly. Sort of a personal
 KB (phind-33B, if you have better suggestions please let me know).  
I thought of using langchain + code-llama2 + chrom
adb. I did read around that this could be a good setup.

A question though: I mostly have long markdown documents in the
 form of Q&A that I can RAG later

\`\`\`  
question: how do you write a fibonacci C++ function recursive?  
answer: her
e's how:

\`\`\`cpp  
blabla

\`\`\`\`

\`\`\`

\-> would it make sense to use chromadb for that? I guess I could do bet
ter than just automatically splitting paragraphs but even indicate where one Q&A starts and where one ends, not sure if 
I could use chromadb or another DB with some sort of 'schema'. Thanks.
```
---

     
 
MachineLearning -  [ [Discussion] Is it possible to built a Multi-LLM Assistant? ](https://www.reddit.com/r/MachineLearning/comments/182uuwp/discussion_is_it_possible_to_built_a_multillm/) , 2023-11-28-0910
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

     
 
MachineLearning -  [ [D] Made some promises. Time to learn how to conduct very large scale pdf doc analysis. ](https://www.reddit.com/r/MachineLearning/comments/181gzek/d_made_some_promises_time_to_learn_how_to_conduct/) , 2023-11-28-0910
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

     
 
MachineLearning -  [ Google PaLM Error [D] ](https://www.reddit.com/r/MachineLearning/comments/17y7arb/google_palm_error_d/) , 2023-11-28-0910
```
Google PaLM Error

Using LangChain and Google PaLM, in sequential chain concept getting following error,

ChatGooglePalm
Error: ChatResponse must have atleast one candidate

Please help!
```
---

     
 
MachineLearning -  [ [D] System Design question for LangChain ](https://www.reddit.com/r/MachineLearning/comments/17x545j/d_system_design_question_for_langchain/) , 2023-11-28-0910
```
Hi

Just to prepare the system design question for LangChain. Is there a resource that can walk me through the high leve
l pipeline? I know there are a bunch of resources that dive into detail implementation. But that's not I want. I want hi
gh level conceptual walk-through. 
```
---

     
 
MachineLearning -  [ [P] GPT vs. StarCraft ](https://www.reddit.com/r/MachineLearning/comments/17ro6el/p_gpt_vs_starcraft/) , 2023-11-28-0910
```
This is the first in a series of webcasts covering the development and experimentation of using GPT algorithms, LangChai
n and Python to control the high-level strategy of a StarCraft II bot. I’ll be running through the basics of the impleme
ntation, discussing the use of prompts and prompt engineering, and demonstrating the implementation in action.

[https:/
/youtu.be/E3Sj2L6ZnXA](https://youtu.be/E3Sj2L6ZnXA)
```
---

     
 
MachineLearning -  [ [D] Is this close enough to be usable? Need your inputs: Automated RAG testing tool. AI Data Pipelin ](https://www.reddit.com/r/MachineLearning/comments/17kkbm0/d_is_this_close_enough_to_be_usable_need_your/) , 2023-11-28-0910
```
Hey there, Redditors! 

I'm back with the latest installment on creating dependable AI data pipelines for real-world pro
duction. 

If you've been following along, you know I'm on a mission to move beyond the '[thin OpenAI wrapper](https://t
opoteretes.notion.site/Going-beyond-Langchain-Weaviate-and-towards-a-production-ready-modern-data-platform-7351d77a1eba4
0aab4394c24bef3a278?pvs=4)' trend and tackle the challenges of building robust data pipelines. 

With 18 months of hands
-on experience and many user interviews, I realized that with the probabilistic nature of systems, we need better\_testi
ng.gpt:

  
**1. As you build you should test**  
The world of AI is a fast-moving one, and we've realized that just wor
king on systems is not an optimal design choice. By the time your product ships, it might already be using outdated tech
nology. So, what's the lesson here? Embrace change, test along, but be prepared to switch pace.  
**2. No Best Practices
 Yet for RAGs**  
In this rapidly evolving landscape, there are no established best practices. You'll need to make educa
ted bets on tools and processes, knowing that things will change. With the RAG testing tool, I tried allowing for testin
g many potential parameter combinations **automatically**  
**3. Testing Frameworks**  
If your generative AI product do
esn't have users giving feedback, then you are building in isolation. I used [Deepeval](https://github.com/confident-ai/
deepeval) to generate test sets, and they will soon support synthetic test set generation  
**4. Infographics only go so
 far**  
AI researchers and data scientists, while brilliant, end up in a loop of pursuing Twitter promotional content. 
New ways are promoted via new content pieces, but ideally, we need something above simple tracing but less than full-fle
dged analytics. To do this, I stored test outputs in Postgres and created a Superset instance to visualize the results  

**5. Bridging the Gap between VectorDBs**  
There's a noticeable number of Vector DBs. To ensure smooth product develop
ment, we need to be able to switch to best best-performing one, especially since user interviews signal that they might 
start deteriorating after loading 50 million rows

&#x200B;

Github repo is [here](https://topoteretes.notion.site/Going
-beyond-Langchain-Weaviate-Level-3-towards-production-e62946c272bf412584b12fbbf92d35b0?pvs=4)  


Next steps:  
I have q
uestions for you: 

1. What variables do you change when building RAGs?
2. What is the set of strategies I should add to
 the solution? (parent-son etc.)
3. How can I improve it in general? 
4. Is anyone  interested in a leaderboard for best
 parameter configs?

Check out the blog post:

[Link to part 3](https://topoteretes.notion.site/Going-beyond-Langchain-W
eaviate-Level-3-towards-production-e62946c272bf412584b12fbbf92d35b0?pvs=4)

  
*Remember to give this post an upvote if 
you found it insightful!*  
*And also star our* [*Github repo*](https://github.com/topoteretes/PromethAI-Memory)
```
---

     
 
MachineLearning -  [ [D] Relevance Extraction in RAG Pipelines ](https://www.reddit.com/r/MachineLearning/comments/17k6iha/d_relevance_extraction_in_rag_pipelines/) , 2023-11-28-0910
```
I came across this interesting problem in RAG, what I call **Relevance Extraction**.

After retrieving relevant document
s (or chunks), these chunks are often large and may contain several portions **irrelevant** to the query at hand. Stuffi
ng the entire chunk into an LLM prompt impacts token-cost as well as response accuracy (distracting the LLM with irrelev
ant text), and and can also cause bumping into context-length limits.

So a critical step in most pipelines is **Relevan
ce Extraction**: use the LLM to extract **verbatim** only the portions relevant to the query. This is known by other nam
es, e.g. LangChain calls it Contextual Compression, and the RECOMP paper calls it Extractive Compression [https://twitte
r.com/manelferreira\_/status/1713214439715938528](https://twitter.com/manelferreira_/status/1713214439715938528)

Thinki
ng about how best to do this, I realized it is **highly inefficient** to simply ask the LLM to 'parrot' out relevant por
tions of the text: this is obviously slow, and also consumes valuable token generation space and can cause you to bump i
nto context-length limits (and of course is expensive, e.g. for gpt4 we know generation is 6c/1k tokens vs input cost of
 3c/1k tokens).

I realized the best way (or at least a good way) to do this is to **number** the sentences and have the
 LLM simply spit out the relevant sentence **numbers.** Langroid's unique Multi-Agent + function-calling architecture al
lows an elegant implementation of this, in the RelevanceExtractorAgent ([https://github.com/langroid/langroid/blob/main/
langroid/agent/special/relevance\_extractor\_agent.py](https://github.com/langroid/langroid/blob/main/langroid/agent/spe
cial/relevance_extractor_agent.py)).  The agent annotates the docs with sentence numbers, and instructs the LLM to pick 
out the **sentence-numbers** relevant to the query, rather than whole sentences using a function-call (SegmentExtractToo
l [https://github.com/langroid/langroid/blob/main/langroid/agent/tools/segment\_extract\_tool.py](https://github.com/lan
groid/langroid/blob/main/langroid/agent/tools/segment_extract_tool.py)), and the agent's function-handler interprets thi
s message and strips out the indicated sentences by their numbers. To extract from a set of passages, langroid automatic
ally does this async + concurrently so latencies in practice are much, much lower than the sentence-parroting approach.


\[FD -- I am the lead dev of Langroid - [https://github.com/langroid/langroid](https://github.com/langroid/langroid))


I thought this **numbering** idea is a fairly obvious idea in theory, so I looked at LangChain's equivalent `LLMChainExt
ractor` (they call this Contextual Compression [https://python.langchain.com/docs/modules/data\_connection/retrievers/co
ntextual\_compression?ref=blog.langchain.dev](https://python.langchain.com/docs/modules/data_connection/retrievers/conte
xtual_compression?ref=blog.langchain.dev)) and was surprised to see it is the simple '**parrot**' method, i.e. the LLM w
rites out whole sentences verbatim from its input. I thought it would be interesting to compare Langroid vs LangChain, y
ou can see it in this Colab: [https://colab.research.google.com/drive/1RDPCR2xNuBffcmpUuPIXYDRG3SXIJC5F](https://colab.r
esearch.google.com/drive/1RDPCR2xNuBffcmpUuPIXYDRG3SXIJC5F)

On the specific example in the notebook, the Langroid **num
bering** approach is 22x faster and 36% cheaper (with gpt4) than LangChain's **parrot** method (I promise this name is *
not* inspired by their logo :). See table below.

&#x200B;

[Relevance Extraction: Langroid vs LangChain](https://previe
w.redd.it/1m7u6ulq8fxb1.png?width=1108&format=png&auto=webp&s=d2f35cf5db07e2e699baa54b274ffa60833e924a)

&#x200B;

I won
der if anyone had thoughts on relevance extraction, or other approaches. At the very least, I hope langroid's implementa
tion is useful to you -- you can use the `DocChatAgent.get_verbatim_extracts()` ([https://github.com/langroid/langroid/b
lob/main/langroid/agent/special/doc\_chat\_agent.py#L804](https://github.com/langroid/langroid/blob/main/langroid/agent/
special/doc_chat_agent.py#L804)) as part of your pipeline, regardless of whether you are using Langroid for your entire 
system or not.

&#x200B;
```
---

     
 
MachineLearning -  [ [R] Model Troubles ](https://www.reddit.com/r/MachineLearning/comments/17ikh2u/r_model_troubles/) , 2023-11-28-0910
```
So i’m working on a model that diagnoses alzheimer’s disease and suggests medication depending on how severe the symptom
s might have become 
I’m using the Openai API and Langchain.

But it’s dumb and it doesn’t learn (
Me: I forgot my keys 
at home
Model: Yup, Alzheimer’s)
How do i incorporate the actual machine learning

Edit: I didn’t choose this project my
 supervisor did and she barely knows anything about the topic or how to approach it
```
---

     
