 
all -  [ Caching in LLM Apps ](https://www.reddit.com/r/LangChain/comments/1cz3ls8/caching_in_llm_apps/) , 2024-05-24-0911
```
Which is your favourite caching technique in LLM Applications. 
Is it in memory or something else.
Which caching integra
tion you like the most and why for a scalable and reliable application.
```
---

     
 
all -  [ ReAct Agent with 0.3 instruct ](https://www.reddit.com/r/MistralAI/comments/1cz2gbb/react_agent_with_03_instruct/) , 2024-05-24-0911
```
Hi upgraded my Langchain ReAct agent with the new 0.3 model that dropped yesterday and wow!

it's faster, more determini
stic, and tool calling is much better.

Haven't tried out the new functions yet since I have no idea how to implement th
is in my framework.

Any tips?

Also, if you have a good prompt to ensure that the agent visits a website is the link is
 provided would be great.
```
---

     
 
all -  [ Is there a better way to get this json into my vectordb? (ollama, chromadb, gp4allembeddings) ](https://www.reddit.com/r/LocalLLaMA/comments/1cz1e2f/is_there_a_better_way_to_get_this_json_into_my/) , 2024-05-24-0911
```
I've been working on a simple chatbot, it responds to inquiries in intercom and in telegram. It makes a database of info
rmation to pull from based on current support articles in Intercom. It worked pretty well with 150 articles, but as I've
 added more and its up to almost 400 it seems to completely miss easy questions now, and I feel like i'm not ingesting a
ll that information in the most efficient way possible.

 It uses Ollama/Llama3 for the model, i have a custom modelfile
 that  looks like:
> FROM llama3
> 
> PARAMETER temperature 0.3
> 
> SYSTEM You are a helpful AI assistant for the 'X' p
latform. Your role is to provide detailed, accurate answers to user questions based on the information in your knowledge
 base, with the goal of assisting users without requiring a human response when possible. If a question can have multipl
e answers depending on the situation, provide guidance on the different options. When giving instructions, be as specifi
c as possible. Never answer questions that are remotely off-topic. Just let them know you can’t help with that.

It uses
 gpt4allembeddings/langchain for embedding and chromadb for the database.

I have a pre-prompt implemented that reads li
ke:
> Answer the question based on the provided context. Do not include introductory phrases. If the question is unclear
 or unrelated to the context, simply state 'I apologize, I can't help with your query, let me get a team member to assis
t.' Do not provide additional explanations.

The json that intercom is providing looks like this:
>         [
>         
  {
>             'id': '123',
>             'type': 'article',
>             'workspace_id': '123',
>             'pare
nt_id': null,
>             'parent_type': null,
>             'parent_ids': [],
>             'title': 'Title',
>      
       'description': 'Description',
>             'body': 'Body',
>             'author_id': 123,
>             'state'
: 'draft',
>             'created_at': 171,
>             'updated_at': 171,
>             'url': null
>           },
> 
          {
>             'id': '234',
>             'type': 'article',
>             'workspace_id': '234',
>          
   'parent_id': null,
>             'parent_type': null,
>             'parent_ids': [],
>             'title': 'Title',

>             'description': 'Description',
>             'body': 'Body',
>             'author_id': 123,
>            
 'state': 'draft',
>             'created_at': 171,
>             'updated_at': 171,
>             'url': null
>        
   },
>     
Here is my script please dont judge i'm an absolute hobbyist and this is my first time trying to dive into 
AI stuff:

    import json
    import logging
    import os
    import aiohttp
    import asyncio
    from dotenv import
 load_dotenv
    from quart import Quart, jsonify, request
    from telethon import TelegramClient, events
    from tele
thon.errors import RPCError, ChatAdminRequiredError, ChannelPrivateError
    from telethon.tl.types import PeerChannel
 
   from langchain_community.vectorstores import Chroma
    from langchain_community.embeddings import GPT4AllEmbeddings

    from langchain_core.prompts import PromptTemplate
    from langchain_community.llms import Ollama
    from langchain
.callbacks.manager import CallbackManager
    from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHa
ndler
    from langchain.chains import RetrievalQA
    from langchain.docstore.document import Document
    from hyperco
rn.config import Config
    from hypercorn.asyncio import serve
    import time
    
    os.makedirs('logs', exist_ok=Tr
ue)
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s', handlers=[
        logging.FileHandl
er('logs/app.log'),
        logging.StreamHandler()
    ])
    
    start_time = time.time()
    
    # .env
    load_do
tenv()
    api_id = os.getenv('API_ID')
    api_hash = os.getenv('API_HASH')
    bot_token = os.getenv('BOT_TOKEN')
    
intercom_token = os.getenv('INTERCOM_TOKEN')
    chat_id = int(os.getenv('CHAT_ID'))
    qa_chain_prompt_template = os.g
etenv('QA_CHAIN_PROMPT_TEMPLATE')
    
    app = Quart(__name__)
    
    client = TelegramClient('logs/tg_chat', api_id
, api_hash)
    
    vectorstore = None
    qa_chain = None
    
    QA_CHAIN_PROMPT = PromptTemplate(
        input_var
iables=['context', 'question'],
        template=qa_chain_prompt_template,
    )
    
    llm = Ollama(model='llama3-tem
p03', callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]))
    
    async def fetch_all_pages():
      
  url = 'https://api.intercom.io/articles'
        headers = {
            'Authorization': f'Bearer {intercom_token}',

            'Accept': 'application/json'
        }
        all_documents = []
        all_data = []
        async with a
iohttp.ClientSession() as session:
            while url:
                async with session.get(url, headers=headers) a
s response:
                    if response.status != 200:
                        logging.error(f'Failed to fetch data:
 {response.status}')
                        break
                    data = await response.json()
                    
all_data.extend(data.get('data', []))
                    if 'data' in data and data['data']:
                        do
cuments = [Document(page_content=article['body']) for article in data['data'] if article['body'].strip()]
              
          all_documents.extend(documents)
                    url = data.get('pages', {}).get('next', None)
        with
 open('info.json', 'w') as f:
            json.dump(all_data, f, indent=2)
        logging.info(f'Total records received
: {len(all_data)}')
        return all_documents
    
    async def rebuild_vectorstore():
        global documents, vec
torstore, qa_chain
        try:
            documents = await fetch_all_pages()
            if documents:
              
  vectorstore = Chroma.from_documents(documents=documents, embedding=GPT4AllEmbeddings())
                logging.info('
Documents processed and vector store rebuilt.')
                qa_chain = RetrievalQA.from_chain_type(
                
    llm,
                    retriever=vectorstore.as_retriever(),
                    chain_type_kwargs={'prompt': QA_C
HAIN_PROMPT},
                )
            else:
                logging.error('No valid documents with non-empty body 
found.')
        except Exception as e:
            logging.error(f'Error rebuilding vector store: {str(e)}')
    
    a
sync def handle_query(query):
        if qa_chain is None:
            logging.error('QA chain is not initialized.')
   
         return {'response': 'Initialization error: Vector store not available. Check log for details.', 'time_taken': 0
}
    
        start_time = time.time()
        try:
            result = qa_chain.invoke(query)
        except Exceptio
n as e:
            logging.error(f'Error during query handling: {str(e)}')
            return {'response': 'An error oc
curred while processing the query.', 'time_taken': 0}
    
        end_time = time.time()
        time_taken = end_time 
- start_time
    
        logging.info(f'Query result: {result}')
    
        if isinstance(result, dict):
            
result = result.get('result', 'No result field found in response.')
        elif isinstance(result, str):
            re
sult = result.strip()
        else:
            result = str(result).strip()
    
        if not result:
            res
ult = 'I apologize, but I don't have enough information to provide a helpful answer.'
    
        return {'response': r
esult, 'time_taken': time_taken}
    
    @app.route('/intercom', methods=['POST'])
    async def intercom_handler():
  
      data = await request.get_json()
        query = data.get('body')
        if query:
            result = await hand
le_query(query)
            response = result['response']
            time_taken = result['time_taken']
            retu
rn jsonify({'response': response, 'time_taken': time_taken}), 200
        else:
            logging.error('No query prov
ided in the request')
            return jsonify({'error': 'No query provided'}), 400
    
    @app.route('/rebuild_vect
orstore', methods=['POST'])
    async def rebuild_vectorstore_handler():
        await rebuild_vectorstore()
        ret
urn jsonify({'message': 'Vector store rebuilt'}), 200
    
    @client.on(events.NewMessage(pattern=r'^\.x (.+)', func=l
ambda e: e.text.lower().startswith('.x ')))
    async def answer_query(event):
        query = event.pattern_match.group
(1)
        logging.info(f'Received query: {query}')
        result = await handle_query(query)
        response = resul
t['response']
        time_taken = result['time_taken']
        await event.respond(f'```{response}```\n**Time to genera
te: {time_taken:.2f} seconds**', parse_mode='Markdown')
    
    @client.on(events.NewMessage(pattern='/rebuild'))
    a
sync def rebuild_vectorstore_command(event):
        logging.info('Received /rebuild command. Rebuilding the vector stor
e...')
        await event.respond('Rebuilding database...')
        await rebuild_vectorstore()
        await event.res
pond('Database rebuilt.')
    
    async def run_server():
        global start_time
        config = Config()
        c
onfig.bind = ['0.0.0.0:5001']
        
        async def custom_serve():
            end_time = time.time()
            
time_to_boot = end_time - start_time
            await send_message(chat_id, f'<span style='color:red'>Bot Online, Time 
to boot: {time_to_boot:.2f} seconds</span>')
            await serve(app, config)
    
        await custom_serve()
    

    async def send_message(chat_id, message):
        try:
            entity = await client.get_entity(PeerChannel(cha
t_id))
            await client.send_message(entity, message, parse_mode='html')
        except ChatAdminRequiredError:

            logging.error(f'Failed to send message to {chat_id}: Bot lacks admin rights.')
        except ChannelPrivate
Error:
            logging.error(f'Failed to send message to {chat_id}: Channel is private.')
        except RPCError as
 e:
            logging.error(f'Failed to send message to {chat_id}: {str(e)}')
    
    async def start():
        try:

            await client.start(bot_token=bot_token)
            logging.info('Telegram client connected.')
            
await rebuild_vectorstore()
            await run_server()
        except Exception as e:
            logging.error(f'Er
ror occurred: {str(e)}. Retrying in 5 seconds...')
            await asyncio.sleep(5)
            await start()
    
   
 async def main():
        try:
            await start()
        except KeyboardInterrupt:
            logging.info('Sc
ript interrupted by user.')
            await send_message(chat_id, '<span style='color:red'>Shutting Down</span>')
    
    finally:
            logging.info('Shutting down...')
            await client.disconnect()
            logging.info
('Client disconnected.')
            pending = [task for task in asyncio.all_tasks() if not task.done() and task is not 
asyncio.current_task()]
            for task in pending:
                task.cancel()
            await asyncio.gather(
*pending, return_exceptions=True)
            loop.stop()
            loop.close()
            logging.info('Script stop
ped.')
    
    if __name__ == '__main__':
        try:
            loop = asyncio.get_event_loop()
            loop.run
_until_complete(main())
        except RuntimeError as e:
            logging.error(f'Runtime error: {str(e)}')
        
finally:
            if not loop.is_closed():
                loop.close()


I'm not sure if i am embedding the json cor
rectly, i thought it would be straightforward in json format but the bad outputs make me second guess whatever im doing,
 really open to whatever, would love to learn what im missing here
```
---

     
 
all -  [ why two different kinds of messages? ](https://www.reddit.com/r/LangChain/comments/1cyz7kw/why_two_different_kinds_of_messages/) , 2024-05-24-0911
```
langchain\_core.messages.human.HumanMessage

langchain.schema.messages.HumanMessage

I got unsupported HumanMessage erro
r when using langchain and found out two kinds of messages. Why?
```
---

     
 
all -  [ [11 YOE] Unable To Get Any Tech Interviews With This Resume, What Am I Doing Wrong? ](https://www.reddit.com/r/resumes/comments/1cyyw3b/11_yoe_unable_to_get_any_tech_interviews_with/) , 2024-05-24-0911
```
https://preview.redd.it/gt05zrf5r72d1.png?width=5100&format=png&auto=webp&s=0745fdbb4f38cd6b4aa6c0104bb949b857496d8a

ht
tps://preview.redd.it/n8c7z5i5r72d1.png?width=5100&format=png&auto=webp&s=71660c9f380f4eb752fc854cbf66d0b6a5082472

http
s://preview.redd.it/zhfi8uf5r72d1.png?width=5100&format=png&auto=webp&s=769140b50f0755620be916931ba43199240f576b

I am o
pen to roles in AI/ML, Backend Full stack, SWE and Product roles, but cant seem to get interview calls, what am I doing 
wrong? I have been suggested to include the exact tech work I did to avoid looking inexperienced, and hence ended up add
ing a lot of tech jargon, could it be that? Please suggest me fixes. What am I doing wrong?  

```
---

     
 
all -  [ [11 YOE] I have Tech and Tech management experience in startups, but cant get an interview. ](https://www.reddit.com/r/EngineeringResumes/comments/1cyyiyu/11_yoe_i_have_tech_and_tech_management_experience/) , 2024-05-24-0911
```
I have been looking for AI/ML, Backend Full stack, SWE and Product roles but cant seem to get interview calls, what am I
 doing wrong? I have been suggested to include the exact tech work I did to avoid looking inexperienced, and hence ended
 up adding a lot of tech jargon. Please suggest me fixes.

https://preview.redd.it/n5cvga0go72d1.png?width=5100&format=p
ng&auto=webp&s=ee684cb4d88cc4569ad8c81fa643a928e3d80e21

https://preview.redd.it/4qkfva0go72d1.png?width=5100&format=png
&auto=webp&s=9c99b53b0164cfa1577f0d69544cb3c4058535d2

https://preview.redd.it/f7fy850go72d1.png?width=5100&format=png&a
uto=webp&s=69e881cfc736d8856a65fe6160c5ee6f23821ba7


```
---

     
 
all -  [ TimeGPT: Generative AI for Time Series  ](/r/ArtificialInteligence/comments/1cytvn5/generative_ai_for_time_series/) , 2024-05-24-0911
```

```
---

     
 
all -  [ ParentDocumentRetriever.add_document function with 'ids' parameter - can't fix an error ](https://www.reddit.com/r/LangChain/comments/1cytwsx/parentdocumentretrieveradd_document_function_with/) , 2024-05-24-0911
```
    from langchain.embeddings import OpenAIEmbeddings
    from langchain.retrievers import ParentDocumentRetriever
    f
rom langchain.schema import Document
    from langchain.storage import InMemoryStore
    from langchain.text_splitter im
port RecursiveCharacterTextSplitter
    from langchain.vectorstores.chroma import Chroma
    
    vectorstore = Chroma(

        collection_name='full_documents',
        embedding_function=OpenAIEmbeddings()
    )
    store = InMemoryStore(
)
    
    docs = [Document(page_content=txt, metadata={'id': id}) for txt, id in [('aaaaaa', 1), ('bbbbbb', 2)]]
    Pa
rentDocumentRetriever(
        vectorstore=vectorstore,
        docstore=store,
        id_key='id',
        parent_spli
tter=RecursiveCharacterTextSplitter(
            chunk_size = 2,
            chunk_overlap  = 0,
            length_func
tion = len,
            add_start_index = True,
        ),
        child_splitter=RecursiveCharacterTextSplitter(
      
      chunk_size = 1,
            chunk_overlap  = 0,
            length_function = len,
            add_start_index = T
rue,
        ),
    ).add_documents(docs,ids=[doc.metadata['id'] for doc in docs])from langchain.embeddings import OpenA
IEmbeddings
    from langchain.retrievers import ParentDocumentRetriever
    from langchain.schema import Document
    f
rom langchain.storage import InMemoryStore
    from langchain.text_splitter import RecursiveCharacterTextSplitter
    fr
om langchain.vectorstores.chroma import Chroma
    
    vectorstore = Chroma(
        collection_name='full_documents',

        embedding_function=OpenAIEmbeddings()
    )
    store = InMemoryStore()
    
    docs = [Document(page_content=t
xt, metadata={'id': id}) for txt, id in [('aaaaaa', 1), ('bbbbbb', 2)]]
    ParentDocumentRetriever(
        vectorstore
=vectorstore,
        docstore=store,
        id_key='id',
        parent_splitter=RecursiveCharacterTextSplitter(
     
       chunk_size = 2,
            chunk_overlap  = 0,
            length_function = len,
            add_start_index = 
True,
        ),
        child_splitter=RecursiveCharacterTextSplitter(
            chunk_size = 1,
            chunk_ov
erlap  = 0,
            length_function = len,
            add_start_index = True,
        ),
    ).add_documents(docs,i
ds=[doc.metadata['id'] for doc in docs])

The error :

    ValueError: Got uneven list of documents and ids. If `ids` is
 provided, should be same length as `documents`.

     

  
The size of documents list and ids list are nevertheless equ
al, i don't understand this error  
  

```
---

     
 
all -  [ How can I properly use tools within a chain in LangGraph? ](https://www.reddit.com/r/LangChain/comments/1cyt7uf/how_can_i_properly_use_tools_within_a_chain_in/) , 2024-05-24-0911
```
Hey guys! I'm trying to develop a chatbot that offers video games recommendations based on user input.  
Problem is, I'm
 stuck at the chain which objective is to use Tavily API tool to search for video games' titles that fit the user's crit
eria.

Here's what I've tried:

    # Game Title Search
    prompt = PromptTemplate(
        template='''You are part of
 a chatbot that provides personalized video game recommendations based on user preferences. \n
        Your task is to s
earch for the top 5 video games that match the user query. \n
        Only return the titles of the games. \n\n
    
   
     User Query: {query}''',
        input_variables=['query'],
    )
    
    game_title_search = prompt | llm.bind_too
ls(tools)
    
    QUERY = '''What games are similar to Skyrim?'''
    
    result = game_title_search.invoke({'query': 
QUERY})
    print(result)

Problem is, when I print result it gives me this instead of the response that I'm expecting (
which are the video games' titles:

`content='' additional_kwargs={'tool_calls': [{'id': 'call_xJGybVhCtBAYGHyNkEE04U1c'
, 'function': {'arguments': '{'query':'games similar to Skyrim'}', 'name': 'tavily_search_results_json'}, 'type': 'funct
ion'}]} response_metadata={'token_usage': {'completion_tokens': 21, 'prompt_tokens': 141, 'total_tokens': 162}, 'model_n
ame': 'gpt-3.5-turbo-1106', 'system_fingerprint': None, 'finish_reason': 'tool_calls', 'logprobs': None} id='run-c7c3309
4-2173-43d8-9e9a-319c80265f57-0' tool_calls=[{'name': 'tavily_search_results_json', 'args': {'query': 'games similar to 
Skyrim'}, 'id': 'call_xJGybVhCtBAYGHyNkEE04U1c'}]`

How can I solve this and use the tools alongside the ChatModel and t
he PromptTemplate to achieve what I want?
```
---

     
 
all -  [ Does unifying the infrastructure code and the application code in a single interface contribute to t ](https://www.reddit.com/r/devops/comments/1cyru9j/does_unifying_the_infrastructure_code_and_the/) , 2024-05-24-0911
```
Hey everyone! I'm currently developing a tool called [Pluto](https://github.com/pluto-lang/pluto), which offers a unifie
d programming interface that enables developers to seamlessly integrate infrastructure code with application code. I bel
ieve this approach could revolutionize the way we develop cloud-native applications, making the process more efficient a
nd streamlined. I'm curious to hear your thoughts on this matter. Do you think this is a step in the right direction for
 cloud-native app development? Your input would be greatly appreciated!

For a real-world example of how Pluto can be ut
ilized, I recommend checking out this article: [How to Bridge the Last Mile in LangChain Application Development](https:
//pluto-lang.vercel.app/blogs/240515-develop-ai-app-in-new-paradigm). It demonstrates how Pluto can be used to simplify 
the development process of a LangChain app.

Thanks in advance for your feedback!
```
---

     
 
all -  [ Does unifying the infrastructure code and the application code in a single interface contribute to t ](https://www.reddit.com/r/u_Zheng_SJ/comments/1cyrrfh/does_unifying_the_infrastructure_code_and_the/) , 2024-05-24-0911
```
Hey everyone! I'm currently developing a tool called [Pluto](https://github.com/pluto-lang/pluto), which offers a unifie
d programming interface that enables developers to seamlessly integrate infrastructure code with application code. I bel
ieve this approach could revolutionize the way we develop cloud-native applications, making the process more efficient a
nd streamlined. I'm curious to hear your thoughts on this matter. Do you think this is a step in the right direction for
 cloud-native app development? Your input would be greatly appreciated!

For a real-world example of how Pluto can be ut
ilized, I recommend checking out this article: [How to Bridge the Last Mile in LangChain Application Development](https:
//blog.stackademic.com/how-to-bridge-the-last-mile-in-langchain-application-development-e4734ca07169). It demonstrates h
ow Pluto can be used to simplify the development process of a LangChain app.

Thanks in advance for your feedback!
```
---

     
 
all -  [ Parsing solutions for PDF ](https://www.reddit.com/r/LangChain/comments/1cyplp8/parsing_solutions_for_pdf/) , 2024-05-24-0911
```
Been struggling with parsing pdf with complex layout, table, imagines.

The option that I am testing is multi modal vect
or, based on unstructured library for pdf extraction. 

I recently discovered llamaparse proprietary solution. Excluding
 the facts that isn't open source and limited for commercial use. Would it perform better then the unstructured approach
 for parsing?


```
---

     
 
all -  [ What are some ways to enforce structured outputs from LLMs not in your control beyond basic promptin ](https://www.reddit.com/r/LangChain/comments/1cyp7ij/what_are_some_ways_to_enforce_structured_outputs/) , 2024-05-24-0911
```
Hi!

I'm currently facing this issue of trying to get an XML out of a model and I use that XML structure to extract and 
format a document that I generate but, no matter how I prompt the model, or even, using different calls generate the ans
wer and to structure it into the required format, sometimes going through different stages of structuring (like first ju
st bullet points, then try to only put stuff into a basic XML format before going into nested.), it still sometimes gene
rate an answer that's not structured.

I included retries on those calls hoping that the model in its second generation 
would structure the output correctly but often this doesn't work.

I was wondering how the community handles this issue 
or if there are creative ways you stumbled upon that deal well with it.

I have seen in the past some libraries that for
ce the generation in some kind of way like the grammars from llama-cpp, or outlines. Maybe there was guidance as well. B
ut I don't think they work with LLMs from providers. I'm facing this problem with mistral-large.


```
---

     
 
all -  [ Need help and knowledge in deployment ](https://www.reddit.com/r/AWS_cloud/comments/1cyp7c6/need_help_and_knowledge_in_deployment/) , 2024-05-24-0911
```
Hi all,

New user of aws here.

I have a python script of an LLM model using bedrock, langchain libraries and streamlit 
for frontend along with the requirements.txt file. I have saved it jnto a repository in CodeCommit and I am aware of two
 different ways to deploy it.

1). The CI/CD pipeline format using the respective services CodeCommit, CodeBuild, CodeDe
ploy, CodePipeline etc. but the problem is it is more suitable for a node.js or proper website project with multiple fil
es instead of a single python script. I found the portion of creating an appspec.yml or buildspec.yml file very complex 
for a single python script and I was not able to find any tutorial on how to do it as well.

2). The 2nd method is to wr
ite some commands on the terminal of an amazon linux machine on the EC2 server instance, I have successfully deployed a 
model using these method on the provided public IP but the problem is if I commit changes in the repository, it does not
 reflect in the EC2 instance even after rebooting the instance. the only way to make the changes reflect is to terminate
 the instance and create a new one, which is very time-consuming.

I would like to know if anyone can guide me in using 
the first method for a single python script or can help in having the changes reflect in the ec2 server as that is what 
will make ec2 method of deployment a CI/CD method.
```
---

     
 
all -  [ Need help in deployment on AWS ](https://www.reddit.com/r/aws/comments/1cyp6ce/need_help_in_deployment_on_aws/) , 2024-05-24-0911
```
Hi all,

New user of aws here.

I have a python script of an LLM model using bedrock, langchain libraries and streamlit 
for frontend along with the requirements.txt file. I have saved it jnto a repository in CodeCommit and I am aware of two
 different ways to deploy it.

1). The CI/CD pipeline format using the respective services CodeCommit, CodeBuild, CodeDe
ploy, CodePipeline etc.  but the problem is it is more suitable for a node.js or proper website project with multiple fi
les instead of a single python script. I found the portion of creating an appspec.yml or buildspec.yml file very complex
 for a single python script and I was not able to find any tutorial on how to do it as well.

2).  The 2nd method is to 
write some commands on the terminal of an amazon linux machine on the EC2 server instance, I have successfully deployed 
a model using these method on the provided public IP but the problem is if I commit changes in the repository, it does n
ot reflect in the EC2 instance even after rebooting the instance. the only way to make the changes reflect is to termina
te the instance  and create a new one, which is very time-consuming.

I would like to know if anyone can guide me in usi
ng the first method for a single python script or can help in having the  changes reflect in the ec2 server as that is w
hat will make ec2 method of deployment a CI/CD method.
```
---

     
 
all -  [ How can I get the csv_agent to return the complete results from its Observation? ](https://www.reddit.com/r/LangChain/comments/1cyoeho/how_can_i_get_the_csv_agent_to_return_the/) , 2024-05-24-0911
```
I'm using create\_csv\_agent to get a csv parsing agent to analyze and return a list of items that meets the criteria. T
he agent handles the questions fine and I can see the correct results printed out in its Observations. However it doesn'
t include the list of items in the final output. How can I get around this?
```
---

     
 
all -  [ I'm new to this and I need help for my RAG ](https://www.reddit.com/r/LangChain/comments/1cynhl3/im_new_to_this_and_i_need_help_for_my_rag/) , 2024-05-24-0911
```
Hey I am doing an internship and my boss asked me to build a RAG that can read financial documents (pdf) and create a LL
M that, with a query, answers based on these documents. I was using BGE as the embedding model and ollama with llama2 fo
r the LLM. My problem is that I was using google collab with the free GPU but once it reaches the limit, I can't keep cr
eating the embeddings. Is there any FREE solution for this? Thank you and sorry for my inexperience.
```
---

     
 
all -  [ For those struggling with API function calls ](https://www.reddit.com/r/LangChain/comments/1cyn34y/for_those_struggling_with_api_function_calls/) , 2024-05-24-0911
```
What worked for me was to create small modular functions out of one big function with different parameters. I broke down
 my API for the bot to use into smaller, modular endpoints with maximum of two parameters each. 

I have been able to us
e gpt-3.5 to get satisfactory outputs without fails. 
```
---

     
 
all -  [ Help Needed: To find total number of results ?  ](https://www.reddit.com/r/LangChain/comments/1cylb81/help_needed_to_find_total_number_of_results/) , 2024-05-24-0911
```
Hi Guys,  
I am exploring LangChain, and stuck at one issue, Needed your help!!

I am trying to get total number of empt
y parking spots available in csv, but I see we can only define k value in retriever,

Is there a way to ignore k value a
nd give full matching result ?

Here is my code: [Langchain/apps/find\_parking/parking\_spots.ipynb at main · DastanIqba
l/Langchain · GitHub](https://github.com/DastanIqbal/Langchain/blob/main/apps/find_parking/parking_spots.ipynb)

Thanks
```
---

     
 
all -  [ Simple choice selection ](https://www.reddit.com/r/LangChain/comments/1cykpbu/simple_choice_selection/) , 2024-05-24-0911
```
Looking to return only a specific choice with langchain using an ollama model and couldn't get the langchoice example to
 work. 
For example, How would I classify a bank transaction description if the only possible classification choices to 
choose from are: taxes, transfer, or payment?
```
---

     
 
all -  [ Best stack for RAG? ](https://www.reddit.com/r/LangChain/comments/1cyjfap/best_stack_for_rag/) , 2024-05-24-0911
```
We’re building a RAG based application which works on internal documents. We’re experimenting with OpenAI for embedding 
models, Milvus (Zilliz cloud) for embedding storage and similarity search, Postgres for all other data and AWS for hosti
ng.

Our main priorities are:
- being fast to market
- above average performance
- costs that don’t scale exponentially 
with scale
- being scalable so we don’t have to refactor all of the code, if we achieve any scale
```
---

     
 
all -  [ What features do you want in the local AI systems? ](https://github.com/yukiarimo/yuna-ai/issues/91) , 2024-05-24-0911
```
Hello guys! I’m a creator of Yuna AI. I need some ideas and suggestions on what we can implement. Here’s our list:

# Yu
na AI Current Project Status:

## What's Working in Yuna:

- [x] User Auth System
- [x] Multiple Chat Histories
- [x] In
dividual Message Deleting
- [x] History Editing
- [x] Full History Management (Import/Export, Edit)
- [x] Custom Message
s
- [x] Audio Transcription
- [x] Video In-Audio Transcription
- [x] Web Search
- [x] Web Q&A (a.k.a LangChain)
- [x] Im
age Transcription and Image Q&A
- [x] Kanojo Character Customization
- [x] Prompt Customization
- [x] Kanojo and Prompt 
Template Export/Import System
- [x] Audio Calls with TTS feedback
- [x] Modes for native and fast inferences. Llama CPP 
+ LM Studio and Siri TTS + Coqui TTS
- [x] Basic Diffusion Single File Inference
- [x] Landing Page
- [x] Dark Mode
- [x
] Gesture Control (alpha)

## What's NOT Working in Yuna (but will be in the future):

- [ ] 2D/3D Taking Head Animation
s for Video Calls
- [ ] Full LangChain Support for PDF, Audio, and Video Q&A
- [ ] RP LSTM
- [ ] Kanojo Connect with Mul
tiple Kanojo in a Single Chat
- [ ] Himitsu Copilot
- [ ] Himitsu Copiloting System
- [ ] Himitsu Actions
- [ ] History 
Collections
- [ ] Advanced Web Search
- [ ] Saved Messages (Notes)
- [ ] Pseudo APIs
- [ ] Light Mode and Automatic Mode

- [ ] Browser Extension
- [ ] Server Config Saver Per User
- [ ] Explore News Tab
- [ ] WebGPU PWA Mobile WASM
- [ ] Mo
del WebUI Manager
- [ ] Offline Viewer
- [ ] YUI (Yuna's Unified UI)
- [ ] Yuna AI Creator Studio
- [ ] Naked Mode
- [ ]
 Training
- [ ] Additional Advanced Models for Art, Uta, and More
- [ ] Emotional Profile
- [ ] Settings
- [ ] Multiling
ual Chats
- [ ] LoRAs
- [ ] Publish Share Link

Feel free to share everything you can think of, even if it exists in any
 other project!
```
---

     
 
all -  [ Need Help Understanding Why My Language Model Chain Isn't Producing Results ](https://www.reddit.com/r/LangChain/comments/1cyhm4y/need_help_understanding_why_my_language_model/) , 2024-05-24-0911
```
I'm working on a project that involves using a language model chain to process questions and generate responses. However
, I've encountered an issue where the chain seems to get stuck at the invocation stage without producing any results.

*
*Background:**

* I'm using a Python script that involves various components such as document loaders, embeddings, text 
splitters, vector stores, retrievers, prompts, parsers, and language models.
* The script is designed to load a PDF docu
ment, split it into chunks, add the chunks to a vector database, initialize a language model, and then retrieve relevant
 information based on input questions.

**Problem:**

* Despite setting up the chain correctly and providing a question 
to the system, it seems to get stuck at the invocation stage without producing any results.
* I've checked the logs, and
 everything seems to be initialized and processed correctly up to the invocation step.

**Code:**

    from langchain_co
mmunity.document_loaders import UnstructuredPDFLoader
    from langchain_community.document_loaders import OnlinePDFLoad
er
    from langchain_community.embeddings import OllamaEmbeddings
    from langchain_text_splitters import RecursiveCha
racterTextSplitter
    from langchain_community.vectorstores import Chroma
    from langchain.prompts import ChatPromptT
emplate, PromptTemplate
    from langchain_core.output_parsers import StrOutputParser
    from langchain_community.chat_
models import ChatOllama
    from langchain_core.runnables import RunnablePassthrough
    from langchain_core.tracers im
port ConsoleCallbackHandler
    from langchain.retrievers.multi_query import MultiQueryRetriever
    import asyncio
    

    # Use raw string notation for the file path
    local_path = r'C:/Users/User/zven/WEF_The_Global_Cooperation_Barome
ter_2024.pdf'
    
    # Load local PDF file
    if local_path:
        try:
            loader = UnstructuredPDFLoader(
file_path=local_path)
            data = loader.load()
            print('PDF loaded successfully.')
        except Exce
ption as e:
            print(f'Error loading PDF: {e}')
            data = None
    else:
        print('Upload a PDF f
ile')
        data = None
    
    if data:
        # Split and chunk text
        text_splitter = RecursiveCharacterTex
tSplitter(chunk_size=7500, chunk_overlap=100)
        chunks = text_splitter.split_documents(data)
        print(f'Docum
ent split into {len(chunks)} chunks.')
        print(data[0].page_content)
        
        # Add to vector database
   
     try:
            vector_db = Chroma.from_documents(
                documents=chunks, 
                embedding=Ol
lamaEmbeddings(model='nomic-embed-text', show_progress=True),
                collection_name='local-rag'
            )

            print('Chunks added to vector database.')
        except Exception as e:
            print(f'Error adding ch
unks to vector database: {e}')
    
        # Initialize LLM from Ollama
        local_model = 'Mistral'
        try:
  
          llm = ChatOllama(model=local_model)
            print('LLM initialized successfully.')
        except Exceptio
n as e:
            print(f'Error initializing LLM: {e}')
    
        # Define query prompt template
        QUERY_PROM
PT = PromptTemplate(
            input_variables=['question'],
            template='''You are an AI language model assi
stant. Your task is to generate five
            different versions of the given user question to retrieve relevant docu
ments from
            a vector database. By generating multiple perspectives on the user question, your
            goa
l is to help the user overcome some of the limitations of the distance-based
            similarity search. Provide thes
e alternative questions separated by newlines.
            Original question: {question}'''
        )
    
        # Ini
tialize retriever
        try:
            retriever = MultiQueryRetriever.from_llm(
                vector_db.as_retrie
ver(), 
                llm,
                prompt=QUERY_PROMPT
            )
            print('Retriever initialized 
successfully.')
        except Exception as e:
            print(f'Error initializing retriever: {e}')
    
        # De
fine RAG prompt template
        template = '''Answer the question based ONLY on the following context:
        {context
}
        Question: {question}
        '''
        print('Template: ', template)
        prompt = ChatPromptTemplate.fro
m_template(template)
        print('Prompt: ', prompt)
    
        chain = (
            {'context': retriever, 'questi
on': RunnablePassthrough()}
            | prompt
            | llm
            | StrOutputParser()
        )
        pri
nt(chain)
        # Print the chain setup
        print('Chain setup completed.')
    
    async def run_chain():
      
  try:
            print('Invoking chain...')
            # Invoke the chain with a question
            result = await 
chain.ainvoke(
                {'question': 'What are the 5 pillars of global cooperation?'},
                config={'c
allbacks': [ConsoleCallbackHandler()]}  # 30 seconds timeout
            )
            print('Chain invoked successfully
.')
            print('Result:', result)
            # Print the answer if it exists
            if 'answer' in result:

                print('Answer:', result['answer'])
        except asyncio.TimeoutError:
            print('Chain invocat
ion timed out.')
        except Exception as e:
            print(f'Error invoking chain: {e}')
    
    # Run the chain

    asyncio.run(run_chain())
    
    # Delete all collections in the db
    vector_db.delete_collection()
    

>

Out
put when I Run it:  
OllamaEmbeddings: 100%|████████████████████████████████████████████████████████████████| 11/11 \[05
:16<00:00, 28.77s/it\]

Chunks added to vector database.

LLM initialized successfully.

Retriever initialized successfu
lly.

Template:  Answer the question based ONLY on the following context:

{context}

Question: {question}

Prompt:  inp
ut\_variables=\['context', 'question'\] messages=\[HumanMessagePromptTemplate(prompt=PromptTemplate(input\_variables=\['
context', 'question'\], template='Answer the question based ONLY on the following context:\\n    {context}\\n    Questio
n: {question}\\n    '))\]

first={

context: MultiQueryRetriever(retriever=VectorStoreRetriever(tags=\['Chroma', 'Ollama
Embeddings'\], vectorstore=<langchain\_community.vectorstores.chroma.Chroma object at 0x0000016DB7450390>), llm\_chain=L
LMChain(prompt=PromptTemplate(input\_variables=\['question'\], template='You are an AI language model assistant. Your ta
sk is to generate five\\n        different versions of the given user question to retrieve relevant documents from\\n   
     a vector database. By generating multiple perspectives on the user question, your\\n        goal is to help the use
r overcome some of the limitations of the distance-based\\n        similarity search. Provide these alternative question
s separated by newlines.\\n        Original question: {question}'), llm=ChatOllama(model='Mistral'), output\_parser=Line
ListOutputParser())),

question: RunnablePassthrough()

} middle=\[ChatPromptTemplate(input\_variables=\['context', 'que
stion'\], messages=\[HumanMessagePromptTemplate(prompt=PromptTemplate(input\_variables=\['context', 'question'\], templa
te='Answer the question based ONLY on the following context:\\n    {context}\\n    Question: {question}\\n    '))\]), Ch
atOllama(model='Mistral')\] last=StrOutputParser()

Chain setup completed.

Invoking chain...

\[chain/start\] \[chain:R
unnableSequence\] Entering Chain run with input:

{

'question': 'What are the 5 pillars of global cooperation?'

}

\[c
hain/start\] \[chain:RunnableSequence > chain:RunnableParallel<context,question>\] Entering Chain run with input:

{

'q
uestion': 'What are the 5 pillars of global cooperation?'

}

\[chain/start\] \[chain:RunnableSequence > chain:RunnableP
arallel<context,question> > chain:RunnablePassthrough\] Entering Chain run with input:

{

'question': 'What are the 5 p
illars of global cooperation?'

}

\[chain/start\] \[chain:RunnableSequence > chain:RunnableParallel<context,question> >
 retriever:Retriever > chain:LLMChain\] Entering Chain run with input:

{

'question': {

'question': 'What are the 5 pi
llars of global cooperation?'

}

}\[chain/end\] \[chain:RunnableSequence > chain:RunnableParallel<context,question> > c
hain:RunnablePassthrough\] \[16ms\] Exiting Chain run with output:

{

'question': 'What are the 5 pillars of global coo
peration?'

}

\[llm/start\] \[chain:RunnableSequence > chain:RunnableParallel<context,question> > retriever:Retriever >
 chain:LLMChain > llm:ChatOllama\] Entering LLM run with input:

{

'prompts': \[

'Human: You are an AI language model 
assistant. Your task is to generate five\\n        different versions of the given user question to retrieve relevant do
cuments from\\n        a vector database. By generating multiple perspectives on the user question, your\\n        goal 
is to help the user overcome some of the limitations of the distance-based\\n        similarity search. Provide these al
ternative questions separated by newlines.\\n        Original question: {'question': 'What are the 5 pillars of global c
ooperation?'}'

\]

}
```
---

     
 
all -  [ Problems with json and enum parser ](https://www.reddit.com/r/LangChain/comments/1cyh8zq/problems_with_json_and_enum_parser/) , 2024-05-24-0911
```
Langchain's enum and json parser just dont work and I can't figure out why. For example, here is my code below:

https:/
/preview.redd.it/smzg0411z22d1.png?width=741&format=png&auto=webp&s=26b6ef00927afc4a1a9e6c8e6bf297dfea96d56f

Where pred
iction is an enum with increase, decrease or no change. When I try it, I get this error:

https://preview.redd.it/3lp1jv
g6z22d1.png?width=1451&format=png&auto=webp&s=b41bdf522394561581dc924abe167898aa19edeb

Which gives the correct answer a
s decreased, but not as an enum. The same happens when I try this with the json parser, it adds unneccessary text around
 the dictionary so langchain doesnt read the output as a dictionary. Is there a fix for this?
```
---

     
 
all -  [ A question regarding ](https://www.reddit.com/r/LangChain/comments/1cycid7/a_question_regarding/) , 2024-05-24-0911
```
I have a use case where I have bunch of notes for a college class and I want to generate flash cards for them. Now I kno
w RAG is used to fetch most closest file from database and answer based on that, however in my case, all the notes shoul
d be loaded. So would RAG be applicable in this case. I can also just load all data in but that would probably run out o
f tokens quickly
```
---

     
 
all -  [ ChatCompletionRequest in AgentExecutor ](https://www.reddit.com/r/LangChain/comments/1cy9zxh/chatcompletionrequest_in_agentexecutor/) , 2024-05-24-0911
```
I was checking out the function calling capability of the new Mistral model and was wondering how to integrate this into
 a ReAct agent flow that uses AgentExecutor. 

[https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3](https://huggi
ngface.co/mistralai/Mistral-7B-Instruct-v0.3)

  
Anyone got any hints? 
```
---

     
 
all -  [ React libraries for conversational AI experiences ](https://www.reddit.com/r/react/comments/1cy8807/react_libraries_for_conversational_ai_experiences/) , 2024-05-24-0911
```
Hello everyone.

I want to add to an existing react application chat on the side which allows the user to interact with 
an agent, is there a library which assists with building AI Chat experiences?

I really like how bing chat streams text 
with references and other suggestions.

I want to render responses I get from llamaindex/langchain/openai in a similar f
ashion, would I have to rebuild this from scratch or is there some react/js libraries I can build over?

Thanks.

https:
//preview.redd.it/yka89xzty02d1.png?width=1756&format=png&auto=webp&s=89d86db4727395a02f19dc00b0ea3b695a5283bd


```
---

     
 
all -  [ Testing And Evaluating LLM RAG Systems ](https://www.reddit.com/r/LangChain/comments/1cy83us/testing_and_evaluating_llm_rag_systems/) , 2024-05-24-0911
```
Hello everyone, 

I am an engineering student currently doing my end of studies internship, and I am working on a projec
t that involves RAG system using LLM for my company and my mission now is to evaluate and test different parameters in t
he process of retrieving and generating like evaluating the embeddings , the different LLM models etc, to finally choose
 what's best to use. So, while doing my researches I found Langsmith and few others I want to know if some of you used o
ne of these platforms and how was your experience and which one do you prefer and why .

Your feedback will greatly assi
st me in my work and research so if you have any information feel free to share it .

THANK YOU
```
---

     
 
all -  [ Any way to make a Chatbot that does EDA on a large dataframe similar to Pandas Dataframe Agent.  ](https://www.reddit.com/r/LangChain/comments/1cy29kb/any_way_to_make_a_chatbot_that_does_eda_on_a/) , 2024-05-24-0911
```
As the title suggests I want to perform EDA using Langchain on a large dataframe. Im currently using Pandas Dataframe Ag
ent , however it is not that efficent when using with large datasets. Can someone please suggest an alternative that wor
ks well. Thankyou 
```
---

     
 
all -  [ Career Advice for Software Development + Gen AI + Copywriting skills ](https://www.reddit.com/r/LangChain/comments/1cy24vw/career_advice_for_software_development_gen_ai/) , 2024-05-24-0911
```
I'm a software developer who's learned about Gen AI stuff (Langchain, LLM, RAG, Agents,etc), and copywriting. Now I'm co
mbining all these skills and looking for career advice or anyone going through the same thing and wants to connect
```
---

     
 
all -  [ I want to build a graph rag with document browsing capability of the PDF its referencing from.  ](https://www.reddit.com/r/LangChain/comments/1cy1w8q/i_want_to_build_a_graph_rag_with_document/) , 2024-05-24-0911
```
I have 100 PDFs that I need to index and make a report of every single week. I need a rag to help me get the info from t
he PDFs in a neat manner but also pull up the images and the PDF associated with the query. I needed the text to be high
lighted as well and the pg numbers. 

can someone please guide me with the stack? im thinking langchain and memgraph for
 DB but more tools and options and stack? thanks!
```
---

     
 
all -  [ JSON Output Parser Error Please help! ](https://www.reddit.com/r/LangChain/comments/1cxxvvc/json_output_parser_error_please_help/) , 2024-05-24-0911
```
I want to parse the LLM output to a particular JSON Schema But I am getting this error

    {
    'name': 'ValidationErr
or',
    'message': '1 validation error for Generation
    text
      str type expected (type=type_error.str)',
    'sta
ck': '---------------------------------------------------------------------------
    ValidationError                   
        Traceback (most recent call last)
    /Users/pratham/LLMApi/pd_agent/ExcelParser.py in line 1
    ----> <a href=
'file:///Users/pratham/LLMApi/pd_agent/ExcelParser.py?line=167'>168</a> top_rows = get_top_rows(doc_df, ChatOpenAI(model
=\'gpt-3.5-turbo\', temperature=0))
          <a href='file:///Users/pratham/LLMApi/pd_agent/ExcelParser.py?line=168'>16
9</a> top_rows
    
    /Users/pratham/LLMApi/pd_agent/ExcelParser.py in line 13, in get_top_rows(df, llm)
         <a h
ref='file:///Users/pratham/LLMApi/pd_agent/ExcelParser.py?line=45'>46</a> print(parser.get_format_instructions())
      
   <a href='file:///Users/pratham/LLMApi/pd_agent/ExcelParser.py?line=46'>47</a> chain = prompt | df_agent | parser
    
---> <a href='file:///Users/pratham/LLMApi/pd_agent/ExcelParser.py?line=47'>48</a> json_output = chain.invoke(
         
<a href='file:///Users/pratham/LLMApi/pd_agent/ExcelParser.py?line=48'>49</a>     {
         <a href='file:///Users/prat
ham/LLMApi/pd_agent/ExcelParser.py?line=49'>50</a>         \'format_instructions\': parser.get_format_instructions()
   
      <a href='file:///Users/pratham/LLMApi/pd_agent/ExcelParser.py?line=50'>51</a>     }
         <a href='file:///User
s/pratham/LLMApi/pd_agent/ExcelParser.py?line=51'>52</a> )
         <a href='file:///Users/pratham/LLMApi/pd_agent/Excel
Parser.py?line=52'>53</a> return json_output[\'number_of_top_rows\']
    
    File ~/LLMApi/venv/lib/python3.12/site-pac
kages/langchain_core/runnables/base.py:2499, in RunnableSequence.invoke(self, input, config)
       <a href='file:///Use
rs/pratham/LLMApi/venv/lib/python3.12/site-packages/langchain_core/runnables/base.py?line=2496'>2497</a> try:
       <a 
href='file:///Users/pratham/LLMApi/venv/lib/python3.12/site-packages/langchain_core/runnables/base.py?line=2497'>2498</a
>     for i, step in enumerate(self.steps):
    -> <a href='file:///Users/pratham/LLMApi/venv/lib/python3.12/site-packag
es/langchain_core/runnables/base.py?line=2498'>2499</a>         input = step.invoke(
       <a href='file:///Users/prath
am/LLMApi/venv/lib/python3.12/site-packages/langchain_core/runnables/base.py?line=2499'>2500</a>             input,
    
   <a href='file:///Users/pratham/LLMApi/venv/lib/python3.12/site-packages/langchain_core/runnables/base.py?line=2500'>2
501</a>             # mark each step as a child run
       <a href='file:///Users/pratham/LLMApi/venv/lib/python3.12/sit
e-packages/langchain_core/runnables/base.py?line=2501'>2502</a>             patch_config(
       <a href='file:///Users/
pratham/LLMApi/venv/lib/python3.12/site-packages/langchain_core/runnables/base.py?line=2502'>2503</a>                 co
nfig, callbacks=run_manager.get_child(f\'seq:step:{i+1}\')
       <a href='file:///Users/pratham/LLMApi/venv/lib/python3
.12/site-packages/langchain_core/runnables/base.py?line=2503'>2504</a>             ),
       <a href='file:///Users/prat
ham/LLMApi/venv/lib/python3.12/site-packages/langchain_core/runnables/base.py?line=2504'>2505</a>         )
       <a hr
ef='file:///Users/pratham/LLMApi/venv/lib/python3.12/site-packages/langchain_core/runnables/base.py?line=2505'>2506</a> 
# finish the root run
       <a href='file:///Users/pratham/LLMApi/venv/lib/python3.12/site-packages/langchain_core/runn
ables/base.py?line=2506'>2507</a> except BaseException as e:
    
    File ~/LLMApi/venv/lib/python3.12/site-packages/la
ngchain_core/output_parsers/base.py:178, in BaseOutputParser.invoke(self, input, config)
        <a href='file:///Users/
pratham/LLMApi/venv/lib/python3.12/site-packages/langchain_core/output_parsers/base.py?line=168'>169</a>     return self
._call_with_config(
        <a href='file:///Users/pratham/LLMApi/venv/lib/python3.12/site-packages/langchain_core/outpu
t_parsers/base.py?line=169'>170</a>         lambda inner_input: self.parse_result(
        <a href='file:///Users/pratha
m/LLMApi/venv/lib/python3.12/site-packages/langchain_core/output_parsers/base.py?line=170'>171</a>             [ChatGene
ration(message=inner_input)]
       (...)
        <a href='file:///Users/pratham/LLMApi/venv/lib/python3.12/site-package
s/langchain_core/output_parsers/base.py?line=174'>175</a>         run_type=\'parser\',
        <a href='file:///Users/pr
atham/LLMApi/venv/lib/python3.12/site-packages/langchain_core/output_parsers/base.py?line=175'>176</a>     )
        <a 
href='file:///Users/pratham/LLMApi/venv/lib/python3.12/site-packages/langchain_core/output_parsers/base.py?line=176'>177
</a> else:
    --> <a href='file:///Users/pratham/LLMApi/venv/lib/python3.12/site-packages/langchain_core/output_parsers
/base.py?line=177'>178</a>     return self._call_with_config(
        <a href='file:///Users/pratham/LLMApi/venv/lib/pyt
hon3.12/site-packages/langchain_core/output_parsers/base.py?line=178'>179</a>         lambda inner_input: self.parse_res
ult([Generation(text=inner_input)]),
        <a href='file:///Users/pratham/LLMApi/venv/lib/python3.12/site-packages/lan
gchain_core/output_parsers/base.py?line=179'>180</a>         input,
        <a href='file:///Users/pratham/LLMApi/venv/l
ib/python3.12/site-packages/langchain_core/output_parsers/base.py?line=180'>181</a>         config,
        <a href='fil
e:///Users/pratham/LLMApi/venv/lib/python3.12/site-packages/langchain_core/output_parsers/base.py?line=181'>182</a>     
    run_type=\'parser\',
        <a href='file:///Users/pratham/LLMApi/venv/lib/python3.12/site-packages/langchain_core/
output_parsers/base.py?line=182'>183</a>     )
    
    File ~/LLMApi/venv/lib/python3.12/site-packages/langchain_core/r
unnables/base.py:1626, in Runnable._call_with_config(self, func, input, config, run_type, **kwargs)
       <a href='file
:///Users/pratham/LLMApi/venv/lib/python3.12/site-packages/langchain_core/runnables/base.py?line=1621'>1622</a>     cont
ext = copy_context()
       <a href='file:///Users/pratham/LLMApi/venv/lib/python3.12/site-packages/langchain_core/runna
bles/base.py?line=1622'>1623</a>     context.run(var_child_runnable_config.set, child_config)
       <a href='file:///Us
ers/pratham/LLMApi/venv/lib/python3.12/site-packages/langchain_core/runnables/base.py?line=1623'>1624</a>     output = c
ast(
       <a href='file:///Users/pratham/LLMApi/venv/lib/python3.12/site-packages/langchain_core/runnables/base.py?lin
e=1624'>1625</a>         Output,
    -> <a href='file:///Users/pratham/LLMApi/venv/lib/python3.12/site-packages/langchai
n_core/runnables/base.py?line=1625'>1626</a>         context.run(
       <a href='file:///Users/pratham/LLMApi/venv/lib/
python3.12/site-packages/langchain_core/runnables/base.py?line=1626'>1627</a>             call_func_with_variable_args, 
 # type: ignore[arg-type]
       <a href='file:///Users/pratham/LLMApi/venv/lib/python3.12/site-packages/langchain_core/
runnables/base.py?line=1627'>1628</a>             func,  # type: ignore[arg-type]
       <a href='file:///Users/pratham/
LLMApi/venv/lib/python3.12/site-packages/langchain_core/runnables/base.py?line=1628'>1629</a>             input,  # type
: ignore[arg-type]
       <a href='file:///Users/pratham/LLMApi/venv/lib/python3.12/site-packages/langchain_core/runnabl
es/base.py?line=1629'>1630</a>             config,
       <a href='file:///Users/pratham/LLMApi/venv/lib/python3.12/site
-packages/langchain_core/runnables/base.py?line=1630'>1631</a>             run_manager,
       <a href='file:///Users/pr
atham/LLMApi/venv/lib/python3.12/site-packages/langchain_core/runnables/base.py?line=1631'>1632</a>             **kwargs
,
       <a href='file:///Users/pratham/LLMApi/venv/lib/python3.12/site-packages/langchain_core/runnables/base.py?line=1
632'>1633</a>         ),
       <a href='file:///Users/pratham/LLMApi/venv/lib/python3.12/site-packages/langchain_core/r
unnables/base.py?line=1633'>1634</a>     )
       <a href='file:///Users/pratham/LLMApi/venv/lib/python3.12/site-package
s/langchain_core/runnables/base.py?line=1634'>1635</a> except BaseException as e:
       <a href='file:///Users/pratham/
LLMApi/venv/lib/python3.12/site-packages/langchain_core/runnables/base.py?line=1635'>1636</a>     run_manager.on_chain_e
rror(e)
    
    File ~/LLMApi/venv/lib/python3.12/site-packages/langchain_core/runnables/config.py:347, in call_func_wi
th_variable_args(func, input, config, run_manager, **kwargs)
        <a href='file:///Users/pratham/LLMApi/venv/lib/pyth
on3.12/site-packages/langchain_core/runnables/config.py?line=344'>345</a> if run_manager is not None and accepts_run_man
ager(func):
        <a href='file:///Users/pratham/LLMApi/venv/lib/python3.12/site-packages/langchain_core/runnables/con
fig.py?line=345'>346</a>     kwargs[\'run_manager\'] = run_manager
    --> <a href='file:///Users/pratham/LLMApi/venv/li
b/python3.12/site-packages/langchain_core/runnables/config.py?line=346'>347</a> return func(input, **kwargs)
    
    Fi
le ~/LLMApi/venv/lib/python3.12/site-packages/langchain_core/output_parsers/base.py:179, in BaseOutputParser.invoke.<loc
als>.<lambda>(inner_input)
        <a href='file:///Users/pratham/LLMApi/venv/lib/python3.12/site-packages/langchain_cor
e/output_parsers/base.py?line=168'>169</a>     return self._call_with_config(
        <a href='file:///Users/pratham/LLM
Api/venv/lib/python3.12/site-packages/langchain_core/output_parsers/base.py?line=169'>170</a>         lambda inner_input
: self.parse_result(
        <a href='file:///Users/pratham/LLMApi/venv/lib/python3.12/site-packages/langchain_core/outp
ut_parsers/base.py?line=170'>171</a>             [ChatGeneration(message=inner_input)]
       (...)
        <a href='fil
e:///Users/pratham/LLMApi/venv/lib/python3.12/site-packages/langchain_core/output_parsers/base.py?line=174'>175</a>     
    run_type=\'parser\',
        <a href='file:///Users/pratham/LLMApi/venv/lib/python3.12/site-packages/langchain_core/
output_parsers/base.py?line=175'>176</a>     )
        <a href='file:///Users/pratham/LLMApi/venv/lib/python3.12/site-pa
ckages/langchain_core/output_parsers/base.py?line=176'>177</a> else:
        <a href='file:///Users/pratham/LLMApi/venv/
lib/python3.12/site-packages/langchain_core/output_parsers/base.py?line=177'>178</a>     return self._call_with_config(

    --> <a href='file:///Users/pratham/LLMApi/venv/lib/python3.12/site-packages/langchain_core/output_parsers/base.py?li
ne=178'>179</a>         lambda inner_input: self.parse_result([Generation(text=inner_input)]),
        <a href='file:///
Users/pratham/LLMApi/venv/lib/python3.12/site-packages/langchain_core/output_parsers/base.py?line=179'>180</a>         i
nput,
        <a href='file:///Users/pratham/LLMApi/venv/lib/python3.12/site-packages/langchain_core/output_parsers/base
.py?line=180'>181</a>         config,
        <a href='file:///Users/pratham/LLMApi/venv/lib/python3.12/site-packages/la
ngchain_core/output_parsers/base.py?line=181'>182</a>         run_type=\'parser\',
        <a href='file:///Users/pratha
m/LLMApi/venv/lib/python3.12/site-packages/langchain_core/output_parsers/base.py?line=182'>183</a>     )
    
    File ~
/LLMApi/venv/lib/python3.12/site-packages/pydantic/main.py:341, in BaseModel.__init__(__pydantic_self__, **data)
       
 <a href='file:///Users/pratham/LLMApi/venv/lib/python3.12/site-packages/pydantic/main.py?line=338'>339</a> values, fiel
ds_set, validation_error = validate_model(__pydantic_self__.__class__, data)
        <a href='file:///Users/pratham/LLMA
pi/venv/lib/python3.12/site-packages/pydantic/main.py?line=339'>340</a> if validation_error:
    --> <a href='file:///Us
ers/pratham/LLMApi/venv/lib/python3.12/site-packages/pydantic/main.py?line=340'>341</a>     raise validation_error
     
   <a href='file:///Users/pratham/LLMApi/venv/lib/python3.12/site-packages/pydantic/main.py?line=341'>342</a> try:
     
   <a href='file:///Users/pratham/LLMApi/venv/lib/python3.12/site-packages/pydantic/main.py?line=342'>343</a>     object
_setattr(__pydantic_self__, '__dict__', values)
    
    ValidationError: 1 validation error for Generation
    text
   
   str type expected (type=type_error.str)'
    }                                                                       
                          

Agent Output:

>Entering new AgentExecutor chain...  
{  
'number\_of\_top\_rows': '2'  
}


>  
Finished chain.

  
Pydantic Object:

    class NumberofTopRows(BaseModel):
        number_of_top_rows: str = Field(
description='Number of top rows of the dataframe that should be header rows as string datatype')

  


This works fine f
or other schemas but not for this one. I am unable to figure out what is the problem. Has anyone faced similar issue? Pl
ease help in resolving this error.
```
---

     
 
all -  [ [RFC] Introduce Pluto as a deployment option for LangServe apps ](https://www.reddit.com/r/LangChain/comments/1cxuc3g/rfc_introduce_pluto_as_a_deployment_option_for/) , 2024-05-24-0911
```
Hi! I am working on a project called Pluto, which is a cloud-native application development tool. It simplifies cloud ap
plication development by providing a streamlined programming interface for leveraging cloud features and building busine
ss logic. Developers can define their dependent services and resources, such as Lambda, Bucket, and etc. by defining a v
ariable. Pluto will automatically provision the resources and deploy the application to the cloud. Developer use the Plu
to without need to learn complex cloud technologies, such as Terraform, Pulumi or AWS CDK.

To help the LangServe app de
velopers that don't have much experience with cloud to deploy their apps on the cloud, I'd like to introduce Pluto as a 
potential option for deploying LangServe apps.

In summary, there are two steps to adapt the LangServe application to th
e Pluto application so that Pluto can deploy it to AWS.

1. First, put the code related to the FastAPI app into a functi
on and make this function return the FastAPI app instance. Here we assume that the function name is `return_fastapi_app`
.
2. Then, replace the entire if `__name__ == '__main__'` code block with the following 4 statements. The `router_name` 
can be modified. It is related to the name of the Api Gateway instance created on AWS.

```python
from mangum import Man
gum
from pluto_client import Router

router = Router('router_name')
router.all('/*', lambda *args, **kwargs: Mangum(retu
rn_fastapi_app(), api_gateway_base_path='/dev')(*args, **kwargs), raw=True)
```

For more information, please refer to [
this link](https://pluto-lang.vercel.app/cookbook/deploy-langserve-to-aws).

I'm not entirely sure if this is an optimal
 interface for developing LangServe applications. Do you believe it's an effective method for LangServe app developers t
o deploy their applications in the cloud? I would appreciate any suggestions or queries that you might have. Thank you!
```
---

     
 
all -  [ Knowledge graph generation and database ](https://www.reddit.com/r/LangChain/comments/1cxqa3f/knowledge_graph_generation_and_database/) , 2024-05-24-0911
```
What is everyone using to extract the KG from unstructured data and into which database? For a local setup.
```
---

     
 
all -  [ How DSPy tuning the prompts? ](https://www.reddit.com/r/LangChain/comments/1cxo55v/how_dspy_tuning_the_prompts/) , 2024-05-24-0911
```
Hey everyone! I'm working in educational research, specifically using large language models (LLMs) to determine if quest
ions require collaboration between students (like if I give different info to Student A and Student B, and they need to 
work together to answer). I've been running several LLMs on various questions and now I'm planning to use DSPy to tweak 
the prompts to hopefully get better accuracy. I can handle the basic DSPy stuff, but I'm stumped on how it actually impr
oves the prompts. I get that prompts with higher metric scores are supposed to be better, but what's the actual strategy
 DSPy uses to enhance them?

Also, my questions often go beyond simple Q&A—they can get pretty lengthy. Do you think DSP
y is suitable for this kind of complex scenario? Any advice would be super helpful. Thanks!
```
---

     
 
all -  [ Is Langchain + Gemini 1.5 even possible (with python)? ](https://www.reddit.com/r/LangChain/comments/1cxl70h/is_langchain_gemini_15_even_possible_with_python/) , 2024-05-24-0911
```
Trying to create a Langchain v1 app with Gemini 1.5 but have hit a wall and can't even get a hello world running. I can'
t find ANY useful information anywhere and the only thing I can get working is vertex AI's API, which is rudimentary wrt
 to pydantic etc. plus I won't be able to migrate to other models later on. 

What do you guys do? Any hints, tricks and
 links are warmly received.
```
---

     
 
all -  [ Errors developing LangGraph chatbot - need urgent help, please! ](https://www.reddit.com/r/LangChain/comments/1cxl689/errors_developing_langgraph_chatbot_need_urgent/) , 2024-05-24-0911
```
Hey guys! Before I start, I'm really thankful to everyone who took their time to read this and hopefully help/guide me w
ith my project, you're saviour. For context, this chatbot is supposed to be my bachelor's final year project, so it real
ly matters a lot to me that I know it's functioning well.

Now unto my chatbot and what it is about; I'm trying to devel
op a chatbot specialized in offering the user video games recomendations based on his preferences. For this task, I thou
gh that going with LangGraph would prove to be a smart move.

For a better understanding of it, I'll attach the diagram 
that I've made of how it should behave and work, and here's a brief explanation on the chatbot's workflow and steps:

1.
 **User Query**: The user inputs a query about video game recommendations.
2. **Input Assistant**: The `input_assistant`
 checks if the query is relevant to video game recommendations using a classification prompt.
   * If relevant, the quer
y proceeds to the next step.
   * If not, the user is asked to provide a more specific query.
3. **Game Search Assistant
**: The `game_search_assistant` uses the Tavily API to find games based on the user's query and returns their titles.
4.
 **Parallel Agents**: Several agents run in parallel to gather detailed information about the recommended games  (also m
aking use of Tavily API):
   * `game_description_assistant`: Fetches game descriptions.
   * `game_platform_assistant`: 
Fetches platform availability and store details.
   * `game_genre_assistant`: Fetches game genres.
   * `game_developer_
publisher_assistant`: Fetches developer and publisher information.
   * `game_metacritic_assistant`: Fetches Metacritic 
scores.
   * `game_age_restriction_assistant`: Fetches age restriction details.
   * `game_trailer_assistant`: Fetches t
railer links.
5. **Output Assistant**: The `output_assistant` compiles the gathered information into a comprehensive res
ponse and returns it to the user.

Diagram:

https://preview.redd.it/duyi2195zu1d1.png?width=2382&format=png&auto=webp&s
=0333f1e13fff4e4d112518d8aca027117ec537fa

Problem is, I'm facing some errors, the current one being 'list indices must 
be integers or slices, not str'. I'm very new to working with this framework, or even adventuring in this sphere of LLM 
apps, so please, forgive me for my stupidity.

The code implementation of this chatbot can be accessed by clicking on th
is link: [https://github.com/MOUNAJEDK/GameSeeker-Chatbot](https://github.com/MOUNAJEDK/GameSeeker-Chatbot)

It would me
an a lot if you gave it some of your time and go through what I've written there and give me the needed feedback!
```
---

     
 
all -  [ Are multi agents systems also meant to be used in chatbots with continuous conversation? ](https://www.reddit.com/r/LangChain/comments/1cxkl24/are_multi_agents_systems_also_meant_to_be_used_in/) , 2024-05-24-0911
```
Title says pretty much. By agent I mean the concept, not exclusively langchain agent. 


```
---

     
 
all -  [ Introducing vector database capabilities in Azure Cosmos DB for NoSQL (Public Preview) ](https://www.reddit.com/r/AZURE/comments/1cxfhpb/introducing_vector_database_capabilities_in_azure/) , 2024-05-24-0911
```
We are excited to announce that native vector indexing and search in Azure Cosmos DB for NoSQL is now available in previ
ew! Azure Cosmos DB is the world’s first full-featured serverless database with vector search and features multiple vect
or index options from flat (exact), quantized flat, and a new DiskANN-based index. DiskANN is a suite of highly scalable
, accurate, and cost-effective approximate nearest neighbor (ANN) algorithms, developed at Microsoft Research, for low-l
atency and cost-effective vector search at any scale.  

You can take advantage of Azure Cosmos DB’s rich features such 
as a NoSQL query syntax to combine vector search with query filters that can increase the relevancy and accuracy of your
 vectors searches. You’ll also get all the benefits of Azure Cosmos DB’s flexibility, instant autoscale, 99.999% SLA, ge
o-replication, and more! Store your data and vectors together, eliminating the need to store vectors in a separate vecto
r database and realize improved consistency, synchronization between vectors and data, and a reduction in the complexity
 and costs of AI applications.

What is DiskANN?

DiskANN is a suite of **scalable** approximate nearest neighbor search
 algorithms designed for **efficient vector search at any scale**. It offers **high recall, high queries per second (QPS
), and** **low query latency** even for billion-point datasets. This makes it it a powerful tool for handling large volu
mes of data. [Learn more about DiskANN from Microsoft.](https://www.microsoft.com/en-us/research/project/project-akupara
-approximate-nearest-neighbor-search-for-large-scale-semantic-search/)



* DiskANN is a graph-based indexing and search
 system that performs fast and accurate approximate nearest neighbor (ANN) search at **any-scale**.
* It primarily uses 
an SSD-based index to scale to an order of magnitude more points compared to in-memory indices, while still retaining **
high QPS and low latency.**
* Quantized (compressed) vectors are kept in memory, and DiskANN balances interactions betwe
en the two to offer low latency and high accuracy.
* DiskANN is based on a novel graph index called **Vamana** that is m
ore versatile than existing graph indices by maintaining accuracy despite many insertions, modifications, and deletions,
 without the need for expensive index rebuilds.

**The DiskANN Advantage**

https://preview.redd.it/hfs6sndsst1d1.png?wi
dth=1536&format=png&auto=webp&s=2c904a439d1169741a7649e71400a975860bce79

**Scalability**

* DiskANN vector indexes are 
stored on high-speed SSDs, while compressed vectors are stored in memory.  This reduces memory-footprint of the vector i
ndex, enabling planet-sized scalability for vector search scenarios.

**Low Latency**

* The DiskANN graph index constru
ction makes it very efficient during search, minimizing the number of SSD reads to achieve high throughput and low laten
cy.

**High Accuracy**

* During index construction, nodes in the graph are connected to diverse neighbors to improve re
call. After the search operation, the results are re-ranked using the full-precision vectors providing high accuracy.

*
*Low Cost**

* Because the quantized vectors are stored in memory and the full-precision graph is stored on SSDs, it’s m
uch less expensive to maintain and operate DiskANN-based indexes. This results in lower RU costs for your vector search 
queries.

**Robust to Insertions, Deletions, and Modifications**

* The DiskANN graph index is capable of supporting tra
nsactional workloads and does not degrade over time with high volumes of inserts, updates, or deletes. This is a differe
ntiator among typical vector databases in the market today, which are built using HNSW and other less robust methods tha
t require computationally expensive full index rebuilds to maintain accuracy.

The benefits of DiskANN, combined with th
e instant & dynamic autoscale, global replication, and industry leading 99.999% SLA of Azure Cosmos DB make for an unpar
alleled database for managing both your operational and vector data workloads.

# What vector index options are availabl
e?

There are multiple types of vector index policies that can be defined for a Cosmos DB collection. [Learn more about 
vector indexing in Azure Cosmos DB](https://aka.ms/CosmosDBVectorIndexing)

* **Flat index** is an exact (sometimes call
ed brute-force) approach to vector indexing. The vectors are placed on the Azure Cosmos DB index and referenced for effi
cient lookup. This may be a good option to use in scenarios where 100% accuracy of vector searches is required, and both
 the dimensionality of the vectors is small.
* **Quantized Flat index** is also an exact index, but the vectors are quan
tized (compressed) before being added to the Azure Cosmos DB index. This is very efficient and uses the same quantizatio
n method featured in DiskANN.
* **DiskANN** enables approximate nearest neighbors (ANN) search at scale, with efficienci
es that reduce RU cost and latency. This is extremely efficient and low-cost, especially when you expect to scale to lar
ger scenarios. **Note** that using the DiskANN index requires [enrollment in a separate preview](https://aka.ms/DiskANNS
ignUp) as it’s still in an early preview version.

This table provides a good guide for the different index types and th
eir strengths:

||
||
|**Index type**|**Description**|**When to use it?**|**Max # of dimensions**|**RU Cost**|**Speed**|
**Accuracy**|
|Flat|Exact search on full vectors|100% accuracy is required The container holds fewer than 10k vectors. V
ectors are small in size|505|High|Slow|Highest|
|Quantized Flat|Exact search on quantized vectors. Faster, with slight a
ccuracy reduction.|High accuracy is needed You have at least 1,000 vectors in the collection. Vectors are larger in size
 The scenario is scoped to at most 100k vectors|4096|Medium|Medium|High|
|DiskANN|Fast, approximate search at any scale.
|In any scenario where scale is expected|4096|Lowest|Fast|High|

 

 

**Enroll in the Vector Search Preview**

Vector s
earch in Azure Cosmos DB for NoSQL is a preview feature and requires enrollment via the *Features* page of your Azure Co
smos DB resource . Follow the below steps to register:

1. Navigate to your Azure Cosmos DB for NoSQL resource page.

2.
 Select the “Features” pane under the “Settings” menu.

3. Select “Vector Search in Azure Cosmos DB for NoSQL”.

4. Read
 the description of the feature and confirm you want to enroll in the preview.

5. Select “Enable” to enroll in the prev
iew.

https://preview.redd.it/jc9y0k5jst1d1.png?width=1536&format=png&auto=webp&s=7ae7741f772a6da598bf4aa827ecbc0fe6d918
ba

 

# Next Steps

The integration of vector search capabilities into Azure Cosmos DB for NoSQL marks a significant ad
vancement in database technology, offering unparalleled scalability, efficiency, and accuracy. With the introduction of 
DiskANN and other vector indexing options, Azure Cosmos DB provides robust solutions for managing large-scale vector dat
a alongside your operational data. Enroll in the Vector Search Preview today and explore the future of AI-driven applica
tions with the powerful features of Azure Cosmos DB.

* [Learn more about Vector Search Preview in Azure Cosmos DB. ](ht
tps://aka.ms/CosmosVectorSearch)
* [Enroll in the DiskANN early preview](https://aka.ms/DiskANNSignUp)
* [Azure Cosmos D
B in Semantic Kernel](https://github.com/microsoft/AzureDataRetrievalAugmentedGenerationSamples/)
* [Azure Cosmos DB | 🦜
️🔗 LangChain](https://python.langchain.com/v0.1/docs/integrations/vectorstores/azure_cosmos_db/)
* [Vector Database | Mi
crosoft Learn](https://learn.microsoft.com/en-us/semantic-kernel/memories/vector-db)
* [DiskANN – Microsoft Research](ht
tps://www.microsoft.com/research/publication/diskann-fast-accurate-billion-point-nearest-neighbor-search-on-a-single-nod
e/)

  
Blog originally posted at: [https://devblogs.microsoft.com/cosmosdb/introducing-vector-database-capabilities-in-
azure-cosmos-db-for-nosql/](https://devblogs.microsoft.com/cosmosdb/introducing-vector-database-capabilities-in-azure-co
smos-db-for-nosql/)
```
---

     
 
all -  [ [For Hire] GenAI Specialist, Ex-Booking.com Data Scientist [50USD/hr] ](https://www.reddit.com/r/freelance_forhire/comments/1cxehch/for_hire_genai_specialist_exbookingcom_data/) , 2024-05-24-0911
```
Hi, I am data analyst/scientist with 4 years experience. I have worked for one of the world biggest Telecom groups (Tele
nor) and also Agoda(Booking.com). Now working as GenAI specialist at vanna AI

If your looking to outsource tasks or get
ting something built in Python/R or QuickSense/Tableau please do reach out.


I can provide evidence of everything, I ev
en write about data science/analytics on Medium: https://python.plainenglish.io/sankeying-with-plotly-90500b87d8cf

GenA
I projects:
https://medium.com/firebird-technologies/generate-powerpoints-using-llama-3-a-first-step-in-automating-slide
-decks-536f5fcb6e0e

https://medium.com/firebird-technologies/using-langchain-to-teach-an-llm-to-write-like-you-aab394d5
4792

Very good at making visualization. Will charge a reasonable rate
```
---

     
 
all -  [ LLM prompt optimization ](https://www.reddit.com/r/LangChain/comments/1cxcln7/llm_prompt_optimization/) , 2024-05-24-0911
```
I would like to ask what are your experience in doing prompt optimization/automation when designing ai pipelines? In my 
experience, if your pipeline is composed of large enough number of  LLMs, that means it’s getting harder to manually cre
at prompts that make the system work. What’s worse is that you even cannot predict and control how the system might sudd
enly break or have worse performance if you change any of the prompts! I’ve played around with DSPy a few weeks before; 
however, I am not sure if it can really help me in the real world use case? Or do you have other tools that can recommen
d to me? Thanks for kindly sharing your thoughts on the topic!
```
---

     
 
all -  [ Can we use more than 1024 input tokens in flan-t5-xxl  ](https://www.reddit.com/r/LangChain/comments/1cxbehz/can_we_use_more_than_1024_input_tokens_in/) , 2024-05-24-0911
```
Is there a way to use the Google/flan-t5-xxl model with context of over 1024 tokens.
I am using hugging face inference a
pi and it has that limitations.
```
---

     
 
all -  [ Need help with prompting Mistral-7B-Instruct-v0.2 for creating a coding tutor bot ](https://www.reddit.com/r/MistralAI/comments/1cxacjw/need_help_with_prompting_mistral7binstructv02_for/) , 2024-05-24-0911
```
Hello everyone,  
I am trying to create a Multi-agent Coding Tutor chatbot (*or academically speaking 'CTS - Conversatio
nal Tutoring System'*) for my course project. We want it to be a personalized tutor, which means that it will teach the 
person based on their age, level of education, and hobbies or interests.

To instruct this Mistral-7B-Instruct-v0.2 4-bi
t quantized model, we have added the following system prompt to the model:

    system_prompt = f'''Imagine you are a fr
iendly and highly knowledgeable teacher who specializes in teaching {prog_language_to_teach} programming. 
    Your stud
ent, who is a {user_age}'s old {user_edu_scope} student and whose understanding and interests is into {user_interest}, i
s eager to learn and looks up to you for clear, easy-to-understand explanations. 
    For every concept you introduce, p
rovide a brief overview and relate it to a real-life scenario or analogy that will resonate with the student, making it 
easier for them to grasp the topic quickly.
    
    When explaining programming concepts, consider the student's age an
d their hobbies or interests, tailoring examples and analogies to align with these details. Your explanations should inc
lude short, precise programming examples relevant to the student's life and interests. 
    After presenting an example,
 break it down into step-by-step explanations to ensure the student fully understands.
    
    Periodically, engage the
 student with quick quiz questions or programming tasks that are directly related to what you've discussed. 
    These a
ctivities should build on the chat history and context, reinforcing the student's learning and keeping the conversation 
interactive and engaging.
    
    Remember, your goal is to create a supportive, engaging learning environment that ada
pts to the student's abilities, interests, and pace, making learning Python an enjoyable and rewarding experience.'''

M
istral-7B-Instruct-v0.2 doesn't have an explicit system prompt, so I had to find a different way to add one to the code 
for the very first prompt.

`model_input = f'<s>[INST] {system_prompt} [/INST]</s>' + f'[INST] {user_message} [/INST]'`


Now, on the initial run, the chatbot is doing fine often and as expected.  In the case of a 10-year-old Kindergartener 
who loves 'Baby Shark Rhyme,' the bot will talk about what he likes. In another case of a 20-year-old shareholder in the
 share market, the bot tried to teach programming using business analogies.

But the common issues I face are the follow
ing:

1. The chatbot is too verbose, especially on complex topics such as Encapsulations. (*I have used* `max_new_tokens
=1000`, is it causing the verbosity? Lessening to 500 or 750 causes the model to stop on incomplete answers abruptly.\*)

2. So far, **switching from a coding tutor to a general tutor has been the hardest thing**. For instance, if the user i
s older and asks about something off-topic, like *Newton's law* or the *American Law of Immigration*, it immediately swi
tches itself from the coding tutor to that other tutor.
3. Another problem is that it gives the answers right away while
 it generates the quizzes. Although I tested with different prompts, I can resist this nature.

My biggest problem so fa
r is the 2nd and 1st one, respectively. I have tried adding refusal prompts in the system prompt, but then it slightly r
efuses to teach those irrelevant topics and then starts making coding examples on it.

        ## Strict Refusal:
      
  If the question is not related to programming, respond strictly with a refusal sentence and do not provide any further
 explanation or code.

For these cases, sometimes it follows, sometimes not. Also adding too many instructions into the 
system prompts too big resulting in GPU memory exhaustion after 5-6 long chats. BTW, To mimic a memory feature, I am sav
ing chats to a dictionary.

Since yesterday and again tonight, I've been trying to make the prompting better but haven't
 been able to. I'm brand new to LLM chatbot programming and have never done this before. This project began a month ago 
because the idea is unique to my MSc project, but I got stuck in the middle of it.

How can I make the prompting better 
to avoid the problems that were brought up? Also, can someone recommend a good tutorial on how to make this kind of chat
bot? I've been looking for these, but most of the tutorials use OpenAI and/or langchain. For a change, my supervisor wan
ts us to only test with open-source models. We can use Mistral to begin because it fits on the Kaggle notebook we have.


Any suggestion including trying to other approaches, totally changing the system prompt, and trying another one (*if yo
u say so, can you please show me one?*) and a good & detailed tutorial will be super appreciated. IDK, suddenly it feels
 so lost.
```
---

     
 
all -  [ [For Hire] Programmer/Web Developer/IT Consultant (Python, PHP, AI, etc.) ](https://www.reddit.com/r/forhire/comments/1cx9mj0/for_hire_programmerweb_developerit_consultant/) , 2024-05-24-0911
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

     
 
MachineLearning -  [ [R] Building an Observable arXiv RAG Chatbot with LangChain, Chainlit, and Literal AI ](https://www.reddit.com/r/MachineLearning/comments/1crwh0q/r_building_an_observable_arxiv_rag_chatbot_with/) , 2024-05-24-0911
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

     
 
MachineLearning -  [ [P] LLMinator: A Llama.cpp + Gradio based opensource Chatbot to run llms locally(cpu/cuda) directly  ](https://www.reddit.com/r/MachineLearning/comments/1cpbgd1/p_llminator_a_llamacpp_gradio_based_opensource/) , 2024-05-24-0911
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

     
