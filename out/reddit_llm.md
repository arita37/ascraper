 
all -  [ Is it possible to change agent prompt based on user question after the agent is already created? ](https://www.reddit.com/r/LangChain/comments/1cpsg8f/is_it_possible_to_change_agent_prompt_based_on/) , 2024-05-12-0911
```
I was following the [LangChain SQL Documentation](https://python.langchain.com/v0.1/docs/use_cases/sql/agents/). So far 
I'm using Few shot prompt template as the prompt for the agent.

    agent = create_sql_agent(
        llm=self.llm,
   
     db=self.db,
        prompt=self.few_shot_prompt,
        verbose=True,
        agent_type='openai-tools',
        t
op_k=10,
    )

Now what I want to do is

1. Create a chain that creates a custom prompt based on user question
2. Then 
pass that custom prompt created by the chain to the agent to use when I invoke it

I've created the chain like this

   
 rg = RunnableParallel(
            {
                'input': lambda x: x['input'],
                'dialect': lambda x
: x['dialect'],
                'top_k': lambda x: x['top_k'],
                'tables': self.table_extraction_chain,
  
          }
        ).assign(prompt=self.few_shot_prompt)

can I pipe in the Agent here somehow to use the custom prompt
?
```
---

     
 
all -  [ Problem with heavy documents ](https://www.reddit.com/r/LangChain/comments/1cps3s5/problem_with_heavy_documents/) , 2024-05-12-0911
```
Hello, I am a beginner in LLM and LangChain, and I am developing a small application that allows me to query PDF documen
ts with my OpenAI API. Everything works well so far with the PDFs. I am able to query the PDFs. If the question is out o
f context, it shows that the information is not in the PDF, otherwise, it displays the information. So, everything is go
ing well at the moment, but the problem is that with documents that are a bit longer, 100 pages or more, I really have p
roblems because I can't even load them to query them. So, what should I do?
```
---

     
 
all -  [ [P] Open source library to scrape PDFs, YouTube, URLs, Presentations, etc for API-hosted vision-lang ](https://www.reddit.com/r/MachineLearning/comments/1cpnlqe/p_open_source_library_to_scrape_pdfs_youtube_urls/) , 2024-05-12-0911
```
[Here I will share an open source library](https://thepi.pe/) you can use to extract text and visual unstructured data f
rom files, webpages, youtube videos, etc to immediately feed the results into API-hosted vision language models (like GP
T-4-Vision or Gemini). I made this simple tool because I was unable to get vision functionality with other extraction fr
ameworks like unstructuredio, langchain exctractors, document layout analysis models, etc,

Cheers & have fun!
```
---

     
 
all -  [ Generate python functions automatically from openapi.json? ](https://www.reddit.com/r/openBB/comments/1cpkkb4/generate_python_functions_automatically_from/) , 2024-05-12-0911
```
If I run the REST server locally, I can get an openapi spec via http://127.0.0.1:8000/openapi.json .

which tools can pa
rse the json and generate a python function or sub for each endpoint?

I tried a couple with a custom python parser and 
I can generate a working function like the below from the json below, but wondering if anyone has done a proper job with
 good docstrings and parameters and defaults? 

tried the bravado module which should take an openai spec and turn it in
to REST get requests, didn't parse the JSON correctly, and openapi-python-client also failed.

wanted to experiment with
 langchain agents talking to openai, anthropic etc., and make a tool for e.g. all the equity endpoints that take a symbo
l. could also inspect the obb functions and docstrings. basically wondering if there is a standard way to do this sort o
f metaprogramming with the openbb platform.

    def equity_price_quote(symbol):
       '''the latest quote for a given 
stock. Quote includes price, volume, and other data.'''

      retval = None
      retlist = obb.equity.price.quote(symb
ol).results
      if retlist and type(retlist is list):
        retval = retlist[0].model_dump_json()
      return retva
l 

json:

        '/api/v1/equity/price/quote': {
            'get': {
                'tags': [
                    'e
quity'
                ],
                'summary': 'Quote',
                'description': 'Get the latest quote for a
 given stock. Quote includes price, volume, and other data.',
                'operationId': 'equity_price_quote',
     
           'parameters': [
                    {
                        'name': 'provider',
                        'in
': 'query',
                        'required': true,
                        'schema': {
                            'e
num': [
                                'cboe',
                                'fmp',
                                '
intrinio',
                                'tmx',
                                'tradier',
                           
     'yfinance'
                            ],
                            'type': 'string',
                           
 'title': 'Provider'
                        }
                    },
                    {
                        'nam
e': 'symbol',
                        'in': 'query',
                        'required': true,
                        '
schema': {
                            'type': 'string',
                            'description': 'Symbol to get data 
for. Multiple comma separated items allowed for provider(s): cboe, fmp, intrinio, tmx, tradier, yfinance.',
            
                'multiple_items_allowed': [
                                'cboe',
                                'fmp
',
                                'intrinio',
                                'tmx',
                                't
radier',
                                'yfinance'
                            ],
                            'title': 
'Symbol'
                        },
                        'description': 'Symbol to get data for. Multiple comma separ
ated items allowed for provider(s): cboe, fmp, intrinio, tmx, tradier, yfinance.'
                    },
               
     {
                        'name': 'use_cache',
                        'in': 'query',
                        'requ
ired': false,
                        'schema': {
                            'type': 'boolean',
                       
     'title': 'cboe',
                            'description': 'When True, the company directories will be cached for 
24 hours and are used to validate symbols. The results of the function are not cached. Set as False to bypass. (provider
: cboe)',
                            'default': true
                        },
                        'description': 
'When True, the company directories will be cached for 24 hours and are used to validate symbols. The results of the fun
ction are not cached. Set as False to bypass. (provider: cboe)'
                    },
                    {
           
             'name': 'source',
                        'in': 'query',
                        'required': false,
       
                 'schema': {
                            'enum': [
                                'iex',
              
                  'bats',
                                'bats_delayed',
                                'utp_delayed',

                                'cta_a_delayed',
                                'cta_b_delayed',
                     
           'intrinio_mx',
                                'intrinio_mx_plus',
                                'delayed_s
ip'
                            ],
                            'type': 'string',
                            'title': 'i
ntrinio',
                            'description': 'Source of the data. (provider: intrinio)',
                       
     'default': 'iex'
                        },
                        'description': 'Source of the data. (provider: 
intrinio)'
                    }
                ],
                'responses': {
                    '200': {
        
                'description': 'Successful Response',
                        'content': {
                            '
application/json': {
                                'schema': {
                                    '$ref': '#/componen
ts/schemas/OBBject_EquityQuote'
                                }
                            }
                        
}
                    },
                    '404': {
                        'description': 'Not found'
               
     },
                    '400': {
                        'description': 'No Results Found',
                        
'content': {
                            'application/json': {
                                'schema': {
             
                       '$ref': '#/components/schemas/OpenBBErrorResponse'
                                }
            
                }
                        }
                    },
                    '500': {
                        
'description': 'Internal Error',
                        'content': {
                            'application/json': {

                                'schema': {
                                    '$ref': '#/components/schemas/OpenBBErro
rResponse'
                                }
                            }
                        }
                   
 },
                    '422': {
                        'description': 'Validation Error',
                        'con
tent': {
                            'application/json': {
                                'schema': {
                 
                   '$ref': '#/components/schemas/HTTPValidationError'
                                }
                
            }
                        }
                    }
                },
                'model': 'EquityQuote',

                'examples': [
                    {
                        'scope': 'api',
                        'pa
rameters': {
                            'symbol': 'AAPL',
                            'provider': 'fmp'
               
         },
                        'provider': 'fmp'
                    }
                ]
            }
        },
```
---

     
 
all -  [ GPT3.5 tool calling more accurately than Claude haiku. ](https://www.reddit.com/r/LangChain/comments/1cpjgn1/gpt35_tool_calling_more_accurately_than_claude/) , 2024-05-12-0911
```
Using the same prompt, GPT 3.5 seems more likely to use tools correctly all the time whereas Claude haiku needs better p
rompting to achieve tool calling? Even so, it misses out a good number of times. 

For eg. I don’t even have to mention 
any tools in the gpt prompt but I have to mention in for haiku to even work. Putting the tool description and query work
s enough for gpt.

E.g a tool parameter for “rag vector query” correctly abstracts the query to keywords but haiku dumps
 the entire question in. GPT is also able to infer from history and use tools (eg, tell me more) while haiku just plain 
responds saying it has no more data. 

Am I using anything wrong? Everyone is saying haiku is smarter and all.. main rea
son I am trying it out is that it is cheaper, potentially allowing for more documents to stuff in. 
```
---

     
 
all -  [ Voice generation ](https://www.reddit.com/r/LangChain/comments/1cpcwcg/voice_generation/) , 2024-05-12-0911
```
Hey there, Is there any way to generate a voice?   
I found some impressive tools out there, but wish they were integrat
ed with langchain like this one: [https://github.com/jasonppy/VoiceCraft](https://github.com/jasonppy/VoiceCraft)
```
---

     
 
all -  [ Resume For Data Scientist / Machine Learning Engineer Review ](https://i.redd.it/ofwbm2tsxqzc1.png) , 2024-05-12-0911
```

```
---

     
 
all -  [ [P] LLMinator: A Llama.cpp + Gradio based opensource Chatbot to run llms locally(cpu/cuda) directly  ](https://www.reddit.com/r/MachineLearning/comments/1cpbgd1/p_llminator_a_llamacpp_gradio_based_opensource/) , 2024-05-12-0911
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

     
 
all -  [ Function/tool calling on non-OpenAI models? ](https://www.reddit.com/r/LangChain/comments/1cpagwd/functiontool_calling_on_nonopenai_models/) , 2024-05-12-0911
```
I have a Next.js application that requires RAG (Specifically web search) with multiple open source models. Is there a wa
y to get them to work with function/tool calling?
```
---

     
 
all -  [ Agent to generate Charts based on the user's prompt ](https://www.reddit.com/r/LangChain/comments/1cp9gqj/agent_to_generate_charts_based_on_the_users_prompt/) , 2024-05-12-0911
```
https://preview.redd.it/4738d3i5aqzc1.png?width=723&format=png&auto=webp&s=89b493a6fc2271d489b0df2e6faddd3bf4a19f43

Hi 
Guys, I have a RAG for csv file, the data is about temperature sensors and apps usage percentage in a phone. I was able 
to use azure gpt 4 and generate a textual response. Since we have a csv file, I want the llm to also generate a graph al
ong with the textual response. Please tell me how to code this up.   
  

```
---

     
 
all -  [ Tutorial on Langchain that doesn't rely on an online service? ](https://www.reddit.com/r/learnprogramming/comments/1cp5udf/tutorial_on_langchain_that_doesnt_rely_on_an/) , 2024-05-12-0911
```
Like every tutorials use langchain with an online service, but I would like to build a llm or a simple chatbot with a cr
appy offline llm that we can run offline. Is there anything like it? I searched and it seems that there's nothing like i
t and it's basically a pipe dream.
```
---

     
 
all -  [ (Code included) I did a workshop on long-term selective memory for LLM applications recently ](https://www.reddit.com/r/LangChain/comments/1cp5q9p/code_included_i_did_a_workshop_on_longterm/) , 2024-05-12-0911
```
Good to be back making content for y’all.

Video: [https://www.youtube.com/watch?v=RkWor1BZOn0](https://www.youtube.com/
watch?v=RkWor1BZOn0)

Code: [https://colab.research.google.com/drive/18\_L\_OX4YPlAHdQCSMfRgjTE9aSOEl-6l?usp=sharing](ht
tps://colab.research.google.com/drive/18_L_OX4YPlAHdQCSMfRgjTE9aSOEl-6l?usp=sharing)

Let me know in the comments what y
ou liked / didn’t like about this and I’ll make it better next time.

or if you need clarifications, I‘m happy to answer
 to the best of my ability.
```
---

     
 
all -  [ Getting Answers from GPT based on document ](https://www.reddit.com/r/ChatGPT/comments/1cp4mt7/getting_answers_from_gpt_based_on_document/) , 2024-05-12-0911
```
Using the api how to give a large amount of information then receive answers from the given data. 

What is the best, mo
st cost efficient solution.
Assistants API? Langchain?
```
---

     
 
all -  [ What's the scoop on serialization? It's all over the show with LangChain ](https://www.reddit.com/r/LangChain/comments/1cp3y1l/whats_the_scoop_on_serialization_its_all_over_the/) , 2024-05-12-0911
```
Hi am I doing something wrong?

I'm using Documents and I want to save/load them. I've tried, \`.json()\` the new \`load
\` module's \`.dumpd()\` and \`.load()\` -- but some documents can't be deserialized.

e.g. I am trying to build somethi
ng that uses LangChain documents. But not all of them are deserializable -- instead you get goop like this when using th
e output of \`ContextualCompressionRetriever\` (which returns some documents) and use one of the above functions to seri
alize:

https://preview.redd.it/74vlfp1wsozc1.png?width=417&format=png&auto=webp&s=0d3d238376da4f9305eed45ee212ce8736025
26e

Basically I have to parse the repr to get the document? Any pointers? Or write my own custom serialization/deserial
ization?
```
---

     
 
all -  [ Ai generated ad that was on my feed ](https://i.redd.it/doitcfsajozc1.jpeg) , 2024-05-12-0911
```
How lazy is a company to use AI?
```
---

     
 
all -  [ how to get LLM to infer dates from a json file or text file? ](https://www.reddit.com/r/LangChain/comments/1coz2io/how_to_get_llm_to_infer_dates_from_a_json_file_or/) , 2024-05-12-0911
```
im currently using mistral-small in my project, i want to create a chatbot that can give answers about the weather in th
e future, so i have a huge json file that i want to feed to the model as a vector embedding and then let the user ask th
e chatbot questions about future weather such as what should i wear tomorrow etc.

the problem is that the LLM seems to 
not read the files, i even tried to programatically rebuild the file as a text file.

this is my code:

\`\`\`

    json
_loader = JSONLoader('C:\\xxxx\\data\\all_weather_by_date.json')
    
    
    # Split text into chunks
    text_splitte
r = RecursiveCharacterTextSplitter()
    documents = text_splitter.split_documents(docs)
    # Define the embedding mode
l
    embeddings = MistralAIEmbeddings(model='mistral-embed', mistral_api_key='XXXXXXXXXXXXXXXXXXXXXXX', )
    # Create 
the vector store 
    vector = FAISS.from_documents(documents, embeddings)
    vector.save_local('cache')
    
    # Def
ine a retriever interface
    retriever = vector.as_retriever()
    # Define LLM
    model = ChatMistralAI(mistral_api_k
ey='XXXXXXXXXXXXXXXXXXXXX', model='mistral-small', temperature=1)
    # Define prompt template
    prompt = ChatPromptTe
mplate.from_template('''
    
    <context>
    {context}
    </context>
    
    Question: {input}''')
    
    # Creat
e a retrieval chain to answer questions
    document_chain = create_stuff_documents_chain(model, prompt)
    retrieval_c
hain = create_retrieval_chain(retriever, document_chain)
    response = retrieval_chain.invoke({'context': instructions,
'input': f'answer max 60 words, end with follow-up question, no clauses: what should i wear tomorrow? today is 10.5.2024
'})
    print(response['answer'])

\`\`\`

my json is built like this:

{

'current\_year\_dates' : {

'2024.05.11' : {


'humidity': '50%',

'degrees': '34'

}

.... all the other dates throught the year

}

when i attempted to change the j
son file to text file, i changed it to this format:

'on 2024.10.5 there will be 50% humidity and 30 degress.'

and stil
l it didnt work



also i have always get a warning when running my code about HF\_TOKEN not being set and using len spl
itter.

please help me!
```
---

     
 
all -  [ LangChain 0.2 prerelease ](https://www.reddit.com/r/LangChain/comments/1coyy48/langchain_02_prerelease/) , 2024-05-12-0911
```
hi all! we're gearing up for a release of langchain 0.2. The main change is no longer depending on langchain-community (
this will increase modularity, decrease size of package, make more secure). We're also adding in a new docs structure an
d highlighting a bunch of the changes we made as part of 0.1

We posted more about this on GitHub (https://github.com/la
ngchain-ai/langchain/discussions/21437) but happy to answer any questions here! Would obviously love and really apprecia
te any feedback :)
```
---

     
 
all -  [ Library that automatically creates a UI for your chatbot? ](https://www.reddit.com/r/LangChain/comments/1cot1we/library_that_automatically_creates_a_ui_for_your/) , 2024-05-12-0911
```
[Cycls](https://docs.cycls.com/getting-started) Python library significantly simplifies the development of AI chatbots f
or developers, particularly those who specialize in backend development and may find creating user interfaces tiring. Th
is library eliminates the need to develop a UI from scratch by providing a prebuilt, ChatGPTlike user interface that dev
elopers can use immediately. By simply importing Cycls into your project, you can integrate it with major LLM Python lib
raries and APIs, enabling the use of various LLM models easily.

Upon importing and running your application, it is auto
matically deployed with the user interface and a public URL, enhancing the efficiency of both development and testing pr
ocesses. This feature is especially valuable for speeding up deployment and reducing the workload on developers focusing
 on backend functionalities.


```
---

     
 
all -  [ duckduckgo_search with langchain ](https://www.reddit.com/r/duckduckgo/comments/1coso6p/duckduckgo_search_with_langchain/) , 2024-05-12-0911
```
am using duckduckgo\_search with langchain community , it was working fine but am getting rate limit error i have alread
y tried to upgrade but still the same error . is there any one who can tell me why
```
---

     
 
all -  [ Nomic embeddings with Ollama using Langchain up to Pinecone ](https://www.reddit.com/r/ollama/comments/1corjsr/nomic_embeddings_with_ollama_using_langchain_up/) , 2024-05-12-0911
```
Anyone attempted this yet?  I have a lot of familiarity using open AI embeddings up to Pinecone and I want to switch to 
Nomic. 

Reviewed the Langchain Python documentation on using nomic embeddings and it seems incomplete to enable me to p
ush up embeddings and text and metadata in the format that I’m used to with OpenAI’s embeddings and pinecone. 


```
---

     
 
all -  [ Would LC be a good platform for building a LLM-based chat which builds user profiles? ](https://www.reddit.com/r/LangChain/comments/1cooqdx/would_lc_be_a_good_platform_for_building_a/) , 2024-05-12-0911
```
Would LC be a good <framework> for building a LLM-based chat which builds user profiles?

For example, over the course o
f the conversation it could fill slots such as name, location, etc. 

or there an off the shelf tool which is already do
ing this? 
```
---

     
 
all -  [ Just a question on LCEL vs RetrievalQA ](https://www.reddit.com/r/LangChain/comments/1colp4k/just_a_question_on_lcel_vs_retrievalqa/) , 2024-05-12-0911
```
Hi all, in the previous version of code, I had something like this:

qa = RetrievalQA.from\_chain\_type(  
 llm=llm,  
 
chain\_type\_kwargs={'prompt': prompt},  
 retriever=retriever,  
 return\_source\_documents=True,          
 tags = tag
s,  
 metadata = metadata          
 )  
basically its a Multivector retriever with RetrievalQA.   In LCEL chain it is l
ike below:

chain = (  
{'context': retriever, 'question': RunnablePassthrough()}  
 | prompt  
 | model  
 | StrOutputP
arser()  
)  
The question I have is, how to add additional parameters in the above LCEL chain?   
additional parameters
:  
return\_source\_documents=True,          
tags = tags,  
metadata = metadata   
```
---

     
 
all -  [ Phi3 text2sql ](https://www.reddit.com/r/LangChain/comments/1colhlx/phi3_text2sql/) , 2024-05-12-0911
```
Has anyone tried phi3 for text2sql in postgres? I am trying and can't generate a correct query
```
---

     
 
all -  [ [For Hire] Programmer/Web Developer/IT Consultant (Python, PHP, AI, etc.) ](https://www.reddit.com/r/forhire/comments/1cola2g/for_hire_programmerweb_developerit_consultant/) , 2024-05-12-0911
```
To get in contact, please message me, I don't use the chat thing and might miss you or reply very late. Then we can swit
ch to email/discord/telegram or whatever else. Apologies for starting with this, but many missed it when it was lower.


I'm a programmer/web developer with 14 years of professional experience. I am available for all sorts of programming and
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

Rate is $50/h.

Portfolio:

https://bdabkowski.yum.pl

Satisfied customer
s:

https://www.reddit.com/r/testimonials/comments/2e8gqy/pos_uqui_need_a_backend_web_dev_look_no_further/

https://www.
reddit.com/r/testimonials/comments/7fsdze/pos_hiring_uqui_was_an_example_of_how_it_should/

https://www.reddit.com/r/tes
timonials/comments/80pu9l/pos_uqui_great_work_detailed_and_fast/

https://www.reddit.com/r/testimonials/comments/b0nx68/
uqui_is_a_hardworking_intelligent_honest_apps/

https://www.reddit.com/r/testimonials/comments/j3mz3p/uqui_is_a_great_we
b_development_consultant_with/

https://www.reddit.com/r/testimonials/comments/v40ay3/pos_uqui_is_a_great_backend_dev_to
_work_with/

Please note: I am not a designer. To make it clear, it means zero aesthetic sense.
```
---

     
 
all -  [ How to deploy langchain chatbot (agent) using flask api and identify and manage unique user conversa ](https://www.reddit.com/r/learnpython/comments/1col188/how_to_deploy_langchain_chatbot_agent_using_flask/) , 2024-05-12-0911
```
Hi, guys. I've made a langchain chatbot agent and I want to deploy it as a simple flask app.  
I'm not sure, how the uni
que conversation sessions would be managed like a single endpoint would be used to invoke the agent but how the flask wo
uld ensure that this request belong to a specific user interacting with chatbot and we know there could be multiple user
s interacting with chatbot at same time.

So I wanna learn how to manage these kind of sessions and using credentials is
 not an option.

one more thing, how the agent memory would be specified per user session in deployment?
```
---

     
 
all -  [ Function Calling + RAG + Langchain Tool Calling Agent + REDIS Memory ](https://www.reddit.com/r/LangChain/comments/1cokru8/function_calling_rag_langchain_tool_calling_agent/) , 2024-05-12-0911
```
Tell me if this idea is feasible and how I can pull this off

I have a langchain agent that does function calling, but o
ne shortcoming is that it fails to answer queries from the pulled data many times, 

Can I store this pulled data into a
 knowledge graph vector database as this data is for holiday packages with key value relations such as duration, price, 
location, ref\_id etc and sub categories like fare sets, cabin sub categories etc. 

How can I make my langchain agent i
n python better using knowledge graphs and making it answer follow up questions using RAG on the last fetched data?


```
---

     
 
all -  [ How to deploy langchain chatbot (agent) using flask api and identify and manage unique user conversa ](https://www.reddit.com/r/LangChain/comments/1cokd2v/how_to_deploy_langchain_chatbot_agent_using_flask/) , 2024-05-12-0911
```
Hi, guys. I've made a langchain chatbot agent and I want to deploy it as a simple flask app.  
I'm not sure, how the uni
que conversation sessions would be managed like a single endpoint would be used to invoke the agent but how the flask wo
uld ensure that this request belong to a specific user interacting with chatbot and we know there could be multiple user
s interacting with chatbot at same time. 

So I wanna learn how to manage these kind of sessions and using credentials i
s not an option.

  
one more thing, how the agent memory would be specified per user session in deployment?
```
---

     
 
all -  [ Profile Review ](https://i.redd.it/0dwb8qutwjzc1.jpeg) , 2024-05-12-0911
```
Thoughts on my profile? Trying to land full-stack AI jobs. Interested in any feedback, even if it’s brutal as long as it
’s actionable.
```
---

     
 
all -  [ Evaluation Models - GPT-3.5 vs. GPT 4 Turbo ](https://www.reddit.com/r/LangChain/comments/1coj65b/evaluation_models_gpt35_vs_gpt_4_turbo/) , 2024-05-12-0911
```
hey guys

I use correctness, hallucination & relevance score to evaluate a RAG chain on langsmith. 

Generally, do you t
hink 3.5 is good enough to evaluate the outcomes?
```
---

     
 
all -  [ LLAMA2 (and Other Models) Engaging in Self-Dialogue: Asking and Answering Its Own Questions ](https://www.reddit.com/r/LLMDevs/comments/1coigub/llama2_and_other_models_engaging_in_selfdialogue/) , 2024-05-12-0911
```
I am using Langchain + different LLM models ('Llama-2-7b-chat-hf', 'Mistral-7B-Instruct-v0.2', ...)..

\*\*My purpose\*\
* is to do prompt engineering and evaluate a model's ability to answer various questions.

\*\*The challenge\*\* is that
 after posing almost any question, the LLM starts a self-conversation, asking itself questions as a 'Human' and then ans
wering them as an 'AI.'

\*\*What am I missing?\*\*

\*\*How can I ensure\*\* the model only responds to the original qu
estion without engaging in a self-conversation?

    conversation = ConversationChain(
      llm=self.llm,
      memory=
ConversationBufferMemory(),
      verbose=False)
    
    print('*************************** chat_conversation *********
******************')
    
    while True:
      user_input = input('> ')            
      ai_response = conversation.pr
edict(input=user_input)
      print('\nAssistant:\n', ai_response)
      print('----------------------------------------
--------------------------------------------------------------\n\n\n')



Example for a prompt:



https://preview.redd.
it/cprggyrahjzc1.png?width=1458&format=png&auto=webp&s=2b9b230a3123d415b7015c7131f5eddf44efedb5

  


  

```
---

     
 
all -  [ How to add JsonOutputParser with RunnableWithMessageHistory? ](https://www.reddit.com/r/LangChain/comments/1cofbkc/how_to_add_jsonoutputparser_with/) , 2024-05-12-0911
```
This my code

    conversational_rag_chain = RunnableWithMessageHistory(
        rag_chain,
        get_session_history,

        input_messages_key='input',
        history_messages_key='chat_history',
        output_messages_key='answer',

    )
    
    conversational_rag_chain.invoke(
        {'input': 'I am interested in Screwdrivers, Sockets, Ratchets. N
ow generate new questions based on past behaviour'},
        config={
            'configurable': {'session_id': 'abc123
'}
        },  # constructs a key 'abc123' in `store`.
    )['answer']
    

I want to add this \`JsonOutputParser\` to 
above \`conversational\_rag\_chain\`

    class ProbingQuestion(BaseModel):
        Question: str = Field(description='p
robing question')
        Options: List[str] = Field(description='list of options for the probing question')
    
    
 
   output_parser = JsonOutputParser(pydantic_object=ProbingQuestion)



So can anyone help this?
```
---

     
 
all -  [ A Daily chronicle of AI Innovations May 09th 2024: 🤖 OpenAI posts Model Spec revealing how it wants  ](https://readaloudforme.com/index_subscribers) , 2024-05-12-0911
```
A Daily chronicle of AI Innovations May 09th 2024: 
🤖 OpenAI posts Model Spec revealing how it wants AI to behave 
🧬 Goo
gle DeepMind unveils AlphaFold 3, the next generation of its protein prediction model 🧠 Neuralink faces setback as first
 human brain implant encounters problem 
🕵️‍♀️  Microsoft developed a secretive AI service for US spies 
🎨 Generate imag
es on Midjourney Alpha 📝Copilot for Microsoft 365 to get auto-complete and rewrite to improve prompts 
🏢New AI data cent
er to be built at the failed Foxconn project site in Wisconsin 
🤔Sam Altman says we are not taking AI’s impact on the ec
onomy seriously 
✒️Typeface Arc replaces prompts; uses AI agent approach to ease marketing workflows 🎮Altera’s gaming AI
 agents get backed by Eric Schmidt, Former Google CEO

 

🤖 OpenAI posts Model Spec revealing how it wants AI to behave


 

OpenAI has introduced the first draft of Model Spec, a proposed framework aiming to shape how AI models respond, emp
hasizing assistance, humanity's benefit, and adherence to social norms and laws.
The framework suggests specific rules f
or AI behavior, including compliance with laws, protection of privacy, and avoidance of NSFW content, with options to ad
just settings like allowing NSFW content in certain contexts.
While the Model Spec seeks public feedback for future adju
stments and doesn't immediately affect existing models like GPT-4 or DALL-E 3, it's envisioned as a living document to g
uide AI behavior improvement over time.
Source: https://readaloudforme.com/index_subscribers

🧬 Google DeepMind unveils 
AlphaFold 3, the next generation of its protein prediction model 

https://youtu.be/9ufplEgtq8w?si=XAREDQVZwYLBtcss



G
oogle DeepMind and Isomorphic Labs have released AlphaFold 3, a new AI model for predicting protein structures, includin
g their interactions with various molecules such as DNA, RNA, and small molecules, thereby enhancing drug discovery poss
ibilities.
This new version is more precise in mapping out complex groupings of molecules, significantly enhancing our a
bility to understand and predict molecular behavior compared to its earlier version.
Google will not open-source this ve
rsion but has launched AlphaFold Server for non-commercial research use, aiming to balance intellectual property concern
s with accessibility for scientific progress.
Source: https://readaloudforme.com/index_subscribers

🧠 Neuralink faces se
tback as first human brain implant encounters problem 

Neuralink admitted that some of the micro-thin threads from thei
r N1 brain chip retracted after implantation in the first human patient, possibly due to air trapped in the skull during
 surgery, which affected the device's data transmission rate.
Despite the retraction of several threads, Neuralink manag
ed to increase the data transmission speed over time by optimizing their recording algorithm and improving signal transl
ation into cursor movements.
The company is planning further implants, with goals to implant two more patients in the co
ming months and ten in total this year, while continuing to refine their technology and reporting developments to the FD
A.
Source: https://readaloudforme.com/index_subscribers

🕵️‍♀️ Microsoft developed a secretive AI service for US spies


Microsoft has developed a top-secret generative AI model entirely disconnected from the internet so US intelligence agen
cies can safely harness the powerful technology to analyze top-secret info. The model based on GPT-4 is now live, answer
ing questions, and will also write code.

Microsoft spent 18 months developing the model, which is 'air-gapped' to ensur
e it is secure. This is the first time a model is fully isolated– meaning it's not connected to the internet but is on a
 special network that's only accessible by the U.S. government.

It can read and analyze files but cannot learn from the
m to stop sensitive information from entering the platform. It is yet to be tested and accredited by the intelligence ag
encies.

Why does this matter?

Intelligence agencies all over the world have been racing to be the first to harness gen
erative AI. I guess we know who’s going to be the winner. If this AI tool is successful, it will fundamentally change th
e way intelligence agencies operate.

Source: https://readaloudforme.com/index_subscribers

What Else Is Happening in AI
 on May 09th 2024❗

📝Copilot for Microsoft 365 to get auto-complete and rewrite to improve prompts

In coming months, Mi
crosoft Copilot will be updated with new features like auto-complete and ‘elaborate your prompt’ that offer suggestions 
to improve AI prompts. It aims to solve the problem of coming up with good prompts for generative AI. (Link)

🏢New AI da
ta center to be built at the failed Foxconn project site in Wisconsin

President Joe Biden announced an AI data center t
o be built on the same site as the failed Foxconn project in Racine, Wisconsin. According to a White House press release
, Microsoft is investing $3.3B in the project, creating up to 2,000 permanent jobs. (Link)

🤔Sam Altman says we are not 
taking AI’s impact on the economy seriously

At a Brooking's Institute panel about AI and geopolitics on Tuesday, Altman
 said the discussions around AI's effect on the economy–  like how it may lead to mass job replacement– died down this y
ear compared to last. He said if we don’t take these concerns seriously enough going forward, it could be a massive issu
e. (Link)

✒️Typeface Arc replaces prompts; uses AI agent approach to ease marketing workflows

It is launching Typeface
 Arc technology, which enables a user to state a high-level marketing objective and then have the system automatically p
lan and generate all the assets, including emails, images, and notifications that are all connected. (Link)

🎮Altera’s g
aming AI agents get backed by Eric Schmidt, Former Google CEO

Altera is the newest startup joining the fray to build a 
new guard of AI agents. It raised $9 million in an oversubscribed seed round, co-led by Eric Schmidt’s deep-tech fund, F
irst Spark Ventures and Patron, the seed-stage fund co-founded by Riot Games alums. (Link)

 

AI TRAINING May 09th 2024


🎨 Generate images on Midjourney Alpha

Generate images on Midjourney Alpha 
Midjourney’s website is now accessible to 
anyone with more than 100 generated images, improving the experience when prompting images over its standard Discord gro
up.

Check that you’ve generated more than 100 images by typing /info in the Midjourney Discord group. If you have, head
 over to Midjourney Alpha.

In the main menu, you can explore other creations and search prompts.

Select where it says 
“imagine” and enter your prompt to generate an image.

Add a reference image by selecting “+” or play with different par
ameters such as image size, stylization, or even weirdness by pressing the “slider control” button

AI RESEARCH on May 0
9th 2024

📶 AI usage surges in the workplace

AI usage surges in the workplace
Microsoft and LinkedIn just published the
ir Work Trend Index Annual Report, revealing that AI adoption is surging in the workplace — calling 2024 the ‘year AI at
 work gets real’.

The report found that use of GenAI has doubled in the last six months, with 75% of knowledge workers 
using the tech in some capacity.

78% of AI users are bringing their own AI to work — with 52% reporting they are reluct
ant to admit to its use.

66% of leaders wouldn't hire someone without AI skills, and 71% prefer less experienced candid
ates with AI aptitude over a more experienced one without it.

AI power users reported enhanced productivity, creativity
, and job satisfaction compared to skeptical peers.

Why it matters: Employees are adopting AI at a rapid pace, regardle
ss of if their own organizations are ready for the shift. As AI spreads across all sectors, generations, and skillsets, 
the early adopters are rising to the top — while those that aren’t at least exploring the tech are quickly running out o
f time

Trending AI Tools May 09th 2024

📍GeoSpy - Uncover photo locations with AI

🧑‍💻 LangChain - Connect LLMs to priv
ate data for context-aware applications

📊 Abstra - Scale business processes with Python and AI

🎨 Freepik Pikaso Upscal
er - Integrated with Magnific, enlarge images without losing quality

💬 Notion AI Q&A - Q&A is now open to the public, a
llowing users to ask and find information across their workspace

🎵 Udio Audio Inpainting - Select a portion of an AI-ge
nerated music track and regenerate it

New AI Job Opportunities on May 09th 2024

🎥 The Rundown - Video Content Creator


🤖 Anthropic - Research Engineer, Human-Computer Interfaces

👩‍💻 Adept AI - Solutions Engineer

📝 Mistral AI - Data Anno
tation Technical Program Manager

```
---

     
 
all -  [ How can I go about creating knowledge graphs from chunks of a document? ](https://www.reddit.com/r/LangChain/comments/1codtrj/how_can_i_go_about_creating_knowledge_graphs_from/) , 2024-05-12-0911
```
I want to improve the quality of retrieval for my RAG application. I have a knowledge base with multiple pdfs and docs, 
and currently I'm using basic recursive splitter with overlap for creating chunks. This is not the most effective way, a
nd I'm thinking of using semantic or agentic chunking to improve the quality of my chunks.

Furthermore, I'm also thinki
ng to use knowledge-graphs for this usecase. Now I understand how knowledge-graphs work but I'm not sure how I can use t
hem for my usecase.

Firstoff, I would need to define some nodes (which could be my chunked documents itself I believe) 
but I'm unsure about how to and to what extent create relationships between those nodes. Again, this is my theory, would
 love to understand if nodes could be something else here.

IF, I decide on nodes being documents, how should I decide p
arameters for my relationships? Do I need to make LLM calls for this? -- this would incur more cost I as I keep adding d
ocuments to my knowledge base.

I'm thinking of extracting key entities from each document, and use those as the basis o
f relationship but -- for that I would need a model for extraction (which I guess, I could find some standard NLP techni
que that are not LLM or even SLM based).

Any thoughts on this would be appreciated. Thanks!
```
---

     
 
all -  [ Iterating hundreds of csv file headers, trying to find the best way to identify related headers usin ](https://www.reddit.com/r/LangChain/comments/1code3k/iterating_hundreds_of_csv_file_headers_trying_to/) , 2024-05-12-0911
```
I have a Neo4j graph that's populated with common category nodes, and sub-nodes. These all have labels and names, other 
than that there is no data stored inside the properties. I want to find a way to identify related headers for that parti
cular category node, for example 'economic', if a column in one of the CSV files is related to economics then it should 
be either be added as a new node to that category node or the data inside that cell from the csv be added as a property 
to an existing node. I'm wondering what everyone also thinks is the best way to set all this up as I am trying to make t
his Graph as efficient as possible because the plan is to add an LLM on top of it with a chatbot to query to graph for c
ontext and return answers.  

```
---

     
 
all -  [ LangChain SQL & Mistral ](https://www.reddit.com/r/LangChain/comments/1cod9zr/langchain_sql_mistral/) , 2024-05-12-0911
```
Hi guys,

Recently I am experimenting on using mistral 7b instruct-v0.1 with sql database, and I have try 3 approach, bu
t all of these give me several errors and issues, and I really cannot fix it.  
Approach 1 (source=[Tal to your database
 using RAG and LLM](https://medium.com/@shivansh.kaushik/talk-to-your-database-using-rag-and-llms-42eb852d2a3c))

https:
//preview.redd.it/hr1yz5w30izc1.png?width=767&format=png&auto=webp&s=2de4ee09e1b184434f3c6baf0a7040000987dbed

https://p
review.redd.it/uyas7shgjdzc1.png?width=953&format=png&auto=webp&s=61b093e5253e193c1f02d69ba6890566a25858a9

This give me
 the error as above, but i thought the question is already a string? And it's so weird to give me 2 SQL Result and answe
r.  


Approach 2 (source is from a youtube)

https://preview.redd.it/n4vj9z2e0izc1.png?width=930&format=png&auto=webp&s
=3d9ea5d0b76e5ba224f1a55e2abb7b5f130de8d0

Approach 3

https://preview.redd.it/wdc8l03j0izc1.png?width=750&format=png&au
to=webp&s=0dcff653e8367b20ad6b4dcba5742bd4d7585bb9

  
This same as approach 1, it gives me 2 different result and answe
r.  
How if i want just only the final answer? How can I get it? print(result\[Answer\])?  

```
---

     
 
all -  [ Vectorsearch for chat history? ](https://www.reddit.com/r/LangChain/comments/1coaa4f/vectorsearch_for_chat_history/) , 2024-05-12-0911
```
Hi guys,
I'm working on a chatbot for our company and we use ChatGPT 4 as an LLM. To keep the costs per request low, I i
mplemented a chat history with only the last 6 messages (3 from user, 3 from bot)

The problem now is, that sometimes pe
ople have inputs that the bot can't answer well, as the messages are already gone in his memory.

Is there any good way 
to fix this? 
Is it possible to use vectorsearch for memory? Or does this heavily increase the latency?

What is the bes
t way to go, what are you guys using?
```
---

     
 
all -  [ LangChain ReAct Argumentation Agent ](https://www.reddit.com/r/LangChain/comments/1co86cn/langchain_react_argumentation_agent/) , 2024-05-12-0911
```
Hello,

Currently, I'm using LangChain to develop a ReAct agent to develop evidence-based arguments supporting the user'
s input. I've successfully developed a Tool that can access data from a web source based on what the model queries. ReAc
t seems like a sensible pattern for this use case, but the model gets stuck in a loop, repeatedly asking the same query 
of the tool. I've also noticed that the conversation history is not populated.

Here is the code I developed. The `searc
h_cse(query)` function just returns the title and text of an article.

    from keys import GOOGLE_GEMINI_API_KEY
    fr
om google_website_scrape import search_cse
    import langchain
    from langchain_core.tools import Tool
    from langc
hain.agents import initialize_agent, AgentType
    from langchain_google_genai import ChatGoogleGenerativeAI
    from la
ngchain.memory import ConversationBufferMemory
    
    langchain.debug = True
    
    llm = ChatGoogleGenerativeAI(
  
      model='gemini-1.0-pro',
        google_api_key=GOOGLE_GEMINI_API_KEY
    )
    tools = [
        Tool(
           
 name='cbs_articles',
            description='This tool provides the content of CBS News articles that pertain to the r
equest.',
            func=search_cse
        )
    ]
    
    PREFIX = '''You are an agent designed to construct argume
nts to fulfill the user's request, specified in the input.
    You arguments must include evidence from CBS News article
s.'''
    FORMAT_INSTRUCTIONS = '''You MUST use the following format: Question, Though, Action, Action Input. This forma
t is explained in further depth below:
    
    Question: This should be the input.
    Thought: You should think about 
arguments to fulfill the user's request.
    Action: Should ALWAYS BE 'cbs_articles'. Do NOT use any other action.
    A
ction Input: This should be a search term that will give you information pertaining to the argument you are trying to ju
stify.
    Observation: You should consider how the information you found supports your argument.
    ... (this Thought/
Action/Action Input/Observation can repeat N times)
    Thought: I now have multiple arguments WITH EVIDENCE to fulfill 
the user's request.
    Final Answer: Here are the arguments WITH EVIDENCE to fulfill the user's request.'''
    SUFFIX 
= '''Begin!
    
    Input: Justify the following: '{input}'
    Thought: {agent_scratchpad}
    Chat History: {chat_his
tory}'''
    
    memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)
    agent = initial
ize_agent(
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        tools=tools,
        llm=llm,
        agent_kwar
gs={
            'prefix': PREFIX,
            'format_instructions': FORMAT_INSTRUCTIONS,
            'suffix': SUFFIX,

            'input_variables': ['input', 'agent_scratchpad', 'chat_history']
        },
        memory=memory,
        
verbose=True,
        handle_parsing_errors=True,
        max_iterations=10
    )
    
    print(agent.run('Electric veh
icles should not be mandated nationally.'))

With this code, the model repeatedly asks itself the following.

    Questi
on: Electric vehicles should not be mandated nationally.
    Thought: Electric vehicles are still too expensive for many
 people.
    Action: cbs_articles
    Action Input: Electric vehicles cost
    Observation:
    [ARTICLE TITLE & CONTENT
]

Please advise me if I'm using the ReAct pattern incorrectly. Thank you for your time.
```
---

     
 
all -  [ Llama3 slow inference ](https://www.reddit.com/r/learnmachinelearning/comments/1co759v/llama3_slow_inference/) , 2024-05-12-0911
```
I'm currently using llama3 for a rag app. I'm using ollama and langchain's chatollama function to run inference. Prompti
ng the model takes between 10 to 30 seconds to return a json response. Is there any way to significantly reduce this inf
erence time (particularly, to under 1 sec)? 

Also, I've heard that Mojo can be used for speeding up machine learning ap
ps. Is there a Mojo implementation of llama3 available?
```
---

     
 
all -  [ RAG Retrieval Evaluation ](https://www.reddit.com/r/LangChain/comments/1co5cl1/rag_retrieval_evaluation/) , 2024-05-12-0911
```
Hey,

Like many others I am working on a RAG Q&A Chatbot.  I have many pdfs related to a certain topic. My goal is to he
lp the end-user answer questions based on the information in the pdfs. From the perspective of GIGO I am first evaluatio
n how well I can retrieve information related to certain questions. However, I am not certain about my approach.

I am u
sing precision at k, recall at k and ndcg at k as my evaluation metrics; next I simply create various pipelines starting
 from the raw pdfs, to embedding to retrieval. Here I vary the following element in the pipeline:

**Chunking:**

* Char
acterTextSplitter vs RecursiveTextSplitter
* Chuck size (400, 800, 1200)
* Chuck overlap (200, 400, 600)

**Embedding:**


* Model (ie. OpenAI vs Cohore)

**Retrieval:**

* Search method: mmr vs similarity
* Number of Documents to return \[k
\] (4, 7)
* Number of Documents to fetch to pass to MMR algorithm \[fetch-k\] (20, 40)

Retrieval is tested as follows; 
at the chunking stage I sample \~10% of the chucks and pass that to an LLM to generate questions. These are then used to
 test how well the pipeline can retrieve the chucks related to the questions.

**Now my problems:**

1. I consider a sin
gle pdf, one document. This document is then chucked, but the document ID is the same for each chuck. Meaning that if a 
question related to chuck A returns chuck Z; this would be counted as correct. While this would obviously not be correct
; I've considered changing the relation from a single page in a pdf being considered one document as this is likely more
 accurate.
2. The evaluation questions generated vary with the chuck size and method; as the given input to the LLM will
 be different. So while testing the pipeline, this is strongly affected by the quality of questions the LLM came up with
.

Are there people here with experience in testing, or does anyone know any good resources?

Thanks!
```
---

     
 
all -  [ Langchain openai FINE TUNING ](https://www.reddit.com/r/LangChain/comments/1co28ib/langchain_openai_fine_tuning/) , 2024-05-12-0911
```
I tried to do fine tuning in openai for limit the topics that my model can to speak, but the model runs bad, for example
 the result has seen like this:

GOOD: good answer 
BAD: bad answer

Q: Who is Taylor Swift? (GOOD)
A: Sorry….

Q: What 
is the sincope in life Sciences? (GOOD)
A: The sincope is…

Q: Hello (BAD)
A: sorry….

… I ask for 5 questions about Lif
e Science
Q: give me the answer of question Numbers 3 (BAD)
A: sorry….

How can I fix it ?

```
---

     
 
all -  [ Langchain allways return 429 error; este limit ](https://www.reddit.com/r/LangChain/comments/1co213w/langchain_allways_return_429_error_este_limit/) , 2024-05-12-0911
```
I have an llm built with langchain, OPENAI and qdrant; in production run well but in my local my app allways return 429 
error; I changed 5 times my tokens, I added 50$ more to my OPENAI account; but the issue persist.

Did anyone have this 
issue ?

```
---

     
 
all -  [ Limitations with existing prompt management tools?  ](https://www.reddit.com/r/LangChain/comments/1co09cc/limitations_with_existing_prompt_management_tools/) , 2024-05-12-0911
```
Hey y’all 🙌🏼 I’ve been using some prompt management tools (Humanloop and Braintrust Data) for a few of my recent project
s. Overall, they’re powerful tools but I’ve hit a few snags that make me wonder if a better tool can be built. 

I'm rea
lly interested in hearing about others' experiences with similar tools, so if you’re willing to share, that would be awe
some! 🫶🏼 

- What tool are you using? 
- How much does it cost you? 
- What kind of issues have you run into while using
 this tool?
- Are there specific features that you feel are lacking? 
- If you could build a wish list of features, what
 would they be? 🌟
```
---

     
 
all -  [ Rag response always includes reference to document  ](https://www.reddit.com/r/LangChain/comments/1cnxfnz/rag_response_always_includes_reference_to_document/) , 2024-05-12-0911
```
My org has this usecase to build a rag to answer questions. In rag works great given that I given it a lot of instructio
ns(prompts). One demand that rag isn't able to fullfill is to never mention document reference in the response.

Eg.
1) 
The document does not mention how to ...
2) you can view the steps on page 60 in the document.

Any prompt suggestions t
o overcome this particular scenario. The rag should never share the source of its response 

My pipeline

1) Pdf Documen
t Langchain 

2) Qdrant for retriever

3) Chat gpt3.5 turbo 16k for llm

```
---

     
 
all -  [ WooCommerce AI Chatbots / AI Agents ](https://www.reddit.com/r/wpsolr/comments/1cnve15/woocommerce_ai_chatbots_ai_agents/) , 2024-05-12-0911
```
We are looking to extend our [WooCommerce plugin](https://www.wpsolr.com/wpsolr-enterprise/) with AI ChatBots / AI Agent
s.  
Either something simple based on the [OpenAI Assistant API](https://platform.openai.com/docs/assistants/overview) a
nd [OpenAI Function Calling API](https://platform.openai.com/docs/guides/function-calling) .  
Or integration with full-
fledged solutions like [LangChain](https://www.langchain.com/), Vertex AI Agent builder, [Botpress](https://botpress.com
/), [FlowiseAI](https://flowiseai.com/).  
Contact me if you have any use cases in mind.
```
---

     
 
all -  [ Hi guys,what is the use of parameter K in ConversationEntityMemory? ](https://www.reddit.com/r/LangChain/comments/1cnu7zh/hi_guyswhat_is_the_use_of_parameter_k_in/) , 2024-05-12-0911
```
[https://api.python.langchain.com/en/latest/memory/langchain.memory.entity.ConversationEntityMemory.html](https://api.py
thon.langchain.com/en/latest/memory/langchain.memory.entity.ConversationEntityMemory.html)

https://preview.redd.it/ufmg
5yvirdzc1.png?width=488&format=png&auto=webp&s=ec24354784b8f84a445c4965f6064b9ed0cd838a


```
---

     
 
all -  [ Need help choosing LLM ops tool for prompt versioning ](https://www.reddit.com/r/llmops/comments/1cntvp0/need_help_choosing_llm_ops_tool_for_prompt/) , 2024-05-12-0911
```
We are a fairly big group with an already mature MLops stack, but LLMOps has been pretty hard.

In particular, prompt-it
eration hasn't been figured out by anyone.  
what's your go to tool for PromptOps ?

## PromptOps requirement:

Requirem
ents:

* Storing prompts and API to access them
* Versioning and visual diffs for results
* Evals to track improvement a
s prompts are develop .... or ability to define custom evals
* Good integration with complex langchain workflows
* Traci
ng batch evals on personal datasets, also batch evals to keep track of prompt drift
* Nice feature -> project -> run -> 
inference call heirarchy
* report generation for human evaluation of new vs old prompt results

## LLM Ops requirement -
> orchestration

* a clean way to define and visualize task vs pipeline
* think of a task as as chain or a self-containe
d operation (think summarize, search, a langchain tool)
* but then define the chaining using a low-code script -> which 
orchestrates these tools together
* that way it is easy to trace (the pipeline serves as a highl evel view) with easy pl
uggability.

Langchain is does some of the LLMOps stuff, but being able to use a cleaner abstraction on top of langchain
 would be nice.

None of the prompt ops tools have impressed so far. They all look like really thin visualization diff t
ools or thin abstractions on top of git for version control.

Most importantly, I DO NOT want to use their tooling to ru
n a low code LLM solution. They all seem to want to build some lang-flow like UI solution. This isn't ScratchLLM for god
's sake.

Also no, I refuse to change our entire architecture to be a startupName.completion() call. If you need to be s
o intrusive, then it is not a good LLMOps tools. Decorators & a listerner is the most I'll agree to.
```
---

     
 
all -  [ Having a hard time with templates  ](https://github.com/oovaa/ChatPDF/blob/main/exper%2Fcommandr.js) , 2024-05-12-0911
```
Hey everyone, I'm diving into LangChain and AI for the first time, so please bear with me as I navigate through this lea
rning curve. 

I've managed to create a small CLI bot with memory, and you can check out the GitHub link here: [GitHub L
ink] https://github.com/oovaa/ChatPDF/blob/main/exper%2Fcommandr.js. 

However, I'm encountering an issue where the bot 
interprets my name input as a command rather than part of the conversation. It seems to struggle with understanding the 
context of the conversation. I'd really appreciate some guidance on how to fix this. Thanks in advance for any help you 
can provide!
```
---

     
 
MachineLearning -  [ [D] Self-optimizing deterministic LLM memory using dspy, neo4j and vector databases. Need your input ](https://www.reddit.com/r/MachineLearning/comments/1cakjaf/d_selfoptimizing_deterministic_llm_memory_using/) , 2024-05-12-0911
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

     
 
deeplearning -  [ Seeking Advice: Solving Data Challenges with Large Language Models (LLMs) ](https://www.reddit.com/r/deeplearning/comments/1ca4nc1/seeking_advice_solving_data_challenges_with_large/) , 2024-05-12-0911
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

     
 
deeplearning -  [ Share the Coolest Out of The Box LLM Applications That Made You Say 'Wow that was smart' ](https://www.reddit.com/r/deeplearning/comments/1c9e6dj/share_the_coolest_out_of_the_box_llm_applications/) , 2024-05-12-0911
```
Hi, I'm looking at some LLM applications today but apart from guys doing big rags with langchain I don't see too many us
es that are out of the box or that make me say 'wow that was smart to use an LLM here'. Have you seen any cool stuff usi
ng LLMs recently that made you say 'wow, that was smart'?
```
---

     
