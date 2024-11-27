 
all -  [ Optimize your LangChain program with Cognify! ](https://www.reddit.com/r/LangChain/comments/1h0jjbh/optimize_your_langchain_program_with_cognify/) , 2024-11-27-0913
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

     
 
all -  [ RAG - how to ensure a date fields in metadata is used to get latest data? ](https://www.reddit.com/r/LangChain/comments/1h0ih0x/rag_how_to_ensure_a_date_fields_in_metadata_is/) , 2024-11-27-0913
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

     
 
all -  [ Junior Engineer here. Looking forwared to getting my Resume review / roasted.  ](https://www.reddit.com/r/developersIndia/comments/1h0hs5x/junior_engineer_here_looking_forwared_to_getting/) , 2024-11-27-0913
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

     
 
all -  [ Is it possible to add a tool call response to the state  ](https://www.reddit.com/r/LangGraph/comments/1h0gcxb/is_it_possible_to_add_a_tool_call_response_to_the/) , 2024-11-27-0913
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

     
 
all -  [ Context Limitations When Returning Large Lists with GPT-4o and Microsoft GraphRAG ](/r/LocalLLaMA/comments/1h0fhyg/context_limitations_when_returning_large_lists/) , 2024-11-27-0913
```

```
---

     
 
all -  [ Seeking Advice on Parsing and Cleaning Legacy Documents ](https://www.reddit.com/r/LangChain/comments/1h0esud/seeking_advice_on_parsing_and_cleaning_legacy/) , 2024-11-27-0913
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

     
 
all -  [ Has anyone used Milvus or Qdrant in cloud? Whats been your experience? ](https://www.reddit.com/r/LangChain/comments/1h0cxtk/has_anyone_used_milvus_or_qdrant_in_cloud_whats/) , 2024-11-27-0913
```
I am planning to build something in prod, any feedback would be great. thanks
```
---

     
 
all -  [ Observability Tools AWS ](https://www.reddit.com/r/LangChain/comments/1h0bjl3/observability_tools_aws/) , 2024-11-27-0913
```
What observability tools are you using right now ? 

I am using aws stack with bedrock and amazon knowledge base and I a
m trying to find a good observability tools like langsmith,  but in AWS environment.  
```
---

     
 
all -  [ Suggestions to host a huggingface model on VLLM + triton server ](https://www.reddit.com/r/LangChain/comments/1h0bgsl/suggestions_to_host_a_huggingface_model_on_vllm/) , 2024-11-27-0913
```
I'm trying to host Qwen 2.5 model on vLLM and triton server. Can anyone suggest me best resource that can help to do it 
correctly. I'm new to this. Any suggestions are also welcome. 

thanks in advance!
```
---

     
 
all -  [ Writer helper tool I've started working on - worth making into a thing or pretty useless? ](https://www.reddit.com/r/LangChain/comments/1h0b10x/writer_helper_tool_ive_started_working_on_worth/) , 2024-11-27-0913
```
https://reddit.com/link/1h0b10x/video/pxvzc467s83e1/player


```
---

     
 
all -  [ Calling Scrapy multiple times (getting ReactorNotRestartable ) ](https://www.reddit.com/r/scrapy/comments/1h0avo7/calling_scrapy_multiple_times_getting/) , 2024-11-27-0913
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

     
 
all -  [ Langchain react agent tool streaming ](https://www.reddit.com/r/LangChain/comments/1h09zge/langchain_react_agent_tool_streaming/) , 2024-11-27-0913
```
I am using LangChain native react\_agent implementation and I have a tool `ask_question` and sometime agent is calling t
hat tool depending upon the context. So I want to stream the input of the `ask_qesution` to user. What is the best way t
o do it? In LangChain, streaming response works only for the final answer not for the tool\_input so far.
```
---

     
 
all -  [ [For Hire] Programmer/Web Developer/IT Consultant (Python, PHP, AI, etc.) ](https://www.reddit.com/r/forhire/comments/1h06zwo/for_hire_programmerweb_developerit_consultant/) , 2024-11-27-0913
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

     
 
all -  [ Building an Application Stack from Scratch with AI (agents) - Seeking Advice, Frameworks, Resources, ](https://www.reddit.com/r/softwarearchitecture/comments/1h036ko/building_an_application_stack_from_scratch_with/) , 2024-11-27-0913
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

     
 
all -  [  Building an Application Stack from Scratch with AI (agents) - Seeking Advice, Frameworks, Resources ](https://www.reddit.com/r/LangChain/comments/1h032wj/building_an_application_stack_from_scratch_with/) , 2024-11-27-0913
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

     
 
all -  [ Advice on Fine-Tuning an LLM for Scored Interpretation Feedback ](https://www.reddit.com/r/LangChain/comments/1gzy5vh/advice_on_finetuning_an_llm_for_scored/) , 2024-11-27-0913
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

     
 
all -  [ Complex Chain Prompting  ](https://www.reddit.com/r/LangChain/comments/1gzt3bk/complex_chain_prompting/) , 2024-11-27-0913
```
I have a complex flow for writing articles, including generating article flow/structure + outlines based on sources, the
n creating sub-outlines, generating section by section while maintaining the flow and structure. then translating it etc
. 

What would be a good Framework, or platform, as well as strategies to create a Co-pilot that involves a predefined w
orkflow as well as human input at every step.
```
---

     
 
all -  [ VectorStore query returns a generic response, as if my information isn't used, is this query correct ](https://www.reddit.com/r/LangChain/comments/1gzq5ko/vectorstore_query_returns_a_generic_response_as/) , 2024-11-27-0913
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

     
 
all -  [ Overcoming output token limit with agent generating structured output ](https://www.reddit.com/r/LangGraph/comments/1gzpz2n/overcoming_output_token_limit_with_agent/) , 2024-11-27-0913
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

     
 
all -  [ Langchain & Langgraph's documentation is so messed up, even ClosedAI couldn't create an error-free a ](https://www.reddit.com/r/Langchaindev/comments/1gzlxy8/langchain_langgraphs_documentation_is_so_messed/) , 2024-11-27-0913
```
Dear Langchain/Langgraph Team, 

Please update the documentation and kindly add more examples with other LLMs as well. I
t seems you're only dedicated to ClosedAI.

This is what I had asked ClosedAI: create a single node SQL Agent using Olla
ma that gets some input from a vector store along with user's input question.
```
---

     
 
all -  [ Claude/Langchain starter tutorial  ](https://www.reddit.com/r/AI_Agents/comments/1gzl1zo/claudelangchain_starter_tutorial/) , 2024-11-27-0913
```
Can anyone provide me with AI Agent building tutorial as a starter guide, cant find a good resource anywhere
```
---

     
 
all -  [ Need help providing more information to LLM regarding prompts ](https://www.reddit.com/r/LangChain/comments/1gzj92z/need_help_providing_more_information_to_llm/) , 2024-11-27-0913
```
So I’m working on this Text to SQL use case, and one thing I’m struggling with is making LLM understand what the prompts
 mean. For example, if I ask for top performing teams in 2024, the LLM does not have an idea what top performing teams m
ean. I’m exploring ways to get this through to the model in the most effective way. Mind you that I am working with tabl
es with large number of columns and passing everything in the prompt is not an option. I am open to any suggestions, may
be something like Human In Loop?
My entire app is created using lang graph with multiple agent interactions. 
```
---

     
 
all -  [ LlamaParse vs Docling for extracting information from bank account statements (PDF)? ](https://www.reddit.com/r/LangChain/comments/1gzdnev/llamaparse_vs_docling_for_extracting_information/) , 2024-11-27-0913
```
I've recently learned about IBM Docling (https://research.ibm.com/blog/docling-generative-AI) which works super well. Ho
wever I wonder how it compares to LlamaParse and what some of the differences are.

How could I go about benchmarking it
?
```
---

     
 
all -  [ Are there any free versions of LangChain or any similar thing? ](https://www.reddit.com/r/developer/comments/1gzcih2/are_there_any_free_versions_of_langchain_or_any/) , 2024-11-27-0913
```
I want to learn creating AI apps, are there any free models?
```
---

     
 
all -  [ Curious Question on the state of model Knowledge and State of LLMs.  ](https://www.reddit.com/r/ChatGPTCoding/comments/1gzav0j/curious_question_on_the_state_of_model_knowledge/) , 2024-11-27-0913
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

     
 
all -  [ Chucking strategy for legal docs ](https://www.reddit.com/r/LangChain/comments/1gza6z5/chucking_strategy_for_legal_docs/) , 2024-11-27-0913
```
For those working on legal or insurance document where there are pages of conditions, what is your chunking strategy?

I
 am using docling for parsing files and semantic double merging chunking. Not satisfied with results.
```
---

     
 
all -  [ Starting point to building a GMail supervised email responder? Validate my stack ](https://www.reddit.com/r/OpenAI/comments/1gz9q81/starting_point_to_building_a_gmail_supervised/) , 2024-11-27-0913
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

     
 
all -  [ Launch: LangGraph Unofficial Virtual Meetup Series! ](https://www.reddit.com/r/artificial/comments/1gz044n/launch_langgraph_unofficial_virtual_meetup_series/) , 2024-11-27-0913
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

     
 
all -  [ Track Token Usage for Azure ChatOpenAI ](https://www.reddit.com/r/LangChain/comments/1gyty0e/track_token_usage_for_azure_chatopenai/) , 2024-11-27-0913
```
I am using AzureChatOpenAI with langchain PromptTemplate using Python.

Is there any way I can calculate the token count
 and associated Azure cost for the LLM calls?

I've tried to print the usage metadata from llm calls but it's not printi
ng the token info 

Please suggest how to track the Usage?


```
---

     
 
all -  [ [For Hire] Frontend and Backend Developer with the top and latest development technologies for a gre ](https://www.reddit.com/r/B2BForHire/comments/1gytgzf/for_hire_frontend_and_backend_developer_with_the/) , 2024-11-27-0913
```
Hi Redditors,

I'm Emad a Full-stack Web developer/engineer with 8 years of experience, and I'm looking for new projects
 to start working on, please take a look at my portfolio here [https://www.sx-portfolio.com](https://www.sx-portfolio.co
m) (let me know if you need more examples or direct links to live websites in the PM)

**Here is my skill set:**

**For 
Frontend:**

* HTML / CSS
* JS / ESNext
* Webpack / Gulp / Grunt / Gatsby
* React (With Redux, Zustand, or MobX)
* Next.
js
* Vuejs (With VueX)
* Angular
* TypeScript

**For Backend:**

* Node.js
* Python
* Express.js
* MongoDB
* Mongoose
* 
Nest.js
* GraphQL
* Meteor (with Apollo and React)
* TypeScript

**For AI-based projects:**

* Python
* Langchain
* Fast
API
* Uvicorn
* Pydantic

**For Desktop Apps:**

* Electron

**For Mobile Apps (iOS and Android):**

* React Native
* Ex
po

**For Design:**

* Photoshop
* Illustrator

**Here is my Resume:**  [My resume link!](http://www.sx-portfolio.com/we
bsite-resources/My%20resume.pdf)

**And here are some testimonials from my clients :)**

* [Slips](https://www.reddit.co
m/r/testimonials/comments/agfmwf/pos_swordx10_is_a_brilliant_developer_and_a/)
* [VidSync](https://www.reddit.com/r/test
imonials/comments/5gvz3d/pos_uswordx10_excellent_frontend_dev/)
* [Las Cruces Directory](https://www.reddit.com/r/testim
onials/comments/5hyks4/uswordx10_is_awesome/)
* [SigurenZalog](https://www.reddit.com/r/testimonials/comments/5jsfqf/pos
_quality_web_design_from_uswordx10/)
* [Bitlounge](https://www.reddit.com/r/testimonials/comments/5lh2pz/pos_uswordx10_t
op_fontend_devdesigner/)
* [Foxul](https://www.reddit.com/r/testimonials/comments/5l3p8j/pos_quality_web_coding_from_usw
ordx10/)
* [LootTicket](https://www.reddit.com/r/testimonials/comments/5nfh1j/pos_uswordx10_is_an_amazing_front_end_dev/
)

**My Pricing:**

I work hourly for $35/hr and my fixed prices depend on your project's complexity.

Don't worry about
 the price, just PM me with your project and I'm sure we can figure out something that goes with your budget. :)

If you
 have any questions don't hesitate to PM me and I will be more than happy to answer you :) and here is my portfolio agai
n if you need my contact details [www.sx-portfolio.com](https://www.sx-portfolio.com) (Click the red handle in the top-r
ight or pm me for it)
```
---

     
 
all -  [ RAG application with text data in no specific format. Ways to do embedding or chunking? ](https://www.reddit.com/r/LangChain/comments/1gymmyl/rag_application_with_text_data_in_no_specific/) , 2024-11-27-0913
```
 'Best practices for chunking and structuring unformatted text data for RAG-based QA system'

I'm developing a Question-
Answering system using RAG to handle customer queries about product features and specifications. Here's my current situa
tion:

Data Characteristics:
- Source: Converted PDF documents containing product instructions/documentation
- Current f
ormat: Plain text files with ~200-300 lines each, separated only by newlines
- Original format (PDFs): Well-structured d
ocuments with paragraphs, each focusing on specific product features
- Content type: Product specifications, feature des
criptions, and usage instructions

Current Implementation:
- Currently embedding entire documents into the vector databa
se
- Customer queries typically focus on specific product attributes or features

Challenges:
1. Lost document structure
 after PDF parsing (I cannot control them to do the parsing in a specific way)
2. No clear paragraph or section demarcat
ion
3. Potential inefficiency in embedding and retrieving from entire documents

Questions:
1. What are the recommended 
approaches for chunking this unstructured text data to maintain semantic coherence?
2. Should I attempt to reconstruct t
he document structure programmatically before embedding?
3. What chunking strategies would work best for feature-focused
 customer queries?
4. Are there any preprocessing steps or tools you'd recommend to improve text segmentation?


Embeddi
ng model used ada02.

```
---

     
 
all -  [ Vercel.live is loading 3.51MB of javascript of every reload ](https://www.reddit.com/r/nextjs/comments/1gyj6vm/vercellive_is_loading_351mb_of_javascript_of/) , 2024-11-27-0913
```
\[Solved\]  
Hi, I was checking network tab and checked the usage and vercel live is using 3.51mb of resource. I am wond
ering, Is there is a way to reduce it and how this usage is determined I mean where it is coming from.  
This is my site
 for referrence - [My portfolio](https://ypiyush.tech)

https://preview.redd.it/fwtb4zcn6s2e1.png?width=1920&format=png&
auto=webp&s=fa6685dbc45635c4a74322e62099510ee556f329
```
---

     
 
all -  [ RAG with a language that is not english ](https://www.reddit.com/r/LangChain/comments/1gya4ox/rag_with_a_language_that_is_not_english/) , 2024-11-27-0913
```
I'm trying to use langchain to build this chatbot that responds on FAQ data.

The FAQ data is really short and contains 
20 questions more or less. 

I'm struggling with embeddings and I figured out that with a similarity search I cannot ret
rieve the most similar question when the prompt contain synonyms. This is due the fact that my data source is not in eng
lish (i used a multilingual embedding model that you can find \[here\](https://huggingface.co/BAAI/bge-m3) )  
For the g
eneration step I've implemented a prompt that prevent the LLM to wonder outside the boundaries of the context and most o
f the times it respond by blocking the user question.  
From a user perspective I will be very upset if it couldnt respo
nd to my question.

I've implemented also another solution that doesn't rely on vectordb and uses the LLM (passing both 
the question and the answer of the FAQ data) but it still struggle when asking some specific questions.

Any other ideas
 in how to complete this simple project are welcome since I'm starting to doubt the feasibility of the project due to th
e poor performances
```
---

     
 
all -  [ Exfunc: API for your AI to take action on the web without a browser ](https://www.reddit.com/r/LLMDevs/comments/1gy717b/exfunc_api_for_your_ai_to_take_action_on_the_web/) , 2024-11-27-0913
```
Today, AI models can process and generate data very well but can’t use software that we use to do our work. This is larg
ely because software that we use is primarily GUI-based and requires a browser to access. We’re trying to change that wi
th [Exfunc](https://www.exfunc.com), which is an API service that your AI can use to fetch data and take action in vario
us software applications without a browser!

With just an API call, you can fetch reviews from Yelp, search properties o
n Zillow, or extract contact information from company websites. We take care of the rest from provisioning infrastructur
e to scaling browser automations. Check out our [documentation](https://docs.exfunc.com/api-reference) and [cookbooks](h
ttps://github.com/carvedai/exfunc/tree/main/cookbooks).

[You can use the chat assistant here: https:\/\/app.exfunc.com\
/chat It is built on top of assistant-ui-stockbroker: https:\/\/github.com\/Yonom\/assistant-ui-stockbroker](https://red
dit.com/link/1gy717b/video/bc06i0om5p2e1/player)

With our [agent toolkit](https://github.com/carvedai/exfunc-agent-tool
kit), you can integrate Exfunc API into your agents in a few lines of code. It supports [Vercel’s AI SDK](https://sdk.ve
rcel.ai) and [LangChain](https://www.langchain.com) and works with any LLM provider that supports function calling.

   
 import {generateText} from 'ai';
    import {openai} from '@ai-sdk/openai';
    import {ExfuncAgentToolkit} from '@exfu
nc/agent-toolkit/ai-sdk';
    
    const exfuncAgentToolkit = new ExfuncAgentToolkit({
      apiKey: process.env.EXFUNC_
API_KEY ?? '',  // This is the default and can be omitted
    });
    
    (async () => {
      const result = await gen
erateText({
        model: openai('gpt-4o-mini'),
        tools: {
          ...exfuncAgentToolkit.getTools(),
        }
,
        maxSteps: 5,
        prompt: 'get reviews for yin du wonton noodle in SF',
      });
      console.log(result.
text);
    })();

You can check out the source code of our toolkit here: [https://github.com/carvedai/exfunc-agent-toolk
it](https://github.com/carvedai/exfunc-agent-toolkit)

Key Features:

* Unified API: You can interact with many applicat
ions through our API without using a separate interface for each application. Standardization also makes it easy for AI 
to chain multiple API calls to accomplish a task (eg. sequential function calling).
* Type-safe, structured format: We p
rovide structured input and output formats and have Python and TypeScript SDKs that validate types.
* Serverless automat
ions: You don’t have to manage your own infrastructure to run browser automations.

You can sign up without a credit car
d and use it for free forever. Free tier limits should be generous enough for personal use. If you need higher limits, y
ou can message me, and I can move you to a paid plan.

API reference: [https://docs.exfunc.com/api-reference](https://do
cs.exfunc.com/api-reference)

Cookbooks: [https://github.com/carvedai/exfunc/tree/main/cookbooks](https://github.com/car
vedai/exfunc/tree/main/cookbooks)

Feel free to join our discord: [https://discord.com/invite/5TdjpyGKbq](https://discor
d.com/invite/5TdjpyGKbq)

Thanks!
```
---

     
 
all -  [ Exfunc: API for your AI to take action on the web without a browser ](https://www.reddit.com/r/LangChain/comments/1gy6vjv/exfunc_api_for_your_ai_to_take_action_on_the_web/) , 2024-11-27-0913
```
Today, AI models can process and generate data very well but can’t use software that we use to do our work. This is larg
ely because software that we use is primarily GUI-based and requires a browser to access. We’re trying to change that wi
th [Exfunc](https://www.exfunc.com), which is an API service that your AI can use to fetch data and take action in vario
us software applications without a browser!

With just an API call, you can fetch reviews from Yelp, search properties o
n Zillow, or extract contact information from company websites. We take care of the rest from provisioning infrastructur
e to scaling browser automations. Check out our [documentation](https://docs.exfunc.com/api-reference) and [cookbooks](h
ttps://github.com/carvedai/exfunc).

[You can use the chat assistant here: https:\/\/app.exfunc.com\/chat It is built on
 top of assistant-ui-stockbroker: https:\/\/github.com\/Yonom\/assistant-ui-stockbroker](https://reddit.com/link/1gy6vjv
/video/bc06i0om5p2e1/player)

With our [agent toolkit](https://github.com/carvedai/exfunc-agent-toolkit), you can integr
ate Exfunc API into your agents in a few lines of code. It supports [Vercel’s AI SDK](https://sdk.vercel.ai) and [LangCh
ain](https://www.langchain.com) and works with any LLM provider that supports function calling.

    from langchain_open
ai import ChatOpenAI
    from langgraph.prebuilt import create_react_agent
    from exfunc_agent_toolkit.langchain.toolk
it import ExfuncAgentToolkit
    
    llm = ChatOpenAI(model='gpt-4o-mini')
    
    exfunc_agent_toolkit = ExfuncAgentT
oolkit()
    
    tools = []
    tools.extend(exfunc_agent_toolkit.get_tools())
    
    langgraph_agent_executor = crea
te_react_agent(llm, tools)
    
    example_query = 'what did dalton caldwell say recently on twitter?'
    
    events 
= langgraph_agent_executor.stream(
        {'messages': [('user', example_query)]},
        stream_mode='values',
    )

    for event in events:
        event['messages'][-1].pretty_print()

You can check out the source code of our toolkit 
here: [https://github.com/carvedai/exfunc-agent-toolkit](https://github.com/carvedai/exfunc-agent-toolkit)

Key Features
:

* Unified API: You can interact with many applications through our API without using a separate interface for each ap
plication. Standardization also makes it easy for AI to chain multiple API calls to accomplish a task (eg. sequential fu
nction calling).
* Type-safe, structured format: We provide structured input and output formats and have Python and Type
Script SDKs that validate types.
* Serverless automations: You don’t have to manage your own infrastructure to run brows
er automations.

You can sign up without a credit card and use it for free forever. Free tier limits should be generous 
enough for personal use. If you need higher limits, you can message me, and I can move you to a paid plan.

Feel free to
 join our discord: [https://discord.com/invite/5TdjpyGKbq](https://discord.com/invite/5TdjpyGKbq)

Thanks!
```
---

     
 
all -  [ Applying from last 3 months but not getting interview calls  ](https://i.redd.it/zaoxv775no2e1.jpeg) , 2024-11-27-0913
```
I started looking for a job in Pune from last three months but not getting any interview calls. Few just called to ask i
nformation but no updates further. Is my resume wrong in some way? Currently im at 9LPA and asking for 30% hike, is I’m 
asking too much? I’m ok if any company match the offer in Pune. Are my expectations are too much or am I applying for th
e wrong companies? I’m applying to every company on naukri, linkedin, indeed. 
```
---

     
 
all -  [ Create a OpenAI swarm agents what are working like a label record but just for programming to reach  ](https://www.reddit.com/r/ChatGPT/comments/1gy38ci/create_a_openai_swarm_agents_what_are_working/) , 2024-11-27-0913
```
Creating a “swarm” of OpenAI agents functioning like a record label for programming is an innovative concept. Here’s a f
ramework for how you could design such a system:

Overview

This platform would manage a collective of AI agents and hum
an programmers, guiding their collaborative efforts towards achieving specific programming-related goals. Think of it as
 a talent label, but for coding and software development.

Key Components

	1.	Swarm Architecture
	•	Core Agent: The lea
der that coordinates other agents, assigns tasks, and ensures alignment with the target goals.
	•	Specialist Agents:
	•	
Frontend, Backend, AI/ML, DevOps, etc.
	•	Agents trained to excel in specific domains, analogous to artists on a record 
label.
	•	Quality Control Agents: These ensure that the output meets coding standards, is efficient, and is free of bugs
.
	2.	Human Collaborators
	•	A pool of human programmers acts as the “mentors” or “producers,” reviewing, refining, and 
expanding the output of the swarm.
	3.	Target-Oriented Design
	•	Goal Definition: A central repository where the “record
 label” (or the user) defines clear goals for a project (e.g., create a new app, optimize an algorithm, or build a platf
orm).
	•	Agent Assignments: Based on the goal, tasks are distributed among agents in parallel or sequentially.
	4.	Learn
ing & Feedback
	•	Every iteration is assessed by both AI-based quality checks and human input.
	•	Continuous learning pi
pelines allow agents to improve based on feedback.

How It Works

	1.	Project Kickoff
	•	The user submits a project idea
 and requirements (akin to a pitch for a record).
	•	The Core Agent breaks down the idea into smaller milestones.
	2.	Ta
sk Allocation
	•	Each Specialist Agent takes on a specific task (e.g., API development, UI design).
	•	Agents collaborat
e using shared models, tools, and repositories like Git.
	3.	Real-Time Collaboration
	•	Agents interact in real-time, sh
aring intermediate results and aligning on dependencies.
	•	Use of a centralized coordination platform for version contr
ol and updates.
	4.	Quality Assurance
	•	Outputs are reviewed by Quality Control Agents.
	•	Human programmers provide fi
nal reviews and adjustments, ensuring production-quality output.
	5.	Release
	•	Once polished, the project is “released”
 to the client, similar to how a record is launched.

Technological Stack

	1.	Infrastructure
	•	Cloud Services: AWS, Az
ure, or Google Cloud for hosting.
	•	Communication: APIs for inter-agent communication, message queues for task distribu
tion.
	2.	Programming Frameworks
	•	Python (for ML and orchestration).
	•	Tools like LangChain for chaining agents.
	•	G
itHub/GitLab for version control.
	3.	Learning Systems
	•	Fine-tuning GPT models for domain-specific tasks.
	•	RLHF (Rei
nforcement Learning with Human Feedback) to refine agent interactions.
	4.	Monitoring and Management
	•	Dashboards to tr
ack progress and bottlenecks.
	•	Logging mechanisms for debugging and improvements.

Benefits

	1.	Parallel Development

	•	Tasks handled simultaneously by agents, speeding up development.
	2.	Cost-Effective
	•	Reduces the need for large hum
an teams by leveraging AI.
	3.	Scalable
	•	Easily add or remove agents based on project complexity.
	4.	Talent Discovery

	•	Like a record label scouts talent, the system identifies promising programmers and AI modules.

Challenges and Solut
ions

	1.	Coordination Among Agents
	•	Solution: Implement robust communication protocols and a hierarchy of responsibil
ities.
	2.	Maintaining Code Quality
	•	Solution: Use linters, static code analyzers, and human oversight.
	3.	Avoiding R
edundancy
	•	Solution: Agents access a shared knowledge base to prevent duplication.

Would you like me to expand on any
 specific part, such as implementation details, an example use case, or a business plan?

Below is a Python-based implem
entation of a basic swarm agent framework using LangChain and asyncio for agent orchestration. This is a prototype to de
monstrate how tasks can be distributed to different agents, monitored, and combined into a single project pipeline.

Cod
e: Swarm Agent Framework

import asyncio
from langchain.agents import initialize_agent, Tool
from langchain.chat_models 
import ChatOpenAI
from langchain.prompts import PromptTemplate

# Initialize OpenAI API
openai_model = ChatOpenAI(temper
ature=0.2, model='gpt-4')

# Define specialized tools (agents for specific tasks)
def frontend_agent(task_description):

    return f'Frontend Agent: Create HTML/CSS/JS for the task: {task_description}.'

def backend_agent(task_description):

    return f'Backend Agent: Develop Python backend for the task: {task_description}.'

def devops_agent(task_descriptio
n):
    return f'DevOps Agent: Set up CI/CD pipeline for the task: {task_description}.'

# Define task manager
class Tas
kManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, agent_func, task_description):
       
 self.tasks.append((agent_func, task_description))

    async def execute_tasks(self):
        results = await asyncio.g
ather(
            *[self.run_agent(agent_func, task_description) for agent_func, task_description in self.tasks]
      
  )
        return results

    async def run_agent(self, agent_func, task_description):
        prompt = agent_func(tas
k_description)
        response = await asyncio.to_thread(lambda: openai_model.run(prompt))
        return response

# M
ain Swarm Orchestration
async def main_project_pipeline(project_goal):
    print(f'Initializing swarm for project: {proj
ect_goal}')

    # Break down project into tasks
    task_manager = TaskManager()
    task_manager.add_task(frontend_age
nt, 'Design the homepage layout')
    task_manager.add_task(backend_agent, 'Create an API endpoint for user registration
')
    task_manager.add_task(devops_agent, 'Set up Docker and deploy to AWS')

    # Execute tasks concurrently
    resu
lts = await task_manager.execute_tasks()

    # Combine and finalize results
    print('\nTask Results:')
    for i, res
ult in enumerate(results, 1):
        print(f'Task {i} Result:\n{result}\n')

    # Integration (placeholder)
    final_
output = 'Integrated Project:\n' + '\n'.join(results)
    print('Final Integrated Output:\n', final_output)

# Run the s
warm pipeline
if __name__ == '__main__':
    asyncio.run(main_project_pipeline('Build a small-scale web application'))


How It Works

	1.	Agents:
	•	Each agent function (e.g., frontend_agent, backend_agent) represents a specialized AI modul
e that works on a specific part of the project.
	•	These are simplistic placeholders; in a real system, they could use f
ine-tuned models for specific programming tasks.
	2.	Task Manager:
	•	A central orchestrator that assigns tasks to agent
s and ensures they run concurrently using asyncio.
	3.	Asynchronous Execution:
	•	All agents run their tasks in parallel
, improving efficiency.
	4.	Final Integration:
	•	Outputs from all agents are gathered and combined into a final deliver
able. This part can be expanded for more complex workflows (e.g., testing and deploying).

Output Example

When you run 
the code, it will simulate agents handling the tasks:

Initializing swarm for project: Build a small-scale web applicati
on

Task Results:
Task 1 Result:
Frontend Agent: Create HTML/CSS/JS for the task: Design the homepage layout.

Task 2 Re
sult:
Backend Agent: Develop Python backend for the task: Create an API endpoint for user registration.

Task 3 Result:

DevOps Agent: Set up CI/CD pipeline for the task: Set up Docker and deploy to AWS.

Final Integrated Output:
Frontend Ag
ent: Create HTML/CSS/JS for the task: Design the homepage layout.
Backend Agent: Develop Python backend for the task: Cr
eate an API endpoint for user registration.
DevOps Agent: Set up CI/CD pipeline for the task: Set up Docker and deploy t
o AWS.

Next Steps

To expand this framework:
	1.	Replace placeholder functions: Use actual programming logic or pre-tra
ined fine-tuned models to generate code.
	2.	Integrate GitHub API: Automate code commits, reviews, and pull requests.
	3
.	Add Testing Agent: Include an agent for automated testing (unit, integration, etc.).
	4.	Deployment Pipeline: Implemen
t a real CI/CD system using tools like Jenkins or GitHub Actions.

Would you like me to add specific functionality, like
 API integration or testing automation?
```
---

     
 
all -  [ Pointers on local LLM with Ollama/OpenWebUI and RAG ](https://www.reddit.com/r/LocalLLaMA/comments/1gy0z2d/pointers_on_local_llm_with_ollamaopenwebui_and_rag/) , 2024-11-27-0913
```
Hi,

I want to be able to ask a local LLM questions on my own documents. Say I have a bunch of manuals for machines and 
my own notes, I want to be able to ask 'what does error code 12 mean on machine XY'. I researched that topic and it seem
s that RAG is what I'm looking for. I also looked that up. Now it seem LangChain and Chroma-DB is are tools that can be 
used for this.

As far as I understood, you (for lack of better words) 'train' the RAG model on your files with LangChai
n, and the resulting 'model' (again, for lack of better words) gets stored on Chroma-DB for later access by whatever LLM
.

What I'd prefer was, to be able to simply drop new files in a folder, that then gets used by the LLM. I wouldn't mind
 if 'training' is a scheduled thing.

Is that correct? Can you maybe give me some advice on better solutions or point me
 to a guide you think is good? I want to deploy with Docker, in case that is important.

Thanks


```
---

     
 
MachineLearning -  [ [P] Open-source declarative framework to build LLM applications - looking for contributors ](https://www.reddit.com/r/MachineLearning/comments/1gkpazh/p_opensource_declarative_framework_to_build_llm/) , 2024-11-27-0913
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

     
