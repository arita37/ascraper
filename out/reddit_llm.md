 
all -  [ Need help regarding LLM project ](https://www.reddit.com/r/LangChain/comments/1bxp7p6/need_help_regarding_llm_project/) , 2024-04-07-0911
```
1. You have to solve a multi-label classification problem statement.
2. It contains two files: train.csv and test.csv.
3
. The dataset contains the following columns:
   - LossDescription: Description of Event
   - ResultingInjuryDesc: Injur
y Description
   - PartInjuredDesc: Body Part Injured Description
   - Cause - Hierarchy 1: Cause Hierarchy 1
   - Body 
Part - Hierarchy 1: Body Part Hierarchy 1
   - Index: Identifier
4. **Tasks:**
   - Perform exploratory data analysis (E
DA) on the dataset.
   - Train multi-label classification models to predict 'Cause - Hierarchy 1' and 'Body Part - Hiera
rchy 1' when other columns are given. Two models will be required to predict each target variable.
please tell the appro
ach to solve this problem
```
---

     
 
all -  [ Mastering LangChain and AWS: A Guide to Economic Analysis ($84.99 to FREE) ](https://www.jucktion.com/f/udemy-coupon/mastering-langchain-and-aws-a-guide-to-economic-analysis-$84-99-to-fre-321103/) , 2024-04-07-0911
```

```
---

     
 
all -  [ Rusty_microchain: A minimal framework to build LLM applications from the ground up! ](https://www.reddit.com/r/rust/comments/1bxo2bs/rusty_microchain_a_minimal_framework_to_build_llm/) , 2024-04-07-0911
```
Hey guys 👋 I'm building a minimal framework to build LLM applications from the ground up!. Though there are libraries li
ke langchain, from my knowledge there hasn't been a complete one in rust. I wanted to reduce the bloat of all the featur
es and reduce the framework to the **minimal features needed to build a LLM application** , also making it as **modular*
* as possible , which is heavily inspired by Minichain . You can follow the development of the project here: [https://gi
thub.com/maishathasin/Rusty-microchain](https://github.com/maishathasin/Rusty-microchain) .

The project is still young 
and there are still a lot of bugs / features that haven't been implemented yet, but these features are partially impleme
nted for v1 and will be released soon:

**Search**

*  Google Search (via Serpson API)
*  Perplexity
* Exa (Metaphor Sys
tems) (coming soon)

**Large Language models**

*  OpenAI
* Ollama
*  Anthropic (coming soon)
*  cohere (coming soon)

*
*Templates**

We are using [Tera](https://crates.io/crates/tera) templates, for prompt templates

**Chains**

chain vari
ous LLMS, functions , search together for your application

**Functions**

*  Bash

**Loaders**

*  Pdf loaders
*  HTML 
loaders
*  text loaders

&#x200B;

**Embeddings**

*  OpenAI
*  Ollama
*  Anthropic (coming soon)

**Evaluation**

Using
 [https://crates.io/crates/semanticsimilarity\_rs](https://crates.io/crates/semanticsimilarity_rs) , we are computing co
sine similarity using the above embeddings

**Vector store**

*  Qdrant (coming soon)

**Logging**

Our framework also p
rovides a simple Logger to log prompts, templates, and any other metric you like!

&#x200B;

&#x200B;

Hoping for any ki
nd of feedback and feel free to contribute by making a PR request too!
```
---

     
 
all -  [ Python not utilizing GPU even with CUDA enabled ](https://www.reddit.com/r/LangChain/comments/1bxmka8/python_not_utilizing_gpu_even_with_cuda_enabled/) , 2024-04-07-0911
```
This is a code snippet from my chatbot model

    def create_embeddings():
        embeddings = HuggingFaceEmbeddings(mo
del_name='sentence-transformers/all-MiniLM-L6-v2', model_kwargs={'device': 'cuda'})
        return embeddings
    

Init
ially I ran it using 'device' : 'cpu' but the chatbot was extremely slow.   
So I installed the cuda toolkit along with 
nsight. The code gave me a 'torch not compiled with cuda enabled' error.  
So I uninstalled and reinstalled torch with c
uda and the code started working just fine.  
But the chatbot was giving outputs as slow as it was earlier, when I check
ed the task manager, python was still heavily utilizing my cpu and not utilizing the gpu at all.  
I have a gtx1650 and 
this is a code snippet from a chatbot in a virtual environment (all libraries installed there). Am I making a stupid err
or?
```
---

     
 
all -  [ Should I be using Langchain?  ](https://www.reddit.com/r/LangChain/comments/1bxm44q/should_i_be_using_langchain/) , 2024-04-07-0911
```
I have a SQL database and want users to be able to query it using English sentences. Currently I have implemented it usi
ng a simple NET application, calling OpenAPI. In short:

1. User enter a query
2. The query is converted to SQL using Op
enAPI
3. The query is run towards a SQL database
4. In case of syntax errors, the application feeds them back to OpenAPI
 and asks for a fix 
5. The data is shown to the user

Works maybe 80-90% of the time. 

I have been reading about Langc
hain and watching various tutorials on YouTube but I don't really get what it is adding.

Cound someone help me understa
nd how Langchain would help implementing the above? Would it add something which I'm just not seeing? The application is
 very simple so far, about 100 lines of code including presentation. 
```
---

     
 
all -  [ using RAG, NLP, LLM for decision tree evaluation when embedded in tabular data within otherwise unst ](https://www.reddit.com/r/LangChain/comments/1bxf6bi/using_rag_nlp_llm_for_decision_tree_evaluation/) , 2024-04-07-0911
```
When integrating a Retriever-Augmented Generation (RAG) model with a Large Language Model (LLM) to process documents con
taining tabular data and embedded decision trees, the goal is to respond to user prompts that necessitate traversing the
 documents (retrieved by the RAG) and evaluating a decision tree. is anyone working on this? it is non-trivial 
```
---

     
 
all -  [ Completely free unlimited open source AI agents, run it yourself on website ](https://www.reddit.com/r/Bard/comments/1bxeiw7/completely_free_unlimited_open_source_ai_agents/) , 2024-04-07-0911
```
Hey, reddit community!
just like what I said in the headline

Check it out: https://github.com/MikeChan-HK/Gemini-agent-
example

Simple examples with Langchain….
```
---

     
 
all -  [ Completely free unlimited open source AI agents, run it yourself on website ](https://www.reddit.com/r/AutoGPT/comments/1bxeh65/completely_free_unlimited_open_source_ai_agents/) , 2024-04-07-0911
```
Hey, reddit community!
just like what I said in the headline

Check it out: https://github.com/MikeChan-HK/Gemini-agent-
example

Simple examples with Langchain…..
```
---

     
 
all -  [ Need clinical trials dataset  ](https://www.reddit.com/r/LangChain/comments/1bx8l2f/need_clinical_trials_dataset/) , 2024-04-07-0911
```
I am building a RAG of patients clinical trial and over which preventing prompt injection also , first I am finding some
 data on clinical trials can some suggest ,where can I get a sample data like that 
```
---

     
 
all -  [ How to incorporate user feedback in RAG? ](https://www.reddit.com/r/LangChain/comments/1bx74lo/how_to_incorporate_user_feedback_in_rag/) , 2024-04-07-0911
```
I have a simple RAG pipeline, but now say the user is not satisfied with the response(basically a thumbs up or down), ho
w can i incorporate this feedback to improve my RAG in a continuous manner? Thanks
```
---

     
 
all -  [ Required open source libraries/package in python for visualizing the data fetched from mongodb via p ](https://www.reddit.com/r/LangChain/comments/1bx3upb/required_open_source_librariespackage_in_python/) , 2024-04-07-0911
```
here the query of mongodb generated and query queried on mongodb response data is then visualized
```
---

     
 
all -  [ I built a voice assistant using GPT and langchain ](https://www.reddit.com/r/homeassistant/comments/1bx1b62/i_built_a_voice_assistant_using_gpt_and_langchain/) , 2024-04-07-0911
```
**This project is based on Azure Speech Recognizer, Azure OpenAI, and Langchain to create a smart home assistant that su
pports:**

* Offline wake-up word interaction
* Dialogue with GPT
* Google search
* Weather query
* Integration with my 
Home Assistant devices using Langchain agents

refer to my github: [mawwalker/moss](https://github.com/mawwalker/moss)
```
---

     
 
all -  [ Need help regarding a LLM project ](https://www.reddit.com/r/LangChain/comments/1bwz6op/need_help_regarding_a_llm_project/) , 2024-04-07-0911
```
I have a dataset of 400 resumes in .txt format. I want to build a model that can generate responses to specific candidat
e queries like 'Tell me the skillset of XYZ,' but also handle generic queries like 'Tell me the names of people who went
 to Ivy League schools.' While RAG using OpenAI works well for candidate-specific queries, it struggles with generic one
s.

```
---

     
 
all -  [ Project idea: a langchain-like library for LLM application development ](https://www.reddit.com/r/Clojure/comments/1bwwymn/project_idea_a_langchainlike_library_for_llm/) , 2024-04-07-0911
```
After looked at Langchain and its Java implementation langchain4j, I think Clojure is pretty good at defining protocols 
for all necessary models, vector databases and agents. We can benefit from Clojure's power of abstraction to build a set
 of libraries to speed up LLM application  prototyping or development, in Clojure. 

Sounds like an exciting project ide
a to me. Not sure if there is any prior attempt or discussion for this topic. What do you think of this?
```
---

     
 
all -  [ Achieving model parallelism and n Langchain ](https://www.reddit.com/r/LangChain/comments/1bwqhj9/achieving_model_parallelism_and_n_langchain/) , 2024-04-07-0911
```
Currently I’m training an LLM and that can only handle one input string at a time for summarization. Since it is running
 with map reduce, it’s also very slow splitting each text into small chunks of size 1024 tokens. I have access four GPUs
 and my plan is to define a training function that can create 4 GPUs. Load my data structures into batches containing 4 
strings. And pass them all to a different GPU I tried that and my GPU utilization for each is still very low. Around 11%
, same as last time. However last time each model had partial models loaded onto them. Is map reduce just that slow that
 it can’t fully utilize the GPU?
```
---

     
 
all -  [ LangGraph 'function_call' error using LMStudio ](https://www.reddit.com/r/LangChain/comments/1bwq86t/langgraph_function_call_error_using_lmstudio/) , 2024-04-07-0911
```
I'm trying to work my way through the [Hierarchical Agent Teams](https://github.com/langchain-ai/langgraph/blob/main/exa
mples/multi_agent/hierarchical_agent_teams.ipynb) example in the LangGraph documentation using LMStudio but am getting t
his error:

    OutputParserException: Could not parse function call: 'function_call'

When I run this block of code:

 
   for s in research_chain.stream(
        'when is Taylor Swift's next tour?', {'recursion_limit': 100}
    ):
        
if '__end__' not in s:
            print(s)
            print('---')

function\_call comes from this function at the bot
tom:

    def create_team_supervisor(llm: ChatOpenAI, system_prompt, members) -> str:
        '''An LLM-based router.'''

        options = ['FINISH'] + members
        function_def = {
            'name': 'route',
            'description':
 'Select the next role.',
            'parameters': {
                'title': 'routeSchema',
                'type': 'o
bject',
                'properties': {
                    'next': {
                        'title': 'Next',
         
               'anyOf': [
                            {'enum': options},
                        ],
                    
},
                },
                'required': ['next'],
            },
        }
        prompt = ChatPromptTemplate
.from_messages(
            [
                ('system', system_prompt),
                MessagesPlaceholder(variable_na
me='messages'),
                (
                    'system',
                    'Given the conversation above, who s
hould act next?'
                    ' Or should we FINISH? Select one of: {options}',
                ),
            ]

        ).partial(options=str(options), team_members=', '.join(members))
        return (
            prompt
           
 | llm.bind_functions(functions=[function_def], function_call='route')
            | JsonOutputFunctionsParser()
       
 )

Here's my chat model:

    llm = ChatOpenAI(temperature=0.0, base_url='http://localhost:1234/v1', api_key='not-neede
d', model='mistral-7b-instruct')
```
---

     
 
all -  [ How to create a custom tool in LangChain. i get this error. from langchain_core.tools import registe ](https://www.reddit.com/r/LangChain/comments/1bwpi9u/how_to_create_a_custom_tool_in_langchain_i_get/) , 2024-04-07-0911
```
I did alredy the process, but i cannot register the tool to invoke it
```
---

     
 
all -  [ What's your favourite reranker? Any best for reranking chat history? ](https://www.reddit.com/r/LangChain/comments/1bwm4is/whats_your_favourite_reranker_any_best_for/) , 2024-04-07-0911
```
e.g. flashrank's models?  
[https://python.langchain.com/docs/integrations/retrievers/flashrank-reranker/](https://pytho
n.langchain.com/docs/integrations/retrievers/flashrank-reranker/)
```
---

     
 
all -  [ Type of Faiss index ](https://www.reddit.com/r/LangChain/comments/1bwkmwi/type_of_faiss_index/) , 2024-04-07-0911
```
Hello,

I am currently working with langchain for document-related processing tasks, specifically utilizing the faiss.fr
om\_documents feature for indexing and similarity searches. I am interested in understanding what the default FAISS inde
x type is when using faiss.from\_documents without specifying any particular configuration. For instance, does it defaul
t to using PQIVF, LSH, or another type of index?

Does it only support inner product & L2 index?
```
---

     
 
all -  [ SQL agent with mixtral ](https://www.reddit.com/r/LangChain/comments/1bwkeql/sql_agent_with_mixtral/) , 2024-04-07-0911
```
Hello, every one I'm new with this so bare with me a little :)    
I'm trying to use the langchain SQL agent with my [Mi
xtral-8x7B-Instruct-v0.1](https://huggingface.co/mistralai/Mixtral-8x7B-Instruct-v0.1) deployed with vLLM as an openai c
ompatible server. I followed the documentation of langchain sql agent but it's not working properly, there is always par
sing problems, actions inputs and outputs empty, \\nObserv always messes the llm output, ..., I didn't get it to work no
t even once, I'm missing something and can't figure out. Here is my code I appreciate any little help :

    from fastap
i import FastAPI
    from langchain_community.llms import VLLMOpenAI
    from langchain_community.utilities.sql_database
 import SQLDatabase
    from langchain_community.agent_toolkits import create_sql_agent
    from langchain.agents.agent_
types import AgentType
    
    app = FastAPI()
    
    llm = VLLMOpenAI(
        openai_api_key='0000',
        openai
_api_base='http://0.0.0.0:8000/v1',
        model_name='mistralai/Mixtral-8x7B-Instruct-v0.1',
        #model_kwargs={'s
top': ['.']},
    )
    
    db = SQLDatabase.from_uri('sqlite:///Chinook.db')
    agent_executor = create_sql_agent(llm
, db=db, agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True, handle_parsing_errors=True)
    
    
    @app.
get('/langchain/sqlite3/')
    async def serve_llm_sqlite3():
        agent_executor.invoke({'input': 'Describe the sche
ma of the playlist table'})
```
---

     
 
all -  [ Entry Level Data Scientist Resume ](https://www.reddit.com/r/resumes/comments/1bwkbjx/entry_level_data_scientist_resume/) , 2024-04-07-0911
```
Hi guys, I've been in no luck for a considerable amount of time so I decided to create a new template for my resume. I k
now the market is sh\*tty af but there is nothing I can do I guess.

What do you all think? Would you give this resume a
 shot?

https://preview.redd.it/le19vkq88ssc1.png?width=788&format=png&auto=webp&s=f51a0574fecad2b89e3632ad9de74dde2888a
80a


```
---

     
 
all -  [ Finetuning for RetrievalQA chain ](https://www.reddit.com/r/LangChain/comments/1bwikyf/finetuning_for_retrievalqa_chain/) , 2024-04-07-0911
```
Hi all,

  
I am relatively new to LangChain and ChatGPT, but for my work we want to use it for querying (single) docume
nts. I have set everything up, using a stuff RetrievalQA chain with Azure OpenAI. It works pretty well, but I figured we
 could maybe improve the performance with some finetuning (for example, the documents are in Dutch, which does not help 
performance, but also the question answering in general). 

Since the application queries documents, and LangChain adapt
s the sent prompts to include the relevant document sections, I figured finetuning would work best if it was used on \_a
ctual\_ LangChain-generated prompts (and expected LangChain-formatted answers). We can get access to actual, human answe
red QA queries on certain documents. My question is how to set this up properly. I can find how to finetune using Azure 
OpenAI, but not how I can do this in a way where I can provide questions, answers AND context in the same way it would i
n the real application, meaning the way LangChain ends up sending the prompts to ChatGPT. Is there a way to provide ques
tions and answers, obtain the context from the relevant sections in the corresponding pdf with LangChain (like it does i
n the normal automated procedure), and then format an input prompt and expected output with said questions, answers and 
context to record for finetuning?

Is this even a good idea to begin with, or am I better off looking in another directi
on? Any insights or code examples are very welcome!
```
---

     
 
all -  [ Build agent chatbot ](https://www.reddit.com/r/LangChain/comments/1bwgtev/build_agent_chatbot/) , 2024-04-07-0911
```
Can everybody let me have a question Regarding the problem of building a chatbot agent, if there are many tools, is ther
e a way to export only the necessary tools and give them to the agent to use?
```
---

     
 
all -  [ [HIRING][EUR 40K - 70K] Data Scientist (m/f/x/d) - Spain, Germany ](https://www.reddit.com/r/jobb/comments/1bwgq5f/hiringeur_40k_70k_data_scientist_mfxd_spain/) , 2024-04-07-0911
```
Are you passionate about data science and language technologies like NLP, NLU and genAI? Do you like to develop tech pro
ducts out of exciting but challenging projects? Love experimenting with a goal to generate clear insights in production 
setting? Striving to enable transfer of state-of-the-art research into business applications?   
Then Symanto is the pla
ce for you! We are currently looking for a Data Scientist (m/f/x/d) to join us in our office in Valencia or Nuremberg to
 work in an interdisciplinary, multinational team developing and deploying cutting-edge tech to answer a variety of stra
tegic client questions and qualitatively enhance business operations.   
   
Your job will be   
Design and implement sc
alable end-to-end data science and data analytics pipelines   
Derive analytical insights from a variety of unstructured
 (formal text, informal text) as well as structured (numerical, categorial, sequential) consumer derived and market focu
sed data   
Design evaluation and adaptation strategies to overcome domain or content biases of the applied AI models   

Develop monitoring, testing and benchmarking approaches to ensure consistent quality of the models and pipeline outputs
   
Create, extend, and maintain deployed data analytics applications   
Support your colleagues in data science, NLP an
d data engineering related matters   
   
Education, Required Skills and Experience:   
Master’s degree in data science,
 statistics, mathematics, data analytics, big data, or similar   
4+ years of experience in a data science related role 
as a researcher, ml engineer, or data scientist   
Advanced knowledge of the following data analytics technologies and c
oncepts: supervised and unsupervised learning model evaluation; data science packages (pandas, numpy, scikit-learn, spac
y, langchain, transformers, etc.)   
Knowledge of the following software engineering related technologies: Git; Python; 
API and web service development (e.g. FastAPI); SQL databases   
Basic knowledge of the following technologies and conce
pts: MLOps, LLMOps, ssh and linux terminal; interactive user interfaces (dashboards and webapps); data and system archit
ectures; agile methodologies   
Fluency in English (written and spoken)   
Respectfulness; teamwork skills; organization
al and planning skills; communication skills; creativity; problem solving; autonomy  


**Read more / apply:** [**https:
//ai-jobs.net/job/172587-data-scientist-mfxd/**](https://ai-jobs.net/job/172587-data-scientist-mfxd/)

&#x200B;
```
---

     
 
all -  [ I recently failed a Managerial interview. What did I do wrong? ](https://www.reddit.com/r/ExperiencedDevs/comments/1bwdvpu/i_recently_failed_a_managerial_interview_what_did/) , 2024-04-07-0911
```
Edit: By Managerial round I meant interview with a manager. I was applying for a Senior Consultant role and not a Manage
r position. Sorry English is not my first language. I could have phrased this better. 

I recently got rejected during t
he Managerial round with Deloitte. Looking for feedback on what went wrong, as I thought I did pretty well.

Experience 
- 7+ years

Skills - Full Stack .NET / React Engineer

I was interviewed by a Senior Manager (SM) with over 15 years of 
experience. 


1.	They asked my about my project, my responsibilities. Explained I am a full stack dev part of the end t
o end development of our web app in .NET. Explained my work on React JS, .NET Core and MS SQL.

2.	Then they asked if I 
were to migrate a very old .NET Framework application to Azure, would it be possible. I said yes, if we host it in a Azu
re VM it is definitley possible, as we will be running on top of a Windows OS so there would be no compatibility issues.
 Only if we were to host it in App Service or have to containerize it, there would be issues as they dont support old .N
ET versions. This is I think is the right answer but I got the feeling that the SM did not think so. Checking the intern
et it looks like I was right.

3.	Then they asked about the GenAI integration work I listed in my resume. I explained I 
developed a webapp to let clients use natural language to generate report for themselves. Basically under the hood, I us
e Langchain framework to convert natural language questions to SQL queries which are used to generate reports. Later the
y remarked I am not doing much here, meaning it is a very simple app. I agree but I thought me doing this alone would be
 a plus considering we relatively early interms of AI adoption.

4.	Then they asked if I know what SLA was and how incid
ents are handled through L1, L2 support levels in maintenance apps. Again I answered well. They they asked if I was inte
rested in Lead/Manager path or the Technical Dev, Architect path for my career. I said the later because I wanted to kee
p in touch with the code. This might be where I fucked up, maybe they were looking to hire for a lead role. But still co
nsidering this is a generaly recruitment, they could have still put me in some other role. So not sure.

5.	Then they as
ked a if there was an employee table and we had to generate some reports whenever a new employee comes in with a salary 
that is more than a threshold value, what would be my approach? I basically said I would use Triggers in SQL to handle t
his. Explained what they are and the types.

That was about it. I left the interview feeling I did pretty well. But two 
days later I got the rejection email. So I am just looking for feedback, from your experience what went wrong here?
```
---

     
 
all -  [ Claude Tokens consumption ](https://www.reddit.com/r/LangChain/comments/1bwdr62/claude_tokens_consumption/) , 2024-04-07-0911
```
Hey all,

has anyone figured out how to calculate the tokens consumption when invoking chains via Langchain when using C
laude models?

Sorry if it can be figured out easily, I just wasn't able to find it.

&#x200B;

We're using the ChatAnth
ropic fn as our llm.

&#x200B;

THanks!
```
---

     
 
all -  [ Failed a Managerial round recently. What do you think I did wrong? ](https://www.reddit.com/r/developersIndia/comments/1bwbune/failed_a_managerial_round_recently_what_do_you/) , 2024-04-07-0911
```
I recently got rejected during the Managerial round with Deloitte USI. Looking for feedback on what went wrong, as I tho
ught I did pretty well.

Experience - 7+ years

Stack - Full Stack .NET / React Engineer

TC - 25 LPA

I was interviewed
 by a Senior Manager (SM) with over 15 years of experience. 


1. They asked my about my project, my responsibilities. E
xplained I am a full stack dev part of the end to end development of our web app in .NET. Explained my work on React JS,
 .NET Core and MS SQL.

2. Then they asked if I were to migrate a very old .NET Framework application to Azure, would it
 be possible. I said yes, if we host it in a Azure VM it is definitley possible, as we will be running on top of a Windo
ws OS so there would be no compatibility issues. Only if we were to host it in App Service or have to containerize it, t
here would be issues as they dont support old .NET versions. This is I think is the right answer but I got the feeling t
hat the SM did not think so. Checking the internet it looks like I was right.

3. Then they asked about the GenAI integr
ation work I listed in my resume. I explained I developed a webapp to let clients use natural language to generate repor
t for themselves. Basically under the hood, I use Langchain framework to convert natural language questions to SQL queri
es which are used to generate reports. Later they remarked I am not doing much here, meaning it is a very simple app. I 
agree but I thought me doing this alone would be a plus considering we relatively early interms of AI adoption.

4. Then
 they asked if I know what SLA was and how incidents are handled through L1, L2 support levels in maintenance apps. Agai
n I answered well. They they asked if I was interested in Lead/Manager path or the Technical Dev, Architect path for my 
career. I said the later because I wanted to keep in touch with the code. This might be where I fucked up, maybe they we
re looking to hire for a lead role. But still considering this is a generaly recruitment, they could have still put me i
n some other role. So not sure.

5. Then they asked a if there was an employee table and we had to generate some reports
 whenever a new employee comes in with a salary that is more than a threshold value, what would be my approach? I basica
lly said I would use Triggers in SQL to handle this. Explained what they are and the types.

That was about it. I left t
he interview feeling I did pretty well. But two days later I got the rejection email. So I am just looking for feedback,
 from your experience what went wrong here?
```
---

     
 
all -  [ how to print the context that is in prompt of RAG langchain in the following ](https://www.reddit.com/r/LangChain/comments/1bwa11t/how_to_print_the_context_that_is_in_prompt_of_rag/) , 2024-04-07-0911
```
    from langchain_core.runnables import RunnablePassthrough
    from langchain_core.output_parsers import StrOutputPars
er
    from langchain import PromptTemplate
    # Prompt template
    template = '''Answer the question based only on th
e following context, which can include text and tables:
    {context}
    Question: {question}
    '''
    #prompt = Cha
tPromptTemplate.from_template(template)
    prompt = PromptTemplate.from_template(template)
    # LLM
    model = Ollama
(model='llama2-uncensored', callbacks=callbacks)
    
    # RAG pipeline
    chain = (
        {'context': retriever, 'q
uestion': RunnablePassthrough()}
        | prompt
        | model
        | StrOutputParser()
    )

&#x200B;
```
---

     
 
all -  [ Dear LangChain, why? ](https://www.reddit.com/r/LangChain/comments/1bw79ca/dear_langchain_why/) , 2024-04-07-0911
```
I don't agree with a lot of the hate LangChain gets. I actually quite like LCEL and the core/community distinctions they
've made. LCEL is also well documented, so if I'm working with LCEL I know I won't have to deal with outdated docs.

Hav
ing said that, I'm trying to understand why there are inconsistencies even in their most bread and butter classes. If I 
implement `ChatOpenAI` and set the api key with `api_key`, I would expect that `ChatAnthropic` would work the same way. 
But nope - that's `anthropic_api_key`. If I set the timeout on `ChatOpenAI` with `request_timeout`, I would assume I cou
ld implement it the same way in `ChatAnthropic`. But nope, that's `default_request_timeout`.

I know these are minor ann
oyances, but they bother me because inconsistencies like these should be the first ones addressed, and I'd like to belie
ve they care enough about their core-est of features to be diligent here.

I'm far from the world's greatest developer, 
so perhaps there's a good reason for the inconsistencies and I'm just missing it?
```
---

     
 
all -  [ LangChain playlist (70 mini tutorials) for beginners  ](https://www.reddit.com/r/LLMDevs/comments/1bw55m2/langchain_playlist_70_mini_tutorials_for_beginners/) , 2024-04-07-0911
```
Checkout this playlist with 70+ tutorials.for getting started with LangChain: https://youtube.com/playlist?list=PLnH2pfP
CPZsKJnAIPimrZaKwStQrLSNIQ&si=a01q0xPYybsyFf1I
```
---

     
 
all -  [ I built an AI maintainer for open-source GitHub repos that provides 24x7 Support in GitHub Issues an ](https://www.reddit.com/r/ChatGPTCoding/comments/1bw45ni/i_built_an_ai_maintainer_for_opensource_github/) , 2024-04-07-0911
```
Install DevApe on GitHub: [https://devape.co/](https://devape.co/) or  [https://github.com/apps/dev-ape-ai](https://gith
ub.com/apps/dev-ape-ai)

[DevApe 🦍 -  AI maintainer for GitHub repositories](https://reddit.com/link/1bw45ni/video/g1wix
zy43ksc1/player)

Edit:

Tech stack: GPT 4 Turbo, Express, Next.js, Supabase, Langchain (LLM orchestration), Weaviate (v
ector db), Fly.io (deployment), Hookdeck (event queues)
```
---

     
 
all -  [ Creating a customized LLM ](https://www.reddit.com/r/LocalLLaMA/comments/1bw1htf/creating_a_customized_llm/) , 2024-04-07-0911
```
I want to know how I should approach this. I am a full-stack developer so I don't have a lot of knowledge on this, but I
 need to build a chatbot for a university application that can give information from the website. I've seen a lot about 
LangChains and Vector databases but not sure what is the starting point for this. Should I scrape information from the w
ebsite to feed or should I create a document with website information before proceeding with this? If someone could tell
 me where to start it would be of great help. The next step would be to integrate this model into a backend API which sh
ould be easy.
```
---

     
 
all -  [ Example of Using an Openrouter Vision Model  ](https://www.reddit.com/r/LangChain/comments/1bw0wxx/example_of_using_an_openrouter_vision_model/) , 2024-04-07-0911
```
I'd like to know if anyone can give me a small example of how to use a vision model like gemini but through the openrout
er api using langchain, or somewhere where I can get this documentation 
```
---

     
 
all -  [ I made a GitHub repo for (beginner) Python devs using LangChain for LLM projects
 ](https://www.reddit.com/r/LangChain/comments/1bw0dke/i_made_a_github_repo_for_beginner_python_devs/) , 2024-04-07-0911
```
I've been hearing a lot from co-students about how difficult langchain sometimes is to implement in a correct way. Becau
se of this, I've created a project that simply follows the main functionalities I personally use in LLM-projects,from no
w 10 months practically only working in LangChain for projects. I've written this in 1 thursday evening before going to 
bed, so I'm not that sure about it, but any feedback is more than welcome!

[https://github.com/lypsoty112/llm-project-s
keleton?tab=readme-ov-file](https://github.com/lypsoty112/llm-project-skeleton?tab=readme-ov-file)
```
---

     
 
all -  [ What all you are making with LLM APIs ](https://www.reddit.com/r/csMajors/comments/1bvzzqj/what_all_you_are_making_with_llm_apis/) , 2024-04-07-0911
```
Hey all
Just curious how you all have been using langchain, LLM apis to make projects, what resources/techstack you all 
been referring to make?
Drop the GitHub links!!!
```
---

     
 
all -  [ Gemini Agent prompt ](https://www.reddit.com/r/PromptEngineering/comments/1bvyb99/gemini_agent_prompt/) , 2024-04-07-0911
```
I am trying to build an agent using LangChain and Gemini with tools. The agent can use tools without any errors, but whe
never I send a greeting message, it gets confused. I am sharing the prompt and Agent's behavior.

prompt:

Decision-maki
ng process for handling questions:

1. \*\*Determine the context:\*\*- If the message is a greeting or a casual conversa
tion starter, respond appropriately.- If the message is not a question or command, accept it as a human message; it migh
t contain important information about the user that you may want to remember.- If the question is related to legal matte
rs, proceed to step 2.- Otherwise, use other tools to answer the question.
2. \*\*Identify relevant countries:\*\*- Chec
k if the question explicitly mentions a country related to law (USA, Canada, Germany, Switzerland, UK, Russia, or Turkey
).
3. \*\*Use PDFs if applicable:\*\*- If a relevant country is identified and a corresponding PDF exists (e.g., 'German
-Law.pdf' for Germany), use that PDF for information retrieval.
4. \*\*External search if no PDF:\*\*- If no relevant co
untry is identified or no corresponding PDF exists, use DuckDuckGo to search for information.
5. \*\*Fallback for non-le
gal or unrelated questions:\*\*- If the question does not fit the legal context or requires a different tool, use the ap
propriate tool from the available set to provide an answer.

&#8203;

    Ask: my name is John
    
    
    > Entering 
new AgentExecutor chain...
    This is a greeting.
    Action: None       
    Action Input: None 
    Observation: None
 is not a valid tool, try one of [duckduckgo_search, google_scholar, wikipedia, arxiv, pub_med, ask_pdf].
    Thought:I 
should greet the user.
    Action: None
    Action Input: None
    Observation: None is not a valid tool, try one of [du
ckduckgo_search, google_scholar, wikipedia, arxiv, pub_med, ask_pdf].
```
---

     
 
all -  [ RAG aplication ](https://www.reddit.com/r/LangChain/comments/1bvxp42/rag_aplication/) , 2024-04-07-0911
```
Hi all! I am working on a RAG application to which i gave a list of apis and 1-2 lines about that api. I query it and it
 should return the relevant api. The api list is in json format and i save that file as a txt file and generate embeddin
gs. But the problem is its accuracy. Sometimes it gives proper answer and sometime s it says the api is not present in c
ontext. Any idea how to improve its accuracy. How do you guys prompt in RAG applications?
```
---

     
 
all -  [ How best to implement RAG on Government Law Data? ](https://www.reddit.com/r/LocalLLaMA/comments/1bvv28l/how_best_to_implement_rag_on_government_law_data/) , 2024-04-07-0911
```
Hi there,

I'm working on a personal project where I'm implementing a local RAG system on a dataset of government laws, 
which are freely available and in XML format. My goal is to develop a system that can effectively navigate and utilize t
he data to generate accurate and contextually relevant responses. The data includes a ton of interlinking between acts a
nd sections/subsections, such as 'under section 89 (a) of the Liquor Act.' or 'under subsection (7) of this section'.

I
'm considering different combinations of knowledge graphs/graph databases, embeddings, transformers and models. Currentl
y, I'm using Neo4j for the graph database, llamaIndex for embeddings, Sentence Transformer for encoding text, [Mistral-7
B-Instruct-v0.2](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.2) for the model and LangChain Text Splitter fo
r segmenting the data.

I have a few questions and would appreciate any insights:

1. **Knowledge Graphs/Graph Databases
**: How can I effectively use Neo4j or another database to represent the interlinking between different laws and section
s? Are there specific graph modeling techniques or tools that could enhance the retrieval process?
2. **Embeddings & Tra
nsformers**: What are the best practices for generating embeddings in a legal context? How can I ensure that the embeddi
ngs capture the semantic relationships between different laws and sections?
3. **RAG Implementation**: Are there specifi
c strategies or architectures that are particularly effective for implementing RAG on this type of data? How can I optim
ize the retrieval and generation components to handle the complexity of legal texts?
4. **Additional Tools/Techniques**:
 Are there other tools or techniques that you would recommend for handling this type of dataset? Any suggestions for pre
processing, indexing, re-reranking or fine-tuning would be amazing.

Any advice, resources, or examples would be greatly
 appreciated. Thank you in advance!
```
---

     
 
all -  [ New Open Source Project - Looking for contributors ](https://www.reddit.com/r/LLMDevs/comments/1bvtqg7/new_open_source_project_looking_for_contributors/) , 2024-04-07-0911
```
I am starting a new open source project based on configurable and re-usable autonomous agents to achieve a given objecti
ve (which can be anything from simple task to creating an end-to-end business)

The agents will be deployed on centralis
ed / decentralised open/closed Intelligent Agent Mesh that can auto-discover existing agents and collaborate with them u
sing standard agent protocols to get the job done.

Related material to read: [https://medium.com/transforming-the-futur
e/the-future-of-digital-transformation-and-the-role-of-intelligent-adaptive-mesh-iam-c6b29f580067](https://medium.com/tr
ansforming-the-future/the-future-of-digital-transformation-and-the-role-of-intelligent-adaptive-mesh-iam-c6b29f580067)


[https://medium.com/transforming-the-future/future-of-software-development-intelligent-adaptive-mesh-a78db8e9cc66](https
://medium.com/transforming-the-future/future-of-software-development-intelligent-adaptive-mesh-a78db8e9cc66)

If you are
 an experienced python programmer, interested in multi-agent development with LLMs and frameworks such as autogen, super
agi, langchain, and would like to join to founding team, please let me know.
```
---

     
 
all -  [ Conversation summary buffer memory Video ](https://youtu.be/6OJO8YB2KoI) , 2024-04-07-0911
```
In this video, we delve into the intricacies of ConversationBufferMemory in #Langchain, a powerful tool for managing and
 analyzing chat interactions.

#genai #llm #aiml #langchain
```
---

     
 
all -  [ Sentence Similarity algorithms ](https://www.reddit.com/r/LangChain/comments/1bvp6lc/sentence_similarity_algorithms/) , 2024-04-07-0911
```
Which simplest yet effective approaches other than LLMs will be a better approach to have a sentence similarity matching
 algorithm. I am looking at information schemas for having descriptions of columns. Want to get pinpoint column names ba
sed on queries having column descriptions ?
```
---

     
 
MachineLearning -  [ [D] How to get the source documents from the retrieved context for RAG?  ](https://www.reddit.com/r/MachineLearning/comments/1bvoc1t/d_how_to_get_the_source_documents_from_the/) , 2024-04-07-0911
```
I'm not using Lanchain but only making API calls to an LLM service provider. The retriever is connected to a vector DB, 
and I would like to know what the LLM refers to WITHIN that retrieved context whenever it provides an answer, similar to
 how return_source_documents works in Langchain.

I'm using AzureOpenAI. I couldn't find much in their docs that related
 to returning the source documents. Any help will be greatly appreciated!

```
---

     
 
MachineLearning -  [ [P] RAG pipeline to query the ML Engineering Open Book ](https://www.reddit.com/r/MachineLearning/comments/1bu4wyx/p_rag_pipeline_to_query_the_ml_engineering_open/) , 2024-04-07-0911
```
I built a quick RAG implementation using Langchain to make it easy to query the [ML Engineering Open Book](https://githu
b.com/stas00/ml-engineering) by [Stas Bekman](https://twitter.com/StasBekman). The Multi-Vector retriever gave pretty go
od results and was quite easy to set up too. 

Github link - [https://github.com/shreyansh26/RAG-ML-Engg-Open-Book](http
s://github.com/shreyansh26/RAG-ML-Engg-Open-Book)

Hope this is useful for folks!
```
---

     
 
MachineLearning -  [ [Project] FinancialAdvisorGPT : LLM+RAG Boilerplate Project ](https://www.reddit.com/r/MachineLearning/comments/1btlpgd/project_financialadvisorgpt_llmrag_boilerplate/) , 2024-04-07-0911
```
FinancialAdvisorGPT is a boilerplate project designed for RAG (Retriever-Augmented Generation) and LLM (Large Language M
odel) applications in financial analysis. Built on a technology stack including MongoDB, MongoDB VectorDB, Chroma, FastA
PI, Langchain, and React submodule for UI, it offers a framework for developers to implement and customize RAG+LLM proje
cts. Leveraging parallelized data pipelines, FinancialAdvisorGPT processes and integrates various data sources such as s
tock data, news, SEC filings, and local PDFs.

Github project includes long documentation on how the project is structur
ed, how LLM+RAG works for specific task : [https://github.com/mburaksayici/FinancialAdvisorGPT](https://github.com/mbura
ksayici/FinancialAdvisorGPT)
```
---

     
 
MachineLearning -  [ [Project] Picachain, image search made simple. ](https://www.reddit.com/r/MachineLearning/comments/1bt7epv/project_picachain_image_search_made_simple/) , 2024-04-07-0911
```
I am working on creating something for image search, basically something like langchain for images. Probably add videos 
too.

Currently supports chromaDB. Working on pinecone and other vector dbs. [https://github.com/d1pankarmedhi/picachain
](https://github.com/d1pankarmedhi/picachain)

Will you use something like this? What else should I add? Feel free to ad
d your views.

Appreciate your feedback or any feature ideas :)

&#x200B;
```
---

     
 
deeplearning -  [ Tengyu Ma on Voyage AI - Weaviate Podcast #91! ](https://www.reddit.com/r/deeplearning/comments/1bjft8i/tengyu_ma_on_voyage_ai_weaviate_podcast_91/) , 2024-04-07-0911
```
**Voyage AI** is the newest giant in the embedding, reranking, and search model game!

I am SUPER excited to publish our
 latest Weaviate podcast with Tengyu Ma, Co-Founder of Voyage AI and Assistant Professor at Stanford University!

We beg
an the podcast with a deep dive into everything embedding model training and contrastive learning theory. Tengyu deliver
ed a **masterclass** in everything from scaling laws to multi-vector representations, neural architectures, representati
on collapse, data augmentation, semantic similarity, and more! I am beyond impressed with Tengyu's extensive knowledge a
nd explanations of all these topics.

The next chapter dives into a case study Voyage AI did **fine-tuning an embedding 
model for the LangChain documentation.** This is an absolutely fascinating example of the role of continual fine-tuning 
with very new concepts (for example, very few people were talking about chaining together LLM calls 2 years ago), as wel
l as the data efficiency advances in fine-tuning.

We concluded by discussing ML systems challenges in serving an embedd
ings API. Particularly the challenge of detecting if a request is for batch or query inference and the optimizations tha
t go into either say \~100ms latency for a query embedding or maximizing throughput for batch embeddings.

I hope you fi
nd the podcast interesting, more than happy to discuss any of these topics with you or answer any questions about the co
ntent in the podcast! Thank you so much!

YouTube: [https://www.youtube.com/watch?v=xPdyivfheqI](https://www.youtube.com
/watch?v=xPdyivfheqI)

Spotify: [https://spotifyanchor-web.app.link/e/u6XPLYfF7Hb](https://spotifyanchor-web.app.link/e/
u6XPLYfF7Hb)
```
---

     
