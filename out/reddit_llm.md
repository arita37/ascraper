 
all -  [ Seeking help with creating CLI for 'non-programmers' (LLMs) ](https://www.reddit.com/r/ArtificialInteligence/comments/1elrl0l/seeking_help_with_creating_cli_for_nonprogrammers/) , 2024-08-07-0911
```
***TL;DR*** What is the best way to convert user input into sequence of commands and their corresponding parameters? Lik
e, imagine you are not a programmer and there is a console app with a CLI, but, well, you don't know the structure and t
he syntax of commands. And you don't want to know. YBut! You have a locally running instance of llama3.1 -- or whatever 
open LLM is out there now -- and you can ask it to create a CLI command for you. What would you do to accomplish that?


**Intro**

A little bit of context. I'm working on a project that targets scientists as end users. It has some UI using 
which it's possible to do all sort of things the lab workers would like to do. But recently the projects product owner d
ecided that it would be cool to have a small chat window that is accessable basically everywhere throughout the applicat
ion UI in which 'lives' a bot that can accept some input from a user and do what is requested. The pool of commands is f
inite and predefined.

**The issue**

So, putting details aside, the main issue to be solved is parsing user input (unst
ructured and possible incomplete data) to some structured form. In general, each and every user input should be transfor
med into a data structure that represents a sequence of commands with their parameters, for example:

User input: Please
, create X with param1 set to value1 and param2 equal to value2

Desired output:

    create_x --param1 value1 --param2 
value2

In this example, there is only one command, but in real life the request can represent a sequence of N commands,
 and they may depend on each other (sequence of execution does matter)

**What I've tried so far**

I have an 'experimen
t' environment: a python project with `ollama` and `langchain` installed. The main model I test is llama3.1-instruct wit
h 5bit quantization. (I'm sort of limited with hardware resourses, so XXB parameter models do not fit).

Up until now, I
've tried to achieve what I want with prompting in different forms, but in general I do the following:

As the very firs
t message in the chat, I create a 'system' one which explain what commands are there. The format is the following (I rep
laced original data not to expose the context more, so it's very generic)

    <scope>
        <models>
            <mod
el name='entityA'>
                <field name='uniqueId' type='string' description='unique identifier for entityA'/>
  
              <field name='label' type='string' description='label for entityA'/>
                <field name='category'
 type='enum' possible-value='alpha, beta, gamma, delta'/>
            </model>
            <model name='entityB'>
      
          <field name='uniqueId' description='unique identifier for entityB'/>
                <field name='entityAIds' 
type='array' description='identifiers of entityAs associated with this entityB'/>
            </model>
        </models>

        <commands>
            <command name='create_entityA' description='creates an instance of entityA'>
           
     <param name='uniqueId' type='string' description='unique identifier for entityA'/>
                <param name='lab
el' type='string' description='label for entityA' required='true'/>
                <param name='category' type='enum' p
ossible-values='alpha, beta, gamma, delta'
                       description='category of entityA (one value from the p
ossible values list)' required='true'/>
            </command>
            <command name='remove_entityA' description='r
emoves an instance of entityA by its unique identifier'>
                <param name='uniqueId' description='unique iden
tifier of the entityA to be removed'
                       required='true'/>
            </command>
            <comman
d name='create_entityB'>
                <param name='label' description='label for entityB'/>
            </command>
  
          <command name='link_entityAs_to_entityB'
                     description='associates instances of entityA wit
h a specific entityB based on the provided unique identifier of entityB'>
                <param name='uniqueId' descrip
tion='unique identifier of the entityB to which entityAs should be associated'
                       required='true'/>

                <param name='entityAIds'
                       description='an array of unique identifiers of entityAs 
to associate with the entityB'
                       type='array'
                       required='true'/>
            
</command>
            <command name='navigate' description='indicates that a user wants to go to a specific section of 
the platform'>
                <param name='section' possible-values='entitiesA, entitiesB, configuration' required='tru
e'/>
            </command>
            <command name='support' description='should be executed when a user seeks assist
ance on available functions'/>
        </commands>
    </scope>

So, now the model is provided with some context. Then, 
also in the 'system' message I:

* 'tell' the model that user input should be converted into a sequence of commands alon
g with the corresponding parameters, all of this is described in the XML above
* describe the desired output format
* tr
y to enforce some restriction and cover edge cases

**The question part**

*Is this approach* ***viable***\*?\*

If yes,
 maybe there are some ***ways to improve it***?

If not, *what would be* ***the alternative***?

So far I don't see how 
to apply fine tuning here

Thank you in advance!
```
---

     
 
all -  [ Need help with creating CLI for 'non-programmers' (LLMs) ](https://www.reddit.com/r/deeplearning/comments/1elrfgm/need_help_with_creating_cli_for_nonprogrammers/) , 2024-08-07-0911
```
***TL;DR*** What is the best way to convert user input into sequence of commands and their corresponding parameters? Lik
e, imagine you are not a programmer and there is a console app with a CLI, but, well, you don't know the structure and t
he syntax of commands. And you don't want to know. YBut! You have a locally running instance of llama3.1 -- or whatever 
open LLM is out there now -- and you can ask it to create a CLI command for you. What would you do to accomplish that?


**Intro**

A little bit of context. I'm working on a project that targets scientists as end users. It has some UI using 
which it's possible to do all sort of things the lab workers would like to do. But recently the projects product owner d
ecided that it would be cool to have a small chat window that is accessable basically everywhere throughout the applicat
ion UI in which 'lives' a bot that can accept some input from a user and do what is requested. The pool of commands is f
inite and predefined.

**The issue**

So, putting details aside, the main issue to be solved is parsing user input (unst
ructured and possible incomplete data) to some structured form. In general, each and every user input should be transfor
med into a data structure that represents a sequence of commands with their parameters, for example:

User input: Please
, create X with param1 set to value1 and param2 equal to value2

Desired output:

    create_x --param1 value1 --param2 
value2

In this example, there is only one command, but in real life the request can represent a sequence of N commands,
 and they may depend on each other (sequence of execution does matter)

**What I've tried so far**

I have an 'experimen
t' environment: a python project with `ollama` and `langchain` installed. The main model I test is llama3.1-instruct wit
h 5bit quantization. (I'm sort of limited with hardware resourses, so XXB parameter models do not fit).

Up until now, I
've tried to achieve what I want with prompting in different forms, but in general I do the following:

1. As the very f
irst message in the chat, I create a 'system' one which explain what commands are there. The format is the following (I 
replaced original data not to expose the context more, so it's very generic): 

```xml
<scope>
    <models>
        <mod
el name='entityA'>
            <field name='uniqueId' type='string' description='unique identifier for entityA'/>
      
      <field name='label' type='string' description='label for entityA'/>
            <field name='category' type='enum'
 possible-value='alpha, beta, gamma, delta'/>
        </model>
        <model name='entityB'>
            <field name='u
niqueId' description='unique identifier for entityB'/>
            <field name='entityAIds' type='array' description='id
entifiers of entityAs associated with this entityB'/>
        </model>
    </models>
    <commands>
        <command nam
e='create_entityA' description='creates an instance of entityA'>
            <param name='uniqueId' type='string' descri
ption='unique identifier for entityA'/>
            <param name='label' type='string' description='label for entityA' re
quired='true'/>
            <param name='category' type='enum' possible-values='alpha, beta, gamma, delta'
             
      description='category of entityA (one value from the possible values list)' required='true'/>
        </command>
 
       <command name='remove_entityA' description='removes an instance of entityA by its unique identifier'>
           
 <param name='uniqueId' description='unique identifier of the entityA to be removed'
                   required='true'/
>
        </command>
        <command name='create_entityB'>
            <param name='label' description='label for enti
tyB'/>
        </command>
        <command name='link_entityAs_to_entityB'
                 description='associates inst
ances of entityA with a specific entityB based on the provided unique identifier of entityB'>
            <param name='u
niqueId' description='unique identifier of the entityB to which entityAs should be associated'
                   requir
ed='true'/>
            <param name='entityAIds'
                   description='an array of unique identifiers of entit
yAs to associate with the entityB'
                   type='array'
                   required='true'/>
        </comman
d>
        <command name='navigate' description='indicates that a user wants to go to a specific section of the platform
'>
            <param name='section' possible-values='entitiesA, entitiesB, configuration' required='true'/>
        </c
ommand>
        <command name='support' description='should be executed when a user seeks assistance on available functi
ons'/>
    </commands>
</scope>
```

So, now the model is provided with some context. Then, also in the 'system' message
 I:

* 'tell' the model that user input should be converted into a sequence of commands along with the corresponding par
ameters, all of this is described in the XML above
* describe the desired output format
* try to enforce some restrictio
n and cover edge cases

**The question part**

*Is this approach* ***viable***\*?\*

If yes, maybe there are some ***way
s to improve it***?

If not, *what would be* ***the alternative***?

So far I don't see how to apply fine tuning here

T
hank you in advance!
```
---

     
 
all -  [ Need help with CLI for 'non-programmers' (LLMs, but maybe it's a wrong choice) ](https://www.reddit.com/r/neuralnetworks/comments/1elre7x/need_help_with_cli_for_nonprogrammers_llms_but/) , 2024-08-07-0911
```
***TL;DR*** What is the best way to convert user input into sequence of commands and their corresponding parameters? Lik
e, imagine you are not a programmer and there is a console app with a CLI, but, well, you don't know the structure and t
he syntax of commands. And you don't want to know. YBut! You have a locally running instance of llama3.1 -- or whatever 
open LLM is out there now -- and you can ask it to create a CLI command for you. What would you do to accomplish that?


**Intro**

A little bit of context. I'm working on a project that targets scientists as end users. It has some UI using 
which it's possible to do all sort of things the lab workers would like to do. But recently the projects product owner d
ecided that it would be cool to have a small chat window that is accessable basically everywhere throughout the applicat
ion UI in which 'lives' a bot that can accept some input from a user and do what is requested. The pool of commands is f
inite and predefined.

**The issue**

So, putting details aside, the main issue to be solved is parsing user input (unst
ructured and possible incomplete data) to some structured form. In general, each and every user input should be transfor
med into a data structure that represents a sequence of commands with their parameters, for example:

User input: Please
, create X with param1 set to value1 and param2 equal to value2

Desired output:

    create_x --param1 value1 --param2 
value2

In this example, there is only one command, but in real life the request can represent a sequence of N commands,
 and they may depend on each other (sequence of execution does matter)

**What I've tried so far**

I have an 'experimen
t' environment: a python project with `ollama` and `langchain` installed. The main model I test is llama3.1-instruct wit
h 5bit quantization. (I'm sort of limited with hardware resourses, so XXB parameter models do not fit).

Up until now, I
've tried to achieve what I want with prompting in different forms, but in general I do the following:

As the very firs
t message in the chat, I create a 'system' one which explain what commands are there. The format is the following (I rep
laced original data not to expose the context more, so it's very generic): 

```xml
<scope>
    <models>
        <model 
name='entityA'>
            <field name='uniqueId' type='string' description='unique identifier for entityA'/>
         
   <field name='label' type='string' description='label for entityA'/>
            <field name='category' type='enum' po
ssible-value='alpha, beta, gamma, delta'/>
        </model>
        <model name='entityB'>
            <field name='uniq
ueId' description='unique identifier for entityB'/>
            <field name='entityAIds' type='array' description='ident
ifiers of entityAs associated with this entityB'/>
        </model>
    </models>
    <commands>
        <command name='
create_entityA' description='creates an instance of entityA'>
            <param name='uniqueId' type='string' descripti
on='unique identifier for entityA'/>
            <param name='label' type='string' description='label for entityA' requi
red='true'/>
            <param name='category' type='enum' possible-values='alpha, beta, gamma, delta'
                
   description='category of entityA (one value from the possible values list)' required='true'/>
        </command>
    
    <command name='remove_entityA' description='removes an instance of entityA by its unique identifier'>
            <p
aram name='uniqueId' description='unique identifier of the entityA to be removed'
                   required='true'/>
 
       </command>
        <command name='create_entityB'>
            <param name='label' description='label for entityB
'/>
        </command>
        <command name='link_entityAs_to_entityB'
                 description='associates instanc
es of entityA with a specific entityB based on the provided unique identifier of entityB'>
            <param name='uniq
ueId' description='unique identifier of the entityB to which entityAs should be associated'
                   required=
'true'/>
            <param name='entityAIds'
                   description='an array of unique identifiers of entityAs
 to associate with the entityB'
                   type='array'
                   required='true'/>
        </command>

        <command name='navigate' description='indicates that a user wants to go to a specific section of the platform'>

            <param name='section' possible-values='entitiesA, entitiesB, configuration' required='true'/>
        </comm
and>
        <command name='support' description='should be executed when a user seeks assistance on available functions
'/>
    </commands>
</scope>

```

So, now the model is provided with some context. Then, also in the 'system' message I
:

* 'tell' the model that user input should be converted into a sequence of commands along with the corresponding param
eters, all of this is described in the XML above
* describe the desired output format
* try to enforce some restriction 
and cover edge cases

**The question part**

*Is this approach* ***viable***\*?\*

If yes, maybe there are some ***ways 
to improve it***?

If not, *what would be* ***the alternative***?

So far I don't see how to apply fine tuning here

Tha
nk you in advance!
```
---

     
 
all -  [ Need help with CLI for 'non-programmers' ](https://www.reddit.com/r/LLMDevs/comments/1elrd9v/need_help_with_cli_for_nonprogrammers/) , 2024-08-07-0911
```
***TL;DR*** What is the best way to convert user input into sequence of commands and their corresponding parameters? Lik
e, imagine you are not a programmer and there is a console app with a CLI, but, well, you don't know the structure and t
he syntax of commands. And you don't want to know. YBut! You have a locally running instance of llama3.1 -- or whatever 
open LLM is out there now -- and you can ask it to create a CLI command for you. What would you do to accomplish that?


**Intro**

A little bit of context. I'm working on a project that targets scientists as end users. It has some UI using 
which it's possible to do all sort of things the lab workers would like to do. But recently the projects product owner d
ecided that it would be cool to have a small chat window that is accessable basically everywhere throughout the applicat
ion UI in which 'lives' a bot that can accept some input from a user and do what is requested. The pool of commands is f
inite and predefined.

**The issue**

So, putting details aside, the main issue to be solved is parsing user input (unst
ructured and possible incomplete data) to some structured form. In general, each and every user input should be transfor
med into a data structure that represents a sequence of commands with their parameters, for example:

User input: Please
, create X with param1 set to value1 and param2 equal to value2

Desired output:

    create_x --param1 value1 --param2 
value2

In this example, there is only one command, but in real life the request can represent a sequence of N commands,
 and they may depend on each other (sequence of execution does matter)

**What I've tried so far**

I have an 'experimen
t' environment: a python project with `ollama` and `langchain` installed. The main model I test is llama3.1-instruct wit
h 5bit quantization. (I'm sort of limited with hardware resourses, so XXB parameter models do not fit).

Up until now, I
've tried to achieve what I want with prompting in different forms, but in general I do the following:

As the very firs
t message in the chat, I create a 'system' one which explain what commands are there. The format is the following (I rep
laced original data not to expose the context more, so it's very generic)

```xml
<scope>
    <models>
        <model na
me='entityA'>
            <field name='uniqueId' type='string' description='unique identifier for entityA'/>
           
 <field name='label' type='string' description='label for entityA'/>
            <field name='category' type='enum' poss
ible-value='alpha, beta, gamma, delta'/>
        </model>
        <model name='entityB'>
            <field name='unique
Id' description='unique identifier for entityB'/>
            <field name='entityAIds' type='array' description='identif
iers of entityAs associated with this entityB'/>
        </model>
    </models>
    <commands>
        <command name='cr
eate_entityA' description='creates an instance of entityA'>
            <param name='uniqueId' type='string' description
='unique identifier for entityA'/>
            <param name='label' type='string' description='label for entityA' require
d='true'/>
            <param name='category' type='enum' possible-values='alpha, beta, gamma, delta'
                  
 description='category of entityA (one value from the possible values list)' required='true'/>
        </command>
      
  <command name='remove_entityA' description='removes an instance of entityA by its unique identifier'>
            <par
am name='uniqueId' description='unique identifier of the entityA to be removed'
                   required='true'/>
   
     </command>
        <command name='create_entityB'>
            <param name='label' description='label for entityB'/
>
        </command>
        <command name='link_entityAs_to_entityB'
                 description='associates instances
 of entityA with a specific entityB based on the provided unique identifier of entityB'>
            <param name='unique
Id' description='unique identifier of the entityB to which entityAs should be associated'
                   required='t
rue'/>
            <param name='entityAIds'
                   description='an array of unique identifiers of entityAs t
o associate with the entityB'
                   type='array'
                   required='true'/>
        </command>
  
      <command name='navigate' description='indicates that a user wants to go to a specific section of the platform'>
  
          <param name='section' possible-values='entitiesA, entitiesB, configuration' required='true'/>
        </comman
d>
        <command name='support' description='should be executed when a user seeks assistance on available functions'/
>
    </commands>
</scope>
```


So, now the model is provided with some context. Then, also in the 'system' message I:


* 'tell' the model that user input should be converted into a sequence of commands along with the corresponding paramet
ers, all of this is described in the XML above
* describe the desired output format
* try to enforce some restriction an
d cover edge cases

**The question part**

*Is this approach* ***viable***\*?\*

If yes, maybe there are some ***ways to
 improve it***?

If not, *what would be* ***the alternative***?

So far I don't see how to apply fine tuning here

Thank
 you in advance!
```
---

     
 
all -  [ What is the best document loader for PDFs? And other docs in general? ](https://www.reddit.com/r/LangChain/comments/1elr7sr/what_is_the_best_document_loader_for_pdfs_and/) , 2024-08-07-0911
```
Based on some advice I got, I started using AWS Textract ($$$) for PDFs and unstructured (local/free) for all other doc 
types such as docx and html. 

My textract bill is getting a bit out of hand and I was wondering if there are any better
 services out there that can interpret things like tables and stuff from PDFs and other docs well?

Quality is my number
 one concern but cost is also important.

Looking to replace textract but also wanted to check to see if unstructured is
 still considered the best for other doc types.
```
---

     
 
all -  [ How to track number of LLM calls in a ReAct agent ](https://www.reddit.com/r/LangChain/comments/1elpms2/how_to_track_number_of_llm_calls_in_a_react_agent/) , 2024-08-07-0911
```
I'm working on a ReAct agent(created with langchain.agents.create\_react\_agent) and we are creating an evaluation and m
onitoring tool for it to analyze and understand agent behavior, performance, latency, bottlenecks, etc. We have already 
some metrics, but I'm looking for the best practices or recommended techniques to calculate:

* Number of LLM calls: giv
en the agent will do it's reasoning/acting cycle doing LLM calls internally we want to measure the number of calls.
* Du
ration per LLM call: we also want to measure the duration per call.

One of the goals is to understand where to focus wh
en doing improvements, for example: 

1. improving tools descriptions, inputs etc to reduce the number of LLM calls.
2. 
Performing model optimization and endpoint tuning to reduce latency per call.

**Note:** due to internal constraints we 
are not  using langsmith and preferably the solution should be independent of the model used(given we will evaluate diff
erent models and we want the metrics for all of them).

Any other suggested metrics are appreciated.

The question is: *
*what is the recommended way to achieve this?** (I have in mind thing like callbacks like the **on\_llm\_end** and addin
g a counter but not sure if this is the recommended way or maybe there is something out of the box).
```
---

     
 
all -  [ Large Language Models, Productivity, and Profits ](https://www.lycee.ai/blog/large-language-models-productivity-and-profits) , 2024-08-07-0911
```

```
---

     
 
all -  [ Sharing my project that was built on Langchain: An all-in-one AI that integrates the best foundation ](https://www.reddit.com/r/LangChain/comments/1ellpk9/sharing_my_project_that_was_built_on_langchain_an/) , 2024-08-07-0911
```
Hey everyone I want to share a Langchain-based project that I have been working on for the last few months — [JENOVA](ht
tps://www.jenova.ai/), an AI (similar to ChatGPT) that integrates the best foundation models and tools into one seamless
 experience.

**AI is advancing too fast for most people to follow.** New state-of-the-art models emerge constantly, eac
h with unique strengths and specialties. Currently:

* Claude 3.5 Sonnet is the best at reasoning, math, and coding.
* G
emini 1.5 Pro excels in business/financial analysis and language translations.
* Llama 3.1 405B is most performative in 
roleplaying and creativity.
* GPT-4o is most knowledgeable in areas such as art, entertainment, and travel.

This rapidl
y changing and fragmenting AI landscape is leading to the following problems for consumers:

* **Awareness Gap:** Most p
eople are unaware of the latest models and their specific strengths, and are often paying for AI (e.g. ChatGPT) that is 
suboptimal for their tasks.
* **Constant Switching:** Due to constant changes in SOTA models, consumers have to frequent
ly switch their preferred AI and subscription.
* **User Friction:** Switching AI results in significant user experience 
disruptions, such as losing chat histories or critical features such as web browsing.

JENOVA is built to solve this.

*
*When you ask JENOVA a question, it automatically routes your query to the model that can provide the optimal answer (bu
ilt on top of Langchain).** For example, if your first question is about coding, then Claude 3.5 Sonnet will respond. If
 your second question is about tourist spots in Tokyo, then GPT-4o will respond. All this happens seamlessly in the back
ground.

JENOVA's model ranking is continuously updated to incorporate the latest AI models and performance benchmarks, 
ensuring you are always using the best models for your specific needs.

In addition to the best AI models, JENOVA also p
rovides you with an expanding suite of the most useful tools, starting with:

* **Web browsing** for real-time informati
on (performs surprisingly well, nearly on par with Perplexity)
* **Multi-format document analysis** including PDF, Word,
 Excel, PowerPoint, and more
* **Image interpretation** for visual tasks

Your privacy is very important to us. Your con
versations and data are never used for training, either by us or by third-party AI providers.

Try it out at [**www.jeno
va.ai**](https://www.jenova.ai/)

**Update:** JENOVA might be running into some issues with web search/browsing right no
w due to very high demand.
```
---

     
 
all -  [ Retrieving all embeddings from an Azure Ai Search instance ](https://www.reddit.com/r/LangChain/comments/1elllb7/retrieving_all_embeddings_from_an_azure_ai_search/) , 2024-08-07-0911
```
Hi Guys,

I am working on an issue and can't seem to figure it out. I want to retrieve all the embeddings that are store
d in a Azure AI Search instance.

  
At this moment i'm trying it like this:

`# Create a SearchClient instance`

`endpo
int = SEARCH_ENDPOINT`  
`search_client = SearchClient(endpoint=endpoint, index_name=index_name, credential=AzureKeyCred
ential(api_key))`

`# Formulate a search request`  
`search_text = '*'`    
`select_fields = '*'` 

`# Execute the searc
h`  
`results = search_client.search(search_text, select=select_fields)`

`print(results)`

  
However, this return me t
he following:

{'content': 'RANDOM CONTENT',   
'metadata':   
'{'source': 'DOC SOURCE,  
 'page': 0,  
 'start\_index':
 4}',  
 'id': 'OTQ4MTUwOWYtNTFiNC00NTViLWE0MzQtNTJlYjQxZDJiMmI0',  
 '@search.score': 1.0, '@search.reranker\_score': N
one,   
'@search.highlights': None,  
'@search.captions': None}

  
However not the embeddings. Can anybody help me?
```
---

     
 
all -  [ Extracting insights from conversational transcripts ](https://www.reddit.com/r/LangChain/comments/1elldx1/extracting_insights_from_conversational/) , 2024-08-07-0911
```
I am trying to build an application that analyses all my transcripts and answer user question based on the context by pe
rforming similarity search. I am loading all my transcripts into vector database(in my case milvus) and storing them as 
embeddings, along with the metadata of the transcripts. I am using rag retrieval process to get the answer, but I didn't
 get the expected output on most cases. Any better way of doing this, any suggestions on choosing the appropriate embedd
ings and dimensions.
```
---

     
 
all -  [ II'll set up your SaaS (Landing page + Stripe, Supabase, Email/Google Auth, and Email Automation int ](https://www.reddit.com/r/SaaSIdeas/comments/1ellaxz/iill_set_up_your_saas_landing_page_stripe/) , 2024-08-07-0911
```
As the title says, if you have a SaaS idea and you are looking to make it real quick, I can help you get started. 🚀

You
’ll receive the full code of your new SaaS App. This includes:

* Landing page template that is easy to modify according
 to your needs.
* Integration with Stripe, Supabase, Email Authentication, Google Authentication, PostHog (super OP Anal
ytics platform for your website, if u haven't used this b4, why not??) 🔒📊
* If you’re building an AI application, I can 
set up a Flask backend with OpenAI and Langchain Integration.
* Tech Stack: React, Next.js, Tailwind, TS, Python, Flask 
💻

These integrations are a MUST when building your own SaaS application, and honestly, it takes so f\*\*\*ing long to s
et them up. So let me help you.

Just trying to gauge interest 🙂 DM me
```
---

     
 
all -  [ I'll set up your SaaS (Landing page + Stripe, Supabase, Email/Google Auth, and Email Automation inte ](https://www.reddit.com/r/SaaS/comments/1ell4v6/ill_set_up_your_saas_landing_page_stripe_supabase/) , 2024-08-07-0911
```
As the title says, if you have a SaaS idea and you are looking to make it real quick, I can help you get started. 🚀

You
’ll receive the full code of your new SaaS App. This includes:

• Landing page template that is easy to modify according
 to your needs. 

• Integration with Stripe, Supabase, Email Authentication, Google Authentication, PostHog (super OP An
alytics platform for your website, if u haven't used this b4, why not??) 🔒📊

• If you’re building an AI application, I c
an set up a Flask backend with OpenAI and Langchain Integration. 

• Tech Stack: React, Next.js, Tailwind, TS, Python, F
lask 💻

These integrations are a MUST when building your own SaaS application, and honestly, it takes so f\*\*\*ing long
 to set them up. So let me help you.

Just trying to gauge interest 🙂 DM me
```
---

     
 
all -  [ How To Build Your Retrieval Augmented Generation (RAG) Using Open-source Tools: LangChain, LLAMA 3,  ](https://www.reddit.com/r/LocalLLaMA/comments/1ell4fq/how_to_build_your_retrieval_augmented_generation/) , 2024-08-07-0911
```

TL;DR: RAG overcomes the limitations of LLMs by bringing in external sources of information as relevant context.  
  
A
t the end of the step-by-step tutorial, you will be able to give your favorite LLM (ChatGPT, LLAMA 3, Mixtral, Gemini, C
laude, etc.) some documents, ask it a question and see it respond based on relevant context.  
  
This will be running l
ocally, using open-source libraries. Zero API and tooling costs.

[Step-by-step Notebook with zero-cost RAG](https://cod
ecompass00.substack.com/p/build-open-source-rag-langchain-llm-llama-chroma)

*Processing img 69v6kjfj3wgd1...*


```
---

     
 
all -  [ WeaviateHybridSearchRetriever with filters? ](https://www.reddit.com/r/LangChain/comments/1elk3g2/weaviatehybridsearchretriever_with_filters/) , 2024-08-07-0911
```
I am currently building a Q&A interface with Streamlit and Langchain. Our initial vector database was in Pinecone. We ha
ve documents about the same topic, but different industries. Pure embedding search is not optimal, as it will match the 
same concepts across industries. So, we build a simple selector option where users pick their industry, and then ask the
 question. In pinecone each industry had their own namespace, we then simply filter on this:

    vectorstore = Pinecone
VectorStore(index_name=index_name, embedding=embeddings, namespace=namespace)
    
    retriever = vectorstore.as_retrie
ver(search_type='similarity', search_kwargs={'k': 3})

Hybrid search with pinecone is not as convenient as with Weaviate
, and since we noticed beter performance with hybrid search we are switching to Weaviate. The downside is that filters a
re not so clear for the Weaviate retriever. 

    retriever = WeaviateHybridSearchRetriever(
            client=client,

            index_name=WEAVIATE_INDEX_NAME,
            text_key='page_content',
            k=5,
            alpha=0.75
,
            attributes=['file_name', 'industry],
            create_schema_if_missing=False,
        )

Our Langchain 
Chain looks similar to this ( [https://github.com/langchain-ai/langchain/blob/master/templates/hybrid-search-weaviate/hy
brid\_search\_weaviate/chain.py](https://github.com/langchain-ai/langchain/blob/master/templates/hybrid-search-weaviate/
hybrid_search_weaviate/chain.py) ):

    # RAG prompt
    template = '''Answer the question based only on the following 
context:
    {context}
    Question: {question}
    '''
    prompt = ChatPromptTemplate.from_template(template)
    
   
 # RAG
    model = ChatOpenAI()
    chain = (
        RunnableParallel({'context': retriever, 'question': RunnablePassth
rough()})
        | prompt
        | model
        | StrOutputParser()
    )

The docs do show this:

    retriever.invo
ke(
        'AI integration in society',
        where_filter={
            'path': ['author'],
            'operator': 
'Equal',
            'valueString': 'Prof. Jonathan K. Sterling',
        },
    )

[https://python.langchain.com/v0.2/d
ocs/integrations/retrievers/weaviate-hybrid/](https://python.langchain.com/v0.2/docs/integrations/retrievers/weaviate-hy
brid/)

Does anyone know how/where to add the `where_filter` parameter for Weaviate hybrid search in the Chain?

[](http
s://github.com/langchain-ai/langchain/blob/master/templates/hybrid-search-weaviate/hybrid_search_weaviate/chain.py)
```
---

     
 
all -  [ Help Desk RAG Documentation New Link? [LangGraph] ](https://www.reddit.com/r/LangChain/comments/1elilnx/help_desk_rag_documentation_new_link_langgraph/) , 2024-08-07-0911
```
I've been keeping my eye on the LangGraph documentation, there was one titled 'Help Desk RAG' or 'Make a Help Desk Agent
 with RAG' or something. This was back when the documentation also showed a 'Design Patterns' category for the graphs.




I'm finally ready to start the tutorial but it has all but vanished. I only see about 6 other RAG based links. All of 
which are long, and with names that don't really indicate the differences. (Corrective RAG, Self-RAG, Agentic RAG...)

 
 
I may end up spending the time diving into them all eventually, but would anyone know which one specifically used to b
e the 'Help Desk RAG'?
```
---

     
 
all -  [ Multimodal AI Assistant Integrated with WhatsApp ](https://www.reddit.com/r/betatests/comments/1elibnc/multimodal_ai_assistant_integrated_with_whatsapp/) , 2024-08-07-0911
```
Hey fellow tech enthusiasts !

I made an AI assistant integrated with WhatsApp, using Langchain and a combination of fun
ctions and tools. Let me introduce to you, Simone !

My objective is to make AI seamlessly integrated to our daily life,
 including those that are not even interested in downloading the OpenAI, Claude or any other AI apps. That's why I've go
ne in favor of a WhatsApp integration, which allows for seamless incorporation into daily life.

Users can interact with
 Simone as they would with any contact, making AI assistance feel more natural and accessible. I realized that myself, a
 developer and tech-oriented user, find it very enjoyable.

Key Features:

* Multilingual support
* Voice message capabi
lity (text-to-speech and speech-to-text)
* Web search and content summarization
* Image analysis and generation
* Locati
on-based services (directions, place info)
* PDF and YouTube transcript reading

I'm particularly interested in hearing 
about:

* How the WhatsApp integration affects user experience: Is it a positive or negative point for you?
* The useful
ness of different features in day-to-day scenarios: What would you use it for?
* Performance, response time and hallucin
ations: If you tried it, did you like it?
* Privacy concerns and how we might address them: Would you feel comfortable d
iscussing any issues you may have with such a bot?
* Do you think it may be of any use for you or one of your friends?
*
 What features would make you consider using an AI assistant through WhatsApp?
* I want Simone to feel 'human-like' but 
I had mixed feedback on that side. What are your thoughts?

I'm after genuine opinions to help refine and improve Simone
. All feedback, positive or critical, is valuable.

For those of you that want to try it, just ask in comments and I'll 
share the link/WhatsApp number.

I spend several hours outside every day handing out flyers to people and asking for the
ir opinion. I hope it will be less painful through Reddit 😅

Thanks for your insights!

# How can I try it?

* Visit [Si
mone.app](http://Simone.app) to get more information
* OR Send a WhatsApp Message to +33 7 66 25 95 58

No registration 
needed.
```
---

     
 
all -  [ Run local LLM on CPU. how Bad would would it be compared to GPUs ](https://www.reddit.com/r/LangChain/comments/1eli67w/run_local_llm_on_cpu_how_bad_would_would_it_be/) , 2024-08-07-0911
```
I wanted to ask, if I want to run local LLMs only on CPU.

I do not have access to GPUs and wanted to ask how much slowe
r CPU would be, compared to GPU.

I would love to run a small Open Source LLM only on CPUs to read 500 pages PDFs and be
 able to ask it questions.


```
---

     
 
all -  [ LLM answer to the question  -  context for answer did not even provide ](https://www.reddit.com/r/LangChain/comments/1eli48o/llm_answer_to_the_question_context_for_answer_did/) , 2024-08-07-0911
```
My application logic is - i give some text from database, and using this context generated answer.But if i ask something
 but its dont exist in context - LLm still answer me. Why?.Here my code  

    const prompt = await pull<ChatPromptTempl
ate>('rlm/rag-prompt');
    
      const ragChain = await createStuffDocumentsChain({
        llm,
        prompt:prompt
,
        outputParser: parcer,
      });
      const stream = await ragChain.stream({
        question:question,
      
  context: [
          new Document({
            pageContent: text as string,
          }),
        ],
      });
    
```
---

     
 
all -  [ Beginner: Advice on Extremely Ambitious Agent-Based Long-Horizon Storytelling ](https://www.reddit.com/r/LangChain/comments/1eli34m/beginner_advice_on_extremely_ambitious_agentbased/) , 2024-08-07-0911
```
**Context:** I have an ambitious idea about using agents for long-horizon text-only storytelling but have limited techni
cal knowledge. I hope more experienced individuals can offer input on feasibility and potential challenges.

**Project O
verview:** My goal is to create very detailed, long form AI roleplaying software where users aren't just reading a novel
, they are the protagonist. In my experience, AI can produce passable prose (Claude 3.5), but it struggles with story pr
ogression and planning, often resulting in circular narratives. To address this, I plan to use agents to create a detail
ed plot outline based on a user-supplied premise. The AI will narrate, and the user will act as the protagonist. Every t
ime the protagonist acts, the AI will follow a series of escalating questions to assess and rewrite the outline as neede
d to keep the story cohesive:

1. Does this fit with the next planned beat? If yes, the writer AI continues; if not,
2. 
Does this fit with the scene? If yes, rewrite the beat; if not,
3. Does this fit with the chapter outline? If yes, rewri
te the scene and beat; if not,
4. Does this fit with the arc?

This way, the story always has an outline to stay on trac
k but can pivot as needed based on the protagonist's actions.

**Assumptions:**

1. Using a series of repeating agents, 
AI can generate and refine variations of a user-supplied premise into hyper-specific instructions. AI-written content of
ten lacks specificity, which I plan to address through careful prompting and QA agents.
2. I can break up the long horiz
on task of impromptu novel writing (AI roleplaying) into discrete chunks I can hand off to specific agents that will onl
y see their little section of the walled garden. This feels risky because different sections might need to know about ea
ch other to be cohesive and it could be hard to predict what that shared knowledge pool might need to be without making 
it so large the cost and wait time balloon beyond toleration.
3. That this won’t run afoul of the bitter lesson - where 
I have to get so granular I stray into deterministic logic which is inherently limiting and better solved with waiting f
or GPT-4.5.
4. I can get the response time from user input to the next beat written to a tolerable experience. I plan to
 make what I can run concurrently and use a bag of tricks to lessen the perceived waiting time.

The plot outline to kee
p things on track is table stakes for me. My real goal is far more ambitious (and far-fetched) about making the characte
rs come alive:

* Give all / many of the characters encountered their own AI which fully fleshes out their backstory, go
als, personality, outlook, relationships with other AI characters, and gives them agency to pursue those minor/major goa
ls as the book unfolds. The events other characters set in motion will be experienced by the protagonist whether it’s br
eaking and entering or being crabby in a conversation because they get hangry and it’s lunch time.
* Create true repercu
ssions for actions the protagonist or other characters take. If the protagonist as a student is rude, the AI controlling
 the teacher will assign detention, the unpleasantness determined by the AI of the teacher administering the detention 


I know a tiny amount of code (enough to hard code Towers of Hanoi in terminal) and with AI’s help, have Open Router hoo
ked up to a local python program in VS Code where it writes to a local document. I plan to create tons of little documen
ts the agents will write/read to. In my day job I work at a startup as a UX designer, have lots of  senior engineering F
AANG friends and have played extensively with AI, particularly with storytelling including programs like Sudowrite and N
ovelcrafter. 

I haven’t yet messed with agents. What do you predict will be the hardest parts of this project and what 
are the odds of success? I suspect the programming will be simple, the prompting will be finicky, the lag challenging an
d the cost fairly high even with GPT-4o mini. Even if I succeed, the output will probably be average until GPT-4.5 comes
 along.
```
---

     
 
all -  [ [0 YoE, Unemployed, Machine Learning Engineer/Data Analyst/Data Scientist, Europe] ](https://www.reddit.com/r/resumes/comments/1elh46a/0_yoe_unemployed_machine_learning_engineerdata/) , 2024-08-07-0911
```
It's my first resume and my only experience is the contracts and gigs I got from Upwork. Most of my experience is relate
d to ml eng./data analytics and I don't know what's wrong with my resume. Any help is  appreciated, thanks.

https://pre
view.redd.it/gdve8o26k1hd1.png?width=1656&format=png&auto=webp&s=e1088df17a4b2e432295dce907908c06e73c7d2a

  

```
---

     
 
all -  [ Intermittent Human Interaction Is Missing ](https://www.reddit.com/r/crewai/comments/1elf90o/intermittent_human_interaction_is_missing/) , 2024-08-07-0911
```
Crewai agents are able to gather feedbacks from human only once at the end. It's incompatible to handle langchain's huma
n input with the retrieval tools. Has anyone worked on this already?
```
---

     
 
all -  [ Internship oppurtunity for 2nd/3rd year students in LLM domain ](https://www.reddit.com/r/developersIndia/comments/1elf8pd/internship_oppurtunity_for_2nd3rd_year_students/) , 2024-08-07-0911
```
Hey guys
My company is in need for interns who can actively work in LLM and SLM based projects.
Tech stack required: Pyt
hon, Tensorflow, Langchain/Llamaindex
The candidate should able to use open source models and fine-tune them
Anyone inte
rested can put in their questions in the comment section or ping me. 

Location: Work From Home(If you are in Pune, you 
can come to the office as well)
Work experience: Fresher

*This is an unpaid internship hence perfect for students who a
re still studying*
```
---

     
 
all -  [ create_sql_agent VS create_react_agent ](https://www.reddit.com/r/LangChain/comments/1eldqp7/create_sql_agent_vs_create_react_agent/) , 2024-08-07-0911
```
I've been building an SQLagent-based chatbot, testing and prototyping with langserve. I've obtained pretty good results 
and the interaction with the database and query production tasks work surprisingly well. Now, I'm about to upgrade to mu
lti-agent to include some RAG functionalities and being able to produce more comprehensive answers and to help users int
egrate information from docs etc. For that I will probably using langgraph.

Up to this point, I've been using the langc
hain SQLAgent, which works pretty well considering that it handles all in one the sql dialect, the prompt construction a
nd the tools.

Yesterday though, starting to design the langgraph upgrade, I found out that the new langchain docs now s
uggest to build SQLagents from scratch using langgraph, through 'create\_react\_agent' and including the sql toolkit, wh
ich to me looks like a less intuitive way compared to SQLAgent, adding extra steps to the process and messing up the old
 prompt building approach (the react\_agent takes in input only llm, tools and messages\_modifier, which is a simple Sys
temMessage, and the db is passed to the SQLDatabaseToolkit. To me this is way less intuitive than just having an sql\_ag
ent that takes llm, db and an actual full prompt template).

Is there a reason for this? Why did they change the documen
tations and tutorials from create\_sql\_agent to this new approach? Is it worth it to make the change if I'm going to ov
erall switch to a langgraph-based design or will I be ok integrating the 'old' SQLAgent?
```
---

     
 
all -  [ Automation?? ](https://www.reddit.com/r/LangChain/comments/1eldor2/automation/) , 2024-08-07-0911
```
I know it's not right place to ask, but I need some suggestions from people who have worked with automation thing. My ma
nager assigned me a task to fetch all the data from a website. I know to write a simple web scraper. But, first we have 
to log into their website. So, they suggested me to do automating website. I tried to write selenium in python. But, thi
s has to be hosted on server and the data from the website should be accessed via an API call. Every time I run selenium
 code, It opens an instance of browser and performing automation. Is there any other way to handle this without opening 
a browser? I think this should be hosted on EC2 instance?? 
```
---

     
 
all -  [ increase number of retrieved docs ](https://www.reddit.com/r/LangChain/comments/1eld8ep/increase_number_of_retrieved_docs/) , 2024-08-07-0911
```
hi guys, I want to do the retrieval part in my rag without a limit on the K. so it can answer such questions, how many t
imes X appears for example. what is the best approach? I tried increasing the k to the total number of documents but it 
gave me a lot of irrelevant documents. and the vectorstore.as\_retriver() always return 4 docs only
```
---

     
 
all -  [ Customer review analysis Ai Agent ](https://www.reddit.com/r/LangChain/comments/1elcgt3/customer_review_analysis_ai_agent/) , 2024-08-07-0911
```
https://preview.redd.it/bb6kdv6oh0hd1.jpg?width=974&format=pjpg&auto=webp&s=078ba4f7babb1c827c9cb413fa236fc9d1cd5c2f

  

This [\~agent\~](https://app.smythos.com/builder?templateId=customer-review-analysis-lxxqii7231.smyth) uses sentiment a
nalysis and an LLM to automatically review and give responses to customer reviews. When the agent receives the customer 
review, it is first taken through sentiment analysis to understand the sentiment of the feedback. Together with the sent
iment for context, the review is sent to the LLM which crafts an appropriate response for the review.

Personally, I thi
nk the secret lies in the prompting of the LLM, in my case I set up the LLM to do 3 things mainly, 

1. Empathize with t
he customer
2. Offer a solution
3. Provide additional information

These three gave me some pretty decent results, you c
an try your own or just use these on the template, but I still think that with more robust prompting, the agent can prod
uce more natural and efficient responses that can help out your brand in a huge way.  

```
---

     
 
all -  [ Deprecated pydantic library is not working for RAG pipeline development ](https://www.reddit.com/gallery/1elbugn) , 2024-08-07-0911
```
I am new to langflow and langchain. Running the new ollama- llama3.1 locally on my machine. The error is in the main.py 
file of pydantic and states that the existing json, fields and other such are deprecated. As a result, i am unable to ru
n the model for my task. Please help😿

```
---

     
 
all -  [ Issue while trying to create index with error The request is invalid. Details: An unexpected 'StartA ](https://www.reddit.com/r/LangChain/comments/1elbo4f/issue_while_trying_to_create_index_with_error_the/) , 2024-08-07-0911
```
index\_name = f'vs\_spn\_chatrules'

search\_client = SearchClient(  
endpoint=service\_endpoint,  
index\_name=index\_n
ame,  
credential=cognitive\_search\_credential,  
)

# Creating an Azure AI Search Vector Store

vector\_store = AzureA
ISearchVectorStore(  
search\_or\_index\_client=index\_client,  
filterable\_metadata\_field\_keys=metadata\_fields,  
i
ndex\_name=index\_name,  
index\_management=IndexManagement.CREATE\_IF\_NOT\_EXISTS,  
id\_field\_key='id',  
chunk\_fie
ld\_key='chunk', #content  
embedding\_field\_key='embedding', #content\_vector  
embedding\_dimensionality=1536,  
meta
data\_string\_field\_key='metadata',  
doc\_id\_field\_key='doc\_id',  
language\_analyzer='en.lucene',  
vector\_algori
thm\_type='exhaustiveKnn', #HNSW focuses on approximate methods for efficiency, KNN ensures exactness through exhaustive
 searches.  
)

Settings.llm = llm  
Settings.embed\_model = embed\_model

storage\_context = StorageContext.from\_defau
lts(vector\_store=vector\_store)

# VectorStoreIndex.from_documents

index = VectorStoreIndex.from\_documents(  
all\_do
cs, storage\_context=storage\_context  
)

all\_docs is a list of documents with document metadata and documents

while 
im trying to create index its gives error

HttpResponseError: () The request is invalid. Details: An unexpected 'StartAr
ray' node was found when reading from the JSON reader. A 'PrimitiveValue' node was expected.  
Code:  
Message: The requ
est is invalid. Details: An unexpected 'StartArray' node was found when reading from the JSON reader. A 'PrimitiveValue'
 node was expected.

anyone faced this
```
---

     
 
all -  [ Looking for low-code tools for building and optimizing RAG ](https://www.reddit.com/r/LangChain/comments/1elarmg/looking_for_lowcode_tools_for_building_and/) , 2024-08-07-0911
```
Hello everyone, I'm looking for a low-code platform to implement RAG in business processes. I've tested tools like Dify,
 RAGflow, Flowise, and langflow, but none of them seem to be well-optimized for RAG. Does anyone know of any low-code pl
atforms that offer better RAG parameter optimization? Thanks in advance!
```
---

     
 
all -  [ LangChain in your Pocket completes 6 months !! ](https://www.reddit.com/r/LangChain/comments/1el7jc9/langchain_in_your_pocket_completes_6_months/) , 2024-08-07-0911
```
I'm glad to share that my debut book, **'LangChain in your Pocket: Beginner's Guide to Building Generative AI Applicatio
ns using LLMs**' completed 6 months last week and what a dream run it has been.

1. The book has been **republished by P
ackt.** And is now available with all major publishers including O'Reilly.
2. So far, the book has sold over **500 copie
s**.
3. It is the **highest-rated book on LangChain** on Amazon (Amazon.in: 4.7; Amazon.com: 4.3 ).

The best part is th
at the book hasn't received a bad review regarding the content from anyone, making this even more special for me

>*A bi
g thanks to the community for all the support.*

https://preview.redd.it/7wtmrl2nnygd1.png?width=901&format=png&auto=web
p&s=da3d9b2ea43d771ee738bcbb611c6331a36ef580


```
---

     
 
all -  [ Denser Retriever Recognized in LangChain Posts ](https://www.reddit.com/r/DenserRetriever/comments/1el1jdd/denser_retriever_recognized_in_langchain_posts/) , 2024-08-07-0911
```
🎉 Excited to share that our Denser Retriever project has been featured in [LangChain Posts](https://www.linkedin.com/pos
ts/langchain_denser-retriever-an-enterprise-grade-ai-activity-7225968746526298112-h0tv?utm_source=share&utm_medium=membe
r_desktop)! A huge thank you to the LangChain team for the recognition. Explore the possibilities of advanced retrieval 
with [Denser Retriever](https://github.com/denser-org/denser-retriever). Happy retrieving! 🚀
```
---

     
 
all -  [ Need advice on how to negotiate or how to approach this matter with manager ](https://www.reddit.com/r/developersIndia/comments/1ekvbko/need_advice_on_how_to_negotiate_or_how_to/) , 2024-08-07-0911
```
I was hired as an AI Tester. I have worked with Langchain and Langsmith during my internship and was hired as an AI Test
er for the same project. I was told that one of the senior tester would be there to help and guide me for the first few 
months until I got used to the work. However 1 week after I joined. The senior tester is leaving for a better offer. 

M
y manager wants me get KT in 2 months from him and continue all the works he has been doing.

I told him I'm a fresher w
ith only 1 yr experience that too as intern. I will not be able to do it on my own. And that I would need some guidance.
 

I told him I could manage for a few months as there are a lot of backlog stories and I know how to do them. But compl
eting the whole automated framework for the project would be impossible on my own.

He is not expecting to hire anyone e
lse as there is a hiring freeze going on. 

He said he would try for someone internally but I don't think it'll really h
appen soon and I'll be expected to be completing stories in the mean time.

Also would like to negotiate salary or anyth
ing that can be improved since I'll be doing a lot more work than I was expecting. Currently my salary is 10LPA+1L perfo
rmances bonus. It was fair when I was joining. But with all these extra work I'll be getting. I would like to get an inc
rement. Feb is usually when our company gives us hikes. But would be possible to get a early hike? 

Also any other sugg
estions or concerns related to this. Please let me know
```
---

     
 
all -  [ Upcoming junior wanting to switch to diff company and hopefully aim for ML internship (I don’t have  ](https://i.redd.it/6fg5iws61wgd1.jpeg) , 2024-08-07-0911
```
How can I make my resume good for when applying to an ML role? I already have SWE experience. My dream: ML at NVIDIA/Met
a. Also planning on going to Grad school if even an opportunity 

```
---

     
 
all -  [ LangChain ChatModel in Autogen ](https://www.reddit.com/r/AutoGenAI/comments/1ekuxc4/langchain_chatmodel_in_autogen/) , 2024-08-07-0911
```
Hello experts I am currently working on a use case where I need to showcase a multi agent framework in Autogen, where mu
ltiple LLM models are being used.
For example Agent1 uses LangChain AzureChatModel, Agent2 uses LangChain OCIGenAiChatMo
del , Agent3 uses LangChain NvidiaChatModel. Is it possible to use LangChain LLM to power a Autogen agent? Any leads wou
ld be great.
```
---

     
 
all -  [ What skills to learn to get a job working with LLMs? ](https://www.reddit.com/r/LocalLLaMA/comments/1ekuu85/what_skills_to_learn_to_get_a_job_working_with/) , 2024-08-07-0911
```
I have just graduated from Computing at university and I have some experience with LLMs. I have studied the theory of th
e transformer and done practical work with Hugging Face and Llama Index and a bit with Langchain. I'm not an expert in a
ny of these but I'd like to know what skills are desireable for employers and start ups. Do I just get really good at Hu
gging Face? Or LangChain? Or both? Or something else? If so, how do you recommend I do this?
```
---

     
 
all -  [ Issues with the embedding or chroma. r/MLQuestions  r/LearnMachineLearning. ](https://www.reddit.com/r/MLQuestions/comments/1ekt6rt/issues_with_the_embedding_or_chroma_rmlquestions/) , 2024-08-07-0911
```
    def generate_response(prompt, model_name, db):
        chat_model = ChatOllama(model=model_name)
        cache = loa
d_cache(model_name)
        if prompt in cache:
            return cache[prompt]
        try:
            context = db.s
imilarity_search(prompt, k=3)
            if not context:
                return 'No relevant documents found.'
        
    context_text = '\n\n'.join([doc.page_content for doc in context])
            full_context = f'Based on the followin
g documents:\n{context_text}\n\nAnswer the question: {prompt}'
            response = chat_model.predict(full_context)  

            cache[prompt] = response
            save_cache(model_name, cache)
            return response
        exce
pt Exception as e:
            return f'Error occurred: {e}'
    
    def main():
        model_name = 'mistral'
       
 embeddings = HuggingFaceEmbeddings(model_name=EMBEDDINGS_MODEL_NAME)
        def embed_query(query):
            return
 embeddings.embed([query])[0]
        db = Chroma(persist_directory=PERSIST_DIRECTORY, embedding_function=embed_query)
 
       while True:
            prompt = input('Enter a query (or type 'exit' to quit): ')
            if prompt.lower() 
== 'exit':
                break
            response = generate_response(prompt, model_name, db)
            print('Mod
el response:')
            display_letter_by_letter(response)

Error = if key in self.model\_fields:

AttributeError: 'C
ollection' object has no attribute 'model\_fields'

i tried updating the langchain library and chroma also huggingface b
ut I only get the errors. Is there any other class which his in embedding and fetching the vector datasets from my folde
r.
```
---

     
 
all -  [ Whisper-Medusa: uses multiple decoding heads for 1.5X speedup ](https://www.reddit.com/r/LangChain/comments/1eks2cm/whispermedusa_uses_multiple_decoding_heads_for/) , 2024-08-07-0911
```
Post by an AI researcher describing how their team made a modification to OpenAI’s Whisper model architecture that resul
ts in a 1.5x increase in speed with comparable accuracy. The improvement is achieved using a multi-head attention mechan
ism (hence Medusa). The post gives an overview of Whisper's architecture and a detailed explanation of the method used t
o achieve the increase in speed:

[https://medium.com/@sgl.yael/whisper-medusa-using-multiple-decoding-heads-to-achieve-
1-5x-speedup-7344348ef89b](https://medium.com/@sgl.yael/whisper-medusa-using-multiple-decoding-heads-to-achieve-1-5x-spe
edup-7344348ef89b)
```
---

     
 
all -  [ LangGraph fan-out UI ](https://www.reddit.com/r/LangChain/comments/1ekr1de/langgraph_fanout_ui/) , 2024-08-07-0911
```
So LangGraph can execute nodes in parallel via fan-out. For example: Select topics -> research each -> ...  
What's a go
od way to visualize this in a UI? Can be tricky in a 1-dimensional, linear chat interface, but also generally if there a
re multiple steps running in parallel.

[fan-out in gotoHuman](https://reddit.com/link/1ekr1de/video/3z2zywmt7vgd1/playe
r)

We are using these tabs for now, but maybe people have come up with smarter solutions already?!  
(Code is [here](ht
tps://github.com/gotohuman/gth-demo-fanout-content-creator))  

```
---

     
 
all -  [ How to pass data from database to Langchain like context/source  ](https://www.reddit.com/r/LangChain/comments/1ekql8w/how_to_pass_data_from_database_to_langchain_like/) , 2024-08-07-0911
```
I build my own RAG application but have a trouble, Logic my app is  - user push button and load some document(text), aft
er this i generate embeddings using this document and write its to database,i use Convex. And i want get this embedding 
from this  document on database and add to llm to generate answer. But i dont find any example how do this, find only ex
ample how use ConvexVectoreStore and transform it to retriver - but in my case its dont work(i have several reason). I n
eed just use embedding from document and pass to context and i dont know how and langchain document/discord dont give me
 answer. Chat bot in langchain site recomend me create CustomRetriever class - but why doc dont have answer, Pls help me

```
---

     
 
all -  [ how can we configure langchain to handle both SQL and Generic response? ](https://www.reddit.com/r/LangChain/comments/1eknw12/how_can_we_configure_langchain_to_handle_both_sql/) , 2024-08-07-0911
```
I'm using LangChain in my LLM to execute SQL query based on the input, now the issue is it doesn't handing well in the g
eneric response like for Hi, How are you or something like this. Now how can we configure langchain to handle these?
```
---

     
 
MachineLearning -  [ [R] [D] Langchain Evaluation with BeyondLLM
 ](https://www.reddit.com/r/MachineLearning/comments/1eki1fv/r_d_langchain_evaluation_with_beyondllm/) , 2024-08-07-0911
```
Hey everyone! Just came across a new feature of Beyond LLM that can evaluate Langchain RAG pipelines! It provides contex
t relevancy, answer relevancy, and groundedness. Check out the code snippet I’m sharing—perfect for testing your RAG pip
elines! For more info, be sure to check it out on GitHub [here](https://github.com/aiplanethub/beyondllm/blob/main/cookb
ook/evaluate_langchain_rag_pipeline_beyondllm.ipynb).

https://preview.redd.it/172m1y3dvsgd1.png?width=3972&format=png&a
uto=webp&s=63d5b0f41f0e46a58e7a2d5fb0d2bbc4384b3b1d


```
---

     
 
MachineLearning -  [ [D] Embedding generation in production? How are you doing it? ](https://www.reddit.com/r/MachineLearning/comments/1e7xt6k/d_embedding_generation_in_production_how_are_you/) , 2024-08-07-0911
```


For those building production RAG pipelines, how are you generating embeddings. More than which model, I'm interested 
in how your deploying it. Are you calling the openai/vertex API endpoint directly? Using langchain/llamaindex wrappers? 
Using vectordb  classes? Or some other way?
```
---

     
 
MachineLearning -  [ [D] Is Anyone Else Setting Up Real-Time Django Workers for their AI Application? What's the best way ](https://www.reddit.com/r/MachineLearning/comments/1e0qens/d_is_anyone_else_setting_up_realtime_django/) , 2024-08-07-0911
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

     
 
MachineLearning -  [ [P] Real Time AI Workers Web Application ](https://www.reddit.com/r/MachineLearning/comments/1dzryk9/p_real_time_ai_workers_web_application/) , 2024-08-07-0911
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

     
