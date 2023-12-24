 
all -  [ 🚀 Introducing Resume Checker: Your Python Companion for Job Applications! ](https://www.reddit.com/r/LangChain/comments/18phsg5/introducing_resume_checker_your_python_companion/) , 2023-12-24-0911
```
Hey Langchain Community!

I'm learning Python and langchain and excited to share a project that i've been working on: [R
esume Checker](https://github.com/navicstein/resume-checker).

Resume Checker is a Python tool designed to analyze how w
ell your resume matches a specific job posting. As someone learning Python, I found this project immensely helpful in un
derstanding langchain and building practical applications.

Check out the [GitHub repository](https://github.com/navicst
ein/resume-checker) for more detailed instructions. let me know what you think
```
---

     
 
all -  [ creating a vectordb from millions of documents ](https://www.reddit.com/r/LangChain/comments/18ph140/creating_a_vectordb_from_millions_of_documents/) , 2023-12-24-0911
```
Hey! I am trying to create a vector store using langchain and faiss for RAG(Retrieval-augmented generation) with about 6
 millions abstracts. is there a strategy to create this vector store efficiently? currently it takes very long time to c
reate it (can take up to 5 days)
```
---

     
 
all -  [ Inconsistent Table Querying ](https://www.reddit.com/r/LangChain/comments/18pfbu9/inconsistent_table_querying/) , 2023-12-24-0911
```
I am working on a project that uses Langchain in multiple places, I am getting inconsistent behavior, hoping someone can
 tell me what I am doing wrong here. (I am using a public bq dataset for this, so nothing proprietary in what I am posti
ng). I first use agent\_executor to generate a description of a table. I pass the table in as a variable. But the agent 
attempts to run the query return an error that the table is not found. In the same project I use db\_chain to allow natu
ral language to SQL querying of the table. In this case the table is found and a result is return. I have checked the SQ
L and results returned against the source data to confirm it is indeed querying the table. I am not sure why the table i
s found in one case but not the other

    # Working agent
    system_prompt = f' in {table_to_query}.You are a BigQuery
 expert. You are able quickly review the tables in a dataset and understand the contents of each table along with their 
relation. You will be asked a question for which you need to generate and execute a query. The table in the question is 
the main focus of the question, but you may also need to join to other tables, so keep them in mind as your create your 
plan. The other tables are {dataset_table_names}. The column names may not match 1:1 in the prompt, use your best reason
ing to select a column (for instance a user may ask for an account but in the table the column is account_name).Ensure t
hat the columns you use in the query exist in the table. As you answer the users question, consider what other columns m
ay be additive to their question and include those in your response'
    full_prompt = user_prompt + system_prompt
    

    
    if run_prompt:
       
        
        from langchain.utilities import SQLDatabase
        from langchain.llms
 import OpenAI
        from langchain_experimental.sql import SQLDatabaseChain
        
        db = SQLDatabase(engine)
 #, include_tables=prompt_tables)
        llm = OpenAI(temperature=.5, verbose=True)
    
        db_chain = SQLDatabase
Chain.from_llm(llm, verbose=True,db=db, use_query_checker=True, top_k=10)
    
        db_chain.run(full_prompt)
    
  
  else: 
        display('Waiting on you to run the query')
    
    
    > Entering new SQLDatabaseChain chain...
    W
hat was the most popular name in Utah in 2010 in bigquery-public-data.usa_names.usa_1910_2013.
    SQLQuery:SELECT
     
   name,
        SUM(number) AS total
    FROM
        `bigquery-public-data`.usa_names.usa_1910_2013
    WHERE
        
state = 'UT'
        AND year = 2010
    GROUP BY
        name
    ORDER BY
        total DESC
    LIMIT 10
    SQLResul
t: [('Olivia', 269), ('William', 264), ('Mason', 243), ('Jacob', 235), ('Ethan', 235), ('James', 231), ('Samuel', 227), 
('Isaac', 215), ('Abigail', 210), ('Logan', 206)]
    Answer:Olivia
    > Finished chain.
    

\--

    # Non Working
 
   from langchain.agents import create_sql_agent
    from langchain.agents.agent_toolkits import SQLDatabaseToolkit
    
from langchain.utilities import SQLDatabase
    from langchain.llms import OpenAI
    
    # from langchain.agents impor
t AgentExecutor
    from langchain.agents.agent_types import AgentType
    
    db = SQLDatabase(engine)
    
    agent_
executor = create_sql_agent(
        llm=OpenAI(temperature=0),
        toolkit=SQLDatabaseToolkit(db=db, llm=OpenAI(tem
perature=0)),
        verbose=True,
        agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    )
    
    agent_execu
tor.run(f'Describe the {table_to_query} table')
    
    
    > Entering new AgentExecutor chain...
    Action: sql_db_l
ist_tables
    Action Input: 
    Observation: 
    Thought: I should query the schema of the usa_names table.
    Actio
n: sql_db_schema
    Action Input: bigquery-public-data.usa_names.usa_1910_2013
    Observation: Error: table_names {'bi
gquery-public-data.usa_names.usa_1910_2013'} not found in database
    Thought: I should check the spelling of the table
 name.
    Action: sql_db_schema
    Action Input: bigquery-public-data.usa_names.usa_1910_2013
    Observation: Error: 
table_names {'bigquery-public-data.usa_names.usa_1910_2013'} not found in database

&#x200B;
```
---

     
 
all -  [ Llama ReAct ](https://www.reddit.com/r/LargeLanguageModels/comments/18pacr8/llama_react/) , 2023-12-24-0911
```
Has anyone be able to get llama to reliably work with langchain for calling multiple tools (Wikipedia arxiv etc) I’m usi
ng the 13b with a custom prompt and occasionally get good results however most outputs are parsing errors. 

Any suggest
ions?
```
---

     
 
all -  [ how to create a rag for all the chats/ conversations between A and everyone else wherein a bot can a ](https://www.reddit.com/r/LangChain/comments/18pa4gz/how_to_create_a_rag_for_all_the_chats/) , 2023-12-24-0911
```
I'm working on a project involving where I want to analyze conversations between two individuals, let's call them Person
 A and Person B. The primary function of this system is to enable a bot to answer questions about Person A's interests b
ased on past conversations between A and other individuals.

I am contemplating the best approach to use embedding model
s in this context. The challenge lies in conversational data, which is inherently different from structured documents. C
onversations typically lack distinct paragraphs or sections, making traditional chunking and embedding techniques less s
traightforward.

1. **Sentence-Level Embeddings**: Embedding each sentence individually to capture specific details. How
ever, this might limit the response to only the information contained in that particular sentence.  
2. **Conversation-L
evel Embeddings**: Creating embeddings for entire conversations. While this could capture the overall context, it might 
not be precise for detailed queries.
3. **Summarization Before Embedding**: Generating a summarized version of the conve
rsations and then embedding these summaries. I'm curious about the effectiveness and potential loss of detail with this 
method.

My questions for the community are:

* What are the recommended practices for embedding models in this kind of 
RAG system, especially considering the conversational nature of the data?
* Are there any specific techniques or methodo
logies that you would suggest for this type of application, possibly something that has worked well in your experience?
```
---

     
 
all -  [ Building a Japanese Kanji Flashcard App using GPT-4, Python and Langchain ](https://adilmoujahid.com/posts/2023/10/kanji-gpt4/) , 2023-12-24-0911
```

```
---

     
 
all -  [ Any good documentation/tutorial/e-book on url tools in langchain? ](https://www.reddit.com/r/LangChain/comments/18p25me/any_good_documentationtutorialebook_on_url_tools/) , 2023-12-24-0911
```
Hi, I have been trying to use LangChain Selenium and other url loaders, but can't find good documentation for now. Any i
nformation source is welcome.
```
---

     
 
all -  [ Way to make gpt 3.5 summarize based on a word count ](https://www.reddit.com/r/PromptEngineering/comments/18p1u55/way_to_make_gpt_35_summarize_based_on_a_word_count/) , 2023-12-24-0911
```
I need to make a summarization bot with python and langchain but i got stuck in the step of telling gpt i want this summ
ary exactly 200 words long. For some reason gpt never writes a 200 word summary even though i say it so. Is there a way 
to make it exactly 200 words long?(or around that bar)
```
---

     
 
all -  [ What frameworks or coding structures are recommended for building applications powered by LangChain  ](https://www.reddit.com/r/LangChain/comments/18p1ghh/what_frameworks_or_coding_structures_are/) , 2023-12-24-0911
```
The application features integrations with various tools, including databases, Retrieval-Augmented Generation (RAG), and
 custom prompts, as well as custom tools within LangChain. 
```
---

     
 
all -  [ Langchain and Python alternatives ](https://www.reddit.com/r/LocalLLaMA/comments/18p01k8/langchain_and_python_alternatives/) , 2023-12-24-0911
```
It seems like almost every RAG and Agent is built around Langchain. Like every single AI video ever made seems to use La
ngchain for something. Is there any way to avoid that? Any other frameworks?

And, am I to be lead to believe that the o
nly language is Python. C++ maybe? C++ and Python are the only two languages with cuda support?

No Golang, Swift, Rust?
 

I don’t want to continually build langchain products, and I’d like to do RAG.
```
---

     
 
all -  [ Ashamed to asked ](https://www.reddit.com/r/LangChain/comments/18opwbl/ashamed_to_asked/) , 2023-12-24-0911
```
kind of ashamed to ask but what am i missing here ?. the cash\_flow\_data method returns a list of cash flow statements 
in the form of dataframes, then i try to map each iteration to the prompt template but thats not working. instead i get 
this error. Any ideas why? u/hwchase17 . 

https://preview.redd.it/6o8c00uy2x7c1.png?width=2336&format=png&auto=webp&s=6
2d403052114c9de56573f1a85b4306497c23599

https://preview.redd.it/r36pe0uy2x7c1.png?width=2336&format=png&auto=webp&s=897
67aa7dbb3a4a2406229bc9611078ef0f4915d
```
---

     
 
all -  [ Bedrock Claude Performance Issue ](https://www.reddit.com/r/LangChain/comments/18opvla/bedrock_claude_performance_issue/) , 2023-12-24-0911
```
Anybody have any idea what I might be doing wrong here?

    const claudeBedrock = new Bedrock({model: 'anthropic.claude
-v2:1',region: aws_region,modelKwargs: {temperature: 0.0,top_k: 250,top_p: 0.999,stop_sequences: ['Human:'],max_tokens_t
o_sample: maxTokens}}
    
    const chain = = new LLMChain({llm: claudeBedrock, prompt: prompt})

I have tried .`call`,
 .`_call`, .`invoke`, .`predict` and they all produce worse results than through the AWS console.

I have verbose ON and
 literally copy and pasting the logged prompt produced by Langchain into the Bedrock playground and it produces better r
esults.

I tried both Chat & Text in playgrounds using the EXACT same settings as above.

The prompt is asking Claude to
 classify a list of something. I have tried multiple times on both sides and the output through Langchain is WORSE by in
cluding results that is wrong. The console produces correct results everytime.

It's driving me nuts that I'm about to t
ear out Langchain and use AWS's SDK instead.

&#x200B;

&#x200B;
```
---

     
 
all -  [ Is there a way in LC to centralize event notifications and configurations? ](https://www.reddit.com/r/LangChain/comments/18om6xq/is_there_a_way_in_lc_to_centralize_event/) , 2023-12-24-0911
```
https://www.youtube.com/watch?v=D34PyNx71vk

The YouTube video shares an architectural difference between LangChain and 
Microsofts orchestrator. Is there really no way to do the same in LangChain?
```
---

     
 
all -  [ [Langchain] Quelle est la différence entre l'agent des fonctions OpenAI et l'agent multi-fonctions O ](https://www.reddit.com/r/redditenfrancais/comments/18oinsw/langchain_quelle_est_la_différence_entre_lagent/) , 2023-12-24-0911
```
J'ai lu le Doc entier plusieurs fois et j'ai finalement fini par lire le code source, mais je ne sais toujours pas quell
e est la différence entre ces deux agents.

Si quelqu'un a une explication, je serai reconnaissant.

Traduit et reposté 
à partir de la publication 14nreov de la communauté langchain. Pour retrouver la publication originale, insérez l'id de 
la publication après 'reddit.com/'
```
---

     
 
all -  [ How do Callbacks for streaming response exactly work? (In Streamlit application) ](https://www.reddit.com/r/LangChain/comments/18ogw3p/how_do_callbacks_for_streaming_response_exactly/) , 2023-12-24-0911
```
Hi,

I'm currently trying to implement my RAG application in Streamlit without the use of LangChain for various reasons,
 however i have a problem to get the streaming response right for my LLM (AWS SageMaker endpoint).

The previous approac
h that works is passing a custom Streamhandler (that takes the streamlit container) to the Chain that overrides the on\_
llm\_new\_token method (writes to the container with every call of the method) and modifying the sagemaker\_endpoint.py 
that it calls the method for every Token i get from the Event Stream. 

As seen here: [https://github.com/langchain-ai/c
hat-langchain/issues/39](https://github.com/langchain-ai/chat-langchain/issues/39)

&#x200B;

Now when trying to get thi
s to work without LangChain i only get empty responses.

I call the endpoint via boto3 client and successfully get a res
ponse stream. However when iterating with the TokenIterator nothing happens. This approach would work in a normal python
 script with writing to the console but not within my Streamlit application.

    def call_llm(prompt, container):
     
   response = boto3_client.invoke_endpoint_with_response_stream(
                Arguments... (No errors here)
         
       )
        print(response) # Shows that i get a valid EventStream
        current_completion = ''
        for toke
n in TokenIterator(response['Body']):
            current_completion += token
            print(token) # Nothing happens
 here
            container.markdown(current_completion) # Nothing happens here either

Same problem when i create a str
eam\_handler class (not inherited from the LangChain BaseCallbackHandler) with the corresponding method. I don't really 
understand how the Callbacks work within LangChain. It seems like i can't get the same behaviour if i code it myself.

 
   def call_llm(prompt, stream_handler): # Give a streamhandler with corresponding container instead
        response = 
boto3_client.invoke_endpoint_with_response_stream(
                Arguments... (No errors here)
                )
     
   print(response) # Shows that i get a valid EventStream
        current_completion = ''
        for token in TokenIter
ator(response['Body']):
            current_completion += token
            print(token) # Nothing happens here
        
    stream_handler.on_llm_new_token(current_completion) # Nothing happens here                         
        either


I'd be very thankful for a workaround or an explanation how the Callbacks work in LangChain.
```
---

     
 
all -  [ [Local Llama] Comment exposer un modèle dans une API? ](https://www.reddit.com/r/redditenfrancais/comments/18od590/local_llama_comment_exposer_un_modèle_dans_une_api/) , 2023-12-24-0911
```
J'ai un PC avec un RTX 3090 et je voudrais l'utiliser pour des modèles comme LLAMA2. Je voudrais ouvrir un port et offri
r la puissance d'inférence de ce PC à d'autres applications exécutant Langchain en dehors du réseau domestique.

J'ai pe
nsé à combiner fastapi avec le package local HF, mais je crois qu'il existe d'autres options beaucoup mieux.

Traduit et
 reposté à partir de la publication 15qs2br de la communauté localllama. Pour retrouver la publication originale, insére
z l'id de la publication après 'reddit.com/'
```
---

     
 
all -  [ How to use LLM response stream without LangChain ](https://www.reddit.com/r/StreamlitOfficial/comments/18od2xf/how_to_use_llm_response_stream_without_langchain/) , 2023-12-24-0911
```
Hi,

I developed a little RAG application and now i want to rebuild most parts without using LangChain for various reaso
ns.

I'm using a SageMakerEndpoint from AWS as my LLM. It was pretty difficult to get the response stream to work with L
angChain, now i have a similiar problem when i try the same without LangChain.

&#x200B;

The solution with LangChain is
 described here: [https://github.com/langchain-ai/chat-langchain/issues/39](https://github.com/langchain-ai/chat-langcha
in/issues/39)

It's pretty straightforward. We have to create a CallbackManager that takes the container and writes on e
very new token. However i don't really understand why we need that in the first place?

My attempt was to implement the 
TokenIterator from here:

[https://aws.amazon.com/de/blogs/machine-learning/stream-large-language-model-responses-in-ama
zon-sagemaker-jumpstart/](https://aws.amazon.com/de/blogs/machine-learning/stream-large-language-model-responses-in-amaz
on-sagemaker-jumpstart/)

pass the container to my llm-call function like this:

    def call_llm(prompt, container):
  
      response = boto3_client.invoke_endpoint_with_response_stream(
                Arguments... (No errors here)
      
          )
        print(response) # Shows that i get a valid EventStream
        current_completion = ''
        for t
oken in TokenIterator(response['Body']):
            current_completion += token
            print(token) # Nothing happ
ens here
            container.markdown(current_completion) # Nothing happens here either

The same code works in a norm
al python application. I guess streamlit just works in a different way i don't understand yet.

I tried the same approac
h with a StreamHandler (writing my own instead of using LangChain). I passed the stream handler with the container to th
e function and called the overwritten on\_new\_llm\_token method inside the TokenIterator loop. Thats the same approach 
as in the solution described just without inheriting from the BaseCallBackHandler from LangChain. This doesn't work eith
er.

THe LangChain approach would be to write your own StreamHandler that overwrites the BaseCallBackHandler. However i 
don't see why this approach works and my own doesn't. What makes the LangChain CallbackHandler so 'special'. I'm probabl
y overseeing something here.

&#x200B;

Thank you for your help
```
---

     
 
all -  [ [Langchain] L'ingénierie rapide semble être une conjecture - comment évaluer correctement l'applicat ](https://www.reddit.com/r/redditenfrancais/comments/18obpkw/langchain_lingénierie_rapide_semble_être_une/) , 2023-12-24-0911
```
Comment les gens évaluent-ils la qualité de vos applications LLM? Je gère un chatbot en santé mentale en production (pet
ite échelle - 10 utilisateurs actifs) et j'ai passé beaucoup de temps à des invites en train de mener, mais ce n'est que
 des conjectures.

Je vais faire un ajustement à l'invite et exécuter quelques conversations de test et obtenir un peu l
es vibrations de savoir si c'est mieux ou pire qu'avant le toit. Est-ce ce que vous faites aussi ou est-ce que je manque
 quelque chose ???

Traduit et reposté à partir de la publication 164ey51 de la communauté langchain. Pour retrouver la 
publication originale, insérez l'id de la publication après 'reddit.com/'
```
---

     
 
all -  [ Langchain returns similarity_search_with_relevance_scores in negative ](https://www.reddit.com/r/LangChain/comments/18o9afp/langchain_returns_similarity_search_with/) , 2023-12-24-0911
```
Guys, I'm doing a similarity search and using relevance scores because I understand relevance scores return scores betwe
en 0 and 1. However when I use Langchain to return these scores, they come back in negatives. However when I use custom 
code for chroma or faiss, I get scores between 0 and 1. Is this a bug in Langchain, pls help.
```
---

     
 
all -  [ Get time needed for individual components of ConversationalRetrievalChain ](https://www.reddit.com/r/LangChain/comments/18o2r72/get_time_needed_for_individual_components_of/) , 2023-12-24-0911
```
Hi all,

Is there a way I can get the time needed for each individual components of ConversationalRetrievalChain?

For e
g, how do I get the time needed for the LLM to generate a reply?
```
---

     
 
all -  [ My import of FAISS is not recognized in my IDE ](https://www.reddit.com/r/pythonhelp/comments/18o2obg/my_import_of_faiss_is_not_recognized_in_my_ide/) , 2023-12-24-0911
```
I'm testing a code from a tutorial to see if i can integrate its concept into mine. But for some reason when I type impo
rt FAISS like below it just stays white unline the rest of the imports in the IDE. I dont know why its not recognized, I
ve traied pip install langchain, pip install faiss-cpu, pip install 'langchain\[all\]', and I looked at the documentatio
n. I am not sure whats causing this and any help is appreciated

    from dotenv import load_dotenv
import streamlit as 
st
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.open
ai import OpenAIEmbeddings
from langchain.vectorstores import FAISS

def main():
    load_dotenv()
    st.set_page_confi
g(page_title='Ask your pdf')
    st.header('Ask your PDF')

    pdf = st.file_uploader('Upload your pdf', type='pdf')

 
   if pdf is not None:
        pdf_reader = PdfReader(pdf)
        text = ''
        for page in pdf_reader.pages:
     
       text += page.extract_text()

        text_splitter = CharacterTextSplitter(
            separator='\n',
         
   chunk_size = 1000,
            chunk_overlap = 200,
            length_function = len
        )

        chunks = tex
t_splitter.split_text(text)

        embeddings = OpenAIEmbeddings()
        knowledge_base = FAISS.from_texts(chunks, e
mbeddings)

        user_question = st.text_input('ask a question about your pdf: ')



if __name__=='__main__':
    mai
n()

&#x200B;
```
---

     
 
all -  [ How to pass some arguments to function call via code and some extracted from LLM? ](https://www.reddit.com/r/LangChain/comments/18nzw4v/how_to_pass_some_arguments_to_function_call_via/) , 2023-12-24-0911
```
I have the following:  
I want to be able to use agents and pass one argument programmatically. I ideally dont want that
 in prompt.

    def testFunc(text1, email):
        print(text1)
        print(email)
    
    
    tools = [
    Struc
turedTool.from_function(
 func=testFunc,
 name='testing',
 args_schema=TestSchema,
 description='tester',
 return_direct
=True,

 )
]
    
    model_with_tools = model.bind(
        functions=[format_tool_to_openai_function(t) for t in tools
],
    )
    prompt = ChatPromptTemplate.from_messages(
        [
            ('system', template),
            Messages
Placeholder(variable_name='chat_history'),
            MessagesPlaceholder(variable_name='agent_scratchpad'),
          
  ('user', '{input}'),
        ]
    )
    agent = (
        {
            'input': lambda x: x['input'],
            'a
gent_scratchpad': lambda x: format_to_openai_function_messages(
                            x['intermediate_steps']
    
                    ),
            'chat_history': lambda x: x['chat_history'],
            'email': lambda x: x['email'
],
        }
        | prompt
        | model_with_tools
        | OpenAIFunctionsAgentOutputParser()
    )
    
    age
nt_executor = AgentExecutor(
        agent=agent, tools=tools, verbose=True, return_intermediate_steps=True
    )
    
 
   result = agent_executor.invoke(
                {'input': 'this is the test code', 'chat_history': [], 'email': 'TEST
@GMAIL.COM'}
            )

I want the output to be 

    this is the test code
    TEST@GMAIL.com

Basically I want the
 email to be passed programmatically and the other arguments to be passed using the LLM. I cant figure this out. Have be
en going at it for a while. No matter what, the function is being called with the prompt, which doesnt have the email an
d it is hallucinating the email as [user@example.com](mailto:user@example.com)  


Is there no way to pass the email to 
the function, maybe a additional kwarg thing or extra configs or something?  
After the prompt part of the chain ends, I
 can see the part entering the LLM is:  


     'kwargs': {           'content': this is the test code',           'addi
tional_kwargs': {}         } 
```
---

     
 
all -  [ Errors using SQL Agent ](https://www.reddit.com/r/LangChain/comments/18ntfoa/errors_using_sql_agent/) , 2023-12-24-0911
```
Hello everyone. I'm using Langchain (js) in my Next.js app and used this guide [https://js.langchain.com/docs/integratio
ns/toolkits/sql](https://js.langchain.com/docs/integrations/toolkits/sql) (that someone very helpful shared with me here
 on reddit) to integrate the SQL agent.

 I'm getting **Agent stopped due to max iterations.** or a random incorrect ans
wer from the agent. 

 I implemented it pretty much exactly like the docs I referenced but with a postgreSQL db in Supab
ase instead of a local .db. 

Any thoughts or recommendations are appreciated👍. Thanks in advance
```
---

     
 
all -  [ How to use Langsmith with a FastAPI/uvicorn setup ](https://www.reddit.com/r/LangChain/comments/18npk5y/how_to_use_langsmith_with_a_fastapiuvicorn_setup/) , 2023-12-24-0911
```
Hi there fellow Langchainers,

I have created an agent in a ipynb. Works great and by simply adding
LANGCHAIN_TRACING_V2
 = os.getenv('LANGCHAIN_TRACING_V2')
LANGCHAIN_PROJECT = os.getenv('LANGCHAIN_PROJECT')
LANGCHAIN_ENDPOINT = os.getenv('
LANGCHAIN_ENDPOINT')
LANGCHAIN_API_KEY = os.getenv('LANGCHAIN_API_KEY')
and adding these values to the .env file and 

f
rom langsmith import Client
client = Client()

Every agent_executor.invoke({'input': 'input query here'})['output']

is 
nicely logged in Langsmith.

But when I wrap this same agent in a fastapi application with uvicorn, it doesn't work. The
 agent works fine, I can use the agent through Postman just fine. But nothing is logged in Langsmith.

Any help is great
ly appreciated.
```
---

     
 
all -  [ How to distribute LLM apps and UI/UX? ](https://www.reddit.com/r/LocalLLaMA/comments/18np956/how_to_distribute_llm_apps_and_uiux/) , 2023-12-24-0911
```
Pretty new to the space but I'm a programmer. I see a lot of YouTube tutorials using Langchain, Ollama, and 50 other too
ls. Seems easy to build my own app.

How are these apps packaged and distributed so other people can install and interac
t with them? What are the best frameworks to use for this? How do you build a custom UI? Looking for best practices or s
hortest path to something basic.

For example: do you use Langchain and launch a Web UI from a local nodejs server that 
lets users modify their documents for RAG or swap models?

Thanks for any helpful responses.
```
---

     
 
all -  [ [Langchain] Besoin d'aide pour augmenter la vitesse de mon application basée sur LLM ](https://www.reddit.com/r/redditenfrancais/comments/18no9yi/langchain_besoin_daide_pour_augmenter_la_vitesse/) , 2023-12-24-0911
```
J'ai construit quelque chose en utilisant Langchain, Chromadb et LLM d'Openai. J'utilise également les intégres d'Openai
, l'ADA-002.
Cependant, les réponses sont très lentes. Pour les petites questions complexes, il faut 20 à 30 secondes po
ur répondre.
La taille du VectorStore est de 62 Mo seulement mais elle est toujours très lente.
Je voulais demander si l
'utilisation d'une instance AWS EC2 G3 avec des GPU augmentera ou non la vitesse? Ou toute autre solution basée sur le c
loud.
De plus, y a-t-il d'autres façons? J'explore également VLLM pour son paramètre de taille parallèle du tenseur.
Que
lle est la meilleure approche que je puisse adopter pour augmenter la vitesse des réponses?

Ps. Je suis un débutant dan
s ce domaine, désolé si j'ai écrit quelque chose de stupide ici :)

Traduit et reposté à partir de la publication 15rpug
k de la communauté langchain. Pour retrouver la publication originale, insérez l'id de la publication après 'reddit.com/
'
```
---

     
 
all -  [ [Langchain] Quel est le meilleur VectorStore pour auto-hoster vos indices vectoriels? ](https://www.reddit.com/r/redditenfrancais/comments/18nnse7/langchain_quel_est_le_meilleur_vectorstore_pour/) , 2023-12-24-0911
```
Je sais que Pinecone est le plus simple, mais sur le niveau libre, ils suppriment vos index après 7 jours. Quel magasin 
vectoriel à Langchain prend en charge la sauvegarde d'un index localement afin que vous puissiez tirer des vecteurs enre
gistrés comme Pinecone? J'ai essayé le chroma, mais cela ne semble pas avoir cette fonctionnalité de ce que je peux dire
. Au lieu de retirer de la conduite Persiste, il passera un appel API pour rétroser les mêmes intérêts.

Traduit et repo
sté à partir de la publication 12ia7nc de la communauté langchain. Pour retrouver la publication originale, insérez l'id
 de la publication après 'reddit.com/'
```
---

     
 
all -  [ [Langchain] Quel modèle d'intégration utilisez-vous les gars? ](https://www.reddit.com/r/redditenfrancais/comments/18nnos2/langchain_quel_modèle_dintégration_utilisezvous/) , 2023-12-24-0911
```
J'essaie de tester plus de modèles d'intégration et je me demande ce que cette communauté utilise ...

Je sais que cela 
'peut varier en fonction du cas d'utilisation', donc dans ce cas, veuillez partager le modèle et le cas d'utilisation co
nnexe.

Actuellement, j'utilise principalement BGE-GARD-V1.5 ou Instructor-XL ...

(intéressé par l'encodeur BI et l'enc
odeur croisé)

Merci im avance !!!

Traduit et reposté à partir de la publication 1816mb5 de la communauté langchain. Po
ur retrouver la publication originale, insérez l'id de la publication après 'reddit.com/'
```
---

     
 
all -  [ Summary of long PDFs ](https://www.reddit.com/r/LangChain/comments/18nlcpm/summary_of_long_pdfs/) , 2023-12-24-0911
```
Hey people,    


I'm new to langchain and have a few questions.    


If I want to summarize large PDFs (e.g. long scie
ntific texts) in an easy-to-understand language, does a vector-based database make sense? Or can I just split the text u
p and then have it summarized piece by piece and create a summary at the end?   


Is the context of the entire PDF pres
erved in both versions?  


I hope you understand my question and can help me. 
```
---

     
 
all -  [ Which framework should I use to build Question-Answering system ? ](https://www.reddit.com/r/LocalLLaMA/comments/18nk6sv/which_framework_should_i_use_to_build/) , 2023-12-24-0911
```
Hi

I currently build a QA system using RAG. I have experience with Langchain and using it to build a POC. But when I st
arted to apply it for production and make more custom to fit with my ideal, I found it too difficult to control the fram
ework, those chains, agents, and prompts are too complicated to control. 

Can you recommend any framework that is more 
controllable? or Should I build from scratch?
```
---

     
 
all -  [ Getting general information over a CSV ](https://www.reddit.com/r/LangChain/comments/18nccz3/getting_general_information_over_a_csv/) , 2023-12-24-0911
```
Hello everyone. I'm new to Langchain and I made a chatbot using Next.js (so the Javascript library) that uses a CSV with
 soccer info to answer questions. Specific questions, for example 'How many goals did **Haaland** score?' get answered p
roperly, since it searches info about Haaland in the CSV (I'm embedding the CSV and storing the vectors in Pinecone).

T
he problem starts when I ask general questions, meaning questions without keywords. For example, 'who made more assists?
', or maybe something extreme like 'how many rows are there in the CSV?'. It completely fails. I'm guessing that it only
 gets the relevant info from the vector db based on the query and it can't answer these types of questions.

&#x200B;

I
'm using `ConversationalRetrievalQAChain` from Langchain

    chain.ts
    
    /* create vectorstore */
      const vec
torStore = await PineconeStore.fromExistingIndex(
        new OpenAIEmbeddings({}),
        {
          pineconeIndex,
 
         textKey: 'text',
        }
      );
    
      return ConversationalRetrievalQAChain.fromLLM(
        model,
  
      vectorStore.asRetriever(),
        { returnSourceDocuments: true }
      );

And using it in my API in Next.js.

 
   route.ts
    
    const res = await chain.call({
        question: question,
        chat_history: history
          
.map((h) => {
            h.content;
          })
          .join('\n'),
      });

&#x200B;

Any suggestions are welcom
ed and appreciated. Also feel free to ask any questions. Thanks in advance
```
---

     
 
all -  [ Identify a Langchain like project like in this video clip ](https://www.reddit.com/r/Langchaindev/comments/18nbrvm/identify_a_langchain_like_project_like_in_this/) , 2023-12-24-0911
```
Can you Advise on finding the open source projects like Azure Cognitive Search + GPT, maybe using Langchain??

This 20 s
econd clip shows exactly the functionality we're looking for  [https://youtube.com/clip/Ugkx4Bx61tbWTnuvDmfEecj2R-msM2AI
3kWA?si=tT7HkGz\_m2wzIeL\_](https://youtube.com/clip/Ugkx4Bx61tbWTnuvDmfEecj2R-msM2AI3kWA?si=tT7HkGz_m2wzIeL_)
```
---

     
 
all -  [ Looking for tutorial on local JS LLMs ](https://www.reddit.com/r/LangChain/comments/18nb0t3/looking_for_tutorial_on_local_js_llms/) , 2023-12-24-0911
```
Hi all,

Are there any resources on using a local JS copy of an LLM (namely Flan-T5) with langchainJS (especially if usi
ng Xenova’s transformers.js for the LLM inference)? I’ve been looking for resources on using the two libraries for a loc
al JS project but information is sparse.
```
---

     
 
all -  [ Integrating LlamaIndex with Langchain. ](https://www.reddit.com/r/LangChain/comments/18n65if/integrating_llamaindex_with_langchain/) , 2023-12-24-0911
```
Hey guys, I am wondering if you know of good guides to go about doing this \^

And would it result in a better memory re
trieval system? (I've heard LlamaIndex is better for RAG systems?) Or would you build everything in Langchain? My system
 will involve a fine-tuned model, external knowledge, plus I am trying to figure out how to store conversation history i
n the vector db for memory retrieval. Eventually I'll add more components like speech-to-text software.. is this support
ed with langchain? Any guidance on this is greatly appreciated.

Right now I'm using Flowise which is built on top of La
ngChain, but haven't found any info on integrating LlamaIndex with Flowise specifically.
```
---

     
 
all -  [ Build your own GPT 5 with Mistral 7B and LangChain ](https://youtu.be/Bc-OSax1G2o) , 2023-12-24-0911
```
Can you develop a latest, your own GPT model with the latest release of mistral 7-b. in this video they talk about using
 Retrieval augmented generation and mistral 7-b. what are your guys thought?
```
---

     
 
all -  [ PGVector - Table ](https://www.reddit.com/r/LangChain/comments/18n2an2/pgvector_table/) , 2023-12-24-0911
```
i was using OPENAIEmbedding before but now i changed it to AzureOpenAIEmbedding but re-building the vector db takes a ve
ry long time. is there anyway i can drop the existing table and re-build it from scratch? although i already have `pre_d
elete_collection=True`

I am using 0.0.348 version 
```
---

     
 
all -  [ Text pre-processing before embedding ](https://www.reddit.com/r/LangChain/comments/18n1741/text_preprocessing_before_embedding/) , 2023-12-24-0911
```
I am trying to create a QNA chatbot with OpenAI API, after using RecursiveCharacterTextSplitter,  texts are coming with 
**'\\n'** Should I be worried? because I have to upsert it into the Pinecone database, and also if there is any preproce
ssing needed before upserting please tell me.. this is my first project

these are the texts: 

`['The\ncow,\na\ngentle\
nherbivorous\nmammal\nof\nthe\nBovidae\nfamily,\nis\na\nvital\ncontributor\nto\nagriculture\nand\nhuman\nsustenance\nglo
bally.\nCharacterized\nby\nits\nlarge\nbody,\ncloven\nhooves,\nand\ndistinctively\npatterned\nhide,\ncows\nprimarily\nse
rve\nas\nsources\nof\nmilk,\nagriculture,livestock,\nfarming\nand\nleather.\nBos\ntaurus,\nthe\nmost\ncommon\nspecies,\n
exists\nin\nvarious\nbreeds,']`

my code : 

    loader = PdfReader('cow.pdf')
    text = ''
    for i,page in enumerate
 (loader.pages):
        content = page.extract_text()
        if content:
            text += content
    
    text_spl
itter = RecursiveCharacterTextSplitter(
        separators=['\n\n', '\n', ' '],
        chunk_size = 400,
        chunk_
overlap  = 20,
        length_function = len,
    )
    
    texts = text_splitter.split_text(text)
    print(texts)
   
 print(len(texts))
    
    embeddings = OpenAIEmbeddings(model='text-embedding-ada-002')
    vectorstore = Pinecone.fro
m_texts(texts,embeddings,index_name=PINECONE_INDEX)

&#x200B;
```
---

     
 
all -  [ How can I modify the context retrieved by RetrievalQA Chain? ](https://www.reddit.com/r/LangChain/comments/18n0obz/how_can_i_modify_the_context_retrieved_by/) , 2023-12-24-0911
```
Guys, I'm in a pickle. I'm evaluating my RAG using Trulens and this takes in the RetrievalQA chain. But I want to modify
 the context to add more information to it say from the metadata. Is it possible to modify the context retrieved by Retr
ievalQA to add information from metadata and perhaps add more info to the context?
```
---

     
 
MachineLearning -  [ [D] github repositories for ai web search agents ](https://www.reddit.com/r/MachineLearning/comments/18dhtm4/d_github_repositories_for_ai_web_search_agents/) , 2023-12-24-0911
```
Do you know of any github repositories that either help with building a web search ai agent or that has a good one?

git
hub repositories that I saw so far but have not yet tried :

- langchain (the WebResearchRetriever and weblangchain for 
example (have not tried either) )
- autogpt
- gpt-researcher

[Edit: changed researchgpt to gpt-researcher]
```
---

     
 
MachineLearning -  [ [P] flex-prompt: a flexible prompt rendering engine that ensures you'll never exceed your LLM's cont ](https://www.reddit.com/r/MachineLearning/comments/18d581q/p_flexprompt_a_flexible_prompt_rendering_engine/) , 2023-12-24-0911
```
When working with LLMs, I frequently experience *token agony*.

[Error: This model's maximum context length is 4097 but 
you are trying to push in all of War and Peace, you imbecile](https://preview.redd.it/nldj0qva4s4c1.png?width=1348&forma
t=png&auto=webp&s=b16af79d83f329db1b77b32ed621f0138d7cc04d)

Perhaps you've experienced it too! The issue is particularl
y pronounced with retrieval augmented pipelines, since you have potentially quite a large set of documents which you cou
ld perhaps include in the prompt if only you knew how big it could be.

I got tired of hacking around this headache, so 
I wrote `flex-prompt` to address it. I wish I didn't have to. Perhaps someone can point me to a better solution! But I c
ouldn't find one, so alas, here it is.

`flex-prompt` provides a basic layout and component model to help you describe h
ow you want the pieces of your prompt to grow and shrink and a token-aware renderer which renders your prompt to fit you
r model's window.

[Github](https://github.com/queerviolet/flex-prompt), [Intro to flex prompt colab](https://colab.rese
arch.google.com/github/queerviolet/flex-prompt/blob/main/doc/intro_to_flex_prompt.ipynb)

# Quick examples

You can just
 `render(Flex(...))`, and flex prompt will fit the prompt into the context window, and tell you how many tokens are left
 over for the response:

    from flex_prompt import render, Flex, Expect
    rendered = render(
        Flex([
        
  'Given the text, answer the question.',
          '--Text--',
          WAR_AND_PEACE,
          '--End Text--',
     
     'Question: What's the title of this text?',
          'Answer:', Expect()
        ], join='\n'),
        model='tex
t-davinci-002')
    
    # rendered.output is the string to send to the model
    # rendered.max_response_tokens is how 
many tokens you can
    #   request in response without exceeding the model's context window
    print(rendered.output, 
rendered.max_response_tokens)

More typically, you'll want to define a prompt which takes parameters. To do this, you ca
n create a class (probably a dataclass) which derives `Flexed`:

    from flex_prompt import Flexed, Expect
    from dat
aclasses import dataclass
    
    @dataclass
    class Ask(Flexed):
      text: str
      question: str
      answer: s
tr | Expect = Expect()
      instruct: str = 'Given a text, answer the question.'
    
      flex_join = '\n' # yielded 
items will be joined by newlines
      def content(self, _ctx):
        if self.instruct:
          yield 'Given the tex
t, answer the question.'
          yield ''
        yield '-- Begin Text --'
        # note: we're using `Flex` here jus
t to attach a flex_weight
        # to the text, telling the renderer we'd like more space for the
        # text than a
nything else.
        yield Flex([self.text], flex_weight=2)
        yield '-- End Text --'
        yield 'Question: ', 
self.question
        yield 'Answer: ', self.answer

The renderer works much as you might expect. You can \`yield\` anyt
hing which you can pass to the top-level render function, including other components, creating a whole tree.

Note that 
the component above can be used to render both the actual prompt and examples. Examples simply have an `answer`. This is
 useful for experimenting with different ways of structuring a prompt while ensuring that all the examples we present to
 the LLM are in the same format.

# LangChain and Haystack Integrations

Flex prompt doesn't really care how you execute
 your prompt. For convenience, `render(model=)` does accept both LangChain and Haystack models:

    ask_tolstoy = Ask(t
ext=WAR_AND_PEACE, question='Who wrote this?')
    
    # Using LangChain
    from langchain.llms import OpenAI
    lc_l
lm = OpenAI()
    rendering = render(ask_tolstoy, model=lc_llm)
    print(lc_llm(rendering.output, max_tokens=rendering.
max_response_tokens))
    
    
    # Using Haystack
    from haystack.nodes import PromptModel
    
    hs_llm = Prompt
Model(model_name_or_path='text-davinci-002', api_key=os.environ['OPENAI_API_KEY'])
    rendering = render(ask_tolstoy, m
odel=hs_llm)
    print(hs_llm.invoke(rendering.output, max_tokens=rendering.max_response_tokens))
    

# Is it worth it
?

As models grow larger and larger context windows, I've asked myself whether this is worth it. Won't context sizes eve
ntually big enough to put in everything we might want without worry?

One response: 'everything I might want' is a very,
 very big set, plausibly bigger than any window size we're going to see soon.

Another: being able to do this kind of to
ken accounting is useful even if we don't completely fill context windows. For example, we might be able to augment our 
prompt with examples, documents, and tips. How much space should we allocate to each? The answer might well be model-dep
endent. How do we figure it out?

Flex prompt's output, a `Rendering` object, actually holds the entire component tree. 
You can look through the object to see how many tokens were allocated to each child. This is currently very manual, but 
it does provide the bedrock infrastructure to e.g. run tests to discover the optimal balance of augmented data for a giv
en prompt and model.

Additionally, the right admixture (and for that matter, the right *phrasing*) may well be model-de
pendent. Flex prompt currently provides only very limited model-specific rendering (you can look at [`ctx.target`](https
://ctx.target), but it doesn't tell you much), but there's no reason that can't be significantly improved. At the extrem
e limit is prompt *erasure*, where we fine-tune a model to require no or minimal instructions/examples for a given set o
f prompts. Flex prompt can enable transitions like this with no changes to the pipelines themselves: you'd still use the
 same prompt components, they'd just render differently if the target is a fine-tuned model vs. a generic one.

# Status
 & Future Work

Flex prompt is very much in early development. I would love to hear if and how people find it useful, an
d would love input and contributions!

Some things I'd like to tackle in the future:

* **Rendering message lists.** Fle
x prompt currently only renders strings, though it's set up to be able to render any type of output. Message histories b
asically grow without bound, so supporting this seems like a no-brainer.
* **Pagination**. If your rendering overflows (
as above, where we're trying to stuff *the entirety of war and peace* into a prompt), flex prompt will clip the offendin
g pieces to fit. But there's currently no way to get 'the next page'. But the `Rendering` actually retains enough inform
ation to do this! It would be great to be able to call `render(...).pages()` to get the sequence of prompts as we 'scrol
l' whatever has overflowed. This is medium-hanging fruit—a little tricky because we do have to descend the tree of rende
rings to find the exact one(s) which overflowed and then update only those.
* **Token accounting.** As mentioned above, 
you can currently grovel around in `Rendering` and look at the pieces of the prompt. This would be more useful if it wer
e a little easier, e.g. if you could use `rendering[Examples]` to find all the parts rendered by the `Examples` componen
t, or `rendering['advice']` to find all the parts which are tagged (somehow) as 'advice'. The use case here is prompt op
timization: discovering the optimal number or percentage of tokens to allot to each thing we might want to drop into the
 prompt.
* **More integrations.** Currently, flex prompt only supports OpenAI models. You can register your own target f
inders, but it would be great to have more support out of the box. This is mostly a matter of digging around and finding
 the tokenizers and window sizes for common models, and then writing the appropriate target finders. Contributions very 
welcome!
* **Model tuning.** As mentioned above, the rendering context could provide a mechanism for fetching model-spec
ific parameters. The basic idea is that `ctx[param]` will evaluate `param` against the context, and then we can define s
ome parameter types which load their model-specific values from *gestures vaguely* somewhere.

Thanks for reading!

* [F
lex prompt Github](https://github.com/queerviolet/flex-prompt)
* [Intro to flex prompt colab](https://colab.research.goo
gle.com/github/queerviolet/flex-prompt/blob/main/doc/intro_to_flex_prompt.ipynb)
* [My website](https://ashi.io). *shame
less plug: I have a lot of engineering experience and a bit of machine learning experience and* [*I am currently looking
 for a job*](https://ashi.io/resume.pdf)
```
---

     
 
MachineLearning -  [ [D] Working on RAG? You should be evaluating its performance and we've built a way to do that. ](https://www.reddit.com/r/MachineLearning/comments/18ciet5/d_working_on_rag_you_should_be_evaluating_its/) , 2023-12-24-0911
```
Check out our new open-source tool, Tonic Validate: [https://www.tonic.ai/validate](https://www.tonic.ai/validate)  


W
e've also been using the tool to evaluate different RAG tools out there. The latest post on LangChain vs Haystack is ava
ilable here:  [https://www.tonic.ai/blog/rag-evaluation-series-validating-the-rag-performance-of-langchain-vs-haystack](
https://www.tonic.ai/blog/rag-evaluation-series-validating-the-rag-performance-of-langchain-vs-haystack)

&#x200B;

Let 
us know what you think and if you're working on a RAG project, we'd love to hear about it! How are you measuring your RA
G system performance?
```
---

     
 
MachineLearning -  [ [R] LLMs for structured data? ](https://www.reddit.com/r/MachineLearning/comments/185ei6v/r_llms_for_structured_data/) , 2023-12-24-0911
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

     
 
MachineLearning -  [ [P] A new way of interacting with Hacker News ](https://www.reddit.com/r/MachineLearning/comments/183n6h7/p_a_new_way_of_interacting_with_hacker_news/) , 2023-12-24-0911
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

     
 
MachineLearning -  [ [Discussion] Is it possible to built a Multi-LLM Assistant? ](https://www.reddit.com/r/MachineLearning/comments/182uuwp/discussion_is_it_possible_to_built_a_multillm/) , 2023-12-24-0911
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

     
 
deeplearning -  [ Unlocking the Power of Language: How LangChain Transforms Data Analysis and More ](https://www.reddit.com/r/deeplearning/comments/18l788y/unlocking_the_power_of_language_how_langchain/) , 2023-12-24-0911
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

     
 
deeplearning -  [ [D] Mastering Chain Composition with LangChain Expression Language (LCEL) ](https://www.reddit.com/r/deeplearning/comments/18i0wot/d_mastering_chain_composition_with_langchain/) , 2023-12-24-0911
```
In the intricate landscape of modern software development, orchestrating complex sequences of actions seamlessly poses a
 significant challenge. Enter LangChain Expression Language (LCEL), a groundbreaking declarative approach designed to re
volutionize the composition of chains within software architecture.

Link: [https://medium.com/ai-artistry/mastering-cha
in-composition-with-langchain-expression-language-lcel-2d5041fb0cbd](https://medium.com/ai-artistry/mastering-chain-comp
osition-with-langchain-expression-language-lcel-2d5041fb0cbd)  
```
---

     
 
deeplearning -  [ [D] Utilizing Multimodal LLM for Extracting Tables and Images LangChain+LlamaIndex’s Role in Semi-St ](https://www.reddit.com/r/deeplearning/comments/185vd56/d_utilizing_multimodal_llm_for_extracting_tables/) , 2023-12-24-0911
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

     
