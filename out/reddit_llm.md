 
all -  [ agent-to-agent resiliency, observability, etc - what would you like to see? ](https://www.reddit.com/r/LangChain/comments/1h1hk7i/agenttoagent_resiliency_observability_etc_what/) , 2024-11-28-0914
```
Full disclosure, actively contributing to [https://github.com/katanemo/archgw](https://github.com/katanemo/archgw) \- an
 intelligent proxy for agents built on Envoy and redesigned for agents. Actively seeking feedback on what the community 
would like to see when it comes to agent-to-agent communication, resiliency, observability, etc. Given that a lot of peo
ple are building  task-specific agents and that  agents must communicate with each other reliably, we were seeking advic
e on what features would you like from an agent-mesh that could solve a lot of the crufty resiliency, observability chal
lenges between agents. Note: the project invests in small LLMs to handle/process certain critical tasks related to promp
ts (routing, safety, etc) so if the answer is machine learning related that's totally okay.

You can add your thoughts b
elow, or here: [https://github.com/katanemo/archgw/discussions/317](https://github.com/katanemo/archgw/discussions/317).
 I’ll merge duplicates so feel free to comment away
```
---

     
 
all -  [ How to Make Parallel Requests for the Same Text Using Different Variables ](https://www.reddit.com/r/LangChain/comments/1h1h2vn/how_to_make_parallel_requests_for_the_same_text/) , 2024-11-28-0914
```
I’m a beginner with LangChain, and I’m working on a project that requires making parallel requests to process the same i
nput text across multiple categories. Here’s the challenge: each category needs a different set of examples to guide the
 output generation.

Here’s what I’m trying to achieve:

1. I have a single input text that needs to be processed.
2. Fo
r each category (e.g., 'medications,' 'family history,' 'exams'), I have a unique prompt and a specific set of examples.

3. I want to execute these requests in parallel to improve efficiency.
4. I’m using RunnableParallel, but I’m strugglin
g to figure out the best way to handle the examples dynamically for each category.

What I’ve tried so far:

* Passing e
xamples dynamically during the request.
   * Formatting prompts by embedding examples beforehand. However, I either enco
unter issues with missing inputs variables.

I’m new to LangChain, so any help or suggestions (even simple ones!) would 
be highly appreciated.

    chains = {}
    inputs = {}
    for category, content in prompts.get('medical_queries', {}).
items():
        try:
            prompt_content = content['prompt']
            prompt_examples = content['examples']
 
   
            prompt_template = ChatPromptTemplate.from_template(prompt_content)
    
            chains[category] = L
LMChain(prompt=prompt_template, llm=llm)
    
            inputs[category] = {'input': text, 'example': content['example
s']}
        except Exception as e:
            print(f'{category}: {e}')
    
    pipeline = RunnableParallel(chains)
 
   
    responses = pipeline.invoke(inputs)
    
```
---

     
 
all -  [ Is Semantic Chunking worth the computational cost? ](https://www.vectara.com/blog/is-semantic-chunking-worth-the-computational-cost) , 2024-11-28-0914
```

```
---

     
 
all -  [ Multi-agent supervisor langgrpah giving error ](https://www.reddit.com/r/GoogleColab/comments/1h1ba4c/multiagent_supervisor_langgrpah_giving_error/) , 2024-11-28-0914
```
I was making a supervised agent using langgraph with two agents (rag and sql) using the template from langchain below

O
fficial Doc one : [https://colab.research.google.com/drive/1KEe9YSTGDQopMuss3CSMHJ3VjDzzrGSh?usp=sharing](https://colab.
research.google.com/drive/1KEe9YSTGDQopMuss3CSMHJ3VjDzzrGSh?usp=sharing)

My code: [https://colab.research.google.com/dr
ive/1QszbxpiFJkhWWYhBpSmDCX\_3MMMeHVdd?usp=sharing](https://colab.research.google.com/drive/1QszbxpiFJkhWWYhBpSmDCX_3MMM
eHVdd?usp=sharing)

however when i run my code above at the end i get the error below which seems routeresponse should g
enerate in json and it doesnt. Any idea how i can fix this will be very much appreciated:

>OutputParserException: Funct
ion RouteResponse arguments:

>{  
next: 'Rag\_agent'  
}

>are not valid JSON. Received JSONDecodeError Expecting prope
rty name enclosed in double quotes: line 2 column 5 (char 6)
```
---

     
 
all -  [ Noob on chunks/message threads/chains - best way forward when analyzing bank account statement trans ](https://www.reddit.com/r/LangChain/comments/1h1aiy7/noob_on_chunksmessage_threadschains_best_way/) , 2024-11-28-0914
```
## CONTEXT:
I'm a noob building an app that takes in bank account statement PDFs and extracts the peak balance from each
 of them. I'm receiving these statements in multiple formats, different countries, languages. My app won't know their fo
rmats beforehand.

## HOW I AM TRYING TO BUILD IT:
Currently, I'm trying to build it by extracting markdown from the PDF
 with Docling and sending the markdown to OpenAI api, and asking for it to find the peak balance and for the list of tra
nsactions (so that my app has a way to verify whether it got peak balance right.)

Feeding all of the markdown and reque
sting the api to send bank a list of all transactions isn't working. The model is 'lazy' and won't return all of the tra
nsactions, no matter my prompt (for reference this is a 20 page PDF with 200+ transactions).

So I am thinking that the 
next best way to do this would be with chunks. Docling offers hierarchy-aware chunking [0] which I think it's useful so 
as not to mess with transaction data. But then what should I, a noob, learn about to better proceed on building this app
 based on chunks?

## WAYS FORWARD?
(1) So how should I work with chunks? It seems that looping over chunks and sending 
them through the API and asking for transactions back to append to an array could do the job. But I've got two more thin
gs in mind.

(2) I've hard of chains (like in langchain) which could keep the context from the previous messages and it 
might also be easier to work with?

(3) I have noticed that openai works with a messages *array*. Perhaps that's what I 
should be interacting with via my API calls (to send a thread of messages) instead of doing what I proposed in (1)? Or p
erhaps what I'm describing here is exactly what chaining (2) does?


[0] https://ds4sd.github.io/docling/usage/#convert-
from-binary-pdf-streams at the bottom
```
---

     
 
all -  [ Open Canvas provides chatgpt canvas style ui to use claude and llama3, stores style rules and user i ](https://www.reddit.com/r/LocalLLaMA/comments/1h1a1b9/open_canvas_provides_chatgpt_canvas_style_ui_to/) , 2024-11-28-0914
```
https://preview.redd.it/xg5bqv9odh3e1.png?width=3328&format=png&auto=webp&s=77d6b1e1926a06340e8a21194c73e6f29ac48331

[h
ttps://github.com/langchain-ai/open-canvas](https://github.com/langchain-ai/open-canvas)  

```
---

     
 
all -  [ Tips for improving the processing time of Langgraph Agents ](https://www.reddit.com/r/LangChain/comments/1h18b0d/tips_for_improving_the_processing_time_of/) , 2024-11-28-0914
```
Hello!! I was tasked to improve the performance and speed of our multi agent llm using langgraph and langchain

Any tips
 on how to improve the processing time?
```
---

     
 
all -  [ Text summarization using LangChain's Map-Reduce method. ](https://www.reddit.com/r/LangChain/comments/1h177es/text_summarization_using_langchains_mapreduce/) , 2024-11-28-0914
```
Hello, 

I've been experimenting with LangChain's Map-Reduce approach to summarize texts of approximately 2000 words eac
h. I am satisfied with the results, but the summarization process takes around 15-20 mins. I was looking for any ideas o
r methods to try and reduce the execution time. I'm using ollama's llama3.1:8b model.

Thanks in advance!
```
---

     
 
all -  [ My business model for a small OSS. From OSS project to SaaS (funding)  ](https://www.reddit.com/r/SaaS/comments/1h14361/my_business_model_for_a_small_oss_from_oss/) , 2024-11-28-0914
```
This is a response/follow-up (??) to a great post done yesterday about [monetization of OSS  ](https://www.reddit.com/r/
SaaS/comments/1h0ha1s/i_am_making_700_monthly_with_my_opensource/)

Now i'm going describe how i'm scaling, and do full-
time work in my project, until it becomes a startup/B2B SaaS.

**Project:** [ExtractThinker](https://github.com/enoch371
2/ExtractThinker)

Its **Document Intelligence for LLMs**, or **Langchain for document intelligence**. So more of a nich
e use case, more oriented to extraction of data (No RAG). The project will be used as ***'proof-of-skill'*** for the res
t of the business, for a complex *agentic* B2B model to eventually be also a SaaS. 

**Question:** People are asking me 
'how do you scale this???'

Flow: [Image flow ](https://imgur.com/a/EYWGoP5)

**Github project:** Well presented with do
cumentation. As example driven as possible. 

**Medium:** Over 1.5k followers, contains articles that mention the projec
t or not (depending on the publisher). They attract clients and people interested in the problem solved. **This gives co
ntractor work that feeds the project with use cases.**

**Documentation:** Medium feeds the documentation, so i 'kill tw
o birds with one stone'**.** From diagrams to in detail explanation.

  
**Plan:** Go over 500+ stars and get 2 other to
p founders (2 tech guys and 1 non-tech sales, still missing), that will eventually use this to get funding, next year, v
ia incubator/accelerator or VC seed right away.

  
I hope this helps! A few 1/2 months back i thought this project woul
d not scale (personally), but doing something on top of this, **could definitely work** (Clients eventually put some sen
se into me). Im just a technical guy, sometimes is difficult to see a business model in something like this. 

  
Thank 
you for your time. 
```
---

     
 
all -  [ Langgraph, user_input node with File Upload ](https://www.reddit.com/r/LangChain/comments/1h13hd3/langgraph_user_input_node_with_file_upload/) , 2024-11-28-0914
```
Hello!

I am trying to figure out how to use Langgraph nodes when there is a non-textual input. I am guiding a user in u
ploading files. Let's say, I have the following structure:

`builder.add_node('ask_email', email_node)`  
`builder.add_n
ode('upload_file', upload_file_node)`

I have two questions:

1. How do I manage the file upload - the UI (openWebUI) ca
n show a drop-in component that will trigger external API and this API will respond 200 OK -> is the upload a tool call?
 
2. How do we pass the information about the upload through the state?

  
I'd appreciate a direction, just can't figur
e out how to go about it.
```
---

     
 
all -  [ KeyError: 'input' in create_retrieval_chain()? ](https://www.reddit.com/r/LangChain/comments/1h0ytlt/keyerror_input_in_create_retrieval_chain/) , 2024-11-28-0914
```
I new to generative ai and langchain, bellow i am sharing code and error. I am trying to create a small application. I a
m using python==3.10.0



***CODE:***

    prompt = ChatPromptTemplate([
        ('system', 'You are an expert generativ
e ai developer, answer question from given context {context}'),
        ('user', '{question}')
    ])

    document_chai
n=create_stuff_documents_chain(llm=llm,prompt=prompt1,output_parser=output_parser)
    document_chain
    

    retrieve
r=new_db.as_retriever()
    from langchain.chains import create_retrieval_chain
    retrieval_chain=create_retrieval_cha
in(retriever,combine_docs_chain=document_chain)
    

    ## Get the response form the LLM
    response=retrieval_chain.
invoke({'question':'tell me what is generative ai, and what are Examples of Generative AI tools?'})
    response['answer
']

  
*ERROR I AM GETTING:*

    ---------------------------------------------------------------------------
    KeyErr
or                                  Traceback (most recent call last)
    Cell In[60], line 2
          1 ## Get the res
ponse form the LLM
    ----> 2 response=retrieval_chain.invoke({'question':'tell me what is generative ai, and what are 
Examples of Generative AI tols?'})
          3 # response = retrieval_chain.invoke({'input': {'question': 'tell me what 
is generative AI, and what are examples of Generative AI tools?'}})
          4 response['answer']
    
    File u:\GENE
RATIVE_AI\venv\lib\site-packages\langchain_core\runnables\base.py:5354, in RunnableBindingBase.invoke(self, input, confi
g, **kwargs)
       5348 def invoke(
       5349     self,
       5350     input: Input,
       5351     config: Optiona
l[RunnableConfig] = None,
       5352     **kwargs: Optional[Any],
       5353 ) -> Output:
    -> 5354     return self.
bound.invoke(
       5355         input,
       5356         self._merge_configs(config),
       5357         **{**self.
kwargs, **kwargs},
       5358     )
    
    File u:\GENERATIVE_AI\venv\lib\site-packages\langchain_core\runnables\base
.py:3022, in RunnableSequence.invoke(self, input, config, **kwargs)
       3020 context.run(_set_config_context, config)

       3021 if i == 0:
    -> 3022     input = context.run(step.invoke, input, config, **kwargs)
       3023 else:
    
   3024     input = context.run(step.invoke, input, config)
    
    File u:\GENERATIVE_AI\venv\lib\site-packages\langch
ain_core\runnables\passthrough.py:494, in RunnableAssign.invoke(self, input, config, **kwargs)
        488 def invoke(
 
       489     self,
        490     input: dict[str, Any],
        491     config: Optional[RunnableConfig] = None,
   
     492     **kwargs: Any,
        493 ) -> dict[str, Any]:
    --> 494     return self._call_with_config(self._invoke,
 input, config, **kwargs)
    
    File u:\GENERATIVE_AI\venv\lib\site-packages\langchain_core\runnables\base.py:1927, i
n Runnable._call_with_config(self, func, input, config, run_type, serialized, **kwargs)
       1923     context = copy_c
ontext()
       1924     context.run(_set_config_context, child_config)
       1925     output = cast(
       1926      
   Output,
    -> 1927         context.run(
       1928             call_func_with_variable_args,  # type: ignore[arg-ty
pe]
       1929             func,  # type: ignore[arg-type]
    . . .
         66     ).assign(answer=combine_docs_chain
)
         67 ).with_config(run_name='retrieval_chain')
         69 return retrieval_chain
    
    KeyError: 'input'Out
put is truncated. View as a scrollable element or open in a text editor. Adjust cell output settings...



Thanks in adv
ance, I hope to hear from you soon.  

```
---

     
 
all -  [ Is there a way to chainge chains setup without changing codes in python ](https://www.reddit.com/r/LangChain/comments/1h0v562/is_there_a_way_to_chainge_chains_setup_without/) , 2024-11-28-0914
```
Hello group,
I am working on an interesting problem to setup chains by providing a yaml file as input ( it could be a di
ctionary,  a string or list of touple).

Ask:
Using lang chains to create a function which could be able to create serie
s and parallel chains as per our yaml without changing the python code for each case scenario.

Already done: i am able 
to write a function which will create chains for each attribute individually. 

The issue: i am facing challenge in comb
ining these chains. The depth and length could be changed using the yaml file.

The code should be able to set up chains
 (series or parallel as per the yaml) without making any changes to it the python code.

Idea: i am not 100 percent sure
 but it will involve recursion 
```
---

     
 
all -  [ Prompt engineering for LLM applications ? ](https://www.reddit.com/r/LangChain/comments/1h0taz4/prompt_engineering_for_llm_applications/) , 2024-11-28-0914
```
how does prompt engineering help develop better LLM powered apps like I understand that if you are able to prompt the mo
del a certain you will get a better response but the avg user is not going to be aware of those techniques and in which 
is prompt engineering just for the more advanced user and not like an aid towards better LLM development?
```
---

     
 
all -  [ Optimize your LangChain program with Cognify! ](https://www.reddit.com/r/LangChain/comments/1h0jjbh/optimize_your_langchain_program_with_cognify/) , 2024-11-28-0914
```
Hi everyone! I'm Reyna, a PhD student working on systems for machine learning.

I want to share an exciting open-source 
project my team has built: [Cognify](https://github.com/GenseeAI/cognify). Cognify is a multi-faceted optimization tool 
that automatically enhances generation quality and reduces execution costs for generative AI workflows written in LangCh
ain, DSPy, and Python. Cognify helps you evaluate and refine your workflows at any stage of development. Use it to test 
and enhance workflows you’ve finished building or to analyze your current workflow’s potential.

Key highlights:

* Work
flow generation quality improvement by up to 48%
* Workflow execution cost reduction by up to 9x
* Multiple optimized wo
rkflow versions with quality-cost combinations for you to choose
* Automatic model selection, prompt enhancing, and work
flow structure optimization

Get Cognify at [https://github.com/GenseeAI/cognify](https://github.com/GenseeAI/cognify) a
nd read more at https://mlsys.wuklab.io/posts/cognify/. Would love to hear your feedback and get your contributions!
```
---

     
 
all -  [ RAG - how to ensure a date fields in metadata is used to get latest data? ](https://www.reddit.com/r/LangChain/comments/1h0ih0x/rag_how_to_ensure_a_date_fields_in_metadata_is/) , 2024-11-28-0914
```
I've created a RAG app that aims to be a personal assistant for everything related to my kids' school. I get a ton of em
ails from school with updates, notices, invites, and a lot more. Some info is recurring, such as the weekly wraps that e
xplain what was taught during that week; some of it is a one-off like an invite to an event.

Ultimately, I plan to have
 this either connected to Whatsapp or actually creating reminders/calendar invites for me, but for now, I'm validating i
ts results. But I've hit a wall when it comes to the freshness of data.

**Question**

When building this RAG app, I wou
ld like it to be mindful of dates as it retrieves relevant docs. For example, I get a Weekly Wrap email every week, on F
ridays. Besides wanting the retriever to find the right context (i.e. weekly wrap emails), I would also like for it to s
ort by date and focus on the latest one. What's the best way to achieve this?

**Further Context**

Here is what the app
 does:

* bulk-reads all past emails using the Gmail API, and keeps the date, sender, subject, body and attachments
* pr
ocesses each email to properly convert the body and relevant attachments to text (converts PDFs, DOCXs, and html body in
to text)
* stores the documents in MongoDB (using `MongoDBStore` from `langchain_community.storage)` , using a Document 
format (the entire body + attachment text under `page_content`, and everything else in `metadata`
* stores a summary of 
each document, also in MongoDB, in order to use Multi-Representation indexing
* maps IDs across both stores

I'm using G
PT-4o as the LLM behind the scenes.

I then build a retriever and a chain like this, and invoke the query. Since the res
ponse doesn't take the dates into account, I don't get the latest info properly...

    mongo_conn_str = 'mongodb://loca
lhost:27017/'
    mongodb_client = MongoClient(
        mongo_conn_str,
        uuidRepresentation='standard'
    )
    

    database = mongodb_client['parent-assistant']
    summary_collection = database['summaries']
    
    docs_store = 
MongoDBStore(
        mongo_conn_str,
        db_name='parent-assistant',
        collection_name='emails'
    )
    emb
eddings = OpenAIEmbeddings()
    
    summary_vector_store = Chroma(
        collection_name='summaries',
        embedd
ing_function=OpenAIEmbeddings()
    )
    
    summaries = list(summary_collection.find())
    
    summary_docs = [
   
     Document(
            page_content=s['summary'],
            metadata={'_id': s['_id']}
        )
        for i, s 
in enumerate(summaries)
    ]
    
    retriever = MultiVectorRetriever(
        docstore=docs_store,
        vectorstor
e=summary_vector_store,
        id_key='_id',
        search_kwargs={'k': 1}
    )
    retriever.vectorstore.add_documen
ts(summary_docs)
    
    template = '''Answer the following question based on this context:
    
    {context}
    
   
 Question: {question}
    '''
    
    llm = ChatOpenAI(model='gpt-4o', temperature=0.1)
    
    def format_docs(docs):

        return '\n\n'.join(doc.page_content for doc in docs)
    
    rag_chain = (
        {'context': retriever | for
mat_docs, 'question': RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )
    
    r
ag_chain.invoke('What did John Doe learn last week?')
```
---

     
 
all -  [ Junior Engineer here. Looking forwared to getting my Resume review / roasted.  ](https://www.reddit.com/r/developersIndia/comments/1h0hs5x/junior_engineer_here_looking_forwared_to_getting/) , 2024-11-28-0914
```
I am working full time for close to an year and I love working with cloud/ devops  but somware i love writing backend co
de. I am looking forwated to getting my resume  reviewed or roasted.  It is 2 pages but would it be better if i make it 
1 ? also I feel like im not good enogh at writing project or experience descriptions. The resume is mostly centerd aroun
d Software Dev type roles but apart from this i work as Technical Content Writer in some companies part time and been ju
dge to few hackathons.  should i put that here ?   
please suggest me to improve, Thank you   


https://preview.redd.it
/lkfy00999a3e1.png?width=2204&format=png&auto=webp&s=a2f654e7af7a466458fe45c157f06d992d8a9476


```
---

     
 
all -  [ Is it possible to add a tool call response to the state  ](https://www.reddit.com/r/LangGraph/comments/1h0gcxb/is_it_possible_to_add_a_tool_call_response_to_the/) , 2024-11-28-0914
```
    from
     datetime 
    import
     datetime
    from
     typing 
    import
     Literal
    
    from
     langch
ain_core.language_models.chat_models 
    import
     BaseChatModel
    from
     langchain_core.messages 
    import
  
   AIMessage, SystemMessage
    from
     langchain_core.runnables 
    import
     (
        RunnableConfig,
        Ru
nnableLambda,
        RunnableSerializable,
    )
    from
     langgraph.checkpoint.memory 
    import
     MemorySaver

    from
     langgraph.graph 
    import
     END, MessagesState, StateGraph
    from
     langgraph.managed 
    impo
rt
     IsLastStep
    from
     langgraph.prebuilt 
    import
     ToolNode
    
    from
     agents.llama_guard 
   
 import
     LlamaGuard, LlamaGuardOutput, SafetyAssessment
    from
     agents.tools.user_data_validator 
    import
 
    (
        user_data_parser_instructions,
        user_data_validator_tool,
    )
    from
     core 
    import
    
 get_model, settings
    
    
    class AgentState(MessagesState, 
    total
    =False):
        
    '''`total=False`
 is PEP589 specs.
    
        documentation: https://typing.readthedocs.io/en/latest/spec/typeddict.html#totality
     
   '''
    
        safety: LlamaGuardOutput
        is_last_step: IsLastStep
        is_data_collection_complete: bool

    
    
    tools = [user_data_validator_tool]
    
    
    current_date = datetime.now().strftime('%B %d, %Y')
    i
nstructions = f'''
        You are a professional onboarding assistant collecting user information.
        Today's date
 is {current_date}.
     
        Collect the following information:
        {user_data_parser_instructions}
     
     
   Guidelines:
        1. Collect one field at a time in order: name, occupation, location
        2. Format the respons
e according to the specified schema
        3. Ensure the data from user is proper before calling the validator
        
4. Use the {user_data_validator_tool.name} tool to validate the JSON data
        5. Keep collecting information until a
ll fields have valid values
     
        Remember: Always pass complete JSON with all fields, using null for pending in
formation
     
        Current field to collect: {{current_field}}
        '''
    
    
    def wrap_model(
    model

    : BaseChatModel) -> RunnableSerializable[AgentState, AIMessage]:
        
    model
     = 
    model
    .bind_tool
s(tools)
        preprocessor = RunnableLambda(
            lambda 
    state
    : [SystemMessage(
    content
    =ins
tructions)] + 
    state
    ['messages'],
            
    name
    ='StateModifier',
        )
        
    return
   
  preprocessor | 
    model
    
    
    def format_safety_message(
    safety
    : LlamaGuardOutput) -> AIMessage:
  
      content = f'This conversation was flagged for unsafe content: {', '.join(
    safety
    .unsafe_categories)}'
   
     
    return
     AIMessage(
    content
    =content)
    
    
    async def acall_model(
    state
    : AgentSta
te, 
    config
    : RunnableConfig) -> AgentState:
        m = get_model(
    config
    ['configurable'].get('model',
 settings.DEFAULT_MODEL))
        model_runnable = wrap_model(m)
        response = 
    await
     model_runnable.ainvo
ke(
    state
    , 
    config
    )
    
        
    # Run llama guard check here to avoid returning the message if i
t's unsafe
        llama_guard = LlamaGuard()
        safety_output = 
    await
     llama_guard.ainvoke('Agent', 
    
state
    ['messages'] + [response])
        
    if
     safety_output.safety_assessment == SafetyAssessment.UNSAFE:
  
          
    return
     {
                'messages': [format_safety_message(safety_output)],
                'safety
': safety_output,
            }
    
        
    if
     
    state
    ['is_last_step'] and response.tool_calls:
     
       
    return
     {
                'messages': [
                    AIMessage(
                        
    id
 
   =response.id,
                        
    content
    ='Sorry, need more steps to process this request.',
          
          )
                ]
            }
    
        
    # We return a list, because this will get added to the exi
sting list
        
    return
     {'messages': [response]}
    
    
    async def llama_guard_input(
    state
    : 
AgentState, 
    config
    : RunnableConfig) -> AgentState:
        llama_guard = LlamaGuard()
        safety_output = 

    await
     llama_guard.ainvoke('User', 
    state
    ['messages'])
        
    return
     {'safety': safety_outp
ut}
    
    
    async def block_unsafe_content(
    state
    : AgentState, 
    config
    : RunnableConfig) -> Agent
State:
        safety: LlamaGuardOutput = 
    state
    ['safety']
        
    return
     {'messages': [format_safety
_message(safety)]}
    
    
    # Define the graph
    agent = StateGraph(AgentState)
    agent.add_node('model', acall
_model)
    agent.add_node('tools', ToolNode(tools))
    agent.add_node('guard_input', llama_guard_input)
    agent.add_
node('block_unsafe_content', block_unsafe_content)
    agent.set_entry_point('guard_input')
    
    
    # Check for un
safe input and block further processing if found
    def check_safety(
    state
    : AgentState) -> Literal['unsafe', 
'safe']:
        safety: LlamaGuardOutput = 
    state
    ['safety']
        
    match
     safety.safety_assessment:

            
    case
     SafetyAssessment.UNSAFE:
                
    return
     'unsafe'
            
    case
    
 _:
                
    return
     'safe'
    
    
    agent.add_conditional_edges(
        'guard_input', check_safe
ty, {'unsafe': 'block_unsafe_content', 'safe': 'model'}
    )
    
    # Always END after blocking unsafe content
    ag
ent.add_edge('block_unsafe_content', END)
    
    # Always run 'model' after 'tools'
    agent.add_edge('tools', 'model
')
    
    
    # After 'model', if there are tool calls, run 'tools'. Otherwise END.
    def pending_tool_calls(
    s
tate
    : AgentState) -> Literal['tools', 'done']:
        last_message = 
    state
    ['messages'][-1]
        
    
if
     not isinstance(last_message, AIMessage):
            
    raise
     TypeError(f'Expected AIMessage, got {type(l
ast_message)}')
        
    if
     last_message.tool_calls:
            
    return
     'tools'
        
    return
 
    'done'
    
    
    agent.add_conditional_edges(
        'model', pending_tool_calls, {'tools': 'tools', 'done': EN
D}
    )
    
    onboarding_assistant = agent.compile(
    checkpointer
    =MemorySaver())
    
    
    
```
---

     
 
all -  [ Seeking Advice on Parsing and Cleaning Legacy Documents ](https://www.reddit.com/r/LangChain/comments/1h0esud/seeking_advice_on_parsing_and_cleaning_legacy/) , 2024-11-28-0914
```
Hey everyone

At work, I've been tasked with handling a collection of guides, documents, and tutorials spanning the past
 20 years. Many of these are in pretty bad shape. While most of the files are in .pdf format, I also come across .pptx f
iles. The most frustrating part is that these documents often contain numerous industry-specific abbreviations, tables, 
and screenshots taken from other software GUI's.

For now, I’m parsing these documents as they are and feeding them into
 an LLM after performing semantic similarity searches. However, when I review the retrieved content, I often find a lot 
of nonsensical chunks. I suspect this is due to the “garbage in, garbage out.”

Today, I was considering using multimoda
l LLMs to parse these PDF screenshots and extract the content more accurately, potentially leveraging an advanced model 
like 4o (or similar).

Do you think this is a good approach? Are there better ways to handle this? I’d appreciate hearin
g about your experiences or recommendations!

Thanks in advance!
```
---

     
 
all -  [ Has anyone used Milvus or Qdrant in cloud? Whats been your experience? ](https://www.reddit.com/r/LangChain/comments/1h0cxtk/has_anyone_used_milvus_or_qdrant_in_cloud_whats/) , 2024-11-28-0914
```
I am planning to build something in prod, any feedback would be great. thanks
```
---

     
 
all -  [ Observability Tools AWS ](https://www.reddit.com/r/LangChain/comments/1h0bjl3/observability_tools_aws/) , 2024-11-28-0914
```
What observability tools are you using right now ? 

I am using aws stack with bedrock and amazon knowledge base and I a
m trying to find a good observability tools like langsmith,  but in AWS environment.  
```
---

     
 
all -  [ Suggestions to host a huggingface model on VLLM + triton server ](https://www.reddit.com/r/LangChain/comments/1h0bgsl/suggestions_to_host_a_huggingface_model_on_vllm/) , 2024-11-28-0914
```
I'm trying to host Qwen 2.5 model on vLLM and triton server. Can anyone suggest me best resource that can help to do it 
correctly. I'm new to this. Any suggestions are also welcome. 

thanks in advance!
```
---

     
 
all -  [ Writer helper tool I've started working on - worth making into a thing or pretty useless? ](https://www.reddit.com/r/LangChain/comments/1h0b10x/writer_helper_tool_ive_started_working_on_worth/) , 2024-11-28-0914
```
https://reddit.com/link/1h0b10x/video/pxvzc467s83e1/player


```
---

     
 
all -  [ Calling Scrapy multiple times (getting ReactorNotRestartable ) ](https://www.reddit.com/r/scrapy/comments/1h0avo7/calling_scrapy_multiple_times_getting/) , 2024-11-28-0914
```
Hi,I know, many already asked and you provided some workarounds, but my problem remained unresolved.  
  
Here are the d
etails:  
Flow/Use Case: I am building a bot. The user can ask the bot to crawl a web page and ask questions about it. T
his process can happen every now and then, I don't know what are the web pages in advance and it all happens while the b
ot app is running,  
time  
Problem: After one successful run, I am getting the famous: twisted.internet.error.ReactorNo
tRestartable error message.I tried running Scrapy in a different process, however, since the data is very big, I need to
 create a shared memory to transfer. This is still problematic because:  
1. Opening a process takes time  
2. I do not 
know the memory size in advance, and I create a certain dictionary with some metadata. so passing the memory like this i
s complex (actually, I haven't manage to make it work yet)  
  
Do you have another solution? or an example of passing t
he massive amount of data between the processes?   
  
Here is a code snippet:  
(I call web\_crawler from another class
, every time with a different requested web address):

    import scrapy
    from scrapy.crawler import CrawlerProcess
 
   from urllib.parse import urlparse
    from llama_index.readers.web import SimpleWebPageReader  # Updated import
    #
from langchain_community.document_loaders import BSHTMLLoader
    from bs4 import BeautifulSoup  # For parsing HTML cont
ent into plain text
    
    g_start_url = ''
    g_url_data = []
    g_with_sub_links = False
    g_max_pages = 1500
  
  g_process = None
    
    
    class ExtractUrls(scrapy.Spider): 
        
        name = 'extract'
    
        # req
uest function 
        def start_requests(self):
            global g_start_url
    
            urls = [ g_start_url, ]
 
            self.allowed_domain = urlparse(urls[0]).netloc #recieve only one atm
                    
            for 
url in urls: 
                yield scrapy.Request(url = url, callback = self.parse) 
    
        # Parse function 
   
     def parse(self, response): 
            global g_with_sub_links
            global g_max_pages
            global g
_url_data
            # Get anchor tags 
            links = response.css('a::attr(href)').extract()  
            
    
        for idx, link in enumerate(links):
                if len(g_url_data) > g_max_pages:
                    print('
Genie web crawler: Max pages reached')
                    break
                full_link = response.urljoin(link)
    
            if not urlparse(full_link).netloc == self.allowed_domain:
                    continue
                if id
x == 0:
                    article_content = response.body.decode('utf-8')
                    soup = BeautifulSoup(art
icle_content, 'html.parser')
                    data = {}
                    data['title'] = response.css('title::text
').extract_first()
                    data['page'] = link
                    data['domain'] = urlparse(full_link).netl
oc
                    data['full_url'] = full_link
                    data['text'] = soup.get_text(separator='\n').str
ip() # Get plain text from HTML
                    g_url_data.append(data)
                    continue
               
 if g_with_sub_links == True:
                    yield scrapy.Request(url = full_link, callback = self.parse)
        

    # Run spider and retrieve URLs
    def run_spider():
        global g_process
        # Schedule the spider for craw
ling
        g_process.crawl(ExtractUrls)
        g_process.start()  # Blocks here until the crawl is finished
        g
_process.stop()
    
    
    def web_crawler(start_url, with_sub_links=False, max_pages=1500):
        '''Web page text
 reader.
            This function gets a url and returns an array of the the wed page information and text, without the
 html tags.
    
        Args:
            start_url (str): The URL page to retrive the information.
            with_su
b_links (bool): Default is False. If set to true- the crawler will downlowd all links in the web page recursively. 
    
        max_pages (int): Default is 1500. If  with_sub_links is set to True, recursive download may continue forever... 
this limits the number of pages to download
    
        Returns:
            all url data, which is a list of dictionar
y: 'title, page, domain, full_url, text.
        '''
        global g_start_url
        global g_with_sub_links
        
global g_max_pages
        global g_url_data
        global g_process
    
        g_start_url=start_url
        g_max_p
ages = max_pages
        g_with_sub_links = with_sub_links
        g_url_data.clear
        g_process = CrawlerProcess(s
ettings={
            'FEEDS': {'articles.json': {'format': 'json'}},
        })
        run_spider()
        return g_u
rl_data
        
        
    

  

```
---

     
 
all -  [ Langchain react agent tool streaming ](https://www.reddit.com/r/LangChain/comments/1h09zge/langchain_react_agent_tool_streaming/) , 2024-11-28-0914
```
I am using LangChain native react\_agent implementation and I have a tool `ask_question` and sometime agent is calling t
hat tool depending upon the context. So I want to stream the input of the `ask_qesution` to user. What is the best way t
o do it? In LangChain, streaming response works only for the final answer not for the tool\_input so far.
```
---

     
 
all -  [ [For Hire] Programmer/Web Developer/IT Consultant (Python, PHP, AI, etc.) ](https://www.reddit.com/r/forhire/comments/1h06zwo/for_hire_programmerweb_developerit_consultant/) , 2024-11-28-0914
```
To get in contact, please message me, I don't use the chat thing and might miss you or reply very late. Then we can swit
ch to email/discord/telegram or whatever else. Apologies for starting with this, but many missed it when it was lower.


I'm a programmer/web developer with 15 years of professional experience. I am available for all sorts of programming and
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

Rate is $60/h.

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

     
 
all -  [ Building an Application Stack from Scratch with AI (agents) - Seeking Advice, Frameworks, Resources, ](https://www.reddit.com/r/softwarearchitecture/comments/1h036ko/building_an_application_stack_from_scratch_with/) , 2024-11-28-0914
```
Hi,

I’m planning to build an application for a personal use case, and also as a way to practice and experiment with AI 
integration. I’d like to start small but design it in a way that allows for future extension and experimentation.

**Her
e’s the tech stack I have in mind:**

* **Frontend:** Angular
* **Backend:** Quarkus or Spring Boot (I want to experimen
t with GraalVM and native compilation, plus I saw GraalVM is polyglot).
* **AI Integration:** LightLLM Proxy (although I
’m not sure if this is the best approach for integrating AI into an app. Should I consider something like LangChain or L
angraph here? Or is LangChain better suited for backend tasks?)
* **Database:** PostgreSQL
* **Containerization:** Docke
r
* **OS Integration (Windows 10):** I want to experiment with AutoHotkey scripts that can run anywhere in Windows. Thes
e scripts would send identifiers to the backend, which would match them with stored full prompts. The prompts would then
 be sent to an LLM, and after processing, the results would be saved in the database—making them available in the fronte
nd.

**My Experience with LLMs So Far**

Up until now, I’ve used AI primarily to modify existing human-written applicati
ons or to solve smaller, specific problems. I’ve used tools like ChatGPT and Claude Sonnet (API). However, I’ve noticed 
that when I don’t repeatedly provide the project context/rules again, the consistency and quality of AI-generated answer
s tend to drift.

Since I’m now trying to build an entire application stack from scratch with AI’s help, I’m concerned a
bout maintaining answer quality over multiple prompts and ensuring that the architecture and code quality don’t suffer a
s a result.

**What I’m Looking For**

I want to set up a strong architectural foundation for my project. Ideally, a wel
l-calibrated AI agent framework could help me:

* Design **diagrams, high-level architecture**, and **API structures**.

* Generate clear **documentation** to make it easier for AI to understand the codebase in the future, reducing errors.
*
 Maintain **consistency** and **quality** throughout the development process.

If this foundational work is done well, I
 believe it will make iterative development with AI smoother.

**My Questions**

1. **AI Agent Frameworks:** What are th
e best AI agent frameworks for designing and developing applications from scratch? I’m looking for tools that can guide 
the process—not just code generation, but also architecture design, documentation, etc.
2. **Best Practices for AI-Frien
dly Applications:** Are there any established best practices or “rules” to follow when designing applications to make th
em easier for AI to work with? For example:
   * Keeping nesting and complexity low.
   * Using clear and descriptive me
thod names.
   * Structuring the application with modularity in mind (e.g., dependency injection).
   * Generating docum
entation tailored to help LLMs understand the codebase.
3. **Templates and Prompt Chains:** Are there any pre-designed t
emplates, prompt chains, or software architecture guides for this purpose? If so, where can I find them?
4. **Advanced T
utorials:** Any recommendations for tutorials or videos that go beyond the basics? I’m especially interested in examples
 where someone builds a complex, skillful application using AI tools—something practical and advanced, not just simple t
oy projects.
5. **Gemini’s Context Window:** I’ve heard Gemini has a very high context window. Could this be relevant he
re, and if so, how?
6. **Communities and Resources:** If you know of good resources, Discord communities, subreddits, or
 YouTube channels that dive deep into this topic, please share! I’d love to connect and learn from others who’ve done th
is kind of thing.

Thanks in advance for your help! 😊
```
---

     
 
all -  [  Building an Application Stack from Scratch with AI (agents) - Seeking Advice, Frameworks, Resources ](https://www.reddit.com/r/LangChain/comments/1h032wj/building_an_application_stack_from_scratch_with/) , 2024-11-28-0914
```
Hi,

I’m planning to build an application for a personal use case, and also as a way to practice and experiment with AI 
integration. I’d like to start small but design it in a way that allows for future extension and experimentation.

 **He
re’s the tech stack I have in mind:**

* **Frontend:** Angular
* **Backend:** Quarkus or Spring Boot (I want to experime
nt with GraalVM and native compilation, plus I saw GraalVM is polyglot).
* **AI Integration:** LightLLM Proxy (although 
I’m not sure if this is the best approach for integrating AI into an app. Should I consider something like LangChain or 
Langraph here? Or is LangChain better suited for backend tasks?)
* **Database:** PostgreSQL
* **Containerization:** Dock
er
* **OS Integration (Windows 10):** I want to experiment with AutoHotkey scripts that can run anywhere in Windows. The
se scripts would send identifiers to the backend, which would match them with stored full prompts. The prompts would the
n be sent to an LLM, and after processing, the results would be saved in the database—making them available in the front
end.



**My Experience with LLMs So Far**

Up until now, I’ve used AI primarily to modify existing human-written applic
ations or to solve smaller, specific problems. I’ve used tools like ChatGPT and Claude Sonnet (API). However, I’ve notic
ed that when I don’t repeatedly provide the project context/rules again, the consistency and quality of AI-generated ans
wers tend to drift.

Since I’m now trying to build an entire application stack from scratch with AI’s help, I’m concerne
d about maintaining answer quality over multiple prompts and ensuring that the architecture and code quality don’t suffe
r as a result.



**What I’m Looking For**

I want to set up a strong architectural foundation for my project. Ideally, 
a well-calibrated AI agent framework could help me:

* Design **diagrams, high-level architecture**, and **API structure
s**.
* Generate clear **documentation** to make it easier for AI to understand the codebase in the future, reducing erro
rs.
* Maintain **consistency** and **quality** throughout the development process.

If this foundational work is done we
ll, I believe it will make iterative development with AI smoother.



**My Questions**

1. **AI Agent Frameworks:** What
 are the best AI agent frameworks for designing and developing applications from scratch? I’m looking for tools that can
 guide the process—not just code generation, but also architecture design, documentation, etc.
2. **Best Practices for A
I-Friendly Applications:** Are there any established best practices or “rules” to follow when designing applications to 
make them easier for AI to work with? For example:
   * Keeping nesting and complexity low.
   * Using clear and descrip
tive method names.
   * Structuring the application with modularity in mind (e.g., dependency injection).
   * Generatin
g documentation tailored to help LLMs understand the codebase.
3. **Templates and Prompt Chains:** Are there any pre-des
igned templates, prompt chains, or software architecture guides for this purpose? If so, where can I find them?
4. **Adv
anced Tutorials:** Any recommendations for tutorials or videos that go beyond the basics? I’m especially interested in e
xamples where someone builds a complex, skillful application using AI tools—something practical and advanced, not just s
imple toy projects.
5. **Gemini’s Context Window:** I’ve heard Gemini has a very high context window. Could this be rele
vant here, and if so, how?
6. **Communities and Resources:** If you know of good resources, Discord communities, subredd
its, or YouTube channels that dive deep into this topic, please share! I’d love to connect and learn from others who’ve 
done this kind of thing.



Thanks in advance for your help! 😊
```
---

     
 
all -  [ Advice on Fine-Tuning an LLM for Scored Interpretation Feedback ](https://www.reddit.com/r/LangChain/comments/1gzy5vh/advice_on_finetuning_an_llm_for_scored/) , 2024-11-28-0914
```

Hi everyone,

A little new to all this...I'm working on fine-tuning an LLM to evaluate user-provided interpretations of
 a scan and provide an accuracy score. Here's the setup for my fine-tuning dataset:

A model answer

A mark scheme

Samp
le learner interpretations

Scores assigned to those learner interpretations


My goal is to create a model that takes a
 user's interpretation of a scan as input and returns an accuracy score based on the fine-tuned data.

What would be the
 best way to structure and use this dataset to achieve reliable scoring? Any tips on preprocessing, model architecture, 
or training strategies would be greatly appreciated.

Thanks in advance for your help!


```
---

     
 
all -  [ Complex Chain Prompting  ](https://www.reddit.com/r/LangChain/comments/1gzt3bk/complex_chain_prompting/) , 2024-11-28-0914
```
I have a complex flow for writing articles, including generating article flow/structure + outlines based on sources, the
n creating sub-outlines, generating section by section while maintaining the flow and structure. then translating it etc
. 

What would be a good Framework, or platform, as well as strategies to create a Co-pilot that involves a predefined w
orkflow as well as human input at every step.
```
---

     
 
all -  [ VectorStore query returns a generic response, as if my information isn't used, is this query correct ](https://www.reddit.com/r/LangChain/comments/1gzq5ko/vectorstore_query_returns_a_generic_response_as/) , 2024-11-28-0914
```
I'm using LangChain JS, with the following query to get the data from my vectorstore, am I missing something? Because th
e data returned is generic, like I would ask it to ChatGPT, without it knowing about my data.

        const pinecone = 
new Pinecone();
        const pineconeIndex = pinecone.Index(process.env.PINECONE_INDEX!);
    
        const vectorStor
e = await PineconeStore.fromExistingIndex(
          new OpenAIEmbeddings(),
          { pineconeIndex },
        );
   
 
        const vectorStoreRetriever = vectorStore.asRetriever();
    
        // Initialize OpenAI Chat model
        c
onst model = new ChatOpenAI({
          openAIApiKey: process.env.OPENAI_API_KEY, // Your OpenAI API key
          model
: 'gpt-4o-mini',
          temperature: 0,
        });
    
        const SYSTEM_TEMPLATE = `Use the following pieces of
 context to answer the question at the end.
        If you don't know the answer, just say that you don't know, don't tr
y to make up an answer.
        ----------------
        {context}`;
    
        const prompt = ChatPromptTemplate.from
Messages([
          ['system', SYSTEM_TEMPLATE],
          ['human', '{question}'],
        ]);
    
        const chai
n = RunnableSequence.from([
          {
            context: vectorStoreRetriever.pipe(formatDocumentsAsString),
       
     question: new RunnablePassthrough(),
          },
          prompt,
          model,
          new StringOutputPars
er(),
        ]);
    
        const answer = await chain.invoke(
          'Tell me a bit about the data you have store
d in your vectors',
        );
```
---

     
 
all -  [ Overcoming output token limit with agent generating structured output ](https://www.reddit.com/r/LangGraph/comments/1gzpz2n/overcoming_output_token_limit_with_agent/) , 2024-11-28-0914
```
Hi there,

I've built an agent based on Option 1 described here https://langchain-ai.github.io/langgraph/how-tos/react-a
gent-structured-output/#option-1-bind-output-as-tool


The output is a nested Pydantic model, LLM is Azure gpt4o

```
cl
ass NestedStructure:
	<some fields>

class FinalOutput(BaseModel):
	some_field: str
	some_other_field: list[NestedStruct
ure]
```

Apart from structured output, it's using one tool only - one providing chunks from searched documents.

And it
 works as I'd expect, except for the case where the task becomes particularly complicated and list is growing significan
tly. As a result, I am hitting 4096 output token limit, structured output is not genrated correctly: Json validation fai
ls due to  unmatched string on output that was finished prematurely.

I removed some fields from the NestedStructure, bu
t it didn't help much. 

Is there something else I could try? Some 'partial' approach? Could I somehow break the output 
generation?

The problem that I've been trying to solve before is that the agent's response was not complete - some rele
vant info from search tool would not be included in the response. Some fields need to be filled with original info so I'
m more on 'provide detailed answer' rather than 'provide brief sumary' side of life.
```
---

     
 
all -  [ Langchain & Langgraph's documentation is so messed up, even ClosedAI couldn't create an error-free a ](https://www.reddit.com/r/Langchaindev/comments/1gzlxy8/langchain_langgraphs_documentation_is_so_messed/) , 2024-11-28-0914
```
Dear Langchain/Langgraph Team, 

Please update the documentation and kindly add more examples with other LLMs as well. I
t seems you're only dedicated to ClosedAI.

This is what I had asked ClosedAI: create a single node SQL Agent using Olla
ma that gets some input from a vector store along with user's input question.
```
---

     
 
all -  [ Claude/Langchain starter tutorial  ](https://www.reddit.com/r/AI_Agents/comments/1gzl1zo/claudelangchain_starter_tutorial/) , 2024-11-28-0914
```
Can anyone provide me with AI Agent building tutorial as a starter guide, cant find a good resource anywhere
```
---

     
 
all -  [ Need help providing more information to LLM regarding prompts ](https://www.reddit.com/r/LangChain/comments/1gzj92z/need_help_providing_more_information_to_llm/) , 2024-11-28-0914
```
So I’m working on this Text to SQL use case, and one thing I’m struggling with is making LLM understand what the prompts
 mean. For example, if I ask for top performing teams in 2024, the LLM does not have an idea what top performing teams m
ean. I’m exploring ways to get this through to the model in the most effective way. Mind you that I am working with tabl
es with large number of columns and passing everything in the prompt is not an option. I am open to any suggestions, may
be something like Human In Loop?
My entire app is created using lang graph with multiple agent interactions. 
```
---

     
 
all -  [ LlamaParse vs Docling for extracting information from bank account statements (PDF)? ](https://www.reddit.com/r/LangChain/comments/1gzdnev/llamaparse_vs_docling_for_extracting_information/) , 2024-11-28-0914
```
I've recently learned about IBM Docling (https://research.ibm.com/blog/docling-generative-AI) which works super well. Ho
wever I wonder how it compares to LlamaParse and what some of the differences are.

How could I go about benchmarking it
?
```
---

     
 
all -  [ Are there any free versions of LangChain or any similar thing? ](https://www.reddit.com/r/developer/comments/1gzcih2/are_there_any_free_versions_of_langchain_or_any/) , 2024-11-28-0914
```
I want to learn creating AI apps, are there any free models?
```
---

     
 
all -  [ Curious Question on the state of model Knowledge and State of LLMs.  ](https://www.reddit.com/r/ChatGPTCoding/comments/1gzav0j/curious_question_on_the_state_of_model_knowledge/) , 2024-11-28-0914
```
So hear me out completely, I use Ai tools and LLMs of choice for development. But, recently I have been stuck into a pro
blem where if I want to incorporate multiple cutting edge technologies into my product the LLM model almost craps out al
l the time, this is because of the knowledge base of LLM is not up to date with the rate at which tech is growing. 

For
 example: I want to incorporate Llamaindex, Langchain, Some vector DB, Scrapy, Playwright etc into my algorithm and top 
it with an agent orchestration system like Autogen or CrewAi. 90% of the time I have to read the documentations of all o
f these technologies because they are developing at rapid scale and implement them in my platform. If I am reading it an
d figuring it out myself whats the use of an LLM to code? Even for troubleshooting its hard because sometimes the featur
e is depreciated like using an outdated version of OpenAi API key docs and even with 'Web' functionality of LLM its kind
a useless because it just doesnt search the things which needs to be searched. 

Current solutions are available in the 
forms of Algolia which is powering the search component of [https://docs.llamaindex.ai/en/stable/](https://docs.llamaind
ex.ai/en/stable/) so the need is there. Where it fails is direct connections with the LLM of the user choice. If I ask a
 question to build me a RAG pipeline based on llamaindex and use the latest docs of Milvus as a vectorDB, I want it done
 not a link to the article on how to build it. Also 

So I went out to solve my own problem and deciding to make it open
source as I build in public. 

Idea for Devdocs: The developer will have an option to connect their gitbooks(for example
) with Devdocs and make the data available for anyone to source into their LLM. This will generate an API or some connec
tor which the user will be able to just connect to their choice of chatbot like AnythingLLM or OpenWebUI. 

The user lik
e us will just go to the docs.llamaindex and click a button to copy the API key of the vector storage(have to figure out
 which one) and paste it inside their chatbot. Then they can also take the docs key from OpenAi and paste it in giving t
hem the most latest iteration on how to use openai and its multiple features. The user can do the same for Autogen, crew
ai etc and have up to date data for their LLM to query. 

The result is that after this platform, the LLMs will have rob
ust and error free information to build softwares. Next gen of LLMs can actually learn from this data and maybe we can f
inally have an LLM learn Langchain and give us proper outputs. 

I think this is going to be huge in the community of so
ftware development. Spend less time reading and more time doing and the stigma that LLM produces shit code will be mitig
ated. 

What are your thoughts, clearly I should not be the only one having this problem. Let me know if I am thinking i
n the right direction or someone has already solved this problem. 
```
---

     
 
all -  [ Chucking strategy for legal docs ](https://www.reddit.com/r/LangChain/comments/1gza6z5/chucking_strategy_for_legal_docs/) , 2024-11-28-0914
```
For those working on legal or insurance document where there are pages of conditions, what is your chunking strategy?

I
 am using docling for parsing files and semantic double merging chunking. Not satisfied with results.
```
---

     
 
all -  [ Starting point to building a GMail supervised email responder? Validate my stack ](https://www.reddit.com/r/OpenAI/comments/1gz9q81/starting_point_to_building_a_gmail_supervised/) , 2024-11-28-0914
```
I am aiming to build a workflow that connects to my Gmail Inbox, looks at unread messages, classifies them into certain 
buckets, and for some buckets creates a personalized and templated response that it puts into the draft folder.

I know 
this is nothing super creative or unseen that I am referencing here and yet I could not find too much boilerplate on the
 web outside of some dated github projects like this:  
[https://github.com/wayswe/auto-gmail-responder](https://github.
com/wayswe/auto-gmail-responder)

I would love to verify that the tech stack I am envisioning seems still right and curr
ent and there isn't any technology enable I am missing out on:  
— any scripting language  
— Gmail API (Oauth)  
— Open
AI API  
— LangChain

I have done a lot of scripting and OpenAI and Google API integrations so that part I am comfortabl
e with; the LangChain part is a question mark knowing it has recently gotten a bad rep for 'too much abstraction' ? Also
 wondering if any of the currently frequently discussed 'agent frameworks' from the big LLMs would/could accelerate deve
lopment here?

Appreciate any input from more experienced folks. TIA. 
```
---

     
 
all -  [ Launch: LangGraph Unofficial Virtual Meetup Series! ](https://www.reddit.com/r/artificial/comments/1gz044n/launch_langgraph_unofficial_virtual_meetup_series/) , 2024-11-28-0914
```
hey everyone! excited to announce the first community-driven virtual meetup focused entirely on LangGraph, LangChain's f
ramework for building autonomous agents.

**when:** tuesday, november 26th, 2024 two sessions to cover all time zones:


* 9:00 AM CST (Europe/India/West Asia/Africa)
* 5:00 PM CST (Americas/Oceania/East Asia)

**what to expect:** this is a 
chance to connect with other developers working on agent-based systems, share experiences, and learn more about LangGrap
h's capabilities. whether you're just getting started or already building complex agent architectures, you'll find value
 in joining the community.

**who should attend:**

* developers interested in autonomous AI agents
* LangChain users lo
oking to level up their agent development
* anyone curious about the practical applications of agentic Ai systems

**for
mat:** virtual meetup via Zoom

**join us:** [https://www.meetup.com/langgraph-unofficial-virtual-meetup-series](https:/
/www.meetup.com/langgraph-unofficial-virtual-meetup-series)

let's build the future of autonomous AI systems together! f
eel free to drop any questions in the comments.
```
---

     
 
all -  [ Track Token Usage for Azure ChatOpenAI ](https://www.reddit.com/r/LangChain/comments/1gyty0e/track_token_usage_for_azure_chatopenai/) , 2024-11-28-0914
```
I am using AzureChatOpenAI with langchain PromptTemplate using Python.

Is there any way I can calculate the token count
 and associated Azure cost for the LLM calls?

I've tried to print the usage metadata from llm calls but it's not printi
ng the token info 

Please suggest how to track the Usage?


```
---

     
 
MachineLearning -  [ [P] Open-source declarative framework to build LLM applications - looking for contributors ](https://www.reddit.com/r/MachineLearning/comments/1gkpazh/p_opensource_declarative_framework_to_build_llm/) , 2024-11-28-0914
```
I've been building LLM-based applications, and was super frustated with all major frameworks - langchain, autogen, crewA
I, etc. They also seem to introduce a pile of unnecessary abstractions. It becomes super hard to understand what's going
 behind the curtains even for very simple stuff.

[So I just published this open-source framework GenSphere.](https://gi
thub.com/octopus2023-inc/gensphere) The idea is have something like **Docker for LLMs**. You build applications with YAM
L files, that define an execution graph. Nodes can be either LLM API calls, regular function executions or other graphs 
themselves. Because you can nest graphs easily, building complex applications is not an issue, but at the same time you 
don't lose control.

You basically code in YAML, stating what are the tasks that need to be done and how they connect. O
ther than that, you only write individual python functions to be called during the execution. No new classes and abstrac
tions to learn.

Its all open-source. **Now I'm looking for contributors** to adapt the framework for cycles and conditi
onal nodes - which would allow full-fledged agentic system building! Pls reach out  if you want to contribute, there are
 tons of things to do!

PS: [you can read the detailed docs here,](https://gensphere.readthedocs.io/en/latest/) And go o
ver this quick [Google Colab tutorial.](https://github.com/octopus2023-inc/gensphere/blob/main/examples/gensphere_tutori
al.ipynb)
```
---

     
