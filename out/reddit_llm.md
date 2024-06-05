 
all -  [ Using LangChain on Cloudflare ](https://www.reddit.com/r/CloudFlare/comments/1d8cnr0/using_langchain_on_cloudflare/) , 2024-06-05-0953
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

     
 
all -  [ Struggling with Pinecone Retrieval Performance? Need Help with LCEL Chains! ](https://www.reddit.com/r/LangChain/comments/1d8b1k5/struggling_with_pinecone_retrieval_performance/) , 2024-06-05-0953
```
Hey, I have a Pinecone namespace with multiple documents, but as the number of documents increases, my retrieval perform
ance is getting worse. I’m thinking of creating multiple retrievers that filter by document name to get relevant chunks 
from each document. I'm struggling to create an LCEL chain to achieve this. Does anyone know how to do this?
```
---

     
 
all -  [ Roast my Resume ](https://i.redd.it/hpyb45p7tl4d1.jpeg) , 2024-06-05-0953
```
While you are at it, if someone has any genuine suggestions, please let me know!
```
---

     
 
all -  [ Open-source low code platform to build and coordinate multi-agent teams ](https://v.redd.it/dzjs6k5szk4d1) , 2024-06-05-0953
```

```
---

     
 
all -  [ RAG as a APA direct text quotes generator  ](https://www.reddit.com/r/LangChain/comments/1d81hl4/rag_as_a_apa_direct_text_quotes_generator/) , 2024-06-05-0953
```
Hello, I have been working on a project that involves using langchain and RAG to write direct text quotes based on sourc
ed texts.

The main objective is to create a vector database with PDF files from Google Academic and then utilize them t
o generate a user-requested text in APA format, which will output a paragraph containing direct text quotes.

For this p
roject, I have been using langchain, local llm (phi3 and llama3 with ollama or llm studio), as well as Chat GPT 4 and Gr
oq.

Unfortunately, I have encountered some difficulties as the models don't seem to follow the instructions, especially
 when it comes to using direct text quotes, even when I include instructions on how to format them in APA style.

Theref
ore, I would appreciate any ideas or suggestions from the community on how I could achieve the desired result.

Thank yo
u.
```
---

     
 
all -  [ Advice for building app with local LLM and custom logic ](https://www.reddit.com/r/LocalLLaMA/comments/1d802kg/advice_for_building_app_with_local_llm_and_custom/) , 2024-06-05-0953
```
https://preview.redd.it/ehkpb8yhik4d1.png?width=750&format=png&auto=webp&s=4f50b30e425a2deba540b3405f31b9abd7858c69

Hi 
everyone,

I'm working on a system to integrate a tutor/assistant in Jupyter notebooks. My main issue right now is how t
o add some logic between the LLM and the chat interface: I want to store the conversations, provide real-time context fr
om the notebook or from an assignment to the agent using system prompts, etc.

Currently, I use [Jupyter-ai](https://jup
yter-ai.readthedocs.io/en/latest/), which seamlessly adds a chat interface (and several other [magical ](https://jupyter
-ai.readthedocs.io/en/latest/users/index.html#the-ai-and-ai-magic-commands)things) to a Jupyter Notebook. On the LLM sid
e, I'm using Ollama (via docker) running `codellama`. With Jupiter-ai, you can choose from multiple models (from Anthrop
ic, OpenAI, HF, etc.); the [trick ](https://github.com/jupyterlab/jupyter-ai/pull/646)is that you can choose a model fro
m OpenAI, let's say `gpt-4,` and change the base URL to the one of Ollama (`localhost:11434/v1`), then in Ollama, copy `
codellama` to a new model just *named* `gpt-4` and run that, so Jupyter-ai *thinks* it's using that.

So, can I do this 
with Ollama? Should I be using something like kcpp or lcpp? Or can I use LangChain and Python to create a REST API that 
is also like OpenAI API, so I can keep using Jupyter-ai? I'd prefer to keep it as simple as posible.

Thanks!
```
---

     
 
all -  [ PostgresVectorStore vs SupabaseVectorStore ](https://www.reddit.com/r/LangChain/comments/1d7y2ue/postgresvectorstore_vs_supabasevectorstore/) , 2024-06-05-0953
```
I am using the managed postgres DB by supabase to store my embeddings and so far I have used the PGVector provided by la
ngchain: [https://python.langchain.com/v0.2/docs/integrations/vectorstores/pgvector/](https://python.langchain.com/v0.2/
docs/integrations/vectorstores/pgvector/)

I see that langchain also provides a vectorstore class specfically tailored t
o supabase: [https://python.langchain.com/v0.2/docs/integrations/vectorstores/supabase/](https://python.langchain.com/v0
.2/docs/integrations/vectorstores/supabase/)

But I can't tell what seems to be the difference except that instead of pa
ssing my Postgres Connection Env variables, I just simply instantiate a client. Is that all that is to it?

Does anyone 
know?
```
---

     
 
all -  [ Anyone implemented GraphCypherQAChain with memory? ](https://www.reddit.com/r/LangChain/comments/1d7uq7p/anyone_implemented_graphcypherqachain_with_memory/) , 2024-06-05-0953
```
I am trying to use `GraphCypherQAChain` with memory,

when I don't use `return_intermediate_steps = False` I am getting 
result, but when its true I am getting the error

Another scenario is when I give the output\_key as intermediate\_steps
, it works, but I need the result, so I have given the `out_put key` as result but then I am getting key error? -  `retu
rn inputs[prompt_input_key], outputs[output_key] KeyError: 'result'`

i need both `result`  and `intermediate_steps`

An
y one implemented this?

any help will be great!!
```
---

     
 
all -  [ Can we deploy a LangGraph graph as an api endpoint with LangServe? ](https://www.reddit.com/r/LangChain/comments/1d7nr29/can_we_deploy_a_langgraph_graph_as_an_api/) , 2024-06-05-0953
```
I'm a bit confused with the class of a graph object, from the LangServe overview page it says we can deploy runnables an
d chains as a rest API, so can we deploy langgraph?

If so, how should I config the Input class when I add\_route? the q
uestion I have is, I am using the checkpointer for memory, so do I need to add a thread\_id into the Input class for the
 client to call the API? I'm asking because to invoke the graph, we pass the thread\_id in the second argument as a conf
ig dictionary, separate from the message, so I'm not sure how this works when we add\_route.
```
---

     
 
all -  [ Does a service exist that allows you to upload documents to a RAG and share the chatbot with others? ](https://www.reddit.com/r/LangChain/comments/1d7nf63/does_a_service_exist_that_allows_you_to_upload/) , 2024-06-05-0953
```
Let's say I am a teacher, and I want my students to be able to interact with all the course material available. Is there
 a service that allows me to upload documents to a langchain chatbot and share it with others without having to host the
 chatbot myself?
```
---

     
 
all -  [ Langchain/Pinecone in Node.JS ](https://www.reddit.com/r/LangChain/comments/1d7m4i0/langchainpinecone_in_nodejs/) , 2024-06-05-0953
```
Has anyone gotten langchain/pinecone running in Node.JS? I have seen a lot of examples and some fully developed github r
epositories showing a RAG implementation in Node, but none of them work. I'm following the examples exactly, but cannot 
get many of the imports to work, such as:

import { OpenAIEmbeddings } from 'langchain/embeddings';

import { PineconeSt
ore } from 'langchain/vectorstores';

If the answer is NO, what is the best way to do the implementation with Python but
 write my server in Node.js? 

  
Thanks
```
---

     
 
all -  [ search error mystery solved (but others emerge) ](https://www.reddit.com/r/crewai/comments/1d7i514/search_error_mystery_solved_but_others_emerge/) , 2024-06-05-0953
```
Although this may be common knowledge to many here, it was eye-opening and a bit disappointing to me.

I was getting man
y `I encountered an error while trying to use the tool.` errors when using ANY search tool. To find out why, I tweaked t
he code in `site-packages/langchain_core/agents.py` to print out the search query. To my amazement, I discovered that th
e way the search query appears to work is that it just keeps sending different formats of the query until one of them wo
rks! The output below is from the verbose log showing the `<tool>:<query>` followed by the error message.  In this case,
 the search engine was EXA.

    Entering new CrewAgentExecutor chain...
    'Search: {'The rise in homelessness and pov
erty statistics'}\n'
    I encountered an error while trying to use the tool. 
    This was the error: Exa.search() miss
ing 1 required positional argument: 'query'.
    
    'Search: {'The rise in homelessness and poverty statistics'}\n'
  
  (same error)
    
    'Search: The rise in homelessness and poverty statistics'\n'
    (same error)
    
    'Search: 
The rise in homelessness and poverty statistics'\n'
    (same error)
    
    'Search: Search('The rise in homelessness 
and poverty statistics')\n'
    (same error)
    
    'Search: Search('The rise in homelessness and poverty trends')\n'

    (same error)
    
    'Search: Search('The rise in homelessness and poverty causes and solutions')\n'
    (same erro
r)
    
    'Search: Search('The rise in homelessness and poverty causes and impacts')\n'
    (same error)
    
    'Sea
rch: Search('The rise in homelessness and poverty in the United States')\n'
    (same error)
    
    'Search: Search('T
he rise in homelessness and poverty trends')\n'
    (same error)
    
    'Search: Search('The rise in homelessness and 
poverty in the United States')\n'
    (same error)
    
    'Search: Search('The rise in homelessness and poverty in the
 United States')\n'
    (same error)
    
    ('Search: Search('The rise in homelessness and poverty causes and impacts 
in the United States')\n'
    (same error))
    
    'Search: Search('The rise in homelessness and poverty articles')\n'

    (same error)
    
    'Search: Search('The rise in homelessness and poverty trends')\n'
    (same error)
    
    '
Search: Search('The rise in homelessness and poverty in the United States')\n'
    (same error)
    
    ('Search: Searc
h('The rise in homelessness and poverty causes and impacts in the United States')\n'
    (same error))
    
    'Search:
 Search('The rise in homelessness and poverty statistics')\n'
    (same error)
    
    'Search: Search('The rise in hom
elessness and poverty in the United States')\n'
    (same error)
    
    ('Search: Search('The rise in homelessness and
 poverty causes and impacts in the United States')\n'
    (same error)
    
    'Search: {\n  'query': 'The rise in home
lessness and poverty'\n}\n'
    {
      'query': 'The rise in homelessness and poverty'
    }

Finally, after 20 failed 
blind attempts, it found one that worked. Ironically, this is not the correct query parameter for EXA, but the EXA funct
ion converts 'query' to 'q'.

This explains why I get boatloads of meaningless error messages, which I can now ignore, u
nless NONE of them work.

**Suggestion to devs** Don't tell me about failed queries if there are GUARENTEED to be failed
 queries.   Better yet, create a query that is compatible with the API in use.

The above workflow created the correct o
utput.

With the server api, the errors are far weider...

    Entering new CrewAgentExecutor chain...
    ('Search the 
internet: {'search_query': 'The rise in homeless and poor statistics and trends'}')
    (results were correct)
    Finis
hed chain.
    
    Entering new CrewAgentExecutor chain...
    ('Search the internet: {'The rise in homelessness and po
verty in the United States'}')
    ('Search the internet: {'The rise in homelessness and poverty in the United States'}'
)
    ('Search the internet: {'The rise in homelessness and poverty in the United States'}')
    (results were correct)

    Finished chain.
    
    Entering new CrewAgentExecutor chain...
    ('Search the internet: {'The rise in homelessne
ss and poverty in the United States'}\n')
    ('Search the internet: {'The rise in homelessness and poverty in the Unite
d States'}\n')
    ('Search the internet: {'The rise in homelessness and poverty in the United States'}\n')
    ('Search
 the internet: {'The rise in homelessness and poverty in the United States'}\n')
    ('Search the internet: {'The rise i
n homelessness and poverty in the United States'}\n')
    (results were correct)
    Finished chain.
    
    Entering n
ew CrewAgentExecutor chain...
    'Search the internet: {'The rise in homeless and poor in the United States'}'
    'Sea
rch the internet: {'The rise in homeless and poor in the United States'}'
    ('Search the internet: {'The rise in homel
essness statistics in the United States'}')
    ('Search the internet: {'Statistics on homelessness and poverty in the U
nited States'}')
    ('Search the internet: Statistics on homelessness and poverty in the United States')
    
    {'mes
sage': 'Missing query parameter', 'statusCode': 400}
    
    ('Search the internet: Statistics on homelessness and pove
rty in the United States')
    'Search the internet: Statistics on homelessness in the United States'
    'Search the in
ternet: Statistics on homelessness in the United States'
    'Search the internet: Statistics on homelessness in the Uni
ted States'
    'Search the internet: Causes of homelessness and poverty in the United States'
    'Search the internet:
 Causes of homelessness and poverty in the United States'
    (no results)
    Finished chain.

Some of the queries were
 submitted one after the other, and some were interspersed with queries like

    Thought: I need to refine my search qu
ery to gather specific data on the rise in homelessness and poverty in the United States.
    Thought: I need to refine 
my search query to gather specific data on the rise in homelessness and poverty in the United States.
    Thought: I nee
d to refine my search query to gather specific data on the rise in homelessness and poverty in the United States.
    Th
ought: I need to refine my search query to gather specific data on the rise in homelessness and poverty in the United St
ates.
    Thought: I need to refine my search query to gather specific data on the rise in homelessness and poverty in t
he United States.
    Thought: I need to gather information on the rise in homelessness and poverty in the United States
 using the available tools.
    Thought: I need to gather information on the rise in homelessness and poverty in the Uni
ted States using the available tools.
    Thought: I need to refine my search query to gather specific data on the rise 
in homelessness and poverty in the United States.
    Thought: I need to gather information on the rise in homelessness 
and poverty in the United States using the available tools.
    

It's a mystery why the same query was resubmitted, but
 this was good! It was doing its homework. But of two identical queries, one responded with

    {'message': 'Missing qu
ery parameter', 'statusCode': 400}

This means the query was missing a required query parameter (400 = Bad Request statu
s code)

But even though it found a ton of links and did a lot of research, the final repost was.

    Unfortunately, du
e to the limitations of the tools provided, I was unable to gather specific information on the rise in homelessness and 
poverty in the United States. Additional resources or access to more advanced research tools would be needed to gather a
ccurate and comprehensive data on this important issue.

As these were the EXACT same workflow, with only the search too
l changed, I have to assume that Serper, or the way CrewAi handles the responses, is the reason why the workflow failed 
miserably, even though is successfully found lots of data.

There are so many inconsistencies, combined with a severe la
ck of tracking/debugging/logging tools and no docs that address or explain these issues, or worse, outdated docs that ar
e inconsistent with the official CrewAI recommendations, that even for home use, any workflow will be way too unreliable
.

For example, sometimes the serper-search workflow outputs a message saying it could not do anything (above), and some
times it outputs a good report (below). Look at the two reports below, and you will see how radically they differ based 
on when the search engine was used! That is NUTS!!

Here is the template I told the Publishing Task to follow:

    # Ti
tle of Report
        ## OPINION PIECE of where and how those concepts will be expressed in the near future in society, 
economics, culture, or any other area that applies.   
        - ### headline of item 1
        > summary of item 1
    
    ###### _title of webpage_, _date_ [name of link](website link)  
    
        - ### headline of item 2
        > Sum
mery of item 2
        ###### _title of webpage_, _date_ [name of link](website link)  
    link)

Serper-based report:


* 'Opinion Piece' unfilled, but format is followed



    # Research Report: The Rise in Homelessness and Poverty
    #
# OPINION PIECE of where and how those concepts will be expressed in the near future, in society, economics, culture, or
 any other area that applies.
    
    - ### State of Homelessness: 2023 Edition 
    > The 2023 State of Homelessness r
eport provides a comprehensive analysis of homelessness in the U.S. in 2022, revealing rising trends in homelessness sta
tistics.
    ###### _endhomelessness.org_, [State of Homelessness](https://endhomelessness.org/homelessness-in-america/h
omelessness-statistics/state-of-homelessness/)
    
    - ### Homelessness in the US
    > The United States Census Bure
au reported a national poverty rate of 12.7% in 2016, with those who are poor and addicted being at increased risk of ho
melessness.
    ###### _nationalhomeless.org_, [Homelessness in the US](https://nationalhomeless.org/homelessness-in-the
-us/)
    
    - ### Homelessness in America: Statistics, Analysis, & Trends
    > In 2023, 653,104 people experienced h
omelessness in the U.S., representing a record-high tally and a 12% increase over 2022.
    ###### _Security.org_, [Home
less Statistics](https://www.security.org/resources/homeless-statistics/)
    
    - ### The Relationship Between Povert
y and Homelessness Among Older Adults
    > Five million people aged 65 and older lived below the poverty level, with at
 least 2.6 million classified as 'near poor,' highlighting the link between poverty and homelessness.
    ###### _endhom
elessness.org_, [Poverty and Homelessness](https://endhomelessness.org/blog/the-relationship-between-poverty-and-homeles
sness-among-older-adults/)
    
    - ### Homelessness In America: Overview of Data and Causes
    > The National Law Ce
nter on Homelessness & Poverty estimates that 2.5 to 3.5 million Americans sleep in shelters every year, emphasizing the
 scale of homelessness.
    ###### _homelesslaw.org_, [Homelessness Overview](https://homelesslaw.org/wp-content/uploads
/2018/10/Homeless_Stats_Fact_Sheet.pdf)
    
    - ### How many Americans live in poverty?
    > The number of people ex
periencing homelessness increased by 12,751 or 2.2% from 2019 to 2020, marking a continuous rise in homelessness rates.

    ###### _USAFacts_, [American Poverty](https://usafacts.org/articles/american-poverty-in-three-charts/)
    
    - ##
# Homelessness Data & Trends
    > Federal homelessness data shows a surge in homelessness, with poverty dropping by 45%
, indicating a complex relationship between poverty and homelessness.
    ###### _usich.gov_, [Data & Trends](https://ww
w.usich.gov/guidance-reports-data/data-trends)
    
    - ### Homelessness in America grew in 2023 as cost of living bal
looned
    > From 2020 to 2022, the number of people becoming homeless for the first time increased by 30%, highlighting
 the impact of cost of living on homelessness rates.
    ###### _usatoday.com_, [Homelessness Growth](https://www.usatod
ay.com/story/news/nation/2023/12/15/homelessness-in-america-grew-2023/71926354007/)
    
    - ### Basic Facts About Hom
elessness: New York City
    > In March 2024, 69% of individuals in shelters were members of homeless families, includin
g 48,304 children, indicating the vulnerable demographics affected by homelessness.
    
    ###### _coalitionforthehome
less.org_, [Basic Facts](https://www.coalitionforthehomeless.org/basic-facts-about-homelessness-new-york-city/)

EXA-bas
ed report

* Did not follow format (minimal entries, no synopsis)
* 'Opinion Piece' filled out



    # Title of Report:
 The Rise in Homelessness and Poverty: A Comprehensive Analysis
    
    ## OPINION PIECE: The urgent need for collabora
tive efforts to address the growing crisis of homelessness and poverty in society
    
    - ### Homeless Numbers Rise i
n U.S. Cities
    ###### _WSJ News Exclusive_, June 19, 2023 [Link](https://www.wsj.com/articles/homeless-numbers-rise-i
n-u-s-cities-fd59bc7b)  
    
    - ### America's Homelessness Crisis
    ###### _The Week_, March 11, 2018 [Link](https
://theweek.com/articles/759683/americas-homelessness-crisis)  
    
    - ### Homelessness in US: A Deepening Crisis on 
the Streets of America
    ###### _BBC News_, October 7, 2018 [Link](https://www.bbc.com/news/world-us-canada-45442596) 
 
    
    - ### Homelessness Data & Trends
    ###### _United States Interagency Council_, August 5, 2022 [Link](https:
//www.usich.gov/guidance-reports-data/data-trends)  
    
    - ### Homelessness Ticks Up for the Second Year in a Row
 
   ###### _NBC News_, December 18, 2018 [Link](https://www.nbcnews.com/politics/white-house/homelessness-ticks-second-ye
ar-row-federal-report-finds-n949086)  
    
    - ### Homelessness Rose in the U.S. after Pandemic Aid Dried Up
    ####
## _CBS News_, June 21, 2023 [Link](https://www.cbsnews.com/news/federal-homelessness-statistics-us-2023-data/)  
    
 
   - ### State of Homelessness: 2022 Edition
    ###### _End Homelessness_, September 27, 2022 [Link](https://endhomeles
sness.org/homelessness-in-america/homelessness-statistics/state-of-homelessness/)

I ran each test 5 times.  With Serper
, I got output files that ranged from 29 bytes to 4K. and '400' errors ranging from 1 to 11 for each report.

With EXA, 
I got many 'Error using tool' per run, with output files ranging from 42 bytes to 2.1K.

So, what's the plan?  Run the w
orkflow in an endless loop until you get a decent report?

p.s. Local models/Ollama fails so miserably it's not even wor
th considering

Tests run with:

    OpenAI/gpt-3.5-turbo
    langchain           0.1.10
    langchain_community 0.0.38

    crewai              0.30.11
    crewai_tools        0.2.6
    Python              3.11.9 | packaged by conda-forge |
 (main, Apr 19 2024, 18:36:13) [GCC 12.3.0]
    System              Linux 6.1.0-18-amd64
```
---

     
 
all -  [ Review my Resume ](https://www.reddit.com/r/Btechtards/comments/1d7hwml/review_my_resume/) , 2024-06-05-0953
```
I am a second year [B.tech](http://B.tech) student and this resume was aimed to help me get AI Intern roles.

https://pr
eview.redd.it/tl3hzp5pqf4d1.jpg?width=988&format=pjpg&auto=webp&s=2853c067801aa13397ddfab46861705bb386b31d


```
---

     
 
all -  [ Review my Resume ](https://www.reddit.com/r/learnmachinelearning/comments/1d7hvtp/review_my_resume/) , 2024-06-05-0953
```
I am a second year [B.tech](http://B.tech) student and this resume was aimed to help me get AI Intern roles.

https://pr
eview.redd.it/9zytlh4lqf4d1.jpg?width=988&format=pjpg&auto=webp&s=2ca9747bc65ace672e2723b37fb30a5bbf539a3f


```
---

     
 
all -  [ RAG for IM chat logs ](https://www.reddit.com/r/learnmachinelearning/comments/1d7gp1x/rag_for_im_chat_logs/) , 2024-06-05-0953
```

Hi,
I'm trying to create an LLM-based system that allows me to 'interact' with my chat logs and draw conclusions from t
hem. 
A few examples:
* Find 'sub'-conversations or messages in which a certain topic is talked about and perhaps even s
ummarize all of those 'sub'-conversations (and it's important not to miss any, which is something I've been struggling w
ith)
* Find people in my group chats that talk a lot about certain topics
And other similar prompts that I give the LLM.



Right now my solution is pretty simple. I processed all my messages with recursive character chunking and each messag
e into a document, while using a Parent Document Retriever to get more context (in the future I plan on using semantic c
hunking to make the parent documents full sub-conversations). Those are then put into a vector database, and A basic con
versational RAG agent (I currently use mixtral-instruct) with langchain. The conversations are injected as JSON as conte
xt.

First of all, I would love to know what approach you guys would take to this problem in each part of it - the embed
ding, the retrieval (is RAG even the solution here?), the context format, the agent, etc. I'm a newbie to LLMs and AI in
 general and I really want to hear the opinions of people with experience

Secondly, I have a few problems I've encounte
red with my setup, mainly:
* Because I currently don't split my documents semantically, I receive a big part of the conv
ersation (up to 4k+ tokens). mixtral seems to, for some reason, ignore some of my context and only remembers it starting
 from some arbitrary index, unless I really shorten it down to several hundreds of tokens. I don't understand why this h
appens as it should have a 32k context window. One solution I thought of was switching to llama3-8b (only 8k but might w
ork better because it's a better model). This is a huge roadblock for this project and I'd appreciate any help here
* I'
m not sure how to approach the not missing conversations part, as I'm always going to have a limited context. How do I m
ake it so the agent continues fetching the rest of the convesations that were less relevant in the vector similarity sea
rch, like continually do it or something.

Thanks in advance!
```
---

     
 
all -  [ RAG for IM chat logs ](https://www.reddit.com/r/LangChain/comments/1d7ghuk/rag_for_im_chat_logs/) , 2024-06-05-0953
```
Hi,
I'm trying to create an LLM-based system that allows me to 'interact' with my chat logs and draw conclusions from th
em. 
A few examples:
* Find 'sub'-conversations or messages in which a certain topic is talked about and perhaps even su
mmarize all of those 'sub'-conversations (and it's important not to miss any, which is something I've been struggling wi
th)
* Find people in my group chats that talk a lot about certain topics
And other similar prompts that I give the LLM.



Right now my solution is pretty simple. I processed all my messages with recursive character chunking and each message
 into a document, while using a Parent Document Retriever to get more context (in the future I plan on using semantic ch
unking to make the parent documents full sub-conversations). Those are then put into a vector database, and A basic conv
ersational RAG agent (I currently use mixtral-instruct) with langchain. The conversations are injected as JSON as contex
t.

First of all, I would love to know what approach you guys would take to this problem in each part of it - the embedd
ing, the retrieval (is RAG even the solution here?), the context format, the agent, etc. I'm a newbie to LLMs and AI in 
general and I really want to hear the opinions of people with experience

Secondly, I have a few problems I've encounter
ed with my setup, mainly:
* Because I currently don't split my documents semantically, I receive a big part of the conve
rsation (up to 4k+ tokens). mixtral seems to, for some reason, ignore some of my context and only remembers it starting 
from some arbitrary index, unless I really shorten it down to several hundreds of tokens. I don't understand why this ha
ppens as it should have a 32k context window. One solution I thought of was switching to llama3-8b (only 8k but might wo
rk better because it's a better model). This is a huge roadblock for this project and I'd appreciate any help here
* I'm
 not sure how to approach the not missing conversations part, as I'm always going to have a limited context. How do I ma
ke it so the agent continues fetching the rest of the convesations that were less relevant in the vector similarity sear
ch, like continually do it or something.

Thanks in advance!
```
---

     
 
all -  [ Need CV Review ](https://www.reddit.com/gallery/1d7e2gt) , 2024-06-05-0953
```
I am entering the EU market formally as I am completing my MBA. I have a placement already that I got from my home count
ry and is a part time opportunity. I want to get a better placement with my recent degree and further experience so I wa
nt to know what should I improve here.
```
---

     
 
all -  [ Can Azure AI Document Intelligence detect charts like histograms? ](https://www.reddit.com/r/Azure_AI_Cognitive/comments/1d7dr1r/can_azure_ai_document_intelligence_detect_charts/) , 2024-06-05-0953
```
Hi, i am working with [models](https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/concept-model-o
verview?view=doc-intel-4.0.0) via Langchain. I am not able to understand how to let the document analysis client to dete
ct charts (i.e. images with numbers on x / y axis in a pdf) like histograms. Can you provide some guidelines on how to p
roceed?

Thank you
```
---

     
 
all -  [ Need help with my use case  ](https://www.reddit.com/r/LangChain/comments/1d78ov3/need_help_with_my_use_case/) , 2024-06-05-0953
```
Hello everyone, langchain noob here. I have some data that I want to use for question answering. That data has informati
on on different camera models and their specs. What I’m trying to do is retrieving the one that suites the provided use 
case best.  So far I’ve been done some experiments with langchain and also preprocessing the prompt but with not so much
 success. 

My question is: has anyone done anything similar to this? Would langchain even be the right choice here? If 
so, how would you approach this? 

Thanks in advance 
```
---

     
 
all -  [ Does Langchain handle prompt formatting? ](https://www.reddit.com/r/LangChain/comments/1d78e78/does_langchain_handle_prompt_formatting/) , 2024-06-05-0953
```
Most LLMs, especially chat models, have some way they expect prompt to be formatted for things to work correctly (Exampl
e: https://llama.meta.com/docs/model-cards-and-prompt-formats/meta-llama-3/). However, the Langchain prompts abstraction
 hides all that away and just lets users create their prompts in a clean, generalized way (https://python.langchain.com/
v0.1/docs/modules/model\_io/prompts/quick\_start/). My assumption would be that, behind the scenes, Langchain is handlin
g those details. But I can't find any information that indicates either way. 
```
---

     
 
all -  [ OpenGPT with gpt4o ](https://www.reddit.com/r/LangChain/comments/1d7837n/opengpt_with_gpt4o/) , 2024-06-05-0953
```
Hi all, anyone is using OpenGPT for the deployment?
I wonder how to use the latest gpt4o which require newer version of 
langchain.
If I upgrade langchain package, it will crash. Any advice or walk around?


```
---

     
 
all -  [ Import packages ](https://www.reddit.com/r/learnpython/comments/1d777a4/import_packages/) , 2024-06-05-0953
```
I have just began my python journey and I am trying to follow simple code snippets and try out on my own. I however alre
ady have some confusions. I understand that there are python packages that we can import. But sometimes there are more g
ranular imports. Here is an example:

#1 import langchain
#2 from langchain.sql_database import SQLDatabase
…
#9 from la
ngchain import sagemakerendpoint

Etc…

1. What are those deeper packages called, like SQLDatabase in line #2 ? Are thos
e also packages just embedded? Or are they functions within the main package? What is the right term for them?

2. How d
o I even know what sub-packages or functions are there within a package that I can import specifically? Do I need to che
ck github every time for the package source code?

3. I found dir() command to show me something similar but still somet
hing not OK. For example when I issue dir(langchain) it doesn’t show any submodules(?) called sagemakerendpoint. So I do
n’t get how it could be imported from langchain package. See line #9 in the code snippet above. 


To me it is very conf
using but I am new to python as well. Can somebody explain these to me?

Thanks


```
---

     
 
all -  [ is langchain even open source now ](https://www.reddit.com/r/LangChain/comments/1d73efm/is_langchain_even_open_source_now/) , 2024-06-05-0953
```
I ask this because there landing page looks like a full blown product page with no clarity whatsover - it looks as if it
 is a commercial sass.

Are there any alternative projects which are less salesy ?
```
---

     
 
all -  [ Langgraph: Using CheckPointer makes the tool calls break, if a tool call has failed ](https://www.reddit.com/r/LangChain/comments/1d71axk/langgraph_using_checkpointer_makes_the_tool_calls/) , 2024-06-05-0953
```
Hi, when using langgraph checkpointer to store the chat history, if a tool call fails, the subsequent tool calls will fa
il with an error:

    openai.BadRequestError: Error code: 400 - {'error': {'message': 'An assistant message with 'tool_
calls' must be followed by tool messages responding to each 'tool_call_id'. The following tool_call_ids did not have res
ponse messages: call_v5dzbL3NBrFZ7Z4xZExU9AUv', 'type': 'invalid_request_error', 'param': 'messages.[8].role', 'code': N
one}}

If I don't use a checkpointer, nothing breaks. I'm stuck because of this error, and need some help!

Also started
 a discussion on langgraph repo:

[https://github.com/langchain-ai/langgraph/discussions/544](https://github.com/langcha
in-ai/langgraph/discussions/544)
```
---

     
 
all -  [ What are the alternatives to langchain agents ](https://www.reddit.com/r/LangChain/comments/1d6xgql/what_are_the_alternatives_to_langchain_agents/) , 2024-06-05-0953
```
What are the alternatives to langchain agents ?

Working on a product that is on production . We use heavily OpenAI LLM 
to take decisions. However, we are integrating tools and we are thinking to use langchain agents for that.
We already di
d a project with langchain agents before and it was very easy for us to use their agents.
Any alternative on how we can 
do this without using langchain ? 

Here is a use case : based on a client choice on a conversation with a chatbot , we 
need to call a tool.
```
---

     
 
all -  [ Streaming in Langserve with the `per_req_config_modifier` ](https://www.reddit.com/r/LangChain/comments/1d6x1k9/streaming_in_langserve_with_the_per_req_config/) , 2024-06-05-0953
```
I am currently developing an app using langserve that requires a user to be authenticated to load files into the vectors
tore and for retrieving documents as well:

Based on the example provided here:  
[https://github.com/langchain-ai/langs
erve/blob/main/examples/auth/per\_req\_config\_modifier/server.py](https://github.com/langchain-ai/langserve/blob/main/e
xamples/auth/per_req_config_modifier/server.py)

I have come up with this so far which works perfectly for the 'invoke' 
request:

    class PerUserQuery(RunnableSerializable):
        '''
        A custom runnable that returns a list of doc
uments for the given user.
    
        The runnable is configurable by the user, and the search results are
        fil
tered by the user ID.
        '''
    
        user_id: Optional[str]
        vectorstore: VectorStore
    
        clas
s Config:
            # Allow arbitrary types since VectorStore is an abstract interface
            # and not a pydanti
c model
            arbitrary_types_allowed = True
    
        def get_rag_chain(self, query):
    
            def for
mat_docs(docs):
                return '\n\n'.join(doc.page_content for doc in docs)
    
            retriever = self.v
ectorstore.similarity_search(
                query, k=10, filter={'user_id': {'$eq': self.user_id}}
            )
     
       formatted_docs = format_docs(retriever)
            setup_and_retrieval = RunnableParallel(
                {'con
text': lambda x: formatted_docs, 'question': RunnablePassthrough()}
            )
            prompt = hub.pull('rarchit
/rag-prompt-bullet')
            llm = get_llm()
            rag_chain = setup_and_retrieval | prompt | llm | StrOutputP
arser()
            return rag_chain
    
        def _invoke(
            self, input: str, config: Optional[RunnableCo
nfig] = None, **kwargs: Any
        ) -> List[Document]:
            '''
            Invoke the retriever
            ''
'
            rag_chain = self.get_rag_chain(query=input)
            return rag_chain.invoke(str(input))
    
        d
ef invoke(
            self, input: str, config: Optional[RunnableConfig] = None, **kwargs
        ) -> List[Document]:

            return self._call_with_config(self._invoke, input, config, **kwargs)

However I am unable modify the endpoin
t to stream the response. If anyone could help out with the same I would really appreciate it. Currently stuck here
```
---

     
 
all -  [ Consider questions related to the uploaded files... ](https://www.reddit.com/r/LangChain/comments/1d6tih5/consider_questions_related_to_the_uploaded_files/) , 2024-06-05-0953
```

Hi, I am trying to build a RAG, the use-case is to upload some pdf files and ask questions about it. The stack include:
 streamlit, langchain, ollama(mistral ig) and chroma db. Only questions related to the uploaded pdf file(s) must be answ
ered. In case there is a question not related to the pdf file content, the answer should be 'I don't know' or 'not relat
ed to the context'. How can this be done ..??
Is it related to the prompt ?? 
```
---

     
 
all -  [ [0 YOE] New Grad with 300+ Tailored Applications with no Interviews. Too busy? Unsubstantive? ](https://www.reddit.com/r/EngineeringResumes/comments/1d6qta2/0_yoe_new_grad_with_300_tailored_applications/) , 2024-06-05-0953
```
https://preview.redd.it/ttb18wl1w84d1.png?width=5100&format=png&auto=webp&s=0bac74240d11d4927d65ec60b87a59700d017857

He
llo all,  
As the title says, I'm failing to get to the interview stage of my applications. I graduated early (3 1/2 yea
rs) and I have been applying for remote and seattle based roles primarily on linkedin and google jobs. I will generally 
tailor the skills section of my resume depending on what a job is looking for. I am primarily looking at full stack, fro
nt end, back end, and python developer roles. I have a job offer from the internship that I took but that starts in 4-5 
months and is not in the locations I am looking for.

Potential problem points:

* Too busy
* Recruiters think I am inte
rnational/need visa
* Flawed application methods
* Busy Bolding
```
---

     
 
all -  [ LLM vs CS Fundamentals ](https://www.reddit.com/r/cscareerquestions/comments/1d6pc2y/llm_vs_cs_fundamentals/) , 2024-06-05-0953
```
I have a bachelor in CS and will be graduating with a master in AI in December. I already have a SDE summer internship l
ined up, but the return rate is quite low. I am wondering should I keep grinding CS fundamentals (leetcode, OS, Network…
) or should I put more focus on MLE related preparation (ML fundamentals, updated research papers and tools such as Lang
chain), considering the recent hype/boost of LLM and over saturation on traditional sde roles. My ultimate goal is to ge
t a job after graduation ASAP. Any advance will be greatly appreciated!
```
---

     
 
all -  [ Llm model selection ](https://www.reddit.com/r/LangChain/comments/1d6o48l/llm_model_selection/) , 2024-06-05-0953
```
Hi everyone!  
Im a starter on playing with langchain and currently trying out llms using Ollama, but im kinda fuzzy on 
how to select a model for a specific use (embedding, text generation, code generation etc.) from such a wide range of mo
dels. Im pretty much using Llama3 for every use case. Can anyone help me? Much appreciated!
```
---

     
 
all -  [ RAG with legal texts ](https://www.reddit.com/r/LangChain/comments/1d6mnum/rag_with_legal_texts/) , 2024-06-05-0953
```
Hello everyone, 

&#x200B;

I want to build a RAG chatbot using case texts but I can't get good results in similarity se
arch. 

When I think about the reasons for this, I suspect that repetitive sentences in legal texts are the problem. How
 can I overcome this problem? I have tried semantic chunking, parent document retrival, almost everything. 
```
---

     
 
all -  [ Is it possible to create an agent that can query a MySQL database and answer questions about a docum ](https://www.reddit.com/r/LangChain/comments/1d6ern3/is_it_possible_to_create_an_agent_that_can_query/) , 2024-06-05-0953
```
Hey,

I'm relatively new to Langchain and have primarily worked with chains and retrievers. Recently, I discovered agent
s and tools, and they seem quite powerful.

I've successfully set up an SQL agent following the documentation. Now, I'm 
interested in creating an agent that can browse both an SQL database and document-based sources.

I saw in the documenta
tion that it's possible to use multiple tools, like combining [Tavily and a retriever tool.](https://python.langchain.co
m/v0.2/docs/how_to/agent_executor/) 

I'd appreciate if someone could let me know where it's possible  to build such an 
agent and where to look for relevant resources? So far, it's been quite difficult to find anything that can point me in 
the right direction.

Thanks!
```
---

     
 
all -  [ TypeError: RequestsPostTool._run() got an unexpected keyword argument 'url' ](https://www.reddit.com/r/LangChain/comments/1d6ebjn/typeerror_requestsposttool_run_got_an_unexpected/) , 2024-06-05-0953
```
I am trying to interact with an external API using RequestsPostTool, AIPluginTool, and create\_openai\_tools\_agent. But
 I am always getting this error:

TypeError: RequestsPostTool.\_run() got an unexpected keyword argument 'url'

  
I che
cked the logs from Langsmith and it seems the issue is caused by double quotations outside the JSON string and not insid
e the JSON string. This causes RequestsPostTool.\_run() function to not work in the code.

My question is how to resolve
 this error efficiently or how to validate the output of LLM before it pass the input to RequestsPostTool.\_run()
```
---

     
 
all -  [ Consider questions related to the uploaded files... ](https://www.reddit.com/r/ollama/comments/1d6ea38/consider_questions_related_to_the_uploaded_files/) , 2024-06-05-0953
```
Hi, I am trying to build a RAG, the use-case is to upload some pdf files and ask questions about it. The stack include: 
streamlit, langchain, ollama(mistral ig) and chroma db. Only questions related to the uploaded pdf file(s) must be answe
red. In case there is a question not related to the pdf file content, the answer should be 'I don't know' or 'not relate
d to the context'. How can this be done ..??
Is it related to the prompt ?? 
```
---

     
 
all -  [ ChatGPT refuse/not aware of its function calling capability, and don't call functions even when ther ](https://www.reddit.com/r/LangChain/comments/1d6dvnw/chatgpt_refusenot_aware_of_its_function_calling/) , 2024-06-05-0953
```
Hi everyone,

I'm new to LangChain, and currently learning LangGraph. This morning things are fine, I was trying to repl
icate the AgentExecutor using LangGraph as presented in their Youtube videos, and the agent (GPT 4.0) was able to use th
e web search tool (DuckDuckGo, btw) to search for information about weather, and return to me correct answer. 

However,
 in the evening of the same day, I could not do so anymore. The model refuse to give me real time data about weather. It
 got worse: when I specifically asked it to use function call to perform search about weather, but it even denying it fu
nction call capabilities.

Do anyone knows why this is the case? It is so frustrating!

[This is the screenshot of my ag
ent denying me. Hurt!](https://preview.redd.it/sl8oai2fz54d1.png?width=1441&format=png&auto=webp&s=c257cb67bbbd91c60fd17
ea239c4adef9df891b2)


```
---

     
 
all -  [ Hi folks, need help regarding ReAct agents and working with urls. ](https://www.reddit.com/r/LangChain/comments/1d6dm3b/hi_folks_need_help_regarding_react_agents_and/) , 2024-06-05-0953
```
Hi, 

I recently started learning langchain and am developing a simple app in which first we enter user's name then one 
agent finds their linkedin profile url and based on that writes a short summary about them, but I am facing an issue whe
re the url is often times another redirecting link to the main profile page url, but when the redirecting link is forwar
ded to Proxycurl API(api to access linkedin page through url) which is not able to detect it, how should i go about this
 problem?  


Thanks. 
```
---

     
 
all -  [ Deploy Langchain Streaming RAG app on Streamlit ](https://www.reddit.com/r/LangChain/comments/1d6bkbr/deploy_langchain_streaming_rag_app_on_streamlit/) , 2024-06-05-0953
```
This video covers:  
- How to use Streamlit Secrets to hide your API keys  
- Importance of requirements.txt file  
- De
ploy the LLM application on Streamlit and get a sharable link  
- Also learn how to fix the Chroma and SQLite3 issues wh
ile deploying your application built using Langchain and Chroma vector base.

  
Watch here: [https://www.youtube.com/wa
tch?v=7BBzM2qCZvc](https://www.youtube.com/watch?v=7BBzM2qCZvc)
```
---

     
 
all -  [ LLM doesn't include the context from the vector database, and hence the frontend gets the generic re ](https://www.reddit.com/r/u_Prakash127_0_0_1/comments/1d67fhq/llm_doesnt_include_the_context_from_the_vector/) , 2024-06-05-0953
```
I am creating a chatbot for my portfolio website. I am using Next.js, OpenAI API, Vercel AI SDK, Langchain and AstraDB.


As I hit request my route, LLM runs twice. The first run of LLM contains no context that I provided and the answer is j
ust simple with no information of mine. But the second run contains the context I provided from the AstraDb vector datab
ase and I get what I want.

For example: I write 'who are you', the first answer is 'I am a language model AI designed t
o assist with answering questions and engaging in conversation. How can I help you today?' and the second answer is 'I a
m Prakash Banjade.........'.

But on the frontend, I get the first answer which is not relevant.

Here's my code:

// ro
ute.ts

`import { ChatOpenAI } from '@langchain/openai';`

`import { createStreamDataTransformer, LangChainAdapter, Stre
amingTextResponse, Message as VercelChatMessage, } from 'ai'`

`import { AIMessage, HumanMessage } from '@langchain/core
/messages';`

`import { ChatPromptTemplate, MessagesPlaceholder, PromptTemplate } from '@langchain/core/prompts'`

`impo
rt { UpstashRedisCache } from '@langchain/community/caches/upstash_redis';`

`import { Redis } from '@upstash/redis';`


`import { createStuffDocumentsChain } from 'langchain/chains/combine_documents';`

`import { createHistoryAwareRetriever
 } from 'langchain/chains/history_aware_retriever';`

`import { createRetrievalChain } from 'langchain/chains/retrieval'
;`

`import { getVectorStore } from '@/lib/astradb';`

`export const dynamic = 'force-dynamic';`

`export const maxDurat
ion = 60;`

`export async function POST(req: Request) {`

`try {`

`const body = await req.json();`

`const messages = b
ody.messages;`

`const chatHistory = messages`

`.slice(0, -1)`

`.map((m: VercelChatMessage) =>`

`m.role === 'user'`


`? new HumanMessage(m.content)`

`: new AIMessage(m.content),`

`);`

`const currentMessageContent = messages[messages.l
ength - 1].content;`

`const cache = new UpstashRedisCache({`

`client: Redis.fromEnv(),`

`});`

`const chatModel = new
 ChatOpenAI({`

`modelName: 'gpt-3.5-turbo',`

`streaming: true,`

`verbose: true,`

`cache,`

`});`

`const rephrasingM
odel = new ChatOpenAI({`

`modelName: 'gpt-3.5-turbo',`

`verbose: true,`

`cache,`

`});`

`const retriever = (await ge
tVectorStore()).asRetriever();`

`const rephrasePrompt = ChatPromptTemplate.fromMessages([`

`new MessagesPlaceholder('c
hat_history'),`

`['user', '{input}'],`

`[`

`'user',`

`'Given the above conversation, generate a search query to look
 up in order to get information relevant to the current question. ' +`

`'Don't leave out any relevant keywords. Only re
turn the query and no other text.',`

`],`

`]);`

`const historyAwareRetrieverChain = await createHistoryAwareRetriever
({`

`llm: rephrasingModel,`

`retriever,`

`rephrasePrompt,`

`});`

`const prompt = ChatPromptTemplate.fromMessages([`


`[`

`'system',`

`'You are a chatbot for a personal portfolio website. You impersonate the website's owner. ' +`

`'A
nswer the user's questions based on the below context. ' +`

`'Whenever it makes sense, provide links to pages that cont
ain more information about the topic from the given context. ' +`

`'Format your messages in markdown format.\n\n' +`

`
'Context:\n{context}',`

`],`

`new MessagesPlaceholder('chat_history'),`

`['user', '{input}'],`

`]);`

`const combine
DocsChain = await createStuffDocumentsChain({`

`llm: chatModel,`

`prompt,`

`documentPrompt: PromptTemplate.fromTempla
te(`

`'Page URL: {url}\n\nPage content:\n{page_content}',`

`),`

`documentSeparator: '\n--------\n',`

`});`

`const r
etrievalChain = await createRetrievalChain({`

`combineDocsChain,`

`retriever: historyAwareRetrieverChain,`

`});`

`re
trievalChain.invoke({`

`input: currentMessageContent,`

`chat_history: chatHistory,`

`});`

`const stream = await chat
Model.stream([new HumanMessage(currentMessageContent), ...chatHistory]);`

`const aiStream = LangChainAdapter.toAIStream
(stream);`

`console.log('hey there 1')`

`return new StreamingTextResponse(aiStream);`

`} catch (e) {`

`console.log(e
)`

`return Response.json({ message: 'internal server error' }, { status: 500 })`

`}}`  


Here the console of LLM:

Co
nnected to Astra DB collection

\[llm/start\] \[1:llm:ChatOpenAI\] Entering LLM run with input: {

'messages': \[

\[

{


'lc': 1,

'type': 'constructor',

'id': \[

'langchain\_core',

'messages',

'HumanMessage'

\],

'kwargs': {

'conten
t': 'who are you?',

'additional\_kwargs': {},

'response\_metadata': {}

}

}

\]

\]

}

hey there 1

\[llm/end\] \[1:
llm:ChatOpenAI\] \[1.01s\] Exiting LLM run with output: {

'generations': \[

\[

{

'text': 'I am a language model AI d
esigned to assist with answering questions and engaging in conversation. How can I help you today?',

'generationInfo': 
{

'prompt': 0,

'completion': 0,

'finish\_reason': 'stop'

},

'message': {

'lc': 1,

'type': 'constructor',

'id': \
[

'langchain\_core',

'messages',

'AIMessageChunk'

\],

'kwargs': {

'content': 'I am a language model AI designed to
 assist with answering questions and engaging in conversation. How can I help you today?',

'additional\_kwargs': {},

'
response\_metadata': {

'prompt': 0,

'completion': 0,

'finish\_reason': 'stop'

},

'tool\_call\_chunks': \[\],

'tool
\_calls': \[\],

'invalid\_tool\_calls': \[\]

}

}

}

\]

\]

}

POST /api/chat 200 in 6053ms

\[llm/start\] \[1:llm:r
etrieval\_chain\] Entering LLM run with input: {

'messages': \[

\[

{

'lc': 1,

'type': 'constructor',

'id': \[

'la
ngchain\_core',

'messages',

'SystemMessage'

\],

'kwargs': {

'content': 'You are a chatbot for a personal portfolio 
website. You impersonate the website's owner. Answer the user's questions based on the below context. Whenever it makes 
sense, provide links to pages that contain more information about the topic from the given context. Format your messages
 in markdown format.\\n\\nContext:\\nPage URL: /about\\n\\nPage content:\\n<div>\\r\\n      <header>\\r\\n        <h2>I\
&apos;m Prakash.</h2>\\r\\n      </header>\\r\\n      <section>\\r\\n        <article>\\r\\n          <p>Hello! I\&apos;
m Prakash Banjade, <em>an aspiring and enthusiastic web developer with a strong foundation in both frontend and backend 
development</em>.\\r\\n ...............................',

'additional\_kwargs': {},

'response\_metadata': {}

}

},

{


'lc': 1,

'type': 'constructor',

'id': \[

'langchain\_core',

'messages',

'HumanMessage'

\],

'kwargs': {

'conten
t': 'who are you?',

'additional\_kwargs': {},

'response\_metadata': {}

}

}

\]

\]

}

\[llm/end\] \[1:llm:retrieval
\_chain\] \[578ms\] Exiting LLM run with output: {

'generations': \[

\[

{

'text': 'I'm Prakash! 🌟\\nI'm an aspiring 
web developer with a strong foundation in both frontend and backend development. You can find more about me on my \[abou
t page\](/about).',

'message': {

'lc': 1,

'type': 'constructor',

'id': \[

'langchain\_core',

'messages',

'AIMessa
ge'

\],

'kwargs': {

'content': 'I'm Prakash! 🌟\\nI'm an aspiring web developer with a strong foundation in both front
end and backend development. You can find more about me on my \[about page\](/about).',

'additional\_kwargs': {},

'res
ponse\_metadata': {

'estimatedTokenUsage': {

'promptTokens': 550,

'completionTokens': 41,

'totalTokens': 591

},

'p
rompt': 0,

'completion': 0,

'finish\_reason': 'stop'

},

'tool\_call\_chunks': \[\],

'tool\_calls': \[\],

'invalid\
_tool\_calls': \[\]

}

}

}

\]

\]

}

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\
_\_\_\_\_\_\_\_\_\_\_\_

On the frontend side, I am receiving the first output of LLM not the second one. Why?
```
---

     
 
all -  [ We're Looking For Developers!!! ](https://www.reddit.com/r/UVA/comments/1d63mzh/were_looking_for_developers/) , 2024-06-05-0953
```
If you are ambitious and have always wanted to build something of your own and help build an idea from the ground up, we
 are an early startup looking for people EXACTLY like you.

**We’re looking for Frontend developers with experience in:*
*

Angular

Typescript

 

**And Backend developers with experience in:**

Python

Typescript

AWS

OpenAI/Langchain

Mi
lvus & DynamoDB

 

We’re a startup currently growing very quickly and accepted within the Darden iLab Incubator for Sum
mer 2024 at UVA. We’re focused on empowering university students to take charge of their university careers by providing
 them with a Personal AI Ecosystem that can optimize their curriculums, courses, schedules, extracurricular activities a
nd also directly help them with their career employment and possibilities in and after university. Your contribution wil
l be invaluable in shaping our future!

Compensation is within discussion depending on expertise, experience, and commit
ment.    
If interested, message me directly and please include your resume.
```
---

     
 
all -  [ Return only used documents ](https://www.reddit.com/r/LangChain/comments/1d5xa86/return_only_used_documents/) , 2024-06-05-0953
```
In my RAG LLM I want to return the documents used to produce the answer. I don't want ALL the documents, but just the on
e or two that open ai used to produce the answer. 

Example

Question: what day is today? 

Documents retrieved 
- doc1 
chunk1: on that day the sky was red
- doc2 chunk15: today is Saturday 
- doc3 chunk666: my name is Michael and I was bor
n two days before my wife 

Answer: today it's Saturday (doc2) 

With returning source documents, my context contains al
l three documents, but just doc2 have been used to answer the question. 

At the moment I'm asking open ai to put a sepa
rator at the end of the question and write a json with the doc index (from 1 to 5), and then pick the context[index], bu
t it's not as robust as I like. 

Any suggestions? 
```
---

     
 
all -  [ How can I get cumulative answer after analysing 1000s of articles? ](https://www.reddit.com/r/LangChain/comments/1d5slpr/how_can_i_get_cumulative_answer_after_analysing/) , 2024-06-05-0953
```
Hi all, I am new to building RAG application. I have no idea about how to make the LLM to answer with all the knowledge 
about 1000s of articles. Let's say I have 1000s of success stories about various businesses, now I want LLM to craft a w
inning strategy.
```
---

     
 
MachineLearning -  [ [P] Superfast RAG: Langchain Streaming and Groq ](https://www.reddit.com/r/MachineLearning/comments/1d5s9g4/p_superfast_rag_langchain_streaming_and_groq/) , 2024-06-05-0953
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

     
 
MachineLearning -  [ [R] Building an Observable arXiv RAG Chatbot with LangChain, Chainlit, and Literal AI ](https://www.reddit.com/r/MachineLearning/comments/1crwh0q/r_building_an_observable_arxiv_rag_chatbot_with/) , 2024-06-05-0953
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

     
 
MachineLearning -  [ [P] LLMinator: A Llama.cpp + Gradio based opensource Chatbot to run llms locally(cpu/cuda) directly  ](https://www.reddit.com/r/MachineLearning/comments/1cpbgd1/p_llminator_a_llamacpp_gradio_based_opensource/) , 2024-06-05-0953
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

     
